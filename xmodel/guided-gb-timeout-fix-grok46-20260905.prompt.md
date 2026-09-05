# BOUNDED INSTRUMENT FIX (≤ 40 min; finish and seal promptly): the gi70-longsolve report (frozen) records that box/lib/guided_gb.py's modular-Hilbert seed path aborted with "driver error 1" after an ERRONEOUS internal 9,900-second timeout (job (b): modular Hilbert seed then guided std on (I : c^∞) with a wp order) — before any Hilbert vector, guided run, or CRT stage existed — so a 170-minute budget produced no result from that path. TASK: (1) read guided_gb.py and find the internal timeout logic (its default, how it is applied to the Hilbert-series stage vs the std stage, and how the outer watchdog is meant to interact); reproduce the failure mode with a small synthetic ideal and an artificially small internal timeout; (2) FIX it minimally: the internal per-stage timeout must be configurable (CLI flag and Python API), default to "no internal timeout" when an outer watchdog is declared, and on expiry must return a typed INCONCLUSIVE_TIMEOUT with the stage name (never a bare "driver error 1"); keep every existing control and promotion-policy behavior byte-identical (PromotionPolicy.exact_q, MODULAR_UNIT_NOT_PROMOTED); (3) add a unit test (box/lib/tests/ or alongside) that exercises: normal completion, internal-timeout expiry typed correctly, and the control battery unchanged; run the existing controls (the known-empty / known-nonempty / tame-automorphism controls in the census-sweep report) through the patched module and confirm identical verdicts; (4) commit the patch to box/lib/guided_gb.py with a clear header comment and list the diff in the report. FALLACY-v2 (an instrument change must not alter any verdict; show the control replay). No fleet. ≤ 45 min; no ledger edits; no jc2-lean; no ideation-*. Drivers to box/guided-gb-fix-20260905/.
Report: xmodel/guided-gb-timeout-fix-grok46-20260905.md
Seal (<!-- BODY-END -->); 4-10KB; 45 min.
charged_input=xmodel/gi70-longsolve-sol56-20260905.md
charged_input=xmodel/census-sweep-grok46-20260905.md
charged_input=box/lib/guided_gb.py
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/guided-gb-timeout-fix-grok46-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
9b4c986f1722a37bd0c7237e6b7bc69380894c70f702b8a1bc3781b128ce74cb  {{LANE_INPUTS}}/gi70-longsolve-sol56-20260905.md
58146fdb40740b9491b7d0390f8f8b38b164bfffba83b81d00e0f5972fc1e404  {{LANE_INPUTS}}/census-sweep-grok46-20260905.md
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
