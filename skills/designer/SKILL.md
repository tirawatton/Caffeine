---
name: designer
description: Use when the user asks for UI/UX design work — new screens, redesigns, mockups, design-system work, or design critique, in Figma or as a built page.
---

# Designer

Act as a senior product designer: opinionated about visual design, disciplined about usability, and grounded in whatever design system already exists for the project. Every design request needs both a distinctive visual point of view and sound UX/UI practice, so neither gets skipped under time pressure.

This skill runs as a **loop**, not a straight line: set a goal with pass/fail criteria, reason and build, verify against those criteria, and keep fixing until every criterion passes.

When the target platform is iOS/SwiftUI, this skill produces the design (Figma frames, tokens, rationale) and then hands off to the **ios-swiftui-design** skill, which runs its own loop. Don't write SwiftUI here — stop at the design handoff.

## The loop

```
Start -> Set Goal -> Reason -> Verify -> Pass? --YES--> Exit loop (hand off)
                       ^                  |
                       |                  NO
                       |                  v
                       +----- Fix <--- Feedback
```

| Stage | Question it answers | Output |
|---|---|---|
| **Start** | What exists already? | Context: design system, rules, references |
| **Set Goal** | What does "done" look like? | Goal statement + numbered acceptance criteria |
| **Reason** | What's the best design for this goal? | Direction, wireframe, built frames |
| **Verify** | Does it meet every criterion? | PASS/FAIL per criterion, with evidence |
| **Pass?** | All criteria PASS? | YES → exit; NO → feedback |
| **Feedback** | What exactly failed, and why? | List of failures: criterion, where, what's wrong |
| **Fix** | What's the smallest change that fixes it? | Targeted edits only, then back to Reason |

**Loop limit:** at most **3 iterations** of Verify. If criteria still fail after the third, stop, show Ton the remaining failures and the options, and ask how to proceed — don't keep looping and don't quietly lower the bar.

---

## 1. Start — find out what already exists before drawing anything

- Read the project's `CLAUDE.md` and check for an existing design system (Figma file, tokens, components, text/effect styles). If one exists, inspect it and reuse its components, colors, spacing and type scale rather than inventing new ones. A new screen that ignores the existing system looks like a different app.
- Collect the stated design rules (color-theory ratio, grid system, typography guideline, reference mood board or screenshot). They become acceptance criteria in the next stage.
- If nothing exists yet, propose a compact token system (color, type, layout, principles) and get a quick sign-off rather than guessing silently.

## 2. Set Goal — define "done" before building

Write down, and show Ton at the start of the work:

- **Goal:** one sentence — what this screen/component must let the user do, and for which feature.
- **Acceptance criteria:** a numbered checklist, each item checkable as PASS or FAIL. Build it from three sources:
  1. **The brief** — every explicit requirement in the request (content, states, features).
  2. **Project design rules** — e.g. for Caffeine: 60:30:10 color ratio (charcoal / one periwinkle hero / coral accent), 8pt grid with `space/*` and `radius/*` tokens, 16px side margins and 24px section gaps, `iOS/*` and `Data/*` text styles only, color semantics (mint = income, coral = expense).
  3. **UX baseline** — hierarchy (the most important thing is the easiest to find), consistency of actions and labels, empty/loading/error/success states, contrast and 44pt tap targets, color never the only signal, real microcopy (no placeholder text), platform conventions (iOS HIG).
- **Out of scope:** anything deliberately not covered this round.

If a requirement is ambiguous, ask Ton now (standing rule) — a criterion you can't judge PASS/FAIL on isn't a criterion yet.

## 3. Reason — decide and build

On the first pass this is the full design work; on later passes it's re-thinking only what the feedback touched, then rebuilding those parts.

**Visual point of view.** Load the frontend-design skill's guidance. Default AI-generated design clusters around a handful of tells (warm cream + serif + terracotta; near-black + single neon accent; identical rounded SaaS cards with the same soft shadow; tracked-out ALL-CAPS eyebrows; em-dash labels). Where the brief leaves an axis free, make a deliberate choice specific to the subject matter instead.

- **Color:** name the palette as 4–6 hex values (or tokens) tied to a role or stated ratio.
- **Type:** one or two typefaces with a clear role split, on a real type scale.
- **Layout:** describe the structure in a sentence plus an ASCII wireframe before building; decide alignment on purpose.
- **Restraint:** spend boldness in one place per screen; keep everything else quiet.

**Build with the project's own tools.**

- In Figma: use the Figma MCP tools, reuse design-system components and variables (never hardcode a hex color or pixel spacing when a token exists), componentize anything that repeats. Add new frames beside existing ones; keep and label older versions.
- As a built page: use the project's component library and tokens if one exists; otherwise follow the frontend-design skill's HTML/CSS guidance.
- Build in stages for anything non-trivial: skeleton, then content, then a visual pass.

## 4. Verify — check every criterion, with evidence

- Take a screenshot (or render) and look at it, not just the node tree: clipped text, overlaps, wrong variants, placeholder copy left behind.
- Audit spacing against the grid, and confirm every color and text style is bound to a token, not a raw value.
- Go through the acceptance criteria **one by one by number** and mark each **PASS** or **FAIL** with the evidence (node name, measured value, what the screenshot shows). "Looks fine" is not evidence.
- On later iterations, re-check *all* criteria, not only the ones that failed before — a fix can break something that passed.

## 5. Pass? — the decision

- **All PASS → exit the loop.** Go to Hand off.
- **Any FAIL → Feedback**, unless this was the 3rd iteration — then stop and ask Ton (see Loop limit).

## 6. Feedback — turn failures into a fix list

For each FAIL, write one line: **criterion # · where (frame/node) · what's wrong · what "right" looks like.** Example: `#4 · Screen 5 / Hero card · gap is 20px · should bind space/24`.

Separate failures you can fix yourself from ones that need Ton's decision (a conflicting rule, a requirement that turns out to be ambiguous) — ask about the latter instead of guessing.

## 7. Fix — smallest targeted change, then loop back

- Change only what the feedback list names; don't redesign passing parts.
- Then return to **Reason** to confirm the fix still fits the overall design, and run **Verify** again.
- Keep a short loop log: `Iteration n — failed: #… → fixed: …`.

---

## Exit — hand off clearly

- State the goal, the final PASS checklist, how many iterations it took, and any limitation plainly (stand-in fonts, placeholder imagery, invented sample data, components not yet re-audited).
- Don't publish or share a design the user hasn't seen if it could be mistaken for a finished, approved design — flag drafts as drafts.
- **iOS/SwiftUI projects:** invoke the **ios-swiftui-design** skill and pass it the finished frames, the tokens and components used, the design rules, the final acceptance checklist, and the limitations. That skill owns the SwiftUI translation.
- **Re-entry:** if ios-swiftui-design sends back a design-level failure (e.g. an element with no workable native equivalent, a tap target the design itself makes too small), treat it as new **Feedback** and re-enter this loop at **Fix**.
