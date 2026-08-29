# Hostile review of the Sigray Section 7 independent audit

Date: 2026-08-28  
Reviewer: GPT-5 / Codex  
Scope: the supplied audit of Sigray Section 7 against the primary PDF,
printed pp. 33--39 (Section 7 itself is pp. 35--39), with only the definitions
needed to check the claimed indexing defect, countermodel, repair, downstream
ledger, and root-`M` conclusion.

## 1. Custody

Reviewed audit:

```text
0159cdf18f9ad1c986677d4631916dbbef0b5310829958f6dac192eab2795a31
  jc2/xmodel/sigray-section7-full-independent-audit-sol-ultra-20260828.md
```

Primary source:

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
  jc2/refs/sigray_full.pdf
```

The expected audit hash matches exactly. No canonical file was edited. No
file under `jc2-lean` was accessed, listed, searched, built, or modified.

## 2. Executive verdict

**VERIFIED WITH TWO MATERIAL QUALIFICATIONS AND ONE FORMALIZATION
REQUIREMENT.**

1. The central source diagnosis is correct. Proposition 7.3 gives one lower
   bound for an entire outgoing-direction cluster, whereas Notation 7.3
   subtracts that lower bound once for every normalized puncture. Therefore
   literal Proposition 7.4 does not follow, and literal equation (22) omits
   an exact nonnegative splitting term.
2. The proposed chart is an exact local Keller countermodel to the
   *local-deformation inference*: all of its flag, contact, normalization,
   and local-degree calculations check. It is not a polynomial Keller pair:
   in affine variables its first component contains `1/(2y^2)`. Thus it does
   not prove that literal Proposition 7.4 is false for the globally
   quantified normalized polynomial pairs. The audit discloses this near the
   end of its model discussion, but the phrases “false” and “precisely the
   analytic category used” need the sharper qualification given below.
3. The cluster ledger is sound after directions are defined geometrically as
   points of the normalized dicritical boundary component. The subsequent
   Euler calculation is sound **conditional on** a global resolved-direction
   lemma. The audit's informal `[c]` quotient and asserted lines
   `E_i ~= A^1` should be replaced by that construction (or by an explicit
   descent lemma). The producer **asserts but does not prove** the resulting
   common-resolution/no-duplication lemma. It is a mandatory addition before
   the producer's repaired Euler theorem can be called self-contained. No
   hidden hypothesis is known to invalidate the repair, but the missing
   lemma cannot be promoted merely as “standard.”

Corollary 7.1 retains exactly the same numerical statement. Any later
`lambda`/`psi` use that applies it to a **set of distinct critical-value
vertices** is unchanged. Per-puncture slack interpretations do not survive.
Section 7 has no consequence for the root case `M_(0,y)=1`.

## 3. The literal indexing mismatch is real

Printed Proposition 7.3 fixes `F in T_(a,cv)` and a realizable coefficient
`c`, defines one set

```text
R_a^* = {P in Rbar_a\R_a : I_P(u+1/kappa)=F*c},
```

and proves only

```text
sum_(P in R_a^*) Lambda(P) >= kappa_F(pi(F)-1).          (P7.3)
```

It gives puncturewise equality only under the additional simple-root
hypothesis, when `R_a^*={P}`.

Printed Notation 7.3 instead defines

```text
delta_a^lit
 = sum_(P finite puncture)
     (Lambda(P)-kappa_(Fhat_P)(pi(Fhat_P)-1)).           (N7.3)
```

Let `C` be one geometric outgoing direction, put

```text
R_C       = its punctures,
r_C       = #R_C,
L_C       = sum_(P in R_C) Lambda(P),
b_C       = kappa_F(pi(F)-1).
```

Then the contribution of `C` to (N7.3) is `L_C-r_C b_C`, while (P7.3)
only proves `L_C-b_C>=0`. For `r_C>1` these are different inequalities.
Nothing on pp. 35--38 converts the latter into the former.

The exact terminology should be:

- Notation 7.3 is a syntactically possible definition but is indexed
  incompatibly with the estimate used to prove Proposition 7.4.
- Literal Proposition 7.4 and the use of literal `delta_a` in Proposition
  7.5 are **unproved**. A global polynomial counterexample to them is not
  exhibited.

The audit is also right about the independent final-sign typo on printed
p. 39. Equation (22) rearranges to

```text
1 = td(f,g) - sum_i b_i - sum_a delta_a,
```

not the printed line with `+sum delta`. The printed `delta_(F_i,a)` is not
the quantity defined in Notation 7.3.

## 4. Exact check of the local Keller chart

Take

```text
s=y^(-1),    t=xy^3,
x=t s^3,     y=s^(-1),
g=t,         f=t^2+s^2/2.
```

The volume calculation is exact:

```text
dx wedge dy = s ds wedge dt,
df wedge dg = (2t dt+s ds) wedge dt = s ds wedge dt.
```

Hence `J_(x,y)(f,g)=1` on the punctured chart `s!=0`.

At the height-three flag, the residual coordinate is `t=xy^3`, so

```text
p_F(t)=t^2,  q_F(t)=t,
d_f=d_g=0,   pi(F)=3,   kappa_F=1,   b_F=2.
```

On `f=0`,

```text
t=alpha_+ s or t=alpha_- s,
alpha_+ != alpha_-,    alpha_+^2=alpha_-^2=-1/2.
```

These are two branches of the normalization. With `z=t` as local
uniformizer,

```text
y ~ C z^(-1),    x ~ C' z^4.
```

Their first differing Puiseux coefficient has height four, so their contact
is four and both lie in the one successor direction `F*0` used by
Proposition 7.3. On each branch `g=z`, hence

```text
Lambda(P_+)=Lambda(P_-)=1,
L_C=2=b_F.
```

Consequently this cluster contributes `0` to the cluster excess but

```text
(1-2)+(1-2)=-2
```

to literal Notation 7.3.

For `f=a!=0`, the boundary points are `t_0=+sqrt(a)` and
`t_0=-sqrt(a)`. Near either point,

```text
t-t_0 = -s^2/(4t_0)+O(s^4),
```

so the local degree of `g-g(P)` is two. Each nearby direction is simple and
has the predicted baseline two. The two ramification points have different
`g`-values; their local degrees therefore cannot be added as if they were
two persistent sheets over one target value. This exactly defeats the
per-special-puncture deformation argument.

### Hidden global hypothesis

In the original affine variables the same functions are

```text
g = x y^3,
f = x^2 y^6 + 1/(2y^2).
```

Thus `g` is polynomial but `f` is not. The model is an exact holomorphic
Keller chart near this boundary point (and an exact rational Keller pair on
`y!=0`), but it is not a pair in `C[x,y]`, much less a normalized polynomial
counterexample as assumed by the paper.

This failure is also visible directly in the Newton-support semigroup. In
the fixed chart, every affine polynomial monomial has the form

```text
x^i y^j = t^i s^(3i-j),    i,j>=0.
```

A pure `s^2` term would require `i=0,j=-2`, which is outside polynomial
support. Thus the offending term is not merely hidden by notation: the
displayed exact germ cannot be the restriction of a polynomial `f` in these
affine coordinates.

This does **not** spoil its decisive, narrower use: it proves that local
Jacobian-one geometry, normalization, proper local degree, and generic
splitting alone do not yield one baseline per special puncture. It does
mean that the audit must not present it as a counterexample to a theorem
quantified over global polynomial pairs, or as proof that a split cluster
actually occurs for such a pair. An algebraization/global-realizability
theorem would be needed for that stronger conclusion, and none is supplied.

## 5. Coordinate-free cluster repair

The repair should avoid the audit's undefined cyclic notation `[c]`.
For each finite puncture `P`, Proposition 7.2 supplies its unique
critical-value flag `Fhat_P`. At `F=Fhat_P`, define the direction `D_P`
geometrically as either

- the germ of the outgoing edge containing `P`, or equivalently
- the point of the normalized dicritical boundary component selected by
  the next Puiseux coefficient.

This is invariant under changing the common Puiseux denominator and under
the root-of-unity change of residual coordinate. Put

```text
C=(F,D),
R_C={P : (Fhat_P,D_P)=(F,D)},
L_C=sum_(P in R_C) Lambda(P),
b_C=kappa_F(pi(F)-1).
```

The `R_C` form a genuine partition of the finite punctures. Proposition 7.3
is exactly

```text
L_C >= b_C.
```

Define

```text
delta_a^cl := sum_C (L_C-b_C).                           (R7.3)
```

Then `delta_a^cl>=0`. Outside the finite discriminant set of the finitely
many boundary value polynomials, every direction is simple, so Proposition
7.3 gives `L_C=b_C` for every `C` and `delta_a^cl=0`.

The exact comparison with the printed quantity is

```text
delta_a^cl = delta_a^lit + S_a,
S_a = sum_C (r_C-1)b_C >= 0.                             (split)
```

Here `b_C>0` follows from Statement 7.1. Formula (split), not a
puncturewise inequality, is the complete correction.

## 6. Euler identity: valid formulation and required lemma

Fix `a_0` and write `T_(a0,cv)={F_1,...,F_s}` and
`b_i=kappa_(F_i)(pi(F_i)-1)`.

On a common smooth resolution of the rational map `(f,g)`, the valuation
`F_i` is represented by a dicritical boundary component. Its direction
chart is a geometric affine line `E_i^o ~= A^1`; define

```text
phi_i=(f,g)|_(E_i^o): E_i^o -> A^2.
```

This geometric definition incorporates the cyclic quotient automatically.
It also makes clear what the audit needs as a lemma: the points of the
fibres of all `phi_i` are in bijection with the direction clusters in all
fibres of `f`, without duplication, and the transported weight is `b_i`.
This is the resolved-boundary form of Statement 3.14. Raw equalities in a
named residual coordinate are neither needed nor safe.

The producer does not actually construct this common resolution or prove
the asserted bijection, descent, and no-duplication statements. Its local
tube argument for Proposition 7.3 does not supply the missing global lemma,
and it cites no external theorem that does. The exact missing result is:

```text
Resolved-direction lemma.
There is one smooth projective resolution X of the rational map
(f,g):P^2 ---> P^1 x P^1 and, for every F_i, one boundary component E_i
such that

(i)   E_i is P^1 and U_i:=E_i\{infinity_i} is A^1;
(ii)  f and g are regular on U_i and their restrictions descend through
      every residual-coordinate stabilizer;
(iii) for every (a,b), the disjoint union of the geometric fibres
      {(z in U_i): (f(z),g(z))=(a,b)} is in bijection with the finite-value
      direction clusters over (a,b);
(iv)  every finite puncture belongs to the cluster of exactly one such z;
(v)   the weight transported along E_i is the constant
      b_i=kappa_(F_i)(pi(F_i)-1).
```

All five clauses are load-bearing. Without them `B(a,b)` might omit or
double-count a cluster, its domain could have Euler characteristic different
from one, or the raw residual polynomials might fail to descend. Accordingly
this lemma is a mandatory correction, not optional exposition. This review
finds the lemma geometrically plausible but does not promote it on that
basis.

Let

```text
N(a,b)=#(f,g)^(-1)(a,b),
B(a,b)=sum_i b_i #phi_i^(-1)(a,b),
```

where `#` counts geometric direction points. It must not be replaced by the
source's boolean relation `a ->_i b`, and it does not count ramification of
`phi_i` as extra directions.

On the normalization of `f=a`, the divisor of `g-b`, together with the
every-fibre degree identity, gives

```text
td(f,g)-N(a,b)
 = sum_(P finite puncture, g(P)=b) Lambda(P).             (fiber)
```

Grouping (fiber) by direction clusters yields

```text
td(f,g)-N(a,b)=B(a,b)+E(a,b),
E(a,b)>=0,
sum_b E(a,b)=delta_a^cl.
```

No injectivity or smoothness of the parametrized value curve is required.
Indeed, constructible Euler pushforward gives

```text
integral_(A^2) N dchi_c = chi_c(A^2)=1,
integral_(A^2) #phi_i^(-1)(z) dchi_c(z)
  = chi_c(E_i^o)=1.
```

Since `delta_a^cl` vanishes away from a finite discriminant set,
Euler-Fubini now gives

```text
td(f,g)
 = 1 + sum_i b_i + sum_(a in C) delta_a^cl.              (22-cl)
```

Equivalently, in the printed indexing,

```text
td(f,g)
 = 1 + sum_i b_i + sum_a delta_a^lit + sum_a S_a.        (22-lit-fixed)
```

This validates only the algebraic/Euler derivation **conditional on proving**
the resolved-direction lemma. The producer's theorem proof as filed is
therefore incomplete, although its constructible-pushforward calculation
after that lemma is correct. No counterexample to the proposed completion
was found, but plausibility is not a proof. The unresolved global-polynomial
status of the local model is irrelevant here: the repair uses the inequality
actually proved by Proposition 7.3, not the model.

## 7. Corollary 7.1 and later consumers

All weights omitted from a chosen subset of `T_(a,cv)` are positive, and
all cluster excesses are nonnegative. Therefore (22-cl) gives exactly

```text
td(f,g) >= 1 + sum_(H in S) kappa_H(pi(H)-1)
```

for every set `S` of distinct critical-value flags. Thus repaired
Corollary 7.1 is unchanged.

Notation 9.3 defines `lambda_F` as a sum of the same vertex weights
`kappa_H(pi(H)-1)`. Statement 9.4's `psi` reserve is likewise the weight of
an additional critical-value vertex on the other root component. Hence the
Section 7 repair changes neither a `lambda` value nor a `psi` charge.

The exact dependency condition is important: Corollary 7.1 bounds a set,
not a multiset. A downstream addition of several `lambda` quantities remains
valid only after showing that the critical-value vertices being added are
distinct (and that the `psi` vertex is outside their union). That condition
is independent of the cluster repair and cannot be certified merely from
pp. 35--39. Accordingly, the audit's blanket phrase “every consumer” should
be read as conditional on the cited downstream distinctness checks.

What definitely does not survive is any assertion that zero global slack
forces

```text
Lambda(P)=kappa_(Fhat_P)(pi(Fhat_P)-1)
```

for each puncture. It forces only `L_C=b_C` for each cluster.

## 8. No root-`M` consequence

The audit's negative answer is correct.

- `M_F` is introduced only in Section 8 and never occurs in the Section 7
  ledger.
- Every Section 7 baseline is attached to
  `H in T_(a,cv) subset T_a^0`, so `d_(f-a,H)=0` and `pi(H)>1`.
- The root `(0,y)` has `pi=0` and positive `f-a` order; it is not a
  critical-value flag.
- Neither the existence nor the saturation of a cluster creates a charge
  from the bare condition `M_(0,y)=1`.

There is also an independent visible root-case gap in the printed proof of
Proposition 8.4: if its starting `F` is already `(0,y)`, the descending
sequence has length zero, but the proof sets `H=F_(n-1)`. Section 7 supplies
no predecessor and no replacement contradiction. Thus even under the
singleton-pole hypothesis, Section 7 does not exclude `M_(0,y)=1`.

## 9. Exact corrections required in the reviewed audit

1. Replace “the per-puncture strengthening is false” by “the
   per-puncture strengthening is not implied by Proposition 7.3 and is
   false in the local Keller-chart category used by the deformation
   argument; no global polynomial counterexample is claimed.”
2. After displaying the chart, state explicitly
   `f=x^2y^6+1/(2y^2)` and record the resulting failure of the global
   polynomial hypothesis.
3. Replace the informal cluster label `(F,[c])` by the geometric pair
   `(F,D)`, or prove the root-of-unity quotient and descent of both residual
   value polynomials.
4. Prove (or cite with hypotheses) the five-clause resolved-direction lemma
   in Section 6 above. Merely asserting a direction line `E_i^o ~= A^1` is
   insufficient.
5. Qualify preservation of all `lambda`/`psi` consumers by the necessary
   no-double-counting/distinct-cv-vertex hypothesis. The Section 7 repair
   itself preserves every individual vertex weight.

## 10. Final classification

```text
Printed Section 7 proof of Proposition 7.4/(22):        INVALID
Global literal Proposition 7.4:                        UNPROVED, NOT DISPROVED
Exact local chart arithmetic:                          VERIFIED
Global-polynomial status of that chart:                REFUTED
Cluster nonnegativity/generic-zero repair:              VERIFIED AFTER GEOMETRIC DEFINITION
Euler identity (22-cl) in the producer report:          INCOMPLETE--MANDATORY LEMMA ABSENT
Euler derivation assuming the resolved-direction lemma: VERIFIED CONDITIONALLY
Corollary 7.1:                                         PRESERVED
lambda/psi budgets:                                    PRESERVED FOR DISTINCT CV SETS
Per-puncture slack-zero consequences:                  NOT PRESERVED
Root M_(0,y)=1 consequence from Section 7:             NONE
```

Overall, the audit found the correct Section 7 ledger defect and the correct
repair architecture. Its substantive overreach is the status assigned to
the local countermodel relative to the paper's global polynomial hypothesis.
Its repaired Euler theorem is not fully proved as filed: it must add the
common-resolution, quotient-descent, cluster-bijection, and no-duplication
lemma that makes the geometric dicritical direction lines and the
constructible pushforward legitimate.
