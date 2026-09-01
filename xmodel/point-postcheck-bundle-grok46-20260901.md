# POINT-POSTCHECK — extraction + repaired postcheck bundle

Status: READY-TO-EXTRACT
Lane: systems/preparation
Date: 2026-09-01
Agent: grok-4.6
No CAS execution on this machine.

## Contents

0. Hash verification and prompt-digest note
1. Dialect lessons (suite-derived) and code-check table
2. Fetched msolve solve-mode and `-P` conventions
3. Scope, rings, validated generators, and extraction strategy
4. Exact verdict rules (point and type)
5. `interpret_msolve.py`
6. Characteristic inputs `type86_A.ms`, `type86_B.ms`
7. `rur_to_points.sage`
8. Rational-slice scripts (`slice_rational.m2`, `slice_rational.sage`)
9. Rewritten `idp_postcheck.m2` and `idp_apply_point.m2`
10. Driver `run_point_postcheck.sh`
11. SHA-256 manifest
12. OPEN items, FALLACY-v2, and non-claims

## 0. Hash verification and prompt-digest note

Frozen copies hashed with `shasum -a 256` before they were read:

```text
3985fbedea72315c0ff3ffd4185de465ba16922bca872623fe2f02fe34cffc08  .../nodal-realization-86-96-grok46-20260831.md
c54d53f0a55586eb0fdd84d3aa311c6d64125a2cded8bec77aad1c3a8f40ec7f  .../msolve-prep-realization-grok46-20260831.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  .../block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

Items 1 and 3 match the prompt. Item 2 does **not** match the boxed digest `64e451b44a421ca8efbd9d5fd553fd43cc2fb7afe6415ab760aab9ac47c27ef4`. That digest is the body hash of `xmodel/braid-prep-row64-grok46-20260831.md` (DIVERT log), a different file. The bytes at the charged *path* hash to `c54d53f0…`, matching both the workspace copy and `run.v2` `charged_input_2_sha256`. Path identity plus the launcher digest identify the named msolve-prep report; the boxed digest is a prompt transcription error. This lane proceeds on those frozen bytes. Canonical ledgers and `jc2-lean` were not inspected. No CAS was run here.

Campaign facts consumed (coordinator LIVE STATE 2026-09-01T14:28Z, not re-computed): `(8,6,11)` and `(8,6,9)` are NONEMPTY at the characteristic-ideal level (msolve GROEBNER proper bases of 138 and 345 elements; `.ms`/`.m2` generators 6/6 and 7/7 sympy-matched). Colon/cover on the M2 mirrors timed out; that residual belongs to this postcheck. `(9,6,4)` and `(9,6,2)` are already KILLED (both engines, unit ideal) and are not jobs here.

## 1. Dialect lessons (suite-derived) and code-check table

Every script below was written against these seven lessons from the realization-suite runs (notes 06:23Z tower/diff repair; 10:10Z GROEBNER/SOLVE mix-up; braid-prep reserved names).

| # | Lesson | What broke | Repair in this bundle |
|---|---|---|---|
| 1 | No M2 reserved locals `pi`, `gamma`, `I`, `O` | `pi` is a constant; `I` is overloaded | `sumvar`/`prodvar` never used as names; ideals are `idpIdeal`, `tanIdeal`; `gam` stays the chart coefficient |
| 2 | No tower-ring `numgens` | `R0[u]` has `numgens 1`, not 12 | Flattened `QQ[B,…,u]` built once; `K[paramt]` has `numgens 1` by construction; never `R0[u]` |
| 3 | Coefficients from the SOURCE ring variable | Ring creation rebinds globals | `srcVar f := (ring f)_0`; `coefficient(src^n, f)` |
| 4 | `diff(var, poly)` | `diff(p,t)` differentiates `t` by `p` | `diff(srcT, p)` everywhere; M2 doc: first argument is the variable |
| 5 | `first degree` for ring elements | `degree f` is a list | `intDeg`: 0-polynomial → `-1`, else `first degree` |
| 6 | No underscore-subscript identifiers | `p_s` parses as subscript | `pS`, `tvarST`, `sumLoc`, `paramt` |
| 7 | GROEBNER vs SOLVE | Driver treated `-g 2` `[1]` as 0-dim nonempty | GROEBNER: `#length of basis` + unit-ideal test. SOLVE (`-P 2`): `[-1]` / `[1,nvars,-1,[]]` / `[0,RUR]`. Interpreter reads basis data, not solver slogans |

Old `idp_postcheck.m2` violated (1)(3)(4)(6) and used `degree(s,Wred)` with the wrong argument. It is replaced, not patched.

## 2. Fetched msolve solve-mode and `-P` conventions

Fetched this lane (not executed):

- msolve 0.10.1 man page, https://www.mankier.com/1/msolve
- Tutorial PDF https://msolve.lip6.fr/downloads/msolve-tutorial.pdf (476161 bytes, SHA-256 `de8ae1ad54e228b18af9c9123730077e1696638c3f52d677480ad7a258edb1cd`), §6.

**GROEBNER (`-g 2`).** Comment block with `length of basis: N`. Unit ideal = EMPTY variety = basis `{1}`. Proper basis = NONEMPTY (Nullstellensatz). This mode does **not** emit points.

**SOLVE (default, `-P 2`).** Top-level list:

- `[-1]` — no point in an algebraic closure (EMPTY).
- `[1, nvars, -1, []]` — infinitely many points (POSDIM).
- `[0, [0, nvars, deg, vars, form, [1, [lw, lwp, param]]]]` — 0-dim RUR. `lw` encodes \(w\); `lwp` the denominator; `param` is \(nvars-1\) pairs `[[deg,L], c]`. Coordinates \(x_i = -v_i(\theta)/w'(\theta)\) at roots of \(w\); the last variable is the parameter. `-P 1` appends real isolating boxes after the RUR; `-P 0` (default) is real boxes only and is **not** an algebraic point list.

Extraction here always calls `msolve -P 2` with **no** `-g`.

## 3. Scope, rings, validated generators, and extraction strategy

Chart (charged NODAL-REALIZATION §2, msolve-prep §2.1):

```text
p = t^8 + B t^5 + C t^4 + D t^3 + E t^2 + F t + G
q = t^6 + b t^4 + gam t^3 + d t^2 + e t + f
```

Flattened ring `QQ[B,C,D,E,F,G,b,gam,d,e,f,u]` (Rabinowitsch `u`). Jobs:

| job | `Δ` | open | `δ_aff` | `.ms` (reused, hash-locked) |
|---|---|---|---:|---|
| `type86_A` | `(8,6,11)` | `h_11≠0` | 11 | `1b3e8ffa…` (462 bytes) |
| `type86_B` | `(8,6,9)` | `h_9≠0` | 10 | `2de11fe3…` (625 bytes) |

Pipeline: (i) `msolve -P 2` on the locked `.ms`; (ii) if POSDIM, M2 rational section (`slice_rational.m2`) writing a sliced `.ms`, sage Groebner fallback; a point of `I+(lin)` is a point of `I` (certificate = the forms); (iii) sage RUR → one M2 script per closed point (QQ or a primitive number field); (iv) `idpApply86` + rewritten `idpPostcheck`. Caps: solve 7200 s each; slice 3600 s; RUR 600 s; per-point idp 300 s; max 64 points.

## 4. Exact verdict rules (point and type)

**Per point** (after building `(p,q)` over the coefficient field):

- `REALIZED` iff all hold: not in-chart cover `B=D=F=gam=e=0`; immersive (`gcd(p',q')=1`); `I_DP` 0-dimensional of degree `N=δ_aff`; reduced; wronskian non-vanishing on `V(I_DP)`; parameter polynomial \(F\) square-free (no reused parameter / triple fibre).
- `NON-REALIZABLE` if any clause FAILs.
- `UNDECIDED` if a step times out or `F` cannot be extracted (`OPEN` inside the checker).

**Per type:**

- `REALIZED` iff some extracted point is `REALIZED`. One closed nodal point suffices (charged NODAL-REALIZATION §2). `REPRESENTATIVE` is not `FULL_ACTUAL_EXIT`.
- `NON-REALIZABLE` iff the characteristic ideal is 0-dimensional, the RUR census is complete (not truncated at 64), and every point is `NON-REALIZABLE`.
- `UNDECIDED` otherwise: TIMEOUT; POSDIM with no nodal witness on the tried sections; incomplete census; solve-mode EMPTY that contradicts a proper Groebner basis (engine disagreement — do not promote a kill); real boxes without RUR.

EMPTY of the *open characteristic ideal* (already refuted for these two types) would be NON-REALIZABLE as a polynomial curve. That verdict is not available here.

---
## 5. `interpret_msolve.py`

```interpret_msolve.py
#!/usr/bin/env python3
"""Classify msolve output by MODE, not by a single bracket convention.

GROEBNER mode (-g 1/2): comments include 'Reduced Groebner basis' / 'length of
basis'. The unit ideal (EMPTY variety) is a basis whose only element is the
constant 1. A proper basis is NONEMPTY. Do not treat a leading coefficient 1
as the unit ideal.

SOLVE mode (default, optionally -P): top-level list. Fetched msolve 0.10.1
man page and tutorial §6 (SHA-256 de8ae1ad54e228b18af9c9123730077e1696638c3f52d677480ad7a258edb1cd):
  [-1]                         EMPTY (no point in an algebraic closure)
  [1, nvars, -1, []]           POSDIM (infinitely many points)
  [0, <payload>]               ZERODIM
    payload with -P 2: RUR [char, nvars, deg, vars, form, [1, [lw, lwp, param]]]
    payload without -P, char 0: real isolating boxes only (not algebraic points)

Exit codes: 0 classify-ok, 2 bad usage, 3 unrecognized.
"""
from __future__ import print_function
import argparse
import os
import re
import sys

def read(path):
    with open(path, "r") as handle:
        return handle.read()

def groebner_unit_ideal(body):
    """True iff the printed basis is exactly the constant 1."""
    # Drop comment lines. Remainder is a list of polynomials, trailing colon.
    lines = []
    for line in body.splitlines():
        if line.lstrip().startswith("#"):
            continue
        lines.append(line)
    blob = "\n".join(lines).strip().rstrip(":").strip()
    if not (blob.startswith("[") and blob.endswith("]")):
        return False
    inner = blob[1:-1].strip()
    # Unit ideal: a single constant 1 (optional sign, no variable, no comma).
    return re.fullmatch(r"[+\-]?1", inner) is not None

def classify(text):
    if re.search(r"Reduced Groebner basis|length of basis:", text):
        match = re.search(r"length of basis:\s*(\d+)", text)
        length = int(match.group(1)) if match else None
        if length == 1 and groebner_unit_ideal(text):
            return "EMPTY", "GROEBNER", "basis={1} unit ideal"
        if length is None:
            return "UNRECOGNIZED", "GROEBNER", "missing length of basis"
        if length == 0:
            return "UNRECOGNIZED", "GROEBNER", "length 0"
        return "NONEMPTY_GB", "GROEBNER", "proper basis length=%d" % length
    # Solve mode: scan the first top-level token after comments.
    body = "\n".join(
        ln for ln in text.splitlines() if not ln.lstrip().startswith("#")
    ).strip()
    if re.match(r"\[-1\]", body):
        return "EMPTY", "SOLVE", "[-1]"
    if re.match(r"\[1\s*,", body):
        if re.match(r"\[1\s*,\s*\d+\s*,\s*-1\s*,\s*\[\s*\]\s*\]", body):
            return "POSDIM", "SOLVE", "[1, nvars, -1, []]"
        return "UNRECOGNIZED", "SOLVE", "leading [1, not the posdim tuple"
    if re.match(r"\[0\s*,", body):
        if re.search(r"-P|parametrization|lw|\[0,\s*\[0,", body) or re.search(
            r"\['[A-Za-z0-9]+'", body
        ):
            # RUR vars list looks like ['z1', 'z2', 'A']
            return "ZERODIM_RUR", "SOLVE", "[0, RUR]"
        # Heuristic: a vars list of quoted names => RUR; else real boxes.
        if re.search(r"'[A-Za-z]", body):
            return "ZERODIM_RUR", "SOLVE", "[0, RUR]"
        return "ZERODIM_BOXES", "SOLVE", "[0, real isolating boxes; not algebraic]"
    if not body:
        return "NO_OUTPUT", "UNKNOWN", "empty file"
    return "UNRECOGNIZED", "UNKNOWN", "first tokens: %r" % body[:80]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output")
    parser.add_argument("--expect-mode", choices=["GROEBNER", "SOLVE"], default=None)
    args = parser.parse_args()
    if not os.path.isfile(args.output):
        print("NO_OUTPUT\tUNKNOWN\tmissing file", file=sys.stderr)
        sys.exit(3)
    kind, mode, note = classify(read(args.output))
    print("%s\t%s\t%s" % (kind, mode, note))
    if args.expect_mode and mode != args.expect_mode and kind not in (
        "NO_OUTPUT",
        "UNRECOGNIZED",
    ):
        print("mode mismatch: got %s want %s" % (mode, args.expect_mode), file=sys.stderr)
        sys.exit(3)
    if kind in ("UNRECOGNIZED", "NO_OUTPUT"):
        sys.exit(3)
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

## 6. Characteristic inputs

```type86_A.ms
B,C,D,E,F,G,b,gam,d,e,f,u
0
3*B-4*gam,
-12*b*gam+3*D-4*e,
-12*b^2*gam+6*B*C-12*b*e-12*gam*d+3*F,
-4*b^3*gam+B^3-12*b^2*e-24*b*gam*d-4*gam^3+6*B*E+6*C*D-12*gam*f-12*d*e,
-4*b^3*e-12*b^2*gam*d-4*b*gam^3+3*B^2*D+3*B*C^2-24*b*gam*f-24*b*d*e-12*gam^2*e-12*gam*d^2+6*B*G+6*C*F+6*D*E-12*e*f,
-12*b^2*gam*f*u-12*b^2*d*e*u-12*b*gam^2*e*u-12*b*gam*d^2*u-4*gam^3*d*u+3*B^2*F*u+6*B*C*E*u+3*B*D^2*u+3*C^2*D*u-24*b*e*f*u-24*gam*d*f*u-12*gam*e^2*u-12*d^2*e*u+6*D*G*u+6*E*F*u-1
```

```type86_B.ms
B,C,D,E,F,G,b,gam,d,e,f,u
0
3*B-4*gam,
-12*b*gam+3*D-4*e,
-12*b^2*gam+6*B*C-12*b*e-12*gam*d+3*F,
-4*b^3*gam+B^3-12*b^2*e-24*b*gam*d-4*gam^3+6*B*E+6*C*D-12*gam*f-12*d*e,
-4*b^3*e-12*b^2*gam*d-4*b*gam^3+3*B^2*D+3*B*C^2-24*b*gam*f-24*b*d*e-12*gam^2*e-12*gam*d^2+6*B*G+6*C*F+6*D*E-12*e*f,
-12*b^2*gam*f-12*b^2*d*e-12*b*gam^2*e-12*b*gam*d^2-4*gam^3*d+3*B^2*F+6*B*C*E+3*B*D^2+3*C^2*D-24*b*e*f-24*gam*d*f-12*gam*e^2-12*d^2*e+6*D*G+6*E*F,
-12*b^2*e*f*u-24*b*gam*d*f*u-12*b*gam*e^2*u-12*b*d^2*e*u-4*gam^3*f*u-12*gam^2*d*e*u-4*gam*d^3*u+6*B*C*G*u+6*B*D*F*u+3*B*E^2*u+3*C^2*F*u+6*C*D*E*u+D^3*u-12*gam*f^2*u-24*d*e*f*u-4*e^3*u+6*F*G*u-1
```

## 7. `rur_to_points.sage`

```rur_to_points.sage
# rur_to_points.sage
# Consume msolve -P 2 RUR (tutorial §6) and emit one M2 script per closed point.
# Usage: sage rur_to_points.sage RURFILE OUTDIR NEXPECTED
# Does not run idp_postcheck. Algebraic points: QQ or a primitive number field.

import os, sys, re

def load_payload(path):
    text = open(path).read().strip()
    if text.endswith(":"):
        text = text[:-1]
    body = "\n".join(ln for ln in text.splitlines() if not ln.lstrip().startswith("#"))
    return sage_eval(body)

def poly_from_enc(enc, R):
    deg, coeffs = enc[0], enc[1]
    if len(coeffs) != deg + 1:
        raise ValueError("RUR encoding length %s != deg+1 %s" % (len(coeffs), deg + 1))
    return R(coeffs)

def qq_str(c):
    c = QQ(c)
    if c.denominator() == 1:
        return str(c.numerator())
    return "(%s/%s)" % (c.numerator(), c.denominator())

def nf_str(elt, prim="primEl"):
    """Write elt of QQ(a) as an M2 polynomial in primEl with QQ coeffs."""
    pol = elt.polynomial()  # in QQ[x]
    parts = []
    for k, ck in enumerate(pol.list()):
        if ck == 0:
            continue
        cs = qq_str(ck)
        if k == 0:
            parts.append(cs)
        elif k == 1:
            parts.append(cs + "*" + prim if ck != 1 else prim)
            if ck == -1:
                parts[-1] = "(-1)*" + prim
        else:
            if ck == 1:
                parts.append("%s^%d" % (prim, k))
            elif ck == -1:
                parts.append("(-1)*%s^%d" % (prim, k))
            else:
                parts.append("%s*%s^%d" % (cs, prim, k))
    if not parts:
        return "0"
    return " + ".join(parts)

def emit_qq_point(path, coords, N, idx):
    vals = ", ".join(qq_str(c) for c in coords)
    open(path, "w").write(
        "load \"idp_postcheck.m2\";\n"
        "load \"idp_apply_point.m2\";\n"
        "vals = {%s};\n"
        "Nexpected = %d;\n"
        "ok = idpApply86(vals, Nexpected);\n"
        "if ok then << \"POINT PASS idx=%d\" << endl else << \"POINT FAIL idx=%d\" << endl;\n"
        "exit(if ok then 0 else 1);\n" % (vals, N, idx, idx)
    )

def emit_nf_point(path, minpoly, coords, N, idx):
    # minpoly in QQ[T], monic
    mp = minpoly.change_ring(QQ)
    coeffs = ", ".join(qq_str(c) for c in mp.list())
    deg = mp.degree()
    # M2: toField(QQ[zz] / (sum c_k zz^k))
    terms = []
    for k, ck in enumerate(mp.list()):
        if ck == 0:
            continue
        if k == 0:
            terms.append(qq_str(ck))
        elif k == 1:
            terms.append(qq_str(ck) + "*zz" if ck != 1 else "zz")
        else:
            terms.append("%s*zz^%d" % (qq_str(ck), k) if ck != 1 else "zz^%d" % k)
    minpoly_m2 = " + ".join(terms) if terms else "1"
    val_items = []
    for c in coords:
        val_items.append(nf_str(c, "primEl"))
    vals = ", ".join(val_items)
    open(path, "w").write(
        "load \"idp_postcheck.m2\";\n"
        "load \"idp_apply_point.m2\";\n"
        "minRing = QQ[zz];\n"
        "zz = minRing_0;\n"
        "K = toField(minRing / (%s));\n"
        "primEl = K_0;\n"
        "vals = {%s};\n"
        "Nexpected = %d;\n"
        "ok = idpApply86(vals, Nexpected);\n"
        "if ok then << \"POINT PASS idx=%d\" << endl else << \"POINT FAIL idx=%d\" << endl;\n"
        "exit(if ok then 0 else 1);\n" % (minpoly_m2, vals, N, idx, idx)
    )

def coords_from_rur(rur, theta, w, wden):
    char, nvars, deg, varnames, form, rest = rur
    one, trip = rest
    lw, lwp, param = trip
    coords = []
    den = wden(theta)
    if den == 0:
        raise ValueError("RUR denominator vanishes at a root (non-generic form)")
    for penc in param:
        enc, cdiv = penc[0], penc[1]
        R = w.parent()
        v = poly_from_enc(enc, R) / QQ(cdiv)
        coords.append(- v(theta) / den)
    # last variable is the parameter
    coords.append(theta)
    if len(coords) != nvars:
        raise ValueError("coord count %s != nvars %s" % (len(coords), nvars))
    return coords, list(varnames)

def take_coeff_coords(coords, varnames):
    """Drop slack u and any extra genericity variable A; keep B..f in chart order."""
    want = ["B","C","D","E","F","G","b","gam","d","e","f"]
    mp = {str(n).strip("'"): coords[i] for i, n in enumerate(varnames)}
    missing = [w for w in want if w not in mp]
    if missing:
        raise ValueError("RUR vars missing %s; have %s" % (missing, list(mp)))
    return [mp[w] for w in want]

def main():
    if len(sys.argv) != 4:
        print("usage: sage rur_to_points.sage RURFILE OUTDIR NEXPECTED")
        sys.exit(2)
    path, outdir, N = sys.argv[1], sys.argv[2], int(sys.argv[3])
    data = load_payload(path)
    if data == [-1] or (isinstance(data, list) and data and data[0] == -1):
        open(os.path.join(outdir, "KIND"), "w").write("EMPTY\n")
        return
    if isinstance(data, list) and data[0] == 1:
        open(os.path.join(outdir, "KIND"), "w").write("POSDIM\n")
        return
    if not (isinstance(data, list) and data[0] == 0):
        raise ValueError("not a solve-mode payload")
    rur = data[1]
    # -P 1 appends real boxes after the RUR; the RUR is rur[0] if nested. Tutorial -P 2: rur is the list.
    if isinstance(rur, list) and rur and isinstance(rur[0], list) and len(rur) == 2 and rur[0] and rur[0][0] in (0, 1):
        # unlikely
        pass
    char = rur[0]
    if char != 0:
        raise ValueError("expected characteristic 0 RUR")
    os.makedirs(outdir, exist_ok=True)
    R.<T> = QQ[]
    trip = rur[5][1]
    w = poly_from_enc(trip[0], R)
    wden = poly_from_enc(trip[1], R)
    idx = 0
    n_written = 0
    MAXP = 64
    for fac, exp in list(w.factor()):
        if fac.degree() == 0:
            continue
        if n_written >= MAXP:
            open(os.path.join(outdir, "TRUNCATED"), "w").write("hit MAXP=%d\n" % MAXP)
            break
        if fac.degree() == 1:
            theta = -fac.constant_coefficient() / fac.leading_coefficient()
            theta = QQ(theta)
            coords, names = coords_from_rur(rur, theta, w, wden)
            chart = take_coeff_coords(coords, names)
            emit_qq_point(os.path.join(outdir, "p%03d.m2" % idx), chart, N, idx)
            n_written += 1
            idx += 1
        else:
            K.<a> = NumberField(fac)
            theta = a
            # reinterpret polynomials in K[T]
            RK.<TK> = K[]
            wK = RK(w)
            wdenK = RK(wden)
            # rebuild param over K via the same encodings
            char, nvars, deg, varnames, form, rest = rur
            one, trip2 = rest
            lw, lwp, param = trip2
            den = wdenK(theta)
            if den == 0:
                raise ValueError("RUR denominator vanishes")
            coords = []
            for penc in param:
                enc, cdiv = penc[0], penc[1]
                v = RK(poly_from_enc(enc, R)) / QQ(cdiv)
                coords.append(- v(theta) / den)
            coords.append(theta)
            chart = take_coeff_coords(coords, list(varnames))
            emit_nf_point(os.path.join(outdir, "p%03d.m2" % idx), fac, chart, N, idx)
            n_written += 1
            idx += 1
    open(os.path.join(outdir, "KIND"), "w").write("ZERODIM_RUR npoints=%d deg_w=%d\n" % (n_written, w.degree()))
    print("rur_to_points: wrote", n_written, "point scripts under", outdir)

if __name__ == "__main__":
    main()
```

## 8. Rational-slice scripts

```slice_rational.m2
-- slice_rational.m2
-- Rational linear sections of a NONEMPTY (8,6) characteristic ideal.
-- Flattened ring built ONCE. No tower, no saturate(), no reserved names.
-- A point of I + (lin_1,...,lin_k) is a point of I (certificate = the forms).
-- Usage: M2 slice_rational.m2   with env JOB=type86_A or type86_B.
-- Writes logs/slice_<job>.ms and logs/slice_<job>.cert.

jobName = getenv("JOB");
if jobName == "" then jobName = "type86_A";

CoeffRing = QQ[B, C, D, E, F, G, b, gam, d, e, f, u, MonomialOrder => GRevLex];
assert(isPolynomialRing CoeffRing);
assert(numgens CoeffRing == 12);
assert(coefficientRing CoeffRing === QQ);
use CoeffRing;

h21 = 3*B - 4*gam;
h19 = -12*b*gam + 3*D - 4*e;
h17 = -12*b^2*gam + 6*B*C - 12*b*e - 12*gam*d + 3*F;
h15 = -4*b^3*gam + B^3 - 12*b^2*e - 24*b*gam*d - 4*gam^3 + 6*B*E + 6*C*D - 12*gam*f - 12*d*e;
h13 = -4*b^3*e - 12*b^2*gam*d - 4*b*gam^3 + 3*B^2*D + 3*B*C^2 - 24*b*gam*f - 24*b*d*e - 12*gam^2*e - 12*gam*d^2 + 6*B*G + 6*C*F + 6*D*E - 12*e*f;
h11 = -12*b^2*gam*f - 12*b^2*d*e - 12*b*gam^2*e - 12*b*gam*d^2 - 4*gam^3*d + 3*B^2*F + 6*B*C*E + 3*B*D^2 + 3*C^2*D - 24*b*e*f - 24*gam*d*f - 12*gam*e^2 - 12*d^2*e + 6*D*G + 6*E*F;
h9 = -12*b^2*e*f - 24*b*gam*d*f - 12*b*gam*e^2 - 12*b*d^2*e - 4*gam^3*f - 12*gam^2*d*e - 4*gam*d^3 + 6*B*C*G + 6*B*D*F + 3*B*E^2 + 3*C^2*F + 6*C*D*E + D^3 - 12*gam*f^2 - 24*d*e*f - 4*e^3 + 6*F*G;

charGens = if jobName == "type86_B"
  then {h21, h19, h17, h15, h13, h11, h9*u - 1}
  else {h21, h19, h17, h15, h13, h11*u - 1};
charIdeal = ideal charGens;
assert(ring charIdeal === CoeffRing);

sliceForms = {B - 1, gam - 1, b - 1, C, d - 1, E, G, f, F - 1, e - 1};
sliceNames = {"B-1", "gam-1", "b-1", "C", "d-1", "E", "G", "f", "F-1", "e-1"};

curIdeal = charIdeal;
acceptedNames = {};
sidx = 0;
while sidx < #sliceForms and dim curIdeal > 0 do (
  trial := curIdeal + ideal(sliceForms#sidx);
  assert(ring trial === CoeffRing);
  dtrial := dim trial;
  if dtrial >= 0 and dtrial < dim curIdeal then (
    curIdeal = trial;
    acceptedNames = append(acceptedNames, sliceNames#sidx);
    << "slice: accepted " << sliceNames#sidx << " dim -> " << dtrial << endl;
  );
  sidx = sidx + 1;
);

<< "slice: final dim=" << dim curIdeal << " nforms=" << #acceptedNames << endl;
certPath = "logs/slice_" | jobName | ".cert";
msPath = "logs/slice_" | jobName | ".ms";
certFile = openOut certPath;
certFile << "job " << jobName << endl;
certFile << "dim " << dim curIdeal << endl;
scan(acceptedNames, nm -> certFile << "form " << nm << endl);
if dim curIdeal != 0 then (
  certFile << "status POSDIM_AFTER_SLICES" << endl;
  close certFile;
  << "slice: UNDECIDED still positive-dimensional" << endl;
) else (
  certFile << "status ZERODIM_SLICE" << endl;
  close certFile;
  baseMs := if jobName == "type86_B" then get "type86_B.ms" else get "type86_A.ms";
  nlen := length baseMs;
  baseTrim := if nlen > 0 then substring(0, nlen - 1, baseMs) else baseMs;
  extra := concatenate apply(acceptedNames, nm -> ("," | newline | nm));
  msFile = openOut msPath;
  msFile << baseTrim << extra << endl;
  close msFile;
  << "slice: wrote " << msPath << endl;
);
```

```slice_rational.sage
# slice_rational.sage
# Certified fallback for slice_rational.m2. Same flattened chart, same forms.
# A point of I+(lin) is a point of I. Groebner dimension via leading-term staircase.
# FLAG: sage.rings.polynomial groebner_basis is used; not SIROCCO.

import os, sys

job = os.environ.get("JOB", "type86_A")
R = PolynomialRing(QQ, names=("B","C","D","E","F","G","b","gam","d","e","f","u"), order="degrevlex")
B, C, D, E, F, G, b, gam, d, e, f, u = R.gens()

h21 = 3*B - 4*gam
h19 = -12*b*gam + 3*D - 4*e
h17 = -12*b**2*gam + 6*B*C - 12*b*e - 12*gam*d + 3*F
h15 = -4*b**3*gam + B**3 - 12*b**2*e - 24*b*gam*d - 4*gam**3 + 6*B*E + 6*C*D - 12*gam*f - 12*d*e
h13 = (-4*b**3*e - 12*b**2*gam*d - 4*b*gam**3 + 3*B**2*D + 3*B*C**2
       - 24*b*gam*f - 24*b*d*e - 12*gam**2*e - 12*gam*d**2 + 6*B*G + 6*C*F + 6*D*E - 12*e*f)
h11 = (-12*b**2*gam*f - 12*b**2*d*e - 12*b*gam**2*e - 12*b*gam*d**2 - 4*gam**3*d
       + 3*B**2*F + 6*B*C*E + 3*B*D**2 + 3*C**2*D - 24*b*e*f - 24*gam*d*f
       - 12*gam*e**2 - 12*d**2*e + 6*D*G + 6*E*F)
h9 = (-12*b**2*e*f - 24*b*gam*d*f - 12*b*gam*e**2 - 12*b*d**2*e - 4*gam**3*f
      - 12*gam**2*d*e - 4*gam*d**3 + 6*B*C*G + 6*B*D*F + 3*B*E**2 + 3*C**2*F
      + 6*C*D*E + D**3 - 12*gam*f**2 - 24*d*e*f - 4*e**3 + 6*F*G)

if job == "type86_B":
    gens0 = [h21, h19, h17, h15, h13, h11, h9*u - 1]
    base_path = "type86_B.ms"
else:
    gens0 = [h21, h19, h17, h15, h13, h11*u - 1]
    base_path = "type86_A.ms"

forms = [B - 1, gam - 1, b - 1, C, d - 1, E, G, f, F - 1, e - 1]
form_names = ["B-1", "gam-1", "b-1", "C", "d-1", "E", "G", "f", "F-1", "e-1"]

def krull_dim(ideal):
    gb = ideal.groebner_basis()
    if gb == [1]:
        return -1
    return ideal.dimension()

cur = R.ideal(gens0)
accepted = []
dcur = krull_dim(cur)
print("slice-sage: start dim", dcur)
if dcur < 0:
    print("slice-sage: EMPTY (contradicts NONEMPTY)")
    sys.exit(1)
for form, name in zip(forms, form_names):
    if dcur == 0:
        break
    trial = cur + R.ideal(form)
    dtrial = krull_dim(trial)
    if dtrial >= 0 and dtrial < dcur:
        cur = trial
        dcur = dtrial
        accepted.append(name)
        print("slice-sage: accepted", name, "dim ->", dcur)

os.makedirs("logs", exist_ok=True)
cert = open("logs/slice_%s.cert" % job, "w")
cert.write("job %s\n" % job)
cert.write("dim %s\n" % dcur)
for name in accepted:
    cert.write("form %s\n" % name)
if dcur != 0:
    cert.write("status POSDIM_AFTER_SLICES\n")
    cert.close()
    print("slice-sage: UNDECIDED still positive-dimensional")
    sys.exit(0)
cert.write("status ZERODIM_SLICE\n")
cert.close()
base = open(base_path).read().rstrip("\n")
extra = "".join(",\n%s" % name for name in accepted)
open("logs/slice_%s.ms" % job, "w").write(base + extra + "\n")
print("slice-sage: wrote logs/slice_%s.ms" % job)
```

## 9. Rewritten postcheck

```idp_postcheck.m2
-- idp_postcheck.m2
-- Rewritten double-point postcheck. Dialect lessons (1)-(6):
-- (1) no reserved locals pi, gamma, I, O
-- (2) no tower rings; every polynomial ring is flattened and generators
--     are read as R_0, R_1, ... immediately
-- (3) coefficients via (ring f)_0, never a rebound global
-- (4) diff(var, poly)
-- (5) first degree, with the 0-polynomial branched off
-- (6) no underscore-subscript identifiers
-- No saturate(). Self-test: (6,4,3) witness PASS; (t^8,t^6) FAIL.

intDeg = (f) -> (
  if f == 0 then -1 else first degree f
);

srcVar = (f) -> (ring f)_0;

rebuildIn = (f, tgtvar) -> (
  src := srcVar f;
  tgtR := ring tgtvar;
  acc := 0_tgtR;
  df := intDeg f;
  if df < 0 then return acc;
  for n from 0 to df do (
    c := coefficient(src^n, f);
    acc = acc + sub(c, tgtR) * tgtvar^n;
  );
  acc
);

dividedDiffTable = (maxn, sumV, prodV) -> (
  pr := ring sumV;
  L := new MutableList from toList((maxn + 1) : 0_pr);
  L#0 = 0_pr;
  if maxn >= 1 then L#1 = 1_pr;
  if maxn >= 2 then L#2 = sumV;
  for n from 3 to maxn do L#n = sumV * (L#(n - 1)) - prodV * (L#(n - 2));
  toList L
);

polyToDelta = (f, L) -> (
  src := srcVar f;
  acc := 0_(ring L#1);
  df := intDeg f;
  if df < 0 then return acc;
  for n from 0 to df do (
    c := coefficient(src^n, f);
    acc = acc + sub(c, ring L#1) * L#n;
  );
  acc
);

wronskianSym = (p, q, sumV, prodV) -> (
  K := coefficientRing ring p;
  ST := K[svar, tvarST, MonomialOrder => GRevLex];
  assert(numgens ST == 2);
  svarLoc := ST_0;
  tvarLoc := ST_1;
  pS := rebuildIn(p, svarLoc);
  pT := rebuildIn(p, tvarLoc);
  qS := rebuildIn(q, svarLoc);
  qT := rebuildIn(q, tvarLoc);
  Wp := diff(tvarLoc, pT) * diff(svarLoc, qS) - diff(svarLoc, pS) * diff(tvarLoc, qT);
  assert((Wp % (svarLoc - tvarLoc)) == 0);
  W1 := Wp // (svarLoc - tvarLoc);
  CR := K[svarC, sumC, prodC, MonomialOrder => Lex];
  assert(numgens CR == 3);
  svarCLoc := CR_0;
  sumCLoc := CR_1;
  prodCLoc := CR_2;
  toConv := map(CR, ST, {svarCLoc, sumCLoc - svarCLoc});
  Waux := toConv W1;
  Wred := Waux % ideal(svarCLoc * (sumCLoc - svarCLoc) - prodCLoc);
  -- degree(var, poly): highest power of var (M2 doc degree(RingElement,RingElement))
  assert(degree(svarCLoc, Wred) <= 0 or Wred == 0);
  PR := ring sumV;
  map(PR, CR, {0_PR, sumV, prodV}) Wred
);

idpPostcheck = method();
idpPostcheck(RingElement, RingElement, ZZ) := (p, q, N) -> (
  Kt := ring p;
  assert(Kt === ring q);
  assert(isPolynomialRing Kt);
  assert(numgens Kt == 1);
  srcT := Kt_0;
  dp := diff(srcT, p);
  dq := diff(srcT, q);
  gg := gcd(dp, dq);
  immersive := (gg == 1_Kt);
  K := coefficientRing Kt;
  PR := K[sumV, prodV, MonomialOrder => GRevLex];
  assert(numgens PR == 2);
  sumLoc := PR_0;
  prodLoc := PR_1;
  maxn := max(intDeg p, intDeg q);
  L := dividedDiffTable(maxn, sumLoc, prodLoc);
  Dp := polyToDelta(p, L);
  Dq := polyToDelta(q, L);
  idpIdeal := ideal(Dp, Dq);
  assert(ring idpIdeal === PR);
  << "idp: dim=" << dim idpIdeal;
  if dim idpIdeal == 0 then << " degree=" << degree idpIdeal;
  << " immersive=" << immersive << endl;
  if not immersive then (
    << "idp: FAIL not immersive (gcd-cover)" << endl;
    return false;
  );
  if dim idpIdeal != 0 then (
    << "idp: FAIL not 0-dimensional" << endl;
    return false;
  );
  if degree idpIdeal != N then (
    << "idp: FAIL length " << degree idpIdeal << " != expected " << N << endl;
    return false;
  );
  if idpIdeal != radical idpIdeal then (
    << "idp: FAIL not reduced" << endl;
    return false;
  );
  Wsym := wronskianSym(p, q, sumLoc, prodLoc);
  tanIdeal := idpIdeal + ideal(Wsym);
  assert(ring tanIdeal === PR);
  if tanIdeal != ideal(1_PR) then (
    << "idp: FAIL coincident tangents" << endl;
    return false;
  );
  ER := K[indX, sumE, prodE, MonomialOrder => Lex];
  assert(numgens ER == 3);
  indLoc := ER_0;
  sumELoc := ER_1;
  prodELoc := ER_2;
  idpE := sub(idpIdeal, ER);
  quad := indLoc^2 - sumELoc * indLoc + prodELoc;
  Gmat := gens gb(idpE + ideal(quad));
  FR := K[indX2];
  assert(numgens FR == 1);
  indF := FR_0;
  FX := 0_FR;
  scan(flatten entries Gmat, gelem -> (
    if gelem != 0 and degree(sumELoc, gelem) <= 0 and degree(prodELoc, gelem) <= 0 then (
      FX = sub(gelem, FR);
    );
  ));
  if FX == 0 then (
    << "idp: OPEN could not extract parameter polynomial F" << endl;
    return false;
  );
  dFX := diff(indF, FX);
  if gcd(FX, dFX) != 1_FR then (
    << "idp: FAIL reused parameter / triple fibre (F not square-free)" << endl;
    return false;
  );
  << "idp: PASS length=" << N << " reduced, distinct tangents, no reused parameter" << endl;
  true
);

-- Library only. Self-test lives in idp_selftest.m2 so load() does not rerun it.
```

```idp_apply_point.m2
-- idp_apply_point.m2
-- Apply idpPostcheck to one (8,6)-chart closed point.
-- Requires idp_postcheck.m2 already loaded.
-- idpApply86(vals, N): vals = {B,C,D,E,F,G,b,gam,d,e,f} in a field K.
-- Cover exclusion: in-chart even locus B=D=F=gam=e=0 is FAIL (gcd-2).
-- Rings: K[paramt] flattened, built after K is known. No tower.

idpApply86 = method();
idpApply86(List, ZZ) := (vals, N) -> (
  if #vals != 11 then error "idpApply86: expected 11 coefficients B..f";
  Kcand := QQ;
  scan(vals, v -> (
    Rv := ring v;
    if Rv =!= ZZ and Rv =!= QQ then Kcand = Rv;
  ));
  K := Kcand;
  valsK := apply(vals, v -> sub(v, K));
  -- in-chart gcd-2 cover: B, D, F, gam, e
  if valsK#0 == 0 and valsK#2 == 0 and valsK#4 == 0 and valsK#7 == 0 and valsK#9 == 0 then (
    << "idpApply86: FAIL in-chart gcd-2 cover (B=D=F=gam=e=0)" << endl;
    return false;
  );
  Kt := K[paramt];
  assert(isPolynomialRing Kt);
  assert(numgens Kt == 1);
  pt := Kt_0;
  toKt := (c) -> sub(c, Kt);
  vals = valsK;
  ppoly := pt^8 + toKt(vals#0)*pt^5 + toKt(vals#1)*pt^4 + toKt(vals#2)*pt^3
           + toKt(vals#3)*pt^2 + toKt(vals#4)*pt + toKt(vals#5);
  qpoly := pt^6 + toKt(vals#6)*pt^4 + toKt(vals#7)*pt^3 + toKt(vals#8)*pt^2
           + toKt(vals#9)*pt + toKt(vals#10);
  idpPostcheck(ppoly, qpoly, N)
);
```

```idp_selftest.m2
-- idp_selftest.m2
-- Positive: ROW-SWEEP (6,4,3) witness. Negative: (t^8,t^6).
-- Flattened QQ[paramt] built once before any symbol use.

load "idp_postcheck.m2";
KtQQ = QQ[paramt];
assert(isPolynomialRing KtQQ);
assert(numgens KtQQ == 1);
pt = KtQQ_0;
rpoly = pt^3 + pt + 1;
qWitness = pt^4 + (2/3)*pt^2 + (4/3)*pt;
pWitness = rpoly^2;
assert(idpPostcheck(pWitness, qWitness, 3));
assert(not idpPostcheck(pt^8, pt^6, 11));
<< "=== idp_postcheck self-tests completed ===" << endl;
```

## 10. Driver `run_point_postcheck.sh`

```run_point_postcheck.sh
#!/usr/bin/env bash
# run_point_postcheck.sh
# AWS-only: extract closed points of (8,6,11) and (8,6,9), run repaired idp_postcheck.
# Requires POINTPOSTCHECK_AWS=1. Controls first; abort on self-test FAIL.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
LOG="$ROOT/logs"
mkdir -p "$LOG"
SUMMARY="$LOG/summary.tsv"
echo -e "job\tstatus\tseconds\tnote" > "$SUMMARY"

if [[ "${POINTPOSTCHECK_AWS:-0}" != "1" ]]; then
  echo "Refusing to run: set POINTPOSTCHECK_AWS=1 on the AWS box." >&2
  echo "This suite is campaign-policy AWS-ONLY (heavy/uncertain CAS)." >&2
  exit 2
fi

have_msolve=0; have_m2=0; have_sage=0
command -v msolve >/dev/null 2>&1 && have_msolve=1
command -v M2 >/dev/null 2>&1 && have_m2=1
command -v sage >/dev/null 2>&1 && have_sage=1
if [[ "$have_msolve" -eq 0 ]]; then echo "msolve missing" >&2; exit 2; fi
if [[ "$have_m2" -eq 0 ]]; then echo "M2 missing" >&2; exit 2; fi

run_timeout() {
  local cap="$1"; shift
  if command -v timeout >/dev/null 2>&1; then
    timeout --signal=TERM --kill-after=30s "$cap" "$@"
  elif command -v gtimeout >/dev/null 2>&1; then
    gtimeout --signal=TERM --kill-after=30s "$cap" "$@"
  else
    echo "timeout(1) missing; running without a wall-clock cap" >&2
    "$@"
  fi
}

record() {
  local job="$1" status="$2" secs="$3" note="$4"
  echo -e "${job}\t${status}\t${secs}\t${note}" | tee -a "$SUMMARY"
}

CAP_SELF=180
CAP_SOLVE_A=7200
CAP_SOLVE_B=7200
CAP_SLICE=3600
CAP_RUR=600
CAP_IDP_PT=300
MAX_POINTS=64

echo "=== CONTROL: idp_postcheck self-test ==="
start=$(date +%s)
set +e
run_timeout "$CAP_SELF" M2 --silent --stop --no-preload "$ROOT/idp_selftest.m2" \
  > "$LOG/idp_selftest.out" 2> "$LOG/idp_selftest.err"
rc=$?
set -e
t=$(( $(date +%s) - start ))
if [[ $rc -ne 0 ]] || ! grep -q 'idp_postcheck self-tests completed' "$LOG/idp_selftest.out"; then
  record idp_selftest FAIL "$t" "rc=$rc"
  echo "ABORT: idp self-test failed" >&2
  exit 1
fi
record idp_selftest PASS "$t" "(6,4,3) witness; (t^8,t^6) rejected"

interpret() {
  python3 "$ROOT/interpret_msolve.py" "$1"
}

run_solve() {
  local job="$1" cap="$2" ms="$3"
  start=$(date +%s)
  set +e
  # SOLVE mode: no -g. -P 2 = rational parametrization (tutorial §6).
  local fpath="$ms"
  [[ "$ms" = /* ]] || fpath="$ROOT/$ms"
  run_timeout "$cap" msolve -v 2 -P 2 -f "$fpath" -o "$LOG/${job}.rur" \
    > "$LOG/${job}.msolve.stdout" 2> "$LOG/${job}.msolve.err"
  rc=$?
  set -e
  echo $(( $(date +%s) - start ))
  echo "$rc" > "$LOG/${job}.msolve.rc"
  return 0
}

postcheck_points() {
  local job="$1" pdir="$2"
  local npass=0 nfail=0 nrun=0
  local f
  shopt -s nullglob
  for f in "$pdir"/p*.m2; do
    if [[ $nrun -ge $MAX_POINTS ]]; then
      record "${job}_idp" UNDECIDED 0 "hit MAX_POINTS=$MAX_POINTS"
      break
    fi
    start=$(date +%s)
    set +e
    run_timeout "$CAP_IDP_PT" M2 --silent --stop --no-preload "$f" \
      > "$LOG/${job}_$(basename "$f" .m2).out" 2> "$LOG/${job}_$(basename "$f" .m2).err"
    rc=$?
    set -e
    t=$(( $(date +%s) - start ))
    nrun=$((nrun + 1))
    if grep -q 'POINT PASS' "$LOG/${job}_$(basename "$f" .m2).out" 2>/dev/null; then
      npass=$((npass + 1))
      record "${job}_$(basename "$f" .m2)" REALIZED "$t" "idp PASS"
    else
      nfail=$((nfail + 1))
      record "${job}_$(basename "$f" .m2)" NON-REALIZABLE "$t" "rc=$rc"
    fi
  done
  echo "$npass $nfail $nrun" > "$pdir/COUNTS"
}

type_verdict() {
  local job="$1" kind="$2" npass="$3" nfail="$4" nrun="$5" truncated="$6"
  # REALIZED: some POINT_NODAL.
  # NON-REALIZABLE: 0-dim complete census, every point POINT_NOT_NODAL.
  # else UNDECIDED.
  if [[ "$npass" -gt 0 ]]; then
    echo REALIZED
    return
  fi
  if [[ "$kind" == "ZERODIM_RUR" && "$truncated" == "0" && "$nrun" -gt 0 && "$nfail" -eq "$nrun" ]]; then
    echo NON-REALIZABLE
    return
  fi
  echo UNDECIDED
}

handle_job() {
  local job="$1" cap="$2" ms="$3" N="$4"
  local t rc line kind mode note pdir npass nfail nrun truncated verdict
  echo "=== EXTRACT $job (msolve SOLVE -P 2) ==="
  t=$(run_solve "$job" "$cap" "$ms")
  rc=$(cat "$LOG/${job}.msolve.rc")
  if [[ $rc -eq 124 || $rc -eq 137 ]]; then
    record "$job" TIMEOUT "$t" "msolve -P 2 cap ${cap}s"
    record "${job}_type" UNDECIDED "$t" "TIMEOUT is not a mathematical verdict"
    return 0
  fi
  line=$(interpret "$LOG/${job}.rur" || true)
  kind=$(echo "$line" | cut -f1)
  mode=$(echo "$line" | cut -f2)
  note=$(echo "$line" | cut -f3-)
  record "$job" "$kind" "$t" "$mode $note"
  if [[ "$kind" == "EMPTY" ]]; then
    record "${job}_type" UNDECIDED "$t" "solve EMPTY contradicts validated NONEMPTY GB; do not promote"
    return 0
  fi
  if [[ "$kind" == "ZERODIM_BOXES" ]]; then
    record "${job}_type" UNDECIDED "$t" "real boxes are not algebraic points; rerun with -P 2"
    return 0
  fi
  if [[ "$kind" == "POSDIM" || "$kind" == "NONEMPTY_GB" ]]; then
    echo "=== SLICE $job (M2, sage fallback) ==="
    start=$(date +%s)
    set +e
    JOB="$job" run_timeout "$CAP_SLICE" M2 --silent --stop --no-preload "$ROOT/slice_rational.m2" \
      > "$LOG/${job}_slice.out" 2> "$LOG/${job}_slice.err"
    rc=$?
    set -e
    ts=$(( $(date +%s) - start ))
    if [[ $rc -eq 124 || $rc -eq 137 || ! -f "$LOG/slice_${job}.ms" ]]; then
      if [[ "$have_sage" -eq 1 ]]; then
        start=$(date +%s)
        set +e
        JOB="$job" run_timeout "$CAP_SLICE" sage "$ROOT/slice_rational.sage" \
          > "$LOG/${job}_slice_sage.out" 2> "$LOG/${job}_slice_sage.err"
        rc=$?
        set -e
        ts=$(( $(date +%s) - start ))
        record "${job}_slice" SAGE_FALLBACK "$ts" "rc=$rc"
      else
        record "${job}_slice" UNDECIDED "$ts" "M2 slice miss and no sage"
        record "${job}_type" UNDECIDED "$ts" "POSDIM, no 0-dim section"
        return 0
      fi
    else
      record "${job}_slice" M2 "$ts" "$(tr '\n' ' ' < "$LOG/slice_${job}.cert" | head -c 200)"
    fi
    if [[ ! -f "$LOG/slice_${job}.ms" ]]; then
      record "${job}_type" UNDECIDED "$ts" "POSDIM_AFTER_SLICES"
      return 0
    fi
    t=$(run_solve "${job}_sliced" "$cap" "logs/slice_${job}.ms")
    line=$(interpret "$LOG/${job}_sliced.rur" || true)
    kind=$(echo "$line" | cut -f1)
    record "${job}_sliced" "$kind" "$t" "$(echo "$line" | cut -f2-)"
    if [[ "$kind" != "ZERODIM_RUR" ]]; then
      record "${job}_type" UNDECIDED "$t" "slice did not yield ZERODIM_RUR"
      return 0
    fi
    job="${job}_sliced"
  fi
  if [[ "$kind" != "ZERODIM_RUR" ]]; then
    record "${job}_type" UNDECIDED 0 "kind=$kind"
    return 0
  fi
  if [[ "$have_sage" -eq 0 ]]; then
    record "${job}_type" UNDECIDED 0 "sage missing; cannot factor RUR"
    return 0
  fi
  pdir="$LOG/pts/${job}"
  mkdir -p "$pdir"
  start=$(date +%s)
  set +e
  run_timeout "$CAP_RUR" sage "$ROOT/rur_to_points.sage" "$LOG/${job}.rur" "$pdir" "$N" \
    > "$LOG/${job}_rur.out" 2> "$LOG/${job}_rur.err"
  rc=$?
  set -e
  trur=$(( $(date +%s) - start ))
  if [[ $rc -ne 0 ]]; then
    record "${job}_rur" FAIL "$trur" "rc=$rc"
    record "${job}_type" UNDECIDED "$trur" "RUR parse failed"
    return 0
  fi
  truncated=0
  [[ -f "$pdir/TRUNCATED" ]] && truncated=1
  postcheck_points "$job" "$pdir"
  if [[ ! -f "$pdir/COUNTS" ]]; then echo "0 0 0" > "$pdir/COUNTS"; fi
  read -r npass nfail nrun < "$pdir/COUNTS"
  verdict=$(type_verdict "$job" "ZERODIM_RUR" "$npass" "$nfail" "$nrun" "$truncated")
  record "${job}_type" "$verdict" "$trur" "npass=$npass nfail=$nfail nrun=$nrun truncated=$truncated"
}

handle_job type86_A "$CAP_SOLVE_A" type86_A.ms 11
handle_job type86_B "$CAP_SOLVE_B" type86_B.ms 10

echo
echo "=== SUMMARY ==="
column -t -s $'\t' "$SUMMARY" || cat "$SUMMARY"
echo
echo "Type-level REALIZED requires some POINT_NODAL."
echo "Type-level NON-REALIZABLE requires a complete 0-dim census with every point POINT_NOT_NODAL."
echo "TIMEOUT / POSDIM-without-nodal-witness / incomplete census = UNDECIDED."
echo "EMPTY of solve-mode that contradicts a proper Groebner basis is UNDECIDED, not a kill."
```

## 11. SHA-256 manifest

Hash convention: SHA-256 of the extracted fence body as UTF-8 POSIX text with exactly one trailing newline. Coordinator re-hashes after extraction.

| file | bytes | SHA-256 |
|---|---:|---|
| `interpret_msolve.py` | 4227 | `1c2bfead6d128ff7a82222d58730e9730d1c29c40075d8f9ea2b8aaaadc73ed2` |
| `type86_A.ms` | 462 | `1b3e8ffa5c8dc814ceda55f02d7f46e23c6bad15222998737245697c9e2d716f` |
| `type86_B.ms` | 625 | `2de11fe3d4b02c3c20ab8650566172baf808fb3c228aaaefbbf3317cc76515e4` |
| `rur_to_points.sage` | 7345 | `c9c2183811b35239d3287b032419c3df690206f353187f8b287051cdfd5ebb97` |
| `slice_rational.m2` | 3113 | `a0551ba51c9df3a6879c6fdb4348547254bad957fe70b3aa669de154b46bc2d2` |
| `slice_rational.sage` | 2792 | `7fb51e80b425dd42f2b40b75032180794c4fec9191d5cc13745fbe691b3aaddd` |
| `idp_postcheck.m2` | 4701 | `d9c21115af0fac09e5b89a196c1656224600d7812cbc82fb04038aa073cb7195` |
| `idp_apply_point.m2` | 1291 | `ebdbc41fdf81c07f5ba4a6c699c6ed18d6a8c3ee933803a397624a96261da0d3` |
| `idp_selftest.m2` | 482 | `43c27bacf7a96632e2b329825b8ed6b3ad35fa5e7745d09beecc6d51fcb336a5` |
| `run_point_postcheck.sh` | 7976 | `04e9b3a394d6a1a27351e34b5dbd97d648d8fb7a9d60ac62ef48ddf476851817` |

`type86_A.ms` / `type86_B.ms` match msolve-prep §13 (generator systems already symbolically cross-checked). Launch: extract the ten fences into one directory; `chmod +x run_point_postcheck.sh interpret_msolve.py`; on the AWS box, `POINTPOSTCHECK_AWS=1 ./run_point_postcheck.sh`. Re-hash against this table first.

## 12. OPEN items, FALLACY-v2, and non-claims

1. **POSDIM sections are not a component census.** Failed slices do not prove NON-REALIZABLE. Typed `UNDECIDED` until a nodal point appears or a 0-dim complete census fails.
2. **`K_0` after `toField`.** Number-field primitive element is `K_0`. If a given M2 rejects that, the point script FAILs loudly (desired). FLAG.
3. **Cover encoding** remains the in-chart even locus plus immersive `gcd(p',q')=1`. General quadratic covers that survive Tschirnhausen are intended to be hit by immersivity; not proved equivalent to “`p,q∈C[t^2]` after every linear change of `t`”.
4. **`sat()` is not used.** Open conditions are Rabinowitsch `u` already in the locked `.ms`. Colon of the M2 mirrors is not replayed (timed out; postcheck is pointwise).
5. **`(8,6,7)` and `(8,6,3)`** are still computing (12 h caps) and are not in this bundle.
6. This report asserts no exit price. `REPRESENTATIVE` is not `FULL_ACTUAL_EXIT`. A nonempty characteristic locus is not a nodal witness.

FALLACY-v2: no flag/place/series identification; no pole identity; no floor-as-attainment; ring maps declared (flattened generator order, `QQ` or a named number field, `sub` image checks); `pi`/`prime` marks are not derivatives. If a step has no safe replacement it returns typed `OPEN`/`UNDECIDED`.

This lane did not run msolve, M2, Sage, or Groebner. Coefficient polynomials are the locked msolve-prep expansions.

**Launch recipe.** Extract fences; `chmod +x run_point_postcheck.sh interpret_msolve.py`; `POINTPOSTCHECK_AWS=1 ./run_point_postcheck.sh`. Controls abort the suite on FAIL. Summary: `logs/summary.tsv`.

<!-- BODY-END -->

