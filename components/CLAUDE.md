# components/ - the code

- New goes here first and onto a screen second. A screen never styles itself.
- A state is a TOKEN, never a value typed into a class: `:hover`, `:active`, `:focus-visible`, `:disabled` (gate 25).
- A state token has a value in BOTH themes, or the state exists in one of them only.
- Colour comes through a semantic role, geometry straight from a primitive (gates 13, 12).
- A pattern starts at three screens, adds no styles of its own, carries no colour, imports last (gate 23).
- The `@import` goes in the group of its level, never at the end: `python3 ui-kit/_levels.py --order`.
- A part is imported before the whole that holds it.
- `python3 ui-kit/_check_kit.py` passes, every gate, before it is a change.
