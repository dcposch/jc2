# Genus-three one-place branch: cable census and Betti-one obstruction

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`genus3_cable_recovery` lane)  
Frozen basis: `eecdbc8c63f88a3aaff8cc8302382e6075d2bc17`  
Lifecycle: **FINAL+VERIFIED THEOREM / GENUS-THREE CABLE ROWS CLOSED IN THE CHARGED BETTI-ONE HORN**

## 0. Theorem and verdict

Let `B` be a reduced irreducible affine plane curve over `C` whose
normalization is `A1`.  Assume

```text
Delta_aff(B)=sum_p delta_p=3,          b1(B)=1.          (0.1)
```

Suppose also that `pi1(A2-B)` has a transitive representation to `S4`
sending every positive generic meridian to a transposition.  Then, up to
the harmless mirror/orientation convention for the knot at infinity,

```text
K_infinity = T(3,4).                                      (0.2)
```

The complete prime iterated-cable census at genus three is

```text
T(2,+/-7),
T(3,+/-4),
C_(2,+/-3)(trefoil or mirror),
C_(3,+/-1)(trefoil or mirror).                            (0.3)
```

The four rows are separated exactly as follows.

1. `T(2,7)` has no full-`S4` meridian-transposition coloring (also
   `det=7`).
2. `T(3,4)` has 24 labelled full-`S4` colorings and remains.
3. Every sign/chirality version of the winding-two trefoil cable has 72
   labelled full-`S4` colorings, but any polynomial one-place realization
   of this two-step infinity type has `b1(B)>=2`.  It is therefore
   incompatible with the charged `b1(B)=1` packet.
4. Every sign/chirality version of the winding-three trefoil cable has zero
   full-`S4` colorings.  Independently, it violates the one-place
   Abhyankar--Moh semigroup condition and cannot be the infinity type of a
   polynomial one-place curve.

The load-bearing new result is row 3.  The unique conductor-six two-step
delta-sequence is `(6,4,3)`.  Every parametrization in that row has, after
allowed affine/parameter normalizations, the complete form

```text
U(t)=(t^2+h)^2+c*t,
V(t)=(t^2+h)^3+(3/2)c*t*(t^2+h)+(3/8)c^2,      c!=0.     (0.4)
```

Its distinct self-pairs are indexed by roots of

```text
H(s)=s^3+4h*s-c.                                        (0.5)
```

The two endpoints belonging to a root `s` are distinct, with

```text
t+u=s,       tu=c/s-h,       (t-u)^2=-3c/s !=0.          (0.6)
```

The cubic (0.5) cannot have a triple root when `c!=0`; hence it has at
least two distinct roots and (0.6) gives at least two distinct unordered
self-pairs.  If their image points differ, they contribute at least two to
`b1(B)`; if their image points agree, that one normalization fibre contains
at least three points and again contributes at least two.  Thus

```text
delta-sequence (6,4,3)  ==>  b1(B)>=2.                   (0.7)
```

This closes the last genus-three satellite survivor in the irreducible
one-place minimal-cycle packet.  It does not exclude the `T(3,4)` row,
classify reducible branches, or prove JC2.

## 1. Charged campaign inputs and primary sources

The predecessor theorem and review are

```text
03865aae3cc11a5f7de264ef7a66d1e3600ccb983ea8f95079c50d8a28b0b5aa
  xmodel/block-descent-a1-total-delta-two-iterated-knot-s4-obstruction-sol56-20260830.md
72cf551054f1f00f99a9cbea113d7b40b2ea0227111357de74fec3d33b39c347
  xmodel/block-descent-a1-total-delta-fox-localization-hostile-review-gpt55-20260830.md
```

They supply the already-reviewed interfaces

```text
g_3(K_infinity)=Delta_aff(B),
K_infinity is an iterated cable and is prime or trivial,
pi1(S3-K_infinity) ->> pi1(A2-B), preserving meridians.
```

The delta-sequence input is

```text
Abdallah Assi and Pedro A. Garcia-Sanchez,
"On curves with one place at infinity",
arXiv:1407.0490v1 (2014), especially Proposition 2,
the delta-sequence definition before Proposition 13, Sections 4--6,
and Examples 16 and 20.
https://arxiv.org/abs/1407.0490
```

The official arXiv PDF fetched for this audit had SHA-256

```text
05081acd04a51c85d231ff288c8522b83e79d75b28af7f99868c2f5149683bf9.
```

Assi--Garcia-Sanchez gives the characteristic sequence, freeness condition,
conductor formula, fixed-genus enumeration procedure, and the explicit
`(6,4,3)` controls.  Example 16 constructs

```text
(y^3-x^2)^2-x,
```

which is a smooth genus-three member of the one-place pencil and is not our
rational branch.  Example 20 gives a rational polynomial-curve embedding
with delta-sequence `(6,4,3)`, but its abstract curve has an ordinary triple
point and `b1=2`.  The normal-form proof below classifies the entire
parametrized `(6,4,3)` row and shows that this is not an accidental feature
of the example.

Schubert's cable-genus formula and the one-place iterated-cabling interface
are used exactly as charged and reviewed in the predecessor.  No claim that
an arbitrary graph knot is polynomially realizable is made.

For the double-branched-cover correction in Section 7, use the standard
cyclic-cover link construction together with the ADE/Kleinian table:

```text
x^2+y^3+z^4=0 is the E6 surface singularity;
its link is S3/(binary tetrahedral group), of order 24.
```

The binary octahedral group of order 48 corresponds to `E7`, not to the
displayed `E6` hypersurface.  This distinction is independently consistent
with `det(T(3,4))=3`: the binary tetrahedral group has abelianization `C3`.

## 2. Exact genus-three prime iterated-cable census

After winding-one and unknot-producing steps are deleted, Schubert's formula
is

```text
g(C_(p,q)(J))=p*g(J)+(p-1)(|q|-1)/2,
p>=2, gcd(p,q)=1.                                      (2.1)
```

For an unknot companion, genus three means

```text
(p-1)(|q|-1)=6.
```

Coprimality gives exactly `(p,|q|)=(2,7),(3,4)`, up to exchanging torus
coordinates.  For a nontrivial companion, `p*g(J)<=3`; hence `g(J)=1`, so
`J` is a trefoil or mirror.  Equation (2.1) then gives exactly

```text
(p,|q|)=(2,3) or (3,1).                                (2.2)
```

No deeper tower occurs: the only possible nontrivial companion already has
genus one, and any further nontrivial stage would have genus at least two
before the final multiplier.  This proves (0.3), with all signs retained to
make the later exclusion stronger.

## 3. Conductor-six one-place delta-sequences

For a delta-sequence `(r0,...,rh)`, put

```text
d1=r0,       d_(i+1)=gcd(r0,...,ri),       e_i=d_i/d_(i+1).
```

The Assi--Garcia-Sanchez conductor formula is

```text
mu=sum_(i=1)^h (e_i-1)r_i-r0+1.                         (3.1)
```

Here `mu=2g=6`.  Their fixed-genus bound gives `h<=log2(g+1)=2`.

If `h=1`, (3.1) is

```text
(r0-1)(r1-1)=6,
```

and `r0>r1`, coprimality give

```text
(r0,r1)=(7,2),(4,3).                                   (3.2)
```

Now let `h=2`, put

```text
d=d2,       r0=a*d,       r1=b*d.
```

The delta inequalities give `a>b>=2`, `gcd(a,b)=1`, and `d>=2`.  Freeness
at the last step says

```text
d*r2 in <r0,r1>,       equivalently r2 in <a,b>,        (3.3)
```

so `r2>=b>=2`.  Formula (3.1) becomes

```text
6=d*((a-1)b-a)+(d-1)r2+1.                              (3.4)
```

Since

```text
(a-1)b-a=(a-1)(b-1)-1>=1,
```

(3.4) gives `3d-1<=6`, hence `d=2`.  It follows that

```text
2*((a-1)b-a)+r2=5.
```

The only solution under the displayed bounds is

```text
(a,b,r2)=(3,2,3),       (r0,r1,r2)=(6,4,3).            (3.5)
```

Thus the complete conductor-six list is

```text
(7,2),       (4,3),       (6,4,3).                     (3.6)
```

Under the standard Puiseux/cabling dictionary, the first two are the torus
rows `T(2,7)` and `T(3,4)`.  In (3.5), the first gcd drop gives the trefoil
`T(3,2)` and the final drop has winding two and meridional absolute value
three: it is the two-step row `C_(2,3)(trefoil)`, up to signs and mirrors.

The winding-three genus-three tower would require the characteristic data

```text
(9,6,1).                                                (3.7)
```

It fails (3.3), since `3*1` is not in `<9,6>`, equivalently `1` is not in
`<3,2>`.  Therefore the `C_(3,+/-1)(trefoil or mirror)` row is not merely
hard to construct: it is forbidden by the polynomial one-place semigroup
condition.  Absolute characteristic data already gives this conclusion;
changing cabling sign or companion chirality cannot repair freeness.

## 4. Complete `(6,4,3)` parametrization normal form

Let `A=C[U(t),V(t)]` be the coordinate ring of a rational polynomial curve
with delta-sequence `(6,4,3)`.  The reduced-coordinate/approximate-root
construction gives

```text
deg U=4,       deg V=6,
```

and a weighted Weierstrass approximate root of parameter degree three.
Completing the square in `V`, depressing the cubic in `U`, scaling leading
coefficients, and translating the parameter are allowed polynomial target
automorphisms and an affine automorphism of `A1`.  They reduce the root to

```text
V^2-U^3+A*U+B,                                          (4.1)
```

and the parametrization to

```text
U=t^4+a2*t^2+a1*t+a0,
V=t^6+b4*t^4+b3*t^3+b2*t^2+b1*t+b0.                    (4.2)
```

For (4.1) to have degree three, coefficients of `V^2-U^3` in degrees ten
through five must vanish; its degree-four coefficient is cancelled by
`A*U`.  Direct coefficient comparison gives

```text
b4=3a2/2,
b3=3a1/2,
b2=3(4a0+a2^2)/8,
b1=3a1*a2/4,
b0=(12a0*a2+6a1^2-a2^3)/16,                            (4.3)

[t^5](V^2-U^3)=-3a1(4a0-a2^2)/8.                       (4.4)
```

If `a1=0`, canceling the degree-four term with `A*U` leaves no degree-three
term, contradicting `r2=3`.  Therefore `a1=c!=0`, and (4.4) forces

```text
a0=a2^2/4.
```

Writing `h=a2/2`, equations (4.2)--(4.3) are exactly (0.4).  Conversely,
direct expansion gives the required approximate root

```text
V^2-U^3-(3/4)c^2*h*U
  =(c^3/64)(8t^3+24h*t+9c),                            (4.5)
```

of degree three.  Thus (0.4) is not one convenient example; it is the full
normalized row.

There is no hidden cusp in this family.  Exact elimination gives

```text
Res_t(U'(t),V'(t))=-1728*c^5 !=0.                       (4.6)
```

Hence the normalization map is immersive for every allowed `c` and `h`.

## 5. Self-pair cubic and the Betti obstruction

Let `t!=u`, set

```text
s=t+u,       p=t*u.
```

Dividing `U(t)-U(u)` and `V(t)-V(u)` by `t-u` and rewriting symmetrically
gives two equations.  The first is

```text
c+2h*s-2p*s+s^3=0.                                     (5.1)
```

Eliminating `p` from the pair gives

```text
s^4(s^3+4h*s-c)=0.                                     (5.2)
```

The value `s=0` is impossible in (5.1) because `c!=0`.  Conversely, every
root of

```text
H(s)=s^3+4h*s-c                                         (5.3)
```

solves both divided difference equations after setting

```text
p=c/s-h.                                                (5.4)
```

The endpoint quadratic `z^2-sz+p` has discriminant

```text
s^2-4p=-3c/s,                                           (5.5)
```

where (5.3) was used.  It is nonzero, so every root of `H` supplies a
genuine unordered pair of distinct normalization points.  Distinct roots
give distinct pairs because their sums differ.

A cubic has only one distinct root exactly when it has a triple root.  But
a triple root of (5.3) would satisfy `H''(s)=6s=0`, hence `s=0`, contradicting
`H(0)=-c!=0`.  Therefore at least two distinct unordered self-pairs exist.

For a finite normalization `nu:A1->B`, the underlying affine curve is the
topological quotient of the contractible normalization by its finite
normalization fibres, and

```text
b1(B)=sum_z (#nu^(-1)(z)-1).                            (5.6)
```

Take the two distinct pairs above.  If their image values differ, (5.6)
gets at least `1+1`.  If their image values agree, their union contains at
least three distinct normalization points (two distinct two-element subsets
cannot have a two-element union), and that one fibre contributes at least
`3-1`.  In both cases

```text
b1(B)>=2.                                               (5.7)
```

Repeated roots of `H` do not create an escape.  They record tangency or
collision multiplicity, while (5.5) keeps the two endpoints distinct; and
the no-triple-root argument still leaves at least two distinct pairs.

This proves (0.7).  It is precisely the inference needed by the charged
minimal-cycle packet, where `b1(B)=1`; no count of pair equations is being
mistaken for a Betti number.

## 6. Independent `S4` meridian-coloring census

The exact finite enumeration uses closed braids.  Let `X_p` be the positive
permutation braid on `2p` strands interchanging two consecutive blocks of
`p` strands.  Explicitly,

```text
X_2=s2 s3 s1 s2,
X_3=s3 s4 s5 s2 s3 s4 s1 s2 s3.                       (6.1)
```

Represent a trefoil companion by the closure of `s1^(3 epsilon)`, with
`epsilon=+/-1`.  Its blackboard `p`-parallel contributes
`3 epsilon p` to the meridional cable parameter.  A zero-framed standard
braid for the `(p,q)` cable is therefore

```text
W_(p,q,epsilon)=X_p^(3 epsilon)
                 (s1...s_(p-1))^(q-3 epsilon p).       (6.2)
```

Negative powers mean inverse words.  Before using (6.2), the replay checks
its closure is a knot and computes its reduced-Burau Alexander polynomial.
For all eight sign/chirality choices it obtains, up to a Laurent unit,

```text
Delta_C(2,+/-3)(trefoil)(t)
 =(t^2-t+1)(t^4-t^2+1),

Delta_C(3,+/-1)(trefoil)(t)
 =t^6-t^3+1,                                           (6.3)
```

exactly the standard cable formula.  Thus the framing convention is checked,
not guessed.

Assign one of the six transpositions of `S4` to each braid meridian and use
the Artin action

```text
sigma_i:(A,B) |-> (A B A^(-1),A).                      (6.4)
```

The replay exhausts all fixed tuples and retains only tuples generating all
24 elements of `S4`.  The labelled counts are

```text
T(2,7):                                      0;
T(3,4):                                     24;

C_(2,+3)(positive trefoil):                 72;
C_(2,-3)(positive trefoil):                 72;
C_(2,+3)(negative trefoil):                 72;
C_(2,-3)(negative trefoil):                 72;

C_(3,+1)(positive trefoil):                  0;
C_(3,-1)(positive trefoil):                  0;
C_(3,+1)(negative trefoil):                  0;
C_(3,-1)(negative trefoil):                  0.         (6.5)
```

Every full-`S4` coloring has trivial global centralizer, so the counts 24
and 72 represent one and three simultaneous-conjugacy classes,
respectively.  More importantly, (6.5) independently reproduces the
interrupted review's `72/0` satellite verdict without relying on its
intermediate state.

The winding-two row is therefore a genuine group-theoretic survivor; it is
killed only after the polynomial one-place `b1` constraint is used.  The
winding-three row fails both gates independently.

## 7. Correct double cover of `T(3,4)`

The double cover of `S3` branched over the plane torus knot `T(3,4)` is the
link of

```text
x^2+y^3+z^4=0.                                         (7.1)
```

This is the `E6` Kleinian singularity.  Its link is the spherical space form
with fundamental group the binary tetrahedral group

```text
2T,       |2T|=24,       (2T)/Z(2T)=A4.                (7.2)
```

Thus the 24 `T(3,4)` colorings in (6.5) are exactly compatible with the
double-cover determinant lemma: the branched-cover group surjects onto
`A4`, and its abelianization is `C3`.

The previously suggested binary octahedral order 48 is wrong for (7.1).
Binary octahedral is the `E7` group.  The superficial `(2,3,4)` triangle
mnemonic is unsafe here because the non-pairwise-coprime Brieskorn Seifert
normalization changes the effective spherical quotient data.  The ADE
hypersurface identification (7.1) is the clean correction.

## 8. Consequence, signs, and exact scope

Combine Sections 2--7 with the charged total-delta theorem.  Under (0.1),
the infinity knot has genus three and is a prime iterated cable.  The
`T(2,7)` and winding-three rows have no `S4` representation.  The
winding-two row is incompatible with `b1(B)=1`.  Only `T(3,4)` remains,
proving (0.2).

The delta-sequence arithmetic uses positive characteristic values and hence
classifies absolute cabling data.  The braid enumeration separately retains
both cabling signs and both trefoil chiralities.  If a sign/chirality variant
is not allowed by the complex algebraic orientation, it is already absent;
if it is allowed, it enters the unique two-step sequence `(6,4,3)` and is
still killed by (5.7).  No orientation convention weakens the conclusion.

This artifact does not prove that every `(4,3)` parametrization has a
quartic cover, satisfy the local double-plane `C2` gate, or arise from a
Keller block.  It does not treat a reducible branch, more than one place at
infinity, total affine delta above three, or the primitive/no-proper-block
horn.  The exact remaining irreducible one-place genus-three Betti-one
question is the `T(3,4)` row.

## 9. Deterministic replay and mutation

```text
838898b13769b073913caf5c18a72a51387bb6e338573efea5d4f6e206b1c5c8
  ops/block_descent_a1_genus_three_cable_b1_replay.py
```

Ordinary, `python3 -O`, and `python3 -OO` executions are byte-identical:

```text
stdout SHA-256:
8887e27ce81d4ca54ee114bbcbb6b4a503cef2fdd525d5d73934bd0e653a67ed

status=PASS-A1-GENUS-THREE-CABLE-B1-OBSTRUCTION
payload_sha256=b44994b41140c3fdb1c900be4a27e4856dbe89cce68951424630701d9d63a5fb
```

The mutation

```text
python3 ops/block_descent_a1_genus_three_cable_b1_replay.py \
  --mutate-allow-winding-two-b1-one
```

exits with status one at

```text
RuntimeError: distinct self-pairs force affine b1 at least two.
```

The replay checks the genus-three Diophantine census, conductor-six
delta-sequence arithmetic, failure of `(9,6,1)` freeness, all displayed
normal-form identities at independent exact specializations, the immersion
resultant interface, the self-pair/no-triple-root logic, exact standard cable
Alexander polynomials, and all labelled `S4` coloring counts.  It does not
encode the Assi--Garcia-Sanchez theorem, Schubert's genus theorem, the
Puiseux/cabling dictionary, normalization-quotient topology, or the ADE link
classification; those are the written primary interfaces above.

No heavy local CAS was used.  Nothing here constructs a quartic cover,
settles the surviving `T(3,4)` row, proves a proper block exists, or proves
JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18228`.
- Body SHA-256:
  `607d796490d0b5edde5d5d965279ae7a2b6d90d33a0c831cafc6ad74a57025d7`.
- Frozen basis: `eecdbc8c63f88a3aaff8cc8302382e6075d2bc17`.
