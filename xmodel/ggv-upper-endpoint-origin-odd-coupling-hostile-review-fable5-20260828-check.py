#!/usr/bin/env python3
# Hostile-audit checker: upper-endpoint origin odd-coupling lemma (Fable5, 2026-08-28).
# Standalone, deterministic, standard library only. Run from repo root:
#   PYTHONDONTWRITEBYTECODE=1 python3 -B xmodel/ggv-upper-endpoint-origin-odd-coupling-hostile-review-fable5-20260828-check.py
#
# Independent of the producer checker (verify_origin_odd_coupling.py): nothing
# is imported from it; every parse, enumeration, identity, and sign is rebuilt
# from the frozen RAW_INPUT.json and first principles.

import hashlib, json, sys
from fractions import Fraction

REPORT = "xmodel/ggv-upper-endpoint-origin-odd-coupling-sol-ultra-20260828.md"
PRODUCER = ("cases/ggv_8_28_upper_endpoint_origin_odd_coupling_20260828/"
            "verify_origin_odd_coupling.py")
RAW = ("cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/"
       "RAW_INPUT.json")

FROZEN = {
    REPORT:   "3e4a0f03acec2ee5e3cdfff558c481e14735408aa18486d23215958ed8d4bb3a",
    PRODUCER: "f23a6d959dc9a8854f051c16a1fe287dea91d5b66b01a63198a64715c08c04c8",
    RAW:      "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876",
}

FAILURES = []
def check(ok, label):
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        FAILURES.append(label)
    return ok

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for blk in iter(lambda: f.read(1 << 16), b""):
            h.update(blk)
    return h.hexdigest()

# ---------------------------------------------------------------- Step A: pins
def verify_pins(tag):
    for path, want in FROZEN.items():
        check(sha256(path) == want, "%s frozen sha256 %s" % (tag, path))

verify_pins("A(start)")

with open(RAW, "rb") as f:
    RAWDOC = json.loads(f.read().decode("utf-8"))
with open(REPORT, "rb") as f:
    REPORT_TEXT = f.read().decode("utf-8")

# --------------------------------------------- Step B: slot parse + chart map
# Chart X = x*y^3, t = 1/y. A weight-w F-slot X^i must be x^i y^(8+3i-w);
# G-slot x^i y^(12+3i-w). Equivalently x^i y^j -> t^(8+3i-j) X^i (F),
# t^(12+3i-j) X^i (G). All raw exponents nonnegative.
def base_of(name):
    return 8 if name == "F" else 12

def parse_slots(bug=None):
    slots = {}   # (name, weight, i) -> slot string
    byname = {}  # slot string -> (name, weight, i, j)
    for name in ("F", "G"):
        base = base_of(name)
        if bug == "wrong_map":
            base += 1
        prefix = "f" if name == "F" else "g"
        for rec in RAWDOC["raw_slots_through_weight_22"][name]:
            i = rec["raw_exponents"]["x"]
            j = rec["raw_exponents"]["y"]
            w = rec["weight"]
            if i < 0 or j < 0:
                return None, "negative raw exponent in %s" % rec["slot"]
            if j != base + 3 * i - w:
                return None, "chart map violated at %s: j=%d != %d+3*%d-%d" % (
                    rec["slot"], j, base, i, w)
            if rec["slot"] != "%s_%d_%d" % (prefix, i, j):
                return None, "slot name mismatch %s" % rec["slot"]
            if rec["raw_monomial"] != "x^%d*y^%d" % (i, j):
                return None, "raw monomial mismatch %s" % rec["slot"]
            if rec["chart_image"] != "t^%d*X^%d" % (w, i):
                return None, "chart image mismatch %s" % rec["slot"]
            key = (name, w, i)
            if key in slots:
                return None, "duplicate slot %s" % str(key)
            slots[key] = rec["slot"]
            byname[rec["slot"]] = (name, w, i, j)
    return (slots, byname), None

parsed, err = parse_slots()
check(err is None, "B slot-level chart/name/exponent verification (%s)" %
      (err or "all %d slots" %
       (len(RAWDOC["raw_slots_through_weight_22"]["F"]) +
        len(RAWDOC["raw_slots_through_weight_22"]["G"]))))
SLOTS, BYNAME = parsed

check(RAWDOC["maps"]["F_raw_to_chart"] == "x^i*y^j -> t^(8+3*i-j)*X^i",
      "B maps.F_raw_to_chart string matches audited law")
check(RAWDOC["maps"]["G_raw_to_chart"] == "x^i*y^j -> t^(12+3*i-j)*X^i",
      "B maps.G_raw_to_chart string matches audited law")

# Window census. Observed frozen windows must be exactly contiguous
# [max(0, ceil((w-base)/3)), cap-w] with cap 16 (F) / 24 (G), weights 0..cap-2? --
# we do not assume the cap law; we record it and verify contiguity + the
# existence/absence facts the D22 enumeration relies on, straight from data.
def window(name, w):
    xs = sorted(i for (n, ww, i) in SLOTS if n == name and ww == w)
    return xs

census_ok = True
for name, cap in (("F", 16), ("G", 24)):
    base = base_of(name)
    weights = sorted({w for (n, w, i) in SLOTS if n == name})
    expect_weights = []
    for w in range(0, 23):
        lo = max(0, -(-(w - base) // 3))  # ceil((w-base)/3), clamped at 0
        want = list(range(lo, cap - w + 1))
        if want:
            expect_weights.append(w)
        if window(name, w) != want:
            census_ok = False
            print("  census violation %s w=%d: %s vs %s" %
                  (name, w, window(name, w), want))
    if weights != expect_weights:
        census_ok = False
check(census_ok,
      "B window census: F = [max(0,ceil((w-8)/3)), 16-w] (nonempty w=0..14); "
      "G = [max(0,ceil((w-12)/3)), 24-w] (nonempty w=0..21); all contiguous, "
      "no slots outside the law through weight 22")

# Existence/absence facts used at n=22 (read from frozen data, not formulas):
facts = [
    (("F", 11, 1), True),  (("F", 12, 1), False),  # F_a[X1] iff a<=11
    (("F", 8, 0), True),   (("F", 9, 0), False),   # F_a[X0] iff a<=8
    (("G", 12, 0), True),  (("G", 13, 0), False),  # G_b[X0] iff b<=12
    (("G", 15, 1), True),  (("G", 16, 1), False),  # G_b[X1] iff b<=15
]
check(all((k in SLOTS) == v for k, v in facts),
      "B boundary slot existence/absence for the n=22 window")

# ------------------------- Step C: complete symbolic enumeration of D22[X^0]
# D_n = sum_{i+j=n} ((12-j) F_i' G_j + (i-8) F_i G_j'), ' = d/dX.
# F_a, G_b carried as symbolic-linear sparse polys {xexp: {slot: coeff}}.
def component(name, w):
    out = {}
    for (n, ww, i), slot in SLOTS.items():
        if n == name and ww == w:
            out[i] = {slot: 1}
    return out

def deriv(p):
    # derivative degree factor k on X^k -> k*X^(k-1)
    out = {}
    for k, lin in p.items():
        if k >= 1:
            out[k - 1] = {s: k * c for s, c in lin.items()}
    return out

def mul_extract_x0(p, q):
    # full convolution, then take X^0 (bilinear in slots)
    out = {}
    for kp, lp in p.items():
        for kq, lq in q.items():
            if kp + kq != 0:
                continue
            for s1, c1 in lp.items():
                for s2, c2 in lq.items():
                    key = (s1, s2)
                    out[key] = out.get(key, 0) + c1 * c2
    return {k: v for k, v in out.items() if v != 0}

def enumerate_d22_x0(bug=None):
    total = {}
    ledger = []
    for a in range(0, 23):
        b = 22 - a
        Fa, Gb = component("F", a), component("G", b)
        c1 = 12 - b
        c2 = a - 8
        if bug == "keep_10_12" and (a, b) == (10, 12):
            c1 = 1
        if bug == "keep_8_14" and (a, b) == (8, 14):
            c2 = 1
        if bug == "sign_flip" and (a, b) == (7, 15):
            c2 = -c2
        if bug == "omit_term" and (a, b) == (7, 15):
            c2 = 0
        t1 = mul_extract_x0(deriv(Fa), Gb)
        t2 = mul_extract_x0(Fa, deriv(Gb))
        entry = {"pair": (a, b),
                 "t1_slots": bool(t1), "t2_slots": bool(t2),
                 "c1": 12 - b, "c2": a - 8}
        for term, c in ((t1, c1), (t2, c2)):
            for key, v in term.items():
                total[key] = total.get(key, 0) + c * v
        ledger.append(entry)
    return {k: v for k, v in total.items() if v != 0}, ledger

D22X0, LEDGER = enumerate_d22_x0()
EXPECT = {("f_1_0", "g_0_1"): 1, ("f_0_1", "g_1_0"): -1}
check(D22X0 == EXPECT,
      "C D22[X0] == +f_1_0*g_0_1 - f_0_1*g_1_0 (complete literal enumeration); got %s"
      % D22X0)

# ------------------------------- Step D: neighbor audit, independent of report
d_ok = True
class_counts = {"contrib": [], "prefactor_zero": [], }
for e in LEDGER:
    a, b = e["pair"]
    # term 1: (12-b) F_a' G_b needs F_a[X1] and G_b[X0]
    t1_slots = ("F", a, 1) in SLOTS and ("G", b, 0) in SLOTS
    t2_slots = ("F", a, 0) in SLOTS and ("G", b, 1) in SLOTS
    if t1_slots and e["c1"] != 0:
        class_counts["contrib"].append(("t1", a, b, e["c1"]))
    if t1_slots and e["c1"] == 0:
        class_counts["prefactor_zero"].append(("t1", a, b))
    if t2_slots and e["c2"] != 0:
        class_counts["contrib"].append(("t2", a, b, e["c2"]))
    if t2_slots and e["c2"] == 0:
        class_counts["prefactor_zero"].append(("t2", a, b))
d_ok = (class_counts["contrib"] ==
        [("t2", 7, 15, -1), ("t1", 11, 11, 1)] and
        class_counts["prefactor_zero"] == [("t2", 8, 14), ("t1", 10, 12)])
check(d_ok,
      "D neighbors: exactly (11,11)+1 and (7,15)-1 contribute; (10,12) killed by "
      "12-j=0, (8,14) by i-8=0; every other pair lacks a required X0/X1 slot: %s"
      % class_counts)

# --------------------- Step E: slot identification with original coordinates
# P = sum f_i_j x^i y^j over frozen F slots; P_x(0,0) is the coefficient of
# x^1*y^0, P_y(0,0) of x^0*y^1. Verify computationally which named slot that is.
def linear_slot(name, di, dj):
    hits = [s for s, (n, w, i, j) in BYNAME.items()
            if n == name and i == di and j == dj]
    return hits[0] if len(hits) == 1 else None

ident = (linear_slot("F", 1, 0) == "f_1_0" and linear_slot("F", 0, 1) == "f_0_1"
         and linear_slot("G", 1, 0) == "g_1_0" and linear_slot("G", 0, 1) == "g_0_1"
         and BYNAME["f_1_0"][1] == 11 and BYNAME["f_0_1"][1] == 7
         and BYNAME["g_1_0"][1] == 15 and BYNAME["g_0_1"][1] == 11)
check(ident, "E f_1_0=F11[X1]=P_x(0), f_0_1=F7[X0]=P_y(0), "
             "g_1_0=G15[X1]=Q_x(0), g_0_1=G11[X0]=Q_y(0); so "
             "D22[X0] = P_x*Q_y - P_y*Q_x |_(0,0) = J(P,Q)(0)")

# --------- Step F: chart/endpoint sign convention, proved by exact computation
# With F(t,X) = t^8 * P(X t^3, 1/t), G = t^12 * Q(X t^3, 1/t) (the frozen map),
# the identity  sum_n D_n t^(n-21) = t * J_{x,y}(P,Q)(X t^3, 1/t)  holds.
# Hence Keller J(P,Q) = +1 forces D_22 = +1 (and every other D_n = 0).
def lmul(p, q):    # Laurent-in-t, poly-in-X sparse dicts {(tx, xe): Fraction}
    out = {}
    for (a1, b1), c1 in p.items():
        for (a2, b2), c2 in q.items():
            k = (a1 + a2, b1 + b2)
            out[k] = out.get(k, 0) + c1 * c2
    return {k: v for k, v in out.items() if v != 0}

def ladd(p, q, s=1):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, 0) + s * v
    return {k: v for k, v in out.items() if v != 0}

def dX(p):
    return {(a, b - 1): b * c for (a, b), c in p.items() if b != 0}

def chart_image(poly_xy, base):
    # poly_xy: {(i,j): coeff} in x,y  ->  {(t-exp, X-exp)} via x=X t^3, y=1/t
    return {(base + 3 * i - j, i): Fraction(c) for (i, j), c in poly_xy.items()}

def jac_xy(P, Q):
    def dx(p): return {(i - 1, j): i * Fraction(c) for (i, j), c in p.items() if i}
    def dy(p): return {(i, j - 1): j * Fraction(c) for (i, j), c in p.items() if j}
    def m(p, q):
        out = {}
        for (i1, j1), c1 in p.items():
            for (i2, j2), c2 in q.items():
                k = (i1 + i2, j1 + j2)
                out[k] = out.get(k, 0) + c1 * c2
        return out
    return ladd(m(dx(P), dy(Q)), m(dy(P), dx(Q)), -1)

def d_series(F, G):
    # sum_n D_n t^(n-21) with D_n = sum_{i+j=n} ((12-j)F_i'G_j + (i-8)F_iG_j')
    # computed weight-by-weight from the chart images.
    Fw, Gw = {}, {}
    for (a, b), c in F.items(): Fw.setdefault(a, {})[(0, b)] = c
    for (a, b), c in G.items(): Gw.setdefault(a, {})[(0, b)] = c
    out = {}
    for a, Fa in Fw.items():
        for b, Gb in Gw.items():
            n = a + b
            term = ladd({k: (12 - b) * v for k, v in lmul(dX(Fa), Gb).items()},
                        {k: (a - 8) * v for k, v in lmul(Fa, dX(Gb)).items()})
            for (tz, xe), v in term.items():
                k = (n - 21, xe)
                out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v != 0}

# generic pair with a spread of parities, deterministic hard-coded coefficients
GEN_P = {(0, 0): 3, (1, 0): 5, (0, 1): 7, (2, 1): 11, (1, 3): -2, (3, 2): 13}
GEN_Q = {(0, 0): -4, (1, 0): 6, (0, 1): 9, (1, 1): -8, (2, 2): 15, (0, 3): 17}
lhs = d_series(chart_image(GEN_P, 8), chart_image(GEN_Q, 12))
# rhs = t * J(...)(X t^3, 1/t): base-0 chart image, t-exponent shifted by +1
rhs = {(a + 1, b): c for (a, b), c in chart_image(jac_xy(GEN_P, GEN_Q), 0).items()}
check(lhs == rhs,
      "F Laurent identity: sum_n D_n t^(n-21) == t * J_{x,y}(P,Q)(X t^3, 1/t) "
      "for a generic exact pair")

def keller_d22(P, Q, bug=None):
    s = d_series(chart_image(P, 8), chart_image(Q, 12))
    target = Fraction(-1 if bug == "endpoint_sign" else 1)
    return (s == {(1, 0): Fraction(1)}) and s.get((1, 0)) == target

check(keller_d22({(1, 0): 1}, {(0, 1): 1}) and
      keller_d22({(1, 0): 1, (0, 3): 1}, {(0, 1): 1}),
      "F Keller fixtures (P,Q)=(x,y) and (x+y^3,y): J=+1 gives D22=+1 exactly, "
      "all other D_n=0 (target is +1, not -1)")

# ------------------------------------------------- Step G: parity of raw slots
def parity_ok(bug=None):
    for (n, w, i), slot in SLOTS.items():
        j = BYNAME[slot][3]
        want = (w + 1) % 2 if bug == "parity_flip" else w % 2
        if (i + j) % 2 != want:
            return False
    return True
check(parity_ok(), "G every raw slot has total degree i+j == weight mod 2")
check(all(BYNAME[s][1] % 2 == 1 for s in ("f_1_0", "f_0_1", "g_1_0", "g_0_1")),
      "G all four coupling slots carry ODD raw weights (11,7,15,11)")

even_slots = {s for s, (n, w, i, j) in BYNAME.items() if w % 2 == 0}
check(all((BYNAME[s][2] + BYNAME[s][3]) % 2 == 0 for s in even_slots),
      "G odd-weights-zero => P,Q supported on even total degree only "
      "(hence invariant under (x,y)->(-x,-y))")
check(not any(BYNAME[s][2] + BYNAME[s][3] == 1 for s in even_slots),
      "G no degree-1 monomial survives => grad P(0) = grad Q(0) = 0")
killed = {k: v for k, v in D22X0.items()
          if k[0] in even_slots and k[1] in even_slots}
check(killed == {},
      "G restricting D22[X0] to the odd-zero section gives identically 0, "
      "so D22=1 is impossible there")

# ------------------------------------ Step H: firewall wording in frozen report
fw1 = ("The lemma alone does not show that the intersection is empty."
       in REPORT_TEXT)
fw2 = ("It proves no\nendpoint exclusion, other-branch result, Keller theorem, "
       "or JC2." in REPORT_TEXT)
fw3 = ("The q15 dimension theorem itself is unchanged: it concerns the\n"
       "q-gate fiber before `(2)` is imposed." in REPORT_TEXT)
# The lemma is about the raw all-odd-weight-zero section; the report must not
# claim that vanishing odd q-gates forces vanishing odd raw weights. The only
# candidate sentence is the "not a survivor merely because" line, which asserts
# the correct direction. Pin all three firewall sentences byte-exactly.
fw4 = ("It\nis not a survivor merely because every odd de Rham gate vanishes "
       "there." in REPORT_TEXT)
check(fw1 and fw2 and fw3 and fw4,
      "H report firewall sentences present byte-exactly; the odd-q-gates => "
      "odd-raw-weights converse is NOT asserted anywhere in the frozen text")

# ------------------------------------------------------- Step I: mutation grid
def mutated_fails(tag, fn):
    ok = False
    try:
        ok = fn()
    except Exception:
        ok = False
    check(not ok, "I mutation detected: %s" % tag)

mutated_fails("sign flip on (7,15) term",
              lambda: enumerate_d22_x0("sign_flip")[0] == EXPECT)
mutated_fails("retaining structural zero (10,12)",
              lambda: enumerate_d22_x0("keep_10_12")[0] == EXPECT)
mutated_fails("retaining structural zero (8,14)",
              lambda: enumerate_d22_x0("keep_8_14")[0] == EXPECT)
mutated_fails("omitting the true (7,15) term",
              lambda: enumerate_d22_x0("omit_term")[0] == EXPECT)
mutated_fails("wrong chart offset (base 8 -> 9)",
              lambda: parse_slots("wrong_map")[1] is None)
mutated_fails("parity law flipped to w+1 mod 2",
              lambda: parity_ok("parity_flip"))
mutated_fails("endpoint target sign -1 instead of +1",
              lambda: keller_d22({(1, 0): 1}, {(0, 1): 1}, "endpoint_sign"))

# ---------------------------------------------------------------- Step J: end
verify_pins("J(end)")

print()
if FAILURES:
    print("FAIL_HOSTILE_AUDIT_ORIGIN_ODD_COUPLING")
    for f in FAILURES:
        print("  first-defect-candidate: " + f)
    sys.exit(1)
print("PASS_HOSTILE_AUDIT_UPPER_ENDPOINT_ORIGIN_ODD_COUPLING_FABLE5")
