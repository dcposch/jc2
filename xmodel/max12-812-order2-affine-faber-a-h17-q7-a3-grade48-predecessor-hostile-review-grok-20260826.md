# Hostile review — affine-Faber `A` H17/q7/a3 grade-48 predecessor

| Field | Value |
|---|---|
| Charged target | `cases/max12_812_order2_affine_faber_a_h17_q7_a3_predecessor_g48_sparse_v4_20260826/RESULT.md` |
| Target SHA-256 | `6e6e5cf16b6b99400ee92e610966d99b70bae46fa6719ad94e9804ec28bef6b8` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none inside the charged fixed integral family `(H,q,alpha)=(17,7,3)` on `D(p*m)` |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile reconstruction from frozen `tails.json` and the two-sided normalized affine substitution. Different model family from the producer. No producer status line, no charged `PASS`/`ENDPOINT` token, no validator string, this prompt, and no F65521 `PASS` is evidence |
| Method | SHA-256 of every charged pin and every freeze/evidence/results row before reading producer verdict prose; independent 10-slot factor substitution; independent abstract collection of all seven raw rows; H17 valuation cut at 48; exact-`Q` series convolution of every survivor including the weight-42/45 load clusters; independent load-graph identities for the two new center terms; odd-row redundancies and `D(p*m)` elimination by hand; both unit-center projective witnesses; row-4 omission negative; F65521 reduction checked only as software/support control |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the eight files named in the review
prompt match those pins. Every freeze, evidence, and results row of the
V4 manifests matches the corresponding on-disk bytes. Producer verdict
language, `PASS-A-H17-Q7-A3-G48-CORRECTED-V4`,
`A_H17Q7V4_ENDPOINT=PASS_CORRECTED_GRADE48_PREDECESSOR`, the Box03/Box02
status strings, V2's incomplete expected block, V3's diagnostic emission,
and the V1 Singular compiler were not used as characteristic-zero
evidence. Exact `Q` is the mathematical lane. Characteristic 65521 is a
software and support control only. V2 is a deliberate failed-closed
negative: it omitted the two center/load terms and is not evidence. V3
only emitted the complete block. V1 is ordinary Singular and has no
verdict. V4 is the controlling sparse exact replay. No file other than
this review was written in the repository. Charged artifacts, producers,
shared ledgers, and `jc2-lean` were not edited.

---

## Verdict

**CONFIRMED.**

On a characteristic-zero complete DVR, in the fixed integral delayed-load
source family `H=17`, `q=7`, `ord_s(a)=3` with the registered
two-sided normalized affine graph, all seven ordinary-Faber rows vanish
below absolute grade 48 after graph cancellation. The complete exact-`Q`
grade-48 block is the 26-term system displayed in the charged `RESULT.md`,
including the two genuine center/load terms

```text
C2 += +15 kk a^2 p^5 / 128,
C6 += -15 kk a^2 p^7 / 1024.
```

The odd rows satisfy the polynomial identities `C5=(3p^2/32)C1-(p/4)C3`
and `C7=(p^2/32)C3-(p^3/64)C1`. On `D(p*m)` the face reduces to the five
displayed formulas for `s0`, `xy`, `d2`, `dm`, `d4`. Both projective
charts admit explicit zeros with `p=m=a=kk=1`; no reconstructed row is a
unit, and the row-4 omission negative is the nonzero value `-1/32`. The
endpoint is genuinely SURVIVES. The statement is internal to this fixed
integral source-graph family on `D(p*m)`.

---

## Hashes and charged artifacts

Recomputed SHA-256, all matching the required pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| V4 `RESULT.md` | `6e6e5cf16b6b99400ee92e610966d99b70bae46fa6719ad94e9804ec28bef6b8` | charged; navigation only |
| V4 `EVIDENCE.sha256` | `051b9cfc18910e40da63da9ce5115397775f6ce9fdb34065da6bfd3359184f85` | charged |
| V4 `FREEZE.sha256` | `1bd52a1b6074537d11693ba9bd5d0589ead68f7a9d037f21e4c2a20edbf78713` | charged |
| V4 `RESULTS.sha256` | `d9f95300ed1a6d91ce5239263b3bd4628606b987ba3e5f13cdefe72181ea0db4` | charged |
| exact-`Q` `grade48_rows.json` | `39632462be45678e3d7d94ab03e9836a121bd281dcbfed3aed3d2078fa006896` | exact-`Q` custody |
| F65521 `grade48_rows.json` | `064de62d5158224bfbca7f68d3383eb26b2986949997cdf93942846876b1abf8` | software control only |
| V4 engine `check_h17_q7_g48_v4.py` | `9758ca40336c36b5b268b1d91ab57df767cd4b3b53eb8b00934d07d581d1463e` | freeze pin; algebra rederived |
| frozen tails `tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` | complete 10-slot ordinary-Faber tails |

Parent freeze pins independently rehashed, used only as algebra sources:

| Artifact | SHA-256 | Role |
|---|---|---|
| V3 `emit_h17_q7_g48_v3.py` | `759f61fd62b50263915a0dba2a3827208e995e71791811c0d5494ce9685ce93e` | diagnostic emission only |
| V2 `compute_h17_q7_g48_sparse.py` | `1ee515a8da4bc86ade10a86dae6a526c57d58eea0061158b977eab2b76020cf4` | failed-closed negative; not evidence |
| sparse dict engine `compute_sparse_dag_v4.py` | `c539fad9a47299faa4a9afe1dbf3ee6ac868f3e8ef7cdbe7bd277c1ddd4d36d2` | ordinary exact dictionaries |

Canonical JSON SHA-256 of `tails.json` is
`6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`.
Every relative path in V4 `EVIDENCE.sha256` (14 rows), `FREEZE.sha256`
(8 rows), and `RESULTS.sha256` (5 rows) rehashes to the recorded digest.
Independently reconstructed exact-`Q` grade-48 dictionaries are termwise
identical to the charged Box03 file.

---

## Attack 1 — seven abstract rows, H17 weights, nothing below 48 after cancellation

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
row1: [0,0,0,0,0,1,0,0,0,1] * (1/4)   = (1/4) B5 K2,
row2: [0,0,0,0,0,0,2,0,0,1] * (-3/32) = (-3/32) B6^2 K2,
row7: [0,0,0,0,0,1,3,0,0,1] * (-51/4096) = (-51/4096) B5 B6^3 K2.
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

(The identity `E-5a^2=(E-3a^2)-2a^2` is the V1 `DD-2 AA^2` form of `n1`.)
Independent dense collection over `Q` produces abstract supports

```text
row 1: 106,  row 2: 146,  row 3: 194,  row 4: 114,
row 5: 379,  row 6: 495,  row 7: 670.
```

Three independent scalar probes (abstract evaluation versus raw 10-slot
substitution) agree on every row. Targets are attached afterwards. On
the affine chart `tau=0`,

```text
P1: 0,  P2: mu2,  P3: 0,  P4: mu4,
P5: 0,  P6: mu6,  P7: -J/4.
```

The charged H17 wall is

```text
v(lambda)=17,  v(X)=v(Y)=7,  v(Ri)=v(Si)=14,
v(a)=3,        v(K10)=v(K6)=v(K2)=42,
v(d6)=v(d2)=v(dm)=v(mu4)=48,  v(mu6)=54,  v(J)=57,
v(E)=v(M)=0.
```

Load graph through the only six relative grades that can reach 48:

```text
K10 = t^42 kk,
K6  = t^42 ((15/32) kk E^2 + t^6 d6),
K2  = t^42 ((15/256) kk E^4 + t^6 d2),
mu2 = t^42 ((-5/4096) kk E^6 + t^6 dm),
mu4 = t^48 d4.
```

`mu6` and `J` have no coefficient of grade `<=48`, so they cannot enter
the predecessor. Valuation cut of the seven abstract rows at weight 48
leaves

```text
row 1: 5 survivors (3 of weight 45, 2 of weight 48),
row 2: 8 survivors (3 of weight 42, 5 of weight 48),
row 3: 6 survivors (3 of weight 45, 3 of weight 48),
row 4: 3 survivors (all weight 48),
row 5: 6 survivors (3 of weight 45, 3 of weight 48),
row 6: 8 survivors (3 of weight 42, 5 of weight 48),
row 7: 6 survivors (3 of weight 45, 3 of weight 48).
```

The weight-42 and weight-45 clusters are pure load:

```text
C1_load(45) = -K2 a E + (3/8) K6 a E^3 - (15/128) K10 a E^5,
C2_load(42) = -(1/8) K2 E^2 + (3/128) K6 E^4 - (5/1024) K10 E^6,
C3_load(45) = (1/4) K2 a E^2 - (3/32) K6 a E^4 + (15/512) K10 a E^6,
C5_load(45) = (3/32) K2 a E^3 - (9/256) K6 a E^5 + (45/4096) K10 a E^7,
C6_load(42) = (1/128) K2 E^4 - (1/512) K6 E^6 + (15/32768) K10 E^8,
C7_load(45) = -(5/128) K2 a E^4 + (15/1024) K6 a E^6 - (75/16384) K10 a E^8.
```

On the load graph with `d2=d6=dm=0` these are polynomial identities in
`(kk,a,E)`:

```text
C2_load(42) - mu2_lead = kk E^6 (
    -15/2048 + 45/4096 - 5/1024 + 5/4096
) = kk E^6 (-30+45-20+5)/4096 = 0,

C6_load(42) = kk E^8 (
    15/32768 - 15/16384 + 15/32768
) = kk E^8 (15-30+15)/32768 = 0,

C1_load(45) = kk a E^5 (
    -15/256 + 45/256 - 30/256
) = 0,
```

and the same cancellation holds for the `C3,C5,C7` triples (coefficients
`1/4, -3/32, 15/512`; `3/32, -9/256, 45/4096`; `-5/128, 15/1024, -75/16384`
against `(15/256, 15/32, 1)`). Because the identities are polynomial in
the full series `E` and `kk`, they kill every positive-excess jet of those
clusters. After substituting the load graph and subtracting `mu2` from
row 2 and `mu4` from row 4, independently convolved series of all seven
rows are the zero jet in every grade `0..47`. No monomial and no target
reaches below grade 48 after graph cancellation.

---

## Attack 2 — twenty-six exact-`Q` terms; the two new center coefficients; excess jets

Independent convolution of the weight-`<=48` survivors, including the
registered `+6` deviations `d6,d2,dm` and the independent target `d4`,
produces exactly twenty-six nonzero grade-48 monomials over `Q`:

```text
C1 = -3 r1 m^2 / 8 + 3 s0 m / 4,

C2 = 3 d6 p^4 / 128 - 3 r0 m^2 / 8 - d2 p^2 / 8 + 3 y^2 / 8 - dm
     + 15 kk a^2 p^5 / 128,

C3 = -3 r1 m^2 p / 32 - 3 x y m / 8 + 3 s0 m p / 16,

C4 = 3 x^2 m^2 / 32 - 3 r0 m^2 p / 16 - 3 y^2 p / 16 - d4,

C5 = -3 r1 m^2 p^2 / 256 + 3 x y m p / 32 + 3 s0 m p^2 / 128,

C6 = -d6 p^6 / 512 - 3 r0 m^2 p^2 / 64 + d2 p^4 / 128
     + 3 y^2 p^2 / 64 - 15 kk a^2 p^7 / 1024,

C7 = 3 r1 m^2 p^3 / 1024 - 3 x y m p^2 / 256
     - 3 s0 m p^3 / 512.
```

Term counts `2+6+3+4+3+5+3=26`. Byte-for-byte, these are the charged
Box03 dictionaries. V2's expected block omitted the two `kk a^2`
monomials and therefore mismatches reconstructed rows 2 and 6 only; that
is the failed-closed negative, not a formula.

The new terms are not an engine accident. They are the weight-48 abstract
load monomials

```text
C2_a2(48) = 2 K2 a^2 E - (3/2) K6 a^2 E^3 + (45/64) K10 a^2 E^5,
C6_a2(48) = -(1/2) K2 a^2 E^3 + (9/32) K6 a^2 E^5 - (15/128) K10 a^2 E^7,
```

which are the `qp=E-6a^2` corrections already collected in the abstract
rows. Substituting the leading load `K2=(15/256)kk E^4`,
`K6=(15/32)kk E^2`, `K10=kk` and `E=p`, `a=a3` gives

```text
C2_a2 = 2*(15/256) + (-3/2)*(15/32) + 45/64
      = 15/128 - 45/64 + 45/64
      = 15/128,

C6_a2 = (-1/2)*(15/256) + (9/32)*(15/32) + (-15/128)
      = -15/512 + 135/1024 - 120/1024
      = -15/1024.
```

The `K6` and `K10` partners cancel in `C2`; the three partners in `C6`
leave `-15/1024`. These coefficients are therefore forced by the
registered graph, not by a truncation of `qp` to `E`.

Positive-excess center, `E`, `M`, and `K10` jets cannot add another
grade-48 term:

- every remaining survivor after the load identities has weight *exactly*
  48, so only leading jets `a3,p,m,kk0,x,y,r0,r1,s0,d2,d6,dm,d4` can
  appear;
- the weight-42/45 clusters are polynomial identities in the full series
  `(kk,a,E)`, so `e_i`, `kk_{i>=1}`, and `a_{i>=4}` inserted into those
  clusters remain zero;
- a weight-48 monomial `K2 a^2 E` already spends `t^6` on `a3^2`; the
  cross term `2 a3 a4` has excess 1 and lands at grade 49;
- `M`-jets do not occur in the load clusters, and the complement
  monomials `R1 lambda^2 M^2`, `S0 lambda^2 M`, `Y X lambda^2 M`,
  `Y^2 lambda^2`, `X^2 lambda^2 M^2` are weight 48 on the nose, so `m_i`
  and `s1` are grade 49 or higher;
- `mu6` starts at 54 and `J` at 57.

Independent expansion with the full jets `e1..e6`, `m1..m6`, `a4..a9`,
`kk1..kk6`, `s1` produced an empty excess-jet support at grade 48.

---

## Attack 3 — F65521 is support/reduction only; engine is ordinary dictionaries

The Box02 file is the coefficientwise reduction of the same 26 exact-`Q`
monomials modulo 65521, with identical support. Independently,

```text
15/128   ≡ 512    (128*512 = 65536 ≡ 15),
-15/1024 ≡ 65457  (1024*64 = 65536 ≡ 15, so 15/1024 ≡ 64 and
                   -64 ≡ 65457),
-3/8     ≡ 24570,   3/4 ≡ 16381,
-1       ≡ 65520.
```

Every one of the 26 reduced rationals matches the Box02 coefficient on
the same exponent vector. That agreement is a software/collection
control. It is not a characteristic-zero proof of the `Q` formulas, and
it was not used as one.

The controlling engine is `compute_sparse_dag_v4.py` with H17 jet names
and valuations overlaid. It stores dense abstract polynomials and sparse
jets as ordinary Python dictionaries `monomial -> Fraction` (or an integer
in characteristic 65521), with explicit addition, scaling, and
multiplication, a support cap, and no Singular session. There is no
quotient-ring `reduce`, no `std`, and no `==` in a quotient. V1 is the
ordinary-Singular polynomial-ring compiler (`tc`/`lowzero` in `ring RR=
(0 or 65521), (...), dp`); it is not this replay, it has no verdict, and
its `excessControl` differentiated the face with respect to the *leading*
center `a3`, which would have falsely rejected the genuine `kk a^2`
terms. V4 does not inherit that defect.

---

## Attack 4 — odd redundancies and `D(p*m)` elimination by hand

From the reconstructed polynomials, not from producer code:

```text
(3 p^2 / 32) C1 = -9 r1 m^2 p^2 / 256 + 9 s0 m p^2 / 128,
-(p / 4) C3     =  3 r1 m^2 p^2 / 128 + 3 x y m p / 32 - 3 s0 m p^2 / 64.
```

Summing, `r1 m^2 p^2` coefficients `-9/256+6/256=-3/256`, `s0 m p^2`
coefficients `9/128-6/128=3/128`, and `x y m p` coefficient `3/32`, which
is exactly `C5`. Likewise

```text
(p^2 / 32) C3 = -3 r1 m^2 p^3 / 1024 - 3 x y m p^2 / 256 + 3 s0 m p^3 / 512,
-(p^3 / 64) C1 =  3 r1 m^2 p^3 / 512 - 3 s0 m p^3 / 256,
```

sum to `C7`. These are polynomial identities, not localized on `D(p*m)`.

On `D(p*m)`, `C1=0` divides by the unit `3m/4` and yields `s0=r1 m/2`.
Substituting into `C3` cancels the `r1` pair and leaves `-3 x y m / 8`,
hence `x y=0` on `D(m)`. The identities of the previous paragraph then
force `C5=C7=0` automatically. From `C4=0`,

```text
d4 = 3 x^2 m^2 / 32 - 3 r0 m^2 p / 16 - 3 y^2 p / 16.
```

From `C6=0`, divide by the unit `p^2` and solve for `d2`:

```text
d2 p^2 / 128
  = d6 p^4 / 512 + 3 r0 m^2 / 64 - 3 y^2 / 64 + 15 kk a^2 p^5 / 1024,
d2 = d6 p^2 / 4 + 6 (r0 m^2 - y^2) / p^2 + (15/8) kk a^2 p^3.
```

Substitute this `d2` into `C2=0`. The `d6` coefficients are
`3/128-1/32=-1/128`, the `r0 m^2` coefficients are `-3/8-3/4=-9/8`, the
`y^2` coefficients are `3/4+3/8=9/8`, and the center coefficients are
`-15/64+15/128=-15/128`, so

```text
dm = -d6 p^4 / 128 - (9/8) r0 m^2 + (9/8) y^2
     - (15/128) kk a^2 p^5.
```

These are the five displayed formulas. They are a parametrization of the
grade-48 block on `D(p*m)`, not a unit.

---

## Attack 5 — unit-center projective witnesses; SURVIVES, not a hidden unit

The charged unit-center points with `p=m=a=kk=1` are exactly the
elimination formulas of Attack 4:

```text
D(x): x=1, y=0, r0=r1=s0=d6=0,
      d2 = 0 + 0 + 15/8 = 15/8,
      dm = 0 - 0 + 0 - 15/128 = -15/128,
      d4 = 3/32 - 0 - 0 = 3/32;

D(y): y=1, x=0, r0=r1=s0=d6=0,
      d2 = 0 + 6(0-1) + 15/8 = -33/8,
      dm = 0 - 0 + 9/8 - 15/128 = 129/128,
      d4 = 0 - 0 - 3/16 = -3/16.
```

Independent evaluation of all seven reconstructed polynomials at both
points is the zero tuple. No row is a nonzero constant. The H16 equality
wall produced a genuine unit `G48-32 F48=-2 p^2 m^3` on `D(p*m)`; the
present block does not. The two charts cover the residual `xy=0`, and
both are zeros rather than `1` in the localized ideal. The correct
endpoint is SURVIVES.

Row-4 omission negative: the `D(x)` point with `d4` replaced by `1/8`
leaves

```text
C4 = 3/32 - 1/8 = -1/32 ≠ 0,
```

and rows `1,2,3,5,6,7` still vanish. Omitting the correct `d4` is visible.
It is not a hidden unit of the corrected system.

---

## Attack 6 — scope

The strongest licensed statement is a fixed integral
`(H,q,alpha)=(17,7,3)` predecessor of the seven ordinary-Faber rows
inside the registered two-sided normalized affine graph, on `D(p*m)`,
at absolute grade 48. Independently confirmed content stops there.

The following are not proved, and the charged `RESULT.md` firewall does
not claim them:

- grade-51 closure, or any reduction of the odd functional through
  grades 49--51;
- rational-regrading invariance of the wall;
- literal-source or total-Rees accessibility of the graph;
- any other graph, load schedule, or `(H,q,alpha)`;
- order two, maximum twelve, `(8,12)`, or JC2.

The displayed grade-51 Kummer combination

```text
-2 m^3 p^2 + (5/4) kk a^3 p^7
```

is navigation only. It is the `q=7` boundary of the H17 upper-graph load
unit, where `(5/4) kappa a^3 E^7` ties `-2 lambda^3 M^3 E^2`. V4 does
not compute it, does not reduce it, and does not call the grade-48
survivor an arc or a contradiction. It must not be silently promoted.

---

## Verdict

CONFIRMED
