# Sigray Section 7: hostile audit of the resolution-free quotient route

Date: 2026-08-28  
Reviewer: GPT-5.5 / Codex  
Target route: close the Section 7 resolved-direction gap without a common
surface-resolution theorem, using Puiseux coefficient charts, corrected
twisted Statement 3.14, and the reviewed every-fibre Proposition 5.8.

## 0. Verdict

**PASS as a campaign repair, with explicit dependencies.**

The proposed route works if the "direction line" is not interpreted as a
component of a final common boundary resolution.  It must be interpreted as
the abstract finite cyclic quotient of a Puiseux residual coefficient line.
With that interpretation:

- the prefix-preserving deck stabilizer and its scalar action can be computed
  for an arbitrary rational truncation height, not only for characteristic
  vertices;
- every zero-order residual polynomial descends to the quotient;
- corrected/twisted Statement 3.14 transports the quotient point and the two
  value functions by one common twist;
- EW1 and EW2 identify the disjoint union of these quotient lines with all
  finite-value direction clusters, including collision points;
- the Euler proof of the cluster identity `(22-cl)` follows without any
  common final graph resolution.

**FAIL as a proof of the literal printed Proposition 7.5.**  The printed
per-puncture `delta_a`, the boolean relation `a ->_i b`, the assertion that
the value curve is biholomorphic to `C`, and exact named-residual-coordinate
transport remain unusable.

The minimal clean repair is the quotient lemma stated in Section 8 below,
plus explicit import of the every-fibre Proposition 5.8 replacement by hash:

```text
47eef0925470fc769eec08e6d3bf972446feaaff6f6ef709c154edaa31054caf
  xmodel/sigray-prop58-every-fiber-independent-audit-sol-ultra-20260828.md
```

## 1. Custody

Files checked:

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
  refs/sigray_full.pdf

0159cdf18f9ad1c986677d4631916dbbef0b5310829958f6dac192eab2795a31
  xmodel/sigray-section7-full-independent-audit-sol-ultra-20260828.md

af1ce600bff775bacee122bea3cd5a098ef6a457616273d8a0147c16438a0afe
  xmodel/sigray-section7-full-independent-audit-hostile-review-gpt5-20260828.md

3e44aba9ae890028b5d64084a635df7060b87765635f2f5f47eb2f8728549ae9
  xmodel/sigray-section7-resolved-direction-lemma-producer-gpt5-20260828.md

aa5dc37bd505cc5be78d77817a115afa5d05062023800ada7c8e40572abe07cb
  xmodel/sigray-section7-resolved-direction-lemma-hostile-review-terra-20260828.md

71aba565608db6e882b6ffd724ab82a14d3de5b678500221190fea4f24904eea
  xmodel/sigray-section7-resolution-free-coordinator-repair-sol-ultra-20260828.md

47eef0925470fc769eec08e6d3bf972446feaaff6f6ef709c154edaa31054caf
  xmodel/sigray-prop58-every-fiber-independent-audit-sol-ultra-20260828.md

569661d0771b8353ae76e4d8f48a809f996e83b36a93239f1e8540bb274fbac8
  ladder/SOL-PROP58-REVIEW.md

bb033a7130da671c4a02b62053c8c24b6e68d9a453f542c93588eb945f1c8648
  xmodel/sigray-lemma61-prop58-coordinator-integration-sol-ultra-20260828.md
```

Primary source pages used:

- printed pp. 10--18: Eggers-Wall definitions, residual coordinate,
  residual polynomial, `nu_F`, `kappa_F`, and Statement 3.14;
- printed p. 28: Proposition 5.8 source statement, noted as an unproved
  source gap but replaced by the campaign audit above;
- printed pp. 35--39: Section 7, including Notation 7.1, Propositions 7.2
  through 7.5, and Corollary 7.1.

No canonical file is edited by this report.

## 2. Corrected inputs used

I use centred notation for the fibre `f=a`.  Thus the first polynomial in the
local Puiseux chart is `A_a=f-a`, not bare `f`; this is the repaired reading
needed to make Section 7 coherent.

The proof below uses only the following local campaign inputs from the
reviewed Section 7 package:

1. **EW1, unique zero-order flag.**  Every normalized puncture on `f=a` with
   finite `g`-value has one unique flag `Fhat_P` with
   `d_(f-a,Fhat_P)=0` and `d_(g,Fhat_P)=0`.

2. **EW2, root-orbit realization and clustering.**  At a cv flag, each
   realized root orbit of the centred first residual polynomial is exactly
   one outgoing geometric direction; every root orbit is realized; punctures
   sharing the flag and orbit form the repaired Proposition 7.3 cluster.

3. **EW4, cluster weight.**  For a cluster `C` at a cv flag `F`,
   `L_C=sum_(P in C) Lambda(P) >= b_F`, where
   `b_F=kappa_F(pi(F)-1)>0`; equality holds for a simple covered residual
   root.

4. **Corrected/twisted Statement 3.14.**  Across fibres, strict truncations
   below a fixed rational height are transported; exact named `eta` equality
   is not asserted.  The residual coordinate may be multiplied by one common
   root of unity, and the same twist applies to all fixed-polynomial residual
   data.

5. **Every-fibre Proposition 5.8 replacement.**  On the normalization of
   every fibre `f=a`, the meromorphic degree of `g` is `td(f,g)`.  This is
   imported from the reviewed replacement with SHA256
   `47eef0925470fc769eec08e6d3bf972446feaaff6f6ef709c154edaa31054caf`.

No use is made of printed Proposition 7.5, printed Proposition 7.4 as stated,
the printed boolean `a ->_i b`, or a common graph-resolution/divisorial
realization theorem.

## 3. Arbitrary rational stabilizer calculation

This is the hostile point that must be stated more precisely than the earlier
producer file did.

Work on a `y`-Puiseux end; the `x`-Puiseux end is identical with `x,y`
interchanged.  Choose a common suitable denominator `K` and write

```text
x = t^(-K),
y = sum_{r>=0} c_r t^r.
```

Let `F=I_P(u)` be any rational flag, not necessarily a vertex.  Put
`n=K u in Z`.  The strict prefix and residual chart are

```text
phi_<n(t) = sum_{r<n} c_r t^r,
y = phi_<n(t) + t^n eta.
```

Let

```text
e_< = gcd(K, { r<n : c_r != 0 }),
```

with `e_<=K` if the displayed support is empty.  The deck group of the
`K`-cover is `mu_K`, acting by `t -> zeta t`.  The subgroup preserving both
`x=t^(-K)` and the strict prefix is exactly

```text
Delta_< = { zeta in mu_K : zeta^r = 1 for all r<n with c_r != 0 }
        ~= mu_{e_<}.
```

In the residual coefficient chart the same deck transformation is

```text
(t, eta) |-> (zeta t, zeta^(-n) eta).
```

The effective image on `eta` therefore has order

```text
m(F,u) = e_< / gcd(e_<, n).                         (3.1)
```

So the geometric coefficient-orbit line is

```text
U_F = A^1_eta / Gamma_F
    = Spec C[eta]^{Gamma_F}
    = Spec C[eta^{m(F,u)}]
    ~= A^1_z.                                      (3.2)
```

This formula is invariant under refinement of the suitable denominator:
replacing `K,n,e_<` by `MK,Mn,Me_<` leaves
`e_</gcd(e_<,n)` unchanged.

At a characteristic vertex with Puiseux characteristic exponent
`u=beta_j/K`, the strict prefix has `e_<=e_{j-1}` and
`gcd(e_{j-1},beta_j)=e_j`, hence

```text
m(F,u) = e_{j-1}/e_j = nu_F.
```

Thus the familiar `nu_F` is only the characteristic-vertex special case.  On
a non-characteristic rational flag, the effective stabilizer can be nontrivial
if the chosen rational height introduces a denominator jump; it is trivial
precisely when `n` is divisible by the current prefix gcd `e_<`.

This proves the requested stabilizer order/action for arbitrary rational
`u`.

## 4. Zero-order residual descent

Let `h(x,y)` be any polynomial.  Substitute the chart from Section 3:

```text
H(t,eta) = h(t^(-K), phi_<n(t) + t^n eta)
         = sum_N t^N H_N(eta),
```

with finitely many nonzero terms in the relevant leading range.  Since
`h(x,y)` is a single-valued polynomial in the original variables,

```text
H(zeta t, zeta^(-n) eta) = H(t,eta)
```

for every prefix-preserving `zeta`.  Comparing `t^N` coefficients gives

```text
H_N(zeta^(-n) eta) = zeta^(-N) H_N(eta).             (4.1)
```

Sigray's leading residual at order `d_(h,F)` is one of these coefficients;
with this convention, `N=0` exactly when `d_(h,F)=0`.  Therefore, if
`d_(h,F)=0`,

```text
H_0(gamma eta) = H_0(eta)       for every gamma in Gamma_F.
```

Hence every zero-order residual polynomial descends uniquely to a polynomial
on `U_F`.  In particular, for a reference cv flag `F_i` on the fibre `f=a0`,
both

```text
p_(f-a0,F_i)(eta),     p_(g,F_i)(eta)
```

descend to polynomials in `z=eta^{m_i}`.

This is the exact zero-order cyclic residual descent lemma Terra demanded.
It is local Puiseux algebra only; it does not use a boundary divisor.

## 5. Corrected Statement 3.14 on the quotient

Fix a reference value `a0` and a reference cv flag `F`.  Write the descended
zero-order residuals as

```text
A_F(z) = p_(f-a0,F)(eta),
Q_F(z) = p_(g,F)(eta),
z = eta^m.
```

Define the bare first-value function

```text
P_F(z) = a0 + A_F(z).                                (5.1)
```

Now transport from the fibre `f=a0` to the fibre `f=a`.  The proof of
Statement 3.14 uses the same strict Puiseux coefficients below `u`.  The
audited correction is that a different Puiseux representative may change the
covered residual coordinate by one deck scalar

```text
eta |-> omega eta.
```

The same scalar is used for every fixed polynomial, in particular for
`f-a0`, `f-a`, and `g`.  Consequently, after passing to the quotient line,
the transported centred first residual and `g` residual are

```text
p_(f-a,F(a))(eta_a) = P_F(z_a) - a,
p_(g,F(a))(eta_a)   = Q_F(z_a),                     (5.2)
```

up to precomposition of both functions by the same automorphism of the
abstract quotient `U_F`.  That ambiguity is harmless: root sets, multiplicity
away from the quotient branch point, `g`-values, and Euler fibre counts are
unchanged by a source automorphism.

The important correction is negative as well as positive: Statement 3.14
does **not** give a canonical named lift `eta` across all fibres.  The route
only needs the quotient point and the pair of descended functions `(P_F,Q_F)`.

Because `d_(g,F)=0` is preserved under the same fixed-polynomial expansion,
corrected Statement 3.14 gives a bijection of reference cv flags with cv
flags on every fibre:

```text
T_(a0,cv) <-> T_(a,cv).                              (5.3)
```

This is an every-fibre statement about abstract coefficient quotients, not
about one common resolved boundary surface.

## 6. Quotient points are direction clusters

Enumerate the finite reference set

```text
T_(a0,cv) = {F_1,...,F_s}.
```

For each `i`, construct `U_i ~= A^1_z` as above, and define

```text
phi_i : U_i -> A^2,
phi_i(z) = (P_i(z), Q_i(z)),
P_i(z)=a0+A_i(z).                                  (6.1)
```

The polynomial `P_i` is nonconstant.  Indeed, on the reference fibre the
centred residual polynomial has at least one realized root and is not the
zero polynomial; a nonzero constant would have no root.  Hence it has
positive degree.  Therefore each `P_i` is surjective over `C`, and the fibres
of `phi_i` are finite.

Given `z in U_i(C)`, put `a=P_i(z)` and choose a covered lift `eta=c`.
Equation (5.2) says that the orbit of `c` is a root orbit of the centred first
residual at the transported flag `F_i(a)`.  By EW2 that orbit is realized and
is exactly one outgoing direction.  The punctures above that direction form
one cluster `C(i,z)`, and every puncture in the cluster has finite value
`g=Q_i(z)`.

Conversely, take any finite-value direction cluster on any fibre.  EW1 gives
the unique cv flag of any puncture in the cluster.  Transport (5.3) sends it
to a unique reference flag `F_i`.  EW2 gives one coefficient orbit, hence one
point of `U_i`.

Thus there is a bijection

```text
coprod_i U_i(C)
  <-> {finite-value direction clusters in all fibres}.       (6.2)
```

This handles the main hostile cases:

- **Cyclic overcount.**  Multiple covered residual coefficients in one
  `Gamma_i`-orbit are one quotient point and one geometric direction.
- **The fixed point `eta=0`.**  It remains one quotient point; no artificial
  multiplicity is introduced.
- **Cross-flag duplication.**  A nonempty cluster cannot come from two
  reference flags, because EW1 gives a unique cv flag on its fibre.
- **Collision points.**  A multiple root or shared target value is still a
  finite coefficient-orbit point in `U_i`; it is not removed.  It contributes
  one baseline term for the direction point, with excess carried separately
  by the cluster weight `L_C-b_C`.
- **Coefficient infinity.**  `U_i` is the affine quotient of the residual
  coefficient line.  Its missing point at infinity is not a finite coefficient
  direction and is never needed for the finite-value cluster ledger.

This is where the resolution-free route differs from the rejected resolved
boundary proof: no claim is made that `U_i` is an open stratum of a final
surface resolution.

## 7. Euler proof of `(22-cl)`

Let

```text
d = td(f,g),
N(a,b) = # Phi^{-1}(a,b).
```

The Keller condition makes affine preimages simple.  The imported every-fibre
Proposition 5.8 says that the meromorphic degree of `g` on the normalization
of every fibre `f=a` is `d`.  Therefore the divisor of `g-b` on that
normalization gives the pointwise identity

```text
d - N(a,b)
  = sum_{P at infinity on f=a, g(P)=b} Lambda(P).        (7.1)
```

Group the right side by the cluster bijection (6.2).  Put

```text
b_i = kappa_{F_i}(pi(F_i)-1) > 0,
B(a,b) = sum_i b_i * # phi_i^{-1}(a,b).                 (7.2)
```

For a cluster `C`, write

```text
L_C = sum_{P in C} Lambda(P),
excess(C) = L_C - b_C >= 0
```

where the inequality is EW4.  Then

```text
d - N(a,b) = B(a,b) + E(a,b),                           (7.3)
```

where `E(a,b)` is the sum of `excess(C)` over clusters with target value
`(a,b)`.

For fixed `a`,

```text
delta_a^cl = sum_b E(a,b)
            = sum_{clusters C on f=a} (L_C-b_C).         (7.4)
```

This is the repaired cluster excess.  It is not the printed per-puncture
`delta_a`.

The support of `delta_a^cl` is finite.  For each `i`, outside the finite set
consisting of critical values of `P_i` and, when `m_i>1`, the branch value
`P_i(0)`, every root of `P_i(z)=a` lifts to a nonzero simple covered residual
root.  EW4 then gives equality `L_C=b_C` for every cluster over that fibre.

Now integrate (7.3) with compactly supported Euler characteristic.  Since
`Phi` is an etale polynomial map with finite fibres,

```text
int_{A^2} N d chi_c = chi_c(A^2) = 1.
```

For each quotient map `phi_i`, `P_i` is nonconstant, so `phi_i` is
quasi-finite, and constructible Euler-Fubini gives

```text
int_{A^2} #phi_i^{-1}(a,b) d chi_c
  = chi_c(U_i) = chi_c(A^1) = 1.
```

Therefore

```text
int_{A^2} B d chi_c = sum_i b_i,
int_{A^2} E d chi_c = sum_a delta_a^cl.
```

Integrating (7.3) yields

```text
td(f,g)
  = 1
    + sum_{i=1}^s kappa_{F_i}(pi(F_i)-1)
    + sum_{a in C} delta_a^cl.                         (22-cl)
```

This is the repaired Section 7 identity.

## 8. Minimal clean repair statement

The following lemma is the minimal replacement for the unresolved
"resolved-direction" assertion.  It should be promoted instead of any common
surface-resolution claim.

```text
Resolution-free cyclic quotient direction lemma.

Let Phi=(f,g):A^2_C -> A^2_C be a polynomial Keller map.  Fix a0 in C and
enumerate the corrected centred critical-value flags
T_(a0,cv)={F_1,...,F_s}.  For every F_i at rational height u_i, choose a
suitable Puiseux denominator K_i and let n_i=K_i u_i.  Let e_i be the gcd of
K_i with the nonzero exponent indices strictly below n_i in the chosen
Puiseux prefix.  Then the prefix-preserving deck subgroup acts effectively on
the residual coefficient eta_i by a scalar cyclic group of order

    m_i = e_i / gcd(e_i,n_i).

The quotient U_i=A^1_eta_i/Gamma_i is A^1_z_i with z_i=eta_i^{m_i}.  If a
polynomial h has d_(h,F_i)=0, then p_(h,F_i)(eta_i) is Gamma_i-invariant and
descends to a unique polynomial on U_i.

For h=f-a0 and h=g, write the descended functions as A_i(z_i) and Q_i(z_i),
and set P_i=a0+A_i.  Under corrected/twisted Statement 3.14, for every fibre
f=a the transported centred residuals are P_i-a and Q_i, up to one common
source automorphism of U_i.  The root orbits of P_i(z_i)=a are exactly the
finite-value direction clusters at the transported flag.  The disjoint union
of U_i(C) over all reference flags is therefore in bijection with all
finite-value direction clusters in all finite fibres.
```

Together with EW4 and the reviewed every-fibre Proposition 5.8, this lemma
proves `(22-cl)`.

## 9. Hostile ledger

| Claim | Verdict | Finding / repair |
|---|---:|---|
| Common surface-resolution theorem is needed | **FAIL** | Not needed.  Use abstract quotient lines `U_i`; do not assert they are final boundary strata. |
| Arbitrary rational stabilizer/action | **PASS** | Formula `m=e_</gcd(e_<,n)` proves the effective scalar action.  Characteristic `nu_F` is only a special case. |
| Zero-order residuals `f-a0` and `g` descend | **PASS** | Deck semi-invariance has character `zeta^{-N}`; at order zero the character is trivial. |
| Corrected/twisted Statement 3.14 identifies quotient points and values | **PASS, corrected** | It identifies quotient data up to one common twist/source automorphism, not literal named `eta` lifts. |
| Bijection `coprod U_i(C)` with direction clusters | **PASS, dependent on EW1/EW2** | EW1 gives unique flag; EW2 gives root-orbit realization and clusters. |
| Collision points | **PASS** | They are finite quotient points and stay in the cluster ledger; only coefficient infinity is absent. |
| Cyclic and cross-vertex deduplication | **PASS** | The quotient removes cyclic representatives; EW1 prevents cross-flag duplication. |
| `P_i` nonconstant and finite fibres | **PASS** | A reference cv flag has a realized root of a nonzero centred residual, forcing positive degree. |
| Finiteness of nonzero cluster excess support | **PASS** | Bad `a` lie among finitely many critical values of `P_i` plus branch values `P_i(0)` for nontrivial covers. |
| Every-fibre degree identity | **PASS AS IMPORTED** | Must cite SHA256 `47eef092...`; it is not a consequence of Section 7. |
| Printed Proposition 7.5 and equation `(22)` | **FAIL** | Uses per-puncture `delta_a`, boolean value curves, and a wrong value-curve/injectivity step. |
| Repaired `(22-cl)` | **PASS** | Follows from the quotient lemma, EW4, constructible Euler-Fubini, Keller quasi-finiteness, and imported Prop. 5.8. |
| Circular use of Section 7 | **PASS** | The proof does not use printed Proposition 7.4, Proposition 7.5, or Corollary 7.1. |
| Use of root Proposition 8.4 or later Section 8/9 material | **PASS** | None used. |

## 10. Post-hoc hostile comparison with the current coordinator file

Current coordinator file checked after the independent route above:

```text
71aba565608db6e882b6ffd724ab82a14d3de5b678500221190fea4f24904eea
  xmodel/sigray-section7-resolution-free-coordinator-repair-sol-ultra-20260828.md
```

Material verdict: **agreement**.  The coordinator's current proof uses the
same abstract quotient replacement and no common final graph resolution.
I found no counterexample to its mathematical route.

Hostile mismatches/gaps to fix before promotion:

1. **Centred versus bare notation.**  The coordinator starts with centred
   data `A=f-a`, but Section 4 writes the descended first residual as
   `P_F(z)=p_(f,F)(eta)`.  This is harmless only after explicitly setting
   `P_F=a0+p_(f-a0,F)`.  Without that sentence, the source's old
   bare/centred ambiguity re-enters.

2. **Twist wording.**  The coordinator says the quotient "removes" the common
   deck twist and that the quotient line is unchanged.  If the twist is
   inside the prefix stabilizer this is literally true; if it arises from a
   different aligned presentation, the safe statement is that it precomposes
   both descended functions by the same source automorphism of `U_i`.  The
   Euler and cluster arguments need only the safe statement.

3. **`P_i` nonconstant proof.**  The coordinator argues that for every `a`,
   transport produces an actual cv flag and hence a root of `P_i(z)=a`.
   That is stronger than needed and reads circularly because root existence
   is part of the same transport/root-realization package.  The cleaner proof
   is reference-fibre local: at `F_i`, the centred residual is a nonzero
   leading polynomial with a realized zero, so it cannot be constant.

4. **Source of the common `g` value.**  In Section 5 the coordinator says EW4
   gives the common value `g=Q_i(z)`.  EW4 gives the weight inequality.
   The common value comes from the residual transport plus EW2/repaired
   Proposition 7.3.  This is a citation/wording gap, not a mathematical
   obstruction.

5. **Promotion-status wording.**  The coordinator closes by saying promotion
   requires a different-model check of the stabilizer, aligned Statement 3.14
   presentations, root-orbit realization at every quotient point, and the
   `z=0` genericity issue.  This report supplies that check, with the
   qualifications above.  The route should still be promoted only as
   `(22-cl)` with the imported Prop. 5.8 hash, not as printed `(22)`.

No other material mismatch was found.  In particular, the coordinator's
stabilizer formula, denominator-refinement check, treatment of collision
points, exclusion of `P_i(0)` for nontrivial covers, constructible baseline,
and final Euler integration match this audit.

## 11. Bottom line

The exact obstruction Terra found in the resolved-boundary proof is real only
for that proof strategy.  The resolution-free quotient route avoids it by
never needing a shared boundary divisor.  The local Puiseux deck calculation
supplies the missing cyclic quotient and descent, and corrected/twisted
Statement 3.14 supplies enough every-fibre transport at quotient level.

Promote `(22-cl)` only in the cluster form and only with the explicit input
package in Section 2.  Do not promote the literal printed equation `(22)`.
