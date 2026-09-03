# Top-face licence from the inverse Proposition 6.3 minor-disc split

Date: 2026-09-03  
Scope: Moh pp. 196–199, 207, 210–211 and the nine requested two-point
`COUNTING-BOUND` rows. Prime marks below label descended data; they never mean
differentiation.

## Executive verdict

**SOURCE-READ.** Moh does **not** state a general inverse-Proposition-6.3
top-face theorem. Propositions 6.3/6.4 give polynomiality, transformed degrees,
a monomial Jacobian, and a radius lower bound; they do not give the descended
root partition or residues. The `2,2,6` sentence belongs to the particular
`(75,50) -> (15,10;11;3;k=2)` calculation.

**DERIVED.** Once the *actual boundary factor data* are supplied, the general
top face is

```text
H = y^V2' product_i (y-a_i*x)^e_i,       sum_i e_i = u'=d2'-V2',
f_top = H^d',                            g_top = H^e',
d'=m'/d2',                               e'=n'/d2'.
```

**DERIVED.** The cited skeleton/source fixes `u'` and bounds the factor count,
but does not determine `(e_i)` or distinct nonzero `(a_i)`. A numeric choice of
a remaining slope is a slice.

**MEASURED.** The source-safe Proposition-4.6 overcover has **30 parametric
partition strata** over the nine rows. A conditional generalisation of Moh's
special inverse-minor observation would reduce this to 21, but that reduction
is not source-licensed; maximum slope dimension is five.

**MEASURED.** Complete symbolic coverage makes `(33,22)` and `(45,30)`
`SATURATED-EMPTY` inside the charged A/B chart. For `(24,16)`, four strata are
empty, three timed out, and four were not run.

**DERIVED (verdict).** The automatic seven-row unlock is not source-licensed
and remains OPEN. The replacement is a finite *parametric* stratum calculation;
p. 210 does not license either requested `u'=2` row to use only
`y^V(y^2-x^2)`.

## 1. Provenance and typing

**MEASURED.** `awk` parsed the lane receipt's paired basename/hash fields into
the `sha256sum -c` manifest. All 11 frozen inputs returned `OK`; no digest was
retyped.

**MEASURED.** Printed page `N` is PDF page `N-139`; cited pages were checked in
page images and layout extraction.

**MEASURED.** Agent-authored lane writes are confined to this report and
`box/topface-20260903/`; the orchestrator also owns its lane log. No ledger,
`jc2-lean`, `ideation-*`, or named in-progress report was edited or read.

## 2. What the source actually says

### 2.1 Splitting data before descent

**SOURCE-READ (p. 164).** Distinct leading-coefficient roots give distinct
child subdiscs; factor multiplicity gives their root counts after the relevant
degree scaling.

**SOURCE-READ (Prop. 4.4, pp. 168–169).** Under its hypotheses the leading
coefficients are powers of one linear polynomial in `pi`; it gives no sibling
split or minor-radius statement.

**SOURCE-READ (Prop. 4.6, pp. 170–171).** For `r>=2`, the leading coefficients
are powers of a common degree-`nu` polynomial `p(pi)`. A square-free `q(pi)`
contains every `p`-root, `p` is not a power of `q`, and

```text
deg q = nu (n-M_r) / d_r.
```

**SOURCE-READ.** This bounds the number of distinct `p`-roots, not their multiplicities or
constants. The following remark covers the monomial-Jacobian form.

**SOURCE-READ (p. 173).** Here `deg q` counts child discs and their root counts
are unequal; the full `p` factorisation is not supplied.

**SOURCE-READ (Def. 5.1, p. 179).** The datum gives counts, inequalities, and
radii for each *chosen major disc*, not the complete sibling tree.

**SOURCE-READ (pp. 190–191).** Multiplicity `E>d_r/(n-M_r)` is major;
`1<=E<=d_r/(n-M_r)` is minor. Proposition 6.1 defines the minor radius from
actual root distances and proves only `delta*_{r-1}>=1`.

**SOURCE-READ (pp. 193–194).** Moh says Proposition 6.1 only estimates
`delta*`; the uncertainty is intrinsic, and changed constants/quasi-roots alter
leading coefficients. Thus `(M,V)` does not recover minor radii or residues.

**SOURCE-READ (p. 194).** In the original `M_s=n-2` case the highest form is

```text
[(y-a*x)^v_s (y-b*x)^u_s]^(n/d_s),       u_s=d_s-v_s, a!=b.
```

**SOURCE-READ.** This fixes the original split, not the split after focusing on
its minor branch.

### 2.2 Propositions 6.2–6.4

**SOURCE-READ (Lemma 6.2, pp. 196–197).** The inversion lemma says suitable
truncations in the old and new parameters determine one another and identifies
their Puiseux fields. It does not assert a factor partition.

**SOURCE-READ (Prop. 6.3, pp. 197–198).** Assuming `delta_s=-1` and
`delta*_{s-1}>=v_s/u_s`, Moh constructs a truncated `pi`-root and a parameter
`gamma`. The transformed expressions lie in `k[gamma,pi]`, are monic in `pi`,
and have `pi`-degrees

```text
u_s*n/d_s,  u_s*(-mu_1)/d_s, ..., u_s*(-mu_{s-1})/d_s.
```

**SOURCE-READ.** Their Jacobian is a nonzero scalar times `gamma^(v_s-u_s-1)`. The proposition
contains no statement fixing a descended leading factorisation, number of
minor children, exact minor radius, or residue constants.

**SOURCE-READ (Prop. 6.4, pp. 198–199).** When `u_s=1`, Moh proves
`delta*_{s-1}>=v_s/u_s=v_s`; hence Prop. 6.3 applies. This remains an
inequality, not an equality or a split theorem.

**SOURCE-READ (p. 209).** In the fourth Appendix-II case Moh explicitly treats
two possibilities according to the distribution of roots inside a minor disc.
That case is outside the first three `u_s=1` descents, so it evidences general
minor-disc variability, not this specific descended setting by itself.

### 2.3 The transformed table

**SOURCE-READ (p. 207).** The transformed columns and linked alternatives are:

| `n` | `m=-M1` | `M2` | `V2` | `delta2` | `delta1` | Jacobian |
|---:|---:|---:|---:|---:|---:|---|
| 16 | 12 | 13 | 3 | -1 | 1/4 | `X` |
| 21 | 14 | 16 `[18]` | 2 `[5]` | -1/2 `[-1]` | 7/6 `[1/3]` | `X` |
| 15 | 10 | 11 | 3 `[2]` | -1 | 1/2 `[4/3]` | `X^2` |

**SOURCE-READ.** Moh applies Props. 6.4/6.3 because `u_3=1` in the first three
cases. Bracketed entries are linked alternatives, not columns to mix.

## 3. The safe general rule—and where it stops

**DERIVED from Prop. 6.3 and the charged drop rule.** Put
`(n',m',k)=(n/d_s,m/d_s,V_s-2)`, divide retained `M` by `d_s`, drop any
`M'=n'-1` level, and carry its surviving `V` path to `(M2',V2')`. Section 5
checks all nine cases. Original `u_s=1` enables descent; it does not force a
later `e_i=1`.

**DERIVED.** For descended data `(n',m';M2',V2';k)`, put

```text
K=d2'=gcd(n',m'),  u'=K-V2',  d'=m'/K,  e'=n'/K.
```

**DERIVED.** At final level `r=2`, Def. 5.1 has `V3=d3`; hence the common
boundary polynomial `p` has degree `K`. The selected major factor accounts for
`V2'`, so all other `p`-factor multiplicities form a partition
`lambda=(e_1,...,e_l)` with `sum e_i=u'`.

**DERIVED.** Proposition 4.6 gives `deg q=n'-M2'` at this level. Therefore

```text
1+l <= n'-M2'.
```

**DERIVED.** The extra `1` is the selected `V2'` factor. Its condition that `p` not be a
power of `q` must also be retained; none of the 30 strata in section 5 violates
it.

**DERIVED, conditional on actual boundary data.** If the distinct noncentre
residue constants are `a_i`, then

```text
H_lambda(x,y) = y^V2' product_i (y-a_i*x)^e_i,
f_top = H_lambda^d',                 g_top = H_lambda^e'.
```

**DERIVED.** Thus the number of noncentre roots of `H` is exactly `u'` with multiplicity,
while the corresponding root packets contain `d'e_i` roots of `f` and
`e'e_i` roots of `g`. Distinct residue blocks have pairwise difference order
exactly the top radius `delta2'=-1`; roots in one repeated block agree through
that level, so their next internal radius is `>-1` and is not determined by
Def. 5.1 or Props. 4.4/4.6.

**DERIVED from pp. 190–191.** A noncentre block is minor exactly when
`e_i<=floor(K/(n'-M2'))`; a larger block is a major sibling. This classifies a
given partition but does not determine which partition occurs.

**DERIVED.** Changes preserving `J=c*x^k` normalize the major slope to zero and
one nonzero slope to one, but not the others. For `lambda=(e_1,...,e_l)` use

```text
H_V[e_1,...,e_l]
 = y^V (y-x)^e_1 product_(i=2..l) (y-a_i*x)^e_i,

Omega = product_(i>=2) a_i(a_i-1) product_(2<=i<j) (a_i-a_j) != 0.
```

**DERIVED.** There are `l-1` slope parameters. A numeric choice is a slice; the charts
saturate by `c*Omega`, not merely `c`.

**OPEN[INVERSE-MINOR].** Moh's one example says its inverse transformation
forces a minor disc. If this were proved generally, at least one part would
satisfy

```text
e_i <= floor(K/(n'-M2')).
```

**OPEN[INVERSE-MINOR].** That is an additional necessary condition, not a sourced theorem for all
descendants. It selects 21 of the 30 source-safe overcases; it is never used to
discard one of the other nine in this report.

## 4. Moh controls

### 4.1 Why `2,2,6` means `y^3(y^2-x^2)`

**SOURCE-READ (pp. 210–211).** Moh is considering the transform of degrees
`(75,50)` with descended data `(15,10;M2=11,V2=3)` and writes that the inverse
transformation supplies a minor disc. He concludes that the three children in
`D2` contain `2,2,6` roots of `f`; equation (5) then has

```text
h_top = y^3(y^2-x^2) = y^3(y-x)(y+x),    f=h^2+2 beta.
```

**DERIVED.** Here `K=5`, `deg q=15-11=4`, and the chosen major multiplicity is
3, leaving mass 2. A minor factor must have integer multiplicity
`E<=5/4`, hence `E=1`; the remaining unit is another simple factor. Since
`d'=10/5=2`, the `h` multiplicities `(3,1,1)` become `f`-root packet sizes
`(6,2,2)`. Moh lists them in the order `2,2,6`. Likewise `g_top=h_top^3`
has packets `(9,3,3)`.

**SOURCE-READ / DERIVED.** Moh obtains the packet counts before invoking
`delta1=1/2` for the lower forms of `h` and `beta`. The `+/-x` presentation is
part of this special normal form. The page does not license copying it to an
arbitrary `u'=2` row.

### 4.2 The single-root control and K=16, t=2

**SOURCE-READ (p. 208).** For `(16,12;13;3;k=1)`, Moh writes

```text
h = y^3(y-x) + lower terms.
```

**DERIVED.** `K=4` and `V2=3`, so `u'=1`: there is only one noncentre root
unit. Here `d'=3,e'=4`, hence the `f` packets are `(9,3)` and the `g` packets
are `(12,4)`.

**DERIVED.** The campaign-`K=16`, `t=2` source skeleton
`(112,80;M=[-80,100,110],V={V2=3,V3=3})` descends to
`(28,20;25;3;k=1)`. Its descended `d2'=gcd(28,20)=4` and `u'=1`, so its
unique normalized face is `y^3(y-x)`.

**MEASURED (frozen charged result).** That K=16 `t=2` chart has 27 unknowns
and 37 equations; it returned saturated `[1]` over the three charged primes and
over `Q` (exact time 32.440 s). This checks the one-root rule, not a general
multi-root split.

## 5. Nine-row face inventory and charged chart counts

### 5.1 Original data

**MEASURED.** Matching the target list against the frozen full skeleton census
gives the following. `M` includes `M1=-m`; the `drop1` row records the full
original `V` path. Matching all displayed `M,V_s,V2'` data makes each entry
unambiguous.

| source | original `M` | original `V` | `(d_s,V_s,u_s)` | descended row | `u'` |
|---|---|---|---|---|---:|
| (125,75) | `[-75,105,123]` | `{V2=2,V3=4}` | `(5,4,1)` | `(25,15;21;2;k=2)` | 3 |
| (132,88) | `[-88,120,130]` | `{V2=8,V3=3}` | `(4,3,1)` | `(33,22;30;8;k=1)` | 3 |
| (175,100) | `[-100,155,173]` | `{V2=2,V3=4}` | `(5,4,1)` | `(35,20;31;2;k=2)` | 3 |
| (180,120) | `[-120,168,176,178]` | `{V2=11,V3=9,V4=3}` | `(4,3,1)` | `(45,30;42;11;k=1)` | 4 |
| (192,128) | `[-128,136,190]` | `{V2=2,V3=7}` | `(8,7,1)` | `(24,16;17;2;k=5)` | 6 |
| (196,56) | `[-56,184,194]` | `{V2=4,V3=3}` | `(4,3,1)` | `(49,14;46;4;k=1)` | 3 |
| (200,120) | `[-120,188,198]` | `{V2=7,V3=3}` | `(4,3,1)` | `(50,30;47;7;k=1)` | 3 |
| (175,125) | `[-125,155,173]` | `{V2=3,V3=4}` | `(5,4,1)` | `(35,25;31;3;k=2)` | 2 |
| (180,144) | `[-144,150,178]` | `{V2=4,V3=5}` | `(6,5,1)` | `(30,24;25;4;k=3)` | 2 |

### 5.2 Explicit source-safe faces and counts

**MEASURED.** The frozen driver's no-`--run` mode counts; the wrapper adds
`--count`, preserves its support arithmetic, and rechecks all hashes. Counts
exclude Rabinowitsch `T`, as in the charged batch.

**DERIVED.** The following faces are explicit via the definition of `H_V[...]`
in section 3; every `a_i` shown there remains symbolic and is included in
`Omega`. The Proposition-4.6 cap has already removed partitions with too many
distinct roots. A star marks the 21 cases also surviving the *conditional*
inverse-minor inequality; stars do not confer a source licence.

| descended row | explicit face families `H_V[partition] -> unknowns` | charged D1-only |
|---|---|---:|
| `(25,15;21;2;k=2)` | `H_2[3] ->145`; `H_2[2,1] ->146*`; `H_2[1,1,1] ->147*` | 148 |
| `(33,22;30;8;k=1)` | `H_8[3] ->28*`; `H_8[2,1] ->29*` | 31 |
| `(35,20;31;2;k=2)` | `H_2[3] ->204`; `H_2[2,1] ->205*`; `H_2[1,1,1] ->206*` | 207 |
| `(45,30;42;11;k=1)` | `H_11[4] ->44*`; `H_11[3,1] ->45*`; `H_11[2,2] ->45*` | 48 |
| `(24,16;17;2;k=5)` | `H_2[6] ->35`; `H_2[5,1] ->36*`; `H_2[4,2] ->36`; `H_2[4,1,1] ->37*`; `H_2[3,3] ->36`; `H_2[3,2,1] ->37*`; `H_2[3,1,1,1] ->38*`; `H_2[2,2,2] ->37`; `H_2[2,2,1,1] ->38*`; `H_2[2,1,1,1,1] ->39*`; `H_2[1,1,1,1,1,1] ->40*` | 41 |
| `(49,14;46;4;k=1)` | `H_4[3] ->194`; `H_4[2,1] ->195*` | 197 |
| `(50,30;47;7;k=1)` | `H_7[3] ->227*`; `H_7[2,1] ->228*` | 230 |
| `(35,25;31;3;k=2)` | `H_3[2] ->149`; `H_3[1,1] ->150*` | 151 |
| `(30,24;25;4;k=3)` | `H_4[2] ->143`; `H_4[1,1] ->144*` | 145 |

**MEASURED.** `case_counts.json` also emits every factored and fully expanded
polynomial, including its symbolic slopes and exact noncollision factor.

**MEASURED.** Per-row source-safe case counts are
`3,2,3,3,11,2,2,2,2`, totalling 30 in the table order. Conditional counts are
`2,2,2,3,7,1,2,1,1`, totalling 21. The 30 strata contain 37 slope-parameter
occurrences in total; per-row maximum dimensions are `2,1,2,1,5,1,1,1,1`.

**DERIVED.** In particular, the two `u'=2` rows require both
`H_V[2]=y^V(y-x)^2` and
`H_V[1,1]=y^V(y-x)(y-a*x)`. Replacing the latter by `a=-1`, and omitting the
former, is not justified by Moh's `(15,10)` calculation.

## 6. Computations

### 6.1 Ring and controls

**MEASURED.** Executable cases use the charged `(d',e')=(2,3)` A/B system,
monic division in `y`, and `J(f,g)=c*x^k`. Rings are `dp` polynomial rings over
`GF(p)` or `Q` in the `h` coefficients, slopes, four beta parameters, `c,T`.

**MEASURED.** Each main ideal contains

```text
T*(c*Omega)-1.
```

**MEASURED.** In the same ring, `<c*Omega,T*c*Omega-1>` reduces to `[1]`, while
`<c*Omega-1,T*c*Omega-1>` does not. Both controls passed on every completed
run; timed controls are unrecorded below. Monic division has no variable leader.

### 6.2 `(33,22;30;8;k=1)`

**MEASURED.** These are all source-safe partitions because `deg q=3` permits
at most two noncentre factors.

| partition / face | unk | eq | build | modular | exact `Q` |
|---|---:|---:|---:|---|---|
| `[3]`: `y^8(y-x)^3` | 28 | 62 | 9.433 s | three `[1]`, 0.007 s each | `[1]`, 0.007 s |
| `[2,1]`: `y^8(y-x)^2(y-a2*x)` | 29 | 62 | 13.190 s | three `[1]`, 0.009 s each | `[1]`, 0.009 s |

**MEASURED verdict.** Both exact bases have size one and both controls pass.
The union of these two parametric strata covers every partition allowed by the
source constraints, so the top-face gap for this row is closed. Within the
charged A/B chart, the `(132,88)` source row is **SATURATED-EMPTY**, not
`COUNTING-BOUND`.

### 6.3 `(24,16;17;2;k=5)`

**MEASURED.** Every system has 162 equations. Four strata completed over all
three primes and `Q`; every basis was `[1]` and both controls passed:

| partition | unk | build | modular times (s) | `Q` (s) |
|---|---:|---:|---|---:|
| `[6]` | 35 | 55.947 s | 0.016, 0.016, 0.016 | 0.016 |
| `[5,1]` | 36 | 96.539 s | 0.168, 0.165, 0.164 | 0.167 |
| `[4,2]` | 36 | 154.097 s | 0.171, 0.171, 0.169 | 0.180 |
| `[3,3]` | 36 | 126.905 s | 2.539, 2.545, 2.537 | 2.776 |

**MEASURED.** The first prime (`32003`) timed out after 600 s for `[4,1,1]`,
`[3,2,1]`, and `[2,2,1,1]`, with respectively 37, 37, and 38 unknowns.
Their symbolic builds were approximately 224, 247, and 547 s, inferred from
process ages because the pre-fix runners then failed to serialize byte-valued
timeout output. Thus their control output was not preserved and is not claimed.
The current driver decodes that output before serialization.

**MEASURED.** Following the bounded-stop rule, `[3,1,1,1]`, `[2,2,2]`,
`[2,1,1,1,1]`, and `[1,1,1,1,1,1]` were not launched. Consequently this row
remains `COUNTING-BOUND`. The durable post-run record distinguishes measured
results, inferred build times, and unrecorded controls in
`box/topface-20260903/timeout_observations.json`.

### 6.4 `(45,30;42;11;k=1)`

**MEASURED.** Each system has 100 equations. All three source-safe strata gave
basis `[1]` over every charged field, with both controls passing:

| partition | unk | build | modular times (s) | `Q` (s) |
|---|---:|---:|---|---:|
| `[4]` | 44 | 85.677 s | 0.008, 0.008, 0.008 | 0.008 |
| `[3,1]` | 45 | 100.193 s | 0.015, 0.018, 0.016 | 0.015 |
| `[2,2]` | 45 | 110.275 s | 0.016, 0.016, 0.016 | 0.016 |

**MEASURED verdict.** Their union covers the source-safe partition overcover,
so the `(180,120)` source row is **SATURATED-EMPTY** inside the charged A/B
chart.

## 7. Verdicts, bounded quantities, and cheapest tests

| typed item | verdict | bounded quantity | cheapest sound test |
|---|---|---|---|
| `OPEN[INVERSE-MINOR]` | No general p.210 inverse-minor theorem was found in Props. 6.1–6.4. | 9 strata separate the 30-case source overcover from the 21-case conditional refinement. | Derive the descended boundary `p,q` factor created by inverse Prop. 6.3; Singular cannot prove this geometric premise. |
| `OPEN[TOP-RESIDUES]` | The skeleton omits the nonzero residues/cross-ratios and inner minor radii. | At most 5 slope parameters in one stratum; 37 parameter occurrences across all 30 strata. | Keep symbolic slopes and saturate `Omega`; do not test a numeric roots-of-unity face. |
| `OPEN[PARTITION-CHART]` | Unfinished strata remain open; an empty stratum never kills the others. | `(24,16)`: 4 empty, 3 timed out, 4 unrun; two other rows are fully empty. | Preprocess the 37-unknown `[4,1,1]` timeout; untouched generic rows begin at 143. |
| `OPEN[PRIOR-SLICE]` | Frozen prior reports conflict: the later `appii-uniform` confines p.210 to its one row, while the compiler/batch copied fixed faces elsewhere. | 2 prior promoted fixed-top rows need audit: `(15,10;11;V2=2,u'=3)` and `(21,14;18;V2=5,u'=2)`. | Rerun their complete symbolic partition strata or find a source normal-form theorem. |

**DERIVED (verdict).** The bounded output is the 30-stratum
inventory, exact counts, the completed source-safe computations in section 6,
and four typed OPENs above. No claim is made that every combinatorial stratum is
attained by an actual Keller pair.

## 8. FALLACY-v2 audit

**DERIVED.** Major radii, a minor branch, and descended factors remain distinct;
the partition floor is not attainment, and unknown minor radii are not replaced
by Def. 5.1 radii.

**MEASURED.** Saturation declares ring, field, order, component and controls.
Remainders are monic normal forms with no vanished leader; the map is
`(x,y)=(gamma,pi)`, and prime marks are labels.

**DERIVED.** A numeric free-slope face is a slice, so only all-strata emptiness
is promoted. No new exit-price claim is made, so no basis declaration is due.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19373`.
- Body SHA-256:
  `cb0464deb9e9088f811a4082efed9b05f0a4364cdcb2409f5d8d90755af79091`.
- Frozen basis: `555bbfc7852f5df3eb8b8924f55fae3ebc00e5a9`.
