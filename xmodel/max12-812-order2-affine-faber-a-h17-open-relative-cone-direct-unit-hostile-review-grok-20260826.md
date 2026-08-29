# Hostile review — affine-Faber `A` H17 open relative-cone direct unit

| Field | Value |
|---|---|
| Charged target | `xmodel/max12-812-order2-affine-faber-a-h17-open-relative-cone-direct-unit-theorem-20260826.md` |
| Target SHA-256 | `513d11901c09046abbeb41f9c5f2441e023b27925fde861d4c873306c9fa1f63` |
| V9 `RESULT.md` | `1244a648d3bc761ae6fe9dbc1be72cad3e09b650d3d98109ebd2b4081ac1bb15` |
| V9 `EVIDENCE.sha256` | `3c8f207fc7522b58835758126a1a15841e76c92e3bc8beacebb6e22c55c81f06` |
| V9 `FREEZE.sha256` | `8bf9aa5e7485555fbeb0a19c0b9ae2dc106715b6c13da850c4bfdfe22925e237` |
| V9 `RESULTS.sha256` | `6aec97c6b03eaca66e6a3df9d80da41884ae5225836b96a5ab269962dcfe4365` |
| V9 exact-`Q` `hseries_exact_support.json` | `60658fb670ea1435e35655d86dc577472ab3213993461837819c1733a673c3df` |
| V4 exact-`Q` `abstract_functional_support.json` | `9ee52ed12c5ca75b0f36fdaf4292be6165d6a4380550c87faab3a654b23306bc` |
| V6 exact-`Q` `abstract_secondary_support.json` | `357829d292056e823c102446b8e95f5822dad961859e832a689160bca1e3fbcd` |
| Recomputed hashes | all nine charged pins match; every V9 freeze/evidence/results row and both parent V4/V6 freeze/evidence rows rehash to the recorded digest |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none inside the internal H17 equality-wall schedule `(1.1)` on `D(E*M)` with complements at `2q` and delayed-load floors `K:42`, `J:57` |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile reconstruction from the complete abstract exact-`Q` supports. Different model family from the producer. No producer status line, no charged `PASS`/`UNIT`/`ENDPOINT` token, no validator string, this prompt, and no V7/V8 label or fail-closed output is evidence |
| Method | SHA-256 of every charged pin and every freeze/evidence row before reading producer verdict prose; independent `Hseries=G-32F` over `Q` on all 663+665 parent monomials; independent affine-weight derivation and intersection of all 629 strict inequalities against grade 51; boundary blocks by direct evaluation at `q=17/4` and `q=7`; F65521 reduction checked only as software control |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the nine files named in the review
prompt match those pins. Every freeze and evidence row of the V9, V4,
and V6 manifests matches the corresponding on-disk bytes. Producer
verdict language, `PASS-A-H17-DIRECT-UNIT-RELATIVE-CONE-V9`,
`PASS_EXACT_RELATIVE_CONE_V9`, V7 displayed labels, and the V8
fail-closed negative were not used as characteristic-zero evidence.
Exact `Q` is the mathematical lane. Characteristic 65521 is a software
and support control only. V9 alone is controlling. No file other than
this review was written. The target, producers, shared ledgers, and
`jc2-lean` were not edited.

---

## Verdict

**CONFIRMED.**

Work in characteristic zero, in the internal normalized
moving-discriminant graph coordinates
`(J,K2,K6,K10,S0,S1,R0,R1,Y,X,a,lambda,M,E)`, with `E`, `M`, and the
leading coefficient of `lambda` units. Independently reconstructed from
the complete exact-`Q` abstract supports,

```text
Hseries = G - 32 F
        = 2 E^2 P3 + 16 E P5 + 64 P7 - E^3 P1/2
```

is a 630-term polynomial over `Q`. Its unique monomial of affine weight
`51` throughout the open interval `17/4<q<7` is `-2 lambda^3 M^3 E^2`.
The coefficient `-2` is a unit in characteristic zero. On that interval
every one of the other 629 monomials has weight strictly larger than
`51`. If every raw ordinary-Faber row vanished through valuation `51`,
every series-linear combination of those rows with coefficients of
non-negative valuation would vanish through valuation `51`, including
`Hseries`. That contradicts the unique unit. Rational `q` after a
common ramification does not change the open interval: the 629
comparisons are linear in `q`.

The statement is internal to this H17 equality-wall graph-support
schedule. It is not a literal source, normalized-Rees, total-Rees,
factor-degenerate, order-two, maximum-twelve, or JC2 theorem.

**CONFIRMED**

---

## Hashes and charged artifacts

Recomputed SHA-256, all matching the required pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| charged theorem | `513d11901c09046abbeb41f9c5f2441e023b27925fde861d4c873306c9fa1f63` | immutable target |
| V9 `RESULT.md` | `1244a648d3bc761ae6fe9dbc1be72cad3e09b650d3d98109ebd2b4081ac1bb15` | charged; navigation only |
| V9 `EVIDENCE.sha256` | `3c8f207fc7522b58835758126a1a15841e76c92e3bc8beacebb6e22c55c81f06` | charged |
| V9 `FREEZE.sha256` | `8bf9aa5e7485555fbeb0a19c0b9ae2dc106715b6c13da850c4bfdfe22925e237` | charged |
| V9 `RESULTS.sha256` | `6aec97c6b03eaca66e6a3df9d80da41884ae5225836b96a5ab269962dcfe4365` | charged |
| V9 exact-`Q` `hseries_exact_support.json` | `60658fb670ea1435e35655d86dc577472ab3213993461837819c1733a673c3df` | exact-`Q` Hseries custody |
| V4 exact-`Q` `abstract_functional_support.json` | `9ee52ed12c5ca75b0f36fdaf4292be6165d6a4380550c87faab3a654b23306bc` | exact-`Q` F custody |
| V6 exact-`Q` `abstract_secondary_support.json` | `357829d292056e823c102446b8e95f5822dad961859e832a689160bca1e3fbcd` | exact-`Q` G custody |

Parent freeze pins independently rehashed, used only as algebra sources:

| Artifact | SHA-256 | Role |
|---|---|---|
| frozen tails `tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` | complete 10-slot ordinary-Faber tails |
| V4 engine `compute_sparse_dag_v4.py` | `c539fad9a47299faa4a9afe1dbf3ee6ac868f3e8ef7cdbe7bd277c1ddd4d36d2` | freeze pin; `F` algebra rederived |
| V6 engine `compute_secondary_odd_v6.py` | `dd605e0a52f3b505a94bd30b783ca2461637beaeecc4a7c8788ea9b73a6f2fe3` | freeze pin; `G` algebra rederived |
| V9 analyzer `analyze_h17_cone_v9.py` | `eebd7825aa0a02dbe89113f4501aa079555ee90b41598320982278c0cc6de405` | freeze pin; inequalities rederived, not trusted |
| V4 F65521 `abstract_functional_support.json` | `b6eafc795464b7e7e077df2b2ea0fd58d7c963b14988e3d5322b312cafdf19a9` | software control only |
| V6 F65521 `abstract_secondary_support.json` | `742783f9679cea0e9bcb946d16d6aeaa6104f99e638283a1661c8929794dd197` | software control only |

Every relative path in V9 `EVIDENCE.sha256`, `FREEZE.sha256`, and
`RESULTS.sha256`, and in both parent `EVIDENCE.sha256` and
`FREEZE.sha256`, rehashes to the recorded digest. Canonical JSON of
the independently reconstructed 630-term `Hseries` is byte-identical
to the charged `hseries_exact_support.json`.

---

## Attack 1 — reconstruct `Hseries=G-32F`, 630 monomials, coefficient `-2`

The frozen tails are 10-slot polynomials in
`(B0,B1,B2,B3,B4,B5,B6,K10,K6,K2)` with counts

```text
row 1: 36,  row 2: 54,  row 3: 58,  row 4: 81,
row 5: 89,  row 6: 120, row 7: 131.
```

There is no `J` slot and no `mu2,mu4,mu6` slot. Targets are attached
afterwards by the row convention

```text
P1: 0,  P2: mu2,  P3: 0,  P4: mu4,
P5: 0,  P6: mu6,  P7: -J/4
```

on the affine chart `tau=0`. The V4/V6 engines substitute the moving
discriminant graph

```text
qp = E - 6 a^2,
qc = 2 a (4 a^2 - E) + X + R1,
qr = a^2 (E - 3 a^2) + R0 - a (X + R1),
n3 = lambda M,
n2 = lambda a M,
n1 = lambda ((E - 5 a^2) M + Y + S1),
n0 = lambda (-a (E - 3 a^2) M - a Y + (1/2) M X + S0 - a S1),
```

into the factor list

```text
B0 = qr^2 + n0,
B1 = 2 qc qr + n1,
B2 = qc^2 + 2 qp qr + n2,
B3 = 2 qp qc + n3,
B4 = qp^2 + 2 qr,
B5 = 2 qc,
B6 = 2 qp,
then K10, K6, K2,
```

and form the two odd-row combinations, adding the missing `P7` target
by hand because it is absent from the 10-slot tails:

```text
F = P7_tails - E^2 P3/32 + E^3 P1/64 - J/4,
G = E^2 P3 + 16 E P5 + 96 P7_tails - 24 J.
```

The `-24 J` is `96*(-J/4)`, not a second copy of a tail target. The
saved abstract supports are the complete graph polynomials: 663 terms
in `F`, 665 terms in `G`, maximum `a`-degree 17. They are not truncated
by the H16 grade-48 jet extraction. That completeness is required: an
H16 weight cutoff at 48 would have dropped `a^17` monomials that remain
present in the H17 comparison.

Independent subtraction over `Q` of every monomial in the union of the
two exact-`Q` supports produces 630 nonzero terms and 35 identical
cancellations `G=32F`. Zero coefficient mismatches against the charged
V9 support file. Two monomials occur only in `G`; none occur only in
`F`. The independently serialized canonical JSON SHA-256 is

```text
60658fb670ea1435e35655d86dc577472ab3213993461837819c1733a673c3df.
```

The intrinsic exponent vector `(lambda,M,E)=(3,3,2)` and all other
exponents zero has

```text
[F] = -1/64,    [G] = -5/2,
[G] - 32 [F] = -5/2 + 32/64 = -5/2 + 1/2 = -2.
```

It is the unique monomial supported on `{lambda,M,E}` alone: the
specialization `a=X=Y=R=S=K=J=0` of `Hseries` is exactly
`-2 lambda^3 M^3 E^2`. The displayed expansion of `(2.1)` is the
polynomial identity

```text
G - 32 F
  = (E^2 P3 + 16 E P5 + 96 P7) - 32 (P7 - E^2 P3/32 + E^3 P1/64)
  = 2 E^2 P3 + 16 E P5 + 64 P7 - E^3 P1/2,
```

with the `J` contribution `-24 J - 32*(-J/4) = -16 J` already inside
`P7`. All 630 denominators are powers of two, so reduction modulo
`65521` is defined. The independently reduced support equals the
F65521 reconstruction of `G-32F` monomial-for-monomial, and
`-2 ≡ 65519 (mod 65521)`. That agreement is a software control. It is
not a characteristic-zero proof.

---

## Attack 2 — independent affine weights, 629 inequalities, rational `q`

The H17 equality wall is the one-parameter valuation schedule on the
same 14 graph coordinates that interpolates the delayed-load integral
family `(H,q,ord(a))=(16,6,4)` by the linear relation
`v(a)+2q=H`. With `H=17`:

```text
v(lambda) = 17.
```

That is the definition of the kernel wall, with leading coefficient a
unit. Complementary pivot and mixed equality put both residue
coordinates at the same order

```text
v(X) = v(Y) = q.
```

Genuine complements of the linear polar of `(3/8)N^2/Q` start at
valuation at least `2q`. The wall schedule puts them at equality, not
strictly above:

```text
v(R0) = v(R1) = v(S0) = v(S1) = 2q.
```

The delayed-load equality `v(a)+2q=H` is the wall in the `(v(a),q)`
plane parallel to the H16 integral point `4+2*6=16`:

```text
v(a) = 17 - 2q.
```

Units:

```text
v(E) = v(M) = 0.
```

Load and target floors are the registered delayed-load source timings,
independent of the kernel weight `H`. Every effective lower load of
the integral graph `k10=Lambda^{12}K10`, `k6=Lambda^8 K6`,
`k2=Lambda^4 K2` is `Lambda^{14}` times its capitalized coordinate.
The source-series implementation of that graph starts `K10,K6,K2` at
absolute grade 42; equivalently, the ramification `Lambda=sigma^3` of
the delayed-load composition gives `14*3=42`. The affine `P7` target
is registered at 57 (`J=s^{57} jt` in the H16 source, and 57>51):

```text
v(K10) = v(K6) = v(K2) = 42,    v(J) = 57.
```

These are schedule hypotheses, not conclusions. A lighter load slope
or a complement strictly below `2q` is a different fan chamber and is
firewalled.

The affine weight of a monomial with exponent vector `e` is therefore
the linear function `const + slope·q` with

```text
const = 57 e_J + 42 (e_K2+e_K6+e_K10) + 17 (e_a + e_lambda),
slope = 2 (e_S0+e_S1+e_R0+e_R1) + (e_Y+e_X) - 2 e_a.
```

The intrinsic monomial has `(const,slope)=(51,0)`. Grade `51=3H` is
three times the kernel order.

Intersecting the 629 strict inequalities `const + slope·q > 51`
against the open `q`-line, with no mixed-domain clamp:

```text
slope > 0 : 255 bounds, maximum 17/4 (attained 5 times),
slope < 0 : 325 bounds, minimum 7     (attained 3 times),
slope = 0 :  49 competitors, all with const >= 57 > 51.
```

The unique-least interval of the 630-term polynomial under `(1.1)` is
therefore exactly

```text
17/4 < q < 7,
```

even before intersecting with the mixed-equality box `4<q<17/2`. That
box is the ambient delayed-load mixed chamber: `v(a)>0` forces
`q<17/2`, and the producer’s mixed-graph floor `q>21-H=4` sits
strictly below `17/4`. No competitor with bound `<=4` or `>=17/2`
enters `(17/4,7)`. Rational `q` is legitimate: after a common
ramification `s=tau^d` every valuation scales by `d`, the 629
comparisons remain the same linear inequalities in the ratio `q`, and
the open interval does not jump. Sample rationals
`q=19/4,9/2,5,11/2,13/2,27/4` each have unique minimum weight 51,
attained only at `-2 lambda^3 M^3 E^2`.

---

## Attack 3 — boundary bookkeeping, not labels

Direct evaluation of all 630 weights at the two endpoints, including
the intrinsic term:

At `q=17/4`, weight 51 is attained by exactly six monomials. The five
non-intrinsic terms all have line `34+(4)q`:

```text
-9/4  R1 X^2 lambda^2 M^2,
 6    R0 Y X lambda^2 M,
 6    R0 R1 lambda^2 M^2 E,
 9/2  S0 X^2 lambda^2 M,
-12   S0 R0 lambda^2 M E.
```

Check: `v(R1)+2v(X)+2v(lambda)=2q+2q+34=34+4q`, and
`34+4*(17/4)=34+17=51`. No other line meets 51 at this endpoint.
Count 5, line `34+4q`. The block consists of complement monomials, as
claimed. The displayed coefficients `-9/4,6,6,9/2,-12` match.

At `q=7`, weight 51 is attained by exactly four monomials. The three
non-intrinsic terms all have line `93+(-6)q`:

```text
155/16  K10 a^3 E^7,
-23     K6  a^3 E^5,
 40     K2  a^3 E^3.
```

Check: `42+3(17-2q)=42+51-6q=93-6q`, and `93-6*7=93-42=51`. Factoring
`a^3 E^3` recovers the displayed combination

```text
a^3 E^3 * ((155/16) K10 E^4 - 23 K6 E^2 + 40 K2).
```

Count 3, all loaded `a^3`, line `93-6q`. No other line meets 51 at
this endpoint.

The counts are correct, so there is no omitted competitor inside
either equality block. The next terms, recorded only as a control,
are:

```text
lower, largest bound < 17/4:
  17/5, line 34+(5)q, five monomials
  (e.g. -12 S0 R0 Y lambda^2).
  Weight at 17/4 equals 221/4 = 51 + 17/4 > 51.

upper, smallest bound > 7:
  38/5, line 127+(-10)q, three loaded a^5 terms
  (e.g. -8381/16 K10 a^5 E^6).
  Weight at 7 equals 57 = 51 + 6 > 51.
```

Neither family ties the intrinsic at the claimed endpoints. V7’s
stale displayed labels and V8’s fail-closed preregistration are
irrelevant: the V9 monomials and lines reconstruct from the support
without those reports.

Neither endpoint is claimed as a unit. On `q=17/4` or `q=7` the
initial form is a sum, and vanishing of that sum is a different
chamber.

---

## Attack 4 — unique abstract monomial to a raw-row unit

`Hseries` is a series-linear combination of the odd raw rows with
coefficients of valuation zero on `D(E)`:

```text
2 E^2,    16 E,    64,    -E^3/2
```

are units times non-negative powers of the unit `E`. The target `-J/4`
in `P7` contributes `-16 J` to `Hseries`. Write each raw row as
`P_j = sum_{n>=0} p_{j,n} s^n` and `E(s)=sum_{k>=0} e_k s^k` with
`e_0` a unit. Then

```text
[s^{51}](E(s)^k P_j) = sum_{i=0}^{51} [s^i](E^k) p_{j,51-i}.
```

Every summand uses a coefficient of `P_j` of degree at most 51. If
every raw ordinary-Faber coefficient through valuation 51 vanishes,
every such convolution vanishes, so `[s^{51}] Hseries = 0`. This uses
the moving series `E(s)` and does not replace `E` by its leading term.
A weaker hypothesis that only the grade-51 raw coefficients vanish,
with lower coefficients free, would not kill the convolutions; that
weaker statement is not claimed.

The unique abstract monomial of weight 51 on `17/4<q<7` is
`-2 lambda^3 M^3 E^2`. Expanding `lambda = s^{17} lambda_0`,
`E=e_0+cdots`, `M=m_0+cdots` with `lambda_0,e_0,m_0` units, its
leading source coefficient is `-2 lambda_0^3 m_0^3 e_0^2`, a unit in
characteristic zero. Higher jets of `E` and `M` contribute strictly
positive excess to this monomial and cannot cancel the leading term.
The other 629 abstract monomials have weight `>51` on the open
interval, so they cannot cancel it either.

Target and load completeness:

- `J` occurs in `Hseries` as the single term `-16 J`, weight 57, slope
  0. It does not meet 51 on the closed interval `[17/4,7]`.
- Every load monomial of `F` or `G` that does not cancel identically
  in `G-32F` is present among the 630. Counts: `K10` 385, `K6` 127,
  `K2` 32, together 544 of 630. Every such monomial has
  `const >= 42`. The 24 load monomials that cancel in `G-32F` cancel
  as polynomial identities (including the three H16 grade-46 terms
  `K10 a E^8`, `K6 a E^6`, `K2 a E^4` and the three grade-48 `X`-load
  terms). They are not omitted from a comparison; they are zero.
- No `mu`-target belongs to `P1,P3,P5,P7`. The 10-slot tails of those
  rows contain only `B0..B6,K10,K6,K2`. The targets `mu2,mu4,mu6` live
  only in the even rows `P2,P4,P6`, which are not summands of `F`,
  `G`, or `Hseries`. They cannot cancel `-2 lambda^3 M^3 E^2`.

Even rows are not needed for the contradiction. Simultaneous vanishing
of all seven raw rows through 51 implies vanishing of the four odd
rows, hence of `Hseries`.

Characteristic zero is required: Faber denominators and the
combinations `F,G` involve `32,64`, and the unit is `-2`. A complete
DVR of residue characteristic zero inverts `2`. Localization `D(E*M)`
is exactly the open on which `-2 E^2 M^3` is a unit. On `E=0` or
`M=0` the identity is `0=0` and supplies no obstruction.

---

## Attack 5 — coordinate jets and scope

On the wall schedule `(1.1)`, a higher jet of any coordinate has
positive excess. Substituting `var = (leading) s^{w} (1 + t s + ···)`
multiplies every monomial that uses that coordinate by a unit series
of valuation zero plus strictly positive valuation. No such jet can
lower an abstract monomial, and none can cancel the unique weight-51
leading coefficient.

A jet that drops a coordinate *below* the wall is a different
valuation chamber:

- complements strictly below `2q` can drop the five `34+4q` terms
  through 51 for some `q>17/4`;
- loads strictly below 42 can drop the three `93-6q` terms through 51
  for some `q<7`;
- `v(a)` off the wall `17-2q` is another equality ray;
- `q=0` is the homogeneous predecessor;
- `E=0` or `M=0` kills the unit.

Those chambers are identified receivers, not holes in `(1.1)`. Common
ramification cannot lower a term: it rescales every valuation by the
same positive integer and preserves the unique-least comparison.

The abstract polynomial is the graph substitution of the complete
ordinary-Faber tails, not a literal source series in the raw
one-parameter Rees coordinates, and not a Cech, normalized-Rees, or
total-Rees cocycle. The H17 comparison does not recompute source jets
at a new integral family; it weights the same 14-variable polynomial
along `(1.1)`. Accessibility of these graph coordinates from the
literal source, another load schedule, factor-degenerate opens, the
whole exceptional `A` fan, order two, `(8,12)`, maximum twelve, and
JC2 are all outside the licensed claim. The charged theorem already
states that firewall. It is not an overclaim.

---

## Attack 6 — strongest correct theorem

The strongest theorem licensed by the frozen complete tails and the
independent exact-`Q` reconstruction is exactly the charged statement.

On a characteristic-zero complete DVR, after finite ramification, in
the internal normalized moving-discriminant graph coordinates with
`E`, `M`, and the leading coefficient of `lambda` units, impose the
H17 equality-wall valuations

```text
lambda: 17;  X,Y: q;  R0,R1,S0,S1: 2q;  a: 17-2q;
K10,K6,K2: 42;  J: 57;  E,M: 0.
```

If `17/4<q<7`, then the 630-term polynomial `Hseries=G-32F` has unique
least monomial `-2 lambda^3 M^3 E^2` of valuation 51, with unit
coefficient. Simultaneous vanishing of the seven raw ordinary-Faber
rows through valuation 51 is therefore impossible. The exact interval
is `17/4<q<7`, contained in the mixed equality domain `4<q<17/2`. The
endpoints are ties, not units. Rational `q` is allowed.

There is no wrong coefficient among the 630 terms, the intrinsic `-2`,
the five lower-block coefficients, or the three upper-block
coefficients. There is no omitted competitor in either equality
block. There is no missing hypothesis inside this schedule on
`D(E*M)`. Do not upgrade the statement to literal source,
normalized-Rees or total-Rees coverage, a factor-degenerate open,
another load slope, the whole order-two problem, maximum twelve, or
JC2. Do not treat the F65521 reduction, V7 labels, or the V8
fail-closed negative as characteristic-zero evidence.

CONFIRMED
