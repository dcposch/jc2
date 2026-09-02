# Keller cluster census: integer enumerator and desk result

**Date:** 2026-09-02  
**Deliverable:** `KELLER-CLUSTER-CENSUS`  
**Typing:** `artifact=NUMERICAL_PROFILE`, `attainment=NECESSARY`

## 1. Result

The requested fail-closed enumerator is
`box/keller_cluster_census.py`.  It is standard-library-only and all
mathematical decisions are integral.  Tests replay the 41 frozen clusters,
both `N=1` controls, and NEG-GEN; commands are `plan`, `census`, `validate`,
and fail-closed `merge`.

The mandated desk census was run with the charged strict window

```text
2 <= N <= 4,  2 <= D <= 40,  2a > N,  a <= N-2,  f-cap=unbounded.
```

It is complete and has **zero parameter rows and zero admissible clusters**.
For each of `N=2,3,4`, the summary value is `NONE_IN_SCANNED_RANGE` in the
declared box `[2,40]`.  This is a vacuous profile-gate result: at `N=2,3,4` there is no
integer satisfying `N/2<a<=N-2`.  It is not evidence that NOETHER-K by itself
excludes a nonempty low-degree profile window.

As a nonvacuous regression beyond the requested desk range, an uncapped exact
run through `N=5,D<=10` found the first strict-window numerical solution at
`D=10`:

```text
(D,n,S,kappa,T,W,a) = (10,5,1,2,3,2,3)
multiplicities       = (5,5,5,4,1,1,1,1)
proximity centers    = ((L),(0),(L),(2),(2,3),(3,4),(3,5),(6))
```

The derived sheets are `(m,k)=(1,1),(4,1)`; the unique dicritical has
`(s,mu,n,c)=(1,2,5,5)` and its unique positive-`m` neighbour has `m=5`.
This is globally nef by the certificate in Section 4 and satisfies every
enumerated numerical equation.  It is nevertheless **not a map**; moreover
`D=10<101`, so Moh's floor excludes it from being an actual noninvertible
Keller map.

## 2. Frozen inputs and scope

The four required SHA-256 checks were performed before either output file was
created.  All matched:

| Frozen input | Verified SHA-256 |
|---|---|
| `n-vs-mapdeg-opus5-20260902.md` | `ca9157617ecfd05fc21bffa6814aea830d1826c75b2ff7965c0128919f8da64a` |
| `n-vs-mapdeg-review-gpt55-20260902.md` | `05d59097a3712d855ffd050aa8dc585af1860b606f53675340d0e334ea05c10b` |
| `integration12-coordinator-fable51-20260902.md` | `ac0f48adf730dfb2d67b224cadb978fd1afc77bd71a2250127dee3ef3f60a644` |
| `deg-af-vs-n-opus5-20260902.md` | `d7cff053a856a61cc2401585737fc47c093eb6edb0562b1c3f4b82420deeb853` |

No canonical ledger was edited, and `jc2-lean` was not inspected.  The saved
drivers in `box/nvm-drivers-20260902/` were used only as the frozen control
corpus.

The promoted H2/Keller input is, with the fixed-sheet count written `a` and
base multiplicities always written `a_i`, as follows:

```text
W = N-a = sum_l s_l mu_l,       S = sum_l s_l,
mu_l >= 2,                      2S <= W,
D = S n + kappa + T,            1 <= kappa <= N,
sum_i a_i = 3D-2N-kappa+n(W-S),
sum_i a_i^2 = D^2-N,
n >= ceil((N-1)/(W-S))+1.
```

These are the promoted DEG-SPLIT and NOETHER-K equations
(`n-vs-mapdeg-opus5-20260902.md:305-376`) and MERIDIAN-FLOOR+
(`n-vs-mapdeg-opus5-20260902.md:483-522`).  The program never substitutes a
bound for a floor.  `kappa>=1` and `T>=0` make SHARP-CHAU `D>=Sn+1` automatic.
Moh `D>=101` is emitted only as an actual-map compatibility tag; it is not used
to erase numerical rows below 101 (`integration12-coordinator-fable51-20260902.md:70-79`).

The default defect cap is explicitly `unbounded`.  At fixed `(N,D)` the search
is still finite because DEG-SPLIT gives `n<=floor((D-kappa)/S)`.  If the user
declares `--f-cap f`, the requested coarse endpoint

```text
n <= floor((3N+f)/(W-S))
```

is intersected with the DEG-SPLIT endpoint.  The code never silently installs
`f=0`; that would assume OPEN[ANTICANON-DEFECT].

The current charge uses strict `a>N/2`.  The frozen ceiling driver instead used
the inclusive `ceil(N/2)<=a` window.  Both are available, but cannot be
confused:

```text
--window strict             # default; current charge
--window legacy-inclusive   # old ceiling-lane replay only
--window all-h2             # declared other H2 window
--window explicit --a-values 0,2,...
```

For a genuinely reducible/non-common-degree profile, `Sn` and `n(W-S)` are not
valid.  The option `--explicit-component-profiles FILE` therefore requires
each dicritical's `s`, `mu`, and component degree `n_c`, plus `N,D,a,kappa` and
an explicit `dicritical_neighbour=true`; every `n_c` must be at least 2, as
required by the promoted dicritical typing.  It uses

```text
Lambda = sum_l s_l n_c(l),
T = D-kappa-Lambda,
sum_i a_i = 3D-2N-kappa + sum_l (mu_l-1)s_l n_c(l).
```

MERIDIAN-FLOOR+ is not applied in that mode.  This exposes the missing data and
does not guess a common `n` or a component assignment.  The validated semantic
corpus (not its whitespace, JSONL order, or raw bytes) receives a canonical
SHA-256 identity.  That global identity is carried even by cells containing no
matching explicit profile.

## 3. Exact finite generator

For one scalar profile, put

```text
A = 3D-2N-kappa+n(W-S),   B = D^2-N,   T = D-Sn-kappa.
```

The generator starts with the boundary component `L` carrying `m_L=c_L=D`.
It adds one base point at a time at exactly one of the legal SNC centers:

1. a free point on `L` or an existing exceptional component; or
2. a satellite at a current dual-tree edge, which subdivides that edge.

For a new point of multiplicity `q` through components `P`, it performs the
integer updates

```text
m_new = sum_{C in P} m_C - q,
c_new = q,                    c_C <- c_C-q for C in P.
```

Negative `m` or `c` is rejected immediately.  The search consumes the exact
remaining free sum `A-T`, satellite sum `T`, and square sum `B`.  It uses parity
`q^2=q mod 2` and exact maximum-square bounds to prune impossible integer
partitions.  Multiplicities are generated in nonincreasing order.  This loses
nothing: every proximate child has multiplicity at most each parent by the
proximity inequality, hence every valid Enriques diagram has a nonincreasing
topological order; independent centers commute.

Chronological relabelings are not counted as new forest shapes.  Partial
states are deduplicated only after an exact colored directed-graph
isomorphism check preserving `L`, multiplicities, `m`, `c`, proximity arcs,
and the current dual tree.  A hash is never used as an isomorphism proof.

The cell field `count` counts profile–cluster matches, since distinct declared
ramification profiles can share one forest.  `unique_cluster_count` separately
counts forest/proximity shapes, so input duplication cannot masquerade as a
new cluster; duplicate explicit profile rows are rejected.

At a terminal state the validator recomputes, rather than accepts as input:

```text
Z^2 = D^2-sum a_i^2,
N   = sum_{m_C>0,c_C>0} m_C c_C,
kappa = sum_{m_C>0,c_C>0} c_C,
T = sum_{satellite i} a_i,
D = kappa + sum_{m_C=0,c_C>0} c_C + T.
```

It classifies `m>0,c>0` vertices as the `L_infty` sheets, `m=0,c>0` vertices
as dicriticals, and `c=0` vertices as contracted.  It matches the whole
dicritical degree multiset to `{s_l n}` (or `{s_l n_c(l)}`), then enforces the
promoted DICRITICAL-NEIGHBOUR statement: each dicritical has exactly one final
neighbour with positive `m`, and that `m` equals its degree
(`n-vs-mapdeg-opus5-20260902.md:287-303`).  Equal-degree dicriticals with
different `mu` values are reported as an unpinned multiset; the program never
invents a `mu`-to-vertex attachment.

No user point cap is needed for mathematical finiteness: `r<=A` because every
`a_i>=1`.  `--max-points`, `--max-states`, and `--deadline-seconds` are only
resource controls.  The per-cell deadline begins after scalar-profile
generation; the box job's outer wall timer covers both phases.  If any control
cuts a forest search, output is

```text
complete=false, count=null, observed_lower_bound=<found so far>.
```

`--allow-any-N` permits individually selected values outside `2..8`.  Before
materializing a CLI range or generated fixed-sheet window, the implementation
caps either selected axis/window at 1,000,000 values and the Cartesian product
at 2,000,000 cells; these are declared allocation guards, not mathematical
bounds on `N` or `D`.  A larger `N` remains selectable with an explicit `a`.

The merger also treats a missing, malformed, mistyped, or incomplete cell as
incomplete.  A shard must contain exactly one compact cell record and one local
summary, with matching engine revision, window, cap, mode, exact field types,
profile-corpus identity, and count invariants.  Each serialized solution is
replayed through the cluster validator and matched against the exact expected
profile set; exact forest isomorphism is rerun so a chronological relabeling
cannot inflate either count.  Explicit-mode merge therefore requires the
original semantic profile corpus, not a hand-entered digest.  It reports a
smallest `D` only inside the serialized scanned domain and only after every
smaller scanned cell has completed empty.  Existing output paths are refused
unless the caller explicitly supplies `--overwrite`.

## 4. Nef certificate and output type

The exact forest recurrences express the class as an actual boundary divisor

```text
Z = sum_C m_C C,   m_C >= 0,   Z.C = c_C >= 0.
```

This certifies global nefness, not merely boundary-nefness.  If an irreducible
curve is a boundary component, its intersection is the checked `c_C`.  If it
is not a boundary component, its intersection with every distinct irreducible
boundary curve is nonnegative, so its intersection with the effective sum
above is nonnegative.  This is stronger than a bare lattice vector, but it
still supplies no linear system, no morphism `Phi`, no polynomial pair, and no
Jacobian witness.

Every cell, solution, and summary therefore keeps the orthogonal fields

```text
artifact   = NUMERICAL_PROFILE
attainment = NECESSARY
```

and says explicitly: **a numerical cluster is not a map**.

## 5. Mandatory controls

`python3 box/keller_cluster_census.py self-test` returned `ok=true` with:

| Control | Exact result |
|---|---:|
| frozen resolved maps passing general polar ledger | 41/41 |
| same maps passing promoted dicritical-neighbour check | 41/41 |
| distinct numerical clusters among those maps | 34 |
| old inclusive noninvertible profile completions | 0/41 |
| actual Keller triangular automorphisms passing `N=1` Noether | 6/6 |
| NEG-GEN rows with residual exactly `N-1` | 35/35 |

The same self-test includes the positive end-to-end `N=5,D=10` census, an
explicit-component-degree match, a resource-cap/incomplete check, and positive
and poisoned merge-contract checks.  It also checks semantic-corpus hash order
independence and rejection of an `--a-values` argument outside its explicit
window; the poisoned shards include a resource-cut erasure and an isomorphic
chronological duplicate.

The 41-map result is mode-specific.  The saved engine accepted all 41 for I1,
I2, `Z^2`, `m,c>=0`, proximity and DEG-SPLIT.  It did not call all 41 Keller
maps.  Six triangular automorphisms separately satisfy `sum a_i=3D-3` and
`sum a_i^2=D^2-1`; the old noninvertible completion loop returns no completion
for any of the 41.

The standard quadratic Cremona cluster `(D;a_i)=(2;1,1,1)` also passes a
separate generic-plane homaloidal control.  It is intentionally not forced
into the infinity-boundary model: three noncollinear proper points are not
three roots on one `L_infty`.  The elementary maps `(x,y+x^k)` are checked in
the boundary mode and reproduce `kappa=1`, `T=k-1`, and both Noether equations.

For each saved NEG-GEN row `(x,x^c y^N)`, `2<=N<=8`, `1<=c<=5`, declare its
general-dominant data `n=1`, `W=N`, `S=Lambda`.  The exact resolved metrics give

```text
sum a_i - [3D-2N-kappa+n(W-S)] = N-1 > 0.
```

Thus Keller form rejects all 35.  General form accepts only after the affine
ramification term `rho_aff=N-1` is explicitly added.  The concrete charged
fixture `(x,x^3y^2)` has residual `1`, agreeing with the frozen review.  The
enumerator does not identify this residual with `deg Jac`; that identification
was not promoted.

Malformed parent order, duplicate parents, nonadjacent satellite parents,
nonpositive multiplicities, negative `m/c`, wrong `N`, unknown types, and
out-of-range `kappa` all fail closed.  The controls also pass under
`python3 -O`, so they do not depend on assertions.

## 6. Desk census receipt

Command:

```text
python3 box/keller_cluster_census.py census \
  --n-min 2 --n-max 4 --d-min 2 --d-max 40 \
  --window strict --f-cap unbounded \
  --max-states 2000000 --deadline-seconds 840 \
  --output /tmp/keller-desk-py312.Gg9WLH/keller-cluster-desk-N2-4-D40.jsonl
```

Receipt:

| N | D cells | scalar profiles | expanded forest states | clusters | smallest D in `[2,40]` |
|---:|---:|---:|---:|---:|---|
| 2 | 39 | 0 | 0 | 0 | none |
| 3 | 39 | 0 | 0 | 0 | none |
| 4 | 39 | 0 | 0 | 0 | none |

All 117 cell rows have `complete=true`; the JSONL has 118 records including
its summary, 84,259 bytes, and SHA-256
`af63f41a3ee43359574e2b5eae3186ce87cd8a3628d37ed2673e573fe86b617d`.
Under Python 3.12, wall time was 0.07 seconds and maximum resident set size was
28,016,640 bytes; the small cost reflects the empty strict profile window.

## 7. Box01 plan (64 vCPU, Python 3.12, 12 hours)

The unbounded-`f`, strict prepass through `D=200` has 1,393 `(N,D)` cells
(`N=2..8,D=2..200`).  Of these, 780 have a raw scalar profile and 777 survive
the square/sum parity prefilter:

| N | raw profiles | after parity | raw active cells | parity-active cells |
|---:|---:|---:|---:|---:|
| 2–4 | 0 | 0 | 0 | 0 |
| 5 | 93,610 | 46,756 | 195 | 194 |
| 6 | 110,600 | 55,300 | 194 | 193 |
| 7 | 258,090 | 138,360 | 196 | 196 |
| 8 | 290,380 | 144,806 | 195 | 194 |
| **total** | **752,680** | **385,222** | **780** | **777** |

The Moh-compatible half `101<=D<=200` contains 580,550 raw profiles and
297,200 after parity, across 400 active cells.  These are parameter-row
counts, not predicted cluster counts.  There is no honest pre-run estimate of
the number of solution records; each is serialized in full, and any resource
cut leaves an explicit lower bound rather than a guessed count.

The following job uses 48 of 64 CPUs to leave memory and merge headroom.  Each
worker has an 11-hour internal forest-search deadline and a 250,000-state cap;
either cap makes that cell incomplete.  The job reserves its last 30 minutes
for merge and hashing inside a hard 12-hour budget.  A timeout can leave files
missing, which `merge` records fail-closed.  Every invocation gets a fresh
`mktemp` run directory under `~/cluster_census/`; the enumerator also refuses
an existing shard path, so a stale shard cannot be mistaken for current work.
The job snapshots and hashes the engine once, preventing a live checkout edit
from mixing source versions.  Set `repo` to the checked-out repository on
box01.

```bash
#!/usr/bin/env bash
set -euo pipefail

repo=${1:?usage: run-keller-census /absolute/path/to/jc2}
source_py="$repo/box/keller_cluster_census.py"
census_root="$HOME/cluster_census"
mkdir -p "$census_root"
census_out=$(mktemp -d "$census_root/run-20260902.XXXXXX")
rows_dir="$census_out/rows"
mkdir -p "$rows_dir"
job_deadline=$(( $(date +%s) + 43200 ))
printf '%s\n' "$census_out" > "$census_out/RUN_DIRECTORY"
census_py="$census_out/keller_cluster_census.py"
install -m 0755 "$source_py" "$census_py"
sha256sum "$census_py" > "$census_out/ENGINE_SHA256"

python3.12 "$census_py" self-test > "$census_out/self-test.json"
python3.12 "$census_py" plan \
  --n-min 2 --n-max 8 --d-min 2 --d-max 200 \
  --window strict --f-cap unbounded > "$census_out/plan.json"

: > "$census_out/cells.txt"
for N in $(seq 2 8); do
  for D in $(seq 2 200); do
    printf '%s %s\n' "$N" "$D" >> "$census_out/cells.txt"
  done
done

export census_py rows_dir
run_cell() {
  N=$1
  D=$2
  set +e
  python3.12 "$census_py" census \
    --N "$N" --D "$D" --window strict --f-cap unbounded \
    --max-states 250000 --deadline-seconds 39600 \
    --output "$rows_dir/$(printf 'N%03d-D%03d.jsonl' "$N" "$D")"
  cell_rc=$?
  set -e
  case "$cell_rc" in
    0|2) return 0 ;;
    *) return "$cell_rc" ;;
  esac
}
export -f run_cell

set +e
parallel_budget=$(( job_deadline - $(date +%s) - 1800 ))
if (( parallel_budget <= 0 )); then
  printf '%s\n' 'no worker budget remained after preflight' >&2
  exit 75
fi
timeout --signal=TERM --kill-after=180 "${parallel_budget}s" \
  parallel --jobs 48 --colsep ' ' --joblog "$census_out/joblog.tsv" \
  run_cell {1} {2} :::: "$census_out/cells.txt"
parallel_rc=$?
set -e
printf '%s\n' "$parallel_rc" > "$census_out/parallel.rc"

set +e
merge_budget=$(( job_deadline - $(date +%s) ))
if (( merge_budget > 0 )); then
  timeout --signal=TERM --kill-after=30 "${merge_budget}s" \
    python3.12 "$census_py" merge \
      --n-min 2 --n-max 8 --d-min 2 --d-max 200 \
      --expected-window strict --expected-f-cap unbounded \
      --expected-profile-mode H2-common-n \
      "$rows_dir" --output "$census_out/all.jsonl"
  merge_rc=$?
else
  merge_rc=124
fi
set -e
printf '%s\n' "$merge_rc" > "$census_out/merge.rc"
hash_budget=$(( job_deadline - $(date +%s) ))
if (( hash_budget > 0 )); then
  timeout "${hash_budget}s" bash -c '
    find "$1" -type f \( -name "*.json" -o -name "*.jsonl" -o -name "*.py" \) -print0 \
      | sort -z | xargs -0 sha256sum > "$1/SHA256SUMS"
  ' _ "$census_out"
fi
printf 'run directory: %s\n' "$census_out"
```

Interpretation of return codes is deliberate: `0` means complete, `2` means
well-formed but incomplete, `64` means invalid input or data, `70` means an
internal/resource failure with no complete result emitted, and `124` is the
outer timeout.  Missing worker files and return code 2 must not be converted to
zero counts.  When `all.jsonl` exists, its last record is the only box-wide
“smallest D” table.

## 8. Opens, limitations, and FALLACY-v2 audit

The census resolves no realization question.  It enumerates exact numerical
forests satisfying necessary equations and nefness, but not a base-point-free
pencil or a polynomial pair.  No output advances beyond
`NUMERICAL_PROFILE/NECESSARY`.

Two existing opens remain, with their bounded quantities stated explicitly:

- **OPEN[ANTICANON-DEFECT]:** whether the integer
  `Z.K_X=sum a_i-3D=-2N-kappa+n(W-S)` is bounded above by a function of `N`
  for noninvertible Keller maps.  The default run leaves `f` unbounded.
- **OPEN[SAT-MASS]:** whether the integer
  `T=D-Sn-kappa=sum_{satellite}a_i` is bounded in `N` for a degree-minimal
  representative.  The census bounds it only through the declared `D_max`.

Resource-incomplete box cells are engineering incompleteness over the finite
declared domain, not a new mathematical OPEN and not an empty verdict.

The FALLACY-v2 checks are reflected directly in the schema: fixed sheets `a`,
base multiplicities `a_i`, polar multiplicities `m_C`, and ramification
lengths `mu_l` are never identified; each sheet/dicritical is counted once;
equal-degree `mu` attachment is left unpinned; floors are not treated as
attainment; Moh is only an actual-map floor; and no representative numerical
cluster is promoted to an actual map.  No exit-price assertion is made, so no
`charge_basis` declaration is applicable.

## 9. Reproducibility inventory

```text
enumerator: box/keller_cluster_census.py
engine revision: 20260902.8
source bytes: 105920
source SHA-256: ef17664c5ff72f80e4a208f1c1b0023ea6d43910da0384c21c4088c6740c3569
self-test: PASS (ordinary and python -O)
desk JSONL SHA-256: af63f41a3ee43359574e2b5eae3186ce87cd8a3628d37ed2673e573fe86b617d
```

The report and enumerator are the only repository writes made by this lane.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19609`.
- Body SHA-256:
  `4eda5650f1a655c1ba27917a5d86eaf5f16ef679c099680ee31bcae41dc4241d`.
- Frozen basis: `6557a4ad6a9d0cbe8fba9394e3371b938235a56f`.
