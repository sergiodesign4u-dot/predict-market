import _shell as S

# event-feed*.html were authored in a prior session (not emitted by assemble()),
# so inject the shared dialogs + wire the logged-out triggers here. Idempotent.
TRIGGERS = [
    ('class="icon-btn desk-only" aria-label="Favorites (sign in to save)"',
     'class="icon-btn desk-only" data-open="signin" aria-label="Favorites (sign in to save)"'),
    ('class="icon-btn" aria-label="Notifications (sign in)"',
     'class="icon-btn" data-open="signin" aria-label="Notifications (sign in)"'),
    ('<button type="button" class="auth-btn">Log in</button>',
     '<button type="button" class="auth-btn" data-open="signin">Log in</button>'),
    ('<button type="button" class="auth-btn primary">Sign up</button>',
     '<button type="button" class="auth-btn primary" data-open="signin">Sign up</button>'),
    ('<button type="button" aria-label="Sign in">',
     '<button type="button" data-open="signin" aria-label="Sign in">'),
]

updated = []
for p in sorted(S.ROOT.glob("event-feed*.html")):
    txt = p.read_text()
    orig = txt
    if 'id="signinDialog"' not in txt:
        txt = txt.replace("</body>", S.SIGNIN_DIALOG + "\n" + S.DEPOSIT_DIALOG + "\n" + S.DIALOG_JS + "\n</body>", 1)
    for old, new in TRIGGERS:
        if old in txt:
            txt = txt.replace(old, new)
    if txt != orig:
        p.write_text(txt)
        updated.append(p.name)
print("injected dialogs / wired triggers on:", len(updated), "feed pages")
print("\n".join(updated))
