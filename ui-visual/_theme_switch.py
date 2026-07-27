#!/usr/bin/env python3
"""
_theme_switch.py  -  the theme boot script, injected into the head of every page
that carries the switch.

WHY IT IS INLINE AND WHY IT IS IN THE HEAD. The stored choice has to be on the
<html> element before the first paint, or the page shows one theme and then
snaps to the other. That rules out the end of the body, and an external file
would still be a request the browser can miss when a page is opened straight off
the disk. So: one small inline block, first thing in the head, and it is the
only script on a painted screen that is allowed there.

WHAT IT IS NOT. This is a harness, not a product feature. The switch exists to
prove that the semantic layer holds when the ground inverts (see section 3 of
components/tokens.css). Whether daylight ships is a separate decision, and
`--strip` is how it leaves: one command and there is no trace.

The markup of the button is NOT here. It lives in the two sidebar renderers,
because that is where each tree already keeps its single source:
  ui-visual/_resync_sidebar.py   -> the screen tree on the 76 painted screens
  ui-kit/_gen_component_pages.py -> _nav.js, the panel on the stand pages
Both of them import BOOT from this file, so the behaviour is written once.

Usage:
    python3 _theme_switch.py            # inject into every painted screen
    python3 _theme_switch.py --check    # report what would change, write nothing
    python3 _theme_switch.py --strip    # remove it again
No em dash.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# The id is what makes this idempotent, and it is also what ui-kit/_check_kit.py
# masks in gate 1: a boot script is chrome wrapped around the screen, the same
# way the sidebar is, so a page carrying it has not moved as a screen.
BOOT = """<script id="uvTheme">/* theme boot: applied before the first paint, so daylight never flashes graphite.
   A frame is a document of its own, so it does not inherit the attribute: this
   block runs in the frames too and they are told by postMessage, the same
   handshake _frames.js already uses, because from file:// every document has
   its own opaque origin and reading into a frame is refused.
   Built by ui-visual/_theme_switch.py. Remove with --strip. */
(function(){var K='pm-theme',r=document.documentElement;
try{if(localStorage.getItem(K)==='light')r.setAttribute('data-theme','light')}catch(e){}
function lit(){return r.getAttribute('data-theme')==='light'}
function set(on){if(on){r.setAttribute('data-theme','light')}else{r.removeAttribute('data-theme')}}
function push(){var f=document.getElementsByTagName('iframe');
for(var i=0;i<f.length;i++){try{f[i].contentWindow.postMessage({pmTheme:lit()?'light':'dark'},'*')}catch(e){}}}
function paint(){var all=document.querySelectorAll('.theme-switch');
for(var i=0;i<all.length;i++){all[i].setAttribute('aria-pressed',lit()?'true':'false');
var l=all[i].querySelector('.ts-label');if(l)l.textContent=lit()?'Daylight':'Vault';}
push();}
function wire(){var all=document.querySelectorAll('.theme-switch');
for(var i=0;i<all.length;i++){if(all[i].dataset.wired)continue;all[i].dataset.wired='1';
all[i].addEventListener('click',function(){var on=lit();set(!on);
try{localStorage.setItem(K,on?'dark':'light')}catch(e){}paint();});}
paint();}
window.addEventListener('message',function(e){var d=e.data;
if(!d||(d.pmTheme!=='light'&&d.pmTheme!=='dark'))return;
set(d.pmTheme==='light');paint();});
document.addEventListener('DOMContentLoaded',function(){wire();
/* the kit side panel is rendered by _nav.js after this fires, so wire once more */
setTimeout(wire,0);
/* a frame that arrives late is told as soon as it is ready */
var f=document.getElementsByTagName('iframe');
for(var i=0;i<f.length;i++){f[i].addEventListener('load',push);}
push();});})();</script>"""

# The button. Selected by class and not by id, because the hub carries it twice:
# once in the panel and once in the page head, and both have to work.
# One label, two swatches: the swatches say what the two grounds look like, the
# ring says which one you are standing on, and the label names the other one.
def button(inline=False):
    """the switch. `inline` is the hub-header variant: same control, laid out in a
       row instead of as the last item of a panel. The variant is a class on the
       component, not a rule in the stand sheet, so the vitrine never styles the
       system."""
    return BUTTON.replace('class="theme-switch"',
                          'class="theme-switch theme-switch-inline"') if inline else BUTTON


BUTTON = ('<button type="button" class="theme-switch" aria-pressed="false">'
          '<span class="ts-swatches" aria-hidden="true">'
          '<span class="ts-sw ts-dark"></span><span class="ts-sw ts-light"></span></span>'
          '<span class="ts-label">Vault</span></button>')

BOOT_RE = re.compile(r'\n?<script id="uvTheme">.*?</script>', re.DOTALL)
HEAD_RE = re.compile(r"(<head>)", re.IGNORECASE)


def process(path, mode):
    with open(path, "r", encoding="utf-8") as fh:
        html = fh.read()
    has = BOOT_RE.search(html)
    if mode == "strip":
        if not has:
            return "unchanged"
        new = BOOT_RE.sub("", html)
    else:
        if has:
            # rewrite in place, so an edit to BOOT reaches every page
            new = BOOT_RE.sub("\n" + BOOT, html)
            if new == html:
                return "unchanged"
        else:
            if not HEAD_RE.search(html):
                return "no-head"
            new = HEAD_RE.sub(lambda m: m.group(1) + "\n" + BOOT, html, count=1)
    if mode != "check":
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new)
    return "stripped" if mode == "strip" else "updated"


def main():
    mode = ("strip" if "--strip" in sys.argv else
            "check" if "--check" in sys.argv else "build")
    counts = {}
    for fname in sorted(os.listdir(HERE)):
        if not fname.endswith(".html"):
            continue
        status = process(os.path.join(HERE, fname), mode)
        counts[status] = counts.get(status, 0) + 1
    for status in sorted(counts):
        print("%-10s %d" % (status, counts[status]))


if __name__ == "__main__":
    main()
