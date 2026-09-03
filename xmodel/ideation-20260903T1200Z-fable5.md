# Ideation round 20260903T1200Z — blind submission — Fable 5 (claude-fable-5-1)

Lane `ideation-20260903T1200Z-fable5`. Packet `/tmp/jc2-lane.3gfRWX/inputs/ideation-20260903T1200Z-packet.md`
verified before any read: SHA-256 `c90fa6876b069478f658845be6efa2bd056b2e340af7284104af4d042e6c4f95` (MATCH).
Basis 4250a6e4. Blind: no `ideation-20260903T1200Z-*` submission opened; the reports of the
running lanes (sibling-coefficients-sol56, screened-census-grok46, whole-tree-review-opus5,
appendix2-compiler-grok46) not opened (their `.run.v2` have no `final_status`); no canonical
ledger edited; `jc2-lean` not inspected. A post-freeze lane directory `box/prop55k-drivers-20260903/`
and prompt `xmodel/prop55k-opus5-20260903.prompt.md` (12:08Z) exist; I opened NEITHER — its tag
suggests overlap with §4 below, flagged for the coordinator's deduplication.

**Sources read.** The packet; AUDIT deltas 17(p)–(t) (AUDIT.md:15840–16081); notes.md LIVE STATE /
EVENT blocks 08:33Z–12:00Z; COORDINATION.md §Full-spectrum; APPROACHES.md (46 rows + overlays);
sealed reports `whole-tree-review-grok46`, `moh-program-review-sol56`, `m2-descent-opus5`,
`descent-radii-grok46`, `ps-growth-opus5`, `next-coeff-psreview-grok46` (§1), `a2six-ray-moment-sol56`,
the 1015Z synthesis and coordinator note, my own 1015Z submission; the prompts of the running lanes.
**Moh 1983 pages opened as images this lane:** journal pp.189–190 (PDF 50–51, `pdftoppm -r 130`).
Everything cited from those two pages is SOURCE-READ; other Moh citations are via the sealed reports.

**Computation (desk, < 1 min, one core, < 100 MB).** Two python probes importing the tracked
`box/moh_skeleton_full.py` and `box/mohprog-drivers-20260903/full_tree_partition.py` (scripts in §13):
(i) the homothety family of Moh's six rows through C_FULL_TREE / C_FULL_TREE_ODE; (ii) the structure of the
52 excess C_FULL_TREE_ODE rows and the 14 POLY+ODE rows from the frozen witness JSONs.

## 0. Headline — direct answers, then the argument

1. **The coordinator's framing ("boundary → N; tree → multiplicities; coefficients → the rest") is right
   about the three layers and wrong about where the tree ends.** Two skeleton-level facts are still on the
   table, both cheap, both measured here:
   * **OPEN[FULL-TREE-RECENTER] should close POSITIVE** (PROVED-HERE/UNREVIEWED, §2.1). The only integral
     radius available to an intermediate disc is δ_j = 0; a nonzero label there is the constant term of the
     root, removable by `y ↦ y − c`, which is exactly Moh's p.190 move (`y ↦ y − ax − b`, SOURCE-READ) and
     preserves his gauge and the tower. The p.189 proof of Prop 5.6 (SOURCE-READ) uses only (a) a pure
     `x^l` term of `g` at the bottom general point, (b) the order balance of Prop 4.1(1) at σ₁, (c)
     δ₁ ≥ δ_{s−1} ≥ 0 — all three chart-covariant under that affine change. MEASURED: exactly 38 of the 52
     excess C_FULL_TREE_ODE rows at n ≤ 100 carry a δ = 0 nonzero selected edge, and they are exactly the
     38 the POLY rule kills (0 mismatches). Operative residue at n ≤ 100 becomes **14 rows in three
     classes (90,60), (96,64), (96,72), all s ≥ 4, all u_s = 1**; on the campaign space the POLY+ODE
     column already measured by Sol (1,420 / 686 / 459 at D ≤ 200; D ∈ {72, 80, 100, 176} additionally
     empty) becomes operative. D = 108 keeps survivors: the frontier does not move.
   * **At s = 3 the screen is EXACT.** All 52 excess rows have s ∈ {4 (37), 5 (15)}; the six s = 3
     survivors of C_FULL_TREE_ODE at n ≤ 100 are Moh's six. OPEN[MOH-PROGRAM-ARTIFACT] is therefore a
     statement about s ≥ 4 only, and after recentring about 14 rows that all descend (u_s = 1).
2. **Q1.** The screened space is not emptied by any all-degree form of the j = 2 mechanism: the kill is the
   arithmetic inequality `(V₃d₂/d₃ mod A₂) > d₂/(n − M₂)` on a still-centred chart, and the complementary
   set (`A₂ | P`, or a minor forced zero) is infinite. What I can add: the homotheties of Moh's own rows
   are NOT a screened family (λ = 2..6: 0/6 classes survive except three sporadic rows with u_s ∈ {3, 5, 14}),
   so the first candidate cofinal family dies at the desk; a screened family, if any, will have u_s > 1
   or s ≥ 4. The theorem the mechanism needs beyond (1)–(13) is the whole-tree universal quantifier plus
   Prop 5.6 — already promoted; nothing further is in the tree. The proof must leave the skeleton.
3. **Q2.** The uniform coefficient statement is theorem (T) restricted to tower height ≤ 2 and, for
   u_s > 1 rows, OPEN[MINOR-DICHOTOMY]. The sibling system and the tree-decorated moment engine are the
   SAME computation (dictionary in §3); on u_s = 1 rows both are dominated by the Appendix-II compiler
   because descent divides the unknown count by d_s². Cheapest exact discriminator on the first D = 108
   survivor: descend and compile (running); build the decorated engine only for u_s > 1 survivors.
4. **Q3.** (T) at k = 0 is Moh's Prop 5.5/5.6 (s = 2 is impossible for Keller pairs — proved by arithmetic).
   The k-twisted p.189 argument does NOT kill: the balance shifts by −k and yields only
   `deg_γ P(γ, 0) ≤ k` (§4; consistent with Moh's (15,10) shapes where `g(x,0)` has x-degree ≤ 2 = k).
   That is why Appendix II needs coefficients. The right uniform target is one level lower: iterate the
   descent while the descended `u' = 1` (Moh's (16,12) row has u' = 1 and descends again to (4,3)); the
   terminal objects are height-1 monomial-Jacobian pairs = GGV's regular-corner problem (row 1).
5. **Q4.** The mechanism outside the three layers is the **pencil**: the Keller condition is invariant under
   `g ↦ g − c`, so EVERY fibre — atypical values included — carries a whole-tree-admissible skeleton with
   the same characteristic data, related by degeneration, under one global sum rule (§5.1); and the fibre
   map `f|_{g=c}` is UNRAMIFIED on the affine curve, giving a Riemann–Hurwitz identity that ties the
   fibre genus to N and the non-proper ramification (§5.2). Plus one literature cross-connection the
   ledger lacks (§5.3, SOURCE-UNVERIFIED): Kaliman 1993 / Lê–Weber 1995 — a Keller pair with a rational
   generic fibre is an automorphism — which would close OPEN[MF-RATIONAL] negative.
6. **Single first lane:** `RECENTER-GATE` (Opus or Sol, 60 min, page images): certify §2.1 from pp.183–190,
   promote the POLY column, and hand the 14-row residue to the compiler. Reason: it is the only item this
   round that moves the operative census by a factor two at the price of two pages.

## 1. Two desk facts (MEASURED, reproducible from §13)

**1.1 The 52 excess rows.** `full-tree-ode-excess-witnesses.json` (52 rows = 58 − Moh's six):

```text
u_s = d_s − V_s :  {1: 52}          s : {4: 37, 5: 15}
δ_j at intermediate levels j ≥ 3 on the selected chain:
   '0': 38,  '1/7': 5, '1/5': 4, '17/44': 3, '3/10': 3, '8/35': 2, '17/35': 2, '5/11': 2,
   '1/4': 2, '3/11': 2, '9/28': 1, '25/77': 1, '5/17': 1, '9/29': 1
rows with a δ = 0 NONZERO selected edge: 38   rows killed by the POLY (recentre) rule: 38   mismatch: 0
```

The 14 POLY+ODE survivors (`full-tree-polynomial-ode-excess-witnesses.json`), selected chain
`(level, δ, label)`: (90,60;10,45,88;V=1,8,4) and (3,8,4): `(3,8/35,zero),(2,5/21,nonzero)`;
(90,60;45,80,88;2,5,4) and (3,5,4): `(3,1/7,zero),(2,5/14,nonzero)`; (96,64;−48,−8,20,94;1,1,6,3):
`(4,9/28,zero),(3,25/77,zero),(2,5/14,nonzero)`; (96,64;48,68,94;1,2,3),(3,2,3): `(3,3/10,zero),(2,2/5,nonzero)`;
(96,64;48,68,94;2,1,3): `(3,3/10,nonzero),(2,11/20,zero)`; (96,72;−60,56,94;1,9,3): `(3,9/29,zero),(2,19/58,nonzero)`;
(96,72;36,78,94;1,1,5): `(3,1/7,nonzero),(2,9/14,nonzero)`; (36,78,94;1,3,5),(4,3,5): `(3,1/7,zero),(2,2/7,nonzero)`;
(96,72;36,80,94;1,9,3),(4,9,3): `(3,3/11,zero),(2,7/22,nonzero)`. Every intermediate radius is a
non-integer: no affine move reaches them. All 14 have u_s = 1.

Consequences. (a) At s = 3, C_FULL_TREE_ODE ∩ {n ≤ 100} = Moh's table (6/6, 0 excess). (b) The entire
effect of the exploratory recentring at n ≤ 100 is the δ = 0 case. (c) Every excess row, before or
after recentring, is in Prop 6.3/6.4's domain.

**1.2 Homotheties of Moh's rows are not a screened family.** For each printed row scale
`(n, m, M₂) ↦ λ(n, m, M₂)`, keep `M₃ = n − 2`, enumerate all (1)–(13) V-assignments at s = 3, apply the
tree screens (`full_tree_ok`, `full_tree_ode_ok`; control at λ = 1: all six printed rows survive):

```text
class (n0,m0,M2)   λ=1 rows/TREE/ODE   λ=2   λ=3   λ=4   λ=5   λ=6      ODE survivors (V2,V3,u_s,P mod A2,h)
(64,48,52)         1/1/1              0/0/0 1/0/0 0/0/0 0/0/0 3/1/1     λ=6: (3,19,5,0,4/3)
(84,56,64)         1/1/1              2/0/0 3/0/0 5/0/0 6/0/0 6/0/0     —
(84,56,72)         2/1/1              2/1/1 1/0/0 4/0/0 2/0/0 5/2/2     λ=2: (5,5,3,0,7/3); λ=6: (5,19,5,1,7/3),(13,19,5,1,7/3)
(75,50,55)         2/2/2              0/0/0 0/0/0 7/0/0 5/0/0 1/0/0     —
(99,66,77)         2/1/1              4/0/0 0/0/0 0/0/0 4/1/1 6/0/0     λ=5: (8,41,14,0,3/2)
```

Reading: the printed rows do not propagate by scaling; the sporadic survivors have u_s ∈ {3, 5, 14}
(outside Prop 6.4) and appear at λ where `d_{s+1} = gcd(d_s, n − 2) = 1`. If a screened cofinal family
exists it is not the obvious one, and its members will need OPEN[MINOR-DICHOTOMY], not the descent.
(The running screened-census lane will settle cofinality to D ≤ 400; this table is a negative control
for its family search, not a substitute.)

## 2. Q1 — the screened census as a proof program

**2.1 OPEN[FULL-TREE-RECENTER] closes positive (PROVED-HERE/UNREVIEWED; two-page check).**
Setting: a whole-tree sibling path from the Lemma 5.3 top chart down to a bottom major disc D₁, all
labels zero except one nonzero label `c` at a level j with δ_j = 0 (radii are strictly increasing down
the tower, so at most one level has δ_j = 0, and δ = −1 occurs only at the top). The bottom general
point in the current chart is σ₁ = c + π t^{δ₁}.
Claim: Prop 5.6 kills this path. Proof sketch. Apply `α: y ↦ y − c` (Moh's p.190 form with a = 0,
SOURCE-READ). α preserves Moh's gauge (monic in y, deg = deg_y, degrees, J), and the tower of
(f∘α, g∘α) is the translated tower with the same radii, root counts and multiplicities (Def 5.1(1)–(3)
are intrinsic; the term c t⁰ lies strictly inside every disc of radius < 0 above level j and is the
label at level j itself). In the new chart the path is zero-typed: σ₁ = π t^{δ₁}. The p.189 proof
(SOURCE-READ) then runs verbatim: (i) g∘α and T₁^ψ∘α are coprime, so `y ∤ (g∘α) + c₂` for all constants,
hence g∘α has a pure `x^l` term, l ≥ 1, and `ord g(σ₁) = nλ ≤ −l`; (ii) the Prop 4.1(1) balance
`nλ + (−M₁)λ − 1 = −2 + δ₁`; (iii) δ₁ ≥ δ_{s−1} ≥ 0; whence l = 1 and δ₁ ≤ (−M₁)λ < 0, contradiction.
Nothing in (i)–(iii) refers to any sibling other than the killing path, so the reviewers' worry ("the
automorphism must centre every sibling chart") does not arise: a kill needs one centred path, and
different killing paths may use different constants. What the edgewise rule must NOT do is treat a
nonzero label at a non-integral radius as removable (a term c t^{δ}, δ ∉ Z, survives every polynomial
change); the frozen POLY implementation applies the rule only at integral δ (MEASURED: its 38 kills
are exactly the δ = 0 rows). Cheapest gate: a different-model reader checks that Prop 4.1(1)'s balance
and Lemma 5.3's chart are chart-covariant under y ↦ y − c (pp.164–166, 185–186 — pages I did not open);
30 minutes. Bounded effect: 58 → 20 rows at n ≤ 100; D ≤ 200: 2,824/1,384/865 → 1,420/686/459 (Sol's
already-measured POLY+ODE column); emptied degrees gain {72, 80, 100, 176}.

**2.2 The j = 2 mechanism has no all-degree form beyond what is promoted.** On a still-centred chart at
s = 3 the kill is `b_min := V₃d₂/d₃ mod A₂ > d₂/(n − M₂)`; survival is the complementary arithmetic
condition and it is satisfied by Moh's six (b_min = 0, 0, 1 ≤ 7/3, 0, 0, 0) and by infinitely many
tuples (there is no monotonicity in D). Turning it into a theorem "for all D" is exactly asking the
screened census to be finite, which the counts (1,516 groups at D ≤ 200, growing) refute. What the
mechanism needs beyond (1)–(13) is precisely: the universal quantifier over siblings (Prop 5.3, p.200(4)),
the Galois orbit structure (p.201), the top-chart danger flag (Lemma 5.3), Prop 5.6 — all promoted —
plus §2.1. There is no further skeleton-level source theorem: §6's scalars are automatic (Sol §3.4),
Prop 5.4 acts only at the globally selected disc, which is D_s by the window `d_s > V_s`.

**2.3 The screened family, if it exists, is a MINOR-DICHOTOMY family.** All 52 excess rows at n ≤ 100
have u_s = 1; the sporadic homothety survivors have u_s ≥ 3. My expectation for the census lane: the
screened space stays nonempty, dominated at large D by rows with u_s > 1 or s ≥ 4. Hence the
counterexample-side target list above D = 100 splits by u_s: u_s = 1 rows go to the compiler; u_s > 1
rows have no exact discriminator yet — OPEN[MINOR-DICHOTOMY] is the bottleneck for them (§7).

## 3. Q2 — the coefficient level in uniform form

**3.1 The dictionary node ↔ datum.** The moment engine's decorated skeleton (delta 17(l): rooted tree on
the n leaves, cyclic action, truncated series per leaf, sharing declarations, exponent support) is
supplied by the whole tree as follows.

| engine datum | whole-tree object |
|---|---|
| leaf i | a root τ_i of g − c; its disc chain D_s ⊃ … ⊃ D_j(i) |
| internal vertex, contact ord | major disc D_j with radius δ_j (Def 5.1(3)); minor disc D*_j with radius ≥ 1 (Prop 6.1) |
| cyclic action on leaves | `t̄ ↦ ω t̄` of order A_j at level j (p.201); nonzero factors of p_j in orbits of size A_j, one fixed root |
| truncated series τ_i(z) up to the bottom | the labels along the path: at each level the factor `π − c_j` of p_j (c_j = 0 or an A_j-orbit), i.e. `σ₁ = Σ_j c_j t^{δ_j} + π t^{δ₁}` |
| sharing declarations | descendants of D_j share the outer series of D_j; different orbits are not identified (a2six §3.3) |
| bottom star | (p₁, q₁) at D₁, Davenport–Stothers by STAR-ABC; fixed by (d, e, V₂) up to scaling |
| exponent support / tame coefficients | NOT in the tree: the coefficients of q_j at non-root slots, the minor discs' internal tree below radius 1, and every non-characteristic (tame) coefficient |

So the tree supplies exactly the decoration the engine could not synthesise (d105-rank-gate, fixed-n6,
a2six all stopped at "the decoration is not determined"), and the sibling-coefficient problem (two
adjacent nodes, ODE at both, Galois symmetry, matching leading terms) is the engine restricted to one
edge of the tree. They are one computation, not two.

**3.2 Which is cheapest on the first D = 108 survivor.** For u_s = 1 rows the answer is neither: Prop 6.3
divides the number of coefficients by d_s² ≥ 16 and turns the Jacobian into a monomial, after which
Moh's shape reduction (now automatable via Φ) leaves Appendix-II-sized systems (Moh: 10–22 unknowns;
G2: 42). The compiler lane is doing this. The decorated engine at degree 108 would carry 108 leaves and
the quadratic lift Sol priced at > 4·10⁵ variables for D = 54 — build it only for u_s > 1 survivors,
where the descent does not apply, and only after MINOR-DICHOTOMY names the two alternatives.

**3.3 Is the uniform form theorem (T)?** Yes for u_s = 1, with one correction to its scope: (T) as
stated in delta 17(q) is a statement about height-2 pairs, but Moh's descended rows can descend AGAIN
when the descended `u' = d₂' − V₂' = 1` ((16,12): d₂' = 4, V₂' = 3). The finite reduction ends at
height 1, not 2 (§4.3). So the uniform coefficient theorem is: **(T₁) no monomial-Jacobian pair of
tower height 1 with the inherited data**, plus the height-2 statement only where `u' > 1`.

## 4. Q3 — attacking (T)

**4.1 What is known: (T) at k = 0 is Moh's Prop 5.5.** For a Keller pair, s = 2 is impossible: Prop 5.4
forces `M₂ = n − 2, δ₂ = −1, d₂ > V₂ > d₂/2`, the bottom coprimality gives (12)/(13), and the
s = 2 radius `δ₁ = [(n*+m*)U₂ − 1]/[(n*+m*)V₂ − 1]` produces the chain `V₂ > V₂ − U₂ = C(D+E) ≥ D ≥ V₂`
(Sol §3.2, SOURCE-READ by that lane). This is an arithmetic proof of a coefficient-free statement.

**4.2 The k-twist of p.189 does not kill; it bounds `deg_γ P(γ,0)`.** Redo Prop 5.6's proof for a descended
pair (P, Q) with `J = cγ^k`, `ord_t γ^k = −k` in Moh's `t = x⁻¹` (the descended pair reuses (x, y) for
(γ, π)): the Prop 4.1(1) balance becomes `nλ + (−M₁)λ − 1 = −2 − k + δ₁` (CONJECTURE: the shift is the
only change, by the Lemma-2.1 dictionary `1 ↦ k + 1` that the rule Φ already confirmed on ten
rationals). With `ord g(σ₁) = nλ ≤ −l` and `(−M₁)λ < 0`: `−l ≥ nλ > −1 − k`, i.e. **`l ≤ k`**; at
k = 0 this forces l = 1 and the contradiction; at k ≥ 1 it only says that the pure-x part `P(γ, 0)`
of the descended top polynomial has degree ≤ k. MEASURED consistency on Moh's (15,10; X²) shapes
(5)–(6): `h(x,0) = a₈`, `A(x,0) = a₆x + a₇`, `B(x,0) = a₄x + a₅`, so `g(x,0) = a₈³ + 3a₈β(x,0) + (3/2)α(x,0)`
has x-degree ≤ 2 = k. So the twisted arithmetic is a NECESSARY shape condition on descended pairs
(`deg_x P(x,0) ≤ k` — cheap to add to the compiler's shape rule; bounded test: it must hold on Moh's
five descended rows and on the 42-unknown G2 normal form), not a kill. That is the structural reason
Appendix II needs coefficient equations: the window `l ≤ k` is open exactly when k ≥ 1.

**4.3 Iterate the descent to height 1.** The descended pair has s' = 2 with top datum (d₂', V₂', u' = d₂' − V₂');
when u' = 1 the k-twisted Prop 6.4 gives `δ*' ≥ v'` and Prop 6.3 applies again (its hypotheses — monic,
deg = deg_y, δ_top = −1, minor radius ≥ v/u — are gauge facts, but Prop 6.4's proof must be re-read for
J = cγ^k: OPEN[TWISTED-64], bounded: one page (p.198), cheapest test: apply the descent formally to
Moh's (16,12; X) row and check the (4,3) result against Moh's p.208–209 ten-coefficient reduction, which
is exactly a (4,3)-sized computation). At height 1 the pair is "almost a (d,e)-power pair": there is H
with `deg_π H = K'` and `P ≈ H^{e}`, `Q ≈ H^{d}` to order n'' − 2 in the mutual expansion, and
`J(P,Q) = cγ^{k''}`. That is the regular-corner problem of GGV (row 1): the leading forms at the
corner are powers of one polynomial and the Jacobian is a monomial. The campaign owns certificates for
corner families; the bridge test is unchanged from my 1015Z card: descend Moh's (75,50) row to
(15,10; X²) and ask the row-1 engine — Moh says empty (pp.210–211, reproduced SATURATED-EMPTY).

**4.4 Uniform obstruction in (n', m', M₂', V₂')?** Not from arithmetic alone: the descended data of Moh's
five rows pass every twisted numerical condition (they are Moh's own survivors) and die only by
coefficients. The only uniform statement I can offer with a proof route is the height-1 one (§4.3):
a height-1 monomial-Jacobian pair with `e ≥ 2` and `d ∤ e`... is a two-variable Davenport–Stothers
problem, and here the campaign's own STAR-ABC/BOTTOM-ODE theory applies at the (single) bottom level
with the dessin-tower count `max(k − 2, 0)`: at height 1 the tower has k = number of bottom discs,
and the expected dimension of the corresponding Hurwitz problem is `k − 2`; a rigid case (k ≤ 2)
is decided by one Belyi computation. This is where the DESSIN-TOWER lane's "19 rigid candidates" and
the descent meet: descend those 19 and see whether they land at height 1 with k ≤ 2.

## 5. Q4 — fresh eyes: the pencil, unramified fibre maps, and one missing theorem

**5.1 The pencil of trees (NEW mechanism, skeleton-external).** Moh's tower is built for the fibre
g = 0; the Keller condition is invariant under `g ↦ g − c`. Therefore for EVERY c the fibre {g = c}
carries a whole-tree-admissible skeleton with the same (n, m, M_i, d_i) (the characteristic data are
read from `f` in powers of `(g − c)^{−1/n} = η(1 + O(η^n))`, unchanged below order n − m, i.e. for
all M_i < n − m; above that they may move — a bounded quantity: which of the M_i ≥ n − m can change
with c). At an atypical value c_j the tree degenerates (roots collide at infinity), and the Euler
characteristic of A² forces the global sum rule `Σ_j λ_j = 2g_gen + r_gen − 1` (λ_j = Milnor number at
infinity of the fibre over c_j; all fibres are smooth since ∇g ≠ 0). So a skeleton must be
COMPLETABLE TO A PENCIL: a generic tree T_gen and finitely many degenerate trees T_j, each
whole-tree admissible, whose degeneration data satisfy the sum rule. This is a necessary condition
that no single tree sees. Bounded quantity: for a given screened survivor, the number of admissible
pencil completions (0 kills). Cheapest test: on Moh's (64,48) row, enumerate the degenerate skeletons
(same n, m, M₁; M₂, M₃ allowed to move only if ≥ n − m; V's arbitrary) that pass C_FULL_TREE, compute
λ from the tree difference, and check whether any subset sums to 2g_gen + r_gen − 1 — needs g_gen,
which needs the minor-disc contact tree (OPEN[NONPROPER-TREE]); so run it first on a control where
the pair is explicit (a composition of two elementary automorphisms in Moh's gauge) to see the sum
rule hold, then on Moh's row with the minor tree bracketed.

**5.2 Riemann–Hurwitz for `f` on a fibre (PROVED-HERE, one line, probably known in another dress).**
On the smooth affine curve C_c = {g = c} the Gelfand–Leray form `ω = dx/g_y = −dy/g_x` is nowhere
vanishing and, by J = 1, equals `df|_{C_c}`. Hence `f|_{C_c}: C_c → A¹` is UNRAMIFIED on the affine
curve, of degree N, and the compactified map `\bar C_c → P¹` is branched only over ∞ and over the finite
escape values a₀ of the non-proper places. Riemann–Hurwitz with `Σ_{proper} e_P = N`:

```text
   2 g_c − 2 + N + r_prop = Σ_{P non-proper} (e_P − 1),      e_P = ord_P (f − a₀(P)).
```

Read: (i) with N ≥ 6 the right side is ≥ 5 + r_prop: there must be non-proper places where `f − a₀`
vanishes to order ≥ 2 — a floor on the non-proper block that the moment lanes treated as free;
(ii) if a Keller pair had ONE escape value per fibre (σ = 1, branched over two points) the cover
would be cyclic, C_c ≅ G_m and g would be a C*-fibration — excluded for coordinates-with-mate by
the classification of C*-polynomials (e.g. `g = x²y + x` has the rational mate `−y/(1 + xy)`; no
polynomial mate). So every fibre of a counterexample has ≥ 2 escape values, i.e. A(Φ) meets every
horizontal line in ≥ 2 points. Bounded: r_np and the e_P per fibre; cheapest test: evaluate the identity
on Sol's explicit branch data for the D = 105 group A (dead, but the data exist) and on the
composition control (must hold with g_c = 0, N = 1). Relation to the ledger: AUDIT:11147 has the
signed adjunction identity `Δ_inf − K_inf = 2 − 2g_C − s`; MF-DEFECT has `2g_L + θ_inf ≥ 2`. The
unramified-ness of `f|_{C_c}` and the branched-over-escape-values reading are, as far as I can see,
not written down; they make the fibre a Belyi-type cover of the f-line branched at A(Φ) ∩ {g = c} ∪ {∞}.

**5.3 A missing theorem (SOURCE-UNVERIFIED, from memory; not in AUDIT/notes/APPROACHES by grep).**
Kaliman, "On the Jacobian conjecture", Proc. AMS 117 (1993) 45–51, and Lê Dũng Tráng–C. Weber,
"Polynômes à fibres rationnelles et conjecture jacobienne à 2 variables", C. R. Acad. Sci. Paris 320
(1995) 581–584: a Keller pair one of whose members has rational generic fibre is an automorphism.
If confirmed, OPEN[MF-RATIONAL] ("can g_L = 0 at all") closes NEGATIVE for counterexamples, and
`g_c ≥ 1` joins the necessary conditions — with §5.2 that gives `Σ_np (e_P − 1) ≥ N + r_prop`.
Cheapest test: the web-sweep lane fetches the two abstracts (10 minutes); then `g_c` from the tree
becomes a kill whenever the minor tree forces genus 0 (the maximal-contact completion of the
minor discs gives the minimal genus; if that minimum is ≥ 1 the row is safe, if 0 the completion is
dead — a partial screen, cheap once OPEN[NONPROPER-TREE] is bracketed).

**5.4 Say it plainly.** The proof, along Moh's line, must be a coefficient computation — but at tower
height 1, on monomial-Jacobian pairs, where "coefficient computation" means Davenport–Stothers /
GGV-corner algebra in two variables, and where the campaign's boundary theory (STAR-ABC,
BOTTOM-ODE) already lives. The tree's job is finished once §2.1 is promoted. The counterexample side
should NOT interpolate at degree 108: it should descend, and where it cannot (u_s > 1) it should
first state MINOR-DICHOTOMY. The pencil (§5.1) and the unramified fibre map (§5.2) are the two
skeleton-external mechanisms I can name with a test; neither is a proof route by itself.

## 6. Disposition vectors

**6.1 APPROACHES.md rows (changes only).**
* Row 1 (GGV corner families, [P,Q] = x^k): **RAISE** further — it is the terminal receiver of the descent
  at tower height 1 (§4.3); charge the bridge test (Moh (75,50) → (15,10; X²) → row-1 engine).
* Row 2 (boundary trees): **RETYPE** — closed as a ceiling; its live content is the pencil-of-trees
  completion (§5.1) and the genus/RH bookkeeping (§5.2).
* Row 5 (JvdK descent): **RETYPE → "monomial-Jacobian descent, iterated"**; depth ≤ s − 1, terminal at height 1.
* Row 6 (Abhyankar–Moh one-place): **unchanged (raised last round)**; the twisted Lemma 2.1 is its content.
* Row 7 (Jelonek A(Φ)): **RAISE (mildly)** — §5.2 makes A(Φ) ∩ {g = c} the branch locus of f|_{C_c};
  its degree per fibre (≥ 2) is a computable invariant of the non-proper block.
* Row 12 / 25 / 26 (monodromy, dessins, primitive groups): **RETYPE** — the fibre cover is branched only
  at escape values and ∞ (§5.2); the dessin-tower dimension is the height-1 residue (§4.4), not a global route.
* Row 16 / 45 (D-module, differential Galois): **LOWER** — ps-growth closed the trace route as a ceiling;
  no dissent left on my side.
* Row 20 (char p): unchanged (diagnostic).
* Row 29 (LND / Gauss–Manin κ(P)): unchanged — same statement as "[dx∧dy] = 0 in the Brieskorn module".
* Row 36 (guided CE search): **RETARGET** to height-1 monomial-Jacobian pairs of the descended D = 108 data.
* Row 28 (log surfaces / BMY): **RAISE one notch** only if §5.3 confirms (genus ≥ 1 fibres feed log-Kodaira).
* All other rows: unchanged.

**6.2 Q1–Q4 candidates.** Screened census as proof program: **NO** (Q1; §2.2). Cofinal screened family:
**expected nonempty, with u_s > 1** (§2.3). Uniform j = 2 theorem: **NO beyond the promoted set + §2.1**.
Theorem (T): **RAISE, restated at height 1 (T₁)**; tree-decorated moment engine: **LOWER for u_s = 1 rows,
keep for u_s > 1**; sibling-coefficient theorem: **same object as the engine; keep the lane, expect
COUNTING-BOUND on (90,60), a verdict only after descent**. Mechanism outside the three: **pencil of trees
(§5.1), unramified fibre map (§5.2), rational-fibre theorem (§5.3)**. Char-p, D-module, dessin-as-proof:
unchanged LOWER.

**6.3 Queued fronts.** Tree-decorated moment engine: **REDESIGN** — restrict to u_s > 1 screened
survivors; use the §3.1 dictionary; do not build for u_s = 1. P202 residue through the sibling system:
**REDESIGN** — after §2.1 the residue is 14 rows, all u_s = 1: send them to the compiler, not the sibling
system. Box01 restart for heavy Gröbner: **HOLD** until a compiler system exceeds 30 unknowns on a
D = 108 survivor; nothing this round needs it.

## 7. Bottlenecks reranked

Proof side: (P1) OPEN[FULL-TREE-RECENTER] → promote (§2.1; one gate, 30 min); (P2) OPEN[MINOR-DICHOTOMY]
in uniform form — every screened family and every sporadic large-D survivor found here has u_s > 1;
(P3) (T₁): the height-1 monomial-Jacobian problem as a theorem (Davenport–Stothers in two variables with
the descended data); (P4) OPEN[TWISTED-64] (Prop 6.4 for J = cγ^k, one page) so the descent iterates;
(P5) the pencil completion (§5.1), a new necessary condition, cost gated by OPEN[NONPROPER-TREE].
Disproof side: (C1) a SURVIVES on a descended height-1 system of a D = 108 u_s = 1 survivor (the
compiler; then OPEN[DESCENT-LIFT]); (C2) a u_s > 1 screened survivor with an explicit MINOR-DICHOTOMY
branch that descends to a small existing pair; (C3) nothing else above D = 100 is cheaper than these.

## 8. Required singles

**New avenue — PENCIL-COMPLETION (§5.1).** Target obstruction: the residual freedom after the tree.
Mechanism: `g ↦ g − c` invariance + the Euler-characteristic sum rule over atypical values. Object: the
finite family of degenerate whole-tree skeletons of one pair. Decisive test: enumerate admissible
degenerate trees for Moh's (64,48) and check the sum rule; a control on an explicit tame composition.
Bounded quantity: number of admissible pencil completions per survivor (0 = kill).

**New cross-connection — the fibre map `f|_{g=c}` is unramified (§5.2) ⇔ NO-RESIDUE + JAC-FIBRE read
globally.** It identifies the moment engine's non-proper block with the branch data of a Belyi-type
cover of the f-line whose branch points are A(Φ) ∩ {g = c} (row 7 ↔ rows 25/26 ↔ the global
interpolation framework). Second cross-connection: §5.3 (Kaliman / Lê–Weber) ↔ OPEN[MF-RATIONAL] ↔ the
minimal-genus completion of the minor tree.

**Strongest proof attack.** Promote §2.1; iterate the descent to height 1 (§4.3, OPEN[TWISTED-64]);
prove (T₁) by the two-variable Davenport–Stothers argument: at height 1 the whole tree is one top disc
and k bottom stars, every star is ABC-extremal (STAR-ABC), the Galois action of order A₁' glues them,
and the monomial Jacobian imposes `deg_x P(x,0) ≤ k` (§4.2) plus the twisted Lemma 2.1 pattern; the
count of free parameters is the dessin-tower number `max(k − 2, 0)` against the `k + 1`-many coefficient
conditions of `deg_x g_{m'−1} = k + 1` and the vanishing pattern of M₂'. Where the count is ≤ 0 the
statement is a finite Belyi computation per (d, e, k).

**Strongest counterexample attack.** Take the first screened D = 108 survivor with u_s = 1 (the census
lane will name it); descend; iterate the descent if `u' = 1`; solve the terminal system exactly with a
planted-automorphism positive control (descend a tame automorphism in Moh's gauge with u_s = 1 — the
compiler lane was asked whether one exists in the autoscan population; if none, construct one by
composing `(y, x + y^a)` with `(x + y^b, y)` and put it in the gauge). A SURVIVES with a positive-
dimensional family is the first honest signal above D = 100; its lift is OPEN[DESCENT-LIFT].

**Decisive experiment / software acceleration.** `RECENTER-GATE` + switch the operative screen to
POLY+ODE (both drivers exist: `full_tree_polynomial_ode_ok`); rerun the census lane's D ≤ 400 pass
with that column as primary. Cost: one 30-minute source check and a flag flip; effect: the operative
census halves (1,384 → 686 groups at D ≤ 200), four more degrees empty, the n ≤ 100 residue becomes
14 rows in three classes, and every one of them is a compiler client.

## 9. Campaign-systems check — UPGRADE (claim/review propagation)

Evidence: the whole-tree review typed the recentring OPEN with a bounded effect of 35 rows and the
note "cheapest test already done"; a two-page covariance check (this lane, 20 minutes) suggests it
closes positive. The same pattern produced PROP-5.6-SHADOW and MAJOR-MULT last round. Smallest useful
implementation: extend the adopted "cheapest test" rule with a **"positive-closure attempt"** field —
when a reviewer types an item OPEN with a source-page cheapest test under one hour, the coordinator
launches that attempt as a 45-minute micro-lane BEFORE the next packet freeze, and the packet lists the
attempt's verdict. Test: apply it to OPEN[FULL-TREE-RECENTER] and OPEN[TWISTED-64] this round; success
metric: both typed (closed or refuted) before the 22:38Z floor.

## 10. Idea cards (three)

**CARD A — RECENTER-GATE (promote §2.1).** Dependencies: pp.164–166 (Prop 4.1), 183–186 (Prop 5.4,
Lemma 5.3), 188–190 (Prop 5.6) as images; the frozen POLY drivers. Discriminator: is every quantity used
in the p.189 proof invariant under `y ↦ y − c`, and is the label at a δ_j = 0 level the constant term of
the root? Outcomes: YES → promote C_FULL_TREE_POLYNOMIAL_ODE as the operative screen (58 → 20;
1,384 → 686 groups at D ≤ 200); NO with a named non-covariant step → the rule stays OPEN and the step
is the new bounded object. Stop: 60 minutes. Gain: highest per minute this round.

**CARD B — DESCENT-ITERATE + (T₁).** Dependencies: descent-radii Φ (promoted), OPEN[TWISTED-64] (p.198
for J = cγ^k), the compiler's shape rule. Discriminator: on Moh's (16,12; X) descended row, does the
second descent reproduce the (4,3)-sized ten-coefficient system of pp.208–209? Outcomes: YES → the
finite reduction terminates at height 1 and (T₁) is the uniform target (row 1 receiver); NO → (T) stays
at height 2 and Appendix II's two-root computation is the template. Stop: half a day. Gain: high —
it fixes the shape of the theorem the campaign must prove.

**CARD C — PENCIL-COMPLETION (§5.1) with the RH identity (§5.2) as the control.** Dependencies: the
whole-tree DP; a bracketing of the minor-disc tree (Prop 6.1's radius ≥ 1 bound); one explicit tame
composition as a control. Discriminator: does the sum rule `Σλ_j = 2g_gen + r_gen − 1` admit a
completion by admissible degenerate trees for Moh's (64,48) row? Outcomes: no completion → a new
uniform necessary condition, run it over the screened census; completions exist → the pencil adds
nothing at the skeleton level and the card closes. Stop: one day. Gain: moderate; it is the only
skeleton-external mechanism with a finite test.

## 11. Lanes — continue / redesign / stop; the single first lane

* sibling-coefficients-sol56: **CONTINUE to seal**, then RETYPE its (90,60) verdict as a one-edge
  instance of the decorated engine; do not relaunch on u_s = 1 rows.
* screened-census-grok46: **CONTINUE**; add the POLY+ODE column as a candidate operative column and
  the u_s distribution of every survivor (this lane's prediction: the large-D survivors have u_s > 1).
* descent-radii-grok46: sealed; no action.
* a2six-ray-moment-sol56: sealed; **STOP** the moment-engine programme on dead rays.
* whole-tree-review-opus5: **CONTINUE** (second gate); ask it to rule on §2.1 explicitly if still open.
* appendix2-compiler-grok46: **CONTINUE**; add the `deg_x P(x,0) ≤ k` shape check (§4.2) as a
  fail-closed gate (must hold on Moh's five) and record whether any descended row has `u' = 1`.
* Queued decorated engine: **REDESIGN** (u_s > 1 only). Queued P202-residue-through-sibling-system:
  **REDESIGN** (send the 14 to the compiler). Box01: **HOLD**.
* Web sweep: add two queries — Kaliman 1993 PAMS 117 and Lê–Weber 1995 CRAS 320 (§5.3).

**Single first lane with a frontier seat:** `RECENTER-GATE` (CARD A). If the coordinator prefers a
mathematics seat over a source seat: CARD B.

## 12. OPENs raised (bounded quantity; cheapest test) and FALLACY-v2 check

* `OPEN[FULL-TREE-RECENTER]` — proposed CLOSED POSITIVE (PROVED-HERE/UNREVIEWED). Bounded: 38 rows at
  n ≤ 100 (58 → 20); D ≤ 200: 2,824/1,384/865 → 1,420/686/459. Cheapest test: CARD A (60 min).
* `OPEN[TWISTED-64]` — does Prop 6.4 (`u_s = 1 ⇒ δ*_{s−1} ≥ v_s`) hold for J = cγ^k? Bounded: one
  page; cheapest test: descend Moh's (16,12; X) row again and compare with pp.208–209.
* `OPEN[DESCENDED-PURE-X]` — is `deg_x P(x,0) ≤ k` a theorem for descended pairs (§4.2)? Bounded: the
  Prop 4.1(1) balance for monomial J (one identity); cheapest test: Moh's five descended rows + G2.
* `OPEN[PENCIL-COMPLETION]` — number of admissible degenerate-tree completions of a screened survivor
  satisfying the sum rule; cheapest test: CARD C's control on a tame composition, then (64,48).
* `OPEN[RATIONAL-FIBRE-THEOREM]` — confirm Kaliman 1993 / Lê–Weber 1995 as stated in §5.3 (bounded: two
  abstracts); consequence: OPEN[MF-RATIONAL] closes negative.
* `OPEN[MOH-PROGRAM-ARTIFACT]` — SHARPENED, not re-raised: conditional on §2.1 the residue is 14 rows /
  3 classes at n ≤ 100, all s ≥ 4, all u_s = 1; unconditional: 52 rows, all u_s = 1, s ≥ 4; at s = 3 the
  screen equals Moh's table.
* `OPEN[MINOR-DICHOTOMY]` — RAISED in priority (P2), not re-raised.

FALLACY-v2: no exit price asserted (no `charge_basis` line due). Flag/place/series: §5.2 keeps places
(P), branches and the series-level N distinct; the RH identity is per place. Per-ray charge: none.
Carrier/attainment: §1.2's survivors are PATH-ARITH survivors of a derived screen, never pairs;
§2.1 is a kill rule, not attainment. Pole/interior: §5.2 uses only that ω is regular and nowhere
zero on the smooth affine curve and that f is a regular function there. Floor/attainment: the RH
identity is an equality; §4.2's `l ≤ k` is a necessary condition, typed CONJECTURE pending the
twisted balance. `sat()`/remainder rules: no ideal computation here. Variable/ring map: the descended
pair's (x, y) are Prop 6.3's (γ, π), as in delta 17(t); `t = x⁻¹`. Prime labels are labels. N_min = 6
read from the frontier line, never re-derived; no D ≤ C(N) inferred.

## 13. Typed block and reproducibility

```text
SUBMISSION   ideation-20260903T1200Z-fable5 (Fable 5), basis 4250a6e4, packet c90fa687 (match)
SOURCE-READ  Moh pp.189-190 (PDF 50-51): Prop 5.6 proof; p.190 translation y -> y - ax - b
MEASURED     52 excess C_FULL_TREE_ODE rows: u_s = 1 (52/52), s in {4:37, 5:15}; 38 carry a delta = 0
             nonzero selected edge = exactly the 38 POLY kills; the 14 POLY+ODE excess rows have only
             non-integral intermediate radii; homotheties of Moh's rows, lambda = 2..6: 0 printed-class
             survivors except (384,288,312) V=(3,19) u_s=5; (168,112,144) V=(5,5) u_s=3;
             (504,336,432) V=(5,19),(13,19) u_s=5; (495,330,385) V=(8,41) u_s=14
PROVED-HERE  (UNREVIEWED) the delta = 0 recentring is Moh's p.190 move and the p.189 proof is covariant
             under it: OPEN[FULL-TREE-RECENTER] closes positive; RH identity for f on a fibre (5.2)
CONJECTURE   k-twisted p.189 balance => deg_x P(x,0) <= k for descended pairs (consistent with Moh's shapes)
SOURCE-UNVERIFIED  Kaliman 1993 / Le-Weber 1995 rational-fibre theorem (5.3)
NOT CLAIMED  any kill or survival of a D = 108 row; cofinality or its failure; any realisation; D <= C(N)
FIRST LANE   RECENTER-GATE (CARD A), 60 min, page images
```

Scripts (run from the repo root; both import only tracked tools):

```python
# /tmp/fable-ideation/homothety.py  (section 1.2)
import sys; from fractions import Fraction as F; from math import gcd
sys.path.insert(0,'box'); sys.path.insert(0,'box/mohprog-drivers-20260903')
import moh_skeleton_full as M, full_tree_partition as FT
base=[(64,48,52,3,3),(84,56,64,2,3),(84,56,72,5,3),(75,50,55,3,4),(75,50,55,2,4),(99,66,77,8,8)]
def rows_for(n,m,M2):
    d2=gcd(n,m); d3=gcd(d2,M2); out=[]
    if d3<4: return out
    for V3 in range(1,d3+1):
        for V2 in range(1,V3*d2//d3+1):
            S=M.Skel(n,m,(M2,n-2),{2:V2,3:V3})
            if S.windows_ok() and S.full_ok(): out.append(S)
    return out
for (n0,m0,M20,_,_) in base:
    for lam in range(1,7):
        n,m,M2=lam*n0,lam*m0,lam*M20; R=rows_for(n,m,M2)
        T=[S for S in R if FT.full_tree_ok(S)]; TO=[S for S in R if FT.full_tree_ode_ok(S)]
        print(lam,(n,m,M2),len(R),len(T),len(TO),[(S.V[2],S.V[3],S.d[S.s]-S.V[S.s],
              (S.V[3]*S.d[2]//S.d[3])%S.A(2),str(F(S.d[2],n-M2))) for S in TO])
```

```python
# section 1.1: walk the selected chain of the frozen witness JSONs
import json, ast
from math import gcd
def walk(w):
    while isinstance(w,dict) and 'j' in w:
        yield (w['j'], w['delta'], w['selected_mode']); w=w.get('selected_child')
d52=json.load(open('box/mohprog-drivers-20260903/full-tree-ode-excess-witnesses.json'))
d14=json.load(open('box/mohprog-drivers-20260903/full-tree-polynomial-ode-excess-witnesses.json'))
for k,w in d52.items():
    n,m,Ms,Vs=ast.literal_eval(k); full=[-m]+list(Ms); dd=[n]
    for MM in full: dd.append(gcd(dd[-1],MM))
    us=dd[len(full)-1]-dict(Vs)[len(full)]          # u_s = d_s - V_s
    z=any(d=='0' and mode=='nonzero' for (_,d,mode) in walk(w))
    print(k, 'u_s=',us, 'delta0-nonzero-edge=',z, 'POLY-killed=',k not in d14)
```

OPENS RAISED

* `OPEN[FULL-TREE-RECENTER]` — proposed closed positive (§2.1); bounded 38 rows at n ≤ 100, 1,384 → 686 groups at D ≤ 200; cheapest test CARD A.
* `OPEN[TWISTED-64]` — Prop 6.4 for J = cγ^k; bounded one page (p.198); cheapest test: second descent of Moh's (16,12; X) vs pp.208–209.
* `OPEN[DESCENDED-PURE-X]` — `deg_x P(x,0) ≤ k` for descended pairs; bounded one order identity; cheapest test: Moh's five descended rows + G2.
* `OPEN[PENCIL-COMPLETION]` — admissible degenerate-tree completions per screened survivor; bounded by the finite DP; cheapest test CARD C control.
* `OPEN[RATIONAL-FIBRE-THEOREM]` — confirm Kaliman 1993 / Lê–Weber 1995; bounded two abstracts; cheapest test: web sweep.


Blind-rule note: the scanner is lexical over the whole banked corpus; any line citing a same-round `ideation-20260903T1200Z-*` file was filtered out by the shell before this lane saw the output. Hits are review candidates for the coordinator, never closures.

## COLLISIONS

status: CANDIDATES

### OPEN[FULL-TREE-RECENTER]


- `OPEN[TWISTED-64]` (report:519): NONE

- `OPEN[DESCENDED-PURE-X]` (report:520): NONE

### OPEN[PENCIL-COMPLETION]

- `APPROACHES.md:265` — | 28 | Log surfaces / BMY / log-Kodaira of the resolved pencil | Log-Chern and adjunction inequalities kill the boundary configuration | S14 / G21 / F5 | Partial — BMY marked NEEDS-DATA; Euler/genus ledger "passes identically" (the predi...
- `xmodel/roundview-20260829T1335Z-92ebe92a.md:131` — | 28 | Log surfaces / BMY / log-Kodaira of the resolved pencil | Log-Chern and adjunction inequalities kill the boundary configuration | S14 / G21 / F5 | Partial — BMY marked NEEDS-DATA; Euler/genus ledger "passes identically" (the predi...
- `xmodel/roundview-20260829T1517Z-40c1ab34.md:120` — | 28 | Log surfaces / BMY / log-Kodaira of the resolved pencil | Log-Chern and adjunction inequalities kill the boundary configuration | S14 / G21 / F5 | Partial — BMY marked NEEDS-DATA; Euler/genus ledger "passes identically" (the predi...

- `OPEN[RATIONAL-FIBRE-THEOREM]` (report:522): NONE

<!-- BODY-END -->
