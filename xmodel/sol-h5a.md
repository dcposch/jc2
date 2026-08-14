# H5a at doubly realized vertices: Q is forced; forced-\(\nu\) is an extra conjecture

Date: 2026-08-13  
Scope: td-7 class-C zero arrivals, with the thesis notation kept distinct from the campaign notation  
Status: **PRIMARY RESEARCH — PROOF + EXACT REDUCTION + DECISIVE-EXPERIMENT SPEC**

## Verdict

**Deliverable classification: (c), sharpened by proofs resolving the definition-level branches.** There is no known normalized counterexample realization, so full coherence of either book cannot honestly be proved here. What can be proved is: Q/max is the unique uniform repair of the global \(\kappa\)-decoration; that repair forces E5; both resulting book branches remain unrefuted by the audit-corrected/verified apparatus; and one minimal residual assertion decides 17 versus 2.

1. **PROVED — H5a is resolved as a uniform global convention.** At a doubly realized vertex, the only uniform presentation-independent repair compatible with the thesis's integer decoration, Notation 3.11, and its explicit use in Proposition 5.5 is the **Q/jump/max value**

   \[
   \boxed{\kappa_F=\frac{\nu_F\kappa_G}{\nu_G}}.
   \]

   A global P/nonjump/coarse convention is not coherent: it can give nonintegral \(D_{h,F}=\kappa_Fd_{h,F}\), contrary to printed Statement 3.8. Moreover, its \(\bar\kappa_F\) has exact denominator \(\nu_F\) at every such jump, so it is pointwise incompatible with the promoted integer Q-data/N1 machinery. A special P-only-at-nonpole-III rule is not separately refuted by a pre-§9 printed pointwise theorem, but it would be a new context-dependent convention, not a reading supplied by Notation 3.5.

2. **PROVED — once Q is used, E5 is forced.** Printed Statement 3.17(ii) and Proposition 9.3(e) give

   \[
   \boxed{D_F=\frac{\nu_FD_G+n\deg p_G}{\nu_G}},\qquad
   \boxed{\bar\kappa_F=\frac{\nu_F\bar\kappa_G+n}{\nu_G}}.       \tag{E5}
   \]

   Thus the denominators \(\nu_F\) printed in Proposition 9.3(g),(h) are wrong unless \(\nu_F=\nu_G\).

3. **The two-cell book requires a new assertion, not a Notation 3.5 choice.** The minimal assertion for this census is

   > **CONJECTURE \(U_{7C}\) (EQUAL-III-7C).** Every actual Proposition 9.3 case-III edge realizing a td-7 class-C zero-arrival certificate admitted by the filed P0/P3/closure hypotheses satisfies \(\nu_F=\nu_G\).

   The stronger global assertion that *every* case-III edge of a normalized counterexample has equal indices will be called **CONJECTURE \(U_{\rm global}\)**; it implies \(U_{7C}\) but is not minimal. Apart from the disputed raw tokens of Proposition 9.3(g),(h)—whose validity on the relevant edges is equivalent to the needed equality—no independently justified printed proof, downstream theorem, or promoted fact in the audited dependency chain proves \(U_{7C}\). The definitions, local Eggers--Wall calculus, Statement 3.17, and isolated Proposition 8.1(iv) differential equation permit \(\nu_F\ne\nu_G\); an exact polynomial model is given below. The model is not a Keller pair, so it does not prove \(\neg U_{7C}\).

4. Consequently, the **17-cell Q+E5 book is the sound conservative object** under the already filed P0/P3/arrival/closure/budget hypotheses. The 2-cell book is the sub-book obtained by additionally imposing **CONJECTURE \(U_{7C}\)**. **Forced-\(\nu\) is a dead hope at the proved tier:** it survives only as an explicitly new Keller-specific conjecture, not as a consequence of H5a, Notation 3.5, the proved content of Proposition 8.1 or 9.3, or any downstream computation in Statements 9.6--9.11.

This resolves the misleading trichotomy in [the census review](grok-census11a-review.md#1-severity-clear--the-census-is-arithmetically-right-the-remaining-question-is-which-h5a-reading-is-true-and-the-printed-record-now-leans-at-the-17-cell-book):

| candidate | status | consequence |
|---|---|---|
| global P/nonjump/coarse \(\kappa_F\) convention | **REFUTED** by Statement 3.8 and Proposition 5.5 | no coherent book |
| Q/jump/max + E5 | **FORCED** by the definitions plus printed transport identities | 17-cell conservative book |
| Q/jump/max + E5 + \(\nu_F=\nu_G\) on relevant edges | not refuted, but equality is **CONJECTURE \(U_{7C}\)** | conditional 2-cell sub-book |

The promoted census numbers remain exactly those recorded in [BOOK-OFFAXIS.md:750](../BOOK-OFFAXIS.md#L750): 17 cells, 238 raw routes, 233 deduplicated routes (197 at equality). The \(U_{7C}\)-restricted sub-book remains exactly the two cells and 49 deduplicated routes (31 at equality) recorded at [BOOK-OFFAXIS.md:790](../BOOK-OFFAXIS.md#L790).

## 1. Orientation and the statement being proved

Proposition 9.3 writes \(G=F+c\), with

- thesis \(F\): the shallower/new vertex, the class-C merge;
- thesis \(G\): the deeper/old vertex, the zero-arrival;
- \(u=\pi(F)<v=\pi(G)\).

The gluing and census notes reverse the letters:

| role | thesis | campaign |
|---|---|---|
| shallower merge | \(F\), index \(\nu_F\) | \(G\), index \(\nu_G\) |
| deeper arrival | \(G\), index \(\nu_G\) | \(U\), index \(\nu_U\) |

Accordingly, **CONJECTURE \(U_{7C}\)** is \(\nu_F=\nu_G\) in thesis notation and \(\nu_G=\nu_U\) in campaign notation, restricted to the td-7 class-C certificates relevant to this book.

Assume case III of Proposition 9.3. A branch \(P\) realizes the deeper jump at \(v\) but does not jump at \(u\); another branch \(Q\) realizes \(u\) as a characteristic exponent. The vertex \(F\) is therefore doubly realized. Notation 3.5 applied literally to \(P\) and \(Q\) gives two values. The following proposition identifies them and selects the one used by the thesis's own later statements.

### Proposition 1 (uniform H5a/Q-repair theorem)

Let \(L_0\) be the denominator index of the common Puiseux lattice immediately below \(u\), and evaluate \(\kappa_G\) through \(P\)'s jump presentation at \(v\). Then

\[
 \kappa_F(P)=L_0=\frac{\kappa_G}{\nu_G},\qquad
 \kappa_F(Q)=\nu_FL_0=\frac{\nu_F\kappa_G}{\nu_G}.        \tag{1}
\]

The second value is the Q/jump/max value. It is the unique uniform global repair of Notation 3.5 among its two presentation-values that is compatible with printed Statement 3.8 and with the \(c=0\) proof of printed Proposition 5.5.

### Proof

Let the last denominator lattice of \(P\) below \(u\) be \(L_0\). At \(v\), \(P\) makes the next characteristic jump. By Notations 3.4--3.5, adjoining that jump multiplies the lattice index by \(\nu_G\), so \(\kappa_G=\nu_GL_0\). This gives the first equality in each part of (1).

For \(Q\), \(u\) itself is a characteristic exponent and its index drop is \(\nu_F\). Its post-jump lattice is therefore \((\nu_FL_0)^{-1}\mathbb Z\), and Notation 3.5 evaluated on this presentation gives \(\kappa_F(Q)=\nu_FL_0\). Since \(\nu_F\ge2\), this is also the maximum of the two values. This proves (1).

There is a pointwise promoted-arithmetic test. Write the jump presentation of \(Q\) as \((K,\beta_1,\ldots)\), let \(u=\beta_j/K\), and put \(e_j=\gcd(K,\beta_1,\ldots,\beta_j)\). Then

\[
 L_0=\frac{K}{e_{j-1}},\qquad
 \nu_F=\frac{e_{j-1}}{e_j},\qquad
 \bar\kappa_F^{Q}=\frac{K-\beta_j}{e_j}.                 \tag{1a}
\]

Furthermore,

\[
 \gcd\!\left(\bar\kappa_F^{Q},\nu_F\right)
 =\frac{\gcd(K-\beta_j,e_{j-1})}{e_j}
 =\frac{\gcd(\beta_j,e_{j-1})}{e_j}=1.                  \tag{1b}
\]

The P/coarse value therefore gives

\[
 \bar\kappa_F^{P}=L_0(1-u)
 =\frac{\bar\kappa_F^{Q}}{\nu_F},                        \tag{1c}
\]

with exact denominator \(\nu_F\ge2\). Thus P is pointwise impossible in the promoted integer Q-data and N1 machinery ([SHEET6-III.md:121](../SHEET6-III.md#L121)--[135](../SHEET6-III.md#L135)). The proof of printed Statement 9.4 separately treats \(\kappa_H(\pi(H)-1)\) as an integer, corroborating the thesis-wide integer-decoration expectation.

Now put a polynomial \(h\) into the chart

\[
 y=\phi_{<u}(x)+x^{-u}\eta .
\]

Every exponent of the resulting \(x\)-series lies on the post-jump lattice \((\nu_FL_0)^{-1}\mathbb Z\). Hence

\[
 d_{h,F}\in\frac1{\nu_FL_0}\mathbb Z,\qquad
 (\nu_FL_0)d_{h,F}\in\mathbb Z.                           \tag{2}
\]

The right member is exactly \(D_{h,F}\) under the Q-value. The coarse value would instead be \(L_0d_{h,F}\), which is not integral in general. The \(x\)-chart argument is symmetric. Statement 3.8 says \(D_{h,F}\in\mathbb Z\) for *every* polynomial \(h\) and every vertex. Thus the Q-value is uniformly compatible with that statement, while the explicit witness in Section 3 refutes a uniform P-value convention. [SIGRAY-AUDIT.md:37](../SIGRAY-AUDIT.md#L37) records the conclusion and an independent nonintegral witness; [SIGRAY-AUDIT.md:92](../SIGRAY-AUDIT.md#L92) records its load-bearing consequence.

The thesis provides an independent in-context check in Proposition 5.5 (printed pp. 26--27). In its \(c=0\) case, \(P\) is explicitly the nonjump presentation, with Puiseux characteristics \((\kappa,\beta_1,\ldots,\beta_m)\) and \(\alpha_m<u\). It then says that any other \(Q\) realizing \(F\) has ramification index \(\nu_F\kappa\), preserves the earlier characteristic exponents, and appends \(u\) as the new characteristic exponent. The tuple as printed is dimensionally garbled—it leaves the old integer numerator indices unscaled and writes rational \(u\) in an integer slot—but its ramification factor and the following displayed ratio are unambiguous.

The proof then computes

\[
 \Lambda(P)=\kappa d_{g,F}=\frac{D_{g,F}}{\nu_F}.           \tag{3}
\]

Equation (3), together with the thesis definition \(D_{g,F}=\kappa_Fd_{g,F}\), forces \(\kappa_F=\nu_F\kappa\), the Q/jump value, in this in-context \(c=0\) pole case. With the P-value \(\kappa_F=\kappa\), the right side would be \(\kappa d_{g,F}/\nu_F\), contradicting the displayed equality because a pole has nonzero order. The dropped \(g\)-subscripts in that proof are the already audited Proposition 5.5 typo; boxed formula (18) contains the correct subscript ([SIGRAY-AUDIT.md:70](../SIGRAY-AUDIT.md#L70)).

Finally, Notation 3.11 takes a maximal \(V_{1,a}\) vertex and chooses a branch \(Q\) realizing it as a characteristic exponent immediately before defining \(D_{h,F}=\kappa_Fd_{h,F}\). At a case-III \(F\), that maximal value is \(u\), hence the chosen \(Q\) is precisely the jump realization. Notation 3.11 does not explicitly say “re-evaluate \(\kappa_F\) through this \(Q\),” so this is textual corroboration, not an additional proof.

Together, (2), the nonintegral witness, and (3) force Q/max as the unique uniform, thesis-intended global repair. Equations (1a)--(1c) additionally exclude P pointwise inside the promoted integer Q-data machinery. The narrower historical caveat is that no pre-§9 printed theorem separately says “use Q at every nonpole case-III vertex”; a P-only context split would be ad hoc, absent from Notation 3.5, and unusable by the promoted book. \(\square\)

## 2. The Q-value forces E5, not equality of the two indices

### Proposition 2 (case-III transport theorem)

Under the Q-value of Proposition 1, printed Statement 3.17(ii) and printed Proposition 9.3(e) force

\[
 D_F=\frac{\nu_FD_G+n\deg p_G}{\nu_G},\qquad
 \bar\kappa_F=\frac{\nu_F\bar\kappa_G+n}{\nu_G}.           \tag{4}
\]

The formulas printed as Proposition 9.3(g),(h) agree with (4) if and only if \(\nu_F=\nu_G\). Neither Notation 3.5 nor the derivation of (4) forces that equality.

### Proof

Statement 3.17(ii) and Proposition 9.3(e) are

\[
 d_F=d_G+(v-u)\deg p_G,qquad
 v-u=\frac{n}{\nu_F\kappa_G}.                              \tag{5}
\]

Multiplying the first identity by the forced value \(\kappa_F=\nu_F\kappa_G/\nu_G\) gives

\[
\begin{aligned}
D_F
 &=\frac{\nu_F\kappa_G}{\nu_G}
   \left(\frac{D_G}{\kappa_G}
         +\frac{n\deg p_G}{\nu_F\kappa_G}\right)\\
 &=\frac{\nu_FD_G+n\deg p_G}{\nu_G}.
\end{aligned}
\]

Similarly,

\[
\begin{aligned}
\bar\kappa_F
 &=\kappa_F(1-u)\\
 &=\frac{\nu_F\kappa_G}{\nu_G}\bigl((1-v)+(v-u)\bigr)\\
 &=\frac{\nu_F\bar\kappa_G+n}{\nu_G}.
\end{aligned}
\]

This is exactly the promoted rederivation at [SHEET6-III.md:131](../SHEET6-III.md#L131)--[139](../SHEET6-III.md#L139).

Printed (g),(h) have the same positive numerators but denominator \(\nu_F\). In case III, \(n>0\), \(\deg p_G>0\), and the down-arrow data have positive \(D_G,\bar\kappa_G\). Therefore either printed equality agrees with (4) exactly when \(\nu_F=\nu_G\). Conversely, equality of the indices makes the formulas identical. This proves the iff assertion.

For completeness, the P/coarse value gives instead

\[
 D_F^{P}=\frac{\nu_FD_G+n\deg p_G}{\nu_F\nu_G},\qquad
 \bar\kappa_F^{P}=\frac{\nu_F\bar\kappa_G+n}{\nu_F\nu_G},  \tag{6}
\]

so it agrees with neither (4) nor the printed formulas; here \(\nu_G\ge2\). This is why the old mixed update was not a third coherent theory. \(\square\)

### Corollary 2.1 (what would be needed for two cells)

The forced-\(\nu\) book follows only after adjoining **CONJECTURE \(U_{7C}\)** to Proposition 2. If \(U_{7C}\) is proved, (4) reduces to printed (g),(h) on every relevant actual edge and the census restricts to the two equal-index cells. Without \(U_{7C}\), deleting the 15 unequal-index cells is not justified.

## 3. Exact unequal-index local model

This model shows that unequal indices are not excluded by the definitions, the Eggers--Wall tree calculus, the down-arrow inequalities, Statement 3.17, or the isolated polynomial equation appearing in Proposition 8.1(iv). It is a case-III **local configuration**, not an application of Proposition 9.3 under its ambient Keller-pair hypothesis.

Take

\[
 f=(xy^2-1)(xy^3-1)(x^2y^3+1),\qquad a=0.                 \tag{7}
\]

Three branches at \(x=\infty\) are

\[
 P:y=x^{-1/2},\qquad Q:y=x^{-1/3},\qquad
 R:y=\zeta x^{-2/3},\quad \zeta^3=-1.
\]

Their contacts give

\[
 F=I_P(1/3)=I_Q(1/3)=I_R(1/3),\qquad
 G=I_P(1/2)=I_R(1/2).
\]

The zero direction out of \(F\) reaches \(G\). Relative to \(P\), it has the exact local combinatorics of Proposition 9.3 case III:

\[
 u=\frac13< v=\frac12,\qquad
 \nu_F=3,\quad \nu_G=2,\quad \kappa_G=2,\quad n=1,        \tag{8}
\]

because \(1/2-1/3=1/(3\cdot2)\).

At \(F\), set \(\eta=x^{1/3}y\). Then

\[
 f^F=(x^{1/3}\eta^2-1)(\eta^3-1)(x\eta^3+1),
\]

so

\[
 f_F^+=x^{4/3}p_F(\eta),\qquad
 p_F=\eta^5(\eta^3-1),\quad d_F=\frac43,\quad\deg p_F=8.    \tag{9}
\]

At \(G\), set \(\eta=x^{1/2}y\). Then

\[
 f^G=(\eta^2-1)(x^{-1/2}\eta^3-1)(x^{1/2}\eta^3+1),
\]

so

\[
 f_G^+=-x^{1/2}\eta^3(\eta^2-1),\qquad
 d_G=\frac12,\quad\deg p_G=5.                              \tag{10}
\]

All checks are exact:

\[
 \frac43=\frac12+\left(\frac12-\frac13\right)5,qquad
 \operatorname{mult}(p_F,0)=5=\deg p_G,                    \tag{11}
\]

and the two local down-arrow inequalities are

\[
 0<\frac43<\left(1-\frac13\right)8,qquad
 0<\frac12<\left(1-\frac12\right)5.                        \tag{12}
\]

At \(F\), Notation 3.5 gives \(\kappa_F(P)=1\) and \(\kappa_F(Q)=3\). Thus

\[
 (D_F,\bar\kappa_F)_{P}=\left(\frac43,\frac23\right),
 \qquad
 (D_F,\bar\kappa_F)_{Q}=(4,2).                             \tag{13}
\]

The P-value directly violates Statement 3.8 for \(h=f\). At \(G\), the Q/max data are \((D_G,\bar\kappa_G)=(1,1)\). E5 gives

\[
 D_F=\frac{3\cdot1+1\cdot5}{2}=4,qquad
 \bar\kappa_F=\frac{3\cdot1+1}{2}=2,                      \tag{14}
\]

whereas printed (g),(h) give \(8/3\) and \(4/3\).

There is also an honest polynomial realization of the isolated Proposition 8.1(iv) equation. Put

\[
 p=\eta^5(\eta^3-1),\qquad q=\eta(\eta^3-1).
\]

Direct differentiation gives

\[
 \frac43pq'-\frac23p'q=2p.                                \tag{15}
\]

The polynomial

\[
 h=xy(xy^3-1)
\]

realizes this top exactly: \(h_F^+=x^{2/3}q\). It is not proved to be the canonical approximate-root polynomial supplied by Proposition 4.2 in a Keller pair, but (15) is not merely formal root-pattern algebra. The nonzero roots of \(p_F=\eta^5(\eta^3-1)\) are simple, so the relation \(p^i=p_F\) forces \(i=1\). With that value, the isolated ratio in Proposition 9.3(f) also checks:

\[
 \frac{\deg p}{\deg q}=\frac84=2
 =\frac{3D_G+n\deg p_G}{3\kappa_G(1-v)+n}
 =\frac{3+5}{3+1}.                                        \tag{16}
\]

This proves that the local definitions, tree geometry, Statement 3.17 identity, and isolated Proposition 8.1(iv) equation do not by themselves derive equality of the indices.

**Scope warning.** The pair \((f,h)\) in (7),(15) is not a Keller pair; its full Jacobian is nonconstant. Therefore this model does **not** prove \(\neg U_{7C}\) or \(\neg U_{\rm global}\), and it is not claimed to extend to a normalized counterexample. A relevant normalized-Keller extension is **CONJECTURE (global extension)**.

## 4. Printed coherence audit

The printed record supports E5 as a denominator-subscript slip and supplies no hidden equality theorem.

### 4.1 Proposition 9.3 itself

The proof on printed pp. 50--51 derives only (a)--(d), using the same multiplication by \(\kappa_F\) as Proposition 2, then says that the remaining statements are proved “the same way.” Repeating that line for case III produces (4), with denominator \(\nu_G\), not the printed \(\nu_F\). There is no extra hypothesis \(\nu_F=\nu_G\) in the case-III statement or proof.

### 4.2 An actual subscript slip in the same calculation

Statement 9.6, case-II solution A (printed pp. 52--53), starts from

\[
 Q(G)=(j,2j,3,2,5),\qquad n=10,\qquad \nu_F=7.
\]

Its proof prints a final denominator \(\nu_F\) but obtains

\[
 D_F=7j,\qquad \bar\kappa_F=5.
\]

The numerators are \(j+10(2j)=21j\) and \(5+10=15\). The displayed outputs divide them by the parent index \(\nu_G=3\), not by the child index \(\nu_F=7\):

\[
 21j/3=7j,qquad 15/3=5.
\]

So the thesis demonstrably has a \(\nu_F/\nu_G\) subscript slip in this exact formula family. This does not by itself disprove \(U_{7C}\) in case III, but it is strong printed evidence that Proposition 9.3(g),(h) contain the same kind of slip. The earlier isolation is at [SHEET6-HIII-REVIEW.md:129](../SHEET6-HIII-REVIEW.md#L129)--[134](../SHEET6-HIII-REVIEW.md#L134); the census review restates its book consequence at [grok-census11a-review.md:62](grok-census11a-review.md#L62).

### 4.3 Statements 9.6--9.11 do not use unequal-index case-III numerics

The downstream statements were checked application by application.

- Statement 9.6 uses case III only to conclude \(M_F=1\) from the displayed \(p,q\) root pattern.
- Statement 9.7 uses it only to obtain an additional nonzero direction and hence \(\lambda_F\ge1\); Statements 9.8--9.10 refer back to the same qualitative move.
- Statement 9.11 again uses the case-III root pattern only to conclude \(M_F=1\).
- Every numerical \(Q(F)\) output in these statements comes from case II, not from case III. No application evaluates (g) or (h) on a case-III edge with \(\nu_F\ne\nu_G\).

Therefore no independently justified downstream theorem in this chain fails when audit-corrected Q+E5 replaces the disputed printed tokens, and no theorem in the chain proves \(U_{7C}\). Literal Proposition 9.3(g),(h) themselves do conflict with unrestricted E5 off the equal-index locus; treating either raw token as an independently valid axiom is exactly a route to \(U_{7C}\), not independent evidence for it.

## 5. Non-contradiction result and minimal residual decider

Two branches remain **unrefuted by the audit-corrected/verified local apparatus**:

1. **Unrestricted Q+E5.** Proposition 2 holds for arbitrary legal \((\nu_F,\nu_G)\). Section 3 supplies an exact unequal-index local realization of the isolated Proposition 8.1(iv) equation with matching polynomial chart tops.
2. **Q+E5+\(U_{7C}\).** This restricts the relevant td-7 class-C certificates to the equal-index locus. On that locus printed (g),(h) and E5 coincide. The existing \((9,15,7,3)@2\) transport witness gives an exact equal-index positive control ([sol-sixcells.md:52](sol-sixcells.md#L52), hostile replay [grok-sixcells-review.md:1](grok-sixcells-review.md#L1)).

This is not a proof of full-Keller coherence for either branch and does not assert existence of a normalized counterexample. Unrestricted E5 contradicts the raw typography of (g),(h); it is compatible with their audit-corrected derivation and all independently verified downstream uses. Existence of any normalized counterexample is outside this note.

### Minimal printed statement whose verification decides 17 versus 2

After Proposition 1, the residual decider is exactly one assertion:

> **\(U_{7C}\):** every actual Proposition 9.3(III) edge realizing one of the td-7 class-C zero-arrival certificates admitted by the filed P0/P3/closure hypotheses has \(\nu_F=\nu_G\).

Equivalent deciding routes are:

- prove printed Proposition 9.3(g) or (h), with its printed denominator, independently for every relevant actual td-7 class-C Keller edge; together with Proposition 2 and positivity this proves \(U_{7C}\) and selects the 2-cell sub-book; or
- construct one dependency-complete, Keller-compatible unequal-index edge realizing one of the 15 relevant promoted-only td-7 certificates; this disproves \(U_{7C}\) and proves that its certificate cannot be deleted.

Within this filed pipeline, nothing smaller remains to inspect: Notations 3.4--3.5 determine the two indices and the uniform Q repair but not their equality; Statement 3.17 and Proposition 9.3(e) force E5; the isolated Proposition 8.1(iv) equation admits the unequal model above; Statements 9.6--9.11 never test the unequal numerical case.

**CONJECTURE \(U_{7C}\) is unproved. Its negation is also unproved.** In that exact state of knowledge, deleting 15 cells would be an unsound false kill. Hence the 17-cell census is the correct conservative work queue under the filed P0/P3/arrival/closure/budget hypotheses.

## 6. Decisive experiment

### 6.1 Short answer

There are two meanings of “decisive.”

- **YES — the discrete route predictions differ.** The promoted-only cell \((18,27,13,9)@\mu_0=5\) has an unequal-index arrival that is a genuine stored direct step-cell in the filed priced transition graph—not a proved Keller-realized arrival. Q+E5 predicts \(n=3\), handshake \(X=4\), and admission to an exact SAT leading Proposition 8.1/transport prefix. The \(U_{7C}\)-restricted theory predicts **NO ROUTE**, because the arrival index 7 differs from the merge index 13.
- **NO — the available 69-row msolve prefix is not itself H5a-discriminating.** It contains no \(n\), H5/H6 equation, chart offset, or J6/T2 cancellation-window index; if Stage 0 is wrongly bypassed, the same prefix is SAT under every reading. Adding the constant equation \(13-7=0\) would manufacture the unit ideal tautologically and is not empirical evidence. A dependency-complete full-route system is a necessary next computational tier, not by itself a semantic decision. Deciding \(U_{7C}\) requires a proof, exhaustive certified EMPTY coverage of every relevant unequal-index route/family, or an exact all-orders/algebraic relevant unequal-index Keller realization.

Thus the Stage-0 experiment below is a decisive regression for the two implementations, while the polynomial prefix is an exact finite local-compatibility certificate. It is not a proof that the leading solution extends to a Keller pair.

### 6.2 Discriminating route

Use the priced path

```text
P2 entry (w=3/2,M=2)
  -- lambda_lb=2, st96 l2e0k1S1x0nu7(21,15) -->
A=(21,15,nu=7,M=3), w=2/3
  -- lambda_lb=1, st96 l3e0k1S2x0nu7(35,15) -->
U=(35,15,nu_U=7,M=5), w_U=2/5
  -- zero, mu0=5 -->
G=(18,27,nu_G=13,M=9), w_G=4/9
  -- lambda_lb=2, st96 l9e3k1S6x0nu4(63,9) -->
T=(63,9,nu=4,M=9), w=4/9, case IV

Second branch synchronized at G:
G -- nonzero mu=1, n=194 --> N=(49,50,nu=49,i=2)
N -- continuation, n=195 --> P1.
```

The synchronized frames \((\rho,\bar\kappa,\nu;w,M)\) are

\[
\begin{array}{c|c}
P2&(1/2,5,3;3/2,2)\\
A &(1/3,5,7;2/3,3)\\
U &(1/5,3,7;2/5,5)\\
G &(2/9,6,13;4/9,9)\\
T &(2/9,2,4;4/9,9)\\
N &(2,100,49;2,1)\\
P1&(1,5,2;2,1).
\end{array}
\]

The two pre-merge chain-2 edge values are \(n=10,16\); the discriminating zero edge has the value below; the suffix edge has \(n=20\); and the chain-1 values are 194 and 195. At the zero edge, campaign-form E5 gives

\[
 n_{Q}=\nu_U\bar\kappa_G-\nu_G\bar\kappa_U
      =7\cdot6-13\cdot3=3,                                \tag{17}
\]

and

\[
 X_G=\mu_0(\bar\kappa_G-\nu_Gw_U)
    =5\left(6-13\cdot\frac25\right)=4,                    \tag{18}
\]

which is the \((18,27)\) cell's required value. The obsolete mixed handshake predicts

\[
 X_{\rm mixed}=5\left(6-7\cdot\frac25\right)=16,
\]

and literal unequal-index printed (h) gives \(n=13(6-3)=39\). These are concrete, mutually incompatible predictions.

The \(U_{7C}\)-restricted branch does not use 16 or 39: it rejects the certificate because \(7\ne13\). Index 13 is neither a stored direct arrival at \((2/5,5)\) nor neutral there, since the neutral class is \(-1\equiv4\pmod5\). The direct arrivals are \(2,7,12\), as recorded at [BOOK-OFFAXIS.md:759](../BOOK-OFFAXIS.md#L759); the priced path is independently replayed at [grok-gluing-preflight-review.md:64](grok-gluing-preflight-review.md#L64).

For the suffix \(T=(63,9,4,9)\), the filed P0 calculation has \(E=18\), \(\bar\kappa=2\), and \(X=14\). Its multiplicity-6 nonzero direction contributes \(\lceil14/6-2\rceil=1\), and its \(\epsilon=3\) zero direction contributes \(\lceil(14/3-2)/4\rceil=1\), hence \(\lambda_{\rm lb}=2\), \(w'=4/9\), and \(M'=9\). Also \(j=9(1-4/9)=5\) and \(\psi=1\). The three displayed \(\lambda\)'s are lower bounds; for any actual carrier, the budget sandwich forces their sum sharp:

\[
 2+1+2=5=6-\psi.
\]

The combinatorial prefix by itself does not prove that an actual carrier exists.

### 6.3 Exact synchronized leading certificate

Choose full-\(f\) synchronization indices

\[
 i_A=2,\quad i_U=14,\quad i_G=98,\quad i_N=2,\quad i_T=196. \tag{19}
\]

Then

\[
4=i_A\cdot2,
\quad21i_A=42=3i_U,
\quad35i_U=490=5i_G,
\quad49i_N=98=i_G,
\quad18i_G=1764=9i_T.
\]

The following is a literal characteristic-zero msolve input: 77 variables, 69 rows, expanded sums only, and no parentheses. It is suitable as a parser/regression smoke test **after Q+E5 Stage 0 passes**. None of these 69 rows itself encodes the H5a discriminator. No emitter currently writes it, so save this block as `h5a_18_27_lead.ms` only when running the experiment.

```text
Ap1,Bp1,Cp1,An,Cn,Ag,Bg,Cg,Au,Bu,Cu,Aa,Ba,Ca,At,Bt,Ct,Ap2,Up2,Vp2,Cp2,cn,cg,cu,ca,ct,dn,dg,du,da,dt,zu,za,zt,Sr,St,Sg,Su,Sn,Sp1,Sa,Sp2,up1A,up1B,up1AB,up1C,unA,unC,ugA,ugB,ugAB,ugC,uuA,uuB,uuAB,uuC,uaA,uaB,uaAB,uaC,utA,utB,utAB,utC,up2A,up2V,up2disc,up2qA,up2C,uSr,uSt,uSg,uSu,uSn,uSp1,uSa,uSp2
0
2*Bp1-3*Ap1,
2*Ap1*Bp1-Cp1,
50*Cn+49*An,
2*Bg-Ag,
13*Ag*Bg+3*Cg,
Bu-2*Au,
7*Au*Bu-3*Cu,
2*Ba-3*Aa,
7*Aa*Ba-5*Ca,
Bt-2*At,
4*At*Bt-Ct,
2*Up2+3*Ap2,
Ap2*Up2+4*Vp2,
3*Ap2*Vp2-Cp2,
cn^49-An,
cg^13-Ag,
cu^7-Au,
ca^7-Aa,
ct^4-At,
dn-49*cn^48,
dg-13*cg^12,
du-7*cu^6,
da-7*ca^6,
dt-4*ct^3,
zu-Au+Bu,
za-Aa+Ba,
zt-At+Bt,
St-Sr,
Sg-St*ct^588*dt^1764*zt^1176,
Su-Sg*Ag^98,
Sn-Sg*cg^490*dg^98,
Sp1-Sn*dn^2,
Sa-Su*du^42*zu^28,
Sp2-Sa*da^4*za^2,
up1A*Ap1-1,
up1B*Bp1-1,
up1AB*Ap1-up1AB*Bp1-1,
up1C*Cp1-1,
unA*An-1,
unC*Cn-1,
ugA*Ag-1,
ugB*Bg-1,
ugAB*Ag-ugAB*Bg-1,
ugC*Cg-1,
uuA*Au-1,
uuB*Bu-1,
uuAB*Au-uuAB*Bu-1,
uuC*Cu-1,
uaA*Aa-1,
uaB*Ba-1,
uaAB*Aa-uaAB*Ba-1,
uaC*Ca-1,
utA*At-1,
utB*Bt-1,
utAB*At-utAB*Bt-1,
utC*Ct-1,
up2A*Ap2-1,
up2V*Vp2-1,
up2disc*Up2^2-4*up2disc*Vp2-1,
up2qA*Ap2^2+up2qA*Up2*Ap2+up2qA*Vp2-1,
up2C*Cp2-1,
uSr*Sr-1,
uSt*St-1,
uSg*Sg-1,
uSu*Su-1,
uSn*Sn-1,
uSp1*Sp1-1,
uSa*Sa-1,
uSp2*Sp2-1
```

The blocks are, in order: seven local Proposition 8.1(iv)/Wronskian patterns; five characteristic-direction rows; five derivative rows; three separation/Taylor-cofactor auxiliary definitions; seven leading transport scale rows; and 35 Rabinowitsch guards. The five preceding equations \(c^{\nu}-A\) are the continuation-root rows.

### 6.4 Exact rational SAT anchor

The system is already proved SAT over \(\mathbb Q\), so msolve can only smoke-test serialization and parsing. Set every local \(A\) and every \(c\) to 1, and set

\[
\begin{array}{c|c}
P1&(B,C)=(3/2,3)\\
N&C=-49/50\\
G&(B,C)=(1/2,-13/6)\\
U&(B,C)=(2,14/3)\\
A&(B,C)=(3/2,21/10)\\
T&(B,C)=(2,8)\\
P2&(U,V,C)=(-3/2,3/8,9/8).
\end{array}
\]

Also take

\[
 (dn,dg,du,da,dt)=(49,13,7,7,4),
 \quad(z_U,z_A,z_T)=(-1,-1/2,-1),
\]

and

\[
\begin{aligned}
S_r&=S_t=1, & S_G&=4^{1764}, & S_U&=S_G,\\
S_N&=S_G13^{98}, & S_{P1}&=S_N49^2,
& S_A&=S_U7^{42}, & S_{P2}&=S_A7^4/4.
\end{aligned}
\]

Each inverse variable is the reciprocal of its displayed guard target. The nontrivial P2 guard values are \(U^2-4V=3/4\) and \(A^2+UA+V=-1/8\). Direct rational substitution makes all 69 rows zero.

Expected outcomes are therefore:

| reading | Stage 0 | leading system |
|---|---|---|
| Q+E5 | PASS: \(n=3,X=4\) | SAT at the rational anchor |
| Q+E5+\(U_{7C}\) | NO CERTIFICATE: \(7\ne13\) | must not be emitted; if wrongly emitted, still SAT |
| literal printed/free-index update | FAIL: \(n=39\ne3\) | must not be emitted; if wrongly emitted, still SAT |
| obsolete BOOK/mixed handshake | FAIL: \(X=16\ne4\) | must not be emitted; if wrongly emitted, still SAT |

No polynomial row in this prefix changes between these readings. A polynomial experiment that actually sees \(n=3\) versus \(n=39\) needs the missing J6/T2 chart-window rows, where \(n\) changes the offset and cancellation window.

### 6.5 Fleet-ready execution contract

Do **not** run msolve locally: [ops/FLEET.md:3](../ops/FLEET.md#L3) prohibits it. Because this tiny system has a known rational point, it belongs alone on `box01` with 2--4 threads. First coordinate with the fleet owner and inspect the current farm load and `crontab -l`; do not stack it on standing jobs. Ship the file with `scp`; do not paste the system through a long ssh command. On the remote host, launch it orphan-safe and self-recording, for example:

```sh
mkdir -p ~/jc72108/h5a/out
cd ~/jc72108/h5a
nohup sh -c "timeout 3600 msolve -g 2 -t 4 -f h5a_18_27_lead.ms -o out/h5a_18_27_lead.out; echo \"LANE h5a-lead: rc=\$? size=\$(wc -c < out/h5a_18_27_lead.out | tr -d ' ') \$(date +%H:%M)\" >> lanes.log" >/dev/null 2>&1 &
```

A partial output is not a verdict, whether it has zero or nonzero size. Accept EMPTY only after recording `rc=0`, a complete basis exactly `[1]`, the input SHA-256, host and msolve version, and an independent parse/evaluation. Such a fully validated EMPTY would be an emitter/parser/solver regression, because the exact rational point proves SAT. The input deliberately obeys the no-parentheses rule in [AUDIT.md:426](../AUDIT.md#L426)--[439](../AUDIT.md#L439).

For modular regressions, validate primality; exclude primes dividing cleared denominators, derivative coefficients/exponents, or fixed nonzero guard data; preserve exponent tokens; pre-reduce every coefficient to \([0,p)\); independently parse/evaluate every row; and run the constant-term smoke required at [AUDIT.md:565](../AUDIT.md#L565)--[577](../AUDIT.md#L577).

### 6.6 The necessary next computational tier

The intended future command contract is

```sh
python3 cases/td7_gluing.py emit \
  --tier full-route \
  --reading q-e5 \
  --cell 18,27,13,9 \
  --mu0 5 \
  --arrival-state 2/5,5 \
  --arrival-cell 35,15,7,5 \
  --certificate eq_t63_n3 \
  --out systems/td7_gluing/18_27_13_9/eq_t63_n3/system.ms
```

This CLI is **NOT IMPLEMENTED**; `lib/td7_gluing.py` and `cases/td7_gluing.py` do not exist. A correct `--tier full-route` implementation must refuse until it has certified tower labels, top patterns, transport windows, root data, and the global Jacobian rows listed at [sol-gluing-design.md:1218](sol-gluing-design.md#L1218)--[1241](sol-gluing-design.md#L1241) and [1582](sol-gluing-design.md#L1582)--[1606](sol-gluing-design.md#L1606).

A genuine full tower/jet system belongs on Box02 with `-t 8` and the default 43200-second cap. Resolve Box02's current IP, start it only under the fleet coordinator's policy, run `sudo ldconfig`, inspect the existing queue/crontab, and never stop it while other lanes run ([ops/FLEET.md:12](../ops/FLEET.md#L12)--[39](../ops/FLEET.md#L39)).

**CONJECTURE (FULL-ROUTE SURVIVAL).** The exact leading anchor above extends to one dependency-complete finite necessary-condition certificate containing the missing tower, window, root, and global Jacobian rows. A future full-route system can test this finite survival conjecture: EMPTY kills that certified route, whereas SAT proves only finite-route compatibility. SAT would not prove an all-orders object or a Keller counterexample. Even EMPTY kills only that route unless every relevant unequal-index route and neutral family has been certified and exhausted.

## 7. Dependency ledger

| assertion | status | dependency |
|---|---|---|
| Notation 3.5 has P and Q values (1) at a case-III vertex | **PROVED** | Puiseux denominator definitions |
| Q/jump/max is the unique uniform global repair of \(\kappa_F\) | **PROVED** | Statement 3.8; Proposition 5.5; explicit model |
| E5 formulas (4) | **PROVED** | Q-value; Statement 3.17(ii); Proposition 9.3(e) |
| printed (g),(h) agree with E5 iff indices are equal | **PROVED** | positivity and denominator comparison |
| unequal-index case-III local configuration satisfying the isolated Prop. 8.1(iv) equation exists | **PROVED** | explicit polynomials (7),(15) |
| every relevant actual td-7 class-C edge has equal indices | **CONJECTURE \(U_{7C}\)** | no independent proof found |
| every normalized-counterexample case-III edge has equal indices | **CONJECTURE \(U_{\rm global}\)** | stronger than needed; no proof found |
| some relevant actual td-7 class-C edge has unequal indices | **CONJECTURE (\(\neg U_{7C}\))** | local model and transition-graph record are not Keller realizations |
| 69-row \((18,27)\) leading prefix is SAT | **PROVED, not H5a-discriminating** | displayed rational anchor |
| leading anchor extends to a dependency-complete finite route | **CONJECTURE (FULL-ROUTE SURVIVAL)** | missing certified global data |
| 17 cells / 233 deduplicated routes within the filed closure | **PROMOTED, conditional on filed P0/P3/arrival/closure/budget hypotheses** | `BOOK-OFFAXIS.md` §11a and hostile replay |
| 2-cell restriction | **PROVED conditional on \(U_{7C}\) and the same census perimeter** | equal-index re-enumeration |

## Final disposition

H5a is no longer open as a uniform global convention: **use the Q/jump/max value.** With that value, the thesis's own transport calculus gives E5. There is no independent derivation of forced \(\nu_F=\nu_G\) on the relevant td-7 class-C edges; imposing it is exactly **CONJECTURE \(U_{7C}\)**.

Therefore, under the filed P0/P3/arrival/closure/budget hypotheses, the promoted td-7 work queue is the **17-cell Q+E5 book**. The 2-cell book is not a sound theorem-level replacement. **Forced-\(\nu\) is dead as a thesis-derived shortcut.**
