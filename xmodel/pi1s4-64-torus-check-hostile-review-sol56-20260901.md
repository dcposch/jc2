# Hostile review of THEOREM ROW-KILL

## 0. Executive verdict and exact scope

**Verdict: PROMOTE ROW-KILL ONLY AS CORRECTED; REJECT THE REPORT AND ITS CAMPAIGN-CLOSURE TABLE AS WRITTEN.** The no-cover conclusion is true for the explicit ROW-NF curves with

\[
c\ne0,\qquad j=b^3/c^2\notin\{-27/4,-81/16\},
\]

but one advertised geometric premise is false and requires a new case argument. The allowed value \(j=0\) has one ordinary triple point \(D_4\), not three nodes. After proving that a \(D_4\) point cannot be inner in a torus presentation, all four NO-TORUS routes extend to it. INF-TRIVIAL also survives at \(j=0\), because its proof needs only the three disjoint folds over \(x=0\), not the report’s false global discriminant census. Thus the repaired chain still excludes every \(S_4\) transposition-meridional surjection on the stated explicit-family scope.

Two further corrections are binding. First, if \(\gamma_\infty\) denotes the standard positive divisor meridian, it is conjugate to the inverse of the geometric-basis product; triviality of its image is unchanged. Second, the downstairs value is unambiguously \(\Pi=1\), \(c(\Pi)=4\), \(g_L=0\); `(2,1)` is an upstairs/non-descending datum or a transcription error.

The projective step is sound after inserting Riemann existence and keeping reduced and weighted branch divisors distinct. The cited source is Taketo **Shirane**, not Shimada; Corollary 0.6 has no genericity or non-cyclic hypothesis and forces the torus identity for the normalized degree-three cover.

What does **not** follow is the blanket claim that every auxiliary OPEN is “resolved NO/vacuous,” that the entire nodal row is dead, or that the result does not transfer to `(8,4)`. The literal partial `FIXED-TUPLE` system and the braid factorization remain different mathematical questions; \(j=-27/4\) is still a three-node curve outside the proved scope; and actual target-equivalence would make the complement property transfer automatically. Exact statuses appear in §§8–10.

## 1. Frozen-input integrity and review method

The stop check passed before any frozen input was read. `shasum -a 256` returned, in the order charged,

```text
a352be2af1aebb5e158cb541a6eacdd0feb90f2ea3aa6750fb4bf1969c6bfefe
a130acb580933543a6909753e665c56295bd4ab052469caa8c84e041766c2467
d0dc4f7971b39f516dae2337cb172f8357bb1618b1143b800c524dbf95b5f31a
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286
```

for `pi1s4-64-torus-check-opus5-20260831.md`, `lit-targeted-endgame-grok46-20260831.md`, `pi1s4-64-zvk-u6-opus5-20260831.md`, and `block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md`, respectively. I abbreviate those frozen files as `TC`, `LIT`, `ZVK`, and `INT`, with line numbers referring to the frozen copies.

I used no CAS and inspected no `jc2-lean` material. The only external mathematical inputs consumed are the primary Oka and Shirane PDFs recorded below; both were streamed rather than retained as review artifacts. All other checks are exact calculations from ROW-NF or elementary topology/group theory. The FALLACY-v2 exit-price rule is inapplicable: this report asserts no new exit price and therefore contains no `charge_basis` declaration.

## 2. Geometry of the generic `(6,4)` row sextic

ROW-NF gives

\[
x=r(t)^2,\quad y=q(t),\qquad r=t^3+bt+c,\quad
q=t^4+\frac{2b}{3}t^2+\frac{4c}{3}t,\quad c\ne0,
\]

with \(j=b^3/c^2\) (`ZVK` 154–163). The implicit curve is the irreducible component defined by

\[
F_{b,c}(x,y)=\operatorname {Res}_t(x-r(t)^2,y-q(t))
\]

up to a nonzero scalar. More intrinsically, the projective parametrisation is

\[
[S:T]\longmapsto[(T^3+bTS^2+cS^3)^2:
S^2(T^4+\tfrac{2b}{3}T^2S^2+\tfrac{4c}{3}TS^3):S^6].
\]

The off-diagonal coincidence equations have only finitely many solutions, so this map is birational. A generic line pulls back with degree six; hence its image is an irreducible reduced sextic. This validates the resultant/degree/irreducibility part of `TC` 89–101.

At \(S=0\) there is exactly one preimage and one place, \(Q_\infty=[1:0:0]\). In the \(X=1\) chart, with \(s=S/T\),

\[
v=Y/X=s^2(1+O(s^2)),\qquad w=Z/X=s^6(1+O(s^2)).
\]

Thus the germ has multiplicity two, \(I_{Q_\infty}(\bar F,L_\infty)=\operatorname{ord}_s w=6\), and Bézout shows that this is the entire intersection with \(L_\infty\). The affine δ-total is three and the normalization is ℙ¹, so δ at infinity is \(10-3=7\). A multiplicity-two plane branch with δ seven has semigroup \(\langle2,15\rangle\) and analytic type \(A_{14}\). These conclusions are correct for every \(c\ne0\), including the exceptional affine configurations.

There is, however, a decisive error in the claimed “three-node stratum.” For a coincident pair \(t\ne s\), put \(e=t+s\). Exact elimination gives

\[
h(e)=e^3+\frac{4b}{3}e-\frac{4c}{3}=0,\quad
r(t)=r(s)=-\frac{e^3}{4},\quad
q(t)=q(s)=\frac b3(e^2+b). \tag{2.1}
\]

For \(b\ne0\), different roots of \(h\) give different image points; their tangent determinant is, up to a nonzero factor,

\[
(t-s)(3e^2+4b)(9e^2+4b).
\]

The second factor can vanish only when \(c=0\), and the third is \(3h'(e)\). Consequently the affine curve has three distinct ordinary nodes exactly when \(b\ne0\) and \(j\ne-81/16\). The value \(j=-27/4\) only makes \(r\) have a double root and changes the chosen projection; it does not destroy the three nodes.

At the allowed value \(j=0\), take \(b=0\). The three roots of \(h(e)=e^3-4c/3\) all give the same point. Equivalently, its three preimages satisfy \(t^3=-4c/3\) and map to

\[
(x,y)=(c^2/9,0).
\]

Their tangent slopes are \(2/t^2\), hence are distinct: this is one ordinary triple point \(D_4\), with δ three, not \(3A_1\). Thus `TC` 85–87, 128–139 and 395–399 and `ZVK` 200–205 are false at \(j=0\). The actual nodal locus is \(j\notin\{0,-81/16\}\); the projection used later additionally requires \(j\ne-27/4\). Any promotion must state this correction.

## 3. THEOREM NO-TORUS: four independent proofs

The local exclusion used throughout is correct but needs one extension. At a common zero of \(G_2,G_3\), a germ \(G_2^3+G_3^2\) cannot be an ordinary node: its quadratic tangent cone is either \(G_{3,1}^2\) or zero. It cannot be an ordinary triple point either: multiplicity three forces—after excluding a quadratic leading term—\(\operatorname{ord}(G_2)=1\), \(\operatorname{ord}(G_3)\ge2\), so its cubic tangent cone is the triple line \(G_{2,1}^3\), not three distinct lines. Thus both \(A_1\) and the \(j=0\) \(D_4\) point are outer in any torus presentation.

1. **Conic/contact proof: valid and effectively source-free.** If \(\bar F=G_2^3+G_3^2\), irreducibility gives \(\gcd(G_2,G_3)=1\). The conic \(G_2=0\) meets \(\bar F\) only at common zeros of \(G_2,G_3\), hence only at singularities. The affine singularities are excluded as above, so all Bézout contact \(6\cdot2=12\) lies at \(Q_\infty\). In the \(X=1\) chart the six conic monomials \(1,v,v^2,w,vw,w^2\) have distinct valuations

   \[
   0,2,4,6,8,12.
   \]

   Therefore contact at least 12 forces \(G_2\in\mathbf C Z^2\). Then \(\bar F=Z^6+G_3^2\) splits into two cubics, contradicting irreducibility. `TC` 199–246 is correct on \(3A_1\), and the preceding \(D_4\) lemma repairs it at \(j=0\). Although `TC` introduces this via Tokunaga’s criterion, only the elementary necessary direction supplied by the displayed identity is used.

2. **Oka ρ-count: valid after the same \(D_4\) repair.** I re-fetched Mutsuo Oka, *Zariski pairs on sextics I*, arXiv:math/0507051v1, from `https://arxiv.org/pdf/math/0507051`; SHA-256 is
   `2a864cdd2530533c30f45d2cf9e9435e24f6a53b3788094df26a63e7208213e4`, exactly the frozen receipt. Pages 2–3 state the quoted inner-simple classification and Proposition 2: an inner simple point has ρ equal to \(I(C_3,C_2;P)\), and the inner ρ-sum is six for a torus sextic with only simple singularities. Nodes and \(D_4\) are not among the possible inner types \(A_{3\iota-1}\) or \(E_6\); the \(A_{14}\) point contributes either zero (outer) or five (inner). Neither total is six. The report’s use is exact.

3. **Parametric pullback proof: valid.** Pulling an affine identity \(A^3-B^2=F\), with \(\deg A\le2,\deg B\le3\), back to the normalization gives \(a(t)^3=b(t)^2\). A zero of \(a\) would map to a common zero of \(A,B\), hence an inner affine point; smooth points, nodes, and the \(D_4\) point are all impossible. Thus \(a\in\mathbf C^*\). The leading degrees of \(x^2,xy,y^2,x,y,1\) after substitution are successively \(12,10,8,6,4,0\), so descending comparison makes \(A\) constant. Then \(F=A^3-B^2\) factors, a contradiction. `TC` 319–349 is sound once its affine-singularity sentence is corrected.

4. **Cubic/maximal-contact proof: valid.** The cubic \(G_3=0\) likewise meets the sextic only at inner points, hence only at \(Q_\infty\). Since \(\operatorname{mult}_{Q_\infty}F=2\), \(G_3\) must be smooth there; otherwise both summands have order at least three. Bézout demands contact 18, whereas a smooth germ at an \(A_{14}\) branch has contact at most 15. Contradiction.

For the quoted Tokunaga provenance I also fetched Hiro-o Tokunaga, *\((2,3)\) torus sextics and the Albanese images of 6-fold cyclic multiple planes*, Kodai Math. J. 22 (1999), 222–242, DOI `10.2996/kmj/1138044044`; the J-STAGE PDF SHA-256 is `3c85df2accb8d9e9d57aa205c504ae96defb35b3c2ab0eadb4e6934901dac0be`. Its Theorem 0.4 supplies the nontrivial sufficient conic criterion for irreducible simple-singularity sextics; Oka’s Lemma 3 records the iff formulation quoted by `TC`. No scope mismatch affects the use here.

Conclusion: NO-TORUS is established for the true \(3A_1+A_{14}\) locus and, by the explicit repair above, also for \(j=0\) with \(D_4+A_{14}\). Calling the four routes fully independent is slightly too strong—they share irreducibility and the elementary inner-point exclusion—but each contradiction is otherwise self-contained.

## 4. The `S_3` resolvent and elementary group theory

Let

\[
V=\{1,(12)(34),(13)(24),(14)(23)\}\triangleleft S_4.
\]

The action on the three nonidentity elements of \(V\), equivalently on the three partitions of four letters into two pairs, gives \(S_4/V\cong S_3\). A transposition fixes one such partition and swaps the other two, so its image is a transposition. Therefore composing any onto meridional map \(\phi\) to \(S_4\) with \(S_4\twoheadrightarrow S_3\) is still onto and still sends every curve meridian to a transposition. The word “odd” alone is not the argument; the explicit quotient and its action are.

The stronger `ZVK` union statement is also correct. If \(\Gamma=\pi_1(\mathbf C^2-U_6)\) maps onto \(S_4\), the three x=0 relations upstairs say that each paired pair of transpositions commutes. After quotienting to \(S_3\), commuting transpositions must be equal (there are no disjoint transpositions in \(S_3\)). Thus the image tuple also satisfies the three downstairs identification relations, is fixed by the missing half-twist \(\beta_0\), and hence factors through \(G=\pi_1(\mathbf C^2-D)\). Surjectivity is preserved. This validates ZVK-RESOLVENT, but only its quotient-existence conclusion, not a computation of the full upstairs presentation.

## 5. THEOREM INF-TRIVIAL and the ZVK-U6 assembly

The six-strand count is correct: \(r(t)^2=x_*\) has six roots on a regular vertical fibre. The *distinct discriminant-value* census in `ZVK` 227–286 is not correct on the report’s whole stratum. At \(j=0\), \(r'=3t^2\), so the purported two simple tangencies coalesce at \(x=c^2\); the three pair singularities coalesce to the \(D_4\) point over \(x=c^2/9\). Hence \(\Sigma_x=\{0,c^2,c^2/9\}\), not six points. More generally two node values coincide at \(j=-2\), and a tangency value meets a node value at

\[
j=-16/3,\qquad j=-4\pm2\sqrt3.
\]

One quick derivation is to put \(z=ba/c\) for \(r'(a)=0\), so \(z^2=-j/3\), and \(w=be/c\) for a root of \(h\), so \(3w^3+4jw-4j=0\). Tangency values are \(c^2(1+2z/3)^2\), while node values are \(c^2(w-1)^2/9\); comparing them gives the listed coincidences. These errors invalidate the advertised “six downstairs/eleven upstairs distinct values” and its local-type split at those moduli. They do not enter INF-TRIVIAL.

The first feed actually needed by INF-TRIVIAL is valid for every \(j\ne-27/4\). The three roots \(\tau_i\) of \(r\) are then simple, and

\[
q'\equiv-\frac83(bt+c)\pmod r
\]

cannot vanish at a root of \(r\) when \(c\ne0\). Their limiting \(y\)-levels are also distinct: modulo \(r\), \(q=(ct-bt^2)/3\), and for distinct roots \(\tau_i,\tau_j\), with remaining root \(\tau_k\),

\[
q(\tau_i)-q(\tau_j)=-\frac{(\tau_i-\tau_j)\tau_k^3}{3}\ne0.
\]

Locally \(t=\tau_i\pm\sqrt{x}/r'(\tau_i)+O(x)\), so a loop around \(x=0\) produces three simultaneous half-twists supported in disjoint discs. A geometric basis adapted to those discs makes the braid \(\sigma_1\sigma_3\sigma_5\), and its ZvK relations are exactly

\[
g_1=g_2,\qquad g_3=g_4,\qquad g_5=g_6. \tag{5.1}
\]

The second feed is standard but has an orientation correction. The compactified vertical fibre meets \(L_\infty\) at \(Q'=[0:1:0]\notin\bar F\). For a consistently based geometric basis, its large affine boundary is

\[
\delta=g_6g_5g_4g_3g_2g_1.
\]

Using (5.1) gives the exact relation

\[
\delta=g_5^2g_3^2g_1^2. \tag{5.2}
\]

A positive divisor meridian \(\mu_{L_\infty}\) uses the local coordinate \(w=1/y\), so it is conjugate to \(\delta^{-1}\), not \(\delta\). Correspondingly \(H_1\) has \([\mu_{L_\infty}]=-6[g]\), whereas `TC` 482–486 calls the affine loop \(\delta\) a meridian and assigns \(+6[g]\). Thus the literal requested identity “\(\gamma_\infty=g_5^2g_3^2g_1^2\)” is correct only for `TC`’s affine-loop convention; with the standard positive meridian it is the inverse, up to basing conjugacy.

This convention does not affect the theorem. If every \(g_i\) maps to an involution, (5.2) makes \(\chi(\delta)=1\), hence also \(\chi(\mu_{L_\infty})=1\). The x=0 matching need not agree with the infinity-cable matching: Hurwitz-changing to the x=0-adapted basis preserves the boundary product. INF-TRIVIAL is therefore valid throughout the stated \(j\notin\{-27/4,-81/16\}\), including the \(j=0\) \(D_4\) member, despite the false global discriminant census.

## 6. The `c(Π)` conflict

The report’s own derivation wins decisively. For the downstairs degree-four cover of a vertical line, the six finite branch cycles are transpositions and their product is \(\Pi=\phi(\delta)=1\). Hence \(c(\Pi)=4\), and Riemann–Hurwitz gives

\[
2g_L-2=4(-2)+6+(4-c(\Pi))=-2,
\]

so \(g_L=0\).

The attempted reconciliation in `ZVK` 469–474 is geometrically impossible downstairs. A vertical projective line \(X=x_*Z\) meets \(L_\infty\) at \(Q'=[0:1:0]\), while the sextic meets \(L_\infty\) only at \(Q_\infty=[1:0:0]\). Its degree-six intersection is exhausted by the six affine points; there is no multiplicity-two downstairs place at \(Q'\).

That residual intersection belongs to the *upstairs* degree-eight union: each quartic \(D'\) and \(D'^-\) passes through \(Q'\). For a non-descending upstairs representation their two meridians may be disjoint transpositions, giving a double-transposition product, \(c=2\), and \(g_L=1\); for a fold-descending representation they are equal and the product is the identity. Thus `(2,1)` is either an upstairs/non-descending datum or a transcription error. It is incompatible with the downstairs relations (5.1). Promote the corrected downstairs value \((c(\Pi),g_L)=(4,0)\); R3 is no longer an open mathematical conflict.

## 7. Projective descent and Shirane Corollary 0.6

The cited author is **Taketo Shirane**, not Shimada. I re-fetched *A note on normal triple covers over ℙ² with branch divisors of degree 6*, arXiv:1211.2526v1, from `https://arxiv.org/pdf/1211.2526`; SHA-256 is

```text
b37e8d45381a299e489516fd479ec896a016f06c402b16ae049d310aa1618153
```

exactly the frozen receipt. As a second receipt, the published Kodai Math. J. 37 (2014), 330–340 PDF (`https://www.jstage.jst.go.jp/article/kodaimath/37/2/37_330/_pdf`, DOI `10.2996/kmj/1404393890`) hashes to `be755f0b83a4ec39a8da97ebf138a6754a4a5469de59166db264ee9a66eef235`.

Write \(U=\mathbf P^2\setminus(\bar F\cup L_\infty)\) and \(W=\mathbf P^2\setminus\bar F\). The inclusion \(U\hookrightarrow W\) induces a surjection on fundamental groups whose kernel is normally generated by a line-at-infinity meridian. INF-TRIVIAL therefore makes the onto \(S_3\) resolvent descend uniquely to \(\pi_1(W)\).

One standard step omitted by `TC` should be inserted. Generalized Riemann existence algebraizes the connected three-sheeted topological cover of \(W\) afforded by the natural \(S_3\)-action. Normalize ℙ² in its degree-three function field. The result \(X\) is integral and normal and \(X\to\mathbf P^2\) is finite of degree three. A normal surface is Cohen–Macaulay; over the smooth surface ℙ², miracle flatness makes this finite morphism flat. This is precisely the point of Shirane Remark 0.2.

At the generic point of \(\bar F\), inertia is a transposition, so the ramification index is two. The cover is étale off \(\bar F\), and possible special behavior over its singular points creates no additional divisorial branch component. In notation that avoids Shirane’s easily lost overbar,

\[
S_\pi=\bar F,\qquad T_\pi=0,\qquad
B_\pi:=S_\pi+2T_\pi=\bar F,\qquad \deg B_\pi=6. \tag{7.1}
\]

Shirane distinguishes the reduced branch locus \(S_\pi+T_\pi\) from the weighted branch divisor \(S_\pi+2T_\pi\); `TC` 417–420 conflates their displayed symbols. It is harmless here only because \(T_\pi=0\).

Corollary 0.6 is exactly an iff for a degree-six **weighted** branch divisor of a normal triple cover. Its necessary direction produces homogeneous \(G_2,G_3\) with \(G_2^3+G_3^2=0\) defining that divisor, plus two local primitivity conditions. The printed phrase assigning degrees \(i=1,2\) is a typo; the formula and proof use degrees two and three. Thus `TC`’s quotation is not literally verbatim, but its mathematical reading is right. Applying the necessary direction to (7.1) contradicts NO-TORUS.

There is no genericity, non-cyclicness, simple-singularity, or smooth-\(X\) hypothesis in Corollary 0.6. For completeness, the constructed cover is non-Galois because its monodromy closure is onto \(S_3\); and it is “generic” in the Ishida–Tokunaga sense because generic inertia is a transposition, so total-ramification points form a proper closed subset of the branch curve and hence are finite. Those facts discharge the alternative theorem too, but Shirane makes them unnecessary.

## 8. Audit of the resolved-NO table

The cover-existence conclusion now follows for the *explicit ROW-NF family* at every \(j\notin\{-27/4,-81/16\}\): use \(3A_1+A_{14}\) when \(j\ne0\), the repaired \(D_4+A_{14}\) argument when \(j=0\), then the \(S_3\) resolvent, INF-TRIVIAL, projective descent, and Shirane. The auxiliary labels do not all acquire the same status.

| item | exact consequence |
|---|---|
| `ROW-KILL` / actual affine \(S_4\) quotient | **NO** on the stated explicit-family scope, after the \(j=0\) repair and infinity-orientation correction. Its identification with every campaign row member remains conditional on provisional FOLD/ROW-NF exhaustiveness. |
| `TRIPLE-COVER` | **NO** if it means a connected simply-branched degree-three/\(S_3\) cover of \(\mathbf A^2\) with branch \(D_j\). This needs the whole NO-TORUS + INF + descent + Shirane chain, not “step 5 alone.” |
| `FIXED-TUPLE` | **Not resolved under the frozen literal definition.** `INT` 85–89 asks only for a transposition tuple satisfying node commutations and the infinity-cable constraint. Nonexistence of a full \(\pi_1\)-homomorphism does not imply nonexistence for that weaker necessary-condition system; the provisional `(O4)`/`72` record makes the distinction material. If the label is redefined to mean a tuple satisfying the *full* ZvK presentation, then it is NO. |
| `TRIPLE-COVER-GLOBAL-MONOGENICITY-ROW` / display (7.1) | **Vacuous only at its charged class.** If \(R_{F,S4}^{nm}\) means actual connected normal \(S_4\)-compatible cubic resolvents, the class is empty. This proves no general unit-representation theorem for binary cubics and says nothing about algebraic coefficient systems not known to define such covers. |
| `FACTORIZATION` / queued braid job | The \(S_4\)-existence decision is settled without it, so the job is **retired/not needed**. The braid factorization itself is a real uncomputed object, not a proposition “resolved NO.” |
| `FOLD-ZVK-U6` | ZVK-RESOLVENT plus the downstairs \(S_3\)-NO makes the **upstairs \(S_4\)-quotient question NO**. It does not compute the full union presentation or factorization. |
| `FOLD-EQUIVARIANT` | Its cover-existence component is likewise NO; any independent structural/equivalence computation is merely unnecessary, not refuted. |

Accordingly the row’s actual cover obstruction and the normalized triple-cover residual close, and the charged nonmonogenic resolvent cage is empty at its stated cover-theoretic scope. The blanket phrase “all resolved NO/vacuous” is not promotable for `FIXED-TUPLE` as literally frozen, for the factorization computation, or for the uncomputed parts of the fold lanes.

## 9. Residual items R1–R3 and non-transfer to `(8,4)`

**R1 (row exhaustiveness) remains.** Everything above is unconditional for curves given by the displayed ROW-NF parametrisation. The assertion that these exhaust every campaign `(6,4)` row member still consumes the provisional FOLD/ROW-SWEEP reduction. This review did not receive enough source material to promote that reduction.

**R2 (special moduli) is misstated and remains scope-critical.** The proved theorem excludes \(j=-27/4,-81/16\). At \(-81/16\), \(h\) has a repeated root and the affine singularity type degenerates. At \(-27/4\), however, the curve still has three distinct ordinary nodes; only \(r\) and the x-projection degenerate. Thus a claim that the entire *nodal* row is dead cannot discard \(-27/4\) on singularity grounds. It needs a separate projection argument or a proved equisingular-isotopy transfer. Neither is in the frozen chain. Conversely \(j=0\) is not nodal, although ROW-KILL itself survives there by the repair in §3.

**R3 is adjudicated, not left OPEN.** The correct downstairs value is \(\Pi=1\), \(c(\Pi)=4\), \(g_L=0\); `(2,1)` was an upstairs/non-descending value or a transcription. The corrected INF theorem is unaffected.

The asserted **non-transfer to `(8,4)` is unsupported and conflicts with the other frozen inputs**. `INT` 80–89 calls `(8,4)` target-equivalent to `(6,4)` and the residual one target-isomorphism class, while `ZVK` 667–679 says a downstairs NO kills both; `TC` 710 instead cites failure to transport a fixed \(B_6\) tuple to a fixed \(B_8\) tuple. If “target-equivalent” means an actual automorphism \(T\in\operatorname{Aut}(\mathbf A^2)\), then

\[
\mathbf A^2\setminus D\cong\mathbf A^2\setminus T(D)
\]

and meridian conjugacy classes are preserved. The \(S_4\)-transposition-quotient property therefore transfers regardless of degree, pencil, or braid basis. If `(8,4)` instead denotes the noninvertible fold union, its \(S_4\) question is killed by ZVK-RESOLVENT. Only if “target-equivalent” was loose numerical shorthand does transfer remain unavailable; then `(8,4)` must be typed OPEN. The frozen record must choose and document one meaning. A categorical “does not transfer” cannot be promoted.

## 10. Promotion recommendation

Promote the following corrected theorem, and no broader formulation:

> Let \(D_{b,c}\) be the explicit ROW-NF curve above, with \(c\ne0\) and \(b^3/c^2\notin\{-27/4,-81/16\}\). Then there is no surjection \(\pi_1(\mathbf C^2-D_{b,c})\twoheadrightarrow S_4\) sending curve meridians to transpositions.

Its proof must split the affine geometry into \(3A_1+A_{14}\) for \(j\ne0\) and \(D_4+A_{14}\) for \(j=0\), cite the strengthened inner-point lemma, state the infinity-product orientation convention, use \((c(\Pi),g_L)=(4,0)\), and cite **Shirane** Corollary 0.6 with the weighted branch divisor. At campaign level, mark this theorem conditional on the provisional assertion that FOLD/ROW-NF exhausts the intended row.

Do not promote: “three nodes iff \(j\notin\{-27/4,-81/16\}\)”; the six/eleven-distinct-discriminant census on that scope; the literal equality with a positive \(L_\infty\)-meridian rather than its inverse; `(2,1)` downstairs; the blanket auxiliary-OPEN table; or categorical non-transfer to `(8,4)`.

The exact frontier after this review is:

- the stated generic projection open set has no relevant \(S_4\) quotient;
- the actual affine \(S_3\) triple-cover question there is NO, and the charged \(S_4\)-compatible nonmonogenic-resolvent class is empty;
- the partial fixed-tuple and factorization computations are retired for cover existence but not mathematically answered;
- \(j=-27/4\) remains outside ROW-KILL despite still being nodal, and \(j=-81/16\) remains outside with degenerate affine type;
- `(8,4)` transfers if the frozen “target-equivalent” claim means an ambient automorphism, is killed via ZVK-RESOLVENT if it means the fold union, and otherwise stays OPEN pending a precise identification.

Final gate: **the central no-surjection theorem survives hostile review only as the corrected explicit-family theorem above; the claimed half-frontier closure does not.**

<!-- BODY-END -->
