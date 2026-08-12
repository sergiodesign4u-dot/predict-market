# Visuals - own-generated imagery (Stage 08, Step 4)

Own, brand-owned photography for the **Vault** visual system, replacing the earlier
July stock. Generated, not sourced. This folder is the record: `masters/` holds the
full-resolution originals; the web-optimized copies actually loaded by the screens live
in `assets/`. The look is set by root `DESIGN.md`, not reinvented here.

## The look these had to hit

From `DESIGN.md`: "Real event photography in thumbnails and hero, masked and veiled into
the graphite, never a grey placeholder." The feeling is "a cast metal plate and a vault
fitting, not a casino floor and not a trading terminal." So every image is: dark, near-black
graphite ground; one warm brass / amber key light; muted, desaturated; fine film grain;
editorial-documentary, credible before anything else; no neon, no hype, no text. This
directly answers Alex's documented fear, "this looks like crypto, so it is a scam."

## How they were made

- **Tool:** Magnific -> **Google Nano Banana 2** (`imagen-nano-banana-2-flash`).
- **Settings:** events at aspect `3:2`, portraits at `1:1`; resolution `2k`.
- **Cohesion:** the chosen Culture frame was passed as a `style` reference when generating
  Crypto, Politics and the portraits, so the whole set shares one grade and mood.
- **Selection:** each subject generated in 2 variants; the picked variant is listed below.
- Masters exported at JPEG q92; shipped copies resized (**events 440px wide q82**, avatars
  400px q85) into `assets/`.
- **The event width is 440 because that is what the screens ask for, measured, and it was 1600
  until 2026-08-12.** Every placement of every photograph was walked across all 106 documents in
  `ui-visual/` at 390 and at 1280: the thumbnail stands in four boxes, `56x88` on the feed card,
  `56x91.8` on the category feeds, `72x72` on `.ed-thumb` and `46x46` on `.rel-thumb`. **The box is
  not the demand.** All four are `background-size:cover`, and `cover` scales the source until the
  box is covered and crops away the rest, so 1600x1073 into 56x88 draws **131x88** of source. The
  largest demand any placement makes is **137x92**, and 440 is three times that with headroom,
  which covers a phone at device pixel ratio 3. The re-export took the four files from 1,158,832
  bytes to 116,050 and the composited thumbnail at ratio 3 is indistinguishable from the one it
  replaced. `docs/decisions.md`, 2026-08-12.
- **The four `trust-*.webp` decorations are not made here and are not resized, ever.** Their
  drawing lives in the alpha channel, which is 65 to 73 per cent of each file, and three of the
  four have no fully opaque pixel at all. One of them is a halftone, and resampling a halftone
  destroys it at every ratio. They are re-encoded in place with
  `cwebp -q 92 -alpha_q 10 -alpha_filter best -sharp_yuv`, which touches no dimension.
  `docs/backlog.md` 140 is what is left of their weight.

## The set

| Asset (`assets/`) | Subject | Picked frame | Prompt (abridged) |
|---|---|---|---|
| `event-politics.jpg` | Politics | capitol at dusk, foggy 3/4 | Neoclassical government capitol with a dome at dusk, warm brass light from tall windows, deep graphite blue-black sky, cinematic, muted, film grain, credible documentary, no people. |
| `event-crypto.jpg` | Crypto / markets | bitcoin coin **inside a bank vault** | A single brushed-gold bitcoin coin on dark slate, dramatic warm brass side light, deep near-black graphite background, macro, weighty and credible like a vault, not neon, not a casino. (Chosen frame set it literally inside a vault - on-concept.) |
| `event-culture.jpg` | Culture | theatre, warm stage pool | Grand ornate theatre auditorium from the dark back rows, a single warm brass-amber spotlight through faint haze onto an empty stage, deep graphite shadows, restrained, not glamorous. |
| `event-general.jpg` | General / World | brass globe + desk lamp | A vintage brass world globe on a dark desk, single warm amber lamp, deep near-black graphite ground, cinematic, muted, film grain, weighty like a vault. |
| `avatar-1.jpg` | Portrait (comment) | woman, warm side light | Editorial head-and-shoulders portrait, calm neutral expression, near-black graphite ground, single warm brass key light leaving half the face in shadow, documentary, crops to a circular avatar. |
| `avatar-2.jpg` | Portrait (comment) | man, warm side light | Same prompt, second frame (a different person) for avatar variety in the same colorway. |

## Where they are wired (via `ui-visual/_theme-vault.css`)

- **Trending feed** (`event-feed.html`): the `.grid > .card:nth-of-type(n) .thumb` rotation now
  cycles the four own subjects (the old `spare-*` and `event-sports` stock are retired from it).
- **Category pages** (`event-feed-{politics,crypto,culture,general}.html`): each page carries a
  `body.cat-*` class, and a `.cat-* .grid > .card .thumb` rule gives every card that page's own
  subject photo.
- **Comment avatars** (`event-detail.html`): `.cmt-list .cmt-av` alternates `avatar-2` / `avatar-1`
  (`:nth-child(even)`); the composer "you" chip keeps its neutral fill.
- The `ui-kit/` showcase inherits all of this through `components/index.css`, the one stylesheet
  every screen links.

## To swap or regenerate

- **Swap a picture:** drop a replacement at the same `assets/<name>.jpg` path (same
  filename -> every screen updates; hard-refresh to clear the browser image cache).
- **Regenerate:** re-run the prompt above on Nano Banana 2, pass one chosen frame as a `style`
  reference to keep the set cohesive, export the master here and the resized copy into
  `assets/`.
- **More variety:** the category pages currently repeat one photo per subject. Generate 2-3 more
  frames per subject and extend the `.cat-*` rules with `:nth-of-type` to vary them.

## Retired (still in `assets/`, no longer in the feed rotation)

`event-sports.jpg`, `spare-markets-dark.jpg`, `spare-reader.jpg`, `spare-newspapers.jpg` - the
July stock. Left on disk in case a Sports category is built later, but out of the Vault rotation.
