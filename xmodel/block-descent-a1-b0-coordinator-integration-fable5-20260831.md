# Coordinator integration: B0 closed at N=4 under H2; residual is the S₄-representation question on polynomial curves

Owner: fable5 (coordinator). Basis: `830b9f09`. Sealed round-1033 successor
wave 2. This integration BINDS the verdicts below; sealed reports are not
edited. Supersedes nothing; extends integration `69970f4d`.

## 0. Charge

| Artifact | SHA-256 (full file) |
|---|---|
| B0 proof report (Opus) | `b37ec3bfd41eb22c14e29b06284100a61c50fd849150fefe2eab89e1d1a78c55` |
| B0 hostile gate review (Sol) | `8ffc0a06edcf2be3908b1486da57e7d4a024973e679f9d25577cc281ef005320` |
| B0 verification arm (Grok) | `4887fb9b8254d989209981cc7f04288bd394f998a0e85eb453b94699a4760324` |
| π₁ acquisition (Grok) | `cd503e487e3b5277519e4d0668de2d6ca69b0f4002405bfb406cce17df6e3b82` |
| THETA-reopen report (Sol) | `4009c3abdc16e972aec121206664a21adc81ff8467dfe8d5a0f561e90f3a86d5` |
| THETA-reopen review (GPT-5.5) | `26079008ffeba9b94ecfcc79c63690cc232f7f50f655d477835dc26b80f59cd3` |
| (M′) integration (prior) | `69970f4d2c4a2c5760e116400b1b27426edc41fdf6a8d15936df14cc567855c9` |

Custody note: the B0 report's lane rc=5 was post-run tool-hash drift caused
by the coordinator's own P0 custody patch applied mid-flight (commit
history at 13:15Z); charged inputs UNCHANGED, seal CLEAN. Adjudicated and
charged with disclosure. Ops rule adopted: no ops patches while lanes fly.

## 1. PROMOTED (gate review §10 scopes; verification arm concordant)

Standing: `F` noninvertible plane Keller, degree `N`; H2 = `A_F`
irreducible; H3 = `normalization(A_F) = A^1`.

1. **Prop 2.1–2.2** (chart dictionary; `det DF_φ = -m_φ J t^{μ_l-1}`;
   `μ_l ≥ 1` forced; `μ_l = 1` iff the chart map is a local
   biholomorphism along the dicritical), with the gate's qualified
   "same chart" wording. **Prop 2.3 is NOT promoted**; retained only as:
   the determinant-order and gcd data alone do not exclude `l = k+1`.
2. **Lemmas 3.1–3.4** (branch locus `Br = ∪_{μ≥2} D_l ≠ ∅`; meridian
   cycle type; [O-5.2] smooth-branches consequence — pointwise, with
   global zero-correction as a sufficient hypothesis; the Euler forcing
   lemma for irreducible `A_F`, `N ≥ 3`, under either branch, with the
   gate's equality repair).
3. **Theorem 3.5** verbatim: no noninvertible Keller map has `A_F`
   irreducible with (i) `A_F` smooth, or (ii) all `corr_l = 0` and
   `2a ≤ N`. **Cor 3.6**: an irreducible `A_F` is singular (an
   independent reproof alongside Chau 4.4, not a strengthening — the
   gate corrected the scope gloss). **Cor 3.7**: H2 ⟹
   `Σ μ_l ≤ N-2` (Orevkov Cor 4.3 strict); "non-immersive point" read
   as *critical point of an immersed parametrization*. **Cor 3.8**:
   no component of `L_F` has `μ_l = N-1`, all noninvertible Keller
   (Orevkov's unproved Remark, now proved). **Prop 4.1**: an
   all-trivial dicritical profile is impossible (degree-independent).
4. **Theorem 4.2 (B0 at N=4 under H2)**: no `μ=1` affine-image
   dicritical; unique cost profile `(2,1)`; `s_1=1`, `a=2`, `b=0`,
   `(δ,e)=(1,2)`; meridian a transposition; global monodromy `S_4`.
   The `(M)`-verbatim sentence holds **with H3 added** (gate: GAP as
   printed; H3 or the checked affine-line bridge is required). The
   census equality `f(z)=2` is unused — Cor 4.5 of SHEET-GATE is
   obsolete for this horn (**Cor 5.2**, N=4+H2 scope only).
5. **Theorem 4.3(1)–(4)** (residual reducible-`A_F` configuration),
   plus the gate's addition `Sing D_1 ∩ D_0 = ∅`. **Theorem 4.3(5) is
   REFUTED as printed** (ε-sign; both arms found it independently — the
   verification arm exhibited a `c_0=2` numerical configuration on the
   printed identity). **Repaired residual, promoted**: by Orevkov
   Lemma 2.1, `ε ≡ 0`; then `s_0 = 1`, `c_0 = 1`, and BOTH
   normalizations are `A^1`: `D_1` and `D_0` are polynomial curves;
   `Cor 4.4` holds throughout the repaired configuration (`D_1`
   singular; its singularities double points of two smooth branches,
   none on `D_0`, `a_p = 0`, local monodromy two disjoint
   transpositions).
6. **Cor 5.1**: under H2, `2m_nt + m_triv ≤ Σμ_l ≤ N-2`; at `N=5`,
   `m ≤ 2`.
7. **N=5 residual census (repaired)**: under H2 exactly ONE profile
   carries a trivial dicritical: `(μ,corr) = (2,1)+(1,0)` with
   `(s_2,s_1,a) = (1,1,2)` — the report's second profile
   `(2,0)+(1,1)` is killed by Żołądek 6.5(b) (`μ=1 ⟹ corr=0`), a
   sourced exclusion the report missed. `OPEN[B0-GENERAL-N]` remains,
   so re-typed.
8. **THETA bounded exclusions** (review fully CONFIRMED):
   OBSTRUCTION[A-DEGREE-ZERO] universally, and
   OBSTRUCTION[A-LINEAR-MINIMAL-JET] at `A`-degree ≤ 1, `p=Z²`,
   `r=Z³−Z`, `T_0=0`. The **degree-8 reframe is adopted as routing
   input**: a landed one-cusp pullback composes to a noninvertible
   Keller map of geometric degree 8, so the horn is settled by
   inconsistency proofs, never by construction; the all-degrees
   induction is OPEN with its first break at `A`-degree 2.

## 2. THE RESIDUAL — one sharp question (PI1-S4)

`OPEN[B0-N4-REDUCIBLE-PI1]`, re-typed by the gate repair + acquisition:

> **(PI1-S4)** Let `D ⊂ C²` be an irreducible polynomial curve
> (normalization `A^1`, one place at infinity) whose every affine
> singularity is a double point of two smooth branches (tangency
> allowed, `A_{2k-1}`). Can `π₁(C² − D)` surject onto `S_4` sending
> every meridian of `D` to a transposition, with the two local
> meridians at each double point mapping to DISJOINT transpositions?

NO closes B0 at `N=4` unconditionally, promotes `A_F = B` at rank four,
and completes the (M) programme in both classes. Acquisition verdict:
OPEN — no source decides it; **no countermodel exists in the class**;
sourced subclass YES results: ordinary nodes + Nori 3.27 after
resolving infinity with `C̄² > 2r`; smooth/flex infinity (Zariski–Oka:
cyclic); ordinary nodes + Orevkov-1990 negativity at infinity (cyclic).
Key negative (flagged inference, to be verified in the successor): the
local group of `A_{2k-1}` admits disjoint transpositions, so the
obstruction MUST be global — infinity and the global braid relation are
where the answer lives. The `C^*` alternative is REMOVED by the repair
(both normalizations `A^1`). Full abelianness is sufficient but
stronger than necessary.

## 3. Stops and corrections binding on future work

- Do not cite B0 report Thm 4.3(5) or its `+ε` identity; use the
  repaired residual of §1.5 only.
- Do not cite Prop 2.3 as a theorem; Route-1-style local valuative
  closures remain conceivable.
- Do not use "locally irreducible singularity" for the Cor 3.7
  conclusion; the promoted reading is critical point of an immersed
  parametrization.
- (M) instantiations at N=4 require H3 wherever `ν`/`s` bookkeeping is
  consumed; T4.2's B0 content itself is H3-free.
- The one-cusp horn may not be attacked by construction (degree-8
  reframe); successor lanes prove inconsistency or bound complexity.
- PI1-S4 successor must treat the acquisition's §4 local-relations
  claim as an inference to re-derive, not a source.

## 4. Review-routing experiment, data point 4

Paired arms on B0 agreed on the core theorem and independently caught
the SAME load-bearing defect (ε-sign in 4.3(5)) by different methods —
the gate by source repair (Orevkov 2.1), the verification arm by an
explicit countermodel configuration. The apparent N=5 conflict
(two profiles vs one) resolved in the gate's favour via a sourced
exclusion outside the report's own system, which the verification arm
was not asked to apply. Pairing retained for flagship gates.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7639`.
- Body SHA-256:
  `812504fab56c25c6a6ef1bc67488981b5c9c939f0dbd697c5df62d1dda64a89d`.
- Frozen basis: `830b9f097dd77f3880f9f0a1cc07ee27a66fc7e0`.
