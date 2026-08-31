# Hostile review: B0-ALL-N report (Sol) — does the mechanism close H2 through N=19?

**Reviewer.** grok-4.6 (different-model gate).  
**Date.** 2026-08-31.  
**Charge.** Default to refutation. Desk-scale exact reasoning; literature hashed as needed. No CAS. No `jc2-lean`. No `charge_basis` declaration.

## 0. Hash verification, inputs, scope

Frozen inputs were hashed with `shasum -a 256` before they were read. All four SHA-256 values match the charge exactly:

```text
621f1356b3b5290e32c2f2bf689b4d9a49412cb852066886a34b580366cb1652  b0-all-n-eta-criticality-sol56-20260831.md
67a9482eecd3fcb5f06bcf2967d4b73f5761429b5be597f2809b8e0767b1b02c  corr-budget-n5-sol56-20260831.md
ba35a89bd6aad2d4c86d5594ef49be1c63033aed5b08140c8f17e0fc0fa42a22  corr-budget-n5-hostile-review-grok46-20260831.md
bbd48de1b028f6c71f006c3f27c10a3b96c593e6da58088c8393a992bde4a963  block-descent-a1-b0-coordinator-integration-fable5-20260831.md
```

Primary PDFs were rehashed at execution and agree with the charged report’s §1:

```text
f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db  refs/jc86.pdf
88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad  refs/zoladek2008_official.pdf
```

Below, **ALL-N**, **N5**, **N5R**, and **Coord** denote those four frozen files in the charge order. Standing notation is Coord’s: \(F\) a noninvertible plane Keller map of geometric degree \(N\ge 3\); H2 means \(D:=A_F\) irreducible; H3 means \(\widetilde D\simeq\mathbb A^1\). No canonical ledger or charged file was edited, `jc2-lean` was not inspected, and no CAS was run. `FALLACY-v2` is in force. No new exit price is asserted.

Default-to-refutation concentrated on: (i) the all-source licence of (2.1)–(2.2); (ii) Orevkov Lemma 2.1 as an all-degree affine-line statement; (iii) whether [Z-6.5(b)] can be made to speak of \(d\eta\) rather than \(d\phi_l\); (iv) the inequality \(M_t\ge e_t\mu_l\) and the \(R\)-bound that produce \(N\ge 20\); (v) a small-\(N\) ramified-cover packet the arithmetic might have missed; (vi) a collision between ALL-N’s “N5 transfer REFUTED” and N5R’s CONFIRMED.

**Verdict.** Theorem 4.1 is CONFIRMED at its written scope. Under H2 the eta/cover mechanism excludes every trivial-dicritical profile for \(N\le 19\), and at every degree if every correction-bearing cover has degree one. Escape requires a ramified nonprimitive cover, first numerically possible at \(N=20\) in the region \(2a>N\), with necessary packet (4.9). The N5 kill survives. All-degree B0 under H2 is not proved.

## 1. Factorization (2.1)–(2.2) and licence at all source points

**CONFIRMED.**

Let \(l\) be an affine-image dicritical, \(l'=l\setminus L_\infty\), \(\phi_l:l'\to D\) of mapping degree \(s_l\). Orevkov Lemma 2.1 (re-opened below, §2) gives \(l'\simeq\mathbb A^1\), so \(\mathbb C[l']=\mathbb C[t]\) with \(l'\) smooth, hence normal. Dominance of \(\phi_l\) embeds \(K(D)\) in \(\mathbb C(t)\). If \(A=\mathbb C[D]\) and \(\overline A\) is its integral closure in \(K(D)\), the image of any \(u\in\overline A\) is integral over \(A\subset\mathbb C[t]\) and therefore over \(\mathbb C[t]\); \(\mathbb C[t]\) is integrally closed in \(\mathbb C(t)\), so that image lies in \(\mathbb C[t]\). The resulting \(\mathbb C\)-algebra map \(\overline A\to\mathbb C[t]\) is a morphism of affine curves

\[
h_l:l'\longrightarrow\widetilde D=\operatorname{Spec}\overline A,\qquad \phi_l=\eta\circ h_l. \tag{2.1}
\]

This is the universal property of normalization for a dominant morphism from a normal curve. It is a morphism of the whole source, including points with \(\phi_l(x)\in\operatorname{Sing} D\): \(h_l(x)\) is the normalization place selected by the source germ, not the physical point \(\eta(h_l(x))\). The covering lemma (smooth stratum \(D_0=D\setminus\operatorname{Sing} D\) only; Coord item 2, N5R:55–56) is not used and is not asked to see those points. Dicriticals live on the compactification, not among the \(a\) affine sheets.

Finiteness: some affine coordinate pulls back along \(\phi_l\) to a nonconstant polynomial \(f\in\mathbb C[t]\) (nonconstancy is the affine-image dicritical). Then \(\mathbb C[f(t)]\subset\overline A\subset\mathbb C[t]\), and \(\mathbb C[t]\) is finite over \(\mathbb C[f]\) on the standard generators \(1,t,\dots,t^{\deg f-1}\). The same generators work over \(\overline A\), so \(h_l\) is finite. A finite dominant map of irreducible curves is surjective, and

\[
\deg h_l=[\mathbb C(t):K(D)]=s_l, \tag{2.2}
\]

because \(K(\widetilde D)=K(D)\). This is the finite, surjective, degree-\(s_l\) licence used without proof at B0:236–243 and in the degree-one case N5:81–91. The four objects that `FALLACY-v2` forbids identifying remain distinct: a point of \(l'\), its image \(\pi(t)\) in Orevkov’s collapsed space, the place \(z=h_l(t)\), and the physical point \(\eta(z)\in D\).

No cv flag or Puiseux series enters. CONFIRMED at all source points.

## 2. Trivial-dicritical step: étale, immersivity, \(l_0'\simeq\mathbb{A}^1\), \(s_0=1\), free H3

**CONFIRMED.**

### 2.1 Primary source for \(l_0'\simeq\mathbb A^1\) at all degrees

Orevkov, *Math. USSR-Izv.* **29** (1987), hashed `refs/jc86.pdf`. Lemma 2.1 is stated on printed/PDF **page 2** (the proof runs through printed p. 4). Immediately before the lemma, irreducible components of \(L=X_e\setminus\mathbb C^2_e\) are nonsingular rational curves, intersecting transversally and at most pairwise. The lemma itself has no restriction on the geometric degree \(N\): after a choice of regularization, each connected component \(K\) of \(L_{FC}\) satisfies

- (a) \(K\) meets \(L_\infty\) at a unique point \(p\), and \(f(K\setminus p)\subset\mathbb C^2\);
- (b) the dual graph of \(K\) is linear, with \(p\) on an endpoint component \(\ell_k\);
- (c) \(\ell_k\subset L_F\) and \(\ell_i\subset L_C\) for \(i<k\).

The \(L_F\)-endpoint \(\ell=\ell_k\) is therefore a smooth rational curve meeting \(L_\infty\) at exactly one point, and \(\ell'=\ell\setminus L_\infty\simeq\mathbb P^1\setminus\{\infty\}\simeq\mathbb A^1\). The §2 regularization (blow-ups only at infinity; polar-divisor Lemma 2.2) never uses \(N=3\). Coord already bound this as the all-degree affine-line repair (\(\varepsilon\equiv 0\); Coord:56–66). ALL-N uses (1.5) at that primary-source scope, not by extrapolating the \(N=5\) values \(s_l=1\). CONFIRMED: the citation is Lemma 2.1(a,c) plus the rationality sentence on PDF p. 2, and it is \(N\)-free.

Lemma 5.3 (PDF p. 9) is *not* the source: it assumes \(N>2\), irreducible \(L_F\), and \(\mu=N-1\), and concludes biregularity. That is a different statement.

### 2.2 \(\mu_0=1\) forces finite étale \(h_0\) and immersive \(\eta\)

[Z-6.5(b)], printed pp. 457–458 / PDF pp. 27–28 of the hashed Żołądek file: \(\mu_{z_0}>\mu_D\) if and only if \(y_0=\widetilde P(z_0)\) is a singular point of the *immersed* curve \(S=\widetilde P(\widetilde D\setminus\infty)\). The parenthetical on p. 457 defines that singularity as vanishing of \((X,Y)'(t_0)\); intersections of smooth local components are not singularities. Separately, \(\mu_D=1\) implies \(S\) is smooth. This is the promoted reading (Coord:43–45, 108–116; N5R:53, 85–93). Applied to \(\phi_0\), one gets \(\operatorname{corr}_0=0\) and \(d\phi_0(x)\ne 0\) at every finite \(x\in l'_0\).

Chain rule as maps of smooth source curves into \(\mathbb C^2\) (never as a derivative of a map of singular schemes \(\widetilde D\to D\)):

\[
d\phi_0(x)=d\eta_{h_0(x)}\circ dh_0(x).
\]

Vanishing of neither factor is compatible with \(d\phi_0\ne 0\). Thus \(h_0\) is unramified (finite étale of degree \(s_0\)) and, because \(h_0\) is surjective by (2.2), \(\eta:\widetilde D\to\mathbb C^2\) is immersive at every place, including every place over \(\operatorname{Sing} D\). CONFIRMED.

### 2.3 Riemann–Hurwitz forces \(s_0=1\) and H3

Extend the finite morphism \(h_0:\mathbb A^1\to\widetilde D\) to smooth projective completions \(\overline h_0:\mathbb P^1\to\overline D\). A nonconstant morphism of projective curves is surjective. The image of \(\mathbb A^1\) lies in \(\widetilde D\); if \(\overline h_0(\infty)\) also lay in \(\widetilde D\), one would have a nonconstant map \(\mathbb P^1\to\widetilde D\) with \(\widetilde D\) affine (finite over the affine curve \(D\)), which is impossible. Hence \(\overline D\setminus\widetilde D\) is nonempty, is covered by the single point \(\infty\), and consists of exactly one point, whose full preimage is \(\{\infty\}\). Finite ramification of \(\overline h_0\) is therefore empty (étale on \(\mathbb A^1\)), and the unique point at infinity has ramification index \(s_0\), contributing \(s_0-1\) to the total ramification.

Riemann–Hurwitz: \(-2=s_0(2g-2)+(s_0-1)\). If \(g\ge 1\) then the right-hand side is at least \(s_0-1\ge 0\), contradicting \(-2\). Thus \(g=0\), \(\overline D\simeq\mathbb P^1\), and \(-2=-2s_0+(s_0-1)\) forces \(s_0=1\). Then \(h_0\) is an isomorphism and \(\widetilde D\simeq\mathbb A^1\), which is Coord’s H3. H3 is a conclusion from a trivial dicritical plus Lemma 2.1, not an extra hypothesis. Withholding Lemma 2.1 would stop at a connected finite étale cover, which H3 would then trivialize; that is correctly flagged as a counterfactual. CONFIRMED.

## 3. Corrected transfer: [Z-6.5b] on the composite, residue of the incidental multiple reduced point

**CONFIRMED** as a correction of the all-\(N\) eta-criticality engine. Nothing load-bearing is lost to the “incidental multiple point.” The N5 equivalence \(d\phi=0\Leftrightarrow d\eta=0\) is *not* false at its own \(s=1\) scope; see §5.

### 3.1 Re-derivation

[Z-6.5(b)] is a statement about the immersed curve \(S=\widetilde P(\widetilde D\setminus\infty)\), i.e. about the composite \(\phi_l=\eta\circ h_l:l'\to\mathbb C^2\). A jump \(\mu_x>\mu_l\) at the Orevkov quotient point corresponding to a parametrization point \(\widehat x\in l'\) is equivalent to \(\phi_l'(\widehat x)=0\). Intersections of smooth local branches are expressly not singularities of that immersed curve (printed p. 457). [O-5.2] (PDF pp. 8–9) gives only the one-way implication “no jump \(\Rightarrow\) nonsingular local embedding”; its contrapositive cannot supply jump-to-criticality. ALL-N is right to refuse that direction.

Chain rule at \(\widehat x\), with \(z=h_l(\widehat x)\):

\[
0=d\phi_l(\widehat x)=d\eta_z\circ dh_l(\widehat x).
\]

Section 2 already gives \(d\eta_z\ne 0\) at every place (immersivity from the trivial dicritical, using surjectivity of \(h_0\)). Therefore \(dh_l(\widehat x)=0\). Conversely, \(dh_l=0\) implies \(d\phi_l=0\), hence a jump by [Z-6.5(b)]. At the parametrization-point level licensed by [Z], correction support of \(l\) is exactly ramification support of \(h_l\). In particular every correction-bearing \(h_l\) has \(s_l\ge 2\) (a degree-one polynomial is unramified) and \(\mu_l\ge 2\) (\(\mu=1\) is immersive everywhere). CONFIRMED.

This is the opposite of “criticality lands on \(d\eta\).” Żołądek’s second example on p. 457 is the local picture: two-fold map \(D\to S\), \(\mu_D=3\), \(\mu_{(0,0)}=8\), a ramified nonprimitive parametrization with a jump and no requirement that the reduced image branch be singular. N5:60–64 and N5R:180 already named this loophole; ALL-N makes it the exact escape rather than a diagnostic aside.

### 3.2 Residue of a multiple reduced point

A reduced branch of \(D\) at \(p\) is singular if and only if \(d\eta=0\) at its place. Immersivity of \(\eta\) excludes that. Every branch is smooth, so every point of \(\operatorname{Sing} D\) is multibranch (\(\nu\ge\sigma\)). Promoted Lemma 3.3 (zero correction \(\Rightarrow\) smooth branch; B0:219–225, Coord item 2) is not reversed: a correction need not be a singular reduced branch.

A multiple point does not itself produce (3.1). If \(h_l\) is unramified at a place over a node, the selected branch parametrization is immersive and [Z-6.5(b)] records no jump. If \(h_l\) ramifies there, the jump is from \(h_l\). Locally one may have \(\eta(u)\) parametrizing a smooth branch and \(h_l(t)=u_0+t^e\) with \(e\ge 2\); then \(\eta\circ h_l\) is critical with smooth reduced image. That is allowed, and it is the escape, not a gap in the obstruction.

Is anything lost? The N5 fibre pin \(r_{p_*}=1\) (unibranch correction image) used \(s_2=1\) and \(N=5\). That pin is not available for a ramified carrier, and ALL-N does not use it. The comparison “one place cannot be both critical and immersive for two degree-one maps” is likewise \(s=1\)-specific. Replacing it by ramification of \(h_l\) is the correct remainder, not a weakening of a theorem that was never claimed for \(s\ge 2\). CONFIRMED: the multiple reduced point is incidental.

## 4. Budget arithmetic: first escape at \(N=20\), necessarily \(2a>N\), packet (4.9)

**CONFIRMED.** No ramified-cover configuration with \(N\le 19\) satisfies the necessary inequalities. The first numerical possibility is \(N=20\), necessarily in \(2a>N\), with equality packet (4.9). Packet (4.9) is a floor, not attainment.

### 4.1 Euler identity and \(2a>N\)

Promoted Corollary 3.6: irreducible \(A_F\) is singular, so \(\sigma\ge 1\). With \(\widetilde D\simeq\mathbb A^1\) and immersive \(\eta\), every singularity is multibranch and \(\nu\ge\sigma\). Compactly supported Euler: \(\chi_c(D-\Sigma)=1-\sigma-\nu\). The irreducible Euler identity, re-derived from promoted \((E)\), the \(\chi_c\) toolkit, and the smooth-stratum covering lemma (B0:236–265; N5R:85–98; identity does not use either branch of Lemma 3.4),

\[
(N-a)\chi_c(D-\Sigma)=N-1-N\sigma+A_\Sigma,
\]

substitutes to ALL-N (4.1):

\[
0=(a-1)+(N-2a)\sigma+(N-a)(\nu-\sigma)+A_\Sigma.
\]

If \(2a\le N\), each of the four terms is nonnegative. For \(N\ge 3\) and \(\sigma\ge 1\), either \(N-2a>0\) and the second term is at least \(1\), or \(N=2a\) and then \(a=N/2\ge 2\) so \(a-1\ge 1\). Contradiction. Hence \(2a>N\). CONFIRMED. (This is strictly stronger than Theorem 3.5(ii), which needed vanishing correction; the trivial dicritical supplies \(c=1\) and \(\nu\ge\sigma\) in its place.)

Write \(W=N-a=\sum_l s_l\mu_l\) and \(d=2a-N=a-W>0\), so \(N=2W+d\) and \(a=W+d\). The trivial dicritical contributes \(1\) to \(W\). A correction carrier has \(\mu_l,s_l\ge 2\), hence contributes at least \(4\). Thus \(W\ge 5\).

### 4.2 Local inequality (4.3) and the correction formula

Orevkov §4 (PDF p. 6): the multiplicity \(\mu_x\phi\) is the largest \(k\) such that every neighbourhood of \(x\) contains \(k\) points with a common image. After contracting \(L_\infty\) and each \(L_C\)-chain, \(f^*:X_e^*\to X^*\) is a constant-multiplicity map of multiplicity \(N\) (PDF pp. 6–7). Lemma 2.1: each \(L_{FC}\) component is a linear chain with a unique \(L_F\)-endpoint, so contraction of the \(L_C\)-part lands at one attachment point of \(\pi(l)\); \(\pi|_{l'}\) does not identify distinct finite points; distinct chains meet only in \(L_\infty\); there are no extra finite \(L_C\)-fibre points (the promoted \(\varepsilon\equiv 0\)).

For \(t\in l'\) let \(e_t\) be the local degree of \(h_l\) and \(M_t=\mu_{\pi(t)}f^*\). Deform \(h_l(t)\) to a nearby regular place of \(\widetilde D\). The \(e_t\) nearby inverse points on \(l'\) are distinct and may be taken off the finite correction set of \(l\). At each, Orevkov Lemma 3.1 (PDF pp. 4–5) supplies the generic normal form with \(\mu_l\) transverse sheets. A nearby off-branch target therefore has \(e_t\mu_l\) inverse points, in disjoint neighbourhoods all contained in any fixed neighbourhood of \(\pi(t)\). The §4 definition gives \(M_t\ge e_t\mu_l\), i.e. \(k_t:=M_t-e_t\mu_l\ge 0\). At an \(L_C\)-attachment the collapsed point is singular in \(X_e^*\); extra preimages can only raise \(M_t\), so the lower bound persists. CONFIRMED.

Because \(\eta\) is immersive, correction points of \(l\) are exactly the critical points of \(h_l\). After parts 1–3 of the theorem, \(h_l:\mathbb A^1\to\mathbb A^1\) is a polynomial of degree \(s_l\), and Riemann–Hurwitz on its projective completion gives \(\sum_t(e_t-1)=s_l-1\). Point-separation plus \(\pi\) injective on \(l'\) converts Orevkov’s inner sum into

\[
\operatorname{corr}_l=\sum_t(M_t-\mu_l)=\mu_l(s_l-1)+\sum_t k_t. \tag{4.4}
\]

Unramified points have \(e_t=1\) and, by immersivity of \(\eta\), \(M_t=\mu_l\), so \(k_t=0\) off ramification. CONFIRMED.

### 4.3 Fibre identity, (4.6), (4.7)

Constant multiplicity at a physical point \(p\in D\): affine points of multiplicity one (empty \((U,e>1)\) box, promoted), plus dicritical contributions. For each place \(z\) over \(p\) and each \(l\), \(\sum_{h_l(t)=z}e_t=s_l\). Setting \(r_p=|\eta^{-1}(p)|\) and \(K_p=\sum k_t\) over \(t\) whose place lies over \(p\),

\[
a_p+r_p W+K_p=N. \tag{4.5}
\]

Generic check: \(r_p=1\), \(K_p=0\), \(a_p=a\) recovers \(a+W=N\). At \(p\in\Sigma\), \(r_p\ge 2\) and \(a_p\ge 0\) give \(K_p\le N-2W=d\). Summing (4.5) over \(\Sigma\) produces \(A_\Sigma=a\sigma-W\nu-\sum_{p\in\Sigma}K_p\). Substituting into (4.1) and using \(N-a=W\), \(d=2a-N\) cancels the \(\sigma\)-terms and yields \(\sum_{p\in\Sigma}K_p=a-1\). CONFIRMED.

Let \(R=\sum_l(s_l-1)\), the total finite ramification multiplicity of the polynomial covers. A singular image with \(K_p>0\) contains a point with \(k_t>0\), hence (by immersivity of \(\eta\)) a ramification point of some \(h_l\). The number of such images is at most the number of critical points, which is at most \(R\). Combined with \(K_p\le d\) on \(\Sigma\),

\[
a-1\le dR. \tag{4.7}
\]

This bound is generous: ramification over smooth points, \(r_p\ge 3\), or several critical points sharing an image all shrink the right-hand side and make survival harder. Using the looser form cannot falsely exclude a small-\(N\) packet. CONFIRMED.

### 4.4 Bound on \(R\) and the numerical frontier

Let \(b\ge 1\) be the number of \(\mu=1\) dicriticals and \(q\ge 1\) the number with \(\mu\ge 2\). Every former has \(s_l=1\), so \(R=\sum_{\mu_l\ge 2}(s_l-1)\) and \(\sum_{\mu_l\ge 2}s_l=R+q\). Then \(W\ge b+2(R+q)\), hence \(2R\le W-b-2q\le W-3\) and \(R\le\lfloor(W-3)/2\rfloor\). The most generous \(R\) (largest right-hand side of (4.7), easiest survival) is \(b=q=1\) and \(\mu=2\) on the unique nontrivial dicritical, saturating \(W=2R+3\). Extra trivial dicriticals, extra \(\mu\ge 2\) components, or \(\mu\ge 3\) all *decrease* \(R\) relative to \(W\) and make (4.8) harder. No missed generous configuration.

With \(a=W+d\), (4.7) becomes ALL-N (4.8): \(W+d-1\le d\lfloor(W-3)/2\rfloor\), \(N=2W+d\). Let \(F=\lfloor(W-3)/2\rfloor\). The inequality rearranges to \(W-1\le d(F-1)\) whenever \(F\ge 2\), and is impossible if \(F\le 1\). Desk check:

| \(W\) | \(F\) | min \(d\) | min \(N=2W+d\) |
| ---: | ---: | ---: | ---: |
| 5 | 1 | impossible | — |
| 6 | 1 | impossible | — |
| 7 | 2 | 6 | **20** |
| 8 | 2 | 7 | 23 |
| 9 | 3 | 4 | 22 |
| 10 | 3 | 5 | 25 |
| 11 | 4 | 4 | 26 |
| 12 | 4 | 4 | 28 |

For \(W\ge 10\), already \(N=2W+d\ge 21\) with \(d\ge 1\); the table’s actual minima are larger. ALL-N’s phrase “\(W\ge 10\) already gives \(N\ge 21\)” is a crude lower bound, not a defect.

No pair \((W,d)\) with \(N=2W+d\le 19\) satisfies (4.8). Explicitly: \(N=19\) would require \((W,d)\in\{(7,5),(8,3),(9,1)\}\), and those \(d\) lie strictly below the minima 6, 7, 4. The same holds down through \(N=3\). The \(W=5\) packet \((\mu,s)=(1,1)+(2,2)\) has \(R=1\) and \(W+d-1=4+d\le d\), impossible for all \(d>0\). CONFIRMED: 19 is the last excluded degree under this mechanism.

### 4.5 Packet (4.9), and a hunt that failed

Equality \(N=20\) in (4.8) forces \(W=7\), \(d=6\), \(a=13\), \(R=2\). Equality in the \(R\)-bounds forces \(b=q=1\), \(\mu=2\), \(s=3\): \(W=1+2\cdot 3=7\). The exact budget \(\sum(\mu+\operatorname{corr})=19\) then gives total correction 16, i.e.

\[
(\mu,s,\operatorname{corr})=(1,1,0)+(2,3,16). \tag{4.9}
\]

A competing \(W=7\) shape \((\mu,s)=(1,1)+(3,2)\) has \(R=1\), and \(6+d\le d\) is impossible, so it is not a second \(N=20\) candidate. Equality in (4.6)–(4.7) further forces two distinct singular images with \(K_p=d=6\) each (one image would give \(a-1\le d=6<12\); \(r_p\ge 3\) would give \(K_p\le N-3W=-1\)). Thus the cubic has two distinct simple critical points, with distinct critical values, each landing on a two-branch singularity, \(k_t=6\), \(M_t=2\cdot 2+6=10\), correction \(8\) apiece, and \(a_p=0\) at both images. A totally ramified cubic (\(e=3\) at one point, still \(R=2\)) has only one critical image and fails (4.7). Additional singularities with \(K_p=0\) are not excluded (necessarily two-branch with \(a_p=6\)). ALL-N correctly types (4.9) as necessary only: not a Keller witness, not attainment. The first OPEN left by the mechanism is exclusion of this ramified-cubic multibranch packet.

No earlier escape was found: every attempt to raise \(R\) relative to \(W\) contradicts \(\mu=1\Rightarrow s=1\) or \(\mu,s\ge 2\) on a correction carrier. CONFIRMED.

## 5. N5-transfer refutation versus N5 review CONFIRMED

**CONFIRMED, with a scope correction rather than a destruction of the N5 theorem.**

N5 (2.2), after \(s_2=s_1=1\), states \(d\phi_2(x)=0\Leftrightarrow d\eta(z)=0\). That equivalence uses \(dh_2\ne 0\), which is the degree-one case. N5R CONFIRMED the \(N=5\) kill on that ground (N5R:172–188) and already wrote the break: “Primitivity was essential: if \(\deg h_2\ge 2\), vanishing of \(d\phi_2\) could be ramification of \(h_2\) with \(d\eta\ne 0\)” (N5R:180); “What breaks at \(s_l\ge 2\) on the corrected dicritical” (N5R:212–216). The unique H2 profile at \(N=5\) is \((\mu,\operatorname{corr})=(2,1)+(1,0)\) with \((s_2,s_1,a)=(1,1,2)\) (Coord:69–74). Fibre arithmetic \(a+2s_2+s_1=5\), \(s_1=1\), \(a\ge 1\) leaves only \(s_2=1\). Both carriers have degree one, so criticality *does* land on \(d\eta\), and the second primitive copy of \(\eta\) is immersive at the same place. That chain-rule contradiction is intact.

ALL-N’s sentence “correction-to-eta transfer — REFUTED as stated” is therefore a refutation of *eta-criticality as an all-\(N\) engine*, which is the theorem ALL-N was asked to prove and which ALL-N itself declines (ALL-N:19, 427–429). It is not a refutation of N5 at N5’s scope. Both reports, and N5R §7, agree on the surviving all-degree engine: under H2, a trivial dicritical plus a *degree-one* correction carrier is impossible. ALL-N recovers the \(N=5\) kill as the \(s_2=1\) instance of Theorem 4.1 parts 1–3, without needing the \(N=5\) fibre pin \((\sigma,\nu,A)=(1,0,1)\).

Reconciliation: N5R CONFIRMED and ALL-N’s transfer-refutation coexist. The N5 conclusion survives via \(s_2=1\). The residual named by N5R for \(N\ge 6\) (corrections on \(s\ge 2\)) is exactly ALL-N’s ramified-nonprimitive remainder, now excluded through \(N=19\) by the budget. No collision. CONFIRMED.

## 6. Consequences typing in §5

**CONFIRMED**, with the conditionality ALL-N records.

### 6.1 Irreducible \(A_F\)

Theorem 4.1 plus the unique Coord profile at \(N=5\) give: under H2, no affine-image \(\mu=1\) dicritical for every \(N\le 19\). In campaign notation, \(b=0\) on that range, with no H3 *hypothesis* (H3 is a conclusion). Coord’s (M)-verbatim sentence still needs H3 or the affine-line bridge wherever \(\nu/s\) bookkeeping is consumed (Coord:52–54, 117–118); that is a different ledger and is not promoted here.

Promoted Cor 5.1 (Coord:67–68): under H2, \(2m_{\mathrm{nt}}+m_{\mathrm{triv}}\le\sum\mu_l\le N-2\). With \(m_{\mathrm{triv}}=b=0\) one has \(2m\le N-2\), one unit stronger than the all-profile bound \(2m\le N-1\). This holds for \(N\le 19\) under H2, and at all \(N\) if the ramified-cover OPEN is later closed. Without H2, \(b=0\) and the exact budget (1.1) give only \(2m\le N-1\). An H2-only B0 theorem cannot make that bound unconditional. CONFIRMED.

### 6.2 Reducible \(A_F\), and what remains conditional

At \(N=4\), the residual is Coord’s repair, not printed Theorem 4.3(5) (refuted; Coord:56–66, 108–111): two dicriticals over distinct components, \((\mu,\operatorname{corr},s)=(2,0,1),(1,0,1)\), both normalizations \(\mathbb A^1\), OPEN[PI1-S4]. ALL-N restates this correctly.

There is no promoted PI1-\(S_N\) analogue for \(N\ge 5\). Different target components have different normalization maps; H2-strictness does not place a correction on the component seen by a trivial dicritical; the common-\(\eta\) argument is only componentwise. The honest remainder is ALL-N’s OPEN[B0-REDUCIBLE-N>=5/COMPONENT-INCIDENCE+RAMIFIED-COVERS], including the budget and fibre identities per component together with promoted meridian cycle-type and transitivity. The \(\mu\ge 2\) component is required by branch-locus nonemptiness; \(\mu=N-1\) is excluded by Cor 3.8. CONFIRMED.

At \(N=5\) the reducible cost multisets containing a \((1,0)\) and a \(\mu\ge 2\) summand of \(N-1=4\) are exactly (5.3): \((2,1)+(1,0)\), \((3,0)+(1,0)\), \((2,0)+(1,0)+(1,0)\). The excluded \((2,0)+(1,1)\) is already killed pointwise by \(\mu=1\Rightarrow\operatorname{corr}=0\), with or without H2. Incidence and cover degrees remain open. The unique Coord profile and its N5 destruction are H2-only. N5’s PI1-S5-CORR paragraph is explicitly counterfactual (N5:320–356; N5R §6) and is not the \(N\ge 5\) reducible residual. CONFIRMED.

What remains conditional:

- all-degree \(b=0\) under H2, and the corresponding \(2m\le N-2\), pending OPEN[B0-H2-N>=20/RAMIFIED-NONPRIMITIVE-COVER], beginning with packet (4.9) in the region \(2a>N\);
- unconditional \(2m\le N-1\), pending the reducible gap at every \(N\ge 4\);
- B0 at \(N=4\) without H2, pending PI1-S4.

A safe all-degree H2 replacement would follow from any one of: every correction carrier has \(s_l=1\); a correction cannot arise solely from ramification of \(h_l\); or \(2a\le N\) under H2. None is promoted. ALL-N does not claim otherwise.

## 7. FALLACY-v2 flags

- **Flag/place/series.** Not identified. The four objects (point of \(l'\), collapsed \(\pi(t)\), place \(z=h_l(t)\), physical \(\eta(z)\)) stay distinct through (2.1), (4.3), and (4.5).
- **Per-ray/exit-set charge.** No typed first-separation exit is asserted. No `charge_basis` line.
- **Carrier/attainment.** Packet (4.9) is typed necessary-only. Żołądek’s second example and the local germs in N5 §2 are diagnostic, not Keller witnesses.
- **Floor/attainment.** \(N\ge 20\) is a lower bound from (4.8), not equality. ALL-N does not treat the bound as an example. The \(R\le\lfloor(W-3)/2\rfloor\) estimate is used as a floor on the obstruction (a looser upper bound on \(R\) would only weaken exclusions; it is in fact the most generous case).
- **Pole/interior, sat(), raw remainder, variable/ring map.** Not used.
- **Prime label/derivative.** Derivatives are \(d\phi\), \(dh\), \(d\eta\) in Żołądek’s parenthetical sense; \(l'\) is the punctured dicritical, not a derivative.
- **Merge-free / target-arrival.** Not in play.

No silent filling by cap or analogy. The one genuine remainder is typed OPEN[B0-H2-N>=20/RAMIFIED-NONPRIMITIVE-COVER], plus the reducible OPEN already on Coord’s books.

## 8. Verdict and promotion recommendation

**Verdict: CONFIRMED.** Default-to-refutation did not find a load-bearing break. Theorem 4.1 stands at its written scope.

Line-by-line:

| Check | Status |
|---|---|
| (1) Factorization (2.1)–(2.2), all source points | CONFIRMED |
| (2) Étale \(h_0\), immersive \(\eta\); Orevkov Lemma 2.1 PDF p. 2, \(N\)-free; \(s_0=1\) and H3 for free | CONFIRMED |
| (3) [Z-6.5(b)] on the composite \(\Rightarrow dh_l=0\); multiple reduced point incidental | CONFIRMED |
| (4) First escape \(N=20\), necessarily \(2a>N\), packet (4.9); no \(N\le 19\) ramified-cover hole | CONFIRMED |
| (5) N5 transfer vs N5R CONFIRMED | CONFIRMED (scope correction; N5 kill survives by \(s_2=1\)) |
| (6) Consequences typing in §5 | CONFIRMED |

**Promote:**

1. Under H2, no affine-image dicritical with \(\mu=1\) for every \(N\le 19\). Equivalently \(b=0\) and \(2m\le N-2\) on that range, with H3 a conclusion rather than a hypothesis.
2. The same exclusion at every degree if every correction-bearing normalization cover has degree one. This includes the promoted \(N=5\) profile, recovered without a new N5-specific argument.
3. The transfer correction: jump-to-criticality is [Z-6.5(b)] on \(\phi_l=\eta\circ h_l\); immersivity of \(\eta\) pushes criticality onto \(dh_l\). Eta-criticality is not the all-degree engine.

**Do not promote:**

- All-degree B0 under H2. Remainder: OPEN[B0-H2-N>=20/RAMIFIED-NONPRIMITIVE-COVER], necessarily \(2a>N\), first numerical candidate the necessary packet \((\mu,s,\operatorname{corr})=(1,1,0)+(2,3,16)\) at \(N=20\), \(W=7\), \(d=6\), \(a=13\), \(R=2\). Not an attainment.
- Unconditional \(2m\le N-1\), or B0 without H2. Remainder: OPEN[B0-REDUCIBLE-N>=5/COMPONENT-INCIDENCE+RAMIFIED-COVERS], and at \(N=4\) the existing OPEN[PI1-S4].
- Any claim that the N5 theorem is false. N5R’s CONFIRMED at \(N=5\) under H2 stands.

Hostile targets that failed: (i) Lemma 2.1 restricted to \(N=3\) — the statement on PDF p. 2 is degree-free; (ii) factorization not licensed over \(\operatorname{Sing} D\) — it is the universal property of \(\eta\), not the covering lemma; (iii) [O-5.2] supplying jump-to-criticality — ALL-N does not use that direction; (iv) a multiple point as an alternative to ramification — [Z] plus immersive \(\eta\) forbid it; (v) an \(N\le 19\) packet with larger \(R\) than \(\lfloor(W-3)/2\rfloor\) — raising \(R\) contradicts \(s_0=1\) or \(\mu,s\ge 2\) on a carrier; (vi) a contradiction between ALL-N and N5R — different scopes of the same chain rule.

Primary sources consumed: Orevkov Lemma 2.1 (PDF p. 2), Lemma 3.1 (pp. 4–5), multiplicity and constant-multiplicity in §4 (pp. 6–7), Lemma 5.2 (pp. 8–9); Żołądek Proposition 6.5(b) both directions with the printed parenthetical (pp. 457–458 / PDF pp. 27–28). Promoted identities consumed at Coord’s scopes: (1.1)–(1.3), Cor 3.6–3.8, Cor 5.1, covering lemma on \(D_0\), empty \((U,e>1)\) box, Euler identity (3.1) of B0 Lemma 3.4 before its case split. No new exit price. No CAS. No ledger, charged-file, or `jc2-lean` inspection.

<!-- BODY-END -->

