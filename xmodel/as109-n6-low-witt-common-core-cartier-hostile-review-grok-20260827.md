# Hostile different-model review — AS109 residual `n=6` low-Witt/common-core Cartier gate

| Field | Value |
|---|---|
| Claim under review | Frozen producer: for an exact integral AS109 lift `P=x-x^{109}+109A`, `Q=y+109B` on the residual corner `deg_y Q=6`, `deg_y P=m>=12`, `d=gcd(m,6) in {3,6}`, with primitive common core `p_m=alpha h^{m/d}`, `q_6=beta h^{6/d}`, the valuation-one branch `v_{109}(beta)=1` forces `(bar h)^b` into `im(d/dx : F_{109}[x] -> F_{109}[x])` via the first-Witt `y^5` row `a_5'+6 b_6=0`; hence `Hbar != 108 (mod 109)` for `d=6` and `Hbar != 54 (mod 109)` for `d=3`. An extra `v_{109}(alpha)=1` and `gcd(m/d,109)=1` subbranch makes the condition automatic. No lift existence or nonexistence is inferred |
| Overall verdict | **CONFIRMED** |
| Packed determinant identity | **CONFIRMED** |
| First-Witt rows, including `a_5'+6b_6=0` | **CONFIRMED** |
| Univariate Cartier image/cokernel | **CONFIRMED** |
| Primitive-core to `(bar h)^b` Cartier, including degree drop | **CONFIRMED** |
| Leading exclusions `Hbar != 108` / `Hbar != 54` | **CONFIRMED** |
| Extra `p_m` UFD/Frobenius positive control | **CONFIRMED** |
| Controls | **CONFIRMED** |
| Novelty (new coupling, old ingredients; not a tautology of the stopped top two bands) | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking precisions below: `q_6=109 b_6` mixes the integral coefficient of `B` with its reduction; “109th power up to scalar / after absorbing a scalar” is redundant over `F_{109}` by Fermat; `(0.1)` is vacuous whenever `deg((bar h)^b)<108`; the registered replay does not exhibit a non-leading Cartier obstruction; the producer’s own `d=3` Wronskian sample is Cartier-obstructed, which illustrates independence rather than a hole) |
| Evidence tier | independent expansion of `det J-1` over `Z[x,y]`; coefficientwise first-Witt rows; univariate Cartier image as `{c_{109k-1}=0}`; Gauss content for primitive `h`; reduction-versus-powering; degree-drop examples; UFD/`gcd(a,109)=1` argument in `F_{109}[x]`; unmodified rerun of the frozen replay as regression only. Producer `PASS-LOW-WITT-CARTIER` strings were not used as evidence |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (Sol / OpenAI) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Review window (UTC) | 2026-08-27T11:47Z |
| Python | 3.14.6; stdlib only (integer/finite-field sparse dicts) |
| Host | hand algebra plus one unmodified frozen replay and one independent sparse-arithmetic engine that does not import the producer script |

Producer, freeze, and every named history artifact reread in full before any verdict. No producer, freeze, case, canonical, or ledger file was edited. This file is the only write. `jc2-lean` was not entered, read, built, status-inspected, or modified. No AWS call, no Singular process, no web.

Charged producer and freeze:

- `xmodel/as109-n6-low-witt-common-core-cartier-producer-sol-20260827.md` (SHA-256 `c79dfbf550962c1fcbae974b6fe1ab1867489ceb8a93906ad4b7739a49522526`, matches the launch prompt)
- `cases/as109_n6_low_witt_cartier_v1_20260827/FREEZE.sha256` (SHA-256 `fcb578ae1940e19d0b7b76e39db33754ac1471e61f462e3e19388d572ae6900a`)
- `cases/as109_n6_low_witt_cartier_v1_20260827/PREREGISTRATION.md` (SHA-256 `5f3dd79b6050d2a66429866ad95a3068fbc1116ed6bdd26aad61fd5a7e784bea`)
- `cases/as109_n6_low_witt_cartier_v1_20260827/verify_low_witt_cartier.py` (SHA-256 `65097ad0aa07447b442a07ce4ca865f834978c87136b1b78d1d068acf75bc5a8`)
- `cases/as109_n6_low_witt_cartier_v1_20260827/EXPECTED_RESULT.json` (SHA-256 `e0fbc93fa41feaa377d1e75a2457bf7539a68ce625db3f266f40fa5c58477907`)

Named load-bearing history, hashes recomputed on the charged tree:

- `xmodel/as109-one-sided-prime4-composition-sol-20260827.md` (SHA-256 `3d6d09fd1c9d1548dc6af78221f74c83276eb89378ee06cecac5fd19b46fcb36`)
- `xmodel/as109-n6-top-two-y-bands-face-isolation-grok-20260827.md` (SHA-256 `7640715607c640beae845855feb261a0d207ea9409a1ccf8a915899f4461ec10`)
- `xmodel/as109-n6-top-two-y-bands-face-isolation-hostile-review-sol-20260827.md` (SHA-256 `571c5e2bda00cf9221debcd43b26f635016a68622714bbf8bbb0e2a68f33525f`)
- `xmodel/as109-support-gate-20260824.md` (SHA-256 `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5`)
- `xmodel/as109-support-gate-20260824-erratum.md` (SHA-256 `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb`)

Novelty comparison only (not charged as theorem inputs; already reviewed elsewhere): wild-symplectic first-digit Cartier floor `[x^{108} y]Q_1=1`; polar-conductor unbounded algebraization conductor; prior bivariate Cartier cokernels in the `p=3` F-only/gauge-growth lanes.

Write `R=Z_{109}`, `K=Q_{109}`, `p=109`, and `J(P,Q)=P_x Q_y-P_y Q_x`. Reduction of a polynomial over `R` is written with a bar. Actual partial `y`-degrees in the displayed AS109 chart.

---

## Promotion

**Accept `PASS-LOW-WITT-CARTIER` at the stated valuation-one `q_6` content-branch scope, as a necessary condition, not as emptiness of residual `n=6`.**

Let

```text
P = x - x^{109} + 109 A,     Q = y + 109 B
```

belong to `R[x,y]` with `det J(P,Q)=1`, and suppose this is an exact integral polynomial lift of `(x-x^{109},y)` on the residual corner

```text
deg_y Q = 6,     deg_y P = m >= 12,     d = gcd(m,6) in {3,6},
p_m = alpha h^{m/d},     q_6 = beta h^{6/d},
```

with `h` primitive in `R[x]` and `b=6/d in {1,2}`. If `v_{109}(beta)=1`, then

```text
(bar h)^b  in  im(d/dx : F_{109}[x] -> F_{109}[x]),
```

equivalently every coefficient of `(bar h)^b` at exponent `109k-1` (`k>=1`) vanishes. Writing `Hbar=deg(bar h)` (degree after reduction, possibly strictly less than `deg(h)`), the leading term of `(bar h)^b` is nonzero of degree `b Hbar`, hence

```text
b Hbar != 108  (mod 109).
```

In particular `d=6` excludes `Hbar = 108 (mod 109)` and `d=3` excludes `Hbar = 54 (mod 109)`.

If in addition `v_{109}(alpha)=1` and `gcd(m/d,109)=1`, then `bar h in F_{109}[x^{109}]` and `(0.1)` is automatic. The new equations are therefore a discriminator on the complementary slice `v_{109}(beta)=1` with either `v_{109}(alpha)>=2` or `109 | (m/d)`, and only once `deg((bar h)^b) >= 108`. They are not a hidden universal contradiction and they do not see `v_{109}(beta)>=2`.

**Eligible for `AUDIT.md` promotion** at exactly this branch-local necessary condition and the extra positive-control subbranch. This review does not edit `AUDIT.md`.

**Do not promote this to:** existence of an AS109 lift; nonexistence of an AS109 lift; emptiness of residual `n=6`; a floor seven; a statement about `v_{109}(beta)>=2`; identification of `Hbar` with the characteristic-zero degree of `h`; a W2/W3, support-cap, or degree-rectangle computation; a closed-support contraction; a characteristic-zero counterexample; or a JC2 decision.

---

## Quarantine

No result here proves or disproves JC2, constructs a lift, or empties the residual corner. Producer strings `PASS-LOW-WITT-CARTIER`, `packed_determinant_identity true`, and the two obstruction JSON objects were not used as evidence. The packed identity, the first-Witt rows, the Cartier image, the Gauss/reduction passage, the leading exclusions, and the UFD positive control were re-derived. The frozen replay is a regression/control suite; the general proof is the coefficientwise argument below.

---

## Scope (not enlarged)

One prime `p=109`, coefficient ring `R`, exact `det J=1`, displayed AS109 coordinates, residual actual degrees `(m,6)` with `d in {3,6}`, primitive common-core normalization, and the single content stratum `v_{109}(beta)=1`. Partial `y`-degree is chart-dependent. Existence, nonexistence, higher Witt digits, bounded gauges, and JC2 are out of scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Over `Z[x,y]`, with `s=x^{108}`, one has `P_x=1+109(A_x-s)`, `P_y=109 A_y`, `Q_x=109 B_x`, `Q_y=1+109 B_y`, and `det J(P,Q)-1 = 109(A_x+B_y-s) + 109^2((A_x-s)B_y-A_y B_x)`. No omitted higher term. This is the packed exact equation of the support-gate erratum, not a separately chosen second residue digit | **CONFIRMED** | a cubic remainder in the correction derivatives; a hidden `109^3` term affecting the first Witt digit; the identity holding only after a digit-wise carry choice |
| 2 | Reducing `(det J-1)/109` modulo `109` gives `bar A_x + bar B_y = x^{108}`. Writing `bar A=sum a_i(x) y^i` and `bar B=sum b_j(x) y^j`, the coefficient of `y^i` is `a_i'+(i+1)b_{i+1}=delta_{i,0} x^{108}`. For `deg_y B=6` the `y^5` row is `a_5'+6 b_6=0`, and every `i>=6` gives `a_i'=0`. The integer `6` is a unit in `F_{109}` | **CONFIRMED** | a `y^5` contribution from `b_7` when `deg_y B=6`; `6=0` in `F_{109}`; the seed `x^{108}` leaking into `i>0` |
| 3 | For `f=sum c_e x^e` in `F_{109}[x]`, the coefficient of `x^e` in a derivative comes only from `x^{e+1}` with scalar `e+1`. Thus `f` lies in `im(d/dx)` if and only if `c_{109k-1}=0` for every `k>=1`. Equivalently `coker(d/dx)` has basis `{x^{109k-1}:k>=1}` and `ker(d/dx)=F_{109}[x^{109}]`. Every `g(x^{109})` is a derivative, via `d/dx(x g(x^{109}))=g(x^{109})` | **CONFIRMED** | a second source monomial for `x^{109k-1}`; `(e+1)` invertible at those exponents; `x^{109}` having nonzero derivative |
| 4 | Seed and Gauss: `q_6=109 B_6` exactly, `h` primitive implies `h^b` primitive, `q_6 in R[x]` forces `beta in R` with `v_{109}(beta)=v_{109}(content(q_6))>=1`, and `bar h != 0`. On `v_{109}(beta)=1` one has `B_6=u h^b` with `u in R^x`, hence `bar b_6 = bar(u) (bar h)^b` with nonzero scalar. Combined with Claim 2 and Claim 3 this is `(0.1)`. Reduction may drop degree (`Hbar <= deg h`); the Cartier condition uses `bar h`, not the characteristic-zero polynomial `h`. Powering commutes with reduction; for `b=2` the leading term of a square cannot cancel | **CONFIRMED** | primitive `h` reducing to `0`; `beta` forced out of `R` after Gauss; `(bar h)^2` losing its leading term in characteristic not `2`; a hidden identification of `Hbar` with `deg h` |
| 5 | If `Hbar=deg(bar h)`, the leading coefficient of `(bar h)^b` is a nonzero `b`-th power in `F_{109}`, of degree `b Hbar`. If that degree is `108 (mod 109)` it is a forbidden Cartier exponent, proving `(0.2)`. For `b=1` this is `Hbar !== 108 (mod 109)`; for `b=2`, invert `2` to get `Hbar !== 54 (mod 109)`. Both residues lie on the already-promoted arithmetic progressions `6|H` / `3|H` when there is no degree drop, so the exclusions are not vacuous relative to the residual stratum. They are implied by `(0.1)`, not equivalent to it | **CONFIRMED** | `2*54 !== 108 (mod 109)`; leading coefficient of a square vanishing; `(0.2)` advertised as equivalent to `(0.1)` |
| 6 | For `i>=6`, `a_i'=0`, in particular `a_m'=0`. On the extra branch `v_{109}(alpha)=1` one gets `(bar h)^a in ker(d/dx)=F_{109}[x^{109}]` with `a=m/d`. Over the perfect field `F_{109}` this is a `109`th power. Unique factorization and `gcd(a,109)=1` force every irreducible exponent in `bar h` to be divisible by `109`, hence `bar h in F_{109}[x^{109}]`. Then `(bar h)^b` is automatically in the derivative image. The hypothesis `gcd(a,109)=1` is necessary: if `109|a` then `a_m'=0` is tautological and does not constrain `bar h` | **CONFIRMED** | `F_{109}[x]` failing unique factorization; `gcd(a,109)=1` omitted while still claiming `bar h` is Frobenius; the positive control sold as holding on `v_{109}(beta)=1` alone |
| 7 | Negative monomial controls: `h=x^{108}`, `b=1` and `h=x^{54}`, `b=2` both produce forbidden coefficient `1` at `x^{108}`. Positive Frobenius controls: `bar h=1+x^{109}` for `b=1,2` lie in the image, admit an explicit polynomial `a_5=-6 int(b_6)`, and realise `bar A_x+bar B_y=x^{108}` with vanishing `y^5` coefficient. Representative Wronskians on the common core vanish identically (including the Cartier-obstructed profile `1+x^{54}` at `d=3`). Top `a_m` on `1+x^{109}` has derivative zero | **CONFIRMED** | a vanishing leading Cartier coefficient on those monomials; the Frobenius samples failing to satisfy the first-Witt `y^5` row; a nonzero Wronskian on a genuine common core |
| 8 | The first-Witt equation and its Cartier cokernel are known (support-gate `E1`, carry-erratum packed form, wild-symplectic floor `[x^{108} y]Q_1=1`, polar conductor as a bounded-category successor, prior bivariate Cartier rows at `p=3`). The leading common core is known. The stopped top two Jacobian bands `y^{m+5}`, `y^{m+4}` cannot see this coefficient: they are tautological on the core and live at `y`-degree `>=16`. Coupling the *low* first-Witt row `y^5` to residual `q_6=beta h^b` on `v_{109}(beta)=1` is not a history duplicate and is not a tautology of the common core. It is vacuous for `deg((bar h)^b)<108` and automatic on the Frobenius subbranch; it can cut only on the complementary high-`Hbar` slice | **CONFIRMED** | the same coupling already written as a promoted residual constraint; the `y^5` first-Witt row identical with Jacobian `[y^5]J` or with the wild floor `[x^{108} y]Q_1`; a universal contradiction on all `v_{109}(beta)=1` profiles |
| 9 | Frozen hashes match the producer listing and `FREEZE.sha256`. Unmodified replay exits 0 and matches `EXPECTED_RESULT.json` byte for byte. Independent sparse arithmetic recovers the packed identity, the `y^i` rows, the Cartier criterion, both leading exclusions, both degree-drop directions, Gauss reduction-powering, and the Wronskian/Cartier independence sample | **CONFIRMED** | a hash mismatch; replay JSON differing from the freeze; independent expansion finding a counterexample to (2.1) or (3.1) |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Independent derivation

### 1. Packed determinant

Set `s=x^{108}`. Direct differentiation:

```text
P_x = 1 - 109 x^{108} + 109 A_x = 1 + 109(A_x - s),
P_y = 109 A_y,
Q_x = 109 B_x,
Q_y = 1 + 109 B_y.
```

The product is quadratic in the correction derivatives and contains no higher power of `109`:

```text
P_x Q_y - P_y Q_x
  = (1 + 109(A_x-s))(1 + 109 B_y) - 109^2 A_y B_x
  = 1 + 109(A_x + B_y - s) + 109^2((A_x-s)B_y - A_y B_x).
```

This is (2.1), as an identity in `Z[x,y]` and therefore in `R[x,y]`. It is the same packed form recorded in the carry erratum

```text
det J(x-x^p+pA, y+pB)-1 = p(L(A,B)-s + p N(A,B)),
```

with `N(A,B)=(A_x-s)B_y-A_y B_x`. No second residue digit is chosen, so the 2026-08-24 carry error does not apply.

Because `R` is torsion-free, `det J=1` implies `A_x+B_y-s+109 N=0` integrally, and reduction modulo `109` is

```text
bar A_x + bar B_y = x^{108}.                                     (2.2)
```

An independent sparse engine, not imported from the registered replay, checked (2.1) on three explicit (non-RNG) pairs, including a degree-`(5,6)` pair and a pair with an `x^{108} y` slot; all three matched.

### 2. Coefficientwise first-Witt rows

Write `bar A=sum_{i>=0} a_i(x) y^i` and `bar B=sum_{j>=0} b_j(x) y^j` in `F_{109}[x][y]`. Then

```text
bar A_x = sum_i a_i' y^i,
bar B_y = sum_j j b_j y^{j-1} = sum_{i>=0} (i+1) b_{i+1} y^i.
```

Equating coefficients of `y^i` in (2.2) gives

```text
a_i' + (i+1) b_{i+1} = delta_{i,0} x^{108}.                      (3.1)
```

The inhomogeneous Cartier monomial `x^{108}` lives only in `i=0`. That is the wild-symplectic first-digit floor, not the row used here.

Now `deg_y B=6` (equivalently `deg_y Q=6`, since the seed `y` has degree `1` and `109` is not a zero-divisor), so `b_j=0` for `j>6`. The row `i=5` is

```text
a_5' + 6 b_6 = 0.                                                (3.2)
```

The scalar `6` is a unit in `F_{109}` (`6*91=546=5*109+1`). For every `i>=6` one has `b_{i+1}=0`, hence `a_i'=0`; in particular `a_m'=0`.

Tried, and failed, to feed `b_7` into (3.2), to let the seed `x-x^{109}` appear in `y^5` of the *first Witt digit*, and to identify (3.2) with the Jacobian band `[y^5]J`. The last is a different object: `[y^5]J` receives every pair `(i,j)` with `i+j=6`, including the seed `p_0`, and is not the equation being coupled. The first-Witt `y^5` row sees only `a_5` and `b_6`.

### 3. Image and cokernel of `d/dx`

Let `f=sum_e c_e x^e` in `F_{109}[x]`. The monomial `x^{e+1}` contributes `(e+1)c` to the coefficient of `x^e` in a derivative, and is the unique source. If `e+1 === 0 (mod 109)`, i.e. `e=109k-1` for `k>=1`, that coefficient is `0` for every input. If `e+1` is invertible, the term integrates uniquely to `(e+1)^{-1} c_e x^{e+1}`, up to adding `ker(d/dx)`.

Hence:

```text
im(d/dx) = { f : c_{109k-1}=0 for all k>=1 },
coker(d/dx)  has basis  { x^{109k-1} : k>=1 },
ker(d/dx)    = F_{109}[x^{109}].
```

The smallest forbidden exponent is `108`; every polynomial of degree at most `107` is therefore a derivative. In characteristic `109`,

```text
d/dx (x g(x^{109})) = g(x^{109}) + x · g'(x^{109}) · 109 x^{108} = g(x^{109}),
```

so `F_{109}[x^{109}] subset im(d/dx)` as well as equal to the kernel. The independent engine recovered: empty obstruction and a matching antiderivative for `1+x^{109}`, `1+x^{54}`, `x`, `x^{107}+3x^6`, and `1+x^{218}`; blocked obstruction `{108:1}` for `x^{108}` and for `x^{114}+x^{108}`; blocked `{217:1}` for `x^{217}`; `d/dx(x(3+5 x^{109}+8 x^{218})) = 3+5 x^{109}+8 x^{218}`; and `d/dx` of `{0:4,109:7,218:2}` equal to zero.

### 4. Primitive common core to Cartier, with degree drop

Over `K[x]`, the already-promoted leading Wronskian `6 p_m' q_6 - m p_m q_6'=0` plus unique factorization give `p_m=alpha h^a`, `q_6=beta h^b` with `a=m/d`, `b=6/d`, and `alpha,beta in K^x`. Scale `h` primitive in `R[x]` (content a unit). Gauss: `content(h^b)=content(h)^b` is a unit, so `h^b` is primitive. Since `q_6 in R[x]`, necessarily `beta in R` and `v_{109}(beta)=v_{109}(content(q_6))`. The seed forces every positive-`y` coefficient of `Q` through `109 B`, and `6>=2`, so `v_{109}(beta)>=1`. The same holds for `alpha` and `p_m`. Integrality of `alpha,beta` is not an extra hypothesis; it is Gauss plus the seed.

Primitivity also forces `bar h != 0` as a polynomial: some coefficient of `h` is a unit.

The `y^6` coefficient of `Q` is exactly `q_6=109 B_6`, because the seed `y` has degree `1`. On the charged branch `v_{109}(beta)=1` write `beta=109 u` with `u in R^x`. Then `B_6 = u h^b`. Reduction is a ring homomorphism, so

```text
bar B_6 = bar(u) (bar h)^b,
```

with `bar(u) != 0`. The first-Witt unknown `b_6` in (3.2) is this reduction. Therefore `6 b_6` is a derivative, hence so is `b_6`, hence so is `(bar h)^b`. That is `(0.1)`.

Attacks that fail:

- *Content normalisation.* Replacing `h` by a unit times `h` does not change `v_{109}(beta)`. Absorbing a factor `109` into `h` would destroy primitivity and is not a legal rescaling of the stated normalisation. The valuation `v_{109}(beta)` is therefore well-defined on the primitive core.
- *Reduction of primitive `h` to zero.* Forbidden by content `1`.
- *Cancellation in `(bar h)^b`.* For `b=1` there is nothing to cancel. For `b=2`, the leading coefficient of a square in a field of characteristic not `2` is a square of a nonzero leading coefficient, hence nonzero; `deg((bar h)^2)=2 Hbar` exactly. Lower Cartier coefficients *can* cancel among cross terms, which is why `(0.1)` is the real condition and `(0.2)` is only the leading shadow. The producer does not equate them.
- *`deg h` versus `deg(bar h)`.* If the leading coefficient of `h` has positive `109`-adic valuation, then `Hbar < deg h`. The Cartier condition is on `bar h`. Two directions were checked independently: `h=109 x^{108}+x^6` is primitive of characteristic-zero degree `108` and reduces to `x^6`, which has empty Cartier obstruction (so a naive `H=108` ban would over-exclude); `h=109 x^{200}+x^{108}+1` reduces onto degree `108` and is forbidden (so using `H` instead of `Hbar` would under-exclude). The producer’s `Hbar` is the correct invariant. No unit-leading-coefficient assumption is used.
- *Powering versus reduction.* For `h=1+109 x+x^2`, content of `h^2` is `1`, and `(h^2 mod 109)=(bar h)^2` as polynomials. No extra `109`-carry creates or destroys finite-field coefficients.
- *Low degree tautology.* The first forbidden exponent is `108`. Thus `(0.1)` is automatic whenever `b Hbar <= 107`, i.e. `Hbar <= 107` for `d=6` and `Hbar <= 53` for `d=3`. Combined with the residual progressions (and no degree drop) the first *possible* leading hit is exactly `Hbar=108` (`d=6`, and `6|108`) or `Hbar=54` (`d=3`, and `3|54`). The producer’s (0.2)--(0.3) are the first nonempty leading cuts, not a constraint on the whole residual arithmetic. This is a precision, not a missing hypothesis: `(0.1)` is correctly the licensed statement, and `(0.2)` is correctly presented as an immediate consequence rather than an equivalent.

The sentence `q_6=109 b_6` in producer §4 identifies the integral coefficient `B_6` with the later-reduced `b_6`. Read as `q_6=109 B_6` followed by `b_6=B_6 mod 109`, it is correct. It is not load-bearingly false.

### 5. Leading-degree exclusions

Let `c` be the leading coefficient of `bar h`, nonzero by definition of `Hbar`. The leading term of `(bar h)^b` is `c^b x^{b Hbar}` with `c^b != 0`. If `b Hbar === 108 (mod 109)`, this exponent is some `109k-1` with `k>=1` (the case `Hbar=0` gives degree `0 !== 108`), and `(0.1)` fails. This is (0.2).

For `d=6`, `b=1`: `Hbar !== 108 (mod 109)`. For `d=3`, `b=2`: `2 Hbar === 108 (mod 109)`. The integer `2` is a unit; `2*54=108`, and if `t` is odd then `108+109t` is odd, hence not a multiple of `2`. So `t` is even and `Hbar=54+109 s`. This is (0.3).

These are not equivalent to `(0.1)`. A non-leading counter-control, not in the registered replay, is `bar h=x^{114}+x^{108}` at `d=6`: `Hbar=114 === 5 !== 108 (mod 109)`, so (0.2) is silent, but the coefficient of `x^{108}` is `1` and (0.1) fails. The producer does not claim otherwise.

### 6. Extra `p_m` valuation / UFD

From (3.1) at `i>=6`, `a_m'=0`, so `bar a_m in F_{109}[x^{109}]`. On the extra branch `v_{109}(alpha)=1` the same Gauss argument as Claim 4 gives `bar a_m = bar(u) (bar h)^a` with `bar(u)!=0`, hence `(bar h)^a in F_{109}[x^{109}]`.

`F_{109}` is perfect. A polynomial `sum c_i x^{109 i}` equals `(sum c_i x^i)^{109}` because `c^{109}=c` in `F_{109}` (Fermat) and the freshman dream holds in characteristic `109`. Thus `(bar h)^a` is a `109`th power in `F_{109}[x]`.

Write `bar h = c prod p_j^{e_j}` in the UFD `F_{109}[x]`. Then `a e_j` is divisible by `109` for every `j`. If `gcd(a,109)=1`, each `e_j` is divisible by `109`, so `bar h in F_{109}[x^{109}]`. (Over `F_{109}` the leading scalar is itself a `109`th power, so “up to scalar” and “after absorbing a scalar” are redundant rather than wrong; they are the correct formulation over a general perfect field of characteristic `109`.) Then `(bar h)^b` is a polynomial in `x^{109}`, hence a derivative, and (0.1) holds automatically.

The coprimeness hypothesis is sharp. Independently, `d/dx((1+x)^{109})=0`, so `a=109` makes `a_m'=0` tautological, while `1+x` is not in `F_{109}[x^{109}]`. The producer states `gcd(m/d,109)=1` as an additional hypothesis on this subbranch and does not claim the Frobenius conclusion without it.

This subbranch is a positive compatibility control, not the new discriminator. Contents of `alpha` and `beta` need not be equal (already recorded in the top-two-band review). The new equations can cut only when `v_{109}(beta)=1` and the top-`P` Frobenius implication is unavailable, and only once `deg((bar h)^b)>=108`.

### 7. Controls, re-derived

Negative:

- `d=6`, `h=x^{108}`, `b=1`: `(bar h)^b=x^{108}`, obstruction `{108:1}`. Residual-compatible: `6|108`.
- `d=3`, `h=x^{54}`, `b=2`: `(x^{54})^2=x^{108}`, obstruction `{108:1}`. Residual-compatible: `3|54`.

Positive:

- `bar h=1+x^{109}` is in `F_{109}[x^{109}]`. For `b=1`, an antiderivative is `x+x^{110}`; for `b=2`, `(1+x^{109})^2=1+2x^{109}+x^{218}` with antiderivative `x+2x^{110}+x^{219}` (because `110 === 219 === 1 (mod 109)`). Setting `a_5=-6` times that antiderivative and `B=x^{108} y + b_6(x) y^6` realises `bar A_x+bar B_y=x^{108}` with vanishing `y^5` coefficient. Support `{1,110}` / `{0,109}` and `{1,110,219}` / `{0,109,218}` matches the frozen JSON, recovered from the antiderivative formula, not from the producer print.

Wronskian (already-promoted top band, not the new constraint): `6 p_m' q_6 - m p_m q_6'` vanishes identically on any common core. In particular it vanishes for the *Cartier-obstructed* profile `h=1+x^{54}` at `(m,d)=(15,3)`, which the registered replay uses as `common_core_wronskian_d3=ZERO`. Independently the same sample has Wronskian the zero polynomial over `Z` and Cartier obstruction `{108:1}` for `(bar h)^2`. That is a feature: the new row is independent of the stopped top band, and a vanishing Wronskian does not imply Cartier.

Top-`P` control: `(1+x^{109})^2` has derivative zero in `F_{109}[x]`.

The replay’s twelve packed-determinant samples are RNG regression, not a proof of (2.1). The proof is the expansion in §1. Absence of a registered non-leading obstruction sample is a control-suite limitation, not a gap in `(0.1)` versus `(0.2)`.

### 8. Novelty

Already in the record, and not re-promoted here:

- Packed first-Witt equation `A_x+B_y=x^{108}`: support gate `E1`, carry-erratum packed form (Claim 1 of this review).
- Univariate/bivariate Cartier cokernel of derivatives: wild-symplectic floor `[x^{p-1} y]Q_1=1` (the *`i=0`* instance of (3.1), forcing the Cartier monomial into the linear-in-`y` slot of `B`); `p=3` F-only/gauge-growth Cartier rows `x^{3k-1} y^{3m-1}`.
- Leading common core `p_m=alpha h^{m/d}`, `q_6=beta h^{6/d}`: one-sided floor-six composition, confirmed.
- Top two Jacobian bands `y^{m+5}` and `y^{m+4}`: face-isolation producer `TWO_BANDS_TAUTOLOGICAL`, confirmed with a non-load-bearing wording repair. Band one is identically zero on the core. Band two is an underdetermined ODE in the next coefficients, with every summand of valuation at least `2`. Card F3 forbade descending; seed-seeing Jacobian bands start at `y^m` or at Jacobian-`y^5`, neither of which is the first-Witt `y^5` row.
- W2/W3 gauge-conductor at a support cap: history duplicate of the confirmed polar-conductor (`kappa_n -> infinity`) and wild-symplectic (one completed orbit) theorems. The present producer correctly refuses that successor.

The coupling that is new is exactly this: on residual `n=6`, the first-Witt unknown `b_6` *is* the reduction of `q_6/109`, so the low row (3.2) becomes a Cartier condition on `(bar h)^b` when `v_{109}(beta)=1`. That coefficient is invisible to the two highest Jacobian bands, is not the wild floor `[x^{108} y]Q_1`, and is not tautological on the common core (the core does not constrain the shape of `bar h` except on the extra Frobenius subbranch). It is a genuine necessary condition on one content stratum, vacuous at low `Hbar` and automatic when `bar h` is Frobenius.

The cheapest honest successor remains the producer’s three-way content split

```text
v_{109}(beta)=1, v_{109}(alpha)=1;
v_{109}(beta)=1, v_{109}(alpha)>=2;
v_{109}(beta)>=2,
```

intersected with the existing residual parameterisation. The first is the positive control. The second is where (0.1) can cut. The third is invisible at this digit. None of those intersections is performed here, and a nonempty intersection would still not be a lift.

---

## Replay and hashes

Frozen listing, recomputed:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as109-n6-low-witt-common-core-cartier-producer-sol-20260827.md` | `c79dfbf550962c1fcbae974b6fe1ab1867489ceb8a93906ad4b7739a49522526` | launch prompt |
| `cases/as109_n6_low_witt_cartier_v1_20260827/FREEZE.sha256` | `fcb578ae1940e19d0b7b76e39db33754ac1471e61f462e3e19388d572ae6900a` | producer §1 |
| `.../PREREGISTRATION.md` | `5f3dd79b6050d2a66429866ad95a3068fbc1116ed6bdd26aad61fd5a7e784bea` | `FREEZE.sha256` |
| `.../verify_low_witt_cartier.py` | `65097ad0aa07447b442a07ce4ca865f834978c87136b1b78d1d068acf75bc5a8` | `FREEZE.sha256` |
| `.../EXPECTED_RESULT.json` | `e0fbc93fa41feaa377d1e75a2457bf7539a68ce625db3f266f40fa5c58477907` | `FREEZE.sha256` |
| `xmodel/as109-one-sided-prime4-composition-sol-20260827.md` | `3d6d09fd1c9d1548dc6af78221f74c83276eb89378ee06cecac5fd19b46fcb36` | producer §1 |
| `xmodel/as109-n6-top-two-y-bands-face-isolation-grok-20260827.md` | `7640715607c640beae845855feb261a0d207ea9409a1ccf8a915899f4461ec10` | producer §1 |
| `xmodel/as109-n6-top-two-y-bands-face-isolation-hostile-review-sol-20260827.md` | `571c5e2bda00cf9221debcd43b26f635016a68622714bbf8bbb0e2a68f33525f` | producer §1 |
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` | producer §1 |
| `xmodel/as109-support-gate-20260824-erratum.md` | `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb` | producer §1 |

`shasum -a 256 -c cases/as109_n6_low_witt_cartier_v1_20260827/FREEZE.sha256` reports `OK` on all three payload lines.

Registered command, rerun unmodified from the repository root:

```text
python3 cases/as109_n6_low_witt_cartier_v1_20260827/verify_low_witt_cartier.py
```

Exit code 0. Stdout equals `EXPECTED_RESULT.json` byte for byte (SHA-256 `e0fbc93fa41feaa377d1e75a2457bf7539a68ce625db3f266f40fa5c58477907`). Advertised fields:

```text
verdict                              PASS-LOW-WITT-CARTIER
packed_determinant_identity          true (12/12)
d6_Hbar_108_obstruction              {108: 1}
d3_Hbar_54_squared_obstruction       {108: 1}
common_core_wronskian_d6             ZERO
common_core_wronskian_d3             ZERO
top_a_frobenius_derivative           ZERO
```

What the replay actually checks, versus what the report proves:

- twelve seeded sparse integer pairs for the packed identity (2.1), as regression;
- monomial Cartier obstructions `x^{108}` and `(x^{54})^2`;
- Frobenius samples `1+x^{109}` at `b=1,2`, with explicit antiderivative, `a_5`, and first-Witt reconstruction including a compensating `x^{108} y` slot;
- integer Wronskians at `(m,d,h)=(12,6,1+x^{109})` and `(15,3,1+x^{54})`;
- derivative of `(1+x^{109})^2`.

It does not prove (2.1) or (3.1) in general, does not enumerate residual cores, and does not exhibit a non-leading Cartier failure. That division of labour is what the producer states.

---

## Licensed conclusion

Bank only this statement, at the primitive common-core normalisation:

> An exact AS109 residual `n=6` lift whose `q_6` common-core scalar has `109`-adic valuation exactly one must satisfy the coefficientwise Cartier condition `(bar h)^{6/d} in im(d/dx)` on `F_{109}[x]`, hence the leading-degree exclusions `Hbar !== 108 (mod 109)` for `d=6` and `Hbar !== 54 (mod 109)` for `d=3`. On the extra subbranch `v_{109}(alpha)=1` and `gcd(m/d,109)=1`, the same condition is automatic because `bar h in F_{109}[x^{109}]`.

Do not infer that the `v_{109}(beta)=1` branch is populated, that `v_{109}(beta)>=2` is constrained, that residual `n=6` is empty, that a polynomial AS109 lift exists, or that one is impossible. Do not launch a W2/W3 bounded-gauge duplicate of polar-conductor / wild-symplectic. A compatible finite support, if one ever emerges on a surviving content stratum, may be tested against the already-reviewed `CLOSED-SUPPORT + UNIT-L` contraction criterion; that remains a possible construction route, not a conclusion of this gate or of this review.

---

## Scope firewall

This review does **not**:

- prove that `v_{109}(beta)=1`, that `v_{109}(alpha)=1`, or that either content pattern occurs in a lift;
- identify `Hbar` with `deg(h)` when the leading coefficient of `h` reduces to zero;
- inspect `v_{109}(beta)>1`;
- run another top Jacobian band, W2/W3, a bounded gauge, a support cap, or a degree rectangle;
- construct a closed nonlinear support module;
- prove or disprove an AS109 polynomial lift, a characteristic-zero counterexample, Gate T, or JC2.

Tried hard, and failed, to break Gauss integrality of `alpha,beta`, to make a primitive `h` reduce to zero, to cancel the leading term of `(bar h)^b`, to smuggle `deg h` in place of `Hbar`, to equate the first-Witt `y^5` row with a tautology of the common core or with the stopped top two Jacobian bands, and to let UFD promote `bar h` to a `109`th power without `gcd(m/d,109)=1`.
