# Dual-pencil infinity-defect definition gate

**Date:** 2026-08-24  
**Root:** P from `xmodel/ideation-20260824T0719Z-synthesis.md`  
**Scope:** definition/source gate only; no GRR, client book, ledger edit, or
compute child  
**Verdict:** **`PRIOR-ART / JUMP-ONLY / TYPE-FAIL`**

The intrinsic infinity defect of each pencil member is well defined and
resolution-independent.  It is the classical Suzuki total Euler/vanishing-
cycle defect.  It does **not** define the proposed finite effective divisor on
the dual projective line.  In fact, if a nonautomorphic Keller map exists,
this defect is a positive integer for **every** pencil direction, so its
universal incidence has horizontal support dominating the dual line.  A
finite residual object can record only jumps from the generic positive
baseline; those jumps have no general effectivity or degree-zero theorem.

This is a complete first-gate stop.  The GRR sequel is not licensed.

## 1. Exact type of the universal pencil

Let

\[
 F=(P,Q):\mathbb A^2_{\mathbb C}\longrightarrow V=\mathbb A^2_{\mathbb C},
 \qquad J(P,Q)=1,
\]

and let \(B=\mathbb P(V^*)\), the dual target line.  If
\(S=\mathcal O_B(-1)\subset V^*\otimes\mathcal O_B\) is the tautological
line, evaluation gives the correctly typed universal map

\[
 \mathcal H:\mathbb A^2\times B\longrightarrow
 \operatorname{Tot}(S^*)=\operatorname{Tot}(\mathcal O_B(1)),
 \qquad (z,\ell)\longmapsto (\ell,\operatorname{ev}_{F(z)}|_\ell).
\]

Choosing a generator \(aX+bY\) of \(\ell\) identifies its fiber coordinate
with

\[
 H_\ell=aP+bQ.
\]

Changing the generator rescales both \(H_\ell\) and its target values, so the
fiber topology and all definitions below descend to \(B\).  This line-bundle
target is necessary: the atypical value \(c\) is not a globally defined
scalar over projective directions.

For every \(\ell=[a:b]\),

\[
 dH_\ell=(a,b),DF,
\]

which is nowhere zero because \(DF\) is invertible.  Thus every pencil member
is a polynomial submersion and all its bifurcations are at infinity.

On the affine chart \(H_s=P+sQ\), the family is the polynomial submersion

\[
 \Psi:\mathbb A^3\to\mathbb A^2,
 \qquad (x,y,s)\mapsto (s,P(x,y)+sQ(x,y)).
\]

The other chart is identical with \(P,Q\) interchanged.  General polynomial-
map bifurcation theory therefore gives a constructible/algebraic bifurcation
locus in the two-dimensional target.  It should be viewed inside
\(\operatorname{Tot}(\mathcal O_B(1))\), not pushed prematurely to a divisor
on \(B\).

## 2. The intrinsic per-member defect

Fix \(\ell\), write \(h=H_\ell\), and let \(G_h\) be a generic fiber.  The
generic fiber is connected.  One quick proof is the primitive factorization:
if \(h=\varphi(g)\) with \(\deg\varphi>1\), a root \(u\) of
\(\varphi'\) has a nonempty fiber \(g^{-1}(u)\), and \(dh=0\) on that fiber,
contrary to submersivity.  Equivalently, Suzuki's primitive factorization
forces \(\deg\varphi=1\).

For each atypical value \(c\), define the local infinity defect

\[
 \epsilon_c(h)=\chi(h^{-1}(c))-\chi(G_h).
\]

For a primitive plane polynomial with no affine critical points, Suzuki's
formula and the Hà--Lê Euler criterion give

\[
 c\in B_\infty(h)\iff \epsilon_c(h)>0,
 \qquad
 \delta(h):=\sum_{c\in B_\infty(h)}\epsilon_c(h)
            =1-\chi(G_h).
\]

If the smooth connected affine curve \(G_h\) has compactification genus
\(g_h\) and \(r_h\ge1\) punctures, then

\[
 \boxed{\delta(h)=b_1(G_h)=2g_h+r_h-1\ge0.}
\]

This is the total number of vanishing cycles at infinity (usually denoted
the total \(\lambda\) when using the isolated-singularity-at-infinity
language).  It is the cleanest possible coefficient candidate: integral,
nonnegative, target-scaling invariant, and defined without choosing a
compactification.

Suzuki already proves the precise formula in his Theorem 2: for a primitive
polynomial of generic type \((g,r)\), the sum of the nonnegative critical-
fiber defects is \(2g+r-1\).  His definitions give each summand as the Euler
jump \(d_i+a_i\).  In the present submersion case all such defects occur at
infinity.

## 3. The coordinate endpoint is exact

The proposed endpoint is valid, and actually sharper than needed:

\[
 \delta(h)=0
 \iff g_h=0,\ r_h=1
 \iff G_h\simeq\mathbb A^1
 \implies h\text{ is a polynomial coordinate}.
\]

For the last implication, a generic fiber is a nonsingular embedded affine
line.  Suzuki's Theorem 5 (equivalently Abhyankar--Moh--Suzuki) sends it to a
coordinate axis; since its irreducible defining equation is \(h-c\), the
polynomial \(h\) itself is a coordinate.

If one pencil member \(H_\ell\) is a coordinate, choose an independent target
linear combination \(K_\ell\) so that
\(J(H_\ell,K_\ell)=1\).  In source coordinates with \(H_\ell=x\), the
Jacobian equation says \(\partial K_\ell/\partial y=1\), hence

\[
 K_\ell=y+r(x).
\]

Thus \((H_\ell,K_\ell)\), and therefore \(F\), is an automorphism.

Consequently,

\[
 \boxed{
 F\text{ nonautomorphic Keller}
 \quad\Longrightarrow\quad
 \delta(H_\ell)\ge1\text{ for every }\ell\in B.}
\]

This is the decisive type check.  Proving even *generic* vanishing of
\(\delta(H_\ell)\) for Keller pairs is already equivalent to proving JC2: a
single direction in the generic open would finish the map.

## 4. Why the proposed divisor does not exist

Define the universal weighted bifurcation incidence locally by

\[
 \mathscr Z_\infty
 =\sum_{(\ell,c)}\epsilon_c(H_\ell)[(\ell,c)]
 \subset\operatorname{Tot}(\mathcal O_B(1)).
\]

This notation is intrinsic at the level of the constructible vanishing-cycle
function.  It is not generally a zero-cycle: if
\(\delta(H_\ell)=\delta_{\rm gen}>0\) generically, its closure has horizontal
components dominating \(B\).  Fiberwise pushforward gives the constructible
integer function

\[
 \ell\longmapsto\delta(H_\ell),
\]

not a Weil divisor on \(B\).  For a hypothetical Keller counterexample the
boxed implication above forces exactly this positive horizontal baseline.

Algebraic stratification makes \(\delta(H_\ell)\) constant on a nonempty
Zariski-open subset of \(B\); because \(B\) is a curve, only finitely many
directions are exceptional.  One may therefore form the finite formal jump
cycle

\[
 J_F=\sum_{\ell\in B}
       \bigl(\delta(H_\ell)-\delta_{\rm gen}\bigr)[\ell].
\]

This is **JUMP-ONLY**.  The generic horizontal contribution has been
subtracted by definition, not killed by \(J=1\).  There is nevertheless a
useful one-sided statement.  Put

\[
 D=\max\{\deg P,\deg Q\},\qquad
 E_{\deg}=\{\ell\in B:\deg H_\ell<D\}.
\]

Because the degree-\(D\) part of \(H_\ell\) depends linearly on \(\ell\),
\(\#E_{\deg}\le1\).  If \(\ell_0\notin E_{\deg}\), a local parameter at
\(\ell_0\) gives a constant-degree deformation of reduced plane polynomials.
Siersma--Tibăr Proposition 5.1 gives, for nearby general \(\ell\),

\[
 \mu(H_\ell)+\lambda(H_\ell)
 \ge \mu(H_{\ell_0})+\lambda(H_{\ell_0}).
\]

Every pencil member is a submersion, so \(\mu=0\), while here
\(\delta=\lambda\).  Hence

\[
 \delta(H_{\ell_0})-\delta_{\rm gen}\le0.
\]

Thus \(J_F\) is anti-effective away from the possible degree-drop direction.
The coefficient at \(E_{\deg}\), if present, is not controlled by that
constant-degree theorem.  This does not rescue the proposed divisor: the raw
defect still has the positive generic horizontal support proved above in the
counterexample regime, while changing sign or deleting \(E_{\deg}\) discards
the generic baseline and a potentially essential compactification correction.
No degree-zero formula for the full \(J_F\) is proved.  Atypical values may
also collide or escape to the infinity section, and any localization formula
must retain those horizontal/infinity terms.

Taking only positive parts would manufacture an effective divisor but destroy
additivity and any natural GRR class.  Conversely, an effective divisor on
\(\mathbb P^1\) of degree zero is automatically zero; deriving that degree
without the discarded horizontal term would already contain the missing
theorem.

Hence the card's proposed

```text
coefficient at ell = total infinity defect of H_ell
```

has infinite support in the counterexample regime and is **TYPE-FAIL** as a
divisor on the dual line.

### 4.1 Relation to the nonproperness curve: verified scope

There is a compatible geometric picture, but it must not be used more
strongly than the sources permit.  Jelonek's nonproperness theorem and Nguyen
Van Chau's nonsingular-plane specialization imply that a nonproper étale
polynomial map has a nonempty algebraic curve \(A(F)\subset\mathbb A^2\) of
nonproper values.  An elementary generic-line argument then says that a
generic *line* (direction and translate together) meets the projective closure
of \(A(F)\) transversely.  For a fixed generic direction, however, the
projection \(A(F)\to\mathbb A^1\) generally has finitely many critical
values: the corresponding tangent **translated lines** sweep a horizontal
curve in the universal \((\ell,c)\)-space as \(\ell\) varies.  They are not a
finite set of directions.  Only degeneracies of this generic projection
picture--degree loss at infinity, collision of critical values, non-Morse
ramification, or singular-point incidence--can be confined to a finite set
of directions after an appropriate stratification.

This verifies the *horizontal-versus-jumping* geometry: generic intersections
and generic projection-critical values of \(A(F)\) persist over an open set
of directions, whereas degenerations of their pattern are jump events.  It
also corrects a tempting but false shorthand: “directions tangent to
\(A(F)\)” are not generally finite; tangent *lines* form the dual curve.  The
picture does **not** by itself identify
the intersection number \(L\cdot A(F)\) with
\(\delta(H_\ell)\), nor identify every missing sheet with one vanishing
cycle.  No such equality was found in the audited primary sources, and it is
not assumed here.  The exact positive-baseline conclusion instead follows
from the Suzuki coordinate endpoint in §3.  Even if a dual discriminant of
\(A(F)\) is used, it records only special-direction changes and forgets the
generic nonproperness intersections; it remains a `JUMP-ONLY` object.

## 5. Resolution and blowup audit

The following distinction is essential.

- The set \(B_\infty(h)\), every Euler jump \(\epsilon_c(h)\), and their total
  \(\delta(h)\) are topological invariants of the polynomial map.  They are
  independent of a projective compactification and of further boundary
  blowups.
- On a chosen good resolution, the same numbers may be distributed among
  critical boundary components and local vanishing-cycle groups.  Extra
  blowups change the dual tree and may split or insert local terms; only the
  correctly aggregated vanishing-cycle/Euler defect is invariant.

Fourrier makes this precise from a resolved meromorphic extension: the dual
resolution tree itself is only defined up to blowups and contractions, while
her theorem on p. 660 identifies regularity at infinity with actual
topological triviality outside a large ball, and Corollary 2 on p. 661
identifies the minimal global bifurcation set.  This validates the aggregate
defect, not a coefficientwise divisor extracted from one common resolution.

A “common graph resolution of the universal pencil” therefore cannot repair
the base-support problem.  It can represent \(\mathscr Z_\infty\), including
its horizontal components, but deleting those components to obtain a base
divisor is an additional noncanonical operation.

## 6. Controls

| control | exact result | interpretation |
|---|---|---|
| identity \((x,y)\) | every \(ax+by\) is a coordinate; \(\delta=0\) | pass |
| triangular \((x,y+x^n)\) | every target-linear projection is a coordinate; \(\delta=0\) | pass independently of presentation degree |
| two-shear tame product | target-linear composition of an automorphism; \(\delta=0\) | pass |
| Hénon tower | target-linear composition of an automorphism; \(\delta=0\) | pass despite arbitrarily large raw boundary passports |
| Broughton \(h=x+x^2y\), single polynomial only | no affine critical point; generic fiber \(\simeq\mathbb C^*\); \(B_\infty=\{0\}\), \(\epsilon_0=\delta=1\) | detects the missing infinity topology; it is **not** a full Keller-pair control |

For Broughton the calculation is direct.  If \(t\ne0\), then \(x\ne0\) and
\(y=(t-x)/x^2\), so the fiber is \(\mathbb C^*\).  At \(t=0\), the fiber is
the disjoint union \(\{x=0\}\sqcup\{xy=-1\}\), and its Euler characteristic
jumps from \(0\) to \(1\).  This is exactly the classical infinity defect.

The mandatory separation matters: every available *full* Keller control is
an automorphism and hence has zero baseline.  Broughton shows that
critical-point-freeness alone permits a positive baseline, but does not
supply a hypothetical nonautomorphic Keller pair on which a new sign could
be tested.

## 7. Different/canonical and no-log comparisons

The standard finite-map identity

\[
 K_X=\pi^*K_{\mathbb A^2}+R_\pi
\]

and the tame height-one different coefficient \(e_E-1\) concern ramification
of a finite normalization.  They neither remove the horizontal universal
bifurcation cycle nor turn the constructible function \(\delta(H_\ell)\) into
a torsion sheaf on \(B\).  A divisor of a rational differential represents a
canonical class; it is not a principal divisor of a rational function.  Thus
the standard different supplies no missing degree-zero relation here.

Likewise,

\[
 dP\wedge dQ=dx\wedge dy
\]

and the exact no-log/action identities are valid for every Keller map.  The
repository's boundary probe already shows that their stable raw outputs are
only determinant volume and zero residues, while boundary Smith splits and
primitive pole orders change under blowups/presentation.  The Euler defect
above is genuinely invariant but is not forced to vanish by those identities.
Treating their cancellation as \(\deg J_F=0\) would be `COSTUME`: it simply
omits the positive generic/horizontal contribution.

## 8. Gate decision

The exact outcome is the allowed combined verdict:

```text
PRIOR-ART:  the intrinsic coefficients and zero-defect coordinate endpoint
            are classical Suzuki / Abhyankar--Moh--Suzuki theory.

JUMP-ONLY:  over the dual line, the total defect is a constructible function
            with a generic baseline; only finitely many deviations remain.

TYPE-FAIL:  in the hypothetical counterexample regime the baseline is >= 1
            in every direction, so the raw defect has horizontal support and
            is not an effective divisor on the dual line.  The residual jump
            cycle is anti-effective away from at most one degree-drop
            direction, but has no full degree-zero formula.
```

No `GENERIC-ZERO` result is obtained; that statement is already equivalent
to JC2 in this setting.  No GRR sequel, second compactification, client book,
AWS job, or ledger promotion is warranted.

## Primary technical sources

1. Masakazu Suzuki, *Propriétés topologiques des polynômes de deux variables
   complexes, et automorphismes algébriques de l'espace C²*, J. Math. Soc.
   Japan 26 (1974), 241--257.  Primitive factorization: p. 242; total defect
   formula, Theorem 2: pp. 246--247; embedded-line coordinate theorem,
   Theorem 5: p. 252.  Official
   [J-STAGE PDF](https://www.jstage.jst.go.jp/article/jmath1948/26/2/26_2_241/_pdf/-char/en).
2. Laurence Fourrier, *Topologie d'un polynôme de deux variables complexes au
   voisinage de l'infini*, Ann. Inst. Fourier 46 (1996), 645--687.  Resolution
   equivalence: pp. 647--648; fibration-at-infinity theorem: p. 660; minimal
   bifurcation set, Corollary 2: p. 661.
   [NUMDAM PDF](https://www.numdam.org/item/10.5802/aif.1527.pdf).
3. Cezar Joiţa and Mihai Tibăr, *Bifurcation set of multi-parameter families
   of complex curves*, 2015, especially the introduction's algebraicity of
   polynomial-map bifurcation loci and the Suzuki--Hà--Lê Euler criterion.
   [arXiv:1512.07499](https://arxiv.org/abs/1512.07499).
4. Dirk Siersma and Mihai Tibăr, *Deformations of polynomials, boundary
   singularities and monodromy*, Moscow Math. J. 3 (2003), no. 2, 661--679.
   Constant-degree FISI semicontinuity: Proposition 5.1; variation of
   \(\lambda\): discussion after Corollary 5.2 and Examples 8.3--8.4
   (Example 8.4 is non-FISI).
   [arXiv:math/0207076](https://arxiv.org/abs/math/0207076).
5. Zbigniew Jelonek and Mihai Tibăr, *Bifurcation locus and branches at
   infinity of a polynomial \(f:\mathbb C^2\to\mathbb C\)*, Math. Ann. 2015,
   including the intrinsic definition of \(B_\infty\) and the Broughton
   example in Remark 1.3.
   [arXiv:1401.6544](https://arxiv.org/abs/1401.6544).
6. S. A. Broughton, *Milnor numbers and the topology of polynomial
   hypersurfaces*, Invent. Math. 92 (1988), 217--241,
   [publisher record](https://link.springer.com/article/10.1007/BF01404452).
7. S. S. Abhyankar and T. T. Moh, *Embeddings of the line in the plane*, J.
   reine angew. Math. 276 (1975), 148--166,
   [DOI record](https://doi.org/10.1515/crll.1975.276.148).
8. Nguyen Van Chau, *Non-proper value set and the Jacobian condition*, 2003:
   a nonempty nonproper-value set of a nonsingular polynomial map
   \(\mathbb C^2\to\mathbb C^2\) is a curve (with one point at infinity).
   [arXiv:math/0305088](https://arxiv.org/abs/math/0305088).
9. Zbigniew Jelonek, *The set of points at which a polynomial map is not
   proper*, Ann. Polon. Math. 58 (1993), 259--266: for a dominant generically
   finite map the nonproperness set is empty or a hypersurface.
   [DOI record](https://doi.org/10.4064/ap-58-3-259-266).
