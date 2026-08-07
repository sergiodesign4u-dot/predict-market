# Census - what actually stands on the five anchor screens

Step 1 of the rebuild, 2026-08-07. Read once, written down, done. **Nothing runs this on a schedule
and no check reads this file.** If it disagrees with the repository later, the repository is right.

## Why it exists

The deleted vitrine documented 51 stylesheets, one page per file, and called the page `button`
because the file was `button.css`. That is a document about the code. **This is a count of what a
person can click**, taken from the rendered page, and the two are not the same thing: the largest
control in this product has no class, no component and no page, and nothing that reads the
stylesheet could ever have said so.

## Method

Five families and every state they ship with, **41 screens of the 106**:

| Family | Screens | What it brings that no other screen has |
|---|---|---|
| event feed | 9 | the browse shell, the category rail, filters, the card grid, logged out |
| event detail | 12 | the outcome pair, the bet sheet and its four failures, tabs, multi-outcome |
| active bets | 9 | the position list, the history split, three empties |
| deposit | 7 | money entry, the amount chips, five failure states |
| sign in | 4 | the auth sheet, providers, a conflict |

Walked in a real browser at **390 and 1280** in **both themes**: 164 renders, **13,930 readings**.
Both widths because the desktop bet panel and the mobile bet dock are different controls, and both
themes because a role given a value in only one of them renders anyway.

**A control is** `a`, `button`, `label`, `summary`, `[role=button]`, `[onclick]`, or anything that
introduces `cursor:pointer` its parent does not have. The last clause catches the divs that act as
controls and excludes the `svg` inside a button, which merely inherits the cursor.

**A face is the computed value** of: background, background image, border width/style/colour,
radius, ink, font family/size/weight, letter spacing, text transform, padding, rendered height, box
shadow, opacity and display. **Computed, not read from the source**, which is the whole point: a
link with no rule still has a colour and it is the User Agent's.

**Width is not part of a face** on purpose: a full-width button in a sheet and the same button in a
row are one decision. **Height is**, because height is what padding and font size add up to, and it
is where a tap target lives.

**What was excluded, and it had to be.** The first run counted **4,264 of 7,987 controls as one
class**, `.sidebar-sub-link`: the course roadmap and screen tree that every page of this repository
carries in `<aside id="rmSidebar">`. It is stand furniture painted by `components/course-chrome.css`
and it answers no product question. Everything in that aside, its toggle, its overlay and the theme
switch are out. **The count more than halved**, and any census that had not noticed would have
reported the panel as the product's most important component.

## The numbers

| | mobile 390 | desktop 1280 |
|---|---|---|
| controls | 3,447 | 3,518 |
| distinct faces | 69 | 72 |
| distinct class strings | 42 | 45 |

The two themes carry **the same set of controls** and differ only in colour, which is the semantic
layer doing its job and is worth having measured rather than assumed.

## The vocabulary, measured

| Axis | Distinct values | What they are |
|---|---|---|
| radius | **3** | `0`, `10px`, `100px` |
| font size | **7** | 10, 11, 12, 13, 14, 16, **19.2** |
| weight | **3** | 400, 600, 700 |
| padding | **18** | of which one is `0` on 1,763 readings; 17 real box paddings |
| rendered height | **29** | 14 to 114 |
| background | 11 | |
| ink | 11 | |
| border | 17 | |

**The radius is already a scale** and that is the one axis nobody has to argue about: three steps,
and each of them means something (a plate, a control, a pill). **The font size is nearly one**, with
a single leak: `19.2px` is `1.2em` of something and is the only value on the list that no one typed.

> **Corrected 2026-08-07 by step 3c, `../typography.html`.** It is not `1.2em` and it is not a leak.
> `--display-hero` is `clamp(19px,1.5vw,23px)`, and 1.5vw of a 1280 viewport is exactly 19.2. Two
> more fluid tokens land on non-integers at that width, `23.68` and `29.44`, and the census did not
> report them only because no control wore them. **A fluid size lands where the viewport puts it.**
**Padding and height are not scales at all**, and 29 heights for controls whose job is "be pressed"
is the same finding the deleted backlog carried as S34, taken again on a fifth of the screens and
coming out the same way.

## The finding: 58 per cent of the controls have no class

**2,035 of 3,518.** Not unstyled: they render correctly, in **23 distinct faces**, through element
selectors and inherited rules.

| Tag | Readings | What they are |
|---|---|---|
| `a` | 1,505 | the footer link columns (26 per screen), the SEO link strip (7 per screen), and the card question, the "try again", the "view your bet" |
| `label` | 304 | the filter panel's checkboxes: a boxed 33px control with a 10px radius, which is a chip by every measurement except its name |
| `summary` | 127 | the sort disclosure, the notification and account menus, the language picker |
| `button` | 99 | **the YES and NO pair on a card**, which is the single most important control in a prediction market |

**The bare `<a>` renders as 12 different faces. The bare `<button>` as 6. The bare `<summary>` as 3.**

This is what a census answers that an inventory cannot. The system has a file called `button.css`
and the product's outcome pair is not in it; it has `chip.css` and the filter checkbox is not in it;
it has no file at all for a link in running text, which is the most common thing on every screen.

## The nine jobs

Every one of the 3,518 readings at 1280 falls in exactly one row. The grouping is by what the
control DOES and what it measures, not by which file styles it.

| Job | Readings | Wearing | Where the decision is today |
|---|---|---|---|
| **text link** | 1,541 | nothing, on 1,511 of them | inherited from the element; 12 faces |
| **chip** | 460 | `.chip-quiet/-nav/-rail/-amount`, `.ed-tablabel`, `.rules-tab` | `chip.css`, `tabs.css` |
| **icon button** | 425 | `.icon-btn` and five face modifiers | `iconbtn.css` |
| **field label** | 304 | nothing: a bare `<label>`, 33px, 10px radius, 8px pad | `filters.css`, through an element selector |
| **row** | 269 | `.nav-item.nav-row`, `.nav-row-stack`, `.nav-slot` | `navitem.css` |
| **button** | 178 | `.btn` with four emphases and four sizes | `button.css` |
| **disclosure** | 135 | nothing: a bare `<summary>`, in 3 faces | `header.css`, `filters.css` |
| **outcome pair** | 104 | **81 of them a bare `<button>`**, the rest `.yesno-pick`, `.bp-side`, `.opt-row` | `yesno.css`, `betpanel.css` |
| **segmented tab** | 18 | nothing: a bare `<button>`, 38px, 100px radius | `tabs.css` |
| named one-offs | 84 | `.logo-btn` 41, `.notif-all` 34, `.related-more` 8, `.sel` 1 | one file each |

**Four of the nine jobs are worn by no class at all**, and between them they are 1,914 readings, 54
per cent of every control on these screens. The field label is the clearest case of what that costs:
it measures 33px with a 10px radius and an 8px pad, which is a chip by every value the browser
reports, and it is not in `chip.css` and never appeared in an inventory. Whether it should BE a chip
is the next step's question. The census can say what it looks like; it cannot say what it is.

## One class, more than one face

Twelve classes render as more than one control. Excluding the bare tags, they are `.q` (3 faces:
the card question at 88, 30 and 15px), `.chip-quiet` (2), `.chip-nav` (2), `.btn-primary.btn-sm` (2),
`.btn-secondary.btn-sm` (2) and `.ed-tablabel` (2). **A class is not a control**: the scope it stands
in decides the paint, and a stand page that shows one of them shows one of two.

## The responsive delta is eleven classes

| Only at 1280 | Only at 390 |
|---|---|
| `.bp-side.yesno-pick` (the bet panel's pair) | `.bp-side.yesno-pick.yesno-pick-bar` (the dock's) |
| `.bal-add`, `.bal-swap`, `.desk-only` (the wallet strip) | `.nav-item.nav-slot` (the bottom nav) |
| `.hiw-btn` (the header pill) | `.btn.btn-md.btn-primary` |
| `.bp-change` | |

**Every one of these is a deliberate decision**, and this is the list a responsive stage inherits.
Nothing here is an accident of the window.

## Tap targets

At 390, **2,783 of 3,447 controls stand under 44px**. 1,621 of them are text with no box, where the
44 floor is a different argument. **1,162 are boxed controls under 44 and those are the real ones**:

| | Height | Readings |
|---|---|---|
| the filter checkbox, bare `<label>` | 33 | 304 |
| `.chip.chip-quiet` | 38 | 210 |
| `.nav-item.nav-row` | 33 | 170 |
| the sort and menu `<summary>` | 36 | 68 |
| `.btn.btn-bare` | 25 | 64 |
| `.logo-btn` | 40 | 41 |
| the language `<summary>` | 27 | 41 |
| `.chip.chip-rail` | 26 | 40 |

## What this decides

1. **The atoms are jobs, not files.** Nine jobs, 72 faces, 45 class strings. The next step declares
   a level for each and names the ones that are one control under two names.
2. **The text link is a component and it does not exist.** It is half the controls on every screen.
3. **The outcome pair must carry a class.** 81 readings of the product's defining control are a bare
   `<button>` painted by an ancestor.
4. **The consolidation has three real axes and one free one.** Padding (17), height (29) and border
   (17) are the work; radius is already decided at three steps and needs only to be written down.
5. ~~**`19.2px` is a leak** and is the cheapest fix in the whole pass.~~ **Withdrawn 2026-08-07**:
   it is a `clamp` resolving at 1280 and there is nothing to fix. See the note in the vocabulary
   section above.
