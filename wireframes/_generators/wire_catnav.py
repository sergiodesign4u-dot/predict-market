import _shell as S

# Convert button-style category chips into real links on pages whose cat-nav was
# authored before the category pages existed (the event-feed* set). Idempotent.
updated = []
for p in sorted(S.ROOT.glob("event-feed*.html")):
    txt = p.read_text()
    if '<nav class="cat-nav"' not in txt:
        continue
    start = txt.index('<nav class="cat-nav"')
    end = txt.index('</nav>', start) + len('</nav>')
    block = txt[start:end]
    if '<a href' in block:
        continue  # already wired
    new = block
    for name, f in S.CAT_FILES.items():
        new = new.replace(f'<button type="button">{name}</button>',
                          f'<a href="{f}"><button type="button">{name}</button></a>')
    # refresh the zone note to reflect navigation
    new = new.replace('zone: second-level navigation (categories)',
                      'zone: second-level navigation (each category opens its own page)')
    if new != block:
        p.write_text(txt[:start] + new + txt[end:])
        updated.append(p.name)
print("wired cat-nav links on:", len(updated), "files")
print("\n".join(updated))
