# Coordinator integration: B0 holds through N=19 under H2; PI1-S4 answered on the coprime stratum; residual = one degree bound

Owner: fable5 (coordinator). Basis: `46dd51af`. Third binding integration of
2026-08-31; extends `69970f4d` and `bbd48de1`.

## 0. Charge

| Artifact | SHA-256 |
|---|---|
| PI1-S4 decision (Opus) | `010330d208c5899ce41832f1187b73d9a63268725d809b0370f2b4d9cd66eadd` |
| PI1-S4 hostile gate (Sol) | `a48b15e4419b088b91bbc51d579407b373d5d28ead9fbf5301da9e2f22a46a47` |
| PI1-S4 verification r2 (Grok) | `21b61cb130df42abc177899ead9929e797d6ec46e936db63a6bdc1560d0ed5b1` |
| CORR-BUDGET-N5 (Sol) | `67a9482eecd3fcb5f06bcf2967d4b73f5761429b5be597f2809b8e0767b1b02c` |
| N5 hostile review (Grok) | `ba35a89bd6aad2d4c86d5594ef49be1c63033aed5b08140c8f17e0fc0fa42a22` |
| B0-ALL-N (Sol) | `621f1356b3b5290e32c2f2bf689b4d9a49412cb852066886a34b580366cb1652` |
| B0-ALL-N hostile review (Grok) | `f865204a3fd2ee3a6944b6739ae581cf29c41a7f2259bbc54cd1587ddf397a46` |
| PI1S4-CLOSE-RESIDUAL r2 (Opus) | `b9a83b0783f4b9b844bc881739e0b3c7c63efeb8683f862e007e6584af238696` |
| B0 integration (prior) | `bbd48de1b028f6c71f006c3f27c10a3b96c593e6da58088c8393a992bde4a963` |

Custody notes. Wave-7 produced two sealed-skeleton lane failures (Grok
verification r1: provider ended turn after skeleton; Opus residual r1:
128K output-cap kill). Root cause was the prompt template sealing the
skeleton; the seal-at-completion contract is now protocol
(COORDINATION.md 17:35Z amendment). Both lanes reran clean as r2 under
the new contract. The r1 artifacts remain banked as failure evidence
and must not be cited for content.

## 1. PROMOTED

1. **PI1-S4 Main Theorem, as corrected (paired review: gate
   PROMOTE-AS-CORRECTED + verification arm all-HOLDS).** Scope: `D`
   an irreducible polynomial curve, normalization `A^1`, one place at
   infinity, coordinates normalized to `d = deg p > n = deg q >= 1`,
   `gcd(d,n) = 1`, every affine singularity a double point of two
   smooth branches (tangency allowed). Then no surjection
   `pi_1(C^2-D) ->> S_4` sends every meridian to a transposition with
   disjoint transpositions at each double point. Gate repairs bound:
   generic shear before braid factorizations; Lemma 5.5 replaced by
   local intersection-number conservation; the "one Puiseux pair"
   equivalence gloss DELETED (`(C1)` is the gcd condition, nothing
   else); Theorem A is a coprime-stratum theorem, not
   `(C1)`-independent. Sub-promotions at their own scopes: Theorem A
   (corrected; `Pi^n=1`, parity, `n>=3`, order-3/order-4 fork);
   Theorem B (nodal + coprime: `pi_1(C^2-D) = Z`); (B') as
   sufficient-only; Theorem C (as corrected). Verified small-case
   kill-list: survivors at `d<=9` under (C1)+A(3) are exactly
   `(4,3),(5,4),(7,4),(8,3),(9,4),(9,8)`.
2. **N=5 trivial-dicritical kill under H2 (review CONFIRMED).** The
   unique profile `(2,1)+(1,0)`, `(s_2,s_1,a)=(1,1,2)` is impossible.
3. **B0-ALL-N Theorem 4.1 (review CONFIRMED at written scope).**
   Under H2: NO affine-image dicritical with `mu = 1` for every
   `N <= 19`; and at EVERY degree whenever each correction-bearing
   normalization cover has degree one. Consequences promoted on that
   range: `b = 0`; `2m <= N-2`; H3 is a CONCLUSION (a trivial
   dicritical forces `l_0' ~ A^1`, `s_0 = 1`, `D~ = A^1` via the
   degree-free Orevkov Lemma 2.1). Transfer correction bound:
   jump-to-criticality is [Z-6.5b] on the composite `phi_l = eta∘h_l`;
   immersivity of `eta` pushes it to `dh_l = 0` — correction support
   equals ramification support of `h_l`; every correction carrier has
   `s_l >= 2` and `mu_l >= 2`. The N5 argument's eta-criticality
   phrasing is scope-corrected (valid at `s=1`), its conclusion
   intact.
4. **From CLOSE-RESIDUAL r2, the independently re-derived items only**
   (the rest is PROVISIONAL pending its review): none promoted yet —
   see §2.

## 2. PROVISIONAL (CLOSE-RESIDUAL r2, review pending)

The r2 lane claims, with PROVED-HERE labels: (a) residual closure for
`deg D_1 <= 4` outright; (b) the `(d,n)=(4,2)` noncoprime case killed
twice independently (a literature-free braid collapse to `S_3`, and
Nori giving `pi_1 = Z`); (c) nodal-coprime closure re-derived from
hashed Nori; (d) `(M-INF)` reduced to the single scalar inequality
`beta_h <= 2d+n-2` for the last characteristic exponent, via
`delta_aff = #(N \ S)` gap counts with `S ⊇ <d,n>`; (e) Theorem A'
(block collapse) settled NEGATIVELY where `n | d` — the outer level
never suffices there. All PROVISIONAL pending different-model review.

## 3. THE REMAINING GAPS (exact, ranked)

1. **`OPEN[PI1S4-D1-DEGREE]`** — highest leverage: no promoted datum
   bounds `deg D_1` for the N=4 reducible residual. A degree bound
   `<= 4` closes B0 at N=4 unconditionally via the (reviewed)
   residual closure; any bound plus per-`(d,n)` checks of `(M-INF)`
   also suffices for nodal cases.
2. **`OPEN[M-INF]`** — two named pieces: prove the embedded-resolution
   identity (4.2) `M_emb(C) = mult(C)+beta_h-1`, and the semigroup
   gap-count bound `beta_h <= 2d+n-2`.
3. **`OPEN[PI1S4-TANGENTIAL-NONCOPRIME]`** — the decision report's
   item (ii), unchanged.
4. **`OPEN[B0-H2-N>=20/RAMIFIED-NONPRIMITIVE-COVER]`** — first
   numerical candidate: packet `(mu,s,corr) = (1,1,0)+(2,3,16)` at
   `N=20`, `W=7`, `d=6`, `a=13`, `R=2`; necessarily `2a > N`. A floor,
   not attainment.
5. **`OPEN[B0-REDUCIBLE-N>=5/COMPONENT-INCIDENCE+RAMIFIED-COVERS]`.**
6. **`OPEN[OREVKOV-1990-CUSTODY]`** — no official PDF obtained; the
   negativity theorem remains UNVERIFIED and unconsumed.

## 4. Campaign state after this integration

Rank four (N=4): A₄ class CLOSED; transposition class closed under H2
(B0 integration); reducible residual closed for `deg D_1 <= 4`
PROVISIONALLY, riding the D_1-degree bound for full closure. All
`5 <= N <= 19`: no trivial dicritical under H2; `2m <= N-2` there.
The frontier is: the D_1 degree bound (N=4 unconditional closure),
the reducible configurations at `N >= 5`, `N >= 20` under H2, and the
one-cusp horn all-degrees induction (independent thread). Review
debt: CLOSE-RESIDUAL r2 (routed now). Systems: seal-at-completion
contract live; replay gate shipped; wave-7 r1 skeletons banked as
failure evidence.

## 5. Review-routing experiment, data point 5

The paired arms on the PI1-S4 decision split the work exactly as
designed: the gate found scope glosses and proof-setup gaps
(shear/genericity, Lemma 5.5); the computation arm certified the
enumerations and produced the survivor table. No conflict. The
wave-7 skeleton failures were a LANE-CONTRACT defect, not a review
defect, and were caught at harvest by report reading — supporting the
amendment that BODY_SEALED never substitutes for reading.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6779`.
- Body SHA-256:
  `3a752c1a7497f1cea0eefa21be648271e74a2eca60bb723ba55e844b18bf2ab8`.
- Frozen basis: `46dd51afa3bd62f8785ef7ab712a21b2ba3af9b5`.
