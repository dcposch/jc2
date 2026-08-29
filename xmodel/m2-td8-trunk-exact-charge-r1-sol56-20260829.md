# `td=8` equal-join trunk: exact exit charge is at least three

Author: Sol 5.6 primary desk-algebra lane. Date: 2026-08-29 UTC.
Lifecycle: `PRODUCER_CHECKED`; different-model hostile review required.

## 0. Result

**Theorem (`TD8-TRUNK-EXIT-GE3`).** On every member of the reviewed affine
equal-join family, let `F` be the `(85,35)` trunk and let `c_*` be a root in
its unique extra orbit (the reduced multiplicity-two orbit). Let
`E_F(c_*)` be the set of distinct critical-value flags in that
first-separation exit subtree. Then

```text
lambda_F^exit(c_*)
  := sum_{H in E_F(c_*)} kappa_H (pi(H)-1)  >= 3.              (0.1)
```

In particular, the exact trunk exit charge is **never 2**. This is an
arity/additivity obstruction, not a new coefficient calculation.

Consequently the entire reviewed `td=8` affine equal-join route is killed at
the actual-weight budget tier, uniformly for every `t>=0`: the two A-exits
cost at least `2+2`, the merge costs `0`, and the trunk costs at least `3`,
whereas the reviewed x-side reserve leaves y-side budget `6`.

The apparent charge-two trunk profile in the reviewed exact-separation report
is a correct **per-ray** calculation but not a charge-two **exit-set**
calculation. Its drop `2i -> i` creates a second, non-remerging subtree and
hence at least two distinct cv flags; both must be added.

This excludes this affine formal route. It proves no global `td=8` exclusion,
degree ceiling, source landing theorem, counterexample, or JC2 conclusion.

## 1. Exact dependencies and custody

Full SHA-256 values recomputed in this lane:

```text
910d3216ad7476b743eb920e3d68026f05efc8ffe1a409c476fb90ce277f6ad4
  xmodel/m2-td8-equal-join-st39-coefficient-transport-primary-fable5-20260829.md
e469e94dbf4393fe820345678c2582ca7f7a528695c25d065fb224b4f796cf61
  xmodel/m2-td8-equal-join-st39-coefficient-transport-primary-hostile-review-opus5-20260829.md
991e1b350ad2f8b2b82808fdc84dec71154f9ae17250c18953a36ac8f6588508
  xmodel/m2-td8-first-extra-jet-exact-lambda-primary-opus5-20260829.md
ec3557953c6387ce35dcf4efe1df267fb828771119c479eb00c8f1793e0ee370
  xmodel/m2-td8-first-extra-jet-exact-lambda-primary-hostile-review-fable5-20260829.md
2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933
  xmodel/sigray-section9-source-audit-sol-ultra-20260828.md
0729a5765729a9e3a6f99720a638cc94a3d3a7837e3946412e13c4233e6b5bad
  xmodel/sigray-section9-source-audit-hostile-review-gpt55-20260828.md
c253bd12d205eed7c01e42a21204c5735d0f5cba70dce1d962fb8744dbd95eb6
  xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md
727f58506af4ff36f6a8c39bb83420c5077c2e4872e6e48bd42ec165c2323aa8
  xmodel/sigray-section7-weighted-euler-inequality-hostile-review-terra-20260828.md
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
  refs/sigray_full.pdf
```

Printed source re-read directly: Definitions 3.1--3.4, Proposition 3.1,
Statements 3.9--3.18 (printed pp. 10--18); Notation 7.1, Statements 7.1--7.3,
Propositions 7.3--7.5 and Corollary 7.1 (pp. 34--39); Notations 9.1--9.3 and
Statements 9.3--9.4 (pp. 48--50). The corrected sign in (24), the
first-separation replacement for the nested literal `Y(F)`, and the
actual-weight version of Corollary 7.1 are used only at their separately
reviewed campaign tier listed above.

No web, AWS, CAS, long computation, canonical edit, commit, or push was used.
Only this report was written.

## 2. Frozen trunk data

The reviewed coefficient transport pins, for `t>=0`,

```text
i := i_F = 112+84t = 28(4+3t),
D_F = 17i,
kbar_F = kappa_F(1-pi(F)) = 7,
mult(p_F,c_*) = 2i.
```

The last equality follows because the reduced trunk pattern is

```text
Phi=(eta^17-A)^3(eta^17-B)^2,       B=(4/3)A,
p_F=C Phi^i,
```

and `c_*^17=B`. Thus the corrected Statement 9.3 gap for **every** cv flag
`H` reached through this one extra direction is

```text
D_F/mult(p_F,c_*) - kbar_F = 17i/(2i)-7 = 3/2.       (2.1)
```

The reviewed integrality upgrade gives

```text
w_H := kappa_H(pi(H)-1) in N*                         (2.2)
```

for every such `H`. Therefore (2.1)--(2.2) already imply `w_H>=2` for
each distinct flag. What remained unnoticed is that the local exit charge is
the **sum** of these weights, not the weight of one selected ray.

## 3. The arity dichotomy

Let `B_*` be the `2i` Puiseux series of the fibre `f=a` which pass through
the child direction `F*c_*` (Proposition 3.1 and Statement 3.9(i)). For each
`P in B_*`, Statement 7.3 and uniqueness of the zero of `d_{I_P(u)}` give a
cv flag `H(P)`. Let

```text
E_F(c_*) := {H(P): P in B_*}.
```

This is precisely the portion of the repaired first-separation exit set owned
by the trunk extra direction. The Eggers--Wall object is a tree: divergent
directions never remerge. Hence a later split of `B_*` produces distinct
elements of `E_F(c_*)`; none may be discarded merely because both groups
started at the same reduced root orbit.

There are two cases.

### Case A: at least two cv flags

If `r:=|E_F(c_*)|>=2`, apply (2.1)--(2.2) to each flag and add:

```text
lambda_F^exit(c_*) = sum_H w_H >= 2r >= 4.             (3.1)
```

This includes the exact-separation report's proposed profile
`N: 2i -> i` at normalized time `tau=8`: the two size-`i` groups lie in two
non-remerging subtrees, so the displayed per-ray value `2` occurs at least
twice. It is not a total charge of `2`.

### Case B: exactly one cv flag

Assume `E_F(c_*)={H}`. Since separated Puiseux series cannot remerge, all
`2i` series agree strictly below the common cv level. In the reviewed exact
descent notation

```text
tau := kappa_F(u-pi(F)),
N(tau) := deg p_{I_P(u)},
tau_0 := kappa_F(pi(H)-pi(F)),
```

we therefore have `N(tau)=2i` on `(0,tau_0]`. The exact area identity gives

```text
17i = integral_0^tau_0 N(tau) d tau = 2i tau_0,
tau_0 = 17/2.                                          (3.2)
```

The exact separation law now reads

```text
w_H = (kappa_H/kappa_F)(tau_0-kbar_F)
    = (kappa_H/kappa_F) * 3/2.                         (3.3)
```

The reviewed denominator/conjugacy argument proves
`q:=kappa_H/kappa_F in N*`. By (2.2), `3q/2` is an integer; hence `q` is
even and `q>=2`. Equations (3.2)--(3.3) yield

```text
lambda_F^exit(c_*)=w_H>=3.                             (3.4)
```

Combining (3.1) and (3.4) proves (0.1). More precisely, the only two
possibilities relevant to the lower bound are

```text
one unsplit cv flag:  charge >=3 (a denominator jump is forced),
two or more flags:    charge >=4 (additivity is forced).
```

Thus the trunk cannot realize the integer rounding `ceil(3/2)=2`: the
mechanism that raises a selected ray from `3/2` to `2` also raises the arity.

## 4. Uniform route kill

Each reviewed A-copy has one alternative direction with corrected gap

```text
14/2-5=2,
```

so choose one cv flag from each A-exit; each has weight at least `2`. Choose
all flags in the trunk exit set, whose total weight is at least `3` by the
theorem. These three exit subtrees are pairwise disjoint in the y-tree, and
the reviewed x-side `psi=1` flag lies in the other component. Therefore the
selected distinct cv flags have total actual weight at least

```text
2+2+3+1=8.
```

The reviewed actual-weight Corollary 7.1 says, for `td(f,g)=8`, that every
set of distinct cv flags has total weight at most `td-1=7`. Contradiction.
Equivalently, after reserving the x-side unit, the y-side exit budget is `6`,
but the two A-exits plus trunk already cost at least `7`.

No A-side contact calculation, trunk subtop coefficient, affine-parameter
specialization, or source landing assumption is needed. The kill is uniform
in `t`.

## 5. Exact repair to the reviewed separation report

The exact descent law, its trunk criterion for a **fixed selected ray**, and
the area calculation in the Opus primary/Fable review remain correct. The
false consumer step is identifying that selected-ray quantity with the whole
local exit charge.

Replace

```text
"Delta_trunk=2 iff kappa_H=kappa_F and tau_0=9"
```

when used as a budget statement by

```text
For one selected H, that equivalence is valid.  For the trunk exit set,
lambda_trunk^exit>=3.  The proposed tau=8 split gives at least two distinct
H's and therefore lambda_trunk^exit>=4.
```

Accordingly, the reviewed theorem claiming survival iff three displayed
per-ray charges equal `2` must be withdrawn for this family. The corrected
budget conclusion is `ROUTE_KILLED_BY_TRUNK_ARITY`.

## 6. Review risks and exclusions

A hostile reviewer should check, in this order:

1. that every cv flag produced after a later split of the same extra root
   orbit belongs to the trunk's repaired first-separation exit set;
2. that tree non-remerging makes `|E_F(c_*)|=1` equivalent to retention of
   all `2i` series through the common cv level;
3. that corrected Statement 9.3 applies separately to every `H` in this
   exit subtree with the same full multiplicity `2i`;
4. that `kappa_H/kappa_F` is a positive integer in the single-flag case and
   that the printed-proof integrality (2.2) is available at the promoted
   tier;
5. that the two A-exits, the trunk exit, and the x-side flag are pairwise
   distinct for the actual-weight Corollary 7.1 application.

This report does not claim that the lower bound `3` is attained. It does not
analyze other `td=8` route families, repair all consumers of literal nested
`Y(F)`, construct a polynomial pair, or settle JC2.

---
Report-body SHA-256 (all bytes before the separator line above):
`688dbf41e3e3b6c777ec7267c8114569c4507261eb6dea9003dc6236c330494c`.
