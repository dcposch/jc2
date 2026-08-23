**VERDICT: SOUND-WITH-ERRATA**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-13.
Target: `xmodel/sol-thmB.md` (GPT-5.6-Sol, claimed OBSTRUCTION theorem B-O).
Cross-cut: `SHEET6-DIRECTIONB.md` §7 (level-42 no-log pins, just proved).
Method: full read of the note against DIRECTIONB §§0–7, TEMPLATE E6 leads, MATHIEU Thm A / Mathieu definition; independent exact re-derivation of Lemmas 1–2 and the (9) jet (no sympy: stdlib rationals); explicit substitution of the family over \(\mathbb F_{349},\mathbb F_{1297},\mathbb F_{1693}\); independent monomial census + modular rank of the banked D=21 pickle (four primes, two \((w,h)\) fibres); Row_10/Row_20 support census against the six live pins.
No other repo file modified. No git.

Theorem B-O is a correct existence theorem about unrestricted jets in \(K[\eta,t]\). The explicit family substitutes and does what it claims on that ambient space. The additive-span claim is proved from the banked relaxation (ranks replay) plus Lemma 4, not merely asserted. Two load-bearing wordings overclaim, and the advertised flexibility mechanism is dead on the §7-pinned residue-A locus.

---

## What §7 changes (read this first)

Section 7 pins the six live level-42 through-\(d_0\) tails

\[
tf1_{42}=tf2_{42}=tg1_{42}=tg2_{42}=tg01_{42}=tg02_{42}=0
\]

(necessary on every residue-A realization: \(\operatorname{Res}_t(y\,dx)=-42\,c_{42}=0\)). In `gm_jet2`, those six coefficients are exactly the linear slot-10 data of \(\Phi,\Gamma\): through-\(d_0\) factors are \(\eta-\widetilde y\) with \(\widetilde y\) slotted by level\(-32\), so level 42 is jet slot 10.

Sol’s family is

\[
\Phi=p^2+r t^{10}+a t^{20},\qquad
\Gamma=p^3+\tfrac32 p r t^{10}+6pa t^{20}+b t^{40},
\]

with \(r\neq0\) forced (Lemma 2: \(r^2=cs+p^3Q\), \(p\) coprime to \(s\), \(c\neq0\)). Slots \(1,\ldots,9\) vanish by support. On the D21 window that support leaves only the six level-42 tails as a source of a pure slot-10: every Row_10 monomial that avoids those six uses a level-38/40 tail and/or a \(vf_{34/36}\) factor, which populates slots \(2,4,6,8\) and exits the family. Hence **the construction requires nonzero level-42 tails**.

**The ceiling theorem’s flexibility mechanism is DEAD under the section-7 pins.** The slot-10 common-cusp tangent, its square \(Q_{20}(r)=-3p'r^2+9prr'\), and the fractional resonance (7) are not available on the pinned residue-A locus. One is back in DIRECTIONB §6.T’s first sub-stratum (level-42 \(=0\)), already inconsistent on the 16 slot-20-linear tails (rank \(4/10\), defect \(\eta^{12,15,18,21,24,27}\)).

What survives of the obstruction on the pinned locus:

- Theorem B-O as a statement about unrestricted \(K[\eta,t]\) jets is untouched. Those jets are not Keller-admissible residue-A points.
- The additive-separator claim **survives**, and is not carried by this family. After the six pins the independent-monomial relaxation is still
  `Row_20: 10 × 2295, rank 10, CONSISTENT`;
  `full window: 76 × 4351, rank 56, CONSISTENT`
  (replayed from the banked pickle; matches DIRECTIONB §7.G). So no linear functional of the remaining columns kills every tail monomial while detecting \(-42\). The surviving columns are the non-L42 monomials (levels 38–41, 43+, \(vf\)-crosses), i.e. the other half of §6.T’s “deeper loading”.
- Proposition 3 (no positive-valuation deformation of the skeleton) is unaffected.
- Sol already listed “additional admissibility of the branch-product tails” as necessary for a kill. Section 7 is exactly that input. It does not refute the functional obstruction; it removes the explicit witness from the campaign locus.

---

## Findings (worst first)

### 1. Severity: erratum — the flexibility mechanism is the L42 quadratic, and §7 kills it

- File: `xmodel/sol-thmB.md:2-8,232-317` and exec item 3, against `SHEET6-DIRECTIONB.md:706-784` and `cases/r1_experiment.py:561-569`.
- Claim: an explicit polynomial family realizes any prescribed nonzero Row 20 with all other J-rows below slot 42 vanishing; the escape “is a common-cusp tangent in slot 10 whose square feeds Row 20, exactly the level-42 quadratic mechanism”.
- How checked:
  - Family (9) has \(F_{10}=r\). Identity \(r^2-cs=p^3Q\) plus \(\gcd(p,s)=1\) forces \(r\neq0\) (independent Q-gcd).
  - Chart dictionary: through-\(d_0\) slot \(=\) level\(-32\). The six live §7 names are the only free level-42 through-\(d_0\) tails; B-side level-42 is already frozen in D21.
  - Pickle census, Row_10: the six `_42` names are exactly L42; 60 linear L42 terms; **366 monomials with no L42 factor**, all of type \(vf_{34/36}\cdot t_{38/40}\) (and cubes). Those terms need lower tails and populate earlier slots, so they are not this family.
  - Row_20 still has 195 pure-L42 quadratics (the §6.T “21 quadratic monomials” after eta-flattening / E-aggregation) plus 19011 monomials with no L42 at all.
- Why this is not a break of Theorem B-O: the theorem is existence in \(K[\eta,t]\), and that existence holds (Finding 3). It is a break of the campaign reading that this family is the level-42 escape still live on residue-A. Under §7 that escape is off the table.
- What a correct ceiling must now say: skeleton + unrestricted 41-jet flexibility do not kill; Keller no-log does kill *this* flexibility; any remaining Theorem B has to use the nonlinear 38–41 / high-tail complex that the nolog relaxation still cannot linearly separate from \(-42\).

### 2. Severity: erratum — “any prescribed nonzero Row 20” is only the constants

- File: `xmodel/sol-thmB.md:5-6` (exec 2) vs the theorem at `:54-67` and the identity \(R_{20}=c\) at `:275-284`.
- Claim (exec): the tails “realize any prescribed nonzero Row 20”.
- What is proved: \(\mathcal B(\Phi,\Gamma)\equiv c t^{20}\pmod{t^{42}}\) for arbitrary \(c\in K^\times\). So \(R_{20}\) is the **constant** polynomial \(c\in K\), i.e. only the \(\eta^0\) component is nonzero.
- The campaign target is exactly that constant (\(-42\) at \(\eta^0\), zeros elsewhere), so the useful case is covered. An arbitrary 10-vector in the eta-slot space, or an arbitrary element of \(K[\eta]\), is not constructed. The resonant ODE \(pC'-\frac23 p'C=\mathrm{rhs}\) with \(C\parallel s\) hits constants and nothing more in this writeup.
- Theorem statement is accurate. Executive summary is not.

### 3. Severity: clear — the family substitutes; p-gauge and all rows below 42 check

- File: `xmodel/sol-thmB.md:15-27,84-317`.
- p-gauge: \(a_1=3+\sqrt3\), \(a_2=3-\sqrt3\) (DIRECTIONB line 23, TEMPLATE `:100-105`; the ratio \(a_1/a_2=2+\sqrt3\) is CAMPAIGN `:10`, not the pole value). Then
  \[
  (\eta^3-a_1)(\eta^3-a_2)=\eta^6-6\eta^3+6.
  \]
  Confirmed. Lead rescaling \(S_M,G_M\) is bilinear in \(\mathcal B\) and only rescales \(c\), as claimed.
- Identity (5): \(\frac92 p s'-3p's=1\) with \(s=(4\eta-\eta^4)/108\). Exact in \(\mathbb Q[\eta]\). Intermediate \(p(1-z)-z(z-3)(4-z)=6\) in \(z=\eta^3\) also exact. \(p\) squarefree (\(\gcd(p,p')\in\mathbb Q^\times\)); \(\gcd(p,4\eta-\eta^4)\in\mathbb Q^\times\); evaluations \(p(0)=6\), \(p|_{\eta^3=3}=-3\), \(p|_{\eta^3=4}=-2\).
- Lemma 1: \(L_n=-2p\bigl(6ph'+(n-18)p'h\bigr)\) and \(Q_{20}=-3p'r^2+9prr'\) re-derived from (1) and checked on random exact \((f,h)\) and on the actual \(p\). Slot-10 local factor \(6m-8\neq0\) for every \(m\in\mathbb Z\) (the writeup’s first-step valuation already covers every finite multiplicity at a simple root; no iteration gap).
- R20 reduction: \(R_{20}=pC'-\frac23 p'C\) with \(C=\frac92 r^2-12ph_{20}\) is an identity of jets. Under (8), \(C=\frac92(r^2-p^3Q)\), hence \(=\frac92 cs\) on Lemma 2, hence \(R_{20}=c\) by (5). All over \(\mathbb Q\).
- \(R_0,R_{10},R_{30},R_{40}\) vanish for **arbitrary** \(r,Q\) once (8) is used (dummy exact polynomials; no square-lift needed). \(R_{30}=-2(rG_{20})'+8(aG_{10})'=0\) is the \(6pa\leftrightarrow\frac32 par\) cancellation. \(R_{40}\) self-pair \(48p'a^2+36paa'\) cancels the \(G_{40}=b\) linearization. Support of (9) admits only slots \(0,10,20,30,40\) below 42.
- Remainder (10): pairs \((10,40)\) and \((20,40)\) only. Re-derived, then matched on the explicit jets.
- Explicit substitution: Hensel lift of \(\sqrt{cs}\) from \(p\) to \(p^3\) in \(\mathbb F_q[\eta]\), then \(\mathcal B(\Phi,\Gamma)\) by the same formula (1).
  - \(\mathbb F_{349}\), \(c=1\) and \(c=5\): live \(t\)-degrees \(\{20,50,60\}\); \(R_{20}=c\); all other \(k<42\) zero; (10) holds.
  - \(\mathbb F_{1297}\) and \(\mathbb F_{1693}\), \(c=1\): same.
- Lemma 2 existence over an algebraic closure is the standard unit-Hensel lift (\(2r_m\) invertible mod \(p\) because \(cs\) is a unit in \(K[\eta]/(p)\)). Algebraic closure is used only there, as claimed; no claim of a model over \(\mathbb Q(\sqrt3)\).
- Conclusion: (2) holds in the unrestricted jet category. This is not a candidate residue-A point (Sol `:452-457` already says so).

### 4. Severity: clear — the span claim is proved from the banked ranks, not asserted

- File: `xmodel/sol-thmB.md:351-442`, citing DIRECTIONB `:475-501`.
- What is claimed: in the recorded full-window relaxation, tail-value vectors span the inhomogeneous residual, so no *unconditional additive* residue/Gaussian/Mathieu separator detects \(-42\).
- Lemma 4: for a polynomial map \(P(u)=\sum_{\alpha\in A}v_\alpha u^\alpha\) over an infinite field, \(\operatorname{span}\{P(u)\}=\operatorname{span}\{v_\alpha\}\). Proof is the standard “quotient + coefficient extraction on \(K^N\)”. Correct; needs infiniteness, which the field factors of the value-tier algebra have.
- Banked numbers, independent replay from `directionb_tails_D21.pkl` (183 vars, rows \(\{6,8,10,12,14,16,18,20\}\)), monomial census **exact**:

  | object | rows × cols | rank (mod \(p\)) | consistent |
  |---|---:|---:|---|
  | Row 20 | 10 × 2718 | 10 | yes |
  | full window | 77 × 5106 | 57 | yes |
  | Row 20, L42=0 | 10 × 2295 | 10 | yes |
  | window, L42=0 | 76 × 4351 | 56 | yes |

  Primes: \(105337,105673,200257\) (campaign) and \(314329\) (extra). Second fibre \(w=(2,3)\), \(h=(+,-)\): Row 20 still \(10\times2718\) rank 10 consistent. Specialization can only drop rank, so E-rank of Row 20 is exactly 10; modular consistency at four primes plus the campaign’s unit-pivot GE is the span statement. After pins one window row dies (Row_10 \(\eta^{28}\) / C10.6), as §7 says; Row 20 stays full rank.
- Lemma 4 + rank 10 \(\Rightarrow\) \(\operatorname{span}\{P_{20}(u)\}=K^{10}\), so the pure \(\eta^0\)-constant is in the span of *values*. Consistency of the affine window \(\Rightarrow -r\in\operatorname{span}\{v_\alpha\}\), upgraded by Lemma 4 to \(-r\in\operatorname{span}\{P(u)\}\). That is a proof, not an assertion.
- It is **not** a proof that some single \(u\) solves \(P(u)=-r\). Sol says so at `:436-442`. Exec item 4’s shorthand “tail-value vectors linearly span the residual” is true as a span statement and easy to misread as existence of a point. Ranked as wording, not a break (Finding 6).

### 5. Severity: nit — functional class and “unconditional” are almost honest, slightly punchy

- File: `xmodel/sol-thmB.md:1-11,54-79,351-442,463-472`.
- Functional class actually used: \(\Phi,\Gamma\in K[\eta,t]\) with square/cube leads and no other support constraints. Not a branch product, not a template point, not Keller-exact, not in the 315-factor image. Stated in the theorem paragraph and again in §7 of the note. Correct.
- “Unconditional” in the separator claim is scoped in the body to a *fixed linear* functional (or fixed linear subspace) of the 77-row window, equivalently of all evaluated tail contributions, without the monomial/toric relations and without the lower-band ideal. Residue, constant-term, and Gaussian-moment functionals in that additive form are genuinely excluded. The Mathieu sentence uses only the underlying vector space (`MATHIEU.md:37-47` is the definition; the \(1\in M\Rightarrow M=\mathcal A\) lemma is the intended hammer). A multiplicative Mathieu argument after imposing the band ideal is explicitly not excluded.
- Two nits, not breaks:
  - Status line “a proved obstruction theorem” bundles B-O (clean existence) with the separator (conditional on the campaign relaxation and on additivity). Different strength.
  - Mathieu subspaces live in an algebra of functions/series, not a priori in \(K^{77}\). The only load-bearing reading is “linear functional on \(R_{20}\in K[\eta]\) / on the window”. That reading works. A reader who thinks a Mathieu subspace of \(K[\eta,t]\) has been ruled out has over-read.
- Section 7 does **not** make the functional theorem false. It makes “unconditional” in the campaign sense obsolete: the no-log pins are extra conditions, and they are now on the table.

### 6. Severity: nit — exec item 4 can be read as a point, not a span

- File: `xmodel/sol-thmB.md:8` vs `:436-439`.
- “Tail-value vectors linearly span the inhomogeneous residual” is Lemma 4 + consistency. Linear combinations may use several tuples. The relaxation treats monomials as independent coordinates; a real \(u\) lies on the Veronese. Sol’s own last paragraph of §6 is the accurate statement. Keep the exec line in that language.

### 7. Severity: nit — \(r\) is not shown to lie in the six-dimensional campaign slot-10 space

- Even before §7, identifying (9) with “exactly” the campaign L42 quadratic overclaims the overlap. Campaign \(F_{10}\) is a specific \(K\)-linear image of six scalars (Galois-twisted through-\(d_0\) products). Sol’s \(r\) is a Hensel lift of a square root of \(cs\) in \(K[\eta]/(p)\), degree \(<18\) after two steps, not proved to lie in that 6-plane. The actual residue-A skeleton also carries \(w_i\) at level 37 (slot 5) and \(vf\) at 34/36 (slots 2,4); family (9) has those slots empty. So (9) is a flexibility in a *larger* ambient space than the campaign jets. Harmless for B-O as stated; another reason the family is not a residue-A witness.

### 8. Severity: nit — Proposition 3 and the fractional-weight remark are fine

- Prop 3 is the associated-graded form of the promoted zero-tail theorem (DIRECTIONB `:221-238`, `:389-396`). Not re-proved here; in scope for a campaign-citing obstruction note. Agrees with the inconsistent differential (`:503-518`).
- That (7) is a fractional-weight \(w=2/3\) counterexample to a naive extension of Theorem A (`MATHIEU.md:279-315`) is correct: \(\deg C=4=\frac23\deg p\), leading factor vanishes, and (5) is the explicit particular solution. Integer-weight Thm A is not touched.

---

## Attack list, closed

1. **Substitute the family, exactly, in the normalized \(p=\eta^6-6\eta^3+6\) gauge.** Done. Identities over \(\mathbb Q\); full \(\mathcal B\) on explicit lifts at three split primes and two nonzero \(c\). All J-rows \(k<42\), \(k\neq20\), vanish; \(R_{20}=c\); remainder (10) holds.
2. **Does it require nonzero level-42 tails?** Yes, as a campaign realization of *this* support. Ceiling flexibility (slot-10 square / L42 quadratic) is **DEAD** under §7. Surviving obstruction on the pinned locus = the additive span via the remaining 2295 Row-20 monomials, plus Prop 3. No explicit pinned witness.
3. **Span: proved or asserted?** Proved: Lemma 4 + banked ranks. Ranks and column counts independently replayed from the D21 pickle, including the nolog numbers.
4. **Scope wording.** Functional class is unrestricted jets (honest). “Any prescribed Row 20” is an exec overclaim (constants only). “Unconditional” is honest if read as additive/linear; punchy if read as ruling out every functional Theorem B, especially after §7.

---

## Checks the writeup did not need, recorded anyway

- p-gauge expansion and TEMPLATE/DIRECTIONB pole pair \(3\pm\sqrt3\) (not the ratio \(2\pm\sqrt3\)).
- Row_10/Row_20 monomial support vs L42, to pin the dictionary rather than trust the prose “exactly”.
- Fourth prime \(314329\) and a second \((w,h)\) fibre on the relaxation, both agreeing with the campaign \(10/57\) and nolog \(10/56\).
- Citations to DIRECTIONB `:44-73,141-158,221-238,389-425,447-501,503-518,549-570,605-645` and MATHIEU `:37-47,279-315` resolve to the facts used.

No files modified except this review.
