# Producer result: complete-source D1 finite band `a=2..5`

Date: 2026-08-26

Status: **DUAL-AWS PRODUCER PASS; HOSTILE REVIEW REQUIRED BEFORE
PROMOTION.**

## Exact endpoint

The frozen fixed-contact compiler passed independently over exact `Q` on
Box03 and `F_65521` on r6d.  Both engine runs returned `rc=0`; both
fail-closed validators printed

```text
validator=PASS_D1_FINITE_BAND_A2_A5_FULLSUPPORT
```

The four exact contacts and source grades are

| `a` | `ord(C)` | `ord(R)` | source grades | endpoint |
|---:|---:|---:|---:|---|
| 2 | 3 | `>=2` | 15,16 | PASS |
| 3 | 4 | `>=3` | 17,18 | PASS |
| 4 | 5 | `>=4` | 19,20 | PASS |
| 5 | 6 | `>=5` | 21,22 | PASS |

For every block, the complete frozen seven-tail source reconstructs all
three lower-load summands and all charged target rows.  The exact source
output certifies that none of `k6,k2,mu2,mu4,mu6,J` occurs through the two
consumed grades.  Thus the old V12 source-support error is absent in this
finite band; lower loads were checked and found too late rather than
silently dropped.

The source rows equal the moving lower-unitriangular Faber image of the
Laurent receiver at both grades.  This includes the moving-`p` connection,
first `A/C` corrections, `RC` when `ord(R)=a`, and `R^3` in the sole
in-window case `a=ord(R)=2`.  Both denominator recurrences pass.  After the
first row allocates the two nonzero linear factors `A_0,C_0` to opposite
roots of squarefree `L=z^2+p/2`, the next `L^2` numerator evaluates at the
`A_0` root to

```text
(3/2)*lambda^2*cv^2,
```

in both orientations.  It is nonzero on `D(p)` with nonzero `C_0` contact.
Therefore, subject to the reviewed generic-square first-normal and
half-weight hypotheses, no finite-order normalized arc exists in any of the
four listed D1 contacts on `D(p*k10)`.

The coefficient `eta` is only the grade-`a` section of `R`.  Arbitrary
`eta` covers exact contact `ord(R)=a`; setting `eta=0` gives the complete
truncation through the next grade for every `ord(R)>a`.  No unbounded
`eta=sigma^s` substitution is used.

## Custody and resource record

```text
0e428345846bac4a4327be18376187d69de761c0e52774e97a085a317eb4de7c
  /tmp/jc2_d1_finite_band_a2_a5_fullsupport_20260826T120500Z.tar.gz
0e6a3098d8c0ea578210ea47b2e33f10ca396bedbc0940a5e97cb6a2a7a43495
  aws_q_box03/compiled/square_d1_finite_band_a2_a5_q.sing
8e4845e5c907ba3b96ffc6a2dc3b1b1aeb9d89f52a32e2fecabd9601a0f7c6b1
  aws_p65521_r6d/compiled/square_d1_finite_band_a2_a5_p65521.sing
be11fa82d08d370451bf55d03ac23de677f10036340c55796264ff65dc69ee40
  stdout on both fields
9e57aef1450418cc1b23d670fd4ea4b4cf0da3282093d9d9da26d35b7f620be0
  validation on both fields
```

The exact-Q Singular process used 0.10 seconds wall time and 19,504 KiB
peak RSS; the `F_65521` control has the same mathematical endpoint.  Both
hosts reported zero swaps for these jobs.  `EVIDENCE.sha256` freezes all 28
retrieved evidence files.

## Next gate

The first load transition is `a=6`: `k6*C/L` enters exactly at the second
grade.  At `a=7` it enters already at the first grade and its next
connection is also present.  The next complete-source client should compile
fixed `a=6,7`, retain independent leading and first-jet coefficients of
`k6`, and include fail-closed negative controls deleting `k6*C`, the moving
row-basis connection, and `RC`.  It must expect possible load cancellation;
it is not a unit-target replay of this band.

## Firewall

This is a producer-tier, arcwise/set-theoretic finite-band result pending
hostile review.  It covers no `a>=6`, no positive-order/ramified `k10`, no
`p=0` or `k10=0`, no zero/infinity receiver, no fan exhaustiveness, no
scheme structure, and no full square/order-two/`(8,12)`/maximum-twelve/JC2
claim.  The exact-square Chebyshev/Pell survivor when `k6,k2` tie `k10` is
not contradicted; later complete-support clients must retain it as a
positive control.

