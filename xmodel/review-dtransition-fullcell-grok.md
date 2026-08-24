# Hostile review: `NONEMPTY-SINGULAR-OR-LOWER-RANK`

| Field | Value |
|---|---|
| Claim | `NONEMPTY-SINGULAR-OR-LOWER-RANK` (one promoted modular D25 `A^14` cell; band-26 compatibility only) |
| Verdict | **CONFIRMED** |
| Smallest failing witness | none |
| Evidence tier | mod `p=105337`, fiber `a00pp`, cell 0 with `(W1,W2)=(31931,9457)`; exact triangular pullback + unreduced source dual jets; two registered points plus four extra same-cell probes for constancy; not a component / inverse-limit / char-0 object |
| Reviewer | Grok 4.6 (adversarial different-model verifier) |
| CLI | `grok 1.0.5 (5115b46bc909) [stable]` |
| Python | 3.14.6 (`/opt/homebrew/opt/python@3.14/bin/python3.14`) |
| Host | Darwin arm64 |
| UTC | 2026-08-24T02:51:07Z |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `8bf25a52f5f6c20886b77c6d9aeeb879eb18f8e4` |
| Scratch | `/tmp/dtransition-fullcell-grok-ghuhSs` (fresh `mktemp -d`) |

**Promotion.** This modular full-cell compatibility record may be promoted off producer-checked provisional. Nothing else may. In particular: the origin is a certified common zero of rank five, a nonzero `5 x 5` minor licenses generic differential rank at least five, and the preregistered rank-six-at-origin gate failed. The repeated `mu` relation is a two-point (and extra-sample) structural signal, not an identity.

**Quarantine if this review is treated as a failure.** Do not feed `NONEMPTY-SINGULAR-OR-LOWER-RANK` into a dimension or component statement, a generic-rank-exactly-five claim, a band-28 child, a persistence or inverse-limit statement, a formal germ, a characteristic-zero lift, algebraization, a polynomial Keller map, or a Jacobian-conjecture counterexample. Do not treat `mu` as a polynomial identity.

**Dirty-state perimeter.** HEAD is clean for every tracked D25/source file named in the JSON manifest (`cases/d25_eplus.py`, `cases/valuation_e.py`, `cases/valuation_e2.py`, parked cells, D21 pickle, and the rest). Workspace dirt is unrelated ledgers (`APPROACHES.md`, `AUDIT.md`, `COORDINATION.md`, `PROGRESS.md`, `pilot-local.log`) plus untracked round-1 case directories and xmodel notes, including this child. Those dirty files are not inputs of the six-function chain.

---

## Claim under review (not enlarged)

1. On the stated `p=105337`, `a00pp`, cell-0 `A^14`, the six compatibility functions are the canonical left-cokernel contractions of the unreduced source-defined band-26 equations after exact D25 and band-24 triangular reconstruction; simultaneous vanishing is equivalent to affine solvability in the ten new coordinates. No D43 object enters.
2. The origin is a certified common zero. Its exact `6 x 14` Jacobian has rank five, including the displayed nonzero `5 x 5` minor `39793`, and no `6 x 6` minor is asserted.
3. The deterministic free-coordinate point `1..14` is on the same promoted cell after exact completion, has the reported nonzero function vector, and its Jacobian has rank five with the displayed minor `104469`.
4. The constant vector `mu=(104372,48519,44983,31248,84848,1)` annihilates the values and Jacobians at the two registered points. The producer correctly labels this a structural signal, not a polynomial identity or generic rank-five upper bound.
5. The only legitimate conclusion is: this modular full-cell compatibility locus is nonempty and the generic differential rank is at least five; the preregistered rank-six-at-origin gate failed. No dimension/component, persistence, band-28, inverse-limit, germ, characteristic-zero, algebraization, polynomial-map, or JC2 inference follows.

---

## Verdict table

| Clause | Verdict | What would have flipped it |
|---|---|---|
| Six functions = canonical left cokernel of unreduced band-26 after exact D25/band-24 pullback; vanishing iff affine solvability; no D43 | **CONFIRMED** | D43 import/artifact in the chain; `A_26` not rank 4; vanishing disagrees with `solve(A,b)`; production `-C_k` prefix gradient surviving the frontier replay |
| Origin is a common zero; exact Jacobian rank 5 with minor `39793`; no `6 x 6` asserted | **CONFIRMED** | origin `C(s)≠0`; a `6 x 6` minor nonzero; displayed `5 x 5` determinant `0` or not `39793` |
| Sequence `1..14` on the same cell; reported nonzero `C`; Jacobian rank 5 with minor `104469` | **CONFIRMED** | different `(W1,W2)` / cell index; `C=0`; det `≠104469`; rank 6 |
| `mu` kills values and Jacobians at the two registered points; correctly not an identity | **CONFIRMED** | `mu·C≠0` or `mu J≠0` at a registered point; report promoting `mu` to a polynomial identity or to generic rank exactly five |
| Scoped conclusion only: nonempty + generic rank `≥5`; origin rank-six gate failed; no later inference | **HONEST** | hidden band-28 / component / char-0 / JC2 promotion |

---

## What was rerun, independently, and not

```bash
/opt/homebrew/opt/python@3.14/bin/python3.14 \
  cases/round1_dtransition_fullcell/fullcell_compat.py --selftest
# PASS selftest: registries, D43 exclusion, exact derivatives/solve

SCRATCH=$(mktemp -d /tmp/dtransition-fullcell-grok-XXXXXX)
# SCRATCH=/tmp/dtransition-fullcell-grok-ghuhSs
/opt/homebrew/opt/python@3.14/bin/python3.14 \
  cases/round1_dtransition_fullcell/fullcell_compat.py --run \
  --out "$SCRATCH/results.json"
# origin compatible/rank: True 5
# sequence compatible/rank: False 5
# VERDICT: NONEMPTY-SINGULAR-OR-LOWER-RANK
```

Scratch `--run` is **byte-identical** to `cases/round1_dtransition_fullcell/results.json` (`cmp` silent; SHA-256 `f15be4e2194692756df743b3c05be13006f0e93eadb1884e933d599c7b01cdbf`). Not stale.

Independent work, **not** `independent_replay.py` and **not** stored `A26_rank` / `compatibility_jacobian_rank` / `compatible` / `verdict` strings as authority:

- Rehashed all 24 `source_manifest` entries against disk: **0 mismatches**. Recomputed `source_manifest_sha256` = `9392233838ae7e015a88177d7c6a2abac64fef94a36f72578f59ecc171b3a2c1`.
- Rebuilt both registered points from `d25_eplus` + unreduced `valuation_e2.build_jets` / `euler_rows`. Extracted `A_26` and `E_26` from the dual jet. Recomputed the canonical left kernel. Re-formed `C_i = λ_i · (-E_26)`. Checked vanishing against an independent modular `solve`.
- Independent stdlib RREF: `rank(A_26)=4`, `rank(J_origin)=5`, `rank(J_sequence)=5`.
- Leibniz expansion (not producer RREF) of the two displayed `5 x 5` minors: `39793` and `104469`. All `C(14,6)=3003` origin `6 x 6` minors vanish; all 3003 sequence `6 x 6` minors vanish.
- `mu` pairings on rebuilt values and on both Jacobians, plus a one-unit negative control.
- Four extra same-cell free assignments (constant 2, unit in `x57`, `17·(1..14)`, and `i^2+3`) to try to falsify constancy/rank four of `A_26`. All four stayed on cell 0, reproduced the same `A_26`, rank 4, and the same six `λ_i`.
- Isolated `Delta = P - C_k Y` at prefix level 18: unit finite difference in `uf18` equals `1-C_k`, not `-C_k`. Replacing the patch by `-C_k` makes the origin displayed minor `21534` and makes the sequence frontier tangent **inconsistent at free column `x68=uf18`**.
- After reconstruction, `sys.modules` contains no `d43*` / `nffid` module.

Not done, and not required by the scoped claim:

- No global symbolic identity for `mu`. Extra samples also satisfy `mu·C=0`; that is recorded below as a non-promotion.
- Band 28 was not touched.
- No search for a non-origin compatible point of Jacobian rank six. The preregistration asks for ranks at registered zeros; the origin is the only registered zero.

---

## Hashes

| object | SHA-256 |
|---|---|
| `cases/round1_dtransition_fullcell/fullcell_compat.py` | `c9b9ac1cc3efbc6b18d72e5444102aabdc9ab4716ca2f3ed59730e2695ff28c9` |
| `cases/round1_dtransition_fullcell/PREREG.md` | `16b21db9c3a9f179e96589f2b3cf4c2472c63483420596e8a2f9de3a71ba5628` |
| `cases/round1_dtransition_fullcell/results.json` (banked and scratch rerun) | `f15be4e2194692756df743b3c05be13006f0e93eadb1884e933d599c7b01cdbf` |
| `xmodel/round1-dtransition-fullcell-20260824.md` | `2b25b3ac5591360f2bac2f1c74f1c97bb936f1826f6aaed3d2969ad37be1f5df` |
| `source_manifest_sha256` | `9392233838ae7e015a88177d7c6a2abac64fef94a36f72578f59ecc171b3a2c1` |
| `cases/round1_dtransition/transition_symbol.py` | `869ff70bf04a991fe2e98e420951b26b94041ef01c91bec087d92b83f3fbe91d` |
| `cases/round1_dtransition/samples.json` | `7ef37f359f518e4e6af3a8a00c3fb4f6d4fbf354d33481fef17fec6d44f51030` |
| `xmodel/round1-dtransition-20260824.md` | `44611afa236b71a5cf133591daccf472ccfebb299333e1a1303854e9b94006db` |
| `xmodel/review-dtransition-grok.md` | `617c29cffa9e321ab5e5027543d2f6ee800e2ac94eab3ecb37f0ab494aefed74` |
| parked `d25fam_p105337_a00pp.ms` | `ef6db7e9ad36666537475fabf8238887de0c7e6d8f02c9381eaa7c810cbe4fe2` |
| `cases/valuation_e2.py` | `c1a858fbe53c291038b0386c124dbfd4bc79400eedc6b9d5d49a4088736d08f8` |
| `cases/d25_eplus.py` | `e964d2b467f76696f16ccef505f6f66cce7d68e722004bb1a70b6e1cf4f21e7c` |
| `directionb_tails_D21.pkl` | `b4ba8dfcd9755fb3201780cd97c1d2ef38bd26d2d1b023521a0e62a3d6db169e` |

The parent one-band tool and samples hashes match the already-reviewed `FREE-TAIL-SIGNAL` record. Parked D25 cells match that same reviewed bank.

The JSON manifest does **not** hash `fullcell_compat.py` itself or this child producer report. The parent D1 report, the parent hostile review, the preregistration, and every reconstruction/source artifact are hashed. A byte-identical scratch `--run` binds the current tool to the banked JSON; this is a provenance-prose nit, not a stale-artifact failure.

---

## 1. Six functions, pullback, solvability, no D43

The band-26 block is cut from unreduced `euler_rows` after the exact D25 certificate:

1. 34-row parked cell solve on the fourteen free coordinates at fixed `(W1,W2)=(31931,9457)` (cell index 0 of the sixteen `a00pp` copies).
2. Pristine D21 groupwise pivots, affine `tg1_44,tg2_44` probe, and rank-four deep zero-completion.
3. Band-24 frontier completion with kernel frees held at zero.
4. Source dual jets; `A_26 = d(Row_26[η^{0,3,...,27}])/d(tf1_53,...,tg02_58)`, `rhs = -E_26`.

`rank(A_26)=4` independently. The canonical left kernel is the six stored `λ_i`, each killing `A_26`. The functions are `C_i(s)=λ_i·(-E_26(s))`. At both registered points, `C=0` if and only if `solve(A_26,rhs)` returns a particular solution. That is affine solvability in the ten new coordinates, not a kernel-dimension count.

Rebuilt origin: `C=(0,0,0,0,0,0)`, `rhs=0`, particular solution exists (the new-coordinate origin). Rebuilt sequence: `C=(23070,55420,82249,287,11111,1237)`, `solve` returns `None`. These six pairings are byte-equal to the already-reviewed parent interior cokernel pairings at `p=105337`. Parent witness `A` equals parent interior `A` equals this full-cell `A_26`.

The five varying prefix coordinates on this cell are exactly `FIXED_DIFF=(uf18,vf1_34,vf1_36,vf2_34,vf2_36)`: `x68=uf18` and `x72,x73=vf2_{34,36}` are free, `x70,x71=vf1_{34,36}` are dependent. `uf24` is an aux-zero, `uf30` is pinned at 0, and `(A_i,W_i)` are fixed by fiber and cell. The tangent therefore has to track those five prefixes through the source.

Production `other_block` writes the correct overlapping **value** `P-C_k Y` at slots 12/18/24/30, but writes gradient `-C_k` whenever a gradient column exists. The full-cell patch changes that coefficient to `1-C_k` and exposes the five prefixes as dual columns. Isolated check at the sequence point (`uf18=8`, twist `C_1=Z[18]=64171`):

```text
1 - C_1  = 41167
- C_1    = 41166
Δ_{18}(uf18+1) - Δ_{18}(uf18) = 41167
```

The unit finite difference of the shared-prefix slot is `1-C_k`, not `-C_k`. Substituting `-C_k` into the patched `other_block`:

- at the origin, frontier replay still closes (the prefix *value* is zero), but the displayed `5 x 5` determinant becomes `21534 ≠ 39793`;
- at the sequence point, the rank-four band-24 tangent is inconsistent at free column `x68=uf18`.

That is the live discriminator the producer cited. The `1-C_k` patch is required, and it is the correct local derivative of `P-C_k Y`.

`A_26` is identical at the two registered points and at the four extra same-cell probes, always rank four, always the same `λ`-basis. The typing claim (a first-occurrence band-26 coordinate pairs only with slot-zero leading factors at this band) was not falsified. This is still a finite-point measurement on one modular cell, not a polynomial-identity certificate that `A_26` is constant as an element of `F_p[x_{57},...,x_{27}]^{10×10}`. Inside the declared two-point full-cell scope, with the extra probes failing to break it, that is the claim, not a defect.

No D43 path occurs in `SOURCE_FILES`. After `reconstruct_free`, no `d43*` / `nffid` module is loaded. `directionb_compress` is the D21 no-log window loader used by D25 membership, as in the parent review; it does not assemble `A_26` or `C`. Frozen `row22red` / `core23` / `row22compat` are `a00pp` pristine gates, not the band-26 source. `eplus_certify` is imported by `d25_eplus` at module load and is not used to build the six functions.

`jmul` uses `float64` with the documented bound. Rechecked: `34·42·p^2 = 1.584e13 < 2^53 = 9.007e15`. Extending `GD` by the five prefix columns does not change the per-entry accumulation bound.

Tangent ranks at both registered points, recomputed from the chain rather than from stored rank fields:

| gate | origin | sequence |
|---|---:|---:|
| 34-row cell dependent block | 10 | 10 |
| D21 + Row-22 reconstruction (`86 × 28`) | 28 | 28 |
| band-24 frontier block | 4 | 4 |
| band-26 new-coordinate block | 4 | 4 |
| six-function Jacobian | 5 | 5 |

The reconstruction tangent uses every pristine D21 row plus all ten Row-22 rows, not merely the 22 square pivots, and replays all 86 differentiated equations as zero. That is the correct implicit-function pullback: the extra rows are cell syzygies and must remain in the tangent kernel. Kernel frees of the rank-four deep and frontier solves stay at the registered zero-completion, including their derivatives.

---

## 2. Origin: common zero, rank five, minor 39793

The origin is the banked D25 witness: all fourteen free coordinates zero, all ten dependent cell coordinates zero, `W=(31931,9457)`, no frontier correction, residual through band 24 equal to the zero array, `E_26=0`. Hence `C=0` and the ten new coordinates are affinely solvable (in fact linearly, with particular solution 0).

The exact `6 x 14` Jacobian, recomputed through cell / reconstruction / prefix / frontier, equals the banked matrix. Independent RREF rank is five. The displayed minor on function rows `0,1,2,3,4` and free columns `x57,x62,x65,x68,x16` has Leibniz determinant `39793 ≠ 0`. `rank_six_minor` is `null`. All 3003 `6 x 6` minors vanish, so no unstated rank-six witness is hiding in the matrix.

A nonzero `5 x 5` minor at one `F_p`-point proves that this minor, as a polynomial on `A^{14}`, is not the zero polynomial. That is the only license for “generic differential rank at least five.” It is not a rank-six certificate and not a component dimension.

---

## 3. Sequence point `1..14`

Free coordinates in the registered order are set to `1,2,...,14`. The reconstructed point remains cell index 0 with the same `(W1,W2)`. Frontier completion is applied, with exactly the four nonzero pivots

```text
tf1_51=4638, tf1_56=91894, tf2_51=11461, tf2_56=14361
```

and residual through band 24 then zero. Rebuilt `C=(23070,55420,82249,287,11111,1237)`, all six entries nonzero, `solve(A_26,rhs)` inconsistent. This is a point of the same promoted cell outside the `X27 -> X25` image.

Recomputed Jacobian equals the banked matrix, RREF rank five. Displayed minor on the first five function rows and free columns `x57,x59,x60,x62,x63` has Leibniz determinant `104469 ≠ 0`. All 3003 `6 x 6` minors vanish. `rank_six_minor` is `null`.

---

## 4. `mu` is a structural signal, not an identity

```text
mu = (104372, 48519, 44983, 31248, 84848, 1)
```

Independent matvecs: `mu` kills both rebuilt function vectors and both Jacobians. One-unit mutation of the origin function vector is *not* killed. The left kernel of each `6 x 14` Jacobian is exactly this one-dimensional line, recomputed rather than read from a rank field.

The producer does not promote this to a polynomial identity on `A^{14}` and does not upgrade “generic rank at least five” to “generic rank exactly five.” That labeling is correct. The two exact symbolic-source attempts that timed out are representation-growth limits, not evidence.

Hostile extra observation, **not** used to enlarge the verdict: the four additional same-cell probes also satisfy `mu·C=0`. That is still a finite set of samples. It is not an identity certificate, not a proof that the sixth cokernel equation is redundant as a polynomial, and not a generic-rank upper bound. This review does not infer that identity.

---

## 5. Scope of `NONEMPTY-SINGULAR-OR-LOWER-RANK`

The preregistered discriminator at the origin was a nonzero exact `6 x 6` Jacobian minor. That gate failed. A certified common zero exists, and every registered zero tested (namely the origin) has Jacobian rank five, witnessed by a nonzero `5 x 5` minor. The verdict name is therefore the only licensed one.

This proves:

- the six source-defined compatibility functions exist on this selected modular `A^{14}` cell;
- their common zero locus is nonempty;
- their generic differential rank is at least five;
- the origin is rank five, not six;
- a deterministic point of the same cell is cut by compatibility.

It does **not** prove:

- generic rank exactly five, or that `mu` is an identity;
- dimension, reducedness, or component structure of the zero locus;
- existence or nonexistence of a non-origin compatible point of rank six;
- anything at band 28 or later;
- persistence, an inverse system, a formal germ, a characteristic-zero point, algebraization, a polynomial map, or a Jacobian-conjecture counterexample.

The producer perimeter states this. `decide()` also contains an unregistered branch `NONEMPTY-ZERO-LOCUS;GENERIC-RANK6;ORIGIN-SINGULAR` for the mixed case “a zero exists and some tested (possibly non-zero) point has Jacobian rank six.” That branch is not a preregistered verdict and is not live on this data (both Jacobians have rank five). Software note only.

---

## Attack checklist

| Attack | Result |
|---|---|
| Stale results JSON | **Fail.** Scratch `--run` is byte-identical. |
| Accidental D43 / `D43-NF-FID` import | **Fail.** No token in the runtime chain, no module after reconstruct, no D43 artifact in `A_26`/`C`. |
| Functions not the source cokernel, or vanishing ≠ solvability | **Fail.** Rebuilt `C_i=λ_i·(-E_26)` matches; `solve` agrees with vanishing at both registered points and four extra points. |
| Jacobian is a finite-difference estimate | **Fail.** Exact implicit differentiation through cell, 86-row reconstruction, prefix dual jets, and rank-four frontier; both matrices recomputed. |
| Displayed minors are RREF bookkeeping | **Fail.** Independent Leibniz `39793` and `104469`; all `6 x 6` minors vanish. |
| `-C_k` is an equivalent prefix derivative | **Fail as a refutation of the patch.** Isolated FD equals `1-C_k`. `-C_k` changes the origin minor and makes the sequence frontier tangent inconsistent at `x68`. |
| `A_26` not constant / not rank four on the cell | **Fail to falsify at six points.** Same matrix, rank 4, same `λ` at origin, sequence, and four extra probes. Not a polynomial identity. |
| `mu` silently treated as an identity | **Fail.** Producer labels it a signal; this review does not promote extra-sample annihilation. |
| Field/fiber/cell mismatch | **Fail.** `p=105337` prime, fiber `a00pp`, radical frame, cell 0, `W=(31931,9457)`, `W1 W2 ≠ 0`. |
| Hidden band-28 / JC2 promotion | **Fail.** Report and JSON perimeter stop at this modular cell and band 26. |

---

## Final verdict

**CONFIRMED**

Evidence tier: modular, one promoted `p=105337` `a00pp` `A^{14}` cell, two registered points, unreduced source dual jets, exact triangular pullback. Independent source reconstruction, independent modular linear algebra, an isolated `1-C_k` finite-difference, a `-C_k` frontier-replay counterexample at `x68`, and a byte-identical producer rerun all agree. The compatibility zero locus on this cell is nonempty; both registered Jacobians have rank five with the displayed nonzero `5 x 5` minors; the rank-six-at-origin gate failed; generic differential rank is at least five and is not hereby shown to be exactly five. Nothing past that scope is confirmed.
