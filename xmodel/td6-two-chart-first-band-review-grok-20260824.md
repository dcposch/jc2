# Hostile different-model review — TD6 two-chart first band

| Field | Value |
|---|---|
| Claim under review | Frozen TD6-TWO-CHART-FIRST-BAND: one licensed SP-2/r9-M2 chart-pattern specialization, with shared global coefficients in the fixed rectangles, has nonempty first Jacobian band over `Q`; the deterministic witness is not Keller and realizes no terminal class |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Hidden local-to-global step | none: a particular `Q`-point of one source-typed first-band affine space is not promoted to a Keller pair, a class realization, a landing theorem, a counterexample, or JC2 |
| Evidence tier | independent exact algebra over `Q` (producer replay plus a second sparse engine that does not import it: iterative chart powers, reverse-lex row order, modular rank over `F_1000000007`, and chart-then-differentiate Jacobians); hand two-forms and pole ODE; primary-source read of committed SP-2/LR2/AF3 r9-M2 ledger text and the reviewed parent centering-escape |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T10:19:14Z – 2026-08-24T10:35:00Z |
| Python | 3.14.6; stdlib `fractions.Fraction` / `math` / `hashlib` only |
| Host | Darwin arm64 |

Producer inputs reread in full before any verdict:

- `xmodel/td6-two-chart-first-band-20260824.md` (SHA-256 `cb373892233bddaf1b8fbf7722335ca43ee366b337151c3b244d2604d8168bf2`)
- `cases/td6_two_chart_first_band_20260824/replay.py` (SHA-256 `c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735`)
- `cases/td6_two_chart_first_band_20260824/FREEZE.sha256` (SHA-256 `995a0ba55a20b9aa59626654614fe54a5f8beb95742a5376ddf006eef3fe3d49`)

All three frozen hashes match the launch prompt. The freeze file body is exactly the two producer hashes above. The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. No producer, canonical, ladder, or PDF file was edited. No AWS work was launched. The next nonlinear rows were not appended.

Reviewed parent and its hostile review, reread against that basis:

- `xmodel/td6-global-compatibility-gate-20260824.md` SHA-256 `b53064c877a4f0b741f23f036b2323195bef825ccc72b6722b98f1fc2d2eec17`
- its typography erratum SHA-256 `efbf05ca2e9f1e13cdc2f6dd67a5510176d6e3e0ce5eb6a0c263046f2ce812dd`
- `xmodel/td6-global-compatibility-review-grok-20260824.md` SHA-256 `f3e468f415fdd7bd1aa85962090d34a55bf6ff15d469c28373347cf1c7cc42ac`

Cited canonical SP-2 / F1 / r9-M2 material reread against the working tree the producer charged (uncommitted parent updates sit on the clean basis; hashes below are the files on disk, not the older committed blobs):

- `ladder/SHEET6.md` SHA-256 `fbec069198310c286193be92adbb05eae2a3b7bdf3d317496e4fb4d262358661`
- `ladder/SHEET6-CAMPAIGN.md` SHA-256 `fca34f4cad606c9097cdb87c4e9e51609ab5c73d16a03efd764a7c06cdc4ccbb`
- `ladder/SHEET6-LROOT.md` SHA-256 `3eb95441c10f375274f8642f2005550e5487477e1b844f9712ea1a48bf220661` (SP-2 ledger 175, 187–200; remaining two-chart surface 256–274)
- `ladder/SHEET6-LT-REVIEW.md` SHA-256 `82d94e1a43ae9ec315189b4892faafa840027f4f1696dba6a394866331aa22c6` (LR2 re-derivation 66–73)
- `ladder/SHEET6-AF3.md` SHA-256 `555363fde61291a0c689bbf9d789c01f73734e0c403d350d85ae2fd0ddab8099` (§4 entry family, displayed ODE)
- `ladder/SHEET6-AF2.md` (IIa pattern `(η^ν−c^ν)^μ Π_k`)
- `ladder/SHEET6-A3L1-REVIEW.md` (entry-family ODE re-check, A=3, B=9 → 675)

All seven charged input hashes in the producer header match the files on disk.

**Promotion.** Accept as `NONEMPTY-WITNESS / STOP` of *this* proposed first-band polynomial-compatibility obstruction, for *one* licensed SP-2/r9-M2 chart-pattern specialization. Bank the joint rank `3508/3602`, the deterministic witness hash, and the two un-imposed next-row hashes. Promote nothing else.

**Quarantine.** The witness is not a Keller pair. No terminal class is realized. The first band being nonempty for this specialization does not imply that every first band is nonempty. Exact `J=1`, landing, coverage, and JC2 remain untouched.

---

## Headline and subclaim table

Write `s=y^{-1}`, `x=s+s^2+s^3+t s^4` (so `T=xy^4-y^3-y^2-y=t`), F1 chart `x=q^{-5}`, `y=η q`, and pole chart `x=r^{-25}`, `y=r^5+ζ r^{17}` (equivalently `q=r^5`, `η=1+ζ r^{12}`).

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Fixed rectangles `(15,60)/(25,100)`, shared centering `(1,1,1)`, reduced F1 polynomial `P=(η^5-1)^2(η^5-2)(η^5-28/25)`, zero dead stretch, `A=1/9` with transported scales `L^3=27`, `L^5=243`, and the three chart substitutions are one licensed control inside SP-2/LR2 + AF3 r9/M2; they are not data forced by the terminal class | **CONFIRMED** | a printed LR2 clause pinning `(c1,c2,c3)=(0,0,0)` or forbidding `(1,1,1)`; IIa reduced pattern required to be a different orbit triple; n=12 / zero dead stretch forced rather than permitted; producer claiming the specialisation is unique or terminal-forced |
| 2 | x-boundary `t^{15}` / `t+t^{25}`; F1 leadings `P^3`, `P^5`; r9/M2 member `p=27ζ(ζ^5-1/9)`, `q=243(ζ^{10}-5/27 ζ^5+5/729)` satisfies `3p q'-5p' q=25`; chart two-forms `dx∧dy=s^2 ds∧dt` and `det ∂(x,y)/∂(r,ζ)=-25 r^{-9}`; the first pole Jacobian row is the ODE built into transport, not 38 extra linear rows | **CONFIRMED** | ODE leftover not 25; two-form exponent `s^1` or `s^3`, or pole det not `-25 r^{-9}`; F1 leading `J_{q,η}` supplying a first nonzero Jacobian constraint that the compiler omitted; `[r^0]J` failing for the transported patterns |
| 3 | Sparse compilers on shared `a_{ij},b_{ij}`: `976`/`2626` variables, transport ranks `946/976` and `2524/2626`, forty x-J rows of which 38 are new, joint rank `3508/3602` (nullity 94); no local copies, no omitted stated transport band, no duplicate variable ids | **CONFIRMED** | a local coefficient copy; joint rank ≠ 3508 over `Q`; independent x-J rows ≠ 38; a stated holomorphy/leading key missing from the compiler; `g` rows writing into `f` indices |
| 4 | Deterministic free=0 rational witness is a genuine `Q`-point of the affine space: 441+1160 nonzero terms, serialization 44200 bytes, SHA-256 `65ae46524727904e636561c6314d1bf65bc3cb31990de89fccacb007953ddf52`; every imposed equation holds by a second path | **CONFIRMED** | empty system; solution only mod `p`; witness hash mismatch under reverse-lex GE; a compiled row failing on the reconstructed polynomials |
| 5 | Un-imposed `[s^{-1}]J` has 35 nonzero terms, SHA-256 `93545adb834f9a3a24bf7a30d7bbb0e30f4cfeea7632d7f3ab82944db36db751`; `[r^1](J-1)` has 2 nonzero terms, SHA-256 `91b086a32d5b268591935b632ce4699d1132f89efd4abc8bbdcb9d5e39346af7`; for this witness `global_J_exact=false` and `terminal_class_realized=false`; later/global data listed in producer §2C remain untied | **CONFIRMED** | either next row identically zero for the witness; those hashes failing; producer inferring emptiness of the next band from this one witness |
| 6 | Scope of `NONEMPTY-WITNESS` is exactly one source-typed first-band specialisation. It stops the proposed obstruction “this first-band system is empty”. It does not imply all first bands are nonempty, and it is not a Keller pair, terminal realization, landing theorem, counterexample, or JC2 decision | **CONFIRMED** | the producer promoting a class kill/realization, exact `J=1`, or a quantification over centering/orbits/`A` |

All remarks below are non-blocking unless marked otherwise. None changes a rank, a witness hash, a next-row hash, or a verdict.

---

## Replay

Registered command, rerun unmodified from the charged tree:

```sh
python3 cases/td6_two_chart_first_band_20260824/replay.py
```

Exit code 0. Printed verdict:

```text
TD6-TWO-CHART-FIRST-BAND: PASS
verdict = NONEMPTY-WITNESS
transport.f = rank 946 / 976; nullity 30
transport.g = rank 2524 / 2626; nullity 102
shared_first_J = rank 3508 / 3602; nullity 94; independent_J_rows=38
witness.terms = f:441 g:1160
witness.sha256 = 65ae46524727904e636561c6314d1bf65bc3cb31990de89fccacb007953ddf52
witness.serialized_bytes = 44200
next_x_row = s^-1 NONZERO terms=35 sha256=93545adb834f9a3a24bf7a30d7bbb0e30f4cfeea7632d7f3ab82944db36db751
next_pole_row = r^1 NONZERO terms=2 sha256=91b086a32d5b268591935b632ce4699d1132f89efd4abc8bbdcb9d5e39346af7
global_J_exact = false
terminal_class_realized = false
```

Canonical stdout SHA-256, including its final newline, recomputed independently:

`06f92eb5cdee0d4b654ab6a27a5e79f4edcd77bcae2ce0cd04b55206e6587a14`.

This matches the producer report. Arithmetic is `fractions.Fraction` on sparse monomials. No CAS, no floating point, no import of the parent D73 or centering-escape code.

A second engine, written for this review and not imported from the registered script, recomputed every identity the registered script actually computes, with three deliberate differences: (i) iterative multiplication for `x^i` in the centered chart, not the producer multinomial; (ii) reverse-lexicographic row order in least-index sparse GE; (iii) an extra rank computation of the same sparse matrix over `F_1000000007`. It also differentiated the substituted chart series (path B) rather than only substituting the polynomial Jacobian (path A). It recorded matching ranks, the same witness hash, the same next-row hashes, and zero failed assertions.

---

## 1. Source typing: one licensed control, not terminal-forced data

SP-2 from committed `SHEET6-LROOT.md:175,187–200`: chain

```text
F0 = (3,6,5,2,8) → F1 = (15,60,5,4,4)  (μ=2 IIa k=2, n=12) → (0,y),
```

type `(3,5)`, `(k_f,l_f)=(60,15)`, `(k_g,l_g)=(100,25)`, `R=π_G=4`, slack 0, one x-cluster. Newton rectangles written as ordinary exponent bounds are exactly `(15,60)/(25,100)`. Reduced F1 pattern `(η^5-c^5)^2 Π_2`. IIa dictionary (`SHEET6-AF2.md:127`) is `p=(η^ν-c^ν)^μ Π_k` with `k≥1`, here `ν=5`, `μ=2`, `k=2`.

LR2 (`LROOT:143–158`, re-derived `LT-REVIEW:66–73`): all x-side branches share one unramified truncation with no split or characteristic exponent below height four. The parent centering-escape, dual-confirmed, already showed that LR2 does **not** pin `(c1,c2,c3)=(0,0,0)` and that `T=xy^4-y^3` is legal. The present choice `(c1,c2,c3)=(1,1,1)` is a further common integral-power specialisation of that same truncation. Integer powers `y^{-1},y^{-2},y^{-3}` are divisible by `e_0` and, being shared, create neither a characteristic exponent nor a `V_2` split. Independently, in the chart,

```text
x y^4 - y^3 - y^2 - y = t
```

as a Laurent identity (the three extra centering terms cancel against `x y^4`). So `T` remains a global polynomial. This licenses the centering; it does not prove that every SP-2 realisation can or must be normalised to `(1,1,1)`. The producer says so.

AF3 §4, up to units:

```text
p = η(η^5-A),     p_g = B(η^{10}-(5/3)A η^5+(5/9)A^2),     AB ≠ 0,
```

with `3p p_g'-5 p' p_g=(25/9)A^3 B` constant, both squarefree and coprime, unique admissible parity `(e,e_g)=(1,0)`. A3L1-REVIEW re-checked the ODE at `A=3`, `B=9` (leftover 675). The producer takes `A=1/9` and the transported top scales `L^3=27`, `L^5=243` with implicit `B=243`. That is a point of the cited one-parameter family, not the whole family.

F1 polynomial. The three fifth-power orbit values `1,2,28/25` are nonzero and distinct; the chain orbit is the squared one. `deg P=20`, so `deg P^3=60` and `deg P^5=100` match the rectangles' `j`-bounds. The value `28/25` is a convenience that makes the Taylor coefficient `L=25(1-2)(1-28/25)=3` a small integer; it is not forced by Q-data. Likewise `A=1/9` makes the linear r9 coefficient `-3`.

Dead stretch. LROOT records `n=12` for this IIa step, which is the chart `η=1+ζ r^{12}`, equivalently `y=r^5+ζ r^{17}`. The eleven intervening coefficients of `r^6,…,r^{16}` are specialised to zero. The compiler comment calls this “a licensed fully specified chain choice”. It is permitted, not derived from the terminal ledger.

Pole scales. Near `η=1+ζ r^{12}`,

```text
η^5-1 = 5 ζ r^{12}+O(r^{24}),
(η^5-1)^2 (η^5-2)(η^5-28/25) = 3 ζ^2 r^{24}+O(r^{36}).
```

So `L=3`, and the transported tops of `P^3` and `P^5` are `L^3=27` and `L^5=243`. These match the leading `ζ^6` / `ζ^{10}` coefficients of the scaled r9 member. The lower `ζ^1` term in `p` is r9 structure, not the F1 Taylor; F1 transport and F0 transport constrain different Laurent bands (`q`-powers `≤-15` versus `r`-powers `≤-3`) and are compatible because the joint solve is consistent.

Chart substitutions. F1 `x=q^{-5}`, `y=η q` is the order-`ν=5` y-pole chart at F1. The pole chart is that chart pulled back along `q=r^5` with zero dead stretch. The x-chart is the LR2-legal shared truncation at height four. All three act on the **same** global monomials `x^i y^j`.

What is forced by the terminal class, versus selected:

| datum | status |
|---|---|
| rectangles `(15,60)/(25,100)`, type `(3,5)`, `R=4`, one x-cluster, IIa `μ=2,k=2,ν=5`, r9/M2 shape `p=ζ(ζ^5-A)` | forced (SP-2 / AF3) |
| common unramified truncation of length 3, no split below height 4 | forced (LR2) |
| `(c1,c2,c3)=(1,1,1)` | selected |
| x-boundary monomials `t^{15}`, `t+t^{25}` rather than general unsplit degree-15/25 polynomials | selected (parent-jet pattern) |
| extra orbits `2` and `28/25` | selected |
| dead stretch identically 0, `A=1/9` | selected |
| free variables of the affine space set to 0 | selected particular solution |

The producer does not claim the selected line is forced. Claim 1 stands.

---

## 2. Leading patterns, two-forms, ODE, and the built-in pole Jacobian

**x-boundary.** After holomorphy through `s=0`, the compiler sets `[s^0]` exactly to `t^{15}` and `t+t^{25}`. Independently, the reconstructed witness satisfies those identities and has no negative `s`-powers.

**F1.** `P` rebuilt from fifth-factors; `P^3` has length 61 and leading coefficient 1, `P^5` length 101 and leading coefficient 1. The compiler imposes every `q`-power `≤-15` (resp. `≤-25`) and the exact leading polynomial. Independently, the witness matches those bands.

**Pole family and ODE.** Directly on

```text
p = 27 ζ^6 - 3 ζ,
q = 243 ζ^{10} - 45 ζ^5 + 5/3,
```

one has `p'=162 ζ^5-3` and `q'=2430 ζ^9-225 ζ^4`, and

```text
3p q' = 196830 ζ^{15} - 40095 ζ^{10} + 2025 ζ^5,
5 p' q = 196830 ζ^{15} - 40095 ζ^{10} + 2025 ζ^5 - 25,
```

hence `3p q'-5 p' q=25` exactly. The unscaled AF3 identity `3p0 q0'-(5)p0' q0=(25/9)A^3` at `A=1/9` is leftover `25/6561`; multiplying by the transported scales `27·243=6561` recovers 25. The second engine asserted the same univariate identity.

**x-chart two-form.**

```text
x = s+s^2+s^3+t s^4,     y = s^{-1},
dx = (1+2s+3s^2+4 t s^3) ds + s^4 dt,
dy = -s^{-2} ds,
dx∧dy = s^4 dt ∧ (-s^{-2} ds) = s^2 ds∧dt.
```

The `ds` part of `dx` wedges to 0 against `dy`. Extra centering coefficients therefore do **not** change the 2-form: it is the same `s^2` as in the parent chart `x=s+t s^4`. Consequently `J_{s,t}=s^2 J_{x,y}`, and the first possible pole of `J_{x,y}` is `s^{-2}`. With

```text
F = t^{15} + s f1(t) + O(s^2),     G = t+t^{25} + s g1(t) + O(s^2),
```

`[s^0]J_{s,t}=f1(1+25 t^{24})-15 t^{14} g1`. Vanishing of that polynomial is exactly `[s^{-2}]J=0`. Only `s^0` and `s^1` of `F,G` enter, so the identity is linear in the global coefficients once transport has pinned `s^0`. Degrees: `f1` has `t`-degree `≤15` and `g1` has `t`-degree `≤25`, so `f1·25 t^{24}` and `15 t^{14} g1` have degree `≤39`. Forty coefficient equations, degrees `0..39`, is exact. Independently, none of those forty rows is the zero form.

**Pole two-form.**

```text
x = r^{-25},     y = r^5 + ζ r^{17},
∂x/∂r = -25 r^{-26},     ∂x/∂ζ = 0,     ∂y/∂ζ = r^{17},
det ∂(x,y)/∂(r,ζ) = -25 r^{-9}.
```

If `f=r^{-3}p(ζ)+O(r^{-2})` and `g=r^{-5}q(ζ)+O(r^{-4})`, then

```text
J_{r,ζ} = r^{-9}(5 p' q - 3 p q') + higher.
```

No term of `J_{r,ζ}` is more singular than `r^{-9}`, because transport forbids `r`-powers of `f` below `-3` and of `g` below `-5`. The ODE `3p q'-5 p' q=25` is therefore exactly `J_{r,ζ}=-25 r^{-9}` at leading order, hence `[r^0]J_{x,y}=1` and no negative `r`-powers. Path A (polynomial `J` then substitute) and path B (expand `f,g` in `(r,ζ)`, differentiate, divide by `-25 r^{-9}`) both give `[r^0]J={0:1}` and empty negative bands for the witness.

**Why this is “built into transport”, not 38 extra rows.** The forty linear Jacobian rows are x-end only. At the pole end the first Jacobian coefficient is a condition on the *leading patterns themselves*. Those patterns are already the transport targets. Adding the ODE as extra rows on `(a_{ij},b_{ij})` would be redundant: it holds identically for every point of the transport space of this specialisation.

**F1 leading Jacobian is not a missing first-band row.** For `f=q^{-15}P^3` and `g=q^{-25}P^5`,

```text
J_{q,η} = (-15 q^{-16} P^3)(5 q^{-25} P^4 P') - (3 q^{-15} P^2 P')(-25 q^{-26} P^5) = 0
```

at leading order, by the type-`(3,5)` monomial map. The first nonzero pole-side Jacobian coefficient is therefore invisible at F1 scale and appears only after the chain blowup, i.e. as the r9 ODE. That is the correct first band. Intermediate `q`-powers of `J_{q,η}` between `q^{-41}` and `q^{-5}`, and Jacobian conditions at the extra F1 orbits `η^5=2` and `η^5=28/25`, are **not** imposed; they sit in producer §2C.

Claim 2 stands.

---

## 3. Compilers, shared coefficients, ranks

Variable counts, independently: `f` has `(15+1)·(60+1)=976` monomials, `g` has `(25+1)·(100+1)=2626`, jointly `3602`. Indexing is `vid=i·(jmax+1)+j` with a single offset `976` for `g`. Every chart row writes into those ids. No second copy of any coefficient is introduced.

Compiled unique keys (second engine; dict keys, so no duplicate equations):

| block | X (`s≤0`) | F1 | F0 | packed | rank | nullity |
|---|---:|---:|---:|---:|---:|---:|
| `f` | 496 | 403 | 865 | 1764 | 946 | 30 |
| `g` | 1326 | 1071 | 2346 | 4743 | 2524 | 102 |

Packed row counts exceed rank: the compilers emit a redundant spanning set of the stated bands, not a basis. Consistency of the surplus is checked by exact row replay on the solution. Nothing in the stated bands (holomorphy below the leading pole, plus the exact leading polynomial in each chart) is omitted: every monomial contribution with exponent at most the cutoff is added, and every listed leading degree is given a right-hand side.

Separate transport solves (reverse-lex least-index GE) give ranks `946` and `2524`. The same matrices over `F_1000000007` have the same ranks. Because rank over `F_p` is at most rank over `Q`, this pins the `Q`-ranks from below at the claimed values; the exact GE pins them from above.

Joint system: transport rows of `f` and `g` occupy disjoint variable blocks, so their combined rank is `946+2524=3470`. Forty x-J rows are then appended. Joint exact rank is `3508`, hence `38` new independent rows, nullity `94`. Modular rank over `F_1000000007` is again `3508`. The 38 new pivot columns lie outside the transport pivot set. Two of the forty J-rows are linearly dependent on transport plus the other J-rows; that is expected (the 40 coefficients of a degree-`≤39` identity need not be independent modulo already-pinned `s^0`/`s^1` data).

Hostile checks that failed to fire:

- `g` rows mentioning an `f` index, or `f` rows mentioning an index `≥976`: none.
- a zero x-J row: none.
- a local `a_{ij}` for the pole chart distinct from the x-chart: none.
- joint rank sensitive to row order: reverse-lex versus producer insertion order gave the same rank and the same particular solution.

Claim 3 stands.

---

## 4. Deterministic rational witness, second path, nonemptiness over `Q`

The solver uses least-index pivots and sets every non-pivot variable to `0`. Over a field the leftmost pivot columns of a matrix are unique, so the coordinate subspace complementary to the free variables contains at most one solution. Reverse-lex row order reproduced the producer witness byte-for-byte:

- support `441` terms in `f`, `1160` in `g`;
- corners `f[(15,60)]=g[(25,100)]=1`, and every exponent inside the rectangles;
- canonical serialization `f\n` then `i,j:num/den\n` (same for `g`), `44200` bytes;
- SHA-256 `65ae46524727904e636561c6314d1bf65bc3cb31990de89fccacb007953ddf52`.

Every compiled row, including the forty x-J rows, was replayed on this vector over `Q`. Independently, the reconstructed polynomials were expanded in all three charts by iterative powers and matched the imposed bands. Path A and path B Jacobians agreed.

This is a point of an affine space defined over `Q`, obtained by exact division in `fractions.Fraction`. It is not a modular lift and not a numerical approximate kernel vector. Nullity `94` means the solution is not unique; nonemptiness over `Q` requires only one point, which this is.

Claim 4 stands.

---

## 5. Next un-imposed rows, fail-closed flags, and what remains untied

Path A (substitute polynomial `J`) and path B (chart derivatives) agree on the first un-imposed bands of this witness.

**x-side `[s^{-1}]J`.** Thirty-five nonzero terms in `t`. Degree 12 is absent (sparse serialization). Canonical payload SHA-256

`93545adb834f9a3a24bf7a30d7bbb0e30f4cfeea7632d7f3ab82944db36db751`.

Independent re-hash of the payload matches. Equivalently this is `[s^1]J_{s,t}`, and `[s^0]J_{s,t}` is empty, so the imposed `[s^{-2}]J=0` is confirmed by the same expansion.

**pole-side `[r^1](J-1)`.** Because `[r^0]J=1`, this is `[r^1]J`. Exactly two terms, at `ζ`-degrees 3 and 8:

```text
3 : 2772625764147988388350297 / 8906250
8 : 12519627029971450902411024 / 1484375
```

SHA-256 `91b086a32d5b268591935b632ce4699d1132f89efd4abc8bbdcb9d5e39346af7`. Both coefficients are nonzero rationals.

Thus this witness proves every claimed finite equation and proves its own failure to be Keller: `J` is not identically 1. No terminal class is realised by a non-Keller pair with only first-band data. The flags `global_J_exact=false` and `terminal_class_realized=false` are therefore correct **for this witness**. The producer does not infer that every point of the 94-dimensional affine space has those next rows nonzero, and does not infer that the next band is empty.

What remains untied or unquantified, matching producer §2C and parent §5:

- the 94 free directions (frozen to zero here);
- the selected centering, extra-orbit, dead-stretch, and `A` parameters, chosen before the solve;
- every local coefficient beyond the prescribed leading/boundary bands;
- every Jacobian coefficient after `[s^{-2}]` at the x-end and after `[r^0]` at the pole end, in particular the pair (9);
- Jacobian conditions at F1 extra orbits and at all other points at infinity;
- finite-fiber data, mapping degree, landing, coverage, `G2-PSC` / `G2-BD`, and the (22) ledger of a global pair.

The next x-row is not a linear condition on the 94-space. Expanding `F=t^{15}+s f1+s^2 f2+…` and `G=t+t^{25}+s g1+s^2 g2+…` gives

```text
[s^1] J_{s,t} = 2 f2(1+25 t^{24}) - 30 t^{14} g2 + (f1 g1' - f1' g1).
```

The last parenthesis is bilinear in the first transverse coefficients, which still vary on the 94-space (transport pins `s^0`; the 38 x-J rows constrain but do not kill `f1,g1`). A successor that merely appends linear rows is the wrong object, as the producer states.

Claim 5 stands.

---

## 6. Scope of `NONEMPTY-WITNESS`

The parent remaining implication (`td6-global-compatibility-gate-20260824.md` §5; `LROOT:256–274`) asked for a two-chart coefficient transport on the original rectangles, with centering carried as data, consuming r9/M2 patterns at the first band where they enter. This report is that first band, for one point of the allowed parameter space.

What is proved: the affine linear system “SP-2 rectangles + this centering + this `P` + this zero dead stretch + this r9/M2 member + `[s^{-2}]J=0` + pole leading ODE” is nonempty over `Q`, of rank `3508` in `3602` variables. Therefore “this first-band system is empty” is false, and cannot kill SP-2.

What is not proved, and is not claimed:

- nonemptiness of the first band after quantifying `(c1,c2,c3)`, extra orbits, dead-stretch coefficients, or `A`;
- nonemptiness of any later Jacobian band, in particular of (9);
- a polynomial with `J≡1`;
- a realization of SP-2 or of any of the other seven terminal classes;
- a pairing of complete Eggers trees, a landing theorem, a counterexample, or a JC2 decision.

The exact conclusion is negative but useful: this source-typed first-band specialisation supplies no global polynomial obstruction. That is the right size for `NONEMPTY-WITNESS / STOP`.

Claim 6 stands.

---

## Source caveats (none load-bearing)

1. The x-side formula for `η_F` remains the “same way” clause of Sigray Notation 3.9, as in the parent review. The identity `T=xy^4-y^3-y^2-y` used here is a direct Laurent check in the selected chart, not a new reading of Notation 3.9.
2. `n=12` is taken from the SP-2 series audit (`LROOT:187–188`) as the IIa step datum licensing `η=1+ζ r^{12}`. The eleven zero dead-stretch coefficients are a further specialisation of that chart, not a printed uniqueness statement.
3. AF3 §4 supplies the r9/M2 family up to units. The producer’s scales `27` and `243` are the Taylor transport of the selected `P` at the chain orbit; they are compatible with the family but not the unique unit normalisation.
4. The special-fiber `Λ`-count and D73 equality mechanism of the parent jets are not reused and are not needed. This gate is coefficient transport, not a `Λ`-equality claim.
5. Working-tree hashes of `ladder/SHEET6.md` and `ladder/SHEET6-LROOT.md` differ from the older blobs cited in the parent review, because those two files now carry the parent’s remaining-surface paragraph. The producer charged the working-tree hashes; those match disk. The parent gate file itself is byte-frozen and unchanged.
6. Packed transport row counts (1764 / 4743) are larger than the ranks. That is redundancy of the compiled spanning set, not an omitted-band defect and not a rank defect.

---

## Promotion advice

**Accept** the report as a bounded `NONEMPTY-WITNESS / STOP` of the proposed first-band emptiness obstruction for this one licensed SP-2/r9-M2 chart-pattern specialisation. Bank:

- joint rank `3508/3602`, nullity `94`, with `38` new x-J rows on top of transport `946+2524`;
- witness SHA-256 `65ae46524727904e636561c6314d1bf65bc3cb31990de89fccacb007953ddf52`;
- next-row SHA-256 values `93545adb…` and `91b086a3…`;
- the fact that the first pole Jacobian coefficient is the r9 ODE, already present in transport.

**Do not accept** as any of the following:

- a polynomial Keller pair, or a realization of SP-2 or of any other terminal class;
- a proof that every first-band specialisation is nonempty, or a quantification over centering / orbits / dead stretch / `A`;
- a kill of any slack-0 class, or a cut of the book 8;
- exact all-order `J=1`, a convergent or algebraized pair, or a landing/coverage theorem;
- a JC2 decision.

Successor work, if any, has to parameterise the 94-dimensional exact affine space of *this* specialisation (or a quantified family of such spaces) and solve the polynomial pair

```text
[s^{-1}]J = 0,     [r^1](J-1) = 0
```

without pretending those are linear rows. Compatibility at all displayed Jacobian rows would still need the omitted global Eggers and landing conditions before it represented a terminal class. A contradiction confined to a different centering, a nonzero dead stretch, or a `C[T,x]` subring is pre-registered as a wrong-object stop.

---

## Explicit exclusions

This review does not:

- edit the producer file, the replay, `FREEZE.sha256`, `ladder/SHEET6-LROOT.md`, `ladder/SHEET6-LT-REVIEW.md`, `ladder/SHEET6-AF3.md`, `AUDIT.md`, `APPROACHES.md`, or `refs/sigray_full.pdf`;
- append the next nonlinear Jacobian rows, or launch AWS;
- treat other uncommitted xmodel artifacts (AS109, secant, fresh-connection, …) as evidence;
- assert that the 94-space contains, or does not contain, a point with both next rows zero;
- assert anything about extra F1 orbits, finite fibers, mapping degree, or the (22) ledger of a global pair.

Frozen producer SHA-256, recomputed on disk at review time:

```text
cb373892233bddaf1b8fbf7722335ca43ee366b337151c3b244d2604d8168bf2  xmodel/td6-two-chart-first-band-20260824.md
c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735  cases/td6_two_chart_first_band_20260824/replay.py
995a0ba55a20b9aa59626654614fe54a5f8beb95742a5376ddf006eef3fe3d49  cases/td6_two_chart_first_band_20260824/FREEZE.sha256
```
