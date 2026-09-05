# Hostile gate: the all-degree finite split-window theorem, + the operative crosswalk

**Lane:** `split-window-gate-opus5-20260905`
**Date:** 2026-09-05
**Charged report:** `xmodel/split-window-alldeg-sol56-20260905.md` (body SHA-256
`278ee0c2…30143`)

## 0. Verdicts

| component | verdict |
|---|---|
| (1) window `1<rho<v_s/u_s`, denominator bound `Q<=u_s` | **CONFIRMED** |
| (2) `(G)` Puiseux–Galois covariance, necessity + group element | **CONFIRMED** |
| (3) `(L)` split-face Jacobian ODE + `W`-dependence repair | **CONFIRMED-WITH-FIX** (blast radius is `18` slots on `17` rows, not `29`/`28`) |
| (4) frozen tool on 3 random census rows, re-derived by hand | **CONFIRMED** |
| crosswalk on the 310 operative `u_s>=2` rows | **DELIVERED**: `233` descent-forced, `77` retain `113` ES leaves |

Custody: the receipt `xmodel/split-window-gate-opus5-20260905.run.v2` was parsed
with `awk` into a manifest and `sha256sum -c` returned `OK` for all eight
charged inputs. No digest was retyped.

Everything below is recomputed from an **independent** implementation,
`box/split-window-gate-20260905/gate_screen.py`, written from the sources, not
from `box/lib/split_window.py`. It differs deliberately in two places: `(G)` is
tested by explicit orbit construction, and `(L)` is tested by **brute force over
all `2^r` low/high assignments**, so the charged monotone-optimum shortcut is
audited rather than reused.

---

## 1. Component (1) — the window and the denominator bound: CONFIRMED

### 1.1 The two endpoints, from the sources

**Lower endpoint.** Moh Proposition 6.1 (printed pp.190–191, read from the frozen
PDF) states `delta*_{r-1} >= 1` and then only "(1) the inequality `delta<1`
implies `ord g(sigma)<0`". So Moh supplies `>=1`, never `>1`. The strict
endpoint is borrowed: Xu Proposition 7.3 (pp.10–11) concludes
"`T_{0,sigma_1}(pi), …, T_{s,sigma_1}(pi)` are powers of a common linear
polynomial", i.e. the order-one face has one root, so no split occurs at
`rho=1`. This is *Xu's* theorem under *Xu's* §7.3 hypotheses (and its proof runs
through his Lemma 7.2, itself extracted from Moh Proposition A.2). The charged
report says exactly this and does not over-claim it.

**Upper endpoint.** `rho < v_s/u_s` is the *definition* of the ES side, whose
complement is the Proposition 6.3 descent side; `ord g(sigma) =
(n/d_s)(u_s rho - v_s)`, so `rho = v_s/u_s` has order zero and is not an early
split. The dichotomy itself is charged campaign material
(`prop63-radius-dichotomy`), consumed here, not re-derived.

### 1.2 The denominator bound is a new lemma, and it is `u_s`

The report is right that this is not a citation. Xu §8 writes "our tools are two
constrains: one is that the denominator of order `delta <= u_s = 3`" — asserted
for the single case, with no all-degree proof anywhere in §7 or §8.

I re-derived the lemma and it holds. The chain is:

1. Moh Lemma 5.3 / p.194 (read verbatim): in the surviving case the highest
   homogeneous form is `[(y-ax)^{V_s}(y-bx)^{u_s}]^{n/d_s}`, `a != b`,
   `u_s = d_s - v_s`; Lemma 5.3 (pp.185–186) constrains `v_s` and Xu §7.3
   states it outright — "here `u_s < v_s = d_s - u_s`" — hence
   **`u_s != v_s`**.
2. Therefore the two clusters have *different* multiplicities and Galois cannot
   swap them: the minor cluster is Galois-stable. **This step is load-bearing
   for both (1) and (2) and the charged report never states it** — it cites
   Lemma 5.3 in §1.1 for the radius but does not connect `u_s != v_s` to the
   stability its §2 proof needs. Substantively fine; an exposition gap.
3. Every cluster member shares the same truncation `c(t)` strictly below `rho`;
   `sigma` acts termwise on exponents, so `sigma(c)` is the truncation of
   another member, `= c`. So `c` is Galois-fixed and the centre multiset is
   canonically defined.
4. With ramification `N` (so `Q | N`), a generator sends `z_i -> omega z_i`,
   `omega = zeta_N^{N rho}`, and
   `ord(omega) = N/gcd(N, NP/Q) = N/((N/Q) gcd(Q,P)) = Q` **exactly**.
5. Nonzero centres have free `Q`-orbits; only `z=0` is fixed. A genuine split
   has `>=2` distinct centres, so at least one is nonzero, so
   `Q <= #{distinct nonzero centres} <= r = len(lambda) <= u_s`.

**Answer to the posed question ("`u_s`, or lcm/branch-count?").** It is `u_s`,
and no lcm can enter: there is one ramification index and one cyclic group, and
`ord(omega)` is fixed by `rho` alone. `Q<=u_s` is deliberately the *coarse*
row-level relaxation, used to make the window finite *before* `lambda` is
chosen. The sharp statement is `Q <= r` together with `(G)`'s divisibility, and
the tool does impose it downstream. Nothing is lost.

The window arithmetic is exact: strict `P/Q < v/u` `<=>` `P <= floor((Qv-1)/u)`,
which is what both implementations enumerate.

---

## 2. Component (2) — `(G)`: CONFIRMED, and it is genuinely necessary

**Is it necessary on any realized face, or does it assume a normalization?**
Necessary. The normalizations it uses are all forced or harmless:

- *Origin.* `z=0` is the Galois-fixed common truncation `c(t)` of §1.2 step 3.
  That is determined by the cluster; it is not a choice.
- *Monicity.* Scaling `P` does not change which `p_i` vanish, so
  `(omega^i - omega^u)p_i = 0` is scale-invariant.
- *Which primitive `Q`-th root.* Immaterial: for every primitive `Q`-th root the
  condition collapses to `Q | (i-u)`, i.e. `P(z) = z^e H(z^Q)`.
- *Parameter rescaling `t -> ct`.* Scales all centres by one constant, which
  commutes with `z -> omega z`.

The conjugated element is correct. For `h(z)=alpha z+beta`,
`gamma_h(w) = h(omega h^{-1}(w)) = omega(w-beta)+beta = omega w + (1-omega)beta`
— re-derived, matches (3.2). The report is right to insist that after an affine
face normalization one may not keep using `z -> omega z`. And because the
partition/multiplicity data is conjugacy-invariant, the *implemented* test
(which reads only `lambda` and `Q`) is coordinate-free, so no kill certificate
depends on the gauge.

**Closed count (2.6) verified.** `A_1(u)=p(u)-1`, `A_Q(u)=sum_{j<=u/Q} p(j) - 1`
for `Q>1`, checked against direct enumeration for every `u=2..15` and every
`Q=1..u`: **0 mismatches**.

The one caveat is the dependency in §1.2 step 2 — `(G)` is necessary *given*
that the minor cluster is Galois-stable, which needs `u_s != v_s`. That holds
throughout Moh's surviving case, so the verdict is CONFIRMED, not
CONFIRMED-WITH-FIX.

---

## 3. Component (3) — `(L)` and the `W`-dependence: CONFIRMED-WITH-FIX

### 3.1 The face equation, re-derived from Xu (7.1)

Xu's identity is `d(T_s(sigma), g(sigma))/d(t,pi) = -J (T_s)_f(sigma) t^{-2+delta}`.
Substituting his own displays, with `E=n/d_s` and `X = u rho - v`:

```text
g(sigma)      = a_1 p^E     t^{EX} + …
(T_s)_f(sigma)= b   p^{W+E} t^{(W+E)X} + …
T_s(sigma)    = a_s q       t^{a} + …,      a = WX - 1 + rho
```

Expanding the Jacobian and cancelling `p^{E-1}` gives
`a q p' - X p q' = C p^{W+1}`, `C != 0`, and comparing leading coefficients with
`p, q` monic forces `C = v-u` via `a u - X D = v - u` (verified symbolically).
Exponent bookkeeping closes exactly: `a + EX - 1 = (W+E)X + delta - 2`.

The `W` used is `(-mu_s-2)/d_s`, **not** the `(-mu_s+n-2)/d_s` printed inside
Xu's Corollary 7.5 proof. This is the campaign's banked exponent correction and
the source settles it in the report's favour: at `(99,66)` Xu §8 himself writes
`deg q(pi) = 13*3+1` and `T_3(sigma) = q(pi) t^{13(-8+3delta)-1+delta}`, i.e.
`W = 13 = (145-2)/11`, `D = 40`, `a = WX-1+rho`, all literal. The competing
formula would give `22` and `D=67`. The report's `D=Wu+1` is right.

Coefficient system (4.2) audited: `(RP')_l = sum_{i+j=l+1} i p_i r_j`,
`(PR')_l = sum_{i+j=l+1} j p_i r_j`, `(P^{W+1})_l` over `W+1` indices — correct
as printed, range `0..(W+1)u` correct.

### 3.2 The local dichotomy, and the monotone optimum

At a distinct root `c` with `P`-multiplicity `lambda`, `R`-multiplicity `nu`:
LHS has order `>= lambda+nu-1` with leading coefficient
`(a lambda - X nu)U(c)V(c)`; RHS has order exactly `lambda(W+1)`. So either it
does not cancel and `nu = W lambda + 1`, or it cancels and `nu = k lambda`,
`k = a/X = W - t`, `t = (rho-1)/(v-u rho) > 0`. These are exact alternatives, as
claimed — not bounds. `nu` is a multiplicity, so `nu in Z_{>=0}`.

The monotone-optimum claim is provable, not merely asserted:
`high - low = (W lambda + 1) - (W-t)lambda = t lambda + 1 > 0`, so all-eligible-low
is strictly optimal. **Brute-forced anyway** over all `2^r` assignments on 500
random census rows and on all `(99,66)` rows: **0 disagreements**.

**Positive control (decisive).** Xu's published witness equation (8.2) —
`d/d(t,pi)(pi(pi+3a)^2(pi-2a) t^{-1}, pi^2(pi+3a) t^{-2}) = 5 pi^4(pi+3a)^2 t^{-4}`
— maps to `(u,v,W,rho) = (3,8,1,2)`, and satisfies my reconstructed `(F)`
identically (`residual = 0`, sympy). Its realized exponents are exactly the
predicted pattern: root `pi=0`, `lambda=2`, `nu = k lambda = 1` **LOW**; root
`pi=-3a`, `lambda=1`, `nu = W lambda + 1 = 2` **HIGH**; `sum nu = 3 <= D = 4`
with the free factor `(pi-2a)` taking up the slack. Three negative controls
(swap low/high; both high; generic `q` of correct degree) all give nonzero
residual.

**`(L)` reproduces Xu Corollary 7.5 exactly.** `rho < (v+1)/(u+1) <=> t < 1`, and
for `lambda=(1^u)` that forces `t*1 not in Z`, hence all-high, hence
`|H| = u >= 2 > 1`. Checked over `u=2..9`, `v=u+1..39`, every window element:
**0 counterexamples**. So Xu's corollary is a strict consequence of `(L)`, which
is why the tool records it as an independent source certificate rather than an
extra screen.

### 3.3 Is the `W`-dependence correct? Yes.

`k lambda in Z <=> t lambda in Z` because `W lambda in Z` always — that is the
charged 17(iiiiii) observation and it is right. What 17(iiiiii) omitted is
`k lambda >= 0`, i.e. `t <= W`. When `t > W` **no** root is eligible for the low
branch, so `|H| = r >= 2 > t*0 + 1 = 1` and the slot dies. Equivalently the
sharper cutoff `rho <= (Wv+1)/(Wu+1)` of (4.5) — verified equivalent to `k>=0`
on every window element of 500 random rows, **0 mismatches**. So the repair is
correct and (4.5) is a sound consequence.

**Direction.** The `W`-independent screen has a *superset* of low options, so its
`min sum nu` is `<=` the repaired one. It can therefore only **under-kill**,
never over-kill.

**On `(99,66)` it does neither.** Running both variants on all six `u_s>=2`
rows: survivor lists are **identical** on `S1, S2, S3, S4, S7, S8`. The charged
claim "it does not change any `(99,66)` verdict" is CONFIRMED.

### 3.4 THE FIX — the stated blast radius is a miscount

§0 says the repair "catches `29` otherwise missed leaves on `28` rows"; §4.3 says
it "affects `29` G-admissible slots on `28` frozen rows". Both wordings assert a
changed verdict. The number `29/28` is not that.

Under the tool's own definition — G-passing slots killed by `L` alone with
`k<0` (`run_census.py:58-61`) — I reproduce **29 slots on 28 rows** exactly. But
that counts *guard firings*, and a firing is not a change: when some
`k lambda_i not in Z`, that root is forced high under **both** variants and the
slot dies either way. Counting slots whose verdict actually differs from the
`W`-independent screen:

```text
tool-style negative-k guard FIRINGS   : 29 slots / 28 rows   (as printed)
actual VERDICT CHANGES vs W-indep (L) : 18 slots / 17 rows   (corrected)
```

The 18 are listed in `box/split-window-gate-20260905/wsens.json`. They include
the report's own §4.3 exhibit, `(114,76)`, `(u,v,W)=(4,15,7)`, `rho=11/3`,
`t=8`, `k=-1`, `lambda=[1,1,1,1]` — which is genuine. So the *correction to
17(iiiiii) stands*; only its advertised size does not. The `(u,v)`-family table
in §6.1 is independently correct: exactly **3 of 132** families show
`W`-sensitive survivor lists — `(3,17)`, `(4,15)`, `(7,23)` — reproduced
family-by-family, `W`-value by `W`-value.

### 3.5 `(99,66)` recomputed from my own implementation

```text
S1 (u,v,W)=(2,9,31)  raw  6  G  6  killed  5  surv 1   4:[1,1]
S2 (u,v,W)=(4,7,23)  raw 16  G  6  killed 13  surv 3   3/2:[2,2], 3/2:[2,1,1], 5/3:[1^4]
S3 (u,v,W)=(4,7,23)  raw 16  G  6  killed 13  surv 3   (same as S2)
S4 (u,v,W)=(3,8,23)  raw 12  G  7  killed 10  surv 2   2:[2,1], 5/2:[1,1,1]
S5, S6               u_s = 1  ->  NOSPLIT (no genuine partition of 1)
S7 (u,v,W)=(4,7,13)  raw 16  G  6  killed 13  surv 3   (same as S2)
S8 (u,v,W)=(3,8,13)  raw 12  G  7  killed 10  surv 2   2:[2,1], 5/2:[1,1,1]

charged open cohort S1,S2,S3,S4,S7 :  raw 66  killed 54  survivors 12   [matches]
banked S8 external control         :  raw 12  killed 10  survivors  2   [matches]
```

The twelve survivors are exactly the charged list. **S8's two survivors are
exactly Xu §8's own published answer**: `delta=2` ("the equation 7.1 produces
Moh's 2 roots split case", partition `[2,1]`) and `delta=5/2` ("this case is
open … possible `p(pi)=pi(pi^2-c)`", partition `[1,1,1]`). That is an external,
non-campaign confirmation of the whole `(2.2)+(G)+(L)` stack on a case the
literature settled independently.

### 3.6 Sharpness (not an error)

`(L)` uses only `sum nu_i <= deg R`. It discards (i) the low-branch requirement
that after cancellation the order still match `lambda(W+1)`, and (ii) the entire
coefficient system (4.2). `(F)` is square — `(W+1)u+1` unknowns against
`(W+1)u+1` equations of which the top is the automatic identity `au-XD=v-u` —
and carries a 2-dimensional affine symmetry `(alpha, beta)`, so solvability is
strictly stronger than the degree count. Survivors are correctly typed
`SURVIVES_NECESSARY_SCREEN`; further kills are available to whoever pays for
(4.2). No carrier is promoted to an exit here.

---

## 4. Component (4) — frozen tool on 3 random census rows: CONFIRMED

Seed `20260905`, `random.sample` over the 6,209 frozen rows.

**Row 4681 — `(192,144)`, `M=(-144,-120,-84,-66,190)`, `V=(1,16,8,4)`, `s=5`.**
gcd chain `d=(192,48,24,12,6,2)`, `d_s=6`, `v=V_5=4`, `u=6-4=2`, `v/u=2`.
`mu`: `-144 -> 4(-144)+24=-552 -> 2(-552)+36=-1068 -> 2(-1068)+18=-2118 ->
2(-2118)+256=-3980`; `W=(3980-2)/6=663`; `D=1327`.
Window `1<rho<2`, `Q<=2`: `Q=1` needs `P<=floor(3/2)=1`, empty; `Q=2` gives
`P=3` only. Window `{3/2}`, one genuine partition `[1,1]`, raw `1`.
`(G)`: `Q=2`, frequencies `{1:2}`, `2 mod 2 = 0` → passes (centres `{r,-r}`).
`(L)`: `t=(1/2)/(4-3)=1/2`, `k=663-1/2=1325/2 not in Z` → both high,
`sum nu = 2*664 = 1328 > 1327`. **KILL.** Survivors `0`. Tool: `0`, attribution
`{'L':1}`. **Match.**

**Row 2399 — `(168,112)`, `M=(-112,140,154,161,166)`, `V=(5,3,10,5)`, `s=5`.**
`d=(168,56,28,14,7,1)`, `d_s=7`, `v=5`, `u=2`, `v/u=5/2`.
`mu`: `-112 -> -84 -> -154 -> -301 -> -597`; `W=(597-2)/7=85`; `D=171`.
Window: `Q=1` gives `P<=floor(4/2)=2` → `rho=2`; `Q=2` gives `P<=floor(9/2)=4`,
odd → `3/2`. Window `{3/2, 2}`, raw `2`, both `(G)`-admissible.
`rho=3/2`: `t=(1/2)/2=1/4`, `k=339/4 not in Z` → both high, `172 > 171`. **KILL.**
`rho=2`: `t=1/(5-4)=1`, `k=84 in Z_{>=0}` → both low, `168 <= 171`. **SURVIVES.**
Survivors `{2:[1,1]}`. Tool: `1`, `2:[1,1]`. **Match.**

**Row 690 — `(135,90)`, `M=(-90,75,100,133)`, `V=(20,9,3)`, `s=4`.**
`d=(135,45,15,5,1)`, `d_s=5`, `v=3`, `u=2`, `v/u=3/2`. `mu_s=-837`, `W=167`.
Window `1<rho<3/2`, `Q<=2`: `Q=1` needs `P<=1`; `Q=2` needs `P<=floor(5/2)=2 < 3`.
**Window empty** — no `(G)`/`(L)` work required. Survivors `0`. Tool: `0`, raw
`0`. **Match.** (This is the empty-raw-window class: descent-forced by the radius
dichotomy alone.)

---

## 5. Full-census replay of the frozen run

My independent screen was run against all **6,209** frozen rows, comparing
profile `(u_s,v_s,W)`, raw/`G` counts, and the **complete survivor list** row by
row.

```text
mismatches (profile, counts, or survivor list)      0 / 6209
raw pair slots            78,575     G-admissible      22,434
killed                    73,677     survivors          4,898
rows with no survivor      3,758
survivor histogram  0:3758 1:1482 2:416 3:287 4:108 5:9 6:86 7:3 8:6 9:17
                    10:9 11:3 12:3 13:1 14:12 15:1 17:1 18:5 21:1 25:1
```

Every aggregate and the entire histogram reproduce the charged §6 table exactly.
The only number I could not reproduce as *described* is the `29/28` of §3.4
above.

---

## 6. CROSSWALK — the corrected operative partition at `n <= 200`

Source of rows: `box/scopeleaks-20260905/scope_enum.json`, `operative_rows`,
`1,420` rows under `C_FULL_TREE_POLYNOMIAL_ODE ∧ XU`, `u_s` histogram
`{1:1110, 2:265, 3:34, 4:9, 5:2}`, i.e. **310** rows with `u_s>=2`. All 310 were
matched into the frozen census by `(n,m,M_2..M_s,V)`: **0 unmatched, 0 survivor-list
disagreements**.

### 6.1 The `u_s>=2` block

```text
310 operative rows with u_s >= 2
  NO G+L survivor  =>  DESCENT D2 FORCED              233
      of which the raw split window is already empty  142
      of which the window is nonempty but screened out 91
  retain typed ES leaves                               77   (113 leaves total)

survivor-count histogram   0:233  1:58  2:9  3:5  4:4  6:1
by u_s   {u_s: [descent-forced, with-leaves]}
   u_s=2: [225, 40]   u_s=3: [6, 28]   u_s=4: [1, 8]   u_s=5: [1, 1]
```

The `233` have no early-split route at all, so the only remaining branch is
`rho >= v_s/u_s`, i.e. the Proposition 6.3 descent D2 is **forced**. They are not
killed: they join the `u_s>=2` descended family and are blocked on
`OPEN[CHILD-TOP-AT-US-GE-2]` (child-data §3.4: `(C-TOP)` is proved at `u_s=1`
and unlicensed at `u_s>=2`).

The **6** operative `u_s>=2` U-NEGATIVE rows — `(160,120)`, `(192,144)`×4,
`(200,80)` — all return `0` survivors, so they sit inside the `233` and are
already dead by scope-leaks §§2/4. Live descent-forced count is therefore
**227**.

The `77` rows carry `113` leaves in `23` distinct `(rho,lambda)` shapes across
`25` degree pairs and `56` `(u_s,v_s,W)` profiles. Leaf `rho` multiset:
`2:43, 3/2:25, 3:15, 5/2:15, 8/3:5, 4:4, 5/3:4, 11/4:1, 7/2:1`. Partition shapes:
`[1,1]:40, [1^3]:29, [2,1]:10, [2,2]:8, [2,1,1]:8, [1^4]:8, [3,1]:4, [1^5]:2,
[4,1]:1, [3,1,1]:1, [2,2,1]:1, [2,1,1,1]:1`. Full listing with `(n,m;M;V)`,
`(u_s,v_s,W)`, `ell` and per-row leaves:
`box/split-window-gate-20260905/crosswalk-310.json`. Landmarks: `(99,66)` S8
appears with `2:[2,1], 5/2:[1,1,1]`; the widest row is `(171,114)`,
`(u,v,W)=(5,14,13)`, with 6 leaves.

### 6.2 The `u_s=1` block — confirmed unchanged

All **1,110** operative `u_s=1` rows return `NOSPLIT`, and the reason is on the
partition side, not the window side: `deg p = u_s = 1`, and there is **no
partition of 1 with `>=2` blocks**, so the raw slot set is empty whatever the
window contains. Nothing in the split-window theorem touches them, so the
**174** live `u_s=1` rows (`(C-TOP)` holds) are unchanged. **Confirmed.**

### 6.3 The corrected operative partition — the exact residual at `n <= 200`

| class | rows | status |
|---|---:|---|
| `u_s=1`, `(C-TOP)` fails | 936 | licensed kill (child-data §3.4) |
| **`u_s=1` live** | **174** | no split possible; unchanged by this theorem |
| **`u_s>=2`, no G+L survivor → D2 forced** | **233** | of these 6 already dead (U-NEG) → **227 live**; blocked on `OPEN[CHILD-TOP-AT-US-GE-2]` |
| **`u_s>=2`, retains ES leaves** | **77** | D2 **not** forced; `113` typed `(rho,lambda)` obligations **plus** the same D2 branch |
| total | 1,420 | |

Operative residual `= 174 + 227 + 77 = 478` live rows (`484` before removing the
6 U-NEG dead). The split-window theorem's contribution to the residual is
sharp and modest: it converts **233 of 310** `u_s>=2` rows from "two open
branches" to "one open branch", and it types the other **77** to `113` explicit
finite leaves. It kills **no row outright** — a row with an empty ES branch is
still alive on its descent branch.

---

## 7. Reproduction

```bash
awk -F= '/^charged_input_[0-9]+_sha256=/{split($1,a,"_");i=a[3];h[i]=$2}
         /^charged_input_[0-9]+_basename=/{split($1,a,"_");i=a[3];b[i]=$2}
         END{for(k=1;k<=8;k++) printf "%s  /tmp/jc2-lane.cgyZY7/inputs/%s\n",h[k],b[k]}' \
    xmodel/split-window-gate-opus5-20260905.run.v2 > /tmp/manifest.sha256
sha256sum -c /tmp/manifest.sha256
python3 -c "import sys; sys.path.insert(0,'box/split-window-gate-20260905');\
  from gate_screen import screen; print(screen(99,66,[77,97],{2:8,3:8})['survivors'])"
```

Artifacts, all in `box/split-window-gate-20260905/`:

```text
gate_screen.py        independent screen; brute-force (L), orbit-built (G)
crosswalk-310.json    the 310 operative u_s>=2 rows with per-row ES leaves
wsens.json            the 17 rows / 18 slots whose verdict the W-repair changes
my-census.json        independent 6,209-row replay
```

No ledger, `jc2-lean`, or `ideation-*` file was edited.

## 8. FALLACY-v2 audit

- **Flag/place/series.** Moh's global p.183 radius `-1`, the terminal minor
  contact `rho`, a face centre `z_i`, a Puiseux series, and a final place are
  kept distinct. `rho < v/u` (ES) and `rho >= v/u` (descent) are never merged.
- **Carrier/attainment.** No survivor is promoted. The `113` leaves are
  `SURVIVES_NECESSARY_SCREEN` carriers; §3.6 states explicitly what `(L)` throws
  away. `sum nu <= deg R` is a floor test, never attainment.
- **Floor/attainment.** Moh Prop 6.1 gives `>= 1` only; the strict `> 1` is
  Xu Prop 7.3's, under Xu's hypotheses, and is labelled borrowed.
- **Variable/ring map.** `(F)`'s ring, generator order and monic normalizations
  are declared; the conjugated group element `gamma_h` is written out; the face
  gauge is not called a source automorphism.
- **Positive and negative controls.** Xu (8.2) verified as an exact solution of
  the reconstructed `(F)`; three negative controls give nonzero residual;
  `(L) => ` Xu Cor 7.5 checked over `u=2..9`, `v<=39`.
- **Prime label/derivative.** `p'`, `q'` are `d/d(pi)` in the declared face ring;
  `s'` (child) is never identified with `s` (parent).
- **Target/arrival index.** `u_s = d_s - v_s` is the ancestor index throughout;
  the descended `u'` of scope-leaks is never substituted for it.
- **Per-ray/exit-set charge.** No new exit-price assertion is made — the gate
  confirms a necessary screen and re-partitions existing obligations — so no
  `charge_basis` line is emitted.

## 9. Typed openings

- `OPEN[SPLIT-FACE-ATTAINMENT]` — unchanged; `(G)+(L)` passage is not existence.
- `OPEN[SPLIT-TO-JOINT-MAP]` — unchanged; no source-to-joint chart map.
- `OPEN[CHILD-TOP-AT-US-GE-2]` — now carries the **227** live descent-forced
  rows in addition to the 77 leaf-carrying rows' descent branches. This is the
  single widest blocker in the `n<=200` residual.
- `OPEN[SPLIT-LEAF-KILLS]` — narrowed on the operative cohort from "310 rows"
  to **113 explicit `(rho,lambda)` leaves on 77 rows**.
- `OPEN[CENSUS-COVERAGE-ALL-DEGREE]` — unchanged and untouched by this gate.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `22920`.
- Body SHA-256:
  `72ea6d6155f400af53f2a30c9b61d16fd6fe911d6702e7ca7c6bb42105cce226`.
- Frozen basis: `847c4cfa47447666cdc9e7c880cc1d1cdd4e6b3c`.
