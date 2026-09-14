#!/usr/bin/env python3
"""Mod-p mirror of fast_compress.py: same block regeneration, coefficients in F_p.

Lemma (pivot substitution). If a generator row r of an ideal I in k[v, w...] has
the form r = u*v - q(w...) with u a nonzero constant of k and q free of v, then
the k-algebra map phi: v |-> q/u, w |-> w carries I onto phi(I) in k[w...] and
V(I) -> V(phi(I)) is a bijection with inverse (w) |-> (q(w)/u, w). Hence I and
phi(I) have the same solution set up to the graph coordinate v.

Every hypothesis is checked mechanically per pivot below:
  (H1) linear-monic:      d r / d v == u, a nonzero CONSTANT of F_p
  (H2) no other v:        substitute(r, v, rhs) == {} (row vanishes exactly)
  (H3) rhs is v-free:     d rhs / d v == {}
  (H4) closure at end:    no eliminated variable occurs in any block/row/image
Order-independence follows because each phi_i is an isomorphism on its own
polynomial ring and the composite depends only on the set of pivots via (H4).
"""
import sys
sys.dont_write_bytecode = True
import argparse, hashlib, importlib.util, json, re, resource, time
from collections import Counter, defaultdict
from pathlib import Path
from flint import nmod, fmpz

EXTRACTOR_SHA = "a1c24fc7b7b4732ec3a78efe968763abe9846418bab80fff8e7128a224386516"
P = None

def K(v): return nmod(v, P)

def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()

def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")

def substitute(poly, variable, rhs):
    out = {}
    powers = {0: {(): K(1)}, 1: rhs}
    for mon, coeff in poly.items():
        exponent = mon.count(variable)
        if not exponent:
            value = out.get(mon, 0) + coeff
            if value: out[mon] = value
            else: out.pop(mon, None)
            continue
        if not rhs: continue
        for e in range(2, exponent + 1):
            if e not in powers: powers[e] = SP.pp_mul(powers[e-1], rhs)
        other = tuple(i for i in mon if i != variable)
        for rm, rc in powers[exponent].items():
            product = SP.merge_monomials(other, rm)
            value = out.get(product, 0) + coeff * rc
            if value: out[product] = value
            else: out.pop(product, None)
    return out

def subst_blocks(blocks, variable, rhs):
    result = {}
    for name, table in blocks.items():
        result[name] = {}
        for xy, poly in table.items():
            value = substitute(poly, variable, rhs)
            if value: result[name][xy] = value
    return result

def derivative(poly, variable):
    out = {}
    for mon, coeff in poly.items():
        e = mon.count(variable)
        if e:
            j = mon.index(variable)
            out[mon[:j] + mon[j+1:]] = coeff * e
    return out

def candidate(poly, forbidden):
    possible = {m[0] for m in poly if len(m) == 1 and m[0] not in forbidden}
    for mon in poly:
        if len(mon) > 1:
            possible.difference_update(mon)
            if not possible: return None
    return min(possible) if possible else None

def regenerate(blocks, e, q, c_index, ell):
    one = {(0, 0): {(): K(1)}}
    Pl = [(one, e)] + [(blocks[f"AA{i}"], e-i) for i in range(1, e+1)]
    Ql = [(one, q)] + [(blocks[f"BB{i}"], q-i) for i in range(2, q+1)]
    levels = defaultdict(dict)
    h = blocks["h"]
    for left, r in Pl:
        for right, s in Ql:
            SP.bp_addto(levels[r+s], SP.bp_jac(left, right))
            if r+s:
                lower = {}
                if s: SP.bp_addto(lower, SP.bp_scaled_product(right, SP.bp_jac(left, h), s))
                if r: SP.bp_addto(lower, SP.bp_scaled_product(left, SP.bp_jac(h, right), r))
                SP.bp_addto(levels[r+s-1], lower)
    powers = {0: one}
    top = max((i for i, table in levels.items() if table), default=0)
    for i in range(1, top+1): powers[i] = SP.bp_mul(powers[i-1], h)
    result = {}
    for level in sorted(levels):
        if levels[level]: SP.bp_addto(result, SP.bp_mul(levels[level], powers[level]))
    target = result.setdefault((ell, 0), {})
    SP.pp_addto(target, {(c_index,): K(1)}, -1)
    if not target: del result[(ell, 0)]
    return result

def text(poly, names):
    """Canonical F_p text: coefficients in [0,p), same monomial order as pp_text."""
    pieces = []
    for mon, coefficient in sorted(poly.items(), key=lambda it: (-len(it[0]), it[0])):
        counts = Counter(mon)
        factors = [names[n] if pw == 1 else f"{names[n]}^{pw}" for n, pw in sorted(counts.items())]
        a = int(coefficient) % P
        body = (("" if a == 1 else str(a) + "*") + "*".join(factors)) if factors else str(a)
        pieces.append(body if not pieces else "+" + body)
    return "".join(pieces) or "0"

def controls():
    a, b, c = 0, 1, 2
    f = {(a,a,b): K(1), (a,): K(3), (b,): K(1)}
    rhs = {(b,): K(1), (): K(1)}
    assert substitute(f, a, rhs) == {(b,b,b): K(1), (b,b): K(2), (b,): K(5), (): K(3)}
    positive = {(a,): K(3), (b,b): K(1), (): K(-2)}
    assert candidate(positive, {c}) == a
    right = {(b,b): K(-1)/K(3), (): K(2)/K(3)}
    assert derivative(positive, a) == {(): K(3)}
    assert not substitute(positive, a, right)
    assert candidate({(a,): K(1), (a,a): K(1)}, {c}) is None
    assert candidate({(a,): K(1), (a,b): K(1)}, {c}) is None
    assert candidate({(c,): K(1), (a,a): K(1)}, {c}) is None
    toy = {"h": {(0,2): {(): K(1)}, (1,0): {(a,): K(1)}, (0,0): {(b,): K(1)}},
           "AA1": {(0,1): {(a,): K(1)}, (1,0): {(b,): K(1)}},
           "AA2": {(0,0): {(b,): K(1)}},
           "AA3": {(1,1): {(a,): K(1)}},
           "BB2": {(1,0): {(a,): K(1)}, (0,1): {(b,): K(1)}}}
    before = regenerate(toy, 3, 2, c, 0)
    mapped = {xy: substitute(poly, a, right) for xy, poly in before.items()}
    mapped = {xy: poly for xy, poly in mapped.items() if poly}
    assert regenerate(subst_blocks(toy, a, right), 3, 2, c, 0) == mapped
    print("CONTROL_ARBITRARY_SUBSTITUTION=PASS", flush=True)
    print("CONTROL_NONLINEAR_MIXED_AND_C_PIVOTS_REJECTED=PASS", flush=True)
    print("CONTROL_REGENERATION_EQUALS_ROW_MAP=PASS", flush=True)

def main():
    global SP, P
    ap = argparse.ArgumentParser()
    ap.add_argument("--directory", required=True, type=Path)
    ap.add_argument("--roster", required=True, type=Path)
    ap.add_argument("--extractor", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    ap.add_argument("--modulus", required=True, type=int)
    ap.add_argument("--deadline-seconds", type=float, default=1e18)
    ap.add_argument("--reduction-control", action="store_true")
    args = ap.parse_args()
    P = args.modulus
    assert fmpz(P).is_prime(), "modulus must be prime for F_p pivot inversion"
    started = time.monotonic()
    assert sha(args.extractor) == EXTRACTOR_SHA
    spec = importlib.util.spec_from_file_location("fast_sparse_exact", args.extractor)
    SP = importlib.util.module_from_spec(spec); spec.loader.exec_module(SP)
    controls()
    source = args.directory.resolve(); out = args.output.resolve()
    out.mkdir(exist_ok=False)
    meta = json.loads((source/"meta.json").read_text())
    row = next(json.loads(l) for l in args.roster.read_text().splitlines()
               if json.loads(l)["row_id"] == meta["row_id"])
    rc = row["receiver_chart"]
    program = (source/"pinned-builder.sing").read_text()
    assert hashlib.sha256(program.encode()).hexdigest() == rc["production_emitter_dry_run"]["emitted_program_sha256"]
    names = meta["variables"]
    assert len(names) == len(set(names)) == rc["unknowns_without_T"]
    assert names[-1] == "c"
    match = re.search(r"^ring R=0,\((.*?)\),\(lp\(1\),dp\((\d+)\)\);$", program, re.M)
    assert match and match[1].split(",") == ["y","x"] + names
    indices = {v: i for i, v in enumerate(names)}
    setup = dict(re.findall(r"^poly (h|AA\d+|BB\d+) = (.*);$", program, re.M))
    blocks = {n: SP.parse_base_polynomial(x, indices) for n, x in setup.items()}
    for table in blocks.values():
        for poly in table.values():
            for mon in poly: poly[mon] = K(poly[mon])
    e, q, ell, ci = rc["e"], rc["q"], row["own_child"]["ell"], indices["c"]
    current = regenerate(blocks, e, q, ci, ell)
    initial_terms = SP.count_terms(current)
    src_audit = json.loads((source/"sparse-ordinary.json").read_text())
    assert len(current) == src_audit["rows"] and initial_terms == src_audit["terms"], "shape must match exact-Q"
    mine = hashlib.sha256(); mine.update(b"index|x_power|y_power|expr\n")
    for k, ((x,y), poly) in enumerate(sorted(current.items()), 1):
        mine.update(f"{k}|{x}|{y}|{text(poly,names)}\n".encode())
    modp_stream_sha = mine.hexdigest()
    print(f"MODP_STREAM_SHA256={modp_stream_sha}", flush=True)
    if args.reduction_control:
        # Byte-exact: reduce the CHARGED exact-Q ordinary stream mod p and compare.
        ref = hashlib.sha256(); ref.update(b"index|x_power|y_power|expr\n")
        t0 = time.monotonic()
        with (source/"sparse-ordinary-run"/"ordinary.tsv").open() as fh:
            assert fh.readline().strip() == "index|x_power|y_power|expr"
            for line in fh:
                idx, xp, yp, expr = line.rstrip("\n").split("|", 3)
                pp = SP.parse_expanded_parameter_polynomial(expr, indices)
                red = {}
                for mon, co in pp.items():
                    v = K(co)
                    if v: red[mon] = v
                ref.update(f"{idx}|{xp}|{yp}|{text(red,names)}\n".encode())
        ok = ref.hexdigest() == modp_stream_sha
        print(f"CONTROL_EXACT_Q_REDUCTION_EQUALS_MODP_REGENERATION={"PASS" if ok else "FAIL"} "
              f"ref_sha={ref.hexdigest()} seconds={time.monotonic()-t0:.1f}", flush=True)
        assert ok
    print("DIRECT_ORIENTATION=PASS", flush=True)
    print(f"DIRECT_J_TERMS={initial_terms}\nORDINARY_GENERATORS={len(current)}\nORDINARY_TERMS={initial_terms}", flush=True)
    images = [{(i,): K(1)} for i in range(len(names))]
    gone = set(); units = []
    audit = (out/"pivot-audit.tsv").open("w", buffering=1)
    xyd = (out/"pivot-coordinates.tsv").open("w", buffering=1)
    audit.write("step|row_slot|variable|unit|row_terms|rhs_terms|rhs_sha256\n")
    xyd.write("step|x_power|y_power|linear_monic_H1|row_vanishes_H2|rhs_v_free_H3\n")
    tb = ti = tr = 0.0; stopped = "COMPLETE"
    while True:
        if time.monotonic() - started > args.deadline_seconds:
            stopped = "DEADLINE"; break
        selected = None
        slots = {xy: k for k, xy in enumerate(sorted(current), 1)}
        for xy, poly in sorted(current.items(), key=lambda it: (len(it[1]), it[0])):
            v = candidate(poly, gone | {ci})
            if v is not None: selected = xy, poly, v; break
        if selected is None: break
        xy, poly, v = selected
        unit = poly[(v,)]
        assert unit and derivative(poly, v) == {(): unit}          # (H1)
        rhs = {mon: -coeff/unit for mon, coeff in poly.items() if mon != (v,)}
        assert not derivative(rhs, v)                               # (H3)
        assert not substitute(poly, v, rhs)                         # (H2)
        gone.add(v); step = len(gone); units.append([names[v], int(unit) % P])
        rtxt = text(rhs, names)
        audit.write(f"{step}|{slots[xy]}|{names[v]}|{int(unit)%P}|{len(poly)}|{len(rhs)}|"
                    f"{hashlib.sha256(rtxt.encode()).hexdigest()}\n")
        xyd.write(f"{step}|{xy[0]}|{xy[1]}|PASS|PASS|PASS\n")
        t = time.monotonic(); blocks = subst_blocks(blocks, v, rhs); tb += time.monotonic()-t
        t = time.monotonic(); images = [substitute(im, v, rhs) for im in images]; ti += time.monotonic()-t
        t = time.monotonic(); current = regenerate(blocks, e, q, ci, ell); tr += time.monotonic()-t
        assert xy not in current, ("chosen pivot did not disappear", step, xy)
        print(f"PIVOT={step} var={names[v]} generators={len(current)} terms={SP.count_terms(current)} "
              f"wall_seconds={time.monotonic()-started:.3f} peak_rss_kib={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss} "
              f"t_blocks={tb:.1f} t_images={ti:.1f} t_regen={tr:.1f}", flush=True)
    audit.close(); xyd.close()
    for im in images: assert all(not gone.intersection(m) for m in im)          # (H4)
    for table in list(blocks.values()) + [current]:
        for poly in table.values(): assert all(not gone.intersection(m) for m in poly)
    assert images[ci] == {(ci,): K(1)}
    for i in set(range(len(names))) - gone: assert images[i] == {(i,): K(1)}
    print("CLOSURE_H4=PASS", flush=True)
    full_terms = SP.count_terms(current)
    c1 = {}
    for xy, poly in current.items():
        value = substitute(poly, ci, {(): K(1)})
        if value: c1[xy] = value
    live = [n for i, n in enumerate(names) if i not in gone]
    with (out/"compressed-c1.ms").open("w", buffering=1<<20) as f:
        f.write(",".join(n for n in live if n != "c") + "\n" + str(P) + "\n")
        f.write(",\n".join(text(p, names) for _, p in sorted(c1.items())) + "\n")
    with (out/"compressed-full.ms").open("w", buffering=1<<20) as f:
        f.write(",".join(live) + "\n" + str(P) + "\n")
        f.write(",\n".join(text(p, names) for _, p in sorted(current.items())) + "\n")
    (out/"live-variables.txt").write_text("\n".join(live) + "\n")
    res = dict(modulus=P, prime=True, stopped=stopped, driver_sha256=sha(__file__),
        modp_stream_sha256=modp_stream_sha, initial_generators=len(current)+0,
        initial_ordinary_terms=initial_terms, pivots=len(gone),
        full_variables=len(names)-len(gone), full_generators=len(current), full_terms=full_terms,
        c1_variables=len(names)-len(gone)-1, c1_generators=len(c1), c1_terms=SP.count_terms(c1),
        pivot_units=units, t_blocks=round(tb,1), t_images=round(ti,1), t_regen=round(tr,1),
        wall_seconds=round(time.monotonic()-started,3),
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    dump(out/"engine.json", res)
    for k in ("pivots","full_variables","full_generators","full_terms","c1_variables","c1_generators","c1_terms"):
        print(f"{k.upper()}={res[k]}", flush=True)
    print(f"COMPRESSION_STATUS={stopped}", flush=True)

if __name__ == "__main__": main()
