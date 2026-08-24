# Hostile different-model review — AS gauge growth at p=3 through depth four

| Field | Value |
|---|---|
| Claim under review | Frozen producer: for the equal-cap systems `B_(3,n)(D,D)` on total-degree simplices, the exact minimum total-degree caps at depths `n=2,3,4` are `3,5,7`; no depth-four survivor occurs below seven; the proposed slope `(n-1)(p-1)+1` survives this finite test only |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking imprecisions below; the formula at `n>=5`, a polynomial lift, `p=109`, `A_infinity`, and JC2 are correctly *not* claimed) |
| Evidence tier | independent coordinate comparison and Hensel uniqueness on the identity branch; commuting-variable polynomial identities for the mod-81 expansions; generic-simplex coefficient extraction and a second integer sparse engine (forward and reversed-column Gauss over `F_3`); exact 81-assignment integer composition of the top slots; unmodified rerun of both registered programs as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `1e4480c14f2ab9c4145eb6f6c74f0ac348baf76a` (matches the charged bank) |
| Review window (UTC) | 2026-08-24T14:57:21Z – 2026-08-24T15:08:10Z |
| Python | uv-pinned CPython 3.11.11 + SymPy `1.14.0` (registered replay and independent reconstruction); host CPython 3.14.6 for hashing |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, freeze, and named bounded-polar-conductor parent reread in full before any verdict:

- `xmodel/as-gauge-growth-p3-depth4-gate-20260824.md` (SHA-256 `bfacd9a475f8e2aa7da9d26e43785b80ff3eadd53615e4823dfe6d52fc6fd660`)
- `cases/as_gauge_growth_p3_depth4_20260824/PREREGISTRATION.md` (SHA-256 `65a36738032e003185f48539b1c571b754bbbec2868629893c840cfae3eceefd`)
- `cases/as_gauge_growth_p3_depth4_20260824/replay.py` (SHA-256 `db6ffc06efcdcc1f3a3619ff73e5d2c243f662ada9a5371394346c9922e93ed7`)
- `cases/as_gauge_growth_p3_depth4_20260824/replay.stdout.txt` (SHA-256 `088cb5546e36968c2e1fb0cd6917b948a45f50b7fefe837a1dbc978873462b7e`)
- `cases/as_gauge_growth_p3_depth4_20260824/independent_check.py` (SHA-256 `2fc1e60f827237d37b91b164a653de5b294aa97d0a48ec5d3aa9d4a3da166d6d`)
- `cases/as_gauge_growth_p3_depth4_20260824/independent_check.stdout.txt` (SHA-256 `10717a107b69ae9b961b86af520a3cc8467ed81780e7271e39d73897639ecc26`)
- `cases/as_gauge_growth_p3_depth4_20260824/MANIFEST.sha256` (SHA-256 `b57bfe29136fe334fef3a53fa53efa4d7ff03607036a0357c71f2b0328d6a380`)
- `cases/as_gauge_growth_p3_depth4_20260824/FREEZE.sha256` (SHA-256 `7805a82e0c8113953cbc203ec7be134fd4aaed83cc81a095f313b86dd3b79fbb`)

Frozen polar-conductor parent, consumed only at its reviewed bounded-category scope:

- `xmodel/as109-bounded-polar-conductor-gate-20260824.md` (SHA-256 `2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b`)
- `xmodel/as109-bounded-polar-conductor-review-grok-20260824.md` (SHA-256 `bda4dda7d24d36bf75b6c55b566f708ee300c80aeb3344c4bb724bfc7e7787fa`), overall **CONFIRMED**
- `cases/as109_bounded_polar_conductor_20260824/FREEZE.sha256` (SHA-256 `aa07a878b41adfbe9e07beaa48aa793562fb49228ffae8982aa8773f600df4e2`)

The committed basis is exactly `1e4480c14f2ab9c4145eb6f6c74f0ac348baf76a`. Named producer artifacts remain uncommitted on top of that basis. No producer, case, canonical, ladder, notes, prompt, log, or run file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp` and did not import `replay.py` or `independent_check.py`. The included same-model checker is a negative control, not this review.

Tried hard, and failed, to cancel `x^6 y` by a leftover same-degree monomial of `c,d,e,f`, to let the homogeneous degree-nine part of `-x a^2` rescue `a_3` before the degree-twelve cube is killed, to produce an `[x^4]` first-divergence carry that would make `L1/3` representative-dependent, to break `K=-U` over `F_3` by a `b_{[x^2 y^2]}` or `a_{[y^2]}` slot, to make the depth-three affine systems consistent at `D=3,4` under reversed-column Gauss, and to promote the three exact minima into a growth law, a no-lift theorem, or JC2.

---

## Promotion

**Accept `EXACT EQUAL-CAP MINIMA 3,5,7 AT p=3 THROUGH DEPTH FOUR; THE COTANGENT-SLOPE LAW SURVIVES THIS FINITE TEST ONLY`.**

On total-degree simplices, for the frozen equal-cap systems `B_(3,n)(D,D)`:

- Gauge elimination from the confirmed orientation `C_p ∘ Φ_F = F` is `A-A^p=P` and `B=Q(1-p A^{p-1})`. Hensel uniqueness holds on the identity branch because `1-p T^{p-1}` is a unit there. The finite `F`-only formulation retains both the map cap and the canonical-gauge cap; the load-bearing computations reintroduce `A,B` only as those canonical digits.
- The unique gauge modulo 81 expands as the displayed formulas `(5)--(7)`, including every `a^2`, `a^3`, `ab`, mixed-bracket, and divided-divergence carry. These are polynomial congruences, not sample checks.
- Depth two has exact minimum three: every `F` reduces to `(x-x^3,y)`, and the identity gauge realises cap three.
- Depth three is empty at `D=3,4` by an affine first-digit certificate of ranks `15/16` and `21/22`, equivalently by the unit row `[x^4 y]=b_{[x^2 y]}-[x^3]a+1=1` after the cap and divergence constraints, and is nonempty at `D=5` by the cotangent truncation. Exact minimum five.
- Depth four is empty at `D=5,6` by an `F_3` unit certificate `(Q row)-(det row)-b_{[x^2 y]}=1` after the forced bounds `deg a<=2`, `deg b<=D-2`, `c_{[x^5]}=b_{[x^2 y]}=0`, with `[x^4]L1=0` over `Z`. The identity gauge realises cap seven. Exact minimum seven.

**Do not promote this to:** the formula `(n-1)(p-1)+1` at `n>=5` or for a general odd prime; a positive asymptotic rate for `κ_n`; existence or nonexistence of an all-depth polynomial lift; a `p=109` computation; identification of the exterior polar divisor with `A_infinity`; a counterexample to JC; or any JC2 inference.

**Smallest honest successor.** An exact depth-five equal-cap discriminator for `B_(3,5)(D,D)` at `D=7,8` (survival expected at `D=9` if the slope continues) is the smallest computational successor. An inductive highest-carry / unit-certificate lemma, forcing the top cotangent monomial `x^{2(n-1)} y` in the `p^{n-1}` digit to remain a unit under the equal cap, is the smallest successor that would actually promote the slope law. Neither is licensed by this finite gate.

---

## Quarantine

No result here proves or disproves JC2, constructs or excludes a polynomial lift of `(x-x^p,y)`, identifies the polar divisor with `A_infinity`, runs `p=109`, or proves the slope at depth five. Producer strings `PASS-AS-GAUGE-GROWTH-P3-DEPTH4` and `PASS-INDEPENDENT-AS-GROWTH-HOSTILE-CHECK` were not used as evidence; the elimination, the mod-81 expansions, the depth-three ranks, the forced degree bounds, the unit certificate, and the cotangent identities were re-derived. The polar-conductor parent is used only for the orientation `C_p ∘ Φ_F=F`, the systems `B_(p,n)(D,D)` on total-degree simplices, and the cotangent positive control, at the reviewed scope that every fixed cap dies at some finite depth. That parent does not supply a growth rate. Independent reconstruction, not the producer scripts, is the evidence for every numbered claim.

---

## Scope (not enlarged)

One prime `p=3`; equal total-degree caps; Witt depths two through four; exact coefficient ring `Z/3^n` with canonical digits on total-degree simplices. The depth-seven survivor is the truncated cotangent map, not a lift to all depths. No rectangular support, no enumerator, no AWS, and no modular-to-characteristic-zero existence inference are in scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | From `C_p=(T-T^p, y/D)` and `C_p ∘ Φ_F=F` one has `A-A^p=P` and `B=Q(1-p A^{p-1})`. Identity-branch Hensel uniqueness. `det J(A, Q D(A))=det J(P,Q)`. Finite `F`-only points retain both map and canonical-gauge caps | **CONFIRMED** | reverse orientation; a second identity-residue root; `det` identity failing by a leftover `Q D'(A) dA` term; eliminating the gauge and then dropping its cap |
| 2 | Universal expansions `(5)--(7)` modulo 81, including `a^2`, `a^3`, `ab`, mixed brackets `{a,d}+{c,b}`, and the divided-divergence slots in `L1,L2,L3` | **CONFIRMED** | a remainder not divisible by 81; an omitted 27-digit monomial that reaches `x^6 y`; a missing `27 a_x d_y` or `9 a_x b_y` term in the Jacobian |
| 3 | Depth two has exact minimum three. Depth three is empty at `D=3,4` (ranks `15/16`, `21/22`) and nonempty at `D=5` (rank `28/28` plus the cotangent witness). After the cap/divergence constraints the 9-digit of `x^4 y` is `b_{[x^2 y]}-[x^3]a+1=1` | **CONFIRMED** | a consistent augmented system at `D=3` or `4` under reversed-column Gauss; a quadratic 9-digit remainder not divisible by 27; cotangent degree not equal to `2n-1` |
| 4 | Forced bounds `deg a<=2` by the first-coordinate cap plus injective cubing over `F_3`, in that order; `deg b<=3` at `D=5` and `<=4` at `D=6`; `c_{[x^5]}=0` from the `x^7` slot; `b_{[x^2 y]}=0` from `[x^2]L1`. No cancellation from `c,d,e,f` or an omitted same-degree monomial | **CONFIRMED** | using the degree-nine part before killing `a_4`, where `-x a_4^2` appears; a degree-seven `a`-term surviving `deg a<=2`; `x^2 b` not the unique over-cap source in the 9-digit of `Q` |
| 5 | `U=[x^5 y](ab)`, `K=[x^4]{a,b}`, `K=-U` in `F_3`. At `D=5` the displayed top `b`-slots are absent and the identity is `0=0`. `[x^4]L1=0` over `Z`. The combination `(Q row)-(det row)-b_{[x^2 y]}` equals `1+6 a_{[xy]} b_{[x^4]}-3 c_{[x^5]}` over `Z` and `1` in `F_3` at both `D=5` and `D=6`. Every one of 81 top tuples leaves the `x^6 y` coefficient equal to `27` modulo 81 | **CONFIRMED** | a representative-dependent `L1/3` at `x^4`; an integer identity claimed as `1` rather than `1` in `F_3`; a top tuple with `x^6 y ̸≡ 27 (mod 81)` after the determinant row; illegal division by 3 |
| 6 | The truncated cotangent map at `D=7` has determinant one modulo 81, exact second-coordinate degree seven, and identity-gauge degree one. The three exact minima are therefore `3,5,7` | **CONFIRMED** | `27 x^6 y ≡ 0 (mod 81)`; `det J(C_(3,4)) ̸≡ 1 (mod 81)`; a depth-four point of cap `<=6` |
| 7 | Nothing here proves the formula at `n>=5`, a `p=109` statement, nonexistence of an unbounded polynomial lift, identification of `A_infinity`, a counterexample, or JC2. The smallest honest successor is an exact `n=5` discriminator, or, to promote the slope, an inductive highest-carry / unit-certificate lemma | **CONFIRMED** | a hidden `n>=5` claim; `κ_n → ∞` sold as a rate; a no-lift or JC2 sentence |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Replay and hashes

Frozen hashes, recomputed on the charged tree, match the launch prompt, `MANIFEST.sha256`, and `FREEZE.sha256`:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as-gauge-growth-p3-depth4-gate-20260824.md` | `bfacd9a475f8e2aa7da9d26e43785b80ff3eadd53615e4823dfe6d52fc6fd660` | prompt, `MANIFEST`, `FREEZE` |
| `cases/as_gauge_growth_p3_depth4_20260824/PREREGISTRATION.md` | `65a36738032e003185f48539b1c571b754bbbec2868629893c840cfae3eceefd` | prompt, `MANIFEST`, `FREEZE` |
| `cases/as_gauge_growth_p3_depth4_20260824/replay.py` | `db6ffc06efcdcc1f3a3619ff73e5d2c243f662ada9a5371394346c9922e93ed7` | prompt, `MANIFEST`, `FREEZE` |
| `cases/as_gauge_growth_p3_depth4_20260824/replay.stdout.txt` | `088cb5546e36968c2e1fb0cd6917b948a45f50b7fefe837a1dbc978873462b7e` | prompt, `MANIFEST`, `FREEZE` |
| `cases/as_gauge_growth_p3_depth4_20260824/independent_check.py` | `2fc1e60f827237d37b91b164a653de5b294aa97d0a48ec5d3aa9d4a3da166d6d` | prompt, `MANIFEST`, `FREEZE` |
| `cases/as_gauge_growth_p3_depth4_20260824/independent_check.stdout.txt` | `10717a107b69ae9b961b86af520a3cc8467ed81780e7271e39d73897639ecc26` | prompt, `MANIFEST`, `FREEZE` |
| `cases/as_gauge_growth_p3_depth4_20260824/MANIFEST.sha256` | `b57bfe29136fe334fef3a53fa53efa4d7ff03607036a0357c71f2b0328d6a380` | prompt, `FREEZE` (listed as a member) |
| `cases/as_gauge_growth_p3_depth4_20260824/FREEZE.sha256` | `7805a82e0c8113953cbc203ec7be134fd4aaed83cc81a095f313b86dd3b79fbb` | prompt (self-hash) |
| `xmodel/as109-bounded-polar-conductor-gate-20260824.md` | `2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b` | producer named input |
| `xmodel/as109-bounded-polar-conductor-review-grok-20260824.md` | `bda4dda7d24d36bf75b6c55b566f708ee300c80aeb3344c4bb724bfc7e7787fa` | producer named input |
| `cases/as109_bounded_polar_conductor_20260824/FREEZE.sha256` | `aa07a878b41adfbe9e07beaa48aa793562fb49228ffae8982aa8773f600df4e2` | producer named input |

Every member hash inside `FREEZE.sha256` was recomputed from the repository root and matched. `FREEZE.sha256` is `MANIFEST.sha256` plus the extra line hashing `MANIFEST.sha256` itself; the two files are not byte-identical, and should not be.

Registered commands, rerun unmodified from the charged tree with `uv run --offline --no-project --with sympy==1.14.0`:

```text
python cases/as_gauge_growth_p3_depth4_20260824/replay.py
python cases/as_gauge_growth_p3_depth4_20260824/independent_check.py
```

Both exited 0. Stdout SHA-256 values `088cb5546e36968c2e1fb0cd6917b948a45f50b7fefe837a1dbc978873462b7e` and `10717a107b69ae9b961b86af520a3cc8467ed81780e7271e39d73897639ecc26` are byte-identical to the frozen files. Markers `PASS-AS-GAUGE-GROWTH-P3-DEPTH4` and `PASS-INDEPENDENT-AS-GROWTH-HOSTILE-CHECK` are present, with `q_values=[1]`, distinct effective counts `9` and `81`, and all registered refusal markers. Those Booleans were discarded as evidence for Claims 1–7.

A second engine, written for this review and not imported from either registered script, used integer sparse polynomials and SymPy generic simplices, with both forward and reversed-column Gauss over `F_3`. Scratch engine SHA-256 `e5f668ea448a31bc2a5e953be9be779a7736d7b09bb9783c59a6deeff82b773e` (outside the repository; not a freeze input). Forward and reversed-column ranks agreed in every depth-three case.

---

## Independent recomputation

### 1. Gauge elimination and finite-system equivalence — CONFIRMED

Write `g(T)=T-T^p`, `D(T)=1-p T^{p-1}`, `C_p=(g, y/D)`. The frozen orientation is `C_p ∘ Φ_F = F` with `Φ_F=(A,B)` on the identity branch. Coordinate comparison is tautological:

```text
A - A^p = P,             B / D(A) = Q,
```

hence `B = Q D(A) = Q(1-p A^{p-1})`. Conversely `C_p(A, Q D(A)) = (P,Q)` exactly in the Tate algebra. Reverse composition is not this statement.

Hensel. Put `f(T)=T-T^p-P`. On the identity branch `P ≡ x-x^p (mod p)`, so `f(x) ≡ 0 (mod p)` and

```text
f'(T) = 1 - p T^{p-1}.
```

At `T ≡ x` this is a unit (`≡ 1 (mod p)`). The residue equation `(T-x)-(T-x)^p=0` has the extra solutions `(T-x)^{p-1}=1`, which are not the identity branch. Unique lift of `T ≡ x` modulo `p^n` follows. `B` is then forced.

Determinant. `dP = D(A)\, dA`. For `B = Q D(A)`,

```text
dB = D(A)\, dQ + Q D'(A)\, dA,
```

and the extra term wedges with `dA` to zero, so

```text
det J(A, Q D(A)) = D(A) det(dA, dQ) = det J(P,Q).
```

The remainder of this identity, as a polynomial in the first partials, is identically zero.

Finite depth. `S_(p,n)(T)=∑_{j<n} p^j T^{j(p-1)}` satisfies `D S_n = 1-p^n T^{n(p-1)}` as a polynomial identity; independently checked at `p=3` through `n=6`. Thus `B S_n(A) ≡ Q (mod p^n)` whenever `B = Q D(A)`. The original system `B_(3,n)(D,D)` caps both `deg(C_(3,n) ∘ Φ)` and `deg Φ`. After unique reconstruction of `Φ` from `F`, dropping the last two inequalities of the producer's `(3)` would define a different system: an `F` of cap `D` whose canonical gauge exceeds `D`. The coefficient proof never does that. Digits `a,c,e` and `b,d,f` are canonical coordinates of that unique gauge, not independent search variables.

Non-blocking. The `F`-only language uses the exact polynomial `Q D(A_n)` as the gauge representative; the load-bearing rows are the composition `C_(3,n) ∘ (A,B)` with canonical digits. Those are equivalent modulo `p^n` on the identity branch.

### 2. Universal depth-four carries — CONFIRMED

Write `A=x+3a+9c+27e` and `B=y+3b+9d+27f` as polynomials in eight commuting variables. Direct expansion modulo 81:

```text
A^3 ≡ x^3 + 9 x^2 a + 27 x^2 c + 27 x a^2 + 27 a^3,
```

because `27 u^3 ≡ 27 a^3` and `27 x u^2 ≡ 27 x a^2` once `u=a+3c+9e`. This is `(5)`. For the second coordinate, `S_4(A)=1+3A^2+9A^4+27A^6` expands to the displayed 3, 9, and 27 digits of `(6)`, including `2xab` from the carry `9 · (6xa) · b = 54 xab ≡ 27 · (2xab)` and `x^3 a y` from `9 A^4 y` (`108 x^3 a ≡ 27 x^3 a`). The Jacobian with generic first partials is exactly `(7)`: no `81`-term survives, and the mixed brackets `{a,d}+{c,b}` are the only 27-digit bilinear sources besides `e_x+f_y`.

These three congruences were checked as polynomial identities: every coefficient of `A-A^3` minus `(5)`, of `B S_4(A)` minus `(6)`, and of `det J(A,B)` minus `(7)`, is divisible by 81. The remainder support of the second-coordinate identity is empty. Forty independent random integer-digit trials, with the same formulas reconstructed from sparse composition rather than from the commuting-variable expansion, all agreed modulo 81.

### 3. Depths two and three — CONFIRMED

Depth two. Reduction of any such `F` is `(x-x^3,y)`, so `deg P >= 3` and no equal cap `D<3` exists. The identity gauge gives `C_(3,2)=(x-x^3, y(1+3x^2))` modulo 9, of degree three, with

```text
(1-3x^2)(1+3x^2)=1-9x^4 ≡ 1 (mod 9).
```

Exact minimum three.

Depth three, small unit row. Modulo 27 only the first digits enter the over-cap rows. The first-coordinate 9-digit `c-x^2 a` forces `deg a <= D-2`. For `D<=4` this is `deg a <= 2`, so `a_{[x^3]}=0`. Independently, `[x^2](a_x)` over `F_3` cannot see `a_{[x^3]}` anyway, because `∂_x(x^3)=3x^2`. After `deg a<=2` one has `[x^2]L1 = b_{[x^2 y]}` exactly over `Z`. The 9-digit of `B S_3(A)` is `d + x^2 b + 2 x a y + x^4 y` over `Z`; the coefficient of `x^4 y` is `9(b_{[x^2 y]} + 1)` once `deg a<=2` and `deg d<=D<=4`. Linear terms not divisible by 9: none. Quadratic terms not divisible by 27: none. After `b_{[x^2 y]}=0` the 9-digit is `1` in `F_3`. Over `F_3` one has `2=-1`, which is the producer's display `[x^2 y]b-[x^3]a+1`.

Non-blocking presentation: the producer attributes both `a_{[x^3]}=0` and `b_{[x^2 y]}=0` to the `x^2` coefficient of `L1`. The first vanishing is the degree bound `(11)` at depth three, not the divergence row. The rows used in the contradiction are nevertheless correct.

Full affine systems, rebuilt from exact integer composition `A=x+3a`, `B=y+3b` (higher digits cannot cancel degree `>D`), with both column orders:

| `D` | variables | rows | coefficient rank | augmented rank | reversed-column | verdict |
|---:|---:|---:|---:|---:|---|---|
| 3 | 20 | 62 | 15 | 16 | agrees | empty |
| 4 | 30 | 89 | 21 | 22 | agrees | empty |
| 5 | 42 | 117 | 28 | 28 | agrees | first digit consistent |

The frozen cap-three 12/13 control of the polar-conductor parent is a proper subsystem (tautological high-`a` rows, divergence, and one forbidden monomial). The full over-cap system is strictly stronger and still empty at `D=3,4`. At `D=5` first-digit consistency is not itself an existence proof; the cotangent truncation `C_(3,3)=(x-x^3, y(1+3x^2+9x^4))` modulo 27 is, of degree five, determinant one. Exact minimum five.

### 4. Depth-four forced degrees — CONFIRMED

`D<=4` is already empty by reduction to depth three. It remains to kill `D=5,6`.

First-coordinate 9-digit forces `deg a <= D-2`. The 27-digit is `e - x^2 c - x a^2 - a^3`. Over `F_3`, cubing is the Frobenius endomorphism: homogeneous degree `3k` of `a^3` is exactly `a_k^3`, and `a_k ↦ a_k^3` is injective on the monomial basis because the images `x^{3i} y^{3j}` are distinct and `c^3=0` implies `c=0` in `F_3`.

Order is essential. Before killing `a_4` at `D=6`, the homogeneous degree-nine part of the 27-digit still contains `-x a_4^2` (coefficient `-a_{4,0}^2` at `x^9`, among others). Using degree nine first would not force `a_3=0`. Degree twelve is the pure cube `-a_4^3` over `Z` (so also over `F_3`); after that vanishing, degree nine is the pure cube `-a_3^3`. At `D=5` there is no `a_4` and degree nine is immediately `-a_3^3`. In both cases `deg a <= 2`. Cubing does *not* kill `a_2`: at degree six the term `-a_2^3` can be cancelled by `-x^2 c_4` or, at `D=6`, by `e_6`.

With `deg a<=2`, the over-cap of the 9-digit of `Q` is exactly `x^2` times the part of `b` of degree `> D-2`. The summands `2 x a y` and `x^4 y` have degree at most 5 and lie inside both caps. Thus `deg b <= 3` at `D=5` and `deg b <= 4` at `D=6`.

The `x^7` coefficient of the 27-digit of `P`, after `deg a<=2`, is exactly `-c_{[x^5]}`. Every other degree-seven monomial of that digit is likewise `-c` of a degree-five source; `e` cannot reach degree 7 under either cap, and `a^2`, `a^3` cannot reach degree 7. In particular `c_{[x^5]}=0`. (Other `c` coefficients of degree 5 are not needed for the unit row.)

Finally `[x^2]L1 = b_{[x^2 y]}` after `deg a<=2`, so `b_{[x^2 y]}=0`. The producer writes `a_{[x^3]}=0` here as well; that coefficient is already absent from `deg a<=2`.

No omitted same-degree monomial reverses these bounds. Digits `e,f` live on the simplex of radius `D` and cannot touch `x^6 y` (degree 7). Digit `d` of degree `<=D` cannot cancel the over-cap of `x^2 b`.

### 5. Unit certificate — CONFIRMED

After the bounds of Claim 4, the only products that can make `x^5 y` in `ab` or `x^4` in `{a,b}` are the displayed top slots:

```text
U = a_{[x^2]} b_{[x^3 y]} + a_{[xy]} b_{[x^4]},
K = 2 a_{[x^2]} b_{[x^3 y]} - 4 a_{[xy]} b_{[x^4]}.
```

Generic-simplex extraction, including the extra slots `a_{[y^2]}`, `b_{[x^2 y^2]}`, and all lower terms, produces exactly these two expressions and no others. Over `Z`,

```text
K + U = 3(a_{[x^2]} b_{[x^3 y]} - a_{[xy]} b_{[x^4]}),
2U - K = 6 a_{[xy]} b_{[x^4]}.
```

Hence `K ≡ -U` in `F_3`. At `D=5` both displayed `b`-slots have degree 4, which is outside `deg b<=3`; they are absent, `U=K=0`, and the identity holds as `0=0`. At `D=6` they are the only possible top coefficients.

The coefficient of `x^4` in `L1` is identically zero over `Z`: it would require `x^5` in `a` or `x^4 y` in `b`. There is no divided carry `L1/3` at this monomial and no representative dependence. The `x^4` coefficient of determinant one modulo 27 is therefore the 9-digit

```text
5 c_{[x^5]} + d_{[x^4 y]} + K = 0   in F_3.
```

The 27-digit of `B S_4(A)` at `x^6 y`, from the independently verified formula `(6)` and from generic extraction after the forced bounds, is

```text
d_{[x^4 y]} + 2U + b_{[x^2 y]} + 2 c_{[x^5]} + 1.
```

The combination named in the gate is an identity over `Z` before any `F_3` reduction:

```text
(Q row) - (det row) - b_{[x^2 y]}
  = 2U - K - 3 c_{[x^5]} + 1
  = 1 + 6 a_{[xy]} b_{[x^4]} - 3 c_{[x^5]}.
```

In `F_3` this is `1`, at both `D=5` and `D=6`. No division is performed. The `c_{[x^5]}` terms cancel modulo 3, so the cap row `c_{[x^5]}=0` is not a hidden necessity of the contradiction; it is an independently forced row. The leftover `6 a_{[xy]} b_{[x^4]}` is the integer content of `2U-K` and is not claimed to vanish over `Z`.

Consequently the coefficient of `x^6 y` in `B S_4(A)` is `27` times a unit modulo 81, for every point of the necessary subsystem. Digits `e,f` cannot reach that monomial under either cap.

Negative control, independent of the same-model script: all 81 assignments of the four displayed top slots, with `d_{[x^4 y]}` solved from the integer bracket so that the determinant 9-digit vanishes in `F_3`, and with every other digit zero, produce `x^6 y ≡ 27 (mod 81)`. At `D=5` the two `b`-slots are absent, so these are nine distinct effective assignments; at `D=6` all 81 are distinct. Random forced-degree samples with the determinant row imposed, including nonzero lower digits of `c,d,e,f`, likewise all give `27`. Without the determinant row at `D=6` the values `{0,27,54}` all occur, as they must.

### 6. Positive depth-four control and exact minima — CONFIRMED

The identity gauge at depth four is

```text
C_(3,4) = (x-x^3, y(1+3x^2+9x^4+27x^6))  (mod 81).
```

The finite geometric series gives `(1-3x^2) S_4(x) = 1-81 x^8 ≡ 1 (mod 81)`, so the Jacobian is one. The second coordinate has exact degree seven because the coefficient of `x^6 y` is `27 ̸≡ 0 (mod 81)`. The gauge has degree one, inside the equal cap. Together with Claims 3–5 the exact minima are

```text
min D for B_(3,2)(D,D) = 3,
min D for B_(3,3)(D,D) = 5,
min D for B_(3,4)(D,D) = 7.
```

The survivor is a finite cotangent truncation, not a polynomial lift to all depths.

### 7. Scope and successor — CONFIRMED

The three exact minima agree with `(n-1)(p-1)+1` at `p=3` for `n=2,3,4`. That is a finite numerical coincidence until it is proved at `n=5` or in general. Nothing in the gate, the preregistration, the replay markers, or the mathematics above licenses:

- the formula at `n>=5`, or at a general odd prime;
- a positive lower rate for `κ_n(F)` beyond the parent theorem `κ_n → ∞`;
- existence or nonexistence of an all-depth polynomial lift of `(x-x^p,y)`;
- a `p=109` computation, an exponent rectangle, or AWS;
- identification of the exterior polar divisor with `A_infinity` or with projective infinity;
- a counterexample to the Jacobian conjecture, or any JC2 inference.

The parent already proves that every fixed equal cap dies at some finite depth. This gate computes the first four depths at `p=3`. An exact `n=5` discriminator — emptiness of `B_(3,5)(D,D)` at `D=7,8` and a cotangent (or other) survivor at `D=9` — is the smallest computational successor. An inductive highest-carry / unit-certificate lemma, that after the analogous degree bounds the monomial `x^{2(n-1)} y` in the `p^{n-1}` digit remains a unit, is the smallest successor that would promote the slope itself. A general-`p` version of either is larger still.

---

## Non-blocking remarks

1. The sentence that “the `x^2` coefficient of `(9)` gives `a_{[x^3]}=b_{[x^2 y]}=0`” overstates the divergence row. Over `F_3` the source `a_{[x^3]}` is invisible in `a_x`. The vanishing `a_{[x^3]}=0` is the degree bound, which is already proved. The unit certificate does not need a different row.
2. The unit combination equals `1` in `F_3`, not as an identity of integer polynomials. Over `Z` it is `1+6 a_{[xy]} b_{[x^4]}-3 c_{[x^5]}`. The gate states the `F_3` claim, and the integer leftover is divisible by 3 with no division performed.
3. The depth-three `D=5` rank `28/28` is first-digit consistency. Existence at depth three is the cotangent witness, not a lift of that affine kernel to `c,d`.
4. Replay reconstructs the depth-three affine matrix from `A=x+3a`, `B=y+3b`. That is a valid necessary subsystem for over-cap rows; `c,d` of degree `<=D` cannot cancel degree `>D`.
5. The same-model `independent_check.py` enumerates the same 81 tuples and is a useful regression. It is not this review.

None of these changes a valuation, a rank, a forbidden coefficient, or a numbered verdict.
