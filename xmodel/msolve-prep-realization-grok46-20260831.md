# MSOLVE-PREP — job files for the six realization ideals

Status: READY-TO-EXTRACT
Lane: systems/preparation
Date: 2026-08-31
Charged inputs:
- `xmodel/nodal-realization-86-96-grok46-20260831.md` (frozen copy; SHA-256 verified below)
- `xmodel/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md` (frozen copy; SHA-256 verified below)

## 0. Hash verification and campaign constraints

Frozen copies were hashed before they were read. Both match the charge exactly:

```text
3985fbedea72315c0ff3ffd4185de465ba16922bca872623fe2f02fe34cffc08
  .../inputs/nodal-realization-86-96-grok46-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286
  .../inputs/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Campaign constraints observed: this lane did **not** run msolve, Macaulay2, Gröbner bases, or any other CAS of uncertain duration. The six realization jobs and both controls are written as ready-to-run inputs for an AWS box. Coefficient polynomials were obtained by finite binomial expansion of `(t^d + lower)^k` with like-term collection and weighted-degree checks (desk-scale, duration < 1 s, no Gröbner). Canonical ledgers and `jc2-lean` were not inspected. This report does not assert an exit price.

msolve input syntax is taken from the public msolve README (first line: comma-separated variables, no trailing comma; second line: characteristic `0`; then expanded polynomials, comma-separated, no comma after the last; one occurrence of each monomial). Primary literature already hashed in the charged NODAL-REALIZATION §10 is not re-fetched. The `(6,4,3)` positive-control witness is the explicit curve of ROW-SWEEP §2, which the charged report names as the control; that parametrization is copied as a cited formula, not re-derived.

## 1. Scope, policy, and extraction discipline

Six finite jobs, matching charged NODAL-REALIZATION §§2–7:

| job | type | `Δ` | ideal | open | `δ_aff` | cap |
|---|---|---|---|---|---:|---:|
| `type86_A` | `(21;10,11;22)` | `(8,6,11)` | `I_21` | `h_11≠0` | 11 | 7200 s |
| `type86_B` | `(23;11,10;24)` | `(8,6,9)` | `I_23` | `h_9≠0` | 10 | 7200 s |
| `type86_C` | `(25;12,9;26)` | `(8,6,7)` | `I_25` | `h_7≠0` | 9 | 10800 s |
| `type86_D` | `(29;14,7;30)` | `(8,6,3)` | `I_29` | `h_3≠0` | 7 | 7200 s |
| `type96_A` | `(23;22,6;25)` | `(9,6,4)` | `I_(9,6,4)` | `k_4≠0` | 6 | 14400 s |
| `type96_B` | `(25;24,4;27)` | `(9,6,2)` | `I_(9,6,2)` | `k_2≠0` | 4 | 14400 s |

Caps are wall-clock suggestions from the charged size notes (complete-intersection-like, 9–12 variables, degree 3–4) against the FSY 2006 hours-scale 11-var/17-poly run. They are not runtime predictions.

Coordinator extraction: every deliverable is a fenced block whose info-string is the filename. File bytes = UTF-8 of the fence body, POSIX text, exactly one trailing newline. Re-hash after extraction; compare to §13.

Discipline (charged §0 / FALLACY `sat()`): extract the ideal, assert its ring, never call `saturate()`. Open conditions use a Rabinowitsch inverse variable. Cover loci use an explicit colon loop `I : J` until stable, with a ring assert at each pass. Resultant `Res(p',q')` is computed *inside* M2 (not expanded here) and inverted by a second variable `v`.

msolve files encode only the characteristic generators plus `h_next·u−1` (or `k_next·u−1`). They do **not** adjoin cover-slack variables: a linear combination `∑ w_i g_i − 1` with extra free `w_i` makes a 0-dimensional coefficient point positive-dimensional in the solver variables. Cover exclusion is therefore M2-side (colon) plus the `I_DP` post-check. Flagged in §14.

Launch: copy the fenced files into one directory on the AWS box and run `REALIZATION_AWS=1 ./run_realization_suite.sh`. This lane did not run that script.

## 2. Shared notation, rings, and encoding of open conditions

### 2.1 (8,6) chart

Charged residual, `gam` for `γ`:

```text
p = t^8 + B t^5 + C t^4 + D t^3 + E t^2 + F t + G
q = t^6 + b t^4 + gam t^3 + d t^2 + e t + f
```

Ring `R0=ℚ[B,C,D,E,F,G,b,gam,d,e,f]` (11 vars). Weights: `B↦3,C↦4,D↦5,E↦6,F↦7,G↦8,b↦2,gam↦3,d↦4,e↦5,f↦6`, so `p` (resp. `q`) is weighted-homogeneous of degree 8 (resp. 6). Optional gauges `f=0` and `gam=1` (on `gam≠0`) are **not** imposed; they are a case-split, not the charged ring.

Binomial split, `p_low=p−t^8` (deg ≤5), `q_low=q−t^6` (deg ≤4):

```text
p^3 = t^{24} + 3 t^{16} p_low + 3 t^8 p_low^2 + p_low^3
q^4 = t^{24} + 4 t^{18} q_low + 6 t^{12} q_low^2 + 4 t^6 q_low^3 + q_low^4
H = p^3 − q^4
```

Degree supports (intermediate check): `p_low` 0..5; `p_low^2` 0..10; `p_low^3` 0..15; `q_low` 0..4; `q_low^2` 0..8; `q_low^3` 0..12; `q_low^4` 0..16. Piece ranges: `3 t^{16} p_low` 16..21; `3 t^8 p_low^2` 8..18; `p_low^3` 0..15; `−4 t^{18} q_low` 18..22; `−6 t^{12} q_low^2` 12..20; `−4 t^6 q_low^3` 6..18; `−q_low^4` 0..16. Hence `H` has support `0..22` and **`h_23≡0`** in this chart (the charged `h_23=−4a_5` already killed `a_5`). Each `h_k` is weighted-homogeneous of degree `24−k` (all 23 nonzero coefficients checked).

Hand identities used as sanity: `h_22=−4b`, `h_21=3B−4gam`, `h_20=−6b^2+3C−4d`, `h_19=−12b·gam+3D−4e`. These recover the charged even-slice relations `B=4gam/3` etc. when even Tschirnhausen is imposed.

Odd coefficients, fully expanded (`gam` for `γ`):

```text
h_23 = 0
h_21 = 3*B-4*gam
h_19 = -12*b*gam+3*D-4*e
h_17 = -12*b^2*gam+6*B*C-12*b*e-12*gam*d+3*F
h_15 = -4*b^3*gam+B^3-12*b^2*e-24*b*gam*d-4*gam^3+6*B*E+6*C*D-12*gam*f-12*d*e
h_13 = -4*b^3*e-12*b^2*gam*d-4*b*gam^3+3*B^2*D+3*B*C^2-24*b*gam*f-24*b*d*e-12*gam^2*e-12*gam*d^2+6*B*G+6*C*F+6*D*E-12*e*f
h_11 = -12*b^2*gam*f-12*b^2*d*e-12*b*gam^2*e-12*b*gam*d^2-4*gam^3*d+3*B^2*F+6*B*C*E+3*B*D^2+3*C^2*D-24*b*e*f-24*gam*d*f-12*gam*e^2-12*d^2*e+6*D*G+6*E*F
h_9  = -12*b^2*e*f-24*b*gam*d*f-12*b*gam*e^2-12*b*d^2*e-4*gam^3*f-12*gam^2*d*e-4*gam*d^3+6*B*C*G+6*B*D*F+3*B*E^2+3*C^2*F+6*C*D*E+D^3-12*gam*f^2-24*d*e*f-4*e^3+6*F*G
h_7  = -12*b*gam*f^2-24*b*d*e*f-4*b*e^3-12*gam^2*e*f-12*gam*d^2*f-12*gam*d*e^2-4*d^3*e+6*B*E*G+3*B*F^2+6*C*D*G+6*C*E*F+3*D^2*F+3*D*E^2-12*e*f^2
h_5  = -12*b*e*f^2-12*gam*d*f^2-12*gam*e^2*f-12*d^2*e*f-4*d*e^3+3*B*G^2+6*C*F*G+6*D*E*G+3*D*F^2+3*E^2*F
h_3  = -4*gam*f^3-12*d*e*f^2-4*e^3*f+3*D*G^2+6*E*F*G+F^3
```

Term counts: `h_21:2`, `h_19:3`, `h_17:5`, `h_15:9`, `h_13:13`, `h_11:15`, `h_9:17`, `h_7:14`, `h_5:10`, `h_3:6`. In-chart gcd-2 cover (even functions in this Tschirnhausen chart): `V(B,D,F,gam,e)`.

### 2.2 (9,6) chart

Charged residual with `P0=c=0`:

```text
p = t^9 + A t^7 + P6 t^6 + B t^5 + P4 t^4 + C t^3 + P2 t^2 + D t
q = t^6 + a t^4 + Q3 t^3 + b t^2 + Q1 t
```

Ring `R0=ℚ[A,P6,B,P4,C,P2,D,a,Q3,b,Q1]`. Weights: `A↦2,P6↦3,B↦4,P4↦5,C↦6,P2↦7,D↦8,a↦2,Q3↦3,b↦4,Q1↦5`. Split `p_low=p−t^9` (deg ≤7, no `t^8`), `q_low=q−t^6` (deg ≤4, no `t^5`):

```text
p^2 = t^{18} + 2 t^9 p_low + p_low^2
q^3 = t^{18} + 3 t^{12} q_low + 3 t^6 q_low^2 + q_low^3
K = p^2 − q^3
```

Supports: `p_low` 1..7; `p_low^2` 2..14; `q_low` 1..4; `q_low^2` 2..8; `q_low^3` 3..12. Pieces: `2 t^9 p_low` 10..16; `p_low^2` 2..14; `−3 t^{12} q_low` 13..16; `−3 t^6 q_low^2` 8..14; `−q_low^3` 3..12. Hence `K` has support `2..16` and **`k_17≡0`** (charged `k_17=−3α` already killed `α`). Each `k_i` is weighted-homogeneous of degree `18−i`.

```text
k_17 = 0
k_16 = 2*A-3*a
k_15 = 2*P6-3*Q3
k_14 = A^2-3*a^2+2*B-3*b
k_13 = 2*A*P6-6*a*Q3+2*P4-3*Q1
k_12 = -a^3+2*A*B+P6^2-6*a*b-3*Q3^2+2*C
k_11 = -3*a^2*Q3+2*A*P4+2*P6*B-6*a*Q1-6*Q3*b+2*P2
k_10 = -3*a^2*b-3*a*Q3^2+2*A*C+2*P6*P4+B^2-6*Q3*Q1-3*b^2+2*D
k_9  = -3*a^2*Q1-6*a*Q3*b-Q3^3+2*A*P2+2*P6*C+2*B*P4-6*b*Q1
k_8  = -6*a*Q3*Q1-3*a*b^2-3*Q3^2*b+2*A*D+2*P6*P2+2*B*C+P4^2-3*Q1^2
k_7  = -6*a*b*Q1-3*Q3^2*Q1-3*Q3*b^2+2*P6*D+2*B*P2+2*P4*C
k_6  = -3*a*Q1^2-6*Q3*b*Q1-b^3+2*B*D+2*P4*P2+C^2
k_5  = -3*Q3*Q1^2-3*b^2*Q1+2*P4*D+2*C*P2
k_4  = -3*b*Q1^2+2*C*D+P2^2
k_3  = -Q1^3+2*P2*D
k_2  = D^2
```

Sanity: `k_16=2A−3a` recovers the charged even-odd relation `A=3a/2`. Even-odd cover in this chart: `V(P6,P4,P2,Q3,Q1)`.

### 2.3 Verdict rules (used in every type)

On the AWS output of the open+immersive+colon ideal:

- **EMPTY** (`msolve [-1]`, or M2 `I=⟨1⟩`): no polynomial curve in this chart with the stated first remainder. Type is **NON-REALIZABLE as a polynomial curve**, hence as a nodal residual. (Does not decide one-place Galindo curves of positive genus.)
- **NONEMPTY**: not yet REALIZED. Extract a closed point, build `(p,q)`, run `idp_postcheck.m2` with `N=δ_aff`. REALIZED iff some point has reduced `I_DP` of length `N`, immersive, distinct tangents, no reused parameter. NON-REALIZABLE iff every component fails that test (non-reduced, triple fibre, cover, or coincident tangents).

`REPRESENTATIVE` is not `FULL_ACTUAL_EXIT`. A nonempty characteristic locus is not a nodal witness.

## 3. Type (8,6)-A — (21; 10, 11; 22), Δ=(8,6,11)

Charged `I_21=(h_23,h_21,h_19,h_17,h_15,h_13)`, open `h_11≠0`, then `I_DP` length 11. In this chart `h_23≡0`, so the msolve/M2 generators are the five odd vanishings plus Rabinowitsch on `h_11`. Expected: possibly positive-dimensional (five conditions, 11 parameters). Cap 7200 s.

EMPTY ⇒ no polynomial curve with first odd remainder 11. NONEMPTY ⇒ run `idp_postcheck` with `N=11`.

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

```type86_A.m2
-- type86_A_I21: characteristic ideal in the (8,6) Tschirnhausen chart.
-- Identically zero generator h23 omitted. No saturate().
R0 = QQ[B, C, D, E, F, G, b, gam, d, e, f, MonomialOrder => GRevLex];
assert(isPolynomialRing R0);
assert(numgens R0 == 11);
assert(coefficientRing R0 === QQ);
h21 = 3*B-4*gam;
h19 = -12*b*gam+3*D-4*e;
h17 = -12*b^2*gam+6*B*C-12*b*e-12*gam*d+3*F;
h15 = -4*b^3*gam+B^3-12*b^2*e-24*b*gam*d-4*gam^3+6*B*E+6*C*D-12*gam*f-12*d*e;
h13 = -4*b^3*e-12*b^2*gam*d-4*b*gam^3+3*B^2*D+3*B*C^2-24*b*gam*f-24*b*d*e-12*gam^2*e-12*gam*d^2+6*B*G+6*C*F+6*D*E-12*e*f;
h11 = -12*b^2*gam*f-12*b^2*d*e-12*b*gam^2*e-12*b*gam*d^2-4*gam^3*d+3*B^2*F+6*B*C*E+3*B*D^2+3*C^2*D-24*b*e*f-24*gam*d*f-12*gam*e^2-12*d^2*e+6*D*G+6*E*F;
I0 = ideal(h21, h19, h17, h15, h13);
assert(ring I0 === R0);
-- open condition h11 != 0 via inverse variable (Rabinowitsch)
R = R0[u];
assert(numgens R == 12);
Iopen = sub(I0, R) + ideal(sub(h11, R)*u - 1);
assert(ring Iopen === R);
-- in-chart gcd-2 cover: p,q even <=> B=D=F=gam=e=0
Cover0 = ideal(B, D, F, gam, e);
assert(ring Cover0 === R0);
Cover = sub(Cover0, R);
assert(ring Cover === R);

colonInf = (I, J) -> (
  assert(ring I === ring J);
  K := I;
  npass := 0;
  while true do (
    npass = npass + 1;
    if npass > 50 then error "colonInf: exceeded 50 passes";
    Knext := K : J;
    assert(ring Knext === ring I);
    if Knext == K then break;
    K = Knext;
  );
  K
);

Icolon = colonInf(Iopen, Cover);
assert(ring Icolon === R);
-- immersive open: resultant(p',q') != 0 (computed in M2, not expanded in this lane)
St = R0[symbol t];
use St;
p = t^8 + B*t^5 + C*t^4 + D*t^3 + E*t^2 + F*t + G;
q = t^6 + b*t^4 + gam*t^3 + d*t^2 + e*t + f;
res0 = resultant(diff(p,t), diff(q,t), t);
assert(ring res0 === R0);
Rv = R0[u, v];
Iimm = sub(I0, Rv) + ideal(sub(h11, Rv)*u - 1, sub(res0, Rv)*v - 1);
assert(ring Iimm === Rv);
IimmColon = colonInf(Iimm, sub(Cover0, Rv));
assert(ring IimmColon === Rv);
<< "=== type86_A_I21 dim Iopen " << dim Iopen << endl;
<< "=== type86_A_I21 dim Icolon " << dim Icolon << endl;
<< "=== type86_A_I21 dim IimmColon " << dim IimmColon << endl;
G = gens gb IimmColon;
<< "=== type86_A_I21 gb IimmColon " << G << endl;
if IimmColon == ideal(1_Rv) then << "=== type86_A_I21 EMPTY" << endl else << "=== type86_A_I21 NONEMPTY" << endl;
```

## 4. Type (8,6)-B — (23; 11, 10; 24), Δ=(8,6,9)

Charged `I_23=I_21+(h_11)`, open `h_9≠0`, `I_DP` length 10. Cap 7200 s.

EMPTY ⇒ no polynomial curve with first odd remainder 9. NONEMPTY ⇒ `idp_postcheck` with `N=10`.

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

```type86_B.m2
-- type86_B_I23: characteristic ideal in the (8,6) Tschirnhausen chart.
-- Identically zero generator h23 omitted. No saturate().
R0 = QQ[B, C, D, E, F, G, b, gam, d, e, f, MonomialOrder => GRevLex];
assert(isPolynomialRing R0);
assert(numgens R0 == 11);
assert(coefficientRing R0 === QQ);
h21 = 3*B-4*gam;
h19 = -12*b*gam+3*D-4*e;
h17 = -12*b^2*gam+6*B*C-12*b*e-12*gam*d+3*F;
h15 = -4*b^3*gam+B^3-12*b^2*e-24*b*gam*d-4*gam^3+6*B*E+6*C*D-12*gam*f-12*d*e;
h13 = -4*b^3*e-12*b^2*gam*d-4*b*gam^3+3*B^2*D+3*B*C^2-24*b*gam*f-24*b*d*e-12*gam^2*e-12*gam*d^2+6*B*G+6*C*F+6*D*E-12*e*f;
h11 = -12*b^2*gam*f-12*b^2*d*e-12*b*gam^2*e-12*b*gam*d^2-4*gam^3*d+3*B^2*F+6*B*C*E+3*B*D^2+3*C^2*D-24*b*e*f-24*gam*d*f-12*gam*e^2-12*d^2*e+6*D*G+6*E*F;
h9 = -12*b^2*e*f-24*b*gam*d*f-12*b*gam*e^2-12*b*d^2*e-4*gam^3*f-12*gam^2*d*e-4*gam*d^3+6*B*C*G+6*B*D*F+3*B*E^2+3*C^2*F+6*C*D*E+D^3-12*gam*f^2-24*d*e*f-4*e^3+6*F*G;
I0 = ideal(h21, h19, h17, h15, h13, h11);
assert(ring I0 === R0);
-- open condition h9 != 0 via inverse variable (Rabinowitsch)
R = R0[u];
assert(numgens R == 12);
Iopen = sub(I0, R) + ideal(sub(h9, R)*u - 1);
assert(ring Iopen === R);
-- in-chart gcd-2 cover: p,q even <=> B=D=F=gam=e=0
Cover0 = ideal(B, D, F, gam, e);
assert(ring Cover0 === R0);
Cover = sub(Cover0, R);
assert(ring Cover === R);

colonInf = (I, J) -> (
  assert(ring I === ring J);
  K := I;
  npass := 0;
  while true do (
    npass = npass + 1;
    if npass > 50 then error "colonInf: exceeded 50 passes";
    Knext := K : J;
    assert(ring Knext === ring I);
    if Knext == K then break;
    K = Knext;
  );
  K
);

Icolon = colonInf(Iopen, Cover);
assert(ring Icolon === R);
-- immersive open: resultant(p',q') != 0 (computed in M2, not expanded in this lane)
St = R0[symbol t];
use St;
p = t^8 + B*t^5 + C*t^4 + D*t^3 + E*t^2 + F*t + G;
q = t^6 + b*t^4 + gam*t^3 + d*t^2 + e*t + f;
res0 = resultant(diff(p,t), diff(q,t), t);
assert(ring res0 === R0);
Rv = R0[u, v];
Iimm = sub(I0, Rv) + ideal(sub(h9, Rv)*u - 1, sub(res0, Rv)*v - 1);
assert(ring Iimm === Rv);
IimmColon = colonInf(Iimm, sub(Cover0, Rv));
assert(ring IimmColon === Rv);
<< "=== type86_B_I23 dim Iopen " << dim Iopen << endl;
<< "=== type86_B_I23 dim Icolon " << dim Icolon << endl;
<< "=== type86_B_I23 dim IimmColon " << dim IimmColon << endl;
G = gens gb IimmColon;
<< "=== type86_B_I23 gb IimmColon " << G << endl;
if IimmColon == ideal(1_Rv) then << "=== type86_B_I23 EMPTY" << endl else << "=== type86_B_I23 NONEMPTY" << endl;
```

## 5. Type (8,6)-C — (25; 12, 9; 26), Δ=(8,6,7)

Charged `I_25=I_23+(h_9)`, open `h_7≠0`, `I_DP` length 9. Cap 10800 s.

EMPTY ⇒ no polynomial curve with first odd remainder 7. NONEMPTY ⇒ `idp_postcheck` with `N=9`.

```type86_C.ms
B,C,D,E,F,G,b,gam,d,e,f,u
0
3*B-4*gam,
-12*b*gam+3*D-4*e,
-12*b^2*gam+6*B*C-12*b*e-12*gam*d+3*F,
-4*b^3*gam+B^3-12*b^2*e-24*b*gam*d-4*gam^3+6*B*E+6*C*D-12*gam*f-12*d*e,
-4*b^3*e-12*b^2*gam*d-4*b*gam^3+3*B^2*D+3*B*C^2-24*b*gam*f-24*b*d*e-12*gam^2*e-12*gam*d^2+6*B*G+6*C*F+6*D*E-12*e*f,
-12*b^2*gam*f-12*b^2*d*e-12*b*gam^2*e-12*b*gam*d^2-4*gam^3*d+3*B^2*F+6*B*C*E+3*B*D^2+3*C^2*D-24*b*e*f-24*gam*d*f-12*gam*e^2-12*d^2*e+6*D*G+6*E*F,
-12*b^2*e*f-24*b*gam*d*f-12*b*gam*e^2-12*b*d^2*e-4*gam^3*f-12*gam^2*d*e-4*gam*d^3+6*B*C*G+6*B*D*F+3*B*E^2+3*C^2*F+6*C*D*E+D^3-12*gam*f^2-24*d*e*f-4*e^3+6*F*G,
-12*b*gam*f^2*u-24*b*d*e*f*u-4*b*e^3*u-12*gam^2*e*f*u-12*gam*d^2*f*u-12*gam*d*e^2*u-4*d^3*e*u+6*B*E*G*u+3*B*F^2*u+6*C*D*G*u+6*C*E*F*u+3*D^2*F*u+3*D*E^2*u-12*e*f^2*u-1
```

```type86_C.m2
-- type86_C_I25: characteristic ideal in the (8,6) Tschirnhausen chart.
-- Identically zero generator h23 omitted. No saturate().
R0 = QQ[B, C, D, E, F, G, b, gam, d, e, f, MonomialOrder => GRevLex];
assert(isPolynomialRing R0);
assert(numgens R0 == 11);
assert(coefficientRing R0 === QQ);
h21 = 3*B-4*gam;
h19 = -12*b*gam+3*D-4*e;
h17 = -12*b^2*gam+6*B*C-12*b*e-12*gam*d+3*F;
h15 = -4*b^3*gam+B^3-12*b^2*e-24*b*gam*d-4*gam^3+6*B*E+6*C*D-12*gam*f-12*d*e;
h13 = -4*b^3*e-12*b^2*gam*d-4*b*gam^3+3*B^2*D+3*B*C^2-24*b*gam*f-24*b*d*e-12*gam^2*e-12*gam*d^2+6*B*G+6*C*F+6*D*E-12*e*f;
h11 = -12*b^2*gam*f-12*b^2*d*e-12*b*gam^2*e-12*b*gam*d^2-4*gam^3*d+3*B^2*F+6*B*C*E+3*B*D^2+3*C^2*D-24*b*e*f-24*gam*d*f-12*gam*e^2-12*d^2*e+6*D*G+6*E*F;
h9 = -12*b^2*e*f-24*b*gam*d*f-12*b*gam*e^2-12*b*d^2*e-4*gam^3*f-12*gam^2*d*e-4*gam*d^3+6*B*C*G+6*B*D*F+3*B*E^2+3*C^2*F+6*C*D*E+D^3-12*gam*f^2-24*d*e*f-4*e^3+6*F*G;
h7 = -12*b*gam*f^2-24*b*d*e*f-4*b*e^3-12*gam^2*e*f-12*gam*d^2*f-12*gam*d*e^2-4*d^3*e+6*B*E*G+3*B*F^2+6*C*D*G+6*C*E*F+3*D^2*F+3*D*E^2-12*e*f^2;
I0 = ideal(h21, h19, h17, h15, h13, h11, h9);
assert(ring I0 === R0);
-- open condition h7 != 0 via inverse variable (Rabinowitsch)
R = R0[u];
assert(numgens R == 12);
Iopen = sub(I0, R) + ideal(sub(h7, R)*u - 1);
assert(ring Iopen === R);
-- in-chart gcd-2 cover: p,q even <=> B=D=F=gam=e=0
Cover0 = ideal(B, D, F, gam, e);
assert(ring Cover0 === R0);
Cover = sub(Cover0, R);
assert(ring Cover === R);

colonInf = (I, J) -> (
  assert(ring I === ring J);
  K := I;
  npass := 0;
  while true do (
    npass = npass + 1;
    if npass > 50 then error "colonInf: exceeded 50 passes";
    Knext := K : J;
    assert(ring Knext === ring I);
    if Knext == K then break;
    K = Knext;
  );
  K
);

Icolon = colonInf(Iopen, Cover);
assert(ring Icolon === R);
-- immersive open: resultant(p',q') != 0 (computed in M2, not expanded in this lane)
St = R0[symbol t];
use St;
p = t^8 + B*t^5 + C*t^4 + D*t^3 + E*t^2 + F*t + G;
q = t^6 + b*t^4 + gam*t^3 + d*t^2 + e*t + f;
res0 = resultant(diff(p,t), diff(q,t), t);
assert(ring res0 === R0);
Rv = R0[u, v];
Iimm = sub(I0, Rv) + ideal(sub(h7, Rv)*u - 1, sub(res0, Rv)*v - 1);
assert(ring Iimm === Rv);
IimmColon = colonInf(Iimm, sub(Cover0, Rv));
assert(ring IimmColon === Rv);
<< "=== type86_C_I25 dim Iopen " << dim Iopen << endl;
<< "=== type86_C_I25 dim Icolon " << dim Icolon << endl;
<< "=== type86_C_I25 dim IimmColon " << dim IimmColon << endl;
G = gens gb IimmColon;
<< "=== type86_C_I25 gb IimmColon " << G << endl;
if IimmColon == ideal(1_Rv) then << "=== type86_C_I25 EMPTY" << endl else << "=== type86_C_I25 NONEMPTY" << endl;
```

## 6. Type (8,6)-D — (29; 14, 7; 30), Δ=(8,6,3)

Charged `I_29=(h_23,h_21,h_19,h_17,h_15,h_13,h_11,h_9,h_7,h_5)`, open `h_3≠0`, `I_DP` length 7. `h_23≡0` omitted. Overdetermined in ~11 vars; Moh JRAM 340 remains an unsourced lead (not consumed). FSY Lemma 1 (`deg_t g_2=3`) is the same finite problem in approximate-root coordinates; this bundle uses the leading-form chart, not `g_2`. Cap 7200 s.

EMPTY ⇒ no polynomial curve with first odd remainder 3. NONEMPTY ⇒ `idp_postcheck` with `N=7`.

```type86_D.ms
B,C,D,E,F,G,b,gam,d,e,f,u
0
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

```type86_D.m2
-- type86_D_I29: characteristic ideal in the (8,6) Tschirnhausen chart.
-- Identically zero generator h23 omitted. No saturate().
R0 = QQ[B, C, D, E, F, G, b, gam, d, e, f, MonomialOrder => GRevLex];
assert(isPolynomialRing R0);
assert(numgens R0 == 11);
assert(coefficientRing R0 === QQ);
h21 = 3*B-4*gam;
h19 = -12*b*gam+3*D-4*e;
h17 = -12*b^2*gam+6*B*C-12*b*e-12*gam*d+3*F;
h15 = -4*b^3*gam+B^3-12*b^2*e-24*b*gam*d-4*gam^3+6*B*E+6*C*D-12*gam*f-12*d*e;
h13 = -4*b^3*e-12*b^2*gam*d-4*b*gam^3+3*B^2*D+3*B*C^2-24*b*gam*f-24*b*d*e-12*gam^2*e-12*gam*d^2+6*B*G+6*C*F+6*D*E-12*e*f;
h11 = -12*b^2*gam*f-12*b^2*d*e-12*b*gam^2*e-12*b*gam*d^2-4*gam^3*d+3*B^2*F+6*B*C*E+3*B*D^2+3*C^2*D-24*b*e*f-24*gam*d*f-12*gam*e^2-12*d^2*e+6*D*G+6*E*F;
h9 = -12*b^2*e*f-24*b*gam*d*f-12*b*gam*e^2-12*b*d^2*e-4*gam^3*f-12*gam^2*d*e-4*gam*d^3+6*B*C*G+6*B*D*F+3*B*E^2+3*C^2*F+6*C*D*E+D^3-12*gam*f^2-24*d*e*f-4*e^3+6*F*G;
h7 = -12*b*gam*f^2-24*b*d*e*f-4*b*e^3-12*gam^2*e*f-12*gam*d^2*f-12*gam*d*e^2-4*d^3*e+6*B*E*G+3*B*F^2+6*C*D*G+6*C*E*F+3*D^2*F+3*D*E^2-12*e*f^2;
h5 = -12*b*e*f^2-12*gam*d*f^2-12*gam*e^2*f-12*d^2*e*f-4*d*e^3+3*B*G^2+6*C*F*G+6*D*E*G+3*D*F^2+3*E^2*F;
h3 = -4*gam*f^3-12*d*e*f^2-4*e^3*f+3*D*G^2+6*E*F*G+F^3;
I0 = ideal(h21, h19, h17, h15, h13, h11, h9, h7, h5);
assert(ring I0 === R0);
-- open condition h3 != 0 via inverse variable (Rabinowitsch)
R = R0[u];
assert(numgens R == 12);
Iopen = sub(I0, R) + ideal(sub(h3, R)*u - 1);
assert(ring Iopen === R);
-- in-chart gcd-2 cover: p,q even <=> B=D=F=gam=e=0
Cover0 = ideal(B, D, F, gam, e);
assert(ring Cover0 === R0);
Cover = sub(Cover0, R);
assert(ring Cover === R);

colonInf = (I, J) -> (
  assert(ring I === ring J);
  K := I;
  npass := 0;
  while true do (
    npass = npass + 1;
    if npass > 50 then error "colonInf: exceeded 50 passes";
    Knext := K : J;
    assert(ring Knext === ring I);
    if Knext == K then break;
    K = Knext;
  );
  K
);

Icolon = colonInf(Iopen, Cover);
assert(ring Icolon === R);
-- immersive open: resultant(p',q') != 0 (computed in M2, not expanded in this lane)
St = R0[symbol t];
use St;
p = t^8 + B*t^5 + C*t^4 + D*t^3 + E*t^2 + F*t + G;
q = t^6 + b*t^4 + gam*t^3 + d*t^2 + e*t + f;
res0 = resultant(diff(p,t), diff(q,t), t);
assert(ring res0 === R0);
Rv = R0[u, v];
Iimm = sub(I0, Rv) + ideal(sub(h3, Rv)*u - 1, sub(res0, Rv)*v - 1);
assert(ring Iimm === Rv);
IimmColon = colonInf(Iimm, sub(Cover0, Rv));
assert(ring IimmColon === Rv);
<< "=== type86_D_I29 dim Iopen " << dim Iopen << endl;
<< "=== type86_D_I29 dim Icolon " << dim Icolon << endl;
<< "=== type86_D_I29 dim IimmColon " << dim IimmColon << endl;
G = gens gb IimmColon;
<< "=== type86_D_I29 gb IimmColon " << G << endl;
if IimmColon == ideal(1_Rv) then << "=== type86_D_I29 EMPTY" << endl else << "=== type86_D_I29 NONEMPTY" << endl;
```

## 7. Type (9,6)-A — (23; 22, 6; 25), Δ=(9,6,4)

Charged `I_(9,6,4)=(k_17,…,k_5)`, open `k_4≠0`, `I_DP` length 6. `k_17≡0` omitted: generators `k_16` through `k_5` plus Rabinowitsch on `k_4`. Even-odd cover excluded by colon against `(P6,P4,P2,Q3,Q1)`. Cap 14400 s.

EMPTY ⇒ no polynomial curve with remainder degree 4. NONEMPTY ⇒ `idp_postcheck` with `N=6`.

```type96_A.ms
A,P6,B,P4,C,P2,D,a,Q3,b,Q1,u
0
2*A-3*a,
2*P6-3*Q3,
A^2-3*a^2+2*B-3*b,
2*A*P6-6*a*Q3+2*P4-3*Q1,
-a^3+2*A*B+P6^2-6*a*b-3*Q3^2+2*C,
-3*a^2*Q3+2*A*P4+2*P6*B-6*a*Q1-6*Q3*b+2*P2,
-3*a^2*b-3*a*Q3^2+2*A*C+2*P6*P4+B^2-6*Q3*Q1-3*b^2+2*D,
-3*a^2*Q1-6*a*Q3*b-Q3^3+2*A*P2+2*P6*C+2*B*P4-6*b*Q1,
-6*a*Q3*Q1-3*a*b^2-3*Q3^2*b+2*A*D+2*P6*P2+2*B*C+P4^2-3*Q1^2,
-6*a*b*Q1-3*Q3^2*Q1-3*Q3*b^2+2*P6*D+2*B*P2+2*P4*C,
-3*a*Q1^2-6*Q3*b*Q1-b^3+2*B*D+2*P4*P2+C^2,
-3*Q3*Q1^2-3*b^2*Q1+2*P4*D+2*C*P2,
-3*b*Q1^2*u+2*C*D*u+P2^2*u-1
```

```type96_A.m2
-- type96_A_I964: characteristic ideal in the (9,6) Tschirnhausen chart.
-- Identically zero generator k17 omitted. No saturate().
R0 = QQ[A, P6, B, P4, C, P2, D, a, Q3, b, Q1, MonomialOrder => GRevLex];
assert(isPolynomialRing R0);
assert(numgens R0 == 11);
assert(coefficientRing R0 === QQ);
k16 = 2*A-3*a;
k15 = 2*P6-3*Q3;
k14 = A^2-3*a^2+2*B-3*b;
k13 = 2*A*P6-6*a*Q3+2*P4-3*Q1;
k12 = -a^3+2*A*B+P6^2-6*a*b-3*Q3^2+2*C;
k11 = -3*a^2*Q3+2*A*P4+2*P6*B-6*a*Q1-6*Q3*b+2*P2;
k10 = -3*a^2*b-3*a*Q3^2+2*A*C+2*P6*P4+B^2-6*Q3*Q1-3*b^2+2*D;
k9 = -3*a^2*Q1-6*a*Q3*b-Q3^3+2*A*P2+2*P6*C+2*B*P4-6*b*Q1;
k8 = -6*a*Q3*Q1-3*a*b^2-3*Q3^2*b+2*A*D+2*P6*P2+2*B*C+P4^2-3*Q1^2;
k7 = -6*a*b*Q1-3*Q3^2*Q1-3*Q3*b^2+2*P6*D+2*B*P2+2*P4*C;
k6 = -3*a*Q1^2-6*Q3*b*Q1-b^3+2*B*D+2*P4*P2+C^2;
k5 = -3*Q3*Q1^2-3*b^2*Q1+2*P4*D+2*C*P2;
k4 = -3*b*Q1^2+2*C*D+P2^2;
I0 = ideal(k16, k15, k14, k13, k12, k11, k10, k9, k8, k7, k6, k5);
assert(ring I0 === R0);
R = R0[u];
Iopen = sub(I0, R) + ideal(sub(k4, R)*u - 1);
assert(ring Iopen === R);
-- even-odd cover: P6=P4=P2=Q3=Q1=0
Cover0 = ideal(P6, P4, P2, Q3, Q1);
assert(ring Cover0 === R0);
Cover = sub(Cover0, R);

colonInf = (I, J) -> (
  assert(ring I === ring J);
  K := I;
  npass := 0;
  while true do (
    npass = npass + 1;
    if npass > 50 then error "colonInf: exceeded 50 passes";
    Knext := K : J;
    assert(ring Knext === ring I);
    if Knext == K then break;
    K = Knext;
  );
  K
);

Icolon = colonInf(Iopen, Cover);
assert(ring Icolon === R);
St = R0[symbol t];
use St;
p = t^9 + A*t^7 + P6*t^6 + B*t^5 + P4*t^4 + C*t^3 + P2*t^2 + D*t;
q = t^6 + a*t^4 + Q3*t^3 + b*t^2 + Q1*t;
res0 = resultant(diff(p,t), diff(q,t), t);
assert(ring res0 === R0);
Rv = R0[u, v];
Iimm = sub(I0, Rv) + ideal(sub(k4, Rv)*u - 1, sub(res0, Rv)*v - 1);
assert(ring Iimm === Rv);
IimmColon = colonInf(Iimm, sub(Cover0, Rv));
assert(ring IimmColon === Rv);
<< "=== type96_A_I964 dim Iopen " << dim Iopen << endl;
<< "=== type96_A_I964 dim Icolon " << dim Icolon << endl;
<< "=== type96_A_I964 dim IimmColon " << dim IimmColon << endl;
G = gens gb IimmColon;
<< "=== type96_A_I964 gb IimmColon " << G << endl;
if IimmColon == ideal(1_Rv) then << "=== type96_A_I964 EMPTY" << endl else << "=== type96_A_I964 NONEMPTY" << endl;
```

## 8. Type (9,6)-B — (25; 24, 4; 27), Δ=(9,6,2)

Charged `I_(9,6,2)=(k_17,…,k_3)`, open `k_2≠0`, `I_DP` length 4. Generators `k_16` through `k_3` plus Rabinowitsch on `k_2=D^2` (so `D≠0`). The involution slice `q∈ℂ[t^2+at+b]` is **not** a separate job: it is a closed subscheme of this ideal (set `Q3=Q1=0` and `P6=P4=P2` as needed) and remains untested at desk, as the charged report states. Cap 14400 s.

EMPTY ⇒ no polynomial curve with remainder degree 2. NONEMPTY ⇒ `idp_postcheck` with `N=4`.

```type96_B.ms
A,P6,B,P4,C,P2,D,a,Q3,b,Q1,u
0
2*A-3*a,
2*P6-3*Q3,
A^2-3*a^2+2*B-3*b,
2*A*P6-6*a*Q3+2*P4-3*Q1,
-a^3+2*A*B+P6^2-6*a*b-3*Q3^2+2*C,
-3*a^2*Q3+2*A*P4+2*P6*B-6*a*Q1-6*Q3*b+2*P2,
-3*a^2*b-3*a*Q3^2+2*A*C+2*P6*P4+B^2-6*Q3*Q1-3*b^2+2*D,
-3*a^2*Q1-6*a*Q3*b-Q3^3+2*A*P2+2*P6*C+2*B*P4-6*b*Q1,
-6*a*Q3*Q1-3*a*b^2-3*Q3^2*b+2*A*D+2*P6*P2+2*B*C+P4^2-3*Q1^2,
-6*a*b*Q1-3*Q3^2*Q1-3*Q3*b^2+2*P6*D+2*B*P2+2*P4*C,
-3*a*Q1^2-6*Q3*b*Q1-b^3+2*B*D+2*P4*P2+C^2,
-3*Q3*Q1^2-3*b^2*Q1+2*P4*D+2*C*P2,
-3*b*Q1^2+2*C*D+P2^2,
-Q1^3+2*P2*D,
D^2*u-1
```

```type96_B.m2
-- type96_B_I962: characteristic ideal in the (9,6) Tschirnhausen chart.
-- Identically zero generator k17 omitted. No saturate().
R0 = QQ[A, P6, B, P4, C, P2, D, a, Q3, b, Q1, MonomialOrder => GRevLex];
assert(isPolynomialRing R0);
assert(numgens R0 == 11);
assert(coefficientRing R0 === QQ);
k16 = 2*A-3*a;
k15 = 2*P6-3*Q3;
k14 = A^2-3*a^2+2*B-3*b;
k13 = 2*A*P6-6*a*Q3+2*P4-3*Q1;
k12 = -a^3+2*A*B+P6^2-6*a*b-3*Q3^2+2*C;
k11 = -3*a^2*Q3+2*A*P4+2*P6*B-6*a*Q1-6*Q3*b+2*P2;
k10 = -3*a^2*b-3*a*Q3^2+2*A*C+2*P6*P4+B^2-6*Q3*Q1-3*b^2+2*D;
k9 = -3*a^2*Q1-6*a*Q3*b-Q3^3+2*A*P2+2*P6*C+2*B*P4-6*b*Q1;
k8 = -6*a*Q3*Q1-3*a*b^2-3*Q3^2*b+2*A*D+2*P6*P2+2*B*C+P4^2-3*Q1^2;
k7 = -6*a*b*Q1-3*Q3^2*Q1-3*Q3*b^2+2*P6*D+2*B*P2+2*P4*C;
k6 = -3*a*Q1^2-6*Q3*b*Q1-b^3+2*B*D+2*P4*P2+C^2;
k5 = -3*Q3*Q1^2-3*b^2*Q1+2*P4*D+2*C*P2;
k4 = -3*b*Q1^2+2*C*D+P2^2;
k3 = -Q1^3+2*P2*D;
k2 = D^2;
I0 = ideal(k16, k15, k14, k13, k12, k11, k10, k9, k8, k7, k6, k5, k4, k3);
assert(ring I0 === R0);
R = R0[u];
Iopen = sub(I0, R) + ideal(sub(k2, R)*u - 1);
assert(ring Iopen === R);
-- even-odd cover: P6=P4=P2=Q3=Q1=0
Cover0 = ideal(P6, P4, P2, Q3, Q1);
assert(ring Cover0 === R0);
Cover = sub(Cover0, R);

colonInf = (I, J) -> (
  assert(ring I === ring J);
  K := I;
  npass := 0;
  while true do (
    npass = npass + 1;
    if npass > 50 then error "colonInf: exceeded 50 passes";
    Knext := K : J;
    assert(ring Knext === ring I);
    if Knext == K then break;
    K = Knext;
  );
  K
);

Icolon = colonInf(Iopen, Cover);
assert(ring Icolon === R);
St = R0[symbol t];
use St;
p = t^9 + A*t^7 + P6*t^6 + B*t^5 + P4*t^4 + C*t^3 + P2*t^2 + D*t;
q = t^6 + a*t^4 + Q3*t^3 + b*t^2 + Q1*t;
res0 = resultant(diff(p,t), diff(q,t), t);
assert(ring res0 === R0);
Rv = R0[u, v];
Iimm = sub(I0, Rv) + ideal(sub(k2, Rv)*u - 1, sub(res0, Rv)*v - 1);
assert(ring Iimm === Rv);
IimmColon = colonInf(Iimm, sub(Cover0, Rv));
assert(ring IimmColon === Rv);
<< "=== type96_B_I962 dim Iopen " << dim Iopen << endl;
<< "=== type96_B_I962 dim Icolon " << dim Icolon << endl;
<< "=== type96_B_I962 dim IimmColon " << dim IimmColon << endl;
G = gens gb IimmColon;
<< "=== type96_B_I962 gb IimmColon " << G << endl;
if IimmColon == ideal(1_Rv) then << "=== type96_B_I962 EMPTY" << endl else << "=== type96_B_I962 NONEMPTY" << endl;
```

## 9. Positive control — (6,4,3): I_DP length 3 reduced

The charged control is the ROW-SWEEP §2 witness, not a characteristic ideal in the (8,6) chart:

```text
r = t^3 + t + 1
q = t^4 + (2/3) t^2 + (4/3) t
p = r^2
I_DP = (pi - sig^2 - 1, 3 sig^3 + 4 sig - 4)
```

Desk check of the conversion: Delta(t^n) = sig*Delta(t^{n-1}) - pi*Delta(t^{n-2}) with Delta(1)=0, Delta(t)=1 gives Delta(r) = sig^2 - pi + 1, hence pi - sig^2 - 1 = 0. Substituting into Delta(q) and clearing -3 yields the cubic. The cubic and its derivative 9x^2+4 are coprime (no shared root), so three distinct sig; pair discriminant -3 sig^2 - 4 cannot vanish on the cubic. Cap 120 s.

msolve expected: 0-dimensional, nonempty, three complex solutions. M2 expected: dim=0, degree=3, radical, gcd(cubic, cubic')=1. FAIL of this control aborts the suite.

```control_pos_643_idp.ms
sig,pi
0
pi-sig^2-1,
3*sig^3+4*sig-4
```

```control_pos_643_idp.m2
-- control_pos_643_idp.m2
-- Positive control: ROW-SWEEP §2 three-node witness of Delta=(6,4,3).
-- Expected: I_DP 0-dimensional, degree 3, radical, distinct tangents, no reused parameter.
-- No saturate(). Rings asserted. Formula of I_DP in (sig,pi) is the charged identity
--   (pi - sig^2 - 1, 3*sig^3 + 4*sig - 4).
R = QQ[sig, pi, MonomialOrder => GRevLex];
assert(isPolynomialRing R);
I = ideal(pi - sig^2 - 1, 3*sig^3 + 4*sig - 4);
assert(ring I === R);
assert(dim I == 0);
assert(degree I == 3);
assert(I == radical I);
-- discriminant of 3x^3+4x-4 is nonzero (desk: 3 cubic, no repeated root with the derivative 9x^2+4>0 on R and gcd(cubic, deriv)=1)
Rt = QQ[x];
cub = 3*x^3 + 4*x - 4;
assert(gcd(cub, diff(cub,x)) == 1_Rt);
<< "=== control_pos PASS: I_DP length 3 reduced" << endl;
```

## 10. Negative control — (t^8, t^6): gcd-2

Parametrization (t^8, t^6) is a degree-2 cover of (u^4, u^3). p'=8t^7, q'=6t^5, gcd has degree 5. Off-diagonal I_DP contains the involution s=-t (sig=0), so it is positive-dimensional, not a reduced length-delta_aff nodal scheme.

msolve input: Delta_8, Delta_6, and u(s-t)-1. Expected: not EMPTY and not 0-dimensional (positive-dim involution). If msolve reports EMPTY or 0-dim of nodal length, the I_DP toolchain is wrong and the suite aborts.

Companion (t^9, t^6) (gcd 3) is asserted in the M2 file only.

```control_neg_t8t6.ms
s,t,u
0
s^7+s^6*t+s^5*t^2+s^4*t^3+s^3*t^4+s^2*t^5+s*t^6+t^7,
s^5+s^4*t+s^3*t^2+s^2*t^3+s*t^4+t^5,
u*s-u*t-1
```

```control_neg_t8t6.m2
-- control_neg_t8t6.m2
-- Negative control: (p,q)=(t^8, t^6), gcd 2. Expected: non-immersive (deg gcd(p',q')>0)
-- and I_DP positive-dimensional (involution s=-t). Abort the suite if this looks nodal.
Kt = QQ[t];
p = t^8;
q = t^6;
g = gcd(diff(p,t), diff(q,t));
assert(degree g > 0);
-- I_DP in (s,t), off-diagonal via inverse u*(s-t)-1
R = QQ[s, t, u, MonomialOrder => GRevLex];
d8 = s^7 + s^6*t + s^5*t^2 + s^4*t^3 + s^3*t^4 + s^2*t^5 + s*t^6 + t^7;
d6 = s^5 + s^4*t + s^3*t^2 + s^2*t^3 + s*t^4 + t^5;
I = ideal(d8, d6, u*(s-t) - 1);
assert(ring I === R);
-- the line s+t=0, s!=t is a component: dim >= 1
assert(dim I >= 1);
<< "=== control_neg PASS: gcd-2, I_DP not 0-dim" << endl;
-- companion (t^9,t^6) gcd-3
Kt2 = QQ[tt];
p9 = tt^9; q6 = tt^6;
g3 = gcd(diff(p9,tt), diff(q6,tt));
assert(degree g3 > 0);
<< "=== control_neg companion (t^9,t^6) gcd-3 PASS" << endl;
```

## 11. Driver script `run_realization_suite.sh`

Requires `REALIZATION_AWS=1`. Runs M2/msolve controls first and aborts on FAIL. Then the six types, each under `timeout(1)` with the caps of §1. Writes `logs/summary.tsv` and per-job stdout/stderr. Interprets msolve `[-1]` as EMPTY, `[1, nvars, -1, []]` as NONEMPTY_POSDIM, else NONEMPTY_0DIM. TIMEOUT is recorded, not treated as EMPTY.

```run_realization_suite.sh
#!/usr/bin/env bash
# run_realization_suite.sh
# AWS-only driver for the six (8,6)/(9,6) realization ideals.
# Runs controls first and aborts on control failure. Does not run on a laptop
# by default: require REALIZATION_AWS=1.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
LOG="$ROOT/logs"
mkdir -p "$LOG"
SUMMARY="$LOG/summary.tsv"
echo -e "job\tstatus\tseconds\tnote" > "$SUMMARY"

if [[ "${REALIZATION_AWS:-0}" != "1" ]]; then
  echo "Refusing to run: set REALIZATION_AWS=1 on the AWS box." >&2
  echo "This suite is campaign-policy AWS-ONLY (heavy/uncertain CAS)." >&2
  exit 2
fi

have_msolve=0
have_m2=0
command -v msolve >/dev/null 2>&1 && have_msolve=1
command -v M2 >/dev/null 2>&1 && have_m2=1
if [[ "$have_msolve" -eq 0 && "$have_m2" -eq 0 ]]; then
  echo "Neither msolve nor M2 is on PATH." >&2
  exit 2
fi

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

run_m2() {
  local job="$1" cap="$2" file="$3"
  local start end rc
  start=$(date +%s)
  set +e
  run_timeout "$cap" M2 --silent --stop --no-preload "$ROOT/$file" \
    > "$LOG/${job}.m2.out" 2> "$LOG/${job}.m2.err"
  rc=$?
  set -e
  end=$(date +%s)
  echo "$rc" > "$LOG/${job}.m2.rc"
  echo $((end-start))
  return "$rc"
}

run_msolve() {
  local job="$1" cap="$2" file="$3"
  local start end rc
  start=$(date +%s)
  set +e
  run_timeout "$cap" msolve -v 2 -g 2 -f "$ROOT/$file" -o "$LOG/${job}.msolve.out" \
    > "$LOG/${job}.msolve.stdout" 2> "$LOG/${job}.msolve.err"
  rc=$?
  set -e
  end=$(date +%s)
  echo "$rc" > "$LOG/${job}.msolve.rc"
  echo $((end-start))
  return "$rc"
}

interpret_msolve() {
  local out="$1"
  if [[ ! -s "$out" ]]; then
    echo "NO_OUTPUT"
    return
  fi
  # msolve: [-1] empty; [1, nvars, -1, []] positive-dim; else 0-dim solutions
  if grep -q '^\s*\[-1\]' "$out"; then
    echo "EMPTY"
  elif grep -q -- ',-1,\s*\[]' "$out" || grep -q 'positive' "$out"; then
    echo "NONEMPTY_POSDIM"
  else
    echo "NONEMPTY_0DIM"
  fi
}

# --- wall-clock caps (seconds), from charged size vs FSY 2006 hours-scale ---
CAP_POS=120
CAP_NEG=120
CAP_IDP=180
CAP_86A=7200    # I_21: 5 vanishing + 1 open, 12 vars, deg <=4
CAP_86B=7200    # I_23: one more generator
CAP_86C=10800   # I_25: eight-ish generators, ~9-12 vars
CAP_86D=7200    # I_29: overdetermined; empty may finish faster
CAP_96A=14400   # 12 vanishing + open, 12 vars, deg <=3
CAP_96B=14400

echo "=== CONTROLS ==="
if [[ "$have_m2" -eq 1 ]]; then
  t=$(run_m2 control_pos "$CAP_POS" control_pos_643_idp.m2) || {
    record control_pos FAIL "$t" "M2 positive control failed"
    echo "ABORT: positive control failed" >&2
    exit 1
  }
  if ! grep -q 'control_pos PASS' "$LOG/control_pos.m2.out"; then
    record control_pos FAIL "$t" "missing PASS line"
    exit 1
  fi
  record control_pos PASS "$t" "I_DP length 3 reduced"

  t=$(run_m2 control_neg "$CAP_NEG" control_neg_t8t6.m2) || {
    record control_neg FAIL "$t" "M2 negative control failed"
    echo "ABORT: negative control failed" >&2
    exit 1
  }
  if ! grep -q 'control_neg PASS' "$LOG/control_neg.m2.out"; then
    record control_neg FAIL "$t" "missing PASS line"
    exit 1
  fi
  record control_neg PASS "$t" "gcd-2 I_DP not 0-dim"

  t=$(run_m2 idp_selftest "$CAP_IDP" idp_postcheck.m2) || {
    record idp_selftest FAIL "$t" "idp_postcheck self-test failed"
    exit 1
  }
  if ! grep -q 'idp_postcheck self-tests completed' "$LOG/idp_selftest.m2.out"; then
    record idp_selftest FAIL "$t" "missing completion line"
    exit 1
  fi
  record idp_selftest PASS "$t" "witness length 3; (t^8,t^6) rejected"
else
  echo "M2 missing: skipping M2 controls; msolve-only path for idp controls"
fi

if [[ "$have_msolve" -eq 1 ]]; then
  t=$(run_msolve control_pos_ms "$CAP_POS" control_pos_643_idp.ms) || {
    record control_pos_ms FAIL "$t" "msolve positive control rc"
    exit 1
  }
  note=$(interpret_msolve "$LOG/control_pos_ms.msolve.out")
  if [[ "$note" == "EMPTY" ]]; then
    record control_pos_ms FAIL "$t" "$note (expected 0-dim nonempty length 3)"
    exit 1
  fi
  record control_pos_ms PASS "$t" "$note"

  set +e
  t=$(run_msolve control_neg_ms "$CAP_NEG" control_neg_t8t6.ms)
  rc=$?
  set -e
  note=$(interpret_msolve "$LOG/control_neg_ms.msolve.out")
  if [[ "$note" == "EMPTY" ]]; then
    record control_neg_ms FAIL "$t" "$note (negative control should NOT be empty: involution component)"
    exit 1
  fi
  if [[ "$note" == "NONEMPTY_0DIM" ]]; then
    record control_neg_ms FAIL "$t" "$note (expected positive-dim gcd-2 component)"
    exit 1
  fi
  record control_neg_ms PASS "$t" "$note (rc=$rc)"
fi

echo "=== SIX TYPES ==="
run_type() {
  local job="$1" cap="$2" ms="$3" m2="$4" empty_means="$5"
  local t note rc
  if [[ "$have_msolve" -eq 1 ]]; then
    set +e
    t=$(run_msolve "$job" "$cap" "$ms")
    rc=$?
    set -e
    note=$(interpret_msolve "$LOG/${job}.msolve.out")
    if [[ $rc -eq 124 || $rc -eq 137 ]]; then
      record "$job" TIMEOUT "$t" "msolve cap ${cap}s"
      return 0
    fi
    record "$job" "$note" "$t" "msolve; EMPTY means: $empty_means"
  fi
  if [[ "$have_m2" -eq 1 ]]; then
    set +e
    t=$(run_m2 "${job}_m2" "$cap" "$m2")
    rc=$?
    set -e
    if [[ $rc -eq 124 || $rc -eq 137 ]]; then
      record "${job}_m2" TIMEOUT "$t" "M2 cap ${cap}s"
      return 0
    fi
    if [[ $rc -ne 0 ]]; then
      record "${job}_m2" FAIL "$t" "M2 rc=$rc"
      return 0
    fi
    if grep -q EMPTY "$LOG/${job}_m2.m2.out"; then
      record "${job}_m2" EMPTY "$t" "M2; EMPTY means: $empty_means"
    else
      record "${job}_m2" NONEMPTY "$t" "M2; run idp_postcheck on a closed point"
    fi
  fi
}

run_type type86_A "$CAP_86A" type86_A.ms type86_A.m2 "no poly curve with first odd remainder 11 (type (8,6,11) non-realizable as polynomial curve)"
run_type type86_B "$CAP_86B" type86_B.ms type86_B.m2 "no poly curve with first odd remainder 9"
run_type type86_C "$CAP_86C" type86_C.ms type86_C.m2 "no poly curve with first odd remainder 7"
run_type type86_D "$CAP_86D" type86_D.ms type86_D.m2 "no poly curve with first odd remainder 3 (Moh lead / FSY g2 job)"
run_type type96_A "$CAP_96A" type96_A.ms type96_A.m2 "no poly curve with remainder degree 4"
run_type type96_B "$CAP_96B" type96_B.ms type96_B.m2 "no poly curve with remainder degree 2"

echo
echo "=== SUMMARY ==="
column -t -s $'\t' "$SUMMARY" || cat "$SUMMARY"
echo
echo "Post-check: for every NONEMPTY type, extract a closed point and run"
echo "  M2 idp_postcheck.m2  (load and call idpPostcheck(p,q,N) with N=delta_aff)."
echo "REALIZED iff some point has reduced I_DP of length delta_aff, immersive, distinct tangents, no triple fibre."
echo "NON-REALIZABLE iff EMPTY, or EVERY component fails the I_DP test."
```

## 12. Double-point-scheme post-check (`I_DP` reduced-length test)

For a closed point `(p,q)` in `QQ[t]`, convert divided differences to `(sig,pi)` by the recurrence Delta(t^n) = sig Delta(t^{n-1}) - pi Delta(t^{n-2}). Tests, in order: immersive (`gcd(p',q')=1`); `I_DP` 0-dimensional of degree `N=delta_aff`; radical; tangent form W = p'(t)q'(s)-p'(s)q'(t) nonvanishing on V(I_DP); parameter polynomial F(X)=product (X^2 - sig X + pi) square-free (no reused parameter / triple fibre). No `saturate()`.

The script self-tests the §9 witness (`N=3`, expect PASS) and `(t^8,t^6)` (`N=11`, expect FAIL). Those self-tests are small 0-dim / positive-dim checks of the *post-check machinery*, not the six realization Groebner jobs. The wronskian-to-(sig,pi) conversion uses a remainder in `QQ[s,sig,pi]`; if M2 rejects `degree(s,Wred)` syntax, treat the tangent clause as OPEN and use the explicit charged W-factors on a numeric closed point instead (flag in §14).

```idp_postcheck.m2
-- idp_postcheck.m2
-- Double-point scheme post-check for a closed point (p,q) in QQ[t].
-- Call:  idpPostcheck(p, q, N)
--   N = expected delta_aff.
-- Writes: length, reduced?, tangent-nonvanishing?, no-reused-parameter?
-- Conversion to (sig,pi) by Delta(t^n) = sig*Delta(t^{n-1}) - pi*Delta(t^{n-2}),
-- Delta(t^0)=0, Delta(t^1)=1. No saturate().

dividedDiffTable = (maxn, sig, pi) -> (
  -- returns a list L_0..L_maxn in the ring of sig
  L := new MutableList from toList((maxn+1):0_(ring sig));
  R := ring sig;
  L#0 = 0_R;
  if maxn >= 1 then L#1 = 1_R;
  if maxn >= 2 then L#2 = sig;
  for n from 3 to maxn do L#n = sig*(L#(n-1)) - pi*(L#(n-2));
  toList L
);

polyToDelta = (f, L) -> (
  -- f in k[t], L_n = Delta(t^n)
  Kt := ring f;
  t := Kt_0;
  d := first degree f;
  acc := 0_(ring L#1);
  for n from 0 to d do (
    c := coefficient(t^n, f);
    acc = acc + sub(c, ring L#1) * L#n;
  );
  acc
);

-- W = p'(t)q'(s)-p'(s)q'(t) = (s-t) * Wsym(sig,pi)
-- Compute Wsym from generating functions: it is the bilinear form on derivatives.
wronskianSym = (p, q, sig, pi) -> (
  Kt := ring p;
  t := Kt_0;
  dp := diff(p, t);
  dq := diff(q, t);
  -- p'(t)q'(s) - p'(s)q'(t) = sum_{i,j} p_i q_j (i t^{i-1} j s^{j-1} - j s^{j-1 wait})
  -- = sum_{i,j} i*j*coeff_p_i*coeff_q_j * (t^{i-1} s^{j-1} - s^{i-1} t^{j-1})
  -- For a pair, evaluate after converting the antisymmetric kernel.
  -- Use: (s-t)^{-1}(p'(t)q'(s)-p'(s)q'(t))
  -- which equals sum i j a_i b_j Delta_{i-1,j-1} with an explicit symmetric polynomial.
  -- Implementation: work in QQ[s,t], form W, divide by (s-t), convert.
  Rst := QQ[s, t];
  ps := sub(p, {t => Rst_1}); -- p as poly in t, then
  -- rebuild p,q in Rst
  toST := (f, var) -> (
    acc := 0_Rst;
    df := first degree f;
    for n from 0 to df do acc = acc + sub(coefficient(t^n, f), Rst) * var^n;
    acc
  );
  p_s := toST(p, s); p_t := toST(p, t);
  q_s := toST(q, s); q_t := toST(q, t);
  Wp := diff(p_t, t)*diff(q_s, s) - diff(p_s, s)*diff(q_t, t);
  assert((Wp % (s-t)) == 0);
  W1 := Wp // (s-t);
  -- W1 is symmetric; express in sig,pi by substituting elementary identities
  -- via the inverse of the map QQ[sig,pi] -> QQ[s,t]^{S2}.
  -- Use: any symmetric poly is unique in sig,pi. Convert monomials s^a t^b + s^b t^a.
  Rsp := ring sig;
  -- Groebner conversion: ring map from QQ[s,t] with lex and reduce by
  -- (s+t-sig, s*t-pi) after symmetrizing is unnecessary if we take
  -- generators of the kernel. Direct: substitute t -> sig-s, reduce st-pi.
  Raux := QQ[s, sig, pi, MonomialOrder => Lex];
  Waux := sub(W1, {s => s, t => sig - s});
  Wred := Waux % ideal(s*(sig-s) - pi);
  -- remainder should lie in QQ[sig,pi]
  assert(degree(s, Wred) <= 0 or Wred == 0);
  sub(Wred, {s => 0_Rsp, sig => sig, pi => pi})
);

idpPostcheck = method();
idpPostcheck(RingElement, RingElement, ZZ) := (p, q, N) -> (
  Kt := ring p;
  assert(Kt === ring q);
  assert(numgens Kt == 1);
  t := Kt_0;
  dp := diff(p, t);
  dq := diff(q, t);
  g := gcd(dp, dq);
  immersive := (g == 1_Kt);
  Rsp := QQ[sig, pi, MonomialOrder => GRevLex];
  sig := Rsp_0; pi := Rsp_1;
  maxn := max(first degree p, first degree q);
  L := dividedDiffTable(maxn, sig, pi);
  Dp := polyToDelta(p, L);
  Dq := polyToDelta(q, L);
  I := ideal(Dp, Dq);
  assert(ring I === Rsp);
  << "idp: dim=" << dim I << " degree=" << (if dim I == 0 then degree I else -1) << endl;
  << "idp: immersive=" << immersive << endl;
  if dim I != 0 then (
    << "idp: FAIL not 0-dimensional (cover or positive-dim identifications)" << endl;
    return false;
  );
  if degree I != N then (
    << "idp: FAIL length " << degree I << " != expected " << N << endl;
    return false;
  );
  if I != radical I then (
    << "idp: FAIL not reduced" << endl;
    return false;
  );
  -- distinct tangents: Wsym does not vanish on V(I)
  Wsym := wronskianSym(p, q, sig, pi);
  J := I + ideal(Wsym);
  assert(ring J === Rsp);
  if J != ideal(1_Rsp) then (
    << "idp: FAIL coincident tangents (Wsym vanishes on a pair)" << endl;
    return false;
  );
  -- no reused parameter: F = product of (X^2 - sig X + pi) over V(I) is square-free
  -- F is the characteristic polynomial of multiplication by a primitive element.
  -- Construct F via elimination: in QQ[X,sig,pi] / I, take resultant wrt a lex order.
  RX := QQ[X, sig, pi, MonomialOrder => Lex];
  IX := sub(I, RX);
  quad := X^2 - sig*X + pi;
  -- eliminate sig,pi from I + (quad): the X-resultant of a 0-dim complete intersection
  -- Use: groebner basis of IX + (quad) and read the univariate in X.
  G := gens gb(IX + ideal(quad));
  -- the elimination ideal in X is generated by a degree-2N polynomial
  FX := 0_(QQ[X]);
  scan(flatten entries G, g -> (
    if g != 0 and degree(sig, g) <= 0 and degree(pi, g) <= 0 then FX = sub(g, QQ[X]);
  ));
  if FX == 0 then (
    << "idp: OPEN could not extract parameter polynomial F(X)" << endl;
    return false;
  );
  dFX := diff(FX, (QQ[X])_0);
  if gcd(FX, dFX) != 1_(QQ[X]) then (
    << "idp: FAIL reused parameter / triple fibre (F not square-free)" << endl;
    return false;
  );
  << "idp: PASS length=" << N << " reduced, distinct tangents, no reused parameter" << endl;
  true
);

-- self-test positive witness (does not solve a realization ideal)
Kt = QQ[t];
r = t^3 + t + 1;
q = t^4 + (2/3)*t^2 + (4/3)*t;
p = r^2;
assert(idpPostcheck(p, q, 3));
-- self-test negative
assert(not idpPostcheck(t^8, t^6, 11));
<< "=== idp_postcheck self-tests completed ===" << endl;
```

## 13. Verification manifest, SHA-256 table, and verdict rules

Hash convention: SHA-256 of the extracted fence body as UTF-8 POSIX text with exactly one trailing newline (the bytes of the job file as generated). Coordinator re-hashes after extraction.

| file | bytes | SHA-256 | expected output |
|---|---:|---|---|
| `type86_A.ms` | 462 | `1b3e8ffa5c8dc814ceda55f02d7f46e23c6bad15222998737245697c9e2d716f` | EMPTY ⇒ type (8,6,11) not a polynomial curve; NONEMPTY ⇒ `idp` `N=11` |
| `type86_A.m2` | 2302 | `4f5d5692804f4ffeb2a1154705487cb31b95898c76a3803c5579db00f5e52184` | same, after colon+`Res` |
| `type86_B.ms` | 625 | `2de11fe3d4b02c3c20ab8650566172baf808fb3c228aaaefbbf3317cc76515e4` | EMPTY ⇒ no first-odd-remainder 9; NONEMPTY ⇒ `idp` `N=10` |
| `type86_B.m2` | 2468 | `6744477c5d53afca6f8e2407a5c3fdde34536894e419805c807d84a91cb3c57b` | same |
| `type86_C.ms` | 757 | `5a63cf30f226275174524ac49f74d1c232a19c82e381f837276049e7dea52dfc` | EMPTY ⇒ no first-odd-remainder 7; NONEMPTY ⇒ `idp` `N=9` |
| `type86_C.m2` | 2615 | `b7dfda9dcff27a46eda6e8cd6914a8d50ab9cfdc03d5949f17217eb6053f3091` | same |
| `type86_D.ms` | 890 | `f6a2f37c578981f4daf0ef7c1f22dc854921937c3823caab725cc97a0d96c29a` | EMPTY ⇒ no first-odd-remainder 3; NONEMPTY ⇒ `idp` `N=7` |
| `type86_D.m2` | 2782 | `da0b661a74de6103406d5a9994b03bf37abe7b5e70ad8827729429c59fb4b611` | same |
| `type96_A.ms` | 500 | `74a18f92926e0adf0adaa5614bc6bed8986a7e15eb675c84f4959f4d48aad300` | EMPTY ⇒ no remainder degree 4; NONEMPTY ⇒ `idp` `N=6` |
| `type96_A.m2` | 2234 | `f32b8f1cb1e656437ed61f199b84cf8fa132c6571dcbe02ff08c3fe2d7e11345` | same |
| `type96_B.ms` | 515 | `c5836ffc89f0d2b41209e86acd26e058f0825970c5cc9cb0356ee7214914406a` | EMPTY ⇒ no remainder degree 2; NONEMPTY ⇒ `idp` `N=4` |
| `type96_B.m2` | 2271 | `bd26670347544de75a9ed267724f06b52ede2f0a9becca2d562cfe6eb73ec0b2` | same |
| `control_pos_643_idp.ms` | 37 | `42080d1da9853205e90f2a9545fd95ecde442b0353b1927734d2ead1f1b11ace` | nonempty 0-dim, 3 solutions; FAIL aborts |
| `control_pos_643_idp.m2` | 792 | `70b86bad8fcf0790a1ca444618e898e2138a5ee3ba187b44ab8bb57e79d1b4bd` | `dim=0`, `degree=3`, radical; FAIL aborts |
| `control_neg_t8t6.ms` | 108 | `553021d807c8494e0fe82e1871fec58ce34b170149718acb6c996cc839eab655` | not EMPTY, not 0-dim; FAIL aborts |
| `control_neg_t8t6.m2` | 870 | `a71ab17a4bfbb6a7a0817d59b4cda98d742b2cf2f005857742ba2e989fe55346` | `deg gcd(p',q')>0` and `dim I_DP≥1`; FAIL aborts |
| `idp_postcheck.m2` | 5470 | `5186ed7d73b0fb719286b57543652d584fdfb63fee4c304fb44822130d8f5f6b` | self-test PASS on witness, reject `(t^8,t^6)` |
| `run_realization_suite.sh` | 7080 | `ce9c3a76e429e38efab5619f25bd9221ee9a317c93494beafdf5be5634145a86` | controls then six types; needs `REALIZATION_AWS=1` |

Verdict summary (charged §9, unchanged by this lane): NONEMPTY is not REALIZED; EMPTY of the open characteristic ideal is NON-REALIZABLE as a polynomial curve of that type. A type becomes REALIZED only after a closed point passes reduced `I_DP` of length `δ_aff` with distinct tangents and no triple fibre. TIMEOUT is not a mathematical verdict.

## 14. Ambiguities, OPEN items, and coordinator notes

Places the charged spec was not unique; this bundle does not guess a theorem in those slots.

1. **`h_23` and `k_17` are identically zero** in the charged Tschirnhausen charts. msolve rejects a zero polynomial. They are omitted from the inputs and recorded as identities in §2. If a later chart reintroduces `t^{d-1}` or the killed `q`-coefficient, restore them.

2. **Cover encoding is not unique.** Charged text lists (i) `p,q∈ℂ[t^2]` after a linear change of `t`, (ii) in-chart even/even-odd loci, (iii) `gcd(p',q')` of degree `>1`. These are related, not equal. This bundle: in-chart cover as an explicit colon (`(B,D,F,gam,e)` on (8,6); `(P6,P4,P2,Q3,Q1)` on (9,6)); immersive open as `Res(p',q')≠0` computed in M2. General quadratic covers that survive Tschirnhausen are intended to be hit by the resultant, not by (i). **OPEN:** resultant not expanded into msolve (Sylvester 12×12 in 11 coefficient variables; size not desk-checked). msolve jobs therefore do *not* exclude covers; post-filter with `idp_postcheck` / M2.

3. **Rabinowitsch slacks for a multi-generator cover** would add free `w_i` and destroy 0-dimensionality. Not used in msolve files. Colon on the M2 side is the charged alternative.

4. **Positive control format.** Charged: `(6,4,3)` `I_DP` length 3 reduced, ROW-SWEEP §2 witness. This is *not* a characteristic ideal in the (8,6) chart. No Tschirnhausen system for `(6,4,3)` is written (that would be a different ring). **OPEN:** if the coordinator wanted a characteristic-style (6,4,3) msolve file, it is not in this bundle.

5. **Optional gauges** `f=0` and `gam=1` on `gam≠0` are named in the charged ring comment and are not imposed. Case `gam=0` is not the full cover (needs `e=0` and odd `p` too).

6. **Closed-point extraction** from a positive-dimensional NONEMPTY component is not automated. A random linear slice is **OPEN** (would be an extra AWS job, not specified).

7. **FSY Lemma 1 / `g_2` coordinates** for `{6,8,3}` are equivalent as a finite problem and are not duplicated. Moh JRAM 340 was not obtained (charged lead only).

8. **`(9,6,2)` involution slice** (`q∈ℂ[t^2+at+b]`) is a closed subscheme of `type96_B`, not a seventh job.

9. **`idp_postcheck.m2` wronskian conversion** (`degree(s,Wred)`, remainder in `QQ[s,sig,pi]`) was not executed. If M2 rejects it, keep dim/degree/radical/immersive tests and treat the tangent clause as OPEN; the charged (6,4,3) tangent factors `9sig^2+4` and `3sig^2+4` remain the positive-control check.

10. **Negative-control M2** uses `degree g > 0` on `gcd(p',q')`. If a given M2 version returns an empty degree list for a non-unit, replace by `g != 1`. The msolve negative input does not depend on that.

11. **M2 `use St` after `R0[symbol t]`** can shadow coefficient names; scripts use distinct names (`B,gam,…`). If `resultant` does not land in `R0`, the `assert(ring res0 === R0)` fails loudly (desired).

12. **No CAS of uncertain duration was run on this machine.** Coefficient expansion was finite binomial multiplication with weighted-degree checks. Groebner, msolve, and `dim`/`degree` of the six ideals are AWS-only.

Launch recipe: extract the 18 fenced files into one directory; `chmod +x run_realization_suite.sh`; on the AWS box, `REALIZATION_AWS=1 ./run_realization_suite.sh`. Re-hash extracted files against §13 before launch.

<!-- BODY-END -->
