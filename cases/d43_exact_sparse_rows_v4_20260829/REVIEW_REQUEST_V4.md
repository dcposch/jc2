# Hostile review request: D43 exact a00pp sparse rows v4

Please return PASS or REPAIR before any AWS registration or launch.  This
revision answers the Opus 5 v3 hostile review (SHA-256
`6e01e5d7e7852d094559ab57cd7a256c41390fca99e38a6c55fbea8f12209bd9`,
report-body seal
`1b90552abddb14bf5946a2e85f0a5ac26dae05d3049ef578db507c766862bd82`),
which confirmed the v3 mathematics within its boundary and returned
REPAIR_REQUIRED on custody.  Its five repairs R1-R5 plus the disclosed
UNADJUDICATED v2->v3 mathematical byte-diff are the charged roots here.

## Charged roots

1. **R1 (was blocking) - value-binding terminal.**  `decide_terminal` /
   `bind_candidate` in `job_contract_v4.py` must recompute or bind every
   payload-bearing candidate field: rehash lease, `records/REGISTERED.json`
   against the lease's registration digest, manifest (+ schema + claim
   boundary + null-shape), preflight receipt (+ pass/authority/manifest
   crosscheck), pilot gate (+ status/nonce/manifest), merge receipt
   (+ schema/status/nonce/lease/manifest/preflight/pilot/payload-name),
   merge payload bytes; cross-bind `semantic_sha256`,
   `template_bridge_sha256`, and `exact_inventory` under the rehashed
   merge receipt; contract-check the inventory as non-bool integers
   `29+155=184` with bands `{20:10, 30:9, 40:10}` and tail degree <= 2;
   validate the exact candidate key census.  Every field must carry
   recorded provenance (`RECOMPUTED_SHA256:...` vs `RECEIPT_CROSSBOUND:...`)
   in the terminal; no unexplained copied digest.  Attack with value
   forgeries in every digest field, impossible/string/bool inventories,
   claim-boundary promotion, and candidate/artifact mutation after the
   producer exited 0.  The v3 suite's fabricated-digest happy-path fixture
   is gone; verify the v4 fixture is honest.
2. **R1 third sub-claim - sidecar archive binding.**
   `verify_sidecar_archive` must resolve the named member relative to the
   sidecar via safe-relative logic, require the exact
   `<job_tag>.terminal.tar.gz` name, require a regular non-symlink file,
   and rehash it before any positive terminal; the terminal records the
   rehashed digest, never a copied sidecar string.  Attack with dangling,
   drifted, foreign-name, and traversal sidecars.
3. **R3 - full-member-set archive census.**  `extract_and_verify_archive`
   must refuse every non-regular member (directories included) and enforce
   exact full-member-set equality against the embedded manifest at every
   authority-bearing replay.  Attack with extra directory members and
   nested directory chains (accepted in v3).
4. **R4 - real censuses, no copied gates.**  The launcher starts the
   supervisor under `setsid --wait` in both containment modes; the
   containment identity gate requires session/PGID leadership in both; the
   final census pgid is `$$` in both (never 0); the terminal refuses
   `--cleanup-pgid <= 1` (`pgid_census_real`) and refuses mode-inconsistent
   cgroup gates (`cgroup_gate_mode_consistent`).  The fallback cgroup gate
   is reported as `NOT_APPLICABLE` with provenance, never a copied boolean;
   `gate_provenance` names each gate's evidence source.  Attack with
   vacuous pgids and copied cgroup values in both modes.
5. **R5 - authority-bearing launcher post-mortem.**  `postmortem-gate` in
   the contract voids a positive terminal that coexists with a non-zero
   post-mortem census rc, a non-empty census, or an unreadable census file,
   by an immutable 0444 `TERMINAL_POSTMORTEM_FAULT.json` (O_EXCL, first
   fault wins) plus launcher exit 78; the terminal is never overwritten,
   and its `post_boundary_contract` block names the fault object and the
   voiding rule.  Attack with positive terminals plus unclean censuses,
   unreadable terminals, and double-fault attempts.
6. **v2->v3/v4 mathematical byte-diff closure.**
   `math_function_diff_v4.py` pins all three producer digests and must
   prove: zero v3->v4 function drift (only the two `.v3`->`.v4` schema
   strings differ among assignments); 39 byte-identical shared functions
   containing the entire collapsed-arithmetic/jet/row core; the 25
   differing functions decompose exactly into the five reviewed repair
   classes; `V2_V4_MATH_FUNCTION_DIFF.md` regenerates byte-identically.
   Verify the adjudication against the actual diffs, not the tool's word.
7. **Preserved v3 confirmations.**  Literal collapsed-D21 structural
   equality with digest receipts only; zero production asserts (AST
   census); `python -O` import refusal in every production module
   including the `terminal` and `postmortem-gate` subcommands; exclusive
   flock lease; single late terminal authority; deterministic 20-member
   source archive `9051a3dbfc4d6d8714a6ee3ca53e84517bcadddfab4fc49baf480d65f0dd31ba`
   pinned only in the external launcher, packet seal, and future
   registration (zero self-reference); `solve=false` everywhere.
8. **Bounded hostile tests.**  `test_job_contract_v4.py` (45 fixtures) and
   `test_selected_rows_v4.py` (21 fixtures) must pass and genuinely cover
   the retained v3 surface plus every new negative control listed above.

## Additional hostile targets

* The honest-fixture construction itself: confirm no test builds its
  candidate from digests that no artifact carries.
* The `NOT_APPLICABLE` lane: confirm a fallback-mode positive terminal
  records the string, not `true`, and that `all`-style gate evaluation
  cannot be spoofed by other truthy strings.
* The launcher fallback `kill_boundary`, which now reads the session
  leader from `custody/containment_identity.json` (the v3 `-$!` group
  kill targeted the setsid wrapper's group, not the supervisor's).
* The macOS fixture gap: live `/proc`, cgroup v2, systemd scopes,
  `setsid`, and IMDSv2 remain exercised only through injected-reader
  fixtures and source reading; no live-Linux run exists.

Maximum promotion after a real successful reviewed run (unchanged from the
Opus 5 review's section 8, including its three narrowings): exact a00pp
support-specialized emission **reproducing the preregistered** 29/155
inventory of the finite 184-row raw-J truncation.  Not point existence,
not the full template, not NF equivalence, not all-depth compatibility,
not a Keller map, not a JC2 counterexample.  **No AWS launch is authorized
by this packet.**
