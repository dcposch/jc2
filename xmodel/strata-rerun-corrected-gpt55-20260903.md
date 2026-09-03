# Corrected symbolic partition-strata rerun

Lane: `strata-rerun-corrected-gpt55-20260903`.  Inputs: `/tmp/jc2-lane.S2kb7J/inputs`.
Drivers/results: `box/strata-rerun-20260903/`.

## Manifest

MEASURED.  The manifest was generated mechanically from
`xmodel/strata-rerun-corrected-gpt55-20260903.run.v2` by pairing the
`charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines, then
running `sha256sum -c`.  All 9 frozen inputs returned `OK`.

Singular: `Singular for x86_64-Linux version 4.3.2 (4330, 64 bit) Apr  1 2024 04:44:00`.

No ledger files were edited.  No `jc2-lean` command was run.  No `ideation-*`
or in-progress lane report files were created.

Primary command:

```text
python3 box/strata-rerun-20260903/strata_rerun.py --run-all --timeout 900
```

The driver persisted every generated Singular script under
`box/strata-rerun-20260903/systems/`, every per-stratum JSON record under
`box/strata-rerun-20260903/results/`, and the tabular summary at
`box/strata-rerun-20260903/summary.tsv`.  The report is sealed only after the
run loop finishes.

## Support comparison

MEASURED.  Old support means the former rule `-i+delta1*j >= -r*delta1` with
no `k+1` x-cap on beta.  Corrected support means
`B=V2*delta1+u*delta2`, `-i+delta1*j >= r*B`, and `deg_x beta <= k+1`.
Here `d'=2`, so the only beta coefficient is `beta_2`.

| row | h support relation | beta support relation |
|---|---:|---:|
| `(33,22;30;8;k=1)` | h_all 27->27 `equal`; h_lower 23->23 `equal` | beta_2 33->28 `new_subset_old` |
| `(45,30;42;11;k=1)` | h_all 44->44 `equal`; h_lower 39->39 `equal` | beta_2 55->40 `new_subset_old` |

`(33,22;30;8;k=1)`: beta_2 is `new_subset_old`, so the old beta inventory was a superset; the h support is equal.
`(45,30;42;11;k=1)`: beta_2 is `new_subset_old`, so the old beta inventory was a superset; the h support is equal.

Differing monomials on the two primary rows:

`(33,22;30;8;k=1)`: h old-new = none; h new-old = none. beta_2 old-new = x^3*y^10, x^4*y^10, x^3*y^9, x^3*y^8, x^3*y^7; beta_2 new-old = none.

`(45,30;42;11;k=1)`: h old-new = none; h new-old = none. beta_2 old-new = x^3*y^14, x^4*y^14, x^5*y^14, x^3*y^13, x^4*y^13, x^5*y^13, x^3*y^12, x^4*y^12, x^3*y^11, x^4*y^11, x^3*y^10, x^4*y^10, x^3*y^9, x^3*y^8, x^3*y^7; beta_2 new-old = none.

Typed consequence: because `beta_2(new) subset beta_2(old)` and `h(new)=h(old)`
on both primary rows, the old saturated-empty systems were run on a support
superset in the D1 inventory.  They were not slice kills caused by missing beta
monomials.  The fresh corrected rerun below independently confirms the strata.

Full support comparison, including the two restoration rows:

| row | old h threshold | corrected B | measured relation |
|---|---:|---:|---|
| `(33,22;30;8;k=1)` | `-1/3` | `-1/3` | h_all 27->27 `equal`; h_lower 23->23 `equal`; beta_2 33->28 `new_subset_old` |
| `(45,30;42;11;k=1)` | `-1/3` | `-1/3` | h_all 44->44 `equal`; h_lower 39->39 `equal`; beta_2 55->40 `new_subset_old` |
| `(21,14;18;5;k=1)` | `-1/3` | `-1/3` | h_all 14->14 `equal`; h_lower 11->11 `equal`; beta_2 16->16 `equal` |
| `(15,10;11;2;k=2)` | `-4/3` | `-1/3` | h_all 15->13 `new_subset_old`; h_lower 11->9 `new_subset_old`; beta_2 28->16 `new_subset_old` |

Restoration support deltas: `(21,14;18;5;k=1)` is unchanged old/new for
`h_all`, `h_lower`, and `beta_2`.  For `(15,10;11;2;k=2)`, corrected support
is a strict subset of the old support: `h_all` is `15->13`, `h_lower` is
`11->9`, and `beta_2` is `28->16`.

## Rerun results

MEASURED.  Each stratum kept symbolic slopes and used saturation by
`c*Omega`, where `Omega` is the product of slope nonzero and noncollision
factors.  Each system ran controls in the declared coefficient ring before the
main saturation.  The sanity gate printed the exact degree in `x` of the
h-adic normalized level-0 Jacobian remainder before subtracting `c*x^k`;
this is the pre-saturation object compared to the target monomial.  Every
stratum reached the required `k`.

| row | stratum | unk | eq | deg_x J | 32003 | 32009 | 32027 | Q | verdict |
|---|---:|---:|---:|---:|---|---|---|---|---|
| `(33,22;30;8;k=1)` | `3` | 28 | 62 | 4 | SATURATED-EMPTY | SATURATED-EMPTY | SATURATED-EMPTY | SATURATED-EMPTY | `SATURATED-EMPTY` |
| `(33,22;30;8;k=1)` | `2+1` | 29 | 62 | 4 | SATURATED-EMPTY | SATURATED-EMPTY | SATURATED-EMPTY | SATURATED-EMPTY | `SATURATED-EMPTY` |
| `(45,30;42;11;k=1)` | `4` | 44 | 100 | 5 | SATURATED-EMPTY | SATURATED-EMPTY | SATURATED-EMPTY | SATURATED-EMPTY | `SATURATED-EMPTY` |
| `(45,30;42;11;k=1)` | `3+1` | 45 | 100 | 5 | SATURATED-EMPTY | SATURATED-EMPTY | SATURATED-EMPTY | SATURATED-EMPTY | `SATURATED-EMPTY` |
| `(45,30;42;11;k=1)` | `2+2` | 45 | 100 | 5 | SATURATED-EMPTY | SATURATED-EMPTY | SATURATED-EMPTY | SATURATED-EMPTY | `SATURATED-EMPTY` |
| `(21,14;18;5;k=1)` | `2` | 16 | 32 | 3 | SATURATED-EMPTY | SATURATED-EMPTY | SATURATED-EMPTY | SATURATED-EMPTY | `SATURATED-EMPTY` |
| `(21,14;18;5;k=1)` | `1+1` | 17 | 32 | 3 | SATURATED-EMPTY | SATURATED-EMPTY | SATURATED-EMPTY | SATURATED-EMPTY | `SATURATED-EMPTY` |
| `(15,10;11;2;k=2)` | `3` | 14 | 34 | 5 | SATURATED-EMPTY | SATURATED-EMPTY | SATURATED-EMPTY | SATURATED-EMPTY | `SATURATED-EMPTY` |
| `(15,10;11;2;k=2)` | `2+1` | 15 | 34 | 5 | SATURATED-EMPTY | SATURATED-EMPTY | SATURATED-EMPTY | SATURATED-EMPTY | `SATURATED-EMPTY` |
| `(15,10;11;2;k=2)` | `1+1+1` | 16 | 34 | 5 | SATURATED-EMPTY | SATURATED-EMPTY | SATURATED-EMPTY | TIMEOUT | `GAP` |

Timings:

| row | stratum | build s | 32003 s | 32009 s | 32027 s | Q s |
|---|---:|---:|---:|---:|---:|---:|
| `(33,22;30;8;k=1)` | `3` | 19.683 | 0.01 | 0.011 | 0.011 | 0.01 |
| `(33,22;30;8;k=1)` | `2+1` | 25.906 | 0.014 | 0.014 | 0.014 | 0.013 |
| `(45,30;42;11;k=1)` | `4` | 142.121 | 0.013 | 0.012 | 0.013 | 0.011 |
| `(45,30;42;11;k=1)` | `3+1` | 113.524 | 0.016 | 0.016 | 0.016 | 0.024 |
| `(45,30;42;11;k=1)` | `2+2` | 164.121 | 0.016 | 0.016 | 0.023 | 0.016 |
| `(21,14;18;5;k=1)` | `2` | 1.522 | 0.006 | 0.007 | 0.007 | 0.006 |
| `(21,14;18;5;k=1)` | `1+1` | 1.753 | 0.007 | 0.007 | 0.007 | 0.007 |
| `(15,10;11;2;k=2)` | `3` | 1.464 | 0.007 | 0.007 | 0.007 | 0.007 |
| `(15,10;11;2;k=2)` | `2+1` | 2.416 | 0.008 | 0.008 | 0.008 | 0.008 |
| `(15,10;11;2;k=2)` | `1+1+1` | 3.491 | 22.181 | 23.698 | 25.218 | 900.183 |

Typed gap records:

- `(15,10;11;2;k=2)` stratum `1+1+1`: `GAP`; Q verdict `TIMEOUT`; controls empty/nonempty `True/True`; Q elapsed `900.183` s.

The only non-confirmed stratum is the final restoration case
`(15,10;11;2;k=2)` with partition `[1,1,1]`: the three finite fields returned
`SATURATED-EMPTY`, but the exact `Q` full-system run timed out at the 900 s
bound.  By FALLACY-v2 this remains `GAP`, not a Q kill.  Auxiliary Q attempts for the final restoration stratum were not counted as
certificates: `legacy_le_34` returned `SURVIVES`, `first_24` timed out at
300 s, `eq2_14` returned `SURVIVES`, and an exploratory full-system `slimgb`
run was stopped without a `MAIN_DONE` result.  These are negative/blocked
checks only.

## Row verdicts

| row | strata | verdict |
|---|---|---|
| `(33,22;30;8;k=1)` | `3`, `2+1` | `CONFIRMED` |
| `(45,30;42;11;k=1)` | `4`, `3+1`, `2+2` | `CONFIRMED` |
| `(21,14;18;5;k=1)` | `2`, `1+1` | `CONFIRMED` |
| `(15,10;11;2;k=2)` | `3`, `2+1`, `1+1+1` | `GAP` |

Typed verdicts: `CONFIRMED` means every listed partition stratum returned
`SATURATED-EMPTY` over all three primes and over `Q`, with the normalized
Jacobian-degree gate reaching the row's `k`.  `REFUTED` would require a surviving
stratum and a representative direct Jacobian check; none occurred.  `GAP`
means timeout, failed control, or failed degree gate.  Here it occurs only for
the exact `Q` run of `(15,10;11;2;k=2)` partition `[1,1,1]`.

Answer to the restoration question: `(21,14;18;5;k=1)` persists completely.
For `(15,10;11;2;k=2)`, `[3]` and `[2,1]` persist, while `[1,1,1]` remains a
Q gap in this bounded rerun despite three modular empty certificates.

## FALLACY-v2 check

`sat()` wrapping: every Singular script declares its ring and saturates by
`T*(c*Omega)-1`; controls `<c*Omega,T*(c*Omega)-1>` and
`<c*Omega-1,T*(c*Omega)-1>` passed for every run.

Raw remainder degree: the driver computes the h-adic normalized level-0
Jacobian remainder degree before saturation and records it in each JSON result
and Singular script header.  The full expanded raw Jacobian was not used as a
promotion shortcut.

Variable/ring map: the emitted rings use the parameter variables plus
Rabinowitsch variable `T`; chart variables are `x,y` in the generator with `x`
the monomial-Jacobian variable in `J=c*x^k`.  Prime marks are labels only.

No exit-price assertion is made here, so no `charge_basis` line is applicable.

<!-- BODY-END -->
