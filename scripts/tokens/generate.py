#!/usr/bin/env python3
"""Generate Caffeine design tokens for iOS and Android.

Usage:
  python3 scripts/tokens/generate.py                 # figma-export.json -> tokens.json -> app files
  python3 scripts/tokens/generate.py --export PATH   # use another Figma export

Fails with "missing token: night/<name>" (exit 2) when a required token is absent. Nothing is
written in that case: every file is rendered in memory first, then all files are replaced.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    ANDROID_THEME, DEPRECATED, EXPORT, HEADER, IOS_COLORS, IOS_SWIFT, REQUIRED_COLORS,
    REQUIRED_DIMS, REQUIRED_TEXT, ROOT, TOKENS_JSON, MissingToken, alpha3, argb, byte, camel,
    hex6, load_json,
)

SWIFT_WEIGHT = {"Regular": ".regular", "Medium": ".medium", "Semibold": ".semibold", "Bold": ".bold", "Heavy": ".heavy"}
KOTLIN_WEIGHT = {"Regular": "FontWeight.Normal", "Medium": "FontWeight.Medium", "Semibold": "FontWeight.SemiBold",
                 "Bold": "FontWeight.Bold", "Heavy": "FontWeight.ExtraBold"}
# Dynamic Type anchor for each Figma style (sizes match the iOS defaults at the Large size).
RELATIVE_TO = {
    "iOS/Large Title": ".largeTitle", "iOS/Title 2": ".title2", "iOS/Title 3": ".title3",
    "iOS/Headline": ".headline", "iOS/Body": ".body", "iOS/Subhead": ".subheadline",
    "iOS/Subhead Regular": ".subheadline", "iOS/Footnote": ".footnote",
    "iOS/Footnote Regular": ".footnote", "iOS/Caption": ".caption", "iOS/Caption Regular": ".caption",
    "iOS/Caption Upper": ".caption", "Data/Display": ".largeTitle", "Data/Mono Caption": ".caption",
    "Data/Mono Subhead": ".subheadline",
}


def build_tokens(export: dict) -> dict:
    colors = {}
    for full, (dark, da, light, la, scopes) in export["colors"].items():
        colors[full.split("/", 1)[1]] = {
            "figma": full, "scopes": scopes.split("|"), "deprecated": full.split("/", 1)[1] in DEPRECATED,
            "dark": {"hex": hex6(dark), "alpha": alpha3(dark[3]), "argb": argb(dark), "alias": da or None},
            "light": {"hex": hex6(light), "alpha": alpha3(light[3]), "argb": argb(light), "alias": la or None},
        }
    for name in REQUIRED_COLORS:
        if name not in colors:
            raise MissingToken(f"night/{name}")
    for name in REQUIRED_DIMS:
        if name not in export["dims"]:
            raise MissingToken(name)
    text = {}
    for name, fam, style, size, lh, ls, case in export["ts"]:
        text[name] = {"family": fam, "weight": style, "size": size, "lineHeight": lh,
                      "letterSpacingPercent": ls, "uppercase": case == "UPPER"}
    for name in REQUIRED_TEXT:
        if name not in text:
            raise MissingToken(name)
    effects = {}
    for name, layers in export["es"]:
        effects[name] = [
            {"type": "dropShadow", "x": l[1], "y": l[2], "blur": l[3], "spread": l[4], "color": l[5]}
            if l[0] == "shadow" else {"type": "backgroundBlur", "radius": l[1]}
            for l in layers
        ]
    return {
        "$schema": "caffeine-tokens/1",
        "source": export["source"],
        "colors": dict(sorted(colors.items())),
        "dimensions": dict(export["dims"]),
        "text": text,
        "effects": effects,
    }


# ---------- iOS ----------

def ios_colorset(tok: dict) -> str:
    def comp(mode):
        h = tok[mode]["hex"]
        return {"color-space": "srgb", "components": {
            "red": "0x" + h[1:3], "green": "0x" + h[3:5], "blue": "0x" + h[5:7], "alpha": tok[mode]["alpha"]}}
    data = {
        "colors": [
            {"idiom": "universal", "color": comp("light")},
            {"idiom": "universal", "appearances": [{"appearance": "luminosity", "value": "dark"}], "color": comp("dark")},
        ],
        "info": {"author": "scripts/tokens/generate.py", "version": 1},
        "properties": {"localizable": False},
    }
    return json.dumps(data, indent=2) + "\n"


def swift_file(t: dict, src: str) -> str:
    L = [f"// {HEADER.format(src=src)}", "// Colours live in Resources/Colors.xcassets/Night (Any = Light, Dark = Dark).",
         "import SwiftUI", "", "/// `Caffeine / Night` semantic colours. Use `Color.night.<token>`.",
         "struct NightPalette: Sendable {"]
    for name, tok in t["colors"].items():
        dep = '    @available(*, deprecated, message: "Legacy hero token, unused since v5")\n' if tok["deprecated"] else ""
        L.append(f'{dep}    /// {tok["figma"]} · Dark {tok["dark"]["hex"]} {tok["dark"]["alpha"]} · Light {tok["light"]["hex"]} {tok["light"]["alpha"]}')
        L.append(f'    let {camel(name)} = Color("Night/{name}")')
    L += ["}", "", "extension Color {", "    static let night = NightPalette()", "}", ""]
    groups = {"space": "Space", "radius": "Radius", "size": "Size", "layout": "Layout"}
    for prefix, enum in groups.items():
        L.append(f"/// `Caffeine / Dimensions` {prefix}/*")
        L.append(f"enum {enum} {{")
        for k, v in t["dimensions"].items():
            if k.split("/")[0] != prefix:
                continue
            key = k.split("/", 1)[1]
            ident = f"s{key}" if prefix == "space" else camel(key)
            L.append(f"    static let {ident}: CGFloat = {v}")
        L.append("}")
        L.append("")
    L += ["/// One Figma text style. Size, line height and tracking are at the default (Large) Dynamic Type size.",
          "struct CaffeineTextStyle: Sendable {",
          "    let size: CGFloat", "    let lineHeight: CGFloat", "    let weight: Font.Weight",
          "    /// Tracking in points (Figma letter spacing % x size).", "    let tracking: CGFloat",
          "    let uppercase: Bool", "    let monospaced: Bool", "    let relativeTo: Font.TextStyle", "",
          "    /// System font (SF Pro / SF Mono) that scales with Dynamic Type from `relativeTo`.",
          "    /// Data/Display has no system size: it returns a fixed 48pt; wrap the size in `@ScaledMetric(relativeTo: .largeTitle)`.",
          "    var font: Font {",
          "        if size == 48 {",
          "            return Font.system(size: size, weight: weight).monospacedDigit()",
          "        }",
          "        return Font.system(relativeTo, design: monospaced ? .monospaced : .default, weight: weight)",
          "    }",
          "}", "",
          "/// `iOS/*` and `Data/*` text styles. Data/Display (48pt) does not match a system size: scale it with",
          "/// `@ScaledMetric(relativeTo: .largeTitle) var size = CaffeineFont.dataDisplay.size` and `.monospacedDigit()`.",
          "enum CaffeineFont {"]
    for name, s in t["text"].items():
        ident = camel(name.split("/", 1)[1]) if name.startswith("iOS/") else "data" + camel(name.split("/", 1)[1])[:1].upper() + camel(name.split("/", 1)[1])[1:]
        tracking = round(s["size"] * s["letterSpacingPercent"] / 100, 2)
        mono = "true" if s["family"] == "DM Mono" else "false"
        L.append(f'    /// {name}: {s["family"]} {s["weight"]} {s["size"]}/{s["lineHeight"]}, tracking {s["letterSpacingPercent"]}%'
                 + (", uppercase" if s["uppercase"] else "") + (" (DM Mono in Figma = SF Mono in the app)" if mono == "true" else ""))
        L.append(f'    static let {ident} = CaffeineTextStyle(size: {s["size"]}, lineHeight: {s["lineHeight"]}, weight: {SWIFT_WEIGHT[s["weight"]]}, '
                 f'tracking: {tracking}, uppercase: {str(s["uppercase"]).lower()}, monospaced: {mono}, relativeTo: {RELATIVE_TO[name]})')
    L += ["}", "", "/// Effect styles. SwiftUI `shadow(radius:)` takes half the Figma blur.", "enum CaffeineEffect {"]
    for name, layers in t["effects"].items():
        ident = camel(name)
        for i, l in enumerate(layers):
            suffix = "" if len(layers) == 1 else ("Blur" if l["type"] == "backgroundBlur" else "Shadow")
            if l["type"] == "dropShadow":
                L.append(f'    /// {name}: drop shadow x {l["x"]} y {l["y"]} blur {l["blur"]}, colour {l["color"]}')
                L.append(f'    static let {ident}{suffix} = (color: Color.night.shadow, radius: CGFloat({l["blur"]}) / 2, x: CGFloat({l["x"]}), y: CGFloat({l["y"]}))')
            else:
                L.append(f'    /// {name}: background blur {l["radius"]} (use .ultraThinMaterial / Liquid Glass on iOS 26)')
                L.append(f'    static let {ident}{suffix}Radius: CGFloat = {l["radius"]}')
    L += ["}", ""]
    return "\n".join(L)


# ---------- Android ----------

def kotlin_colors(t: dict, src: str) -> str:
    L = [f"// {HEADER.format(src=src)}", "package com.tonapps.caffeine.shared.theme", "",
         "import androidx.compose.runtime.Immutable", "import androidx.compose.ui.graphics.Color", "",
         "/** `Caffeine / Night` semantic colours. Alpha tokens keep their alpha in the ARGB value. */",
         "@Immutable", "data class CaffeineColors("]
    for name, tok in t["colors"].items():
        dep = '    @Deprecated("Legacy hero token, unused since v5")\n' if tok["deprecated"] else ""
        L.append(f"{dep}    val {camel(name)}: Color,")
    L += [") {", "    companion object {"]
    for mode in ("dark", "light"):
        L.append(f"        val {mode} = CaffeineColors(")
        for name, tok in t["colors"].items():
            L.append(f"            {camel(name)} = Color({tok[mode]['argb']}),")
        L.append("        )")
    L += ["    }", "}", ""]
    return "\n".join(L)


def kotlin_dimens(t: dict, src: str) -> str:
    L = [f"// {HEADER.format(src=src)}", "package com.tonapps.caffeine.shared.theme", "",
         "import androidx.compose.ui.unit.dp", "", "/** `Caffeine / Dimensions` (pt in Figma = dp). */",
         "object CaffeineDimens {"]
    for k, v in t["dimensions"].items():
        prefix, key = k.split("/", 1)
        ident = f"space{key}" if prefix == "space" else camel(prefix + " " + key)
        L.append(f"    val {ident} = {v}.dp")
    # shadows
    L += ["", "    /** Effect styles: drop shadow offset / blur in dp (colour = CaffeineColors.shadow). */"]
    for name, layers in t["effects"].items():
        for l in layers:
            base = camel(name)
            if l["type"] == "dropShadow":
                L += [f"    val {base}ShadowY = {l['y']}.dp", f"    val {base}ShadowBlur = {l['blur']}.dp"]
            else:
                L.append(f"    val {base}BlurRadius = {l['radius']}.dp")
    L += ["}", ""]
    return "\n".join(L)


def kotlin_type(t: dict, src: str) -> str:
    L = [f"// {HEADER.format(src=src)}", "package com.tonapps.caffeine.shared.theme", "",
         "import androidx.compose.ui.text.TextStyle", "import androidx.compose.ui.text.font.FontFamily",
         "import androidx.compose.ui.text.font.FontWeight", "import androidx.compose.ui.unit.em", "import androidx.compose.ui.unit.sp", "",
         "/**", " * iOS and Data text styles from Figma. SF Pro is Apple-only, so Android uses the system sans (Roboto)",
         " * and the system monospace at the same sizes and weights (Q-24 may pick a brand font later).",
         " * Styles in [UPPERCASE] must be rendered with `text.uppercase()`.", " */", "object CaffeineType {"]
    upper = []
    for name, s in t["text"].items():
        key = name.split("/", 1)[1]
        ident = camel(key) if name.startswith("iOS/") else "data" + camel(key)[:1].upper() + camel(key)[1:]
        fam = "FontFamily.Monospace" if s["family"] == "DM Mono" else "FontFamily.Default"
        ls = s["letterSpacingPercent"] / 100
        tnum = ', fontFeatureSettings = "tnum"' if name == "Data/Display" else ""
        L.append(f"    /** {name}: {s['family']} {s['weight']} {s['size']}/{s['lineHeight']}, tracking {s['letterSpacingPercent']}% */")
        L.append(f"    val {ident} = TextStyle(fontFamily = {fam}, fontWeight = {KOTLIN_WEIGHT[s['weight']]}, fontSize = {s['size']}.sp, "
                 f"lineHeight = {s['lineHeight']}.sp, letterSpacing = ({ls}).em{tnum})")
        if s["uppercase"]:
            upper.append(ident)
    L.append(f"    val UPPERCASE: Set<String> = setOf({', '.join(chr(34) + u + chr(34) for u in upper)})")
    L += ["}", ""]
    return "\n".join(L)


def render(tokens: dict) -> dict[Path, str]:
    src = f"Figma {tokens['source']['fileKey']}, exported {tokens['source']['exportedAt']}"
    files: dict[Path, str] = {TOKENS_JSON: json.dumps(tokens, indent=2, ensure_ascii=False) + "\n"}
    files[IOS_COLORS / "Contents.json"] = json.dumps(
        {"info": {"author": "scripts/tokens/generate.py", "version": 1}, "properties": {"provides-namespace": True}}, indent=2) + "\n"
    for name, tok in tokens["colors"].items():
        files[IOS_COLORS / f"{name}.colorset" / "Contents.json"] = ios_colorset(tok)
    files[IOS_SWIFT] = swift_file(tokens, src)
    files[ANDROID_THEME / "CaffeineColors.kt"] = kotlin_colors(tokens, src)
    files[ANDROID_THEME / "CaffeineDimens.kt"] = kotlin_dimens(tokens, src)
    files[ANDROID_THEME / "CaffeineType.kt"] = kotlin_type(tokens, src)
    return files


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--export", type=Path, default=EXPORT)
    args = ap.parse_args()
    try:
        tokens = build_tokens(load_json(args.export))
        files = render(tokens)
    except MissingToken as e:
        print(f"missing token: {e}", file=sys.stderr)
        return 2
    # Stage everything, then swap in. The colour set folder is replaced as a whole so removed tokens disappear.
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for path, text in files.items():
            staged = tmp / path.relative_to(ROOT)
            staged.parent.mkdir(parents=True, exist_ok=True)
            staged.write_text(text, encoding="utf-8")
        if IOS_COLORS.exists():
            shutil.rmtree(IOS_COLORS)
        for path in files:
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(tmp / path.relative_to(ROOT), path)
    print(f"generated {len(tokens['colors'])} colours x 2 modes, {len(tokens['dimensions'])} dimensions, "
          f"{len(tokens['text'])} text styles, {len(tokens['effects'])} effects")
    return 0


if __name__ == "__main__":
    sys.exit(main())
