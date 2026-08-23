# Five cross-approach connections: landing, ceiling, and the residue-A signals

**Date:** 2026-08-23  
**Scope:** meta-analysis of the 46 approaches, using the current reductions and
the four completed probes `sol-symplectic.md`, `sol-jvdk.md`,
`sol-wtc1-round2.md`, and `sol-hc4probe.md`.  
**Status convention:** statements labelled **EXACT** are deductions from the
filed results or elementary calculations reproduced here. Everything proposed
as a missing theorem is labelled **CONJECTURE**.

## Executive ranking

| rank | connection | approaches joined | target | assessment |
|---:|---|---|---|---|
| 1 | Enrich the GGV packet flag by the cusp/approximate-root tower | GGV, JvdK, valuations, Eggers--Wall, symplectic residue | G2 | best direct landing experiment |
| 2 | Replace packet concentration by a normalized multi-Rees/b-divisor energy inequality | WTC/PCC, ZMT/Rees, proximity, log surfaces | G5 | best exotic global bridge |
| 3 | The residue-A genome is a rigid tetrahedral Belyi map; rung 36 may be its tangent equation | formal germ, dessins, splice, monodromy, D43 | char-0 obstruction/certificate | new exact classical identification |
| 4 | Put Jelonek and monodromy on the same canonically labelled dicritical flags | nonproperness, AM, coupled monodromy, WTC | realizability; not a ceiling alone | worthwhile only after rank 1 |
| 5 | JvdK and HC4 fail for the same ramification reason | automorphism descent, HC4, normal cones, approximate roots | method selection | explains two negative probes and names the next layer |

The main negative conclusion is also useful: the global action primitive cannot
itself be made into a landing functor. It is exact before a boundary model is
chosen, has zero residues on every resolution, and cannot distinguish one
local `Lambda=3` pole from two. The useful carrier is instead a **rank-two
boundary flag plus paired residual data**. The action/vertex-gap functional can
then be attached to that carrier as a consistency label.

---

## 1. G2: the cusp remainder is the missing label in the flag transport

### The seam

Three results now stop at adjacent, not identical, boundaries.

1. [TRANSPORT.md](../TRANSPORT.md) carries the selected pre-Laurent GGV
   polynomial pair, its rectangle, and its recoverable valuation ledger to an
   orbit-minimal Sigray frame. Its explicit remaining gap is **CONJECTURE T**:
   a GGV corner does not determine residual cancellation in the other
   coordinate, pole status, or the full decorated Eggers--Wall tree.
2. [sol-wtc1-round2.md](sol-wtc1-round2.md) proves that every *certified paired
   packet* determines an intrinsic rank-two flag valuation
   
   \[
   \widehat\nu_\lambda(H)=
   \bigl(\nu(H),\operatorname{ord}_\lambda\operatorname{res}_\nu(H)\bigr),
   \]
   
   hence a canonical Enriques point sequence and proximity ID over the
   original plane. Fan subdivision, Kummer presentation, root coordinate, and
   graph resolution do not change it.
3. [sol-jvdk.md](sol-jvdk.md) identifies the exact datum that the two leading
   powers erase. For a coprime `(m,n)` pair, the monomial-curve substitution
   has kernel
   
   \[
   B(U,V)=d^mU^n-c^nV^m.
   \]
   
   No target coordinate can have initial form in `(B)`. Thus an automorphism
   cannot use the first common-power cancellation, although the non-coordinate
   polynomial `B(P,Q)` can and does expose the next layer.

This suggests that the GGV packet is one label short. The paired values of
`P,Q` name the flag, but the **cusp remainder**

\[
 h_1=d^mP^n-c^nQ^m                                      \tag{1.1}
\]

records the residual cancellation needed to decide which tangent direction
continues, whether the flag is a pole flag, and which characteristic successor
appears. In the `(2,3)` genome this is the familiar approximate root
`g^2-const*f^3`; Sigray's `h_1,h_2,...` tower is already the downstream
language for precisely this information.

> **CONJECTURE 1 (enriched flag transport).** For a certified complete GGV
> chain, the ordered data
> \[
> \left(\widehat\nu_\lambda(P),\widehat\nu_\lambda(Q),
>       \widehat\nu_\lambda(h_1),\widehat\nu_\lambda(h_2),\ldots;
>       A(\nu),\mathcal I_P,\mathcal I_Q\right)             \tag{1.2}
> \]
> through the last eligible cut determine the corresponding fiber-tagged
> Eggers--Wall segment, its pole/finite status, pattern roots, and the Sigray
> decorations consumed by the book compiler. Here `A(nu)` is the log
> discrepancy and the two ideals are the transformed projective pencil ideals.

The conjecture is stronger than merely transporting Newton rays, but much
weaker than reconstructing the whole polynomial pair. It asks whether the
standard approximate-root data are a complete coordinate system on the finite
tree segment already traversed by the GGV chain.

### Where the symplectic result fits

The untwisted action primitive is not the functor. Its canonical residues are
zero for a hypothetical counterexample as well as for a tame automorphism.
What survives is the boundary-twisted reconstruction residue. At a flag where
the strip model is valid, it is exactly `R_{k,d_2}`. Thus it can be attached to
(1.2) as a natural **edge consistency functional**:

\[
 (\widehat\nu_\lambda;P,Q,h_j)\longmapsto
 \operatorname{Res}_{(E,\lambda)}(\text{twisted reconstruction form}).
                                                               \tag{1.3}
\]

This explains both facts in `sol-symplectic.md`: the action route is hollow
without a boundary choice, while the same no-log mechanism becomes nontrivial
after the flag and toric twist are supplied.

### Concrete first experiment

Use the component-sorted pre-Laurent `(8,28),(m,n)=(3,2)` record, **before**
the Laurent step changes the bracket to `x^2`.

1. Retain the exact cut-prefix field maps and every nonzero root orbit in one
   complete certified GGV chain.
2. Emit the canonical flag/Enriques ID from Theorem 2.1 of
   `sol-wtc1-round2.md`.
3. At every occurrence compute the two entries of the flag valuation on
   `f`, `g`, the normalized cusp remainder `h_1=g^2-lambda*f^3`, and the next
   approximate root if the chain calls for one; also compute the two weak
   pencil ideals and discrepancy.
4. Independently construct the Newton--Puiseux/Eggers--Wall segment of the
   corresponding fibers and compare, vertex by vertex, the characteristic
   exponent, tangent/root, pole tag, `nu`, `M`, and `kappa(1-pi)`.
5. Evaluate the boundary-twisted residue at every matched flag. It must agree
   with the GGV reconstruction obstruction and be invariant under the inverse
   signed-axis transport.

The experiment fails closed. Two realizations with identical data (1.2) but
different next Eggers--Wall vertices refute the proposed sufficiency and name
the missing label. A full match gives the first actual client of the
corner-to-tree functor and a typed schema for G2. Residue A is only a
frame-schema control here; `TRANSPORT.md` proves that it is not the same
equivalence class as `(8,28)`.

---

## 2. G5: multi-Rees energy, not packetwise concentration

### The seam

The second WTC round changes the natural G5 object. A packet does not
unconditionally land as one point-basis atom. It lands as a canonical flag and
two contact flows

\[
 A=\sum_iR_{p_i},\qquad C=\sum_jS_{q_j}.                 \tag{2.1}
\]

The Laurent constant-Jacobian example

\[
 I_f=(r^2+x,x^2),\qquad I_g=(r^3+\tfrac32xr,x^3)        \tag{2.2}
\]

has the correct boundary powers and denominator capacities but contact vectors
`(1,1)` and `(2,1)`. It proves that the local Jacobian, one common-power face,
and denominator orders do not imply KPC. This is not an annoying exception:
it identifies the correct global object.

The integral closures of the two projective pencil ideals have canonical Rees
valuations and point-basis clusters. On a common resolution their divisor
classes are

\[
 C_f=B\alpha H-\sum_pR_pE_p^*,\qquad
 C_g=B\beta H-\sum_pS_pE_p^*,                            \tag{2.3}
\]

with

\[
 C_f^2=C_g^2=0,\qquad
 C_fC_g=td,qquad
 \sum_pR_pS_p=B^2\alpha\beta-td.                         \tag{2.4}
\]

PCC asks for the common-cluster energy

\[
 \sum_p h_p^2\ge B^2-1,
 \qquad
 h_p=\min\!\left(\left\lfloor R_p/\alpha\right\rfloor,
                  \left\lfloor S_p/\beta\right\rfloor\right). \tag{2.5}
\]

The packet forest supplies linear contact conservation, whereas (2.5) is
quadratic and contact splitting has the wrong sign. A normalized **multi-Rees
algebra** retains exactly what the scalar packet forest forgets: all Rees
valuations, both multiplicity vectors, proximity, and their common exceptional
support.

> **CONJECTURE 2 (global common-part inequality).** For the two complete
> projective pencil ideals of a polynomial Keller pair, the normalized
> multi-Rees b-divisor has a canonical common positive part `H_cap` satisfying
> \[
> -H_{\cap}^2=\sum_ph_p^2\ge B^2-1.                       \tag{2.6}
> \]
> Equivalently, the total splitting and normalized-divergence defect is at
> most one. The inequality is allowed to use polynomial origin, the divisor
> of `dx wedge dy`, and the full boundary; it is not a local consequence of a
> packet face.

If true, (2.6) bypasses KPC packet by packet. It consumes the proved
vector-valued WTC output and gives PCC directly, hence

\[
 td\le\alpha\beta.                                       \tag{2.7}
\]

This is not yet an absolute numerical bound because `(alpha,beta)` remain
unbounded. It is nevertheless the only current G5 proposal that converts the
existing exact intersection identities into a ceiling on each type; it can
then be paired with a separate type bound or a finite type classification.

### Why this is the best untried exotic

Among the exotic rows, ZMT/Rees is best aligned with the residual:

- WTC now outputs valuations, integral closures, point IDs, and contact
  vectors--the native input of Rees and b-divisor theory.
- G5 needs a quadratic intersection inequality, not another linear residue or
  sheet count.
- Zariski Main identifies nonfiniteness with added boundary; the multi-Rees
  normalization records that boundary instead of merely restating that
  finiteness is missing.

By comparison, ordinary `K_2` reciprocity gives linear/product conservation;
motivic `A^1` degree and primitive monodromy count sheets but do not penalize
their separation; p-adic transfer first needs the missing uniform
degree/support bound; and completeness of the commuting frame is essentially
properness/LND again. An infinitesimal two-dimensional tame symbol remains a
plausible way to certify **coverage of flags**, but it has no visible route to
the square in (2.6).

### Concrete first experiment

Run a two-control intersection computation, without assuming KPC.

1. For Proposition 5.1 of `sol-wtc1-round2.md`, normalize the bi-Rees algebra
   of the two ideals in (2.2), emit its Rees valuations and proximity matrix,
   and compute the candidate common-part square. Any proposed inequality must
   visibly fail here or acquire a correction term detecting its Laurent/non-
   polynomial origin.
2. For one smallest *complete* polynomial-origin boundary book, build the
   integral closures of `(F,Z^d)` and `(G,Z^e)` chartwise and glue their Rees
   valuations by the canonical point IDs. Compute the full vectors `R,S`, the
   negative-definite proximity form, discrepancy coefficients, and the
   Zariski decomposition of the greatest common sub-b-divisor permitted by
   `R/alpha` and `S/beta`.
3. Test whether
   
   \[
   B^2+H_{\cap}^2
   \]
   
   is exactly a sum of nonnegative local splitting/divergence defects plus a
   boundary canonical-divisor term. The target is an identity whose Keller
   term is at most one and whose Laurent control violates that bound.

The first useful output need not prove (2.6). An exact defect decomposition
would replace the opaque PFE target by named local terms and say whether log
surface, Rees-integrality, or polynomial-origin data can control each one.

---

## 3. The `2+sqrt(3)` genome is a tetrahedral dessin; rung 36 may be its tangent obstruction

### Exact classical identification

The residue-A `h_2` collapse is

\[
 W(t)=t(t-b)^3-(t-a_1)^2(t-a_2)^2,                       \tag{3.1}
\]

with

\[
 a_1+a_2=\sigma,\qquad a_1a_2=\sigma^2/6,
 \qquad b=2\sigma/3.                                    \tag{3.2}
\]

Put `u=t/sigma`. Then (3.1) is the numerator of `beta-1` for

\[
 \beta(u)=
 \frac{u(u-2/3)^3}{(u^2-u+1/6)^2}.                      \tag{3.3}
\]

Direct expansion gives

\[
 u(u-2/3)^3-(u^2-u+1/6)^2=\frac{4u-3}{108},             \tag{3.4}
\]

and differentiation gives

\[
 \beta'(u)=-\frac1{9}
 \frac{(u-2/3)^2}{(u^2-u+1/6)^3}.                       \tag{3.5}
\]

Therefore **EXACTLY**:

- over `0`, the ramification partition is `(3,1)`;
- over infinity, it is `(2,2)`;
- over `1`, the finite point `u=3/4` is simple and `u=infinity` is triple,
  so the partition is `(3,1)`.

Thus (3.3) is a degree-four Belyi map with passport

\[
 ((3,1),(2,2),(3,1)).                                   \tag{3.6}
\]

Up to simultaneous conjugacy, there is one transitive branch-cycle triple of
these ordered types; it generates `A_4` in its four-point action. This is the
tetrahedral dessin. The two double poles are

\[
 u_{1,2}=\frac12\left(1\mathbin\pm\frac1{\sqrt3}\right),
 \qquad
 \frac{u_1}{u_2}=2+\sqrt3.                              \tag{3.7}
\]

Hence the quadratic unit is not an accidental solution of one ODE. It is the
splitting-field signal of the `(2,2)` fiber of a `Q`-rational rigid Belyi
passport. Splice topology sees the integer ramification data; the collapse
identity fixes the labelled double-pole positions and produces `Q(sqrt(3))`.
This also explains why the splice and
single-cover passport tests pass: the local genome is not merely topologically
admissible; it already carries a classical algebraic realization.

### The rung-36 connection

The banked modular rung-36 row has shape

\[
 c_1(tf1_{48}+tf2_{48})+
 c_2\bigl(2(tg1_{48}+tg2_{48})+tg01_{48}+tg02_{48}\bigr)=0. \tag{3.8}
\]

In both primes, the recorded coefficients satisfy `c_1=-3c_2` exactly:

\[
 48635+3(54013)=0\pmod {105337},\qquad
 50809+3(18288)=0\pmod {105673}.                         \tag{3.9}
\]

Thus the common rational candidate is

\[
 3\operatorname{Tr}(tf_{48})-
 2\operatorname{Tr}(tg_{48})-
 \operatorname{Tr}(tg0_{48})=0.                         \tag{3.10}
\]

The pair sums are exactly the Galois traces under the pole swap, and the
coefficients `3,2,1` reproduce the ramification multiplicities in (3.6).
Moreover the exact level-48 condition `C16.10` already has linear part
`3 Tr(tf)-2 Tr(tg)-Tr(tg0)` before its nonlinear terms are eliminated.

> **CONJECTURE 3 (Hurwitz tangent interpretation).** The rung-36
> compatibility row is the unique non-gauge first-order obstruction to
> deforming the factored Belyi map (3.3) while preserving its passport and the
> two-coordinate cusp normalization. Equivalently, the D43 left-kernel row is
> a Hurwitz-space tangent equation, not an accidental modular syzygy.

This would turn two empirical char-0 signals into one classical invariant:
`sqrt(3)` is the rigid dessin modulus, while `3:2:1` is the linearized
ramification divisor.

### Concrete first experiment

Construct the deformation complex of (3.3) over `Q`.

1. Perturb the four factored fibers in (3.3) by dual-number coefficients,
   preserving the multiplicity partitions `(3,1)`, `(2,2)`, `(3,1)`.
2. Quotient by infinitesimal source and target `PGL_2` changes.
3. Map the six level-48 tail variables to the induced perturbations at the two
   conjugate double poles and the two `g0` streams using the exact
   `directionb_window` source formulas.
4. Eliminate the gauge variables. The predicted remaining row is (3.10), up
   to a nonzero scalar.
5. Replay that row directly over `Q(sqrt(3))` against the char-0 rung
   constructor and then against both primes.

A match gives a small, human-readable char-0 certificate for the rung-36 row
and a principled way to search later rungs by representation of the dessin
monodromy. A mismatch cleanly separates the Belyi coincidence from the D43
operator and prevents overinterpreting the `2:1` pattern.

---

## 4. Jelonek plus coupled monodromy becomes meaningful only on labelled flags

### What the two lanes lack separately

The nonproperness and monodromy lanes currently forget complementary data.

- Jelonek supplies the right global objects: every irreducible component of
  `A(F)` is a rational curve with one place at infinity. But the books have not
  constructed those components or determined which source flags map to the
  same component.
- The residue-A monodromy sweep labels one degree-six cover abstractly. All
  169 passports admit transitive factorizations. It forgets the second
  coordinate, the common source-sheet labels, and the asymptotic component to
  which each inertia orbit belongs.
- WTC round 2 supplies exactly the missing identity layer: canonical flags,
  Enriques point IDs, and contact chains. Once a flag is proved dicritical,
  its residual map to the target boundary can group occurrences by an actual
  component of `A(F)` rather than by a root token.

> **CONJECTURE 4 (dicritical flag coupling).** For a complete resolved Keller
> boundary, the canonical packet flags together with the residual maps of
> `P,Q` determine (i) the normalization and one-place semigroup of each
> component of `A(F)`, and (ii) a common sheet labelling for the two coordinate
> branch-cycle systems. The Abhyankar--Moh constraints on the component and
> the coupled Nielsen class then form one realizability obstruction.

This is a plausible **realizability** bridge, but not a G5 ceiling by itself.
Primitive groups `A_d,S_d` exist in arbitrarily large degree, so primitivity
cannot bound `td` without a new restriction on allowed inertia. Jelonek's
degree ceiling scales with `deg f,deg g` and has enormous slack on residue A.
Neither theorem removes large `d`. Their role is to test a boundary
configuration after the rank-1 connection has supplied global labels.

### Concrete first experiment

Use residue A as the positive-stress client and the single local
`Lambda=3` datum from `sol-symplectic.md` as the negative control.

1. Complete the smallest compatible `B/x` tails far enough to identify every
   dicritical divisor and compute the residual maps `E -> P^1 x P^1`.
2. Group flags by equality of the normalized image component in `A(F)`.
   Compute for each component its parametrization degree, unique place
   semigroup, and the degrees of the maps from the contributing dicriticals.
3. Put the `f`- and `g`-fiber inertia permutations on the **same six sheet
   labels**, with flag IDs attached, and impose both coordinate products, the
   Jacobian contact pairing, and the tetrahedral auxiliary passport (3.6).
4. Apply the one-place semigroup restrictions to the target components, not
   to the multiplace Keller fibers.
5. Require the implementation to reject the one-pole `td=3` local control.
   Its action primitive and all local residues pass, while Orevkov excludes a
   global map; failure to reject it shows that the coupling still lacks a
   genuinely global condition.

This is substantially sharper than another primitive-group database sweep.
Its decisive output is either an impossible coupled Nielsen class/semigroup or
an explicit abstract global model showing that monodromy and Jelonek still do
not reach algebraization.

---

## 5. JvdK and HC4 share a ramification obstruction: first variations lose the reduced equation

### The common mechanism

The JvdK and HC4 probes look unrelated--one concerns plane automorphisms, the
other a four-variable Hessian equation--but they fail at the same geometric
kind of locus.

For the rectangular cusp pair,

\[
 (P_+,Q_+)=(cH^m,dH^n),
\]

the substitution map from target polynomials to the monomial curve has kernel
`(d^mU^n-c^nV^m)`. The only top cancellation lies in that kernel. The
coordinate-cusp theorem says the automorphism orbit is transverse to the
wrong directions: no coordinate initial form can enter the kernel. Thus the
Jung action cannot access the reduced cusp equation at all.

For the cotangent HC4 embedding,

\[
 h(x,y)=y_1P(x)+y_2Q(x),\qquad
 \det\operatorname{Hess}h=(\det DF)^2,                  \tag{5.1}
\]

the map to the Hessian equation is quadratically ramified along the plane
determinant locus. At the first two homogeneous layers,

\[
 C_{12}=a_6^2,\qquad C_{11}=2a_6a_5.                   \tag{5.2}
\]

After passing to the reduced top locus `a_6=0`, the entire first variation
vanishes and does not constrain `a_5`. The unique ambient GL4 module selects
the factored tangent direction even though the restricted plane coefficient
space contains a second copy of the same isotype.

In both cases the proposed machinery probes a **ramified power image**:

- JvdK coordinates cannot use the cusp-kernel direction;
- the first HC4 variation is divisible by the equation defining the reduced
  plane locus.

This is also why the non-coordinate approximate root (1.1) is useful: it
leaves the automorphism orbit and measures the normal direction that JvdK is
forbidden to use. Likewise, any remaining HC4 leverage must live in the
normal cone/second fundamental form, not in the first post-top module.

> **CONJECTURE 5 (normal-cone discriminator).** After saturating the HC4
> cotangent restriction by the reduced plane top ideal, either a later layer
> selects the *second* copy of the plane isotype found in `sol-hc4probe.md`, or
> every ambient HC4 layer factors through the ordinary determinant descent.
> The first alternative is the earliest possible genuinely new JC2 equation;
> the second would explain the whole HC4 discount structurally.

### Concrete first experiment

Do not attack all quintic HC4. Compute the second normal layer at the generic
binary-quartic top point.

1. Explicitly construct a basis for the two copies of
   `S_(13,2) X tensor S_(2,2) Y` in the sector coefficient space. Mark the
   known line `a_6a_5` and the complementary covariant.
2. Form `C_10,C_9` universally on the `y`-linear sector, saturate by the
   coefficient ideal `(a_6)`, and take their initial forms in the normal-cone
   filtration of the top locus.
3. Project those initial forms to the complementary covariant after quotienting
   all equations generated by the ordinary homogeneous descent of `det DF=1`.
4. A nonzero projection is the first HC4 equation not already in the plane
   determinant tower and deserves a new probe. Zero through this second normal
   layer is a sharp stop rule for HC4-as-JC2-leverage.

As a cross-check, perform the analogous normal-cone calculation for the cusp
pair using `h_1=d^mP^n-c^nQ^m`. The first surviving class should be an
approximate-root/vertex-gap datum, never a coordinate descent. Agreement would
make the shared obstruction precise rather than metaphorical.

---

## Strategic verdict

The five connections separate the two global gaps cleanly.

- **G2 is a data-transport problem.** The promising carrier is the canonical
  rank-two flag enriched by the cusp/approximate-root tower and pencil ideals.
  The symplectic action primitive is too universal; its twisted residue is a
  useful flag label after landing, not the landing mechanism.
- **G5 is an intersection-energy problem.** Primitive monodromy, Jelonek,
  ordinary reciprocity, and motivic degree are linear/counting invariants. The
  normalized multi-Rees b-divisor is the one exotic object already shaped like
  the required quadratic PFE inequality.
- **The char-0 residue-A signals have a classical source.** The
  `2+sqrt(3)` pair is the double-pole field of a rigid tetrahedral Belyi map,
  and the rung-36 `3:2:1` trace row is a plausible infinitesimal form of its
  passport rigidity. This is the cheapest new exact experiment in the list.
- **Two attractive lanes are first-order blind for the same reason.** JvdK and
  the first HC4 layer meet ramified power loci. Their next honest tests must use
  normal data--approximate roots for the former, the second normal cone for the
  latter.

If only one experiment is run for each global gap, run rank 1 on the
pre-Laurent `(8,28)` chain and rank 2 on one complete polynomial-origin
boundary cluster with the Laurent separation example as a compulsory negative
control. If one cheap signal experiment is run first, run rank 3: it can turn
the most conspicuous modular/radical coincidences into an exact classical
equation without another large coefficient solve.
