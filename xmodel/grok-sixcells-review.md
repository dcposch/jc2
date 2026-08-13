**VERDICT: SOUND — the (9,15,7,3)@μ0=2 next-step survival witness substitutes exactly at every displayed vertex, the two equality completions are exactly the filed px5 pair, both case-IV triples are the P1 terminal laws, integerized AF2 sharpness is a sandwich, and the extra-unit step is correctly labeled CONJECTURE.**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-13.
Target: `xmodel/sol-sixcells.md` (GPT-5.6-Sol, next-tier attack on the six td=7 survivor cells).
Claim under review: td-7 cell (9,15,7,3) at μ0=2 has PROVEN next-step SURVIVAL — local solution p=η²(t−A), q=η(t−A)(t−(2/3)A), t=η⁷, C̃=−(14/15)A² passing every transport handshake (SHEET6-DEPTH w, BOOK-OFFAXIS R2.1) and both deduplicated budget-equality completions (case IV at (2/3,3,2) and trunk (35,15,7,5) at (2/5,5,1)); equality forces integerized AF2 summands sharp; extra-unit contradiction is CONJECTURE.
Method: exact η-calculus substitution of every displayed (p,q) into the leftover of Prop. 8.1(iv)/T1 over Q(A); silent replay of `px5.py` (raw 1713 / dedup 1689) and extraction of every `cell(9,15)` record; predecessor Dijkstra on the filed `px2.chain_steps` menu; line-read of every cited P0/P1/P2/R1/R2/AF2/LROOT/DEPTH/TEMPLATE pin.
No other repo file modified. No git.

---

## Findings (worst first)

### 1. Severity: clear — every displayed vertex substitutes into Prop. 8.1(iv)

- File: `xmodel/sol-sixcells.md:145-174, 196-206`
- Claim: each listed (p,q) solves T1 (θpq′−p′q=Cp after legal division by 1−u) with the displayed forced relation and nonzero C; root law holds.
- How checked: reduced leftover in the filed η-calculus,
  p=η^ε P(t), q=η Q(t), t=η^ν,
  L=(θ−ε)PQ + ν t (θ P Q′ − P′ Q),
  T1 with constant C iff L=C·P as polynomials. Built L over `fractions.Fraction` at A=1 and A=5. Derivatives are in η (the filed ODE), not in t; this is the same leftover that reproduces `sol-td7-law.md` (3) on the merge shape.

  | vertex | θ, ν, ε | forced data | claimed C | L/P | rem |
  |---|---|---|---|---|---|
  | F1 (20,16) | 5/4, 5, 0 | B+D=3A, BD=3A² | −15A³/4 | −15A³/4 | 0 |
  | F2 (119,35) | 17/5, 17, 0 | B=3A/2 | 51A²/10 | 51A²/10 | 0 |
  | F3 (38,6) | 19/3, 5, 3 | — | −10A/3 | −10A/3 | 0 |
  | H2 (14,8) | 7/4, 7, 0 | — | −7A/4 | −7A/4 | 0 |
  | G (9,15) | 3/5, 7, 2 | B=2A/3 | −14A²/15 | −14A²/15 | 0 |
  | trunk (35,15) | 7/3, 7, 0 | B=2A | 14A²/3 | 14A²/3 | 0 |

  Nearby wrong relations fail constancy (F1 with B+D=2A or BD=2A²; F2 at every tested B≠3A/2). The F1 system is affine in (σ,π)=(B+D,BD): coeff of t forces σ=π, coeff of t² forces σ=3A, so the displayed pair is the unique solution over Q. Displayed leftovers (2.5) and the trunk formula (7/3)((B−2A)t+AB) match L/P at three B-values each. η-degrees recover every advertised (d_p,d_q). All C≠0 for A≠0. Disc(z²−3Az+3A²)=−3A²≠0; no listed extra root is 0 or A; every p-root is simple in q; the only q-only root is G's B, which is simple. 1−u≠0 at every vertex (κ̄∈{3,4,5}). Cor 6.1 top-cancellation applies: all six vertices are ↘. This is existence of a vertex-local admissible solve, which is what they claim.

### 2. Severity: clear — the two completions are exactly the filed generator's (9,15) book

- File: `xmodel/sol-sixcells.md:176-210`, citing `px5.py:254-262` and `xmodel/grok-td7-law-review.md:48-58`
- Claim: exactly two deduplicated routes through (9,15,7,3)@2, both budget-equality: direct case-IV at (2/3,3,2) with cost 4, and one trunk step through (35,15,7,5) to (2/5,5,1) with cost 5.
- How checked: imported the filed `px5` functions and reran `main`'s collection silently (52.5s). Raw 1713 / deduped 1689 / equality 1390, same as the previous law review. Live-C split:

  | cell | routes | equality |
  |---|---:|---:|
  | (10,15,7,5) | 47 | 29 |
  | (9,15,7,3) | 2 | 2 |
  | (15,25,8,5) | 1 | 1 |
  | (15,25,12,5) | 1 | 1 |
  | (18,27,13,9) | 1 | 1 |
  | (39,65,32,13) | 1 | 1 |

  The two deduped `(9,15)` lines are, verbatim,

  ```
  lam=4<=4: C mu0=2 w2=1/2(lam4) nu2=7 cell(9,15)nu7M3
            | trunk(2/3,3)+0 -> terminal(w=2/3,M=3,psi=2)
  lam=5<=5: C mu0=2 w2=1/2(lam4) nu2=7 cell(9,15)nu7M3
            | trunk(2/3,3)+1 -> terminal(w=2/5,M=5,psi=1)
  ```

  Raw count is 4: the second copy is the parallel arrival (w,M)=(1/2,4) at the same lam=4, which the filed `seen` key collapses (ctx does not carry M2). No third terminal. `trunk_routes(2/3,3,bleft=1)` is exactly those two states; bleft=2 would add (2/9,9) and (2/7,7), which overruns because lam_pre=4. The unique λ=1 menu edge (2/3,3)→(2/5,5) is `st96 l3e0k1S2x0nu7(35,15)`. So the named trunk cell is not an extra invention: it is the unique priced step realizing the generator's second terminal.

### 3. Severity: clear — both case-IV checks are the filed P1 statement

- File: `xmodel/sol-sixcells.md:182-206`, citing `BOOK-OFFAXIS.md:486-500`
- Claim: direct completion passes case IV at (w,M,ψ)=(2/3,3,2); the other passes case IV at (2/5,5,1).
- How checked: P1 (`BOOK-OFFAXIS.md:486-500`) is the case-IV terminal certificate, not R2.1(iv) alone. It says: G may be “the trunk chain vertex or the merge itself”; w_G<1 (R2.1 IV), M_G≥2 (MP2), j:=M_G(1−w_G)∈ℕ*, and ψ=⌈M_G/j⌉−1, equivalently ψ=⌈1/(1−w_G)⌉−1; budget Σλ≤td−1−ψ. It even works the example “w=2/3: ψ=2, budget td−3” and “w≤1/2 keeps ψ=1”.

  | terminal | w<1 | M≥2 | j=M(1−w) | ψ=⌈M/j⌉−1 | 6−ψ | Σλ |
  |---|---|---|---:|---:|---:|---:|
  | merge itself | 2/3 | 3 | 1 | 2 | 4 | 4 |
  | (35,15) trunk | 2/5 | 5 | 3 | 1 | 5 | 5 |

  Both j∈ℕ*. The citation range is the statement they use. R2.1:308-309 is only the parent-side w_e<1 root-merge filter; they do not pretend that line computes ψ. Merge-as-terminal is explicitly in P1, so calling the first completion “case IV at (2/3,3,2)” is the book's language, not a conflation with a root merge of two chains.

### 4. Severity: clear — the parent chain is a min-cost witness, and the charged DAG is unique

- File: `xmodel/sol-sixcells.md:61-143`
- Claim: the table is a minimum-cost chain-2 witness; every (2.1) row holds; both merge handshakes close by R2.1; arrival (μ0,ν_H)=(2,7) is legal; every positive-cost min path carries (119,35) and an l=7,ε=3 pure-b.
- How checked:
  - Dijkstra on `px2.chain_steps` from (3/2,2) at budget 5: dist(1/2,2)=4, dist(3/4,4)=2, dist(2/7,7)=3. The paper's cost 2+1+1 is the minimum, not a slack path.
  - Every table row of (2.1) is an identity: (1/2+7)/(5+7)=20/(2·16); (1/4+21)/(4+21)=119/(4·35); (1/7+46)/(5+46)=38/(7·6); (1/2+17)/(3+17)=14/(2·8); and κ̄_child=(κ̄_par+n)/ν_par recovers 4,5,3,4. Pure-b P0 side-check: w=l w_par/(l−ε)=7·(2/7)/4=1/2 and λ≥⌈l w_par/ε⌉=⌈2/3⌉=1. H2 is the clean n=1 specialization of R1.2 (Δ=1, w conserved, n_e=tν−ρ=17).
  - Unique charged min-DAG into every even-M state with νw=7/2 and lam=4, namely (1/2,2) and (1/2,4):

    ```
    (3/2,2) --λ=2 (20,16)--> (3/4,4) --λ=1 (119,35)--> (2/7,7) --λ=1 pure-b l7e3--> (1/2,*)
    ```

    No other charged parent exists. Identity neutral-drops generate infinitely many padded walks; they do not add charge. So “(119,35) and l=7,ε=3 pure-b sit on every positive-cost min path” is true, and (38,6) is correctly flagged as a ν-representative of that pure-b family, not a universal cell pin. The uniform gap (X/3−κ̄)/ν=2/3 along the family is a one-line identity from their displayed (κ̄,X)=((ν+1)/2,(7ν+3)/2).
  - Merge: chain 1 frozen (1,5,2;2,1) is Q=(aα,bα,ν,b,a(α+β)) at (a,b,ν)=(1,1,2) of type (2,3). n1=5 gives κ̄_G=(5+5)/2=5, X=(1+5)/2=3. R2.1 II: X=μ(κ̄−w)=1·(5−2)=3. Case III: X=μ0(κ̄−ν w)=2(5−7/2)=3. Class-C pin (μ0 ν w−2)/(μ0−1)=(7−2)/1=5. Then X/κ̄=3/5=9/15, ρ=3/9=1/3, w=(5−1/3)/7=2/3, M=3. Arrival: 2∣M=2 and 7≡−1 (mod 2), which is P2:510-519. DEPTH §5c is the μ=1 shadow of the same 0-edge; they use the general-μ R2.1 form, which is the one the off-axis book actually states at :301-309.

### 5. Severity: clear — integerized AF2 sharpness is a sandwich; extra unit is correctly CONJECTURE

- File: `xmodel/sol-sixcells.md:226-351`
- Claim: L=Σ a(F,c)=6−ψ forces every recorded integerized AF2 summand sharp, every selected cv vertex to have exactly that integer mass, and (under the book's E9/H2 Euler reading) x-mass=ψ with every δ_a=0; the extra unit from a repeated direction is not a consequence of Prop. 7.3.
- How checked: AF2 (`SHEET6-AF2.md:94-115`) is λ_F≥Σ_c max(1,⌈gap⌉) with distinct directions giving distinct Y(F) vertices and each mass a positive integer. P1 is Σ_F λ_F≤6−ψ. If L=6−ψ then 0≤Σ(λ_F−Σ a(F,c))≤0, so every difference vanishes. That is 1–2. Part 3 uses the Euler identity td−1=Σ_cv κ(π−1)+Σδ (`SHEET6-LROOT.md:33-98`), λ_root=0 at every case-IV terminal (`:100-126`), and the ψ lower bound becoming sharp-capable by the single-root identity k_f=deg p_G. Forced y-mass 6−ψ plus x-mass ≥ψ exhausts 6; remaining nonnegative terms vanish. The standing-E9/H2 rider is the book's own reading (LROOT:103-104), not a silent extra axiom.
  Direct substitution into P0 (`BOOK-OFFAXIS.md:455-475`) recovers every displayed raw gap: F1 two simple extras, gap=X−κ̄=5−4=1; F2 gap=17/3−5=2/3; F3 zero-root (X/ε−κ̄)/ν=(19/3−3)/5=2/3; trunk gap=7/2−3=1/2. Merge prices 0 by P2:502-509 (arriving 0-chain, q-extra not a p-direction). Ledgers (3.1) are 4+2=6 and 5+1=6. “Integerized” is load-bearing: equality pins the rounded floor, not the rational gap — they say so.
  Prop. 7.3 (`SHEET6-LT-REVIEW.md:84-118`) gives equality only for eventual-fibre multiplicity one; at multiplicity ≥2 the printed control is ≥, not a strict excess. The extra-unit implication is therefore not a theorem. They label it CONJECTURE, refuse the false lemma “every μ0≥2 merge costs one”, and name the (10,15) direct route as the necessary negative control (`sol-avenues2.md:160-170`). That control is real: its only charged A-step is a simple NE orbit, μ0=3 is an arriving pole direction, merge costs zero, and it saturates 2=6−ψ. The provenance tuple they point at (`sol-avenues2.md:174-183`) is already specified. No CONJECTURE is used in the survival proposition.

### 6. Severity: clear — higher-jet / coefficient compatibility is not a hidden assumption

- File: `xmodel/sol-sixcells.md:59-60, 212-224, 390-396`
- Claim: the proposition does not assert a simultaneous Puiseux/Keller lift; independent local scales are CONJECTURE; DEPTH and TEMPLATE leave the coefficient layer out of scope.
- How checked: St 3.9 pins leading Taylor coefficients across edges (`SHEET6-TEMPLATE.md:140-154`) and does *not* pin subleading pattern coefficients. Independent A_v at each vertex can violate that leading-coeff transport. They do not use St 3.9, do not glue A_v, and do not claim a global Keller pair. DEPTH `:403-422` explicitly excludes the coefficient layer and M≥2 suffixes; DEPTH `:429-432` and BOOK `:632-646` warn that the state/arrival construction is a conservative superset with P-realizability untracked. The proven object is finite Q-transport (Prop. 9.3 (a)–(d) / R1.2 / R1.4 / R2.1 / P1) plus vertex-local T1. That is a strictly smaller tier than a glued jet, and they say so twice (once under the proposition, once as a boxed CONJECTURE). Attack (5) therefore finds a correctly labeled perimeter, not a smuggled hypothesis.

### 7. Severity: nit — two citations name the right object one click off

- `SHEET6-DEPTH.md:67-77` is the *definition* w=(κ̄−ρ)/ν, not a conservation theorem. The w-laws they actually use are R1.2/R1.4 at `BOOK-OFFAXIS.md:239-256,273-283`, which they also cite. Content is right; “DEPTH w-invariant” as a handshake name is slightly fat.
- `px5.py:63-87` is `close_with_cells`, which stores (w,M)↦λ_min and does not retain predecessors. The chain table is a hand replay of `px2.chain_steps` against that distance function, which is what they say (“predecessor replay of that exact transition graph”). Not a false citation, just not a stored path.

No other pin in §§1–5 was off by more than a fat line-range. P0/P1/P2/P3, R1.0–R1.4, R2.1–R2.2, AF2, LROOT, TEMPLATE 2a, and the six-cell local table in `sol-td7-law.md:264-283` all say what they are cited for.

---

## Attack-list scorecard

| # | Target | Result |
|---|---|---|
| 1 | Exact substitution into Prop. 8.1(iv) at every displayed vertex | Holds. All six L/P are the claimed nonzero constants; F1 relation unique over Q; (2.5) and the trunk leftover replay. |
| 2 | Two-completion census vs filed `px5.py` | Holds to the last string. Deduped 2/2 equality; terminals (2/3,3,ψ=2) and (2/5,5,ψ=1); unique λ=1 edge is (35,15,7,5). |
| 3 | Replay both case-IV checks vs the filed statement | Holds. P1:486-500 is exactly those triples, including merge-as-G and the worked w=2/3 example. |
| 4 | Sharp-forcing soundness | Holds as a sandwich on integerized AF2 floors. Extra-unit step is correctly CONJECTURE; Prop. 7.3 does not give it. |
| 5 | Hidden unproven assumptions (higher-jet / coefficient compatibility) | Not hidden. Independent A_v / St 3.9 gluing is labeled CONJECTURE and placed outside DEPTH's coefficient-layer exclusion. |

The cell is a demonstrated survivor at the stated Prop. 9.3 transport + vertex-local T1 tier. It is not a global lift, and the note does not claim one.
