# Hostile adjudication: Roy van Rijn (`royvanrijn/jacobian-research`)

Adjudicator: Grok 4.6 (hostile, external-actor tier). Date: 2026-08-22.
Charge: today's sweep delta 1 (`xmodel/websweep-2026-08-22.md`). Read what is needed; write only this file. No git.

Actor: Roy van Rijn, GitHub `royvanrijn/jacobian-research` ("Vibing verifiable math").
Created 2026-07-20T16:57Z (Alpöge-announcement day). Pushed 2026-08-23T04:08Z. 5 stars, ~5,895 files, currently also on an Elkies/Q80 lane. Cites Helali and GGHV; never us, never Eiki Suzuki, never Strinz, never Ishihara, never Palomar, never vertex-gap.

Read: the cloned HEAD at `/tmp/royvanrijn-jacobian-research` (shallow clone of `main`); the (72,108) closure / Prop 4.3 audit / Helali provenance / Case-2 syzygy notes; the HC4 Wronskian, shared-boundary, Schur-descent, and relative-nilpotent master notes; the F2 (75,125) derivation / classifier / forcing notes; `STATUS.md` rows that name those objects. Compared against paper1, `CROSSCHECK.md`, `AUDIT.md`, `hc4-adjudication.md`, `APPROACHES.md` row 10, `FACE-ISOLATION.md`, race doctrine in `notes.md`. Executable check: his `plane-jc/cas/verify_prop43_exhaustiveness.py` was run here and printed `PROP43_EXHAUSTIVENESS_AUDIT_PASS`. The Case-1 `RANKDROP_EXACT_UNIT_PASS` Singular identity was **not** re-run (needs Helali pkl + Singular). No coefficient-level replay of the HC4 master theorem or the F2 live block.

---

## VERDICT

**Collaboration, not threat, not irrelevant.** Fourth independent replication line for the *conditional* (72,108) exclusion; first public actor to replace Helali's 89 MB Case-1 identity by a small determinantal two-generator statement; first public finite census of the abbreviated Prop 4.3 tail. Same conditionality we flag. Does **not** scoop, contradict, or subsume the promoted vertex-gap theorem. Independently executing APPROACHES row 10 at a depth our campaign has not tried, and has seen two real things the Aug-21 HC4 adjudication did not write down — neither of which repairs the structural discount. His (75,125) F2 programme is the public post-125 frontier, complementary to our sheet-6 endgame, with an uncrosswalked disagreement versus Strinz, and no tripwire on unpublished campaign objects.

Recommended posture: **coordinated-note / citation-courtesy tier, DC decides outreach.** Cite by merit (Prop 4.3 exhaustiveness audit; Case-1 `(h,N)` lemma; 5-dessin first-block if used). Credit Helali first, as he does. Do not treat his Aug-1 "closure" as a theorem of JC2. Daily-watch the repo. Do not start an HC4 case-tree without first replaying his Wronskian-unit argument and his isotropic Schur recognition, and do not open a (75,125) stake just because the window is crowded.

---

## 0. Actor, in one paragraph

This is a high-volume AI-math shop, not a specialist JC2 campaign. The root README is a dim-3 Keller / marked-root / moment-Prony / GMC / elliptic-rank programme; `plane-jc/` and a forest of `HC4_*.md` files are two among many lanes. Named-theorem inflation is the house style (`HC4RSD1`–`80`, then a "master" `HC4-MR` that confesses it has neither end-to-end replay nor external review). That mill-texture is a credibility tax, not a dismissal: the (72,108) subdirectory is the most carefully firewalled object in the repo, and the firewall is honest.

---

## 1. The (72,108) determinantal-closure claim

### 1.1 What he actually claims (not the sweep paraphrase)

`plane-jc/JC2_72_108_DETERMINANTAL_CLOSURE.md`, last authored commit `f0aad99b` **2026-08-01**, "Close the JC(2) (72,108) certificate gaps (#20)":

> The two Laurent systems in GGHV Proposition 4.3 are inconsistent over characteristic zero.
>
> Consequently, **assuming the published general GGV/GGHV reduction and degree classification**, the degree pair `(72,108)` (and its swap) is excluded and the published frontier becomes `125`. This is not a proof of the planar Jacobian conjecture, and it is not a from-scratch reproof of the general theorem ladder or of the earlier admissible-chain census.

Companion `PAIR_72_108_REPRODUCTION.md` classifies every section as **external reduction / local reproduction / repository interpretation**, and its final section "makes no theorem claim". `DEGREE_FRONTIER_125.md` quotes Helali's theorem *verbatim* as an exclusion of two transcribed systems, then writes the 125-bound as a corollary still conditional on Prop 4.3 exhaustiveness and faithful transcription. Provenance pins Zenodo 21479814 / Helali commit `d9ea4fd`, same 89,105,967-byte hard certificate SHA-256 `0e48ffab…656a` that `CROSSCHECK.md` replayed.

He is not claiming a new (72,108) theorem. He is claiming a *structural reconstruction* of Helali's already-claimed exclusion, plus a case-specific front-end audit of Prop 4.3.

New content, as he lists it:

1. finite Newton-tail census from the live corner `(24,7)` to exactly the two corrected Laurent polygons, including the printed `(0,1)` → `(8,14)` typo;
2. first Wronskian block descends to an intrinsic `μ_7` quotient (`Q[q]/(H_5(q))`) before elimination — the degree-35 field is a rank-seven pullback of a degree-five quotient;
3. Case 2 packaged as a binary-octic complete intersection `(N_7,N_9)` of Hilbert vector `1..8..1` (length 64) plus an origin Bézout identity;
4. Case-1 hard ideal proved equal to `(h,N)` by a two-generator determinantal lemma, replacing the 89 MB membership dump.

### 1.2 Is the conditionality the same Prop-4.3 conditionality we flag?

**Yes. Same arrow, same trusted-external input, same honest scope.**

`AUDIT.md` Claim 8.1: GGV Prop 4.3 itself is the trust boundary, "parts of the supporting chain (1401.1784 / 1605.09430 / 1406.0886 / 1708.07936 / 2204.14178) are arXiv-only/unrefereed". Paper1 §computation: "That claim is conditional on Proposition 4.3 itself; [GGV2,GGV3,GGV4,GGHV] are arXiv-only". `CROSSCHECK.md` bottom line: both Helali and Suzuki exclude (72,108) "conditional on Prop 4.3". Roy's boxed sentence is the same sentence.

Two differences of *hygiene*, not of logic:

- He actually *fills* the two finite arithmetic steps Prop 4.3 abbreviates ("as in Proposition 4.1"; "would have no way of being parallel"). That is exactly the interface we listed as remaining (`AUDIT.md` "the Prop-4.3-to-emit.py polygon transcription has no check against the paper other than eyes"). His checker is stdlib-only. **Replayed here: `PROP43_EXHAUSTIVENESS_AUDIT_PASS`.** Census table, `k=2` exclusion, collinear-nonvertex collapse of `(17,5),(10,3),(3,1)`, monomial map `T(i,j)=(-i+4j,j)`, and the `(0,1)` typo all match the polygons we, Helali, and Suzuki already use. This is a genuine complement to our record, not a restatement.
- He vendors Helali and does **not** cite Eiki Suzuki (Zenodo 21483636), whose 5-dessin top-edge classification he independently reconstructs (`JC2_72_108_BELYI_DEFORMATION_CLOSURE.md`, passport `(2^{10},1)|(3^7)|(17,1^4)`, five conjugate Belyi maps over one irreducible quintic, Galois closure `S_5`). That passport is Suzuki's. Citation courtesy toward Helali is his; toward Suzuki it is missing. Ours is the only public three-way (Helali/Suzuki/Generator A) transcription agreement.

### 1.3 Overlap / contradict / complement versus the promoted record

| Our promoted object | Relation |
|---|---|
| **Paper1 vertex-gap theorem** (unconditional strip-pair obstruction; `(k,d_2)=(2,2)` empties the generic chart; main theorem is the residue functional `R_{k,d_2}` on the depth-two block, every cell `k,d_2≥2` in char 0) | **No overlap of theorems.** Vertex-gap is a geometric mechanism for *strip* pairs. Roy has no vertex-gap, no gap-kill, no `R_{k,d_2}`, no strip-ODE rigidity lemma. His Case 2 is still coefficient algebra (binary octics + unit identity). Paper1 §coverage already states that Prop 4.3 subcase (1) is *outside* vertex-gap because of `y`-axis support `(0,8)/(0,12)`. He does not contradict a theorem he does not touch. Application of vertex-gap to `(8,28)` still inherits Prop 4.3; so does his closure. Complementary mechanisms for the *same* subcase (2). |
| **CROSSCHECK / Helali+Suzuki replay / companion (72,108) emptiness claim** | **Overlap of conclusion, complement of method.** Same two polygons, same `t=xy^2`, `z=y^{-1}`, same `J4`–`J0` bands, same lattice counts (61+125 / 25+47), same `K_0` of degree 35 and same quintic `L=Q[w]/(w^5-w^4+3w^3+3w^2+26)`, same `s=±c` split, same `E_6-λ E_2 = S Λ^2` with `λ=±13/9`, same involution `(h,u_1,u_2)↦(h,-u_1,-u_2)`. He is a **fourth** replication line (Helali, Suzuki, our audited s2/c1, Roy), not a first. The new piece is Case-1 opacity: Helali's 89 MB identity `h=Σ T_i F_i` is replaced by the ring-theoretic lemma `I=(h,N)` once `(m_{12},m_{23},m_{34},F_1)=(1)` and the special fibre `(a_i)` is unit modulo `h`. The lemma is standard and correct as algebra (syzygies `a_i F_j - a_j F_i = h m_{ij}`; multiply a unit identity in minors-plus-`F_k` by `h`). Whether Helali's actual `F_i` satisfy the minor-unit hypothesis is the computational claim I did **not** re-run. |
| **AUDIT.md subcase (2) emptiness over char 0** | Complements. Our generic chart dies by the ten-event chain ending in `-1=0` (vertex-gap); remaining strata `cCa2/cCa6` by Gröbner. His Case 2 is a *global* unit-ideal packaging of Helali's four-generator identity, which already covered all charts. No disagreement of verdicts. |
| **Bound 125 as a public statement** | Same conditional shape, Helali-priority. He does not scoop us: Helali 2026-07-21, Suzuki 07-22, Roy reconstruction 08-01, our CROSSCHECK 08-04, paper1 isolates a *different* theorem. If anyone "closed (72,108)" in the public record, it is Helali, then Suzuki. Roy's Aug-1 note is the first *structural* Case-1 write-up and the first executable Prop 4.3 tail audit. |

**Contradiction search: none found.** Same polygons, same fields, same emptiness, same conditionality. The only numerical disagreement in the (72,108) file set is the printed GGHV typo `(0,1)` vs `(8,14)`, which we, Helali, and he all already correct the same way.

**Priority/citation ledger (hostile, by merit):**

- Exclusion of the two transcribed systems: **Helali first**. Roy vendors him. We already cite him. Do not let Roy's "determinantal closure" phrasing displace that.
- Structural Case-1 `(h,N)` reconstruction: **Roy**, Aug 1, if the un-replayed `RANKDROP_EXACT_UNIT_PASS` holds. Merit citation if we use it.
- Prop 4.3 finite exhaustiveness: **Roy**, and I have replayed the checker. This is the one piece of his (72,108) work we should have had and did not. Cite if any write-up claims the interface from `(24,7)` to the two polygons is audited.
- 5-dessin first-block: **Suzuki first** (Jul 22); Roy reconstructs it without citation. If we mention Roy's Belyi note, cite Suzuki.
- Vertex-gap / strip residue: **ours**, unclaimed by him. Paper1 remains the unique promoted theorem in this cluster.

No tripwire on unpublished campaign objects: nothing on Newton-corner beyond Prop 4.3, no 125-locus / residue-A / td=6 books / D-series / `R_{k,d_2}` / Palomar IDs.

---

## 2. His HC4 route versus the Aug-21 adjudication

Adjudicated record (`xmodel/hc4-adjudication.md`): chain **valid** in the constant-determinant formulation; y-linear sector **is** JC2 both ways; `HC4 = JC2 ⊕ (strictly larger bulk)`; Gordan–Noether protection at `n=4` is signal not survivorship; quintic obstruction module finite; honest scores **6.5/10** information-yield and **2.5–3/10** endgame; first-experiment spec is Ni-quartic replay + quintic module + sector control + Meng–Yang 5→4 kill-probe.

### 2.1 He is on the same avenue, started earlier, went into the bulk

`JC2_HC4_SHARED_BOUNDARY_PROGRAM.md` first-commit cluster **2026-07-30**. Wronskian-to-JC2 **2026-08-07/08**. Our row-10 survey is 08-21; our campaign has **no executed HC4 attack**. He is not following us.

The doubling is the same construction the adjudication proved in five lines, written in cotangent coordinates:

\[
\Psi_F = tP + mQ + H,\qquad
\operatorname{Hess}\Psi_F
=\begin{pmatrix} A & (DF)^T \\ DF & 0 \end{pmatrix},\qquad
\det\operatorname{Hess}\Psi_F = J(P,Q)^2.
\]

He states the collision comparison as an *equivalence* inside this chart (`∇Ψ` injective ⇔ `F` injective), which is the sector decomposition made operational. Formulation is (D) constant-determinant, not de Bondt–van den Essen nilpotent: same as Meng–Yang / Ni / the adjudication. He imported Meng–Yang Schur descent (`MENG_YANG_SCHUR_DESCENT_BRIDGE.md`) with the extra hypothesis the adjudication did not flag: the unbordered Hessian pencil `det M(s,w)` must vanish identically, automatic for doubled Keller potentials, **not** for an arbitrary polynomial affine-linear in one variable. That is a real precision.

### 2.2 Has he seen something the adjudication missed?

**Yes, two objects; no, not a repair of the score.**

**Object A — isotropic Schur recognition.** Expanding `det Hess(tP+Φ)` in `t` gives `[t^2]=0` and `[t]=-Φ_{mm} R(P)` with `R(P)=(∇P)^T adj(Hess P) ∇P`. Constant Hessian determinant forces `Φ_{mm}=0` or `R(P)=0`. The first branch *is* the cotangent/doubling chart; the second is a bordered-degeneracy branch already in his support-free reductions. The adjudication wrote the doubling as a *construction* (JC2 → a point of HC4). He writes the inverse recognition problem: every minimal 4-variable constant-Hessian collision should, after an allowed symplectic rechart, hit this flag, or the `R(P)=0` boundary must be classified until it cannot carry a collision. That problem is well-posed and was not in the Aug-21 spec. It is also unsolved in his notes.

**Object B — Wronskian unit obstruction for moving rank-three `[4]`.** `HC4_RANK_THREE_WRONSKIAN_TO_JC2.md`, theorem `HC4RSD70`. After reducing to `A=yP(x,w)+zQ(x,w)+R(x,w)` with `J(P,Q)=0`, Lüroth gives `P=p(h), Q=q(h)`; the top kernel is `D=b(h)∂_y - a(h)∂_z`; projective motion is `Θ=ab'-ba'`. A polynomial-unit argument on `det S = (τL)^2 (Θ L + B(h))^2` forces `Θ=0` because the only units of `K[x,w]` are constants. Genuinely moving kernels in this subbranch are impossible; the packet falls under a fixed-kernel theorem and reduces to HC2 or the "exact JC2 cotangent endpoint". This is the sector decomposition *used as a kill*, not as a slogan. The adjudication's spec never wrote this unit argument.

**What he has not seen, or has seen and not priced:**

- The y-linear sector is JC2 *in both directions* (if `F` is an automorphism then `∇h` is too, with polynomial inverse). He uses one direction as a reduction; the converse, which makes the sector *exactly* JC2, is unstated.
- Quintic success yields no new JC2 theorem (plane degree ≤ 4 is Wang/Moh). He is running an all-degree Jordan case-tree instead of a quintic module; that tree is exactly the "infinite tower" the adjudication used to cut Sol's 9/10 down to 6.5.
- His own shared-boundary *experiment* returned zero: "the proposed paired initial-conormal class in the associated-graded conductor cokernel is identically zero". The JC2-HC4 bridge, as computed, does not produce a new obstruction. That is the Grok discount in his own handwriting.
- `HC4-MR` ("every generic Jordan stratum of the relative-nilpotent pencil reduces globally to HC2 or the cotangent lift of a plane Keller map") would, *if true*, collapse the "strictly larger bulk" on that one branch. Hostile: (i) it is only the relative-nilpotent pencil `det(S+sT)=δ` for all `s`, not all of HC4; (ii) the note itself says the registered checker "is not an aggregate replay of every implication", and `HC4MR1` "currently has neither an independent end-to-end replay nor external review"; (iii) the `HC4RSD*` numbering has already been reassigned at least once (`archive/hc4-superseded-branches/`). Treat `HC4-MR` as an unaudited claim in a lemma mill, not as a theorem that changes the row-10 score.
- He did not run the cheapest falsification in the adjudicated spec (Meng–Yang Schur descent 5→4 of their degree-14 example, expected to stall at Gordan–Noether / isotropy). He has the lemma; I found no kill-probe.

**Net on row 10.** He has not found a JC2 proof, an HC4 proof, or a reason to raise 6.5. He has executed the case-tree the adjudication predicted would be the *modal* outcome ("hard coupled-layer case tree"), and inside it he isolated a clean unit obstruction that reduces one moving-kernel packet to JC2. That is information-yield of the kind Sol scored, obtained independently, and it is the one HC4 object worth replaying before we spend campaign days on Ni's quartic. It does not change the endgame probability: leftover packets still have to *be* JC2.

Hostile compression of his HC4 corpus: dozens of notes closing named strata, a master theorem that reduces the remainder to "the conjecture we already had", and a shared-boundary computation that vanished. That is the Zhao-ladder instinct wearing Gordan–Noether's dimension-4 protection. The protection is real (adjudication §3); the instinct still has to pay the strictly-stronger tax.

---

## 3. His (75,125) F2 programme versus our frontier

### 3.1 What he is doing

Family `F2`, `j=1`: `A_0=(5,20)`, `(m,n)=(3,5)`, degrees `(75,125)`. Status, quoted: **"forced skeleton, not a normal-form certificate"**; "this note does not claim to eliminate `(75,125)`". Live algebraic gap: descent 12 (layer 28), Schur/Fitting through descent 37, 13 residual functionals after endpoint elimination. Carrier Wronskian classifier: squarefree row `R(v)=(v^2-3v+3)/25` mapping with `(e,f)=(1,3)` to ray `(5,36)`; double-root row `ρ^2-3ρ+1=0` recovering the same Belyi passport `(5,1)|(3,3)|(3,1,1,1)` already on the principal terminal divisor. Nonlinear forcing keeps **both** roots of `27y^2-9y+1` through `v^{10}`, with uniform return surjectivity `18r-1` interior pivots for every `r≥2`. Earlier overclaim (first four zero layers force common-root divisibility) is **disclosed and retracted** in the same file.

`NEXT_DEGREE_FRONTIER.md` is a deterministic regression of the published GGV 125–150 table: 13 unordered pairs starting `(75,125),(84,126),…,(100,150)`. He does not claim an independent reimplementation of the complete-chain generator. That matches our `lib/families.py` posture (faithful table port, gates A/B).

### 3.2 Versus us

Our active endgame is sheet-6 / topological-degree, not a (75,125) coefficient campaign. The deg≤150 farm exists (`lib/farm.py`, 34 families / 62 systems); FACE-ISOLATION names `(75,125)` as a *candidate export* of a DvdK/dessin rigidity that would "subsume and re-derive Suzuki's 5-class top-edge classification … and export it to every cell of the (75,125) frontier" — status **conjectural**, not executed. We have no F2 Laurent compiler, no carrier Wronskian, no `27y^2-9y+1` packet.

So: **he is ahead of us on this pair, and we are not racing him there.** His programme is complementary to vertex-gap (wrong shape: not a `(k,d_2)` strip of the paper1 type) and complementary to td=6 (different invariant). No unpublished overlap.

### 3.3 Versus Strinz (the other public (75,125) actor)

Sweep D2: Strinz `wstrinz/plane-jacobian-75-125` (created Aug 22), open-problem framed, K5 kills generic roots (resultant 63); Roy keeps both roots of `27y^2-9y+1` through `v^{10}`. Both say the coordinates are uncrosswalked. Hostile reading: two independent F2 attacks already disagree at the first interesting modulus, which is the correct scientific state for an *open* pair and a reason not to treat either as a hidden exclusion. Roy does not cite Strinz (Strinz's repo is same-day new; Roy's F2 notes predate it, from Aug 2–11).

Helali opened (75,125) on 2026-07-22 and stalled. Roy is the actor who kept going.

---

## 4. RATE and posture

| Axis | Rating | Why |
|---|---|---|
| **Threat to unpublished programme** (vertex-gap bulk, td=6 residue-A, D-series, 125-locus) | **Low** | Full-grep of markdown for our names, DOIs, Palomar, vertex-gap, Ishihara, Strinz: empty. His (72,108) work stops at the published Prop 4.3 systems. His (75,125) and HC4 are public avenues, not our private ones. |
| **Threat to (72,108) / bound-125 narrative** | **Low–medium** | Fourth replication line, Helali-priority, honest firewall. Medium only if a write-up of ours claims "first structural Case-1" or "first Prop 4.3 tail audit" without citing him. Paper1's theorem is not the exclusion; no scoop. |
| **Threat to row-10 / HC4 option value** | **Medium** | He is executing the untried shortlist item. If `HC4-MR` were real and refereed, the bulk-discount would need a rewrite (on one branch). It is not. The actual risk is priority on the *Wronskian-unit* and *isotropic-Schur* lemmas if we later want them. |
| **Threat to Palomar / paper positioning** | **Low** | No Palomar landing gear visible in the plane-jc docs I read; no 14R15 claim; "no theorem claim" on (72,108). Strinz is the actor with Zenodo+Palomar gear on (75,125). |
| **Collaboration value** | **High** | Proper Helali citation, claim-firewall discipline better than most of the 2026 JC2 field, executable Prop 4.3 audit that we needed, independent 5-dessin reconstruction, an HC4 case-tree we can mine rather than rebuild. House style is a mill; the (72,108) subdirectory is not. |
| **Irrelevant** | **No** | Concurrent, active today, on three of our live objects. |

**Recommended posture (race doctrine: urgency not adversarial; generous credit; share partial results; cite by merit; nothing external without DC):**

1. **Daily watch** `royvanrijn/jacobian-research` (already in the sweep's action list). Commit stream, not just the (72,108) files — the HC4 master and F2 live block are the moving parts.
2. **Cite by merit, if used:** Prop 4.3 exhaustiveness audit (replayed here); Case-1 `(h,N)` lemma (pending our own `RANKDROP` replay); 5-dessin first-block only *with* Suzuki. Helali remains first for the exclusion. Vertex-gap remains ours.
3. **Do not scoop silently.** If paper1 v5 or the companion (72,108) note mentions a finite Prop 4.3 census or a two-generator Case-1 reconstruction, Roy is a required citation as of Aug 1. That is courtesy we already extended to Helali.
4. **HC4:** before spending campaign days on the adjudicated quintic-module spec, replay (i) the Wronskian-unit argument (`verify_hc4_rank_three_wronskian_generic_jet.py` and the unit-obstruction note) and (ii) the isotropic Schur recognition. Keep the 6.5/10 score until one of those produces a degree-uniform mechanism or an HC4 counterexample. Do not absorb `HC4-MR` as a theorem.
5. **(75,125):** complement-citation posture, no new stake required. Our endgame is td=6. Feed his F2 skeleton and the Roy/Strinz K5 disagreement into the next avenue-expansion round as *landscape*, not as a fork we must enter. If FACE-ISOLATION TL3 is ever executed, his 5-dessin and carrier passports are the right negative controls.
6. **Outreach:** candidate for the coordinated-note tier (sweep D1(e)). Content, if DC authorizes: we replayed his Prop 4.3 checker; we have an independent strip-pair mechanism for his Case 2 generic chart; Suzuki exists; Palomar-first is now the channel advice. **No contact without DC.** Standing rule.
7. **Do not** inflate him into a JC2 competitor for the unpublished campaign, and **do not** dismiss him as vibe-noise because the repo is 5,895 files wide. The (72,108) subdirectory is the part that survives hostility.

---

## 5. Verification boundary (what this file is not)

- Not a replay of Helali's 89 MB identity (already done in `CROSSCHECK.md`).
- Not a Singular replay of `RANKDROP_EXACT_UNIT_PASS` / `CASE1_H_DETERMINANTAL_PASS`. The *lemma* is correct; the *instance* is unchecked here.
- Not an audit of `HC4-MR` or of the F2 live Schur/Fitting block.
- Not a claim that bound 125 is now four-times-proved as a theorem: it is four-times-replicated as a *conditional* computational exclusion of two Laurent systems.
- Not a recommendation to change paper1's theorem. Vertex-gap is a different object and remains the unique promoted contribution in this cluster.

**One-line for DC.** Roy is a careful Helali-line auditor who closed our Prop 4.3 interface gap, reconstructed Case 1 without the 89 MB dump, independently walks row 10, and is building the public (75,125) frontier; cite the audit and the `(h,N)` lemma if we use them, watch the repo, do not treat Aug 1 as a scoop, do not enter (75,125) just because he and Strinz did.
