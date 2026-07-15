# CJM As-Is - Current Experience

**Focus: Alex (News Junkie, primary persona) x Main Job (MJ)**

Main job (English gloss): "When an event I follow nears its outcome, I want a real stake in the result, so it is not just news but my personal participation with real consequences."
Source: `user-research/docs/jtbd.md` (## MJ · Main Job), `research/docs/lean-ux-canvas.md` §4.

Mining depth for the emotion layer: **Lite** (re-projection of existing research + search autosuggest + observed friction from the captured competitor screens in `research/screens/`). Honesty rule for As-Is: every emotion stands on a source; no source -> `[?]`, not a drawn emotion. Signal = one mention; Pattern = repeated across sources.

---

## Phases (As-Is skeleton)

The path is derived from how Alex reaches this job today, with existing products, not from a generic funnel. Emotions and barriers are added in the next section (step 4).

| # | Phase | Phase goal (job) | Actions | Touchpoints / channels | Source |
|---|---|---|---|---|---|
| 1 | Trigger: the news moment | Turn a followed event plus his own opinion into a real stake (MJ) | Reads the morning news, forms a take before others, feels the "I called it" pull as the event nears its climax | News media, X, podcasts | personas Context; research.md §6 (KEY entry point); §9 F4 (motivation precedes onboarding, HIGH) |
| 2 | Looking for a way to act | Find where to place a real stake on this specific event | Recalls prediction markets or a Polymarket screenshot seen on X; looks for a platform. `[?]` exact discovery action (search term / cited-odds click / a friend) is not in the data | X (screenshots), media citing Polymarket / Kalshi odds, word of mouth | personas Context; research.md §9 F4 #3; §4 Competitors; `[?]` |
| 3 | Hitting the platform wall | Get in and see a market | Opens Polymarket / Futuur, meets MetaMask + USDC + 8+ wallet icons before any market, frequently closes the tab | Polymarket, Futuur (crypto-native signup) | personas Context + Pains (benchmark C6: 2/5) |
| 4 | Trying to make sense of a market | Understand what he would bet on and why the price is what it is | If past the wall, sees "67%" and "resolves"; no story or context; the market feels detached from the news he was reading | Competitor market-detail pages | personas Pains; research.md §4 ("no why this price", "event in isolation"); ux-patterns.md (Story-driven) |
| 5 | The money question | Fund the bet without feeling he will lose money to fees or risk | Faces fiat-to-crypto conversion; asks "what happens to my money?"; no clear answer before deposit; unclear fees | On-ramp / wallet steps on competitor platforms | personas Pains + Trust (benchmark C2: Futuur / Polymarket 1/5); H4 / H6 |
| 6 | Placing the bet and following the event | Have real skin in the game and track it against reality (MJ) | Reached by few: places a YES / NO stake, then follows the event through the news he already consumes | Competitor bet interface; his existing news channels | jtbd.md MJ; personas Context |
| 7 | Resolution: win or loss | Get vindication (win) or closure (loss) | Outcome resolves. On a win he wants to share "I told you this would happen" (SJ). On a loss, "after a loss, nothing", no context, no next step; latent fear of platform betrayal | Competitor resolution / notifications; chats and social for sharing | personas Pains + Context; research.md §4 (post-resolution undesigned); §9 F3, F5; SJ |

**Path honesty note:** this is not "Alex successfully bets." Today there is mass attrition at phases 3 to 6 (the crypto wall), and his real behavior often falls back to being a passive observer (reading odds cited in the media, never betting). Source: research.md §9 F4 #3. This is expected to be the deepest dip of the curve, but emotions are assigned in step 4, not here.

## Emotions and barriers (per phase)

Lite pass plus a targeted step-6 re-research. Emotions are re-projected from the existing research (personas.md, research.md §4/§9, benchmark.md) and the captured competitor screens; the two most decision-critical phases (the crypto wall and the post-loss moment) were then confirmed with real public quotes mined in step 6 (see "Re-research" below and research.md "Re-research for CJM"). Phases still on re-projection alone keep `[?]` in the Quote column. Strength: signal = one mention, pattern = repeated across sources or HIGH-confidence.

| Phase | Thoughts / questions (derived) | Emotion (sign · 1-5 · strength) | Barrier | Quote |
|---|---|---|---|---|
| 1 Trigger | "I called this. I want in on it." | + · 4 · **pattern** (research.md §9 F4 HIGH; personas Context) | none yet; latent - no accessible way to act on the take | `[?]` |
| 2 Looking for a way | "Where do I even do this? Is Polymarket the thing? Is it legit and safe?" | neutral to - · 2 · **signal** (discovery action is `[?]`) | unclear where to go or whether it is legitimate; `[?]` exact action | `[?]` |
| 3 Hitting the platform wall | "Wait, I need a crypto wallet just to look? What is MetaMask?" | - · **5** · **pattern** (personas "closed the tab" + benchmark C6: 2/5; step-6 mine) | crypto wall: MetaMask / USDC / 8+ wallet icons before any market | "connected my wallet successfully, but I'm a bit confused about how users usually fund their accounts" (Reddit, pattern) - Q1 |
| 4 Trying to make sense of a market | "Why is it 67 percent? What does 'resolves' mean? What am I even betting on?" | - · 4 · **pattern** (research.md §4 "no why this price"; "event in isolation"; step-6 mine) | no context or story; trader vocabulary | "the website ... feels more like scrolling an Excel spreadsheet ... confusing overwhelming" (Reddit, signal) |
| 5 The money question | "What happens to my money? Where does my USDC sit? What are the fees?" | - · 4 · **pattern** (benchmark C2: 1/5 Futuur / Polymarket; H4; step-6 mine) | no funds-safety explanation before deposit; opaque fees | "deposited 25 USDC ... wouldn't allow me to bet ... in some wallet I can't access. Basically lost 25 USDC" (Trustpilot, pattern) |
| 6 Placing the bet and following | "OK, I'm in. Let's see if I was right." | + · 3 · **signal** (reached by few; inferred) | reached by few (attrition); tracking happens outside the product | `[?]` |
| 7 Resolution | win: "I told you!" / loss: "...now what? Why did I lose?" | win + · 4 · **pattern** (SJ share) / loss - · **5** · **pattern** (research.md §9 F3, §4, F5 HIGH; step-6 mine) | after a loss "nothing", no context or next step; platform-betrayal fear (frozen funds / opaque resolution) = #1 trust killer | "I am so confused ... What do I do?" · "never do that again" · "what's the point" · "try to make it back" (Reddit, pattern) - Q2 |

**Most-dangerous `[?]`, now closed (step 6):** the exact words at the wall (phase 3) and right after a first loss (phase 7) were the two re-projection-only points that most shape To-Be. Both were confirmed with real public quotes in the step-6 re-research below, so their `[?]` is removed. Phases 1, 2 and 6 keep `[?]` on the quote (low design impact, honestly marked).

### Re-research (step 6): sourced quotes

Targeted Deep mine on the two decision-critical phases, public / pre-login only (Reddit via old.reddit.com, Trustpilot). Six evidence screenshots in `research/screens/` (prefix `cjm-mining-`). Full log in `research/docs/research.md` -> "Re-research for CJM".

**Q1 - crypto wall and funding (phases 3-5):**
- "I connected my wallet successfully, but I'm a bit confused about how users usually fund their accounts and manage balances on the platform." - Reddit r/Polymarket, ~2 mo ago. `research/screens/cjm-mining-polymarket-newuser-wallet-confused-reddit.png`. Strength: pattern (a single r/Polymarket search surfaced ~25 deposit-trouble threads).
- "The website itself is a bit chaotic and messy, at times it feels more like scrolling an Excel spreadsheet. Information isn't always clear and it can be a little confusing overwhelming." - Reddit r/Polymarket, "Rookie Impression". `cjm-mining-polymarket-rookie-impression-clarity-reddit.png`. Strength: signal.
- "I deposited 25 USDC using coinbase and then the website wouldn't allow me to bet so I tried to withdraw the money ... instead it is in some wallet I can't access. Basically lost 25 USDC. This site is SCAM." - Trustpilot (Polymarket 1.4/5, 589 reviews), Feb 2026. `cjm-mining-polymarket-usdc-coinbase-lost-trustpilot.png`. Strength: pattern.

**Q2 - the moment after a loss (phase 7):**
- "I am so confused ... Polymarket didn't count the game ... as a win? What do I do?" - Reddit r/Polymarket, "How did I lose?". `cjm-mining-polymarket-howdidilose-confused-reddit.png`. Strength: pattern (many near-identical "why didn't this resolve" posts).
- "lost the bet whatever ... Definitely will never do that again lol" - Reddit r/PredictionsMarkets. `cjm-mining-polymarket-loss-noclosure-scam-reddit.png`. Strength: pattern (loss -> quit arc).
- "the Switzerland game fucked me over no response from support like what's the point of this app then" - Reddit, same thread. Strength: pattern (no closure / no support).
- "Right now I'm down $2300 ... Going to try to make it back with a few parlays on world cup." - Reddit r/Polymarket, "What's the most you lost/gained". `cjm-mining-polymarket-most-lost-chasing-reddit.png`. Strength: signal (loss chasing, ties to F5 / EJ3).

## Emotional curve and growth zones

### Emotional curve

Each point rests on a step-4 emotion (with a source). `[?]` and single-source (signal) points are weaker than pattern points and must render lighter / smaller in the chart, not interpolated.

| Phase | Sign · intensity | Strength | Note |
|---|---|---|---|
| 1 Trigger | + · 4 | pattern | Peak - enters most motivated |
| 2 Looking for a way | - · 2 | signal | Weak / undefined - discovery action `[?]` |
| 3 Hitting the platform wall | - · 5 | pattern | **Dip 1 (deepest)** - crypto wall, mass attrition |
| 4 Trying to make sense of a market | - · 4 | pattern | Negative plateau |
| 5 The money question | - · 4 | pattern | Negative plateau |
| 6 Placing the bet and following | + · 3 | signal | Small lift, only for the few who get through |
| 7 Resolution (win) | + · 4 | pattern | Share spike |
| 7 Resolution (loss) | - · 5 | pattern | **Dip 2** - "after a loss, nothing" + betrayal fear |

Curve shape: high start, crash at the wall, negative through market-confusion and money, a small lift for the few, then a split at resolution (win spike / loss crater). Two dips: phase 3 (the wall) and phase 7 loss.

### Growth zones

Where today's experience hurts most and where we can win the comparison. Each is tied to a step-4 barrier and a research gap; solutions are deferred to To-Be (step 7). All five are pattern-backed.

1. **Kill the crypto wall.** Barrier: phase 3 (wallets before any market). Gap: benchmark.md C6 (2/5), personas.md "closed the tab". This is the deepest dip.
2. **Explain the number, tell the story.** Barrier: phase 4 (no "why this price", event in isolation). Gap: research.md §4, ux-patterns.md (Story-driven).
3. **Answer "what happens to my money" before deposit.** Barrier: phase 5 (no funds safety, opaque fees). Gap: benchmark.md C2 (1/5), H4 / H6.
4. **Design the loss and the post-resolution moment.** Barrier: phase 7 loss ("after a loss, nothing"). Gap: research.md §4 (post-resolution undesigned), §9 F3.
5. **Earn trust against the betrayal fear.** Barrier: latent phase 7 (platform betrayal = #1 trust killer). Gap: research.md §9 F5 (HIGH).

Zones 1 to 3 and 5 map onto the product core (clarity + trust); zone 4 maps onto the voice principle "design the loss". These are the candidates To-Be must close.

