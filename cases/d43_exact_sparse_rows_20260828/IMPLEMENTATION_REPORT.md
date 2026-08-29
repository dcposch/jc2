# D43 exact support-specialized row compiler: implementation report

**Status:** review-frozen and deliberately AWS-unregistered.  No D43
checkpoint was unpickled locally, no real D43 jet was built locally, and no
AWS job was launched.

## Outcome

`selected_rows.py` implements two exact paths:

1. The primary source-first path reconstructs the exact 348-coordinate D43
   registry, pins its literal 326-coordinate complement, retains exactly the
   common 22-coordinate support, builds both pure-y source jets including all
   fixed B-orbit factors, and computes only requested canonical row
   components by complementary `(eta,slot)` lookup.
2. A dormant full-checkpoint path verifies content hashes before unpickling,
   reconstructs the same registry, specializes the final cumulative f/g jets
   to the support, and uses the same selected-component engine.  It is
   intentionally blocked because no final GB21 g checkpoint exists and the
   observed checkpoint producer uses a different `r1_experiment.py` hash from
   the current consumer.

The frozen registry has 348 variables and SHA-256
`b3fce1ef76e01c4698b97f7e4cc3562f4da3cd022b301ddde15b1ae086298ce6`.
The 22-support digest is
`6d050cb75c561305e5676e57f987322cf71fce38e56766644c3250be4af2c970`.
The 184-target registry digest is
`25603a9e25d5926b0617ada9af61e9ef408977587abb29074d6d87c544825651`.

## Corrected box01 checkpoint state

A read-only metadata audit found seven, not nine, cumulative orbit
checkpoints.  The last completed g checkpoint is

```text
jet_g_03_G0p2.pkl
337,919,305 bytes
sha256 782f99c0282bcd6eec50e131591e1cac8e6ad3cf6f5705a09d206c0f42cb3fbc
```

`jet_g_04_GB42.pkl` and `jet_g_05_GB21.pkl` do not exist.  The log has no
`jets: ... assembling rows` marker, so the long-running process has not
entered `directionb_strike.jrows`; it is still before the GB42 checkpoint.
The final available f checkpoint is

```text
jet_f_02_B.pkl
29,261,066 bytes
sha256 102500c71d97eda78761c0f450d00c033edf63e42c487c63e559de869fdb08a7
```

The dormant path records these facts and cannot mistake G0p2 for final g.

## Exact source specialization

The retained source names are

```text
tf1_47 tf1_52 tf1_57 tf1_62 tf1_67 tf1_72
tf2_47 tf2_52 tf2_57 tf2_62 tf2_67 tf2_72
tg1_47 tg1_52 tg1_57
tg2_47 tg2_52 tg2_57
tg01_52 tg01_62 tg02_52 tg02_62
```

The reconstruction asserts that these and only these registry variables have
state `None`; every `uf`, `vf`, B-tail, other P-tail, and other G-tail is the
exact zero `R_ext` element before orbit multiplication.  In particular all
six PIN42 variables

```text
tf1_74 tf2_74 tg1_74 tg2_74 tg01_74 tg02_74
```

are pinned.

Pinning B-tail coordinates is not deletion of the B orbits.  The producer
asserts exactly

```text
B.series    = {12: eta_B}
GB42.series = {12: eta_B}
GB21.series = {12: eta_B},
```

with orbit sizes 42, 42, and 21.  Thus the fixed B factors remain in the f/g
source products.

Both committed floor-passing modular certificates were checked by name.  At
each prime alpha and beta vanish, every graph complement coordinate vanishes,
and the nonzero coordinates map to exactly the frozen 22-source support.

## Selected component and digest contracts

For target `(n,s)`, the compiler evaluates only

```text
sum_(na+nb=n,sa+sb=s) A[na,sa] Gamma_eta[nb,sb]
- sum_(na+nb=n,sa+sb=s) Phi_eta[na,sa] B[nb,sb].
```

It never materializes either unrestricted `jmul`.  The inhomogeneous `+42`
is appended exactly at `(0,20)`.  A synthetic exact-ring fixture compares the
selected component with `directionb_strike.jrows` and passes.

Every semantic digest is computed from sorted target pairs, sorted source
variable names, sorted eight-exponent `R_ext` keys, and normalized numerator /
denominator pairs for both `K3` coefficients.  Pickle bytes have a separate
content hash; pickle insertion order is never treated as mathematical
identity.  An insertion-order mutation test produces identical semantic
digests.

The band-20 pilot emits its ten targets and requires exact semantic equality
with the independently committed D21 source bank after the identical literal
pin specialization and `+42` addition.  This is equality in `R_ext`, not a
two-prime comparison.  The real equality check is an AWS pilot gate; only its
lightweight expected-row construction was exercised locally.

All checkpoint, shard, receipt, and merge writes are temporary-file + fsync +
atomic-rename operations.  Every shard carries a canonical custody digest of
its input kind and complete checkpoint receipt.  The future merge accepts
exactly 19 disjoint band receipts, requires identical input custody, and
proves exact coverage of the frozen 184-target set; duplicate, missing, and
extra targets are fatal.

## Three distinct claim tiers

### Tier 1: exact row emitter

A successful band-20 pilot, and later a successful 184-row fanout, establish
only that the requested pure-y source rows were emitted exactly on the
registered support.  W1 and W2 remain free polynomial coordinates in
`R_ext`.  No solution and no nonemptiness statement follows from emission.

No standalone `E`, `HM`, `s1F`, E5, or E6 row belongs in the row emitter.
The radical reductions and fixed template constants already present in
`R_ext` are retained, and the output is the pristine J-row object.

### Tier 2: relaxed finite 184-J scheme

Solving the 184 emitted equations, with the two chart equations
`Wi*uWi-1` if the UU chart is claimed, would give a characteristic-zero point
of the finite relaxed J-row scheme on this source support.  It would bypass
the banked NF traces.  It would not show that the point satisfies every
upstream template tie.

On reduced terminal strata the J rows may eliminate to

```text
E = (9+5*r3)*A1*W1^4 + (9-5*r3)*A2*W2^4 = 0.
```

If such an equality is derived from the emitted rows it may be recorded as a
consequence.  It must not be inserted as an independent shortcut, and it is
not a replacement for the individual E5 quartics.

### Tier 3: intended template-conform locus

Promotion from a relaxed finite J point to the intended residue-A template
locus requires a mechanically explicit bridge.  At minimum it must account
for:

* the two individual exact E5 equations pinning `W1^4` and `W2^4`, with their
  correct `HM` normalization;
* W-unit/chart conditions;
* the applicable E6 transport/cube tie and the required nonzero `HM/s1F`
  scale conditions if extension to the upstream/deeper tower is claimed; or
* a proved elimination-equivalent set of equations that retains precisely
  those conditions.

On the intended E5 locus, relation E is an exact consistency identity: the
two E5 substitutions make it vanish.  Therefore E is necessary as a reduced
J-core compatibility but is insufficient as the template bridge.

`HM` and `s1F` are not coordinates of the finite pure-y Gm D43 emitter, so
their absence is correct at Tier 1.  Their absence is not evidence that E5/E6
extendability holds at Tier 3.  The current direct route must stop at Tier 2
until the explicit E5/E6/unit bridge is built or elimination-equivalence is
proved.

No tier here proves NF/source presentation equivalence, an all-depth inverse
limit, a Keller map, or a JC2 counterexample.

## AWS custody

The review manifest is deliberately unregistered and all compute entry points
reject it.  After review, create a fresh sealed manifest for an idle isolated
host; box02 is preferred if its source packet can be copied immutably.  The
operational wrapper requires:

* nonempty, exactly matching tag, hostname, product, instance, CPU count, and
  runtime registration;
* Linux and Amazon EC2;
* zero configured swap before and after each stage;
* at least 512 GiB available RAM and 100 GiB disk;
* source hashes before compute;
* no competing heavy algebra process;
* `timeout`, `prlimit`, `taskset`, `nice`, `/usr/bin/time -v`, and terminal
  markers.

The review manifest authorizes band 20 only.  It rejects every other band and
the 184-row merge.  Fanout requires a new post-pilot manifest containing the
reviewed pilot receipt hash.

## Local validation

The light suite covers registry/target counts, exact pin support at both
primes, fixed B factors, selected-vs-full component equality, insertion-order
independence, PIN42/sentinel rejection, exact D21 expected-row construction,
pre-unpickle hash checks, inert full-checkpoint and AWS lanes, atomic writes,
and duplicate/missing 184-cover controls.

No solve is authorized by this packet.
