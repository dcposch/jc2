# Hostile review — affine-Faber `A` H18/q6/a6 grade-54 direct unit

| Field | Value |
|---|---|
| Charged target | `cases/max12_812_order2_affine_faber_a_h18_q6_a6_g54_direct_unit_v1_20260826/RESULT.md` |
| Target SHA-256 | `ec8e0ecc9e97cc70cc0da5030210139aa9783a305077b4eed941fc101d8665d2` |
| `FREEZE.sha256` | `f1a463578cf622c9082241858e4ea56a74055a361ed9894a37efa8c5fbdf9382` |
| `EVIDENCE.sha256` | `ca10926b5243706791424b10387f02903663ed2df8792562fb98a12abb6f7c9b` |
| `RESULTS.sha256` | `55b6fc500cf48c1049a4df126762c948ac45f99a6efe97d40450a783c2b7e421` |
| Source compiler | `cases/.../compute_h18_q6_a6_g54_v1.py` SHA `1e04a8badb47f557b7daa5388d007eebb3ada950a6b0e248779a6db13d9c2c6a` |
| Exact-`Q` `hseries_through_g54.json` | `1c761b1aac81006bdbbcb3fbec1fd476b7749c0b8ea64875234a9bf1b8c9676c` |
| F65521 `hseries_through_g54.json` | `35763b3650ef00a041570d48ca4abcd2fc9e14e00e82be3d8be237638cd02e8c` |
| Recomputed hashes | all four charged pins, the source compiler, both serialized functionals, every freeze/evidence/results row, and the three frozen parents match the recorded digests |
| Overall verdict | **CONFIRMED** |
| Smallest exact defect | none |
| Smallest missing hypothesis | none inside the fixed normalized graph cell `(H,q,a)=(18,6,6)` with complements at `2q`, delayed loads at `42`, and `J` at `57`, on `D(p*m)` |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile reconstruction from the complete frozen 10-slot Faber tails. Different model family from the producer. No producer status line, no charged `PASS`/`ENDPOINT`/`UNIT` token, no validator string, this prompt, and no F65521 `PASS` is evidence |
| Method | SHA-256 of every charged pin and every freeze/evidence/results row before reading producer verdict prose; independent dense collection of odd rows 1,3,5,7 over `Q`; independent formation of `H`; hand specialization of the 10-slot factors at vanished centers; independent H18-wall weights of all 629 monomials; load-graph substitution of the two displayed `K6,K2` identities; eight scalar probes of abstract `H` against raw 10-slot evaluation; F65521 reduction checked only as software/support control |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 hashes of the files named in the review
prompt match those pins. Every freeze, evidence, and results row of the
V1 manifests matches the corresponding on-disk bytes. Producer verdict
language, `PASS-A-H18-Q6-A6-G54-DIRECT-UNIT-V1`,
`A_H18Q6A6_ENDPOINT=PASS_G54_DIRECT_UNIT`, both external validator
strings, and the F65521 coefficient `65519` were not used as
characteristic-zero evidence. Exact `Q` is the mathematical lane.
Characteristic 65521 is a software and support control only. No file
other than this review was written. Charged artifacts, producers,
shared ledgers, and `jc2-lean` were not edited.

---

## Verdict

**CONFIRMED.**

Work in characteristic zero, on the fixed normalized repeated-`A` graph
cell with valuations

```text
v(lambda)=18,  v(a)=v(X)=v(Y)=6,  v(R0)=v(R1)=v(S0)=v(S1)=12,
v(K10)=v(K6)=v(K2)=42,  v(J)=57,  v(E)=v(M)=0.
```

Independently reconstructed from the complete frozen 10-slot ordinary-Faber
tails, the raw odd-row polynomial

```text
H = 2 E^2 P3 + 16 E P5 + 64 P7 - (E^3/2) P1
```

is a 629-term polynomial over `Q`. Its unique monomial of affine weight
`54` on this cell is `-2 lambda^3 M^3 E^2`. Every other monomial has
weight at least `60` (thirty monomials) or `66` (thirty-six monomials).
The `P7` target contributes `±16 J` at weight `57` and is absent from the
tails combination. Substituting the exact affine load graph

```text
K6 = (15/32) K10 E^2 + s^48 d6,
K2 = (15/256) K10 E^4 + s^48 d2
```

and any moving-center or tangent jet of non-negative relative degree
cannot lower any of those weights. With `lambda = s^{18}` exactly and
leading coefficients `E(0)=p`, `M(0)=m`, the unique weight-54 monomial
expands as

```text
[s^g] H = 0  for g < 54,
[s^54] H = -2 m^3 p^2.
```

On `D(p*m)` the coefficient `-2 m^3 p^2` is a unit of the residue field,
so this fixed normalized graph cell is empty. The statement is internal
to that cell. It is not a ramified-fan theorem, not a literal
rational-source germ, and not a total-Rees, Taylor, order-two,
maximum-twelve, or JC2 theorem.

**CONFIRMED**

---

## Hashes and charged artifacts

Recomputed SHA-256, all matching the required pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| V1 `RESULT.md` | `ec8e0ecc9e97cc70cc0da5030210139aa9783a305077b4eed941fc101d8665d2` | charged; navigation only |
| V1 `EVIDENCE.sha256` | `ca10926b5243706791424b10387f02903663ed2df8792562fb98a12abb6f7c9b` | charged |
| V1 `FREEZE.sha256` | `f1a463578cf622c9082241858e4ea56a74055a361ed9894a37efa8c5fbdf9382` | charged |
| V1 `RESULTS.sha256` | `55b6fc500cf48c1049a4df126762c948ac45f99a6efe97d40450a783c2b7e421` | charged |
| V1 compiler `compute_h18_q6_a6_g54_v1.py` | `1e04a8badb47f557b7daa5388d007eebb3ada950a6b0e248779a6db13d9c2c6a` | freeze pin; algebra rederived, AWS `main()` not executed |
| exact-`Q` `hseries_through_g54.json` | `1c761b1aac81006bdbbcb3fbec1fd476b7749c0b8ea64875234a9bf1b8c9676c` | exact-`Q` custody |
| F65521 `hseries_through_g54.json` | `35763b3650ef00a041570d48ca4abcd2fc9e14e00e82be3d8be237638cd02e8c` | software control only |

Parent freeze pins independently rehashed, used only as algebra sources:

| Artifact | SHA-256 | Role |
|---|---|---|
| frozen tails `tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` | complete 10-slot ordinary-Faber tails |
| V2 `compute_h17_q7_g48_sparse.py` | `1ee515a8da4bc86ade10a86dae6a526c57d58eea0061158b977eab2b76020cf4` | freeze pin; dense/expand helpers only; H17 source series not used |
| sparse dict engine `compute_sparse_dag_v4.py` | `c539fad9a47299faa4a9afe1dbf3ee6ac868f3e8ef7cdbe7bd277c1ddd4d36d2` | ordinary exact dictionaries |
| parent H17 `hseries_exact_support.json` | `60658fb670ea1435e35655d86dc577472ab3213993461837819c1733a673c3df` | cross-check only; 630-term `G-32F` including `-16 J` |

Canonical JSON SHA-256 of `tails.json` is
`6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`.
Every relative path in V1 `EVIDENCE.sha256` (14 rows), `FREEZE.sha256`
(7 rows), and `RESULTS.sha256` (5 rows) rehashes to the recorded digest.
Independently reconstructed exact-`Q` support of `H` is termwise identical
to the parent 630-term polynomial with the single `J` monomial removed,
and the charged exact-`Q` coefficient file at grade 54 is the single term
`-2 p^2 m^3`.

---

## Attack 1 — H18 weights, 14-slot graph, jets that can reach 54

The frozen tails are polynomials in the 10-slot factor ring
`(B0,B1,B2,B3,B4,B5,B6,K10,K6,K2)` with counts

```text
row 1: 36,  row 2: 54,  row 3: 58,  row 4: 81,
row 5: 89,  row 6: 120, row 7: 131.
```

First frozen terms match the 10-slot order
`B0=qr^2+n0`, `B1=2 qc qr+n1`, `B2=qc^2+2 qp qr+n2`,
`B3=2 qp qc+n3`, `B4=qp^2+2 qr`, `B5=2 qc`, `B6=2 qp`,
then `K10,K6,K2`:

```text
row1: [0,0,0,0,0,1,0,0,0,1] * (1/4)     = (1/4) B5 K2,
row2: [0,0,0,0,0,0,2,0,0,1] * (-3/32)   = (-3/32) B6^2 K2,
row7: [0,0,0,0,0,1,3,0,0,1] * (-51/4096) = (-51/4096) B5 B6^3 K2.
```

There is no `J` slot and no `mu2,mu4,mu6` slot. Targets are attached
afterwards by the affine-chart convention

```text
P1: 0,  P2: mu2,  P3: 0,  P4: mu4,
P5: 0,  P6: mu6,  P7: -J/4.
```

The two-sided normalized affine substitution used to expand those factors
is

```text
qp = E - 6 a^2,
qc = 2 a (4 a^2 - E) + X + R1,
qr = a^2 (E - 3 a^2) + R0 - a (X + R1),
n3 = lambda M,
n2 = lambda a M,
n1 = lambda ((E - 5 a^2) M + Y + S1),
n0 = lambda (-a (E - 3 a^2) M - a Y + (1/2) M X + S0 - a S1).
```

Independent dense collection over `Q` produces abstract supports

```text
row 1: 106,  row 3: 194,  row 5: 379,  row 7: 670.
```

(Even rows 2, 4, 6 were not used in `H` and were not needed.) Eight
independent scalar probes (abstract evaluation versus raw 10-slot
substitution of the same combination) agree on every probe.

The H18 wall is the delayed-load equality `v(a)+2q=H` at the integral
point `q=6`, `a=6`, with complementary pivots at `q` and genuine
complements at `2q`:

```text
v(lambda)=18,  v(a)=v(X)=v(Y)=6,  v(R_i)=v(S_i)=12,
v(K10)=v(K6)=v(K2)=42,  v(J)=57,  v(E)=v(M)=0.
```

In the 14-slot order `(J,K2,K6,K10,S0,S1,R0,R1,Y,X,a,lambda,M,E)` this
is exactly the overridden tuple

```text
ABS_VALUATIONS = (57, 42, 42, 42, 12, 12, 12, 12, 6, 6, 6, 18, 0, 0).
```

Affine weight of an exponent vector `e` is the linear function
`const + slope·q` with

```text
const = 57 e_J + 42 (e_K2+e_K6+e_K10) + 18 (e_a + e_lambda),
slope = 2 (e_S0+e_S1+e_R0+e_R1) + (e_Y+e_X) - 2 e_a.
```

At `q=6` this recovers the valuation tuple above. The intrinsic monomial
`lambda^3 M^3 E^2` has `(const,slope)=(54,0)`.

Jets present in the H18 source series, and whether they can reach
grade 54:

| Series | Start | Jets charged | Absolute span | Can reach 54? |
|---|---|---|---|---|
| `lambda` | 18 | leading `1` only | `{18}` | yes, as `s^{54}` in `lambda^3` |
| `E` | 0 | `p,e1..e12` | `0..12` | yes, but only grade 0 is used |
| `M` | 0 | `m,m1..m12` | `0..12` | yes, but only grade 0 is used |
| `a` | 6 | `a6..a13` | `6..13` | no monomial of weight `<=54` contains `a` |
| `X,Y` | 6 | seven jets each | `6..12` | no monomial of weight `<=54` contains them |
| `R0,R1,S0,S1` | 12 | seven jets each | `12..18` | no monomial of weight `<=54` contains them |
| `K10` | 42 | `kk0..kk12` | `42..54` | K-bearing monomials have weight `>=60` |
| `d6,d2` | inner 6, then `+42` | seven jets each | `48..54` | load-deviation excess is `+6` on top of `42` |
| `J` | 57 | zero series | none | weight `57>54` |
| `mu2,mu4,mu6,d4,dm` | even-row targets | not in `H` | — | odd functional does not see them |

No omitted center, kernel, complement, load, or load-deviation jet can
reach grade 54. A deeper `a`-jet through grade 18, or `E,M` jets through
grade 54, would be required only by a monomial of weight strictly less
than 54. Independently, no such monomial exists (Attack 2). Truncation of
those superfluous jets is not a hole.

---

## Attack 2 — `H` from frozen tails, vanishing below 54, `[s^{54}]H=-2m^3p^2` over `Q`

Independent formation over `Q` of

```text
H = 2 E^2 P3 + 16 E P5 + 64 P7 - (E^3/2) P1
```

from the four odd abstract rows produces a 629-term polynomial. All 629
denominators are powers of two (maximum `128`), so the polynomial is
defined over `Z[1/2]` and reduces modulo `65521`.

The unique monomial supported on `{lambda,M,E}` alone is extracted by
the 10-slot specialization `a=X=Y=R=S=K=J=0`, which collapses the
factors to

```text
B0=B2=B5=K10=K6=K2=0,   B1=lambda E M,   B3=lambda M,
B4=E^2,   B6=2 E.
```

Only 5, 7, 9, and 12 tail terms of rows 1, 3, 5, 7 survive. Direct
evaluation of the combination at six independent numeric points, including
`(E,M,lambda)=(3,5,7)` and sign-changing points, equals
`-2 lambda^3 M^3 E^2` at every point. This coefficient is therefore an
identity of the frozen tails, not an inference from the modular run and
not an inference from the parent H17 cone file.

Weight census of the 629 monomials at the H18 schedule:

```text
W=54 : 1   = -2 lambda^3 M^3 E^2
W=60 : 30
W=66 : 36
W>=72: the rest.
```

Minimum weight is 54, attained once. Consequently every series
coefficient of `H` below grade 54 vanishes, and the grade-54 coefficient
is exactly the leading-jet evaluation of that one monomial. With
`lambda=s^{18}` exactly, `M=m+O(s)`, `E=p+O(s)`,

```text
lambda^3 M^3 E^2 = s^{54} m^3 p^2 + O(s^{55}),
```

hence `[s^{54}]H=-2 m^3 p^2` over `Q`. Higher jets of `E` and `M` multiply
the already-saturated `s^{54}` and land above 54. The charged exact-`Q`
file records empty dictionaries at grades 42 through 53 and the single
term `-2 p^2 m^3` at grade 54, matching this expansion. Grades 0 through
41 are omitted from the serialized file; the weight census makes those
grades identically zero, so the omission is not a mathematical hole.

The parent 630-term `G-32F` file differs from this `H` by exactly one
monomial: `-16 J`. Termwise comparison of the other 629 coefficients is
the zero dictionary. That agreement is a cross-check against an already
charged exact-`Q` support. It is not a substitute for the tails
reconstruction above, and it was not used to infer the characteristic-zero
coefficient.

F65521 of the same dictionary replaces `-2` by `65519 ≡ -2 (mod 65521)`
on the same monomial and leaves every other recorded grade empty. That
is a software/support control. It is not a characteristic-zero proof.

---

## Attack 3 — moving centers, tangent jets, load graph, `J`/`mu4`/`mu6`

The thirty weight-60 monomials are, grouped by type:

Complement / mixed-center block (twelve terms), including the five
lines that meet weight `3H` at the lower wall endpoint `q=9/2`:

```text
-6   Y lambda^3 M^2 E,
-9/4 R1 X^2 lambda^2 M^2,     6 R0 Y X lambda^2 M,
 6   R0 R1 lambda^2 M^2 E,    9/2 S0 X^2 lambda^2 M,
-12  S0 R0 lambda^2 M E,
```

and seven mixed `a`-corrections of the same weight (for instance
`-3 R1 a^2 lambda^2 M^2 E^2`, `3 R1 X a lambda^2 M^2 E`). Each has
weight 60 at `q=6`. A tangent jet of `X,Y,R,S` or a higher jet of `a`
adds strictly positive degree and cannot drop these terms to 54.

Load block (eighteen terms). The three pure `a^3` loads

```text
(155/16) K10 a^3 E^7,   -23 K6 a^3 E^5,   40 K2 a^3 E^3
```

are the H17 upper-endpoint combination, now at weight
`42+3·6=60`. Substituting the exact affine graph

```text
K6 = (15/32) K10 E^2 + s^{48} d6,
K2 = (15/256) K10 E^4 + s^{48} d2
```

into that combination produces

```text
a^3 E^7 K10 · (155/16 - 23·15/32 + 40·15/256)
 = a^3 E^7 K10 · (310/32 - 345/32 + 75/32)
 = (5/4) K10 a^3 E^7,
```

still of weight 60, plus `d6,d2` terms of weight `48+18=66`. The other
fifteen load monomials (`K_* X^* a^*` and `K_* R0 *`) likewise stay at
weight 60 after the `E`-polynomial part of the graph and rise to 66 or
more after the `s^{48}` deviations. Cancellation among load monomials
can only raise the valuation of the sum. It cannot create a grade-54
term. The unique weight-54 monomial contains no `K`, so the graph does
not touch it.

K-bearing monomials in the full 629-term polynomial have minimum weight
60 (544 of them). None reach 54.

Target modes:

- `P1=P3=P5=0` on the affine chart, so the odd tails combination is the
  odd-row functional.
- `P7=-J/4` contributes `64·(J/4)=16 J` or, with the opposite sign
  convention on the free coordinate `J`, `-16 J`. Either way the term
  has weight 57. It is not suppressed too early: 57 is the registered
  delayed-load target floor, strictly above 54. H18 sets the `J` series
  to zero; the tails polynomial therefore omits it, which is correct
  through grade 56.
- `mu4` and `mu6` are even-row targets (`P4`, `P6`). They do not enter
  `H`. A non-vanishing odd-row unit already empties the seven-row system,
  so even-row targets need not be retained for this emptiness claim.
  They are not suppressed too early; they are not present in the
  functional.

Moving the unit centers `E,M` by higher jets cannot alter grade 54 of
the unique monomial, as recorded in Attack 2. Recentering that would
change the leading values `p,m` is a different chart, excluded by
localization on `D(p*m)` rather than omitted.

---

## Attack 4 — localization on `D(p*m)`, fixed cell only

The residue coefficient `-2 m^3 p^2` is a unit on `D(p*m)` because
`-2` is a unit in characteristic zero and `p,m` are units of the
residue field. Therefore `H` cannot vanish at grade 54, the odd Faber
rows cannot all vanish, and the fixed normalized graph cell is empty.

This is producer evidence for one integral point of the delayed-load
wall

```text
(H, q, v(a)) = (18, 6, 6),
```

with the registered complement floor `2q`, load floor `42`, and target
floor `57`. It is not an exhaustive `q`-cell or ramified-fan theorem.

An independent weight comparison of the same 629 monomials against
grade `54=3H`, with no mixed-domain clamp, yields the unique-least
interval

```text
9/2 < q < 7
```

on the H18 wall: 255 positive-slope competitors with maximum lower bound
`9/2` (attained five times, all complement monomials), 325 negative-slope
competitors with minimum upper bound `7` (attained three times, the
`a^3` loads), and 49 slope-zero competitors of constant at least 57.
The integral point `q=6` lies in the open interval, which is why the
unit is unique there. That interval is a control on this reconstruction.
It is not charged, and it is not promoted to a theorem covering other
`q`, other `a`, a lighter `J` or load slope, or a ramified fan.

A different chamber — complements strictly below `2q`, loads lighter
than 42, `J` below 57, or `v(a)+2q≠18` — is a different cell. Nothing
here speaks to it.

---

## Attack 5 — source firewall

On the balanced integer slope-four ray `alpha=4` the source-descent
congruence is `3|H`. Independently:

```text
4·18/3 = 24 ∈ Z,   compatible.
```

The leading H18 remainder is also `mu_3`-invariant on the Gate-A
substitution `tau=s^3`, `varrho=s^3`, `sigma=s^4`: `sigma^{18}=s^{72}`
and `72≡0 (mod 3)`. The same arithmetic excludes a leading H17 remainder
(`s^{68}`, `68≡2 (mod 3)`). Compatibility of the leading orders
`(H,q,a)=(18,6,6)` with a rational germ is therefore necessary and holds.

It is not sufficient. A literal rational-source germ lives in a
completion `L((tau))=L((s^3))` and must be fixed by `s |-> zeta_3 s` on
every series coefficient, not only on the grade-54 face. The present
cell is a normalized formal `s`-series graph. Descent of the entire
jet, total-Rees or Taylor realization of the source, order two,
maximum twelve, and JC2 are not proved and are not claimed by the
charged `RESULT.md` firewall. They are not inferred here.

---

## Attack 6 — software semantics

The charged algebra is ordinary exact sparse dictionaries: monomial
tuples to `Fraction` (characteristic 0) or integers modulo `65521`.
No Singular quotient-ring, no remainder test, no Groebner basis, and no
`std`/`reduce` equality is licensed or used. The V1 compiler never
enters a quotient ring. Dense 14-slot collection of the four odd rows,
formation of `H`, and the weight census were rederived from those
dictionaries.

Stale diagnostic labels `H17Q7_ABSTRACT_ROW=...` appear eighteen times
in the exact-`Q` stdout because the V1 client imports V2's
`build_abstract_rows`. They are cosmetic. The actual overridden state
at the point of expansion is H18:

```text
MAX_GRADE = 54,
ABS_VALUATIONS = (57, 42, 42, 42, 12, 12, 12, 12, 6, 6, 6, 18, 0, 0),
```

with H18 `JET_VARS` and H18 `source_series` (`a` starting at 6,
complements at 12, `lambda=s^{18}`, load graph with `d6,d2` at inner
grade 6, `J` zero, no `mu2/mu4`). V2's own H17 source series, H17
expected block, and `MAX_GRADE=48` are not used. Row supports 106, 194,
379, 670 are the valuation-independent abstract odd rows, not an H17
cutoff. The labels do not contaminate the identity.

Dual AWS is correctly split: the exact-`Q` lane is evidence; the F65521
lane is a software/support control whose serialized coefficient differs
only by encoding `-2` as `65519`. The characteristic-zero coefficient
was not inferred from that reduction.

---

## Scope

The strongest licensed statement is emptiness of the fixed normalized
graph cell `(H,q,a)=(18,6,6)` with the registered complement, load, and
`J` floors, on `D(p*m)`, by a unit of the odd-row functional at grade
54. Independently confirmed content stops there.

The following are not proved, and the charged `RESULT.md` firewall does
not claim them:

- any other integral or rational `q` on the H18 wall, including the
  open interval `9/2<q<7` recorded only as a control;
- a ramified fan, a lighter load slope, or a `J` floor below 57;
- the even Faber rows as a separate obstruction;
- the full `mu_3` fixed-locus condition on every series coefficient;
- total-Rees or Taylor realization, order two, maximum twelve, or JC2.

---

CONFIRMED
