# Hostile review: order-two `p=0`, `D(rs*k0)` cusp grade-12 unit

Date: 2026-08-26

Verdict: **CONFIRMED.**  On the raw normalized post-`M=0` chart

```text
p=0,     rs*k0 != 0,
c0=0,    5*k0*rs^3+96*c1^2=0,    15*k0*cs*rs^2+96*a0*c1=0,
```

the complete seven-row Faber source, formed before any grade-eleven
substitution, has sixth row at absolute `sigma`-grade twelve equal to

```text
row(6,12) = (18144/125)*k^5*tau^8
          = -(21/1024)*rs^3*u^2.                      (0.1)
```

This is a Laurent unit on `D(k*tau)=D(rs*k0)`.  The raw localized source
ideal is therefore the unit ideal on this open.  The identity does not use
a radical, Gate A, a terminal row, or a Taylor pullback.

Stored `PASS` strings, modular residues, and the producer status line were
not treated as characteristic-zero algebra.

## 0. Custody

Independently recomputed SHA-256 of every named target matches the review
prompt:

| artifact | SHA-256 |
|---|---|
| `cases/.../RESULT.md` | `fadb2794e395bfbc037aac4cd68b88eb1304ce8e58883d391f847e8a09aa4526` |
| `cases/.../RESULTS.sha256` | `9008a545ec71f0f67719c0f37c2c58ac0d3e8e9e7a4de7b20a9b2c8661c766d7` |
| `cases/.../FREEZE.sha256` | `0fc1d6f4a52d54df98d5c650611421a2e82657038840be54a6f60f95641145a2` |
| `cases/.../replay_p0_cusp_grade12_unit.py` | `31f21bce95686110fbb90dc24eb94eb9a38bd8cc5341519b795f6f1dbd7c6244` |
| grade-12 unit design | `b426aa9e516b9c1a01e3b8510ddd5ad6415e5125523fbe3e7d409ef3e657c220` |
| companion raw-chart design | `04ca7018ad1609dfd11839914ecbe214cf896ad78edd661cbeecc07f18614622` |
| `cases/.../AWS_LAUNCH_METADATA.md` | `3643549ac96ed7324eed354f90f3f217348d4442a58dd3b84fda3b5ee7c0e421` |

Every path named in `RESULTS.sha256` (23 files) and every path named in
`FREEZE.sha256` (9 files) rehashes to the printed digest, including the
canonical tails file

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
```

and the canonical JSON digest `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`
charged by the collector.  Repo `HEAD` at review time:
`418e413593120d19e15e6546eb50c985f4b1f038`.  No file other than this
review was written.

Method: source reading, hash verification, hand identities in `Q`, and
exact `Fraction` collection of the frozen tails.  No Singular, Sage,
msolve, or Lean.

---

## 1. Raw localized grade-ten algebra — PASS

The four displayed raw grade-ten rows on `p=0`, written `s=cs`, `d=rs`,
are

```text
E1 = (15/256)*k0*s*d^2 + (3/8)*(a1*c0+a0*c1),
E2 = (5/1024)*k0*d^3 + (3/8)*a0*c0 + (3/32)*c1^2,
E3 = (3/16)*c0*c1,
E4 = (3/32)*c0^2.
```

`E4=0` gives `c0^2=0`.  On `D(d*k0)` the term `(5/1024)*k0*d^3` is a unit,
so `E2=0` makes `c1^2` equal to a unit plus a multiple of the nilpotent
`c0`.  In the localized ring a unit plus nilpotent is a unit, hence `c1`
is a unit.  Then `E3=0` is `c0` times a unit, so `c0=0` in the raw
localized quotient, not merely in its radical.

The remaining two rows become, after clearing the nonzero rationals
`1024` and `256`,

```text
5*k0*d^3 + 96*c1^2 = 0,
15*k0*s*d^2 + 96*a0*c1 = 0.
```

No saturation by `c0,c1,d` and no radical is used.  The companion
derivation `c0*H2 - c1*(c0*c1) - 4*a0*c0^2 = (5/96)*k0*d^3*c0` is an
identity, and localization by `k0*d` again forces `c0=0` raw.

The parametrization

```text
rs = -(96/5)*k*tau^2,     c1 = (96/5)*k^2*tau^3,
a0 = k*tau*d,             cs = -d/3,     k0 = k,
k*tau != 0
```

substitutes into both remaining generators and yields zero identically.
The inverse on the localized quotient is

```text
tau = -c1/(k0*rs),     d = -3*cs = a0/(k0*tau).
```

Direct substitution recovers `tau` and `d`.  Also `u=c1/rs=-k*tau`, so
`u` is a unit on `D(k*tau)`.  Because `rs*k0=-(96/5)*k^2*tau^2`, the
opens `D(k*tau)` and `D(rs*k0)` coincide in characteristic zero.  This is
a Laurent-chart isomorphism of the localized raw quotient with a Laurent
polynomial ring in `k,tau,d` and the remaining free source coordinates.

---

## 2. Collector independence and completeness — PASS

The collector `replay_p0_cusp_grade12_unit.py` is a self-contained exact
`Q` sparse multiplier.  It does not import the grade-10/11 Singular
emitter, the terminal DAG, or any stored Singular answer.  The file
`compile_p0_cusp_g10_g11.py` is hashed as a freeze pin and never loaded.
Expected pivots and the unit monomial are assertion targets after the
collection, not inputs to it.

Primitive series on the normalized chart, with `Lambda=sigma^2`:

```text
p  = 2*ell1*sigma + 2*ell2*sigma^2,
cs = -d/3 + cs1*sigma + cs2*sigma^2,
rs = -(96/5)*k*tau^2 + rs1*sigma + rs2*sigma^2,
A  = (a1*z + k*tau*d) + sigma*(aa1*z+aa0) + sigma^2*(aaa1*z+aaa0),
C  = ((96/5)*k^2*tau^3 * z + sigma*(e1*z+e0) + sigma^2*(ee1*z+ee0))/2,
k10 = k + k1*sigma + k2c*sigma^2,
```

together with `k6` shifted by `sigma^12` and `k2` shifted by `sigma^20`.
These are exactly the second-correction jets the design requires, plus
both later loads.  The seven coefficient series of `f` reproduce the
frozen `source_coefficients` of the grade-10/11 compiler, restricted to
the chart `c0=0` and (1.4).  All 120 sixth-row tails, and all tails of
the other six rows, are consumed.  The weight contract
`sum n_i wt_i = 12+ell` holds for every frozen monomial.

Independent exact collection of those tails, using the collector's own
series ring but not its assertions, gives:

- every row of grade `<10` is the zero polynomial;
- every normalized grade-ten row is the zero polynomial;
- unreduced `row(4,11)=-(864/25)*k^4*tau^6*ell1`;
- unreduced `row(3,11)=(18/5)*k^2*tau^3*e0` (no `ell1` term even before
  the allowed drop);
- unreduced `row(6,12)=(18144/125)*k^5*tau^8`.

The collector truncates `p` at `ell2` and truncates `R,A,C,k10` at order
two.  That is the design's "required order", not an accidental slice.
As a hostile extra-jet control, the same sixth-row collection was rerun
with `ell3,ell4,cs3,rs3`, third `A`/`C` jets, `k10_3`, and `k6_1`
adjoined.  Grades 10, 11, and 12 of row six were unchanged.  Lower loads
`k6,k2` cannot meet weight `18` at `sigma`-degree `12` on this chart:
`wt(k6)=6` and `wt(k2)=10`, while every `a_i` has positive `sigma`
valuation.  Targets are absent from the ten-tuple tails; they enter only
by the charged convention of Section 6.

---

## 3. Absolute grade, half-weight, and Faber connection — PASS

The collector indexes coefficients by the literal exponent of `sigma`.
Load shifts `4,12,20` are `Lambda^2,Lambda^6,Lambda^10` with
`Lambda=sigma^2`.  Tail homogeneity uses the half-weight vector
`(8,7,6,5,4,3,2,2,6,10)` on `(a0,...,a6,k10,k6,k2)`.  Thus "grade 12"
means `[sigma^12]`, not `[Lambda^12]`.  This is the same convention as
the charged square-ladder `tail_text` (`Lambda^{LOAD_WEIGHT}`) and as
the grade-10/11 compiler's replacement `Lambda -> sigma^2`.

The tails are already Faber/source polynomials.  The moving
ordinary-to-Faber rule

```text
g11[ell] = h11[ell] + ((ell-2)/2)*ell1*h10[ell-2]     (ell>=3)
```

is therefore included, not omitted.  On the normalized chart every
`h10` coefficient vanishes (independently recomputed: all seven
grade-ten rows are the zero polynomial), so `g11=h11`.  At grade twelve
the possible connection terms are multiples of `ell1` against a
grade-eleven row, or of `ell1,ell2` against a grade-ten row.  The
grade-ten rows are zero, and the unreduced sixth row at grade twelve
contains neither `ell1` nor `ell2`.  No moving-centre connection
survives in (0.1).

---

## 4. Grade-eleven fourth and third pivots — PASS

From the charged analytic receiver, with `c1=(96/5)*k^2*tau^3`,

```text
[z^{-4}] H11 = -(3/32)*ell1*c1^2
             = -(3/32)*(96/5)^2 * k^4*tau^6 * ell1
             = -(864/25)*k^4*tau^6*ell1,
[z^{-3}] H11 mod ell1
             = (3/16)*c1*e0
             = (3/16)*(96/5)*k^2*tau^3*e0
             = (18/5)*k^2*tau^3*e0.
```

Both identities are hand-exact in `Q`.  Independent tail collection
reproduces them as the complete unreduced polynomials `row(4,11)` and
`row(3,11)`.  On `D(k*tau)` the coefficients `-864/25` and `18/5` are
units of `Q` (only the prime `5` appears in a denominator).  Hence
`ell1=0` and then `e0=0` in the raw localized quotient, without a
radical.  The later triangular solutions for `e1,aa0` are not used.

---

## 5. Raw grade-twelve sixth row — PASS

Before any grade-eleven substitution, independent collection of all 120
sixth-row tails yields exactly one monomial, `(18144/125)*k^5*tau^8`.
No `ell1`, `e0`, second correction, moving load, or lower load remains.

The companion Laurent calculation, using only leading `R0,D0,k0` on the
chart, produces the same rational:

```text
[z^{-6}] (-(3/8)*R0*D0^2/L^4) = -(3/128)*rs^3*u^2,
[z^{-6}] (-(5/128)*k0*R0^4/L^3)
       = -(5/32768)*k0*rs^4
       = +(3/1024)*rs^3*u^2,
```

the second step by `5*k0*rs+96*u^2=0`.  Sum `-21/1024 * rs^3*u^2`.
The two displayed geometric terms are the only degree-`2` (resp.
degree-`0`) numerators that can produce pole six; higher `R0` or `D0`
summands raise the `z`-degree.  Second corrections of `R,A,C`, the
`k10 D K^{1/2}` cross term, and `k6 L^3` have strictly smaller pole
order or are polynomial, as claimed.

Chart comparison: `u=c1/rs=-k*tau`, so `u^2=k^2*tau^2` and
`rs^3=-(96/5)^3 k^3 tau^6`.  Therefore

```text
-(21/1024)*rs^3*u^2
  = (21/1024)*(96^3/125)*k^5*tau^8
  = (18144/125)*k^5*tau^8,
```

because `21*96^3/1024=18144`.  This is an identity of rational
functions, not a numerical coincidence.

Frozen-tail monomials that can meet `[sigma^{12}]` of row six by
valuation include many `a6`-heavy terms with positive slack.  Their
contributions cancel in the sum: the collected remainder is a single
monomial.  That cancellation is among charged tails, not an uncharged
equation.  Extra jets beyond second order do not disturb the remainder
(Section 2).  Row six at grade eleven is already zero, so no
grade-eleven pivot is available or needed to manufacture (0.1).

The collector's assertion drops `ell1` and `e0` before comparing to the
unit monomial.  That test would not by itself prove absence of those
variables.  The stored JSON field
`grade12_row6_before_pivot_reduction` and the independent unreduced
collection both show there was nothing to drop.  The weakness is in the
assertion, not in the identity.

---

## 6. Targets, unit, and exclusion mechanism — PASS

The charged target vector is `(0, mu2, 0, mu4, 0, mu6, J/4)`.  The
square-ladder compiler inserts `-Lambda^{12+ell}*target`; the
grade-10/11 compiler inserts `-sigma^{2*(12+ell)}*target`.  These agree
under `Lambda=sigma^2` and give first target grades

```text
mu2: 28,     mu4: 32,     mu6: 36,     J: 38.
```

Row six therefore has no target at grade twelve (first possible target
grade 36).  The collector hardcodes those four grades rather than
emitting a target series; at `MAX_DEGREE=12` a `mu6*sigma^{36}` term
could not appear in any case.  The convention is independently the
charged one.

On `D(k*tau)` the monomial `k^5 tau^8` is a Laurent unit and
`18144/125` is a unit of `Q`.  Equivalently, on the original open,

```text
-(1024/(21*rs^3*u^2))*row(6,12) = 1,
```

with `rs*u` a unit.  A single raw unit in the source ideal kills the
localized chart.  No radical, no Gate A, no later terminal row, and no
finite Taylor/global overlap is used or needed.

---

## 7. Focused four-monomial sentinel — PASS

At `rs=u=1`, `s=a1=0`, `k0=-96/5` (equivalently `k=-96/5`,
`tau=5/96`), the specialized polynomial is

```text
a4=(1/2)*sigma^2,     a1=(1/2)*sigma^5,     a0=(1/16)*sigma^4,
k10-load = k*sigma^4,
```

and `a6=a5=a3=a2=0`.  Exactly four sixth-row frozen tails are supported
on `{a0,a1,a4,k10}`:

| monomial | tail coefficient | focus value |
|---|---|---|
| `a4^4 k10` | `15/2048` | `-9/1024` |
| `a1^2 a4` | `-3/32` | `-3/256` |
| `a0 a4^2 k10` | `-5/128` | `+3/256` |
| `a0^2 k10` | `5/32` | `-3/256` |

Each evaluation is a product of the specialized leading coefficients
with the frozen tail coefficient; none of them passes through
`(18144/125)*k^5*tau^8`.  The sum is `-21/1024`.  No other sixth-row
tail lives on this support, so the count four is exact.  This is an
independent Faber-index and sign control.

---

## 8. AWS records and negative controls — PASS

Two registered exact-`Q` lanes:

| | Box03 | r6d |
|---|---|---|
| host | `ip-172-30-0-249` | `ip-172-30-0-45` |
| tag | `...T110537Z_Box03_exact` | `...T110537Z_r6d_exact` |
| `engine_rc` | 0 | 0 |
| wall | 0.81 s | 0.80 s |
| max RSS | 18996 KiB | 18864 KiB |
| result SHA-256 | `59728f3bf784d6e9a4e45b3a684511a83fc2630a968822291b00cf1a435a1ff7` | `99be700dc6ccd07df46f772aa6661cac7173b74cf701016748b056d1b5a0aee2` |
| stdout SHA-256 | `55d2a2e353b95d1484e5abd91758d56a6b2bac01da455887319b8fb6b3bbc22e` | `ca64d0943aacb5b4c101d2c3b47663429929b863f507ecc73a27b125dae1bfde` |
| stderr SHA-256 | `514367ebfb64c511ea1c0b7d485de36260be8985dcdb427e566f7b8cfc56e295` | `bda9a7e3105666fa8bcd36c425f0e340f36aa446d96ca40b07f3abd7f2b9479b` |
| validation SHA-256 | `77b751d9cad6cf74975a8bfdbc56115b4ecdd6c2b22ff569da48a2153429ba6c` | same two-line payload |
| freeze_check | `5fa4f3eba1aeb80230b0a6e633437d85ea2307600d1afce4e91c9fe156c8a692` | same `OK` list |

The two `result.json` objects differ by exactly one field, the
registered lane tag.  Every mathematical field agrees, including
`characteristic: 0`, the unreduced unit monomial, the four focused
contributions, and the control residues `19859 mod 32003` and
`5911 mod 65521`.  Both residues are `(18144/125) mod p` and are
nonzero.  Independently, `21/1024` reduces to `7782 mod 32003` and
`26298 mod 65521`, both nonzero (`32003` and `65521` are odd primes
larger than `7`, and `1024=2^{10}`).

The collector performs every exact `Q` identity check before writing
modular residues.  Characteristic zero is carried by those `Fraction`
identities, independently recomputed here, not by the modular line or
by `validator=PASS_P0_CUSP_GRADE12_UNIT_REPLAY`.

---

## 9. Scope — PASS

Confirmation licenses only raw localized exclusion of the post-`M=0`,
`p=0`, `D(rs*k0)` cusp open in this `(8,12)`, exact-order-two, `[6,2]`
client.  It does not cover:

- the odd chart `V(rs) intersect D(cs*k0)`;
- the residual `R=C=0` zero section;
- moving or ramified `p`, or `k0=0`;
- finite Taylor or global overlap (Gate A is unused and unproved here);
- all square strata, all order two, maximum twelve, or JC2.

The producer report states the same firewall.  No scope leak was found
in the collector output, the designs, or `RESULT.md`.

---

## Verdict table

| Item | Charge | Finding |
|---|---|---|
| 0. Target and manifest hashes | every named file | all match |
| 1. Raw `c0=0` then (1.2) | four grade-ten rows | raw localized, no radical; Laurent isomorphism `(k,tau,d)` |
| 2. Collector independence | tails vs Singular | sparse `Q` multiplier; freeze-pin only of the 10/11 emitter |
| 2. Completeness | second corrections, loads, targets | present through required order; extra jets do not change (0.1) |
| 3. Grade convention | `[sigma^{12}]` vs half-weight | literal `sigma`; loads `Lambda^{2,6,10}` |
| 3. Faber connection | moving `p` at grades 10–12 | `h10=0`; unreduced `g12[6]` free of `ell1,ell2` |
| 4. Pivots | hand and tails | both exact; coefficients units on `D(k*tau)` |
| 5. Unreduced `g12[6]` | all 120 sixth-row tails | exactly (0.1), before any pivot |
| 5. Two Laurent terms | pole six | `-3/128+3/1024=-21/1024`; chart conversion exact |
| 6. Targets | `2*(12+ell)` | first grades 28, 32, 36, 38; row six has none at 12 |
| 6. Unit | Laurent localization | kills the open; no Gate A / terminal / Taylor |
| 7. Focused four tails | independent Faber evaluation | `-9/1024,-3/256,+3/256,-3/256`; sum `-21/1024` |
| 8. Dual AWS exact `Q` | two hosts | differ only by lane tag; modular residues nonzero controls |
| 9. Scope | firewall | cusp `D(rs*k0)` after `M=0` only |

No failing coefficient, missing charged source term, illegal reduction,
hash mismatch, or scope leak.

ORDER2_P0_CUSP_GRADE12_UNIT_CONFIRMED
