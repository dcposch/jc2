# Hostile audit: Opus cutoff-two full-fixture reduction

Date: 2026-08-28  
Reviewer: Sol Ultra, independent exact lane  
Charged report:
`xmodel/ggv-upper-endpoint-tail2-fullfixture-ideation-opus5-20260828.md`  
Charged SHA-256:
`4facfc4a960eeefe0bd2aa5f1aeded26757fad417ff6e1c80c3bc2b047f10ab6`

## Verdict

**FAIL AS AN EXACT REDUCTION; substantial salvageable core.**

The report's central Theorem D is false.  Over `K[X]_A[[t]]`, the complete
characteristic solution through weight 21 has not five but nine post-head
even modes:

```text
F^(3/2)
+ c4  t^4  F
+ c6  t^6  F^(3/4)
+ c8  t^8  F^(1/2)
+ c10 t^10 F^(1/4)
+ c12 t^12
+ c14 t^14 F^(-1/4)
+ c16 t^16 F^(-1/2)
+ c18 t^18 F^(-3/4)
+ c20 t^20 F^(-1)                         (mod t^22).
```

The four negative-power constants are not free polynomial kernels, but they
cannot be deleted: polynomial-window conditions at weights 14, 16, 18, and
20 can force them to unique **nonzero** values.  This is not a hypothetical
possibility.  A one-variable mutation along the report's own exact
`F8[X^0]` gauge gives a literal raw counterexample to Theorem D.

Consequently the report's `Phi_22`, which retains only the first five free
modes, is not in general the characteristic deficit of the raw system.
Theorem E's endpoint differential identity and its closed antiderivative are
correct only after `Phi_22` is replaced by the coefficient of the **full**
nine-mode continuation.  Its at-least-three exact order-five pole corollary
then survives.

The following substantial pieces pass independently:

- reconstruction of all 303 variables and all 513 frozen generators;
- the two additive gauges;
- the `R_n` absorption identity and same-row cancellation of `F_n`;
- the count of five **free polynomial** modes;
- the endpoint sign and antiderivative;
- the at-least-three order-five pole statement for the corrected endpoint
  coefficient;
- the polynomial transport identity
  `2G E(F,G)=E24(F,G^2-F^3)` and its triangular converse.

No endpoint point or exclusion, cutoff-two field classification, other GGV
branch, Keller-pair, or JC2 conclusion follows from this audit.

## 1. Custody and independent computation

The charged bytes and raw source recompute to

```text
4facfc4a960eeefe0bd2aa5f1aeded26757fad417ff6e1c80c3bc2b047f10ab6
  xmodel/ggv-upper-endpoint-tail2-fullfixture-ideation-opus5-20260828.md

ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
```

I used a fresh standard-library checker, not the producer's scratch code.
Its polynomial type was

```text
(X-degree, sorted raw-variable monomial) -> Fraction,
```

with independently written addition, multiplication, differentiation, and
row assembly.  It rebuilt `A,H,F0,...,F14,G0,...,G21` from the raw window
registry and the displayed fixed head.  Exact output was

```text
SOURCE_RECONSTRUCTION 303 513 PASS
GAUGES ['f_0_0', 'g_0_0']
ABSORPTION rows=1..22 PASS
FORCED_NEGATIVE_MODE c16=-3/8 rows4..21=0 actual_D22=0 PASS
GAUGE_ONLY_FORCED_NEGATIVE_MODE c8=-3/2 c16=3/8 PASS
ENDPOINT_TRANSFER symbolic_identity PASS
ENDPOINT_ANTIDERIVATIVE PASS
ROOT_POLES at_least_three_order5 PASS
QUADRATIC_TRANSPORT identity_and_triangular_reverse PASS
```

No CAS, floating point, AWS computation, or specialized tail exclusion was
used.  The calculation did not access `jc2-lean` and did not edit any case or
canonical ledger.

## 2. Source reconstruction and gauges: PASS

Fresh expansion of

```text
D_n=sum_(i+j=n)((12-j)F_i'G_j+(i-8)F_iG_j')
```

gave zero identically in rows 0 through 3.  In rows 4 through 21 every
coefficient, monomial, and sign equalled the corresponding frozen generator.
At row 22 the only difference between the mathematical `D22` and the frozen
generator list was the expected constant `-1` in X-degree zero.  The counts
were independently recovered:

```text
rows D4..D21: 495 generators,
row D22:       18 generators,
total:        513 generators;

z,tt:          17 variables,
F4..F14:       79 variables,
G4..G21:      207 variables,
total:        303 variables.
```

The fixed head printed in §1 of the report, including the constant `1/8` in
`G3`, is exact.  The raw slot dictionary and the endpoint coefficient

```text
D22[X^0]-1=-1-f_0_1*g_1_0+f_1_0*g_0_1
```

also pass.

Scanning literal monomial support gives exactly

```text
{f_0_0, g_0_0}={F8[X^0],G12[X^0]}
```

as variables absent from every generator.  Translation in either coordinate
is therefore a genuine scheme-level `G_a` symmetry, and setting both to zero
is a global additive slice.  The effective raw variable count `303 -> 301`
is correct.  Importantly, the `F8[X^0]` symmetry is also the cheapest
falsifier of the later five-mode claim; gauge invariance of the determinant
does not mean invariance of a truncated characteristic-coordinate choice.

## 3. The `R_n` absorption identity: PASS

Put

```text
R_n=G_n-(3/2)H F_n,
P_n=sum_(i+j=n, i,j>=1)F_iF_j.
```

Fresh symbolic expansion verifies, for every `1<=n<=22`,

```text
D_n = L_n(R_n)
    + sum_(i+j=n, i,j>=1)
        ((12-j)F_i'R_j+(i-8)F_iR_j')
    + 3H P_n' + (3/4)(n-16)H'P_n,

L_n(R)=2H((12-n)H'R-4HR').
```

The apparently exceptional value

```text
R_0=G_0-(3/2)HF_0=-(1/2)H^3
```

is exactly what cancels the same-row `F_n` contribution.  The remaining
`F_n` coefficient is zero, so `F_n` first constrains the following row.

Multiplication by `H=A^2` sends every literal `F_n` window into its `G_n`
window, including the positive lower cutoffs at later weights.  Therefore

```text
(F_n,G_n) -> (F_n,R_n)
```

is indeed a triangular linear automorphism of the raw affine coordinate
space.  No localization or carrier chart is hidden in this step.

## 4. Fatal omission in Theorem D

For fixed `F`, subtract two rational characteristic solutions whose first
difference is at weight `m`.  The difference satisfies

```text
L_m(h_m)=0,
h_m=c_m F_0^((12-m)/8)=c_m A^((12-m)/2).
```

Odd `m` gives a half-integral power of the squarefree polynomial `A` and no
nonzero element of `K(X)`.  But **every even `m`** gives a rational element of
`K[X]_A`, including

```text
m=14: A^-1,
m=16: A^-2,
m=18: A^-3,
m=20: A^-4.
```

Equivalently, direct substitution gives

```text
E(F,t^m F^((12-m)/8))=0
```

for those four negative powers exactly as for the five positive powers.
Thus the charged sentence “over `K[X]_A[[t]]` these span the general
solution” is already false in its stated localized ring.

The correct distinction is:

- `c4,c6,c8,c10,c12` are free because their birth coefficients are
  polynomial and lie in the raw windows;
- `c14,c16,c18,c20` are not free raw kernels, because their birth
  coefficients are polar;
- nevertheless, a raw polynomial solution can require unique nonzero values
  of the latter constants to cancel poles accumulated from earlier modes.

The raw kernel census `1,0,1,0,1,0,1,0,1,0,...` therefore confirms only the
five-dimensional **free polynomial kernel**.  It does not license truncating
the rational continuation.  The pinned
`CHARACTERISTIC_CROSSCHECK.md` states precisely this firewall, but the
failure below is independently reconstructed from the raw system.

### 4.1 Literal gauge-only counterexample

Let

```text
U=A^2+t/2,
F=U^2+t^8,
G=U^3                         (through weight 21).
```

This is the raw assignment

```text
f_0_0=1,
every other one of the 303 raw variables=0.
```

Since `f_0_0` is absent from every determinant generator, direct evaluation
of the frozen JSON gives

```text
D4=...=D21=0,
D22=0
```

(the only nonzero frozen generator value is the folded target `D22-1=-1`).

Now expand exactly, writing `x=t^8/U^2`:

```text
F^(3/2)=U^3(1+x)^(3/2),
F^(1/2)=U(1+x)^(1/2),
F^(-1/2)=U^-1(1+x)^(-1/2).
```

Through weight 21,

```text
U^3
 = F^(3/2)
   -(3/2)t^8 F^(1/2)
   +(3/8)t^16 F^(-1/2)          (mod t^22).
```

Hence this literal raw solution has

```text
c8=-3/2,
c16=+3/8,
all other c_m through 20 zero.
```

The five-mode formula first forces `c4=c6=c10=c12=0` and `c8=-3/2` from
weights 4, 6, 8, 10, and 12.  At weight 16 it then leaves

```text
-(3/8)U^-1[X,t^0]=-3/(8A^2),
```

whereas the literal raw `G16` is zero.  Only `c16=3/8` cancels it.  This is
a field-valued, cover-free, source-replayed counterexample to Theorem D.

For a sign mutation, another literal solution is

```text
F=U^2+t^8,
G=U^3+(3/2)t^8U,
```

whose only additional raw slots are

```text
g_0_4=3/2, g_4_16=-3, g_8_28=3/2, g_0_3=3/4.
```

It also has `D4=...=D21=0,D22=0`, but requires `c16=-3/8` with all five free
modes zero.  Both signs of a forced negative mode therefore occur on simple
literal raw points.

## 5. Consequence for the endpoint object

Let `widehat(Phi)_22` denote the weight-22 coefficient of the full
continuation using modes through `c20`, but no new `c22` kernel.  Because the
raw fixture has neither `F22` nor `G22`, the deficit identity is

```text
D22_raw=-L22(widehat(Phi)_22).
```

The report's displayed coefficient must be repaired to

```text
widehat(Phi)_22
 = (F^(3/2))_22
 + c6  (F^(3/4))_16
 + c8  (F^(1/2))_14
 + c10 (F^(1/4))_12
 + c14 (F^(-1/4))_8
 + c16 (F^(-1/2))_6
 + c18 (F^(-3/4))_4
 + c20 (F^(-1))_2.
```

The `c4` and `c12` terms still drop for the reasons given in the report.

The gauge-only point exposes the failure of the truncated endpoint object
numerically.  Omitting its required `c16=3/8` leaves

```text
Phi_22^(five-mode)=-3/(512 A^14),
```

because `[t^6]U^-1=1/(64A^14)`.  The omitted term contributes
`+3/(512A^14)` and makes the correct `widehat(Phi)_22=0`, as required by its
literal `D22=0`.  Thus the charged equality

```text
D22=-L22(Phi_22)
```

is false for its defined five-mode `Phi_22` even on this elementary raw
point.

### 5.1 Endpoint sign and closed form after repair: PASS

For every rational `R`, direct differentiation gives

```text
-A L22(R)=8(A^5R)',
L22(R)=-8A^3(5A'R+AR').
```

Therefore, with the corrected continuation,

```text
D22=1
  <=> A^5 widehat(Phi)_22=X^5/40-X/8+gamma,
      gamma in K.
```

The sign and normalization are exact because

```text
8(X^5/40-X/8+gamma)'=X^4-1=A.
```

This is a useful structural reduction, but it is not the explicit endpoint
formula in 96+5 variables claimed by the report until the four forced
constants have been correctly reconstructed.

### 5.2 At least three exact order-five poles: PASS after repair

Put

```text
N=X^5-5X+40gamma.
```

At any geometric root `rho` of `A`,

```text
N(rho)=-4rho+40gamma.
```

A single `gamma` cannot equal `rho/10` for two distinct fourth roots, over
any characteristic-zero coefficient field after algebraic closure.  Hence
`N` is nonzero at at least three roots.  At each such root,
`widehat(Phi)_22=N/(40A^5)` has exact pole order five.  This conclusion does
not require the report's extra qualification about which roots already lie
in `K`.

At a possible exceptional root the numerator has exactly a double zero,
because `N'=5A` and `A'(rho)!=0`; the local pole order is then three.  This is
consistent with, and sharpens, the stated at-least-three result.

## 6. Polynomial transport: PASS, independently of Theorem D

For `Xi=G^2-F^3`, direct product-rule expansion gives

```text
E24(F,G^2)=2G E(F,G),
E24(F,F^3)=0,
2G E(F,G)=E24(F,Xi).
```

Coefficientwise,

```text
[t^n]E24(F,Xi)
  =2A^6D_n+2sum_(i=1)^n G_iD_(n-i).
```

Since `A^6` is a nonzero monic polynomial, induction gives the converse as
well as the forward implication.  Thus the charged raw system is exactly
equivalent to

```text
[t^n]E24(F,Xi)=0       for n<22,
[t^22]E24(F,Xi)=2A^6,
Xi=G^2-F^3.
```

This proof uses no characteristic expansion and survives the failure of
Theorem D.  The same-weight operator

```text
-8A^(4+b_n)(Xi_n A^(-b_n))',
b_n=(24-n)/2,
```

and `Xi_0=Xi_1=Xi_2=0` also check exactly.

If a machine introduces `Xi` as an independent variable, however, it must
retain the defining cubic equations `Xi=G^2-F^3`; the transport rows alone
are only a larger projection.  The special formula in §6 also uses an
undefined `delta`.  On its stated all-nonbaseline-modes-zero locus, exact
comparison with the endpoint constant is

```text
Xi_22=-2A^6 widehat(Phi)_22
     =-(A/20)(X^5-5X+40gamma),
```

so the printed version is correct only after declaring `delta=-2gamma` and
interpreting `c_*=0` as all nonbaseline modes, including forced negative
ones.

## 7. Bookkeeping: what survives

The number of free raw data remains

```text
7 z-coefficients + 10 T-coefficients + 79 F-slots + 5 free modes = 101.
```

The four negative constants do not add free dimensions: at their birth rows
the polynomial kernel is zero, so a raw solution, if it exists, determines
them uniquely.  They must nevertheless be carried as derived scalars.

The linear same-row ranks independently give 293 compatibility equations:

```text
16,15,16,15,16,15,16,15,16,16,16,16,17,17,17,18,18,18
```

at rows 4 through 21.  The 47 row-4/5/6 contractions are vacuous on the
fixed head, leaving 246 nonvacuous compatibility expressions.  These counts
survive.  What fails is their advertised encoding by the truncated
five-mode algebraic family.

## 8. Cutoff-five comparison: direct import fails; survival is open

The report correctly establishes the following narrower facts:

- there is no all-linear raw prefix at cutoff two;
- the literal cutoff-five prefix coordinates and its `V0` variable cannot be
  imported unchanged;
- the first local Newton polygon is altered by the nonzero `F2(rho)=1/4`;
- the discriminant identity
  `F1^2-4F0F2=-A^6Z` is exact;
- the endpoint determinant and additive gauges transfer.

It does **not** establish that the two-branch mechanism “fails, not splits,”
or that root/`gamma` data replaces every later scalar branch.  Absence of an
initial linear prefix does not prevent nonlinear radical descent from
producing a transported core.  Indeed, the independently frozen cutoff-four
analysis later obtains

```text
R0*(b*R0+U0^2)=0
```

at `D18`, explicitly the cutoff-five two-branch invariant shifted by one
tail mode.  That cutoff-four result is not used anywhere above; it is a
counterexample only to the report's broad strategic wording.  For cutoff
two the honest status is:

```text
literal prefix/core import: rejected;
emergence of an analogous post-cascade branch: unresolved.
```

## 9. Proposed `INEQ`: still a conjecture, and the plan is incomplete

The report labels

```text
v_rho(c_22)>=v_rho(c_21)-2
```

as heuristic rather than proved, so it is not a false theorem claim.  The
Newton scaling for a `W^k` mode,

```text
lambda^(24-3k-2n),
```

is correct.  But the proposed proof plan lists only `k=1,2,3,4` submodes and
omits the forced modes

```text
k=-1,-2,-3,-4
  <-> m=14,16,18,20.
```

After factoring the dominant `k=6` scale, these enter with additional
orders `21,24,27,30`.  Those orders are close enough to the target value
`v(c_22)=33` to participate in exactly the cancellations the inequality must
control.  The gauge-only counterexample shows that such a cancellation is
real even in the simplest homogeneous raw family.

Moreover, high valuation of one coefficient can arise from cancellation of
modes rather than a uniform lower bound on each algebraic branch.  No
adjacent-coefficient valuation inequality follows merely from the first
infinite binomial term.  A valid successor must first rebuild the complete
nine-mode local recurrence and then either prove `INEQ` for the **sum** with
all forced constants, or produce a mutation.  The present heuristic is not
downstream evidence and should not drive an exclusion claim.

## 10. Required repair and promotion firewall

Before any part of the claimed cutoff-two reduction is consumed downstream:

1. replace Theorem D by the nine-mode continuation;
2. serialize how raw polynomiality uniquely determines
   `c14,c16,c18,c20`, including lower-window conditions;
3. replace every `Phi_22` by `widehat(Phi)_22` with the four missing terms;
4. replay the literal gauge mutation `f_0_0=1`, which must return
   `c8=-3/2,c16=3/8` and `widehat(Phi)_22=0`;
5. retain `Xi=G^2-F^3` in any transport compiler;
6. weaken “the cutoff-five mechanism fails” to the precise unresolved
   statement above;
7. reformulate `INEQ` with all nine modes before testing it.

Until those repairs and a new independent review, the report must not be
promoted as an exact reduction.  The source reconstruction, gauges,
absorption identity, corrected endpoint differential/pole theorem, and
quadratic transport may be promoted separately at their stated scopes.
