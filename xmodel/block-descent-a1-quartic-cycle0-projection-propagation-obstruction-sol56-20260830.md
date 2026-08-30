# Rank-four zero-cusp cycle: based-braid escape and propagation firewall

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`rank4_cycle_m0` lane)  
Frozen basis: `6ed236c23e2fce71d1a279ca541239a405a757bf`  
Lifecycle: **FINAL+VERIFIED SHARP THREAT MAP / BRAID CONTROL PASSES / POLYNOMIAL HORN OPEN**

## 0. Verdict

The current rank-four ledger does **not** force the zero-cusp minimal cycle
to preserve a perfect matching.  The tempting propagation proof fails at a
precise place: connected monodromy of a polynomial normalization controls
the permutation of projection punctures, but based Zariski--van Kampen
meridians are acted on by full Hurwitz braid tails.  It does not identify
their `S4` transposition labels.

The exact group dichotomy is clean.  At the unique `(2,2)` conductor value,
write the two local inertias as

```text
tau=(12),                 upsilon=(34),
M=12|34.                                                   (0.1)
```

Every transporter carrying `tau` to `upsilon` preserves `M`; node-only
transport therefore lies in the order-eight stabilizer `D4=Stab(M)`.  But
`D4` is maximal in `S4`.  One based braid tail outside `D4`, equivalently one
cross-meridian label among

```text
(13), (14), (23), (24),                                  (0.2)
```

upgrades the image to full `S4`.

An explicit four-strand quasipositive braid packet realizes exactly this
escape.  It has:

```text
normalization permutation graph = a tree;
normalization Euler number       = 1;
one boundary cycle               = one place at infinity;
one positive node packet         = two disjoint transpositions;
three simple branch packets      = equal local transpositions;
based quartic image              = full S4.               (0.3)
```

There is no local rank-three or rank-four packet in this control.  Thus
positivity, a disk normalization, one two-point identification, all affine
rank-two local color constraints, and the based infinity product relation
do not imply monodromy at most `D4`.

Rudolph's algebraic-functions theorem makes the quasipositive braided disk an
algebraic curve piece in a bidisc (with the node obtained by the standard
collision of its two positive bands).  It does **not** by itself produce a
global polynomial parametrization `A1->A2` with exactly the charged affine
singularity census and no extra events outside the bidisc.  Consequently the
actual row

```text
h=k=1, beta1(B)=n22=1, n4=0, m=0,
(C,Q)=(A1,1) or (P1,0)                                  (0.4)
```

remains open.  What is now closed is the proposed purely braid-local `D4`
shortcut.  The next discriminator must consume the algebraic link at
infinity / polynomial-parametrization semigroup, or the proper-block first
leg and ruling data.

## 1. Charged campaign inputs

```text
cf157e17db8179b590f15808aab84447717df343735416578e005a2085d73d4e
  xmodel/block-descent-a1-quartic-minimal-cycle-nodal-control-threat-map-sol56-20260830.md
768cf08fe2be7a72e9e17cd15acd56976b6743cefa293bf11472a4fb4e701805
  xmodel/block-descent-a1-quartic-branch-topology-acyclic-obstruction-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d
  xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md
b9f0352ce63513ce16925f9bf4d7b5be11e0246c9426ecc72cf477cd977103a0
  ops/block_descent_a1_quartic_cycle0_braid_escape_replay.py
```

The braid conventions and algebraic-realization firewall are checked against
the following primary sources:

```text
Lee Rudolph, "Algebraic functions and closed braids",
Topology 22 (1983), 191--202,
DOI 10.1016/0040-9383(83)90031-9.

Daniel C. Cohen and Alexander I. Suciu,
"The braid monodromy of plane algebraic curves and hyperplane arrangements",
Commentarii Mathematici Helvetici 72 (1997), 285--315,
DOI 10.1007/s000140050017; arXiv:alg-geom/9608001.
```

Only standard braid monodromy and affine Zariski--van Kampen are consumed.
No classification of rational one-place curve complements is asserted.

## 2. Based braid coloring, not permutation propagation

Choose a generic finite projection of the target branch and a regular fibre
with geometric meridians `x_1,...,x_N`.  A braid word acts on a tuple of
quartic meridian images by the Hurwitz action.  This report uses the right
action

```text
(g_i,g_(i+1))*sigma_i
  =(g_i g_(i+1) g_i^(-1), g_i).                         (2.1)
```

The inverse convention reverses the displayed words but changes no
conclusion.  If `beta_v` is the based braid monodromy around a finite
critical value, a homomorphism

```text
rho:pi1(A2-B)->S4
```

with fibre-color tuple `T=(g_1,...,g_N)` must satisfy

```text
T*beta_v=T.                                             (2.2)
```

Locally, a simple smooth critical point is a positive band

```text
a sigma_i a^(-1).                                      (2.3)
```

The two colors after transport by the tail `a` must be equal when the
quartic local factor has rank two.  A positive node is

```text
a sigma_i^2 a^(-1),                                    (2.4)
```

and its two transported colors may be distinct only when they commute; the
`(2,2)` row requires them to be disjoint transpositions.

The false shortcut replaces (2.1) by the permutation action of the braid on
puncture indices.  A polynomial normalization `A1->A1` does make the finite
critical permutations transitive.  It does **not** make the original
`g_i` equal: a conjugating tail `a` can turn two different base colors into
the same local color in (2.3).  This is the standard knot/quandle-coloring
phenomenon, and it is exactly where the proposed generalization from the
named nodal cubic breaks.

The named cubic has a tail-free half twist, so its relation really is
`a=b`.  An arbitrary polynomially parametrized branch need not admit a
simultaneously tail-free system.  Tangential conductor and unibranch
singularities make this warning stronger, not weaker: their local factor
still constrains the *transported* colors, while their braid tails retain
the embedding information.

## 3. Exact perfect-matching dichotomy

Fix (0.1).  If `g tau g^(-1)=upsilon`, then `g` carries the support
`{1,2}` to `{3,4}` and its complement to `{1,2}`.  Hence

```text
g in Stab(12|34)=D4.                                    (3.1)
```

There are four such transporters, and every group `<tau,g>` has order eight.
Thus the stable letter supplied by the conductor cycle itself is
matching-preserving.

The complete `S4` census is:

```text
Stab(M):             8 elements;
outside Stab(M):    16 elements
  4 cross transpositions,
  8 three-cycles,
  4 four-cycles.                                           (3.2)
```

The matching stabilizer is a maximal subgroup of `S4`.  Direct enumeration
also gives

```text
<D4,g>=S4 for every g outside D4.                         (3.3)
```

Because plane-curve complement groups are meridian-generated, an outside
transport word contains, after resolving it into based meridians, a first
transposition whose support crosses `M`.  Conversely any cross transposition
in (0.2), together with `(12),(34)`, generates `S4`.  Therefore the following
are equivalent at the finite-image level:

```text
all based colors preserve M;
the image is contained in D4;
the cubic-resolvent image fixes the point M;
there is no cross-meridian / outside-D4 transport.         (3.4)
```

Local `(2,1,1)` and `(2,2)` factor data decide none of the conjugating tails
in (2.3)--(2.4).  That missing datum is the exact primitive-overlap escape.

## 4. Explicit four-strand primitive packet

Work in `B4=<s_1,s_2,s_3>` and color a regular projection fibre by

```text
T=((34),(34),(23),(12)).                                  (4.1)
```

This tuple generates full `S4`.  Define three simple positive bands

```text
b1 = s1,
b2 = s2^3 s1 s2^(-3),
b3 = s3 s2^3 s1 s2^(-3) s3^(-1),                        (4.2)
```

and one positive node band

```text
n = s2 s3^2 s2^(-1).                                     (4.3)
```

The deterministic replay verifies the following exact statements under
(2.1).

1. `T*b_j=T` for `j=1,2,3`.  In the local frame of each band, the two
   colliding colors are both `(34)`.  Every simple affine packet is therefore
   compatible with one rank-two factor; no cusp/overlap is hidden locally.
2. `T*n=T`.  After the tail `s2`, the two node colors are `(34),(12)`, so
   they are distinct disjoint transpositions, exactly the `(2,2)` packet.
3. The underlying permutations of `b1,b2,b3` are the star edges
   `(1 2),(1 3),(1 4)`.  They make the normalization covering connected.
4. Three simple branch points on four sheets give

   ```text
   chi(normalization)=4-3=1.                              (4.4)
   ```

5. The total based infinity braid is

   ```text
   beta_infinity=b1 b2 b3 n
    =s1 s2^3 s1 s2^(-3)
       s3 s2^3 s1 s2^(-3) s3^(-1)
       s2 s3^2 s2^(-1).                                  (4.5)
   ```

   Its normalization permutation is a four-cycle.  Together with (4.4),
   this says that the normalization is a disk with one boundary component.
   Collapsing the node pair gives first Betti number one.
6. `T*beta_infinity=T`, as required by the based product relation, but the
   base color `(23)` crosses the node matching `12|34`.  Thus the quartic
   image is `S4`, not `D4`.

This is the requested exact primitive escape.  The three local simple
packets all look like `(34),(34)` only after their different braid tails are
applied.  Erasing the tails reduces (4.2) to three identical half twists and
incorrectly collapses (4.1) to one color.

## 5. What the infinity relation does and does not say

Let `delta_1,...,delta_s` be positively oriented loops around all finite
critical values of the projection, and `delta_infinity` the boundary loop.
On the compactified projection base,

```text
delta_1 ... delta_s delta_infinity=1.                    (5.1)
```

Accordingly, after fixing path-composition convention, the infinity braid is
the product of the finite based braid factors (or its inverse if
`delta_infinity` is taken with the opposite orientation).  Equation (4.5) is
the literal product convention used by the replay.

Polynomiality with one normalization place at infinity constrains the
*permutation* of (4.5) to be one cycle.  It neither deletes the pure-braid
parts of the tails nor turns (5.1) into equality of the fibre meridians.
The packet (4.1)--(4.5) satisfies both the one-cycle permutation condition and
the full based Hurwitz relation while retaining a cross color.

Thus there is no additional free generator named "infinity", but there is
genuine infinity information: it is the conjugating/pure-braid content of
the finite factorization and its product.  Calling (5.1) a product of finite
loops does not show that every factor preserves one globally based matching.

## 6. Algebraic realization and the remaining global gap

Each factor in (4.2) is a conjugate of a positive Artin generator.  The node
factor (4.3) is the square of such a positive band.  Hence (4.5) is
quasipositive.  Rudolph proves that quasipositive band representations are
realized by algebraic `n`-valued functions without poles, equivalently by
algebraic braided curve pieces in a bidisc.  The two identical positive bands
in (4.3) may be collided to the standard positive ordinary-node model.

This prices the control more strongly than a free-group fantasy: complex
orientation, positivity, disk normalization, the one-boundary infinity
permutation, and algebraicity on a compact bidisc all coexist with the full
`S4` coloring.

The theorem must not be overextended.  It does not establish that the
algebraic curve piece extends to an affine plane curve whose normalization is
globally `A1`, whose only two-point normalization fibre is this node, and
whose remaining affine singularities have the exact charged census.  A
polynomial approximation can create extra discriminant events outside the
chosen bidisc.  Nor does the packet construct the finite-flat quartic surface
`Y`, the first Keller leg, constant units, or either ruling row in (0.4).

Therefore:

```text
abstract S4 representation:                   realized;
positive singular braided disk:               realized;
algebraic curve piece in a bidisc:             licensed by Rudolph;
global polynomial A1 branch with exact census: OPEN;
actual proper block / Keller first leg:        OPEN.       (6.1)
```

The cheapest decisive successor is now sharply specified.  Either:

1. realize (4.1)--(4.5), or any Hurwitz-equivalent packet, by explicit
   polynomials `(x(t),y(t))` with exactly one two-point conductor fibre and
   audit its complete affine and infinity braid; or
2. prove from the splice/Puiseux semigroup of a global polynomial `A1` curve
   that every admissible infinity braid factorization is `D4`-colorable only.

Only after such a global theorem may `R4-CYCLE-0` be closed.  In parallel,
the proper-block ruling and nonprincipal ramification class remain stronger
discriminators than complement topology alone.

## 7. Maximum-safe campaign update

Promote exactly the following.

1. A conductor transporter between disjoint quartic transpositions preserves
   their perfect matching and is `D4`-valued.
2. The exact primitive escape is an outside-`D4` based braid tail, equivalently
   a cross transposition in some based meridian color.  Any such escape gives
   `S4` once the node matching is present.
3. The explicit packet (4.1)--(4.5) passes every finite braid, positivity,
   disk-normalization, one-node, and local rank-two color gate.  Therefore
   those gates do not exclude `R4-CYCLE-0`.
4. The packet is not yet a global polynomial-parametrized branch satisfying
   the full ledger.  The two ruling rows in (0.4) remain open.

Retract any proposed argument that transitivity of the normalization
projection propagates equality of the original based transposition colors.
It propagates puncture indices; Hurwitz tails retain conjugation data.

Do not infer existence of a finite-flat quartic cover, an actual block, a
Keller map, or a JC2 counterexample from this braid control.

## 8. Deterministic verification and firewalls

The replay is

```text
b9f0352ce63513ce16925f9bf4d7b5be11e0246c9426ecc72cf477cd977103a0
  ops/block_descent_a1_quartic_cycle0_braid_escape_replay.py
```

Ordinary, `python3 -O`, and `python3 -OO` executions are byte-identical, with

```text
stdout SHA-256:
ee32d7f080a79618111a8d43f6a82618272aed73415b5c627e3e18c130d904c3

status=PASS-R4-CYCLE-0-BASED-BRAID-ESCAPE
payload_sha256=79e9aa4e133a8dee70a48527c08f3bf9edaa082fac9b0b26d63bb70b073643f1
```

It checks the right Hurwitz action and inverses, every band word, all local
equal/disjoint colors, van Kampen invariance of the full tuple, the star
normalization graph, Euler number, the four-cycle infinity permutation, full
`S4` generation, the order-eight matching stabilizer, and every outside
transporter.  The mutation `--mutate-force-matching` is rejected because it
destroys full `S4` generation.

The replay does not encode the Zariski--van Kampen theorem, Rudolph's
algebraic-realization theorem, collision of two bands to an algebraic node,
global polynomial algebraization, finite flatness, the source-forest theorem,
the ruling theorem, or existence of a Keller first leg.  Those distinctions
are literal output fields and written firewalls.

Nothing here closes `R4-CYCLE-0`, resolves `R4-CYCLE-1`, touches the
disconnected branch horn or the primitive/no-block horn, constructs a
counterexample, or proves JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15663`.
- Body SHA-256:
  `54e702190dca604adb6d8a302c2d4356d3d0e85e10f1b175be52f58fc6ea0146`.
- Frozen basis: `6ed236c23e2fce71d1a279ca541239a405a757bf`.
