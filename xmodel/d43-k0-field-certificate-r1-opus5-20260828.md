# D43 `K0` field certificate, R1 — producer report

**UTC:** 2026-08-28
**Role:** Opus 5, producer (continuation of my own theorem report; this is not a review)
**Packet:** `cases/d43_k0_field_certificate_r1_20260828/`
**Status:** `R1_SOURCE_READY_AWS_NOT_AUTHORIZED`

A different-model hostile source PASS and a coordinator GO are both required
before execution. No AWS run, no PARI/GP run, no CAS run, and no `jc2-lean`
access occurred while producing this packet. `gp` on this host is a shell alias
for `git push`; that is the same host condition the charged report recorded.

---

## 0. Custody

| file | SHA-256 |
|---|---|
| `xmodel/d43-k0-splitting-primary-research-opus5-20260828.md` (charged theorem) | `6d3d53c20387d324766daaf40eb502df42d9e2776c6ab6053041bc1f3dee1430` |
| `cases/d43_common_integral_emitter.py` | `5420b5c0b4164c719e98316cade96c094c2945a6fed8bad3ac0926771855984d` |
| `cases/d43_exact_sparse_rows_v2_20260828/selected_rows_v2.py` | `9fc9bd7a365827ddba2c1ba45cbb34870d6f2d71c9d3eecb6b242d46e00990b2` |
| `cases/d43_full_pointbank_p105337.pkl` | `bb0f13b61616c486116027e284483a4fb0f529f8df2dca7f728d56584d98fcbb` |
| `cases/d43_full_pointbank_p105673.pkl` | `b933cdb5b72bd4073da0cb82150db768f6b4607d5cd29d3d4aec0fe22ce5bcc3` |

All five recomputed on this host now and matching the charged report's §0 and
§8.3 tables. The charged theorem's hash matches the value in the charge.

---

## 1. What the packet is

Two engines, one runner, one supervisor, one atomic terminal that keeps the
unconditional theorem and the E-conditional theorem apart. Thirty-six named
fail-closed Python gates in five layers plus a census gate; seventy-nine GP
gates; twenty-one shared integer observables on which the two engines must
agree exactly; thirty-five MUST_FAIL mutations, two MUST_SURVIVE mutations,
and two gate unit tests.

The decisive design choice is that **Kummer independence is proved by explicit
cubic-character ring homomorphisms**, not by factorisation. For each certificate
prime `p ≡ 1 (mod 168)` the certificate exhibits actual roots `omega` of
`Phi_168 (mod p)` — each *is* a ring map `Z[y]/(Phi_168) → F_p` — covering both
square roots of 3, and then brute-forces the nine pairs `(i,j) ∈ (Z/3)^2` to
show only `(0,0)` annihilates both character pairs and that the pairs generate
`mu_3 × mu_3`. Two primes are used, `673` and `1009`, and each is independently
sufficient.

This makes the whole theorem path free of `nffactor`, of any absolute primitive
polynomial, of any degree-432 or degree-144 irreducibility claim, and of the
pointbanks. The `nffactor` block survives only inside an optional,
`alarm(600)`-capped GP tail that no verdict line reads.

Two typing decisions carried over from the charged report and enforced in code:
the 432-frame count is `CONSISTENCY` (a totally split `L × L × L` with
`[L:Q] = 144` gives the same 432), and the pointbank regression is
`CORROBORATION` (it must pass, but it feeds neither theorem verdict).

The certificate also gates *positively* that the registered primes `105337` and
`105673` are character-silent — both `alpha_k` are cubes there, so their
character pairs are trivial and they annihilate all nine classes — and refuses
to accept either as a certificate prime.

---

## 2. Corrections to the charged report's illustrative GP recipe

Eight defects, each marked `[FIX n]` at its site in `k0_field_cert_r1.gp`.

1. **Variable collision.** The recipe built the tower as
   `z = Mod('x, polcyclo(168,'x))` and then evaluated `subst(P42,'x,z42)`,
   substituting a `t_POLMOD` in `x` into a polynomial in the *same* variable
   `x`. The tower now lives in `y`; `P42` stays in `x`.
2. **Incomplete order test.** `z42^42==1 && z42^21!=1 && z42^14!=1` omits the
   prime `7` of `42`. It therefore accepts elements of order 6. This is not
   hypothetical: `zeta_168^28` has order 6, and
   `(z^28)^42 = z^1176 = 1`, `(z^28)^21 = z^84 = -1 ≠ 1`,
   `(z^28)^14 = z^56 ≠ 1` — it passes all three tests and fails the corrected
   `z^6 != 1`. `k0_mutations_r1.gate_unit_order42` executes exactly this
   counterexample as a required unit test, and `M_BASE_ORDER42_INCOMPLETE`
   mutates the cofactor list to `(2,3)` and requires the gate to fire.
3. **`my()` scoping.** `my(r = if(...), a = znlog(Mod(3+r,p)...))` evaluates
   `a`'s initialiser in the *enclosing* scope, where `r` is unbound. Both the
   `charvec` helper and the L4 frame loop had this. Every `my()` in the
   corrected file declares names only, at the head of its block, with plain
   assignments afterwards.
4. **Double `Mod`.** `w = Mod(znprimroot(p), p)` wraps a `t_INTMOD` inside
   `Mod()`. The corrected character layer needs no generator at all: it works
   with the literal values `alpha^((p-1)/3) ∈ mu_3(F_p)` and never takes a
   discrete logarithm. That also removes a real soundness wrinkle in the
   charged report — the printed exponents `(2,0),(0,2)` at `673` are
   generator-dependent (my own run of the same object printed `(1,0),(0,1)`),
   whereas the generated subgroup and the annihilator set are not.
5. **`P42'`.** Replaced by explicit `deriv(P42,'x)`.
6. **`chk()` accepted any nonzero object** as true, so a `t_POLMOD` or a
   `t_VEC` would have passed silently. It now raises unless the value is a
   `t_INT`.
7. **No census.** Deleting a line turned a FAIL into a PASS. `chk()` counts,
   the script prints `CENSUS n/nexpect`, and `preflight_r1.gp_static_census`
   re-derives the expected count *from the file* (68 static sites, three loops
   with trip count 2, giving 79) and compares it to the declared `nexpect`.
8. **`nffactor` on the theorem path.** Moved to the optional capped tail.

Two further defects were in the report's *checker plan*, not its GP, and are
repaired in the Python engine:

* **The `W2 = 1` blind spot.** The report's §9.3(4) asks for the direct
  substitution `E(q0,1) == 0`. That substitution cannot see the exponent on
  `W2`, because `1^4 = 1^2 = 1`. I found this when `M_E_EXPONENT`
  (`W2^4 → W2^2`) fired only `E_LITERAL_PIN`. `E_DIRECT_SUBSTITUTION` now also
  substitutes along the branch line `(q0*s, s)` at two nontrivial scales, which
  detects any loss of degree-4 homogeneity; the mutation now fires it.
* **The provenance of `q0`.** The E-layer must substitute the *declared* `q0`,
  not a value computed by an earlier gate, or a perturbed coefficient would be
  caught only by a normal-form comparison and never by the substitution itself.
  `Q0_NORMAL_FORM` now publishes the declared datum before comparing it to the
  independently computed one, and `M_Q0_COEFFICIENT` fires both gates.

One self-audit finding from writing the battery: the two homogeneity scales
were gate-body literals and therefore out of the battery's reach. They are now
`Spec.e_substitution_scales` with two mutations of their own. The review
request asks the reviewer to assume there are more such literals and to
enumerate them.

---

## 3. Gate inventory

| layer | gates | typing |
|---|---|---|
| L0 source and rank | `SRC_FILE_HASHES`, `SRC_PHI42_LITERAL`, `SRC_ALGEBRA_BLOCK`, `PHI42_DISCRIMINANT`, `PHI168_SHAPE`, `RANK432_MONIC_BASIS` | PIN, THEOREM |
| L1 base = `Q(zeta_168)` | `BASE_WELLDEFINED`, `BASE_I_SQUARE`, `BASE_ZETA8`, `BASE_SURJECTIVE`, `BASE_DIMENSION_48`, `BASE_CONDUCTOR_TOWER` | THEOREM |
| L2 Kummer | `KUMMER_HOMS_EXHIBITED`, `KUMMER_RANK_TWO`, `KUMMER_ALL_EIGHT_NONCUBES`, `KUMMER_REPRESENTATIVE_CLASSES`, `KUMMER_NORM_COROBORATION`, `KUMMER_SILENT_PRIME_GUARD` | THEOREM, SECOND_PROOF |
| L3 field, étale, ramification | `FIELD_DEGREE_432`, `IDEMPOTENTS_ONLY_0_1`, `GALOIS_STABILITY`, `NONABELIAN`, `ETALE_OVER_Z_1_42`, `RAMIFIED_EXACTLY_2_3_7` | THEOREM |
| L4 frames | `FRAME_RELATIONS`, `FRAME_ORDER_AND_JACOBIAN`, `SPLIT_COUNT_432`, `P2_HENSEL_REPLAY` | EXECUTED, CONSISTENCY |
| L5 E-conditional | `E_LITERAL_PIN`, `F_IDENTITIES`, `Q0_NORMAL_FORM`, `E_DIRECT_SUBSTITUTION`, `FOUR_K0_RATIONAL_BRANCHES`, `SIGMA_E_SYMMETRY`, `POINTBANK_REGRESSION` | CONDITIONAL, CORROBORATION |
| LZ | `CENSUS_COMPLETE` | HARNESS |

`unconditional_k0_theorem` is computed from L0–L4 with `CORROBORATION` gates
excluded; `e_conditional_ratio_theorem` from L5 the same way; both additionally
require `CENSUS_COMPLETE`. No L0–L4 gate reads `spec.e_terms`,
`spec.q0_terms`, or the pointbanks.

Some numbers the gates produce, all recomputed here from scratch and all
agreeing with the charged report: `disc(Phi42) = 205924456521 = 3^6·7^10` and
odd; `deg Phi_168 = 48` with `Phi_168(x) = Phi_42(x^4)`; the generation
identity `zeta8^5·zeta42^16 = zeta_168` with `21·5 + 4·16 = 337 ≡ 1 (mod 168)`;
character pairs at `673` and `1009` each generating an order-9 subgroup with
annihilator set `{(0,0)}`; trivial characters and all nine annihilators at both
registered primes; both frames satisfying all five relations with Jacobian
`(72846, 1590, 63015, 32307, 95731)` at `105337`; `12 × 2 × 18 = 432` at both
primes; all five `p^2` residues zero with correct reduction; `q0` normalising
to exactly the four terms

```
(0,0,2,1,0) : -5/6   (0,1,2,1,0) : 1/2   (7,0,2,1,0) : 2/3   (7,1,2,1,0) : -1/3
```

with denominators in `{2,3}`; four pairwise distinct branches; and the banked
ratios `7210` and `14755` landing on branch indices `3` and `0`.

---

## 4. Mutation battery

Thirty-five `MUST_FAIL` entries, each naming the gate that must report the
failure; "something failed" is not accepted. The perturbed data are the `Phi42`
tuple (last entry, and a monicity-preserving middle entry), the basis shape,
the declared rank, the discriminant, the `r3` exponents, the `h` halving
denominator, the order-test cofactor list, the `zeta8` exponent, the generation
exponent, the certificate prime list (silent prime, single prime), the class
generators, the class representatives (a cube, and a coverage gap), the
ramified set, the unramified witness, the component list, the idempotent list,
the degree, both registered frames, the `p^2` frame, the frame count, the `q0`
coefficient, the `q0` monomial, the `E` coefficient, the `E` exponent, the two
E-substitution scales, the branch count, and both pointbank expectations.
Deleting `BASE_SURJECTIVE` or `E_DIRECT_SUBSTITUTION` from the census is itself
a `MUST_FAIL` entry, caught by `CENSUS_COMPLETE` and again by the runner's
comparison against the sealed census hash.

Two `MUST_SURVIVE` entries, both of which the harness must **not** report as
failures:

* `M_CLASS_REP_EPS_SQUARED` — the charged report's own surviving mutation,
  `eps → eps^2 = 7 + 4·sqrt3`. Still a non-cube, and the representative list
  still covers all eight classes, so the certificate PASSes.
* `M_CLASS_GENERATOR_BASIS` — generators `(alpha1, alpha1·alpha2)`, a different
  basis of the same `Delta`. Independence is basis-free, so the certificate
  PASSes.

Two gate unit tests: `GATE_UNIT_ORDER42` (the order-6 element above) and
`GATE_UNIT_SOURCE_HASH` (one flipped nibble in a pinned source hash must fire
`SRC_FILE_HASHES`).

---

## 5. AWS route and terminal

`aws_supervisor_r1.py` has **no local mode**: absent a live IMDSv2 identity it
exits without running any mathematics. Launch authority is the SHA-256 in the
live tag `jc2-d43-k0-field-cert-authorization-sha256`, addressing a root-owned
`0444` coordinator record that must carry `coordinator_go = true` and a
`reviewer_pass` naming a model other than Opus 5. Two further live tags must
read `D43-K0-FIELD-CERT-R1` and `r6b`. The authorization must bind the exact
instance id, instance type, AMI, region, `gp` binary path and SHA-256, and
`gp_version = 2.15.4`; `runner_r1.py` refuses an unpinned `gp` binary and a
version banner other than `2.15.4`.

One core (`AllowedCPUs=0`, `CPUAffinity=0`, all thread variables `1`, plus a
runner-side `sched_getaffinity` check that the mask has exactly one CPU); zero
swap (`MemorySwapMax=0`, `memory.swap.events` must show no activity, and host
`SwapTotal` must be `0`); `MemoryMax=1G`, `TasksMax=24`, `RLIMIT_AS` 768 MiB;
`RuntimeMaxSec=300`, runner wall-clock cap 240 s, `gp` subprocess timeout
120 s. Artifacts are capped at 512 KiB each and 4 MiB per run, written once via
`O_EXCL` + `fsync` + `chmod 0444`, and never overwritten. The run path is
claimed by atomic `mkdir`, so a second launch is `DUPLICATE_LAUNCH` and a
crashed job downgrades to `NO_VERDICT` rather than re-running.

The runner replays every artifact against `manifest.json`, then rebuilds and
re-extracts `artifacts.tar` and checks every member's mode, mtime and digest,
before writing one atomic `terminal.json` whose two top-level verdicts are
`K0_UNCONDITIONAL_THEOREM` and `E_CONDITIONAL_RATIO_THEOREM`. The supervisor
independently re-replays the manifest and archive before installing its own
single `supervisor_terminal.json`.

Neither engine's PASS banner is trusted. The runner parses all 79 GP gate lines
itself and requires every printed flag to be `1`, requires the count to be 79,
requires the `CENSUS` line to agree, refuses any unparsed output line, and
requires exact agreement with the Python engine on all 21 observables.

Emission policy is enforced mechanically: `_component_policy` and
`_forbidden_language_scan` run over every artifact, and the only component list
that may be written is `["K0"]`, the only idempotent list `[0, 1]`, the only
component count `1`. `mutations.json` is scanned in `refusal_record` mode,
which permits the rejected inputs to appear inside `note`, `reason` and
`gate_errors` values and nowhere else — without that distinction the honest
record of `M_COMPONENT_PRODUCT` would have tripped the packet's own policy.

**One open pin, stated plainly.** I do not know which EC2 instance type the
label `r6b` denotes. The packet carries an allowlist (`r6i.large`, `r6a.large`,
`r6g.large`, `r6id.large`, `r6in.large`, `r6idn.large`) and requires the
authorization to name one that equals the live IMDS value exactly. If the real
host is outside that family the coordinator must extend the allowlist, which is
a source change and a new R-number. I did not invent a single type, because a
wrong exact pin would be worse than a declared allowlist.

---

## 6. Exact hashes

Packet: `cases/d43_k0_field_certificate_r1_20260828/`

| file | SHA-256 |
|---|---|
| `PAYLOAD.sha256` | `62d1bdec3de728f23b082875e5d765b2a0e985c85c57abd628a3a75db12dcf7a` |
| `README.md` | `7c21c7e07f8981162b58a46fc4bc3f16ed4b57fffc64e727b05fa7685095c5eb` |
| `REVIEW_REQUEST.md` | `d61e56aa890861ebbfcfe9a915a266822651d1b1e42557ff4eead319efbf6ce2` |
| `SOURCE_ARCHIVE.sha256` | `a86277657870ba39a4674742ec4a678b4c4885bdf703c7e2c9d2b48149c6f699` |
| `SOURCE_ARCHIVE.tar` | `e5d140db10194f1cab0812e3eaa003ca7aafd36a6e2b1fb11c153862975790b5` |
| `SOURCE_SEAL.sha256` | `583db53e641adfee8dec8cc3f5f4fc2c413b2f2651362790bea9d08dea5cb611` |
| `authorization_template_r1.json` | `fdd792457cfbcd720041ef80269adb664d4032147fb9f04a2aa8d498736bf164` |
| `aws_supervisor_r1.py` | `60885a5006e256ee6487a21056d09218c7581c34802b5a25f5bfb84d43508b6f` |
| `aws_worker_r1.sh` | `71d0316b5ed4bae41e9cc0c280a2ded75f646e7db8950cdf4b5e0af230093bd4` |
| `execution_pins_r1.json` | `2119bbc381a5342e67f30697cdf7d69cbd83788e337451989ee29241b5f240fb` |
| `k0_algebra_r1.py` | `ff58905ec0b8c3e576d3697c1f3ac42cbc4aa8f23285794c09493408d43b956b` |
| `k0_field_cert_r1.gp` | `fde358dcf28f419454d4e768e27cab39af888f18410a32a1498e7a40354c64c3` |
| `k0_field_checker_r1.py` | `095ddc6b9d714d128e27f1963fc7aa95a1dd97df18cc7da473c3216227a79b68` |
| `k0_mutations_r1.py` | `21daf08880d1eae24540c83d3adaa1b5f8bde9f8dcdd5be77006ec1c2fe0b72f` |
| `preflight_r1.py` | `94d61127439254a9aed3f0d0232ac4f88c0c01cb01cc7a604fcb963892ff7f0b` |
| `preregistration_r1.json` | `e4913a72921e13970bd98d99902a7f72dd3ab6743b60d907a897bff206b63ecf` |
| `runner_r1.py` | `8edf3cb674216a8f6574a40c2039e682a23045db31f17efc3e353ba6c0950b56` |
| `seal_r1.py` | `499408dd0e34894deca9a586bb3a579edd0e87d4b8a16a81fb5a8c83892ded87` |
| `systemd_unit_template_r1.service` | `51cac12ea9cbf29a5c16bee686b9dc4e1a2d501069743f1a620e724f90eba9b2` |

Sealed source archive: 21 members, `3143680` bytes, mode `0444`, SHA-256
`e5d140db10194f1cab0812e3eaa003ca7aafd36a6e2b1fb11c153862975790b5`.
Deterministic: PAX format, sorted repo-relative member names, uid/gid `0`,
empty uname/gname, mtime `0`, mode `0444`, regular files only.
`seal_r1.py --root . --verify` rebuilds it in memory and reports all four
`matches_disk` entries true.

Result hashes produced by the engines:

| object | SHA-256 |
|---|---|
| Python gate census (36 PASS gate names) | `2544c8cc0e5d6397c76bbc4d8149dc25b8f09637a6b4c0ef98b12cc9eb75422e` |
| shared observables (21 keys) | `e51ed0d2e9dfb41eee07baf51e50f4743db3849afc9b6ad32fc226652c8781e6` |
| mutation battery verdict vector | `9b9699551f775a4ee62e4ab60ed87fed8502b70cecaa9eccfb75c248a8104f1f` |

The first two are pinned in `execution_pins_r1.json`; `runner_r1.py` faults
with `CENSUS_DRIFT` or `OBSERVABLE_DRIFT` if the host reproduces anything else.

---

## 7. Bounded tests actually run

All on this host, stdlib Python only, exact arithmetic, seconds of wall clock.
`python3 cases/d43_k0_field_certificate_r1_20260828/preflight_r1.py --root .`
reports `preflight_pass: true` with:

* **P1** packet manifest: the 15 non-generated packet files (`PAYLOAD.sha256` excludes itself and the three other generated
  seal artifacts), 0 mismatched.  `SOURCE_SEAL.sha256` carries all 18 other
  packet files; the packet is 19 files.
* **P2** source archive: 21 members, 0 missing, 0 extra, 0 hash mismatches,
  archive digest verified; plus `seal_r1.py --verify` rebuilding the archive
  byte for byte in memory.
* **P3** GP static census: predicted `79` from 68 static `chk(` sites and three
  trip-count-2 loops, agreeing with the file's declared `nexpect = 79`; and
  predicted `21` observable emissions, agreeing with the Python engine's 21.
* **P4** Python engine: 36/36 gates PASS, `unconditional_k0_theorem` true,
  `e_conditional_ratio_theorem` true, `corroboration_ok` true.
* **P5** mutation battery: 35 MUST_FAIL all firing their named gates, 2
  MUST_SURVIVE both surviving, 2 gate unit tests PASS, 0 failed entries.
* **P6** pinned hashes: census, observable and GP-script hashes all matching
  their pins; observable count matching the GP prediction.
* **P7** emission policy: `components == ["K0"]`, `idempotents == [0,1]`,
  `component_count == 1`.

Separately executed while building the packet, and reproduced inside the gates:
`Phi_42` from `x^42-1` by exact division and its match to the emitter's literal
tuple; `Res(Phi42, Phi42')`; `Phi_168 = Phi_42(x^4)`; every Theorem A identity
in `Z[x]/(Phi_168)`; the character frames at `673`, `1009`, `105337`, `105673`;
both registered frames with Jacobians and 432-counts; the `p^2` Hensel replay;
every Theorem F identity in the canonical 432-monomial normal form, including
the direct substitution and the four branches; the `sigma` involution facts;
and both pointbank regressions read through a globals-refusing unpickler (the
pointbank files contain no pickle globals at all, which I verified by
`pickletools` opcode census before loading).

## 8. Recipes not run

* **`k0_field_cert_r1.gp` was never executed.** There is no PARI on this host.
  It was written, hand-reviewed against the eight defects above, and
  statically census-audited by P3 — nothing more. Its correctness as *PARI*
  is an open item for the reviewer, and the review request lists the five
  constructs I reasoned about but did not observe (`Mat(t_MAP)`,
  `polrootsmod` returning `t_INTMOD`, `Set` returning objects not strings, the
  `chk` type guard, and the loop trip counts). If the file does not run, the
  Python engine still stands alone, but the terminal's two-engine claim would
  be false and must not be emitted.
* **The optional `nffactor` corroboration block** was never run anywhere.
* **`runner_r1.py`, `aws_supervisor_r1.py`, `aws_worker_r1.sh` and the systemd
  unit were never executed.** They are syntax-checked only. Their custody
  logic — IMDSv2, cgroup v2, cpuset, swap events, service user, atomic mkdir
  lease — is Linux-only and unobservable from this host.
* **No AWS call of any kind was made**, and no authorization record exists.
  `authorization_template_r1.json` has `status: TEMPLATE_NOT_AUTHORIZED` and
  `coordinator_go: false`, and the supervisor refuses it.
* The instance type behind `r6b` is unresolved; see §5.

## 9. Claim firewall

This packet certifies exactly two things, and they are separated in the gate
typing, in the runner terminal, and in the supervisor terminal:

1. a **coefficient-field theorem** — `K0` is a number field of degree exactly
   432, Galois and non-abelian over `Q`, with base `Q(zeta_168)` of degree 48,
   independent Kummer classes spanning `(Z/3)^2`, one factor and only the
   idempotents `0` and `1`, finite étale of rank 432 over `Z[1/42]`, ramified
   rational primes exactly `{2,3,7}`, both registered primes splitting
   completely with 432 frames, and a unique `p^2` Hensel lift; and
2. an **E-conditional ratio theorem** — conditional on the literal displayed
   `E = (9+5*r3)*A1*W1^4 + (9-5*r3)*A2*W2^4`, which I did not re-derive, the
   ratio `W1/W2` is `K0`-rational with the four explicit branches `q0*i^k`.

It is **not** a D43 row certificate, not a point, not a template or D25 result,
not raw-J existence, not branch survival, not source/parked equivalence, not a
`Z_p` or characteristic-zero point, not a formal germ, not an ambient Keller
map, and not a JC2 result. It removes a coefficient-algebra prerequisite; it
supplies none. If the bridge's `E` is later corrected, layer L5 must be
recomputed and layers L0–L4 are untouched.
