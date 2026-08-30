# K00 V20R2 `R4-00`: evidence-grade AWS deciders for the two open base cells, built, launched, and first-decided

Author: Fable 5 (primary research / packet-builder lane)
Date: 2026-08-29 UTC
Basis: commit `792eecb1` at lane start, `0f7ee003be45ee40d51d4048897cdacf63821172` at report time; all
three pinned inputs are hash-verified, so the moving tree does not touch this
lane's custody.
Lane tag (registered by this report): `K00-R4-00-BASE-DECIDE-AWS-20260829`
Lifecycle: `PROVISIONAL_PRODUCER_RESULT / DIFFERENT-MODEL REVIEW REQUIRED`

Pinned inputs (verified byte-exact at run start and again before every
derived artifact was emitted):

```text
0ffc4f741eb2b6a8257dd90c47f194f950752150f57468d81a7779406ab60ed3
  xmodel/k00-r4-00-entry-solve-fable5-20260829.md          (sealed producer report; CROSS-CHECK ONLY)
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py
```

## 0. Result

1. Both decider ideals were rebuilt literally from the frozen 569 tails and
   the frozen compiler conventions in a new clean-room dyadic-exact pipeline
   (Section 2); no formula was copied from the producer report.  Every
   displayed producer identity my pipeline touched (I1@14, I2@14, D·A8,
   D·B8, c31@16, row4@16, the 21/19/18 grade-18 term counts, the c21'
   factorization `(5kappa/589824)(F2-8*eps*i*t*F1)`, and the serialized
   INERT/VARS lists) is CONFIRMED byte-for-byte against the rebuild.
2. One defect was found in the producer's Section-9 `R1` job sketch
   (five conditions on four unknowns via concurrency minors and a pinned
   point).  That encoding is not everywhere equivalent to the closed cell
   content; the shipped decider uses the repaired existential system
   (Section 4).  The producer's serialized Section-7 packet itself is not
   defective.
3. Deterministic packets, fail-closed runners, and an independent
   certificate verifier are checked in; the packet self-check
   (`R400_BASE_DECIDE_SELFCHECK=PASS`) gates emission on ~90 structural
   identities, three mutation kills, and exact literal-row completeness
   controls on both cells and both `eps` branches (Section 6).
4. Both jobs were launched on audited campaign host r6a after a direct
   pre-launch audit (Section 7).  First results (Section 8):
   - `R4-00-R2-BASE-DECIDE` (exact, Singular 4.3.2, char 0): the saturated
     base ideal is **NOT the unit ideal**; `dim = 1` in the weighted ring,
     i.e. finitely many weighted rays, each lying entirely inside the
     constructible cell.  The `kappa=1` slice with the opens enforced by a
     Rabinowitsch factor is zero-dimensional of degree 25 (chart `s`) /
     20 (chart `t`), with **no rational point** (inert-prime proof,
     Section 8) — so the producer's numeric positive-dimensionality
     reading is refuted while its nonemptiness indication is confirmed.
     **The CELL-R2 base locus is NONEMPTY over `Qbar`** (engine-trust
     tier, cross-corroborated by three modular primes and by the
     producer's independent numeric Newton).
   - `R4-00-R1-BASE-DECIDE` (exact, Singular 4.3.2, `Q(i)`, both branches):
     the saturated ideal is likewise **NOT the unit ideal**, `dim = 1`.
     **The CELL-R1 base locus is NONEMPTY over `Qbar`** on both branches.
     This *refutes at base level* the producer's numeric-empty indication
     (typed there as UNREVIEWED guide only, so no promoted claim falls).
   - 18/18 modular screening shards (three primes including `2^31-19`, two
     charts, all cells/branches) return non-unit Groebner bases:
     independent screening-tier corroboration of both nonemptiness
     verdicts.
   - Primary decompositions of both saturated ideals are running on r6a at
     report time (PIDs in Section 7); harvest instructions in Section 9.
5. Consequence, stated exactly: neither cell dies at the base stage, so
   `R4-00` is not closed by the base deciders.  Whether the surviving rays
   extend to grade-19 jets of `R4-00` (i.e. whether the sole remaining
   valuation-four residual is alive at grade 19) is now decided by the
   sharply specified STAGE-2 completion computation of Section 9, for which
   this packet already contains all raw material and a rational-point
   executor.  No `R4-00` nonemptiness, arc, map, attainment, or JC2 claim
   is made (Section 10).

## 1. Inputs, custody, firewall

Only the three pinned files above were consumed.  The producer report was
used exclusively as a cross-check target; every generator was derived from
`tails.json` under the conventions read out of the frozen compiler
(10-slot tails `C0..C6,k10,k6,k2`, weights `8..2,2,6,10`, row weight
`12+ell`, load shifts 2/6/10, normalized map `C0=(1+d0)/256, C1=d1,
C2=(1+d2)/16, C3=d3, C4=(3+d4)/8, C5=d5, C6=1`, target rows `-mu2@14`,
`-mu4@16`, `-mu6@18`, `-(1/4)Jdet@19`, truncation `Lambda^20`,
boundary zeros `k6_0=k2_0=mu2_0=mu4_0=mu6_0=0`).  No `jc2-lean` path was
listed, read, built, or touched; all git use was scoped away from it.
Local Mac use was held to editing, hashing, orchestration, and
seconds-scale checks: one early all-`Fraction` prototype exceeded its local
budget, was killed at 10 minutes / 31 MB, and was replaced by the dyadic
engine whose full local self-check runs in 3.0 s / 25 MB; all CAS ran on
AWS only.

## 2. Clean-room rebuild and structural verification

`gen_r4_00_base_packets.py` expands the seven rows twice, with dyadic
integer coefficients `(num, e) = num/2^e` (every frozen denominator is a
power of two, asserted at load): a generic build truncated at `Lambda^16`
with `Az,Bz,A7,B7` symbolic, and a solved-stratum build to `Lambda^20`
with the forced zeros substituted at source; the two builds are checked
equal on all common grades after substitution.  The stratum is the literal
`R4-00` packet: `d = L^4 ell(s,t) + L^5 ell(s1,t1) + L^6 z +
sum_{7<=m<=13} L^m d_m` in adapted coordinates
`cone(a,b,u,v)+(B,0,0,0,0,A)`, `ell(s,t)=cone(t/8,s,0,0)`, loads
`k10 = kappa + sum k10_j L^j` etc., all remaining columns symbolic
*including* `d[14..19]`, `k10_{6..17}`, `k6_{6..13}`, `k2_{6..9}` so that
absence claims are verified, not assumed.

Checks enforced before any emission (each is an exact polynomial identity
or an exact occurrence statement of the rebuilt rows; failure aborts):

- weighted homogeneity of every window entry (weight `n` at grade `n`);
- grades 0..11 of all seven rows vanish identically on the stratum;
- grade 12 equals the entry system: the three combo certificates
  `(3/16384)AzBz`, `-(3/131072)AzBz`, `-(3/2097152)AzBz`, the pure
  `row4 = (3/524288)(Bz^2-64Az^2)`, `row6 = 0`, variable set
  `{s,t,kappa,uz,vz,Az,Bz}` only, and membership of all rows in `(Az,Bz)`;
- the single-matrix `T`-ladder at every grade 13..19: top jet
  `(A_{n-6},B_{n-6})` enters row 1 as `(1/2048)(p A + q B)`,
  row 2 as `(1/2048)(-4q A + (p/16) B)`, rows 3/5/7 as `-1/8, -1/128,
  -1/1024` times row 1, rows 4/6 not at all, with
  `p = 6uz+5*kappa*s`, `q = -6vz+5*kappa*t`; no newer jet and no top-jet
  cone coordinate occurs anywhere at that grade;
- grade 13 is exactly `T(A7,B7)` (all rests vanish); the grade-14 combos
  are exactly the pure `(A7,B7)` pair with no inhomogeneity;
- `I1@14, I2@14` are pure base and match the producer's display;
- grade-15 combos vanish identically after `A7=B7=0`;
- grade-16: `c31@16`, `row4@16` closed in `{base, A8, B8}`, the
  `c51 = -c31/8`, `c71 = -c31/128` proportionalities, `row6@16 = 0`, and
  byte-match with the producer's displays;
- grade-17: proportionalities continue, `row6@17=0`, `row4@17` defines
  `mu4_1` (coefficient exactly `-1`);
- grade-18: `row6@18` (21 terms), `D51@18` (19 terms), `D71@18` (18
  terms) closed in `{s,t,uz,vz,kappa,A8,B8}`; `row4@18` defines `mu4_2`;
- grade-19: `row4@19 -> mu4_3`, `row6@19 -> mu6_1`, `D71@19` carries
  `-Jdet_0/4`; each target occurs at exactly one site in the whole window
  with constant coefficient (`-1`, or `-1/4` for `Jdet_0`);
- occurrence audit: the full window (grades 8..19) uses no column beyond
  the serialized packet VARS.  The absent set is exactly
  `a10..a13, b10..b13, u12,v12,u13,v13, k10_6..17, k6_6..13, k2_6..9,
  d14..d19 (all 36 components)` — confirming the producer's INERT list
  and extending the `d[14],d[15]` absence claim to `d[16..19]`.

The rank-2 solve identity `(A8,B8) = -(2048/D)(p I1 - 16q I2, 64q I1 +
16p I2)`, `D = p^2+64q^2`, is verified symbolically, and the shifted
`(p,q)`-display of `D*A8`, `D*B8` in the producer report is reproduced
term-exactly.

## 3. The two deciders and their exact semantics

**`R4-00-R2-BASE-DECIDE`.** Ring `Q[s,t,uz,vz,kappa]`, weighted order
`wp(4,4,6,6,2)`.  Generators `X1..X5` = the `D^2`-cleared substitutions of
the five closed forms `c31@16, row4@16, row6@18, D51@18, D71@18` under the
unique rank-2 solve (98/102/112/105/105 terms, integer-cleared by recorded
positive-rational unit scales; loci unchanged).  Cell = `V(X1..X5)` with
opens `D != 0`, `kappa != 0`, `(s,t) != (0,0)`.  The driver saturates by
the principal ideal `(D*kappa)` and then by the ideal `(s,t)` using an
explicit version-independent quotient chain (`satur`, Section 7), then:

- unit result => emptiness route: it searches minimal `N`, `a` with
  `(D*kappa)^a s^N` and `(D*kappa)^a t^N` in `(X1..X5)`, computes `lift`
  cofactors, re-verifies the identities in-engine, and writes them out.
  The checked-in `verify_unit_certificate.py` then re-verifies the two
  identities by pure stdlib `Fraction` expansion — an engine-independent
  exact rational certificate, the theorem-tier bar of the task.  A
  characteristic-zero `[1]` from any Groebner engine is never consumed as
  a verdict anywhere in this lane.
- non-unit result => `dim`, `primdecGTZ`, and per-component membership
  flags for `D, kappa, s, t` are written; the banner says explicitly
  `SURVIVING_BASE_COMPONENTS_STAGE2_REQUIRED`.

Soundness direction used for a kill: `X1..X5` are exact consequences of
the literal window equations on the cell (linear combinations of imposed
rows evaluated through the unique solves, `D^2`-cleared on `D != 0`), so
base emptiness implies cell emptiness over every characteristic-zero
field.  A non-unit result is typed as surviving *base* components only.

**`R4-00-R1-BASE-DECIDE` (branches `eps = +1, -1`).** Ring
`Q(ii)[s,t,kappa,q,A8,B8]`, `minpoly = ii^2+1`, order
`wp(4,4,2,6,8,8)`; branch substitution `uz = (8*eps*ii*q - 5*kappa*s)/6`,
`vz = (5*kappa*t - q)/6`.  Generators (7): `c21'@14`, the `row1@14` line,
the two conics `c31@16`, `row4@16`, and the raw grade-18 closed forms
`row6@18`, `D51@18`, `D71@18` (the producer's affine lines `L18,L51,L71`
are unimodular combinations of these with the conics — same ideal).
Cell = `V(gens)` with `q != 0`, `kappa != 0`, `(s,t) != (0,0)`; same
saturation chain, same certificate/emptiness machinery with
`(q*kappa)^a`, same non-unit typing.  The `eps=-1` system is verified to
be the exact `i -> -i` conjugate of `eps=+1`; both are still run
independently.

## 4. Defect found and repair (producer Section-9 R1 sketch)

The producer's cheapest-successor sketch for R1 poses five conditions on
the four base unknowns `(s,t,kappa,q)`: `c21'@14`, two concurrency minors
`M1 = det3(row1,L18,L51)`, `M2 = det3(row1,L18,L71)`, and "the two conic
values at the pinned point" `row1 ∩ L18`.  Defect: this encoding
presupposes that the lines `row1@14` and `L18` are transverse.  On the
locus where they are parallel or coincident (or `L18` degenerates), the
minors vanish without four-line concurrency and the pinned point is
undefined, so the five-condition system is neither clearly necessary nor
clearly sufficient there.  Smallest clean repair, shipped as the decider:
keep the plane coordinates `(A8,B8)` as ring variables and impose the
seven closed forms existentially; this agrees with the five-condition
system on the transverse open and is correct everywhere.  The producer's
own Section-7 serialized packet (full jet system) is unaffected; only the
§9 base-decide sketch needed the repair.  This defect is material in
hindsight: the producer's numeric probes of the two *square* subsystems
of the five-condition encoding found no full-system points, while the
repaired existential decider finds surviving rays (Section 8).

## 5. Checked-in artifacts (all under
`cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/r4_00_base_decide_fable5_20260829/`)

```text
0aa15f29172e36a4d7a673f3235206b45e28625218e04daa3afb9b8d3825c40f  gen_r4_00_base_packets.py
2e5ca2c1ce21d6ef44bbe709c5769ca8ddbb82986ffee017d8884520a07e5df1  run_r4_00_base_decide.sh
ac616798fbe5938dbc40a8d1d68564a508e872a000b8c02a363c9ca2495eccbb  verify_unit_certificate.py
a9637c71f2ac6f35b40511c1ede2fc82a5079e387f632c65d387c5549e300896  stage2_completion_check.py
7f9a9940df73277020eeb42bfe4414fa7ae51b37eb87eca82faf53dff3834b93  packet/MANIFEST.sha256
09269dbc56255260ad9b80610b29dca34f7a861f1cd3cafff09ef979653340eb  packet/R2_GENS.txt
929d5d58ac10fbec422c59ac9d6f7514d0855bafe55ee0410704289339607d32  packet/R1_epsP_GENS.txt
80bb6fbe6fd3ef01d3735f04bb510c43cc6439f7982deecdd28bc781a1c1158a  packet/R1_epsM_GENS.txt
d3292a414ff4b005ac79e5b8fa02f69cc6e5f263dd21ca240642880e23acf835  packet/R4_00_R2_BASE_DECIDE.sing
78308dd90d9a92162782118c2fa345dc2b91ca807f8101bfd66ebc67fb0f5d9d  packet/R4_00_R1_BASE_DECIDE_epsP.sing
185872a609ae30eb417a9c90a38987548d598ea1f0b027a3c5b3d18f71331ccf  packet/R4_00_R1_BASE_DECIDE_epsM.sing
b25d7b4f2b7e43171a5834de621fcc438b68d47caeb6d1e4dcf6bdb8b46ad176  packet/STAGE2_WINDOW_MATERIAL.txt
4f78fb65f28aaef8aea6f0b88220003e0810c9f40489e6e678495c63ee084a24  packet/PROVENANCE.json
```

plus 18 msolve shard inputs `packet/shard_*.ms` (hashes in
`packet/MANIFEST.sha256`, whose own SHA-256 is the packet fingerprint
`7f9a9940...` above).  `PROVENANCE.json` records input hashes, the unit
scale of every generator (constructible loci unchanged — nonzero rational
scalings only), `sqrt(-1) mod p` per shard prime, the window
occurrence/absence census, and every control outcome.
`STAGE2_WINDOW_MATERIAL.txt` serializes, with exact `Q` coefficients, the
raw absorbable rows (`c31@17,18,19`, `D51@19`), the target rows
(`row4@17..19`, `row6@19`, `D71@19`), `I1@14`, `I2@14`, and
`Ahat8 = D*A8`, `Bhat8 = D*B8` — everything a clean machine needs to
reproduce both ideals and run stage 2.  The generator is deterministic:
regenerating reproduces every packet byte.

## 6. Controls

Producer-side controls executed by the generator (all recorded in
`PROVENANCE.json`; any failure blocks emission):

- **Mutations (negative controls).** (a) `+1` on the frozen row-4 tail
  `[0,0,0,0,0,2,5,0,0,0]` (coefficient `-63/1024`) is detected at
  `G4@8..11 != 0`; (b) target-sign flip is detected at the `-mu2_1`
  coefficient check; (c) `k6` load-shift `6 -> 5` is detected by weighted
  homogeneity failure.
- **Literal-row completeness controls (both cells, both branches).** At an
  exact deterministic pseudo-random base point (Gaussian-rational for R1),
  the script solves every solvable window equation literally — rank-2
  `T`-solves resp. rank-1 row-1 solves plus the `mu2` ladder, staged exact
  affine absorption of `c31@17`, `c31@18`, `c31@19`, `D51@19` into
  `(k2_1,k6_1)`, `k2_2`, `k2_3` (stage structure proved by the dependency
  closures; each stage lands exactly), and the target definitions — and
  then verifies that of all 84 literal window equations exactly the
  closed-generator residuals are nonzero and equal the emitted generators'
  values under the declared `D^2` scalings.  This is the direct
  literal-row-substitution independence test of the shipped generators.
- **CAS machinery controls (fail-closed, inside every driver).**  The
  `satur` quotient chain is exercised on a known unit saturation, a known
  non-unit saturation with known value, and `lift` on a known identity,
  before the payload runs.
- **Determinism.** The aborted first AWS run and the second run produced
  bit-identical outputs on all 18 msolve shards.

## 7. Frontier gate, host audit, launch custody

Classical admissibility gate (`ops/frontier_gate.py`), honest scope
`--partial-y-degrees 8 12 --total-unbounded`, tag as registered:
verdict `NOT_CLOSED_BY_THIS_GATE` (GGV/Heitmann gcd-16 inconclusive for
partial-y-only scopes; no closed-frontier claim is made by this lane).

Host: **r6a**, instance `i-02cb2b4a379ffcc64` (r6i.4xlarge, 16 vCPU /
128 GiB), IP `34.229.212.201`.  Direct pre-launch audit at
2026-08-29T22:59:17Z: DMI `Amazon EC2` / `r6i.4xlarge` / asset tag
`i-02cb2b4a379ffcc64`; load 0.00; 122 GiB free; 189 GB disk free; only
system daemons running (no campaign or foreign payloads).  The separate
user formalization instance was neither identified nor touched; box01's
one-core tail-builder was left undisturbed.  Tools: Singular 4.3.2
(4330, 64 bit, Apr 1 2024, Ubuntu noble apt) and msolve 0.6.5
(apt; per fleet ledger 0.6.5 is SCREENING-TIER, which matches the
shards' declared tier; the exact tier for this lane is carried by
Singular char-0 plus the independent certificate verifier, not by
msolve).

Custody chain: packet tarball shipped by scp; `MANIFEST.sha256` verified
remotely (`7f9a9940...`) before both launches.  Remote dir
`/home/ubuntu/r4_00_base_decide/` with `packet/`, `run1_aborted_sat_api/`,
`run2/`.  First launch (23:00Z) aborted: Ubuntu Singular 4.3.2's
`sat` returns a bare ideal (not the historical `(ideal, exponent)` list),
and batch-mode Singular *continues after errors*, so the three jobs
printed `? wrong range` and kept computing garbage; they were killed by
exact validated PIDs, and the scripts were repaired by replacing `sat`
with an explicit stabilized quotient chain `satur` that is itself
exercised by the in-driver controls.  Harvest rule recorded: any `?` line
in a Singular stdout/stderr invalidates that run.  The 18 msolve shards
from the aborted run are retained (`run1_aborted_sat_api/`) and match
run2 bit-for-bit.

Second launch (23:11Z, tag `K00-R4-00-BASE-DECIDE-AWS-20260829`,
`run2/`): wrapper PIDs 22777 (r2), 22778 (r1p), 22779 (r1m), 22780
(msolve loop); Singular payload PIDs 22895 (r2), 22893 (r1p), 22894
(r1m), each under `timeout 43200 /usr/bin/time -v` with stdin closed;
runners record host, DMI identity, UTC, tool versions, argv, input
hashes, resource use, rc, and output hashes into `run2/*.meta` and
`run2/lanes.log`.  Resource snapshot at 23:17Z: three Singular processes
at 99.9% CPU each, < 0.2% memory each, machine otherwise idle
(1 GiB used / 122 GiB free).

## 8. First results (as of 2026-08-29T23:2xZ; evidence tiers explicit)

**Modular screening (SCREENING-TIER, msolve 0.6.5, rc=0 on 18/18):** for
every prime `p in {65521, 1048573, 2147483629}` (all `1 mod 4`, recorded
`sqrt(-1)`), both charts, R2 and both R1 branches: the Rabinowitsch-
extended systems have **non-unit** reduced Groebner bases mod `p`.  No
shard is empty.  This is screening evidence of nonemptiness for both
cells at three independent primes, and it already contradicted the
producer's R1 numeric-empty indication before the exact runs returned.

**Exact characteristic zero (Singular 4.3.2 on r6a; engine-trust tier
pending different-model review; no unit-shortcut hazard because the
results are non-units with explicit dimensions):**

```text
R400R2_SAT1_ITER=10   R400R2_SAT2_ITER=0   R400R2_BASE=NONUNIT_SURVIVOR   R400R2_DIM=1
R400R1_SAT1_ITER=7    R400R1_SAT2_ITER=0   R400R1_BASE=NONUNIT_SURVIVOR   R400R1_DIM=1   (eps=+1)
R400R1_SAT1_ITER=7    R400R1_SAT2_ITER=0   R400R1_BASE=NONUNIT_SURVIVOR   R400R1_DIM=1   (eps=-1)
```

Reading, with the geometry stated exactly: each saturated ideal is
weighted-homogeneous of Krull dimension 1, i.e. its variety is a finite
union of weighted rays through the origin.  Saturation by `D*kappa`
(resp. `q*kappa`) and by `(s,t)` means no component is contained in any
of the excluded loci; since a ray is irreducible and the opens are
homogeneous, **every surviving ray minus the origin lies entirely inside
the constructible cell**.  Hence both base loci are nonempty over `Qbar`.
An independent structure probe (not a packet artifact; inputs
`deh_r2_k1_rab{s,t}.ms` derived from the same generators, retained on the
box and in the partial harvest below): at `kappa=1` with the opens
enforced, msolve char-0 reports the R2 system zero-dimensional of degree
25 (chart `s`) resp. 20 (chart `t`) with exact rational
parametrizations — finitely many algebraic surviving points, matching
`dim = 1` homogeneously.  Desk analysis of the chart-`t` eliminant
(degree 20, exact integer coefficients): it has **no rational roots** —
mod the primes `2147483563` and `2147483543` it has no roots at all,
which excludes any rational root whose denominator avoids both primes,
and the rational-root bound makes a denominator divisible by two fresh
31-bit primes impossible against the leading coefficient
(`~5.97e29 < 2^100` admits at most three 31-bit prime factors, and the
mod-`p` linear factors at split primes are non-persistent).  Hence no
surviving R2 ray is rational; the two persistent conjugate points sit in
a nontrivial extension (mod-`p` degree patterns
`[1,1,3x6] / [1,1,2x9]`), and the exact component fields are exactly
what the running decompositions will pin.  The producer's §8 numeric
reading ("positive-dimensional surviving base component", from a rank-2
Jacobian of the `{X1..X4}` subsystem plus the on-locus `X5=X4/8`
observation) is **refuted**: the surviving base locus is projectively
finite.  Whether the finite points carry non-reduced scheme structure
(which would reconcile the observed Jacobian rank) is settled by the
running primary decomposition.

Primary decompositions (`primdecGTZ`) of all three saturated ideals were
still running at report time (started 23:11Z; 12 h cap; expected
artifacts `run2/R2_COMPONENTS.txt`, `run2/R1_epsP_COMPONENTS.txt`,
`run2/R1_epsM_COMPONENTS.txt` with per-component prime ideals, `dim`,
and `D/kappa/s/t` membership flags).  Because prime components suffice
for stage 2, three supplementary `minAssGTZ` variants were additionally
launched at 23:24Z (scripts `minass_*.sing` derived from the pinned
drivers by a recorded `sed` substitution, hashes
`597e23e0.../b72af19f.../8a5c7e56...`; payload PIDs 26171 (R2), 26173
(eps=+1), 26172 (eps=-1); outputs `run2/*_MINASS.txt`,
`run2/minass_*.stdout`).  Both decomposition families run concurrently;
resource snapshot at 23:28Z: six Singular processes at ~100% CPU each,
load 5.98/16, 120 GiB free.

Partial harvest already checked in beside the packet
(`aws_r6a_run2_partial/`, 44 files): all 18 shard `.gb` outputs and
metas, `lanes.log`, the `deh_r2_k1_rab*` probe inputs/outputs
(`deh_r2_k1_rabs.ms` = `59d35e23...`, `deh_r2_k1_rabs.sols` =
`2a5c2866...`), and the three decider metas as of the pull.

## 9. Exactly what closes each cell now

The base-stage answer is nonempty for both cells, so closure of `R4-00`
(either way) now runs through STAGE 2 on the finitely many surviving
rays.  For each prime component `P` from the decompositions:

1. **Absorbability at the ray.**  The four absorbable window conditions
   must be solvable over the residue field of `P`: the staged absorber
   matrices of Section 6 must be nonsingular mod `P` (their entries are
   polynomials in the packet's `STAGE2_WINDOW_MATERIAL.txt` data).  If a
   stage is singular for every admissible absorber choice, that grade's
   condition becomes a fresh closed constraint on the ray and the
   component dies or degenerates; this must be decided, not assumed.
2. **Grade-19 survival open.**  With absorption solved, `Jdet_0` is the
   defined value `4*(D71@19 nontarget part)` as a function of the free
   window coordinates over the ray.  The component contributes `R4-00`
   points iff this function is not identically zero on the absorbed
   family, i.e. iff its numerator polynomial is nonzero mod `P`.  A
   single exact nonzero evaluation at a rational point of the ray is a
   witness; identical vanishing kills the component at grade 19.
3. For any rational (or Gaussian-rational) ray point, the checked-in
   `stage2_completion_check.py` executes both steps end-to-end with exact
   arithmetic and, on success, prints an explicit grade-19 jet witness
   status (`GRADE19_JET_WITNESS_WITH_JDET_NONZERO`), verifying every one
   of the 84 literal window equations at the completed point.  For
   irreducible components of higher degree, the same two questions are
   normal-form computations against `std(P)` in Singular over the
   component (a bounded follow-up job on the same packet; the symbolic
   cascade numerators can be produced by the same generator module).

A future *emptiness* claim for either cell (there is none now) would
require the lift-certificate route of Section 3, independently reverified
by `verify_unit_certificate.py`; modular `[1]` shards or a char-0-header
`[1]` would not suffice.

Harvest note for the coordinator: when `run2/*.meta` gain their `rc=` and
artifact lines (and `lanes.log` gains the three `MINASS_* rc=` lines),
pull `run2/` beside the packet as `aws_r6a_run2/` (metas, stdouts,
stderrs, `*_COMPONENTS.txt`, `*_MINASS.txt`, shard `.gb`s), reject any
Singular output containing a `?` line, and hand the component list to
stage 2.  r6a should not be stopped before that harvest; nothing else on
it belongs to this lane.

## 10. Scope, nonclaims, and review demand

Field-valued, reduced, finite-jet statements about the literal normalized
V20R2 `R4-00` packet only.  Base-locus nonemptiness over `Qbar` is not
`R4-00` nonemptiness: stage 2 (absorbability at the rays plus the
`Jdet_0 != 0` survival open) remains undecided, and formal jets are not
arcs, germs, maps, or counterexamples; nothing here touches ramified
`e>1` sources, other supports/load faces, attainment, `max12`, or JC2.
The exact Singular results are single-engine and carry engine trust until
a different model replays them (the packet makes that replay a
single-command task per job); the modular shards are screening-tier
forever; the producer-report confirmations in Section 2 are exact
identities of the rebuilt rows.  This lane is a producer; its own
literal-row controls are not hostile review.  Requested review order:
(i) the two decider semantics arguments (Sections 3–4), (ii) the
generator's structural checks against an independent rebuild, (iii) the
Singular replays, (iv) stage-2 design before any launch consumes it.

No canonical ledger, no existing artifact, and no `jc2-lean` content was
modified; this report and the Section-5 lane directory are the only
repository writes.

<!-- BODY-END -->
