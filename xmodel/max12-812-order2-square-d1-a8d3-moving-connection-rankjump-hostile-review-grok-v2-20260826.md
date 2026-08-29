# Hostile review V2 — D1 a=8,d=3 moving-connection rank jump

| Field | Value |
|---|---|
| Target | isolated `k6RC` diagnostic plus moving-connection rank jump on `D(p)` |
| Isolated result | `cases/max12_812_order2_square_owner_d1_a8d3_k6rc_isolated_bridge_20260826/RESULT.md` |
| Rank-jump result | `cases/max12_812_order2_square_owner_d1_a8d3_connection_rankjump_20260826/RESULT.md` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest hash defect | none |
| Smallest firewall defect | none |
| Reviewer / model | Grok 4.6 (xAI). Independent replacement after the first Claude launch exhausted that provider's API usage limit and wrote no report. Producer `PASS` tokens, validator strings, and RESULT status lines are not authority |
| Method | SHA-256 of every charged pin, nested AWS result, stdout, stderr, and validator; independent binomial/IFT derivation of the moving inverse-root mixed tail; independent extraction of family-15 `k6A^2` from the frozen inventory; elementary two-row linear algebra over `Q`; exact reduction of the isolated literals modulo `65519` and `65521`. No Singular re-execution, Sage, msolve, Lean, or AWS replay |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

The first Claude/Fable delivery wrote no report and has no mathematical verdict; it is unused. Independently recomputed SHA-256 of every charged primary pin matches the review charge. Nested freeze and evidence manifests rehash in full. No file other than this review was written. No producer, ledger, prompt, source, or other file was edited. No computation was launched.

This confirms only that a normalized coefficientwise universal odd functional cannot annihilate both the frozen family-15 `k6A^2` column and the moving-inverse-root `k6RC` column on `D(p)`. It is not an a=8,d=3 cell verdict.

---

## Verdict

**CONFIRMED.**

Starting from `f0=L^4`, `delta_R f=2L^2 R`, `delta_C f=C`, and exponent `3/4`, the mixed negative tail at fixed inverse root is `q_RC=-(3/8) R C/L^3`. At fixed Faber coordinate `w` the inverse root moves by `z_R=-R/(4z L)`. The correction identity

```text
q_RC + (partial_z q_C) z_R = -(3/16) R C'/(z L^2)
```

is exact, including sign and factor. The two `RC/L^3` summands cancel. Translating `C'=c1`, `R=b1 z+b0`, `L=w^2`, and `z=w(1-(p/2)w^{-2})^{1/2}` through row 7 recovers exactly the isolated canonical literals

```text
e4[k60*c1*b1] = -3/16,
e5[k60*c1*b0] = -3/16,
e7[k60*c1*b0] = -3p/64,
```

with every charged `c0` coefficient and `e6[k60*c1*b1]` equal to zero. Those literals are the Q stdout of the isolated diagnostic; both prime controls are their exact reductions. The preregistered fixed-`z` Laurent prediction is the object that fails. The frozen canonical tails are vindicated.

Family 15 of the frozen complete source inventory is `k6`, `A=2`, `C=0`, `R=0`, pole 3, coefficient `-3/32`, grade 38. Its independent source monomial `k60*a0*a1` has odd rows `(Phi5,Phi7)=(-3/16,+3p/64)`. There is no first-order `k6 A` negative family, so `q_A` has no negative part at this order and the inverse-root motion does not correct `k6A^2`. Faber conversion of the inventory's analytic family-15 monomials reproduces the literal rows, including the `p`-fill.

The corrected `k6RC` column is `(-3/16,-3p/64)`. The two forced `alpha` values are `+1/4` and `-1/4`. Their two-row determinant is `9p/512`, a unit on `D(p)`. The same span contains the terminal direction

```text
e7 = (32/(3p))*col(k6A^2) - (32/(3p))*col(k6RC).
```

No functional `Phi7 + alpha*p*Phi5 + beta*p^2*Phi3 + gamma*p^3*Phi1` can annihilate both columns. The uncorrected family-16 inventory column would have forced the same `alpha=+1/4` as family 15 and would have hidden the jump; that column is the falsified fixed-`z` model and is not used.

The conclusion is route falsification only. It does not decide the a=8,d=3 cell, construct a nonlinear solution or point, or produce an existence or counterexample certificate. The legitimate successor is saturation or chamber splitting by the two source products `k60*a0*a1` and `k60*b0*c1` in the complete earlier zero locus, then a terminal `J` test on each branch.

No conclusion depends on a Singular `qring`. The isolated diagnostic is an ordinary polynomial ring with explicit `reduce` before `==0`. The rank-jump client is Python `Fraction` arithmetic.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 1. Rehash freeze, evidence, nested AWS, rc, swap, archive | exact Q and two distinct primes | **holds**; 6/6 charged pins; isolated 3+21+8; rank-jump 18+7+3; all six lanes `engine_rc=0`, `Swaps: 0`, distinct archives |
| 2. Moving inverse-root identity and rows 4,5,7 | exactness of `-(3/16) R C'/(z L^2)` | **holds**; vindicating canonical literals; falsifying only the fixed-`z` bridge |
| 3. Family-15 `k6A^2` and no A-correction | inventory extraction; `q_A` has no negative part; rows 5,7 `(-3/16,+3p/64)` | **holds** |
| 4. Corrected `k6RC`, forced alpha, det, `e7` span | `(-3/16,-3p/64)`, `+1/4,-1/4`, `9p/512`, stated `e7` | **holds** |
| 5. Firewall | only failure of a normalized coefficientwise universal odd functional on `D(p)` | **holds**; successor is saturation/chamber splitting on the two source products |
| 6. Singular qring noncanonical assignment | any `==0`, `subst`, or `diff` on a qring without explicit reduction | **does not occur** |

---

## 1. Custody

Independently recomputed SHA-256 of the six charged primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| isolated `RESULT.md` | `64f731aa4a518b467d2b60489643178c2e6f0c069b7f9c0a568ae685f9378ba2` | moving-root adjudication |
| isolated `DIAGNOSTIC_FREEZE.sha256` | `84262c311e3a7944ba945df630bfb254a0d838a9c0065098295835cb64db80ab` | isolated freeze root |
| rank-jump `RESULT.md` | `2c422f36cecec94e870c1bab4767d3dc61b689f100fc583ad3509a2a176f90bc` | rank-jump certificate |
| rank-jump `EVIDENCE.sha256` | `0b63361de1f29c16eba1ce28e22c81a4febc7560ed4f97395c985f45622dca3d` | rank-jump evidence manifest |
| rank-jump `PRODUCER_FREEZE.sha256` | `a28e20033d4e0d5cd8fd3303a371d802147db65875cace445904a48f9f4fc83e` | rank-jump freeze root |
| `source_inventory.json` | `de195a2a005c32a53c3802dc1ee5f8429bb94a7337543d4f1419be5ad4c14cf6` | complete frozen source inventory |

The V2 review prompt rehashes to `397857135a10a397ac0e4f72a8238eff38fdff7808b0ee9cf8b564170d65acec`. The unused Claude prompt rehashes to `1d181e6464ed4fb916dcd1cfb0bcbf6dbb5d89aa8995dd1350b6d57b8fee3d0f` and is not mathematical evidence.

Manifest row counts, all matching:

| Manifest | Rows |
|---|---|
| isolated `DIAGNOSTIC_FREEZE.sha256` | 3/3 |
| isolated `EVIDENCE.sha256` | 21/21 |
| isolated `FREEZE.sha256` | 8/8 |
| rank-jump `EVIDENCE.sha256` | 18/18 |
| rank-jump `FREEZE.sha256` | 7/7 |
| rank-jump `PRODUCER_FREEZE.sha256` | 3/3 |

`PRODUCER_FREEZE.sha256` pins the rank-jump `EVIDENCE.sha256`, `RESULT.md`, and `FREEZE.sha256`. `DIAGNOSTIC_FREEZE.sha256` pins isolated `EVIDENCE.sha256`, `RESULT.md`, and `FREEZE.sha256`. Nested `compiled.sha256` on every AWS lane matches the compiled `result.json` and, where present, the compiled `.sing`.

### Isolated diagnostic, archive `520e2dde5dd1d7d5b67be4296fce536d3297705bd6059a3eb4d444cdea04f06e`

All three V2 lanes used that archive, returned `engine_rc=0`, validator `PASS_A8D3_K6RC_ISOLATED_DIAGNOSTIC`, and `Swaps: 0`. Compiler stderr is empty. Characteristics are `0`, `65519`, and `65521` on three hosts.

| field | host | tag | stdout SHA-256 |
|---|---|---|---|
| Q | Box02 | `max12_812_order2_square_d1_a8d3_k6rc_isolated_v2_q_box02_20260826T205500Z` | `9b496cb7ab68530fdb2355832278e224f629c3ad359ae25ced037c685df536a1` |
| F65519 | Box03 | `max12_812_order2_square_d1_a8d3_k6rc_isolated_v2_p65519_box03_20260826T205500Z` | `1247bc3a4e74f327d5c0aeb0afcb105e0146c93203a4e77b894475ea3677ae3c` |
| F65521 | r6d | `max12_812_order2_square_d1_a8d3_k6rc_isolated_v2_p65521_r6d_20260826T205500Z` | `8aecf0af84f76da049c3572beeb97191f8a098c2f307edaf22da3d8958d3c15f` |

Q literals (the mathematical record):

```text
K6RC_LIT_R4_C1B1=-3/16*eta
K6RC_LIT_R5_C1B0=-3/16*eta
K6RC_LIT_R5_C0B1=0
K6RC_LIT_R6_C0B0=0
K6RC_LIT_R6_C1B1=0
K6RC_LIT_R7_C1B0=-3/64*p*eta
K6RC_LIT_R7_C0B1=0
K6RC_ALL_LITERAL_ROWS_MATCH_LAURENT=0
```

The validator is a recording gate: it requires unique `LIT/PRED/DIFF/MATCH` lines and the endpoint `RECORDED_NO_CELL_VERDICT`. It does not require `MATCH=1`. That is the correct diagnostic contract. The preregistered fixed-`z` prediction is the side that fails (`PRED` is twice the odd leading literals, inserts `c0` terms, and has the wrong row-7 sign).

Finite-field literals are the exact reductions of the Q values, including Singular's signed representatives:

| coefficient | Q | F65519 signed | F65521 signed |
|---|---|---|---|
| `-3/16` | `-3/16` | `-12285` | `12285` |
| `-3/64` | `-3/64` | `-19451` | `-13309` |
| `-3/8` (fixed-`z` pred) | `-3/8` | `-24570` | `24570` |
| `3/32` (fixed-`z` pred row 7) | `3/32` | `-26617` | `26618` |

The V1 archive is retained only as failed syntax evidence (`poly^number`); it is not a verdict and is not used below.

### Rank jump, archive `640b2d2aba9c58b2208added780f6146dae6271970670ce83e955aea2da658b1`

All three lanes used that distinct archive, returned `engine_rc=0`, validator `PASS_A8D3_CONNECTION_RANKJUMP`, and `Swaps: 0`. The two primes are distinct from each other and from characteristic zero.

| field | host | tag | stdout SHA-256 |
|---|---|---|---|
| Q | Box02 | `max12_812_order2_square_d1_a8d3_connection_rankjump_q_box02_20260826T2115Z` | `bf1966e2ce4308e7b997e525773d578a7106cf5eff8f52a894edcf27a98314e1` |
| F65519 | Box03 | `max12_812_order2_square_d1_a8d3_connection_rankjump_p65519_box03_20260826T2115Z` | `bd266ce03b325a531c57aeca93104c1052fa165eabe4c8b345417cc9405d5983` |
| F65521 | r6d | `max12_812_order2_square_d1_a8d3_connection_rankjump_p65521_r6d_20260826T2115Z` | `8d051356c66e7d87d49833ecaafb5d61f22e38418f69e7826bccb84819e8ead2` |

The rank-jump client is AWS-pinned Python. It reads family 15 from the frozen Q inventory and uses the independently adjudicated `k6RC` column; it does not consume uncorrected family-16 inventory coefficients. On the two primes it only checks that `9/512` remains a unit (`15484` in `F_65519`, `13181` in `F_65521`). That is a software control, not a second derivation. The isolated Singular reductions already supply the characteristic-`p` identity of the corrected `k6RC` literals.

A passing validator is not a theorem. The identities below are re-derived.

---

## 2. Moving inverse-root correction

Work at the background `f0=L^4` with `L=z^2+p/2`, perturbations `delta_R f=2L^2 R` and `delta_C f=C`, and exponent `alpha=3/4`. The negative Laurent piece is the negative part of `q=f^{3/4}-F_6`.

### Fixed `z`

```text
partial_C (f^{3/4}) = (3/4) f^{-1/4} C,
```

hence at the background `q_C=(3/4) C/L`. The mixed derivative is

```text
partial_R partial_C (f^{3/4})
  = (3/4)(-1/4) C f^{-5/4} (2 L^2 R)
  = -(3/16) C L^{-5} (2 L^2 R)
  = -(3/8) R C / L^3.
```

So `q_RC=-(3/8) R C/L^3` at fixed `z`. This is the preregistered Laurent, equivalently `binom(3/4,2)*2!*2=-3/8` times `eta k60 (b1+b0 t)(c1+c0 t) t^5 (1+(p/2)t^2)^{-3}`.

### Motion of the inverse root

Hold the Faber coordinate `w` fixed. Implicit function theorem on `f(z,R)` gives

```text
z_R = -(delta_R f) / (partial_z f0).
```

Now `partial_z f0=4 L^3 * 2z=8 z L^3`, so

```text
z_R = -(2 L^2 R)/(8 z L^3) = -R/(4 z L).
```

Differentiate `q_C=(3/4) C/L` in `z`, with `C'=partial_z C` and `partial_z L=2z`:

```text
partial_z q_C = (3/4) (C' L - 2z C) / L^2.
```

The moving mixed tail is

```text
(partial_z q_C) z_R
  = (3/4)(C' L - 2z C)/L^2 * (-R/(4 z L))
  = -(3/16) R C'/(z L^2) + (3/8) R C / L^3.
```

Adding the fixed-`z` mixed term cancels the two `RC/L^3` contributions:

```text
q_RC + (partial_z q_C) z_R = -(3/16) R C'/(z L^2).
```

The identity is exact: sign `-`, factor `3/16`, denominator `z L^2`, and `C'` not `C`.

### Translation to rows 4, 5, 7

In this cell `C'=c1` and `R=b1 z+b0`. With `L=w^2` and `z=w(1-(p/2)w^{-2})^{1/2}`,

```text
-(3/16) R C'/(z L^2)
  = -(3/16) c1 b1 w^{-4}
    -(3/16) c1 b0 w^{-5} (1-(p/2)w^{-2})^{-1/2}.
```

The binomial `(1-x)^{-1/2}=1+(1/2)x+O(x^2)` with `x=(p/2)w^{-2}` gives `1+(p/4)w^{-2}+O(w^{-4})`, hence through row 7

```text
-(3/16) c1 b0 w^{-5} - (3/16)(p/4) c1 b0 w^{-7} + O(w^{-9})
  = -(3/16) c1 b0 w^{-5} - (3p/64) c1 b0 w^{-7} + O(w^{-9}).
```

Therefore the only nonzero mixed coefficients through row 7 are

```text
e4[k60*c1*b1] = -3/16,
e5[k60*c1*b0] = -3/16,
e7[k60*c1*b0] = -3p/64.
```

Every charged `c0` coefficient vanishes because `C'=c1`. The even row `e6[k60*c1*b1]` vanishes because the `b1` term is purely `w^{-4}`. These are exactly the isolated Q literals, including the overall `eta` from `R=sigma^8 eta (b1+b0 t)`.

The same expansion falsifies only the fixed-`z` bridge: that prediction keeps the uncancelled `-(3/8) R C/L^3`, so it doubles the leading odd/even mixed coefficients, inserts `c0` terms, and produces row-7 coefficient `+3p/32` instead of `-3p/64`. The isolated `PRED_*` lines are that wrong model. The canonical literal tails, compiled from the frozen `tails.json` pin `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848`, are the correct side.

---

## 3. Family-15 `k6A^2`

The frozen inventory

```text
cases/max12_812_order2_square_owner_d1_d23_a8a9_j38_r3_tail_20260826/aws_v2_failed_a8d3_q_box02_highmem/evidence/compiled/source_inventory.json
```

is the complete a=8,d=3 grade-38 source census (`status=COMPLETE-D1-A8D3-THROUGH-GRADE38`, 17 primitive families, 17731 literal Faber monomials). Family 15 is

```text
{'A': 2, 'C': 0, 'R': 0, 'base_grade': 38, 'coefficient': '-3/32',
 'fixed_sigma': 22, 'load': 'k6', 'name': 'k6', 'pole': 3}.
```

Grade-38 literal Faber monomials of family 15, extracted independently:

| row | variables | coefficient |
|---|---|---|
| 4 | `a1,a1,k60` | `-3/32` |
| 5 | `a0,a1,k60` | `-3/16` |
| 6 | `a0,a0,k60` | `-3/32` |
| 6 | `a1,a1,k60,p` | `3/64` |
| 7 | `a0,a1,k60,p` | `3/64` |

The independent source monomial `k60*a0*a1` therefore has odd rows

```text
(Phi5, Phi7) = (-3/16, +3p/64).
```

There is no family-15 support in rows 1 or 3 at grade 38.

### Why there is no inverse-root correction for `k6A^2`

`A` enters `L`, not `f` additively. At `R=C=0` one has `f=L_A^4` with `L_A=L+A`, so

```text
f^{3/4} = L_A^3 = L^3 + 3 L^2 A + 3 L A^2 + A^3,
```

which is polynomial. The first variation is `q_A=3 L^2 A` with no negative Laurent part. Equivalently, the primitive-family list contains `k6 C` at pole 1 (family 0, coefficient `3/4`) and no `k6 A` at pole 1; the first `k6`-loaded pure-`A` family is this pole-3 `A^2` term.

Because the negative part of `q_A` is already zero, the moving-root correction `(partial_z q_A) z_A` does not contribute to the negative tail at this order. (The shift `z_A` is itself regular: `delta_A f=4 L^3 A` and `z_A=-(4 L^3 A)/(8 z L^3)`, a polynomial in `A`.) The `A^2` negative family is therefore already given by the fixed-`z` second variation together with the ordinary Faber conversion.

That last claim is checkable on the inventory itself. Analytic family-15 monomials at grade 38 begin

```text
t^5 a1^2 k60 : -3/32,
t^6 a0 a1 k60 : -3/16,
t^7 a0^2 k60 : -3/32,
t^7 a1^2 k60 p : 9/64,
t^8 a0 a1 k60 p : 9/32.
```

The isolated diagnostic's conversion (`h_k=[t^{k+1}]H`, then the Chebyshev/Faber fill `Pred5=h5`, `Pred7=(5/4)p h5+h7` on this support) sends the `a0 a1` column to

```text
Pred5 = h5 = -3/16,
Pred7 = (5/4)p(-3/16) + (9/32)p = -15p/64 + 18p/64 = 3p/64,
```

which is exactly the literal row pair. The `p`-fill is ordinary Faber arithmetic, not inverse-root motion. By contrast, the same conversion of analytic family 16 reproduces the isolated `PRED_*` lines and not the literals — that is the RC bridge failure already derived in section 2.

Using uncorrected family-16 inventory coefficients would be a defect: they force `alpha=-(3/32)/(-3/8)=+1/4`, the same value as family 15, and would falsely report no jump. The rank-jump client does not do that.

---

## 4. Rank jump on `D(p)`

Write the two-row columns as

```text
col(k6A^2) = (-3/16, +3p/64),
col(k6RC)  = (-3/16, -3p/64).
```

The second column is the moving-root result of section 2, matching the isolated Q literals for `k60*c1*b0` (the independent source monomial `k60*b0*c1`).

A normalized odd functional

```text
Phi7 + alpha*p*Phi5 + beta*p^2*Phi3 + gamma*p^3*Phi1
```

restricted to a column `(c5,c7)` with vanishing rows 1 and 3 forces `c7 + alpha p c5=0`, hence `alpha=-c7/(p c5)`:

```text
alpha(k6A^2) = -(3p/64) / (p*(-3/16)) = +1/4,
alpha(k6RC)  = -(-3p/64) / (p*(-3/16)) = -1/4.
```

These cannot be imposed simultaneously. The two-row determinant is

```text
det = (-3/16)(-3p/64) - (-3/16)(3p/64) = 9p/1024 + 9p/1024 = 9p/512.
```

On `D(p)` the element `p` is a unit, and `9/512` is a unit in characteristic zero, so `9p/512` is a unit. In the two prime controls `9/512` remains nonzero, so the matrix stays rank two after reduction.

The same two columns span the row-7 target direction. Directly

```text
(32/(3p))*col(k6A^2) - (32/(3p))*col(k6RC)
```

has row 5

```text
(32/(3p))*(-3/16) - (32/(3p))*(-3/16) = 0
```

and row 7

```text
(32/(3p))*(3p/64) - (32/(3p))*(-3p/64) = (32/(3p))*(3p/64)*2 = 1.
```

Thus `e7=(32/(3p))*col(k6A^2)-(32/(3p))*col(k6RC)` in the two-row coefficient space. A coefficientwise terminal-target separator is impossible without extra nonlinear source equations or a chamber split.

Incompatibility of the two `alpha` values already kills every choice of `beta,gamma`. Rows 1 and 3 of both charged monomials are empty at grade 38, so those coefficients are not an escape.

---

## 5. Firewall and successor

The argument is linear algebra on two frozen source columns in odd rows 5 and 7, after replacing the falsified fixed-`z` `k6RC` model by the moving-root literals. It proves only that no normalized coefficientwise universal odd functional on `D(p)` annihilates both columns.

It does not prove:

- emptiness or nonemptiness of the a=8,d=3 cell;
- that either monomial `k60*a0*a1` or `k60*b0*c1` can take an arbitrary value on the complete earlier zero locus;
- a nonlinear solution, a point, a component, or an existence/counterexample certificate;
- a statement about a=7, a=9, another D1 chamber, maximum twelve, or JC2.

Both RESULT files state this firewall. The isolated diagnostic further states that it does not alter the frozen literal-tail compiler.

The legitimate successor is chamberwise: adjoin the complete earlier equations, split (or saturate) on the two source products in that earlier zero locus, and test the terminal `J` target on each branch. Until that is done, a=8,d=3 remains a no-verdict cell whose one-functional order-three route is closed.

---

## 6. Singular qring noncanonical-assignment hazard

Singular 4.3.2 `qring` objects need not be canonically reduced under assignment, `==0`, `subst`, or `diff` unless the polynomial is explicitly reduced by the quotient standard basis. That hazard is relevant only if a conclusion here consumes such an operation.

It does not.

The isolated diagnostic compiles an ordinary ring

```text
ring R=<char>,(sigma,p,eta,c1,c0,b1,b0,k60,t),dp;
```

There is no `qring` declaration in that case directory, in either compiled `.sing`, or in the rank-jump directory. Truncation uses `ideal S38=std(ideal(sigma^38))` and `S39=std(ideal(sigma^39))` with explicit `reduce` before every `==0` on the literal side (`int lit_*_div=(reduce(lit_*_raw,S38)==0)`). Taylor coefficients of the (falsified) predictor use `diff` and `subst` in the same ordinary ring; those operations are canonical there. The binomial check `((3/4)*((3/4)-1)/2*4==-3/8)` is a number comparison and holds in all three characteristics.

The rank-jump client is Python `Fraction` arithmetic against the frozen JSON inventory. It never calls Singular.

Unrelated campaign qring audits are not imported.

---

## Scope reminder

This review confirms a navigation/route negative: the one-functional a=8,d=3 order-three route is closed on `D(p)` after the moving-root correction of `k6RC`. The a=8,d=3 cell is not decided.

CONFIRMED
