# Hostile review — affine-Faber `A` H17/q7/a3 sequential grade-51 receiver

| Field | Value |
|---|---|
| Charged target | `cases/max12_812_order2_affine_faber_a_h17_q7_a3_sequential_g51_v6_20260826/RESULT.md` |
| Target SHA-256 | `4cfbda6e3188e72460aa46d5a2d5bf95b384755d53551d883b569df00666fc7f` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none inside finite prolongation through grade 51 on the two registered charts `D(x0*p*m*a3)` and `D(y0*p*m*a3)` of the fixed graph `(H,q,ord(a))=(17,7,3)` |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile reconstruction from frozen exact-`Q` V5 rows and functionals. Different model family from the producer. No producer status line, no charged `PASS`/`ENDPOINT` token, no validator string, this prompt, and no F65521 `PASS` is evidence |
| Method | SHA-256 of every charged pin and every freeze/evidence/results row before reading producer verdict prose; independent sparse Laurent dictionaries over `Q`; grade-by-grade monomial-unit pivots on both charts without V6 expected formulas; hand substitution of the grade-48 predecessor into raw `K51`; independent `d60` solve; F65521 used only as coefficient/support reduction |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the nine files named in the review
prompt match those pins. Every freeze, evidence, and results row of the
V6 manifests matches the corresponding on-disk bytes. Producer verdict
language, `PASS-A-H17-Q7-A3-SEQUENTIAL-G51-V6`,
`A_H17Q7G51V6_ENDPOINT=PASS_SEQUENTIAL_REDUCTION_THROUGH_GRADE51`, the
Box03/Box02 status strings, and both external validator tokens were not
used as characteristic-zero evidence. Exact `Q` is the mathematical
lane. Characteristic 65521 is a software and support control only. V6
is a Laurent reducer of already-frozen V5 rows; it does not recompile
the source. No file other than this review was written in the
repository. Charged artifacts, producers, shared ledgers, and
`jc2-lean` were not edited.

---

## Verdict

**CONFIRMED.**

On a characteristic-zero complete DVR, in the fixed integral delayed-load
source family `H=17`, `q=7`, `ord_s(a)=3` with the registered two-sided
normalized affine graph, the complete exact-`Q` V5 rows in absolute
grades 48--51 admit a sequential monomial-unit reduction on each of
`D(x0*p*m*a3)` and `D(y0*p*m*a3)`. Twenty linear pivots

```text
P1 -> s0j,  P3 -> yj (resp. xj),  P6 -> d2j,  P2 -> dmj,  P4 -> d4j
```

at `j=0,1,2,3` have a single registered Laurent-monomial coefficient at
every grade, with no illicit inversion. After those pivots,
`P5=P7=0` in grades 48, 49 and 50 on both charts. At grade 51 the same
five ordinary pivots leave the literal identities

```text
K51 = P5_51,
H51 = 16 p P5_51 + 64 P7_51,
```

and `K51=0` solves the remaining free leading correction by

```text
d60 = 36 (r00 m^2 - y0^2) / p^4
      - 5 kk0 a3^2 p - 2 m^3 / (a3 p^4).
```

On `D(x0)` one has `y0=0` from the grade-48 cross-kernel pivot, so the
`y0^2` term drops; on `D(y0)` the four-term display remains. After this
solve, `K51=P5_51=0` and the sole residual on both charts is

```text
64 P7_51 = H51 = -2 m^3 p^2 + (5/4) kk0 a3^3 p^7.
```

The fixed boundary therefore does not die through grade 51. It lands on
the candidate receiver `5 kk0 a3^3 p^5 - 8 m^3 = 0` in this graph only.
The statement is finite prolongation, not an all-orders arc.

---

## Hashes and charged artifacts

Recomputed SHA-256, all matching the required pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| V6 `RESULT.md` | `4cfbda6e3188e72460aa46d5a2d5bf95b384755d53551d883b569df00666fc7f` | charged; navigation only |
| V6 `EVIDENCE.sha256` | `735a89c01b685f3bbe03d71f0828e35bbec533bafbfd6b9c4beb860857e08c6b` | charged |
| V6 `FREEZE.sha256` | `ba04614debcc85e590f716ec966deae7d13fbd9ffbfee39f6596dd4748b88904` | charged |
| V6 `RESULTS.sha256` | `248b3f466451a11330f9389c29f438e65438fc018e85c77daa8b4e94d3de7cbb` | charged |
| exact-`Q` `chart_reductions.json` | `44fc3d616b241047198612d0020be6217f49fe511ecb6150fa68189e1cae8d6d` | exact-`Q` custody |
| F65521 `chart_reductions.json` | `2c1b0acda6c3244a7a60df192ebb04ebad4c3bdd7f136fde2114b78141227692` | software control only |
| exact-`Q` V5 `rows_g48_g51.json` | `1e626d0832d511a2bea5936eb1d687084f51a58f7f44062af23c3f71e88318ee` | exact-`Q` source rows |
| exact-`Q` V5 `functionals_g51.json` | `71ff2027b1d17c421bb84738a7298eed3f8136d8f488b39ab5f9414767c2542a` | exact-`Q` source functionals |
| grade-48 predecessor review | `e7df100dcbed28bf85e14108bb033c1663ae6334c810696e31d9927362a17f1c` | charged parent algebra |

Parent freeze pins independently rehashed, used as algebra sources only:

| Artifact | SHA-256 | Role |
|---|---|---|
| V6 engine `reduce_h17_q7_g51_v6.py` | `a345bcc009015ebe412fa6ef495ac9331f88d2501ae23ffe1e9f08cd46c1fd47` | freeze pin; algebra rederived independently |
| V6 `REGISTRATION.md` | `6c7373c8a4921946f279169cc054be9ad27c3dc504e6f7d9aa45e614bc6e357b` | freeze pin; localization printed as `D(x0*p*m)` but every actual inversion uses `a3` as well |
| F65521 V5 rows | `f33ab36df9f3a2db2684de2feab0195420926729a8cb8a1bcf43b2b4842d857e` | software control only |
| F65521 V5 functionals | `70ffdc19efde934dde590fa5b475b0a73df5b709ded8de9a9a878d9bca41c1a0` | software control only |

Every relative path in V6 `EVIDENCE.sha256` (14 rows), `FREEZE.sha256`
(8 rows), and `RESULTS.sha256` (5 rows) rehashes to the recorded digest.
Independently reduced exact-`Q` Laurent solutions and residuals are
termwise identical to the charged Box03 `chart_reductions.json`.

---

## Attack 1 — independent sequential pivots; monomial units; no illicit inversion

The frozen V5 exact-`Q` rows are ordinary sparse dictionaries in the
80-name jet window, with support sizes

```text
grade 48:  2,  6,  3,  4,  3,  5,  3
grade 49:  4, 11,  9,  8, 10, 12, 10
grade 50:  7, 23, 19, 17, 25, 29, 26
grade 51: 13, 41, 39, 29, 55, 58, 61
```

matching the V5 diagnostic counts. No negative exponents occur in the
source. The independent reducer does not import V6 and does not consult
`expected_h` or `expected_d60`.

Grade 48 raw polynomials, with V5 names `s00,r10,d20,d60,dm0,d40,x0,y0,r00,kk0,a3`:

```text
P1 = (3/4) m s00 - (3/8) m^2 r10,

P2 = (3/128) d60 p^4 - (1/8) d20 p^2 - dm0
     - (3/8) m^2 r00 + (3/8) y0^2 + (15/128) kk0 a3^2 p^5,

P3 = (3/16) m p s00 - (3/8) m x0 y0 - (3/32) m^2 p r10,

P4 = - d40 + (3/32) m^2 x0^2 - (3/16) m^2 p r00 - (3/16) p y0^2,

P5 = (3/128) m p^2 s00 + (3/32) m p x0 y0 - (3/256) m^2 p^2 r10,

P6 = (1/128) d20 p^4 - (1/512) d60 p^6
     - (3/64) m^2 p^2 r00 + (3/64) p^2 y0^2 - (15/1024) kk0 a3^2 p^7,

P7 = - (3/512) m p^3 s00 - (3/256) m p^2 x0 y0 + (3/1024) m^2 p^3 r10.
```

These are the charged V4/V5 grade-48 block, including the two genuine
center terms `+15 kk0 a3^2 p^5 / 128` in `P2` and `-15 kk0 a3^2 p^7 / 1024`
in `P6`.

On `D(x0*p*m*a3)` the first two ordinary pivots are

```text
P1 = 0  =>  s00 = (1/2) m r10
            (coefficient 3 m / 4, unit on D(m));

after that substitution, P3 = - (3/8) m x0 y0,
P3 = 0  =>  y0 = 0
            (coefficient -3 m x0 / 8, unit on D(x0*m)).
```

The same `s00` on `D(y0*p*m*a3)` leaves `P3 = - (3/8) m y0 x0`, hence
`x0 = 0`. Then `P6` is linear in `d20` with coefficient `p^4 / 128`:

```text
D(x0):  d20 = (1/4) d60 p^2 + 6 r00 m^2 / p^2 + (15/8) kk0 a3^2 p^3,
D(y0):  d20 = (1/4) d60 p^2 + 6 (r00 m^2 - y0^2) / p^2 + (15/8) kk0 a3^2 p^3.
```

`P2` is then linear in `dm0` with coefficient `-1`, and `P4` is linear in
`d40` with coefficient `-1`. Explicitly, after the `d20` solve and
`y0=0` on `D(x0)`,

```text
dm0 = - (1/128) d60 p^4 - (9/8) r00 m^2 - (15/128) kk0 a3^2 p^5,
d40 = - (3/16) r00 m^2 p + (3/32) m^2 x0^2.
```

On `D(y0)` the `y0^2` partners remain: `+ (9/8) y0^2` in `dm0` and
`- (3/16) p y0^2` in `d40`. These are the predecessor parametrization,
still linear in the free `d60`.

The same five pivot coefficients recur at every later grade:

```text
P1:s0j   coefficient  (3/4) m,
P3:yj    coefficient  - (3/8) m x0     on D(x0),
P3:xj    coefficient  - (3/8) m y0     on D(y0),
P6:d2j   coefficient  (1/128) p^4,
P2:dmj   coefficient  -1,
P4:d4j   coefficient  -1.
```

Independently recorded for all 20 ordinary pivots and for the final
`K51`-pivot of `d60`. Every coefficient is a single Laurent monomial.
The names in those monomials lie in `{x0,p,m,a3}` or `{y0,p,m,a3}`
according to the chart. No pivot inverts `r00`, `kk0`, `d61`, or any
other non-unit. No pivot is quadratic or a sum of two monomials: a
two-term Jacobian in `d2j` involving `e1 p^3` would have been an
immediate fail-closed stop, and it does not occur. The grade-by-grade
split keeps the leading Jacobian as the sole coefficient of the new
unknown.

At grade 51 the ordinary solutions first feel the obstruction. Before
the `d60` back-substitution, on `D(x0)`,

```text
s03 = - (1/6) a3 d60 m^{-1} p^3 + 8 a3 m r00 / p
      - (5/12) a3^3 kk0 m^{-1} p^4
      + (1/2) m r13 + (1/2) m1 r12 + (1/2) m2 r11 + (1/2) m3 r10,

y3  = - (1/6) a3 d60 m^{-1} p^4 x0^{-1} + 6 a3 m r00 x0^{-1}
      - (5/8) a3^3 kk0 m^{-1} p^5 x0^{-1} - (1/6) m^2 x0^{-1}.
```

The pivot coefficients remain `(3/4) m` and `-(3/8) m x0`. The factors
`m^{-1}` and `x0^{-1}` in the solutions are the legitimate localization
of a remainder that is not divisible by `m` or `x0`, not an illicit
inversion of a non-unit. On `D(y0)` the same coefficients invert `m`
and `y0`. After `d60` is substituted, the `r00` pair in `y3` cancels
and one is left with

```text
D(x0):  y0 = y1 = y2 = 0,
        y3 = (5/24) a3^3 kk0 m^{-1} p^5 x0^{-1} + (1/6) m^2 x0^{-1},

D(y0):  x0 = x1 = x2 = 0,
        x3 = -4 a3 m^{-1} y0
             + (5/24) a3^3 kk0 m^{-1} p^5 y0^{-1} + (1/6) m^2 y0^{-1}.
```

Twenty-one solutions per chart, all Laurent over the registered
units.

---

## Attack 2 — `P5=P7=0` in grades 48, 49, 50; complete V5 jets; `mu6` at 54 and `J` at 57

After `s00 = (1/2) m r10`,

```text
P5_48 = (3/32) m p x0 y0,
P7_48 = - (3/256) m p^2 x0 y0.
```

The cross-kernel pivot sets `y0=0` on `D(x0)` and `x0=0` on `D(y0)`, so
both vanish on both charts. This is the polynomial identity of the
predecessor (`C5 = (3 p^2 / 32) C1 - (p / 4) C3` and
`C7 = (p^2 / 32) C3 - (p^3 / 64) C1`) after the same two solves, not a
localization accident.

The independent reducer then substitutes each new solution into every
remaining row of grades 48--51 and into both frozen functionals. After
the five ordinary pivots of grades 48, 49 and 50, the reduced `P5` and
`P7` dictionaries are empty on both charts. That is twelve vanishing
compatibilities, obtained from the V5 polynomials, not from a V6
status field.

Jet completeness of the V5 input, from the registered valuations

```text
v(J)=57,  v(K2)=v(K6)=v(K10)=42,  v(S_i)=v(R_i)=14,
v(X)=v(Y)=7,  v(a)=3,  v(lambda)=17,  v(M)=v(E)=0,
v(d6)=v(d2)=v(dm)=v(mu4)=48,  v(mu6)=54.
```

The V5 window is `d4,dm,d2,d6,s0,s1,r0,r1,x,y` through excess 3
(`*0` through `*3`), together with `m1..m9`, `e1..e9`, `a3..a12`,
`kk0..kk9`. This covers every abstract monomial that can reach grade 51:

- weight-42 load needs excess 9 (`kk,e,m` through 9);
- weight-45 load needs excess 6 (`a` through `a9`);
- weight-48 face needs excess 3 (`x0..x3`, `y0..y3`, `r00..r03`,
  `s00..s03`, and the four `d*`-jets);
- weight-49 = `42+7` (`K X` or `K Y`) needs `X,Y` excess at most 2.

`J` is attached as the zero series: its first jet is at 57 and cannot
enter. `mu6` is not subtracted from row 6, correctly, because
`mu6 = t^{54} nu6` cannot enter a grade-`<=51` coefficient. Neither
`mu6` nor `J` appears in any frozen term.

Names that actually occur in the V5 rows and functionals through grade
51 are

```text
a3..a6, e1..e3, m,m1..m3, kk0..kk3,
d20..d23, d40..d43, d60..d63, dm0..dm3,
s00..s03, r00..r03, r10..r13, x0..x3, y0..y3, p.
```

The listed but unused names `s10..s13`, `m4..m9`, `e4..e9`, `a7..a12`,
`kk4..kk9` remain in the source series; they are not omitted from the
window. Their coefficients in the frozen rows are zero after
cancellation. The weight-42/45 load clusters are polynomial identities
in the full series `(kk,a,E)`, so their excess jets through 51 remain
zero and do not require a larger `X,Y` window. Every complete V5 source
jet that can reach grade 51 is present in the input.

---

## Attack 3 — grade 51: `K51=P5_51`, the `d60` formula, and the residual `H51`

Raw frozen functionals, parsed independently:

```text
K51 = 4 d40 a3 - dm0 p a3 + (1/8) d20 p^3 a3
      - (9/128) d60 p^5 a3 + (3/2) y0^2 p a3
      - (3/8) x0^2 m^2 a3 - (1/16) m^3 p
      - (65/128) kk0 a3^3 p^6,

H51 = -2 m^3 p^2 + (5/4) kk0 a3^3 p^7.
```

`H51` contains none of the twenty-one solved names, so sequential
substitution cannot change it. It is already the claimed residual at
the V5 source.

Hand substitution of the grade-48 predecessor into `K51`, without V6
formulas. Write `K51 = a3 K' - (1/16) m^3 p` and insert

```text
d40 = 3 x0^2 m^2 / 32 - 3 r00 m^2 p / 16 - 3 y0^2 p / 16,
d20 = d60 p^2 / 4 + 6 (r00 m^2 - y0^2) / p^2 + (15/8) kk0 a3^2 p^3,
dm0 = - d60 p^4 / 128 - (9/8) r00 m^2 + (9/8) y0^2 - (15/128) kk0 a3^2 p^5.
```

The `x0^2 m^2` pair in `4 d40` against `- (3/8) x0^2 m^2` cancels.
Collecting the rest:

```text
d60 p^5:     1/128 + 1/32 - 9/128 = -1/32,
r00 m^2 p:  -3/4 + 9/8 + 3/4     =  9/8,
y0^2 p:     -3/4 - 9/8 - 3/4 + 3/2 = -9/8,
kk0 a3^2 p^6: 15/128 + 15/64 - 65/128 = -5/32.
```

Hence

```text
K' = - (1/32) d60 p^5 + (9/8) (r00 m^2 - y0^2) p - (5/32) kk0 a3^2 p^6,
K51 = - (1/32) a3 d60 p^5 + (9/8) a3 (r00 m^2 - y0^2) p
      - (5/32) kk0 a3^3 p^6 - (1/16) m^3 p.
```

On `D(a3 p)`, `K51=0` rearranges by multiplying through by
`-32 / (a3 p^5)`:

```text
d60 = 36 (r00 m^2 - y0^2) / p^4 - 5 kk0 a3^2 p - 2 m^3 / (a3 p^4),
```

because `(9/8)*32 = 36`, `32*(5/32) = 5`, and `32*(1/16) = 2`. This is
the charged formula, derived from the predecessor plus raw `K51`, not
from V6's `expected_d60`.

The independent sequential reducer confirms the same polynomial after
all twenty ordinary pivots, on both charts:

```text
D(x0):  K51 = P5_51
            = - (1/32) a3 d60 p^5 + (9/8) a3 r00 m^2 p
              - (5/32) kk0 a3^3 p^6 - (1/16) m^3 p,

D(y0):  K51 = P5_51
            = - (1/32) a3 d60 p^5 + (9/8) a3 (r00 m^2 - y0^2) p
              - (5/32) kk0 a3^3 p^6 - (1/16) m^3 p.
```

The `d60` coefficient is the monomial unit `- a3 p^5 / 32`. The solved
`d60` matches the display above (with `y0=0` on `D(x0)`). After this
solve both `K51` and `P5_51` are the zero dictionary.

The row identity `H51 = 16 p P5_51 + 64 P7_51` holds before the `d60`
solve. On `D(x0)`, before that solve,

```text
P7_51 = (1/128) a3 d60 p^6 - (9/32) a3 r00 m^2 p^2
        + (15/256) kk0 a3^3 p^7 - (1/64) m^3 p^2.
```

Then `16 p P5` contributes `- (1/2) a3 d60 p^6 + 18 a3 r00 m^2 p^2
- (5/2) kk0 a3^3 p^7 - m^3 p^2` and `64 P7` contributes the opposite
`d60` and `r00` terms plus `(15/4) kk0 a3^3 p^7 - m^3 p^2`. The
`d60` and `r00` pairs cancel, leaving

```text
(5/4) kk0 a3^3 p^7 - 2 m^3 p^2 = H51.
```

The `y0^2` partners on `D(y0)` cancel in the same way. After `d60` is
set, `P5_51=0`, so necessarily `64 P7_51 = H51`. Directly,

```text
P7_51 = (5/256) kk0 a3^3 p^7 - (1/32) m^3 p^2
```

on both charts, and `64` times this is `H51`. `H51` itself is unchanged
by the `d60` substitution, as predicted from its support. Equivalently
on `D(p)`,

```text
H51 = (p^2 / 4) (5 kk0 a3^3 p^5 - 8 m^3),
```

which is the charged receiver. No extra grade-51 monomial survives on
either chart.

---

## Attack 4 — custom Laurent reducer; not the quarantined Singular-qring bug; F65521 as control

The V6 engine, and the independent reconstruction, store Laurent
polynomials as Python dictionaries `canonical monomial -> coefficient`
with `Fraction` in characteristic zero and an integer in characteristic
65521. Addition, scaling, multiplication, and substitution are explicit
sparse operations. There is no Singular session, no `qring`, no `std`,
and no quotient-ring `==`. The quarantined Singular-qring equality bug
does not apply.

Coefficient parsing is `Fraction` of the frozen decimal-slash strings
(`"3/4"`, `"-9/128"`, `"5/4"`). Canonical monomials sort name pairs and
drop zero exponents, keeping negative exponents of localizations.
Substitution of a solved variable fails closed if that variable occurs
with a negative exponent in the target, and `power` refuses a negative
polynomial exponent of a whole polynomial. Negative exponents that do
occur (`p^{-4}`, `m^{-1}`, `a3^{-1}`, `x0^{-1}`, `y0^{-1}`) are of
registered units, produced by inverting a monomial pivot coefficient,
not by raising a polynomial to a negative power.

Substitution order is grade 48, 49, 50, 51, and inside each grade
`P1, P3, P6, P2, P4`, then `d60` from reduced `K51`. Each new solution
is substituted into every previously stored solution (back-substitution)
and into every remaining row and both functionals, then stored once.
No variable is solved twice. The post-substitution check that the pivot
row is the empty dictionary catches a leftover linear term. The grade-51
formulae for `s03` and `y3` (resp. `x3`) still contain `d60` at the
moment they are solved; the later `d60` substitution updates those
stored solutions and is back-substitution, not a second solve of `y3`.

Comparison is dictionary equality on canonical monomials. The zero
polynomial is the empty dictionary. This is ordinary exact arithmetic.

F65521 is the coefficientwise reduction of the same 532 exact-`Q` row
terms plus the two functionals, with identical support. Independently,

```text
5/4  ≡ 49142,    -2 ≡ 65519,
-5   ≡ 65516,    -36 ≡ 65485  (mod 65521).
```

Every registered pivot denominator (`4, 8, 32, 128` and the monomials
`m, x0, y0, p, a3`) is invertible in `F_65521`. The same sequential
reduction in characteristic 65521 reproduces the reduced `d60` and
`H51` on both charts. That agreement is a software and support control.
It is not a characteristic-zero proof of the `Q` identities, and it was
not used as one.

Registration prints the charts as `D(x0*p*m)` in one sentence. The
`d60` formula, the Jacobian `- a3 p^5 / 32`, the g51 odd-row
localizations, the charged `RESULT.md`, and every recorded pivot
coefficient use `D(x0*p*m*a3)` and `D(y0*p*m*a3)`. The printed
omission of `a3` in that one registration sentence is not a failed
identity: the engine inverts `a3` exactly where the algebra requires it.

---

## Attack 5 — endpoint and scope

The strongest licensed statement is finite prolongation of the
corrected grade-48 predecessor through absolute grade 51, on the two
registered projective charts of the fixed integral source-graph family
`(H,q,ord(a))=(17,7,3)`, together with the identification of the sole
grade-51 residual with

```text
H51 = -2 m^3 p^2 + (5/4) kk0 a3^3 p^7,
```

equivalently the receiver `5 kk0 a3^3 p^5 - 8 m^3 = 0` on `D(p)`.
Solving for the campaign parameter `kk0` is rational; over a fixed
`kk0` the same equation is a cubic Kummer sheet. Independently
confirmed content stops there.

The following are not proved, and the charged `RESULT.md` firewall does
not claim them:

- all-orders lifting of the five dependent series, or of the receiver
  (that is a separate implicit-function composition, not this reduction);
- literal-source or total-Rees accessibility of the normalized graph;
- terminal `[6,2]` or either finite Taylor pullback;
- any other graph, load schedule, or `(H,q,ord(a))`;
- order two, maximum twelve, `(8,12)`, or JC2.

A confirmation of this sequential reduction does not promote the
provisional all-orders Kummer-lift composition, and it does not make
the grade-51 residual a contradiction. The boundary survives through
grade 51 on both charts.

---

## Verdict

CONFIRMED
