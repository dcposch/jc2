# Certificate slice A: `(99,66)`, `delta=2`, stage-4 unit `6264`

## Result and scope

The charged terminal normal form is reproduced exactly:

```text
stage4_J_d159_k35  -->  6264.
```

Backward tracing from the terminal, before the cumulative joint substitutions,
has three distinct sizes which must not be conflated:

| object | incidence | outer | pole | Jacobian | localization | total |
|---|---:|---:|---:|---:|---:|---:|
| reduced scalar line `6264/6264` | 0 | 0 | 0 | 1 | 0 | 1 |
| recursive DAG in the fixed-face, `B1`-support quotient | 0 | 0 | 4 | 3 | 0 | **7** |
| full syntactic provenance DAG, lifting every touched `D2/D1` zero fact | 1 | 98 | 4 | 3 | 0 | **106** |
| nonzero rows after exact certificate-coefficient pruning | 1 | 0 | 4 | 3 | 0 | **8** |

The 106-node result is the requested full transitive closure: its 98 outer
nodes are exactly 90 strict-below `B1`-`D2` coordinate rows plus the eight
at-level `B1`-`D1` scalar rows.  The outer rows occur in the substitution DAG,
but their coefficients cancel in the final raw polynomial identity.  The
incidence row does not cancel.  Thus the quotient certificate has seven rows,
whereas the certificate before fixing the face has eight.

The eight-row raw certificate is inclusion-minimal on its displayed support.
This is a fixed-ledger support-minimality statement.  It is **OPEN** whether a
different choice among the other charged residuals/pivots yields a globally
smaller certificate; neither the charged ledger nor this bounded slice solves
that global sparse syzygy problem.

No `A2`, `A3`, or `B2` coefficient occurs.  No `T2`/`T3` bridge row occurs.
The deepest series band carried is local/`t` power 8; the deepest Jacobian
band used is `t` power 4.  No localization equation is used, and no multiplier
has `rho` in its denominator.  The identity therefore already holds over the
unlocalized rational polynomial ring in the declared chart coordinates.

Primary charged evidence: the ledger records 35 cumulative rational pivots
and 659 input labels (`inputs/stage4.json:48-53`) and its first residual is the
named constant `6264` (`inputs/stage4.json:265-272`).  The charged report makes
the same distinction between the scalar reduced residue and the triangularly
equivalent full system (`inputs/g9966-global-band-sol56-20260903.md:229-250`).

## Custody

The lane receipt was parsed mechanically.  An `awk` program joined its
`charged_input_<i>_sha256` and `charged_input_<i>_basename` fields into
`/tmp/delta2_manifest.sha256`; then `sha256sum -c` returned `OK` for all 16
charged inputs.  In particular, the script rereads the receipt rather than
embedding the stage-4 digest and asserts

```text
sha256(stage4.json) =
5e9dd9516335ef5afa0bd956d014cf8050601ea960e284b6e5b0a6effef51.
```

See `delta2_certificate.py:41-60,297-305`.  No ledger or charged input was
edited.  No running lane, including `minor-residue-formula-opus5`, was read.

## Declared ring and what is actually lifted

Work is over `QQ` in the declared common-chart coordinates

```text
Hc_*, K2c_*, B1c_*, u, rho, face,
```

with `face` standing for `K2[t^4 (w-1)^21]`.  The incidence equation is

```text
I_face := face + 8 = 0.
```

The value `-8` is the `k=1` member of
`(-1)^k binomial(8,k)` in the fixed equality family; the charged engine builds
that family at `band_engine.py:363-377`.  The script deliberately exposes this
one coefficient before constructing the rows and puts it back as a labelled
source equation (`delta2_certificate.py:91-129,307-312`).

The `K2c` coordinate map is not merely a name match: the charged artifact
declares `K2c_(r,q)` as the low-`q` coefficient after `D2`, the field `Q`, the
generator order, and unit `C3/C2` leaders (`inputs/stage4.json:11-20`).  It also
records 106 low-`q` outputs and the seven `h2`-`D1` pivots
(`inputs/stage4.json:778-816`).  However, it explicitly says that the full
inverse map to the original `C2/C3` coordinates was not serialized
(`inputs/stage4.json:15-18`; also
`inputs/g9966-global-band-sol56-20260903.md:88-96`).  Consequently:

```text
EXACT: certificate in the declared K2c/B1c/Hc chart, with every reached
       joint pivot and every reached B1 D2/D1 support fact lifted.

OPEN:  coefficient-by-coefficient expansion of this certificate all the way
       back to the original C2/C3 coordinates, because the required inverse
       ledger is absent.
```

This is the ledger-preservation limit; it is not filled by analogy.

## Reconstruction and tracing rule

The replay imports the static clean-room sparse-`Q` engine identified in the
sealed independent report (`inputs/g9966-independent-engine-opus5-20260903.md:
121-125`).  It reconstructs the delta-2 common-`h3` branch, builds `K2`, exposes
the face, reinstates the full `B1` support before `D2/D1`, and forms the four
needed `G` pole rows and the selected Jacobian rows
(`delta2_certificate.py:91-131`).  This is below the outer onset: the static
engine proof gives

```text
KF = K2^3,
KG = K2^2 + t K_B1 K2
```

through `t` power 21, because `A2,B2` begin at `r>=21` and `A3` at `r>=53`;
every present band is at power at most 8
(`inputs/g9966-independent-engine-opus5-20260903.md:150-156`).  Its normalized
Jacobian and degree/`t` conversion are stated at the same source,
lines 158-174, agreeing with the charged four-term formula
(`inputs/g9966-global-band-sol56-20260903.md:142-161`).

For a pivot equation `E=a*x+r` with rational `a!=0`, the tracer records
`x=-r/a`.  When reducing a later row `R`, it computes its exact substituted
image `R'` and the polynomial quotient `q=(R-R')/E`, checks

```text
R - R' - q E = 0,
```

and updates the source-row combination by `-q` times the complete certificate
for `E`.  This implements the same admissible affine `Q*` rule as the charged
engine (`inputs/band_engine.py:191-239`) while preserving coefficients; see
`delta2_certificate.py:144-207`.  The selected pivot labels, variables, and
coefficients are reread from the charged JSON and asserted exactly
(`delta2_certificate.py:210-218,352-364`).

## The quotient DAG

Write an edge `R -> P` when reducing raw row `R` directly substitutes the
pivot supplied by row `P`.  The exact seven-node transitive closure is:

| row | family | charged pivot `(variable, coefficient)` | direct parents in the seven-node closure |
|---|---|---|---|
| `stage1_G_local5_coord0` | pole | `(B1c_0_24, 8)` | none |
| `stage1_J_d162_k36` | Jacobian | `(B1c_0_25, -765)` | `stage1_G_local5_coord0` |
| `stage2_G_local6_coord0` | pole | `(B1c_1_23, -8)` | `stage1_G_local5_coord0` |
| `stage2_J_d161_k36` | Jacobian | `(B1c_1_24, 738)` | `stage2_G_local6_coord0` |
| `stage3_G_local7_coord0` | pole | `(B1c_2_22, 8)` | `stage1_G_local5_coord0`, `stage1_J_d162_k36`, `stage2_G_local6_coord0` |
| `stage4_G_local8_coord0` | pole | `(B1c_3_22, 8)` | `stage1_G_local5_coord0`, `stage1_J_d162_k36`, `stage2_G_local6_coord0`, `stage2_J_d161_k36`, `stage3_G_local7_coord0` |
| `stage4_J_d159_k35` | Jacobian terminal | not a pivot; normal form `6264` | `stage1_G_local5_coord0`, `stage1_J_d162_k36`, `stage2_G_local6_coord0`, `stage2_J_d161_k36`, `stage4_G_local8_coord0` |

Thus only six of the 28 prior candidate joint pivots are transitively reached.
In particular, none of the `k=37,...,43` rows, and no stage-3 Jacobian pivot,
survives recursive dependency pruning.  The program emits the edge dictionary
and asserts the seven-node closure at `delta2_certificate.py:388-428,507-525`.

The 28 candidates are still reconstructed and checked in ledger order.  This
is intentional: it starts at the raw terminal before cumulative substitutions,
so a prior B-level pivot cannot disappear merely because a cumulatively reduced
terminal expression was used as input.

## Lifting the order-support layer

The outer specifications declare `B1` degree 32 and boundary `W0=93`, with
`W=3r+4q` (`inputs/g9966-global-band-sol56-20260903.md:110-117`; frozen engine
`band_engine.py:392-418`).  Across the `B1` levels reached by powers 1 through
4, the raw core syntactically touches 126 coordinates:

```text
r=0: q=0..32  (33)
r=1: q=0..31  (32)
r=2: q=0..30  (31)
r=3: q=0..29  (30).
```

The strict-below `D2` facts among them are exactly

```text
r=0: q=0..23  (24)
r=1: q=0..22  (23)
r=2: q=0..21  (22)
r=3: q=0..20  (21),     total 90.
```

They are source rows `outer_B1_D2_zero_B1c_r_q := B1c_r_q`; the set is
extracted dynamically by `3r+4q<93` and asserted to have size 90
(`delta2_certificate.py:314-330`).

At level `W=93`, the eight positions are

```text
(3,21), (7,18), (11,15), (15,12),
(19,9), (23,6), (27,3), (31,0).
```

The charged artifact says the `B1` offset-zero block has eight positions and
eight raw rows and lists the same pivot variables
(`inputs/stage4.json:993-1017,1041-1048`).  The replay rebuilds the eight scalar
rows

```text
R_k = outer_B1_D1_s0_k{k}
    = sum_{(r,q): 3r+4q=93, q>=k} binomial(q,k) B1c_(r,q),
    k=0,...,7.
```

Only `B1c_3_21` from this boundary occurs syntactically in the core rows.  Its
fully original `D1`-row lift is checked standalone as

```text
B1c_3_21 =
    (374/19683) R_1
  - (20/729)    R_2
  + (166/6561)  R_3
  - (112/6561)  R_4
  + (55/6561)   R_5
  - (2/729)     R_6
  + (1/2187)    R_7.
```

The coefficient of `R_0` is zero.  The triangular elimination nevertheless
examines all eight rows, and all eight occur in the syntactic dependency
closure before coefficient cancellation.  Construction and exact assertion
are at `delta2_certificate.py:332-350,374-386`.

Adding the incidence face, these 90 `D2` rows, eight `D1` rows, 28 candidate
joint pivots, and the terminal gives a 128-row scheduled superset, with family
counts `(incidence,outer,pole,Jacobian,localization)=(1,98,4,25,0)`.  Recursive
dependency pruning gives the exact 106-node closure

```text
(1,98,4,3,0).
```

This is a closure count, not a rank or a claim that 106 nonzero multipliers
remain.

## Exact certificate

Let

```text
a  = K2c_5_21,   b0 = K2c_6_20, b1 = K2c_6_21,
c0 = K2c_7_19,   c1 = K2c_7_20, c2 = K2c_7_21,
h  = Hc_7_4.
```

In the fixed-face/support quotient, define

```text
C3 = a/512 - 9*rho*u/64,

C2 = a^2/4096 - 9*a*rho*u/256 - b0/512 + b1/512
     + 81*rho^2*u^2/64 - 81*rho^2/256
     - 21*u^3/128 - 3483*u/1856,

C1 = -45*h/512 + a^3/32768 - 27*a^2*rho*u/4096
     - a*b0/2048 + a*b1/2048
     + 243*a*rho^2*u^2/512 - 81*a*rho^2/1024
     - 21*a*u^3/512 - 3483*a*u/14848
     + 9*b0*rho*u/256 - 9*b1*rho*u/256
     + c0/512 - c1/512 + c2/512
     - 729*rho^3*u^3/64 + 729*rho^3*u/128
     + 189*rho*u^4/64 + 218151*rho*u^2/14848
     + 2848*rho/2465.
```

Then the replay checks the seven-row polynomial identity

```text
1 = (1/6264) stage4_J_d159_k35
  + C1          stage1_G_local5_coord0
  - (991*rho/177480) stage1_J_d162_k36
  + C2          stage2_G_local6_coord0
  + (u/174)     stage2_J_d161_k36
  + C3          stage3_G_local7_coord0
  + (1/64)      stage4_G_local8_coord0.
```

This is not the statement `1=(1/6264)*raw(stage4_J...)`: the script explicitly
asserts that scalar normalization of the raw terminal row is not 1
(`delta2_certificate.py:430-432`).  It is the back-substituted identity in the
declared quotient.

Before fixing the face, the same seven multipliers occur and there is one more
term

```text
             + C_face * (face+8),
```

where the exact polynomial `C_face` is computed by the row-operation tracer.
Equivalently and compactly,

```text
C_face = cancel((1 - sum(the seven displayed multiplier*raw-row terms))
                /(face+8)).
```

The division is checked to be exact in the polynomial ring; it is not a
localization.  `C_face` is large because it carries the 126 pre-support `B1`
coordinates.  The replay prints the complete, unabridged coefficient with
`--multipliers`, between `BEGIN_FULLY_LIFTED_MULTIPLIERS` markers.  The exact
identity assertion is `delta2_certificate.py:361-372`; printing is at lines
546-564.  After simplification, every `D2` and `D1` source-row multiplier is
zero, hence the raw eight-row family count `(1,0,4,3,0)`.

There is no `rho^-1`, `face^-1`, or Rabinowitsch row.  Rational constants such
as `1/6264` and `1/64` are the only unit normalizations.  This is stronger than
the localized statement in the charged branch ring.

## Minimality and controls

### Fixed-ledger inclusion-minimality

For the seven quotient rows, specialize legally to

```text
rho=1, u=1, face=-8, all other non-B1 parameters=0.
```

The resulting affine-linear system in the surviving `B1c` variables has
coefficient rank 6 and augmented rank 7, while every leave-one-row-out system
is consistent over `QQ`.  Thus all seven rows are needed within this support.
The script computes rather than assumes these ranks
(`delta2_certificate.py:253-294,464-470`).

For the eight-row raw certificate, removing any core row uses the corresponding
quotient leave-one-out common zero and `face=-8`, so the incidence row also
vanishes.  Removing the incidence row instead leaves the common zero

```text
rho=1; every other source-row symbol, including face and every B1c, is 0.
```

All seven raw pole/Jacobian rows are asserted to vanish there
(`delta2_certificate.py:471-484`).  Hence the eight-row support is
inclusion-minimal.  Again, global minimum cardinality across alternative
charged rows is **OPEN**.

### Perturbed-row negative control

The stage-4 pole row has value `face^2=64` at `face=-8` and all `B1c=0`.
The negative control replaces

```text
stage4_G_local8_coord0
    by stage4_G_local8_coord0 - face^2.
```

Keeping the frozen certificate multipliers changes its value from `1` to

```text
1 - face^2/64,
```

which is not 1.  At `face=-8` and every `B1c=0`, all perturbed source rows
vanish, giving a common zero and proving the perturbed ideal is proper.  This
is an ideal-level negative control, not merely a mismatch of one printed
number (`delta2_certificate.py:434-449`).

## Provenance verdict

- **Incidence (one retained row):** the fixed `K2` face `face+8`.  It is the
  sole affine source of the final constant.
- **Outer (98 closure nodes, zero retained multipliers):** precisely the 90
  strict-below `B1`-`D2` zeros and eight `W=93` `B1`-`D1` rows.  No live
  `A2/A3/B2` coefficient occurs.  The exact-onset proof is source-covered at
  `inputs/g9966-independent-engine-opus5-20260903.md:150-156`.
- **Pole (four retained rows):** the `G` local-power rows 5, 6, 7, 8.  The
  independent mechanism identifies exactly these nonzero delta-2 pole powers
  (`inputs/g9966-independent-engine-opus5-20260903.md:295-314`).
- **Jacobian (three retained rows):** stage-1 `J162,k36`, stage-2 `J161,k36`,
  and the stage-4 terminal `J159,k35`.  Stage 3's Jacobian pivot is not reached.
- **Localization (zero):** `rho!=0` is part of the branch declaration
  (`inputs/stage4.json:757-764`), but neither a denominator nor the wrapper
  row enters this certificate.
- **Bridge:** no `T2/T3` row or symbol is present.  This matches the sealed
  Card A discriminator (`inputs/ideation-20260904T0000Z-fable5.md:441-453`).

The stage specifications independently identify stage 4 as Jacobian `t` power
4 and pole local power 8 (`inputs/stage4.json:1345-1518`; frozen engine
`band_engine.py:666-682`).  These indices are reported separately.

## FALLACY-v2 audit

- **Flag/place/series:** the common chart flag, the declared delta-2 place,
  and the local cover series are not identified.  `D2` strict-below rows,
  `D1` at-level rows, pole-local power, and Jacobian `t` power remain separate.
- **Per-ray/exit-set charge:** no new exit-price assertion is made.  Therefore
  no `charge_basis=` line is emitted.
- **Carrier/attainment and floor/attainment:** this is an ideal certificate for
  a killed chart, not a `REPRESENTATIVE`, `FULL_ACTUAL_EXIT`, equality, or
  attainment claim.
- **Pole/interior:** the replay uses only the already charged delta-2 principal
  place and its labelled polynomiality rows; it does not extend them to an
  unverified vertex class.
- **`sat()` wrapping:** no saturation or localization is needed.  The positive
  raw identity and the perturbed-row proper-ideal control are both asserted in
  the declared polynomial ring.
- **Raw remainder degree:** the residue is normal-formed under exactly the
  charged rational pivots, zero leaders are handled, and the result is the
  nonzero rational constant 6264.  Every selected charged pivot coefficient
  is rechecked.
- **Variable/ring map:** field, generator role, and `K2c` definition are
  declared.  The absent original `C2/C3` inverse is recorded as `OPEN`, not
  silently reconstructed from matching names.
- **Prime label/derivative:** no prime notation is used; `_t` and `_w` have the
  explicitly defined derivative meanings in the engine Jacobian.
- **Merge-free/M-descent and target/arrival index:** no descent or exit claim is
  made.  Stage number, pole-local power, Jacobian `t` power, degree, and
  coefficient index are all kept distinct.

This follows the guardrail categories in `inputs/FALLACY-v2.md:5-30`.  The
overall independent report performs the same typed separation and says no exit
claim is made (`inputs/g9966-independent-engine-opus5-20260903.md:398-430`).

## Replay

```bash
timeout 1800 python3 box/obscore-20260903/delta2_certificate.py
timeout 1800 python3 box/obscore-20260903/delta2_certificate.py --multipliers
timeout 1800 python3 -m py_compile box/obscore-20260903/delta2_certificate.py
```

The normal run prints the terminal, all three count layers, the quotient DAG
edges, the D1 lift, exact-minimality ranks, and the negative-control witness.
The `--multipliers` run additionally prints every nonzero quotient and raw
source-row multiplier.  A successful run exits 0 only after all identities,
hashes, pivot coefficients, family exclusions, and controls have passed.

## Slice verdict

```text
CERTIFIED-SLICE[(99,66), delta=2]:
  terminal normal form = 6264;
  quotient DAG = 7 rows (pole 4, Jacobian 3);
  full support-provenance DAG = 106 rows
      (incidence 1, outer 98, pole 4, Jacobian 3, localization 0);
  inclusion-minimal raw certificate support = 8 rows
      (incidence 1, pole 4, Jacobian 3);
  deepest power = 8 (Jacobian t-power 4);
  A2/A3/B2 = none; T2/T3 bridge = none; localization = none;
  original-C2/C3 coefficient lift = OPEN (inverse ledger not serialized);
  alternative-ledger global sparsity minimum = OPEN.
```
