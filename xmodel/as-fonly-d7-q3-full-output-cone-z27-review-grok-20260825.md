# Hostile different-model review — AS F-only D7 complete three-fibre output cones modulo 729

| Field | Value |
|---|---|
| Claim under review | Frozen producer: at each of the three pinned, reviewed Q3 affine fibres `0000`, `0270`, `0513`, the complete degree-at-most-seven output-coefficient cone `F=F0+27T` with `T` in `(Z/27)^72` makes every one of the 91 coefficients of `det J(F)-1` vanish modulo 729. Exact identity `det J(F0+27T)-1 = D0 + 27 A T + 729 det J(T_P,T_Q)` reduces the problem to the linear congruence `D0/27 + A T ≡ 0 (mod 27)`. Three-stage F3 Bockstein ranks/kernels `27/45 -> 36/81 -> 47/106` and `27/45 -> 43/74 -> 49/97`; liftable prior dimensions 61 of 81 and 52 of 74; new solution counts `3^106` and `3^97` |
| Overall verdict | **CONFIRMED** |
| Mathematics | **CONFIRMED** |
| Source typing | **CONFIRMED** (non-blocking notes below; none load-bearing) |
| Software | **CONFIRMED** (non-blocking notes below; none load-bearing) |
| Custody | **CONFIRMED** of the frozen two-host AWS run recorded below. Box02 and r6d are independent executions of one implementation, not independent implementations. `replay_all.sh` was not re-launched |
| Wording / scope | **CONFIRMED.** Producer body, preregistration, JSON `scope` / `refusal_scope`, and the next-modulus firewall match the licensed object |
| Finite fibrewise `Z/27` cone theorem | **CONFIRMED** |
| Fourth global linear Bockstein / mod 2187 / whole predecessor / all-depth / collision / characteristic zero / counterexample / no-lift / JC2 | **REFUSED** (not claimed by the producer body; not licensed here) |
| Strongest licensed scope | three pinned reviewed Q3 fibres, all 72 fixed-D7 output digits modulo 27, determinant modulo 729. One compiler at three inputs |
| Replay/custody | **CONFIRMED** of the frozen AWS Box02 and r6d runs recorded below. This review used read/search only; no Bash, Python, CAS, solver, or local Jacobian replay. Independent constant-term Jacobian arithmetic was done by hand on the stored supports |
| Smallest failing identity | none inside the displayed cone |
| Smallest missing hypothesis | none that breaks the numbered fibrewise claim. A fourth linear Bockstein, the whole predecessor scheme, and modulus 2187 are **missing by design** |
| Evidence tier | SHA-pinned exec of z27 / z9-prefix / two-level prefix / Q3 / Q4 / Q4-restore / H6 V2; integer identity `P_x Q_y - P_y Q_x - 1`; exact `/27` then `% 27` on all 91 slots; `729 det J(T_P,T_Q) ≡ 0 (mod 729)`; three F3 RREF stages with free-column kernels; 1296 P/Q pair remainders `% 729 == 0`; Q3-kernel differences `% 81 == 0` inside D7 and `72*kdim` mixed second differences `% 2187 == 0`; stored 72-digit particulars in `{0,…,26}` reconstructing as `P0+27T`; payload degree ≤ 7 and AS seed `(x-x^3,y) mod 3`; hand-checked constant term of `det J-1` divisible by 729 at all three fibres; rc 0 and stdout/JSON rank agreement |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Review constraint | read/search only; no Bash, Python, CAS, solver, web, or network; no producer/case/ledger/prompt edits; all substantive replay is the frozen two-host AWS run |
| Review window (UTC) | 2026-08-25 |

Producer report, preregistration, portable case, z27 compiler, remote launcher, replay wrapper, freeze/manifest, both AWS job trees (result, rc, stdout, stderr, start/end, SOURCE/OUTPUT hashes), the AWS `verify_frozen.py` run, the CONFIRMED z9 cone review, the CONFIRMED Q3 whole-kernel review, and the hash-pinned parent compilers through H6 V2 were reread in full before any verdict. No producer, case, prompt, parent, or ancestry file was edited.

---

## Required decisions

### Finite fibrewise `Z/27` cone theorem

**Correct.** On each of the three pinned reviewed Q3 affine fibres, the complete order-27 D7 output-digit cube is a linear congruence module over `Z/27` for `det J ≡ 1 (mod 729)`, and that module is nonempty. The quadratic remainder carries the factor `729` and is identically zero at this modulus. The compiled 91-row inventory is the full coefficient list of a degree-at-most-12 determinant of two degree-at-most-seven maps. Three exact F3 Bockstein stages have rank/kernel pairs `27/45 → 36/81 → 47/106` at `0000` and `27/45 → 43/74 → 49/97` at `0270` and `0513`. The projection of the final kernel onto the prior `Z/9` parameters has dimensions 61 of 81 and 52 of 74; the 45-dimensional fresh top-digit kernel of `A mod 3` accounts for the new exponents 106 and 97. Each displayed particular is a 72-tuple in `{0,…,26}` reconstructing as `F = F0 + 27 T`, and the SHA-pinned compiler asserts every 91-slot coefficient of the reconstructed integer determinant is divisible by 729 before writing JSON.

### Fourth linear Bockstein / modulus 2187 / whole predecessor

**Not licensed.** Modulo 2187 the term `729 det J(T_P,T_Q)` survives and is quadratic on the liftable prior stratum. A fresh order-729 output digit enters linearly. No coefficient is imposed modulo 2187, and no order-729 digit is a variable. Order-9 chart digits remain frozen inside `F0`.

### Strongest licensed scope after that decision

Three **pinned reviewed Q3 fibres** (`0000`, `0270`, `0513`), each with its displayed Q3 particular and with the reviewed Q3 kernel absorbed as an order-81 D7 output direction, for **all 72** polynomial output coefficients of total degree at most seven modulo 27, making `det J-1` vanish coefficientwise modulo 729 on the 91 slots of degrees 0 through 12. This is one implementation at three SAT-model inputs. It does not cover the rest of the Q5/global predecessor scheme, does not impose modulus 2187 or order-729 digits, and does not produce a `Z_3` point, a collision, a characteristic-zero counterexample, a no-lift theorem, or JC2.

### Source, arithmetic, coverage, or custody defects

- **None load-bearing.** The producer body's fibrewise hedge, the explicit `729 det J(T,T)` firewall, and the refusal list match the licensed object.
- **Non-blocking software:** several JSON flags (`literal_integer_replay_mod729_passed`, `exact_linearity_mod27_after_division_by27`, `q3_fresh_mixed_terms_divisible_by2187`) are written as the literal `True` after the corresponding asserts. The load-bearing objects are the asserts, the integer control counts `1296 / 1008 / 720 / 720`, the stored 72-digit particulars and `P_support`/`Q_support`, and rc 0. Those flags were not used as evidence.
- **Non-blocking source-typing:** the z27 compiler asserts degree at most seven on Q3-kernel differences, not on `P0,Q0` or on the reconstructed particular. Completeness of the 91-slot inventory is inherited from the pinned Q4 parent (`max_total_degree_P4 = max_total_degree_Q4 = 7` at all three models), from Q3 adjoining only `81*(H5+H4)` of degrees 5 and 4, from the D7 support of the 72 fresh digits, and from the stored reconstructed supports, which contain no monomial of degree ≥ 8. Derivatives of two degree-7 maps have degree at most 6, so the determinant has degree at most 12 and cannot grow a coefficient outside the 91 slots. An in-solver `sum(xy)<=7` assert on the reconstructed maps would close this hole locally; it is not a missing coefficient in the frozen run.
- **Non-blocking packaging:** dense integer / Bockstein matrices are not serialized, only SHA-256 plus ranks. Independent re-RREF from the payload is therefore impossible. Rank/kernel arithmetic `27+45=72`, `36+81=117`, `43+74=117`, `47+106=153`, `49+97=146`, the identities `47=27+20` and `49=27+22` against the prior-versus-liftable gaps, injectivity of the nested free-column parametrizations, and stdout/JSON agreement were checked. The AWS compiler is the Jacobian-level certificate for the 90 non-constant residual slots.
- **Non-blocking custody:** AWS `SOURCE.sha256` inventories only the z27 solver, launcher, and preregistration. The live parent chain is SHA-asserted inside the compiler (`EXPECTED_SOURCE` of the z9 file, then the already-reviewed z9 prefix chain). Result JSON `source_sha256` records that z9 parent hash, not the z27 file hash; the z27 hash `f6eaa0a0…` is in MANIFEST and both-host `SOURCE.sha256`. `OUTPUT.sha256` correctly excludes itself (the z9 self-hash snapshot is not repeated). Host timestamps and stderr differ; result JSON and stdout are byte-identical per fibre.
- **Not a defect:** Box02 and r6d are two executions of one implementation. Rank/kernel pairs `47/106` versus `49/97`/`49/97` are input-dependence of that compiler, not a second implementation.
- **Not a defect:** the displayed z9 particular fails to lift at every fibre (`stored_z9_particular_lifts: false`). That is a statement about one previously printed point, not a no-lift theorem for the cone.

### Independent replay

Not re-launched. Frozen Box02 and r6d commands and hashes are recorded in the custody section below.

---

## Promotion

**Accept `AT EACH OF THE THREE PINNED REVIEWED Q3 AFFINE FIBRES 0000, 0270, AND 0513, THE COMPLETE FIXED-D7 OUTPUT-DIGIT CONE F = F0 + 27 T WITH T IN (Z/27)^72 IS A LINEAR CONGRUENCE MODULE FOR det J(F) ≡ 1 (MOD 729) ON ALL 91 COEFFICIENTS OF DEGREES 0 THROUGH 12, AND THAT MODULE IS NONEMPTY. THE THREE EXACT F3 BOCKSTEIN STAGES HAVE RANK/KERNEL 27/45 → 36/81 → 47/106 AT 0000 AND 27/45 → 43/74 → 49/97 AT 0270 AND 0513. OF THE PRIOR MOD-243 MODULES, 3^61 OF 3^81 AND 3^52 OF 3^74 LIFT; ADDING THE 45-DIMENSIONAL FRESH TOP-DIGIT KERNEL GIVES 3^106 AND 3^97 SOLUTIONS. EACH DISPLAYED PARTICULAR REPLAYS THE INTEGER DETERMINANT COEFFICIENTWISE DIVISIBLE BY 729 AND REDUCES TO (x-x^3, y) MODULO THREE. THE REVIEWED Q3 KERNEL IS ABSORBED AS AN ORDER-81 D7 OUTPUT DIRECTION, WITH EVERY MIXED SECOND DIFFERENCE AGAINST THE 72 FRESH BASES DIVISIBLE BY 2187. THE PREVIOUSLY DISPLAYED MOD-243 PARTICULAR IS TERMINAL AT EACH FIBRE; THE COMPLETE FIBRE IS NOT.`**

**Refuse `WHOLE Q5/GLOBAL PREDECESSOR SCHEME`, `FOURTH GLOBAL LINEAR BOCKSTEIN`, `MODULUS 2187`, `ORDER-729 DIGITS`, `ALL-DEPTH COMPATIBLE TOWER`, `Z_3 SOLUTION`, `COLLISION`, `CHARACTERISTIC-ZERO COUNTEREXAMPLE`, `NO-LIFT`, and `JC2`.**

On the aligned F-only `D=7` chart, after the CONFIRMED Q3 whole-kernel gate and the CONFIRMED `Z/9` cone:

- Over `Z`, write `P = P0 + 27 T_P`, `Q = Q0 + 27 T_Q`, with `T_P, T_Q` of total degree at most seven and with `(P0,Q0)` one literal Q3 particular. This is 36+36=72 variables in `Z/27`. The Jacobian determinant is bilinear, so
  ```text
  det J(P0+27 T_P, Q0+27 T_Q) - 1
    = D0 + 27 L(T) + 729 det J(T_P, T_Q),
  ```
  where `D0 = det J(P0,Q0)-1` and `L(T) = det J(P0,T_Q) + det J(T_P,Q0)`. Expanding the first derivatives gives the same identity termwise: the cross term is `27(P0_x T_{Q,y} + T_{P,x} Q0_y - P0_y T_{Q,x} - T_{P,y} Q0_x)` and the quadratic is `729(T_{P,x} T_{Q,y} - T_{P,y} T_{Q,x})`. Since `729 ≡ 0 (mod 729)`, the condition `det J ≡ 1 (mod 729)` is exactly the linear system `(D0/27 + A T) ≡ 0 (mod 27)`, once `D0` is known to be divisible by 27 (asserted coefficientwise on all 91 slots before any `% 27`).
- Orientation is the parent integer determinant
  `P_x Q_y - P_y Q_x - 1`,
  with `nderivative(·,0)=∂/∂x`, obtained transitively from `replay_full_q4_restore.py` via `solve_full68.py`, `solve_q3.py`, and the two-level prefix. H6 V2 inserts the AS seed in source:
  `P = (x-x^3) + 3U + 9C + 27W + 81(H7+H6)`,
  `Q = y + 3V + 9D + 27Z + 81(J7+J6)`.
  Every subsequent order-27 or order-81 correction is `0 mod 3`, so every reconstructed map reduces to `(x-x^3, y) mod 3`.
- The 91-slot order is
  `slots = [(i, d-i) for d in 0..12 for i in 0..d]`,
  length `1+2+…+13 = 91`. The D7 support is the same convention in degrees 0 through 7, length 36, hence 72 combined variables. Parent `max_total_degree_P4/Q4 = 7` at all three models; Q3 adds only degree 4–5 at order 81; fresh digits are D7. Stored reconstructed supports contain no monomial of total degree ≥ 8. The determinant of two degree-7 maps has degree at most 12, so the 91 slots are the complete coefficient inventory.
- Stage 0: `A3 = A mod 3`, `rhs = (-D0/27) mod 3`. Rank 27, kernel 45 (`27+45=72`) at all three parents, matching the CONFIRMED z9 first stage. Stage 1 writes `T = p0 + K0 s0 + 3 x1` without reducing the integer expression, divides the integer residual and the integer action of `K0` by 3, and stacks `[K0_carries | A3]` on `(s0, x1)`. Rank/kernel `36/81` and `43/74` satisfy `rank + ker = 117` and match the CONFIRMED z9 Bockstein. Stage 2 analogously writes `T = T9_base + K1tilde s1 + 9 x2`. The map `stage1_to_T` includes the affine constant `p0` even on a kernel vector; the compiler subtracts `p0` (not `T9_base`) from those images, which is the correct linear part `K0 s + 3 t1`. Rank/kernel `47/106` and `49/97` satisfy `47+106=153=81+72` and `49+97=146=74+72`. Independently, `rank(stage 2) = rank(A3) + (prior_dim - liftable_dim)` recovers `27+20=47` and `27+22=49`.
- The map `(s0,x1) ↦ K0 s0 + 3 x1` is injective `F3^{117} → (Z/9)^{72}` because `K0` is in free-column echelon form: reducing mod 3 forces `s0=0`, after which `3 x1 ≡ 0 (mod 9)` forces `x1=0`. The further map `(s1,x2) ↦ K1tilde s1 + 9 x2` is injective `F3^{len(K1)+72} → (Z/27)^{72}` by the same argument against the injective z9 kernel embedding. Unreduced integer representatives of `T9_directions` change stage-2 carry columns by vectors in `col(A3)` and do not change the column space of `[K1_carries | A3]`, nor the injectivity after reduction modulo 9. Solution counts are therefore exactly `3^{ker}`.
- Projection: each stage-2 kernel vector is `(s1, x2) ∈ F3^{len(K1)+72}`. The first `len(K1)` coordinates span a space of dimension `projection_dimension`. The kernel of that projection is `{s1=0, A3 x2 = 0} ≅ ker(A3)`, dimension 45. The asserted identity `len(K2) = projection_dimension + 45` is this exact sequence, not an independent measurement, and it holds: `106=61+45`, `97=52+45`. The rank routine transposes before RREF; rank is transposition-invariant, so this is not a row/column mix-up. Distinct kernel basis vectors cannot represent the same `T` class, by injectivity above.
- Linearity controls that actually ran: all `36*36=1296` opposite-output pairs with bilinear remainder divisible by 729 and with `(det//27) ≡ D0/27 + A_i + A_j (mod 27)`; Q3-kernel output differences divisible by 81 with degree at most 7; mixed second differences against all 72 fresh bases divisible by `81*27=2187`, counts `72*14=1008`, `72*10=720`, `72*10=720`. Same-output doubling is identically affine by bilinearity (`det J(T_P,0)=0`), so the omitted doubled-basis loop is not a missing quadratic. There is no hidden order-9 *variable*: the Q3 kernel is order 81, and order-9 digits of the H6 chart are frozen in `F0`.
- Hand check of the constant slot, from the stored supports, not from a stored boolean. Constant term of `det J` is `P_x(0) Q_y(0) - P_y(0) Q_x(0)`:
  - `0000`: `1·1 - 108·54 = 1-5832`, so `det J-1 = -5832 = -8·729`;
  - `0270`: `1·1 - 162·162 = 1-26244`, so `det J-1 = -26244 = -36·729`;
  - `0513`: `1·1 - 270·162 = 1-43740`, so `det J-1 = -43740 = -60·729`.
  The other 90 slots are the compiler's integer replay at rc 0, charged against the stored `T` and the reconstructed maps.

**Do not promote this to:** coverage of the whole Q5/global predecessor scheme; a fourth global linear Bockstein; a constant RREF over free order-9 coordinates; modulus 2187; an order-729 digit layer; an all-depth compatible tower; a `Z_3` point; a collision; a characteristic-zero counterexample; a no-lift theorem; or JC2. Do not read three SAT-model inputs as three structural bases. Do not read failure of the previously displayed z9 particular as emptiness of the fibre.

**Smallest honest successor.** Keep the three liftable prior strata (dimensions 61 and 52) and impose modulus 2187 as a quadratic Kuranishi/Fitting or exact trit-SAT gate on that entire nonreduced stratum, with a linear fresh order-729 output digit. Do not write a fourth linear Bockstein. Do not silently promote these three fibres to the global scheme.

---

## Quarantine

The following readings are refused and must not be reused as live mathematics:

- this gate as a statement about the whole Q5 fibre, the global predecessor scheme, or any Q5 model other than the three consumed Cartier-zero SAT endpoints;
- this gate as a fourth global linear Bockstein, or as a constant linearized matrix in the presence of free order-9 coordinates;
- this gate as modulus-2187 closure, as order-729 digits, as an all-depth lift, as a `Z_3` solution, as a collision, as a characteristic-zero counterexample, as a no-lift theorem, or as JC2;
- the failure of the previously displayed z9 particular to lift as emptiness of the fibre (the complete prior module has a 61- or 52-dimensional liftable stratum);
- three jobs as three independent implementations;
- two AWS hosts as two implementations;
- stored JSON booleans as a substitute for the integer asserts, control counts, particulars, and `P_support`/`Q_support`.

---

## Hostile checks

Tried hard, and failed, to replace the consumed Q3 parents by reset or unrelated maps, or to consume only a Q3 particular without its kernel; to flip the Jacobian orientation; to make `729 det J(T_P,T_Q)` contribute a 729-relevant remainder; to shrink the 91-slot inventory or the 72 D7 variables; to leak a degree-8 output or a degree-13 determinant coefficient past the 91 slots; to skip exact division by 27, 3, or 9, or to reduce modulo 3 first; to make `stage1_to_T` keep the affine constant `p0` on kernel directions, or to subtract `T9_base` instead of `p0`; to break RREF inverses in `F3`, kernel-carry columns, or high-digit reconstruction; to make rank/kernel fail `n = rank + ker`, to make `106 ≠ 61+45` or `97 ≠ 52+45`, or to make `3^{106}`/`3^{97}` disagree with the frozen integers; to find a duplicated `T`-parametrization or a row/column-rank swap in the projection; to skip a P/Q pair or a Q3-kernel/fresh mixed difference; to find a hidden order-9 *variable* inside the 72-cube, a Q3-kernel direction of order other than 81, or a nonlinear parameter direction hidden by absorption; to accept `literal_integer_replay_mod729_passed` without the assert site, stored particular, and stored supports; to make the reconstructed maps miss the AS seed `(x-x^3,y) mod 3` or grow a degree-8 monomial; to make the constant term of `det J-1` fail divisibility by 729; to read Box02 and r6d as independent implementations; or to promote the fibrewise cone to whole-predecessor, a fourth linear Bockstein, modulus 2187, `Z_3`, collision, counterexample, no-lift, or JC2 coverage.

### 1. Transitive source chain and consumed Q3 parents

Runtime `exec` pins, each asserted before compile. z27 SHA-pins the z9 compiler and execs only the prefix before `base = []`; that prefix SHA-pins and execs the two-level prefix before `stages = []`, which fully execs Q3, which fully execs Q4, restore, and H6 V2. Nested `PARENT_OUTPUT_JSON` reuse writes Q4 then overwrites with Q3 on the same path; the frozen `q3_parent_output_sha256` values are the Q3 solver output.

| object | SHA-256 |
|---|---|
| z27 `solve_full_output_cone_z27.py` | `f6eaa0a0f1dabb785bdd4358fa84739d907820bc539cc619a1b692ad5755cb19` |
| z9 `solve_full_output_cone_z9.py` (asserted `EXPECTED_SOURCE`, stored as result `source_sha256`) | `2d2e0f5fa03c663201157d109a961055ebe1b3daad552b34954f20a633de32f7` |
| two-level `solve_two_level.py` | `cec50f9fd9bf9ce3311e5687658473e9c4d7577b4997ac96b1e1f3b3932d2fcd` |
| Q3 `solve_q3.py` | `14d69e65255482491293373bbbd212742e2077322931e65b8d5af215915d303b` |
| Q4 `solve_full68.py` | `ed19ea87d2252e9e483a5c3970549eeac2db62d064e7bd900698b600739180a4` |
| Q4 restore `replay_full_q4_restore.py` | `9fa649802565ad52a448c23e8091e9bdeca90576d35834a61ae19ed701fb119c` |
| H6 V2 `replay_global_q5_h6_v2.py` | `41e0e74ec4d318bdd33242dcb9053ce53572470570ab5d54f1431184eb789ffa` |
| H6 V1 (bytes patched in memory) `replay_global_q5_h6.py` | `75e153c3ea2a0de9ce2bf26ba13893e44a4092cd8b1bdd1d45256f12ac023eea` |
| z27 preregistration | `82dd16298f757873b2f4d3df22279b1b4d2b4864fab748f10a3acb056f285289` |
| z27 launcher `launch_remote_one.sh` | `db345d6e6f8bd37bfdc02a08f67c466347152c3feac9991aaec11e727cb23da7` |

Consumed SAT models, regenerated Q3 JSON, and previous z9 results match the CONFIRMED Q3 and z9 reviews on the nose:

| base | model SHA-256 | `q3_parent.json` SHA-256 | previous z9 result SHA-256 | Q3 kdim |
|---|---|---|---|---:|
| 0000 | `dbb405ac9ab12b9d4b01df6e934ac6979609dfd4eabbe2ccf65a65aaf8cdcb81` | `89c9b8bfb4c46b566e10e7f5716502b0a3b6f64af29a5f4e14234cc09b945187` | `3e6a559c5b4906b489b9c43350b95259a191c1fbe529656f32b52fdc40bd4f0a` | 14 |
| 0270 | `05627048aa3e648b975acc1ed47e97a451241c3544e7fa5b58a7c42a1cd4be03` | `9016e7737c7f3a31107a80f4da91e1e8cec7be686569cd548e55e135fcec4dfb` | `eb6936b975de974f26e0f571a3e1839ee118d6ed96ea12bf769ecd2f6015d97e` | 10 |
| 0513 | `9c319fe4d1a576569869cbccbcc7411fee5eb12dedaa4e6a820a395263820200` | `e2711128f358f5b65f215a2898ccf90fa10a7e1e6908ccdde7c9a4410290b4bb` | `c8716a9828b42f3b97f89a41e646b5fa8b8744fe5945ebfe1b24a42141b9fd1e` | 10 |

Those three Q3 output hashes are exactly the Q3 producer hashes. Mixed-control counts `1008/720/720` are `72` times those kernel dimensions. The live object is `ns["q3_kernel"]` after the Q3 exec, not a reset representative and not a truncated JSON kernel. The maps are the previously reviewed fibres.

### 2. Determinant orientation, identity, 91 slots, degree ≤ 7

`replay_full_q4_restore.py` defines

```text
det J - 1 = P_x Q_y - P_y Q_x - 1
```

with axis 0 the `x`-exponent. z27 obtains this function from the z9 prefix as `determinant_minus_one`. Support length 36 and variable count 72 are asserted and stored. Slot 8 is `(2,1)` in the inherited z9/two-level convention.

Bilinearity gives remainder `729 det J(T_P,T_Q)` on a P/Q pair, identically divisible by 729, hence `0 mod 729` and `0 mod 27` after `/27`. Doubling a single output is affine in that output (the other held at the base), so the 1296 opposite-output pairs are the complete quadratic design.

Degree bound: stored `P_support`/`Q_support` at all three fibres have `i+j ≤ 7` on every monomial, including those inherited from `P0`. A degree-8 term in `P0` cannot be cancelled by a D7 correction. Two degree-7 maps cannot produce a determinant monomial of degree > 12; the compiler also asserts every key of the reconstructed determinant has total degree ≤ 12. The 91-slot scan is therefore complete for this cone: there is no silently omitted coefficient.

### 3. Three Bockstein stages

`rref_solve` is Gaussian elimination over `F3` with `pow(a,-1,3)` (so pivot 2 scales by 2). Elimination is `value - scalar*pivot`. Kernel vectors put 1 on a free column and `(-work[row][free])%3` on pivots. Contradictions return `particular=None`; none occur.

Stage 0 uses the *integer* matrix `A` (not the z9 matrix already reduced mod 9) and `D0//27` before `% 3`. Extra 9-divisible parts of `A` vanish in the first carry, so stage 0/1 match the CONFIRMED z9 ranks. Frozen `stage_mod3` is rank 27, kernel 45 at all three. stdout prints the same numbers.

`stage1_to_T(v) = p0 + K0 v_s + 3 v_t` is not reduced. For kernel directions the compiler subtracts `p0`, leaving `K0 s + 3 t1`. Subtracting `T9_base` instead would have mixed the particular into the directions; that is not what the source does. Exact `/3` of `base + A·p0` and of `A·K0`, and exact `/9` of `base + A·T9_base` and of `A·T9_directions`, are asserted before the next `% 3`. Python `//` and `%` on possibly negative integers are the floor convention, consistent with the least-nonnegative residue used in the later `% 27` checks.

Independent rank verification from a stored dense matrix is not possible (only SHA-256). Arithmetic `rank+ker=n`, the block-rank identity `rank([K1_carries|A3]) = 27 + (prior-liftable)`, injective parametrization, and stdout/JSON agreement hold. Frozen integer-matrix SHAs differ across all three inputs, as required of one compiler at three bases (`f1811e9a…` / `7575cf98…` / `2b4a7937…`).

### 4. Projection onto the prior mod-243 modules

| fibre | prior `Z/9` ker | liftable | fresh `ker A3` | new exponent | check |
|---|---:|---:|---:|---:|---|
| 0000 | 81 | 61 | 45 | 106 | `61+45=106`, `81-61=20`, `27+20=47` |
| 0270 | 74 | 52 | 45 | 97 | `52+45=97`, `74-52=22`, `27+22=49` |
| 0513 | 74 | 52 | 45 | 97 | same arithmetic |

The last 72 columns of the stage-2 matrix are `A3`, so `{s1=0}` inside `K2` is exactly `ker(A3)` and has dimension 45 whether or not `K1_carries` is rewritten by unreduced representatives. The projection rank is the dimension of the span of the `s1`-blocks of the free-column kernel basis. The affine liftable-prior set is a torsor over that span because the stage-2 system is consistent (`p2 is not None`). Stored counts are Python `3 ** k` from those exponents; last digits match the `3^n` cycle (`3^{61}` ends in 3, `3^{52}` in 1, `3^{106}` in 9, `3^{97}` in 3). No duplicated `T` representation survives the injectivity argument of check 3.

The displayed z9 particular is tested separately: `A3 x2 ≡ -((D0/27 + A·T9)//9) (mod 3)` is inconsistent at all three fibres, with `stored_z9_particular_next_rank` equal to `rank(A3)=27` (matrix rank, not augmented rank). The boolean `stored_z9_particular_lifts: false` is the load-bearing record.

### 5. Literal particulars, modulo 729, AS seed

Each result stores a 72-vector `combined_z27_particular` in `{0,…,26}` together with `P_support` and `Q_support`. Support indexing is the inherited z9 order `(0,0), (0,1), (1,0), (0,2), …`. Payload reconstruction `P = P0 + 27 T_P` was checked monomial-by-monomial on the AS-seed slots and on several high-degree slots; e.g. at `0000`, `T[(0,1)]=4` and `P[(0,1)]=108`; `T[(1,0)]=0` and `P[(1,0)]=1`; at `0513`, `T[(3,0)]=1` and `P[(3,0)]=26 = -1 + 27`. Every stored coefficient other than `P[(1,0)]=1`, `P[(3,0)]≡-1 (mod 3)`, and `Q[(0,1)]=1` is `0 mod 3`. Every stored monomial has total degree ≤ 7.

The compiler rebuilds `P0+27T_P`, `Q0+27T_Q` and asserts every 91-slot coefficient of `det J-1` is divisible by 729, then stores `determinant_sha256` of `repr(sorted(determinant.items()))`. rc 0 at all six jobs (three fibres × two hosts) is the certificate that those asserts ran. The boolean flag was ignored. The constant slot was recomputed by hand from the stored supports and is divisible by 729 at all three fibres, as above.

### 6. Pair controls and Q3-kernel absorption modulo 729

| control | frozen count | identity |
|---|---:|---|
| P/Q pairs | 1296 | remainder `% 729==0` and affine after `/27` modulo 27 |
| Q3-kernel differences | 14 / 10 / 10 | output difference `% 81==0`, degree ≤ 7 |
| mixed Q3-kernel × fresh | 1008 / 720 / 720 | second difference `% 2187==0` |

Moving along a reviewed Q3-kernel direction is `F0 ↦ F0+81 K` with `K` D7-supported, i.e. a `T`-step of `3K`. The mixed second difference against an order-27 fresh basis is `81·27=2187` times a bilinear form. After `/27` the linear map `T ↦ A T` therefore changes by a multiple of 81, hence is constant modulo 27 on the Q3 fibre. The Q3-kernel quadratic is `81^2=6561=9·729 ≡ 0 (mod 729)`, so absorption cannot hide a nonlinear parameter direction at this modulus. An order-9 kernel direction would make the mixed term valuation 5 (`9·27=243`), failing `% 2187==0`. Passage of the 2187-assert, together with `% 81==0` on the output difference, is a source-level proof that every reviewed Q3-kernel direction is an order-81 D7 increment.

Order-9 *chart* digits `9C, 9D` exist in H6 V2 and are frozen in `F0`. They contribute to the linear form `L(T)` and are not variables.

### 7. Custody: two executions of one implementation

Immutable AWS jobs:

- Box02, `ip-172-30-0-186`, `/home/ubuntu/jobs/as_d7_full_output_z27_20260825T1545Z_box02`
- r6d, `ip-172-30-0-45`, `/home/ubuntu/jobs/as_d7_full_output_z27_20260825T1545Z_r6d`

`launch_remote_one.sh` runs the same `solve_full_output_cone_z27.py` under `timeout`/`ulimit`/`/usr/bin/time`, with `JC2_ROOT` the staged source tree, `MODEL_OUTPUT` the pinned SAT model, `PARENT_OUTPUT_JSON` the pinned Q3 JSON, and `PREVIOUS_Z9_RESULT_JSON` the pinned z9 result. Compiler SHA `f6eaa0a0…` is identical in both-host `SOURCE.sha256` and MANIFEST. Result SHAs differ across fibres because the SAT models differ, and agree across hosts.

| parent | rc | Box02 wall / RSS | r6d wall / RSS | result SHA-256 |
|---|---:|---|---|---|
| 0000 | 0 | 11.80 s / 22740 KiB | 14.33 s / 23492 KiB | `007b3f097cec491d480c7f240e02cedf61175d3d92ca865436ba6cf1bc2ed21d` |
| 0270 | 0 | (stdout match) | (stdout match) | `b7d571a23bb7e75b25d6540768b248b6935a35a16d903ec1c0cc71f69a079966` |
| 0513 | 0 | (stdout match) | (stdout match) | `5d109dde446f5202b2e16024873a504db75c0fef82eb3bfee9927038dbfcbc74` |

stdout `output_sha256` lines match those result SHAs. stdout files are byte-identical across hosts (same MANIFEST hashes); stderr and timestamps are not. FREEZE pins MANIFEST `80eca89d…` and producer `5bfaec75…`. `verify_frozen.py` on AWS printed `PASS-AS-Q3-FULL-OUTPUT-CONE-Z27-FROZEN` at rc 0; it checks hashes, both-host equality, ranks, counts, and refusal fields without re-running the algebra. JC2_ROOT on each host is the staged source tree, not a live checkout of unrelated maps.

`replay_all.sh` points `PARENT_OUTPUT_JSON` at the frozen z9 `q3_parent.json` path, which the two-level/Q3 prefix will overwrite. That is a packaging footgun for a local rerun and is not how the AWS jobs were launched (`old/` copies). Campaign policy is AWS-only for substantive replay; this review did not run it.

### 8. Strongest licensed theorem and next-modulus firewall

Three pinned reviewed Q3 fibres, complete fixed-D7 output digits modulo 27, determinant modulo 729, nonempty `Z/27` affine cones of F3-ranks 47 / 49 / 49. Of the prior mod-243 modules, 61 of 81 and 52 of 74 dimensions lift. Nothing else.

Modulo 2187 write `T = T9 + 9 x2` with `T9` on the liftable prior. Then
```text
729 det J(T,T) = 729 det J(T9,T9) + 6561 (mixed in x2) + 729·81 det J(x2,x2).
```
`6561 = 3·2187` and `729·81 = 9·6561`, so every term involving the fresh `x2` vanishes modulo 2187, while `729 det J(T9,T9)` survives and is quadratic in the 61- or 52-dimensional liftable prior parameter. A fresh order-729 output digit would enter linearly. The successor is therefore a source-pinned quadratic Kuranishi/Fitting or exact trit-SAT gate on that entire nonreduced stratum. No fourth global linear-Bockstein claim is licensed.

---

## Frozen AWS replay record (not re-launched)

- Hosts: Box02 `ip-172-30-0-186` and r6d `ip-172-30-0-45`
- Jobs: `/home/ubuntu/jobs/as_d7_full_output_z27_20260825T1545Z_box02` and `…_r6d`
- Start/end UTC (0000): Box02 `2026-08-25T15:44:34Z`–`15:44:46Z`; r6d `2026-08-25T15:44:57Z`–`15:45:11Z`
- Command (each parent): `python3 …/solve_full_output_cone_z27.py` under `timeout`/`ulimit` from `launch_remote_one.sh`, with `JC2_ROOT` the staged source tree, `MODEL_OUTPUT` the pinned SAT model, `PARENT_OUTPUT_JSON` the pinned Q3 JSON, `PREVIOUS_Z9_RESULT_JSON` the pinned z9 result
- Immediate compiler SHA-256: `f6eaa0a0f1dabb785bdd4358fa84739d907820bc539cc619a1b692ad5755cb19`
- Parent z9 compiler SHA-256: `2d2e0f5fa03c663201157d109a961055ebe1b3daad552b34954f20a633de32f7`

This review did not re-execute that command.
