# K16 DEP locus (Card C): the τ = 0 part of the cone is the z-type locus J(Q,P) = −c·z, not the dependent-pair locus

**Lane:** `k16-dep-locus-fable5-20260903`  **Date:** 2026-09-04  **Basis:** `fd5b2b88`
**Drivers/artifacts:** `box/k16dep-20260903/` (33 files, manifest `SHA256SUMS`, sha256 `3ca3213f814386511858c78e4befeafb41f3952c321eb3cb44d60868c1f85651`).

## 0. Verdict

- **DEP at t = 2: REFUTED (exact, PROVED-HERE).**  At `y = 1/5`, on the b3-axis cone point
  `b3 = 1, b4 = 0`, the actual ansatz pair `(Q,P)` of the chart (degrees 20, 28 in `(γ,π)`),
  rebuilt from the residual point through the proved spine, has

  ```text
  J(Q,P) = Q_γ P_π − Q_π P_γ = (7/625)(π − γ) = −c·z,   c = −yg = −7/625,  z = π − γ.
  ```

  Not `0`.  The same holds for every `b3` (explicit family in §3) and at the origin of every fibre
  tested (`t = 2..6`).  §1.2 of my round submission is withdrawn.
- **What the τ = 0 part of the cone IS (PROVED-HERE, every t, every residual point p):**

  ```text
  J(Q_p,P_p) = c·γ + π·E_t(h),     E_t(h) := Σ_{k=0}^{2t−1} T_{t,k}(p) h^k,     c = −yg.
  ```

  Hence `V(I_{t,+}) = { p : J = cγ + T_{t,0}(p)·π }` (the Jacobian is a *linear form*), and
  `τ_t(p) = 0 ⟺ J = c(γ − π) = −c z` ("z-type pair", the phrase already used for the axis in the
  Fable terminal-proof report §3).  Lemma CONE is the special case `T_{t,0}(p) = 0` after rescaling.
- **Dependent pairs do not exist in the chart at any t (PROVED-HERE):** the `π^0` coefficient of
  `π³·J` in `K[h][π^{±1}]` is `y g (h − b4) ≠ 0` for *every* choice of `U,R,V,S,T,b_i`.  So the
  literal dependent-pair system of step (4) is inconsistent identically; **DEP-EMPTY holds
  vacuously at t = 8** (and at every t) and decides nothing about (V0).
- **The decision-grade replacement.**  `(V0) ⟺ (T) ∧ Z-EMPTY_t`, with
  `Z-EMPTY_t : V(I_{t,+}) ∩ {τ_t = 0} = {0}`.  Z-EMPTY is the cone with one more homogeneous
  generator (`T^hom_{t,0}`), i.e. **not a smaller system**; it fails at `t = 2, y = 1/5`, holds
  for `t = 3..7` (cone `{0}`), and at **t = 8** this lane proves its `b4 = 0` half
  (`dim 0` mod 32003 in 34 s, promoted by the properness lemma) while the `b4 = 1` chart
  (17 generators, 7 variables) is **INCONCLUSIVE_TIMEOUT** at the 590 s foreground cap
  (`std` and `slimgb`); the top-tail cone and the full z-system also timed out.
- **Bonus (PROVED-HERE via 5.1): RESIDUAL-ZERO at t = 8** (`⟨T_1..T_15, b4⟩` has `dim 0`
  mod 32003, root 11288, 21 s).
- Nothing here is an exit-price assertion; no `charge_basis` line is due.

## 1. Custody

The receipt `xmodel/k16-dep-locus-fable5-20260903.run.v2` was parsed with `awk`; the paired
`charged_input_<i>_sha256`/`_basename` fields produced `box/k16dep-20260903/manifest.sha256` and
`sha256sum -c` returned `OK` for **15/15** frozen inputs (`manifest.check.log`).  No digest was
retyped.  Beyond the frozen inputs, the only repository files read were sealed sources of the
chart: `box/k16t56-20260903/t_order_system.py` (the frozen ansatz), the sealed
`xmodel/k16-middle-spine-sol56-20260903.md` §2 (the Laurent identities), and the sealed Fable
terminal-proof drivers/rows in `box/k16terminal-fable5-20260903/` (the exact `t = 8` rows reduced
mod 32003).  No ledger, `jc2-lean`, or in-progress lane report was read or edited.  All new files
are in `box/k16dep-20260903/` and this report.  Every job ran in the foreground; the tool's hard
cap is 600 s per call, so `timeout 590` replaced the prescribed `timeout 1800` (stated per run).

## 2. Step (3) first: the chart pair and the Laurent identity, line by line

Frozen ansatz (`t_order_system.py`, `q = 2t+1`, `e = 3t+1`):

```text
z = π − γ,  B = πz + b1π + b2,  A = πB + b3,  h = πA + b4 = π⁴ − γπ³ + b1π³ + b2π² + b3π + b4,
Q = U(h) + A·R(h) + y·B,      P = V(h) + A·S(h) + B·T(h) + g·z          (Sol 17(qqq) (2.1)),
```

with `U, R, V, S, T ∈ A_t[X]` (`X` stands for `h`), `y` a root of `H_t`, `g = g₃` the normalizer
scalar.  Since `A = L/π`, `B = L/π² − b3/π`, `z = −b1 − b2/π − b3/π² + L/π³` (`L = h − b4`), the pair
is `Q = U + Q1/π + Q2/π²`, `P = P0 + P1/π + P2/π² + P3/π³` with (Sol (2.2))

```text
Q1 = LR − yb3,  Q2 = yL,  P0 = V − gb1,  P1 = LS − b3T − gb2,  P2 = LT − gb3,  P3 = gL.
```

`h` and `π` are algebraically independent (`γ = (π⁴ + b1π³ + b2π² + b3π + b4 − h)/π³`), and
`J(h,π) = h_γ = −π³`, so `J_{γ,π}(Q,P) = −π³·(Q̃_h P̃_π − Q̃_π P̃_h)` and collecting powers of `π`
gives the identity (prime = `d/dX`)

```text
π³·J(Q,P) = −( D0·π⁴ + D1·π³ + D2·π² + D3·π + D4 )|_{X=h},                              (2.1)
D0 = Q1P0' − U'P1,   D1 = 2Q2P0' + Q1P1' − Q1'P1 − 2U'P2,   D2 = −3U'P3 + Q1P2' − 2Q1'P2 + 2Q2P1' − Q2'P1,
D3 = Q1P3' − 3Q1'P3 + 2(Q2P2' − Q2'P2),   D4 = 2Q2P3' − 3Q2'P3 = −ygL   (identically).
```

Because `cγ·π³ = −(−cπ⁴ − cb1π³ − cb2π² − cb3π + cL)`, the requirement `J = cγ` is exactly Sol's
five identities `D0 = −c, D1 = −cb1, D2 = −cb2, D3 = −cb3, D4 = cL`, and `D4` forces `c = −yg`.
**The scalar `g = g₃` is therefore both the leading-form scalar and the Jacobian constant** — the
gap I had flagged resolves *against* DEP: on the spine, (D3), (D2), (D1) are solved identically in
`w = 1/h` (Fable §2.1: their `w`-degrees are `t−1`, `2t`, `3t+1` and every coefficient is a
recurrence step or the `b1` pivot; the gauge fixes `T(0)`), so **`D1 = −cb1, D2 = −cb2, D3 = −cb3,
D4 = cL` hold at every residual point**, while `D0 = yg − E_t(h) = −c − E_t(h)` (its `w^0`
coefficient vanishes by (5.7a), `w^1..w^{2t+1}` are the pivots, `w^{2t+2}..w^{4t+1}` are the rows).
Substituting in (2.1):

```text
J = −D0·π − c(b1 + b2/π + b3/π² − L/π³) = (c + E_t(h))π − c·z = c·γ + π·E_t(h).            (2.2)
```

So `Δ ≡ 0 ∧ (D1)–(D3)` is **not** `J ≡ 0`; it is `J = −c·z`.  Controls (`identity_check.py`,
`laurent_coeff_check.py`, symbolic coefficients): the five decompositions, `h_γ = −π³`, (2.1),
`D4 = −ygL`, the `cγ` translation, and (2.2) all print `True`; in `K[H][π^{±1}]` the `π^0`
coefficient of `π³J` is `yg(H − b4)`, so `J ≡ 0` is impossible for every chart pair.

## 3. Step (1): t = 2, y = 1/5, rebuild of (Q,P) and exact J

`rebuild_pair.py` replays the proved spine (`laurent_spine.py` / Sol (2.2)–(2.13)) at a numeric
residual point in exact arithmetic (`Fraction` on a rational fibre, `GF(p)` on a modular root),
solving the `2t+1` affine pivots by evaluation (affinity asserted by a third evaluation), then builds
`Q, P ∈ K[γ,π]` from `U, R = LC, V = ∫P0' + gb1, S, T` and the frozen `A, B, z, h`, and
differentiates directly (bivariate dictionaries; degrees `4q = 8t+4`, `4e = 12t+4` asserted).
Controls at every point: the four/`2t` banked rows (`terminal_laurent_t2.json`, sign `R = −E`)
matched exactly at every `t = 2` point on both fibres; the `t = 4` record matched mod 32029 at a
random point (`t4_json_control.log`); `D0..D4` recomputed from the pieces satisfy
`D0 = −c − E, D1 = −cb1, D2 = −cb2, D3 = −cb3, D4 = cL` (`LAURENT_IDENTITY ... OK`).

At `t = 2, y = 1/5` (`d = −1`; normalizer `g1 = 7/5, g2 = 14/25, g = 7/125, c = −7/625`), the axis
point `b3 = 1, b4 = 0` gives pivots `c1 = 0, u2 = 0, u3 = −1/2, u4 = 0, b2 = 0`, `b1 = 0`, rows
`T = (7/625, 0, 0, 0)`, i.e. `τ_2 = T_{2,0} + c = 0`, and

```text
J(Q,P) = −(7/625)·γ + (7/625)·π = −c·z      (26-term Q of degree 20, 47-term P of degree 28).
```

The whole axis is the explicit family (symbolic `b3`, verified in `identity_check.py` (III)):

```text
h = π⁴ − γπ³ + b3π,   A = π³ − γπ² + b3,   B = π² − γπ,
Q = h⁵ − (b3/2)h² + A·h² + B/5,
P = h⁷ − (7/20)b3·h⁴ + A·((7/5)h⁴ + (7/25)b3·h) + (14/25)B·h² + (7/125)(π − γ),
J(Q,P) = (7/625)(π − γ)   for every b3.                                                       (3.1)
```

(`u3 = ρ₂b3 = −b3/2`, `σ₂ = 7/25`, `ν₁ = −7/20`, `ν₂ = 0`, `T = g2h²` — the axis lemma values.)
Numeric checks at `b3 = 3, −2/7` and with the gauge `B0 = 5/3` (`P ↦ P + (B0/y)Q`; rows and `J`
unchanged, `P` gets 73 terms) agree.  Off the axis (`(b3,b4) = (2,3), (0,1), (−5/2,1/3)`, both
fibres) and at random points mod `p` for `t = 3,4,5,6` (`controls.log`), `J` is a polynomial of
degree `8t−3` with up to 275 terms and `J − (cγ + πE_t(h)) = 0` every time (`FORMULA_OK`);
at the origin of every `t` the pair is z-type (`J = cγ − cπ`, `E = −c`).  On `y = 2/5` the axis
point has `T_{2,3} = −28/625` and `J = (28/625)(γ − π)^3π^{10} + …` (not a cone point), as banked.

**Verdict (1): DEP REFUTED at t = 2, y = 1/5** — `J ≠ 0`, value `(7/625)(π − γ)`.

## 4. Step (2): no H exists; what the τ = 0 part is; t = 3

No `H, φ, ψ` with `P = φ(H), Q = ψ(H)` can exist (§2, `J ≢ 0`), so step (2) is void.  What the
τ = 0 cone points are instead: **z-type pairs**, `J(Q,P) = −c·z = c·(γ − π)`.  In the sheared
coordinates `γ' = γ − π` (a plane automorphism) these are monomial-Jacobian pairs `J = c·γ'` with

```text
h = π³(b1 − γ') + b2π² + b3π + b4      (the π⁴ term is absorbed; top form −γ'π³),
```

i.e. the same two places at infinity (`[1:0]` triple, `[1:1]` simple), but the Jacobian line
`γ' = 0` now passes *through the simple place*, whereas the (8.1)-type pairs have `J = cγ` with
`γ = 0` through neither.  The τ = 0 condition `D0 ≡ 0` is the factorization
`Q1·V' = U'·P1` in `A_t[X]` (`V'/U' = P1/Q1 =: F`; on the axis (3.1) `F = (7/5)h²`, at the origin
`F = g1h^t`) — a proportionality of the first Laurent correction to the differential of the
leading pair, not an algebraic dependence.  The torus orbit of a cone point `p` realizes every
linear form `cγ + μπ` with `μ ≠ −c` when `τ_t(p) ≠ 0` (Lemma CONE, `μ = 0`), and only `μ = −c` when
`τ_t(p) = 0`.

**t = 3.**  The cone is `{0}` (banked exact `dim 0`); `τ_3` has positive weight so `τ_3(0) = 0`
and `T_{3,0}(0) = −c ≠ 0`; the τ = 0 part of the cone is the origin alone, whose pair is the bare
z-type pair (`J = −cz`, verified mod 32003: `J = 9045γ + 22958π`, `c ≡ 9045`).  There is no
non-trivial point to test at `t = 3`; the same holds for `t = 4..7`.  Note the origin's pair is
*not* `(h^{3t+1}, h^{2t+1})`: it is `Q = h^q + Ah^t + yB`, `P = h^e + g1Ah^{2t} + g2Bh^t + gz`.

## 5. Step (4): the dependent-pair system is inconsistent; Z-EMPTY at t = 8

*Literal system.*  `H = h + Σ ε_j h^{−j}`, `P = φ(H)`, `Q = ψ(H)` implies `J(Q,P) = 0`; by §2 the
chart forces the `π^0` coefficient of `π³J` to be `yg(h − b4) ≠ 0`.  The system is empty at every
`t` before any order row or gauge is imposed.  **DEP-EMPTY at t = 8: HOLDS (vacuously), size 0.**
It does not bear on (V0), because DEP is false.

*Replacement.*  `Z-EMPTY_8 : V(T_{8,1..15}, T^hom_{8,0}) = {0}` in `A_8[b3,b4,q_2..q_7]`
(`A_8 = Q(√3)`, weights `9,1,2,…,7`).  Rows: Fable's exact `t = 8` rows reduced at
`P = (32003, y − 11288)` (frozen `t8_p32003_r11288_rows.txt`; no `div. by 0`/`error` marker in any
output of this lane).  Exact system size (`zsys_t8_full_p32003_r11288.log`):

```text
generators 16 (T_1..T_15, T0hom), variables 8;  weighted degrees 32,31,…,18 and 33;
terms: T_1..T_15 = 3124, 2700, 2327, 1994, 1706, 1452, 1231, 1039, 875, 730, 609, 504, 415, 339, 277;
T0hom = 3580 (T_{8,0}(0) ≡ −15556);  at b4 = 0: 424, 373, …, 55 and 456.
```

| job (mod 32003, root 11288) | generators | result | time / RSS | typing |
|---|---:|---|---|---|
| full z-system `⟨T_1..T_15, T0hom⟩`, `std` | 16 | not finished | 590 s cap, 538 MB | INCONCLUSIVE_TIMEOUT |
| z-slice `b4 = 0`: `⟨T_k|_{b4=0}, T0hom|_{b4=0}, b4⟩`, `std` | 17 | **dim 0**, size 2275 | 34 s, 40 MB | PROVED-HERE via 5.1 |
| z-chart `b4 = 1`: `⟨T_k|_{b4=1}, T0hom|_{b4=1}, b4−1⟩`, `std` / `slimgb` | 17 | not finished / not finished | 590 s, 454 MB / 590 s, 661 MB | INCONCLUSIVE_TIMEOUT |
| top tail `⟨T_8..T_15⟩`, `std` (dim 0 would give (V0) itself) | 8 | not finished | 590 s cap, 693 MB | INCONCLUSIVE_TIMEOUT |
| RESIDUAL-ZERO `⟨T_1..T_15, b4⟩`, `std` | 16 | **dim 0**, size 2314 | 21 s, 42 MB | PROVED-HERE via 5.1 |

Promotion: the two `dim 0` ideals are weighted-homogeneous with positive weights, so by the
properness lemma (Fable §5.1, `R` = localization of `Z[y]/(H_8)` at `P`, fraction field `A_8`, a
field since `27` is not a square) the characteristic-zero cones are `{0}`.  Consequences:
**RESIDUAL-ZERO holds at t = 8** (the `b4 = 0` chart of the terminal system is unit: the residual
maximal ideal is nilpotent modulo `I_{8,+}|_{b4=0}` and `T_{8,0}(0) = −c` is a unit), and **every
non-zero z-type point at t = 8 has `b4 ≠ 0`**, so `Z-EMPTY_8` is equivalent to the emptiness of
the `b4 = 1` z-chart, which is the only open piece.  The modular nonresults are not verdicts.

**Verdict (4): DEP-EMPTY at t = 8 HOLDS vacuously (system inconsistent identically); Z-EMPTY_8:
b4 = 0 half PROVED, b4 = 1 chart INCONCLUSIVE_TIMEOUT (17 generators, 7 effective variables,
590 s cap).**  No witness exists on `b4 = 0`; whether (V0) fails at `t = 8` is undecided here.

## 6. Step (5): t = 9, 10

Not attempted: the `t = 8` `b4 = 1` chart did not finish at the cap, and the `t = 9` rows exist
only as a modular spine (1.6 MB, `k16terminal-fable5`); a z-slice at `b4 = 0` for `t = 9` would be
the same 30 s-class job (`probe_t8.py` generalizes by changing `t`), but it cannot decide
`Z-EMPTY_9` without the `b4 = 1` chart.  Typed `NOT-RUN[BUDGET]`.

## 7. What replaces §1.2 (the decision for the campaign)

1. **The uniform statement.**  `(V0)_t ⟺ (T)_t ∧ Z-EMPTY_t`.  The second conjunct is *not*
   classical: z-type pairs are honest monomial-Jacobian pairs (`J = cγ'`, Jacobian line through
   the simple place at infinity), with the same degrees `(8t+4, 12t+4)` and the same two places.
   Gordan–Noether/Schinzel never enters.  My round text "(V0) = (T) ∧ no dependent pair" and
   "the τ = 0 part is classical" are withdrawn; the "bare tower" is a z-type pair, not a
   dependent one.
2. **The instrument is over-strong exactly by Z-EMPTY.**  Z-EMPTY fails at `t = 2, y = 1/5`
   (the axis family (3.1)), holds for `t = 3..7`, and at `t = 8` is reduced here to the `b4 = 1`
   z-chart.  A future `dim I_{t,+} > 0` at some `t` must be read as "a z-type family exists", not
   as a failure of (T); the theorem's own test is Rabinowitsch `τ_t ∈ √I_{t,+}` (GPT's cone gate
   at `t = 2`), or equivalently "the only cone points are z-type".
3. **No smaller system.**  Z-EMPTY is the cone plus `T^hom_{t,0}`; the hoped-for
   "linear in φ, ψ" system does not exist because its solution set is empty by identity.  The
   cheapest honest test at `t = 8` is the `b4 = 1` z-chart above with a longer bound (the
   `b4 = 0` half is done), or the top-tail cone (8 generators), whose `dim 0` would give
   `(V0)_8` outright; both timed out at 590 s on a host at load ≈ 14.
4. **Structural lead (typed OPEN, not promoted).**  `OPEN[K16-Z-TYPE-RECEIVER]`: does the
   campaign's receiver descent (Prop 6.3/6.4 data `J = cγ^k`) ever produce a datum whose Jacobian
   line passes through the simple place at infinity?  If not, z-type pairs are irrelevant to the
   Jacobian problem and (V0) should be demoted to a fixed-`t` instrument (Opus V5, V7); if yes,
   Z-EMPTY is a second receiver-emptiness statement to which the same engine applies.  Bounded
   test: the order data of the family (3.1) at the place `[1:1]` against the campaign's receiver
   typing.
5. **New fixed-t facts:** RESIDUAL-ZERO at `t = 8` (PROVED-HERE via 5.1), and the `b4 = 0` half of
   Z-EMPTY at `t = 8`.

OPENS RAISED

- `OPEN[K16-Z-EMPTY-T8-B4ONE]` — is `⟨T_{8,k}|_{b4=1} (k=1..15), T^hom_{8,0}|_{b4=1}⟩` the unit ideal
  of `A_8[b3,q_2..q_7]`?  Bounded: one modular `std`/`slimgb` (17 generators; `probe_t8.py b4one`)
  with `timeout ≥ 1800` on a quiet host; a modular unit ideal must then be combined with the proved
  `b4 = 0` half (homogeneous cone `{0}` mod `p`) before promotion by 5.1.
- `OPEN[K16-Z-TYPE-RECEIVER]` — as in §7.4.

## 8. FALLACY-v2 audit

- **Variable/ring map.**  Coordinates `(γ,π)`, `h = πA + b4`, `X ↔ h`, `s = L = X − b4`; the
  Laurent decomposition lives in `K[h][π^{±1}]` with `h, π` independent (§2), never in
  `K[γ][π^{±1}]` (an earlier check of mine extracted a coefficient in the wrong ring and was
  discarded; the corrected one is `laurent_coeff_check.py`).  The sign `T = −[X^k]R` was fixed
  against the banked `t = 2` and `t = 4` records at every point used.
- **Prime label/derivative.**  Primes in §2 are `d/dX`; the finite-field prime is `p = 32003`.
- **Split index.**  `A_2 = Q × Q` handled per fibre (`y = 1/5`, `y = 2/5`); `A_8 = Q(√3)` is a
  field, one root used; no zero divisor inverted (all pivots asserted non-zero at run time).
- **Modular promotion.**  Only weighted-homogeneous `dim 0` results are promoted (properness
  lemma); the inhomogeneous `b4 = 1` chart returned nothing and nothing is inferred from it; no
  `sat()`; no raw-remainder degree used; `reduce(1,G)` only inside the timed-out chart.
- **Floor/attainment.**  DEP's refutation is by an exact witness (3.1) and an identity; Z-EMPTY
  at `t = 8` is split into a proved half and a typed timeout, not a verdict.
- **No interpolation in t.**  The identity (2.2) is a derivation valid for all `t`; the `t = 2..6`
  runs are controls of it, not its proof.

## 9. Reproduction and artifacts

```text
cd box/k16dep-20260903
python3 rebuild_pair.py 2 --fibre 1/5 --point 1,0 --json /tmp/jc2-lane.9Mpgn1/inputs/terminal_laurent_t2.json
./run_controls.sh            # t=2 both fibres, gauge change; t=3..6 mod p  -> controls.log
python3 identity_check.py; python3 laurent_coeff_check.py; python3 json_control_modp.py
ROWS=../k16terminal-fable5-20260903/t8_p32003_r11288_rows.txt
python3 probe_t8.py b4zero $ROWS z.log 590 > j.sing && timeout 590 Singular -q j.sing   # dim 0, 34 s
python3 probe_t8.py resz   $ROWS r.log 590 > j.sing && timeout 590 Singular -q j.sing   # dim 0, 21 s
python3 probe_t8.py {full|b4one|topt} ...                                                # timeouts at 590 s
```

Files: `t2_f15_axis_b3_1.log`, `controls.log`, `identity_check.log`, `laurent_coeff_check.log`,
`t4_json_control.log`, `zsys_t8_*.log`, `zchart_t8_*.log`, `topt_t8_*.log`, `resz_t8_*.log`,
`*.err` (`/usr/bin/time -v`, exit codes 124 for the timeouts), `manifest.sha256`,
`manifest.check.log`, `SHA256SUMS`, `REGENERATE.txt` (the 10.5 MB Singular job files were
deleted after the runs and are regenerated by `probe_t8.py`).

<!-- BODY-END -->
