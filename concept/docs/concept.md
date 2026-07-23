# Concept - Visual Language (Stage 06)

> Taste first (written down, not held in the head), then attributes (visual opposites, each
> traced to a data line and a borrowed technique), then the three directions and the locked
> choice. Internal doc, English, no em dash.
>
> Sources: concept/docs/references.md (Refero) + personas.md + jtbd.md + voice/docs/voice.md
> + research.md. Taste captured from the designer (Sergiy) on 2026-07-13, verbatim intent.

---

## Designer taste

### Likes (named products, not adjectives)

- **Predict Market + Kalshi** - likes the prediction-market product and Kalshi as a product,
  but on Kalshi the primary color does not have enough contrast against the white background.
  Reading: the fix he wants is more contrast, which a dark canvas solves natively.
- **MELEE** (melee, prediction-market landing) - the strongest anchor. "Very cool, bright,
  contrasty." Near-black canvas, acid lime plus electric violet, big bold two-tone display
  headline (white plus lime word), a soft glow orb behind the card. This is the north star
  of the taste.
- **Jupiter** - "more or less", but specifically likes the glowing dot-grid in the center
  ("dots with backlight") and the lime CTA on dark. We take the glow/dot-grid detail, not
  the whole trading terminal.
- **Space** (gamified prediction product) - "also cool." Dark cards, vivid green/red YES/NO,
  glossy 3D icons, gamified. Liked visually. Caution: its trader/gamified density (leverage
  slider, PNL, ranks, buyback and burn) is the part the data rejects - see the tension note.

### Anti-references (definitely not)

- **Beige / warm / soft-gentle colors and AI-cliche palettes** - cream, terracotta, muted
  pastel. This is the model's reflex on "trustworthy / cozy" and is banned. (Matches the
  reference we already rejected on sight: Monarch and the oat/cream cluster.)
- **Hedgehog** (screenshot #2) - navy canvas with a muddy blue hero banner and low-contrast
  dark-green / dark-red buttons. Flat, no energy, low contrast. This is the exact opposite of
  what he wants: the contrast complaint from Kalshi, made worse.
- **Trader-terminal density as behavior** - leverage sliders, PNL rank, gacha, buyback-and-burn,
  ticker walls. Liked as a look in Jupiter/Space, but rejected as product surface because it
  contradicts the whole thesis (Alex, News Junkie, spectator-not-trader, "looks like crypto =
  scam" fear). We keep the ENERGY (dark, vivid, glow, contrast), not the terminal gadgets.

### Decisions locked from taste (2026-07-13)

| Decision | Choice | Note |
|---|---|---|
| Base canvas | **Dark, near-black, high contrast** | Flips the Step-1 light base. Revolut now contributes method only (photo carries the screen, one rare accent), not a light skin. |
| Accent | **Electric violet = brand, acid lime = highlight** | Superseded 2026-07-16: the shipped accent is **matte brass `#c7a24e`**, not violet/lime (see the Vault section below and root `DESIGN.md`). The reserved-outcome rule was kept: green/red stay YES/NO only, so brass never collides with the win/lose semantic. |
| Tone | **Span the three directions** | One calm-credible, one crypto-native, one in between. Decided live at Step 3. Energy is shared; density varies. |
| Surface | **Hybrid: dark + real event photo + glow** | Real news/event photography carries the story (FJ2), on a dark canvas, with the vivid accent and a subtle glow / dot-grid (Jupiter detail). |

### The one honest tension (data vs taste)

The liked references (Jupiter, Space) are crypto-trader / gamified. The data pulls the other
way: Alex fears "this looks like crypto = a scam" (personas.md, What scares) and wants a
spectator feel, not a trader terminal (voice.md Principle 3; Market Board rejected in
ux-patterns.md). Resolution, agreed with the designer: take the palette energy and contrast
from the taste, cap the trader density with the data. Attributes 2 and 3 below are the
guardrails that hold this line.

---

## Attributes (visual opposites)

Five pairs. Each is "this, not that", traced to the exact data line it comes from and the
borrowed technique (references.md) that delivers it. No pair contradicts the taste; where
data caps taste, it is marked.

### A1 - High-contrast and alive, not muddy and flat

- **From the data:** "Probability-over-time chart ... Movement = engagement. Users return to
  check position" (research.md §4, common pattern 3) and "Event-triggered arrival - KEY
  pattern for all segments. Entry point" (ux-patterns.md). The product greets a user who
  arrived because something is happening now; it must feel live.
- **Technique:** dark near-black canvas with one vivid accent at maximum contrast (Revolut's
  achromatic discipline applied on dark, so color stays rare and loud), plus a subtle glow /
  dot-grid (Jupiter detail).
- **Taste:** core love. Directly answers his Kalshi contrast complaint and the Hedgehog
  anti-reference (muddy, flat, low-contrast is the thing to avoid).

### A2 - Credible and controlled, not hyped or degen

- **From the data:** Trust is the #1 value for the audience (benchmark.md, Why Trust). EJ2:
  "feel this is a serious and transparent organisation, so my anxiety about fund safety
  leaves before I press confirm" (jtbd.md EJ2). Platform-betrayal / "looks like a scam" is
  the #1 documented churn driver (research.md §9 F5).
- **Technique:** the accent is used ONLY for action and active state, never as a decorative
  fill (Monzo: "reserve its impact"; Revolut: the photo/accent is the only color). Energy
  comes from contrast and one loud accent, not from many colors or casino shine.
- **Taste, capped:** this is the guardrail on "lean crypto-native." The energy he likes stays;
  the degen/casino hype (Space's glossy loot, buyback-and-burn theatrics) does not. Marked
  tension, resolved by his "energy, not terminal" intent.

### A3 - A spectator's clarity, not a trader's terminal

- **From the data:** FJ2 "understand why the market thinks this" is the single confirmed
  differentiator (jtbd.md FJ2; research.md §4 gap "no competitor explains why this price").
  The Market Board / trading view is explicitly rejected for the primary audience: "the
  language of a trader, not a spectator" (ux-patterns.md; jtbd.md, features to cut).
- **Technique:** one clear number + one-line why + YES/NO, on a calm hairline data card
  (Public's editorial data card), never an order-book or a wall of tickers.
- **Taste, capped:** Jupiter/Space density is the anti-pattern here. The look's energy is
  welcome; the terminal density is not.

### A4 - Proof of safety is visible, not buried

- **From the data:** FJ4 "an unambiguous answer to 'what happens to my money', so my risk is
  about the event, not the platform" (jtbd.md FJ4). "He doesn't know what happens to his
  money. No clear explanation of funds protection before the first deposit" (personas.md).
  Benchmark C2: Futuur 1/5, Polymarket 1/5 - the gap is wide open.
- **Technique:** N26's "Risk Indicator / ledger" disclosure card - hairline border, one plain
  line ("Your USDC is held 1:1. We never lend it without your permission") plus the on-chain
  verify link, with the accent on the action only.
- **Taste:** neutral, sits cleanly on dark. The ledger card is calm by design, which supports
  A2 (credible, not hyped).

### A5 - The event is a story, not an isolated question

- **From the data:** FJ2 again, and Alex's pain "Markets feel disconnected from the news he's
  reading. The event exists in isolation. There's no story around it" (personas.md, Pains).
- **Technique:** the hybrid surface - real event / news photography carries the card on the
  dark canvas (Revolut method, adapted to dark plus glow), not a bare text question row.
  Photography = real subject imagery (Unsplash by subject), never a grey placeholder.
- **Taste:** the "hybrid: dark + photo + glow" choice. Reconciles the graphic/glow energy he
  likes with the story-led surface the data needs.

---

## Provisional palette seeds (finalised in concept.html at Step 4)

> Superseded 2026-07-16. These violet/lime seeds were the Signal starting point; the shipped
> palette is Vault (graphite + matte brass). The real, contrast-checked hex live in root
> `DESIGN.md`; the Vault section at the end of this file explains the change. Kept here as the
> historical record.

Not final hex yet (colors are decided and contrast-checked on the stand at Step 4). Direction
only, so Step 3 has a starting point:

- Canvas: near-black (not pure #000; a slightly warm-or-cool very dark neutral, chosen per direction).
- Brand accent: electric violet - action, brand, active state.
- Highlight: acid lime - sparingly, for emphasis / glow, never as body or large fill.
- Outcome semantics: green = YES, red = NO - reserved, never reused as the brand accent.
- Neutrals: dark greys with a slight tilt toward the accent hue (not pure grey).
- All accent-on-dark and text-on-dark pairs get a WCAG AA contrast check at Step 4.

---

## Directions

Three contrasting directions built live in `concept/directions.html`, spanning the spectrum
the designer chose ("span the three directions"):

1. **Newsroom after dark** (calm, credible pole) - canvas #0E1116, brand violet #7C5CFF
   restrained under 10%, lime nearly absent, minimal glow, hairline borders, Archivo display,
   Solar linear icons. Leans A2/A3/A4/A5. Recorded, on the shelf.
2. **Signal** (balanced, synthesis center) - canvas #0B0A12 with a violet tilt, violet #8B5CF6
   + lime #C9F24E, soft glow + backlit dot-grid, violet card shadow, Sora display. Leans
   A1/A2/A3/A5. **CHOSEN (2026-07-13), being refined.**
3. **Arena** (crypto-native pole) - near-black #060609, loud violet #7C4DFF + acid lime
   #B6FF3C, neon halos, glowing number, Space Grotesk. Leans A1/A3 (A3 as the guardrail).
   Recorded, on the shelf.

### Signal, refined (two corrections from the designer)

The first Signal card had an oversized 16:9 hero image and an invented per-card safety line.
Both corrected in `concept/directions-signal.html`:

- **Image is now a small thumbnail**, not a hero. The dominant image was the complaint.
- **Structure and content come from `wireframes/event-feed.html`** verbatim: `.top`
  (thumbnail + question), `.why` (context line), `.prob-line` (YES + probability),
  `.yesno`, `.meta` (Volume, Closes, bookmark). No per-card safety line - that belongs on
  the deposit / confirm screen (A4 lives there), not in the feed. Real event copy reused
  (US gov shutdown, Bitcoin $150k, Ethereum upgrade, UK election multi).

Four card treatments offered, same Signal palette, for the designer to pick:
- **A - Wireframe-faithful:** small 60px thumbnail beside the question, text prob-line. Smallest footprint.
- **B - Odds bar:** adds a slim YES/NO split bar under the why line.
- **C - Short media strip:** a photo but at a third of the old height (~112px), category chip on it.
- **D - Multi-outcome:** option rows (name, prob, compact YES/NO), per the wireframe multi card.

Three more binary treatments added for exploration (`concept/directions-signal.html`, lower
section): **E** number-forward (probability leads, YES/NO carry the price), **F** two outcome
tiles (green/red % tiles, imbalance visible), **G** featured/live (stronger glow + a trend
sparkline; the sparkline is a candidate IA addition to the feed card, not yet in the wireframe).

### LOCKED (2026-07-13), then SUPERSEDED by Vault (2026-07-16 - see the Vault section below)

- **Direction: 2, Signal.**
- **Binary feed card: treatment B** (thumbnail + why + odds bar + YES/NO + meta).
- **Multi-outcome feed card: treatment D** (thumbnail + why + option rows + meta).
- **Reference screen for Step 5: `wireframes/event-feed.html`** (the working horse), colorized
  as a copy in `ui-visual/`.
- Newsroom after dark (1) and Arena (3) stay on the shelf in `directions.html`. E/F/G stay
  recorded above; G's sparkline is parked as a possible IA add, decided later.

Rule held: structure and content stay owned by `wireframes/`; the concept layer owns only the
visual language. The full stand is `concept/concept.html` (Step 4).

---

*Next (Step 3, under /impeccable): build concept/directions.html - three contrasting
directions spanning calm-credible to crypto-native, each shown live (palette, a card with a
real photo, icons), each labeled with the attributes above it is built from.*

---

## Vault - the shipped direction (LOCKED 2026-07-16, supersedes Signal)

This section is written back FROM the built mockups (`concept/concept.html` +
`ui-visual/event-feed.html` and the Event Detail family), which are the living truth. Where
this file's earlier Signal decisions diverge from what shipped, the mockups win and the earlier
lines are annotated "superseded" above. The token-level system is documented in root
`DESIGN.md`; this section records only WHY the direction changed and how each attribute survived.

**What Vault is.** A graphite canvas (`#0f1013` page / `#141619` device) with ONE matte-brass
accent (`#c7a24e`, text-safe `#d7ac53`, lit `#e6c877`) and reserved green/red for YES/NO only.
Real event photography, embossed two-stone plates (a lighter outer slab, darker inset plates and
cards that float and cast shadow), inset brass hairlines + notched corners on the small tiles.
Fonts: Space Grotesk (display), DM Sans (body), IBM Plex Mono (numbers). Signal, Newsroom and
Arena are archived to `concept/old/pre-vault-3d/`.

**The one honest divergence (taste vs shipped), named, not buried.** The taste doc above locked
"electric violet = brand, acid lime = highlight" (the MELEE north star). Vault ships **matte
brass on graphite instead**. This is a deliberate designer decision (Sergiy, 2026-07-16), made on
the stand, not a silent model drift. Why it holds: brass on near-black solves the SAME root
complaint the violet was chosen for (Kalshi: "the primary color has no contrast") while reading
as *credible and weighty* rather than *neon and crypto-native* - which serves A2 (credible, not
degen) and Alex's "looks like crypto = scam" fear better than acid lime did. The MELEE energy
survives as high contrast + one loud accent + real photography; only the hue changed. Flagged here
because it contradicts the "Accent" row of the taste-locked table; anyone re-reading that table
should treat brass, not violet, as final.

**How each attribute survived into Vault (macro reasons):**

- **A1 - High-contrast and alive, not muddy and flat.** Kept, delivered differently: the energy
  comes from a near-black graphite canvas + one loud brass accent + the two-stone emboss (cast rim
  + drop shadow) and real event photos, instead of Signal's glow/dot-grid. Still the direct answer
  to the Kalshi contrast complaint and the Hedgehog (muddy, flat) anti-reference.
- **A2 - Credible and controlled, not hyped or degen.** Strengthened. Brass + stone reads as a
  vault fitting, not a casino; the One-Accent rule (brass only on identity, active state, one CTA)
  is the guardrail. This is the attribute that drove the violet -> brass change.
- **A3 - A spectator's clarity, not a trader's terminal.** Kept intact. The odds bar carries the
  outcome color so the tinted YES/NO buttons stay quiet; the AMM state is shown as a pool + depth
  curve, never an order book. Numbers are always mono (the honesty cue).
- **A4 - Proof of safety is visible, not buried.** Kept. The trust line ("USDC held 1:1, we never
  lend it / N events resolved") sits near the action in neutral stone; the footer trust cards and
  the notched brand tile carry it, calm by design (supports A2).
- **A5 - The event is a story, not an isolated question.** Kept. Real event photography carries the
  card (thumbnail masked and bleeding into the graphite) and the featured hero; never a grey
  placeholder. The "why" line under each question is the story cue.

*Rule still held: structure and content stay owned by `wireframes/`; the concept/visual layer owns
only the visual language. The shipped stand is `concept/concept.html`; the token spec is root
`DESIGN.md`.*
