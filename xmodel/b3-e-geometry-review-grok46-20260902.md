# Hostile review: B3-E-GEOMETRY — every PROVED-HERE item, the witness, the table

**Reviewer.** grok-4.6 (different-model gate).
**Date.** 2026-09-02.
**Lane.** `B3-E-GEOMETRY-REVIEW`.
**Charge.** Default to refutation. Desk-scale exact reasoning plus sympy 1.14.0 over `Q`. Frozen inputs only. `FALLACY-v2` in force. No `charge_basis` line: no new exit price. No canonical-ledger edit; `jc2-lean` not opened.

**Headline.** There is still **NO KILL** of `(B3)`. Seven of eight PROVED-HERE items survive independent derivation, with binding repairs on compactifications, the contracted Orevkov model, and the arithmetic-genus reading of `g`. The witness quintic realises the charged numerical type; its printed points at infinity are misnamed. The fibre-split numbers `2+1+2` are right; “only three of five sit on the dicritical” over-identifies two objects. The proposed successor is not a well-posed lemma.

## Verdict table

| # | Claim | Verdict |
|---|---|---|
| (1) | LEMMA E-ETALE: connected finite étale cover of degree `N` | **CONFIRMED** |
| (2) | THEOREM E-BMY-VACUITY: `kappa-bar` and both log Chern numbers scale by `N` | **CONFIRMED**, binding repair: log-smooth / `Q`-Cartier |
| (3) | PROP 3.1 / LOC-1: fibre split; no infinite place over a smooth point | **CONFIRMED** |
| (4) | COR 3.2 vs B3-N4 at `k <= 8` | **CONFIRMED**, repair: `g = p_a(E~-bar)` |
| (5) | THEOREM E-CHARGE vs Orevkov `k_t` as in MI | **CONFIRMED**, binding repair: contracted model |
| (6) | THEOREM B3-E-GENUS | **CONFIRMED** |
| (7) | THEOREM B3-E-NOCROSS, G-ANTI table, unique-gate claim | **CONFIRMED** among the two G-ANTI ingredients |
| (8) | WITNESS `E_0` | **CONFIRMED** as `REPRESENTATIVE` type; **GAP** on printed point names |
| — | Correction: only 3 of 5 places sit on the dicritical | **CONFIRMED** as a split of `E~-bar`; **GAP** as `E-bar_X ∩ l` |
| — | Correction: orbifold BMY needs `n` and a boundary model | **CONFIRMED** that the charged sentence is false |
| — | The two OPENs raised | **CONFIRMED** well-posed as OPENs |
| — | §6: `(mu,corr)=(2,1)` killed by DO I §§2–7; not `N`-uniform | **CONFIRMED** against integration #7 and `do1-mu2-replay` |
| — | SUCCESSOR: `E-bar_X · l` against Orevkov determinants | **GAP**: not well-posed as written |

Nothing here closes `(B3)` at any `N`. The producer does not claim that it does.

---

## 0. Custody, method, scope

Frozen copies were hashed with `shasum -a 256` **before any was read**. All four match the charge:

```text
87fa5cb23ca59cf8f059a6710a1a460ebf323cee6166da43db2a75ea07666cb2  b3-e-geometry-opus5-20260902.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  horn-flagship-opus5-20260902.md
424e2f5ddec7189efa90c4259b19394ccee75e3eec4842ed1879544cb8fd7fd2  horn-flagship-review-grok46-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  mprime-alln-h2-opus5-20260902.md
```

**BE** = producer, **HF**/**HR** = HORN-FLAGSHIP and its grok-4.6 review, **MI** = MPRIME-ALLN-H2. After the quartet: `xmodel/do1-mu2-replay-sol56-20260901.md` (assembly at 715–722) and `xmodel/integration7-coordinator-fable5-20260902.md` (`N=4-CHECKED-CLOSED`). `xmodel/mprime-alln-review-gpt55-20260902.md` was grepped only for whether Lemma 4.1 is in that review’s promotion list (used, not named there). This gate consumes `N-a_p = r_p W + K_p` as MI displays it. Producer drivers at `box/b3e-drivers-20260902/` were compared after independent CAS, not used as a source.

**Method.** Independent derivation of E-ETALE, log ramification, the fibre-split Euler identities, the RH cap, and the `N-3` closed form. sympy 1.14.0 over `Q`: parametrisation resultant, `factor_list`, pairwise resultants for the affine singular locus, 2-/3-jets, Puiseux inversion, injectivity resultant, generic-fibre gcd. Integer arithmetic for B3-N4 and G-ANTI. No Groebner of `(f,f_X,f_Y)`. No AWS, no literature fetch, no `jc2-lean`. No exit-price assertion.

**Consumed at HR CONFIRMED:** HF B3-N4, HF Prop 3.1 (`rho(G)=S_4`), HF Prop 3.2, B3-DEGREE, B3-CAGE, B3-PUSHOFF, B3-COMPONENT, `SCOPE[B3-QH]`. **Consumed as MI states them:** Lemma A, Lemma 4.1 / `(L)`, control 2, 7.B', N4-PIN, THEOREM PROFILE, Orevkov Lemma 2.1, `k_t := mu_t - e_t mu_l`. **Not consumed:** `Z(G)=1`; `A2`-cell results; `CUSP-A-VOID`; any value of `kappa-bar(A^2 \ A_F)`; `deg E-bar = N · deg A_F-bar`.

---

## 1. LEMMA E-ETALE — CONFIRMED

> `F : A^2 \ E --> A^2 \ A_F` is a connected finite étale covering of degree `N`.
> (BE:111–121.)

**Consumed.** Keller (`Jac F ∈ C^*`); geometric degree `N = [C(x,y):C(P,Q)]`; Jelonek’s non-properness set `A_F`, a closed curve, with `F` proper over `A^2 \ A_F` by that definition; `E := F^{-1}(A_F)`; char 0, `C`. Algebraic properness equals topological properness for finite-type morphisms of `C`-varieties (used silently; the only way the definition of `A_F` yields a finite morphism of schemes).

**Finiteness.** `F : A^2 -> A^2` is étale, hence quasi-finite; the restriction remains quasi-finite. Proper + quasi-finite + finite type + separated implies finite. The parenthetical “proper exactly off the non-properness set” (BE:51–52) is the definition, not an extra theorem.

**Étale of degree `N`.** `Jac F ∈ C^*` makes `F` étale on all of `A^2`. A finite étale morphism to a connected normal base has constant fibre cardinality equal to the function-field degree. Surjectivity: the image is open (étale) and closed (proper) in the connected space `A^2 \ A_F`, and nonempty (`F` dominant). For an automorphism (`N=1`, `A_F` empty) the statement is the identity and remains true; noninvertibility is not required.

**Connectedness.** `A^2 \ E` is the complement of a curve in `A^2`. Over `C` that complement is classically connected (real codimension 2) and Zariski-irreducible. Irreducibility of `E` is not used and must not be: at `N=4`, `k_odd=0`, B3-N4 gives `E` disconnected, and `A^2 \ E` is still connected.

**Promote** at Keller, any profile, any `N`.

---

## 2. THEOREM E-BMY-VACUITY — CONFIRMED, compactification repair

(BE:129–161.) `V := A^2 \ A_F`, `V' := A^2 \ E`, `mu := F|_{V'} : V' -> V` the cover of §1.

**(b) `c_2-bar`.** Defined as `e(V')`. A degree-`N` covering space of a finite-CW homotopy type has `e(V') = N e(V)`. Complex quasi-projective varieties have that homotopy type. For a complex surface, Poincaré duality gives `e = e_c`, so this is also the compactly-supported Euler characteristic of Theorem (E). This number **does not depend on a compactification**.

**(c) log ramification.** `K_{X'} + D' = mu-bar^*(K_X + D)` for `D' = (mu-bar)^{-1}(D)_{red}` is logarithmic Riemann–Hurwitz, once defined. As written, `(X,D)` is “any log compactification of `V` with `D` reduced and `X` normal” (BE:135–137). On a normal surface `K_X+D` need not be `Q`-Cartier, so pullback and square are undefined.

**Repair (binding).** Start from a **log-smooth** compactification of `V` (SNC `D` on smooth `X`; exists in dimension 2). Let `X'` be the normalisation of `X` in `C(V')=C(x,y)`, `D'=(mu-bar)^{-1}(D)_{red}`. Then `mu-bar` is finite, étale over `X \ D`, ramified only along `D'`, and `K_{X'} = mu-bar^*K_X + sum_i (e_i-1)D'_i` with `mu-bar^*D = sum_i e_i D'_i`, so `K_{X'}+D' = mu-bar^*(K_X+D)`. Finite degree-`N` intersection theory gives `(mu-bar^*Z)^2 = N Z^2`. Cyclic quotients along `D'` are allowed; `(K+D)^2` remains rational.

**(d) both numbers, log-minimal models.** `c_1-bar^2` of an open surface is `(K+D)^2` on a **log-minimal** model, not on an arbitrary compactification. Finite pullback preserves nefness and contracts no curve, so a log-minimal `(X,D)` pulls back to a log-minimal (possibly quotient-singular) `(X',D')`. Thus `c_1-bar^2(V') = N c_1-bar^2(V)`. Combined with (b),

```text
c_1-bar^2(V') - 3 c_2-bar(V')  =  N ( c_1-bar^2(V) - 3 c_2-bar(V) ),
```

so log-BMY holds upstairs iff downstairs, and likewise any equal-weight bihomogeneous inequality.

**Same compactification for `c_1^2` and `c_2`?** `c_2-bar` as `e(V)` uses none. `c_1-bar^2` uses the log-minimal model of the pair in (c). On a log-smooth compactification one may also read `c_2` as `c_2(Ω_X(log D)) = e(X)-e(D) = e_c(V)`, and `Ω_{X'}(log D') ≅ mu-bar^* Ω_X(log D)`, so **both** log Chern numbers of that pair scale by `N`. The naive pair `(P^2, A_F-bar + L_infty)` is typically not log-smooth; its `(K+D)^2` is not `c_1-bar^2(V)`. The theorem is about the invariants of the open surfaces.

**(a) `kappa-bar`.** Finite morphisms preserve Iitaka dimension. The sketch (BE:152–157) is a sketch: `mu-bar_* O_{X'}` is coherent of rank `N`, and `h^0(L^{\otimes m} ⊗ E)` has the same growth order as `h^0(L^{\otimes m})` for fixed `E`. That is Iitaka’s étale invariance. Not a promotion blocker.

**Galois-closure variant.** Connected finite étale Galois of degree `|rho(G)|`. HF Prop 3.1 (HR CONFIRMED) gives `S_4` at `N=4`, hence degree 24. E-BMY-VACUITY applies with 24 in place of `N`. The arm cannot say anything the same instrument on `A_F` does not. BE correctly reports no value of `kappa-bar`. **Promote** with the log-smooth / `Q`-Cartier repair binding.

---

## 3. PROP 3.1 / LOC-1 and COR 3.2 — CONFIRMED

`A_F~ ≅ A^1` (MI Lemma A), compactified to `P^1`. Punctures of `A_F°`: `R := sum_p r_p` branch punctures plus one place at infinity. `F` étale and control 2 give an étale cover `E° -> A_F°` of degree `a`. Then `E~-bar -> P^1` is finite of degree `a`, unramified over `A_F°`.

Over the puncture `P_b` of a branch `b` at `p ∈ Sing A_F`: each of the `a_p` affine preimages `y` is a local isomorphism `(E,y) ≅ (A_F,p)`, hence one unramified point of `E~` over `P_b`. Remaining degree `a-a_p = (r_p-1)W+K_p` (MI `(L)`) is at infinity. Over the infinity puncture of `A_F` the whole degree `a` is at infinity. That is PROP 3.1 (BE:226–238). LOC-1 is the smooth case `a_p=a`: the fibre is entirely affine.

**COR 3.2, derived.** Let `S` be the points of `E~-bar` over the `1+R` punctures. Then `sum_{q∈S} e_q = a(1+R)` and `#S = n_infty + sum_p a_p r_p`. RH, ramified only there:

```text
2g-2 = -2a + a(1+R) - #S = a(R-1) - n_infty - sum_p a_p r_p,
```

so `n_infty = (R-1)a + 2 - 2g - sum_p a_p r_p`. For `chi_c`: `chi_c(E~)=2-2g-n_infty` and `chi_c(E)=chi_c(E~)-sum_y(r_y-1)` with `sum_y(r_y-1)=sum_p a_p(r_p-1)`. Substituting cancels `g`:

```text
chi_c(E) = a(1-R) + sum_p a_p.
```

This is BE:244–248. The `chi_c` identity does not use connectedness.

**Repair for `n_infty`.** The derivation writes `2g-2` for a connected curve. At `N=4`, `k_odd=0`, B3-N4 gives two rationals, and the connected formula with `g=-1` (`p_a` of two copies of `P^1`) still returns the right `n_infty`. Binding reading: `g` is `p_a(E~-bar)`, or the formula is applied componentwise.

**Recomputation against B3-N4, every cell `k<=8`.** N=4 (B3): `a=W=2`, cusp `(r,K,a_p)=(1,1,1)`, `k` double points `(2,0,0)`, `R=1+2k`, `sum a_p r_p=1`. Then `chi_c=2(1-R)+1=1-4k`, matching N4-PIN in both branches. With `g=k_odd-1` (`k_odd>=1`) or `g=-1` (`k_odd=0`):

```text
n_infty = 4k+1-2g = 3+4k-2 k_odd   (k_odd>=1)
                    = 3+4k           (k_odd=0).
```

Exactly B3-N4 (HF:337–345). All 44 cells `k=1..8`, `k_odd=0..k` agree on `n_infty` and `chi_c`; `g` agrees for `k_odd>=1`. Samples: `(k,k_odd)=(1,0)` gives `n=7, chi=-3`; `(1,1)` gives `n=5, chi=-3, g=0`; `(8,8)` gives `n=19, chi=-31, g=7`.

**Promote** COR 3.2 with the `p_a` reading.

---

## 4. THEOREM E-CHARGE — CONFIRMED, contracted-model repair

MI:222–225 defines `k_t := mu_t - e_t mu_l >= 0` and `K_p := sum_l sum_t k_t`, so `N-a_p = r_p W + K_p`. At a unibranch point, `(L)` is `a-a_p=K_p`. PROP 3.1 says that quantity is the total degree of the places of `E` at infinity over `P_b`. So “`a-a_p=K_p` is carried entirely by places of `E` at infinity” (BE:630–631) is Lemma 4.1 plus PROP 3.1, and does not need a new intersection inequality.

The **new** statement is (BE:285–290)

```text
k_t  >=  sum  deg(Phi|_Gamma)
```

over branches `Gamma` of `E-bar_X` at `t` with `Phi(Gamma)=b`, the branch `phi_l` covers near `t`.

**The written proof has a hole.** BE:279–283 infers from MI’s Orevkov Lemma 2.1 (“linear chains, contracted tail attached at one point of `l`”) that “no boundary component other than `l` meets `l'`”. Escaping preimages over `p∈A_F` are indexed by points of `l'` (MI:237–239), so those tails **do** meet `l'` at the corresponding `t`. On the uncontracted `X`, `Phi` is not finite there, and `(Phi^*C · Phi^*C')_t = mu_t (C·C')_p` is not applicable as written.

**Repair (binding).** Work in Orevkov’s **contracted** model (Lemma 3.1 normal form `u=x'`, `v={y'}^{mu_l}`, the model in which `mu_t` is defined). After contracting `L_C`, `Phi` is finite of degree `mu_t` at `t∈l'`, the tails are points, and the only curve germs in `Phi^{-1}(A_F-bar)` at `t` are `l'` and the branches of `E-bar_X`. Then `Phi^* b >= mu_l·l' + sum Gamma` (coeff. 1 along each `Gamma` because `E=F^*A_F` is reduced) intersected with `Phi^*L` for a generic line `L` through `p` yields the inequality, using `(l'·Phi^*L)_t = e_t(b·L)_p` and `(Gamma·Phi^*L)_t = deg(Phi|_Gamma)·(b·L)_p`. This is the same model MI Lemma 4.1 already consumes.

**Equality at unibranch points.** Summing the repaired inequality over the `t` over `p` gives `K_p >= sum deg(Phi|_Gamma)`. The right-hand side equals the total degree of the infinite places over `P_b` once those places are identified with the branches of `E-bar_X` at those `t` (after contraction, infinite places over `p` pass through the `t` over `p`). PROP 3.1 then saturates the sum, hence each term. At a cusp, `r_p=1`, so `K_p=a-a_p` is exactly that total degree. At `N=4`, `s_l=1`, one `t` over the unique cusp place.

**Clause (iii), `N=4` node.** N4-PIN: `K_p=0` at double points, hence every `k_t=0`. With `s_l=1`, `e_t=1`, `mu_t=mu_l=2`. No branch of `E-bar_X` at `t` may map to the branch `b` that `l'` covers. The infinite places over the node still sit at those `t` (remaining degree 2) and must map to the other branch. That is the branch-exchange.

FALLACY-v2: the written proof identifies places of `E~-bar` with branches of `E-bar_X` at `t` without stating the dictionary. The repair states it. Each `Gamma` is charged to `k_t` only when `Phi(Gamma)=b(t)`; the `(r_p-1)W` term is declared uncharged.

**Promote** with the contracted-model repair and the dictionary explicit.

---

## 5. B3-E-GENUS and B3-E-NOCROSS — CONFIRMED

Over a branch puncture at `p`, `n_P = a_p + n_infty(P)` with `n_infty(P) >= 1` iff `a_p < a`. Hence `a-n_P <= max(0, a-a_p-1) = max(0,(r_p-1)W+K_p-1)`. Over infinity, `a-n_P <= a-1`. RH `2g-2 = -2a + sum_P(a-n_P)` yields BE:436–440:

```text
2 g(E)  <=  1 - a + sum_p r_p · max(0, (r_p-1)W + K_p - 1).
```

At `N=4` this is `2g <= 2k-1`, hence `g <= k-1` in integers. B3-N4 gives `g = k_odd-1 <= k-1`, attained at `k_odd=k`. The real RH estimate with max ramification at every puncture including infinity is `2g <= 2k-1` and is not attained (infinity is unramified at `N=4`). The integer cap is attained. Nonblocking: BE:445’s “the bound is attained” is the integer reading against B3-N4.

**Closed form, recomputed.** THEOREM PROFILE (B3): `ceil(N/2) <= a <= N-2`, `W=N-a>=2`, `K_c+K_m=a-1`, `K_m <= D_gap=2a-N`, `a_p>=0`. (The comment in `anti.py` writes the strict `N/2 < a`; the loop is the correct closed interval.) The range forces `K_m <= D_gap <= a-2`, so the cap collapses to `2g <= 2W+K_m-3`. Maximising takes `K_m=D_gap=2a-N` (admissible: `K_c=W-1>=1`, `a_{cusp}=D_gap+1>=1`, `a_{mult}=0`) and gives `N-3`, independent of `a`.

Every admissible `(N,a)` for `N=4..20`: max cap equals `N-3`; empty cells none. Spot checks against BE:459–467: `(4,2)->1`, `(5,3)->2`, `(6,3)` and `(6,4)->3`, `(12,6)->9`, `(20,11)` and `(20,18)->17`. All match. `anti.py` prints `g <= (N-3)/2`; same numbers.

**Stronger than stated.** Minimising over `K`-splits gives `2g <= 2W-3 >= 1`. No counting-admissible minimal profile has a negative covering cap. An extra `K=0` node contributes `+2 max(0,W-1) >= +2`.

**Unique gate.** Among the two G-ANTI ingredients, yes. The only counting-side parameter unbounded at fixed `N` is the number of `K_p=0` double points (`sum K_p=a-1` bounds cusps; `r_p W <= N` bounds branch counts). Extra nodes raise the covering cap. A bound on `#`nodes comes from the delta-budget of `A_F-bar`, i.e. MI’s `OPEN[DEG-AF-VS-N]`. It is **not** unique among all `(B3)` instruments: the two OPENs of §7 are other arms. `OPEN[B3-INFINITY-RANK]` is correctly not needed. The plane-curve identity bounds `d` from below given `g`, not from above; that is the same blockage.

**Promote** B3-E-NOCROSS and the unique-gate claim at G-ANTI scope.

---

## 6. WITNESS `E_0` — CONFIRMED as type, GAP on point names

Independent sympy 1.14.0 over `Q`. Producer drivers were not a source.

**Equation.** `x(5)=15`, `y(5)=1`. Resultant of `numer(x-X)`, `numer(y-Y)` in `t` is `-2` times the displayed quintic (content `-2`, one degree-5 factor, LC `72`, primitive parts identical). Total degree 5. `factor_list` over `Q`: one factor. `gcd(f,f_X)=gcd(f,f_Y)=1`: reduced. Leading form `72 X^2 Y^3`.

**Geometric irreducibility.** Four generic fibres (`t_0=6, 1/2, 7, -1`) each have gcd-degree 1. The map `P^1 -> P^2` given by `[n_x d_y : n_y d_x : d_x d_y]` has coordinate-gcd 1. A birational parametrisation over `Q` implies the image is geometrically irreducible.

**Five places at infinity, labels repaired.** Poles at `t=0,1,2,3,4`, all simple (`ord(u)=1` at `t=0,1,2` in `u=1/x`, `w=y/x`; `ord(v)=1` at `t=3,4` in `v=1/y`, `z=x/y`). Homogenisation meets `Z=0` in `72 X^2 Y^3=0`: `[1:0:0]` multiplicity 3, `[0:1:0]` multiplicity 2. Both points are singular (all four partials vanish). The charts BE ran are the right charts. The **names in the prose are swapped**, and `[0:0:1]` is the affine origin:

```text
 actual                                BE:384-390 printed
 t=0,1,2 : [1:0:0], slopes             "[0:1:0]"
           -13/12, -5/3, -7/2
           ordinary triple, delta=3
 t=3,4   : [0:1:0], slope 43/3,        "[0:0:1]"
           Puiseux difference
           109417 v^3/288 - 2233 v^2/72
           contact 2, tacnode, delta=2
```

The coefficient `-2233/72` of `v^2` matches BE:389. `t=∞` maps to the affine origin `(0,0)`, which is smooth (`f_X(0,0)=-6699`, `f_Y(0,0)=332717`). Five places at infinity, not six.

**Unique affine `A_2`.** Pairwise resultants: `gcd` of the three `Res_X` is `c(Y-1)^2`; `gcd` of the three `Res_Y` is `c'(X-15)^2(3X-43)^2`. `solve` on `(f,f_X,f_Y)` returns `{(15,1)}`. `X=43/3` is the vertical asymptote, not an affine singular point: `f_Y(43/3,Y)=30076/9 ≠ 0`. At `(15,1)`,

```text
2-jet = 2(30X-31Y)^2
3-jet = Y(1939 X^2 + 3327 X Y + 32 Y^2)
```

exactly as printed. Remainder of the 3-jet on `30X-31Y` is `(4986289/900)Y^3 ≠ 0`. On the parametrisation: `x-15` and `y-1` both order 2 in `(t-5)`; tangent-killed combination order 3. Semigroup `<2,3>`. Two independent proofs of ordinary `(2,3)` cusp, `delta=1`.

**Injectivity off the poles.** After dividing out `t_1-t_2`, the resultant in `t_2` is `-4466(t_1-5)^2(t_1-4)(t_1-3)`. Complete solution set `{(3,4),(4,3),(5,5)}`. The pair `(5,5)` is the diagonal (cusp ramification, not a failure of injectivity). Off `{0,1,2,3,4}`, the only non-injective pair is the tacnode at infinity.

**Delta budget and `chi_c`.** `3+2+1=6=(5-1)(5-2)/2`. Geometric genus 0; the birational parametrisation lists every place, so no further singularity. Cusp unibranch ⇒ `chi_c(E_0)=2-5=-3=1-4k` at `k=1`. The tuple `(g,n_infty,#affine sings,type)=(0,5,1,(2,3))` is B3-N4’s `k=1`, `k_odd=1` cell.

BE:410–416 types it `REPRESENTATIVE ONLY` and does **not** claim it is `F^{-1}(A_F)` for any Keller map, nor that it admits a degree-2 map onto a one-place-at-infinity rational cuspidal curve. That is the correct carrier reading. The type does not force a large degree (`deg E_0=5` versus `N·deg A_F-bar >= 12` at `N=4`); that is not a degree formula. **Promote** the numerical type with the point names repaired to `[1:0:0]` and `[0:1:0]`.

---

## 7. Charge corrections and the two OPENs

**Places on the dicritical.** At `N=4`, `k=k_odd=1`, B3-N4 gives `n_infty=5`. PROP 3.1 plus HF’s puncture signs split them as BE:257–266: 2 over `∞_{A_F}` (unramified), 1 over the cusp (`a-a_{p_0}=1`), 2 over the two node punctures (odd contact, one place of index 2 each). This split of **places of `E~-bar`** is CONFIRMED. Three of five lie over affine singular points, hence are the candidates to meet `l'`.

The sentence “NOT all five sit on the dicritical. Exactly the places converging to AFFINE points do” (BE:64–70, 643–645) identifies those places with points of `E-bar_X ∩ l`. The two places over `∞_{A_F}` converge to the unique point of `A_F-bar \ A_F` (Lemma A). The dicritical satisfies `Phi(l)=A_F-bar`, so `l \ l'` maps to that point. Those two places may still meet `l` at `l \ l'`. Whether they do is unpinned, and is part of `OPEN[E-INFINITY-SPLICE-DEGREE]`.

**Repair.** Three of five places of `E~-bar` lie over affine punctures and are the candidates to meet `l'`; the other two lie over `L_infty` of the target. Do not assert they fail to meet the compact curve `l`.

**Orbifold BMY.** The charged sentence “orbifold BMY there needs only `(p,q,k,t_i,rho)`, all pinned at `N=4`” is false. The pair `(P^2,(1-1/e)A_F-bar + L_infty)` needs `n=deg A_F-bar` and `A_F-bar · L_infty`. HF Prop 3.1 pins `e=2` on meridians, not a model of the cover over `L_infty`. The dicritical has `(s,mu)=(1,2)` and maps onto `A_F-bar`, not onto `L_infty`.

**Qualification, not a refutation of the OPEN.** The numerical pair `(P^2,(1-1/2)C+L)` has orbifold Chern numbers once `n` and `C·L` are known. What the OPEN correctly names is the justification that they are the Chern numbers of a compactification of the Galois cover.

**OPENs raised.** `OPEN[E-INFINITY-SPLICE-DEGREE]`: `deg E-bar` is not a function of the (B3) type. The floors `deg E-bar >= n_infty(E)` and `(d-1)(d-2)/2 >= g + sum_p a_p delta_p` are floors (at `k=k_odd=1`, `(p,q)=(2,3)` the second is `d>=3`, weaker than `n_infty=5`). BE invents no degree formula and does not use `deg E-bar = N · deg A_F-bar`. The witness realises the type at `d=5`, so the floors are not secretly equalities. `OPEN[ORBIFOLD-BMY-AT-INFINITY]`: well-posed, above. Neither is filled by cap or analogy.

---

## 8. Section 6: Domrina–Orevkov, `N`-uniformity, successor

**Killing lemma — CONFIRMED as a lemma set.** N4-PIN: one dicritical `(s,mu)=(1,2)`. Orevkov’s one-dicritical budget at `N=4` is `mu+corr=3`, so `(mu,corr)=(2,1)`. In DO I this is `n(g~)=2`, `m(g~)=1`, `Deg g~=2` (`do1-mu2-replay`:48–60). Assembly table (`do1-mu2-replay`:715–722): `(1,2)` by campaign Prop 4.1; `(2,1)` by §§2–7 of DO I with named fills; `(3,0)` by campaign Cor 3.8. Integration #7’s `N=4-CHECKED-CLOSED` chain is that mu2 track (REPLAYED-SOUND, five-for-five CONFIRMED) plus Prop 4.1 plus Cor 3.8 plus Domrina II. The (B3) `N=4` object is the middle row. It is not killed by Prop 4.1 or Cor 3.8. It is killed by the lemma **set** §§2–7: census Lemmas 8–9, six-graph assembly, elimination Lemmas 10–15, on Prop 3 / Lemmas 1–5, with the named campaign repairs. There is no single killing lemma; BE’s answer as a set is the right one.

The mechanism is a boundary argument on the dual graph of `X \ A^2`. It does not use `Sing A_F`, `rho`, or `E`. The campaign cage is affine and representation-theoretic. Those halves are disjoint. That correctly explains HF’s “rigid but not empty”.

**Not `N`-uniform — CONFIRMED.** Finiteness of the census is `sum Deg a~ = 4` (DO I formula (9), p. 854; replay (4.1) line 211), yielding the four-element fork list `(D;m,n)=(2;2,1),(3;3,1),(4;4,1),(4;2,2)`. At general `N` the identity is `sum Deg=N`. The determinant package and RH on `F|_{a~}:P^1->P^1` transport; they are the tools, not the kill.

**SUCCESSOR — GAP, not well-posed.** “`E-bar_X · l` with the three (at `N=4`) contact multiplicities against Orevkov’s determinant package” (BE:688–693). `E-bar_X · l` is a weighted count of points. Three of those (at `N=4`, `k=1`) lie on `l'` over `Sing A_F`; the other two places may contribute points of `l \ l'`, unpinned. Orevkov’s package is the dual graph of `X \ A^2`. A curve in `A^2` meeting the boundary at points of `l` adds marked points on an existing vertex, not a new vertex. No identity is stated that would consume those marks and contradict `det L=-1` or `det D_a>1`.

A well-posed successor would name the splice diagram of `(E-bar_X ∪ boundary)` and a specific determinant identity. That is the Neumann/EN test already blocked on `deg E-bar`. At `N=4` the object is already killed by DO I; a successor is for general `N`, where the census is infinite. As written it names two objects from the two disjoint halves and no map between them. The direction “a boundary instrument fed by affine data” is not a theorem.

---

## 9. FALLACY-v2

No new exit price; no `charge_basis` line. `A_F`, `A_F~`, `E`, `E~/E~-bar`, and `l/l'` are kept apart except where E-CHARGE and the dicritical-sitting correction use an unstated dictionary (repaired above). `E_0` is `REPRESENTATIVE`. B3-E-GENUS and the two degree floors are bounds, not equalities. “No crossing” is nonemptiness of a window. Local degree applies only in the contracted model. Parametrisation-to-implicit is a resultant in `t`. `l'` is a label, not a derivative. Affine singular locus via pairwise resultants, complete finite support. The two OPENs stay OPEN; the successor is typed GAP.

---

## 10. Typed verdict block

```text
LANE              B3-E-GEOMETRY-REVIEW
SCOPE             Hostile gate on BE's PROVED-HERE items; Keller, H2, (B3);
                  E = F^{-1}(A_F).  Quasi-homogeneity only where HF local
                  theory is consumed (SCOPE[B3-QH]).

CONFIRMED         E-ETALE         connected finite etale of degree N.
                                  Consumed: Jac F in C^*, geometric degree N,
                                  A_F = Jelonek non-properness set (a curve),
                                  properness over the complement,
                                  proper+quasi-finite => finite, C.
                  E-BMY-VACUITY   kappa-bar invariant; c_2-bar := e(V) scales
                                  by N independently of compactification;
                                  c_1-bar^2 scales by N on log-minimal models
                                  of the normalisation pair.  Log-BMY
                                  upstairs <=> downstairs, all N, all
                                  profiles.  BINDING REPAIR: log-smooth
                                  compactification so K+D is Q-Cartier.
                  PROP 3.1/LOC-1  fibre split; no infinite place over a
                                  smooth point of A_F.
                  COR 3.2         n_infty=(R-1)a+2-2g-sum a_p r_p,
                                  chi_c=a(1-R)+sum a_p; matches B3-N4 at
                                  every (k,k_odd), k<=8.
                                  BINDING REPAIR: g = p_a(E~-bar).
                  E-CHARGE        k_t >= sum deg(Phi|_Gamma) over same-branch
                                  branches at t; equality at unibranch
                                  points.  BINDING REPAIR: Orevkov contracted
                                  model (Phi finite of degree mu_t at t).
                  B3-E-GENUS      2g <= 1-a+sum r_p max(0,(r_p-1)W+K_p-1);
                                  integer cap g<=k-1 attained at N=4.
                  B3-E-NOCROSS    minimal (B3) profile: max cap 2g <= N-3
                                  independent of a; window nonempty at every
                                  N=4..20 (min cap 2W-3 still >=1); no
                                  crossing.  OPEN[DEG-AF-VS-N] is the unique
                                  G-ANTI gate among those two ingredients.
                  WITNESS E_0     rational plane quintic, Q- and C-
                                  irreducible, five places at infinity,
                                  ordinary triple delta=3 at [1:0:0],
                                  tacnode delta=2 at [0:1:0], unique affine
                                  A_2 at (15,1), injective off the poles,
                                  chi_c=-3.  REPRESENTATIVE of the k=1,
                                  k_odd=1 numerical type.  NOT a Keller
                                  preimage.
                  §6 read-off     (mu,corr)=(2,1) is DO I §§2-7 (lemma SET),
                                  matching do1-mu2-replay assembly and
                                  integration #7 N=4-CHECKED-CLOSED.  Not
                                  N-uniform (sum Deg a~ = 4).
                  NO KILL of (B3) at any N.

GAP               printed names of E_0's points at infinity (BE:384-390
                  [0:1:0]/[0:0:1]; actual [1:0:0]/[0:1:0]; charts and
                  deltas are right).
                  "only 3 of 5 sit on the dicritical": the 2+1+2 split of
                  places of E~-bar is right; whether the two places over
                  ∞_{A_F} meet l \ l' is unpinned.
                  SUCCESSOR "E-bar_X · l against Orevkov determinants":
                  no identity consumes the intersection number.

REFUTED           none of the eight PROVED-HERE statements.  The charged
                  sentence "orbifold BMY needs only (p,q,k,t_i,rho)" is
                  false as BE says; that is a correction, not a BE claim.

OPENS (well-posed) OPEN[E-INFINITY-SPLICE-DEGREE]
                   OPEN[ORBIFOLD-BMY-AT-INFINITY]
                   OPEN[DEG-AF-VS-N] re-ranked as the unique G-ANTI gate.

PROMOTE           E-ETALE; E-BMY-VACUITY with the log-smooth repair;
                  PROP 3.1 / LOC-1; COR 3.2 with p_a reading; E-CHARGE
                  with the contracted-model repair; B3-E-GENUS;
                  B3-E-NOCROSS at G-ANTI scope; E_0 as REPRESENTATIVE
                  numerical-type witness with point names repaired; the
                  §6 identification and N-uniformity claim; both OPENs
                  as OPENs; NO KILL.

DO NOT PROMOTE    the successor as a well-posed next lemma;
                  "not on the dicritical" as a statement about
                  E-bar_X ∩ l; the printed [0:0:1]; any kill of (B3);
                  any value of kappa-bar(A^2 \ A_F); any Keller map;
                  deg E-bar; Z(G)=1; case (A); A2 cells.

MEASURED          E_0: resultant = -2 * displayed quintic; factor_list
                  length 1 over Q; gcd(f,f_X)=gcd(f,f_Y)=1; leading
                  72 X^2 Y^3; generic fibres degree 1 at four t_0;
                  P^1->P^2 coord-gcd 1; affine singular locus gcd of
                  three Res_X = c(Y-1)^2, solve {(15,1)}; 2-jet
                  2(30X-31Y)^2, 3-jet remainder (4986289/900) Y^3;
                  param orders (2,2) killed-order 3; Puiseux difference
                  -2233 v^2/72 + O(v^3); injectivity resultant
                  -4466 (t1-5)^2 (t1-4)(t1-3), solutions (3,4),(4,3),(5,5).
                  B3-N4: all 44 cells k<=8, n_infty and chi_c.
                  G-ANTI: every admissible (N,a) for N=4..20, max cap
                  = N-3, min cap = 2W-3 >=1, empty cells none.

computation       sympy 1.14.0 over Q; resultants, not Groebner of
                  (f,f_X,f_Y); integer RH / PROFILE arithmetic.
                  no AWS, no msolve, no jc2-lean, no canonical ledger.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `31710`.
- Body SHA-256:
  `e44c5bb0573baa64fdaadc31625dedcd9f579f7a0303d71f84720e4e6d23e819`.
- Frozen basis: `cb15149a0a7d3aa3fa6a26c017077c9c7ef048d1`.
