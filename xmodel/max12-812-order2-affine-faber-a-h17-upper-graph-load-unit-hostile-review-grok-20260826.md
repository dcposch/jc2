# Hostile review — affine-Faber `A` H17 upper affine-graph load unit

| Field | Value |
|---|---|
| Charged target | `xmodel/max12-812-order2-affine-faber-a-h17-upper-graph-load-unit-theorem-20260826.md` |
| Target SHA-256 | `773b4d773cee9cc967645b6c67417d7d60c3058d2e5ae898f06d12b4863800fc` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none inside the internal H17 wall `(1.1)` on `D(kappa*a*E)` for `7<q<17/2`; `q=7`, `q>=17/2`, `kappa*a*E=0`, other load graphs, literal source/total-Rees, factor-degenerate, order two, max12, and JC2 are identified receivers, not holes |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile reconstruction from frozen exact-`Q` abstract supports. Different model family from the producer. No producer status line, no charged `PASS`/`UNIT`/`ENDPOINT` token, no validator string, this prompt, and no V10 scope string is evidence |
| Method | SHA-256 of every charged pin and every freeze/evidence/results row before reading producer verdict prose; independent `Hseries=G-32F` over `Q` on all 663+665 parent monomials; independent polynomial substitution `K6=(15/32)K10 E^2`, `K2=(15/256)K10 E^4`; comparison of all 468 reduced affine lines and of all 630 source lines, including the three centrally cancelled clusters; F65521 reduction checked only as software control |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the six files named in the review
prompt match those pins. Every freeze, evidence, and results row of the
V10 manifests matches the corresponding on-disk bytes. Producer verdict
language, `PASS-A-H17-UPPER-GRAPH-LOAD-UNIT-V10`,
`PASS_EXACT_GRAPH_LOAD_UNIT`, `A_H17_UPPER_GRAPH_*` print tokens, and
the V10 scope string
`INTERNAL_AFFINE_GRAPH_SPECIAL_FIBRE_...` were not used as
characteristic-zero evidence. Exact `Q` is the mathematical lane.
Characteristic 65521 is a software and support control only. No file
other than this review was written. The target, producers, shared
ledgers, and `jc2-lean` were not edited.

---

## Verdict

**CONFIRMED.**

Work in characteristic zero, in the internal normalized
moving-discriminant graph coordinates
`(J,K2,K6,K10,S0,S1,R0,R1,Y,X,a,lambda,M,E)`, after a common ramified
base change, on the H17 equality wall

```text
v(lambda)=17,  v(X)=v(Y)=q,  v(Ri)=v(Si)=2q,
v(a)=17-2q,    v(K10)=v(K6)=v(K2)=42,  v(J)=57,
v(E)=v(M)=0,
```

and on the positive-contact affine load graph

```text
K10 = t^42 kappa,
K6  = t^42 ((15/32) kappa E^2 + d6),
K2  = t^42 ((15/256) kappa E^4 + d2),
v(d6)>0, v(d2)>0.
```

Independently reconstructed `Hseries = G-32F` is a 630-term polynomial
over `Q`. The exact special-fibre substitution `d6=d2=0` yields 468
nonzero monomials, with unique least term throughout `7<q<17/2`

```text
(5/4) kappa a^3 E^7
```

of affine weight `93-6q`. The coefficient `5/4` is a unit in
characteristic zero, and the leading source coefficient is a unit on
`D(kappa*a*E)`. Every one of the other 467 reduced monomials has
strictly larger weight on that open interval. Every source monomial of
the unreduced 630-term polynomial, including the three clusters that
cancel identically after substitution, has special-fibre weight at least
`93-6q` on the same interval, with equality only on the three load-cluster
partners that leave the displayed unit. Any expansion term that carries
at least one factor of `d6` or `d2` therefore has strict excess over
`93-6q`, and cannot cancel or precede the unique initial term.

If every raw ordinary-Faber row vanished as a series, the combination
`Hseries` would vanish, contradicting the unique unit. At `q=7` the same
monomial ties exactly `-2 lambda^3 M^3 E^2`; that boundary is excluded.
The statement is internal to this graph and does not close the firewalled
receivers.

---

## Hashes and charged artifacts

Recomputed SHA-256, all matching the required pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| charged theorem | `773b4d773cee9cc967645b6c67417d7d60c3058d2e5ae898f06d12b4863800fc` | immutable target |
| V10 `RESULT.md` | `37d43ffdf7098028e02a79509461b6e06777e203ab04b57ee1d0c5f3801d5f57` | charged; navigation only |
| V10 `EVIDENCE.sha256` | `b9c11be5a6821d31826a947f8c73562c1f6447423894d2718ff7020fb178e909` | charged |
| V10 `FREEZE.sha256` | `7b2534e945398a31e8ce5111786e0bad45fc0ca125354178242189de4227891c` | charged |
| V10 `RESULTS.sha256` | `34d701dc7b33125774a89a11e47bd1284c21f8650cffaaf085c14e589f189553` | charged |
| V10 exact-`Q` `hseries_affine_graph_support.json` | `ae18b65c01e0b7381c6944754a1bb9690ed006255a922399716ef2cc99bc550e` | exact-`Q` reduced-support custody |

Parent freeze pins independently rehashed, used only as algebra sources:

| Artifact | SHA-256 | Role |
|---|---|---|
| V4 exact-`Q` `abstract_functional_support.json` | `9ee52ed12c5ca75b0f36fdaf4292be6165d6a4380550c87faab3a654b23306bc` | exact-`Q` `F` custody |
| V6 exact-`Q` `abstract_secondary_support.json` | `357829d292056e823c102446b8e95f5822dad961859e832a689160bca1e3fbcd` | exact-`Q` `G` custody |
| V4 F65521 `abstract_functional_support.json` | `b6eafc795464b7e7e077df2b2ea0fd58d7c963b14988e3d5322b312cafdf19a9` | software control only |
| V6 F65521 `abstract_secondary_support.json` | `742783f9679cea0e9bcb946d16d6aeaa6104f99e638283a1661c8929794dd197` | software control only |
| frozen tails `tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` | complete 10-slot ordinary-Faber tails |
| V10 analyzer `analyze_upper_graph_v10.py` | `7f871d224aedaee4f6558c3d8fb956bd09afa3bff0099ff56aa399b510e34f9f` | freeze pin; inequalities rederived, not trusted |

Every relative path in V10 `EVIDENCE.sha256` (16 rows), `FREEZE.sha256`
(8 rows), and `RESULTS.sha256` (3 rows) rehashes to the recorded digest.
Independently serialized canonical JSON of the 468-term reduced
polynomial is byte-identical to the charged exact-`Q` support file.

The r6d copy of that JSON has the same digest; its `result.json` differs
only by lane tag and is not a characteristic-zero identity.

---

## Attack 1 — independent substitution, 468 terms, coefficient `5/4`

The frozen tails are 10-slot polynomials in
`(B0,B1,B2,B3,B4,B5,B6,K10,K6,K2)` with counts

```text
row 1: 36,  row 2: 54,  row 3: 58,  row 4: 81,
row 5: 89,  row 6: 120, row 7: 131.
```

Targets are attached afterwards. On the affine chart `tau=0`,

```text
P1: 0,  P2: mu2,  P3: 0,  P4: mu4,
P5: 0,  P6: mu6,  P7: -J/4.
```

The parent exact-`Q` supports are the complete graph polynomials of the
odd-row combinations, not H16 grade-48 slices: 663 terms in `F`, 665
terms in `G`, maximum `a`-degree 17. They are built by substituting the
moving-discriminant graph

```text
qp = E - 6 a^2,
qc = 2 a (4 a^2 - E) + X + R1,
qr = a^2 (E - 3 a^2) + R0 - a (X + R1),
n3 = lambda M,
n2 = lambda a M,
n1 = lambda ((E - 5 a^2) M + Y + S1),
n0 = lambda (-a (E - 3 a^2) M - a Y + (1/2) M X + S0 - a S1),
```

into the factor list `B0=qr^2+n0`, `B1=2 qc qr+n1`, `B2=qc^2+2 qp qr+n2`,
`B3=2 qp qc+n3`, `B4=qp^2+2 qr`, `B5=2 qc`, `B6=2 qp`, then `K10,K6,K2`,
and forming

```text
F = P7_tails - E^2 P3/32 + E^3 P1/64 - J/4,
G = E^2 P3 + 16 E P5 + 96 P7_tails - 24 J.
```

The `-24 J` is `96*(-J/4)`, not a second tail target. Independent
subtraction over `Q` of every monomial in the union produces 630
nonzero terms and 35 identical cancellations `G=32F`. Two monomials
occur only in `G`; none occur only in `F`. The `J` contribution is
`-24 J - 32*(-J/4) = -16 J`, already the image of `64*(-J/4)` inside
`64 P7`. The displayed expansion

```text
G - 32 F = 2 E^2 P3 + 16 E P5 + 64 P7 - E^3 P1/2
```

is a polynomial identity. All 630 denominators are powers of two.

Exact substitution `K6=(15/32)K10 E^2`, `K2=(15/256)K10 E^4` is the
monomial map

```text
(K2,K6,K10,E)  |->  (0, 0, K10+K2+K6, E+4 K2+2 K6)
```

with coefficient factor `(15/256)^{k2} (15/32)^{k6}`. It produces 471
reduced clusters, of which 3 sum to zero and 468 are nonzero. No `K2`
or `K6` remains. Independently recomputed canonical JSON SHA-256 is

```text
ae18b65c01e0b7381c6944754a1bb9690ed006255a922399716ef2cc99bc550e.
```

Zero coefficient mismatches against the charged support file.

The load exponent vector `(K10,a,E)=(1,3,7)` and all other exponents
zero has three source preimages:

```text
K10 a^3 E^7 :  155/16
K6  a^3 E^5 :  -23
K2  a^3 E^3 :   40
```

and reduced coefficient

```text
155/16 + (-23)(15/32) + 40(15/256)
  = 2480/256 - 2760/256 + 600/256
  = 320/256
  = 5/4.
```

The intrinsic exponent vector `(lambda,M,E)=(3,3,2)` is untouched by
the substitution and has coefficient `-2`, recovered as
`[G]-32[F] = -5/2 + 32/64 = -2`.

F65521 has identical 630-term support for `Hseries` and identical
468-term support after the modular graph map, with every exact-`Q`
coefficient reducing to the modular one. That agreement is a software
control. It is not a characteristic-zero proof.

---

## Attack 2 — every reduced affine weight under H17

On the wall schedule the affine weight of a reduced monomial is the
linear function `const + slope·q` with

```text
const = 57 e_J + 42 e_K10 + 17 (e_a + e_lambda),
slope = 2 (e_S0+e_S1+e_R0+e_R1) + (e_Y+e_X) - 2 e_a.
```

(`K2` and `K6` have already been folded into `K10` and `E`, and
`v(E)=v(M)=0`.) The load monomial has line `93-6q`. Direct comparison
of all 467 other reduced monomials against that line:

- same slope as the load: only the load itself;
- competitors that could undercut from the left (`dslope>0` and bound
  `>7`): none;
- competitors that could undercut from the right (`dslope<0` and bound
  `<17/2`): none;
- strictly negative difference on the closed interval `[7,17/2]`: none.

The eight monomials that meet the load at an endpoint, and nowhere
inside the open interval, are:

```text
q=7,     weight 51:
  -2      lambda^3 M^3 E^2          51
  5/4     K10 a^3 E^7               93-6q

q=17/2,  weight 42:
  5/4     K10 a^3 E^7               93-6q
  -899/4  K10 a^5 E^6               127-10q
  55805/8 K10 a^7 E^5               161-14q
  -352315/4 K10 a^9 E^4             195-18q
  2272445/4 K10 a^11 E^3            229-22q
  -1990105  K10 a^13 E^2            263-26q
  3616184   K10 a^15 E              297-30q
  -2676960  K10 a^17                331-34q
```

At `q=7` there are exactly two ties: the load and
`-2 lambda^3 M^3 E^2`. No third reduced monomial meets weight 51. (The
three unreduced loaded partners `K10 a^3 E^7`, `K6 a^3 E^5`,
`K2 a^3 E^3` have already been combined into the single reduced
monomial of coefficient `5/4`.)

The uniqueness interval of the load as least reduced monomial, on this
wall schedule, is therefore exactly `7<q<17/2`. For `q<7` the intrinsic
term of weight 51 is strictly smaller. For `q>17/2` the wall formula
makes `v(a)` negative and the higher odd powers of `a` undercut. Sample
rationals `q=71/10, 29/4, 22/3, 15/2, 8, 33/4, 42/5, 31/4` each have
unique minimum weight `93-6q`, attained only at `(5/4) K10 a^3 E^7`.
Rational `q` after a common ramification `s=tau^d` does not change the
open interval: every comparison is linear in the ratio `q`.

Interior excess to the next family is at least 3, attained as `q\to 7+`
by the three lines `68-2q`

```text
-3  R1 a^2 lambda^2 M^2 E^2,
 6  S0 a^2 lambda^2 M E^2,
 6  Y X a^2 lambda^2 M E.
```

As `q\to 17/2-` the excess to `K10 a^5 E^6` tends to 0 from above. On
the open interval it remains strictly positive.

---

## Attack 3 — positive-deviation composition, including central cancellation

Write `K6 = t^{42}((15/32) kappa E^2 + d6)` and
`K2 = t^{42}((15/256) kappa E^4 + d2)` with `v(d6),v(d2)>0`, and keep
the same moving `E` that appears in `Hseries`. A source monomial
`K2^{p} K6^{q} K10^{r} · rest` expands by the binomial theorem in
`(spec2+d2)^p (spec6+d6)^q`. Every summand that carries at least one
`d2` or `d6` has valuation strictly larger than that source monomial's
special-fibre valuation, because `v(t^{42} d6)=42+v(d6)>42=v(K6_spec)`
and likewise for `d2`. This comparison is per source monomial. The
only way a deviation term could still meet or undercut the unique
reduced minimum `W_min=93-6q` is if some source monomial had
special-fibre weight strictly below `W_min` and then cancelled in the
special fibre.

That does not occur. Using the unreduced weight
`57 e_J + 42(e_K2+e_K6+e_K10) + 17(e_a+e_lambda)` plus the same slope
as above, none of the 630 source monomials undercuts `93-6q` on the
closed interval `[7,17/2]`. Nineteen source monomials touch an
endpoint; on the open interval they are strictly above, except the
three load-cluster partners, which have exactly the load line
`93-6q` for every `q`:

```text
K10 a^3 E^7,   K6 a^3 E^5,   K2 a^3 E^3.
```

Those three do not cancel. Their special-fibre leftover is the unit
`5/4`. The associated deviation terms are

```text
-23 t^{42} d6 a^3 E^5,     40 t^{42} d2 a^3 E^3,
```

of weights `93-6q+v(d6)` and `93-6q+v(d2)`, plus the mixed
`d6 d2` term from any higher binomial, which is still higher. They
cannot cancel `(5/4) kappa a^3 E^7`.

Three reduced clusters cancel identically. Each is a three-term
`K10/K6/K2` identity of common weight strictly above `W_min` on
`7<q<17/2`:

```text
K10 R0 a E^6     59        excess at q=7 is 8,  at q=17/2 is 17
K10 R0 X E^5     42+3q     excess at q=7 is 12, at q=17/2 is 51/2
K10 R0 R1 E^5    42+4q     excess at q=7 is 19, at q=17/2 is 34
```

Coefficient sums:

```text
15/16 + (-3)(15/32) + 8(15/256)     = 0,
-15/32 + (3/2)(15/32) + (-4)(15/256) = 0,
-15/32 + (3/2)(15/32) + (-4)(15/256) = 0.
```

The special-fibre contribution of each cluster is the zero polynomial,
not a term of valuation below `W_min`. Deviation-bearing leftovers from
those clusters live at the cancelled weight plus `v(d)>0`, hence
strictly above `59`, `42+3q`, or `42+4q`, all of which already exceed
`93-6q` on the open interval. Even `v(d)=0` would not undercut the
load; the actual hypothesis `v(d)>0` is more than is needed for these
three clusters.

The 124 surviving multi-source clusters have mixed-sign special-fibre
contributions, so they are partial cancellations. Each such cluster
occupies a single affine line, equal to every source partner's
special-fibre line. Attack 2 already compared all 468 surviving lines;
every one other than the load is strictly above `W_min` on the open
interval. Partial cancellation does not create a new line, and does not
create a below-minimum residue. The leftover coefficient is nonzero by
construction of the 468-term support.

The theorem's prose that "the substitution is polynomial and both
deviations have positive valuation" is therefore correct on this
support, including terms created by central cancellation. It does not
need an extra hypothesis on `d6,d2` beyond `v(d6),v(d2)>0` in the
completed local ring of the arc. Localization `D(kappa*a*E)` may invert
`a`, but the valuation hypothesis already records the total order of
each remainder along the arc.

The charged V10 run is special-fibre only. That is a custody fact, not
a hole in the theorem: the composition is a finite binomial expansion
plus the 630-line comparison just recorded, not a second machine
identity.

---

## Attack 4 — raw-row signs, completeness, ramification, localization, jets

`Hseries` is a series-linear combination of the odd raw rows with
coefficients of valuation zero on `D(E)`:

```text
2 E^2,    16 E,    64,    -E^3/2.
```

Each is a unit times a non-negative power of the unit `E`. The target
`-J/4` in `P7` contributes the single term `-16 J` to `Hseries`, of
weight 57. If every raw ordinary-Faber row vanished as a series, every
such combination would vanish, including `Hseries` after the graph
substitution. A weaker hypothesis that only the exact grade `93-6q`
raw coefficients vanish, with lower coefficients free, would not kill
the moving-`E` convolutions; that weaker statement is not claimed.

Target and load completeness of the reduced polynomial:

- `J` occurs as the single term `-16 J`, weight 57, slope 0. On
  `7<q<17/2` one has `42 < 93-6q < 51`, so `57` is strictly above the
  unique minimum.
- Source load counts in the 630-term polynomial: `K10` 385, `K6` 127,
  `K2` 32, together 544; 86 terms carry no load. After substitution,
  382 reduced monomials carry `K10` and 86 carry none, plus the three
  identically cancelled clusters. No load monomial of `F` or `G` that
  survives `G-32F` is omitted from the 468-term comparison.
- No `mu`-target belongs to `P1,P3,P5,P7`. The even rows `P2,P4,P6` are
  not summands of `Hseries`. Simultaneous vanishing of all seven raw
  rows implies vanishing of the four odd rows, hence of `Hseries`. Even
  rows are not needed for the contradiction.

Characteristic zero is required: Faber denominators and the combinations
`F,G` involve `32,64`, and the unit is `5/4`. A complete DVR of residue
characteristic zero inverts `2` and `5`.

Localization `D(kappa*a*E)` is exactly the open on which the leading
source coefficient `(5/4) kappa_0 a_0^3 E_0^7` is a unit. Here
`kappa_0`, `a_0`, and `E_0` are the leading coefficients after
ramification, with `v(a)=17-2q` finite and `v(E)=0`. The open does not
need `M` or `lambda`: the unique initial monomial does not use them.
On `kappa=0`, `a=0`, or `E=0` the identity is `0=0` and supplies no
obstruction; those loci are excluded, not missing.

Moving `E` and `a` jets cannot tie the initial term on the wall
schedule. The 468-term polynomial is already written in the full
coordinates `E` and `a`, not in their leadings. Substituting

```text
a = a_0 t^{17-2q} (1 + higher),     E = E_0 (1 + higher)
```

multiplies every monomial by a unit series of valuation zero plus
strictly positive valuation. No jet can lower an abstract monomial.
No jet can cancel the unique weight-`93-6q` leading coefficient,
because:

- nothing in the 468-term support has leading weight `< 93-6q` on the
  open interval, so no jet from below can fill a gap to `W_min`;
- `v(E)=0` does not create a hidden same-weight partner: every
  distinct `E`-power is already a distinct monomial in the 468, and
  the unique monomial of weight `93-6q` is `K10 a^3 E^7`;
- `v(M)=0` likewise: no `K10 a^3 E^7 M^k` for `k>0` is present.

A jet that drops a coordinate *below* the wall is a different chamber
(complements strictly below `2q`, loads strictly below 42, `v(a)` off
`17-2q`, `q=0`, `E=0`). Those are identified receivers.

---

## Attack 5 — scope, strongest licensed theorem, smallest defect

The strongest licensed theorem is the charged statement, internal to
the normalized H17 affine-Faber graph with the positive-contact load
congruences `(1.1)`:

on `D(kappa*a*E)`, for every rational `7<q<17/2` after a common
ramification, simultaneous vanishing of the seven raw ordinary-Faber
rows is impossible.

Smallest defect: none inside that statement. The uniqueness interval
is sharp, the coefficient `5/4` is exact, the `q=7` tie-set is exactly
two reduced monomials, and the deviation expansion does not undercut
the unit, including at the three centrally cancelled clusters.

The theorem does not prove access to `(1.1)` from a literal source or
total-Rees chart. It does not resolve `q=7`, `q>=17/2`, `kappa*a*E=0`,
another graph or load schedule, terminal/Taylor strata, factor-
degenerate fibres, order two, `(8,12)`, maximum twelve, or JC2. Those
are firewalled receivers, not holes in `(1.1)--(1.2)`.

CONFIRMED
