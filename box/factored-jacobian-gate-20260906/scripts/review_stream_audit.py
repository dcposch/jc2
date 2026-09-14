#!/usr/bin/env python3
"""Fable gate: stream/serialization audit. Validates JSONL structure, footer, labels,
per-row flint invariants (600-var ctx, degrevlex), variable census, and byte-level
relation of complete_checked.sing / complete_export.sing to the JSONL. Read-only."""
import json, hashlib, re, time, resource, sys
from pathlib import Path
from flint import fmpq_mpoly, fmpq_mpoly_ctx
PILOT = Path('/home/ubuntu/factored-jacobian-pilot-20260906'); OUT = Path('/home/ubuntu/factored-jacobian-review-20260906')
T0 = time.monotonic()
def wrap(text):
    assert re.search(r"\^\d+/", text) is None, 'fraction after exponent'
    return re.sub(r"(?<![A-Za-z0-9_^])(\d+)/(\d+)", r"(\1/\2)", text)
assert wrap("1/2*x^9-3/4*y") == "(1/2)*x^9-(3/4)*y"
res = {"checks": {}}
def rec(name, ok, **kw):
    res["checks"][name] = {"ok": bool(ok), **kw}; print(("PASS " if ok else "FAIL ")+name, json.dumps(kw)[:300], flush=True)
    if not ok: res['any_fail'] = True
jl = (PILOT/'complete_export.generators.jsonl').open()
header = json.loads(jl.readline()); names = header['variables']
ctx = fmpq_mpoly_ctx.get(tuple(names), ordering='degrevlex'); gens = ctx.gens(); idx = {n: i for i, n in enumerate(names)}
chk = (PILOT/'complete_checked.sing').open(); orig = (PILOT/'complete_export.sing').open()
ringline = "ring R=0,(" + ",".join(names) + "),dp;"
c1, o1 = chk.readline().rstrip('\n'), orig.readline().rstrip('\n')
rec('sing_ring_line', c1 == ringline and o1 == ringline)
c2, o2 = chk.readline().rstrip('\n'), orig.readline().rstrip('\n')
rec('sing_ideal_line', c2 == 'ideal I=' and o2 == 'ideal I=')
ident = re.compile(r'[A-Za-z_][A-Za-z_0-9]*')
inv = open(OUT/'flint_row_invariants.tsv', 'w')
inv.write("k\tlabel\tterms\tdegree\tleadcoef\tleadmonom\ttrailcoef\ttrailmonom\n")
def mono(exps):
    return "*".join(f"{names[i]}^{e}" if e > 1 else names[i] for i, e in enumerate(exps) if e) or "1"
count = 0; terms = 0; digest = hashlib.sha256(); labels = set(); occurs = set(); footer = None
wrapped_differs = 0; unwrapped_has_slash = 0; unsafe = 0; rows_with_rational = 0
var_in_row_not_declared = 0; maxdeg = 0; maxterms = (0, None); zj_rows = []
label_kinds = {"define": 0, "inverse": 0, "J": 0}
J_positions = set()
for line in jl:
    row = json.loads(line)
    if row['type'] == 'complete':
        footer = row; rec('no_trailing_jsonl', jl.read().strip() == ''); break
    assert row['type'] == 'generator' and row['index'] == count
    lab = row['label']; assert lab not in labels; labels.add(lab)
    text = row['polynomial']
    p = fmpq_mpoly(text, ctx=ctx)
    assert bool(p) and len(p) == row['terms'] and int(p.total_degree()) == row['degree'], f'field mismatch at {lab}'
    ids = set(ident.findall(text)); occurs |= ids
    if not ids <= set(names): var_in_row_not_declared += 1
    if 'Zj' in ids: zj_rows.append(lab)
    if lab.startswith('define_Hfact_'):
        label_kinds['define'] += 1; v = lab[len('define_'):]
        r = p - gens[idx[v]]; d = r.degrees()
        assert all(d[idx[n]] == 0 for n in names if n.startswith('Hfact_') or n == 'Zj'), 'non-monic/non-source definition'
    elif lab == 'inverse_J': label_kinds['inverse'] += 1
    else:
        m = re.fullmatch(r'J_(\d+)_(\d+)', lab); assert m and (int(m.group(1)), int(m.group(2))) != (0, 0); label_kinds['J'] += 1
        J_positions.add((int(m.group(1)), int(m.group(2))))
    # serialization relation
    cl = chk.readline().rstrip('\n'); ol = orig.readline().rstrip('\n')
    pre = ',' if count else ''
    w = wrap(text)
    if cl != pre + w: wrapped_differs += 1
    if ol != pre + text: unsafe += 1
    if '/' in text: rows_with_rational += 1
    if w != text: pass
    # invariants
    lc, lm = p.coefficient(0), p.monomial(0); tc, tm = p.coefficient(len(p)-1), p.monomial(len(p)-1)
    inv.write(f"{count+1}\t{lab}\t{len(p)}\t{int(p.total_degree())}\t{lc}\t{mono(lm)}\t{tc}\t{mono(tm)}\n")
    digest.update(line.encode()); count += 1; terms += len(p); maxdeg = max(maxdeg, int(p.total_degree()))
    if len(p) > maxterms[0]: maxterms = (len(p), lab)
    if count % 300 == 0: print(json.dumps({"rows": count, "terms": terms, "t": round(time.monotonic()-T0, 1)}), flush=True)
inv.close()
rec('footer', footer is not None and footer['generators'] == count == 1629 and footer['terms'] == terms == 11299180 and footer['generator_stream_sha256'] == digest.hexdigest() and footer['maximum_semantic_degree'] == maxdeg == 12,
    generators=count, terms=terms, maxdeg=maxdeg, maxterms=maxterms)
rec('label_kinds', label_kinds == {"define": 160, "inverse": 1, "J": 1468}, **label_kinds)
rec('Zj_only_in_inverse', zj_rows == ['inverse_J'])
rec('all_row_identifiers_declared', var_in_row_not_declared == 0)
missing = [n for n in names if n not in occurs]
rec('every_declared_variable_occurs', not missing, missing=missing)
rec('checked_sing_rows_equal_wrapped_jsonl', wrapped_differs == 0, rows_with_rational=rows_with_rational)
rec('original_sing_rows_equal_unwrapped_jsonl', unsafe == 0)
ctail = chk.read(); otail = orig.read()
expected_tail = ';\nprint("ALL_ROWS_PARSED"); print("GENERATORS="+string(size(I))); print("VARIABLES="+string(nvars(basering))); print("END_PARSE"); quit;\n'
rec('sing_footers', ctail == expected_tail and otail == expected_tail, checked_tail=ctail[-160:], original_tail=otail[-160:])
res['J_positions_by_degree'] = {}
for i, j in J_positions: res['J_positions_by_degree'][i+j] = res['J_positions_by_degree'].get(i+j, 0)+1
res['export_json_coordinate_order_matches'] = json.loads((PILOT/'complete_export.json').read_text())['coordinate_order'] == names
res['wall_seconds'] = time.monotonic()-T0; res['peak_rss_kib'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
(OUT/'stream_audit_result.json').write_text(json.dumps(res, sort_keys=True, indent=1)+'\n')
print('DONE any_fail=', res.get('any_fail', False))
