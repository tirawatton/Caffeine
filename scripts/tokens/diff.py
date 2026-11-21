#!/usr/bin/env python3
"""Token diff gate: a Figma export vs the generated iOS and Android files, both modes.

Usage: python3 scripts/tokens/diff.py [--export PATH]
Prints one line per difference, then the total. Exit 0 only when the total is 0.
Re-export Figma (use_figma read-only) to a fresh file and pass it with --export before a release gate;
the default compares against scripts/tokens/figma-export.json.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    ANDROID_THEME, EXPORT, IOS_COLORS, IOS_SWIFT, alpha3, camel, canonical_from_export, load_json,
)


def ios_color(name: str):
    p = IOS_COLORS / f"{name}.colorset" / "Contents.json"
    if not p.exists():
        return None
    data = json.loads(p.read_text())
    out = {}
    for entry in data["colors"]:
        mode = "dark" if entry.get("appearances") else "light"
        c = entry["color"]["components"]
        out[mode] = {"hex": "#" + "".join(c[k][2:].upper() for k in ("red", "green", "blue")),
                     "alpha": alpha3(float(c["alpha"]))}
    return out


def kotlin_colors():
    text = (ANDROID_THEME / "CaffeineColors.kt").read_text()
    out = {}
    for mode in ("dark", "light"):
        block = re.search(rf"val {mode} = CaffeineColors\((.*?)\n        \)", text, re.S).group(1)
        out[mode] = dict(re.findall(r"(\w+) = Color\((0x[0-9A-F]{8})\)", block))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--export", type=Path, default=EXPORT)
    args = ap.parse_args()
    fig = canonical_from_export(load_json(args.export))
    diffs: list[str] = []
    swift = IOS_SWIFT.read_text()
    kc = kotlin_colors()
    kdim = (ANDROID_THEME / "CaffeineDimens.kt").read_text()
    ktype = (ANDROID_THEME / "CaffeineType.kt").read_text()

    # colours
    names_ios = {p.name[:-9] for p in IOS_COLORS.glob("*.colorset")}
    for extra in sorted(names_ios - set(fig["colors"])):
        diffs.append(f"ios extra colour set: {extra}")
    for extra in sorted(set(kc["dark"]) - {camel(n) for n in fig["colors"]}):
        diffs.append(f"android extra colour: {extra}")
    for name, modes in fig["colors"].items():
        ic = ios_color(name)
        if ic is None:
            diffs.append(f"ios missing colour set: {name}")
        if f'Color("Night/{name}")' not in swift:
            diffs.append(f"swift missing Color.night.{camel(name)}")
        for mode in ("dark", "light"):
            want = modes[mode]
            if ic is not None and (ic[mode]["hex"] != want["hex"] or ic[mode]["alpha"] != want["alpha"]):
                diffs.append(f"ios {name} {mode}: {ic[mode]} != figma {want['hex']} {want['alpha']}")
            got = kc[mode].get(camel(name))
            if got != want["argb"]:
                diffs.append(f"android {camel(name)} {mode}: {got} != figma {want['argb']}")

    # dimensions
    for k, v in fig["dims"].items():
        prefix, key = k.split("/", 1)
        sid = f"s{key}" if prefix == "space" else camel(key)
        if not re.search(rf"static let {re.escape(sid)}: CGFloat = {v}\b", swift):
            diffs.append(f"swift dimension {k} != {v}")
        kid = f"space{key}" if prefix == "space" else camel(prefix + " " + key)
        if not re.search(rf"val {re.escape(kid)} = {v}\.dp", kdim):
            diffs.append(f"android dimension {k} != {v}")

    # text styles
    for name, s in fig["text"].items():
        key = name.split("/", 1)[1]
        ident = camel(key) if name.startswith("iOS/") else "data" + camel(key)[:1].upper() + camel(key)[1:]
        m = re.search(rf"static let {ident} = CaffeineTextStyle\(size: ([\d.]+), lineHeight: ([\d.]+),.*?uppercase: (\w+)", swift)
        if not m or float(m.group(1)) != s["size"] or float(m.group(2)) != s["lineHeight"] or (m.group(3) == "true") != s["uppercase"]:
            diffs.append(f"swift text style {name}")
        m = re.search(rf"val {ident} = TextStyle\(.*?fontSize = ([\d.]+)\.sp, lineHeight = ([\d.]+)\.sp, letterSpacing = \((-?[\d.]+)\)\.em", ktype)
        if not m or float(m.group(1)) != s["size"] or float(m.group(2)) != s["lineHeight"] or abs(float(m.group(3)) - s["letterSpacingPercent"] / 100) > 1e-9:
            diffs.append(f"android text style {name}")
        if s["uppercase"] and f'"{ident}"' not in ktype:
            diffs.append(f"android uppercase flag {name}")

    for d in diffs:
        print(d)
    print(len(diffs))
    return 0 if not diffs else 1


if __name__ == "__main__":
    sys.exit(main())
