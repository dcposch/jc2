# Hostile review: N-ON-THE-TREE — FRONTIER-N, RADIUS-ORDER, DETECTOR-NULL, N-CEILING, FILTER-INVERSION, the N < D/2 corollary

**Reviewer.** grok-4.6 (different-model gate). **Date.** 2026-09-02. **Lane.** `N-ON-THE-TREE-REVIEW`.
Default to refutation. Desk-scale CAS, sympy 1.14.0 over `Q`. Frozen inputs only. `FALLACY-v2` in force. No `charge_basis`. No ledger edit; `jc2-lean` not opened.

**Headline.** The instrument exists, inverts the charged filter, and does **not** prove a `D`-ceiling. FRONTIER-N, RADIUS-ORDER (in the `M_s=n-2` gauge), DETECTOR-NULL, N-CEILING as an **upper** bound, FILTER-INVERSION, and `N<D/2` under the stated Moh-gauge hypotheses survive. The residue of `OPEN[N-ON-THE-TREE]` is the sub-tree of the last major disc `D_1`. Two producer claims about Moh's printed page fail: `n=75` is not OCR-illegible, and Theorem (5) already prints the root-count bound `n/(n-M_r)`.

## Verdict table

| # | Claim | Verdict |
|---|---|---|
| (a) | CONTACT-DEFICIENCY, monicity, seven controls, same-slope scope | **CONFIRMED**. Three rows recomputed. Negative control load-bearing. DC §5.1 scope repair **CONFIRMED**. |
| (b) | THEOREM FRONTIER-N | **CONFIRMED**. Reproved. Exact on 7/7 driver rows; 3 recomputed here. |
| (c) | THEOREM RADIUS-ORDER | **CONFIRMED** in NU-TWO scope (`M_s=n-2` ⇒ `n-M_s-1=1`). From Def 5.1(3) p.179. 242099/0 reproduced. |
| (d) | DETECTOR-NULL; missing datum is the sub-tree of `D_1` | **CONFIRMED** against Prop 6.1(2) p.191 and Theorem (5) p.200. Inverts DC's location of the missing input. |
| (e) | N-CEILING; no lower bound; `D_1` lowers `N` | **CONFIRMED** as an upper bound. No skeleton lower bound. Mechanism exhibited. |
| (e) | FILTER-INVERSION | **CONFIRMED**. `"N<=16"` rejects nothing. Operative test `U >= N_min`. |
| (f) | `1/N > 1/deg P + 1/deg Q`, hence `N < D/2` | **CONFIRMED** for degree-minimal noninvertible Keller pairs in Moh's gauge with NU-TWO and Lemma 6.1. **Not** for every noninvertible Keller pair. |
| (f) | `N <= 44` at MOH-SHARP-2 admissible degrees | **CONFIRMED** as a measured corollary of N-CEILING: max `U_rob=224/5` at `D=120`. |
| (g) | `D<=400`: 3874261 groups; `U<2` never; min `U=792/329`; `U<4` on 1147 (0.030%); no `D` emptied | **CONFIRMED** against the hashed log and a `D<=60` rerun. **"Provably" `U>2` at all `D` is GAP.** |
| (h) | Window `[101,200]`: 19455 of 116385 inside `[4,16]`, 418 pinned to `N=4` | **CONFIRMED** (recomputed). Survivor `U_tower=9,6,10.5,12,8,16` **CONFIRMED**. `(64,48)` **CONFIRMED**. |
| (i) | C5: top-form exponent `n/d_s` not `d_s` | **CONFIRMED** as OCR restoration. p.194 already has stacked `n/d_s`. |
| (i) | C6: Theorem (5) printed `d_r/(n-M_r)` as a root count | **REFUTED as a Moh-error.** p.200 already prints `#roots <= n/(n-M_r)`. Recovered formula **CONFIRMED**. |
| (i) | `n=75` deltas "OCR illegible"; predicted `(1/5,2/3)` | **"Illegible" REFUTED.** p.202 prints `1/5` and `1/2 [1/3]`. Formula gives `1/2 [2/3]`. `OPEN[DELTA75-BRACKET]` **remains OPEN**. |

---

## 0. Custody, method, scope

Frozen copies hashed with `shasum -a 256` **before any was read**. All four match the charge:

```text
44223b324641e75be374f09c4b6daead796937d3176d8841844551e2d19c3967  n-on-the-tree-opus5-20260902.md
863b05dbbd425035a09265cacdf6c418a2a3a1a7fadbeb303571bb5ccba618d6  depth-ceiling-opus5-20260902.md
4a171d910e8e7308ed958a539f97c53e01abcee62239581564ef03fca0031421  depth-ceiling-review-gpt55-20260902.md
8116bc656f46647a111675f49051f363030fe9f852be66ddaf77d86b97de9e4c  integration15-coordinator-fable51-20260902.md
```

**CH** = producer. **DC** = DEPTH-CEILING. **DR** = its gpt-5.5 review. **INT15** = integration #15. Moh = T.T. Moh, J. reine angew. Math. 340 (1983) 140–212. Journal page `P` is PDF page `P-139`. `MOH:` lines are `box/depth-drivers-20260902/moh.txt`.

```text
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  refs/moh1983_jram340_configurations_of_roots.pdf
b6a369146240dbd36107907ebfb63ab2fc602abb524151d6ab31d39e5bc10722  box/depth-drivers-20260902/moh.txt
3022020435c86b62ecd28df8d28d1bdf9ab4e361828c028b913ba8aae3f11a39  box/moh_skeleton_N.py  (= nott-drivers copy)
be641ba89bad574bbd9fdcd91d8f3b63b2bd21a2391c7d173c2ee133b09d50aa  box/nott-drivers-20260902/filter400.log
```

Pages rendered at 160 dpi and read as images: 179 (Def 5.1), 191–194 (Prop 6.1, leading form, Lemma 6.1), 200 (Theorem (4)–(5)), 202 (table), 207 (Appendix II). Independent derivation of FRONTIER-N, RADIUS-ORDER from the p.179 display, DETECTOR-NULL from Prop 6.1(2)/Theorem (5), N-CEILING covering, and the harmonic bound; sympy over `Q` on three two-tower rows plus the gauge negative control; Fractions on Def 5.1(3) for the six Moh rows and the min-`U` skeleton; delivered driver for `D<=60`, CONTROL 6/7, and the `[101,200]` window. No Groebner, no AWS, no `jc2-lean`, no ledger edit. No exit price.

Consumed at INT15 PROMOTED: CONTACT-DEFICIENCY (monic GEN), NU-TWO, DEPTH-LOG as a count, PLACE-LEDGER, MOH-SHARP-2 arithmetic, `(64,48)`, recovered Def 5.1(3). **Not consumed:** case (A), A2, `Z(G)=1`. `OPEN[DELTA75-BRACKET]` was **not** promoted (INT15; DR executive). Six integers kept apart: campaign `N`; Moh `n=deg_y g=D`; `m=deg_y f`; `K=gcd(m,n)`; exponent `d` in `l(f)=alpha H^d`; Moh's `d_i`. Campaign `n=deg Abar_F` does not occur.

---

## 1. Item (a) — CONTACT-DEFICIENCY

**CONFIRMED.** Reconfirm INT15 with monicity load-bearing and with DC §5.1's budget form scoped to Moh Lemma 6.1 / Prop 6.1.

CH:91–109. Let `f,g in C[x,y]` be **monic in `y`** with `deg f = deg_y f = m`, `deg g = deg_y g = n`, and `F=(f,g)` dominant. For generic `(c_1,c_2)`, `t=x^{-1}`, Puiseux roots `phi_j` of `f-c_1` and `tau_i` of `g-c_2`,

```text
N := deg F = deg_x Res_y(f-c_1, g-c_2) = - sum_{i,j} ord_t(tau_i - phi_j).
```

Both monic ⇒ `Res_y = prod_{i,j}(phi_j-tau_i)` with **no leading-coefficient factor** — the load-bearing use of monicity. `deg_x=-ord_t` on `C[x]`; `ord_t` additive. Three genericity clauses: fibre reduced (automatic for Keller; generic `c` otherwise); distinct `x`-coordinates (generic linear change in the gauge); `deg_x Res` maximal (coefficients polynomial in `(c_1,c_2)`).

Off gauge the identity fails. Independent, `c_1=7/3`, `c_2=-5/2`: `(y, x+y^5)` and `(y, x+y^7)` give `deg_x Res=1=N`; `psi_2 o (x, x y^2)` (`f=x+x^2 y^4`, not monic in `y`) gives 6 ≠ 2; `psi_3 o (x, x y^3)` gives 12 ≠ 3; `(x, x y^2)` and `(x^3,y^2)` accidentally agree. CH:139–154, driver CONTROL 2. **Monicity is load-bearing and was tested by failure.**

Closed-form factors `(y-a x)^p - b x^q`. Three rows recomputed independently of the deliverable (first, the `(m,n)=(4,4)` N=13 row, near-proportional row):

```text
f-spec                         g-spec                      m n  Nres Npair Nfront
[(1,1,3,0),(2,1,5,0)]          [(1,2,7,1),(2,1,11,0)]      2 3    4     4      4
[(1,2,3,1),(2,2,5,1)]          [(1,3,7,2),(2,1,11,0)]      4 4   13    13     13
[(1,2,3,1),(2,2,3,1)]          [(1,3,3,1),(2,3,3,1)]       4 6   18    18     18
```

Remaining four rows equal in `run200.log` (N = 9, 9, 12, 18). Seven of seven.

**Scope repair to DC §5.1.** Same-slope pairs have `ord_t > -1` for free. They have `ord_t >= 0` only after a shear realising Lemma 6.1 (`delta_{s-1}>=0`, p.194: "If `delta_s=-1` then `delta_{s-1}>=0`") and Prop 6.1 (`delta*_{s-1}>=1`). Off that normalisation the same-slope sum is negative and `N` exceeds the cross-class count. MEASURED row 0: leading coefficients `{1,2}` on both; 3 cross pairs; `N=4>3`. Five of seven rows have `[l(f),l(g)]≠0` (CONTROL 5a), so `2deuv` is undefined. **Scope, not error.** Do not promote DC's budget `sum same-slope >= 180-N` off Lemma 6.1.

---

## 2. Item (b) — THEOREM FRONTIER-N

**CONFIRMED.** PROMOTE for every dominant `F` with both coordinates monic in `y` of `y`-degree equal to degree; generic `(c_1,c_2)`.

CH:174–193. Moh's `pi`-root `sigma_delta` is the general point of the disc of logarithmic radius `delta` (Def 1.3 / Prop 1.2, p.147; `MOH:361–384`). Multiplicity = number of roots in the disc, and `ord_t h(sigma_delta) = sum_j min(delta, ord_t(sigma-h-root_j)) =: lambda_h(delta)`: continuous, piecewise-linear, nondecreasing; slope = roots still in the disc; `lambda_g(-1)=-n`, `lambda_f(-1)=-m` in the gauge.

**Statement.** For each root `rho_i` of `g` let `delta^0_i` be the unique level with `lambda_g^{(i)}(delta^0_i)=0`. Then for generic `(c_1,c_2)`,

```text
N = sum_{i=1}^{n} max(0, - lambda_f^{(i)}(delta^0_i)).
```

**Reproof.** Let `B` be the ball of radius `delta^0:=delta^0_i` about `rho_i`, with `a(B)` roots of `g`. Prop 1.2: `g(sigma_{delta^0}) = g_sigma(pi) t^0 + higher` with `deg_pi = a(B)`. Generic `c_2` makes `g_sigma(pi)=c_2` have `a(B)` simple roots — a bijection from the `g`-roots of `B` onto the roots of `g-c_2` inside `B`; they follow the unshifted `g`-tree to `delta^0` and separate at order exactly `delta^0`. For the corresponding `tau` and every unshifted `f`-root `phi_j^0`, generically `ord_t(tau-phi_j^0)=min(delta^0, ord_t(rho_i-phi_j^0))`, hence `ord_t f(tau)=lambda_f^{(i)}(delta^0)`. Generic `c_1` gives `ord_t(f(tau)-c_1)=min(0, ord_t f(tau))`. `g` monic ⇒ `Res_y(f-c_1,g-c_2)=prod_tau(f(tau)-c_1)`; `f` monic ⇒ no `lc(f)` in the `t`-adic order. So `N = -sum_tau min(0, lambda_f(delta^0)) = sum_i max(0, -lambda_f^{(i)}(delta^0_i))`.

The `c`-shift is absorbed: the formula is on the tree of `f g` alone. Deficiency reading (CH:197–202): if counts stay proportional (`b/a=m/n`) along `rho_i` wherever `lambda_g<0`, then `lambda_f=(m/n)lambda_g` there, so `lambda_f(delta^0_i)=0` by continuity and that root contributes nothing. `N` measures failure of Moh Def 3.1 (distribution detector, p.162; `MOH:1153–1170`).

Verified: `N(frontier)=N(resultant)` on all seven control rows, including near-proportional row 6 (`N=18` because proportionality breaks at the last level). Independent on three rows (§1). A repeated `g`-root would saturate `lambda_g` below 0; excluded for generic `c` and for Keller (étale ⇒ reduced fibres). No `charge_basis`: identity for `N`, not an exit price.

---

## 3. Item (c) — THEOREM RADIUS-ORDER

**CONFIRMED** in NU-TWO scope. PROMOTE `lambda_g(delta_r)=-n prod_{j>r} P_j/Q_j = -n(1-delta_r)/(n-M_r)` whenever `M_s=n-2`. The producer proof elides `n-M_s-1=1`; that factor is 1 in scope and is kept in the driver's `lam_g_radius`.

Journal p.179, Def 5.1(3), display intact, OCR-dropped (`MOH:2129–2133`):

```text
delta_i = 1 - (n-M_i)  prod_{j=i+1}^{s} [V_j(n-M_j)-d_j]
              ------------------------------------------------
              (n-M_s-1) prod_{j=i+1}^{s} [V_j(n-M_{j-1})-d_j]
```

`P_j:=V_j(n-M_j)-d_j>0`, `Q_j:=V_j(n-M_{j-1})-d_j>P_j` (positivity is Def 5.1(2)). So `1-delta_i=((n-M_i)/(n-M_s-1)) R_i` with `R_i=prod_{j>i} P_j/Q_j`. Moh's order is `ord_t g(sigma_i)` at the general point of `D_i` (Prop 1.2; slope `a_i=#` of `g`-roots in `D_i = n V_{i+1}/d_{i+1}`, Def 5.1(1)). Logarithmic radius is `delta=ord_t` (`MOH:347–356`).

**Identity of the two closed forms.** Def 5.1(3) ⇒ `R_i=(1-delta_i)(n-M_s-1)/(n-M_i)`, so `-n R_i=-n(1-delta_i)(n-M_s-1)/(n-M_i)`. NU-TWO (INT15 PROMOTED) has `M_s=n-2`, hence `n-M_s-1=1` and `-n R_i=-n(1-delta_i)/(n-M_r)`.

**This equals `ord_t g(sigma_i)`.** Downward induction, using `n-M_s-1=1`. At `r=s`: empty product, `R_s=1`; root ball `delta_s=-1` contains all `n` roots, so `lambda_g=-n`; also `-n(1-(-1))/(n-(n-2))=-n`. Step: `lambda_g(delta_i)=lambda_g(delta_{i+1})+a_i(delta_i-delta_{i+1})` with `a_i=n V_{i+1}/d_{i+1}`. From Def 5.1(3), `delta_i-delta_{i+1}=R_{i+1} d_{i+1}(M_{i+1}-M_i)/Q_{i+1}` because `(n-M_{i+1})Q-(n-M_i)P=d(Delta M)`. Then `a_i` times that is `n V_{i+1} R_{i+1}(Delta M)/Q_{i+1}`, and `-n R_{i+1}+n V R (Delta M)/Q = -n R_{i+1}(1-V(Delta M)/Q)=-n R_{i+1} P/Q=-n R_i` since `Q-V(Delta M)=P`. Along the major tower `lambda_f=(m/n)lambda_g` by Def 5.1(1): `b_i/a_i=m/n` (`T_1=f`). Without `M_s=n-2` the increment carries `n-M_s-1`; the census never tests that. The driver's `lam_g_radius` keeps the factor and reduces on every census row.

Independent Fractions on Moh's six rows: incremental = product = radius form; `delta_s=-1`; `n-M_s-1=1`; `a_{s-1}=u e`. Published `delta` matches the four unbracketed pairs `(1/4,9/16)`, `(2/7,16/21)`, `(1/4,7/12)`, `(1/3,4/9)` and unbracketed `n=75` values `delta_2=1/5`, `delta_1=1/2` at `V_2=3`. CONTROL 6, rerun: 242099 V-skeletons at `n<=100`, 0 failures of RADIUS-ORDER, product form, and closed N-CEILING. `lambda_g(delta_1)=-1/4,-1/7,-1/4,-3/10,-1/5,-1/3`, all negative. The `n=75`, `V_2=2` computed `delta_1=2/3` does **not** match Moh's printed bracket (item (i), not a failure of the identity).

---

## 4. Item (d) — DETECTOR-NULL, and what `D_1` is

**CONFIRMED.** PROMOTE DETECTOR-NULL and the inversion of DC's missing-input location. Do **not** promote the extra identification of PLACE-LEDGER's `S n` non-proper places with frontier balls inside minor discs (CH:298–300): typing claim, not needed for N-CEILING, not checked here.

**Moh Prop 6.1(2), p.191.** Hypotheses: `g` monic in `y`, `n>1`, a major tower `D_s ⊇ ⋯ ⊇ D_r` for **`r>=2`**, factor `(pi-c_r)` of multiplicity `V_r` with `d_r/(n-M_r) >= V_r` (minor). For any `pi`-root `sigma` of `g prod_{i=1}^{r-1} T_i^psi` with `ord(sigma-tau)>delta_r`: (1) `delta<1` ⇒ `ord g(sigma)<0`; (2) `ord g(sigma)<0` ⇒ `sigma` is a distribution detector for `g, T_1^psi, …, T_{r-1}^psi`. Also `delta*_{r-1}>=1`. Def 3.1 (p.162): a detector has `ord T_j(sigma)=lambda·deg_y T_j` with common `lambda`. With `T_1=f` and `-mu_1=m`, this is `lambda_f=(m/n)lambda_g`.

**Theorem (5), p.200**, displays intact (OCR at `MOH:3239–3245` dropped the numerators). For any `r>=2`, covering of `D_r` by Def 1.1 subdiscs: (4) if `#` of `g`-roots in `E_i` is `> n/(n-M_r)`, the major tower extends to `E_i`; (5) if that number is `<= n/(n-M_r)`, then `E_i` is a minor disc and any `pi`-root `sigma` of `g` with `ord g(sigma)<0` is a distribution detector for `g, T_1^psi, …, T_{r-1}^psi`. Equivalence with Def 5.1(2): `#roots=(n/d_r)V`, so `#roots <= n/(n-M_r)` iff `V <= d_r/(n-M_r)`. Moh already states (5) in root counts; see item (i) C6.

**DETECTOR-NULL (CH:283–293).** Let `E` be a minor disc at any level `r>=2`. Every `g`-root in `E` contributes **0** to `N`. Proof: Prop 6.1(2) + Theorem (5) ⇒ `lambda_f=(m/n)lambda_g` on `{lambda_g<0} ∩ E`. FRONTIER-N evaluates at the `g`-frontier where `lambda_g=0`. Continuity ⇒ `lambda_f(delta^0)=0` ⇒ `max(0,-lambda_f(delta^0))=0`. Moh's gloss (p.193–194): roots in a minor disc "are all distributed proportionally according to the `y`-degrees up to the uncertainty of `2^0=1`" — the blur at `ord g=0` is the frontier FRONTIER-N already accounts for by `min(0,·)`.

This inverts DC `OPEN[N-ON-THE-TREE]` (DC:671–679; INT15 successor): DC located the missing input as "the minor-disc distribution (Moh sec.6, Prop 6.1)". Prop 6.1 is what makes those discs contribute zero. Section 6 supplies them completely.

**What "the sub-tree of `D_1`" is.** The major tower is `D_s ⊋ ⋯ ⊋ D_1`, constructed for `r>=2`. NU-TWO: `D_s` has exactly two children, major `D_{s-1}` (`ue` roots of `g`, `ud` of `f`) and minor `D*_{s-1}`. DETECTOR-NULL kills minor children; major ones continue. The tower **stops at `D_1`**. At `r=1`, Theorem (5)'s minor criterion would read `#roots <= n/(n-M_1)=n/(n+m)<1`. No nonempty disc is minor. Every nonempty subdisc of `D_1` would be "major" under (4) and would want to extend the tower — but there is no `M_0`, no `T_0`, no next characteristic pair, and Prop 6.1 / the Theorem are stated only for `r>=2`. **`D_1` is where Moh's recursion ends.**

For each bottom-major disc `D_1` (radius `delta_1`, `a_1=e V_2` roots of `g`, `b_1=d V_2` of `f`): the joint ultrametric tree of those `a_1+b_1` Puiseux roots at orders **strictly finer than** `delta_1`. Effect on `N` is one rational `N|_{D_1}=sum_{rho in D_1}(-lambda_f(delta^0_rho))^+` in `[0, a_1(-lambda_f(delta_1))]`. Top: every `f`-root separates from every `g`-root at `ord=delta_1` (`lambda_f` frozen). Bottom: counts stay proportional until `lambda_g=0`. Summed over bottom-major discs: `N in [0,U]`, cut only by global `N>=2`. Jacobian may still constrain this. Moh's published recursion does not. That is `OPEN[D1-SUBTREE]`.

---

## 5. Item (e) — N-CEILING, no lower bound, FILTER-INVERSION

**CONFIRMED** as an upper bound, with no skeleton lower bound. PROMOTE N-CEILING and FILTER-INVERSION. Do not promote attainability of `N=U`. Do not promote RAMIFICATION-FLOOR's identification of proper places with bottom-major discs (CH:350–356).

CH:311–333. FRONTIER-N: `N=sum_i(-lambda_f^{(i)}(delta^0_i))^+`. `lambda_f` nondecreasing, so if `rho_i` lies in a disc `B` with `delta(B)<=delta^0_i` the term is `<=(-lambda_f(delta(B)))^+`. Cover `g`-roots by maximal minor discs plus bottom-major discs. Minor part: 0 (DETECTOR-NULL). Bottom-major discs are disjoint subsets of `D_{s-1}` (Def 1.1(2)), so their `g`-root counts total `<= a_{s-1}=ue`. On the major tower `lambda_f=(d/e)lambda_g`, hence `-lambda_f(delta_1)=(d/e)(-lambda_g(delta_1))`. Therefore `N <= ue·(d/e)(-lambda_g(delta_1))=u d(-lambda_g(delta_1))^+`. RADIUS-ORDER at `r=1` with `M_1=-m`, `n+m=K(d+e)`, `n=Ke` gives `u d e(1-delta_1)/(d+e)`. If `lambda_g(delta_1)>=0` the covering gives `N=0`; a dominant map has `N>=1`, a noninvertible Keller map has `N>=2` (degree 1 ⇒ birational étale ⇒ injective ⇒ surjective by Ax–Grothendieck ⇒ automorphism). So `lambda_g(delta_1)>=0` is impossible at a counterexample.

The cover `<=a_{s-1}=ue` is crude: Moh's search (8)–(11) would only lower `U`. Reported kill counts are a **floor** on kills (CH:733–736, honest). Different major branches may carry different `V_2,…,V_{s-1}` and different `delta_1`; `U_rob` takes the max at fixed `V_s`. CONTROL 7, rerun: top-of-window `V` realises that max on all 3975 groups at `D<=100`, 0 mismatches.

**No lower bound.** Every ball contributes a nonnegative term to the contact total `N=mn-sum_{B≠root} Delta(B)a(B)b(B)`. Unknown structure **below** `delta_1` can only **increase** contact, which **decreases** `-lambda_f(delta^0)` relative to `-lambda_f(delta_1)`, which **lowers** `N`. The skeleton cannot forbid the proportional configuration that drives `N|_{D_1}` to 0; that is a Jacobian question at a depth Moh's criterion does not reach. The only lower bound from this instrument is global `N>=2` (or `N>=4` under H2, typed as campaign residual). FALLACY-v2: `U` is an upper bound only; `N=U` is never asserted; `[2,U]` is an interval; combinatorial attainability of the top is not Jacobian attainment.

**FILTER-INVERSION (CH:431–438).** A Moh skeleton determines an **upper** bound on `N` and no lower bound. `"N<=16"` is compatible with every skeleton: even those with `U>16` may have `N` as small as 2 if the `D_1` sub-tree adds enough contact. It rejects nothing. The operative test is `U(skeleton)>=N_min`. This is why the instrument cannot prove `D<=C(N)`: that needs a **floor** on `N` as a function of `D`. DC's conditional "if the filter empties the census, the ceiling is proved" (DC:678–679) was never satisfiable.

---

## 6. Item (f) — `N < D/2`, and `N <= 44`

**CONFIRMED with hypotheses.** PROMOTE HARMONIC-BOUND for degree-minimal noninvertible Keller pairs in Moh's gauge with NU-TWO and Lemma 6.1. Do **not** promote it for every noninvertible Keller pair. PROMOTE `N<=44` at `{105,108,112,117,120}` as a measured corollary of N-CEILING, not as a closed form.

CH:335–341. Lemma 6.1 (p.194): `delta_s=-1` ⇒ `delta_{s-1}>=0`. Radii increase downward, so `delta_1>=delta_{s-1}>=0` and `1-delta_1<=1`. Two points at infinity force `V_s<d_s` (Cor 6.1(3), `MOH:3200`), hence `v>=1` and `u<=K-1`. N-CEILING then gives `N<=U<=(K-1)de/(d+e)<Kde/(d+e)=mn/(m+n)`, i.e. `1/N>1/deg P+1/deg Q`. Under (MIN), `d<e`, so `N<D·d/(d+e)<D/2`. Sanity (CH:343–344): for `(x,y+x^k)` the corollary would read `N<k/(k+1)<1`, false — and correctly excluded: `nu=1`, `delta_s>-1`, neither NU-TWO nor Lemma 6.1 applies.

**Not every noninvertible Keller pair.** Required: (i) degree-minimal (NU-TWO, `M_s=n-2`, `s>=3`); (ii) Moh's gauge (monic, `deg=deg_y`); (iii) two points at infinity (`delta_s=-1`); (iv) Lemma 6.1; (v) N-CEILING; (vi) `2<=d<e`. INT15's orbit bridge puts every Aut×Aut `D`-degree-minimal counterexample into GGV subrectangular form with `nu=2`, so in the **campaign's degree-minimal scope** the gauge is available. Without degree-minimality the inequality is false of automorphisms. "Unconditional" in CH:335 means "no H2", not "no hypotheses".

**`N<=44` at the admissible degrees.** MOH-SHARP-2 list `{105,108,112,117,120}` (INT15 PROMOTED). Independent scan of `D=120`: 4104 groups, 7 with `U<4`, max `U_rob=224/5=44.8`. Log maxes: `5400/161`, `6528/169`, `7488/181`, `7128/179`, `224/5`. A degree-minimal counterexample of one of those degrees has some skeleton, hence `N<=U<=44.8`. `N` integer ⇒ `N<=44`. Tightest at `D=120`. Does not reach 16; empties no cell.

---

## 7. Item (g) — measured claims

**CONFIRMED** at the stated ranges, with one wording GAP. PROMOTE the `D<=400` counts as matching the hashed log; PROMOTE the `D<=60` rerun; do **not** promote "`U>2` at all `D`" as a theorem.

Delivered driver rerun, `--nmax 60 --skip-pairing` (pairing already recomputed independently): ALL CONTROLS PASSED (CONTROL 3–7, including 242099 RADIUS-ORDER and 3975 top-of-window).

```text
D<=60:   groups=200     U<2:0  U<4:5     surv=195    min=120/49=2.449  max=1728/89   empty D: NONE
D<=100:  groups=3975    U<2:0  U<4:79    min=192/79     max_tower=5760/161
D<=200:  groups=120641  U<2:0  U<4:360   min=408/169    max_rob=27360/341
D<=400:  groups=3874261 U<2:0  U<4:1147  min=792/329    max_rob=123648/719
         U<=0: 0.  empty degrees: NONE.
```

`D<=60` agrees with `filter400.log` rows `n=48,54,60` to the unit. `1147/3874261=0.0296%`, charged `0.030%`. Independent reconstruction of the claimed min-`U` skeleton `n=390`, `m=260`, `M=(-195,388)`, `V_s=33` (top of window `V_2=66`): `U=792/329`, `(u,v,d,e)=(66,64,2,3)`, `(u-v)de/(d+e)=12/5`. Driver CONTROL count: 100 `[ok]` in `run200.log`, 0 failures. Window arithmetic: `3975+116666=120641`.

**GAP on "provably cannot fire".** CH:59–60, CH:475–480 claim an asymptotic floor `2de/(d+e)>=12/5` so the unconditional filter "provably CANNOT fire". The derivation: as lower `V_j→∞`, `P_j/Q_j→(n-M_j)/(n-M_{j-1})` and `sup U` exceeds `(u-v)de/(d+e)`; minimising that **lower estimate of a supremum** at `2V_s-d_s=1`, `(d,e)=(2,3)` gives `12/5`. That does **not** prove `U>(u-v)de/(d+e)` at finite `V`, nor `U>2` at all `D`. CH:661 already caves: "`U>2` beyond `D=400` is **not** claimed." Repair: strike "provably"; keep MEASURED `U<2` equals 0 at `D<=400`; leave all-`D` `U>2` as OPEN with bounded quantity the next min `U_rob` at `D>400`. FALLACY-v2: a measured floor on a finite set is not a theorem.

The `U<4` kills are confined to nearly-balanced top forms. At `D<=60` the five kills are all `n=54`, `m=36`, `V_s=5`, `U=120/49`.

---

## 8. Item (h) — per-skeleton window and survivor `U`

**CONFIRMED.** PROMOTE the window counts and the six `U_tower` values. PROMOTE the independent `(64,48)` confirmation.

Surviving = `U_rob>=4`. "Top=16" means `U_rob>=16`. "Inside `[4,16]`" means `4<=U_rob<16`. "Pinned to `N=4`" means `4<=U_rob<5`. Recomputed from the delivered `U_robust` (these counts are **not** printed by the driver):

```text
[48,100]:   groups 3975   surv 3896   top=16: 2197   inside: 1699   pin4: 104
[101,200]:  groups 116666 surv 116385 top=16: 96930  inside: 19455  pin4: 418
```

CH:490–496: 3896, 2197, 104 at `[48,100]`; 116385, 19455 (16.7%), 418 at `[101,200]`. Exact match. D=105 example CH:502: `m=42`, `M=(-35,103)`, `V_s=4`, `(u,v)=(12,9)`, `1-delta_1=21/83`, `U_rob=360/83=4.337`. Independent `U_robust` agrees.

Independent Def 5.1(3) on Moh's published `V`:

```text
row                 K (d,e) (u,v) 1-delta_1 U_tower           U_rob
(64,48)            16 (3,4) (12,4)  7/16      9               1152/83=13.880
(84,56) M2=64,V2=2 28 (2,3) (21,7)  5/21      6               441/26=16.962
(84,56) M2=72,V2=5 28 (2,3) (21,7)  5/12     21/2             441/26=16.962
(75,50) V2=3       25 (2,3) (20,5)  1/2      12               200/11=18.182
(75,50) V2=2       25 (2,3) (20,5)  1/3       8               200/11=18.182
(99,66)            33 (2,3) (24,9)  5/9      16               2160/119=18.151
```

`U_tower=9,6,10.5,12,8,16` as charged. With Moh's own `V` row, all four sit inside `N<=16` as an **upper** bound (FILTER-INVERSION: compatible with the campaign window, not killed by it). `U_rob` exceeds 16 on five of six rows; the reverse filter at 16 does not pin them. The `(84,56)` `M_2=64` row has `U_tower=6`, so `N in [4,6]` under H2 at Moh's published `V`.

`(64,48)`: Appendix II p.207 prints "(64, 68)" and, in the same appendix, the reduced table `(n,m)=(16,12)`. `68/4=17≠12`; `(64,48)/4=(16,12)`. DC's C1 / INT15 promotion CONFIRMED by this independent reading of p.207. Census contains all six published `(n,m,M,V)` rows (CONTROL 4, rerun).

---

## 9. Item (i) — two Moh OCR corrections, against the page

**C5, p.194 — CONFIRMED as OCR restoration.** The image reads `g(x,y)=[(y-ax)^{v_s}(y-bx)^{u_s}]^{n/d_s}` with stacked exponent `n/d_s`, and `u_s=d_s-v_s`. Degree `(v_s+u_s)·n/d_s=n`. The OCR (`MOH:2896–2898`) flattened the stack to `]^{d_s}`, which has degree `d_s^2`. CH:233–239 correctly restores the page. Slope classes then carry `(n/d_s)V_s` and `(n/d_s)(d_s-V_s)` roots — Def 5.1(1) at `i=s-1` — so the top form is `L_1^{ue} L_2^{ve}` with `u=V_s K/d_s`. Verified: `a_{s-1}=ue` on all six Moh rows. **Not a Moh error.**

**C6, p.200 — REFUTED as a Moh-error; CONFIRMED as the recovered formula.** CH:607–610: "the number of roots of `g(y)` in `E_i` is `<= d_r/(n-M_r)` is the bound on the MULTIPLICITY `V`; in root counts, `#roots <= n/(n-M_r)`." The page already prints `#roots > n/(n-M_r)` in (4) and `#roots <= n/(n-M_r)` in (5). The OCR dropped the numerator `n` (`MOH:3239–3244`). The producer guessed `d_r` and then "corrected" it to `n`. Repair: C6 is restoration of OCR-dropped `n`, not a correction of Moh. The recovered root-count form is what the paper says, equivalent to Def 5.1(2)/Prop 6.1's bound on `V`. At `r=s`, `#roots<=n/2` on the minor slope class iff `v<=u`, which is NU-TWO.

**`n=75` "OCR illegible" — REFUTED.** p.202, row `n=75`: `delta_2=1/5`, `delta_1=1/2 [1/3]`, perfectly legible (DR already read this crop; INT15 left `OPEN[DELTA75-BRACKET]` unpromoted). Def 5.1(3) gives `delta_1=1/2` at `V_2=3` (matches the unbracketed entry) and `delta_1=2/3` at `V_2=2` (does **not** match `[1/3]`). CH:541–543 and the driver label both `n=75` rows "OCR illegible (prediction)" and print `(1/5,2/3)` for `V_2=2`. That is the formula, not the page. If the printed `1/3` were used as `delta_1`, then `1-delta_1=2/3` and `U_tower=16` still inside `N<=16`; one printed entry, not a wreck of N-CEILING. **`OPEN[DELTA75-BRACKET]` remains OPEN.** Bounded quantity: one bracketed `delta_1` at `(n,m,M_2,V_2)=(75,50,55,2)`, printed `1/3` versus computed `2/3`. Possible Moh/typesetter swap of `delta` with `1-delta` on the alternative `V` only (`1-2/3=1/3`); not filled here.

---

## 10. What the instrument CAN and CANNOT decide

**CAN.** Write `N` as a contact deficiency on the tree of `f g` (FRONTIER-N), for dominant maps in the monic `deg=deg_y` gauge. Evaluate an **upper** bound `U(skeleton)` from Moh's major-tower data alone, after DETECTOR-NULL sets every minor disc's contribution to 0. Reject a skeleton as a host for geometric degree `>=N_min` when `U<N_min`. Pin `N` to a closed integer window `[N_min, min(floor(U), N_max)]`; at `D in [101,200]`, 418 groups are pinned to `{4}` under H2. Prove `N<D/2` and `1/N>1/deg P+1/deg Q` at a degree-minimal counterexample in Moh's gauge with NU-TWO. Exhibit the exact skeletons a realisability/endgame lane must still kill, now with an `N`-window attached.

**CANNOT.** Prove any ceiling `D<=C(N)` (the skeleton bounds `N` above; a `D`-ceiling at fixed `N` needs a floor on `N`). Compute `N` exactly from a skeleton (`D_1` sub-tree is free in Moh's recursion and can drive the contribution from `U` down to 0). Empty a degree, or empty the census under `"N<=16"` (FILTER-INVERSION). Decide realisability of any skeleton, kill Moh's four survivors, or bound `T`, `Psi`, `D`, or `D_min`. Constrain the `D_1` sub-tree by Prop 6.1 / Theorem (5) (those require `r>=2`). Assert `U>2` at all `D` (measured to 400 only).

INT15 §D hoped the filter `"N<=16"` over the census would either empty it (a theorem) or exhibit the exact skeletons. The second branch is what happened, structurally, not for lack of machine.

---

## 11. Opens

```text
OPEN[D1-SUBTREE]  (residue of OPEN[N-ON-THE-TREE], which this lane otherwise
   CLOSES).  Joint ultrametric tree of a_1=e V_2 roots of g and b_1=d V_2
   roots of f below radius delta_1.  BOUNDED QUANTITY: N|_{D_1} in
   [0, a_1 (-lambda_f(delta_1))].  A Jacobian-forced lower bound here would
   make the filter two-sided.  Not filled by cap or analogy.

OPEN[DELTA75-BRACKET]  (INT15, not closed; producer mislabelled "illegible").
   BOUNDED QUANTITY: one printed entry, Moh p.202 delta_1=1/2 [1/3] at
   (75,50,55), versus Def 5.1(3) at V_2=2 giving 2/3.

OPEN[U-GT-2-ALL-D]  (new; the "provably" gap).  BOUNDED QUANTITY: min U_rob
   over branch-robust groups with D>400.  Measured min at D<=400 is 792/329;
   12/5 is not a theorem.

OPEN[UPPER-TO-FLOOR]  (producer; well-posed).  Name an instrument that bounds
   N from below by a function of D.  Absent that, D<=C(N) is not reachable
   from the boundary tree.  BOUNDED QUANTITY: the integer N in [2,16] at a
   degree-minimal counterexample.

OPEN[MOH-14]  (producer; cheap).  Is u d e (1-delta_1)/(d+e) >= 2 implied by
   Moh (7)-(13)?  BOUNDED QUANTITY: the 1147 groups at D<=400 with U<4.
```

Carried: `OPEN[MOH-ENDGAME]`, `OPEN[NONPROPER-DEGREE]`, `OPEN[SUBRECT-ORBIT-BRIDGE]` (INT15 CLOSED YES, not reopened), `OPEN[ANTICANON-DEFECT]`, `OPEN[SAT-MASS]`, `OPEN[DELTA-AFF-VS-N]`. **Retyped, not promoted here:** `OPEN[NU-BOUND-AT-A-PLACE]` as a floor — the direction is right if a proper place sits under a bottom-major disc; the identification of every proper place with such a disc is not checked.

---

## 12. FALLACY-v2 audit

Flag/place/series: Moh `n=D` never mixed with campaign `n=deg Abar_F`. `d_i`, exponent `d` of `H^d`, and GGV `d_j` kept apart. Major tower / minor discs / `D_1` sub-tree carry different theorems (Def 5.1(1); Prop 6.1; nothing). The Sn/proper-place identification in CH:298–300 is **not** promoted. Per-ray: no exit price, no `charge_basis`; FRONTIER-N charges each `g`-root once at its frontier; N-CEILING counts bottom-major discs as disjoint subsets of `D_{s-1}`. Floor/attainment: `U` is an upper bound only; `N=U` never asserted; `min U=792/329` is MEASURED on a finite set; 12/5 is not a theorem (item (g) GAP). Pole/interior: `lambda_h(delta)=ord_t h(sigma_delta)` only at a genuine `pi`-root (Prop 1.2). Controls over `Q` in `x,y`; Puiseux exponents as `Fraction`, coefficients as sympy radicals, compared by `simplify`. Resultant identity has a negative control. No prime read as a derivative. No cap or analogy: `OPEN[D1-SUBTREE]` and `OPEN[DELTA75-BRACKET]` left open; `"provably U>2"` not filled by the 12/5 heuristic.

---

## 13. Typed verdict block

```text
LANE       N-ON-THE-TREE-REVIEW
SCOPE      Keller, noninvertible, degree-minimal, Moh's gauge (deg=deg_y,
           monic in y, two points at infinity / NU-TWO). CONTACT-DEFICIENCY
           and FRONTIER-N for every dominant F in that gauge. Case (A) EMPTY
           and untouched; A2 untouched; no Z(G)=1. H2 only where the
           campaign N-window is quoted. No charge_basis.

PROMOTE    CONTACT-DEFICIENCY CONFIRMED (monic GEN; negative control
             load-bearing). Scope repair: same-slope ord >=0 only under
             Moh Lem 6.1 / Prop 6.1. Reconfirm INT15.
           FRONTIER-N CONFIRMED. N = sum_i (-lambda_f^{(i)}(delta^0_i))^+
             on the tree of f*g. 7/7 driver rows; 3 independent.
           RADIUS-ORDER CONFIRMED for M_s=n-2. lambda_g(delta_r)
             = -n prod_{j>r} P_j/Q_j = -n(1-delta_r)/(n-M_r).
             From Def 5.1(3) p.179. 242099/0.
           DETECTOR-NULL CONFIRMED (Prop 6.1(2) p.191, Thm (5) p.200).
             Minor discs contribute 0. Inverts DC's missing-input location.
           N-CEILING CONFIRMED as UPPER bound
             N <= U = u d (-lambda_g(delta_1)) = u d e (1-delta_1)/(d+e).
             No lower bound from the skeleton.
           FILTER-INVERSION CONFIRMED. "N<=16" rejects nothing.
             Operative test U >= N_min.
           HARMONIC-BOUND CONFIRMED in the stated scope:
             1/N > 1/deg P + 1/deg Q, hence N < D/2.
             NOT for every noninvertible Keller pair.
           N<=44 at {105,108,112,117,120} CONFIRMED (max U_rob=224/5).
           MEASURED D<=400 counts CONFIRMED (log + D<=60 rerun +
             independent min-U skeleton 792/329).
           WINDOW [101,200] 19455/116385 and pin4=418 CONFIRMED.
           SURVIVOR U_tower 9, 6, 10.5, 12, 8, 16 CONFIRMED.
           (64,48) CONFIRMED independently (p.207 (16,12)).
           C5 OCR restoration CONFIRMED (p.194 already n/d_s).

NOT        a D-ceiling on any range; N = U; a skeleton lower bound on N;
CLAIMED    U>2 at all D; HARMONIC-BOUND off degree-minimality / NU-TWO;
           RAMIFICATION-FLOOR's proper-place identification; Sn = minor
           frontier balls; exact N on a skeleton; realisability of any
           row; emptying of any degree; C6 as a Moh-error; n=75
           "OCR illegible".

REFUTED    C6 as "Moh printed d_r/(n-M_r) for #roots" (p.200 prints n).
           "n=75 OCR illegible" (p.202 prints 1/5 and 1/2 [1/3]).

GAP        "provably" U>2 (measured to D<=400 only).
           OPEN[DELTA75-BRACKET] still open (1/3 printed vs 2/3 computed).

CLOSED     OPEN[N-ON-THE-TREE] as posed (instrument exists; filter inverts;
           missing datum is D_1, not minor discs). Residue OPEN[D1-SUBTREE].

DECISION   THE CEILING IS NOT PROVED ON ANY RANGE BY THIS INSTRUMENT.
           The reason is FILTER-INVERSION, not cost. The finite instrument
           INT15 named exists, runs, and answers the opposite question.

CAN        upper-bound N; reject U < N_min; pin some groups to N=4;
           prove N < D/2 in scope; prove minor discs contribute 0.
CANNOT     prove D <= C(N); lower-bound N from the skeleton; evaluate N
           exactly; decide realisability; empty a degree; handle D_1
           with Moh's r>=2 recursion.

DISCLOSURE (1) Prop 6.1(2)/Thm (5) imported as Moh, quoted from page
           images; if they fail, DETECTOR-NULL and N-CEILING fail;
           FRONTIER-N and RADIUS-ORDER do not.
           (2) Def 5.1(3) read from p.179, not from the OCR.
           (3) Kill counts are a floor (crude cover by a_{s-1}=ue).
           (4) N>=4 uses H2 (INT15 §C) and is typed as such.
           (5) D<=400 not rerun (charged D<=60); totals checked against
           the hashed log, the D<=60 rerun, and independent window
           arithmetic 3975+116666=120641.

MEASURED   3 independent pairing rows exact; 6 Moh U_tower exact;
           D<=60 driver: 200 groups, U<2 =0, U<4 =5, min 120/49;
           window [101,200] 19455 / 418; min-U skeleton U=792/329;
           D=120 max U=224/5; 100 [ok] in run200.log.
COMPUTATION python3 + sympy 1.14.0 over Q; Fractions on Def 5.1(3);
            delivered driver for census/filter. No Groebner, no AWS,
            no jc2-lean.
DEVIATIONS C6 retargeted as OCR restoration; n=75 "illegible" rejected;
           "provably U>2" demoted to measured; HARMONIC-BOUND scoped.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `35964`.
- Body SHA-256:
  `5369ee59c2c94e64d055335c94f1ee4b7e5a9b57876bbd35537bdef43212ac7d`.
- Frozen basis: `6a4fbe1d19c9ce187b2f5520ca0b30b0f2c766e5`.
