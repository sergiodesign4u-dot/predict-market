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
- **Changes made:** none to the glyphs. The paths are used as published. What the system adds is
  around them: a shared `viewBox`, the `.ic` box, and the ink, which comes from a role token rather
  than from the file.
- **Where the attribution is:** here; in `DESIGN.md` under the icon rule; and in the comment above
  the sprite on every screen that carries one, which is the place a person reading the markup
  actually meets it.

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
