# Hostile different-model review — AS post-D10 omitted Frobenius cross-carry erratum

| Field | Value |
|---|---|
| Claim under review | Frozen erratum: the quarantined post-D10 D9/D8 generator included `L/3` from the four derivative-visible degree-six Frobenius directions, then formed the degree-nine/eight residual from `M` alone, omitting the single-cross `[K_Frob/3] mod 3`. That term is nonzero. Vertical D8 columns/counts and the entire stated `g`-endpoint reduction/counts are retracted. The vertical D9 global section, six D8 unit pivots, D8 coefficient matrix, and its geometric rank loci survive. No corrected census, and no change to the reviewed D10 theorem |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking remarks below; a regenerated census, the next divided carry, full `D=7`, lift/no-lift, characteristic zero, a counterexample, and JC2 are correctly *not* claimed) |
| Evidence tier | independent integer Jacobian expansion over `Z` (400 random `(U,V,C,D)` samples, zero remainder); constructive check of `(det J-1)/27=E1+M+3N` after `L=3L1` and `E=3E1` (80 random families plus the vertical witness with a degree-seven `C` correction, plus the minimal pair `V=x^2 y`, `D=x^4 y`); independent single-cross formula versus `K(U0+UF,V0+VF)-K(U0,V0)` on both licensed branches; all nine Frobenius Poisson products after `/3` mod 3; symbolic max-degree profiles in all six Frobenius directions; two integer witnesses rebuilt from scratch; F3 exhaustion of the published D9 section (`729` points) and of matrix `(6)` (`2187` points); source audit of the quarantined generator as frozen bytes, not as mathematics |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the erratum producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD at launch | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` (the charged freeze basis) |
| Git HEAD at close | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` (unchanged) |
| Review window (UTC) | 2026-08-24T20:19:44Z – 2026-08-24T20:35:13Z |
| Python | host CPython 3.14.6 (hashes, integer identities, symbolic single-cross, F3 rank/section censuses, registered replay) |
| Singular | 4.4.1 (present; not used as mathematical evidence) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Erratum, freeze, and named payloads reread in full before any verdict:

- `xmodel/as-fonly-d7-postd10-d98-f3-erratum-20260824.md` (SHA-256 `26dd0908295bfbcc36ad2f0efe59b645ce1dd11411fd88ab8e37337a74fc0d7d`)
- `cases/as_fonly_d7_postd10_d98_f3_erratum_20260824/FREEZE.txt` (SHA-256 `cd3009992df83be446c2ffbab6249137e6fbbc7096f5b6d29a3cc885dbdd487e`)
- `cases/as_fonly_d7_postd10_d98_f3_erratum_20260824/MANIFEST.sha256` (SHA-256 `5a3d0f9f4587064988cfa7ae3a6be399b4d8f24908d0033367e220f07d935978`)
- `cases/as_fonly_d7_postd10_d98_f3_erratum_20260824/README.md` (SHA-256 `f69b3aa744a8f94c42134176f6a27ad93f6ae8b37fb06e84bfa72c168931aefc`)
- `cases/as_fonly_d7_postd10_d98_f3_erratum_20260824/replay_omitted_frobenius_carry.py` (SHA-256 `0bc6d3913fedf322a48a8d79acef1af56d6b3b41f078aa49ecf1b60bc0b463d8`)

Quarantined predecessor, consumed only for the retraction ledger, byte-preservation check, and the source-omission audit, never as live compatibility evidence:

- `xmodel/as-fonly-d7-postd10-d98-f3-20260824.md` (SHA-256 `ff85614982fb26a7d8aba2859c7d1be6e3274ff8170114f23b247b5172fd0fc9`)
- `cases/as_fonly_d7_postd10_d98_f3_20260824/FREEZE.txt` (SHA-256 `f03fc06930c12398f714d5af60ed93374ffa80226bf1504d9429747cbdd6fa60`)
- `cases/as_fonly_d7_postd10_d98_f3_20260824/MANIFEST.sha256` (SHA-256 `1efda261bcd531fd4352c8b3f27ee2cafd77b7bf36dd31a9379d9083733a8f2b`)
- `cases/as_fonly_d7_postd10_d98_f3_20260824/generate_and_enumerate.py` (SHA-256 `243c357c18dbbe445f665621ceb5c748f96aa026cb73947fe38dd8b7af8e365e`)

Confirmed D10 producer/review and corrected divided-carry predecessor, consumed only to refuse promotion into those theorems and to check that degree ten is out of range of the omitted term:

- `xmodel/as-fonly-d7-degree10-pointwise-20260824.md` (SHA-256 `e4311a80aef2d3617c7b449e16cb19d34cfe25d31c558bb68f78ddc02fcae4ab`)
- `xmodel/as-fonly-d7-degree10-pointwise-review-grok-20260824.md` (SHA-256 `8ccaa15fd9180660d5ab7e2957737c028a96bb5b28508378e0a3ca93964089b5`), overall **CONFIRMED**
- `xmodel/as-fonly-first-residual-divided-carry-deep-d7-erratum-20260824.md` (SHA-256 `cbcd8851200f2ab15c29a7b9414c1d720c7aee0aa852b2cd522dcd7d699ae194`)
- `xmodel/as-fonly-first-residual-divided-carry-deep-d7-erratum-review-grok-20260824.md` (SHA-256 `4e915fb6f7e8701d1932b2b28df76db35859520bc94ffe8fb08a1cd679936ae8`), overall **CONFIRMED**

The charged freeze basis is `2e6104a417cfe15a93a901aa0a9129094a2ae11b`. Review started and closed there. Named erratum artifacts remain uncommitted. Recomputed erratum hashes at close match the launch table. No producer, erratum, case, canonical, prompt, log, run, coordination, or predecessor file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp/as_d7_d98_f3_erratum_review/` and did not import `replay_omitted_frobenius_carry.py`, `generate_and_enumerate.py`, or any Singular payload as mathematical evidence.

Tried hard, and failed, to cancel the omitted degree-eight class `2x^8` by any bounded `C_x+D_y` (those reach degree at most six); to keep a double-Frobenius product alive after division by three; to leak a single Frobenius cross into the degree-ten mixed-carry row; to produce a degree-nine single-cross on the vertical branch; to express `u6_0` or `v6_6` as a triangular rewrite of `f_a,f_b,f_c,f_d`; to restore the stated `g`-endpoint rows `g f_c=g f_d=0` after adjoining formula (4); to make `M` depend on a degree-six Frobenius coefficient modulo three; to find a rank-one or rank-four value of the published `7 x 5` matrix on any of the `2187` literal F3 bases; and to promote the erratum to a corrected census, a next divided carry, full `D=7`, lift/no-lift, characteristic zero, a counterexample, or JC2.

---

## Promotion

**Accept `THE QUARANTINED POST-D10 D9/D8 GENERATOR INCLUDED L/3 FROM THE DEGREE-SIX FROBENIUS FIRST-DIGIT LAYER, THEN FORMED THE DEGREE-NINE/EIGHT RESIDUAL FROM M ALONE, OMITTING THE SINGLE-CROSS [K_Frob/3] MOD 3. THAT TERM IS NONZERO IN EXACT INTEGER WITNESSES. THE FROZEN VERTICAL INHOMOGENEOUS COLUMN AND EVERY COMPATIBILITY COUNT DERIVED FROM IT, AND THE ENTIRE STATED G-ENDPOINT REDUCTION AND COUNTS, ARE RETRACTED. THE VERTICAL D9 GLOBAL SECTION, SIX D8 UNIT PIVOTS, D8 COEFFICIENT MATRIX, AND ITS GEOMETRIC RANK LOCI SURVIVE. THE REVIEWED D10 THEOREM IS UNCHANGED.`**

On the map-only aligned deep branch `P=x-x^3+3U+9C`, `Q=y+3V+9D`:

- Over `Z`, `det J(P,Q)-1=3L+9(K+C_x+D_y)+27M+81N` with the displayed signs. After the reviewed first-digit equations give `L=3L1`, and after the next accepted row gives `E=L1+K+C_x+D_y=3E1`, the residual is exactly `(det J-1)/27=E1+M+3N`.
- Split `U=U0+UF`, `V=V0+VF` with the six degree-six Frobenius directions. Every integer derivative of `(UF,VF)` is divisible by three. The omitted class in `E1` is the single cross

```text
K_Frob/3 =
 (UF_x/3) V0_y +(U0_x-x^2)(VF_y/3)
 -(UF_y/3)V0_x-U0_y(VF_x/3).
```

  The double-Frobenius product is divisible by nine, hence vanishes after division by three. Against a degree-four base this reaches total degree eight and not nine. Against `V_5=g x^5` it reaches degree nine and not ten.
- The integer pair `U0=2x^4`, `V0=x^2 y+x^3 y`, `UF=x^6`, `VF=0` (the triangular inverse of the frozen fibre-count-one base `(P,Q,R,T,s,w,h)=(0,0,0,1,0,0,0)` with `f_b=1`) has

```text
[(K(U0+UF,V0)-K(U0,V0))/3] mod 3 = 2x^7+2x^8.
```

  On the `g=1` endpoint, `UF=y^6` and `V0=x^2 y+x^5` give `2 x y^6 + 2 x^4 y^5`. These terms are absent from the quarantined generator: that generator emits high rows from `M` alone, never names `u6_0` or `v6_6`, and inherits a mod-three formal derivative that drops every exponent divisible by three.
- Formula (4) does not involve `C,D`, so it cannot change the vertical D8 coefficient matrix, the six `M`-based unit pivots, or the triangular coordinates `(P,Q,R,T)`. It cannot reach vertical degree nine. Independently, the published D9 section identity holds at every F3 point of `(p,q,r,s,t,w)`, and the published `7 x 5` matrix takes only ranks `0,2,3,5` on all `2187` F3 bases, with the stated vanishing sets. The vertical D8 inhomogeneous column and every count/hash derived from it do not survive. On the `g` endpoint the degree-nine piece of (4) is `2 g u6_0 x^4 y^5 + g u6_3 x^7 y^2`, so the stated rows `g f_c=g f_d=0` and the `13 x 14` system do not survive. All six Frobenius directions enter (4).
- The omitted term has degree at most nine, so it does not alter the reviewed degree-ten gate. The erratum makes no corrected census and no next-carry, full-D7, lift/no-lift, characteristic-zero, counterexample, or JC2 claim.

**Do not promote this to:** a regenerated vertical or `g`-endpoint census; a completed following integer carry; emptiness or nonemptiness of `FONLY_(3,7)(D=7)`; all-depth lifting; a characteristic-zero lift or no-lift theorem; a counterexample to JC; or any JC2 inference. Do not treat the quarantined `50939/177147` or `954/4374` counts as accidentally still valid. Do not reuse the four-variable Frobenius fibre `(f_a,f_b,f_c,f_d)` as complete.

**Smallest honest successor.** Regenerate every affected inhomogeneous row from the integer expansion and formula (4), retain all six Frobenius directions, and only then repeat a literal-F3 census or advance a divided carry. The surviving vertical D9 section, D8 coefficient matrix, and rank loci may be reused as matrix-level statements; their old inhomogeneous columns and counts may not.

---

## Quarantine

The following predecessor statements are retracted and must not be reused as live mathematics:

- the frozen vertical degree-eight inhomogeneous column is the exact source column;
- the vertical compatibility census `50939/177147`, the fibre histogram, the displayed representatives, and the rank-stream hash `d7910730247c3da26599fac9c11cb28472ec7591ef49c221a825ef5978e17bee`;
- the `g`-endpoint equations `g f_c=g f_d=0`, the remaining `13 x 14` system, the census `954/4374`, the fibre histogram, and the rank-stream hash `119580e2aab411d56dc2b41f6118cf9fd03768bb8cc10397c0aa2b29abcd2da8`;
- the four displayed Frobenius variables `f_a=u6_3`, `f_b=u6_6`, `f_c=v6_0`, `f_d=v6_3` are the only relevant degree-six directions for the degree-nine/eight residual.

The quarantined bytes themselves are unchanged. No result here proves or disproves JC2, constructs or excludes a polynomial lift of `(x-x^3,y)`, empties or populates `FONLY_(3,7)(D=7)`, runs a corrected census, or produces a compatible tower. Producer string `PASS-OMITTED-FROBENIUS-CROSS-CARRY-WITNESSES` was not used as evidence; the Jacobian identities, formula (4), both witnesses, the degree bounds, and the preservation/retraction boundary were re-derived. Independent reconstruction, not the erratum replay, is the evidence for every numbered claim.

---

## Scope (not enlarged)

One prime `p=3`; one total-degree cap seven; the aligned deep branch of the confirmed 30-row first-digit ideal; the omitted single-cross in the post-D10 degree-nine/eight residual on the licensed vertical and `g`-endpoint survivors of the confirmed degree-ten gate. No rectangular support, no enumerator, no AWS, no gauge cap, and no modular-to-characteristic-zero existence inference are in scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | From `P=x-x^3+3U+9C`, `Q=y+3V+9D`, the identity `det J-1=3L+9(K+C_x+D_y)+27M+81N` holds over `Z`. After `L=3L1` and `E=L1+K+C_x+D_y=3E1`, the residual is `(det J-1)/27=E1+M+3N` | **CONFIRMED** | a leftover sign on `K`, `M`, or `N`; a `27`-term already in the `(U,V)`-only expansion; `(det J-1)/27` unequal to `E1+M+3N` on a pair with both divisibility hypotheses |
| 2 | Split `U=U0+UF`, `V=V0+VF` with the six degree-six Frobenius directions. The omitted class is the displayed single-cross (4). The double-Frobenius product vanishes after `/3`. Maximum degree is eight on the vertical branch and nine on the `g` endpoint | **CONFIRMED** | a double-Frobenius monomial surviving `/3` mod 3; a degree-nine single-cross on vertical; a degree-ten single-cross on either licensed branch; formula (4) missing a seed or a direction |
| 3 | The integer witnesses rebuild as `2x^7+2x^8` and `2 x y^6+2 x^4 y^5` modulo 3. Those terms are absent from the quarantined generator, not rewritten in `(P,Q,R,T)` or in `(f_a,f_b,f_c,f_d)` | **CONFIRMED** | either witness polynomial unequal to the displayed support; the generator emitting `[K_Frob/3]` or naming `u6_0,v6_6`; `2x^8` already present in `M` at `C=D=0` |
| 4 | Vertical D9 global section, six D8 unit pivots, D8 coefficient matrix, and its geometric rank loci survive. Vertical D8 inhomogeneous column/counts and the entire stated `g`-endpoint reduction/counts do not. All six Frobenius directions enter (4) | **CONFIRMED** | a degree-nine single-cross on vertical; formula (4) contributing a `C,D` coefficient; a rank-one or rank-four F3 value of matrix (6); `g f_c=g f_d=0` still the full D9 residual after adjoining (4); `u6_0` or `v6_6` absent from (4) |
| 5 | The erratum does not alter the reviewed D10 theorem and makes no corrected census, next-carry, full-D7, lift/no-lift, characteristic-zero, counterexample, or JC2 claim | **CONFIRMED** | a degree-ten single-cross; the erratum asserting a new census or reusing `50939` / `954`; `FONLY_(3,7)(D=7)=∅` or `≠∅`; a lift, no-lift, or JC2 sentence |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Replay and hashes

Registered commands, rerun unmodified from the erratum case directory:

```sh
python3 replay_omitted_frobenius_carry.py
shasum -a 256 -c MANIFEST.sha256
```

Both exited 0. Replay printed `2x^7+2x^8`, `2 x y^6+2 x^4 y^5`, an empty double-Frobenius class, and `PASS-OMITTED-FROBENIUS-CROSS-CARRY-WITNESSES`. Manifest contents (`README.md`, `replay_omitted_frobenius_carry.py`) matched. These runs were regressions only.

The quarantined predecessor manifest, checked from its own directory, also matched (`README.md`, `audit_vertical_core_rank.sing`, `audit_vertical_d9_section.sing`, `generate_and_enumerate.py`).

Recomputed SHA-256 (all match the launch prompt and `FREEZE.txt`):

| Artifact | SHA-256 |
|---|---|
| `xmodel/as-fonly-d7-postd10-d98-f3-erratum-20260824.md` | `26dd0908295bfbcc36ad2f0efe59b645ce1dd11411fd88ab8e37337a74fc0d7d` |
| `cases/as_fonly_d7_postd10_d98_f3_erratum_20260824/MANIFEST.sha256` | `5a3d0f9f4587064988cfa7ae3a6be399b4d8f24908d0033367e220f07d935978` |
| `cases/as_fonly_d7_postd10_d98_f3_erratum_20260824/FREEZE.txt` | `cd3009992df83be446c2ffbab6249137e6fbbc7096f5b6d29a3cc885dbdd487e` |
| `replay_omitted_frobenius_carry.py` | `0bc6d3913fedf322a48a8d79acef1af56d6b3b41f078aa49ecf1b60bc0b463d8` |
| `README.md` | `f69b3aa744a8f94c42134176f6a27ad93f6ae8b37fb06e84bfa72c168931aefc` |

Quarantined predecessor hashes, unchanged:

| Artifact | SHA-256 |
|---|---|
| old report | `ff85614982fb26a7d8aba2859c7d1be6e3274ff8170114f23b247b5172fd0fc9` |
| old freeze | `f03fc06930c12398f714d5af60ed93374ffa80226bf1504d9429747cbdd6fa60` |
| old manifest | `1efda261bcd531fd4352c8b3f27ee2cafd77b7bf36dd31a9379d9083733a8f2b` |
| old generator | `243c357c18dbbe445f665621ceb5c748f96aa026cb73947fe38dd8b7af8e365e` |

---

## Independent recomputation

### 1. Integral residual after division by 27 — CONFIRMED

Let `P=x-x^3+3U+9C` and `Q=y+3V+9D` in `Z[x,y]`. Direct expansion of the Jacobian, with integer derivatives and no reduction, gives

```text
P_x = 1-3x^2+3 U_x+9 C_x,     P_y = 3 U_y+9 C_y,
Q_x = 3 V_x+9 D_x,             Q_y = 1+3 V_y+9 D_y,
```

and

```text
det J(P,Q)-1
  = 3(U_x+V_y-x^2)
    + 9((U_x-x^2)V_y-U_y V_x + C_x+D_y)
    + 27((U_x-x^2)D_y+C_x V_y-U_y D_x-C_y V_x)
    + 81(C_x D_y-C_y D_x).
```

The right-hand side is exactly `3L+9(K+C_x+D_y)+27M+81N` with the erratum signs. Four hundred random integer samples of `(U,V,C,D)` through total degrees six and seven left a zero remainder.

After `L=3L1`, this is `9E+27M+81N` with `E=L1+K+C_x+D_y`. After `E=3E1`, division by `27` is exact and yields `E1+M+3N`. That substitution was checked on eighty constructed families `U=9U_2`, `V=9V_2+x^2 y`, `C=3C_1`, `D=3D_1+x^4 y`; on the vertical witness with the correcting digit `C=2x^5+x^7`; and on the minimal pair `V=x^2 y`, `D=x^4 y`. All remainders vanished.

### 2. Single-cross formula, vanishing double, degree bounds — CONFIRMED

Write `U=U0+UF`, `V=V0+VF`. Expanding `K` gives a base term, a single cross, and a double product `UF_x VF_y-UF_y VF_x`. Every derivative of a degree-six Frobenius monomial is divisible by three, so the single cross is divisible by three and the double product by nine. Reducing the single cross by three recovers formula (4), including the seed `-x^2` in the `VF_y` slot. The same identity holds as a polynomial on the generic vertical normal form and on the generic `g`-endpoint normal form (zero remainder after `/3` mod 3). All nine Poisson products of `{x^6, x^3 y^3, y^6}` in `U` against the same three monomials in `V`, divided by three, vanish modulo three.

Symbolic support of (4) in the six named directions:

| Branch | Max degree | Degree 8 | Degree 9 | Directions present |
|---|---|---|---|---|
| vertical (degree-five layer zero) | 8 | 6 monomials | none | all six, at degrees 7 and 8 |
| `g` endpoint (`V_5=g x^5`) | 9 | 6 monomials | `x^4 y^5`, `x^7 y^2` | all six; degree 9 is `u6_0` and `u6_3` only |

The degree-nine `g`-endpoint polynomial is exactly `2 g u6_0 x^4 y^5 + g u6_3 x^7 y^2`. No single-cross monomial of degree ten occurs on either licensed branch, so the reviewed D10 row `M_10` is out of range.

### 3. Witnesses, and absence from the quarantined generator — CONFIRMED

The triangular inverse of `(P,Q,R,T,s,w,h)=(0,0,0,1,0,0,0)` is `t=1` and `p=q=r=s=w=h=0`. In the D10 normal form this is `U0=2x^4`, `V0=x^2 y+x^3 y`. With `UF=x^6` and `VF=0`,

```text
UF_x/3 = 2 x^5,     V0_y = x^2+x^3,
K_Frob/3 = 2 x^5(x^2+x^3) = 2x^7+2x^8,
```

and reduction modulo 3 does not change the coefficients. Direct `K(U0+UF,V0)-K(U0,V0)` reproduces the same polynomial. The omitted degree-eight coefficient is `2`.

On `g=1`, `U0=0`, `V0=x^2 y+x^5`, `UF=y^6`:

```text
K(UF,V0)-K(0,V0) = -12 x y^6-30 x^4 y^5,
(K_Frob)/3 ≡ 2 x y^6+2 x^4 y^5  (mod 3).
```

At `C=D=0` the mixed term `M` of this vertical witness is zero, so `2x^8` is not hidden inside `M`. `C_x+D_y` cannot cancel a degree-eight class.

The quarantined generator does not contain these terms under another name. Its high rows are `Mfull.get((i,total-i))` after solving the degree-five acceptance row that includes only the four `L/3` directions `fa,fb,fc,fd`. The allowed base set is `{p,q,r,s,t,w,h,fa,fb,fc,fd}` on the vertical branch and `{r,s,t,w,h,g,fa,fb,fc,fd}` on the `g` branch. The strings `u6_0`, `v6_6`, and `K_Frob` do not occur. The consumed D10 emitter builds `U,V` only in degrees 3, 4, 5, and its derivative drops every exponent divisible by three. The triangular coordinates `(P,Q,R,T)` are an invertible rewrite of `(p,q,r,t)` and do not create a sixth-degree Frobenius variable. The omitted class is an additive piece of `E1`, not a coordinate change of `M`.

### 4. Preservation and retraction boundary — CONFIRMED

Vertical D9. On the generic vertical normal form, (4) has no degree-nine monomial. After the D10 solve, `C_x+D_y` has degree at most six and the vertical base `K` has degree at most six, so the only possible degree-nine residual is `M_9`. The published section `ell=(-pr,-qr-pt,-qt,r^2,0,-rt,0,t^2,0)^T` satisfies `A9 ell = b9` at all `729` F3 points of `(p,q,r,s,t,w)`. The section survives.

Vertical D8 matrix, pivots, rank loci. Formula (4) is bilinear in first-digit derivatives and does not involve `C,D`. Eighty random samples confirm that `M` is independent of the six Frobenius coefficients modulo three, and that `K` is independent of `C,D`. The C,D-linear part of the residual at degree eight is therefore still `M_8`. The six named pivots `d7_0,c7_0,d7_3,c7_3,d7_6,c7_6` appear with F3-unit coefficients in `M_8` at the vertical witness; formula (4) cannot change those coefficients. The triangular change `(p,q,r,t)↦(P,Q,R,T)` is a base rewrite and is likewise untouched.

The published matrix (6) was exhausted on all `3^7=2187` F3 bases. Observed ranks are only `{0,2,3,5}`, with counts `(17,64,66,2040)`. The stated loci hold pointwise: rank `<=4` equals rank `<=3` equals vanishing of the three coefficients of `Delta=A^2+h^3 B`; rank `<=2` equals `V(h,P,Q)`; rank `<=1` equals rank `0` equals `V(P,Q,h,Rs,Ts+Rw,Tw)`. Ranks one and four do not occur. (The old `177147`-point rank split is `81` times this matrix-rank census, as it must be, because the coefficient matrix ignores the four-variable fibre. That consistency concerns ranks of `A`, not compatibility of `[A|b]`.)

Vertical D8 column and counts. The omitted class on the fibre-count-one representative is `2x^8` at degree eight. The frozen column is therefore not the source column, and every compatibility count, histogram, representative, and the hash `d7910730...` derived from it is retracted. A later regenerated census might or might not numerically coincide; it is not licensed by the frozen bytes.

`g`-endpoint. The stated D9 rows `g f_c=g f_d=0` are not the full degree-nine residual: adjoining (4) adds `2 g u6_0 x^4 y^5 + g u6_3 x^7 y^2`. The first of those involves the omitted pure direction `u6_0`; the second involves `u6_3=f_a`, which the old system named but did not put in those two rows. The `13 x 14` reduction, its fibre `(f_a,f_b)`, the census `954/4374`, the histogram, and the hash `119580e2...` are therefore invalid. Formula (4) also contributes degree-eight terms on this chart, so the old D8 `g`-endpoint column is likewise not source-honest.

All six directions. On the generic vertical branch every one of `u6_0,u6_3,u6_6,v6_0,v6_3,v6_6` appears in (4) at degrees 7 and 8. On the generic `g` endpoint all six still appear; `v6_6` only at degree 7, `u6_0` and `u6_3` at degree 9. The statement that the four displayed variables were the only relevant degree-six directions is false.

### 5. D10 unaltered; no extra claim — CONFIRMED

The reviewed D10 theorem uses the degree-ten coefficient of `(det J-1)/27` after the first residual is divisible by three, and identifies that coefficient with `M_10`. A single Frobenius cross reaches degree at most nine. A double cross at degree ten is zero after `/3` mod 3. The D10 producer already recorded this bound; the present erratum does not change it. The D10 hostile review remains **CONFIRMED**.

The erratum asserts no corrected census, no next divided carry, no full-D7 emptiness or nonemptiness, no lift or no-lift, no characteristic-zero statement, no counterexample, and no JC2 inference. Its successor sentence is a regeneration instruction, not a computed object. Frozen predecessor bytes are unmodified.

---

## Non-blocking remarks

- The published `7 x 5` matrix was not re-emitted from `M` in this review. Preservation is the structural fact that formula (4) cannot change any `C,D` coefficient, plus an independent F3 rank census of the published matrix. The original derivation of (6) from `M` remains an inherited, still-unreviewed compilation of the quarantined producer; it is not retracted by the omitted cross, and it is not hereby confirmed as a fresh D8 producer.
- Rank-locus membership was checked on every F3 point of the coefficient space, not as a radical-minor identity in the polynomial ring. Over F3 the geometric statement of (8) holds. An algebraic-closure restatement of those loci is a matrix claim about (6) and is unaffected by the omitted column.
- `v6_6` enters (4) on the `g` endpoint only at degree 7 in the generic normal form used here. That is enough to retract “only four relevant directions.” Witness (6) exhibits `u6_0`, not `v6_6`, exactly as written.
- Identity (3) requires both divisibility hypotheses. On the raw vertical witness with `C=D=0`, `L` is divisible by three but `E` is not (`E ≡ 2x^4+2x^6 mod 3`). The omitted D8 class is still `K_Frob/3`, which no later `C,D` of cap seven can cancel at degree eight. After the correcting digit `C=2x^5+x^7`, (3) holds and the degree-eight piece of `E1` remains `2x^8`.

---

## Refusal

This review confirms a source-honest retraction. It does not license the quarantined D9/D8 counts, does not replace them by a new census, does not advance a divided carry, and does not speak to JC2.
