# Strata Gate: Symbolic Top-Face Replay and Prior-Slice Audit

Date: 2026-09-03  
Driver directory: `box/strata-gate-20260903/`  
Main driver: `box/strata-gate-20260903/strata_gate.py`  
Frozen input receipt: `xmodel/strata-gate-gpt55-20260903.run.v2`

## Verdict

**MEASURED.** The frozen input manifest was generated from the receipt's
`charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines with `awk`
and checked with `sha256sum -c`.  The first attempted manifest path was inside
the read-only frozen-input directory and failed before checking; the manifest
was regenerated at `/tmp/strata-gate-inputs.sha256`.  Result: **10/10 OK**.

**MEASURED.** Singular is
`Singular for x86_64-Linux version 4.3.2 (4330, 64 bit) Apr  1 2024 04:44:00`.

**VERDICT.** `(33,22;30;8;k=1)` under parent `(132,88)` is
**CONFIRMED** within the charged descended `(d',e')=(2,3)` A/B chart and the
source-safe Prop. 4.6 partition overcover.

**VERDICT.** `(45,30;42;11;k=1)` under parent `(180,120)` is
**CONFIRMED** within the same scope.

**VERDICT.** `(15,10;11;2;k=2)` with `u'=3` is **CONFIRMED** within the
symbolic top-face A/B chart.  The full `[1,1,1]` 42-equation basis timed out,
but an exact saturated subset of those full equations has basis `[1]`; since a
subset ideal is already empty after the same localization, the full stratum is
empty.

**VERDICT.** `(21,14;18;5;k=1)` with `u'=2` is **CONFIRMED** within the
symbolic top-face A/B chart.

**DERIVED.** These confirmations do not assert that every listed stratum is
attained by an actual Keller pair; they assert that every source-allowed
symbolic stratum in the stated chart is empty.

## Source And Cap Audit

**SOURCE-READ.** Page images were rendered from
`refs/moh1983_jram340_configurations_of_roots.pdf` into
`box/strata-gate-20260903/page-images/`.  Printed p.170 is
`moh_pp168_172-31.png`; printed p.171 is `moh_pp168_172-32.png`; printed p.207
is `moh_p207-68.png`; printed p.208 is `moh_p208-69.png`.

**SOURCE-READ.** The p.170 image of Prop. 4.6 states that, for `r>=2`, the
leading coefficients are powers of a common polynomial `p(pi)` of degree `nu`;
`T^psi_{r,sigma}(pi)=p(pi)^... q(pi)` with `q` of degree
`nu*(n-M_r)/d_r`; `q` has distinct roots; all roots of `p` are roots of `q`;
and `p` is not a power of `q`.

**DERIVED.** In the descended final two-point rows used here, the cap used by
the driver is

```text
number of distinct top-face factors = 1 + len(partition) <= n' - M2' .
```

**DERIVED.** The `1` is the selected factor normalized to `y=0`; the remaining
non-centre factors have multiplicities forming a partition of
`u'=K-V2'`, with one nonzero slope normalized to `1` and the others kept as
symbolic variables.

**MEASURED.** The allowed partition cover used in this gate is:

| row | `K` | `u'` | `n'-M2'` cap | allowed partitions |
|---|---:|---:|---:|---|
| `(33,22;30;8;k=1)` | 11 | 3 | 3 | `[3]`, `[2,1]` |
| `(45,30;42;11;k=1)` | 15 | 4 | 3 | `[4]`, `[3,1]`, `[2,2]` |
| `(15,10;11;2;k=2)` | 5 | 3 | 4 | `[3]`, `[2,1]`, `[1,1,1]` |
| `(21,14;18;5;k=1)` | 7 | 2 | 3 | `[2]`, `[1,1]` |

**MEASURED.** This matches the frozen charged `case_counts.json` for the two
replay rows and the new driver enumeration for the two prior-slice rows.

## Saturation Audit

**DERIVED.** For partition `[e1,...,el]`, the top face used is

```text
H = y^V (y-x)^e1 product_{i=2..l} (y-a_i*x)^e_i .
```

**DERIVED.** The non-degeneracy factor is

```text
Omega = product_{i=2..l} a_i(a_i-1)
        product_{2<=i<j<=l} (a_i-a_j).
```

**MEASURED.** Every generated and replayed saturated main ideal contains
`T*(c*Omega)-1`.  For one-part strata, `Omega=1` and the saturation factor is
`c`; for one free slope it is `c*a2*(a2-1)`; for two free slopes it is
`c*a2*a3*(a2-1)*(a3-1)*(a2-a3)`, expanded in the emitted Singular scripts.

**MEASURED.** The wrapper controls used in every completed Singular script are:
`<c*Omega, T*c*Omega-1>` reduces to `[1]`, and
`<c*Omega-1, T*c*Omega-1>` is nonunit.  The full `[1,1,1]` run for
`(15,10;11;2;k=2)` printed both control passes before its main-basis timeout;
the exact subset certificate also passed both controls.

**DERIVED.** The linear factors are monic in `y`, so there is no additional
top-face leading coefficient to invert after the normalization used here.  The
Jacobian scalar `c` is included in the same Rabinowitsch factor.

## Algebra Driver

**MEASURED.** `strata_gate.py` is an independent SymPy generator for these A/B
systems.  It derives `K=gcd(n',m')`, `d'=m'/K`, `e'=n'/K`, `u'=K-V2'`,
`delta2'=-(k+1)/(n'-M2'-1)`, and the charged closed form for `delta1'`; it
then builds the D1 lower monomial support for `h`.

**MEASURED.** The generator keeps the slope variables in the coefficient ring,
uses monic division in `y`, and forms the h-adic Jacobian remainders from

```text
J(a h^r, b h^s)
 = h^(r+s) J(a,b)
 + h^(r+s-1)(s b J(a,h) + r a J(h,b)).
```

**MEASURED.** For generated systems the direct numeric recomposition check
returned `true`: substituting a deterministic numeric parameter point into the
expanded `J(f,g)` equals the recomposed h-adic remainder sum.

**MEASURED.** The replay part executes the existing charged exact `Q` Singular
scripts under `box/topface-20260903/systems/` and records fresh gate results
under `box/strata-gate-20260903/results/`.

## A. Charged Replay Results

**MEASURED.** The exact `Q` replay of `(33,22;30;8;k=1)` is:

| partition | face | unknowns | equations | saturation | exact verdict |
|---|---|---:|---:|---|---|
| `[3]` | `y^8*(y-x)^3` | 28 | 62 | `c` | `SATURATED-EMPTY`, basis `1`, 0.011 s |
| `[2,1]` | `y^8*(y-x)^2*(y-a2*x)` | 29 | 62 | `c*a2*(a2-1)` | `SATURATED-EMPTY`, basis `1`, 0.013 s |

**MEASURED.** The exact `Q` replay of `(45,30;42;11;k=1)` is:

| partition | face | unknowns | equations | saturation | exact verdict |
|---|---|---:|---:|---|---|
| `[4]` | `y^11*(y-x)^4` | 44 | 100 | `c` | `SATURATED-EMPTY`, basis `1`, 0.012 s |
| `[3,1]` | `y^11*(y-x)^3*(y-a2*x)` | 45 | 100 | `c*a2*(a2-1)` | `SATURATED-EMPTY`, basis `1`, 0.024 s |
| `[2,2]` | `y^11*(y-x)^2*(y-a2*x)^2` | 45 | 100 | `c*a2*(a2-1)` | `SATURATED-EMPTY`, basis `1`, 0.025 s |

**MEASURED.** All five replayed exact scripts passed the empty and nonempty
Rabinowitsch wrapper controls.

**MEASURED.** The new independent generator rederived and reran one
symbolic-slope stratum from each replay row:

| row | partition | unknowns | equations | build | exact verdict | recomposition |
|---|---|---:|---:|---:|---|---|
| `(33,22;30;8;k=1)` | `[2,1]` | 29 | 62 | 32.998 s | `SATURATED-EMPTY`, basis `1`, 0.016 s | `true` |
| `(45,30;42;11;k=1)` | `[3,1]` | 45 | 100 | 208.834 s | `SATURATED-EMPTY`, basis `1`, 0.015 s | `true` |

**DERIVED.** Since the listed partitions are exactly the Prop. 4.6 cap cover
for the two replay rows, the two charged full-stratum kills are restored as
source-safe symbolic-slope kills in the stated chart.

## B. Prior-Slice Rows

**MEASURED.** For `(15,10;11;2;k=2)`, `K=5`, `u'=3`,
`d'=2`, `e'=3`, `delta2'=-1`, `delta1'=4/3`, and the Prop. 4.6 cap is
`n'-M2'=4`.

**MEASURED.** The full symbolic partition strata are:

| partition | face | unknowns | full equations | full-basis result | final stratum verdict |
|---|---|---:|---:|---|---|
| `[3]` | `y^2*(y-x)^3` | 16 | 42 | exact `[1]`, 0.011 s | `SATURATED-EMPTY` |
| `[2,1]` | `y^2*(y-x)^2*(y-a2*x)` | 17 | 42 | exact `[1]`, 0.016 s | `SATURATED-EMPTY` |
| `[1,1,1]` | `y^2*(y-x)*(y-a2*x)*(y-a3*x)` | 18 | 42 | exact full basis timed out at 900.213 s after controls passed | `SATURATED-EMPTY` by exact subset certificate |

**EXACT-CERTIFICATE.** For the `[1,1,1]` stratum, the certificate script
`box/strata-gate-20260903/systems/certificate_75_50_v2_part_1_1_1_Q.sing`
uses the same 18-variable ring and the same saturation by
`c*a2*a3*(a2-1)*(a3-1)*(a2-a3)`.  It keeps 17 of the 42 full equations, with
1-based indices
`[1,2,3,4,5,9,18,29,30,31,32,33,34,35,39,42,7]`, and returns exact
`SATURATED-EMPTY`, basis `1`, in 0.224 s.

**DERIVED.** Because those 17 equations are a subset of the full stratum ideal,
their saturated emptiness implies saturated emptiness of the full 42-equation
stratum.

**MEASURED.** A diagnostic modular run of the full `[1,1,1]` ideal over
`GF(32003)` also returned `[1]` in 53.686 s; this was not needed for the
characteristic-zero verdict.

**SOURCE-READ.** The p.207 image gives the transformed Appendix-II table:
the second row is `(21,14)` with bracketed alternative `M2=16 [18]`,
`V2=2 [5]`; the third row is `(15,10)` with `V2=3 [2]`.

**SOURCE-READ.** The p.208 image says that similar arguments apply to the
second case to show impossibility directly and to the third case to reduce the
number of coefficients to `22 [15 or 13]`.

**DERIVED.** Thus Moh's "second case" is the `(21,14)` table row, and Moh's
"third case" is the `(15,10)` table row.  Within the third case, the bracket
splits the `V2=3` and `V2=2` alternatives from p.207; for the audited
`V2=2` row, the A/B count is `11` lower `h` coefficients plus `4` beta
parameters, hence Moh's `15` before adding the Jacobian scalar `c`, and `16`
unknowns in the one-slope-normalized `[3]` stratum.

**MEASURED.** For `(21,14;18;5;k=1)`, `K=7`, `u'=2`,
`d'=2`, `e'=3`, `delta2'=-1`, `delta1'=1/3`, and the Prop. 4.6 cap is
`n'-M2'=3`.

**MEASURED.** The full symbolic partition strata are:

| partition | face | unknowns | equations | saturation | exact verdict |
|---|---|---:|---:|---|---|
| `[2]` | `y^5*(y-x)^2` | 16 | 32 | `c` | `SATURATED-EMPTY`, basis `1`, 0.009 s |
| `[1,1]` | `y^5*(y-x)*(y-a2*x)` | 17 | 32 | `c*a2*(a2-1)` | `SATURATED-EMPTY`, basis `1`, 0.016 s |

**DERIVED.** The earlier fixed face `y^5(y^2-x^2)` was an unlicensed numeric
slice of `[1,1]`; the new computation covers both `[2]` and symbolic `[1,1]`,
so the prior kill is restored in licensed form.

## C. Row Verdicts And Scope

**VERDICT.** `(33,22;30;8;k=1)` parent `(132,88)`: **CONFIRMED**.  Scope:
all symbolic partitions allowed by `1+len(partition)<=3` in the charged A/B
chart, saturated by `c*Omega`.

**VERDICT.** `(45,30;42;11;k=1)` parent `(180,120)`: **CONFIRMED**.  Scope:
all symbolic partitions allowed by `1+len(partition)<=3` in the charged A/B
chart, saturated by `c*Omega`.

**VERDICT.** `(15,10;11;2;k=2)` parent `(75,50) V2=2`: **CONFIRMED**.  Scope:
all symbolic partitions `[3]`, `[2,1]`, `[1,1,1]` allowed by
`1+len(partition)<=4`; the `[1,1,1]` verdict uses the exact subset certificate
above after the full basis timed out.

**VERDICT.** `(21,14;18;5;k=1)` parent `(84,56)`: **CONFIRMED**.  Scope:
both symbolic partitions `[2]` and `[1,1]` allowed by
`1+len(partition)<=3`.

**MEASURED.** No stratum survived.  Therefore no representative point was
printed and no direct representative `J` check was required.

## FALLACY-v2 Audit

**DERIVED.** No cv flag, physical place, and cover series are identified with
one another; the computation is explicitly scoped to descended A/B charts and
top-face partition strata.

**DERIVED.** A Prop. 4.6 cap is used only to enumerate allowed partitions; it
is not used as a kill and not used to infer attainment.

**MEASURED.** Saturation uses explicit Rabinowitsch wrappers in the declared
Singular rings, and positive/negative wrapper controls are recorded.

**MEASURED.** Remainders are normal forms after monic division in the declared
`y` variable; no vanished leader branch is hidden because the divisor `h` is
monic in `y`.

**DERIVED.** Prime marks are labels.  The variables in the generated systems
are the descended chart variables `(x,y)`; no name matching is used as a proof
of a map.

**DERIVED.** No new exit-price assertion is made, so no `charge_basis` line is
due.

<!-- BODY-END -->
