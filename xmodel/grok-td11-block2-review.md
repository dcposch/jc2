**VERDICT: SOUND-WITH-ERRATA — NF-Z† DIE-horn and Lemma M1 hold identically; the two B-zero handshakes self-refuse by the general den-criterion (not Lemma CAP-DEN's X-family); the 21 windowed-out (B,B) stamps are not death certificates (outer merge unanalyzed) and the 3 BB2 M=1 rows hide discrete alternatives, so “all 67 DEAD-AT-TIER” is not earned.**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-14.
Targets: `NF-Z.md` §6 (round-6 addendum) + `TOWER-TD11.md` §§15–17; `NF-M.md` (core + §5); `cases/nfm_check.py`, `cases/tower_td11.py`.
Three results, dependency order: (1) NF-Z† instantiation — multi-word families CLOSED at all 3 entries by deep-gap-halving + the c=3 sweep at 11-B; (2) NF-M core — square-system reduction, Lemma M1 identically, Bézout `(Q̂−1)!`, future-locality on 0-dim types, fail-closed OB1; (3) the 67-row sweep — 31 unrealizable + 21 windowed-out + 15 self-refused, and the three in-window merged emissions dying at their own vertex via CAP-DEN.
Method: line-read of the three prose claims against `sol-normalform.md` §2.2, `TOWER-TD11.md` §7.4 Lemma CAP-DEN, and the 145-row expander. Independent exact `Fraction` replay of the all-`u_min` census (brute mixed words included), of the c=3 / 5/4 lattices, of M1 as an algebraic identity (not the B1 sample), of homogeneity of the `x^j` coefficients, of both B-zero square solves, of all three self-refusals on the `{1,2}` and `{1,2,4}` lattices, and of the 67 live rows with inner `M_G` stored. Spot-check 5 of the 31 and 5 of the 21 against explicit decorations. Gates: `python3 cases/nfm_check.py` exit 0, **18/18**; `python3 cases/tower_td11.py` exit 0, **66/66** (121 s); `python3 cases/nfd_check.py` exit 0, **22/22**; `python3 cases/nfz_check.py` exit 0, **39/39**. No other repo file modified. No git.

---

## Result 1 — NF-Z† DIE-horn (`NF-Z.md` §6 + `TOWER-TD11.md` §15)

### 1. Severity: clear — the halving census is exact, and no pure-neutral coupling object at gap `≥ 1/2` exists besides X

- File: `TOWER-TD11.md:601-611,628-633`; `cases/tower_td11.py:816-840`; letter domain `TOWER-TD11.md:50-64`; cylinder `(2.5)` at `sol-normalform.md:254-265`
- Claim: max gap of a depth-`d` neutral letter is `(u_min+1)/(P_0 u_min^d)`, which at least halves per depth; the only objects at gap `≥ 1/2` are the depth-1 chain-1 letters (X itself). Opponent maxima `3/8`, `1/5`, `3/10`.
- How checked.

  **Domain `u_min` matches the claimed table**, independently from `gcd(a,u)=1` and `d | u+1`:

  | chain | `w` | `P_0` | legal `u` (first) | claimed `u_min` |
  |---|---|---:|---|---:|
  | 11-A/C ch-1 | 2 | 2 | 3,5,7,… | 3 |
  | 11-A ch-2 | 3 | 4 | 2,4,5,7,… | 2 |
  | 11-B ch-1 | 3 | 2 | 2,4,5,7,… | 2 |
  | 11-B ch-2 | 4/3 | 6 | 5,11,17,… | 5 |
  | 11-C ch-2 | 3/2 | 4 | 5,7,11,… | 5 |

  **All-`u_min` is the genuine maximum.** `γ_d = (u_d+1)/(P_0 u_1⋯u_d) = 1/(P_0 · (∏_{i<d} u_i) · u_d/(u_d+1))`. The factor `u/(u+1)` is increasing, so the last letter is minimised at `u_min`; the prefix product is minimised at all-`u_min`. Brute `itertools.product` over legal letters `≤ 20` at depths 1, 2, 3 on every chain: brute max equals the formula, and the maximiser is the all-`u_min` word. Zero mixed words at depth `≥ 2` have gap `≥ 1/2`.

  **Halving is `1/u_min`, not a slogan.** `max(d+1)/max(d) = 1/u_min ∈ {1/2, 1/3, 1/5}`. The prose “at least halves” is the `u_min=2` case; the other chains decay faster.

  **Depth-1 values replay the scope menus exactly:** chain-1 gives `2/3` (11-A/C, `ν=3`) and `3/4` (11-B, `ν=2`) — these *are* X; opponents give `3/8`, `1/5`, `3/10`. Depth 2 is already `2/9`, `3/8`, `3/16`, `1/25`, `3/50`, all `< 1/2`.

- Coupling hunt (what the census could miss).

  | candidate | reaches `≥ 1/2`? | in the DIE-horn class? |
  |---|---|---|
  | mixed-letter depth `≥ 2` | **no** (brute) | yes |
  | one-step charged menus | only 11-A `5/8` and 11-B `5/4` | no — DG2 dispatches both |
  | two opponent words coupling at `3/10` | no, `3/10 < 1/2 < gap(X)` | yes, but after X |
  | a letter that *shrinks* `P` then a later large gap | `(2.5)` has `P'=Pu`; `(2.6)` has `ε+lu ≥ ε+2l > l` so `P` grows; resonance `4→8` grows | would be charged / NF-P |
  | `ν=1` rescaling | out of cylinder | NF-P, already a rider |
  | simultaneous sibling-X tie | opponent max `< 1/2 <` every X | no tie |
  | cap-shrink producing a new prime | `gcd(c,e) | c`, so the divisor closures `{1,2,4}`, `{1,2,3,6}`, `{1,2}` are complete | DG3 |

  No pure-neutral coupling pattern at gap `≥ 1/2` was found. The DIE-horn does not need a general cross-branch algorithm: X is first among remaining vertices and is already refused. That is exactly the “finite because the kill precedes coupling” honesty of DG6, and it is correctly scoped to *clashed* entries.

### 2. Severity: clear — the c=3 sweep is a real find and has zero escapes

- File: `TOWER-TD11.md:615-622`; `cases/tower_td11.py:847-869`; Lemma CAP-DEN `TOWER-TD11.md:241-254`
- Claim: cross-branch coupling shrinks 11-B’s cap to `gcd(6,e)`, hence 3 must be swept; `3`-free `ν | 9` is empty; resonant `5/4` dens `{4,12} ∤ 3`.
- How checked.

  **Necessary condition is sharp.** `ν | c² = 9` forces `ν ∈ {1,3,9}`. Domain `3 ∤ ν` at `w=3` removes 3 and 9; `ν=1` is outside every X-interval. The 3-free slice of `ν | 9` is empty — this is the algebraic closure, not a lattice accident.

  **Direct den-criterion, third and sixth lattices, `ν ≤ 400` plus `5/4`:** zero triples `(c, α, g)` with `r = α−1+g > 0` and `den(r) | 3`. Resonant dens:

  | lattice | dens of `α − 1 + 5/4` | divides 3? |
  |---|---|---|
  | `a/3` | `{4,12}` | no |
  | `a/6` | `{4,12}` | no |
  | `a/2` | `{4}` | no |

  The stronger identity “some residue has `den | c` iff `2ν | c(ν+1)`” fails only at the irrelevant cell `(c,ν)=(1,1)` (where `r ≤ 0`). On 11-B’s live set it holds.

  Rounds 2–5 really did omit `c=3`. Adding it is the right divisor-completion, and it does not create an escape.

### 3. Severity: residual — DG4/DG5 are not machine content

- File: `cases/tower_td11.py:870-888`
- `DG4` checks `gcd(c,e) | c`, which is the definition of gcd. `DG5` is `True and ok3`. The DIE-horn verdict is the conjunction of DG1–DG3 (which do constrain arithmetic) plus the monotone-shrink observation (which is a one-line lemma, not a gate). Do not count DG4/DG5 toward the 66.

**Result-1 residual risk, not a break.** The dagger is a *pure-neutral* statement. Charged descendants beyond the exact-core (already OPEN in §12(iii) / §13.0) can in principle grow a vertex with gap `≥ 1/2` that is not X; that is a different clause and is not smuggled into DG5.

---

## Result 2 — NF-M core (`NF-M.md` §§1–4)

### 4. Severity: clear — Lemma M1 is identical, not a sample. The B1 lattice is confirmatory.

- File: `NF-M.md:75-84`; `cases/nfm_check.py:186-201`; degree law `(2.7)` at `sol-normalform.md:299-307`
- Claim: the `x^{Q̂}` coefficient of `F` vanishes identically — the Fuchs degree identity `d_p d_q − d_q d_p = 0` — for every admissible decoration.
- How checked. The written proof is already an identity on the definitions

  ```
  d_p = ε + ν Σ p_i f_i,     d_q = 1 + ν Q̂,
  lead(F) = (d_p − d_q ε) + ν (d_p Q̂ − d_q Σ p_i f_i)
          = d_p (1 + ν Q̂) − d_q (ε + ν Σ p_i f_i)
          = d_p d_q − d_q d_p = 0,
  ```

  using only that `G` and every `F_i` are monic (so `lead((G/F_i) F_i') = f_i`). This does not mention the specific polynomials, the split/unsplit distinction, the extras, or the value of `ν`. It holds for *every* monic decoration.

  **Off-lattice confirmation (not the gate’s B1 rectangle).** Closed-form `lead(F)` on `ε ∈ 0..8`, `ν ∈ 2..20`, eleven mult/block signatures including cubic and mixed, extras `0..5`: **11,286 trials, 0 failures.** `Fsys` numeric leading on decorations the gate never sees (`ν ∈ {11,13,17,19,23,29}`, `ε ∈ {4,5,6,7,8}`, cubic/quartic blocks, quadratic extras, four extras): **240 trials, 0 failures.** Empty schema `Q̂=0` gives `F={}`, consistent with `deg ≤ −1` being vacuous.

  B1’s “full lattice” is `ε ∈ {0,1,2,3} × ν ∈ {2,3,5,7} ×` five mult-vectors × two block-degree patterns × extras `0,1,2`. That is a sample. The *lemma* is not. The likeliest overclaim (“identically means for all admissible decorations”) is true, and the gate undersells the proof by sampling it.

  The only hypothesis is that `(2.7)` really is `d_p` and `d_q`. That is R2.2: `p = η^ε Π F_i(x)^{p_i}`, `q = η · Π F_i · Π G_r`, `x=η^ν`. Unsplit blocks are included (`f_i = deg F_i`). Shared roots between an extra and an `F_i` do not break monicity or the division `G/F_i`.

### 5. Severity: residual — B2 is a tautology. Bézout itself is the right bound.

- File: `NF-M.md:86-93`; `cases/nfm_check.py:202-206`
- The gate is

  ```
  all((Qh - 1) == (Qh - 1) for Qh in range(1, 6)) and [1, 1, 2, 6] == [1, 1, 2, 6]
  ```

  That does not touch `Fsys`. It would pass if the `x^j` equation had degree 17.

  **The mathematics is still correct.** Root-scaling `a_i ↦ 2 a_i` on split schemas `Q ∈ {1,2,3,4,5}` (30 random points each) and on mixed unequal-mult / extra configurations (F2, G-row, cylinder, four-orbit): the coefficient of `x^j` scales as `2^{Q−j}` in every case. So the `x^j` equation is homogeneous of degree `Q̂−j`. Projective Bézout on `Q̂−1` equations of degrees `1,2,…,Q̂−1` is `(Q̂−1)!`, as an *upper* bound on isolated points (infinity and non-reduced structure only shrink the isolated count). Unsplit blocks have *fewer* free coefficients than the split picture; the bound still dominates.

  Observed types sit far below the bound (every td-7 `t1_local` row has exactly one type; both B-zero schemas have one; the cylinder is one type per `ν`). Fail-closed OB1 correctly refuses to quotient a positive-dimensional component; none was observed, and the cylinder’s free `g_0` is the scaling parameter (`x^r + g_0` is one orbit of `η ↦ λη`).

### 6. Severity: clear — M3 is a covariance argument, not a computation, and is scoped

- File: `NF-M.md:108-122,214-220`
- Two solutions of the same 0-dimensional type differ by permutation × scaling. Scaling is the chart change `η ↦ λη`, under which L1–L9 are written to be covariant; equal-multiplicity permutation is a slot relabelling. That needs the 0-dim hypothesis (inside a positive-dimensional component a later edge can see the extra parameter — this is why OB1 retains the component). The consumer list is flagged: a later edge that reads coefficient data outside `(frame, degrees, C, L9 orbit values)` re-opens M3. Honest.

  H4 (`nfm_check.py:551-558`) is `True and len(AB_MENU)==2` — a rider restated as a gate. Same class as DG5.

**Result-2 status.** The square-system reduction (M1+M2+Bézout+M3+OB1) is proved. The core does not depend on the 67-row execution.

---

## Result 3 — the 67-row sweep and the three self-refusals (`NF-M.md` §5)

### 7. Severity: erratum — the 21 DEAD-WINDOWED-OUT stamps are not death certificates. They are all `(B,B)` inner merges whose vertex sits below `1/2`, after which the OUTER merge with A is unanalyzed.

- File: `NF-M.md:173-196,669`; `cases/nfm_check.py:507-550`; composition perimeter `TOWER-TD11.md:323-336,656-662`
- Claim: 21 rows die because every matching schema’s merged vertex sits below `1/2`.
- How checked.

  **The 31/21/15 split matches the actual 67 live rows** once inner `M_G` is stored (the 145-layer already splits on `(M_G, μ_e)`; the synthetic `ROWS67` is not a fiction):

  | flavour | inner `(μ, M_G)` | n | stamp reason |
  |---|---|---:|---|
  | `G(G(A,B*),B*)` ×2 | `(1,2), 1` | 6+6=12 | in-window AB schemas, self-refused |
  | `G(G(A,B*),B*)` ×2 | `(1,2), 3` | 14+14=28 | no AB schema with `M=3` |
  | `G(G(B1,B2),A)` | `(1,1), 1` | 3 | no BB1 schema with `M=1` |
  | `G(G(B1,B2),A)` | `(1,1), 2` | 6 | BB1 schema gap `1/10` |
  | `G(G(B1,B2),A)` | `(2,2), 1` | 3 | cylinder (and two discrete `M=1` schemas) |
  | `G(G(B1,B2),A)` | `(2,2), 2` | 6 | gaps `2/13`, `5/28` |
  | `G(G(B1,B2),A)` | `(2,2), 4` | 9 | gaps `1/10`, `1/10` |
  | | | **67** | |

  All 21 windowed-out rows are `(B,B)` inners. There is no A-pole in the inner chart, so “vertex below `1/2` ⇒ X dies first ⇒ CAP-DEN” is the *completed* 3-pole’s clash, not the inner 2-pole’s.

  **That completed-object clash is exactly the undischarged OB-8 nested obligation.** `TOWER-TD11.md:333-336` says nested `G(G(B1,B2),A)` makes “the opponent a merged chart whose post-merge menu is NF-M-gated,” and §16 says the 67 “need the merged-emission law first.” The gate then stamps DEAD-WINDOWED from the *inner* `(κ̄, d_p)` alone, with no outer handshake, no emitted `w_G`, no outer `(2.9)`.

  Inner vertex `< 1/2` means the inner chart is *not* self-killed. It is a live arrival at the outer merge with A. The outer merge emits a new vertex whose gap is a new computation. If that gap is `> 1/2` and its death step is legal, the row is not dead; if the gap is `< 1/2`, the completed object may die at X — but that is a composition lemma this round was written to supply and did not.

  The rider “merged-chart descendant strata stay in the standing perimeter” (`NF-M.md:198-203`) names *post-merge P0 expansion*, not the outer merge that is already a node of the row’s own tree. H3 prints `0 DEFERRED` and has a `DEFER` stamp it never uses. The honest stamp for these 21 is `DEFERRED` / `OPEN` at the outer-merge obligation.

  Spot-check of the five windowed *gaps* (the arithmetic is right; the death is not):

  | # | decoration (live row) | schema | `i_G` | gap |
  |---|---|---|---:|---|
  | W1 | BB1 `μ=(1,1)`, `M_G=2`, `μ_out=(1,1)`, `M_root=1` | `ν=5, ε=0, x=1, (10,16)` | 4 | `4/(4·10)=1/10` |
  | W2 | BB2 `μ=(2,2)`, `M_G=2`, `μ_out=(1,1)`, `M_root=1` | `ν=5, ε=1, m_j=(1,), (26,16)` | 2 | `8/(2·26)=2/13` |
  | W3 | same flavour, `M_root=2`, interior | `ν=3, ε=2, m_j=(1,1), (14,10)` | 2 | `5/(2·14)=5/28` |
  | W4 | BB2 `M_G=4`, `M_root=1` | `ν=5, ε=0, (20,16)` | 2 | `4/(2·20)=1/10` |
  | W5 | BB2 `M_G=4`, `M_root=2`, interior | `ν=3, ε=2, m_j=(1^4), (20,16)` | 2 | `1/10` |

  All five sit below `1/2`. None of the five has an outer-merge menu.

### 8. Severity: erratum — Lemma CAP-DEN’s hypothesis is the X-family. The three self-refusals use the general den-criterion. For the two B-zero handshakes that is legitimate. For the cylinder the name is a wrong-vertex-class citation; the arithmetic still refuses.

- File: Lemma CAP-DEN `TOWER-TD11.md:241-254`; self-refusal `NF-M.md:180-189`; `cases/nfm_check.py:479-504`; death equation `TOWER-TD11.md:238-239`; “`k | 2` while X is alive” `TOWER-TD11.md:217-220`
- Claim: the three in-window emissions die at their own merged vertex via CAP-DEN, over the 11-C caps `{1,2}`.
- Circularity check, as requested.

  **These gaps are not X-family.** `gap(X)=(ν+1)/(2ν)` inverted:

  | object | gap | would-be `ν` | integer `≥ 2`? |
  |---|---|---|---|
  | B-zero `ν_e=3` | `7/10` | `5/2` | no |
  | B-zero `ν_e=4` | `5/4` | `2/3` | no |
  | cylinder `ν=2` | `5/6` | `3/2` | no |
  | cylinder `ν=3` | `21/26` | `13/8` | no |

  Lemma CAP-DEN (the `ν | c²` closure) does **not** apply. What is applied is the *general* den-criterion `k = den(α − 1 + g)`, which is the ladder death equation `ℓ/k = α − 1 + g` (Z1) for an arbitrary vertex, together with caps `{1,2}`.

  **“Killed by the arithmetic of its own death step” is not circular.** The merge exists (square system solves, unique type, `C ≠ 0` for the B-zeros, `b=−a` for the cylinder). The configuration then has a vertex `G` of that gap. `G` must die, and dies first (`7/10 − 2/3 = 1/30`; `5/4 > 2/3`; cylinder `∈ (3/4, 5/6]`, limit `3/4 > 2/3`; no odd `ν_X` has `gap(X) ≥ 7/10`). The forced `k` divides no cap. Contradiction. That is the same shape as the X-refusal, and it is a legitimate impossibility certificate **provided** the death equation, the register lattice, and the cap are the ones that belong to this vertex.

  **Where the cap comes from.** `i_G` is recovered from `deg(p_e) = i_G · μ_e`: AB live has `deg(p_A)=2=i_G·1` and `deg(p_B)=4=i_G·2`, so `i_G=2`; BB2 has `μ=2`, `deg=4`, `i_G=2`; BB1 has `μ=1`, `deg=4`, `i_G=4`. Gap is `κ̄/(i_G d_p)`. When `G` dies, `k | i_G`. Additional live vertices only shrink the cap. Using `{1,2}` at `i_G=2` is the conservative (largest) cap for a kill.

  **Wrong cap, exhibited.** If one illicitly took the cap to be `X_G` or `d_p` (the surplus / the whole `p`-degree — a different vertex class):

  | object | illicit cap | at `α=3/2` | verdict |
  |---|---|---|---|
  | `7/10` | 5 (`X_G=d_p`) | `r=6/5`, `k=5`, `5 | 5` | **LIVE** |
  | `5/4` | 4 or 8 (`d_p` or `X_G`) | `r=7/4`, `k=4`, `4 | 4` | **LIVE** |

  Those are the escapes a referee gets by applying CAP-DEN’s *conclusion* with the merge’s own degree as if it were the X-exponent. They are not live under `k | i_G=2`.

  **The two B-zero handshakes are legitimate.** Inner merge is `G(A,B)`: X is present, still alive (`gap(G) > gap(X)`), so `k | 2` while X is alive (Prop. 4.2(iii), cited) *and* `k | i_G=2`. The register starts at `α_1=3/2` and prefix steps with `k | 2` stay on the half-integral lattice (OB7a). Independent replay:

  | object | `α=3/2` | `r` | `den` | `den | 2`? | full `{1,2}`-lattice |
  |---|---|---|---:|---|---|
  | `7/10` | yes | `6/5` | 5 | no | dens `{5}` only; refused |
  | `5/4` | yes | `7/4` | 4 | no | dens `{4}`; refused |

  Quarter-register cells `α ∈ {1/4, 3/4}` *would* let `5/4` escape (`r=1/2` and `r=1`). They are the ledger-row-5 shape. 11-C has no cap 4, and `k | 2` cannot produce `den(α)=4`. Excluded, entry-paired, as in OB7g.

  Square solves, independently: unique ratios `q=(2/5)a` (`κ̄=7`) and `q=a/4` (`κ̄=10`), `C ≠ 0`, one type each, `≤ (2−1)!`. Cylinder `b=−a` for every `ν=2..29`.

  **The cylinder is the wrong-name case, not a live escape.** The inner chart is `(B,B)`: no A, no X, no 11-C `α_1=3/2`. Citing “CAP-DEN over the divisor-complete 11-C caps `{1,2}`” applies an X-side lemma to a vertex class that does not carry X. The *own-exponent* cap is still `i_G=2`. Sweeping `{1,2,4}` (B-pole residual) and lattices `den | 4`, `ν=2..200`: **zero escapes.** The odd-factor law `(4ν+1)/gcd(4ν+1,3) ≥ 3` odd holds on `ν=2..500`; at `α=3/2` one has the closed form `r=(5ν+2)/(4ν+1)`, whose denominator never divides 2 or 4. The only register that produces an escape shape is `α=2/3` at `ν=2` (`r=1/2`, `k=2 | 2`) — and `den(2/3)=3` lies on neither the `i_G=2` lattice nor the B-pole `den | 4` lattice. Spurious.

  So: the cylinder *dies* by the general den-criterion at `k | i_G=2`. It does *not* die by Lemma CAP-DEN. Write the den-criterion, not the X-lemma. The “own death step” is legitimate once the vertex class is named correctly.

### 9. Severity: erratum — the 3 BB2 `M_in=1` rows are stamped DEAD-SELF-REFUSED because the cylinder is in-window; they also carry two discrete `M=1` schemas at gap `7/22`

- File: `cases/nfm_check.py:532-540`; menu `nfm_check.py:441-446`
- H3’s rule is: if *any* matching object is in-window, stamp SELFREF. For `kind=BB2` and `Min=1` it then appends the cylinder family even when the discrete `mine` list is entirely windowed-out.

  Discrete `M=1` schemas (menu-complete, see finding 10): `(ν,ε,m_j,κ̄,d_p,d_q) = (2,1,(1,),7,11,7)` and `(3,2,(1,),7,11,7)`, both gap `7/(2·11)=7/22 < 1/2`. The three live decorations are

  ```
  μ_out=(1,1), M_root=1, interior=False
  μ_out=(1,1), M_root=2, interior=True
  μ_out=(1,1), M_root=2, interior=False
  ```

  A compiler that realises the discrete schema, not the cylinder, has an inner vertex below `1/2` and falls into finding 7 (outer merge unanalyzed). Stamping the *row* dead because a *sibling schema* self-refuses is a disjunction error. Split the stamp, or kill the discrete alternatives by an outer-merge argument that does not exist.

### 10. Severity: clear — the 31 unrealizable stamps are earned. Menu complete. Five spot-checks.

- File: `NF-M.md:163-178,191-196`; enumerator `nfm_check.py:340-411`; `(2.8)–(2.11)` at `sol-normalform.md:316-365`
- Independent enumerator, bounds strictly larger than the gate (`ν_e ≤ 40`, `x ≤ 20`, `k ≤ 8`, `ν ≤ 200`):

  **`(A,B)`.** Both-nonzero pins `(κ̄,X)=(1,−1)`. A-zero gives `κ̄=3−2ν_e ≤ −1`. B-zero with no NE (forced: `m_j < min μ_e = 1`) produces **exactly two** schemas, the claimed pair; `ν_e=2` dies on MP6 (`M=5 ∤ 3`). No third schema out to `ν_e=40`.

  **`(B,B)`, `μ=1`.** Exactly one discrete schema `(ν=5, x=1, κ̄=4, (10,16), M=2)`. The `C=0` position is the both-nonzero cylinder `κ̄=3(1+2ν)/2`, odd numerator, parity-dead. No `M=1` schema.

  **`(B,B)`, `μ=2`.** Exactly the six claimed discrete schemas, all windowed, plus exactly two `C=0` shapes: `ε=0` is again parity-dead; `ε=1` is the claimed cylinder `κ̄=6ν+3`, `(4ν+1, 2ν+1)`, `M=1`.

  Spot-check, five unrealizable decorations (all live after inner-H8, no matching `ν≥2` schema):

  | # | row | why unrealizable |
  |---|---|---|
  | U1 | AB1, `μ_out=(1,1)`, `M_root=1`, `M_G=3` | AB menu `M ∈ {1}` |
  | U2 | AB1, `μ_out=(1,1)`, `M_root=2`, interior, `M_G=3` | same |
  | U3 | AB1, `μ_out=(1,1)`, `M_root=2`, not interior, `M_G=3` | same |
  | U4 | AB1, `μ_out=(1,2)`, `M_root=1`, `M_G=3` | same; MP6 would *allow* `M=3 | 3` — the hole is `(2.9)`, not MP6 |
  | U5 | BB, `μ=(1,1)`, `M_G=1`, `μ_out=(1,1)`, `M_root=1` | BB1 menu `M ∈ {2}`; `μ=1` cylinder parity-dead |

  The 28 A-flavour `M_G=3` rows plus the 3 BB1 `M_G=1` rows are exactly the 31. No missed schema resurrects any of them. Conditional rider on the B-zero handshakes stands: if the refile realises neither `ν_e ∈ {3,4}`, those 12 self-refused AB rows become unrealizable instead. Dead either way.

---

## What the block actually delivers

| result | advertised | earned |
|---|---|---|
| NF-Z† at td-11 | two-word deep families CLOSED, all 3 entries | **yes**, on the pure-neutral class; DIE-horn, not a general algorithm |
| NF-M core | square system, M1 identical, Bézout, M3, OB1 | **yes**; B2/H4/DG5 are non-gates |
| 31 unrealizable | no `ν≥2` schema matches `M_in` | **yes**; menus complete |
| 12 AB self-refused | in-window B-zero emissions die at `G` | **yes**, by the *general* den-criterion + `k | i_G=2` (X present). Not by Lemma CAP-DEN |
| 3 cylinder / BB2 `M=1` | parametric family dies at `G` via CAP-DEN | cylinder arithmetic **refuses** at `k | i_G=2`; the *name* is a wrong-vertex-class citation; the 3 *rows* also carry discrete `7/22` alternatives |
| 21 windowed-out | merged vertex `< 1/2` ⇒ DEAD | **no**; all `(B,B)`, outer merge with A unanalyzed, OB-8 smuggled back in |
| “67 nested rows CLOSED-AT-TIER” | `TOWER-TD11.md:669` | **43 earned** (31+12), **24 not earned** as death certificates (21+3) |

Suggested errata, in order:

1. Relabel the 21 as `DEFERRED` / `OPEN` at the outer-merge obligation. Do not cite TD11-CLASH (direct hierarchies only) for `G(G(B1,B2),A)`.
2. Split the 3 BB2 `M=1` rows by schema: cylinder = self-refused (den-criterion, `k | i_G=2`); discrete `(11,7)` = same deferral as the 21.
3. In `NF-M.md:184-189` and `TOWER-TD11.md:669`, replace “CAP-DEN-refused” by “den-criterion refused at `k | i_G=2`”. Reserve Lemma CAP-DEN for the X-family `ν | c²` closure. State that the two B-zero objects additionally have X alive, so Prop. 4.2(iii) independently gives the same cap.
4. Delete or replace the tautological gates B2, H4, DG4, DG5.

On the objects that were honestly checked — the DIE-horn census, the c=3 completion, M1 as an identity, the two B-zero charts as standalone 2-pole objects, and the 31 missing schemas — the mathematics stands. The round-8 slogan that the 129 nested rows are closed at tier does not.

Machine gates: `nfm_check.py` 18/18, `tower_td11.py` 66/66, `nfd_check.py` 22/22, `nfz_check.py` 39/39, all exit 0. Companion `tower_check.py` not rerun. No git commit.
