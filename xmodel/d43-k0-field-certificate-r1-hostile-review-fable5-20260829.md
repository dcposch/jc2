# Hostile source review: D43 `K0` field certificate, R1

**UTC:** 2026-08-29
**Role:** Fable 5, different-model adversarial mathematics and certificate-source referee
**Producer:** Opus 5 (`xmodel/d43-k0-field-certificate-r1-opus5-20260828.md`)
**Packet:** `cases/d43_k0_field_certificate_r1_20260828/`
**Status reviewed:** `R1_SOURCE_READY_AWS_NOT_AUTHORIZED`

No AWS action, no PARI/GP execution (none exists on this host; `gp` resolves to
a `git push` shell alias, confirmed live), no heavy CAS, no `jc2-lean` access,
no canonical-ledger edit, no commit. All executed checks below are bounded
stdlib Python, seconds of wall clock. The producer report was treated as
allegation; every number cited below was recomputed here or is marked
hand-derived.

---

## Verdict

**`PASS_FOR_PINNED_GP_REHEARSAL`**

This PASS licenses exactly one thing: a separately authorized, coordinator-GO,
one-core live PARI 2.15.4 rehearsal of `k0_field_cert_r1.gp` under the sealed
supervisor/runner path on the registered host. It does **not** itself certify a
two-engine run, and the defect list below (D1–D8) must be repaired in an R2
before any two-engine certification terminal is credited as final. Nothing
found allows the certificate to pass while being wrong: every defect is
fail-closed (can only turn a true verdict into a refusal or a misreported
FAIL), or is a naming/typing overstatement whose load is carried by a real
anchor elsewhere in the packet or by the grok46-confirmed theorem report.

---

## 1. Frozen charge and replay evidence (all exact)

Charge hashes, recomputed and matching:

| object | SHA-256 | match |
|---|---|---|
| `SOURCE_SEAL.sha256` (full file) | `583db53e641adfee8dec8cc3f5f4fc2c413b2f2651362790bea9d08dea5cb611` | charge |
| `SOURCE_ARCHIVE.tar` | `e5d140db10194f1cab0812e3eaa003ca7aafd36a6e2b1fb11c153862975790b5` | charge |
| `REVIEW_REQUEST.md` | `d61e56aa890861ebbfcfe9a915a266822651d1b1e42557ff4eead319efbf6ce2` | charge |
| producer report | `2fac39ec75073fda92d3dff2ccd88ee37289bb36dd841a65a58b9ca2fdf81887` | charge |
| theorem report | `6d3d53c20387d324766daaf40eb502df42d9e2776c6ab6053041bc1f3dee1430` | charge |
| grok46 theorem review, body above `<!-- self-hash -->` delimiter | `877e451f33b24b7714c712404401f11b35b6621e80400e791c4b54cfbe5078fd` | charge |

Replays executed:

* `seal_r1.py --root . --verify`: `ok: true`, all four `matches_disk` true,
  archive `e5d140db…`, payload `62d1bdec…`, seal `583db53e…`. The archive is
  byte-deterministic as declared (PAX, sorted members, uid/gid 0, empty
  uname/gname, mtime 0, mode 0444; 21 members = 16 packet + 5 external).
* `preflight_r1.py --root .`: `preflight_pass: true`. P1 15/15 packet files;
  P2 21/21 archive members, 0 missing/extra/mismatched; P3 GP static census
  79/79 with 68 static sites + 3 trip-2 loops, 21 observables predicted;
  P4 36/36 Python gates, both theorem booleans true; P5 35 MUST_FAIL + 2
  MUST_SURVIVE + 2 gate unit tests, 0 failed entries, battery
  `9b9699551f775a4e…`; P6 census `2544c8cc…`, observables `e51ed0d2…`, GP
  script `fde358dc…`, all matching `execution_pins_r1.json`; P7 clean.
* `SOURCE_ARCHIVE.sha256` member lines equal the REVIEW_REQUEST frozen-inputs
  table exactly (emitter `5420b5c0…`, `selected_rows_v2.py` `9fc9bd7a…`,
  pointbanks `bb0f13b6…` / `b933cdb5…`, theorem report `6d3d53c2…`).
* Independent battery re-run with per-entry inspection: all 35 MUST_FAIL fire
  **their named gate** (verified via `intended ⊆ failed_gates` and reading
  `gate_errors`); both MUST_SURVIVE survive with zero gate failures; battery
  hash reproduces `9b969955…`.
* Independent from-scratch cubic-character computation (no packet code
  reused; order-168 elements found by direct order test): at 673 the two
  `sqrt3`-fibres `r=26, 647` carry pairs `(255,1)` and `(1,255)`; at 1009 the
  fibres `r=860, 149` carry `(374,1)` and `(1,374)`; annihilator set exactly
  `{(0,0)}` and generated order 9 at both; at 105337 and 105673 all pairs are
  `(1,1)`, nine annihilators, generated order 1. Matches both engines'
  declared observables and grok46's root values.
* Fresh baseline run reproduces the pinned census and observable hashes with
  exactly 21 observables.

---

## 2. Item A — the Kummer layer

**Sound, and genuinely basis-free.** The verdict-path objects are
`chi(alpha) = alpha^((p-1)/3) ∈ mu_3(F_p)`, the annihilator count, and the
generated order — all canonical integers. The checker never calls `mu3()` or
`primitive_root()` on the verdict path (grep-verified; `primitive_nth_roots`
returns the full canonical order-168 set and its own order verification is
generator-independent), and the GP layer uses `polrootsmod` plus direct
powering with no `znlog`/`znprimroot`. The charged report's
`(2,0),(0,2)`-versus-`(1,0),(0,1)` discrepancy at 673 is exactly a
discrete-log basis artifact, and no discrete log survives anywhere in this
packet. Replacing `w` by `w^2` cannot change any gated quantity. No FAIL here.

**The valuation step.** The executable shadow of `v_P(alpha_k) = 0` is gated
in both engines: `(3±r) mod p ≠ 0` (`_character_frames`; GP line 148), and
`alpha_k` is integral, so nonzero residue is exactly valuation zero. The
remaining descent — `alpha = x^3, x ∈ B^*` implies `3·v_P(x) = 0`, so `x` is a
local unit and the character kills the class — is prose, carried by the
charged theorem report and independently CONFIRMED by the grok46 review (§3.2
runs the same argument for `eps`, §3.3 for the characters). The certificate is
entitled to it; there is no meaningful executable replacement beyond the
residue check already present. Recommended R2 hardening (not required): add
`poly_eval_mod(Phi168, omega, p) == 0` per hom, which replaces the cited
"exact order 168 ⟹ root of `Phi_168 mod p`" step with one line of
computation.

**`Z[zeta_n] = O_{Q(zeta_n)}`.** Cited, not checked; acceptable — it is a
named standard theorem and the theorem layer is separately reviewed. A cheaper
sufficient citation exists and is worth recording in R2 prose: the argument
only needs residue degree 1, which follows from `p ∤ disc(Phi_168)` (automatic
from `p ∤ 42`, since `disc(Phi_168) | 168^48`) plus the conductor-index lemma;
no cyclotomic-specific maximal-order theorem is required.

**Strictness bonus (correct direction):** `KUMMER_RANK_TWO` demands rank two
at *every* listed prime individually, which is stronger than the theorem needs
(one certifying prime suffices) and fails safe.

**One vacuous sub-check found (D10):** the within-fibre consistency need
("character value depends on the hom within a fibre") cannot fire as coded —
`v` is computed from `r` alone before insertion, so all members of a fibre
carry the identical pair by construction. The mathematical fact is real but
this line certifies nothing. Same in GP (`mapget(tab,…) != v`).

---

## 3. Item B — gates that cannot fail

Executed demonstration: calling the gate functions directly with the absurd
monic datum `phi42 = x^12 + 5` (spec otherwise true), **`RANK432_MONIC_BASIS`,
`GALOIS_STABILITY` and `NONABELIAN` all PASS**. Consequences:

* **`RANK432_MONIC_BASIS` (D2).** The 432-monomial normal-form loop is
  tautological (basis monomials are below every rewrite threshold, for any
  `phi42`); the five-relation loop is tautological (the relations are built
  from the same data as the rewrite rules, so they normalise to zero
  identically — e.g. `Phi42(z)` reduces to 0 for *any* monic degree-12
  tuple); `len(basis) == 432` reads the module-level `BASIS_SHAPE`, not the
  spec; `alg.one() != {}` is constant. The gate's live content is the shape
  literal compare and the product arithmetic. `"confluent_on_basis": True` in
  the detail payload is an **asserted literal, not a computed fact**. Answer
  to the request's question: the gate certifies that the rewriting implements
  the declared presentation and that the shape arithmetic holds; freeness of
  rank 432 additionally rests on the triangular/coprime-leading-term Gröbner
  lemma, which lives in the theorem report (Lemma L1) and is grok46-CONFIRMED
  (§1, associated-graded argument). The sealed anchors that make `phi42`
  drift detectable are `SRC_PHI42_LITERAL` (recomputes `Phi_42` from
  `x^42-1`) and `PHI42_DISCRIMINANT` (recomputes the resultant) — both real,
  both battery-covered. Not unsound; the gate name and detail oversell.
* **`GALOIS_STABILITY` (D3).** The sigma-preserves-relations loop computes
  `sigma` of already-normalised relation values, i.e. `sigma({}) == {}` five
  times — vacuous. The remaining needs (`sigma(r) = -r`, `sigma` swaps
  `A1,A2`, fixes `A1·A2`) are structural consequences of the `sigma` code
  itself. The genuine content — sigma permutes the relation *set* in the free
  polynomial ring, hence descends to a ring automorphism — is certified
  nowhere in code; it is carried by the theorem report (grok46 §4). An honest
  R2 check operates on free-ring polynomials before quotienting.
* **`NONABELIAN`** is entirely constant arithmetic (Eisenstein digits,
  `disc = -972`, square test) plus one structural product; same class.
* **`BASE_CONDUCTOR_TOWER` (D10):** five of six needs are constant arithmetic
  (`12 % 4 == 0`, `84 % 24 != 0`, …); the one real, falsifiable need is
  `disc(Phi42)` odd.
* **`KUMMER_NORM_COROBORATION` (D10):** `need(2 - 1 > 0 and 2 - 2 > -1, "eps
  has a negative real embedding")` is constant-true and the message is
  mathematically garbled — `eps = 2+sqrt3` is totally positive; the intended
  fact (both embeddings positive, forcing the sign in `±eps^{3n} = eps`) is
  the opposite of what the string says. The norm facts themselves are real
  arithmetic; the gate's honest "requires abelian descent" typing is correct,
  and the descent needs `3 ∤ [B:Q(sqrt3)]`… which is false (`24 = 3·8`) — the
  correct descent is the Galois-subfield argument (grok46 §3.1), not a norm
  cofactor argument; the gate does not state a wrong argument, only a wrong
  embedding sentence.
* **`KUMMER_REPRESENTATIVE_CLASSES`:** the `(i,j) != (0,0)` need is dead code
  (a `(0,0)` representative dies at the witness-None need first). Cosmetic.
* **`L1 CRT` line:** given `BASE_ZETA8` (`zeta8 == x^21`), the ring identity
  `z8^5·z42^16 == z` and the exponent congruence `21·5+4·16 ≡ 1 (mod 168)`
  are equivalent; the CRT need is a restatement, but both read the same
  mutable spec exponents, so it is redundant belt-and-braces, not a
  cannot-fail gate. Keep.
* **`FIELD_DEGREE_432` / `BASE_DIMENSION_48`:** consistency arithmetic on
  spec numbers. The `9` is a literal; its computed counterpart is
  `KUMMER_RANK_TWO`'s `generated_order == 9`, which is real, battery-covered
  and observable-pinned, but there is **no data-flow** from L2 into the L3
  gate — the end-to-end chain is a conjunction of gates plus the standard
  Kummer correspondence and the equal-dimension surjection argument, both
  prose in the theorem report (grok46 §4). Acceptable architecture for a
  certificate whose theorem layer is separately reviewed; R2 should make the
  gate read `generated_order` from ctx and cite the report section in its
  detail string.

The five hard computational anchors of the unconditional layer — Phi42
recomputation, discriminant, the `Q[x]/(Phi_168)` identities of L1, the
character layer, the frame/Hensel layer — are all real, falsifiable, and
battery-covered. The tautologies pad the census; they do not carry load.

---

## 4. Item C — the mutation battery

* **All 35 MUST_FAIL fire their named gates** (re-executed; `gate_errors`
  read; the verdict logic requires the named gate in the failure set, not
  merely "something failed"). Notable confirmations: `M_SRC_PHI42_MIDDLE` is
  caught by the literal pin as designed; `M_E_EXPONENT` fires
  `E_DIRECT_SUBSTITUTION` itself — the branch-line scale substitution really
  does repair the charged `W2 = 1` blind spot (`1^4 = 1^2`).
* **Both MUST_SURVIVE survive for the right reason.** `class_generators`
  genuinely feeds the annihilator/generated-order computation (the degenerate
  basis `((1,0),(2,0))` fails `KUMMER_RANK_TWO`), so
  `M_CLASS_GENERATOR_BASIS`'s survival exercises basis-freeness rather than
  unused data; `M_CLASS_REP_EPS_SQUARED` re-runs the witness search on the
  inverse class and the coverage census. Verified by direct runs.
* **Three new surviving mutations constructed and accepted by the harness**
  (battery extended in memory to 35+5, `battery_pass` true): certificate
  primes reordered `(1009, 673)`; the all-inverse representative set
  `((2,0),(0,2),(2,2),(2,1))`; the swapped generator basis `((0,1),(1,0))`.
* **Two *unintended* surviving mutations found (D4).**
  `pointbank_expected = ((105337,7210,3),)` — the 105673 regression silently
  dropped — passes all 36 gates; and the sharper
  `frames = ((105337, …),)` **plus** the halved pointbank list passes all 36
  gates, while the terminal text still asserts "both registered frames … both
  primes split completely". No gate pins the *cardinality* of
  `spec.frames` or `spec.pointbank_expected` (contrast `character_primes`,
  which has `len ≥ 2`, a liveness check, and a 673 pin). Reach of the defect:
  battery/Spec space only — the sealed defaults contain both frames, any
  source edit is caught by the PAYLOAD/authorization seal chain, and a
  frames-halving would additionally be caught end-to-end by the observable
  count (4 per-prime keys would vanish, 17 ≠ 21) and cross-engine agreement.
  The pointbank halving has **no observable shadow** at all. R2: add
  cardinality-and-prime-set needs to `FRAME_RELATIONS` and
  `POINTBANK_REGRESSION`, with one mutation each.
* **Gate-body literals duplicating Spec data (D5)**, exactly the class the
  producer asked to be enumerated: (i) `_character_frames` hardcodes the
  exponents `14, 154` instead of reading `spec.r3_exponents` — the L1↔L2 tie
  ("the same `r3` element in both layers") is enforced by duplication, not by
  data flow; a `r3_exponents` mutation fails L1 while L2 silently keeps
  certifying the true object. (ii) `POINTBANK_REGRESSION` hardcodes
  `(9±5r)·a·W^4` instead of building `E` through `_E(spec)` — an `e_terms`
  mutation is caught by `E_LITERAL_PIN` but the corroboration gate keeps
  testing the true `E`. Both are detection-preserving today; both should read
  from `Spec` in R2. Remaining presentation constants inside gate bodies
  (`3±r`, `3/2`, the `range(3)` of `mu_3`, the `12·2·18` split shape) are the
  fixed presentation itself, mirrored between the two engines and anchored by
  `SRC_ALGEBRA_BLOCK`; I classify them as acceptable.
* **Battery coverage gaps, probed and confirmed falsifiable (D6):** perturbing
  each of `s2_exponents`, `gen_z8_power`, `i_zeta3_exponent`,
  `silent_primes`, `p2_prime`, the 105673 frame, and a duplicated certificate
  prime `(673,673)` fails a correct real gate (respectively
  `BASE_WELLDEFINED`, `BASE_SURJECTIVE`, `BASE_I_SQUARE`,
  `KUMMER_SILENT_PRIME_GUARD`+`KUMMER_HOMS_EXHIBITED`, `P2_HENSEL_REPLAY`,
  `FRAME_RELATIONS`, `KUMMER_RANK_TWO` via `len(per) ≥ 2`). These are
  coverage gaps only; R2 should add one mutation per field.

---

## 5. Item D — the GP file, never executed anywhere

There is no PARI on this host (verified: `gp` is a `git push` alias and no
`gp` binary exists in PATH or the standard prefixes), so this file has still
never been seen by any GP parser. Static adversarial findings:

* **All five producer-flagged constructs check out on 2.15.4 semantics as
  documented:** `Mat(t_MAP)` yields the sorted 2-column key/value matrix and
  `#M[,1]` is the key count; `polrootsmod` returning `t_INTMOD` is handled
  robustly by `lift`-then-`Mod`; `Set(...) == Set([3,7])` compares canonical
  sorted GEN sets, not strings; the `chk` `t_INT` guard was checked against
  **every one of the 79 call sites** — each passes a comparison, boolean
  combination, `!ispower/issquare`, `setsearch(...) > 0`, `polisirreducible`,
  or an integer arithmetic result, all `t_INT`; no legitimate value can
  false-alarm it. Loop trip counts recounted independently by hand:
  L0 = 10, L1 = 19, L2 = 2 + 2·4 + 2·2 + 6 = 20, L3 = 12, L4 = 2·5 + 2 = 12,
  L5 = 6 — total **79 = `nexpect`**; observables 3+1+6+3+8+0 = **21**, with
  key names and values agreeing with the Python `_observables` map
  (including `annihilators_p = 1` vs Python's `len([(0,0)]) = 1`).
* **Mechanical checks executed:** comment-stripped, string-adjusted
  parenthesis/bracket/brace balance is exact (336/336, 89/89, 6/6); every
  `my()` declares names only (the [FIX 3] discipline holds mechanically); all
  gate labels fit the runner's 81-char label window; the runner's parse order
  (OBS, CENSUS, TERMINAL, then gate lines, `OPTIONAL` skipped, anything else
  a fault) cannot misclassify any line this script prints.
* **The `1`-indexing hazard is handled** (`BASIS_SHAPE[1]*[2]*[5] = 48`), the
  tower lives in `y` with `P42` in `x` ([FIX 1] verified at every `subst`
  site), the order test carries the prime 7 ([FIX 2], plus the executable
  order-6 counterexample in the unit test), and the census terminal is
  fail-closed on count mismatch.
* **D7 — the GP terminal overstates the E layer.** GP contains **no gate that
  reads `E` at all** — its L5 block certifies six base-level identities
  (F1/F2/eps/F4/`s`-typing/`mu_4`). Yet it prints
  `E_CONDITIONAL <ok>` from the same global `ok`, and the runner requires
  that flag for `e_ok`. Nothing false can be *emitted* (the flag is just
  "all 79 GP gates pass", and the Python E gates are separately required),
  but the "two genuinely independent engines" framing does not hold for the
  E-conditional theorem: that layer is single-engine Python plus GP
  base-identity corroboration. R2 must rename the GP flag (e.g.
  `E_BASE_IDENTITIES`) or the terminal must say the E theorem is
  single-engine.
* **D9 — cap inconsistency:** the optional `nffactor` block's `alarm(600)`
  exceeds the 120 s GP subprocess timeout and the 300 s unit cap. Unreachable
  in the sealed flow (`K0_OPTIONAL` unset ⟹ `type` is `t_POL` ⟹ block
  skipped, and the type test correctly short-circuits before truthiness), and
  fail-closed if ever enabled; still wrong numbers.
* GP's norm-corroboration and conductor chks are constant arithmetic — the
  same census padding as Python (D10).
* **Consequence of never having executed the file:** a nonzero residual risk
  of parse- or API-level surprise remains that no amount of static review
  can retire. Every such failure mode lands fail-closed in the runner
  (`GP_EXIT`, `GP_UNPARSED_LINE`, `GP_GATE_COUNT`, `GP_CENSUS`,
  `GP_OBSERVABLE_COUNT`, `ENGINE_DISAGREEMENT`) — a refusal, never a wrong
  verdict — and the terminal cannot be emitted without 79 printed `1` flags
  and 21 exactly-agreeing observables. That is precisely what the pinned
  rehearsal exists to probe; it is why the verdict is scoped to it.

---

## 6. Item E — custody and the terminal

* **`emit_immutable`:** the `path.exists()` check followed by
  `os.replace(tmp, path)` has a classic TOCTOU window in which a concurrent
  writer's file would be silently replaced; within this design the window is
  closed by the supervisor's atomic-mkdir lease (single runner per run dir),
  and any race degrades to a crash without a terminal (`O_EXCL` on the shared
  `.tmp` name), never to a second terminal. The `.tmp` suffix cannot collide
  with a member: the member list is fixed and none ends in `.tmp` (D11,
  cosmetic). `RUN_DIR_REUSE` lists only three artifacts, but the run dir is
  freshly created by the lease, so stale members are unreachable.
* **The archive-replay `or`:** safe. `extracted != members` faults first, and
  `members` is exactly `artifacts` keys plus `manifest.json`, so the
  `artifacts.get(m.name) or artifacts_manifest_sha` fallback is reachable
  only for `manifest.json`; artifact hashes are 64-hex strings and never
  falsy. Member mode/mtime/type are re-checked; duplicate or foreign names
  fail the sorted-list equality.
* **Single writer / `DUPLICATE_LAUNCH`:** the runner's fault path writes no
  terminal (stderr + exit 70); `terminal.json` cannot be written twice
  (exists-check plus `O_EXCL` tmp). The supervisor's `claim_run_path` mkdir
  is atomic and sits *before* its try block, so a second launch faults
  without touching the claimed directory, and both supervisor terminal paths
  (VERDICT and NO_VERDICT) go through one `atomic_bytes` with a collision
  guard. `DUPLICATE_LAUNCH` is unreachable twice by construction.
* **The pins sentinel resolves correctly:** sealed
  `execution_pins_r1.json` carries
  `gp_binary_sha256 = COORDINATOR_AUTHORIZATION_SUPPLIES_THIS`, which the
  runner's `[0-9a-f]{64}` check refuses — and the supervisor writes a merged
  `execution_pins_live.json` substituting the authorization's SHA-256. As
  shipped, any invocation outside the supervisor path is refused
  (`GP_BINARY_UNPINNED`). Correct fail-closed wiring.
* **D8 — authorization checks are incomplete.** `load_authorization` never
  checks `reviewer_pass.verdict == "PASS"` (the template's `<MUST_BE_PASS>`
  sentinel is enforced by nobody), and the same-model refusal matches only
  the exact spellings `{None, "", "opus5", "Opus 5"}` — `"OPUS5"`,
  `"opus-5"`, `"Opus5"` pass. Coordinator honesty is assumed; both checks are
  one-line R2 repairs.
* **Instance-type allowlist:** acceptable as a *declared provisional* pin.
  The producer states plainly that the type behind `r6b` is unknown; the
  authorization must name one type equal to the live IMDS value, and
  extending the list is a new R-number. For a rehearsal this is honest
  custody; R2 should collapse the allowlist to the single observed type after
  first contact.
* **`_forbidden_language_scan`:** tested against the real artifacts-to-be.
  `result.json` and `mutations.json` (in `refusal_record` mode) scan CLEAN; a
  reconstructed terminal-shaped payload scans CLEAN and passes
  `_component_policy`; the GP file text (proxy for `gp_stdout.txt` labels)
  has no forbidden-pattern hits; and removing the refusal exemption makes the
  battery record fault — the exemption is load-bearing, correctly scoped to
  `note`/`reason`/`gate_errors`/`error`/`detail` values only (the mutation
  *spec* itself is not serialized into the record). `\bK_?[1-9]\d*\b` has no
  false positive on any legitimate emission (`K0…` never matches);
  `component_count` catches any value not exactly `1` including multi-digit.
  Evasions (lowercase `k1`, Unicode subscripts, prose circumlocutions) exist,
  but the scan is a tripwire layered under the structural
  `_component_policy` check; adequate for this packet.
* Environment/cgroup/swap/service-user/systemd hardening are coherent
  (RLIMIT_AS 768 MiB > `parisizemax` 256M; unit env equals the supervisor's
  required env; `GP_DATA_DIR` forbidden by the supervisor and merely
  whitelisted by the runner, so absent; `MemoryDenyWriteExecute` is safe for
  PARI, which does not map W+X pages). Cosmetics: `SAFE_ID_RE` and two
  imports are dead code (D13).

---

## 7. Item F — claim discipline, and the one real quarantine finding

* No unconditional gate reads `spec.e_terms`, `spec.q0_terms`, or the
  pointbanks (usage-site grep: `e_terms` only in `Spec`, `_E`,
  `E_LITERAL_PIN`; `q0_terms` only in `Spec`, `Q0_NORMAL_FORM`; pointbanks
  only in `POINTBANK_REGRESSION` and the loader). `i_zeta3_exponent` is
  shared between L1 and L5, harmlessly (L1 is the anchor).
* The 432-frame count is typed consistency-only in **both** engines with the
  `L×L×L` caveat verbatim; the pointbank gate is CORROBORATION and feeds
  neither theorem's direct gate list; the terminal, prereg and README carry
  the correct forbidden-claims lists; nothing anywhere claims a D43
  row/point/template/D25/raw-J/Keller/JC2 result or derives fieldness from
  the frame count.
* **D1 — the theorem booleans are entangled through the census.**
  `ctx["executed"]` records only PASSes, so **any** gate failure anywhere
  (L5, corroboration, anything) fails `CENSUS_COMPLETE`, and both
  `unconditional_k0_theorem` and `e_conditional_ratio_theorem` require the
  census — making both booleans extensionally equal to `all_pass` in every
  reachable state. Executed proof: mutating only the `q0` coefficient
  (`-5/6 → -5/7`) produces **zero L0–L4 gate failures** yet
  `unconditional_k0_theorem: false`; every one of the ten pure-L5 MUST_FAIL
  battery entries likewise records `unconditional_k0_theorem: false`. So the
  answer to the review request's question 2 is: the quarantine is real in
  *content* (a corrected `E` changes no L0–L4 gate, and no unconditional
  computation reads E-data) and real in the *fail-closed direction* (a wrong
  `E` can never fabricate an unconditional PASS), but the boolean
  `unconditional_k0_theorem` is **not** computed from L0–L4 only, contrary to
  item F's stated property, and a wrong `E` would misreport the unconditional
  theorem as FAIL in the terminal of a refused run. The producer report §3
  discloses the census conjunct but not this consequence. The GP terminal has
  the same all-or-nothing structure. R2 repair: give each theorem boolean a
  layer-restricted census (all L0–L4 gates executed for the unconditional
  verdict; all L5 for the conditional), or document the entanglement in the
  terminal itself.

---

## 8. Theorem and scope limits

What a fully green future run of this source would establish, and no more:

1. **Unconditional (L0–L4):** `K0` is a number field of degree exactly 432,
   Galois non-abelian over `Q`, base exactly `Q(zeta_168)`, Kummer classes
   spanning `(Z/3)^2`, idempotents `{0,1}`, finite étale of rank 432 over
   `Z[1/42]`, ramified set exactly `{2,3,7}`, both registered primes split
   with 432 degree-1 frames, unique registered `p^2` Hensel lift. The
   computational inputs are all gated; the glue steps (rank-432 freeness via
   the triangular Gröbner lemma, Kummer correspondence `[L:B] = |Delta|`,
   equal-dimension surjection, `Z[zeta_n]` maximality, abelian descent,
   ramification bookkeeping) are prose in the charged theorem report,
   independently CONFIRMED by the grok46 review whose body seal I verified.
   This certificate does not re-prove them and cannot stand without that
   review.
2. **Conditional (L5):** only relative to the literal displayed
   `E = (9+5r3)·A1·W1^4 + (9-5r3)·A2·W2^4`; single-engine Python plus GP
   base-identity corroboration (see D7); recompute on any `E` correction.
3. **Corroboration:** the pointbank regressions are mod-p evidence with
   frame-local branch indices; they prove nothing and are correctly typed.
4. **Nothing D43/JC2:** no row, point, template, D25, raw-J, branch-survival,
   Keller or JC2 content; the 432-frame count proves no fieldness; the
   E-branch index is not portable across frames.
5. **The GP engine is not yet evidence of anything** — it has never been
   parsed. Until the rehearsal, the packet's factual support is the Python
   engine plus this review's independent recomputations.

---

## 9. Defect list

Required before an R2 two-engine certification run is credited (none blocks
the rehearsal):

* **D1 (moderate):** theorem booleans entangled through `CENSUS_COMPLETE`;
  layer-restrict the census conjunct or document in the terminal. §7.
* **D2 (moderate):** `RANK432_MONIC_BASIS` internal loops unfalsifiable;
  `confluent_on_basis` asserted, not computed; rename/retype or add a real
  independence probe (cheapest honest options: gate the pairwise-disjoint
  leading-variable structure of the five relations explicitly, or evaluate
  the 432 basis monomials at the 432 frames of one registered prime and gate
  the mod-`p` determinant nonzero). §3.
* **D3 (moderate):** `GALOIS_STABILITY` relation loop is `sigma({}) == {}`;
  check sigma on free-ring polynomials before quotienting. §3.
* **D4 (minor):** no cardinality/prime-set pins on `spec.frames` and
  `spec.pointbank_expected`; two unintended surviving mutations demonstrated;
  add needs plus one mutation each. §4.
* **D5 (minor):** gate-body duplicates of Spec data (`14/154` in
  `_character_frames`; the `E` form inside `POINTBANK_REGRESSION`); route
  through `Spec`. §4.
* **D6 (minor):** battery coverage gaps on seven falsifiable Spec fields; add
  mutations. §4.
* **D7 (minor–moderate):** GP prints `E_CONDITIONAL` with no E-reading gate;
  relabel the GP flag or restate the E theorem as single-engine in the
  terminal. §5.
* **D8 (minor):** supervisor does not enforce `reviewer_pass.verdict ==
  "PASS"` and the same-model check misses case variants. §6.

Cosmetic, fix opportunistically: **D9** `alarm(600)` vs the 120 s cap;
**D10** constant-true sub-checks (conductor-tower digits, the garbled
`eps`-embedding line, the vacuous within-fibre check, the dead `(0,0)` need,
`NONABELIAN` constants) — census padding in both engines; **D11**
`emit_immutable` exists/replace window and `RUN_DIR_REUSE`'s three-name list,
both closed by the lease; **D12** preflight static-census fragilities (nested
loops combine by `max` not product; per-line paren counting would break on
parenthesised comments — both currently harmless); **D13** dead code
(`SAFE_ID_RE`, unused imports).

Positive findings worth carrying forward: the `W2 = 1` blind-spot repair
demonstrably works (`M_E_EXPONENT` fires the substitution gate itself); the
refusal-record scanner exemption is load-bearing, correctly scoped, and the
honest battery record passes it; the archive is byte-deterministic and the
whole external-input surface is inside the seal chain.

---

## 10. Minimal next action

Coordinator: (1) resolve the `r6b` host to one exact instance type from the
sealed allowlist and supply the absolute path and SHA-256 of its PARI/GP
2.15.4 binary; (2) complete `authorization_template_r1.json` with this
report's path, model (`Fable 5`), verdict, and SHA-256, set
`coordinator_go = true`, freeze root-owned 0444, and set the live tag to the
record's hash; (3) run the one-core rehearsal through the sealed
supervisor/worker/systemd path exactly as sealed. Treat any GP deviation —
parse error, census ≠ 79, any observable disagreement — as a finding for R2,
never as something to patch on the host. Fold D1–D8 into R2 alongside
whatever the rehearsal reveals; R2 is a new seal and a new review.

No canonical-ledger edit, no commit, no push, no web access, no AWS action
was performed. The only file written is this report.

The SHA-256 of this review's body — every byte above the delimiter line —
is recorded immediately below.
<!-- self-hash -->
df389c19fd9fbac98527c21bf6bb633be374bfbf3ea18205206c2ce45c618824  report body above this delimiter
