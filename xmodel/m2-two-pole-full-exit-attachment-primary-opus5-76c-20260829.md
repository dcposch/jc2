# Two-pole full-exit attachment: primary attack

**Date:** 2026-08-29
**Author:** Opus 5, independent co-researcher (primary lane, not a review)
**Basis:** `76c746f698103d20019bfeb72654a361ccc5371d`
**Target blocker:** the ambient orbit-tree attachment lemma named `BLOCKER` by
`ac49c025…` and named as the decisive gate by `3e3cea4a…` §7.3.

## 0. Verdict

```text
PROVED_FULL_TWO_POLE_ATTACHMENT
```

Every clause of the mandated objective is proved, on one fixed fibre `f=a`,
from printed Sigray Definitions 3.2–3.4, Statements 3.1–3.3, 3.9–3.10, 3.13,
3.16–3.18, Notations 3.1–3.8, Propositions 3.1–3.2 and 7.2–7.3, together with
the two filed corrections (Statement 3.13 `d_(f-a)`, Statement 3.18
`F*(epsilon c)`) and the reviewed actual-weight Corollary 7.1.

Summary of the four decisive findings.

1. **There is no second quotient.** The "cyclic/orbit quotient" whose
   single-valued parent structure the MFE hostile review could not license
   does not exist as a quotient. Definition 3.3 is the *only* identification
   in the source, and the cyclic group acts on the *root set of `p_F`* — a
   subset of `C`, not of the tree. Corrected Statement 3.18 is a **section**
   (one realized child per nonzero orbit), not a quotient map. §B.2, §B.3.
2. **The attachment proof never uses selectedness.** The frozen selected-orbit
   lemma (`9f4526f2…` Lemma 3.1, repaired by `f55a00f5…` §3) proves
   `A_P=[0,u]` for the ray carrying the chosen Statement-7.3 witness. Its
   proof consumes only two facts about that ray — `I_P(u)=F` and "the
   direction is not a pole-chain arrival" — both of which hold for **every**
   ray of the cluster `P(F,c)`. The strong/weak asymmetry recorded in
   `3e3cea4a…` §7.3 item 1 is therefore a **statement-perimeter asymmetry, not
   a mathematical one**. §C.2, §6.
3. **The two-pole union needs no new argument.** `U^full` is a union of
   rootward-closed segments, hence rootward closed; the truncation
   `min(v_j,O(P,P_j))` prescribed by `f55a00f5…` §3 already handles both the
   several-pole-rays-through-`F` case and the pole-endpoint case. The
   singleton-pole §4.6 first-separation partition generalizes verbatim, with
   the shared suffix appearing once because `U` is a **set**. §A.4, §C.2.
4. **The abstract countermodel violates Definition 3.3(ii).** It requires
   `I_(P_1)(w)=I_(P_2)(w)` at a height `w > O(P_1,P_2)`. `O` is a single
   height-independent rational; the predicate `u <= O(P,Q)` is downward
   closed in `u` and cannot switch back on. §B.4.

The consumer type this licenses is **`FULL_ACTUAL_FIRST_SEPARATION`** at
`m>=2`, which is strictly stronger than `REPRESENTATIVE` and is exactly the
type `ladder/BOOK-OFFAXIS.md:500` demands of a full-exit P0/P2 consumer.
Two `charge_basis=` lines are emitted in §9 for LL-1's four `delta=2/3` cells.
**No attainment is claimed anywhere**; `L_safe` is a floor and is used only as
a floor.

What this does **not** do is listed in §8. In particular it does not repair
Notation 3.5 / H5a, does not re-prove the `L_safe` floor or `(C7.1*)`, does not
promote the LL-1 book, and does not exclude `td=6`.

## 1. Custody

### 1.1 Commit and task

`git rev-parse HEAD` returned `76c746f698103d20019bfeb72654a361ccc5371d` at
the start of work and immediately before this verdict. Working tree changes at
both checkpoints were confined to the untracked `xmodel/*-76c-20260829.*` lane
artefacts and the pre-existing `jc2-lean` submodule pointer, which was never
entered, read, searched, built, modified, status-checked or controlled.

### 1.2 Frozen 18-file perimeter, before and after

`shasum -a 256` run against the declared list at both checkpoints.

| # | file | declared SHA-256 | before | after |
|---:|---|---|:--:|:--:|
| 1 | `refs/sigray_full.pdf` | `9bf9f032…7e1623ae` | OK | OK |
| 2 | `ladder/SIGRAY-AUDIT.md` | `ded3051d…37da6d15` | OK | OK |
| 3 | `xmodel/sigray-multipole-global-first-exit-partition-sol-ultra-20260828.md` | `86b491ad…8bbc83a8` | OK | OK |
| 4 | `xmodel/sigray-multipole-global-first-exit-partition-hostile-review-gpt56-20260828.md` | `ac49c025…07cc8004` | OK | OK |
| 5 | `xmodel/sigray-section9-source-audit-sol-ultra-20260828.md` | `2763d970…89459933` | OK | OK |
| 6 | `xmodel/sigray-section9-source-audit-hostile-review-gpt55-20260828.md` | `0729a576…3e6b5bad` | OK | OK |
| 7 | `xmodel/m2-arity-law-place-conservation-source-audit-sol56-20260829.md` | `05f68f4b…55784d84` | OK | OK |
| 8 | `xmodel/m2-arity-law-place-conservation-source-audit-hostile-review-fable5-20260829.md` | `56e95db5…6174a34d` | OK | OK |
| 9 | `xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md` | `c253bd12…dbd95eb6` | OK | OK |
| 10 | `xmodel/sigray-section7-weighted-euler-inequality-hostile-review-terra-20260828.md` | `727f5850…c2323aa8` | OK | OK |
| 11 | `xmodel/sigray-multipole-selected-orbit-attachment-repair-gpt56-20260828.md` | `9f4526f2…79145f14` | OK | OK |
| 12 | `xmodel/sigray-multipole-selected-orbit-attachment-hostile-fable5-20260828.md` | `f55a00f5…94e216bb` | OK | OK |
| 13 | `xmodel/m2-exit-safe-floor-legacy-reprice-r1-stable-hostile-rereview-opus5-20260829b.md` | `3e3cea4a…408a166b` | OK | OK |
| 14 | `xmodel/m2-exit-safe-floor-legacy-reprice-r1-sol56-20260829.md` | `aaa7496b…942ddeb7` | OK | OK |
| 15 | `cases/landing_ledger_ll1_r3_20260829/out/ll1_book.json` | `205e7f58…cb725a1e` | OK | OK |
| 16 | `ladder/BOOK-OFFAXIS.md` | `1ae50f79…91c58840` | OK | OK |
| 17 | `ladder/SHEET6-MULTIPOLE.md` | `93adb7ac…5a964bcb` | OK | OK |
| 18 | `ladder/SHEET6-2POLE.md` | `d7d0038c…c6c8ab2f` | OK | OK |

18/18 OK before, 18/18 OK after. No `INPUT_MUTATED` condition arose.
Full 64-hex values as verified are reproduced in §10.

### 1.3 Files read outside the frozen perimeter

Declared for transparency; nothing load-bearing rests on them alone.

- `ladder/SHEET6-AF2.md` — read for the §2 R1–R4 direction rule that
  `ladder/BOOK-OFFAXIS.md:518-529` (P0) consumes. Its R4 distinctness argument
  is *reproved from source* in §C.2 below, so the citation is corroborative.
- `cases/landing_ledger_ll1_r3_20260829/out/ll1_book.json` is in the perimeter;
  `cases/m2_exit_safe_floor_legacy_reprice_r1_20260829/check.py` is **not** and
  was **not run**. The 13→7 inventory consequence is inherited from
  `3e3cea4a…` §4, not re-derived here (§8 item 7).

### 1.4 Primary-source extraction method

Statements were extracted with `pdftotext -f N -l N` (no `-layout`, per the
campaign's stacked-fraction hazard note). Every display I rely on is a
*linear* expression (contact orders, memberships, root patterns), not a
stacked fraction, so the known `-layout` inversion hazard does not apply.
Printed page = PDF page throughout, as recorded in `ladder/SIGRAY-AUDIT.md:3`.

## 2. Standing objects and the exact hypothesis list

Fix a normalized counterexample `(f,g)` of type `(alpha,beta)` (Notation 2.3,
2.4, p. 9) and one fibre `f=a`. All of §A and §B are statements about that
single fibre; no cross-fibre transport is used anywhere.

```text
Rbar_a \ R_a        the finite set of punctures ("physical places", p. 10-11)
O(P,Q)              contact (Definition 3.2, p. 10), values in Q+ u {-1}
Omega               coherent series selection (Statement 3.2, p. 11)
T_a^*               ((Rbar_a \ R_a) x [0,infinity]) / ~   (Definition 3.3, p. 11)
I_P, pi             embedding / projection (Notation 3.1, p. 11)
V_a = V_1a u V_2a u {(0,x),(0,y)}      vertices (Definition 3.4, p. 11)
F^o, e_(F,F^o), E_a                    parent, edges (Notation 3.3, p. 12)
nu_F, kappa_F                          (Notations 3.4, 3.5, p. 12)
T_a = T_a^* n pi^(-1)(Q)               (Notation 3.6, p. 12)
F', F*c                                (Notation 3.8, p. 12)
p_F := p_(f-a,F),  d_F := d_(f-a,F)    (Notation 3.13, p. 16, corrected reading)
T_a^+, T_a^0, T_a^-                    (Notation 3.14, p. 16)
T_a^nearrow, T_a^searrow              (Notation 6.1, p. 29)
T_(a,cv) = {F in T_a^0 : d_(g,F)=0}    (Notation 7.1, p. 35)
T_(a,pole) = {P_1,...,P_m}             (Notation 5.2, p. 25, repaired Prop 5.1)
```

**Hypotheses used.** Each is either printed, or a filed correction with a
review-closed status inside the frozen perimeter.

| id | content | status | citation |
|---|---|---|---|
| S1 | exactly one of forms (3)/(4) per place | printed | p. 10, St 3.1 |
| S2 | `O(P,Q) = max` over corresponding reps; `-1` cross-form | printed | p. 10, Def 3.2 |
| S3 | coherent `Omega` with `O(P,Q)=O(Omega P,Omega Q)` | printed (proof absent; audit VERIFIED_WITH_NIT) | p. 11, St 3.2; `ladder/SIGRAY-AUDIT.md:18` |
| S4 | `O(P,P) := infinity` | **unstated convention, forced** | `ladder/SIGRAY-AUDIT.md:19` |
| S5 | `~` of Definition 3.3 | printed | p. 11 |
| S6 | `V_2a` contains every contact point; `V_a` finite | printed | p. 11, Def 3.4; `ladder/SIGRAY-AUDIT.md:23` |
| S7 | `F^o` independent of `P`; edges are intervals `I_P([u*,u])` | printed | p. 12, Not 3.3 |
| S8 | `F*c` well posed; depends on `kappa` | printed + printed remark | p. 12–13, Not 3.8 |
| S9 | `mult(p_(h,F),c) = deg(p_(h,F*c))`, `d_(h,F*c)=d_(h,F)-mult/kappa` | printed | p. 15, St 3.9(i),(iii) |
| S10 | `omega, omega*` monotone decreasing; slope `-omega*` | printed | p. 16, St 3.10 |
| S11 | unique `u` with `d_(f-a,I(u))=0` | printed, **corrected to `d_(f-a)`** | p. 16, St 3.13; `ladder/SIGRAY-AUDIT.md:45` |
| S12 | `F in V_1a u V_2a` iff `p_F` has >1 root; `p_F = eta^l ptilde(eta^nu)` | printed | p. 17, St 3.16 |
| S13 | `F = G+c` exists uniquely, `kappa`-independent | printed | p. 18, Prop 3.2 |
| S14 | `deg p_F = mult(p_G,c)`; `d_F = d_G-(pi F-pi G)deg p_F` | printed | p. 18, St 3.17 |
| S15 | root↔direction: existence + **`F*(epsilon c)`** uniqueness | printed conclusion garbled; **corrected form** | p. 18, St 3.18; `ladder/SIGRAY-AUDIT.md:52` |
| S16 | `R_a^* = {P : I_P(u+1/kappa)=F*c}` is `kappa`-independent | printed | p. 36, Prop 7.3 |
| S17 | `g(P) in C` iff a cv flag exists on `I_P` | printed | p. 36, Prop 7.2 |
| S18 | `I_P(u) in T_a^nearrow` for some `u` `=>` cv flag on `I_P` | printed | p. 35, St 7.3 |
| S19 | `pi(H) > 1` for `H in T_(a,cv)` | printed with proof | p. 35, St 7.1 |
| S20 | `T_a^*` has exactly two components | printed | p. 11, St 3.3 |
| S21 | actual-weight `(C7.1*)` for every pairwise-distinct cv subset | reviewed repair, Terra gate PASS on amended hash | `c253bd12…:33`, `:266`; `727f5850…:12` |
| S22 | `kappa_H(pi(H)-1) in N*` (the "St 9.4-proof integrality line") | inherited campaign line | `ladder/SHEET6-AF2.md` §2 R4 |
| S23 | repaired Prop 6.7/6.8: `gap>0 => ` microchild in `T_a^nearrow`; `gap<0 =>` same-branch pole | reviewed repair | `ac49c025…:96-104` |
| S24 | `L_safe` piecewise floor for a full actual exit set | PROMOTED | `ladder/BOOK-OFFAXIS.md:473-491`; `05f68f4b…:429` |

**H5a note.** `Notation 3.5` is a standing `GAP` (`ladder/SIGRAY-AUDIT.md:26`):
`kappa_F` is not well-defined as printed, and the forced repair is the
jump-realization/max value. Nothing in §A or §B uses `kappa_F` at all. §C uses
it only inside the *already promoted* weight/floor layer (S22, S24). The
attachment theorem is therefore H5a-free; the numeric floor is not. This is
stated again in §8.

## 3. Part A — the physical flag object is a rooted tree

### A.1 Ultrametricity of contact

> **Lemma A1.** For all `P,Q,R in Rbar_a \ R_a`,
> `O(P,R) >= min(O(P,Q), O(Q,R))`.

*Proof (via `Omega`).* By S1 each place carries a well-defined **side**,
`y` (form (3)) or `x` (form (4)), and `O = -1` exactly when two places have
different sides (S2, and `ladder/SIGRAY-AUDIT.md:22` re-derives the same
separation).

*Case 1: all three on the same side.* Write `A=Omega(P)`, `B=Omega(Q)`,
`C=Omega(R)`, formal series `Sigma_j c_j x^(-j)` indexed by `j in Q+`
(exponents `j/kappa`, `kappa` suitable, S1 and the Prop 3.1 print-error note
at `ladder/SIGRAY-AUDIT.md:39`). Let `s := min(O(A,B), O(B,C))`. For every
`j < s` we have `a_j = b_j` and `b_j = c_j`, hence `a_j = c_j`. Therefore
`O(A,C) = min{j : a_j != c_j} >= s`. By S3, `O(P,R)=O(A,C)` and
`O(P,Q)=O(A,B)`, `O(Q,R)=O(B,C)`, which is the claim.

*Case 2: sides differ.* If `P,R` share a side and `Q` does not, then
`O(P,Q)=O(Q,R)=-1` and `O(P,R) >= 0 > -1`. If `P,R` have different sides then
`O(P,R)=-1`, and `Q` differs in side from at least one of them, so the right
side is also `-1`. Both subcases give `>=`. QED.

*Proof (without `Omega`, robustness).* This is the route the frozen Fable-5
review carried out at `f55a00f5…:96-115`; I re-derived it independently. For
a common suitable `kappa` the Puiseux representatives of a fixed place form a
single orbit under the deck substitutions `sigma_zeta : x^(1/kappa) ->
zeta x^(1/kappa)`, `zeta in mu_kappa`, and `sigma_zeta` multiplies the
coefficient at exponent `j/kappa` by `zeta^(-j)`; hence
`O(sigma_zeta A, sigma_zeta B) = O(A,B)` for raw series. Pick raw
representatives `p,q` realizing `O(P,Q)` and `q',s` realizing `O(Q,S)`, and
write `q' = sigma(q)`. Then
`O(P,S) >= O(sigma p, s) >= min(O(sigma p, sigma q), O(q',s)) =
min(O(p,q), O(q',s)) = min(O(P,Q), O(Q,S))`,
the middle step being Case 1 applied to raw series. So Lemma A1 does **not**
depend on Statement 3.2, whose proof is absent from the thesis.

> **Corollary A2.** With the forced convention `O(P,P) := infinity` (S4),
> `~` of Definition 3.3 is an equivalence relation, and `T_a^*` is a
> well-formed quotient.

Reflexivity is S4; symmetry is symmetry of `O`; transitivity: if
`u <= O(P,Q)` and `u <= O(Q,R)` then `u <= min(...) <= O(P,R)` by A1.
This closes the exact nit filed at `ladder/SIGRAY-AUDIT.md:19`
("transitivity … is nowhere established in the thesis").

### A.2 Unique rootward restriction and no remerging

> **Theorem A3 (flag equality is contact equality).** For `P != Q` and
> `t in [0,infinity]`,
> ```text
> I_P(t) = I_Q(t)   <=>   t <= O(P,Q).                        (A.1)
> ```
> Consequently:
> (a) *rootward restriction* — if `I_P(t)=I_Q(t)` and `0 <= t' <= t`, then
>     `I_P(t')=I_Q(t')`;
> (b) *no remerging* — if `I_P(t) != I_Q(t)` and `t'' >= t`, then
>     `I_P(t'') != I_Q(t'')`;
> (c) `{t : I_P(t)=I_Q(t)} = [0, O(P,Q)] n [0,infinity]`, a closed initial
>     segment, empty iff `O(P,Q) = -1`.

*Proof.* `I_P(t) = (P,t)_~` and `I_Q(t) = (Q,t)_~` by Notation 3.1. Class
equality holds iff `(P,t) ~ (Q,t)`, i.e. (Definition 3.3, both clauses with
`u=u^*=t`) iff `t <= O(P,Q)`. That is (A.1). (a) and (b) are the two
directions of monotonicity of the predicate `t <= O(P,Q)` in `t`; the point
is that **`O(P,Q)` is one number, fixed once and for all, not a function of
`t`**. (c) restates (A.1). QED.

Two remarks that matter downstream.

* Theorem A3 is *definitional*, exactly as `9f4526f2…:60` claims for its
  display (1.2) and as `f55a00f5…:82-90` confirms. It needs no proof beyond
  unwinding Definition 3.3, and in particular it needs no vertex-level input.
* `I_P` is injective because `pi o I_P = id` (Notation 3.1), and `I_P(0)`
  is the common root `(0,y)` (resp. `(0,x)`) of its component (Notation 3.2,
  Statement 3.3), since two same-side places have `O >= 0`.

> **Corollary A4 (rooted-tree structure).** On each component of `T_a^*`,
> define `F <= G` iff `F in rho_G := I_P([0, pi(G)])` for some/any `P` with
> `G = I_P(pi(G))`. Then:
> (i) `rho_G` is representative-independent;
> (ii) `<=` is a partial order with least element the component root;
> (iii) `{F : F <= G}` is order-isomorphic to `[0, pi(G)]`, so every point has
>       a **unique** rootward path;
> (iv) any two points have a greatest lower bound, and for `G=I_P(s)`,
>       `K=I_Q(t)`, `rho_G n rho_K = I_P([0, min(s,t,O(P,Q))])`.

*Proof.* (i) If `G = I_P(s) = I_Q(s)` then `s <= O(P,Q)` by A3, so for every
`t <= s` also `t <= O(P,Q)` and `I_P(t)=I_Q(t)`; thus `rho_G` is the same set.
(ii) Reflexive and transitive by (i); antisymmetric because `F <= G` forces
`pi(F) <= pi(G)`, so `F <= G <= F` gives `pi(F)=pi(G)` and then `F=G`
by (i). Least element: `I_P(0)`. (iii) `t |-> I_P(t)` is an order isomorphism
`[0,pi(G)] -> {F : F <= G}` by injectivity of `I_P` and (i).
(iv) `I_P(t) in rho_K` iff `t <= t` and `I_P(t)=I_Q(t)` for the relevant
heights, i.e. iff `t <= min(t_K, O(P,Q))`; combine with `t <= s`. QED.

Clause (iii) is precisely the "unique rootward restriction"; clause (b) of A3
is precisely "once two flags differ at one height they differ at every greater
height". Both mandated items are therefore **proved**, from Definition 3.3
alone, and are strictly stronger than the vertex-level statement `MP0`
(`ladder/SHEET6-MULTIPOLE.md:80`) that the prior hostile review found
insufficient.

### A.3 The rational/vertex subtree inherits it, and nothing is requotiented

> **Proposition A5.** `T_a = T_a^* n pi^(-1)(Q)` (Notation 3.6) is a
> rootward-closed sub-poset of `T_a^*` containing `V_a` (Statement 3.4), and
> `(V_a, E_a)` with parent map `F |-> F^o` is a finite rooted tree whose
> geometric realization is the union of the closed segments
> `e_(F,F^o) = I_P([u^*,u])`.

*Proof.* Rootward closure: `F <= G in T_a` and `pi(F) in Q` gives `F in T_a`;
`T_a` is by definition the rational-height slice, which is rootward closed in
the sense that its induced order is the restriction. `V_a subset T_a` is
Statement 3.4 (p. 12). Well-definedness of `F^o`: Notation 3.3 chooses `u^* <
u` with `I_P(u^*) in V_a` and `I_P((u^*,u)) n V_a = empty`; if `F = I_P(u) =
I_Q(u)` then by A3(a) `I_P(t)=I_Q(t)` for all `t <= u`, so the two rays have
the *same* set of vertices below `u` and the same `u^*` — this reproves the
printed "independent of the choice of `P`" from A3 rather than assuming it.
Single-valuedness of the parent plus strict height decrease gives acyclicity;
finiteness of `V_a` is Definition 3.4 (`ladder/SIGRAY-AUDIT.md:23`). QED.

> **Proposition A6 (no later quotient).** Every object the transition calculus
> introduces after Definition 3.3 is either (i) a *point* of `T_a^*` presented
> as `I_P(.)`, (ii) a *subset* of `T_a^*`, or (iii) an object living outside
> the tree (a polynomial, a root of a polynomial, a number). No construction
> imposes a further identification on flags.

*Sweep, with the discriminating reason in each case.*

| object | where | type | why no identification |
|---|---|---|---|
| `F'`, `F*c` | Not 3.8, p. 12 | point | defined as `I_P(pi(F) -+ 1/kappa)`; the printed remark records `kappa`-dependence of the *point*, not of the equivalence |
| `(F*c)' = F` | St 3.5, p. 13 | identity of points | consistency of the two displacements on one ray |
| `F = F'*c` | St 3.6, p. 13 | surjectivity of the step | no gluing |
| `eta_F`, `h^F` | Not 3.9, p. 13 | function | not a tree element |
| `h^+_F`, `d_(h,F)`, `p_(h,F)` | Not 3.10, p. 13 | number/polynomial | not tree elements |
| `F = G+c` | Prop 3.2, p. 18 | point | uniqueness of `c`, `kappa`-independence of the *coefficient* |
| `T_a^+/T_a^0/T_a^-`, `T_a^nearrow/searrow`, `T_(a,cv)`, `T_(a,pole)` | Not 3.14, 6.1, 7.1, 5.2 | subsets | filtration, not quotient |
| `Fhat_P` | Not 7.2, p. 36 | point | selection, not gluing |
| `R_a^*` | Prop 7.3, p. 36 | subset of places | `kappa`-independent by printed claim (S16) |
| `Y(F)`, `lambda_F` | Not 9.3, p. 49 | set of vertices / number | counting, not gluing |
| `M_(a,b)` | St 3.14, p. 16 | cross-**fibre** map | not used here at all (§8 item 3) |
| `mu_(nu_F)`-orbits of roots of `p_F` | St 3.16, p. 17 | orbits **in `C`** | see §B; the map orbit → tree is a section (S15), not a quotient |

This table is the direct answer to the MFE hostile review's fear of "a later
quotient identifying cv representatives". The frozen Fable-5 review reached the
same conclusion in one sentence (`f55a00f5…:83-88`: "There is no further
quotient anywhere in the source … The prior review's fear … has no referent in
Definition 3.3"). I confirm it by exhaustive sweep of Sections 3–9's tree-valued
constructions, and I add the discriminating type in each row, because the
*reason* matters: the cyclic group acts on a **root set in `C`**, and a group
acting on the parameter set of the children of a fixed node cannot glue two
distinct nodes.

### A.4 The two-pole union `U`, its rootward closure, and unique attachment

Let `T_(a,pole) = {P_1,…,P_m}` (`m=2` for LL-1) with pole flags
`F^*_(P_j) = I_(P_j)(v_j)` (Notation 5.1 under the repaired Proposition 5.1),
and set, following `9f4526f2…:90`,

```text
U := union_(j=1..m) I_(P_j)([0, v_j]).                            (A.2)
```

By A4(i) each segment is representative-independent, and by
`ladder/SHEET6-MULTIPOLE.md:80` (MP0) the vertex set of `U` is the campaign's
chain tree `U \ {(0,y)}` together with the root.

> **Lemma A7 (rootward closure and the attachment interval).** `U` is
> rootward closed. For every place `P`,
> ```text
> A_P := {t in [0,infinity] : I_P(t) in U}
>      = [0, max_j min(v_j, O(P,P_j))],                            (A.3)
> ```
> with the convention `O(P,P_j)=infinity` when `P=P_j` and `[0,-1] = empty`.

*Proof.* `I_P(t) in U` iff there is `j` and `s <= v_j` with
`I_P(t) = I_(P_j)(s)`; applying `pi` forces `s=t`, so the condition is
`t <= v_j` **and** `t <= O(P,P_j)` by A3, i.e. `t <= min(v_j, O(P,P_j))`. The
union over `j` of the initial segments `[0, min(v_j,O(P,P_j))]` is the initial
segment up to their maximum. Rootward closure of `U` is the special case
`P = P_j` plus the same computation. QED.

> **Theorem A8 (unique attachment).** Let `H = I_P(w)` be a flag with
> `w > mu_P := max_j min(v_j, O(P,P_j)) >= 0`. Then
> `rho_H n U = I_P([0, mu_P])` and its outermost point
> ```text
> A(H) := I_P(mu_P)
> ```
> is well defined (independent of the representative `P` of `H`), lies in
> `V_a n U`, and is the unique maximal element of `rho_H n U`. If
> `A(H) != A(H')` then no flag lies in both descendant components; more
> precisely, the map `H |-> A(H)` is a well-defined function on the set of
> `y`-side flags off `U`, so its fibres partition that set.

*Proof.* `rho_H = I_P([0,w])` is representative-independent (A4(i)), and
`rho_H n U = I_P(A_P n [0,w]) = I_P([0,mu_P])` by A7 and `w > mu_P`. A
nonempty closed initial segment of a chain has a unique maximum, so
`A(H)` is well defined; representative-independence follows because
`rho_H n U` is a set defined without reference to `P`. Membership in `V_a`:
if the maximum in (A.3) is attained at an index `j` with
`mu_P = O(P,P_j) < infinity` then `I_P(mu_P) in V_(2,a)` by Definition 3.4;
if it is attained with `mu_P = v_j` then `I_P(mu_P) = I_(P_j)(v_j)` is the
pole flag, a vertex; if `mu_P = 0` it is the component root. In all cases
`A(H) in V_a`. Finally `A` is a function, so distinct values give disjoint
fibres. QED.

Theorem A8 is the mandated A.4 in full. Note what it did **not** need: no
finiteness of `U`, no regularity, no pricing, no `Omega`-specific structure
beyond A3, and no hypothesis that `H` is a *selected* witness. The
`min(v_j, ·)` truncation is exactly the endpoint repair that `f55a00f5…:173-200`
prescribed for display (3.2) of the frozen selected-orbit packet; here it is
built into (A.3) from the start, so the endpoint defect cannot recur.

## 4. Part B — the direction-orbit interface

### B.1 Roots of `p_F` occur in `mu_(nu_F)` orbits

Statement 3.16 (p. 17), second half, verbatim: *"Set `F in V_a` and let
`nu := nu_F`. Then there exists a polynomial `ptilde` and `l in N` such that
`p_F(eta) = eta^l ptilde(eta^nu)`."* Hence:

* `0` is a root of `p_F` iff `l >= 1`, with multiplicity `l`;
* the nonzero roots are permuted by `eta |-> zeta eta`, `zeta in mu_nu`, with
  multiplicity preserved; for `c != 0` the orbit `{zeta c}` has exactly `nu`
  distinct elements and one common multiplicity `m_c`.

This is exactly the shape the P0 engine assumes,
`p = (-)eta^epsilon (eta^nu - c^nu)^l prod_j (eta^nu - d_j^nu)^(m_j)`
(`ladder/BOOK-OFFAXIS.md:518-520`), and I verified the shape numerically on all
four LL-1 cells in §C.4 (`dp = epsilon + nu(l + sum_j m_j)` holds exactly).

Statement 3.16's **first** half gives a fact that is used silently everywhere
and is worth stating: for `F in T_a \ (V_a u {(0,x),(0,y)})`, `p_F` has at most
one root, so `F` carries **no** alternative direction. Hence *exits can only
occur at vertices*, and `sum_(F in U)` may be read as `sum_(F in U n V_a)`
without loss.

### B.2 Corrected Statement 3.18 realizes exactly one microchild per orbit

Printed Statement 3.18 (p. 18), verbatim: *"Let `F in T_a`, `kappa in N*` be
suitable such that `kappa pi(F) in N`. Then, if `F*c` exists, then `c` is a
root of `p_F`. If `0` is a root of `p_F`, then `F*0` exists. If `c in C*` is a
root of `p_F`, then there exists a unique `nu_F`-th root of unity, `epsilon`
such that `F*c` exists."*

The final clause is the filed erratum: `epsilon` does not occur in the
conclusion, so as printed it is false for `nu_F >= 2`
(`ladder/SIGRAY-AUDIT.md:52`). The corrected reading, used by every campaign
consumer, is **`F*(epsilon c)` exists**.

> **Lemma B1 (bridge).** Let `F in T_a`, `kappa` suitable with
> `u := pi(F)`, `kappa u in N`, and let `c in C*` be a root of `p_F`. Then
> (i) at least one element of the orbit `mu_(nu_F) c` is realized, i.e. is the
> `Omega`-coefficient at exponent `u` of some place through `F`; (ii) at most
> one element of that orbit is realized. Together: exactly one.

*Proof of (i).* By Proposition 3.1(\*\*) (p. 14, with the print correction
`c_j x^(-j/kappa)` noted at `ladder/SIGRAY-AUDIT.md:39`),
`mult(p_F, c) = #{P in R^* : x(P)=infinity, eta_n(P)=c}`, which is `>= 1`.
So some point of the cover carries a *raw* series with coefficient `c` at
exponent `u`. That cover point lies over a place `P in Rbar_a \ R_a` with
`I_P(u) = F`. Its `Omega`-representative differs from that raw series by a
deck substitution fixing the prefix below `u`, and such substitutions act on
the coefficient at exponent `u` through `mu_(nu_F)` (the cyclic
semi-invariance computation, reproduced and independently re-checked at
`f55a00f5…:230-251`). Hence `Omega(P)`'s coefficient at `u` is `zeta c` for
some `zeta in mu_(nu_F)`, and `F*(zeta c)` exists.

*Proof of (ii).* Suppose `P,Q` are places through `F` with `Omega`-coefficients
`epsilon c` and `epsilon' c` at `u`, `epsilon,epsilon' in mu_(nu_F)`. Since
prefix-fixing deck substitutions permute the raw representatives of `P` and act
on the height-`u` coefficient through `mu_(nu_F)`, `P` also admits a raw
representative with coefficient `epsilon' c`. Two raw representatives of `P`
and `Q` then agree at every exponent `<= u`, so `O(P,Q) > u`; by S3,
`Omega(P)` and `Omega(Q)` agree at `u`, i.e. `epsilon c = epsilon' c`, and
`c != 0` gives `epsilon = epsilon'`. QED.

**Load-bearing scope.** Only (i) is load-bearing for the budget theorem of
§C: it guarantees that every *priced* orbit is an actual direction with a
nonempty cluster, so Statement 7.3 has something to act on. Clause (ii)
(uniqueness) is used only for exactness of the per-orbit *menu*; if some orbit
happened to realize two children, the P0 per-orbit sum would be an
**undercount**, and every inequality in §C would still hold. I flag this
explicitly because the corrected form of Statement 3.18 is a filed erratum,
and it is worth knowing that the two-pole budget does not stand or fall with
its uniqueness half.

### B.3 Different realized microchildren are different, permanently

> **Theorem B2.** Let `F in T_a`, `u := pi(F)`, and let `c != c'` be two
> realized coefficients at `F` (i.e. `P(F,c), P(F,c') != empty`, where
> `P(F,c) := {P : I_P(u)=F and Omega(P)_u = c}`). Then for **every**
> `P in P(F,c)` and `Q in P(F,c')` and every `t > u`,
> `I_P(t) != I_Q(t)`. In particular the descendant components of the two
> microchildren are disjoint, and no later construction can identify a flag of
> one with a flag of the other.

*Proof.* `Omega(P)` and `Omega(Q)` differ at exponent `u`, so
`O(P,Q) <= u < t`, and A3(b) gives `I_P(t) != I_Q(t)`. The "no later
construction" clause is Proposition A6: `~` of Definition 3.3 is the only
identification in the source. QED.

Theorem B2 subsumes and generalizes the frozen packet's Lemma 3.1(2)
(`9f4526f2…:155-163`) and AF2 §2 R4's distinctness line: those are stated for
one *selected* witness per direction; B2 is stated for the whole cluster on
both sides.

Two further items requested by the mandate.

* `P(F,c)` is **`kappa`-independent** and equals Sigray's own `R_a^*` of
  Proposition 7.3 (p. 36): "`R_a^* := {P in Rbar_a \ R_a : I_P(u+1/kappa) =
  F*c}`. Then the set `R_a^*` does not depend on the choice of `kappa`."
  So the cluster is a printed object, not a campaign invention.
* `P(F,c) = P(F*_kappa c) = P(F+c)` for every suitable `kappa` and the next
  vertex `F+c`. Indeed if `P,Q in P(F,c)` then `O(P,Q) > u`; if
  `O(P,Q) < pi(F+c)` then `I_P(O(P,Q)) in V_(2,a)` would be a vertex strictly
  between `F` and `F+c` on that ray, contradicting Notation 3.3's defining
  property of the edge `e_(F+c, F)`. Hence `O(P,Q) >= pi(F+c)` and
  `I_P(pi(F+c)) = I_Q(pi(F+c))`. This closes the microstep/next-vertex
  distinction that sweep r2 `581219e0…` insisted on
  (`ladder/SIGRAY-AUDIT.md:79`, `ladder/SHEET6-AF2.md` §2 R1): the two objects
  differ as *points*, but they have the **same cluster of places**, which is
  all the exit-set argument uses.

### B.4 The MFE abstract countermodel: which axiom it violates

The countermodel (`ac49c025…:135-151`) is: keep the MP0 tree `P -> F -> R`,
`U={P,F,R}`; let `d_1 != d_2` be two local direction-orbits at `F`; *"Suppose
the cyclic/orbit quotient identifies their later cv representatives `H_1,H_2`
as one cv flag `H`, retaining both incidences."*

> **It violates Definition 3.3(ii), read with Definition 3.2 and Statement
> 3.2(ii).** Nothing else.

Precisely. Write `H_i = I_(P_i)(w)` with `P_i in P(F,c_i)`, `c_1 != c_2`,
`w > u = pi(F)`. Identifying `H_1 = H_2` means `(P_1,w) ~ (P_2,w)`, which by
Definition 3.3(ii) requires `w <= O(P_1,P_2)`. But Definition 3.2 computes
`O(P_1,P_2)` as a first-difference index of the (`Omega`-selected, S3) series,
and those differ already at exponent `u`; hence `O(P_1,P_2) <= u < w`.
Contradiction. The single structural feature that kills the countermodel is
that **`O(P,Q)` is one height-independent rational number**, so the predicate
`t <= O(P,Q)` is downward closed in `t` and cannot switch back on — the
"retaining both incidences" clause is exactly a request for a non-monotone
predicate.

The second half of the countermodel — *"the same diagram can make `H` appear
attached to two different vertices of `U`"* — violates the same axiom via
Lemma A7: `A_P` is an interval because each `{t : I_P(t)=I_(P_j)(t)}` is an
initial segment; two attachments would require `A_P` to be disconnected.

**Is the source's bridge from root orbits to microchildren complete?** Yes,
with one filed correction. The chain is:
`p_F` root pattern (S12, printed) → realization of at least one orbit
representative (Prop 3.1(\*\*), printed, plus the prefix-stabilizer action) →
distinctness of realized children (Theorem B2, Definition 3.3) → uniqueness
per orbit (corrected S15). Only the last link rests on a filed erratum, and
§B.2 records that it is not load-bearing for the inequality. **No countermodel
satisfying every available statement exists**, and I therefore do not exhibit
one; the mandate's fallback branch is not triggered.

### B.5 Every priced non-chain direction is an actual child component

Define, at `F in U n V_a` with `u := pi(F)`:

```text
Ch(F) := {Omega(P_j)_u : P_j pole ray with I_(P_j)(u)=F and v_j > u}
Rea(F):= {c : P(F,c) != empty}
Ex(F) := {c in Rea(F) \ Ch(F) : the microchild F*c lies in T_a^nearrow}
```

`Ch(F)` is the set of *chain-arrival* coefficients: one at a trunk or
pre-merge vertex, `r(F)` at a merge, none at a pole flag (endpoint case).
`Ex(F)` excludes them, and the rootward direction is not a root of `p_F` at all
(the roots of `p_F` parameterize the directions **above** `F`; Proposition 3.2
writes the child as `F = G + c` with `G = F^o`, so the parent is not indexed by
a root). Merge arrivals are additionally excluded on the pricing side by
`ladder/SHEET6-2POLE.md:234-236` ("the OTHER chain's orbit is never
lambda-charged (it is searrow …)") and `ladder/SHEET6-MULTIPOLE.md:105-118`
(MP8: "excluding pole arrivals and the rootward continuation").

By S23 (repaired Propositions 6.7/6.8, gate row at `ac49c025…:96-104`), a
direction with `gap(c) := X_F/mult - kbar_F > 0` has its microchild in
`T_a^nearrow` unconditionally, and a direction with `gap(c) < 0` is a searrow
microstep that the 6.8 recursion carries along the same branch to a pole,
hence is a chain arrival; Statement 6.1 excludes `gap = 0`. Therefore

```text
{ priced non-chain directions at F } = Ex(F),
```

each element of which is, by Lemma B1(i), an actual realized child with a
nonempty cluster `P(F,c)`, and, by Theorem B2, a child component disjoint from
every other. This discharges the fourth mandated bullet of Part B.

## 5. Part C — the full actual exit consumer

### C.1 Definition of `E_all(F,d)`

For `F in U n V_a` and `d = c in Ex(F)` set

```text
P(F,c) = {P in Rbar_a \ R_a : I_P(pi F)=F, Omega(P)_(pi F)=c}   (finite, = R_a^*)
u_0(P) = the unique u with d_(f-a,I_P(u)) = 0        (S11, corrected St 3.13)
E_all(F,c) = { I_P(u_0(P)) : P in P(F,c) }  as a SET of flags.   (C.1)
```

Well-posedness and nonemptiness:

1. `P(F,c) != empty` by definition of `Rea(F)`, and finite because
   `Rbar_a \ R_a` is finite (Statement 3.2, p. 11).
2. For every `P in P(F,c)`, the microchild `F*_kappa c = I_P(pi F + 1/kappa)`
   lies on `I_P` and is in `T_a^nearrow` (§B.5). Statement 7.3 (p. 35) is
   **universal in `P`** — "Set `P in Rbar_a \ R_a`. Assume that there exists
   `u in Q+` such that `I_P(u) in T_a^nearrow`. Then there exists `v in Q+`
   such that `I_P(v) in T_(a,cv)`" — so each such `P` carries a cv flag.
3. `T_(a,cv) subset T_a^0` (Notation 7.1) and S11 gives at most one `T_a^0`
   point per ray, so that cv flag **is** `I_P(u_0(P))`, and `E_all(F,c)` is
   exactly the set of cv flags lying on the rays of the cluster.
4. `u_0(P) > pi(F)`: `d` is monotone decreasing along the ray (S10) and
   `d_(F*c) > 0` because `F*c in T_a^nearrow subset T_a^+`; since
   `d_(I_P(u_0(P)))=0`, S11's uniqueness forces `u_0(P) > pi(F*c) > pi(F)`.
   Independently, `pi(H) > 1 > pi(F)` by S19 and `F in T_a^searrow`.

> **Closure property.** `E_all(F,c) = {H in T_(a,cv) : A(H) = F and the
> exit coefficient of `H` at `F` is `c`}`, and membership is
> representative-independent: if `H = I_P(w) = I_Q(w)` with `P in P(F,c)`,
> then `w <= O(P,Q)` and `pi(F) < w`, so `I_Q(pi F) = F` and
> `Omega(Q)_(pi F) = Omega(P)_(pi F) = c`, i.e. `Q in P(F,c)`.

So `E_all` is a *flag-intrinsic* object; no choice of representative leaks.

### C.2 All members attach at `F`; the family is pairwise disjoint over `U`

> **Theorem C1 (full attachment).** Let `F in U n V_a`, `u := pi(F)`,
> `c in Ex(F)`. Then for **every** `P in P(F,c)`,
> ```text
> A_P = [0, u].                                                   (C.2)
> ```
> Consequently every `H in E_all(F,c)` lies outside `U`, has attachment
> `A(H) = F`, and lies in the `y`-component.

*Proof.* `(⊇)` `I_P(u) = F in U` and `U` is rootward closed (Lemma A7), so
`[0,u] subset A_P`.

`(⊆)` Suppose `t in A_P` with `t > u`. By (A.3) there is an index `k` with
`t <= v_k` and `t <= O(P,P_k)`. Then:

* `O(P,P_k) >= t > u`, so by Definition 3.2 the series `Omega(P)` and
  `Omega(P_k)` agree at **every** exponent `<= u`; in particular
  `Omega(P_k)_u = Omega(P)_u = c`;
* `u < t <= O(P,P_k)` also gives `I_(P_k)(u) = I_P(u) = F`, so the `k`-th pole
  ray passes through `F`;
* `v_k >= t > u`, so the `k`-th pole segment continues strictly above `F`.

The three bullets say exactly `c in Ch(F)`, contradicting `c in Ex(F)`.
Hence `A_P = [0,u]`. Since `u_0(P) > u`, `H = I_P(u_0(P)) notin U`, and
Theorem A8 gives `A(H) = I_P(u) = F`. The component claim is because `I_P` is
connected and `F` is `y`-side. QED.

Three things to notice about this proof, because they are the whole finding.

* It uses `P` **only** through `I_P(u)=F` and `Omega(P)_u=c`. It never uses
  that `P` was *selected*, never uses Statement 7.3, never uses a price, and
  never uses `kappa`. So it applies to the whole cluster verbatim.
* It handles the **pole-endpoint case** with no separate argument: if the only
  pole rays through `F` stop at `F` (`v_k = u`), the third bullet fails
  immediately, so `Ch(F) = empty` and every realized `c` is an exit. This is
  the configuration where the frozen packet's display (3.2) was false
  (`f55a00f5…:161-172`); phrasing the lemma through the truncated interval
  (A.3) rather than through "contact is exactly `u`" removes the defect at the
  source.
* It handles **several pole rays through `F`** (the merge and the whole shared
  suffix) with no separate argument: the quantifier over `k` is already there.

> **Theorem C2 (pairwise disjointness).** The family
> `{E_all(F,c)}_(F in U n V_a, c in Ex(F))` is pairwise disjoint.

*Proof.* *Same `F`, different `c != c'`.* Let `H in E_all(F,c) n E_all(F,c')`,
say `H = I_P(w) = I_Q(w)` with `P in P(F,c)`, `Q in P(F,c')`. Flag equality
gives `w <= O(P,Q)`; Theorem B2 gives `O(P,Q) <= pi(F) < w`. Contradiction.

*Different `F != F'`.* Every `H in E_all(F,c)` has `A(H)=F` and every
`H in E_all(F',c')` has `A(H)=F'` by Theorem C1; `A` is a function
(Theorem A8), so the two sets are disjoint. QED.

> **Theorem C3 (`x`-side disjointness).** The `x`-side witness `H_x` used to
> supply `psi` lies in the other component of `T_a^*` (Statement 3.3, p. 11),
> hence differs from every `H in E_all(F,c)`.

This reproduces, at the two-pole union, the singleton-pole step at
`2763d970…:329-333`.

**Shared suffix counted once.** `U` is a set; `U n V_a` is a set of vertices;
the outer sum in (C.3) below runs over that set. A vertex lying on both pole
paths contributes one term. This is the two-pole analogue of MP8's clause "A
shared suffix occurs once, never once per pole path"
(`ladder/SHEET6-MULTIPOLE.md:113-114`), now with the full sets rather than the
selected witnesses.

### C.3 The exact simultaneous single-budget inequality

Write, for `F in U n V_a` and `c in Ex(F)`,

```text
W(F,c) := sum_(H in E_all(F,c)) kappa_H (pi(H) - 1)      (actual exit weight)
```

> **Theorem C4 (two-pole full-actual first-separation budget).** On the fibre
> `f=a`, with `U` as in (A.2) and `psi` the certified `x`-side weight,
> ```text
> sum_(F in U n V_a) sum_(c in Ex(F)) W(F,c)  <=  td(f,g) - 1 - psi.   (C.3)
> ```

*Proof.* By Theorems C1–C3 the set
`S := {H_x} u (disjoint union over (F,c) of E_all(F,c))` is a set of pairwise
distinct elements of `T_(a,cv)` on the single fibre `f=a`. Apply the reviewed
actual-weight Corollary 7.1 **once** to `S` (S21: `(C7.1*)` holds for
`T_(a,cv)` and hence for every pairwise-distinct subset,
`c253bd12…:33`, `:266-267`, Terra gate amended-hash PASS at `727f5850…:12`):

```text
td(f,g) >= 1 + kappa_(H_x)(pi(H_x)-1) + sum_(F,c) W(F,c)
        >= 1 + psi + sum_(F,c) W(F,c).
```

Rearranging gives (C.3). QED.

> **Corollary C5 (priced form).** With `L_safe` (S24) and the zero-direction
> rule kept separate,
> ```text
> lambda_F^full := sum_(j : nonzero non-chain orbits) L_safe(X_F/m_j - kbar_F)
>                + [0 in Ex(F)] * max(1, ceil((X_F/epsilon_F - kbar_F)/nu_F))
> ```
> satisfies `sum_(F in U n V_a) lambda_F^full <= td(f,g) - 1 - psi`, with
> ```text
> L_safe(delta) = delta            if delta in N*,
>                 ceil(2 delta)    if delta > 0 nonintegral.
> ```

*Proof.* By Lemma B1(i) and §B.5 the nonzero non-chain **orbits** index the
elements of `Ex(F) \ {0}` (at least injectively; if an orbit realized more than
one child the sum is an undercount and the inequality is unaffected — §B.2).
For each such `c`, the per-flag bound of corrected Statement 9.3
(`2763d970…:252-268`, sign erratum E6 repaired) holds for **every** ray of the
cluster: for `P in P(F,c)` and `H = I_P(u_0(P))`, S9(iii) gives
`d_(F*c) = d_F - mult(p_F,c)/kappa`, and S10 gives `omega*` monotone
decreasing, so `d` falls at rate at most `mult(p_F,c)` on `[pi F, u_0(P)]`;
hence `u_0(P) - pi(F) >= d_F/mult(p_F,c)` and, with `kappa_H >= kappa_F`,
`kappa_H(pi(H)-1) >= D_F/mult(p_F,c) - K_F = X_F/m_j - kbar_F = delta`.
Together with the integrality line S22 this is precisely the input list of the
promoted safe-floor lemma (`05f68f4b…:429-450`), whose branch C ("singleton
with `q=1`") requires **full physical-place coverage** — supplied here by the
closure property of §C.1, which makes `E_all(F,c)` the complete cv slice of the
direction. For `c=0` the same chain runs with `kappa_H >= kappa_F/nu_F`, giving
the printed `/nu_F` summand; `L_safe` is **not** applied there. Summing the
per-direction floors and using Theorem C4 gives the corollary. QED.

**This is a floor.** Nothing above asserts that any `W(F,c)` equals its floor;
`ladder/BOOK-OFFAXIS.md:497` ("It is never an attainment theorem") is respected
throughout, and no `delta_a = 0` or equality form of Proposition 7.5 is used or
implied.

### C.4 Application to LL-1's four multiplicity-3 P0 cells

LL-1 R3 is the two-pole packet `packet = "LL1-R3 (td=6, m=2)"`, header
`{td:6, m:2, Lambda:[3,3], type:[2,3]}`, `poles = [P1,P2]` each
`(a,b,nu,M,kbar,w0) = (1,1,2,1,5,2)`
(`cases/landing_ledger_ll1_r3_20260829/out/ll1_book.json`, `sections.entry[0]`).
The four cells sit on the shared suffix below the single merge (MP1 forces
exactly one merge at `m=2`), all reached from source state `(w,M,charge) =
(3/4, 4, 2)`. Those suffix vertices lie in `C_1 n C_2 subset U`, and by MP1
each has a **unique** chain predecessor, so `|Ch(F)| = 1` at each of them and
the extra orbit plus the zero root are genuine exits.

Independent recomputation from the stored `(dp,dq,nu,l,k,eps,mults)` — I wrote
the arithmetic from the P0 formulas rather than importing the checker:

| cell | `eps` | `l` | `nu` | `mults` | `dp` check | `dq` check | `E` | `kbar` | `X` | `delta` |
|---|---:|---:|---:|---|---|---|---:|---:|---:|---|
| `(17,5)@2` | 3 | 4 | 2 | `[3]` | `3+2(4+3)=17` | `1+2(1+1)=5` | 3 | 5 | 17 | `17/3-5=2/3` |
| `(51,15)@7` | 2 | 4 | 7 | `[3]` | `2+7(4+3)=51` | `1+7(1+1)=15` | 9 | 5 | 17 | `2/3` |
| `(85,25)@12` | 1 | 4 | 12 | `[3]` | `1+12(4+3)=85` | `1+12(1+1)=25` | 15 | 5 | 17 | `2/3` |
| `(119,35)@17` | 0 | 4 | 17 | `[3]` | `0+17(4+3)=119` | `1+17(1+1)=35` | 21 | 5 | 17 | `2/3` |

with `E = l·dq - dp`, `kbar = l·w_src·dq/E` at `w_src = 3/4`, `X = kbar·dp/dq`.
All twelve identities hold exactly. Strict NE tests
(`ladder/BOOK-OFFAXIS.md:520-521`) also hold: `m_j·dq < dp` gives
`15<17, 45<51, 75<85, 105<119`; `eps·dq < dp` gives `15<17, 30<51, 25<85`
(and is vacuous at `eps=0`).

Applying Corollary C5 cell by cell, keeping the zero/epsilon direction on the
old rule:

| cell | nonzero orbits | `L_safe(2/3)` | zero defect `(X/eps-kbar)/nu` | zero floor | `lambda^full` | book `lam` |
|---|---:|---:|---|---:|---:|---:|
| `(17,5)@2` | 1 | `ceil(4/3) = 2` | `(17/3-5)/2 = 1/3` | 1 | **3** | 2 |
| `(51,15)@7` | 1 | 2 | `(17/2-5)/7 = 1/2` | 1 | **3** | 2 |
| `(85,25)@12` | 1 | 2 | `(17/1-5)/12 = 1` | 1 | **3** | 2 |
| `(119,35)@17` | 1 | 2 | — | 0 | **2** | 1 |

Each cell moves by exactly `+1`, carried entirely by the single nonzero
multiplicity-3 direction; **no epsilon/zero direction is repriced**, and the
`PURE-B` and `NEUTRAL` families (which have `k = lex = Sm = 0`, hence no
nonzero extra direction) are untouched. `2/3` is the only nonintegral defect in
the book exceeding `1/2`, so these four are the only cells `L_safe` can move —
the book's nonintegral defect set is `{2/3, 1/2, 1/3, 1/4, 1/6}` and
`L_safe = max(1,ceil(delta))` on the rest.

Why this is now *typed* rather than *declared*: the previous obstacle was
whether the four `E_all` sets, each possibly containing several distinct cv
flags, may be inserted into one Corollary 7.1 application alongside every other
priced direction on **both** pole paths. Theorems C1–C4 supply exactly that,
for the union of the two pole paths, with the shared suffix counted once.

Budget side, unchanged and inherited: `td=6`, `psi >= 1`, so the shared budget
is `sum lambda <= 4` (`ladder/SHEET6-2POLE.md:148-149`), refined at termination
by `psi = ceil(1/(1-w_G)) - 1` (`ladder/BOOK-OFFAXIS.md` P1). The downstream
13→7 alive-inventory consequence of these four `+1`s is the frozen checker
result reproduced at `3e3cea4a…` §4; I did **not** re-run it (§8 item 7).

### C.5 The weaker partial type I found

Three carrier types are now cleanly separable, and a fourth was worth naming:

| tag | object charged | what it needs | status here |
|---|---|---|---|
| `REPRESENTATIVE` | one Statement-7.3 witness per direction-orbit | frozen selected-orbit lemma | already GREEN (`9f4526f2…`, `f55a00f5…`) |
| `FULL_ACTUAL_FIRST_SEPARATION` | `E_all(F,d)` for every priced `d` at every `F in U`, one budget | Theorems C1–C4 + S21–S24 | **PROVED here** |
| `FULL_ACTUAL_SINGLE_VERTEX` *(new, weaker)* | `E_all(F,d)` at **one** vertex `F`, other vertices left `REPRESENTATIVE` | Theorem C1 at that `F` + C2's same-`F` clause only | proved a fortiori; useful when only one cell is being repriced |
| `FULL_ACTUAL_EXIT` (BOOK-OFFAXIS wording) | as `FULL_ACTUAL_FIRST_SEPARATION`, plus attainment | an attainment theorem | **NOT** proved, and not claimed |

The third row is the genuinely weaker partial type the mandate asked me to look
for. It matters because a consumer that reprices a *single* cell — which is
what each of LL-1's four independently does at its own vertex — needs only
Theorem C1 at that vertex plus the same-`F` clause of Theorem C2; the
cross-vertex clause (and therefore Theorem A8) is needed only when two repriced
cells lie on one route. In the LL-1 book they do: the four cells sit on routes
that also charge other vertices, so the full type is the one actually
consumed.

The fourth row is a naming hazard I want on record: `ladder/BOOK-OFFAXIS.md:500`
calls its stronger type `FULL_ACTUAL_EXIT`, and the word "exit" there means the
*set*, not an equality. Read literally as "the exit charge", it would invite
attainment. `FULL_ACTUAL_FIRST_SEPARATION` is the name I emit, and it is
defined as *floor-valued*.

## 6. Why the prior blocker was a perimeter omission

The MFE hostile review's blocker (`ac49c025…:44-60`) was stated as the jump
from `MP0` ("`U` is a finite tree under `F -> F^o`") to "an ambient `T` in
which every cv witness has a unique root path". Its diagnosis was accurate:
MP0 is a **vertex-level** statement about a **down-vertex set**, and it cannot
yield a **point-level** statement about `T_(a,cv)`. But the missing statement
was not missing from the *mathematics*; it was missing from the *citation*.
Definition 3.3 supplies it in one line (Theorem A3), and Definition 3.3 was
inside the advertised perimeter the whole time.

Three specific ways the omission propagated, each now closed:

1. **`MP0` was cited where Definition 3.3 was needed.** The frozen producer's
   Section 2 ambient paragraph leaned on the finite chain tree. The repair
   packet replaced it with (1.1)/(1.2) and (2.2); §A here proves those from
   Definition 3.3 with the equivalence-relation hygiene (Lemma A1, Corollary
   A2) that the thesis never printed.
2. **"Cyclic quotient" was a category error.** The review reasonably feared a
   second quotient because the campaign's own language ("direction-orbit",
   "orbit quotient") sounds like one. Proposition A6 shows the cyclic action
   lives on the root set of `p_F` in `C`; corrected Statement 3.18 is a
   *section* of that action into the tree, so the induced map
   `{orbits} -> {children}` is injective by Theorem B2. There is nothing to
   quotient.
3. **Strong-vs-weak was a quantifier, not a hypothesis.** The stable rereview
   (`3e3cea4a…` §7.3 item 1) recorded that the full-set upgrade "needs a
   strictly stronger hypothesis than the legacy book" — the arborescence
   "containing … every flag in `T_(a,cv)`" versus the version "stated only for
   the finite set of selected directions and their 7.3 witnesses". That
   asymmetry is real **as written**. It is not real **as proved**: the
   selected lemma's own proof (`9f4526f2…:136-166`) uses the witness ray only
   through `I_P(u)=F` and non-arrival of the direction, and both hold for
   every ray of `P(F,c)`. Theorem C1 is the same proof with the quantifier
   moved, plus the truncation fix that `f55a00f5…` §3 had already prescribed.

So the honest classification of the prior blocker is: **a perimeter/citation
omission that a hostile referee was right to refuse to waive, and that costs
one page of Definition-3.3 bookkeeping to close** — not a mathematical gap, and
not a place where a countermodel was ever available.

I record one respect in which the prior review was *more* than cautious and
was correct to be: its abstract countermodel is a valid proof that MP0 alone
cannot discharge the assertion. It is refuted only by adding Definition 3.3,
which is exactly what it asked for.

## 7. Dependency graph

```text
Def 3.2 (p.10) ─┐
St 3.1  (p.10) ─┼─> Lemma A1 (ultrametric)  ──> Cor A2 (~ is an equivalence)
St 3.2  (p.11) ─┘                                     │
                                                      v
Def 3.3 (p.11) ──────────────────────────────> Thm A3 (flag = contact)
                                                 │        │
                            Not 3.1/3.3, Def 3.4 │        │
                                                 v        v
                                      Cor A4 (rooted tree)  Prop A5 (V_a tree)
                                                 │              Prop A6 (no requotient)
                                                 v
                          Not 5.1/5.2 ──> U (A.2) ──> Lem A7 (A_P interval)
                                                 │
                                                 v
                                             Thm A8 (unique attachment, A: flags -> U n V_a)
                                                 │
St 3.16 (p.17) ──> B1(i) roots in mu_nu orbits   │
Prop 3.1(**)   ──> Lem B1(i) realization         │
cyclic semi-inv ─> Lem B1(ii) uniqueness  [not load-bearing]
St 3.18 corr.  ──> one child per orbit           │
                        │                        │
                        v                        v
                    Thm B2 (children permanently distinct)
                        │                        │
Prop 6.7/6.8 repaired ──┴─> §B.5 Ex(F) = priced non-chain directions
                                                 │
St 7.3 (p.35, universal in P) ───────┐           │
St 3.13 corr. (p.16, unique zero) ───┼──> §C.1 E_all(F,c) well posed, complete
Prop 7.3 R_a^* kappa-indep (p.36) ───┘           │
                                                 v
                                   Thm C1 (full attachment)  <── Lem A7
                                   Thm C2 (pairwise disjoint) <── Thm A8, Thm B2
                                   Thm C3 (x-side)            <── St 3.3
                                                 │
(C7.1*) actual-weight [c253bd12, Terra 727f5850] ┴─> Thm C4 (single budget, C.3)
                                                 │
St 3.9(iii)+St 3.10 ─> per-flag delta bound      │
St 9.4 integrality line (S22) ───────────────────┼─> Cor C5 (priced form, L_safe)
L_safe [BOOK-OFFAXIS:473, arity 6.2] ────────────┘
                                                 │
                                                 v
                                   §C.4 LL-1 four cells: 2,2,2,1 -> 3,3,3,2
```

Inputs **not** used anywhere above, deliberately: Statement 3.14 (cross-fibre,
`GAP`); printed Proposition 7.5 equation (22); the literal per-puncture
`delta_a`; `(22-cl)`; MP8's no-refinement claim; any fixed cross-fibre `kappa`
transport; Notation 3.5's `kappa_F` inside §A/§B.

## 8. Scope limitations and what is *not* proved

1. **One fibre only.** Every statement in §A–§C is about a single `f=a`. No
   cross-fibre transport, no Statement 3.14, no `M_(a,b)`. `(C7.1*)`'s own
   proof does use a fibre-comparison argument, but it is consumed as a black
   box at its reviewed scope.
2. **H5a / Notation 3.5.** `kappa_F` is not well-defined as printed
   (`ladder/SIGRAY-AUDIT.md:26`; forced repair = jump/max). §A and §B are
   `kappa_F`-free. §C's *weights* are not: `W(F,c)`, `delta`, `q_H = kappa_H/
   kappa_F` and hence `L_safe` all inherit the H5a convention. The attachment
   theorem is unconditional on H5a; the numeric floor is not.
3. **Integrality line (S22).** `kappa_H(pi(H)-1) in N*` is the campaign's
   "St 9.4-proof integrality line", inherited, not re-derived here. Both
   `L_safe` branches (`2 ceil(delta)` and `ceil(2 delta)`) consume it. If it
   failed, the floors would degrade to the real-valued bounds `2 delta` and
   `2 delta`, and `L_safe(2/3)` would drop from 2 to `>4/3`, i.e. the four
   cells would not move.
4. **No attainment.** `L_safe` is a floor; `W(F,c)` may exceed it. No equality,
   no `delta_a = 0`, no restoration of printed (22), no MP8 equality rhetoric.
5. **Statement 3.2 has no printed proof.** Lemma A1 is given twice, once with
   `Omega` and once without, precisely so that Part A does not rest on an
   unproved Statement. The rest of §B's `Omega`-coefficient language *does*
   use S3; where it matters (Lemma B1(ii)) I flagged that the clause is not
   load-bearing.
6. **`Ex(F)` typing is inherited.** That every remaining direction is
   `nearrow` or a same-branch chain arrival is repaired Propositions 6.7/6.8
   (S23), reviewed but outside this report. If a priced direction were not
   `nearrow`, Statement 7.3 would give nothing and that summand would be
   unjustified — the failure mode would be an over-charge, i.e. unsafe, so
   this input is genuinely load-bearing and is declared.
7. **LL-1 downstream.** I verified the four cells' arithmetic and their
   `+1` increments independently. I did **not** re-run
   `cases/m2_exit_safe_floor_legacy_reprice_r1_20260829/check.py` and did not
   re-derive the 13→7 alive inventory, the pooled-BFS legitimacy, or the
   `(2/7,7,4)` path analysis; those are `3e3cea4a…` §§4–5 results, inherited.
8. **Menu exhaustiveness is inherited.** That the LL-1 residue-step menu and
   the `td=12` thirteen-edge menu are complete is not a result of this report.
9. **M-PAT and the two-pole pattern zoo.** `ladder/SHEET6-2POLE.md:219-233`
   flags its merge-step patterns as hypothesis `M-PAT` at H1/H4 trust tier.
   Theorem C4 does not depend on M-PAT (it is a statement about `U` and
   `T_(a,cv)`, not about which patterns occur); the LL-1 *numbers* do.
10. **Not a landing, realizability, ceiling, Keller or JC2 statement.** In
    particular nothing here excludes `td=6`.
11. **No promotion.** This is a primary attack. Whether the LL-1 book carries a
    `FULL_ACTUAL_FIRST_SEPARATION` field, and whether its quarantine at
    `ladder/BOOK-OFFAXIS.md:504-506` lifts, is a coordinator decision.
12. **Process.** No canonical, ladder, case, guardrail or operations file was
    edited; this report is the only file created; no commit, push, web, AWS,
    install or heavy computation occurred; `jc2-lean` was never entered,
    enumerated, searched, read, built, modified, status-checked or controlled.

## 9. Machine-readable consumer tags and charge declarations

```text
attachment_theorem = PROVED_FULL_TWO_POLE_ATTACHMENT
scope              = one fibre f=a; U = union of the m pole characteristic paths; m>=1
carrier_type       = FULL_ACTUAL_FIRST_SEPARATION
weaker_partial     = FULL_ACTUAL_SINGLE_VERTEX   (one vertex repriced, others REPRESENTATIVE)
supersedes         = REPRESENTATIVE  (strictly stronger; REPRESENTATIVE remains valid)
excludes           = FULL_ACTUAL_EXIT-with-attainment  (NOT proved)
budget_form        = sum_(F in U n V_a) lambda_F^full <= td - 1 - psi
disjointness_proof = Thm C1 (attachment) + Thm C2 (pairwise) + Thm C3 (x-side)
attainment         = NOT_CLAIMED
epsilon_directions = SEPARATE; priced by max(1, ceil((X/eps - kbar)/nu)); L_safe NOT applied
zero_orbit         = single child, guaranteed by corrected St 3.18 existence half
inherited_inputs   = S21 (C7.1*), S22 (integrality), S23 (6.7/6.8), S24 (L_safe), H5a kappa
```

**Charge declarations for the LL-1 `delta=2/3` cells.** FALLACY.md permits one
`charge_basis=` line per exit claim; the mandate requires the two exhaustive
nonintegral branches. These are the two branches of a **single** exit claim —
the branch `q=1-exact` is impossible because `delta = 2/3 notin N*` — and both
branches yield the same charged value `2`, so the declaration is unambiguous.

```text
charge_basis={"delta":"2/3","branch":"q>=2","flag_count":1,"citation":"xmodel/m2-arity-law-place-conservation-source-audit-sol56-20260829.md:443"}
charge_basis={"delta":"2/3","branch":"multi-flag","flag_count":2,"citation":"xmodel/m2-arity-law-place-conservation-source-audit-sol56-20260829.md:441"}
```

Branch reading, so that the declaration is auditable:

* `q>=2`: `E_all(F,c)` is a singleton `{H}` with `q_H = kappa_H/kappa_F >= 2`;
  then `w_H >= 2 delta = 4/3` and `w_H in N*` give `w_H >= ceil(4/3) = 2`.
* `multi-flag`: `|E_all(F,c)| >= 2`; each flag has `w >= ceil(2/3) = 1`, total
  `>= 2`.
* `q=1-exact` is excluded: it forces `tau_0 = D/m` and `w = delta = 2/3 notin
  N*`. Its exclusion is exactly what **full** coverage buys, and full coverage
  is what §C.1's closure property and Theorem C1 establish.

Cells covered by these two lines, each with one nonzero orbit of per-root
multiplicity 3 at `(X,kbar) = (17,5)`:
`(17,5)@2`, `(51,15)@7`, `(85,25)@12`, `(119,35)@17`.
Zero-direction summands `1,1,1,-` are declared separately and are **not**
repriced. Resulting `lambda^full`: `3,3,3,2` against book `lam` `2,2,2,1`.

## 10. Custody after

`shasum -a 256`, full values, re-verified immediately before sealing; identical
to the before-run and to the declared perimeter.

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
ded3051d1a2009498f49bed20e5168d34b823518ab1b94ed340b380b37da6d15  ladder/SIGRAY-AUDIT.md
86b491adc6ba6b21fcec5a8722126d80f3666d8e3d9f2cdcf4568d408bbc83a8  xmodel/sigray-multipole-global-first-exit-partition-sol-ultra-20260828.md
ac49c025e3e010d3ecaf3839adf51c40cb88b0088198ae1c5ab1198e07cc8004  xmodel/sigray-multipole-global-first-exit-partition-hostile-review-gpt56-20260828.md
2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933  xmodel/sigray-section9-source-audit-sol-ultra-20260828.md
0729a5765729a9e3a6f99720a638cc94a3d3a7837e3946412e13c4233e6b5bad  xmodel/sigray-section9-source-audit-hostile-review-gpt55-20260828.md
05f68f4b7278a8ac1216ba82b40e7081bfff66f351380ccd671d12a955784d84  xmodel/m2-arity-law-place-conservation-source-audit-sol56-20260829.md
56e95db58e53aa030ef1100cc1640d115105a77607d40e3f160e77b46174a34d  xmodel/m2-arity-law-place-conservation-source-audit-hostile-review-fable5-20260829.md
c253bd12d205eed7c01e42a21204c5735d0f5cba70dce1d962fb8744dbd95eb6  xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md
727f58506af4ff36f6a8c39bb83420c5077c2e4872e6e48bd42ec165c2323aa8  xmodel/sigray-section7-weighted-euler-inequality-hostile-review-terra-20260828.md
9f4526f209366098f12bbe60387a190c6d2942a374c05fad092917bc79145f14  xmodel/sigray-multipole-selected-orbit-attachment-repair-gpt56-20260828.md
f55a00f5259d77766cc8179f3d1248ee0c1320daf411f04758487d2e94e216bb  xmodel/sigray-multipole-selected-orbit-attachment-hostile-fable5-20260828.md
3e3cea4aa6e0bda907dd291a0f1e62e1ffa744e84463e5596c2e0e0e408a166b  xmodel/m2-exit-safe-floor-legacy-reprice-r1-stable-hostile-rereview-opus5-20260829b.md
aaa7496bd6182bd124935b8534307ad3167fffe9393efad3e56cf349942ddeb7  xmodel/m2-exit-safe-floor-legacy-reprice-r1-sol56-20260829.md
205e7f5825604e0e334d1a822b13a595dfe6b9ce06d0f011b199a0ddcb725a1e  cases/landing_ledger_ll1_r3_20260829/out/ll1_book.json
1ae50f7925de2d63a718b48ab892c78a3313e4a505b8faf7385853d591c58840  ladder/BOOK-OFFAXIS.md
93adb7acedf4cf0fd56ffc68e4571649a04eab12e1271431449a79465a964bcb  ladder/SHEET6-MULTIPOLE.md
d7d0038c5fd1a3522b2908a598d99c23c64e85ec81d1280f1c7ec686c6c8ab2f  ladder/SHEET6-2POLE.md
```

18/18 match. Fail-closed condition not triggered.

---

Final disposition:

```text
Part A  physical flag tree (A.1-A.4)                     PROVED
Part B  direction-orbit interface (B.1-B.4)              PROVED; countermodel REFUTED
        (violates Definition 3.3(ii) read with Def 3.2 + St 3.2(ii))
Part C  full actual exit consumer (C.1-C.5)              PROVED at floor scope
overall                                                  PROVED_FULL_TWO_POLE_ATTACHMENT
attainment                                               NOT CLAIMED
```

<!-- END-SEALED-BODY::m2-two-pole-full-exit-attachment-primary-opus5-76c-20260829 -->

## Seal (outside the sealed body)

Convention: the sealed body is the byte range from the first byte of this file
through and including the newline that terminates the unique end-marker line
`<!-- END-SEALED-BODY::m2-two-pole-full-exit-attachment-primary-opus5-76c-20260829 -->`.
That marker occurs exactly once. Everything in this section lies outside the
sealed body and is excluded from the hash. Neighbouring cuts are given so the
convention is pinned rather than guessed.

```text
sealed-body bytes      61389
sealed-body SHA-256    2fe6a14ca8a04033d176547704de20ccd7d1c7e5dd19599970dffab3a60cbe18
  cut at 61388 bytes  2058f458a19192e46da026d4445adf302d69920127b29b0c9708f460158ea54e
  cut at 61390 bytes  25f124d788ad3cf606b59289e5e182c93f2a06510fc8e8b62f6f138ec6422275
```

Basis commit `76c746f698103d20019bfeb72654a361ccc5371d`; frozen 18-file
perimeter verified before and after (§1.2, §10), 18/18 OK both times.
