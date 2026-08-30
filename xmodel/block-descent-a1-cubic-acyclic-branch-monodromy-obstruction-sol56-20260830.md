# Proper-cubic affine survivor: acyclic branch monodromy obstruction

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`sectioned_two_support_universal` lane)  
Frozen basis: `f91e751041a0f926b6981c9bfe33aa1665c2c226`  
Lifecycle: **EXACT PROVISIONAL THEOREM / CUBIC AFFINE BRANCH ROW CLOSED / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Verdict

Let

```text
pi:Y -> A2_C
```

be finite flat of degree three, with `Y` integral and normal.  Let `B` be
the reduced branch support.  Assume:

```text
B is connected and topologically contractible;
every geometric fibre over B has partition (2,1).
```

Then no such cover exists.  More precisely, after restricting over
`A2-B`, the connected degree-three cover would have transitive monodromy,
but the Lin--Zaidenberg classification forces its whole monodromy image
into one transposition subgroup of `S3`.

This closes the singular **and reducible** acyclic-branch escape left open
by the previous cubic funnel.  The campaign's extra hypotheses that every
component is one-place, the affine incidence is a forest, and
`R_red -> B` is an analytic homeomorphism are stronger than needed for this
obstruction.  The result remains conditional on the promoted proper-block
inputs actually supplying the displayed finite-flat cover, contractibility,
and the `(2,1)` partition at every affine branch value.  It is not a theorem
about degree at least four, an arbitrary non-acyclic branch, or JC2 without
the proper cubic block.

## 1. Exact classification source and charged warning control

The source used here is:

```text
Ivan Arzhantsev and Mikhail Zaidenberg,
"Acyclic curves and group actions on affine toric surfaces",
arXiv:1110.3028v2; MPIM Preprint 2011 (61),
published in Affine Algebraic Geometry (World Scientific, 2013), 1--41,
DOI 10.1142/9789814436700_0001.

41245c20b1b61a0dcf8116340672d037b977e6759d5d99054fc06c292d5c36fc
  refs/arzhantsev_zaidenberg_acyclic_curves_arxiv1110.3028v2.pdf
```

On printed page 3, subsection 1.1 defines an acyclic curve to be connected
and simply connected.  Theorem 1.3(b), printed pages 3--4 (PDF pages 3--4
of the pinned arXiv copy), explicitly applies to **any reduced, simply
connected plane curve**, not only an irreducible one.  Up to an algebraic
automorphism of `A2`, it gives exactly one of

```text
(I)   y^epsilon_y p(x)=0;

(II)  x^epsilon_x y^epsilon_y
      product_(i=1)^r (y^a-kappa_i x^b)=0,
```

where `epsilon_x,epsilon_y` are zero or one, `p` has simple roots,
`a,b>=1` are coprime, `r>0`, and the nonzero `kappa_i` are pairwise
distinct.  Thus the cited theorem genuinely includes the reducible rows.
The irreducible part is the original Lin--Zaidenberg theorem; the full
reduced statement above is the exact result charged here.

The following sealed hostile-review control is also charged:

```text
9e32b0fe8835b6ea6002036b95e2261a612754d73d796cb10edda347cf3cf65e
  xmodel/block-descent-a1-cubic-affine-survivor-funnel-hostile-review-gpt55-20260830.md
```

Its explicit cover

```text
z^3-3z+2+xy=0
```

has reduced branch `xy(xy+4)=0`, local `(2,1)` companions, and global
`S3` monodromy.  Its branch is disconnected.  This is the required warning
that unrelated local companion labels do not globalize in general.  The
proof below never assumes such propagation: it uses either a central
global meridian in normal form (I), or a single local group which is already
the whole global group in normal form (II).

## 2. The exact local and global monodromy statements

Put

```text
U=A2-B,                 V=Y-pi^(-1)(B).
```

Then `V->U` is finite etale of degree three.  Since `Y` is integral, `V` is
a nonempty irreducible open subset, hence the monodromy representation

```text
rho:pi1(U,u0)->S3
```

acts transitively on the three sheets.

At a point `b in B`, pass to the henselian local base.  The fibre algebra
has two distinct local factors of lengths two and one.  Its two fibre
idempotents lift uniquely, splitting the finite-flat algebra into factors
of ranks two and one.  A unital finite-flat rank-one algebra over the local
base is the base itself.  Hence the full local complement group fixes the
companion sheet:

```text
rho(pi1(local complement at b)) <= a conjugate of S2.       (2.1)
```

At a generic smooth point of every branch component its meridian is a
nonidentity transposition.  This is point-local information only.  No
choice of a common globally based companion letter has been made.

An automorphism of `A2` transports the cover and preserves all these
properties, so the two canonical forms may now be treated directly.

## 3. Form (I): lines and arbitrary combs

First list every connected degeneration of

```text
y^epsilon_y p(x)=0.                                      (3.1)
```

If `epsilon_y=0`, the curve is a disjoint union of the vertical lines over
the simple roots of `p`; connectedness forces exactly one root.  If
`epsilon_y=1` and `p` is constant, the curve is the horizontal line.  Both
are coordinate lines.  Their complement has fundamental group `Z`, and
the branch meridian maps to a transposition, so the image has order two and
is not transitive.

It remains to include, explicitly, every comb with one, two, or arbitrarily
many teeth.  Write the distinct roots as `alpha_1,...,alpha_s`, `s>=1`.
Then

```text
U=(C-{alpha_1,...,alpha_s}) x C*,
pi1(U)=F_s x <h>,                                        (3.2)
```

where `h` is the horizontal-line meridian and is central.  The generic
`(2,1)` hypothesis along `y=0` gives `rho(h)=tau`, a transposition.  For
every `gamma in pi1(U)`, centrality gives

```text
rho(gamma) tau = tau rho(gamma).
```

But the centralizer of a transposition in `S3` is exactly `<tau>`, of order
two.  Hence

```text
rho(pi1(U)) <= <tau>,                                    (3.3)
```

which is intransitive.  This proof covers `s>=2` without identifying any
tooth companion with a globally transported local label.

There are two common meanings of the campaign's infinity phrase, and
neither leaves a gap.  Every individual line in a comb is one-place.  If
instead the **whole** projective closure is required to have one
set-theoretic point at infinity, a nontrivial comb is already impossible:
the horizontal line meets infinity at `[1:0:0]`, while every vertical tooth
meets it at `[0:1:0]`.  Thus that stronger reading leaves only the coordinate
line row, already handled above.

## 4. Form (II): the weighted-cone rows

Now let

```text
B={x^epsilon_x y^epsilon_y
   product_i(y^a-kappa_i x^b)=0}.                         (4.1)
```

Every component passes through the origin, and (4.1) is invariant under
positive weighted scaling

```text
r.(x,y)=(r^a x,r^b y),             r>0.                  (4.2)
```

Indeed both `y^a` and `x^b` have weight `ab`, and the coordinate axes are
also invariant.  With

```text
N(x,y)=|x|^(2/a)+|y|^(2/b),
```

one has `N(r.(x,y))=r^2 N(x,y)`.  Every positive scaling orbit in
`A2-{0}` meets the weighted sphere `N=1` exactly once.  Since `B` is a
weighted cone, the global complement and the complement in an arbitrarily
small weighted ball both deformation retract onto the same link complement.
Ordinary and weighted balls are cofinal neighborhoods of the origin, so

```text
pi1(A2-B) isomorphic to pi1(local complement of B at 0).  (4.3)
```

Apply (2.1) at the single point `0`.  Equation (4.3) puts the **whole**
global monodromy image inside one companion-fixing `S2`, hence inside an
intransitive subgroup of `S3`.  Again no propagation among separately based
local groups is used.

For completeness, a one-point-at-infinity reading only narrows (4.1):

```text
a<b: all monomial factors meet [0:1:0]; x=0 may occur, y=0 may not;
a>b: all monomial factors meet [1:0:0]; y=0 may occur, x=0 may not;
a=b: coprimality gives a=b=1, and one common infinity point permits
     only one of the distinct line directions.
```

The weighted radial proof covers both the unrestricted componentwise
one-place reading and every one-point subrow above.

## 5. Contradiction and proper-block consequence

The two classified forms exhaust every reduced connected simply connected
plane curve.  Sections 3 and 4 show in all cases that

```text
rho(pi1(A2-B)) is contained in a subgroup of order two.
```

Such a subgroup fixes one of three letters and cannot act transitively.
This contradicts connectedness of `V->A2-B` from Section 2.  Therefore the
cover in Section 0 does not exist.

In the promoted proper-cubic affine equality row, the previous inputs give
exactly: `B` reduced, connected and analytically contractible; the finite
flat cubic has no triple or `S0` fibres; and the complement cover is
connected.  Subject to those charged inputs, the entire remaining cubic
branch row is empty.  In particular, the reducible branch conclusion in the
earlier provisional infinity-gate producer is superseded by this exact
classification argument.

## 6. Desk replay

The finite `S3` part is independently replayed by

```text
648022d35191b67d9f1e1eec61cddc95bbee745001410ad1fbbffa1044417389
  ops/block_descent_a1_cubic_acyclic_branch_monodromy_replay.py
```

Ordinary, `-O`, and `-OO` runs give the identical payload hash

```text
0e1afb3f3d226393fa143d972620607d46ee3db7daf8b37751fee2d2402db740.
```

It checks combs with one through six teeth, the cone subgroup, and the
disconnected two-transposition `S3` warning.  The deliberate mutation
`--mutate-drop-comb-centrality` is rejected.  The script has zero AST
`Assert` nodes.  It does not encode or purport to verify the
Lin--Zaidenberg classification, the product complement (3.2), weighted
radial equivalence (4.3), or algebraic cover hypotheses.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9646`.
- Body SHA-256:
  `1153c316bedf4df9daf8536e3128bfaf5ff0993f399dffad3a1a43dcb160e8c6`.
- Frozen basis: `f91e751041a0f926b6981c9bfe33aa1665c2c226`.
