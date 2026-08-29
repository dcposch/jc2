# Hostile review — tied square/D1 `(a,c,r)=(1,5,2)` maximal-pole producer

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_d1_tied_a1c5r2_maxpole2_20260826/` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Earliest missing source family | none |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Producer PASS markers, V1/V2 names, and prior reviews are not authority |
| Method | SHA-256 of every named pin and evidence file; compiled-script inspection; independent four-summand atom census with padded replay; hand reconstruction of `N2_full`, the remainder modulo `L^2`, the ordinary quotient, both root/derivative functionals, and both deck terminals. No Singular, Sage, msolve, Lean, or package compiler was executed by the reviewer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of every required primary pin matches. Every path named in `PRODUCER_FREEZE.sha256` (8 rows), source `FREEZE.sha256` (17 rows), and `EVIDENCE.sha256` (36 rows) rehashes to the printed digest. All three nested V2 `compiled.sha256` files, and all three nested V1-failed `compiled.sha256` files, rehash to the retrieved local compiled scripts and inventories once the AWS absolute prefixes are stripped. The `/tmp` V2 source archive rehashes to the claimed digest. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

On the frozen generic square/D1 unit-load chart `D(p*k0)`, the exact contact cell

```text
ord(A)=1,  ord(C)=5,  ord(R)=2
```

is scheme-theoretically empty at absolute grade 16. The complete polar source through that grade is exactly four primitives, all first occurring in grade 16, with unique pole-two family `RA2`. After clearing `L^2`, the Laurent/Faber tail is the remainder of the displayed rational numerator modulo `L^2`, not the full cleared polynomial. The two same-root charts of nonzero linear `A,R` are unit ideals from that remainder. The two opposite-root charts divide by `L` exactly; at the root occupied by `A` the quotient terminal is the deck pair `±(5/2) k0 λ^3 bu^3`, equivalently the derivative unit `5 k0 λ^4 bu^3`. Both are nonzero after inverting only `λ`, `k0`, and the named nonzero root value of `R`. Faithfully flat descent from the finite étale splitting cover of `L` on `D(p)` gives emptiness on the base chart.

The V1 literal equality `N2 = N2_full` is only a normalization sentinel: V1 already possessed every root functional, allocation, terminal, and negative control, and a separate exact division identity exhibits the discarded ordinary quotient. V2 changes only that sentinel. The old hand-triage sentence that at `c=5` the family `AC` may cancel the post-allocation `R^3` pole is refuted on this cell: after opposite-root allocation those poles occupy different roots, and at the `A` root `AC`, `A^2`, and divided `RA2` vanish while `R^3` is the displayed unit.

The statement does not cover another face, another load chamber, `p=0`, `k0=0`, the exact-square zero section, terminal/Taylor receivers, fan exhaustiveness, order two, `(8,12)`, maximum twelve, or JC2. The triage memo is not edited.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Primary pins | six claimed SHA-256 | **holds** |
| 0. Named manifests | `PRODUCER_FREEZE` 8/8, `FREEZE` 17/17, `EVIDENCE` 36/36 | **holds** |
| 0. Nested compiled manifests | three V2 + three V1, two rows each | **holds** against retrieved local files |
| 1. Exact `Q` vs two good primes; zero swap; validator | separate hosts/rings; fail-closed | **holds**; exact `Q` is the endpoint |
| 2. Polar census through grade 16 | independently from four binomials | exactly `AC, A2, R3, RA2`; all start at 16; unique pole-two is `RA2` |
| 3. Seven literal rows, extraction, Faber bridge, ceilings | first grade equals ceiling | **holds**; no normal/connection jet and no target at grade 16 |
| 4. `N2_full` vs remainder vs ordinary quotient | identities; V1 sentinel | **holds**; V1 failure is only `N2 = N2_full` |
| 5. Four root-value charts | `2λ`; same-root units; opposite residual; scheme | **holds**; no omitted chart, no radical, no extra inverse |
| 6. Both deck quotients and derivative terminals | `±(5/2)k0 λ^3 bu^3` and `5 k0 λ^4 bu^3` | **holds**; `AC`, `A2`, divided `RA2` vanish at the `A` root; `R3` cannot cancel |
| 7. Omitted-`R3` control; first pole is allocation; étale descent; firewall; triage sentence | | **holds**; “at `c=5`, `AC` may cancel” is refuted on this cell |

---

## 0. Custody

Recomputed SHA-256 of the required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../RESULT.md` | `f09b44f18011e592f8366a380d1bba723a223d4c424fbf9cbfa951a8de87d994` | producer report |
| `.../PRODUCER_FREEZE.sha256` | `7813393ee756923f73754fd6c3e1ba8e153594ffa7ccf3963926e765761adede` | producer-level freeze |
| `.../EVIDENCE.sha256` | `d4802e87047438882c5f825980d7bf622436636e4a94c8c8429ad46a826a8be1` | evidence freeze |
| `.../FREEZE.sha256` | `b7f931512b676500fe93504c5598837ad0fa2c834a1e1d9d37504550ffe2ed08` | source freeze |
| `/tmp/jc2_d1_tied_a1c5r2_maxpole2_20260826_v2.tgz` | `4b903ffcb76b3d584f64105b821372d82580ad851415e1538d7dc84bd8a5367d` | V2 source archive |
| `xmodel/max12-812-order2-square-maximal-pole-row-syzygy-miner-spec-20260826.md` | `c4eba2d79521d6c621223dc1b36bb298e7a805bf1cd595b593f444d14f148358` | generic miner specification |

`PRODUCER_FREEZE.sha256` names eight files, all matching, including `EVIDENCE.sha256`, source `FREEZE.sha256`, `FAILED_ATTEMPTS.md`, both V1-failed archive pointers, and the V2 archive pointer `9a32cd84…`.

Source `FREEZE.sha256` names seventeen files, all matching. Ancestry pins consumed by the compiler also rehash: r1/d1 `compile_r1_d1_ac.py` `e024a13d…` and its freeze `34b0f325…`; CGE3 `compile_cge3_universal.py` `352ad4f2…` and its freeze `a5efc70c…`; `ops/aws_exact_lane.sh` `ebe06a10…`; V1-failed compiler `6967836a…` and V1 preregistration `ad7a8a3b…`. Frozen tails `d72f774c…` and canonical all-tails `6eed03d4…` rehash; the seven rows have 36/54/58/81/89/120/131 monomials.

`EVIDENCE.sha256` names 36 files; all 36 rehash. Nested V2 `compiled.sha256` rows, which record AWS absolute paths, match the retrieved local compiled objects:

| Lane | `source_inventory.json` | `.sing` |
|---|---|---|
| exact `Q` / Box02 | `67922f35…` | `7d544c52…` |
| `F_65519` / Box03 | `b054e400…` | `e8a1067f…` |
| `F_65521` / r6d | `5603acff…` | `d29f494f…` |

The three V2 compiled scripts differ by exactly the ring-characteristic token (`Rtied=0` / `65519` / `65521`). Substitutions, recurrences, charts, terminals, and sentinels are otherwise identical. All three inventories report `primitive_count=4` and `target_jet_count=0`.

The V1 no-verdict archive `/tmp/jc2_d1_tied_a1c5r2_maxpole2_20260826_v1.tgz` rehashes to `e564be31…`. Nested V1 compiled objects rehash. V1 is not cited as a producer PASS.

A passing manifest is not a mathematical verdict. The algebra below is independent of those sentinels.

---

## 1. Exact `Q`, two good-prime controls, swap, validator

Exact `Q` is the theorem endpoint. `F_65519` and `F_65521` are software/support controls only. They are genuinely separate frozen runs.

| Charge | Exact `Q` (Box02) | `F_65519` (Box03) | `F_65521` (r6d) |
|---|---|---|---|
| Host | `ip-172-30-0-186` | `ip-172-30-0-249` | `ip-172-30-0-45` |
| Tag | `…_v2_q_box02_20260826T1935Z` | `…_v2_p65519_box03_20260826T1935Z` | `…_v2_p65521_r6d_20260826T1935Z` |
| Characteristic | `0` | `65519` | `65521` |
| Compiled script SHA | `7d544c52…` | `e8a1067f…` | `d29f494f…` |
| Engine `rc` | `0` | `0` | `0` |
| Validator | `PASS_D1_TIED_A1C5R2_MAXPOLE2_EMPTY` | same | same |
| Stdout SHA | `40614e98…` | same structural payload | same |
| Peak RSS / swaps | 19,712 KiB / 0 | 20,100 KiB / 0 | 19,880 KiB / 0 |
| Source archive in registration | `4b903ffc…` | same | same |

Both control primes are prime, neither divides `2,3,5,32`, and both are odd, so the denominators `2,4,8,16,32` and the numerator `5` remain units. The two validation files are byte-identical (`engine_rc=0` plus the same validator line), hash `3f508c08…`; that common payload is not evidence that the runs were copied. Identical stdout is expected: on success the script prints only `0/1` markers and fixed diagnostic strings. All three `freeze_check.stdout` records are byte-identical and report every `FREEZE` row OK. All three metas record `argv` as `timeout 1800` wrapping the lane-local V2 compiler then `Singular -q` on the emitted script, return code 0, and stdout hashes matching `EVIDENCE.sha256`. Compiler stderr is the empty-file digest `e3b0c442…` on all three lanes. Caps were 16 GiB virtual (`16777216` KiB) and 1800 s engine.

The fail-closed validator requires each listed marker exactly once, including `T15_COMMON_N2=1` and `T15_ENDPOINT=PASS_EMPTY_A1_C5_R2_ON_D_P_K0`, and rejects `=FAIL`, `// **`, a leading `?`, `error occurred`, and `Swaps: [1-9]`. V1 was rejected at `FAIL_MISSING_OR_NONUNIQUE:T15_COMMON_N2=1` after engine `rc=0`, which is the correct fail-closed behaviour. Neither V2 stdout nor stderr contains the rejected patterns. Zero swap is recorded on every V2 and V1 stderr.

The printed strings `T15_QUOTIENT_TERMINALS=…`, `T15_DERIVATIVE_TERMINALS=…`, and `T15_FIRST_POLE_ONLY=ALLOCATION_NOT_ENDPOINT` are compile-time constants. The corresponding integer identities live in `T15_endpoint`. Those strings are not mathematical evidence; the identities are reconstructed below.

---

## 2. Independent polar census

The frozen square source is `f=K^2+σ^5 D` with `K=L^2+σ^2 R` and `D=LA+C`. Factoring `f=L^4(1+x)` gives the four atoms

```text
x = 2 σ^2 R/L^2 + σ^4 R^2/L^4 + σ^5 A/L^3 + σ^5 C/L^4
```

of `σ`-costs `(2,4,5,5)` and denominators `(2,4,3,4)`, with scalars `(2,1,1,1)`. The four binomial summands are

```text
f^{3/2},   σ^4 k10 f^{5/4},   σ^{12} k6 f^{3/4},   σ^{20} k2 f^{1/4},
```

i.e. alphas `3/2, 5/4, 3/4, 1/4`. Pole order is `denominator - 4α`. Contact costs on this cell are `ord(A)=1`, `ord(C)=5`, `ord(R)=2`, so atom costs become `(4,8,6,10)`. The unit-load chart names `k10` as `k0`.

Independent expansion through grade 16, with atom bounds `budget // cost` and with one extra count in every atom direction, produces identical retained signatures. Every positive atom cost is at least 4 on this baseline, so a degree-`(bound+2)` tuple already exceeds the ceiling. There is no cutoff hole.

Aggregation by `(summand, load, fixed, eR, eA, eC, pole)` produces two genuine zeros:

```text
unloaded R^4 / L^2 at grade 16:  (4 r1) + (2 r1 + 1 r2) + (2 r2)
                                  3/8  +     -3/4      +  3/8  = 0
unloaded R^2 A / L  at grade 14:  (1 r2 + 1 a) + (2 r1 + 1 a)
                                  3/4          + -3/4           = 0
```

Those monomials are absent from the source, not hidden by a leftover coefficient. No cancelled key reappears after padding. The k6 linear `R` term at grade 16 has pole `-1` and is ordinary; k2 has fixed weight 20 and is out of window.

The nonzero polar inventory is exactly four families, all of first grade 16:

| Family | Summand | Coefficient | Pole | First grade |
|---|---|---|---|---|
| `AC` | unloaded | `3/4` | 1 | 16 |
| `A2` | `k10` | `5/32` | 1 | 16 |
| `R3` | `k10` | `5/16` | 1 | 16 |
| `RA2` | unloaded | `-3/8` | 2 | 16 |

The `R3` coefficient is itself an aggregation: three type-1 `R` contributes `-5/16` and one type-1 plus one type-2 contributes `+5/8`, summing to `+5/16`. The unique pole-two family is `RA2`. There is no fifth polar primitive and no polar k6 or k2 through grade 16.

This census is taken from the frozen generating function. It does not import a support-miner emptiness claim.

---

## 3. Seven rows, extraction, bridge, and first-grade ceilings

The compiled source rows are `tail_text` of the frozen seven-row tails, with `Lambda → σ^2` and the target subtractions

```text
row 1,3,5: 0
row 2: σ^{28} μ2
row 4: σ^{32} μ4
row 6: σ^{36} μ6
row 7: σ^{38} (J/4)
```

which is the same `2(12+row)` timing as the frozen CGE3 emitter. Extraction divides by `σ^{16}`, substitutes `σ=0`, and forbids residual dependence on `k6`, `k2load`, `μ2`, `μ4`, `μ6`, and `J`. Recursive quotients check exact division at each `σ`-step. Because the ceiling equals the first polar grade, there is no further jet to peel: the seven leading coefficients are the entire in-window source.

No target can occur at grade 16: the earliest target is `μ2` at grade 28. After dividing `Φ_2` by `σ^{16}` the target remainder is still `σ^{12} μ2`, which vanishes at `σ=0`. The forbidden-derivative check would additionally catch any illicit in-window target monomial.

No delayed load other than unit `k0` can occur as a polar family: k6 polar requires denominator at least 4 and remaining budget 4, which cannot buy a polar atom; the only in-window k6 monomial is ordinary `k6 R`. k2 starts at weight 20. The extracted grade-16 rows are therefore unit-load by support, not by setting `k6=k2=0` by hand.

No normal jet can occur at the first grade. The compiled ring carries only the leading two coefficients of each of `A,C,R`, at exact orders `σ^1`, `σ^5`, `σ^2`. The next `σ`-jet of any of those forms raises the grade by 1 and would be a grade-17 family.

No connection jet can occur at the first grade. The Faber bridge is the frozen lower-unitriangular transform `T_{ij}(p)` at the same grade. Independently, `T_{ij}` is zero unless `i-j` is a nonnegative even integer `2n`, with leading coefficient

```text
(∏_{k=0}^{n-1} (j/2 + k)) / (n!  2^n)  p^n.
```

This reproduces the compiled same-grade identities

```text
g1 = h1
g2 = h2
g3 = (p/4) h1 + h3
g4 = (p/2) h2 + h4
g5 = (3/32) p^2 h1 + (3/4) p h3 + h5
g6 = (1/4) p^2 h2 + p h4 + h6
g7 = (5/128) p^3 h1 + (15/32) p^2 h3 + (5/4) p h5 + h7.
```

The `σ^1` and `σ^2` columns of `T_{ij}` involve `ell1` and `ell2`. The compiled `row_checks` include those columns only when the grade offset is at least 1 or 2. Here minimum = maximum = 16, so the offset is 0 and the connection columns are absent. The ring does not even declare `ell1`. The analytic receiver likewise uses undeformed `L=z^2+p/2`. That is the mechanical reason the first-grade source cannot see a moving connection.

The analytic generating function at this contact, after extracting `σ^{16}`, retains only the four polar families of §2:

```text
(3/4) t A C inv1  - (3/8) t^2 R A^2 inv2
+ (5/16) k0 R^3 inv1  + (5/32) k0 t A^2 inv1,
```

with `A=a1+a0 t` and `inv_q = (1+(p/2)t^2)^{-q}` through `t^8`. The later primitives `C^2`, `A^3`, `k0 RC`, `k0 R^2 A` start at grades 20, 18, 18, 18 and are absent. Completeness of this truncated `H` at grade 16 is the census, not an extra hypothesis.

---

## 4. Pole-two numerator, ordinary quotient, recurrences, V1 sentinel

Let `L=z^2+p/2`. The four polar families clear against `L^2` to

```text
N2_full = (3/4) A C L + (5/32) k0 A^2 L
        + (5/16) k0 R^3 L - (3/8) R A^2.             (1)
```

This is a polynomial of degree 5. The Laurent/Faber tail discards the ordinary part, so the reconstructed numerator `N2` is the unique remainder of (1) modulo `L^2`, of degree at most 3. Polynomial division gives the exact ordinary quotient

```text
Q_ord = (3/4) a1 c1 + (5/32) k0 a1^2
      + (5/16) k0 (b1^3 z + 3 b1^2 b0),              (*)
```

and the identity `N2_full = N2 + L^2 Q_ord` holds with no remainder. The three summands of `(*)` are respectively the `z^4` parts of `AC L` and `k0 A^2 L` and the `z^5,z^4` parts of `k0 R^3 L`. In particular `Q_ord` is not zero, so `N2 ≠ N2_full` as polynomials.

The analytic reconstruction with `h_j = [t^{j+1}] H` and

```text
N2 = h1 z^3 + h2 z^2 + (h3 + p h1) z + (h4 + p h2)
```

equals that remainder identically. The denominator recurrences

```text
h5 + p h3 + (p^2/4) h1 = 0,
h6 + p h4 + (p^2/4) h2 = 0,
h7 + p h5 + (p^2/4) h3 = 0
```

hold identically; the signs are those of `L^2 = z^4 + p z^2 + p^2/4` and of `inv_2 = (1+(p/2)t^2)^{-2}`.

After `p = -2λ^2`, the Faber combinations

```text
Ψ± = g4 ± λ (g3 + (p/4) g1),
DΨ± = g3 ± 2λ g2 - (3p/4) g1
```

are tautologically `N2(±λ)` and `N2'(±λ)` given the same-grade transform of §3. Independently of the transform, evaluation of the remainder at a root of `L` agrees with evaluation of (1), because `L^2 Q_ord` vanishes there:

```text
N2(±λ) = -(3/8) R(±λ) A(±λ)^2.                       (2)
```

That is the first pole functional, derived from the source rather than imposed.

V1 demanded the polynomial equality `N2 = N2_full` and printed `T15_COMMON_N2=0` on all three AWS lanes, with every other listed identity equal to 1, including both root Faber identities, both derivative syzygies, all four charts, both exact `L` quotients, both terminals, both unit ideals, and the omitted-`R3` control. The fail-closed validator rejected those runs at `T15_COMMON_N2=1`. V2 replaces that test by `N2 ≡ N2_full (mod L^2)` together with the exact division identity against `(*)`. A line-diff of the two compilers shows no other mathematical change: the census, seven-row extraction, charts, terminals, localizations, and scope are identical; V2 additionally prints a version marker and pins the V2 preregistration. The V1 failure is only a normalization sentinel. It does not conceal a defect in the root obstruction.

---

## 5. Four root-value charts

Work on the finite étale splitting cover `L=(z-λ)(z+λ)` of `D(p)`, with `λ` inverted. For linear forms the two-root evaluation map has matrix `[[1,λ],[1,-λ]]` and determinant `-2λ`. The compiled check `std(2λ, iλ·λ-1)` being the unit ideal is the statement that `2` is a unit once `λ` is a unit, which holds in every registered characteristic. Consequently every nonzero linear `A` (resp. `R`) is nonzero at at least one root, and the four opens

```text
D(A(+) R(+)),  D(A(+) R(-)),  D(A(-) R(+)),  D(A(-) R(-))
```

cover every nonzero linear pair. There is no fifth chart: a linear form vanishing at both roots is identically zero, which is outside the contact.

On `D(A(+) R(+))` the identity (2) reads `-(3/8) R(+) A(+)^2 = 0` with both factors units, so the localized ideal is already `(1)`. The same holds at `-λ`. These are scheme-theoretic unit ideals: the compiler takes `std` of the pole equation plus the two inverses and `iλ·λ-1`, and tests `reduce(1)=0`. No radical and no saturation are used.

On `D(A(+) R(-))`, (2) at `+λ` forces `R(+)=0` because `A(+)` is a unit, and (2) at `-λ` forces `A(-)=0` because `R(-)` is a unit. That is the opposite allocation

```text
A = au (z+λ),   R = bu (z-λ)
```

up to units. The symmetric open `D(A(-) R(+))` is the deck conjugate. The residual ideals compiled on those opens are

```text
(Ψ+, Ψ-, DΨ-,  iA(+) A(+)-1, iR(-) R(-)-1, iλ λ-1, ik0 k0-1)
(Ψ+, Ψ-, DΨ+,  iA(-) A(-)-1, iR(+) R(+)-1, iλ λ-1, ik0 k0-1).
```

The extra generator is the derivative at the root occupied by `A`. After the allocation, `R(-) = -2λ bu` (resp. `R(+) = 2λ bu`), so inverting `R(-)` and `λ` inverts `bu` without a separate inverse of the leading coefficient. Likewise `A(+) = 2λ au`. The only inverted quantities are `λ`, `k0`, and a named nonzero root value of `A` and of `R`. That is the exact-contact inverse on `D(p*k0)` for nonzero linear `A,R`. `C` is not inverted; emptiness without inverting `C` is stronger than the contact `ord(C)=5`. There is no inverse of `L`, no inverse of a connection, and no inverse of a higher jet.

Once the derivative generator is included, §6 shows it is the unit `5 k0 λ^4 bu^3`. The residual ideals are therefore unit ideals. Because `reduce(1)=0` on `std` of those ideals, there are no residual nilpotent or embedded points on these charts. The cover of nonzero linear `A,R` is scheme-theoretically empty.

---

## 6. Both deck quotients and the unmatched `R3` terminal

On each opposite-root allocation, `N2(±λ)=0`, and `N2` has degree at most 3, so `L` divides `N2` exactly. Write `Q1=N2/L`. At a simple root, `Q1(λ)=N2'(λ)/(2λ)`. Differentiating (1) on `A=au(z-λ)`, `R=bu(z+λ)` at `z=λ` gives vanishing of every summand that still contains a factor of `A` or of `L`, and the single surviving derivative

```text
d/dz[(5/16) k0 R^3 L ]|_λ = (5/16) k0 (2λ bu)^3 (2λ) = 5 k0 λ^4 bu^3.
```

Hence

```text
Q1(λ) = (5/2) k0 λ^3 bu^3,                                (3)
N2'(λ) = 5 k0 λ^4 bu^3.                                   (4)
```

The deck conjugate `A=au(z+λ)`, `R=bu(z-λ)`, evaluated at the `A` root `z=-λ`, produces `Q1(-λ)=-(5/2) k0 λ^3 bu^3` and the same derivative value (4). Both identities were also checked by substituting the allocation into the remainder `N2` reconstructed in §4, not only into `N2_full`; the ordinary part `L Q_ord` vanishes at either root and does not affect the terminal.

At the nominated `A` root:

- `AC` contributes `(3/4) A C` to `Q1`, which vanishes with `A`;
- `A2` contributes `(5/32) k0 A^2`, which vanishes with `A`;
- divided `RA2` is `-(3/8) R A^2 / L = -(3/8) bu au^2 (z-λ)` on the first orientation, which vanishes at `z=λ`;
- `R3` contributes `(5/16) k0 R(λ)^3 = (5/2) k0 λ^3 bu^3`, which is a unit on `D(λ k0 bu)`.

No linear combination of `AC` and `A2` can cancel (3). The hand-triage possibility that `AC` cancels the post-allocation `R^3` pole does not occur, because those poles sit at opposite roots.

---

## 7. Negative controls, descent, firewall, triage sentence

Omitting `R3` from (1) leaves a numerator still divisible by `L` on the same allocation, with quotient terminal 0 at the `A` root. That is the compiled omitted-`R3` control, and it is the same identity obtained by deleting the only surviving derivative in §6.

Stopping after (2) does not yield emptiness. On `D(A(+) R(-))` the pair of root equations cuts out the allocation `R(+)=A(-)=0` with `au`, `bu`, and the two coefficients of `C` still free. That locus is nonempty (e.g. `λ=1`, `au=bu=k0=1`, `A=z+1`, `R=z-1`). The first pole functional therefore allocates and does not finish. The producer prints this as a constant string rather than compiling a non-unit test of the Ψ-only residual ideal; the geometry of that residual is nevertheless immediate and is not a missing source family.

Descent is from the finite étale cover `Z[λ,λ^{-1}] → Z[p,p^{-1}]` adjoining a root of `λ^2+p/2`, whose discriminant is a unit times `p` on `D(p)` in the registered characteristics. Emptiness after a faithfully flat cover is emptiness on the base. The inverted elements on every chart of the cover are among `{λ, k0, A(±λ), R(±λ)}`, all already units on `D(p*k0)` with nonzero linear `A,R`.

Firewall, as claimed: the result eliminates only this equality vector on `D(p*k0)` at grade 16. It does not treat another lower-hull face, a positive-order or ramified load, `p=0`, `k0=0`, the exact-square zero section, terminal or Taylor receivers, fan exhaustiveness, order two, `(8,12)`, maximum twelve, or JC2.

The prior hand triage left `(1,5,2)` open because, after the opposite-root allocation forced by `L | R A^2` on the `c≥6` boundary, it allowed the newly arriving simple pole `AC/L` at `c=5` to cancel `R^3/L`. On the actual grade-16 source those two simple poles occupy opposite roots, and the exact quotient at the `A` root is the unit (3) with no `AC` contribution. The sentence “at `c=5`, `AC` may cancel” is therefore false for this cell. The triage memo is not edited.

---

## Scope reminder

This confirmation is the emptiness of the unit-load D1 cell `ord(A)=1`, `ord(C)=5`, `ord(R)=2` on `D(p*k0)` through absolute grade 16, and nothing else.

CONFIRMED
