# D43 coefficient algebra `K0`: sealed exact field certificate, R3

**Status: `R3_SOURCE_READY_AWS_NOT_AUTHORIZED`.**
A different-model hostile source PASS and a coordinator GO are both required
before any execution. No AWS run, no PARI run, and no CAS run was performed
while producing this packet, and **the GP file has still never been parsed by
any GP.**

R3 is a fresh packet. Neither `cases/d43_k0_field_certificate_r1_20260828/`
nor `cases/d43_k0_field_certificate_r2_20260829/` is patched or superseded in
place; both are immutable, and their authorizations and leases are retired.

## Why R3 exists

R3 repairs a **custody defect only**. The mathematics, both engines and the
mutation battery are the reviewed R2 mathematics: the census hash, the
observable hash and the battery hash are byte-identical to R2's
(`b828f93d…`, `4b1c7ff6…`, `e416de0e…`), and `k0_algebra_r3.py` is byte-identical
to `k0_algebra_r2.py`.

1. The Fable 5 hostile source review of R2
   (`xmodel/d43-k0-field-certificate-r2-hostile-review-fable5-20260829.md`,
   verdict `PASS WITH REPAIR`) confirmed the mathematical and harness content
   of R2 in full — all thirteen R1 defects genuinely repaired, no path to a
   wrong PASS in either engine — and raised exactly one blocking finding,
   REPAIR-1: **the R2 authorization lease could not be taken by the service
   user.** `claim_authorization_lease` required the run parent to be owned by
   uid 0 with no group or world write bit, and then tried to *create* a file
   in it, while the unit runs as `User=jc2k0` with an empty capability set.
   The two requirements are jointly unsatisfiable, so the next rehearsal was
   guaranteed to die — either at `CUSTODY_FAULT PATH_OWNER`, or on an uncaught
   `PermissionError` traceback — before either engine ran. That is the same
   failure class as the R1 `-I` import fault, in code that
   `preflight_r2.py` never executed.
2. While rebuilding that path the producer found a **second** never-executed
   integration fault of the same class in R2 (REPAIR-2, below): the R2
   run-directory law admitted only `job_marker.json` and
   `execution_pins_live.json`, but the supervisor always extracts the reviewed
   archive to `<run dir>/source` before it spawns the runner, so
   `check_run_dir_clean` would have refused `RUN_DIR_REUSE` on **every** real
   launch, one step after REPAIR-1.

Both are repaired here, and both now have executed controls (P11) that would
have caught them. The promoted paper theorem is unchanged and is not
broadened.

## The R3 privilege boundary

```
<sealed parent>                             root:root   0755   never service-writable
  ├── spent/                                root:root   0700   root-only mint ledger
  │     └── <auth-sha>.spent                root:root   0444   the one-shot gate
  └── run-<UTC>/                            jc2k0:jc2k0 0700   the only writable path
        ├── .jc2-k0-r3-claim-<auth-sha>.json          root:root 0444
        └── .jc2-k0-r3-authorization-<auth-sha>.lease jc2k0     0444
```

* The sealed-parent gate is **unchanged** — root-owned, no group or world
  write bit, no writable ancestor. It is now *satisfiable* because the service
  never creates anything in the parent, rather than *weakened*.
* Root, via `ExecStartPre=+ mint_claim_r3.sh`, creates the per-run directory
  and chowns it to `jc2k0`, and mints a **root-owned 0444 claim token** inside
  it. An unprivileged process cannot create that token (it cannot chown to
  root) and cannot modify it (no write bit for anyone but root; the unit's
  capability set is empty, so `CAP_DAC_OVERRIDE` and `CAP_CHOWN` are
  unavailable; and a POSIX ACL cannot smuggle write access in, because the ACL
  mask surfaces in the group-class bits the parent gate rejects). It can only
  unlink it, which denies only itself: the launch then refuses `CLAIM_ABSENT`
  and consumes nothing.
* Minting is one-shot **outside** the unprivileged process:
  `mint_claim_r3.sh` creates `spent/<digest>.spent` with `O_EXCL` *before*
  anything else exists, so a unit restart dies with `MINT_ALREADY_SPENT` and
  never reaches the supervisor, even if the first mint crashed halfway.
* The service takes its one-time consumption lease **inside its own run
  directory**, last, after every precondition has been verified. A failed
  precondition therefore never burns the authorization; a second presentation
  of the same authorization lands on the same directory (the run path is
  inside the hashed record, hence inside the live tag) and dies at
  `AUTHORIZATION_REUSE`. Every custody step sits outside the try block, so a
  refused launch writes no terminal at all.
* Every filesystem call on the custody path converts `OSError` into a
  `CustodyFault`, and `main` converts anything else into
  `CUSTODY_FAULT UNCLASSIFIED` with rc 70. The R2 traceback path is gone.
* `ExecStopPost=+ retire_claim_r3.sh` seals the finished run directory back to
  root-owned and read-only.

Before starting the unit, ops runs, **as the service user**,
`custody_selftest_r3.py --on-host-dry-run`, which calls the very same
`verify_custody_preconditions` the supervisor calls, against the real
root-owned tree, and stops before the lease. It writes nothing and consumes
nothing, so a refusal there costs no coordinator record.

## Every R2 review finding, and its disposition

| # | R2 review finding | disposition in R3 |
|---|---|---|
| REPAIR-1 | the authorization lease cannot be taken by the service user (§4) | **repaired**: the privilege boundary above; sealed-parent gate unchanged, run directory pre-created and service-owned, claim token root-minted, lease taken inside the run directory after every precondition. Executed by P11 controls and 10 supervisor mutations. |
| REPAIR-1b | `PermissionError` escapes `claim_authorization_lease` as a traceback (§4) | **repaired**: every custody filesystem call raises `CustodyFault`; `LEASE_UNWRITABLE` is exercised against a real 0500 directory, and `main` converts anything else to `CUSTODY_FAULT UNCLASSIFIED`. Mutation `CM6` restores the traceback and the control fails. |
| §4 (asked) | "add a preflight control that exercises the lease claim end to end as a non-root user against both an owned and an unowned parent fixture" | **done, and widened**: P11 runs the whole sequence, both parent branches, both claim-owner branches, the mode laws, the one-time claim, the second-claim refusal, the crash/restart cases, and the no-burn proof. |
| §7.i | the GP `L1 CRT` line is constant-true | **repaired**, mechanically: `Z8E`, `Z42E`, `GENE` and `CONDTOWER[3]` drive it. Gate count, labels, observables and values unchanged; the GP file's hash moved. |
| §7.ii | the unreachable within-fibre branch in `charframes` should not be mistaken for a check | **repaired as documentation**: the branch is marked `[R3-B]` defensive, not a gate, not counted. |
| §7.iii | the GP leading-term block validates declared `LEAD` data, not the relations' leading monomials — "worth one honest line in a future README" | **recorded**: that line is now in *Two genuinely independent engines* above. No code change; changing it would change the GP engine. |
| §5E | `IDEMPOTENTS_ONLY_0_1` is a Spec-routed emission-policy pin; "I recommend (cosmetic) retyping it away from `THEOREM`" | **recorded, deliberately not changed.** Retyping moves a gate between the `theorem_inputs` censuses, which is precisely the D1 separation surface the review confirmed; the charge for R3 is a custody repair that preserves every mathematics hash. It is a live item for a future mathematics revision. |
| §8 | `normalize_model` maps look-alike evasions such as `0pus 5` to `0pus5`, which does not contain `opus`; "a note, not a repair" | **recorded, deliberately not changed.** `validate_authorization_record` is frozen in R3 — the charge forbids changing authorization semantics, and the guard is against accidental same-model review, not a malicious coordinator who could write anything. |
| §6 | the compound coordinated-scope-shrink fixture passes the checker | **recorded** (already documented in R2): the observable pin and cross-engine agreement refuse it at run level. Unchanged. |
| §10.1 | the GP file has never been parsed by any GP | **unchanged and restated**: still true, stated in the README, the preregistration, the preflight output and the terminal. |

## What is certified

Two theorems and two non-theorems, kept apart in the gate typing, in the
runner terminal and in the supervisor terminal.

**Unconditional (`K0_UNCONDITIONAL_THEOREM`, layers L0–L4).** `K0` is a number
field of degree exactly 432, Galois and non-abelian over `Q`. Its degree-48
base is exactly `Q(zeta_168)`. The two Kummer cubic classes are independent.
Its only idempotents are `0` and `1`; there is one factor. It is finite étale
of rank 432 over `Z[1/42]` and the ramified rational primes are exactly
`{2,3,7}`. Both registered frames are degree-1 primes and both primes split
completely with exactly 432 frames; the registered `p^2` frame is the unique
Hensel lift. This layer reads no `E`, no pointbank, no `nffactor`, and no
absolute primitive polynomial. **Two engines.**

**Conditional (`E_CONDITIONAL_RATIO_THEOREM`, layer L5).** *Conditional on the
literal displayed* `E = (9+5*r3)*A1*W1^4 + (9-5*r3)*A2*W2^4`, the ratio
`W1/W2` is `K0`-rational: `q0 = u*(1+i)*(r3-1)/2` with `u = A2/A1` and
`i = r3*(1+2*zeta42^14)/3` solves `E` by direct substitution, and the four
branches `q0*i^k` are four distinct elements of `K0`. `E` is **not**
re-derived here; it is *read* out of the sealed E5/E6 bridge. **One engine**
— see D7 below.

**`EXECUTION_INTEGRITY`** (census, mutation battery, cross-engine agreement,
manifest and archive replay, environment) and **`CORROBORATION`** (the
pointbank regression and the GP base identities) are reported separately and
are never folded into either theorem. A theorem status is *credited* only
jointly with `EXECUTION_INTEGRITY = PASS`; corroboration is never credited.

The charged theorem report is
`xmodel/d43-k0-splitting-primary-research-opus5-20260828.md`, SHA-256
`6d3d53c20387d324766daaf40eb502df42d9e2776c6ab6053041bc1f3dee1430`, whose
prose steps were independently confirmed by
`xmodel/d43-k0-field-theorem-hostile-review-grok46-20260829.md`, SHA-256
`07f20be55add0fea0ff6329ce0d4ca386024af33edad33254d46451fd575a94a`. Both are
sealed into this packet's archive.

## The R1 review's defect list, and what R2 does about it

| # | R1 defect | R2 repair |
|---|---|---|
| — | `python3 -I` dropped the script directory; the sibling import failed | `runner_r3.py` loads `k0_algebra_r3`, `k0_field_checker_r3` and `k0_mutations_r3` by explicit file path out of the extracted packet directory, verifying each against `PAYLOAD.sha256` whose own digest is bound to the authorization's `packet_manifest_sha256`. `sys.path` is never touched and the loader asserts it is unchanged. Isolated mode is now *required*, not merely used. `--import-smoke` runs exactly that loader and preflight P8 executes it as a real `python3 -I -B` subprocess, alongside a live reproduction of the R1 failure. |
| D1 | both theorem booleans required one shared census, so a wrong `E` misreported the unconditional theorem as FAIL | three census gates: `CENSUS_UNCONDITIONAL` (L0–L4 non-corroboration), `CENSUS_CONDITIONAL` (L5 non-corroboration), `CENSUS_COMPLETE` (integrity only). 19 battery entries pin the exact `(unconditional, conditional)` pair they must report; the battery refuses unless both separation classes occur. |
| D2 | `RANK432_MONIC_BASIS` loops were unfalsifiable and `confluent_on_basis` was an asserted literal | the literal is gone and the gate is retyped `EXECUTED`. Freeness of rank 432 is now `RELATION_LEADING_TERMS`, computed in the **free** polynomial ring: the five relations have pairwise coprime pure-power leading monomials under graded lex, so Buchberger's first criterion makes them a Gröbner basis and the standard monomials are the declared box. `RANK432_INDEPENDENCE` adds a mod-`p` witness: the 432×432 evaluation matrix at the 432 `F_p`-points is a Kronecker product of a 12×12, an 18×18 and a 2×2 block, all three nonsingular. Both engines compute the three squared determinants. |
| D3 | the `GALOIS_STABILITY` relation loop computed `sigma({}) == {}` | `GALOIS_STABILITY_FREE` substitutes sigma into the **unreduced** relations and requires the resulting multiset to be the relation set, with the induced permutation itself pinned. `GATE_UNIT_SIGMA_FREE_VS_QUOTIENT` runs both shapes side by side on a broken sigma and shows the R1 shape accepts it and the R2 shape does not. |
| D4 | no cardinality or prime-set pins on `frames` and `pointbank_expected`; two unintended surviving mutations | `_frame_cardinality` and the pointbank gate pin both counts and both prime sets; `M_FRAMES_HALVED`, `M_FRAME_PRIME_SET`, `M_POINTBANK_HALVED` and `M_POINTBANK_PRIME_SET` are MUST_FAIL entries and preflight P10 re-runs the two demonstrations. |
| D5 | gate-body literals duplicating `Spec` (`14/154`, the `E` form inside the pointbank gate) | `_character_frames` reads `spec.r3_exponents` and `spec.alpha_data`; the pointbank gate builds `E` through `_E_mod` from `spec.e_terms`. The presentation itself (`alpha_data`, `r_square`, `h_relation`) is a constructor argument of `K0Algebra`, so a mutation of it moves the whole checker. |
| D6 | seven falsifiable `Spec` fields had no mutation | all seven now do, plus one per new field. 58 MUST_FAIL entries, up from 35. |
| D7 | GP printed `E_CONDITIONAL` with no gate that reads `E` | the GP flag is `E_BASE_IDENTITIES`; the GP L5 block now genuinely reads the literal `ETERMS` data and checks the base-level reduction chain `(alpha2/alpha1)*s^4 == -C2/C1`; and the runner terminal types the E theorem as **single-engine Python with GP base-identity corroboration**. |
| D8 | `reviewer_pass.verdict` was never checked and the same-model refusal missed case variants | `validate_authorization_record` is a pure function requiring the verdict to be exactly the string `PASS` and refusing any model name that normalises (lowercase, punctuation stripped) to contain `opus`. Preflight P9 runs it against 33 crafted records including `pass`, `PASS `, `Pass`, `PASSED`, `<MUST_BE_PASS>`, `OPUS5`, `opus-5`, `Opus5`, `claude-opus-5` and `Opus 5 (max reasoning)`. |
| D9 | `alarm(600)` exceeded both the 120 s gp cap and the 300 s unit cap | the optional `nffactor` block is **deleted**. It was never on the theorem path. Its removal also lets the runner treat every unrecognised GP output line as a fault, since nothing prints `OPTIONAL` any more. |
| D10 | constant-true sub-checks padding the census in both engines | the conductor tower recomputes `disc(x^2-3)` and the three cyclotomic degrees; the `eps` line reads `spec.eps_data`, checks the norm, the trace, the mod-3 impossibility of `x^2-3y^2=-1` and the `b=1` unit list, and its message is no longer backwards; the vacuous within-fibre character test is replaced by a per-hom exact-order-168 test in GP and a per-hom `Phi_168(omega) = 0` test in Python; the dead `(0,0)` need is moved ahead of the witness search; `NONABELIAN` computes `alpha1*alpha2` and `disc(t^3-m)` instead of asserting `6` and `-972`. |
| D11 | `emit_immutable`'s exists-then-replace window; `RUN_DIR_REUSE`'s three-name list | artifacts are created with `O_CREAT|O_EXCL` **on the final name**, so the collision semantics are the atomic create itself and there is no `.tmp` sidecar at all; `check_run_dir_clean` pins the whole pre-run directory content to exactly `{job_marker.json, execution_pins_live.json}`. |
| D12 | the static-census predictor combined nested loops by `max` and counted parentheses on raw lines | nested loops multiply; comments and string literals are stripped before the parenthesis scan; loop bounds are resolved from the file's own vector declarations instead of a hardcoded table. Preflight P10 mutates the GP text three ways and requires the predictor to move exactly when it should. |
| D13 | dead code (`SAFE_ID_RE`, unused imports) | removed. |

Two R1 review findings are **retained deliberately**, with reasons:

* **The `L1 CRT` line.** It restates the exponent congruence that
  `BASE_ZETA8` and `BASE_SURJECTIVE` already imply. It is kept because both
  sides read the same mutable `Spec` exponents, so it is redundancy rather
  than a gate that cannot fail; `M_BASE_SURJ_EXPONENT` and
  `M_BASE_GEN_Z8_POWER` both fire it.
* **`SPLIT_COUNT_432` remains `CONSISTENCY`.** A totally split `L x L x L`
  with `[L:Q] = 144` would produce the same 432. R2 does not upgrade it and
  the typing string says so verbatim in both engines.

## Two genuinely independent engines

| engine | file | what it uses |
|---|---|---|
| PARI/GP 2.15.4 | `k0_field_cert_r3.gp` | `polcyclo`, `t_POLMOD`, `t_INTMOD`, `polrootsmod`, `matrix`, `matdet`, `subst` |
| stdlib Python | `k0_field_checker_r3.py` + `k0_algebra_r3.py` | explicit integer polynomials, a free polynomial ring with a graded-lex order, explicit `F_p`, and a canonical 432-monomial normal form written from scratch |

Neither reads the other's output. They agree on **29 shared integer
observables**, emitted by GP as `OBS key value` lines and rebuilt
independently by the Python engine; `runner_r3.py` requires exact agreement on
every key and refuses on any disagreement. 25 of the 29 belong to the
unconditional layers and 4 are E-layer corroboration; the terminal reports the
split. Neither engine's own PASS banner is trusted: the runner counts all 110
printed GP gate flags itself and compares the census line against the count.

R1's `Map`/`mapput`/`mapget`/`Mat(t_MAP)` layer and every discrete-log helper
are gone from the GP file, which reduces the unexecuted-API surface. Preflight
P3 additionally scans the GP file for those deleted constructs, requires it to
be ASCII and tab-free, and bounds every one of the 99 printed gate labels
against the runner's 80-character parse window — a hand check in the R1 review,
executed here, because an over-wide label would fault the run exactly as the R1
import defect did.

One asymmetry, stated plainly (the R2 review's §7.iii): the GP leading-term
block validates the *declared* `LEAD` data — pure powers, distinct variables,
shape — but does not recompute the leading monomials of the actual relations.
That tie is Python-only. GP's substantive rank content is the independence
witness, and every load-bearing number in the block is cross-checked through
the shared observables, so the two-engine claim for the unconditional layer
stands; but "two engines" does not mean "two identical checks" at that one
site.

The R2 review also found the GP `L1 CRT` line constant-true — `(21*5+4*16)%168`
cannot print 0 without editing the file, whereas the Python engine read the
same mutable exponents on both sides. R3 makes it data-driven: `Z8E`, `Z42E`
and `GENE` now drive the zeta8 line, the `GENERATION` line and the `CRT` line
alike, with the modulus read from `CONDTOWER[3]`. The gate count, the label
set, the observable set and every printed value are unchanged; only the GP
file's hash moved, and `execution_pins_r3.json` records the new one.

## The theorem path avoids the expensive and the unexecuted

Kummer independence is established by **explicit cubic-character ring
homomorphisms** at two primes, `673` and `1009`, both `= 1 (mod 168)`. For each
prime the certificate exhibits actual roots `omega` of `Phi_168 (mod p)` — each
one *is* a ring map `Z[y]/(Phi_168) -> F_p` — covering both square roots of 3,
and then checks by brute force over the nine pairs `(i,j)` that only `(0,0)`
annihilates both character pairs, and that the pairs generate `mu_3 x mu_3`.
This is basis-free: it does not depend on which primitive cube root of unity is
chosen, which is why the certificate never computes a discrete logarithm.

Consequently there is **no** appeal to `nffactor`, to irreducibility of a
degree-432 or degree-144 polynomial, to an absolute primitive element, or to
the modular pointbanks.

The registered primes `105337` and `105673` are **character-silent**: both
`alpha_k` are cubes there, so their character pairs are trivial and they
annihilate all nine classes. The certificate gates this positively
(`KUMMER_SILENT_PRIME_GUARD`) and refuses to use them as certificate primes.

## What the two new L0 gates do and do not prove

`RELATION_LEADING_TERMS` is a complete executable proof of Lemma L1 for
*whatever monic presentation `Spec` declares*: coprime leading monomials give
a Gröbner basis by Buchberger's first criterion, hence freeness on the
standard monomials. It is deliberately **not** a pin on `Phi_42`; the specific
polynomial is pinned by `SRC_PHI42_LITERAL`, `PHI42_DISCRIMINANT` and
`RANK432_INDEPENDENCE`. Preflight P10 makes exactly that point executable: fed
the absurd datum `x^12 + 5`, `RELATION_LEADING_TERMS` correctly passes while
`RANK432_INDEPENDENCE`, `SRC_PHI42_LITERAL` and `PHI42_DISCRIMINANT` all fail.
The R1 gate passed on all four.

`RANK432_INDEPENDENCE` certifies that the 432 standard monomials are
linearly independent **over `F_p` at the witness prime**, so the reduction of
the presented algebra is free of rank 432 there. It is a witness, not a
substitute for the Gröbner argument, and its 18 middle points are built from
the registered frame times `mu_3` while GP builds the same set from
`polrootsmod`; the shared observables are the squared block determinants,
which are row-order independent.

## Mutation battery

`k0_mutations_r3.py`: **58 MUST_FAIL**, **4 MUST_SURVIVE**, **19 theorem
separation controls**, 5 gate unit tests. Each MUST_FAIL entry names the gate
that has to report the failure; "something failed" is not accepted.

The four **MUST_SURVIVE** entries guard against a vacuous "all mutations fail"
harness: `eps -> eps^2`, the generator basis `(alpha1, alpha1*alpha2)`, the
reordered certificate primes, and the all-inverse representative set. A
battery that reports any of them as a failure is miscoded.

The five gate unit tests are the order-42 counterexample (`zeta_168^28` has
order 6 and passes the charged recipe's three-condition test), a flipped
nibble in a pinned source hash, the free-ring-versus-quotient sigma
demonstration, the leading-term coprimality criterion, and the corroboration
separation control.

**The battery is byte-identical to R2's**, mutation for mutation and verdict
for verdict: `battery_sha256 = e416de0e07…`, the same value the R2 review
replayed. R3 adds a *separate* battery on the custody surface —
**13 hostile source mutations** in preflight P11, each patching one anchor in
the sealed supervisor or runner and requiring the named control to stop
holding. `CM11` reproduces the R2 run-directory law exactly and shows it
refusing a correctly staged launch.

## Files

| file | role |
|---|---|
| `k0_algebra_r3.py` | exact arithmetic: integer polynomials, `Q[x]/(Phi_168)`, the free ring `Q[z,r,A1,A2,h]` with graded lex, a parametrised canonical 432-monomial `K0`, scan-free `F_p` helpers, an `F_p` determinant |
| `k0_field_checker_r3.py` | 39 named fail-closed gates in six layers plus three layer-restricted census gates, 42 in all |
| `k0_field_cert_r3.gp` | the corrected PARI/GP engine, 110 gates, 29 observables |
| `k0_mutations_r3.py` | the hostile battery, the separation controls and the five gate unit tests |
| `runner_r3.py` | sealed sibling loader, both engines, observable agreement, bounded immutable artifacts, manifest and archive replay, one atomic terminal with four separated blocks; `--import-smoke` is the loader-only mode |
| `aws_supervisor_r3.py` | AWS custody: live IMDSv2 identity, tag-addressed authorization, pure record validator, host/instance/PARI-binary binding, cgroup-v2 one-core zero-swap contract, the R3 privilege boundary (sealed parent, service-owned run directory, root-minted claim token, one-time lease), one terminal |
| `aws_worker_r3.sh` | the environment-stripping exec shim |
| `mint_claim_r3.sh` | **new in R3**: the root-side one-shot mint (`ExecStartPre=+`); spent marker first, then the run directory, then the root-owned claim token |
| `retire_claim_r3.sh` | **new in R3**: the root-side retirement (`ExecStopPost=+`); seals the finished run directory back to root-owned and read-only |
| `custody_selftest_r3.py` | **new in R3**: the executable custody controls (real directories, real uid/gid, real permission bits) and the on-host dry run |
| `systemd_unit_template_r3.service` | root-owned unit template; drop-ins forbidden; mints as root, runs unprivileged, retires as root |
| `authorization_template_r3.json` | the coordinator record; a template authorizes nothing, and preflight proves the validator refuses it |
| `execution_pins_r3.json` | source, bridge, review, pointbank, GP-script, census and observable pins |
| `preflight_r3.py` | the bounded local self-test, P1–P11 |
| `seal_r3.py` | the deterministic sealer; `--verify` rebuilds the archive in memory and compares it to disk |
| `preregistration_r3.json` | immutable scope, claim firewall, stop conditions |
| `PAYLOAD.sha256`, `SOURCE_ARCHIVE.tar`, `SOURCE_ARCHIVE.sha256`, `SOURCE_SEAL.sha256` | the sealed deterministic source, 28 members (19 packet + 9 external) |
| `REVIEW_REQUEST.md` | the hostile review charge |

## AWS route

One `r6i.large` host labelled `r6b` with PARI/GP **2.15.4**, one effective core
(`AllowedCPUs=0`, `CPUAffinity=0`, all thread variables `1`, and a runner-side
`sched_getaffinity` check), `MemoryMax=1G`, `MemorySwapMax=0` with host
`SwapTotal` required to be `0`, `TasksMax=24`, `RuntimeMaxSec=300`, and a GP
subprocess timeout of 120 s. The whole job is seconds of work; the short
timeout is a containment property, not a budget.

Launch authority is the SHA-256 in the live EC2 tag
`jc2-d43-k0-field-cert-authorization-sha256`. Two further live tags,
`jc2-d43-k0-field-cert-job` and `jc2-host-label`, must read
`D43-K0-FIELD-CERT-R3` and `r6b`. There is no local-execution mode: absent a
live IMDSv2 identity the supervisor exits without running any mathematics.

**One authorization, one launch, ever**, now enforced on both sides of the
privilege boundary. Root mints at most one claim per authorization digest
(`spent/<digest>.spent`, `O_EXCL`, created first); the service takes at most
one consumption lease per authorization inside its own run directory
(`O_CREAT|O_EXCL`, taken last, after every precondition). Every custody step
sits outside the try block, so a refused launch writes no terminal at all. A
crashed or `NO_VERDICT` run therefore retires its authorization: a retry needs
a new coordinator record, a new digest and a new live tag. This is the direct
lesson of the R1 rehearsal, and the R2 review's REPAIR-1 is why it is now
executable rather than merely stated.

The R1 instance-type allowlist is gone: R2 pinned the single type the
rehearsal actually ran on, `r6i.large`, and R3 keeps it. The `gp` binary path and SHA-256 remain
coordinator-supplied and are verified against the on-disk binary;
`execution_pins_r3.json` records the hash observed on the (now terminated) R1
host for reporting only, and a mismatch is reported rather than gated.

## Replay

```
python3 cases/d43_k0_field_certificate_r3_20260829/seal_r3.py --root . --verify
python3 cases/d43_k0_field_certificate_r3_20260829/preflight_r3.py --root .
python3 -O cases/d43_k0_field_certificate_r3_20260829/preflight_r3.py --root .
python3 cases/d43_k0_field_certificate_r3_20260829/custody_selftest_r3.py
```

The first rebuilds the archive in memory and must report `ok: true` with every
entry of `matches_disk` true; the second and third must report
`preflight_pass: true` (there are no `assert` statements anywhere in the
packet, so `-O` cannot silence anything); the fourth runs the custody controls
alone and must report `ok: true`. Together they take under a minute and need
no AWS, no PARI, and no CAS. The custody controls refuse to run as root,
because root would bypass every permission denial they assert.

**What the custody controls do and do not execute.** They run the real
supervisor functions against real directories: real `lstat` results, real uid
and gid values, real POSIX mode bits, real `O_CREAT|O_EXCL`, real `EACCES` on
an unwritable directory, real `EPERM` on `chown` to root. The one thing an
unprivileged producer host cannot build is a *root-owned* object, so the
fixtures drive the same code through a `CustodyPolicy` whose custodian uid is
the running uid. That single seam is pinned separately: `production_policy`
is the only `CustodyPolicy` construction in the supervisor, it pins the
literal `custodian_uid=0`, and mutation `CM1` shows the pin is load-bearing.
The root-owned half is verified where root-owned objects exist, by
`--on-host-dry-run` before the unit starts.

## Claim firewall

This packet certifies a **coefficient-field theorem** plus an **E-conditional
ratio theorem**. It is not a D43 row certificate, not a point, not a template
or D25 result, not raw-J existence, not branch survival, not a Keller
statement, and not a JC2 result. It removes a coefficient-algebra prerequisite;
it supplies none. Nothing here bears on the 184-row packet's correctness, on
`V(Delta)` retention, on the tail-Jacobian drop locus, or on rail separation.
Nothing here asserts that the GP engine has ever run.
