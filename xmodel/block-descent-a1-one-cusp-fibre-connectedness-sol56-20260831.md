# General coordinate-fibre connectedness

## 1. Charge, frozen inputs, and verdict

The frozen copies were hashed before mathematical reading and matched:

```text
2710e90fdcbf1c2c9f61d6a606cf1e6553de5de65e4899367005433bc4f4e5f5
  block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
8abde87c3e9320ae1b75e90d4c4c26e4a7a16dc685398bf446b5b33b230f9787
  block-descent-a1-one-cusp-wild-valuation-prereview-sol56-20260831.md
d5fa676a7c364bb8cbc470a2a912be995456ba98cea7a9d4943044844f73b97a
  block-descent-a1-one-cusp-wild-valuation-hostile-review-grok46-20260831.md
```

**Verdict: PROVED for both coordinates.**  The relative algebraic closures
of `C(f)` and `C(g)` in `Frac(R)` are trivial.  Hence each general coordinate
fibre is geometrically irreducible and connected.

The pre-review's proposed boundary proof is not complete from the literal
frozen census: it would require an unstated exhaustivity assertion excluding
extra vertical or horizontal ramified boundary images.  This report makes
all earlier steps of that route exact and types its last interface `OPEN`,
then proves primitivity independently from the rationality and unit group of
the exact ring together with `{f,g}=kappa`.  Thus the route is open but the
theorem is not.  No CAS was run, no charged or canonical file was edited, and
`jc2-lean` was not inspected.

## 2. Algebraic and geometric setup

Put

```text
K=Frac(R),                 E_f=C(f),
pi=(f,g):S->A2,            R=C[A,U,Z]/(U^2-A-A^2Z).
```

Only these frozen inputs were used for packet provenance.

The sketched boundary proof would need the following exhaustive datum:

```text
(BC)  every ramified prime divisor of Y-S maps into B;
      equivalently, B is the whole codimension-one ramified boundary image.
```

The cusp in the reviewed census makes `B` neither a vertical nor a horizontal
line (a coordinate line is smooth), so `(BC)` would exclude a ramified
boundary divisor over either kind of coordinate line.  But `(BC)` is not
actually stated in the frozen valuation packet or hostile review.  The phrase
“sole irreducible nonvertical boundary image `B`” occurs only in the
pre-review's unproved sketch.  The packet's assertion that a *general* slice
has no other finite deleted points cannot detect a boundary component over
one exceptional coordinate value.  Cofiniteness of `pi(S)` also does not
exclude it: retained sheets may still cover the generic point of that line.
Concretely, the degree-four map

```text
A2_(x,y)->A2,             (x,y) |-> (x^4+x,y),
```

restricted to `S_0=D(4x^3+1)`, is etale and still surjective: over each of its
three distinct critical values the deleted double point has two retained
simple companions.  Yet its deleted divisors map onto vertical lines.  This
is a countercontrol to the cofinite-image inference, not a realization of the
charged ring.  In the frozen texts, compare the census at structure
lines 387--412 and hostile-review lines 468--471 with the unfinished proposal
at pre-review line 101.
Accordingly the proposed boundary-census proof has one precisely typed open
interface.  Section 3 first isolates it, then proves primitivity by a different
argument intrinsic to `R`.

Since `pi|_S` is etale, `S` is smooth and both `f:S->A1` and `g:S->A1` are
smooth.  In particular, every scheme fibre of either coordinate is a smooth,
hence reduced, curve.  For such a fibre, connectedness and irreducibility are
equivalent: distinct irreducible components of a smooth curve are disjoint.

We use the following standard field form of generic geometric integrality.
For a dominant map from an integral variety to a smooth curve in
characteristic zero, its generic fibre is geometrically integral exactly when
the base function field is algebraically closed in the total function field.
Once this holds, geometric integrality spreads over a nonempty open subset of
the base.  Since the base here is `A1`, the exceptional set is finite.

## 3. The general `f`-fibre

### 3.1 Relative closure and forced finite ramification

Let `L_f` be the relative algebraic closure of `E_f=C(f)` in `K`, and put
`delta_f=[L_f:E_f]`.  This is a finite separable extension.  Let
`Tbar_f->P1_f` be the finite map from the smooth projective curve with
function field `L_f`; it is connected and has degree `delta_f`.
Also `g` is transcendental over `L_f`, and the tower
`C(f,g) subset L_f(g) subset K` shows that `delta_f` divides `4`.

Suppose `delta_f>1`.  This cover must ramify over a finite value of `f`.
Indeed, if all ramification lay over infinity and `r` were the number of
points above infinity, then its total ramification would be

```text
R_infty=sum_(q|infinity)(e_q-1)=delta_f-r<=delta_f-1.
```

Riemann--Hurwitz would give

```text
2g(Tbar_f)-2=-2delta_f+R_infty<=-delta_f-1<-2,
```

which is impossible.  Hence there are `a in C` and a point `q` above `a`
with `e(q/a)>1`.  This is the precise finite-ramification step: a nontrivial Stein
curve cannot be an unramified cover of `A1`, nor can all of its necessary
ramification be hidden over infinity.

### 3.2 The ramified point creates a vertical boundary divisor

Let `T_f` be the normalization of `A1_f` in `L_f`.  Its coordinate ring is
the integral closure of `C[f]` in `L_f`.  If `t` belongs to that ring, then
`t` is integral over `C[f]`; the same monic equation has coefficients in
both `R` and `C[f,g]`.  Normality of `R` and of `Y` therefore gives

```text
O(T_f) subset R intersect O(Y) subset K.
```

Consequently both the coordinate map on `S` and the finite normalization
factor through `T_f`.  More explicitly, with `W=T_f x A1_g`, there is a
finite dominant factorization

```text
Y --rho--> W --(tau,id)--> A1_f x A1_g.
```

Finiteness of `rho` is elementary here: `O(Y)` is finite over `C[f,g]`, it
contains `O(T_f)[g]`, and the same finite module generators work over the
larger intermediate ring.  On function fields this is the tower
`K/L_f(g)/C(f,g)`.

The curve `E_q={q} x A1_g` is a prime divisor of `W`.  By lying over for the
finite dominant map `rho`, choose a prime divisor `D` of `Y` above `E_q`.
At the corresponding DVRs,

```text
ord_D(f-a)=e(D/E_q)e(q/a)>1.                            (3.1*)
```

Thus `pi` is ramified at the generic point of `D`.  That generic point cannot
belong to `S`, where `pi` is etale, so `D` is a divisor in `Y-S`.  Moreover a
finite map preserves dimension and `rho(D)=E_q`; hence

```text
pi(D)={f=a},
```

the whole vertical line, not just a point of it.  By `(BC)`, `pi(D)` is
contained in `B`.  Both are irreducible curves, so this would make `B` that
vertical line, contradicting the reviewed singular nonvertical `B`.
Thus the pre-review's proposed route would prove `delta_f=1` if `(BC)` were
available.  On the frozen statements, however, its last implication is

```text
OPEN[census-exhaustivity-f]: no vertical irreducible component occurs
in the codimension-one ramified boundary image of Y->A2.
```

This `OPEN` belongs to that proof route, not to the connectedness question:
the next argument closes the latter without `(BC)` or any boundary census.

### 3.3 Intrinsic primitivity from rationality and units

First, the defining equation gives

```text
K=C(A,U),                  Z=(U^2-A)/A^2,
```

so `K` is a rational function field of transcendence degree two.  By the
generalized Luroth (unirational-curve) argument, `Tbar_f` is rational: it is
dominated rationally by `P2`, and a general line has nonconstant restriction,
so `P1` dominates it.  Hence `Tbar_f` has genus zero and is `P1`.

The exact ring has no nonconstant units.  Indeed,

```text
R_A=C[A,A^(-1),U],
```

so a unit of `R` becomes `cA^n` after localization.  At the height-one prime
`P=(A,U)`, the relation gives `ord_P(A)=2`; a global unit has order zero.
Thus `n=0` and

```text
R^*=C^*.                                                     (3.2*)
```

The affine normalization `T_f` is `Tbar_f=P1` minus the nonempty finite set
`tau^(-1)(infinity)`.  As shown in §3.2, `O(T_f) subset R`, so
`O(T_f)^* subset R^*`.  If at least two points had been removed from `P1`,
this affine curve would have a nonconstant unit: after sending one removed
point to infinity, `t-alpha` is a unit when a second removed point is
`alpha`.  Equation (3.2*) forbids this.  Hence precisely one point is removed
and, after choosing a coordinate,

```text
O(T_f)=C[t],                 f=P(t) for some P in C[t].
```

Here `t` lies in `R`, and the degree of `P` is `delta_f`.  The constant
Poisson bracket now supplies the decisive primitivity identity

```text
kappa={f,g}=P'(t){t,g}.
```

Both factors lie in `R`; since their product is a unit, `P'(t)` is a unit of
`R`.  By (3.2*) it is a nonzero constant.  Characteristic zero and the
transcendence of `t` give `deg P=1`.  Consequently `delta_f=1`, i.e.

```text
C(f) is algebraically closed in K.                         (3.3*)
```

It follows that the generic `f`-fibre is geometrically integral and that
`C_f=V(f-a)` is geometrically irreducible (hence connected) for every `a` in
some nonempty open subset of `A1`.

### 3.4 Exceptional values

The complement of that open subset is finite.  At those values the fibre is
still smooth and reduced, because it is the base change of a coordinate line
under the etale map `pi|_S`, but the charged data do not classify its number
of connected components.  No connected single-genus formula is asserted for
such a special fibre.  Cofiniteness of `pi(S)` makes both coordinate maps
surjective, so none of these special fibres is empty.

For the boundary table one must enlarge this finite exceptional set by the
`f`-coordinates of the cofinite target complement, `c`, `n`, the other
singular points of `B`, and `Sing(Y)`, together with the critical values of
`f o beta_B`, the tangency values of vertical lines with `B`, and the finitely
many values supporting any vertical boundary components permitted by
`OPEN[census-exhaustivity-f]`.  Outside the resulting finite set, the fibre
is connected and the charged general-slice conclusion (3.1) applies: its
completed mate map has degree four, and every finite boundary place is a
distinct transverse index-two place.  At an excluded value, intersections
may collide or become tangent, may meet a special boundary point or
`Sing(Y)`, and the places and indices must be recomputed on the normalization
of that special fibre.

## 4. The general `g`-fibre

The same proof applies after interchanging `f` and `g`.  Let `L_g` be the
relative algebraic closure of `C(g)` in `K`.  If its degree were greater than
one, Riemann--Hurwitz for its projective Stein curve would again force a
ramified point over a finite `g`-value.  Factoring `Y` through
`T_g x A1_f` would then produce a ramified divisor of `Y-S` mapping onto the
horizontal line `{g=a}`.  The frozen census does not expressly exclude it,
so the analogous proposed route stops at

```text
OPEN[census-exhaustivity-g]: no horizontal irreducible component occurs
in the codimension-one ramified boundary image of Y->A2.
```

The intrinsic proof is fully symmetric.  The projective curve of `L_g` is
`P1`; its affine normalization embeds in `R`; and `R^*=C^*` forces it to have
one point at infinity.  Thus its ring is `C[t]` and `g=Q(t)`.  Now

```text
kappa={f,g}=Q'(t){f,t}.
```

It follows that `Q'(t)` is a unit of `R`, hence a nonzero constant, so
`deg Q=1`.  Therefore

```text
C(g) is algebraically closed in K,
```

and the general `g`-fibre is geometrically irreducible and connected.

Nothing in the intrinsic argument breaks under the interchange.  Only the
unused boundary route changes direction: it would need `B` nonvertical for
`f` and nonhorizontal for `g`, both of which follow from the cusp, as well as
the missing exhaustivity clauses.  The exceptional-value discussion is
likewise symmetric, with horizontal tangencies and the `g`-coordinates of
the listed special sets, including any horizontal boundary-component values,
substituted for their vertical counterparts.

## 5. Repaired identities and partition table

Fix `h in {f,g}`, let `k` denote the other coordinate, and choose a general
value as in §§3.4--4.  Let `Cbar_h` be the smooth connected projective
completion of `C_h`, let `gamma_h` be its genus, and split the deleted places
as `Sigma_infty` over `k=infinity` and `Sigma_fin` over finite `k`.  Put
`r_h=#Sigma_infty`, and let `e_p` be the local degree of the completed mate
map `kbar:Cbar_h->P1`.  Its total degree is four.

### 5.1 Repaired (2.5)

The exact local vector-field divisor from (2.1) and Riemann--Hurwitz give

```text
deg Zero(X_h|C_h)=sum_(p in Sigma_infty)(e_p+1)=4+r_h,
deg Pole(X_h|C_h)=sum_(p in Sigma_fin)(e_p-1)
                  =2gamma_h+2+r_h,
deg div(X_h|C_h)=2-2gamma_h.                 (2.5-repaired)
```

This is now justified because `Cbar_h` is one connected curve.  Indeed,
`sum_infty e_p=4`, while Riemann--Hurwitz says

```text
2gamma_h-2=-8+sum_all(e_p-1).
```

### 5.2 Repaired (3.2) and the four rows

Consuming the charged general-slice conclusion (3.1), after the additional
generality conditions in §§3.4--4, every finite deleted place is transverse
of index two, and their number is

```text
d_h=deg(h o beta_B).
```

Therefore the finite ramification sum in (2.5-repaired) is `d_h`, so

```text
d_h=2gamma_h+2+r_h.                         (3.2-repaired)
```

The pole orders of `k` over infinity form a positive partition `lambda_h` of
four, of length `r_h`.  The complete necessary table is consequently

| `r_h` | `lambda_h` | necessary `d_h` |
|---:|---|---:|
| 1 | `(4)` | `2gamma_h+3` |
| 2 | `(3,1)` or `(2,2)` | `2gamma_h+4` |
| 3 | `(2,1,1)` | `2gamma_h+5` |
| 4 | `(1,1,1,1)` | `2gamma_h+6` |

These rows are necessary, not sufficient, and assert no attainment of a
tuple.  They apply separately to `f` and `g`; the charged data give no
equality between the two genera or between the two infinity partitions.

### 5.3 Repaired closure (3.6)

A supplied pair of tuples `(d_h,gamma_h,r_h,lambda_h)` is excluded if any of
the following holds:

```text
d_f<=2 or d_g<=2;
d_h-r_h-2 notin 2Z_(>=0) for some h in {f,g};
gamma_h != (d_h-r_h-2)/2 for some h in {f,g};
lambda_h is not a positive partition of 4 of length r_h
    for some h in {f,g}.                       (3.6-repaired)
```

The third line is the missing consistency clause.  Equivalently, do not
supply `gamma_h` independently, but define it by

```text
gamma_h=(d_h-r_h-2)/2.
```

Without this clause, for example, `(d,r,gamma,lambda)=(5,1,17,(4))` passes
the three literal old tests despite contradicting (3.2-repaired).

### 5.4 Correct provenance of (2.6)

Once a finite deleted ramified place `p` of index `e_p` is known, the
Riemann--Roch witness and local calculation are valid.  If `H` has its only
pole on `Cbar_h` at `p`, of order `M>0`, then

```text
epsilon_f=1,                    epsilon_g=-1,
ord_p((X_h|C_h)^j H)=-M-j e_p,                         (2.6)
lc_p((X_h|C_h)^j H)
 =(epsilon_h kappa/e_p)^j lc_p(H)
   product_(i=0)^(j-1)(-M-i e_p) != 0,
```

Thus the orders are attained and the iterates are linearly independent.

The existence of `p` did not follow from the phrase “total degree four”
alone: a disconnected fully split degree-four control can have no finite
ramification.  There are two valid provenance routes in the repaired packet.
First, the connectedness theorem above plus (2.5-repaired) makes the finite
ramification sum `2gamma_h+2+r_h>0`.  Second, independently, a general
transverse intersection with the noncoordinate boundary `B` supplies an
index-two place (because `d_h>0`).  Formula (2.6) itself is local once either
route has supplied that place.

## 6. Other surviving corrections

At the interior companion over the target cusp, put

```text
p=f-f(u_c),                    q=g-g(u_c).
```

Etaleness gives the exact marked completion and fields

```text
Ohat_(S,u_c)=C[[p,q]],
X_f=kappa partial_q,           X_g=-kappa partial_p.       (1.11)
```

The safe cusp-companion conclusion is narrower than “no local invariant can
detect wildness”:

> The unmarked formal conjugacy class of the vector-field germ, and hence any
> fixed finite jet of that unmarked germ, cannot detect global
> non-local-finiteness.  Full marked expansions of distinguished global
> algebra generators can detect it.

Indeed, the unmarked pair is the same translation pair as on the tame affine
plane.  Once the embedding of `R` and the labels `A,U,Z` are retained,
however, local finiteness is equivalent to a constant-coefficient polynomial
recurrence for every generator orbit.  Global non-local-finiteness therefore
forces at least one full marked generator series to fail such a recurrence.
This is infinite-jet data; the polynomial cusp equation itself and any fixed
finite jet of the unmarked vector-field/cusp germ remain unable to witness it.

With the connectedness repair, the packet's local divisor formula (2.1),
uniformizer iterate formula (2.4), and the conditional local calculation
(2.6) survive exactly.  The generic transverse-boundary calculation and its
independent non-local-finiteness witness also survive.  Nothing here supplies
the special length-three cusp-boundary completion, a cusp Puiseux expansion,
or an existence theorem for any row of the necessary table.

## 7. Conclusions and typed open points

The hidden premise is now discharged: for `h=f` and `h=g`,

```text
C(h)^alg intersect K=C(h),
```

where the algebraic closure is taken inside `K`.  Thus the general coordinate
fibres are geometrically irreducible, and (2.5), (3.2), the four-row table,
and (3.6) are valid in the repaired connected forms of §5.  In particular a
recorded genus must obey `gamma_h=(d_h-r_h-2)/2`.

Two limitations remain, neither affecting that verdict:

1. `OPEN[CENSUS-EXHAUSTIVITY]`: the frozen inputs do not say that `B` is the
   entire codimension-one boundary or branch image.  Consequently the
   pre-review's proposed *boundary* proof stops at this interface.  The
   intrinsic rationality/unit/bracket proof bypasses it.
2. `OPEN[SPECIAL-FIBRES]`: the finitely many nongeneral coordinate fibres are
   smooth and reduced, but their connected-component counts and their
   normalized boundary-place ledgers are not determined by the charged data.

No exit price is asserted.

<!-- BODY-END -->
