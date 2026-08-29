# D43 common-integral next-step audit

Reviewer: GPT-5.6 hostile/source audit  
Date: 2026-08-28  
Scope: residue-A D43 artifacts in `jc2`, excluding `jc2-lean`; read-only audit basis, except banking this report and its `.sha256` sidecar. No solver or heavy local compute was run.

## Verdict

**NO-AWS-YET.**

The smallest non-duplicative next step toward a common integral / number-ring presentation is not another finite-field solve and not a longer band-34 local-normal-form run. It is an exact emitter/proof task:

> Re-emit the D23/D25 parked/reducer layer over the source radical number ring or the selected `Z_p` coefficient ring, with reducer-to-parked traces and specialization gates back to the existing modular artifacts.

Until that exists, an AWS solve would act on an unverified scheme if it uses least-residue lifts of prime-specific coefficients. This shortcut is explicitly forbidden by the current D43 integral gate.

## 1. Established theorem/state

The promoted D43 result is modular and fixed-scale only.

- `xmodel/sol-d43full.md` states the scoped object as fixed `B=84`, residue-A `a00pp`, mod `p=105337,105673`, not characteristic zero, not a formal germ, and not a polynomial Keller map (`xmodel/sol-d43full.md:5-10`).
- The fully reconstructed ideal is `34 parked + 95 graph rows in bands 6..24 + 89 graph rows in bands 26..42` inside `F_p[184]` (`xmodel/sol-d43full.md:14-21`).
- It is nonempty at both banked primes, with explicit `184`-coordinate points satisfying all `218` generators and the full survivor gate (`xmodel/sol-d43full.md:23-33`, `xmodel/sol-d43full.md:116-139`).
- The honest interpretation remains: mod-`p` nonempty through D43 at fixed `B=84`; no characteristic-zero nonemptiness, inverse-limit survival, algebraization, globalization, polynomial Keller realization, or unbounded scale (`xmodel/sol-d43full.md:162-172`).
- The different-model review confirms completeness, witness soundness, and scope honesty (`xmodel/grok-d43full-review.md:33-43`, `xmodel/grok-d43full-review.md:219-234`, `xmodel/grok-d43full-review.md:264-269`).
- The ledger records the same: no first depth kill at fixed `B=84`, but no A-SCALE disproof, char-zero lift, or algebraization (`AUDIT.md:7393-7414`, `AUDIT.md:7416-7435`).

The lift/integral layer is still open.

- `sol-clift` proves a positive source-model `p^2` screen: the pristine 184-row Euler source equations have rank profile `129 = rank[J | -F/p]`, and a 24-coordinate correction kills all 184 source rows modulo `p^2` (`xmodel/sol-clift.md:11-23`, `xmodel/sol-clift.md:120-155`).
- That does not certify the assembled 218-row presentation modulo `p^2`, because common integral NF checkpoints/traces and a common integral parked emission are absent from that artifact (`xmodel/sol-clift.md:24-29`, `xmodel/sol-clift.md:108-118`).
- The exact special-fiber rank is `rank J_218 = 131`, tangent dimension `53`, with a unit `131x131` minor `810 mod 105337`; this is rank data only, not smoothness (`xmodel/sol-clift.md:31-45`, `xmodel/sol-clift.md:194-219`).
- `sol-d43int` upgrades the modular audit: the recovered `cases/d43red/` files close the modular 218-row census at both primes and replay the 184 modular source-to-D23-NF identities at `p=105337` (`xmodel/sol-d43int.md:12-31`, `xmodel/sol-d43int.md:102-129`).
- It explicitly does not produce the common integral 218-row model (`xmodel/sol-d43int.md:37-50`, `xmodel/sol-d43int.md:146-157`).
- The different-model NF review promotes only modular source-to-D23-NF fidelity, with quarantine against common-integral, all-218 `p^2`, smoothness, `Z_p`, characteristic-zero, germ, or Keller consequences (`xmodel/review-d43-nf-fid-grok.md:17-19`, `xmodel/review-d43-nf-fid-grok.md:153-171`).

## 2. Exact missing implication

The first missing implication is:

```text
prime-specific modular parked rows + modular D23 reducers + modular source/NF traces
  ⇒ common integral / Z_p 34+184-row presentation with reducer-to-parked traces.
```

No existing artifact proves this.

- `sol-d43int` says the regenerated identity stops at the 509-element D23 basis over `F_p`; the repository still has no common integral/`Z_p` 34-row parked presentation, no membership of the 509 reducers in integral parked generators, and no integral source-to-parked NF identity (`xmodel/sol-d43int.md:37-50`, `xmodel/sol-d43int.md:125-129`).
- It lists the uncomputed all-218 integral objects: `F_218(x1)/p`, parked-coordinate columns of the integral correction matrix, all-218 corrected replay mod `p^2`, and integral syzygies identifying the NF presentation with the source model (`xmodel/sol-d43int.md:146-157`).
- The consolidated gate machine file says the same: missing common integral/`Z_p` parked presentation, integral/`Z_p` membership of the 509 D23 reducers, integral raw-to-NF identities, and all-218 `p^2` replay (`cases/d43_integral_gate.py:118-134`; banked output `cases/d43_integral_gate_p105337.json:2-24`).
- The `d43_nf_trace_replay.py` boundary is explicit: its identities are over `F_p` against the D23 GB and do not supply integral parked generators or integral/p-adic source-to-parked traces (`cases/d43_nf_trace_replay.py:2-18`, `cases/d43_nf_trace_replay.py:237-238`).

Therefore the current rank/minor data cannot invoke formal smoothness or Stacks 02H6. `sol-clift` names the missing conditions: local dimension, local generation by the selected 131 equations, `p`-flatness, and integral reduction identity (`xmodel/sol-clift.md:210-219`).

## 3. Reusable artifacts/scripts

Reuse, but do not rerun as the mathematical next step:

- `cases/build_tails_modp.py`: source-row front end. It mirrors the numeric Euler engine but folds radicals numerically mod `p` (`cases/build_tails_modp.py:6-20`) and outputs a mod-`p` per-fiber symbolic bank (`cases/build_tails_modp.py:480-487`). It should be ported to a number-ring/`Z_p` coefficient backend.
- `cases/d25_reduce.py`: D23 reducer/NF conventions. It defines the 22-variable base ring and trace contract, including `h == NF + Σ q_k G_k` over `F_p[22 vars]` (`cases/d25_reduce.py:2-13`, `cases/d25_reduce.py:29-36`, `cases/d25_reduce.py:68-83`, `cases/d25_reduce.py:153-156`). Its radical specialization is modular, not a common-ring proof (`cases/d25_reduce.py:45-50`).
- `cases/d43_nf_trace_replay.py`: deterministic replay skeleton for row grouping, normal forms, trace hashes, and checkpoint equality (`cases/d43_nf_trace_replay.py:112-157`, `cases/d43_nf_trace_replay.py:209-247`). It is useful as a verifier architecture after the common-ring emitter exists.
- `cases/d43_full_family.py`: modular 34+95+89 assembly/audit, point slice, continuation slice, witness replay, and final certificate modes (`cases/d43_full_family.py:1-24`, `cases/d43_full_family.py:287-383`, `cases/d43_full_family.py:583-699`, `cases/d43_full_family.py:713-778`). It proves modular assembly, not integral emission.
- `cases/d43_local_fiber.py`: fixed parked graph-fiber local-generation audit only; it explicitly does not certify the total 184-variable family (`cases/d43_local_fiber.py:2-15`). Its banked run passes through band 32 and times out at band 34 (`xmodel/sol-d43int.md:60-69`, `xmodel/sol-d43int.md:172-203`).
- `cases/d43_integral_gate.py`: fail-closed summary and best current checklist. It already states the next move as re-emitting the D23/D25 parked system over the source radical number ring or `Z_p`, then running full-cell local membership (`cases/d43_integral_gate.py:170-174`; `cases/d43_integral_gate_p105337.json:48-52`).

## 4. Preregistered common-ring emitter acceptance gates

The next exact artifact should be a source-controlled emitter/verifier, not an AWS solve. Acceptance gates:

1. **Coefficient ring gate.** Declare the coefficient ring before emission:
   `r3^2=3`, `zeta42^42=1` with the primitive-root condition or cyclotomic replacement, `A1^3=3+r3`, `A2^3=3-r3`, `2h^2=3`, plus an explicit denominator/unit ledger. These are the coefficient radicals used by the `p^2` screen (`xmodel/sol-clift.md:51-73`; `xmodel/sol-d43int.md:131-145`).

2. **Specialization gate.** Provide homomorphisms to the two banked finite fields matching the existing radical/fiber embeddings at `p=105337` and `p=105673`. Specializing the common object must reproduce the existing modular parked rows and reducer data, not merely least-residue lifts. Least-residue lifts are specifically forbidden (`cases/d43_integral_gate_p105337.json:2-9`).

3. **Parked-row gate.** Emit the 34 D25 parked rows over the common ring and verify that their reductions match the prime-specific `d25fam_p*_a00pp.ms` rows used in the modular assembly (`xmodel/review-d43-nf-fid-grok.md:91-104`; `cases/d43_full_family.py:343-349`).

4. **Reducer gate.** Emit or trace the 509 D23 reducers over the common ring or selected `Z_p` ring. Required output is not just specialized GB text; it must include membership/traces relating reducers to the common parked generators. The modular reducer format and trace identity are only a template (`cases/d25_reduce.py:29-36`, `cases/d25_reduce.py:153-156`).

5. **Raw-to-NF gate.** Rebuild the 184 pristine source graph rows over the same ring and produce integral/`Z_p` raw-to-NF identities. After specialization, these must reproduce the reviewed modular `184/184` source-to-D23-NF trace replay (`xmodel/sol-d43int.md:102-129`; `xmodel/review-d43-nf-fid-grok.md:121-149`).

6. **P4P1 sidecar gate.** Emit the band-42 `Xf_alpha`/`Xg_beta` sidecar separately, with its source identity and origin-zero specialization. The ledger says checkpoint traces do not themselves cover the sidecar, while the sidecar is exact-source and load-bearing away from `3*alpha-2*beta=0` (`AUDIT.md:7493-7520`).

7. **No-promotion gate.** The emitter must output a fail-closed verdict unless it has all of: common parked rows, reducer-to-parked traces, integral raw-to-NF identities, specialization hashes, and sidecar handling. Until then, it cannot feed Hensel, flatness, `Z_p`, characteristic-zero, germ, or Keller claims.

Only after these gates pass should a compute job be specified for all-218 `p^2` replay and local generation/flatness.

## 5. AWS decision

**NO-AWS-YET; expected AWS cost: `$0`.**

Reason: the missing object is a definition/proof-emitter, not a hard finite-field solve. The current artifacts already solve/replay the modular presentation. AWS would be duplicative if it repeats D43 mod-`p` nonemptiness, and unsound if it attempts characteristic-zero or `Z_p` inference using least-residue coefficients.

Post-emitter compute can be preregistered later, under a strict `<1 TiB` memory cap, for:

- all-218 `F(x1)/p` and correction matrix in the common `Z_p` presentation;
- all-218 corrected replay modulo `p^2`;
- full 14-free-cell local generation after common-ring presentation exists;
- if band 34 remains the bottleneck, a non-origin point search on the same coherent modular component.

That compute is not currently licensed.

## 6. Duplication check

Do not duplicate these finished or scoped gates:

- **D23:** already promoted at fiber-local/mod-`p` tier; D23 row-22 obstruction does not eliminate the window, and the 509-element GB/nonemptiness work is banked (`AUDIT.md:6944-6967`). Reuse the D23 reducer object; do not rerun D23 nonemptiness.
- **D25:** already promoted at modular tier as 36 fibers, 16 disjoint `A^14` cells per fiber, with exact certificate and hostile review (`AUDIT.md:6982-7017`). Reuse the D25 parked cell structure; do not re-prove modular D25.
- **D43 full modular assembly:** already dual-confirmed as `34+95+89=218` and nonempty at both primes (`AUDIT.md:7393-7425`). Do not rerun the D43 exact-slice/nonempty campaign as the next common-integral step.
- **Band34/local generation:** the fixed-fiber engine is incomplete at band 34 and, even if completed, would certify only the fixed parked graph fiber, not the total 184-variable local ring or `p`-flatness (`xmodel/sol-d43int.md:60-69`, `xmodel/sol-d43int.md:172-203`; `cases/d43_local_fiber.py:14-15`, `cases/d43_local_fiber.py:425-426`).
- **D25-to-D27 compatibility:** this is related but separate. The ledger says the source-defined full-cell compatibility locus at band 26 is nonempty/rank at least five but does not prove band-28 persistence, germ, char-zero, or D43 consequences (`AUDIT.md:7522-7584`). This should not be conflated with the D43 common-ring emitter.

## 7. Stale-ledger repair list

These are wording repairs for future canonical updates; this report made no canonical edits.

1. **`xmodel/sol-clift.md:108-115` and `cases/d43_char0_lift_p105337.json:4-25`: stale after recovery.** They say the `d43red` checkpoints are absent. After `sol-d43int`, the modular checkpoints are recovered. Correct wording: the checkpoints exist and close the modular polynomial audit, but they contain no integral coefficients/traces and do not provide a common integral model.

2. **`AUDIT.md:7446-7447`: stale in the same way.** Replace “d43red checkpoints are absent locally” with “d43red checkpoints are recovered, but are prime-specific modular payloads without integral/trace data.”

3. **`xmodel/sol-d43full.md:5` historical status is stale if quoted as current.** The report header says `INTERNAL / UNREVIEWED / MOD-p`; after Grok review, current ledger tier is dual-confirmed mod-`p`, still not char-zero or algebraic (`AUDIT.md:7416-7425`).

4. **Old §10.7/WTC wording that graph-preserving D43 was unresolved is superseded.** `grok-d43wtc-review.md` correctly described the pre-full-reconstruction split and said the graph-preserving D43 family was unresolved (`xmodel/grok-d43wtc-review.md:29-44`, `xmodel/grok-d43wtc-review.md:190-219`). Current wording must distinguish: modular full graph-preserving D43 is nonempty; common integral/Stage 2 remains open.

5. **Do not say “all assembled graph polynomials are covered by checkpoint traces.”** The sidecar correction is source-derived and origin-zero, but checkpoint traces do not cover `Xf_alpha`/`Xg_beta`; use the clean ledger wording at `AUDIT.md:7517-7520`.

6. **Do not advertise the unit minor as a smoothness certificate.** It is a nonzero Jacobian minor/rank certificate only; localized generation, local dimension, and flatness are still absent (`xmodel/sol-clift.md:194-219`; `cases/d43_integral_gate_p105337.json:26-47`).

## 8. Maximal promotable statement

The maximal current theorem is:

> At fixed Sigray scale `B=84`, residue-A fiber `a00pp`, in the `PIN42`, no-log, `W1W2≠0` chart, the fully graph-preserving D43 modular presentation `34+95+89` in `184` variables is nonempty over `F_105337` and `F_105673`; at `p=105337`, the 184 pristine graph rows have modular source-to-D23-NF fidelity against the recovered checkpoints, and the pristine source point has no first-order `p^2` obstruction. No common integral 218-row presentation, all-218 `p^2` replay, local smoothness/flatness, `Z_p` point, characteristic-zero point, formal germ, polynomial Keller map, or A-SCALE disproof is established.

