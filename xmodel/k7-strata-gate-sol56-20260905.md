# HOSTILE GATE: K=7 beta-strata closures b=9,...,13

Lane `k7-strata-gate-sol56-20260905`; frozen-input root
`/tmp/jc2-lane.qb6I1q/inputs`; evidence root
`box/k7-strata-gate-20260905/`.  No ledger, `jc2-lean`, or `ideation-*` file was
read or edited.

## Verdict

**CONFIRMED-WITH-FIX; promote all five closures.**  On every one of the ten
charts the independently reconstructed, denominator-cleared integral generator
file is byte-for-byte the frozen producer file, and a new characteristic-zero
msolve 0.10.1 run returns the reduced basis `[1]`.  A separately packaged
msolve 0.6.5 build also returns `[1]` on the same bytes.  Exact Singular
cofactor certificates for three distinct charts multiply directly to 1.

The required fix is a ring-typing correction, not a failed closure.  The full
MASTER-cut construction introduces the auxiliary scalar `lam`; the light
construction does not.  Thus the producer's literal claim that light drops
only rows and never an unknown, with both ideals in one unchanged ring, is
false if `lam` is counted.  No geometric `h`, lower-`B`, or active top-`q`
coordinate is dropped.  With

```text
S = Q[h_ij, B_ij, active q, q_pin_inv],       T = S[lam],
```

the checked statement is `I_light*T subset I_full` in `T`.  Consequently
`1 in I_light` implies `I_light*T=T` and then `I_full=T`.  The theorem-cut
ideal is still empty on every chart.  Each per-chart verdict is therefore
`CONFIRMED-WITH-FIX`, and none is refuted.

The b=8 control has the disclosed mixed actual status: q0 is `[1]`, while q1
produces no result by the 2400-second cap.  Since both cover charts are needed,
b=8 remains OPEN.  This is not a non-unit claim.  After the banked b=5 unit and
the five promoted closures, the K=7 open degree indices are exactly `{6,7,8}`;
"open" does not assert attainment.

## 1. Frozen custody

Before substantive work, `verify_inputs.sh` mechanically read the receipt's
numbered `_basename` and `_sha256` fields with `awk`, created
`frozen-inputs.sha256`, and ran `sha256sum -c`.  The retained
`frozen-inputs.check.log` says 7/7 `OK` and no mismatch.  The matched digests
are:

```text
2af3e012...f25be4c  k4ray-strata-solve-opus5-20260905.md
689e3ed8...d508ae  k4ray-beta-strata-grok46-20260905.md
2befb3ca...96a2a  k4ray-degree-tower-opus5-20260903.md
eed2cdf5...47e43  pinned_chart.py
501f3b1f...781f3  guided_gb.py
a9da94d3...11c4c  fleet.sh
e47fd16c...c38f5  FALLACY-v2.md
```

All construction comparisons used these frozen copies.  The fresh output root
was separate from the producer root.

## 2. Independent chart reconstruction

For K=7 the charged data give `H=y^6(y-x)`.  LEVEL 4 and the exact
`deg_y beta <= 6` normal-form cap give

```text
P = y^4(y-x)Q,  d=b-5,  deg_y Q<=1,
Q = q0*x^d + q1*x^(d-1)*y.
```

The q0 chart keeps both `q0,q1` and adds `q0*q0_inv-1`.  The q1 chart imposes
`q0=0`, keeps `q1`, and adds `q1*q1_inv-1`.  Those two opens cover every
nonzero `(q0,q1)`, hence every leading form of exact degree b.  Suppressing
`q0` in the q1 chart is its defining equation, not a floor.

The independently rebuilt `h` box consists of all `(i,j)` with `i+j<=6`
except `(0,6)`, hence 27 coefficients.  The exception is the charged monic
gauge.  The lower beta variable `B=2 beta` has exactly

```text
{B_i_j: 0<=j<=6 and 0<=i<=b-1-j},       count 7b-21,
```

giving 42,49,56,63,70 coefficients for b=9,...,13.  There is no D2/weight
floor in this selection.  The cap `j<=6` is the charged normal-form theorem,
not a discarded coordinate.  The only other chart variable is the relevant
Rabinowitsch inverse.  Fresh prelude markers on all ten say
`TARGET_FOUND 1`, `PRE__CST_ZERO 0`, `PRE__HOMOG_I 1`,
`PRE__HOMOG_CST 1`, and `PRE__THEOREM_SKIPPED disabled`.

`chart_structure_audit.py` imports the charged `QUOY`, boxes, naming and joins
from `pinned_chart.py`, then reconstructs names, weights, `Q`, `Btop`, forced
rho top, rho rows, ID6 Jacobian rows, target row, localizer and, separately,
the MASTER rows.  All 20 independently built light/full Singular preludes
equal the producer strings byte-for-byte.  It then parses each fresh Singular
dump, checks `cleardenom(ROWS[i])`, independently reapplies the declared
longest-name-first `v_i` alias map, and recreates the `.ms` file.  All ten are
byte-for-byte equal to the frozen exact-Q custody hashes; characteristic is 0
and no generator contains `/`.

| b | chart | variables | generators | bytes | identical SHA-256 |
|---:|:---:|---:|---:|---:|:---|
| 9 | q0 | 72 | 241 | 12,675,213 | `15b4b715767a72e152f340dda11354af380897f6670d6370f0542841cdb4c275` |
| 9 | q1 | 71 | 235 | 11,511,528 | `09002c7229da517ca0d809f925873aeb94d44650467bd6addf71268aacbb7934` |
| 10 | q0 | 79 | 261 | 19,173,893 | `273a1a0f65308af6019c3b8986fa921c76d4e27da30d0b675afc532bc3f3d434` |
| 10 | q1 | 78 | 255 | 17,715,692 | `a49433e9834c4fa7a76a89aef50e7f3852ee0e26ff1d665bc1c8516dc390f97d` |
| 11 | q0 | 86 | 281 | 27,133,266 | `e8e57139c2292f0535226e7fb8fc2fac90b459685e939b825abec31531b2367e` |
| 11 | q1 | 85 | 275 | 25,367,692 | `42f96a5f916e94457887e933cb8cb3f8656537e1547e719e30851075990fd4f1` |
| 12 | q0 | 93 | 301 | 36,605,124 | `3a3821db1511fa96096f627d5d5ed23b1b60a2c95022f33dfb90791a4c60561d` |
| 12 | q1 | 92 | 295 | 34,517,061 | `875573726b784dc4700de3835f0130617279eb5bab451f712f77088c26cae4e2` |
| 13 | q0 | 100 | 325 | 47,622,625 | `970026efbf5ffd1150def477d64de057b8212455527a15f6abbf18807d5cce2c` |
| 13 | q1 | 99 | 317 | 45,201,213 | `570e241e4e2515d1c97c77f9b7696e5d519fb97697543da93410ca5eb2797a8b` |

The charged construction licences are beta-strata report lines 43--73 and
`pinned_chart.py` lines 79--104, 148--175 and 180--245.  The producer's
beta-strata and solve drivers differ only in their output-root assignment, but
the comparison above rebuilt the algebra rather than relying on that textual
fact.

## 3. The rows omitted by I_light

With `Al=4 alpha` and `Rh=4 rho`, the denominator-cleared E identity is

```text
E64 = 8*B^3 - 48*Rh*h^2 - 72*B*Rh + 9*Al^2 = 64*(g^2-f^3).
```

For each chart the omitted generators are exactly the nonzero coefficients

```text
[x^i y^j](E64 - lam*(h^2+B)),       i+j>13.
```

No rho, Jacobian, target, localizer, `h`, lower-`B`, or active-top row or
coordinate is removed.  Put `D=i+j`.  On every chart their common support is

```text
D=14..20:       j=0..D
D=21..2b+10:    j=0..20.
```

The exact tails (each notation means every integer j in the interval) and
raw/simplified counts are:

| b | chart | D=2b+11 | D=2b+12 | D=2b+13 | rows |
|---:|:---:|:---:|:---:|:---:|---:|
| 9 | q0 | 2..20 | 8..20 | 14..20 | 333 |
| 9 | q1 | 4..20 | 10..20 | 16..20 | 327 |
| 10 | q0 | 2..20 | 8..20 | 14..20 | 375 |
| 10 | q1 | 4..20 | 10..20 | 16..20 | 369 |
| 11 | q0 | 2..20 | 8..20 | 14..20 | 417 |
| 11 | q1 | 4..20 | 10..20 | 16..20 | 411 |
| 12 | q0 | 2..20 | 8..20 | 14..20 | 459 |
| 12 | q1 | 4..20 | 10..20 | 16..20 | 453 |
| 13 | q0 | 2..20 | 4..20 | 12..20 | 507 |
| 13 | q1 | 4..20 | 8..20 | 15..20 | 498 |

`theorem-row-support.json` lists every `(D,i,j)` explicitly.  Its proof is
deterministic: monic division supplies the exact upper bounds
`deg_y Al<=5`, `deg Al<=2b-7`, `deg_y Rh<=6`, `deg Rh<=2b-1` and top-band
divisibility by `y^2` on q0 or `y^4` on q1.  The degree-2b remainder cancels
because `B_b^2/H=4y^2(y-x)Q^2`.  Exact integer specializations witness every
coefficient permitted by those bounds; Singular exact-Z arithmetic separately
re-evaluated `Al`, `Rh`, `E64-lam(h^2+B)` and the support, 100/100 checks.  No
probabilistic generic-nonzero inference is used.  Here `simplify(...,2)` only
removes zero entries, so raw and printed counts agree.

The full prelude prints `PRE__THEOREM_CUTOFF 13` and the row count.  Its licence
is the charged MASTER theorem, degree-tower report lines 167--186: for K>=7 a
unique lambda has `deg(g^2-f^3-lambda*f)=K+6`; K=7 gives cutoff 13.  Scaling by
64 only rescales lambda.  The E-CUBIC source is lines 120--123.  Light instead
prints `PRE__THEOREM_SKIPPED disabled`.  Large redundant symbolic E-row
enumerations were resource-preempted; they are not results and are superseded
by the exact support proof just described.

## 4. Exact-Q Gröbner reruns

Every run below consumed the identical integral `.ms` bytes in the table,
whose second line is characteristic 0, with `-g 2`; every successful output
has basis length one and body `[1]`.  The primary fresh engine is official
msolve 0.10.1, binary SHA-256
`0436525b06fe83b1a6a00097a96d9bcafdc40d8de6315c724b9ada9a4c04ff5f`.
The fallback is the independently packaged Ubuntu/Debian msolve 0.6.5-1build2,
binary SHA-256
`c2722288d22c3a1eab00c0b818d0204d4a98104d059b2fd4ecb7343e8ef759fa`
(package SHA-256
`dbbca584ac7518ed3924e5614a5b83ace6f89de6ab561ca63b336499fb3f575d`).

| b | chart | msolve 0.10.1 exact Q | msolve 0.6.5 exact Q | chart verdict |
|---:|:---:|:---:|:---:|:---:|
| 9 | q0 | `[1]`, 16:53.78 | `[1]`, 23:03.20 | CONFIRMED-WITH-FIX |
| 9 | q1 | `[1]`, 1:59.46 | `[1]`, 6:18.90 | CONFIRMED-WITH-FIX |
| 10 | q0 | `[1]`, 0:15.69 | `[1]`, 0:16.97 | CONFIRMED-WITH-FIX |
| 10 | q1 | `[1]`, 0:19.82 | `[1]`, 1:09.10 | CONFIRMED-WITH-FIX |
| 11 | q0 | `[1]`, 0:13.02 | `[1]`, 0:13.70 | CONFIRMED-WITH-FIX |
| 11 | q1 | `[1]`, 0:10.71 | `[1]`, 0:11.28 | CONFIRMED-WITH-FIX |
| 12 | q0 | `[1]`, 0:04.00 | `[1]`, 0:04.52 | CONFIRMED-WITH-FIX |
| 12 | q1 | `[1]`, 0:03.63 | `[1]`, 0:04.04 | CONFIRMED-WITH-FIX |
| 13 | q0 | `[1]`, 0:05.15 | `[1]`, 0:05.93 | CONFIRMED-WITH-FIX |
| 13 | q1 | `[1]`, 0:04.78 | `[1]`, 0:05.56 | CONFIRMED-WITH-FIX |

The two b=9,q0 successes peaked at 34,823,016 and 34,889,000 KiB and both are
within 40 minutes.  A separate local, two-thread 0.6.5 attempt reached its
exact 2400-second watchdog with `rc=124` and empty output; the recorded
eight-thread run of the same independently packaged build is the `[1]` result
in the table.  The result classifier strips only comments/whitespace and
requires the complete Gröbner-basis body to be literally `[1]:`; all 20
chart/build records pass, not merely their printed basis-length fields.

Singular 4.3.2 scripts declared coefficient field Q and `option(redSB)`.
Ordinary full `std` was resource-preempted without a basis on b9q0/q1 at
24:07/21:40, b10q0/q1 at 14:58/18:41, b11q0/q1 at 12:26/11:25, and b12q0/q1
at 8:40/8:39; the exact peaks and reasons are in `preemption-ledger.tsv` and
none is interpreted algebraically.  Singular `liftstd` did finish on both
b=13 full generator sets, returning the singleton unit and direct identities
below.  Per the gate's fallback rule, the all-chart verdict explicitly relies
on the two independent msolve builds where ordinary Singular `std` did not
finish.

## 5. Explicit cofactor identities

Generator indices below are one-based in the frozen/fresh `.ms` order.  Each
certificate was constructed over exact Q by Singular `liftstd`; a separate
`matrix(I)*T` multiplication reduced literally to the constant 1.

1. **b=13,q1 (317 generators).**  Only cofactors 1 and 317 are nonzero:
   `a1=v98^3`, `a317=-(v97^2*v98^2+v97*v98+1)`.  Here
   `g1=v97^3`, `g317=v97*v98-1`; with `t=v97*v98`, the identity is
   `t^3-(t^2+t+1)(t-1)=1`.  Output markers are `GB_SIZE 1`, `UNIT 1`, and
   `DIRECT_CHECK 1` (Singular timer 7 seconds).

2. **b=13,q0 (325 generators).**  Only cofactors 2, 8 and 325 are nonzero:
   `a2=-(143/175)v99^3`, `a8=(3/175)v99^3`, and
   `a325=-(v97^2*v99^2+v97*v99+1)`.  The recorded generators are
   `g2=v97^3-3v97^2*v98`, `g8=106v97^3-143v97^2*v98`, and
   `g325=v97*v99-1`.  The first two products sum to `(v97*v99)^3`; the last
   is `1-(v97*v99)^3`.  Markers again say `GB_SIZE 1`, `UNIT 1`,
   `DIRECT_CHECK 1` (Singular timer 8 seconds).

3. **b=12,q1 (295 generators).**  Exact minimization found the six original
   indices `12,13,15,17,18,295`, the last being `v90*v91-1`.  Singular's
   localized lift on the first five gives explicit rational cofactors whose
   sum times the rows is `v90^25`; these are retained in the 3.0-MiB
   `K7_B12_Q1_core_localized_clear25.out`.  The polynomial-ring verifier
   multiplies those cofactors by `v91^25` and assigns the localizer cofactor
   `-(1+t+...+t^24)`, `t=v90*v91`.  On the full-source hash
   `87557372...4cae4e2`, exact Singular multiplication prints
   `DIRECT_CHECK_POLYNOMIAL 1` and `CHECK_VALUE 1`.  All other 289 cofactors
   are zero.  Thus this is a polynomial identity in the original ring, not a
   localization-only assertion.

The complete, parseable cofactors and check programs are under
`cert-audit/lifts/`.  Modular subset searches were only heuristics; every
identity stated here was generated and multiplied in characteristic zero.

## 6. b=8 control: actual status

Fresh b=8 emissions from the same construction are byte-for-byte the frozen
files:

```text
q0: 65 variables, 221 generators, 7,580,109 bytes,
    SHA-256 24507c39c2e3e6385e233fc79bb58dc586338de50c3c06851d96e2192b5f068b
q1: 64 variables, 215 generators, 6,701,623 bytes,
    SHA-256 062ccc0c7dc7e83aee99f2cf1a8d2a6b7c05c82e1a468e9d6a97557eae511f25
```

Both have the correct target/nonzero/homogeneity/localizer markers.  The
charged q0 exact-Q computation actually returned basis `[1]`, length one, in
1424.280 solver seconds (1463.834 seconds total), inside 40 minutes.  Thus q0
does **not** behave as a non-unit negative control.  The charged q1 run was
preempted with `rc=-9` after 2454.917 seconds and zero output.  A fresh exact-Q
q1 run on the identical bytes with msolve 0.10.1 reached the exact 2400-second
hard cap: `rc=124`, zero stdout, zero `.msout`, last observed RSS 37,099,468
KiB.  Its result is `OPEN/TIMEOUT`, not `NONUNIT`.

The cover is `q0!=0` together with `q0=0,q1!=0`; a unit on q0 alone does not
close their union.  The combined b=8 status therefore remains
`OPEN (one-cover partial)`.  The requested negative did not return `[1]` on
the unresolved q1 chart within budget, but did return `[1]` on q0; both facts
are reported rather than forcing the expected label.

## 7. K=7 range logic

The charged degree-tower report, lines 349--362, gives

```text
b_min = max(ceil((2K+1)/3), ceil(2(K-1)/3)+1),   b_max=2K-1.
```

For K=7, `smin=ceil(12/3)=4`, the two lower entries are 5 and 5, so
`b_min=5`, `b_max=13`, and the residual integer interval is `{5,...,13}`.
The dispositions are disjoint:

- the composite arm covers only `deg beta=0` (degree report lines 332--341);
- the proved `3b<=2K` contradiction excludes positive b=1,2,3,4 (lines
  97--108), equivalently leaving the floor `3b>=15`;
- the banked exact-Q unit closes b=5 (beta report lines 73--75);
- this gate closes b=9,10,11,12,13 on both cover charts.

It follows exactly that the unresolved K=7 indices are `{6,7,8}`.  This is an
index census: it asserts neither a representative nor a FULL_ACTUAL_EXIT nor
existence in any open stratum.

## 8. FALLACY-v2 and promotion disposition

- **Floor/attainment:** the `3b>=2K+1` inequality is used only as a lower
  bound; no equality or witness is inferred.
- **Carrier/cover:** both q charts are required.  In particular the b=8 q0
  unit is not promoted across the unresolved q1 chart.
- **Row/unknown and ring map:** exact boxes and alias order were reconstructed,
  every image check is positive, and the auxiliary-`lam` extension is stated
  explicitly.  Matching names alone was not used.
- **MASTER:** only rows licensed by the K+6 theorem are added; no cap or
  analogy fills a gap.
- **Localization:** every localizer is an explicit Rabinowitsch generator;
  `sat()` is nowhere used.  Positive unit runs, the b=8 mixed control, and a
  synthetic non-unit parser control are distinguished.
- **Exactness:** modular work is not promoted.  All ten closure results and
  all three multiplication checks are over Q.  Timeouts and preemptions are
  typed OPEN/engine-limit, never non-unit or geometric survival.
- The flag/place/series, per-ray charge, pole/interior,
  prime-label/derivative, merge/M-descent and target/arrival traps are not
  invoked by this ideal-containment gate.

No new exit-price assertion is made, so no `charge_basis` line is emitted.

## 9. Evidence and fleet custody

Primary notes are `chart-audit/CHART-AUDIT.md`, `structure-audit.json`,
`generator-comparison.tsv`, `theorem-row-support.{json,tsv}`;
`cert-audit/versions.txt`, the exact-Q `results/`, and `cert-audit/lifts/`;
and `logic-negative/{audit-notes.md,summary.json}`.  Reproduction scripts are
retained beside those results.  `CERTIFICATE-AUDIT.md` and
`results-summary.json` have SHA-256 `02238f89...e5313` and
`46254c93...40d9`; the logic summary has `907f49d3...af07`.  The chart support
JSON SHA-256 is
`dad66132dacdf1a692efa424549924f459f450fa3bc70505a39704c75cfbe7c0`;
the b=12 polynomial verifier/output hashes are
`35af3e1d11303b3c0e5fd2ba69b94a7073fe06296c38e28d050b9e27a95355eb`
and `f8c7d678b5f463a15021a40ddc05c97b511f8230a4903b3ad537e28f60b1f2bf`.

Exactly one fleet worker was launched for this lane: r7i.8xlarge
`i-0d82db109a472cb25`, private IP `172.30.0.222`, owner
`k7-strata-gate-sol56-20260905`.  The exact-ID termination command returned
`shutting-down`; an AWS exact-ID query at 2026-09-05T19:15:15Z returned
`terminated`.  No other instance was touched.  The command and verification
are retained in `fleet-instance.txt` and `fleet-termination.log`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17282`.
- Body SHA-256:
  `61da448b37bf3b0309e9435503b02f961e7536486085f1e5ade8ff6a0ee538bf`.
- Frozen basis: `90e5b152fe204c3094370e836dcfceab410dbbba`.
