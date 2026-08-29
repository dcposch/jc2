# Hostile review — delayed-load affine-Faber `A` valuative composition

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-affine-faber-a-delayed-load-valuative-composition-theorem-20260826.md` |
| Charged theorem | SHA-256 `fef0524a91c239b9086df8377e0b1270430b2fb164915eb8286bf52f9508cf32` |
| Charged identity review | `xmodel/max12-812-order2-affine-faber-a-formal-weighted-h3-h5-hostile-review-grok-20260826.md` = `7349330c903e7a336738792324d63570fd0f14252c20754337c6c6f801fa1cf5` |
| Charged freeze | `FREEZE.sha256` = `0ef7cfc84691c5fa466e98cf76f942d6bcd217547d0eb91b0f3860240da8eae5` |
| Charged evidence | `EVIDENCE.sha256` = `86883cc16a48e0ee4b4a1ea01844cedbdd212eb41414fe918f641d6654582f48` |
| Charged result | `RESULT.md` = `5736a3b00ec6e1b74b43c5112b8fadccf340b98558854b63ddd6ca9042d8370d` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing valuation face | none inside the weighted exceptional neighbourhood stated below; `q=0` and `0<v(a)<5` are earlier faces with identified receivers, not holes in that neighbourhood |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation of the valuative composition. Different model family from the producer. No producer status line, no charged `CONFIRMED`/`PASS`/`UNIT`/`ENDPOINT` token, and no validator string is evidence |
| Method | SHA-256 of every charged pin; hand expansion of (2.1)--(2.3); linearization of `(3/8)N^2/Q` at the moving double root; substitution of the frozen complete ordinary-Faber tails into the exact delayed `A` chart, independently of the formal-weighted producer; hand identities on the extracted first faces. The already confirmed polynomial identity is consumed only after the weight bounds are licensed. Characteristic 65521 was not used as characteristic-zero algebra |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the four files named in the review
prompt match those pins. Independently recomputed SHA-256 of `RESULT.md`
matches the identity review's charged result pin. Producer verdict
language, `A_FWH35_*` tokens, and both validator `PASS_*` strings were
not used as characteristic-zero evidence. Exact `Q` is the mathematical
lane for the parent identity; a finite field is at most a software
control. The composition theorem was not inferred from the identity
alone: sections 2--4 below license the chart, the complement bound, and
the `q<6` face from the coefficient ring and the complete tails, and only
then is the polynomial congruence substituted. No file other than this
review was written. `jc2-lean` and shared ledgers were not touched.

---

## Verdict

**CONFIRMED.**

On the delayed-load ray `k10=Lambda^{12} K10`, `k6=Lambda^8 K6`,
`k2=Lambda^4 K2`, after the ramification `Lambda=sigma^3` that extracts
the normal scale `sigma^{15} lam`, work in the formal neighbourhood of
the repeated-root affine-Faber point inside `D(p*m*K10)`, with chart
weights `v(a)>=5` and `q=min(v(U),v(V))>0`. Equations (2.1) and (2.3)
are inverse regular maps on `D(M)`, hence a coefficient-coordinate
isomorphism of the unique seven-tuple `(a,E,U,R0,M,V,W0)`. Extra
`(R1,S1)` are a non-unique splitting of that isomorphism; existence of
some splitting is all the valuative argument uses. The linear
complementary polar part of `(3/8)N^2/Q` is exactly (3.1). On solutions,
either that polar part supplies a unit pivot, or every genuine complement
starts at valuation at least `2q`. The four unloaded ordinary rows at
grade `30+2q` reconstruct from the complete tails as (4.1); every
rational `0<q<6` is empty on `D(p*m)`. After those bounds, the confirmed
polynomial identity kills every `q>=6` arc that already lies on the
chart, including unequal and ramified orders and `q=infinity`. Loads and
targets cannot reach the direct-unit coefficient through grade 45. This
is an internal affine-Faber composition, not a total-Rees or raw-source
atlas theorem.

**CONFIRMED**

---

## Hashes and charged artifacts

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| composition theorem | `fef0524a91c239b9086df8377e0b1270430b2fb164915eb8286bf52f9508cf32` | immutable provisional theorem (matches required pin) |
| identity hostile review | `7349330c903e7a336738792324d63570fd0f14252c20754337c6c6f801fa1cf5` | charged parent identity review (matches required pin) |
| `.../FREEZE.sha256` | `0ef7cfc84691c5fa466e98cf76f942d6bcd217547d0eb91b0f3860240da8eae5` | freeze manifest (matches required pin) |
| `.../EVIDENCE.sha256` | `86883cc16a48e0ee4b4a1ea01844cedbdd212eb41414fe918f641d6654582f48` | evidence manifest (matches required pin) |
| `.../RESULT.md` | `5736a3b00ec6e1b74b43c5112b8fadccf340b98558854b63ddd6ca9042d8370d` | parent identity result (matches identity-review pin) |
| `.../RESULTS.sha256` | `1946cec19e71fcce5b7a38a68125362a158bb589c61347b196d36bb6cdc62fbf` | results manifest |
| `.../REGISTRATION.md` | `e47cd54dcf2a88c37fbb6239f11f56f04666188527edeb532a4809c9dac64fd6` | identity scope; firewall, not algebra |
| frozen `tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` | complete ordinary-Faber tails used to rebuild (4.1) |
| V2 direct-unit addendum | `78766c9df5dbf95fad5bdff531657f58cb7445e30575a58a59cec656b00d9a63` | claimed raw congruences of the parent identity |
| first-normal UFD V2 | `4c9d9cfc58eb4ca2a33c9bf83beb485c15f0796fa36d2ffe4826c3fdeeac374d` | family `D` closed point; `q=0` receiver |
| one-parameter Rees reduction | `5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b` | affine-linearity of the three lower loads |
| delayed-load source (1.1) | `9419c08b4be09fee8ecae9b73c8c9c610770a7166e17a973251312d28b69a695` | load/target timing; not used as an `A`-exclusion |
| exact-`Q` identity stdout | `4fa84c7587556d43f9441ac68bfbb6c6f7577a39ea9e58e6e1fef91d61233af8` | printed reduced polynomials of the parent identity |

Every hash above matches the corresponding freeze, evidence, or charged
pin, or is an auxiliary reconstruction check. Characteristic-65521
stdout hash `61e108b59227dfa40de6da32455aef3e3e08d548c011c5e23c42559640b7d867`
appears in `EVIDENCE.sha256` and was opened only to confirm it is a
software control. It is not characteristic-zero evidence.

---

## 1. Both directions of (2.1)--(2.3) on `D(M)`

Let `Q=z^4+qp z^2+qc z+qr` and `N=n3 z^3+n2 z^2+n1 z+n0`, and set
`M=n3`, `A=z-a`, `B=4a`, `D=A^2+B A+E`. Expanding `(z-a)^k` gives

```text
A^4+4a A^3+E A^2
  = z^4 + (E-6 a^2) z^2 + 2a(4a^2-E) z + a^2(E-3 a^2),
A^3+4a A^2+E A
  = z^3 + a z^2 + (E-5 a^2) z - a(E-3 a^2).
```

The `z^3` term of `Q` cancels, so the displayed `Q` is depressed.
Adding `U A+R0` and `M(A D)+V A+M U/2+W0` therefore yields exactly
(2.3):

```text
qp=E-6 a^2,
qc=2a(4a^2-E)+U,
qr=a^2(E-3 a^2)+R0-a U,
n3=M,
n2=a M,
n1=(E-5 a^2)M+V,
n0=-a(E-3 a^2)M-a V+M U/2+W0.
```

Conversely, on `D(M)` the formulae (2.1) are the unique regular
inverses of (2.3): `a=n2/M` is regular, `E=qp+6 a^2` is polynomial,
`U=qc-2a(4a^2-E)` undoes `qc`, `R0=qr-a^2(E-3 a^2)+a U` undoes `qr`,
`V=n1-(E-5 a^2)M` undoes `n1`, and
`W0=n0+a(E-3 a^2)M+a V-M U/2` undoes `n0`. Substituting (2.3) into
(2.1) is the identity map on `(a,E,U,R0,M,V,W0)`; substituting (2.1)
into (2.3) is the identity map on `(qp,qc,qr,n3,n2,n1,n0)` after
inverting `M`. This is a regular isomorphism of affine charts, not an
analogy, not an endpoint projection, and not a Rees-torsion statement.

What it proves, and what it does not:

- On `D(M)` the unique seven-tuple `(a,E,U,R0,M,V,W0)` is a
  coefficient-coordinate isomorphism with the raw depressed `(Q,N)`.
- Extra `(R1,S1)` in the weighted presentation
  `Q=A^2 D+(X+R1)A+R0`, `N=M A D+(Y+S1)A+M X/2+S0` are a splitting of
  that isomorphism: `U=X+R1`, `V=Y+S1`, `W0=S0-M R1/2`. Existence of
  some splitting is regular (e.g. `X=U`, `R1=0`, `Y=V`, `S1=0`);
  uniqueness fails as soon as `R1` is free. The valuative argument
  needs only existence.
- The maps do not identify the original octic/load source with this
  `(Q,N)` chart, do not produce a two-sided total-Rees atlas, and do
  not force a raw source arc to enter `D(p*m*K10)`. That overlap
  remains a separate lemma. The theorem states this firewall; it is
  not silently closed.

Normal-scale extraction: writing `N=sigma^{15} lam * N_{shape}` with
`M` a unit is a chart hypothesis (the delayed-load normal weight 15),
not a conclusion of (2.1). Multiplying `lam` by a unit `u` and dividing
`M` by `u` leaves every displayed source combination invariant:
`lam^2 M U V` and `lam^3 M^3` are unchanged because `U` is a `Q`
coordinate while `V` and `M` scale as `N_{shape}`. A unit in
`Lambda=sigma^3 u` is removed by the finite ramification
`sigma |-> sigma u^{1/3}` already permitted in characteristic zero.
Uniqueness of that ramified parameter is not required.

---

## 2. Complementary negative tail (3.1), and the bound `2q`

The unloaded first-normal principal part is the negative `z`-part of
`(3/8) N^2/Q`, equivalently the polar part at the moving double root.
On the principal double root `Q=A^2 D`, `N=M A D`, one has
`N^2/Q=M^2 D`, holomorphic. The linearization in
`delta Q=R1 A+R0`, `delta N=S1 A+S0` is

```text
2 N dN/Q - N^2 dQ/Q^2
  = 2 M (S1 A+S0)/A - M^2 (R1 A+R0)/A^2
  = 2 M S1 + (2 M S0-M^2 R1)/A - M^2 R0/A^2.
```

`S1` is holomorphic. Multiplying the polar part by `3/8` is exactly
(3.1). Since `M` is a unit on `D(M)`, a leading complementary jet is
either a unit coefficient of `A^{-2}` or `A^{-1}`, or it satisfies
`R0=0`, `S0=M R1/2`. The latter is the kernel form of (2.2): replacing
`U <- U+R1`, `V <- V+S1` absorbs it, and the pairing `M U/2` is
precisely the holomorphic `S0` so produced.

The kernel square of the same expansion is the quadratic term
`(3/8)(V A - M U/2)^2/(A^2 D)` of valuation `2q`. Nonlinear
kernel-complement cross terms have valuation `q+r`; complement squares
have valuation `2r`. If `r>=2q` and `q>0`, then `q+r>=3q>2q` and
`2r>=4q>2q`, so those terms cannot meet the first complementary face.
Moving-center and `(E,M)` tangent jets do not contribute polar parts
from the principal piece `N^2/Q=M^2 D`, which remains polynomial in
`A` after any regular change of `a,E,M`. Reparametrizing `U <- U+R1`
with `v(R1)>=2q>q=v(U)` (the last inequality uses `q>0`) preserves
`v(U)`. Thus a single leading-coefficient dichotomy on a complete DVR,
after the ramification that makes `q` integral so that the value group
is `Z`, is justified: either an earlier unit linear pivot contradicts
the source rows, or `v(R0),v(W0)>=2q` in unique coordinates. Infinite
induction is not required for that bound; unique coordinates already
exist as regular functions on `D(M)`, and a complete DVR supplies a
leading coefficient. The smallest candidate missing term — a
center-kernel monomial of weight `5+q` at `q=5`, or an `(E,M)`-tangent
of weight 31 — is absent from every ordinary row through grade
`30+2q` after substituting the complete tails (section 4). No smaller
false polar monomial was found.

Existence of the weighted presentation used by the formal producer
follows: for a solution with `q>=6`, set `X=U`, `Y=V`, `R1=S1=0`. Then
`v(X),v(Y)>=6` and `v(R0),v(S0)>=2q>=12`. That is existence, not
uniqueness, and it is licensed only on the solution locus (or after
the complementary linear face has already killed the rest).

---

## 3. Why `q>0`, the central ideal, and the `q=0` receiver

The closed point of the exceptional moving-discriminant `A` chart is
the repeated-root first-normal point of family `D` in the reviewed UFD
erratum: `Q=z^2(z^2+p)`, `N=lambda m z(z^2+p)`, equivalently (1.4) at
`a=0`. In unique coordinates this is the maximal ideal generated by
`(U,V,R0,W0,a)` together with the higher jets of `E-p` and `M-m`. Every
DVR in the formal neighbourhood of that point therefore has
`q=min(v(U),v(V))>0` (or `q=infinity`). This is a consequence of the
central ideal, not a bare extra hypothesis, once the chart is that
formal neighbourhood.

The receiver for `q=0` is the complementary first-normal open: a unit
leading `U` (equivalently a unit `qc` after `a=0`) means the reduced
quartic is not the repeated-root form, so the arc specializes to the
squarefree/generic affine-Faber stratum or to the square family
`S: Q=(z^2+s)^2`. The discriminant `K`-face receives the remaining
quadratic degeneration. Those strata are outside the exceptional `A`
neighbourhood and are not claimed.

If one interpreted the theorem as a Zariski statement on the whole
affine open `D(p*m*K10)` without completing at the repeated-root point,
`q=0` would be an omitted face and would have to be added as an
explicit hypothesis. The theorem's language is the exceptional /
repeated `A` chart, and `v(a)>=5` is already a neighbourhood weight, so
the correct narrowing is: the claim is the weighted formal
neighbourhood of that closed point, not the uncompleted affine open.
The same neighbourhood carries the chart weight `v(a)>=5`; the
receiver for `0<v(a)<5` is an earlier center Newton face, likewise
outside the weighted chart used by the parent identity. The formula
`a=n2/M` does not by itself force `v(a)>=5`; that bound is a chart
weight, and the strongest surviving theorem records it as such.

---

## 4. Independent reconstruction of (4.1), and emptiness for `0<q<6`

The frozen complete ordinary-Faber tails, on the monomials

```text
(qr^2+n0, 2 qc qr+n1, qc^2+2 qp qr+n2, 2 qp qc+n3,
 qp^2+2 qr, 2 qc, 2 qp, k10, k6, k2),
```

were substituted with the exact delayed chart map (2.3), loads omitted
(they start at grade 42), `Lambda=sigma^3`, `N=sigma^{15} lam * N_{shape}`,
`a=sigma^5 a_5`, `U=sigma^q x`, `V=sigma^q y`, and complements of order
`2q`. Every ordinary row vanishes strictly below grade `30+2q`. At
that grade the seven rows are, independently of `q` in `{1,2,3,4,5}`
and independently of the jets `a_5`, `E_1`, `M_1`,

```text
G1= (3/4) m lam^2 s0 - (3/8) m^2 lam^2 r1,
G2= (3/8) lam^2 y^2 - (3/8) m^2 lam^2 r0,
G3= -(3/8) m lam^2 x y + (3/16) p m lam^2 s0 - (3/32) p m^2 lam^2 r1,
G4= (3/32) m^2 lam^2 x^2 - (3/16) p lam^2 y^2 - (3/16) p m^2 lam^2 r0,
G5= (3/32) p m lam^2 x y + (3/128) p^2 m lam^2 s0 - (3/256) p^2 m^2 lam^2 r1,
G6= (3/64) p^2 lam^2 y^2 - (3/64) p^2 m^2 lam^2 r0,
G7= -(3/256) p^2 m lam^2 x y - (3/512) p^3 m lam^2 s0 + (3/1024) p^3 m^2 lam^2 r1.
```

Dividing by the unit `lam^2` recovers (4.1) exactly, signs and scalars
included. The linear kernel face of weight `30+q` is identically zero
in every row: the pairing `S0=M U/2` cancels the polar part of
`2 N_{prin} N_{ker}/Q` against `-N_{prin}^2 (U A)/Q^2`. The
combination used by the theorem is the same cancellation at order
`2q`,

```text
G3-(p/4) G1 = -(3/8) m lam^2 x y,
```

so on `D(m)` one has `x y=0`. Then `G6=0` on `D(p)` gives `r0 m^2=y^2`.
On `D(x)` this forces `y=r0=0` and `G4=(3/32) m^2 lam^2 x^2`, a unit
times `x^2`. On `D(y)` it forces `x=0`, `r0=y^2/m^2`, and
`G4=-(3/8) p lam^2 y^2`, a unit times `y^2`. The two residue charts
exhaust the nonzero leading kernel. Localizations by `p` and `m` are
the chart open `D(p*m*K10)`; `K10` does not appear in the unloaded
face.

Unequal orders: if `v(U)<v(V)`, the order-`q` residue of `V` is zero,
so one is already on `D(x)`; the `x y` combination is strictly later
than `30+2q`, `G6` forces the order-`2q` residue of `r0` to vanish, and
`G4` remains a unit times `x^2`. The symmetric case `v(V)<v(U)` is the
`D(y)` residual. If one kernel series vanishes identically, the same
axis applies. If the orders become integral only after ramification
`sigma=tau^e`, the face is homogeneous of `tau`-degree `e(30+2q)`,
while loads start at `42e`; the inequality `30+2q<42` is preserved.
Center/connection, `(E,M)` tangents, complements of order `>=2q`,
loads, and targets do not appear at grade `30+2q`: the complete-tail
substitution through that grade, with `a_5`, `e_1`, and `m_1` present,
contains only the monomials of (4.1). Loads and `mu2` start at 42, and
`42>30+2q` for every rational `q<6`.

---

## 5. Composition of the `q>=6` identity after the weight bounds

Only after sections 2--4 is the parent identity eligible. On a solution
in the weighted neighbourhood one has `v(a)>=5`, `v(U),v(V)>=6`,
`v(R0),v(W0)>=2q>=12`, and normal scale `sigma^{15} lam` with `E,M,lam`
units on `D(p*m)`. Existence of the weighted symbols
`a,E,M,X,Y,R1,R0,S1,S0,lam` with those minimum weights follows by
`X=U`, `R1=0` (section 2). The confirmed polynomial congruence

```text
H3 = -(3/8) t^{42} lam^2 M X Y - (1/16) t^{45} lam^3 M^3,
H5 =  (3/8) t^{42} E lam^2 M X Y
```

modulo `t^{46}` is an identity in every displayed symbol. A
`Q`-algebra map sending `t` to `t` (or to `tau^e`) and the remaining
symbols to power series of nonnegative valuation therefore preserves
divisibility by `t^{46}` (resp. `tau^{46e}`). Negative powers are not
licensed, so substitution cannot lower the chart weights.

Unequal and fractional orders: raise the valuations of `X` and `Y`
independently, or after `t=tau^e` write `U=tau^{e q-6e} U'` and
likewise for `V`. All weights only increase. The direct unit
`[t^{45}](E H3+H5)=-E lam^3 M^3/16` becomes a unit at grade `45e` on
`D(E lam M)`. Common ramification is the same substitution `t=tau^e`.
The case `q=infinity` is `X=Y=0`; the cubic unit remains, and the
identity does not thereby become a statement that every raw source arc
enters the chart. Higher-kernel monomials through weight 45 are present
in the complete tails and cancel in the inverse-Faber rows; they are
not an omitted face.

This still does not prove source-to-chart coverage. Arcs that never
enter the weighted neighbourhood — including `q=0`, `v(a)<5`,
`v(n3)` different from 15, `m=0`, other load slopes, terminal/Taylor
receivers, and the complement of `D(p*m*K10)` — are outside both the
identity and this composition.

---

## 6. Loads, targets, `lam/M`, and the coordinate inverse through grade 45

The delayed-load source is

```text
Phi_l = r_l(C, Lambda^2 k10, Lambda^6 k6, Lambda^{10} k2)
        - Lambda^{12+l} delta_l,
(delta_1,...,delta_7)=(0, mu2, 0, mu4, 0, mu6, J/4).
```

The graph `k10=Lambda^{12} K10`, `k6=Lambda^8 K6`, `k2=Lambda^4 K2`
puts every effective lower-load slot at `Lambda^{14}`. With
`Lambda=sigma^3` this is sigma grade 42. Affine-linearity of `r_l` in
the three lower loads (one-parameter Rees parent) implies that
quadratic load monomials start at `Lambda^{28}=sigma^{84}`, far after
45; only the three independent weight-42 symbols can meet the window,
and they do so together. Target timing from the same source is

| target | source power | sigma grade |
|---|---:|---:|
| `mu2` in `P2` | `Lambda^{14}` | 42 |
| `mu4` in `P4` | `Lambda^{16}` | 48 |
| `mu6` in `P6` | `Lambda^{18}` | 54 |
| `J/4` in `P7` | `Lambda^{19}` | 57 |

A load times the moving center has grade at least `42+5=47`. A load
times a kernel variable has grade at least `42+6=48`. After the
weights of section 5 are licensed, the parent identity is a polynomial
congruence in independent load symbols of weight 42, and its reduced
`H3,H5` contain no load monomial through grade 45. Independently of
that reduction: `mu2` occurs only in `P2`, and the inverse-Faber row
`H3=P3-(B/2)P2+(5 B^2/32-E/4)P1` multiplies `P2` by `B=4a` of weight
5, hence first possible `mu2` contribution 47. In `H5=P5-B P4+...`
every `P2` target is again multiplied by a positive power of `B`,
while `mu4` is absent from `P4` until grade 48 and meets `H5` through
an extra positive `B` at grade 53. Rows `P1,P3,P5` have no direct
target. No omitted target, no `mu4` through `B P4`, and no
load-center or load-kernel cross term can reach the coefficient
`[sigma^{45}](E H3+H5)`.

The `lam/M` unit normalization is the scaling of section 1: it changes
no equation. The raw `(Q,N)` inverse on `D(p*m*K10)` is (2.1), which
exists and is unique as a seven-tuple on `D(M)`; uniqueness fails only
after extra `(R1,S1)` are adjoined. Existence of that inverse is not
existence of a map from the original octic/load source onto the chart.

---

## 7. Strongest exact theorem that survives

Work over a field of characteristic zero, on the delayed-load ray
`k10=Lambda^{12} K10`, `k6=Lambda^8 K6`, `k2=Lambda^4 K2`, after a
finite ramification `Lambda=sigma^3 u` reduced to `Lambda=sigma^3`.
Let the exceptional moving-discriminant `A` chart be the weighted
formal neighbourhood of the repeated-root point
`Q=z^2(z^2+p)`, `N=lambda m z(z^2+p)` inside `D(p*m*K10)`, with
`v(a)>=5` and normal scale `sigma^{15} lam`, `lam` a unit. Unique
coordinates (2.1) exist on `D(M)`. Then `q=min(v(U),v(V))>0` (or
`q=infinity`), genuine complements of a source solution satisfy
`v(R0),v(W0)>=2q`, and:

1. every rational `0<q<6`, after ramification making `q` integral,
   including unequal orders and a vanishing kernel series, dies at the
   unloaded quadratic face of grade `30+2q`, by the complete-tail rows
   (4.1) on `D(p*m)`;
2. every `q>=6`, including unequal and ramified orders and
   `q=infinity`, dies by the parent polynomial identity
   `[sigma^{45}](E H3+H5)=-E lam^3 M^3/16`, a unit on `D(E lam M)`,
   after the weight bounds of sections 2--4 license substitution into
   that identity.

No formal or Puiseux arc on this weighted chart satisfies all seven
source rows through grade 45. The statement is internal to the exact
affine-Faber `(Q,N)` chart. It is not a two-sided lemma from the
original coefficient source, not a total-Rees atlas theorem, and not a
theorem on `m=0`, `p=0`, other load slopes, terminal/Taylor receivers,
the Pell receiver, the `K`-face, order two, maximum twelve, or JC2.
Those require a separately proved overlap.

CONFIRMED
