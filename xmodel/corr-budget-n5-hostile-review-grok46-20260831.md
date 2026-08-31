# Hostile review: CORR-BUDGET-N5 (Sol) — does the profile really self-destruct?

**Reviewer:** grok-4.6
**Date:** 2026-08-31
**Mode:** different-model gate; default to refutation
**Charged report:** `xmodel/corr-budget-n5-sol56-20260831.md`
**Integrations:** `xmodel/block-descent-a1-b0-coordinator-integration-fable5-20260831.md`, `xmodel/b0-trivial-dicritical-proof-opus5-20260831.md`

**Frozen-input SHA-256 (verified match):**

```text
67a9482eecd3fcb5f06bcf2967d4b73f5761429b5be597f2809b8e0767b1b02c  corr-budget-n5-sol56-20260831.md
bbd48de1b028f6c71f006c3f27c10a3b96c593e6da58088c8393a992bde4a963  block-descent-a1-b0-coordinator-integration-fable5-20260831.md
b37ec3bfd41eb22c14e29b06284100a61c50fd849150fefe2eab89e1d1a78c55  b0-trivial-dicritical-proof-opus5-20260831.md
```

**Verdict: CONFIRMED.** Promote the \(N=5\) kill under H2. The unique residual trivial-dicritical profile self-destructs by a chain-rule comparison of two degree-one parametrizations on the same normalization place. Default-to-refutation did not find a load-bearing break.

## 0. Scope, method, and hash gate

The three frozen inputs were hashed with `shasum -a 256` before this review used their contents. All three SHA-256 values match the charge exactly (see the block above). No canonical ledger or charged file was edited, `jc2-lean` was not inspected, and no CAS was run. `FALLACY-v2` (flag/place/series, floor/attainment, typed charging) is in force. No new exit price is asserted, so there is no `charge_basis` line.

Line citations `integration`, `proof` follow the two non-report frozen files. Citations `review` are to the B0 gate review whose scopes the integration already binds (integration §1; hash `8ffc0a06…`, not a third frozen file of this lane). Primary PDFs were rehashed at execution and agree with the charged report’s §7:

```text
f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db  refs/jc86.pdf
88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad  refs/zoladek2008_official.pdf
```

Orevkov, *Math. USSR-Izv.* **29** (1987), Lemma 2.1 (`jc86.pdf` p. 2) and Lemma 5.2 (pp. 8–9); Żołądek, *Topology* **47** (2008), Prop. 6.5(b) (printed pp. 457–458 / PDF pp. 27–28). No substitute edition is used.

## 1. Promoted premises: scope consumption and local model

Standing: \(F\) a noninvertible plane Keller map of geometric degree \(N=5\); H2 says \(D:=A_F\) is irreducible. The integration promotes exactly one trivial-dicritical profile at this scope (integration 66–74, repairing the proof’s two-profile census by [Z-6.5(b)]):

\[
(\mu,\operatorname{corr})=(2,1)+(1,0),\qquad (s_2,s_1,a)=(1,1,2).
\]

Both dicriticals therefore dominate the **same** reduced irreducible curve \(D\). They are not two components of \(A_F\). The competing placement of the correction on the \(\mu=1\) dicritical is excluded by the same sourced implication \(\mu=1\Rightarrow\operatorname{corr}=0\), which is part of the promoted [Z-6.5(b)] reading (integration 108–116; review 85–93, 235–244).

Three integers are kept distinct, as the report does:

- \(\mu_2=2\) is the generic transverse ramification index of the **surface** map along the nontrivial dicritical;
- the unique correction point \(x\in\pi(l_2)\) has \(\mu_x=3\), because Orevkov’s exact budget \(\sum_l(\mu_l+\operatorname{corr}_l)=N-1=4\) together with integrality of local multiplicities forces a single jump of size one on the \(\mu=2\) prime;
- \(s_2=s_1=1\) are mapping degrees of the dicritical restrictions onto \(D\), equivalently (function fields) the degrees of the unique factorizations through the normalization of \(D\).

Corrections are attached to points of \(\pi(l)\), not to a cv flag or a Puiseux series (proof 38–50, 63–65; review 66–71). That discipline is respected throughout the charged argument.

Promoted pointwise calculus, consumed at the scopes the integration actually binds:

- **[O-5.2]** (`jc86.pdf` pp. 8–9): \(\mu_y=\mu_l\) at a chosen quotient point makes \(f^*\circ\pi\) a nonsingular local embedding of \(l\) at that point. No global vanishing of \(\operatorname{corr}_l\) is required; global vanishing is only a sufficient condition to apply it everywhere (review 73–77). Lemma 3.3 is promoted with that qualification (integration item 2).
- **[Z-6.5(b)]** (printed p. 457): \(\mu_{z_0}>\mu_D\) if and only if \(y_0=\widetilde P(z_0)\) is a singular point of the **immersed** curve \(S=\widetilde P(\widetilde D\setminus\infty)\). The parenthetical on the same page is the definition that will be used in §5: a singularity of \(t\mapsto(X,Y)(t)\) means \((X,Y)'(t_0)=0\); intersections of smooth local components are not singularities. Separately, \(\mu_D=1\) implies that immersed curve is smooth. This is strictly stronger than [O-5.2], not equivalent “on the nose” (review 85–93); the charged report follows the stronger, promoted reading.
- **Corollary 3.7**: under H2, \(\sum\mu_l\le N-2\). The profile saturates \(2+1=3=N-2\) and is therefore not killed by strictness. The promoted reading of the complementary jump is “critical point of an immersed parametrization,” not “locally irreducible singularity of the reduced germ” (integration 114–116).
- **Covering lemma** (M′ integration §1.3, consumed by the B0 proof at promoted scope): \(F^{-1}(D_0)\to D_0\) is a finite covering of degree \(a\), on the **smooth stratum** \(D_0=D\setminus\operatorname{Sing} D\) only. Conversion \(a_p=s_p-b_p\) is for all \(p\); box \((U,e>1)\) empty; flatness \(\sum_{y\in q^{-1}(p)}e_y=N\) at every \(p\in\mathbf C^2\).
- **Orevkov Lemma 2.1** (`jc86.pdf` p. 2): each finite-value boundary chain meets \(L_\infty\) once, the \(L_F\) component is the endpoint, and \(l':=l\setminus L_\infty\simeq\mathbf A^1\). The integration already binds the \(\varepsilon\equiv 0\) consequence of this lemma (integration §1.5). The charged report uses the affine-line statement as a primary-source input, which is the same repair the gate required.

Lemma 3.4 itself is promoted only under its two branches (smooth \(D\), or all \(\operatorname{corr}_l=0\) and \(2a\le N\)). The \(N=5\) profile satisfies neither. The charged report does not invoke the lemma’s **conclusion**; it uses the Euler **identities** that the gate wrote down before those branches (review 181–195). Those identities are consequences of promoted \((E)\), the \(\chi_c\) toolkit (including the normalization formula), and the smooth-stratum covering lemma. Re-derivation is in §3 below. This is legitimate custody, not an out-of-scope appeal to Theorem 3.5.

The local model at the correction is exactly as advertised: one point of \(\pi(l_2)\) with \(\mu_x=3\). That integer is the local multiplicity of the collapsed/finite **surface** map, not the multiplicity of the plane branch and not \(\operatorname{ord}\,d\eta\).

## 2. What the local model does not determine (OPEN[LOCAL-PUISEUX-N5])

## 2. What the local model does not determine (OPEN[LOCAL-PUISEUX-N5])

The typing `OPEN[LOCAL-PUISEUX-N5]` is correct for the **isolated** germ \((\mu_l,\mu_x)=(2,3)\) of a finite normal surface map, and it is correctly not treated as a residual after the complete profile is imposed.

Hand check of the two diagnostic germs (no CAS; these are not Keller witnesses, so using them as attainment would violate floor/attainment):

- For odd \(k\ge 1\), \(G_k(u,v)=(u,\,v^3-3u^k v)\). The local algebra at the origin is \(\mathbf C\{u,v\}/(u,v^3)\), length three. Jacobian determinant \(3(v^2-u^k)\); generic points of the critical curve have \(\partial^2 Y/\partial v^2=6v\neq 0\), so generic transverse index two. The parametrization \((u,v)=(t^2,t^k)\) of that critical curve (primitive because \(k\) is odd) maps to \((t^2,-2t^{3k})\), Puiseux type \((2,3k)\). Thus \((2,3)\), \((2,9)\), \((2,15),\ldots\) all display the same \((\mu_l,\mu_x)=(2,3)\). Żołądek’s own Whitney example (printed p. 457) is the case \(k=1\).
- The hypersurface \(W=\{z^3+xz+y^2=0\}\to\mathbf C^2_{x,y}\) is Cohen–Macaulay with isolated singularity (gradient \((z,3z^2+x,2y)\) vanishes only at the origin), hence normal, with local algebra \(\mathbf C\{z\}/(z^3)\). Discriminant \(4x^3+27y^4=0\), a \((3,4)\) branch. The ramification curve \(x=-3z^2\), \(y^2=2z^3\) normalizes by \((z,y)=(t^2,\sqrt 2\, t^3)\) onto \((-3t^4,\sqrt 2\, t^3)\). Generic ramification is simple.

The extra hypotheses that would pin the ordinary cusp — smoothness of the finite source and of the reduced ramification divisor at \(x\), forcing \(\operatorname{ord}_0 a=1\) after Weierstrass — are unpromoted. Local data therefore force a critical **primitive** normalization branch once \(s_2=1\) is in play (the nonprimitive loophole of review 235–244 is then closed), but no Puiseux characteristic. Against the *complete* profile the consistent list is empty by §5, so the OPEN records a genuine local underdetermination, not a surviving global candidate.

## 3. Euler / aggregate accounting

Under H2 there is one target component. The repaired \(N=4\) two-target aggregate must not be copied componentwise. The exact analogue of the affine-line repair is

\[
s_2=s_1=1,\qquad l_2'\simeq l_1'\simeq\widetilde D\simeq\mathbf A^1,\qquad c=1.
\]

Orevkov Lemma 2.1 supplies \(l_i'\simeq\mathbf A^1\). Degree one then identifies each with the unique normalization of the irreducible \(D\) (details in §5.1). This is the same primary-source repair used at review 321–337, now applied to the promoted degrees.

From promoted \((E)\), the \(\chi_c\) toolkit, and the smooth-stratum covering lemma, with \(\Sigma=\operatorname{Sing} D\), \(\sigma=|\Sigma|\), \(\nu=\sum(r_p-1)\), \(A=\sum a_p\), and \(D_0=D-\Sigma\):

\[
\chi_c(D)=2-c-\nu,\qquad
\chi_c(D_0)=2-c-\nu-\sigma,
\]
\[
\chi_c(F^{-1}(D))=a\,\chi_c(D_0)+A,
\]
because \(F^{-1}(D_0)\to D_0\) is an \(a\)-sheeted covering in the affine source (dicriticals live on the compactification, not in \(F^{-1}(D)\subset\mathbf C^2\)) and \(F^{-1}(\Sigma)\) contributes the finite set counted by \(A\). Substituting into \((E)\) yields the gate’s repaired identities, with no sign change and without either branch of Lemma 3.4:

\[
(N-a)\chi_c(D_0)=N-1-N\sigma+A.
\]

Putting \((N,a)=(5,2)\) gives \(3(2-c-\nu-\sigma)=4-5\sigma+A\), i.e.

\[
3c+3\nu-2\sigma+A=2.
\]

With \(c=1\) this is the exact \(N=5\) aggregate \(3\nu+A=2\sigma-1\). Arithmetic confirmed. The covering lemma is used here only on \(D_0\), which is its promoted scope.

## 4. Componentwise budgets and fibre equations

There are no separate image-curve budgets: both source components map to the same \(D\) and, after the isomorphisms of §5.1, induce the same \(\eta\).

**Fibre equation, every physical \(p\in D\).** Flatness of \(q\) (promoted, all \(p\)) gives \(\sum e_y=5\). Box \((U,e>1)\) empty, so every affine point contributes \(e=1\). Orevkov 2.1 supplies \(\varepsilon\equiv 0\): contracted \(L_C\) chains produce a point already on \(\pi(l)\), not an extra fibre point (integration §1.5; review 321–324). Because both \(h_i\) are isomorphisms onto \(\widetilde D\), each place of \(\eta^{-1}(p)\) contributes exactly one point of \(B_1\) and one of \(B_2\).

These points of \(Y\) are distinct. The report’s “additivity of local degree under coalescence” is a cruder bound than needed, but the conclusion is correct:

- \(B_1\simeq\mathbf A^1\) and \(B_2\simeq\mathbf A^1\) are smooth, so two places of one prime cannot be the same point of \(Y\).
- A point of \(B_1\cap B_2\) would lie on \(B_1\), hence have \(e_y=\mu_1=1\) by \(\operatorname{corr}_1=0\), but it would also lie on \(B_2\), whose generic multiplicity is 2, so \(e_y\ge 2\). Contradiction. Cross-dicritical collision in the affine finite model is therefore impossible, without any claim that local degrees add at a crossing.

Thus over \(p\) one has \(r_p\) points of \(B_1\) each of multiplicity 1, \(r_p\) points of \(B_2\) each of multiplicity 2, plus \(\iota_p=1\) extra at the unique correction when \(p=p_*:=\phi_2(x)\), plus \(a_p\) affine points of multiplicity 1:

\[
a_p+3r_p+\iota_p=5.
\]

At \(p_*\), \(r_{p_*}\ge 1\) and \(\iota=1\) force \(r_{p_*}=1\), \(a_{p_*}=1\), partition \((3,1,1)\). Local irreducibility at the correction image is a consequence of the degree-five fibre, not of [Z-6.5(b)]. For \(p\neq p_*\) the same equation forces \(r_p=1\), \(a_p=2\). At those points both restricted parametrizations are nonsingular embeddings by pointwise [O-5.2]; a unibranch germ with that property is smooth. Hence \(p_*\) is the only singular point, and

\[
\sigma=1,\qquad \nu=0,\qquad A=1.
\]

The aggregate of §3 becomes \(1=1\). Strictness does not kill the arithmetic: \(\sum\mu_l=3=N-2\), saturating Corollary 3.7.

The curve budget before the second dicritical is then: polynomial curve, \(\widetilde D\simeq\mathbf A^1\), one affine singularity, unibranch, \(\nu=0\) but \(a_{p_*}=1\), and a critical primitive normalization forces \(\delta_{p_*}\ge 1\), hence Milnor number \(2\delta_{p_*}\ge 2\), unrelated to Orevkov’s \(\mu_x=3\). Euler bookkeeping uses \(r_p-1\), not \(\delta_p\), so it does not pin a Puiseux pair. The second row of the report’s table — \(\eta\) immersive at the same \(z\) — forces the germ smooth and \(\delta=\mu_{\mathrm{Mil}}=0\). That incompatibility is the content of §5; the Euler/fibre pin is a consistent shape, not the killing blow.

No floor was treated as attainment. No illicit componentwise copy of the reducible \(N=4\) identity occurs.

## 5. Heart: shared normalization, \(h_1/h_2\), and flag/place discipline

This is the load-bearing step. Default-to-refutation concentrated here: the covering lemma’s smooth-stratum scope, the identification of two source points with one place, and the chain rule at a singular image.

### 5.1 Covering/normalization data and degree-one factorization

Let \(\phi_i:l_i'\to D\subset\mathbf C^2\) be the two restricted maps. Each source \(l_i'\) is a smooth (hence normal) affine line by Orevkov Lemma 2.1. The universal property of the normalization \(\eta:\widetilde D\to D\) therefore supplies unique morphisms of **curves**

\[
\phi_i=\eta\circ h_i,\qquad h_i:l_i'\longrightarrow\widetilde D,
\]

defined on all of \(l_i'\), including at the correction point \(x\in l_2'\) and including over the possibly singular image \(p_*=\eta(z)\). This factorization is not an instance of the covering lemma. The covering lemma concerns the affine source covering \(F^{-1}(D_0)\to D_0\). Dicritical curves live on the compactification; they are not among the \(a\) affine sheets. Lemma 3.4’s proof already uses the same factorization for every dicritical dominating an irreducible \(D\) (proof 241–243), before either case branch, and that lemma is promoted with the equality repair.

Degrees: \(s_i:=\deg(l_i'\to D)\). Function fields of a reduced irreducible curve and of its normalization coincide, so \(\deg h_i=s_i\). The promoted profile has \(s_2=s_1=1\). (Independently: \(\operatorname{corr}_1=0\) plus [O-5.2] makes \(\phi_1\) an immersion at every finite point, hence \(h_1\) unramified; a finite étale map \(\mathbf A^1\to\widetilde D\) is an isomorphism because \(\mathbf A^1\) is simply connected. Combined with the generic fibre \(a+2s_2+s_1=5\) and \(a\ge 1\), this forces \(s_2=1\), \(a=2\) uniquely. The promoted pair \((s_2,s_1,a)=(1,1,2)\) is therefore also recovered from Orevkov 2.1 plus fibre arithmetic.)

Finiteness: \(\Phi\) extends regularly to the compactification, so each \(l_i\simeq\mathbf P^1\to\overline D\) is a morphism of projective curves of degree \(s_i=1\). Factoring through the normalization of the projective closure gives a degree-one map \(\mathbf P^1\to\widetilde{\overline D}\), hence an isomorphism of smooth rational curves. Restricting to the unique infinite place (Lemma 2.1: \(l\) meets \(L_\infty\) once) yields \(c=1\), \(\widetilde D\simeq\mathbf A^1\), and \(h_i\) an isomorphism of affine lines. In particular both parametrizations are primitive: the nonprimitive loophole of review 235–244 is closed.

H2 enters exactly here: there is one reduced irreducible \(D\), hence one \(\eta\), and both degree-one maps land on that same \(\widetilde D\). The integers \(s_1=s_2=1\) are the reason both \(h_i\) are isomorphisms rather than ramified covers of \(\eta\).

The factorization is therefore licensed **at the correction point itself**. Nothing in this paragraph asked the covering lemma to see \(p_*\).

### 5.2 Comparison at the place \(z\) versus the singular image

Put \(z:=h_2(x)\in\widetilde D\) and \(x_1:=h_1^{-1}(z)\in l_1'\). These are well-defined because \(h_2,h_1\) are isomorphisms of smooth curves. The three objects that `FALLACY-v2` forbids identifying remain distinct:

- \(x\in l_2'\) and \(x_1\in l_1'\) are two distinct physical points of two distinct boundary primes;
- \(z\) is a place of the algebraic normalization \(\widetilde D\);
- \(p_*=\eta(z)\) is the physical singular point of \(D\subset\mathbf C^2\);
- no cv flag or cover series is used.

The comparison in (5.1)–(5.2) is the chain rule for holomorphic maps of smooth source curves **into \(\mathbf C^2\)**. Write \(\eta\) and \(\phi_i\) as \(\mathbf C^2\)-valued maps (the embedding \(D\hookrightarrow\mathbf C^2\)). Then \(d\eta(z)\in\operatorname{Hom}(T_z\widetilde D,\,T_{p_*}\mathbf C^2)\) is defined because \(\widetilde D\) is smooth at every place, including those lying over a singular image. Differentiating an abstract map \(\widetilde D\to D\) of singular schemes is never invoked. This is exactly Żołądek’s parenthetical: a singularity of the immersed curve means \((X,Y)'(t_0)=0\).

The covering lemma still does not enter. Flatness of \(q\) at \(p_*\) was used only for the fibre pin of §4, which §5 does not need: even if several places lay over \(p_*\), the contradiction is already at this particular place \(z\) coming from the unique correction.

### 5.3 Equations (5.1)–(5.2) and promoted-statement consistency

[Z-6.5(b)], both directions, at the affine quotient point corresponding to \(x\in l_2'\setminus\infty\): \(\mu_x=3>2=\mu_2\) if and only if \(\phi_2'(x)=0\) as a map \(l_2'\to\mathbf C^2\). (The reverse implication is the “local Jacobian calculation” on printed p. 458; the Whitney germ on p. 457 is the model case \(\mu_D=2\), \(\mu_{(0,0)}=3\).) The curve \(l_2'\) is smooth at \(x\), whether or not \(x\) is an \(L_C\)-meeting in the surface: Lemma 2.1 contracts \(L_C\) onto a point of \(\pi(l)\), and \(\pi|_l\) remains an isomorphism of the abstract curve \(l\simeq\mathbf P^1\). So

\[
0=d\phi_2(x)=d\eta(z)\circ dh_2(x).
\]

Here \(h_2\) is an algebraic isomorphism of smooth curves, so \(dh_2(x)\neq 0\). Therefore \(d\eta(z)=0\). This is (5.1). Primitivity was essential: if \(\deg h_2\ge 2\), vanishing of \(d\phi_2\) could be ramification of \(h_2\) with \(d\eta\neq 0\), which is Żołądek’s second example on p. 457 (two-fold map \(D\to S\), \(\mu_D=3\), \(\mu_{(0,0)}=8\)).

Since \(h_1\) is likewise an isomorphism,

\[
d\phi_1(x_1)=d\eta(z)\circ dh_1(x_1)=0.
\]

This is (5.2). But \(\mu_1=1\) and \(\operatorname{corr}_1=0\), so [O-5.2] at the point \(x_1\) (or [Z-6.5(b)] globally for \(\mu=1\)) makes \(\phi_1\) a nonsingular embedding at \(x_1\), hence \(d\phi_1(x_1)\neq 0\). Contradiction.

No promoted statement collides with this conclusion. Corollary 3.7 permits the numerical profile and only forces some critical point of some immersed parametrization; the extra input is that a second primitive copy of the same \(\eta\) cannot be immersive at that place. Lemma 3.3 is applied only to the zero-correction dicritical. Proposition 4.1 concerns an all-trivial branch locus and is not used. Theorem 4.2 is \(N=4\). The covering lemma’s smooth-stratum restriction is never violated. The local models of §2 are not Keller witnesses.

The Euler/fibre shape of §3–§4 is compatible arithmetic, not a hidden extra hypothesis of (5.1)–(5.2). The kill is the chain rule on \(\widetilde D\).

## 6. Counterfactual typing and residual PI1 questions at \(N=5\) under H2

Section 6 of the charged report is correctly typed. After (5.1)–(5.2) the profile does not exist, so there is no complement-group question attached to it. No `OPEN[PI1-S5-CORR]` should be entered, and no PI1 acquisition is required for this profile.

The displayed **counterfactual** `PI1-S5-CORR` is what would remain if one deliberately forgot the \(\mu=1\) copy: an irreducible polynomial curve, \(\widetilde D\simeq\mathbf A^1\), one unibranch affine singularity which is the discriminant of a normal triple cover with generic simple ramification and one local-degree-three point, with \(\pi_1(\mathbf C^2-D)\twoheadrightarrow S_5\) sending meridians to transpositions and with local orbit partition \((3,1,1)\). The \(S_5\) target and the local \(S_3\) are correctly forced by transpositions generating a transitive group. A YES would still not realize the Keller configuration, because it omits the second degree-one parametrization. The source-aware residual is exactly “can one \(\eta:\mathbf A^1\to D\) be critical at \(z\) through one degree-one dicritical and immersive at the same \(z\) through another?”, which (5.1)–(5.2) answer NO.

Scope warning, not a defect: “no PI1 question remains at \(N=5\) under H2” is **profile-scoped**. Other \(N=5\) H2 profiles with no trivial dicritical (for instance a unique \((\mu,\operatorname{corr})=(2,2)\) or \((3,1)\)) are outside B0 and are not closed by this lane.

## 7. Generalization under H2: all \(N\), \(s=1\), and the \(s\ge 2\) break

The \(N=5\) kill does not use \(N=5\) except to force \(s_2=1\) from the fibre equation and to name the unique residual profile. The chain-rule engine is:

- H2: both dicriticals dominate one irreducible \(D\), so one \(\eta\);
- a dicritical \(l_0\) with affine image and \(\mu_{l_0}=1\), hence \(\operatorname{corr}_{l_0}=0\) by [Z-6.5(b)], hence \(s_{l_0}=1\) by Orevkov 2.1 plus [O-5.2] (finite étale \(\mathbf A^1\to\widetilde D\));
- a correction on some dicritical \(l\) (possibly different from \(l_0\)) with \(s_l=1\).

Then \(h_l\) is an isomorphism, the jump gives \(d\eta(z)=0\), and the \(\mu=1\) copy is immersive at the same place. Euler characteristic, Puiseux type, uniqueness of the singular point, and the value \(\mu=2\) are unused.

**What breaks at \(s_l\ge 2\) on the corrected dicritical.** Then \(d\phi_l(x)=0\) need not imply \(d\eta(z)=0\): the vanishing may be ramification of \(h_l\) along a possibly smooth branch. That is the nonprimitive loophole, realized as a local (non-Keller) picture by Żołądek’s second example. The argument does **not** break if only the trivial dicritical were allowed to have \(s\ge 2\), because that case does not occur: \(\mu=1\) plus Orevkov 2.1 already forces \(s=1\).

**What breaks without H2.** Distinct target components have distinct normalizations; a jump on \(D_1\) does not constrain the parametrization of \(D_0\). That is the surviving \(N=4\) residual.

At \(N=5\) under H2 the generic fibre \(a+2s_2+s_1=5\) with \(s_1=1\) and \(a\ge 1\) leaves only \(s_2=1\), so every residual trivial-dicritical profile is of the killed shape. For \(N\ge 6\) the same engine leaves a residual: a trivial dicritical together with all corrections supported on dicriticals of mapping degree \(\ge 2\).

**Typed statement for a successor lane.**

> **B0-H2-s=1 (candidate, all \(N\ge 3\)).** Let \(F\) be a noninvertible plane Keller map with \(A_F\) irreducible. Then \(F\) cannot have both (i) a dicritical with affine image and \(\mu=1\), and (ii) a dicritical of mapping degree \(s=1\) that carries a positive correction. Equivalently: under H2, if every correction lies on an \(s=1\) dicritical, there is no trivial dicritical.
>
> **Corollary already proved at \(N=5\):** there is no trivial affine-image dicritical. Thus B0 extends to \(N=5\) under H2.
>
> **Residual for \(N\ge 6\) under H2:** trivial-dicritical profiles in which every correction lives on a dicritical with \(s\ge 2\). The nonprimitive loophole is then open, and a new input is required.

This is a typed successor, not a promotion. The present lane proves the \(N=5\) case, where (ii) is automatic.

## 8. Verdict

**CONFIRMED.** Promote: under H2, the unique \(N=5\) trivial-dicritical profile \((\mu,\operatorname{corr})=(2,1)+(1,0)\) with \((s_2,s_1,a)=(1,1,2)\) is impossible. Consequently B0 extends to \(N=5\) under H2.

The argument is not the \(N=4\) row-(d) strictness argument. Euler and fibre pin a consistent shape \((\sigma,\nu,A)=(1,0,1)\) with local partition \((3,1,1)\); the two degree-one parametrizations then contradict one another by the chain rule at a single normalization place \(z\). Local Puiseux type remains `OPEN[LOCAL-PUISEUX-N5]` as an isolated-germ statement and is empty against the complete profile. No PI1 residual attaches to this profile.

Hostile targets that failed: (i) covering-lemma scope at \(p_*\) — factorization is the universal property of \(\eta\), comparison is at \(z\in\widetilde D\); (ii) possible ramification of \(h_2\) at the jump — forbidden by \(s_2=1\); (iii) [Z-6.5(b)] speaking only of a singular reduced germ — the source defines the singularity of the immersed curve as vanishing of \((X,Y)'\); (iv) the \(\mu=1\) copy hitting a different place — \(h_1\) is an isomorphism onto the same \(\widetilde D\); (v) Euler identities taken from Lemma 3.4 outside its promoted branches — they follow from \((E)\), \(\chi_c\), and the smooth-stratum covering lemma, as already written in the bound equality repair.

`OPEN[B0-GENERAL-N]` is therefore closed at \(N=5\) under H2, and remains open for \(N\ge 6\) only in the \(s\ge 2\) residual named in §7.

Primary sources consumed: Orevkov Lemma 2.1 and Lemma 5.2; Żołądek Proposition 6.5(b), both directions, with the printed parenthetical. No new exit price. No CAS. No ledger, charged-file, or `jc2-lean` inspection.

<!-- BODY-END -->

