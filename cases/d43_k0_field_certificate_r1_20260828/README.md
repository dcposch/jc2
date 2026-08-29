# D43 coefficient algebra `K0`: sealed exact field certificate, R1

**Status: `R1_SOURCE_READY_AWS_NOT_AUTHORIZED`.**
A different-model hostile source PASS and a coordinator GO are both required
before any execution. No AWS run, no PARI run, and no CAS run was performed
while producing this packet.

## What is certified

Two theorems, kept apart everywhere — in the gate typing, in the runner
terminal, and in the supervisor terminal.

**Unconditional (`K0_UNCONDITIONAL_THEOREM`, layers L0–L4).** `K0` is a number
field of degree exactly 432, Galois and non-abelian over `Q`. Its degree-48
base is exactly `Q(zeta_168)`. The two Kummer cubic classes are independent.
Its only idempotents are `0` and `1`; there is one factor. It is finite étale
of rank 432 over `Z[1/42]` and the ramified rational primes are exactly
`{2,3,7}`. Both registered frames are degree-1 primes and both primes split
completely with exactly 432 frames; the registered `p^2` frame is the unique
Hensel lift. This layer reads no `E`, no pointbank, no `nffactor`, and no
absolute primitive polynomial.

**Conditional (`E_CONDITIONAL_RATIO_THEOREM`, layer L5).** *Conditional on the
literal displayed* `E = (9+5*r3)*A1*W1^4 + (9-5*r3)*A2*W2^4`, the ratio
`W1/W2` is `K0`-rational: `q0 = u*(1+i)*(r3-1)/2` with `u = A2/A1` and
`i = r3*(1+2*zeta42^14)/3` solves `E` by direct substitution, and the four
branches `q0*i^k` are four distinct elements of `K0`. `E` is **not** re-derived
here; if the bridge's `E` is corrected, this layer must be recomputed and the
unconditional layer is untouched.

The charged theorem report is
`xmodel/d43-k0-splitting-primary-research-opus5-20260828.md`, SHA-256
`6d3d53c20387d324766daaf40eb502df42d9e2776c6ab6053041bc1f3dee1430`.

## Two genuinely independent engines

| engine | file | what it uses |
|---|---|---|
| PARI/GP 2.15.4 | `k0_field_cert_r1.gp` | `polcyclo`, `t_POLMOD`, `t_INTMOD`, `polrootsmod`, `Map` |
| stdlib Python | `k0_field_checker_r1.py` + `k0_algebra_r1.py` | explicit integer polynomials, explicit `F_p`, and a canonical 432-monomial normal form written from scratch |

Neither reads the other's output. They agree on **21 shared integer
observables**, emitted by GP as `OBS key value` lines and rebuilt
independently by the Python engine; `runner_r1.py` requires exact agreement on
every key and refuses on any disagreement. Neither engine's own PASS banner is
trusted: the runner counts all 79 printed GP gate flags itself and compares
the census line against the count.

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
the modular pointbanks. The `nffactor` block in the GP file is optional,
`alarm`-capped, and read by no verdict line. The pointbank regression is typed
`CORROBORATION` and feeds no theorem gate. The 432-frame count is typed
`CONSISTENCY ONLY`, because a totally split `L x L x L` with `[L:Q] = 144`
would produce the same 432.

The registered primes `105337` and `105673` are **character-silent**: both
`alpha_k` are cubes there, so their character pairs are trivial and they
annihilate all nine classes. The certificate gates this positively
(`KUMMER_SILENT_PRIME_GUARD`) and refuses to use them as certificate primes.

## Corrections to the charged report's illustrative GP recipe

Each is marked `[FIX n]` at its site in `k0_field_cert_r1.gp`.

1. **Variable collision.** The recipe built the tower as `Mod('x, polcyclo(168,'x))`
   and then substituted it into `P42`, a polynomial in the *same* variable `x`.
   The tower now lives in `y` and `P42` stays in `x`.
2. **Incomplete order test.** `z^42==1 && z^21!=1 && z^14!=1` omits the prime
   `7` of `42`. It therefore accepts elements of order 6:
   `zeta_168^28` passes all three tests. The corrected gate also demands
   `z^6 != 1`. `k0_mutations_r1.gate_unit_order42` executes exactly this
   counterexample and is a required unit test.
3. **`my()` scoping.** `my(r = ..., a = f(r))` evaluates `a`'s initialiser in
   the *enclosing* scope, where `r` is unbound. Both the character helper and
   the frame loop did this. Every `my()` now declares names only, at the head
   of its block, with plain assignments after.
4. **Double `Mod`.** `w = Mod(znprimroot(p), p)` wraps a `t_INTMOD` inside
   `Mod()`. The character layer no longer needs a generator at all.
5. **`P42'`.** Replaced by explicit `deriv(P42,'x)`.
6. **`chk()` accepted any nonzero object** as true, so a `t_POLMOD` or a
   `t_VEC` could pass silently. `chk()` now raises unless the value is a
   `t_INT`.
7. **No census.** Deleting a line turned a FAIL into a PASS. `chk()` now
   counts, the script prints `CENSUS n/nexpect`, and `preflight_r1.py`
   *statically* re-derives the expected count from the file itself.
8. **`nffactor` on the theorem path.** Moved to an optional, capped,
   corroboration-only block.

Two further defects were found in the report's *checker plan* and repaired
here rather than in GP: substituting `(q0, 1)` into `E` cannot see the exponent
on `W2` (both `1^4` and `1^2` are `1`), so `E_DIRECT_SUBSTITUTION` also
substitutes along the branch line `(q0*s, s)` at two invertible scales; and the
`q0` datum used by the E-layer is the *declared* one, not a value computed by
an earlier gate, so a perturbed coefficient is caught by the substitution
itself and not merely by a normal-form comparison.

## Mutation battery

`k0_mutations_r1.py`: **35 MUST_FAIL**, **2 MUST_SURVIVE**, 2 gate unit tests.
Each MUST_FAIL entry names the gate that has to report the failure; "something
failed" is not accepted. Every load-bearing datum is directly perturbed — the
source polynomial, the basis shape and rank, the discriminant, the `r3` and `h`
constructions, the order-test cofactor list, the generation exponent, the
certificate primes, the class generators and representatives, the ramified set,
the component and idempotent lists, both registered frames, the `p^2` frame,
the frame count, the `q0` coefficient and monomial, the `E` coefficient and
exponent, the two E-substitution scales, the branch count, and both
pointbank expectations. Deleting
`BASE_SURJECTIVE` or `E_DIRECT_SUBSTITUTION` from the census is itself a
MUST_FAIL entry, caught by `CENSUS_COMPLETE` and again by the runner's
comparison against the sealed census hash.

The two **MUST_SURVIVE** entries guard against a vacuous "all mutations fail"
harness:

* `M_CLASS_REP_EPS_SQUARED` — the charged report's own surviving mutation:
  `eps -> eps^2 = 7 + 4*sqrt3` is still a non-cube and still covers all eight
  classes, so the certificate must PASS;
* `M_CLASS_GENERATOR_BASIS` — generators `(alpha1, alpha1*alpha2)` are a
  different basis of the same `Delta`, and independence is basis-free.

A battery that reports either as a failure is miscoded.

## Files

| file | role |
|---|---|
| `k0_algebra_r1.py` | exact arithmetic: integer polynomials, `Q[x]/(Phi_168)`, canonical 432-monomial `K0`, scan-free `F_p` helpers |
| `k0_field_checker_r1.py` | 36 named fail-closed gates in five layers plus a census gate |
| `k0_field_cert_r1.gp` | the corrected PARI/GP engine, 79 gates, 21 observables |
| `k0_mutations_r1.py` | the hostile battery and the two gate unit tests |
| `runner_r1.py` | runs both engines, requires observable agreement, emits bounded immutable artifacts, replays the manifest and archive, writes one atomic terminal |
| `aws_supervisor_r1.py` | AWS custody: live IMDSv2 identity, tag-addressed authorization, host/instance/PARI-binary binding, cgroup-v2 one-core zero-swap contract, atomic-mkdir launch lease, one terminal |
| `aws_worker_r1.sh` | the environment-stripping exec shim |
| `systemd_unit_template_r1.service` | root-owned unit template; drop-ins forbidden |
| `authorization_template_r1.json` | the coordinator record; a template authorizes nothing |
| `execution_pins_r1.json` | source, pointbank, GP-script, census and observable pins |
| `preflight_r1.py` | the bounded local self-test, P1–P7 |
| `seal_r1.py` | the deterministic sealer; `--verify` rebuilds the archive in memory and compares it to disk |
| `preregistration_r1.json` | immutable scope, claim firewall, stop conditions |
| `PAYLOAD.sha256`, `SOURCE_ARCHIVE.tar`, `SOURCE_ARCHIVE.sha256`, `SOURCE_SEAL.sha256` | the sealed deterministic source, 21 members |
| `REVIEW_REQUEST.md` | the hostile review charge |

## AWS route

One `r6*.large`-class host labelled `r6b` with PARI/GP **2.15.4**, one
effective core (`AllowedCPUs=0`, `CPUAffinity=0`, all thread variables `1`,
and a runner-side `sched_getaffinity` check), `MemoryMax=1G`,
`MemorySwapMax=0` with host `SwapTotal` required to be `0`, `TasksMax=24`,
`RuntimeMaxSec=300`, and a GP subprocess timeout of 120 s. The whole job is
seconds of work; the short timeout is a containment property, not a budget.

Launch authority is the SHA-256 in the live EC2 tag
`jc2-d43-k0-field-cert-authorization-sha256`. Two further live tags,
`jc2-d43-k0-field-cert-job` and `jc2-host-label`, must read
`D43-K0-FIELD-CERT-R1` and `r6b`. There is no local-execution mode: absent a
live IMDSv2 identity the supervisor exits without running any mathematics.

**One open pin.** The exact EC2 instance type behind the label `r6b` is not
known to the producer, so the packet carries an allowlist
(`r6i.large`, `r6a.large`, `r6g.large`, `r6id.large`, `r6in.large`,
`r6idn.large`) and requires the authorization to name one that matches the
live IMDS value exactly. If the real host is outside that family the
coordinator must extend the allowlist, which is a source change and a new
R-number. The `gp` binary path and SHA-256 are likewise coordinator-supplied;
`runner_r1.py` refuses an unpinned binary.

## Replay

```
python3 cases/d43_k0_field_certificate_r1_20260828/seal_r1.py --root . --verify
python3 cases/d43_k0_field_certificate_r1_20260828/preflight_r1.py --root .
```

The first rebuilds the archive in memory and must report `ok: true` with every
entry of `matches_disk` true; the second must report `preflight_pass: true`.
Together they take a few seconds and need no AWS, no PARI, and no CAS.

## Claim firewall

This packet certifies a **coefficient-field theorem** plus an **E-conditional
ratio theorem**. It is not a D43 row certificate, not a point, not a template
or D25 result, not raw-J existence, not branch survival, not a Keller
statement, and not a JC2 result. It removes a coefficient-algebra prerequisite;
it supplies none. Nothing here bears on the 184-row packet's correctness, on
`V(Delta)` retention, on the tail-Jacobian drop locus, or on rail separation.
