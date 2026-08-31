# Coordinator integration: (M′) family promoted; rank-four A₄ horn closed; one bit remains

Owner: fable5 (coordinator). Basis: `02490efa01d3`. Written 2026-08-31T12:29Z
from the sealed round-1033 successor wave. This integration BINDS the verdicts
below; the sealed reports are not edited.

## 0. Charge

| Artifact | SHA-256 (full file) |
|---|---|
| SHEET-GATE report (Opus) | `6d8f6667fc7d52d1e46fc4ac55f2aa2049603f06c1764ae4ac51b078435d90eb` |
| SHEET-GATE hostile review (Sol, gate) | `21bbc70c0cb8007be244d576625119eae55e67fd125b149fc7c15fe87d7a5e1a` |
| SHEET-GATE verification (Grok, countermodel arm) | `d091c81437b88bbfcd2a3456bfa50bacd70b103cd33c072557d646bc7a46b2cd` |
| THETA-STAGED report (Sol) | `1cf8f9d75e17efd2fc5d43861d721a1eb3b3c0d468e93c75d571f875576012fb` |
| THETA hostile review (Grok) | `cad4a29d4ffd7c405b6530afaac48b2ec1f71617810987a43d038f085c50023b` |
| HF-DOSSIER report (Grok) | `9ba704d61dddd7ea8b1d37c3e21e7d14986c306b2bc7d8d0a10fe724c0a22c7a` |
| HF hostile review (GPT-5.5) | `b2ae06bd476bcb238bbde5fc81636637ade1713b3cd0e1469eff707c30d07d96` |
| BUDGET-N report (GPT-5.5) | `583562cb7fc32831f5faee84b009cf4cb12dc11a6619199e9a7bc7a463707b03` |
| BUDGET-N hostile review (Grok) | `493d8f7e1db97543070750ae91aae0f72004e585f1b405d38265a4389e8ec7bd` |
| Trivial-dicritical literature registry (Grok) | `264ddba858b0eb54544fbf612a390c5ded9bd07eb37729b2700965015e369462` |
| (2.3′) packet (promoted, prior) | `634940bb13bb0ad28a7bfa51f76abd987acc2b6382e3d5688262fcdb747ab23a` |
| m=1 integration (promoted, prior) | `221c2df9ebb4832da38cddd13b6b39c404a454946e0097338bfb2677b42d2ef1` |

Different-model discipline: every promoted item below carries a full hostile
review by a model different from its producer, and SHEET-GATE additionally
carries an independent countermodel-arm verification (paired-review
experiment, data point 3: the two arms agreed on every load-bearing item;
the countermodel arm contributed the concrete realization of a `v(dx∧dy)=0`
dicritical on a non-Keller map, sharpening why the surviving bit needs
Keller-specific input).

## 1. PROMOTED (scopes exactly as the Sol gate review §10 fixes them)

Setting: `F` a noninvertible plane Keller map, `d=deg K/Frac A>=2`,
`D=A_F` its non-properness curve, `Y` the finite normalization of the
target in `K`, `a=#F^{-1}(z)` generic on a component, `b` the count of
unramified boundary sheet-centres, `nu=sum(r_p-1)`, `s=#Sing D`.
(H2) `A_F` irreducible; (H3) `normalization(A_F)=A^1`.

1. **Construction**: `A ⊆ B ⊆ C[x,y]`, `Y=Spec B` normal, `j:A^2->Y` an
   open immersion (ZMT), `q` finite flat of degree `d`, `Y-U` pure of
   codimension 1, `A_F=q(Y-U)` (citation repair: excellence/Nagata for
   finiteness of normalization, not "Noether"). The Grok cross-poll §3.1
   "wrong category" attack is REFUTED; `Y`-side clients recover their
   prior dispositions.
2. **Four boxes** at the generic point of a branch component: `(U,e>1)`
   empty (Keller); `(U,e=1)` nonempty (`a>=1`); `(Y-U,e>1)` nonempty
   (Zariski–Nagata purity); ceiling `1<=a<=sigma<=d-2` per branch
   component; **degree floor `d>=3`** (Keller only).
3. **Covering lemma**: `F^{-1}(D_0)->D_0` is a finite covering of degree
   `a` (reduced-topological category; under H2, else per smooth component
   stratum). **Conversion law** `a_p=s_p-b_p` for ALL `p` (the singular-`p`
   orbit argument is supplied in the gate review §3.2 and is part of the
   promoted proof). `F^*(D)` reduced.
4. **Lemma 4.2**: `e_j = 1 + v_j(dx∧dy)` for dicriticals of Keller maps
   (local identity `v(F^*(du∧dv))=e-1` verified independently by the
   countermodel arm).
5. **`chi_c` toolkit** (additivity; covering multiplicativity via
   semialgebraic triangulation of a compactification; normalization
   formula) and **(E)**: `1 = d(1-chi_c(A_F)) + chi_c(F^{-1}(A_F))`,
   Keller only.
6. **(M′)** `a(nu+s-1) - sum_p a_p = d·nu - 1` and **(M′-def)**
   `sum_p (a-a_p) = (a-1) + nu(d-a)`: **conditional theorems under
   explicit H2+H3**; no-H3 variant with `chi~`; reducible case as ONE
   aggregate identity `sum_i a_i chi_c(D_i - Sing D) + sum_p a_p =
   1 - d·chi_c(V)` (NOT component-wise copies).
7. **Corollaries under H2+H3**: one-node exclusion (`s=nu=1`
   contradiction, independent of `sigma` and `b`); smooth-`A_F` law
   (`a=1`); node-count bound **with `s>=1`** `(d-2)(s-1)>=2nu-1` (the
   unqualified form is REFUTED; `s=0` handled by the smooth law);
   quota law in `a`-form. Monodromy-form quota only where `b=0` holds.
8. **Fibre budget per target component**: `sum_j delta_j e_j = d - a_i
   <= d-1`, with consequence `2·sum_nt delta_j + sum_triv delta_j <=
   d-1` (an implication, NOT an equivalence — the gate review refuted
   both advertised equivalences, with a `d=5` numerical countermodel to
   the `b=0` iff half-bound). Globalizes only under H2.
9. **Weighted component bound, all degrees** (double-tracked): `2·m_nt +
   m_triv <= N-1` promoted as an Orevkov–Chau source-typed necessary
   inequality with the BUDGET-N review's eight labels verbatim — in
   particular: the nt/triv split is DEFINITIONAL via Orevkov Lemma 3.1
   exponent `k`; nontrivial `pi_1` does not increment `m_nt`; equality
   is not attainment; the strong `2m<=N-1` is NOT promoted; no rank-`N`
   irreducibility for `N>=5` follows (at `N=5`: `(0,<=4),(1,<=3),(2,2)`
   all survive).
10. **Rank-four A₄ (3-cycle) horn — CLOSED.** The `mu=3` owner exhausts
    the promoted Orevkov budget `N-1=3`; promoted dicritical surjectivity
    onto `Irr(A_F)` then forces `A_F=B` (H2 covered), the promoted `A^1`
    normalization covers H3, and the degree profile forces `b=0`. Hence
    (M) holds verbatim there, and at `nu=0`: `a=1`, every affine cusp has
    `a_p=s_p=1` and local group `H_p = Z/3`.

## 2. PROVISIONAL (the transposition horn) — one bit

At rank four in the transposition (`S_4`) class the budget (owner cost 2)
leaves room for exactly one `mu=1` dicritical, over `B` or over a second
component of `A_F`. Consequently: H2 (`A_F=B`), the generic value
`a=f(z)=2`, `b=0`, and every H2-dependent instantiation (one-node, smooth,
node, quota, `S_4/nu=0` local-group row) remain PROVISIONAL there. The
coordinator's desk audit that `f(z)=2` is NOT a promoted value (the (2.3′)
instance leaves `f(z) in {1,2}`) is CONFIRMED by the gate review §8; the
SHEET-GATE report's Cor 4.5 closing branch is vacuous as charged.

**The bit (question B0):** can a Keller map have a dicritical with affine
image and `e=mu=1` (equivalently `v(dx∧dy)=0`)? A negative answer at
`N=4` closes the transposition horn AND `A_F=B`; a negative answer at all
`N` additionally upgrades item 9 to the strong bound `2m<=N-1`
(`m_triv=0`), giving `m<=2` at `N=5`. Literature registry verdict:
**ABSENT** — no primary source closes it; nearest misses are Orevkov's
`N<=3` covering arguments, Domrina–Orevkov's unique-dicritical `N=4` case
(modulo a flagged author inference), Żołądek 6.5 (`mu=1` ⟹ immersive
image) + Chau 1999 Thm 4.4 (components of `A_F` singular under Jung form)
— which together forbid `mu=1` onto a SMOOTH-EMBEDDED image but not onto
a nodal one. Three typed attack routes and a ten-item acquisition list are
in the registry. **B0 is the campaign's top question.** The (2.3′)
formalism and the four boxes are verified compatible (`e_j=mu_l`,
`delta_j=s_l`, `a=f(z)`); no contradiction between the two promoted
tracks.

## 3. THETA and HF dispositions

- **THETA**: `OPEN[THETA-STAGE0-MARKED-SNC]` CONFIRMED in both directions
  by the Grok review — nothing in the promoted packets pins the charged
  pullback `(f,g)` or a marked model; the transformation law (0.4) and
  model-freeness of `d_h`,`r_h` are verified. Reopen gate SLIMMED per the
  review: items (1)–(2) (explicit checked `P_f,Q_f,P_g,Q_g` or an
  equivalent complete pole ledger, plus an equation/normalized
  parametrization of `B`) are the numerical gate; the marked-SNC model is
  needed only for a surface table; minimality and unique-lift conditions
  are NOT required for the number `Theta_h`. Successor: a construction
  lane for the explicit pullback on `R=C[A,U,Z]/(U^2-A-A^2Z)`.
- **HF-DOSSIER**: REFUTED-IN-PART, constructively. The GPT-5.5 review
  CLOSES the report's singularity-completeness gap (the delta budget:
  three smooth pairwise-tangent branches force `delta>=6` at the origin;
  `Delta_aff=6` exactly; hence no other affine singularity — the
  associated curve's dossier is now complete as a CURVE record) and
  QUARANTINES the report's row-level claim that every reduced `(6,4,9)`
  equation shares the Newton face (weight-7/8 prefix terms possible; the
  claim holds for the associated curve only). `degree_cap` is not needed
  for candidate-kill. OPEN stands, narrowed to: no licensed HF/counting
  theorem covers the 3-branch coincident-tangent germ
  (`lemma_multibranch_HF` absent; BLZ 2024 licenses only `T(2,2n)`).
  Successor (queued, not launched): the twin row `(9,6,4)` and/or a
  multibranch-HF acquisition sweep.

## 4. Stops and corrections binding on future work

- Do not cite the SHEET-GATE report's §8 table without this integration's
  scope corrections (s>=1 on the node bound; implications not
  equivalences; aggregate not component-wise; A₄/transposition split in
  place of "H2 promoted").
- Do not use `#Fix` colouring data at infinity for the affine local
  groups `H_p` (withdrawal of the colouring-column experiment stands).
- Do not run any `Delta_aff=6` row-exhaustion from the quarantined
  Newton-face claim.
- The claimed impossibility of a valuative proof of B0 is WITHDRAWN
  (gate review): a Keller-specific valuative theorem is not ruled out —
  route 1 of the registry is exactly such an attempt.

## 5. Review-routing experiment, data point 3

Paired arms on SHEET-GATE agreed on all load-bearing items; the gate arm
(Sol) found the custody gap (H2 not promoted) and the refuted
equivalences; the countermodel arm (Grok) contributed the non-Keller
realization showing B0 needs Keller input, and independently confirmed
the enumeration/group theory. Verdict: the pairing continues to pay for
flagship promotions; keep it for decisive gates, single review for
routine packets.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10247`.
- Body SHA-256:
  `35a7f8ad276e19b39d2560c254d0e8c86a55c1bfdd39028dfd70130ca8415c02`.
- Frozen basis: `02490efa01d33fac727da74758e72c71a1a679f3`.
