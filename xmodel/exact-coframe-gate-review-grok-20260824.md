# Hostile different-model review — frozen exact-coframe gate

| Field | Value |
|---|---|
| Claim under review | Frozen exact-coframe gate: one-way closed-row + det-1 + literal non-`E_2` bridge; Cohn/Park lineage and `y ↦ 2y` transport; completeness of `M(h)=L(h)C_B`; curl equation `δh=6y`; empty `H_2` tangent with unit certificate; weight recurrence / terminal obstruction / rational control; one-left-shear scope; Wright priority and rejection of Shpilrain–Yu Prop. 2.4's printed arbitrary-second-row strengthening |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Evidence tier | independent exact arithmetic over `Q` (two engines); primary-source read of Cohn 1966, Park 1995, Shpilrain–Yu 1997, Nguyen Van Chau 2003/arXiv:math/0408077, Chapovskyi–Kozachok–Petravchuk arXiv:2412.03688v1; registered replay byte-identical |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family, root E) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `dd11599b07eb05591b5c006791005eef19457d8e` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T07:04:24Z – 2026-08-24T07:12:00Z |
| Python | 3.14.6; stdlib `fractions.Fraction` only (no SymPy in the attack engine) |
| Host | Darwin arm64 |

The background file `xmodel/exact-coframe-background-review-grok-20260824.md` was read only as prior background. It is not a vote on the producer artifact. Every algebraic identity below was recomputed from the frozen gate files.

**Promotion.** None. No claim, lemma, family, certificate, or wording may be promoted off this record. The scoped no-go is not JC2 and not a theorem on the full elementary double orbit.

**Quarantine.** Do not treat emptiness of this one-left-shear family as evidence against exact coframes in `E_2 C E_2` with a changed first row. Do not write `SL_2/E_2` as a group. Do not upgrade emptiness of exact coframes to a proof of JC2. Do not widen shear, coordinates, degree, or support.

---

## Headline and subclaim table

Let `S = C[x,y]` (exact replay over `Q[x,y]`). Write

```text
U(f) = [[1, f], [0, 1]],     L(f) = [[1, 0], [f, 1]],
```

and let `E_2(S)` be the subgroup they generate. Jacobian convention is the row-gradient matrix `J(P,Q) = [[P_x, P_y], [Q_x, Q_y]]`. Curl is `curl(r,s) = r_y - s_x`.

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Closed rows + `det M = 1` + `M ∉ E_2(S)` ⇒ the rows integrate to a det-1 Keller nonautomorphism. Proof uses only polynomial Poincaré, Jung–van der Kulk, substitution, and explicit constant-`GL_2` normalisation; no normality of `E_2` in `SL_2` | **CONFIRMED** | Poincaré lemma false in char 0; Jung–van der Kulk false over `C`; conjugation `diag(λ,1) U(f) diag(λ^{-1},1) = U(λ f)` failing; a det-1 automorphism with Jacobian outside `E_2` |
| 2 | Cohn matrix `C ∉ E_2` (in fact `∉ GE_2`) by Cohn 1966 Prop. 7.3 and Park 1995 Thm. 5.2.1; `C_alt` has the same literal lineage; `θ(x)=x`, `θ(y)=2y` is the unique scaling `y ↦ λy` making the first row closed and transports nonmembership | **CONFIRMED** | a published elementary factorization of this `C`; Park's leading-term test passing on `C`; `θ^{-1}` failing to be a ring automorphism over `Q` or `C`; first-row closedness for some `λ ≠ 2` |
| 3 | Every det-1 polynomial matrix with first row `(1+2xy, x^2)` is `M(h)=L(h)C_B` for a unique `h ∈ S` | **CONFIRMED** | a second-row difference `(p,q)` with `a q - b p = 0` but `(p,q)` not a polynomial multiple of `(a,b)`; `det C_B ≠ 1` |
| 4 | Second-row closedness on this family is exactly `(1+2xy) h_y - x^2 h_x = 6y` | **CONFIRMED** | a leftover `2xh` term; `curl_2(C_B) ≠ -6y`; the identity `curl_2(L(h)C_B) = curl_2(C_B) + δh` failing on any monomial |
| 5 | On `H_2 = span_Q{y^2, xy^3, x^2 y^4}`, the map `δ` has matrix rank 3 and augmented rank 4 against `6y`; explicit unit certificate `-1/6 e_0 + 1/12 e_1 - 1/20 e_2 + 1/30 e_3 = 1` | **CONFIRMED** | rank `[A | t] = rank A`; the displayed linear combination failing to cancel the `c_i` and to produce the constant 1 |
| 6 | Weight `w(x^i y^j)=i-j` is raised by 1 under `δ`; only the weight `-2` part of a polynomial `h` can hit `6y`; the recurrence is `c_n = (-1)^n (n+3)` with uncancelled terminal `(N+4) c_N x^{N+1} y^{N+2}`; the rational control `h_rat = y^2(3+2xy)/(1+xy)^2` satisfies `δ h_rat = 6y` and is the nonterminating generating function | **CONFIRMED** | a weight `≠ -2` monomial with `δ`-image of weight `-1`; a finite `N` with `(N+4)c_N = 0` in char 0; a nonzero numerator for `δ(N/D)-6y` |
| 7 | The no-go is exactly: no polynomial left shear completes the fixed Broughton first row in the Cohn non-`E_2` lineage. It is not a theorem on `E_2 C E_2` with a changed first row, and not a theorem on JC2 | **CONFIRMED** | the producer promoting the empty tangent to JC2; a silent right factor or second left factor entering the verdict |
| 8 | Wright 1978 (via the printed restatement of Theorem 6, p. 250, in Shpilrain–Yu) is prior art for the broader exact-coframe dichotomy on a *full* det-1 Jacobian. Shpilrain–Yu Proposition 2.4's printed arbitrary-second-row strengthening is false, with counterexample `L(y)` | **CONFIRMED** | Wright's actual hypothesis being an arbitrary second row; `curl_2(L(y))=0`; a primary Wright text reversing the GE2⇒automorphism direction |

All remarks below are non-blocking unless marked otherwise. None changes a coefficient, a rank, or a verdict.

---

## Independent recomputation

Two engines:

- the registered script `cases/exact_coframe_gate_20260824/replay_exact.py`, rerun unmodified;
- a separate sparse monomial ring over `Q` written for this review, not imported from the registered script.

They agree on every polynomial identity the registered script actually computes. The global recurrence, unit certificate, completeness argument, and bridge lemmas are not derived by the registered script; they were attacked by hand and by the second engine.

### 1. Bridge — CONFIRMED

**Exactness.** In characteristic zero, a polynomial 1-form `a dx + b dy` is exact iff it is closed. The primitive

```text
P(x,y) = ∫_0^x a(t,y) dt + ∫_0^y b(0,s) ds
```

is a polynomial, `P_x = a`, and `a_y = b_x` gives `P_y = b`. Same for the second row. Additive constants do not change `J(P,Q)`. If `det M = 1` then `[P,Q] = 1`.

Independent check on the frozen first row of `C_B`: `a = 1+2xy`, `b = x^2`, `b(0,s) = 0`, so `P = x + x^2 y`. Matches `P_x, P_y`.

**Tame Jacobians lie in `E_2` after det-1.** Nguyen Van Chau, arXiv:math/0408077, states Jung's theorem over `C` in the exact generation form used by the producer: every polynomial automorphism of `C^2` is a finite product of linear automorphisms and shears `(x,y) ↦ (x+p(y), y)`. (Van der Kulk 1953 is the arbitrary-field source; conjugation by a linear swap supplies the other triangular orientation.)

Shear Jacobian: `U(p'(y)) ∈ E_2`. Linear Jacobian: constant in `GL_2(C)`. Chain rule: `J(Φ∘Ψ) = (JΦ ∘ Ψ) JΨ`. Substitution sends `U(f) ↦ U(f∘Ψ)` and `L(f) ↦ L(f∘Ψ)`, hence preserves `E_2`.

Constant conjugation, independently expanded:

```text
diag(λ,1) U(f) diag(λ^{-1},1) = U(λ f),
diag(λ,1) L(f) diag(λ^{-1},1) = L(λ^{-1} f).
```

Write `K = diag(det K, 1) K_0` with `K_0 ∈ SL_2(C)`. Gaussian elimination puts `K_0` in `E_2(C)`. The Weyl element is

```text
[[0,-1],[1,0]] = U(-1) L(1) U(-1),
```

checked identically by the second engine. For `u ≠ 0`,

```text
diag(u, u^{-1})
  = (U(u) L(-u^{-1}) U(u)) (U(-1) L(1) U(-1)),
```

checked by the same multiplication (producer formula; the intermediate is `[[0,u],[-u^{-1},0]]` times the Weyl element). Thus constant `GL_2(C)` normalises `E_2(S)` by explicit formulae, with no appeal to normality of `E_2` in `SL_2(S)`.

Inductively every plane automorphism `Φ` has `JΦ = K E` with `K ∈ GL_2(C)` and `E ∈ E_2(S)`. If `det JΦ = 1` then `det K = 1`, so `K ∈ SL_2(C) = E_2(C) ⊂ E_2(S)` and `JΦ ∈ E_2(S)`.

**Nonautomorphism.** If the integrated `(P,Q)` were a polynomial automorphism, `M = J(P,Q)` would lie in `E_2(S)`, contrary to literal nonmembership. No collision is required for this implication. The converse (`M ∈ E_2 ⇒` automorphism) is not part of the one-way bridge; it is Wright, treated in subclaim 8.

Fatal preregistration outcomes (Cohn lineage uncertified; tame-to-`E_2` failure; integration changing the Jacobian convention; a step needing `E_2 ◃ SL_2`) do not occur.

### 2. Cohn / Park lineage and `y ↦ 2y` — CONFIRMED

**Cohn 1966, primary PDF.** SHA-256 `3fa7efc1453144af36d87e27ec961a5848852756137f725650355ffcbd2d7957`. Proposition 7.3 (end of §7, immediately before §8): if a `k`-ring with a degree function is a `GE_2`-ring, then of any two elements of the same degree forming a regular row, each is `R`-dependent on the other. Total degree on `k[x,y]`; regular row `(1+xy, x^2)`; neither is `R`-dependent on the other. Therefore

```text
C = [[1+xy, x^2], [-y^2, 1-xy]]
```

“cannot be expressed as a product of elementary matrices.” Independent replay: `det C = 1`, `curl(C) = (-x, -y)`. So `C ∉ GE_2`, hence `C ∉ E_2`.

Non-blocking citation defect: the producer report and source audit say “section 8”. Section 8 of Cohn is “Discretely ordered rings.” The displayed matrix and the `k[x,y]` obstruction sit at the end of §7 (Prop. 7.3). The identity is right; the section number is wrong.

**Park 1995, primary dissertation.** SHA-256 `422b952fe8243deefc1c5f298b14d7628d30680e20c3d839897a94a9c4c12357`, retrieved from `https://digitalassets.lib.berkeley.edu/techreports/ucb/text/ERL-95-39.pdf`. Theorem 5.2.1, printed page 52: if `A ∈ SL_2(k[x])` is realizable (product of elementary matrices) then, for any monomial order, either `lt(A)` has rank 2 or one leading row is a monomial multiple of the other. Remark 5.2.2, printed pages 52–53, is the Cohn replay: `lt(C)` has rank 1 and the rows are `x(y,x)` and `-y(y,x)`, neither a monomial multiple of the other. This is exactly the certificate the producer uses. It works over `Q` or `C`. No Mennicke symbol is involved.

For this `C` every graded monomial order gives the same leading-term matrix `[[xy, x^2], [-y^2, -xy]]`, because each off-constant summand is already a monomial of total degree 2.

**Alternate form.** Independently,

```text
C(x,-y) [[0,-1],[1,0]] = [[x^2, xy-1],[xy+1, y^2]] = C_alt,
```

and the constant rotation is `U(-1)L(1)U(-1)`. Both factors of the identity are obstruction-preserving (ring automorphism; elementary multiplication). Chapovskyi–Kozachok–Petravchuk arXiv:2412.03688v1 (SHA-256 `c85a9ed67faebaecf2de88dc4571113678dfe2771f0c29eef2545e7a57e443c7`) prints this `C_alt` as Cohn's counterexample. Non-blocking: the source audit's “current manuscript date 2026-03-22” was not found; arXiv currently serves only v1 (4 Dec 2024). The matrix is already in v1.

**Transport `y ↦ λy`.** Applying `θ_λ(x)=x`, `θ_λ(y)=λy` to entries of `C` yields `[[1+λ xy, x^2], [-λ^2 y^2, 1-λ xy]]`. First-row curl is `(λ-2)x`. The unique `λ ∈ Q \ {0}` making the first row closed is `λ=2`. Then

```text
C_B = [[1+2xy, x^2], [-4y^2, 1-2xy]],
det C_B = 1,     curl(C_B) = (0, -6y).
```

Over `Q` or `C`, `2` is a unit, so `θ` is a ring automorphism with inverse `y ↦ y/2`. Automorphisms send elementary generators to elementary generators in both directions. Hence `C_B ∉ E_2`. Independently, Park's test on `C_B` itself also fails: leading rows `x(2y, x)` and `-2y(2y, x)`.

The first row of `C_B` is `dP` for `P = x + x^2 y`. Directly: `P_x = 1+2xy` and `P_y = x^2` have no common zero (if `x=0` then `P_x=1`); `P^{-1}(0) = {x=0} ∪ {1+xy=0}` is reducible. Broughton 1988 is a control label, not a topological premise.

### 3. Completeness of `M(h)=L(h)C_B` — CONFIRMED

Let `M'` be any matrix in `SL_2(S)` with the same first row `(a,b) = (1+2xy, x^2)` as `C_B`. Then

```text
M' C_B^{-1}
```

has first row `(1,0)` (because `C_B^{-1}` is the adjugate, and `det C_B = 1`). A det-1 matrix with first row `(1,0)` is exactly `L(h)` for `h` equal to its `(2,1)`-entry. Thus `M' = L(h) C_B` for a unique polynomial `h`. Independently: `C_B · adj(C_B) = I` and `(a,b) · adj(C_B) = (1,0)` were checked by the second engine.

The producer's coprime-row argument is the same fact in coordinates: `det M' = det C_B = 1` forces `a q - b p = 0` on the second-row difference `(p,q)`, and the explicit unimodular identity

```text
(1-2xy)a + 4 y^2 b = 1
```

(which is `det C_B = 1` rewritten) gives `p = h a`, `q = h b`. Language “coprime” is weaker than unimodular, but the identity they display is the unimodular one, and `C[x,y]` is a domain, so `a ≠ 0` cancels. No missing hypothesis.

If `M(h)` were elementary then `L(-h) M(h) = C_B` would be elementary. The whole family is therefore non-`E_2`.

Among elementary generators, only left shears can preserve this first row: a nontrivial right `U(s)` or `L(s)` changes `(a,b)`. Completeness is stronger than “the licensed left shears”: it is all of `SL_2` with this first row.

### 4. Curl equation — CONFIRMED

Second row of `M(h)`:

```text
(-4y^2 + h(1+2xy),  1-2xy + h x^2).
```

Expanding `curl_2` with `h` an arbitrary polynomial:

```text
∂_y(-4y^2 + h(1+2xy)) - ∂_x(1-2xy + h x^2)
  = -8y + (1+2xy) h_y + 2x h + 2y - x^2 h_x - 2x h
  = -6y + (1+2xy) h_y - x^2 h_x.
```

The `2xh` terms cancel. Define `δ = (1+2xy) ∂_y - x^2 ∂_x`. Then `curl_2(M(h)) = -6y + δh`. Closedness is `δh = 6y`.

Hostile monomial sweep: for every monomial `x^i y^j` with `0 ≤ i,j ≤ 6`,

```text
curl_2(L(x^i y^j) C_B) = curl_2(C_B) + δ(x^i y^j),
det(L(x^i y^j) C_B) = 1,     curl_1 = 0.
```

No failures. The first row remains closed for every `h` because left `L(h)` does not change it.

### 5. Frozen `H_2` ranks and unit certificate — CONFIRMED

```text
δ(y^2)     = 2y + 4 x y^2,
δ(x y^3)   = 3 x y^2 + 5 x^2 y^3,
δ(x^2 y^4) = 4 x^2 y^3 + 6 x^3 y^4.
```

Output span `{y, x y^2, x^2 y^3, x^3 y^4}` is exhaustive for these images. Matrix and target:

```text
A = [[2, 0, 0],
     [4, 3, 0],
     [0, 5, 4],
     [0, 0, 6]],     t = [6, 0, 0, 0]^T.
```

Exact Gaussian elimination over `Q`: `rank A = 3`, `rank[A|t] = 4`. So `6y ∉ δ(H_2)`. Affine-linear family ⇒ the tangent equations are the exact bounded equations. EMPTY-TANGENT; elimination not licensed.

Coefficient residuals:

```text
e0 = 2 c0 - 6,     e1 = 4 c0 + 3 c1,     e2 = 5 c1 + 4 c2,     e3 = 6 c2.
```

The displayed combination is an identity in the parameters:

```text
(-1/6) e0 + (1/12) e1 + (-1/20) e2 + (1/30) e3  =  1.
```

Second engine: the combination applied to `(c0,c1,c2,constant)` returns `(0,0,0,1)`. Equivalently the left kernel vector `v = (-1/6, 1/12, -1/20, 1/30)` satisfies `v A = 0` and `v · t = -1 ≠ 0`. Unit-ideal certificate holds. It is *not* computed by the registered script; the script only prints ranks. The independent check is what certifies it.

### 6. Weight recurrence, terminal obstruction, rational control — CONFIRMED

For any monomial,

```text
δ(x^i y^j) = j x^i y^{j-1} + (2j - i) x^{i+1} y^j.
```

Both surviving terms have weight `w+1` (the first term is absent if `j=0`; the second if `2j=i`; if `i=j=0` then `δ(1)=0`). Sweep `0 ≤ i,j ≤ 7`: no weight leak. Thus `δ` is strictly of weight `+1` on polynomials.

`6y` has weight `-1`, so only the weight `-2` summand of `h` can contribute. That summand is exactly

```text
h_{-2} = Σ_{n=0}^N c_n x^n y^{n+2}.
```

Kernel elements of other weights cannot cancel a weight `-1` residual. On weight `-2` itself the homogeneous problem has `2c_0 = 0`, hence is trivial.

```text
δ(x^n y^{n+2}) = (n+2) x^n y^{n+1} + (n+4) x^{n+1} y^{n+2}.
```

Coefficient of `y`: `2 c_0 = 6`, so `c_0 = 3`. For `n ≥ 1`, coefficient of `x^n y^{n+1}`:

```text
(n+2) c_n + (n+3) c_{n-1} = 0  ⇒  c_n = (-1)^n (n+3).
```

Every `c_n` is nonzero in characteristic zero. A finite truncation of length `N` leaves the uncancelled terminal monomial

```text
(N+4) c_N x^{N+1} y^{N+2} ≠ 0.
```

Independent check of the closed form through `N=7`: intermediates vanish, the `y`-coefficient is 6, and the terminal coefficient is `(N+4)(-1)^N (N+3)`, matching `(N+4)c_N`. Therefore no polynomial `h` satisfies `δh = 6y`.

The registered script *prints* the recurrence as a string; it does not derive it. The derivation above is independent of that print.

**Rational control.** Let `N = y^2(3+2xy)`, `D = (1+xy)^2`. Quotient rule for the derivation `δ`:

```text
δ(N) D - N δ(D) - 6y D^2  =  0
```

identically (both engines). So `δ(N/D) = 6y` in `Q(x,y)`. Expanding in `z = xy`,

```text
(3+2z)/(1+z)^2 = Σ_{n≥0} (-1)^n (n+3) z^n,
```

checked by multiplying the truncated series by `(1+z)^2` through degree 11 and recovering `3+2z`. This is the nonterminating generating function of the same recurrence. The pole along `1+xy=0` is the obstruction; the rational solution is not a polynomial survivor.

### 7. Scope — CONFIRMED

The producer theorem is:

> There is no polynomial `h` for which `L(h) C_B` has both rows closed.

Equivalently: the exact Broughton row `d(x+x^2 y)` has no det-1 closed polynomial completion in this Cohn non-`E_2` lineage with the first row held fixed.

The report does not close `E_2 C E_2` with a changed first row. It does not claim JC2. It does not run a right factor, a second left factor, a coordinate change, a generic sparse family, or a second elimination. Post-freeze coordinator remarks about `x + x^m y` and length-two left words are explicitly unused. This matches the preregistration.

A right elementary factor would change the first row (subclaim 3). A second left `U`-factor would also change the first row. Those are different gates.

### 8. Priority wording — CONFIRMED

**Wright.** The 1978 JPAA paper was not retrieved as a body in this session (ScienceDirect still does not expose it here). The DOI `10.1016/0022-4049(87)90004-1` is the MathSciNet/AMS identifier for Wright, *J. Pure Appl. Algebra* 12 (1978) 235–251; the author's publication list confirms the title including “the weak Jacobian theorem for two variables.” Shpilrain–Yu, *J. Algebra* 197 (1997), author PDF `https://shpilrain.ccny.cuny.edu/paperyu.pdf` (SHA-256 `4c6e041f037a7f7116626edf0e49b8fdc3a1759e4095d0f3186ec59c8f5b613f`), printed page 6, restates Wright's Theorem 6, p. 250:

> if `p,q` are two polynomials from `P_2` and the corresponding Jacobian matrix belongs to `GE_2(P_2)`, then `p` and `q` generate `P_2`; in particular they are both coordinate polynomials.

Combined with Jung–van der Kulk (subclaim 1) and the elementary nature of constant det-1 diagonals, this is the biconditional, for a *full* det-1 polynomial Jacobian:

```text
J(P,Q) ∈ E_2(C[x,y])  ⇔  (P,Q) is a polynomial automorphism.
```

The one-way bridge of this gate is the Jung–van der Kulk direction plus Poincaré. It is classical, not a new reformulation. Wright is prior art for the converse and hence for the dichotomy. The producer retains a self-contained proof of the direction the gate actually uses. That priority wording is correct.

Non-blocking: the opening sentence of the producer report attributes the full dichotomy to Wright alone; the later paragraph correctly says “Combining Wright with Jung–van der Kulk.” No identity fails.

**Shpilrain–Yu Proposition 2.4, printed.** After restating Wright, the paper prints a strengthening: if

```text
J = [[d1(p), d2(p)], [s1, s2]] ∈ GE_2(P_2),
```

then `p` is a coordinate, and furthermore there is `q` with `s_i = d_i(q)` such that `p,q` generate `P_2`. Take

```text
p = x,     J = L(y) = [[1, 0], [y, 1]] ∈ E_2 ⊂ GE_2.
```

First row is `dx`. Second-row curl is `1 ≠ 0`. Independently: `det L(y)=1`, `curl = (0, 1)`. So the printed “furthermore” is false. This does not touch Wright, whose hypothesis is a full Jacobian, and does not touch the coordinate conclusion for `p=x`. The producer does not use Proposition 2.4 anywhere in the no-go. Correct rejection.

---

## Registered replay

Command: `python3 cases/exact_coframe_gate_20260824/replay_exact.py`

Live stdout is byte-identical to `cases/exact_coframe_gate_20260824/replay_exact.txt` (SHA-256 `8bce91b8495a4b163640af0b5936837758ed0fb9660385cf37e73667745bc751`).

```text
EXACT-COFRAME-GATE-20260824
engine=python-stdlib sparse polynomial ring over Q
det(C)=1
curl_rows(C)=['-x', '-y']
det(C_B)=1
C_B=[[2*x*y + 1,x^2],[-4*y^2,-2*x*y + 1]]
curl_rows(C_B)=['0', '-6*y']
first_row_integral_P=x^2*y + x
unimodular_identity=1
h=x^2*y^4*c2 + x*y^3*c1 + y^2*c0
det(M(h))=1
curl_row_1(M(h))=0
curl_row_2(M(h))=6*x^3*y^4*c2 + 5*x^2*y^3*c1 + 4*x^2*y^3*c2 + 4*x*y^2*c0 + 3*x*y^2*c1 + 2*y*c0 - 6*y
delta_basis=['4*x*y^2 + 2*y', '5*x^2*y^3 + 3*x*y^2', '6*x^3*y^4 + 4*x^2*y^3']
output_basis=['y', 'x*y^2', 'x^2*y^3', 'x^3*y^4']
linearized_matrix=[['2', '0', '0'], ['4', '3', '0'], ['0', '5', '4'], ['0', '0', '6']]
target=['6', '0', '0', '0']
rank=3
augmented_rank=4
target_in_image=False
coefficient_equations=['2*c0 - 6', '4*c0 + 3*c1', '5*c1 + 4*c2', '6*c2']
linsolve=EMPTY
elimination_licensed=False
rational_solution_numerator_check=0
formal_series_coefficients_n0_to_n6=[Fraction(3, 1), Fraction(-4, 1), Fraction(5, 1), Fraction(-6, 1), Fraction(7, 1), Fraction(-8, 1), Fraction(9, 1)]
global_recurrence=c_0=3; (n+2)c_n+(n+3)c_(n-1)=0 for n>=1
global_coefficients=c_n=(-1)^n(n+3)
terminal_residual=(N+4)c_N*x^(N+1)*y^(N+2), nonzero for finite N
VERDICT=EMPTY-TANGENT; ELIMINATION_NOT_LICENSED; ONE-SHEAR-NO-POLYNOMIAL
```

The last four printed lines are documentation, not a computation. They happen to be correct (subclaim 6).

---

## Hashes

Recomputed on disk at 2026-08-24T07:05:43Z.

| Artifact | SHA-256 |
|---|---|
| `xmodel/exact-coframe-gate-20260824.md` | `8aad8b60777fb7d52fb037df961f1204f255ee36f1775a3f8c772d1739691571` |
| `cases/exact_coframe_gate_20260824/00_preregistration.md` | `d0d629c6231f814d2cd3ac0fdf76baef4240cbb6271b2271ae9a9f95e6d54658` |
| `cases/exact_coframe_gate_20260824/01_source_audit.md` | `52e39a480dfd52f1d95d8daf33a9f62695c3fe5f3635319005bc240031b27ce8` |
| `cases/exact_coframe_gate_20260824/replay_exact.py` | `e02ae9da94b01ac337fabd65b8733557503963fa19ba9963548b6e2059a30920` |
| `cases/exact_coframe_gate_20260824/replay_exact.txt` | `8bce91b8495a4b163640af0b5936837758ed0fb9660385cf37e73667745bc751` |
| `xmodel/ideation-20260824T0453Z-synthesis.md` | `76d9b7685771f65138fcb3c3dba1cfdd1ab104a9a5b21a7e3262c971f96ff790` |
| `xmodel/exact-coframe-background-review-grok-20260824.md` (background only) | `1fa8b5cc89d35163ad0aa43e1eb0a2fc3f7f1f6a28cbcf2085af45a0dca2e553` |

The four case-file hashes match the producer report's artifact table. The synthesis hash matches the producer header. The producer-report hash is not in that table (the report says it is recorded after freeze); the on-disk value is as above.

Primary sources retrieved this session:

| Source | SHA-256 |
|---|---|
| Cohn 1966 NUMDAM PDF | `3fa7efc1453144af36d87e27ec961a5848852756137f725650355ffcbd2d7957` |
| Park 1995 ERL-95-39 PDF | `422b952fe8243deefc1c5f298b14d7628d30680e20c3d839897a94a9c4c12357` |
| Shpilrain–Yu author PDF | `4c6e041f037a7f7116626edf0e49b8fdc3a1759e4095d0f3186ec59c8f5b613f` |
| Nguyen Van Chau arXiv:math/0408077 PDF | `b2c5815afad9af4c746d723f4a01b7d134834d952e19214d228096b246f15812` |
| arXiv:2412.03688v1 PDF | `c85a9ed67faebaecf2de88dc4571113678dfe2771f0c29eef2545e7a57e443c7` |
| Wright 1976 BAMS announcement PDF | `a0dc25b58f1ca8b8f8906dafd7c23c7068476d3dcd867cdcab013caec20bb229` |

Wright 1978 JPAA body: not retrieved. Weak Jacobian statement taken from Shpilrain–Yu's primary reprint of Theorem 6, p. 250, as in the producer source audit.

---

## Promotion advice

Do not promote.

- The one-way bridge is correct and classical. It is a disproof certificate, not a new theorem.
- The gate-specific result is a complete one-left-shear no-go for the fixed Broughton/Cohn first row. That is a scoped negative. It may be recorded as such in a later freeze; this review does not write the ledger.
- EMPTY-TANGENT on `H_2` is the preregistered stop. The weight recurrence is the stronger, also preregistered, certificate for the same family. Neither licenses a second family.

---

## Priority caveats

1. Wright 1978 is prior art for the *biconditional* exact-coframe dichotomy on a full det-1 Jacobian. The one-way lemma used by the gate is Jung–van der Kulk plus Poincaré, also classical (cf. Drensky–Yu 2001, one-line remark). Do not claim literature novelty for either.
2. Wright's converse remains unread from the 1978 PDF in this session. The printed Shpilrain–Yu restatement of Theorem 6 is consistent with the producer audit and with the standard secondary statement. Until the 1978 text is read, do not treat `M ∈ E_2` as an automorphy certificate off that restatement.
3. Shpilrain–Yu Proposition 2.4's printed “furthermore” (arbitrary second row under a gradient first row in `GE_2` is itself a gradient) is false, counterexample `L(y)`. Do not cite Prop. 2.4 as Wright.
4. Cohn's obstruction is Prop. 7.3 in §7, not §8. Park Thm. 5.2.1 is the leading-term certificate, printed pages 52–53, as claimed.

---

## Explicit exclusions

Not reviewed except as named conflicts: any other shear; any right factor; any second left factor; any coordinate change; any degree or support cap beyond frozen `H_2`; generic sparse search; the full double orbit `E_2 C E_2` with unfixed first row; JC2; descendants; `x + x^m y`; length-two left elementary words; Mennicke symbols; quotient language `SL_2/E_2`; AUDIT/APPROACHES/PROGRESS/COORDINATION ledgers; books, D/Witt, TRACE, passports, HC4, Dixmier, GGV farm mathematics.

No canonical ledger was edited. No file other than this one was written.

---

## Final one-line record

Overall **CONFIRMED**: the one-way bridge holds, the Cohn/Park/`y ↦ 2y` lineage holds, the fixed-row family `L(h)C_B` is complete, the curl equation is `δh=6y`, the frozen `H_2` tangent is empty with an explicit unit certificate, every polynomial `h` is blocked by a nonterminating weight recurrence whose generating function is the displayed rational control, the scope is one-left-shear / fixed Broughton row, and the priority wording on Wright versus Shpilrain–Yu Prop. 2.4 is right. Smallest failing identity: none. Promotion: none.
