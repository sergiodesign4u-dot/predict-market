# Visuals - own-generated imagery (Stage 08, Step 4)

Own, brand-owned photography for the **Vault** visual system, replacing the earlier
July stock. Generated, not sourced. This folder is the record: `masters/` holds the
full-resolution originals; the web-optimized copies actually loaded by the screens live
in `assets/`. The look is set by root `DESIGN.md`, not reinvented here.

**That sentence was false for the trust decorations until 2026-08-13, and in the one direction
that costs bytes**: their five 1254x1254 masters, 8,322,176 of them, sat in `assets/`, the folder
the screens load, referenced by nothing, while the photographs' masters sat here as the README
says. `masters/` holds all eleven now, and `assets/` holds only what a screen asks for:
**9,690,253 bytes to 1,107,186.** Two things here are the master of nothing shipped and are named so
that nobody takes them for one: `trust-source-alt.png` is the unpicked second variant of the source
drawing, kept because the note above says every subject was generated in two; and
`trust-column.svg` with `trust-globe.svg` are a SIMPLER schematic of the same subjects, dated an
hour before the renders that replaced them. Adopting the vectors was refused on 2026-08-12 because
it is a decision about how the trust strip should LOOK and not about its weight, and they are kept
here as the evidence for that refusal. `docs/backlog.md` 138 and 140.

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
- **The trust decorations are not made here, and since 2026-08-13 they are MASKS rather than
  pictures.** They shipped as four `trust-*.webp` whose drawing lived in the ALPHA channel, 65 to
  73 per cent of each file, and WebP codes alpha with a lossless coder, so 488,842 bytes of them
  on 105 screens would not come out by re-encoding: `-alpha_q 10` had already been tried.
  **The masters settled it, and they say the alpha plane should never have existed.** All five
  `masters/trust-*.png` are 1254x1254 and **100 per cent opaque**: brass line art on black, a
  LUMINANCE drawing, and the mean of a master's luminance and the mean of the alpha made from it
  agree, 23.8 against 22.3. So the four shipped files are `*-mask.webp` now, greyscale and opaque,
  used as `mask-image` with `mask-mode:luminance` over a flat `--color-trust`. **256,422 bytes for
  what cost 488,842**, because a DCT codec can reach a luminance plane and the alpha coder could
  not. Dimensions are still not a free parameter and the halftone is still not resampled: three
  keep their exact size and their exact coverage, taken from the shipped file's own alpha channel.
  The fourth GREW, 520x600 to 640x738, because it has two placements pulling opposite ways and the
  seo plate was upscaling it: it is cut from `masters/trust-column-full.png` at (121, 84, 1014 x
  1171), which is the crop the 520 was cut from, solved by matching the drawing's bounding box.
  `docs/backlog.md` 139 and 140, closed together.

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
