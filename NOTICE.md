# Third-party assets, and what each one requires

This repository ships two kinds of asset it did not draw: an icon set and three type families.
Each entry says what it is, where it came from, what its licence requires, and where the
requirement is met. **An asset with no entry here has not been cleared and may not ship.**

## Solar, the icon set

- **What:** the filled half of the icon set. 20 glyphs, drawn as `<symbol>` in a sprite on every
  painted screen and referenced through `<use>`. They are the "Bold" weight. It was 21 until
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
  `assets/icons.svg`, which is the file that holds the glyphs**; and in the pointer comment on every
  screen and kit page that references it, which is the place a person reading the markup actually
  meets it. The sprite stopped being inlined into 112 documents on 2026-08-09 and the attribution
  moved with it rather than being dropped.

**This entry was written on 2026-08-09 and the glyphs had been shipping since the Vault pass.**
Fifteen Solar Bold glyphs were already in the sprite with the set named in a comment and **no
attribution anywhere**, so the licence was being relied on and not honoured. Naming an asset is not
crediting it. Backlog 31, and the account is in `docs/decisions.md`.

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
