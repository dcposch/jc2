# Hostile different-model review — AS map-only `p=3,D=7` associated top components

| Field | Value |
|---|---|
| Claim under review | Frozen producer: the first-digit high carry rows of degrees 12 and 11 have three reduced layer-`7/6` components and one load-bearing embedded primary component. This is a checkpoint, not a classification of the full cap-seven lift locus |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking writeup remarks below; carry rows 10..7, the Cartier row, an accepted second digit, emptiness or nonemptiness of `FONLY_(3,7)(D=7)`, all-depth lifting, characteristic zero, a counterexample, and JC2 are correctly *not* claimed) |
| Evidence tier | independent integer Jacobian identity over `Z`; independent sparse polynomial emitter using the product rule then reduction modulo 3 (not the producer derivative dictionaries); 200+80 random `F3` spot-checks of every emitted row against literal `det D`; leftover five-quadric affine point census over `F3`; independent Singular Groebner bases, `minAssGTZ`, `primdecGTZ`, and `primdecSY`; two-sided ideal reduction across monomial orders `dp`/`lp`/`Dp` and reversed generators; unmodified rerun of the three registered programs as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `1e60fcedc8626650c7c7544ad296c3624173415f` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T17:30:56Z – 2026-08-24T17:46:57Z |
| Python | host CPython 3.14.6 (hashes, sparse emitter, affine census, spot-checks, registered replays) |
| Singular | 4.4.1 |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, freeze, and named payloads reread in full before any verdict:

- `xmodel/as-fonly-p3-d7-associated-top-components-20260824.md` (SHA-256 `e50297762088b17e3a01d98e4a76823ec6f33abe02df8b05f50486a3224c30a3`)
- `cases/as_fonly_p3_d7_associated_top_components_20260824/FREEZE.txt` (SHA-256 `c89c9e29aac0be1b7ebfe7042364c2a879876d2c6717cd1ceb93232286a46da6`)
- `cases/as_fonly_p3_d7_associated_top_components_20260824/MANIFEST.sha256` (SHA-256 `e8e7e7169966848a58cdac9aac7412e5e5e2d2d4f56c521f0b4d7a3a570d6bf9`)
- `cases/as_fonly_p3_d7_associated_top_components_20260824/README.md` (SHA-256 `596e8290e56f6050d77d400a129f4f7feaac72bf58b8f88c7a287b4d53b14c1f`)
- `cases/as_fonly_p3_d7_associated_top_components_20260824/generate_top_gate.py` (SHA-256 `64032b10b8ec0c9fbed4a9e3cd12d314d28b58264f6dcb929bec816d696af411`)
- `cases/as_fonly_p3_d7_associated_top_components_20260824/generate_layers76_gate.py` (SHA-256 `2dd77cadc42509b3e2fff62a97642a769d783a8d02e46f1d9ab353602a231973`)
- `cases/as_fonly_p3_d7_associated_top_components_20260824/replay_rows_and_incidence.py` (SHA-256 `38ab633076c804f6a60ccc24e8b338cfe303ea5c7c52f11fd44cdf97f646e986`)

Confirmed triangular-terminal parent, consumed only for the displayed integer first map and to refuse promotion into a full-locus statement:

- `xmodel/as-fonly-p3-d7-depth6-triangular-terminal-20260824.md` (SHA-256 `5325890a505489570a6e02409d64e026560d2635ddf989b865039eeb6ecddccb`)
- `xmodel/as-fonly-p3-d7-depth6-triangular-terminal-review-grok-20260824.md` (SHA-256 `75ff0c8588c633fcf53e17104bf77cdc74fba30bc9c02aa776b23ad0baaa2318`), overall **CONFIRMED**

The committed basis is exactly `1e60fcedc8626650c7c7544ad296c3624173415f`. Named producer artifacts remain uncommitted on top of that basis. No producer, case, canonical, ladder, notes, prompt, log, run, or erratum file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp/as_fonly_p3_d7_assoc_review/` and did not import `generate_top_gate.py`, `generate_layers76_gate.py`, or `replay_rows_and_incidence.py`.

Tried hard, and failed, to leak the fixed `-x^2 V_y` term into carry degrees 12 or 11; to obtain a third top minimal prime, a radical original top ideal, or an embedded associated prime at the one-layer stage; to keep a derivative-visible degree-six coefficient alive on a dimension-ten branch; to keep a nonzero degree-seven layer on the dimension-eight branch; to separate the embedded associated prime from the claimed support `U_7=V_7=0` plus eight derivative-visible degree-six zeros; to move the origin off any associated-prime support; to change the set of minimal primes by reversing generators or switching to `lp`/`Dp`; and to promote the checkpoint to emptiness or nonemptiness of `FONLY_(3,7)(D=7)`, an accepted second digit, all-depth lifting, characteristic zero, a counterexample, or JC2.

---

## Promotion

**Accept `THE FIRST-DIGIT HIGH CARRY ROWS OF DEGREES 12 AND 11 HAVE THREE REDUCED LAYER-7/6 COMPONENTS AND ONE LOAD-BEARING EMBEDDED PRIMARY COMPONENT. THIS IS A CHECKPOINT, NOT A CLASSIFICATION OF THE FULL CAP-SEVEN LIFT LOCUS`.**

On the map-only first digit `P=x-x^3+3U`, `Q=y+3V` over `F_3`, with `U,V` of total degree at most seven:

- The identity `det J=1+3(U_x+V_y-x^2)+9K` holds over `Z`, with `K=(U_x-x^2)V_y-U_y V_x`. The degree-six and degree-five divergence rows together with the degree-12 and degree-11 coefficients of `det D(U_7+U_6,V_7+V_6)` are the exact gate. The fixed term `-x^2 V_y` has degree at most eight and does not enter those two carry rows.
- The top degree-seven scheme has 16 variables, 20 nonzero rows, reduced Groebner size 16, dimension four, and exactly two dimension-four minimal associated primes, sharing the linear spine `(4)` displayed below. The original ideal is not radical: its primary decomposition has two components, one nonprime thickening (sizes 18/22) and one prime (sizes 22/22), and no embedded associated prime.
- Attaching all 14 degree-six coefficients, complete degree-five divergence, and degree-11 carry to the original nonreduced top ideal yields 30 variables, 38 nonzero rows, reduced Groebner size 59, dimension ten, and exactly three minimal primes of dimensions `10,10,8`. The two dimension-ten primes force the eight derivative-visible degree-six coefficients to zero and leave the six Frobenius coefficients free. The dimension-eight prime is `U_7=V_7=0` together with the complete degree-six divergence.
- The complete primary decomposition has a fourth, embedded component of dimension six (sizes 329/24) whose associated support is exactly zero degree-seven layer plus those eight derivative-visible zeros. The nilpotent thickening is load-bearing for accepted-digit / Fitting recursion; field-valued point coverage of this gate still sees only the three minimal supports.
- The frozen triangular first digit is `(U_0,V_0)=(x^3,x^2 y)` over `F_3`. Its degree-`7/6` projection is the origin, which lies on both top minimal primes, all three layer-`7/6` minimal primes, and all four associated-prime supports.

**Do not promote this to:** a statement about carry rows of degrees 10, 9, 8, or 7; the Cartier coefficient `[x^2 y^2]K`; existence of an accepted second digit; emptiness or nonemptiness of `FONLY_(3,7)(D=7)` or of the full depth-six D7 locus; all-depth lifting; a characteristic-zero lift or no-lift theorem; a counterexample to JC; or any JC2 inference. Incidence of the origin at this gate does not place the full lower-degree triangular point on every eventual component.

**Smallest honest successor.** Descend componentwise through the degree-10 carry row, attaching the degree-five layer, and retain the original nonreduced primary structure including the embedded component `(5)`. That is the next homogeneous obstruction and the cheapest exact continuation of the associated-scheme program. A reduced calculation still covers field-valued points of *this* gate, but it is not an honest successor for accepted-digit / Fitting recursion. Do not replace the successor by the already observed opaque global Groebner basis in 42 variables.

---

## Quarantine

No result here proves or disproves JC2, constructs or excludes a polynomial lift of `(x-x^3,y)`, empties or populates `FONLY_(3,7)(D=7)`, runs a second accepted digit, attaches carry rows 10..7 or the Cartier row, or produces a compatible tower. Producer strings `PASS-TOP-COMPONENTS`, `PASS-LAYERS76`, and `PASS-FONLY-D7-TOP-ROW-PROVENANCE` were not used as evidence; the Jacobian identity, every row coefficient, both prime ideals, the four primary components, the containments, and the origin reductions were re-derived. The triangular-terminal parent is used only for the displayed integer maps `(P,Q)` and to keep the present file a checkpoint rather than a locus classification. Independent reconstruction, not the producer scripts, is the evidence for every numbered claim.

---

## Scope (not enlarged)

One prime `p=3`; one total-degree cap seven; the first map digit only; homogeneous divergence degrees 6 and 5; next-carry homogeneous degrees 12 and 11. No rectangular support, no enumerator, no AWS, no gauge cap, and no modular-to-characteristic-zero existence inference are in scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | From `P=x-x^3+3U`, `Q=y+3V`, the identity `det J=1+3(U_x+V_y-x^2)+9K` holds over `Z` with `K=(U_x-x^2)V_y-U_y V_x`. A D7 next digit affects divergence only through degree six. Carry degrees 12/11 equal the corresponding rows of `det D(U_7+U_6,V_7+V_6)`; `-x^2 V_y` has degree at most 8. Independently enumerated variables, nonzero rows, signs, and every coefficient match 16/20 and 30/38 | **CONFIRMED** | a leftover `27`-term in the Jacobian; a degree-7 derivative producing degree 7; `-x^2 V_y` of degree `>=11`; a vanished or extra row; a coefficient/sign mismatch against literal `det D` |
| 2 | Over `F_3`: 16 variables, 20 rows, Groebner size 16, dimension 4, exactly two dimension-4 minimal associated primes, common spine `(4)`, two-sided equality of both displayed primes, order/generator independence, two primary components with one nonprime thickening (18/22) and one prime (22/22), no embedded associated prime, original ideal not radical | **CONFIRMED** | a third minAss prime; radical original ideal; an embedded associated prime; two-sided failure against a displayed prime; `lp`/`Dp`/reversed generators producing a different set of primes; both primaries equal to their associated primes, or neither |
| 3 | Attaching all 14 degree-six coefficients, complete degree-five divergence, and degree-11 carry to the original nonreduced top ideal: 30 variables, 38 rows, Groebner size 59, dimension 10, exactly three minimal primes of dimensions `10,10,8`. From the ideals, the two dimension-10 primes contain the eight derivative-visible degree-six coefficients and not the six Frobenius coefficients; the dimension-8 prime contains the whole degree-seven layer and the six degree-six divergence rows, not all eight derivative-visible coefficients | **CONFIRMED** | a fourth minimal prime; VIS not reducing to 0 on a dim-10 prime; FROB reducing to 0 there; D7 not reducing to 0 on the dim-8 prime; DIV6 failing to reduce to 0 there; killing the six Frobenius coefficients failing to drop the dim-10 branches to dimension 4 |
| 4 | Complete primary decomposition has four components; the fourth is embedded of dimension 6, associated support exactly `U_7=V_7=0` plus the eight derivative-visible degree-six zeros (size 24), primary Groebner size 329, properly thicker than its associated prime. All three minimal primes sit inside that associated prime. The thickening is load-bearing for accepted-digit/Fitting recursion; reduction still covers field-valued points of this gate | **CONFIRMED** | a fifth primary; associated prime unequal to the claimed support; the fourth associated prime coinciding with a minimal prime; primary equal to associated prime; a minimal prime not contained in the embedded prime |
| 5 | Frozen triangular first digit is `(U_0,V_0)=(x^3,x^2 y)` over `F_3`; its degree-`7/6` projection is the origin; the origin reduces to 0 against both top minimal primes, all three layer-76 minimal primes, and all four associated-prime supports. This does not place the full lower-degree point on every eventual component | **CONFIRMED** | `3U` or `3V` not divisible by 3; a nonzero degree-6 or 7 coefficient modulo 3; origin reduction nonzero on any associated prime; an inference that lower-degree layers already lie on every later component |
| 6 | The checkpoint covers only divergence degrees 6/5 and carry degrees 12/11. Inferences about carry 10..7, Cartier, an accepted second digit, full D7 emptiness/nonemptiness, all-depth lifting, characteristic zero, a counterexample, or JC2 are out of scope. Descending through degree 10 while retaining the original primary structure is the smallest honest successor | **CONFIRMED** | `FONLY_(3,7)(D=7)=∅` or `≠∅` asserted; a Cartier or second-digit claim; the successor sold as already computed, or as a reduced-only calculation of the Fitting program |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Replay and hashes

Frozen hashes, recomputed on the charged tree, match the launch prompt, the manifest, and the freeze record:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as-fonly-p3-d7-associated-top-components-20260824.md` | `e50297762088b17e3a01d98e4a76823ec6f33abe02df8b05f50486a3224c30a3` | prompt, freeze `report_sha256` |
| `cases/.../FREEZE.txt` | `c89c9e29aac0be1b7ebfe7042364c2a879876d2c6717cd1ceb93232286a46da6` | prompt |
| `cases/.../MANIFEST.sha256` | `e8e7e7169966848a58cdac9aac7412e5e5e2d2d4f56c521f0b4d7a3a570d6bf9` | prompt, freeze `manifest_sha256` |
| `cases/.../README.md` | `596e8290e56f6050d77d400a129f4f7feaac72bf58b8f88c7a287b4d53b14c1f` | prompt, `MANIFEST` |
| `cases/.../generate_top_gate.py` | `64032b10b8ec0c9fbed4a9e3cd12d314d28b58264f6dcb929bec816d696af411` | prompt, freeze, `MANIFEST` |
| `cases/.../generate_layers76_gate.py` | `2dd77cadc42509b3e2fff62a97642a769d783a8d02e46f1d9ab353602a231973` | prompt, freeze, `MANIFEST` |
| `cases/.../replay_rows_and_incidence.py` | `38ab633076c804f6a60ccc24e8b338cfe303ea5c7c52f11fd44cdf97f646e986` | prompt, freeze, `MANIFEST` |
| triangular-terminal producer | `5325890a505489570a6e02409d64e026560d2635ddf989b865039eeb6ecddccb` | parent |
| triangular-terminal review | `75ff0c8588c633fcf53e17104bf77cdc74fba30bc9c02aa776b23ad0baaa2318` | parent, landed `CONFIRMED` |

Every member hash inside `MANIFEST.sha256` was recomputed from the case directory and matched. The freeze record names the report digest, the manifest digest, and the three program digests; it does not duplicate the README digest, which is in the manifest and the launch prompt. That is freeze bookkeeping, not a mathematical gap.

Registered commands, rerun unmodified from the case directory (`Singular -q` was fed an extra `exit;` by the independent scripts only, without editing any payload):

```text
python3 replay_rows_and_incidence.py
M=7 DO_PRIMARY=1 python3 generate_top_gate.py | Singular -q
TOP=7 LOW=6 DO_PRIMARY=1 python3 generate_layers76_gate.py | Singular -q
shasum -a 256 -c MANIFEST.sha256
```

All three engines exited 0 and the manifest check passed. Live regression counts:

```text
top:     variables 16, equations 20, Gsize 16, dim 4, minAss 2, primary 2 (dims 4,4; sizes 18/22 and 22/22)
layers:  variables 30, equations 38, Gsize 59, dim 10, minAss 3 (dims 10,10,8), primary 4
         last associated prime = all u7_i, v7_i, and the eight VIS zeros
PASS-FONLY-D7-TOP-ROW-PROVENANCE / PASS-TOP-COMPONENTS / PASS-LAYERS76
```

Those Booleans were discarded as evidence for Claims 1–6.

Independent engines, written for this review and not imported from any registered program (scratch SHA-256, outside the repository):

- sparse `F3` emitter with integer product-rule derivatives: `8bc50809370f3f8f2bfc03308b0cdd4c139e571117d69901bd6b032138fff56c`
- triangular first-digit derivation: `ba7b997acdd0d60140d2da8bbde537925257649cbd5c8bb3b8c041480c6f9986`
- affine leftover-quadric census: `c075fb753dbefd3c3960d8b93e210f16fe4d77d6ba8c6b7786b41e8f84e7b9f4`
- random spot-check of every row against literal `det D`: `2d07430957328b488c120a26bc4d873317881926a5d2dea0713bbb00e8dffd28`
- independent top Singular verifier: `9279b6bdae96cfaebfd9a828f83c879bd710e2fcb37eba9b0d10fe8188846ef4`
- independent layer-76 Singular verifier: `cabbe9c38badddd40506932bc0651f8f9f567d50357bd2345ced6130ebe5f48c`
- monomial-order two-sided comparison: `6299c2fec31170fbb6d5e33aaa4b4e1bdbda7ad756b4fde21baae21228fa003b`

A consistency check (not independent evidence) reduced the independently emitted ideals against the producer-generated ideals two-sided: both matched, with Groebner sizes 16 and 59.

---

## Independent recomputation

### 1. Source rows — CONFIRMED

Write `P=x-x^3+3U` and `Q=y+3V` with `U,V` polynomials over `Z`. Then

```text
P_x = 1-3x^2+3 U_x,     P_y = 3 U_y,
Q_x = 3 V_x,            Q_y = 1+3 V_y,
```

and expanding gives the identity over `Z`

```text
det J(P,Q) = 1 + 3(U_x+V_y-x^2) + 9 K,
K          = (U_x-x^2) V_y - U_y V_x
           = det D(U,V) - x^2 V_y.
```

Twelve random integer polynomials of total degree at most seven produced remainder `0`. There is no `27`-term in this expansion. Modulo 9 the identity reduces to `U_x+V_y=x^2`. Modulo 27, after the first-digit residual is absorbed as a degree-at-most-six divergence, the next carry is `K`.

A next digit of total degree at most seven has derivatives of degree at most six, so it can cancel `K` only in degrees `<=6`. Every homogeneous coefficient of `K` in degrees `>6` must vanish before any such next digit exists. This checkpoint treats only degrees 12 and 11.

Degree bounds, independently:

- `deg V<=7` implies `deg V_y<=6`, hence `deg(x^2 V_y)<=8<11`.
- `det D(U_7,V_7)` is homogeneous of degree 12; mixed `det D` of layers 7 and 6 is homogeneous of degree 11.
- A leftover layer of degree `<=5` paired with layer 7 produces `det D` of degree at most `(5-1)+(7-1)=10`, so it cannot enter degrees 12 or 11.

The independently emitted polynomials for `-x^2 V_y` have maximum degree 8 on both the top scheme and the layer-`7/6` scheme. Coefficient-wise comparison of `K` with `det D(U_7+U_6,V_7+V_6)` on every monomial of degrees 12 and 11 is the zero difference.

Variables and nonzero rows from the product-rule emitter, coefficients in `F_3`:

Top scheme, 16 variables `a0..a7,b0..b7` for `U_7=sum a_i x^i y^{7-i}`, `V_7=sum b_i x^i y^{7-i}`. Seven divergence rows of degree 6 and thirteen carry rows of degree 12; all 20 are nonzero as formal polynomials.

```text
[y^6]     a1+b0
[x y^5]   2 a2
[x^2 y^4] 2 b2
[x^3 y^3] a4+b3
[x^4 y^2] 2 a5
[x^5 y]   2 b5
[x^6]     a7+b6
[y^12]    2 a0 b1 + a1 b0
[x y^11]  a0 b2 + 2 a2 b0
[x^2 y^10] 2 a1 b2 + a2 b1
[x^3 y^9] 2 a0 b4 + a1 b3 + 2 a3 b1 + a4 b0
[x^4 y^8] a0 b5 + 2 a2 b3 + a3 b2 + 2 a5 b0
[x^5 y^7] 2 a1 b5 + a2 b4 + 2 a4 b2 + a5 b1
[x^6 y^6] 2 a0 b7 + a1 b6 + 2 a3 b4 + a4 b3 + 2 a6 b1 + a7 b0
[x^7 y^5] 2 a2 b6 + a3 b5 + 2 a5 b3 + a6 b2
[x^8 y^4] a2 b7 + 2 a4 b5 + a5 b4 + 2 a7 b2
[x^9 y^3] 2 a3 b7 + a4 b6 + 2 a6 b4 + a7 b3
[x^10 y^2] 2 a5 b6 + a6 b5
[x^11 y]  a5 b7 + 2 a7 b5
[x^12]    2 a6 b7 + a7 b6
```

Since `2` is a unit in `F_3`, the seven divergence rows are exactly the claimed spine

```text
b5=b2=a5=a2=0,     a7=-b6,     a4=-b3,     a1=-b0.           (4)
```

Layer-`7/6` scheme, 30 variables `u7_0..u7_7,v7_0..v7_7,u6_0..u6_6,v6_0..v6_6`. Thirteen divergence rows (seven of degree 6, six of degree 5) and twenty-five carry rows (thirteen of degree 12, twelve of degree 11); all 38 are nonzero. Degree-five divergence, independently:

```text
[y^5]     u6_1
[x y^4]   2 u6_2 + 2 v6_1
[x^2 y^3] v6_2
[x^3 y^2] u6_4
[x^4 y]   2 u6_5 + 2 v6_4
[x^5]     v6_5
```

The six Frobenius coefficients `u6_0,u6_3,u6_6,v6_0,v6_3,v6_6` (both exponents divisible by three) are absent from every derivative, hence from every divergence row. The eight derivative-visible coefficients are `u6_1,u6_2,u6_4,u6_5,v6_1,v6_2,v6_4,v6_5`. The mixed degree-11 carry rows are the bilinear pairings of layer 7 with layer 6; they are recorded in full in the scratch emitter output. Two hundred random `F_3` evaluations of the twenty top rows and eighty random evaluations of the thirty-eight layer rows matched the literal Jacobian determinant of the reconstructed polynomials, including `K=det D` on degrees 11 and 12. Zero failures.

### 2. Top scheme — CONFIRMED

Independent Singular, ring `F_3[a0..a7,b0..b7]` with `dp`, `option(redSB)`, equations as in Claim 1:

```text
variables 16, nonzero equations 20, reduced Groebner size 16, dimension 4
minAssGTZ count 2, dimensions 4,4, reduced sizes 22,22
origin reduces to 0 on both
spine (4) reduces to 0 on both
the two primes are not equal (two-sided leftover sizes 13 and 7)
radical equals the intersection of the two minAss primes (two-sided)
original ideal is not radical
primdecGTZ count 2
  Q1: dim 4, size 18, associated prime dim 4 size 22, Q1 proper subset of P1, P1 not subset of Q1
      associated prime two-sided equal to minAss[1]
  Q2: dim 4, size 22, associated prime dim 4 size 22, Q2 = P2 = minAss[2]
no embedded associated prime: both associated primes of the primary decomposition are the two minimal primes
```

The two reduced primes, independently:

```text
P1 = < b5, b2, a7+b6, a5, a4+b3, a2, a1+b0,
       b6^2+a6 b7, b4 b6-b3 b7, b3 b6+a3 b7, b1 b6-b0 b7, b0 b6+a0 b7,
       a6 b4-a3 b7, b3^2+a3 b4, b1 b3-b0 b4, b0 b3+a0 b4, a6 b3-a3 b6,
       a6 b1-a0 b7, a3 b1-a0 b4, b0^2+a0 b1, a6 b0-a0 b6, a3 b0-a0 b3 >

P2 = < b5, b2, a7+b6, a5, a4+b3, a2, a1+b0,
       b6^2+a6 b7, b4^2-b1 b7, b3 b4+b1 b6+b0 b7, a6 b4-b3 b6+a3 b7,
       a3 b4+b0 b6, a6 b1+b3^2+b0 b6+a0 b7, a3 b1-b0 b3+a0 b4,
       b0^2+a0 b1, a6 b0+a3 b3+a0 b6, a3^2-a0 a6,
       b1 b4 b6+b1 b3 b7+b0 b4 b7, b0 b4 b6+b0 b3 b7-a0 b4 b7,
       a0 b4 b6-a3 b0 b7, a3 b0 b6+a0 b3 b6-a0 a3 b7,
       a3 b0 b3+a0 b3^2-a0 b0 b6+a0^2 b7 >
```

These are character-for-character the primes printed by the producer replay under the same monomial order. Two-sided reduction is therefore the zero ideal in both directions.

Order and generator-order attack, two-sided comparison of `minAss` lists after mapping back to the `dp` ring: reversed equation order matches; `lp` matches; `Dp` matches. Lex and `Dp` Groebner bases are larger (size 36 for the original ideal; second prime size 30 rather than 22) as expected for those orders; the ideals are the same. Reversed variable order rewrites the spine as `b0+a1`, `b3+a4`, `b6+a7` and keeps two dimension-four primes of size 22. `primdecSY` returns the same primary count, dimensions, and sizes 18/22 and 22/22.

Second reconstruction after substituting the spine. The leftover coordinates are nine variables `(a0,a3,a6,b0,b1,b3,b4,b6,b7)`. After the spine one has `U_x=2 V_y` in `F_3`, and `det D` is supported on the Veronese monomials `y^{12},x^3 y^9,x^6 y^6,x^9 y^3,x^{12}` with the five quadrics

```text
b0^2 + a0 b1,
b0 b3 - a0 b4 - a3 b1,
-b3^2 + b0 b6 - a0 b7 - a3 b4 - a6 b1,
b3 b6 - a3 b7 - a6 b4,
2 b6^2 - a6 b7.
```

An exhaustive census of `F_3^9` finds 153 zeros. The displayed primes, rewritten in leftover coordinates, contain 105 and 81 of those points with intersection 33 and union 153: no leftover `F_3`-point, and `105+81-33=153`. This is a point-set confirmation over `F_3`, not a replacement for `minAss` in `F_3[a,b]`.

### 3. Layer-76 scheme — CONFIRMED

Independent Singular, 30 variables, 38 independently emitted rows, `dp`:

```text
variables 30, nonzero equations 38, reduced Groebner size 59, dimension 10
minAssGTZ count 3, dimensions 10, 10, 8, reduced sizes 30, 30, 22
original ideal is not radical
```

Ideal-theoretic tests, not prose, on the three reduced primes. Write

```text
D7   = (u7_0,...,u7_7, v7_0,...,v7_7),
VIS  = (u6_1,u6_2,u6_4,u6_5, v6_1,v6_2,v6_4,v6_5),
FROB = (u6_0,u6_3,u6_6, v6_0,v6_3,v6_6),
DIV6 = (u6_1, 2 u6_2+2 v6_1, v6_2, u6_4, 2 u6_5+2 v6_4, v6_5).
```

| Test | minAss 1 (dim 10) | minAss 2 (dim 10) | minAss 3 (dim 8) |
|---|---|---|---|
| `reduce(D7, C)` size | 12 (not 0) | 12 (not 0) | 0 |
| `reduce(VIS, C)` | 0 | 0 | size 4 (not 0) |
| `reduce(FROB, C)` size | 6 (not 0) | 6 (not 0) | 6 (not 0) |
| `reduce(DIV6, C)` | 0 | 0 | 0 |
| `dim(C+FROB)` | 4 | 4 | 2 |
| `dim(C+VIS)` | 10 | 10 | 6 |
| `dim(C+D7)` | 6 | 6 | 8 |
| origin on `C` | yes | yes | yes |

The two dimension-ten primes therefore contain every derivative-visible degree-six coefficient and none of the six Frobenius coefficients; killing the Frobenius coefficients drops dimension by exactly six, from 10 to 4, so those six are free. Their degree-seven generators are exactly the two top primes of Claim 2, rewritten in `u7_i,v7_i`, together with the eight VIS zeros (size `22+8=30`).

The dimension-eight prime contains the entire degree-seven layer. Its remaining generators are exactly `DIV6`:

```text
v6_5, v6_2, u6_5+v6_4, u6_4, u6_2+v6_1, u6_1
```

together with `u7_i=v7_i=0`. That is the complete divergence-free degree-six layer: six independent conditions on fourteen coefficients, dimension `30-16-6=8`. Four of the eight VIS coefficients remain (the mixed pairs `u6_2+v6_1=0` and `u6_5+v6_4=0`); killing all of VIS drops this branch to dimension 6.

Reversed generator order returns the same count, dimensions, and sizes `30,30,22`.

### 4. Embedded component — CONFIRMED

Independent `primdecGTZ` of the original nonreduced layer ideal:

| Primary | dim | primary GB size | associated dim | associated GB size | equals associated prime? | associated is minimal? | origin |
|---|---|---|---|---|---|---|---|
| 1 | 10 | 26 | 10 | 30 | no; `Q1 subset P1` proper | yes (minAss 1) | yes |
| 2 | 10 | 30 | 10 | 30 | yes | yes (minAss 2) | yes |
| 3 | 8 | 22 | 8 | 22 | yes | yes (minAss 3) | yes |
| 4 | 6 | 329 | 6 | 24 | no; `Q4 subset P4` proper | **no** | yes |

The fourth associated prime is

```text
< v6_5, v6_4, v6_2, v6_1, u6_5, u6_4, u6_2, u6_1,
  v7_7,...,v7_0, u7_7,...,u7_0 >.
```

Two-sided reduction against the claimed support `(5)` — all sixteen degree-seven coefficients together with the eight VIS coefficients — is zero in both directions. So the associated support is exactly zero degree-seven layer plus the six degree-six Frobenius coefficients as free coordinates, dimension 6.

Containments: each of the three minimal primes reduces to 0 against this associated prime, so

```text
V(P_embedded) ⊂ V(minAss 1) ∩ V(minAss 2) ∩ V(minAss 3).
```

The associated prime is strictly larger than its primary (size 24 versus 329; `P4` does not reduce to 0 against `Q4`). That is a genuine nilpotent thickening, not a duplicate of a minimal prime.

When the thickening is load-bearing, and when it is not. Every field-valued point of the embedded component already lies on all three minimal components, because the supports nest. For enumerating `F_3bar`-points of this gate, passing to the radical (or to the three minimal primes) still covers the same set; the origin, in particular, is already on every minimal prime. The thickening is load-bearing as soon as a later gate reads scheme structure rather than support: accepted-digit Fitting ranks, Jacobian Fitting ideals of the carry map, and any recursion that consumes the original nonreduced ideal or a primary component rather than its radical. The displayed primary `Q4` of Groebner size 329 is that nonreduced object. Throwing it away would not lose a field point of the present gate, but it would discard the infinitesimal data that the successor's Fitting/accepted-digit computation is licensed to use at the triangular origin.

### 5. Incidence — CONFIRMED

The confirmed triangular residue is the integer pair

```text
P = x + 2 x^3 + 441 x^5 + 108 x^7,
Q = y - 6 x^2 y + 18 x^4 y - 27 x^6 y.
```

Then `P-(x-x^3)=3x^3+441 x^5+108 x^7`, so `U=x^3+147 x^5+36 x^7`, and `Q-y=y(-6x^2+18x^4-27x^6)`, so `V=-2 x^2 y+6 x^4 y-9 x^6 y`. Reducing modulo 3 uses `147≡0`, `36≡0`, `-2≡1`, `6≡0`, `-9≡0`, hence

```text
U ≡ x^3,     V ≡ x^2 y     (mod 3).
```

Every degree-six or degree-seven coefficient vanishes modulo 3, so the projection of this first digit onto the present gate is the origin of `A^{16}` and of `A^{30}`. Independent `reduce` of every minimal and associated prime against the maximal ideal of all coordinates returns the zero ideal: the origin lies on both top minimal primes, all three layer-`7/6` minimal primes, and all four associated-prime supports, including `(5)`.

This is why a reduced generic-component calculation would not faithfully describe the triangular point's later *scheme-theoretic* lift space. It does not say that the degree-five and lower layers of the same point lie on every eventual component: those coordinates are not in this ring, and carry rows 10 through 7 and the Cartier row have not been attached.

### 6. Scope and recurrence — CONFIRMED

The exact object is the associated scheme of divergence degrees 6/5 and carry degrees 12/11. The independently reconstructed recurrence is the one the producer wrote:

```text
nonzero degree-7 derivative layer
    -> one of two four-dimensional top types
    -> degree-6 follower is derivative-zero Frobenius;

rank-zero degree-7 layer
    -> retain the full degree-6 divergence-free problem;

their intersection
    -> retain the embedded Frobenius-supported primary thickening.
```

Nothing in the ideals, the degree bounds, or the triangular incidence decides carry rows 10, 9, 8, or 7; the bounded Cartier coefficient `[x^2 y^2]K`; existence of a second accepted digit; emptiness or nonemptiness of the complete `D=7` next-depth system; all-depth lifting; characteristic zero; a counterexample; or JC2. Minimal primes navigate; the original nonreduced ideal is the object that subsequent carry and Fitting gates consume.

The next homogeneous obstruction is carry degree 10, which is the first degree at which a degree-five layer can appear (`(5-1)+(7-1)=10`). Attaching that layer globally is the 42-variable calculation the producer declines. Descending componentwise through degree 10 while keeping the four primary components, including `(5)`, is the smallest exact continuation that does not drop either a reduced branch or the load-bearing thickening. A radical-only successor would still see every field-valued point of *this* gate and would be dishonest for the Fitting program the checkpoint is written to serve.

---

## Non-blocking remarks

- The producer row-replay asserts counts and the degree bound `2+(7-1)=8<11`; it does not list coefficients. The lists in Claim 1 are from the independent emitter.
- `generate_top_gate.py` prints `vdim` of positive-dimensional primes, which Singular reports as `-1`. That print is unused by any numbered claim.
- The markdown report does not paste the two top primes; the portable Singular replay does. This review treats those printed primes as the displayed ones and re-derives them.
- The freeze file omits the README digest, which is in the manifest. Bookkeeping only.

None of these remarks is a `GAP` or a `REFUTED`.
