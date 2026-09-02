# REDUCIBLE-BRANCH REPRICE — the day's exact machinery is H2-FREE, the reducible datum lives in the block that contributes exactly ZERO to `N`, and the `N >= 6` frontier recovers 99.6% of the H2 kill without H2

Lane: `REDUCIBLE-BRANCH-REPRICE` (charge 18:36Z, `notes.md:20538`).
Date: 2026-09-02. Agent: Opus 5. Desk derivation + desk-scale CAS (python3 3.14.7 /
sympy 1.14.0, exact over `Q`; no Singular, no AWS, no web, no fetching). Drivers in
`box/reducible-reprice-20260902/`; one core, peak RSS < 400 MB.

## 0. Custody, scope, method

The seven charged frozen copies were hashed with `shasum -a 256` **before any was
read**; all seven match. The five `xmodel/` originals and the two `box/` drivers on
disk are byte-identical to the frozen copies (re-hashed), so every `file:line`
citation below is valid against the repository paths: `126d9c84` integration17,
`26479b06` d1-subtree-opus5 [**CH**], `66c3e82f` its grok-4.6 review [**RV**],
`bf1d428c` integration14, `6b8a7123` integration16, `30220204` `box/moh_skeleton_N.py`,
`cf0780cc` `box/d1sub-drivers-20260902/d1floor.py`.

Record read for the reducible branch, as charged: `AUDIT.md` (H2 residual entries,
integration deltas), `APPROACHES.md` (its rank-four overlay uses "reducible" for the
*block branch* — a different object, see K5), `notes.md` LIVE STATE 2026-09-01/02 (the
reducible cage, the companion front, the N=4/N=5 closures, the 01:10Z frontier),
integration #14 §C/§D.

**Typing.** Everything asserted here is PROVED-HERE/UNREVIEWED or MEASURED at the
stated scope; consumed items keep their record type. No canonical ledger edited;
`jc2-lean` not inspected; nothing fetched. **No `charge_basis` line: no new exit price
is asserted.**

**Degree-like integers kept apart**, extending CH §0: `D`; the geometric degree `N`;
`K = gcd(deg P, deg Q)`; Moh's `n = deg_y g = deg g = D` and `m = deg_y f`; and — the
one CH deliberately excluded and this lane must reintroduce — the campaign's
`n_A = deg Abar_F` (target side), with the **horizontal degree**
`n_A^Y := #(A_F ∩ {Y = c_2})` at generic `c_2`. From §3 on I write `D` for Moh's `n`.
`delta` is never `delta_aff`; Moh's `d_i`, the exponent `d` of `l(P) = alpha H^d`, and
`d_s` stay three-way distinguished.

Drivers, sealed (`box/reducible-reprice-20260902/`): `nmin_reprice.py` (the (UNI)
integrality filter at variable `N_min`), `nonproper_count.py` (the non-proper branch
count), `nonproper_rate.py` (CONTROL R).

## 1. Verdict, up front

```text
(1) SCOPE.  NOT ONE ITEM of the day's exact machinery uses H2.  H2 enters the charged
    reports at exactly one place: the CLIP of the integrality filter to the window
    [4,16] (CH:546).  What the machinery DOES use -- and what §2's table separates --
    is (GEN) the monic gauge, (MIN) degree-minimality, and Moh's tower with M_s = n-2.
    ONE non-obvious load-bearing dependency, checked by perturbation: the D1-PIN
    coincidence floor(1) = ceiling(1) needs n-M_s-1 = 1 EXACTLY; off M_s = n-2 the gap
    at r = 1 is (1-delta_1)(1-(n-M_s-1)) != 0 and N is only bracketed.
(2) THE REDUCIBLE BRANCH UNDER EXACT-N.  N is unchanged, structurally: D1-STAR +
    DETECTOR-NULL + FRONTIER-EXACT partition the D branches of a generic fibre into
    PROPER (the e*sum_B V_2(B) roots of the bottom-major discs) and NON-PROPER (all in
    minor discs, each contributing EXACTLY 0).  Every datum that distinguishes A_F
    reducible from irreducible -- the limit points (a_0,c_2) in A_F, their monodromy
    orbits, the component degrees -- is carried by the NON-PROPER block.  The pinned N
    is blind to reducibility BY CONSTRUCTION.
(3) NEW, PROVED HERE, on the reducible side of that line: NONPROPER-COUNT
    (# non-proper branches = D - e sum_B V_2(B) = e(K - sum V_2), skeleton-determined);
    NONPROPER-RATE (ord_t(f(tau)-a_0) = delta^0 - 1 + ord_t J at EVERY branch, the half
    of (JF) the D1 lane never used); STRICT-FRONTIER (Keller => delta^0 = 1 is
    IMPOSSIBLE); NONPROPER-CAP (n_A^Y <= e(K - sum_B V_2(B))).  CONTROL R: 113 exact
    checks, 0 failures, on 19 non-Keller rows with genuinely non-proper branches.
(4) MEASURED REPRICE.  The N<=5 closure is H2-FREE, so the reducible branch has the
    SAME N_min = 6.  (UNI) integrality at D <= 120 with N_min = 6 and no upper window:
    893,340/902,893 assignments (98.94%) and 6,360/10,637 groups (59.79%) die --
    against the record's H2 numbers 98.98% / 60.04%: the frontier upgrade recovers
    99.6% of the H2 group kill WITHOUT H2.  REBASED (§4.3) onto the sibling lane's
    proved Moh-condition gate: 63.40% H2-free against 63.69% H2, same picture; on its
    reconstructed full gate the unconditional filter kills NOTHING and the whole kill
    is the frontier (9.41% H2-free vs 13.94% H2).  No degree emptied anywhere.
(5) VERDICT (c) PARTIALLY SUBSUMED, boundary at proper/non-proper: the census and the
    pinned-N filter are ONE program for both branches; the reducible branch's own
    residual -- OPEN[COMPANION-R0-REALISATION]/degree-cap (notes.md:18413-18416) -- is
    a statement about the non-proper block, which the machinery proves contributes
    zero.  The cheapest discriminating computation was RUN and returns ZERO kills.
```

## 2. Part (1): SCOPE AUDIT

### 2.1 The hypotheses, named

```text
 (GEN) Moh's gauge: deg f = deg_y f = m, deg g = deg_y g = n = D, both monic in y,
       m < n  (CH:106-108).  A NORMALISATION: a generic linear change of (x,y)
       achieves it for any pair and preserves Keller and N.  Costs nothing.
 (KEL) [f,g] = c in C^*, F dominant and noninvertible.
 (MIN) degree-minimality (Aut x Aut orbit-minimal; GGV-minimal for the subrectangular
       gauge).  int14:20-23: "(LF) and (MIN): … at a degree-minimal representative
       d, e >= 2, d != e".
 (TOW) Moh's tower Def 5.1 with M_1 = -m, M_s = n-2, s >= 3, V_s < d_s.  Sources, in
       the census docstring box/moh_skeleton_N.py:279-287: "M_1 = -m, M_s = n-2  Moh
       search (1),(2) + Prop 5.4/Lem 5.3"; "V_s < d_s  two points at infinity
       (delta_s = -1)" [Moh Cor 6.1]; "s >= 3  Moh Prop 5.5"; "K >= 16  GGV Cor 6.6".
 (NU2) NU-TWO: leading form has exactly two distinct linear factors of different
       multiplicities, M_s = n-2, gauge-free -- a DEGREE-MINIMAL theorem
       (notes.md:20106-20111).  Supplies the UNIQUE major child D_{s-1} of the root
       ball, hence sum_B V_2(B) <= u.
 (H2)  A_F irreducible.  Definition: xmodel/block-descent-a1-mprime-coordinator-
       integration-fable5-20260831.md:38, "(H2) `A_F` irreducible".
```

`(TOW)` and `(NU2)` are two independent routes to the same `M_s = n-2` — Moh's own
search for a minimal-degree counterexample, and the campaign's gauge-free theorem at a
degree-minimal representative. Either suffices; the exact machinery needs one of them,
and needs it **at level `s`**, not merely at level `1` (§2.4).

### 2.2 The table

`U` = used / load-bearing; `–` = not used.

| item | (GEN) | (KEL) | (MIN) | (TOW)/(NU2) | (H2) | weakest scope where it holds |
|---|---|---|---|---|---|---|
| **JAC-FIBRE**, general `= -1 + ord_t J` | U | – (dominant only) | – | – | – | any dominant pair monic in `y` |
| **JAC-FIBRE**, Keller form `= -1` | U | U | – | – | – | Keller only |
| **FRONTIER-EXACT** `N = Σ(1-δ⁰)⁺` | U | U | – | – | – | Keller only |
| **DETECTOR-NULL**, non-proper ⇒ 0 | U | U | – | – | – | Keller only (immediate from FRONTIER-EXACT) |
| **DETECTOR-NULL**, minor disc ⇒ 0 | U | U | – | U (Moh Prop 6.1(1), `r≥2`, minor window) | – | +Moh tower |
| **D1-PIN FLOOR**, as an inequality | U | U | – | – | – | Keller only (JAC-FIBRE + slope ≥ 1) |
| **D1-PIN FLOOR**, closed value | U | U | – | U (Lemma 5.2 **and** `M_s=n−2`) | – | +Moh tower |
| **D1-PIN CEILING** | U | U | – | U (Def 5.1(1) at level 1) | – | +Moh tower |
| **D1-PIN**, the coincidence at `r=1` | U | U | – | U (**`M_s=n−2` load-bearing**) | – | +Moh tower / NU-TWO |
| **D1-PIN**, `N=Σ_B V₂q`, `Σ_B V₂ ≤ u` | U | U | U (via NU2) | U (unique major child) | – | +degree-minimal |
| **D1-STAR** | U | U | – | U (as D1-PIN) | – | +Moh tower |
| **PIN-NOT-CEILING** (measured) | U | U | U (census `K≥16`, `2≤d<e`, `s≥3`) | U | – | +degree-minimal |
| **integrality filter**, uncond. column | U | U | U | U | – | +degree-minimal |
| **integrality filter**, `[4,16]` column | U | U | U | U | **U** | +H2 — *the only H2 use in the day's machinery* |
| **condition (15)** | U | U | U | U | – | +degree-minimal |
| **HARMONIC-BOUND** | U | U | U | U | – | +degree-minimal (**false** for automorphisms) |
| **N-CEILING** `N ≤ uq` | U | U | U (via NU2) | U | – | +degree-minimal |

### 2.3 The hypothesis lines, verbatim

**JAC-FIBRE** (`xmodel/d1-subtree-opus5-20260902.md:192-194`): "Let `f, g in C[x,y]`
be monic in `y`, `F` dominant, `J := [f,g] = f_x g_y - f_y g_x`. Fix generic `c_2`,
let `tau in C<t>` be any root of `g - c_2`, and let `a_0` be the `t^0`-coefficient of
`f(tau)`." No Keller, no minimality, no tower, no `A_F`; the Keller specialisation is
the next sentence (`:198`). **FRONTIER-EXACT** (`:232-233`) adds only "For a Keller
pair in the gauge and generic `c_2`"; the review states the weaker requirement
explicitly (`xmodel/d1-subtree-review-grok46-20260902.md:100-101`): "The formula does
**not** require the `g`-roots to separate at `delta^0` itself. It requires only that
no contact exceed `delta^0`, which is the definition of the frontier."

**DETECTOR-NULL** (`:307-311`) imports Moh Prop 6.1(1) with its printed hypotheses —
"**Prop 6.1** is stated for **`r >= 2`** and for a factor of `p(pi)` whose
multiplicity satisfies the **minor** window `d_r/(n - M_r) >= V_r >= 1`" — a tower
statement. The *contribution-zero* half is not: it is FRONTIER-EXACT's
`(1 - delta^0)^+ = 0`, Keller-only.

**D1-PIN** (`:328-334`); the review splits its Moh inputs (`review:159-163`): "CEILING
half: Def 5.1(1) at level 1 … FLOOR half: JAC-FIBRE + slope `>=1` is Moh-free. The
closed number `m(1-delta_1)/(n+m)` uses Lemma 5.2." The `sum_B V_2(B) <= u` constraint
is NU-TWO (`CH:352`, `review:156`, CH DISCLOSURE (3) `:762-764`): "Disjointness of
bottom-major discs inside the unique major child `D_{s-1}` of the root ball (NU-TWO)".

**HARMONIC-BOUND** is the sharpest illustration that "no H2" is not "no hypotheses"
(`integration16:50-54`): "(degree-minimal, Moh's gauge, NU-TWO, Lemma 6.1,
`2 <= d < e`) … **NOT** for every noninvertible Keller pair (false of automorphisms;
"unconditional" in the producer meant "no H2")." The coordinator bindings say the same
from above (`integration17:7-10`, identical at `CH:716-721`): "Scope: Keller,
noninvertible, degree-minimal, Moh's gauge (GEN, NU-TWO) … **H2 only where the window
is quoted**."

### 2.4 The one non-obvious dependency: `M_s = n-2` is load-bearing at `r = 1`

Neither report isolates this, and it answers "does the pin survive off NU-TWO?".
With `c := n - M_s - 1` (RADIUS-ORDER in general form, `box/moh_skeleton_N.py:189-193`):

```text
   lambda_g(delta_r) = -n(1-delta_r)c/(n-M_r),
   floor(r) - ceiling(r) = (1-delta_r)[1 - (n+m)c/(n-M_r)],
   at r = 1  (n - M_1 = n + m):   floor(1) - ceiling(1) = (1-delta_1)(1-c).
```

The coincidence holds **iff `c = 1`, i.e. `M_s = n-2`** (`delta_1 = 1` is excluded: it
gives `lambda_g(delta_1) = 0`, hence `N = 0`, against `N >= 2`). Perturbation check on
census-legal skeletons with `M_s` lowered, exact `Fraction`s:

```text
  n=48 m=32 Ms=(-8,46) c=1  floor=ceiling=1/3      PINNED
  n=48 m=32 Ms=(-8,45) c=2  floor=-13/72 ceil=13/18   gap=-65/72
  n=48 m=32 Ms=(-8,44) c=3  floor=-20/27 ceil=10/9    gap=-50/27
  n=64 m=48 Ms=(16,62) c=1  floor=ceiling=-72/25   PINNED
  n=64 m=48 Ms=(16,61) c=2  gap=14/5     Ms=(16,60) c=3  gap=224/75
```

So `D1-PIN`/`D1-STAR` are not "Keller + Lemma 5.2 + Def 5.1(1)"; they are "Keller +
Moh's tower **with its top level normalised**". The normalisation is available twice
over, and NU-TWO's route needs (MIN). The pin is therefore a degree-minimal theorem —
for a reason (`M_s = n-2`) independent of the reason the *filter* is degree-minimal
(`Σ_B V₂ ≤ u`, `K ≥ 16`).

## 3. Part (2): the reducible branch under EXACT-N

### 3.1 `N` is unchanged — a partition, not an omission

FRONTIER-EXACT sums `(1-δ⁰)⁺` over the `D` roots of `g`; `δ⁰ ≥ 1` is "exactly the
condition that the branch be non-proper" (`CH:239-240`) and contributes `0`. D1-STAR
gives every root of a bottom-major disc the same `δ⁰ = δ₁ + n(1-δ₁)/(n+m) < 1`
(`CH:373`); DETECTOR-NULL gives `δ⁰ ≥ 1` on every minor branch; the covering is
exhaustive (`CH:685-688`: "every subdisc of a tower disc is major … or minor
(Prop 6.1), and a tower halting above level 1 leaves its roots in minor discs,
contributing 0"). Hence

```text
 {D branches of a generic fibre} = PROPER (bottom-major discs) ⊔ NON-PROPER (minor discs)
 N = sum over the PROPER block only;   the NON-PROPER block contributes exactly 0.
```

`A_F` is reached only through the non-proper block: such a branch has `f(tau) -> a_0`
finite while `x -> infinity`, so `(a_0, c_2)` is a point of the asymptotic set. **The
entire reducible/irreducible distinction is a statement about the zero-contributing
block.** `N = Σ_B V₂(B) q(B)` is unchanged when `A_F` is reducible — not because the
derivation was careless about `A_F`, but because it is orthogonal to it.

### 3.2 What DOES change, counted exactly

> **NONPROPER-COUNT (PROVED-HERE, UNREVIEWED; H2-free, scope of D1-STAR).** For a
> degree-minimal Keller pair in Moh's gauge, the number of Puiseux branches of a
> generic fibre `{g = c_2}` that escape to `A_F` is
> ```text
>     R := D - Σ_B a_1(B) = D - e·Σ_B V_2(B) = e(K - Σ_B V_2(B)) = D - N(d+e)/((1-δ_1)d),
> ```
> determined by the skeleton and the bottom-disc `V`-packet — the same datum that
> determines `N`.

*Proof.* The proper branches are exactly the `Σ_B a_1(B) = e Σ_B V₂(B)` roots of the
bottom-major discs (§3.1); `D` is the total; `Σ_B V₂(B) = N/q` by D1-PIN. ∎

Three consequences in the campaign's own currency.

- **PLACE-LEDGER's `S·n`.** `D - T = kappa + S n` over the places at infinity of a
  generic net member (`notes.md:20112-20115`), `Lambda = S n` the non-proper places,
  `kappa` the proper ones. The identification of CH's places with PLACE-LEDGER's is a
  named GAP (`integration17:72-74`), so I do **not** assert `Lambda = R`.
  Unconditional: `R = Σ_{non-proper places} ν_γ ≥ Lambda`, each place carrying
  `ν_γ ≥ 1` branches.
- **Reducible `A_F` splits `Lambda`.** Under H2 every dicritical dominates the single
  curve `A_F` and `Lambda = S·n_A`. With `A_F = A_1 ∪ … ∪ A_c` the same count reads
  `Lambda = Σ_l s_l n_{i(l)}`, `i(l)` the component dicritical `l` dominates. This is
  the exact sense in which "`S·n`" is the H2 specialisation of a component-indexed
  sum, and it is the **only** ledger entry reducibility touches inside the machinery.
- **Minor-disc structure.** Reducibility is a statement about how the `R` non-proper
  branches group into places and how those places' limit points group into components
  — i.e. about the sub-trees of the MINOR discs, which D1-STAR does **not** pin
  (D1-STAR is about bottom major discs only, `CH:365-376`).

### 3.3 The non-proper half of `(JF)`

The D1 lane proved `(JF)` for every branch but consumed only the proper half: its
controls are polynomial automorphisms, which have **no** non-proper branch
(`CH:753-755`). The non-proper half is one line, and it reaches `A_F`.

> **THEOREM NONPROPER-RATE (PROVED-HERE, UNREVIEWED).** For `f,g` monic in `y`, `F`
> dominant, generic `c_2`, and **every** root `tau` of `g - c_2`,
> `ord_t(f(tau) - a_0) = δ⁰_tau - 1 + ord_t J(tau)`, with `a_0` the `t^0`-coefficient
> of `f(tau)`. For a Keller pair the last term is `0`, so at every non-proper branch
> `f(tau)` approaches its limit `a_0 ∈ A_F` at the exact rate `t^{δ⁰-1}`;
> equivalently, at a place `γ` of ramification `ν_γ` over `x = ∞`,
> `ord_γ(f - a_0) = ν_γ(δ⁰_γ - 1) ∈ Z_{>0}`.

*Proof.* `(JF)` (CH §3.1) plus `ord_t g_y(tau) = -δ⁰_tau`, which is CH's own
`Λ(δ⁰) = 0` computation (`CH:242-249`) — that computation nowhere assumes `δ⁰ < 1`; it
uses only that `δ⁰` is the frontier of `tau` on the tree of `g - c_2`. ∎

> **COROLLARY STRICT-FRONTIER (PROVED-HERE, UNREVIEWED).** For a Keller pair in the
> gauge, **no** branch of a generic fibre has `δ⁰ = 1`: proper `⟺ δ⁰ < 1`, non-proper
> `⟺ δ⁰ > 1`, strictly.

*Proof.* `δ⁰ = 1` gives `ord_t(f(tau) - a_0) = 0`, i.e. `f(tau) - a_0` has a nonzero
`t^0` coefficient, contradicting the definition of `a_0`. (`f(tau) - a_0 ≢ 0`: a Keller
pair is étale hence quasi-finite, so no fibre branch maps to a point.) ∎

This sharpens `CH:239-240`: the value `1` is a **gap** in the frontier spectrum of a
Keller pair, and `ν_γ(δ⁰_γ - 1)` is a positive integer at every non-proper place — the
analogue on the minor block of "`N ∈ Z`" on the major block.

**CONTROL R** (`nonproper_rate.py`, exact over `Q(c_2)`; 19 rows, 38 places,
**113 checks, 0 failures**, 0.4 s). Rows are non-Keller dominant pairs whose generic
fibre is rational, parametrised so every order is that of an explicit rational
function; both places per row; `a_0 ≠ 0` rows included. Verified per branch: `(JF)`;
NONPROPER-RATE; and that **every** non-proper branch has `ord_t(f - a_0) > 0` —
STRICT-FRONTIER's local content.

```text
  row                  place  ord(f-a0)  ord g_y  ord J  delta^0  proper  (JF)
  f=y,   g=y^2+xy      s->0        1       -1       1       1       NO     OK
  f=xy,  g=y^2+xy      s->0        2       -1       2       1       NO     OK  (a_0=c_2)
  f=y,   g=y^3+xy^2    s->0      1/2     -1/2       1     1/2       NO     OK
  f=y,   g=y^5+xy^2    s->oo    -1/3     -4/3    -2/3     4/3      yes     OK
  … 38 places; full table in the driver's stdout
```

The third row matters: a **non-Keller** pair can have a non-proper branch with
`δ⁰ = 1/2 < 1`. The proper `⟺ δ⁰ < 1` dichotomy is Keller-specific, and the control
exhibits its failure quantitatively — CH's "tested by failure" discipline.

### 3.4 Where H2 actually sits, in tree terms

`γ ↦ (a_0(γ), c_2)` sends the non-proper places of `{g = c_2}` onto `A_F ∩ {Y = c_2}`,
of cardinality `n_A^Y` at generic `c_2`. Continuing in `c_2` gives an action of the
monodromy of the `c_2`-line (minus a finite set), and the components of `A_F` are the
orbits of the induced action on `A_F ∩ {Y = c_2}`. Lemma NL (no component of `A_F` is
a line; `jc2-reducible-all-n-cage-opus5`, from Chau Thm 1) says no component is
`{Y = const}`, so every component dominates the `Y`-line. Hence

```text
  H2  ⟺  the c_2-monodromy is TRANSITIVE on the limit points of the non-proper places,
  and always  c := #components(A_F) ≤ n_A^Y ≤ Λ ≤ R = e(K - Σ_B V_2(B)).
```

> **COROLLARY NONPROPER-CAP (PROVED-HERE, UNREVIEWED).** At a degree-minimal Keller
> counterexample in Moh's gauge, `n_A^Y ≤ e(K - Σ_B V_2(B)) = D - N(d+e)/((1-δ_1)d)`,
> and `c ≤ n_A^Y`. If Chau's divisibility (`e | deg A_i`) transfers to the horizontal
> degree, `c ≤ K - Σ_B V_2(B)`.

The conditional clause carries **GAP[HORIZONTAL-DEGREE]** (bounded quantity:
`mult_{[1:0:0]} Abar_F ∈ [0, n_A]`, since `n_A^Y = n_A - mult_{[1:0:0]} Abar_F`). This
is the first cap on `A_F`'s size from the boundary tree — and it is in the **same
direction** as the companion razor the reducible branch already has, which is why §5
measures no kill.

### 3.5 The reducible residual as the record states it

Not cells — **one named OPEN plus a razor stack** (`notes.md:18412-18416`):

> "Reducible branch: Euler species retired with proofs; residual =
> OPEN[COMPANION-R0-REALISATION]/degree-cap + the razor stack (blocked only on
> declared-completion data)."

with, upstream, the reducible cage's profile census (13/27/90 profiles at `N = 6,7,8`;
residual `OPEN[CUSP-2-AT-CONTRACTED-ATTACHMENT]`) and `NO-DEG-CAP` (post-composition by
target automorphisms preserves `N`, Keller and the profile while `deg A_F` grows
without bound, so no degree/genus/delta gate can close the cage). Integration #14 §D.3
carries it as "The reducible branch and the counterexample census — unchanged"
(`int14:98-99`). `OPEN[COMPANION-R0-REALISATION]`'s currency is
`Σ deg D_i ≤ max(deg P, deg Q)` — "the ONLY reachable handle on companion degree"
(`notes.md:17669-17671`), an **upper** bound. What the branch needs in order to die is
a **lower** bound; NONPROPER-CAP supplies another upper bound.

### 3.6 Does the pinned `N` reprice it?

**No reducible-branch cell or case dies, and the branch is untouched *by design*.**

- The filter kills **Moh skeletons**, not campaign profiles, and is H2-free (§2, §4),
  so it applies **verbatim** to the reducible branch — same census, same `q`, same
  knapsack, same numbers. That is a genuine reprice: the reducible branch now inherits
  59.79% of groups dead at `D ≤ 120`, where before today it inherited nothing from the
  boundary at all.
- No reducible-branch object (profile, cage row, companion type, `R_0` condition) is a
  function of the skeleton, so none can die from it. `CH:568-570` says the
  corresponding thing on the H2 side: "NO (B2) or (B3) cell dies. The filter conditions
  Moh SKELETONS at a fixed `D`; a campaign cell `(N,D)` dies only if EVERY skeleton at
  that `D` fails for that `N`, and none does." The reducible branch has no `(N,D)` cell
  structure at all, so it cannot even be reached that way.
- The one place the machinery speaks about `A_F` is NONPROPER-CAP; §5 measures its
  kill: **zero**.

## 4. Part (3): the `N >= 6` frontier

### 4.1 The `N <= 5` closure is H2-FREE

- `N ≤ 3`: Orevkov (`notes.md:15648`), no hypothesis on `A_F`.
- `N = 4`: the pair-reviewed ledger line (`notes.md:17562-17573`) —
  "**N=4-CHECKED-CLOSED: no four-sheeted polynomial self-map of `C^2` has nonzero
  constant Jacobian.** Chain: Domrina–Orevkov I (mu2 track REPLAYED-SOUND; (1,2)
  closed by campaign Prop 4.1; (3,0) closed by campaign Cor 3.8 …) + Domrina II
  (censuses repaired; root gaps closed by Theorems R1/R2 …). MODULO: structure
  packages (F1)/(F2)/(S1)/(S2)/(S4)". Domrina's title is *the general case*; the audit
  records explicitly that it is the **campaign's own** `N=4` theorems that are
  H2-bound, not hers (`xmodel/domrina-1999-audit-sol56-20260901.md:304-310`): "Under
  H2 (`A_F` irreducible), Theorem 4.2 excludes `mu=1` at `N=4`. … The all-degree
  Theorem 7.B … proves under H2 and `N>=3` that no affine-image dicritical has
  `mu=1`. **It does not apply to reducible `A_F`.**"
- `N = 5`: Żołądek Theorem 6.12, quoted in the dependency audit
  (`xmodel/n5-soundness-grok46-20260902.md:96`): "**"Any Jacobian map `P` with
  `degtop P <= 5` is invertible."**" — no irreducibility hypothesis; and `:6`, "The
  residual after H2 is reducible `A_F`", i.e. the lane itself types its `N=5` closure
  as covering the reducible case. Typing carried: SOUND-BY-DEPENDENCY-AUDIT, with
  `OPEN[ZOLADEK-6.12-ARITHMETIC]` open (`:104-105`).

**So the reducible branch has the SAME `N_min = 6`.** If one refuses the literature
and uses only campaign-internal chains, the reducible branch's `N_min` drops to `4`
(the campaign's own `N=4`/`N=5` kills are H2-bound; its reducible `N=4` work reduced
only the `B0` sub-question to "the six (8,6)/(9,6) msolve types",
`notes.md:16343-16345`). Both readings are priced below.

### 4.2 The rerun (`nmin_reprice.py`, `D <= 120`, one core, 31 s)

`achievable()` and `qval()` are imported unmodified from the frozen `d1floor.py`; the
only change is that `(N_lo, N_hi)` is swept. Calibration first: the record's two
windows come out **to the unit**, including the per-degree table of `integration17:45-47`.

```text
== (UNI) INTEGRALITY at variable N_min, D in [48,120] ==
   window        assign        kill       %      groups   grpkill      %
   N>=2          902893      891820   98.77%      10637      5864   55.13%  [record 98.77/55.13]
   N>=4          902893      892439   98.84%      10637      6051   56.89%
   N>=6          902893      893340   98.94%      10637      6360   59.79%  <-- H2-FREE, post-frontier
   N>=4 <=16     902893      893706   98.98%      10637      6386   60.04%  [record 98.98/60.04]
   N>=6 <=16     902893      894607   99.08%      10637      6700   62.99%

   per-degree GROUP kills, MOH-SHARP-2 admissible degrees
       D   groups   N>=2   N>=4   N>=6   [4,16]   [6,16]      [record H2 column]
     105      264    195    203    216      209      222            209
     108      824    359    383    402      419      439            419
     112     1163    743    749    775      795      821            795
     117       60     39     45     45       47       47             47
     120     4104   2158   2190   2262     2390     2463           2390

   degrees with EVERY group killed:  NONE, in every window.
```

**Reading.** (i) The frontier upgrade `N ≥ 2 → N ≥ 6` is worth `+4.66` percentage
points of groups **with no hypothesis at all**, and recovers `6360/6386 = 99.6%` of the
record's H2 group kill. The filter was never window-driven (`CH:574-576`); it is now
nearly H2-independent as a *number*, not only as a mechanism. (ii) The `[4,16]` clip is
a genuine extra hypothesis, not a theorem: over the surviving assignments the
achievable pinned `N` takes **33 distinct values `≥ 6`, up to `N = 40`** (measured).
Under H2 the record's own statement is that the residual is `(B2) ∪ (B3)` **for
`N ≤ 16`** (`AUDIT.md:14908`) with `(B1)` reopening at `N ≥ 17` (`notes.md:17714`);
there is no proved ceiling on `N` on either branch. So `N ≥ 6` with **no** upper window
is the honest operative filter for both branches, and 59.79% is the operative number.
(iii) No degree is emptied in any window; `MOH-SHARP-2`'s `D_min ≥ 105` is neither
improved nor weakened; no `(B2)`/`(B3)` cell dies; no reducible-branch object dies.

A `D ∈ [121,200]` extension was launched on the same driver and had not returned inside
this lane's window; nothing above depends on it, and its expected content is a wider
"no degree emptied" range, not a new kill.

### 4.3 REBASE onto Moh's own search conditions (sibling lane, landed mid-lane)

`time-function-calibration-d48-opus5-20260902` (banked 11:41Z, *not* among my charged
inputs; found on disk and in the memory index while sealing) establishes that
`box/moh_skeleton_N.py`'s `census()` implements Moh's search conditions (1)–(7) and
Def 5.1(2) **only, not (8)–(11)**, so every integration-#17 filter number describes a
strict SUPERSET of Moh's admissible skeletons. Its instruction — rebase any census
number before quoting it — applies to §4.2, so I re-ran the sweep through that lane's
own gate (`box/tfcal-drivers-20260902/mohcond.py`; my driver `rebase_mohcond.py`, 51 s):

```text
 STAR-CONGRUENCE gate (that lane's FULLY PROVED level-1 form, a_1 = eV_2 = 0 or 1 mod Delta_1)
   base: 137,319 assignments / 9,630 groups at D <= 120
     N>=2       129,695 (94.45%)   groups 5,730 (59.50%)
     N>=6       130,607 (95.11%)   groups 6,105 (63.40%)   <-- H2-free
     N>=4 <=16  130,849 (95.29%)   groups 6,133 (63.69%)   <-- H2
 MOH_ALL gate ((10) for j=2..s-1 + star; (10) is an OCR reconstruction with the
 alpha = 0 branch (11) missing, so ITS kills are a CEILING)
   base: 329 assignments / 287 groups at D <= 120
     N>=2            0 (0.00%)     groups     0 (0.00%)
     N>=6           27 (8.21%)     groups    27 (9.41%)    <-- H2-free
     N>=4 <=16      52 (15.81%)    groups    40 (13.94%)   <-- H2
   NO degree is emptied under either gate, in any window.
```

**What survives the rebase and what does not.** (i) The *headline of §4.2 survives on
the proved gate*: `N >= 6` H2-free kills 63.40% of groups against the H2 window's
63.69% — 99.5% recovery, the same picture. (ii) On the (reconstructed, ceiling-typed)
full Moh gate the picture changes in one respect worth recording: there the
unconditional `N >= 2` filter kills **nothing** (every one of the 287 groups admits an
integer `N >= 2`), so the entire kill comes from the frontier — `N >= 6` kills 9.41% of
groups H2-free against the H2 window's 13.94%, i.e. recovery drops to 67%. The
frontier, not H2 and not integrality alone, is what does the work on Moh's own
census. (iii) Nothing in §§2–3 or §5 depends on the census size: the scope audit is a
hypothesis question, and §5's discriminating test returns zero violations on the larger
census, hence also on every sub-census.

## 5. Part (4): direct verdict, and the discriminating computation — run, not proposed

**VERDICT: (c) PARTIALLY SUBSUMED, boundary at proper/non-proper.**

```text
 SUBSUMED (one program, no separate instruments): the Moh skeleton census;
   q = (1-delta_1)de/(d+e); N = sum_B V_2(B) q(B); the integrality filter and
   condition (15); PIN-NOT-CEILING; HARMONIC-BOUND; N-CEILING; N_min = 6.  All
   H2-free (§2); all apply verbatim to a reducible-A_F counterexample; all deliver
   the same 59.79% group kill at D <= 120.
 NOT SUBSUMED (untouched by design -- it lives in the zero-contributing block):
   OPEN[COMPANION-R0-REALISATION]/degree-cap, the razor stack, the reducible cage's
   profile census and OPEN[CUSP-2-AT-CONTRACTED-ATTACHMENT], NO-DEG-CAP.  The
   machinery's only statement about them is NONPROPER-CAP, an UPPER bound in the
   same direction as the razor they already have.
```

**The single cheapest discriminating computation** is the one that decides whether
NONPROPER-CAP can become a kill: test the surviving assignments against the reducible
branch's own floor on `A_F`. One arithmetic pass (30 s) on the same census — run here
(`nonproper_count.py`, `D ≤ 120`, `N_min = 6`):

```text
  R = e(K - sum_B V_2(B))  over the 9,553 assignments (4,277 groups) surviving the
  N >= 6 integrality filter:
     FREE test  R >= 2   (reducible needs >= 2 components; Lemma NL)  -> 9,553 pass
     CHAU test  R >= 2e  (every component degree a multiple of e)     -> 9,553 pass
     groups killed by the reducible test alone : 0
     min R over surviving assignments : 6 = 2e, attained at D=48, K=16, e=3,
                                        sum V_2 = 14, pinned N = 14
     K - sum_B V_2(B) ranges over [2, 34]  (so c <= 34 under GAP[HORIZONTAL-DEGREE])
```

**Zero kills, and `R ≥ 2e` is tight but never violated.** The discriminator has
returned: the exact machinery does not reprice the reducible branch beyond the skeleton
filter it shares with the H2 branch. The next cheapest thing that could change this is
not another census pass but the missing direction —
`OPEN[COMPANION-DEGREE-FLOOR]`. A floor `n_A^Y ≥ φ(N)` would compose with
NONPROPER-CAP into `φ(N) ≤ e(K - N/q)`, a two-sided condition on the skeleton, and the
same 30-second pass becomes a kill count.

## 6. Corrections to the record

```text
 K1. "N <= 5 closed" must NOT be carried as an H2-side statement.  It is H2-free
     (§4.1); the campaign's own N=4 chain being H2-bound (Thm 4.2, 7.B) is a fact
     about that chain, not about the closure.  Consequence: the reducible branch's
     N_min is 6, not 4, and every reducible-branch lane may consume N >= 6.
 K2. Integration #17 item 7 and CH §5.2 report the filter's unconditional column as
     "N >= 2".  Post-frontier it is "N >= 6" (55.13% -> 59.79% of groups at D <= 120).
     The H2 column [4,16] should be re-labelled: its lower end is superseded and its
     upper end 16 is the H2 residual WINDOW, not a bound on N -- the achievable
     pinned N reaches 40 on the surviving census.
 K3. CH DISCLOSURE (1) is right that no noninvertible Keller pair exists to test on,
     but understates a testable gap: the automorphism controls exercise only the
     PROPER half of (JF).  Consumers of "delta^0 >= 1 iff non-proper" should carry
     STRICT-FRONTIER instead: for a Keller pair delta^0 = 1 is impossible, and for a
     NON-Keller pair delta^0 < 1 does not imply proper (CONTROL R, f=y, g=y^3+xy^2:
     delta^0 = 1/2, non-proper).
 K4. The D1-PIN coincidence is not "Lemma 5.2 + Def 5.1(1)"; it additionally needs
     M_s = n-2 (§2.4).  Both reports state the tower with M_s = n-2 and neither
     isolates it as load-bearing at r = 1.  This matters for any attempt to run the
     pin off Moh's search list, e.g. at a non-minimal representative.
 K5. APPROACHES.md:12-15 ("Stop all reducible-row work permanently") is about the
     rank-four BLOCK branch, not about reducible A_F; the two senses of "reducible"
     should be distinguished in any future overlay.
```

## 7. Opens raised, with bounded quantities

```text
OPEN[COMPANION-DEGREE-FLOOR]  (new; the exact residue of this lane).  NONPROPER-CAP
   and the companion razor both bound A_F's degree from ABOVE; the reducible branch
   dies only from a LOWER bound.  BOUNDED QUANTITY: n_A^Y = #(A_F ∩ {Y=c_2}) at a
   degree-minimal counterexample, an integer in [c, e(K - sum_B V_2(B))], c >= 2.
   Composing a floor with NONPROPER-CAP is a 30-second census pass (§5).
GAP[HORIZONTAL-DEGREE]  (new).  Chau's divisibility bounds deg A_i, not the
   horizontal degree.  BOUNDED QUANTITY: mult_{[1:0:0]} Abar_F in [0, n_A].  Needed
   to upgrade "c <= n_A^Y" to "c <= K - sum_B V_2(B)".
OPEN[MINOR-INTEGRALITY]  (new; the minor-block analogue of the integrality filter).
   STRICT-FRONTIER makes nu_gamma(delta^0_gamma - 1) a POSITIVE INTEGER at every
   non-proper place.  BOUNDED QUANTITY: per surviving skeleton, the multiset of
   (nu_gamma, delta^0_gamma) over the minor discs.  NOT cheap as things stand: the
   sub-tree of a minor disc is not pinned by D1-STAR, so delta^0 there is not a
   function of the skeleton; making it cheap is OPEN[NONPROPER-DEGREE].
CARRIED UNCHANGED: BRANCH-ORBITS, V-FLOOR, STAR-REALISABILITY,
   COMPANION-R0-REALISATION, CUSP-2-AT-CONTRACTED-ATTACHMENT, MOH-14, MOH-ENDGAME,
   NONPROPER-DEGREE, ZOLADEK-6.12-ARITHMETIC, SUBRECT-ORBIT-BRIDGE, ANTICANON-DEFECT,
   SAT-MASS, DELTA-AFF-VS-N.  The PLACE-LEDGER identification stays a GAP; nothing
   here consumes it.
```

## 8. FALLACY-v2 audit

* **Flag/place/series.** The one degree-like integer CH excluded — `n_A = deg Abar_F` —
  is reintroduced under its own name, `D` is used for Moh's `n` from §3 on, and `n_A`
  vs `n_A^Y` is a named GAP, never elided. Three trees stay apart (`eta`-adic tower;
  `t`-adic major tower; the sub-trees of `D_1` and of the minor discs); the reducible
  datum sits on the third and is never transported to the second. "Reducible" in the
  rank-four-block sense is separated from "reducible `A_F`" (K5).
* **Per-ray/exit-set charge; carrier/attainment.** No exit price, no `charge_basis`
  line. Each branch of `g - c_2` is charged once, in exactly one block; the partition
  is proved exhaustive by citation (`CH:685-688`). `R` counts BRANCHES, `Λ` counts
  PLACES, and the inequality between them is used in the safe direction only.
  NONPROPER-CAP is an upper bound and used only as one; `min R = 2e` is MEASURED over
  an enumerated finite set with no claim beyond `D ≤ 120`, its tightness reported as
  attained at one named row, not as a law. The filter kill counts are floors in the
  record's own sense (`CH:762-764`), re-run from the frozen code, not re-derived.
* **Pole/interior; floor/attainment at the frontier.** `(star)` is invoked only through
  CH's proved statement; the new use extends it to `ord ≥ 0` branches, where the `a_0`
  subtraction is what makes it legitimate, and `f(tau) - a_0 ≢ 0` is argued
  (quasi-finiteness of an étale map), not assumed. STRICT-FRONTIER excludes `δ⁰ = 1` by
  contradiction, and CONTROL R exhibits a non-Keller row with `δ⁰ = 1/2` at a
  non-proper branch — the Keller hypothesis is tested by failure.
* **Variable/ring map; no cap or analogy.** `g_y` is a genuine partial derivative; all
  CAS is exact (`Fraction`s for the census; sympy over `Q(c_2)` for CONTROL R, orders
  as `ord_s(num) − ord_s(den)` of a cancelled rational function converted by
  `ord_t = ord_s/ord_s(t)`, the factor computed per place). Where the reducible
  branch's own floor is missing I return `OPEN[COMPANION-DEGREE-FLOOR]` with its
  bounded quantity rather than substituting the razor's upper bound for it.

## 9. Typed verdict block

```text
LANE       REDUCIBLE-BRANCH-REPRICE (charge 18:36Z)
SCOPE      Keller, noninvertible.  Degree-minimality and Moh's gauge are used exactly
           where §2's table says.  H2 is used NOWHERE except to reproduce the
           record's [4,16] column for calibration.
PROVED HERE (all PROVED-HERE, UNREVIEWED)
 SCOPE-AUDIT [2]  the table; M_s = n-2 is load-bearing for the D1-PIN coincidence at
     r = 1 (gap = (1-delta_1)(1-(n-M_s-1))), verified by perturbation.
 NONPROPER-COUNT [3.2]  # non-proper branches = D - e sum_B V_2(B) = e(K - sum V_2).
 NONPROPER-RATE [3.3]   ord_t(f(tau)-a_0) = delta^0 - 1 + ord_t J at EVERY branch.
 STRICT-FRONTIER [3.3]  Keller => delta^0 != 1; proper <=> delta^0 < 1, strictly.
 NONPROPER-CAP [3.4]    n_A^Y <= e(K - sum_B V_2(B)); #components <= n_A^Y.
 H2-AS-MONODROMY [3.4]  H2 <=> the c_2-monodromy is transitive on the limit points of
     the non-proper places: H2 is a statement about the minor-disc block alone.
MEASURED   nmin_reprice.py (D <= 120, 31 s): record's two columns reproduced to the
           unit incl. integration17:45-47's per-degree table; new H2-free column
           N >= 6 -- 893,340/902,893 assignments (98.94%), 6,360/10,637 groups
           (59.79%); no degree emptied in any of five windows; 33 distinct achievable
           N >= 6, max 40.  rebase_mohcond.py (51 s): the same sweep through the
           sibling lane's Moh-condition gates -- 63.40% (H2-free) vs 63.69% (H2) on
           the proved gate; 9.41% vs 13.94% on the reconstructed full gate, where the
           unconditional N >= 2 filter kills nothing at all.  nonproper_count.py
           (30 s): ZERO kills from either reducible test, min R = 2e attained.
           nonproper_rate.py: 113 exact checks, 0 failures, 19 non-Keller rows with
           non-proper branches.
DECISION   THE EXACT MACHINERY IS H2-FREE AND THE REDUCIBLE DATUM LIVES IN THE BLOCK
           IT PROVES CONTRIBUTES ZERO.  Verdict (c): one census and one filter for
           both branches; the reducible residual OPEN[COMPANION-R0-REALISATION]/
           degree-cap untouched by design.  The cheapest discriminating computation
           was RUN and returns zero kills; the missing direction is a LOWER bound on
           companion degree.
CORRECTED  K1..K5 (§6).
CONFIRMED  CH/RV/integration17's scope lines, read as written: H2 is quoted only at
           the window.  The record's filter numbers, re-run from the frozen drivers.
DISCLOSURE (1) No noninvertible Keller pair exists to test on; CONTROL R is on
               NON-Keller pairs and tests the general (ord_t J) law plus the Keller
               specialisation's local content, not the Keller case itself.
           (2) NONPROPER-CAP's component form is conditional on
               GAP[HORIZONTAL-DEGREE]; unconditionally it caps n_A^Y, not n_A.
           (3) The CH-places / PLACE-LEDGER-places identification is the record's GAP
               and is NOT consumed: R bounds Lambda from above, nothing more.
           (4) The D in [121,200] extension of §4.2 had not returned inside the lane's
               window; nothing here depends on it.
           (5a) The sibling lane `time-function-calibration-d48` landed mid-lane and
               was NOT a charged input; §4.3 rebases on it but consumes only its
               drivers, at its own typing (the (10) clause is an OCR reconstruction,
               so MOH_ALL kills are a ceiling).  §4.2's numbers are kept as printed
               because they are the record's own base and the calibration to
               integration17:45-47 is what licenses the new column.
           (5) (UNI) is the record's hypothesis, inherited unchanged; the
               hypothesis-free knapsack was NOT re-run at a new N_min (record cost:
               1317 s at D = 72 alone, CH:558-559).  These (UNI) numbers are
               comparable to the record's (UNI) numbers and to nothing else.
           (6) SIZE: body 40.8 KB against the charged 20-30 KB band.  The overrun is
               §2's hypothesis table with its verbatim source lines, §3.3's two proofs
               and control table, and the two measurement tables of §4.2 and §4.3 --
               kept complete rather than compressed, since the table IS the deliverable
               of part (1), the §4.2 calibration is what licenses the new column, and
               §4.3 was added at seal time to honour the sibling lane's rebase rule.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `40916`.
- Body SHA-256:
  `fd1f383a2882712ad2a288b2b023b464529570652cbd889778cd665c187c96be`.
- Frozen basis: `8127b8ace42269a26f5cdde7ecb30d3bcf0874d1`.
- Drivers (this lane, `box/reducible-reprice-20260902/`): `b6349f5a` nmin_reprice.py;
  `c76f5b8e` nonproper_count.py; `92ded32b` nonproper_rate.py; `859b2d9b` rebase_mohcond.py.
