# WEB-SWEEP backstop — 2026-09-01 (Grok 4.6)

**Lane.** Scout / literature backstop.
**Charged input.** `xmodel/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md`
**Window.** Roughly 2026-07-01 through 2026-09-01, plus older items the campaign may have missed.
**Mode.** Registry only. No proofs. Desk-scale. No CAS. No canonical-ledger edits. No `jc2-lean` inspection.
**Threat protocol.** Any find that contradicts a promoted campaign item is tagged THREAT and listed first.

## 0. Input hash and charge digest

Frozen input rehashed this session; stop condition not triggered.

```text
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.uSW1xA/inputs/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

Matches the charge. Body of that integration is 5395 bytes with SHA-256 `130b3de6d043fa9bc82e284fddaa6c69a93c08a7dadf5b46f2d2c1282d32ed6f`.

**Promoted items this sweep must not be scooped or contradicted.**

1. THEOREM 7.B (all-degree B0 under H2): every noninvertible plane Keller map of geometric degree \(N\ge 3\) with \(A_F\) irreducible has **no** dicritical of affine image and \(\mu=1\). Consequences: \(b=0\), \(\sum\mu_l\le N-2\), \(2m\le N-2\), H3 as a conclusion. `OPEN[B0-H2-N>=20/RAMIFIED-NONPRIMITIVE-COVER]` is CLOSED.
2. THEOREM EXHAUST (as corrected): one-place curves with the reviewed-gauge row invariants lie in the explicit families after a target automorphism.
3. CAMPAIGN-PIN: no promoted \(d_{\min}\) bound (`OPEN[CAMPAIGN-PIN-D1-DMIN-BOUND]`). SHAPE-KILL is PROVISIONAL.
4. THEOREM S5-COPRIME-KILL: S2 coprime stratum and affine-normal-form \((6,4)\) slice are dead.
5. N5-S1 remains OPEN as typed.
6. HF-ATTAIN: \(k=6,7\) saturations tautological for the pin class; \((9,6,4)\) is an explicit sharpness witness not listed in BLZ 2024; pass remains `PASS_NECESSARY_ONLY`.

**Named OPENs used as bearing targets.**

- Shape residuals: `OPEN[SHAPE-2-INNER-g>=3]`, `OPEN[SHAPE-2-INFINITY-Z3]`, `OPEN[SHAPE-3-ALL-g]`, `OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]`.
- Pin: `OPEN[CAMPAIGN-PIN-D1-DMIN-BOUND]`.
- N=5: `OPEN[PI1-S5-NODAL-NONCOPRIME]`, `OPEN[N5-S2-ROW-PIN]`, `OPEN[PI1-S5-CUSP-CORRECTION]`, `OPEN[N5-S1-INF-WORD]`.
- N=4 reducible / PI1-S4 class (six AM-numerical candidate types, Box03 suite) and off-stratum `OPEN[PI1-S4]`.
- Disproof: HF \((9,6,4)\) sharpness / BLZ equality cases.

**Search boundary.** Window \(\approx\) 2026-07-01 through 2026-09-01, plus older items the campaign’s JC-only sweeps may have missed. Previous JC backstop: `xmodel/websweep-20260831T0454Z.md` (cutoff 2026-08-31T04:54Z). This lane is topic-scoped to the seven charged fronts, not a re-run of that JC census. Method: arXiv abs/PDF, GitHub heads, Zenodo/SSRN, MathOverflow/Wikipedia/MathWorld status pages. Search snippets are not evidence. PDFs streamed this session to `/tmp/jc2-websweep-20260901/` and SHA-256’d. No CAS. No canonical-ledger edits. No `jc2-lean`. This report declares no exit price.

**Status pages used for the plane-JC scoop check.** Wikipedia Jacobian conjecture (snapshot 2026-08-28), MathWorld (2026-08-28), SuperMind README, and the date-ordered arXiv “Jacobian conjecture” corpus through 2608.27341. All still state that characteristic-zero JC2 is open.

## 1. THREAT board (empty if none)

**Empty.** No fetched source exhibits a characteristic-zero plane Keller map, a \(\mu=1\) dicritical of affine image under H2, a one-place curve outside THEOREM EXHAUST, an \(S_5\) coprime survivor, or a BLZ equality case that the \((9,6,4)\) witness violates. Status pages (Wikipedia 2026-08-28, MathWorld 2026-08-28, SuperMind HEAD `8b376296`, 2026-08-05) still state that JC2 is open.

One **scoop-claim**, not a THREAT: Schenk, Zenodo 18622130 (2026-02-12), purports a complete proof of JC2 by eliminating affine dicritical ramification. If sound it would *imply* THEOREM 7.B, not contradict it. It is older than the 60-day window and is absent from campaign greps of `Schenk` / `18622130`. Registered in §§2 and 9. This lane does not audit it.

Kistner–Shaska arXiv:2608.02863 (2026-08-03) constructs graded counterexamples only in dimension 3 and records that no member of the cyclic-cone family descends to a two-variable Keller pair (Prop. 3.21). Compatible with Shaska’s dim-2 emptiness and with 7.B.

## 2. Jacobian conjecture (plane case) — announcements and preprints

Window check against the 2026-08-31T04:54Z JC backstop, plus Keller-map titles that phrase-search missed.

**F1. Kistner–Shaska, *Orbits and fields of definition for graded Keller maps*, arXiv:2608.02863v1, submitted 2026-08-03.** PDF SHA-256 `3cd7e239d8b01c79239789a97c26e466208d9cb216d9773574562c468c915a2e` (39 pp.). Classifies graded (i.e. \(\mathbb{G}_m\)-equivariant) Keller maps in the unit-positive hyperbolic sector \(w=(1,-r,-s)\). Constructs cyclic-cone families populating \(K(3,(1,-1,-1))\) at every composite generic degree \(N\ge 6\), and a diagonal family \(K(3,(1,-p,-p))\ne\emptyset\) for every \(p\ge 2\). Geometric monodromy is \(A_N\) or \(S_N\). Prop. 3.21: no cyclic-cone member descends to a two-variable Keller pair; a single coefficient is the obstruction. The paper explicitly treats JC2 as open. **Bearing: IRRELEVANT to THEOREM 7.B as a threat; STRUCTURE for the graded wall already recorded from Shaska 2607.20210.** New-to-phrase-search because the title does not contain “Jacobian conjecture”.

**F2. Gao, *Counterexamples to the Jacobian conjecture in dimensions greater than two*, arXiv:2608.00222v1, 2026-07-31.** SHA-256 `483208235e32ae69aaf83832916451707c78aa5a4410486c860950bd3eb6860f`. Tangent-sweep construction of étale non-proper self-maps of \(\mathbb{C}^n\), \(n\ge 3\), of arbitrarily large geometric degree. Explicitly does not touch the plane. **IRRELEVANT** to the plane OPENs; **STRUCTURE** only as language for non-proper étale maps.

**F3. Mondello, *A dimension-two counterexample to the separable Jacobian conjecture in characteristic two*, arXiv:2608.02634v1, 2026-07-29.** SHA-256 `b6933e8dc2238cc46aac5b96727cc01ae97ee4b178d691cf65ff175dc8d6a86e`. An explicit char-2 separable Keller map of generic degree 3 that is not injective. **IRRELEVANT** to char-0 JC2.

**F4. Shaska, *Graded Keller maps and the Jacobian Conjecture*, arXiv:2607.20210v2, 2026-07-25.** SHA-256 `66cbff919a7d8372f1ee4d53b9f887a249c53c91c9c1b79a02d3a67e7d2b06ec`. In dimension two, every graded/equivariant Keller map is an automorphism, for every weight signature. **STRUCTURE** for a special class; does not reduce arbitrary plane Keller maps to the graded class; does not contradict 7.B.

**F5. Jelonek, *On mappings with Jacobian one*, arXiv:2607.20597v1, 2026-07-22.** SHA-256 `9e593e2c6e18503b9e25af01a508912b2798545525cdfe81f7c94206e74c275a`. The bounded-degree automorphism locus inside \(\{Jac=1\}\) is Zariski closed. No plane decision. Already in the 08-26 sweep. **IRRELEVANT**.

**F6. van Dobben de Bruyn, *Divisors in projective bundles over \(\mathbb{P}^1\) whose complement is affine space*, arXiv:2608.27341v1, 2026-08-27.** SHA-256 `ad2b2f112a5c61b101758cd45f38339a69a7e3ce6343dfa81e87f784298298c6` (matches the 08-28 sweep). Affine-space recognition on ruled surfaces; appendix explains the dim-3 counterexample and shows the naive dim-2 analogue fails. **STRUCTURE** for topology-at-infinity of a hypothetical compactified plane map; not a plane proof or counterexample.

**F7. Pissolato, *On the density of polynomial mappings satisfying the Jacobian conjecture*, arXiv:2608.19069v1, 2026-08-19.** SHA-256 `c88dc004277cd82b61472d339d740cd2518806b65d4c6a544580594c8edfe751`. Dense-open generic statement; abstract leaves dim 2 open. **IRRELEVANT**.

**F8. Schenk, *A valuation-theoretic proof of the Jacobian conjecture in dimension two*, Zenodo 18622130, 2026-02-12.** File `Jacobi in N=2.pdf`. SHA-256 `6ba4088386eb40affbb4abad54bb8e1574de09d00da9d1fbeac9f5c88d160f24` (569113 bytes). Theorem 1.1 claims JC2 over any algebraically closed field of char 0. Strategy: normalize the projective graph, Stein-factor, kill horizontal boundary (U-HIT), analyze affine dicriticals by Rees degeneration, force positivity of the Jacobian two-form, contradict the Keller identity, then invoke triviality of finite étale covers of \(\mathbb{A}^2\) and Zariski’s Main Theorem. Historical paragraph still says the conjecture is open in dimension \(\ge 2\) (pre-Alpöge). **Scoop-claim of the whole plane problem, not a THREAT to 7.B.** Not audited here. Campaign greps of `Schenk` / `18622130` are empty: missed older item.

**F9. SuperMind / Strinz public heads.** SuperMind `8b376296` (2026-08-05) unchanged; Strinz `(75,125)` last commit `16ae8b263cb8` (2026-08-30) already triaged on 08-31. No JC2 resolution.

No new 2026-08-31 / 2026-09-01 arXiv JC2 claim was found.

## 3. Dicritical divisors / non-properness sets of polynomial maps

**F10. Artal Bartolo–Veys, *Dicritical divisors and hypercurvettes*, arXiv:2505.24648v1, 2026-05-30.** SHA-256 `cdbb75f81b71896bda5e361757f7eb08a03502014e857c7eb3abeb67e11056db`. Local germs of rational functions on smooth varieties of arbitrary dimension: given a blowup \(\pi\), there exists \(h\) making a prescribed subset of exceptional components dicritical of prescribed degrees, via hypercurvettes. This is the Abhyankar–Artal existence theorem in dim \(\ge 3\). It does not constrain dicriticals of a global polynomial map \(\mathbb{A}^2\to\mathbb{A}^2\), nor \(\mu=1\) affine-image dicriticals under H2. **STRUCTURE** for the dicritical vocabulary; **IRRELEVANT** to THEOREM 7.B as a close or a threat.

**F11. El Hilany, *Around the topological classification problem of polynomial maps: a survey*, arXiv:2501.03828v2, 2025-08-07.** SHA-256 `c6d4c63e7d7ab0114e80326b91983bed343a0cd66d823caf9b084fb679715082`. Survey of topological types of polynomial maps; §5 treats singularities at infinity of generically finite maps, Jelonek’s non-properness set, and dicritical coherent faces of Newton polytopes (Thm 5.5: for generic support, \(S(f)\) is the union of resultants of dicritical faces). Records the El Hilany–Tsigaridas algorithm for real planar Jelonek sets. **STRUCTURE** for \(A_F\) as a Jelonek/non-properness curve. Does not decide \(\mu=1\) under H2.

**F12. El Hilany, *The tropical non-properness set of a polynomial map*, arXiv:2207.00989v2, 2024-07-19 (DCG, to appear).** SHA-256 `37363694e8bf6a3cdd90d915a0282a08b88ff4cbd76418ca290061a5b8b083da`. Identifies \(\mathrm{Val}(S(f)\cap(\mathbb{K}^*)^n)\) with the tropical non-properness set of the tropical polynomial map (dicritical half-lines in the virtual fibre). Recovers the fan dual to the Newton polytope of the complex Jelonek set. **STRUCTURE** for Newton-fan descriptions of \(A_F\); not a \(\mu\)-statement.

**F13. Tang–Xia–Zhao, *Detecting nonproperness of likelihood equations*, arXiv:2608.01976v1, 2026-08-03.** SHA-256 `d403bd3054a081808cdd2e2b32d8a36c075531729c021e637e6f797ab8c66099`. Nonproperness of statistical likelihood systems (solutions escaping to infinity in parameter space). Keyword collision with Jelonek’s set. **IRRELEVANT**.

Gao F2 supplies explicit étale non-proper maps only for \(n\ge 3\). No post-2020 source found that produces, or forbids, a \(\mu=1\) affine-image dicritical for an irreducible-\(A_F\) plane Keller map. **No close and no threat to THEOREM 7.B.**

## 4. Fundamental groups of complements of rational plane curves; \(S_n\)-covers; Tokunaga school

**F14. Ye–Zhu, *Linearity and virtual poly-freeness of the fundamental group of plane curves of degree at most five*, arXiv:2512.08642v1, 2025-12-09.** SHA-256 `3f951a64d2eadad1eb5995f8af247b0c92b34c8b0a598ca85657647affb9378c`. Theorem 1.2: for every algebraic plane curve \(C\subset\mathbb{CP}^2\) of degree \(\le 5\), \(\pi_1(\mathbb{CP}^2\setminus C)\) is linear and virtually polyfree, hence residually finite. Degree \(\le 3\) is classical; degree 4 uses Nori and Cogolludo–Elduque [CAE25] to list the possible groups (abelian, finite, \(B_3(S^2)\), \(F_3\), \(B_3\), \(\mathbb{Z}*\mathbb{Z}/2\), \(F_2\rtimes\mathbb{Z}\)); degree 5 reviews Degtyarev’s presentations and checks virtual polyfreeness. **STRUCTURE / PARTIAL** for `OPEN[PI1-S5-NODAL-NONCOPRIME]` and `OPEN[PI1-S5-CUSP-CORRECTION]`: any residual \(S_5\) image is a linear group, but the paper does not decide existence of a meridian-to-transposition surjection \(\pi_1(\mathbb{A}^2\setminus D)\twoheadrightarrow S_5\) with the charged local types. It does not kill S1/S2.

**F15. Cogolludo–Elduque, *The fundamental group of the complement of a generic fiber-type curve*, arXiv:2507.15814v1, 2025-07-21.** SHA-256 `f637826ff0f0040639ea2360163cfacc7c276e17b1c91834b8bf39fcbedd4958`. Main Theorem: for a component-free pencil \(F:\mathbb{P}^2\dashrightarrow\mathbb{P}^1\) as in their Condition 1.4 and \(B\subset\mathbb{P}^1\setminus B_F\) finite of cardinality \(s\), \(\pi_1(\mathbb{P}^2\setminus C_B)\cong G(sp;sq;kq)\) (Oka groups). Avoids braid monodromy. Cor. 1.9: an irreducible generic fibre of a pencil of degree \(d\) with at most one multiple fibre has \(\pi_1\cong\mathbb{Z}_d\). **STRUCTURE** for fibre-type (pencil) curves. Residual one-place polynomial curves in the Box03 / S5 cage are not generic fibre-type, so this does not close PI1-S4/S5.

**F16. Cogolludo–Elduque, *Geometric realizability of epimorphisms to curve orbifold groups*, arXiv:2507.10508v2, 2025-10-29.** SHA-256 `361d6247ba61eed880b6d03facfc1bb48cd5fee4ea500a59fcd1d026a1ac96c2`. Converse to “a holomorphic map to a curve induces an orbifold-group quotient”: if \(\chi^{\mathrm{orb}}(G)<0\), a finitely generated normal \(K\) with \(\pi_1(U)/K\cong G\) is realized by a unique surjective holomorphic map \(U\to C\). Applied to Serre’s question of which curve-orbifold groups arise as \(\pi_1(\mathbb{P}^2\setminus C)\). **STRUCTURE** for orbifold quotients; does not produce or forbid an \(S_n\)-cover branched at a one-place rational curve.

**F17. Cogolludo–Elduque, *Homotopy type of complements of fiber-type curves*, arXiv:2507.16374v1, 2025-07-22.** SHA-256 `94c504e05c538ee962103d7d53e129b894288cebdc3aa7653ab5b71f8f5496c3`. Homotopy type of fibre-type complements; partial positive answer to Libgober’s question (homotopy type determined by \(\pi_1\) and Euler characteristic) for free products of cyclic groups. **IRRELEVANT** to the charged \(S_n\) residuals.

**F18. Cogolludo–Măcinic, *On modular inequalities for plane projective curves*, arXiv:2605.26237v1, 2026-05-25.** SHA-256 `ced7d10252ff1715bf0e740444d02cf8e01066292c8f46eee4c66626a03c0f2d`. Modular inequalities for Alexander / twisted Alexander polynomials of plane curves via a combinatorial Aomoto complex; applied to quasi fibre-type curves. Controls cyclic covers of \(\mathbb{P}^2\setminus C\), not \(S_n\)-covers with transposition meridians. **STRUCTURE** for Alexander modules; **IRRELEVANT** to PI1-S4/S5 as currently typed.

**F19. Bannai–Tokunaga, *Examples of strong Ziegler pairs of conic-line arrangements of degree 7 and 8*, arXiv:2509.08403v1, 2025-09-10.** SHA-256 `d2db584c871ddfdbc27aa377ec603b0d761397f782fad55e24eb7d4ebe9a67b3`. Some Zariski pairs of CL arrangements are strong Ziegler pairs (non-isomorphic Milnor algebras). **IRRELEVANT** to \(S_n\)-covers of one-place rational curves.

**F20. Shirane, *A note on combinatorial type and splitting invariants of plane curves*, arXiv:2409.07915v2, 2026-04-24.** SHA-256 `025c058a07cca29858725815218ba49c0405344bbd5a0ad7b36d84e33d0d9566`. \(G\)-combinatorial type from Hironaka’s modified plumbing graph; splitting invariants of a plane curve under a Galois cover branched along another curve. Distinguishes embedded topology among curves with the same \(\pi_1\). **STRUCTURE** for splitting numbers of \(S_n\)-covers, not an existence/nonexistence theorem for the charged tuples.

No 2025–2026 Tokunaga-school paper supplies an \(S_3\)/\(S_4\)/\(S_5\) existence criterion for a one-place polynomial curve of the residual types. The 2026-08-31 lit-targeted report’s IT09/Sh12 torus-type criteria remain the strongest projective \(S_3\) input; they were not improved in this window.

## 5. Triple/quintic covers of surfaces; Tschirnhausen splittings

Target residual: `OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]` — does the \(S_3\)-resolvent triple cover of \(\mathbb{P}^2\) attached to a residual \(D\) have split Tschirnhausen bundle \(E=\mathcal{O}(k)\oplus\mathcal{O}(2k)\)? If yes, \(6\mid d\).

**F21. Ciliberto–Miranda, *Non-cyclic triple planes with branch curve of degree at most 10*, arXiv:2512.07965v1, 2025-12-08.** SHA-256 `e935f9e7286f57ac50aa6e955854e9aa43fa7e26d35405f21dcac5ef95531c6b` (matches the 2026-08-31 lit-targeted hash). Classifies *normal non-cyclic* triple covers \(\pi:X\to\mathbb{P}^2\) with \(\deg B\le 10\). Tschirnhausen bundle \(E\) is defined in §1.1 (\(\pi_*\mathcal{O}_X=\mathcal{O}\oplus E^\vee\)). Degree of \(B\) is even, \(d=2h\), \(h\ge 2\). Degree 6: the cover is the projection of a normal cubic surface in \(\mathbb{P}^3\) from an external point (or the 9-cuspidal exceptional example, Tschirnhausen \(\Omega^1_{\mathbb{P}^2}\)); if \(X\) is smooth the branch is a six-cuspidal irreducible sextic, or two cubics of contact 3. Degree 8: \(q=1\) is excluded (Prop. 24); \(q=0\) is rational and classified (Prop. 31). Degree 10: projections of quartic K3s plus four rational cases; one \(p_g=0,q=1\) slot left open. Completeness fails only at that slot. **PARTIAL** for the *projective* existence of a non-cyclic triple plane of even branch degree \(\le 10\): the classified Tschirnhausen types at degree 6 are the split \(\mathcal{O}(-1)\oplus\mathcal{O}(-2)\) (cubic-surface projection) or \(\Omega^1_{\mathbb{P}^2}\) (exceptional). This does **not** prove that every \(S_3\)-resolvent attached to a residual affine \(D\) has split Tschirnhausen, nor that \(6\mid d\) in general (Horrocks: rank-two bundles on \(\mathbb{P}^2\) need not split). Affine ramification along \(L_\infty\) remains the compactification gap already recorded in lit-targeted. Does not close family-3’s non-constant stratum (SK-5: no projective \(S_3\) cover).

**F22. Choi–Iliev–Kim, *On the Tschirnhausen module of coverings of curves on decomposable ruled surfaces*, arXiv:2507.11304v1, 2025-07-15.** SHA-256 `e2b5d8497256eae38faf87891ae37a051773cf58d752f352bda63110fba192cd`. For \(m\)-secant curves on \(S=\mathbb{P}(\mathcal{O}_Y\oplus\mathcal{O}_Y(E))\), the Tschirnhausen module of \(\varphi:X\to Y\) splits completely as \(\bigoplus_{i=1}^{m-1}\mathcal{O}_Y(-iE)\) (or with an extra \(-q\)). Geometric setting is a curve cover of a curve, not a triple cover of \(\mathbb{P}^2\). **STRUCTURE** for the splitting phenomenon on decomposable ruled surfaces; **IRRELEVANT** as a close of the charged OPEN.

No 2025–2026 source was found that forces splitting of the Tschirnhausen bundle of an \(S_3\)-resolvent of a residual plane curve, nor a quintic-cover analogue that would close `OPEN[N5-S2-ROW-PIN]`. **OPEN stands.**

## 6. Numerical semigroups of one-place curves; realization theorems

Target: realization of the six AM-numerical candidate types (Box03 suite) as one-place polynomial curves, and any theorem that would bound or exhaust \(\delta\)-sequences.

No 2025–2026 primary source was found that proves a new realization theorem for numerical semigroups of plane curves with one place at infinity, or that classifies which \(\delta\)-sequences arise from polynomial maps of a given degree. The classical chain remains: Abhyankar–Moh (semigroup at infinity is free with \(n_ia_i>a_{i+1}\)); Pinkham (every such semigroup is realized by some projective plane curve with one place at infinity); Bresinsky–Teissier for local plane branches (the opposite inequality). Assi–García-Sánchez arXiv:1407.0490 (2014) still supplies the constructive \(\delta\)-sequence census and the GAP implementation; Almirón’s 2024 survey arXiv:2411.19260 reviews the same theorems without a new realization result. Montgomery arXiv:2403.00588 (honest embedding dimension) treats space curves, not the plane one-place problem.

Álvarez–Moreno-Ávila–Ojeda, *On the smallest numerical semigroups closed under affine maps*, arXiv:2607.03258 (2026-07-07), is a combinatorial affine-orbit construction of numerical semigroups; it does not discuss plane curves or places at infinity. **IRRELEVANT**.

**No close, partial, or threat to EXHAUST or to the six AM-numerical types.** Realization of the residual rows remains a campaign lemma.

## 7. Heegaard–Floer bounds for plane curves (BLZ-adjacent)

**F23. Borodzik–Liu–Zemke, *Heegaard Floer homology, knotifications of links, and plane curves with noncuspidal singularities*, arXiv:2104.13709v2; Algebr. Geom. Topol. 24 (2024) 4837–4889.** SHA-256 of the arXiv v2 PDF fetched this session: `ac64acd8f728bc9c920f4063fb6e9699ee13d79cb7fd586b11bc31a9edf84803` (matches the HF-ATTAIN charged hash). This is the licensed source of Theorem 6.4 used for the \((9,6,4)\) witness. No 2025 or 2026 successor paper was found that sharpens the equality cases of Thm 6.4, lists additional saturating semigroups, or treats mixed nodal/\(A_3\) configurations beyond BLZ. Zemke’s 2025–2026 papers (lattice=HF, graph TQFT, surgery formula) do not return to plane algebraic curves.

**Bearing on HF-ATTAIN / \((9,6,4)\):** **IRRELEVANT as news.** The candidate remains an explicit sharpness witness not listed in BLZ 2024. No threat to `PASS_NECESSARY_ONLY`. The next necessary layer remains `OPEN[PI1S4-NONCOPRIME]` as typed in HF-ATTAIN, not a new Floer inequality.

## 8. Certified braid monodromy / SIROCCO

**F24. SIROCCO2 upstream.** GitHub `miguelmarco/SIROCCO2`, latest release **2.1.1** (commit `2195fccda542`, 2025-08-11, pkg-config). Previous release 2.1.0 (2021-06-30) added per-factor tracking. **No 2026 commit.** Sage optional SPKG remains 2.1.1, as already recorded in `braid-prep-row64`. Practical status unchanged: Interval-Newton certified tubes, known to compute \(\pi_1\) of degree-7 CL arrangements.

**F25. Bannai–Tokunaga–Yorisaki, *The realization spaces of certain conic-line arrangements of degree 7*, arXiv:2409.05011v1, 2024-09-08.** SHA-256 `edfd615855437462d971cafc1126eea179ce901add5b8e88f998db1e0420612a`. Appendix computes fundamental groups of the degree-7 CL arrangements **using SageMath and the package SIROCCO**. This is the most recent published computation at a scale comparable to a degree-6/7 residual sextic. **STRUCTURE** for SIROCCO’s published range; does not certify the campaign’s queued \((6,4)\) braid job.

**F26. Duff–Lee, *Certifying Galois/monodromy actions via homotopy graphs*, arXiv:2603.17288v1, 2026-03-18.** SHA-256 `4f937867081e56524a3faa97f745318a985526031ca70303d4fa94c741680b52`. Certified path-tracking (interval arithmetic) for Galois/monodromy groups of *parametrized polynomial systems*, assembled on a homotopy graph in parameter space. Different problem from Zariski–van Kampen braid monodromy of a plane curve. **STRUCTURE** as an alternative certification style; not a SIROCCO replacement for affine plane curves.

No 2026 SIROCCO limitation note, no Bettini–Marco successor, and no published certified braid word for a \(3A_1+A_{14}\) sextic (or for the \((9,6,4)\) candidate) was found. The AWS-gated SIROCCO job remains the campaign’s computational path.

## 9. Older items the campaign may have missed

These sit outside the 60-day window, or were missed by JC-phrase sweeps.

| item | why missed | bearing |
|---|---|---|
| Schenk Zenodo 18622130 (2026-02-12), F8 | not on arXiv; campaign greps empty | scoop-claim of JC2; audit queued, not a THREAT |
| Ciliberto–Miranda 2512.07965 (2025-12) | ingested in lit-targeted 08-31, not in JC backstops | PARTIAL for projective triple planes \(\deg B\le 10\) |
| Ye–Zhu 2512.08642 (2025-12) | JC-phrase sweeps | STRUCTURE for \(\pi_1\) of degree \(\le 5\) |
| Cogolludo–Elduque 2507.15814 / 2507.10508 / 2507.16374 (2025-07) | fibre-type, not JC | STRUCTURE for Oka groups / orbifold realizability |
| Cogolludo–Măcinic 2605.26237 (2026-05-25) | Alexander polynomials | STRUCTURE, not \(S_n\) |
| Choi–Iliev–Kim 2507.11304 (2025-07) | ruled-surface Tschirnhausen | STRUCTURE, wrong geometry |
| Artal–Veys 2505.24648 (2025-05) | local dicriticals, all dimensions | STRUCTURE |
| El Hilany survey 2501.03828 + tropical 2207.00989v2 | classification survey | STRUCTURE for Jelonek/\(A_F\) |
| Bannai–Tokunaga 2509.08403; Bannai–Tokunaga–Yorisaki 2409.05011 | CL arrangements | SIROCCO published range; Ziegler pairs IRRELEVANT |
| Shirane 2409.07915v2 (2026-04-24) | splitting invariants | STRUCTURE |
| Duff–Lee 2603.17288 (2026-03) | certified monodromy of parametrized systems | STRUCTURE |
| Kistner–Shaska 2608.02863 (2026-08-03) | title omits “Jacobian conjecture” | STRUCTURE, dim 3 only |
| Matysiak SSRN 7229358/7229458 | already audited unsound 2026-08-28 | not reopened; no new version found |

Not re-audited: Matysiak remains unsound at D1/E1. Schenk is the one new (to the campaign) purported JC2 proof.

## 10. Bearing table (OPEN × find)

| OPEN / promoted | find | tag |
|---|---|---|
| THEOREM 7.B (no \(\mu=1\) affine-image dicritical, H2) | F1–F9, F10–F12, F8 | no THREAT; F8 is a scoop-claim of the whole plane problem |
| THEOREM EXHAUST / six AM-numerical types | §6 empty of new realization theorems | IRRELEVANT as news |
| `OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]` | F21 PARTIAL (projective, \(\deg B\le 10\)); F22 wrong geometry | stands OPEN |
| `OPEN[SHAPE-2-INNER-g>=3]`, `OPEN[SHAPE-2-INFINITY-Z3]`, `OPEN[SHAPE-3-ALL-g]` | no Tokunaga/Cardano criterion upgrade | stands OPEN |
| `OPEN[CAMPAIGN-PIN-D1-DMIN-BOUND]` | none | stands OPEN |
| `OPEN[PI1-S5-NODAL-NONCOPRIME]`, `OPEN[PI1-S5-CUSP-CORRECTION]`, `OPEN[N5-S1-INF-WORD]`, `OPEN[N5-S2-ROW-PIN]` | F14 linearity of all deg-\(\le 5\) groups; F15 fibre-type Oka groups | STRUCTURE, not a kill |
| `OPEN[PI1-S4]` class / Box03 | F15–F20 do not decide transposition tuples on one-place curves | stands OPEN |
| HF-ATTAIN \((9,6,4)\) | F23 no equality-case successor | IRRELEVANT as news |
| SIROCCO job | F24 no 2026 update; F25 published deg-7 CL; F26 different problem | STRUCTURE |

## 11. Sources fetched (URL, retrieval date, PDF SHA-256)

All PDFs streamed 2026-08-31 to `/tmp/jc2-websweep-20260901/`. SHA-256 of the bytes.

| id | URL | SHA-256 |
|---|---|---|
| 2608.02863 | https://arxiv.org/pdf/2608.02863 | `3cd7e239d8b01c79239789a97c26e466208d9cb216d9773574562c468c915a2e` |
| 2608.00222 | https://arxiv.org/pdf/2608.00222 | `483208235e32ae69aaf83832916451707c78aa5a4410486c860950bd3eb6860f` |
| 2608.02634 | https://arxiv.org/pdf/2608.02634 | `b6933e8dc2238cc46aac5b96727cc01ae97ee4b178d691cf65ff175dc8d6a86e` |
| 2607.20210 | https://arxiv.org/pdf/2607.20210 | `66cbff919a7d8372f1ee4d53b9f887a249c53c91c9c1b79a02d3a67e7d2b06ec` |
| 2607.20597 | https://arxiv.org/pdf/2607.20597 | `9e593e2c6e18503b9e25af01a508912b2798545525cdfe81f7c94206e74c275a` |
| 2608.27341 | https://arxiv.org/pdf/2608.27341 | `ad2b2f112a5c61b101758cd45f38339a69a7e3ce6343dfa81e87f784298298c6` |
| 2608.19069 | https://arxiv.org/pdf/2608.19069 | `c88dc004277cd82b61472d339d740cd2518806b65d4c6a544580594c8edfe751` |
| 2608.01976 | https://arxiv.org/pdf/2608.01976 | `d403bd3054a081808cdd2e2b32d8a36c075531729c021e637e6f797ab8c66099` |
| 2607.21572 | https://arxiv.org/pdf/2607.21572 | `253c1dbb8d1406f718b4e871fe5de68460274edfe4c4bb6588d2eaab01a57cde` |
| 2607.20968 | https://arxiv.org/pdf/2607.20968 | `32b6821f24631f2fdbdfffd29eaad9dbf1f8524fb6d70f48b76ef938fa75e3d4` |
| 2607.22198 | https://arxiv.org/pdf/2607.22198 | `090c1735997c598f14741fb8083666b3043cf62bc59da303494166bb5e9c18f5` |
| 2505.24648 | https://arxiv.org/pdf/2505.24648 | `cdbb75f81b71896bda5e361757f7eb08a03502014e857c7eb3abeb67e11056db` |
| 2501.03828 | https://arxiv.org/pdf/2501.03828 | `c6d4c63e7d7ab0114e80326b91983bed343a0cd66d823caf9b084fb679715082` |
| 2207.00989 | https://arxiv.org/pdf/2207.00989 | `37363694e8bf6a3cdd90d915a0282a08b88ff4cbd76418ca290061a5b8b083da` |
| 2512.08642 | https://arxiv.org/pdf/2512.08642 | `3f951a64d2eadad1eb5995f8af247b0c92b34c8b0a598ca85657647affb9378c` |
| 2512.07965 | https://arxiv.org/pdf/2512.07965 | `e935f9e7286f57ac50aa6e955854e9aa43fa7e26d35405f21dcac5ef95531c6b` |
| 2507.11304 | https://arxiv.org/pdf/2507.11304 | `e2b5d8497256eae38faf87891ae37a051773cf58d752f352bda63110fba192cd` |
| 2507.15814 | https://arxiv.org/pdf/2507.15814 | `f637826ff0f0040639ea2360163cfacc7c276e17b1c91834b8bf39fcbedd4958` |
| 2507.10508 | https://arxiv.org/pdf/2507.10508 | `361d6247ba61eed880b6d03facfc1bb48cd5fee4ea500a59fcd1d026a1ac96c2` |
| 2507.16374 | https://arxiv.org/pdf/2507.16374 | `94c504e05c538ee962103d7d53e129b894288cebdc3aa7653ab5b71f8f5496c3` |
| 2605.26237 | https://arxiv.org/pdf/2605.26237 | `ced7d10252ff1715bf0e740444d02cf8e01066292c8f46eee4c66626a03c0f2d` |
| 2509.08403 | https://arxiv.org/pdf/2509.08403 | `d2db584c871ddfdbc27aa377ec603b0d761397f782fad55e24eb7d4ebe9a67b3` |
| 2409.05011 | https://arxiv.org/pdf/2409.05011 | `edfd615855437462d971cafc1126eea179ce901add5b8e88f998db1e0420612a` |
| 2409.07915 | https://arxiv.org/pdf/2409.07915 | `025c058a07cca29858725815218ba49c0405344bbd5a0ad7b36d84e33d0d9566` |
| 2104.13709 | https://arxiv.org/pdf/2104.13709 | `ac64acd8f728bc9c920f4063fb6e9699ee13d79cb7fd586b11bc31a9edf84803` |
| 2603.17288 | https://arxiv.org/pdf/2603.17288 | `4f937867081e56524a3faa97f745318a985526031ca70303d4fa94c741680b52` |
| Schenk | https://zenodo.org/records/18622130/files/Jacobi%20in%20N=2.pdf | `6ba4088386eb40affbb4abad54bb8e1574de09d00da9d1fbeac9f5c88d160f24` |

GitHub HEADs (no PDF): SuperMind `8b376296bb8f` (2026-08-05); Strinz 75-125 `16ae8b263cb8` (2026-08-30); SIROCCO2 `2195fccda542` / tag 2.1.1 (2025-08-11).

## 12. Negative searches and coverage gaps

Negative (no hit in the charged window, or hits off-scope):

- Characteristic-zero plane Keller counterexample; valid JC2 proof on arXiv after 2026-07-01.
- New \(\mu=1\) affine-image dicritical theorem, or a counterexample to THEOREM 7.B.
- Tokunaga/Shirane/IT09-style existence criterion for \(S_3\)/\(S_4\)/\(S_5\) covers of a one-place polynomial curve (as opposed to CL arrangements or fibre-type pencils).
- Quintic-cover classification of \(\mathbb{P}^2\) that would close `OPEN[N5-S2-ROW-PIN]`.
- Tschirnhausen-splitting theorem for \(S_3\)-resolvents of residual affine curves (F21 is projective and degree-bounded).
- Realization theorem for the six AM-numerical types, or a 2025–2026 \(\delta\)-sequence classification.
- BLZ equality-case successor listing \((9,6,4)\) or forbidding it.
- SIROCCO 2026 release; published certified braid word for a \(3A_1+A_{14}\) sextic.
- New Matysiak version or repair.

Coverage gaps, honestly typed:

- Private/seminar notes and non-indexed preprints are invisible. Schenk itself shows that Zenodo-only JC2 claims can evade arXiv phrase search.
- arXiv API `all:"Jacobian conjecture"` was flaky this session; the census used abs pages, HTML, and direct ID fetches. A paper whose title and abstract avoid both “Jacobian conjecture” and “Keller” could still be missed (Kistner–Shaska was caught only via a graded-Keller query).
- Casnati–Ekedahl 1996 and several Tokunaga journal PDFs remain as previously SOURCE-OPEN (no new open PDF).
- Schenk is registered, not audited. A hostile gate of F8 is the only external item that could, if sound, retire the campaign.
- This lane did not inspect `jc2-lean` or edit canonical ledgers.

## 13. Verdict for the coordinator

Characteristic-zero JC2 remains externally open. Nothing in the 60-day window, and nothing older that this topic-scoped pass recovered, contradicts a promoted item. **THREAT board empty.**

Highest-value external object is **Schenk Zenodo 18622130** (F8): a February 2026 purported valuation-theoretic proof of JC2 that the campaign has never grepped. It is a scoop-claim of the whole plane problem, not a contradiction of 7.B. Route a hostile primary-text audit (dicritical/Rees/wedge-strictness steps) before any theorem is withdrawn or any lane is stopped.

Second: **Ciliberto–Miranda 2512.07965** remains the strongest literature adjacent to `OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]`. It classifies projective non-cyclic triple planes of branch degree \(\le 10\) but does not force Tschirnhausen splitting for residual affine \(S_3\)-resolvents. The OPEN stands.

Third: **Ye–Zhu 2512.08642** puts every degree-\(\le 5\) plane-curve fundamental group in a linear, virtually polyfree list. Useful as a group-theoretic envelope for the N=5 residuals; it does not decide the charged \(S_5\) ramification types.

No literature close of the six AM-numerical types, of the shape residuals, of PI1-S4 off-stratum, or of the HF \((9,6,4)\) next layer. SIROCCO is frozen at 2.1.1 (2025-08-11). SuperMind and Strinz heads are unchanged since the 08-31 JC backstop.

**Coordinator action.** Do not withdraw 7.B, EXHAUST, S5-COPRIME-KILL, or HF-ATTAIN. Queue F8 for audit. Do not promote a Tschirnhausen split from F21. No rerank of the residual cage.

<!-- BODY-END -->
