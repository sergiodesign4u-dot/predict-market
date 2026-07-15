# References - Visual Language Sources (Stage 06 Concept, Step 1)

> How we found the visual language. Not a mood board, not a clone. One reference is the
> base, concrete techniques are borrowed from others, and every borrowed technique names
> the persona anxiety it removes (cited to personas.md / jtbd.md).
>
> Method: Refero MCP (styles + screens), under the refero-design skill. Search date 2026-07-13.

---

## Which benchmark, and why

The strategic dimension was already named at Stage 01 (research). It is **Trust**:
research.md and benchmark.md dedicate a whole section (§5 "Benchmark: Trust & First-Time
Credibility") to it, because Trust is the #1 value for the audience (20-40, real money)
and the exact axis where direct competitors are weakest.

Benchmark set from research §5: Polymarket, Kalshi, Futuur (HARD), Bet365 (SOFT), and the
best-in-class-from-another-category aspirational bar, **Revolut** (32/40, described in
research as "the aspirational bar for how a non-bank financial product builds trust").
Revolut is the benchmark whose *visual language* we mine here (Bet365 and Kalshi are
gambling / regulated-exchange brands we cannot and should not imitate; research §5 marks
copying Bet365's brand authority as the mechanism that will NOT work).

We did not run new research. We searched Refero for the visual language of the named
aspirational benchmark plus adjacent trust-first consumer fintech.

---

## What Refero returned

**Styles: strong coverage.** Four full style references pulled (Revolut, N26, Monzo,
Public). These carry concrete tokens (color roles, type scale, radius, component specs),
which is what we borrow from.

**Screens: thin coverage for our niche, stated honestly.** Screen search for
prediction-market / betting / funds-protection deposit patterns returned off-target
results (spreadsheets, a Kraken pro-trading terminal, SeatGeek, Xbox, Bloomberg). Refero's
screen index is web-marketing-heavy and does not cover prediction-market or betting product
screens. Rather than force a weak screen reference, the concrete anxiety-reducing *patterns*
below are taken from the named components inside the four full styles (for example N26's
"Risk Indicator Card", Revolut's "Social Proof - Stats & Awards Block", Monzo's "Status
Badge") combined with the Top-3 trust mechanisms already decided in research §5. This is a
transparency note, not a blocker: Refero worked, styles were rich.

---

## Base reference (ONE): Revolut

- **Source:** Revolut, https://revolut.com (Refero style `ffb5ffe7-18a3-402f-bba9-6b1e14d64540`)
- **Why the base:** it is the research-named aspirational trust benchmark, and its method
  matches two of our hardest jobs at once: it is **photo-led** (the photograph carries the
  screen, so the product reads as life/story first) and **strictly achromatic** (white,
  off-white, black, near-black; the photo provides the only color), which reads as credible
  and controlled rather than hyped.
- **Technique taken (the method, not the skin):**
  1. The image carries the screen; UI recedes to a thin frame over it. We keep the method,
     but swap Revolut's aspirational-travel photography for **real event / news photography**
     tied to each market's subject. This directly answers Alex's pain "Markets feel
     disconnected from the news he's reading. The event exists in isolation. There's no
     story around it" (personas.md, Pains) and job FJ2 "understand why the market thinks
     this" (jtbd.md FJ2, the confirmed differentiator).
  2. Restrained achromatic base + architectural, tightly-tracked display type =
     "serious, transparent organisation" before a single word of copy. Answers EJ2 "feel
     this is a serious and transparent organisation, so my anxiety about fund safety leaves
     before I press confirm" (jtbd.md EJ2) and Alex's fear "Platform looks like crypto - he
     associates crypto with scams" (personas.md, What scares).
- **NOT cloned:** we reject Revolut's luxury-travel positioning, mountain/adventure imagery,
  89px hero drama, and center-everything hero. Our product is news-and-events, mobile-first,
  spectator-friendly, not a wealth brand. We take the discipline (photo carries color,
  achromatic UI, calm type) and leave the persona.

---

## Borrowed technique 1: N26 - the "ledger" disclosure card

- **Source:** N26 ("The online bank"), https://n26.com (Refero style `59911817-9d14-445a-9f1b-617418001061`)
- **Concrete technique taken:** N26's **"Risk Indicator Card"** - a white card, 1px hairline
  border (Horizon Gray `#e9e9e9`), minimal radius, a plain-language heading plus a small
  caption, no decoration, and a **single brand accent used only for the primary action**.
  We adopt this exact form for the funds-safety block: the plain reassurance line
  ("Your USDC is held 1:1. We never lend it without your permission") plus the on-chain
  verify link, presented as a calm ledger card, not a legal wall and not a colored banner.
- **Anxiety it removes:** Alex's "He doesn't know what happens to his money. No clear
  explanation of funds protection before the first deposit" (personas.md, Pains; benchmark
  C2 Futuur 1/5, Polymarket 1/5) and job FJ4 "an unambiguous answer to 'what happens to my
  money', so my risk is about the event, not the platform" (jtbd.md FJ4).
- **Role rule preserved:** single accent = primary action / active state only, never a
  decorative fill. This keeps color rare so the reassurance reads as fact, not marketing.

---

## Borrowed technique 2: Monzo - approachable-not-trader character

- **Source:** Monzo, https://monzo.com (Refero style `aa5196ac-072e-42ec-8248-1174ae843063`)
- **Concrete technique taken:** three specific moves that make a money product feel
  human rather than like a trading terminal:
  1. **One warm accent, reserved for impact** - Monzo uses a single vivid accent (hot coral
     `#ff4f40`) "exclusively for primary calls-to-action ... reserving its impact". We adopt
     the discipline (one accent, CTA-only), not the coral hue.
  2. **Chunky, highly-legible display headline** (MonzoSansDisplay) - confident and readable,
     the opposite of dense trader type.
  3. **Soft-rounded pill primary button + monoline outline icons** - friendly, calm, tactile.
- **Anxiety it removes:** Alex's fear "Platform looks like crypto - he associates crypto with
  scams" (personas.md, What scares) and the product voice rule "speak to a spectator with an
  opinion, not a trader" (voice.md, Principle 3). A News Junkie is a Forecaster/Analyst by
  self-image (research §9 F6), not a trader; the interface must not read as a terminal.
- **Role rule preserved:** accent stays vivid or absent, never a greyed-out or repurposed
  background (Monzo's own don't-rule).

---

## Secondary reference on watch (not a core borrow): Public

- **Source:** Public, https://public.com (Refero style `b501d608-f10c-490c-8e88-a48a557603db`)
- **Why kept:** Public is an investment product that stays **editorial and calm** rather than
  becoming a trading board: monochrome canvas, hairline-bordered data cards (Smoke `#e9edf3`),
  a light-weight display face that gets authority through understatement, and one interactive
  accent color. This is a useful model for the FJ2 "why this price" story block - presenting a
  probability with quiet authority instead of trader density.
- **Status:** logged as a reference, not borrowed yet. If Step 3-4 need the story block to
  show a number with context, Public's hairline data-card is the pattern to adapt. Naming it
  here so the decision is traceable, not invented later.

---

## Rejected on sight: reflexive palettes

Per the anti-averaging and anti-slop rules, we reject the palette that is guessable from the
category and from the search word "trustworthy / calm":

- **Monarch (`monarchmoney.com`) and the warm oat/cream + serif + terracotta cluster** scored
  high for "trustworthy, calm" but this is exactly the current AI-slop reflex the refero-design
  and impeccable rules flag: "warm ivory/cream canvases, olive/clay/terracotta palettes". It is
  the first association with "cozy / trustworthy", so it is a reflex, not a decision. Not our base.
- We also do not average the four references into a safe middle (Revolut is achromatic-photo-led,
  Monzo is single-warm-accent, N26 is single-teal-ledger, Public is monochrome-editorial - the
  answer is NOT cream + one muted accent + a polite serif). Revolut owns mood and density; the
  others contribute one bounded technique each.

---

## Reference lock (carried into Step 2-4)

> Updated at Step 2 (2026-07-13) after the designer taste: the base shifts from light to
> **dark**. Revolut now contributes METHOD only (photo carries the screen, one rare accent,
> calm architectural type), not a light skin. Accent decided: electric violet (brand) + acid
> lime (highlight); green/red reserved for YES/NO. See concept.md "Designer taste".

```
Primary direction: Revolut method on a DARK canvas - photo carries the screen, one rare accent, calm architectural type; high contrast, alive.
Preserve: hybrid dark surface (real EVENT/NEWS imagery + subtle glow/dot-grid), near-black base, one rare accent, spectator-friendly (not trader) tone.
Borrow only:
  - N26: the "Risk Indicator / ledger" disclosure card (hairline border, plain line, accent = action only) -> funds safety FJ4/EJ2.
  - Monzo: one accent CTA-only + chunky legible display + monoline icons -> approachable, not-a-terminal.
  - Public (on watch): hairline editorial data card for the "why this price" number -> FJ2.
  - Taste refs (MELEE base, Jupiter glow dot-grid): dark canvas energy, violet+lime accent, subtle glow. NOT their trader/gamified density.
Role rules: brand accent = violet (action/active only); lime = highlight, sparse; green/red = YES/NO only; photography = real subject imagery (never grey placeholder); numbers presented calm, not dense.
Media strategy: real Unsplash photography by event subject on dark; funds/trust as a bordered ledger card; icons monoline outline (Solar, chosen in Step 3-4).
Reject: cream/oat + terracotta reflex; muddy low-contrast (Hedgehog); center-everything luxury hero; trader-terminal density (leverage/PNL/gacha); averaged safe middle; any accent used as a decorative fill.
Token commitments (provisional, finalised in concept.html Step 4): light text on near-black canvas; brand accent electric violet + highlight acid lime (not indigo-by-default, not category-reflex); green/red for outcomes; hairline neutral borders tilted toward the accent; single rare accent for action; all pairs WCAG AA at Step 4.
```

---

## Source index

| Source | Refero UUID | Role here | Anxiety line it serves |
|---|---|---|---|
| Revolut | `ffb5ffe7-...` | BASE (method: photo-led, achromatic, calm type) | FJ2 story-led; EJ2 credible org; "looks like crypto/scam" fear |
| N26 | `59911817-...` | Borrow 1 (ledger disclosure card) | FJ4 / EJ2 funds safety |
| Monzo | `aa5196ac-...` | Borrow 2 (approachable, one accent, monoline icons) | spectator-not-trader; "looks like crypto" fear |
| Public | `b501d608-...` | On watch (editorial data card) | FJ2 "why this price" |
| Monarch + cream cluster | n/a | REJECTED (category reflex / AI slop) | - |

*Next (Step 2): designer taste (named products + anti-references) written into concept.md,
then 3-5 attribute pairs, each traced to a data line and a borrowed technique above.*
