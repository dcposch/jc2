# Rank-four `R4-CYCLE-1`: pseudo-plane and companion-divisor threat map

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`rank4_cycle_m1` lane)  
Frozen basis: `4393243bccdbe1a32d80fe8c770c2c8b909f4c01`  
Lifecycle: **FINAL+VERIFIED EXACT FUNNEL / THREE PROPOSED SHORTCUTS BLOCKED / HORN OPEN**

## 0. Verdict

Charge the exact connected rank-four row

```text
A2 --g1--> Y --pi=g2--> A2,          deg(pi)=4,
R=NonEt_Y(pi)_red,                   U=Y-R,
h=k=1, beta1(B)=n22=1, n4=0,
|T31|=1,                             (C,Q)=(A1,0).
```

The row does not yet contradict the proper-block package.  It does, however,
collapse to a much sharper global object.

1. The ruling `rho:U->A1` has exactly one multiple fibre
   `mu*Phi`, with `mu>=2`.  Moreover

   ```text
   Pic(U)=Z/mu<[Phi]>,       H_i(U;Q)=0 for i>0,
   U-g1(A2) is finite,       mu divides d1,
   K_U~0.                                                   (0.1)
   ```

   Thus every survivor is a unique-multiple-fibre affine pseudo-plane in the
   general, untyped sense.  The no-multiple row would make `U=A2` and turn
   `pi|U` into a degree-four polynomial Keller map, contradicting the
   promoted topological-degree-at-most-five theorem.

2. The unramified companion curve

   ```text
   T=U times_(A2) B -> B
   ```

   is etale, reduced, and an effective principal Cartier divisor of `U`.
   Its geometric fibre counts are exactly

   ```text
   2 on T211,       1 at the unique T31 point c,
   0 at the unique S22 point n.
   ```

   Since `e(B)=0`, this gives

   ```text
   e(T)=-3,        e(U-T)=4.                               (0.2)
   ```

   The complement is the connected finite-etale `S4` cover of degree four
   over `A2-B`.  Also

   ```text
   pi(U)=A2-{n}.                                           (0.3)
   ```

3. The Picard/different data are consistent, not contradictory.  For each
   irreducible target component `B_i`, with generic ramification prime `R_i`
   and total unramified companion closure `S_i` in `Y`,

   ```text
   div_Y(pi^*b_i)=2R_i+S_i,
   [S_i]=-2[R_i] in Cl(Y).                                (0.4)
   ```

   The classes `[R_i]` are freely independent, while
   `Cl(Y)/<[R_i]> isomorphic to Pic(U)=Z/mu`.  Hence `S_i` is nonprincipal on `Y` even
   though `T_i=S_i intersect U` is principal on `U`.  This is the exact
   localization obstruction that any proposed "principal companion" proof
   must overcome.

4. The cusp overlap and node pairing do not choose that missing
   trivialization.  At permutation level one cusp packet plus one node packet
   generates `S4`, but every conjugacy transport between two transposition
   inertias has four choices, two of each companion-pair parity.  Local
   permutation labels therefore determine neither a companion determinant
   character nor a scalar gluing of the different line.

5. The cusp and node do not by themselves force an extra bad ruling fibre.
   The ruling and `pi` are unrelated morphisms.  A principal cusp-node curve
   already coexists with a componentwise-irreducible `A1`-ruling on `A2`;
   Section 6 gives the exact control.  A contradiction requires a new theorem
   coupling `rho` to `pi`, not only the existence of the curve `T`.

The sharp remaining target is therefore a **pseudo-plane-to-plane gate**:
exclude an etale quasi-finite rank-four map satisfying (0.2)--(0.4), or prove
that the actual first leg forces the companion closure to extend
principally.  Neither conclusion follows from the present local packets.

## 1. Frozen inputs

```text
cf157e17db8179b590f15808aab84447717df343735416578e005a2085d73d4e
  xmodel/block-descent-a1-quartic-minimal-cycle-nodal-control-threat-map-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
2e6d82035df6717d1a39f31dc19b23b7c727bb940d4730d2c7ea9400e5433cce
  xmodel/block-descent-a1-cubic-affine-survivor-funnel-sol56-20260830.md
9e32b0fe8835b6ea6002036b95e2261a612754d73d796cb10edda347cf3cf65e
  xmodel/block-descent-a1-cubic-affine-survivor-funnel-hostile-review-gpt55-20260830.md
38baa55d6e2d54bf3fa5329e1623d983b4e6ac6eaddf7fd7dbb60b2cd1675578
  ladder/SHEET6.md
88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad
  refs/zoladek2008_official.pdf
0b01b3901363097e25e03fe67d0644c287ee3ef1701acd4e9ee1e166da05ca54
  ops/block_descent_a1_quartic_cycle1_pseudoplane_replay.py
```

The pseudo-plane argument below is the degree-four reuse of the already
different-model-reviewed general surface lemmas in the cubic funnel.  Its
only degree-specific replacement is the no-multiple endpoint: degree four is
excluded by the stronger promoted `td<=5` theorem rather than Orevkov's
degree-three theorem.

Use `mu` for the multiplicity of the ruling fibre.  This avoids confusing it
with the charged symbol `m=|T31|=1` in the preceding threat map.

## 2. The ruling forces one multiple fibre

The charged Euler equality gives

```text
e(U)=2-|T31|=1=e(A1)+Q,
```

so `C=A1`, `Q=0`, and every reduced ruling fibre is one affine line.  The
composite

```text
h=rho o g1:A2->A1
```

is a nonconstant polynomial.  Restriction to a general affine source line
gives a transverse nonconstant morphism `A1->U`.  Miyanishi Lemma 1.4.16,
with the hypotheses checked in the reviewed cubic funnel, then permits at
most one multiple ruling fibre.

Suppose there is none.  Equidimensionality makes `rho` flat; all its scheme
fibres are smooth affine lines, so `rho` is a smooth `A1`-bundle.  Over
`A1`, both the line-bundle class and the additive torsor class vanish.  Hence

```text
U isomorphic to A2.                                      (2.1)
```

Under (2.1), `pi|U` is a regular etale map between affine planes and is
therefore a polynomial Keller map.  Its function-field degree is still four,
because `U` is dense in `Y`.  The promoted theorem that every plane Keller
map of topological degree at most five is invertible contradicts this degree.
Thus the no-multiple row is empty.

Let the unique multiple fibre be `mu*Phi`, `mu>=2`.  Miyanishi's general
irreducible-fibre Picard lemma gives

```text
Pic(U)=Z/mu<[Phi]>,       H_i(U;Q)=0 for i>0.           (2.2)
```

Put `V=g1(A2)`.  If a nonzero divisor supported in `U-V` were principal,
both its defining rational function and its inverse would be regular on
`V`; their pullbacks would be inverse polynomials on `A2`, hence scalars.
Dominance would make the original function scalar.  Thus the free group on
missed prime divisors injects into the finite group (2.2).  There are no
missed prime divisors, and

```text
U-V is finite.                                           (2.3)
```

Choose a ruling coordinate `t` with
`div_U(t-a)=mu*Phi`.  Etaleness makes `g1^*Phi` reduced.  Factoriality of
`C[x,y]` gives

```text
g1^*(t-a)=c P^mu,       c in C*.                        (2.4)
```

The exact order `mu` of `[Phi]` makes
`X^mu-(t-a)/c` irreducible over `C(U)`, by the standard Kummer binomial
criterion exactly as reconstructed in the reviewed cubic funnel.  It embeds
a degree-`mu` subfield in `C(x,y)`, so

```text
mu divides d1.                                          (2.5)
```

Finally `pi|U` is etale, and hence

```text
omega_U=pi^*omega_A2=O_U.                               (2.6)
```

Condition (2.6) does **not** eliminate the multiple fibre.  Arbitrary affine
pseudo-planes are not covered by the special typed `(d,n,r)` canonical-class
formula; the reviewed cubic funnel already quarantines that false upgrade.

## 3. The exact companion divisor

Let

```text
T=U times_(A2) B.
```

Base change of the etale morphism `pi|U` makes `T->B` etale.  It need not be
finite.  The rank-four fibre census gives the geometric fibre cardinality

```text
u_T(z)=2,  z in T211;
u_T(c)=1,  c the unique T31 value;
u_T(n)=0,  n the unique S22 value.                       (3.1)
```

The points `c` and `n` are distinct because their fibre partitions differ.
Since `e(B)=h-n22=0`, constructible Fubini gives

```text
e(T)=2e(B-{c,n})+1=2(0-2)+1=-3.                        (3.2)
```

If `b=product_i b_i` is a reduced equation for `B`, etale pullback makes

```text
T=div_U(pi^*b)                                          (3.3)
```

a reduced effective principal Cartier divisor.  This is a statement on
`U`, not on `Y`.

Removing `T` removes every point over the target branch:

```text
W=U-T=Y-pi^(-1)(B).
```

Thus `W->A2-B` is connected, finite etale, and degree four.  Its monodromy
is the charged full `S4`.  The two Euler calculations agree:

```text
e(W)=4e(A2-B)=4(1-e(B))=4,
e(W)=e(U)-e(T)=1-(-3)=4.                               (3.4)
```

Equation (3.1) also gives the exact second-leg image

```text
pi(U)=A2-{n}.                                           (3.5)
```

This is strong but not a purity contradiction: `pi|U` is not finite, and
its fibre cardinality drops along `B` as missing sheets run into `R`.

## 4. Localization explains the class and different

Write `B=union_i B_i`, with irreducible equation `b_i`.  The generic fibre
over `B_i` is `(2,1,1)`.  There is one ramification prime `R_i` of index two;
let `S_i` be the sum, with coefficient one, of the unramified height-one
primes above `B_i`.  The height-one pullback formula is

```text
div_Y(pi^*b_i)=2R_i+S_i.                                (4.1)
```

Residue degree two versus two residue-degree-one companion primes does not
change (4.1): divisor coefficients are ramification indices.

Every `R_i` is missed by `g1`.  The promoted boundary-class theorem gives an
injection

```text
direct_sum_i Z[R_i] -> Cl(Y).                           (4.2)
```

Since `U=Y-union_i R_i`, normal localization and (2.2) give

```text
Cl(Y)/<[R_i]> isomorphic to Pic(U)=Z/mu.                (4.3)
```

Taking classes in (4.1),

```text
[S_i]=-2[R_i].                                          (4.4)
```

Consequently each `S_i` is nonprincipal on `Y`, while its restriction
`T_i=S_i intersect U` is principal by (3.3), componentwise.  The codimension-
one different is

```text
D_(Y/A2)=sum_i R_i,                                     (4.5)
```

because the generic tame ramification indices are two.  Equations
(4.2)--(4.5) make its nonprincipality transparent.

This is not an unresolved sign issue.  It is a consistent class lattice:
the cusp and node are codimension-two specializations and alter none of the
coefficients in (4.1) or (4.5).  To get a contradiction one must prove new
global information, such as `S_i` principal already on `Y`.  Principality
only after deleting `R_i` is exactly what localization predicts.

The condition `O(U)^*=C^*` is load-bearing in (4.2), but it points in the
opposite direction from the naive shortcut: it proves that the boundary
class cannot be killed by a rational function supported on `R`.

## 5. Cusp transport does not choose a boundary character

At the unique cusp, two overlapping transpositions satisfy the braid
relation and generate an `S3` on three sheets.  At the node, two disjoint
transpositions commute.  The concrete labelled packet

```text
tau=(12),       upsilon=(23),       sigma=(34)
```

has

```text
<tau,upsilon>=S3,       <tau,upsilon,sigma>=S4.         (5.1)
```

Thus the local packet is group-theoretically feasible.

There is also an exact ambiguity that blocks the proposed character
shortcut.  For any transpositions `a,b in S4`,

```text
{g in S4 : g a g^-1=b}
```

has four elements.  Each maps the two fixed sheets of `a` to the two fixed
sheets of `b`; after either ordering is chosen, two preserve and two reverse
the companion-pair ordering.  This is simply the order-four centralizer of a
transposition, and the replay checks all 36 ordered pairs.

Therefore local inertia labels plus conjugacy transport do not determine a
`Z/2` companion character.  Still less do they determine a scalar
trivialization of the rank-one reflexive different module.  A permutation
identification of sheets is not a rational section of `O_Y(D)`.

The unique target cycle is precisely where unrecorded gluing can live.  A
proof may eventually calculate it from a based infinity relation or from a
global quartic algebra, but it cannot be read from the cusp braid and node
matching alone.

## 6. A bad ruling fibre is not forced formally

Consider the irreducible plane curve

```text
Gamma: y^2=x^3(x-1)^2,
(x,y)=(t^2,t^3(t^2-1)).                                 (6.1)
```

The derivative vanishes simultaneously only at `t=0`, with orders `(2,3)`,
so the origin is an ordinary cusp.  The only distinct normalization
collision is `t=1` with `t=-1`; the tangent determinant there is eight, so
the image `(1,0)` is an ordinary node.  Hence

```text
e(Gamma)=e(A1)-1=0.                                     (6.2)
```

On `A2_(x,y)`, take the unrelated ruling `rho=x`.  Every ruling fibre is one
reduced `A1`, so `Q=0`; also `O(A2)^*=C^*`, `K_A2=0`, and `Gamma` is
principal.  Thus a principal curve with exactly the charged cusp-node
topology does not force a reducible ruling fibre.

This is a firewall, not a block control: it has no unique multiple fibre,
quartic finite-flat cover, nonprincipal different, or first leg.  Its exact
role is to show that any implication

```text
cusp/node on T  =>  Q>0
```

must consume a proved relation between `rho` and `pi`; surface, unit, and
curve data alone do not supply one.

## 7. What the actual first leg adds, and what it does not

By (2.3), `g1(A2)=U-E` for a finite set `E`.  Combining this with (3.5),

```text
A2-F(A2) is finite and contains n.                       (7.1)
```

This is not exceptional enough to close the row.  A Keller map cannot omit
an entire target divisor in the first place: the defining polynomial of
such a divisor would pull back to a nowhere-zero polynomial, hence a scalar.
Thus cofinite image is compatible with the general Keller setup.

Pulling back (3.3) gives the reduced principal plane curve

```text
g1^*T=V(b(F)) subset A2.                                (7.2)
```

The node `n` has no preimage.  The unique companion point over the cusp is
either one of the finitely many points in `E`, or every source point above it
has the same cusp germ because `F` is etale.  Both alternatives are presently
consistent.

Strong Zariski Main does not repair this.  In the finite normalization of
`U` inside `C(x,y)`, boundary divisors can dominate a divisor of `U` which is
simultaneously reached by another open sheet.  The reviewed pseudo-plane
cyclic-cover control does exactly this over the multiple fibre.  Therefore
cofiniteness of `U-g1(A2)` does not make `g1` finite and does not turn (7.1)
into a Hartogs contradiction.

The genuinely new first-leg datum still available for a successor is the
simultaneous polynomial pair

```text
rho o g1=P^mu up to an affine scalar,        b o F,      (7.3)
```

with the latter having one omitted node and the companion/cusp census of
Section 3.  No current theorem couples the two polynomials in (7.3).

## 8. Maximum-safe conclusion and next gate

Promote exactly the following conditional statement.

> **`R4-CYCLE-1` pseudo-plane funnel.**  Every actual proper rank-four block
> in the connected minimal-cycle row with exactly one `(3,1)` value is a
> unique-multiple-fibre affine pseudo-plane satisfying (0.1).  Its companion
> curve is a reduced principal Cartier divisor of Euler number `-3`; its
> complement is the connected degree-four `S4` cover of `A2-B`; and
> `pi(U)=A2-{n}`.  On the full normal surface, the companion closures satisfy
> `[S_i]=-2[R_i]`, so they are nonprincipal even though their restrictions to
> `U` are principal.

Do not promote an exclusion of `R4-CYCLE-1`, a principal different, a forced
extra ruling component, a finite first leg, or a companion-character
identity.

The cheapest decisive successors are, in order:

1. **`R4-CYCLE-1-FUNCTION-PAIR`.**  Use the actual polynomial pair (7.3),
   retaining the omitted node and cusp preimage alternative, to force a
   second multiple/reducible ruling fibre or a forbidden polynomial-fibre
   Euler relation.
2. **`R4-CYCLE-1-EXTENSION`.**  Prove from the global quartic algebra that
   some `T_i` defining section has zero valuation along `R_i`.  Then it would
   make `S_i` principal on `Y`, contradicting (4.2)--(4.4).  Local
   cusp/node packets are insufficient; an infinity or norm relation is
   required.
3. **`R4-CYCLE-1-PSEUDOPLANE-MAP`.**  Classify etale quasi-finite degree-four
   maps from a `K`-trivial unique-multiple-fibre pseudo-plane to `A2` with
   image `A2-{n}` and companion Euler number `-3`.

The missing inputs are theorem-level global relations, not large
eliminations.  No AWS computation is justified by this packet.

## 9. Desk verification and firewalls

The deterministic replay is

```text
0b01b3901363097e25e03fe67d0644c287ee3ef1701acd4e9ee1e166da05ca54
  ops/block_descent_a1_quartic_cycle1_pseudoplane_replay.py
```

Ordinary, `python3 -O`, and `python3 -OO` executions are byte-identical:

```text
stdout SHA-256:
f239c255f72d02ca28c57b918b443c1d8638beb790acb467ecbb726b85c88da9

status=PASS-QUARTIC-CYCLE1-PSEUDOPLANE-THREAT-MAP
payload_sha256=328df8df376dc974bd9aa5a672f3f8f6e64f35de9cf95163aabf6b737e0b6473
```

It checks the cusp `S3`, the cusp-plus-node `S4`, all 36 ordered
transposition transporter sets and their `2+2` companion-parity split, the
two Euler calculations, an abstract free-boundary/torsion-quotient class
model, and the explicit cusp-node curve (6.1).  The mutation
`--mutate-force-companion-parity` is rejected.

The replay does not encode the proper-block sandwich, the ruling theorem,
Miyanishi's multiple-fibre/Picard lemmas, the low-degree Keller theorem,
normal localization, the relative different, finite flatness, existence of
an actual quartic cover, or JC2.

Nothing here treats `R4-CYCLE-0`, disconnected rank-four branch, block degree
at least five, the primitive/no-block horn, constructs a counterexample, or
proves JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18090`.
- Body SHA-256:
  `c21f168a64e9c30452f49b1e820d21d57bdb03718cbd4bb580431a46538cad2a`.
- Frozen basis: `4393243bccdbe1a32d80fe8c770c2c8b909f4c01`.
