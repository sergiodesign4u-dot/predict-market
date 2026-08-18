# Third-party assets, and what each one requires

This repository ships three kinds of asset it did not draw: an icon set, three type families, and
the event pictures. Each entry says what it is, where it came from, what its licence requires, and
where the requirement is met. **An asset with no entry here has not been cleared and may not ship.**

## Solar, the icon set

- **What:** the filled half of the icon set. 20 glyphs, drawn as `<symbol>` in one sprite,
  `assets/icons.js`, loaded by every painted screen and referenced through `<use href="#i-name">`. They are the "Bold" weight. It was 21 until
  `danger-circle` was retired on 2026-08-09 and its placements went to `danger-triangle`.
- **Author:** 480 Design.
- **Source:** the Solar Icon Set, https://www.figma.com/community/file/1166831539721848736, taken
  through the Iconify API (`api.iconify.design/solar.json`).
- **Licence:** **CC BY 4.0**, https://creativecommons.org/licenses/by/4.0/.
- **What that requires:** attribution. Credit the author, name the licence, and say if changes were
  made. It does NOT require the product to be open, and it does not restrict commercial use.
- **Changes made:** **no path data is altered. Two symbols are composed differently, and this is the
  line CC BY asks for.** `magnifer-o` is placed at `scale(.9294)` about the cell centre, because it
  painted 21.5 x 21.5 where the rest of the set paints 20 and so stood inside the two-module safe
  field; the `d` string is Solar's, untouched, and removing the wrapper restores the original size
  exactly. `clock-circle-bold` was delivered as a full-cell rectangle behind a `<mask>` and is now
  its two published subpaths in one path with `fill-rule="evenodd"`; both `d` strings are Solar's,
  the silhouette is identical to within antialiasing, and the mask went because it carried a
  document-unique id and was invisible to every measurement this repository takes. Everything else
  the system adds is around the glyphs: a shared `viewBox`, the `.ic` box, and the ink, which comes
  from a role token rather than from the file.
- **Where the attribution is:** here; in `DESIGN.md` under the icon rule; **at the head of
  `assets/icons.js`, which is the file that holds the glyphs**; and in the pointer comment on every
  screen and kit page that references it, which is the place a person reading the markup actually
  meets it. The sprite stopped being inlined into 112 documents on 2026-08-09 and the attribution
  moved with it rather than being dropped. It became a script the same day, for a reason that is
  about `file://` and not about the licence, and the attribution moved again with it.

**This entry was written on 2026-08-09 and the glyphs had been shipping since the Vault pass.**
Fifteen Solar Bold glyphs were already in the sprite with the set named in a comment and **no
attribution anywhere**, so the licence was being relied on and not honoured. Naming an asset is not
crediting it. Backlog 31, and the account is in `docs/decisions.md`.

## The event pictures, and they are GENERATED rather than photographed

- **What:** `assets/ev-*.webp`, 25 images, one per open market, **in two cuts**. The master is
  **1664 x 936**, 2,208 KB for the set, and the feed hero draws it. `-sm` is **240 x 360 and is a
  PORTRAIT CROP**, 246 KB for the set, drawn by the card thumbnail, the related row and the event
  detail head. It is not a scaled-down master: it is `-crop 800 0 960 1440` of the 2560 original,
  the central 37.5 per cent that `background-position:center` was already showing in a 56px-wide
  slot, so no pixel is downloaded to be discarded. Measured across 11 widths and 5 screens,
  **340 of 341 slots upscale by nothing**, and the feed's pictures cost **251 KB against 833** when
  one 1400px file served every slot. **24 of the 25 masters have 0 live references** and are kept
  deliberately: they are the largest copy this repository holds, and the small cut is derived from
  the original rather than from them.

- **Where they came from:** generated on 2026-08-17 with **Seedream 5 Pro** through Magnific, from
  text prompts written here. No reference image, no photograph, no stock library, no person's
  likeness. The prompts are recorded in `docs/decisions.md` under the entry for that date, and **the 2560 x 1440 originals are not in this repository**: they were re-fetched from the account once already, which is the supported way to re-cut them.
- **What that requires:** nothing a licence asks for, and something this product asks for.
  **A prediction market is a claim about the world, so it must not illustrate one with a fabricated
  record of the world.** The rule these 25 were written under, and the rule any replacement has to
  keep:
  - **no people at all**, no faces, no silhouettes, so no likeness is invented;
  - **no legible text**, no signage, no numbers, no logos, so nothing reads as a document;
  - **the SUBJECT, never the OUTCOME**: a ballot box, not a result; an empty stage, not a winner;
    cracked ground, not a named drought. The picture says what the market is ABOUT and takes no
    side, which is the same discipline that keeps green and red off the brand;
  - **no red or green light source**, because in this product those two colours mean YES and NO.
    The first attempt returned a data hall lit by red and green indicators, and it was discarded on
    that ground alone.
- **Two more constraints came from the layout rather than from ethics**, and they are here because
  a replacement image has to meet them too: the card crops to the **central 37.5 per cent** of the
  frame, so the subject has to live in the middle third; and the hero draws the picture at 42 per
  cent opacity under a veil that follows the ink, so a pale image vanishes in Daylight and a dark
  one drowns in the Vault. Mid-tone with internal contrast, and neutral: **not pre-graded.**
- **Where this is said to a reader:** here, and in `DESIGN.md` under Photography, which no longer
  claims the pictures are photographs of anything.

## The three type families

`assets/fonts/` holds Space Grotesk, DM Sans and IBM Plex Mono as woff2, self-hosted so that no
page calls a font host: a request to one carries a visitor's IP to a third party before the consent
banner has asked anything. All three are **SIL Open Font License 1.1**, which permits bundling and
requires the licence to travel with the files and the fonts not to be sold on their own.

- Space Grotesk, Florian Karsten, OFL 1.1.
- DM Sans, Colophon Foundry and Jonny Pinhorn, OFL 1.1.
- IBM Plex Mono, Mike Abbink and Bold Monday for IBM, OFL 1.1.

## The photographs

`assets/*.jpg` and `assets/*.webp` are placeholders standing in for event photography and are not
cleared for anything. **They are not a shipping asset**, and the handoff owes a real answer:
either a licensed source with its terms recorded here, or generated art with its provenance
recorded here. Filed as a Stage 12 question rather than assumed.
