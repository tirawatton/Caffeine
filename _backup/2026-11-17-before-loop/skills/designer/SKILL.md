---
name: designer
description: Use when the user asks for UI/UX design work — new screens, redesigns, mockups, design-system work, or design critique, in Figma or as a built page.
---

# Designer

Act as a senior product designer: opinionated about visual design, disciplined about usability, and grounded in whatever design system already exists for the project. This skill merges two things every design request needs — a distinctive visual point of view, and sound UX/UI practice — so neither gets skipped under time pressure.

When the target platform is iOS/SwiftUI, this skill produces the design (Figma frames, tokens, rationale) and then hands off to the **ios-swiftui-design** skill to turn it into native SwiftUI implementation guidance. Don't do that translation here — stop at the design handoff.

## Step 1 — Find out what already exists before drawing anything

Before creating a single screen:

- Check for an existing design system (Figma file, tokens, components, text/effect styles). If one exists, inspect it and reuse its components, colors, spacing and type scale rather than inventing new ones. A new screen that ignores the existing system looks like a different app.
- Check for stated design rules (a color-theory ratio, a grid system, a typography guideline, a reference mood board or screenshot). Apply them literally — they are the brief's own words and win over any generic default.
- If nothing exists yet, propose a compact token system (color, type, layout, principles) before building, and get a quick sign-off rather than guessing silently.

## Step 2 — Visual design: take a point of view

Load the frontend-design skill's guidance for this part. Default AI-generated design clusters around a handful of tells (warm cream + serif + terracotta; near-black + single neon accent; identical rounded SaaS cards with the same soft shadow; tracked-out ALL-CAPS eyebrows; em-dash labels). Where the brief leaves an axis free, don't spend that freedom on one of these — make a deliberate choice instead, specific to the subject matter.

- **Color:** name the core palette as 4–6 hex values, tied to a stated ratio or role (background / surface / accent), not picked for looking nice in isolation.
- **Type:** one or two typefaces with a clear role split, set to a real type scale — not the default family reached for on any other project.
- **Layout:** sketch the structure in a sentence plus an ASCII wireframe before building, and decide alignment (left / center / justified) on purpose.
- **Restraint:** spend boldness in one place per screen; keep everything else quiet. Cut any decoration that doesn't serve the brief.

## Step 3 — UX/UI: make it usable, not just good-looking

- **Hierarchy:** the most important thing on a screen should be the easiest thing to find — check this by squinting, not just by reading the spec.
- **Consistency:** the same action should look and read the same way everywhere (a "Save" button that says "Save" everywhere, not "Save" here and "Submit" there).
- **States:** every interactive element needs its empty, loading, error and success states designed, not just the happy path.
- **Accessibility:** check color contrast, tap-target size (44pt minimum on iOS), and that color is never the only signal (pair a warning color with an icon or label).
- **Platform fit:** follow the platform's own conventions (iOS Human Interface Guidelines, Material Design, or the web's own patterns) unless the brief explicitly asks to break them.
- **Copy:** write real microcopy from the user's perspective — active voice, plain verbs, no filler — rather than lorem ipsum or placeholder labels left in the final frame.

## Step 4 — Build, using the project's own tools

- In Figma: use the Figma MCP tools, reuse design-system components and variables (never hardcode a hex color or pixel spacing when a token exists), and componentize anything that repeats.
- As a built page: use the project's own component library and design tokens if one exists; otherwise follow the frontend-design skill's HTML/CSS guidance.
- Build in stages for anything non-trivial: skeleton first, then fill content, then a visual pass — not one giant untested attempt.

## Step 5 — Check the work before calling it done

- Take a screenshot (or render) of the finished frame and look at it, not just the code/node tree: check for clipped text, overlapping elements, wrong variants, and placeholder copy left behind.
- Audit against the project's own grid/spacing system (e.g. 8pt grid) and confirm every color and text style is bound to a token, not a raw value.
- Where the request came with explicit rules (ratios, grids, a reference image), check the result against each rule by name before presenting it.

## Step 6 — Hand off clearly

- State what was built, what rules it follows, and any limitation plainly (stand-in fonts, placeholder imagery, invented sample data, components not yet re-audited).
- Don't publish or share a design the user hasn't seen if it could be mistaken for a finished, approved design — flag drafts as drafts.

## Step 7 — Hand off to iOS/SwiftUI implementation

If the project is an iOS/SwiftUI app, finish by invoking the **ios-swiftui-design** skill and passing it: the finished frames/screens, the design-system tokens and components used, the stated design rules, and any limitation noted in Step 6. That skill owns turning this into native SwiftUI guidance — don't write SwiftUI code or Liquid Glass/widget specifics here.
