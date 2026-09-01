# Lean lane: K1-L17a + K1-L17 — local monogenicity and the tame different equality

You are a Lean formalization lane (Opus) executing the HIGH-risk Stage-1
lane of the Keystone 1 plan. Read
`xmodel/k1-mathlib-survey-and-plan-opus5-20260901.md` (entries K1-L17a,
K1-L17, and survey section A.4) first. You work in the Lean project
`jc2-lean/keystone-graph/` (single package, Mathlib pinned; the skeleton
and `scripts/box_build.sh` exist). You may write new module files under
`KeystoneGraph/` and add their imports to `KeystoneGraph.lean`.
NEVER run local `lean`/`lake`; verify exclusively with
`./scripts/box_build.sh` (green = `BUILD_EXIT=0`). Permitted axioms:
`propext`, `Classical.choice`, `Quot.sound`; no `sorry`; no new axioms.
If another lane has edited `KeystoneGraph.lean` meanwhile, merge imports
additively; never delete another lane's module.

## K1-L17a — local monogenicity (`KeystoneGraph/Monogenic.lean`)

A finite extension of DVRs (Noetherian local domains, both DVRs) with
separable residue field extension is monogenic: there is `x` with
`B = A[x]` (equivalently a `PowerBasis`). The survey found NO
`exists_powerBasis`/monogenicity declaration at the pin — check again
first (`Mathlib/RingTheory/DedekindDomain/`, `.../Different.lean`,
`PowerBasis` API, Krasner/unramified files) in case a usable form
exists under another name; if found, wrap it instead of re-proving.
Otherwise prove it: lift a primitive element of the residue extension,
adjust by a uniformizer (the classical argument via Nakayama on
`A[x] ⊆ B`). Est. 300–600 lines.

## K1-L17 — tame different equality (`KeystoneGraph/TameDifferent.lean`)

For a finite extension of Dedekind domains `B/A` in characteristic zero
(so residue extensions of the relevant primes are separable and
ramification is tame), with `𝔮` over `𝔭`, prove
`v_𝔮(differentIdeal A B) = e_𝔮 − 1` (ramification index
`e_𝔮 = Ideal.ramificationIdx`). Mathlib supplies the floor
`pow_sub_one_dvd_differentIdeal` (≥ direction) — the FALLACY guard from
the plan applies: citing the floor for the equality is refuted on
sight; the ≤ direction is the work. Route: localize to the DVR/DVR
case, use K1-L17a monogenicity, `conductor_mul_differentIdeal`
(`Different.lean:637`) and `aeval_derivative_mem_differentIdeal` to
reduce to `v_𝔮(f'(x)) = e − 1` for the minimal polynomial `f`, where
tameness (`e` a unit in the residue field, automatic in char 0) gives
the exact valuation of the derivative's lowest term. Est. 400–900
lines; split into helper modules if cleaner. State the theorem so
Stage-1 lane K1-L18 can consume it directly (explicit `A B : Type*`
with `[IsDedekindDomain]`-style hypotheses, not the Keystone setup).

## Report

Write `xmodel/k1-l17-tame-different-opus5-20260901.md`: statements
proved (verbatim), file SHA-256s, the box build tail, and axioms. If
genuinely blocked, land the maximal green partial (e.g. L17a alone) and
state the precise obstruction — no overclaims.
