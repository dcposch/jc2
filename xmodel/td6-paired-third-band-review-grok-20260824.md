# Hostile different-model review — TD6 paired third band

| Field | Value |
|---|---|
| Claim under review | Frozen TD6-PAIRED-THIRD-BAND: at the explicit algebraic moduli-zero point `C=1`, `D=S-22/25`, `L=3`, `A=1/9` in `K=Q[S]/(10S^2-35S+37)`, the complete 56-dimensional paired-next-row family forces `[s^0 t^0]J=81/15625` identically, hence that single point is `K-EMPTY` for the third paired Jacobian band |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Hidden local-to-global step | none: one algebraic point of one retained SP-2/r9-M2 chart-pattern control is empty at the next centered Jacobian coefficient; this is not a kill of the moduli curve, of SP-2, of a td=6 terminal class, of landing, or of JC2 |
| Evidence tier | independent exact algebra over the quadratic field `K` (registered replay; a second engine that does not import the third-band script: all-`K` least-index GE in insertion order and in reverse row order, iterative chart powers, own `[s^0]J` and `[r^2]J` compilers, coefficientwise affine replay of all 6547 base rows and of the 38 previous next-row equations, hand two-form / jet formula / pole wedge, and direct global `J` at five affine points of the 56-space); primary-source read of the completed first-band, numerical-next-row, and moduli-uniformity hostile reviews |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T11:15:02Z – 2026-08-24T11:33:00Z |
| Python | 3.14.6; stdlib `fractions.Fraction` / `math` / `hashlib` only |
| Host | Darwin arm64 |

Producer inputs reread in full before any verdict:

- `xmodel/td6-paired-third-band-20260824.md` (SHA-256 `a98de6d23ff2942360c328e4eeb6c08e24a122b0f9c964a5ad586cf0b009e9f2`)
- `cases/td6_paired_third_band_20260824/replay.py` (SHA-256 `5d05a6de17e3959ad221527ab74c7da77ba1e1980e8a7d86d0fd8cdca10d468a`)
- `cases/td6_paired_third_band_20260824/FREEZE.sha256` (SHA-256 `f509e1c500ea7f565bafd5f558589a92435d1fde81a75f06d8abaa44c3a6896f`)

All three frozen hashes match the launch prompt. The freeze file body is exactly the two producer hashes above. The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. No producer, canonical, ladder, or PDF file was edited. The uniform successor on the moduli curve was not run. No AWS work was launched.

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
- `xmodel/td6-moduli-uniformity-review-grok-20260824.md` SHA-256 `d95e0d684464c2f56b76ceb5cf32158d47ed907565216ff2974ca1d5f883730b` (overall **CONFIRMED**; all seven subclaims **CONFIRMED**; landed during this review window)

The 94-dimensional first-band family and the 56-dimensional paired-next family were reconstructed over `K` in this review rather than imported as a witness. The moduli-uniformity confirmation is corroboration, not a load-bearing citation for the ranks or for `[s^0 t^0]J`.

**Promotion.** Accept as `K-EMPTY / STOP` of *this* single algebraic moduli point at the third paired Jacobian band. Bank the field `K`, the identity `[s^0 t^0]J=81/15625` on the whole 56-space, residual `-15544/15625`, and the observation that homogeneous rank `25` is not a solution-space dimension. Promote nothing else.

**Quarantine.** The one-dimensional complex moduli-zero locus is not killed. SP-2 is not killed. No td=6 terminal class is killed. JC2 is untouched. Exact `J=1`, landing, and broader x-boundary patterns remain open.

---

## Headline and subclaim table

Write `s=y^{-1}`, `x=s+s^2+s^3+t s^4`, F1 chart `x=q^{-5}`, `y=η q`, pole chart `x=r^{-25}`, `y=r^5+ζ r^{17}`, and `K=Q[S]/(10S^2-35S+37)` with `D=S-22/25`.

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | `K` is the genuine quadratic field of discriminant `-255`; source-open conditions `1-S+D=3/25`, `D≠0`, `U≠V`, `U,V≠1`, and `L^8 A^3=9` hold; the specialisation is exactly `C=1`, `D=S-22/25`, `L=3`, `A=1/9` on the survivor curve; no numerical embedding of `K` is used | **CONFIRMED** | `10S^2-35S+37` reducible over `Q`; `S=22/25` or `S=-9/25` a root; `3^8(1/9)^3≠9`; a `float`/`complex` embedding of `S`; the point missing the curve `-2S^2+2S+5D-3=0` |
| 2 | Rebuilt 6547-row system over `K` has rank `3508/3602` (94 free, identity block), affine-replays every base row, and after independently compiled `[s^{-1}]J=0` and `[r^1](J-1)=0` has rank `38/94` leaving a consistent 56-dimensional affine family; `t^{13}` of `[s^{-1}]J` vanishes identically on `K` | **CONFIRMED** | reverse-row rank ≠ 3508; a base row with a nonzero parameter polynomial; previous next rows inconsistent over `K`; free count ≠ 56; `[s^{-1}t^{13}]J` not identically zero |
| 3 | `[s^0]J=[s^2](F_s G_t-F_t G_s)=f1 g2'+2 f2 g1'+3 f3 q'-3 p' g3-2 f1' g2-f2' g1`; forty `t` slots are complete; `[s^0 t^0]J=81/15625` on the entire 56-space with all parameter coefficients zero, residual `-15544/15625`; the affine system is empty before a pivot | **CONFIRMED** | two-form `s^1` or `s^3`; a surviving `f4`/`g4` term in `[s^2]` of the local wedge; a free parameter in the `t^0` row; a 56-point with `[s^0 t^0]J` equal to `1` or to any other value; required constant `0` rather than `1` changing the residual while secretly making `J=1` possible |
| 4 | Parameter origin of the 56-family is a valid affine point (coefficientwise replay of all previously imposed rows). Independent global differentiation at that origin, and at four further 56-points, recovers `[s^0 t^0]J=81/15625` without using formula (4), and rechecks the two prior negative bands and `[r^0]J=1`, `[r^1](J-1)=0` | **CONFIRMED** | origin failing a previous row; a sampled 56-point with `[s^{-2}]` or `[s^{-1}]` nonzero, or with `[s^0 t^0]J≠81/15625`; global `J` disagreeing with the jet compiler at origin |
| 5 | Pole numerator (5) divided by `-25` is `[r^2]J`; induced supports `p1:{4}`, `p2:{2}`, `q1:{3,8}`, `q2:{1,6}`; parameter degree 2; 78 distinct quadratic monomials; tangent ranks `2/56` and combined `26/56`. Logically irrelevant: the centered constant row is already inconsistent | **CONFIRMED** | wedge sign disagreeing with path-A `[r^2]J`; extra nonzero `ζ` slot; quadratic degree ≠ 2; monomial count ≠ 78; producer treating tangent rank `26` as a solution-space dimension |
| 6 | All hashes and the exact registered stdout match. Verdict is `K-EMPTY` only at this algebraic point inside the fixed normalized SP-2 chart-pattern control. No uniform-curve, SP-2, terminal-class, landing, or JC2 claim. Smallest valid successor is a moduli-uniform `[s^0 t^0]J-1` on the curve `-2S^2+2S+5D-3=0` | **CONFIRMED** | stdout/equations/certificate SHA mismatch; producer promoting a class kill, a uniform-in-moduli theorem, exact `J=1`, or a further band at this now-empty algebraic point as if it still carried information |

All remarks below are non-blocking unless marked otherwise. None changes a rank, a jet, a certificate coefficient, a hash, or a verdict.

---

## Replay

Registered command, rerun unmodified from the charged tree:

```sh
python3 cases/td6_paired_third_band_20260824/replay.py
```

Exit code 0. Printed verdict:

```text
TD6-PAIRED-THIRD-BAND: PASS
verdict = K-EMPTY
previous_survivor = rank 38 / 94; dimension 56
current_x = scalar_slots 40; nonzero_rows 35; parameter_degree 1; tangent_rank 25 / 56
certificate = [s^0*t^0]J = 81/15625; required 1; residual -15544/15625
certificate.parameter_coefficients = 0
current_pole = scalar_slots 40; nonzero_rows 2 (zeta 1,6); parameter_degree 2; quadratic_monomials 78; tangent_rank_at_origin 2 / 56
combined_tangent_rank_at_origin = 26 / 56
current_equations.sha256 = c31a6eb89d34985028ddddb4e789941164980618b7fc2dc618e3243afe066103
certificate.sha256 = e07f7b476308fb5a411835bfa9b739b8ded26c36bbbe1ea4015e8d4d488640e4
independent_global_differentiation = pass
pointwise_only = true
terminal_class_killed = false
JC2_resolved = false
```

Canonical stdout SHA-256, including its final newline, recomputed independently:

`3ef256cb1a1afc9d0da1aa4617c4999734e2c05dd6e54da9cbba086b4d4ec8b8`.

This matches the producer report. Arithmetic is `fractions.Fraction` on the pair `(a,b)` representing `a+bS`, reduced by `S^2=(7/2)S-37/10`. No CAS, no floating point, no finite-field inference, no embedding of `K` into `C`.

The third-band script imports the moduli-uniformity replay only after asserting SHA-256 `55340fa662a20e1777eaa18fae2d26589c11ec7f3f2960f4a0a6efe015e7b6ab`, and uses it solely as the already hash-pinned next-row/first-band compiler chain. It does not import a pickled 94- or 56-witness.

A second engine, written for this review and not imported from the registered third-band script, rebuilt the 6547-row system from the hash-pinned first-band compiler with F1 right-hand sides replaced by `R(η^5)^3` and `R(η^5)^5` over `K`, and then diverged on purpose: (i) all matrix coefficients coerced to `K`, not mixed `Q`/`K`; (ii) reverse-row-order least-index GE in addition to insertion order; (iii) iterative multiplication for `x^i` in the centered chart, not the producer multinomial; (iv) an independent affine back-substitution that replays every base row as a 94-parameter identity over `K`; (v) independently derived `[s^{-1}]J`, `[s^0]J`, `[r^1]J`, and `[r^2]J` compilers; (vi) direct polynomial `J` at five points of the 56-family (`u=0`, `e_0`, `e_{27}`, `e_{55}`, all-ones). Every stated rank, jet, certificate coefficient, and serialization hash matched. No assertion failed.

---

## 1. Quadratic field, source-open conditions, specialisation

The minimal polynomial `10T^2-35T+37` is Eisenstein at `37`, hence irreducible over `Q`. Discriminant `1225-1480=-255=-3·5·17` is not a square, so `K` is a genuine imaginary quadratic field, not `Q`. The other root of `T` is `7/2-S` and the product of roots is `37/10`, which independently produces the multiplication rule

```text
S^2 = (7/2)S - 37/10
```

and the inverse of `a+bS` via the conjugate `a+(7/2)b-bS` divided by the norm `a^2+(7/2)ab+(37/10)b^2`. Both were re-derived and checked: `(2+3S)(2+3S)^{-1}=1`. Elements are stored as exact pairs `(a,b)` of rationals. A scan of the third-band replay finds no `float`, `complex`, `cmath`, `mpmath`, or `numpy`.

Specialisation. `C=1` is the already-licensed chain-orbit normalisation. `D=S-22/25` is the unique linear relation that forces `L=25(1-S+D)=3` while remaining on the survivor graph `D=(2S^2-2S+3)/5`: substituting yields exactly `10S^2-35S+37=0`. Independently on `K`,

```text
-2S^2 + 2S + 5D - 3 = 0,
(6/5)(5E_2 - 2E_1^2) = 0
```

with `E_1=2+S` and `E_2=1+2S+D`. So this point is on the moduli-zero curve, and the previous `[s^{-1}t^{13}]J` obstruction vanishes. `A=1/9` and `L=3` give `3^8(1/9)^3=9`, so the pole Jacobian normalisation holds. Pole leading patterns therefore coincide with the original first-band `p=27ζ^6-3ζ`, `q_0=243ζ^{10}-45ζ^5+5/3`; only the extra F1 orbits change.

Source-open, all checked on `K` and by evaluating the rational minimal polynomial at the excluded rationals:

| condition | check |
|---|---|
| chain collision `1-S+D=0` | `1-S+D=3/25≠0` |
| extra orbit `D=0` | `S=22/25` is not a root (`M(22/25)=1743/125≠0`) |
| extra-orbit collision `S^2-4D=0` | resultant identity `10Δ-M=-5S-9/5`; the only candidate `S=-9/25` is not a root (`M(-9/25)=6362/125≠0`); on `K`, `Δ=-9/50-(1/2)S≠0` |
| pole normalisation | `L^8 A^3=9` |

No source-open divisor vanishes. Claim 1 stands.

---

## 2. Reconstructed 94-family and 56-family over `K`

The left-hand side is the same rational first-band matrix as in the confirmed first-band review: rectangles `(15,60)/(25,100)`, center `(1,1,1)`, x-boundary `t^{15}` and `t+t^{25}`, zero dead stretch, pole patterns for `L=3`, `A=1/9`. Only F1 leading right-hand sides are replaced, by `R(η^5)^3` and `R(η^5)^5` with `R(z)=(z-1)^2(z^2-Sz+D)`. Both old and new patterns are polynomials in `η^5` of the same degree, so every possible nonzero new right-hand side occupies a nonempty packed row. Stricter F1 holomorphy rows keep rhs `0`.

Packed counts, independently: `6547` rows, `976+2626=3602` variables. Transport blocks: every `f`-transport row writes only into `[0,976)`; every `g`-transport row writes only into `[976,3602)`; of the 40 first-Jacobian rows, 18 write into both blocks, 14 into `f` only, 8 into `g` only, and none elsewhere. No second copy of any coefficient is introduced.

Insertion-order least-index GE over `K` and reverse-row-order least-index GE over `K` both give rank `3508`. Leftmost pivot columns agree, so the 94 free coordinates are uniquely determined. Nullity `3602-3508=94`. The affine map is constructed by descending back-substitution. Independently:

- each free coordinate `v_k` has form `(0,{k:1})` (identity block, hence injective);
- every one of the 6547 base rows evaluates to the constant right-hand side with identically zero parameter polynomial (hence exhaustive);
- the constant term of the map is the particular solution at free-variables-zero.

On this 94-space the first transverse jets are rigid, matching the F1-line formulae specialised to `K`:

```text
f1 = -3(2+S) t^{14} = (-6-3S) t^{14},
g1 = -(2+S)/5 - 5(2+S) t^{24},
[t^{13}] f2 = 3E_2 + 3E_1^2 = 63/50 + (63/2)S,
```

with empty parameter dictionaries. Independently compiled `[s^{-1}]J` therefore has vanishing `t^{13}` slot (the moduli obstruction is zero on `K`), and 36 remaining nonzero x-rows. Independently compiled `[r^1](J-1)` is supported at `ζ^3,ζ^8`. Packed together they give 38 rows of rank `38` in 94 parameters, hence a consistent 56-dimensional affine family. Coefficientwise replay of those 38 equations holds in all 56 parameters. Composing back into the 3602 global coefficients is the family used below.

The producer did not import a stale `Q`-parameterization of the original numerical point. It rebuilt the affine map over `K` from the replaced F1 right-hand sides. Claim 2 stands.

---

## 3. The `[s^0]J` formula, every `t` row, and the constant certificate

In the selected chart

```text
x = s+s^2+s^3+t s^4,     y = s^{-1},
dx = (1+2s+3s^2+4 t s^3) ds + s^4 dt,
dy = -s^{-2} ds,
dx∧dy = s^2 ds∧dt.
```

Therefore `J_{s,t}=s^2 J_{x,y}` and `[s^0]J_{x,y}=[s^2](F_s G_t-F_t G_s)`. Write `F=p+s f1+s^2 f2+s^3 f3+O(s^4)` and `G=q+s g1+s^2 g2+s^3 g3+O(s^4)` with `p=t^{15}`, `q=t+t^{25}`. The coefficient of `s^2` in the local wedge is

```text
f1 g2' + 2 f2 g1' + 3 f3 q' - 3 p' g3 - 2 f1' g2 - f2' g1.
```

Jets `f4,g4` first appear in `[s^3]` of `F_s` and `G_s`, so they are omitted correctly. Exact `J=1` requires this polynomial in `t` to equal the constant `1`: the `t^0` coefficient must be `1` and every `t^{k>0}` coefficient must vanish. The compiler subtracts `1` only from degree `0`. That is the correct required constant. Imposing `[s^0]J=0` instead would still be empty (`81/15625≠0`), but it would be the wrong equation; the producer imposes `=1`.

A priori `t`-degrees are at most `39` (each product in the formula is bounded by `15+24` or `14+25`). Forty slots `t^0,…,t^{39}` are therefore complete. Independently compiled rows, on the whole 56-space:

| `t` degrees | status |
|---|---|
| `0` | constant `81/15625`, no parameters |
| `1..10`, `12`, `14..34` | affine, nonzero constant at the origin |
| `11`, `35` | pure linear (vanish at the origin) |
| `12` | second parameter-free row: `-927/250+(729/250)S ≠ 0` |
| `13`, `36`, `37`, `38`, `39` | identically zero |

Nonzero affine rows: `35`. Parameter degree: `1`. No quadratic monomials, as required by rigidity of `f1,g1`. Homogeneous/tangent rank: `25/56`. Homogeneous nullity `31` describes only the linear part of those rows. The `t^0` row has no homogeneous part, so the affine system is inconsistent before any pivot is introduced. The producer states this distinction explicitly; this is not a rank/nullity claim for a solution space.

Because `f1` is purely `t^{14}` and `g1` is `const + t^{24}`, every channel in the jet formula except `3 f3 q'` and `-f2' g1` misses `t^0`. The identity on the 56-space therefore collapses to

```text
[s^0 t^0]J = 3 [t^0]f3 + (E_1/5) [t^1]f2,
```

and that combination is the constant `81/15625`. The compiled parameter polynomial for this row is exactly `{(): 81/15625}` before subtracting `1`, and `{(): -15544/15625}` after. Residual `81/15625-1=-15544/15625≠0`. Certificate payload

```text
[s^0*t^0]J=81/15625;required=1;residual=-15544/15625\n
```

has SHA-256 `e07f7b476308fb5a411835bfa9b739b8ded26c36bbbe1ea4015e8d4d488640e4`.

The second parameter-free row at `t^{12}` is an additional, independent emptiness certificate for `[s^0]J=1` (and even for `[s^0]J=0`). It is not needed for the producer’s `t^0` argument and is not claimed there. Claim 3 stands.

---

## 4. Global differentiation and the parameter origin

The 56-origin is the particular solution of the 38 previous next-row equations at free-variables-zero. Affine parameterization replays those 38 equations coefficientwise, so the origin is a point of the 56-space, not an extraneous slice. Reconstructing `(f,g)` from the constant terms of the composed 3602-forms, forming `f_x g_y-f_y g_x` in `K[x,y]`, and substituting the charts does not use formula (4) or (5).

| affine point | `[s^0 t^0]J` | `#` terms in `[s^0]J` | `max t` | `[s^{-2}]`, `[s^{-1}]` | `[r^0]J` | `[r^1](J-1)` |
|---|---|---:|---:|---|---|---|
| `u=0` | `81/15625` | 33 | 34 | empty | `{0:1}` | empty |
| `e_0` | `81/15625` | 33 | 34 | empty | `{0:1}` | empty |
| `e_{27}` | `81/15625` | 33 | 34 | empty | `{0:1}` | empty |
| `e_{55}` | `81/15625` | 34 | 35 | empty | `{0:1}` | empty |
| all-ones | `81/15625` | 35 | 35 | empty | `{0:1}` | empty |

The rest of the `[s^0]J` band *does* move (term counts 33→35, and both pole-`r^2` coefficients change). The `t^0` slot does not. Combined with the empty parameter dict on that compiled row, there is no `K`-point of this affine space at which `[s^0 t^0]J` equals `1`. At the origin, the full `[s^0]J` constant-term band and the `[r^2]J` constant-term band reproduce the jet compilers coefficientwise, including `/ -25` on the pole side.

The producer’s own “independent” check is this origin path; the five-point path is the genuinely independent exact check required here. Claim 4 stands.

---

## 5. Pole `r^2` audit, kept logically irrelevant

With `F=r^{-3}p+r^{-2}p1+r^{-1}p2+O(1)` and `G=r^{-5}q+r^{-4}q1+r^{-3}q2+O(r^{-2})`,

```text
[r^{-9}](F_r G_ζ-F_ζ G_r) = -3 p q' + 5 p' q,
[r^{-7}](F_r G_ζ-F_ζ G_r) = -3 p q2' - 2 p1 q1' - p2 q' + 3 p' q2 + 4 p1' q1 + 5 p2' q.
```

Chart determinant `det ∂(x,y)/∂(r,ζ)=-25 r^{-9}`, so `[r^k]J = [r^{k-9}]` of the local wedge divided by `-25`. In particular `[r^2]J=[r^{-7}]W/(-25)`, and `[r^2](J-1)=[r^2]J` because the constant `1` lives only in `r^0`. The compiler divides by `-25` and does not subtract `1`. Path-A global `J` at the origin reproduces both nonzero coefficients, including the division.

After substituting the 56-family, the only induced coefficient supports are `p1:{4}`, `p2:{2}`, `q1:{3,8}`, `q2:{1,6}`. A priori products occupy `ζ` degrees `{1,6,11}`; degree `11` cancels identically, leaving nonzero rows at `ζ^1,ζ^6` only. Audit, independently:

| item | result |
|---|---:|
| possible slots retained | 40 |
| nonzero rows | 2 (`ζ^1,ζ^6`) |
| parameter degree | 2 |
| quadratic monomial occurrences | 78 |
| distinct quadratic monomials | 78 |
| tangent rank at the origin | `2/56` |
| combined with centered tangents | `26/56` |

Degree 2 is structural: `p` and `q` are constant, while `p1 q1'` and `p1' q1` are quadratic in the 56 parameters. The 78 quadratic monomials are distinct; occurrence count and distinct count coincide, so the producer’s table word “distinct” is accurate. Combined tangent rank `26=25+2-1` records a one-dimensional overlap of homogeneous directions; it is not a solution-space dimension.

These figures are logically irrelevant to emptiness. The centered `t^0` row is already an inconsistent parameter-free affine equation. Claim 5 stands.

---

## 6. Hashes, stdout, scope, and successor

Imported and produced hashes, all matching disk:

| artifact | SHA-256 |
|---|---|
| third-band report | `a98de6d23ff2942360c328e4eeb6c08e24a122b0f9c964a5ad586cf0b009e9f2` |
| third-band replay | `5d05a6de17e3959ad221527ab74c7da77ba1e1980e8a7d86d0fd8cdca10d468a` |
| third-band freeze manifest | `f509e1c500ea7f565bafd5f558589a92435d1fde81a75f06d8abaa44c3a6896f` |
| canonical replay stdout | `3ef256cb1a1afc9d0da1aa4617c4999734e2c05dd6e54da9cbba086b4d4ec8b8` |
| compiled current equations | `c31a6eb89d34985028ddddb4e789941164980618b7fc2dc618e3243afe066103` |
| one-row certificate payload | `e07f7b476308fb5a411835bfa9b739b8ded26c36bbbe1ea4015e8d4d488640e4` |
| imported moduli report | `499e95763759fe195ab1eba5fbf97bfb9d255bbf6fb2b090add938d92f1f3a06` |
| imported moduli freeze manifest | `8d28ce7bc0ca31b51887457e9f5e33537f0ec86d950a6e0e21c78813a78994af` |
| imported moduli replay | `55340fa662a20e1777eaa18fae2d26589c11ec7f3f2960f4a0a6efe015e7b6ab` |
| imported next-row replay | `0fc299a18a7ace6e5f64f98f38a71775331f226baac2e8ad258dd40e744fa5b8` |
| imported first-band replay | `c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735` |

Equations digest and certificate digest were recomputed from the independent compilers and match the producer.

What is proved: every `K`-point of the 56-dimensional affine space of pairs in the fixed rectangles with this centering, this F1 pattern at this algebraic `(S,D)`, this zero dead stretch, this r9/M2 member, `[s^{-2}]J=0`, `[s^{-1}]J=0`, `[r^0]J=1`, and `[r^1](J-1)=0` satisfies

```text
[s^0 t^0] J(f,g) = 81/15625 ≠ 1.
```

Consequently `[s^0]J=1` is empty on that space, and the paired system `[s^0]J=1` together with `[r^2](J-1)=0` is empty over `K`. That is exactly `K-EMPTY` for this single algebraic point. The opposite-side `r^2` row is well-defined, quadratic, and rank-2 at the origin, but is not needed for emptiness.

What is not proved, and is not claimed:

- emptiness of `[s^0]J-1` as a function on the whole source-open curve `-2S^2+2S+5D-3=0`;
- a kill of SP-2, of any of the other seven td=6 terminal classes, or of the book 8;
- a polynomial with `J≡1`, a landing theorem, a pairing of complete Eggers trees, a counterexample, or a JC2 decision.

The point (1) is dead, so appending another band there adds no information. The smallest valid successor is a **moduli-uniform third band** on

```text
-2S^2 + 2S + 5D - 3 = 0:
```

derive `[s^0 t^0]J-1` as an exact function on that curve and determine its remaining zero locus before handling the quadratic pole row. A nonzero formula on the whole source-open curve would eliminate this normalized boundary-pattern control; a new zero would provide the next algebraic point. Even uniform elimination of this curve would not yet kill SP-2 without quantifying broader licensed x-boundary data and restoring all omitted global Eggers, infinity, mapping-degree, and landing conditions.

Claim 6 stands.

---

## Attacks that did not fire

The prompt asked for a sign/normalisation error, an incorrect required constant row, a hidden numerical embedding, a stale affine parameterization, or a rank/nullity claim made for an inconsistent affine system. Independently:

1. **Sign of formula (4).** Re-derived from `dx∧dy=s^2 ds∧dt` and the `s^2` coefficient of `F_s G_t-F_t G_s`. Matches the compiler, including scales `3`, `75=3·25`, and `-45=-3·15`. Path-A global `J` agrees at five 56-points.
2. **Required constant `1`.** For `J≡1`, `[s^0]J` must be the constant polynomial `1`. Subtracting `1` only from `t^0` is correct. The residual is `81/15625-1`, not `81/15625-0`. Emptiness would hold either way, but the stated residual is the `J=1` residual.
3. **Hidden numerical embedding.** `S` is the pair `(0,1)`. No `float`/`complex`. Inverse uses the exact conjugate. Discriminant `-255` is not a square.
4. **Stale affine parameterization.** The 94-map is rebuilt over `K` from replaced F1 rhs; the 56-map is rebuilt from independently compiled previous next rows. Coefficientwise replay of all 6547+38 equations holds. The original numerical point had `[s^{-1}t^{13}]J=-18858/3125`; here that slot is identically zero.
5. **Rank/nullity of an inconsistent system.** Homogeneous rank `25` and nullity `31` are stated as properties of the linear part only. The affine system has no solution space. The `t^0` row never becomes a pivot.
6. **Mixed `Q`/`K` arithmetic in `exact_solve`.** The producer keeps a `Q`-matrix and a `K`-valued rhs. The second engine coerced every matrix coefficient to `K`. Ranks, jets, and hashes agreed, so the mixed-type path did not silently drop a `K` term.
7. **Constructor trap `K(-1,25)` versus `K(-1/25)`.** The producer scales the pole wedge by `K(Q(-1,25))`, i.e. the rational `-1/25`, not `-1+25S`. Path-A `[r^2]J` confirms the division.

Copied-coefficient / missing-variable hunt that failed to fire: `g` transport mentioning an `f` index, or `f` transport mentioning an index `≥976`, none except the 18 genuine mixed first-Jacobian rows; a second `a_{ij}` for the pole chart distinct from the x-chart, none; a missing global variable that could have moved `[s^0 t^0]J`, reverse-row free set agrees with insertion order, identity block holds, and extra-point term counts move while `t^0` does not.

---

## Source caveats (none load-bearing)

1. The present theorem is a statement about one affine space over `K` constructed from the first-band compiler with replaced F1 rhs. The first-band and next-row hostile reviews have confirmed that compiler; the moduli-uniformity review has confirmed the algebraic point is source-typed and finite-band nonempty at the previous pair of rows. This review re-obtained the 94- and 56-families over `K` by a second GE, so those confirmations are discharged rather than left open. Residual risk is the usual one for finite exact linear algebra: an undetected transcription error in a chart identity that both engines share. The two-form, the jet formula, the pole wedge, and `/ -25` were re-derived by hand and checked against path-A global `J`, which does not use those formulae.
2. Working-tree hashes of `ladder/SHEET6.md` and `ladder/SHEET6-LROOT.md` have moved since the first-band freeze (`37f90bc8…` and `d8dc2eed…` at review time) because of uncommitted campaign-status notes. No canonical campaign file was used as evidence beyond inherited source-typing of the specialisation, which the moduli-uniformity review already re-checked against the same working tree.
3. Degrees `t^{13}` and `t^{36}…t^{39}` of `[s^0]J` vanish identically on this family. Direct expansions never exceeded `t^{35}`. The identically zero `t^{13}` slot is the previous obstruction, now killed by sitting on the moduli curve.
4. No good-prime probe was run by the producer. An exact characteristic-zero identity with empty parameter support is strictly stronger; reverse-row rank was used only to pin the *linear* first-band rank from a second pivot order, not to infer emptiness.

---

## Promotion advice

**Accept** the report as a bounded `K-EMPTY / STOP` of the third paired Jacobian band at this one algebraic moduli-zero point of the retained SP-2/r9-M2 chart-pattern control. Bank:

- field `K=Q[S]/(10S^2-35S+37)`, specialisation `C=1`, `D=S-22/25`, `L=3`, `A=1/9`;
- first-band rank `3508/3602` over `K`, previous next-row rank `38/94`, affine dimension `56`;
- certificate `[s^0 t^0]J=81/15625` with vanishing parameter support, residual `-15544/15625`, SHA-256 `e07f7b476308fb5a411835bfa9b739b8ded26c36bbbe1ea4015e8d4d488640e4`;
- current-equation serialization `c31a6eb89d34985028ddddb4e789941164980618b7fc2dc618e3243afe066103`;
- homogeneous tangent ranks `25, 2, 26` and the observation that tangent rank misses the emptiness;
- the extra parameter-free row `[s^0 t^{12}]J=-927/250+(729/250)S≠0`, not needed for the certificate.

**Do not accept** as any of the following:

- emptiness of `[s^0]J-1` on the whole source-open curve `-2S^2+2S+5D-3=0`;
- a kill of SP-2 or of any other td=6 terminal class;
- a polynomial Keller pair, exact all-order `J=1`, a landing/coverage theorem, or a JC2 decision;
- a reason to compile further bands at this algebraic point.

Successor work, if any, has to treat `[s^0 t^0]J-1` as an exact function on that curve, inside the same fixed rectangles, keeping the F1-to-r9 transport relation. Compatibility of a nonempty residual zero with all displayed Jacobian rows would still need the omitted global Eggers and landing conditions before it represented a terminal class.

---

## Explicit exclusions

This review does not:

- edit the producer file, the replay, `FREEZE.sha256`, the moduli-uniformity case, the first-band or next-row cases, `ladder/SHEET6-LROOT.md`, `AUDIT.md`, `APPROACHES.md`, or `refs/sigray_full.pdf`;
- run the uniform successor on the moduli curve, append later Jacobian bands, or launch AWS;
- treat other uncommitted xmodel artifacts (AS109, secant, fresh-connection, …) as evidence;
- assert emptiness, or nonemptiness, of `[s^0]J=1` at any other point of the moduli curve;
- assert anything about extra F1 orbits as Jacobian conditions, finite fibers, mapping degree, or the (22) ledger of a global pair.

Frozen producer SHA-256, recomputed on disk at review time:

```text
a98de6d23ff2942360c328e4eeb6c08e24a122b0f9c964a5ad586cf0b009e9f2  xmodel/td6-paired-third-band-20260824.md
5d05a6de17e3959ad221527ab74c7da77ba1e1980e8a7d86d0fd8cdca10d468a  cases/td6_paired_third_band_20260824/replay.py
f509e1c500ea7f565bafd5f558589a92435d1fde81a75f06d8abaa44c3a6896f  cases/td6_paired_third_band_20260824/FREEZE.sha256
55340fa662a20e1777eaa18fae2d26589c11ec7f3f2960f4a0a6efe015e7b6ab  cases/td6_moduli_uniformity_20260824/replay.py
c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735  cases/td6_two_chart_first_band_20260824/replay.py
```
