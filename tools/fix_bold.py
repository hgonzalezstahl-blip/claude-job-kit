#!/usr/bin/env python
"""
Fix OVER-BOLD resume bullets so they match a clean resume's pattern:
bold only the LEAD PHRASE (to the first comma) + the METRICS (numbers), plain the rest.
A whole bullet in bold reads as AI-generated clutter.

Usage:
  py tools/fix_bold.py "<path to a Resume .docx OR a folder>"

Makes a .bak backup next to each file before editing. Generic: no personal data.
Only touches long, fully-bold body bullets that appear after the first ALL-CAPS
section header. Leaves the name, the tagline, section headers, role titles, and
already-partial bullets alone.
"""
import sys, os, glob, re, copy, shutil
try:
    from docx import Document
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
except ImportError:
    print("python-docx is not installed. Run:  py -m pip install python-docx")
    sys.exit(2)

METRIC = re.compile(r'\S*\d\S*')  # any token containing a digit ($17M, 5,200+, 44%, 8,000)

def is_allcaps(t):
    L = [c for c in t if c.isalpha()]
    return bool(L) and all(c.isupper() for c in L)

def fully_bold(p):
    rs = [r for r in p.runs if r.text.strip()]
    return bool(rs) and all(r.bold for r in rs)

def lead_end(full):
    for sep in [', ', ' – ', ' — ', ': ']:
        i = full.find(sep)
        if 12 <= i <= 70:
            return i
    s = 0; c = 0
    for w in full.split(' '):
        s += len(w) + 1; c += 1
        if c >= 7 or s >= 55:
            break
    return min(s, len(full))

def set_b(r_el, bold):
    rPr = r_el.find(qn('w:rPr'))
    if rPr is None:
        rPr = OxmlElement('w:rPr'); r_el.insert(0, rPr)
    b = rPr.find(qn('w:b')); bcs = rPr.find(qn('w:bCs'))
    if bold:
        if b is None: rPr.append(OxmlElement('w:b'))
    else:
        if b is not None: rPr.remove(b)
        if bcs is not None: rPr.remove(bcs)

def make_run(template_el, text, bold):
    r = copy.deepcopy(template_el)
    for t in r.findall(qn('w:t')): r.remove(t)
    for tab in r.findall(qn('w:tab')): r.remove(tab)
    set_b(r, bold)
    t = OxmlElement('w:t'); t.set(qn('xml:space'), 'preserve'); t.text = text
    r.append(t)
    return r

def normalize(p):
    runs = p.runs
    if not runs: return
    full = "".join(r.text for r in runs)
    if not full.strip(): return
    template = runs[0]._element
    le = lead_end(full)
    mask = [i < le for i in range(len(full))]
    for m in METRIC.finditer(full):
        for i in range(m.start(), m.end()):
            if i < len(mask): mask[i] = True
    segs = []; i = 0
    while i < len(full):
        j = i
        while j < len(full) and mask[j] == mask[i]: j += 1
        segs.append((full[i:j], mask[i])); i = j
    for r in list(runs): p._p.remove(r._element)
    for text, bold in segs:
        p._p.append(make_run(template, text, bold))

def fix_file(path):
    d = Document(path)
    seen = False; targets = []
    for p in d.paragraphs:
        t = p.text.strip()
        if is_allcaps(t): seen = True
        if seen and t and len(t) > 70 and fully_bold(p):
            targets.append(p)
    if not targets:
        print(f"[ok] no over-bold bullets: {os.path.basename(path)}"); return 0
    shutil.copy(path, path + ".bak")
    for p in targets: normalize(p)
    d.save(path)
    print(f"[fixed {len(targets)}] {os.path.basename(path)}  (backup: {os.path.basename(path)}.bak)")
    return len(targets)

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    target = sys.argv[1]
    files = (glob.glob(os.path.join(target, "**", "Resume*.docx"), recursive=True)
             if os.path.isdir(target) else [target])
    if not files:
        print("No Resume*.docx found at:", target); sys.exit(2)
    total = sum(fix_file(f) for f in sorted(files))
    print(f"\nDone. Fixed {total} over-bold bullet(s). Re-run verify_docx.py to confirm.")

if __name__ == "__main__":
    main()
