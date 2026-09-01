# Hostile review: N20-ESCAPE / Theorem 7.B

## 1. Verdict and exact proposed scope

**Verdict: Theorem 7.B is CONFIRMED AFTER REPAIR and is an all-degree theorem at the H2/B0 scope.** The N=20 packet is independently dead. The decisive §7 link argument also survives hostile review once “the image branch” is localized to the normalization-selected germ and Orevkov’s distinguished inverse knot is replaced explicitly by the full inverse link. Those are necessary proof repairs, not new hypotheses.

The exact conclusion is: for a noninvertible plane Keller map of geometric degree \(N\ge3\), if \(A_F\) is irreducible, no affine-image dicritical has \(\mu_l=1\). Thus \(b=0\) and the promoted strict budget gives \(2m\le\sum_l\mu_l\le N-2\) at every such degree. H3 is not assumed: a hypothetical trivial dicritical forces \(\widetilde A_F\simeq\mathbb A^1\) by the degree-free cover/Riemann–Hurwitz argument.

The all-degree proof is independent of packet (4.9), \(R\), and the \(N=20\) equality arithmetic. It proves that every local surface excess \(k_l\) vanishes; the exact correction budget then forces \(a=1\), while the promoted H2 Euler calculation forces \(2a>N\), a contradiction for \(N\ge3\). If the §7 extension were withheld, the concentration/budget argument would still kill N=20 and move the first numerical frontier to \(N\ge26\).

Promotion must not overrun this scope. The no-excess lemma is conditional on H2 plus the hypothetical trivial dicritical, not a general law. Reducible \(A_F\), unconditional \(2m\le N-1\), and all without-H2 work remain untouched by Theorem 7.B. The old `OPEN[PI1-S4]` wording in N20 is no longer the exact current ledger label under the newer charged COORD; §10 records the replacement.

## 2. Input integrity and audit method

All four frozen inputs matched the charged SHA-256 values before reading:

```text
46c5f62fe92fd5ecbd12b1f74d83d272624253f1f06e9324c9fa1b1c21eac619  n20-escape-kill-opus5-20260901.md
621f1356b3b5290e32c2f2bf689b4d9a49412cb852066886a34b580366cb1652  b0-all-n-eta-criticality-sol56-20260831.md
f865204a3fd2ee3a6944b6739ae581cf29c41a7f2259bbc54cd1587ddf397a46  b0-all-n-hostile-review-grok46-20260831.md
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc  block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
```

I use **N20**, **ALL-N**, **REV**, and **COORD** for those files in that order; line references are to the frozen copies. The two local primary PDFs cited by N20 were independently rehashed and read directly:

```text
f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db  refs/jc86.pdf
88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad  refs/zoladek2008_official.pdf
```

The first is S. Yu. Orevkov, *On three-sheeted polynomial mappings of C2*, DOI 10.1070/IM1987v029n03ABEH000984; the load-bearing text is Lemmas 2.1, 3.1, 4.2, and 5.2 on PDF pp. 2–9. The second is H. Żołądek, *An application of Newton–Puiseux charts to the Jacobian problem*, DOI 10.1016/j.top.2008.04.001; Proposition 6.5(b) is on printed pp. 457–458 / PDF pp. 27–28. No CAS or uncertain-duration computation was run, and `jc2-lean` was not inspected. This review asserts no exit price and supplies no exit-price declaration.

## 3. Statement reconstruction and dependency graph

The flagship statement actually under review is:

> Let \(F:\mathbb C^2\to\mathbb C^2\) be a noninvertible plane Keller map of geometric degree \(N\ge3\), and assume H2: \(A_F\) is irreducible. Then no affine-image dicritical has \(\mu_l=1\).

Its dependency chain is

```text
H2 + hypothetical μ0=1
  -> finite normalization cover; l' ≅ A1
  -> s0=1, D~ ≅ A1, η immersive (H3 is derived)
  -> corr support = ramification support of h_l
  -> Orevkov local normal form: one finite carrier site t0
  -> full-inverse-link argument: k_l=0
  -> corr_l=μ_l(s_l−1)
  -> Orevkov budget gives W=N−1; fibre budget gives a=1
  -> promoted Euler inequality 2a>N
  -> N<2, contradiction.
```

The separate \(W,d,R,q'\) calculation kills the N=20 packet and excludes all \(N\le25\) even if the link step were withheld. It is a fallback branch, not a dependency of Theorem 7.B.

The exact consequence is \(b=0\) under H2 for every candidate degree \(N\ge3\). Hence every dicritical has \(\mu_l\ge2\), and the promoted H2 strict budget gives
\[
2m\le\sum_l\mu_l\le N-2.
\]
This closes `OPEN[B0-H2-N>=20/RAMIFIED-NONPRIMITIVE-COVER]`; it does not make a without-H2 statement.

There is an editorial contradiction inside N20 that must be removed before integrating the source report: its “verdict up front” says the all-degree prize is not attained (N20:50–61), while Theorems 7.A/7.B and the typed conclusions say that it is (N20:471–583). This review tests the later theorem rather than treating the stale opening sentence as mathematical evidence.

## 4. Corr–ramification dictionary at promoted scope

Let \(t\in l'\), \(x=\pi(t)\), \(z=h_l(t)\), and \(p=\eta(z)\). These are, respectively, a parametrization point, a point of Orevkov’s contracted source, a normalization place, and a physical target point. Żołądek Proposition 6.5(b) applies to \(x\) on the quotient dicritical and says
\[
M_t:=\mu_xf^*>\mu_l\quad\Longleftrightarrow\quad d\phi_l(t)=0.
\]
It does not say that \(p\) is a singular physical point or that \(d\eta_z=0\). Orevkov Lemma 2.1 makes \(\pi|_l\) one-to-one: contracting the \(L_C\)-chain collapses its unique attachment but identifies no two finite points of \(l\). Thus the correction sum may be indexed by the associated \(t\)’s without identifying the four objects above (ALL-N:72–81, 152–171, 240–245; REV:91–109; Żołądek printed pp. 457–458).

Under the hypothetical trivial dicritical, §5 gives a common immersive \(\eta\) under H2. The chain rule then sharpens the dictionary to
\[
M_t>\mu_l\quad\Longleftrightarrow\quad dh_l(t)=0.
\]
If \(e_t\) is the local degree of \(h_l\), deformation to nearby regular normalization places and Orevkov Lemma 3.1 give
\[
k_t:=M_t-e_t\mu_l\ge0.
\]
Unramified points have \(M_t=\mu_l\), hence \(k_t=0\). Combining this with the finite RH count gives the correctly typed identity
\[
\operatorname{corr}_l
=\sum_t(M_t-\mu_l)
=\mu_l(s_l-1)+\sum_t k_t.                 \tag{4.1}
\]
This is ALL-N:233–273 and N20:84–86, 309–318. The first term is controlled by ramification; RH supplies no bound on the second.

N20’s new concentration lemma is also valid. Off the unique finite attachment \(t_0=l\cap L_C\), the total boundary has only the smooth component \(l\). Since \(\eta\) is immersive, the selected image branch is smooth. Orevkov Lemma 3.1 applies to the finite surface germ and gives local coordinates in which \(f=(u,v^{\mu_l})\). Consequently \(d\phi_l(t)\ne0\), \(e_t=1\), and \(M_t=\mu_l\) for every \(t\ne t_0\) (N20:185–239; Orevkov PDF pp. 2, 4–5). Therefore all finite ramification and all correction on a carrier are concentrated at \(t_0\). In characteristic zero,
\[
h_l(t)=c(t-t_0)^{s_l}+z_0,
\qquad
\operatorname{corr}_l=\mu_l(s_l-1)+k_l,       \tag{4.2}
\]
with one possible excess \(k_l\ge0\). This kills the two-simple-critical-point realization demanded by the N=20 equality packet.

Scope repair: Corollary 3.2 at N20:234–239 suppresses its ambient assumptions. Concentration as used here requires the hypothetical \(\mu_0=1\) and H2, through the common immersive normalization. It must not be promoted as an unconditional statement about all Keller dicriticals.

## 5. Degree-`s` cover, Riemann–Hurwitz, and the H3-free affine-line claim

**CONFIRMED over \(\mathbb C\), at the claimed all-degree scope.** Orevkov Lemma 2.1 is degree-free: every component of the boundary is a smooth rational curve, and each connected \(L_{FC}\)-component is a linear chain whose unique \(L_F\)-endpoint \(l\) meets \(L_\infty\) at one point. Therefore
\[
l'=l\cap f^{-1}(\mathbb C^2)\simeq\mathbb P^1\setminus\{\infty\}\simeq\mathbb A^1
\]
for every affine-image dicritical, without H2 or H3 (N20:90–96, 171–183; ALL-N:97–105; REV:57–67). The finite \(L_C\)-attachment is not the omitted point.

For an irreducible image component \(D_l\), normality of \(\mathbb C[t]\) gives the global factorization \(\phi_l=\eta_l\circ h_l\), including source points above physical singularities. The coordinate-ring argument makes \(h_l:\mathbb A^1\to\widetilde D_l\) finite, surjective, connected, and of degree \(s_l\) (ALL-N:107–125; REV:31–51). This keeps the source point \(t\), quotient point \(\pi(t)\), normalization place \(h_l(t)\), and physical point \(\eta_l(h_l(t))\) distinct.

If \(\mu_0=1\), the promoted Żołądek statement makes \(d\phi_0\ne0\) at every finite source point. The chain rule and surjectivity make \(h_0\) finite étale and \(\eta_0\) immersive everywhere. Complete to
\[
\bar h_0:\mathbb P^1\longrightarrow\bar D_0.
\]
The affine target normalization has exactly one missing point: every boundary point must have a projective preimage, while no finite source point maps there, so its full preimage is \(\{\infty\}\), with \(e_\infty=s_0\). In characteristic zero the cover is separable and tame. Riemann–Hurwitz is therefore
\[
-2=s_0(2g(\bar D_0)-2)+(s_0-1),
\]
which forces \(g=0\) and \(s_0=1\). Hence \(\widetilde D_0\simeq\mathbb A^1\) and H3 is a conclusion, not a hypothesis (ALL-N:127–150; REV:69–85).

This conclusion is componentwise even without H2. H2 is needed to say \(D_0=A_F\) and hence to use the same immersive normalization for every dicritical. It does not propagate across different components of reducible \(A_F\).

Once H2 supplies that common \(\widetilde D\simeq\mathbb A^1\), each \(h_l:\mathbb A^1\to\mathbb A^1\) is a degree-\(s_l\) polynomial. Its projective extension is totally ramified at infinity, so
\[
\sum_{t\in\mathbb A^1}(e_t-1)=s_l-1.
\]
RH controls this ramification divisor only. It does **not** bound the surface excess \(k_t\) or the magnitude of \(\operatorname{corr}_l\); N20 correctly rejects that naive N=20 kill at lines 145–167. In N20 Theorem 4.A, “totally ramified at the single point” must mean the single **finite** point; infinity is also totally ramified on the projective cover.

## 6. General corr bound and strict-budget consequence

Put
\[
W=\sum_l s_l\mu_l=N-a,
\qquad d=a-W=2a-N>0,
\]
and let \(q'\) be the number of carriers with \(s_l\ge2\). H2 strictness supplies a positive correction; by §4 at least one such carrier exists. A trivial dicritical has weight one, while every carrier has \(s_l,\mu_l\ge2\), so
\[
W\ge1+4q'.                                             \tag{6.1}
\]

For a carrier, (4.2) leaves at most one excess \(k_l\). If its physical image \(p\) were smooth, the promoted \(a\)-sheeted covering over the smooth stratum gives \(a_p=a\); the exact fibre identity then reads \(a+W+K_p=N\) and forces \(K_p=0\). Thus positive excess lies at \(p\in\operatorname{Sing}D\). Immersivity of \(\eta\) makes every physical branch smooth, so \(r_p=|\eta^{-1}(p)|\ge2\), and
\[
a_p+r_pW+K_p=N
\quad\Longrightarrow\quad
K_p\le N-2W=d.                                         \tag{6.2}
\]
The Euler/fibre calculation gives \(\sum_{p\in\operatorname{Sing}D}K_p=a-1\) (ALL-N:275–295; REV:149–165). There are at most \(q'\) distinct positive-excess images, even if several carriers share one. Hence
\[
a-1=W+d-1\le q'd,                                     \tag{6.3}
\]
and, carrier by carrier,
\[
\operatorname{corr}_l\le\mu_l(s_l-1)+d.               \tag{6.4}
\]
These are valid general ceilings in the hypothetical H2/trivial-dicritical situation; they do not claim attainment.

For \(q'=1\), (6.3) gives \(W\le1\), contradicting (6.1). The N=20 packet has exactly one carrier, so it is **dead** independently of Theorem 7.A. More generally, \((q'-1)d\ge W-1\ge4q'\) and \(N=2W+d\) give the fallback floor \(N\ge26\), with the numerical minimum \((q',W,d,N)=(2,9,8,26)\) (N20:388–464). This is a lower bound, not a witness.

The old variable \(R=\sum_l(s_l-1)\) counts finite ramification with multiplicity and produced ALL-N’s weaker \(N\ge20\) frontier. Concentration replaces the number of possible physical excess sites by \(q'\), not \(R\). Neither \(R\), \(q'\), \(d\), nor the N=20 packet enters the all-degree link argument. If that argument proves \(k_l=0\), (4.1) becomes the exact identity \(\operatorname{corr}_l=\mu_l(s_l-1)\); the Orevkov budget then becomes \(N-1=W\), and the generic fibre identity gives \(a=1\). Section 7 audits precisely that last implication.

## 7. Line-by-line audit of Theorem 7.B

**Theorem 7.A is valid after two necessary local repairs.** Literally, N20:477–485 writes \(B_1=f^*(l^*)\). At a multibranch physical point \(p\), the global image is \(D\), not one smooth germ. Choose instead a small representative of the germ \((l^*,x_0)\); its image is the single local branch \(B_1\) selected by \(z=h_l(t_0)\). Shrink the target ball \(B\) and the component \(\widetilde B\subset f^{*-1}(B)\) so that \(x_0\) is its unique point over \(p\), no other contracted point occurs, and the only boundary germ in \(\widetilde B\) is \(l^*\). Immersivity of \(\eta\) makes \(B_1\) a smooth disk, so \(K=B_1\cap\partial B\) is an unknot.

Orevkov Lemma 5.2 is printed under \(M_{x_0}=\mu_l\). Re-reading its proof (PDF pp. 8–9) shows exactly where that hypothesis enters: it identifies the **full** inverse of \(K\) with the distinguished circle cut out by \(l^*\). It is not needed for the small-ball component, analyticity of the finite Stein factor, or the link construction. N20 correctly replaces that circle by
\[
K'=f^{*-1}(B_1)\cap\widetilde S,
\qquad \widetilde S=\partial\widetilde B.
\]
The replacement closes rather than assumes the desired equality:

1. The finite Stein factor is a normal analytic surface germ at \(x_0\), resolved by the rational \(L_C\)-chain. Its exceptional intersection matrix is negative definite and nonsingular. Consequently its link \(\widetilde S\) is a rational homology sphere. This is the same Mumford presentation used in Orevkov’s proof.

2. Outside the full inverse of \(B_1\), every point of this localized source lies in \(\mathbb C^2\), where the Keller map is a local biholomorphism. Thus
   \[
   \widetilde S-K'\longrightarrow S^3-K
   \]
   is a proper local homeomorphism, hence a covering. The complement of finitely many embedded circles in connected \(\widetilde S\) is connected, so its fundamental group injects into \(\pi_1(S^3-K)=\mathbb Z\). Therefore \(b_1(\widetilde S-K';\mathbb Q)\le1\).

3. If \(K'\) has \(r\) components, Mayer–Vietoris (equivalently Alexander duality in a rational homology sphere) gives
   \[
   b_1(\widetilde S-K';\mathbb Q)=r.
   \]
   Since the distinguished \(l^*\)-link is one component, \(r=1\). Hence no additional affine curve branch of \(f^{*-1}(B_1)\) passes through \(x_0\).

Finally use conservation of local degree for the finite germ. For a physical \(q\in B_1\setminus\{p\}\), first take the unique normalization place \(z_q\) on the selected branch with \(\eta(z_q)=q\). There are \(e_{t_0}\) nearby points of \(h_l^{-1}(z_q)\), each of surface local degree \(\mu_l\) by Orevkov’s normal form. Any remaining local preimages are affine, of degree one, and as \(q\) varies would form an additional branch of \(f^{*-1}(B_1)\), which \(r=1\) excludes. Thus
\[
M_{t_0}=e_{t_0}\mu_l,
\qquad k_l=0.                                        \tag{7.1}
\]
This also repairs N20:528–531, which literally asks \(h_l\) to lie “over” the physical point \(q\) rather than over \(z_q\).

The safe version of Theorem 7.A is therefore: **assuming H2 and, for contradiction, a dicritical with \(\mu_0=1\), every dicritical has zero excess \(k_l\).** N20:491 and 569–583 suppress these ambient hypotheses; N20:602–606 correctly restores them. No general Keller-map “no excess” theorem is licensed.

With that correction, every line of Theorem 7.B closes. Suppose \(\mu_0=1\). Sections 4–5 give the common immersive \(\eta\), and (7.1) gives
\[
\operatorname{corr}_l=\mu_l(s_l-1).
\]
The exact Orevkov budget and generic fibre identity then give
\[
N-1=\sum_l(\mu_l+\operatorname{corr}_l)
=\sum_l s_l\mu_l=W,
\qquad a=N-W=1.                                      \tag{7.2}
\]
The final input \(2a>N\) is genuinely load-bearing. It is not P5 alone: under H2, the promoted singularity theorem gives \(\sigma=|\operatorname{Sing}D|\ge1\); H3 and immersivity give \(\nu\ge\sigma\); and the Euler identity
\[
0=(a-1)+(N-2a)\sigma+(N-a)(\nu-\sigma)+A_\Sigma
\]
forces \(2a>N\) (ALL-N:194–227; REV:117–133). Substituting \(a=1\) yields \(N<2\), contrary to the stated noninvertible scope \(N\ge3\).

Thus Theorem 7.B is **CONFIRMED AFTER REPAIR**. It is “all-degree” for noninvertible plane Keller candidates of geometric degree \(N\ge3\), not a claim that the proof itself treats degrees 1 or 2. Degree 1 is invertible; degree 2 is separately classically excluded. The \(R/q'/d\) frontier and the N=20 packet do not enter (7.1)–(7.2); only \(W\) enters through the two exact budgets.

## 8. Packet independence and all-degree quantifiers

The independence claim at N20:585–586 is correct after restoring hypotheses. The ingredients used by §7—Orevkov’s degree-free boundary chain and local normal form, the finite normalization factorization, the local normal-surface link, and the Keller condition on the affine locus—contain no value of \(N\). The only numerical quantities in Theorem 7.B are the universally promoted identities \(W=\sum s_l\mu_l=N-a\) and \(\sum(\mu_l+\operatorname{corr}_l)=N-1\). Neither the equality packet \((N,W,d)=(20,7,6)\), nor \(R\), \(q'\), nor an equality/attainment assumption is consumed.

Conversely, the N=20 death does not depend on Theorem 7.A: concentration makes a cubic carrier totally ramified at one finite point, whereas the old equality analysis requires two distinct simple critical sites. Equations (6.1)–(6.3) make the contradiction quantitative and leave the independently valid fallback “no trivial dicritical for \(N\le25\).” If §7 were not accepted, the correct status would therefore be a frontier at \(N\ge26\), not a reversion to the old N=20 packet.

H2 enters in three exact places: it makes all dicritical images share one normalization; it supplies the strict/singularity package used to ensure a carrier and \(\sigma\ge1\); and, together with the trivial-dicritical hypothesis, it licenses \(2a>N\). H3 does not enter as a hypothesis. The local H3-free result is componentwise, but the propagation to all dicriticals is not.

Accordingly, “at any degree” means every geometric degree \(N\ge3\) in the noninvertible candidate class under H2. The theorem closes the all-degree **B0/H2 lane and its strict dicritical-count budget**; it should not be paraphrased as completing every other H2-dependent part of the broader programme.

## 9. FALLACY-v2 guardrail audit

- **Flag/place/series:** the corrected proof distinguishes \(t\), \(\pi(t)\), \(z=h_l(t)\), and \(p=\eta(z)\). N20:528–531 has a literal place/physical-point lapse, repaired in §7 by inserting \(z_q\). Its notation \(B_1=f^*(l^*)\) also had to be localized to the selected branch germ. No cv flag or cover series is identified with either.

- **Per-ray/exit-set charge:** no first-separation or exit-price assertion occurs. “Ramified escape frontier” denotes a degree-budget remainder, not a priced exit. Accordingly this report contains no exit-price declaration.

- **Carrier/attainment and floor/attainment:** packet (4.9), the \(N\ge26\) fallback, and \((q',W,d)=(2,9,8)\) are necessary numerical floors only. None is asserted to be a Keller witness. Theorem 7.B is a nonexistence theorem, not an attainment step.

- **Pole/interior:** the only pole calculation is RH at infinity, after establishing \(l'\simeq\mathbb A^1\), finiteness/separability, the unique target boundary point, and its full source fibre. Finite ramification and the point at infinity are counted separately.

- **Prime/derivative:** \(l'\) denotes a punctured dicritical; derivatives are written \(d\phi_l\), \(dh_l\), or explicitly as a polynomial derivative. The meanings are not interchanged.

- **Other guards:** no `sat()`, quotient-ring remainder, variable map, exit charge, M-descent, or target-arrival argument is used. The full-inverse-link proof supplies a theorem for the omitted excess; it is not a cap or analogy.

## 10. Untouched items and promotion recommendation

**Recommendation: PROMOTE WITH THE REPAIRS IN §§4 AND 7.** The exact promoted theorem should read:

> Let \(F:\mathbb C^2\to\mathbb C^2\) be a noninvertible plane Keller map of geometric degree \(N\ge3\). If \(A_F\) is irreducible, then no affine-image dicritical has \(\mu_l=1\). Consequently \(b=0\) and \(2m\le\sum_l\mu_l\le N-2\) for every such \(N\), without assuming H3.

This closes `OPEN[B0-H2-N>=20/RAMIFIED-NONPRIMITIVE-COVER]` in the negative. Also promote, at their stated conditional scopes: the all-degree affine-line/H3-free lemma; concentration at the unique finite \(L_C\)-attachment; the corrected conditional no-excess theorem; death of packet (4.9); and the independent \(N\le25\) fallback. Do **not** promote N20 verbatim until its contradictory opening verdict (N20:50–61), suppressed hypotheses (N20:234–239, 491, 569–583), local-branch notation, and physical-point/place lapse are corrected.

The reducible programme is untouched mathematically. Distinct target components have distinct normalizations, and H2 strictness does not place a correction on the component seen by a trivial dicritical. Thus the umbrella
`OPEN[B0-REDUCIBLE-N>=5/COMPONENT-INCIDENCE+RAMIFIED-COVERS]`
remains outside Theorem 7.B. The latest COORD refines the provisional \(N=5\) work to S1/S2 and the named residuals at COORD:77–82; that refinement also remains untouched.

The without-H2 \(N=4\) work is likewise outside Theorem 7.B, but N20’s exact ledger sentence is stale. N20:619 repeats `OPEN[PI1-S4]`; the newer charged COORD says the named PI1S4 sublanes are resolved/retired (COORD:67–70) and replaces the current reducible residual by six \((8,6)/(9,6)\) AM-numerical types, with closure still conditional on the stated decision and ROW-NF exhaustiveness dependencies (COORD:55–60, 73–76, 96–100). Therefore promote only: “Theorem 7.B does not touch the current N=4 without-H2 residual,” not the obsolete OPEN label.

There is also charged-basis citation drift: N20:550–552 cites `COORD:69–74` for the N=5 H2 profile, but those lines in the actually charged COORD concern the updated N=4 ledger. The available frozen support is ALL-N:351–358, which quotes the older coordinator lineage. This does not affect the all-degree proof, but the citation must be repaired before integration.

No unconditional \(2m\le N-1\), no B0 theorem for reducible \(A_F\), no standalone general \(k_l=0\) theorem, and no assertion that every H2-dependent programme item is complete should be promoted from this lane.

<!-- BODY-END -->
