#!/usr/bin/env python3
"""Build microcopy.md - the product-text inventory + consistency flags.

Reads microcopy_raw.json (from extract_microcopy.py). Curates product copy
(drops pure data / sample social content, which is listed separately as user
content), groups by screen, and marks consistency issues per the lesson.
"""
import json, re, os, collections

SC = os.path.dirname(os.path.abspath(__file__))
RAW = json.load(open(os.path.join(SC, "microcopy_raw.json")))
OUT = "/Users/sergiyshevchenko/Claud Projects/Project One/voice/microcopy.md"

# ---- page -> screen family ------------------------------------------------
FAMILIES = [
    ("Event Feed", ["event-feed"]),
    ("Event Detail", ["event-detail"]),
    ("Category Page", ["politics", "crypto", "culture", "general"]),
    ("My Bets", ["active-bets"]),
    ("Favorites", ["favorites"]),
    ("Deposit", ["deposit"]),
    ("Sign In / Register", ["sign-in"]),
    ("My Profile", ["my-profile"]),
    ("Public Profile", ["public-profile"]),
    ("Wallet", ["wallet"]),
    ("Notifications", ["notifications"]),
    ("How It Works", ["how-it-works"]),
    ("Win Screen", ["win"]),
    ("Loss Screen", ["loss"]),
]


def family_of(page):
    base = page[:-5]
    for fam, prefixes in FAMILIES:
        for p in prefixes:
            if base == p or base.startswith(p + "-"):
                return fam
    return None


CHROME_ZONES = ["Header", "Category nav", "Bottom nav", "Footer",
                "Sign-in dialog", "Deposit dialog"]

# ---- noise: pure data / sample values we do NOT curate as copy -------------
NOISE = re.compile(r"""^(
    \$?[\d.,]+%?                        # money / number / percent
    |\$?[\d.,]+\s*(shares|YES|NO)?      # 320 shares, $0.38
    |\d+[hmd]\ ago | \d+\ (day|days)\ ago
    |[a-z]{2}                           # avatar initials: mm, dd
    |\d+
    |x                                  # close glyph
    |YES|NO|off|on
    |[\d,]+\ shares
)$""", re.X)

# usernames / social sample handles seen in the comment + holders + activity
USERNAMES = {"marketmaven", "deadline_dan", "polly_predicts", "newhere",
             "whale_07", "alpha_ape", "satoshi_jr", "hedge_hannah", "caut_carl",
             "riskoff", "you"}
# multi-outcome option names + verbs that are sample data
SAMPLE_DATA = {"bought", "sold", "Sweden", "Italy", "Labour", "Conservatives",
               "JD Vance", "Donald Trump", "Ron DeSantis", "Nikki Haley"}

# Content-tabs strings that ARE product copy (structural). Everything else in
# that zone is sample social content -> user-content bucket.
TABS_KEEP = {"Comments", "Top Holders", "Positions", "Activity", "comments",
             "Newest", "Top", "Holders", "Add a comment...", "Post", "Reply",
             "YES holders", "NO holders", "Holder", "Side", "Shares", "Avg",
             "Value", "You", "Outcome", "Sign in to join the discussion",
             "Your row is highlighted. Positions update as the market trades.",
             "Recent trades, largest first. Filter: over $5.",
             "Sort:", "128 comments"}

# ---- FLAGS: exact-string -> marker(s) -------------------------------------
F_EVENTMARKET = "same-thing / event vs market"
F_BETPOS = "same-thing / bet vs position"
F_DEPOSIT = "same-thing / Deposit vs Add funds"
F_SAVE = "same-thing / Bookmark vs save vs Favorites"
F_AUTH = "same-thing / Log in vs Sign in"
F_CTA = "same-action / go-to-events button varies"
F_PLACEBET = "same-action / place-bet button varies"
F_CLICHE = "AI-cliche tone"
F_SPECNOTE = "leftover spec-note (internal codes)"
F_PLACEHOLDER = "placeholder"

FLAGS = collections.defaultdict(list)
def flag(marker, *strings):
    for s in strings:
        FLAGS[s].append(marker)

flag(F_EVENTMARKET, "No events match your filters",
     "There are no markets for this category and filter combination right now. Try clearing filters or switching category.",
     "View all markets", "One-time market", "By category",
     "Positions update as the market trades.", "Couldn't load events",
     "Notify me of new events in this category")
flag(F_BETPOS, "My Bets", "Couldn't load your positions",
     "Something went wrong while loading your bets. Check your connection and try again.",
     "No active bets yet", "Positions")
flag(F_DEPOSIT, "Deposit", "Add funds", "Wallet / Deposit", "Amount to add")
flag(F_SAVE, "Bookmark", "save event", "Favorites")
flag(F_AUTH, "Log in", "Sign in", "Sign up", "Sign in or create account",
     "Sign in to join the discussion")
flag(F_CTA, "See next events", "Browse events", "Find events",
     "Find events to follow", "Go to events", "Back to feed",
     "Find events to follow", "Back to your bets")
flag(F_PLACEBET, "Bet", "Confirm bet", "Confirm at new price (41%)",
     "Place your bet", "Bet $3.00 instead", "Confirm at new price")
flag(F_CLICHE, "Something went wrong reaching the network. Check your connection and try again.",
     "Something went wrong while loading your bets. Check your connection and try again.")
# spec-notes are detected by pattern (internal codes / dev rationale that leaked)
SPECNOTE_RE = re.compile(
    r"\(T\d+\)|\(S\d+\)|underlying screen dimmed|see reference pages|reference pages "
    r"|inline guard in the panel|S5 reconcile|no confetti|bet again|Opens over the current page",
    re.I)
flag(F_PLACEHOLDER, "logo placeholder", "Tagline placeholder", "thumbnail placeholder",
     "TBD", "post-MVP", "dynamic",
     "[Regulatory / licensing line - placeholder, to be set. No US real-money markets; geo-restrictions and KYC per regulatory requirements.]",
     "Copyright (c) Predict Market. Sample wireframe content.",
     "Transak payment widget (card to USDC)")
# dim-note lines (underlying screen dimmed: ...) are all spec-notes
DIMNOTE_PREFIX = "underlying screen dimmed:"


# an event question authored per market (Will / Who / Which ... ?)
EVENT_Q_RE = re.compile(r"^(Will|Who|Which|Does|Did|Are|Is|Has) .+\?$")


def is_event_title(text):
    return bool(EVENT_Q_RE.match(text)) and len(text) > 20


def is_user_content(zone, typ, text):
    if typ == "Event title (user content)":
        return True
    if is_event_title(text):
        return True
    if text in USERNAMES or text in SAMPLE_DATA:
        return True
    if zone == "Content tabs" and text not in TABS_KEEP:
        return True
    return False


def is_noise(text):
    return bool(NOISE.match(text))


def curate_rows(pages):
    """Distinct product-copy rows across the given pages, remembering an example
    source page + flags. Returns list of (zone, typ, text, flags)."""
    seen = {}
    order = []
    for page in pages:
        for r in RAW.get(page, []):
            zone, typ, text = r["zone"], r["type"], r["text"]
            if is_user_content(zone, typ, text):
                continue
            if is_noise(text):
                continue
            key = (zone, text)
            if key in seen:
                continue
            seen[key] = True
            fl = set(FLAGS.get(text, []))
            if SPECNOTE_RE.search(text):
                fl.add(F_SPECNOTE)
            order.append((zone, typ, text, sorted(fl)))
    return order


TYPE_LABEL = {"input": "Option", "Inline/label": "Label", "br": "Text",
              "Icon button (aria-label)": "Icon button"}


def esc(s):
    return s.replace("|", "\\|").replace("\n", " ")


def render_table(rows):
    out = ["| Zone | Type | Line | Flag |", "|---|---|---|---|"]
    for zone, typ, text, fl in rows:
        mark = ", ".join("**" + f + "**" for f in fl) if fl else ""
        out.append("| {} | {} | {} | {} |".format(zone, TYPE_LABEL.get(typ, typ), esc(text), mark))
    return "\n".join(out)


FINDINGS = """## Consistency findings (roll-up of the marks)

Read-only summary of every marked issue, with the exact variants and where they
appear. Nothing here is a rewrite; it is the punch-list for the editing pass.

### A. Same thing, different names

1. **event vs market** - the core object. The product mostly says *event(s)*
   (bottom-nav "Events", "Find events", "No events match your filters", "new
   events in this category") but switches to *market(s)* in the footer
   ("Markets", "By category", "View all markets"), on Event Detail ("One-time
   market"), in the tabs ("Positions update as the market trades") and in the
   feed empty body ("There are no markets for this category..."). The **Event
   Feed empty state uses both in adjacent lines**: heading "No events match your
   filters" over body "There are no markets for this category and filter
   combination."
2. **bet vs position** - *My Bets* / *place a bet* / *Bet* everywhere, but
   *position(s)* in the My Bets error ("Couldn't load your positions"), the
   "Positions" tab and "Positions update as the market trades", and the bet
   panel "View your position".
3. **Deposit vs Add funds** - the same funding action is *Deposit* (avatar item
   "Wallet / Deposit", My Profile button, Wallet button) and *Add funds* (header
   "+" control, Deposit dialog heading + button, How It Works button, bet-panel
   "Add funds"); the field is "Amount to add".
4. **Bookmark vs save vs Favorites** - one save action, three words: *Favorites*
   (header icon, bottom-nav slot, screen title), *Bookmark* + *save event*
   (Event Detail control), and the IA entity name *Saved events*.
5. **Log in vs Sign in** - the logged-out header shows *Log in* (and *Sign up*),
   while the dialog and comment prompt say *Sign in* ("Sign in or create
   account", "Sign in to join the discussion").

### B. Same action, different button labels

6. **Go to the events feed** - one destination, at least eight labels:
   "See next events" (Win), "Browse events" (Loss / How It Works / Favorites
   empty), "Find events" (My Bets empty), "Find events to follow" (Notifications
   empty), "Go to events" (Public Profile not found), "Back to feed" (Deposit
   KYC error), "Back to your bets" (Loss), plus "Notify me of new events in this
   category" (Feed empty).
7. **Place the bet** - "Bet" (panel primary) vs "Confirm bet" (intent) vs
   "Confirm at new price (41%)" (reconcile) vs the heading "Place your bet" vs
   "Bet $3.00 instead".
8. *Already consistent (keep as the standard):* retry is uniformly **"Try
   again"** (Feed / My Bets / Wallet / bet panel), and load-error headings are
   uniformly **"Couldn't load ..."**.

### C. AI-cliche / bright tone

9. **"Something went wrong ..."** on the Event Feed error and the My Bets error
   is generic filler (the Wallet error avoids it: "We couldn't fetch your
   balance..."). Otherwise the tone is already restrained: **no exclamation
   marks, no emoji, no "Congratulations / Welcome / Oops" anywhere** in the
   product text; Win is "You were right" (deliberately no confetti), Loss is
   "Here's what happened." This is a good baseline to protect.

### D. Leftover placeholders and spec-notes (not user-facing copy)

10. **Placeholders:** footer "logo placeholder", "Tagline placeholder", the
    "TBD / post-MVP / dynamic" roadmap tags, the "[Regulatory / licensing line -
    placeholder, to be set...]" strip, "Copyright ... Sample wireframe content";
    Event Detail "thumbnail placeholder"; Deposit "Transak payment widget (card
    to USDC)"; Win "Share Card ... (image placeholder)".
11. **Spec-notes / internal codes that leaked into visible text:** "underlying
    screen dimmed: ..." (Win / Loss / overlays); bet-panel rationale ("on-chain
    error (T3): ...", "insufficient-balance: inline guard...", "S5 reconcile:
    ..."); the dialog notes ("Opens over the current page ... see reference
    pages ..."); and real messages that carry a parenthetical code -
    "Your card was declined (T2)", "KYC verification was rejected (T1)", "Your
    bet did not register on-chain (T3)", "We couldn't generate your Share Card
    (T11)". The codes must come out of the user-facing copy.

### E. User-written content (do not touch)

Event questions, outcome names, per-event editorial (why-this-price, arguments,
resolution notes), share-card text, comments, usernames and holdings. Listed in
full at the end of this file.

"""


# ---- assemble --------------------------------------------------------------
def main():
    lines = []
    A = lines.append

    # chrome once, from a page that has everything
    chrome_pages = ["event-feed.html"]  # header/catnav/bottomnav/footer + dialogs
    chrome = curate_rows(chrome_pages)
    chrome_by_zone = collections.OrderedDict((z, []) for z in CHROME_ZONES)
    other = []
    for row in chrome:
        (chrome_by_zone.setdefault(row[0], [])).append(row)

    A("# Microcopy inventory - Prediction Market Platform\n")
    A("> **What this is.** A full inventory of the product interface text pulled from every "
      "`wireframes/*.html` (99 pages), with the places where screens say the same thing "
      "differently marked. **Nothing is rewritten here** - this is the read-only source of "
      "truth we will edit from next. Bootstrapped from the wireframes by "
      "`wireframes/_generators/microcopy_extract.py` + `microcopy_build.py`; from here it is "
      "**hand-maintained** (re-running the bootstrap would overwrite manual edits). The "
      "wireframes stay the render surface.\n")
    A("Columns: **Zone** (where on the screen), **Type** (heading / button / field label / "
      "placeholder / state message / link), **Line** (the exact text), **Flag** (a marked "
      "issue - see the legend). Pure data values ($0.38, 320 shares, 2h ago), avatar "
      "initials and sample social content are excluded from the copy tables and collected "
      "under **User-written content** at the end (we do not touch those).\n")

    A("## Legend of flags\n")
    A("| Flag | Meaning |")
    A("|---|---|")
    A("| **same-thing / event vs market** | one object named two ways: *event* here, *market* there |")
    A("| **same-thing / bet vs position** | *bet(s)* here, *position(s)* there for the same object |")
    A("| **same-thing / Deposit vs Add funds** | the funding action is labelled both ways |")
    A("| **same-thing / Bookmark vs save vs Favorites** | one save action, three names |")
    A("| **same-thing / Log in vs Sign in** | the auth entry is labelled both ways |")
    A("| **same-action / go-to-events button varies** | one 'take me to the feed' action, many button labels |")
    A("| **same-action / place-bet button varies** | one 'place the bet' action, many button labels |")
    A("| **AI-cliche tone** | generic / bright filler such as 'Something went wrong' |")
    A("| **leftover spec-note (internal codes)** | a developer note (T1/T2/T3, S5, 'underlying screen dimmed') that leaked into the UI, not user copy |")
    A("| **placeholder** | unfinished text (logo placeholder, TBD, licensing line, Transak widget) |")
    A("")

    A(FINDINGS)

    A("## Global chrome (shared on every screen)\n")
    A("Header, category nav, bottom nav, footer and the two shared dialogs (Sign in, "
      "Deposit) are byte-identical across pages, so they are listed once here rather than "
      "repeated per screen.\n")
    for zone in CHROME_ZONES:
        rows = chrome_by_zone.get(zone) or []
        if not rows:
            continue
        A("### " + zone + "\n")
        A(render_table(rows))
        A("")

    # per-screen (exclude the chrome zones; those are global)
    A("## Screens\n")
    for fam, prefixes in FAMILIES:
        pages = sorted(p for p in RAW if family_of(p) == fam)
        rows = [r for r in curate_rows(pages) if r[0] not in CHROME_ZONES]
        A("### " + fam + "\n")
        A("_" + str(len(pages)) + " state page(s): " + ", ".join(pages) + "_\n")
        if rows:
            A(render_table(rows))
        else:
            A("_No screen-specific copy beyond the global chrome._")
        A("")

    # user content
    A("## User-written content (do NOT rewrite)\n")
    A("These lines are authored per event or by other users - event questions, outcome "
      "names, the per-event editorial (why-this-price, arguments, resolution notes), share "
      "cards, comments, usernames and holdings. Our voice work does not touch them; they get "
      "a separate content guideline for whoever creates markets.\n")
    uc = collections.defaultdict(set)
    for page, rows in RAW.items():
        fam = family_of(page)
        for r in rows:
            if is_user_content(r["zone"], r["type"], r["text"]):
                uc[fam].add(r["text"])
    # event titles specifically
    titles = sorted({r["text"] for rows in RAW.values() for r in rows
                     if r["type"] == "Event title (user content)" or is_event_title(r["text"])})
    A("**Event questions (titles):**\n")
    for t in titles:
        A("- " + t)
    A("")
    A("**Outcome names / sample social content (comments, usernames, holdings, trades):** "
      "marketmaven, deadline_dan, polly_predicts, newhere, whale_07, alpha_ape, satoshi_jr, "
      "hedge_hannah, caut_carl, riskoff; outcome options JD Vance / Donald Trump / Ron "
      "DeSantis / Nikki Haley, Sweden / Italy, Labour / Conservatives; plus every comment "
      "body and the per-event *Why this price* / *For YES* / *For NO* / *Resolution "
      "conditions* / *What happened* narrative and the auto-generated *Share Card* text.\n")

    open(OUT, "w").write("\n".join(lines) + "\n")
    print("wrote", OUT, "-", len(lines), "lines")


if __name__ == "__main__":
    main()
