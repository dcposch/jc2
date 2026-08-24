# Hostile different-model review — AS `p=3`, depth-five exact cap-seven minimum

| Field | Value |
|---|---|
| Claim under review | Frozen producer: the identity-branch equal-cap system `B_(3,5)(7,7)` on total-degree simplices is nonempty; reduction modulo `81` of any depth-five equal-cap `D<=6` point would be a depth-four equal-cap `D<=6` point; the reviewed depth-four table excludes that set; therefore the exact minimum is `D_min(3,5)=7`; this falsifies the proposed law `(n-1)(p-1)+1` at `(p,n)=(3,5)` rather than leaving it unproved |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none (for the six numbered claims). The same integer representatives fail already at depth six: `[x^4 y^4](A-A^3) ≡ 243 ≢ 0 (mod 729)`, so `deg P = 9` modulo `729`; that is a quarantine identity, not a failure of the depth-five minimum |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking digit-count / carry-narrative remarks below; depth six, liftability of this residue class, an inverse-limit/polynomial/Tate lift, `A_infinity`, deck descent, and JC2 are correctly *not* claimed) |
| Evidence tier | independent reconstruction of `B_(3,5)(7,7)` from the confirmed polar/wild orientation; exact integer expansions of `P=A-A^3` and `Q=B S_5(A)` by a sparse engine (unreduced `Z`-coefficients and reduce-after-every-op), a dense coefficient box, a SymPy `ZZ[x,y]` engine, and a second Singular script, none of which import the producer; free-variable truncated inverse; direct Jacobians of the reduced coordinates; an independent reduction lemma modulo `81`; unmodified rerun of the two registered programs as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `c327bdc8d02472feba42573760325099f34b8cdf` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T16:06:41Z – 2026-08-24T16:12:16Z |
| Python | host CPython 3.14.6 (hashes, sparse/dense engines, registered replay); uv-pinned SymPy `1.14.0` for the second independent engine |
| Singular | 4.4.1 (`(integer,243)`, `(integer,81)`, `(integer,3)` imap, and a separate `(integer,729)` digit rebuild) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, freeze, and named parents reread in full before any verdict:

- `xmodel/as-gauge-growth-p3-depth5-d7-minimum-20260824.md` (SHA-256 `618a954ea683fd8444dafc4511c9aed708ea88459c524d747b815d48c6618f65`)
- `cases/as_gauge_growth_p3_depth5_d7_minimum_20260824/report_n5_d7_minimum.md` (same SHA-256; byte-identical to the xmodel copy)
- `cases/as_gauge_growth_p3_depth5_d7_minimum_20260824/replay_n5_d7_minimum.py` (SHA-256 `f7a877784fee1bcf2a1cdb49873d959001ea4a08a7639127612fdefd8f13d295`)
- `cases/as_gauge_growth_p3_depth5_d7_minimum_20260824/audit_n5_d7_minimum.sing` (SHA-256 `7e0caabd513f907199489ae7c1181356e1584eede9da65a7b40e7dc96cc6beb1`)
- `cases/as_gauge_growth_p3_depth5_d7_minimum_20260824/MANIFEST_n5_d7_minimum.sha256` (SHA-256 `42d3917672e1eb24ea390cbb24b57d40d5e1a933300ed4f2d3047910ea8bfefc`)
- `cases/as_gauge_growth_p3_depth5_d7_minimum_20260824/FREEZE_n5_d7_minimum.txt` (SHA-256 `fac6c139ffdcb373d983cd74bc96a0293378d2ccffdc66d4e1c5fa0884222b83`)

Depth-four table, consumed only at its reviewed equal-cap simplex scope:

- `xmodel/as-gauge-growth-p3-depth4-gate-20260824.md` (SHA-256 `bfacd9a475f8e2aa7da9d26e43785b80ff3eadd53615e4823dfe6d52fc6fd660`)
- `xmodel/as-gauge-growth-p3-depth4-review-grok-20260824.md` (SHA-256 `fecc4e758727b540cef9951ca59162f77cb2d8ff5876132e72f6175350891919`), overall **CONFIRMED**

Bounded-polar and completed-gauge parents, consumed only for the finite system `B_(p,n)(D_F,D_phi)` and the orientation `C_p ∘ Φ_F = F`:

- `xmodel/as109-bounded-polar-conductor-gate-20260824.md` (SHA-256 `2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b`)
- `xmodel/as109-bounded-polar-conductor-review-grok-20260824.md` (SHA-256 `bda4dda7d24d36bf75b6c55b566f708ee300c80aeb3344c4bb724bfc7e7787fa`), overall **CONFIRMED**
- `xmodel/as109-wild-symplectic-conductor-gate-20260824.md` (SHA-256 `c7ad3660c136bbee7105e786cc8b717d025534b67ac63cababb33c4b6de29e7c`)
- `xmodel/as109-wild-symplectic-conductor-review-grok-20260824.md` (SHA-256 `a59c7ccbf39971ad7ab47f8e865926c93e4ac9d46305be076f4bd0193b2b1a9a`), overall **CONFIRMED**

The committed basis is exactly `c327bdc8d02472feba42573760325099f34b8cdf`. Named producer artifacts remain uncommitted on top of that basis. No producer, case, canonical, notes, prompt, log, run, or erratum file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp/as-d5-d7-review` and did not import `replay_n5_d7_minimum.py` or `audit_n5_d7_minimum.sing`. No newer unreviewed depth-six Cartier calculation was read or used.

Tried hard, and failed, to reverse the composition to `Φ ∘ C_3` or `F ∘ Φ`, to read the system on an exponent rectangle, to drop the gauge cap or the map cap, to keep a monomial of total degree `>7` after coefficientwise reduction modulo `243`, to make `det J(P,Q)` fail while `det J(A,B)=1`, to realise the identity gauge at cap seven (it has map degree nine), to drop this displayed point to cap six, to break the reduction map `B_(3,5)(D,D) → B_(3,4)(D,D)` by the extra `81 A^8` summand of `S_5`, to treat the cited depth-four emptiness as a different category, to make these same integer representatives work modulo `729` at cap seven, and to promote the minimum to a polar-theorem failure, a polynomial lift, `A_infinity`, deck descent, or JC2.

---

## Promotion

**Accept `THE EXACT EQUAL-CAP MINIMUM AT (p,n)=(3,5) IS SEVEN`.**

On the same identity-branch equal-cap simplex category as the reviewed depth-four table:

- The finite system is polar `(5.3)` at `p=3`, `n=5`, `D_F=D_phi=7`: polynomial gauge `(A,B)` over `Z/243Z` with `A ≡ x`, `B ≡ y (mod 3)`, `det J(A,B)=1`, and `deg(A-A^3), deg(B S_5(A)) <= 7`, with `S_5=1+3A^2+9A^4+27A^6+81A^8`. The orientation is `C_3 ∘ (A,B) = (P,Q)`, not the reverse. Supports are total-degree simplices, not exponent rectangles. Both the map cap and the canonical gauge cap are load-bearing.
- The displayed digits `a=0`, `b=x^5`, and the six further polynomials `c,d,e,f,g,h` assemble to a point of exact total degrees `(7,7,7,7)` with special fibre `(x-x^3,y) (mod 3)` and with no reduced monomial of total degree `>7`.
- Independently, `(1-3A^2)S_5(A)=1 (mod 243)` as a polynomial identity, `B=Q(1-3A^2)`, and `det J(A,B)=det J(P,Q)=1 (mod 243)`, the last also by direct differentiation of the reduced coordinates.
- Therefore the point lies in `B_(3,5)(7,7)`, so that set is nonempty.
- Reduction of coefficients modulo `81` sends every point of `B_(3,5)(D,D)` to a point of `B_(3,4)(D,D)` without increasing either cap. The reviewed depth-four gate proves `B_(3,4)(D,D)` empty for `D<=6`. Hence `B_(3,5)(D,D)` is empty for `D<=6`, and the exact minimum is seven.
- The reviewed minima at depths two through four are `3,5,7`. The proposed value `(n-1)(p-1)+1` would have been nine at depth five. A point of cap seven falsifies that law, rather than leaving it a surviving coincidence.

**Do not promote this to:** survival at depth six or at any later depth; compatibility of this residue class across depths; a polynomial, Tate-algebra, or inverse-limit lift; failure of the polar theorem `κ_n → ∞`; an `A_infinity` identification; deck descent; a counterexample to JC; or any JC2 inference.

**Smallest honest successor.** An exact depth-six equal-cap discriminator for `B_(3,6)(D,D)` at a stated cap — emptiness or a point, starting at seven — is the smallest computational successor. It is not licensed by this finite minimum. In particular, these same integer representatives are not a depth-six cap-seven point.

---

## Quarantine

No result here proves or disproves JC2, constructs or excludes a polynomial lift of `(x-x^3,y)`, identifies the polar divisor with `A_infinity`, runs `p=109`, or produces a compatible tower. Producer strings `EXACT_BOUNDED_SURVIVOR_D7_AND_REVIEWED_DEPTH4_LOWER_BOUND_PIN_MINIMUM_7` and `AUDIT_PASS` were not used as evidence; the system, the reduced supports, both Jacobians, the truncated inverse, the cap cancellations, and the reduction lemma were re-derived. The polar parent is used only for `B_(p,n)(D_F,D_phi)` on total-degree simplices and for the orientation `C_p ∘ Φ_F=F`, at the reviewed scope that every *fixed* cap dies at some finite depth. A depth-five minimum of seven does not contradict that theorem and does not supply a rate. The depth-four parent is used only for emptiness of `B_(3,4)(D,D)` at `D<=6` and for the three exact minima `3,5,7`. Independent reconstruction, not the producer scripts, is the evidence for every numbered claim. No unreviewed depth-six calculation enters the minimum verdict.

---

## Scope (not enlarged)

One prime `p=3`; one Witt depth `n=5`; equal total-degree simplex caps; exact coefficient ring `Z/243Z`; identity branch. The displayed survivor is a finite bounded witness, not a lift to all depths. No rectangular support, no enumerator, no AWS, and no modular-to-characteristic-zero existence inference are in scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Frozen identity-branch system at `p=3,n=5` is `P=A-A^3`, `Q=B S_5(A)`, `S_5=1+3A^2+9A^4+27A^6+81A^8` modulo `243`, with `det J(A,B)=1` and simultaneous total-degree simplex caps on both gauge and map. Same orientation and category as the reviewed depth-four table | **CONFIRMED** | reverse composition; rectangle support; map cap without gauge cap, or the reverse; `S_5` truncated at `A^6`; a different special fibre; digits used as independent search variables rather than as the unique identity-branch gauge |
| 2 | The eight base-three digits (`a=0` and the seven displayed polynomials `b,c,d,e,f,g,h`) assemble to integer `A,B` whose reduced `P,Q` match the displayed supports, all four exact total degrees are seven, and the special fibre is `(x-x^3,y) (mod 3)` | **CONFIRMED** | a reduced degree-eight term; a digit outside the simplex of radius seven; `P ≢ x-x^3 (mod 3)`; support tables imported rather than recomputed; `a` secretly nonzero |
| 3 | `(1-3A^2)S_5(A)=1 (mod 243)`, `B=Q(1-3A^2)`, `det J(A,B)=det J(P,Q)=1 (mod 243)` by chain rule *and* by direct differentiation of the reduced coordinates; every unreduced monomial of `P` or `Q` of total degree `>7` has coefficient divisible by `243` | **CONFIRMED** | truncated inverse remainder not divisible by `243` in a free variable; `det J(P,Q)` only inferred; a surviving over-cap coefficient modulo `243` |
| 4 | The point lies in `B_(3,5)(7,7)`. Reduction modulo `81` sends `B_(3,5)(D,D)` into `B_(3,4)(D,D)` without increasing caps. The cited depth-four result excludes `D<=6` in exactly that system. Therefore `D_min(3,5)=7` | **CONFIRMED** | `S_5` reduction failing to match `S_4`; a hidden extra constraint at depth five not present at depth four; the depth-four emptiness holding in a different category; this point having a reduced degree-eight monomial |
| 5 | Reviewed minima at depths two through four are `3,5,7`. This point gives depth-five minimum seven, against the proposed value `(5-1)(3-1)+1=9`. The law is falsified, not merely unproved | **CONFIRMED** | the law only claimed as a depth-four coincidence and not tested; minimum asserted to remain seven at later depths; `D_min=8` left open as if this point failed |
| 6 | No inference to depth six, liftability of this residue class, an inverse-limit/polynomial/Tate lift, `A_infinity`, deck descent, or JC2. The producer licenses none of them | **CONFIRMED** | a hidden `n=6` claim; `κ_n → ∞` declared false; this point sold as a lift; a JC2 sentence; an unreviewed depth-six Cartier calculation imported into the minimum |

All remarks below are non-blocking unless marked otherwise. None changes a reduced monomial, a Jacobian, a reduction map, or a numbered verdict.

---

## Replay and hashes

Frozen hashes, recomputed on the charged tree, match the launch prompt, the manifest, and the freeze record:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as-gauge-growth-p3-depth5-d7-minimum-20260824.md` | `618a954ea683fd8444dafc4511c9aed708ea88459c524d747b815d48c6618f65` | prompt; byte-identical case copy |
| `cases/.../report_n5_d7_minimum.md` | `618a954ea683fd8444dafc4511c9aed708ea88459c524d747b815d48c6618f65` | prompt, `MANIFEST` |
| `cases/.../replay_n5_d7_minimum.py` | `f7a877784fee1bcf2a1cdb49873d959001ea4a08a7639127612fdefd8f13d295` | prompt, `MANIFEST` |
| `cases/.../audit_n5_d7_minimum.sing` | `7e0caabd513f907199489ae7c1181356e1584eede9da65a7b40e7dc96cc6beb1` | prompt, `MANIFEST` |
| `cases/.../MANIFEST_n5_d7_minimum.sha256` | `42d3917672e1eb24ea390cbb24b57d40d5e1a933300ed4f2d3047910ea8bfefc` | prompt, freeze `manifest_sha256` |
| `cases/.../FREEZE_n5_d7_minimum.txt` | `fac6c139ffdcb373d983cd74bc96a0293378d2ccffdc66d4e1c5fa0884222b83` | prompt |
| canonical replay payload | `6e161a0cde8387b5853dc6756ef13e44c60785f166bcdd8658a086023090924b` | prompt, freeze `python_payload_sha256`, live stdout |
| depth-four gate | `bfacd9a475f8e2aa7da9d26e43785b80ff3eadd53615e4823dfe6d52fc6fd660` | parent |
| depth-four review | `fecc4e758727b540cef9951ca59162f77cb2d8ff5876132e72f6175350891919` | parent |
| polar-conductor gate | `2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b` | parent |
| polar-conductor review | `bda4dda7d24d36bf75b6c55b566f708ee300c80aeb3344c4bb724bfc7e7787fa` | parent |
| wild-symplectic gate | `c7ad3660c136bbee7105e786cc8b717d025534b67ac63cababb33c4b6de29e7c` | parent |
| wild-symplectic review | `a59c7ccbf39971ad7ab47f8e865926c93e4ac9d46305be076f4bd0193b2b1a9a` | parent |

Every member hash inside `MANIFEST_n5_d7_minimum.sha256` was recomputed from the case directory and matched. The freeze record is not a second copy of the manifest; it names the manifest digest and the canonical payload digest.

Registered commands, rerun unmodified from the case directory:

```text
python3 replay_n5_d7_minimum.py
Singular -q audit_n5_d7_minimum.sing
shasum -a 256 -c MANIFEST_n5_d7_minimum.sha256
```

Both engines exited 0. Live payload SHA-256 `6e161a0cde8387b5853dc6756ef13e44c60785f166bcdd8658a086023090924b`, recomputed from the canonical JSON with `payload_sha256` stripped. Singular printed `AUDIT_PASS p=3 n=5 D=7 modulus=243` with degrees `7,7,7,7` and the same reduced `P,Q` as the report. Those Booleans were discarded as evidence for Claims 1–6.

Independent engines, written for this review and not imported from either registered program (scratch SHA-256, outside the repository):

- sparse `Z[x,y]` engine, two reduction schedules, plus a dense `72×72` coefficient box, host CPython 3.14.6: `cf21b3fbb7385436d2ab8645cc0c6c2579fc3cb44625698a0ad0ac365e4163b0`
- SymPy `1.14.0` over `ZZ[x,y]`: `bfdc7b214f24b5c67761265c985dc8986ef8aaad636e352f5085608f7bcad316`
- second Singular script over `Z/243Z`, characteristic-3 imap, and `Z/81Z`: `4f1a434f66e6586d92060fd6ae2782e61d8e08a619fbfcf2201fa52db4ec1954`
- separate Singular rebuild of the same digits in `Z/729Z` (naive depth-six probe only): `3c6067f6197c8fa0c014da1a3a9eec929ba611fb2892cc7432e524d88437ca13`

The dense box truncates unreduced monomials of `x`- or `y`-degree `>=72`. Every such monomial has total degree `>=72` and, by the untruncated sparse and SymPy expansions, coefficient divisible by `243`. Reduced cap-seven supports were cross-checked against both non-truncating engines and against the live producer payload, monomial by monomial.

---

## Independent recomputation

### 1. System, orientation, carry, and cap grammar — CONFIRMED

Write `g(T)=T-T^3`, `D(T)=1-3T^2`, `C_3=(g, y/D)`. The confirmed wild/polar orientation is `C_3 ∘ Φ_F = F` with `Φ_F=(A,B)` on the identity branch. Coordinate comparison is tautological:

```text
A - A^3 = P,             B / D(A) = Q,
```

hence `B = Q(1-3A^2)`. Reverse composition `Φ ∘ C_3` and left-versus-right swap `F ∘ Φ = C_3` are not this statement. Independently substituting `x ↦ x-x^3`, `y ↦ y` into the reduced `(A,B)` does not recover `(P,Q)`.

At finite depth five, `S_5(T)=∑_{j<5} 3^j T^{2j}` satisfies the polynomial identity

```text
(1-3T^2) S_5(T) = 1 - 243 T^{10}
```

in `Z[T]`. Independently expanded in a free variable, the remainder is exactly `-243 T^{10}`; it vanishes in `(Z/243Z)[T]`. Thus `Q := B S_5(A)` is the correct finite-depth second coordinate, and `C_(3,5) ∘ (A,B) = (A-A^3, B S_5(A))` in `(Z/243Z)[x,y]`. Polar `(5.3)` at equal caps is exactly

```text
A ≡ x, B ≡ y (mod 3),
det J(A,B) = 1 in Z/243Z,
deg(A), deg(B) <= 7,                 (gauge cap)
deg(A-A^3), deg(B S_5(A)) <= 7.      (map cap)
```

Supports are total-degree simplices: a monomial `x^i y^j` is admitted iff `i+j <= D`. This is the same grammar as the reviewed depth-four table, not an exponent rectangle. Dropping either cap would define a different system. The identity-gauge control `A=x`, `B=y` realises map degree nine, because `81 x^8 y ≢ 0 (mod 243)`, and is the pinned positive control of the larger system `B_(3,5)(9,9)`; it is not a point of `B_(3,5)(7,7)`.

Carry. The unique identity-branch gauge modulo `243` has the shape

```text
A = x + 3a + 9c + 27e + 81g,
B = y + 3b + 9d + 27f + 81h,
```

with every digit on the simplex of radius seven. The displayed point has `a=0`, equivalently `A ≡ x (mod 9)`, which is checked after assembly and is not an omitted `3a` term. Nonlinear products in `A^3` and in `B S_5(A)` generate many monomials of total degree `>7`; those are the cap-cancellations of Claim 3, not a licence to work on a rectangle.

### 2. Digit transcription, assembly, degrees, special fibre — CONFIRMED

Digits transcribed from the frozen report display, not from producer dictionaries:

```text
b = x^5,
c = 2 x^2 y,
d = x y^2 + x^5 + 2 x^7,
e = 2x + x y + 2 x^2 + x^4 y + 2 x^5,
f = y + y^2 + 2 x y + y^3 + 2 x y^2 + x y^3 + x^3 y^2 + 2 x^4 y + x^6 y + x^7,
g = x + x^2 + 2 x y^2 + 2 x^2 y + 2 x y^3 + x^2 y^2 + 2 x^2 y^3
    + x^4 y + x^5 + 2 x^2 y^4 + 2 x^7,
h = y + y^2 + 2 x y + y^4 + 2 x y^4 + x y^5 + 2 x^5 y + 2 x^6 y.
```

Each coefficient lies in `{1,2}`. Each support lies on the simplex of radius seven (`deg b=5`, `deg c=3`, `deg d=deg f=deg g=deg h=7`, `deg e=5`). There is no displayed eighth nonzero digit: the eighth slot is `a=0`.

Integer assembly, before any producer table:

```text
A = x + 9c + 27e + 81g,
B = y + 3b + 9d + 27f + 81h.
```

Collecting overlapping monomials over `Z` and reducing modulo `243` gives, independently of the report's displayed supports and then compared to them,

```text
A = 162 x^7 + 162 x^2 y^4 + 135 x^5 + 108 x^4 y + 162 x^2 y^3
    + 81 x^2 y^2 + 162 x y^3 + 180 x^2 y + 162 x y^2 + 135 x^2
    + 27 x y + 136 x,

B = 45 x^7 + 189 x^6 y + 162 x^5 y + 81 x y^5 + 12 x^5 + 54 x^4 y
    + 27 x^3 y^2 + 162 x y^4 + 27 x y^3 + 81 y^4 + 63 x y^2
    + 27 y^3 + 216 x y + 108 y^2 + 109 y.
```

Sample overlapping carries, as a hand check of the same assembly: `[x]A = 1 + 27·2 + 81·1 = 136`; `[x^2 y]A = 9·2 + 81·2 = 180`; `[x^5]A = 27·2 + 81·1 = 135`; `[x^7]B = 9·2 + 27·1 = 45`; `[y]B = 1 + 27·1 + 81·1 = 109`. All match.

`P=A-A^3` and `Q=B S_5(A)` were then expanded over `Z` and reduced coefficientwise modulo `243` by four engines (sparse unreduced, sparse reduce-every-op, dense box, SymPy). All four, and the second Singular script, produce

```text
P = 162 x^6 y + 162 x^2 y^4 + 135 x^5 + 54 x^4 y + 162 x^2 y^3
    + 81 x^4 + 162 x^3 y + 81 x^2 y^2 + 162 x y^3 + 80 x^3
    + 180 x^2 y + 162 x y^2 + 135 x^2 + 27 x y + 136 x,

Q = 81 x^7 + 216 x^6 y + 162 x^5 y + 81 x^3 y^3 + 81 x y^5 + 12 x^5
    + 63 x^4 y + 81 x^3 y^2 + 81 x^2 y^3 + 162 x y^4 + 27 x y^3
    + 81 y^4 + 165 x^2 y + 63 x y^2 + 27 y^3 + 216 x y
    + 108 y^2 + 109 y.
```

Exact total degrees after reduction: `deg A = deg B = deg P = deg Q = 7`. The degree-seven survivors are

```text
[x^7]A = 162,           [x^7]B = 45,    [x^6 y]B = 189,
[x^6 y]P = 162,         [x^7]Q = 81,    [x^6 y]Q = 216.
```

None of these is `0` modulo `243`, so the equal cap is exact seven, not a concealed six. Reduced grammar: every surviving monomial of `A,B,P,Q` has `i+j <= 7`; the rectangle-but-not-simplex set `{i+j > 7, max(i,j) <= 7}` is empty.

Special fibre. Reducing the same four polynomials modulo `3`:

```text
A ≡ x,     B ≡ y,
P ≡ x + 2 x^3 ≡ x - x^3,     Q ≡ y.
```

(The only residues not divisible by three in `P` are `[x]=136≡1` and `[x^3]=80≡2`; in `Q`, `[y]=109≡1`.) Independently, `A ≡ x (mod 9)` and `B ≡ y + 3 x^5 (mod 9)`, which is the digit claim `a=0`, `b=x^5`.

### 3. Inverse, orientation, both Jacobians, cap cancellations — CONFIRMED

The free-variable identity of Claim 1 already gives `(1-3A^2)S_5(A)=1-243 A^{10}` as a polynomial in `A`. Direct multiplication on this `A` over `Z` recovers exactly `-243 A^{10}` as the remainder; every coefficient is divisible by `243`, and the reduced product is `1`. Consequently `Q(1-3A^2)-B` vanishes modulo `243` (the unreduced difference is a nonzero `243`-divisible polynomial of `1731` terms; it is not claimed to vanish over `Z`). This is the frozen orientation `C_3 ∘ (A,B)=(P,Q)`.

Jacobians. Write `J(U,V)=U_x V_y - U_y V_x`. After reducing `A,B,P,Q` coefficientwise modulo `243`, differentiate those reduced polynomials — not the unreduced `Z`-representatives, and not via the chain rule `dP=D(A) dA`. All four engines, and both Singular scripts, return

```text
det J(A,B) = 1,     det J(P,Q) = 1     in (Z/243Z)[x,y].
```

The unreduced-then-reduce Jacobians agree. In particular `det J(P,Q)=1` is not inferred from `det J(A,B)=1`. (The chain-rule identity `det J(A, Q D(A))=det J(P,Q)` remains available as a consistency check: the extra term `Q D'(A) dA` wedges to zero with `dA`.)

Cap cancellations. Unreduced `P=A-A^3` has `105` monomials of total degree `>7`, in degrees `8` through `21`. Unreduced `Q=B S_5(A)` has `1261` such monomials, in degrees `8` through well above `20`. Every one of those coefficients is divisible by `243`. The smallest unreduced over-cap coefficient of `Q` is `[x^8]Q=1321920=243·5440`. After reduction, no monomial of total degree `>7` survives in `A`, `B`, `P`, or `Q`. That is the exact content of the equal cap seven: the high products cancel modulo `243`, rather than being excluded by a rectangular support restriction.

### 4. Membership, reduction lemma, cited emptiness, exact minimum — CONFIRMED

Membership. Claims 1–3 are exactly polar `(5.3)` at `(p,n,D_F,D_phi)=(3,5,7,7)`. The point is therefore in `B_(3,5)(7,7)`, so that set is nonempty. This is an upper bound `D_min(3,5) <= 7`.

Reduction lemma. Let `φ=(X,Y)` be a point of `B_(3,5)(D,D)` over `Z/243Z`. Write `X',Y'` for the same polynomials with coefficients reduced modulo `81`. Then `φ'` is a point of `B_(3,4)(D,D)` over `Z/81Z`:

- `X' ≡ X ≡ x (mod 3)` and `Y' ≡ Y ≡ y (mod 3)`.
- `det J(X',Y') ≡ det J(X,Y) ≡ 1 (mod 81)`, because a polynomial identity modulo `243` remains an identity modulo `81`, and derivatives of `243`-divisible terms remain `243`-divisible.
- Coefficient reduction cannot increase total degree, so `deg X', deg Y' <= deg X, deg Y <= D` and likewise for the two compositions below.
- `g(X)=X-X^3 ≡ X'-X'^3 = g(X') (mod 81)`.
- `S_5(T)=S_4(T)+81 T^8`, so `Y S_5(X)=Y S_4(X)+81 Y X^8 ≡ Y S_4(X) (mod 81)`. Also `S_4(X) ≡ S_4(X') (mod 81)` and `Y ≡ Y' (mod 81)`, hence `Y S_5(X) ≡ Y' S_4(X') (mod 81)`.

The extra depth-five summand `81 A^8` is precisely the term that dies modulo `81`. There is no hidden constraint at depth five whose reduction would land outside the depth-four system: both systems are polar `(5.3)` at equal total-degree simplex caps, with the same orientation, the same special fibre, and the same Jacobian condition at the corresponding modulus.

Consequently, if `B_(3,5)(D,D)` were nonempty for some `D<=6`, then `B_(3,4)(D,D)` would be nonempty. The contrapositive is the lower bound.

Cited depth-four emptiness. The frozen depth-four producer, hostile-reviewed as **CONFIRMED** at SHA-256 `fecc4e758727b540cef9951ca59162f77cb2d8ff5876132e72f6175350891919`, proves, in this same category,

```text
B_(3,4)(D,D) empty for D <= 6,
B_(3,4)(7,7) nonempty.
```

The emptiness at `D<=4` is reduction to the confirmed depth-three minimum five; the emptiness at `D=5,6` is the unit certificate that the coefficient of `x^6 y` in the `27`-digit of `Q` is `27` times a unit modulo `81`, after the forced bounds `deg a<=2`, `deg b<=D-2`, `c_{[x^5]}=b_{[x^2 y]}=0`, and with `[x^4]L1=0` over `Z`. That is an exhaustive exclusion of the set `B_(3,4)(D,D)` for `D<=6`, not a sample. It is the same equal-cap simplex system, not a rectangle and not a map-cap-only system.

Therefore `B_(3,5)(D,D)` is empty for `D<=6`. Combined with the point of Claim 2,

```text
D_min(3,5) := min { D : B_(3,5)(D,D) nonempty } = 7.
```

Sanity on the displayed point's own reduction: modulo `81` one has degrees `(A,B,P,Q)=(5,7,5,7)`, with surviving degree-seven terms `[x^7]B=45`, `[x^6 y]B=27`, `[x^6 y]Q=54`. So this particular depth-five cap-seven point reduces to a depth-four cap-seven point, which is allowed, and does *not* reduce into the excluded `D<=6` slot. The identity gauge is not this reduction: reduced `B` is not `y`.

### 5. The proposed law is falsified — CONFIRMED

The reviewed depth-four table gives exact minima

```text
D_min(3,2) = 3,     D_min(3,3) = 5,     D_min(3,4) = 7.
```

Those three numbers agree with `(n-1)(p-1)+1` at `p=3`. At `n=5` the same formula predicts nine. Claim 4 supplies `D_min(3,5)=7 < 9`. The law is therefore false at `(p,n)=(3,5)`, as an exact numerical statement about these finite systems. It is not an unproved conjecture that has merely not yet been checked at depth five.

The mechanism is visible in the identity-gauge control: at depths two, three, and four the cotangent truncation realises the minimum, because `3^{n-1} x^{2(n-1)} y` is nonzero modulo `3^n` and has degree `2n-1=(n-1)(p-1)+1`. At depth five that truncation has degree nine, but a non-identity gauge with `a=0` and `b=x^5` cancels every degree-eight-and-nine contribution modulo `243` and realises cap seven. The law predicted the identity-gauge degree, not the minimum.

Nothing in this falsification asserts a replacement formula, a value at depth six, or a rate for `κ_n`.

### 6. No licensed inference off the finite system — CONFIRMED

The producer lists the refusals; they are correct, and they were attacked.

Depth six, this residue class. Interpreting the same integer polynomials `(A,B)` in `(Z/729Z)[x,y]` and forming `S_6=S_5+243 A^{10}` yields

```text
deg A = 7,     deg B = 7,     deg(A-A^3) = 9,     deg(B S_6(A)) = 11
```

modulo `729`. The smallest failing identity for that naive lift is already in `P`:

```text
[x^4 y^4](A - A^3) ≡ 243 ≢ 0 (mod 729),
[x^9](A - A^3)     ≡ 243 ≢ 0 (mod 729).
```

Independently, `[x^{10} y](B S_6(A)) ≡ 486 ≢ 0 (mod 729)`. (The truncated inverse `(1-3A^2)S_6(A)=1-729 A^{12}` *does* hold modulo `729`; inverse-failure is not the obstruction.) Adding a general `243`-digit `(α,β)` and asking whether some lift of this residue class remains bounded is a different search. It is not performed here, and a yes or a no would not change `D_min(3,5)`.

Inverse-limit / polynomial / Tate lift. Polar `(5.3)` at a *fixed* pair of caps is empty for some finite depth, by the reviewed König-plus-no-cancellation argument. A depth-five cap-seven point is compatible with that theorem: the cap may jump later. Existence of a bounded compatible tower, or of a polynomial `Φ_F`, is not implied by a single finite point, and nonexistence is not implied by the naive representatives failing at depth six.

`A_infinity`, deck descent, JC2. The completed gauge and the polar divisor live on the integral unit bidisc. They are not the Hensel residual factor `A_infinity`, not a rational deck action, and not a statement about polynomial invertibility of a characteristic-zero lift that has not been produced. No JC2 inference is licensed.

No unreviewed depth-six Cartier calculation was imported. The depth-six probe above rebuilds the displayed digits in `Z/729Z` and stops.

---

## Non-blocking remarks

1. The launch prompt says “eight displayed base-3 digit polynomials `b,c,d,e,f,g,h`”. That list is seven polynomials; the eighth slot is the undisplayed `a=0`. The producer report is accurate (`a=0`, `b=x^5` in §5, and seven displayed polynomials in §2). No coefficient is missing.
2. The narrative that the nonzero Frobenius-horizontal term `b=x^5` “opens a carry channel that the clean `a=b=0` component lacks” is a description of this witness, not a uniqueness or classification theorem. The minimum does not depend on it.
3. The earlier cap-eight cyclotomic motif `(1-y)(1+y+y^2)=1-y^3` is a different point of a larger system. It is not used here, and cap eight is no longer the upper bound.
4. Reduction of *this* point modulo `81` has `deg(A,P)=5` and `deg(B,Q)=7`. That is consistent with the depth-four minimum seven and is not a cap-six counterexample.
5. Producer replay pins the identity-gauge comparison at cap nine as a positive control of `B_(3,5)(9,9)`. That control is correct and is not the `D=7` witness.

None of these changes a reduced monomial, a Jacobian, the reduction lemma, or a numbered verdict.

---

## Quarantine (closing)

Accept the exact finite-system statement `D_min(3,5)=7` on total-degree simplices, with the frozen orientation, at `p=3`, depth five, modulus `243`. Do not promote it to depth six, to a compatible tower, to a polynomial or Tate lift, to a failure of `κ_n → ∞`, to an `A_infinity` identification, to deck descent, or to JC2. Independent reconstruction, not producer replay, is the evidence. The smallest failing identity for the six numbered claims is none. The smallest failing identity for the unlicensed same-representative depth-six reading is `[x^4 y^4](A-A^3) ≡ 243 (mod 729)`.
