# Hostile review of Grok46 `FACE-NC` and `FACE-CHAR`

**Reviewer:** Sol Ultra  
**Round:** `20260827T2137Z` post-seal cross-review  
**Scope:** Grok46 sections 3.1, 3.2, Cards A/B, and their dependencies only

## Custody

The SHA-256 of
`xmodel/ideation-20260827T2137Z-grok46.md` was recomputed as

```text
bfd18a275165e1740f883222c1a6e0f8b43cb5e2737d18b8eea01b9c2615d57e
```

and matches the assigned seal.  This review also uses
`xmodel/ideation-20260827T2137Z-postseal-truth-delta.md` and, solely to type
the passport base correctly, its named finite-end source
`xmodel/g2-finite-end-asymptotic-monodromy-connection-sol-ultra-20260827.md`.
No blind-round custody is altered.

## Verdict

Both proposed promotions fail in their present form.

| Proposal | Verdict | Decisive defect |
|---|---|---|
| `FACE-NC` | **TYPE-FAIL / SPLIT** | Nearby cycles of the zero-locus family are supported on `Z(H)`, not on `U=A^1\setminus Z(H)`.  The proposed live truncation is locally the constant divisor `H=0`.  Moreover, distinct `mu_4` eigenspaces such as rows 23 and 24 split canonically; nearby-cycle nilpotent extensions cannot cross those eigenvalues. |
| `FACE-CHAR` | **NOT TYPED** | The face character and Keller passport are representations of fundamental groups of different bases.  No map of bases, map of loops, or character factorization is supplied.  A local `-1` eigenvalue also does not by itself say that the total permutation is odd. |

The narrow salvage is rank one: the Kummer interpretation of `nabla_m`, its
local character calculation, and an exact chain-map relation between
`T_A` and `nabla_23`.  There is no exhibited rank-two client and currently no
passport cut.

## 1. `FACE-NC`: nearby cycles do not give the claimed SES on `U`

### 1.1 The support/base mismatch is fatal

Let

```text
Y = {(X,t) : F(X,t)=0} subset A^1_X times Delta_t,
p:Y -> Delta_t,
Y_0=Z(H),
j:U=A^1_X minus Z(H) -> A^1_X.
```

For the ordinary meaning of “nearby cycles of the fibres
`F(\cdot,t)=0`,” `R psi_p` is an object on `Y_0`.  After closed pushforward to
`A^1_X`, it is supported on `Z(H)`, so

```text
j^* R psi_p = 0.
```

It therefore cannot be a nonzero extension of the two rank-one connections
`nabla_m` and `nabla_{m+1}`, both of which are local systems on `U`.

The alternative literal reading does not help.  Applying nearby cycles for
the projection `A^1_X times Delta_t -> Delta_t` to the constant sheaf on the
ambient product gives the constant sheaf on `A^1_X`; it is independent of
`F` and contains no `nabla_m`.  Passing instead to cohomology of complements
`A^1_X\setminus Z(F_t)` would produce a family over the **parameter base**
`Delta_t`, not a short exact sequence of connections on the **spatial base**
`U`.  A further Gauss--Manin or direct-image construction would have to be
specified and typed from scratch.

Thus the phrase “nearby-cycles exact sequence ... of constructible sheaves /
connections on `U`” conflates three different categories and two different
bases.

### 1.2 Nearby cycles do not automatically furnish a short exact sequence

The canonical nearby/vanishing-cycle formalism supplies distinguished
triangles and the `can`/`var` maps.  A short exact sequence requires a chosen
t-structure, concentration in the required perverse degrees, and an actual
two-step filtration.  None is supplied.  Nor is there any reason that:

```text
GGV row number = monodromy eigencharacter = monodromy-weight index.
```

These are separate gradings.  Monodromy weight pieces arise only after more
structure and the nilpotent logarithm; they are not “consecutive row
connections” by nomenclature.

### 1.3 The proposed live family is locally trivial

Card A asks for the nearby-cycle sequence of

```text
F = H + t F_1,       F_1=H V.
```

But exactly

```text
F = H(1+tV).
```

The factor `1+tV` is a unit in every formal neighbourhood of `t=0` and in
particular near every point of `Z(H)`.  Hence the zero-locus germ is just
`H=0` times the parameter disc.  Its vanishing cycles are zero and its nearby
cycles are the constant specialization supported at `Z(H)`.  For the live
`V=1` fixture this is even globally `F=(1+t)H` near `t=0`.

Terms of order `t^2` could change the full family, because the displayed
reduced-cascade `F_2` contains a `V^2/4` term.  But then Card A's object is not
`H+tF_1`; the complete flat family, its sheaf or D-module, and its functorial
relation to the row system must be stated.  First-order divisibility by `H`
cannot certify a nonsplit extension.

This factorization is the cheapest exact discriminator proposed by the card,
and it already returns **FAIL** without any nearby-cycle computation.

### 1.4 `mu_4` semisimplicity forbids the advertised nonsplit pair

The valid source of the face character is the Kummer cover

```text
pi: {y^4=H(X)} -> U.
```

On this cover, a horizontal solution of

```text
nabla_m = d + (m/4)dH/H
```

is `y^{-m}`.  Thus `nabla_m` is a deck-character eigensummand of
`pi_* C`, with character determined by `m mod 4`.  In characteristic zero,
`mu_4` is linearly reductive.  The four idempotents

```text
e_k = (1/4) sum_{zeta in mu_4} zeta^{-k}[zeta]
```

split every equivariant local system into its eigensummands.

Rows 23 and 24 have distinct deck characters (`23 == 3 mod 4`,
`24 == 0 mod 4`).  Consequently every `mu_4`-equivariant sequence

```text
0 -> nabla_23 -> E -> nabla_24 -> 0
```

splits by the idempotents.  The same conclusion holds if the `mu_4`
grading is presented as the finite-order semisimple part of nearby-cycle
monodromy: generalized eigenspaces for distinct eigenvalues split
canonically.  The nilpotent logarithm `N` acts within one generalized
eigenspace, not between the `m=23` and `m=24` eigenvalues.

There is therefore a clean disjunction:

1. retain the claimed Kummer/nearby-cycle eigenspace provenance, in which
   case the consecutive-character extension splits; or
2. discard equivariance and write an explicit off-diagonal connection form,
   in which case the face-eigenline story no longer constructs the
   extension.

Abstract nonequivariant extensions are not the issue.  Indeed their classes
would lie in

```text
Ext^1(nabla_24,nabla_23)
  = H^1(U, Hom(nabla_24,nabla_23)),
```

and for the four-root fixture the relevant difference character again has
nontrivial local monodromy and a three-dimensional `H^1`.  Choosing an
arbitrary class there would make a rank-two connection, but it would not show
that a GGV unfolding or row recursion supplies that class.

The only same-character location where a nearby-cycle nilpotent extension is
not excluded on semisimplicity grounds is between indices congruent modulo
4, for example `m` and `m+4`.  Those connections are already gauge-isomorphic
on `U`, and support plus construction still remain unresolved.  This does not
rescue the proposed consecutive `(23,24)` client.

### 1.5 The numerical `3=3` match is not an SES

For `H=A^2`, `A=X^4-1`, the calculations

```text
dim H^1(U,nabla_23)=3,
dim coker(T_A)=3
```

are correct as dimensions.  They do not identify nearby cycles, an extension,
or even two objects carrying the same loop action.  `H^1(U,nabla_23)` is
global cohomology, not a local system on `U`; the finite coefficient cokernel
has no supplied `pi_1(U)` action.  “Matching local monodromy characters” is
therefore not a property of those two vector spaces as stated.  The number
three is also forced very cheaply: a nontrivial rank-one local system on an
affine line with four punctures has Euler-characteristic contribution three,
while the displayed polynomial window has dimensions `16-13=3` once
`T_A` is injective.

There is, however, a sharper rank-one identity worth salvaging.  Since

```text
nabla_23 = d + (23/2)dA/A,
T_A(Q)   = 2A Q' - 3A'Q,
```

one has the exact chain formula

```text
nabla_23(A^(-13)Q)
   = (1/2) A^(-14) T_A(Q) dX.                 (NC-salvage)
```

Thus the finite complex

```text
C[X]_(deg<=12) --T_A--> C[X]_(deg<=15)
```

maps explicitly into the algebraic de Rham complex of `nabla_23`.  This is
far stronger and better typed than equality of dimensions, but it is still
rank one.  To promote an isomorphism

```text
coker(T_A) ~= H^1_dR(U,nabla_23),
```

one must certify that this finite-window inclusion is a quasi-isomorphism (or
at least an isomorphism on `H^1`) by exact pole-order reduction.  That is the
narrowest salvage of `FACE-NC`.  It supplies no short exact sequence of
connections and no new R1 client.

## 2. `FACE-CHAR`: there is no typed loop map to the Keller passport

### 2.1 The two representations have different domains

The face character is

```text
chi_m: pi_1(U_X=A^1_X minus Z(H)) -> mu_4,
chi_m(gamma_i)=exp(-2 pi i m e_i/4).
```

For `m=23`, `e_i=2`, this gives `chi_23(gamma_i)=-1`.

The degree-`d=td` Keller passport on a generic vertical slice is instead

```text
rho: pi_1(B=L_a minus (A(F) intersect L_a)) -> S_d,
```

where its meridians surround target points on the asymptotic curve and act on
the `d` source sheets.  A root of a Newton face polynomial is a face
coefficient/branch datum.  It is not, merely by sharing a label, a target
branch value in `B`.

To compare the two, one needs at minimum a geometrically induced homomorphism

```text
theta: pi_1(U_X) -> pi_1(B)
```

and a one-dimensional character `lambda` of the passport monodromy group
such that

```text
chi_m = lambda o rho o theta.                  (CHAR-factor)
```

Grok46 supplies none of `theta`, `lambda`, or the factorization.  Identifying
`H` as a Newton face of an exact pair does not create them.  In particular, a
GGV coefficient fixture is not automatically a Keller map, has no constructed
asymptotic curve, and has no `td`-sheeted etale cover whose passport could be
queried.  Calling the fixture case “tautological” is false.

### 2.2 The post-seal chart correction makes the dependency narrower, not valid

The truth delta refutes the physical-other-chart interpretation of
Corollary 7.4 and splits the old `C74-PLACE` package.  Face-power custody is
native, but `H-TRUNC` and the deck/leaf-place bijection remain open; chart
coverage belongs to the exact-pair constructor.  Even successful resolution
of those items would identify face data with boundary places, not yet a face
meridian with a transverse target meridian of `A(F)`.

Accordingly `FACE-CHAR` must be refiled behind:

```text
exact-pair face custody
  + H-TRUNC
  + deck/leaf-place custody
  + finite-end/asymptotic-value landing
  + an explicit induced loop word in the vertical passport base.
```

It does not depend on the refuted `C74 -> EXIT-RPMC` corridor, but the
exact-pair forest alone is insufficient.  The missing loop map is an
additional obligation, not an automatic consequence of repairing L3/L5.

### 2.3 `-1` as an eigenvalue is not the sign character

Even after a loop map is supplied, Card B conflates two different group
tests.

For a permutation `sigma`:

- `-1` occurs in its permutation-matrix spectrum iff at least one cycle has
  even length;
- `sign(sigma)=-1` iff the total number of even-length cycles is odd
  (equivalently, the total permutation index is odd).

Thus a permutation with two transpositions has local `-1` eigenvectors but
is in the kernel of sign.  A generic asymptotic meridian can contain several
marked inertia cycles, one for every finite end over the same target point.
The face character of one root cannot be promoted to the sign of the entire
permutation without proving that it selects a particular cyclic inertia
factor and, for the total-sign claim, controlling all the other factors.

Nor does an abstract embedding `G <= S_d` guarantee that its sign character
is a rank-one constituent of the `d`-dimensional permutation local system.
What Card B calls “the permutation's cyclic quotient” must be specified:
an eigencharacter of one local cyclic subgroup, a character of the global
monodromy group, and the sign quotient are not interchangeable.

The narrow conditional statement is:

> If an explicit `theta` and a character `lambda` satisfy
> `(CHAR-factor)`, then each named loop obeys
> `lambda(rho(theta(gamma_i)))=exp(-2 pi i m e_i/4)`.

If `lambda` has separately been proved to be sign, value `-1` forces an odd
permutation.  If instead the character is attached to one specified local
cycle, value `-1` forces that cycle's order to be even; it says nothing by
itself about the sign of the other cycles.  This conditional one-line lemma
is the narrowest salvage of `FACE-CHAR`.

### 2.4 The proposed 169-row test is premature and stale after the delta

The post-seal marked-component congruence reduces the clean residue-A census
from 169 ordinary rows to 48 marked-profile survivors and kills none of those
48.  Ordinary passports also forget which `e=1` fixed points are missing
boundary sheets rather than affine sheets.  Therefore, even after a typed
face-to-target map exists, the character must be applied to the marked local
inertia factor on the 48-row census, not blindly to the 169 unmarked identity
tuples.

At present there is no constraint to enumerate at all: without `(CHAR-factor)`,
discarding a passport because one arbitrarily named permutation has the wrong
sign would be a base-change error, not a mathematical cut.  The alternative
`8_28` orbit `(z^4-alpha)^21` has the same defect.  Its four face roots and
deck orbit do not constitute meridians in `L_a\setminus A(F)`.

## 3. Cheapest exact discriminators and disposition

### `FACE-NC`

The current proposal is already decided exactly:

1. `j^*R psi_p=0` by support for the zero-locus interpretation; and
2. `F=H(1+tV)` makes Card A's displayed family locally constant; and
3. the `mu_4` idempotents split the `(23,24)` eigenspaces.

No computation is warranted.  The cheapest useful **salvage** test is
desk-scale rational reduction of `(NC-salvage)`: reduce a basis of the full
twisted de Rham complex to the `deg<=15` pole window and verify that the
induced cokernel map has rank three and zero kernel.  PASS promotes only the
rank-one isomorphism `coker(T_A) ~= H^1_dR`; FAIL leaves merely the already
known dimension count.  Neither result raises avenues 3 or 16 as a coupled
client.

If a later author produces a genuine full unfolding, the exact discriminator
is not “compare dimensions.”  It is: write the resulting connection or
perverse sheaf, state its support, project it with the four `mu_4`
idempotents, and exhibit the off-diagonal extension class.  A `(23,24)`
off-diagonal in an equivariant object must be zero.

### `FACE-CHAR`

Use a one-root type test before any CSP sweep:

1. start from a coefficient-complete exact pair and one named face root;
2. by exact Puiseux substitution, identify its marked boundary end and its
   target asymptotic value;
3. output the induced target-meridian word `theta(gamma_i)` in the generators
   of `pi_1(L_a\setminus A(F))`;
4. compute `rho(theta(gamma_i))` and identify the particular marked inertia
   cycle to which the face character is claimed to apply;
5. test the one-bit character factorization, using total sign only if a
   global sign factor and all other local cycles have been justified.

Failure to produce step 3 is a decisive **NOT TYPED** result and stops the
card.  Once the word exists, the group calculation is one exact permutation
evaluation, not a new 169-passport enumeration.  Any later census should use
the 48 marked survivors from the truth delta.

## Final campaign action

```text
DELETE: FACE-NC as an exhibited nearby-cycles SES of consecutive rows.
DELETE: the Avenue-3/Avenue-16 raise that depends on that SES.
KEEP:   the rank-one Kummer character and formula (NC-salvage), pending
        one finite-window quasi-isomorphism check.
HOLD:   FACE-CHAR as the conditional lemma (CHAR-factor), with zero present
        passport eliminations.
DELETE: the claim that a GGV fixture tautologically supplies passport loops.
REFILE: any future passport test behind exact target-meridian custody and the
        48-row marked-profile census.
```

The two attractive `3`'s and the four `-1` meridians are real arithmetic.
They do not bridge support, base, equivariant splitting, or passport custody.
