# Hostile different-model review — AS `p=3`, depth-five cap-eight survivor

| Field | Value |
|---|---|
| Claim under review | Frozen producer: the identity-branch equal-cap system `B_(3,5)(8,8)` on total-degree simplices is nonempty; the displayed point is an exact survivor; consequently `D_min(3,5) <= 8 < 9 = (5-1)(3-1)+1`, so the proposed numerical cap-growth law fails at `(p,n)=(3,5)`; cap seven remains open and cap eight is not claimed minimal |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking integer-formula precision below; depth six, a compatible tower, a polynomial/Tate lift, failure of the polar theorem, `A_infinity`, deck descent, and JC2 are correctly *not* claimed) |
| Evidence tier | independent reconstruction of `B_(3,5)(8,8)` from the confirmed polar/wild orientation; exact integer expansions of `P=A-A^3` and `Q=B S_5(A)` by a dense coefficient-matrix engine, a SymPy `ZZ[x,y]` engine, and a second Singular script, none of which import the producer; hand collection of every reduced monomial of `P` and of `Q` from the truncated geometric series; direct Jacobians of the reduced coordinates in addition to the chain rule; unmodified rerun of the two registered programs as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `c327bdc8d02472feba42573760325099f34b8cdf` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T15:54:37Z – 2026-08-24T16:02:00Z |
| Python | host CPython 3.14.6 (hashes, matrix engine, registered replay); uv-pinned SymPy `1.14.0` for the second independent engine |
| Singular | 4.4.1 (`(integer,243)` and characteristic-3 imap) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, freeze, and named parents reread in full before any verdict:

- `xmodel/as-gauge-growth-p3-depth5-d8-survivor-20260824.md` (SHA-256 `3cca09d0c31b46ed12b8510e0d343fd097b2727e2b8ff3aef464c334d48dba6f`)
- `cases/as_gauge_growth_p3_depth5_d8_survivor_20260824/report_n5_d8_survivor.md` (same SHA-256; byte-identical to the xmodel copy)
- `cases/as_gauge_growth_p3_depth5_d8_survivor_20260824/replay_n5_d8_survivor.py` (SHA-256 `0c030b231e6e830a7fcdd50d731db33f01ac3b15523179c5c8e063b6967357ac`)
- `cases/as_gauge_growth_p3_depth5_d8_survivor_20260824/audit_n5_d8_survivor.sing` (SHA-256 `91b347525075083a8fe1a5f9ad4ce6b35e7f00469f2808ed0c4fab0ed7d7cea8`)
- `cases/as_gauge_growth_p3_depth5_d8_survivor_20260824/MANIFEST_n5_d8_survivor.sha256` (SHA-256 `7cf4df1eb4427d08fc2eb6bfa665466b05c65d7b7beaa2f0ca1ebbb81fe0e16d`)
- `cases/as_gauge_growth_p3_depth5_d8_survivor_20260824/FREEZE_n5_d8_survivor.txt` (SHA-256 `e64cd77214d0809fd5c5b3754d002daa687b98183362901afb4a99219baf83a9`)

Depth-four table, consumed only at its reviewed equal-cap simplex scope:

- `xmodel/as-gauge-growth-p3-depth4-gate-20260824.md` (SHA-256 `bfacd9a475f8e2aa7da9d26e43785b80ff3eadd53615e4823dfe6d52fc6fd660`)
- `xmodel/as-gauge-growth-p3-depth4-review-grok-20260824.md` (SHA-256 `fecc4e758727b540cef9951ca59162f77cb2d8ff5876132e72f6175350891919`), overall **CONFIRMED**

Bounded-polar and completed-gauge parents, consumed only for the finite system `B_(p,n)(D_F,D_phi)` and the orientation `C_p ∘ Φ_F = F`:

- `xmodel/as109-bounded-polar-conductor-gate-20260824.md` (SHA-256 `2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b`)
- `xmodel/as109-bounded-polar-conductor-review-grok-20260824.md` (SHA-256 `bda4dda7d24d36bf75b6c55b566f708ee300c80aeb3344c4bb724bfc7e7787fa`), overall **CONFIRMED**
- `xmodel/as109-wild-symplectic-conductor-gate-20260824.md` (SHA-256 `c7ad3660c136bbee7105e786cc8b717d025534b67ac63cababb33c4b6de29e7c`)
- `xmodel/as109-wild-symplectic-conductor-review-grok-20260824.md` (SHA-256 `a59c7ccbf39971ad7ab47f8e865926c93e4ac9d46305be076f4bd0193b2b1a9a`), overall **CONFIRMED**

The committed basis is exactly `c327bdc8d02472feba42573760325099f34b8cdf`. Named producer artifacts remain uncommitted on top of that basis. No producer, case, canonical, ladder, notes, prompt, log, run, or erratum file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp` and did not import `replay_n5_d8_survivor.py` or `audit_n5_d8_survivor.sing`.

Tried hard, and failed, to reverse the composition to `Φ ∘ C_3` or `F ∘ Φ`, to read the system on an exponent rectangle, to drop the gauge cap or the map cap, to keep a monomial of total degree `>8` after coefficientwise reduction modulo `243`, to make `det J(P,Q)` fail while `det J(A,B)=1`, to cancel `x^8 y` without the pair `(c,d)`, to let `{c,d}` fail to be a multiple of three, to treat `f` as the source of the `Q`-cap rather than of the determinant carry, to realise this exact `(A,B)` at depth six modulo `729`, to drop this point to cap seven, and to promote the survivor to a polar-theorem failure, a polynomial lift, `A_infinity`, deck descent, or JC2.

---

## Promotion

**Accept `B_(3,5)(8,8)` IS NONEMPTY and the predicted cap-nine law is false at depth five.**

On the same identity-branch equal-cap simplex category as the reviewed depth-four table:

- The finite system is polar `(5.3)` at `p=3`, `n=5`, `D_F=D_phi=8`: polynomial gauge `(A,B)` over `Z/243Z` with `A ≡ x`, `B ≡ y (mod 3)`, `det J(A,B)=1`, and `deg(A-A^3), deg(B S_5(A)) <= 8`, with `S_5=1+3A^2+9A^4+27A^6+81A^8`. The orientation is `C_3 ∘ (A,B) = (P,Q)`, not the reverse.
- The displayed point
  `A=x+9x^5-9x^5 y`, `B=y+9x^4+198 x^4 y+144 x^4 y^2`
  reduces to total degrees `(6,6,8,8)` with special fibre `(x-x^3,y) (mod 3)` and with no reduced monomial of total degree `>8`.
- Independently, `(1-3A^2)S_5(A)=1 (mod 243)`, `B=Q(1-3A^2)`, `det J(A,B)=det J(P,Q)=1 (mod 243)`, the last also by direct differentiation of the reduced coordinates.
- The pair `c=x^5(1-y)`, `d=x^4(1+y+y^2)` cancels the degree-nine cotangent monomial `x^8 y` in the `81`-digit of `Q`; `f=7x^4 y+5x^4 y^2` absorbs the divided divergence; `{c,d}` is a multiple of three. This is an exact finite-depth construction, not a proved all-depth recurrence.
- Therefore `D_min(3,5) <= 8 < 9`. Combined with the confirmed depth-four minimum seven, one has `7 <= D_min(3,5) <= 8`. Cap seven is open and cap eight is not proved minimal.

**Do not promote this to:** emptiness or existence at cap seven; a depth-six point, a compatible inverse-limit tower, or a polynomial/Tate lift; failure of the polar theorem `κ_n → ∞`; an `A_infinity` identification; deck descent; a counterexample to JC; or any JC2 inference.

**Smallest honest successor.** Exact emptiness or a point of `B_(3,5)(7,7)` decides whether the minimum is seven or eight. Independently, lifting the cancellation motif to depth six while keeping a stated cap, starting at the present cap eight, is the smallest test of whether the new mechanism iterates. Neither is licensed by this finite survivor.

---

## Quarantine

No result here proves or disproves JC2, constructs or excludes a polynomial lift of `(x-x^3,y)`, identifies the polar divisor with `A_infinity`, runs `p=109`, or produces a compatible tower. Producer strings `EXACT_BOUNDED_SURVIVOR_D8_FALSIFIES_PREDICTED_D9_CAP_LAW` and `AUDIT_PASS` were not used as evidence; the system, the reduced supports, both Jacobians, the carry identities, and the `81`-digit cancellation were re-derived. The polar parent is used only for `B_(p,n)(D_F,D_phi)` on total-degree simplices and for the orientation `C_p ∘ Φ_F=F`, at the reviewed scope that every *fixed* cap dies at some finite depth. That parent does not predict the numerical law `(n-1)(p-1)+1`, and a depth-five cap-eight point does not contradict it. Independent reconstruction, not the producer scripts, is the evidence for every numbered claim.

---

## Scope (not enlarged)

One prime `p=3`; one Witt depth `n=5`; equal total-degree simplex caps; exact coefficient ring `Z/243Z`; identity branch. The displayed survivor is a finite cotangent-cancelled point, not a lift to all depths. No rectangular support, no enumerator, no AWS, and no modular-to-characteristic-zero existence inference are in scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Frozen identity-branch system at `p=3,n=5` is `P=A-A^3`, `Q=B S_5(A)`, `S_5=1+3A^2+9A^4+27A^6+81A^8` modulo `243`, with `det J(A,B)=1` and total-degree simplex caps on both gauge and map. Same orientation and category as the reviewed depth-four table | **CONFIRMED** | reverse composition; rectangle support; map cap without gauge cap, or the reverse; `S_5` truncated at `A^6`; a different special fibre |
| 2 | The displayed `(A,B)` reduces to degrees `(6,6,8,8)` with the displayed monomials of `P` and `Q`, special fibre `(x-x^3,y) (mod 3)`, and no reduced monomial of total degree `>8` | **CONFIRMED** | a reduced degree-nine term; `81 x^8 ≡ 0 (mod 243)`; `P ̸≡ x-x^3 (mod 3)`; support tables imported rather than recomputed |
| 3 | `(1-3A^2)S_5(A)=1 (mod 243)`, `B=Q(1-3A^2)`, `det J(A,B)=det J(P,Q)=1 (mod 243)` by chain rule *and* by direct differentiation; `c_x+d_y=3x^4(2-y)`, `f_y=x^4(10y+7)`, `{c,d}=-3x^8(2y^2-3y-3)`, and `9(c_x+d_y)+27 f_y=243 x^4(1+y)` | **CONFIRMED** | truncated inverse remainder not divisible by `243`; `det J(P,Q)` only inferred; carry identity failing over `Z`; `{c,d}` not a multiple of three |
| 4 | `c,d` cancel the high part of `x^4 d+x^3 c y+x^8 y` in the final `Q` digit; the divided divergence is absorbed by `f`; the remaining bracket is divisible by three. Exact construction, not an all-depth recurrence | **CONFIRMED** | `x^8 y` surviving modulo `243`; `f_y ̸≡ -x^4(2-y) (mod 9)`; the three-row motif sold as a theorem for every `n` |
| 5 | The point lies in `B_(3,5)(8,8)`, so `D_min(3,5)<=8`, while the preregistered prediction was nine. The law `(n-1)(p-1)+1` is therefore false at `(3,5)`. Cap seven is open and cap eight is not proved minimal | **CONFIRMED** | a hidden extra cap in the system; the law only claimed as a depth-four coincidence and not tested; cap seven declared empty; `D_min=8` asserted |
| 6 | No inference to depth six, a compatible tower, a polynomial/Tate lift, failure of the polar theorem, `A_infinity`, deck descent, or JC2. Honest successors: exact cap seven, and lifting this motif to depth six at a stated cap | **CONFIRMED** | a hidden `n=6` claim; `κ_n → ∞` declared false; this point sold as a lift; a JC2 sentence |

All remarks below are non-blocking unless marked otherwise. None changes a reduced monomial, a Jacobian, or a numbered verdict.

---

## Replay and hashes

Frozen hashes, recomputed on the charged tree, match the launch prompt, the manifest, and the freeze record:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as-gauge-growth-p3-depth5-d8-survivor-20260824.md` | `3cca09d0c31b46ed12b8510e0d343fd097b2727e2b8ff3aef464c334d48dba6f` | prompt; byte-identical case copy |
| `cases/.../report_n5_d8_survivor.md` | `3cca09d0c31b46ed12b8510e0d343fd097b2727e2b8ff3aef464c334d48dba6f` | prompt, `MANIFEST` |
| `cases/.../replay_n5_d8_survivor.py` | `0c030b231e6e830a7fcdd50d731db33f01ac3b15523179c5c8e063b6967357ac` | prompt, `MANIFEST` |
| `cases/.../audit_n5_d8_survivor.sing` | `91b347525075083a8fe1a5f9ad4ce6b35e7f00469f2808ed0c4fab0ed7d7cea8` | prompt, `MANIFEST` |
| `cases/.../MANIFEST_n5_d8_survivor.sha256` | `7cf4df1eb4427d08fc2eb6bfa665466b05c65d7b7beaa2f0ca1ebbb81fe0e16d` | prompt, freeze `manifest_sha256` |
| `cases/.../FREEZE_n5_d8_survivor.txt` | `e64cd77214d0809fd5c5b3754d002daa687b98183362901afb4a99219baf83a9` | prompt |
| canonical replay payload | `b5fb3f3e48c7193ea385293ce38bbe62219a84ebd318ce72c8f47587d3c24382` | prompt, freeze `python_payload_sha256`, live stdout |
| depth-four gate | `bfacd9a475f8e2aa7da9d26e43785b80ff3eadd53615e4823dfe6d52fc6fd660` | parent |
| depth-four review | `fecc4e758727b540cef9951ca59162f77cb2d8ff5876132e72f6175350891919` | parent |
| polar-conductor gate | `2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b` | parent |
| polar-conductor review | `bda4dda7d24d36bf75b6c55b566f708ee300c80aeb3344c4bb724bfc7e7787fa` | parent |
| wild-symplectic gate | `c7ad3660c136bbee7105e786cc8b717d025534b67ac63cababb33c4b6de29e7c` | parent |
| wild-symplectic review | `a59c7ccbf39971ad7ab47f8e865926c93e4ac9d46305be076f4bd0193b2b1a9a` | parent |

Every member hash inside `MANIFEST_n5_d8_survivor.sha256` was recomputed from the case directory and matched. The freeze record is not a second copy of the manifest; it names the manifest digest and the canonical payload digest.

Registered commands, rerun unmodified from the case directory:

```text
python3 replay_n5_d8_survivor.py
Singular -q audit_n5_d8_survivor.sing
```

Both exited 0. Live payload SHA-256 `b5fb3f3e48c7193ea385293ce38bbe62219a84ebd318ce72c8f47587d3c24382`. Singular printed `AUDIT_PASS p=3 n=5 D=8 modulus=243` with degrees `6,6,8,8` and the same reduced `P,Q` as the report. Those Booleans were discarded as evidence for Claims 1–6.

Independent engines, written for this review and not imported from either registered program (scratch SHA-256, outside the repository):

- dense `N=24` coefficient-matrix engine, host CPython 3.14.6: `c5b49abd2e2ea51164ad24e3460b0ed66d2f23666b9135f74821f87ee6198c50`
- SymPy `1.14.0` over `ZZ[x,y]`: `b3eef103bc50dce2303f85deb0a369e6dd34e9833073a05cc17bcc3e32711a7c`
- second Singular script over `Z/243Z` plus characteristic-3 imap: `3638a20934800d1ad67161451dbc325e872dacf0659286e2492b7292a7033db6`

The matrix box truncates unreduced monomials of `x`-degree `>=24`. Every such monomial has total degree `>=24` and, by the untruncated SymPy expansion, coefficient divisible by `243`. Reduced cap-eight supports were cross-checked against both non-truncating engines.

---

## Independent recomputation

### 1. System and cap semantics — CONFIRMED

Write `g(T)=T-T^3`, `D(T)=1-3T^2`, `C_3=(g,y/D)`. The confirmed wild/polar orientation is `C_3 ∘ Φ_F = F` with `Φ_F=(A,B)` on the identity branch. Coordinate comparison is tautological:

```text
A - A^3 = P,             B / D(A) = Q,
```

hence `B = Q(1-3A^2)`. Reverse composition `Φ ∘ C_3` and left-vs-right swap `F ∘ Φ = C_3` are not this statement.

At finite depth five, `S_5(T)=∑_{j<5} 3^j T^{2j}` satisfies the polynomial identity

```text
(1-3T^2) S_5(T) = 1 - 243 T^{10}.
```

Independently expanded in a free variable `T` over `Z`, the remainder is exactly `-243 T^{10}`; it vanishes in `(Z/243Z)[T]`. Thus `Q := B S_5(A)` is the correct finite-depth second coordinate, and `C_(3,5) ∘ (A,B) = (A-A^3, B S_5(A))` in `(Z/243Z)[x,y]`. Polar `(5.3)` at equal caps is exactly

```text
A ≡ x, B ≡ y (mod 3),
det J(A,B) = 1 in Z/243Z,
deg(A), deg(B) <= 8,          (gauge cap)
deg(A-A^3), deg(B S_5(A)) <= 8.   (map cap)
```

Supports are total-degree simplices: a monomial `x^i y^j` is admitted iff `i+j <= D`. This is the same grammar as the reviewed depth-four table, not an exponent rectangle. Dropping either cap would define a different system. The identity-gauge control `A=x`, `B=y` realises map degree nine and is the pinned positive control of that larger system `B_(3,5)(9,9)`; it is not a point of `B_(3,5)(8,8)`.

### 2. Exact survivor — CONFIRMED

Work from the displayed polynomials, not from producer support tables. Over `Z`,

```text
c = x^5(1-y),     d = x^4(1+y+y^2),     f = 7 x^4 y + 5 x^4 y^2,
A = x + 9c = x + 9x^5 - 9x^5 y,
B = y + 9d + 27f = y + 9x^4 + 198 x^4 y + 144 x^4 y^2.
```

The coefficient check `9+27·7=198` and `9+27·5=144` is exact. After reduction modulo `243`,

```text
A = x + 9x^5 + 234 x^5 y,          (234 ≡ -9)
B = y + 9x^4 + 198 x^4 y + 144 x^4 y^2,
```

with total degrees `6,6`. For `P=A-A^3`, the binomial expansion uses `(9c)^2=81 c^2` and `(9c)^3=729 c^3`:

```text
A^3 = x^3 + 27 x^7(1-y) + 243 x^{11}(1-y)^2 + 729 x^{15}(1-y)^3
    ≡ x^3 + 27 x^7 - 27 x^7 y   (mod 243).
```

Hence, over `Z/243Z`,

```text
P = x - x^3 + 9x^5 - 9x^5 y - 27 x^7 + 27 x^7 y
  = x + 242 x^3 + 9x^5 + 234 x^5 y + 216 x^7 + 27 x^7 y,
```

using `242 ≡ -1`, `234 ≡ -9`, `216 ≡ -27`. Total degree eight; the leading reduced terms `27 x^7 y` and `216 x^7` are nonzero. Every unreduced monomial of `P` of degree `>8` has coefficient divisible by `243` (SymPy: degrees `11` and `15` with coefficients `±243, ±486, ±729`).

For `Q=B S_5(A)`, write `A=x+9c` so that `A^k ≡ x^k + 9k x^{k-1} c + 81 binom(k,2) x^{k-2} c^2 (mod 243)`. Collecting every summand that can survive modulo `243` gives the exact truncated expansion

```text
Q ≡ y + 3x^2 y + 54 x c y
     + 9x^4 y + 81 x^3 c y
     + 27 x^6 y + 81 x^8 y
     + 9d + 27 d x^2 + 81 d x^4
     + 27f + 81 f x^2          (mod 243).
```

Substituting the displayed `c,d,f` and reducing coefficients produces exactly

```text
Q = y + 3x^2 y + 9x^4 + 207 x^4 y + 144 x^4 y^2
      + 27 x^6 + 189 x^6 y + 135 x^6 y^2 + 81 x^8.
```

Sample collection: the `x^6 y` integer coefficient is `54+27+27+567=675 ≡ 189 (mod 243)`; the `x^6 y^2` coefficient is `-54+27+405=378 ≡ 135 (mod 243)`; the `x^4 y` coefficient is `9+9+189=207`. The three independent engines return this support and no other reduced monomial. Total degree eight; `81 x^8 ̸≡ 0 (mod 243)`. No reduced monomial has `i+j > 8`.

Special fibre: `9c ≡ 0`, `9d ≡ 0`, `27f ≡ 0 (mod 3)`, and `S_5(A) ≡ 1 (mod 3)`, so `(A,B) ≡ (x,y)` and `(P,Q) ≡ (x-x^3,y) (mod 3)`.

The signed Singular representative `x-x^3+9x^5-9x^5 y-27x^7+27x^7 y` is the same reduced polynomial as the unsigned report form. There is no mismatch.

### 3. Inverse, orientation, and Jacobians — CONFIRMED

The geometric identity of Claim 1 specialises at this `A` to `(1-3A^2)S_5(A)=1 (mod 243)`. All three engines record `D(A) S_5(A) ≡ 1` and `Q D(A) ≡ B`. That is the frozen orientation `C_3 ∘ (A,B)=(P,Q)`.

Jacobian of the gauge, over `Z`:

```text
A_x = 1+9 c_x,   A_y = 9 c_y,
B_x = 9 d_x + 27 f_x,   B_y = 1+9 d_y + 27 f_y,
det J(A,B)
  = 1 + 9(c_x+d_y) + 27 f_y + 81{c,d} + 243{c,f}.
```

The last summand is absent from the producer's displayed formula. It is already a multiple of `243`, so the displayed formula is correct *modulo `243`*, which is the stated claim. Direct differentiation of the displayed `c,d,f` gives

```text
c_x + d_y = 3x^4(2-y),
f_y       = x^4(10y+7),
{c,d}     = 9x^8 + 9x^8 y - 6 x^8 y^2
          = -3x^8(2y^2-3y-3),
{c,f}     = 35 x^8 + 43 x^8 y - 30 x^8 y^2.
```

Then `9(c_x+d_y)+27 f_y = 243 x^4(1+y)` as an identity over `Z`, and `81{c,d}` is a multiple of `243` because `{c,d}` is a multiple of three. Unreduced `det J(A,B)` is

```text
1 + 243 x^4(1+y) + 9234 x^8 + 11178 x^8 y - 7776 x^8 y^2,
```

and every non-constant coefficient is divisible by `243`. Reduced, `det J(A,B)=1`.

Chain rule for the truncated composition `C_(3,5)=(u-u^3, v S_5(u))`:

```text
dP = (1-3A^2) dA,
dQ = S_5(A) dB + B S_5'(A) dA,
```

the second summand wedges with `dA` to zero, and `(1-3A^2)S_5(A)=1-243 A^{10}`, so

```text
det J(P,Q) = (1-243 A^{10}) det J(A,B)
```

as an identity over `Z`. SymPy records this remainder as the zero polynomial; the matrix engine records it after convolution. Reducing, `det J(P,Q) ≡ 1 (mod 243)`.

The same determinant was recomputed without that inference, by differentiating the already-reduced displayed `P` and `Q` (and, independently, by Singular on `Z/243Z`). Both routes return `1`. Differentiation and reduction commute on polynomial rings, so this is not a representative artefact.

### 4. Counter-motif — CONFIRMED

The identity gauge contributes `81 x^8 y` to `Q`, of total degree nine. The `81`-digit sources that can see degree eight or nine are `y A^8`, `d A^4`, `x^3 c y`, and `f A^2`. Their top part is

```text
x^4 d + x^3 c y + x^8 y
  = x^8(1+y+y^2) + x^8 y(1-y) + x^8 y
  = x^8 + 3 x^8 y.
```

The `y^2` terms cancel over `Z`. Multiplication by `81` yields `81 x^8 + 243 x^8 y ≡ 81 x^8 (mod 243)`. That is the exact cancellation of the degree-nine cotangent monomial, leaving a degree-eight monomial on the simplex boundary. It uses the finite geometric series through `A^8`; omitting `81 A^8` would not produce the class, and omitting `c` or `d` would leave `81 x^8 y` or `81 x^8 y^2`.

The first-digit divergence `c_x+d_y=3x^4(2-y)` is not zero over `Z`, but is a multiple of three of degree five. The condition that `f` absorb the divided divergence is `f_y ≡ -x^4(2-y) (mod 9)`. The displayed `f` has `f_y=x^4(7+10y)` and `7+10y-(y-2)=9(y+1)`, so the congruence holds. Equivalently `div/3 + f_y = 9x^4(1+y) ≡ 0 (mod 9)`. Without `f`, one would have `det J(A,B) ≡ 1+27x^4(2-y) ̸≡ 1 (mod 243)`. Digit `f` is a determinant correction, not the source of the `Q`-cap: `c,d` already kill `x^8 y` in `Q`.

The remaining bracket `{c,d}` is a multiple of three, so `81{c,d}` vanishes modulo `243`. This is the carry missed by a naive two-row induction that would keep the final cotangent class forced.

The three linked rows are an exact construction at this one depth. They are not a proved recurrence for every `n`, and the producer does not state them as one. In particular they do not supply a depth-six point.

### 5. Falsification logic — CONFIRMED

The reconstructed point satisfies every equation of `B_(3,5)(8,8)`: identity branch, both simplex caps, both determinants, and the truncated orientation. Hence that system is nonempty and `D_min(3,5) <= 8`.

The proposed formula `(n-1)(p-1)+1` gives `9` at `(3,5)`. It was the numerical law that survived the confirmed depth-four table `3,5,7`, and the preregistered depth-five discriminator — named by the depth-four review, the audit ledger, and the live notes — was cap eight against the cap-nine cotangent control. A survivor strictly below nine falsifies the equality `D_min(3,5)=9`. That is a falsification of a proposed numerical law at one pair `(p,n)`, not a polynomial lift and not a no-lift theorem.

This particular point is not a cap-seven witness: `deg P=deg Q=8` exactly, because `216 x^7` and `81 x^8` are nonzero modulo `243`. The identity-branch gauge of a given `F` is unique, so no other representative of this same `F` has smaller gauge degree. Existence of some other point of `B_(3,5)(7,7)` is not decided. Reduction of a depth-five equal-cap point modulo `81` lands in `B_(3,4)(D,D)`, and the confirmed depth-four minimum is seven, so `D_min(3,5) >= 7`. The honest remaining discriminator is exactly cap seven.

### 6. Scope and successor — CONFIRMED

The producer refuses every promotion listed in the launch prompt, and the mathematics agrees.

- *Depth six.* The same polynomials `(A,B)`, read modulo `729`, do not lie in `B_(3,6)(*,*)` at cap eight. Unreduced `det J(A,B)` contributes `243 x^4(1+y)` and degree-eight terms, all nonzero modulo `729`. Independently, `Q=B S_5(A)` already has reduced total degree `13` modulo `729` (`243 x^8 y^2` and several degree-ten terms). The extra geometric summand `243 A^{10}` of `S_6` changes the `x^{10} y` coefficient but leaves over-cap terms. Fresh `243`-digits would be required even to restore the determinant. This artifact does not provide them.
- *Compatible inverse-limit tower / polynomial or Tate lift.* A bounded-degree compatible tower would inverse-limit to a polynomial gauge with polynomial composition, contradicting the confirmed polar no-cancellation lemma. A polynomial `F` over `Z_3` would have `κ_n(F) → ∞`. One finite-depth point is not such a tower.
- *Polar theorem.* Polar `(0.3)` asserts that every *fixed* equal cap dies at some finite depth, equivalently `κ_n → ∞` for a hypothetical polynomial lift. It does not assert `D_min(p,n)=(n-1)(p-1)+1`. A depth-five cap-eight survivor is compatible with unbounded later conductors.
- *`A_infinity`, deck descent, JC2.* None of the identities above names the residual generic factor, a rational deck map, or a characteristic-zero Keller pair. The identity-gauge control remains a valid cap-nine point; the new point is a strictly better bounded control and does not make the identity control incorrect.

Honest successors remain exactly those named in the promotion section: decide `B_(3,5)(7,7)`, and test whether the `(c,d,f)` cancellation can be lifted to depth six at a stated cap, starting at eight. An inductive highest-carry lemma that would have promoted the slope law is now known to fail in the form that kept `x^{2(n-1)} y` forced at every depth.

---

## Non-blocking remarks

1. The integer Jacobian identity is `1+9(c_x+d_y)+27 f_y+81{c,d}+243{c,f}`. The producer omits `{c,f}` because the claim is modulo `243`. Unreduced, `{c,f}=35x^8+43x^8 y-30x^8 y^2` accounts for the leftover degree-eight coefficients `8505, 10449, -7290` after the displayed carry and bracket are subtracted. None of those coefficients survives modulo `243`.
2. Unreduced `P` and `Q` have total degrees `18` and `54`. Every monomial above cap eight has coefficient divisible by `243`. The bounded system is the reduced one.
3. Digit `f` is required for `det J(A,B)=1` and is not required to bring `deg Q` down to eight. Presentation that lists `f` among the three linked rows is still accurate, because the point as a whole uses all three.
4. The parent lower bound `D_min(3,5) >= 7` is reduction to the confirmed depth-four minimum, not a computation inside this freeze. The producer correctly leaves cap seven open rather than asserting `D_min=8`.
5. Registered Python and Singular are same-model regression. They agree with the independent engines on the reduced supports and both determinants; that agreement was not used as a substitute for the expansions above.

None of these changes a reduced monomial, a valuation, or a numbered verdict.
