# D23-core characteristic-zero certification

**Pre-registered next-day plan, 2026-08-17.**  Joint Codex / GPT-5.6 Sol
co-research.  This is a plan, not a verdict and not authorization to alter the
currently running lanes.  Trigger: the authenticated D23 main lanes return
`GB = [1]` at all banked primes.  If that trigger fails, follow Decision D0
below instead.

The object is the hybrid D23 core of `SHEET6-DIRECTIONB.md:1187-1223`:
`cases/directionb_core23_p*.ms`.  The intended implication is

```text
exact unit certificate for the canonical D23 core
    => no characteristic-zero point on the stated saturated D23 chart
    => residue-A depth-23 window death
    => on-axis td=6 closure, only after a separate bridge/scope review.
```

The last two arrows are not silently bundled into the computation.  They get
their own review gate.

## 0. Decision up front

1. **A proof-bearing full characteristic-zero GB is not presently costed as
   feasible.**  The live D23 jobs were launched without `-v 2` and without
   `/usr/bin/time -v`; their outputs cannot supply the degree/matrix trace or
   final peak RSS needed for an honest estimate.  At a planning-time read-only
   snapshot, after about 9.2 minutes the fiber had reached 7.36 GiB HWM and the
   two mains 17.74/17.76 GiB and were still growing.  Thus the premise
   "fresh GBs are seconds each" has not yet been established for the D23 main
   object.  These lower bounds already exclude the green class below for the
   specialized 87-variable main presentation; its replay can only classify it
   yellow or red.
2. **If the post-verdict verbose replay is trace-green, a bounded char-0 run is
   worth doing as reconnaissance:** 256--512 GiB / 2 hours first; at most one
   isolated Box02 continuation, with a 1.2-TiB planning projection, a hard stop
   at 70% of measured `MemTotal`, and a 24-hour cap, if a provenance-capable
   exact pilot gives a defensible coefficient-growth projection.  This gate
   must come from the same 88-variable Q-flat presentation; a specialized
   trace does not transfer.  A displayed msolve char-0 `[1]` is strong
   evidence, but it is not the final certificate under this plan because
   msolve does not export cofactors.
3. **The primary proof route is a targeted, trace-driven multimodular
   Nullstellensatz certificate.**  Row 22 has ten affine deep variables but
   constant rank four after chart-unit factors are removed.  Replace its ten
   equations by six exact compatibility equations, keep provenance back to the
   pristine rows, then certify the D21 core plus those six equations.
4. **The 397-element D21 basis helps, but does not make lifting automatically
   small.**  It is a positive-dimensional, 282,304-term GB, not a 397-element
   vector-space basis, and it carries no transformations to the input rows.
   Use it as a stable normal-form/learning skeleton and retain only terminal
   ancestry.
5. **No finite combination of ordinary mod-p `[1]` results, a partial char-0
   run, and structural plausibility earns the decisive claim.**  The promotion
   endpoint is an exact identity over `Q(sqrt(3))`, or an exact checked
   arithmetic DAG that composes to one.  The multi-prime wave is defense in
   depth, not a replacement for that identity.

This deliberately exceeds the older three-prime/same-engine posture recorded
in `AUDIT.md:281-299`.

## 1. Freeze the exact mathematical object

### 1.1 Canonical ideal

Let `s^2 = 3` and `K = Q(s)`.  With the variable order frozen from the main
artifact, define

```text
I23 = < C1,...,C38, P1,...,P22, R1,...,R10, T1,...,T7 > in K[x1,...,x87],
```

where `C` are the compressed D21 CORE2 rows, `P` the pristine defining pivot
rows, `R` the pristine Row-22 rows, and `T` the radical/saturation rows.  The
main files parse as 87 distinct variables and 77 equations.

For engines over `Q`, use the preferred flattened presentation

```text
I23_Q = <the same 77 rows with s retained, s^2-3> in Q[s,x1,...,x87].
```

This is an 88-variable, 78-generator rational ideal.  A final integer
certificate has the durable form

```text
A = sum_i H_i F_i + H_s (s^2-3),
A in Z \ {0},  H_i,H_s in Z[s,x].
```

That identity proves the required characteristic-zero emptiness directly.
It also avoids ambiguity about which complex embedding of `sqrt(3)` was used.
Do **not** flatten an equation `a+s*b=0` into the two equations `a=b=0`; that
is not an equivalent operation when the unknown coordinates range over `K`.

### 1.2 Parser-derived census, not prose-derived census

The exact row census of `directionb_core23_p105337.ms` is:

| zero-based rows | role | equations | terms |
|---|---|---:|---:|
| 0--37 | D21 CORE2 | 38 | 6,311 |
| 38--59 | pristine pivot definitions | 22 | 17,017 |
| 60--69 | pristine Row 22 | 10 | 35,988 |
| 70--76 | radical/saturation | 7 | 15 |

Thus `59,316 terms` is the campaign convention for the first 70 core rows;
the literal file contains 59,331 terms including the seven tower/guard rows.
Degree is at most 13.

One preflight discrepancy must be resolved before a fiber decomposition is
used in a proof: `cases/directionb_core23_fiber_p105337.ms` actually has 82
distinct header variables and 72 equations, whereas
`SHEET6-DIRECTIONB.md:1204-1205` says 80 variables.  The full 87-variable main
object is unaffected, but the fiber legend must say exactly which five
variables have been specialized.  No fiber certificate may be promoted until
this census is reconciled.

### 1.3 Canonical emission rule

Before CRT or a char-0 run:

1. emit one canonical char-0 generator list from the exact tower machinery;
2. primitive/content-normalize every rational row with a fixed leading-sign
   convention;
3. freeze variable order, generator order, monomial order, and row labels;
4. hash every row and the whole artifact;
5. derive every new modular input by reduction of this frozen artifact;
6. if a legacy prime file differs by a nonzero row scalar, record that scalar
   explicitly and verify the equality, rather than treating equal support as
   equal generators.

Independent per-prime row scaling is fatal to naive cofactor CRT.  This gate is
load-bearing.

Required exact emission replays are the D21 38-row prefix, all 22 pivot rows,
the unique `+42`, the ten Row-22 rows, tau/conjugation, the radical and
saturation rows, independent parser round-trip, source back-substitution, and
the 12-point filter replay already listed at
`SHEET6-DIRECTIONB.md:1207-1216`.

## 2. The targeted object: six Row-22 compatibilities

### 2.1 Correction to the proposed "32-condition contradiction"

The registered 32 D21 residual conditions are **not** a contradiction.
`SHEET6-DIRECTIONB.md:540-552` explicitly proves that they vary with the low
data; at D21 the relevant fixed-radical locus is nonempty and 13-dimensional.
Therefore a certificate using the 32 conditions alone cannot exist at the
banked primes.

The valid targeted question is:

```text
Is 1 in the ideal generated by the D21/CORE2 conditions together with the
six compatibility conditions forced by Row 22?
```

Equivalently, use the full D21 hybrid plus all ten Row-22 equations.  The first
form is substantially smaller and is the preferred certificate target.

### 2.2 Exact rank-four structure

The only variables first introduced in main rows 60--69 are `x74,...,x83`,
and each occurs affinely.  Write

```text
R22(z,y) = A(z)y + b(z),      y = (x74,...,x83)^T.
```

The matrix `A` has only 96 monomial terms total; `b` has 35,892.  Direct
support inspection gives

```text
A = C * diag(u1,...,u10),
```

where `C` is a constant 10-by-10 matrix over `K` and the column factors are
among

```text
1, A2^2*HW2, A1^2*HW1, A2^2*W2, A1^2*W1.
```

Modulo the banked prime, `rank(C)=4`; ten independent evaluations give
`rank(A)=4` and `rank([A|b])=5`, in agreement with the exact first-occurrence
rank in `xmodel/sol-instrument3.md:309-317`.  A modular left-kernel basis gives
six compatibility rows, each 4,376 terms, degree at most 13, with no deep
variables.

The next-day exact gate is to reconstruct this factorization over `K` and
make the rank statement certificate-producing:

1. construct `U,V in GL_10(K)` with

   ```text
   U*C*V = diag(I4,0_6),
   ```

   and verify `U`, `V`, and both inverses exactly;
2. prove each `u_j` is a unit on the stated chart;
3. make the certified changes `y' = diag(u_j)y` and `y'=V*y''`;
4. take `L` to be the bottom six rows of `U`, and verify that the transformed
   system consists of four defining equations for four coordinates of `y''`
   and the six compatibility equations `c := L*b=0`.

The unit proof must be explicit.  `W_i` is inverted by the existing `uW_i`
row; `A_i^3=3 +/- s` makes `A_i` a unit over `K`; and
`2 HW_i^2=3 W_i^2` makes `HW_i` a unit when `W_i` is.  Record the polynomial
identities, not just field-level prose.

This split normal form remains exact after base change to every `K`-algebra.
Once these items pass, no minor/rank-drop branch is missing: the rank is
globally four because the only variable column factors are units.  The ten
Row-22 rows can be replaced, for emptiness, by the six rows `c=L*b`.

### 2.3 Relative certificate pipeline

The preferred target is built in this order:

1. form the six `L*b` rows **before** substituting any of the 22 pivot
   definitions;
2. retain the direct provenance `L*R22 = L*b`, since `L*A=0`;
3. substitute the 22 pivot definitions into only those six rows, normalizing
   `W`-units and reducing modulo the unspecialized D21 ideal after every step;
4. retain an arithmetic DAG for every substitution, radical-lattice
   reduction, and unit stripping;
5. reduce the six rows with an unspecialized D21 GB in which the radical
   variables remain live, or with an explicitly exhaustive finite-factor
   decomposition;
6. compute an incremental GB or Nullstellensatz representation for
   `I21 + <c1,...,c6>`;
7. compose the resulting representation through the DAG back to the 77 frozen
   hybrid generators, then separately check source-to-hybrid provenance.

The 397-polynomial fixed-radical GB may be used only for modular discovery,
support learning, and fiber-local normal forms.  The proof pass must either
use an unspecialized D21 basis with the radical variables retained, or provide
an exact exhaustive factor decomposition, idempotent recombination, and
Galois descent.  No fixed-fiber normal form may be composed directly into the
global certificate.

This avoids the measured bad representation: substituting every pivot into
all ten Row-22 rows produced 4,971,007 terms and degree 32
(`SHEET6-DIRECTIONB.md:1191-1197`).

For every stripped factor, keep the ideal identity.  For example, if
`uW*W-1=0` and `g=W^a f`, then

```text
f = uW^a g - (uW*W-1) * f * sum_{k=0}^{a-1} (uW*W)^k.
```

Analogous recorded steps lift reductions by `A_i^3-(3 +/- s)` and
`2 HW_i^2-3 W_i^2` back to the original generators.

### 2.4 Minimal-core mining

If D23 is modularly empty, find a small stable input core before asking for
large cofactors:

1. add the six compatibility rows incrementally to the proper D21 ideal;
2. delta-debug row blocks, then individual rows, at two learning primes;
3. require the same row-label core at a third prime;
4. freeze that row set before coefficient reconstruction;
5. verify that removing all Row-22 compatibility rows restores the proper D21
   control.

This is discovery only.  The final exact identity, not minimality, proves the
claim.  A sparse core may expose a human lemma, as the 3-of-21 cofactor support
did in `CERT-UPGRADE.md:82-120`.

## 3. What the 397-polynomial D21 basis buys

The fixed-radical D21 fiber has a stable 397-polynomial basis at all three
banked primes.  Its retained verbose trace at p=105337 measures:

| field | value |
|---|---:|
| variables / equations | 22 / 26 |
| basis polynomials / terms | 397 / 282,304 |
| serialized GB | 10,532,902 bytes |
| output max degree / pair degree | 12 / 14 |
| peak matrix | 399,924 x 920,821 at printed 0.010% |
| F4 wall | 10.84 s |
| symbolic preparation | 9.00 s (83%) |
| linear algebra | 0.41 s |
| pairs / rows / zero reductions | 3,313 / 7,025 / 2,797 |
| symbolic / basis hash peaks | 2^20 / 2^21 |

Per-polynomial support ranges from 2 to 13,424 terms (median 184, p95 2,679).
This is a useful, cheap normal-form scaffold.  It is **not** a finite quotient
basis: the quotient is 13-dimensional, so multiplication-matrix lifting is
not available.  It is also not a cofactor representation.

Consequences:

- lifting the 282k scalar GB coefficients could be modest;
- lifting a full 397-by-input transformation matrix could be enormous;
- the correct object is the reduction/row-operation DAG reachable from the
  terminal unit, not provenance vectors for every intermediate basis row;
- a fixed-fiber certificate proves only that fiber.  A global proof either
  keeps the radical variables or supplies an exact, exhaustive fiber cover.

The 397 structure makes the targeted incremental route plausible, not
automatically tractable.  Tractability is decided by the measured terminal
ancestry/cofactor support below.

## 4. Telemetry estimator to execute after the lanes finish

### 4.1 Current telemetry gap

The live D23 commands are plain `msolve -g 2 -t 4`.  They have neither verbose
F4 output nor a GNU-time footer.  Do not interrupt them.  Treat their sampled
elapsed/RSS values as censored lower bounds.  After they terminate, run an
instrumented representative replay sequentially, without other heavy jobs,
using:

```text
same msolve 0.10.1 binary and input hash
-g 2 -t 4 -v 2 --random-seed 1786403517
GNU time -v (or equivalent)
5-second RSS/HWM/VM/fault/I/O sampler
```

Maintain three separate telemetry classes:

```text
S87 = the specialized 87-variable main presentation,
Q88 = the canonical 88-variable Q-flat presentation with s^2-3,
T   = the six-compatibility targeted presentation.
```

No trace color or resource projection transfers between them.  The specialized
`s -> +/-sqrt(3)` S87 runs are equivalence controls for Q88, not cost samples
for it.  Replay an S87 input to recover its structure; after canonical emission
run one Q88 fresh-prime trace first, and only if it completes below the red
veto run two more.  Apply the same one-then-two adaptive schedule to T.  D6
requires three stable completed Q88 traces.  Use the worst authenticated
good-prime trajectory within each class, never the fastest or a vote over
outliers.

### 4.2 Exact parser contract

Preserve the printed round sequence: degrees can repeat and appear out of
numeric order.  For each `-v 2` F4 row record

```text
(seq, degree, selected pairs, pair-list size,
 matrix rows, matrix columns, printed density interval,
 new basis elements, zero reductions, real seconds, CPU seconds).
```

The historical format is visible in
`runs/r1/r1_25chain_core.err:22-123`; char-0 multi-modular fields are at
`:151-182`.  Parse `reduce final basis` separately.  Require
`new + zero = selected`.  Printed density is rounded: `0.00%` does not mean a
zero matrix, so store an interval rather than an invented exact nonzero count.

Also retain:

- complete input/options/host/binary hashes, the exact seed, and the verbose
  `Initial seed` header;
- input term, degree, and coefficient-height histograms;
- phase times (`select`, symbolic preparation, update, convert, linear
  algebra, final reduction);
- final basis size/terms/max degree/leading-monomial hash;
- pairs, rows, zero reductions, and symbolic/basis hash peaks;
- char-0 initial/new primes, number of polynomials lifted, maximum coefficient
  bits, good/bad-prime count, CRT and rational-reconstruction times;
- OS time series and terminal return code/output bytes.

A missing footer, partial final line, zero-byte output, timeout, or nonzero
return code is censored data, not a completed trace or a verdict.

### 4.3 Structural features

For round `j`, with printed density interval `[rho_j^-,rho_j^+]` percent, use

```text
A_j = rows_j * cols_j,
NNZ_j in A_j * [rho_j^-,rho_j^+] / 100.
```

Record `Dmax`, peak rows/columns/NNZ, cumulative rows and estimated NNZ, basis
term mass, pair backlog, phase wall, and hash exponents.  The full ordered
tuple of degrees, pairs, dimensions, and new/zero rows is the stock trace
fingerprint; add pre-unit pivots/leading monomials when an instrumented engine
exposes them.  Degree is a feature, not a progress clock: verbose degrees can
reset, repeat, and arrive out of order.  Progress and cross-field fits must
align by ordered round, generator batch/phase, and trace fingerprint.

Do not rank jobs by dense cell count.  The D21 fiber's nominal peak matrix has
`3.68e11` cells but completed in 11 seconds because it was extremely sparse;
symbolic monomial generation dominated.  Use observed RSS, columns/monomial
universe, estimated NNZ, hash size, and symbolic-preparation wall.

For a censored trajectory only, fit upper envelopes of

```text
log(rows), log(cols), log(NNZ), log(round wall)
```

against the last 3--5 ordered checkpoints within one contiguous phase.  Do not
fit across a degree reset or generator-batch boundary.  Report a range, not a
point forecast.  Once a mod-p run completes, its actual structural trace is
the better predictor for trace applications.

For a prime wave also compute

```text
effective_cores = CPU_seconds / wall_seconds,
P_mem = floor((RAM_plan - baseline_RAM) / per_lane_RSS),
P_cpu = floor(vCPU / effective_cores),
P = min(P_mem, P_cpu, lane_count),
wave_wall ~= ceil(lane_count/P) * worst_good_wall,
wave_CPU = sum(per_lane_CPU).
```

Use measured effective cores, not the requested `-t 4`; historically sparse
symbolic phases have used close to one effective core.

### 4.4 Why mod-p telemetry cannot estimate coefficient growth by itself

The direct rational cost depends on coefficient bit heights absent from a
finite-field trace.  A structurally identical exact matrix may need many-limb
arithmetic and much more storage.  The estimator therefore refuses to price a
proof-bearing exact run until a capped exact pilot supplies, by aligned ordered
checkpoint within one phase,

```text
coefficient bit-height distribution,
coefficient slots/term count,
exact RSS and wall,
same-checkpoint slowdown k_j = t_Q,j / t_p,j.
```

For `N_j` stored coefficients of height `B_j` bits at checkpoint `j`, use the
storage floor

```text
M_Q,j >= N_j * (c0 + q*ceil(B_j/8)),
```

with `c0=32--64` structural bytes, `q=1` for fraction-free integers or roughly
2 for numerator/denominator storage, followed by a 2--4x allocator/hash safety
factor.  Fit `log(k_j)` and `B_j` only after at least three aligned completed
checkpoints.  If the exact engine cannot align to the ordered pre-unit trace,
or exposes no coefficient heights, the full run remains **unpriced**.

For msolve's multi-modular rational GB path, a stable trace gives

```text
T_Q ~= T_learn + (nprimes-1)*T_apply + T_CRT + T_ratrecon.
```

That can make a rational *basis* run cheap.  For a unit ideal, however, the
reduced basis is just `[1]`; its coefficient height is zero and says nothing
about the height of the hidden cofactors.  It does not price the certificate.

### 4.5 Green / yellow / red gate

Classify green/yellow only after at least three good-prime results have the
same ordered pre-unit round signature, unit-arrival checkpoint, and trace
envelope; a provenance-capable trace must additionally have the same
staircase/pivot profile.  Stock `-v 2` does not expose every pivot, and final
leading support is always `{1}` for an EMPTY run, so neither may be invented
as a discriminator.  One authenticated red resource crossing vetoes D6 for
that presentation; a divergent trace returns to bad-prime/emitter audit.

**Green structural trace**

- all verdicts `[1]`, no trace anomaly;
- the unit arrives at the same ordered checkpoint with no unexplained late
  trace divergence;
- peak modular RSS below 16 GiB;
- peak columns below about 2 million and cumulative estimated NNZ below about
  `2e8`;
- wall below roughly one minute.

Green earns a 256--512 GiB / 2-hour provenance-capable exact pilot.  Continue
only if the pilot reaches the penultimate trace-aligned pre-unit checkpoint,
coefficient height remains below 1,000 bits, and its upper projection fits the
resource fences below.

**Yellow**

- stable complete modular result, but 1--30 minutes, 16--128 GiB, or 2--20
  million peak columns;
- exact projection at most 1.2 TiB and at most 24 hours.

Yellow permits one isolated Box02 / 24-hour run only after the exact pilot,
with a 1.2-TiB planning projection and the 70%-of-`MemTotal` hard stop; modular
telemetry alone cannot authorize it.

**Red**

- mixed verdicts or support/rank divergence;
- modular wall over 30 minutes, RSS over 128 GiB, or peak columns over 20
  million;
- exact coefficients grow by more than 4x in bits per successive aligned
  checkpoint within a phase;
- exact RSS exceeds 128 GiB before the penultimate pre-unit checkpoint;
- upper projection exceeds 1.2 TiB or 24 hours.

Red skips the monolithic char-0 GB and goes directly to the targeted/DAG
certificate.  Failure of a compute gate is not evidence of nonemptiness.

### 4.6 Iron and cash fences

Repository-recorded inventory/rates (`ops/FLEET.md:12-29` and
`xmodel/sol-instrument3.md:486-505`):

| host | nominal RAM | planning / hard RSS fence | recorded cost |
|---|---:|---:|---:|
| Box03 | 512 GiB | 300 GiB / 70% measured `MemTotal` | about $4.03/h |
| Box02 | 2 TiB | 1.2 TiB / 70% measured `MemTotal` | about $13/h |

Rules:

- no full char-0 job on shared box01; it has about 991 GiB but a farm baseline
  and only about 88 GiB root-disk headroom at planning time;
- size scratch and verifier RAM from the projected CRT accumulator/DAG live
  frontier; require at least `max(3x serialized artifacts, 1.5x projected
  verifier spill/frontier)` of scratch;
- stop at 70% of the host's measured physical RAM;
- the full attempt must have P90 wall below 24 hours and is hard-stopped there;
- the Box02 budget ceiling is about $312/24 h;
- the former 6-TiB ultramem host is retired under `ops/FLEET.md`; this decision
  tree has no 6-TiB branch;
- Box03's installed apt msolve is 0.6.5 and is screening-only.  It may define
  no frozen support, pivots, trace, or CRT residue until campaign-standard
  0.10.1 and the chosen extraction engine are installed, pinned, and hashed.

Historical priors justify the caution: the 27-variable cCa2 Singular lift
returned nothing in a 120-second probe at 634 MiB and later long lift attempts
were retired (`CERT-UPGRADE.md:70-80`, `AUDIT.md:601-606`); cCa6's char-0 run
needed 17h43m and 761 GiB (`AUDIT.md:275-280`).  Variable count alone is not a
cost model.

## 5. Multimodular certificate reconstruction

### 5.1 Extraction substrate

msolve 0.10.1 has no released option that emits `h_i` in
`1=sum h_i f_i`; see `CERT-UPGRADE.md:32-52` and the
[official msolve interface](https://github.com/algebraic-solving/msolve).
One of the following is therefore required, ranked:

1. Singular modular `liftstd` / `lift(I,ideal(1))` on the six-compatibility
   target; Singular documents that `liftstd` returns a standard basis and its
   transformation matrix;
2. a deterministic trace/Macaulay replay that tracks only the ancestry of the
   terminal constant row;
3. a patched msolve provenance pass over a frozen trace;
4. Groebner.jl learn/apply for trace acceleration, augmented with explicit
   representation tracking.  Its
   [official interface](https://sumiya11.github.io/Groebner.jl/interface/)
   warns that trace application can be probabilistic; it is never the final
   checker.

The CERT-UPGRADE small-scale pipeline is the functional precedent: modular or
char-0 extraction followed by independent python-flint multiplication
(`CERT-UPGRADE.md:56-68`).

### 5.2 Cofactor pilot and go/no-go metrics

At each learning prime measure:

```text
number of nonzero cofactors,
total cofactor monomial count S,
maximum cofactor and product degree,
P = sum_i support(h_i) * support(f_i),
serialized size,
extraction wall/RSS,
terminal ancestry DAG nodes and scalar count.
```

Proceed with flat cofactor CRT only if three primes have the same canonical
support and pivot profile, the modular witness is at most 20 GiB, and total
cofactor support is at most about `1e7` terms.  These are storage/operations
gates, not mathematical bounds.  If support is unstable or crosses either
gate, switch to the pruned DAG or the targeted six-row route; do not keep
adding primes blindly.

### 5.3 Canonicalization: cofactors are not unique

Arbitrary `lift()` results at different primes cannot be matched by row number.
Freeze:

- the exact canonical generator normalization;
- generator and monomial order;
- the learned monomial universe and pivot columns;
- row swaps/scalings and the convention that all free solution coordinates
  are zero;
- the cofactor/DAG support after the discovery wave.

A reliable pattern is: learn support at three primes, freeze it, then solve the
same fixed-support linear system with deterministic RREF at every later prime.
Reject a prime when a frozen pivot vanishes, rank changes, or support/leading
staircase changes.  It is an unlucky/bad prime, not data to force into the CRT.

### 5.4 Preferred rational flattening

The cleanest CRT route keeps `s` as a polynomial variable and includes
`s^2-3`.  Then every reconstructed scalar is rational and ordinary
coefficientwise CRT applies.  At split primes this single unspecialized ideal
contains both `s` components; `[1]` means both are empty.

The existing D23 files specialize one embedding.  Before relying on the
flattened route, run the canonical unspecialized reduction at three fresh
split primes and check it against both specialized `+/-s_p` lanes and exact
tau transport.

If a native `K=Q(s)` representation is used instead, compute both embeddings
at every rational prime.  Freeze one learning trace over the `+` embedding
and mechanically tau-transport that same trace, generator order, pivots,
free-coordinate convention, and DAG topology to the `-` embedding.  Verify
node-for-node conjugacy; independently computed witnesses can differ by
syzygies and must not be paired coefficientwise.  Only then recover

```text
a mod p = (c_plus + c_minus)/2,
b mod p = (c_plus - c_minus)/(2*s_p)
```

for a coefficient `a+b*s`.  A single embedding does not support ordinary
componentwise reconstruction of `a` and `b`.  Never mix native-K and
Q-flattened residues in one CRT.

### 5.5 Prime ledger and adaptive reconstruction

Pre-register the fresh primes before reading their verdicts:

1. starting above `2^30`, scan upward for primes below `2^31` with
   Legendre symbol `(3/p)=+1`;
2. exclude 2, 3 and primes dividing the canonical input denominators,
   contents, pivot-unit norms, or discriminant ledger;
3. take the first 19 admissible primes in that deterministic order;
4. use primes 1--3 for trace/support learning; after freezing the
   representation, replay them and use primes 1--16 as the reconstruction and
   trace-replay set;
5. keep primes 17--19 untouched as holdouts;
6. if more modulus is required, append deterministic working primes beginning
   at prime 20 while leaving 17--19 permanently outside the CRT.

The three small banked primes remain legacy checks and do not replace this
fresh wave.  Reproduce two fresh primes with a second GB implementation.

For coefficient numerator/denominator height at most `H` bits, 29--30 usable
bits per prime, and safety `sigma` bits,

```text
nprimes >= ceil((2*H + sigma)/bits_per_prime).
```

Use at least `sigma=128` for planning.  Since `H` is unknown, reconstruct after
8, 16, 32, 64, ... use-primes.  A candidate may be tried as soon as it appears,
but it is accepted only when the **exact** identity verifies.  Stability over
two modulus doublings and three fresh holdouts is a diagnostic, not a logical
substitute for exact verification.

With `C` reconstructed scalars and `n` primes, raw CRT storage is at least

```text
C*n*bits_per_prime/8,
```

before a 2--4x GMP/container allowance.  Streaming CRT by `(cofactor row,
monomial)` key avoids retaining every prime witness.  If complete modular
outputs are retained, disk is `n * one-prime-output-size`.

### 5.6 Trace-driven provenance / DAG variant

If flat cofactors are large, use two passes.

**Learning pass:** record selected pairs, symbolic monomial sets, reducers,
pivot columns, row swaps/scalings, and the terminal constant row.  Hash the
trace.

**Provenance pass:** for Q-flat computation initialize the 78 generators (or
74 targeted generators), including `s^2-3`; for native `K`, initialize 77 (or
73 targeted) generators.  Walk backward from the terminal constant and retain
only reachable nodes.  A node records scalar/monomial multiplication and exact
addition of earlier nodes.  Do not attach an expanded generator vector to
every one of the 397 D21 basis polynomials.

Replay the frozen DAG at later primes.  CRT-lift its scalar coefficients or,
if still small, its final cofactors.  The exact certificate may remain a DAG:
an independent checker that verifies every node and obtains the nonzero
constant at the root proves precisely the same ideal-membership statement as
an expanded `sum h_i f_i`.

If no engine exposes a suitable trace, reconstruct the terminal Macaulay
system on the **observed trace monomial universe**, not on every monomial in
87 variables.  Freeze the RREF pivots and solve for the constant row with
provenance.  Verify the resulting degree claim by multiplication; do not infer
it from F4 sugar alone.

## 6. Direct full char-0 GB lane

This lane is secondary and runs in parallel only after a Q88 green/yellow
gate from the identical frozen presentation.

### 6.1 Two meanings of "char-0 GB"

1. **msolve multi-modular rational run.**  This can reuse a finite-field trace
   only from the identical Q88 presentation and may finish near modular cost.
   Its `[1]` is reconnaissance here: msolve exposes no cofactors, and its `-g`
   output is described as the reduced GB for the first prime.  Bank the full
   verbose prime/reconstruction record, but do not end certification there.
2. **Proof-bearing exact computation.**  Singular `liftstd`, a provenance F4,
   or another exact engine produces transformations to the canonical input.
   This is what coefficient growth threatens and what the exact-pilot
   estimator prices.

### 6.2 Attempt order

1. First obtain the three same-presentation Q88 modular traces required by
   section 4.
2. Run pinned msolve on the identical frozen Q-flat object only as verbose
   multi-modular reconnaissance, with a 256--512 GiB / two-hour fence.
3. Separately run a capped provenance-capable exact-engine pilot on that same
   Q-flat input.  Only this run's aligned checkpoint, coefficient-height, RSS,
   and wall telemetry can authorize one Box02 continuation.
4. Continue on Box02 only with an upper projection below 1.2 TiB and 24 hours;
   hard-stop at 70% of measured `MemTotal` or 24 hours.
5. If msolve prints a bare `[1]`, archive it and return to D5; do not ask that
   run for a transformation it cannot emit.

A provenance-capable run that stops after an aligned trace prefix may provide
coefficient-height calibration.  Neither it nor a bare msolve `[1]` combines
with finite-prime results to prove emptiness.

## 7. Exact verification and artifact package

### 7.1 Required exact checks

The final cofactor or DAG must be checked against the frozen char-0 generator
hashes, not a regenerated look-alike.

1. clear denominators and verify the integer identity coefficient by
   coefficient;
2. reduce powers of `s` only through the explicit generator `s^2-3` (or retain
   its cofactor in the Q-flat identity);
3. verify all targeted compatibility and pivot-provenance nodes back to the 77
   frozen hybrid generators;
4. independently parse the certificate twice;
5. check it with two exact paths: a streaming python-flint/custom sparse
   checker and a second CAS/replayer; if Singular extracted it, Singular alone
   is not the independent check;
6. reduce the frozen identity at the three untouched 30-bit holdouts and at
   both `sqrt(3)` embeddings as a fast tripwire before the expensive exact
   multiplication;
7. verify the final constant `A` is nonzero.

Random evaluations alone never promote a certificate.

### 7.2 Negative and wrong-object controls

The certification package must also show:

- D21-only remains proper at all banked primes and reproduces the 397-element
  structure;
- removing the six Row-22 compatibilities destroys the terminal certificate;
- a D23-targeted constant-block-dropped control, emitted by the same canonical
  pipeline, has an exhibited exact satisfying point; until that exists, label
  any legacy D21 `ctl0`/origin result as a parser/emitter control only, not a
  validation of the D23 Row-22 emission;
- both tau embeddings and the unspecialized `s^2-3` object agree;
- mutating/removing the unique `+42` trips a guard;
- main and fiber variable/row legends match parser-derived censuses;
- all mod-p coefficients are in `[0,p)`, with independent evaluation
  round-trip, per `AUDIT.md:565-577`.

### 7.3 Reproduction package

Archive immutably:

```text
canonical char-0 input and row legend;
all derived prime inputs and the deterministic prime/bad-prime ledger;
SHA-256 of inputs, outputs, binaries, certificate, and verifier;
complete commands, seed/control status, engine versions/builds, host specifications;
-v 2 logs, GNU-time files, OS samples, return codes and output sizes;
trace/support/pivot fingerprints and rejected-prime reasons;
cofactor or DAG plus both independent verifier transcripts;
source-to-hybrid and targeted-compatibility provenance;
negative-control transcripts.
```

One fresh machine must reproduce the exact verification from the archived
input and certificate.  Two fresh primes must be reproduced by an alternate
GB implementation.

## 8. Promotion standard for the decisive claim

### 8.1 Evidence tiers

| tier | required evidence | allowed language |
|---|---|---|
| M1: screen | authenticated `[1]` at the three banked primes | "D23 empty at three primes" |
| M2: exceptional modular package | M1 + 16 preselected fresh reconstruction/replay primes + three untouched holdouts, both-embedding/unspecialized checks, stable traces, two alternate-engine reproductions, all controls | "exceptionally strong modular evidence for D23 emptiness" |
| C0: char-0 computational theorem | M2 + exact canonical cofactor/DAG ending in a nonzero constant + two exact verifiers + source provenance | "the canonical D23 core is empty in characteristic zero" |
| C1: campaign promotion | C0 + hostile audit of emitter equivalence and the D23-to-residue-A implication | "residue-A dies at the depth-23 window tier" |
| C2: program claim | C1 + independent audit of every remaining on-axis td=6 branch/cover implication | the decisive td=6 closure language |

The fresh-prime count is intentionally far above the usual three.  It is still
not a theorem without C0.

### 8.2 What explicitly does not meet the bar

- 3, 16, 100, or a million ordinary-size mod-p `[1]` results alone;
- mod-p `[1]` plus a char-0 timeout or incomplete rational GB;
- msolve char-0 `[1]` plus same-engine prime agreement but no checked
  membership representation;
- one `sqrt(3)` embedding with no exact tau/conjugation bridge;
- a 397-polynomial D21 GB with no provenance;
- random evaluations of a proposed cofactor identity;
- a fixed-radical fiber certificate with no exhaustive global cover;
- an exact certificate for the 77 emitted hybrid generators without exact
  source-to-hybrid equivalence/provenance for the source-level D23 identities;
- an exact D23 certificate with the final residue-A/td=6 scope implication
  left unaudited.

The effective spreading-out prime-product route cannot repair any of these:
the bounds in `CERT-UPGRADE.md:124-175` are astronomically beyond the engine's
prime range.

## 9. Pre-registered decision tree

### D0. The trigger fails

- **Any authenticated modular NONEMPTY:** stop this all-EMPTY-triggered
  workflow, but do not infer characteristic-zero nonemptiness.  Extract and
  raw-row-verify a point over its actual finite extension, test saturation and
  smoothness, and attempt a Hensel lift.  Only a successful p-adic lift (or an
  exact characteristic-zero point) proves characteristic-zero propriety.  If
  a singular point does not lift, keep char-0 emptiness open and treat the
  prime as potentially exceptional.
- **Mixed verdicts or trace shapes:** quarantine; distinguish exceptional
  reduction, embedding mismatch, bad denominators/pivots, and emitter drift
  before further computation.
- **Timeouts only:** no verdict.  Do not enter this char-0 tree.

### D1. All three banked main lanes are EMPTY

Authenticate `rc=0`, nonzero complete outputs, full reduced-GB headers,
variable/field/order data, basis length one, SHA-256, and controls.  Freeze the
current artifacts.  Do not silently re-emit them after seeing the result.

### D2. Freeze and validate the canonical char-0 object

Build the K-native and preferred Q-flat emissions, reduce them at banked and
fresh primes, reconcile all row scalars, resolve the 82-vs-80 fiber census,
and pass every gate in section 1.  Any failure returns to emitter audit; no GB
result survives a wrong-object failure.

### D3. Recover the missing telemetry

Run the adaptive sequential replays in section 4.  Classify S87, Q88, and T
separately from the worst authenticated good-prime trajectory.  Never vote
away an outlier; divergent trajectories return to bad-prime/emitter audit.
In parallel, prove the exact `A=C diag(u)` rank-four factorization and emit the
six compatibility rows with provenance.

### D4. Prime/support discovery

Run the first three fresh primes and both embedding checks.  Mine a stable
minimal row core and try modular cofactor extraction on the targeted ideal.

- unstable verdict/LM/trace: return to prime/emitter audit;
- stable small canonical cofactors: D5-flat;
- large/unstable cofactors but small terminal ancestry: D5-DAG;
- large ancestry: D5-targeted;
- a Q88-green/yellow exact projection may additionally launch D6 in
  parallel.

### D5-flat. Cofactor CRT

Freeze support and RREF pivots, stream the 16 reconstruction primes, keep
primes 17--19 outside the CRT as untouched holdouts, extend the working set in
deterministic batches if necessary, and run the two exact verifiers.  A valid
identity goes to D7.  Failure to reconstruct after support growth beyond 2x
or two fixed-support prime failures switches to D5-DAG.

### D5-DAG. Trace provenance

Prune to terminal ancestry, replay at fresh primes, lift scalar nodes, and
verify every node exactly.  If the DAG exceeds the 20-GiB / `1e7`-scalar pilot
gate or trace pivots are not stable, switch to D5-targeted.

### D5-targeted. Six compatibilities over D21

Use the exact left kernel, per-step pivot substitution, unspecialized D21
normal forms, and minimal-core mining in section 2.  Try Singular modular
`liftstd`, then the observed-support Macaulay system.  Retain a circuit
certificate if expansion is large.  Exact success goes to D7.

### D6. Bounded full char-0 reconnaissance

- Q88 green: 256--512 GiB / 2 hours;
- Q88 yellow with provenance-capable exact-pilot projection: Box02 / 24 hours,
  1.2-TiB planning and 70%-RAM hard stop;
- Q88 red: skip.

A completed bare `[1]` is banked as strong evidence and as a trace source, but
certification continues through D5.  A partial run only updates the estimator.

### D7. Independent verification

Verify the exact integer/K identity, source provenance, three untouched
holdouts, negative controls, and clean-machine replay.  Any mismatch returns
to the route that produced the bad node/cofactor; it is not patched by more
primes.

### D8. Promotion gauntlet

Conduct two separate hostile reviews:

1. computation: canonical emission, hybrid equivalence, rank-four reduction,
   certificate and independent replay;
2. mathematics/scope: why emptiness of this saturated, B-frozen, no-log D23
   core kills exactly the claimed residue-A locus and what remains before the
   on-axis td=6 statement.

Only after both pass may C1/C2 language be used.

### D9. Fixed-budget failure

If the targeted modular lift, pruned DAG, and the single Box02 lane yield no
exact identity within their registered gates, stop and record:

```text
D23 is EMPTY at the listed primes with the archived robustness package;
characteristic-zero certification remains open.
```

Do not promote residue-A death or td=6 closure.  The next scientific move is a
human lemma from the stable minimal core or a genuinely new provenance-capable
engine, not an unpriced memory escalation.

## 10. Next-day execution order and budget

Assuming D1 triggers:

| order | work | cap / decision product |
|---:|---|---|
| 1 | authenticate and hash banked outputs | 1 hour; stop on any hygiene failure |
| 2 | canonical K/Q-flat emission + exact row gates + fiber census repair | 2--4 engineering hours |
| 3 | adaptive S87, Q88, and targeted telemetry | run one presentation/prime first; a 30-min, 128-GiB, or 20M-column crossing makes that class red (and vetoes D6 for Q88); only then run two further stable traces |
| 4 | exact rank-four factorization and six-compatibility emitter | 2--6 engineering hours; no heavy GB needed |
| 5 | three-prime targeted cofactor/minimal-core pilot | Box03 only after pinning/hash-verifying msolve 0.10.1 and the extraction engine; otherwise screening-only; 300-GiB planning ceiling, 2 h first |
| 6 | trace/DAG or fixed-support 16-use-prime + 3-holdout wave | cost from measured apply time and support; no blind parallel fanout |
| 7 | direct char-0 reconnaissance, only if Q88 is green/yellow | 512 GiB/2 h, then at most one Box02 lane: 1.2-TiB planning, 70%-RAM hard stop, 24 h (about $312) |
| 8 | exact verification and clean-machine replay | scratch >= max(3x serialized package, 1.5x projected verifier frontier/spill); no promotion until both finish |

The prime wave and full char-0 run are not prerequisites for beginning the
rank-four/targeted work.  That exact reduction is the highest-value first move
after artifact authentication.

## 11. Success criteria in one line

The campaign succeeds only when an independently replayable exact artifact
checks

```text
nonzero integer = exact combination of the 77 frozen hybrid D23 generators
                  and s^2-3,
```

and the separate scope review confirms the promised implication.  Everything
before that is graded evidence, however compelling.
