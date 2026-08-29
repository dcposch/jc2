# D43 `K0` field certificate R2 — hostile source review (Fable 5)

**Verdict: `PASS WITH REPAIR`**

**UTC:** 2026-08-29 (host clock 2026-08-28 local)
**Reviewer:** Fable 5 (model id `claude-fable-5`), independent of the R2 producer (Opus 5)
**Object:** `cases/d43_k0_field_certificate_r2_20260829/`, status `R2_SOURCE_READY_AWS_NOT_AUTHORIZED`
**Charge:** that packet's `REVIEW_REQUEST.md` (SHA-256 `f77f8cf411dd5c6f3b5a5448730d91653f66cebc3ce93f68348fa25dea825dfa`)

## What this verdict licenses, exactly

* It licenses **nothing on AWS**. The supervisor's `validate_authorization_record`
  requires the verdict field to read exactly `PASS`; this report's verdict is
  `PASS WITH REPAIR` and therefore **cannot enter an authorization record**.
  Any authorization citing this report's hash must be refused.
* It records that the **mathematical and harness content of the R2 packet is
  confirmed**: every allegation in the review request that I could execute or
  hand-audit came back true, all 13 R1 defects (D1–D13) are genuinely repaired,
  the mutation battery is honest, the layer separation is watertight at the
  harness level, and I found **no path to a wrong PASS** in either engine.
* It requires **one repair before any launch authorization** (REPAIR-1 below):
  the new authorization-lease custody path is unexecutable as shipped and
  guarantees the next rehearsal fails closed before any mathematics — the same
  failure class as the R1 `-I` import fault, introduced in new R2 custody code.
  The repair touches only `aws_supervisor_r2.py` /
  `systemd_unit_template_r2.service` semantics (plus a preflight control for
  it); the mathematics, both engines, the battery, and the seal discipline need
  no change. A repaired packet (fresh seal, fresh R-number or amended packet
  per house rules) needs a fresh different-model review of the changed custody
  surface before its authorization; the mathematical layers may cite this
  review as already-confirmed.
* The GP engine **has still never been parsed by any GP**; nothing here
  changes that, and no PASS of any kind should be read as evidence the GP file
  runs.

---

## 1. Execution gap, stated first

There is no PARI/GP on this host (`command -v gp` resolves to a shell alias
for `git push`; no PARI binary exists). Following the charge I did **not**
install one. `k0_field_cert_r2.gp` was reviewed **by adversarial source
reading and static census only** (§7). Every statement below about GP is a
statement about source text and about PARI 2.15 documented semantics from
knowledge, not about an execution. The producer's identical disclosure
(README, preregistration, preflight report) is accurate and consistently
maintained; nothing in the packet claims the GP engine has run.

Everything else charged was executed: the sealer verification, the full
preflight under normal Python **and** `python3 -O`, the full mutation battery
standalone under both modes, and my own independent fixtures (§5, §6, §8).

## 2. Charged inputs, verified byte-exact

All eight frozen externals match the review request's table (recomputed with
`shasum -a 256`):

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

All 19 packet files match the producer report §2.1 byte for byte; the four I
charge below are the ones a follow-up must treat as load-bearing:

```
k0_algebra_r2.py        a7de3c3fcefc42302e402b8dfcaeefbba6d5a582ae694447e8f95f6a8e8dd4a6
k0_field_checker_r2.py  14650a3d473477423434763e0d2c0528914b5a4357cf4db2e6e9daf588761251
k0_field_cert_r2.gp     c3f576dd5bbc1c0af970246379c97d1c541daa7ae521f722ed43f905e4713d76
k0_mutations_r2.py      45ae1eeb8d70c1fa55ce9cf8ac359ec91a19581f8901c3c57f1e245c019d6650
runner_r2.py            c0866be32c54465ce581de51fefddb467bad9a8678c4ea67c6c661150cc0139a
aws_supervisor_r2.py    55f43cdc1f11c297c491b48a99f59057a92dcd01638ccc40fea440d2de1aa0b6
preflight_r2.py         02cf8950a5d24445bd1dd328c2e45207955d98eea698392c56461997a785641a
seal_r2.py              c3fa02b1f671a891b184ba20249641f6f24c70382909fe83cb98537512256edf
PAYLOAD.sha256          8bfdd426990a3891fde526336fc26585ad46d912d8fcb3a8951dc97019e5526d
SOURCE_ARCHIVE.tar      569bb51cad8d64749cc7f1b911ccb849f315c4db4634beee4472ee9f9f63c685
SOURCE_ARCHIVE.sha256   561dea8d7a58a7c64dd5fe6613e39eb394bd9f44af012308ffb1ad9af1c374d6
SOURCE_SEAL.sha256      69279ae99c9a3a35c31b536f62b31970fba1b7997f5ef092ae97ecd9d8f47f34
```

## 3. Replication record (commands and counts)

* `python3 seal_r2.py --root . --verify` → `ok: true`, 24 archive members,
  all four `matches_disk` true, archive `569bb51c…`, payload `8bfdd426…`.
* `python3 preflight_r2.py --root .` → `preflight_pass: true`, rc 0, 6.5 s.
  P1 15/15; P2 24/24; P3 predicted **110 = declared 110**, 99 static sites, 13
  loops, 0 unresolved, 29 predicted observables, hygiene 0/13 forbidden
  constructs, 99 labels max width 63 ≤ 80, ASCII, tab-free; P4 **42/42**
  gates, `theorem_inputs` pairwise disjoint; P5 **58 MUST_FAIL + 4
  MUST_SURVIVE + 19 separation controls + 5 unit tests, 0 failed**, separation
  census `{uncond_true_e_false: 8, both_true: 8, uncond_false: 46}`; P6 all 8
  booleans true; P7 CLEAN; P8 8/8; P9 33 records + template refusal + 3
  collision + 2 reuse assertions; P10 10/10.
* `python3 -O preflight_r2.py --root .` → identical `preflight_pass: true`.
  I additionally grepped all six Python files for `assert` statements: **none
  exist**, so `-O` cannot silence anything.
* Standalone battery replay (my own path-loader, outside the packet dir),
  normal and `-O`: `battery_pass: true` both, byte-identical output except the
  optimize flag, `battery_sha256 e416de0e074cc0125ac2419a724c420d0d5f9c4dcd141abbd276f477bafbc25b`
  = the producer's pin. Programmatic check over all 58 MUST_FAIL entries:
  **every one fires its named gate** (empty "did not fire" list); sampled
  `gate_errors` verbatim carry the intended reasons (e.g. `M_SIGMA_NO_SWAP` →
  `GALOIS_STABILITY_FREE: sigma sends relation 2 outside the relation set`,
  `M_E_EXPONENT` → three gates including the scale-probe homogeneity message).
* Pinned run values reproduce: census
  `b828f93d6a29c15371e4d277473e63c0a25ba0280fa5ab44706d10c786f9aeb0`,
  observables
  `4b1c7ff63935adb27148a2967037b7a357354848b0bbc2f0df827db2e45148f6`,
  GP script `c3f576dd…`.

## 4. REPAIR-1 (required): the authorization lease cannot be taken by the service user

`aws_supervisor_r2.claim_authorization_lease` (new in R2) does, in order:

1. `require_root_owned_immutable(run_path.parent)` — the run parent must be
   **owned by uid 0** and have **no group or world write bit** (and likewise
   all its ancestors);
2. `os.open(parent/.jc2-k0-r2-authorization-<digest>.lease, O_CREAT|O_EXCL)` —
   i.e. it must **create a file in that directory**.

The process is required to run as `jc2k0` (`SERVICE_USER` gate), and the unit
template sets `User=jc2k0`, `CapabilityBoundingSet=` (empty),
`AmbientCapabilities=` (empty), `NoNewPrivileges=yes`. Creating a directory
entry requires write permission on the directory; for a root-owned directory
with no group/world write bit, only root has it, and the empty capability set
excludes `CAP_DAC_OVERRIDE`. A POSIX ACL granting jc2k0 write is also
excluded, because the ACL mask surfaces in the group-class permission bits
that `require_root_owned_immutable` rejects. **The two requirements are
jointly unsatisfiable.** The unit's own comment ("the run parent must be
writable because the supervisor takes its authorization lease there") plus
`ReadWritePaths=<ABSOLUTE_RUN_PARENT_DIRECTORY>` show the producer intended
write access, but `ReadWritePaths` only lifts the `ProtectSystem=strict`
mount-level read-only remount; it grants no DAC permission.

Evidence that this bites in practice: the harvested R1 rehearsal records show
run path `/var/lib/jc2-k0/run-20260829T010727Z`, and R1's `claim_run_path`
(no ownership check) successfully `mkdir`ed it as jc2k0 — so the real run
parent **is** service-user-writable, i.e. it fails R2's
`require_root_owned_immutable` (`PATH_OWNER` if jc2k0-owned, `PATH_MODE` if
root-owned group-writable). Concretely, on the next rehearsal:

* if the parent is left as in R1: clean `CUSTODY_FAULT PATH_OWNER`, rc 70,
  no lease taken, no terminal, no mathematics;
* if ops "fix" it to root-owned 0755: `os.open` raises `PermissionError`,
  which is **not caught anywhere** (`claim_authorization_lease` catches only
  `FileExistsError`; `main` catches only `CustodyFault`) → raw traceback,
  exit 1; and `claim_run_path.mkdir` would fail identically one line later.

In both branches the failure is **before either lease exists**, so the
authorization is *not* consumed and the fail-closed property holds — no wrong
verdict, no terminal, no reuse hazard. But the packet's only purpose after a
PASS is a successful rehearsal, and this defect guarantees another burned
rehearsal attempt in brand-new, **never-executed-anywhere** custody code:
`preflight_r2.py` P9 never calls `claim_authorization_lease`,
`claim_run_path`, or `require_root_owned_immutable` (grep: zero references).
That is the same "integration defect that fails closed before any
mathematics" class as the R1 `-I` fault, which is why it is a required repair
and not a note.

**Repair shape (producer's choice, but it must be executable and tested):**
either (a) relax the lease-parent policy to "owned by root **or** by the
dedicated service user, not group/world-writable" (the lease still cannot be
spoofed: an attacker would need to *be* jc2k0 or root), or (b) keep the
root-owned policy and have root (e.g. `ExecStartPre=+…`) pre-create a
jc2k0-owned lease+run subdirectory one level down and point `run_path` there,
with the root-owned check applied to *its* parent. Either way, add a
preflight control that exercises the lease claim end-to-end as a non-root
user against both an owned and an unowned parent fixture.

## 5. The unconditional mathematics, gate by gate (all confirmed)

Registry shape verified: 42 gates = L0 (3 PIN + 4 THEOREM + 1 EXECUTED),
L1 (6 THEOREM), L2 (5 THEOREM + 1 SECOND_PROOF), L3 (6 THEOREM),
L4 (3 EXECUTED + 1 CONSISTENCY), L5 (2 CONDITIONAL_PIN + 6 CONDITIONAL +
1 CORROBORATION), LZ (3 HARNESS). Grep-verified: **no L0–L4 gate reads
`spec.e_terms`, `spec.q0_terms`, or the pointbanks** — those appear only in
`_E`/`_E_mod`, the five L5 sites, and `POINTBANK_REGRESSION`.

**A. `RELATION_LEADING_TERMS` (the rank-432 theorem gate).** Audited in
full. `grlex_key = (total degree, lex tuple)` is a genuine monomial order
(translation-invariant, degree-dominant, well-order). The gate computes — in
the free ring, where nothing is reduced — the leading monomial of each of the
five relations, requires it to be a pure power of its own generator with
exponent `basis_shape[k]` (so `z^12` beats the degree-≤11 tail of any monic
degree-12 datum, `A1^3` beats `r` of degree 1, `r^2`/`h^2` beat constants),
requires pairwise coprimality, and requires every tail monomial to be
reduced. Pairwise coprime leading monomials satisfy Buchberger's first
criterion over the field Q (leading coefficients, including the non-monic 2
on `2h^2−3`, are irrelevant to it), so the five relations are a Gröbner
basis of the ideal they generate and the standard monomials — exactly the
12·2·3·3·2 box — are a Q-basis of the quotient. That is a complete
executable proof of freeness of rank 432 for the declared presentation.
The deliberate blindness to *which* monic degree-12 `Phi_42` is used is
honestly documented and is covered: `SRC_PHI42_LITERAL` both compares to the
sealed emitter literal **and recomputes `Phi_42` from `x^42−1` by exact
division**, `PHI42_DISCRIMINANT` recomputes `3^6·7^10` by resultant, and the
independence witness forces the 12 z-points to be primitive 42nd roots of
unity that are roots of the datum. P10's `x^12+5` probe (leading-term gate
passes, the other three fail) executed as claimed.

**B. `RANK432_INDEPENDENCE` (the mod-p witness).** The completeness argument
is sound and I verified it two independent ways. In a field, `r^2 = 3` has at
most 2 roots, and each `x^3 = c` (c ≠ 0) has 0 or 3; the gate exhibits 18
*distinct* verified points, hence the complete set. My independent check
(own code, no packet imports): exhaustive scan over all of `F_105337` finds
exactly 2 r-roots {795, 104542}, exactly 18 (r,A1,A2) points, exactly 2
h-roots, exactly 12 roots of `Phi_42`. The Kronecker factorisation is
correct with the column index `j−1 = 9b + 3c + d` used identically by the
Python row builder and the GP `matrix` expression; nonsingularity of the
three blocks is equivalent to nonsingularity of the 432×432 evaluation
matrix; squared determinants are row-order invariant, so the two engines'
different row orders (sorted vs `polrootsmod`/loop order) cannot disagree.
My independently recomputed values: **`det_z² = 101851`, which equals
`disc(Phi_42) = 3^6·7^10 = 205924456521 mod 105337` exactly** (the
closed-form Vandermonde identity — an independent confirmation the z-block
is the full root set), `det_mid² = 35131`, `det_h² = 6 = disc(h²−3/2)`.
All three match both the checker's observables and the producer's claims.
The GP route (`polrootsmod` + `sqrt(Mod(3,p))` + `μ3` from cubic roots)
constructs the same *sets*, so the engines cannot produce different squared
determinants; a non-split accident would `error()` out fail-closed.

**C. L1 (Theorem A).** All identities re-derived by hand and confirmed as
executed: `r3 = x^14 + x^154` squares to 3; `s2 = x^21 + x^147` squares to 2;
`2h^2 = 3`; `i = r3(1+2ζ3)/3` squares to −1; `z8 = (1+i)h·r3/3 = x^21`;
generation `z8^5·z42^16 = x^169 = x` with `21·5 + 4·16 = 169 ≡ 1 (mod 168)`;
`Phi_168(x) = Phi_42(x^4)` verified by coefficient stretch; order-42 test
covers all three prime cofactors (the order-6 element `x^28` counterexample
unit test executed). The conductor tower gate now computes
`disc(x²−3) = 12`, `f6 = 24`, and the three cyclotomic degrees 12/24/48 by
exact division; the divisibility pattern (12 ∤ 21, 12 | 84, 24 ∤ 84,
24 | 168) is the standard conductor criterion. The well-defined + surjective
+ equal-dimension argument makes B ≅ Q[y]/(Phi_168); note (§10, prose base)
that identifying that quotient as a *field* uses irreducibility of `Phi_168`
(classical, carried by the charged report's prose layer).

**D. L2 (Kummer).** The within-fibre subtlety is now handled correctly: the
character pair depends only on the r-image, so R1's within-fibre equality was
structurally unfalsifiable; R2 replaces it with per-hom exact-order-168 /
`Phi_168(ω) ≡ 0` tests, which are real. `KUMMER_RANK_TWO` demands the
trivial annihilator and full μ3×μ3 image **at every listed prime
individually** — stronger than needed, fail-closed. The silent-prime guard
positively verifies the registered primes are character-trivial and bars
them from the certificate-prime list. `KUMMER_NORM_COROBORATION` is
correctly typed SECOND_PROOF (norms 6, 36 non-cubes; ε = 2+√3 norm-1; the
mod-3 nine-pair enumeration is real — it moves under an `r_square` mutation);
its float `is_cube` bracket is generous by many orders of magnitude for the
shipped data (declared debt §8.5, confirmed adequate).

**E. L3.** `FIELD_DEGREE_432` genuinely multiplies the two `ctx` values
published by L1/L2 (the two skip-mutations `M_KUMMER_RANK_DROPPED`,
`M_BASE_DIM_DROPPED` executed and fire it). `GALOIS_STABILITY_FREE` is
sound: substitution into unreduced relations via `fp_substitute` (full
expansion, verified no reduction path exists in that code), involution on
generators, image-membership with the induced permutation computed then
compared to the pin, and a non-identity requirement. Since σ is a ring
endomorphism of the free ring mapping generators of I to generators, σ(I) ⊆
I, and involutivity gives σ(I) = I, so σ descends to an automorphism of the
quotient — the correct executable shadow; extending to "K0/Q Galois" is the
charged report's prose (every τ ∈ Gal(B/Q) sends α1 to α1 or α2 according to
τ(√3), so the σ case is the only nontrivial one). The
`sigma_relation_permutation` pin is mildly redundant but adds a mutation
surface and is not circular (the computed permutation is derived, not read
back). The side-by-side unit test (quotient shape accepts the broken table,
free shape rejects) executed. `NONABELIAN` is real: `(A1A2)^3 = 6` computed
in the algebra, Eisenstein at 2 and 3 checked with square-part exclusion,
`disc(t³−6) = −972` by resultant, non-square, hence a non-normal cubic
subfield, hence non-abelian and non-cyclotomic. `IDEMPOTENTS_ONLY_0_1`
remains a Spec-routed emission-policy pin; its mathematical content is
carried by fieldness (L1+L2+L3). Routing through `Spec` is enough *given*
that typing is declared — the gate exists to make a forbidden emission
impossible, not to prove anything, and `M_COMPONENT_PRODUCT` /
`M_IDEMPOTENT_LIST` fire it. I recommend (cosmetic) retyping it away from
`THEOREM` in a future revision.

**F. L4.** Frame relations, exact order 42, unit Jacobian entries, the
432-count with the `L×L×L` caveat verbatim (CONSISTENCY), and the p² Hensel
replay all re-verified independently by my own modular arithmetic at both
primes, including that the p²-frame reduces to the p-frame. The "splits
completely" phrasing is justified: 432 F_p-points of a rank-432 étale
algebra forces all residue degrees 1.

**G. L5 (conditional, single-engine).** The whole identity chain was
re-derived by hand: `u³ = α2/α1 = (3−√3)²/6 = 2−√3 = ε^{-1}`;
`(2−√3)³ = 26−15√3` so F2 holds; `s = (1+i)(√3−1)/2` gives
`s² = i(2−√3)`; `q0 = u·s` gives `q0² = i·u⁵` and
`q0⁴ = −u^10 = (15√3−26)u = c`; `E(q,1) = 0 ⟺ q⁴ = −(26−15√3)·u = c` since
`(9−5√3)/(9+5√3) = 26−15√3`; the branch set `i^k q0` splits `t⁴−c`;
`σ(q0)·q0 = −1` via `σ(u) = u^{-1}`, `s·σ(s) = −1`. `E_BASE_REDUCTION`
reads every number from `spec.e_terms`/`alpha_data`/`eps_data`, computes
`CBASE = −C2/C1` through an exhibited inverse, ties it to `−(2−r3)³`, and
verifies `(α2/α1)·s⁴ = CBASE` plus `u³ = α2/α1` plus `q0^4 = c` directly —
no literal is read back to itself. The two-scale substitution really does
catch the `W2` exponent (`M_E_EXPONENT`'s `gate_errors` show the
homogeneity message). **Independent numerical confirmation:** with my own
modular code (no packet imports) I rebuilt i, u, s, q0 at both registered
frames and verified `E(q0,1) ≡ 0`, `q0⁴ ≡ c`, and four distinct branches
mod 105337 and mod 105673. The literal pins parse the sealed files
correctly: `BRIDGE_E_RE` matches exactly one display in the bridge (line 56,
`E := (9+5*r)*A1*W1^4 + (9-5*r)*A2*W2^4 = 0`) and `REPORT_Q0_RE` exactly the
four q0 rows of report §8.2, values equal to `TRUE_Q0`. The pointbank
regression recomputes ratios 7210 / 14755 from the raw banked W-values
(restricted unpickler admits no globals).

**H. Theorem separation (D1).** The three censuses partition correctly:
`theorem_inputs` = 31 unconditional (30 gates + `CENSUS_UNCONDITIONAL`), 9
conditional, 1 corroboration — pairwise disjoint (asserted by P4 and by my
replay); `CENSUS_COMPLETE` feeds only `execution_integrity`. The boolean
formulas make **"unconditional true while an L0–L4 gate did not run"
impossible**: a failed gate flips the `all(...)` conjunct; a skipped gate is
non-PASS *and* missing from `ctx["executed"]`, so the layer census fails
too; the `LOAD_BEARING` name lists guard even a hypothetical registry
shrink. The 19 separation controls pin the pairs and the battery refuses
unless both `(true,false)` and `(true,true)` occur (8 and 8 observed).
`M_BASE_SURJ_DROPPED` = (False, True), pure-L5 and corroboration-only
probes = (True, False) / (True, True) all executed.

## 6. My own hostile fixtures (beyond the shipped battery)

Run against the sealed checker via an out-of-tree path loader; commands and
overrides reproducible from the names:

| fixture | override | result | reading |
|---|---|---|---|
| `X_LEAD_H_CUBE` | declared h leading monomial `(0,0,0,0,3)` | `RELATION_LEADING_TERMS` FAIL | computed-vs-declared pin is real |
| `X_SIGMA_IDENTITY` | identity sigma table | `GALOIS_STABILITY_FREE` FAIL (non-identity need) + `SIGMA_E_SYMMETRY` FAIL | the trivial-sigma hole is closed |
| `X_TOWER_42` | `conductor_tower=(42,84,168)` | survives, 42/42 | benign: Q(ζ42)=Q(ζ21); harness accepts a mathematically equivalent variant (the "new surviving mutation" the charge asked for — not rejected) |
| `X_Z8_PLUS168` | `zeta8_exponent=189` | survives | benign: same element mod 168; crt still ≡ 1 |
| `X_R3_SWAPPED` | `r3_exponents=(154,14)` | survives | benign: symmetric sum |
| `X_SIGMA_H_SIGN` | sigma with `h → −h` | survives | benign and **correct**: it is the other genuine lift of the base involution (fixes `2h²−3`, same relation permutation, q0 is h-free) — evidence the gate checks mathematics, not a literal |
| `X_FRAME_OTHER_ZROOT_105673` | frame z replaced by `z^5` (another primitive 42nd root) | all L0–L4 pass; only `POINTBANK_REGRESSION` fails; theorems (True, True), `all_pass` False | a different *valid* frame is mathematically legitimate; only the frame-bound corroboration notices. Correct typing; at run level `census_sha256` drift refuses the run |
| `X_COMPOUND_DROP_105673` | frames/registered/silent/pointbank all coherently shrunk to 105337 | **checker passes 42/42** | the battery's structural boundary: `registered_primes` is self-referential, so a *coordinated* scope shrink is invisible to the checker. Verified the deployed pipeline still refuses it: the observable set drops 29 → 24, so `observable_sha256` ≠ pin (`OBSERVABLE_DRIFT`), and GP's hard-coded frames would force `ENGINE_DISAGREEMENT`. Not a live hole; document it as the reason the observable pin is load-bearing |

**Gate-body literal census (charge E).** Full sweep of
`k0_field_checker_r2.py`. Remaining in-body literals are: verification
*targets* that can only force a FAIL when wrong (the F-identity constants
`15, −26`, `Fr(1,6)` inverses, `Fr(1,3)`, `Fr(1,2)` — each is checked
against algebra recomputed from mutable `Spec` data, and the load-bearing E
statement goes through `spec.e_terms` in `E_DIRECT_SUBSTITUTION` /
`E_BASE_REDUCTION` regardless); the declared registered-target policy pins
(432, `{2,3,7}`, witness 5, `("K0",)`, `(0,1)`), all Spec-routed and
mutation-covered as the README states; structural constants of the objects
themselves (168, 48, 3, cube exponents); and one cosmetic literal `12` in
`SPLIT_COUNT_432` where `spec.basis_shape[0]` would be cleaner (harmless —
shape drift is caught in L0). **I found no load-bearing literal that could
produce a wrong PASS and is out of the battery's reach.** The R1 findings
(`14/154`, the pointbank E form) are confirmed routed through `Spec`.

**MUST_SURVIVE right-reason check.** All four survive with (True, True) and
for the right mathematical reasons: `(2,1)` completes the inverse-pair
coverage (8/8 classes) and is a non-cube by the exhibited characters; the
generator change `((1,0),(1,1))` has determinant 1 mod 3 (a basis);
certificate primes are order-insensitive (sorted iteration; 673-membership
by set); the all-inverse set is inverse-closed with full coverage.

## 7. The GP file, read as an adversary (never executed — this is source review only)

Hand census: **110 `chk`/`chkE` sites** (L0 20, L1 20, L2 23, L3 19, L4 13,
L5 15) and **29 `obs` sites** (7+1+6+3+8+4), matching `nexpect = 110`, the
static predictor, the runner's constants, and the 25/4 unconditional/E
split. The Python observable values I computed all agree with what the GP
expressions must produce if PARI behaves as documented (`poldisc(P42) =
3^6·7^10`; squared block determinants as in §5B; frame counts 12/2/18/432;
`ENORM = 6`; etc.).

Semantics audited line by line; the constructs the charge flagged:

* `matrix(m,n,i,j,expr)` with `t_INTMOD` entries and `matdet` — standard;
  sizes 12/18/2 are trivial for `parisize=64M`. Column decomposition
  `(j−1)\9, ((j−1)\3)%3, (j−1)%3` matches Python's column order exactly.
* `polrootsmod` on the non-monic `HB*'t^2 − HC` and on `'t^3 − (3±r)` —
  supported for any poly over F_p; the count checks (2, 3, 3) fail closed
  if not fully split, and `sqrt(Mod(RSQ,p))` errors on a non-residue —
  which is contained (below).
* the `sg(f)` swap-via-`'tw` subst chain — traced on all five relations:
  RELA1 ↦ RELA2 ↦ RELA1, RELZ/RELR/RELH fixed; involution and
  individual-non-fixing lines are real; GP polynomial `==` is semantic
  (gequal), not representational, so the chain's variable shuffling is safe.
  This genuinely operates before any quotient (fresh variables, never
  `Mod`ed) — repair D3/R2-E confirmed on the GP side too.
* `chkE` as a second accumulator — confirmed: `ok` (L0–L4) and `okE` (L5)
  never mix; both `chk` and `chkE` increment the one `ncheck`, and every
  printed line is exactly one census entry; the terminal line prints the two
  flags separately, so an L5 failure cannot flip the unconditional banner.
* `select(u -> u == 2, vector(...))` — **does not exist in the shipped
  file**. The review request's item F names a construct that is absent
  (grep: no `select(`, no `->`); the hygiene scan in fact *forbids* both.
  Stale sentence in the charge; no code risk.

Failure-mode containment I specifically checked: a GP `error()` mid-script
(or any partial run) may exit 0 on some gp builds after falling back to
reading empty stdin, but the runner independently requires exactly 110
parsed gate lines all printing 1, the `CENSUS 110/110` line, exactly 29
observables, and the terminal line — a partial or error-bearing transcript
faults on `GP_UNPARSED_LINE`/`GP_GATE_COUNT`/`GP_CENSUS`/`GP_TERMINAL`
regardless of exit status. Label widths (max 63) fit the runner's 80-char
window; the four line regexes are mutually exclusive on this file's output
shapes.

Residual GP notes (no repair required, record for the rehearsal reader):
(i) the GP `L1 CRT` line is pure constant arithmetic `(21*5+4*16)%168 == 1` —
in the *Python* engine the same fact reads mutable Spec fields (the README's
retention defense holds there), but in GP this one line cannot print 0
without editing the file; it is redundancy beside the computed GENERATION
line, one line of census padding, and should be data-driven in any future
edit. (ii) the within-fibre branch
`if (vvals[idx] != v, error(...))` in `charframes` is unreachable (the
character pair is a function of the r-value alone — the very fact that made
R1's version vacuous); it is an uncounted defensive branch, not a gate, so
it pads nothing, but it should not be mistaken for a check. (iii) the GP
leading-term block validates the *declared* LEAD data (pure powers,
distinct variables, shape) but does not recompute leading monomials of the
actual relations — that tie is Python-only; the GP side's substantive rank
content is the independence witness. The two-engine claim for the
unconditional layer remains fair because every load-bearing number is
cross-checked through the 25 shared observables, but the asymmetry is worth
one honest line in a future README.

The mod-3 nine-pair line is real (moves under `RSQ` mutation), the
`E_BASE_IDENTITIES` retype plus `TERMINAL_LINE` regex change close D7 both
ways, and the predicted-count arithmetic (110) is now triple-anchored:
declared `nexpect`, the D12-repaired predictor (nested loops multiply,
strings/comments stripped, loop bounds resolved from the file's own vector
declarations, refusal on unresolved loops over gates), and my independent
hand count.

## 8. Custody and the terminal (charge G) — everything except REPAIR-1 confirmed

* `emit_immutable`: `O_CREAT|O_EXCL` on the final name, write, fsync, fchmod
  0444, directory fsync — no `.tmp`, no window; a short or torn write is
  caught by the byte-for-byte manifest replay and archive replay (explicit
  per-member expectation table, no truthiness fallback), which run before
  any terminal.
* One-terminal discipline: the runner's fault path writes nothing (stderr +
  exit 70); the supervisor publishes exactly once through `publish_terminal`
  (itself `O_EXCL`); the NO_VERDICT path zeroes all four statuses and both
  credited booleans. A second presentation of the same authorization dies at
  the lease (once REPAIR-1 makes the lease reachable) **before the try
  block**, hence with no terminal; changing the run path requires changing
  the record, hence the digest, hence the live tag.
* `validate_authorization_record`: pure, and P9's 33 cases replicate. I
  probed for records that should be refused and are not: the only gap I
  found is that `normalize_model` maps look-alike evasions such as `0pus 5`
  to `0pus5`, which does not contain `opus` and would be accepted. The
  guard is against accidental same-model review, not a malicious
  coordinator (who could write anything), so this is a note, not a repair.
  The verdict check is exact string identity with `"PASS"`; my verdict
  above therefore blocks authorization by construction.
* Instance type collapsed to `r6i.large`: **right call.** It pins the type,
  not the terminated instance id; a fresh rehearsal host of the same type
  satisfies it, and the id/image/region binding comes from the fresh
  coordinator record. It will not block a legitimate rehearsal.
* `_forbidden_language_scan` `\bK_?[1-9]\d*\b`: exercised by P7 on the real
  `result.json`, `mutations.json` (refusal-record mode), and the GP text as
  the `gp_stdout` proxy — CLEAN, and I checked the 62-entry battery names
  and all gate labels by eye for false-positive shapes (`K0`, `Kummer`,
  `KUMMER_…` all safe). Non-ASCII evasions die earlier (`ascii` encode of
  GP stdout; canonical JSON is `ensure_ascii`).
* Environment/cgroup contract, IMDSv2 identity, tag triple, root-owned
  authorization/archive/gp-binary bindings, safe tar extraction, and the
  runner's isolated-mode and marker checks all read correctly; the sealed
  module loader chain (authorization → `packet_manifest_sha256` →
  `PAYLOAD.sha256` → per-module hashes → `sys.modules` pre-registration →
  `sys.path` immutability assertion) is exactly what P8's eight live
  subprocess controls exercise, including the live reproduction of the R1
  `ModuleNotFoundError`.
* Terminal claim discipline: four separated blocks; the E theorem typed
  single-engine with a named reason and corroboration list; the
  unconditional statement names no frame-derived fieldness; crediting only
  jointly with EXECUTION_INTEGRITY; `not_claimed` carries the firewall; and
  nothing anywhere asserts the GP engine has run. One behavioral note: in
  practice the runner refuses (census/observable drift) rather than
  emitting FAIL terminals, so any terminal that exists will be all-PASS —
  refusal-over-wrong-verdict, which is the declared design.

## 9. Answers to the charge's remaining direct questions

* **`L1 CRT` retained — defensible?** In Python yes (both sides read the
  same mutable exponents; `M_BASE_SURJ_EXPONENT`/`M_BASE_GEN_Z8_POWER` fire
  it). In GP it is constant-true (§7.i) — retention defensible, the stated
  reason only half-applies.
* **`IDEMPOTENTS_ONLY_0_1` through `Spec` — enough?** Yes, as a declared
  emission-policy pin whose mathematics lives in fieldness; see §5E.
* **GP mod-3 line — real or padding?** Real (§7).
* **`E_BASE_REDUCTION` chain sound, nothing self-read?** Yes (§5G).
* **Two engines' point sets can't differ?** They are both the complete
  solution sets, so no; and the shared observables are squared
  determinants, so even orientation can't disagree (§5B).
* **A mutation whose declared pair is wrong / a failure class the controls
  miss?** None found; the 19 pins replicate, and my compound fixture (the
  one class the *checker* misses) is refused by the runner's observable pin
  and cross-engine agreement (§6).

## 10. Residual risk and claim boundary

1. **The GP file has never been parsed by any GP.** All §7 statements are
   static. Every plausible failure lands in a runner refusal, never a wrong
   verdict, but the two-engine claim for the unconditional theorem becomes
   true only when GP actually runs and agrees.
2. **REPAIR-1** (§4) must land before any authorization; until then the
   custody flow cannot reach either engine.
3. The unconditional theorem's prose base (declared in the packet,
   grok46-confirmed): `Z[ζ_n]` maximality, Kummer correspondence, the
   equal-dimension surjection identification (including `Phi_168`
   irreducibility), local-unit descent behind the character argument,
   abelian descent for the SECOND_PROOF gate. The certificate is an
   executable shadow plus that report; it does not claim otherwise.
4. The E theorem is conditional on the literal displayed E and
   single-engine Python; typed so everywhere.
5. Frames are witnesses: a different valid frame moves only corroboration
   (§6, `X_FRAME_OTHER_ZROOT`); branch indices are frame-bound and pinned.
6. The battery is single-field; coordinated multi-field redefinitions are
   caught only at the runner/seal level (§6, compound fixture). The seal is
   what fixes the shipped `Spec`.
7. Nothing here is a D43 row/point/template/D25/raw-J/Keller/JC2 result;
   nothing derives fieldness from the 432-frame count; this review does not
   authorize AWS, and only a future literal-`PASS` review of the repaired
   packet can enter an authorization record.

## 11. Reproduction

```
cd <repo root>
python3 cases/d43_k0_field_certificate_r2_20260829/seal_r2.py --root . --verify
python3 cases/d43_k0_field_certificate_r2_20260829/preflight_r2.py --root .
python3 -O cases/d43_k0_field_certificate_r2_20260829/preflight_r2.py --root .
```

plus the fixtures of §5B/§5G/§6 (overrides named inline; each is a
`dataclasses.replace` on `Spec` run through `run_from_pins` with the packet's
`execution_pins_r2.json` and the two hashed pointbanks). Body hash below:
verify with `sed -n '1,/^<!-- BODY-END -->$/p' <this file> | shasum -a 256`.

<!-- BODY-END -->
5cac28d3387e56b1159577612d62c2bc01db9040e7888b54257d80e9280f6009  body: everything from the first byte of this file through the BODY-END line inclusive
