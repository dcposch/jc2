**VERDICT: SOUND-WITH-ERRATA — Theorems 1.1 and 2.1 replay, and I did not find a break in the cusp-peak mechanism; the document proves a genuine T2→T4 simultaneous-normalization theorem for the selected pre-Laurent GGV pair and is not a restatement of G1; it does not repair G2 as REDUCTION CRITICAL 3 defines it (no corner-to-tree map); the machine gate does not verify any of the theorems.**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-17.
Target: `TRANSPORT.md` + `cases/transport_check.py`.
Claim under review: Sol's partial repair of REDUCTION gap G2 — a transport theorem for the GGV-selected polynomial standard pair (cusp peak reduction; lexicographic minimality; signed-axis transport), with the stated scope limits (does not decorate Eggers–Wall trees, does not cover post-Laurent `[P,Q]=x^j` objects, does not repair book coverage or the `td` bound).
Attacks: (1) replay the cusp-peak lemma exactly; (2) machine gate vs prose; (3) SCOPE vs REDUCTION G2 / T-chain (repair, or G1 restated?); (4) residue-A and td-7 instance checks; (5) anything FALSE, not merely unproven.
Method: line-read of `TRANSPORT.md` against `REDUCTION.md` T1–T10 / executive point 2 / CRITICAL 3, `xmodel/grok-reduction-review.md` G2, `xmodel/sol-lateral3.md` §1, `SIGRAY-AUDIT.md` Not 2.1–2.4 / Lem 2.1 / Thm 6.1, Sigray thesis pp. 7–9, `lib/families.py` live `(8,28)` record, `SHEET6-TEMPLATE.md` §1a, `SHEET6-TDUNIFORM.md` (R3), `cases/towers/t9_15_direct.json`; independent replay of the LND inequalities, the unique-northeast maximizer, and the lex bound; `python3 cases/transport_check.py` (exit 0, `"status": "PASS"`); live dump of `section4_families()["8_28"]`. No other repo file modified. No git.

---

## Findings, ranked

### 1. Severity: high — the machine gate does not verify the theorems. Classic hazard.

- File: `TRANSPORT.md:1-6,467-474,602-607,709-711`; `cases/transport_check.py` (entire file)
- Claim: “The machine gate is `cases/transport_check.py`.” Run it; it “exits zero and prints `"status": "PASS"`.” Section 8: “the machine gate proves those frames are different.”
- How checked. The script was run from the repository root. Exit 0. Printed JSON has `"status": "PASS"` and the three blocks advertised in §5. Then the script was read against Theorems 1.1, 2.1, 3.1 and against (4.1)–(4.5).

  **What is actually asserted.**

  | check | what it does | what it does not do |
  |---|---|---|
  | `ggv_8_28_transport` | Reads the live GGV5/S4 record. Checks `(m,n)=(3,2)`, degrees `(108,72)`, `S`, the two scaled hulls, transpose of the two northeast hull vertices, `check_sigray_frame` on `(56,16),(84,24)`, transpose of the three named points, first-edge orthogonality / both cross-product conventions / sign reversal, and `p/q=3/4`. | Construct a polynomial pair. Apply `C` or `R` to polynomials. Test a coordinate. Test an initial form. Test cancellation. Search an Aut class. Test Jacobian 1. Test `td`. Test any family other than `8_28`. |
  | `residue_a_frame_control` | Hardcodes `(126,42),(189,63)`, checks the four Sigray rectangle inequalities, the inverse-transpose/scale round trip to `(21,63)`, `pole_mass` on two hardcoded `(1,1,2)` poles, and `168≠72`. | Read `SHEET6-TEMPLATE.md`. Transport a GGV chain (there is none). Verify that those four numbers are the template's. |
  | `td7_frame_control` | Reads `R0` of `t9_15_direct.json` as `(deg_p_f, D_f)` and `(deg_p_g, d_g)`, checks the rectangle inequalities, the same style of round trip, hardcoded poles `(1,1,2)⊕(1,2,3)`, `M=b`, `TOWER-OBSTRUCTED` as a substring, and `271320≠72`. | Read pole types from the JSON (they are sitting on `P1`/`P2` and are not consulted). Check that `D_f` rather than `d_f` is the right second coordinate except by the accident `κ_{R0}=1`. Transport a GGV chain. |

  **The theorems.** Theorem 1.1 is an LND statement about coordinates. Theorem 2.1 is a degree identity for every source/target Aut. Theorem 3.1 is a simultaneous-normal-form existence statement. None of these is an input, an oracle, or an output of the script. The script cannot fail because a coordinate's initial form lies in the cusp ideal, which is the kill criterion Sol himself wrote in `xmodel/sol-lateral3.md:77-79`. The Jung-word / small-field falsification sweep proposed in that same pitch (`sol-lateral3.md:66-75`) was not implemented.

  **The cheap identities that *are* checked.** (4.1)–(4.5) are term-by-term facts about \(H(y,-x)\). Checking them on one recorded edge is a regression fixture, not a proof, and they were never the load-bearing content.

  **The “PASS proves the frames are different” sentence.** The script proves `168 ≠ 72` and `271320 ≠ 72`. The interpretation that the three objects cannot lie in one Sigray Aut class is Theorem 2.1, which the script does not see. The status key is a constant assigned after three `assert` blocks.

- Suggestion. Rename the script a fixture/regression gate. State in §0 and §5 that it does not verify 1.1/2.1/3.1. If a machine gate for the *theorem* is wanted, implement the Jung-word remainder test Sol already specified, or a symbolic check that a named list of elementary automorphisms cannot drop the ordered degree pair of a rectangular cusp pair.

### 2. Severity: high — the SCOPE statement is a real T2→T4 repair, not a G1 restatement, and not a repair of G2 as REDUCTION CRITICAL 3 defines it.

- File: `TRANSPORT.md:8-12,609-662`; `REDUCTION.md:25-30,271-336,813-824`; `xmodel/grok-reduction-review.md:29-47,134-136,161`
- Claim: “This document repairs REDUCTION gap G2 for the GGV-selected polynomial standard pair.” The T-chain table then says T4 is “strengthened for the T2-selected pair,” T6–T10 are unchanged, and “the fork drawn in T4 closes at the normalization layer.”
- How checked. G2 was read in the three places that define it, then compared with what Theorems 2.1 and 3.1 actually conclude.

  **What G2 was.** Three different missing objects have been sold under that name.

  | source | missing object |
  |---|---|
  | `REDUCTION.md` executive point 2 | a theorem that transports GGV corner/admissible-chain data through Sigray source/target Aut |
  | `REDUCTION.md` CRITICAL 3 / T4 | a theorem sending a GGV chain to a specified Sigray *tree* datum; without it the honest diagram is a fork |
  | `xmodel/grok-reduction-review.md` G2 / triage | “a *dictionary* GGV-chain ↔ Sigray-tree, **or** a proof that one Aut can achieve both NFs at once” |

  **What was proved.** Assume JC2 is false. T2 supplies a globally minimal standard polynomial pair with coprime multipliers \(m,n>1\), a positive integral base \(A=(a,b)\), proportional support rectangles, and both northeast corners. After the determinant-one target sort \(C\) and the signed source rotation \(R(x,y)=(y,-x)\),

  \[
    (f,g)=C\circ(P,Q)\circ R
  \]

  is Sigray-almost-normalized (Theorem 2.1) and satisfies Lemma 2.1(i)–(iv) with type \((\alpha,\beta)=(\min(m,n),\max(m,n))\). The GGV ledger is recovered by the inverse rotations. Later rational GGV5 corners are stored as a valuation spreadsheet, not re-certified in the new chart. Post-Laurent \([P,Q]=x^j\) objects are excluded. Trees are Conjecture T.

  That is exactly the second half of the grok-reduction-review or: **one Aut achieves both normal forms at once**, for the T2 pair, before Laurent cuts. It is new mathematics relative to T2. G1 is the quantifier of GGV Corollary 5.21 (existential selection; the selected pair's \(td\) need not equal a starting pair's). Theorem 2.1 is a lex-minimum *inside this pair's Sigray Aut class*. Those are different invariants. Restricting to the GGV-selected pair is the correct quantifier, not a collapse onto G1: an arbitrary counterexample does not carry GGV-minimal rectangle data, and the document does not claim it does.

  **Which T-link is actually proved.**

  \[
    \mathrm{T2}\;\Longrightarrow\;\text{enhanced T4 for that same pair}.
  \]

  Concretely: T4 already said you may Sigray-normalize the T2 pair and keep its \(td\). The missing piece was that the Aut doing so need not destroy the GGV rectangle. Theorem 2.1 is why. The GGV pair with the smaller multiplier first is *already* almost-normalized, so there is no second Aut-search that would replace the polygon. \(C\) and \(R\) are only a sort and an axis swap. That closes the T4 *normalization* fork.

  It does **not** prove T3 ⇒ T6, T2 ⇒ T7, or CRITICAL 3. The GGV5 fourteen-clause chain is not a Sigray pole tree. Sheet engines still start from type \((\alpha,\beta)\) and Q-data, not from a transposed GGV ledger. Section 6's sentence that T6–T7 “can be attached without discarding the GGV ledger” is coexistence, not a dictionary. Conjecture T is correctly labelled. The T-chain table's “unchanged” rows for T5–T10 are correct.

  **The residual overclaim** is the header “repairs REDUCTION gap G2” without the qualifier that the object repaired is the *normalization fork*, not the *corner-to-tree arrow* that CRITICAL 3 named as G2. The body mostly knows this. A reader of the first twelve lines can miss it.

- Suggestion. Replace the header by: repairs the T4 normalization fork for the T2-selected pre-Laurent pair. Keep CRITICAL 3 / Conjecture T open. Do not write “G2 repaired.”

### 3. Severity: clear — residue-A and the td-7 cell are independent frame-schema controls. The numbers match the cited sources. They are not instance transports, and the script does not even load the poles from the files that contain them.

- File: `TRANSPORT.md:539-607`; `cases/transport_check.py:151-208`; `SHEET6-TEMPLATE.md:61-64,74`; `SHEET6-TDUNIFORM.md:52-58`; `cases/towers/t9_15_direct.json` `R0`/`P1`/`P2`
- Claim: §5.2–5.3 are “exact machine instances”; they validate the transport schema and “fail closed against a false same-representative claim.”
- How checked. The printed arithmetic was replayed by hand and against the live sources. The original commission (`xmodel/sol-transport-prompt.md:19-22`) asked to “verify the transport on the residue-A template data and one td-7 configuration (the books give the Sigray-side data; the GGV side comes from the (72,108) corner tables).”

  **Sol correctly refused the identification.** Residue-A has ordered degrees \((168,252)\). The transported `(8,28)` pair has \((72,108)\). The filed td-7 root has \((271320,406980)\). Theorem 2.1 makes the lex-minimal degree pair an Aut-class invariant, so these cannot be Sigray-equivalent to the `(8,28)` representative if realized. That is the right response to a prompt that would have produced a false identification. Section 8's “no conjecture identifying them is viable” is correct as a data-level statement.

  **The numbers that are there are right.**

  | object | claimed | source | match? |
  |---|---|---|---|
  | residue-A corners / degrees / type | \((126,42),(189,63)\), \((168,252)\), \((2,3)\) | `SHEET6-TEMPLATE.md:61-63` | yes |
  | residue-A masses | \(\Lambda(1,1,2)=3\), \(3+3=6\) | TDU (R3): \(\Lambda=ab\alpha\beta/\nu\); template `td=6=3+3`; pole Q-data \(P_i=(2,2,2,1,5)\) is \(a=b=1,\nu=2\) | yes, but hardcoded |
  | inverse base | \(T^{-1}(126,42)/2=(21,63)\) | \(T\) is an involution; \(\alpha=2\) | yes |
  | td-7 `R0` as \((k_f,l_f),(k_g,l_g)\) | \((203490,67830),(305235,101745)\) | JSON `deg_p_f, D_f, deg_p_g, d_g`; at root \(\kappa=1\) so \(D_f=d_f=67830\); campaign convention \(k_f=\deg p_f\big|_{R}\), \(l_f=d_f\big|_{R}\) (same as template \(126\) and \(42\)) | yes at this root |
  | td-7 poles / \(M\) / masses | \((1,1,2)\oplus(1,2,3)\), \(M=(1,2)\), \(3+4=7\) | JSON `P1`/`P2` types; TDU (R3); unique td-7 entry | yes, but hardcoded; JSON types are unused |
  | `TOWER-OBSTRUCTED` | substring of `status` | live JSON | yes |
  | incompatibility with `(72,108)` | both degree pairs differ | arithmetic | yes |

  **What the instance section does not do, and the prompt asked for.** There is no GGV chain on the residue-A template or on the td-7 cell, so there is nothing to transport except the four rectangle numbers and a formal inverse base. Calling these “exact machine instances” of a *transport theorem* is the same genus of overclaim as Finding 1. They are schema-consistency checks plus a degree-pair inequality.

  **Two implementation defects, neither fatal to the arithmetic.**

  1. Residue-A is not read from `SHEET6-TEMPLATE.md`. Td-7 poles are not read from the certificate that the prose says the gate “reads.” A future edit of either source will not fail this script.
  2. `td7_frame_control` uses `D_f` on the \(f\)-side and `d_g` on the \(g\)-side (`transport_check.py:182-184`). At `R0` they coincide. Off the root they do not: vertex `G` has `deg_p_f=203490` and `D_f=67830` but `d_f=9690`. The identification “root Q-degrees = Sigray corners” is campaign-conventional and happens to hold here; it is not enforced by a uniform field rule.

- Suggestion. Load residue-A from the template file or from a single pinned record. Load td-7 poles from `P1`/`P2`. Use `d_f` at the root, or assert `kappa==1` and `D_f==d_f` before treating `D_f` as \(l_f\). Call §5.2–5.3 controls, not instances of the transport.

### 4. Severity: residual — attack (1) does not break the cusp-peak mechanism. Theorems 1.1 and 2.1 replay. The LND proof is the real content.

- File: `TRANSPORT.md:64-305`; Sigray thesis Not 2.1 / Lem 2.1 (pp. 7–9); `xmodel/sol-lateral3.md:44-86`
- Claim: a coordinate cannot have \((r,s)\)-initial form in the cusp ideal \((d^r U^s-c^s V^r)\); therefore a rectangular northeast pair is already lex-minimal in its Sigray Aut class, and \(C,R\) put it in Sigray normal form.
- How checked. The proof was replayed line by line, then compared with Sigray's printed definitions and with the five-line pitch in `sol-lateral3.md`.

  **Theorem 1.1, replay.**

  \(h\) is a coordinate, so some mate \(k\) has \(J(h,k)=\lambda\in\mathbf C^*\) and \(\partial=J(h,-)\) is LND (in \((h,k)\)-coordinates it is \(\lambda\,\partial/\partial k\)). Let \(\bar h=\operatorname{in}_{r,s}h\) and \(D=J(\bar h,-)\). The \((r,s)\)-filtration is the standard positive grading; \(D\) is the associated-graded derivation, homogeneous. If \(D\) failed to be LND a homogeneous witness \(q\) would have \(D^j(q)\ne0\) for all \(j\), and that leading piece would be the leading piece of \(\partial^j(q)\), contradicting local nilpotence of \(\partial\). \(D\ne0\) because \(\bar h\) is nonconstant in characteristic zero. LND-degree \(\delta_D\) is additive on a char-0 domain by the single surviving Leibniz term \(\binom{e_1+e_2}{e_1}D^{e_1}q_1\,D^{e_2}q_2\). Hence \(\ker D\) is factorially closed.

  If \(\bar h=Bq\) with \(B=d^r U^s-c^s V^r\), then \(D(\bar h)=0\) forces \(B\in\ker D\), hence
  \[
    s d^r U^{s-1}D(U)=r c^s V^{r-1}D(V).
  \]
  \(U^{s-1}\) and \(V^{r-1}\) are coprime in \(\mathbf C[U,V]\), so \(V^{r-1}\mid D(U)\) and \(U^{s-1}\mid D(V)\). Neither side vanishes (else \(D=0\)). Writing \(p=\delta_D(U)\), \(q_0=\delta_D(V)\) and using \(\delta_D(Da)=\delta_D(a)-1\),
  \[
    p-1\ge(r-1)q_0,\qquad q_0-1\ge(s-1)p,
  \]
  which add to \((s-2)p+(r-2)q_0\le-2\). For integers \(r,s\ge2\) and \(p,q_0\ge0\) the left side is \(\ge0\). Contradiction. (In fact \(p,q_0\ge1\), but that is not needed.)

  The kernel of \(U\mapsto cZ^r\), \(V\mapsto dZ^s\) is \((B)\) because \(B\) is the primitive irreducible binomial of a coprime monomial curve and a surjection of one-dimensional domains is an isomorphism. So (1.1) \(\Leftrightarrow\) (1.2). Coprimality of \(r,s\) is used here, not in the LND inequality.

  I did not find a hole. The filtered-leading-part paragraph is the standard associated-graded argument and is slightly terse, not wrong. Weighted Jung–van der Kulk is genuinely unused: a mate exists by the document's definition of coordinate. The inequality is why \(r,s>1\) is essential; at \(r=1\) it need not be impossible.

  **Corollary 1.2.** Top-face terms of \(h\) become a common multiple of \(H^e\); the total coefficient is the coefficient of \(Z^e\) in \(\operatorname{in}_{r,s}h(cZ^r,dZ^s)\), nonzero by (1.2). Lower faces have ordinary degree \(<De\). Correct. The written sentence “The scalar is nonzero” is sloppy: individual top-face terms may cancel; the *sum* does not. Theorem 2.1's own cancellation clause states the evaluation form correctly, so this is a local wording defect, not a broken corollary. See Finding 5.

  **Theorem 2.1, replay.** Support in the two rectangles with northeast coefficients \(c,d\ne0\). For \(L=(u,v)\) one has \(\deg u,\deg v\ge1\), so \(D_L=a\deg u+b\deg v\ge a+b\). The functional \((i,j)\mapsto i\deg u+j\deg v\) on \([0,ra]\times[0,rb]\) is uniquely maximized at \((ra,rb)\) because both weights are strictly positive. Hence \((P\circ L)_+=cH^r\) and \((Q\circ L)_+=dH^s\) with \(H=u_+^a v_+^b\) homogeneous of degree \(D_L\). For a target coordinate \(h\), only the maximal \((r,s)\)-face can reach ordinary degree \(D_L\deg_{r,s}h\), and cancellation at that degree is (1.2), which is forbidden. That is (2.3).

  Every nonconstant polynomial has \((r,s)\)-degree at least \(r\) (since \(r<s\), the unique monomial of weight \(r\) is \(U\)). So the first degree in (2.4) is at least \(r D_L\ge r(a+b)\). Equality forces \(D_L=a+b\) (i.e. \(\deg u=\deg v=1\)) and \(\deg_{r,s}h_1=r\), hence \(h_1=\gamma U+\gamma_0\). Then \(J(h_1,h_2)=\gamma\,\partial h_2/\partial V\in\mathbf C^*\), so \(h_2\) has a \(V\)-linear term and \(\deg_{r,s}h_2\ge s\). Apply (2.3). The original pair attains \((r(a+b),s(a+b))\) because the northeast monomials have those ordinary degrees. Therefore it is almost-normalized in Sigray's sense (Not 2.1: lex-min \((\deg f,\deg g)\) in the source/target Aut class).

  Ordinary non-divisibility of \(r D_L\) and \(s D_L\) is indeed not enough: \(P^s\) and \(Q^r\) both have degree \(rs D_L\), and \(P^s-Q^r\) can cancel. Theorem 1.1 is exactly the missing input. This matches the novelty guard in `sol-lateral3.md:83-86`.

  **Theorem 3.1, replay against Sigray print.** After \(C\), the smaller multiplier is first, so 2.1 applies. \(R(x,y)=(y,-x)\) has Jacobian \(1\) and preserves total degrees, so almost-normalized is preserved and \(J=1\) is preserved. On exponents, \(x^i y^j\mapsto(-1)^j x^j y^i\), so the rectangles become
  \[
    (k_f,l_f)=\alpha(b,a),\qquad (k_g,l_g)=\beta(b,a).
  \]
  Sigray Lemma 2.1(i) is “\(N_f\) is a part of the rectangle with vertices \((0,0),(0,l_f),(k_f,l_f),(k_f,0)\)” and the printed proof normalizes to \(f^+_{1,1}=x^{k_f}y^{l_f}\). That is this convention. The five numerical claims are immediate from \(0<a<b\), \(1<\alpha<\beta\), \(\gcd(\alpha,\beta)=1\). The printed Lemma 2.1(iii) only has \(l_f\le k_f\); the strict inequality is Sigray Theorem 6.1. Here it is free from \(a<b\). \(a<b\) itself is not an extra wish: if the northeast corner occurs, it lies on the \((1,0)\)-face, GGV orients \(\operatorname{en}_{1,0}\) as the upper endpoint, and \(v_{1,-1}(\operatorname{en}_{1,0})<0\) is \(m(a-b)<0\).

  Why Abhyankar 18.13/19.2 are unused: for this pair, \(f^+_{1,1}\) is already the northeast monomial (unique \((1,1)\)-maximizer on the rectangle). Sigray's linear map \(A\) is needed when that leading form is a product of two linear forms. Here it is a monomial, and the only linear change required is the axis swap that enforces \(l_f\le k_f\). \(R=(y,-x)\) is the determinant-one form of that swap. Identifying the result as “normalized of type \((\alpha,\beta)\)” uses Not 2.1–2.4 as nomenclature, not Lemma 2.1's existence proof. That claim is correct.

  **What would kill this**, and was not found: a coordinate whose \((r,s)\)-initial form lies in \((B)\); or a GGV-standard polynomial pair in the scope of T2 whose supports are not proportional rectangles with unique northeast corners. Those are Sol's own kill criteria. I did not produce either.

- Suggestion. Keep 1.1/2.1. Expand the associated-graded paragraph by one sentence (filtration is \(D\)-stable; leading term of \(\partial^j(q)\) is \(D^j(q)\) whenever the latter is nonzero). Fix the Corollary 1.2 wording (Finding 5). Do not call 2.1 “stronger than global GGV minimality.”

### 5. Severity: erratum — three sentences are false or category-wrong as written. None of them carries 1.1/2.1/3.1.

- File: `TRANSPORT.md:195-207,297-300,333-341`
- Claim / how checked.

  1. **Corollary 1.2, “The scalar is nonzero by Theorem 1.1.”** False if “the scalar” is a per-term coefficient. Several top-face monomials can cancel; Theorem 1.1 only makes the sum nonzero. The next theorem already uses the evaluation form. One-line repair: “the sum of those coefficients is the coefficient of \(Z^e\) in (1.2), hence nonzero.”

  2. **“The theorem is stronger than global GGV minimality.”** Category error, not a strengthening. GGV minimality is \(\gcd(v_{1,1}(P),v_{1,1}(Q))=B_{\mathrm{GGV}}\) among *all* counterexamples. Theorem 2.1 is lex-min \((\deg f,\deg g)\) inside *this* pair's Sigray Aut class. Neither implies the other. The second isolated point in the same paragraph (ordinary non-divisibility does not stop \(P^s-Q^r\) from cancelling) is the one that is true and useful.

  3. **Theorem 3.1.4 “precisely Sigray's rectangular normal-form conditions.”** Sigray Lemma 2.1(iii) prints \(l_f\le k_f\) (and \(l_g\le k_g\)). Strict \(l_f<k_f\) is Theorem 6.1, “later… a slightly deeper analysis.” The document obtains the strict inequality from \(a<b\) and does not need 6.1. Say that. Do not say the printed (iii) is already strict.

- Suggestion. Three one-line edits. No change to the theorems.

---

## Attack-by-attack

### (1) Cusp-peak mechanism — replay

**Stands.** The LND argument, the unique-northeast maximizer, and the lex bound close. Weighted Jung–van der Kulk is not a hidden dependency. The mechanism is exactly the one pitched in `sol-lateral3.md` §1, with the improvement that step 4 of that pitch (weighted JvdK peak reduction) was replaced by a self-contained degree formula. I did not find a characteristic-zero coordinate whose initial form lies in the cusp ideal, and I did not find a hole that would produce one.

### (2) Machine gate vs prose

**The hazard is real and is the worst process defect in the filing.** `"status": "PASS"` is a fixture of three arithmetic blocks. It is not a verification of Theorems 1.1, 2.1, or 3.1. See Finding 1.

### (3) SCOPE vs G2 / T-chain

**Not G1 restated.** G1 is T2's existential quantifier. This is T2 ⇒ enhanced T4 for that pair: already almost-normalized, so \(C\) and \(R\) suffice, and the GGV polynomial ledger is recoverable.

**Not a repair of G2 as CRITICAL 3.** No GGV-chain ↦ Sigray-tree map. Conjecture T is correctly open. T5–T10 are correctly unchanged. The honest slogan is: the T4 *normalization* fork closes for the selected pre-Laurent pair; the *data* fork (polygon versus decorated tree) does not.

### (4) Residue-A and td-7

**Honest refusal of a false identification; weak as “instances.”** Degree pairs differ; TDU masses and template/JSON corners match; poles are hardcoded; no GGV chain is transported because none exists on those objects. See Finding 3.

### (5) FALSE, not merely unproven

Three local falsehoods, none load-bearing: Corollary 1.2's “the scalar”; “stronger than global GGV minimality”; “precisely” Sigray (iii) for a strict inequality. See Finding 5.

I did **not** find a false theorem. The following remain unproven and are labelled as such, correctly: Conjecture T (corner-to-tree); Conjecture A (native transposed GGV5 admissibility); book coverage; an upper bound on \(td\); existence of any polynomial realizing the `(8,28)` record.

---

## Live gate output (independent run, 2026-08-17)

```text
$ python3 cases/transport_check.py ; echo EXIT:$?
```

Exit 0. `"status": "PASS"`. Live `8_28` dump from `lib/families.py` matches §5.1:

```
mn (3, 2)
deg 108 72
S ((0, 0), (1, 0), (8, 28), (0, 4))
A0 (8, 28)   A0p (1, 0)   final (11/4, 7)
steps ((4, -1, 3, 4),)
supp P (0,0),(3,0),(24,84),(0,12)
supp Q (0,0),(2,0),(16,56),(0,8)
```

First-edge replay: \(w=(4,-1)\), edge \((7,28)\), \(w\times\mathrm{edge}=119>0\); \(Tw=(-1,4)\); pointwise transported edge has cross \(-119\); orientation-preserving pair \(((0,1),(28,8))\) has cross \(+119\); \((\rho+\sigma)/v_w(A_0)=3/4\) on both sides.

Residue-A and td-7 degree/mass arithmetic as in Finding 3.

---

## Bottom line

The load-bearing new fact is Theorem 1.1, and it looks like a theorem. Theorem 2.1 is the reason the T2 pair does not need Sigray's Abhyankar-based Aut search. Theorem 3.1 is then an axis sort plus an axis swap. That is a real, correctly quantified repair of the T4 *normalization* fork for the selected pre-Laurent pair. It is not G1 restated, it is not a corner-to-tree functor, and it is not what `transport_check.py` checks.

Write the header as a T2→T4 theorem. Keep Conjecture T open. Demote the script from “machine gate of the theorem” to “fixture of the `(8,28)` ledger and two formal frames.” Fix the three local false sentences.

No other repo file modified. No git.
