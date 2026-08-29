# Finite ends, the asymptotic curve, and marked branch cycles

**Lane:** Sol Ultra, independent connection audit  
**Date:** 2026-08-27  
**Scope:** Avenues 7, 25, and 26 only.  No claim about `C74-PLACE`, landing,
coverage, a degree ceiling, or JC2.  The `20260827T2137Z` peer ideation reports
and `jc2-lean` were not read.

## Verdict

The raw connection is **KNOWN**, not a new avenue.  For a generic vertical
fibre, the confirmed finite-end identity is exactly Chau's 1999 equation
(4.4), written as `chi=1-b1`; his Theorem C already couples the corresponding
vertical and horizontal identities.  A finite end of order `e` is a marked
local inertia cycle of length `e` at a generic point of `A(F)`, but an
ordinary permutation passport forgets whether a fixed point is an affine
sheet or an `e=1` missing sheet.  Therefore `T-RH` cannot simply be appended
to the existing unmarked passport CSP.

There is one exact, apparently unrecorded campaign corollary worth keeping:
after grouping generic asymptotic values by irreducible component of `A(F)`,
the number of vertical values of every fixed generic inertia type is divisible
by the normalized degree `alpha`.  For the clean residue-A passport
(`alpha=2`), this forces each of `a,b,c` to be even and reduces the existing
169 rows to 48.  It does not eliminate the family: all 48 are among the rows
already realized by transitive tuples.

**Allocation:** stop a broad `T-RH -> primitive monodromy` lane.  Add only the
cheap marked-component congruence to the future Avenue-25 coupled CSP.  It
becomes finite only after a complete boundary book supplies all finite ends,
including `e=1` ends, and their component/flag provenance.

## 1. Setup and the exact generic correspondence

Let

```text
F=(f,g): A^2_C -> A^2_C,       J(f,g) in C*,
d=td(F),                       A=A(F)=union_j A_j.
```

Choose `a` outside a finite exceptional set: `C_a=f^{-1}(a)` is smooth and
irreducible; its smooth completion is `bar C_a`; the vertical line
`L_a={u=a}` meets each `A_j` in smooth transverse points and avoids component
intersections and exceptional values of the boundary maps.  Partition the
punctures of `C_a` into poles `P_a` of `g` and finite ends `N_a`.  For
`S in N_a`, put

```text
b_S = g(S),                 e_S = ord_S(g-b_S) >= 1.
```

Then the correspondence is exact:

```text
S in N_a  --->  q_S=(a,b_S) in A intersect L_a.
```

Several `S` may map to the same `q`.  Conversely every generic
`q=(a,b) in A intersect L_a` has at least one such end.  Indeed, on the
degree-`d` map `g:bar C_a -> P^1`, the fibre over `b` consists of the affine
points of `F^{-1}(q)`, each with multiplicity one because `F` is etale, and
the finite boundary ends above `q`.  Hence

```text
delta(q) := d - #F^{-1}(q)
          = sum_{S in N_a, b_S=b} e_S.                    (1)
```

Jelonek's properness criterion identifies this fibre deficit with
nonproperness for a Keller map, so these and only these generic target points
lie on `A(F)`.

Take a small disc in `L_a` transverse to `A` at `q`, with coordinate `z`
vanishing at `q`.  At a finite end `S`, a local source parameter `t` gives
`z=unit*t^{e_S}`.  Thus a meridian about `A_j` has one cycle of length `e_S`
for every end above `q`, together with `d-delta(q)` fixed affine sheets.  In
particular

```text
index(sigma_q)   = sum_S (e_S-1),
support(sigma_q) = sum_{e_S>1} e_S,
delta(q)         = sum_S e_S.                             (2)
```

This exposes the passport loss: an `e_S=1` end is a fixed point of
`sigma_q`, indistinguishable in the conjugacy class from an affine sheet that
extends across `q`.  `delta(q)`, and hence `T-RH`, is not determined by an
ordinary conjugacy class.  It is determined by a **marked** class retaining
boundary-versus-affine fixed points.

The restricted cover over `L_a minus A` is literally the vertical-line
restriction of the global finite etale cover over `A^2 minus A`; its
monodromy is therefore a transitive subgroup of the global monodromy.  Equality
of the two images would require a separate surjectivity theorem for this
special vertical-line inclusion.  It is not supplied by `T-RH` and is not
assumed here.

## 2. Theorem candidate A: weighted Jelonek--inertia balance

> **T-A (generic vertical slice).**  Let `nu_j:A^1 -> A_j` be the
> normalization and put
> `k_j=deg(f o nu_j)>0`.  Let `delta_j` be the generic value of (1) on
> `A_j`.  Then
> 
> ```text
> sum_{S in N_a} e_S
>   = sum_j k_j*delta_j
>   = d + b1(C_a) - 1.                                   (3)
> ```

**Proof.**  A generic vertical line meets `A_j` in `k_j` points.  The
transverse boundary profile, hence `delta_j`, is locally constant on a dense
open subset of `A_j`.  Summing (1) gives the middle expression.  Riemann--
Hurwitz for `g:bar C_a -> P^1`, using that all ramification is at punctures
and that the pole orders sum to `d`, gives the last expression.  QED.

**Status: KNOWN.**  Chau 1999, p. 305, equation (4.4), writes precisely

```text
chi(C_a) = d - sum_{finite branches gamma} deg_gamma F.
```

Since `chi(C_a)=1-b1(C_a)` and `deg_gamma F=e_S`, this is (3).  Opus5's
`T-RH` is a correct independent rederivation, not a literature-new theorem.
The grouping through `A_j` is the standard generic-deficit interpretation.
Closest campaign hits are `GROK-MONODROMY.md` (local cycle length equals
ramification index) and `sol-connections.md` section 4 (the need for labelled
dicritical flags).

## 3. Theorem candidate B: component blocks, degree congruence, and braid orbit

Write

```text
deg f = B*alpha,        deg g = B*beta,        gcd(alpha,beta)=1.
```

Chau's component-degree theorem says that, on the normalization of every
`A_j`,

```text
deg(f o nu_j) / deg(g o nu_j) = alpha/beta.
```

Consequently there is an integer `h_j>=1` with

```text
k_j=alpha*h_j,          l_j=beta*h_j.           (4)
```

> **T-B (marked component-block law).**  With `M_f=d+b1(C_a)-1` and the
> analogous `M_g` on a generic horizontal fibre,
> 
> ```text
> M_f = alpha * sum_j h_j*delta_j,
> M_g = beta  * sum_j h_j*delta_j,
> M_f/alpha = M_g/beta.                          (5)
> ```
> 
> More finely, let `tau_j` be the generic marked transverse inertia type on
> `A_j`: the unordered boundary-versus-affine cycle data, modulo the
> tangential deck permutation over `A_j`, rather than literal point names.
> For generic `a`, if `n_tau(a)` counts points of
> `A intersect L_a` of type `tau`, then
> 
> ```text
> n_tau(a) = alpha * sum_{j:tau_j=tau} h_j,
> n_tau(a) == 0 (mod alpha).                     (6)
> ```
> 
> As `a` varies away from the projection discriminant, the `alpha*h_j`
> points contributed by one `A_j` form a transitive braid orbit.  Around
> `a=infinity`, their label permutation is an `alpha*h_j`-cycle.  The
> associated `d`-sheet meridians are conjugate and the ordered branch-cycle
> tuple changes only by Hurwitz moves and simultaneous conjugation.

**Proof.**  Equation (5) is T-A in the two coordinate directions plus (4).
For (6), the generic profile is constant on each irreducible `A_j`, which
contributes exactly `k_j=alpha*h_j` vertical intersections.  Finally the
roots of the polynomial `(f o nu_j)(t)-a` form a connected degree-`k_j`
cover off its critical values; polynomiality gives its unique totally
ramified point over infinity.  QED.

**Status.**  The two mass identities in (5) are **KNOWN**: they are exactly
Chau 1999 Theorem C,

```text
deg f * (d-chi_g) = deg g * (d-chi_f).
```

The marked profile congruence (6) is **NEW TO THE REPOSITORY**, but is an
elementary corollary of Chau's known component-degree ratio, not a claimed
literature novelty.  The braid statement is **KNOWN topology**.  Its campaign
value is typing: the braid acts on asymptotic **branch values**, not as a
block system on the `d` source sheets.

## 4. Exact finite CSP consequence

For a fixed complete book, (5)--(6) do give a finite refinement.  Set
`H=M_f/alpha`.  A component assignment must choose positive integers
`h_j,delta_j` with

```text
sum_j h_j*delta_j = H,        1 <= delta_j <= d,            (7)
```

attach every finite end (including `e=1`) to one of those components, and
then solve the usual product-one/transitivity equations in `S_d`, now with
component blocks and the horizontal mass `M_g=beta*H`.  Since `H` and `d`
are fixed, this is finite.  Immediate inequalities are

```text
#components <= H,
ceil(M_f/d) <= #(A intersect L_a) <= M_f,
alpha | M_f,                  beta | M_g.                    (8)
```

Without a complete end list or `b1`, (7) is not a finite campaign object.

**Residue-A clean control.**  Here `d=6`, `alpha=2`, and the existing tight
passport writes the x-side branch-value counts as

```text
(2)^a (2,2)^b (2,2,2)^c,       a+2b+3c=42.
```

Under the same unramified B-side/no-extra-cycle control used for the 169-row
sweep, (6) forces

```text
a == b == c == 0 (mod 2).
```

Writing `(a,b,c)=2(A,B,C)` leaves `A+2B+3C=21`, which has exactly

```text
11+10+8+7+5+4+2+1 = 48
```

nonnegative solutions.  Thus the marked asymptotic-component condition
removes 121 of the 169 permissive passports, but all 48 survivors still have
transitive identity factorizations by the banked exhaustive sweep.  This is a
real CSP pruning, not a family kill.

## 5. Why this does not advance primitive monodromy

The component blocks in T-B are blocks of **branch values** under variation
of `a`; they are not blocks for the action on the `d` sheets.  Neither (3) nor
(5) bounds the support of a local inertia permutation by anything smaller
than `d`, and neither bounds `H` independently of fibre topology.

There is a scalable exact negative model.  For every `d>=2`, take

```text
bar C=P^1,     g_d(z)=z^d-d*z,
C=bar C minus ({infinity} union {z:z^(d-1)=1}).
```

The only pole has order `d`; the `d-1` removed finite critical points have
distinct values and `e=2`; `g_d` is unramified on `C`; and

```text
sum_N e = 2(d-1) = d + b1(C) - 1.
```

Its finite inertia consists of transpositions and its monodromy is `S_d`.
This is not asserted to come from a Keller surface map; it proves exactly
that T-RH alone cannot force imprimitivity, exclude `A_d/S_d`, or bound `d`.
It agrees with the executed `sol-monodromy-td.md` wall and the residue-A
`S_6` control.

**SCOPE-CONFLICT.**  A varying-`a` braid can become stronger only after the
actual normalized components of `A(F)` (or their parametrizations) are known,
because the van Kampen/Hurwitz relations depend on that braid monodromy.
Degrees and one-place rationality alone do not determine it.  No such
component construction is presently banked.

## 6. Cheapest discriminator / negative control

Run one zero-cost filter, `AF-MARKED-PASSPORT-R1`, on the existing 169
residue-A rows:

1. retain a row iff `a,b,c` are all even;
2. assert the survivor count is exactly 48;
3. use `(a,b,c)=(0,3,12)` as the negative control: it satisfies
   `a+2b+3c=42` and already has a transitive product-one witness, but must be
   rejected by the `alpha=2` component-block congruence.

If the full B-side is later allowed to ramify or share values, rerun on the
**combined marked profiles**, not on x-side cycle types alone.  Do not launch
a new group census: the 48 survivors already pass the old one.

## 7. Source and history pins

Primary sources:

```text
N. V. Chau, "Non-zero constant Jacobian polynomial maps of C^2",
Ann. Polon. Math. 71 (1999), 287-310,
https://doi.org/10.4064/ap-71-3-287-310
repo PDF: refs/chau1999_apm71_full.pdf
SHA-256 ed63b44c6a48f85c80b66e4b95b93618f1b3a4bead536a7ad7ee1bfa5084aac7
Load-bearing locations: Theorem C pp.287-288; Theorem 4.4(E1) pp.304-305;
equation (4.4) p.305; Theorem 4.5 p.306.

Z. Jelonek, "The set of points at which a polynomial map is not proper",
Ann. Polon. Math. 58 (1993), 259-266,
https://matwbn.icm.edu.pl/ksiazki/apm/apm58/apm5834.pdf
fetched PDF SHA-256
30b497466c1c27923a918db1c7277e90485667647fb3f2d6505f3f2c26ef420e
Load-bearing location: Proposition 6 (properness iff full generic
multiplicity is present in the fibre), pp.261-262.

N. V. Chau, "Non-proper value set and the Jacobian condition",
https://arxiv.org/abs/math/0305088
arXiv e-print SHA-256
c35bdf31aac73c0f5f08cc947490586e3308e1827158734e7dd7f064727fc40d
PDF SHA-256
8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f
Load-bearing location: Theorem 1 / Corollary 2 (one point at infinity and
the normalized component-degree shape).
```

Campaign history read (no peer-round reports):

```text
xmodel/g2-c74-place-exit-rpmc-hostile-review-opus5-20260827.md
  968b42ced94bd6c59b33bfdab30677e2ad6ad91a349fc978a271c01083d11e7d
ladder/GROK-MONODROMY.md
  a45ffd7577809c5e9ced861d10c6cd1d7c7e9286c6e257c3f4f0c2ced1acbd6c
xmodel/sol-monodromy-td.md
  b814463138788826dccffc9cf4913c0b49c7fbe2bb13e16cce66dff1e5702a45
xmodel/sol-connections.md
  3fe165e55704e0a4b5dba3b5968ea995846a81f58b65968fa89521ef8595895c
xmodel/sol-lateral3.md
  a6cc7385b6a2fbb0c92db05a3052dfe14b083d04d3e049e7006923f7f3b293ca
```

## 8. Final disposition

```text
Avenue 7:  KEEP as the component/flag object; T-A is already known.
Avenue 25: ADD the marked component-block congruence and Chau Theorem C;
            cheapest exact pruning is 169 -> 48 on the clean residue-A CSP.
Avenue 26: NO CHANGE / STOP T-RH-only continuation; A_d/S_d remain scalable.
```

The broad proposed connection stops here: beyond the 48-row marked filter it
is a reformulation of known generic-fibre topology until the campaign actually
constructs the normalized components and braid monodromy of `A(F)`.
