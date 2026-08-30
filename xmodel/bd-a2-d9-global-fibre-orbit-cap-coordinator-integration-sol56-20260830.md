# Binding integration: global `D9` fibre signatures and shared cap ledger

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen integration basis: `7e72f3422017511b400003733807c52d4fbf267a`  
Lifecycle: **BINDING COMBINATORIAL INTEGRATION / EFFECTIVITY OPEN**

## 0. Evidence, review, and exact scope

This integration binds the transactional producer

```text
9a02c626267b1cd9fa31d241119f096d0915afa5f418a592589a6bdf68d9b037
  xmodel/bd-a2-d9-global-fibre-orbit-cap-ledger-sol56-20260830.md
  body 26016 / 08484e2866fffda5ce9d2fd109f04e2f05dee3d1f4958ea28d4a08b69e8563ca
  manifest 71bc7064fee68941b63b174fa723a22d05c9ca5f03c973b83dbf75cd34443bd2
```

to the independent GPT-5.5 xhigh hostile review

```text
2eea6b7a1134f95ca927e2f93a5fbaa99a0525b49d83b750f9b8fac71f073074
  xmodel/bd-a2-d9-global-fibre-orbit-cap-ledger-hostile-review-gpt55-20260830.md
  body 16223 / cc578954a1e49fc5f7b1a32d5af5974107f31bbc4260414265286ddb20e6edcc
  receipt bcdeb64ca231b80c15ae9242035d9af8d2643ba620fdcb33be23af06fd4706cf
  verdict CONFIRM_WITH_CORRECTIONS
```

The review independently rebuilt the signed-support classification, ruled
fibre normal form, orbit and stabilizer argument, generating functions,
replay output, every JSON record, total-transform identities, shared cap
ownership, and reduced-infinity genus filter.  It found no mathematical gap.
The corrections below make the subsystem convention, abstract-versus-
effective boundary, and exceptional-versus-total genus contribution exact.

The charged geometric basis is the promoted normal class-`2A+3B` incidence
resolution with its ruled nine-blowup marking and exact
`D9(-1)=(ZA+ZB)^perp`.  This packet classifies abstract unmarked weighted
vertical blowup forests and supplies conditional numerical constraints.  It
does not classify marked blowup configurations, carrier classes, target
images, analytic incidences, or maps.

## 1. Exact signed-support classification

Use signed coordinates

```text
R(D9)={+-e_i+-e_j : i!=j}.
```

For one connected used coordinate support of size `s`, switching signs along
a spanning tree makes the tree roots differences.  A balanced signed support
generates

```text
B_s=A_(s-1),
```

while one unbalanced cycle supplies a sum root and reflection closure gives

```text
U_s=D_s.
```

Here `U_2=D_2=A1+A1` is disconnected as a root system, and
`U_3=D_3=A3`.  There is no third connected signed-support closure.  A global
signature is therefore

```text
sigma=(u; b_2,...,b_9; d_2,...,d_9),
u+sum_(s=2)^9 s(b_s+d_s)=9,                           (1.1)
```

where `u` counts unused coordinates, `b_s` counts balanced blocks, and `d_s`
counts unbalanced blocks.

The convention in (1.1) is **reflection-closed signed-support subsystem**.
It is not the stronger saturation convention
`R(D9) cap span_Q(Phi)`.  Under (1.1), the used-support generating series is

```text
product_(s=2)^9 (1-x^s)^(-2),
```

with coefficient histogram

```text
[1,0,2,2,5,6,13,16,30,40]
```

before the unused-coordinate factor.  Multiplying by `(1-x)^(-1)`, the
degree-nine coefficient is exactly

```text
115 = 1 zero + 15 connected nonzero + 99 disconnected. (1.2)
```

The index-two passage from the full signed permutation group to `W(D9)`
does not split any of these orbits.  Every stabilizer contains an odd signed
element: an unused-coordinate flip, a flip inside an unbalanced block, or,
when all coordinates are covered by balanced blocks, the flip of an
odd-sized balanced block.  The exhaustive case split is `75+32+8=115`.

For the optional saturated-span diagnostic, at most one unbalanced block is
allowed.  Its count is `75`, of which `59` are disconnected.  This diagnostic
is useful but is not substituted for the 115-signature theorem.

## 2. Geometric vertical-fibre normal form

Let `C` be a final smooth rational component in a fibre of the resolved conic
fibration.  With `K=-A+B` and `B.C=0`, adjunction gives

```text
A.C=C^2+2.
```

Nefness of `A` therefore forces `C^2>=-2`.  Since an original fibre starts
with square zero and every blowup exceptional starts with square `-1`, no
component already at square `-2` can be blown up again.  The final affected
fibre has only `-1` and `-2` components.

There are exactly two weighted block forms:

```text
B_s: (-1)-(-2)-...-(-2)-(-1),
     beta=(1,...,1), root graph A_(s-1);

U_2: two beta-one (-2) leaves joined through one beta-two (-1),
     root graph A1+A1;

U_s, s>=3: two beta-one short leaves and a beta-two fork/long arm,
     root graph A3 for s=3 and D_s for s>=4.
```

`B_s` comes from terminal smooth blowups.  The sole node blowup can occur only
as the second blowup of a fresh fibre, producing `U_s`; any later node blowup
would touch a `-2` component.  For every block the full fibre matrix satisfies

```text
Q beta=0,       gcd(beta)=1,
sum_(C^2=-1) beta_C=2.                                (2.1)
```

Thus no missed multiple-fibre or proximity type occurs in the charged ruled
marking.  Under projective finiteness, every final vertical `-2` component is
exactly a Du Val exceptional component: `A.C=0` contracts its target image,
and a finite map cannot send a nonexceptional source curve to a point.
Without projective finiteness, extra `A`-null nonexceptional curves remain
possible and this converse is unavailable.

Equations (1.1)--(2.1) give a bijection only between the 115 signatures and
**abstract unmarked weighted blowup-forest block multisets**.  Marking the
original fibre component gives `floor(s/2)+1` species for `B_s` and one for
`U_s`, hence generating function

```text
(1-x)^(-1) product_(s=2)^9
  (1-x^s)^(-(floor(s/2)+2)),
```

whose degree-nine coefficient is `362`.  Neither number counts effective
marked configurations or incidence moduli.

## 3. Reproducible finite data

The standard-library replay

```text
38d0d6cd6af0e76d0bddf30018effb3c3a2c8a4ebb511945fa771f3c888b166b
  ops/d9_fibre_signature_enumerate.py
```

emits the canonical JSON

```text
88d30955fc6017770fe02cb381ab25cbcd2ce8263f7403864e8c2dc862530d96
  xmodel/bd-a2-d9-fibre-signatures-sol56-20260830.json.
```

Root and reviewer independently regenerated byte-identical output.  The
reviewer also checked all 17 block records and all 115 signature records,
including `U_2` as one physical fibre but two root components.  The script's
allowed-self-intersection assertion is only a replay consistency check;
adjunction and nefness in Section 2 are the geometric proof.

## 4. Exact total-transform identity and cap ownership

Over one ADE tree use `E_i.E_j=-C_ij` and write

```text
r^*D=D'+xE,          r^*G=G'+yE.
```

Orthogonality gives `D'.E=Cx` and `G'.E=Cy`; expanding all three exceptional
cross terms leaves exactly one copy:

```text
D.G=D'.G'+x^t C y.                                  (4.1)
```

Nonnegativity of the strict residual intersection yields a cap only when the
two named divisors share no strict carrier.  The binding ownership rules are:

1. `A.R=8` and `A.H=3` are shared per target image; singular points over the
   same target point consume one budget.
2. `B.R=4` and `B.H=2` are shared per actual source fibre with its exact
   `beta` weights.  The two `A1` trees inside one `U_2` block do not get two
   independent fibre budgets.
3. `H.R=8` is one global fixed-infinity budget with contribution `h^t n`.
4. `n=Cm` is the ramification vector and `a=Ch` is the infinity vector; they
   remain distinct in every contraction.
5. A common strict carrier suppresses the cap.  Its residual formula contains
   a self-intersection term and is a separate geometric stratum, not an
   uncapped instance of the finite table.

When `pi:X->P2` is projectively finite, normality and Cohen--Macaulayness make
the degree-three map finite flat.  Each target fibre then has length three and
at most three source points.  Generic finiteness alone does not license this
bound.

## 5. Reduced-infinity genus filter

For reduced connected `H` of bidegree `(2,3)`, `p_a(H)=2`.  At one Du Val
point write

```text
r^*H=H'+sum h_iE_i,          a=Ch.
```

Crepancy and orthogonality give the exact **exceptional contribution**

```text
p_a(r^*H)-p_a(H')=h^t a/2.                           (5.1)
```

The full local delta is

```text
delta_p(H)=h^t a/2 + sum_(q over p) delta_q(H'),      (5.2)
```

so (5.1) is the whole local delta only if the lifted strict transform has no
remaining singularity.  Every physical branch meets the exceptional set,
but one branch can meet an exceptional node; therefore

```text
r_p(H)<=sum_i a_i.                                   (5.3)
```

The normalization graph and `p_a(H)=2` yield the global defect cap

```text
sum_p max(0, h_p^t a_p/2-sum_i a_(p,i)+1) <=2.       (5.4)
```

In particular `h^t a<=2(sum a_i+1)` locally.  In a proper no-common-carrier
`B/H` stratum, `sum a_i<=beta^t a<=2`, hence `h^t a<=6`; a row with
`h^t a=8` dies there, while a row with value six and `sum a=2` consumes the
entire genus-two defect budget.  These deductions do not apply on an actual
common fibre carrier.

## 6. Promotion boundary and next gate

Promoted:

```text
115 unmarked reflection-closed signed-support signatures;
75 under the separate saturated-span diagnostic;
362 marked-original abstract fibre species;
exact B_s/U_s weighted vertical blowup forests;
conditional shared target/fibre/infinity caps;
exact reduced-H exceptional genus and global defect filters.
```

Not promoted: simultaneous marked effectivity; blowup locations; target-image
partitions; physical contact atoms; strict ramification or F5 carrier classes;
analytic incidence realization; a finite algebra; an etale first leg; a
polynomial map; a counterexample; or JC2.

The exact successor is a carrier-labelled decoration problem.  Expand a
signature to physical ADE points, preserve `U_2` as two trees in one actual
fibre, partition source points by target image, attach `(m,n,h,a)`, allocate
only licensed shared budgets, and then add physical contact atoms and strict
carrier labels modulo the stabilizer of the marked fibre representative.
Only after that finite necessary-data layer should ruled-class effectivity and
analytic realization be tested.  The now-reviewed F5 bridge supplies the
unique infinity carrier pattern for the reduced finite normal-singular cell;
it is bound in its own integration rather than silently imported here.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10341`.
- Body SHA-256:
  `67ada59969c8208fff3a6b476fbbbd4d1317319fa3521904748ddd8010aef5c4`.
- Frozen basis: `7e72f3422017511b400003733807c52d4fbf267a`.
