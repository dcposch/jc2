# Hostile review request — D43 `K0` field certificate, R1

**Requested verdict:** `PASS` / `PASS WITH REPAIR` / `FAIL`, on the *source*.
**Reviewer constraint:** must be a **different model** from the producer
(Opus 5). Your report's SHA-256 and your model name go into the authorization
record; `aws_supervisor_r1.py` refuses an authorization whose
`reviewer_pass.model` is Opus 5.

**Status you are reviewing:** `R1_SOURCE_READY_AWS_NOT_AUTHORIZED`. Nothing has
been executed on AWS and no PARI/GP run exists anywhere. Do not treat a PASS as
a launch: the coordinator GO is separate.

## What you are asked to decide

1. Does the **unconditional** layer (L0–L4) actually prove what the terminal
   says it proves, using only what it executes?
2. Is the **conditional** layer (L5) correctly quarantined, so that a wrong `E`
   cannot contaminate the unconditional verdict?
3. Can the certificate pass while being wrong — i.e. is there a gate that
   cannot fail, a mutation that should fail and does not, or a conclusion that
   is asserted rather than computed?

## Specific attacks I want you to run

### A. The Kummer layer is the only thing standing between 432 and 144

`KUMMER_RANK_TWO` is the load-bearing gate for the degree. Attack it:

* The argument needs each root `omega` of `Phi_168 (mod p)` to induce a ring
  map on which the classes are units, and needs a valuation argument
  (`v_P(alpha_k) = 0` for `P` over `p` not dividing `6`) to descend a cube root
  `x in B^*` into the local ring. **That valuation step is prose in this
  README, not a gate.** Decide whether the certificate is entitled to it, and
  whether it should be replaced by something executable.
* The step from "48 roots of `Phi_168 (mod p)` give ring maps `Z[y]/(Phi_168)
  -> F_p`" to "primes of `O_B`" uses `Z[zeta_n] = O_{Q(zeta_n)}`. That is a
  standard theorem but it is **cited, not checked**. Is citing it acceptable
  here, and does anything cheaper work?
* Confirm the annihilator computation is genuinely basis-free. I claim the
  verdict is invariant under replacing the primitive cube root of unity `w` by
  `w^2`; the charged report prints exponents `(2,0),(0,2)` at `673` while my
  local run of the same object printed `(1,0),(0,1)`, precisely because of that
  choice. If you find any residual dependence on a generator, that is a FAIL.

### B. Gates that might not be able to fail

Read every gate in `k0_field_checker_r1.py` and every `chk(` in
`k0_field_cert_r1.gp` and ask of each: *what input makes this print 0?* I have
already removed two tautologies (`1 == 1` for the component count, `[0,1] ==
[0,1]` for the idempotents) by routing them through the mutable `COMPONENTS`
and `IDEMPOTENTS` data. Look for the ones I missed. Candidates I am least
confident about:

* `L1 CRT 21*5 + 4*16 == 1 mod 168` — is this doing work, or is it restating
  the exponents it reads?
* `L3 [K0:B]*[B:Q] == 9*48 == declared rank` — the `9` is a literal. Where does
  the certificate *compute* `[K0:B] = 9` rather than assert it?
* `BASE_DIMENSION_48` and `FIELD_DEGREE_432` — both are arithmetic on numbers
  established elsewhere. Is the chain L1(freeness) + L2(Kummer) -> degree 432
  actually gated end to end, or is there a step that only lives in prose?
* `RANK432_MONIC_BASIS` normalises each of the 432 monomials and each of the 5
  relations. Does that actually certify freeness of rank 432, or only that the
  rewriting has the claimed normal forms? If the latter, say so and tell me
  what the gate is worth.

### C. The mutation battery

* Verify that each of the 35 `MUST_FAIL` entries fires **its named gate**, not
  merely something. Re-run with `k0_mutations_r1.py` and read
  `gate_errors` for each.
* Verify the 2 `MUST_SURVIVE` entries survive for the *right* reason. If
  `M_CLASS_GENERATOR_BASIS` survives because the generators are never really
  used, that is a hole, not a feature.
* Find a load-bearing datum I did **not** mutate. `Spec` is the complete list
  of what the battery can reach; anything load-bearing that is a literal inside
  a gate body instead of a `Spec` field is out of the battery's reach and is a
  defect. I found one this way — the two homogeneity scales used by
  `E_DIRECT_SUBSTITUTION` were gate-body literals — and lifted them into
  `Spec.e_substitution_scales` with two mutations of their own. Assume there
  are more. Enumerate every literal appearing inside a gate body and decide,
  one by one, whether it is load-bearing.
* Construct a *new* surviving mutation and check the harness does not reject
  it.

### D. The GP file, which I could not execute

There is no `gp` on the producer host. `k0_field_cert_r1.gp` has been
**hand-reviewed only**. Please either run it on a PARI 2.15.4 host or read it
as an adversary. Known risk points, all of which I reasoned about but did not
observe:

* `Mat(t_MAP)` returning a 2-column key/value matrix, and `#M[,1]`;
* `polrootsmod` returning `t_INTMOD`s in 2.15.4;
* `Set(...)` returning objects rather than strings in 2.15.4, so
  `Set(factor(n)[,1]~) == Set([3,7])` is a comparison of integer vectors;
* whether `chk`'s `type(val) != "t_INT"` guard rejects anything the script
  legitimately produces (a false alarm would make the whole file abort);
* whether the three `for` loops' trip counts are what
  `preflight_r1.gp_static_census` assumes — the predicted count 79 and the
  declared `nexpect = 79` agree, but both are my arithmetic.

If the GP file does not run, that is a repair, not necessarily a FAIL: the
Python engine is independent and complete. But the *two-engine* claim in the
terminal would then be false, and the terminal must not say it.

### E. Custody and the terminal

* `runner_r1.py` writes artifacts `0444` after `fsync` and refuses to
  overwrite. Check `emit_immutable` for a TOCTOU window and check that the
  `.tmp` suffix cannot collide with a real member.
* The archive replay compares each member against `artifacts.get(m.name) or
  artifacts_manifest_sha`. Convince yourself that `or` cannot silently accept a
  wrong hash for a member whose name is absent from `artifacts`.
* `publish_terminal` is the single writer. Check that the fault path cannot
  also produce a runner terminal, and that `DUPLICATE_LAUNCH` really is
  unreachable twice.
* The supervisor's instance-type allowlist is a **provisional pin** (see the
  README's "One open pin"). Decide whether an allowlist is acceptable custody
  or whether R2 must carry a single exact type.
* `_forbidden_language_scan` uses a regex `\bK_?[1-9]\d*\b`. Check it does not
  false-positive on legitimate content and does not miss an obvious evasion.

### F. Claim discipline

The terminal must keep two things apart. Check that:

* no unconditional gate reads `spec.e_terms`, `spec.q0_terms`, or the
  pointbanks;
* `unconditional_k0_theorem` in `k0_field_checker_r1.run` is computed from
  layers L0–L4 only, and the `CORROBORATION`-typed gate is excluded from both
  theorem verdicts but still required to pass overall;
* nothing anywhere claims a D43 row, point, template, D25, raw-J, Keller or
  JC2 result, and nothing claims the 432-frame count proves fieldness.

## Frozen inputs

| file | SHA-256 |
|---|---|
| `xmodel/d43-k0-splitting-primary-research-opus5-20260828.md` | `6d3d53c20387d324766daaf40eb502df42d9e2776c6ab6053041bc1f3dee1430` |
| `cases/d43_common_integral_emitter.py` | `5420b5c0b4164c719e98316cade96c094c2945a6fed8bad3ac0926771855984d` |
| `cases/d43_exact_sparse_rows_v2_20260828/selected_rows_v2.py` | `9fc9bd7a365827ddba2c1ba45cbb34870d6f2d71c9d3eecb6b242d46e00990b2` |
| `cases/d43_full_pointbank_p105337.pkl` | `bb0f13b61616c486116027e284483a4fb0f529f8df2dca7f728d56584d98fcbb` |
| `cases/d43_full_pointbank_p105673.pkl` | `b933cdb5b72bd4073da0cb82150db768f6b4607d5cd29d3d4aec0fe22ce5bcc3` |

The packet's own file hashes are in `PAYLOAD.sha256` and `SOURCE_SEAL.sha256`;
the deterministic source archive is `SOURCE_ARCHIVE.tar` with its hash in
`SOURCE_ARCHIVE.sha256`.

## How to replay everything the producer ran

```
cd <repo root>
python3 cases/d43_k0_field_certificate_r1_20260828/seal_r1.py --root . --verify
python3 cases/d43_k0_field_certificate_r1_20260828/preflight_r1.py --root .
```

The sealer must report `ok: true` with all four `matches_disk` entries true;
if it does not, the packet you are reading is not the packet that was sealed
and you should stop and say so.

Expect `preflight_pass: true`, 36/36 Python gates, 35 MUST_FAIL + 2
MUST_SURVIVE + 2 gate unit tests, GP static census `79/79`, observables
`21/21`, census SHA-256
`2544c8cc0e5d6397c76bbc4d8149dc25b8f09637a6b4c0ef98b12cc9eb75422e`, observable
SHA-256 `e51ed0d2e9dfb41eee07baf51e50f4743db3849afc9b6ad32fc226652c8781e6`.
Runtime is a few seconds; nothing here needs AWS, PARI, or a CAS.
