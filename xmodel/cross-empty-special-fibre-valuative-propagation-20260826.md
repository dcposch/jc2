# Empty special fibre propagates across every positive base valuation

Date: 2026-08-26

Status: **ELEMENTARY ALGEBRAIC LEMMA AND CAMPAIGN INTERFACE DESIGN.  NO
SQUARE, TD6, D1, MAXIMUM-TWELVE, OR JC2 VERDICT.**

## 1. The finite-type lemma

Let `k` be a field, let `t` be a base parameter, and let

```text
B = S^(-1) k[t,x1,...,xn]/I
```

be one raw source chart.  The factors in `S` are exactly the registered chart
units; in particular no power of `t` is inverted.  If the scheme-theoretic
special fibre is empty,

```text
B/tB = 0,                                           (1)
```

then `t` is a unit in `B`.  Indeed, (1) says

```text
1 = t*b                                             (2)
```

for some `b in B`.  Consequently there is no homomorphism

```text
B -> R
```

to a local ring `R` which sends every element of `S` to a unit and sends `t`
to the maximal ideal.  In particular there is no source-typed formal arc into
this chart with `ord(t)>0`, over a DVR or after finite ramification.

This is stronger than checking one or several moving-`t` coefficients.  Once
(1) is proved in the *same total raw chart*, all positive integral and rational
orders of `t` are excluded at once.

### Proof

Apply the proposed homomorphism to (2).  The product of an element of the
maximal ideal with any element of a local ring remains in the maximal ideal,
whereas `1` does not.  This is a contradiction.  Equivalently, a ring map
must send the unit `t` of `B` to a unit of `R`.

## 2. Exact certificate form

For replay and review, (1) should be represented by an explicit localized
identity

```text
s = sum_i h_i*f_i + t*h,                            (3)
```

where `s in S`, the `f_i` are complete raw source rows, and every denominator
of `h_i,h` is a product of registered factors in `S`.  Dividing (3) by `s`
in `B` gives (2).  A radical computation without a recoverable identity is a
routing result, not the desired certificate.

If the special fibre is covered by finitely many principal or normalized
charts, it is enough to prove (3) on every chart, provided that the cover and
all overlaps are exact.  A formal arc into a reduced finite-type component
lifts to its normalization after passing to the integral closure of its DVR
and, if necessary, a finite extension of the fraction field.  Thus normalized
chart units can exclude arcs, but only after all of the following are proved:

1. the normalization maps are finite and cover every reduced component of
   the special fibre;
2. the chosen principal opens cover every permitted leading-unit support;
3. embedded or nilpotent directions are either killed by raw equations on a
   DVR point or routed to explicit higher-contact charts;
4. the normalized equations are pullbacks of the same total raw source ideal,
   not equations from an analogous or separately rescaled model;
5. all zero sections excluded from the leading-unit opens have named
   receivers.

Without these five items, a successful calculation at `t=0` does not exclude
arcs in a missing Rees cone.

## 3. Square-branch composition opportunity

Take `t=p` only after constructing one total correction-aware square chart in
which `p` remains a genuine base coordinate.  On the reviewed half-weight
special fibre with `k0!=0`, the raw grade-ten support has:

```text
D(rs):                  the cusp chart,
V(rs) intersect D(cs):  the odd-R chart,
V(rs,cs):               the R-zero/higher-contact receiver.
```

The odd chart is already hostile-review confirmed empty.  The cusp chart now
has a dual-field producer unit at grade twelve and is entering hostile review.
Those two results do **not** yet prove (1): the `R=0` receiver retains the
`A` direction and higher-contact/nilpotent directions.  A promising third
chart is the exact `p=0,R=C=0,A!=0` cubic receiver.  Its first nominal term is

```text
-(1/16) A^3/L^3 = -(1/16) A^3/z^6,
```

so complete polynomiality would force `z^6 | A^3`; for `deg(A)<=1` this
forces `A=0`.  This is only a candidate until the complete source/Faber rows,
connections, targets, and all terms tied at the same valuation are replayed.

If the cusp, odd, and every `R=0` receiver furnish an exact Cech/normalized
cover with identities (3), then every positive-valuation `p` arc *in that
same total Rees chart* dies automatically.  Separate clients for `p=tau^m`
at every `m` should then be retired.  Other square Rees cones, positive-order
loads, `k0=0`, and the exact-square higher-contact section remain separate.

## 4. TD6 and D1 applications

The same lemma separates genuine divisor geometry from repeated jet work.

- **TD6.**  If an original-source CURRENT chart over a factor parameter `F`,
  `G`, or `L` has an exact empty special fibre, then all arcs approaching that
  divisor inside the chart are excluded.  The current V82QST2 `F=0` endpoint
  does not qualify: its elimination coefficients introduce unregistered
  denominator divisors and explicitly report
  `F_RAW_registered_generic_open_killed=false`.
- **D1.**  If the weighted triple-root special fibre is covered and empty in
  the same discriminant family that contains the smooth chart, then every
  positive root-axis valuation is excluded without one client per valuation.
  The reviewed smooth `D(a)` obstruction alone does not establish the needed
  special-fibre identity.

## 5. Minimal implementation contract

Extend each divisor/special-fibre producer with a `VALUATIVE_PROPAGATION`
block which prints:

1. the hash of the total raw family before setting `t=0`;
2. the exact specialization map and proof that `t` was not inverted;
3. the finite chart/normalization cover and overlap hashes;
4. one identity of the form (3) per chart;
5. a routing table for every complement and zero section;
6. a negative control with one omitted chart, which must fail coverage.

The theorem consumer may then replace an infinite moving-base jet queue by a
single implication `special_fibre_empty => ord(t)=0` at that exact chart ID.
It must not propagate across a different filtration, source presentation,
normalization, or support localization.

## 6. Scope firewall

This note proves only the elementary finite-type implication (1)--(2).  It
does not prove that any current campaign special fibre is completely empty,
that the displayed square charts form the required total cover, that the
candidate `A^3/z^6` receiver survives the complete source rows, or that the
TD6/D1 divisor families satisfy the hypotheses.  It supplies a precise way
to turn future exact special-fibre coverage into all-positive-valuation
coverage without a jet-by-jet induction.
