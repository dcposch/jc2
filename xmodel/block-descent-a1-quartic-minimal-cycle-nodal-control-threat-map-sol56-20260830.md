# Rank-four minimal connected cycle: nodal control and exact threat map

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`rank4_nodal_horn` lane)  
Frozen basis: `0ad5f9a2d684698ea524efeb4576a3884c92ca7d`  
Lifecycle: **FINAL+VERIFIED SHARP THREAT MAP / CONTROL EXCLUDED / ACTUAL HORN OPEN**

## 0. Verdict

The concrete nodal cubic proposed as the first desk control cannot support
the required quartic monodromy.  For

```text
B0: y^2=x^2(x+1),       (x,y)=(t^2-1,t(t^2-1)),
```

Zariski--van Kampen gives

```text
pi1(A2-B0)=Z.
```

More precisely, a simple vertical tangency equates the two node-branch
meridians.  A quartic `(2,2)` fibre requires those meridians to be two
different disjoint transpositions.  Hence no based `S4` representation with
the charged local fibre data exists for `B0`.

This does **not** exclude the actual minimal connected-cycle horn.  The
ledger hypotheses

```text
h=k=1, beta1(B)=n22=1, n4=0
```

say that the target branch is obtained topologically from a connected
contractible source forest by one two-point identification.  They do not say
that the source forest is irreducible, that the identification is an ordinary
node, that there are no unibranch singularities, or that the embedded curve
has the complement group of `B0`.

The main new narrowing is exact.  If `(2,1,1)` is generic on every branch
component, so that the `(3,1)` locus is finite of cardinality `m`, then the
proper-block ruling leaves only

```text
m=0:  (C,Q)=(A1,1) or (P1,0);
m=1:  (C,Q)=(A1,0).                                  (0.1)
```

No row with `m>=2` can be an actual proper block.  A single `(3,1)` cusp
packet plus one `(2,2)` matching is already abstractly sufficient to generate
`S4`; there are 72 based labelled packets and every one generates `S4`.
If `m=0`, the extra overlapping-sheet transport needed for `S4` must instead
come from the global embedding or the unique place at infinity.

The conductor budget gives equality, not a contradiction:

```text
generic: 4=2+1+1,             node packet: 4=2+2.      (0.2)
```

The cubic resolvent also does not remove the cycle.  The two disjoint node
transpositions have the same image in `S3`, but the normalized local cubic
factor is a double cover branched over both node branches; its branch support
is still nodal, not acyclic.

Finally, an explicit smooth finite-free quartic spectator realizes

```text
h=k=1, beta1=n22=1, n4=0, full S4,
```

together with two `(3,1)` cusps.  Its deleted ramification complement is
`A1 x Gm`, with Euler number zero and a nonconstant unit, so it fails the
proper-block ruling and unit gates.  This proves that local normality,
flatness, node matching, conductor length, and abstract monodromy alone cannot
close the horn.  The next discriminator must consume the global first leg,
the nonprincipal ramification/different class, and the based infinity
relation.

## 1. Charged campaign inputs

```text
768cf08fe2be7a72e9e17cd15acd56976b6743cefa293bf11472a4fb4e701805
  xmodel/block-descent-a1-quartic-branch-topology-acyclic-obstruction-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
c229cbc4eb93722eb9d5c247c5e0616901a0e5cfce0278613cffc7f9e4fcbe85
  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-coordinator-integration-sol56-20260830.md
f19d7d57a4995d88f442b29124403866b77d92238efb0469b6ced354ec522801
  xmodel/af-pi1-nodal-squeeze-source-audit-sol56-20260830.md
6677635e5f06fe908aa7a6d7837a7f721edc4236b43bf731baaf330ed45848c4
  ops/block_descent_a1_quartic_minimal_cycle_replay.py
```

No external theorem beyond the standard Zariski--van Kampen construction is
needed for the new conclusions.  In particular, no classification of all
rational one-place nodal plane curves is asserted or used.

## 2. Exact scope of the minimal horn

Assume an actual strict block factorization

```text
A2 --g1--> Y --pi=g2--> A2,       deg(pi)=4,
R=NonEt_Y(pi)_red,                U=Y-R,
B=pi(R)_red.
```

The charged block package makes `Y` integral and normal, `pi` finite flat,
and `g1:A2->U` dominant, quasi-finite and etale.  It also gives

```text
O(U)^*=C^*,       e(U)=e(C)+Q,       C=A1 or P1,       Q>=0. (2.1)
```

Charge the connected minimal-cycle row

```text
h=b0(R)=1,       k=b0(B)=1,
n22=1,           beta1(B)=1,
n4=0.                                                    (2.2)
```

The source-forest theorem makes `R(C)` contractible.  The finite map
`R->B` is point-bijective except at the unique `(2,2)` value, where it has
two reduced preimages.  Thus `B` has the homotopy type of a circle.  This is
a topological quotient statement only.

Several tempting strengthenings are not licensed by (2.2):

1. `h=1` counts connected components, not irreducible components.  The
   connected source forest can have several rational components.
2. `n22=1` records one two-point fibre of `R_red->B`; it does not prove that
   the two embedded target branches are transverse.  The ordinary node is
   the cleanest control, not the general theorem.
3. Point-bijective unibranch singularities do not change `beta1(B)` and are
   invisible in (2.2).
4. One place at infinity does not determine the affine complement group.
   Its knotting and the singularity at infinity remain global data.

Assume now that every irreducible component is generically `(2,1,1)`.  Then
`T31` is finite; put `m=|T31|`.  The exact quartic ledger specializes to

```text
e(U)=4-2h-e(T31)-2n4=2-m.                              (2.3)
```

Combining (2.1) and (2.3) gives exactly the three rows (0.1).  Thus the word
"minimal" still splits into a no-affine-cusp row and a one-affine-cusp row.
The phrase "the special node is `(2,2)`" does not by itself decide between
them.

## 3. The nodal cubic control has cyclic complement

For

```text
B0: y^2=x^2(x+1),
```

project to the `x`-axis.  Over `x` outside `{-1,0}`, the fibre is a line
minus the two points

```text
y=+-x*sqrt(x+1).
```

Let `a,b` be positive meridians around those two points in a generic fibre.
The critical value `x=-1` is a simple vertical tangency; its braid is one
half-twist `sigma`.  The value `x=0` is the ordinary node; its braid is the
full twist `sigma^2`.  Affine Zariski--van Kampen therefore gives the free
group on `a,b` modulo the two braid coinvariant relations.  In any standard
Artin convention these are equivalently

```text
half-twist: a=b,
full twist: [a,b]=1.
```

Consequently

```text
pi1(A2-B0)=<a,b | a=b, [a,b]=1>=Z.                    (3.1)
```

At the node, the two local branch meridians are the transported `a` and `b`.
Equation (3.1) makes them equal.  In a quartic `(2,2)` fibre the henselian
local algebra has two rank-two factors.  Its two divisorial inertia elements
must be distinct disjoint transpositions, conjugate to

```text
(12), (34).                                             (3.2)
```

Equations (3.1)--(3.2) are incompatible.  Equivalently, every homomorphism
from (3.1) which sends a meridian to a transposition has image `C2` and is
intransitive.  Thus `B0` supports neither the quartic cover nor an actual
proper block.

The load-bearing relation is `a=b`, supplied by the additional smooth
vertical tangency at `x=-1`.  An arbitrary polynomially parametrized
one-place curve with one two-point conductor identification need not have
that braid factor.  The control calculation cannot be promoted to the whole
row (2.2).

## 4. Based `S4` packets and the cubic resolvent

Let the three pairings of four sheets be

```text
12|34,       13|24,       14|23.
```

The cubic-resolvent quotient

```text
q:S4 -> S3
```

is the action on this set.  Directly,

```text
q((12))=q((34));                                        (4.1)
```

and the same holds for the two members of every perfect matching.  Thus a
quartic node with local group `<(12),(34)>` has resolvent image `C2` and
normalized resolvent fibre `(2,1)`.

Equation (4.1) is not a quartic meridian equality.  It says only that their
product `(12)(34)` belongs to the Klein-four kernel.  At an ordinary node
with target local equation `uv=0`, the corresponding henselian cubic algebra
has the model

```text
C[[u,v]][z]/(z^2-uv)   x   C[[u,v]].                   (4.2)
```

The rank-two factor in (4.2) is normal, its branch support is both axes, and
its ramification support maps point-bijectively to the node.  Hence passing
to the normalized cubic resolvent preserves the target cycle.  It does not
produce the connected acyclic branch required by the cubic block theorem,
and the resolvent has no inherited Keller first leg in any case.

There is nevertheless a useful exact group discriminator.  Fix
`tau=(12)`.  Every `g in S4` satisfying

```text
g*tau*g^-1=(34)
```

preserves the unordered partition `12|34`; all four choices generate with
`tau` a group of order eight, conjugate to `D4`.  Therefore a presentation
generated only by one node transposition and one transporter to its disjoint
mate cannot have full `S4`.  This is a conditional one-stable-letter lemma,
not a presentation theorem for an arbitrary curve complement.

The smallest way out is an overlapping transposition.  Two distinct
overlapping transpositions satisfy the cusp braid relation and generate an
`S3` on three sheets.  There are 24 ordered cusp packets and three node
perfect matchings.  For all

```text
24*3=72
```

labelled combinations, the combined subgroup is `S4`.  Their resolvent
images generate all of `S3`.  Thus the `m=1` row in (0.1) is fully feasible
at the abstract local-monodromy level.  In the `m=0` rows, any full-`S4`
representation must obtain an overlapping transport from infinity or other
global based relations rather than from an affine `(3,1)` point.

## 5. The conductor and sheet budget is exactly saturated

At the generic point of a branch component the quartic fibre has one simple
ramified factor and total unramified degree two:

```text
d=4,       E_B=2,       a_B=2,       d=E_B+a_B.         (5.1)
```

At the unique conductor collision, the two distinct ramification points
each have local fibre length two.  Finite flatness gives

```text
4=length(pi^-1(b))=2+2.                                (5.2)
```

Thus the general packet inequality `d>=2e`, or equivalently `a_B>=e` when
`e=2`, is equality here.  There is no unused length from which to derive a
contradiction.

The stronger sheet-deficient formula `d=e+1` is unavailable.  It assumes
only one unit of generic unramified/affine degree.  The quartic fixed-sheet
row has two such units, either as two residue-degree-one primes or as the
same total residue degree organized differently.  A fixed block sheet of
`g2` is also not an individual sheet of the full Keller map.  Multiplying by
the first-leg degree creates no new packet deficit; it only repeats the
already-accounted missing-sheet ledger.

## 6. Exact finite-flat spectator: all local gates can coexist

Consider

```text
pi:A2_(s,w) -> A2_(s,y),
(s,w) |-> (s, y=w^4-2w^2+s*w).                         (6.1)
```

It is finite free of degree four: `w` satisfies the monic equation

```text
w^4-2w^2+s*w-y=0,
```

and `1,w,w^2,w^3` is a target-module basis.  The source is the smooth normal
integral plane.  Its ramification curve is

```text
R: 4w^3-4w+s=0,
```

the graph `s=4w-4w^3`, hence `R isomorphic to A1`.  Writing its parameter as
`t`, the branch is

```text
(s,y)=(4t-4t^3, 2t^2-3t^4).                            (6.2)
```

Its projective closure meets the line at infinity only at the image of
`t=infinity`; hence its normalization in the affine chart is `A1` and it has
one place at infinity.

The self-intersection and cusp census is elementary.  If `t!=u` have the
same image, equality of the first coordinate gives

```text
t^2+t*u+u^2=1,
```

while equality of the second gives

```text
(t+u)*(2-3(t^2+u^2))=0.
```

The second-factor alternative forces `(t-u)^2=0`; the remaining alternative
is `u=-t`, `t^2=1`.  Thus there is exactly one self-node, joining `t=1` and
`t=-1`, at `(s,y)=(0,-1)`.  The two tangent slopes are `+1` and `-1`, so it
is ordinary.  At that value,

```text
w^4-2w^2+1=(w-1)^2(w+1)^2,                             (6.3)
```

giving the `(2,2)` fibre.

The derivative of (6.2) is

```text
(s'(t),y'(t))=4(1-3t^2)*(1,t).
```

It vanishes exactly at `t^2=1/3`.  The determinant of the second and third
derivative vectors there is `384`, so both points are ordinary cusps.  If
`r^2=1/3`, the fibre factorization is

```text
w^4-2w^2+(8r/3)w-1/3=(w-r)^3(w+3r),                   (6.4)
```

of type `(3,1)`.  There is no `(4)` fibre.  Away from (6.3)--(6.4), every
branch fibre is `(2,1,1)`.

The cover is connected because its source is integral.  Its monodromy is
transitive, contains a generic transposition, and contains a cusp
three-cycle.  Among the transitive subgroups of `S4`, only `S4` contains both
cycle types: the order-four and `D4` rows contain no three-cycle, while `A4`
contains no transposition.  Hence the monodromy of (6.1) is full `S4`.

The source and target ledgers are therefore

```text
h=k=1,       beta1(B)=n22=1,       n4=0,
m=2,         monodromy=S4.                                (6.5)
```

This is not an actual block.  Put

```text
r=s+4w^3-4w.
```

Then `(r,w)` are polynomial coordinates on the source, `R=(r=0)`, and

```text
U=A2-R isomorphic to Gm_r x A1_w.                       (6.6)
```

Thus `e(U)=0` and `r` is a nonconstant unit on `U`.  Moreover the source
surface `Y=A2`, the ramification divisor is principal, and `m=2`; all four
features contradict promoted proper-block requirements.  The spectator is
not a Keller map or a candidate block.  Its role is exact: it realizes the
normal finite-flat conductor, cusp, and full-monodromy packet simultaneously,
so an exclusion must use the global first-leg/ruling/class data that (6.1)
lacks.

## 7. Maximum-safe conclusion and next discriminator

Promote exactly the following.

1. The specific nodal cubic `B0` is excluded by its cyclic complement group.
2. In the minimal connected-cycle horn with generic `(2,1,1)`, the actual
   proper-block ruling permits only the three rows in (0.1); in particular
   at most one affine `(3,1)` value exists.
3. The quartic conductor packet saturates the finite-flat sheet budget and
   is not excluded by it.
4. The two node meridians become equal in the cubic resolvent, but the branch
   cycle survives; the cubic acyclic theorem does not apply.
5. One cusp plus one node is abstractly compatible with full `S4`.  With no
   affine cusp, the missing overlap must be global/infinite.
6. The spectator (6.1) proves that all local cover-side conditions can coexist
   before the proper-block ruling, unit, and nonprincipal-class gates.

Do **not** promote an exclusion of the minimal connected-cycle horn, an
abelian-complement theorem for arbitrary rational one-place nodal curves, or
an inheritance of the cubic proper-block theorem by the resolvent.

The next proof obligation should be split by (0.1):

```text
R4-CYCLE-1:
  m=1, C=A1, Q=0.  Combine the unique cusp packet and node endpoint
  pairing with O(U)^*=C^*, the A1-fibration, and the nonprincipal
  ramification/different class.  The target is to prove that the overlap
  transport forces either a principal boundary character or an extra bad
  ruling fibre.

R4-CYCLE-0:
  m=0.  Compute the based braid/meridian relation at the unique infinity
  place.  Every affine local image lies in a rank-two factor; prove that the
  infinity transport preserves one perfect matching (hence gives at most
  D4), or exhibit the exact primitive class which permits an overlap.
```

A frozen branch equation or infinity braid word should be fed to a small
finite representation enumerator before any heavy computation.  No AWS
calculation is presently justified: the missing input is a theorem-level
global relation, not a large elimination.

## 8. Desk verification and firewalls

The deterministic replay is

```text
6677635e5f06fe908aa7a6d7837a7f721edc4236b43bf731baaf330ed45848c4
  ops/block_descent_a1_quartic_minimal_cycle_replay.py
```

Ordinary, `python3 -O`, and `python3 -OO` executions are byte-identical, with

```text
stdout SHA-256:
df9ffae6c15906af7b57f8e3c5b1297b125e0f5368e57fa6236d437fec1fa973

status=PASS-QUARTIC-MINIMAL-CYCLE-THREAT-MAP
payload_sha256=561550f5cdd04f4aac465252a1d36a51c1ee6b3090cd60a022fbed2f2c928c9b
```

It checks the three node matchings, the `S4->S3` equality, all four
node-only transporters, the 24 cusp packets, all 72 cusp-plus-node `S4`
packets, the exact ruling rows, both sheet budgets, and the displayed
spectator fibre factorizations.  The mutation
`--mutate-resolvent-separates-node` is rejected.

The replay does not encode Zariski--van Kampen, normality, finite flatness,
the source-forest theorem, the ruling theorem, the local algebra model (4.2),
or existence of an actual block.  Those are written mathematical inputs and
must not be inferred from a passing finite check.

Nothing in this report constructs a Keller map, proves a rank-four block
exists, excludes all rank-four blocks, touches the disconnected branch horn,
settles the primitive/no-block horn, or proves JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17337`.
- Body SHA-256:
  `c22fc5f741ec4ca618a255184e0115f3e7d06315bcaab7bd000208f805303969`.
- Frozen basis: `0ad5f9a2d684698ea524efeb4576a3884c92ca7d`.
