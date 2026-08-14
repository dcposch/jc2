**VERDICT: SOUND-WITH-ERRATA — no Markov counterexample pair against the fat record (1.2); the four finite bounds replay (the ε=0 display assumes ν≥2; “≤ td−2” is really ≤ td−1−ψ); the 11-A v₂=1-versus-3 merge kill stands and every u≥2 preceding pad scales the 5/8 to ≤5/16; NF-Z/NF-P/NF-M stay honestly necessary for a finite quotient and are not implied by any promoted kernel; a fat-state enumerator is complete without those lemmas, but infinite, and cannot certify emptiness.**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-14.
Target: `xmodel/sol-normalform.md` (GPT-5.6-Sol, priced inter-merge normal form).
Claims under review: (1) the exact Markov state — context/budget ledger, `(w,M,ν,κ̄,ρ,pdeg,i)`, last-cell+factor data, cost-coupled arrival provenance, exact scale, charged/tower history, merge/ODE certificate — is genuinely Markov (equal invariants ⇒ identical labelled futures); hunt a counterexample pair; (2) the PROVED finite part — ≤ td−2 positive-price events, pointwise strict numerator descent for concrete clean resonances, cap-free bounds for `k` / multiplicity partitions / `ℓ_ex`, ≤ m−1 merges — replay each bound; (3) the 11-A kill — pole-adjacent 5/8 is merge-impossible by `v₂(pdeg)=1` versus `3`, and any preceding neutral pad scales the alleged intruder to ≤ 5/16 — replay the 2-adic argument and check that pad-scaling covers ALL pad positions; (4) are NF-Z / NF-P / NF-M honestly necessary, or does a promoted fact already prove one; (5) is the compiler interface sound to build against with the conjectures open (does an enumerator that stores the full exact Markov state remain COMPLETE even without the symbolic quotient, just bigger).
Method: line-read of `sol-normalform.md` against `BOOK-OFFAXIS.md` P0/P1/R1/R2, `TOWER-UNIFORM.md` E5F and the m=23 row, `SHEET6-DEPTH-REVIEW.md:183-218,245-267`, `SHEET6-MULTIPOLE.md` MP5/MP6, `SHEET6-III.md` N1, `sol-td11-13-scope.md:290-355`, `sol-gluing-design.md:1149-1154`, `px2.py` identities and `close_states`; independent exact `Fraction` replay of every displayed 11-A identity, the P0 `(C,T,E)` relations, merge `(2.7)–(2.11)`, E5F offsets at `(2/23,23)`, and the ψ-budget table. No other repo file modified. No git.

---

## Findings (worst first)

### 1. Severity: erratum — Claim (1) stands for the fat record (1.2). No equal-invariants / unequal-futures pair exists against that record. Thinner projections that the exec-summary slogan could be misread as do fail, and the written proof is a retention tautology plus a five-consumer checklist, not an exhaustion of consumers.

- File: `xmodel/sol-normalform.md:20-24,69-168`
- Claim: two concrete inter-merge prefixes with equal records (1.2) have identical labelled futures in the fixed remaining context.
- How checked.

  **What was hunted.** Markov failure means a pair of concrete prefixes whose (1.2) records agree and whose labelled futures do not. The pairs the document itself uses to reject thinner quotients were replayed, plus the natural word-collision on a single cylinder.

  | pair | what agrees | what differs in (1.2) | futures |
  |---|---|---|---|
  | td-7 `(w,M)=(2/3,3)` min-price 2 via `(21,15) ν=7` versus the `(21,9) ν=4` self-return | `(w,M)` | `A`, last cell, spent, `Θ` | E5F endpoint and cost disagree |
  | td-7 `(w,M)=(2/5,5)` min-price 3 via `(35,15) ν=7` versus direct `ν=12` at cost 4 (`(85,25)` from `(3/4,4)`) | `(w,M)` | `A`, last cell, spent | same |
  | td-7 `w=2/23, M=23`: direct `(ν,κ̄)=(11,1)` versus clean pad `(45,4)` | `(w,M)` | frame `(ν,κ̄)`, `A` | E5F offsets `−1` versus `+2` |
  | 11-A unpadded 5/8 versus any `A≥2` prefix | entry, `(w,M)` after the resonance | `S`, `Θ`, gap | merge still dies; tower window does not |
  | two `w=2` neutral words with the same product and the same last letter, e.g. `(3,5,7)` versus `(5,3,7)` | `(w,M,ν,κ̄,ρ,P)`, last cell, `S` as a product | `Θ` (intermediate gaps / degrees / prefix-δ) | H8 product and E5F endpoint agree; the ladder sees different intermediate gaps |

  The first four are exactly why `(w,M,λ_min)+cellmap` is not Markov. They are **not** counterexamples to (1.2), because (1.2) keeps `A`, the frame, `S`, and `Θ`.

  The fifth pair is the closest thing to a counterexample the hunt produced. Endpoint frame and full-degree product agree, so every consumer that only looks at the arrival and at `P` is blind to the swap. Tower consumers are not: N4 gaps, prefix-δ, and live-factor caps are evaluated at every created atom. Because `Θ` stores every atom, the records differ. Drop `Θ` (or replace it by `max-gap` plus the product `P`) and this pair is a genuine Markov failure. That is the content of NF-Z, not a refutation of (1.2).

  Machine check of the td-7 cost/offset numbers, against `px2.close_states` from seed `(3/2,2)` and the E5F closed forms at cell `(90,135,67,45)@23` (`kbar_G=6`, `X=4`, `ν_G=67`, `μ=23`):

  ```
  dist[(2/3, 3)] = 2          # (21,15) ν=7 from (3/2,2)
  (21,9) ν=4 self-return     # +2 from that state, total 4
  dist[(2/5, 5)] = 3          # (35,15) ν=7 from (2/3,3)
  cheapest ν=12 landing      # (85,25) from (3/4,4), total 4
  n(11,1) = 11·6 − 67·1 = −1
  n(45,4) = 45·6 − 67·4 = +2
  ```

  These are exactly the regression gates at `:728-730`. The citation `TOWER-UNIFORM.md:147-173,184-201` is the right block: E5F’s `kbar=1` directs are `ν=(m−1)/2` with `n=−1`, and the frozen m=23 row is the pad `(45,4)` with `n=2`.

  **What the proof actually does.** §1.2 inspects five consumers (P0/P1, E5F, merge legality, tower arithmetic, coefficients) and says each is a function of (1.2). The coefficient clause is a retention tautology: “anything not proved to disappear remains in `Ω`.” That is valid as a policy and empty as an identification of fields. The checklist also never names WIN / competing-gap comparisons, N2/N3 joint caps, prefix-δ integrality, Q+E5 as distinct from E5F, or chart/scale data consumed by later gluing. Those consumers are covered *if* `Θ` and `Ω` really retain everything they can observe. The theorem gives no independent reason to believe the listed `TowerHistory` / `CoefficientHistory` slots are that complete; it just defines them to be.

  **Symbolic half.** The setwise statement is conditioned on “complete feasible-value constraint systems agree.” Equivalence of arbitrary Diophantine constraint systems is not a compiler-executable equality. For concrete instantiated records this does not matter. For symbolic records it means §1.1’s dedup rule is not an algorithm until the constraint language is restricted to the residue-class cylinders already written in (2.5)–(2.6), or NF-Z/P/M supply a canonical form.

  **Erratum to write.** (i) State explicitly that the hunt found no concrete pair against (1.2), and that the fifth pair above is the reason `Θ` cannot be replaced by a max-gap / product summary. (ii) Replace “finite-arity exact Markov invariant” with “finite-field-count record whose list-valued fields (`Θ`, `Ω`, the exact word) have unbounded length.” Finite arity as a datatype is true and easy to misread as finite range. (iii) Restrict symbolic equality to a named decidable fragment, or mark it `UNRESOLVED` alongside the budget inventory flag.

  The sufficiency *claim* for concrete fully-instantiated (1.2) records survives. That is why this is an erratum and not a break.

### 2. Severity: erratum — Claim (3) stands. The 2-adic merge kill is exact. Preceding u≥2 pads all scale to ≤5/16. The written pad slogan does not mention the degree-preserving ν=1 insertion, which keeps 5/8 but does not save the route.

- File: `xmodel/sol-normalform.md:486-596`; `xmodel/sol-td11-13-scope.md:337-355`; `SHEET6-MULTIPOLE.md:52-54`; `BOOK-OFFAXIS.md:305-315`
- Claim: the pole-adjacent 5/8 route is merge-impossible by `v₂(P)=1` versus `3`; any preceding neutral pad scales the alleged intruder to at most 5/16.
- How checked.

  **Entry packet.** Type `(2,3)`, `L3a1b1n2 + L8a2b2n3`: `Λ=(3,8)`, `P=(2,4)`, `w=(2,3)`, `M=(1,2)`. Matches `sol-td11-13-scope.md:294`.

  **Strict branch.** `M=1` is absorbing (MP5 / St 8.4). `W(2)={2}`: `Δ | 2` and `Δ≥3` is empty, so no changing clean resonance. Neutral `(κ̄,ρ,w)=(2(u+1),2,2)`. BOOK-N1 (`SHEET6-III.md:121-129`) is `gcd(κ̄,ν)=1` at every `ν≥2` vertex, i.e. `gcd(2,u)=1`, so every multiplier is odd. Entry `P=2` times an odd product is `P₁=2C` with `C` odd, so `v₂(P₁)=1`. Pole-adjacent gap with parent degree 2 is `(ν_X+1)/(2ν_X)`. Independent check: `5/8 > g_X ⇔ ν_X>4`; N1 makes `ν_X` odd, so the in-window family is exactly odd `ν_X≥5`. `ν_X=3` has `g_X=2/3>5/8` and is outside the advertised window. This block is exact.

  **Off-axis resonance.** `(Δ,n,ν)=(3,2,2)`, `dq=5`, from `(w,M,P)=(3,2,4)`:

  | `l` | `E=l dq−dp` | `κ̄` | `P'=4·dp/l` | `w'` | `M'` | gap |
  |---:|---:|---:|---:|---:|---:|---|
  | 1 | 3 | 5 | 8 | 2 | 1 | 5/8 |
  | 2 | 6 | 5 | 8 | 2 | 1 | 5/8 |

  Both allowed arrivals give the same full degree because `P·(2l)/l=8`. After the step, N1 again forces odd multipliers, so `P₂=8B` with `B` odd and `v₂(P₂)=3`. Identity check of the gap: `l·5/(4·2l)=5/8`.

  **2-adic merge rejection.** `m=2`, one merge.

  - Root: R2.1 case IV needs every arriving `w<1`. Both branches arrive at `w=2`. Dead.
  - Interior: current `M=1` on both sides forces `(μ₁,μ₂)=(1,1)`. MP6(b) (and the general St 8.3(ii)+Prop 8.1(i) identity `P_{H_e}=i_G μ_e`, which does not use the zero-slot) forces `P₁=i_G=P₂`. Then `v₂(P₁)=1 ≠ 3≤v₂(P₂)`.

  Preceding pads only raise `v₂(P₂)`: a prefix product `A` gives `P₂=8AB`, so `v₂(P₂)≥3`, still not `1`. Post-resonance the chain is `M=1`, hence `l=1` and R1.3 forbids dirty vertices; remaining steps are odd neutrals and preserve `v₂=3`. There is no 2-adic cancellation path. The certificate

  ```
  H8_EQUAL_QUOTIENT_VP_MISMATCH {
    prime: 2,
    arrivals: [(mu=1, vp_pdeg=1), (mu=1, vp_pdeg>=3)]
  }
  ```

  is the right one-line object. It removes the specific conjecture at `sol-td11-13-scope.md:337-355` for this family. E5F and the local ODE never fire. Honest residual, as written: other charged 11-A routes are untouched, and this is not a global NF-Z.

  **Pad-scaling, position by position.** Resonance gap as a function of the parent degree is `g_R=5/(2 P_before)=5/(8A)`.

  | pad position | what it does to `g_R` / `v₂` | in-window? | merge? |
  |---|---|---|---|
  | empty prefix `A=1` | `g_R=5/8`, `v₂=3` | yes, vs odd `ν_X≥5` | dies, 1 vs 3 |
  | one preceding neutral `u≥2` on the `w=3` branch | `P_before=4u≥8`, `g_R≤5/16` | no: `5/16<1/2≤g_X` | still dies, `v₂≥3` |
  | several preceding neutrals | `A` is a product of `u_i≥2`, `g_R` smaller | no | still dies |
  | even `u` (legal at `w=3`: N1 only needs `3∤u`) | `v₂(P₂)≥4`, `g_R≤5/16` | no | still dies |
  | after the resonance, before the merge | 5/8 atom already exists; odd neutrals preserve `v₂=3` | 5/8 remains | dies |
  | on the strict `w=2` branch | first vertex **is** `X`; later neutrals have N4 gap `(ν+1)/(D_prev ν)≤3/8` once `D_prev≥4` | does not create or scale 5/8 | `v₂(P₁)` stays 1 |
  | charged / pure-b / dirty step before the resonance | leaves `(w,M)=(3,2)`; not this family | out of scope | out of scope |

  Independent scan of `A∈{1,2,4,5,7,8,10,11,13,14,16,25,35}`: `A=1` is the unique value with `g_R≰5/16`; every `A≥2` has `g_R≤5/16<1/2`. The comparison does not depend on which odd `ν_X≥3` is chosen, so it covers every legal `X`, not just a sample.

  **The ν=1 hole in the slogan.** Cylinder (2.5) is stated with `u≥2`. A `ν=1, n=1` insertion at `(w,M)=(3,2)` is *not* in that cylinder (N1 is scoped to `ν≥2`; R1.2 is case II / `V_{1,a}`). If it is nonetheless admitted as a “neutral pad,” it does **not** scale the degree: `P'=P·dp/l=4`, and the subsequent `(2,2)` resonance is again `P=8`, `g=5/8`. So the sentence “any preceding neutral pad scales the alleged intruder to at most 5/16” is false if “neutral pad” is read as every zero-cost insertion, and true if it is read as cylinder (2.5). Either reading, the route still dies at the merge by `v₂`. `px2.chain_steps` does not emit `ν=1` clean cells (`nu` starts at 2), which is the document’s own convention.

  **Erratum to write.** Replace the STATUS / §4.2 slogan by: every preceding (2.5)-pad has `u≥2`, hence `P_before≥8` and `g_R≤5/16<g_X`; a degree-preserving `ν=1` insertion, if ever allowed, keeps `g_R=5/8` and is still merge-impossible by the same 2-adic mismatch. List the position table above, or the claim “ALL pad positions” is an un-audited sentence.

### 3. Severity: erratum — Claim (2) stands as finiteness, not as the displayed inequalities. Four of four bounds replay; two of the written displays are strictly narrower than the fact.

- File: `xmodel/sol-normalform.md:175-232,279-304,457-464`; `BOOK-OFFAXIS.md:455-500,285-315`; `SHEET6-DEPTH-REVIEW.md:256-267`
- Claim: at most `td−2` positive-price events; pointwise strict numerator descent for concrete clean resonances; cap-free bounds for `k`, multiplicity partitions, and `ℓ_ex`; at most `m−1` merges.
- How checked.

  **≤ m−1 merges.** A rooted hierarchy on `m` leaves with every internal node of out-degree `r≥2` satisfies `Σ(r−1)=m−1`. The number of merge nodes is at most `m−1`, with equality on a binary tree. This is the tree-layer count already in `SHEET6-DEPTH-REVIEW.md:258`. Exact.

  **Pointwise numerator descent.** Changing clean step: `Δ=(n−1)ν+1≥3`, `Δ | num(w)`, `w'=w·n/Δ`. For `ν≥2, n≥2`, `n/Δ=n/((n−1)ν+1)≤n/(2n−1)≤2/3`, with equality at `(n,ν)=(2,2)`. Write `w=a/d` reduced. Then `Δ | a` and the unreduced numerator of `w'` is at most `a n/Δ≤2a/3<a` for `a≥1`. Reduced numerator is therefore strictly smaller. Independent scan of every reduced `w` with `num≤39`, `den≤19`, every legal `(Δ,n,ν)`: 0 descent failures. `a=1` admits no `Δ≥3`. This is a theorem about *concrete* rationals, exactly as labelled. It is not a uniform symbolic closure (that is NF-P, correctly).

  **Cap-free `k`, partitions, `ℓ_ex`.** Replay of (2.1) on the lattice `l=2..5`, `ε<l`, `k≤4`, `x≤7`, `ν=1..7`: `E=l dq−dp=νC+l−ε` identically, and `C·dq−Q·E=−T` identically, where `Q=1+k+x`.

  - `k≤b`: AF2 prices each NE orbit at least 1, so `k` cannot exceed remaining budget. Exact.
  - `1≤m_j≤l−1`: searrow/NE, `m_j dq<dp<l dq`. Finite sorted partitions of `S∈[k, k(l−1)]` for fixed `l,k`. Exact.
  - `0≤ε<l` on a *chain* P0 step: a free 0-root is a non-arriving NE orbit, so `ε dq<dp<l dq`. Exact for §2.1; not claimed at merges (arriving `ε=μ₀` can be large).
  - `ε>0`: `T≥1` is exactly the strict 0-root NE law `ε Q<l+S` (the identity `T=S+l−ε Q` does not involve `ν`). Then (2.3) is just solving `T≥1` for `x`. Exact. `T=0` is the R1.0 boundary `dp=ε dq`; `T<0` violates NE and is correctly excluded. `px2.py:92-93` skips `T≤0` for the same reason.
  - `ε=0`, displayed (2.4): `E=νC+l≥2C+l` uses `ν≥2`, and `E≤l a T` uses `E | l a T` with `T=S+l`. That bounds `x` for `ν≥2`. **The displayed inequality is false for `ν=1`**, where `E=C+l`. Finiteness still holds: `C+l≤l a(S+l)` bounds `C`, hence `x`. NF-P’s “`ν=1` case-I *merge* schemas” do not cover a `ν=1` dirty *chain* step. `px2` also rejects `nuq<2`. The missing line is one inequality, not a missing finiteness proof.

  **≤ td−2 positive-price events.** P1 / St 9.4 is `Σλ ≤ td−1−ψ` with `ψ=⌈1/(1−w_term)⌉−1`, and every non-clean step has `λ≥1`, so the *number* of such events is `≤ td−1−ψ`. Terminals need `w<1` (R2.1 IV).

  | `w_term` | `ψ` | budget at td=11 |
  |---|---:|---:|
  | `2/3` | 2 | 8 |
  | `3/4` | 3 | 7 |
  | `∈(0,1/2]` | 1 | 9 |
  | `0` | 0 | **10 = td−1** |
  | `<0` | 0 | td−1 |

  So “at most `td−2`” is the `ψ≥1` case, i.e. `w_term>0`. Transport from a positive entry `w` by R1.2 / R1.4 / (2.6) preserves `w>0`, and standard L6 entries have `w₀=a(b(α+β)−1)/(bν)>0`. A merge-emitted `w_tr=0` is not excluded by the written filters (`κ̄_G>0`, `X_G>0` do not force `κ̄>ρ`). The STATUS line should say `≤ td−1−ψ`, with `td−2` as the generic positive-`w` corollary (and `td−1` if a `w≤0` terminal is ever legal). “At most 9 for td-11 and 11 for td-13” inherits the same `ψ≥1` hypothesis. Finiteness is not in doubt: even `td−1` is a cap.

  Mid-route, `ψ` is not yet known. A compiler residual must use a conservative cap (`td−1`, or `td−2` once positivity of every legal terminal is recorded). Using the exploratory `k<7` / `ℓ_ex<41` loops is correctly forbidden.

### 4. Severity: clear — Claim (4). NF-Z, NF-P, and NF-M are honestly necessary for a *finite* compiler quotient. No promoted kernel proves any of them. They are not necessary for fat-state completeness.

- File: `xmodel/sol-normalform.md:391-484`; `SHEET6-DEPTH-REVIEW.md:183-218`; `xmodel/sol-gluing-design.md:1149-1154`; `TOWER-UNIFORM.md` N1–N4 / E5F; `BOOK-OFFAXIS.md:655-669`
- Claim: the three obligations are independent; none follows from the cited kernels or from the other two.
- How checked.

  **NF-Z.** The depth theorem gives a finite `w`-alphabet and a finite jump-cell *menu* on an `M=1` merge-free segment, with the safe representative bound `d₀≤2 gen(W)+2` (the printed `gen(W)+2` is still unproved; the document cites the right review lines and uses only (2.12)). It does not identify E5F/tower futures of equal-`w` vertices. N1 is `gcd(κ̄,ν)=1`. N4 is the gap identity `(ν+1)/(D_prev ν)` and a monotonicity bound; it does not quotient the degree product or H8/cap congruences. The gluing “neutral-insertion invariance” conjecture is a coefficient-eliminant statement, weaker and also unproved. The 11-A 2-adic projection is a one-prime special case of a consumer monoid, not NF-Z. Finding 1’s fifth pair is exactly the obstruction: same endpoint and same `P`, different intermediate tower atoms. Honest.

  **NF-P.** Three bundled obligations, not one: (i) unbounded characteristic of a single pure-(b) vertex (2.6); (ii) pure equal-handshake merge cylinders, where `w_tr` *can* depend on the free `ν` via (2.10); (iii) every `ν=1` case-I merge schema, including the eta-absorbed / eta-factor variants and the td-7 `(2,2t)` tail. The gluing “pure-b characteristic invariance” is (i) for coefficients only. Pointwise numerator descent discharges changing resonances of a *concrete* `w`; after a P0 pure-(b) step `w'=lw/e` is itself concrete, so the “uniform clean-resonance closure” clause is needed for merge-emitted parametric `w`, not for (2.6) itself. That is a packaging nit, not a proof of NF-P. P3’s `(2,2t)` inversion is td-7-specific (`BOOK-OFFAXIS.md:643-644`). Honest, and slightly oversold as a single lemma.

  **NF-M.** The td-7 generalized zero-chain law is a coefficient decision on a fixed 62-cell book. It is not a finite future-local type for a parametric multi-orbit / mixed / `ν=1` merge ODE. Solving one concrete cell does not uniformize a `ν`- or `x`-tail. Honest.

  **Independence, as stated.** Without NF-Z there is unbounded zero-cost depth at frozen charged skeleton and frozen coefficients. Without NF-P there is an unbounded characteristic at one charged vertex, plus unclassified `ν=1` merges. Without NF-M there is unclassified coefficient data after every integer parameter is frozen. None of those three sentences is discharged by either of the other two, or by depth / N1–N4 / P3 / the 11-A 2-adic. The “independent relative to the cited kernels” claim is correct.

  What the three are *not* needed for is recorded under finding 5.

### 5. Severity: clear — Claim (5). The interface is sound to build against with the conjectures open. A fat-state enumerator is complete without the symbolic quotient. “Just bigger” means infinite, and emptiness is not a decision.

- File: `xmodel/sol-normalform.md:598-737`
- Claim: until NF-Z/NF-P/NF-M are proved, the interface is the safe stopping point — exact, auditable, finite-arity, not yet a terminating finite census quotient.
- How checked.

  The schema is a field-wise image of (1.2)–(1.3): `ContextKey`/`BudgetLedger` = `χ,L`; `Frame` = the 7-tuple plus checked `dp,dq,X`; `ChainRecord`/`MergeRecord` = last cell and (1.3); `ArrivalWitness`/`SymbolicEndpointFamily` = `A`; `ScaleExpr` = `S`; `TowerHistory` = `Θ`; `CoefficientHistory` = `Ω`. The constructors on `ScaleExpr` match the transport identities (CONST, `P·dp/l`, `P·u`, `P(lu+ε)/l`, `i_G dp`). `NEUTRAL_STAR` is correctly forbidden in a final census until NF-Z. Rules 1–7 match §1.1 and the td-7 anti-patterns (no unioned `cellmap` on `λ_min`, no sorting of labelled branches, no exploratory caps, no empty certificate under an open obligation).

  **Completeness without the quotient.** Store the full exact word, the full exact characteristic, and the live coefficient variables. Do not apply `NEUTRAL_STAR`, do not fold cylinders, do not promote a lower bound to an exact ledger. Then every concrete legal route specializes exactly one record, and exact Markov sufficiency says quotienting equal records loses no future. That enumerator is **complete as a representation of the concrete route set**. The conjectures are not used.

  It is not “just bigger” in any finite sense. Cylinder (2.5) is an infinite residue union; cylinder (2.6) is an infinite family at one charged vertex; `Θ` has unbounded length. A naive instantiation loop does not terminate. Rule 6 is the honest operational consequence: a run with `NEEDS_NF_Z` / `NEEDS_NF_P` / `NEEDS_NF_M` / `UNRESOLVED_BUDGET_INVENTORY` may emit a symbolic candidate or `OPEN`; it may **not** certify an empty panel.

  So the interface is a sound *semidecision* procedure for ALIVE (if a concrete route exists and parameters are instantiated far enough, it will be found) and an incomplete *decision* procedure for DEAD. Uniform kills that do not need a quotient — the 11-A 2-adic certificate is the model — remain available and are the only emptiness proofs the interface currently justifies.

  **Build-against risks, not interface breaks.** (i) Symbolic dedup on “full future signature” is not executable for general constraint systems (finding 1). Implement equality first on concrete records and on the named residue cylinders. (ii) `gross_cap` must not silently bake in `td−2` before terminal `ψ` is known (finding 3). (iii) `locality_type_if_proved` must stay unset until NF-M; filling it early re-introduces the false identification NF-M is there to prevent. (iv) The four minimum regression gates at `:728-733` are the right ones and all four replay (findings 1–3, and `d₀=2 gen(W)+2`).

  Conditional completeness theorem (`:456-476`): if the three conjectures hold, the finite closed quotient exists. The proof is the obvious induction and is correctly labelled conditional. No hidden use of an unstated fourth lemma was found.

---

## Attack scorecard

| attack | result |
|---|---|
| (1) Markov: hunt an equal-(1.2) / unequal-futures pair | **no such pair.** Thinner projections fail; the fifth pair in finding 1 is why `Θ` is mandatory |
| (2a) `≤ td−2` positive-price events | **finite, display too sharp.** True bound is `≤ td−1−ψ`; `td−2` needs `ψ≥1` |
| (2b) pointwise numerator descent | **proved** on the concrete lattice; 0 failures in the scanned range |
| (2c) cap-free `k` / partitions / `ℓ_ex` | **finite.** `(C,T,E)` identities hold; `T>0` is 0-root NE; `ε=0` display assumes `ν≥2` |
| (2d) `≤ m−1` merges | **proved** (tree count) |
| (3a) 11-A `v₂=1` vs `3` | **proved.** Root and interior cases both die; padding cannot cancel the valuation |
| (3b) pad-scaling covers ALL positions | **all `u≥2` positions yes; `ν=1` degree-preserving insertion keeps 5/8 and still dies at merge** |
| (4) NF-Z/P/M necessary, none already proved | **yes**, for the finite quotient only |
| (5) fat-state enumerator complete with conjectures open | **yes, as a complete infinite representation / ALIVE semidecision; not as an emptiness decision** |

---

## What the compiler may treat as proved, today

1. Concrete (1.2) records are an exact Markov state. Dedup and Pareto only on that full record, with exact budgets.
2. Non-parametric P0 dirty steps are a finite menu (write the `ν=1, ε=0` bound; do not import `k<7` / `ℓ_ex<41`).
3. Concrete changing clean resonances strictly descend the reduced numerator.
4. `ν≥2` merges reduce to a finite discrete menu plus the pure cylinder; `ν=1` case I is unreduced.
5. At most `m−1` merges; at most `td−1−ψ` positive-price events.
6. The 11-A pole-adjacent 5/8 family — including every preceding (2.5)-pad — is merge-dead by `H8_EQUAL_QUOTIENT_VP_MISMATCH` at `p=2`. Emit that certificate; do not enumerate odd `ν_X≥5`.

Everything else (neutral-word summaries, free-characteristic / `ν=1` schemas, multi-orbit coefficient types, empty-panel certificates that are not a uniform kill of this kind) stays `OPEN`.
