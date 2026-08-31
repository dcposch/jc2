# ROW-SWEEP: the residual (N=4) cage after wave 10

## 0. Source integrity and typing conventions

The five frozen copies were hashed before they were read.  The hashes were,
in the order charged,

```text
0549dfafe339d20c67fe0d64a0bc713c1e64850013fbaab9f07f654c7fbf8fc2
028b1c03489791f8cd674cc371c8b43c8994784aa65a05c8cfbb6dae269d3129
8b9fe37f142afeb204d356d49dbb3bf535e59ff14a460851486b586b8ec5022a
aa41551f14f34bdae34d9f172be253882f67c8cc3c6cc699ed98b5b85bbc60f0
bafe5e8929a77aa306e76ebdee1b300bbaf579a685f793cd8684ad861f041270
```

and all five match the charge exactly.  References below are to those frozen
copies, although paths are written with the charged `xmodel/` names.

For the delta-sequence conversion I also re-fetched, without saving, the
primary PDF C. Galindo--F. Monserrat, *The Abhyankar--Moh theorem for plane
valuations at infinity*, arXiv:0910.2613v2, from
`https://arxiv.org/pdf/0910.2613v2`.  Its SHA-256 was
`637acfd15d3d73b47f2ddc75b713063ee6e236ff6fef271417d96d5846d5a4c9`,
exactly the custody value already recorded at
`xmodel/m-inf-hostile-review-sol56-20260831.md:101-112`.

`KILLED` means that every configuration in the row reaches a promoted
no-`S_4` gate.  `SURVIVES-AS` records configurations not killed by the full
battery; it is not an existence assertion for a Keller residual.  `OPEN`
names an additional realization, topology, or route-to-tuple lemma that is
still needed.  In particular, numerical admissibility is not called
attainment.

There is one necessary correction to the proposed structural battery.
The order-three/order-four fork is a subtheorem of the **coprime** Main
Theorem and cannot be applied to any row swept here
(`xmodel/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md:30-47`).
Moreover `c(Pi)` in the slice formula is the number of cycles, so an order-three
element has two cycles and a four-cycle has one, not three.  Off the coprime
stratum the promoted facts are only A'(1)--(4)
(`xmodel/pi1s4-close-residual-hostile-review-sol56-20260831.md:51-60`).
Thus even `d` permits `c(Pi)=4` or `2`, and odd `d` permits `3` or `1`, by
parity; the identity itself is
`d=2g_L+c(Pi)+2`
(`xmodel/d1-degree-bound-sol56-20260831.md:357-378`).

Finally, none of the five charged files defines `T` or proves (M-INF-T).
The review instead leaves tangential noncoprime transport open
(`xmodel/pi1s4-close-residual-hostile-review-sol56-20260831.md:149-159`).
Accordingly the two charged values of `T` are treated as frozen labels and
every conclusion using (M-INF-T) is explicitly **CONDITIONAL**.

## 1. Constraint battery and promoted inputs

Put `a=d-n`.  In the infinity chart the branch has orders `(a,d)`
(`xmodel/d1-degree-bound-sol56-20260831.md:60-64`).  With

```text
v=s^a,  u=sum c_k s^k,  e_0=a,
e_i=gcd(e_(i-1),beta_i),  e_h=1,
```

the `beta_i` are integer characteristic numerators, not maximal-contact or
degree-semigroup generators
(`xmodel/m-inf-hostile-review-sol56-20260831.md:19-29`).  A smooth tangent
germ has contact a multiple of `a` strictly below `beta_1`, or contact exactly
`beta_1` (`xmodel/pi1s4-close-residual-hostile-review-sol56-20260831.md:25-31`).
The Euclidean resolution blocks give

```text
2 delta_inf = sum_i (e_(i-1)-e_i) beta_i - a + 1,
M_emb = a+beta_h-1,
M_inf = max(d,M_emb).
```

The second identity is PROMOTED-AS-CORRECTED, including terminal
multiplicity-one centers (`xmodel/m-inf-hostile-review-sol56-20260831.md:39-81`),
and the exact maximum identity is reviewed at
`xmodel/pi1s4-close-residual-hostile-review-sol56-20260831.md:78-92`.
The genus split is
`delta_aff+delta_inf=(d-1)(d-2)/2`; in the residual class
`delta_aff=sum k_p>=1`, with every point exactly two smooth branches
(`xmodel/d1-degree-bound-sol56-20260831.md:310-321`).  In a nodal row this
means exactly `delta_aff` ordinary nodes.

For the infinity census I use the reviewed Abhyankar--Moh/Galindo
delta-sequence conditions: if `Delta=(delta_0,...,delta_s)` begins `(d,n)`,
the successive gcd quotients exceed one,
`n_i delta_i` lies in the semigroup generated earlier, and
`delta_i<n_(i-1)delta_(i-1)`; the primary-source custody and conversion are
recorded at `xmodel/m-inf-hostile-review-sol56-20260831.md:85-124`.
For a rational normalization the gaps of the degree semigroup equal
`delta_aff`; the containment direction is never reversed
(`xmodel/pi1s4-close-residual-hostile-review-sol56-20260831.md:94-108`).

For nodes, (M-INF)

```text
M_inf <= 3d-3
```

implies `pi_1(C^2-D)=Z` and hence kills the prescribed `S_4` quotient
(`xmodel/pi1s4-close-residual-hostile-review-sol56-20260831.md:78-80,110-116`).
The charged tangential analogue is used only conditionally.  The remaining
structural checks are the Chau shapes `(u,1)`, `(odd u,2)`, `(4,3)` and
`g<=gcd(deg P,deg Q)-2`
(`xmodel/d1-degree-hostile-review-gpt55-20260831.md:94-119`), together with
A'(1)--(4).  At every actual affine double point its two meridians must map
to disjoint transpositions; their contact order adds no further local
`S_4` relation (`xmodel/pi1s4-close-residual-hostile-review-sol56-20260831.md:21-35`).

## 2. Row `(6,4)`, nodal residual class

Here `a=2`, and contact six is a multiple of `a` strictly below the first
characteristic numerator.  The complete delta-sequence census is
`Delta=(6,4,c)`.  Its gcd chain is `6,2,1`; hence `c` is odd,
`2c in <6,4>`, and `c<12`.  Thus

| `c` | `beta_1=18-c` | `delta_inf` | `delta_aff` | infinity cluster | `M_inf` |
|---:|---:|---:|---:|---|---:|
| 11 | 7  | 3 | 7 | `(2^3,1,1)` | 8 |
| 9  | 9  | 4 | 6 | `(2^4,1,1)` | 10 |
| 7  | 11 | 5 | 5 | `(2^5,1,1)` | 12 |
| 5  | 13 | 6 | 4 | `(2^6,1,1)` | 14 |
| 3  | 15 | 7 | 3 | `(2^7,1,1)` | 16 |

This also checks the genus total `10` and every cluster sum directly.  Since
`3d-3=15`, promoted (M-INF) kills the first four nodal configurations.  The
sole numerical threat is `Delta=(6,4,3)`, `beta_1=15`, with three required
nodes.  This is precisely the type for which the reviewed report retracted
the old semigroup argument: its banked witness has an ordinary triple point
and is out of class
(`xmodel/m-inf-hostile-review-sol56-20260831.md:134-168,188-199`).

The infinity type nevertheless **is attained in the nodal class**.  Put

```text
r=t^3+t+1,
q=t^4+(2/3)t^2+(4/3)t,
p=r^2.
```

The exact identity

```text
8r/27 = p^2-q^3-2pq+(2/3)q^2-(16/27)p+(1/9)q-1/9
```

gives `C[p,q]=C[r,q]`; since `gcd(deg r,deg q)=1`, its fraction field is
`C(t)`.  The reduced off-diagonal double-point scheme is especially small.
For `sigma=t+s`, `pi=ts`, divided differences of `r` and `q` give

```text
I_DP=(pi-sigma^2-1, 3sigma^3+4sigma-4).
```

The cubic has nonzero discriminant.  Its three roots give pair discriminant
`-3sigma^2-4`, which cannot vanish on the cubic, and their common images have
`r=-sigma^3/4=(sigma-1)/3`, `q=(sigma^2+1)/3`, so they are distinct.  Also `r'=0`
forces `q'=4/3`, and the two tangent directions at each pair are distinct
(their determinant has nonzero factors `9sigma^2+4` and
`3sigma^2+4`).  Hence the affine curve has exactly three ordinary nodes and
no diagonal or triple fibre.  Consequently `delta_aff=3` and its degree
semigroup, which contains `<3,4>`, is exactly `<3,4>`.  The sextic genus then
forces `delta_inf=7`; with multiplicity two this is `beta_1=15`.  Thus the
banked triple point is a special member, not a forced feature of the
parametrization structure.

The remaining structural tests do not kill this witness type.  Its reduced
shape is `(3,2)`, and the scale inequality only requires
`gcd(deg P,deg Q)>=4`.  For the generic slice, either
`(c(Pi),g_L)=(4,0)` or `(2,1)`.  Here `(g;d',n')=(2;3,2)`, so A'(1)--(4)
give one `P`-conjugacy orbit of block products and `P^2` central in
`<U_1,P>`; the equal-product clause does not apply because `4` does not
divide `6` (`xmodel/pi1s4-close-residual-hostile-review-sol56-20260831.md:53-74`).
At the three nodes the abstract assignments
`{(12),(34)}`, `{(13),(24)}`, `{(14),(23)}` show that the pointwise
disjoint-transposition conditions themselves are compatible with generators
of `S_4`.  This is only a local negative control: no promoted result routes
those labels to an infinity-fixed tuple.

**Verdict: OPEN[PI1S4-(6,4)-FIXED-TUPLE].**  Exactly the nodal
`(beta_1,delta_inf,delta_aff,M_inf)=(15,7,3,16)` configuration survives and
is geometrically attained.  What is missing is the noncoprime infinity-braid
fixed-tuple/route-to-state theorem; the general noncoprime tuple problem is
explicitly retained at
`xmodel/pi1s4-close-residual-hostile-review-sol56-20260831.md:140-159`.

## 3. Row `(6,3)`, tangential configuration `(beta_1,T)=(7,4)`

Here `a=3`, contact six lies strictly below `beta_1`, and the complete
delta sequence for this label is `Delta=(6,3,5)`: its degree-semigroup
conductor is eight, so `delta_aff=4`.  Galindo conversion gives the one-pair
germ `(a;beta_1)=(3;7)`, infinity cluster `(3,3,1,1,1)`,
`delta_inf=6`, and

```text
M_inf=max(6,3+7-1)=9.
```

The totals pass the class filter arithmetically: four delta units can be
carried entirely by double points of two smooth branches.  Since `T` is not
defined in the charged sources, no partition of those units is inferred
from the charged label `T=4`.  The **CONDITIONAL** tangential expression is
`M_inf+2T=17>15`, so (M-INF-T) does not fire in any event.

There is instead an unconditional structural kill.  The approximate root
belonging to the last delta-sequence generator has the form
`r=p-phi(q)` with `deg phi=2` and `deg r=5`.  The triangular target
automorphism `(p,q)->(r,q)` therefore changes the normalized degree pair to
the coprime pair `(5,3)`.  Target isomorphisms preserve the Keller residual,
cover, branch locus, and local monodromy data
(`xmodel/d1-degree-hostile-review-gpt55-20260831.md:44-70`).  The promoted
coprime Main Theorem applies with tangency allowed and forbids precisely the
required transposition-valued `S_4` quotient
(`xmodel/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md:30-47`).

**Verdict: KILLED (triangular reduction to the promoted coprime theorem).**
The conditional M-INF-T statement is not consumed.

## 4. Row `(6,3)`, tangential configuration `(beta_1,T)=(8,3)`

This label has `Delta=(6,3,4)`, one characteristic pair `(3;8)`, infinity
cluster `(3,3,2,1,1)`, and

```text
delta_inf=7,  delta_aff=3,  M_inf=3+8-1=10.
```

Three affine delta units are arithmetically compatible with double points of
smooth branches.  Again no meaning beyond the frozen label is assigned to
`T=3`.  Conditionally, `M_inf+2T=16>15`, so the proposed tangential gate does
not fire.

The last delta generator now gives a triangular approximate root
`r=p-phi(q)` of degree four.  The target-isomorphic parametrization
`(r,q)` has coprime normalized pair `(4,3)`, so the same promoted coprime
Main Theorem, at its tangency-allowed scope, rules out the prescribed `S_4`
representation.  This uses the target-invariance and theorem citations in
section 3, not (M-INF-T).

**Verdict: KILLED (triangular reduction to the promoted coprime theorem).**

## 5. Row `(8,2)`

Here `a=6`, contact eight equals `beta_1`, and `e_1=2`; a second odd
characteristic numerator is required.  The delta-sequence axioms give exactly
`Delta=(8,2,c)` with `c=7,5,3` (the additional value `c=1` has
`delta_aff=0` and is outside the residual).  The complete census is

| `c` | characteristic sequence | infinity cluster | `delta_inf` | `delta_aff` | `M_inf` |
|---:|---|---|---:|---:|---:|
| 7 | `(6;8,9)`  | `(6,2^3,1,1)` | 18 | 3 | 14 |
| 5 | `(6;8,11)` | `(6,2^4,1,1)` | 19 | 2 | 16 |
| 3 | `(6;8,13)` | `(6,2^5,1,1)` | 20 | 1 | 18 |

Indeed `2delta_inf=beta_2+27`, and the table sums to the degree-eight genus
`21`.  In the nodal class the three rows require respectively three, two,
and one ordinary nodes, so no listed configuration is discarded merely for
wrong branch count.  But every cluster sum satisfies
`M_inf<=18<21=3d-3`.  The promoted nodal Nori implication therefore makes
the complement group cyclic in every case.

**Verdict: KILLED (M-INF), for every admissible infinity type.**  This
sharpens the already reviewed row bound
`xmodel/m-inf-hostile-review-sol56-20260831.md:190-203`; no structural
assumption after the gate is consumed.

## 6. Row `(8,4)`

Now `a=4` and contact eight is below `beta_1`.  The delta-sequence axioms
give exactly three families.  Galindo conversion and the Euclidean clusters
give the following complete table (`G=21`):

| `Delta` | characteristic sequence | infinity cluster | `delta_inf` | `delta_aff` | `M_inf` |
|---|---|---|---:|---:|---:|
| `(8,4,7)` | `(4;9)` | `(4^2,1^4)` | 12 | 9 | 12 |
| `(8,4,5)` | `(4;11)` | `(4^2,3,1^3)` | 15 | 6 | 14 |
| `(8,4,3)` | `(4;13)` | `(4^3,1^4)` | 18 | 3 | 16 |
| `(8,4,2,3)` | `(4;14,15)` | `(4^3,2^2,1^2)` | 20 | 1 | 18 |
| `(8,4,6,11)` | `(4;10,11)` | `(4^2,2^2,1^2)` | 14 | 7 | 14 |
| `(8,4,6,9)` | `(4;10,13)` | `(4^2,2^3,1^2)` | 15 | 6 | 16 |
| `(8,4,6,7)` | `(4;10,15)` | `(4^2,2^4,1^2)` | 16 | 5 | 18 |
| `(8,4,6,5)` | `(4;10,17)` | `(4^2,2^5,1^2)` | 17 | 4 | 20 |
| `(8,4,6,3)` | `(4;10,19)` | `(4^2,2^6,1^2)` | 18 | 3 | 22 |

Each `M_inf` is both the displayed cluster sum and
`max(8,4+beta_h-1)`.  The first eight types satisfy
`M_inf<=21=3d-3` and are killed in the nodal class.  Only
`Delta=(8,4,6,3)` fails (M-INF); this is the reviewed numerical threat at
`xmodel/m-inf-hostile-review-sol56-20260831.md:201`.

Its required three-node realization is explicit, rather than merely
numerical.  Starting from the three-node curve in section 2, replace its
degree-six coordinate `p` by `P=p+q^2`.  This is a triangular target
automorphism, preserves every affine singularity and complement datum, and
has degree sequence

```text
(8,4,6,3),  since P-q^2=p has degree 6 and r has degree 3.
```

The conversion gives `(a;beta_1,beta_2)=(4;10,19)` exactly.  Thus this row's
sole infinity survivor is target-isomorphic to the sole survivor of row
`(6,4)`.

The structural filters do not add a kill.  The reduced shape is `(2,1)`;
`g=4` only forces `gcd(deg P,deg Q)>=6`.  The slice possibilities are
`(c(Pi),g_L)=(4,1)` or `(2,2)`.  Since `4|8`, A'(4) says that the two
four-entry block products are a common `c` and `P=c^2`.  Equality does not
control the internal transpositions: for example two four-transposition
blocks with common product one can together contain `(12),(23),(34)` and
generate `S_4`.  The review expressly rejects a universal equal-block kill
and withholds A'(5) (`xmodel/pi1s4-close-residual-hostile-review-sol56-20260831.md:61-74`).
As in section 2, pointwise disjoint labels do not supply the missing global
route to the fixed tuple.

**Verdict: OPEN[PI1S4-(8,4)-FIXED-TUPLE], target-equivalent on the sole
survivor to OPEN[PI1S4-(6,4)-FIXED-TUPLE].**  The exact survivor is
`(Delta;betas;delta_inf,delta_aff;M_inf)=((8,4,6,3);10,19;18,3;22)`,
attained with three ordinary nodes.

## 7. Row `(8,6)`

Here `a=2`, contact eight is below the sole odd `beta_1`, and the complete
census is

```text
Delta=(8,6,c),
c in {23,21,19,17,15,13,11,9,7,3},
beta_1=32-c.
```

The omitted positive odd values one and five are not in `<4,3>`, as required
by `2c in <8,6>`.  For every row the cluster is
`(2^delta_inf,1,1)`, and

| `c` | `beta_1` | `delta_inf` | `delta_aff` | `M_inf` |
|---:|---:|---:|---:|---:|
| 23 | 9  | 4  | 17 | 10 |
| 21 | 11 | 5  | 16 | 12 |
| 19 | 13 | 6  | 15 | 14 |
| 17 | 15 | 7  | 14 | 16 |
| 15 | 17 | 8  | 13 | 18 |
| 13 | 19 | 9  | 12 | 20 |
| 11 | 21 | 10 | 11 | 22 |
| 9  | 23 | 11 | 10 | 24 |
| 7  | 25 | 12 | 9  | 26 |
| 3  | 29 | 14 | 7  | 30 |

Thus (M-INF), whose threshold is `21`, kills the first six types and leaves
exactly the last four.  This agrees with the corrected review: the genuine
largest threat is `beta_1=29`, not 31, and 25, 23, and 21 remain as well
(`xmodel/m-inf-hostile-review-sol56-20260831.md:114-132,170-177`).

For a nodal residual the four survivors would require respectively
`11,10,9,7` distinct ordinary nodes.  The delta sequences are numerically
admissible, but this does **not** prove that an `A^1` normalization realizes
all of those delta units by reduced off-diagonal double fibres.  The charged
review makes exactly this attainment distinction for `(8,6,3)`
(`xmodel/m-inf-hostile-review-sol56-20260831.md:126-132`).  No configuration
is discarded as out of class without such an exclusion theorem.

Structurally, `(d/g,n/g)=(4,3)` is an allowed Chau shape and the scale bound
only says `gcd(deg P,deg Q)>=4`.  The slice alternatives are
`(c(Pi),g_L)=(4,1)` or `(2,2)`.  With `(g;d',n')=(2;4,3)`, A'(1)--(4)
give one conjugacy orbit of four two-entry block products and `P^3` central
in `<U_1,P>`; there is no equal-product conclusion.  Repeated pointwise
disjoint pairs are locally compatible with `S_4`, but the promoted theorem
does not route them into a fixed infinity tuple.

**Verdict: OPEN[ROW-(8,6)-NODAL-REALIZATION+S4-TUPLE].**  The exact
surviving `(beta_1,delta_inf,delta_aff,M_inf)` configurations are
`(21,10,11,22)`, `(23,11,10,24)`, `(25,12,9,26)`, and
`(29,14,7,30)`.  A safe closure needs either an in-class realization
obstruction for each delta sequence or a noncoprime fixed-tuple theorem;
AM admissibility supplies neither.

## 8. Row `(9,3)`

Here `a=6`, contact nine is `beta_1`, and `e_1=3`.  The positive-affine-
delta sequences and their full local data are

| `Delta` | characteristic sequence | infinity cluster | `delta_inf` | `delta_aff` | `M_inf` |
|---|---|---|---:|---:|---:|
| `(9,3,8)` | `(6;9,10)` | `(6,3^2,1^3)` | 21 | 7 | 15 |
| `(9,3,7)` | `(6;9,11)` | `(6,3^2,2,1^2)` | 22 | 6 | 16 |
| `(9,3,5)` | `(6;9,13)` | `(6,3^3,1^3)` | 24 | 4 | 18 |
| `(9,3,4)` | `(6;9,14)` | `(6,3^3,2,1^2)` | 25 | 3 | 19 |
| `(9,3,2)` | `(6;9,16)` | `(6,3^4,1^3)` | 27 | 1 | 21 |

The omitted `Delta=(9,3,1)` has `delta_aff=0`.  Equivalently,
`delta_inf=beta_2+11` and `M_inf=beta_2+5`; every displayed row checks the
degree-nine genus `28`.  A nodal realization would have the displayed number
of nodes, but all cluster sums satisfy `M_inf<=21<24=3d-3`.  Hence the
promoted nodal gate kills every admissible type.

**Verdict: KILLED (M-INF).**  As an independent check, the approximate-root
target shear produces the coprime pairs `(8,3)`, `(7,3)`, `(5,3)`, `(4,3)`,
and `(3,2)`, respectively, so the promoted coprime theorem reaches the same
no-`S_4` conclusion even without nodality.  No off-coprime order restriction
is used.

## 9. Row `(9,6)`

Here `a=3`, contact nine lies below the sole characteristic numerator.  The
complete delta-sequence list is

```text
Delta=(9,6,c),
c in {17,16,14,13,11,10,8,7,5,4,2},
beta_1=27-c.
```

These are exactly `c<18`, `3` not dividing `c`, and `c in <3,2>`.  The
cluster is `M(3,beta_1)`: it is `(3^k,1^3)` for `beta_1=3k+1` and
`(3^k,2,1^2)` for `beta_1=3k+2`.  Hence

| `c` | `beta_1` | `delta_inf` | `delta_aff` | `M_inf` |
|---:|---:|---:|---:|---:|
| 17 | 10 | 9  | 19 | 12 |
| 16 | 11 | 10 | 18 | 13 |
| 14 | 13 | 12 | 16 | 15 |
| 13 | 14 | 13 | 15 | 16 |
| 11 | 16 | 15 | 13 | 18 |
| 10 | 17 | 16 | 12 | 19 |
| 8  | 19 | 18 | 10 | 21 |
| 7  | 20 | 19 | 9  | 22 |
| 5  | 22 | 21 | 7  | 24 |
| 4  | 23 | 22 | 6  | 25 |
| 2  | 25 | 24 | 4  | 27 |

Thus `M_inf<=24=3d-3` kills the first nine nodal types and leaves precisely
the last two.  Their class requirement is strong: `Delta=(9,6,4)` needs six
reduced unordered double fibres and `Delta=(9,6,2)` needs four, with an
immersive parametrization, no parameter reused in a triple fibre, and no
other singularity.  The AM census proves neither that nodal matching scheme
nor its impossibility.

The reduced pair `(3,2)` passes Chau, and `g=3` only imposes
`gcd(deg P,deg Q)>=5`.  Odd-degree slice parity gives
`(c(Pi),g_L)=(3,2)` or `(1,3)`.  Since `(g;d',n')=(3;3,2)`, A'(1)--(4)
give one conjugacy orbit of three block products and `P^2` central in
`<U_1,P>`; `6` does not divide `9`, so equal products are unavailable.
Neither this nor the pointwise disjoint-transposition rule is a contradiction.

**Verdict: OPEN[ROW-(9,6)-NODAL-REALIZATION+S4-TUPLE].**  The exact
survivors are

```text
(Delta;beta_1;delta_inf,delta_aff;M_inf)
=((9,6,4);23;22,6;25),
 ((9,6,2);25;24,4;27).
```

The missing lemma must either exclude/realize the stated nodal matching
schemes or solve the corresponding noncoprime fixed tuples; a semigroup
floor cannot substitute for either.

## 10. Final residual ledger

| row | verdict | exact residue or killing gate |
|---|---|---|
| nodal `(6,4)` | **OPEN** | Sole survivor `Delta=(6,4,3)`, `beta_1=15`, `(delta_inf,delta_aff,M_inf)=(7,3,16)`; explicitly attained by three nodes; missing noncoprime fixed-tuple routing. |
| `(6,3)`--`(7,4)` | **KILLED** | Triangular target reduction to coprime `(5,3)`, then the promoted coprime no-`S_4` theorem. |
| `(6,3)`--`(8,3)` | **KILLED** | Triangular target reduction to coprime `(4,3)`, then the promoted coprime no-`S_4` theorem. |
| nodal `(8,2)` | **KILLED** | Every admissible type has `M_inf<=18<21`; (M-INF). |
| nodal `(8,4)` | **OPEN** | Sole survivor `Delta=(8,4,6,3)`, characteristic `(4;10,19)`, `(18,3,22)`; three-node attained and target-equivalent to the `(6,4)` survivor; same fixed-tuple gap. |
| nodal `(8,6)` | **OPEN** | Four numerical types `(beta_1;delta_inf,delta_aff;M_inf)=(21;10,11;22),(23;11,10;24),(25;12,9;26),(29;14,7;30)`; nodal realization/exclusion and fixed tuple both missing. |
| nodal `(9,3)` | **KILLED** | Every admissible type has `M_inf<=21<24`; (M-INF). |
| nodal `(9,6)` | **OPEN** | Two numerical types `(23;22,6;25)` and `(25;24,4;27)`; nodal realization/exclusion and fixed tuple both missing. |

The two degree-six tangential kills are unconditional and do not consume
(M-INF-T).  All nodal M-INF kills consume the corrected cluster identity and
the reviewed Nori implication at their stated scopes.  The surviving
numerical rows do not consume a converse from AM admissibility, an attainment
claim, A'(5), or the coprime order fork.  The only in-class attainments proved
here are the target-equivalent three-node survivors in rows `(6,4)` and
`(8,4)`; neither is asserted to carry the global residual `S_4`
representation.

Accordingly the sweep closes four of the eight charged rows.  The remaining
topological core is one target-isomorphism class of an explicitly nodal
three-node curve, plus six higher-degree AM-numerical types whose nodal
attainment is itself unresolved.  A safe next lemma must be either a
noncoprime braid fixed-tuple theorem with explicit route-to-node data, or an
exact divided-difference realization obstruction for the six numerical
types.  The promoted sources expressly leave the general noncoprime and
residual-double-point problems open
(`xmodel/pi1s4-close-residual-hostile-review-sol56-20260831.md:140-159`;
`xmodel/m-inf-hostile-review-sol56-20260831.md:205-218`).

<!-- BODY-END -->
