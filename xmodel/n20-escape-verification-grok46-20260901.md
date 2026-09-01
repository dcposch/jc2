# N20-ESCAPE verification — computation arm

Lane: N20-ESCAPE (paired review, computation arm; independent of the prose arm).
Date: 2026-09-01.
Scope: desk-scale exact arithmetic and enumeration only. No CAS. No `jc2-lean`. No edits to charged files or canonical ledgers.
Charged inputs (frozen copies under `/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.OsT3p1/inputs`):
- `n20-escape-kill-opus5-20260901.md`
- `b0-all-n-hostile-review-grok46-20260831.md`
- `block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md`

This report does not declare a `charge_basis`.

## 0. Hash verification

Frozen copies were hashed with `shasum -a 256` before they were read. All three match the charge exactly:

```text
46c5f62fe92fd5ecbd12b1f74d83d272624253f1f06e9324c9fa1b1c21eac619  n20-escape-kill-opus5-20260901.md
f865204a3fd2ee3a6944b6739ae581cf29c41a7f2259bbc54cd1587ddf397a46  b0-all-n-hostile-review-grok46-20260831.md
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc  block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
```

Primary PDFs in `refs/` were rehashed at execution and agree with ESCAPE §0 / REV §0:

```text
f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db  refs/jc86.pdf
88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad  refs/zoladek2008_official.pdf
```

Orevkov was read with `pdftotext -layout` on PDF pp. 2–5 (Lemma 2.1, Lemma 2.2, Lemma 3.1). No CAS. No `jc2-lean`. No charged file or canonical ledger edited. `FALLACY-v2` in force. No `charge_basis` line: this arm asserts no new exit price.

Notation consumed as promoted (ESCAPE [P1]–[P8], ALL-N (1.1)–(4.8), REV §4): geometric degree `N`; `W = N − a = Σ_l s_l μ_l`; `d = 2a − N = a − W`; `R = Σ_l (s_l − 1)`; `q' = #{l : s_l ≥ 2}`; `corr_l = μ_l(s_l − 1) + Σ_t k_t` with `k_t = M_t − e_t μ_l ≥ 0`; fibre identity `a_p + r_p W + K_p = N`; ALL-N’s `ν = Σ_{p∈Σ}(r_p − 1)` (not `Σ r_p`). Coordinator file COORD is the S₄ row-kill integration; it contributes no N=20 packet arithmetic and is used only as a lineage marker for the affine-line repair.

## 1. Target (1): corr budget of the (2,3,16) packet; charged relation; synthetic packets

### 1.1 Finite ramification of a degree-3 cover `A^1 → A^1`

Let `h : A^1 → A^1` be polynomial of degree `s = 3`. Two Euler counts, both elementary.

**(P) Projective completion.** Extend to `h̄ : P^1 → P^1`. Riemann–Hurwitz:

```text
−2 = 3(−2) + Σ_p (e_p − 1)     ⇒     Σ_p (e_p − 1) = 4.
```

A polynomial sends `∞` to `∞` with `e_∞ = 3`, so the infinite place contributes `e_∞ − 1 = 2`. Finite ramification is the remainder `4 − 2 = 2`.

**(A) Affine Euler.** Topological (and compactly supported) Euler characteristic `χ(A^1) = 1`. For a degree-3 branched cover of smooth affine curves, `1 = 3 · 1 − Σ_{t finite}(e_t − 1)`, hence again `Σ(e_t − 1) = 2`.

The query’s two formulae are both correct and name **different** divisors: projective total ramification has degree 4; the finite ramification divisor of `A^1 → A^1` has degree 2. Equivalently, `h'` is quadratic, so two finite critical points counted with multiplicity. The two combinatorial types:

| type | finite profile | `Σ(e−1)` |
|---|---|---|
| two simple crit. pts. | `e=2,2` | `1+1=2` |
| totally ramified | `e=3` at one point | `2` |

ESCAPE Theorem 4.A retains only the second, by concentration (not by RH). REV §4.5 budgeted the first. RH alone does not choose.

### 1.2 Re-derived corr of packet (4.9)

Packet data: `N=20`, dicriticals `(μ,s,corr) = (1,1,0) + (2,3,16)`, so `W = 1·1 + 3·2 = 7`, `a = 13`, `d = 6`, `R = (3−1) = 2`.

- Orevkov budget [P1]: `Σ(μ+corr) = 1+0+2+16 = 19 = N−1`. Holds.
- Corrected formula [P8]: `corr_1 = μ_1(s_1−1) + Σ k_t = 2·2 + Σ k_t = 4 + Σ k_t`. Forces `Σ k_t = 12`.
- RH-controlled piece is only `μ(s−1) = 4`. The residue `12` is fibre excess, not ramification degree. The naive count “16 units cannot sit on a ramification divisor of degree 2” **does not close**: it identifies `corr_l` with `Σ(e_t−1)`. Those are different quantities (FALLACY-v2 carrier/attainment, and prime-label: `h_l'` in 4.A is a derivative, `corr` is not).
- Two-site REV arrangement (OLD equality in (4.7)): two simple crit. pts., distinct images, each `k_t = 6`, `M_t = 2·2+6 = 10`, correction `8` apiece, `K_p = 6 = d`, `r_p = 2`, `a_p = 0`. Fibre check: `0 + 2·7 + 6 = 20`. Sum `K = 12 = a−1`. Numerically consistent with the *promoted* bound `a−1 ≤ dR = 12`.
- One-site concentration (ESCAPE): `h_1(t) = (t−t_0)^3`, `e=3`, one `k = 12`, `M = 3·2+12 = 18`, `corr = 18−2 = 16`. Then `K_p = 12 > d = 6`. Fibre: `a_p = 20 − r_p·7 − 12 ≤ 20−14−12 = −6` if `r_p ≥ 2`.

So the (2,3,16) corr budget **re-derives** as `4 + 12`, and the kill is the ceiling `K_p ≤ d` after concentration, not RH.

### 1.3 The charged general inequality

ESCAPE (5.1), re-derived from promoted identities only (no concentration of *values*, only of *sites* via `q'`):

```text
a − 1 = Σ_{p∈Σ} K_p ≤ |P| · d ≤ q' · d,
```

i.e. `W + d − 1 ≤ q' d`, using `K_p ≤ d` on `Σ` (from `r_p ≥ 2`, `a_p ≥ 0`) and `|P| ≤ q'` (at most one correction site per ramified carrier). Weight floor `W ≥ b + 2(q−q') + 4q' ≥ 1 + 4q'` gives (5.2) `q' ≤ ⌊(W−1)/4⌋`. The `q' = 1` case of (5.1) is `W ≤ 1`, contradicting `W ≥ 5`; this is ESCAPE §5(f).

Equality in `a−1 ≤ q' d` holds if and only if both steps saturate: `|P| = q'` (every carrier has `k_l > 0` and pairwise distinct physical images) **and** `K_p = d` for all `p ∈ P` (hence `r_p = 2` and `a_p = 0` at each). This is a numerical equality stratum, not an attainment claim.

### 1.4 Three synthetic packets

All three are integer tuples of the author’s design, subject to [P1]–[P8] and `2a > N`. No Keller witness is asserted.

**SYN-1 (small `s`, `q' = 1`, inequality never holds).** `(μ,s) = (1,1)+(2,2)`. Then `W = 5`, `R = 1`, `q' = 1`. For any `d ≥ 1`, `N = 10+d`, `a = 5+d`, `corr_1 = N−1−3 = 6+d`, and [P8] gives `k = corr − μ(s−1) = 4+d`. (5.1) reads `5+d−1 ≤ d`, i.e. `4 ≤ 0`, false for every `d`. Same obstruction as `k = 4+d ≤ d`. RH: `s−1 = 1`, one simple critical point; `corr` still overshoots by `4`. Equality in (5.1) is impossible at `q' = 1`.

**SYN-2 (small `s`, equality case of both (5.1) and (5.2)).** `(μ,s) = (1,1)+(2,2)+(2,2)`. Then `W = 9`, `q' = 2`, `R = 2`, `b = 1`, `q = q' = 2`. Weight floor saturates: `W = 1+4+4 = 9 = 4q'+1`, so (5.2) is equality. (5.1) becomes `8 ≤ d`; equality at `d = 8`, `N = 26`, `a = 17`. Budget: `Σ(μ+corr) = 25`, `Σμ = 5`, `Σ corr = 20`. Each carrier contributes `μ(s−1) = 2`, so `k_1 + k_2 = 16 = 2d`. Equality conditions of §1.3 are exactly `k_1 = k_2 = 8`, two distinct node images, `a_p = 0`. Fibre: `0 + 2·9 + 8 = 26`. This is ESCAPE Theorem 6.A’s numerical minimum, typed necessary-only.

**SYN-3 (mixed `μ`, mixed small `s`).** `(μ,s) = (1,1)+(2,3)+(3,2)`. Then `W = 1+6+6 = 13`, `q' = 2`, `R = 3`. (5.2): `⌊12/4⌋ = 3 ≥ 2`. (5.1): `12 ≤ d`.

- At `d = 11 < 12`, `N = 37`, `a = 24`: left side `13+11−1 = 23`, right side `22`. **Fails.**
- At `d = 12`, `N = 38`, `a = 25`: `24 ≤ 24`. **Equality.** Budget `Σ corr = 31`, ramification piece `μ(s−1)` sums to `4+3 = 7`, so `k_1+k_2 = 24 = 2d`. Equality again forces `k_1 = k_2 = 12`, `r_p = 2`, `a_p = 0`. Fibre: `0 + 2·13 + 12 = 38`.
- At `d = 13`, `N = 39`, `a = 26`: `25 ≤ 26`. **Holds strictly.** Then `Σ k = 25`, so the pair `(k_1,k_2)` cannot both equal `d`; e.g. `(12,13)` saturates one slot and leaves one unit.

On every synthetic packet the claimed inequality is the numerically correct ceiling, and equality occurs precisely at the two-step saturation of §1.3. Packet (4.9) is the `q' = 1` instance of SYN-1’s obstruction (with `s = 3` in place of `s = 2`): `12 ≤ 6` is false.

**Verdict, target (1): HOLDS.** Finite ramification degree is 2, not 4. Corr of (4.9) is `4+12`. The naive RH kill is not a kill. Inequality (5.1) holds as a numerical relation on all three synthetics; equality is the double saturation `|P|=q'` and `K_p=d`.

## 2. Target (2): enumeration of numerically-admissible escape packets at N = 20, 21, 24

Standing filters (promoted budget, **without** (5.1)): `b ≥ 1` trivials with `(μ,s,corr)=(1,1,0)`; every other dicritical has `μ ≥ 2`; a correction carrier has `s ≥ 2` hence `μ ≥ 2`; `W = Σ sμ`, `d = N − 2W > 0` (i.e. `2a > N`), `a = N−W`; `R = Σ(s−1) ≤ ⌊(W−3)/2⌋`; `a−1 ≤ dR` (4.7); `Σ(μ+corr)=N−1` with `corr_l ≥ μ_l(s_l−1)`; H2 `Σ μ ≤ N−2`. An *escape packet* is a ramified (`R ≥ 1`) integer multiset passing all of these.

Pairs `(W,d)` with `N = 2W+d`, `W ≥ 5`, `d ≥ 1`, and (4.8) `W+d−1 ≤ d·⌊(W−3)/2⌋`.

### 2.1 Admissible `(W,d)` at the three degrees

`F = ⌊(W−3)/2⌋`. Rearrangement: `F ≤ 1` is impossible; for `F ≥ 2`, `d ≥ ceil((W−1)/(F−1))`.

**N = 20.** Candidates `(W,d) ∈ {(5,10),(6,8),(7,6),(8,4),(9,2)}`.

| W | F | (4.8) | d | pass? |
|---:|---:|---|---:|---|
| 5 | 1 | impossible | 10 | no |
| 6 | 1 | impossible | 8 | no |
| 7 | 2 | `d ≥ 6` | 6 | **yes, equality** |
| 8 | 2 | `d ≥ 7` | 4 | no |
| 9 | 3 | `d ≥ 4` | 2 | no (`2 < 4`) |

Only `(W,d) = (7,6)`, `a = 13`. Then `a−1 = 12 ≤ 6R` forces `R ≥ 2`, and `R ≤ F = 2`, so `R = 2`.

**N = 21.** Candidates `(5,11),(6,9),(7,7),(8,5),(9,3),(10,1)`.

| W | F | need | d | pass? |
|---:|---:|---|---:|---|
| 5,6 | 1 | imp | | no |
| 7 | 2 | `d ≥ 6` | 7 | **yes** |
| 8 | 2 | `d ≥ 7` | 5 | no |
| 9 | 3 | `d ≥ 4` | 3 | no |
| 10 | 3 | `d ≥ 5` | 1 | no |

Only `(7,7)`, `a = 14`. Then `13 ≤ 7R` and `R ≤ 2` force `R = 2` (`13 ≤ 14`).

**N = 24.** Candidates `(5,14)…(11,2)`.

| W | F | need | d | pass? |
|---:|---:|---|---:|---|
| 5,6 | 1 | imp | | no |
| 7 | 2 | `d ≥ 6` | 10 | **yes** |
| 8 | 2 | `d ≥ 7` | 8 | **yes** |
| 9 | 3 | `d ≥ 4` | 6 | **yes** |
| 10 | 3 | `d ≥ 5` | 4 | no (`4 < 5`; `13 ≤ 12` fails (4.8)) |
| 11 | 4 | `d ≥ 4` | 2 | no |

Three pairs: `(7,10)`, `(8,8)`, `(9,6)`.

### 2.2 Shapes at each surviving `(W,R)`

Write `q'` = number of ramified carriers, `u` = number of unramified `μ ≥ 2`. Min weights: trivial 1, unramified `μ≥2` at least 2, carrier at least 4. `R = Σ(s_i−1)`.

**W = 7, R = 2** (N=20 and N=21, and N=24’s first pair). `q' = 2` needs weight `≥ 8 > 7`, impossible. So `q' = 1`, `s−1 = 2`, `s = 3`, carrier weight `3μ`. `μ = 2` gives weight 6, remainder 1: only one trivial. `μ ≥ 3` gives weight `≥ 9 > 7`. No room for an unramified extra. Unique shape: `(1,1)+(2,3)`.

- N=20: `corr = 19−3 = 16`, `k = 12`. Packet **P20** = `(1,1,0)+(2,3,16)`. This is (4.9).
- N=21: `corr = 20−3 = 17`, `k = 13`. Packet **P21** = `(1,1,0)+(2,3,17)`.
- N=24, W=7: `corr = 23−3 = 20`, `k = 16`. Packet **P24a** = `(1,1,0)+(2,3,20)`, `d=10`, `a=17`.

**W = 8, R = 2** (N=24 only). `R ≤ ⌊5/2⌋ = 2` already used. `q' = 2` needs weight `≥ 8`, remainder 0, hence `b = 0`: excluded by the trivial-dicritical filter. `q' = 1`, `s = 3`, weight `3μ`. `μ = 2` gives remainder 2. With `b ≥ 1` the only splitting of 2 is two trivials (an unramified `μ=2` would spend the remainder and leave `b=0`). `μ = 3` overflows. Unique shape: `2×(1,1)+(2,3)`. Packet **P24b** = `(1,1,0)+(1,1,0)+(2,3,19)`, `k = 15`, `a=16`.

**W = 9, R = 3** (N=24: `14 ≤ 6R` forces `R ≥ 3`, and `R ≤ 3`). `q' = 2` with `R = 3` means degrees `{2,3}`, weights `≥ 4+6 = 10 > 9`. `q' = 3` needs `≥ 12`. So `q' = 1`, `s−1 = 3`, `s = 4`, weight `4μ`. `μ = 2` gives remainder 1: one trivial. Unique shape: `(1,1)+(2,4)`. Packet **P24c** = `(1,1,0)+(2,4,20)`, `k = 14`, `a=15`.

No other integer multiset at these `N` passes (4.7)–(4.8) with `b ≥ 1` and `R ≥ 1`. In particular the competing W=7 shape `(1,1)+(3,2)` has `R = 1` and dies already under OLD (`a−1 ≤ d` forces `W ≤ 1`). Two-carrier shapes begin at `W ≥ 9` and, with `R = q' = 2`, need `d ≥ 8` from OLD (4.7), hence `N ≥ 26`; they are absent from {20,21,24}.

### 2.3 Apply (5.1): every OLD survivor dies

All five packets have `q' = 1`. Then (5.1) is `W ≤ 1`, already false. Explicitly:

| packet | N | W | d | a−1 | q'd | (5.1) |
|---|---:|---:|---:|---:|---:|---|
| P20 | 20 | 7 | 6 | 12 | 6 | 12 ≤ 6 **false** |
| P21 | 21 | 7 | 7 | 13 | 7 | 13 ≤ 7 **false** |
| P24a | 24 | 7 | 10 | 16 | 10 | 16 ≤ 10 **false** |
| P24b | 24 | 8 | 8 | 15 | 8 | 15 ≤ 8 **false** |
| P24c | 24 | 9 | 6 | 14 | 6 | 14 ≤ 6 **false** |

Each also fails the explicit fibre form: one site carries `k = corr − μ(s−1) ∈ {12,13,16,15,14}`, all strictly above `d`.

**Verdict, target (2): HOLDS.** Five packets, listed above, exhaust the promoted budget at N=20,21,24; (5.1) kills all five. No residual integer point.

## 3. Target (3): W/R bookkeeping identities at charged packet values

Charged numbers: `N = 20`, `W = 7`, `d = 6`, `a = 13`, `R = 2`. All identities below are integer tautologies or substitutions of promoted (4.1)–(4.5); `ν` is ALL-N’s `ν = Σ_{p∈Σ}(r_p − 1)`, **not** `Σ r_p`. (Using the wrong `ν` produces a spurious `Σ K = a−1+Wσ` and would appear to break (4.6); that is a label error, not a broken identity.)

### 3.1 Linear relations among `(N,W,d,a)`

```text
W = N − a           7 = 20 − 13
d = 2a − N          6 = 26 − 20
d = a − W           6 = 13 − 7
N = 2W + d          20 = 14 + 6
a = W + d           13 = 7 + 6
d = N − 2W          6 = 20 − 14
2a > N              26 > 20
```

All seven hold. Fibre count [P3]: `a + Σ s_l μ_l = 13 + 7 = 20 = N`.

### 3.2 Ramification and correction

Packet `(1,1,0)+(2,3,16)`: `R = (1−1)+(3−1) = 2`. Most-generous bound `R ≤ ⌊(W−3)/2⌋ = ⌊4/2⌋ = 2` saturates, as does `W = 2R+3 = 7` (`b=q=1`, `μ=2`).

Orevkov [P1]: `1+0+2+16 = 19 = N−1`. [P8]: `16 = 2·2 + Σ k`, `Σ k = 12`. H2: `Σ μ = 3 ≤ 18`, `Σ corr = 16 ≥ 1`.

### 3.3 Fibre identity and (4.6)

At any physical `p`, `a_p + r_p W + K_p = N`. Sum over `Σ`:

```text
A_Σ + W Σ r_p + Σ K_p = N σ.
```

With `Σ r_p = ν + σ`, this is `A_Σ = Nσ − W(ν+σ) − ΣK = aσ − Wν − ΣK`, which is ALL-N’s displayed formula after (4.5). Substitute into (4.1)

```text
0 = (a−1) + (N−2a)σ + (N−a)(ν−σ) + A_Σ
```

and use `N−2a = −d`, `N−a = W`:

```text
0 = (a−1) − d σ + W(ν−σ) + aσ − Wν − ΣK
  = (a−1) + (−d − W + a)σ − ΣK.
```

The coefficient of `σ` is `−d − W + a = −(a−W) − W + a = 0`. Hence `Σ_{p∈Σ} K_p = a−1 = 12`. This is (4.6) at the charged values.

OLD (4.7): `12 ≤ dR = 6·2 = 12`, equality. NEW (5.1): `12 ≤ q' d = 6`, false. The two bounds agree only when `R = q'`; here `R = 2 > q' = 1`, and that gap is the whole kill.

Generic check of (4.5): `r=1`, `K=0`, `a_p=a` recovers `13+7=20`. Equality two-site arrangement (REV, not concentrated): `r_p=2`, `K_p=6`, `a_p=0` gives `0+14+6=20` at each of two points, and `6+6=12=a−1`. Concentrated one-site arrangement: `K_p=12`, `r_p≥2` gives `a_p ≤ 20−14−12 = −6`, which is the positivity break.

### 3.4 Euler identity as a numerical control

Promoted covering Euler `(N−a)χ_c(D−Σ) = N−1−Nσ+A_Σ` with `χ_c(D−Σ) = 1−σ−ν` rearranges to (4.1) identically (the substitution in §0 of ALL-N is an equivalence, not a new constraint). Feeding `A_Σ = aσ − Wν − 12` into (4.1) at `(a,W,d)=(13,7,6)` returns `0 = 12 − 12` independently of `σ,ν`. Control values:

- `σ=1`, `ν=1` (one node): `χ_c = 1−1−1 = −1`, RHS of covering Euler `19−20+A_Σ`, and `A_Σ = 13−7−12 = −6`, so `7·(−1) = −1−6`. Holds.
- `σ=2`, `ν=2` (two nodes, REV equality): `χ_c = 1−2−2 = −3`, `A_Σ = 13·2 − 7·2 − 12 = 0`, and `7·(−3) = 19−40+0 = −21`. Holds.

(The negative `A_Σ` in the first control is a cardinality obstruction at `σ=1`, matching `a_p = −6` after concentration; it is consistent as arithmetic and is not a witness.)

**Verdict, target (3): HOLDS.** All W/R/fibre/Euler identities close at `(W,d,a,R)=(7,6,13,2)` once `ν = Σ(r_p−1)` is the ALL-N convention. The only false inequality at these numbers is (5.1), which is the intended kill, not a bookkeeping error.

## 4. Target (4): H3-free l' ≅ A^1 at a non-minimal example

H3 is the statement `D̃ ≅ A^1` (normalization of the branch curve). The claim under test is that `l' ≅ A^1` for an affine-image dicritical does **not** use H3, and that this remains so away from Orevkov’s N=3 / chain-length-1 minimum.

### 4.1 Primary-source chain, N-free

Orevkov, `refs/jc86.pdf` PDF p. 2, before Lemma 2.1: irreducible components of `L = X̃ \ C̃²` are nonsingular rational curves, intersecting transversally and at most pairwise; the dual graph of `L` is a tree. The regularization (§2) is a finite sequence of σ-processes at infinity for a polynomial map `C² → C²`; geometric degree `N` is not an input.

Lemma 2.1 (same page; proof through p. 4, via Lemma 2.2 on polar-versus-zero multiplicities and the branch structure of `L_1 ∩ L_2`): `X̃` may be chosen so that each connected component `K` of `L_{FC}` satisfies (a) unique point `p = K ∩ L_∞` with `f(K \ p) ⊂ C²`; (b) dual graph of `K` linear, `p` on an endpoint component `l_k`; (c) `l_k ⊂ L_F` and `l_i ⊂ L_C` for `i < k`. The proof of (c) is: a function on `l_i` without poles is constant. No sheet-count, no branch curve, no `η`.

Hence `l_k ≅ P^1` and `l' := l_k \ {p} ≅ A^1`. This is ALL-N (1.5) / ESCAPE [R1], at the printed scope.

### 4.2 Non-minimal example NM

Minimal picture is `k = 1`: no `L_C`, `l_1 ⊂ L_F`, `l' ≅ A^1`, typically the trivial dicritical (`μ=1`, `corr=0`). Non-minimal: take the carrier of P20, and lengthen the contracted chain to `k = 3` (two `L_C` components). Dual graph of that `L_{FC}`-component:

```text
L_∞ ──(p)── l_3 ⊂ L_F (μ=2, s=3) ──(t_0)── l_2 ⊂ L_C ── l_1 ⊂ L_C
```

Inputs used: Lemma 2.1(a,b,c) plus “components of `L` are nonsingular rational.” Not used: H3, immersivity of `η`, `μ`-values, `N`, the Orevkov budget, (5.1). Outputs:

- `l_3 ≅ P^1` meets `L_∞` at exactly one point `p` and meets `l_2` at exactly one other point `t_0` (tree, pairwise, linear). Those two points are distinct, so `t_0 ∈ l' = l_3 \ {p}`.
- `l' ≅ P^1 \ {p} ≅ A^1`.
- The contracted configuration `l_1 ∪ l_2` is connected and meets `l_3` only at `t_0`; `π` sends it to one point `x_0 = π(t_0)` of `π(l) \ {∞}`. This is the unique candidate jump site on this dicritical (ESCAPE Lemma 3.1), but that refinement is *not* required for `l' ≅ A^1`.

The same graph with `N = 4` (any noninvertible degree other than Orevkov’s 3) and `k = 3` gives the same `l' ≅ A^1`. Degree never enters.

### 4.3 Where H3 actually sits

H3 is deduced *after* `l'_0 ≅ A^1`, from a trivial dicritical: `dφ_0 ≠ 0` everywhere ⇒ `h_0` étale of some degree `s_0`, projective RH on `P^1 → D̄` forces genus 0 and `s_0 = 1`, hence `D̃ ≅ A^1` (REV §2.3). Using H3 to justify `l' ≅ A^1` would reverse that dependency. Example NM does not have a trivial dicritical on the displayed chain (the displayed `l_3` has `μ=2`); H3, if present at all, would come from a *different* dicritical `l_0` of the same map, and still would not be an input to `l_3 \ {p} ≅ A^1`.

**Verdict, target (4): HOLDS.** At the non-minimal chain `k=3` (and at any `N ≥ 3`) the identification `l' ≅ A^1` is Lemma 2.1 plus rationality of components of `L`, with H3 unused.

## 5. Packet shapes the charged case analysis might miss

Hunt is against ESCAPE §§5–6 (the (5.1) case split `q'=1` impossible, then min `N` at `q'≥2`) and against the N=20/21/24 census of §2. Shapes tried: large `s`, large `μ`, several carriers, extra trivials, `b=0`, shared images. No CAS; all counts are integer partitions of `W` with the weight rules of §2.

**Large `s`.** Family `(1,1)+(2,s)`, `W=1+2s`, `R=s−1`, `q'=1`. Then (5.1) is `W≤1`, false for every `s≥2`. At the charged degrees the only large-`s` OLD survivor is P24c (`s=4`, `W=9`), already killed. Next, `s=5`, `W=11`: at N=24 one has `d=2` and (4.8) `12 ≤ 8`, false; at N=20,21, `W=11` forces `d<0`. Larger `s` is worse.

**Large `μ`.** Family `(1,1)+(μ,2)` has `R=1`, and (4.7) forces `W≤1`, impossible; these never enter the OLD census. Family `(1,1)+(μ,3)`, `W=1+3μ`: `μ=3` gives `W=10`, which fails (4.8) at N=20 (`d=0`), N=21 (`d=1<5`), N=24 (`d=4<5`). `μ≥4` overshoots `W=N/2`.

**Multiple carriers.** Min weight `W ≥ 1+4q'`. At `q'=2`, `W≥9`. The unique `W=9` point in the census is N=24, `d=6`. Two carriers of type `(2,2)` have `R=2`, and OLD needs `14 ≤ 12`, false. Mixed `(2,3)+(2,2)` needs weight `≥10>9`. So **no two-carrier packet is OLD-admissible at N=20,21,24**. First OLD (and NEW) two-carrier numerical slot is SYN-2: `W=9`, `d=8`, `N=26`. At `q'=3`, `W≥13`, and `N=24` gives `d=24−26<0`, excluded by `2a>N`. Extra trivials or unramified `μ≥2` only raise `W` at fixed `q'`, which at these `N` shrinks `d` and makes both (4.7) and (5.1) harder.

**Shared images / `k_l=0` on some carrier.** These drop `|P|` below `q'`, so `a−1 ≤ |P|d` is strictly stronger than (5.1). They cannot be missed survivors.

**`b=0` (no trivial dicritical).** Example: two `(2,2)` carriers, `W=8`, `N=24`, `d=8`, `q'=2`. Numerically (5.1) would read `15 ≤ 16` and would pass. This is **not** an escape packet of `OPEN[B0-H2-N>=20/RAMIFIED-NONPRIMITIVE-COVER]`: that OPEN assumes a `μ=1` dicritical (so [P5], H3, and `2a>N`). `b=0` is the B0 conclusion, not a remainder of this lane. ESCAPE §5 never claims (5.1) without [P5]. Not a missed shape *of the charged case analysis*.

**`r_p=1` reading of P20.** If one ignores ESCAPE §5(b) and allows a smooth correction image, (4.5) at P20 with `K_p=12`, `r_p=1` gives `a_p=1≥0`. Fibre positivity alone does not kill (4.9) under concentration; the kill uses `r_p≥2` from [P5]+[P6]. ESCAPE §6 already records this. It is a load-bearing geometric hypothesis, not an unlisted integer packet. This arm does not re-prove §5(b); it records that the numerics of P20 are consistent with `a_p≥0` if and only if `r_p=1` is allowed.

**Independent min-`N` check of Theorem 6.A.** Substitute `W ≥ 4q'+1` and `(q'−1)d ≥ W−1` into `N=2W+d`, `q'≥2`:

| `q'` | min W | min d | min N |
|---:|---:|---:|---:|
| 1 | — | impossible | — |
| 2 | 9 | 8 | 26 |
| 3 | 13 | 6 | 32 |
| 4 | 17 | 6 | 40 |
| 5 | 21 | 5 | 47 |

Raising `W` by 1 costs 2 in `N` and saves at most `1/(q'−1) ≤ 1` in `d`; the minimum is at `W=4q'+1`, increasing in `q'` for `q'≥2`. No integer `(q',W,d)` with `N∈{20,21,24}` satisfies (5.1) and `W≥4q'+1`, `q'≥1`, `d≥1`.

No packet shape at large `s`, large `μ`, or several carriers slips the charged case split at the three degrees. **No miss found.**

## 6. FALLACY-v2.md guardrail check

- **Flag/place/series.** Four objects kept distinct: `t ∈ l'`, `π(t) ∈ X̃^*`, place `h_l(t) ∈ D̃`, physical `η(h_l(t)) ∈ D`. Example NM in §4 turns on `p ≠ t_0` on the same `P^1`. No cv flag, place, or cover series identified.
- **Per-ray/exit-set charge.** No typed first-separation exit is asserted. No `charge_basis` line (charge forbids one; this arm declares no new exit price).
- **Carrier/attainment.** P20–P24c, SYN-1–SYN-3, and the `(W,d,q')=(9,8,2)` slot are integer packets, necessary-only. None is `FULL_ACTUAL_EXIT` or a Keller witness. `REPRESENTATIVE` (e.g. the two-site REV arrangement) is not treated as attainment.
- **Pole/interior.** No pole identity used.
- **Floor/attainment.** `N ≥ 26` is a floor from (5.1), used only to exclude {20,21,24}. Equality in (5.1) is characterised as double saturation (`|P|=q'` and `K_p=d`), not as existence. `R ≤ ⌊(W−3)/2⌋` and `q' ≤ ⌊(W−1)/4⌋` are floors on the obstruction (looser upper bounds on `R` or `q'` would only weaken exclusions).
- **`sat()`, raw remainder, variable/ring map.** Not used. No CAS.
- **Prime label/derivative.** `l'` is the punctured dicritical. The only derivative is `h'` (polynomial derivative of a degree-`s` cover), used in §1.1 to count finite critical points. `corr_l` is not a derivative.
- **Merge-free / M-descent / target-arrival.** Not in play.
- **No silent cap.** The `r_p=1` reading of P20, which would leave `a_p=1≥0`, is typed in §5 as a geometric hypothesis of ESCAPE §5(b), not filled by analogy. Theorems 7.A–7.B (link, `k_l=0`, all-degree B0) are outside this arm’s computation scope and are not used to close any numerical gap.

No item required a typed `OPEN` in place of a number. The five OLD survivors and the three synthetics are fully numeric.

## 7. Verdicts

| Target | Claim tested | Verdict |
|---|---|---|
| (1) | Finite ramification of a degree-3 `A^1→A^1` cover has degree 2 (projective total 4 includes `e_∞−1=2`); corr of (4.9) is `μ(s−1)+Σk = 4+12`; naive RH kill does not close; (5.1) holds on SYN-1 (never), SYN-2 (equality at `d=8`), SYN-3 (fails `d=11`, equality `d=12`, strict `d=13`); equality iff `|P|=q'` and `K_p=d` | **HOLDS** |
| (2) | OLD-admissible escape packets at N=20,21,24: exactly P20 `(2,3,16)`, P21 `(2,3,17)`, P24a `(2,3,20)`, P24b two trivials + `(2,3,19)`, P24c `(2,4,20)`; each has `q'=1` and dies under (5.1) | **HOLDS** |
| (3) | Identities at `(W,d,a,R)=(7,6,13,2)`: linear W/d/a/N, `R=2` saturating `⌊(W−3)/2⌋`, [P1]/[P8], fibre sum with `ν=Σ(r_p−1)` yielding `ΣK=a−1=12`, Euler controls at `(σ,ν)=(1,1)` and `(2,2)` | **HOLDS** |
| (4) | `l' ≅ A^1` on the non-minimal chain `k=3` (P20 carrier, two `L_C` components) uses Orevkov Lemma 2.1 and rationality of `L`, not H3 | **HOLDS** |

All four targets HOLDS as desk-scale exact arithmetic, enumeration, and primary-source instantiation. No integer hole in the N=20/21/24 census; no synthetic packet violates (5.1) in the direction that would save (4.9); no missed large-`s` / large-`μ` / multi-carrier shape at these degrees.

Not in scope of this arm (prose / geometry, not a numerical break): ESCAPE Lemma 3.1 and Theorem 4.A (concentration / total ramification); §5(b) (`P ⊆ Sing D`); Theorems 7.A–7.B (`k_l=0` and all-degree B0). If §5(b) failed, P20 would be fibre-nonnegative at `r_p=1`; that is a hypothesis check for the other arm, not a counterexample packet.

Sources used: Orevkov, *Math. USSR-Izv.* 29 (1987), `refs/jc86.pdf` SHA-256 `f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db`, Lemma 2.1 pp. 2–4, Lemma 3.1 p. 4; Żołądek 2008 rehashed, not re-opened; charged ESCAPE / REV / ALL-N identities as cited. COORD contains no packet arithmetic.

No `charge_basis` declaration.

<!-- BODY-END -->
