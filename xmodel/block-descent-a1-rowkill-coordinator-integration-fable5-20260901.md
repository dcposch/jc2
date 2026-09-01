# Coordinator integration: the S₄ row-kill theorem — both N=4 residual curve rows are dead

Owner: fable5 (coordinator). Basis: `6779309a`. Fifth binding integration;
extends `69970f4d`, `bbd48de1`, `bafe5e89`, `126c2d29`.

## 0. Charge (wave 14–18 artifacts)

| Artifact | SHA-256 |
|---|---|
| TORUS-CHECK (Opus) | `a352be2af1aebb5e158cb541a6eacdd0feb90f2ea3aa6750fb4bf1969c6bfefe` |
| TORUS-CHECK hostile gate (Sol) | `0fb4778e6baa40fa6961e1cae8e7c7faf5dd88e3f5ca4ce2dd0c2ba8f02fba83` |
| TORUS-CHECK verification (Grok) | `9b03dad679d5060d2456bff81037feb008c448196dc1ddf8bee3a06d20a0b200` |
| EDGE-MODULI (GPT-5.5) | `d853764d8eebc2c9d59a72ec2816bbc1122708649dd790307bfb304c659b440c` |
| ROW-84 (Opus) | `6bdd164ca89bfd8b8947dbb23222929bfd575c48e65b261f3c085397de42bd64` |
| Combined closure review (Grok) | `a88890bdf50e9b864379eb62603d08c11f67f981d589360b75a58ae0d60e5896` |
| TRIPLE-COVER r2 (Sol) | `c99ffc7f64562ac08e81aa7e927dc04e8c0765182d99db9fdc9f10351772cf9f` |
| TRIPLE-COVER-CLOSE (Sol) + review (5.5) | `14021542…`, `0dd3b8d5…` |
| NONMONOGENIC (Sol) | `7d7321589b83b6a0da5d44e6b4a657174d5746f50f131d095f602399a5d2ca65` |
| FIXED-TUPLE (Opus) + review (Sol) | `a6088750…`, `01ddd1fb…` |
| FOLD-REDUCTION (Opus) + review (Grok) | `8529de8e…`, `7c23976b…` |
| ZVK-U6 (Opus) + review (Grok) | `d0dc4f79…`, `9344d6b3…` |
| M-INF (Grok) + review (Sol) | `084346b5…`, `8b9fe37f…` |
| D1-DEGREE (Sol) + review (5.5) | `0549dfaf…`, `028b1c03…` |
| N5-REDUCIBLE (Opus) + review (Sol) | `48d417d6…`, `bd6443b3…` |
| HF-TWIN (Grok) + review (5.5) | `7cef355b…`, `735990ea…` |
| R5-CHARGE (Grok) | `b10e91a1…` |
| LIT-TARGETED (Grok) | `a130acb5…` |
| N5-S2 (Sol, PROVISIONAL — review pending) | `363cdd1ce1253b0a7429b231e2151477e3eaaad794710b98b73a9f530537f6d5` |

## 1. THE CENTERPIECE — promoted per the combined closure review

> **THEOREM (S₄ row-kill, corrected scope).** Let `D_{b,c}` be the
> explicit ROW-NF sextic family (`x=r(t)²`, `y=q(t)`, `r=t³+bt+c`,
> `q=t⁴+(2b/3)t²+(4c/3)t`, `c≠0`) and `D'_{b,c}` the explicit (8,4)
> octic family (its image under `Φ⁻¹`, `Φ=(x−y²,y) ∈ Aut(A²)`). Then
> for EVERY `c≠0` — all moduli, no stratum gap — there is no
> surjection `π₁(C²−D) ↠ S₄` sending curve meridians to
> transpositions.

Proof chain, every link different-model reviewed: affine typing per
stratum (three nodes iff `b≠0, j≠−81/16`; `j=0` is `D₄+A₁₄`;
`j=−27/4` is still `3A₁` — the "tacnode stratum" mislabel is purged;
`j=−81/16` is `A₃+A₁`); Theorem NO-TORUS at every stratum (four
proofs generic; exact elimination + Oka ρ-count at `j=0`; Oka
essential at the `A₃` edge); the S₃ resolvent; Theorem INF-TRIVIAL at
every stratum (`γ_∞` an even word — `2+2+2` generic, `g₅²g₁⁴` at
`j=−27/4` via the ball-complement argument); descent to `P²` (with
the gate-inserted generalized-Riemann-existence + normality +
miracle-flatness step); **Shirane** Cor 0.6 (fetched, hashed, typo
noted) forcing torus type — contradiction. The (8,4) family dies by
the meridian-preserving `Aut(A²)` transport (`Δ=(8,4,6,3) ⟺
deg(P−Q²)=6`, so `Φ` is a type-preserving bijection of the whole
explicit families — including degenerate moduli).

**Dependency list (all that the theorem still rides):** Shirane
Cor 0.6 as a published theorem (hashed); ROW-NF family membership =
campaign row identification (Theorem FOLD statement + ROW-SWEEP
census — both review-CONFIRMED but the closure review retains the
exhaustiveness label PROVISIONAL; "union = campaign rows" is NOT
promoted). Adjudications bound: `(c(Π),g_L) = (4,0)` on the vertical
pencil (the `(2,1)` value is correct arithmetic for a different
pencil — not a competitor); the FIXED-TUPLE/ZVK finite sets are
retired for cover existence but not "mathematically answered".

## 2. Consequences bound

1. `OPEN[PI1S4-(6,4)-FIXED-TUPLE]`, `-TRIPLE-COVER`,
   `-FACTORIZATION`, `-FOLD-*`: resolved NO / vacuous / retired at
   the scopes the gate fixed. The class (7.1) is empty because the
   ambient class `C_F` is empty on the explicit families.
2. The AWS braid job is a pure CROSS-CHECK; its outcome cannot
   promote or demote the theorem, only flag an inconsistency.
3. **The N=4 reducible residual is now exactly the six (8,6)/(9,6)
   AM-numerical types** under exact msolve decision (both-engine
   agreement rule). EMPTY on all six ⟹ B0 closes at N=4
   unconditionally (given the ROW-NF exhaustiveness dependency).
4. N=5 (PROVISIONAL, review pending): the corrected cage is TWO
   survivors — S1 (singular branch; own treatment needed) and S2
   (PI1-S4 shape); S2's coprime stratum is killed by
   THEOREM[S5-COPRIME-KILL] (the Theorem-A machinery runs at S₅) and
   its (6,4)-cable stratum by transport; residual
   OPEN[PI1-S5-NODAL-NONCOPRIME] + OPEN[N5-S2-ROW-PIN].
5. Auxiliary promoted items: M-INF Piece 1 (the reduction is an
   equivalence); the (6,4)-counterexample to the general β_h bound
   (out-of-class); D1-DEGREE cage at typed scope; HF-TWIN
   PASS_NECESSARY_ONLY with pins (first confirmed counterexample-side
   construction target); STOP[R5-CHARGE/NO-FROZEN-GRAMMAR] (matrix
   route formally closed); GAP[BETA0-TUBE-POSITION] retained.

## 3. Stops binding on future work

- Never cite the "three-ordinary-node stratum j∉{−27/4,−81/16}"
  sentence — the corrected stratum table of the closure review §2 is
  the only licensed typing.
- Cite **Shirane**, not Shimada, for Cor 0.6.
- The row-kill covers the EXPLICIT families; campaign-row phrasing
  requires the FOLD/ROW-SWEEP identification and stays PROVISIONAL
  until an exhaustiveness lemma is separately promoted.
- Suite verdicts require .ms/.m2 agreement; NONEMPTY verdicts are
  additionally PROVISIONAL until the repaired idp postcheck runs.

## 4. Paired-review ledger (data points 7–9)

TORUS-CHECK: the gate found the stratum error, the citation error,
and adjudicated (c(Π),g_L); the verification arm independently found
the same stratum error (j=0 D₄) by explicit computation and confirmed
INF-TRIVIAL's feeds — convergent catches, complementary methods. The
closure review then repaired both reports' residual mislabels and
supplied the missing ball-complement argument. Three consecutive
waves in which review strictly improved the theorem. Pairing stays
mandatory for flagship promotions.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6431`.
- Body SHA-256:
  `786499db079b016fff8394231587ca7b362d066453b13133bd49356ced39e3cf`.
- Frozen basis: `6779309a30bc2a9ffa205a7d3244f10bc54bf8c1`.
