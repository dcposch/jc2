# Provisional theorem: first-leg degree does not exclude a complete-base `A1` ruling

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`a1_p1_degree_obstruction` lane)  
Frozen basis: `00b2fb0c682c5ca2a056af588a29b2421c1b7ce4`  
Lifecycle: **PROVISIONAL SOURCE-AUDITED PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Verdict

In the setting of the provisional `A1`-ruling packet, the additional fact that
the actual first leg

```text
g_1:A2 -> U
```

is etale of generic degree `d_1>=2` does **not**, by itself, rule out the
complete-base branch `rho:U->P1`.  This is not merely a failure to find an
argument.  Miyanishi gives complete-base controls with a stronger source-map
hypothesis:

> There are smooth affine rational surfaces `X` with an `A1`-fibration
> `rho:X->P1`, all fibres irreducible, and a morphism `q:A2->X` which is
> etale and whose image contains every codimension-one point of `X`, with
> generic degree greater than one.

In particular, if the two multiple fibres have multiplicities `m_1|m_2` and
`m_2/m_1>1`, Miyanishi's lemma gives a **non-Galois** affine
pseudo-covering of exact degree `m_2`.  Taking `(m_1,m_2)=(2,4)` gives an
exact degree-four control.  If the two multiplicities are equal and greater
than one, a Galois affine pseudo-covering also exists; the case `(2,2)` gives
the degree-two cyclic control by the normalization/fundamental-group check in
Section 3.

Here "affine pseudo-covering" has the source's exact meaning: an etale
morphism of smooth affine varieties whose image contains every
codimension-one point.  It is therefore dominant, open, and quasi-finite, but
it is not asserted to be finite, proper, or surjective.  Confusing any of
those notions would destroy the control.

Consequently the old `F_n minus S` example can be strengthened from a
degree-one open immersion to genuine degree-`>1`, including non-Galois,
first-leg controls.  The proper cubic-block campaign must use data absent
from these controls.  The sharp extra package already available internally is
the **second etale leg**

```text
pi_U:U -> A2
```

of generic degree three, together with its extension to the fixed normal
finite-flat cubic algebra and the `(2A+3B; H,R)` compactification.  A cheap
necessary shadow is `K_U=0`; a stronger necessary shadow is that its unique
volume generator is an exact decomposable form.  Neither shadow should be
substituted for the full cubic-extension condition without proof.

Thus the sharp external control question is now two-sided:

```text
does any degree > 1 complete-base pseudo-cover control A2 -> X
also admit an etale morphism X -> A2?
```

An affirmative example would already compose to a Keller counterexample, so
the source controls do not answer this question.  They only show that the
first arrow cannot answer it alone.

## 1. Exact internal hypothesis under test

Charge the source-audited conclusions of

```text
xmodel/bd-a2-a1-ruling-euler-boundary-cap-sol56-20260830.md
```

only provisionally.  They give a smooth rational affine surface

```text
U = X minus Supp(H+R_X),
O(U)^* = C^*,                 bar-kappa(U)=-infinity,
rho:U -> C,                   C=A1 or P1,
```

and, for total ADE rank `r` and the number `c` of nonexceptional reduced
boundary carriers,

```text
e(U)=12-r-c.
```

In the complete-base branch,

```text
e(U)=2+sum_t(number Irr(rho^{-1}(t)_red)-1),
r+c<=10.
```

The actual block factorization supplies more than that packet used:

```text
A2 --g_1, etale quasi-finite of degree d_1>=2--> U
   --pi_U, etale quasi-finite of degree 3------> A2.
```

The question here is deliberately narrower: does the information on `g_1`
alone remove `C=P1`?  The answer is no.

## 2. Primary-source audit

The load-bearing source is:

1. M. Miyanishi, *Affine pseudo-coverings of algebraic surfaces*, Journal of
   Algebra **294** (2005), 156--176,
   `doi:10.1016/j.jalgebra.2005.01.042`.  The publisher abstract confirms the
   definition and that the paper studies precisely the cases in which the
   source or target is `A2`.
2. M. Miyanishi, *Affine pseudo-planes and affine pseudo-coverings*,
   Oberwolfach Reports **2** (2005), Report 19/2005, pp. 1110--1112.  This is
   an authored primary theorem summary.  Definition 2.5 and Lemmas 2.6--2.7
   state the complete-base controls used below.
3. M. Miyanishi, *Lectures on Geometry and Topology of Polynomials --
   Surrounding the Jacobian Conjecture*, arXiv:`1504.07179`, Section 2.5.
   This later primary exposition was used to crosscheck the exact distinction
   between a pseudo-covering, its finite normalization, and a finite etale
   cover; to audit the precise scope of the known reverse-direction
   exclusions; and to extract the canonical-class formula for an irreducible-
   fibre `P1` ruling.

The fetched source receipts were, without adding them to the repository,

```text
e35a88d8a33daa64b24b9120bd85aeca0c891869bfa79cdb81ef545a6acfd909
  Oberwolfach Report 19/2005 PDF, 493374 bytes;
ab4eb0cb74e4051e3fb1f702a253d29cb1a658632f11bc6f4b04a8bb9e7daaa4
  arXiv:1504.07179 PDF, 806236 bytes.
```

No claim below depends on a search-result paraphrase.  The exact definition
and both existence lemmas were read in the authored Oberwolfach text; the
later lecture notes were read through the relevant Section 2.5.

## 3. The degree-`>1` complete-base controls

Miyanishi starts with a smooth affine rational surface `X` carrying an
`A1`-fibration over a rational curve.  In Definition 2.5(2), a **cyclic
`A1`-fiber space** is such a surface with

```text
rho:X -> P1,
every fibre irreducible,
at most two multiple fibres.
```

If the multiple fibres are `m_1F_1,m_2F_2`, their reduced curves are affine
lines and

```text
pi_1(X) has order gcd(m_1,m_2).
```

The exact existence statements are:

* Lemma 2.6(1)(ii): if there are two multiple fibres of the same
  multiplicity `m>1`, then `A2` is a Galois affine pseudo-covering of `X`.
* Lemma 2.7: if `m_1|m_2` and `m_2/m_1>1`, then there is a non-Galois affine
  pseudo-covering

  ```text
  q:A2 -> X
  ```

  of exact generic degree `m_2`.

For the second statement choose `(m_1,m_2)=(2,4)`.  By the definition quoted
above, this gives all of

```text
q is an actual morphism;
q is etale everywhere;
q is quasi-finite and open;
q(A2) contains every codimension-one point of X;
q is dominant;
[C(x,y):C(X)] = 4;
the field extension is non-Galois.
```

Thus neither degree `d_1>=2`, Galois versus non-Galois monodromy, nor even
codimension-one surjectivity of the first-leg image excludes `P1`.

The equal-multiplicity case supplies the complementary Galois control.  For
`m=2`, nontriviality and degree two can also be read topologically: the
cyclic space has fundamental group `Z/2`, while a degree-one almost-surjective
etale map from simply connected `A2` would be an open immersion missing at
most finitely many points.  Removing finitely many points from a smooth
complex surface does not change its fundamental group, a contradiction.  On
the other hand, purity makes the finite normalization a finite etale cover,
whose degree divides `|pi_1(X)|=2`; hence its nontrivial degree is two.  This
is only a crosscheck: the non-Galois exact-degree-four row already settles the
theorem without it.

## 4. Match to the first-leg invariant package

The controls are at least as strong as the abstract first-leg package in every
relevant respect.

**Units.**  If `u in O(X)^*`, then `q^*u` is a unit in `C[x,y]`, hence a
scalar.  Dominance of `q` makes `u` the same scalar.  Therefore

```text
O(X)^*=C^*.
```

**Rationality and logarithmic Kodaira dimension.**  Rationality is part of
the source setup.  Miyanishi's Lemma 2.2(3) also directly gives negative
logarithmic Kodaira dimension from the source `A2`.  These are not loopholes
distinguishing the control from `U`.

**Euler number.**  Every reduced fibre is one affine line.  Scheme
multiplicity is invisible to topological Euler characteristic, so

```text
e(X)=e(P1)=2.
```

In the internal boundary identity this is the equality cell `r+c=10`.  The
control does not claim to realize any actual F5/ADE decoration with
`r+c=10`; it shows that no argument using only the displayed first-leg
invariants and `d_1>=2` can remove that cell.

**Image strength.**  The old `F_n minus S` control used an open immersion
`A2 subset X`, hence degree one.  Here `q(A2)` contains the generic point of
every prime divisor of `X` while the function-field degree is greater than one.  Replacing
"dominant" by "almost surjective" therefore does not rescue the proposed
obstruction.

## 5. Why the tempting generic-fibre argument fails

One cannot argue that `A1` has no connected finite etale cover of degree
greater than one and conclude `d_1=1`.  That argument silently inserts two
false hypotheses.

First, `q` is not asserted finite or proper.  An affine pseudo-covering is an
etale quasi-finite morphism with image complement of codimension at least
two; its finite normalization contains `A2` only as an open subset.  In a
non-Galois control, any ramification of that finite normalization is disjoint
from the `A2` open and can lie on its deleted boundary.  In a Galois control,
purity instead makes the finite normalization etale, while the original map
can remain nonfinite because `A2` is obtained by deleting affine-line boundary
curves upstairs.

Second, `q` need not preserve the ruling with the identity on `P1`.  In the
source construction the function-field degree can be horizontal: a ramified
cover of the completed base is normalized against the multiple fibres, and
the total surface map is etale because the base ramification is cancelled by
the fibre multiplicities.  Restricting to "the generic fibre" over the same
base field is therefore unlicensed.  After the correct base extension the
geometric generic fibre pieces can each map with degree one while the total
surface degree remains greater than one.

The distinctions are:

| property of `q:A2->X` | source control |
|---|---|
| morphism / dominant / quasi-finite / etale | yes |
| open image | yes, because etale |
| every codimension-one target point attained | yes |
| finite | not part of the theorem |
| proper | not part of the theorem |
| surjective on all closed points | not required |
| ruling-preserving over the identity of `P1` | not required |
| generic degree greater than one | yes; exact degree four in the `(2,4)` row |

## 6. The actual additional invariant and the finite successor

The controls settle what is **not** enough.  They do not realize the proper
cubic block, because the actual `U` also carries

```text
pi_U:U -> A2
```

which is etale of generic degree three and extends, after restoring the
deleted different, to the fixed normal finite-flat cubic algebra.  Composing
`pi_U` with `g_1` is the original Keller map.  Supplying both arrows for one
of the controls would therefore no longer be a harmless model: it would
already supply a JC2 counterexample.

There is a useful hierarchy of additional tests.

1. **Canonical class.**  Etaleness of `pi_U` forces

   ```text
   wedge^2 Omega_U^1 ~= pi_U^*(wedge^2 Omega_A2^1) ~= O_U,
   hence K_U~0.
   ```

   This is actual linear triviality, with a distinguished trivialization
   pulled back from `du wedge dv`, not merely a statement that some further
   pullback of `K_U` is trivial.

   Miyanishi gives a concrete version of this filter.  For any smooth affine
   `A1`-fibration `rho:X->P1` with all fibres irreducible, take his adapted
   completion `V`, obtained from a ruled surface `Sigma_n`.  If the image of
   the horizontal boundary is `T~M+a ell`, the multiple fibres are `m_iF_i`,
   and `k_i` is the coefficient of the completed `F_i` in `K_V`, his equation
   (1) reads in `Pic(X) tensor Q`

   ```text
   [K_X] = I[ell|_X],
   I = 2a-n-2 + sum_i(k_i/m_i).                         (6.1)
   ```

   Here `a=0` or `a>=n`, and the same source records `k_i>m_i`.  For a cyclic
   two-multiple-fibre control, `Pic(X)/Pic(X)_tor` has rank one, so `I!=0`
   proves `K_X` nontrivial.  In particular, if `T!=M` then

   ```text
   I > 2a-n >= n >= 0,
   ```

   and no reverse etale map to `A2` is possible.  Only the `T=M` rows can
   survive the rational canonical test, and they must satisfy

   ```text
   k_1/m_1 + k_2/m_2 = n+2.                            (6.2)
   ```

   Even (6.2) kills only the free part: exact `K_X~0` still requires the
   torsion class to vanish in the integral boundary lattice.

   Miyanishi's Oberwolfach Theorem 2.9 excludes reverse etale maps for
   `ML_0` affine pseudo-planes and Platonic `A1`-fiber spaces.  The expanded
   Theorem 2.5.6 and Remark 2.5.9 in the later lectures exclude etale maps
   from the same classes (with the unresolved Platonic sequence `{2,2,m}`
   for `m>5`) even to any affine surface with trivial canonical divisor.
   Theorem 2.5.10 further says that an affine pseudo-plane of type `(d,n,r)`
   mapping etale to `A2` must have `r=2` (this is Miyanishi's type parameter,
   not the ADE rank used elsewhere in this report).  None of these theorems
   treats the cyclic two-fibre spaces used for the degree-`>1` controls here.
   Therefore the source does **not** settle whether a surviving cyclic row
   admits an etale map to `A2`.
2. **Exact decomposable volume.**  With `O(U)^*=C^*`, a nowhere-vanishing
   canonical form is unique up to scalar.  The second leg forces that
   generator to be

   ```text
   pi_U^*(du wedge dv)=d(pi_U^*u d(pi_U^*v)),
   ```

   hence zero in algebraic de Rham cohomology and decomposable by two global
   functions whose differential map has rank two everywhere.  This is
   strictly stronger than the abstract equality `K_U=0`.
3. **Cubic extension and boundary compatibility.**  The two functions must
   extend through the specified rank-three finite-flat normalization with
   different `R_X~2A+B`, reduced F5 infinity `H~A`, the full intersection
   length `H.R_X=8` at `p_0`, and the actual D9/ADE carrier marking.  This is the
   block-specific information that the external controls do not possess.

The clean finite successor is therefore not another attempt to infer the
base from `d_1`.  First apply (6.1)--(6.2) directly to the Miyanishi control
families, and in parallel apply the same hierarchy to each surviving internal
`P1`-ruling boundary row:

```text
(i)  compute K_U in Pic(U) from the adapted boundary lattice and discard
     K_U!=0;
(ii) in K_U=0 rows, compute the algebraic-de-Rham class of a canonical
     generator and discard a nonzero class;
(iii) impose the degree-three coordinate pair and its F5/different extension.
```

Step (i) is cheap and exact.  Step (ii) is a stronger necessary condition but
requires a correctly adapted ruling completion.  Step (iii), not the
first-leg degree, is the sharp proper-block discriminator.  At the external-
control level, the crisp next question is exactly whether a degree-`>1`
cyclic pseudo-cover target passing (i)--(ii) admits *any* etale morphism to
`A2`; at the internal level, the fixed cubic extension makes that reverse
arrow still more rigid.

## 7. Firewall

This packet proves no occurrence of a cyclic `A1`-fiber space inside the
normal quadratic incidence, no effective D9 marking, no compatibility with
F5, no finite cubic algebra, no polynomial Keller map, no counterexample, and
no JC2 result.  The external controls refute only the proposed implication

```text
dominant etale A2 first leg of degree >=2 + P1-base A1 ruling
    => contradiction.
```

They do not refute a contradiction obtained from the **two-sided** etale
sandwich plus the fixed cubic compactification.  Formal data, source theorem
statements, and actual maps remain distinct throughout.  In particular, the
internal Euler equality `r+c=10` in the complete-base branch would show that
all reduced ruling fibres are irreducible, but it does not by itself prove the
Q-homology, finite-fundamental-group, number-of-multiple-fibres, or other
hypotheses needed to label the internal surface pseudo-plane, cyclic, or
Platonic and invoke Miyanishi's classification theorems.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16077`.
- Body SHA-256:
  `0fdef779643fd98fe8774ea01138bc35023c79aa063b6749a14249ce9898139c`.
- Frozen basis: `00b2fb0c682c5ca2a056af588a29b2421c1b7ce4`.
