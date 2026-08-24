# Hostile different-model review — depth-six Cartier obstruction for frozen D7 point

| Field | Value |
|---|---|
| Claim under review | Frozen producer: the named depth-five cap-seven residue class of `(A,B)` has `(det J-1)/243 ≢ 0` on the Cartier monomial `x^2 y^2`, and no next digits `U,V` of any degree can kill that row; the class is therefore terminal modulo `729` at every cap. This does **not** empty `B_(3,6)(7,7)` or any depth-six cap |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking parent-review and writeup remarks below; emptiness of `B_(3,6)`, a compatible tower, a polynomial/Tate lift, `A_infinity`, deck descent, and JC2 are correctly *not* claimed) |
| Evidence tier | reconstruction of `A,B` from the frozen cap-seven digits; exact Jacobian over `Z`; pairing formula for `[x^2 y^2]`; complete first-variation identity including the `243^2` term; Cartier cokernel of divergence in characteristic three; representative-invariance tests; unmodified rerun of both registered programs as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `c327bdc8d02472feba42573760325099f34b8cdf` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T16:07:58Z – 2026-08-24T16:16:30Z |
| Python | host CPython 3.14.6 (hashes, integer engine, pairing, registered replay); uv-pinned CPython 3.11.11 + SymPy `1.14.0` |
| Singular | 4.4.1 (registered `(integer,729)` replay; independent characteristic-0 computation of `R`, then reduction modulo 3) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, freeze, and named parents reread in full before any verdict:

- `xmodel/as-gauge-growth-p3-depth6-cartier-d7-point-20260824.md` (SHA-256 `9bff27d0aed6294633c7e5726a7d1c0d7e0fb8a5629809790da783c62b41fea4`)
- `cases/as_gauge_growth_p3_depth6_cartier_d7_point_20260824/report_n6_cartier_d7_point.md` (same SHA-256; byte-identical to the xmodel copy)
- `cases/as_gauge_growth_p3_depth6_cartier_d7_point_20260824/replay_n6_cartier_d7_point.py` (SHA-256 `050df7433e170389ed13b0045f1fae5b96950032ca19d8fa710d5f2b3157270a`)
- `cases/as_gauge_growth_p3_depth6_cartier_d7_point_20260824/audit_n6_cartier_d7_point.sing` (SHA-256 `f2795d080019a2472604ae0cf831863390b19090267ae75bebe07f63df45ac10`)
- `cases/as_gauge_growth_p3_depth6_cartier_d7_point_20260824/MANIFEST_n6_cartier_d7_point.sha256` (SHA-256 `a0c7a82a55f55dba1cd66466d70933ee61533929b8377a78952ae0a7e8bd610a`)
- `cases/as_gauge_growth_p3_depth6_cartier_d7_point_20260824/FREEZE_n6_cartier_d7_point.txt` (SHA-256 `023d71a84d2ea8b84a099d09f001790f4516dfb3278adc903c8384efd2ccba4d`)

Frozen depth-five cap-seven source of the integer representatives, and its different-model review (overall **CONFIRMED**):

- `xmodel/as-gauge-growth-p3-depth5-d7-minimum-20260824.md` (SHA-256 `618a954ea683fd8444dafc4511c9aed708ea88459c524d747b815d48c6618f65`)
- `xmodel/as-gauge-growth-p3-depth5-d7-minimum-review-grok-20260824.md` (SHA-256 `7006d82c4f6ff9943433bb4447bb95d3f94d6a76ea28ba1088bcc9aac774621f`), overall **CONFIRMED**
- `cases/as_gauge_growth_p3_depth5_d7_minimum_20260824/report_n5_d7_minimum.md` (same SHA-256 as the xmodel producer copy; byte-identical)
- `cases/as_gauge_growth_p3_depth5_d7_minimum_20260824/replay_n5_d7_minimum.py` (SHA-256 `f7a877784fee1bcf2a1cdb49873d959001ea4a08a7639127612fdefd8f13d295`)
- `cases/as_gauge_growth_p3_depth5_d7_minimum_20260824/audit_n5_d7_minimum.sing` (SHA-256 `7e0caabd513f907199489ae7c1181356e1584eede9da65a7b40e7dc96cc6beb1`)
- `cases/as_gauge_growth_p3_depth5_d7_minimum_20260824/MANIFEST_n5_d7_minimum.sha256` (SHA-256 `42d3917672e1eb24ea390cbb24b57d40d5e1a933300ed4f2d3047910ea8bfefc`)
- `cases/as_gauge_growth_p3_depth5_d7_minimum_20260824/FREEZE_n5_d7_minimum.txt` (SHA-256 `fac6c139ffdcb373d983cd74bc96a0293378d2ccffdc66d4e1c5fa0884222b83`)

Reviewed depth-four gate and completed-gauge orientation parents, consumed only at their reviewed equal-cap simplex / identity-branch scope:

- `xmodel/as-gauge-growth-p3-depth4-gate-20260824.md` (SHA-256 `bfacd9a475f8e2aa7da9d26e43785b80ff3eadd53615e4823dfe6d52fc6fd660`)
- `xmodel/as-gauge-growth-p3-depth4-review-grok-20260824.md` (SHA-256 `fecc4e758727b540cef9951ca59162f77cb2d8ff5876132e72f6175350891919`), overall **CONFIRMED**
- `xmodel/as109-bounded-polar-conductor-gate-20260824.md` (SHA-256 `2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b`)
- `xmodel/as109-bounded-polar-conductor-review-grok-20260824.md` (SHA-256 `bda4dda7d24d36bf75b6c55b566f708ee300c80aeb3344c4bb724bfc7e7787fa`), overall **CONFIRMED**
- `xmodel/as109-wild-symplectic-conductor-gate-20260824.md` (SHA-256 `c7ad3660c136bbee7105e786cc8b717d025534b67ac63cababb33c4b6de29e7c`)
- `xmodel/as109-wild-symplectic-conductor-review-grok-20260824.md` (SHA-256 `a59c7ccbf39971ad7ab47f8e865926c93e4ac9d46305be076f4bd0193b2b1a9a`), overall **CONFIRMED**

The committed basis is exactly `c327bdc8d02472feba42573760325099f34b8cdf`. Named producer artifacts remain uncommitted on top of that basis. No producer, case, canonical, notes, prompt, log, run, or erratum file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp/n6_cartier_review/` and did not import `replay_n6_cartier_d7_point.py`, `audit_n6_cartier_d7_point.sing`, or any cap-seven replay module. Support tables were not imported: `A,B` were rebuilt from the cap-seven digit formula, and `R` was the integer quotient `(det J(A,B)-1)/243`.

Tried hard, and failed, to cancel `[x^2 y^2]` by `U=x^3 y^2` or `V=x^2 y^3`, to let the quadratic `243^2 J(U,V)` contribute modulo `729`, to let the Poisson remainder `{A-x,V}+{U,B-y}` move a Cartier row before reduction modulo 3, to manufacture an extra Jacobian source from the depth-six cubing carry `3A^2\cdot 243 U`, to use the orientation identity `B=Q D(A)` or a representative change by `243` times a monomial to move the class, to realise `det J(A,B)=1` modulo `729` at any tested cap, and to promote this pointwise kill into emptiness of `B_(3,6)(7,7)`, a compatible tower, a polynomial/Tate lift, `A_infinity`, deck descent, or JC2.

---

## Promotion

**Accept `THE FROZEN DEPTH-FIVE CAP-SEVEN RESIDUE CLASS IS CARTIER-TERMINAL MODULO 729, AT EVERY CAP`.**

On the same identity-branch equal-cap simplex category as the reviewed depth-four table and the frozen cap-seven digits:

- The integer polynomials
  `A=x+9c+27e+81g`, `B=y+3b+9d+27f+81h`
  reconstructed from those digits already have coefficients in `{0,...,242}`, satisfy `A≡x`, `B≡y (mod 3)`, and satisfy `det J(A,B)=1 (mod 243)`.
- Over `Z`, every coefficient of `det J(A,B)-1` is divisible by `243`. The first residue
  `R=(det J(A,B)-1)/243 mod 3`
  is exactly the displayed degree-ten polynomial, and `[x^2 y^2]R=-1` in `F_3`. The integer coefficient is `230`, with `3`-adic valuation exactly five.
- Every lift is `A+243U`, `B+243V`. The complete expansion is
  `J(A+λU,B+λV)=J(A,B)+λ({A,V}+{U,B})+λ^2 J(U,V)`
  with `λ=243`. The quadratic term vanishes modulo `729` because `243^2=59049=81\cdot 729`. Reducing the linear term modulo 3 uses only `A≡x` and `B≡y`, and yields
  `(det J(A_new,B_new)-1)/243 ≡ R + U_x + V_y (mod 3)`.
- In characteristic three, `[x^2 y^2](U_x+V_y)=0` for every pair of polynomials (and every pair of power series): the only source monomials are `x^3 y^2` and `x^2 y^3`, each multiplied by `3`. Map equations, gauge orientation, representative changes, and the quadratic term do not enlarge that image. Hence this residue class modulo `243` has no determinant-one gauge lift modulo `729` at any polynomial cap.

**Do not promote this to:** emptiness of `B_(3,6)(7,7)` or of `B_(3,6)(D,D)` at any `D`; uniqueness of the depth-five cap-seven point; a compatible inverse-limit tower; a polynomial or Tate lift of `(x-x^3,y)`; failure of the polar theorem `κ_n→∞`; an `A_infinity` identification; deck descent; a counterexample to JC; or any JC2 inference.

**Smallest honest successor.** The producer's proposed intersection of the *full* depth-five cap-seven solution scheme with vanishing of every Cartier row of `(det J-1)/243 mod 3`, the cap-seven image of the next divergence digit, and the depth-six `P,Q` support rows, is the smallest exact search that could empty `B_(3,6)(7,7)`. If that intersection is nonempty, the same test at caps eight, nine, and ten is the next discriminator. Neither intersection is a theorem of this pointwise obstruction. Do not spend further work trying to repair *this* frozen residue.

---

## Quarantine

No result here proves or disproves JC2, constructs or excludes a polynomial lift of `(x-x^3,y)`, identifies the polar divisor with `A_infinity`, runs `p=109`, empties any depth-six bounded system, or produces a compatible tower. Producer strings `FROZEN_D7_POINT_IS_CARTIER_TERMINAL_AT_DEPTH_6_AT_EVERY_CAP` and `AUDIT_PASS` were not used as evidence; the representatives, the integer Jacobian, the pairing formula for `[x^2 y^2]`, the first-variation identity, and the Cartier cokernel were re-derived. The polar/wild parents are used only for the orientation `C_3 ∘ Φ_F=F` and the finite systems `B_(p,n)(D,D)` on total-degree simplices, at the reviewed scope that every *fixed* cap dies at some finite depth. That parent does not predict the Cartier class of this residue. Independent reconstruction, not the producer scripts, is the evidence for every numbered claim.

---

## Scope (not enlarged)

One prime `p=3`; the named identity-branch residue class modulo `243` coming from the frozen cap-seven digits; the single congruence `det J=1` modulo `729`; polynomial gauges of unrestricted degree. The kill is pointwise in that residue class. No rectangular support, no enumerator, no AWS, and no modular-to-characteristic-zero existence inference are in scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | The cap-seven digit formula reconstructs integer `A,B` with `A≡x`, `B≡y (mod 3)` and `det J(A,B)=1 (mod 243)` | **CONFIRMED** | a coefficient of `A` or `B` outside the displayed supports; a remainder of `det J-1` not divisible by `243`; special fibre not `(x,y)` |
| 2 | Over `Z`, `R_Z=(det J-1)/243` is integral; `R_Z mod 3` is the displayed polynomial; in particular `[x^2 y^2]R=-1` in `F_3` | **CONFIRMED** | a coefficient of `det J-1` not divisible by `243`; a mismatched monomial in the mod-3 reduction; `[x^2 y^2]R_Z` divisible by `3` |
| 3 | For arbitrary next digits `U,V`, `(det J(A+243U,B+243V)-1)/243 = R + U_x + V_y mod 3`, including every cross term and with `243^2 J(U,V)≡0 (mod 729)` | **CONFIRMED** | a leftover `A_y V_x` or `(A_x-1)V_y` term not divisible by `3`; `243^2 ≢ 0 (mod 729)`; a test pair with `R_new ≢ R+U_x+V_y (mod 3)` |
| 4 | `[x^2 y^2](U_x+V_y)=0` in characteristic three for polynomials of any degree. Map equations, orientation, representative changes, and nonlinear terms do not cancel (1) | **CONFIRMED** | a monomial with `∂_x` or `∂_y` coefficient not divisible by `3` on `x^2 y^2`; a cubing or `Q D'(A)` contribution to the `243`-digit of the Jacobian; a representative change moving the Cartier row |
| 5 | The Cartier class is independent of the choice of integer lifts of the depth-five coordinates by multiples of `243`, and proves that this residue class modulo `243` has no determinant-one gauge lift modulo `729` at any cap | **CONFIRMED** | a `243`-shift of a coefficient changing `[x^2 y^2]R`; a high-degree `(U,V)` with `det J=1 (mod 729)` |
| 6 | The kill is pointwise. It does not empty `B_(3,6)(7,7)` or any depth-six cap. No compatible-tower, polynomial, Tate, `A_infinity`, deck-descent, or JC2 conclusion. The proposed full-locus Cartier intersection is a successor search, not a theorem | **CONFIRMED** | a hidden uniqueness claim for the depth-five point; `B_(3,6)(7,7)=∅` asserted; the successor sold as proved empty |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Replay and hashes

Frozen hashes, recomputed on the charged tree, match the launch prompt, the manifest, and the freeze record:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as-gauge-growth-p3-depth6-cartier-d7-point-20260824.md` | `9bff27d0aed6294633c7e5726a7d1c0d7e0fb8a5629809790da783c62b41fea4` | prompt; byte-identical case copy |
| `cases/.../report_n6_cartier_d7_point.md` | `9bff27d0aed6294633c7e5726a7d1c0d7e0fb8a5629809790da783c62b41fea4` | prompt, `MANIFEST` |
| `cases/.../replay_n6_cartier_d7_point.py` | `050df7433e170389ed13b0045f1fae5b96950032ca19d8fa710d5f2b3157270a` | prompt, `MANIFEST` |
| `cases/.../audit_n6_cartier_d7_point.sing` | `f2795d080019a2472604ae0cf831863390b19090267ae75bebe07f63df45ac10` | prompt, `MANIFEST` |
| `cases/.../MANIFEST_n6_cartier_d7_point.sha256` | `a0c7a82a55f55dba1cd66466d70933ee61533929b8377a78952ae0a7e8bd610a` | prompt, freeze `manifest_sha256` |
| `cases/.../FREEZE_n6_cartier_d7_point.txt` | `023d71a84d2ea8b84a099d09f001790f4516dfb3278adc903c8384efd2ccba4d` | prompt |
| canonical replay payload | `b77499127f2f5eb9400134c7d85ba9a7befcdf7d516fc3ea127cbd5012736473` | prompt, freeze `python_payload_sha256`, live stdout |
| cap-seven report (both copies) | `618a954ea683fd8444dafc4511c9aed708ea88459c524d747b815d48c6618f65` | parent |
| cap-seven review | `7006d82c4f6ff9943433bb4447bb95d3f94d6a76ea28ba1088bcc9aac774621f` | parent, overall **CONFIRMED** |
| depth-four gate | `bfacd9a475f8e2aa7da9d26e43785b80ff3eadd53615e4823dfe6d52fc6fd660` | parent |
| depth-four review | `fecc4e758727b540cef9951ca59162f77cb2d8ff5876132e72f6175350891919` | parent |
| polar-conductor gate | `2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b` | parent |
| polar-conductor review | `bda4dda7d24d36bf75b6c55b566f708ee300c80aeb3344c4bb724bfc7e7787fa` | parent |
| wild-symplectic gate | `c7ad3660c136bbee7105e786cc8b717d025534b67ac63cababb33c4b6de29e7c` | parent |
| wild-symplectic review | `a59c7ccbf39971ad7ab47f8e865926c93e4ac9d46305be076f4bd0193b2b1a9a` | parent |

Every member hash inside `MANIFEST_n6_cartier_d7_point.sha256` was recomputed from the case directory and matched. The freeze record is not a second copy of the manifest; it names the manifest digest and the canonical payload digest.

Registered commands, rerun unmodified from the case directory:

```text
python3 replay_n6_cartier_d7_point.py
Singular -q audit_n6_cartier_d7_point.sing
shasum -a 256 -c MANIFEST_n6_cartier_d7_point.sha256
```

Both engines exited 0 and the manifest check passed. Live payload SHA-256 `b77499127f2f5eb9400134c7d85ba9a7befcdf7d516fc3ea127cbd5012736473`. Singular printed `AUDIT_PASS frozen D7 point has Cartier-terminal depth-six row` and the identity `det J-1=243 R` in `(Z/729Z)[x,y]`. Those Booleans were discarded as evidence for Claims 1–6. (The registered Singular script *pastes* `R` and checks the identity in a ring where `243` is a zero-divisor; that is why it is regression-only. The independent characteristic-0 computation below *divides* `det J-1` by `243` over `Q`.)

Independent engines, written for this review and not imported from either registered program (scratch SHA-256, outside the repository):

- integer sparse engine, host CPython 3.14.6: `8d571bdf0fb74c885a40b7bbec9eb57120cfdd23aa3bbc76b5b4671311c115e3`
- Jacobian pairing formula on the displayed supports: `999c2515ceb7b0edd5c8bcd03ca4544ce28b1f5ac566b0c058a86dda860f1195`
- SymPy `1.14.0` over `ZZ[x,y]`: `1db8af37bd75920106285bb6407d86a99b1ee0da54e6ccf90997df02d8bfb855`
- second Singular script, characteristic 0 then reduction modulo 3: `dce7918423ae5d2ee0a44f232f73876844997de276bc24cf06590cd1f755baef`

The three non-pasting engines produced the same integral `R_Z`, the same mod-3 polynomial, and the same Cartier coefficient `230 ≡ -1 (mod 3)`.

---

## Independent recomputation

### 1. Frozen representatives and `det J ≡ 1 (mod 243)` — CONFIRMED

Digits are taken from the cap-seven report, not from the Cartier replay:

```text
b = x^5,
c = 2 x^2 y,
d = x y^2 + x^5 + 2 x^7,
e = 2x + x y + 2 x^2 + x^4 y + 2 x^5,
f = y + y^2 + 2 x y + y^3 + 2 x y^2 + x y^3 + x^3 y^2 + 2 x^4 y + x^6 y + x^7,
g = x + x^2 + 2 x y^2 + 2 x^2 y + 2 x y^3 + x^2 y^2 + 2 x^2 y^3
      + x^4 y + x^5 + 2 x^2 y^4 + 2 x^7,
h = y + y^2 + 2 x y + y^4 + 2 x y^4 + x y^5 + 2 x^5 y + 2 x^6 y,
A = x + 9c + 27e + 81g,
B = y + 3b + 9d + 27f + 81h.
```

Expanding over `Z` already yields coefficients in `{0,...,242}`: there is no hidden multiple of `243` in the digit formula. The reduced supports are exactly those displayed in the cap-seven package,

```text
A = 162 x^7 + 162 x^2 y^4 + 135 x^5 + 108 x^4 y + 162 x^2 y^3
      + 81 x^2 y^2 + 162 x y^3 + 180 x^2 y + 162 x y^2 + 135 x^2
      + 27 x y + 136 x,
B = 45 x^7 + 189 x^6 y + 162 x^5 y + 81 x y^5 + 12 x^5 + 54 x^4 y
      + 27 x^3 y^2 + 162 x y^4 + 27 x y^3 + 81 y^4 + 63 x y^2
      + 27 y^3 + 216 x y + 108 y^2 + 109 y.
```

Every coefficient of `A-x` and of `B-y` is divisible by `3`, so `A≡x` and `B≡y (mod 3)`. Direct differentiation gives `A_x ≡ 1`, `A_y ≡ 0`, `B_x ≡ 0`, `B_y ≡ 1 (mod 3)`. The integer Jacobian `J=A_x B_y - A_y B_x` satisfies: every coefficient of `J-1` is divisible by `243`, and the constant term is `14824=1+243\cdot 61`. Hence `det J(A,B)=1 (mod 243)` and `det J(A,B) ≢ 1 (mod 729)`.

Parent orientation, rechecked on these same representatives and not used as Cartier evidence: `(1-3A^2)S_5(A)=1 (mod 243)`, `Q D(A)=B (mod 243)` for `P=A-A^3` and `Q=B S_5(A)`, and `det J(P,Q)=1 (mod 243)`. At depth six, `S_6=S_5+243 A^{10}` still satisfies `D(A)S_6(A)=1 (mod 729)`, and `det J(P, B S_6(A))=det J(A,B) (mod 729)`. The gauge determinant *is* the oriented map determinant.

### 2. The first unfulfilled digit, including `[x^2 y^2]R=-1` — CONFIRMED

Define `R_Z=(J-1)/243` over `Z` (exact integer division of every coefficient) and `R=R_Z mod 3`. Three engines give the same integral polynomial, whose reduction is

```text
R = x^{10} + x^8 + x^7 y + x^7 - x^6 y^3 - x^6 y + x^5 y - x^3 y
      + x^2 y^3 - x^2 y^2 + x y^3 + x y^2 + x y - x - y^3 + y^2 + y + 1
```

in `F_3[x,y]`. Termwise equality with the displayed producer polynomial holds; there are no extra mod-3 monomials. (Over `Z` there *are* extra terms, such as `882 x^{12}`, all of whose coefficients are divisible by `3`. The producer correctly reports only the first residue.)

The Cartier coefficient is visible without a support table. The only pairs of monomials that can produce `x^2 y^2` in `J` are those with `a+c=3` and `b+d=3` in

```text
[x^m y^n] J = sum_{a+c=m+1, b+d=n+1} (a d - b c) A_{a,b} B_{c,d}.
```

The contributing pairs on the displayed supports are

```text
A_{[x^2 y]}  =180,  B_{[x y^2]}= 63,  ad-bc=3,  contribution  34020
A_{[x^2]}    =135,  B_{[x y^3]}= 27,  ad-bc=6,  contribution  21870
A_{[x^2 y^2]}= 81,  B_{[x y]}  =216,  ad-bc=0,  contribution      0
```

so `[x^2 y^2]J=55890=243\cdot 230`. Thus `[x^2 y^2]R_Z=230` and `230 ≡ 2 ≡ -1 (mod 3)`. The factor `230=2\cdot 5\cdot 23` is not divisible by `3`, so the `3`-adic valuation is exactly five: the obstruction is a genuine depth-six digit, not an accident of a higher power of `3`. Among monomials `x^i y^j` with `i≡j≡2 (mod 3)`, the only nonzero row of `R` is `(i,j)=(2,2)`.

### 3. First variation is exactly `R+U_x+V_y` modulo 3 — CONFIRMED

Write `λ=243` and expand as a polynomial identity over `Z`:

```text
J(A+λU, B+λV)
  = (A_x + λ U_x)(B_y + λ V_y) - (A_y + λ U_y)(B_x + λ V_x)
  = J(A,B) + λ ({A,V}+{U,B}) + λ^2 J(U,V),
```

where `{P,Q}=P_x Q_y - P_y Q_x`. Now `λ^2=59049=81\cdot 729 ≡ 0 (mod 729)`, so the quadratic term is absent from the depth-six digit. Dividing by `243` over `Z` therefore gives

```text
(J_new - 1)/243 = R_Z + {A,V} + {U,B} + 243 J(U,V).
```

It remains to reduce the Poisson bracket modulo 3. Because `A=x+3α` and `B=y+3β` as integer polynomials,

```text
{A,V}+{U,B}
  = (1+3α_x) V_y - (3α_y) V_x + U_x (1+3β_y) - U_y (3β_x)
  = U_x + V_y + 3(α_x V_y - α_y V_x + β_y U_x - β_x U_y).
```

The extra sum is divisible by `3`, hence vanishes in `F_3[x,y]`. Equivalently `A_x≡1`, `A_y≡0`, `B_x≡0`, `B_y≡1 (mod 3)`, which was checked by reducing the differentiated supports. Therefore

```text
(det J(A+243U, B+243V)-1)/243 ≡ R + U_x + V_y  (mod 3),
```

as polynomials, for arbitrary `U,V`. This was rechecked on mixed-degree test pairs, including the Cartier source monomials `U=x^3 y^2`, `V=x^2 y^3`, high degrees `(10,10)` and `(6,5)`, and a generic sparse pair; the integer identity, the mod-3 prediction, and invariance of `[x^2 y^2]` all held. SymPy verified the bilinear-plus-quadratic identity as an element of `ZZ[x,y]`. Independent Singular verified it over `Q` and the reduction `R_new ≡ R + U_x + V_y (mod 3)`.

No cross term was omitted. In particular the mixed brackets `A_x V_y`, `U_x B_y`, `-A_y V_x`, `-U_y B_x` are all present, and the only reason they collapse to `U_x+V_y` is the special fibre `(x,y)`.

### 4. Cartier cokernel; no hidden cancellation — CONFIRMED

Let `k` be any field of characteristic three (in particular `F_3`), and let `U,V ∈ k[x,y]` or even `k[[x,y]]`. Write `U=∑ u_{ij} x^i y^j`. Then

```text
U_x = ∑ i u_{ij} x^{i-1} y^j.
```

The coefficient of `x^2 y^2` in `U_x` comes only from `(i,j)=(3,2)`, and equals `3 u_{32}=0`. The coefficient of `x^2 y^2` in `V_y` comes only from `(i,j)=(2,3)`, and equals `3 v_{23}=0`. There is no other source monomial. The same holds for every Cartier monomial `x^{3k-1} y^{3m-1}` with `k,m≥1`. Thus `x^2 y^2` lies in the cokernel of the divergence `(U,V) ↦ U_x+V_y` in characteristic three, independently of degree.

This was also exhausted on the monomial basis of total degree `≤12`: every basis vector of `U` and of `V` has `[x^2 y^2](U_x+V_y)=0` in `F_3`. Over `Z` one has `∂_x(x^3 y^2)=3 x^2 y^2` and `∂_y(x^2 y^3)=3 x^2 y^2`, both `0` modulo 3.

Four cancellation routes the producer could have missed:

- *Nonlinear `λ^2` term.* `243^2 J(U,V)≡0 (mod 729)` identically. Checked on a mixed pair with `J(U,V)≠0`.
- *Representative change.* Replacing `(A,B)` by `(A+243U, B+243V)` is the substitution of Claim 3. The Cartier coefficient is invariant on every monomial shift of total degree `<8`, and on the high-degree tests of Claim 3.
- *Map equations.* At this Witt step the cubing carry dies: `(A+243U)-(A+243U)^3 ≡ (A-A^3)+243 U (mod 729)`, because `3 A^2 \cdot 243 U` is a multiple of `729`. The next `P`-digit is exactly `U`. That constrains `(U,V)` if one also imposes a cap on `(P,Q)`; it cannot *enlarge* the image of divergence. The orientation identity `B=Q D(A)` likewise identifies `det J(A,B)` with `det J(P,Q)` (the extra term `Q D'(A)\,dA` wedges to zero with `dA`) and does not add a Jacobian source outside `{A,V}+{U,B}`.
- *A different special fibre.* Out of scope: the frozen point is on the identity branch, and `A≡x`, `B≡y (mod 3)` were rechecked.

Equation (1) is therefore unreachable. The frozen residue has no symplectic gauge lift modulo `729`, of any polynomial degree.

### 5. Representative invariance and promotion scope — CONFIRMED

The depth-five coordinates are elements of `(Z/243Z)[x,y]`. Any two integer lifts differ by `243` times a polynomial, which is the substitution of (2). The class of `R` modulo `im ∂_x + im ∂_y`, and specifically the linear functional `[x^2 y^2]`, is therefore a residue-class invariant, not a serialization accident. In the present digit formula the integer representatives *already* lie in `{0,...,242}`, so even that serialization choice does not arise.

What is proved is exactly: this residue class modulo `243` admits no pair `(A',B')` with `A'≡A`, `B'≡B (mod 243)` and `det J(A',B')=1 (mod 729)`, in the polynomial category of any cap, and equally in the Tate algebra (the same cokernel computation applies coefficientwise to restricted series). Combined with the orientation identity at depth six, it also admits no oriented map lift of this gauge class.

What is *not* proved is uniqueness of the depth-five point inside `B_(3,5)(7,7)`, nor terminality of any other residue class. The producer headline's phrase "minimum-cap point" is parent language for the source of the digits; the obstruction does not use minimality.

### 6. Stronger readings, and the successor as a search — CONFIRMED

A different point of `B_(3,5)(7,7)` — or a point of `B_(3,5)(D,D)` at a larger cap — may have vanishing Cartier class. The identity gauge `(x,y)` is the positive control: `det J(x,y)=1` exactly, so `R=0`. The earlier cap-eight survivor is a different residue. Nothing here empties `B_(3,6)(7,7)` or `B_(3,6)(D,D)` at any `D`.

No compatible tower across depths, no polynomial or Tate lift of `(x-x^3,y)`, no failure of the polar theorem `κ_n→∞`, no `A_infinity` identification, no deck descent, and no JC2 inference is licensed. The finite system at depth six remains open.

The proposed next discriminator — intersect the full depth-five cap-seven *scheme* with (i) vanishing of every Cartier row of `(det J-1)/243 mod 3`, (ii) the cap-seven image of the next divergence digit, and (iii) the depth-six `P,Q` support rows, repeating at caps eight, nine, and ten if needed — is the correct search if the goal is emptiness of a bounded depth-six system. It is not a theorem of this review, and this frozen residue should not be repaired.

---

## Non-blocking remarks

- The depth-five cap-seven existence package is now independently **CONFIRMED** (`xmodel/as-gauge-growth-p3-depth5-d7-minimum-review-grok-20260824.md`). This review still rebuilt those digits and rechecked `det J(A,B)=det J(P,Q)=1 (mod 243)` before attacking the depth-six Cartier claim. That parent also records a *different* depth-six failure of these same representatives, `[x^4 y^4](A-A^3)≡243 (mod 729)`, which inflates `deg P` before any next digit is added. That map-degree row is in principle movable by `U`, because the next `P`-digit is `U`; the Cartier row of `det J` is not. Emptiness of `B_(3,5)(D,D)` for `D≤6` is taken from the already-reviewed depth-four gate and is not used in Claims 1–6.
- The registered Singular replay pastes `R` into `(integer,729)`, a ring in which `243R` determines `R` only modulo `3`. With coefficients in `{-1,0,1}` that still pins the displayed polynomial, but it is not an independent computation of `R`. The characteristic-0 division in the scratch Singular script is.
- Producer section 2 is terse: it quotes (2) from `A≡x`, `B≡y` without writing the `λ^2` term or the Poisson remainder. Both vanish for the reasons in Claim 3; the displayed identity is correct.
- Singular's `(integer,729)` printer writes `-1` as `728`. The live stdout polynomial is the same class as the displayed `R`.
- The identity-gauge cap-nine pin in the Python replay is a degree comparison for the cotangent truncation, not a Cartier computation. It was not used.

---

## Quarantine (close)

Accept only the pointwise statement: the frozen cap-seven residue class modulo `243` is Cartier-terminal modulo `729` at every cap. Do not quote this file as emptiness of `B_(3,6)`, as a no-lift theorem, as an `A_infinity` or deck-descent statement, or as a JC2 result. Independent reconstruction of `A,B`, of `R_Z`, of the pairing coefficient `230`, of the first-variation identity, and of the characteristic-three cokernel is the evidence; producer `PASS` strings are not.
