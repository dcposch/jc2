# Hostile different-model review — TD6 moduli-uniform third-band gate

| Field | Value |
|---|---|
| Claim under review | Frozen TD6-MODULI-UNIFORM-THIRD-BAND: on the source-open moduli-zero curve `Q=-2S^2+2S+5D-3=0` left by the uniformity gate, with the fixed normalized reduced-boundary control, the new centered row `[s^0 t^0]J=1` cuts the curve to six licensed complex values of `S`, and the remaining coefficients of `[s^0]J-1` are inconsistent at all 18 pole-normalized conjugates via an exact left-syzygy with nonzero residue already at `t^4` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Hidden local-to-global step | none: emptiness of one fixed normalized reduced-boundary family at the centered Jacobian band is not a kill of SP-2, of a td=6 terminal class, of the broader boundary/dead-stretch/centering moduli, of landing, or of JC2 |
| Evidence tier | independent exact algebra over `Q`, `K=Q[S]/(F)`, and `E=K[A]/(A^3-α)` (registered replay; a second engine that does not import the third-band script: expansion of `3H^3-1`, resultant/norm, Rabin at three primes, reverse-row and reverse-lex GE, independently derived `[s^0]J` and `[r^1]J` compilers, unreduced left-null multiply); primary-source read of the completed first-band, numerical-next-row, moduli-uniformity, and paired-third-band hostile reviews |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T11:48:17Z – 2026-08-24T12:12:00Z |
| Python | 3.14.6; stdlib `fractions.Fraction` / `hashlib` only |
| Host | Darwin arm64 |

Producer inputs reread in full before any verdict:

- `xmodel/td6-moduli-uniform-third-band-20260824.md` (SHA-256 `0d3e2dc8e57b03060582d6906212ae707cb1d42b10416cff85117daa93b4ed7b`)
- `cases/td6_moduli_uniform_third_band_20260824/replay.py` (SHA-256 `7a21f9495d1e8784a9b253253430846ce882e2ce26f91815b31b6e061022cba8`)
- `cases/td6_moduli_uniform_third_band_20260824/FREEZE.sha256` (SHA-256 `0685b4412f6cb65f8b6556ede01d63c2652a508d08dc76ba57cf53b351254da9`)

All three frozen hashes match the launch prompt. The freeze file body is exactly the two producer hashes above. The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. No producer, canonical, ladder, or PDF file was edited. The quadratic next pole row was not compiled. No AWS work was launched.

Frozen dependency producers/reviews, reread against that basis:

- `xmodel/td6-two-chart-first-band-20260824.md` SHA-256 `cb373892233bddaf1b8fbf7722335ca43ee366b337151c3b244d2604d8168bf2`
- `cases/td6_two_chart_first_band_20260824/replay.py` SHA-256 `c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735`
- `xmodel/td6-two-chart-first-band-review-grok-20260824.md` SHA-256 `265c1103391e2bae889c018bb0637fe486e7292644c0295e4f9965e5085e7a25` (overall **CONFIRMED**; all six subclaims **CONFIRMED**)
- `xmodel/td6-two-chart-next-row-20260824.md` SHA-256 `32124d20ec84ef59d5b116639176b12053f5da6de1a9458dd4a2095d6b1618f0`
- `cases/td6_two_chart_next_row_20260824/replay.py` SHA-256 `0fc299a18a7ace6e5f64f98f38a71775331f226baac2e8ad258dd40e744fa5b8`
- `xmodel/td6-two-chart-next-row-review-grok-20260824.md` SHA-256 `12834c356c2c26243522b2609753370118ecd2c8ed87907033ca27e926d2ac2f` (overall **CONFIRMED**; all six subclaims **CONFIRMED**)
- `xmodel/td6-moduli-uniformity-gate-20260824.md` SHA-256 `499e95763759fe195ab1eba5fbf97bfb9d255bbf6fb2b090add938d92f1f3a06`
- `cases/td6_moduli_uniformity_20260824/replay.py` SHA-256 `55340fa662a20e1777eaa18fae2d26589c11ec7f3f2960f4a0a6efe015e7b6ab`
- `cases/td6_moduli_uniformity_20260824/FREEZE.sha256` SHA-256 `8d28ce7bc0ca31b51887457e9f5e33537f0ec86d950a6e0e21c78813a78994af`
- `xmodel/td6-moduli-uniformity-review-grok-20260824.md` SHA-256 `d95e0d684464c2f56b76ceb5cf32158d47ed907565216ff2974ca1d5f883730b` (overall **CONFIRMED**; all seven subclaims **CONFIRMED**)
- `xmodel/td6-paired-third-band-20260824.md` SHA-256 `a98de6d23ff2942360c328e4eeb6c08e24a122b0f9c964a5ad586cf0b009e9f2`
- `cases/td6_paired_third_band_20260824/replay.py` SHA-256 `5d05a6de17e3959ad221527ab74c7da77ba1e1980e8a7d86d0fd8cdca10d468a`
- `xmodel/td6-paired-third-band-review-grok-20260824.md` SHA-256 `3f2462b2c61d01a39769cc82cf3e9a04732e2bc824edea92bcb0eb9c449d3ad7` (overall **CONFIRMED**; all six subclaims **CONFIRMED**)

Cited canonical SP-2 / F1 / r9-M2 material, working-tree hashes on disk at review time:

- `ladder/SHEET6.md` SHA-256 `37f90bc8aff1ad977486cb5f414b88f983d4e7d46d771bd5ef34649085120f4d`
- `ladder/SHEET6-LROOT.md` SHA-256 `d8dc2eed9d386a74c76075fe265abee3ffae5b5c700341aa5134f5592fa0a358` (SP-2 ledger 187–200)
- `ladder/SHEET6-AF2.md` SHA-256 `c7f7601d5b72e2512561d12d160ac8e7458ee3954a8c18182b41ef6174053b3c`
- `ladder/SHEET6-AF3.md` SHA-256 `555363fde61291a0c689bbf9d789c01f73734e0c403d350d85ae2fd0ddab8099`

The third-band replay imports the moduli-uniformity compiler only after asserting SHA-256 `55340fa662a20e1777eaa18fae2d26589c11ec7f3f2960f4a0a6efe015e7b6ab`, which itself pins the next-row compiler at `0fc299a18a7ace6e5f64f98f38a71775331f226baac2e8ad258dd40e744fa5b8` and the first-band compiler at `c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735`. No imported-hash mismatch.

**Promotion.** Accept as `NORMALIZED-BOUNDARY-FAMILY-EMPTY-AT-CENTERED-BAND / STOP` of *this* one fixed normalized reduced-boundary family at the centered Jacobian band. Bank formula (2), the sextic `F`, the degree-18 field `E`, ranks `3508/3602`, `36/94`, `58`, pole rank `2/58`, homogeneous rank `25/58`, and the unreduced left-syzygy residual (5). Promote nothing else.

**Quarantine.** SP-2 is not killed. No td=6 terminal class is killed. The broader x-boundary, dead-stretch, centering, and other F1-pattern moduli remain open. JC2 is untouched. Exact `J=1` is not proved or disproved.

---

## Headline and subclaim table

Write `s=y^{-1}`, `x=s+s^2+s^3+t s^4`, F1 chart `x=q^{-5}`, `y=η q`, pole chart `x=r^{-25}`, `y=r^5+ζ r^{17}`, and on the survivor curve `D=(2S^2-2S+3)/5`.

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Inherited source typing is the retained SP-2/r9-M2 control: rectangles `(15,60)/(25,100)`, `p=t^{15}`, `q=t+t^{25}`, center `(1,1,1)`, zero dead stretch, reduced F1 `R(z)=(z-1)^2(z^2-Sz+D)`, source relation `L=25(1-S+D)`, pole normalization `L^8 A^3=9`. Every listed modulus other than the curve coordinate `S` (with `D` on `Q=0`) and the cubic pole scale `A` is fixed, not quantified | **CONFIRMED** | a new rectangle, x-boundary monomial, centering triple, dead-stretch slot, F1 orbit pattern, or pole shape in the third-band compiler; producer claiming those data are quantified by the emptiness certificate |
| 2 | Rebuilt transport has rank `3508/3602` (94 free), previous centered row rank `36/94` with unique compatibility a nonzero rational multiple of `Q`, leaving a consistent 58-dimensional affine family on `Q=0`; inherited pole row `[r^1](J-1)=0` is consistent of rank two. No imported-hash, coordinate-order, or pivot-denominator error | **CONFIRMED** | reverse-row rank ≠ 3508; previous tangent rank ≠ 36; a second nonzero compatibility polynomial not a multiple of `Q`; pole rank ≠ 2 or pole inconsistency over `E`; `factor_matrix` / `exact_solve` pivot sets disagreeing; a pivot lead involving `S,D,L,A` |
| 3 | Independently, `dx∧dy=s^2 ds∧dt` so `[s^0]J=[s^2](F_s G_t-F_t G_s)`; on the 58-family `f_{(2,1)}=0` and `f_{(3,0)}=H^3` with empty parameter dictionaries, hence `[s^0 t^0]J-1=3(1-S+D)^3-1`. Substituting `D=(2S^2-2S+3)/5` gives `F(S)/125` by exact polynomial expansion, with no free affine parameter in the constant row | **CONFIRMED** | two-form `s^1` or `s^3`; a surviving `f4`/`g4` term; a nonzero 58-parameter coefficient in `f_{(2,1)}`, `f_{(3,0)}`, or the `t^0` row; substitution of `Q=0` producing a polynomial other than `F/125`; interpolation used in place of expansion |
| 4 | `F` is primitive, has no rational root, `gcd(F,F')=1`, and is irreducible over `F_31` by Rabin, hence irreducible and squarefree over `Q`. Source-open Euclidean gcds with the divisors of `D=0`, `U=V`, `U=1` or `V=1` (i.e. `H=0`), `S+2`, and `H` are units. The sextic therefore leaves exactly six licensed complex `S` values and introduces or loses no boundary branch | **CONFIRMED** | a linear/quadratic/cubic factor of `F` over `Q`; Rabin gcd against `x^{31^2}-x` or `x^{31^3}-x` nontrivial; `F` sharing a root with any listed exclusion; the old quadratic `10S^2-35S+37` dividing `F` |
| 5 | `K=Q[S]/(F)` is a degree-6 field; `α=9/(25H)^8=243H/25^8` on `K`; `N_{K/Q}(α)=3^{28}/5^{96}` by both a multiplication determinant and a resultant. The 3-adic valuation 28 is not divisible by 3, so `α` is not a cube in `K`, so `A^3-α` is irreducible over `K` and `1,A,A^2` is a `K`-basis of the degree-18 field `E` at all six roots | **CONFIRMED** | `N(α)` a rational cube; `3H^3≠1` in `K`; `H=0` at a root of `F`; a factorization of `T^3-α` over `K`; a numerical embedding of `S` or `A` used as if it were the field |
| 6 | All forty coefficients of `[s^0]J-1` compile over `E`; 35 symbolic nonzero rows; homogeneous rank `25/58` in insertion and reverse-row GE; the insertion-order left-null has first contradiction at input row `t^4` and residual (5), including the nonzero coefficient `(136875/29)A`. Multiplying the certificate into the unreduced matrix reproduces that residual and a zero variable side | **CONFIRMED** | equation digest mismatch; nonzero-row count ≠ 35; homogeneous rank ≠ 25; unreduced variable side nonzero; residual ≠ (5); `A`-coefficient `0` in the advertised insertion-order certificate; the affine system consistent over `E` |
| 7 | Residual (5) is a nonzero element of the field `E`, hence nonzero at every one of the 18 pole-normalized conjugate embeddings. The quadratic pole band `[r^2](J-1)` is not compiled or used. Homogeneous rank 25 is consistent while the affine system is not; reverse-row GE remains inconsistent. No field-special rank jump, conjugate-specific vanishing, or affine/homogeneous mismatch alters the emptiness | **CONFIRMED** | an embedding of `E` sending (5) to 0; a conjugate at which the unreduced syzygy fails; producer using `[r^2](J-1)` as a load-bearing row; homogeneous system inconsistent, or affine system consistent, in a second GE order |
| 8 | Admissible conclusion is emptiness of this one fixed normalized reduced-boundary family at the centered band. It does not kill SP-2, any terminal class, the broader boundary/dead-stretch/centering moduli, or JC2. Smallest valid successor is a bounded deformation of one frozen datum that can enter (2) or (5) | **CONFIRMED** | producer promoting a class kill, a uniform-in-all-boundary-data theorem, exact `J=1`, or a further Jacobian band on this now-empty family as if it still carried information |

All remarks below are non-blocking unless marked otherwise. None changes a rank, a jet, a certificate coefficient, a hash, or a verdict.

---

## Replay

Registered command, rerun unmodified from the charged tree:

```sh
python3 cases/td6_moduli_uniform_third_band_20260824/replay.py
```

Exit code 0. Wall-clock `real 13.81`. Printed verdict:

```text
TD6-MODULI-UNIFORM-THIRD-BAND: PASS
verdict = NORMALIZED-BOUNDARY-FAMILY-EMPTY-AT-CENTERED-BAND
normalized_source_curve = -2*S^2+2*S+5*D-3=0
constant_row = 3*(1-S+D)^3-1
elimination_polynomial = 24*S^6-252*S^5+1170*S^4-3045*S^3+4680*S^2-4032*S+1411
elimination_degree = 6; squarefree = true; irreducible_mod_31 = true
source_exclusions_saturated = D, U-V, 1-U, 1-V, S+2, L, A
transport = rows 6547; rank 3508 / 3602; first_affine_dimension 94
previous_centered_band = rank 36 / 94; curve_affine_dimension 58
pole_normalization = L=25*(1-S+D); A^3=9/L^8; degree_18_source_field
inherited_pole_band = rank 2 / 58; consistent
centered_band = slots 40; symbolic_nonzero_rows 35; tangent_rank 25 / 58 over Q(S,A) residue field
left_syzygy = X0 degree 4; residual = (2495634-4154976*S+4405068*S^2-2488119*S^3+761922*S^4-105084*S^5)/3625 + (136875/29)*A
residual_nonzero_at_all_18_pole_normalized_conjugate_points = true
quadratic_pole_band_touched = false
centered_equations.sha256 = afcc6e2d51be0bc3d66f18afc030ba974aebc7c872732d04941bc4a319dd37a9
left_syzygy.sha256 = 6fffd7e470665e2af6f66a6f5b5dad1ddc066389bc4bdd8af8d4bdc845964aee
formula.sha256 = cf1a56c1d31a27ee06071d216aea8dd648ab6754e1888ea2fe4050163a2e2047
parent_replay.sha256 = 55340fa662a20e1777eaa18fae2d26589c11ec7f3f2960f4a0a6efe015e7b6ab
normalized_boundary_family_killed = true
SP2_killed = false
JC2_resolved = false
```

Canonical stdout SHA-256, including its final newline, recomputed independently from the live bytes (1380 bytes):

`c5c3417f3ba32574a778126de4cbc2bab5ee1f4528a17d3f86b106b68cbbd2ea`.

This matches the producer report and the launch-prompt frozen stdout hash. Arithmetic is `fractions.Fraction` on sparse monomials in `(S,D,L,A)` and on the residue field `E`. No CAS, no floating point, no modular sampling of the Jacobian system, no AWS.

A second engine, written for this review and not imported from the registered third-band script, rebuilt the 6547-row system from the hash-pinned first-band compiler with symbolic F1/r9 right-hand sides, and then diverged on purpose: (i) reverse-row-order least-index GE of the first-band matrix and of every subsequent tangent; (ii) reverse-lex GE of the 94-space previous centered tangent; (iii) an independently derived `[s^0]J` compiler from the two-form `[s^2](F_s G_t-F_t G_s)`; (iv) an independently derived `[r^1]J` compiler from the local wedge divided by `-25`; (v) expansion of `3(2S^2-7S+8)^3-125` rather than the producer substitution helper; (vi) resultant and multiplication-determinant norms of `α`; (vii) Rabin at `31`, `79`, and `97`; (viii) an unreduced left-null certificate in insertion order and a second one in reverse row order. Every stated rank, jet on the 58-family, certificate coefficient, and serialization hash matched. No assertion failed.

---

## 1. Source typing and what remains fixed

SP-2 from `SHEET6-LROOT.md:187–200`: chain

```text
F0 = (3,6,5,2,8) → F1 = (15,60,5,4,4)  (μ=2 IIa k=2, n=12) → (0,y),
```

type `(3,5)`, rectangles `(15,60)/(25,100)`, reduced F1 pattern `(η^5-c^5)^2 Π_2`. With the chain orbit normalized to `C=1` this is exactly `R(z)=(z-1)^2(z^2-Sz+D)`. The r9/M2 pole shape is the AF3 §4 family transported by `L=25(1-S+D)` and normalized by `L^8 A^3=9`. Zero dead stretch (the eleven coefficients at `r^6,…,r^{16}`) and common centering `(1,1,1)` are the same licensed specializations already confirmed by the first-band and moduli-uniformity reviews, not terminal-forced data.

What this emptiness certificate actually specializes, versus what it cuts:

| datum | status in this gate |
|---|---|
| rectangles `(15,60)/(25,100)`, IIa `μ=2,k=2,ν=5`, r9/M2 shape | fixed (inherited combinatorics) |
| x-boundary `t^{15}`, `t+t^{25}` | fixed (selected) |
| common centering `(c1,c2,c3)` | fixed at `(1,1,1)` |
| F1 chain orbit `C` | fixed at `1` |
| r9 dead stretch | fixed at zero |
| source relation `L=25(1-S+D)` | fixed (forced by first-band compatibility) |
| pole normalization `L^8 A^3=9` | fixed as a relation; the three cube roots of `A` are the cubic of `E` |
| curve coordinate `S`, with `D=(2S^2-2S+3)/5` | quantified, then cut to six values by `F` |
| 58 affine first-band + previous-centered parameters | quantified, then shown inconsistent |

No new chart, rectangle, or pattern is introduced. The hash-pinned first-band compiler is the same object whose rank `3508/3602` and x-boundary `{t^{15}}` / `{t^1,t^{25}}` were already confirmed. Claim 1 stands.

---

## 2. Parent transport, ranks `3508/3602` and `36/94`, pole rank two

The first-band homogeneous matrix depends on centering and chart supports, not on F1/pole *values*. With center frozen at `(1,1,1)` it is the confirmed rational matrix of rank `3508` in `3602` variables (`976+2626`, `6547` rows). Insertion-order least-index GE and reverse-row-order least-index GE both give rank `3508`. The `factor_matrix` pivot set equals the `exact_solve` pivot set, so the 94 free coordinates are not a row-order artefact. Unreduced pivot leads lie in `Q`, are never zero, have maximum denominator `9`, and involve none of `S,D,L,A`. Every `f`-transport row writes only into `[0,976)`; every `g`-transport row writes only into `[976,3602)`; the 40 first-Jacobian rows write into both blocks and nowhere else. The 94-space parameterization is an identity block on those free coordinates.

The previous centered row `[s^{-1}]J=0` has homogeneous rank `36` in insertion, reverse-row, and reverse-lex GE. Its unique symbolic compatibility polynomial is exactly `-(6/5)Q`, recovering the confirmed obstruction (11) of the uniformity gate. On `Q=0` the x-system is solvable of affine dimension `94-36=58`.

The inherited pole row `[r^1](J-1)=0` is the confirmed local wedge

```text
-3 p q1' - 2 p1 q' + 4 p' q1 + 5 p1' q
```

divided by the chart-determinant coefficient `-25`. Independently compiled on the 58-family and evaluated on `E`, it is consistent of rank two in both insertion and reverse-row GE. Homogeneous directions of this row do not depend on a coordinate permutation of `(S,D,L,A)`: pole leading supports remain `{1,6}` for `p` and `{0,5,10}` for `q0`. No denominator involving a moduli variable appears.

The numerical particular solution of `affine_parameterization` (built from the frozen first-band RHS `C=1,U=2,V=28/25,A=1/9`) is discarded; only its homogeneous kernel is used, composed with the symbolic particular solution of the moduli RHS. That split is legitimate because the matrix, and therefore the kernel, does not see those values.

Claim 2 stands.

---

## 3. Two-form, `f_{(2,1)}=0`, `f_{(3,0)}=H^3`, and the sextic

Chart Jacobian: `y=s^{-1}`, `x=s+s^2+s^3+t s^4` gives `x_s y_t-x_t y_s=s^2`, so `dx∧dy=s^2 ds∧dt` and

```text
[s^0] J_{x,y} = [s^2](F_s G_t - F_t G_s).
```

Expanding `F=p+s f1+s^2 f2+s^3 f3+⋯` and `G=q+s g1+s^2 g2+s^3 g3+⋯` with `p=t^{15}`, `q=t+t^{25}` produces exactly

```text
f1 g2' + 2 f2 g1' + 3 f3 q' - 3 p' g3 - 2 f1' g2 - f2' g1.
```

No `f4`/`g4` term enters `[s^2]`. The independent compiler of this two-form, run on the 58-family, produces the same forty-slot digest `afcc6e2d51be0bc3d66f18afc030ba974aebc7c872732d04941bc4a319dd37a9` as the producer.

On that 58-family, `f_2` at `t^1` has zero constant polynomial and empty parameter dictionary, and `f_3` at `t^0` equals `H^3` with empty parameter dictionary, where `H=1-S+D`. These two vanishings are *not* first-band invariants: dual evaluation of `[s^2 t^1]f` against the 3508-row factorization hits a free column, the 94-space particular solution of both jets still contains an `L^3 A` term together with a large `(S,D)` polynomial, and each jet has 16 nonzero 94-parameter directions. After the previous centered row those directions die and the constants collapse to `0` and `H^3`. The producer claims rigidity on the 58-family, which is the correct statement.

Consequently the only `t^0` contribution to `[s^0]J` is `3 f_{(3,0)}·[t^0]q'=3H^3`. The `f2' g1` slot, which would have contributed `-f_{(2,1)} g1(0)` at `t^0`, is killed by `f_{(2,1)}=0`. Subtracting the required value `1` gives (2). No 58-parameter can enter this scalar.

Substituting `D=(2S^2-2S+3)/5` into `H` gives `H=(2S^2-7S+8)/5`. Exact expansion, not interpolation,

```text
3(2S^2-7S+8)^3 - 125
 = 24S^6-252S^5+1170S^4-3045S^3+4680S^2-4032S+1411 = F(S),
```

so (2) becomes `F(S)/125`. Equivalently `3H^3=1` on `K`. At the already-killed algebraic point `H=3/25` of the paired-third-band gate one recovers `3H^3-1=-15544/15625`, matching that gate's residual, and the quadratic `10S^2-35S+37` does not divide `F`. Claim 3 stands.

---

## 4. Rabin, squarefreeness, six licensed values of `S`

`F` is primitive (`gcd` of coefficients `1`) and has no rational root (every divisor of `1411=17·83` over every divisor of `24` fails). Euclidean `gcd(F,F')` is a unit, so `F` is squarefree over `Q` and therefore over `C`.

Rabin's criterion for degree six over `F_p` is `x^{p^6}≡x mod F` together with `gcd(x^{p^2}-x,F)=gcd(x^{p^3}-x,F)=1`, provided `p` does not drop the degree. This holds at `p=31` (producer) and independently at `p=79` and `p=97`. Irreducibility over any one `F_p` implies irreducibility over `Q`. (It fails at some other primes, e.g. `37`, as Chebotarev permits; that is not a factorization over `Q`.)

Source-open saturation, all Euclidean gcds with `F` equal to a unit:

| divisor | polynomial | meaning |
|---|---|---|
| extra orbit zero | `2S^2-2S+3` | `D=0` |
| extra-orbit collision | `-3S^2+8S-12` | `U=V` |
| chain collision | `2S^2-7S+8` | `H=(1-U)(1-V)=0` |
| `E1=0` | `S+2` | `U+V=-2` at `C=1` |
| pole scale | `H` again | `L=25H=0` would kill `A^3=9/L^8` |

Since `F` is irreducible of degree six and squarefree, it has six distinct complex roots, none of which lies on those divisors. `L=25H≠0` and `A^3=9/L^8` then gives three nonzero cube roots of `A` at each root. No source exclusion removes a branch, and no extra boundary component is introduced. Claim 4 stands.

---

## 5. Degree-18 residue field and `N(α)=3^{28}/5^{96}`

`K=Q[S]/(F)` is a degree-6 field. On `K` one has `3H^3=1` by reduction of `F`, so

```text
α = 9/(25H)^8 = 9 H / (25^8 H^9) = 9 H / (25^8 · 1/27) = 243 H / 25^8.
```

The norm `N_{K/Q}(H)` equals the resultant of the monic `F/24` against `(2S^2-7S+8)/5`, which is `1/9`. Then

```text
N(α) = 243^6 · N(H) / 25^{48} = 3^{30}·3^{-2} / 5^{96} = 3^{28}/5^{96}.
```

A second computation, the determinant of multiplication-by-`α` in the basis `1,S,…,S^5`, returns the same value. The 3-adic valuation `28` is not divisible by three, so `N(α)` is not a cube in `Q`, so `α` is not a cube in `K`. Over a field of characteristic not three, `T^3-α` is therefore irreducible. The extension `E=K[A]/(A^3-α)` has degree 18 over `Q`, and `1,A,A^2` is a `K`-basis intrinsically — not by choosing a complex cube root at each of the six embeddings. Because `H≠0` on `V(F)`, one has `α≠0` at every root, so the three cube roots remain distinct and nonzero. Claim 5 stands.

---

## 6. Forty coefficients, rank `25/58`, unreduced left-syzygy

The independent two-form compiler produces 40 affine-linear slots (no quadratic monomial in the 58 parameters), of which 35 are symbolically nonzero, matching the producer. Evaluated on `E`, the degree-`0` slot vanishes identically (that is the definition of `F`). Insertion-order and reverse-row-order least-index GE of the homogeneous parts both have rank `25/58` and are consistent. The affine system is inconsistent: insertion-order GE first fails at input key `('X0', 4)`; reverse-row-order GE first fails at `('X0', 12)`.

The insertion-order left-null combination, multiplied directly into the *unreduced* coefficient matrix, has vanishing variable side and constant side equal to

```text
ρ = (2495634 - 4154976 S + 4405068 S^2 - 2488119 S^3
     + 761922 S^4 - 105084 S^5)/3625
    + (136875/29) A.
```

This is residual (5). The `A`-coefficient `136875/29` is a nonzero rational (`136875=3·5^4·73`), so in the `K`-basis `1,A,A^2` of `E` one has `ρ≠0`. The serialization of this combination is SHA-256 `6fffd7e470665e2af6f66a6f5b5dad1ddc066389bc4bdd8af8d4bdc845964aee`, matching the producer. Rank `25` describes only the homogeneous linear part; the inconsistent affine system has no solution space. Claim 6 stands.

---

## 7. Eighteen conjugates, unused quadratic pole band, no rank jump

`E` is a field, `ρ≠0` in `E`, and every `Q`-homomorphism `E→C` is injective. The 18 embeddings are the 6 roots of `F` times the 3 cube roots of `α`. None of them can send `ρ` to zero. The unreduced identity “combination · matrix = 0 and combination · rhs = ρ” is polynomial in the field elements, so it cannot fail at a specialization of an embedding even if a later GE pivot would have vanished there.

A reverse-row-order left-null combination is also nonzero in `E`. Its `A`-coefficient happens to vanish, so that residual lies in `K`; it is still a nonzero field element and still excludes all six values of `S` (hence all 18 conjugates). That is a second certificate, not a disagreement.

The quadratic next pole row `[r^2](J-1)=0` is not present in the third-band compiler, is not hashed, and is not used. The inherited *linear* pole row `[r^1](J-1)=0` remains consistent of rank two over `E` and is unnecessary for the contradiction: the new centered band is already empty on the larger 58-family.

Homogeneous rank is 25 in two GE orders; the affine system is inconsistent in two GE orders. There is no affine/homogeneous mismatch and no detected rank jump on the source-open locus `LA≠0`. Claim 7 stands.

---

## 8. Scope and the smallest valid successor

The verdict `NORMALIZED-BOUNDARY-FAMILY-EMPTY-AT-CENTERED-BAND` is exactly emptiness of the family in section 1 of the producer report: fixed rectangles, fixed x-boundary `p=t^{15}`, `q=t+t^{25}`, fixed center `(1,1,1)`, zero dead stretch, reduced F1 pattern with `C=1`, source relation, and pole normalization, at the centered Jacobian band. Printed flags `SP2_killed = false` and `JC2_resolved = false` match that scope. The one-dimensional complex moduli-zero curve is killed *only after* those normalizations; a different x-boundary monomial, a nonzero dead-stretch coefficient, a different centering triple, or a different reduced F1 shape is not addressed.

The quadratic pole band on this family is now information-free: the family is already empty. Repeating a further Jacobian coefficient at these 18 points cannot add information.

The smallest valid successor is therefore a bounded deformation of one frozen datum that can actually enter (2) or the syzygy (5), and an exact re-elimination of that one-parameter family. The producer names an additional x-boundary or dead-stretch coefficient. That is licensed. Common centering `(c1,c2,c3)` is equally frozen, and the 94-space (pre-centered-row) expressions for `f_{(2,1)}` and `f_{(3,0)}` see the chart multinomial, so a single centering coefficient is a legitimate alternate successor of the same size. Neither successor is an SP-2 kill, a terminal-class kill, or JC2. Before any such claim the campaign still has to justify that the retained x-boundary exhausts licensed x-direction data and to restore omitted Eggers-tree, other-infinity, mapping-degree, and landing conditions.

Claim 8 stands.

---

## Parameter, field, and GE caveats (non-blocking)

1. `f_{(2,1)}=0` and `f_{(3,0)}=H^3` hold on the 58-family, not as first-band dual invariants. The 94-space particular solutions still contain `±(11/250)L^3 A` plus a degree-three polynomial in `(S,D)`. The previous centered row is what kills those directions. The producer states the 58-parameter claim, which is the one used in (2).
2. `S+2` is the vanishing of `E1=2+S` at `C=1`, not an IIa source-open divisor. It is an extra saturation check; `gcd(F,S+2)=1`.
3. Rabin irreducibility is a property of the reduction at a good prime. Failure at `p=37` (and several others) is compatible with irreducibility over `Q`.
4. Unreduced pivot *leads* have maximum denominator `9`. Normalized pivot-*row entries* can have denominator `36`. The parent uniformity review's “maximum denominator 9” refers to leads, and that bound still holds.
5. The reverse-row syzygy residual lies in `K` rather than using the `A`-direction of `E`. Both certificates are valid; the advertised insertion-order residual (5) is the one hashed.
6. `SHEET6.md` / `SHEET6-LROOT.md` hashes match the moduli-uniformity review (campaign-status notes relative to the first-band freeze). The IIa/r9 combinatorics used above are the same ledger text at 187–200.

---

## Hashes

| artifact | SHA-256 |
|---|---|
| third-band report | `0d3e2dc8e57b03060582d6906212ae707cb1d42b10416cff85117daa93b4ed7b` |
| third-band replay | `7a21f9495d1e8784a9b253253430846ce882e2ce26f91815b31b6e061022cba8` |
| third-band freeze manifest | `0685b4412f6cb65f8b6556ede01d63c2652a508d08dc76ba57cf53b351254da9` |
| canonical replay stdout | `c5c3417f3ba32574a778126de4cbc2bab5ee1f4528a17d3f86b106b68cbbd2ea` |
| compiled centered equations | `afcc6e2d51be0bc3d66f18afc030ba974aebc7c872732d04941bc4a319dd37a9` |
| exact left-syzygy | `6fffd7e470665e2af6f66a6f5b5dad1ddc066389bc4bdd8af8d4bdc845964aee` |
| formula payload | `cf1a56c1d31a27ee06071d216aea8dd648ab6754e1888ea2fe4050163a2e2047` |
| imported moduli-uniformity replay | `55340fa662a20e1777eaa18fae2d26589c11ec7f3f2960f4a0a6efe015e7b6ab` |
| imported moduli-uniformity report | `499e95763759fe195ab1eba5fbf97bfb9d255bbf6fb2b090add938d92f1f3a06` |
| imported moduli-uniformity freeze | `8d28ce7bc0ca31b51887457e9f5e33537f0ec86d950a6e0e21c78813a78994af` |
| imported next-row replay | `0fc299a18a7ace6e5f64f98f38a71775331f226baac2e8ad258dd40e744fa5b8` |
| imported first-band replay | `c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735` |
| moduli-uniformity hostile review | `d95e0d684464c2f56b76ceb5cf32158d47ed907565216ff2974ca1d5f883730b` |
| paired-third-band hostile review | `3f2462b2c61d01a39769cc82cf3e9a04732e2bc824edea92bcb0eb9c449d3ad7` |
| first-band hostile review | `265c1103391e2bae889c018bb0637fe486e7292644c0295e4f9965e5085e7a25` |
| next-row hostile review | `12834c356c2c26243522b2609753370118ecd2c8ed87907033ca27e926d2ac2f` |

**JC2 scope.** This is an exact emptiness certificate for one fixed normalized reduced-boundary family at the centered Jacobian band. It neither realizes nor kills a terminal class, supplies no Keller pair, does not quantify broader boundary or dead-stretch moduli, and neither proves nor disproves the plane Jacobian conjecture.
