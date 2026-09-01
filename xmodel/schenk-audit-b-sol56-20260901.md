# Hostile Audit B (SOL56): Schenk’s Claimed Proof of JC2

## 1. Scope, frozen inputs, and method

This is a primary-text audit of Philipp Schenk, *A Valuation-Theoretic Proof of the Jacobian Conjecture in Dimension Two*, dated 2026-02-12 (53 PDF pages, including front matter and bibliography). Page references below are the printed page numbers in the paper; “PDF p.” is used only when ambiguity matters. The audit reconstructs the dependencies actually written, tests each numbered result, and distinguishes a true statement with a repairable proof from a premise that is never obtained.

The mandated SHA-256 check was performed before any charged input was read. All three hashes matched:

| frozen input | SHA-256 |
|---|---|
| `schenk_jc2_zenodo18622130.pdf` | `6ba4088386eb40affbb4abad54bb8e1574de09d00da9d1fbeac9f5c88d160f24` |
| `web-sweep-20260901-grok46.md` | `23fab48635178dd905d67be2b9d0eeb8574b641be0d097c82af4a55bf4fcc7d4` |
| `block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md` | `763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9` |

No CAS was run, no `jc2-lean` material was inspected, and no additional literature was fetched. The countermodels below are explicit schemes or rings checked by hand. Status terminology is strict: **VERIFIED** means the statement follows (occasionally by a short repair explicitly supplied); **GAP** means the claimed conclusion may be true in the Keller setting but is not proved by the stated inputs; **FALSE** means the statement or a necessary displayed assertion has a direct counterexample. Conditional results are not credited as establishing their unmet hypotheses.

## 2. Executive verdict

**VERDICT: FATALLY-FLAWED.** The manuscript does not prove JC2. Its core contains several independent false steps, not one local omission.

1. **U-HIT is not proved** (Theorem 5.3, pp. 16–17). The selected point
   \(s\in C\cap S^\circ\cap S^{\circ\circ}\) need not exist: a dense open of \(\mathbb A^2\) can omit the whole fixed curve \(C\). Indeed, the open where the original affine map becomes finite is expected to omit its nonproperness curve. Lemma 5.1 also falsely identifies a scheme-theoretic fiber with a base change of \(f_*\mathcal O_X\).
2. **The Rees family is not defined** (Chapter 7). The ring
   \(\mathcal R=\bigoplus_{m\ge0}(t^m)s^m=R[ts]\subset R[s]\) does not contain \(s\), hence has no asserted \(k[s]\)-algebra structure, generic fiber “\(s\ne0\),” or special fiber “\(s=0\).” Moreover, specialization does not commute with taking an image without the strictness equality \(B\cap s\mathcal R=sB\), which is neither stated nor proved.
3. **The dicritical parameter is erased.** The claimed special algebra is written over \(\kappa(D)\). If \(v_D(P)=v_D(Q)=0\), then \(F_0,G_0\in\kappa(D)\), so \(\kappa(D)[F_0,G_0]=\kappa(D)\) has dimension zero even when \(D\to C\) is nonconstant. If instead one retains the correct ground field \(k\), the ambient \(\kappa(D)[T]\) has two sources of transcendence and the rank-one conclusion does not follow. No result supplies the \(k\)-coefficient relation required by Lemma 8.9 and used in Chapter 9.
4. **A zero of the Jacobian form at a boundary ramification divisor is not a contradiction.** Lemma 10.2 falsely infers that a divisor lying over the target torus lies in the source affine chart. Chapter 10 then repeats the same error as “\(D\) dominates a curve, hence meets \(U\).” On a boundary dicritical, the Keller identity is an identity of rational forms and permits \(dx\wedge dy\) to vanish or have a pole. Positive order at tame ramification is precisely the expected different exponent, not evidence that the divisor lies in \(U\).

The finite-étale triviality and birational/Zariski-main tail are essentially standard after repair, but their only input is the unproved Theorem 10.3. Neither the promoted campaign machinery nor a minor correction fills these failures: doing so would require new global control of the nonproperness/branch divisor and would contain the unresolved heart of JC2.

## 3. Reconstructed logical skeleton

The written dependency chain is:

```text
Keller pair (P,Q)
  -> normalized projective graph X, affine-target part X0, U ~= A^2       [2.1–2.6]
  -> proper f:X0->A^2 and Stein factor X0 -rho-> Y0 -sigma-> A^2         [3.1–3.5]
  -> rank-d finite-flat open for sigma; rank-d finite-etale open for F    [4.1–4.2]
  -> equal fiber lengths, hence no horizontal D in X0\U (“U-HIT”)        [5.1–5.3]
  -> DVR R=O_{X0,eta_D}, P=t^a u, Q=t^b v, initial forms F0,G0           [6.1–6.2]
  -> flat Rees/image family transports dicritical dimension to B0        [7.1–7.8]
  -> dim B0=1 gives an adapted residue character; somehow c lies in k    [8.1–8.10]
  -> adapted k-character and a+b>0 force ord_D(dP wedge dQ)>0             [9.1]
  -> branch C lifts to dicritical D; branch forces a+b>0                  [10.1–10.2]
  -> U-HIT puts D in U, where Keller gives order 0; contradiction         [10.3]
  -> sigma finite etale -> sigma ~= A^2 -> F birational                   [11.1–12.1]
  -> F etale and birational -> open immersion -> automorphism             [12.2–12.4]
```

More exactly, Chapters 2–3 construct \(X_0=f^{-1}(\mathbb A^2)\), with \(U\cong\mathbb A^2\) the original affine graph, and assert that \(Y_0\) is the normalization of \(\mathbb A^2\) in \(k(x,y)\). Chapter 4 produces two unrelated dense opens: \(S^\circ\), where the finite map \(\sigma\) is flat of rank \(d=[k(x,y):k(P,Q)]\), and \(S^{\circ\circ}\), where \(F\) is finite étale of degree \(d\). Lemmas 5.1 and 5.2 are then the sole stated inputs to U-HIT.

For a proposed horizontal divisor \(D\), Chapter 6 sets \(a=v_D(P)\), \(b=v_D(Q)\) and \(F_0=u_0T^a\), \(G_0=v_0T^b\). Lemmas 7.1–7.5 purport to build a flat \(k[s]\)-family whose fibers are the original image algebra and \(\kappa(D)[F_0,G_0]\). Lemma 7.6 is the dimension-semicontinuity link; Lemma 7.7 supplies generic dimension from dicriticality; Corollary 7.8 supplies special dimension at least one. Since the latter algebra lies in a one-variable polynomial ring over \(\kappa(D)\), Chapter 8 takes its dimension to be one.

Lemmas 8.1–8.3 then produce
\[
  ma+nb=0,\qquad u_0^m v_0^n=c\in\kappa(D)^\times.
\]
This relation is tautological for two Laurent monomials and is not yet the hypothesis of Lemma 9.1. Lemma 8.9 upgrades \(c\) to \(k^\times\) only **if** a nonzero relation \(H(F_0,G_0)=0\) with \(H\in k[U,V]\) exists. No later result proves that hypothesis. Nevertheless §10.4 says simply “the character relation implies” wedge strictness. This is a missing dependency edge. There is a second mismatch: Chapter 8 fixes \(a,b>0\), whereas Lemma 10.2 yields only \(a+b>0\); Lemma 9.1 treats the one-zero cases only conditionally on the unproved \(k\)-character.

Finally, Lemma 10.1 selects a divisor over a branch curve, Lemma 10.2 is meant to give \(a+b>0\), and Lemma 9.1 gives positive differential order. Section 10.4 gets order zero not from any global divisor formula, but from the assertion that a divisor dominating an affine curve meets \(U\). That assertion is exactly what U-HIT was supposed to establish. Indeed, if U-HIT were valid, Lemma 10.1 plus generic étaleness on \(U\) would already exclude a branch divisor; Chapters 6–9 would be unnecessary. Thus the entire proof is concentrated in the invalid Chapter 5 separation, with Chapters 7–10 adding further invalid routes rather than repairing it.

## 4. Lemma-by-lemma verification ledger

### 4.1. Main theorem through the degeneration

| location | status | independent check and actual dependency |
|---|---|---|
| Thm. 1.1 | **GAP** | This is JC2 itself. It consumes Theorem 10.3, which is not established. |
| Lemma 2.1 | **VERIFIED** | The affine graph is isomorphic to \(\mathbb A^2\), hence it and its closure are irreducible. |
| Lemma 2.2 | **VERIFIED** | Over the two affine charts the closure is the already-closed affine graph; normalization is an isomorphism over this smooth open, so \(f\) restricts to \(F\). |
| Lemma 2.3 | **VERIFIED** | Nonzero Jacobian makes \(P,Q\) algebraically independent (equivalently \(F\) dominant), hence the extension \(f\) is dominant. |
| Lemma 2.4 | **VERIFIED** | This repeats Lemma 2.2 and names the dense open \(U\cong\mathbb A^2\). |
| Lemma 2.5 | **VERIFIED** | Keller makes \(F\), and therefore \(f\), dominant and generically separable. |
| Lemma 2.6 | **VERIFIED** | An open of the normalization of an integral surface is an integral normal surface; its height-one local rings are DVRs. |
| Lemma 3.1; Prop. 3.2 | **VERIFIED** | Properness survives restriction to the inverse image of the affine target, and Stein factorization applies. |
| Lemma 3.3 | **VERIFIED after repair** | Its sentence “finite over a normal scheme implies normal” is false. Here normality follows instead from \(\rho_*\mathcal O_{X_0}=\mathcal O_{Y_0}\): sections on inverse images of affine opens in the normal integral \(X_0\) are integrally closed. |
| Lemma 3.4 | **VERIFIED** | The generic fiber is the finite field extension \(k(x,y)/k(P,Q)\), so \(k(Y_0)=k(X_0)\) and \(\rho\) is birational. |
| Lemma 3.5 | **VERIFIED** | Duplicate of Lemma 3.4. With repaired Lemma 3.3, finite normal \(Y_0\) is indeed the normalization of the target in the common field. |
| Lemma 4.1 | **VERIFIED** | Generic freeness gives a finite-flat rank-\(d\) restriction of \(\sigma\). |
| Lemma 4.2 | **VERIFIED after minor repair** | A dominant quasi-finite map is finite over a suitable dense target open; étaleness persists and the degree is the common function-field degree. ZMT alone needs the additional step of deleting the finite image of the complement in its finite envelope. |
| Lemma 5.1 | **FALSE** | Proper base change does not identify \(\mathcal O_{f^{-1}(s)}\) with \((f_*\mathcal O_X)\otimes\kappa(s)\); the latter concerns global functions, not the fiber scheme. A blow-up \(\operatorname{Bl}_0\mathbb A^2\to\mathbb A^2\) has \(f_*\mathcal O=\mathcal O\), rank one, but its fiber over \(0\) is \(\mathbb P^1\), with no finite length. Nothing earlier proves \(f\) quasi-finite at every \(s\in S^\circ\). |
| Lemma 5.2 | **VERIFIED** | On the chosen finite étale open, each closed fiber has \(d\) reduced points. |
| Theorem 5.3 (U-HIT) | **GAP—fatal** | The proof needs \(C\cap S^{\circ\circ}\ne\varnothing\), but a dense open of the surface may omit all of \(C\). The explicit blow-up model in §5 below satisfies every bullet claimed in Remark 5.4 and has a horizontal boundary curve. Fiber additivity is available only after finiteness is known and does not cure the empty intersection. |
| Lemma 6.1 | **VERIFIED** | Target coordinates pull back to regular functions on \(X_0\), hence have nonnegative order along every prime divisor. |
| Lemma 6.2 | **VERIFIED** | The residue field is the function field of an integral \(k\)-curve, and algebraically closed \(k\) is its own algebraic closure there. |
| Lemma 7.1 | **FALSE** | \(R[ts]\) does not contain \(s\), so it is not the asserted \(k[s]\)-algebra. The claimed flat morphism and both fibers are undefined. Reduction “modulo \(s\)” inside \(R[ts]\) is meaningless. |
| Lemma 7.2 | **FALSE/undefined** | The map \(k[s][U,V]\to\mathcal R\) cannot be formed. Torsion-free over a PID would imply flatness only after a genuine injective base-ring map existed. |
| Lemma 7.4 | **GAP** | Being a subring of a domain would prove domainness for a corrected \(B\), but the stated \(B\) is undefined. Its dominance argument (“generic fiber nonzero”) is also vacuous: every unital fiber contains 1 if it exists. |
| Lemma 7.5 | **FALSE** | Generic specialization gives an algebra such as \(k(s)[P,Q]\), not the field “\(\operatorname{im}k(P,Q)\).” Specialization of an image requires \(B\cap s\mathcal R=sB\). For \(B=k[s,sx]\subset k[s,x]\), \(B/sB\cong k[z]\), while its image after setting \(s=0\) is only \(k\). The further replacement of \(k[F_0,G_0]\) by \(\kappa(D)[F_0,G_0]\) is an unjustified scalar extension. |
| Lemma 7.6 | **FALSE as stated** | A finitely generated flat algebra can have empty special fiber: \(B=k[s,s^{-1},x]\) is flat and has a one-dimensional generic fiber but \(B/(s)=0\). Dominance does not imply that the point \(s=0\) is in the image. Extra hypotheses can yield the familiar dimension inequality, but they are absent. |
| Lemma 7.7 | **FALSE in its use of \(B_\eta\)** | Keller gives \(P,Q\) algebraically independent in the full function field. Thus a corrected \(k(s)[P,Q]\) has relative dimension two, whereas the displayed “image of \(k(P,Q)\)” is a field of Krull dimension zero. Dicriticality concerns the residues on \(D\), not \(P,Q\) in \(\operatorname{Frac}R\). The inference “between 1 and 2, hence 1” is invalid. |
| Cor. 7.8 | **FALSE** | If \(a=b=0\), then \(F_0,G_0\in\kappa(D)\) and \(\kappa(D)[F_0,G_0]=\kappa(D)\) has dimension zero, even when \(k(F_0,G_0)\) has transcendence degree one over \(k\). This is precisely the lost dicritical parameter. |

### 4.2. Rank, wedge, branch, and the standard tail

| location | status | independent check and actual dependency |
|---|---|---|
| Lemma 8.1 | **VERIFIED** | A prime kernel of quotient dimension one in the two-variable polynomial ring \(K[U,V]\) has height one. |
| Lemma 8.2 | **VERIFIED** | Laurent monomials are linearly independent over \(K=\kappa(D)\). |
| Theorem 8.3; Cor. 8.6 | **VERIFIED but tautological** | For \(a,b>0\), take \(g=\gcd(a,b)\), \((m,n)=(b/g,-a/g)\); then \(F_0^mG_0^n=u_0^mv_0^n\in K^\times\). No dimension hypothesis is needed. The written proof wrongly reduces a same-weight coefficient sum to two selected terms; there may be more. Crucially, the resulting “constant” is an arbitrary function in \(K\), not an element of \(k\). |
| Lemma 8.7 | **VERIFIED** | Duplicate of Lemma 6.2. |
| Lemma 8.9; Cor. 8.10 | **VERIFIED after repair, conditional only** | The two-term argument is again invalid. A repair groups \(H\) by \((a,b)\)-weight; a nonzero weight component becomes a one-variable polynomial over \(k\) in \(u_0^{b/g}v_0^{-a/g}\). Since \(k\) is algebraically closed in \(K\), that ratio lies in \(k\). But the required nonzero \(H\in k[U,V]\) is never produced by Chapter 7 or anywhere else. |
| Lemma 9.1 | **VERIFIED after correcting its calculation** | Its hypotheses do imply the valuation jump at the smooth generic point of \(D\). The text incorrectly says \((a,b)\) is proportional to \((m,n)\); \(ma+nb=0\) instead gives \((m,n)\parallel(b,-a)\). It also swaps \(u,v\): the leading coefficient is \(b v_0\,du_0-a u_0\,dv_0\), which the correctly differentiated character does kill. The one-zero cases follow from the differential transitivity sequence. The lemma remains unusable because its \(k^\times\)-character hypothesis is unmet. |
| Lemma 10.1 | **VERIFIED after repair** | Proper birationality supplies the strict transform of a prime divisor \(E\subset Y_0\), which dominates \(E\). The manuscript’s stated reason—every DVR of the common field is realized by a divisor on any normal model—is false; a valuation can have a codimension-two center. |
| Lemma 10.2 | **FALSE** | Units \(P,Q\) merely say that the generic image lies in \(\mathbb G_m^2\); they say nothing about ramification and do not put \(\eta_D\) in \(U\). A direct finite countermodel is \(\mathbb A^2_{r,s}\to\mathbb A^2_{P,Q}\), \(P=1+r^2, Q=1+s\): it ramifies along \(r=0\), while both target coordinates have valuation zero there. The asserted conclusion is also not invariant under target translations, whereas ramification is. |
| Theorem 10.3 | **GAP—fatal** | It consumes U-HIT, the nonexistent degeneration, the missing \(k\)-character, and false Lemma 10.2. The last sentence “finite unramified implies étale” is false without flatness, though flatness can be repaired here by the Cohen–Macaulay/miracle-flatness argument for a finite normal surface over the regular surface \(\mathbb A^2\). |
| Theorem 11.1 | **VERIFIED** | \(\mathbb A^2\) has trivial geometric étale fundamental group in characteristic zero, by descent to a finitely generated field, embedding into \(\mathbb C\), and comparison. For arbitrary \(k\) and \(\mathbb C\), one routes through algebraic closures of the common field of definition rather than treating one as an extension of the other. |
| Cor. 11.2 | **VERIFIED conditionally** | A connected finite étale cover of \(\mathbb A^2\) is degree one. It cannot be applied because Theorem 10.3 fails. |
| Prop. 12.1 | **VERIFIED conditionally** | If \(\sigma\) is an isomorphism, the function fields agree and \(F\) is birational. |
| Lemma 12.2 | **FALSE** | For the dense open \(U=D(x)\subset\mathbb A^2\), \(1/x\) is regular and \(\Gamma(U,\mathcal O)=k[x,y,1/x]\), not \(k[x,y]\). Normality extends across codimension at least two, not across divisors. |
| Lemma 12.3 | **VERIFIED after repair** | A proper open subset of \(\mathbb A^n\) is not isomorphic to \(\mathbb A^n\): a divisorial complement creates a nonconstant unit; if the complement has codimension at least two, Hartogs gives the same global ring and affineness forces the inclusion to be all of \(\operatorname{Spec}k[x_1,\dots,x_n]\). The manuscript incorrectly asserts every nonempty complement has a divisor and also invokes false Lemma 12.2. |
| Lemma 12.4 and final conclusion | **VERIFIED conditionally after the preceding repair** | A birational quasi-finite map factors as an open immersion into a finite birational model, which is the normal target. Lemma 12.3 then gives surjectivity. The general sentence “a birational open immersion into a normal variety is surjective” is false, but the \(\mathbb A^2\)-specific result suffices. |
| Appendix Lemma A.5 | **VERIFIED** | With a chosen uniformizer (so not canonically without that choice), \(\operatorname{gr}R\cong\kappa[T]\). |
| Appendix Lemma A.7 | **VERIFIED** | A genuine polynomial identity has a vanishing minimal-valuation initial part. No such identity in \(k[P,Q]\) exists for a Keller pair itself, since \(P,Q\) are algebraically independent. |
| Appendix Lemma A.8 | **FALSE as displayed** | \(\Omega^2_{R/k}/t\Omega^2_{R/k}\not\cong\Omega^2_{\kappa/k}\). For \(R=k[z,t]_{(t)}\), \(\kappa=k(z)\): \(dt\wedge dz\) is nonzero modulo \(t\), while \(\Omega^2_{k(z)/k}=0\). The tautology “zero in the actual quotient implies divisibility by \(t\)” is valid. |
| Appendix Lemma A.9 | **VERIFIED in context** | Localization alone is not injective on a module with torsion, contrary to the proof. Here the codimension-one point of a normal finite-type surface over perfect \(k\) is smooth, so \(\Omega^2\) is locally free and localization is injective. |

## 5. U-HIT and the horizontal-boundary step

The exact failure is at p. 16, immediately after setting \(C=f(D)\): “Choose \(s\in C\cap S^\circ\cap S^{\circ\circ}\). This intersection is nonempty since all three sets are dense open.” Only \(S^\circ\) and \(S^{\circ\circ}\) are dense open in \(\mathbb A^2\); \(C\) is a closed curve. Either open can omit \(C\) entirely. In particular, \(S^{\circ\circ}\) was obtained by deleting target values at which \(F\) is not finite, so a horizontal boundary image is exactly what may be deleted.

There is a desk-scale countermodel to the claimed “pure fiber-length” principle. Let
\[
 f:X=\operatorname{Bl}_{(0,0)}\mathbb A^2_{p,q}\longrightarrow\mathbb A^2_{p,q}
\]
and take the blow-up chart
\(U\cong\mathbb A^2_{x,y}\) with \(p=x,q=xy\). Thus \(f|_U=(x,xy)\). The complement \(D=X\setminus U\) is the strict transform of \(p=0\) and maps isomorphically onto \(C=\{p=0\}\). The Stein finite map is the identity, so \(d=1\) and one may take \(S^\circ=\mathbb A^2\). Over \(S^{\circ\circ}=\{p\ne0\}\), however, \(f|_U\) is an isomorphism, hence finite étale of degree one. Thus every bullet in Remark 5.4 holds, yet the prohibited horizontal boundary exists and \(C\cap S^{\circ\circ}=\varnothing\). At the origin the full fiber is \(\mathbb P^1\), directly disproving Lemma 5.1’s “length \(d\)” assertion. (This model is not Keller; its purpose is exact: it disproves the claim that the listed generic fiber facts imply U-HIT. The manuscript uses no further Keller input in that proof.)

Purity does not repair this. Purity says that non-étaleness of the finite normal cover \(Y_0\to\mathbb A^2\) appears in codimension one; it does not say that the corresponding strict transform on \(X_0\) enters \(U\). In fact, because \(F\) is étale on \(U\), a ramification divisor of \(\sigma\) must have its strict transform in the boundary. A valid U-HIT theorem would therefore already eliminate the branch divisor and nearly complete the proof. Establishing it requires global control of the nonproperness curve, not generic fiber counting. None of the promoted purity/branch-locus results supplies that unconditional control.

## 6. Rees degeneration of affine dicriticals

Chapter 7 fails before dimension is considered. For a DVR \((R,(t))\), the ordinary Rees ring written in the paper is
\[
 \mathcal R=\bigoplus_{m\ge0}(t^m)s^m=R[ts]\subset R[s].
\]
It contains \(ts\), but not \(s\): otherwise comparison of the coefficient of \(s\) would put \(t^{-1}\) in \(R\). Consequently the inclusion \(k[s]\subset\mathcal R\), the morphism to \(\mathbb A^1_s\), localization at \(s\), and quotient by \(s\) on pp. 23–24 do not exist. A standard deformation uses an extended Rees construction and a parameter with the opposite grading; substituting that construction would change all subsequent formulas and does not validate them automatically.

Even granting a corrected family, Lemma 7.5 uses the generally false equality
\[
 B/sB=\operatorname{im}\bigl(k[U,V]\to\mathcal R/s\mathcal R\bigr).
\]
The kernel is \((B\cap s\mathcal R)/sB\), so equality requires a strict/saturated filtration. The example \(B=k[s,sx]\subset k[s,x]\) makes the defect visible: abstractly \(B/sB\cong k[z]\), but specialization of its image sends \(z=sx\) to zero and yields only \(k\). No strictness, saturation, or Gröbner/initial-ideal theorem is proved for Schenk’s image algebra.

The claimed fibers also mix incompatible coefficient fields. Dicriticality says that the residues of \(P,Q\) generate a transcendence-degree-one field over \(k\). After adjoining all of \(\kappa(D)\) as scalars, those residues become constants. Thus:

- over \(\kappa(D)\), \(\kappa(D)[F_0,G_0]\subset\kappa(D)[T]\) is one-variable, but when \(a=b=0\) it is just \(\kappa(D)\), of dimension zero, and it has forgotten the map \(D\to C\);
- over \(k\), the curve parameter in \(\kappa(D)\) remains visible, but the ambient algebra can have transcendence degree two, so the asserted rank-one Laurent character is not forced.

The generic side has the complementary error. In the fraction field of the DVR, a Keller pair \(P,Q\) is algebraically independent, so \(k(s)[P,Q]\) has relative dimension two. If one literally takes the paper’s \(\operatorname{im}(k(P,Q)\to\operatorname{Frac}R)\), it is a field and has Krull dimension zero. Dicriticality concerns reduction to \(\kappa(D)\), not the unreduced pair in \(\operatorname{Frac}R\). The sentence on p. 28 that transcendence degree is at least one and at most two “so necessarily” one is invalid.

Nor is the Keller condition preserved. Treating \(s\) as a base constant, the proposed lifts \(\widetilde P=s^aP\), \(\widetilde Q=s^bQ\) satisfy
\[
 d\widetilde P\wedge d\widetilde Q=s^{a+b}dP\wedge dQ.
\]
When \(a+b>0\)—the very case needed later—the special member has zero Jacobian form. If absolute differentials include \(ds\), extra terms appear instead; neither version is a Keller family. The manuscript never constructs a family of affine-plane maps, never proves preservation of a dicritical component, and never obtains a nonzero relation over \(k\). Repair would require a different, strict degeneration together with a theorem retaining both the residue-curve parameter and the Keller identity. That is new core mathematics, not a local edit.

## 7. Two-form positivity and polar bookkeeping

With the usual convention, positive \(\operatorname{ord}_D(\omega)\) means a zero and negative order means a pole. The conditional content of Lemma 9.1 can be repaired: from \(ma+nb=0\) one has \((m,n)\parallel(b,-a)\), and the actual leading coefficient of \(dP\wedge dQ\) is
\[
 b v_0\,du_0-a u_0\,dv_0,
\]
not \(b u_0\,du_0-a v_0\,dv_0\) as printed on p. 34. A genuine relation \(u_0^mv_0^n\in k^\times\) kills the corrected coefficient. But no such \(k\)-relation was obtained, and this local vanishing would not itself contradict Keller.

At a tame ramification divisor, vanishing is exactly what one expects. Locally, if a target parameter pulls back as \(z=t^e\) times a unit and a second parameter is transverse along \(D\), then
\[
 \operatorname{ord}_D(dz\wedge dw)=e-1.
\]
Thus for ramification index \(\mu=e\ge2\), the promoted reference identity \(v_D(dx\wedge dy)=\mu-1\ge1\) agrees with, rather than contradicts, Schenk’s desired positivity. It becomes a contradiction only if \(D\)’s generic point lies in \(U\), where \(x,y\) are regular affine coordinates and \(dx\wedge dy\) is a unit.

That last membership is never proved. Lemma 10.2 says that \(P,Q\) being units puts \(\eta_D\) in \(U\cap f^{-1}(\mathbb G_m^2)\); it puts it only in \(f^{-1}(\mathbb G_m^2)\). Section 10.4 similarly says “\(D\) dominates a curve in \(\mathbb A^2\), hence meets \(U\).” A horizontal boundary divisor is the direct negation. If U-HIT were available, one could infer the membership, but U-HIT is the fatal gap already identified.

The coordinate valuation test is also intrinsically unsuitable. A target translation can make both coordinate functions generically nonzero on any fixed branch curve, hence make \(v_D(P)=v_D(Q)=0\), without changing ramification. Conversely, \(v_D(P)>0\) says the entire image curve lies on the coordinate line \(P=0\). Lemma 10.2 would therefore force every branch component to be one of two coordinate axes, a non-invariant and false conclusion.

Finally, the global polar part is absent from the manuscript. On the original source \(\mathbb P^2\),
\[
 \operatorname{div}(dx\wedge dy)=-3L_\infty.
\]
On a normalized/resolved graph, pullback and discrepancy terms redistribute these poles and may create zeros on exceptional divisors. The rational Keller identity
\(dP\wedge dQ=(\det DF)dx\wedge dy\) remains true there, so every boundary order—positive or negative—appears on both sides. Schenk neither writes a canonical-divisor equality nor balances the \(-3L_\infty\) contribution against exceptional terms. The only order-zero argument is the invalid assertion that \(D\) lies in \(U\). Hence “positivity” supplies no global contradiction.

## 8. Finite-étale triviality and Zariski’s Main Theorem

This tail is not the source of the claimed breakthrough. If one had actually shown that \(\sigma:Y_0\to\mathbb A^2\) is unramified, its missing flatness could be supplied: a normal two-dimensional finite algebra is Cohen–Macaulay, and miracle flatness over the regular two-dimensional target makes it locally free. It would then be finite étale. The manuscript’s unrestricted sentence “finite unramified is étale” is false (a finite closed immersion gives a basic counterexample), but is repairable in this particular equidimensional setting.

Theorem 11.1 is standard. Finite étale covers descend to a finitely generated characteristic-zero field, geometric base change reaches \(\mathbb C\), and Riemann existence identifies covers of \(\mathbb A^2_\mathbb C\) with covers of the simply connected space \(\mathbb C^2\). Since \(Y_0\) is irreducible, a trivial finite cover would have one sheet. Consequently \(\sigma\) would be an isomorphism and \(k(P,Q)=k(x,y)\).

From that conditional birationality, Keller makes \(F\) étale and hence quasi-finite. Zariski’s Main Theorem makes it an open immersion after the finite birational intermediate model is identified with the normal target. The paper’s Lemma 12.2 is false, and its proof of Lemma 12.3 misses codimension-two complements, but the required \(\mathbb A^2\)-specific conclusion is repairable: a divisorial complement gives a nonconstant unit on an alleged copy of \(\mathbb A^2\); a codimension-at-least-two complement has the same global coordinate ring by normality and cannot itself be affine with that spectrum unless it is all of \(\mathbb A^2\). Thus a birational Keller map would indeed be an automorphism.

The feed into this sound conditional tail is absent. Theorem 10.3 has not established unramifiedness in codimension one, so Chapters 11–12 cannot be activated.

## 9. Comparison with the promoted reference frame

The charged integration states only that, under H2 (irreducible \(A_F\)), an affine-image dicritical with \(\mu=1\) is excluded; it explicitly leaves reducible \(A_F\) configurations at \(N=5\) and above (integration lines 22–35 and 65–73). Ramified dicriticals with \(\mu\ge2\) remain compatible with the promoted local identities and weighted budgets. Schenk claims much more: U-HIT would remove every horizontal source-boundary curve, without H2, degree restrictions, branch-shape hypotheses, or budget analysis.

That disparity pinpoints—not prejudges—the necessary new work. The new work would have to control the finite-open complement along the actual nonproperness curve, retain the normalization-selected branch valuation through degeneration, and show why every ramified/reducible survivor is impossible. Instead:

- U-HIT samples only the generic finite locus and cannot sample a curve wholly contained in its complement;
- the Rees argument conflates the physical divisor parameter \(\kappa(D)\), its place, and the grading parameter \(T\), then makes \(\kappa(D)\) the coefficient field and loses dicritical variation;
- no typed branch/exit datum is transported through specialization, and no proof shows distinct divisors or ramification indices survive;
- the positive differential order \(\mu-1\) is treated as anomalous even though it is the promoted and standard local ramification formula.

The promoted \(Y=\operatorname{Spec}B\), four-box, \(e=1+v(dx\wedge dy)\), all-degree B0-under-H2, and weighted-budget results therefore do not fill Schenk’s holes. They provide strictly conditional obstructions and explicitly allow configurations that Schenk’s invalid universal steps purport to erase. Conversely, this audit does not use those survivors as a counterexample to JC2: it tests Schenk’s lemmas directly. The blow-up and finite-cover countermodels target his general inferences, while the failure to produce a Keller counterexample is exactly why the missing global claims cannot be assumed.

## 10. Final verdict and repair analysis

**FATALLY-FLAWED.** The first fatal break is Theorem 5.3 at printed p. 16: the curve \(C\) need not meet the dense open \(S^{\circ\circ}\). The accompanying Lemma 5.1 is independently false. The blow-up model in §5 is a concrete countermodel to every generic fiber-length premise that Remark 5.4 says is sufficient.

Even deleting Chapter 5 would not leave a repairable proof. Chapter 7 has no \(k[s]\)-family; specialization of its image algebra is unjustified; its generic and special dimensions use different coefficient fields; and the proposed scaling destroys the nonzero Jacobian at the special member. Chapter 8 never obtains the \(k\)-relation consumed by Lemma 9.1. Lemma 10.2 then makes the false, coordinate-dependent claim that branch ramification forces \(v(P)+v(Q)>0\), and §10.4 mistakes “lies over the affine target” for “lies in the source affine chart.” The ignored boundary order of \(dx\wedge dy\) makes the advertised positivity entirely compatible with ramification.

A repair would require, at minimum, a new theorem forcing a horizontal boundary divisor to meet \(U\) or otherwise excluding the nonproperness curve; alternatively it would require a genuine strict degeneration that preserves the relevant Keller/dicritical data and yields a relation over \(k\), plus complete canonical-divisor bookkeeping at infinity. None is present, and none follows from the charged promoted machinery. These are the heart of JC2, not editorial gaps. The standard finite-étale and ZMT tail remains conditional and does not change the verdict.

Accordingly, Schenk’s manuscript supplies no resolution of the two-dimensional Jacobian conjecture and creates no reason to withdraw or strengthen any promoted campaign theorem.

## Sources checked

- Philipp Schenk, *A Valuation-Theoretic Proof of the Jacobian Conjecture in Dimension Two*, Zenodo record 18622130, version dated 2026-02-12; frozen PDF SHA-256 `6ba4088386eb40affbb4abad54bb8e1574de09d00da9d1fbeac9f5c88d160f24`. Every chapter, numbered result, appendix lemma, and bibliography entry in the 53-page PDF was inspected.
- `web-sweep-20260901-grok46.md`, frozen SHA-256 `23fab48635178dd905d67be2b9d0eeb8574b641be0d097c82af4a55bf4fcc7d4`, especially lines 38–46, 66, 72–82, 138–158, and 224–244 for external status and routing of the Schenk claim.
- `block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md`, frozen SHA-256 `763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9`, especially lines 22–35 and 65–73 for the exact scope of B0 under H2 and the surviving reducible cases.

No additional source was downloaded. Standard facts used in the independent checks (Stein factorization, strict transforms under proper birational maps, purity, miracle flatness, Riemann existence, and Zariski’s Main Theorem) were used only in their conventional forms; the audit does not depend on accepting a prior validator’s conclusion.

<!-- BODY-END -->
