# Hostile review: D1-SUBTREE — JAC-FIBRE, FRONTIER-EXACT, D1-PIN, D1-STAR, PIN-NOT-CEILING, the integrality filter, condition (15)

**Reviewer.** grok-4.6 (different-model gate). **Date.** 2026-09-02. **Lane.** `D1-SUBTREE-REVIEW`.
Default to refutation. Desk-scale CAS, python 3.14.7 / sympy 1.14.0 over `Q`. Frozen inputs only. `FALLACY-v2` in force. No `charge_basis`. No ledger edit; `jc2-lean` not opened.

**Headline.** The Jacobian identity on a generic `g`-fibre pins the last major disc: per `g`-root the contribution is `m(1-delta_1)/(n+m)`, the `g`-tree below `delta_1` is a star, and `OPEN[D1-SUBTREE]` closes as posed. The pinned value does not grow with `D`, so no ceiling `D<=C(N)` follows. Integrality is a real arithmetic filter and empties no degree. One producer table is wrong: CONTROL 5 printed `N`-sets that ignore the factor `V_2`.

## Verdict table

| # | Claim | Verdict |
|---|---|---|
| (a) | THEOREM JAC-FIBRE, no-log, non-proper | **CONFIRMED**. Reproved. 101+151 driver checks; 3 pairs independent. |
| (b) | FRONTIER-EXACT; `sum_{j≠i} ord_t(tau_i-tau_j)=-delta^0_i` | **CONFIRMED**. Reproved. Closed form on `(y,x+y^k)`. |
| (c) | D1-PIN; `floor(r)-ceiling(r)=(1-delta_r)(-M_r-m)/(n-M_r)`; zero iff `r=1` | **CONFIRMED**. Algebra + 8000 V-skeletons + six Moh rows. CEILING uses Def 5.1(1) at level 1. FLOOR inequality is Moh-free except the evaluation of `lambda_g(delta_1)` by Lemma 5.2. |
| (d) | D1-STAR for both families; Moh "stops" | **CONFIRMED** for the `g`-family and for mixed `f`/`g` contacts. Intra-`f` clustering is free. No contradiction with Moh. He does not print "stops"; Prop 4.6 treats `r=1` as a terminal clause and Prop 5.3/6.1 are stated for `r>=2`. |
| (e) | Drivers `jacfibre.py` / `treecheck.py`; three genuine pairs | **CONFIRMED**. 101/0, 151/0; three independent pairs 52/0. |
| (f) | Six Moh `N` sets; (UNI) filter `D<=120`; no degree emptied | Filter **CONFIRMED** (902893 / 98.98% / 60.04%; per-degree 264/209, 824/419, 1163/795, 60/47, 4104/2390; no degree emptied). Printed CONTROL 5 `N`-sets **REFUTED**. |
| (g) | PIN-NOT-CEILING `min V_2 q`; OPEN[V-FLOOR] from Moh | **CONFIRMED** measured: `3/64` at `D<=120`, `3/112` at `D<=200`. No `V_j` floor from Prop 4.4/4.6/5.3 or search (1)–(13) beyond the Def 5.1(2) window. |
| (h) | (UNI); OPEN[BRANCH-ORBITS] | (UNI) **CONFIRMED** inside one local Galois orbit; **not** a theorem for the whole fibre. Bounded quantity: number of orbits in `{1,...,u}` and the partition of `sum_B V_2(B)<=u`. |
| (i) | Condition (15) vs NOTT (14) | **CONFIRMED**: `(15) => (14)`, strictly stronger. |
| (j) | PLACE LAW | **CONFIRMED** on places of `{g=c_2}`. **GAP** as a PLACE-LEDGER theorem (generic net member). |
| (5) | RADIUS-ORDER is Moh Lemma 5.2 | **CONFIRMED**. Novelty correctly withdrawn. |

---

## 0. Custody, method, scope

Frozen copies hashed with `shasum -a 256` **before any was read**. All five match the charge:

```text
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  d1-subtree-opus5-20260902.md
44223b324641e75be374f09c4b6daead796937d3176d8841844551e2d19c3967  n-on-the-tree-opus5-20260902.md
481d71bfdb9f5237405c671234c751b7c9a3d5339a23f676aa947b7fc69c5ba9  n-on-the-tree-review-grok46-20260902.md
6b8a712344397e1248e4efe230f5fcbeb41ae8b64423de272a77e98ae6b1a241  integration16-coordinator-fable51-20260902.md
3a4744ddb23e6659ad1ab752e7d7b531c8a325f041971b7d72ec1179f11155e1  ideation-20260902T1608Z-sol56.md
```

**CH** = D1-SUBTREE producer. **NOTT** = N-ON-THE-TREE. **NR** = its grok-4.6 review. **INT16** = integration #16. **SOL** = ideation 1608Z. Moh = T.T. Moh, J. reine angew. Math. 340 (1983) 140–212. Journal page `P` is PDF page `P-139`.

```text
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  refs/moh1983_jram340_configurations_of_roots.pdf
b6a369146240dbd36107907ebfb63ab2fc602abb524151d6ab31d39e5bc10722  box/depth-drivers-20260902/moh.txt
3022020435c86b62ecd28df8d28d1bdf9ab4e361828c028b913ba8aae3f11a39  box/moh_skeleton_N.py
574f2f4498be8aef0457d17bbe6da4e3d80719f0fcd0f87c470d5864e0406eea  jacfibre.py
27a30dd7708556113a1c88d6f5188508cd250db58b41bf3aa7800305ff2b5a62  treecheck.py
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  d1floor.py
e2b4d616a6ccbd771f1eb8c1b9e37ffaf50a46e278a529c1e05c5de948fda313  runall.py
e7d7d2e6f108f7a50392f530f7f561c30685dd17c8cfeed3d01e57ce97865b28  general.py
cb6cebd1c27accc57b084c5d07635091a072b51caef8f4cf7b1208051eac8ef8  runall.log
a01c2cc925cce7282e47d0d2b04498c47b9b6c2ba58d1d560b4b5e1be8619a7d  general.log
```

Pages rendered at 160 dpi and read as images: 150 (Ω-symmetry), 151 (Lemma 2.1, both displays), 164 (Prop 4.1), 170–171 (Prop 4.6, `r=1` clause), 177–179 (Lemma 5.2, Def 5.1), 180 (Prop 5.3), 190–191 (Prop 6.1). Reproofs of `(star)`, FRONTIER-EXACT, the D1-PIN gap, and D1-STAR; sympy over `Q` on three automorphisms not imported from `jacfibre.py`; Fractions on Def 5.1(3)/Lemma 5.2 for six Moh rows and 8000 census skeletons; (UNI) filter at `D<=120`; floors at `D<=120` and `[101,200]`; knapsack at `D=80` only. No Groebner, no AWS, no `jc2-lean`, no ledger edit. No exit price.

Consumed at INT16 PROMOTED: CONTACT-DEFICIENCY (monic GEN), FRONTIER-N, RADIUS-ORDER (`M_s=n-2`), DETECTOR-NULL, N-CEILING as an **upper** bound, NU-TWO, MOH-SHARP-2 arithmetic. **Not consumed:** case (A), A2, `Z(G)=1`, RAMIFICATION-FLOOR's place identification. Six integers kept apart: campaign `N`; Moh `n=deg_y g=D`; `m=deg_y f`; `K=gcd(m,n)`; exponent `d` in `l(f)=alpha H^d`; Moh's `d_i`. SOL §2 (SD1)–(SD6) and `box/exactn-drivers-20260902/dictionary.py` (D1)–(D3) write the same `(star)` independently — a cross-check, not a proof.

---

## 1. Item (a) — THEOREM JAC-FIBRE

**CONFIRMED.** PROMOTE the identity, including the no-log step and the non-proper split. Repair: write the Puiseux-field exclusion of `ord F'=-1` from a constant term explicitly (CH folds it into "char 0" and `a_0` subtraction).

Let `f,g in C[x,y]` be monic in `y`, `F` dominant, `J=[f,g]`. Put `t=x^{-1}`, `ord=ord_t`, so `ord x=-1`. Fix generic `c_2`, let `tau in C<<t>>` be any root of `g-c_2` (squarefree: étale, or generic `c_2`). Write `F(t)=f(t^{-1},tau(t))`, `G(t)=g(t^{-1},tau(t))=c_2`. Then `G'=0` and `g_y(tau)≠0` (`dg` never vanishes when `J≠0`) give `tau'=g_x t^{-2}/g_y`. Substitute into `F'=-f_x t^{-2}+f_y tau'`:

```text
F'(t) · g_y(t^{-1},tau(t))  =  - t^{-2} J(t^{-1},tau(t)).          (star)
```

This is an identity in the Puiseux field. Let `a_0` be the coefficient of `t^0` in `F`, and put `k=ord_t(F-a_0)`. Then `k≠0` whenever `F` is nonconstant (a branch on which both `f` and `g` are constant is a point). In characteristic 0 the leading term `a_k t^k` differentiates to `k a_k t^{k-1}`, so `ord F'=k-1`. Taking `ord` in `(star)` yields

```text
ord_t(F-a_0) + ord_t g_y(tau)  =  -1 + ord_t J(tau).              (JF)
```

**No-log.** A Puiseux series has no logarithm. The constant term differentiates to 0, not to `c t^{-1}`. Equivalently: if `ord F'=-1` with `F` of order 0, integrating `(star)` would produce `c log t`, contradicting `F in C<<t>>`. After `a_0` is stripped, `k≠0`, so this case is excluded. It is exactly `delta^0=1` in the contact reading of §2 (`ord g_y=-delta^0` and `(JF)` with `J` a unit would force `ord(F-a_0)=0`). CH:213 states `ord F'=ord(F-a_0)-1` (char 0) without naming the residue. Repair, not a hole: the identity lives in `C<<t>>`.

**Keller, proper.** `ord J=0` on every branch. If `ord F<0` then `a_0=0` and `ord_t f(tau)+ord_t g_y(tau)=-1`.

**Non-proper.** If `ord F>=0` then `ord(F-a_0)>0`, so `(JF)` gives `delta^0=1+ord(F-a_0)>1` (Keller). The contribution to `N` is `(1-delta^0)^+=0`. No genuine noninvertible Keller pair exists to test this empirically; CONTROL T5 tests the non-Keller analogue (`delta^0=4/3,9/4,2,4/3`, naive sum `0`, `N` recovered by `1-delta^0-ord J` when `ord J` is single-valued). The argument is the identity, not the automorphism sample.

Monicity of `g-c_2` in `y` gives `g_y(tau_i)=prod_{j≠i}(tau_i-tau_j)`, hence for a proper Keller branch `-ord_t f(tau_i)=1+sum_{j≠i} ord_t(tau_i-tau_j)`. The `d/dx` form (SOL SD1; dictionary D1) is the same identity: `dt/dx=-t^2` so `dF/dx=J/g_y`.

Rerun: `jacfibre.py` 101/0 (4.2 s). CONTROL B: `ord(f g_y)=-j=-1+ord J` on all 16 rows, and `=-1` iff `j=1`. CONTROL C: four non-Keller two-tower rows, general law holds, Keller value `-1` on none. Three independent automorphisms (§5): every branch has `ord(f g_y)=-1`.

Lemma 2.1 (p.151, both displays) is the Keller condition on the `eta=g^{-1/n}` expansion: `f_i in k` for `i<n-1` and `deg_x f_{n-1}=1`. Its only tree consequence is `M_i<=n-1`. CH:295–303 is right: Lemma 2.1 is the wrong variable for the sub-tree of `D_1`; `(star)` is the `t`-adic identity.

---

## 2. Item (b) — FRONTIER-EXACT and the contact formula

**CONFIRMED.** PROMOTE `N=sum_rho (1-delta^0_rho)^+` for Keller pairs in the gauge, generic `c_2`; equivalently `lambda_f(delta^0)=delta^0-1` at every frontier with `delta^0<1`, and `delta^0>=1` iff the branch is non-proper.

Let `Lambda(delta)=sum_j min(delta, ord(tau_i-tau_j))` along `tau_i`'s path (self-term `=delta`). For `delta<delta^0` one has `lambda_g^{tau}(delta)<0`, so `Lambda(delta)=ord_t((g-c_2)(sigma_delta))=lambda_g^{tau}(delta)`. Continuity: `Lambda(delta^0)=0`. Generic `c_2` makes the leading form of the frontier ball have simple roots (FRONTIER-N, INT16 PROMOTED): no two shifted roots have contact `>delta^0`. Hence `min(delta^0, ord(tau_i-tau_j))=ord(tau_i-tau_j)` for `j≠i`, and

```text
Lambda(delta^0)  =  delta^0 + sum_{j≠i} ord_t(tau_i-tau_j)  =  0,
```

which is the charged contact formula `sum_{j≠i} ord_t(tau_i-tau_j)=-delta^0_i`. Combined with `(ii)` of §1: `-ord_t f(tau_i)=1-delta^0_i` on every proper branch, and `(1-delta^0)^+=0` on every non-proper branch. CONTACT-DEFICIENCY (monic, generic `(c_1,c_2)`) then gives `N=sum_i (1-delta^0_i)^+`. Combined with FRONTIER-N, `lambda_f(delta^0)=delta^0-1` exactly at every proper frontier.

The formula does **not** require the `g`-roots to separate at `delta^0` itself. It requires only that no contact exceed `delta^0`, which is the definition of the frontier. D1-STAR will put the `g`-splitting at `delta_1<delta^0`; the contact identity still holds (the self-term is `delta^0`, the off-diagonal sum is `-delta^0`).

Closed form, `(f,g)=(y,x+y^k)`: `tau_i=zeta^i (c_2-x)^{1/k}`, `ord_t(tau_i-tau_j)=-1/k` for `j≠i` (`k-1` terms), sum `=-(k-1)/k`. Frontier `delta^0=(k-1)/k`. Check. Independent pairs in §5: `Lambda(delta^0)=0` and the averaged off-diagonal equals `-delta^0` on all three.

CH:253 inverts NOTT's reading: extra `g`-contact *lowers* `delta^0` and *raises* `1-delta^0`. That sign is right. Extra `f`/`g` contact below `delta_1` is not free, because `lambda_f(delta^0)=delta^0-1` is forced.

---

## 3. Item (c) — D1-PIN

**CONFIRMED.** PROMOTE the coincidence at `r=1` and the closed gap. State the Moh inputs exactly.

Lemma 5.2 (p.177–179, image). `L<=M_r<...<M_s<n-1`, `V_i(n-M_i)>d_i`,

```text
((n-L)/d_r) lambda^*  =  -1 + delta^* .
```

Read at `L=M_r`, `delta^*=delta_r`. Prop 6.1's proof (p.191, first computation) pushes this to `g` by `ord g(sigma)=(n/d_r) lambda^*`, giving

```text
lambda_g(delta_r)  =  n(delta_r-1)/(n-M_r).
```

NU-TWO has `M_s=n-2`, so `n-M_s-1=1`; this is NR's RADIUS-ORDER, now identified as Moh's own lemma (item (5) below). At `r=1`, `M_1=-m`, `lambda_g(delta_1)=-n(1-delta_1)/(n+m)<0`.

Def 5.1(1) (p.179, image): in `D_i` one has `(n/d_{i+1})V_{i+1}` roots of `g` and `(-mu_j/d_{i+1})V_{i+1}` roots of `T_j^psi`. With `-mu_1=m` this is `b_i/a_i=m/n`, hence `lambda_f(delta_r)=(m/n)lambda_g(delta_r)` along the major tower. At `i=1`: `a_1=e V_2`, `b_1=d V_2`.

**FLOOR.** `c_rho=1-delta^0_rho` (FRONTIER-EXACT). Along any path the self-term of `lambda_g` contributes slope 1, so the slope is `>=1` at every level (Moh-free: it is the definition of `lambda_g`). From `lambda_g(delta_1)<0` one therefore reaches 0 by radius at most `-lambda_g(delta_1)`, i.e. `delta^0<=delta_1-lambda_g(delta_1)`, hence

```text
c_rho  >=  (1-delta_1)+lambda_g(delta_1)  =  m(1-delta_1)/(n+m)
```

once Lemma 5.2 evaluates `lambda_g(delta_1)`. The *inequality* `c_rho>=(1-delta_1)+lambda_g(delta_1)` uses JAC-FIBRE and slope `>=1` only. The closed value uses Lemma 5.2.

**CEILING.** `lambda_f` is nondecreasing, so `c_rho=-lambda_f(delta^0)<=-lambda_f(delta_1)`. Def 5.1(1) at **level 1** (and only there, for the numerical coincidence) gives `-lambda_f(delta_1)=-(m/n)lambda_g(delta_1)=m(1-delta_1)/(n+m)`.

**Gap.** For a general tower level,

```text
floor(r)    = (1-delta_r)+lambda_g(delta_r)           = (1-delta_r)(-M_r)/(n-M_r),
ceiling(r)  = -(m/n)lambda_g(delta_r)                 = m(1-delta_r)/(n-M_r),
floor-ceiling = (1-delta_r)(-M_r-m)/(n-M_r).
```

`M_1=-m<M_2<...<M_s=n-2` (Moh search (1),(2); Def 5.1), and Lemma 5.2 gives `delta_r<1`, `n-M_r>0`. The gap vanishes iff `M_r=-m` iff `r=1`, and is strictly negative for `r>=2`. Verified on 8000 census V-skeletons (`n<=120`) and on all six Moh rows: equality at `r=1`, never at `r>=2`.

Hence at every bottom-major disc, every `g`-root contributes exactly `c_rho=m(1-delta_1)/(n+m)=(1-delta_1)d/(d+e)`, and

```text
N  =  sum_B a_1(B)·(1-delta_1(B))·d/(d+e)  =  sum_B V_2(B)·q(B),
q  = (1-delta_1)de/(d+e)  =  deK prod_{j=2}^{s} [V_j(n-M_j)-d_j]/[V_j(n-M_{j-1})-d_j].
```

The product form is Def 5.1(3) with `n-M_1=K(d+e)` and `n-M_s-1=1`. Disjointness of bottom-major discs inside the unique major child `D_{s-1}` of the root ball (NU-TWO) gives `sum_B a_1(B)<=a_{s-1}=u e`, i.e. `sum_B V_2(B)<=u`. Then `N<=u q=U`: NOTT's N-CEILING is attained when the discs exhaust `D_{s-1}`, and is otherwise the same formula with `u` replaced by `sum V_2(B)`.

**Moh inputs, as charged.**

- CEILING half: Def 5.1(1) at level 1 (proportionality `lambda_f=(m/n)lambda_g` at `delta_1`) plus `lambda_f` nondecreasing. If Def 5.1(1) failed, the ceiling would fail, the floor would survive, and D1-STAR would be lost. CH DISCLOSURE (2) is correct. Independently verified on automorphisms (CONTROL T / §5), which sit outside Def 5.1(3) but still have `b/a=m/n` at the intrinsic `delta_1`.
- FLOOR half: JAC-FIBRE + slope `>=1` is Moh-free. The closed number `m(1-delta_1)/(n+m)` uses Lemma 5.2.

Slogan repair: `N` is determined by the **bottom-disc `V`-packet**, not by the Moh group `(n,m,M_*,V_s)` alone. Different lower-`V` data give different `q`. That residue is OPEN[BRANCH-ORBITS].

---

## 4. Item (d) — D1-STAR, both families, and Moh

**CONFIRMED** for the `g`-roots and for mixed contacts. **Not** a star of the `f`-family among themselves. **No contradiction** with Moh.

Equality in both chains of D1-PIN forces:

- (a) slope of `lambda_g` exactly 1 on `[delta_1,delta^0]`: no other `g`-root accompanies `rho` below `delta_1`. The `a_1=e V_2` roots of `g` in `D_1` separate pairwise at exactly `delta_1`.
- (b) `lambda_f` constant on `[delta_1,delta^0]`: no `f`-root follows `rho` below `delta_1`.
- (c) `delta^0=delta_1+n(1-delta_1)/(n+m)` is the same for every `g`-root in the disc.
- (d) the leading form of `g` at `sigma_1` has `a_1` distinct simple roots.

The `b_1` roots of `f` may still cluster with each other (invisible to `N`; CH:377–378). "Both root families" therefore splits: **yes** for `g`; **no** for intra-`f`. Mixed `f`/`g` contacts below `delta_1` are forbidden.

**Moh does not print "stops".** What he prints:

- Prop 5.3, p.180: "Suppose that `g(x,y)` is monic in `y` with `y`-degree `n>1` and **for `r>=2`** a tower of major discs `D_s ⊇ ... ⊇ D_r` is constructed." The conclusion produces `D_{r-1}` and asserts the extended tower is again major.
- Prop 6.1, p.190–191: same `r>=2`, and the **minor** window `d_r/(n-M_r)>=V_r>=1`.
- Prop 4.6, p.170: "Then we have, **if `r>=2`**, the following: [detector + `q(pi)` has all distinct roots, all roots of `p` are roots of `q`, `p` is not a power of `q`]. **Moreover if `r=1`** then `g_sigma(pi)` and `T_{1,sigma}^psi(pi)` satisfy `D(n,-M_1,g_sigma,T_{1,sigma}^psi)=` nonzero constant."

The `r=1` clause is a different, terminal conclusion (only `D≠0`, i.e. not a detector at the general point). It does **not** claim that `p(pi)` has simple roots, and it does not produce a disc `D_0`. Def 5.1 is introduced (p.179) under "for some `r>=2` we identify a tower". There is no `M_0`. That is the halt.

D1-STAR does not contradict this. It supplies a Jacobian reason why a further major step would be empty of `g`-clusters: after pairwise separation the subdiscs are singletons, and a singleton with `V_1=1` cannot satisfy Def 5.1(1) at a nonexistent level 0 (`(m/n)·1=d/e` is not an integer). Formally "major" under Theorem (5) at `r=1` (`#roots<=n/(n+m)<1` never holds for a nonempty disc), unable to extend.

Wording repair: there **is** something below `delta_1` — a ray of length `-lambda_g(delta_1)` on which `lambda_g` climbs to 0 with slope 1. "Nothing below" means no further `g`-branching. The frontier is strictly later: `delta^0=delta_1-lambda_g(delta_1)>delta_1`.

Prop 4.6 at `r=1` does not already give (d). OPEN[STAR-REALISABILITY] is well-posed: a forced repeated root of the level-1 leading form would contradict D1-STAR and kill the skeleton. Bounded quantity: the multiplicity partition of `e V_2` at `sigma_1`. Leave OPEN.

CONTROL T (rerun): `n=8` automorphisms split `2+2+2+2` at `delta_1=5/8`; below it, slope of `lambda_g` is 1 and `lambda_f` is constant. Independent pair 2 (`m=2,n=4`): `delta_1=1/4`, `delta^0=3/4`, same star.

---

## 5. Item (e) — drivers and three genuine pairs

**CONFIRMED.** Hashes match CH. Rerun, fail-closed:

```text
jacfibre.py   101 checks, 0 failures, 4.2 s
treecheck.py  151 checks, 0 failures, 2.9 s
```

Independent of both drivers (own Newton polygon, own three polynomials):

```text
pair                         m  n  N   delta^0  delta_1  floor
(y, x+y**5)                  1  5  1     4/5     -1/5     1/5
Jung (x,y+x^2) then (x+y^2,y)  2  4  1     3/4      1/4     1/4
Jung (x,y+x^2) then (x+y^3,y)  2  6  1     5/6      1/3     1/6
```

52 checks, 0 failures: JAC-FIBRE on every branch; complementary multisets `{1-delta^0}={-ord f}`; `N=sum(1-delta^0)^+`; `Lambda(delta^0)=0`; contact average `-delta^0`; intrinsic Lemma 5.2; floor `=` ceiling; proportionality at `delta_1`; D1-STAR (a) and (b). Closed-form contact on `(y,x+y^k)` for `k=2..6`.

CH DISCLOSURE (1) stands: these are polynomial automorphisms (`s=1`, `M_s=n-1`), outside Def 5.1(3). They test JAC-FIBRE, FRONTIER-EXACT, the intrinsic `delta_1`, the coincidence, and D1-STAR. They do not test the numerical `delta_i` of a `s>=3` tower; that is the census / Moh rows.

Negative controls remain load-bearing. CONTROL B fails the Keller value `-1` exactly off `j=1`, quantitatively. CONTROL T5: `N=sum(1-delta^0)^+` holds iff Keller, on four non-Keller rows.

---

## 6. Item (f) — Moh survivor `N` sets and the (UNI) filter

**Filter numbers CONFIRMED. Printed CONTROL 5 `N`-sets REFUTED. No degree emptied CONFIRMED.**

`d1floor.achievable` implements (UNI) correctly: `N=k V_2 q` with `k V_2<=u` and `N in Z`. CONTROL 5 **prints a different formula**, `N=k·numerator(q)` for `k=1..floor(u/den(q))`, which is `N=t q` for `den(q)|t<=u` and **drops `V_2`**. That check is display-only: the only `check()` in CONTROL 5 is `U=u q`. The 232 384 skeleton controls therefore did not catch it.

Correct (UNI) sets for the six published rows, versus CH:522–528:

```text
row                     u  V2    q    CONTROL 5 print     achievable()   H2
(64,48)                12   3   3/4   3,6,9               {9}            {9}
(84,56) M2=64,V2=2     21   2   2/7   2,4,6               {4}            {4}
(84,56) M2=72,V2=5     21   5   1/2   1,2,...,10          {5,10}         {5,10}
(75,50) V2=3           20   3   3/5   3,6,9,12            {9}            {9}
(75,50) V2=2           20   2   2/5   2,4,6,8             {4,8}          {4,8}
(99,66)                24   8   2/3   2,4,...,16          {16}           {16}
```

All six sets are nonempty and all meet `[4,16]`. The qualitative claim "Moh's six survivor rows all admit an integer `N`" **survives**. The sentences "pinned to `N in {4,6}`" for `(84,56)` `M_2=64` and "to `N in {6,9}`" for `(64,48)` (CH:531) are **false**; the (UNI) values are `{4}` and `{9}`. Repair: print `achievable(S)`, not `k*p`.

(UNI) filter rerun, one core, same enumerator, `D<=120` complete:

```text
V-assignments 902893 : no integer N>=2     891820 (98.77%)
                       no integer N in [4,16]  893706 (98.98%)
groups        10637  : every assignment dead, uncond  5864 (55.13%)
                                              H2     6386 (60.04%)
per degree (groups / H2-killed)
  105: 264/209   108: 824/419   112: 1163/795   117: 60/47   120: 4104/2390
MOH-SHARP-2 slice {105,108,112,117,120}:
  assignments 655892, H2-killed 650126 (99.12%)
  groups 6415, H2-killed 3860 (60.17%), uncond 3494 (54.47%)
degrees D with every group killed: NONE
```

Unit match to `runall.log` (hash above) and to CH:544–553. Census calibration: 3975 groups at `D<=100` (sum of the per-degree floors 48–100). No `(B2)`/`(B3)` cell dies: a campaign cell `(N,D)` dies only if every skeleton at that `D` fails for that `N`, and none does.

**General knapsack `D in [80,100]`.** Does not fit in 15 min. `D=80` alone (496 groups) took 651.7 s: killed 132 (26.61%), capped/UNDECIDED 76 (counted as surviving). `[48,79]` was not rerun; the hashed `general.log` gives 179/725 = 24.7% killed, 46 capped, and the same code path was just exercised at `D=80`. `D=96` (1113 groups) would exceed the remaining budget. Report `D=80` as the `[80,100]` sample: kill rate comparable to `[48,79]`, no degree emptied, cap still a floor on the true kill.

---

## 7. Item (g) — PIN-NOT-CEILING and OPEN[V-FLOOR]

**CONFIRMED** as measured. PROMOTE the statement that the pinned floor does not yield `D<=C(N)`. Leave OPEN[V-FLOOR].

Rerun of the hypothesis-free floor `L=min V_2 q` over branch data:

```text
D<=120 complete     10637 groups   min L = 3/64  = 0.04688   L>16 kills: 0   emptied: NONE
D in [101,200]     116666 groups   min L = 3/112 = 0.02679   L>16 kills: 0   emptied: NONE
```

Per-degree `min L` at the MOH-SHARP-2 degrees: `105: 3/46`, `108: 3/64`, `112: 1/12`, `117: 1/18`, `120: 3/64`. At `D=180`: `3/112`; at `D=200`: `1/20`. The minimum does not increase with `D` on the range run. Since the only lower bound the boundary supplies is `N>=L` and `L` stays below 1, no inequality `D<=C(N)` follows, for any `C`. The obstruction is as CH states: `V_2=1` is in the Def 5.1(2) window whenever `d_2/(n-M_2)<1`, and `q` is a product of `s-1<=6` factors each `<1`.

**OPEN[V-FLOOR], from Moh, as charged.** Bounded quantity: the integers `V_j` in `(d_j/(n-M_j), V_{j+1} d_j/d_{j+1}]` for `j=2..s` at a degree-minimal counterexample; equivalently `q in (0, de(K-1)/(d+e))`. Prop 4.4 is non-splitting (powers of a linear form). Prop 4.6 takes `v` as an *input* and, at `r=1`, concludes only `D≠0`. Prop 5.3 extends the tower inside the Def 5.1(2) window already. Search (1)–(13) pin `M_1=-m`, `M_s=n-2`, the `d`-chain, and (7)–(13) restrict `V` by roots of unity rather than forcing `V_2=Omega(K)`. Nothing here gives `q=Omega(1)`. Leave OPEN.

---

## 8. Item (h) — (UNI) and OPEN[BRANCH-ORBITS]

**(UNI) is correctly argued inside one local orbit, and is a hypothesis globally.** PROMOTE the naming; do not promote "one orbit at a counterexample".

The Galois group of `C((t))^{alg}/C((t))` acts on Puiseux roots by rotating fractional powers. It is an isometry of the `t`-adic metric, so it permutes discs of a given radius and preserves `(a_1,delta_1)`. Within one orbit of the splitting field of `g-c_2` over `C((t))`, the lower-`V` datum is constant. That is (UNI) on an orbit.

It is **not** a theorem that the fibre has a single orbit of bottom-major discs. Distinct radii, or same-radius clusters whose residue coefficients are not in one cyclotomic orbit of the splitting field, give several orbits. Moh p.150 does not settle this. Quote, image: "Due to the existence of the automorphisms `Omega_i`, the tree data associated with the configuration of the roots of the equation (1) over `k[x]((eta))` are completely symmetric." The `Omega_i` are `eta |-> omega^i eta` on the **`eta`-adic** expansion of the curve `(f,g)` over `k(x)`. Different Galois group, different tree. CH:654–655 is right to refuse the import.

**OPEN[BRANCH-ORBITS].** Bounded quantity: the number of Galois orbits of bottom-major discs, an integer in `{1,2,...,u}`, together with the partition of `sum_B V_2(B)<=u` among them. Number of discs `<=u` because each disc has `a_1=e V_2>=e` roots (`V_2>=1`) and the discs are disjoint in a pool of `a_{s-1}=u e` roots. (UNI) — one orbit — turns a 24.7% group kill (`[48,79]`, hashed log) into a 60.04% group kill (`D<=120`). The hypothesis-free number is the operative one (CH DISCLOSURE (4)).

---

## 9. Item (i) — condition (15) versus NOTT (14)

**CONFIRMED.** PROMOTE (15) as a strictly stronger search condition containing (14).

NOTT (14) (NOTT:563–566): `u d e (1-delta_1)/(d+e)>=2` (unconditional), `>=4` under H2. That is `U=u q>=2` for one tower, or `U_rob>=2` branch-robustly.

CH (15): `q=deK prod_{j>=2} P_j/Q_j` must admit `sum_B V_2(B) q(B)` integral and `>=2`, with `sum_B V_2(B)<=u`.

Any packet satisfying (15) has `2<=N=sum V_2 q<=u·max q=U_rob`, hence `U_rob>=2`, hence (14). The converse is false: `U>=2` does not make a combination integral. Containment is `(15)=> (14)`; (15) is strictly stronger. (15) is the general (no-(UNI)) condition; (UNI) specialises it to `k V_2 q in Z`. OPEN[MOH-14] (is (14) implied by Moh (7)–(13)?) remains open and is not absorbed: (15) is a new test, not an answer to that question.

---

## 10. Item (j) — PLACE LAW

**CONFIRMED** as an identity on the places at infinity of the compactified curve `{g=c_2}`. **GAP** as a theorem of PLACE-LEDGER. Do not promote the identification.

On `{g=c_2}¯`, a place `gamma` at `x=infty` is a Galois orbit of `nu_gamma` Puiseux branches `tau`. The pole order of `f` along `gamma` is `-ord_s f=nu_gamma·(-ord_t f)`. For a proper branch FRONTIER-EXACT plus D1-PIN give `-ord_t f=(1-delta_1)d/(d+e)`, hence

```text
m_gamma  =  nu_gamma · (1-delta_1) d/(d+e)
```

constant on the proper places of one bottom-major disc, and `N=sum m_gamma` is the degree of the pole divisor of `f` on `{g=c_2}¯` (equal to `deg(f|{g=c_2})`). That is the PLACE LAW on this curve.

PLACE-LEDGER (INT15 PROMOTED) is a sum over places at infinity of a **generic net member** `alpha f+beta g=0`: `nu_gamma=I(gamma,L_infty)`, `m_gamma=` pole order of `P`, `D=sum nu`, `N=sum m`. A generic net member is not `{g=c_2}`. NR already refused RAMIFICATION-FLOOR's identification of proper places with bottom-major discs. The same refusal applies here. FALLACY-v2: do not identify a place of `{g=c_2}`, a place of a generic net member, and a cover series.

Repair: state the law on `{g=c_2}`. Then `nu_gamma/m_gamma=(d+e)/((1-delta_1)d)` is an exact ratio on those places, so a bound on `nu` is a bound on `m` and does not open a `T<=sum h(m_gamma)` ceiling. OPEN[NU-BOUND-AT-A-PLACE] remains a ratio on `{g=c_2}`, not a PLACE-LEDGER theorem.

---

## 11. RADIUS-ORDER is Lemma 5.2; DETECTOR-NULL's second proof

**CONFIRMED.** NOTT's "THEOREM RADIUS-ORDER (new)" is Moh Lemma 5.2, reused as the last equality in the proof of Prop 6.1 (p.191: "the reader is referred to Lemma 5.2"). The identity and NR's 242 099/0 check stand; novelty is withdrawn. D1-PIN may rest on a published lemma.

**DETECTOR-NULL, second proof CONFIRMED.** Prop 6.1(1), p.191: for a `pi`-root `sigma` of `g prod_{i<r} T_i^psi` with `ord(sigma-tau)>delta_r`, "`delta<1` implies `ord g(sigma)<0`". On a minor branch `delta^0>=1`, so FRONTIER-EXACT gives contribution 0. Reading clause (2) off the printed `r>=2` MINOR hypothesis would make every frontier a detector and force `N=0`. NOTT's minor-only statement is safe. JAC-ARC as an *inequality* `lambda_f+lambda_g<=delta-1` is not a Keller criterion (CH C6, CONTROL T5); the Keller content is equality at the frontier.

---

## 12. What the pinned formula CAN and CANNOT decide

**CAN.** Write `N=sum_B V_2(B) q(B)` with `q=(1-delta_1)de/(d+e)` and `sum V_2<=u`. Evaluate the per-root contribution at a bottom-major disc as `m(1-delta_1)/(n+m)`. Force that disc's `g`-tree to be a star. Reject a `V`-assignment with no integer `N>=2` (or none in `[4,16]` under H2), and a group under (UNI) when every assignment dies. Prove, on the enumerated census, that this floor does not grow with `D` and so does not yield `D<=C(N)`.

**CANNOT.** Prove `D<=C(N)`. Compute `N` from the Moh group `(n,m,M_*,V_s)` alone. Empty a degree or a `(B2)`/`(B3)` cell. Decide the number of Galois orbits. Bound `V_j` below beyond Def 5.1(2). Decide realisability. Identify PLACE-LEDGER places with `{g=c_2}` orbits. Constrain intra-`f` clustering. Bound `T`, `Psi`, `D`, or `D_min`. Assert (UNI) for the whole fibre.

OPEN[D1-SUBTREE] as posed — the joint tree below `delta_1` as a free rational in `[0,a_1(-lambda_f(delta_1))]` — is **CLOSED**. Residue: OPEN[BRANCH-ORBITS]. OPEN[UPPER-TO-FLOOR] remains ANSWERED-SPLIT: a floor exists and equals the old ceiling; it is `O(1)`, not `Omega(D)`.

---

## 13. Opens

```text
OPEN[BRANCH-ORBITS]  (CH; residue of D1-SUBTREE).  Number of Galois orbits of
   bottom-major discs, an integer in {1,...,u}, and the partition of
   sum_B V_2(B)<=u among them.  (UNI) is the one-orbit case.  Not filled.

OPEN[V-FLOOR]  (CH; residue of PIN-NOT-CEILING).  The integers V_j in
   (d_j/(n-M_j), V_{j+1} d_j/d_{j+1}], j=2..s, at a degree-minimal
   counterexample; equivalently q in (0, de(K-1)/(d+e)).  Nothing in
   Prop 4.4/4.6/5.3 or search (1)-(13) forces q=Omega(1).  Not filled.

OPEN[STAR-REALISABILITY]  (CH; cheap).  Multiplicity partition of p(pi) at
   sigma_1 (a partition of e V_2).  Prop 4.6 at r=1 does not already force
   simple roots; D1-STAR does.  A forced repeated root would kill the
   skeleton.  Not implemented.

OPEN[MOH-14]  (NOTT).  Is (14) implied by Moh (7)-(13)?  (15) does not
   answer this.  Bounded: the 1147 groups at D<=400 with U<4.

OPEN[UPPER-TO-FLOOR]  ANSWERED-SPLIT: floor yes (equality), D-ceiling no.
   Bounded quantity remains the integer N in [2,16] at a degree-minimal
   counterexample; the boundary tree does not supply N=Omega(D).
```

CLOSED: `OPEN[D1-SUBTREE]` as posed. Carried: `OPEN[MOH-ENDGAME]`, `OPEN[NONPROPER-DEGREE]`, `OPEN[SUBRECT-ORBIT-BRIDGE]`, `OPEN[ANTICANON-DEFECT]`, `OPEN[SAT-MASS]`, `OPEN[DELTA-AFF-VS-N]`, `OPEN[DELTA75-BRACKET]`, `OPEN[U-GT-2-ALL-D]`. Retyped on `{g=c_2}` only, not promoted as PLACE-LEDGER: `OPEN[NU-BOUND-AT-A-PLACE]`.

---

## 14. FALLACY-v2 audit

Flag/place/series: Moh `n=D` never mixed with campaign `n=deg Abar_F`. Three trees kept apart (`eta`-adic / major tower / `D_1` sub-tree). Places of `{g=c_2}` not identified with PLACE-LEDGER's generic net member. Per-ray: no exit price, no `charge_basis`; each `g-c_2` root charged once at its frontier; bottom-major discs disjoint in `D_{s-1}`. Floor/attainment: D1-PIN proved by the closed gap vanishing only at `r=1`; `L`,`U` are bounds; `min L=3/112` is MEASURED; knapsack caps survive. Carrier: an automorphism tree is not a full actual first-separation set. Pole/interior: `(star)` only where `g_y≠0` and `F` nonconstant; no-log in the Puiseux field. Prime: `g_y` is a partial; `T_r` vs `T_r^psi`, `delta^*_{r-1}` vs `delta_{r-1}` distinguished. No `sat()`, no Groebner. No cap or analogy on OPEN[BRANCH-ORBITS], OPEN[V-FLOOR], OPEN[STAR-REALISABILITY], (UNI), or the PLACE-LEDGER identification.

---

## 15. Typed verdict block

```text
LANE       D1-SUBTREE-REVIEW
SCOPE      Keller, noninvertible, degree-minimal, Moh's gauge (GEN, NU-TWO).
           JAC-FIBRE (general ord J form) and FRONTIER-EXACT for every
           dominant F in that gauge; D1-PIN and D1-STAR additionally use
           Def 5.1(1), Lemma 5.2, Prop 6.1(1), all read from the page
           images.  Case (A) EMPTY and untouched; A2 untouched; no Z(G)=1.
           H2 only where the campaign window is quoted.  No charge_basis.

PROMOTE    JAC-FIBRE CONFIRMED.  ord(f(tau)-a_0)+ord g_y(tau)=-1+ord J(tau)
             on every branch of a generic fibre; =-1 for Keller proper.
             No-log = Puiseux field (repair: state it).  Non-proper:
             delta^0>1 and (1-delta^0)^+=0.
           FRONTIER-EXACT CONFIRMED.  N=sum_rho (1-delta^0_rho)^+;
             lambda_f(delta^0)=delta^0-1 at proper frontiers;
             sum_{j≠i} ord(tau_i-tau_j)=-delta^0_i.
           D1-PIN CONFIRMED.  floor(r)-ceiling(r)=(1-delta_r)(-M_r-m)/(n-M_r),
             zero iff r=1.  c_rho=m(1-delta_1)/(n+m), N=sum_B V_2(B) q(B).
             CEILING: Def 5.1(1) at level 1.  FLOOR inequality Moh-free
             except Lemma 5.2's evaluation of lambda_g(delta_1).
           D1-STAR CONFIRMED for the g-family and mixed f/g contacts.
             Intra-f clustering free.  p(pi) at sigma_1 has a_1 simple
             roots as a Jacobian consequence, not as Prop 4.6 r=1.
           RADIUS-ORDER = Moh Lemma 5.2 CONFIRMED (novelty withdrawn).
           DETECTOR-NULL second proof CONFIRMED (Prop 6.1(1)); scope of
             (2) pinned by the N=0 contradiction.
           PIN-NOT-CEILING CONFIRMED measured (min L=3/64 at D<=120,
             3/112 at D<=200; no growth in D; no D<=C(N)).
           INTEGRALITY FILTER numbers CONFIRMED (UNI D<=120; no degree
             emptied; per-degree kills as charged).
           Condition (15) CONFIRMED: strictly stronger, contains (14).

NOT        a D-ceiling on any range; N from the Moh group alone;
CLAIMED    (UNI) for the whole fibre; PLACE-LEDGER identification;
           D1-STAR for intra-f clustering; realisability of any row;
           emptying of any degree; V_j=Omega(K); "nothing below" as
           "frontier = delta_1".

REFUTED    CONTROL 5 printed N-sets (drop V_2).  CH:531 "(84,56) M2=64
           pinned to {4,6}" (actual {4}) and "(64,48) to {6,9}"
           (actual {9}).  Qualitative "all six admit an integer N"
           SURVIVES (corrected sets {9},{4},{5,10},{9},{4,8},{16},
           all in [4,16]).

GAP        PLACE LAW as a PLACE-LEDGER theorem (confirmed on {g=c_2}).
           Slogan "N determined by the skeleton" if skeleton = the
           group (n,m,M_*,V_s): it is determined by the V-packet.

CLOSED     OPEN[D1-SUBTREE] as posed.  Residue OPEN[BRANCH-ORBITS].
ANSWERED-SPLIT  OPEN[UPPER-TO-FLOOR]: floor yes, ceiling no.

DECISION   THE JACOBIAN CONDITION BELOW D_1 IS AN EQUALITY AND IT PINS
           THE PER-DISC CONTRIBUTION.  It does not pin the packet, and
           the pinned value does not grow with D.  OPEN[D1-SUBTREE]
           CLOSED; the ceiling program on the boundary remains closed
           for a sharper reason (PIN-NOT-CEILING), with residue
           OPEN[V-FLOOR] and OPEN[BRANCH-ORBITS].

CAN        pin c_rho; write N=sum V_2 q; force a g-star; reject
           non-integral assignments; prove (measured) no D-ceiling
           from this floor.
CANNOT     prove D<=C(N); empty a degree; decide orbits; bound V_j
           below; evaluate N from a Moh group; identify PLACE-LEDGER
           places; decide realisability.

DISCLOSURE (1) Controls are automorphisms (s=1), outside Def 5.1(3).
           (2) CEILING half imports Def 5.1(1) at level 1.
           (3) sum V_2<=u uses NU-TWO; kills are a floor.
           (4) (UNI) named; [80,100] knapsack did not fit (D=80:
           132/496 killed, 76 capped, 651.7 s). [48,79] not rerun;
           hashed general.log accepted after the D=80 code-path check.

MEASURED   jacfibre 101/0; treecheck 151/0; 3 pairs 52/0; gap formula
           on 8000 V-skeletons; (UNI) D<=120 902893 / 98.98% / 60.04%,
           per-degree 264/209, 824/419, 1163/795, 60/47, 4104/2390,
           no degree emptied; min L=3/64 (D<=120), 3/112 (D<=200);
           D=80 knapsack 26.61%.
COMPUTATION python3 3.14.7 + sympy 1.14.0 over Q. No Groebner, no AWS,
            no jc2-lean.
DEVIATIONS CONTROL 5 N-sets -> achievable(); PLACE LAW on {g=c_2};
           D1-STAR split by colour; "nothing below" -> no further
           g-branching.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `36424`.
- Body SHA-256:
  `b77f9285ffad5cd6e6b93f1baba206080552c3c4e5eff63e93fcad95d89c1f43`.
- Frozen basis: `6ae086dc3ce2b44734c170ea0138a2d68d1589b8`.
