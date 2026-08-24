# Hostile different-model review — balanced cyclotomic AS terminal family

| Field | Value |
|---|---|
| Claim under review | Frozen producer: for every odd integer `m>=3` there is a triangular total-degree `D=2m+1` map-only AS-seed residue which survives modulo `3^(2m)` and has no same-cap lift modulo `3^(2m+1)`. This is a family of finite-depth controls, not an all-depth lift or counterexample |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | `m=2`: `A_2(z)B_2(z)=(1-z^2)^2=1-2z^2+z^4 ≠ 1-z^4`. Oddness of `m` is load-bearing for (1). The AS special fibre further requires `m>=3` (`m=1` satisfies (1) but reduces to `(x+x^3,y)`) |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking writeup remarks below; a compatible all-depth branch at fixed `D`, classification of a full locus, a uniform upper death bound for other branches, a characteristic-zero lift or no-lift theorem, a counterexample, and JC2 are correctly *not* claimed) |
| Evidence tier | independent geometric-sum identities over `Z[z]`; 3-adic valuation of every coefficient of `P_m`; exact Jacobian over `Q[x]` / `Q_3[x]`, not a congruence; clean unit-denominator representatives, including when `3|(2k+1)`; first-variation linearization including `λ^2`; mixed / Frobenius / shear / representative attacks and monomial exhaustion at `m=3,5,7,9`; independent recovery of the frozen D7 point and a complete D11 point; unmodified rerun of the registered program as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `1e60fcedc8626650c7c7544ad296c3624173415f` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T17:36:57Z – 2026-08-24T17:44:52Z |
| Python | host CPython 3.14.6 (hashes, Fraction/`Z` convolution, 3-adic inverses, monomial exhaustion, registered replay); uv-unavailable host SymPy `1.14.0` via the Cellar PyTorch site-packages, used only as a second CAS |
| Singular | 4.4.1 (independent characteristic-0 identities `A B-(1-z^{2m})` and `P_x Q_y-(1-3^{2m}x^{4m})` for `m=1..9`, plus explicit integrated maps at `m=3,5,7`) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, freeze, and named payloads reread in full before any verdict:

- `xmodel/as-fonly-p3-balanced-cyclotomic-terminal-family-20260824.md` (SHA-256 `8d6873550d06136f3a725160161500a844b43c9793a90c59798e5dc2b3c4c8e4`)
- `cases/as_fonly_p3_balanced_cyclotomic_family_20260824/MANIFEST.sha256` (SHA-256 `c4244493a6e94c5f2ddb275d8aab1bd61902e78d6a8bcba9af3fff3441398494`)
- `cases/as_fonly_p3_balanced_cyclotomic_family_20260824/README.md` (SHA-256 `d55b6c3c58c9e5e756553e767a071a640d351ffdfa7d5682ef7579b89bdfc006`)
- `cases/as_fonly_p3_balanced_cyclotomic_family_20260824/replay.py` (SHA-256 `7464a1936ee089fc0d22f24ff4c3151225aea7942845a14d69ad283388fc53ef`)
- `cases/as_fonly_p3_balanced_cyclotomic_family_20260824/FREEZE.txt` (SHA-256 `577e974fafbbff2db9af99ca920660175a8bb5944651eb8228e4aa1bc4308d6a`)

Confirmed D7 triangular terminal producer/review, consumed only as a regression target for `m=3`:

- `xmodel/as-fonly-p3-d7-depth6-triangular-terminal-20260824.md` (SHA-256 `5325890a505489570a6e02409d64e026560d2635ddf989b865039eeb6ecddccb`)
- `xmodel/as-fonly-p3-d7-depth6-triangular-terminal-review-grok-20260824.md` (SHA-256 `75ff0c8588c633fcf53e17104bf77cdc74fba30bc9c02aa776b23ad0baaa2318`)

The committed basis is exactly `1e60fcedc8626650c7c7544ad296c3624173415f`. Named producer artifacts remain uncommitted on top of that basis. No producer, case, canonical, ladder, notes, prompt, log, run, or erratum file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp/as_fonly_p3_cyc_review/` and did not import `replay.py`.

Tried hard, and failed, to make even `m` satisfy `A_m B_m=1-z^{2m}`; to replace `B_m=A_m(-z)` by `(1-z)S_m(z)` or by `S_m(-z)` and still obtain (1); to find a coefficient of `P_m` with negative 3-adic valuation, or a `k>=2` term that survives modulo 3; to cancel a top coefficient of `P_m` or `Q_m` at modulus `3^{2m}` or `3^{2m+1}`; to equate a dirty integer reduction of `P_m` with the exact identity `1-3^{2m}x^{4m}` over `Z`; to cancel `x^{4m}` by a mixed cap-`D` digit, a Frobenius monomial, a target shear, a representative change, or the quadratic Jacobian term; to treat `m=1` as an AS-seed; and to promote the family to a compatible all-depth branch at fixed `D`, a full-locus classification, a uniform death bound for other residues, a characteristic-zero lift or no-lift theorem, a counterexample, or JC2. The only tested cancellation of `x^{4m}` uses a total-degree `4m+1` digit (`V=x^{4m} y`, or `U=x^{4m+1}` when `4m+1` is a unit modulo 3), which is excluded by every family cap `D=2m+1`.

---

## Promotion

**Accept `FOR EVERY ODD INTEGER m>=3 THERE IS A TRIANGULAR TOTAL-DEGREE D=2m+1 MAP-ONLY AS-SEED RESIDUE WHICH SURVIVES MODULO 3^{2m} AND HAS NO SAME-CAP LIFT MODULO 3^{2m+1}`.**

On the map-only category `FONLY_(3,n)(D=2m+1)` — polynomials `P,Q` over `Z/3^n Z` of total degree at most `2m+1`, special fibre `(x-x^3,y)` over `F_3`, `det J(P,Q)=1`, and **no** cap on a canonical gauge `(A,B)`:

- The exact maps over the localisation `Z_{(3)} subset Z_3`,
  `P_m` the zero-constant antiderivative of `A_m(3x^2)` and `Q_m=y B_m(3x^2)`,
  with `A_m=(1+z)(1+...+z^{m-1})` and `B_m=A_m(-z)`, have total degree `2m+1`, reduce to `(x-x^3,y)` modulo 3, and satisfy the identity `det J(P_m,Q_m)=1-3^{2m}x^{4m}` in `Q[x]`. Reducing coefficients via unit-denominator inverses gives a genuine point of `FONLY_(3,2m)(D=2m+1)`.
- Every same-residue next lift at the same cap is `P_m+3^{2m}U`, `Q_m+3^{2m}V` with `deg U,V<=2m+1`. The first residual is `-x^{4m}+U_x+V_y (mod 3)`. No divergence of total degree at most `2m` has an `x^{4m}` term, so the fibre of this residue in `FONLY_(3,2m+1)(D=2m+1)` is empty.
- At `m=3` the construction independently recovers the frozen D7 point `P=x+2x^3+441x^5+108x^7`, `Q=y-6x^2 y+18x^4 y-27x^6 y` modulo 729, and the clean next representative `1566` of the `x^7` coefficient. At `m=5` it supplies an explicit D11 point modulo `3^{10}` which survives through depth ten and is terminal at depth eleven.

**Do not promote this to:** a compatible all-depth branch at any fixed `D`; emptiness of `FONLY_(3,2m+1)(D=2m+1)` or classification of that locus; a uniform upper death bound for other triangular or non-triangular residues; a simultaneous `(A,B)` gauge-cap theorem; a polynomial, Tate-algebra, or inverse-limit lift of `(x-x^3,y)`; a characteristic-zero no-lift theorem; a counterexample to JC; or any JC2 inference. It does not falsify any characteristic-zero expectation that `D=2m+1` is a negative control. It falsifies only the stronger finite claim that a theorem-calibrated negative degree must already be empty at a shallow Witt level: in this family the survival depth is exactly `D-1`.

**Smallest honest successor.** Each displayed residue is dead at its family cap; do not spend further work trying to lift *these* residues at `D=2m+1`. The smallest exact search that could decide emptiness of `FONLY_(3,2m+1)(D=2m+1)` is an exhaustive compilation of every other depth-`2m` residue at that cap. The family is a compiler regression fixture, not that compilation.

A true pointwise corollary of the same degree comparison, not claimed by the producer and not a locus theorem, is recorded in Claim 4: the displayed residue remains terminal at every total-degree cap `D'<=4m`. The first degree at which a divergence can see `x^{4m}` is `4m+1`. That still does not produce a lift, classify a locus, or bound other branches.

---

## Quarantine

No result here proves or disproves JC2, constructs or excludes a polynomial lift of `(x-x^3,y)`, identifies the polar divisor with `A_infinity`, runs `p=109`, empties any bounded system `FONLY_(3,2m+1)(D=2m+1)`, produces a compatible tower at fixed `D`, or supplies a uniform death depth for residues outside this family. Producer strings `PASS-AS-FONLY-P3-BALANCED-CYCLOTOMIC-FAMILY`, `m3=FROZEN-D7-POINT-RECOVERED`, `m5=D11-SURVIVES-DEPTH10-TERMINAL-DEPTH11`, and `all_depth_inference=false` were not used as evidence; the geometric identity, the valuation of `A_k 3^k/(2k+1)`, the exact Jacobian, the clean inverses, the first-variation formula, and the four instantiations were re-derived. The confirmed D7 review is a regression target for `m=3` only. Independent reconstruction, not the producer script, is the evidence for every numbered claim.

---

## Scope (not enlarged)

One prime `p=3`; the odd integers `m>=3`; for each such `m`, one triangular residue class of total degree `D=2m+1`, surviving through depth `2m` and terminal at depth `2m+1`. The kill is pointwise in that residue class. No rectangular support, no enumerator, no AWS, no gauge cap, and no modular-to-characteristic-zero existence inference are in scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | For every odd `m>=3`, `A_m=(1+z)S_m` and `B_m=A_m(-z)` satisfy `A_m B_m=1-z^{2m}` as polynomials. Oddness is used for the sign `(-z)^m=-z^m`. Even `m` fails, with smallest counterexample `m=2` | **CONFIRMED** | a coefficient of `A_m B_m-(1-z^{2m})` nonzero for some odd `m`; even `m` accidentally satisfying (1); the identity depending on a cancelled factor that is not a domain argument |
| 2 | With `z=3x^2`, the zero-constant antiderivative `P_m` of `A_m(z)` has every coefficient in `Z_3`: after writing `2k+1=3^a u` the remaining denominator `u` is a 3-adic unit. The only nonzero correction modulo 3 is `2x^3`, so the special fibre is `(x-x^3,y)`. Both total degrees are exactly `D=2m+1` at the working moduli | **CONFIRMED** | some `k` with `v_3(2k+1)>k`; a `k>=2` coefficient nonzero modulo 3; top coefficient of `P_m` or `Q_m` of valuation `>=2m`; `m=1` sneaking in as an AS-seed |
| 3 | Over `Q_3[x]` (in fact over `Q[x]`) one has `det J(P_m,Q_m)=1-3^{2m}x^{4m}` exactly, not a congruence. The maps therefore survive modulo `3^{2m}`. Clean representatives modulo `3^{2m+1}` are the unit-denominator 3-adic digits, well-defined even when `3|(2k+1)` | **CONFIRMED** | an extra monomial in the exact Jacobian; a denominator not invertible modulo `3^{2m+1}` after cancelling `3^a`; survival failing for the exact maps |
| 4 | Every same-residue lift at depth `2m+1` has residual `-x^{4m}+U_x+V_y (mod 3)`. Under cap `D=2m+1` one has `deg(U_x+V_y)<=2m<4m`, hence terminality. Mixed monomials, Frobenius derivatives, representative changes, target shears, and the quadratic Jacobian term do not cancel `x^{4m}` | **CONFIRMED** | a leftover cross term not divisible by 3; `3^{4m}` not vanishing modulo `3^{2m+1}`; a cap-`D` pair with residual `0`; a representative change moving the `x^{4m}` class |
| 5 | Independent instantiation at `m=3,5,7,9` recovers the frozen D7 coefficients and the clean `1566` representative at `m=3`, and produces a complete D11 point modulo `3^{10}` whose exact determinant is `1-3^{10}x^{20}` and whose next obstruction is `-x^{20}` | **CONFIRMED** | mismatch with the frozen D7 point; `1566≢108 (mod 729)`; a D11 Jacobian not equal to `1-59049 x^{20}`; a cap-eleven digit cancelling `x^{20}` |
| 6 | The exact meaning is an infinite family of different finite-degree points, each terminal one digit after depth `D-1`. It is a compiler regression family. It is not an all-depth branch at fixed `D`, not a locus classification, not a uniform death bound, not a characteristic-zero lift/no-lift, not a counterexample, and not a JC2 inference. A stronger *pointwise* cap-range terminality through `D'<=4m` follows from the same comparison and does not enlarge the campaign meaning | **CONFIRMED** | `FONLY_(3,2m+1)(D=2m+1)=∅` asserted; a compatible tower at fixed `D`; the cap-range corollary sold as a locus theorem or uniform bound |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Replay and hashes

Frozen hashes, recomputed on the charged tree, match the launch prompt, the manifest, and the freeze record:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as-fonly-p3-balanced-cyclotomic-terminal-family-20260824.md` | `8d6873550d06136f3a725160161500a844b43c9793a90c59798e5dc2b3c4c8e4` | prompt, freeze `report_sha256` |
| `cases/.../MANIFEST.sha256` | `c4244493a6e94c5f2ddb275d8aab1bd61902e78d6a8bcba9af3fff3441398494` | prompt, freeze `manifest_sha256` |
| `cases/.../README.md` | `d55b6c3c58c9e5e756553e767a071a640d351ffdfa7d5682ef7579b89bdfc006` | prompt, `MANIFEST` |
| `cases/.../replay.py` | `7464a1936ee089fc0d22f24ff4c3151225aea7942845a14d69ad283388fc53ef` | prompt, freeze `replay_sha256`, `MANIFEST` |
| `cases/.../FREEZE.txt` | `577e974fafbbff2db9af99ca920660175a8bb5944651eb8228e4aa1bc4308d6a` | prompt |
| D7 producer | `5325890a505489570a6e02409d64e026560d2635ddf989b865039eeb6ecddccb` | prompt, D7 freeze |
| D7 review | `75ff0c8588c633fcf53e17104bf77cdc74fba30bc9c02aa776b23ad0baaa2318` | prompt |

Every member hash inside `MANIFEST.sha256` was recomputed from the case directory and matched. The freeze file is not a second copy of the manifest; it names the report, manifest, replay, and payload digests. `FREEZE.txt` itself is not a manifest member. That is freeze bookkeeping, not a mathematical gap.

Registered command, rerun unmodified from the repository root:

```text
shasum -a 256 -c cases/as_fonly_p3_balanced_cyclotomic_family_20260824/MANIFEST.sha256
python3 cases/as_fonly_p3_balanced_cyclotomic_family_20260824/replay.py
```

The manifest check passed. The replay exited 0 and printed `payload_sha256=badabc43d596f94e8fbae3ca2f2afbbaf6115af529423ed8974b544cb739b27b`, matching the launch prompt and the freeze record. Those Booleans and the printed `PASS-*` strings were discarded as evidence for Claims 1–6.

Independent engines, written for this review and not imported from the registered program (scratch SHA-256, outside the repository):

- Fraction/`Z` convolution + 3-adic inverses + monomial exhaustion, host CPython 3.14.6: `bf559a9eb833b0ea112524d163324846d77ced8889685e85693bb3a5b5683b9b` (script), report digest `9d0d9ea3d780a7d62db24c4a56696d95b20e04890248fc385845fb22ed95fdf4`
- SymPy `1.14.0` over `QQ[z]` / `QQ[x,y]`: `b5d2c6f6faa466e86c1c31abab211332fc759dedc689990713b202be06432d5c` (script), output digest `451f1c25e814386b91fac27a7dd6559c177d45bf208dd97fc506dba1aa88cd91`
- Singular 4.4.1 over `Q`: `8a78fda212a70edc69bfe94246a9bae49761497687c9050a9ec80651fb8d77ff` (script)

The three engines produced the same odd-`m` identity `AB=1-z^{2m}`, the same even-`m` square `(1-z^m)^2`, the same exact Jacobians `1-3^{2m}x^{4m}`, and the same special fibre `(x+2x^3,y) ≡ (x-x^3,y) (mod 3)`.

---

## Independent recomputation

### 1. Geometric identity, oddness, even-`m` control — CONFIRMED

Write `S_m(z)=sum_{i=0}^{m-1} z^i`, a polynomial, and set `A_m=(1+z)S_m`, `B_m=A_m(-z)=(1-z)S_m(-z)`. These are the producer’s definitions, reconstructed from the finite sums rather than from the stored coefficient pattern. Expanding the first product gives the coefficient list

```text
A_m = 1 + 2z + 2z^2 + ... + 2z^{m-1} + z^m
```

for every integer `m>=1`, odd or even. Direct convolution for `m=1..15` matches that pattern. The pattern is therefore not the oddness hypothesis.

The identity `A_m B_m=1-z^{2m}` *does* use oddness. In `Z[z]`, which is an integral domain,

```text
(1-z) S_m(z) = 1-z^m,
(1+z) S_m(-z) = 1-(-z)^m.
```

If `m` is odd then `(-z)^m=-z^m`, so the second display is `1+z^m`. Multiplying,

```text
A_m B_m (1-z^2)
  = (1+z)(1-z^m) · (1-z)(1+z^m)
  = (1-z^2)(1-z^{2m}).
```

Cancelling the non-zero-divisor `1-z^2` yields (1). Equivalently, as rational functions one has `S_m(z)S_m(-z)=(1-z^{2m})/(1-z^2)` and therefore `A_m B_m=(1-z^2)·S_m(z)S_m(-z)=1-z^{2m}`; both sides are polynomials, so the identity holds in `Z[z]`. Evaluation at `z=±1` is consistent (`0=0`).

If `m` is even then `(-z)^m=z^m`, the same computation produces `A_m B_m=(1-z^m)^2`, and

```text
(1-z^m)^2 - (1-z^{2m}) = 2z^{2m}-2z^m ≠ 0.
```

The smallest failing identity is `m=2`:

```text
A_2=(1+z)^2=1+2z+z^2,     B_2=1-2z+z^2,
A_2 B_2=1-2z^2+z^4,
1-z^4=1-z^4,
difference = 2z^4-2z^2.
```

Singular over `Q` returns the same difference `2z^4-2z^2` and confirms `A_2 B_2-(1-z^2)^2=0`. Direct convolution and SymPy agree for every even `m=2,4,6,8,10,12`: the product is the square, never `1-z^{2m}`.

Two wrong-factor controls at the first odd value `m=3` also fail, so the sign in `B_m=A_m(-z)` is load-bearing:

```text
A_3·(1-z)S_3 = 1+2z+2z^2-2z^4-2z^5-z^6,
A_3·S_3(-z)  = 1+z+z^2+z^3+z^4+z^5,
A_3 B_3      = 1-z^6.
```

Odd `m=1,3,5,7,9,11,13,15` all give `AB=1-z^{2m}` on all three engines. Claim 1 is the identity for odd `m>=3`; `m=1` is postponed to Claim 2 as a special-fibre control, not a failure of (1).

### 2. `Z_3` coefficients, special fibre, total degree — CONFIRMED

Set `z=3x^2`. Then `A_m(3x^2)=sum_{k=0}^m A_k 3^k x^{2k}` with `A_0=A_m=1` and `A_k=2` for `1<=k<=m-1`. The unique antiderivative with `P_m(0)=0` is the finite sum

```text
P_m = sum_{k=0}^m (A_k 3^k / (2k+1)) x^{2k+1},
Q_m = y sum_{k=0}^m B_k 3^k x^{2k}.
```

`Q_m` has integer coefficients. For `P_m`, write `2k+1=3^a u` with `u` coprime to 3. Then `2k+1>=3^a`, so `k>=(3^a-1)/2`. The comparison `a<=(3^a-1)/2` is `3^a>=2a+1`, which holds for every `a>=0`. Hence `a<=k`, and after cancelling `3^a` the remaining denominator is the unit `u`. Every coefficient of `P_m` therefore lies in `Z_{(3)} subset Z_3`. Direct 3-adic valuation for `k=0..400` never violates `v_3(2k+1)<=k`. Equality `v_3(2k+1)=k` occurs only at `(k,2k+1)=(0,1)` and `(1,3)`.

For `k=1` one has `A_1=2` as soon as `m>=2`, and the coefficient is `2·3/3=2` exactly. For `k>=2` the stricter bound `v_3(2k+1)<=k-1` holds: the only equality case `a=k` is `k=1`, and for a pure power `2k+1=3^a` with `a>=2` one has `2a+3<=3^a`. The smallest gaps `k-v_3(2k+1)` for `k>=2` are 2 (at `k=2,4`). Consequently every coefficient of `P_m` except those of `x` and `x^3` has positive 3-adic valuation, and

```text
P_m ≡ x+2x^3 ≡ x-x^3,     Q_m ≡ y     (mod 3).
```

This was checked for every odd `m=3,5,...,39` by reducing the unit-denominator representatives modulo 3, and in SymPy by reducing `P_m,Q_m` coefficientwise; all four maps `m=3,5,7,9` reduce to `2x^3+x` and `y`.

The bound `m>=3` is load-bearing for the special fibre. At `m=1` one has `A_1=1+z`, so the `k=1` term is the top term with coefficient `3/3=1`, and `P_1=x+x^3 ≡ x+x^3 ≢ x-x^3 (mod 3)`. Identity (1) holds at `m=1`; the AS-seed does not.

Total degrees are exactly `D=2m+1` as polynomials over `Q`, and they remain `D` after reduction at the working moduli. The top coefficient of `P_m` is `3^m/(2m+1)`, of valuation `m-v_3(2m+1)<=m<2m` for `m>=3`, hence nonzero modulo `3^{2m}` and modulo `3^{2m+1}`. The top coefficient of `Q_m` is `(-1)^m 3^m=-3^m`, of valuation `m`. There is no top-coefficient cancellation. The extreme case `m=13` (where `2m+1=27=3^3`) has top `P`-coefficient `3^{10}=59049`, valuation 10, strictly less than depth 26.

### 3. Exact determinant, survival, clean representatives — CONFIRMED

The maps are triangular, `P_m=P_m(x)` and `Q_m=y T_m(x)`, so `P_y=0` and `det J=P_x Q_y`. Differentiating the antiderivative over `Q` recovers `P_x=A_m(3x^2)` on the nose, and `Q_y=B_m(3x^2)`. Identity (1) therefore gives the *exact* polynomial identity

```text
det J(P_m,Q_m)=A_m(3x^2)B_m(3x^2)=1-(3x^2)^{2m}=1-3^{2m}x^{4m}
```

in `Q[x]`, hence in `Q_3[x]` and in `Z_3[x]`. This is not a congruence. Three engines return a zero error polynomial at `m=3,5,7,9`; Singular additionally returns a zero error for the product `P_x Q_y` at every odd `m=1,3,5,7,9` without integrating. Survival modulo `3^{2m}` is immediate: `det J-1` is divisible by `3^{2m}` and by nothing smaller in the leading term.

Clean coefficient representatives modulo `M=3^{N}` are the residues `A_k 3^k (2k+1)^{-1} (mod M)`, computed after cancelling `3^a` from `2k+1=3^a u` and inverting the unit `u` modulo `M`. The inverse exists for every `N`, including `N=2m+1`, even when `a>=1`. Samples:

- `k=1`, `2k+1=3`, coefficient exactly `2`.
- `k=4`, `2k+1=9`, coefficient exactly `18` for every `m>=5`.
- `m=7`, `k=7`, `2k+1=15=3·5`, coefficient `3^7/15=729/5`. Then `5^{-1}` exists modulo `3^{14}=4782969` and modulo `3^{15}=14348907`, giving the clean digits `3826521` and `8609490` respectively. Check: `3826521·5=729+4·4782969` and `8609490·5=729+3·14348907`.

A dirty reduction of `P_m` modulo `3^{2m}` still satisfies `det J ≡ 1 (mod 3^{2m})`, but its first residual need not be `-x^{4m}`. That is the D7 lesson, and it recurs at every sampled `m`:

| `m` | dirty residual of `P_mod` modulo 3 | clean residual of `P_clean` modulo 3 |
|---|---|---|
| 3 | `x^6-x^{12}` | `-x^{12}` |
| 5 | `x^6+x^{10}-x^{20}` | `-x^{20}` |
| 7 | `x^6-x^{10}+x^{12}-x^{28}` | `-x^{28}` |
| 9 | `-x^6+x^{10}-x^{12}+x^{16}+x^{18}-x^{36}` | `-x^{36}` |

The extra low terms are divergences of the representative error `P_clean-P_mod=3^{2m} W` with `deg W<=D`. For `m=3` one has `W=2x^7` and `W_x≡2x^6 (mod 3)`, converting `x^6-x^{12}` into `-x^{12}`, which is the confirmed D7 calculation. Using the unit-denominator digits modulo `3^{2m+1}` is therefore legitimate and necessary for the obstruction; claiming that an arbitrary 0-to-`3^{2m}-1` lift of the same class already has residual `-x^{4m}` is false, and is not what the producer writes.

Over `Z`, the clean integer polynomial is still not equal to the exact `P_m` (the error is a multiple of `3^{2m+1}`). For `m=3` the clean Jacobian equals `1-729x^{12}` only modulo 2187, as already recorded in the D7 review. For every sampled `m` the difference `det J(P_clean,Q_m)-(1-3^{2m}x^{4m})` *is* divisible by `3^{2m+1}`. The exact identity belongs to the 3-adic/rational maps; the clean congruence belongs to their digits modulo the next power.

### 4. Linearization, degree bound, attacks — CONFIRMED

Let `λ=3^{2m}` and let `P_new=P_m+λ U`, `Q_new=Q_m+λ V` with `deg U,V<=D=2m+1`. Since `P_y=0` exactly,

```text
det J(P_new,Q_new)
  = (P_x+λ U_x)(Q_y+λ V_y) - (λ U_y)(Q_x+λ V_x)
  = P_x Q_y + λ(U_x Q_y + P_x V_y - U_y Q_x) + λ^2 det J(U,V).
```

Substitute `P_x Q_y=1-λ x^{4m}`. The quadratic coefficient has 3-adic valuation `4m`. The next modulus is `3^{2m+1}`, and `4m>2m+1` for every integer `m>=1`, so `λ^2 ≡ 0 (mod 3^{2m+1})`. After division by `λ` the residual is the polynomial

```text
-x^{4m} + U_x Q_y + P_x V_y - U_y Q_x     (mod 3).
```

Modulo 3 one has `P_x=A_m(3x^2)≡1`, `Q_y=B_m(3x^2)≡1`, and `Q_x=y (B_m(3x^2))'` with every coefficient of the derivative divisible by 3, hence `Q_x≡0`. The special-fibre Jacobian of `(x-x^3,y)` is `diag(1-3x^2,1)≡I (mod 3)`. The residual collapses to

```text
-x^{4m} + U_x + V_y     (mod 3).
```

A polynomial of total degree at most `2m+1` has derivatives of total degree at most `2m`. The comparison `2m<4m` is the terminality. Equivalently, the monomial primitives of `x^{4m}` are `x^{4m+1}/(4m+1)` and `x^{4m} y`, both of degree `4m+1>2m+1`.

Attacks, all of which leave the class `-x^{4m}` untouched at cap `D`:

- **Mixed monomials.** If `U=x^i y^j` with `j>=1` and `i+j<=2m+1`, then `U_x` still carries `y^j` and cannot produce a pure power `x^{4m}`. If `V=x^i y^j`, then `V_y=j x^i y^{j-1}` produces `x^{4m}` only for `(i,j)=(4m,1)`, of degree `4m+1`. Exhaustion of every monomial of total degree `<=D` at `m=3,5,7,9` returned zero hits on `x^{4m}`. An explicit mixed pair at `m=5`, `U=x^5 y^2+2x^3 y+x^{11}`, `V=y^{11}+x^4 y^2+2x^6 y`, has divergence supported in degrees `<=10` and no `x^{20}` term. A second pair `U=x^5 y^2`, `V=x^4 y^2` has unreduced linear form congruent to `U_x+V_y=2x^4 y^2+2x^4 y` modulo 3, matching the special-fibre reduction, still with no `x^{20}`.
- **Frobenius derivatives.** In characteristic 3, `∂_x x^{3k}=0`. These monomials shrink the image of divergence; they do not enlarge it. At `m=5` the naive primitive `U=x^{21}` is itself a Frobenius monomial (`21≡0 (mod 3)`), so even at cap 21 that particular `U` fails. The `V`-primitive `V=x^{20} y` has multiplier 1 and is the one that first sees `x^{20}`.
- **Representative changes.** Replacing a depth-`2m` digit by another lift of the same class adds a divergence `W_x+Z_y` of degree `<=2m`. The `x^{4m}` class is invariant. Explicitly, the digits of `P_clean-P_mod` at `m=3,5,7,9` reproduce the dirty-to-clean residual conversion recorded in Claim 3 and never touch `x^{4m}`.
- **Target shears.** `V=S(x)` has `V_y=0`. For triangular maps the shear `S(x)` is determinant-invisible at every precision: `det J(P, yT+S)=P_x T`.
- **Quadratic term.** `λ^2 det J(U,V)` has valuation `4m>=2m+1`, hence vanishes at the next digit. After division by `λ` it is still `0` in `F_3`.

The same comparison yields a pointwise corollary the producer did not need: this residue is terminal at every total-degree cap `D'` with `D'<=4m`, because `deg(div)<=D'-1<4m`. The first cap at which a divergence can cancel `x^{4m}` is `4m+1`, via `V=x^{4m} y` (always, multiplier 1) and via `U=x^{4m+1}` when `4m+1≢0 (mod 3)`. That is not a lift theorem at cap `4m+1`, not a locus statement, and not a death bound for any other residue. Cap `D=2m+1` is load-bearing for the family as stated, and is the only cap the producer claims.

### 5. Instantiations `m=3,5,7,9` — CONFIRMED

All four maps were rebuilt from the finite-sum definition of `A_m`, integrated over `Q`, and reduced by independent modular inverses. None of the numbers below was read from `replay.py`.

**`m=3`, `D=7`, depth 6, modulus 729.** Exact coefficients `P=x+2x^3+(18/5)x^5+(27/7)x^7` and `Q=y-6x^2 y+18x^4 y-27x^6 y`. Reducing via `5^{-1}≡146` and `7^{-1}≡625` modulo 729 gives

```text
P ≡ x+2x^3+441x^5+108x^7,
Q ≡ y+723 x^2 y+18x^4 y+702 x^6 y     (mod 729),
```

which is the frozen D7 point (`723≡-6`, `702≡-27`). The clean next inverse `7^{-1}` modulo 2187 produces `x^7` coefficient `1566=108+2·729`. Exact Jacobian `1-729x^{12}`; clean residual `-x^{12}`; dirty residual `x^6-x^{12}`, as in the confirmed D7 review. This is recovery of a previously reviewed point, not a second proof of the D7 compiler counts.

**`m=5`, `D=11`, depth 10, modulus `3^{10}=59049`.** Exact coefficients

```text
P = x + 2x^3 + (18/5)x^5 + (54/7)x^7 + 18 x^9 + (243/11)x^{11},
Q = y - 6x^2 y + 18x^4 y - 54x^6 y + 162x^8 y - 243 x^{10} y.
```

The `k=4` term has `2k+1=9`, coefficient exactly 18, a 3-divisible-denominator case that remains an integer. Unit inverses modulo 59049 give the complete D11 point

```text
P ≡ x + 2x^3 + 35433 x^5 + 33750 x^7 + 18 x^9 + 53703 x^{11},
Q ≡ y + 59043 x^2 y + 18 x^4 y + 58995 x^6 y + 162 x^8 y + 58806 x^{10} y
                                                                    (mod 59049).
```

Checks: `35433·5=18+3·59049`, `33750·7=54+4·59049`, `53703·11=243+10·59049`. Exact Jacobian `1-59049 x^{20}`. Clean representatives modulo `3^{11}=177147` are

```text
P ≡ x + 2x^3 + 35433 x^5 + 151848 x^7 + 18 x^9 + 112752 x^{11}
                                                                    (mod 177147),
```

with Jacobian `1-59049 x^{20}` modulo 177147 and next residual `-x^{20}`. No cap-eleven monomial produces an `x^{20}` in the divergence. The point is a genuine member of `FONLY_(3,10)(D=11)` with empty fibre in `FONLY_(3,11)(D=11)`.

**`m=7`, `D=15`, depth 14.** Exact top coefficient `729/5` (`3|(2m+1)`). Survival digit `3826521`, clean next digit `8609490`, both independent of the producer. Exact Jacobian `1-3^{14}x^{28}=1-4782969 x^{28}`. Clean residual `-x^{28}`. The 3-divisible denominators at exponents 3, 9, and 15 are `2`, `18`, and `729/5`, all with unit remaining denominator.

**`m=9`, `D=19`, depth 18.** Exact top `19683/19`. Clean residual `-x^{36}`. Exact Jacobian `1-3^{18}x^{36}=1-387420489 x^{36}`. Degrees 19 and 19.

SymPy independently integrated `P_m` from `A_m(3x^2)` at all four values and obtained the same rationals and the same exact determinants. Singular checked the `m=3,5,7` integrals against `P_x` and against `1-3^{2m}x^{4m}`.

### 6. Exact meaning, regression value, refused promotions — CONFIRMED

The construction yields one triangular residue for each odd integer `m>=3`. The degree `D=2m+1` takes infinitely many distinct values `7,11,15,19,...`. Each residue survives through depth `D-1=2m` and dies at depth `D` at that same cap. That is an infinite family of different finite-degree points, each terminal one digit after depth `D-1`.

It is not a compatible all-depth branch at fixed `D`: the member with parameter `m` lives at cap `2m+1` and dies at the next digit; increasing `m` changes the cap. Holding `D=7` and trying to ride the family to larger depth is the `m=3` point, already killed. It does not classify `FONLY_(3,2m)(D=2m+1)` or `FONLY_(3,2m+1)(D=2m+1)`: other triangular components and all non-triangular maps are untouched. It does not give a uniform upper death bound for other branches; it gives a *lower* bound on how late death can occur for some branches, namely depth `D` after a surviving depth `D-1`. It does not algebraize a Witt tower, produce or exclude a characteristic-zero Keller map, give `A_infinity=0`, or decide JC2.

As a compiler regression family it is exactly as useful as the producer states. Each pair

```text
(m, D=2m+1, n=2m survivor with det J=1, n=2m+1 terminal residual -x^{4m})
```

is a closed-form, arbitrarily deep, exact PASS/FAIL fixture, and the `m=3` end independently recovers a previously confirmed point. That is the right use. The pointwise cap-range corollary through `D'<=4m` is a free consequence of Claim 4 and may be used as an additional fixture (this residue dies at every cap from `2m+1` through `4m`). It still does not empty a locus and is not a uniform bound.

The campaign warning that a theorem-calibrated negative degree need not die at a shallow Witt level is licensed by the family and should not be read as a characteristic-zero statement. Depth `D-1` survival at cap `D` is compatible with `D` remaining a negative control over `Q`.

---

## Non-blocking remarks

1. The producer states “if `3^a` divides `2k+1`, then `a<=k`” without writing the comparison `3^a>=2a+1`. The inequality is true; the missing line is not a gap in the claim.
2. The first-variation display omits the quadratic term `λ^2 det J(U,V)`. Valuation `4m>2m+1` kills it for every `m>=1`. The D7 review had to check `729^2 ≡ 0 (mod 2187)` the same way.
3. Dirty integer reductions of `P_m` have extra residual monomials, exactly as at D7. The xmodel prose already insists on unit-denominator representatives modulo the next power. That distinction must not be collapsed to “the displayed 0-to-`3^{2m}-1` digits already have residual `-x^{4m}` over `Z`”.
4. `MANIFEST.sha256` does not list `FREEZE.txt`. The freeze file names the four digests it needs. Bookkeeping only.
5. The registered replay samples `m=3,5,7,9`. The universal claim is the algebraic identity, not the sample; Claim 5 is the sample.
6. Equation numbers in the producer report are consecutive and not reused. No D7-style numbering collision.
7. `m=13` (top denominator `27=3^3`) was used as an extra stress test of Claims 2–4 and is not a producer obligation.

None of these remarks changes a numbered verdict.

---

## End quarantine

This review confirms an infinite family of pointwise map-only statements at one prime, one special fibre, and one triangular residue per odd `m>=3`. It does not empty any `FONLY_(3,2m+1)(D=2m+1)`, does not cap a gauge, does not produce a tower or a polynomial, and does not speak to JC2. Independent reconstruction is the evidence; registered `PASS-*` strings are not.
