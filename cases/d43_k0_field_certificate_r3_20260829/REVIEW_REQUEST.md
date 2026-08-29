# Hostile review request — D43 `K0` field certificate, R3

**Requested verdict:** `PASS` / `PASS WITH REPAIR` / `FAIL`, on the *source*.
**Reviewer constraint:** must be a **different model** from the producer
(Opus 5). Your report's SHA-256 and your model name go into the authorization
record; `aws_supervisor_r3.validate_authorization_record` refuses any model
name that normalises to contain `opus`, and requires the verdict field to read
exactly `PASS`.

**Status you are reviewing:** `R3_SOURCE_READY_AWS_NOT_AUTHORIZED`. Nothing has
been executed on AWS and **no PARI/GP run of this file exists anywhere**. Do
not treat a PASS as a launch: the coordinator GO is separate.

## What changed since R2, and where your attention is most valuable

R2 was reviewed by Fable 5
(`xmodel/d43-k0-field-certificate-r2-hostile-review-fable5-20260829.md`,
`824e24d794e8828de6a3f5b9c9b0b40bf93305f72a06fd91275a6e89933f3602`, verdict
`PASS WITH REPAIR`). That review **confirmed the mathematical and harness
content of R2 in full** — all thirteen R1 defects genuinely repaired, the
battery honest, the layer separation watertight, no path to a wrong PASS in
either engine — and raised one blocking finding: the R2 authorization lease
could not be taken by the service user, so the next rehearsal was guaranteed
to fail closed before any mathematics.

**R3 is a custody repair.** The mathematics did not change and can be checked
not to have changed, mechanically:

| pinned value | R2 | R3 |
|---|---|---|
| census SHA-256 | `b828f93d6a29c15371e4d277473e63c0a25ba0280fa5ab44706d10c786f9aeb0` | identical |
| observable SHA-256 | `4b1c7ff63935adb27148a2967037b7a357354848b0bbc2f0df827db2e45148f6` | identical |
| battery SHA-256 | `e416de0e074cc0125ac2419a724c420d0d5f9c4dcd141abbd276f477bafbc25b` | identical |
| `k0_algebra` file SHA-256 | `a7de3c3fcefc42302e402b8dfcaeefbba6d5a582ae694447e8f95f6a8e8dd4a6` | identical (byte for byte) |
| `k0_field_checker` diff vs R2 | — | one import line and one schema string |
| `k0_mutations` diff vs R2 | — | two import lines, one docstring line, one schema string |

So the layers §5 and §6 of the R2 review confirmed may be cited as
already-reviewed if you agree the diff above is what it says it is; **verify
that first**, because everything else in this request assumes it.

The surfaces that are genuinely new and unreviewed, and where a hostile read is
most valuable, are: `aws_supervisor_r3.py`'s custody layer, `runner_r3.py`'s
run-directory law, `mint_claim_r3.sh`, `retire_claim_r3.sh`,
`custody_selftest_r3.py`, `preflight_r3.py` P11, the unit template, and the
two-line GP change. **Please do not assume the R2 review's PASS transfers to
any of those.**

The README's disposition table is the producer's claim about the R2 findings.
Treat it as an allegation.

## What you are asked to decide

1. Does the **unconditional** layer (L0–L4) actually prove what the terminal
   says it proves, using only what it executes?
2. Is the **conditional** layer (L5) correctly quarantined, so that a wrong `E`
   cannot contaminate the unconditional verdict — now that the censuses are
   layer-restricted rather than shared?
3. Can the certificate pass while being wrong — i.e. is there a gate that
   cannot fail, a mutation that should fail and does not, or a conclusion that
   is asserted rather than computed?

## Specific attacks I want you to run

### A. The two new L0 gates, which carry the rank claim

* `RELATION_LEADING_TERMS` claims that pairwise coprime pure-power leading
  monomials under graded lex give a Gröbner basis by Buchberger's first
  criterion, hence freeness of rank `prod(basis_shape)`. Check the order is
  really a monomial order on these five relations (in particular that
  `deg A1^3 = 3 > deg r = 1` and that `Phi_42`'s tail is degree ≤ 11), that
  the "already reduced" loop is doing what it says, and that the conclusion
  is the one the theorem report's Lemma L1 needs. I claim this gate is
  deliberately blind to *which* monic degree-12 `Phi_42` is used. Decide
  whether the README is honest about that and whether the other three pins
  cover it.
* `RANK432_INDEPENDENCE` builds 18 middle points as (registered frame) times
  `mu_3` and claims that is the *complete* solution set of
  `r^2 = 3, A1^3 = 3+r, A2^3 = 3-r` over `F_p`. Verify the completeness
  argument, verify that the Kronecker factorisation of the 432×432 evaluation
  matrix is correct with the column indexing actually used
  (`j-1 = 9b + 3c + d`), and verify that the squared determinants really are
  row-order independent. If GP's `polrootsmod` route and Python's frame route
  can produce *different sets*, the two engines will disagree and the run will
  refuse — but say so, because that would be a design fault, not a finding.
* Both gates emit shared observables. Confirm the GP side computes the same
  three numbers from an independent construction.

### B. The theorem-separation repair (D1)

* `CENSUS_UNCONDITIONAL`, `CENSUS_CONDITIONAL` and `CENSUS_COMPLETE` partition
  the registry. Confirm the three expected-sets are what the names say, that
  `theorem_inputs` in `result.json` really are pairwise disjoint, and that no
  L5 or CORROBORATION failure can reach `unconditional_k0_theorem`.
* The battery pins 19 `(unconditional, conditional)` pairs. Find a mutation
  whose declared pair is wrong, or a class of failure the controls miss.
  Specifically: is there any input for which the unconditional boolean is
  `true` while an L0–L4 gate did not run?

### C. The free-ring Galois gate (D3)

`GALOIS_STABILITY_FREE` substitutes sigma into unreduced relations and
requires the image multiset to be the relation set. Check that
`fp_substitute` really expands (no accidental reduction), that the involution
test is not vacuous, and that "sigma permutes the ideal generators" is enough
to conclude "sigma descends to a ring automorphism of `K0`". Then decide
whether the declared `sigma_relation_permutation` pin adds anything or is
circular.

### D. Gates that might still not be able to fail

Read every gate in `k0_field_checker_r3.py` and every `chk(`/`chkE(` in
`k0_field_cert_r3.gp` and ask of each: *what input makes this print 0?* R1's
reviewer found `RANK432_MONIC_BASIS`, `GALOIS_STABILITY`, `NONABELIAN`, five
of six `BASE_CONDUCTOR_TOWER` needs, the `eps` embedding line, the
within-fibre character test and the `(0,0)` representative need. I believe
each of those is now either computed or deleted. Find the ones I missed.
Candidates I am least confident about:

* `L1 CRT` — the R2 review found the GP copy constant-true. It now reads
  `Z8E`, `GENE`, `Z42E` and `CONDTOWER[3]`. Is it *actually* falsifiable now,
  and does it still say the same thing? (The GP file is still unparsed by any
  GP: a syntax error here is a repair, not a finding, but say so.)
* `IDEMPOTENTS_ONLY_0_1` — still literal-vs-literal through mutable `Spec`
  fields. Is routing through `Spec` enough?
* the GP `L2 x^2 - 3y^2 = -1 is impossible mod 3` line, which enumerates nine
  residue pairs. Real, or padding?
* `E_BASE_REDUCTION` — does the chain
  `(alpha2/alpha1)*s^4 == -C2/C1` plus `u^3 == alpha2/alpha1` really imply
  `q0^4 == c`, and is anything in it reading a literal back to itself?

### E. The mutation battery

* Verify that each of the 58 `MUST_FAIL` entries fires **its named gate**, not
  merely something. Read `gate_errors` for each.
* Verify the 4 `MUST_SURVIVE` entries survive for the *right* reason.
* Find a load-bearing datum I did **not** mutate. `Spec` is the complete list
  of what the battery can reach; anything load-bearing that is a literal
  inside a gate body instead of a `Spec` field is out of reach and is a
  defect. R1's reviewer found two (`14/154` and the pointbank `E` form) and
  both are routed now. Enumerate the remaining gate-body literals and decide,
  one by one, whether they are load-bearing.
* Construct a *new* surviving mutation and check the harness does not reject
  it.

### F. The GP file, which I could not execute

There is no `gp` on the producer host. `k0_field_cert_r3.gp` has been
**hand-reviewed and statically census-audited only**. Please either run it on
a PARI 2.15.4 host or read it as an adversary. New risk points relative to R1:

* `matrix(m,n,i,j,expr)` with `t_INTMOD` entries and `matdet` over `F_p`;
* `polrootsmod` on the non-monic `HB*'t^2 - HC` and on `'t^3 - (3±r)`;
* the multivariate `subst` chain in `sg(f)`, including the temporary variable
  `'tw`, and whether polynomial `==` after that chain is canonical;
* the three new data variables `Z42E`, `Z8E`, `GENE` and their three use
  sites, which are the only R3 change to this file besides a comment;
* `chkE` as a second accumulator, and whether the census still counts every
  printed line exactly once;
* whether the predicted count 110 and the declared `nexpect = 110` agree with
  what GP actually prints — both are my arithmetic, and
  `preflight_r3.gp_static_census` is my predictor.

If the GP file does not run, that is a repair, not necessarily a FAIL: the
Python engine is independent and complete for the unconditional layer. But the
*two-engine* claim in the terminal would then be false, and the terminal must
not say it.

### G. The R3 privilege boundary — the main event

This is the surface the R2 review sent back. The question is not "does it look
safer"; it is **"can it actually run, and is it still fail-closed?"** Both R1
and R2 shipped custody code that had never executed and that would have burned
the one licensed rehearsal.

* Walk the whole sequence in `run_job`: `production_policy` →
  `live_identity` → `load_authorization` → host binding →
  `require_service_identity` → environment → cgroup → `establish_custody` →
  try block. For each step ask: **can a `jc2k0` process with an empty
  capability set actually do this on a Linux host where the sealed parent is
  root-owned 0755?** Name any step that cannot.
* `establish_custody` verifies then burns. Convince yourself the burn is
  unreachable from a failed precondition, that the run path in the
  authorization is what binds the lease location (and that it is inside the
  hashed record, hence inside the live tag), and that a second presentation
  produces no terminal.
* The claim token is root-owned 0444 inside a directory the service owns. Is
  it really unforgeable by `jc2k0`? Consider: `chown`, `chmod`, `rename`,
  hard links, replacing the directory, a symlink at the token path, an ACL,
  `CAP_DAC_OVERRIDE`, `CAP_CHOWN`, `CAP_FOWNER`, and what the empty
  `CapabilityBoundingSet=` plus `NoNewPrivileges=yes` actually exclude. The
  producer's claim is: the service can only *delete* it, and deleting denies
  only itself. Attack that claim.
* `mint_claim_r3.sh` runs as root via `ExecStartPre=+`. Read it as an
  adversary: argument injection, the `set -C` noclobber `O_EXCL` claim, the
  ordering (spent marker before the run directory), the `realpath` test, the
  portable `stat`/`sha256` wrappers, what happens on a partial mint, and
  whether a unit restart can ever produce a second mint. Note it deliberately
  does **not** parse the authorization: the record-to-claim binding is
  enforced by `verify_claim_token` in Python. Is that split sound?
* `retire_claim_r3.sh` runs as root via `ExecStopPost=+` on every exit path.
  Can it damage evidence, or be pointed somewhere it should not be?
* `CustodyPolicy` is the single seam that makes the boundary testable off-host.
  Production constructs it once with a literal `custodian_uid=0`. Decide
  whether that seam can be reached in production, whether the P11 static
  controls really pin it, and whether the fixture policy (custodian uid = the
  running uid, ancestors allowed to be custodian- *or* root-owned) proves
  anything about the deployed configuration. **In production the two allowed
  ancestor owners coincide, both being 0** — check that.
* `runner_r3.check_run_dir_clean` is the R3 producer-found repair (REPAIR-2).
  The R2 law admitted only two file names while the supervisor always stages
  `<run dir>/source` first, so every real launch would have died on
  `RUN_DIR_REUSE`. Verify the new law in both directions, and verify the
  custody file names really are derived from the marker's authorization
  digest.
* P11's 13 source mutations claim each control is load-bearing. Find a control
  with no mutation, or a mutation whose declared effect is wrong.
* `emit_immutable` creates the final name with `O_CREAT|O_EXCL`. Check there
  is no remaining window, and that a crash mid-write is caught by the manifest
  replay. (Unchanged from R2.)
* `validate_authorization_record` is a pure function, **frozen in R3**;
  preflight P9 runs 33 cases against it. Find a record that should be refused
  and is not. The R2 review's `0pus 5` note is recorded and deliberately not
  acted on; say if you disagree.
* The instance type is a single exact value. Decide whether that is right or
  whether it will simply block the next rehearsal. (Unchanged from R2.)
* `_forbidden_language_scan` still uses `\bK_?[1-9]\d*\b`. Check it does not
  false-positive on the new artifacts and does not miss an obvious evasion.

### G2. What the custody controls do not execute

The producer host has no root, so no fixture here creates a root-owned object,
and no fixture runs under systemd. Decide whether the substitutes are honest:

* real POSIX facts executed: a directory without a write bit refuses creation
  even to its owner; a 0444 file refuses a write even to its owner; an
  unprivileged process cannot `chown` to root; `O_EXCL` refuses a second
  create;
* the systemd identity is checked as a *contract* (`User=`/`Group=` in the
  unit versus `DEDICATED_SERVICE_USER`/`DEDICATED_SERVICE_GROUP` in the
  supervisor), not by running systemd;
* the root-owned half is deferred to `custody_selftest_r3.py
  --on-host-dry-run`, run as the service user on the deployed host before the
  unit starts, which calls the same `verify_custody_preconditions` and stops
  before the lease.

Is that enough to license a rehearsal, or do you want the dry run to be a
precondition inside the supervisor rather than an operational step?

### H. Claim discipline

The terminal must keep four things apart. Check that:

* no unconditional gate reads `spec.e_terms`, `spec.q0_terms`, or the
  pointbanks;
* `unconditional_k0_theorem` is computed from L0–L4 non-corroboration gates
  only, and `e_conditional_ratio_theorem` from L5 non-corroboration gates only;
* the E theorem is typed **single-engine** everywhere it appears;
* nothing anywhere claims a D43 row, point, template, D25, raw-J, Keller or
  JC2 result, that the 432-frame count proves fieldness, or that the GP engine
  has run.

## Frozen inputs

| file | SHA-256 |
|---|---|
| `cases/d43_common_integral_emitter.py` | `5420b5c0b4164c719e98316cade96c094c2945a6fed8bad3ac0926771855984d` |
| `cases/d43_exact_sparse_rows_v2_20260828/selected_rows_v2.py` | `9fc9bd7a365827ddba2c1ba45cbb34870d6f2d71c9d3eecb6b242d46e00990b2` |
| `cases/d43_full_pointbank_p105337.pkl` | `bb0f13b61616c486116027e284483a4fb0f529f8df2dca7f728d56584d98fcbb` |
| `cases/d43_full_pointbank_p105673.pkl` | `b933cdb5b72bd4073da0cb82150db768f6b4607d5cd29d3d4aec0fe22ce5bcc3` |
| `xmodel/d43-e5-e6-elimination-bridge-gpt56-20260828.md` | `e1b99600b01f91f7b95df4f7f969481efa1e7b1ee377e83156f3f6b6a8e3c863` |
| `xmodel/d43-k0-splitting-primary-research-opus5-20260828.md` | `6d3d53c20387d324766daaf40eb502df42d9e2776c6ab6053041bc1f3dee1430` |
| `xmodel/d43-k0-field-theorem-hostile-review-grok46-20260829.md` | `07f20be55add0fea0ff6329ce0d4ca386024af33edad33254d46451fd575a94a` |
| `xmodel/d43-k0-field-certificate-r1-hostile-review-fable5-20260829.md` | `29e9496e0552f94d6823c744b7b979ad02274e6cbf39ae124ec01e6465d596e2` |
| `xmodel/d43-k0-field-certificate-r2-hostile-review-fable5-20260829.md` | `824e24d794e8828de6a3f5b9c9b0b40bf93305f72a06fd91275a6e89933f3602` |

The packet's own file hashes are in `PAYLOAD.sha256` and `SOURCE_SEAL.sha256`;
the deterministic source archive is `SOURCE_ARCHIVE.tar` with its hash in
`SOURCE_ARCHIVE.sha256`.

The R1 rehearsal's three harvested terminal records live under
`cases/d43_k0_field_certificate_r1_20260828/custody/ephemeral_20260829T010727Z/terminal/`.
They are evidence about R1 and are not part of this packet's seal.

## How to replay everything the producer ran

```
cd <repo root>
python3 cases/d43_k0_field_certificate_r3_20260829/seal_r3.py --root . --verify
python3 cases/d43_k0_field_certificate_r3_20260829/preflight_r3.py --root .
python3 -O cases/d43_k0_field_certificate_r3_20260829/preflight_r3.py --root .
python3 cases/d43_k0_field_certificate_r3_20260829/custody_selftest_r3.py
```

The custody controls refuse to run as root; run them as an ordinary user.

The sealer must report `ok: true` with all four `matches_disk` entries true;
if it does not, the packet you are reading is not the packet that was sealed
and you should stop and say so.

Expect `preflight_pass: true`, 42/42 Python gates, 58 MUST_FAIL + 4
MUST_SURVIVE + 5 gate unit tests, 19 theorem-separation controls, GP static
census `110/110`, observables `29/29`, census SHA-256
`b828f93d6a29c15371e4d277473e63c0a25ba0280fa5ab44706d10c786f9aeb0`, observable
SHA-256 `4b1c7ff63935adb27148a2967037b7a357354848b0bbc2f0df827db2e45148f6`, GP
script SHA-256
`c3f576dd5bbc1c0af970246379c97d1c541daa7ae521f722ed43f905e4713d76`, and all
eight P8 isolated-import controls, 33 P9 authorization controls plus the
artifact and run-directory controls, and 10 P10 gate-surface controls green.
Runtime is well under a minute; nothing here needs AWS, PARI, or a CAS.
