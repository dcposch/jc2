# Coordinator integration: Theorem N-A promoted; residual cage swept to one explicit curve class + six numerical types

Owner: fable5 (coordinator). Basis: `8196c87a`. Fourth binding integration of
2026-08-31; extends `69970f4d`, `bbd48de1`, `bafe5e89`.

## 0. Charge

| Artifact | SHA-256 |
|---|---|
| NORI-BC report (Opus) | `64bcabd1e14d69026cc86e101ff266a92009c7f15e9dfc00dce88fb607e7560f` |
| NORI-BC hostile gate (Sol) | `90d2a3e81bb61d0238676e3a764683e951ab3f6ebfe78e5c2f41d469efcbaa60` |
| NORI-BC verification arm (Grok) | `d4fd1530636ebef3f7ba00b1ba8b58cd6cc5f4923c26177c7591d9dede8290c8` |
| M-INF report (Grok) | `084346b52b0d67e1d147ec839aa1e75a2bfe816aa4b39d7ff58b8905c3745450` |
| M-INF hostile review (Sol) | `8b9fe37f142afeb204d356d49dbb3bf535e59ff14a460851486b586b8ec5022a` |
| D1-DEGREE report (Sol) | `0549dfafe339d20c67fe0d64a0bc713c1e64850013fbaab9f07f654c7fbf8fc2` |
| D1-DEGREE hostile review (GPT-5.5) | `028b1c03489791f8cd674cc371c8b43c8994784aa65a05c8cfbb6dae269d3129` |
| ROW-SWEEP report (Sol) | `aa873151fca957516e4a2ffe94d79733659307a038d252b2a50d94bcd4f1a9eb` |
| Residual-r2 review (prior, Sol) | `aa41551f14f34bdae34d9f172be253882f67c8cc3c6cc699ed98b5b85bbc60f0` |
| N≤19 integration (prior) | `bafe5e8929a77aa306e76ebdee1b300bbaf579a685f793cd8684ad861f041270` |

## 1. PROMOTED

1. **Theorem N-A (paired review: gate CONFIRMED-AS-CORRECTED +
   verification all-HOLDS on numerics and both countermodels).** For
   `X` smooth projective over `C`, reduced curves `D, E` with every
   singular point of `D` a double point of two smooth branches
   (contact `k_p >= 1`), `D ∪ E` normal-crossing along `D − Sing D`,
   `E ∩ Sing D = ∅`, common components removed: if every irreducible
   `C ⊆ D` has `C² > 2r₁(C) + 4T(C) + T_x(C)`, then
   `ker(π₁(X−(D∪E)) → π₁(X−E))` is finitely generated abelian with
   finite-index centralizer. The `T_x` coefficient is SHARP (two
   bitangent conics: fail by one unit, conclusion false,
   `π₁ = Z * Z/2` independently sourced). Sub-promotions: Lemma 3.1
   as corrected (`s(A_{2k−1}) = 4k`; separate `k=1` clause), Lemma
   3.2 (blow-up invariance of the kernel), the normal-sheaf reading
   of Nori's hypothesis. REFUTED and binding: the naive `B(C)>0`
   extension (Zariski sextic `B=36>0`, `π₁=Z/2*Z/3`; and the
   smooth-branch componentwise version via the conics); the local
   Fact-1.4 transversality replacement; the 3.26 substitution;
   unqualified δ-constant π₁-transport. Errata ledger: Nori's Remark
   6.6 `s(node)` misprint CONFIRMED (correct value 4); the charged
   report's factor-2 "erratum" in Def 3.25 is REVERSED — Nori's
   printed text is correct; only the earlier gloss is corrected.
2. **Corollary N-A-RES, promoted as a package with the
   terminal-center Lemma 4.3** (independently proved in the gate
   review §6): for the residual `D_1` (irreducible polynomial curve,
   all singularities double points of smooth branches), the gate
   `M_∞ + 2T <= 3d−3` implies `π₁(C²−D_1) = Z`, answering the
   residual NO. At `T=0` this is verbatim (M-INF).
3. **M-INF split (review verdicts).** Piece 1 PROMOTED-AS-CORRECTED:
   `M_emb = mult + β_h − 1` for every plane branch (with the
   Euclidean-induction repair); hence (M-INF) ⟺ `β_h ≤ 2d+n−2`.
   Piece 2 REFUTED as a general theorem: banked counterexample — the
   polynomial curve of type (6,4) with `S_aff = <3,4>`, `β_h = 15`,
   `M_emb = 16 > 15` (an ordinary TRIPLE point; out of the residual
   class). Row statuses bound: (4,2), (6,2), (6,3) nodal closed
   ((6,2) closed entirely by N-A-RES per the verification arm);
   (6,4) nodal was returned OPEN and is now superseded by the sweep
   (§2).
4. **D1-DEGREE (review: promote at typed scope).** If the residual
   class is nonempty, `deg D_1` is unbounded under target
   automorphisms; the meaningful target is
   `d_min = min_{T∈Aut(A²)} deg T(D_1)`. Every escaping residual
   satisfies `g = gcd(d,n) >= 2`, reduced shape `(u,1)`, `(odd u,2)`,
   or `(4,3)`, `d = 2g_L + c(Π) + 2`, and
   `g <= gcd(deg P, deg Q) − 2`. Chau-filtered noncoprime list
   through `d<=9`: `(4,2);(6,2),(6,3),(6,4);(8,2),(8,4),(8,6);
   (9,3),(9,6)`. Coprime intermediate survivors reduce to `(4,3)`.

## 2. ROW-SWEEP results (PROVISIONAL pending different-model review, routed now)

Battery over the surviving rows; four of eight KILLED:

| row | verdict | residue / gate |
|---|---|---|
| (6,3)-(7,4) | KILLED | triangular target reduction to coprime (5,3) + promoted coprime no-S₄ theorem (unconditional, no (M-INF-T)) |
| (6,3)-(8,3) | KILLED | same, to coprime (4,3) |
| (8,2) nodal | KILLED | every admissible type has `M_∞ ≤ 18 < 21` — (M-INF) |
| (9,3) nodal | KILLED | every admissible type has `M_∞ ≤ 21 < 24` — (M-INF) |
| (6,4) nodal | OPEN | sole survivor `Δ=(6,4,3)`, `β₁=15`, `(δ_∞,δ_aff,M_∞)=(7,3,16)`; attained by an explicit three-node curve; missing: noncoprime fixed-tuple theorem |
| (8,4) nodal | OPEN | sole survivor `(4;10,19)`, `(18,3,22)`; target-equivalent to the (6,4) survivor — same gap |
| (8,6) nodal | OPEN | four numerical types; nodal attainment unresolved |
| (9,6) nodal | OPEN | two numerical types; nodal attainment unresolved |

**The N=4 residual topological core is now ONE target-isomorphism
class** — the explicit three-node (6,4) curve — with the single
missing lemma `OPEN[PI1S4-(6,4)-FIXED-TUPLE]`: does an S₄
transposition tuple with node-commutation constraints exist fixed by
the (6,4)-cable braid at infinity? (The (4,2) analogue collapsed to
S₃, promoted.) Plus six AM-numerical types at (8,6)/(9,6) whose
in-class nodal attainment is itself unproved
(`OPEN[ROW-(8,6)/(9,6)-NODAL-REALIZATION]`).

## 3. Stops and corrections binding on future work

- Use `4T` (not `2T`) as the tangential charge until
  OPEN[NORI-BC-SELF-TANGENT-COEFF] (the rational 5-tacnode sextic
  test object) is settled; existence UNTESTABLE-AT-DESK so far.
- Do not cite the charged NORI-BC report's factor-2 Nori erratum;
  the gate reversed it.
- The (6,4) β_h=15 counterexample curve is OUT of the residual class
  (triple point); it kills only the general β_h bound.
- Raw-degree phrasings of residual payoffs are barred; use `d_min`.
- ROW-SWEEP kills are PROVISIONAL until its review lands; the two
  degree-six tangential kills consume only promoted items and the
  coprime theorem, the two (M-INF) kills consume the corrected
  cluster identity + reviewed Nori implication.

## 4. Review-routing note (data point 6)

The N-A paired arms again split correctly: the gate caught a reversed
erratum and scope repairs; the verification arm certified all
numerics, both countermodels (with an independently hashed source for
the conics π₁), and extended the N-A-RES gate tables to (6,2)
(closing that row entirely). Pairing retained for flagship items.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6902`.
- Body SHA-256:
  `0916c0f541f8d7e4b59ca8a5e1cdcff5d6b187c0d3a7f09e8798af13e00b39f7`.
- Frozen basis: `8196c87a87dfb9cd64d74b42672dcb4ff214b00d`.
