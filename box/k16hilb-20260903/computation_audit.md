# K=16 Hilbert / initial-ideal computation audit

## Scope and conventions

This is a read-only audit of the artifacts present in
`box/k16hilb-20260903/`; no Singular process was started.  The requested
analysis ring/order is

```text
(b4,q2_0,...,q(t-1)_0,b3), wp(1,2,...,t-1,t+1).
```

Thus there are `t` variables.  In the tables, **clean** means that the output
has `JOB_DONE`, the resource record has `exit=0`, stderr is empty, and stdout
has no Singular error marker.  **Tainted** means that numerical records were
printed but stdout contains an error.  **Legacy bridge** means a previously
computed lead monomial ideal in the older variable order was imported for a
Hilbert-series replay.  An uncompleted `.out` or a metadata `.json` alone is
not counted as a computation.

For every generated full job, the SHA-256 in its metadata JSON equals the
current `.sing` file.  For every completed clean full job, the printed GB
cardinality equals the number of printed minimal lead monomials.  The two
tainted `t=3` modular jobs also printed all 20 monomials and all 20 exponent
vectors before their parser error.

## Completed full-cone jobs

The pure powers below are the least pure generators in the printed minimal
monomial basis for this exact prompt-order `wp`.  A dash means no pure power.
`H2-`, `H2+`, and `Ht` refer to the coefficient vectors in the next section.

| t | mode / coefficient field | branch or root | status | dim | fibre length | GB / minbase | least prompt-order pure powers | Hilbert record |
|---:|---|---:|---|---:|---:|---:|---|---|
| 2 | split exact, `Q` | `y=1/5` | clean | 1 | infinite | 3 / 3 | `b4^6`; no `b3` power | `H2-` |
| 2 | split exact, `Q` | `y=2/5` | clean | 0 | 12 | 4 / 4 | `b4^6, b3^3` | `H2+` |
| 3 | exact quadratic field `Q[y]/(H3)` | generic | clean | 0 | 66 | 20 / 20 | `b4^8, q2_0^6, b3^4` | `H3` |
| 3 | `F_1009` | `y=632` | **tainted** | 0 | 66 | 20 / 20 | printed as `b4^8, q2_0^6, b3^4` | `H3` |
| 3 | `F_1009` | `y=810` | **tainted** | 0 | 66 | 20 / 20 | printed as `b4^8, q2_0^6, b3^4` | `H3` |
| 4 | exact quadratic field `Q[y]/(H4)` | generic | clean | 0 | 338 | 81 / 81 | `b4^10, q2_0^7, q3_0^6, b3^5` | `H4` |
| 4 | `F_1009` | `y=468` | clean | 0 | 338 | 81 / 81 | `b4^10, q2_0^7, q3_0^6, b3^5` | `H4` |
| 4 | `F_1009` | `y=990` | clean | 0 | 338 | 81 / 81 | `b4^10, q2_0^7, q3_0^6, b3^5` | `H4` |
| 5 | `F_1009` | `y=433` | clean | 0 | 1709 | 340 / 340 | `b4^12, q2_0^8, q3_0^7, q4_0^7, b3^6` | `H5` |
| 5 | `F_1009` | `y=760` | clean | 0 | 1709 | 340 / 340 | `b4^12, q2_0^8, q3_0^7, q4_0^7, b3^6` | `H5` |
| 6 | `F_1009` | `y=380` | clean | 0 | 8621 | 1391 / 1391 | `b4^14, q2_0^10, q3_0^8, q4_0^8, q5_0^7, b3^6` | `H6` |
| 6 | `F_1009` | `y=940` | clean | 0 | 8621 | 1391 / 1391 | `b4^14, q2_0^10, q3_0^8, q4_0^8, q5_0^7, b3^6` | `H6` |
| 7 | `F_1009` | `y=400` | clean | 0 | 43133 | 5830 / 5830 | `b4^16, q2_0^11, q3_0^9, q4_0^8, q5_0^8, q6_0^8, b3^7` | `H7` |

The new `t=7` requested-order computation has `JOB_DONE`, empty stderr, and
resource record `wall=1199.14 maxrss_kb=382420 exit=0`.  Its 5,830 printed
exponent vectors were independently parsed into
`t7_mod_p1009_b0_full_initial_ideal.tsv`; the validator checked contiguous
indices, arity/order, exact count, pairwise divisibility-antichain minimality,
and every pure-power minimum.  The validation itself completed with empty
stderr and `exit=0` in 0.75 seconds; its structured result is
`t7_mod_p1009_b0_full_initial_ideal_validation.json`.

There is no new prompt-order full output for the second `t=7` root `475`, and
no accepted full-cone output for either `t=8` root `64,352`.  All accepted
modular metadata through `t=7` records `p>8t+3`, the selected root in the
listed root pair, and nonzero `g`, `yg`, and all `2t+1` pivots.

## Weighted Hilbert series

Put

```text
D_t(s)=(1-s) product_{j=2}^{t-1}(1-s^j) (1-s^(t+1)).
```

Singular's `hilb(G,1,WTS)` supplies a numerator `N_t`; the actual weighted
series is `N_t/D_t`.  The `*_hilbert.json` files divide by `D_t`.  Every one of
the 16 decoded new-or-legacy JSON records for `t=3..7` has empty division
remainder, its coefficient sum equals its reported `vdim`, and has the
following terminating coefficient vector.  The eventual Hilbert polynomial
is therefore zero in each zero-dimensional case.

```text
H3 = [1,1,2,2,4,4,6,6,8,7,8,6,6,3,2]                         sum 66

H4 = [1,1,2,3,4,6,8,10,13,16,19,22,25,27,29,30,29,28,25,
      20,14,6]                                                  sum 338

H5 = [1,1,2,3,5,6,10,12,17,21,28,33,43,49,60,68,80,87,100,
      105,115,118,124,120,121,109,100,80,61,29,1]              sum 1709

H6 = [1,1,2,3,5,7,10,14,19,25,33,42,54,67,83,101,122,145,
      171,199,230,262,296,330,365,399,431,460,485,504,516,
      519,512,493,460,413,349,269,170,54]                      sum 8621

H7 = [1,1,2,3,5,7,11,14,21,27,37,47,63,78,101,124,156,188,
      232,275,333,390,462,534,624,710,816,917,1037,1150,1282,
      1400,1537,1655,1786,1893,2009,2089,2174,2214,2249,2230,
      2198,2099,1981,1786,1560,1251,906,468]                   sum 43133
```

`H7` is now independently supplied by the clean new `p=1009`, root-400
requested-order recurrence run.  Its decoded
`t7_mod_p1009_b0_full_hilbert.json` is byte-for-byte identical to
`legacy_t7_hilbert.json`.  Complete legacy numerator/denominator vectors are
in `legacy_t3_hilbert.json` through `legacy_t7_hilbert.json`; the new decoded
JSONs agree byte-for-byte with the corresponding legacy JSON throughout every
overlap `t=3..7`.  In particular, exact and modular data agree at `t=3,4`,
both modular roots agree at `t=3..6`, and the independent order change agrees
at `t=7`.

The field status matters.  Lengths 66 and 338 have exact characteristic-zero
computations.  Lengths 1709, 8621, and 43133 are special-fibre lengths modulo
1009;
the properness lemma can promote `dim=0`, but not these lengths or full Hilbert
series, to characteristic zero.  The same warning applies to the independently
matching modular origin of legacy `H7`.

## t=2 controls

Both rational factors were computed exactly.  With
`D_2=(1-s)(1-s^3)`, the `y=1/5` numerator is

```text
N_2,- = 1-s^6-s^7-s^8+s^9+s^10,
H_2,- = 1+s+s^2+2s^3+2s^4+2s^5+2s^6+s^7
        +(s^9+s^10)/(1-s^3).
```

It is nonterminating, has dimension one and infinite vector-space dimension,
and its minimal lead ideal is

```text
(b4^6, b4^4*b3, b4^2*b3^2).
```

Thus no pure `b3` power occurs, exactly as the negative control requires.

For `y=2/5`,

```text
N_2,+ = 1-s^6-s^7-s^8+s^10+s^11,
H_2,+ = 1+s+s^2+2s^3+2s^4+2s^5+2s^6+s^7,
coefficients = [1,1,1,2,2,2,2,1],  length = 12.
```

This is the positive zero-dimensional control.  Its four minimal lead
monomials include `b4^6` and `b3^3` in the prompt order.  The different older
figures `b4^8,b3^2` use `(b3,b4),wp(3,1)` and are not a contradiction: `wp`
tie-breaking changes after the variable permutation.

## Candidate-subset jobs

The literal prompt interval is `k=t-2,...,2t-1`; it has `t+2` rows and cannot
be a regular sequence in a polynomial ring with only `t` variables.  The
completed direct checks nevertheless record its quotient Hilbert series:

| t | selected rows | field | status | dim | fibre length | CI numerator equal? |
|---:|---|---|---|---:|---:|---|
| 3 | `1,...,5` | exact | clean | 0 | 66 | no |
| 4 | `2,...,7` | exact | clean | 0 | 359 | no |
| 5 | `3,...,9` | `F_1009`, root 433 | clean | 0 | 2001 | no |
| 6 | `4,...,11` | `F_1009`, root 380 | clean | 0 | 11354 | no |
| 7 | `5,...,13` | `F_1009`, root 400 | timeout at 1800.04 s (`exit=124`) | -- | -- | uncomputed |
| 8 | `6,...,15` | `F_1009`, root 64 | manually retired at 743.45 s (`exit=1`) | -- | -- | uncomputed |

The dimensionally corrected tail is `k=t,...,2t-1`, with exactly `t` rows:

| t | selected rows | field | status | dim | fibre length | CI numerator equal? |
|---:|---|---|---|---:|---:|---|
| 3 | `3,4,5` | exact | clean | 0 | 90 | yes |
| 4 | `4,...,7` | exact | clean | 0 | 572 | yes |
| 5 | `5,...,9` | `F_1009`, root 433 | clean | 0 | 3640 | yes |
| 6 | `6,...,11` | `F_1009`, root 380 | clean | 0 | 23256 | yes |
| 7 | `7,...,13` | `F_1009`, root 400 | timeout at 1800.07 s (`exit=124`) | -- | -- | uncomputed |
| 8 | `8,...,15` | `F_1009`, root 64 | not separately started | -- | -- | uncomputed |

All clean subset outputs have `JOB_DONE`, empty stderr, and resource
`exit=0`.  The timeout and manually retired outputs stop before a standard
basis, dimension, or Hilbert numerator and are not mathematical evidence.

## Consistency and failure audit

### Legacy bridge and order dependence

The legacy jobs import the previously printed `JPLUS_LEAD` monomials into the
older order

```text
(b3,b4,q2,...), wp(t+1,1,2,...).
```

They do not recompute the recurrence or a standard basis.  Their source modes
are the earlier exact `t=3` result and modular results at the listed roots.

| t | source mode/root | legacy status | dim | length | imported lead-generator count | least legacy-order pure powers | series |
|---:|---|---|---:|---:|---:|---|---|
| 3 | exact quadratic field | legacy bridge | 0 | 66 | 15 | `b3^2,b4^10,q2^8` | `H3` |
| 4 | `F_32029`, root 25378 | legacy bridge | 0 | 338 | 66 | `b3^2,b4^12,q2^9,q3^8` | `H4` |
| 5 | `F_32009`, root 1821 | legacy bridge | 0 | 1709 | 285 | `b3^2,b4^14,q2^10,q3^9,q4^8` | `H5` |
| 6 | `F_32003`, root 27617 | legacy bridge | 0 | 8621 | 1224 | `b3^2,b4^16,q2^11,q3^10,q4^9,q5^8` | `H6` |
| 7 | `F_32059`, root 4425 | legacy bridge, cross-checked by new requested-order run | 0 | 43133 | 5304 | `b3^2,b4^18,q2^13,q3^11,q4^10,q5^9,q6^9` | `H7` |

The new and legacy GB/minimal-basis counts and pure exponents differ, while
their order-invariant Hilbert series agree at every overlapping `t=3..7`.
That is expected: lowercase Singular `wp` includes a reverse-lex tie-break,
so permuting variables changes the initial ideal.  Neither cardinality nor
least pure exponent is an invariant of the weighted grading alone.

Each legacy output contains `// ** M is no standard basis` because the
imported monomial ideal was not marked with Singular's standard-basis
attribute.  A monomial generating set is nevertheless a Gröbner basis, and
the identical `t=3..7` decoded series give a strong replay control.  The
legacy `t=7` bridge is no longer a substitute for missing evidence: it is now
an order-independent cross-check of the completed requested-order run.

### Concrete faults and exclusions

1. `t3_mod_p1009_b0_full.out` and `t3_mod_p1009_b1_full.out` contain a parser
   error after `FULL_INITIAL_EXP_20`.  Their generated source has an extra `}`
   at line 136; Singular reports an error at line 144 and then continues to
   print pure-power lines and `JOB_DONE`.  Exit zero does not make these two
   artifacts clean.  Their dimension, length, numerator, and 20 monomials all
   precede the fault and match the clean exact `t=3` run exactly.
2. `FULL_HILB_REDUCED` is a misleading label for `hilb(G,2,WTS)` and is not
   the terminating weighted quotient series.  The independent probe
   `x^3,y^2` with weights `(1,2)` prints `[1,2,3,3,2,1]` there, whereas direct
   monomial counting gives `[1,1,2,1,1]`.  Only `hilb(G,1,WTS)` followed by
   exact division by `D_t` was used above.  The negative entries printed for
   the one-dimensional `t=2,y=1/5` case are another visible warning.
3. The first `t=8` requested-order Hilbert-target experiment,
   `t8_mod_p1009_b0_requested_target.out`, is excluded despite `exit=0` and
   `ANALYSIS_DONE`.  Its wrapper passed the conjectural Froberg numerator to
   `std(I,H,WTS)` without Singular's required trailing bookkeeping-zero
   sentinel.  The last genuine coefficient `1228` was therefore used as that
   sentinel, and the call returned the malformed one-generator seed
   (`DIM=7`).  It also lacked an independent re-standardization of the seed
   together with the input ideal.  This artifact neither tests nor certifies
   the Froberg prediction.
4. The `t=7` stated-interval and corrected-tail jobs each reached the 1800 s
   timeout (`exit=124`) before printing a dimension.  At `t=8`, the legacy
   direct and `groebner` full jobs timed out at 1800.10 and 1800.12 seconds.
   The `t=8` stated-interval job was manually retired after 743.45 seconds,
   and the legacy incremental full job was manually retired after 1325.13
   seconds, after checkpoints only through `T12` (`DIM=4`).  The manual
   retirements have `exit=1` and a terminal `halt 1`; none is accepted.
5. `t7_mod_p1009_b0_requested_target.out` is a separate, redundant
   target-optimization attempt, not the clean requested-order full run.  It
   was retired with `exit=1` after 652.79 seconds and supplies no result.
6. `hilb_help.out` is only a failed local help-browser attempt and contains a
   Singular error.  It has no mathematical evidentiary value.
7. No completed clean output has nonempty stderr.  All completed full-job
   resource records say `exit=0`; this check alone would have missed item 1.

### Final retry status (no jobs running; no new evidence)

All remaining `t=8` retries ended at the 1800-second timeout with `exit=124`:

| prime | order / method | wall seconds | last certified output |
|---:|---|---:|---|
| 1009 | legacy corrected target | 1800.11 | row grading pass |
| 1009 | requested corrected target | 1800.18 | row grading pass |
| 1009 | legacy `slimgb` | 1800.10 | row grading pass |
| 73 | legacy corrected target | 1800.09 | row grading pass |
| 73 | requested corrected target | 1800.09 | row grading pass |
| 73 | legacy corrected target with `redSB` | 1800.11 | row grading pass |

None printed `TARGET_SEED_SIZE`, a dimension, a Hilbert numerator, a pure
power, or an analysis-completion marker.  They therefore supply no seed or
full-standard-basis evidence.  A preliminary p1009 requested-target retry was
also manually retired after 39.74 seconds; it likewise printed only the
grading and row-order checks.

The p73 preexpansion itself passed the arithmetic admissibility audit:
`p=73>8t+3=67`, `H_8` has roots `34,61`, the selected fibre has
`y=34`, `g=38`, `yg=51`, all 17 high pivots are nonzero, and both independent
modular point checks passed.  These checks certify that the emitted rows are a
good reduction; because every subsequent standard-basis attempt timed out,
they do **not** give a dimension result.

The formerly active redundant `t=7` legacy-target replay was manually retired
after 1020.97 seconds, after `TARGET_SEED_SIZE=5304` but before any independent
analysis.  It is not used; the clean requested-order full `t=7` result above
remains the accepted evidence.  There are no remaining lane Singular jobs.

## Artifact notes

The `t*_full.json` files are generation metadata, not result records.  The
`t*_full.out` files contain the full minimal monomial lists, and the
`t*_full_hilbert.json` files contain decoded numerator, weighted denominator,
coefficient vector, socle degree, coefficient sum, and exact-division
remainder.  The latter exist for new full jobs at `t=3..7`; the two `t=2`
series were derived directly above from their printed numerators.

The exact-division JSON identity checks are especially strong:

```text
t=3: exact = both p1009 roots = legacy
t=4: exact = both p1009 roots = legacy
t=5: both p1009 roots = legacy
t=6: both p1009 roots = legacy
t=7: p1009 root 400 requested order = legacy
```

They establish internal consistency of the completed computations, not a
uniform formula in `t`, and do not turn modular lengths into characteristic-
zero lengths.
