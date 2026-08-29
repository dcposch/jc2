# Hostile review: typed `G2-PSC` source-to-pole-tree interface

**Reviewer lane:** Opus 5, different-model hostile review
**Date:** 2026-08-27
**Target:** `xmodel/g2-psc-typed-source-to-pole-tree-interface-sol-ultra-20260827.md`
**Target SHA-256:** `4c3f2236a11f296f7eb194bb26e8cdc8ff0b91f10d8d7151e6314caa62629304` (rehashed; **matches**)

**Headline verdict:** **CONFIRMED WITH REPAIR.** The three-arrow separation
survives hostile audit and I reproduced every desk check and the whole
`8_28` collision from scratch. But four load-bearing atoms need repair, one
is **REFUTED**, one novelty claim is **REFUTED**, and the producer's own
statement of what is missing is *in the wrong place*: it under-states the
obstruction on one side and over-states it on the other.

- The ring map `theta_i` that the entire Section 3 diagram rests on is **not**
  in GGV5 Theorem 2.20's fourteen clauses. It exists — I found it — but in an
  **undeclared** external paper (Valqui–Guccione–Guccione, `arXiv:1401.1784`
  = GGV5's `[6]`, Prop. 5.17/5.18), which constructs the successor literally
  as `(phi(P),phi(Q))`.
- The "all roots" half of clause (4.1) is **already closed at the live
  `8_28` corner**: `p_0(z) = lambda (z^4 - alpha)^21` is a single deck orbit
  and every root satisfies VGG's side condition (5.9) with `m_lambda = 21 >= 4`.
  The producer over-states the open content there.
- The **second chart is not merely unreached; it is not expressible.** GGV's
  entire apparatus lives in `L^(l) = K[x^{+-1/l}, y]`, polynomial in `y`, with
  direction interval `I = ](1,-1),(1,0)]`. There is no `y = infinity` locus in
  that ring at any stage, and the campaign's own faithful port asserts `a < b`.
  This upgrades O2 from an observation to a structural impossibility and
  relocates the first genuinely missing theorem.
- `DPT_a` as specified in (2.11) **does not** contain the labels the later book
  machinery consumes. Sigray Statements 9.5/9.12 consume `lambda_F`, `M_F` and
  `Q(F)` along the whole *characteristic sequence* `F_0,...,F_n = (0,y)`, and
  `M_F` at a non-pole vertex needs the full approximate-root tower degrees.

Nothing here promotes `G2-PSC`, `G2-BD`, landing, cofinality, or JC2, and
nothing here weakens any promoted campaign result.

---

## 0. Method and what I refused to take on trust

I rehashed the producer, re-derived every displayed identity by hand, and
read the **primary sources directly** rather than the producer's prose:
Sigray's thesis text extracted from the pinned `refs/sigray_full.pdf`
(Statements 3.1–3.15, Notations 3.4–3.14, 5.1–5.3, 8.1, 9.1, Propositions
3.1, 4.2, 4.3, 5.3–5.7, Statements 9.5, 9.12), GGV5 Theorem 2.20 in full from
`arXiv:1708.07936v1`, and — because Theorem 2.20 turned out not to say what
the producer needs — GGV5's reference `[6]` from `arXiv:1401.1784v3`.

I re-ran all three desk checks, re-derived the `8_28` collision (boundary
census, residual, exact gcd, both pole masses) without using either the
producer's or Grok's numbers, and independently reproduced the campaign's
`8_28` final corner `(11/4, 7)` from GGV5's own equation (2.5).

I did not enter, list, read, build, status-inspect or modify `jc2-lean`, ran
no heavy local algebra, launched no AWS, and edited no canonical ledger or
other campaign artifact.

---

## 1. Section 1 — exact source types

### A1. Rotation (1.1) — **CONFIRMED**

`ladder/TRANSPORT.md:46` gives the source rotation as a map on points,
`R(x,y) = (y,-x)`. Its pullback on coordinate functions is `X |-> y`,
`Y |-> -x`, which is exactly the producer's (1.1). The Jacobian matrix of
`(x,y) |-> (y,-x)` is `[[0,1],[-1,0]]` with determinant `+1`, so
`[f,g] = [H,J]` with no scaling. Correct.

### A2. Component sort (1.2)–(1.3), `H = Q` for `8_28` — **CONFIRMED**

`TRANSPORT.md:31-41` gives `C(U,V) = (U,V)` if `m<n` and `(V,-U)` if `n<m`,
i.e. exactly (1.2). Antisymmetry gives `[Q,-P] = -[Q,P] = [P,Q] = c`, so the
producer's `[H,J] = c` is right.

Running the frozen library (`lib/families.py`, SHA matches):

```text
8_28: fields=16, mn=(3,2), degP=108, degQ=72
cases/transport_check.py: ggv_degrees (108,72) -> sigray_degrees (72,108), type (2,3)
```

`n = 2 < 3 = m`, so `H = Q`, `J = -P`. (1.3) is correct.

### A3. Fibre algebra (1.4)–(1.5) — **CONFIRMED** (one type nit)

The smoothness argument is right and worth stating explicitly, since the
producer compresses it: if `f_x = f_y = 0` at a point then `[f,g] = 0 != c`
there, so `(f_x,f_y)` never vanishes and every fibre `C_a` is smooth, hence
reduced. `f` is then nonconstant, so `C_a` is a nonempty curve for every `a`.

Nit: if `C_a` is reducible then `B_a` is not a domain and `iota_S` in (1.5) is
not injective; it is still a well-defined ring map (restrict to the component
carrying `S`). Calling it an "exact evaluation map" is fine; calling it an
embedding would not be.

### A4. Coefficient-complete witness (1.6)–(1.11) — **CONFIRMED WITH REPAIR**

Verbatim against `arXiv:1708.07936v1`:

| producer | GGV5 primary | verdict |
|---|---|---|
| (1.6) `L_i = K[X^{1/l_i},X^{-1/l_i},Y]` | `[6]`: `L^(l) := K[x^{+-1/l}, y]` | exact |
| (1.8) `l_{i+1} = lcm(l_i,rho_i)`, `Z_i = X^{-sigma_i/rho_i}Y` | Thm 2.20 **item (8)**, verbatim | exact |
| (1.9) `l_{rho_i,sigma_i}(P_i) = X^{k_i/l_i} p_i(Z_i)` | item (8), verbatim | exact |
| (1.10) `phi_i(X^{1/l_{i+1}}) = X^{1/l_{i+1}}`, `phi_i(Y) = Y + lambda_i X^{sigma_i/rho_i}` | item (8), verbatim | exact |
| "type-II.a transition is the identity" | item **(7)**: `l_{i+1}=l_i`, `(P_{i+1},Q_{i+1})=(P_i,Q_i)` | exact |
| "fourteen clauses" | items (1)–(14) | exact |

**REPAIR 1 (undeclared dependency, load-bearing).** (1.7) — the cumulative
homomorphism `theta_i : A -> L_i` with `theta_i(P) = P_i`, `theta_i(Q) = Q_i` —
is **not** among Theorem 2.20's fourteen clauses. Item (8) asserts only a
*leading-form* relation,

```text
l_{rho_i,sigma_i}(P_{i+1}) = phi(l_{rho_i,sigma_i}(P_i)),
```

and items (3)/(4) only that `(P_i,Q_i)` is an `(m,n)`-pair in `L^(l_i)` with
matching earlier leading forms. The proof of Theorem 2.20 obtains
`(P_{t+1},Q_{t+1})` by *citing* `[6]*Proposition 5.18 and Remark 3.9`.

I fetched `[6]` (Valqui–Guccione–Guccione, *On the shape of possible
counterexamples to the Jacobian Conjecture*, J. Algebra **471** (2017)
13–74 = `arXiv:1401.1784v3`) and read Proposition 5.18. It **does** supply
what the producer needs, and more cleanly than Theorem 2.20 states it: the
successor pair is literally `(phi(P), phi(Q))`, with

```text
phi in Aut(L^(l')),  l' := lcm(rho,l),
phi(x^{1/l'}) := x^{1/l'},   phi(y) := y + lambda x^{sigma/rho},
A^(1) := (1/m) st_{rho,sigma}(phi(P)).
```

So `theta_i = phi_{i-1} o ... o phi_0` (with the Kummer inclusions) exists and
is exactly the producer's (1.7). **Verdict: (1.7) is true, but its source is
an external paper absent from the producer's Section 9 dependency list.**
The producer's Section 9 sentence "GGV5 Theorem 2.20 and its fourteen clauses
were checked ... item 8 explicitly has ..." is accurate as far as it goes, and
its silence about `[6]` is the defect.

**REPAIR 2 (dropped side conditions).** (1.9)–(1.10) describe `lambda_i` only
as "a selected nonzero root of the exact face polynomial". GGV5 item (8) and
VGG Prop. 5.18 impose more: `lambda in K^x`, `#factors(p_i) > 1`,
`m | m_lambda`, and the multiplicity bound

```text
(5.9)   m_lambda >= (m/l) * (a*rho + b*l*sigma) / (rho + sigma).
```

This matters for clause (4.1) — see §5 below — and must be in any typed
source contract, because a "root" failing (5.9) has no GGV successor pair at
all.

### A5. Residual polynomial (1.11) — **CONFIRMED**

The term-by-term justification is correct: on the face
`rho_i r + sigma_i s = v_i(E)` and `X^r Y^s = X^{r - u_i s} Z_i^s`, so the
`X`-exponent is constant `= v_i(E)/rho_i` and the residual is a genuine
polynomial in `Z_i`. Uniqueness is immediate.

---

## 2. Section 2 — the exact target type

### B1. Two-chart split (2.1) — **CONFIRMED WITH REPAIR**

Sigray's Statement 3.1 (thesis p. 10) reads, verbatim:

> *The normalized counterexamples of the Jacobian conjecture have an important
> property.* **Statement 3.1.** Set `P in R̄_a \ R_a`. Then exactly one of the
> following two properties holds: (i) `x(P) = infinity` and `y(P) in C`,
> moreover `y = sum_{j>=0} c_j x^{-j/kappa}` ...; (ii) `y(P) = infinity` and
> `x(P) in C`, moreover `x = sum_{j>=0} c_j y^{-j/kappa}`.

The dichotomy is therefore **a property of normalized counterexamples**, not a
Newton–Puiseux generality. The producer's Theorem 2.1 asserts it for
`(K,P,Q,c,m,n,a)` with the displayed hypotheses `[P,Q] = c`,
`mult(P,Q) = (m,n)`, `gcd(m,n) = 1`, `m,n > 1` — which do **not** imply it:
`(f,g) = (x + y^2, y)` is Keller with `[f,g] = 1`, and the unique place at
infinity of `x = a - y^2` has `x = y = infinity`.

**Repair (supplied, four lines).** The needed hypothesis is Sigray Lemma
2.1(i), which `TRANSPORT.md:23-29` already imposes by reference
(`Supp P subset [0,ma]x[0,mb]` with the northeast corner occurring). Then:
let `S` be a place with `ord_S(x) = -p < 0` and `ord_S(y) = -q < 0`. For
`(i,j) in Supp f subset [0,k_f]x[0,l_f]` we have `pi + qj <= p k_f + q l_f`
with equality only at `(k_f,l_f)`, whose coefficient is nonzero because
`f^+_{(1,1)} = x^{k_f} y^{l_f}`. Hence `ord_S(f) = -(p k_f + q l_f) < 0`,
contradicting `f == a` on the fibre. **QED.**

So (2.1) is true for the producer's intended class, but Theorem 2.1's
displayed hypothesis list must add the rectangle/NE-corner condition, and the
dichotomy must be cited as a lemma rather than folded into "standard
Newton–Puiseux theory".

### B2. Puiseux presentations (2.2) — **CONFIRMED.** Exactly Sigray's forms (3) and (4).

### B3. Contact and tree (2.3) — **CONFIRMED WITH REPAIR**

`(S,u) ~ (T,u) iff u <= O(S,T)` is Sigray Definition 3.3 exactly, and the
vertex description matches Definition 3.4 (`V_a = V_{1,a} u V_{2,a} u
(0,x) u (0,y)`). Sigray Statement 3.3 gives the two components.

**Repair.** The producer defines `O(S,T)` as "the first exponent at which two
Puiseux series differ". Sigray Definition 3.2 defines it as the **maximum**
over corresponding presentations, and Definition 3.3 is an equivalence only
through Statement 3.2's coherent `Omega` — which `ladder/SIGRAY-AUDIT.md`
records as `VERIFIED_WITH_NIT` with **no printed proof** ("false for general
series sets"; re-derived in the campaign audit). The producer's (2.3) silently
consumes a campaign-repaired statement without declaring it.

### B4. `kappa_F`, `nu_F`, Q/jump/max (2.4) — **CONFIRMED** (one mis-scoping)

- Sigray Notation 3.5: `kappa_F := kappa/e_j` where `alpha_j <= u < alpha_{j+1}` —
  matches the producer's prose exactly (`alpha_j = beta_j/kappa`).
- Sigray Notation 3.4: `nu_F := e_{j-1}/e_j` at a characteristic jump, else 1 —
  matches exactly.
- `SIGRAY-AUDIT.md` Not 3.5: `GAP`, "`kappa_F` NOT well-defined as printed",
  forced repair = "jump-realization/max (Eggers–Wall) value"; St 3.8:
  `ERRATUM`, "only the jump/max `kappa_F` reading makes St 3.8 true".
- `xmodel/sol-h5a.md:271`: "At `F`, Notation 3.5 gives `kappa_F(P)=1` and
  `kappa_F(Q)=3`." The producer's citation is **exact**, and line 643 records
  "Q/jump/max is the unique uniform global repair of `kappa_F` | **PROVED**".

**Mis-scoping (harmless).** (2.4) presents `nu_F` as "the corresponding jump
ratio" of the maximising presentation, i.e. as convention-dependent.
`SIGRAY-AUDIT.md` Not 3.4 records the opposite as proved: "`nu_F`
P-independence PROVED here ... H5a does NOT infect `nu_F`". The values agree;
the typing suggests a dependence that the campaign has closed.

Also: the identification of the displayed max in (2.4) with the prose "choose
a *jump* presentation attaining the maximum denominator" is exactly Sigray
Notation 3.11's canonical reading plus the campaign's `(Q,j)`-independence
result. The producer uses both phrasings interchangeably without citing what
makes them the same.

### B5. `eta_F`, `d/p`, `D`, `kappa-bar` (2.5)–(2.7) — **CONFIRMED**

- (2.5) is Sigray Notation 3.9 verbatim (`eta_F := x^{pi(F)}(y - sum_{j<pi(F)} c_j x^{-j})`),
  and the producer's "common truncation below `u`" is a correct and clearer
  gloss, since all series through `F` agree strictly below `u`.
- (2.6) is Notation 3.10 (`h^+_F = xi^{j/kappa} p_j(eta)` with `j` maximal;
  `d_{h,F} := j/kappa`, `p_{h,F} := p_j`).
- `D_{h,F} = kappa_F d_{h,F} in Z` is Notation 3.11 + Statement 3.8.
- `kappa-bar_F = kappa_F(1-u)` is the **fifth slot of Sigray's Notation 9.1**
  `Q(F) := (D_F, deg(p_F), nu_F, M_F, kappa_F(1-pi(F)))`. Correct, and
  Statement 9.1 gives `D_F + D_{g,F} = kappa-bar_F` at pole vertices.

### B6. Fibre selector (2.8) — **CONFIRMED, with a proof the producer omits**

Retaining `p_{f-a,F}` *and* `p_{f,F}` is right: Sigray Notation 3.13 prints
`p_F := p_{f,F}`, while `SIGRAY-AUDIT.md` records the load-bearing repair
`p_F = p_{f-a,F}` (St 3.13 `ERRATUM`, false as printed for `a != 0`).

The producer then uses `p_{f,F}` in (2.12) without comment. **This is safe,
and here is why:** on `T_a^+` we have `d_{f-a,F} > 0`, and `f = (f-a) + a`
adds only a constant, at `xi`-exponent `0 < d_{f-a,F}`; hence
`d_{f,F} = d_{f-a,F}` and `p_{f,F} = p_{f-a,F}` throughout `T_a^+`, and
`T_{a,pole} subset T_a^+`. Sigray's own proof of Statement 3.14 uses the same
step. The producer should say this rather than leave an apparent conflict with
its own (2.8).

### B7. Approximate-root tower (2.9)–(2.10) — **CONFIRMED WITH REPAIR**

Sigray Proposition 4.2, items (i)–(iii), verbatim:
`gcd(k_j,l_j) = 1`; `h_{j+1} = h_j^{k_j} - s_j f^{l_j}`;
`(h^+_{j,F})^{k_j} = s_j (f^+_F)^{l_j}`; `h_0 = g`. Exact match.

**Repair 3.** Two omissions, both inside the producer's own declared perimeter:

1. Proposition 4.2 is stated for `F in T_a^+` only. The `T_a^-` tower
   (Proposition 4.3: `h_0 = g - b`, `h_{j+1} = h_j^{k_j} - s_j (f-a)^{l_j}`,
   with `b` satisfying (7)) is not in (2.9)–(2.10). A forest that spans from
   the roots to the pole vertices passes through `T_a^0` and can meet
   `T_a^-`; the producer's own (2.8) anticipates this and then (2.9) drops it.
2. `SIGRAY-AUDIT.md` files Proposition 4.2 as a **`GAP`**: "'since `h_j` is
   non-constant, `l_j != 0`' conflates `h_j` with its leading part: if
   `h^+_{j,F} in C^*` ... the tower is stuck (`l_j = 0 not in N^*`)". Theorem
   2.1's uniqueness claim covers `(h_j,k_j,l_j,s_j)_j`, the pole thresholds and
   (2.12), all of which inherit that gap. The status line "EXACT relative to
   ... the campaign's reviewed corrections to Sigray's definitions" does not
   cover it, because this is an unrepaired existence gap in a *proposition*,
   not a definition correction.

### B8. Pole-vertex decorations (2.11)–(2.12) — **SPLIT VERDICT**

- `M_F = gcd(deg p_{f,F}, deg p_{g,F})` — **CONFIRMED at pole vertices.**
  Sigray Notation 8.1 defines
  `M_F := gcd(deg p_F, deg p_{h_0,F}, ..., deg p_{h_m,F})` with `m = m_F`. At
  `F in T_{a,pole}` we have `m_F = 0` (Notation 5.1/5.2) and `h_0 = g`, so the
  definition collapses to exactly the producer's two-term gcd. Correct, but it
  is a *consequence of `m_F = 0`*, not the definition, and the producer states
  it as if it were general.
- `Lambda(F) = D_{g,F} deg p_{f,F} / nu_F` — **CONFIRMED.** Sigray Proposition
  5.6 (19): `Lambda(F) := D_{g,F} deg(p_F)/nu_F = sum_P Lambda(P)`, with
  `p_F = p_{f,F} = p_{f-a,F}` on `T_a^+` by B6.
- **"This target contains the labels consumed by the later book machinery" —
  REFUTED as stated.** Sigray Statement 9.5 requires
  `sum_{i=1}^{n} lambda_{F_i} <= td(f,g) - 2` over the **characteristic
  sequence** `F_0, F_1, ..., F_n = (0,y)` of a pole vertex, and Statement 9.12
  (the engine of Theorem 9.1, `td >= 6`) argues that "either the
  characteristic sequence has an element `F_j` with `M_{F_j} = 1`, or (26)
  does not hold". Notation 9.1 defines `Q(F)` on `V_a u T_a^+`, not on
  `T_{a,pole}`. So `Q(F)`, `M_F` and `lambda_F` are consumed at **every vertex
  of the ancestor path**, and at a non-pole vertex `m_F > 0`, so `M_F`
  genuinely needs `deg p_{h_j,F}` for `j = 0..m_F`. The producer's (2.11)
  requires its list only "at a pole vertex".

  **Repair 4 (required):** (2.11) must be demanded at every vertex of the
  pole-spanned forest, and the tower-degree list `deg p_{h_j,F}` must be
  retained at non-pole vertices.

### B9. Theorem 2.1 (exact pair constructor) — **CONFIRMED WITH REPAIR**

The construction is correct and the proof sketch is sound: (1.1)–(1.4) fix the
fibre algebra; normalization gives `B_a` intrinsically; Newton–Puiseux over
`K = K-bar`, `char 0` gives all expansions; conjugates are deck orbits;
substitution evaluates all residuals; `t_S`-reparametrisation invariance and
the deck quotient give canonicity. Repairs: add the rectangle hypothesis (B1),
carry the `T_a^-` tower (B7.1), and downgrade "EXACT" to "exact modulo the
campaign's own filed Sigray Prop. 4.2 `GAP`" (B7.2). The producer's refusal to
call this `G2-PSC` is correct and important.

---

## 3. Section 3 — the local flag transport

### C1. Ring diagram (3.1)–(3.3) — **CONFIRMED WITH REPAIR**

The diagram is well-formed and `beta_i = beta_{i+1} o phi_i` is the right
compatibility. Two hidden assumptions must be surfaced:

**Hidden assumption 1 (resolved in the producer's favour).** `theta_i` exists —
see A4/REPAIR 1. Without VGG Prop. 5.18 the domain `L_i/(theta_i(H)-a)` of
(3.2) is not even defined.

**Hidden assumption 2 (the `P`-vs-`H` root mismatch).** GGV's chain, its
corners, its face polynomial `p_i` and its selected root `lambda_i` all belong
to `P`, whereas (3.2) quotients by `theta_i(H) - a` with `H = Q` when `n < m`
(the `8_28` case). A root of the `P`-face has no a priori reason to name a
branch of `{H = a}`. This is rescued — but only by an unstated theorem: VGG
Theorem 7.6(2) gives, at a type-II regular corner,
`l_{rho_j,sigma_j}(P) = R_j^{m d_j}` for a homogeneous `R_j`, and the type-II
hypothesis `[l(P), l(Q)] = 0` forces the two faces to be proportional powers
of the same `R_j`. Hence the `P`-face and `Q`-face have the **same** root set,
with multiplicities in ratio `m : n`. Any typed contract must record this.

### C2. Inverse substitution (3.4) — **CONFIRMED.** `x = -Y`, `y = X` is the exact inverse of (1.1).

### C3. `eta_F = -Z_i` (3.5) — **CONFIRMED WITH REPAIR**

I re-derived it. The native `{X = infinity, Y finite}` sector maps under
`X = y`, `Y = -x` to Sigray's `{y = infinity, x finite}` component
`B_{a,x}` — so the correct formula is the *x*-side one,
`eta_F = y^{u}(x - s_F(y))`. Substituting `y = X`, `x = -Y` gives

```text
eta_F = X^u(-Y - s_F(X)) = -(X^u Y) - X^u s_F(X) = -Z_i - X^{u_i} s_F(X),
```

so `eta_F = -Z_i` exactly when the truncation is absorbed. The height is right:
`Y ~ lambda_i X^{sigma_i/rho_i}` matches `x ~ c y^{-u}` iff
`u = -sigma_i/rho_i = u_i`, and `u_i >= 0` is forced because GGV's direction
interval is `I = ](1,-1),(1,0)]` (`rho > 0`, `sigma <= 0`), so
`u_i in Q_+ = [0,1)`, inside Sigray's `Q_+`. The producer's orientation and
sign are **correct**; its Section 10 contingency for a sign error is not
needed.

**Repair 5 (name the hypothesis).** The clause "after the earlier cuts have
been absorbed into `theta_i`" is an *assumption*, not a consequence of
(3.2)–(3.3). Unrolling `beta_i = beta_{i+1} o phi_i` gives
`beta_0(Y) = sum_{j<i} lambda_j X^{sigma_j/rho_j} + beta_i(Y)`, so what
`theta_i` absorbs is precisely the GGV translation sum. Sigray's `s_F` is the
truncation of the **actual** branch series below `u_i`. Equality of the two is
the statement that the GGV chain's type-II.b steps enumerate the branch's
successive nonzero Puiseux terms with nothing hidden in the type-II.a
(identity) steps. If any intermediate term were skipped, the discarded terms
would have exponent `> -u_i` and `y^{u_i}`-scaling would make them blow up,
breaking (3.6). Call this **H-TRUNC**; it belongs in Prop. 3.1's hypothesis
list, not in a subordinate clause.

### C4. Residual identities (3.6) — **CONFIRMED**

Term-by-term: the `(rho_i,sigma_i)`-top face is the top power of `X = y`
(monomials `X^r Y^s |-> X^{v_i/rho_i} Z_i^s`), so matching
`X^{d} r(Z_i)` against Sigray's `y^{d_{h,F}} p_{h,F}(eta)` with `Z_i = -eta`
gives `d_{f,F_i} = d_{theta_i(H),i}` and `p_{f,F_i}(eta) = r_{theta_i(H),i}(-eta)`,
and likewise for `J`. Exactly (3.6). The hedge "up to the recorded target
sign" is precisely the `Z_i = -eta` sign, correctly flagged.

The caveat sentence — "On the positive-weight segment the constant `a` does
not change the leading face; outside it, the packet must separately retain
`r_{theta_i(H)-a,i}`" — is correct and is the same fact I proved in B6.

### C5. Proposition 3.1 — **CONFIRMED as conditional**

The statement is honest and its disclaimer paragraph ("It does not assert that
the occurrence exists for the sorted fibre component at every primary selected
root, that all roots were selected, that the other chart was run, or that
every pole threshold was reached") is exactly right. Its hypothesis list must
additionally carry **H-TRUNC** (C3), the **`P`/`Q` face-root identification**
(C1), and the **`theta_i` existence citation** (A4).

---

## 4. Section 5 — the obstructions

### O0. `CornerData` is not a source object — **CONFIRMED, exactly**

Direct introspection of the frozen library:

```text
CornerData._fields (16): name A0 A0p chain final steps k family mn j
                         degP degQ S c upper_dir rhs_exp
has_exact_pair=False  has_fibre=False  has_face_root=False  has_ring_map=False
Corner=(a,l,b)  Edge=(A,Ap)  Chain=(edges,final)  Family=(k,i,m0,n0,d1,d2)
```

The *transitive closure* is pure integer/`Fraction` lattice data — there is no
coefficient anywhere, in any nested field. The producer's claim is not merely
about the top-level record and is fully correct. This is a schema
obstruction, exactly as characterised.

### O1. Ambient nonfunction — **CONFIRMED** (conclusion) **WITH REPAIR** (frame/letters)

I re-derived the whole collision independently.

*Boundary census.* For `B = x(xy^4-1)^7`, `f = B^2 - x - y^8` (`deg f = 72`):

- `y -> infinity`: put `x ~ c y^{-3}`; then `xy^4 ~ cy`, `B ~ x(cy)^7 = c^8 y^4`,
  `B^2 ~ c^16 y^8`, so `f` is bounded iff `c^16 = 1`. **16 places, kappa = 1**,
  `ord(y) = -1`, `ord(x) = +3`.
- `x -> infinity`: `xy^4 -> 1`; writing `w = xy^4 - 1 ~ eps x^{-1/14}`,
  `B = xw^7 ~ x^{1/2}`. **2 places, kappa = 28**, `ord(x) = -28`, `ord(y) = +7`.
- Check: `16*1 + 2*28 = 72 = deg f`. The census closes exactly.

*Residual and pole orders.* On the 16 places,
`B^3 ~ c^24 y^12 = c^8 y^12` (using `c^16 = 1`), `y^12` contributes `1`,
`tau x y^15 ~ tau c y^12`, and `2x^2y^2 ~ 2c^2 y^{-4} -> 0`. The `y^12`
coefficient is therefore

```text
R_tau(c) = c^8 + 1 + tau*c,   c^16 = 1,      R_tau(-1) = 2 - tau.
```

Exact polynomial gcd over `Q`:

```text
gcd(C^16-1, C^8+1+1*C) = 1        -> all 16 places keep pole order 12
gcd(C^16-1, C^8+1+2*C) = C+1      -> exactly one place drops 12 -> 11
```

On the 2 places, `B^3` and `2x^2y^2` both have `x`-exponent `3/2`, so
`ord = -28*(3/2) = -42`, and both are `tau`-independent. Masses:
`2*42 + 16*12 = 276` and `2*42 + 15*12 + 11 = 275`. **Every number in O1 and
in (7.1) is confirmed from scratch**, and matches the canonical record
`AUDIT.md:900-914` ("72 sheets, two ramification-28 plus sixteen unramified
places ... 276 -> 275") and the frozen Grok review.

*Does it prove ambient nonfunction, or only a normalization/fibre mismatch?*
**It proves nonfunction.** `f` is literally identical across the two controls
and the fibre `a` is the same, so there is no normalization or fibre freedom
to blame: the tree `T_a` is the same object, and only a decoration changes.
The separating datum is the coefficient of a single monomial `x y^15` that is
off the initial face and invisible to every field of `CornerData`. Hence no
map factoring through the discrete Newton/chain ledger can be a function on
the ambient polynomial class. The producer's own scope note — "These controls
are not Keller, so this does not refute a Keller-restricted theorem" — is
correct and is corroborated by the canonical non-Keller witness
`Jac(f,g_1)|_{x=0} = -12y^11 + 8y^22`.

**Repair 6 (frame/letters, mandatory).** The O1 display violates the
producer's own Section 1 conventions:

- Section 1.1 declares "Keep native GGV variables capitalized", yet O1 writes
  the pair in lowercase `x,y` as `f, g_tau`.
- Read **literally as Sigray-frame** `f`, the Newton polygon of `B^2` has
  `(k_f,l_f) = (16,56)`, so `l_f > k_f`, contradicting Sigray Lemma 2.1(iii)
  (`l_f <= k_f`). It is therefore *not* a Sigray-normalized pair.
- `TRANSPORT.md:512-522` settles it: for `8_28`, `2S` has corner `(16,56)` and
  "after the component and source rotations the Sigray corners are
  `(56,16) = 2(28,8)`". The O1 display is in **native GGV coordinates**.
- (1.2) also requires `J = -P`, so the paired component should carry a sign;
  O1 writes `g_tau = B^3 - ...` unsigned, dropping the very sort bit Section
  1.1 calls load-bearing.

None of this changes the conclusion (the rotation is a determinant-one linear
automorphism, so places, pole orders and masses are preserved), and the
"second chart" attribution is **correct under the native reading**: the native
`{X = infinity, Y finite}` sector is the 2-place side, which the mutation does
not touch, while the 16 changed places are native `y = infinity`, i.e.
Sigray's `B_{a,y}` — the chart GGV never enters. But the display must be
relabelled `(P,Q)` or explicitly declared native.

### O2. One-chain trace — **CONFIRMED AND STRENGTHENED**

GGV5 Theorem 2.20 item (8) asserts only "*there exists a root* `lambda in K^x`
of `p_i(z)` such that `m | m_lambda`". So the "selected root" reading is exact.

The chart half is **much stronger than the producer states**, and I can prove
it structurally rather than observationally:

1. GGV's ambient ring is `L^(l) = K[x^{+-1/l}, y]` (`[6]`, §2) — Laurent in
   `x`, **polynomial in `y`**. There is no `y = infinity` locus in the ring at
   any stage `i`.
2. The direction interval is `I := ](1,-1),(1,0)]` (GGV5 §2), so every
   `(rho_i,sigma_i)` has `rho_i > 0`, `sigma_i <= 0`, i.e.
   `u_i = -sigma_i/rho_i in [0,1)`; every occurrence has `X -> infinity` with
   `Y ~ lambda_i X^{-u_i}` bounded.
3. The campaign's faithful port asserts `a < b` at chain start
   (`lib/families.py:156`), which is GGV standard orientation; the transposed
   corner `(28,8)` is not an admissible input.

**Conclusion:** the second Sigray chart is not "unreached by a linear chain" —
it is **not expressible** in GGV's source category. No enrichment of a chain,
no factor expansion, and no all-root refinement can produce it. This is a
strictly stronger statement than the producer's O2 and it relocates the first
missing theorem (§6).

### O3. One presentation does not determine Q/jump/max — **CONFIRMED**

Corroborated at two independent points: `SIGRAY-AUDIT.md` St 3.8 `ERRATUM`
("`D in Z` FALSE under Not 3.5's P-presentation ... only the jump/max
`kappa_F` reading makes St 3.8 true") and `sol-h5a.md:274-276`
(`(D_F,kappa-bar_F)_P = (4/3, 2/3)` nonintegral versus `(4,2)` integral). The
producer's warning that `kappa_F = l_i` (or `l_{i+1}`) is not a valid global
label is correct: `l_i` is an ambient Kummer denominator of the *pair's*
lattice, whereas `kappa_F` is a per-place ramification datum quotiented by the
deck stabiliser.

### O4. Post-Laurent endpoints — **CONFIRMED.** Corroborated verbatim by the canonical `ladder/REDUCTION.md` CRITICAL 3: "Proposition 4.3 lands at `[P,Q] = x^2`, whereas Sigray assumes a constant-Jacobian polynomial pair; those later records remain metadata, not polynomial Sigray inputs."

### Section 6 failed-shortcut table — **CONFIRMED** on all eight rows. The `use only native P` row is verified by A2; the symplectic-residue row is corroborated by `sol-landing1.md` §2.4/§4.5.

---

## 5. Section 4 — the proposed contract

### D1. `ARF_a(P,Q)` items 1–7: sufficient? — **CONFIRMED (sufficient), NOT minimal**

The producer explicitly disclaims minimality ("**sufficient**, not claimed
collision-minimal"), and that disclaimer is faithful to the canonical record:
`AUDIT.md:916` says "Only the `y` residual/root/pole vector and `x*y^15`
provenance are forced by this collision; the other packet fields are merely
sufficient". I confirm non-minimality independently: item 3's "its inverse on
the function field" is recoverable from item 1 plus the forward map, and item
5's intrinsic flag/Enriques IDs are computable from items 1–4 by Theorem 2.1 —
they are gluing conveniences, not information.

**Missing field (from B8):** the tower degrees `deg p_{h_j,F}` at non-pole
vertices, required by `M_F` along the characteristic sequence.

### D2. Theorem 4.1 (forest compiler) — **CONFIRMED, but near-tautological**

The statement is true, and the schema/theorem separation the producer claims
is **not clean**: item 7 is not a schema field at all, it is a *certificate of
the coverage theorem*. Once "every boundary branch orbit has been emitted and
expanded through all characteristic and contact vertices needed to decide its
`g` order and tower threshold" is assumed, Theorem 4.1 is Theorem 2.1 with the
answer supplied. The producer half-acknowledges this. The honest reading is:
items 1–6 are the schema; item 7 *is* clause (4.1); Theorem 4.1 is the
observation that nothing else is needed. That is worth stating, not worth
labelling **EXACT** at the same tier as Theorem 2.1. Theorem 4.1 also inherits
the Prop. 4.2 `GAP` (B7.2).

### D3. Scoped conjecture and clauses (4.1)–(4.3) — **CONFIRMED WITH REPAIR**

Three findings, in order of importance:

**(a) (4.1)'s "all roots" half is already closed at the live `8_28` corner.**
I checked VGG's side condition at the live stage-0 datum
`A_0 = (8,28)`, `l = 1`, `(rho,sigma) = (4,-1)`, `m = 3`:

```text
(5.9) bound:  (m/l)*(a*rho + b*l*sigma)/(rho+sigma) = 3*(32-28)/3 = 4
face:   l_{4,-1}(P) = lambda_P * x^3 * (z^4 - alpha)^21,  z = x^{1/4} y
        (since xy^4 = z^4), so every root has m_lambda = 21
21 >= 4 (5.9 holds),  3 | 21 (m | m_lambda holds),  #factors = 4 > 1
```

and, as a cross-check that this really is the live record, GGV5's own equation
(2.5) then gives

```text
A_1 = (k/(m l), 0) + (m_lambda/m)(-sigma/rho, 1)
    = (3/3, 0) + 7*(1/4, 1) = (11/4, 7)          [campaign 8_28 final corner]
gamma = m_lambda/m = 7                            [campaign gamma = 7]
```

So at `8_28` the four roots of `p_0` form a **single deck orbit** (`z^4 =
alpha`) and every one of them is GGV-admissible. The producer's clause (4.1)
therefore over-states the open content at the live case: its root half is
already satisfied there, and what remains open at `8_28` is exactly **the
second chart and pole-path reachability**.

**(b) (4.1)'s "all roots" half is nonetheless not vacuous in general**, and
the producer's phrasing hides why. VGG Prop. 5.18's hypotheses `(5.9)` and
`#factors(p_i) > 1` are not bookkeeping: at a root with `m_lambda` below the
bound there is **no GGV successor `(m,n)`-pair at all**, so "run the chain at
every root" is not a defined operation in GGV's theory. Any typed contract must
either carry (5.9) as a field or carry a theorem that it always holds.

**(c) The clause list is missing its first entry.** (4.1)–(4.3) presuppose the
second chart is *expressible*. By O2-strengthened it is not. A repaired clause
list must begin:

```text
(4.0)  a source theory for the transposed pair exists at all.
```

### D4. Does the producer miss a theorem that recovers roots/chart/coverage? — **partly**

- **All roots:** partly recovered — see D3(a); GGV supplies them at `8_28`.
- **Ring map / source-map fidelity:** recovered, by VGG Prop. 5.17/5.18 (A4).
- **`P`/`Q` face-root identification:** recovered, by VGG Thm 7.6(2) (C1).
- **Second chart:** **not** recovered, and provably not recoverable inside
  GGV's category (O2-strengthened).
- **Corrected denominator maxima:** not recovered; `l_i` is a pair-lattice
  index, `kappa_F` a per-place ramification datum (O3). No GGV statement
  bridges them.
- **Paired residuals:** recovered locally by (3.6) once `theta_i` is present.
- **Coverage / pole-path reachability:** not recovered; nothing in GGV5 §2
  speaks about pole thresholds.

---

## 6. The shortest corrected typed contract

Replacing the producer's items 1–7:

```text
SOURCE(a) :=
  S0  PairRef(P,Q) in K[X,Y]^2 with [P,Q]=c in K^*, mult (m,n) coprime, m,n>1,
      Supp P subset [0,ma]x[0,mb] with the NE corner mA occurring  (and n for Q);
      the component-sort bit and its sign, giving (H,J) and (f,g)=r^*(H,J);
      the fibre value a.
  S1  chart in {native, transposed}.                    <-- new, forced by O2
  S2  per stage i: (rho_i,sigma_i), l_i, the FULL face polynomial p_i with
      coefficients and factor multiplicities, EVERY root orbit lambda, each
      tagged with m_lambda and the VGG (5.9) admissibility flag,
      and the paired Q-face witness R_i with l(P_i)=R_i^{m d_i}.
  S3  the cumulative map theta_i : K[X,Y] -> L^(l_i) as an explicit composite
      of phi_j's and Kummer inclusions, plus its inverse on the function field
      [existence: VGG arXiv:1401.1784 Prop. 5.17/5.18, NOT GGV5 Thm 2.20].
  S4  H-TRUNC: a certificate that sum_{j<i} lambda_j X^{sigma_j/rho_j} equals
      Sigray's truncation s_F strictly below u_i.
  S5  the deck stabiliser at each node (for reduced presentation denominators)
      and an intrinsic rank-two flag ID for gluing duplicate presentations.
  S6  a fail-closed coverage certificate: every boundary place orbit of
      {f=a}, in BOTH charts, emitted and expanded through every characteristic
      and contact vertex on its path to its tower threshold.

TARGET :=
  DPT_a(f,g), the two-component pole-spanned decorated forest, carrying at
  EVERY vertex of the forest (not only pole vertices):
      (u, kappa_F, nu_F, D_{f,F}, D_{g,F}, p_{f-a,F}, p_{f,F}, p_{g,F},
       deg p_{f,F}, deg p_{g,F}, (h_j,k_j,l_j,s_j)_{j<=m_F},
       {deg p_{h_j,F}}_{j=0..m_F}, M_F, Lambda(F), kappa-bar_F),
  plus chart, parent/child, contact data and deck action,
  with kappa_F/nu_F under the reviewed Q/jump/max repair,
  with T_a^+ / T_a^0 / T_a^- typed and the Prop. 4.3 tower used on T_a^-.

CONTRACT:  Theorem 2.1 factors through SOURCE(a); S6 is the theorem, S0-S5 is
           the schema.  Everything downstream of the tower is conditional on
           the campaign's open Sigray Prop. 4.2 gap.
```

Changes versus the producer: S1 and S2's (5.9)/`R_i` fields are new; S3 gains
its true citation; S4 is promoted from a parenthetical to a field; the target
decorations are demanded at every vertex, with the tower degrees; the `T_a^-`
tower is typed.

---

## 7. The first genuinely missing theorem

Not `theta_i` (it exists), and not "all roots" (closed at `8_28`). It is:

> **T-transpose (second-source theorem).** There is a GGV-type source theory
> for the transposed pair `(P^t, Q^t)`, `P^t(x,y) := P(y,x)`, producing
> complete chains whose occurrences name the boundary places of `{f = a}` in
> Sigray's *other* infinity chart, together with a gluing statement
> identifying the two runs' outputs at the tree roots `(0,x)`, `(0,y)`.

It is first because it is a **category** obligation, not a coverage
obligation: GGV's ring `K[x^{+-1/l},y]` has no `y = infinity` locus and its
direction interval is `I = ](1,-1),(1,0)]`, so no enrichment of the existing
chain can reach the second chart; and the campaign's own faithful GGV port
refuses `a > b` inputs (`lib/families.py:156`). The `8_28` collision lives
*exactly* in that chart, so T-transpose is precisely what the collision forces.

Second missing theorem: **pole-path reachability** (that every Sigray pole
threshold on either chart is reached by some GGV-eligible occurrence) — this
is the producer's (4.1) residue and `sol-landing1.md`'s PSC, correctly
identified and correctly attributed.

Third: a bridge from the pair-lattice index `l_i` to the per-place `kappa_F`
under the Q/jump/max repair (O3), needed before any `Q(F)` slot can be
emitted from source data.

---

## 8. What may be promoted

**Promotable now (as typed, scoped statements — no `G2-PSC` content):**

1. **A2/A4/A5** — the exact source typing (1.1)–(1.6), (1.8)–(1.11), with
   REPAIR 1's citation added.
2. **B1 with the supplied proof** — the two-chart dichotomy follows from
   Sigray Lemma 2.1(i) by a four-line valuation argument; this is a small
   genuinely new lemma and removes the "normalized counterexample" hypothesis
   in favour of the rectangle/NE-corner condition the campaign already has.
3. **C2/C3/C4** — the orientation and residual identities (3.4)–(3.6) are
   correct as displayed; the Section 10 sign-error contingency can be retired.
4. **O0** — the schema obstruction, verified by direct introspection of the
   frozen library's full transitive closure.
5. **O1** — ambient nonfunction, independently re-derived here (census
   `16*1 + 2*28 = 72`, exact gcds `1` and `C+1`, masses `276`/`275`), with
   REPAIR 6's relabelling.
6. **O2-strengthened** — the second chart is not expressible in GGV's source
   category. This is the strongest new item in the review and it is a
   structural, citation-backed statement, not an experiment.
7. **D3(a)** — at the live `8_28` corner, `p_0 = lambda(z^4-alpha)^21`, one
   deck orbit, all roots GGV-admissible under (5.9), and GGV5 (2.5)
   reproduces the campaign's `(11/4,7)` and `gamma = 7`. This is a clean
   source-to-ledger consistency certificate and it narrows clause (4.1) at the
   live case.

**Not promotable:**

- "`DPT_a` contains the labels consumed by the later book machinery" (B8,
  **REFUTED**).
- "Increment: the sorted-component `H=Q` issue for `8_28`" as *new* (§10
  below, **REFUTED**).
- Theorem 4.1 at `EXACT` tier (D2).
- Anything about `G2-PSC`, `G2-BD`, landing, cofinality, or JC2.

---

## 9. Cheapest next discriminator

The producer proposes an `8_28` coefficient-scheme elimination for the paired
second-chart residual scalar `r`. That is a reasonable *second* step but it is
not the cheapest, and D3(a) shows it is aimed slightly off-target.

**Cheapest (desk-scale, hours, no AWS, no CAS):**

> **DISC-1 (transposability census).** Take the frozen `8_28` record and ask
> whether the transposed corner `(28,8)` admits *any* GGV chain: run the
> campaign's own faithful port with the `a < b` guard at `lib/families.py:156`
> examined rather than executed, and determine whether GGV's standard-pair
> definition (`[6]`, Def. 4.3) can be satisfied by a pair whose base corner
> has `a > b`. Two outcomes, both decisive:
>
> - *No*: T-transpose is a genuinely new theorem and `G2-PSC` cannot be closed
>   by any strengthening of Theorem 2.20. The campaign should then either
>   adopt a pure-Sigray architecture (which `REDUCTION.md` §7.1 already says
>   bypasses `G2-PSC`) or prove T-transpose from scratch.
> - *Yes* (via a swap automorphism absorbed into the equivalence `~`): then
>   the second chart is reachable by a *second* GGV run, `G2-PSC` reduces to
>   pole-path reachability alone, and the producer's clause list collapses from
>   three boxed clauses to one.

This costs one primary-source read and no computation, and it decides which
of the producer's three boxed clauses is actually load-bearing. Only after
DISC-1 returns *Yes* does the producer's `r`-constancy elimination become the
right next experiment.

**Second-cheapest (also desk-scale):** verify H-TRUNC (C3) on the live `8_28`
chain by comparing `sum_j lambda_j X^{sigma_j/rho_j}` against the first three
Puiseux coefficients of the two `x = infinity` places already computed in the
frozen prototype. That closes the last conditional in Proposition 3.1.

---

## 10. Desk checks, custody and novelty

### Checks I ran (all exit 0, all reproduced)

```text
$ shasum -a 256 xmodel/g2-psc-typed-source-to-pole-tree-interface-sol-ultra-20260827.md
4c3f2236a11f296f7eb194bb26e8cdc8ff0b91f10d8d7151e6314caa62629304     [MATCHES]

$ python3 -B tests/test_families.py
  PLLC OK / II.b (1,0)-guard OK / (q_k) machinery OK
  GGV5 S5 family table (24 families, 9 corners) OK
  GGV5 S6 tables (34 cases, maxdeg <= 150) OK
  Gate A OK / Gate B OK: S4 corner data for (9,27),(9,24),(8,28),(7,21) exact
  ALL FAMILIES TESTS PASS                                             [MATCHES]

$ python3 -B cases/transport_check.py
  status PASS; ggv_degrees (108,72) -> sigray_degrees (72,108), type (2,3)  [MATCHES]

$ python3 -B cases/.../ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/verify_r1.py
  status PASS; mathematical_result_unchanged true;
  frozen_result_sha256 deb3a6308e07137c4113a45d4edafdd7a0be34d954d600b33d85ddb8acba57bd  [MATCHES]

$ CornerData introspection: 16 fields; has_exact_pair/fibre/face_root/ring_map all False;
  Corner/Edge/Chain/Family closure is pure lattice data                [MATCHES]
```

### Independent checks the producer did not run

```text
exact gcd over Q:  gcd(C^16-1, C^8+1+C)  = 1        (tau=1: no root)
                   gcd(C^16-1, C^8+1+2C) = C+1      (tau=2: exactly c=-1)
boundary census:   16*1 + 2*28 = 72 = deg f         (dichotomy closes exactly)
pole masses:       2*42+16*12 = 276 ; 2*42+15*12+11 = 275
VGG (5.9) at 8_28: bound 4, m_lambda = 21, 3|21, #factors 4>1  -> all roots admissible
GGV5 (2.5):        (3/3,0) + 7*(1/4,1) = (11/4,7) ; gamma = 7   -> matches live record
Sigray St 3.1:     re-proved from Lem 2.1(i) by a positive-weight valuation argument
```

### Snapshot rehash

10 of the 13 recorded canonical/primary hashes reproduce byte-for-byte,
including every load-bearing one: `ladder/REDUCTION.md`, `ladder/TRANSPORT.md`,
`ladder/SIGRAY-AUDIT.md`, `notes.md`, `refs/sigray_full.pdf`, `lib/FAMILIES.md`,
`lib/families.py`, `tests/test_families.py`, `xmodel/sol-landing1.md`,
`xmodel/sol-h5a.md`, `xmodel/sol-wtc1-round2.md`, and both prototype artifacts.
`COORDINATION.md`, `AUDIT.md` and `APPROACHES.md` have drifted — these are the
shared concurrently-dirty files the producer itself flags, and none is
load-bearing for any verdict here.

### Custody anomaly — **PROVISIONAL, not CONFIRMED**

Section 9 states "this producer did not edit any canonical file" and Section 10
repeats "No canonical file, frozen artifact, or `jc2-lean` file was edited."
This is **not verifiable from the working tree**, and there is a self-reference:

```text
ladder/REDUCTION.md  sha256 = 1ff57e1f...  [exactly the value recorded in Section 9]
  -> contains a block "Provisional typed-interface sharpening (2026-08-27
     19:19Z; independent review live)" citing `4c3f2236...`, the producer's OWN
     SHA-256, plus "Opus5 hostile review is pending".
  -> that block is ABSENT from git HEAD (418e413).
  -> mtime(ladder/REDUCTION.md) = 12:44:39,  mtime(producer) = 12:24:46.
```

The bytes that hash to `1ff57e1f...` already cite the producer's final hash.
So either the Section 9 snapshot was taken after a canonical-file edit that
Section 9 disclaims, or the file was written by another lane after the freeze
and the producer's recorded hash could not have been a pre-freeze read. This
is a **provenance flag only** — it affects no mathematical verdict, and the
ledger block itself is correctly marked provisional with review pending. I did
not edit it.

**Live drift during this review (recorded for reproducibility).** The shared
worktree was written by other lanes while I worked. `ladder/REDUCTION.md` read
`1ff57e1f...` when I took the snapshot above (matching the producer's Section 9
value) and `17c67873a960e273b8bd40d589144177022f14058eeff62236d4521a72fd875f`
at the end of the review — same byte length (75340) and same mtime
(`Aug 27 12:44:39`), i.e. a same-length in-place edit by a concurrent lane.
`AUDIT.md` likewise moved from `5a0f0c43...` to `21c2559c...` (mtime advanced
to `12:46:32`). At both readings the CRITICAL 3 block still cites
`4c3f2236...` and still reads "Opus5 hostile review is pending", so every
quotation in this review is current. `ladder/TRANSPORT.md`
(`9750aa9d...`), `ladder/SIGRAY-AUDIT.md`, `lib/families.py`,
`tests/test_families.py`, `refs/sigray_full.pdf` and both prototype artifacts —
the actually load-bearing reads — were byte-stable throughout. **I wrote
exactly one file: this report.**

### Novelty and history — **CONFIRMED in part, REFUTED in part**

- **CONFIRMED (honest):** `xmodel/sol-landing1.md` (2026-08-23) already
  isolates "a fiber-tagged, two-chart, all-root residual forest" and names
  **CONJECTURE PSC (pole-skeleton capture)** as the minimal landing lemma,
  with the exact hidden-tail separation at §4.6. The producer's Section 9
  explicitly refuses to rename that idea as new. Correct and creditable.
- **CONFIRMED:** the explicit ring-level interface (1.1)–(3.6) and the
  three-arrow composition audit are genuine increments.
- **REFUTED as new:** "the sorted-component `H = Q` issue for `8_28`".
  `ladder/TRANSPORT.md:512-530` already works `8_28` through the component and
  source rotations and records "the Sigray corners are `(56,16) = 2(28,8)`,
  `(84,24) = 3(28,8)`, so the ordered degrees are `(72,108)` and the type is
  `(2,3)`" — i.e. the Sigray `f` is already the `Q`-derived component there.
  The producer's contribution is the *interface consequence* ("a source
  contract containing only the `P` face is ill-typed"), not the fact.
- **CONFIRMED:** the separation of GGV Kummer denominators from Q/jump/max
  labels (O3) is a genuine increment relative to `sol-h5a.md`, which proves the
  repair but does not state the `l_i != kappa_F` interface consequence.

---

## 11. Verdict table

| # | atom | verdict |
|---|---|---|
| A1 | rotation (1.1) vs `TRANSPORT.md` `R(x,y)=(y,-x)`, det 1 | **CONFIRMED** |
| A2 | component sort (1.2)–(1.3), `H=Q` at `8_28`, `[H,J]=c` | **CONFIRMED** |
| A3 | fibre algebra (1.4)–(1.5), smoothness, boundary places | **CONFIRMED** |
| A4 | GGV witness (1.6),(1.8)–(1.10) verbatim vs Thm 2.20 items (7),(8) | **CONFIRMED** |
| A4' | `theta_i` (1.7) — not in Thm 2.20; supplied by VGG `1401.1784` Prop 5.18 | **CONFIRMED WITH REPAIR** |
| A4'' | (1.9) omits `m\|m_lambda`, `#factors>1`, VGG (5.9) | **CONFIRMED WITH REPAIR** |
| A5 | residual polynomial (1.11) | **CONFIRMED** |
| B1 | two-chart split (2.1) vs Sigray St 3.1 (normalized-counterexample scope) | **CONFIRMED WITH REPAIR** |
| B2 | Puiseux presentations (2.2) vs forms (3),(4) | **CONFIRMED** |
| B3 | contact/EW tree (2.3): `O` as max over presentations; St 3.2 `Omega` | **CONFIRMED WITH REPAIR** |
| B4 | `kappa_F`/`nu_F` and Q/jump/max (2.4); `sol-h5a` 1 vs 3 | **CONFIRMED** |
| B5 | `eta_F`, `d/p`, `D`, `kappa-bar` (2.5)–(2.7) vs Not 3.9–3.11, Not 9.1 | **CONFIRMED** |
| B6 | both `p_{f-a,F}`, `p_{f,F}` (2.8); coincidence on `T_a^+` | **CONFIRMED** |
| B7 | tower (2.9)–(2.10) vs Prop 4.2(i)–(iii); missing `T_a^-`; Prop 4.2 `GAP` | **CONFIRMED WITH REPAIR** |
| B8a | `M_F` at pole vertices (`m_F = 0` collapse) | **CONFIRMED** |
| B8b | `Lambda(F)` vs Prop 5.6 (19) | **CONFIRMED** |
| B8c | "contains the labels consumed by the later book machinery" | **REFUTED** |
| B9 | Theorem 2.1 (exact pair constructor) | **CONFIRMED WITH REPAIR** |
| C1 | ring diagram (3.1)–(3.3); `P`/`Q` face-root identification | **CONFIRMED WITH REPAIR** |
| C2 | inverse substitution (3.4) | **CONFIRMED** |
| C3 | `eta_F = -Z_i` (3.5); H-TRUNC must be a hypothesis | **CONFIRMED WITH REPAIR** |
| C4 | residual identities (3.6), sign and orientation | **CONFIRMED** |
| C5 | Proposition 3.1 as a conditional local statement | **CONFIRMED** |
| O0 | `CornerData` is not a source object (16 fields, closure verified) | **CONFIRMED** |
| O1 | ambient nonfunction; masses 276/275; `R_tau`, `R_tau(-1)=2-tau` | **CONFIRMED** |
| O1' | O1 display frame/letters/sign vs producer's own §1.1, (1.2) | **CONFIRMED WITH REPAIR** |
| O2 | one-root, one-sector trace | **CONFIRMED** (strengthened: chart not expressible) |
| O3 | one presentation does not determine Q/jump/max | **CONFIRMED** |
| O4 | post-Laurent `[P,Q]=X^2` endpoints excluded | **CONFIRMED** |
| §6 | failed-shortcut table, all eight rows | **CONFIRMED** |
| D1 | `ARF` items 1–7 sufficient, not minimal | **CONFIRMED** |
| D2 | Theorem 4.1 (forest compiler) at `EXACT` tier | **CONFIRMED WITH REPAIR** |
| D3 | clauses (4.1)–(4.3) complete | **CONFIRMED WITH REPAIR** (missing (4.0)) |
| D3a | "all roots" open at `8_28` | **REFUTED** (closed: `m_lambda=21 >= 4`, one deck orbit) |
| §7 | `R_tau(C)=C^8+1+tau C mod C^16-1`, `R_tau(-1)=2-tau` | **CONFIRMED** |
| §7 | proposed elimination is the cheapest next test | **PROVISIONAL** (DISC-1 is cheaper) |
| §8 | three desk checks | **CONFIRMED** (all reproduced) |
| §9 | snapshot hashes | **CONFIRMED** (10/13; 3 flagged-dirty non-load-bearing) |
| §9 | "did not edit any canonical file" | **PROVISIONAL** (self-reference in `REDUCTION.md`) |
| §9 | dependency list complete | **CONFIRMED WITH REPAIR** (VGG `1401.1784` undeclared) |
| §9 | novelty: `sol-landing1` dedup | **CONFIRMED** |
| §9 | novelty: sorted-component `H=Q` at `8_28` as new | **REFUTED** (`TRANSPORT.md:512-530`) |
| §10 | scope firewall | **CONFIRMED** |
| §11 | status vocabulary | **CONFIRMED WITH REPAIR** (add the Prop 4.2 `GAP` rider) |

---

## 12. Implications

- **`G2-PSC`:** not proved, not advanced past `sol-landing1.md`'s PSC in
  content, but **retyped usefully** and, by O2-strengthened, now known to
  require a *new source category* (T-transpose) before coverage is even a
  well-posed question. The producer's refusal to call Theorem 2.1 `G2-PSC` is
  correct.
- **`G2-BD`:** untouched. `REDUCTION.md` §7.1's "no established implication in
  either direction" stands; nothing here bears on delay/carrier bounds.
- **Landing / full-configuration coverage:** untouched. `REDUCTION.md`
  CRITICAL 4's five requirements are unaffected; a local flag segment is not a
  landing record.
- **Cofinality / absolute total-degree ceiling:** untouched.
- **JC2:** nothing. No family exclusion, no degree ceiling, no counterexample.
- **No promoted result is weakened.** The `8_28` controls are non-Keller
  (canonical witness `Jac(f,g_1)|_{x=0} = -12y^11 + 8y^22`), and no campaign
  theorem ever asserted a `CornerData -> DPT` map.
- **One campaign hygiene item surfaced:** the interface documents should carry
  the VGG `arXiv:1401.1784` dependency wherever `theta_i` or a GGV successor
  pair is used, since GGV5 alone does not supply it.

---

## 13. Output, identity, checks, scope firewall

**Output path:** `xmodel/g2-psc-typed-source-to-pole-tree-interface-hostile-review-opus5-20260827.md`
**SHA-256:** `d4339be820d9f373fb6ea27ede2e62e336d39deaf2590afd991273ebd5881c5b`
(self-hash of the byte-state immediately preceding insertion of this line; the
final file hash is emitted by the review transcript and differs by exactly this
substitution).
**Model identity:** Opus 5, exact model ID `claude-opus-5`, acting as a
different-model hostile mathematical reviewer. No sub-agent, no
`deep-research`, no `ultrareview` was invoked.

**Checks run.** Producer rehash (match). Three producer desk checks re-executed
(`tests/test_families.py`, `cases/transport_check.py`, prototype `verify_r1.py`),
all exit 0 and all outputs matching. `CornerData` introspection over the full
transitive closure. Snapshot rehash of all 13 recorded artifacts. Primary-source
reads: Sigray thesis pp. 7–17, 19–21, 24–28, 39, 48 (extracted from the pinned
`refs/sigray_full.pdf`, hash verified); GGV5 Theorem 2.20 in full and its
direction interval / `L^(l)` definitions from `arXiv:1708.07936v1`; VGG
Propositions 5.18 and Theorem 7.6 and the `L^(l)` definition from
`arXiv:1401.1784v3`. Independent exact desk computations: boundary-place census
`16*1 + 2*28 = 72`; residual `R_tau(C) = C^8 + 1 + tau C`; exact polynomial gcds
over `Q`; pole masses 276/275; VGG (5.9) bound at the live `8_28` corner;
GGV5 (2.5) reproduction of `(11/4,7)` and `gamma = 7`; a from-scratch proof of
Sigray Statement 3.1's dichotomy from Lemma 2.1(i).

**Scope firewall.**

- This review proves no `G2-PSC`, `G2-BD`, GGV family exclusion, degree
  ceiling, landing theorem, cofinal ceiling, counterexample, or JC2 result.
- Every verdict is about the producer's typed interface. The `8_28` controls
  are non-Keller; O1 establishes ambient ledger insufficiency only.
- The `REFUTED` verdict on B8c is about the producer's *sufficiency claim* for
  `DPT_a`, not about any Sigray statement; Sigray's Notation 9.1/Statements
  9.5 and 9.12 are quoted as printed, with the campaign's `SIGRAY-AUDIT.md`
  errata perimeter unchanged.
- The `REFUTED` verdict on D3a is confined to the live `8_28` stage-0 corner;
  it says nothing about other corners, other families, or the general case,
  where D3(b) shows the "all roots" clause remains substantive.
- O2-strengthened rests on two printed definitions (`L^(l) = K[x^{+-1/l},y]`
  and `I = ](1,-1),(1,0)]`) plus the campaign's own port guard
  `lib/families.py:156`. If a GGV convention permitting `a > b` inputs is
  produced, O2-strengthened and T-transpose roll back to the producer's weaker
  O2, and clauses (4.1)–(4.3) stand unchanged.
- The custody anomaly in §10 is a provenance observation only and carries no
  mathematical weight; I did not investigate authorship further.
- **I edited no canonical ledger, no frozen artifact, and no other campaign
  file.** I did not enter, list, read, build, status-inspect or modify
  `jc2-lean`. No heavy local algebra was run (largest computation: a degree-16
  exact polynomial gcd). No AWS job was launched. Network access was used only
  for two read-only arXiv fetches of primary literature.
