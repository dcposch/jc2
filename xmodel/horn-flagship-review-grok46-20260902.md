# Hostile review: HORN-FLAGSHIP — (B3) theorem set and THEOREM HORN-A2

**Reviewer.** grok-4.6 (different-model gate).
**Date.** 2026-09-02.
**Lane.** `HORN-FLAGSHIP-REVIEW`.
**Charge.** Default to refutation. Desk-scale exact reasoning plus sympy 1.14.0 over `Q`. Frozen inputs only. `FALLACY-v2` in force. No `charge_basis` line: no new exit price.

**Headline.** The charge's `(B3)` presentation is false, and the flagship's ZvK correction is the right replacement. B3-DEGREE, B3-CAGE, the local CENTRAL-RANK survival, B3-PUSHOFF, B3-COMPONENT, the `N=4` pinning, and THEOREM HORN-A2 all survive independent replay. Global CENTRAL-RANK is correctly blocked as hypothesis-absent; the stronger sentence "`G` has no centre" is not proved. The "global-abelian or local" slogan is not an exhaustive partition, but no theorem crosses `iota` in the direction NO-PUSHFORWARD forbids.

## Verdict table

| # | Claim | Verdict |
|---|---|---|
| (a) | Charge "`G_{p,q}` + `k` commuting squares" is false; flagship ZvK correction is right | **CONFIRMED** |
| (b) | THEOREM B3-DEGREE, all-degree parity | **CONFIRMED** |
| (c) | THEOREM B3-CAGE, orbit-summed local cage | **CONFIRMED** |
| (d) | CENTRAL-RANK refuted globally; survives per-orbit | **CONFIRMED** as hypothesis-absent globally, and locally under `SCOPE[B3-QH]`. **GAP** on `Z(G)=1` |
| (e) | THEOREM B3-PUSHOFF and THEOREM B3-COMPONENT | **CONFIRMED** under `SCOPE[B3-QH]` |
| (f) | `N=4`: `rho(G)=S_4`; Puiseux `(2\|p,3\|q)` or `(3\|p,2\|q)`; `E` dichotomy | **CONFIRMED** |
| (g) | THEOREM HORN-A2, including chamber II `det = 36 n (c+2e)(c+2e+1)` | **CONFIRMED** |
| — | "Every theorem is global-and-abelian or local" as a partition | **GAP** (third class exists). Forbidden `iota`-crossing: **CONFIRMED** absent |
| — | Chambers I/III empty, Wall B ray, `U<3e-1` resultant | **CONFIRMED** |
| — | T5 / Wall B composition | **CONFIRMED**, scope-clean |

Nonblocking observations in §8. Nothing here closes `(B3)` at any `N`, and the flagship does not claim that it does.

---

## 0. Custody, method, scope

Frozen copies were hashed with `shasum -a 256` **before any reading**. Both match the charge exactly:

```text
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  horn-flagship-opus5-20260902.md
d1b5dc55f850c7b4215ba16a7143a52b96185574ed3c721c44da47b5e427b94b  cell-32-termination-opus5-20260901.md
```

Below: **HF** = the charged flagship, **C32** = CELL-32-TERMINATION. After the charged pair was read, HT/HR and MI/MR were grepped for consumption typing (LEMMA F1, NO-PUSHFORWARD, CENTRAL-RANK, ORBIFOLD-CAGE, CUSP-PARITY, N4-PIN, Lemma A). HR CONFIRMS the HT cusp theorems; MR CONFIRMS N4-PIN and Lemma A. This gate re-derives the group theory and the leading-coefficient calculus; it does not rest on those reviews.

**Method.** Independent ZvK derivation; replay of B3-DEGREE and the orbifold Euler identity; monomial substitution `eta = A Z^e`, `s = S Z^sigma`, `q = Q Z^m`, `r = R Z^n`, `G = C Z^g` in sympy 1.14.0 over `Q`; exact 3x3 determinants; Wall B kernel; resultant of `P(c)` against EQ4 on the EQ1–EQ2 ray. Integer/rational only. C32 T1–T5 remain UNREVIEWED; this gate confirms HF's calculus *from* C32's displays (and the four `e=0` identities), not the derivation of those displays from `O0`–`E3`. No `charge_basis` line.

---

## 1. The presentation — CONFIRMED that the charge is wrong

The research charge (HF's input prompt, restated at HF:97-106) asserts that for `A_F` a quasi-homogeneous cusp plus `k` nodes,

```text
G = pi_1(C^2 \ A_F)  is  G_{p,q}  with k commuting-square relators adjoined.
```

**Independent ZvK.** Let `pr: (x,y) |-> x` be a generic linear projection, `n = deg_y bar A_F`. Zariski–van Kampen presents `G` on meridians `x_1,...,x_n` of a generic fibre, with one braid relation per discriminant value:

* ordinary vertical tangency: local braid `sigma`, relation `x_i = x_j`;
* two smooth branches of contact `t` (`A_{2t-1}`): local braid `sigma^{2t}`, relation `(x_i x_j)^t = (x_j x_i)^t`. This is `[x_i,x_j]=1` if and only if `t=1`;
* quasi-homogeneous cusp `{x^p=y^q}`, `gcd(p,q)=1`: local braid `(sigma_1...sigma_{p-1})^q` on the `p` strands through that fibre, i.e. the `(p,q)` torus-braid relations among *those* `p` generators.

Four independent obstructions kill the charged sentence as a presentation of `G`.

1. **Generator count.** `G_{p,q} = <alpha, beta | alpha^p = beta^q>` is 2-generated. ZvK presents `G` on `n` meridians, and `n` is the degree of a generic projection of `A_F`, unbounded in `(p,q,k)`. The cusp's relators involve only `p` of them.
2. **`iota` is not a presentation map.** The canonical object is `iota: Loc_{p_0} cong G_{p,q} -> G`. Meridians of an irreducible curve are conjugate in `G`, so `iota(Loc)` contains one meridian; conjugators in `G` need not lie in `iota(Loc)`, so `iota` need not be surjective (nor injective: extra global relations can only shrink). Adjoining `k` words to `G_{p,q}` describes a quotient, i.e. the unbanked surjective case.
3. **Vertical tangencies.** The charge omits the `x_i=x_j` relations.
4. **Contact `t >= 2`.** Double points of two smooth branches include tacnodes. The node relator is a commuting square only for `t=1`.

The charge is right about the *local* relators and wrong about the global shape. HF:97-106 is the right replacement. `SCOPE[B3-QH]` (HF:76-81) is correctly typed: MI's "cusp" is any unibranch germ; a general unibranch local group is an iterated-torus-knot group, not treated here. A charitable reading of the charge as "ZvK braids" is a true description of local braids, not of `G cong G_{p,q}/<<k commutators>>`. **CONFIRMED false.**

---

## 2. THEOREM B3-DEGREE — CONFIRMED

> `sgn rho(h) = eps^{deg h}` for every `h in G`, with `eps = sgn rho(m) = (-1)^{W - sum_l s_l}`.

*Replay.* `A_F` irreducible (H2) and LEMMA F1 give `G^{ab} = Z <m>`. The composition `sgn o rho: G -> {+-1}` is a homomorphism to an abelian group, hence factors through `G^{ab}` and is determined by its value on `m`. Cycle type `1^a prod_l mu_l^{s_l}` has `N - #cycles = W - sum_l s_l = sum_l s_l (mu_l - 1)`, so `eps = (-1)^{W - sum_l s_l}`. That is HT CUSP-PARITY with the case-(A) hypothesis deleted: the argument never used `G cong G_{p,q}`, only `G^{ab} = Z`. It contains HT's two identities as the special cases `h = iota(alpha)` (`deg = q`) and `h = iota(beta)` (`deg = p`).

**`deg iota(z) = pq`.** In `G_{p,q}^{ab}`, `alpha |-> q`, `beta |-> p`, `z = alpha^p |-> pq`. The global degree is linking number with `A_F`. A loop in a Milnor ball about `p_0` has the same linking number with the germ as with `A_F`, so `deg(iota(z)) = pq`. Evaluating the global character `sgn o rho` on `iota(z)` is not a forbidden push of local torsion.

LEMMA F1 (HT:97-107): meridians generate `H_1(C^2 \ E)`, and the winding-number map `(f_1,...,f_r): C^2\E -> (C^*)^r` sends them to a basis of `Z^r`. Elementary, and used only for `r=1`. **CONFIRMED.**

---

## 3. THEOREM B3-CAGE — CONFIRMED

Notation as HF:184-197: `A = rho(iota(alpha))`, `B = rho(iota(beta))`, orbits `O_i` of `<A,B>` on the `N` sheets, `kappa_i = ord(rho(z)|_{O_i})`, `M_i = |O_i|/kappa_i`, `M_tot = sum M_i`, `T` = number of orbits, `R_tot = sum r_{O_i}`.

*Euler, per orbit.* `rho(z)` is central in `<A,B>`, hence semiregular on each orbit (the action on `O_i` is transitive by definition of orbit, so HT (C-4) applies orbitwise with no global transitivity). Base orbifold `D^2(p,q)` has `chi^{orb} = 1/p + 1/q - 1`. Degree-`M_i` cover:

```text
(2-2g_i-c_i) - s_i - s_i' + M_i/p + M_i/q  =  M_i(1/p + 1/q - 1),
```

hence `s_i + s_i' = M_i + 2 - 2g_i - c_i`. Kurosh free rank `r_i = 2g_i + c_i - 1` rewrites this as `s_i + s_i' = M_i + 1 - r_i`. Summing over orbits and using `c_A = sum s_i`, `c_B = sum s_i'` gives

```text
(B3-1)   c_A + c_B  =  M_tot + T - R_tot.
```

At `T=1` this is HT's `s+s' = M+2-j` with `j = r+1`. **CONFIRMED.**

(B3-2) is the orbit/component correspondence for the restricted ACS covering of a Milnor ball. (B3-3) is LEMMA B3-LOC: an affine orbit has `|O|=1`, `F` étale so `(E,y) cong (A_F, p_0)` analytically, unibranch, `H_1(B_y \ E) = Z`, hence `r_O = 0`. (B3-4) is HT (C-2)–(C-3) orbitwise: `H_O^{ab} = H_1(U_O)` is torsion-free (local complement of a plane germ), so the cone-order coprimality survives.

`N=4` check (HF:306-313): `A` a transposition and `B` a 3-cycle in `S_{{1,2,3}}` give `c_A=3`, `c_B=2`, `kappa_i=1`, `M_tot=4`, `T=2`, so `R_tot=1`; affine `r=0` forces the size-3 orbit to have `r=1`. Degree-3 cover of `D^2(p,q)` with `A`-cycles `(2,1)` and `B`-cycle `(3)` has `chi^{orb} = chi(Sigma)-3+3/p+3/q = 3(1/p+1/q-1)`, so `chi(Sigma)=0`, annulus, `r=1`. Agrees.

---

## 4. The dichotomy, and CENTRAL-RANK — mixed

HF:108-112: every `(B3)` theorem is either global-and-abelian or strictly local, and none crosses `iota` in the forbidden direction.

**Forbidden crossing: CONFIRMED absent.** B3-DEGREE uses only `G^{ab}`. B3-CAGE and B3-LOC apply HT theorems to `rho o iota: G_{p,q} -> S_N`, a genuine representation of the *local* group. B3-PUSHOFF computes a local word in `pi_1(B_P \ A_F)` and evaluates `rho` on it. That is the allowed direction.

**Partition: GAP.** B3-PUSHOFF's first sentence (fibre of `E° -> A_F°` equals `Fix rho(m)`), B3-COMPONENT, and THEOREM B3-N4 are global covering geometry of `E`, neither abelianisation of `G` nor a theorem inside `Loc_{p_0}`. The slogan is not exhaustive. The load-bearing content — no NO-PUSHFORWARD violation — stands. Nonblocking for (b)–(f).

### 4.1 Global CENTRAL-RANK: CONFIRMED refuted as hypothesis-absent; GAP on `Z(G)=1`

HT CENTRAL-RANK is a theorem about the central extension `1 -> Z_H -> H -> Delta -> 1` with `Z_H <= Z(G_{p,q})` and `Delta <= Z/p * Z/q`. That structure is the Seifert fibration of a cone complement. In `(B3)`, `A_F` is not a cone (it has a multibranch point), so `C^2 \ A_F` does not retract to `S^3 \ T(p,q)`, and `iota(z)` is not a candidate for a global Seifert fibre. The hypothesis of global CENTRAL-RANK is absent. HF:147-149 is the right typing: do not quote it at `(B3)`.

The stronger sentence "`G` has no centre" (HF:42, 147) is **not proved**. Two standard constructions of a centre are absent — the cone's Seifert fibre, and Oka's meridian of a *generic* line at infinity (Lemma A gives one place at infinity, so `L_infty` is not generic) — but "no candidate" is not a vanishing theorem. `G cong Z` would have centre `G`; at `N=4`, Prop 3.1 gives `rho(G)=S_4`, so `G` is nonabelian and any central element lands in `ker rho`, which does not make `Z(G)` trivial. For general `N` even nonabelianness of `G` is not proved in HF. **GAP** on `Z(G)=1`. The refutation of *applying CENTRAL-RANK globally* does not need it.

### 4.2 Local survival: CONFIRMED under `SCOPE[B3-QH]`

LEMMA B3-LOC applies HT CENTRAL-RANK to `H_O <= G_{p,q}`. The five-term sequence needs `H_2(Delta_O)=0` and `Z_H cong Z`, both intact for a subgroup of a torus-knot group. The covering-space identification `H_O^{ab} = H_1(U_O)` is the local ACS covering of a Milnor ball. For an affine orbit, `F` étale plus unibranch gives `r_O = 0`. **CONFIRMED**, and it must not be quoted for a general unibranch germ.

---

## 5. B3-PUSHOFF and B3-COMPONENT — CONFIRMED

**PUSHOFF.** The fibre of the `a`-sheeted cover `E° -> A_F°` over a smooth point `p` is `Fix rho(m_p)`: those are the affine preimages, size `a` by MI control 2 / ACS-1. For a smooth branch `b` at a singular point `P`, a loop `gamma` in `b` bounds a disc inside `b`; a normal push-off of that disc meets `A_F` in the other branches with multiplicity `(b·b')_P` and has `lk(gamma~, b)=0`, so `gamma~ = prod_{b' != b} g_{b'}^{(b·b')_P}` in `pi_1(B_P \ A_F)`. At a double point of contact `t` this is `g_{other}^t`. At a unibranch quasi-homogeneous germ the push-off is a longitude of the link, hence lies in `Z(Loc_P) = <z>`, so `rho(gamma~)` is central in `rho(Loc_P)`. **CONFIRMED** under `SCOPE[B3-QH]`. (Iterated torus knots that are not torus knots have trivial centre in the knot group; that is why the scope flag is load-bearing.)

**COMPONENT.** `E = E° union (E ∩ F^{-1}(Sing A_F))`. Removing finitely many points from an irreducible curve keeps it connected, so components of `E` and of `E°` agree except for merges at the points `y` over singularities, where `F` étale gives `r_P` branches of `E` at `y`. The groupoid generated by the `(2.5.1)`-monodromy on the `a` sheets plus those branch identifications therefore has orbit count `j`. And `j = rank H^{ab}` by F1. **CONFIRMED.** This is the third class of §4: global topology of `E`, not a local `G_{p,q}` theorem and not abelianisation of `G`.

---

## 6. `N=4` rigidity — CONFIRMED

N4-PIN (MI §8.1, CONFIRMED by MR; replayed here from the printed numbers): `a=2`, `W=2`, one dicritical `(1,2)`, generic meridian cycle type `(2,1,1)`, fibre partition `(3,1)` at the cusp with `a_{p_0}=1`, `(2,2)` at each double point with `a_q=0`.

**Prop 3.1.** `A_F` irreducible ⇒ meridians conjugate ⇒ `rho(G)` is generated by the transpositions conjugate to `rho(m)`. A transitive subgroup of `S_4` generated by transpositions has connected transposition graph on 4 vertices, hence is `S_4`. (The transitive subgroups of `S_4` that are not `S_4` contain no generating set of transpositions: `A_4` has none; the standard `D_4` contains at most two transpositions, which generate a Klein four-group; point-stabiliser `S_3` is not transitive on 4 letters.) At `p_0` the orbits are `(3,1)`, so `rho(Loc)` preserves both; generating transpositions lie in the 3-set; transitive there ⇒ `S_3`. At a double point the two meridians are conjugate to `m`, hence transpositions. For `t=1` they commute: equal transpositions give orbits `(2,1,1)`, disjoint give `(2,2)`. The fibre is `(2,2)`, so they are disjoint. For `t>=2`, two transpositions sharing a letter generate `S_3` with product a 3-cycle; `(sigma)^{t} = (sigma^{-1})^{t}` forces `3|t` and orbits `(3,1)`, excluded by `(2,2)`. **CONFIRMED.**

**Prop 3.2.** `rho(z)` is central in `rho(Loc_{p_0}) = S_3`. `Z(S_3)=1`, so `rho(z)=e`. Thus `ord(A)|p`, `ord(B)|q`, coprime, and `<A,B>=S_3`. Elements of `S_3` have orders in `{1,2,3}`; neither generator can be trivial (`S_3` non-cyclic); the only coprime pair generating `S_3` is `{2,3}`. **CONFIRMED.** Independent parity: `deg z = pq`, `rho(z)=e` even, B3-DEGREE gives `eps^{pq}=+1` with `eps = (-1)^{2-1}=-1`, so `pq` even — the weaker half. Agrees.

**THEOREM B3-N4.** `a=2`, so `(2.5.1)` is a homomorphism `pi_1(A_F°) = F_{2k+1} -> Z/2`. Punctures of `A_F~ cong A^1`: one at the cusp, two per double point, one at infinity.

* Cusp: `rho(gamma~) in Z(S_3)=1` ⇒ `eps=0`. Independently, `a_{p_0}=1` and `F` étale give one degree-1 piece at `y_0` plus one more, so the two sheets of `(2.5.1)` do not exchange.
* Double point: `rho(gamma~) = rho(g_{other})^{t_i} = (34)^{t_i}` on `Fix rho(g_{self}) = {3,4}` ⇒ `eps = t_i mod 2`.
* Infinity: product of all local monodromies is `1` in `Z/2`; the others sum to `2 k_odd ≡ 0`, so `eps_infty = 0`.

Branch locus of the compactified degree-2 cover `bar E -> P^1` is the `2 k_odd` punctures with `t_i` odd. Riemann–Hurwitz: `2g-2 = 2(-2) + 2 k_odd`, so `g = k_odd - 1`. For `k_odd=0` there is no connected unramified degree-2 cover of `P^1`, hence `j=2`, both components rational. For `k_odd>=1` the cover is connected, `j=1`, geometric genus `k_odd-1`.

Places at infinity from `chi_c(E)=1-4k` (N4-PIN) and a unibranch cancellation in compactly-supported Euler: `chi_c(E)=2-2g-n_infty` with `g=k_odd-1` gives `n_infty=3+4k-2k_odd`; for `j=2`, `n_1+n_2=3+4k`. Both branches reproduce `chi_c=1-4k`. One affine singular point of `E`, namely `y_0` (`a_{p_0}=1`, `a_q=0`). **CONFIRMED.** CUSP-KILL does not fire: for `k_odd>=1`, `E` has genus `k_odd-1` and `>=5` ends, so is not homeomorphic to `C`. Correctly reported as found.

---

## 7. THEOREM HORN-A2 — CONFIRMED

### 7.1 Displays, `e=0` controls, rows

C32's live-section equations, consumed at their typing. Monomial calculus as HF:411-413, coefficient field `Q(a,b)`, generator order `(Z; eta, s, q, r, G)`. Four `e=0` identities rebuilt from C32 §5.1 and subtracted; all differences are the zero polynomial:

```text
Xi - 4I                     |_{e=0}  =  0
EQ1 - 2*E1d                 |_{e=0}  =  0
EQ2 - E2d                   |_{e=0}  =  0
EQ3 - 2A*(2Z^2 I - t(Z G^2)')|_{e=0}  =  0
```

`u`-grading independently: every family of EQ3 has degree `(3e+1)+u` with `u_r=n+e`, `u_q=m`, `u_s=2sigma-e`, `u_eta=3e-1`, `u_G=e+g-1`, `u_T=2g-e-1`. Simultaneous-top `u_r=u_q=u_s=U` is `m=U`, `n=U-e`, `2sigma=U+e`. Variables `x = a eta_e^3 r_n n`, `y = b eta_e^2 q_m`, `w = a eta_e s_sigma^2 / b`, and in chamber II `c = G_{2e}/(b eta_e^2)`.

EQ3 from T2's Xi families (leaders re-derived by Euler eigenvalues, matching C32:267-275): `[12, 8(e-m), -6(e-sigma)]`. EQ1 from C32 (1.1) plus T1, chamber II eta+G added:

```text
EQ1 :  [ 6(3e+1) ,  4(2e+1)(e-m) ,  -3(e+1)(e-sigma) ]
       + c * [ 9 ,  2(g-2m) ,  (3/2)(e-g+sigma) ].
```

Hand check: `E1` leader `b(1+2e+c) eta_e^2`, `D1` leader `a(1+3e+(3/2)c) eta_e^3`; `q`-terms combine to `4(e-m)(1+2e+c) y`. Matches. EQ2 from C32's displays, extracted on integer cells `(e,U)` in `{1,2,3,4}x{3e,...,5e}` and matched to HF's row including the `c` block `[12, 4(g-m), (3/2)(2e-2g+1)]`. EQ2's pure `G^2` family has Euler factor `(2e-g)` and vanishes in chamber II. Chamber I uses EQ3 eta-type against EQ1/EQ2 G-type; chamber III uses all three eta-type.

### 7.2 Determinants — exact match

This gate's determinants, after substituting `m=U`, `n=U-e`, `sigma=(U+e)/2`:

```text
Chamber III (g<2e, eta-type 3x3) :  det =  72 e n (2e+1)
Chamber I   (g>2e, EQ3 eta / EQ1,EQ2 G-type) :  det =  36 (U + g - 3e)
Chamber II  (g=2e, eta+G added) :  det =  36 n (c + 2e)(c + 2e + 1)
```

HF:483-487, ratio of this gate's det to HF's displayed polynomial is `1` in all three chambers (overall signs absorbed by `n = U-e = -(-U+e)`). **This is the charged comparison: chamber II det = `36 n (c+2e)(c+2e+1)`, confirmed.** Off the walls `c=-2e` and `c=-(2e+1)`, with `n>=1` and `e>=1`, chamber II is empty in the simultaneous-top regime. Pair-minors of EQ3 in chamber III: `-48 e (e-U)`, `36 e (e-U)`, `12 e (e-U)^2`, matching HF:492. EQ3 entries `[12, 8(e-U), -3(e-U)]`, all nonzero for `U != e` (and `U=e` is `n=0`, excluded by T5).

### 7.3 Chamber I/III residues

**III, `U < 3e-1`.** Lone eta-family of EQ3: `12 a b e^2 (2e-1) eta_e^{6}` at degree `6e`, nonzero for `e>=1`.

**III, `U = 3e-1`.** `2sigma=4e-1` odd, `s` excluded. EQ1 and EQ2 are homogeneous in `(x,y)` (EQ2's pure-eta bracket cancels identically). Their 2x2 is `12(20e^3-4e^2+5e+1)`, matching HF:497, positive for `e>=1`. Forces `x=y=0` against EQ3's eta-family. Singles die on `6(3e+1)` and `4(2e+1)(1-2e)`.

**I, `U >= 2g-e`.** `U+g-3e >= 3g-4e > 0` for `g>=2e+1`. Det nonzero.

**I, `U < u_T`.** Lone target `(3a/b)(1+2e+2g) eta_e^2 G_g^2 != 0`.

**I, `U = u_T`.** `2sigma=2g-1` odd. EQ1–EQ2 2x2 is `12(3g-e-1)`, matching HF:507, at least `5e+2>0`. Empty.

### 7.4 Walls

**`c = -2e`.** EQ1 = `(1/2)` EQ3 as rows (identity of the substituted matrices). Rank 2, kernel ray `(x,y,w) = (-n w/4, 0, w)`. Then `y=0` contradicts `q` at the top. EQ4's top on that ray is a nonzero multiple of `n w^2` (this gate's interpolation gives `(3/2) n w^2` up to overall normalisation; HF:517 writes `-3 n w^2 / 4`; both are nonzero for `n,w != 0`). The `{r,s}` pair is killed by EQ4's surviving top `(3/2)(c+2e+2) x w = 3 x w`. Leaders of `E1, D1, C1` at `c=-2e` are `b eta_e^2`, `a eta_e^3`, `d eta_e s_sigma`, all alive. **EMPTY.**

**`c = -(2e+1)`, Wall B.** `E1` leader `b(1+2e+c) eta_e^2` vanishes, so `deg E1 <= 2e-1`. E1-carrying families of EQ1 and EQ4 drop one degree; EQ2 and EQ3 are unaffected. Recomputed rows, confirmed by monomial substitution with `C = -(2e+1) b A^2` (which kills `E1` identically, hence isolates the D1/C1 top of EQ1 that survives the drop in the genuine polynomial case):

```text
EQ3 = [12, -8n, 3n]
EQ1 = [-3,  0,  3n/4]
EQ2 = [ 6,  2-4e-8n,  3e + 9n/2 - 3/2]
```

Rank 2, nullspace exactly `(n/4, 3/4, 1)`. EQ2 is identically zero on that ray. EQ4's surviving top `(3/2) x w - (n/2) y w` vanishes on it. Translating the ray into leaders:

```text
r_n = s_sigma^2 / (4 b eta_e^2),    q_m = 3 a s_sigma^2 / (4 b^2 eta_e),
m = U,  n = U-e,  2 sigma = U+e,  U >= 3e.
```

**SURVIVES.** This is C32's Wall B: `G_{2e} = -b(1+2e) eta_e^2`.

**`U=3e-1` on Wall B.** EQ1 row `[-3, 0]` forces `x=0`, contradiction. Empty.

### 7.5 `U < 3e-1` in chamber II

EQ3's top is the coincident eta/G/target families, independent of `(x,y,w)`:

```text
P(c) := 4 e^2 (2e-1) + 4 c e (2e-1) - c^2 (6e+1) = 0.
```

Re-derived from Xi families (i)+(v) against `(Z eta^2 G^2)'`; matches HF:539. `c=-(2e+1)` is not a root (`P(-(2e+1)) = -32e^3-32e^2-6e-1 != 0`), so this is a different wall from Wall B: it *would* threaten HORN-A2's uniqueness if it survived.

EQ1, EQ2 remain linear in `(x,y,w)` at their own top (the `c`-folded D1/E1/C1 leaders). Their 2x3 matrix has rank 2 off a denominator that is nonzero on `P(c)=0` in the sampled cells. EQ4 on that ray, using the interpolated top

```text
-3 c w x + 4 c x y - 6(e+1) w x + n w y + 4(2e+1) x y
```

(itself matching every simultaneous-top cell in §7.1), produces a rational function of `c`. Resultant against `P` with respect to `c`:

```text
Res_c = -576 n^2 (32 e^3 + 32 e^2 + 6 e + 1) * F(e,n),
```

`F` quadratic in `n`, leading coefficient

```text
1024 e^6 (2e-1)(16 e^2 - 8 e - 1)(18 e^3 + 24 e^2 + 6 e + 1),
```

matching HF:544 exactly (ratio 1). Discriminant

```text
disc_n(F) = (2^6 e^3 K(e))^2 * 2e(2e-1),
```

with `K` the octic `11520 e^8 + 3456 e^7 - 18432 e^6 - 12464 e^5 - 2984 e^4 + 428 e^3 + 292 e^2 + 63 e + 4`, no integer root (`K(1)=-18117`, `K(e)>0` for `e>=2`; rational-root candidates `±1,2,4` fail). `32e^3+32e^2+6e+1` has no positive real root (positive at 0, positive derivative). `2e(2e-1)` is never a square for integer `e>=1`: `gcd(2e,2e-1)=1`, so both factors would be squares; `2e=s^2` forces `s` even, `e=2u^2`, then `2e-1=(2u-1)(2u+1)` is two coprime factors differing by 2, and no two positive squares differ by 2. Hence `disc_n(F)` is never a square, `F` has no rational root in `n`, `Res_c != 0` at every integer cell `e>=1`, `n>=1`. Three exact cells `(e,U)=(2,4),(3,7),(4,10)` were additionally expanded with the full monomial calculus: `P(c)=0` has two real roots, EQ1=EQ2 give a ray, EQ4 on that ray is a nonzero multiple of `w^2 / (a eta_e^3)`. **EMPTY.**

### 7.6 Composition with C32 T5: scope-clean

C32 T5 (C32:583-619): `r'=0` is impossible except possibly in Chamber II under the E1-wall, with `sigma=0`, `E1 != 0`, `2 deg E1 <= max(e-1,1)`. Same live section as HORN-A2 (`G != 0`, `s != 0`, `a b kappa != 0`, `eta != 0`, `e >= 1`). Same variables, same Wall B equation `G_{2e} = -b(1+2e) eta_e^2`. T5 therefore sends the whole `r'=0` section onto the same wall that HORN-A2 names, and licenses `r' != 0`, `n >= 1` off that leftover window.

The two leftovers on the wall are disjoint: T5's window has `r'=0` and `sigma=0`; HORN-A2's pinned ray is the simultaneous-top regime `r' != 0`, `U >= 3e`. HF does not claim the T5 window is empty, and types `OPEN[A2-CELL-32-E1WALL]` accordingly. EQ4 = C32 (2.2), from `O0+E0`, is an extra row beyond C32 §6's three-equation charge; HF discloses this (HF:727-728). This gate confirms it is identity on the Wall B ray and kills `c=-2e`.

C32 T1–T5 are UNREVIEWED. The `e=0` identities and the leader calculus from the printed displays are confirmed here; a gap in T1/T2/T5 as derivations from `O0`–`E3` would propagate. That is a dependency, not a gap *in HF's linear algebra*.

---

## 8. Nonblocking observations

1. HF:517's EQ4 coefficient `-3 n w^2/4` on the `c=-2e` ray disagrees in the constant factor with this gate's interpolation; emptiness is unaffected.
2. Chamber III's `{r,q}` 2x2 is the EQ1–EQ2 minor, not EQ3–EQ1. HF does not name the rows; the displayed polynomial matches EQ1–EQ2, which is the homogeneous pair. The language "forcing `x=y=0` against the nonzero eta-family" is correct for that pair.
3. Drivers left in `/tmp/hornflag` (HF:729) are a custody deviation, not a mathematical one. This gate did not consume them.
4. `SCOPE[B3-QH]` is charged, not banked from MI. Correctly typed as `OPEN[B3-QH]`.
5. `|rho(G)|=24>4` satisfies MI COR 7.2 rather than violating it. Correctly reported.

---

## 9. FALLACY-v2

Flag/place/series: `Loc_{p_0}`, `Loc_{q_i}`, `G`, `G_{p,q}` kept apart; `iota` not crossed forbiddenly. Carrier/attainment: Prop 3.1–3.2, B3-N4, the A2 ray are `REPRESENTATIVE` necessary conditions, not realisation. Floor/attainment: `c_A+c_B <= M_tot+T` is an inequality at general `N`; `N=4` equality is derived and Euler-checked. No exit price, no `charge_basis`. Vanished leaders are branched (Wall A/B, `c=-2e`, both parity exclusions); Wall B rows recomputed, not reused. Primes in §2–§3 are labels, in §4 are `d/dZ`. Monomial map declared and `e=0`-validated. No `sat()`/pole. Charge's presentation replaced rather than derived; `Z(G)=1` returned as GAP, not filled by analogy.

---

## 10. Gate

Promote B3-DEGREE, B3-CAGE, B3-LOC (local CENTRAL-RANK), B3-PUSHOFF, B3-COMPONENT, Prop 3.1, Prop 3.2, THEOREM B3-N4, and THEOREM HORN-A2, at the printed scope including `SCOPE[B3-QH]`. Promote the correction of the charged presentation, and the global-CENTRAL-RANK exclusion as hypothesis-absent. Do **not** promote "`G` has no centre" as a theorem. Do **not** promote an EMPTY window in `N` for `(B3)`. Do **not** close `OPEN[A2-CELL-32]`; the live section collapses to `OPEN[A2-CELL-32-E1WALL]` as typed. C32 T1–T5 remain UNREVIEWED producer input to the A2 calculus.

```text
LANE              HORN-FLAGSHIP-REVIEW
SCOPE             Keller, noninvertible, H2, case (B3); cusp quasi-homogeneous
                  (SCOPE[B3-QH], charged, not banked from MI).

CONFIRMED         charge's G_{p,q}+k commuting squares is false; ZvK correction.
                  B3-DEGREE, B3-CAGE, B3-LOC, B3-PUSHOFF, B3-COMPONENT.
                  Prop 3.1, Prop 3.2, THEOREM B3-N4.
                  HORN-A2: chamber II det = 36 n (c+2e)(c+2e+1) (ratio 1);
                  chambers I/III EMPTY including residues; c=-2e EMPTY;
                  Wall B ray (n/4, 3/4, 1); U<3e-1 Res_c matches HF:543-545
                  including F leading coefficient and disc = (2^6 e^3 K)^2 * 2e(2e-1).
                  T5 composition scope-clean, same Wall B, disjoint leftovers.
                  no forbidden iota-crossing.

GAP               Z(G)=1 as a theorem (hypothesis-absent is the valid global
                  CENTRAL-RANK refutation).  "global-abelian or local" as an
                  exhaustive partition (third class: covering geometry of E).

NOT PROMOTED      any EMPTY window in N for (B3);  Z(G)=1;  closure of
                  OPEN[A2-CELL-32];  C32 T1-T5 (UNREVIEWED dependency);
                  realisability of any admitted (p,q) or of the A2 ray.

MEASURED          four e=0 identities, all 0;  chamber dets ratio 1;
                  Wall B kernel exactly (n/4, 3/4, 1);  Res_c prefactor and
                  F leading coeff ratio 1;  three U<3e-1 cells EQ4 nonzero
                  on the P(c)=0 ray;  K(e) no integer root.

computation       sympy 1.14.0 over Q; monomial substitution as HF:411-413.
                  no AWS, no msolve, no jc2-lean, no canonical ledger.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `27586`.
- Body SHA-256:
  `9c549543c954567680439d7d1f8c729678f0a621f38c219b244c54373672c672`.
- Frozen basis: `73b32fdb60da29fba84990136875de495207ffe1`.
