# Hostile review — integer-slope source-descent congruence

| Field | Value |
|---|---|
| Charged target | `xmodel/max12-812-order2-affine-faber-integer-slope-source-descent-congruence-theorem-20260826.md` |
| Target SHA-256 | `596bf3260038885c917d12203e72f3892a987d8eb324f01cffe9ca967005dde0` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest counterexample | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile reconstruction from the charged source identities. Different model family from the producer. No producer status line, no charged `CONFIRMED`/`PASS`/`UNIT` token, and no validator string is evidence |
| Method | SHA-256 of the target and of every named source identity before reading producer verdict prose; hand reconstruction of the unramified `T=1` completion, the centered monic-square coordinate change over `Z[1/2]`, the unique extension of `tau`-valuation through `sigma^3=Lambda`, vector-minimum and cancellation controls, the balanced-ray table `alpha=4`, `H=15,16,17,18`, and the Galois module of the Gate-A lift `tau=s^3`, `varrho=s^3`, `sigma=s^4`. No Singular, Sage, msolve, Lean, or substantive CAS identity was used as evidence |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the charged target is
`596bf3260038885c917d12203e72f3892a987d8eb324f01cffe9ca967005dde0`,
matching the required pin. Producer verdict language, the target's own
status line, and any `CONFIRMED` token on a parent review were not used
as evidence. No file other than this review was written. The target,
named source identities, shared ledgers, and `jc2-lean` were not edited.

---

## Verdict

**CONFIRMED.**

At either unramified coefficient-infinity place of the fixed order-two
`U=2,[6,2]` source, an actual rational coefficient germ has invariant
coordinates in `L(x)` and therefore in the completion `L((tau))`. On an
integer strict ray `Lambda=tau^alpha u(tau)` with `alpha>3` and `u(0)!=0`,
every scaled ordinary coefficient `C_i` and both blocks of the unique
centered monic-square division `C=Q^2+Delta` remain in that same complete
field. After a finite constant extension and the Hensel cube root of the
unit `u`, one has `sigma^3=Lambda` with `ord_tau(sigma)=alpha/3`. The
normalized cell `ord_sigma(Delta)=H<infinity` is the vector minimum of
four coefficient valuations. Because that minimum conversion factor is
the positive constant `alpha/3` on every component, one gets
`ord_tau(Delta)=alpha H/3`. The left side is an integer, so `3` divides
`alpha H`. Cancellation inside the square division cannot leave
`L((tau))` and cannot fractionalize the minimum. Units, the odd
coefficient twist, and the choice of cube root of `u` do not change any
valuation.

On the balanced ray `alpha=4` this is exactly `3|H`. Independently:

```text
H=15:  4*15/3=20 in Z,   compatible;
H=16:  4*16/3=64/3 not in Z, excluded;
H=17:  4*17/3=68/3 not in Z, excluded;
H=18:  4*18/3=24 in Z,   compatible.
```

The Gate-A substitution `tau=s^3`, `varrho=s^3`, `sigma=s^4` is a
ramified formal point of the two-parameter source. Flatness of the toric
algebra map `Lambda |-> tau^3 varrho` equates algebraic boundary schemes;
it does not make a series in `s^4` into a series in `s^3`. The
`mu_3`-action `s |-> zeta_3 s` fixes `(tau,varrho)` and sends
`sigma^{17}` to `zeta_3^2 sigma^{17}`. The leading form of a genuine
`H=17` remainder is therefore not Galois-invariant, so the lift does not
descend to `L((tau))`. The same obstruction does not exclude `H=17` on a
different integer slope with `3|alpha`, does not touch the normalized
formal IFT over `L((s))`, and does not speak to Taylor realization, order
two, `(8,12)`, maximum twelve, or JC2.

**CONFIRMED**

---

## Hashes and charged artifacts

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| charged theorem | `596bf3260038885c917d12203e72f3892a987d8eb324f01cffe9ca967005dde0` | immutable target; matches required pin |
| `xmodel/max12-812-order2-u2-62-strict-rees-client-20260825.md` | `e5e3472f052b2ae932daefc9dec7a17106ca4c13f8b920ba59da627d0653fec7` | unramified `T=±1`, `tau=T-1`, twists, `Lambda=tau^3 varrho` |
| `xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md` | `5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b` | flat toric pullback `Lambda |-> tau^3 varrho`; scheme equality only |
| `xmodel/max12-812-order2-affine-faber-a-h17-q7-a3-arcwise-gate-a-composition-theorem-20260826.md` | `266d85ca49aae4b893e0514a3ab1bf271c688ce54295ae20f414675a8c401bc3` | provisional lift `tau=s^3`, `varrho=s^3`, `sigma=s^4`, cell `H=17` |

All four hashes match the values printed in the review prompt or in the
named parent. The reduction-review file
`xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-review-grok-20260826.md`
rehashes to `1da9974dde45fd73c757eb315d50bc9e8abaa028ebb8d5894ca2ea4b2bd6d2de`;
its verdict token was not used. Characteristic zero and invertibility of
`2` are the ambient ring of the `U=2` client (`Q`, square division over
`Z[1/2]`). They are loaded, already satisfied, and not a hole in (1.4).

The target and the three source identities are presently untracked.
`HEAD` at review time is `418e413593120d19e15e6546eb50c985f4b1f038`.

---

## Strongest exact theorem that survives

Work at `T=1` (or the unit-equivalent place `T=-1`) of the rational
Kummer curve of `U=2`, `h=x^6(x-1)^2`. Let `tau=T-1`. Every invariant
source coefficient of an actual rational germ lies in `L((tau))`. On an
integer strict ray

```text
Lambda = tau^alpha u(tau),    alpha in Z, alpha>3, u(0)!=0,
```

form the ordinary scaled centered octic `C` and the unique monic square
division `C=Q^2+Delta` with `deg_z Delta <= 3`. After a finite constant
extension, let `sigma` satisfy `sigma^3=Lambda`. If a normalized cell
declares `ord_sigma(Delta)=H<infinity`, then necessarily

```text
3 divides alpha*H.
```

In particular `gcd(alpha,3)=1` forces `3|H`. On the balanced ray
`varrho=tau*(unit)`, equivalently `alpha=4`, the orders `H=16` and
`H=17` cannot occur for an `L((tau))` germ, while `H=15` and `H=18` are
congruence-compatible. The displayed Gate-A arc `tau=s^3`, `varrho=s^3`,
`sigma=s^4` is a ramified formal source-row point and not an
`L((tau))`-germ. The criterion is necessary, not sufficient, and applies
only to integer strict slopes.

---

## Attack 1 — `C_i` and `Delta` on an actual germ really lie in `L((tau))`

**CONFIRMED.** No coefficient of `Q` or `Delta` leaves the complete
unramified field.

**Place.** The charged client gives the rational Kummer parametrization
`x=1/(1-T^2)`, `T^2=(x-1)/x`, with deck involution `T |-> -T`. The two
points over `x=infinity` are `T=±1`. Substituting `T=1+tau` yields

```text
1-T^2 = -tau(2+tau),     x = -1/(tau(2+tau)).
```

Thus `1/x` equals `tau` times a unit of `L[[tau]]`. The place is
unramified of residue degree one, and its completion is `L((tau))`. The
opposite sheet `T=-1` is the same after `tau |-> T+1` and a unit. Finite
branch ramification `x=sigma_0^2`, `x-1=sigma_1^2` is at `T=infinity` and
`T=0`, disjoint from this chart.

**Invariant coefficients.** Client `(1.2)` puts `a_i=T^{i mod 2} A_i(x)`
with `A_i in L(x)`. Rational functions of `x` pull back to rational
functions of `tau`, hence to Laurent series in `L((tau))`. There is no
Puiseux ramification at this place: an actual rational germ cannot
introduce fractional powers of `tau` into the `A_i`.

**Scaling and twist.** On the integer ray (1.1), `Lambda` itself lies in
`L((tau))`. Faber weights `wt(B_i)=8-i` give `B_i=Lambda^{8-i} A_i`,
still in `L((tau))`. The ordinary twist `C_i=(1+tau)^{i mod 2} B_i` multiplies
odd coefficients by the unit `1+tau` of `L[[tau]]` and does not enlarge
the field. The client octic is already centered (`f=z^8+sum_{i=0}^6 a_i z^i`
after the `R_0` shear), so `C` has no `z^7` term.

**Monic square division is a polynomial automorphism over `Z[1/2]`.**
Write `C=z^8+C_6 z^6+C_5 z^5+C_4 z^4+C_3 z^3+C_2 z^2+C_1 z+C_0` and
`Q=z^4+q_2 z^2+q_1 z+q_0`. Expanding `Q^2` over `Z[q_2,q_1,q_0]` and
equating coefficients of `z^6,z^5,z^4` gives the unique solution

```text
q2 = C6/2,
q1 = C5/2,
q0 = (C4 - q2^2)/2,
Delta3 = C3 - 2 q2 q1,
Delta2 = C2 - q1^2 - 2 q2 q0,
Delta1 = C1 - 2 q1 q0,
Delta0 = C0 - q0^2.
```

The forward map is polynomial over `Z[1/2]`. The inverse is
`C=Q^2+Delta`, polynomial over `Z`. Uniqueness holds over every field of
characteristic not two: computing `Q` and `Delta` after a ramified
extension cannot produce a different remainder. Independent expansion of
five rational samples, including a generic `Q`-point with denominators,
recovers exactly these formulae and stays inside the field generated by
the `C_i`. Division by `2` is the only inversion; it is already licensed
by the ambient exact-`Q` client. Therefore every coefficient of `Q` and
of `Delta` lies in `L((tau))`.

What this does not do: it does not force the `C_i` to be power series
rather than Laurent series, and it does not by itself bound
`ord_tau(Delta)`. Poles of `A_i` at `tau=0` are allowed. The target
correctly names `L((tau))` rather than `L[[tau]]`.

The target's phrase “harmless finite constant or complete-local
extension” is only a licence to define `sigma` and the integer `H`. It
is not a licence to enlarge the coefficient field of `C` or `Delta`.
Section 2 of the target places those coefficients in `L((tau))` before
adjoining `sigma`. That order is load-bearing and is the order used here.

---

## Attack 2 — `sigma^3=Lambda` and `ord_sigma Delta=H` force `ord_tau Delta=alpha H/3`

**CONFIRMED.** Units, vector minima, and square-division cancellation do
not break the conversion.

**Units.** From `sigma^3=tau^alpha u(tau)` with `u(0)!=0` one has
`ord_tau(Lambda)=alpha` exactly. In characteristic not three, `X^3-u(0)`
is separable. A finite constant extension puts a cube root of `u(0)` in
the residue field; Hensel then lifts it uniquely to a unit of `L[[tau]]`
because the derivative `3X^2` is a unit at a nonzero cube root. The cube
root of `u` contributes valuation zero, so

```text
ord_tau(sigma) = alpha/3
```

as a `Q`-valued extension of `ord_tau`. The three choices of cube root
differ by `mu_3` and have the same valuation, so `H` is independent of
the choice. The odd twist `1+tau` is likewise a unit.

**Normalized discrete form, to avoid a `Q`-valued objection.** Let
`d=gcd(alpha,3)`, write `alpha=d a` and `3=d r` with `gcd(a,r)=1`, and
let `s` be a uniformizer of the totally ramified extension with

```text
ord_s(tau)=r=3/d,     ord_s(sigma)=a=alpha/d.
```

Then `ord_s(Delta)=H * (alpha/d)`. If the four coefficients of `Delta`
lie in `L((tau))`, each nonzero coefficient has `s`-valuation divisible
by `r=3/d`. The minimum of a nonempty finite set of such valuations is
still divisible by `3/d`. Hence `H alpha / d` is an integer multiple of
`3/d`, i.e. `3` divides `alpha H`, which is equivalent to
`ord_tau(Delta)=alpha H/3 in Z`. When `d=3` the extension is unramified
after the constant cube root of `u`, `sigma` itself lies in `L((tau))`,
and `3|alpha H` is automatic. When `d=1` one recovers `3|H`.

**Vector-valued minimum.** The normalized cell uses the unweighted
coefficient minimum: `ord_sigma(Delta)=min_i ord_sigma(Delta_i)`, the
same convention as Gate-A (`Delta=sigma^{17} N` with `N=n_3 z^3+...` and
`n_3` a unit). Each conversion `ord_s = (alpha/d) ord_sigma` is the same
positive constant on every component, so the minimum converts. There is
no cross-term in which two components of different ramified weights
could cancel: the four coefficients are separate elements of one field.

**Cancellation in the square division.** Any cancellation among monomials
in the formulae of Attack 1 takes place inside `L((tau))` and can only
raise some `ord_tau(Delta_i)`. Raising the minimum raises `H` relative
to a naive bound from the `C_i`; it cannot produce a non-integral
`tau`-valuation, and it cannot place a germ with exact declared order
`H` into `L((tau))` when `alpha H/3` is non-integral. Vanishing of the
whole remainder is excluded by `H<infinity`. Uniqueness of monic square
division blocks the fantasy that a ramified computation of `Q` could
cancel more leading terms than the already unique remainder over
`L((tau))`.

**Leading-form exactness.** The cell declares the order exactly `H`, not
at least `H`. If the leading vector `N_0` is nonzero in residue, there
is no extra vanishing after Hensel or after substituting a unit cube
root. Thus `ord_tau(Delta)` equals `alpha H/3`, not a strictly larger
rational with the same denominator.

---

## Attack 3 — the necessary condition is exactly `3|alpha H`; balanced ray

**CONFIRMED.** The condition is necessary and, on the leading valuation,
sharp. It is not a hidden stronger congruence, and it is not sufficient
for full series descent.

Necessity is Attack 2. Sharpness of the denominator: if `3` does not
divide `alpha H`, then `alpha H/3` is not an integer, so no nonzero
vector in `L((tau))^4` can have `sigma`-order `H`. No weaker arithmetic
condition (for instance `3|H` even when `3|alpha`, or `9|alpha H`) is
forced by the leading valuation alone.

On the balanced ray of Gate-A `(4.2)`–`(4.3)`,

```text
Lambda = tau^3 varrho,     varrho = tau * (unit),
```

one has `alpha=4` and `gcd(4,3)=1`, hence `3|H`. Direct values:

| `H` | `alpha H / 3` | `4H mod 3` | `3\|H` | descent of the leading term to `L((tau))` |
|---|---|---|---|---|
| 15 | 20 | 0 | yes | possible |
| 16 | `64/3` | 1 | no | impossible |
| 17 | `68/3` | 2 | no | impossible |
| 18 | 24 | 0 | yes | possible |

Equivalently with the common uniformizer `s` of the second proof,
`tau=s^3`, `sigma=s^4*(unit)`, one has `ord_s(Delta)=4H`. Membership of
the leading term in `L((s^3))` requires `3|4H`, hence `3|H`. The four
rows of the table are then `60,64,68,72`, of which only the first and
last are divisible by three.

The target's sentence “the next integral normalized normal order after
the compatible `H=15` cell is `H=18`” is a statement about the
congruence lattice `{H : 3|H}` on this ray. It does not assert that an
`H=15` or `H=18` rational germ exists. Compatibility of the leading
valuation is not inhabitability of the Newton cell.

The condition is not sufficient for descent of a whole series in
`sigma`. A series `sigma^H (n_0+n_1 sigma+...)` pulled back by
`sigma=s^4` lies in `L((s^3))` if and only if every exponent
`4(H+k)` with a nonzero coefficient is divisible by three, i.e. the
series is in fact a series in `Lambda=sigma^3` rather than a general
series in `sigma`. For `H=15` the leading monomial `sigma^{15}=s^{60}=tau^{20}`
does lie in `L((tau))`, while a generic next jet `sigma^{16}` does not.
The target claims only the necessary leading-valuation law (1.4), so
this stronger jet obstruction is a remark, not a missing hypothesis.

---

## Attack 4 — Gate-A `tau=s^3`, `varrho=s^3`, `sigma=s^4` is ramified; flatness does not descend it

**CONFIRMED.** The displayed lift is a ramified formal point. Flat toric
base change does not supply an omitted descent.

**The substitution is algebraically correct and ramified.** Gate-A `(4.3)`
sets `sigma=s^4`, `tau=s^3`, `varrho=s^3`. Then

```text
tau^3 varrho = s^9 s^3 = s^{12} = (s^4)^3 = sigma^3 = Lambda
```

exactly, both `tau` and `varrho` have positive order, and `R=1+s^3` is a
unit. The inverse of the odd-coefficient automorphism is
`B_even=C_even`, `B_odd=C_odd/R`, `j=J/R` as written. This exhibits a
map `Spec L[[s]] ->` (two-parameter source). It does not exhibit a map
from `Spec L[[tau]]` or from `Spec L[[tau,varrho]]`.

**`L((s^3))` versus `L((s^4))`.** Along this arc, `L((tau))=L((s^3))` and
the Gate-A coefficient series live in `L((sigma))=L((s^4))`. A monomial
`s^k` lies in both Laurent fields if and only if `3|k` and `4|k`, hence
if and only if `12|k`. Intersection of the two power-series rings is
`L[[s^{12}]]=L[[Lambda]]`. A genuine `H=17` remainder has

```text
Delta = sigma^{17} N = s^{68} (N_0 + s^4 N_1 + ...),
```

with `N_0` a unit in at least one coefficient (Gate-A `(2.4)`:
`n_3 mod sigma = m` a unit). Then `ord_s(Delta)=68`, and `68=22*3+2` is
not divisible by three, so no coefficient of `Delta` lies in `L((s^3))`.
This is the balanced-ray case of Attack 2 with no remaining room for
units or cancellation.

**Galois module, independent of valuations.** The cover `L((s))/L((s^3))`
is Galois of group `mu_3`, acting by `s |-> zeta_3 s`. This action fixes
`tau=s^3` and `varrho=s^3`, hence fixes the two-parameter base, and
sends `sigma=s^4` to `zeta_3^4 s^4 = zeta_3 sigma`. Therefore

```text
sigma^{17} |-> zeta_3^{17} sigma^{17} = zeta_3^2 sigma^{17}.
```

If `N` were a power series in `sigma` with nonzero constant term `n_0`,
invariance of `Delta` would require `n_0 = zeta_3^2 n_0`, hence `n_0=0`,
contradicting the unit leading form. So `Delta` is not
`mu_3`-invariant, hence is not a function of `(tau,varrho)`. The same
character `zeta_3^H` is trivial if and only if `3|H`, which is again
(1.4) on this ray.

**Flatness does not descend formal sections.** The one-parameter
reduction proves that

```text
Q[Lambda] -> Q[tau, varrho, (1+tau)^{-1}],    Lambda |-> tau^3 varrho
```

is torsion-free over a PID, hence flat, and that principal saturation by
`Lambda J` commutes with this extension. That is an equality of
algebraic boundary schemes in coefficient-load space, including
nilpotents. The same review of that reduction already records that a
ramified finite map such as `Q[t]->Q[x]`, `t |-> x^2`, is likewise flat:
ramification is not an obstruction to flatness, and therefore flatness
is not a descent criterion for formal arcs.

A Gate-A solution is a section over `L[[sigma]]` with `Lambda=sigma^3`,
not a section over `L[[Lambda]]`. Pulling it back along
`Lambda=tau^3 varrho` produces a commutative square of complete local
rings whose right-hand vertical arrow is `L[[s]]/L[[tau]]` of degree
three. The geometric point is a degree-three point of the two-parameter
scheme over `L((tau))` along `varrho=tau`, not an `L((tau))`-rational
point. Pushforward of `Spec L[[s]]` is likewise a degree-three cycle,
not a descended germ.

Uniqueness of the normalized IFT over `L[[sigma]]` does not create a
descended solution. A descended solution would base-change to a
ramified solution with `ord_s(Delta)` divisible by three. The unique
`H=17` lift has `ord_s=68`, so it cannot be that base change. Uniqueness
on the ramified disc therefore reinforces the obstruction: there is a
unique ramified formal point in the cell, and no `L((tau))` point that
maps to it.

**What Gate-A actually claimed.** Gate-A `(4.1)` already says “after
finite ramification” and Section 5 already names a “literal
**source-row** survivor, not yet a polynomial Keller pair”. Section 6
already withholds “the invariant rational coefficient functions”. The
target's quarantine at ramified formal source-row scope is therefore a
correct restriction of the accessibility reading of Gate-A `(4.1)`, not
a refutation of the ramified IFT or of the two-sided affine coordinate
change. The phrase “literal rational-source accessibility conclusion
withdrawn on the balanced ray” is accurate as a scope correction on
that ray. It would be a misreading of Gate-A to treat the ramified IFT
itself as refuted; the target does not do so.

---

## Attack 5 — scope firewall

**CONFIRMED.** The target does not overclaim.

Integer strict slopes only, `alpha>3`. The bound `alpha>3` is exactly
strictness of `varrho=tau^{alpha-3}*(unit)`: positive order of `varrho`
forces `alpha>=4`. Fractional slopes are not classified. The same
normalized `H` on a different integer slope with `3|alpha H` is not
excluded. In particular `H=17` is congruence-compatible on every
integer slope with `3|alpha` (the first two are `alpha=6` and
`alpha=9`). Other positive rational splittings of
`v(Lambda)=3 v(tau)+v(varrho)`, which Gate-A `(4.1)` already declines to
classify, are not killed by this theorem when the congruence holds.

The normalized complete-local H17/q7/a3 solution over `L((s))`, its
finite-grade identities, and any fixed-branch prolongation remain
untouched: they are statements over the ramified disc. Finite Taylor
polynomiality, the `H=18` predecessor, other source-fan cells, order
two, `(8,12)`, maximum twelve, and JC2 are explicitly out of scope and
are not used. No CAS identity is claimed.

A parenthetical that is not a hole: the theorem never writes
“characteristic zero” as a numbered hypothesis. Division by `2` in the
square map and the separable cube of a unit use `2!=0` and `3!=0`. Both
are the ambient ring of the charged `U=2` client. Residue
characteristics two and three are outside the written source, not a
defect of (1.4).

---

## Smallest counterexample

None. The theorem's numbered claims survive.

The smallest explicit descent-obstruction witness *for* the theorem, on
the balanced ray, is the leading monomial of a normalized `H=16`
remainder:

```text
alpha=4, H=16,    sigma^{16} = s^{64} = tau^{21} * s,
```

which does not lie in `L((s^3))`, equivalently `4*16/3=64/3 not in Z`.
The named Gate-A cell `H=17` is the next such witness,
`sigma^{17}=s^{68}=tau^{22} * s^2`. Neither is a counterexample to
(1.4); both are the content of (1.4) on this ray.

No smaller integer pair `(alpha,H)` with `alpha>3` and `H<infinity` is
required. The pair `(4,16)` is the first incompatible order after the
congruence-compatible `H=15` cell named by the target.

---

CONFIRMED
