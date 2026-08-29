# Hostile review: D43 pristine-source high-order Hensel packet

Date: 2026-08-28  
Reviewer: independent GPT-5.6/Sol hostile lane  
Verdict: **REPAIR — mathematical core passes; AWS launch is blocked**

## Decision

The finite-source mathematics in the packet is sound under its declared
scope.  I independently reproduced the committed `p^2` point, checked the
full `184 x 182` Jacobian against the exact evaluator, checked the eight
deleted nominal coordinates as exact value-side null directions, and checked
the band-42 `alpha,beta` law against a separately assembled sparse full
operator over `Z/p^2`.

The packet is nevertheless **not launch-ready**.  There are two independent
launch blockers and one machine-readable scope defect.

1. Resume validation does not enforce the registered deterministic branch or
   replay its digit history.  A different valid `p^2` point obtained by adding
   a nonzero tangent-kernel digit is accepted while the state retains the old
   deterministic history and old point hash.
2. No route-specific AWS wrapper exists.  The command in the preregistration
   can run directly on macOS and does not enforce Linux/Amazon-EC2 identity, a
   lane tag, the sealed input hashes, the 1200-second timeout, the 2 GiB RSS
   cap, or zero swap.  This violates `ops/FLEET.md` for every `p^3+` run.
3. The runner's `FORBIDDEN_CLAIMS` omits the preregistered
   `parked/source presentation equivalence` prohibition and does not make the
   documented finite-versus-indefinite/formal-smoothness boundary explicit.

No wrong mathematical result has followed from these defects: no `p^3+` run
or AWS result exists, and the independently reproduced `p^2` evidence is
valid.  The defects concern custody, branch identity, launch enforcement, and
scope serialization.  They require repair before an AWS pilot.

## 1. Inputs reviewed

The sealed input checks passed before review:

```text
5ba4b9115f7807c04d8c41b68e22b3f039a51396a848e5bda8d1205bb9013053  cases/d43_source_high_hensel.py
268eb6f6185c4040be8b82c2f148c26737e42edc2490634ae8fff9adb75ed5ee  cases/test_d43_source_high_hensel.py
062a7e4a5390a353754a9b83d95691678f7247f549d9ea56c88eb0581d945c01  cases/d43_source_high_hensel_prereg_20260828.json
edb7ccab11924d77db2bc1c9511438c096deb80129e8e3063bd22dc2a4aff324  cases/d43_source_high_hensel_p2_replay_20260828.json
85d59be634f8384317d98c6334360813797afea49ac6bb4a0a91a22fc6f85e4a  xmodel/d43-source-high-hensel-preflight-gpt56-20260828.md
```

Every hash embedded in the preregistration's `inputs` dictionary also matches
the current corresponding file.  Both existing SHA-256 sidecars verify.

## 2. Coordinate census and the eight zero columns: PASS

The nominal registry is exactly

```text
4 * 36 dense tails + 2 * 18 even tails + 8 fixed + alpha,beta = 190.
```

The eight labels

```text
(tf1,39) (tf1,41) (tf2,39) (tf2,41)
(tg1,39) (tg1,41) (tg2,39) (tg2,41)
```

are genuinely absent from this selected source window, not merely absent from
a reconstruction dictionary.  A dense tail at `r=39` or `r=41` occurs at an
odd through-slot.  The selected bands are even and at most 42; the smallest
other odd through-slot is the `W/HW` slot 5.  Thus the first possible even
totals are 44 and 46.  The other-block occurrences of these same levels begin
still later.  Eta differentiation and the theta shifts do not alter the
t-slot.

There are three mutually reinforcing checks:

- all eight columns of the recovered `184 x 190` Jacobian are literally zero;
- the parity/cutoff proof above is exact;
- assigning independent large nonzero values to each deleted coordinate over
  `Z/p^2` leaves all 184 exact row values unchanged.

Deleting them therefore gives exactly 182 effective coordinates for this
finite source system.  This statement is scoped to the declared 184 rows; it
does not identify a total ambient Keller-map moduli space.

## 3. Exact evaluator and the band-42 x side: PASS

The pure-y evaluator uses exact modular sparse arithmetic.  The additional
band-42 value law is

```text
42 * S_M * G_M * (3 alpha - 2 beta) * [eta^a](p^4 p'),
S_M = 7^12/2^6,  G_M = -7^18/2^9.
```

It has the correct support and coefficient.  With
`U_f=1+alpha*t^42` and `U_g=1+beta*t^42`, the exact product identity is

```text
B(U_f Phi,U_g Gamma)
 = U_f U_g B(Phi,Gamma)
   + U_g (theta U_f) Phi Gamma_eta
   - U_f (theta U_g) Phi_eta Gamma.
```

At slot 42, the new terms see only the slot-zero y factors.  Every positive
y slot pushes them above the cutoff and the `alpha*beta` term starts at slot
84.  This gives the displayed linear law at arbitrary moving y points, not
only its tangent at the registered point.

In addition to the packet's mod-p basis and perturbed-y controls, I assembled
the full sparse `U_f/U_g` operator independently over `Z/p^2`, at a point with
four nontrivial y/fixed perturbations and nonzero p-adic `alpha,beta`.  Its 184
rows agreed dictionary-exactly with `source_rows_with_x`.  The resulting row
digest was

```text
be3f6777a644058e8c5e2c16718adeb0cbcc15aa5ced5770cf3c31bf63ce4aa6.
```

## 4. Jacobian and Newton semantics: PASS

I checked every one of the 182 retained Jacobian columns by a directional
finite difference over `Z/p^2`:

```text
(F(x+p e_j)-F(x))/p mod p.
```

All 182 columns equal the frozen Jacobian.  The aggregate digest of the
ordered column digests is

```text
dc819ec4fd75fb6aca5ea76c2e6f58eaaa48d2f8246f4fc9c58e6d74c0028897.
```

This independently covers the eight dynamically patched fixed-coordinate
columns as well as the tail and x-side columns.  In particular, it removes
the float-gradient implementation as a trust point at the registered residue
point.

The Jacobian rank is 129.  Hence the tangent-kernel dimension is
`182-129=53` and the left-cokernel dimension is `184-129=55`.

The Newton order and sign are correct.  If `x_n` solves modulo `p^n`, first
uniquely lifting the coefficient frame to `p^(n+1)` and then setting

```text
b = -F(x_n)/p^n mod p
```

leads to `J delta=b`.  Because both the moving point and the lifted radical
frame reduce to the registered residue data, the derivative modulo p is the
same frozen `J` at every digit.  Applying `x_{n+1}=x_n+p^n delta` and replaying
all rows is the correct final gate.

The RREF implementation is deterministic: columns are scanned in registry
order, the first available pivot row is used, and all free correction digits
are set to zero.  The recorded bottom 55 rows of the row-operation transform
are a valid left-kernel basis.  A nonzero pairing therefore obstructs the
current `p^n` point.  At later digits it does not obstruct alternative earlier
kernel choices, and the runner states this limitation correctly.

## 5. Radical frame: PASS

The lift order is correct: `r3` is lifted before `A1,A2`, whose equations
contain it.  The cyclotomic equation is literal `Phi_42`, and the exact-order
tests at exponents 6, 14, 21, and 42 exclude every proper prime-divisor
quotient of 42.  All five derivatives and all registered source denominators
are required to be units.

The light tests continue the registered frame through `p^4`; the real bounded
replay reproduces the committed `p^2` frame exactly.  Re-deriving
`HW_i=h W_i` after every coordinate update correctly includes both the
coefficient-frame motion and the W-coordinate motion.

## 6. Bounded p2 anchor: PASS

A fresh bounded run through `p^2` completed in 7.8 seconds and reproduced all
material committed quantities:

```text
rank(J)                                      129
left-cokernel dimension                       55
nonzero entries of -F/p                       29
nonzero correction coordinates                24
nonzero cokernel syndrome entries               0
all source rows zero modulo p^2           184/184
correction SHA-256
  e3a15fa66ed6f08e3f1c78eb793226ad750ab67a9216ce3dadbaeae82ad79c26
corrected-point SHA-256
  c8bee81b9e56a32d7695f9905951c7798e6d88a6b9c72725ad08e4bce08530b4
state-payload SHA-256
  ce3a145ea936e597a424da1beb8de97c3972c1e92a0a8ef69a7804f2d0cf2f81
```

Thus the historical `p^2` evidence and the newly reconstructed deterministic
digit agree.  This is finite source evidence only.

## 7. Resume authentication: FAIL, launch blocker

`validate_resume_payload` checks the envelope digest, dependency fingerprint,
residue point, current radical equations, current 184-row congruence, and the
history length.  It does **not** check that:

- the current point is the point selected by the deterministic RREF branch;
- the first digit is the committed `p^2` correction;
- any history record describes the transition that produced the current
  point;
- a recorded obstruction witness is valid;
- the serialized status, scope, branch policy, invariants, and forbidden
  claims equal the registered values.

This is exploitable even without constructing a new nonlinear solution.  I
took the fresh deterministic `p^2` state, formed a nonzero kernel vector using
free column 67 of the RREF, and added `p` times that vector to its coordinates.
The vector has 16 nonzero entries and satisfies `J k=0`, so the modified point
still solves every source row modulo `p^2`.  I deliberately left the old
history and old point hash in place, re-enveloped the payload, and called the
production resume validator.  It accepted the state.

```text
old history coordinate-point hash
  c8bee81b9e56a32d7695f9905951c7798e6d88a6b9c72725ad08e4bce08530b4
actual accepted alternate-point hash
  07c541fd04640a24cc22d0aa2b2d8df613b3a9d0d01f5f9f82644b51644ccc8d
validator result
  RESUME_ACCEPTED_NONDETERMINISTIC_P2_BRANCH
```

The SHA-256 envelope detects accidental byte corruption, but it is not a
semantic branch certificate: anyone or any repair script can recompute it.
Consequently a continued run could no longer be interpreted as the
preregistered zero-free-digit branch.

### Required repair

Use a new state schema and deterministically replay the chain on every resume.
The simplest fail-closed method is to start with the registered residue point,
rerun each Newton digit in order, and compare the complete canonical prefix
with the stored frame, coordinates, and history record.  Equivalently, derive
each base-p digit from the final coordinates and verify it against a fresh
solve at every prefix.  In either implementation:

- the actual first correction, not merely a stored string, must match the
  committed `p^2` anchor;
- every successful and obstructed history record must be recomputed;
- exact allowed status/scope/policy/claim/invariant fields must be checked;
- canonical coordinate/frame ranges should be required;
- valid obstruction states, including the schema's first possible failed
  digit, must resume or terminate coherently.

Add negative tests for an alternate kernel branch, a changed history hash, a
forged obstruction, altered scope/status/claims, and a changed p2 anchor.  The
alternate point above is a compact real-D43 hostile fixture.

## 8. AWS and preregistration enforcement: FAIL, launch blocker

The preregistration describes reasonable resources for this single-threaded
pilot, but description is not enforcement.  Repository search finds no D43
high-Hensel AWS wrapper.  The registered command invokes the Python runner
directly.  The runner has no checks for:

```text
Linux
Amazon EC2 DMI identity
nonempty registered lane tag
sealed manifest and preregistered dependency hashes
1200-second wall timeout
2 GiB RSS cap
zero swap before and during the job
host/Python/NumPy/resource custody ledger
```

Its default command can therefore start the target-16 computation locally,
contrary to the strengthened fleet policy.  The generic
`ops/aws_exact_lane.sh` supplies Linux/EC2/tag checks, but the preregistration
does not invoke it; moreover, its generic timeout is 43200 seconds and it does
not itself implement this packet's RSS or swap gates.

### Required repair

Add a route-specific wrapper (possibly around `ops/aws_exact_lane.sh`) that:

1. verifies all files in the sealed manifest and every hash embedded in the
   preregistration before constructing or resuming a state;
2. requires Linux, Amazon EC2 identity, and a nonempty registered job tag;
3. records hostname, instance identity/type, UTC bounds, exact argv, Python
   and NumPy versions, source archive/manifest hashes, and durable paths;
4. refuses nonzero swap at preflight and monitors process-group RSS and swap;
5. enforces the 1200-second pilot timeout and 2 GiB RSS ceiling, killing the
   whole process group on violation;
6. writes a terminal manifest and records interruption/timeout distinctly
   from mathematical obstruction;
7. invokes target 16 first and permits target 64 only from an authenticated,
   semantically replayed target-16 state.

The runner should also fail closed for `target_exponent > 2` unless the AWS
wrapper exports an authenticated lane marker.  This prevents accidental local
execution even if the wrapper is bypassed.

For stronger crash durability, fsync the containing directory after
`os.replace` and hold an exclusive state-path lock so two supervisors cannot
race on the same checkpoint.

## 9. Forbidden-claim firewall: REPAIR

The prose boundaries are substantially correct, but the machine-readable
lists disagree.  The preregistration forbids
`parked/source presentation equivalence`; the runner's
`FORBIDDEN_CLAIMS` does not.  The prose also correctly says that finite
survival proves neither indefinite solvability nor formal smoothness, but
those boundaries are absent from the state/report list.

Use one canonical list shared by runner, preregistration, report, and tests.
At minimum it should forbid:

```text
assembled 218-row p-adic point
parked/source presentation equivalence
indefinite source solvability or formal smoothness
Z_p point
characteristic-zero point
formal germ
ambient polynomial Keller map
JC2 counterexample
```

This is a serialization/scope defect, not evidence that the current prose
made any forbidden inference.

## 10. Light checks run

No `p^3+`, heavy CAS, or AWS job was run.  The local audit used only bounded,
short Python checks:

```text
sha256sum -c cases/d43_source_high_hensel_preflight_20260828.sha256
sha256sum -c xmodel/d43-source-high-hensel-preflight-gpt56-20260828.md.sha256
python3 -m unittest -v cases/test_d43_source_high_hensel.py
python3 cases/d43_source_high_hensel.py --selftest
/opt/homebrew/bin/python3 cases/d43_source_high_hensel.py --target-exponent 2 ...
```

Results:

```text
sealed input checks                         PASS
unit tests                                 8/8 PASS
pure selftest                              PASS
fresh real-source p2 replay                PASS
all 182 exact directional derivatives      PASS
eight dead-tail exact p2 value controls     PASS
independent full x-side sparse p2 control   PASS
alternate-kernel resume rejection          FAIL (state was accepted)
AWS/resource enforcement                   FAIL (wrapper absent)
```

## Final verdict

**REPAIR — do not launch.**  Preserve the mathematical implementation and
the `p^2` evidence.  Replace the resume schema with semantic deterministic
chain replay, add an enforced AWS custody wrapper, synchronize the forbidden
claim list, regenerate all seals, and obtain a new hostile review.  Once those
repairs pass, the preregistered target-16 source-only pilot is mathematically
appropriate.
