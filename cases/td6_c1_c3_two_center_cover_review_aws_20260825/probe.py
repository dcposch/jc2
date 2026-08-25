#!/usr/bin/env python3
"""Independent probe for the TD6 (C,1,U) two-center cover review (claude, 2026-08-25).

Run from the jc2 repository root:  python3 /tmp/td6_two_center_cover_probe_claude.py

Stdlib only.  Recomputes every byte hash the no-shell review could only read,
extracts the four charged archives, pins the archived producers against the
recorded hashes, byte-compares archived parent modules against the repo
copies, and re-derives every printed algebraic identity with an independent
polynomial engine (no python-flint).  Prints PASS/FAIL per check and exits
nonzero on any FAIL.
"""

import hashlib
import itertools
import sys
import tarfile
import tempfile
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(".").resolve()
CASE = ROOT / "cases/td6_c1_c3_two_center_cover_20260824"
FAILURES = []


def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" [{detail}]" if detail else ""))
    if not ok:
        FAILURES.append(name)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


# ---------------------------------------------------------------- 1. hashes
CHARGED = {
    "xmodel/td6-c1-c3-two-center-cover-gate-20260824.md":
        "2ada2d70fbdb9db2cf6d93c3b8d3ba0b1f19be1dd5530365a0b3b235e230fbd6",
    "cases/td6_c1_c3_two_center_cover_20260824/MANIFEST.sha256":
        "e3af7ba9859ddb17516c6950efc062e525330317f5eb7d48495f9ae55a360440",
}
for rel, expect in CHARGED.items():
    check(f"charged {rel}", sha(ROOT / rel) == expect)

manifest_entries = []
for line in (CASE / "MANIFEST.sha256").read_text().splitlines():
    digest, rel = line.split(None, 1)
    manifest_entries.append((digest, rel.strip()))
    check(f"manifest {rel.strip()}", sha(CASE / rel.strip()) == digest)
check("manifest covers 32 files", len(manifest_entries) == 32)

listed = {rel for _, rel in manifest_entries} | {"MANIFEST.sha256", "FREEZE.sha256"}
actual = {str(p.relative_to(CASE)) for p in CASE.rglob("*") if p.is_file()}
check("manifest coverage exhaustive", actual == listed,
      f"unlisted={sorted(actual - listed)} missing={sorted(listed - actual)}")

EMPTY = hashlib.sha256(b"").hexdigest()
check("empty-string sha constant",
      EMPTY == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")

for meta_rel in ["evidence/v4/generic.meta", "evidence/v4/b_local.meta",
                 "evidence/v4/h_zero.meta", "evidence/v5/u_zero_v5.meta",
                 "evidence/v5/intersection_v5.meta", "evidence/v6/launch.meta",
                 "evidence/v7/launch.meta"]:
    fields = dict(line.split("=", 1) for line in
                  (CASE / meta_rel).read_text().splitlines() if "=" in line)
    stem = meta_rel.rsplit(".", 1)[0]
    if "launch" in meta_rel:
        stem = {"evidence/v6/launch": "evidence/v6/h-b-quotient",
                "evidence/v7/launch": "evidence/v7/h-b-raw-quotient"}[stem]
    check(f"{meta_rel} stdout pin",
          sha(CASE / (stem + ".stdout")) == fields["stdout_sha256"])
    check(f"{meta_rel} stderr pin",
          sha(CASE / (stem + ".stderr")) == fields["stderr_sha256"])

# ------------------------------------------------- 2. archives and producers
PINNED_PRODUCERS = {
    "v5": ("jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py",
           "8b4d6a360b3134fc40aab652ae03f523520b35b4e73a5c41dc646715042f9571"),
    "v6": ("jc2/cases/td6_c1_c3_two_center_cover_20260824/replay.py",
           "56df638aaa3ae02cf437a32258a920a8a66afb2781c089e30b1774a5b38e65db"),
    "v7": ("jc2/cases/td6_c1_c3_two_center_cover_20260824/h_b_raw_quotient.py",
           "9b3de6b502292ba29c8e1b14524792c323dcdecc056cc64feccb0fa36251969f"),
}
PARENT_PINS = {  # asserted at import time by the read parents
    "cases/td6_jet_orbit_adjoint_20260824/replay.py":
        "fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198",
    "cases/td6_boundary_q2_deformation_20260824/replay.py":
        "0ba184470dc051fad50640647c4b78ea869b8a4153219026b23abdcf0652d357",
    "cases/td6_moduli_uniform_third_band_20260824/replay.py":
        "7a21f9495d1e8784a9b253253430846ce882e2ce26f91815b31b6e061022cba8",
    "cases/td6_two_chart_next_row_20260824/replay.py":
        "0fc299a18a7ace6e5f64f98f38a71775331f226baac2e8ad258dd40e744fa5b8",
}
for rel, expect in PARENT_PINS.items():
    check(f"repo parent hash {rel}", sha(ROOT / rel) == expect)

for tag in ["v4", "v5", "v6", "v7"]:
    arc = CASE / f"archives/td6-aws-handoff-20260824-{tag}.tar.gz"
    with tempfile.TemporaryDirectory() as tmp, tarfile.open(arc) as tf:
        tf.extractall(tmp, filter="data")
        # macOS may add top-level AppleDouble ``._*`` resource-fork files to
        # an archive.  Select the extracted payload directory explicitly.
        base = next(p for p in Path(tmp).iterdir() if p.is_dir())
        src = base / "SOURCE.sha256"
        ok = True
        for line in src.read_text().splitlines():
            digest, rel = line.split(None, 1)
            member = base / rel.strip()
            if not member.exists() or sha(member) != digest:
                ok = False
        check(f"{tag} archive SOURCE.sha256 self-consistent", ok)
        if tag in PINNED_PRODUCERS:
            rel, expect = PINNED_PRODUCERS[tag]
            check(f"{tag} pinned producer {rel.rsplit('/', 1)[-1]}",
                  sha(base / rel) == expect)
        for rel in PARENT_PINS:
            member = base / "jc2" / rel
            if member.exists():
                check(f"{tag} archived parent == repo: {rel}",
                      member.read_bytes() == (ROOT / rel).read_bytes())
        two = base / "jc2/cases/td6_c1_c3_two_center_cover_20260824"
        print(f"INFO {tag} producer replay.py sha =",
              sha(two / "replay.py") if (two / "replay.py").exists() else "absent")

# ------------------------------------------- 3. bivariate polynomial algebra
def padd(a, b, s=Q(1)):
    out = dict(a)
    for m, c in b.items():
        v = out.get(m, Q(0)) + s * c
        if v:
            out[m] = v
        else:
            out.pop(m, None)
    return out


def pmul(a, b):
    out = {}
    for (i, j), c in a.items():
        for (k, l), d in b.items():
            m = (i + k, j + l)
            v = out.get(m, Q(0)) + c * d
            if v:
                out[m] = v
            else:
                out.pop(m, None)
    return out


def pscale(a, s):
    return {m: s * c for m, c in a.items() if s * c}


def mono(i, j, c=1):
    return {(i, j): Q(c)}


B = padd(padd(padd(padd(padd(mono(2, 2, 4), mono(1, 4, 24)), mono(1, 1, -4)),
          mono(0, 6, 20)), mono(0, 3, -20)), mono(0, 0, 1))
T = padd(padd(padd(padd(padd(mono(2, 2, 4), mono(1, 4, 28)), mono(1, 1, -4)),
          mono(0, 6, 24)), mono(0, 3, -24)), mono(0, 0, 1))
H = padd(mono(1, 0), mono(0, 2, -3))
U1 = mono(0, 1)
P = padd(padd(mono(0, 6, 128), mono(0, 3, -32)), mono(0, 0, 1))

check("T - B == 4U^3(CU+U^3-1)",
      padd(T, B, Q(-1)) == pmul(mono(0, 3, 4), padd(padd(mono(1, 1), mono(0, 3)),
                                                    mono(0, 0, -1))))
check("B(C,0) == 1", {m: c for m, c in B.items() if m[1] == 0} == mono(0, 0, 1))
check("P == B(3U^2, U)",
      P == padd(padd(padd(padd(padd(mono(0, 6, 36), mono(0, 6, 72)),
           mono(0, 3, -12)), mono(0, 6, 20)), mono(0, 3, -20)), mono(0, 0, 1)))

# printed denominators (expanded forms from the frozen stdouts)
GEN_REL = {(4, 4): Q(1), (3, 3): Q(-1), (2, 8): Q(-22), (2, 5): Q(1),
           (2, 2): Q(1, 4), (1, 10): Q(24), (1, 7): Q(21), (1, 4): Q(-3, 2),
           (0, 12): Q(45), (0, 9): Q(-45), (0, 6): Q(9, 4)}
GEN_TERM = {(5, 5): Q(1), (4, 7): Q(-3), (4, 4): Q(-1), (3, 9): Q(-22),
            (3, 6): Q(4), (3, 3): Q(1, 4), (2, 11): Q(90), (2, 8): Q(18),
            (2, 5): Q(-9, 4), (1, 13): Q(-27), (1, 10): Q(-108),
            (1, 7): Q(27, 4), (0, 15): Q(-135), (0, 12): Q(135),
            (0, 9): Q(-27, 4)}
BL_REL = {(2, 4): Q(1), (1, 6): Q(7), (1, 3): Q(-1), (0, 8): Q(6),
          (0, 5): Q(-6), (0, 2): Q(1, 4)}
BL_TERM = {(3, 5): Q(1), (2, 7): Q(4), (2, 4): Q(-1), (1, 9): Q(-15),
           (1, 6): Q(-3), (1, 3): Q(1, 4), (0, 11): Q(-18), (0, 8): Q(18),
           (0, 5): Q(-3, 4)}
HZ_REL = {(0, 8): Q(1), (0, 5): Q(-1, 4), (0, 2): Q(1, 128)}
HZ_TERM = {(0, 9): Q(1), (0, 6): Q(-1, 4), (0, 3): Q(1, 128)}
V6_REL = {(0, 9): Q(1), (0, 6): Q(-1, 4), (0, 3): Q(1, 128)}
V6_TERM = {(0, 10): Q(1), (0, 7): Q(-1, 4), (0, 4): Q(1, 128)}

U2, U3, U4 = mono(0, 2), mono(0, 3), mono(0, 4)
check("generic relation den == (1/4)B U^2 H^2",
      GEN_REL == pscale(pmul(pmul(B, U2), pmul(H, H)), Q(1, 4)))
check("generic termwise den == (1/4)B U^3 H^3",
      GEN_TERM == pscale(pmul(pmul(B, U3), pmul(pmul(H, H), H)), Q(1, 4)))
check("B-local relation den == (1/4)U^2 T",
      BL_REL == pscale(pmul(U2, T), Q(1, 4)))
check("B-local termwise den == (1/4)U^3 H T",
      BL_TERM == pscale(pmul(pmul(U3, H), T), Q(1, 4)))
check("H-zero relation den == (1/128)U^2 P",
      HZ_REL == pscale(pmul(U2, P), Q(1, 128)))
check("H-zero termwise den == (1/128)U^3 P",
      HZ_TERM == pscale(pmul(U3, P), Q(1, 128)))
check("V6 relation den == (1/128)U^3 P (contains P)",
      V6_REL == pscale(pmul(U3, P), Q(1, 128)))
check("V6 termwise den == (1/128)U^4 P (contains P)",
      V6_TERM == pscale(pmul(U4, P), Q(1, 128)))

# resultants in C (coefficients are univariate polys in U, as dicts j->Q)
def ucoeffs(p, degc):
    out = [{} for _ in range(degc + 1)]
    for (i, j), c in p.items():
        out[i][j] = c
    return out[::-1]  # leading first


def umul(a, b):
    out = {}
    for i, c in a.items():
        for j, d in b.items():
            out[i + j] = out.get(i + j, Q(0)) + c * d
    return {k: v for k, v in out.items() if v}


def sylvester(f, g, m, n):
    """Res_C of f (deg m) and g (deg n); entries univariate in U."""
    fc, gc = ucoeffs(f, m), ucoeffs(g, n)
    size = m + n
    rows = []
    for s in range(n):
        rows.append([{}] * s + fc + [{}] * (n - 1 - s))
    for s in range(m):
        rows.append([{}] * s + gc + [{}] * (m - 1 - s))
    total = {}
    for perm in itertools.permutations(range(size)):
        sign = 1
        seen = list(perm)
        for a in range(size):
            for b in range(a + 1, size):
                if seen[a] > seen[b]:
                    sign = -sign
        term = {0: Q(sign)}
        dead = False
        for r in range(size):
            e = rows[r][perm[r]]
            if not e:
                dead = True
                break
            term = umul(term, e)
        if not dead:
            for k, v in term.items():
                total[k] = total.get(k, Q(0)) + v
    return {k: v for k, v in total.items() if v}


check("Res_C(B,T) == 64 U^10", sylvester(B, T, 2, 2) == {10: Q(64)})
check("Res_C(B,(1/4)U^2T) == 4 U^14",
      sylvester(B, pscale(pmul(U2, T), Q(1, 4)), 2, 2) == {14: Q(4)})
r5 = sylvester(B, pscale(pmul(pmul(U3, H), T), Q(1, 4)), 2, 3)
check("Res_C(B,(1/4)U^3HT) == +-(512U^22-128U^19+4U^16)",
      r5 in ({22: Q(512), 19: Q(-128), 16: Q(4)},
             {22: Q(-512), 19: Q(128), 16: Q(-4)}), str(sorted(r5.items())))

# U inverse mod P, squarefreeness, irreducibility of P (encodes the hand proof)
def u_divmod(a, b):
    a = dict(a)
    q = {}
    db = max(b)
    lb = b[db]
    while a and max(a) >= db:
        da = max(a)
        c = a[da] / lb
        q[da - db] = c
        for j, v in b.items():
            a[da - db + j] = a.get(da - db + j, Q(0)) - c * v
        a = {k: v for k, v in a.items() if v}
    return q, a


Puni = {6: Q(128), 3: Q(-32), 0: Q(1)}
prod = umul({5: Q(-128), 2: Q(32)}, {1: Q(1)})
check("x * (-128x^5+32x^2) mod P == 1", u_divmod(prod, Puni)[1] == {0: Q(1)})
Pprime = {5: Q(768), 2: Q(-96)}


def ugcd(a, b):
    while b:
        a, b = b, u_divmod(a, b)[1]
    lead = a[max(a)]
    return {k: v / lead for k, v in a.items()}


check("gcd(P,P') == 1 (squarefree)", ugcd(Puni, Pprime) == {0: Q(1)})
# hand-proof arithmetic: y^2 substitution disc nonsquare; norm not a cube
disc = 32 * 32 - 4 * 128
isq = int(disc ** 0.5)
check("disc(128y^2-32y+1)=512 nonsquare",
      disc == 512 and isq * isq != disc and (isq + 1) ** 2 != disc)
norm_a = Q(2 + 0, 16) * Q(2, 16) - Q(2, 16 * 16)  # ((2)^2 - 2)/256 = 2/256
check("N((2+sqrt2)/16) == 1/128, v2=-7 not divisible by 3",
      norm_a == Q(1, 128) and (-7) % 3 != 0)

# ------------------------------------------------------- 4. the field tower
F_INT = (1411, -4032, 4680, -3045, 1170, -252, 24)
F_MONIC = [Q(v, 24) for v in F_INT]


def kred(cs):
    cs = [Q(c) for c in cs]
    for d in range(len(cs) - 1, 5, -1):
        c = cs[d]
        if c:
            for i in range(6):
                cs[d - 6 + i] -= c * F_MONIC[i]
        cs[d] = Q(0)
    cs = cs[:6] + [Q(0)] * (6 - len(cs[:6]))
    return tuple(cs[:6])


def kmul(a, b):
    out = [Q(0)] * 11
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return kred(out)


def kinv(a):
    # extended gcd over Q[S] against F_MONIC
    r0, r1 = list(F_MONIC), [Q(x) for x in a]
    s0, s1 = [Q(0)], [Q(1)]
    t0, t1 = [Q(1)], [Q(0)]

    def trim(p):
        while p and not p[-1]:
            p.pop()
        return p

    r0, r1 = trim(r0), trim(r1)
    while r1:
        q, r = [], list(r0)
        while r and len(r) >= len(r1):
            d = len(r) - len(r1)
            c = r[-1] / r1[-1]
            q = q + [Q(0)] * max(0, d + 1 - len(q))
            q[d] += c
            for i, v in enumerate(r1):
                r[d + i] -= c * v
            r = trim(r)
        news = trim([ (s0[i] if i < len(s0) else Q(0))
                     - sum(q[j] * (s1[i - j] if 0 <= i - j < len(s1) else Q(0))
                           for j in range(len(q)))
                     for i in range(max(len(s0), len(q) + len(s1)))])
        r0, r1, s0, s1 = r1, r, s1, news
    lead = r0[-1]
    check("k gcd with F is a unit", len(r0) == 1 and bool(lead))
    inv = [c / lead for c in s0]
    return kred(inv + [Q(0)] * (6 - len(inv)))


K1 = kred([1])
k_el = kred([252, -342, 144, -36])
check("k = 252-342S+144S^2-36S^3 nonzero", any(k_el))
check("k * k^-1 == 1 in K", kmul(k_el, kinv(k_el)) == K1)
Hf = kred([Q(8, 5), Q(-7, 5), Q(2, 5)])
check("3H^3 == 1", kmul(kmul(Hf, Hf), kmul(Hf, kred([3]))) == K1)
Lf = kmul(Hf, kred([25]))
L8 = K1
for _ in range(8):
    L8 = kmul(L8, Lf)
ALPHA = kmul(kred([9]), kinv(L8))

cols = []
p = ALPHA
for d in range(6):
    cols.append(p)
    p = kmul(p, kred([0, 1]))
mat = [[cols[c][r] for c in range(6)] for r in range(6)]


def det6(m):
    m = [row[:] for row in m]
    det = Q(1)
    for c in range(6):
        piv = next(r for r in range(c, 6) if m[r][c])
        if piv != c:
            m[c], m[piv] = m[piv], m[c]
            det = -det
        det *= m[c][c]
        inv = 1 / m[c][c]
        m[c] = [v * inv for v in m[c]]
        for r in range(c + 1, 6):
            f = m[r][c]
            if f:
                m[r] = [a - f * b for a, b in zip(m[r], m[c])]
    return det


check("Norm(ALPHA) == 3^28/5^96 (v3=28, not a cube)",
      det6(mat) == Q(3 ** 28, 5 ** 96) and 28 % 3 != 0)

# F irreducible mod 31 (independent Rabin)
PR = 31
F31 = [v % PR for v in F_INT]


def fp_dm(a, b):
    a = a[:]
    binv = pow(b[-1], -1, PR)
    while len(a) >= len(b) and any(a):
        d = len(a) - len(b)
        c = (a[-1] * binv) % PR
        for i, v in enumerate(b):
            a[d + i] = (a[d + i] - c * v) % PR
        while a and a[-1] == 0:
            a.pop()
    return a


def fp_mulmod(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % PR
    return fp_dm(out, F31)


def fp_powx(e):
    r, b = [1], [0, 1]
    while e:
        if e & 1:
            r = fp_mulmod(r, b)
        b = fp_mulmod(b, b)
        e >>= 1
    return r


def fp_gcd(a, b):
    while any(b):
        a, b = b, fp_dm(a, b)
        while b and b[-1] == 0:
            b.pop()
    return a


def frob_minus_x(it):
    v = fp_powx(PR ** it)[:]
    v += [0] * max(0, 2 - len(v))
    v[1] = (v[1] - 1) % PR
    while v and v[-1] == 0:
        v.pop()
    return v


g2 = fp_gcd(F31[:], frob_minus_x(2))
g3 = fp_gcd(F31[:], frob_minus_x(3))
check("F irreducible mod 31 (Rabin)",
      len(g2) == 1 and len(g3) == 1 and not frob_minus_x(6))
check("F(0) != 0 (S invertible)", F_INT[0] != 0)

# --------------------------------------- 5. exceptional-stratum stdout facts
uz = (CASE / "evidence/v5/u_zero_v5.stdout").read_text().splitlines()
ix = (CASE / "evidence/v5/intersection_v5.stdout").read_text().splitlines()


def field(lines, key):
    return next(l.split("=", 1)[1] for l in lines if l.startswith(key + "="))


check("U=0 and origin residuals identical",
      field(uz, "first_incompatibility[0]_residual_coordinates")
      == field(ix, "first_incompatibility[0]_residual_coordinates"))
check("residual nonzero (unit of the field E)",
      "'-9'" in field(uz, "first_incompatibility[0]_residual_coordinates"))
check("origin chart is 1 (raw, no inversion)",
      field(ix, "first_incompatibility[0]_certificate_chart_denominator") == "(1)")
check("U=0 conservative chart C^3",
      field(uz, "first_incompatibility[0]_certificate_chart_denominator") == "(C^3)")

print()
if FAILURES:
    print(f"PROBE FAILED: {len(FAILURES)} failing checks: {FAILURES}")
    sys.exit(1)
print("PROBE PASSED: all checks succeeded")
