# UCD-A-min: degree minimality does not bound the type-`(2,3)` carrier

**Date:** 2026-08-23  
**Characteristic:** `0`  
**Inputs accepted as proved:** `xmodel/sol-k2c.md`,
`xmodel/sol-bdelay.md`, and `xmodel/sol-unify.md` (read in full).

**Tier convention.** **EXACT** means proved below or imported from those
inputs. **FORMAL** means exact H1/tree arithmetic without polynomial origin.
Every new uniform Keller assertion is labelled **CONJECTURE**.

## 0. Verdict

UCD-A-min is **not proved**. The degree-minimality attack has a decisive
negative outcome:

\[
 \boxed{\text{a type-}(2,3)\text{ rectangular cusp pair is already
 Aut-orbit degree-minimal at every common degree scale}.}                 \tag{0.1}
\]

Thus degree minimality supplies no bound

\[
 \deg f\leq \Phi(6,(2,3)).                                               \tag{0.2}
\]

This is not merely failure of the elementary shears. In characteristic zero
the coordinate-cusp theorem excludes a degree-lowering word in arbitrary
source and target polynomial automorphisms. The obstruction is specific to
reduced type with both entries bigger than one. It fails exactly for the
Hénon type `(1,2)` tower, where `V-U^2` is itself a coordinate and deletes
the last stage.

The prompt's removability principle therefore splits as follows.

* If an excess carrier is globally extractable as a Hénon coordinate tail,
  degree minimality removes it. This gives the conditional explicit bound
  `K_A=42` in Theorem 5.1.
* A local approximate root is not thereby a coordinate of
  `C[x,y]`. If the FORMAL residue-A insertion algebraizes while retaining the
  type-`(2,3)` rectangular frame, (0.1) says that it is necessarily a
  **non-removable** carrier. Minimality does not exclude it.

The constant-Jacobian and conductor attacks also stop sharply. At a
residue-A pole,

\[
 \operatorname{ord}_t f_y=3-\kappa_i,                                  \tag{0.3}
\]

and the local branch conductor satisfies

\[
 c(P_i)=2\delta(P_i)\geq2(\kappa_i-1).                                  \tag{0.4}
\]

Equation (0.3) is a compatibility identity, while (0.4) is a lower bound.
Neither gives the missing upper bound. The global genus/conductor budget
grows with the common polynomial degree, and degree six does not bound the
number of finite asymptotic punctures through Riemann--Hurwitz alone.

The single sufficient inequality left by the degree route is

> **CONJECTURE A-SCALE.** There is an integer `B_A` such that every orbitwise
> degree-minimal, nonautomorphic residue-A pair with Sigray rectangle base
> `(a,b)` satisfies
> \[
>     a+b\leq B_A.                                                        \tag{0.5}
> \]

It would give the explicit implication

\[
 \kappa_i\leq\deg f=2(a+b)\leq2B_A,qquad K_A=2B_A.                      \tag{0.6}
\]

No present identity proves (0.5). The coordinate-cusp theorem proves that
automorphism minimality alone cannot prove it.

## 1. Exact carrier and degree coordinates

For a residue-A pole the characteristic-index ladder is

\[
 1\xrightarrow{\,7\,}7\xrightarrow{\,3\,}21
  \xrightarrow{\,2\,}42.                                                \tag{1.1}
\]

For a primitive Puiseux series, the gcd dictionary is

\[
 \prod_j\nu_j=\kappa_i.                                                  \tag{1.2}
\]

The self-reproducing FORMAL `l=0` direction therefore gives, using repeated
`nu=2`,

\[
 \kappa_i(r)=42\cdot2^r.                                                 \tag{1.3}
\]

It leaves the two pole entries `(a_P,b_P,nu_P)=(1,1,2)`, hence

\[
 \mathcal E_{\rm MR}=1,qquad \operatorname{td}=6,qquad \deg\Psi=36,   \tag{1.4}
\]

unchanged at H1 tier.

Write the positive base corner of a Sigray type-`(2,3)` rectangular pair as
`(a,b)`. Thus

\[
\begin{aligned}
 \operatorname{Supp}f&\subseteq[0,2a]\times[0,2b],
 & [x^{2a}y^{2b}]f&\ne0,\\
 \operatorname{Supp}g&\subseteq[0,3a]\times[0,3b],
 & [x^{3a}y^{3b}]g&\ne0.
\end{aligned}                                                            \tag{1.5}
\]

Put `B=a+b`. The northeast terms in (1.5) give exactly

\[
 d_f=2B,qquad d_g=3B.                                                    \tag{1.6}
\]

Polynomial origin gives the fixed-degree bound

\[
 \kappa_i\leq d_f=2B,qquad
 \#\{\text{characteristic vertices on }P_i\}
 \leq\lfloor\log_2(2B)\rfloor.                                         \tag{1.7}
\]

Consequently the entire issue is whether `td=6`, type `(2,3)`,
nonautomorphy, and orbitwise minimality bound `B`. Section 2 proves that
orbitwise minimality by itself does not even constrain `B`.

For the filed residue-A scale,

\[
 (a,b)=(63,21),\quad B=84,\quad
 (d_f,d_g)=(168,252),\quad \kappa_i=42.                                  \tag{1.8}
\]

## 2. Degree minimality versus global coordinate extraction

### Lemma 2.1 -- removable tails are incompatible with minimality (**EXACT**)

Let `F=(f,g)` be lexicographically minimal in its
`Aut(A^2) x Aut(A^2)` source/target orbit. Suppose an excess carrier stage is
globally represented by a polynomial automorphism `A` and there is a pair
`F^-` such that

\[
 F=K\circ F^-\circ A\circ L,qquad
 \deg F^-<_{\rm lex}\deg F,                                             \tag{2.1}
\]

for polynomial automorphisms `K,L`. Then the carrier cannot occur.

**Proof.** Equation (2.1) puts `F^-` in the same source/target orbit as `F`
with smaller degree pair, contradicting minimality. In particular this
applies to a genuine Hénon tail

\[
 H_q(U,V)=(V,V^q-U),\qquad
 H_q^{-1}(U,V)=(U^q-V,U).                                                \tag{2.2}
\]

Both maps in (2.2) are polynomial automorphisms with Jacobian `1`.
\(\square\)

The missing converse is load-bearing: an approximate root in the completed
local ring of one pole need not be a coordinate of `C[x,y]`, need not have a
polynomial coordinate mate, and need not split off as (2.1).

### Theorem 2.2 -- type-`(2,3)` cusp protection (**EXACT**)

Every pair satisfying (1.5) is lexicographically degree-minimal in its full
source/target polynomial-automorphism orbit. The assertion is independent of
the Jacobian condition and holds for every positive `a,b`.

**Proof.** Give target variables `(U,V)` weights `(2,3)`. Let
`L=(u,v)` be a source automorphism and set

\[
 D_L=a\deg u+b\deg v\geq a+b,qquad
 H=u_+^av_+^b,                                                           \tag{2.3}
\]

where `u_+,v_+` are the top ordinary homogeneous forms. The northeast
monomials in (1.5) are unique maximizers for the positive functional
`(i,j) \mapsto i deg u+j deg v`; hence

\[
 (f\circ L)_+=cH^2,qquad (g\circ L)_+=dH^3,qquad c,d\ne0.              \tag{2.4}
\]

For a target coordinate `h(U,V)`, cancellation at the expected top degree
would require

\[
 \operatorname{in}_{2,3}h(cZ^2,dZ^3)=0.                                \tag{2.5}
\]

The kernel of the cusp substitution in (2.5) is

\[
 (d^2U^3-c^3V^2).                                                       \tag{2.6}
\]

No coordinate has weighted initial form in (2.6). For completeness, take a
coordinate mate of \(h\) and the locally nilpotent derivation

\[
 \partial=J(h,-).
\]

Its top weighted part is \(D=J(\operatorname{in}h,-)\), again a nonzero
LND. The LND degree is additive on products, so `ker D` is factorially
closed. If the cusp binomial in (2.6) divided `in h`, factorial closure
would put that binomial in `ker D`. Neither \(D(U)\) nor \(D(V)\) vanishes:
the equation \(D(B)=0\) for the binomial \(B\) in (2.6) makes them vanish
together, which would contradict \(D\ne0\). Writing

\[
 p=\deg_D U,\qquad q=\deg_D V
\]

then forces

\[
 p-1\geq q,qquad q-1\geq2p,                                           \tag{2.7}
\]

which is impossible. This is the characteristic-zero coordinate-cusp
exclusion.

Therefore

\[
 \deg h(f\circ L,g\circ L)=D_L\deg_{2,3}h.                              \tag{2.8}
\]

If `K=(h_1,h_2)` is a target automorphism, its first coordinate has weighted
degree at least `2`. Equality forces it to be affine linear in `U`; its mate
then has a nonzero `V` term and weighted degree at least `3`. Equations
(2.3) and (2.8) give

\[
 \deg\bigl(K\circ(f,g)\circ L\bigr)
 \geq_{\rm lex}(2(a+b),3(a+b)).                                        \tag{2.9}
\]

The original pair attains equality. \(\square\)

### Consequence

There is no implication

\[
 \text{orbitwise degree-minimal}+(\operatorname{td},\text{type})
 \Longrightarrow B\leq B_A                                            \tag{2.10}
\]

from automorphism theory or leading forms. Theorem 2.2 certifies minimality
for every value of `B`; it does not assert polynomial existence for any new
residue-A scale.

This corrects the proposed picture. Minimality has already disposed of
**globally removable** insertions by Lemma 2.1. Any polynomial realization of
the H1 carrier extension inside (1.5) would, by Theorem 2.2, be a genuinely
non-removable insertion. Prohibiting those realizations is the content of the
new Keller theorem, not a consequence of minimization.

## 3. Constant Jacobian on a residue-A pole

Let `t` be the primitive parameter of a residue-A pole branch of a generic
fiber `f=a_0`. Write

\[
 \operatorname{ord}_t x=-\kappa_i,qquad
 \operatorname{ord}_t g=-3.                                            \tag{3.1}
\]

The second equality is the pole-order-three half of the fixed two-pole
inventory `(3,3)`, whose sum is `td=6`.

Along the fiber,

\[
 f_xx'+f_yy'=0,qquad
 g'=g_xx'+g_yy'=-j\frac{x'}{f_y}                                      \tag{3.2}
\]

for \(J(f,g)=j\in\mathbf C^*\). Characteristic zero prevents cancellation of
the derivative of a leading Laurent monomial, so

\[
 \operatorname{ord}_t x'=-\kappa_i-1,qquad
 \operatorname{ord}_t g'=-4.                                          \tag{3.3}
\]

Taking orders in (3.2) proves the exact identity

\[
 \boxed{\operatorname{ord}_t f_y=3-\kappa_i.}                           \tag{3.4}
\]

At the filed scale, (3.4) is `3-42=-39`, the independently banked
zero-slack valuation.

Equation (3.4) does constrain the entire contact sum in the product formula
for `f_y`. It does not bound `kappa_i`: as a scalar valuation equation it is
arithmetically compatible with every `kappa_i` once the degree/contact table
is allowed to grow. In the Sigray frame the homogenized boundary equation is

\[
 F_XG_Y-F_YG_X=jZ^{d_f+d_g-2}=jZ^{5B-2}.                               \tag{3.5}
\]

Thus increasing the carrier scale also increases the number of boundary
cancellation equations. There is no fixed-order system attached only to
`td=6`.

The `A_4` passport does not add the missing order. It belongs to the
degree-four quotient after the exact cancellation

\[
 \frac{(C^4h_1)^3}{(C^3f)^4}=\frac{h_1^3}{f^4}.                         \tag{3.6}
\]

The characteristic denominator of the carrier `C` is absent from (3.6).
The two-pole handshake fixes the pole order `3` in (3.1); (3.4) shows
directly that it does not fix the pole order `kappa_i` of `x`.

Hence a stopping theorem for successive Puiseux coefficients would be a new
uniform no-solution theorem for (3.5) as \(B\to\infty\). Neither the pure
boundary identity nor the fixed passport contains such a theorem.

## 4. Semigroup and conductor: the available inequality has the wrong sign

In the projective pole chart, after subtracting the tangent, a residue-A
branch has a parametrization beginning with

\[
 z=t^{\kappa_i},\qquad w=\text{terms of order }>\kappa_i.               \tag{4.1}
\]

Thus its local value semigroup has multiplicity `kappa_i`. The integers
`1,...,kappa_i-1` are gaps. For a plane branch the number of semigroup gaps
is `delta(P_i)` and the semigroup is symmetric, so its conductor is
`c(P_i)=2 delta(P_i)`. Therefore

\[
 \delta(P_i)\geq\kappa_i-1,qquad
 c(P_i)\geq2(\kappa_i-1),qquad
 \kappa_i\leq\frac{c(P_i)}2+1.                                       \tag{4.2}
\]

At the filed residue-A pole,

\[
 \kappa_i=42,qquad \delta(P_i)=1139,qquad c(P_i)=2278,                \tag{4.3}
\]

so (4.2) has enormous slack: \(2278\geq82\).

The relevant global identities give no fixed upper bound on (4.3). A generic
fiber is affine-smooth because \(df\) never vanishes under
\(J(f,g)\in\mathbf C^*\).
For its degree-`2B` projective closure,

\[
 \sum_{q\in L_\infty}\delta_q
 =\frac{(2B-1)(2B-2)}2-g(\overline C),                                \tag{4.4}
\]

where `delta_q` includes branch deltas and pairwise intersections at each
infinity point. The right side grows quadratically with `B`.

On the intrinsic normalization, `g` has degree `6`, no affine ramification,
and pole partition `(3,3)`. Riemann--Hurwitz gives

\[
 g(\overline C)
 =-3+\frac12\sum_{q\in D_{\rm fin}}(e_q-1),
 \qquad
 \sum_{q\in D_{\rm fin}}(e_q-1)=2g+6.                                \tag{4.5}
\]

Here `D_fin` consists of punctures at which `g` has a finite asymptotic
value. Degree six bounds each `e_q` by `6`, but it does not bound the number
of such punctures. The fixed residual passport again forgets them after
carrier cancellation.

Therefore positive conductor prices a carrier only if one first proves an
upper conductor budget. The required multi-place substitute would be:

> **CONJECTURE A-CONDUCTOR.** There is an integer `C_A` such that every
> orbitwise degree-minimal, nonautomorphic residue-A pair satisfies
> \[
>     c(P_i)\leq C_A\quad(i=1,2).                                      \tag{4.6}
> \]

By (4.2), (4.6) would give

\[
 K_A=\left\lfloor\frac{C_A}{2}\right\rfloor+1.                        \tag{4.7}
\]

No one-place Abhyankar--Moh inequality proves (4.6): the generic fiber is
multi-place, and its pole branches lie on the local side of the one-place
inequality. Applying one-place theory to components of the nonproperness set
does not identify their semigroups with `c(P_i)` and supplies no bound
independent of `B`.

Equations (4.4)--(4.5) identify the exact missing direction. One needs either
an upper bound on the common scale `B` as in A-SCALE, or a new inequality
charging each non-removable pole conductor increment to a global quantity
bounded independently of `B`. Existing degree, genus, and Riemann--Hurwitz
ledgers do not do this.

## 5. The strongest conditional result and explicit constant

Define the following genuinely additional hypothesis.

> **CONJECTURE GCT-A (global coordinate-tail extraction).** If a
> polynomial-origin residue-A pole contains a characteristic carrier beyond
> the fixed ladder `(7,3,2)`, an outermost excess carrier of index
> \(q\geq2\)
> globalizes to a Hénon coordinate tail (2.2), and applying its inverse gives
> a source/target equivalent Keller pair with lexicographically smaller
> degree pair.

### Theorem 5.1 -- UCD-A-min under GCT-A (**EXACT implication**)

Assume GCT-A. Then every degree-minimal residue-A pair has

\[
 \kappa_i=7\cdot3\cdot2=42,qquad K_A=42.                              \tag{5.1}
\]

Consequently

\[
 d_{\rm sh}\leq\lfloor\log_2 42\rfloor=5.                             \tag{5.2}
\]

**Proof.** If an excess carrier existed, GCT-A and Lemma 2.1 would produce a
smaller representative in the same orbit, contradicting degree minimality.
Only the fixed ladder (1.1) remains, and (1.2) gives (5.1). Equation (5.2)
is the proved depth dictionary. \(\square\)

GCT-A is not a reformulation of a local approximate-root fact. Its assertion
that the local root is a **global coordinate tail** is exactly the missing
algebraization/gluing statement. Theorem 2.2 shows why it cannot be obtained
from the type-`(2,3)` leading frame: that frame is protected against every
coordinate cancellation.

More generally, A-SCALE with a specified `B_A` gives

\[
 K_A=2B_A,qquad
 d_{\rm sh}\leq\lfloor\log_2(2B_A)\rfloor                            \tag{5.3}
\]

by (1.7). This is the exact requested degree-bound route, conditional on the
single missing inequality (0.5).

## 6. Hénon sanity gate

Every claimed mechanism above fails at the correct place for the automorphism
tower of `sol-k2c.md`.

1. Its reduced type is `(1,2)`, not `(2,3)`. The coordinate-cusp exclusion
   requires both weights greater than one. For `(1,2)`,
   \[
      h(U,V)=V-U^2
   \]
   is a coordinate and
   \[
      h(Z,Z^2)=0.                                                        \tag{6.1}
   \]
   Thus the exact step forbidden by Theorem 2.2 is available.
2. Each displayed recurrence stage is the polynomial automorphism `H_q`.
   Lemma 2.1 applies, so the displayed high-degree representative is not
   degree-minimal. Applying the inverse tower gives the identity pair, with
   degree pair `(1,1)` and pole denominator `1`.
3. Before minimization, the generic coordinate fiber has degree
   `kappa_r`, genus zero, and one singularity at infinity with
   \[
      \delta_\infty
      =\frac{(\kappa_r-1)(\kappa_r-2)}2.                                \tag{6.2}
   \]
   Hence even a large positive embedded conductor is not an Aut-orbit
   invariant. After minimization the fiber is a line and this conductor is
   zero.

Thus no assertion here would bound the nonminimal Hénon presentation. The
only conditional bound, Theorem 5.1, uses degree minimality exactly where the
Hénon family fails it. Conversely, Theorem 2.2 explains why the same escape
is unavailable merely from a type-`(2,3)` cusp leading form.

## 7. Final disposition

\[
\begin{array}{c|c}
\text{attack}&\text{verdict}\\ \hline
\text{degree minimality / approximate roots}
 &\text{removable tails die, but the }(2,3)\text{ cusp protects every scale}\\
J=\text{const}+\text{passport}+\text{handshake}
 &\operatorname{ord}_t f_y=3-\kappa_i;\ 
   Z\text{-order}=5B-2\text{ grows with }B\\
\text{semigroup / conductor}
 &c(P_i)\geq2(\kappa_i-1)\text{ is a lower bound; no fixed upper budget}
\end{array}                                                             \tag{7.1}
\]

There is no unconditional `K_A`. Under the explicit global-coordinate-tail
hypothesis, `K_A=42`; under the explicit scale bound \(B\leq B_A\),
`K_A=2B_A`.

The evidence does **not** presently support UCD-A-min as a consequence of
degree minimality, constant Jacobian, the tetrahedral passport, or ordinary
semigroup theory. The exact cusp theorem removes the main proposed source of
support: in reduced type `(2,3)`, degree minimality is automatic at arbitrary
common scale. Nonautomorphy forces the hypothetical pair into the nonproper
Keller sector, but no available nonproperness theorem turns that qualitative
fact into a scale or conductor ceiling. The conjecture may still be true
because the lower Puiseux coefficient equations might forbid every
large-scale polynomial Keller realization, but that is precisely the
unproved algebraization/exclusion wall.

\[
 \boxed{\textbf{UCD-A-min is itself the G2 crux; a counterexample sequence,
 if one exists, can live in the non-removable type-}(2,3)\textbf{ carrier
 direction.}}                                                          \tag{7.2}
\]
