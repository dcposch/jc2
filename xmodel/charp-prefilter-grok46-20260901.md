# CHARP-PREFILTER — modular evidence for types (8,6,7) and (8,6,3)

Status: READY-TO-EXTRACT
Lane: systems/preparation
Date: 2026-09-01
Agent: grok-4.6
No CAS execution on this machine (trial division of three 10-digit primes only).

## Contents

0. Hash verification and prompt-digest note
1. Scope, non-claims, and campaign facts consumed
2. Fetched msolve syntax: characteristic is line 2; `-p` is precision
3. Exact logical value of each modular outcome (Hensel typed)
4. Dialect checklist
5. Rings, generators, primes, degeneration companions
6. Job files (templates and controls)
7. Interpreter `interpret_charp.py` (GROEBNER-mode)
8. Driver `run_charp_prefilter.sh`
9. Verdict rules (honest typing)
10. SHA-256 manifest
11. Braid job argument-dispatch: diagnostics and one-file fix spec
12. OPEN items and FALLACY-v2

## 0. Hash verification and prompt-digest note

Frozen copies hashed with `shasum -a 256` before they were read:

```text
c54d53f0a55586eb0fdd84d3aa311c6d64125a2cded8bec77aad1c3a8f40ec7f  .../msolve-prep-realization-grok46-20260831.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  .../block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

Item 2 matches the prompt. Item 1 does **not** match the boxed digest `64e451b44a421ca8efbd9d5fd553fd43cc2fb7afe6415ab760aab9ac47c27ef4`. That digest is the body hash of `xmodel/braid-prep-row64-grok46-20260831.md` (DIVERT log), a different file. The bytes at the charged *path* hash to `c54d53f0…`, matching the workspace copy, the DIVERT log of the named msolve-prep report, and `run.v2` `charged_input_1_sha256`. Path identity plus the launcher digest identify the named msolve-prep report; the boxed digest is a prompt transcription error. This lane proceeds on those frozen bytes. Canonical ledgers and `jc2-lean` were not inspected. No Gröbner/CAS was run here.

## 1. Scope, non-claims, and campaign facts consumed

Two timeout types, charged msolve-prep §§5–6:

| label | type | `Δ` | open characteristic ideal | open | `δ_aff` |
|---|---|---|---|---|---:|
| C | `(25;12,9;26)` | `(8,6,7)` | `I_25=(h_21,…,h_9)` plus `h_7 u−1` | `h_7≠0` | 9 |
| D | `(29;14,7;30)` | `(8,6,3)` | `I_29=(h_21,…,h_5)` plus `h_3 u−1` | `h_3≠0` | 7 |

Campaign facts consumed (coordinator LIVE STATE 2026-09-01T10:10Z / 14:28Z, not re-computed): `(8,6,11)` and `(8,6,9)` are NONEMPTY at the characteristic-ideal level (msolve GROEBNER proper bases of 138 and 345 elements). `(9,6,4)` and `(9,6,2)` are KILLED (both engines, unit ideal). C and D timed out at 3 h in characteristic 0 and are rerunning at 12 h caps. This prefilter is independent modular evidence; it does not wait for those caps.

Cover colon and `I_DP` postcheck are **out of scope**. msolve-prep §14.2: msolve files do not exclude covers. A modular EMPTY of the *open characteristic ideal* is already a statement about polynomial curves with the stated first remainder, cover or not. A modular NONEMPTY is not REALIZED.

`REPRESENTATIVE` is not `FULL_ACTUAL_EXIT`. This report asserts no exit price.

## 2. Fetched msolve syntax: characteristic is line 2; `-p` is precision

Fetched this lane (not executed):

- msolve 0.10.1 man page, https://www.mankier.com/1/msolve (July 2026 dump).
- Tutorial PDF https://msolve.lip6.fr/downloads/msolve-tutorial.pdf (476161 bytes, SHA-256 `de8ae1ad54e228b18af9c9123730077e1696638c3f52d677480ad7a258edb1cd`), §§1–2,5–6.
- README (raw GitHub `algebraic-solving/msolve` master).

**The prompt phrase “msolve `-p` syntax” does not set the prime.** Man page and tutorial §4: `-p`, `--precision` PRE is the bit precision of *real root isolation* (default 128). Characteristic is **not** a CLI flag.

Input format (README and tutorial §2):

1. variables, comma-separated, no trailing comma;
2. **field characteristic** (a prime `p < 2^31`, or `0`);
3. polynomials, comma-separated, no comma after the last; one occurrence of each monomial.

Tutorial §5 example of a prime-field Gröbner job:

```text
z1, z2, z3
1073741827
7*z1*z2+5*z2*z3+z3^2+z1+5*z3+10,
...
```

Command: `msolve -g 2 -f in.ms -o out.ms`. The printed header is `#field characteristic: 1073741827`. Unit ideal = `#length of basis: 1` and the list `[1]`. Proper basis = NONEMPTY over an algebraic closure of `F_p` (Nullstellensatz over a field).

Ceiling: `p < 2^31` (tutorial §1, README “Computing Groebner bases”). All three primes below satisfy this.

**Why not characteristic 0 with a CLI prime.** Campaign erratum (msolve 0.10.1): `-g 2` on char-0 input returns after the *first* modular F4 when that modular reduced GB is `{1}`, prints `#field characteristic: 0`, and never reconstructs a Q-cofactor. This prefilter puts `p` on line 2, so the engine is honestly computing over `F_p` and the header must match. A char-0 header on a prime-field input is `ENGINE-MISMATCH`, not EMPTY.

GROEBNER (`-g 2`) does not emit points. SOLVE-mode `[-1]` / `[1,nvars,-1,[]]` conventions are **not** used here (that mix-up is how the original suite misread `{1}` as `NONEMPTY_0DIM`).

## 3. Exact logical value of each modular outcome (Hensel typed)

Let `I ⊂ Q[x]` be the open characteristic ideal (`I_C` or `I_D`), `I_p` its reduction in `F_p[x]`. Integers `D` below are unknown a priori (a Q-membership certificate is exactly such a `D` plus cofactors).

**A. EMPTY over Q implies EMPTY mod almost all p.** If `1 ∈ I` over Q, write `D = Σ H_i f_i` with `D ∈ Z\{0}` and `H_i ∈ Z[x]`. Then `I_p = (1)` for every `p` not dividing `D`. Contrapositive: `I_p ≠ (1)` implies either `I ≠ (1)` over Q, or `p | D`.

**B. EMPTY mod one p does not imply EMPTY over Q.** Unlucky primes exist: `p` may divide a leading coefficient of a Gröbner basis of `I` over Q, so the reduced GB over `F_p` is not the reduction of a Q-basis. Typed `EMPTY-MOD-p`. Never a char-0 verdict.

**C. EMPTY mod three independent large primes.** The unlucky primes for a fixed `I` are finite. Three 31-bit primes all being unlucky is possible and is **not** excluded by a theorem in this lane. Typed `STRONG-EVIDENCE-EMPTY`. Never a Q-verdict; never `NON-REALIZABLE`. A reconstructed cofactor `1 = Σ h_i f_i` over Q would be a verdict; this bundle does not produce one.

**D. Degeneration-compatible EMPTY.** The closed ideals `I_C^{cl}=(h_21,…,h_9)` and `I_D^{cl}=(h_21,…,h_5)` (no Rabinowitsch, no `u`) are weighted-homogeneous in the charged (8,6) chart. For a positively graded homogeneous ideal, `1 ∈ I` iff a nonzero constant lies in `I`. If `I^{cl}_p = (1)` then emptiness is not an artifact of the affine chart `h_next ≠ 0`. Combined with (C) on *both* the closed cone and the open chart, type `STRONG-EVIDENCE-EMPTY` with tag `degeneration-compatible`. Still not a Q-verdict.

**E. NONEMPTY mod p, no smooth point.** Typed `MODULAR-NONEMPTY`. Does **not** prove char-0 nonempty: a constant content `D` of a Z-combination that writes a unit over Q can be divisible by a 31-bit prime (resultants of a 12-variable degree-4 system can have huge content). Three-prime `MODULAR-NONEMPTY` is `EVIDENCE-NONEMPTY`, not a verdict.

**F. Smooth modular point, Hensel hypotheses.** Let `f_1,…,f_c ∈ Z[x_1,…,x_n]` be the charged generators (including `h_next u−1` in the open case), `a ∈ Z^n`, `p` prime, `f_i(a) ≡ 0 (mod p)`.

*Complete-intersection form* (checkable). If `c ≤ n` and some `c×c` minor of the Jacobian `(∂f_i/∂x_j)(a)` is invertible in `F_p`, then by the multivariate Hensel lemma there is a lift `â ∈ Z_p^n` with `â ≡ a (mod p)` and `f_i(â)=0`. (Univariate prototype: Stacks Tag 03QD / Algebra 10.153.1, simple root of a monic; complete local rings are henselian, Tag 10.153.9. Multivariate Jacobian form: the same Newton iteration on a full-rank square block, free coordinates held fixed.) Then `I ≠ (1)` in `Q[x]`, hence `V(I)` is nonempty over `C` (Nullstellensatz). Typed `CHAR0-NONEMPTY` of the *characteristic ideal only*. Not REALIZED; not a nodal witness.

*General smooth form.* If `Spec Z[x]/I` is smooth over `Z` at the `F_p`-point (Jacobian criterion on a presentation, rank equal to embedding-codimension), maps from that smooth algebra into the henselian pair `(Z_p, p Z_p)` lift (Stacks Tag 0D49, Lemma 15.13.3). Same typed value. If the scheme is not a complete intersection, do not apply the minor test alone.

**G. Modular point without (F).** A point of `V(I_p)` that is singular, or whose Jacobian rank is not checked, does **not** lift in general (`x^2 − p = 0` has a double root at `0` mod `p` and no `Z_p`-root). Typed `MODULAR-POINT`, not `CHAR0-NONEMPTY`.

GROEBNER mode does not emit points. A Hensel probe needs a later SOLVE-mode parametrization over `F_p` (tutorial §6) plus a Jacobian check. That probe is specified as optional in the driver and is **OPEN** until run.

**H. TIMEOUT, NO_OUTPUT, ENGINE-MISMATCH.** Not mathematical evidence.

## 4. Dialect checklist

| # | Lesson | Repair here |
|---|---|---|
| 1 | No M2 reserved locals `pi`, `gamma`, `I`, `O` | No M2 in this bundle |
| 2 | No tower-ring `numgens` | No M2 |
| 3 | Coefficients from the source ring | Generators copied from charged msolve-prep, not re-derived |
| 4 | `diff` argument order | No `diff` |
| 5 | `first degree` | Unused |
| 6 | No underscore-subscript identifiers | Variables `B,C,D,E,F,G,b,gam,d,e,f,u` as charged |
| 7 | GROEBNER vs SOLVE | Interpreter reads `#length of basis` + unit-ideal test; refuses SOLVE tokens as a C/D verdict; requires `#field characteristic:` equal to the job prime |
| 8 | `sat()` wrapping | Ideal extracted; ring = line 1; positive control `1`; negative control `x`; A-control = charged `type86_A` reduced at the same `p` (must be NONEMPTY or that prime is aborted) |
| 9 | Variable/ring map | Line 1 order is the grevlex order; coefficient field `F_p`; image check = header characteristic |
| 10 | Prime label vs derivative | `p` is a field characteristic, not a differentiation mark |

FALLACY-v2 remaining items (flag/place, per-ray charge, pole/interior, merge-free, target index, raw remainder degree): unused. Floor/attainment: `STRONG-EVIDENCE-EMPTY` is a floor on suspicion, not attainment of Q-emptiness.

## 5. Rings, generators, primes, degeneration companions

Chart (charged msolve-prep §2.1): `p=t^8+B t^5+C t^4+D t^3+E t^2+F t+G`, `q=t^6+b t^4+gam t^3+d t^2+e t+f`. Ring `Q[B,C,D,E,F,G,b,gam,d,e,f]` plus Rabinowitsch `u`. Identically zero `h_23` omitted. Generators are the charged expansions; this lane does not re-expand.

Open jobs (msolve-prep §§5–6, characteristic line replaced):

- `I_C`: `(h_21,h_19,h_17,h_15,h_13,h_11,h_9, h_7 u−1)` in 12 variables.
- `I_D`: `(h_21,…,h_5, h_3 u−1)` in 12 variables.

Closed degeneration companions (weighted-homogeneous; no `u`):

- `I_C^{cl}=(h_21,…,h_9)` in 11 variables.
- `I_D^{cl}=(h_21,…,h_5)` in 11 variables.

Three primes, each `< 2^31`, none dividing an input coefficient (coefficients lie in `{1,2,3,4,6,12,24}`):

| id | prime | reason |
|---|---:|---|
| `p0` | `1073741827` | tutorial §5 example characteristic (`2^30+3`) |
| `p1` | `2147483629` | `2^31−19` |
| `p2` | `2147483647` | Mersenne `M_31=2^31−1` (Euler 1772) |

Primality of `p0` and `p1` checked by odd trial division up to `isqrt` (desk integer arithmetic, not a Gröbner engine). `p2` is classical.

## 6. Job files (templates and controls)

Coordinator extraction: fenced body = file bytes, UTF-8 POSIX text, one trailing newline. The driver substitutes `__PRIME__` on line 2. Do not ship a file whose second line is the token `__PRIME__` to msolve.

```type86_C.open.tpl
B,C,D,E,F,G,b,gam,d,e,f,u
__PRIME__
3*B-4*gam,
-12*b*gam+3*D-4*e,
-12*b^2*gam+6*B*C-12*b*e-12*gam*d+3*F,
-4*b^3*gam+B^3-12*b^2*e-24*b*gam*d-4*gam^3+6*B*E+6*C*D-12*gam*f-12*d*e,
-4*b^3*e-12*b^2*gam*d-4*b*gam^3+3*B^2*D+3*B*C^2-24*b*gam*f-24*b*d*e-12*gam^2*e-12*gam*d^2+6*B*G+6*C*F+6*D*E-12*e*f,
-12*b^2*gam*f-12*b^2*d*e-12*b*gam^2*e-12*b*gam*d^2-4*gam^3*d+3*B^2*F+6*B*C*E+3*B*D^2+3*C^2*D-24*b*e*f-24*gam*d*f-12*gam*e^2-12*d^2*e+6*D*G+6*E*F,
-12*b^2*e*f-24*b*gam*d*f-12*b*gam*e^2-12*b*d^2*e-4*gam^3*f-12*gam^2*d*e-4*gam*d^3+6*B*C*G+6*B*D*F+3*B*E^2+3*C^2*F+6*C*D*E+D^3-12*gam*f^2-24*d*e*f-4*e^3+6*F*G,
-12*b*gam*f^2*u-24*b*d*e*f*u-4*b*e^3*u-12*gam^2*e*f*u-12*gam*d^2*f*u-12*gam*d*e^2*u-4*d^3*e*u+6*B*E*G*u+3*B*F^2*u+6*C*D*G*u+6*C*E*F*u+3*D^2*F*u+3*D*E^2*u-12*e*f^2*u-1
```

```type86_C.closed.tpl
B,C,D,E,F,G,b,gam,d,e,f
__PRIME__
3*B-4*gam,
-12*b*gam+3*D-4*e,
-12*b^2*gam+6*B*C-12*b*e-12*gam*d+3*F,
-4*b^3*gam+B^3-12*b^2*e-24*b*gam*d-4*gam^3+6*B*E+6*C*D-12*gam*f-12*d*e,
-4*b^3*e-12*b^2*gam*d-4*b*gam^3+3*B^2*D+3*B*C^2-24*b*gam*f-24*b*d*e-12*gam^2*e-12*gam*d^2+6*B*G+6*C*F+6*D*E-12*e*f,
-12*b^2*gam*f-12*b^2*d*e-12*b*gam^2*e-12*b*gam*d^2-4*gam^3*d+3*B^2*F+6*B*C*E+3*B*D^2+3*C^2*D-24*b*e*f-24*gam*d*f-12*gam*e^2-12*d^2*e+6*D*G+6*E*F,
-12*b^2*e*f-24*b*gam*d*f-12*b*gam*e^2-12*b*d^2*e-4*gam^3*f-12*gam^2*d*e-4*gam*d^3+6*B*C*G+6*B*D*F+3*B*E^2+3*C^2*F+6*C*D*E+D^3-12*gam*f^2-24*d*e*f-4*e^3+6*F*G
```

```type86_D.open.tpl
B,C,D,E,F,G,b,gam,d,e,f,u
__PRIME__
3*B-4*gam,
-12*b*gam+3*D-4*e,
-12*b^2*gam+6*B*C-12*b*e-12*gam*d+3*F,
-4*b^3*gam+B^3-12*b^2*e-24*b*gam*d-4*gam^3+6*B*E+6*C*D-12*gam*f-12*d*e,
-4*b^3*e-12*b^2*gam*d-4*b*gam^3+3*B^2*D+3*B*C^2-24*b*gam*f-24*b*d*e-12*gam^2*e-12*gam*d^2+6*B*G+6*C*F+6*D*E-12*e*f,
-12*b^2*gam*f-12*b^2*d*e-12*b*gam^2*e-12*b*gam*d^2-4*gam^3*d+3*B^2*F+6*B*C*E+3*B*D^2+3*C^2*D-24*b*e*f-24*gam*d*f-12*gam*e^2-12*d^2*e+6*D*G+6*E*F,
-12*b^2*e*f-24*b*gam*d*f-12*b*gam*e^2-12*b*d^2*e-4*gam^3*f-12*gam^2*d*e-4*gam*d^3+6*B*C*G+6*B*D*F+3*B*E^2+3*C^2*F+6*C*D*E+D^3-12*gam*f^2-24*d*e*f-4*e^3+6*F*G,
-12*b*gam*f^2-24*b*d*e*f-4*b*e^3-12*gam^2*e*f-12*gam*d^2*f-12*gam*d*e^2-4*d^3*e+6*B*E*G+3*B*F^2+6*C*D*G+6*C*E*F+3*D^2*F+3*D*E^2-12*e*f^2,
-12*b*e*f^2-12*gam*d*f^2-12*gam*e^2*f-12*d^2*e*f-4*d*e^3+3*B*G^2+6*C*F*G+6*D*E*G+3*D*F^2+3*E^2*F,
-4*gam*f^3*u-12*d*e*f^2*u-4*e^3*f*u+3*D*G^2*u+6*E*F*G*u+F^3*u-1
```

```type86_D.closed.tpl
B,C,D,E,F,G,b,gam,d,e,f
__PRIME__
3*B-4*gam,
-12*b*gam+3*D-4*e,
-12*b^2*gam+6*B*C-12*b*e-12*gam*d+3*F,
-4*b^3*gam+B^3-12*b^2*e-24*b*gam*d-4*gam^3+6*B*E+6*C*D-12*gam*f-12*d*e,
-4*b^3*e-12*b^2*gam*d-4*b*gam^3+3*B^2*D+3*B*C^2-24*b*gam*f-24*b*d*e-12*gam^2*e-12*gam*d^2+6*B*G+6*C*F+6*D*E-12*e*f,
-12*b^2*gam*f-12*b^2*d*e-12*b*gam^2*e-12*b*gam*d^2-4*gam^3*d+3*B^2*F+6*B*C*E+3*B*D^2+3*C^2*D-24*b*e*f-24*gam*d*f-12*gam*e^2-12*d^2*e+6*D*G+6*E*F,
-12*b^2*e*f-24*b*gam*d*f-12*b*gam*e^2-12*b*d^2*e-4*gam^3*f-12*gam^2*d*e-4*gam*d^3+6*B*C*G+6*B*D*F+3*B*E^2+3*C^2*F+6*C*D*E+D^3-12*gam*f^2-24*d*e*f-4*e^3+6*F*G,
-12*b*gam*f^2-24*b*d*e*f-4*b*e^3-12*gam^2*e*f-12*gam*d^2*f-12*gam*d*e^2-4*d^3*e+6*B*E*G+3*B*F^2+6*C*D*G+6*C*E*F+3*D^2*F+3*D*E^2-12*e*f^2,
-12*b*e*f^2-12*gam*d*f^2-12*gam*e^2*f-12*d^2*e*f-4*d*e^3+3*B*G^2+6*C*F*G+6*D*E*G+3*D*F^2+3*E^2*F
```

A-control (charged `type86_A.ms` generators; expected NONEMPTY at each `p`):

```type86_A.open.tpl
B,C,D,E,F,G,b,gam,d,e,f,u
__PRIME__
3*B-4*gam,
-12*b*gam+3*D-4*e,
-12*b^2*gam+6*B*C-12*b*e-12*gam*d+3*F,
-4*b^3*gam+B^3-12*b^2*e-24*b*gam*d-4*gam^3+6*B*E+6*C*D-12*gam*f-12*d*e,
-4*b^3*e-12*b^2*gam*d-4*b*gam^3+3*B^2*D+3*B*C^2-24*b*gam*f-24*b*d*e-12*gam^2*e-12*gam*d^2+6*B*G+6*C*F+6*D*E-12*e*f,
-12*b^2*gam*f*u-12*b^2*d*e*u-12*b*gam^2*e*u-12*b*gam*d^2*u-4*gam^3*d*u+3*B^2*F*u+6*B*C*E*u+3*B*D^2*u+3*C^2*D*u-24*b*e*f*u-24*gam*d*f*u-12*gam*e^2*u-12*d^2*e*u+6*D*G*u+6*E*F*u-1
```

Tiny controls (no `__PRIME__` substitution except line 2):

```control_unit.tpl
x
__PRIME__
1
```

```control_linear.tpl
x
__PRIME__
x
```

Expected: `control_unit` → GROEBNER `EMPTY` (basis `{1}`); `control_linear` → `NONEMPTY_GB`; `type86_A` → `NONEMPTY_GB`. FAIL of a tiny control aborts the suite. EMPTY of the A-control at a prime **aborts that prime** (unlucky or toolchain), and C/D EMPTY at that prime is not counted toward `STRONG-EVIDENCE-EMPTY`.

## 7. Interpreter `interpret_charp.py` (GROEBNER-mode)

```interpret_charp.py
#!/usr/bin/env python3
"""Classify msolve GROEBNER-mode output over a declared prime.

Unit ideal (EMPTY variety over an algebraic closure of F_p): printed basis
exactly the constant 1. Proper basis: NONEMPTY_GB. Require the header
'#field characteristic: P' to equal the job prime. A characteristic-0
header on prime-field input is ENGINE-MISMATCH, not EMPTY.

SOLVE-mode tokens ([-1], [1, nvars, -1, []]) are not C/D verdicts.
"""
from __future__ import print_function
import argparse, os, re, sys

def read(path):
    with open(path, "r") as handle:
        return handle.read()

def groebner_unit_ideal(body):
    lines = [ln for ln in body.splitlines() if not ln.lstrip().startswith("#")]
    blob = "\n".join(lines).strip().rstrip(":").strip()
    if not (blob.startswith("[") and blob.endswith("]")):
        return False
    inner = blob[1:-1].strip()
    return re.fullmatch(r"[+\-]?1", inner) is not None

def classify(text, expect_p):
    char_hits = re.findall(r"field characteristic:\s*(\d+)", text)
    char_p = int(char_hits[-1]) if char_hits else None
    if expect_p is not None and char_p is not None and char_p != expect_p:
        return ("ENGINE-MISMATCH", "GROEBNER",
                "header characteristic %s != job prime %s" % (char_p, expect_p))
    if expect_p is not None and char_p == 0:
        return ("ENGINE-MISMATCH", "GROEBNER",
                "characteristic-0 header on prime-field input")
    if re.search(r"Reduced Groebner basis|length of basis:|Leading ideal", text):
        match = re.search(r"length of basis:\s*(\d+)", text)
        length = int(match.group(1)) if match else None
        if length == 1 and groebner_unit_ideal(text):
            return "EMPTY", "GROEBNER", "basis={1} unit ideal"
        if length is None:
            return "UNRECOGNIZED", "GROEBNER", "missing length of basis"
        if length == 0:
            return "UNRECOGNIZED", "GROEBNER", "length 0"
        return "NONEMPTY_GB", "GROEBNER", "proper basis length=%d" % length
    body = "\n".join(ln for ln in text.splitlines()
                     if not ln.lstrip().startswith("#")).strip()
    if re.match(r"\[-1\]", body):
        return "SOLVE-EMPTY-TOKEN", "SOLVE", "[-1] (not a GROEBNER verdict)"
    if not body:
        return "NO_OUTPUT", "UNKNOWN", "empty file"
    return "UNRECOGNIZED", "UNKNOWN", "first tokens: %r" % body[:80]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output")
    parser.add_argument("--prime", type=int, required=True)
    args = parser.parse_args()
    if not os.path.isfile(args.output):
        print("NO_OUTPUT\tUNKNOWN\tmissing file", file=sys.stderr)
        sys.exit(3)
    kind, mode, note = classify(read(args.output), args.prime)
    print("%s\t%s\t%s" % (kind, mode, note))
    if kind in ("UNRECOGNIZED", "NO_OUTPUT", "ENGINE-MISMATCH", "SOLVE-EMPTY-TOKEN"):
        sys.exit(3)
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

## 8. Driver `run_charp_prefilter.sh`

AWS-only (`CHARP_AWS=1`). Instantiates templates, runs `msolve -v 2 -g 2 -t "$THREADS"` (default 8). Cap default 1800 s per job (modular; the 12 h caps belong to the char-0 reruns). TIMEOUT is recorded, never read as EMPTY. Optional `CHARP_LIFT=1` re-runs a 0-dimensional NONEMPTY job without `-g` for a parametrization; Jacobian/Hensel remains OPEN (no point parser in this bundle).

```run_charp_prefilter.sh
#!/usr/bin/env bash
# run_charp_prefilter.sh
# Modular GROEBNER prefilter for I_C, I_D at three primes.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
LOG="$ROOT/logs"
mkdir -p "$LOG" "$ROOT/instantiated"
SUMMARY="$LOG/summary.tsv"
echo -e "job\tprime\tstatus\tseconds\tnote" > "$SUMMARY"

if [[ "${CHARP_AWS:-0}" != "1" ]]; then
  echo "Refusing to run: set CHARP_AWS=1 on the AWS box." >&2
  exit 2
fi
command -v msolve >/dev/null 2>&1 || { echo "msolve missing" >&2; exit 2; }
command -v python3 >/dev/null 2>&1 || { echo "python3 missing" >&2; exit 2; }

PRIMES=(1073741827 2147483629 2147483647)
THREADS="${THREADS:-8}"
CAP="${CAP:-1800}"

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

instantiate() {
  local tpl="$1" prime="$2" dest="$3"
  sed "s/^__PRIME__$/${prime}/" "$ROOT/$tpl" > "$dest"
  grep -q "^${prime}$" "$dest" || { echo "prime substitution failed: $dest" >&2; exit 2; }
}

record() { echo -e "$1\t$2\t$3\t$4\t$5" | tee -a "$SUMMARY"; }

run_job() {
  local job="$1" prime="$2" tpl="$3" expect="$4"
  local inst="$ROOT/instantiated/${job}.p${prime}.ms"
  local out="$LOG/${job}.p${prime}.msolve.out"
  instantiate "$tpl" "$prime" "$inst"
  local start end rc secs note
  start=$(date +%s)
  set +e
  run_timeout "$CAP" msolve -v 2 -g 2 -t "$THREADS" -f "$inst" -o "$out" \
    > "$LOG/${job}.p${prime}.stdout" 2> "$LOG/${job}.p${prime}.stderr"
  rc=$?
  set -e
  end=$(date +%s)
  secs=$((end-start))
  echo "$rc" > "$LOG/${job}.p${prime}.rc"
  if [[ $rc -eq 124 || $rc -eq 137 ]]; then
    record "$job" "$prime" TIMEOUT "$secs" "cap ${CAP}s"
    return 0
  fi
  set +e
  note=$(python3 "$ROOT/interpret_charp.py" --prime "$prime" "$out" 2>"$LOG/${job}.p${prime}.interp.err")
  local irc=$?
  set -e
  if [[ $irc -ne 0 ]]; then
    record "$job" "$prime" FAIL "$secs" "${note:-interpreter rc=$irc}"
    if [[ "$expect" != "advisory" ]]; then
      echo "ABORT: $job p=$prime failed control/interp" >&2
      exit 1
    fi
    return 0
  fi
  local kind="${note%%$'\t'*}"
  if [[ -n "$expect" && "$expect" != "advisory" && "$kind" != "$expect" ]]; then
    record "$job" "$prime" FAIL "$secs" "got $kind want $expect ($note)"
    echo "ABORT: $job p=$prime expected $expect" >&2
    exit 1
  fi
  record "$job" "$prime" "$kind" "$secs" "$note"
}

echo "=== CONTROLS ==="
for P in "${PRIMES[@]}"; do
  run_job control_unit "$P" control_unit.tpl EMPTY
  run_job control_linear "$P" control_linear.tpl NONEMPTY_GB
  run_job type86_A "$P" type86_A.open.tpl NONEMPTY_GB
done

echo "=== C/D OPEN + CLOSED ==="
for P in "${PRIMES[@]}"; do
  run_job type86_C_open "$P" type86_C.open.tpl advisory
  run_job type86_C_closed "$P" type86_C.closed.tpl advisory
  run_job type86_D_open "$P" type86_D.open.tpl advisory
  run_job type86_D_closed "$P" type86_D.closed.tpl advisory
done

echo "=== SUMMARY ==="
column -t -s $'\t' "$SUMMARY" || cat "$SUMMARY"
echo
echo "Typing: see the CHARP-PREFILTER report §9. EMPTY at one prime is EMPTY-MOD-p."
echo "EMPTY at all three primes on an open job is STRONG-EVIDENCE-EMPTY, never a Q-verdict."
echo "Closed EMPTY at all three plus open EMPTY is degeneration-compatible STRONG-EVIDENCE-EMPTY."
```

Launch: extract fences into one directory; `chmod +x run_charp_prefilter.sh interpret_charp.py`; on the AWS box, `CHARP_AWS=1 ./run_charp_prefilter.sh`. Re-hash against §10 before launch.

## 9. Verdict rules (honest typing)

Per job, after a successful GROEBNER run whose header prime matches:

| engine output | typed value |
|---|---|
| basis `{1}` | `EMPTY-MOD-p` |
| proper basis | `MODULAR-NONEMPTY` |
| TIMEOUT / NO_OUTPUT / ENGINE-MISMATCH | no mathematical content |

Per type (`I_C` or `I_D`), after three primes (A-control NONEMPTY at each counted prime):

| pattern | typed value |
|---|---|
| `EMPTY-MOD-p` at all three, open job | `STRONG-EVIDENCE-EMPTY` — **never** a char-0 EMPTY verdict, **never** `NON-REALIZABLE` |
| plus closed job also `EMPTY-MOD-p` at all three | same, tag `degeneration-compatible` |
| `MODULAR-NONEMPTY` at one or more primes | `EVIDENCE-NONEMPTY`; char-0 nonempty of the characteristic ideal is **not** proved |
| smooth `F_p`-point with a full-rank Jacobian minor (Hensel §3.F), after a later SOLVE-mode probe | `CHAR0-NONEMPTY` of the characteristic ideal only; not REALIZED |
| mixed EMPTY / NONEMPTY across primes | `MIXED-REDUCTION` — do not promote either direction; possible unlucky prime on the EMPTY side |
| any TIMEOUT among the three | `UNDECIDED` |

A single-prime EMPTY is not `STRONG-EVIDENCE-EMPTY`. Char-0 NONEMPTY of a characteristic ideal is not a nodal realization and is not `FULL_ACTUAL_EXIT`.

## 10. SHA-256 manifest

Hashes of extracted fence bodies (UTF-8, one trailing newline), computed on this machine after the fences were written:

| file | bytes | SHA-256 |
|---|---:|---|
| `type86_C.open.tpl` | 765 | `e96ee5d6e079bd192af711327deb67c68a47e1e21adc003686ae96f8ea7f48f7` |
| `type86_C.closed.tpl` | 595 | `0c56a7ccadc80ef461bb6099458f85dd1d366c49d337925366184a385f3e20cc` |
| `type86_D.open.tpl` | 898 | `5c58709aa8e0c214b3803e34b33227fe8f5c0c57c6c634f059340f54e840859e` |
| `type86_D.closed.tpl` | 831 | `bc23d6ae206331c3ea0ede98091378f16e590fa1f226e3d1aba65353943fa2d2` |
| `type86_A.open.tpl` | 470 | `7c1a57dadb344e27726adee6f7e3c0930e533947c230a88672750df57024be05` |
| `control_unit.tpl` | 14 | `0cc7d42fc5424d83e557ed03d25b8fbe40cb22a7922bbd9a5e7e960d649c2a0e` |
| `control_linear.tpl` | 14 | `f63846acbd73ffefcf9109c7933c609e3dde055df8009ff16b7145519b5db0a9` |
| `interpret_charp.py` | 2947 | `06c1960a5c5b6f2d283e18fad3f3f35d332262b179388a785886e8fba9d50c9d` |
| `run_charp_prefilter.sh` | 3445 | `42add88f80515059cef7fbc263d30e23f5c661ee45e4ea287d67699b90757d68` |

Fetched literature:

```text
de8ae1ad54e228b18af9c9123730077e1696638c3f52d677480ad7a258edb1cd  msolve-tutorial.pdf (476161 bytes)
```

Man page and README were fetched as HTML/text; they are not job bodies.

## 11. Braid job argument-dispatch: diagnostics and one-file fix spec

This lane cannot read Box03 `driver.log` / `*.meta`. Coordinator LIVE STATE 2026-09-01T04:06Z: sage monodromy stage exited in 1 s with no output; selftest JSON present; typed `OPEN[BRAID-JOB-DISPATCH]`. Spec only.

**Why the generated driver is ill-posed.** `run_braid_job.sh` calls `sage "$SAGE_SCRIPT" precheck` and `sage "$SAGE_SCRIPT" monodromy`. Sage 10.8 CLI (fetched https://doc.sagemath.org/html/en/reference/repl/options.html):

```text
usage: sage [...] [file ...]
positional arguments:
  file    execute the given file as sage code
```

A second positional is another *file to execute*, not `sys.argv` of the first file. Shebang invocation `./a.sage 42` can pass a positional (Sage issue 41908, 2026-03-28); the driver’s `sage script.sage MODE` path is the documented multi-file CLI. Independently, `braid_monodromy_row64.sage` does `mode = argv[0] if argv else "precheck"`: an empty argv silently runs precheck and exits 0 in about a second — matching the 1 s empty monodromy stage.

**Diagnostic steps on the box (coordinator):**

1. `cat $BRAID_JOB_OUT/driver.log` — confirm `START precheck cmd=…` and `START monodromy cmd=…` and their `rc=`.
2. `cat $BRAID_JOB_OUT/precheck.stderr $BRAID_JOB_OUT/monodromy.stderr` — look for `usage: sage`, `unrecognized arguments`, `No such file: monodromy`, `No such file: precheck`.
3. `cat $BRAID_JOB_OUT/precheck.stdout $BRAID_JOB_OUT/monodromy.stdout` — look for `mode=precheck` vs `mode=monodromy`. `mode=precheck` inside the monodromy stage is the silent default.
4. `cat $BRAID_JOB_OUT/monodromy.meta` — `exit_status`, `output_sha256` of an empty stdout.
5. Probe, not a math job: `sage -c 'print(1)'` vs `sage /path/braid_monodromy_row64.sage monodromy` vs `./braid_monodromy_row64.sage monodromy` (shebang). Record which path prints `mode=monodromy`.
6. Do not treat a precheck JSON written during the monodromy stage as SIROCCO output.

**One-file fix spec (`run_braid_job.sh` only).** Stop passing a second positional to `sage`. The sage script selects mode from `sys.argv` and defaults to precheck if argv is empty; `BRAID_JOB_RUN_MONODROMY` is consulted only after mode is already `monodromy`. Replace both sage `run_capped` lines by `sage -c`/`load` with an explicit argv (no extra file operand):

```text
run_capped precheck "$PRECHECK_WALL" sage -q -c \
  "import os,sys; sys.argv=['braid_monodromy_row64.sage','precheck']; load(os.environ['BRAID_JOB_ROOT']+'/braid_monodromy_row64.sage')"
export BRAID_JOB_RUN_MONODROMY=1
run_capped monodromy "$WALL_SECONDS" sage -q -c \
  "import os,sys; sys.argv=['braid_monodromy_row64.sage','monodromy']; load(os.environ['BRAID_JOB_ROOT']+'/braid_monodromy_row64.sage')"
```

Add in `run_capped` after launch: refuse rc=0 with empty stdout (`[[ ! -s $stdout_path ]] && die "$name produced empty stdout"`). That guard would have caught the 1 s empty monodromy stage.

Do not implement the fix in this lane (one report, no other file). Cross-check only; deprioritized as charged.

## 12. OPEN items and FALLACY-v2

1. Hensel probe (SOLVE-mode parametrization + Jacobian minor) is specified, not implemented. Without it, `MODULAR-NONEMPTY` does not upgrade to `CHAR0-NONEMPTY`.
2. Cover colon remains M2-side (charged §14.2). Modular EMPTY of the open characteristic ideal does not mention covers; modular NONEMPTY may include cover points.
3. Three-prime EMPTY is not a Nullstellensatz certificate over Q.
4. Closed-job EMPTY is the degeneration-compatible tag, not a separate theorem.
5. Braid dispatch logs were not read; §11 is a spec.
6. Char-0 12 h reruns of C/D are independent; this prefilter does not consume them.

This report does not declare an exit price.

Launch recipe: extract the nine fenced files; `chmod +x run_charp_prefilter.sh interpret_charp.py`; `CHARP_AWS=1 ./run_charp_prefilter.sh`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `29427`.
- Body SHA-256:
  `b8cb249f2fe5c11c243b7760f130d193d8986703dc1247e68ef930981b37c1b4`.
- Frozen basis: `2c562c110706b732ae8da663c57891768aede3b3`.
