# System and global nodes - IA Detailed layer (Stage 03b)

The nodes that do not belong to any cluster and are easy to forget: error and maintenance
pages, the cookie-consent banner, and toasts. Part of the IA Detailed layer (targeted
reconcile). The wireframes carry per-screen error and loading states, but none of these
global system nodes exist as dedicated pages or components yet; this file specs them.

Legal claims (the cookie banner) are grounded in real sources, cited at the end, not invented.
Where a requirement is uncertain it is marked `[?]`. Ready product copy is shown as literal
strings; it follows the product voice (name what happened and the way out, no apology, no
joke, no "something went wrong", no exclamation). No em dash.

## Overview

| Node | Type | HTTP | Robots | Never a dead-end |
|---|---|---|---|---|
| 404 Not Found | page | `404` | `noindex,follow` | search or quick links + home |
| 500 Server Error | page | `500` | `noindex` | retry + home, funds reassurance |
| 503 Maintenance | page | `503` + `Retry-After` | `noindex` | retry + expected time |
| Cookie consent | component (banner) | n/a | n/a | dismissible, reopenable from footer |
| Toast / notification | component | n/a | n/a | auto-dismiss + manual close |
| Search | page + 2 states | `200` | `noindex,follow` | the field itself, the category strip, and a no-match block with two ways out |

Search was **deferred** in `sitemap.md` ("Search - Deferred until catalog scale") and was **built on
2026-08-16**, at 25 events rather than at scale. The indexation policy recorded here and in `seo.md`
is what shipped: `event-feed-search.html` and its two states are `noindex,follow`, and the no-match
state offers two ways out, "Browse all events" and "How events are chosen".

**The 404 is the reason this row moved, and it had been arguing for it in the markup.** The
"never a dead-end" column above has said "search or quick links + home" since this table was
written; the page shipped the quick links, and drew `i-magnifer-o` over "This page does not exist"
for a control that did not exist. It now carries "Search events" in its quick-link list, which makes
the icon a promise the product keeps.

---

## 1. 404 Not Found

- Type: page - a full page with the global header and footer, not a bare message
- HTTP status: `404` (a real 404, never a soft-404 that returns `200`) - `noindex,follow`
- Purpose: a broken or old link, or a removed event, must still land the user somewhere useful

Content:
- H1 and a one-line reason
- A primary way forward (Browse events) plus quick links to the four categories and How it works
- The global header and footer stay, so the user is never stranded

Ready copy:
- H1: **This page does not exist**
- Body: **The link may be old, or the event may have been removed.**
- Primary action: **Browse events** - secondary: the four categories, How it works, Home

a11y / SEO: a real `404` status so crawlers drop the URL; the page is `noindex` but its links
are followed; it is reachable from any bad URL and is never a dead-end.

---

## 2. 500 Server Error

- Type: page - a minimal template that does not depend on the backend that just failed
- HTTP status: `500` - `noindex`
- Purpose: name that the fault is on our side, reassure on money, offer a retry

Content:
- H1 and a one-line, plain reason (server-side, not the user's bet or funds)
- A retry action and a way home
- A one-line funds reassurance (the trust principle applies even in an error)

Ready copy:
- H1: **We could not load this page**
- Body: **This is on our side, not your bet or your funds. Your money is safe.**
- Primary action: **Try again** - secondary: **Home**

a11y / SEO: served with a `500` status; static template (inline critical CSS) so it renders
even if the app server is down; `noindex`.

---

## 3. 503 Maintenance

- Type: page - a static template for planned downtime, independent of the backend
- HTTP status: `503` with a `Retry-After` header (tells crawlers to come back, keeps rankings)
- Purpose: planned maintenance, not a crash; set expectation and reassure

Content:
- H1 and a one-line note that this is scheduled
- A funds-and-bets reassurance and, where known, an expected return time
- A retry action

Ready copy:
- H1: **Yonder is down for scheduled maintenance**
- Body: **Your bets and funds are safe. We will be back shortly.** (add the expected time when known)
- Primary action: **Try again**

a11y / SEO: `503` + `Retry-After` is the correct signal (not `200`, not `404`), so search does
not treat downtime as content loss; `noindex`.

---

## 4. Cookie consent (banner component)

- Type: component (a banner, not a page); appears on first visit before non-essential cookies are set
- Purpose: obtain valid prior consent for non-essential cookies, and let the user change it later

**Grounding.** The product is global with geo-restrictions, so it is built to the strictest
common bar, GDPR and the ePrivacy Directive, which also satisfies Ukraine's less prescriptive
law. The rules that shape this component:
- **Prior consent.** Non-essential cookies (analytics, marketing) are blocked until the user
  opts in. Setting them on landing, or treating "continue browsing" or scrolling as consent, is
  not valid. [1][2][4]
- **Reject as easy as accept.** "Reject all" has the same prominence as "Accept all" - same
  level, same weight, not a small "Manage" link that hides the reject path. [1][3]
- **No pre-ticked boxes.** Analytics and marketing are unticked by default; the user actively
  turns them on. [1][3]
- **Granular and withdrawable.** Consent is per category and can be changed or withdrawn at any
  time, as easily as it was given. [2][4]
- **Ukraine.** Law No. 2297-VI requires prior consent with the privacy policy readable first;
  there is no statutory cookie definition or mandated banner, but a banner is the practical way
  to obtain informed consent, and cookies-on-landing via inaction are not proper consent. [5][6]

Structure:
- A short plain explanation and a link to the Privacy policy and Cookie policy (register both in `sitemap.md`, Step 7)
- Three top-level actions of equal prominence: **Accept all**, **Reject all**, **Manage**
- Manage opens per-category toggles: **Necessary** (always on, control disabled and explained), **Analytics** (off by default), **Marketing** (off by default)
- Re-entry: a **Cookie preferences** link in the footer reopens this banner so the choice can be changed later

Ready copy:
- Text: **We use cookies to run the site and, only if you allow it, to measure and improve it.**
- Actions: **Accept all** - **Reject all** - **Manage**
- Toggle labels: **Necessary (always on)** - **Analytics** - **Marketing**
- Footer re-entry: **Cookie preferences**

a11y: keyboard reachable, focus trapped in the banner until a choice is made, the three actions
are real buttons with equal visual weight (no dark pattern). No SEO impact.

---

## 5. Toast / notification (component)

- Type: component - a transient message for the result of an action; not a page, no own URL, no SEO impact
- Purpose: confirm an action or report a failure inline, then get out of the way

Behavior:
- Appears briefly, auto-dismisses, and also has a manual close
- `aria-live="polite"` for confirmations, `aria-live="assertive"` for errors, so screen readers announce it
- Does not block the page; never the only place a critical error is shown

Ready copy (voice: state the fact and the next step, no celebration):
- Success: **Bet placed** - **Funds added** - **Saved into Favorites**
- Error: **We could not place your bet. Try again.**

---

## References

1. Secure Privacy - GDPR Cookie Consent Requirements 2025: prior consent, reject as easy as accept, dark-pattern enforcement (CNIL EUR 325M fine, Sept 2025). https://secureprivacy.ai/blog/gdpr-cookie-consent-requirements-2025
2. EU ePrivacy Directive (the "cookie law") overview. https://www.recordinglaw.com/world-laws/world-data-privacy-laws/eu-data-privacy-laws/eprivacy-directive-cookie-law/
3. Termly - Pre-ticked GDPR checkboxes for cookies are not allowed. https://termly.io/resources/articles/gdpr-checkboxes/
4. Your Europe (European Commission) - Online privacy: how to use cookies. https://europa.eu/youreurope/business/dealing-with-customers/data-protection/online-privacy/index_en.htm
5. Sayenko Kharenko - Ukraine: Cookies and similar technologies (Law No. 2297-VI, prior consent, no statutory cookie definition). https://sk.ua/ukraine-cookies-similar-technologies/
6. DataGuidance - Ukraine: Cookies and similar technologies (implied consent hard to prove; cookies-on-landing not proper consent). https://www.dataguidance.com/notes/ukraine-cookies-similar-technologies
