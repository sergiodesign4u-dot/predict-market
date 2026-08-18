# Block bank

What a page of a given TYPE is made of, before anyone draws one. One section per page type, and a
type is banked once: the bank is why a second node of the same type costs a layout decision and not
a research pass.

**This file did not exist until 2026-08-03**, and its absence was found by the Design System stage
walking its four sources for the next screen to build: source 2 (the next node on the IA map) named
a node and had nowhere to get its blocks from. A node with no block source does not stop a designer,
it makes one invent the composition, and an invented composition is a median of everything the
inventor has ever seen. That is the failure this file exists to prevent, so the first rule is about
where a row comes from and not about what it says.

## The four rules a row obeys

1. **No block without a trace.** Every row cites a confirmed job (`jtbd.md`: MJ, FJ1-5, EJ1-3,
   SJ1-2), a CJM barrier (`cjm-as-is.md` / `cjm-to-be.md`: GZ1-GZ5), or a structural SEO requirement
   (`ia/docs/pages/seo.md`). A block that traces to none of the three is not banked, however normal
   it looks on other people's pages.
2. **The "where we are better" column is filled, never skipped.** If it were empty on every row the
   bank would be a collected median wearing a table, and that would be said out loud rather than
   shipped quietly.
3. **A reference is an INPUT, not an output.** A composition that matches one source one for one is
   a copy. What each source contributed and what was deliberately left is written below the table.
4. **Every block carries MVP or LATER.** A bank with no phase is a wish list.

---

## Type 1: the static content page

### Which nodes it covers

Five of the six page nodes `ia/docs/sitemap.md` registers under SYSTEM AND GLOBAL, and **all five
ship at MVP by the decision of 2026-08-18** recorded there. The `Built` column is the live state and
this sentence used to say all five had no screen in either tree:

| Node | Robots | Body profile |
|---|---|---|
| Terms of Service | `index,follow` | DOCUMENT - **built 2026-08-03**, the first use of this bank |
| Privacy Policy | `index,follow` | DOCUMENT - **built 2026-08-18** |
| Cookie Policy | `index,follow` | DOCUMENT - **built 2026-08-18** |
| Responsible betting | `index,follow` | DOCUMENT - **built 2026-08-18** |
| About | `index,follow` | STATEMENT - **built 2026-08-18**, and the people section is left out because this bank marks it LATER |

**All five stand in both trees, `wireframes/` and `ui-visual/`, one name each.** The four that
arrived on 2026-08-18 were built against `terms.html` rather than from this table, because a built
precedent carrying all eleven blocks is a better source than a specification of them, and the body
of each painted page is lifted from its grey twin so the two trees cannot disagree about what is on
it.

**The sixth node, Contact / Support, is NOT this type, and that is a decision with a reason.** It
carries a form, and a form brings a field vocabulary, four states of its own (empty, validating,
error, submitted), a success destination and a job trace to support rather than to trust. Banking it
here would put a transactional composition inside a reading composition and both would be wrong. It
is a second type and gets its own section of this file when its screen comes up.

**One type, two body profiles, and the evidence forced the split.** The shell is identical across
all five and is banked once. The body is not: a legal document is a long-read with sections and a
date, while About is a company statement with a hero, people and a closing action. Both sources say
so independently. Refero files them as two different page types (`Terms & Conditions` / `About`) with
two different UX pattern sets (`Article & Text` versus card grids, logo walls and hero images), and
the live crawl agrees: Kalshi's `/about` is 3,109 words with 11 images and a "Create your account"
CTA at the foot, while every legal page found is prose with no image at all. Pretending they are one
composition would give the About page a table of contents and the Terms page a team grid. Each row
below therefore carries its profile, and rows marked BOTH are the shell.

### The two sources, and what each one is for

**Domain truth: the competitors, read live in a browser on 2026-08-03.** From
`research/docs/competitors.md`, the benchmarked five. What they actually put on a page of this type,
and what holds a person there.

| Read | What it is, measured | What it teaches |
|---|---|---|
| `polymarket.com/tos` | H1, then the whole document inside an **`<iframe>` pointing at `docs.google.com`**. Host page carries 5 words of its own. No date, no contents, no anchors | The largest prediction market ships its terms as a Google Doc in a frame. The content is not in their DOM: not indexable, not themeable, not printable as their page, and not reachable by in-page search |
| `kalshi.com/regulatory/terms-of-service` | Not a document: an **index of regulatory documents grouped by legal entity** (Kalshi EX & Klear, Kinetic Markets FCM), 12 group headings, one link per document, one of them a raw S3 PDF | A regulated exchange has many documents, so the entry point is a hub, not a page. The grouping is by ENTITY, which is a legal fact the reader is made to resolve |
| `kalshi.com/privacy-policy` | **Rendered header and footer and no policy body at all** (161 words, 0 headings, no `<main>`) in a live browser | Recorded as measured, not as a verdict about their product: on this date, from this session, the volume leader's privacy policy showed a person nothing |
| `help.futuur.com/Terms-of-Service-...` | **16,739 words, 40 headings, 1 in-page anchor.** `Last updated: January 24, 2025` as the first line under H1. 720px column at 16px. Published on **Notion**, off-domain, **no footer**, no product chrome, no way back | Our closest structural analog leaves its own product to say what it is bound by. 16.7k words with one anchor cannot be navigated. The date is the one thing it does well, and it does it first |
| `revolut.com/legal/terms/` | 12,803 words, 73 headings, **breadcrumb** (Terms & Policies > Personal terms), **Download PDF**, **History**, a **region switcher** at the very top, and an effective-date BLOCK: updated 11 December 2025, effective immediately for new customers and 13 February 2026 for existing ones, with a link to the previous version. Sections numbered and titled as questions: "Why this document is important", "Can I open an Account?", "How is my money protected?" | The aspirational bar, and it is a voice bar rather than a layout bar. Two effective dates is the best single thing found anywhere: it answers "does this apply to ME yet", which every other page leaves the reader to guess |
| `help.bet365.com/.../safer-gambling` | 137 words. **Breadcrumb**, 17px prose in a 720px column, **"Was this article helpful?"**, links out to the tools, no footer. Four identical `H1`s on one page | The Crossover Bettor's reference frame files responsible gambling as a HELP ARTICLE, short, with the tools one tap away. The short page is a deliberate choice: the tools are the answer, the prose is the doorway |
| `kalshi.com/about` | 3,109 words, 11 images, full product chrome. Sections: what an event contract is, company history, values, founders, **backers**, **certification and regulation**, press, hiring, then **Create your account** | The About template in this category is a trust argument that ends in a conversion, and regulation is a SECTION of it rather than a footnote |

**Craft truth: Refero, searched by page type and job, never by industry.** 1,364 screens filed under
`Terms & Conditions`, 903 under `Privacy Policy`, 888 under `About`. Read: MasterClass, Copy.ai,
Cal, Fibery, Visual Electric, Calm, Mocha, Square, Prose, Maze, Parallel, MWM, Yelp, Outchat, Bezi,
Limitless, Ballpark, Expedia, Instacart, Craft, GoFundMe, ManyChat, Leonardo, Fingerprint,
TravelPerk, Pastel, Julienne, Slack; and for the statement profile Maze, Teal, Homerun, Nothing,
Dropbox, ShareWillow, Fable, Craft, Krisp, Clearful.

Five layout families exist for the document profile and the split is not decorative:

1. **Single column, no contents.** The majority: MasterClass, Cal, Fibery, Calm, Yelp, Limitless,
   Bezi, Outchat, Julienne, Pastel. Works to about 3,000 words and stops working after that.
2. **Two columns, sticky contents on the LEFT.** Maze, Parallel, Slack, Craft, TravelPerk.
3. **Two columns, sticky contents on the RIGHT.** GoFundMe, Leonardo, Instacart.
4. **Two columns, the sidebar holding SIBLING DOCUMENTS rather than sections.** Square, Expedia,
   ManyChat. Answers a different question: "which document am I in", not "where in it am I".
5. **Three columns**, document nav plus reading column plus contents. Fingerprint. A docs shell
   borrowed for a policy, and it is more machinery than the job needs.

Families 2 and 4 answer different questions and several products ship both at once. That is the
single most useful thing the craft half gave, because our five nodes are a SET, and a reader who
arrives at Cookie Policy from the cookie banner needs to find Privacy from there.

**Nothing was physically unavailable, so nothing is substituted.** Both halves ran. The one page
that did not yield what it should have is Kalshi's privacy policy, and it is recorded as an
observation with its date rather than replaced by a guess.

---

### The bank

`Profile`: DOC = the four legal documents. STATEMENT = About. BOTH = the shell, on all five.

| # | Block | Profile | Phase | Traces to | Reference input | Where we are better |
|---|---|---|---|---|---|---|
| B1 | **App header** in its logged-out or logged-in variant, unchanged | BOTH | MVP | R6 (usage rule: the logged-out header carries no account); FJ1 return path | Kalshi and Revolut keep full product chrome; Futuur and Polymarket do not | Futuur's terms live on a Notion subdomain with no header at all. Ours is the same header component as every other screen, so the reader never leaves the product to read what binds them |
| B2 | **Breadcrumb**: Legal > *this document* | DOC | MVP | SEO structural layer (breadcrumb + `BreadcrumbList` schema is decided in IA); GZ5 betrayal fear, which is partly not knowing where you are | Revolut (Terms & Policies > Personal terms), Bet365 (Home / My Account) | Neither Polymarket nor Futuur has one, and a document with no breadcrumb is a document with no siblings. Ours names the set, which is what makes B9 findable |
| B3 | **H1 + one-line lede in the product voice**, saying what this document decides for the reader | BOTH | MVP | `voice/docs/voice.md` (a plain provable sentence, spectator language); GZ2, the "explain the number" instinct applied to prose | Revolut's "Why this document is important" is the only lede found in seven live pages | Six of the seven sources open with the legal text itself. Ours opens by telling a person whether they need to read it, which is the same move the feed makes with the story line |
| B4 | **Effective-date block**, not a line: last updated, effective for new readers, effective for existing readers, and a link to the previous version | DOC | **MVP** | GZ5 (betrayal fear: a term that changed under you is the betrayal); FJ4 funds safety | Revolut's dual effective date is the best single pattern found. Futuur has the date and only the date. ManyChat and Fingerprint keep a previous version | Revolut gives two dates; **we add the one-line "what changed"**, which no source has. A version link answers "was it different", a changed-line answers "did it matter", and only the second is a question a person actually has |
| B5 | **Table of contents, anchored**, sticky on desktop and collapsed above the body on mobile | DOC | MVP | SEO (the H2 list is decided in IA and the anchors are its internal-linking plane); FJ1 scanning behaviour | Families 2 and 3: Maze, Slack, Craft, GoFundMe, Leonardo, Instacart | Futuur ships **16,739 words behind one anchor**. That is the measured failure this block exists against, and the threshold is stated in the bank rather than left to taste: over 1,500 words the contents is not optional |
| B6 | **The document body**: H2 sections, no skipped levels, numbered, section titles written as the reader's own question | DOC | MVP | `voice/docs/voice.md`; `CLAUDE.md` heading rule (one H1, no skipped level, in both trees) | Revolut: "Can I open an Account?", "How is my money protected?", "How do I close my Account?" | Revolut is alone in doing this and it does it in a bank's register. Ours carries the same question form into a spectator product, and the lexicon is already fixed in `microcopy.md`, so the phrasing does not drift between five documents |
| B7 | **The money answer, lifted to the top** of Terms and Privacy: one plain provable sentence about custody, linked to How It Works | DOC | MVP | FJ4, EJ2, GZ3; benchmark C2, where Polymarket and Futuur both score 1 of 5 | Revolut buries the same answer at section 7 ("How is my money protected?"); Polymarket has no such sentence anywhere | **This is the differentiator on this page type.** The benchmark says our two closest competitors score 1/5 on the funds question. Putting the answer above the fold of the legal page costs one paragraph and closes the gap the whole product is positioned on |
| B8 | **Reading aids**: a 60 to 75 CHARACTER column, which is `--measure:46ch`, **a DOCUMENT type scale of 16px/1.6 since 2026-08-19**, anchor links on every H2 | DOC | MVP | `DESIGN.md` section 3 (body prose at 13-14px and 60 to 75 characters). **This cell and the two above it said `60-75ch` until 2026-08-18, which is the mistake `tokens.css` records against this very unit**: `ch` is the advance of a zero, not of a character, so `70ch` renders about 104 characters and the number would have been wrong on all four documents this bank is about to build | Bet365 and Futuur both sit at a 720px column; Revolut at 1000px | All three exceed our own rule. 720px at 16px is roughly 90 characters and 1000px is well past 120. We already decided 60 to 75 characters and measured it; here it simply gets enforced on a page that is nothing but prose. **This was the FOURTH `60-75ch` in this row and the first pass caught three**, which is the point about a unit written wrong: it does not appear once, it appears everywhere the number is repeated. **AND THE CELL SAID `the seo-plate type scale` UNTIL 2026-08-19, WHICH IS THE OTHER HALF OF THE SAME MISTAKE.** `seo-plate` is the plate at the foot of a card grid and its prose is `--text-13`, the size of a paragraph a reader passes on the way somewhere else; naming it here set the only five surfaces in this product that are nothing but prose read end to end in the smallest prose size the product has, and the reader saw a 409px column on a 1220px frame. The competitor cell beside this one is the tell: Bet365 and Futuur were marked down for a 720px column, and the number that made theirs wrong was the CHARACTER count, not the type size. Ours is 16px/1.6 now at the same 46ch, and the band did not move by one character, because a `ch` scales with the face. `DESIGN.md` section 3 carries the Document rank |
| B9 | **Sibling documents block**: the other four, named, at the foot of the body | BOTH | MVP | Backlog item 27 (the footer promises destinations the map omits); GZ5 | Family 4: Square, Expedia, ManyChat | The five nodes are a SET and every source treats each as an island. A reader who reached Cookie Policy from the cookie banner has no path to Privacy on any page we read except through a footer they have to hunt |
| B10 | **Contact line**: the one address for a question about this document | BOTH | MVP | `ia/docs/sitemap.md` Contact / Support node; EJ2 | Futuur closes with support@; Mocha exposes a copyable legal address | Both bury it in the last paragraph. Ours is a block, because a person who has a question about a term has already decided not to finish reading |
| B11 | **Footer + bottom nav**, unchanged | BOTH | MVP | R9 (the bottom nav stands on every screen); "a screen is never a dead end" | Kalshi and Revolut keep the footer; Futuur's Notion page and Bet365's help article have none | Two of the seven pages we read have no way back into the product except the browser's back button. Our own rule already forbids that, and this is the first page type where it would have been tempting to make an exception |
| B12 | **Download / print view** | DOC | LATER | GZ5; a legal document a person can keep is a legal document they can hold you to | Revolut (Download PDF), Mocha (print via the browser) | LATER because a print stylesheet is a Stage 10 answer and a PDF is a build artefact, neither of which exists yet. Named now so the layout does not make it impossible |
| B13 | **"Was this helpful"** | DOC | LATER | No confirmed job. Kept as a candidate, not banked | Bet365 | Deliberately LATER **and flagged**: it traces to nothing in `jtbd.md`, so by rule 1 it does not enter MVP. It is recorded because Bet365 is the Crossover Bettor's reference frame and its absence will be noticed |
| B14 | **Region / jurisdiction note** | DOC | LATER | Geo restrictions (backlog item 27 names it as promised by the footer and absent from the map); compliance scope in `PRODUCT.md` | Revolut's country switcher is the first element on the page | LATER only because the geo policy is an open IA question, not because it is optional. When item 27 resolves, this block is where its answer lands |
| B15 | **Statement hero**: what the product is, in one sentence, over the shared plate | STATEMENT | MVP | EJ2 trust; MJ | Kalshi About, Maze, Homerun, Dropbox, Craft | Every About hero read is a mission sentence about the company. Ours is a sentence about the reader's job, which is the same discipline the event card's story line follows |
| B16 | **Resolution and custody, as a section of About** | STATEMENT | MVP | FJ4, EJ2, GZ5; benchmark C8 (resolution clarity) | Kalshi files "Certification, Regulation & Compliance" as a top-level About section | Kalshi can point at the CFTC. We cannot, so the section has to carry the mechanism itself: who resolves, against which public source, and the resolved count. That is the trust principle stated rather than borrowed |
| B17 | **Numbers block**: events resolved, USDC held, markets live | STATEMENT | MVP | SJ2, EJ2; `aarrr.md` social proof | Teal, Clearful, Homerun all ship a stats band; Polymarket uses volume as its entire trust case | Volume as social proof is the competitor default and it says nothing about whether you get paid. Ours counts **resolutions**, which is the only figure that answers the question a new user is actually asking |
| B18 | **People**, named, with what each is accountable for | STATEMENT | LATER | EJ2 | Kalshi (Tarek & Luana), Dropbox, Fable, Craft | LATER because the team is not public yet. Named so the About layout reserves the slot instead of being redrawn |
| B19 | **Closing action back into the product** | STATEMENT | MVP | MJ; the "never a dead end" rule | Kalshi ends About with "Create your account"; Pastel, Bezi, Limitless all end a legal page with a CTA | The competitors' CTA is a signup button on a page about the company. Ours routes to the feed, not to signup: this stage's own rule is that a bet panel does not stand where a person has not chosen an event, and a signup gate is the same mistake one step earlier |
| B21 | **Prototype notice**: this page's structure, headings and dates are real and its body text is not an operative term | BOTH | **SCAFFOLDING** | nothing, and that is the point | nothing: no shipped product carries one | **BANKED 2026-08-19, AFTER IT HAD BEEN BUILT ON ALL FIVE PAGES AND DECLARED ON NONE.** It is the first block in the DOM after the H1 on every one of the five, in both trees, and no row here described it, so a reader of this bank would have found a composition the pages do not have. It is SCAFFOLDING rather than MVP, the same rank as the wireframe's `TBD` chip: it exists because the copy under it is a description of what each section would decide rather than the clause itself, and **it leaves the day real legal copy lands**. Banked rather than deleted because a page that carries prototype copy and does not say so is the worse of the two failures |
| B20 | **Logo wall of investors / partners** | STATEMENT | **NOT BANKED** | nothing | Maze, Teal, Fable, Krisp, Nothing, Kalshi ("Our Backers") | Six of the ten statement pages ship one and it traces to no job. Rule 1 keeps it out. Recorded here so that the next person who notices its absence finds the decision instead of the gap |

### What the sources offered and the bank refused

Rule 3 is only real if the refusals are written down.

- **The embedded third-party document** (Polymarket's Google Doc, Futuur's Notion). It is the cheapest
  possible answer and it fails four of our own gates at once: the content is not in the page, so
  gate 9's "one source of css" is moot because the page has no content to style, gate 20's font rule
  is broken by a third-party host, the theme cannot reach it, and gate 15 cannot read its headings.
- **The regulatory hub grouped by legal entity** (Kalshi). Correct for an exchange with two
  registered entities and wrong for us: we have one, so grouping by entity would create a hierarchy
  that exists in no fact about our product.
- **The three-column docs shell** (Fingerprint). More navigation than five documents need.
- **The logo wall** (B20), and the reason is in its row.
- **A "last updated" line with nothing behind it.** Six of seven sources treat the date as
  decoration. B4 makes it a block with a version link and a changed-line, or it is not worth the row.

**No block in the bank matches any single source's composition.** The closest is Revolut, and the
bank departs from it in four places: the money answer moves from section 7 to the top (B7), the
column narrows to our own rule rather than theirs (B8), the sibling set becomes a block instead of a
breadcrumb parent (B9), and the effective-date block gains a changed-line (B4).

### Block order, mobile first (base 360px)

DOCUMENT: B1 header, B2 breadcrumb, B3 H1 + lede, **B21 prototype notice**, B4 effective-date
block, B7 money answer, B5 contents (collapsed), B6 body, B10 contact, B9 siblings, B11 footer +
bottom nav.

B7 stands above the contents on purpose. On mobile the contents is a collapsed control, so anything
below it is below a closed door; the one sentence that answers the money question is the last thing
that may sit there.

Desktop promotes B5 to a sticky left column and the body keeps its 60 to 75 character measure
rather than filling the remaining width. That is family 2, chosen over family 3 because our side
panel vocabulary already puts navigation on the left in all three trees and a right-hand contents
would be a second answer to a question the system has answered.

**THIS LINE SAID `min-width 760px` UNTIL 2026-08-19 AND THE RUNG IS 900, WHICH IS THE RAIL RUNG THE
LADDER ALREADY HAS.** The build has always used 900 and the difference was never read; measured on
`ui-visual/terms.html` by forcing the rail on at four widths, the reading column arrives at
**388px at 760, 428 at 800, 488 at 860 and its full 503 at 900**. So promoting the contents at 760
would have made the reading column **narrower than it is at 640 with no rail at all**, which is the
one thing the sentence beside it forbids: the body keeps its measure, and a rail that takes the
measure to pay for itself is a rail that has been given the wrong rung. 900 is not a compromise
here, it is the first width at which both halves of this paragraph are true at once. The ladder is
`components/tokens.css`, page frame: DESK 40rem, DETAIL 47.5rem, RAIL 56.25rem.

**AND THE SECOND HALF OF THIS PARAGRAPH DECIDES SOMETHING THE PAINT WAS NOT DOING.** "The body keeps
its measure rather than filling the remaining width" means the width is DECLARED to go unused, and
until 2026-08-19 the painted plate went on drawing a border, a bevel and a shadow around the part
that goes unused: at 1440 a 1140px plate held a 214px rail and a 600px column with 144px between
them and 153px of nothing to the right, and about.html ran 600 of 1140. The plate fits the document
now, in both trees. A declaration that a space will not be filled is also a declaration that nothing
should be drawn around it.

STATEMENT: B1, B3, **B21 prototype notice**, B15 hero, B16 resolution and custody, B17 numbers,
B18 people (LATER), B19 closing action, B11.

**WHAT `about.html` ACTUALLY HOLDS, READ FROM THE DOM 2026-08-19, AND IT IS NOT THIS ORDER.** The
page runs the DOCUMENT body shape: a breadcrumb, the H1, B21, the money answer, a link to How It
Works, then **five `feed-seo` sections** (`#what`, `#resolution`, `#money`, `#numbers`,
`#regulation`), a contact box and B9 siblings. So **B16 and B17 are built as prose sections rather
than as a custody block and a stats band**, which is a fair rendering of both; **B15 hero and B19
closing action are declared and not built at all**; and the page carries **B2, a breadcrumb this
bank gives to DOC only**. Recorded rather than quietly corrected, because two of the three are
product decisions and not layout ones: a numbers band needs numbers and a closing action needs a
destination chosen. The order above is what the bank decides, this paragraph is what the disk holds,
and `docs/backlog.md` carries the row. It is the same class as `blocks.md` line 45: the four
documents were built against `terms.html` rather than from this table.

### States

A static page has fewer than a product screen, and saying which are absent is part of the bank.

- **success** - the page. The only state MVP needs.
- **loading** - only if the document is fetched rather than shipped. That is a build decision, so
  the block bank records it as conditional rather than deciding it.
- **error / 404** - a legal URL that does not resolve goes to the existing system 404, which already
  exists in both trees. No new state.
- **empty** - does not exist for this type. A legal document with no body is a defect, not a state.

### What this bank does NOT decide, and who does

- Which of the six nodes ship at MVP. `ia/docs/sitemap.md` says "page content is post-MVP where
  marked" and marks only Contact. **Open question for IA.**
- The eight footer destinations that are on no map (`docs/backlog.md` item 27). Four of them
  (Careers, Press, Brand, Geo restrictions) would be this type if they became nodes.
- The legal text itself. The bank decides the blocks; the copy is legal review plus
  `voice/docs/microcopy.md`, in that order.
