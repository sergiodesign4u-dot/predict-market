# Research Workflow Prompts

Reusable two-phase prompt sequence for auditing research docs, surfacing product decisions, and building HTML deliverables. Developed on the Prediction Market project (June 2026).

---

## When to use

After you have a working `research.html` and at least one source `.md` file (personas, JTBD, strategy, etc.) that was written during early product research. This workflow cleans up the research, closes gaps, forces founder decisions, and builds polished HTML output.

---

## Prompt A - Research Audit & Decision Brief

Run this first. It ends with a structured decision brief - you respond with your choices, then run Prompt B.

```
Context:
- Project: [PROJECT_NAME]
- Working dir has: research.html (main research doc), [LIST_YOUR_DOCS].md
- All generated files must be in English.
- Mobile-first dark theme: base CSS for mobile, desktop via min-width.

Step 0 - Sidebar check:
Open research.html. If the sidebar nav is missing links to any other
research pages that exist in the project root, add them now.

Step 1 - Audit [personas.md / jtbd.md / equivalent docs]:
For every claim in each file, classify as one of:
  - CONFIRMED: backed by research cited in research.md
  - HYPOTHESIS: educated guess, marked [?] or not
  - INVENTED: no source, no marker, presented as fact

Output: a table per file, one row per claim.

Step 2 - Danger list:
From the HYPOTHESIS and INVENTED claims, identify those that
DIRECTLY affect a design or product decision. These are the dangerous
ones. List them in priority order with: what depends on this claim,
and where to look for the answer (specific forums, products, reviews).

Step 3 - Close the top 3-5 gaps:
Run live web research (Reddit, X, Trustpilot, product blogs, 2024-2026
sources only). For each gap: find evidence, update research.md
in a new section "§[N] Post-Audit Research - [Month Year]".
In the source doc, replace [?] markers where answered; note what changed
and why where claims were refuted.

Step 4 - Product decisions brief:
Surface all open product/architecture decisions that:
  a) Are blocking enough to affect MVP scope or tech choices
  b) Have 2+ viable options with real tradeoffs

For each decision, present:
  - The question
  - Option A vs Option B (vs C if relevant)
  - Evidence for each from research
  - Your recommendation with one-line rationale

Then STOP. Do not make decisions. Wait for founder input.
```

---

## Prompt B - Post-Decision: Finalize Docs + HTML

Run this after you've replied to the decision brief with your choices.

```
Context:
- Project: [PROJECT_NAME]
- Decisions made: [PASTE THE DECISIONS THE FOUNDER GAVE]
- All generated files must be in English.
- CSS design system: --bg:#0e0e0e; --surface:#161616; --border:#242424;
  --text:#e8e8e8; --muted:#666; --accent:#c8ff00; --red:#ff5f5f;
  --green:#5fdb8f; --blue:#5fa8ff

Step 1 - Lock in decisions:
Update strategy.md (or equivalent) and research.md to reflect
each decision. Mark open questions as CLOSED. Cross-reference decisions
to any HYPOTHESIS claims in personas/jtbd that the decisions now resolve.

Step 2 - Final gap research (if any remain):
Any HYPOTHESIS claims still open that are closeable via web research -
close them now. Update docs same pattern as Prompt A Step 3.

Step 3 - Build HTML pages:
For each .md research doc (personas.md, jtbd.md, etc.):
  - Create a matching .html page, mobile-first dark theme
  - Match the visual language of research.html exactly
  - Sidebar: list ALL html pages with cross-links; current page active
    with sub-links to its sections
  - Hypothesis claims show a [?] badge; confirmed claims show no badge;
    updated claims show a ⚠️ warning block with source reference
  - Structured data (matrices, tables) rendered as styled HTML tables

Step 4 - Update research.html sidebar:
Add links to all newly created HTML pages.

Step 5 - Push to GitHub:
git add all changed/created files, commit with descriptive message, push.
```

---

## Notes from first run (Prediction Market, June 2026)

- Prompt A produced 4 decisions: AMM vs CLOB, fee model (taker per trade vs fee-on-win), resolution mechanism (multisig vs oracle), and geo strategy.
- The decision brief format worked well: present options with evidence + one-line recommendation, then stop.
- Prompt B created personas.html (~550 lines) and jtbd.html (~600 lines) in parallel agents - fast.
- Sidebar cross-linking between all 3 html pages (research, personas, jtbd) was the last manual step before push.
- IntersectionObserver for active section tracking: `rootMargin: '-15% 0px -75% 0px'` - works well on mobile.
