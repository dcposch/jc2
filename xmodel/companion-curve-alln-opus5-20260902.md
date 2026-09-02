# COMPANION-CURVE-ALLN: the forced companion, and why (M') cannot see it

Lane: COMPANION-CURVE-ALLN · 2026-09-02 · Opus 5
Path-2 flagship. Desk-scale exact reasoning; CAS used and disclosed.

## 0. Custody, typing, scope, execution disclosure

Hash verification was the first action. All three frozen inputs matched the boxed
manifest exactly; the stop condition did not fire.

```text
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  rep-96-inner-opus5-20260901.md
bdd857c9d8c55fa000fcffee05f9f3084c5d073fb4d06285edf2af0d3c369339  reducible-all-n-r2-opus5-20260901.md
48d417d6980e52d61550a733f0dcded7d26a0c4e127677ac73bd544a8a00713b  b0-reducible-n5-opus5-20260831.md
```

Below **REP96**, **CAGE**, **N5** denote them in that order.

**Two files were consulted that are not charged inputs**, and both are disclosed
because load-bearing statements are read out of them:

- `xmodel/round1033-sheet-gate-opus5-20260831.md` — the *source* of `(M')`, which
  REP96 SS7 R4 quotes by line number without reproducing. Three items are taken
  from it, each re-derived here before use: SS7's block-free form, Prop 2.4's
  ceiling, (E)/Thm 5.2's Euler budget. Typed `[S]`.
- `refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf`,
  `8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f`, typed `[L]`.
  N5 SS5.3 and CAGE clause 1 route the shared-point-at-infinity and common-type
  clauses to it, and the charge sends the whole existence question through those
  clauses, so the paper was opened rather than paraphrased: Theorem 1,
  Corollaries 1-2 and the normalisation discussion, pp. 1-2.

**Typing.** `[P]` promoted; `[D]` derived here; `[L]` primary literature read
here; `[S]` consulted non-charged campaign file; `[A]` audit against a consumed
item; `[C]` machine-checked here. Nothing below is an attainment claim for a
Keller map: SS5's witness is a *curve pair*, not a counterexample, and is typed as
such throughout.

**Execution disclosure.** A shell was available and used. All computations are
exact: sympy 1.14.0 over `Q`, resultants, gcds, factorisation and integer
arithmetic only; no floating point enters any claim. Scripts are in `/tmp/comp/`,
and every number quoted in SS2, SS3.3-3.4, SS4 and SS5 was produced by them; the
randomised control of SS2.5 ran 33116 admissible configurations. No
AWS, no `msolve`, no `qqideal`, no `jc2-lean`, no canonical ledger.

**Scope.** The reducible-`A_F` branch RED-N of CAGE: `F` a noninvertible plane
Keller map of geometric degree `N >= 4`, `A_F = D_1 u ... u D_m` with `m >= 2` and
at least one affine-image dicritical with `mu = 1`. Notation is CAGE SS0's:
`c_l = mu_l s_l + K_l`, `W_i = sum_{l->i} s_l mu_l`, `a^{(i)} = N - W_i`, and
`K_tot = sum_l K_l = sum_p K_p` (CAGE SS0 and N5 SS1.4 respectively; equal, since
each `K_l` is distributed over its own correction sites).

**The two `b`s, kept apart, as the charge demands.** `b_dic` is the count of
affine-image dicriticals with `mu = 1` (THEOREM 7.B's symbol; a *consequence* of
H2). `b_br` is the number of **branched components** of `A_F`, the symbol of
`(RC2)` and of CAGE clause 2, forced to `1` at `N = 4, 5`. **Only `b_br` is used
below, and it is written `b_br` everywhere**, never `b`. A third `b` appears in
the source of `(M')` (`sigma = a + b`, the unramified-dicritical box count); it
occurs here only inside the quotation of Prop 2.4 in SS2.4 and is written `b_box`.

## 1. Verdict

Three findings, in decreasing order of consequence. Two are negatives; the charge
anticipated that and asked for the survivor to be exhibited if the data is
realizable. It is.

**F1 `[D]`+`[C]` — the collapse is total, and `(M')` is exhausted on the whole
reducible cage.** REP96 SS7 R4 reports that at the `N = 4` profile the block-free
`(M')` collapses to `chi_2 + sigma_2 = 1`, with the branched component's node count
`s_1` cancelling identically. That is the visible tip of an exact and completely
general phenomenon. At **every** `N >= 4`, on **every** profile in the CAGE-N-R2
ledger, with `a_p` supplied by `(LOC)` (SS2.2):

```text
    LHS(M'-bf) - RHS(M'-bf)  =  (N - 1) - K_tot - sum_i W_i * chi~_i ,
```

`chi~_i := chi_c(normalisation of D_i)`. Every `sigma_i`, `nu_i`, node count and
crossing count, on **every** component - branched and companion alike - cancels
identically. Granted Lemma A the right side is the Orevkov budget `(AGG)`; so
`(M'-bf)` **is** the budget and carries not one bit more. The general-`N` analogue
of `chi_2 + sigma_2 = 1` requested by task (1) exists, is profile-independent, and
is `sum_i W_i(chi~_i - 1) = 0`, whose unique consequence is Lemma A - already
promoted. This closes `OPEN[REP-96-MPRIME-COMPANION]` **NEGATIVE**: the identity
cannot "become binding once `D_2` is pinned"; it can never bind. SS2.4 diagnoses why
the same identity is fatal under `(H2)` and inert here.

**F2 `[D]`+`[C]` — the companion exists, at every `N`, and explicitly at
`(9,6,2)`.** SS3.2 pins the complete forced datum (C1)-(C11); SS4 exhibits a uniform
family realising it for every coprime `(d,e)` with `d,e >= 2`, every multiplicity,
every value of the Chau invariant, with Gate EMB automatic. **There is no `N_0`.**
At the `(9,6,2)` substrate the datum is pinned completely (SS5.2) and a witness is
machine-verified (SS5.3): `D_2 : xi -> (xi^3 + xi + 1, xi^2 + 3)`, an immersive
nodal cubic with matching Chau invariant, meeting `D_1` in 12 distinct transverse
points, avoiding all four nodes of `D_1`, Bezout ledger `27 = 12 + 15`. Every
promoted local, numerical and topological constraint of the `N = 4` reducible cage
is satisfied by the pair. It is **not** a Keller counterexample (SS5.5).

**F3 `[L]`+`[A]` — Chau re-read: a sharper pin and two inverted formulas.**
Theorem 1 pins components harder than CAGE clause 1's paraphrase: the *same*
leading pair `(A,B)` serves every component, so the shared invariant is the single
scalar `A^e/B^d`; and the "common type `u = c v^{d/e}`" is common only in `c^e`.
Corollary 1's printed leading form and Corollary 2's radical are inverted; the
correct ones are `B^d u^e - A^e v^d` and `c^e = A^e/B^d`, machine-verified on
`xi -> (2 xi^3, xi^2)`. Invisible in the monic normalisation used so far, so
nothing banked is disturbed. SS3.3.

**Lane verdict.** `COMPANION-CURVE-ALLN: CLOSED-NEGATIVE as an obstruction lane.`
The forced companion is not a route to an all-degree contradiction: the identity
charged to constrain it is information-free, and the datum it must carry is
realizable at every degree. The `(9,6,2)` row survives this attack on the merits.
The residue is redirected, not lost: SS3.5 lists three load-bearing negatives saying
where not to spend budget, and SS6-SS7 name the successors that do carry decision
power.

## 2. Task (1): the block-free (M') at general N

### 2.1 The identity, restated exactly, with its hypotheses

`(M')`'s block-free form is quoted by REP96 SS7 R4 from its source `[S]` SS7:

> Each irreducible component `D_i` has its own constant `a^{(i)} >= 1` on
> `D_i \ Sing(D)`, and
> `sum_i a^{(i)} chi_c(D_i \ Sing D) + sum_{p in Sing D} a_p = 1 - d chi_c(V)`.

Objects: `d = N`; `V = C^2 \ A_F`, so `chi_c(V) = 1 - chi_c(A_F)`;
`a^{(i)} = #F^{-1}(pt)` on `D_i \ Sing(A_F)`, constant there by the block-free
covering lemma; `a_p = #F^{-1}(p)`. It is the stratification
`chi_c(F^{-1}(A_F)) = sum_i a^{(i)} chi_c(D_i \ Sing D) + sum_p a_p` set against
the Keller-only Euler budget (E), `chi_c(F^{-1}(A_F)) = 1 - N chi_c(V)`. Only
Keller is used; `(H2)`+`(H3)` are what collapse it to a single `a`.

*Control that the reading is right.* Under `(H2)`+`(H3)`: `m = 1`, `chi~ = 1`,
`chi_c(D \ Sing D) = 1 - nu - s`, `a^{(1)} = a`, and the display becomes
`a(nu + s - 1) - sum_p a_p = N nu - 1`, verbatim `(M')`. `[A]`

### 2.2 THEOREM COLLAPSE-N

Write `Sigma := Sing(A_F)`, `sigma := |Sigma|`, `sigma_i := |Sigma n D_i|`,
`r_{i,p} := #eta_i^{-1}(p)` (zero off `D_i`),
`nu_i := sum_{p in Sigma n D_i}(r_{i,p} - 1)`, `chi~_i := chi_c(D~_i)`. Every
correction site lies in `Sigma` (a critical point of `eta_i` makes `D_i` singular),
so `sum_{p in Sigma} K_p = K_tot`.

> **THEOREM COLLAPSE-N `[D]`.** Assume only: each `D~_i` is smooth irreducible
> with `chi_c(D~_i) = chi~_i`, `a^{(i)} = N - W_i`, and `(LOC)`
> `a_p + sum_i r_{i,p} W_i + K_p = N` at every `p in Sigma`. Then
>
> ```text
>    LHS(M'-bf) - RHS(M'-bf) = (N - 1) - K_tot - sum_i W_i chi~_i .
> ```
>
> Hence `(M'-bf)` holds **iff** `sum_i W_i chi~_i + K_tot = N - 1`. Granted the
> Orevkov budget `(AGG)` `sum_i W_i + K_tot = N - 1`, this is equivalent to
> `sum_i W_i (chi~_i - 1) = 0`, i.e. - since `W_i >= 1` and `chi~_i <= 1` for any
> smooth affine curve - to `chi~_i = 1` for every `i`, which is Lemma A.

*Proof.* `eta_i` is injective off `eta_i^{-1}(Sigma)`, so
`chi_c(D_i \ Sigma) = chi~_i - sum_{p in Sigma} r_{i,p} = chi~_i - sigma_i - nu_i`,
and `chi_c(A_F) = sum_i (chi~_i - sigma_i - nu_i) + sigma`. Summing `(LOC)` over
`Sigma` and using `sum_{p in Sigma} r_{i,p} = sigma_i + nu_i`,

```text
   sum_{p in Sigma} a_p = N sigma - sum_i W_i (sigma_i + nu_i) - K_tot .
```

Substitute both into the left side, with `a^{(i)} = N - W_i`:

```text
LHS = sum_i (N - W_i)(chi~_i - sigma_i - nu_i)
        + N sigma - sum_i W_i (sigma_i + nu_i) - K_tot
    = sum_i (N - W_i) chi~_i - N sum_i (sigma_i + nu_i) + N sigma - K_tot ,
```

the `W_i (sigma_i + nu_i)` terms cancelling in pairs. The right side is

```text
RHS = 1 - N chi_c(V) = 1 - N + N chi_c(A_F)
    = 1 - N + N sum_i chi~_i - N sum_i (sigma_i + nu_i) + N sigma .
```

Subtract: the two `-N sum_i (sigma_i + nu_i)` and the two `N sigma` cancel, and
`sum_i (N - W_i) chi~_i - N sum_i chi~_i = - sum_i W_i chi~_i`, leaving
`LHS - RHS = (N - 1) - K_tot - sum_i W_i chi~_i`. []

**Every singularity variable has vanished** - `sigma_i`, `nu_i`, `sigma`, the
split of `Sigma` into self-singularities and crossings, the `r_{i,p}`, the node
counts of *all* components. The identity's entire content on the cage is one scalar
equation in `(W_i, chi~_i, K_tot, N)`.

### 2.3 The general-N analogue of `chi_2 + sigma_2 = 1`, per profile

Task (1) asks for the exact per-profile analogue. It is COLLAPSE-N, and it is the
*same* equation on every profile:

```text
   (2.1)    sum_i W_i (chi~_i - 1) = 0 ,   equivalently   chi~_i = 1 for all i.
```

Componentwise, `chi~_i = 1` reads `chi_c(D_i) + (self-branch excess) = 1`; for a
component whose only singularities are `sigma_i^{self}` nodes it is literally
`chi_i + sigma_i^{self} = 1`. **REP96's (7.1) is exactly the `i = 2` instance of
(2.1)**, and it looked like a constraint on `D_2` only because Lemma A had already
been spent on `D_1` and the remaining unknown was solved for; fixing `D_2`'s
normalisation first, the same algebra would have "constrained" `D_1` and cancelled
`sigma_2`. There is no branched/companion asymmetry in `(M')` and no
profile-dependence. Uniformly at every `N` and every ledger row:

| question | answer from COLLAPSE-N |
|---|---|
| does the branched component's singularity data always cancel? | **yes**, identically, at every `N`, on every profile |
| does the companion's cancel too? | **yes** - the charge's premise that `(M')` "constrains only `D_2`" is an artefact of the order of substitution |
| what does `(M')` force on the companion: genus, `chi`, node count, crossings `j` with `D_1`? | **genus and `chi~` only**: `g_i = 0` and one place at infinity, i.e. Lemma A. Node count: nothing. `j`: nothing |
| exact analogue of `chi_2 + sigma_2 = 1` per profile | (2.1), profile-independent |

### 2.4 Why the same identity is fatal under (H2) and inert here

REP96 SS7 R4's control - no nodal `N = 4` residual survives `(M')` under `(H2)` -
is correct, and the diagnosis matters. The kill does not come from the identity but
from combining it with **inequalities**: `a_p >= 0` and the ceiling `a <= N-2`.
Prop 2.4 `[S]` proves the latter as
`sigma = a + b_box = N - sum_{j: e_j>=2} delta_j e_j <= N - 2`, at the stated scope
*every component of `A_F` lying in the branch locus* - the subtraction needs a
ramified dicritical over that very component. So in RED-N the ceiling is

```text
   a^{(i)} <= N - 2   for branched D_i    <=>   W_i >= 2   for branched D_i,
```

which is automatic (`W_i >= mu_l >= 2`), and it is **not** available on companions:
`a^{(companion)} = N - w` can be `N - 1`. This is a genuine flag/place separation -
"component of `A_F`" is not "branch component" - and mis-applying Prop 2.4 to a
companion would kill the promoted `N = 4` profile `W = (1,2)` outright and falsely.
`[A]` **AUDIT-CC-1.**

With the ceiling neutralised, all that is left of `(M')` in RED-N is `a_p >= 0` and
`a_p <= a^{(i)}`. Both are *consequences* of `(LOC)`:
`a_p = N - sum_j r_{j,p}W_j - K_p >= 0` is (LOC-1)/(LOC-2), and
`a_p <= N - r_{i,p}W_i <= N - W_i = a^{(i)}` is automatic. So:

> **Corollary `[D]`.** In scope RED-N, the entire content of `(M')` - identity,
> ceiling and fibre bounds - is implied by `(LOC)` + `(AGG)` + Lemma A, all three
> promoted. `(M')` is not an independent gate in the reducible branch.

This independently reproduces, and extends from `(AGG)` to the unequal-`a^{(i)}`
form of `(M')`, N5 SS1.4's finding that the aggregate Euler identity carries no
information beyond the Orevkov budget with the local fibre identities. `[A]`

### 2.5 Controls

*Positive control (a realized configuration).* The SS5 witness pair - the `(9,6,2)`
curve with its 4 nodes, plus the nodal cubic `xi -> (xi^3+xi+1, xi^2+3)`, meeting
in 12 transverse points - has `W = (2,1)`, `K_tot = 0`, `chi~ = (1,1)`,
`a^{(1)} = 2`, `a^{(2)} = 3`, `Sigma` of size 17, `(sigma_1,nu_1) = (16,4)`,
`(sigma_2,nu_2) = (13,1)`, and `a_p` from `(LOC)` equal to `0` at the four
`D_1`-nodes, `1` at the twelve crossings, `2` at the `D_2`-node. Then
`LHS = 2(-19) + 3(-13) + 14 = -63` and `RHS = 1 - 4(1 - (-15)) = -63`. `[C]` The
identity is satisfied **exactly** by a configuration assembled by hand from two
independently chosen curves, with no map anywhere in the construction and none
claimed. That is the point: `(M')` cannot tell that configuration from a genuine
`A_F`, so it cannot separate.

*Negative controls.* Replacing `chi~_2 = 1` by `0` (a companion with two places at
infinity, e.g. a hyperbola) gives `LHS - RHS = 1`; by `-1`, gives `2`; by `-3`,
gives `4` - matching `(N-1) - K_tot - sum_i W_i chi~_i` on the nose in all three.
`[C]` So the identity does detect the one thing it can detect, and detects nothing
else.

*Randomised control.* 33116 admissible configurations: `N in [4,12]`,
`m in [2,4]`, `W_i in [1,4]`, up to 8 singular points with random branch vectors
and random `K_p in {0,1,2}`, **retaining only those with
`sum_i W_i + sum_p K_p = N - 1`** and `a_p >= 0`. With `chi~ = 1`: **0/33116
failures**. With `chi~_i` free in `[-3,1]`: **0/33116 mismatches** with
`LHS - RHS = (N-1) - K_tot - sum_i W_i chi~_i`. `[C]` An earlier run reported mass
failures; the harness was wrong, not the theorem - it let `K_tot` float free of
`sum_p K_p`, violating the hypothesis. Reported because a reviewer re-running a
naive harness will hit the same trap.

## 3. The forced companion datum at general N

### 3.1 What a companion is

Fix a profile from the CAGE-N-R2 ledger. A component `D_i` is **branched** iff it
owns a carrier with `mu_l >= 2`; there are `b_br` of these, `1 <= b_br <=
floor((N-2)/2)`. Every other component - call it a **companion** - owns only
trivial carriers `(1,1,0)`, so with `w_i := #{trivials on D_i}`:

```text
   W_i = w_i ,   a^{(i)} = N - w_i ,   K_i = 0 ,   iota_i = 0 ,
   meridian gamma_i of cycle type 1^{a_i} prod 1^{s_l} = 1^N  (trivial).
```

At `N = 4,5` `(RC2)` forces `b_br = 1`; at `N >= 6` a profile can have `b_br = 2`
or `3`, and the notion stays well defined per component. Companions are exactly the
components carrying no monodromy - hence invisible to the whole `pi_1` layer, and
attackable only through curve geometry.

### 3.2 The complete forced datum

Every clause below is promoted or is derived here from promoted material; the
derivations are one line each and are given.

| # | forced datum for a companion `D_i` | source |
|---|---|---|
| C1 | `D~_i ~ A^1`, one place at infinity: a polynomial curve `xi -> (a_i,b_i)`, birationally parametrised | Lemma A `[P]`; `s_l = 1` on trivials |
| C2 | `chi~_i = 1`; geometric genus `0` | C1; also the *only* output of `(M')` (SS2.3) |
| C3 | `eta_i` **immersive**: every branch smooth, every singular point multibranch | trivial carrier has `s = 1`, `corr = 0`; Gate SELF-R2's mechanism `[P]` |
| C4 | `D_i` is **singular**: `eta_i` not injective, so at least one multibranch point | Gate EMB `[P]` + finiteness of `eta_i` |
| C5 | `2 w_i <= N`, hence `1 <= w_i <= floor(N/2)` and `ceil(N/2) <= a^{(i)} <= N-1` | Gate SELF-R2 `[P]`, applicable since `D_i` owns a trivial |
| C6 | `deg a_i = m_i d`, `deg b_i = m_i e`, `gcd(d,e)=1`, `(d,e)` the **same** for every component of `A_F`, `deg D_i = m_i max(d,e)`, `max(d,e) >= 2` | Chau Thm 1 `[L]`; CAGE clause 1 `[P]` |
| C7 | leading coefficients satisfy `A_i^e / B_i^d = A^e / B^d`, one scalar shared by every component and equal to the invariant of `(P_+, Q_+)` | Chau Thm 1 `[L]`, sharpened in SS3.3 |
| C8 | all components meet `L_inf` at the same point, one place each, tangent to `L_inf` | Chau Cor 2 `[L]` |
| C9 | branch caps: `r_{i,p} w_i + sum_{j != i} r_{j,p} W_j + K_p <= N` at every `p` | `(LOC)` `[P]` |
| C10 | `sum_i d_i iota_i = N - 2 + 2g + Sigma_inf`, to which `D_i` contributes **nothing** (`iota_i = 0`) | Gate TG `[P]` |
| C11 | `(M')`: nothing beyond C2 | THEOREM COLLAPSE-N `[D]` |

C3: the trivial carrier has `s_l = 1`, so `h_l` is an isomorphism and `(G4)` gives
`d phi_l != 0`; `d phi_l = d eta_i o d h_l` forces `d eta_i != 0`. C4: `eta_i` is
finite, so an injective immersion is a closed embedding of `A^1`, which Gate EMB
forbids. C5 is the only *numerical* pressure on a companion, and it pinches the
weight, not the geometry.

Per profile this is explicit. From the CAGE ledger: `N = 4`, one companion, `w = 1`,
`a = 3`. `N = 5`: `S1` and `P3a` have companions of weight `1` (`a = 4`), `P3b` one
of weight `2`. `N = 6`: `w in {1,2,3}`, with CAGE's `[2]` row `W = (2,3)` sitting at
the C5 boundary `2w = N`. `N = 7`: `w <= 3`. `N = 8`: `w <= 4`, attained e.g. on the
`[2]` row `W = (2,4,1)`, again at the C5 boundary. **In every case the companion datum is
(C1)-(C10) with the single integer `w` moving.**

### 3.3 Chau re-read: the pin is sharper, and two printed formulas are inverted

`[L]` Chau, *Non-proper value set and the Jacobian condition*, arXiv:math/0305088.
Theorem 1: with `J(P,Q) = const != 0`, `deg P = Kd`, `deg Q = Ke`, `gcd(d,e) = 1`,
`P` and `Q` monic in `y` with leading coefficients `A`, `B`, every irreducible
component of `A_f` is parametrised by
`xi -> (A xi^{md} + l.o.t., B xi^{me} + l.o.t.)`, `m in N`.

Two things follow that CAGE clause 1 does not say.

*(i) The pin is sharper.* `(A,B)` is the **same** for every component; only `m`
varies. The one remaining freedom `xi -> lambda xi` sends
`(A,B) -> (A lambda^{md}, B lambda^{me})` and fixes `A^e/B^d`. So the
component-independent scalar is `A^e/B^d`, and it equals the invariant of the
leading forms, `P_+^e = (A^e/B^d) Q_+^d`, the relation the Jacobian condition
forces. This is strictly stronger than "the ratio `deg p_i/deg q_i` is the same".

*(ii) `c` is common only up to an `e`-th root.* From `u ~ A xi^{md}`,
`v ~ B xi^{me}`, Cor 2's `c` is `A B^{-d/e}`, i.e. `c^e = A^e/B^d`: it is pinned by
the shared invariant only up to a primitive `e`-th root of unity, and components
may sit on different roots. CAGE clause 1's "**a common** Newton-Puiseux type
`u = c v^{d/e}`" over-reads the source if `c` is taken literally common; the safe
form is *common exponent `d/e`, common `c^e`*. `[A]` **AUDIT-CC-2** (flag/place:
asymptotic coefficient vs. its `e`-th power).

*(iii) Two printed formulas are inverted.* Cor 1 prints
`R_0 = C(A^e u^e - B^d v^d)^M + sum_{0<=id+je<Mde} c_{ij}u^i v^j` and Cor 2 "`c` a
`d`-radical of `B^d/A^e`". But `A^e u^e ~ A^{2e} xi^{mde}` and
`B^d v^d ~ B^{2d} xi^{mde}` cancel only if `A^{2e} = B^{2d}`; the combination that
always cancels is `B^d u^e - A^e v^d`. Machine check `[C]`: the component
`xi -> (2 xi^3, xi^2)` (`A=2, B=1, d=3, e=2`) has equation `u^2 - 4v^3`;
`B^d u^e - A^e v^d = u^2-4v^3` divides it, `A^e u^e - B^d v^d = 4u^2-v^3` does not;
and `c = 2` gives `c^e = 4 = A^e/B^d`, not `c^d = 8` versus `B^d/A^e = 1/4`. Read
Cor 1 as `(B^d u^e - A^e v^d)^M` and Cor 2 as `c^e = A^e/B^d`. Both printed forms
are correct at `A = B = 1`, so nothing banked is disturbed. `[A]` **AUDIT-CC-3.**

*Positive control on the campaign's own curve.* `[C]` The `(9,6,2)` curve
`t -> (t^9+12t^5+24t, t^6+8t^2)` has implicit equation `f_1(u,v)` of total degree
`9`, `deg_u = 6`, `deg_v = 9`, weighted-`(3,2)` degree `18`, and weighted-leading
form **exactly** `(u^2 - v^3)^3`. That is Chau Cor 1's shape with `(d,e) = (3,2)`,
`m_1 = 3`, `A = B = 1`, `M = 3`. In closed form,

```text
   f_1 = Z^3 - 192 v Z^2 + 12288 v^2 Z + 32768 Z - 262144 v^3 - 2359296 v,
   Z := u^2 - v^3 ,
```

verified by expansion. The weighted levels present are `18, 14, 10, 6, 2` only.

### 3.4 Lemma CONTACT: components of `A_F` are forced into high mutual contact

> **Lemma CONTACT `[D]`.** Let `D_1, D_2` be distinct components with Chau data
> `(d,e)` and multiplicities `m_1, m_2`. Then
> ```text
>   sum_{p in C^2} (D_1.D_2)_p  <=  m_1 m_2 d e - min(m_1, m_2) ,
>   (D_1.D_2)_{P_inf}           >=  m_1 m_2 max(d,e) |d - e| + min(m_1, m_2) .
> ```

*Proof.* `sum_{p affine} (D_1.D_2)_p = deg_xi f_1(a_2(xi), b_2(xi))`, since the
`D_2`-parametrisation is proper and birational. Grade `C[u,v]` by
`wt(u) = d, wt(v) = e`; `f_1` has weighted degree `m_1 de` with weighted-leading
form `(B^d u^e - A^e v^d)^{m_1}` (SS3.3). Substituting raises weighted degree `w` to
`xi`-degree at most `m_2 w`. The top level contributes at most
`m_1 (m_2 de - 1)` because `B^d a_2^e - A^e b_2^d` loses its leading coefficient
exactly by C7; every lower level contributes at most `m_2(m_1 de - 1)`. Take the
max of the two, i.e. subtract `min(m_1,m_2)`. Bezout in `P^2` with
`deg D_i = m_i max(d,e)` and `max(d,e)^2 - de = max(d,e)|d-e|` gives the second. []

*Controls `[C]`.* `(9,6,2)` against `m_2 = 1` companions: bound `17`, actual `12`;
contact bound `>= 10`, actual `15`; Bezout `27 = 12 + 15`. Against two independent
`m_2 = 2` companions: bound `34`, actual `33` both times; contact bound `>= 20`,
actual `21` both times. Near-sharp, never violated.

### 3.5 Three load-bearing negatives

**(N1) `(LOC-2)` is vacuous in RED-N.** It forbids `D_i n D_j != {}` when
`W_i + W_j > N`; but `W_i + W_j <= sum_k W_k = N - 1 - K_tot < N` always. No pair
of components is ever forced apart, so Lemma CONTACT can never be played against a
forced disjointness. `[D]`

**(N2) The companion's degree is invisible to every promoted degree gate.** In
Gate TG / CAGE clause 7 the companion enters as `d_i iota_i` with `iota_i = 0`, and
DEG-PER-R2 needs the component's generic-line meridians to generate transitively -
they are trivial. So no promoted result bounds `deg D_i` above or below beyond
`deg >= 2` (Lemma NL) refined by C6 to `deg in max(d,e) Z_{>0}`. `[D]`

**(N3) The companion carries no monodromy.** Its meridian is trivial, so `rho`
factors through `pi_1(C^2 - D_br)`: `N-A-RES`, PIN-R2, the transposition-graph
machinery and the ZvK/braid layer are blind to companions by construction. `[D]`
(N5's (M-1), read as a limitation rather than a simplification.)

## 4. Task (2): existence — THEOREM COMPANION-EXISTS

The charge asks whether a rational companion with the forced data exists for any
`N`, with instructions to exhibit a family if it does and to state `N_0` exactly if
the data is contradictory beyond some degree. It exists at every `N`, and `N_0`
does not exist.

### 4.1 Gate EMB is automatic when `d, e >= 2`

> **Lemma EMB-AUTO `[D]`.** If `d, e >= 2` then no birational immersive
> parametrisation of bidegree `(m d, m e)` is injective; hence C4 is automatic and
> Gate EMB imposes no condition on companions.

*Proof.* Abhyankar-Moh: a smoothly embedded `A^1 subset C^2` given by
`xi -> (a,b)` has `deg a | deg b` or `deg b | deg a`. Here `md | me` iff `d | e`
iff `d = 1`, and `me | md` iff `e = 1`. []

So the only `(d,e)` where Gate EMB is a real condition are `(d,1)` and `(1,e)`; the
witness below satisfies it there too, by exhibiting a member with a double point.

### 4.2 The uniform family

> **THEOREM COMPANION-EXISTS `[D]`+`[C]`.** Fix coprime `(d,e)` with
> `max(d,e) >= 2`, an integer `m >= 1`, and any `lambda in C^*`. Choose `A, B` with
> `A^e/B^d = lambda`. Then
> ```text
>        C_{d,e,m} :  xi  |-->  ( A (xi^{md} + xi) ,  B xi^{me} )
> ```
> is a plane polynomial curve satisfying **C1-C8** and, generically in its
> coefficients, **C9**: `A^1` normalisation, one place at infinity, bidegree
> `(md, me)`, the prescribed Chau invariant, immersive parametrisation, and at
> least one multibranch point.

*Proof.* *Birational.* If `xi_1 != xi_2` have the same image then
`xi_2 = zeta xi_1` with `zeta^{me} = 1`, and `xi_1^{md} + xi_1 = zeta^{md}
xi_1^{md} + zeta xi_1`; for `xi_1` outside a finite set the two monomials are
independent, forcing `zeta = 1`. So `eta` is generically injective, hence
birational, and `deg C = max(md, me)`. *Immersive.* `a' = A(md xi^{md-1} + 1)`,
`b' = B me xi^{me-1}`; the only zero of `b'` is `xi = 0`, where `a' = A != 0`.
*One place at infinity, C6-C8.* Immediate from the bidegree and the leading
coefficients `(A,B)`, which give exactly `A^e/B^d = lambda`. *Singular.* By
EMB-AUTO when `d,e >= 2`; when `e = 1` (resp. `d = 1`) replace `b` by
`B(xi^{me} + xi^2)` and check the two-parameter fibre directly. []

*Machine control `[C]`.* For `(d,e) in {(3,2),(2,3),(5,3),(3,5),(5,2),(4,3),(7,4)}`
and `m in {1,2,3}` - 21 shapes - the family was checked exactly: `gcd(a',b') = 1`
in all 21 (immersive), and `Res_eta` of the two divided differences has positive
degree in all 21 (non-injective, so singular). Bidegrees range over `(3,2)` to
`(21,12)`.

### 4.3 Consequence, and the exact answer to the charge

> **Corollary `[D]`.** For every `N >= 4`, every profile in the CAGE-N-R2 ledger,
> and every companion slot of weight `w` in that profile, the forced companion
> datum (C1)-(C8) is realized by an explicit curve. C5 constrains only `w`, which
> is a property of the profile and not of the curve; C9 is a finite set of open
> conditions relative to the rest of `A_F`; C10 and C11 are vacuous on companions
> (SS3.5 (N2), THEOREM COLLAPSE-N). **There is no `N_0 >= 4` beyond which the
> companion datum is contradictory.**

Three attacks the charge names were run; none bites, recorded so they are not
re-run. *Genus-degree / Bezout*: genus is `0` by C2, degree is free by (N2), and
Bezout against `D_1` is absorbed by the contact at infinity (Lemma CONTACT), which
by (N1) is never forced to be everything. *Log-Chern / BMY*: these bound
`kappa`-positive configurations; the companion is a rational cuspless polynomial
curve, the class for which the promoted `bar-kappa(U) = min(#S-2,1)` gives no
obstruction at `#S <= 2`. Nothing is asserted. *Zaidenberg-Lin*: statements about
curves with one place at infinity and `A^1` normalisation - the companion is in the
hypothesis class, not the excluded one; their bite on which `(md,me)` occur is
Abhyankar-Moh's divisibility, already used in EMB-AUTO.

**Survivor, exhibited.** The nodal cubic `C_{3,2,1}` - concretely
`xi -> (xi^3 + xi, xi^2)` up to the coefficient normalisation - realizes the
companion datum at the `N = 4` profile. SS5 upgrades this to a member matched to the
realized `(9,6,2)` curve.

## 5. Task (3): the (9,6,2) substrate, complete forced datum, and a witness

### 5.1 `D_1` re-verified here

`[C]` Independently of REP96 SS1, on the curve `D_1 = image(t -> (p,q))`,
`p = t^9 + 12t^5 + 24t`, `q = t^6 + 8t^2`:

```text
  p^2 - q^3 - 64q - 64t^2 = 0                                  (exact, expands to 0)
  f_1(u,v) = Res_t(p-u, q-v) :  total degree 9, deg_u 6, deg_v 9
  weighted-(3,2) degree 18, weighted-leading form (u^2 - v^3)^3
  f_1(0,v) = -v (v^4 + 96 v^2 + 1536)^2
  p_a = 28 = delta_aff 4 + delta_inf 24
```

The last display settles the node census alone: `u = 0` meets `D_1` in the smooth
point `v = 0` and in the four roots of `v^4+96v^2+1536`, each to multiplicity
**2**, total `1 + 8 = 9 = deg D_1`. So the four affine nodes are exactly
`(0,v)` with `v^4+96v^2+1536 = 0`, all on `u = 0`, and `delta_aff = 4` is
exhausted - REP96 SS1 by a third route (there: the symmetry `p(-t) = -p(t)` plus
numerics). Chau data of `D_1`: `(d,e) = (3,2)`, `m_1 = 3`, `A = B = 1`, invariant
`1`.

At the `N = 4` profile (core `(2,1,0)`, `W_br = 2`, one companion of weight `1`):
`a^{(1)} = 2`, which **saturates** the branched ceiling `a <= N - 2 = 2`;
`gamma_1` has cycle type `1^2 2^1`, a transposition; Gate TG reads
`2g + Sigma_inf = deg D_1 . iota_1 - 2 = 7`, so
`(g, Sigma_inf) in {(3,1), (2,3)}` - the only two admissible pairs, since
`1 <= Sigma_inf <= N = 4` and parity forces `Sigma_inf` odd.

### 5.2 The complete forced datum of `D_2`

Instantiating SS3.2 at `N = 4`, `W_1 = 2`, `w_2 = 1`, `K_tot = 0`:

```text
 (D1) polynomial curve, D~_2 ~ A^1, one place at infinity          (C1,C2)
 (D2) bidegree (3 m, 2 m), m >= 1; deg D_2 = 3m                    (C6)
 (D3) leading coefficients with A_2^2 / B_2^3 = 1                  (C7)
 (D4) eta_2 immersive: no cusps; all singularities multibranch,
      all branches smooth                                          (C3)
 (D5) at least one multibranch point                               (C4, automatic by EMB-AUTO)
 (D6) a^{(2)} = 3 ; meridian trivial ; iota_2 = 0                  (SS3.1)
 (D7) at each p in D_1 n D_2 :  a_p + 2 r_{1,p} + r_{2,p} = 4,
      hence  r_{1,p} = 1  and  r_{2,p} <= 2                        (LOC)
 (D8) therefore D_2 AVOIDS all four nodes of D_1                   (LOC at a node: r_2 = 0)
 (D9) at a point of D_2 alone with r branches: a_p = 4 - r >= 0    (LOC)
 (D10) Bezout: 9 . 3m = sum_p (D_1.D_2)_p + (D_1.D_2)_{P_inf},
      with sum_affine <= 18m - min(3,m)                            (Lemma CONTACT)
 (D11) (M') : nothing beyond (D1)                                  (COLLAPSE-N)
```

Two corrections to REP96 SS7 R4's reading of the same datum. `[A]` **AUDIT-CC-4.**
(i) It says `D_2` meets `D_1` **transversally**, with `a_p = 1` there. `(LOC)`
counts *branches*, not intersection multiplicities: it forces `r_{1,p} = 1` and
`r_{2,p} <= 2` and nothing about tangency. `a_p = 1` holds when `r_{2,p} = 1`; at a
tangential crossing of two smooth branches `a_p` is still `1`, and if `p` is the
`D_2`-node lying on `D_1` then `a_p = 0`. Transversality is an available *choice*,
not a forced datum. (ii) The crossing count `j` is not determined - it is
`sum_p (D_1.D_2)_p` minus tangency and node corrections, and (D10) bounds it only
above.

**Is there a finite-dimensional family to search?** Yes, and it is small. Fixing
`A_2 = B_2 = 1` (which uses up the `xi`-scaling exactly, the invariant `A^2 = B^3`
cutting out precisely the scaling orbit) and normalising the `xi`-translation, the
companions of multiplicity `m` form an affine space of dimension

```text
        3m + 2m - 1  =  5m - 1 ,      so dimension 4 at m = 1.
```

(D4), (D8) and the `r_{2,p} <= 2` half of (D7) are Zariski-open on it.

### 5.3 The witness

`[C]` Take the smallest admissible multiplicity, `m = 1`, and

```text
        D_2 :   xi  |-->  ( xi^3 + xi + 1 ,  xi^2 + 3 ) .
```

Machine-verified, exactly, over `Q`:

| item | value | status |
|---|---|---|
| bidegree | `(3,2)`, `deg D_2 = 3`, `m_2 = 1` | (D2) ok |
| leading coefficients | `(A_2,B_2) = (1,1)`, `A_2^2/B_2^3 = 1` | (D3) ok, matches `D_1` |
| immersive | `gcd(a', b') = gcd(3xi^2+1, 2xi) = 1` | (D4) ok |
| self-crossing ideal | `(eta + xi, eta^2 + 1)`: one pair `{i,-i}` | one node, at `(1,2)` |
| singularity type | one ordinary node of two smooth branches, `r = 2` | (D5) ok |
| `f_1(a(xi),b(xi))` | degree `12`, squarefree, **irreducible over `Q`**, `lc = -343` | see below |
| `gcd(f_1(a,b), a(xi))` | `1` | no crossing has `u = 0` |
| `gcd(f_1(a,b), b^4+96b^2+1536)` | `1` | (D8) ok - all four `D_1`-nodes avoided |
| does `xi^2+1` divide `f_1(a,b)` | no | the `D_2`-node is **not** on `D_1` |
| Bezout | `9 . 3 = 27 = 12 + 15` | `(D_1.D_2)_{P_inf} = 15` |

Since `f_1(a(xi),b(xi))` is squarefree of degree `12` and `eta_2` is injective off
`{i,-i}` which are not among its roots, `D_1 n D_2` consists of **12 distinct
points, each of intersection multiplicity 1**: twelve transverse crossings, at each
of which `r_{1,p} = r_{2,p} = 1`. (D7) and (D9) are then satisfied with room to
spare, and Lemma CONTACT's affine bound `17` and contact bound `>= 10` are both
respected (`12` and `15`).

So `D_1 u D_2` satisfies **every** promoted constraint of the `N = 4` reducible
cage: clause 1 (both polynomial curves, one common point at infinity, common
`(d,e) = (3,2)` and invariant `1`, neither a line nor a smoothly embedded `A^1`);
clause 2 (`2 + 1 + 0 = 3 = N-1`); clause 3 (`(LOC)` at all 17 points, census
below); clause 4 (SELF-R2 `2W_2 = 2 <= 4`, LZ-KILL `2W_1 = 4 <= 4` at equality);
clause 5 (vacuous, no ramified carrier); clause 6 (`gamma_1` a transposition,
`gamma_2` trivial, `G = S_4` by PIN-R2); clause 7 (`d_1 iota_1 = 9 >= 3`, Gate TG
as in SS5.1); clause 8 (nothing asserted about raw degree).

### 5.4 The `a_p` census, and `(M')` evaluated on the witness

From `(LOC)`, `Sigma` has 17 points and

```text
   4 nodes of D_1     : r = (2,0)  ->  a_p = 4 - 4 = 0
   1 node of D_2      : r = (0,2)  ->  a_p = 4 - 2 = 2
  12 crossings        : r = (1,1)  ->  a_p = 4 - 2 - 1 = 1
```

so `sum_p a_p = 0 + 2 + 12 = 14`, and every `a_p` obeys `0 <= a_p <= a^{(i)}`
(`2` at the `D_2`-node against `a^{(2)} = 3`; `1` at a crossing against
`min(2,3) = 2`). With `chi_c(D_1 \ Sigma) = 1 - 16 - 4 = -19` and
`chi_c(D_2 \ Sigma) = 1 - 13 - 1 = -13`:

```text
  LHS = 2(-19) + 3(-13) + 14 = -63 ,
  chi_c(A_F) = -19 - 13 + 17 = -15 ,  chi_c(V) = 16 ,  RHS = 1 - 4(16) = -63 .
```

`(M')` is satisfied **exactly**. This is SS2.5's positive control and the concrete
face of THEOREM COLLAPSE-N: an entirely hand-chosen pair of curves passes the
identity that was charged as the companion's obstruction.

### 5.5 What the witness does and does not establish

**Does.** The forced companion datum at the `(9,6,2)` substrate is *consistent*:
(D1)-(D11) admit a solution, exhibited, over `Q`, in the `4`-dimensional `m = 1`
family. Companion existence at `N = 4` is therefore **DECIDED POSITIVE**, and the
charge's "does the data exist for ANY `N`" is answered by SS4.3 plus this.

**Does not.** The pair is *not* claimed to be `A_F` of any Keller map, and there is
no evidence that it is. Three things stand between it and a counterexample, none
reachable by the companion question:

1. `OPEN[REP-96-BM-FACTORISATION]` - the nine local braid conditions on `D_1`, of
   which `rho_inf`-fixedness is only the product. Unchanged by this lane.
2. `OPEN[REP-96-SOURCE-IS-C2]` - Riemann existence gives a normal surface `Y`, not
   `Y ~ C^2`. Unchanged, and still the largest gap.
3. A new one, typed here: even given a representation and a source, `A_F` must be
   the *actual* non-properness set of the resulting map, which pins `R_0(u,v)` up
   to a constant, hence pins `M = M_1 + M_2` and, through Chau's resultant,
   `M <= K = deg P / d`. `OPEN[COMPANION-R0-REALISATION]`, SS7.

On item 3, one derived remark `[D]`: `Res_y(P-u,Q-v) = R_0 x^N + ... + R_N` has
`deg_u <= deg_y Q = Ke` and `deg_v <= deg_y P = Kd`, while `R_0`'s weighted-leading
form `(B^du^e - A^ev^d)^M` has `deg_u = Me`, `deg_v = Md`; hence **`M <= K`**, i.e.
`sum_i k_i m_i <= K` and `sum_i deg D_i <= max(deg P, deg Q)`. Nothing is bounded
absolutely (`deg P` is free), but this is the exact currency in which a degree-cap
attack - `OPEN[N5-DEGREE-CAP]`, restored as high-leverage by CAGE SS2.5 - must be
paid.

## 6. The machine job

The charge asks for the exact job that would decide `D_2`'s existence. **The base
question no longer needs one**: existence at `m = 1` is decided positive by the
SS5.3 witness, which doubles as the positive control for anything below. What a
machine can still decide, cheaply, is the *stratification* of the companion family
- which contact profiles against `D_1` are attainable. Two jobs, in priority order.

### JOB-A (small, decisive for a named stratum): the affinely-disjoint companion

*Question.* Is there a multiplicity-`m` companion of the `(9,6,2)` curve that meets
`D_1` **only** at `P_inf`, i.e. with maximal contact `(D_1.D_2)_{P_inf} = 27m`?

*Ring.* `Q[a_{3m-1},...,a_0, b_{2m-2},...,b_0]`, no auxiliary variables: leading
coefficients fixed to `1` by C7 + `xi`-scaling, `b_{2m-1} := 0` by `xi`-translation.
Dimension `5m - 1`; at `m = 1`, `Q[a_2,a_1,a_0,b_0]`.

*Generators.* Form `S(xi) := f_1(a(xi), b(xi)) in Q[coeffs][xi]` with `f_1` the
closed form of SS3.3. Let `I_A := ( [xi^1]S, [xi^2]S, ..., [xi^{6m+... }]S )` - all
coefficients of positive powers of `xi`. Disjointness is `S = const != 0`, so the
decision is `V(I_A) != {}` together with `[xi^0]S != 0` on it. At `m = 1`, `S` has
degree `12`, so `I_A` has **12 generators in 4 variables**.

*Decision.* `msolve -g 2` (or `qqideal` for the rational-solution question)
on `I_A`; `V(I_A) = {}` is the expected answer and would prove that **every**
`m = 1` companion of the `(9,6,2)` curve meets it affinely - a clean, sourced
structural fact about the substrate, and the first nontrivial constraint tying the
two components together.

*Controls, mandatory.* (+) Replace `f_1` by the companion's own `f_2`: then
`S = 0`, `I_A = (0)`, `V = A^4` - catches a substitution/ring error. (-) Drop C7
(set `A_2 = 2`): `S` jumps to degree `18`, `I_A` gains 6 generators, and any
emptiness verdict is then for a different reason. (0) Feed the SS5.3 witness
`(a_2,a_1,a_0,b_0) = (0,1,1,3)`: `S` must have degree `12`, so the witness **fails**
`I_A` - confirming the job asks the intended question.

### JOB-B (the one with decision power over the row): the braid factorisation

`OPEN[REP-96-BM-FACTORISATION]` is unchanged by this lane and is still the cheapest
decisive step on the row. Not a Groebner job: eight tangency transports for a
degree-`9` curve whose singular-fibre census is already exact (REP96 SS7 R1: eight
simple tangency fibres, one fibre `x = 0` carrying all four nodes, ledger
`8.1 + 4.2 = 16 = 2 delta_aff + d - 1`). SS5.1 supplies the set-up data: the nodes
are the roots of `v^4+96v^2+1536` on `u = 0`, the tangency parameters the roots of
`3t^8+20t^4+8` with pairwise distinct `p`-values. **Prefer JOB-B to JOB-A** if only
one can be run.

*What must not be run.* Any job that tries to decide the companion by imposing
`(M')`. By THEOREM COLLAPSE-N the resulting ideal is `(0)` up to the budget, and
the job would return a vacuous NONEMPTY. This is the concrete cost of the negative
in SS2 and the reason it was worth proving.

## 7. Typed verdict block, OPENs, deviations

```text
LANE                 COMPANION-CURVE-ALLN   (Path-2 flagship, reducible branch)
VERDICT              CLOSED-NEGATIVE as an obstruction lane.
                     The forced companion is realizable at every degree; the
                     identity charged to constrain it is information-free.

THEOREM COLLAPSE-N   PROVED-HERE, UNREVIEWED, machine-controlled.
                     LHS(M'-bf) - RHS(M'-bf) = (N-1) - K_tot - sum_i W_i chi~_i.
                     Given (AGG): (M'-bf) <=> chi~_i = 1 for all i <=> Lemma A.
                     Corollary: (M') is not an independent gate in RED-N.

THEOREM COMPANION-   PROVED-HERE, UNREVIEWED, machine-controlled on 21 shapes.
  EXISTS             C_{d,e,m}: xi -> (A(xi^{md}+xi), B xi^{me}) realizes
                     C1-C8 for every coprime (d,e), max(d,e)>=2, every m,
                     every value of A^e/B^d.   N_0 DOES NOT EXIST.

Lemma CONTACT        PROVED-HERE, UNREVIEWED, near-sharp on 3 machine controls.
Lemma EMB-AUTO       PROVED-HERE (Abhyankar-Moh).
Chau AUDIT-CC-2/3    Cor 1 leading form is (B^d u^e - A^e v^d)^M, not
                     (A^e u^e - B^d v^d)^M; Cor 2's c satisfies c^e = A^e/B^d.
                     Machine-verified. Harmless in the monic normalisation.

(9,6,2) SUBSTRATE    Companion existence DECIDED POSITIVE at N = 4, m = 1, with
                     an explicit witness over Q. The row SURVIVES this attack.
                     Status unchanged at OPEN[REP-96-BM-FACTORISATION] and
                     OPEN[REP-96-SOURCE-IS-C2].
```

**OPENs closed.** `OPEN[REP-96-MPRIME-COMPANION]` - **closed NEGATIVE**: the
identity never binds, at any `N`, on any profile, for any pinning of `D_2`.

**OPENs opened.** `OPEN[COMPANION-R0-REALISATION]`: `A_F` must be the zero set of
the leading resultant coefficient `R_0`, which pins `M = sum_i k_i m_i` and forces
`M <= K = deg P/d`, i.e. `sum_i deg D_i <= max(deg P, deg Q)`. This is the exact
currency of `OPEN[N5-DEGREE-CAP]` / `OPEN[RED-N-DMIN-BOUND]`, restored as
high-leverage by CAGE SS2.5, and it is the only place found in this lane where the
companion's degree can be reached at all.
`OPEN[COMPANION-AFFINE-DISJOINT]`: JOB-A, SS6.

**OPENs untouched.** `OPEN[REP-96-BM-FACTORISATION]`, `OPEN[REP-96-SOURCE-IS-C2]`,
`OPEN[CUSP-2-AT-CONTRACTED-ATTACHMENT]`, `OPEN[PI1-S_N-CAGE(...)]`,
`OPEN[RED-N-ORDINARY-GENERATION]`, `OPEN[RED-N-BLOCK-SYSTEM]`,
`OPEN[ZARISKI-GENERIC-LINE-CUSTODY]`, `OPEN[THREE-TRIVIALS-ONE-OWNER]`.

**Deviations from the charge.** (a) The charge frames tasks (1)-(2) as steps toward
an all-degree contradiction. Task (1) refutes the premise that `(M')` can supply
one, so task (2) was run against the *cage's* forced datum rather than against
`(M')`'s output, and its verdict is the exhibition the charge authorised as a
success rather than a failure. (b) Task (3) asks for a Groebner job deciding `D_2`'s
existence; existence is decided by hand plus an exact witness, so SS6 specifies the
job for the residual stratum question and names the higher-leverage successor
instead of manufacturing a decision job for a settled question. (c) One non-charged
campaign file and one primary source were read; both are disclosed in SS0 with
hashes. (d) No `charge_basis` line: no exit-price assertion is made anywhere here.
(e) **Size.** The body overruns the charged 25-35 KB target by roughly 30%. Three
compression passes were run; what remains is the two theorems with their proofs,
the (C1)-(C11) datum, the `(9,6,2)` instantiation with its verified witness, the
control ledger the hostile standard requires, and the job spec. Nothing was dropped
to hit a byte count, and the overrun is reported rather than paid for with
verified mathematics or with controls.

## 8. FALLACY-v2 self-check

*Flag/place/series.* Three separations are load-bearing. (i) The two `b` symbols
the charge warns about are written `b_dic` and `b_br` throughout, plus `b_box` for
the third one hiding inside Prop 2.4's proof; SS0 fixes all three. (ii) "Component
of `A_F`" vs "component in the branch locus" (AUDIT-CC-1): Prop 2.4's ceiling is
licensed only on the second, and applying it to a companion would falsely kill the
promoted `N = 4` profile. (iii) Asymptotic coefficient `c` vs its `e`-th power
(AUDIT-CC-2): only `c^e = A^e/B^d` is component-independent.

*Carrier/attainment.* SS5.3 is typed as a curve pair satisfying a necessary cage,
never as a witness for a Keller map; SS5.5 states the three remaining gaps.
`THEOREM COMPANION-EXISTS` is an attainment claim **about curves with prescribed
data** and is proved by construction plus a 21-shape machine check, not inferred
from non-emptiness of a cage.

*Floor/attainment.* Lemma CONTACT is one-sided and used only so; its controls are
reported with actual values (`12` vs bound `17`; `33` vs `34`, twice) so it is not
read as an equality. `M <= K` in SS5.5 is a ceiling and is not converted into a cap.

*Raw remainder degree / variable-ring map.* Every degree statement about `A_F` is
weighted (`wt(u)=d, wt(v)=e`, declared at each use) or tied to a named
parametrisation with its leading coefficients. The one raw-degree relation,
`sum_i deg D_i <= max(deg P, deg Q)`, is flagged as gauge-dependent on the `x,y`
side and is not a `d_min` bound. The substitution `u -> a(xi), v -> b(xi)` in SS3.4
and SS6 declares source ring, target ring, images and the grading it respects.

*Controls.* SS2.5: one positive, three negative (`chi~_2 = 0,-1,-3`, each matching
the predicted defect), one 33116-case randomised; the failed first harness is
reported, not discarded. SS4.2: 21 shapes. SS6 specifies `(+)`, `(-)`, `(0)`.

*Pole/interior, `sat()`, prime-label, merge-free, target/arrival.* Not in play.

*Gaps.* Nothing filled by cap or analogy. Where source and campaign paraphrase
disagree (Chau Cor 1/2) the disagreement is reported with a machine check on an
explicit example rather than averaged away; where a promoted clause over-reads its
source (CAGE clause 1's "common `c`") the safe weakening is stated and the strong
form is not used.

## 9. Custody and sources

```text
frozen inputs (verified, SS0)
  a47945ab...db2401  rep-96-inner-opus5-20260901.md              [REP96]
  bdd857c9...f3c369339 reducible-all-n-r2-opus5-20260901.md      [CAGE]
  48d417d6...a00713b  b0-reducible-n5-opus5-20260831.md          [N5]
consulted, disclosed
  xmodel/round1033-sheet-gate-opus5-20260831.md                  [S]  (source of (M'))
  8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f
      refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf    [L]  (Thm 1, Cor 1, Cor 2)
primary literature cited, not re-read here
  Abhyankar-Moh (1975) / Suzuki (1974), embedding line theorem   (via EMB-AUTO)
computation
  sympy 1.14.0 over Q; scripts /tmp/comp/{d1,d1b,d2,d3,witness,mprime3,family,contact,final}.py
  no AWS, no msolve/qqideal run, no jc2-lean, no canonical ledger
```
