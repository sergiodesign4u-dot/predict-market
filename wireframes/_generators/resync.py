import _shell as S

updated = []
for p in sorted(S.ROOT.glob("*.html")):
    txt = p.read_text()
    if '<nav class="wf-nav"' not in txt:
        continue
    start = txt.index('<nav class="wf-nav"')
    end = txt.index('</nav>', start) + len('</nav>')
    newnav = S.nav_tree(p.name).lstrip()
    txt2 = txt[:start] + newnav + txt[end:]
    if txt2 != txt:
        p.write_text(txt2)
        updated.append(p.name)
print(f"resynced {len(updated)} files:")
print("\n".join(updated))
