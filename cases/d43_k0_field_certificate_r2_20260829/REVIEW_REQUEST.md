# Hostile review request — D43 `K0` field certificate, R2

**Requested verdict:** `PASS` / `PASS WITH REPAIR` / `FAIL`, on the *source*.
**Reviewer constraint:** must be a **different model** from the producer
(Opus 5). Your report's SHA-256 and your model name go into the authorization
record; `aws_supervisor_r2.validate_authorization_record` refuses any model
name that normalises to contain `opus`, and requires the verdict field to read
exactly `PASS`.

**Status you are reviewing:** `R2_SOURCE_READY_AWS_NOT_AUTHORIZED`. Nothing has
been executed on AWS and **no PARI/GP run of this file exists anywhere**. Do
not treat a PASS as a launch: the coordinator GO is separate.

## What changed since R1, and what that means for you

R1 was reviewed by Fable 5
(`xmodel/d43-k0-field-certificate-r1-hostile-review-fable5-20260829.md`,
`29e9496e0552f94d6823c744b7b979ad02274e6cbf39ae124ec01e6465d596e2`, verdict
`PASS_FOR_PINNED_GP_REHEARSAL`). The rehearsal it licensed failed closed
before either engine: `python3 -I` omitted the script directory from
`sys.path`. R2 repairs that and the review's D1–D13. **Please do not assume
the R1 review's PASS transfers.** Every gate that R1's reviewer found vacuous
has been rewritten, and the rewrites are new code that has never been
reviewed.

The README's defect table is the producer's claim about those repairs. Treat
it as an allegation.

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

Read every gate in `k0_field_checker_r2.py` and every `chk(`/`chkE(` in
`k0_field_cert_r2.gp` and ask of each: *what input makes this print 0?* R1's
reviewer found `RANK432_MONIC_BASIS`, `GALOIS_STABILITY`, `NONABELIAN`, five
of six `BASE_CONDUCTOR_TOWER` needs, the `eps` embedding line, the
within-fibre character test and the `(0,0)` representative need. I believe
each of those is now either computed or deleted. Find the ones I missed.
Candidates I am least confident about:

* `L1 CRT` — retained deliberately (see the README). Is that defensible?
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

There is no `gp` on the producer host. `k0_field_cert_r2.gp` has been
**hand-reviewed and statically census-audited only**. Please either run it on
a PARI 2.15.4 host or read it as an adversary. New risk points relative to R1:

* `matrix(m,n,i,j,expr)` with `t_INTMOD` entries and `matdet` over `F_p`;
* `polrootsmod` on the non-monic `HB*'t^2 - HC` and on `'t^3 - (3±r)`;
* the multivariate `subst` chain in `sg(f)`, including the temporary variable
  `'tw`, and whether polynomial `==` after that chain is canonical;
* `select(u -> u == 2, vector(...))` — a closure, which R1 did not use;
* `chkE` as a second accumulator, and whether the census still counts every
  printed line exactly once;
* whether the predicted count 110 and the declared `nexpect = 110` agree with
  what GP actually prints — both are my arithmetic, and
  `preflight_r2.gp_static_census` is my predictor.

If the GP file does not run, that is a repair, not necessarily a FAIL: the
Python engine is independent and complete for the unconditional layer. But the
*two-engine* claim in the terminal would then be false, and the terminal must
not say it.

### G. Custody and the terminal

* `emit_immutable` now creates the final name with `O_CREAT|O_EXCL`. Check
  there is no remaining window, and that a crash mid-write is caught by the
  manifest replay.
* `claim_authorization_lease` runs before `claim_run_path` and both are
  outside the try block. Convince yourself a second presentation of the same
  authorization can produce no terminal, and that the lease path cannot be
  spoofed by a run path whose parent is not root-owned.
* `validate_authorization_record` is a pure function; preflight P9 runs 33
  cases against it. Find a record that should be refused and is not.
* The instance type is now a single exact value. Decide whether that is right
  or whether it will simply block the next rehearsal.
* `_forbidden_language_scan` still uses `\bK_?[1-9]\d*\b`. Check it does not
  false-positive on the new artifacts (the battery now carries 62 entries) and
  does not miss an obvious evasion.

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

The packet's own file hashes are in `PAYLOAD.sha256` and `SOURCE_SEAL.sha256`;
the deterministic source archive is `SOURCE_ARCHIVE.tar` with its hash in
`SOURCE_ARCHIVE.sha256`.

The R1 rehearsal's three harvested terminal records live under
`cases/d43_k0_field_certificate_r1_20260828/custody/ephemeral_20260829T010727Z/terminal/`.
They are evidence about R1 and are not part of this packet's seal.

## How to replay everything the producer ran

```
cd <repo root>
python3 cases/d43_k0_field_certificate_r2_20260829/seal_r2.py --root . --verify
python3 cases/d43_k0_field_certificate_r2_20260829/preflight_r2.py --root .
```

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
