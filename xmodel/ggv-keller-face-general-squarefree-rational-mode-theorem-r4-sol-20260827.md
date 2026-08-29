# General-squarefree Keller-face rational modes, with perfect-square stop

Date: 2026-08-27  
Author lane: Sol, `actual_total_g20`  
Status: **EXACT PRODUCER THEOREM / PROVISIONAL PENDING HOSTILE REVIEW /
NONSQUAREFREE STAGE STOPPED AT A WEIGHT-22 RESONANCE**

## 0. Decisive result

The reviewed R3 rational-mode proof does not use `H=X^8-1` until its final
degree calculation.  It transports verbatim to every nonconstant squarefree
polynomial `H`.

Let `K` be a characteristic-zero field, let `H in K[X]` be nonconstant and
squarefree, and suppose

```text
F,G in K[X][[t]],       F_0=H^2,       G_0=H^3.        (0.1)
```

For

```text
E(F,G)=12F_XG-8FG_X-t(F_XG_t-F_tG_X),                 (0.2)
```

the complete rational homogeneous list through weight 22 is

```text
weight  0: F^(3/2),
weight  4: t^4 F,
weight  8: t^8 F^(1/2),
weight 12: t^12,
weight 16: t^16 F^(-1/2),
weight 20: t^20 F^(-1),
weight 22: no rational homogeneous mode.               (0.3)
```

In particular, the negative-power modes at 16 and 20 remain mandatory for
every such `H`; they were not special to degree eight.

After subtracting (0.3), any hypothetical jet with
`E=t^22+O(t^23)` has a residual `t^22d` satisfying

```text
-20HH'd-8H^2d'=1.                                     (0.4)
```

The change `g=-8H^2d` always gives the now-audited endpoint

```text
2Hg'+H'g=2H.                                          (0.5)
```

Squarefree denominator provenance further forces `d=-Y/(2H)` with
`Y in K[X]`, and hence

```text
4HY'+6H'Y=1.                                          (0.6)
```

If `deg H>=2`, (0.6) has no polynomial solution.  Therefore:

> **General-squarefree exclusion.**  No polynomial-`X` formal jet satisfying
> (0.1) can have `E=t^22+O(t^23)` when `H` is nonconstant, squarefree, and
> `deg H>=2`.

Degree one is the exact boundary: if `H=aX+b`, then
`Y=1/(6a)` solves (0.6).  This says only that the endpoint obstruction is
silent; it does not construct a polynomial jet.

The requested second stage cannot cross the perfect-square branch.  For
`H=X^2`, weight 22 has the new rational homogeneous mode

```text
r_22=X^(-5),
t^22 F^(-5/4)=t^22 X^(-5)       when F=X^4.            (0.7)
```

Thus a uniform `H=A^2B` transport encounters a charged-weight resonance as
soon as `B` is constant.  Per the stop condition, no general nonsquarefree
mode/provenance theorem is claimed here.

## 1. Custody, history, and additive boundary

The new frozen case is

```text
cases/ggv_keller_face_general_squarefree_modes_r4_20260827/
```

It pins without rewriting:

```text
e752b86b5a8953649a3ce8c55379d18eca2dc1bdc8ab4fcd030c63dd64071823
  cases/ggv_8_28_keller_face_rational_mode_exclusion_r3_20260827/FREEZE.sha256
b1851156c83657fa85eb875df7e191a99fd339bfcb79ca1a752742ddff9f70b7
  xmodel/ggv-8_28-keller-face-rational-mode-exclusion-r3-sol-20260827.md
27fcd25640f62a92c147863e7a8ef8ca4b7b004f05d54450c8d2d8811c97cdc6
  xmodel/ggv-8_28-keller-face-rational-mode-exclusion-r3-hostile-review-grok-20260827.md
1c17b61f00079802b20fc459550eea7bc7b09bcdcc98f27c233bde91cf348968
  xmodel/ideation-20260827T1349Z-opus5.md
d382c21f416afdc150d621506c38076aa4ec2b96e4680c0a938ddd56f06394ed
  xmodel/ggv-superelliptic-endpoint-criterion-hostile-audit-actual-20260827.md
```

History searches for `general squarefree H`, an arbitrary-squarefree
rational-mode theorem, `F^(-5/4)`, and a weight-22 perfect-square homogeneous
mode found no earlier campaign statement.  R3 itself explicitly charged only
`H=X^8-1`; Opus5 left general-`H` mode completeness open.  The present
general-squarefree theorem and the stop example (0.7) are additive.

## 2. Linearization: no degree or root data

Work in `K(X)[[t]]`.  Since `F_0=H^2` and `H!=0`, there is a unique branch

```text
S=F^(1/2)=H+O(t).                                      (2.1)
```

Put `R=G-F^(3/2)`.  The face operator is linear in its second slot, and every
function of `F` has zero Jacobian with `F`; hence

```text
E(F,G)=E(F,R).                                         (2.2)
```

For every integer `n` and rational `gamma`, direct differentiation gives

```text
E(F,t^n F^gamma)
 =t^n F^gamma F_X(12-8gamma-n).                       (2.3)
```

These steps use only `H!=0`, characteristic zero, and the leading square
`F_0=H^2`.  They do not use squarefreeness, `deg H=8`, the roots of `H`, or
the formula `X^8-1`.

## 3. Complete squarefree mode classification

Suppose a residual first appears at weight `n`, with coefficient
`r_n in K(X)`.  Its homogeneous equation is

```text
2H((12-n)H'r_n-4Hr_n')=0,
r_n'/r_n=((12-n)/4)H'/H.                              (3.1)
```

Put `q_n=(12-n)/4`.  At every irreducible factor `p` of squarefree `H`, the
logarithmic residue of the right side is `q_n`, while the logarithmic residue
of a rational function is the integer `ord_p(r_n)`.  Therefore a nonzero
rational solution requires `q_n in Z`.  Conversely, for integral `q_n`,

```text
r_n=c H^q_n,       c in K,                             (3.2)
```

is the complete solution: the quotient has zero logarithmic derivative, and
the constant field of `K(X)` is `K`.

For `0<=n<=22`, integrality occurs exactly at

```text
n=0,4,8,12,16,20.                                     (3.3)
```

At these weights put `gamma_n=(12-n)/8`.  Writing
`F=H^2U`, `U in 1+tK(X)[[t]]`, gives

```text
F^gamma_n=H^q_n U^gamma_n in K(X)[[t]].               (3.4)
```

Thus every leading solution (3.2) lifts to the exact homogeneous mode in
(0.3), and (2.3) says that mode vanishes identically, not merely at its first
coefficient.  Inductively subtracting it proves completeness.  In full,

```text
G = F^(3/2)
  + c4  t^4  F
  + c8  t^8  F^(1/2)
  + c12 t^12
  + c16 t^16 F^(-1/2)
  + c20 t^20 F^(-1)
  + t^22 d + O(t^23).                                 (3.5)
```

The sole use of squarefreeness in this section is the integral-valuation
conclusion in (3.1).  Nonconstancy is also necessary: for constant `H`, the
right side of (3.1) is zero and every weight has a constant rational kernel.

## 4. Endpoint and exact use of squarefreeness

Only `F_0=H^2` enters the coefficient of the first residual `t^22d`, so (0.4)
is independent of the degree and roots of `H`.  Likewise, differentiating
`g=-8H^2d` gives (0.5) for every nonzero `H`; no squarefree hypothesis is
used in that change of variable.

Polynomiality of the original `F,G`, together with (3.4), shows that every
finite denominator of `d` divides a power of `H`.  At a simple root of `H`,
if

```text
d=aH^(-m)+O(H^(1-m)),       m>=2,                     (4.1)
```

the leading term of (0.4) is

```text
(8m-20)aH'H^(1-m).                                    (4.2)
```

No integer `m>=2` makes `8m-20` zero, so regularity of the unit target forces
at most a simple pole.  Since all roots are simple, `Hd` is polynomial.
Writing `d=-Y/(2H)` gives (0.6).

This pole reduction uses squarefreeness twice: the local parameter has
`ord(H)=1`, and one global factor `H` clears all allowed poles.  It uses no
root locations or degree.

Finally let `h=deg H` and `y=deg Y`.  For nonzero `Y`,

```text
deg(4HY'+6H'Y)=y+h-1,
lc(4HY'+6H'Y)=(4y+6h)lc(H)lc(Y).                      (4.3)
```

The coefficient is nonzero in characteristic zero.  If `h>=2`, the image
has positive degree and cannot be the unit.  If `h=1`, only a constant `Y`
can work, and `Y=1/(6H')` does.  Thus degree enters only at this final
yes/no endpoint, not in the rational-mode normal form.

This also agrees exactly with the audited Opus criterion: squarefree `H`
has `A=1`, `B=H`, and `1 in im(N_H)` precisely in degree one.

## 5. Dependency table

| Step | Exact hypotheses used | Not used |
|---|---|---|
| Formal branch `F^(1/2)` | `H!=0`, characteristic not two | squarefree, degree, roots |
| Linearization and (2.3) | differential algebra, weights `(12,8)` | squarefree, degree, roots |
| Rational leading-mode list | nonconstant squarefree `H`, constants of `K(X)` equal `K` | degree, root positions |
| Exact lift of each mode | `F=H^2(1+O(t))`, integral leading `H` exponent | degree, root positions |
| Denominator provenance | polynomial `F,G`, the six exact rational modes | degree, root positions |
| `d=-Y/(2H)` | squarefree `H`, charged target 22 | degree, root positions |
| Endpoint ODE (0.5) | only (0.4) and `H!=0` | squarefree, degree, roots |
| `M_H(Y)!=1` | characteristic zero and `deg H>=2` | squarefree beyond the prior reduction, root positions |

The special polynomial `X^8-1` is needed only to identify R3's original GGV
replacement control and its degree-eight numerical fixture.  It is not used
by the transported theorem.

## 6. Second-stage scope and mandatory stop

For a general factorization

```text
H=c product_p p^(e_p)=A^2B,       B squarefree,        (6.1)
```

the same first-residual equation (3.1) shows that weight `n` has a rational
leading mode exactly when

```text
q_n e_p in Z for every p,
equivalently 4 divides (12-n)e_p for every p.          (6.2)
```

This is the safe amount of the nonsquarefree classification.

If `B` is nonconstant, at least one exponent `e_p` is odd.  Since the only
possible denominators of `q_n` divide four, (6.2) again forces `q_n` to be an
integer.  Thus the **leading rational mode weights** remain (3.3).  This does
not transport the pole/provenance theorem: other roots can still have even
multiplicity, and their endpoint pole behavior must be reclassified.

If `B` is constant, every `e_p` is even.  Already the smallest example

```text
H=X^2,
q_22=(12-22)/4=-5/2,
r_22=X^(-5)                                            (6.3)
```

satisfies (3.1), because

```text
-10(2X)X^(-5)-4X^2(-5X^(-6))=0.                      (6.4)
```

For the constant formal edge `F=X^4`, (2.3) gives the exact charged mode

```text
t^22F^(-5/4)=t^22X^(-5).                              (6.5)
```

In fact the multiplicity-two signature admits every even weight
`0,2,...,22`; a fourth-power signature admits every weight.  Most
importantly, weight 22 itself is resonant.  The endpoint equation still
exists, but its homogeneous kernel is no longer zero.  For this same example
a particular rational solution is

```text
d=-1/(16X^3),       g=-8H^2d=X/2,                     (6.6)
```

and arbitrary multiples of `X^(-5)` may be added to `d`.

This is the requested stop.  The audited rational endpoint theorem remains
true, but it cannot be linked to polynomial jets through the squarefree R3
normal form on this branch.  A future nonsquarefree theorem would need a new
resonant-mode quotient and a multiplicity-sensitive pole/provenance lemma.

## 7. Exact verifier and mutations

The desk-scale pure-Python verifier uses only `fractions.Fraction`.  It:

- rehashes all five inputs;
- recomputes `gamma_n=(12-n)/8` and `q_n=(12-n)/4` for every `0<=n<=22`;
- checks the exact six squarefree modes, including the negative powers;
- checks squarefree fixtures of degrees `1,2,3,5,8` and the leading law
  (4.3) for `Y=X^y`, `0<=y<=24`;
- verifies the linear survivor `M_{X+1}(1/6)=1`;
- checks every charged pole scalar for `1<=m<=12`;
- checks the endpoint change-of-variable coefficients;
- computes the multiplicity-one, mixed odd/even, multiplicity-two, and
  multiplicity-four weight inventories; and
- requires the exact `H=X^2`, `n=22`, `r=X^(-5)` mutation to pass.

Replay:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_keller_face_general_squarefree_modes_r4_20260827/verify_r4.py
```

## 8. Scope, rollback, and nonclaims

The additive producer theorem extends reviewed R3 only from
`H=X^8-1` to **nonconstant squarefree `H` of degree at least two**, with the
same exact `H^2/H^3` leading edge and charged operator.  It does not say that
an arbitrary GGV face has this form.

Until different-model hostile review, canonical scope remains the reviewed
R3 theorem at `H=X^8-1`.  On any failure, delete only the new R4 case/report;
the pinned R3 bytes and its review remain unchanged.

No claim is made of:

- existence of a polynomial jet for squarefree linear `H`;
- a general `H=A^2B` normal-form or pole/provenance theorem;
- raw `2S/3S` polynomial-source provenance;
- landing a genuine complete GGV chain in this leading edge;
- a GGV-family exclusion, `G2-PSC`, `G2-BD`, a counterexample, or JC2.

