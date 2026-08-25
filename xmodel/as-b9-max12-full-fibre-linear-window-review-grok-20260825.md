# Hostile different-model review — B9 fixed-D12 full affine linear window through `3^10`

| Field | Value |
|---|---|
| Producers | `xmodel/as-b9-max12-full-output-mod729-producer-20260825.md`; `xmodel/as-b9-max12-full-fibre-linear-window-producer-20260825.md` |
| Frozen cases | `cases/as_b9_max12_full_output_mod729_20260825/`; `cases/as_b9_max12_literal_digit_ladder_20260825/`; `cases/as_b9_max12_full_fibre_mod2187_20260825/`; `cases/as_b9_max12_full_fibre_linear_window_20260825/` |
| Parent case / review | `cases/as_b9_max12_w5_survivor_aws_20260825/`; `xmodel/as-b9-max12-w5-survivor-review-grok-20260825.md`, overall **CONFIRMED** |
| Parallel first-gate implementation | `cases/as_b9_max12_w6_next_digit_aws_20260825/` (TD6 owner, 141-row); corroboration only |
| Overall verdict | **CONFIRMED** |
| Mathematics | **CONFIRMED** |
| Source typing | **CONFIRMED** |
| Software | **CONFIRMED** (non-blocking control-strength nits below) |
| Custody | **CONFIRMED** of the frozen dual-AWS same-implementation runs |
| Terminology / wording | non-blocking only |
| Mathematical defects | none |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Evidence | no-shell source and integer-arithmetic review: binomial ambient counts; Jacobian polarization identity over `Z`; independent expansion of `(P5,Q5)` and reconstruction of the 11-term particular; rank-nullity and `kernel - projection = 74` interlocking through five stages; dual-host hash and stdout identity as declared. No local Bash, Python, CAS, or solver execution. No AWS replay |
| Review window | 2026-08-25 |

## Verdict

**CONFIRMED**

Over the displayed B9 mod-243 point `(P5,Q5)`, the complete fixed-D12 output cone is a linear congruence through determinant modulus `3^10`. The first gate is a consistent `276 x 182` system of rank 108 and affine kernel 74. Its deterministic free-zero particular has eleven nonzero terms, reconstructs an integer pair of actual total degrees `(11,12)` and actual partial `y`-degrees `(9,12)`, and is determinant one modulo 729 in every coefficient. That particular is inconsistent at modulus 2187; the full 74-dimensional fibre is not. Successive Bocksteins of the same integer operator then give the claimed table through `3^10`, each stage consistent, each with a literal D12 integer witness. The quadratic term `243^2 det J(T)` is invisible on this window and first enters the divided carry at the transition `3^10 -> 3^11`. Box02 and Box03 are two executions of one implementation. This is one displayed parent, one complete D12 cone, finite depth.

## Strongest exact claim

Let `u=x+y^3` in `Z[x,y]`, and let `(P5,Q5)` be the frozen B9 branch through modulus `243` with

```text
P5 = u - u^3 + 18 u y + 81(2 u y + x y^2),
Q5 = y + u^4 + 3 u^2 y + 72 y^2 + 81(y^2 + x^4 y^2 + x y^{11}).
```

Write `F = (P5,Q5) + 243 T` with `T=(R,S)` ranging over both copies of every monomial of total degree at most twelve (91+91=182 coefficients). The Jacobian identity

```text
det J(F) - 1 = D5 + 243 A(T) + 243^2 det J(T),    243^2 = 3^10,
```

holds coefficientwise over `Z`. Consequently, for `1 <= k <= 5`, the condition `det J(F) ≡ 1 (mod 3^{5+k})` is exactly the linear congruence

```text
D5/243 + A(T) ≡ 0  (mod 3^k)
```

on that 182-dimensional coefficient space. The complete ambient of the determinant is the 276 monomials of total degree at most 22. Exact successive Bocksteins of this system, retaining every column and every row, are consistent and give

| determinant modulus | combined rank | affine kernel | projection to prior fibre |
|---:|---:|---:|---:|
| `3^6=729` | 108 | 74 | 0 |
| `3^7=2187` | 147 | 109 | 35 |
| `3^8=6561` | 162 | 129 | 55 |
| `3^9=19683` | 164 | 147 | 73 |
| `3^{10}=59049` | 164 | 165 | 91 |

The first-gate free-zero particular is the eleven-term digit

```text
R = xy + x y^2 + 2 x^3 y^2 + 2 x^5 + x^2 y^5 + 2 x y^8 + 2 x^2 y^9,
S = 2 x^4 y^2 + x^3 y^5 + x^2 y^8 + 2 x y^{11},
```

the reconstructed pair `(P5+243 R, Q5+243 S)` has actual total degrees `(11,12)` and actual partial `y`-degrees `(9,12)`, and `det J ≡ 1 (mod 729)`. That same particular does not lift to modulus 2187. The 74-dimensional fibre does: the fresh operator has rank 108 and left-cokernel dimension 168; 70 nonzero affine obstruction equations of coefficient rank 39 cut the predecessor fibre to a 35-dimensional liftable subset; the combined system has rank 147 and kernel 109. Each later stage likewise admits a literal integer witness of total and partial `y` degree at most twelve.

## Sharpest non-claim

Full staged affine families in the complete D12 cone over one displayed B9 mod-243 point, through determinant modulus `3^{10}` only. Not the complete earlier mod-243 fibre, not an inverse limit or `Z_3` point, not a characteristic-zero polynomial map or collision, not a Keller counterexample, not a maximum-twelve theorem, not a TD6 result, not a resolution of JC2, and not a linear Bockstein for the transition `3^{10} -> 3^{11}=177147`.

---

## 1. Parent, support, and ambient

The first-gate solver source-pins

```text
cases/as_b9_max12_w5_survivor_aws_20260825/replay.py
```

at SHA-256 `f1b50bb2c3e21369da205ebcf1ba028eede20c89d5ad863253fdfec4d6d28c5d`, matching the parent `SOURCE.sha256` and the already-confirmed w5 review. The parent constructs `(P5,Q5)` over `Z` with the binomial expansions of `u^3` and `u^4` retained, asserts `det J(P5,Q5) ≡ 1 (mod 243)`, and exposes the same `jac` used downstream: `P_x Q_y - P_y Q_x` in `(x,y)`. Because `(x,y)mapsto(u,y)` has Jacobian 1, this is the correct source orientation.

The complete fresh support is enumerated as

```text
support = [(i, d-i) for d in range(13) for i in range(d+1)].
```

The number of monomials of total degree at most `d` in two variables is `(d+1)(d+2)/2`, so degree `<=12` has `13*14/2=91` monomials. Both output digits give 182 columns, including zero and spectator columns. The determinant ambient is the same construction through degree 22: `23*24/2=276` rows. For maps of total degree at most 12, each first partial has degree at most 11 and the Jacobian has degree at most 22, so these 276 rows are the complete ambient. There are no omitted equations of degree 23 or higher: those coefficients are identically zero for D12 maps.

Of those 276 first-gate rows over `F_3`, 135 are zero on every column and on the target. The TD6 owner's 141-row implementation collects exactly the union of the supports of the special-fibre operator `D(R,S)=R_x-u^3 R_y+S_y` over `F_3` and of the divided residual; `276-141=135`. By that construction the dropped rows are `F_3`-zero, not omitted nonzero equations. Because `F5 ≡ G9 (mod 3)`, the integer polarization `A` at `F5` agrees with `D` modulo 3, so the same 135 rows are zero in the `276 x 182` matrix `A3`. They need not vanish identically over `Z`; integer rows that are only 3-divisible still belong in later Bocksteins. The licensed 276-row solvers retain them. Rank 108 on 276 rows with 135 `F_3`-zero rows is the same as rank 108 on the remaining 141, and the left-cokernel dimension `276-108=168=135+(141-108)` matches the focused 2187 solver.

## 2. Identity, divisions, and pair controls

For `F=F5+λ T` with `λ=243`,

```text
det J(F) = (P5_x+λ R_x)(Q5_y+λ S_y) - (P5_y+λ R_y)(Q5_x+λ S_x)
         = det J(F5) + λ A(T) + λ^2 det J(T),
```

where `A(T)=P5_x S_y + R_x Q5_y - P5_y S_x - R_y Q5_x`. Subtracting 1 gives the stated identity over `Z`. Every first-gate and window division is of a quantity the identity forces to be divisible by `243=3^5`:

- `D5=det J(F5)-1` is 0 modulo 243 by the parent;
- for a pure-`P` or pure-`Q` unit column, `det J(e_j)=0`, so `(jac(F5+243 e_j)-d5)/243` is exactly the corresponding column of `A`;
- mixed pairs contribute the extra `243^2 det J(e_i+e_j)`.

The window solver runs 91×91=8,281 mixed P/Q pair controls. After subtracting the two unit columns, it asserts that the leftover after one division by 243 is again 0 modulo 243. That is a valuation/additivity check: the quadratic remainder of the mixed-pair Jacobian is 0 modulo `243^2`. It is not a coefficientwise comparison of that remainder against an independently computed `243 det J(T)`. Algebraically the remainder *is* `243 det J(T)`, so the assertion is automatic for a correct Jacobian and would fail if the quadratic piece had valuation less than 10 or if `A` failed to be additive on mixed pairs. The unused local `linear` (which includes the affine constant `D5/243`) is dead code; the pair loop also omits the exact-divisibility assert `coefficient(delta)%243==0` that the unit-column loop has. Neither gap disturbs the identity. The real control of the linear window is the identity itself together with the integer Jacobian replay at each stage.

## 3. First complete gate

Independent expansion of the parent, retaining binomial mixed terms:

```text
P5 = -x^3 + x - 3 x^2 y^3 - 3 x y^6 - y^9 + y^3 + 180 x y + 180 y^4 + 81 x y^2,
Q5 = y + x^4 + 4 x^3 y^3 + 6 x^2 y^6 + 4 x y^9 + y^{12}
     + 3 x^2 y + 6 x y^4 + 3 y^7 + 153 y^2 + 81 x^4 y^2 + 81 x y^{11}.
```

The frozen particular has eleven nonzero `F_3` coefficients, at support indices matching

```text
R: (1,1)=1, (1,2)=1, (3,2)=2, (5,0)=2, (2,5)=1, (1,8)=2, (2,9)=2;
S: (4,2)=2, (3,5)=1, (2,8)=1, (1,11)=2.
```

Adding `243 R` and `243 S` to `(P5,Q5)` reproduces the frozen `P_support`/`Q_support` coefficientwise, including

```text
xy:     180+243=423,
x y^2:  81+243=324,
x y^8:  243*2=486,
x^2 y^5: 243,
x^2 y^9: 486,
x^3 y^2: 486,
x^5:    486,
x y^{11}: 81+486=567,
x^4 y^2: 81+486=567,
x^2 y^8: 243,
x^3 y^5: 243,
```

and every parent term that the digit does not touch. Actual total degrees are 11 in `P` (`x^2 y^9`) and 12 in `Q` (`y^{12}`); actual partial `y`-degrees are 9 and 12. The solver then asserts that every coefficient of `det J-1`, on the 276-row ambient union any extra keys of the computed Jacobian, is 0 modulo 729, that those keys have total degree at most 22, and that reduction modulo 3 is the seed `(u-u^3, y+u^4)`. Dual-AWS stdout records rank 108, consistency, kernel 74, matrix SHA `f99150e22eefb3d71fbb170e66fac01caf925cb4855cfd52ea8f70ff0cf04d0f`, result SHA `d267a2b5f4d7f6fd8d0535857923cd8f842322aa59d1a4b5bbd520f3a13a52dc`. Rank-nullity: `182-108=74`.

The TD6 owner's distinct source uses `D` over `F_3`, drops the 135 `F_3`-zero rows, and Gaussian-eliminates a `141 x 182` matrix. Its stdout records rank 108, the identical eleven-term support in the same column order, and the same actual degree pairs. That is parallel implementation evidence that `D ≡ A (mod 3)` on this parent and that the dropped rows are `F_3`-zero. It is not an independent mathematical solution: the parent formulae, the column order, and the free-zero RREF convention are shared. The initial TD6 dual-host `rc=1` (reporter demanded the ordered total-degree pair stay `(9,12)`) is preserved as a negative custody control and is not mathematics.

## 4. Pointwise negative control

`advance_literal.py` consumes the frozen mod-729 result at SHA `d267a2b5...` and modulus 729, linearizes at that stored pair, and returns `consistent False` with the same matrix SHA `f99150e2...`. Box02 and r6d agree at result SHA `b1e4ccbeb2126375f9d58f82b889abc0e43e1ea581da07ab128894f197b2b5d0`. The matrix SHA is the same as the first gate because `A` at `F5+243 T_0` agrees with `A` at `F5` modulo 3. The focused 2187 fibre solver independently asserts that the stored particular, fed to `A3` against the next carry, is inconsistent, and records `stored_particular_lifts: False`. The literal-ladder preregistration states that a failure kills only that point. The linear-window producer states that the pointwise failure is not a fibre theorem. No fibrewise conclusion is drawn.

## 5. Full 74D Bockstein at modulus 2187

The focused solver rebuilds the integer matrix `A`, the stored particular, and the 74-dimensional `F_3` kernel, then forms the next carry along that affine space. The left kernel of `A3` has dimension `276-108=168`. Pairing against the carry produces 70 nonzero affine equations of rank 39 on the 74 predecessor parameters. Consistency of a rank-39 system on 74 parameters gives a 35-dimensional solution space, which is exactly the recorded projection of the combined kernel onto the predecessor coordinates. The combined matrix is `[direction_carries | A3]`, of size `276 x (74+182)=276 x 256`. Combined rank 147 equals `108+39`; combined kernel `256-147=109`. Dual-AWS result SHA `edd34aea79057b5239d6ab47c86fa56cf9f0f24cfe9b1f751ba3060e196bf464`. A literal witness is reconstructed as `F5+243 T+729 V` and asserted determinant one modulo 2187, still of actual degrees `(11,12)` and `(9,12)`. Sign of the affine constant is `M x = -carry`, i.e. the next digit of `(D5/243 + A T)/3`.

## 6. Later full-family Bocksteins

The linear-window loop is the same Hensel/Bockstein, now iterated for `k=1..5` with `power=3^{k-1}` and modulus `3^{5+k}`. Stage 1 recovers the first gate (`directions=[]`, projection 0). Stage 2 recovers the focused 2187 package. Dual-AWS stdout, byte-identical on Box02 and Box03:

```text
stage 1 729   108  74  0
stage 2 2187  147 109 35
stage 3 6561  162 129 55
stage 4 19683 164 147 73
stage 5 59049 164 165 91
pair_controls 8281
```

Rank-nullity on the combined columns `(pred_dim + 182)` holds at every stage: `182-108=74`, `256-147=109`, `291-162=129`, `311-164=147`, `329-164=165`. The projection is the rank of the new kernel's predecessor coordinates, not the kernel dimension and not a cokernel rank. Orientation check: at every stage, `kernel_dimension - projection = 74 = 182-108`, and `projection = pred_dim - (combined_rank - 108)`. Swapping kernel and projection would break both identities. Affine constants remain `M x = -carry` along the running particular. The encoding `T = particular + sum a_i dir_i + 3^{k-1} V` is injective modulo `3^k` because the previous directions are `F_3`-independent and the fresh piece is scaled by `3^{k-1}`; there is no duplicate parameterization of the `T`-space. Rank stabilizes at 164 from `3^9` to `3^{10}`: the last two stages impose 56 independent cokernel conditions on their respective predecessor spaces, plus the standing fresh rank 108.

The final integer witness is an unreduced representative in the D12 cone (coefficients in the millions). Visible `P_support` has 42 monomials, maximum total degree 12 (`y^{12}`, `x^3 y^9`) and maximum `y`-degree 12; `Q_support` includes `y^{12}` and `x y^{11}`. The solver asserts both caps before recording the witness. Actual degrees of this later particular are no longer `(11,12)`/`(9,12)`; the claim is the cap, correctly.

## 7. Witnesses, caps, dual-host custody

Literal first-gate reconstruction is in section 3. Support and `y`-degree caps are asserted at every integer replay. Both-host custody, as declared and as read:

| package | job tag | result SHA | stdout SHA | Box02 RSS | Box03 RSS | rc |
|---|---|---|---|---:|---:|---:|
| full output mod 729 | `...T1620Z` | `d267a2b5...` | `102c1666...` | 17,656 KiB | 18,852 KiB | 0 |
| fibre mod 2187 | (focused) | `edd34aea...` | `b8935202...` | 20,720 KiB | 21,988 KiB | 0 |
| linear window | `...T1640Z` | `6a214518...` | `d754ed5d...` | 21,724 KiB | 22,448 KiB | 0 |
| literal ladder UNSAT | Box02/r6d | `b1e4ccbe...` | `1b3fb7f9...` | — | — | 0 |

Solver source SHAs pin: first gate `4deb7fe0...`, window `0bf4766d...`, fibre `ec14a1c2...`, ladder `0d4800a8...`, parent replay `f1b50bb2...`. Result JSON hashes on Box02 and Box03 are declared equal inside each freeze; stdout hashes are declared equal; stderr hashes differ in host-specific `time -v` fields. Launcher stdout/stderr are the empty-file digest `e3b0c442...`. The 0.08-second first gate has `start_utc=end_utc=2026-08-25T16:18:30Z` on both hosts (one-second clock). The window runs `16:27:55Z` to `16:27:59Z` on both hosts, matching 3.50 seconds elapsed. Box02 and Box03 are two executions of one implementation, as the producers state.

`MANIFEST.sha256` / `FREEZE.sha256` internally list those same result, source, and producer-report hashes. Cryptographic recomputation of file digests was not performed locally. The first-gate producer reports a source-closure SHA `c9ea6b8c...` that does not appear as an artifact in the frozen case; the pinned parent and solver source SHAs do.

## 8. Off-by-one firewall

`243^2=3^{10}=59049`. For modulus `3^{5+k}` with `k<=5`, the quadratic `3^{10} det J(T)` is 0, so the linear congruence is exact, not approximate. At `k=5` one has `D5 + 243 A(T) ≡ 0 (mod 3^{10})`, hence `det J(F)-1 ≡ 0 (mod 3^{10})`. The next divided carry, for a lift to `3^{11}=177147`, is

```text
(D5 + 243 A(T))/3^{10} + det J(T) ≡ 0  (mod 3),
```

in which `det J(T)` is quadratic in the 182 coefficients. No linear Bockstein is licensed there. The window solver records `quadratic_coefficient_valuation=10` and `quadratic_enters_divided_carry_for_transition=3^10_to_3^11`, and refuses that transition in `refusal_scope`.

## 9. Scope

The body, preregistrations, and refusal lists match the licensed object: full staged affine D12 families over one displayed B9 mod-243 point, through `3^{10}`. They refuse the complete earlier mod-243 fibre, an inverse limit, a `Z_3` point, a characteristic-zero map or collision, a counterexample, a maximum-twelve theorem, TD6, JC2, and the `3^{11}` gate.

---

## Mathematical defects

None.

## Source typing

The Jacobian is the `(x,y)` determinant of the integer pair `(P5,Q5)`; the special-fibre operator `D` is used only by the TD6 parallel first gate and agrees with `A` modulo 3. Column order, ambient, and free-zero RREF are uniform. No illicit reduction of binomial mixed terms, no Freshman `u^3`/`u^4`, no conjugacy claim.

## Software nits (non-blocking)

1. The 8,281 pair controls check that the mixed-pair quadratic remainder is 0 modulo `243^2`. They do not coefficient-match `243 det J(T)`. The producer sentence “every P/Q fresh pair contributes exactly `243^2` times its Jacobian” overstates the control. The identity is independently the bilinear expansion of `det`.
2. The mixed-pair loop uses truncating `// 243` without the exact-divisibility assert present on unit columns. Under the identity the division is exact.
3. Dead locals: pair-loop `linear`; window `previous_particular_T`.
4. `run_aws.sh` does not set an address-space `ulimit`; the first-gate README's “4 GiB cap” is not in that script. RSS is under 23 MiB.

## Custody and wording nits (non-blocking)

1. First-gate source-closure SHA `c9ea6b8c...` is reported but not deposited in the frozen case. Solver and parent source SHAs are deposited and consistent.
2. Empty launcher stdout/stderr on every host. Dual-host identity is carried by `solver.stdout`, `result.json`, `solver.rc=0`, and distinct `time -v` stderr.
3. Sub-second first gate records identical start and end timestamps on both hosts.
4. “Identically zero ambient rows” in the TD6 README is `F_3`-zero on `D` and the target, which is the correct dropping criterion for that first gate. The 276-row solvers do not claim integer vanishing.
5. Box02/Box03 remain two executions of one implementation, not two implementations.

None of these changes an identity, a rank, a particular, or the firewall.

## Separated verdicts

| Axis | Verdict |
|---|---|
| Mathematics | **CONFIRMED** |
| Source typing | **CONFIRMED** |
| Software | **CONFIRMED** |
| Custody | **CONFIRMED** |
| Wording | non-blocking overclaim on pair-control strength; source-closure hash not deposited |
| Overall | **CONFIRMED** |
