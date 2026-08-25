# Hostile different-model review — normalized B9 common-cubic family at `3^11`

| Field | Value |
|---|---|
| Producer | `xmodel/as-b9-9-12-common-cubic-3p11-producer-20260825.md` (SHA-256 `b3a86bbd55ed99ca60dfc3eeb89560dbc483265db603de0bec4a26e63d673a2b`) |
| Frozen case | `cases/as_b9_9_12_common_cubic_3p11_20260825/` |
| V2 erratum | `xmodel/as-b9-9-12-common-cubic-v2-zero-divisor-erratum-20260825.md` (SHA-256 `cb07f729ca3a8cf32b07d7c8e4ed2cc9cf178750f21a06bb38342eb4dea4722c`) |
| V2 quarantine case | `cases/as_b9_9_12_common_cubic_v2_zero_divisor_erratum_20260825/` |
| Independent compiler | `INDEPENDENT_AUDIT_BOX02/independent_common_core.py` (SHA-256 `460199584e128bc2c5f3196871a34437ebdfd7d674ccf0bcc2f52b9db8ace6b8`) |
| Overall verdict | **CONFIRMED** |
| Mathematics | **CONFIRMED**, including the displayed `F_3`-digit counts `3^{95}` and `3^{150}` after the parameterization/containment audit the producer left provisional |
| Source typing | **CONFIRMED** |
| Software | **CONFIRMED** (non-blocking notes below) |
| Custody | **CONFIRMED** of the frozen dual-host V3 emitters (Box03 and r6d), the Box02 independent reconstruction, and the separate V2 quarantine package. Box03/r6d are two executions of one V3 wrapper, plus a second modulus-repair emitter that matches byte-for-byte |
| Wording / scope | **CONFIRMED** of the licensed finite congruence claim. `3^{150}` is an `F_3`-digit count of one displayed Hensel parameterization, not a scheme fibre dimension and not a characteristic-zero Q8 landing |
| Mathematical defects | none |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Evidence | source audit of V2, V3, the independent 149-coordinate compiler, and the witness verifier; independent SHA-256 of freeze/manifest/closure/SMT/result/ANF/witness; AST constructor inventory; V2 SMT/DIMACS zero-divisor inspection; byte comparison of three V3 formulas; combinatorial counts `55+91=146`, `276`, `10+13=23`; rank-nullity of the stored stage table; independent scan of all `81^3` parent-level monic cubics; independent polynomial replay of the witness on all 276 determinant slots and all 23 top-form rows; short local re-execution of the independent compiler matching the frozen AWS Box02 bytes. No Z3/Boolector/CaDiCaL launch |
| Git HEAD | `d0f6edfbfcd8fbe4c77ffadcd336df349c11eb7e` (producer, this case, and the V2 erratum uncommitted) |
| Review window | 2026-08-25 |

## Verdict

**CONFIRMED**

V2 is an invalid formula: its residue constructor reduced the modulus constant itself, every intended `bvurem` by `177147` became a remainder by zero, and each `h_i < 177147` bound became `h_i < 0`. The frozen V2 SMT bit-blasts to the empty-clause DIMACS `p cnf 0 1`. No V2 solver or proof byte is consumed. V3 splits residue and raw-modulus constructors, encodes the positive divisor `(_ bv177147 64)`, and is byte-identical across Box03, r6d, and an independently repaired emitter at SHA-256 `5af9efbe4b138f1cb0408099c90283842b4ef0b0fef9d7d33447d51a29d53563`.

A source-independent 149-coordinate compiler that never reads producer SMT, run on AWS Box02 and re-executed from the same source, constructs the 299-row common-core system from the pinned linear-window parent and yields stage ranks/family dimensions `94/55, 123/81, 131/99, 132/116, 132/133`. At the first quadratic gate the 133 predecessor directions split invertibly into 17 active and 116 spectators; the fresh operator is `299×149` of rank/kernel/cokernel `94/55/205`; the spectator image in the cokernel has rank 38; the reduced obstruction is empty. The displayed parameterization therefore has `3^{95}` liftable predecessors and `3^{150}` complete next-stage tuples. One explicit point with

```text
H ≡ y^3 + 119880 x y^2 + 40581 x^2 y  (mod 177147)
```

replays all 276 determinant rows and all 23 top-form rows, reduces to the displayed B9 parent modulo 243, has leading units `(2,1)` modulo 3, and has exact total-degree pair `(9,12)`.

This is one fixed-parent finite-depth integral congruence. It is not a lift past `3^{11}`, not an inverse-limit or characteristic-zero point, not a Q8 landing, not a maximum-twelve theorem, not a counterexample, and not JC2. Stopped V3 Boolector/Z3 searches are custody, not solver evidence.

## Strongest exact claim

Fix the displayed B9 point `(p5,q5)` of source SHA-256 `f1b50bb2c3e21369da205ebcf1ba028eede20c89d5ad863253fdfec4d6d28c5d`, determinant one modulo 243. Inside the complete normalized total-degree box `deg P ≤ 9`, `deg Q ≤ 12`, impose the integral common-cubic incidence

```text
H = y^3 + h1 x y^2 + h2 x^2 y + h3 x^3,
P9 = P_(0,9) H^3,
Q12 = Q_(0,12) H^4,
h1,h2,h3 ≡ 0 (mod 3),
P_(0,9), Q_(0,12) units modulo 3.
```

The monic parent cubic is uniquely `[1,81,0,0]` among all `81^3` candidates with `h_i ≡ 0 (mod 3)` modulo 243. The complete displayed deformation space of that parent in the 149-coordinate box (146 map coefficients plus three `H` digits) has linear Hensel fibres of `F_3`-dimension `55,81,99,116,133` at moduli `3^6,…,3^{10}`. After an invertible change of the 133 predecessor coordinates, every assignment in `F_3^{17}` lifts through the first quadratic gate: the 116 spectators have rank 38 in the 205-dimensional fresh cokernel, and the reduced system has zero equations. The displayed `F_3`-digit parameterization therefore has cardinality `3^{17+(116-38)}=3^{95}` on the predecessor projection and `3^{95+55}=3^{150}` after the fresh kernel. One zero-active witness has `det J(P,Q)≡1 (mod 177147)` on all 276 ambient slots, both leading units, and honest degrees `(9,12)`.

## Sharpest non-claim

A finite-depth parameterized count and one literal point over **one** B9 mod-243 parent. Not a scheme-theoretic fibre dimension, not survival to `3^{12}`, not an inverse-limit/`Z_3` point, not a characteristic-zero Keller map, not a source-honest landing in the selected Q8 chart, not complete earlier-parent coverage, not a maximum-twelve theorem, not a counterexample, and not JC2. V2 `UNSAT` is an encoding negative control. Stopped V3 solvers are not a SAT certificate. Box03 and r6d do not supply a second mathematical solution of the independent 149-coordinate system.

---

## Evidence layers (do not collapse)

1. **Source/compiler correctness.** V2, the V3 wrapper, the independent `modulus_bv` repair, the 149-coordinate compiler, and the witness verifier were read. Residue versus raw-modulus constructors, 64-bit overflow, 276+23 row inventory, the unique parent cubic, the `GL(133,Z)` split, and the coefficientwise containment test are correct as written. Rank arithmetic `17+116=133`, `94+205=299`, `149-94=55`, `116-38=78`, `17+78=95`, `95+55=150` is tautological given those ranks.
2. **Two-host V3 emission plus a second repair.** Box03 and r6d executed the same V3 wrapper (patched source SHA-256 `7dfe73ea…`) and emitted byte-identical canonical SMT, Boolector SMT, and `emit_result.json`. The independent audit emitter `emit_common_cubic_fixed_audit.py` (SHA-256 `d157c7e2…`) is a distinct source that never uses `bv(MODULUS)`; its canonical SMT is nevertheless byte-identical. Distinct `/usr/bin/time -v` stderr hashes show two V3-wrapper processes. This is custody that the audited constructors ran, plus one independent formula match.
3. **Independent 299-row reconstruction.** The Box02 compiler at SHA-256 `46019958…` does not parse SMT. A short local re-execution of that same source produced byte-identical `independent_result.json`, empty ANF, and witness payload. That is a second execution of one implementation, not a second algorithm.
4. **Literal SAT, not a solver model.** The load-bearing SAT object is the integer witness and its separate polynomial replay. V3 Boolector/Z3 were sent `SIGTERM` after that witness landed (`unknown` / empty stdout, rc 15 and 143).

Stopped V3 searches and the V2 quarantine remain AWS custody. The independent compiler is a 5-second, 29 MiB job; it was re-run locally only as short validation against the frozen Box02 bytes.

---

## Charge 1 — V2 zero-modulus bug; no V2 `UNSAT` consumed

**CONFIRMED**

V2 source SHA-256 `ab85df4824042f9919e535ad9b2d9c4213deb1aa2ed953ae6fa6aed4c66a7556` defines

```python
def bv(value):
    return f"(_ bv{value % MODULUS} {WIDTH})"
```

and uses `bv(MODULUS)` both as the `bvurem` divisor (`modterm`) and as the strict bound `bvult h_i bv(MODULUS)`. Since `177147 % 177147 == 0`, the frozen V2 SMT at SHA-256 `182bc9f7302ba852b32d04899e6b7a86b38d0eaf0cb2faaa280717d4b9c70604` contains

```smt2
(assert (bvult h1 (_ bv0 64)))
```

and the identical impossible unsigned bounds for `h2,h3`. It contains **zero** copies of `(_ bv177147 64)` and 10631 `bvurem` gates, all but the five explicit remainder-by-three unit/cube checks using the zero divisor. Deterministic Z3 4.16 bit-blasting of that file is exactly

```text
p cnf 0 1
0
```

at SHA-256 `69ee12c3118a428a28f674ec24e362b721e0611c800f65afbcb8a48e778c1394`. Instant Boolector/Z3 `UNSAT`, CaDiCaL, and trivial DRAT verification certify the empty clause and say nothing about the common-cubic locus.

No V2 solver byte is in this report’s load-bearing chain:

- this case’s `FREEZE.sha256` pins the V3 formula, the independent result/witness replay, and the erratum note, not the V2 SMT or DIMACS;
- the independent result JSON contains neither `182bc9f7` nor `UNSAT`;
- the producer states that no V2 solver or proof byte supports it;
- V2 custody lives in the separate frozen package `cases/as_b9_9_12_common_cubic_v2_zero_divisor_erratum_20260825/` with quarantine reason `stopped-invalid-zero-divisor`.

Non-blocking erratum wording: the xmodel erratum’s “407 `bvurem` gates” is not the SMT-level remainder count (10631), and five remainder-by-three gates are not zero. The zero-modulus bug, the impossible `h_i < 0` bounds, and the trivial CNF are still exact.

## Charge 2 — V3 constructors, positive modulus, width, 276+23 rows

**CONFIRMED**

The V3 wrapper replaces the V2 residue constructor by a pair

```python
def bvraw(value):
    assert 0 <= value < 2 ** WIDTH
    return f"(_ bv{value} {WIDTH})"

def bv(value):
    return bvraw(value % MODULUS)
```

and rewrites the two source occurrences of `bv(MODULUS)` to `bvraw(MODULUS)`. Independent AST walk of the patched source (SHA-256 `7dfe73ea02f68434b1a548c51b69353a50e4d593f2d3e404e64c13790f49a98c`):

- 14 `bv(...)` call sites, none of whose arguments is `MODULUS`: `0`, `base+243*T_base[coordinate]`, `value`, `3**10`, `i*ell`, `-j*k`, the determinant target `1 if xy==(0,0) else 0`, `1`, and the five remainder-by-three literals;
- two raw-modulus uses `bvraw(MODULUS)` (the `bvurem` divisor and the `h_i` bound);
- a third `bvraw` node is the residue body `bvraw(value % MODULUS)`, not a raw-modulus constant.

The independent repair `emit_common_cubic_fixed_audit.py` uses a distinct `modulus_bv()` helper and the same 14 residue sites. Both print `variables_rows 294 276 23`.

Width/overflow: `WIDTH=64`, `MODULUS=3^{11}=177147`. Every residue constructor reduces modulo `177147` before emission. Stepwise `mulmod`/`addmod` reduce after each `H`-product. Determinant summands are `bvmul` of a coefficient at most `9·12=108` with a product of two reduced 64-bit residues; the unreduced maximum `108·177146^2 = 3389116174128` is strictly less than `2^{64}`. Negative Jacobian coefficients `-j*k` are emitted as Python residues in `{0,…,177146}`. The two raw constants satisfy `0 ≤ 177147 < 2^{64}`.

Row inventory, independent of SMT:

- monomials of total degree `≤9` number `10·11/2=55`;
- monomials of total degree `≤12` number `13·14/2=91`;
- the D12 determinant ambient of total degree `≤22` numbers `23·24/2=276`;
- top forms are 10 coefficients of `H^3` plus 13 of `H^4`, total 23.

The V3 formula declares 145 trit predecessors, 146 trit fresh digits, three `h_i`, 55 `p`-coordinates, 91 `q`-coordinates, 10 `h3_*` and 13 `h4_*` helpers, contains 767 `assert`s matching `276` determinant rows plus the 23 helper definitions, 23 top equalities, two leading-unit checks, six `h_i` bounds/divisibility asserts, 291 trit bounds, and 146 polynomial definitions, and writes `(_ bv177147 64)` 10629 times (every modular gate plus the three `h_i` bounds; the five remainder-by-three checks correctly use `(_ bv3 64)`). The bound `(assert (bvult h1 (_ bv177147 64)))` is present; the V2 bound `(assert (bvult h1 (_ bv0 64)))` is absent.

## Charge 3 — Byte equality of V3 SMT `5af9efbe…` and the independent repair

**CONFIRMED**

Independently recomputed SHA-256, all equal:

| Object | SHA-256 |
|---|---|
| `V3_BOX03/common_cubic_v3.smt2` | `5af9efbe4b138f1cb0408099c90283842b4ef0b0fef9d7d33447d51a29d53563` |
| `V3_R6D/common_cubic_v3.smt2` | `5af9efbe4b138f1cb0408099c90283842b4ef0b0fef9d7d33447d51a29d53563` |
| `INDEPENDENT_AUDIT_BOX02/common_fixed.smt2` | `5af9efbe4b138f1cb0408099c90283842b4ef0b0fef9d7d33447d51a29d53563` |
| Box03/r6d/fixed Boolector SMT | `2eb69355a0b85b6928899a619840ecb7856ee6e6cc2ef050ab76067e44c835f7` |
| Box03/r6d patched source | `7dfe73ea02f68434b1a548c51b69353a50e4d593f2d3e404e64c13790f49a98c` |
| Box03/r6d `emit_result.json` | `45a79eedbfcec2cd24b60f0fc5a5b3a91b25c2c6fdcd6f4f17afa433c2bcd4fe` |
| independent repair source | `d157c7e2e13b144eb299669a0861ccc0ed5d1b5030fd7e5441a008da7319c47a` |

Canonical SMT files are byte-identical, not merely same-hash. The independent emitter is a different program (`modulus_bv` versus a patched `bvraw`); agreement is a formula match, not a second run of the wrapper. The independent `emit_result_fixed.json` SHA differs (`f6d26c27…`) only because its status string is `SMT-EMITTED` rather than `SMT-V3-EMITTED`. Stopped-solver `INPUT.sha256` pins the same V3 formula, so the interrupted searches were of the repaired gate, not of V2.

## Charge 4 — Independent compiler `46019958…`; stage ranks `94/55,…,132/133`

**CONFIRMED**

The compiler source SHA-256 is `460199584e128bc2c5f3196871a34437ebdfd7d674ccf0bcc2f52b9db8ace6b8`, matching `independent_source.sha256`. It `exec`s only the linear-window parent `solve_linear_window_9_12.py` at the already-reviewed SHA-256 `fb4f16d808dfba754582fb1b5fe10dfa0e69bca0888b38f92586e1f5534724e2`. It does not open, parse, or hash any SMT: the tokens `smt2`, `common_cubic_v3`, `emit_common_cubic`, `5af9efbe`, `182bc9f7`, `boolector`, and `z3` are absent except for the comment that producer SMT is not consumed. AWS `JC2_ROOT` was the snapshot `…/source` tree, which does not contain V2/V3 SMT.

It builds 299 exact integer rows (276 determinant slots plus 23 top forms) on 149 coordinates, with `H` specialized to the unique parent cubic plus `243` times three digits:

```text
h = [1, 81 + 243 * values[146], 243 * values[147], 243 * values[148]].
```

Frozen Box02 stdout and `independent_result.json` (SHA-256 `fad73f36b609363f0ee8cde84f9ffd89233913ec9e036b00441ee11de5e8307f`) record

```text
modulus       rank    complete family dimension
3^6 = 729       94    55
3^7 = 2187     123    81
3^8 = 6561     131    99
3^9 = 19683    132   116
3^10= 59049    132   133
```

Rank-nullity on combined columns `(pred_dim + 149)` holds at every stored stage: `149-94=55`, `204-123=81`, `230-131=99`, `248-132=116`, `265-132=133`. Each stage asserts exact integer vanishing of the 299-row residual on the new base and on `base ± direction` and `base ± 2·direction`.

A short local re-execution of the same compiler against the live parent chain reproduced those prints and emitted byte-identical result, ANF, and witness files. That reproduces the ranks as a second run of one implementation. Dual-host confirmation of this compiler is not in the package; Box03/r6d dual custody is of the V3 emitter, not of these ranks.

## Charge 5 — Split `17+116`, fresh `94/55/205`, spectator rank 38, zero residual

**CONFIRMED**

The compiler greedily extracts an `F_3`-basis of the 133 directions modulo three (17 pivots), then replaces each dependent direction `d` by `d-∑λ_j p_j` with `λ_j∈{0,1,2}`, asserting the remainder is `0 mod 3`. Ordering pivots first, the change-of-basis is a permutation times an integer unitriangular matrix, hence lies in `GL(133,Z)`. The `Z`-span is preserved; every old digit tuple has a unique new `(active, spectator)` representative. Over `F_3` the 116 spectators vanish and the 17 actives remain independent. `17+116=133`.

The fresh operator is assembled by probing `base + 3^5 e_j` and dividing the 299-row increment by `3^{10}`, independently of the earlier `/243` matrix. Reported rank 94 on 149 columns forces kernel 55 and, on 299 rows, cokernel 205. Finite-difference extraction of the divided residual along `±1,±2` and mixed active pairs is the exact degree-`≤2` interpolation over `F_3`; spectators have vanishing diagonal quadratic, as asserted. Projection to the fresh left kernel, then quotient by the spectator image of rank 38, leaves `keep=[]`: every constant, linear-in-active, diagonal, and cross coefficient is zero. The reduced ANF is therefore the empty 17-active quadratic, SHA-256 `2a65d00367451476f31941426f086de0fef53bc0b73478e4eb9fa87fb2cf913e`.

That ANF hash collides with the unconstrained quadratic parent’s empty 17-active ANF. The serialization is the same empty `constant/linear/diagonal/cross` object with `C(17,2)=136` index pairs; it is not a second fingerprint of the 299-row ranks. Containment itself was recomputed by the independent compiler, not borrowed from the parent quadratic job.

## Charge 6 — Exponents 95 and 150 from an injective complete parameterization

**CONFIRMED** as displayed `F_3`-digit counts of this one-parent Hensel parameterization. **Rejected** as a scheme-theoretic fibre dimension, as an inverse-limit cardinality, and as a count of SMT `h_i` residues.

The producer left `3^{95}` and `3^{150}` provisional pending audit of parameterization and containment. Containment is Charge 5. Parameterization:

1. **Complete parent cubic.** The displayed parent has top forms `P9 ≡ -y^9 (mod 243)` and `Q12 ≡ y^{12}+81 x y^{11} (mod 243)`. Among all `81^3=531441` monic cubics with `h_i ≡ 0 (mod 3)` modulo 243, the unique solution of `P9=P_(0,9) H^3` and `Q12=Q_(0,12) H^4` is `H=[1,81,0,0]`. (The unit `4` modulo 243 makes `4 h1 ≡ 81` unique, and the remaining coefficients force `h2=h3=0`.) Every common-cubic lift of this parent in the displayed box therefore has that unique 243-level cubic, so the compiler’s three `H` coordinates are the complete monic deformation space, not a slice. The SMT’s looser `h_i ∈ 3Z/177147Z` does not enlarge the locus: any solution must already satisfy the parent-level top forms.
2. **Injective linear digits through `3^{10}`.** Each linear stage’s `rref_solve` returns `F_3`-independent kernel vectors with distinct free `1`s, then writes `new = old_combo + 3^{k-1}·fresh`. That triangular scaling, together with the literal `±1,±2` residual replay, is an injective complete parameterization of the affine kernel of the 299-row linear system over `Z/3^k Z`. Family dimensions `55,81,99,116,133` are those kernel ranks. The `GL(133,Z)` change of Charge 5 is a bijection on that `133`-digit module.
3. **Every active lifts, uniquely modulo spectator/fresh kernels.** Empty `keep` means the obstruction polynomial in the 17 active `F_3`-coordinates, after projection away from `W` and away from the 116 spectators, is the zero polynomial. For each `a∈F_3^{17}` the spectator equation therefore has a solution, and the spectator matrix has constant rank 38, hence a `78`-dimensional affine fibre. The fresh solve then has a `55`-dimensional kernel. Distinct `(a, spectator-kernel, fresh-kernel)` triples give distinct displayed points `F5+243 T+3^{10} W` because `T mod 3` recovers `a` from the 17 independent actives, and the remaining Hensel digits are the triangular spectator/fresh coordinates. Cardinality `3^{17}·3^{78}·3^{55}=3^{150}`. Predecessor projection `3^{95}`.

The compiler constructs only the zero-active particular. The count is the cardinality of this displayed parameterization, not an enumeration of `3^{17}` points and not a statement about the scheme-theoretic fibre over `Spec Z/3^{11}Z`. That is the same typing already licensed for the unconstrained `3^{162}` family. SAT does not depend on the count: the literal point remains.

## Charge 7 — Independent replay of witness `H=[1,119880,40581,0]` and all 299 rows

**CONFIRMED**

Witness payload SHA-256 `a39bc9185a21df92173b356c027a00650ced4b92cfc15d587a91b39c8aca299a`. Coefficients `[1,119880,40581,0]` satisfy `119880=81+243·493`, `40581=243·167`, and `h_i ≡ 0 (mod 3)`. A separate verifier (SHA-256 `eba7d223b88fd61da246fd766a3c5f4f73163e9b0261263d64406779671d6689`) uses its own polynomial arithmetic and a hardcoded copy of the displayed integer B9 parent; it does not import the compiler. AWS Box02 and a local re-run both emit result SHA-256 `2008726f5791b86b3c4f6e5b296cbbf4cdfa91766290c1d32aeec81e4a52c67a`.

An independent Jacobian/convolution replay of the same payload, not by exec of that verifier, checks:

- all 276 ambient determinant slots: `det J(P,Q) ≡ 1` at `(0,0)` and `0` elsewhere modulo 177147 (142 nonzero integer coefficients before reduction, all of which except the constant vanish modulo `3^{11}`);
- all 10+13 top-form rows, residuals identically zero modulo 177147;
- leading units `(P_(0,9), Q_(0,12)) ≡ (2,1) (mod 3)`;
- `P ≡ p5`, `Q ≡ q5` modulo 243 for the displayed parent
  `u=x+y^3`, `p5=u-u^3+18uy+81(2uy+x y^2)`, `q5=y+u^4+3 u^2 y+72 y^2+81(y^2+x^4 y^2+x y^{11})`;
- exact total degrees `(9,12)`, no coefficient outside the box.

Those 276+23 rows are the 299-row residual. Leading units are in any case forced throughout the `243 T + 3^{10} W` box: `P_(0,9)≡-1 (mod 243)` already. Frozen AWS verifier RSS 14592 KiB, 0.03 s.

## Charge 8 — One-parent finite-depth refusal; congruence versus characteristic-zero Q8

**CONFIRMED**

The producer, preregistration, README, independent result, and V3 `refusal_scope` all restrict the claim to one fixed B9 mod-243 parent and its complete displayed common-core congruence family at modulus `3^{11}`. The following are explicitly out of scope, and this review does not license them:

- any lift past `3^{11}`, inverse-limit/`Z_3` point, or all-depth chain;
- characteristic-zero (or finite-extension-of-`Q_3`) Keller pair;
- a source-honest landing in the selected corrected-Q8 chart;
- complete coverage of earlier mod-243 parents;
- a maximum-twelve theorem, counterexample, or JC2.

The licensed object is an **integral congruence incidence**: coefficientwise identities `P9=P_(0,9) H^3` and `Q12=Q_(0,12) H^4` modulo `177147` inside a finite coefficient box. A characteristic-zero Q8 landing is a strictly stronger object: an exact pair in `O[x,y]` with `det J=1` identically, reducing to B9, whose degree-22 face forces leading-form proportionality over a field of characteristic zero and whose selected Q8 source is an order-three `p=1` divided-row chart that refuses an order-one common-core specialization (reviewed interface SHA `1cb8f1c1…`). In characteristic 3 the prefactor `12` of `J(P12,Q12)` vanishes, so a mod-`3^{11}` common-cubic point does not supply that proportionality and does not enter that chart. The two must not be identified.

---

## Independently recomputed hashes

| Object | SHA-256 |
|---|---|
| producer report | `b3a86bbd55ed99ca60dfc3eeb89560dbc483265db603de0bec4a26e63d673a2b` |
| this review’s prompt | `23cf53326211a076de688dacb50f6aa75a45bc729d5517913f62b0dde5f2d5be` |
| V2 erratum (xmodel) | `cb07f729ca3a8cf32b07d7c8e4ed2cc9cf178750f21a06bb38342eb4dea4722c` |
| V2 emitter | `ab85df4824042f9919e535ad9b2d9c4213deb1aa2ed953ae6fa6aed4c66a7556` |
| V2 SMT | `182bc9f7302ba852b32d04899e6b7a86b38d0eaf0cb2faaa280717d4b9c70604` |
| V2 DIMACS | `69ee12c3118a428a28f674ec24e362b721e0611c800f65afbcb8a48e778c1394` |
| V3 wrapper | `c2583024a8324033e25df9d8b4b2c2c4455f0c761838f70356b52bb1fd9f9bfe` |
| V3 patched source | `7dfe73ea02f68434b1a548c51b69353a50e4d593f2d3e404e64c13790f49a98c` |
| V3 / independent canonical SMT | `5af9efbe4b138f1cb0408099c90283842b4ef0b0fef9d7d33447d51a29d53563` |
| V3 Boolector SMT | `2eb69355a0b85b6928899a619840ecb7856ee6e6cc2ef050ab76067e44c835f7` |
| V3 emit result | `45a79eedbfcec2cd24b60f0fc5a5b3a91b25c2c6fdcd6f4f17afa433c2bcd4fe` |
| independent compiler | `460199584e128bc2c5f3196871a34437ebdfd7d674ccf0bcc2f52b9db8ace6b8` |
| independent result | `fad73f36b609363f0ee8cde84f9ffd89233913ec9e036b00441ee11de5e8307f` |
| independent / parent empty ANF | `2a65d00367451476f31941426f086de0fef53bc0b73478e4eb9fa87fb2cf913e` |
| witness payload | `a39bc9185a21df92173b356c027a00650ced4b92cfc15d587a91b39c8aca299a` |
| witness verifier source | `eba7d223b88fd61da246fd766a3c5f4f73163e9b0261263d64406779671d6689` |
| witness verifier result | `2008726f5791b86b3c4f6e5b296cbbf4cdfa91766290c1d32aeec81e4a52c67a` |
| linear-window parent | `fb4f16d808dfba754582fb1b5fe10dfa0e69bca0888b38f92586e1f5534724e2` |
| quadratic parent compiler | `7a51c772b0df8c900eddd84e4388fe5f3d47e2bb755ef837d17d7cc28debde58` |
| B9 W5 replay | `f1b50bb2c3e21369da205ebcf1ba028eede20c89d5ad863253fdfec4d6d28c5d` |
| `MANIFEST.sha256` (165 lines, all match) | `53663a8ea95b4993ad28478b11f143714fa5b698fb5f5592fe4fd67641b13107` |
| `FREEZE.sha256` (8 lines, all match) | `86e01887732321d5f0c9306d3e5de0bb0e8e80470e0c01e116743f5cf6f01405` |
| V3 `SOURCE_CLOSURE.sha256` (67 lines, Box03=r6d) | `54230928e3fa82f0e9919c4791e223729a37a5340e555a6e3df0a7e74e3cbe13` |

## Software / custody notes (non-blocking)

- Box03 and r6d are two hosts running one V3 wrapper. The independent `modulus_bv` emitter is the second implementation of the formula, not a second 149-coordinate reconstruction.
- The independent compiler has one AWS host (Box02, 4.96 s, 28920 KiB RSS, 2026-08-25T17:31:16Z–17:31:21Z). Local re-execution matched those bytes; it is not a second algorithm and is not dual-AWS custody.
- V3 Boolector/Z3 on Box02 were killed after five minutes (`STOP_REASON.txt`: `stopped-after-independent-source-replayed-SAT`), with Boolector RSS about 17 GiB and Z3 about 72 GiB, stdout `unknown` / empty. They are not SAT evidence.
- The empty-ANF hash `2a65d003…` is shared with the unconstrained quadratic parent. Expected for two empty 17-active quadratics; do not treat it as an independent rank certificate.
- The xmodel V2 erratum’s “407 remainder gates” is a wrong SMT-level count. Quarantine of V2 remains correct.
