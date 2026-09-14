# Corrected (99,66) source chart

The sealed report is `../../xmodel/g9966-corrected-engine-astra-20260905.md`.
This directory contains the drivers and their evidence. A nonunit prefix is
not a survivor of the full chart. The support-only rational points have zero
Jacobian and fail the required nonzero D1 face.

## Entry points

- `source_data.py` derives the radii, faces and support exponents from the
  frozen printed source. `print-audit-derivations.md` supplies the hypotheses.
- `engine.py --branch delta2 --stage 8 --out PATH` runs a finite source
  checkpoint. Its cumulative compatibility adapter accepts stages 0–8 only.
  `delta52` is the other branch. The deep endpoint rows must use the target
  faces, so extending the compatibility adapter's integer stage is forbidden.
- `deep_driver.py` supplies the incremental finite and deep schedules.
  `deep_accelerated.py` orders the complete minor remainder blocks first.
  `deep_gauge_accelerated.py` uses the audited translation slice.
- `deep_resume_graph_faces.py` introduces the computed D1 coefficient graph
  and the nonzero Jacobian scalar. `deep_resume_jacobian_flint.py`,
  `deep_resume_jacobian_batch.py`, and `deep_resume_jacobian_quotient.py`
  continue exact global Jacobian coefficients on certified preceding loci.
  Their `--help` lists all required source, checkpoint and code paths.
  For an already-certified quotient checkpoint, use the separate successor
  `deep_resume_jacobian_quotient_resume.py`. Its exact zero-new-band resume
  control is `deep_quotient_resume_control.json`; it reuses the certified
  transition instead of reintroducing eliminated graph coordinates.
- `minor_merged_verify.py` independently replays the source/map ancestry and
  regenerates terminal rows. Its immutable version directories identify the
  verifier actually used by each certificate.
- `summarize_runs.py --jacobian PATH --jacobian PATH` curates completed
  records, recursively resolving ancestor snapshots by SHA-256. It is not
  an independent ideal verifier.

Production uses Python 3, SymPy, Singular and python-flint. Exact versions
and commands are retained in the fleet receipts and logs. Native arithmetic
is over Q; every smaller occurring-variable ring embeds into the declared
full free ring. Rational row denominators are cleared before Singular input.

## Custody and replay

Use the `run-code*` and `minor-verification-code-*` snapshots named in the
actual result metadata when reproducing an existing certificate. The live
top-level modules contain later fixes and are not silently substituted for
those snapshots. Historical controls use the frozen engine's compatibility
chart and reproduce the numerical units 6264 and 64. They do not claim the
same first unit after adding new source remainder equations.

The launch JSONs retain exact argument vectors and worker paths. Their
checkpoint path names are remote provenance names; all referenced local
copies must be located by the expected hash, not merely a matching basename.
The phase certificates record the field, generator order, source image map,
localizer, raw rows, rational pivots, permitted radical steps and residues.
The monic quotient transition retains the old ideal under its recorded
graph maps and retains both complex components. Combined A+B*d rows must
never be replaced by separate equations A=B=0.

`inputs.sha256` and `hash-check.txt` are the initial charged-input check.
The final report names the selected terminal results, independent replay
certificates and the owned worker's termination receipt. No ledger changes
or mathematical promotion outside that report are part of this lane.
