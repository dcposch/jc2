# PCC and radical-fiber equivariance

**Date:** 2026-08-20  
**Scope:** primary audit of the banked TD-bound machinery and exact
radical-fiber computation in the residue-A, fixed-`r3`, `B`-frozen, no-log,
`PIN42`, `W1*W2 != 0` chart.  
**Status:** PCC is still **CONJECTURE**.  The fiber action on the pristine
depth ideals is **PROVED**, and its D25 realization is **COMPUTED EXACTLY**.

## 0. Results

1. The maximally precise version of proportional-center coverage is

   \[
   \boxed{\sum_{p\in K_f\cup K_g}
   \min\!\left(\left\lfloor\frac{R_p}{\alpha}\right\rfloor,
               \left\lfloor\frac{S_p}{\beta}\right\rfloor\right)^2
   \ge B^2-1.}\tag{PCC}
   \]

   Here the sum is over the canonical proper and infinitely-near base
   cluster in the minimal simultaneous point resolution of the two
   projective pencils.  PCC immediately gives `td <= alpha*beta`.  Unlike
   KME-2, it is not the desired inequality rewritten: it is a formally
   stronger sufficient lemma, with no converse asserted.

2. PCC is not proved by the bank.  The earliest missing implication in the
   Corollary-7.4 common-power route is the following single-packet transport
   statement:

   > **CONJECTURE WTC-1 (weighted-to-center transport).** A certified
   > Corollary 7.4 Laurent factor packet, together with both transformed
   > denominator sections, determines a named ordinary proper or
   > infinitely-near base center.  After exceptional monomials are removed,
   > the two complete pencil base ideals have the predicted ordinary mobile
   > multiplicities, and the construction records the center's proximity
   > parents.

   No FC5, `w`-invariant, NF-M, or census theorem supplies that arrow.  Even
   after WTC-1, a second coverage/no-double-counting theorem must prove the
   squared mass `>= B^2-1`.  These are the exact obstructions in that proof
   lane, not a shortage of local enumeration.

3. The 36 radical fibers form one free orbit under

   \[
   G=(C_3)^2\times(C_2)^2.
   \]

   No variable or row permutation is needed: a diagonal scaling gives an
   isomorphism between every pair of adjacent fibers.  At D25 the identity

   \[
   F_{\ell,g\lambda}(T_gx)=\chi_\ell(g)F_{\ell,\lambda}(x)
   \]

   was checked as an exact monomial-dictionary identity for

   \[
   2\cdot36\cdot4\cdot34=9792
   \]

   row edges, at `p=105337` and `p=105673`, with zero failures.  This also
   amounts to 438,912 exact specialized coefficient comparisons.

4. The all-depth symmetry of the *pristine source ideal* is proved, rather
   than conjectured: the two cube generators and two sign generators are
   literal reindexings of the 42/21 branch products, and the Jacobian depth
   construction commutes with them.  The remaining operational gap is:

   > **CONJECTURE FUTURE-EMISSION FIDELITY.** Every future optimized D27+
   > Schur/pivot/NF/saturation output is an exact presentation of the
   > corresponding pristine localized ideal and respects the displayed
   > pullback identities.

   This is reducible to finite compiler gates.  Conditional on that gate,
   the orbit count is **one**, so the potential saving is **36x per prime**:
   one solve plus transports instead of 36 solves.  Across the two banked
   primes, 72 solves reduce to two representatives.

---

## 1. PCC: exact statement

Let `k` be an algebraically closed field of characteristic zero.  Let

\[
(f,g):\mathbb A_k^2\longrightarrow\mathbb A_k^2
\]

be a dominant, nonautomorphic, Sigray-normalized polynomial Keller pair,
so `J(f,g) in k*`, and put

\[
\operatorname{td}:=[k(x,y):k(f,g)].
\]

Write its coprime type and degrees as

\[
2\le\alpha<\beta,\qquad (\alpha,\beta)=1,
\qquad d=\deg f=B\alpha,\quad e=\deg g=B\beta,
\]

where `B=gcd(d,e)`.  Let

\[
F(X,Y,Z)=Z^df(X/Z,Y/Z),\qquad
G(X,Y,Z)=Z^eg(X/Z,Y/Z)
\]

and consider the two pencils

\[
\mathcal L_f=\langle F,Z^d\rangle,
\qquad \mathcal L_g=\langle G,Z^e\rangle,
\]

or equivalently the rational maps `[F:Z^d]` and `[G:Z^e]` from
`P^2` to `P^1`.

Let

\[
\pi:X\longrightarrow\mathbb P^2
\]

be the minimal simultaneous resolution by point blowups on which both
pencil maps are morphisms.  Let `K_f` and `K_g` be their clusters of proper
and infinitely-near base centers.  For every
`p in K_f union K_g`, define:

- `R_p` as the order at `p`, immediately before `p` is blown up, of the
  mobile strict transform of a general member of `L_f`;
- `S_p` analogously for `L_g`;
- the value to be zero for a pencil for which `p` is not a base center.

Thus `R_p,S_p` are the point-basis coefficients of the two generic fiber
classes, not multiplicities of a selected special member and not
coefficients in the strict-exceptional basis.  Define the coordinatewise
integral meet

\[
h_p:=\min\!\left(
\left\lfloor\frac{R_p}{\alpha}\right\rfloor,
\left\lfloor\frac{S_p}{\beta}\right\rfloor
\right).\tag{1.1}
\]

> **CONJECTURE PCC (proportional-center coverage).** For every pair above,
> on its minimal simultaneous base cluster,
> \[
> \sum_{p\in K_f\cup K_g}h_p^2\ge B^2-1.\tag{1.2}
> \]

In the orthogonal total-transform point basis, put

\[
H_{\cap}:=\sum_ph_pE_p^*.
\]

Then PCC is equivalently

\[
-H_{\cap}^2\ge B^2-1.\tag{1.3}
\]

This notation does **not** assert that `(h_p)` satisfies proximity
inequalities, is antinef, or is itself the base cluster of a complete
ideal.  It is only a coordinatewise meet in the orthogonal point basis.
Using the minimal simultaneous cluster removes resolution-choice
ambiguity.  A further fixed point blowup after both pencils are resolved
adds zero generic multiplicities, so a legitimate common refinement does
not change (1.2).

### 1.1 PCC is sufficient

Let `H` be the pullback of a line and use the orthogonal total-transform
basis.  The generic fiber classes are

\[
C=B\alpha H-\sum_pR_pE_p^*,\qquad
D=B\beta H-\sum_pS_pE_p^* .\tag{1.4}
\]

The resolved pencils give `C^2=D^2=0`.  For a generic pair of finite target
values, the boundary divisor avoids that target point, while the affine
intersection has degree `td`; hence `C.D=td`.  Therefore

\[
\sum_pR_p^2=B^2\alpha^2,\qquad
\sum_pS_p^2=B^2\beta^2,\qquad
\sum_pR_pS_p=B^2\alpha\beta-\operatorname{td}.\tag{1.5}
\]

By (1.1), term by term,

\[
R_p\ge\alpha h_p,\qquad S_p\ge\beta h_p,\qquad
R_pS_p\ge\alpha\beta h_p^2.\tag{1.6}
\]

Consequently PCC gives

\[
\begin{aligned}
B^2\alpha\beta-\operatorname{td}
 &=\sum_pR_pS_p\\
 &\ge\alpha\beta\sum_ph_p^2\\
 &\ge\alpha\beta(B^2-1),
\end{aligned}
\]

and hence

\[
\boxed{\operatorname{td}\le\alpha\beta}.\tag{1.7}
\]

This is the exact sufficiency argument audited in
`xmodel/grok-k-g5-review.md:525-533,579-583`, strengthening the initial
formulation at `xmodel/sol-g5-emission.md:1014-1048` by fixing the cluster
and point-basis conventions.

There is also an exact mismatch identity.  With

\[
\Delta:=C/\alpha-D/\beta,
\]

(1.5) gives

\[
\sum_p\left(\frac{R_p}{\alpha}-\frac{S_p}{\beta}\right)^2
=\frac{2\operatorname{td}}{\alpha\beta},
\qquad
\Delta^2=-\frac{2\operatorname{td}}{\alpha\beta}.\tag{1.8}
\]

Thus KME-2, `Delta^2 >= -2`, is exactly the desired TD bound rewritten.
It is not an independent sufficient mechanism.  PCC is formally stronger
as a proposed point-basis condition: it termwise implies the bound, while
no converse is asserted or banked.  It is the only named target in the G5
audit that could genuinely imply the sharp bound without simply renaming
it.

### 1.2 Equality exposes PCC's strength

If `td=alpha*beta` and PCC holds, both summed inequalities in (1.7), and
the product inequality `R_p*S_p >= alpha*beta*h_p^2` at every center, are
equalities.  Therefore

\[
\sum_ph_p^2=B^2-1,
\]

and, for every center with `h_p>0`,

\[
R_p=\alpha h_p,\qquad S_p=\beta h_p.
\]

Every center with `h_p=0` must have `R_pS_p=0`.  Thus a sharp pair would
have no residual shared multiplicity away from exactly proportional
centers.  PCC is correspondingly strong; the calculation proves its
sufficiency, not its truth.

---

## 2. PCC proof attempt from the bank

### 2.1 The one available local foothold

The common-power conclusion of GGV Corollary 7.4, in a certified
Laurent/weighted frame and specialized to the type ratio, has the form

\[
\ell(P)=\lambda\widetilde R^{q\alpha},\qquad
\ell(Q)=\mu\widetilde R^{q\beta}.\tag{2.1}
\]

More generally a factor of ordinary order `t` in `R_tilde` occurs to
orders `q*alpha*t` and `q*beta*t`.  This gives the following elementary
conditional statement.

> **Conditional local lemma.** Suppose a theorem transports (2.1) together
> with the transformed denominator sections `Z^d,Z^e` to a named center
> `p` of the simultaneous projective base cluster.  After removing the
> recorded fixed exceptional factors, suppose the *mobile strict transforms
> of generic pencil members* `F-cZ^d` and `G-c'Z^e` have lowest ordinary
> local forms `lambda_0*R_0^(q*alpha)` and
> `mu_0*R_0^(q*beta)`, where `ord_p(R_0)=t`.  Then
> \[
> R_p\ge q\alpha t,\qquad S_p\ge q\beta t,
> \qquad h_p\ge qt.\tag{2.2}
> \]

Once the hypothesis is available, (2.2) is immediate.  The hypothesis is
not banked.  `SECTION4-AUTOMATION.md:140-163` certifies the edge power;
`xmodel/sol-tdbound-review.md:437-483` records precisely why it does not yet
identify an ordinary base-center multiplicity.

Weighted initials alone cannot make that identification.  For example,

```text
u^(q*alpha) + x,       u^(q*beta) + 2*x
```

can display the desired powers on a selected weighted face while ordinary
multiplicity and intersection are controlled by the lower `x` terms.  One
must carry the actual chart substitution, exceptional monomial, ordinary
maximal ideal, and proximity ancestry.

### 2.2 The minimal obstruction in the common-power lane

The first absent theorem can be stated without asking for all of PCC.

> **CONJECTURE WTC-1 (single-packet weighted-to-center transport).** Let a
> certified Corollary 7.4 cut contain a named factor packet
> `R_tilde^(q*alpha*t), R_tilde^(q*beta*t)`.  Transport the complete base
> ideals `(F,Z^d)` and `(G,Z^e)`, including both denominator sections, by an
> explicitly constructed chart map into the minimal simultaneous point
> resolution.  It produces a named proper or infinitely-near center `p`
> such that, after stripping the recorded exceptional factors, the generic
> mobile multiplicities obey (2.2).  The construction records the immediate
> proximity parents of `p` and is functorial under the next Laurent cut.

This is the **minimal sub-obstruction in the Corollary-7.4 packet-to-PCC
lane**: the bank cannot prove even the one-packet arrow before any summation
is attempted.  A different global route, such as log ramification, could
bypass this arrow and prove the TD bound directly.

If WTC-1 is proved, a second statement is still required.

> **CONJECTURE PCC-COVER (coverage and no double counting).** The packet
> centers produced along all cuts can be identified or separated according
> to their actual proximity ancestry so that integers `c_p <= h_p` satisfy
> \[
> \sum_pc_p^2\ge B^2-1.\tag{2.3}
> \]

Repeated visibility of one factor cannot be summed as if it supplied new
centers.  Conversely, successive transforms of a factor can contribute at
successive infinitely-near centers only after the blowup charts prove that
ancestry.  In point-basis language the target is the one-unit residual
point-basis energy bound

\[
B^2-\sum_ph_p^2\le1.\tag{2.4}
\]

None of the current inputs bounds this residual.

### 2.3 Why FC5 stops before WTC-1

The exact FC5 emission is

\[
w_G=\frac{\bar\kappa_G(d_q-1)}{\nu_Gd_q},\qquad
M_G=\gcd(d_p,d_q).\tag{2.5}
\]

At a pole,

\[
\Phi_s(w,M):=\frac{wM^2}{sM-1}=\frac{ab}{\nu},
\qquad
\frac{\operatorname{td}}{\alpha\beta}
=\sum_{P\text{ pole}}\Phi_s(w_P,M_P).\tag{2.6}
\]

Equations (2.5)-(2.6) are exact, but FC5 consumes a local frame and emits
only two scalars.  It contains no incoming pole mass, root position,
ordinary center, exceptional divisor, proximity relation, or cross-chart
identifier.  Moreover `Phi_s` is geometric only at poles and is
nonmonotone on internal coefficient-solvable charts in both directions.
Thus FC5 identifies the scalar quantity that the global geometry must
control, but cannot place any contribution into `(R_p,S_p)`.

Source: `xmodel/sol-g5-emission.md:69-206,306-378` and the hostile audit at
`xmodel/grok-k-g5-review.md:375-494`.

### 2.4 Why the `w` depth invariant stops before WTC-1

On an `M=1` chain the bank proves

\[
w_{j+1}=w_j\frac{n}{(n-1)\nu+1}.\tag{2.7}
\]

Neutral steps preserve `w`; resonant steps contract it, so the cumulative
jump-cell menu is finite for a **fixed entry**.  This is useful depth
closure, but:

- the Puiseux denominator and endpoint frame are not bounded;
- the theorem does not bound distinct entries across the TD ladder;
- its printed scope excludes `M>=2` suffixes; and
- `w` has no banked point-cluster or proximity interpretation.

It therefore cannot construct the center in WTC-1.  See
`SHEET6-DEPTH.md:28-51,128-138,142-205,403-431`.

### 2.5 Why NF-M's Bezout theorem stops before WTC-1

For a **fixed** discrete `nu>=2` merge schema, NF-M reduces the local Fuchs
equation to `Qhat-1` homogeneous equations in `Qhat-1` essential orbit
variables.  The equation of index `j` has degree `Qhat-j`, giving the
projective Bezout bound

\[
(\widehat Q-1)!\tag{2.8}
\]

on zero-dimensional coefficient types modulo permutation and scaling.
Positive-dimensional components are retained, and future locality requires
the same type **and the same emitted frame**.

This Bezout theorem counts local coefficient decorations after a schema and
emitted frame have already been fixed.  It does not count base centers,
identify `I_infinity`, or produce a point-basis vector.  In particular, it
supplies no uniform bound while those discrete inputs—and hence the
`B`-related degree data—vary.  NF-M can certify a factor `R_tilde` after a
center dictionary exists; it cannot create that dictionary.  See
`NF-M.md:31-129,257-272`.

### 2.6 Exact scale-loss control

For

\[
A=30t+5,
\]

the bank contains a formal type-`(2,3)` one-pole arithmetic schema with

\[
(a,b,\nu)=(A,2,3),\qquad
\operatorname{td}=4A,\qquad \frac{ab}{\nu}=\frac{2A}{3},\tag{2.9}
\]

but a locally admissible IIa step emits the constant state

\[
(w,M)=(2/3,3).\tag{2.10}
\]

The child has `Qhat=2` and one NF-M type for every `A`.  The parent and
child coefficient symbols are intentionally independent because the
missing parent-to-child substitution/gluing is not banked.

This is **not** a Keller counterexample and is not claimed globally
realizable.  It is an exact quantifier control: FC5 plus the displayed
local arithmetic, local ODEs, depth closure, and finite NF-M type count do
not imply PCC, SP, or even a finite type-`(2,3)` bound.  A proof must use
the omitted cross-chart gluing and global base-cluster information.  See
`xmodel/sol-g5-emission.md:387-520,621-676` and
`xmodel/grok-k-g5-review.md:432-496`.

### 2.7 Why the 21-of-22 census is not coverage

If `q` is the number of pole vertices, the pole laws give

\[
\operatorname{td}=\sum_i\Lambda_i,\qquad \Lambda_i\ge\beta.
\]

Thus `q>alpha` violates TD-BOUND immediately.  If `q=alpha`, equality
requires every pole to be beta-minimal, and MP4 then forces every `b_i=1`;
an off-axis row with `q=alpha` also violates automatically.  These two
selection rules force 21 of the 22 recorded violations.  The census has no
`R_p,S_p`, no proximity matrix, and no realizability theorem.  Its
frequency is therefore a construction effect, not evidence for (2.3).

The one-pole cap `ab<=nu` is the mandatory smallest sector test for any
emission proof, but it is exactly TD-BOUND in the one-pole sector.  It is
not a substitute for PCC.  See `TDBOUND.md:7-20`,
`xmodel/sol-g5-emission.md:884-918`, and
`xmodel/sol-tdbound-review.md:211-257`.

### 2.8 Ranked routes

| rank | route | what it could establish | priority | difficulty |
|---:|---|---|---|---:|
| 1 | Complete ideals and proximity | Principalize `(F,Z^d)` and `(G,Z^e)`, transport each Corollary 7.4 factor through explicit toric/blowup charts, compute the point-basis/proximity matrix, and prove residual energy (2.4). This attacks PCC directly and enforces no-double-counting naturally. | HIGH | 8.5/10 |
| 2 | Log ramification/Jacobian divisor | On `Phi:X -> P1 x P1`, use `K_X-Phi^*K` and boundary ramification to force `Delta^2 >= -2`. This may bypass floors and PCC, but targets the TD/KME statement directly. | HIGH | 9/10 |
| 3 | Exact one-pole gluing stress test | Write the actual Puiseux/chart substitution for the `A`-family in one coefficient ring, impose both local equations, and eliminate. A contradiction would kill this sharp scale-loss schema; without a completeness theorem it would not prove any broader SP sector, much less PCC. | HIGH diagnostic | 7.5/10 |
| 4 | Vector-valued FC5 | Enrich the state by point-basis increments and proximity parents, then seek a telescope. Scalar `(w,M)` is proved insufficient; this route becomes meaningful only after WTC-1. | MEDIUM | 9/10 |
| 5 | More NF-M or census enumeration alone | Useful for fixed-schema falsification and regression only. The one-type-for-every-`A` family prevents a uniform proof from these counts. | LOW | not a viable uniform proof |

For the common-power route, the most economical next target is WTC-1 in one
explicit Corollary 7.4 chart, including its point-basis and proximity
output.  Trying to prove the global square sum within that route before the
local dictionary exists reverses the logical dependency.

---

## 3. The radical-fiber group

### 3.1 The 36-point torsor

At either split prime, fix the chosen square root `r` of 3 and a primitive
cube root `omega`.  The selector algebra is

\[
B_{36}=\mathbb F_p[A_1,A_2,h_1,h_2]/
\left(A_1^3-(3+r),A_2^3-(3-r),2h_1^2-3,2h_2^2-3\right)
\simeq\mathbb F_p^{36}.\tag{3.1}
\]

Here `h_i=HW_i/W_i`.  Its components are labeled

```text
a{i}{j}{s1}{s2},     i,j in Z/3,     s1,s2 in {p,m}.
```

Define

\[
G=(\mathbb Z/3)^2\times(\mathbb Z/2)^2
\]

and, for `g=(a,b,e1,e2)`, let

\[
g:(i,j,s_1,s_2)\longmapsto
(i+a,j+b,(-1)^{e_1}s_1,(-1)^{e_2}s_2).\tag{3.2}
\]

Equivalently on selectors,

\[
(A_1,A_2,h_1,h_2)\longmapsto
(\omega^aA_1,\omega^bA_2,(-1)^{e_1}h_1,(-1)^{e_2}h_2).\tag{3.3}
\]

The action is free and transitive, so the 36 points form one `G`-torsor.

For `p=105337`, exact atlas data give

\[
\omega=15094,\quad\omega^2=90242,
\]

and the `a00pp` selector point is

\[
(A_1,A_2,h_1,h_2)=(50630,10114,50267,50267).\tag{3.4}
\]

Every JSON fiber is exactly

\[
(\omega^iA_1,\omega^jA_2,s_1h_1,s_2h_2).
\]

At `p=105673`, independently,

\[
\omega=13168,\quad\omega^2=92504,
\]

with base point

\[
(38664,46664,35053,35053),\tag{3.5}
\]

and the same law.

### 3.2 What the atlas coefficient classes mean

Put `Delta=x57-x65`.  The exact modular template replayed on all atlas
fibers is

\[
\begin{aligned}
g_1={}&\Delta^2uW_1^2
-2(r+2)h_1\frac{A_1}{A_2}x_{53}uW_1
+\left(\frac92+3r\right)A_1^2x_{72},\\
g_2={}&\Delta^2uW_2^2
-2h_2x_{58}uW_2
+\left(\frac92-3r\right)A_2^2x_{72},\\
g_3={}&x_{70}+(r-2)\frac{A_2}{A_1}x_{72}.
\end{aligned}\tag{3.6}
\]

Consequently the literal coefficient arrays have the census

| rows | dependence | distinct arrays | multiplicity |
|---|---|---:|---:|
| `g1` | `(i,j,s1)` | 18 | 2 |
| `g2` | `(j,s2)` | 6 | 6 |
| `g3` | `(j-i) mod 3` | 3 | 12 |
| joint triple | all four labels | 36 | 1 |

This is the atlas's `(j-i) mod 3` organization.  The joint arrays are
literally distinct, but (3.6) suggests character covariance rather than 36
unrelated systems.  The next computation proves exactly that.

The template is a modular identity on the banked split fibers; it is not,
by itself, promoted to a characteristic-zero ideal identity.  Its prior
audit is at `xmodel/sol-conjecture-k.md:195-241`.

---

## 4. Actual action on the D25 objects

### 4.1 Convention

Fix the **geometric source-to-target convention**

\[
T_g:X_\lambda\longrightarrow X_{g\lambda},\qquad y=T_gx.\tag{4.1}
\]

Thus the target equations are evaluated at the scaled source point.  If an
inverse pullback convention is used instead, every cube exponent `1` and
`2` below is exchanged.

### 4.2 Diagonal coordinate lift

For the generator `rho1:(i,j)->(i+1,j)`, `T_rho1` multiplies by `omega^2`
on

```text
x33 x16 x19 x70 x54 x63 W1
```

and by `omega` on

```text
x52 x55 x62 uW1.
```

For `rho2:(i,j)->(i,j+1)`, it multiplies by `omega^2` on

```text
x38 x24 x27 x72 x59 x66 W2
```

and by `omega` on

```text
x47 x57 x60 x65 uW2.
```

For the first sign generator `sigma1`, it negates

```text
x16 x53 x55.
```

For `sigma2`, it negates

```text
x24 x58 x60.
```

All omitted D25 variables are fixed.  On the union-family selector
variables, generator by generator,

\[
\begin{array}{c|c}
\rho_1&A1r\mapsto\omega A1r\\
\rho_2&A2r\mapsto\omega A2r\\
\sigma_1&h1r\mapsto-h1r\\
\sigma_2&h2r\mapsto-h2r
\end{array}\tag{4.2}
\]

Every other selector variable is fixed under the named generator.

Powers and products give `T_g` for every `g`.  There is **no variable
permutation and no row permutation**.

There is a harmless `2^2` lift ambiguity from sign chart gauges that act
trivially on the selector labels.  The canonical lift above fixes `W_i`
under `sigma_i` and flips `HW_i`; it is the convention used in all exact
identities below.

### 4.3 Exact row characters

Order the 34 parked D25 equations as

```text
core0..core25 | g1,g2,g3 | R1..R5.
```

Their two cube-character vectors are the checksum strings

```text
rho1: 10011112222200000011111100 | 202 | 00000
rho2: 10011112222220000011111100 | 210 | 00000
```

and both sign-character vectors are all zero.  Writing these exponents as
`d1_ell,d2_ell` for equation index `ell`, the exact identity is

\[
\boxed{
F_{\ell,g\lambda}(T_gx)
=\omega^{a d_{1\ell}+b d_{2\ell}}F_{\ell,\lambda}(x)
}\tag{4.3}
\]

for `g=(a,b,e1,e2)`.  The sign characters are one, because coefficient
sign changes are compensated by the displayed variable sign changes.
Every multiplier in (4.3) is a unit, so

\[
T_g^*I_{25}(g\lambda)=I_{25}(\lambda)\tag{4.4}
\]

and `T_g` is a scheme isomorphism, not merely a support bijection.

For a concrete first-prime edge, `a00pp -> a10pp`, the `g1` coefficient of
`x53*uW1` changes

```text
50008 -> 81147 = omega*50008,
```

while `uW1` itself gains another `omega`; the row therefore gains
`omega^2`, as its character says.  The `x72` coefficient changes

```text
103704 -> 1277 = omega^2*103704.
```

For `a00pp -> a00mp`, `50008 -> 55329 = -50008`, while `x53` also changes
sign, leaving the row invariant.

### 4.4 Exact finite checks

The following were computed with integer modular arithmetic and monomial
dictionaries, not numerical sampling.

- At `p=105337`, all
  `36 fibers * 4 generators * 34 rows = 4896` identities (4.3) pass.
- The independent `p=105673` compilation gives another 4896, all passing.
- Total: **9792 exact row identities, zero failures**.
- Each parked file has 34 rows, 28 variables, and 6096 monomial terms.
  Comparing all 72 files term by term gives **438,912 coefficient checks**,
  zero failures.
- Both 38-row union files `cases/d25fam_p{105337,105673}.ms`, including the
  four selector laws, are rowwise semi-invariant under the total-space
  action.
- The exact source bank `directionb_tails_D21.pkl` contains 183 registry
  variables, 77 raw `Row_k[eta^n]` cells, and 43,574 radical-expanded
  monomial terms.  Every term has the predicted weight under all four
  generators, with zero failures.

This upgrades the atlas's support identity to exact coefficient covariance.

Earlier unsplit presentations contain the auxiliary equation

\[
u_A(A_1-A_2)=1,
\]

which is not a character-homogeneous row under independent cube rotations.
It transports fiberwise by

\[
u_A'=
\frac{A_1-A_2}{\omega^aA_1-\omega^bA_2}\,u_A.\tag{4.5}
\]

The denominator is nonzero on all 36 fibers because `A1^3 != A2^3`.
Thus this is a removable chart-coordinate nuisance, not a broken orbit.
The folded D25 systems have already eliminated it.

---

## 5. All-depth source equivariance

### 5.1 Uniform level rule

Work after adjoining a primitive 42nd root `zeta`, and put

\[
\omega=\zeta^{14},\qquad
C_c\!\left(\sum_\ell y_\ell t^\ell\right)
=\sum_\ell\zeta^{c\ell}y_\ell t^\ell.\tag{5.1}
\]

For branch `i`, define:

- `rho_i` by applying `C_{-14}` simultaneously to `P_i`, `Gp_i`, and
  `G0p_i`; equivalently every branch-`i` absolute-level coefficient
  `y_l` is multiplied by `omega^{-l}`;
- `sigma_i` by applying `C_21` to `Gp_i` only; equivalently
  `y_l -> (-1)^l y_l` in that stream.

All `B`, `GB42`, and `GB21` streams are fixed.  The shared prefix levels
18, 24, and 30 are cube-fixed.  Shared branch merge variables occur at
levels for which the simultaneous assignments agree, so the action is
well-defined on the registry.

In particular,

\[
A_i\ (\ell=32)\mapsto\omega A_i,\qquad
W_i,HW_i\ (\ell=37)\mapsto\omega^2(W_i,HW_i),\tag{5.2}
\]

so `h_i=HW_i/W_i` is cube-fixed, while `uW_i -> omega*uW_i`.  The sign
generator fixes `A_i,W_i`, flips `HW_i`, and hence flips `h_i`.

### 5.2 Proof by branch reindexing

In `cases/r1_experiment.py:357-407,501-590`, the factors in a selected outer
direction have phases

\[
c=k+7j.
\]

Applying `C_{-14}` sends

\[
k+7j\longmapsto k+7(j-2),
\]

and applying `C_21` sends

\[
k+7j\longmapsto k+7(j+3).\tag{5.3}
\]

Both transformations preserve the outer direction `k` and merely permute
the internal factors in each complete 42- or 21-branch product.  On the
even 21-orbit support the sign action is trivial.  Hence the full orbit
products `Phi` and `Gamma` are unchanged after relabeling.

The raw Jacobian-depth equation in `cases/directionb_strike.py:36-58` is
built from `Phi`, `Gamma`, `eta`-derivatives, and the Euler operator
`theta=t*d/dt`.  The twists (5.1) commute with `theta`,
`eta`-differentiation, and truncation.  Therefore, for every truncation
depth `D`,

\[
F^D_{g\lambda}(T_gx)=E_gF^D_\lambda(x)\tag{5.4}
\]

for an invertible diagonal row-character matrix `E_g` (the pristine raw
rows can be taken invariant).  `B`-freezing, zero pins, the level-42
`PIN42`, and the open conditions `W_i != 0` are stable.

> **THEOREM (scoped all-depth equivariance).** Over a splitting field in
> which the pristine source construction and its banked denominators are
> defined and 42 is invertible, the residue-A, fixed-`r`, `B`-frozen,
> no-log, `PIN42`, `W`-chart depth ideal is `G`-equivariant at every
> truncation depth.  Its 36 radical fibers are one orbit of isomorphic
> schemes.

Adjoining `zeta` is a proof device: the branch permutation descends to the
displayed `omega` and sign scalings on the invariant coefficient objects.

### 5.3 Consequences for banked algebraic operations

Let `D_g` be the diagonal coordinate matrix of `T_g` and `E_g` the row
matrix in (5.4).

1. **Groebner bases and normal forms.** Diagonal scaling preserves every
   monomial and the monomial order.  Uniqueness of a reduced monic basis
   implies that the target basis is the transformed source basis followed
   by leading-coefficient normalization.  Leading monomials and
   elementwise supports are therefore identical.  This explains the
   397-element D21 and 509-element D23 atlas support identities.  Normal
   forms commute with transport.

2. **Jacobians and minors.** Differentiating
   `F_{g lambda}(D_g x)=E_g F_lambda(x)` gives
   \[
   J_{g\lambda}(D_gx)D_g=E_gJ_\lambda(x).\tag{5.5}
   \]
   Ranks, tangent/conormal dimensions, and determinantal conditions are
   unchanged.

3. **Schur and pivot operations.** Affine blocks acquire only invertible
   diagonal row and column factors.  Unit pivots, ranks, left kernels,
   compatibility rows, and backsolves transport.

4. **Saturation.** For the induced ring automorphism `S_g`,
   \[
   S_g(I:q^\infty)=S_g(I):(S_gq)^\infty.\tag{5.6}
   \]
   The annihilator must itself be transported; one must not reuse the same
   printed coefficients on a different fiber.

5. **Witnesses.** Since `omega` and `±1` lie in each split prime field,
   every banked `a00pp` rational witness transports to rational witnesses
   on the other 35 fibers.  Transporting the six D23 witnesses and checking
   the first 29 equations gave 216 fiber-witness checks per prime, all zero
   (432 total).

These statements concern algebraic presentations at a fixed finite depth.
They do not prove DEPTH-STAB, a Hensel condition, existence of an inverse
limit point, algebraization, or a polynomial Keller pair.

---

## 6. Orbit count and D27+ gate

The action on labels has trivial stabilizer, hence

\[
\#(\Lambda/G)=1,\qquad |G|=36.\tag{6.1}
\]

For every faithful emitted depth system, any isomorphism-invariant solver
question—emptiness, dimension, degree, component count after corresponding
base change, rank defect, or existence of a point—has the same answer on
all 36 fibers.  A point or certificate on the representative transports
explicitly by `T_g`.

Thus the D27+ execution plan is:

1. compile one representative, normally `a00pp`;
2. verify the finite source-to-emission and character gates below;
3. solve that representative once per prime;
4. transport the result or certificate to the remaining 35 components.

The potential reduction is

\[
36\to1\quad\text{per prime},\qquad
72\to2\quad\text{for the two banked primes},\tag{6.2}
\]

or 97.22 percent fewer expensive per-fiber solves.  The primes themselves
are not in the same orbit.

> **CONJECTURE FUTURE-EMISSION FIDELITY.** A not-yet-built optimized D27+
> presentation obtained by pivoting, Schur reduction, normal forms,
> saturation, and gauge choices equals the localized pristine depth ideal
> and satisfies (5.4).

This gap is operational and finitely checkable.  A future compiler should
fail closed unless it passes:

1. an absolute-level weight registry for every retained variable and
   selector;
2. row homogeneity or the four generator-edge dictionary identities;
3. transport of every nonzero pin, chart denominator, and saturation
   polynomial;
4. both ideal inclusions for each optimized pivot/Schur replacement;
5. reduced-GB/NF round trips and leading-support checks; and
6. one independent second-prime replay before promoting a cross-prime
   structural claim.

The raw all-depth theorem means a failure of one of these gates diagnoses
the compiler/presentation; it is not evidence that mathematical
equivariance failed.

No action is claimed here between the two `r3` embeddings, between primes,
after swapping pole charts, after unfreezing `B`, or on other infinity
charts.  Those are separate symmetry or coverage questions.

---

## 7. Exact reproduction

The following read-only Python reproduces the 36-point orbit census and all
9792 parked D25 generator-edge identities.

```bash
python3 - <<'PY'
from pathlib import Path
from collections import Counter
import json

ROOT = Path('/Users/dc/code/math/jc72108')

# Geometric convention: source fiber -> target fiber i+1/j+1.
W = {
 'r1': {'x33':2,'x16':2,'x19':2,'x70':2,'x52':1,'x54':2,
        'x55':1,'x62':1,'x63':2,'W1':2,'uW1':1,'A1r':1},
 'r2': {'x38':2,'x24':2,'x27':2,'x72':2,'x47':1,'x57':1,
        'x59':2,'x60':1,'x65':1,'x66':2,'W2':2,'uW2':1,'A2r':1},
 's1': {'x16':1,'x53':1,'x55':1,'h1r':1},
 's2': {'x24':1,'x58':1,'x60':1,'h2r':1},
}
MOD = {'r1':3, 'r2':3, 's1':2, 's2':2}

def parse_ms(path):
    lines = path.read_text().splitlines()
    variables = [x.strip() for x in lines[0].split(',')]
    vi = {x:i for i,x in enumerate(variables)}
    p = int(lines[1])
    rows = []
    for row in '\n'.join(lines[2:]).strip().split(',\n'):
        data = {}
        for term in row.split('+'):
            factors = term.split('*')
            exponent = [0]*len(variables)
            coeff = int(factors.pop(0)) % p if factors[0].isdigit() else 1
            for factor in factors:
                if '^' in factor:
                    x, a = factor.split('^')
                    exponent[vi[x]] += int(a)
                else:
                    exponent[vi[factor]] += 1
            exponent = tuple(exponent)
            data[exponent] = (data.get(exponent,0)+coeff) % p
        rows.append({e:c for e,c in data.items() if c})
    return variables, p, rows

def next_label(label, generator):
    i, j = int(label[1]), int(label[2])
    s1, s2 = label[3], label[4]
    if generator == 'r1': i = (i+1) % 3
    if generator == 'r2': j = (j+1) % 3
    if generator == 's1': s1 = 'm' if s1 == 'p' else 'p'
    if generator == 's2': s2 = 'm' if s2 == 'p' else 'p'
    return f'a{i}{j}{s1}{s2}'

def scaled(row, scales, p):
    out = {}
    for exponent, coeff in row.items():
        value = coeff
        for a, scale in zip(exponent, scales):
            value = value * pow(scale, a, p) % p
        out[exponent] = value
    return out

total = 0
for p in (105337, 105673):
    atlas = json.loads(
        (ROOT/f'cases/d23_atlas_p{p}.json').read_text()
    )['fibers']
    labels = sorted(atlas)
    omega = min(x for x in range(2,p) if (x*x+x+1) % p == 0)

    # Selector-coordinate law.
    ref = atlas['a00pp']['fiber']
    h0 = ref['HW1_over_W1']
    bad = []
    for label in labels:
        fiber = atlas[label]['fiber']
        i, j = int(label[1]), int(label[2])
        want = {
          'A1': ref['A1']*pow(omega,i,p) % p,
          'A2': ref['A2']*pow(omega,j,p) % p,
          'HW1_over_W1': h0 if label[3]=='p' else -h0 % p,
          'HW2_over_W2': h0 if label[4]=='p' else -h0 % p,
        }
        if fiber != want:
            bad.append(label)

    # Orbit and atlas g-row census.
    components = []
    unseen = set(labels)
    while unseen:
        queue = [unseen.pop()]
        seen = set(queue)
        while queue:
            x = queue.pop()
            for generator in W:
                y = next_label(x,generator)
                if y not in seen:
                    seen.add(y)
                    unseen.discard(y)
                    queue.append(y)
        components.append(len(seen))
    classes = [Counter(z['g_rows'][k] for z in atlas.values())
               for k in range(3)]
    joint = Counter(tuple(z['g_rows']) for z in atlas.values())

    # Derive row characters from the union object; check all parked edges.
    master_vars, _, master_rows = parse_ms(ROOT/f'cases/d25fam_p{p}.ms')
    parked = {
      label: parse_ms(ROOT/f'cases/d25fam_p{p}_{label}.ms')
      for label in labels
    }
    identities = 0
    degree_strings = {}
    for generator in W:
        modulus = MOD[generator]
        weights = [W[generator].get(x,0) for x in master_vars]
        degrees = []
        for row in master_rows[:34]:
            ds = {sum(a*b for a,b in zip(e,weights)) % modulus
                  for e in row}
            assert len(ds) == 1, (p,generator,ds)
            degrees.append(ds.pop())
        degree_strings[generator] = ''.join(map(str,degrees))

        character = omega if modulus == 3 else p-1
        for label in labels:
            target_label = next_label(label,generator)
            variables, _, source = parked[label]
            target_vars, _, target = parked[target_label]
            assert variables == target_vars and len(source) == len(target) == 34
            scales = [pow(character,W[generator].get(x,0),p)
                      for x in variables]
            for row_index, (source_row,target_row) in enumerate(
                    zip(source,target)):
                lhs = scaled(target_row,scales,p)
                rhs = {e:c*pow(character,degrees[row_index],p) % p
                       for e,c in source_row.items()}
                assert lhs == rhs, (p,generator,label,target_label,row_index)
                identities += 1

    total += identities
    print('p=',p,'omega=',omega,'coordinate_bad=',bad,
          'orbit_sizes=',components)
    print('g_class_counts=',[len(c) for c in classes],
          'multiplicities=',[sorted(set(c.values())) for c in classes],
          'joint_classes=',len(joint))
    print('degrees=',degree_strings,'row_identities=',identities)

print('TOTAL_ROW_IDENTITIES=',total)
PY
```

Expected checksum output begins

```text
p= 105337 omega= 15094 coordinate_bad= [] orbit_sizes= [36]
g_class_counts= [18, 6, 3] multiplicities= [[2], [6], [12]] joint_classes= 36
degrees= {'r1': '1001111222220000001111110020200000',
          'r2': '1001111222222000001111110021000000',
          's1': '0000000000000000000000000000000000',
          's2': '0000000000000000000000000000000000'}
row_identities= 4896
p= 105673 omega= 13168 coordinate_bad= [] orbit_sizes= [36]
...
row_identities= 4896
TOTAL_ROW_IDENTITIES= 9792
```

The parser relies on the audited expanded msolve emission syntax: integer
coefficients, `+`, `*`, `^`, and no parentheses.  The 34 parked rows are
the 26 core rows, three `g` rows, and five residuals; the four selector
equations occur only in each 38-row union master.

The pre-existing bank gates were also replayed read-only:

```text
python3 cases/tdbound_scan.py       -> 6/6 PASS
python3 cases/depth_closure_check.py -> ALL PASS
python3 cases/nfm_check.py          -> 25/25 PASS
```

These regressions confirm the stated content of the bank; they do not fill
WTC-1 or PCC-COVER.

---

## 8. Final status ledger

| statement | status |
|---|---|
| PCC is sufficient for `td <= alpha*beta` | **PROVED** |
| PCC holds for every Sigray-normalized Keller pair | **CONJECTURE** |
| Corollary 7.4 common powers imply ordinary base multiplicities | **CONJECTURE WTC-1; minimal blocker in the packet-to-PCC lane** |
| Packet contributions cover squared mass `B^2-1` without duplication | **CONJECTURE PCC-COVER** |
| FC5 / `w` / NF-M / 21-of-22 imply PCC | **NO; their banked quantifiers/data are insufficient** |
| Atlas label action has one orbit of size 36 | **COMPUTED EXACTLY** |
| D25 parked equations are diagonally equivariant | **COMPUTED EXACTLY at both primes** |
| Pristine source depth ideals are equivariant at every depth | **PROVED by branch reindexing** |
| One representative solve suffices for a faithful emitted system | **PROVED** |
| Future optimized D27+ emissions are faithful equivariant presentations | **CONJECTURE FUTURE-EMISSION FIDELITY; finite gate** |
| Fiber equivariance proves DEPTH-STAB, a germ, or a Keller pair | **NO** |

No git operation was used.  This audit writes only this report.
