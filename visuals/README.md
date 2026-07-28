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
- Masters exported at JPEG q92; shipped copies resized (events 1600px wide q82, avatars
  400px q85) into `assets/`.

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
