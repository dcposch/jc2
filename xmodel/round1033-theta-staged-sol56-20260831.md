# THETA-STAGED — kill or pin the one-cusp horn

## Scope, frozen inputs, and verdict

This lane used only the four frozen read-only copies in
`/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.aVr0vY/inputs`.
Before mathematical reading, `shasum -a 256` returned, in the charged order,

```text
2710e90fdcbf1c2c9f61d6a606cf1e6553de5de65e4899367005433bc4f4e5f5
7a60ff245fc351a99a23815908909327dc6a9644f849a4d3b289079c98488474
e87d0af3fb433edc5056ff651ce8623aae840bfb962d7d08eba6588b970123ca
2793104bcf746eab690ca75a2aaf2ef105b64e7be0c1826eb1fa9ed51ba992ef
```

All four values match the charge.  No canonical ledger or charged original was
read or edited; `jc2-lean` was not inspected; no CAS was run.  Exact source
references below are to line numbers in these frozen copies, abbreviated
`structure`, `connectedness`, `review`, and `synthesis`.

## Stage 0 — typing and presentation independence

### 0.1 The maps that are, and are not, charged

Fix the coefficient field `C` and the ordered presentation generators
`(A,U,Z)`.  Put

```text
q=U^2-A-A^2Z,
R=C[A,U,Z]/(q),
S=Spec R.
```

For definiteness the intended charged coordinate would be `h=f`, with mate
`k=g`; the symmetric choice is `h=g`, `k=f`.  Its target pullback would have
to be

```text
pi^#: C[xi,eta] -> R,
       xi |-> f=P_f(A,Z)+U Q_f(A,Z),
       eta|-> g=P_g(A,Z)+U Q_g(A,Z).                 (0.1)
```

The normal form displayed in (0.1) is the unique normal form available for
*every* element of `R` (`structure:145-149`).  The frozen inputs name the
abstract map `pi=(f,g):S->A2` (`connectedness:31-36`) and assume its charged
properties, but nowhere supply any of the four polynomials
`P_f,Q_f,P_g,Q_g`.  The formal coefficients `f_i(Z),g_i(Z)` along `Phi` are
also only names, not values (`structure:164-180`).  Thus (0.1) is a typed
direction and generator order, but not an explicit ring map whose images can
be checked or whose pole divisors can be resolved.

There is one different explicit map in the packet:

```text
iota: R -> C[x,y],
      A |-> x^2,
      U |-> x+x^3y,
      Z |-> 2y+x^2y^2.                              (0.2)
```

Indeed the image of `q` is
`(x+x^3y)^2-x^2-x^4(2y+x^2y^2)=0`.  This is the retained cyclic-source chart
(`structure:96-98`), not the oppositely directed charged pullback (0.1).
Renaming its `x,y` as `xi,eta` would identify source variables with target
coordinates without a ring map.  Likewise `A` is explicitly the ruling
coordinate `t` (`structure:483-484`), not a licensed substitute for
`h in {f,g}`.

### 0.2 Admissible model class and the invariant part that survives

The model class needed by the promoted table can be stated, but no member is
specified by the frozen data.  An admissible marked model for `(h,k)` would be
a smooth projective surface `X` with an open immersion `S subset X`, reduced
SNC boundary `D=X-S`, resolutions of the rational maps defined by `h` and
`k` to `P1`, and markings that retain separately

1. the closure of the intrinsic divisor `Phi=V(A,U)`;
2. the source prime(s) over the ramification boundary of `pi`;
3. the closure and normalization of a general `h`-fibre; and
4. the lift(s) of the unique point at infinity of the normalized target curve
   `B`.

“Minimal” would additionally require an explicit contraction rule: no
boundary `(-1)`-curve may be contracted while preserving the SNC condition,
both resolved maps, and all four markings.  The packet supplies neither that
rule nor a canonical representative.  Its finite normalization `Y` is not
such an `X`: the packet says that the two-dimensional boundary neighborhood
requires a chosen `Y` and absent pole expansions (`structure:243-248`), and
later says directly that an actual SNC boundary/pole model is still missing
(`structure:596-609,638-642`).

There is nevertheless a presentation-independent definition of the *number*
`Theta_h`, conditional only on a fixed charged pair and the promoted table.
Let `q_infty` be the single point at infinity on the smooth completion of the
normalization of `B`, and let `Cbar_h` be the unique smooth projective model of
the general `h`-fibre.  Then

```text
d_h = -ord_(q_infty)(h o beta_B),
r_h = # {p in Cbar_h : ord_p(k)<0},
Theta_h = d_h-r_h-2.                                  (0.3)
```

These are the definitions used in `structure:596-606` and
`connectedness:291-296,318-329`.  If `X'->X` is any boundary birational
modification that is the identity on `S`, normalization leaves the two
function fields and their smooth projective curve models unchanged.  Hence

```text
d_h(X')=d_h(X),       r_h(X')=r_h(X),
Theta_h(X')=Theta_h(X).                               (0.4)
```

This is the required transformation law for the numerical invariant.  It
does not identify a surface divisor, and no pole identity is used to obtain
it.

### 0.3 Failure of the horizontal-vertex typing

The phrase “horizontal vertex” occurs in the frozen material only in the
launch instruction (`synthesis:70-80`); it is not defined or exhibited in a
model.  With the standard relative meaning, such a vertex is an irreducible
component of `D` whose map to the `h`-base is dominant, hence a divisorial
valuation of `K=C(S)`.  In contrast, `q_infty` in (0.3) is a point/place of
the one-dimensional field `C(B)`.  A lift from that target place to a prime
of a source compactification may split and requires the missing marked
normalization and resolution.

In particular, the one-place statement for `B` does not imply a unique
horizontal source component.  The promoted table itself permits
`r_h=1,2,3,4` (`connectedness:332-340`), and `r_h` counts source places on
`Cbar_h`, not the target place on `B`.  Calling `q_infty` the desired vertex
would identify a place with a surface divisor/flag and would select the
`r_h=1` row before computing it.  The packet separately warns that `Phi`, the
normalization boundary, and deleted cyclic lines are different objects
(`structure:37-49`).

Nor do (1.12)--(1.14) repair the typing.  They concern the unique ramified
factor at the **generic point of `B`** (`structure:243-279`), whereas `d_h`
uses the special place `q_infty` and `r_h` uses places on a general source
fibre.  Transporting that generic factor to a unique vertex at infinity is
exactly the missing geometric assertion.  Accordingly none of those pole
identities, and no divisor/intersection subtraction, is invoked here.

The fail-closed verdict is

```text
OPEN[THETA-STAGE0-MARKED-SNC]: the charged pullback is not explicit, no
admissible minimal marked SNC representative is supplied, and no unique
horizontal source vertex or unique lift of q_infty is proved.
```

The minimal data needed to reopen the lane are: explicit checked images for
`f,g` in (0.1) (or an equivalent complete divisorial pole ledger), an equation
and normalized parametrization for `B`, one marked SNC compactification
resolving them, a marking-compatible minimality rule, and a proof identifying
all source primes over `q_infty`.  The packet only says “let `b(f,g)` be” an
equation of `B` (`structure:250`); it gives neither `b` nor `beta_B`.  Stage 0
therefore fails, so the protocol stops here.

## Stage 1 — global prefilter

**Not entered.**  The staged charge permits the puncture/parity prefilter only
after Stage 0 types the charged model and horizontal vertex.  No global
puncture count is transferred from another curve, and no partition row is
selected.

## Stage 2 — marked SNC model and computation

**Not entered.**  In particular, this report does not construct an unmarked
compactification of `Spec R` and then retrofit `f` or `g`; does not iterate
boundary blowups to manufacture a vertex; does not promote the interior
completion (1.3) into a boundary chart; and does not apply (1.12)--(1.14) away
from their typed generic ramification valuation.  There is consequently no
divisor/intersection table and no subtraction purporting to evaluate
`Theta_h`.

## Guardrail audit and conclusion

- **Variable/ring map:** (0.1) and (0.2) have different directions, variables,
  and meanings.  Their names were not matched, and the image check for (0.2)
  was displayed.
- **Flag/place/series:** the target place `q_infty`, a source horizontal prime,
  a point on `Cbar_h`, the interior divisor `Phi`, and the generic ramified
  factor of (1.12) remain distinct.
- **Pole/interior and floor/attainment:** no pole identity is used before a
  vertex is typed; no valuation floor, necessary table row, or representative
  is promoted to attainment.
- **Orevkov side observation:** no remainder species is computable before the
  marked SNC model exists.  The packet itself says that the monogenic-index
  identity supplies no Orevkov--Chau correction (`structure:539-557`).  It is
  not identified with `Theta_h`, numerically or geometrically.
- **Charge:** no new exit price is asserted.

Final disposition:

```text
OPEN[THETA-STAGE0-MARKED-SNC]
```

This is a geometric missing-object verdict, not a contradiction in the
promoted partition table.  The intrinsic transformation law (0.4) protects
`Theta_h` once the charged pair is fixed, but it cannot supply the absent
marked map, lift, or horizontal vertex.  The one-cusp configuration is
therefore neither killed nor pinned by this lane.

<!-- BODY-END -->
