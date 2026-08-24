# Hostile different-model review — partial-`y` history stop and `(6,9)` frontier

| Field | Value |
|---|---|
| Claim under review | Frozen producer history stop: every characteristic-zero Keller pair whose two *actual* `y`-degrees are at most eight is a polynomial automorphism, by a large triangular source shear plus the repaired Appelgate--Onishi prime-total-gcd theorem and the peer-reviewed Guccione--Guccione--Valqui `2p` theorem, together with equal-degree target `GL_2` and divisible-degree target shears. The first fundamental remainder at maximum nine is `(6,9)` with `3\|H`. The coprime weighted-boundary mechanism stops on a two-dimensional common-cubic family. Conditional on the already reviewed residue-ball Hensel noninjectivity, an exact AS109 lift cannot have maximum actual `y`-degree at most eight, and a lift of maximum exactly nine reduces to `(6,9)` with `3\|H`. Out of scope: existence of a lift, arbitrary support, higher degree, and JC2 |
| Overall verdict | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking: the cited Kyoto bitstream for Nagata currently serves HTML so the producer hash of that PDF was not independently recomputed; GGV Corollary 7.9 is phrased as `B\neq 2p` but its ingredients exclude `gcd=2p` for every standard pair; after weighted gauge the common-cubic moduli dimension is one, still positive) |
| Evidence tier | independent hand re-derivation of the top Jacobian identity, the leading UFD, the exact sheared total degrees, and the `y^{13}` row; official Magnus PDF, official GGV arXiv source, official Moskowicz arXiv source, and the local official Żoładek PDF, all hash-checked; GGV Corollary 7.9 and Lemma 4.10 of Żoładek read in the primary text; an independently written 81-pair enumeration, Dirichlet grid, `K^2`/`K^3` expansion, binary Jacobian, and integral first-row control that do not import the producer scripts; unmodified rerun of both registered replays as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T12:05:00Z – 2026-08-24T12:27:42Z |
| Python | 3.14.6; stdlib only |
| Singular | `/opt/homebrew/bin/Singular` |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer and provenance inputs reread in full before any verdict:

- `xmodel/as109-partial-y-history-stop-20260824.md` (SHA-256 `6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe`)
- `cases/as109_partial_y_history_stop_20260824/verify_coverage.py` (SHA-256 `0e07b8fcc51a7b3cf2b84985aff0bf0fce6f8eeb06e76b6e60d2b1ac6ccc6f9f`)
- `cases/as109_partial_y_history_stop_20260824/verify_69_cubic_power_stop.sing` (SHA-256 `980a44cfd5f0ab8fa6f3ed7cd91c15704bcd49bc59f2bc97a4fadcaa5c9ea8fd`)
- `cases/as109_partial_y_history_stop_20260824/FREEZE.sha256` (SHA-256 `f3d0dc4167cb1df4537f6ff2aeee37252c0c4be6cb3431e30920b85952158d34`)

Conditional inputs, consumed only at the stated hypotheses:

- `xmodel/as109-support-gate-20260824.md` and landed review `xmodel/as109-support-review-grok-20260824.md`, Claim 6 only: one-way Hensel noninjectivity of an exact seed lift over `Q_{109}`
- `xmodel/as109-bounded-y6-chain-audit-20260824.md` and landed review `xmodel/as109-bounded-y6-chain-review-grok-20260824.md`, only to record that the prior `(4,6)`, `(5,6)`, and bounded-`y<=6` certificates remain mathematically valid and are superseded as *novelty*, not as validity

Primary sources retrieved or hash-checked independently of the producer:

- Arne Magnus, *Math. Scand.* 3 (1955), 255–260, official MSP/tidsskrift PDF. SHA-256 `f8c95ebdb04076928d8e37d1cf862853bf05cbbd5f6a7cc2bf32fb0f90e800da`. Theorem 2 read in full from the scan.
- C. Valqui, J. A. Guccione, J. J. Guccione, *J. Algebra* 471 (2017), 13–74, arXiv:1401.1784v3 e-print. SHA-256 `e6a01769d1f017467c2cba2b1e425ed708da9b4ac917391399fb34f5ac0d86f0`. Abstract, definition of `B`, and Corollary 7.9 read in full.
- Vered Moskowicz, arXiv:1810.08202v2 e-print. SHA-256 `ca974bd7a3603262952c9a5751bc7466c71b2ed47693489e5991096846674419`. Theorems 1.1, 1.2, 2.4, 2.6, 2.7, Proposition 2.1, and Remark 4.2 read in full.
- Henryk Żoładek, *Topology* 47 (2008), 431–469, local official PDF `refs/zoladek2008_official.pdf`. SHA-256 `88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad`. Pages 444–448, including Lemma 4.10 and the Appelgate--Onishi/Nagata sentence on p. 447, inspected only to delimit the gap.

The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. Named producer artifacts remain uncommitted on top of that basis. No producer, canonical, ledger, freeze, or case file was edited. No enumerator was written into the tree. No AWS call was made.

Write `K` for an arbitrary characteristic-zero field. Actual `y`-degrees are used throughout.

---

## Promotion

**Accept `SOURCE-AUDITED HISTORY STOP; ALL MAXIMUM ACTUAL y-DEGREE <=8 IS CLASSICAL; FIRST FUNDAMENTAL REMAINDER IS (6,9) WITH 3|H` at the stated scope.**

- Over any characteristic-zero field, every Keller pair with both actual `y`-degrees at most eight is a polynomial automorphism of `A^2_K`.
- At maximum nine the only fundamental residue of this theorem is `(6,9)` with `3 | deg(h)`. The pair `(9,9)` is derivative: one integral constant target `GL_2` step lands on some `(r,9)`, and the only nonclassical child is `(6,9)` with `3|H`.
- The coprime weighted finite-map mechanism used by the campaign's `(5,6)` calculation does not have a zero-dimensional leading boundary at this residue. The family `(K^2,K^3)` is a positive-dimensional common-cubic stop, not a Keller pair.
- Conditional on the already reviewed Hensel lemma: an exact `Z_{109}` lift of `(x-x^{109},y)` with `det J=1` cannot have maximum actual `y`-degree at most eight, and a lift of maximum exactly nine reduces, after an integral constant target `GL_2` and possibly a swap, to `(6,9)` with `3|H`.

**Do not promote this to:** existence of a lift; nonexistence of a lift; an arbitrary-support AS109 no-go; a found Keller pair of type `(6,9)`; impossibility of some other `(6,9)` method; a total-degree theorem; a JC2 decision; or a claim that the campaign's `(4,6)`, `(5,6)`, and bounded-`y<=6` *proofs* are wrong.

**Do not start** a `(4,7)`, `(5,7)`, `(6,7)`, or other consecutive computation. Those are history duplicates.

**Smallest valid successor.** A transverse deformation of the depressed `(6,9)` Jacobian system about `(K^2,K^3)`, quotiented by source/target gauges and the tangent space in `(u,v)`, with the cubic Kummer weights imposed, asking whether the constant Jacobian row lies in the cokernel. Stop that gate if the constant row survives generically. Do not open a generic coefficient search on the `(6,9)` leading boundary.

---

## Quarantine

No result here proves or disproves JC2. Producer strings `PASS-PARTIAL-Y-HISTORY-COVERAGE` and `PASS-(6,9)-CUBIC-POWER-STOP` were not used as evidence; the pair table, the shear identities, and the cubic family were re-derived. Hensel is consumed only as the already reviewed one-way noninjectivity of an exact seed lift. The prior bounded-`y<=6` synthesis and its two leaf reviews remain valid as alternative proofs; they are not first exclusions of those strata and are not an input to the coverage argument of Sections 1–3. Priority is separated from mathematical validity.

---

## Scope (not enlarged)

One characteristic-zero field theorem about *actual partial* `y`-degrees through eight, the identification of `(6,9)` with `3|H` as the first fundamental remainder at nine, a negative control that the coprime finite-map mechanism fails there, and a quarantined AS109 degree implication. Arbitrary finite `x`-degree is in scope. Generic coefficient search, AWS, a constructed lift, an arbitrary-support no-go, and JC2 are out of scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Top Jacobian identity `n a_m' b_n - m a_m b_n'=0`; UFD `a_m=α h^a`, `b_n=β h^b` for `m=da`, `n=db`; sheared total degrees `a(H+dL)`, `b(H+dL)`. Constant `h`, arbitrary characteristic-zero constants, scalar extension, source orientation `σ_L(x,y)=(x,y+x^L)`, domination `L>max(M,1)`, unique top term, no cancellation. Automorphy equivalent before and after the shear | **CONFIRMED** | a leftover `y^{m+n-1}` term; kernel of `d/dx` on `K(x)` larger than `K`; `L>M` failing to dominate a lower row; postcomposition used as if it were a source shear; a source auto manufacturing automorphy in only one direction |
| 2 | Magnus is the coprime-total-degree theorem, not the prime-gcd theorem. Nagata repairs Appelgate--Onishi in the prime-gcd scope consumed here. GGV independently excludes total-degree gcd `2p` for every prime, and the Żoładek Lemma 4.10 gap is not projected onto that proof. Field hypotheses and descent from `C` to arbitrary characteristic zero are exact | **CONFIRMED** | Magnus used as if it covered `gcd=p`; Appelgate--Onishi cited alone for prime gcd; Żoładek used as the `2p` input; GGV proving only `B≠2p` for the global minimum and not excluding a non-minimal `2p` pair; a missing descent for a theorem written only over `C` |
| 3 | After `g=gcd(H,d)`, Dirichlet produces arbitrarily large `L` with `H_0+d_0 L` prime. Cases `g=1,2` are exactly prime and `2p`. All 81 ordered pairs of maximum actual `y`-degree at most eight are covered, including zeros, equal degrees, divisible shears, constant leadings, and lex termination. The complete maximum-nine row has sole fundamental residue `(6,9)` with `3\|H`; `(9,9)` is derivative | **CONFIRMED** | a missing pair; a cycle in `(max,m+n)`; Dirichlet failing for `H=0`; `(8,9)` with constant leadings escaping; `(9,9)` independently closed; a second fundamental max-nine residue |
| 4 | The prior `(4,6)`, `(5,6)`, and bounded-`y<=6` certificates remain correct but cease to be new coverage. Moskowicz 2018 is the older theorem of this method, not strictly stronger than the producer's formulation, and does not close `(6,9)` with `3\|H`. Priority is separated from validity | **CONFIRMED** | a published `deg_y<=8` theorem that also closed `(6,9)` with `3\|H`; Moskowicz 2.6 already covering that residue; the campaign leaves being *invalid* rather than merely unoriginal |
| 5 | Re-expansion of `K=z^3+u t^2 z+v t^3`, `F=K^2`, `G=K^3`: binary Jacobian zero, depressed `z^5` and `z^8` rows, boundary ideal dimension two, Kummer weights `(1,2,0)`. This proves only failure of the prior finite-map mechanism. The two-dimensional family and descent survive the stated normalizations; after gauge the moduli dimension is still positive | **CONFIRMED** | a nonzero Jacobian; boundary ideal dimension zero after the stated depressions; Kummer weights killing the family; the family being a Keller pair; a claim that no other `(6,9)` method exists |
| 6 | Seed congruence forces `109` to divide all `y^{>=1}` coefficients of `P` and all `y^{>=2}` coefficients of `Q`. Primitive-core Gauss gives `v_{109}(α),v_{109}(β)>=1`. The `y^{13}` row is `8 a' d + 9 c' b - 6 a d' - 5 c b'=0`, every term already `0` modulo `109^2`. The explicit control is a zero-Jacobian pair, not the seed and not a Keller pair | **CONFIRMED** | a seed `y`-power of degree `>=2` in `Q` or `>=1` in `P`; content of a primitive `h` absorbing the `109`; a leftover `y^{13}` term of valuation `0` or `1`; treating `(5.5)` as a lift |
| 7 | Integral constant target `GL_2` on raw `(9,9)` uses the smaller `109`-adic content, stays in `Z_{109}`, and preserves the seed/high-row divisibility, noninjectivity, and invertibility equivalence. With Hensel only, every exact AS109 lift of maximum actual `y`-degree exactly nine reduces to `(6,9)` with `3\|H`, and maximum at most eight is excluded. Existence, arbitrary support, higher degree, and JC2 remain quarantined | **CONFIRMED** | a ratio outside `Z_{109}` after the content-directed choice; a chart-destroying shear applied to the lift before Hensel; Hensel asserting existence; the corollary claiming no lift of degree `>=10` |
| 8 | Every frozen hash matches. Both registered replays rerun unmodified. An independently implemented pair enumeration and exact algebra check recover the coverage table, the expansions, the Jacobian, and the first-row control. No AWS. No producer/canonical/ladder edit | **CONFIRMED** | a hash mismatch against the launch prompt or `FREEZE.sha256`; a registered replay failing; an independent enumeration finding a missing pair or a nonzero cubic Jacobian |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Replay and hashes

Frozen hashes, recomputed on the charged tree, match the launch prompt and `FREEZE.sha256`:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as109-partial-y-history-stop-20260824.md` | `6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe` | prompt and `FREEZE.sha256` |
| `cases/as109_partial_y_history_stop_20260824/verify_coverage.py` | `0e07b8fcc51a7b3cf2b84985aff0bf0fce6f8eeb06e76b6e60d2b1ac6ccc6f9f` | prompt and `FREEZE.sha256` |
| `cases/as109_partial_y_history_stop_20260824/verify_69_cubic_power_stop.sing` | `980a44cfd5f0ab8fa6f3ed7cd91c15704bcd49bc59f2bc97a4fadcaa5c9ea8fd` | prompt and `FREEZE.sha256` |
| `cases/as109_partial_y_history_stop_20260824/FREEZE.sha256` | `f3d0dc4167cb1df4537f6ff2aeee37252c0c4be6cb3431e30920b85952158d34` | prompt (self-hash) |

The case directory contains exactly those four files. No enumerator, exponent rectangle, or AWS helper is present.

Registered commands, rerun unmodified:

```sh
python3 cases/as109_partial_y_history_stop_20260824/verify_coverage.py
Singular -q cases/as109_partial_y_history_stop_20260824/verify_69_cubic_power_stop.sing
```

Both exit 0. Exact output:

```text
PASS-PARTIAL-Y-HISTORY-COVERAGE
consecutive_pairs=KNOWN_BY_PRIME-GCD-SHEAR
max_actual_y_degree_le_7=ALL_64_ORDERED_PAIRS_COVERED
max_actual_y_degree_le_8=ALL_81_ORDERED_PAIRS_COVERED
max9_fundamental_open=(6,9) with 3|H
max9_derivative_open=(9,9) via target-GL2 successor (6,9)
preflight_target=(6,9),3|H

PASS-(6,9)-CUBIC-POWER-STOP
leading_boundary_dimension=2
finite_weighted_map=false
coprime_common-factor_lemma_transfers=false
as109_scalar_valuations_control=(1,1)
as109_first_nontop_valuation_contradiction=false
generic_search_run=false
aws_used=false
as109_lift_construction_or_exclusion=false
jc2_inference=false
```

Those PASS strings are regression only. The independent enumeration and algebra of Claims 3 and 5 are the evidence.

Independently recomputed primary-source hashes that match the producer table:

| Source | SHA-256 | Match |
|---|---|---|
| Magnus, official MSP/tidsskrift PDF | `f8c95ebdb04076928d8e37d1cf862853bf05cbbd5f6a7cc2bf32fb0f90e800da` | producer §2 |
| GGV arXiv:1401.1784 e-print | `e6a01769d1f017467c2cba2b1e425ed708da9b4ac917391399fb34f5ac0d86f0` | producer §2 |
| Moskowicz arXiv:1810.08202 e-print | `ca974bd7a3603262952c9a5751bc7466c71b2ed47693489e5991096846674419` | producer §2 |
| Żoładek local official PDF | `88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad` | producer §2 |

The Kyoto bitstream `9ef8e868-5526-4830-b19f-543c0af09e7c` currently returns an HTML shell, so the producer hash `ea57f589536d97866155a81cd0c2177743ac9e1fe0ab6e8536cb71d00cae0bb7` of the Nagata PDF was not independently recomputed. The theorem-scope claim is corroborated from other primary text (Claim 2). This is a process limitation, not a citation error.

---

## Claim 1 — top-row UFD and source shear

**CONFIRMED.**

Let `P=a_m(x) y^m+...`, `Q=b_n(x) y^n+...` be a Keller pair over `K` with `m,n>0` and `J(P,Q)∈K^*`. A pair of terms `(a_i y^i, b_j y^j)` contributes `j a_i' b_j - i a_i b_j'` to the coefficient of `y^{i+j-1}`. Lower `y`-coefficients cannot produce a higher top degree, so the unique contribution to `y^{m+n-1}` is

```text
n a_m' b_n - m a_m b_n' = 0.                                  (1.1)
```

Characteristic zero supplies `n≠0` and `deg π'=deg π-1` for nonconstant `π∈K[x]`. Equivalently `(a_m^n / b_n^m)'=0` in `K(x)`, hence `a_m^n = c b_n^m` with `c∈K^*`: the kernel of `d/dx` on `K(x)` is `K`.

Put `d=gcd(m,n)`, `m=d a`, `n=d b`, `gcd(a,b)=1`. Then `b v(a_m)=a v(b_n)` at every prime of `K[x]`. Coprimality of `a,b` forces `a | v(a_m)`, so

```text
a_m = α h^a,     b_n = β h^b,     α,β ∈ K^*,   h ∈ K[x].     (1.2)
```

Units of `K[x]` are `K^*`, so no polynomial root is extracted and no scalar extension is required for (1.2). Constant nonzero `h` is included: `H:=deg(h)=0`. Absorbing a unit of `K` into a perfect `a`-th power is optional for the degree count and is the only place a scalar extension of the constant field could appear; it is not used below.

Let `M` be the maximum `x`-degree of all coefficients of `P` and `Q`, and let `L>max(M,1)` be an integer. The triangular source automorphism is

```text
σ_L(x,y) = (x, y+x^L).
```

On the coordinate ring this is `P ↦ P(x, y+x^L)`, which is Moskowicz's convention: the algebra endomorphism `g:(x,y)↦(x,y+x^L)` applied to `p=f(x)` gives `g(p)=p(x,y+x^L)`. Geometrically this is *precomposition* of the Keller map with `σ_L`. The Jacobian identity `J(F∘σ)=J(F)(σ)·J(σ)` with `J(σ)=1` and `J(F)` a nonzero constant preserves the Keller property. Automorphy is equivalent in both directions because `σ_L` lies in `Aut(A^2_K)`.

For each `j<m`,

```text
deg(a_j(x)(y+x^L)^j) = deg_x(a_j) + L j < deg_x(a_m) + L m,
```

because `deg_x(a_j)-deg_x(a_m) ≤ M < L ≤ L(m-j)`. Within the `j=m` summand the unique largest total-degree term is the leading `x`-term of `a_m` times `x^{L m}`: every other binomial term `y^k x^{L(m-k)}` has total degree `k+L(m-k)=L m-(L-1)k < L m` for `k>0`. There is no cross-row or internal cancellation. The exact transformed total degrees are therefore

```text
deg σ_L(P) = a(H+d L),     deg σ_L(Q) = b(H+d L),
gcd = H+d L.                                                (1.3)
```

Constant `h` (`H=0`) gives degrees `m L` and `n L` with gcd `d L`, as required. The bound `L>max(M,1)` is strictly stronger than Moskowicz's `L>M` and is harmless for Dirichlet.

---

## Claim 2 — primary-source theorem chain

**CONFIRMED.**

**Magnus is coprime, not prime-gcd.** Official scan, *Math. Scand.* 3 (1955), 255–260, Theorem 2 p. 256, read from the pages:

> Let `u=u(z_1,z_2)` and `v=v(z_1,z_2)` denote two polynomials of degrees `m≥2` and `n≥2`, respectively, in the two complex variables `z_1` and `z_2`. If the Jacobian `u_{z_1} v_{z_2}-u_{z_2} v_{z_1}=k=` constant and `m` and `n` are relatively prime, then `k=0` and there exists a polynomial `h` of first degree in `z_1` and `z_2` such that `u` and `v` are polynomials in `h`.

A Keller pair therefore cannot have coprime total degrees both at least two. After the shear (1.3), the total-degree gcd is `H+dL`, which Dirichlet makes a prime `p` or twice a prime, *not* `1`. Magnus does not apply to the sheared pair. The producer correctly refuses to cite it for the `g=1` arrow.

**Nagata repairs Appelgate--Onishi in the consumed scope.** Appelgate--Onishi, *J. Pure Appl. Algebra* 37 (1985), 215–227, prove (as their abstract states) the two-dimensional Jacobian conjecture when the degree of `f` or `g` has at most two prime factors. Żoładek, *Topology* 47 (2008), 447, states in primary text, immediately after the reprint of that theorem as Theorem 4.7:

> H. Appelgate and H. Onishi published this theorem in 1985. In fact, Appelgate and Onishi's proof was not correct, but Nagata [20,21] and Nowicki with Nakai [24] completed it.

Moskowicz, arXiv:1810.08202v2, Theorem 1.1, attributes “`gcd(deg p, deg q)` is `≤8` or belongs to the primes” to Appelgate--Onishi and Nagata pp. 158–159, 169–172 of the 1990 Kyoto record, and the product-of-two-primes case to Nagata pp. 169–170. That is the repaired prime-gcd theorem consumed when `g=1`: after the shear, total-degree gcd is a prime `p`, so Nagata Theorem 7.3 supplies `K[P,Q]=K[x,y]`. The two-prime-factors consequence is *not* the input used for composite consecutive pairs such as `(8,9)`: the sheared degrees are `8p` and `9p`, and `8p` need not be a product of two primes. Prime gcd is the load-bearing statement, and it is the one the producer cites.

The Kyoto bitstream named in producer §2 currently serves an HTML wrapper, so the producer PDF hash was not recomputed (process note above). The theorem-scope claim is independently present in Żoładek p. 447 and in Moskowicz's page citations, both hash-checked. No theorem-scope error was found.

**GGV independently excludes `gcd=2p` for every prime; Żoładek is not consumed.** GGV, *J. Algebra* 471 (2017), abstract, over an arbitrary field `K` of characteristic zero:

> We also prove that `gcd(deg(P),deg(Q)) ≠ 2p` for any prime `p`.

The introduction records the Żoładek gap with the exact assertion GGV could not justify: Lemma 4.10 of Żoładek claims without proof that `I_2 ⊂ (1/m)Γ(f_2)`. The official Żoładek PDF, Lemma 4.10 p. 447, is the lemma whose proof asserts that a successor chart `θ_2` has vertices in a fractional lattice `(1/k)Z × Z` and then estimates `p_0(θ_2)`. That is the diagnosed gap. The producer does not use Żoładek for `2p`.

GGV Corollary 7.9 is phrased as `B≠p` and `B≠2p`, where `B` is the minimum of `gcd(v_{1,1}(P),v_{1,1}(Q))` over counterexamples. The ingredients are stronger than the wording. The first half of Corollary 7.9 holds for *every* standard `(m,n)`-pair: writing `(a,b)=(1/m) en_{1,0}(P)`, one has `(a,b)∈N×N` and `gcd(a,b)>2`. For any standard pair, `G:=gcd(v_{1,1}(P),v_{1,1}(Q))=v_{1,1}(P)/m` and `a+b=G`. If `G=2p` then `gcd(a,b)∈{1,2,p,2p}`; the cases `1,2` are already excluded, `gcd(a,b)=2p=a+b` is impossible for positive `a,b`, and `gcd(a,b)=p` forces `a=b=p`, contradicting `a<b`. Every counterexample reduces, by GGV Propositions 4.2–4.3 / Corollary 5.21, to a standard pair with the *same* `v_{1,1}` degrees. Therefore no counterexample has total-degree gcd `2p`. The abstract matches. A sheared pair with gcd `2p` cannot be a counterexample.

The argument uses no computer search and no restriction on the prime `p`. Dirichlet's large primes are included.

**Field hypotheses and descent.** GGV and Moskowicz are written over an arbitrary characteristic-zero field. Magnus is written over `C` and is not consumed for the coverage. Nagata's symposium record is cited for complex/characteristic-zero polynomials; the producer descends by passing to the algebraic closure of the finitely generated coefficient subfield and embedding it in `C`. Automorphy descends because a polynomial endomorphism of `A^2` has at most one polynomial inverse, which is therefore Galois-fixed (equivalently, faithful flatness of the scalar extension). Nonexistence of a counterexample of a given total-degree gcd likewise descends: a Keller pair over `K` remains a Keller pair of the same total degrees over `C`. No algebraic-closure qualification is missing from the field statement.

---

## Claim 3 — Dirichlet arithmetic and coverage

**CONFIRMED.**

Put `g=gcd(H,d)`, `H=g H_0`, `d=g d_0`, so `gcd(H_0,d_0)=1`. Dirichlet supplies infinitely many `L` with `H_0+d_0 L` prime; the condition `L>max(M,1)` cuts out only finitely many terms, so arbitrarily large such `L` exist. Then `H+dL = g(H_0+d_0 L)=g p`, and (1.3) has total-degree gcd `g p`. Consequently:

```text
g=1  =>  transformed total gcd is prime,     Nagata 7.3;
g=2  =>  transformed total gcd is 2p,        GGV.
```

If `d=gcd(m,n)≤2` then `g∈{1,2}` for every `H`, including `H=0`. If `d=1`, one may take the prime `H+L`; if `H=0`, take `L` itself prime. An independent finite sweep over `1≤m≤n≤20`, `0≤H≤15`, and `L` starting at `20` found a Dirichlet prime in every cell; the producer script's broader grid is consistent and was not imported.

Lexicographic induction on `(max(m,n), m+n)`:

- `m=0`: Moskowicz Proposition 2.1, read in full. If `n=0` then `J=0`. If `n≥2` then `a_0' Q_y` cannot be a nonzero constant. If `n=1` the pair is triangular. Covered, whether labelled triangular or impossible.
- `gcd(m,n)≤2`: Section 1, including constant leadings.
- `0<m<n` and `m|n`: UFD of (1.1) gives `b_n = k a_m^{n/m}` with `k∈K^*`. The polynomial target shear `Q ↦ Q-k P^{n/m}` strictly lowers the larger actual degree. Constant `a_m` is included.
- `m=n>0`: (1.1) makes `a_m/b_n` constant. A constant target `GL_2` cancels exactly one leading `y`-coefficient. Both leadings cannot vanish at once: that would force a zero-determinant matrix.

Shears drop the maximum; equal-degree `GL_2` keeps the maximum and drops the sum. There is no cycle.

Independent classification of all `81` ordered pairs with `0≤i,j≤8`, not imported from the producer script. Unordered pairs are identified by swap (`GL_2`). Counts: `17` zero-coordinate (`Z`), `54` universal shear (`G`), `4` divisible (`D`: the ordered pairs `(3,6),(6,3),(4,8),(8,4)`), `6` equal-degree `E` that are not already `G` namely `(3,3)` through `(8,8)`, and `0` open. Pairs such as `(2,4)`, `(2,6)`, `(2,8)` are `G` because `gcd≤2`, not `D`. Pairs `(1,1)` and `(2,2)` are `G` and are also `E`; either route closes them. The producer table lists them as `E`, which is valid. Every equal or divisible step lands on a strictly smaller lex pair, all of which are already closed. Thus

```text
deg_y(P), deg_y(Q) ≤ 8  =>  (P,Q) is an automorphism.         (3.1)
```

Through eight, the constant-leading case is included: `(8,8)` is `E`, `(6,8)` is `G` via `g=2` and GGV, `(5,8)` is `G` via `g=1`. The pair `(8,9)` belongs to the maximum-nine row below. Moskowicz Theorem 2.7 does *not* cover constant-leading `(6,8)` or `(8,9)` because neither invariant is in `{1,4}∪primes`; the producer shear with prime `L` does. That is a modest strengthening of Moskowicz, not a missing pair in the producer table.

Complete maximum-nine row, unordered `0≤m≤9`:

| Pair | Route |
|---|---|
| `(0,9)` | `Z` |
| `(1,9)`, `(2,9)`, `(4,9)`, `(5,9)`, `(7,9)`, `(8,9)` | `G`, gcd one |
| `(3,9)` | `D` |
| `(6,9)` | gcd three; closed if `3` does not divide `H`; fundamental open if `3\|H` |
| `(9,9)` | `E`; derivative on `(6,9)` only |

For `(6,9)` one has `d=3`, `a=2`, `b=3`, so `a_6=α h^2`, `b_9=β h^3`, sheared degrees `2(H+3L)`, `3(H+3L)`. Then `g=gcd(H,3)` is `1` or `3`. If `3` does not divide `H`, Dirichlet makes `H+3L` prime. If `3\|H`, the gcd is always a multiple of three and Dirichlet only produces `3p`, which no cited total-degree theorem covers. An independent check on `H=0..35` confirms `g=3` if and only if `3\|H`.

The pair `(9,9)` is not independently closed: one `GL_2` step produces `(r,9)` for some `r<9`. If `r≠6` that child is classical; if `r=6` the residue `3\|H` of the *reduced* pair remains. Some `(9,9)` Keller pairs reduce to a classical child and are therefore automorphisms; the *class* `(9,9)` is not a second fundamental remainder.

---

## Claim 4 — novelty / history; older theorems

**CONFIRMED.**

The campaign's independently confirmed `(4,6)` and `(5,6)` certificates, and the bounded-`y<=6` synthesis that consumes them, remain mathematically valid at their stated scopes. They are alternative proofs and exact instruments. They are not first exclusions of those degree strata, because those strata are among the `81` pairs of Claim 3.

Moskowicz, arXiv:1810.08202v2 (2018), is the older theorem of *this method*. After the leading UFD one always has Moskowicz's aligned case `ũ=ṽ` and `ñ=r̃`. Theorem 2.6 then says: if `uv≠0` (nonconstant leadings) and either one of `{A,C}` lies in `{1,4}∪P` or `gcd(A,C)∈{1,2}`, the pair is an automorphism. Here `A=a g`, `C=b g`, and `gcd(A,C)=g=gcd(H,d)`. For every pair with `gcd(m,n)≤2` one has `g∈{1,2}`, so Moskowicz 2.6 already covers all nonconstant-leading pairs that the producer covers by the prime/`2p` shear. Theorem 2.7 covers a coordinate of actual `y`-degree prime or four, including constant leadings via `gcd(N,0)=N`. It does *not* cover constant-leading `(6,8)` or `(8,9)`. The producer shear with prime `L` does. Moskowicz is therefore the older source of the method, and is not strictly stronger than the producer's formulation.

Moskowicz Theorem 2.4's extra residue `{8}∪P∪2P` requires the *non*-aligned case, which the leading UFD of a Keller pair never produces. It does not close additional Keller pairs. Moskowicz Remark 4.2 explicitly records that a `3P` total-degree theorem would upgrade Theorem 2.6 to `gcd(A,C)∈{1,2,3}` and would close `d=3`, including `(6,9)`. That is primary-text confirmation that `(6,9)` with `3|H` is the known next residue of this method, not a new discovery of this freeze.

Heitmann's `gcd(deg P, deg Q)≥16` for counterexamples, and GGV's elementary re-proof of it, are about *total* degrees of a putative counterexample. After a large source shear the total gcd is a large prime or twice a large prime, hence at least `16` automatically. Heitmann does not close additional *partial* `y`-degree pairs, and does not replace Nagata (large primes) or GGV `2p` (large twice-primes). It is not a stronger older theorem for this coverage statement.

Nakai--Baba (total-degree gcd `≤2`) likewise does not apply after a large shear.

No older theorem was found that is both valid and strictly stronger than the producer's formulation in a way that would also close `(6,9)` with `3|H`. Priority: the method is Moskowicz 2018, clarified and slightly strengthened for constant leadings, with GGV in place of Żoładek. Validity of (3.1) does not depend on that priority.

The bounded-`y<=6` chain review's Claim 7 already recorded that classical reductions subsume reducible rows and do not replace the genuine-leaf audit. That observation is now superseded as *novelty*: those genuine leaves `(4,6)` and `(5,6)` are themselves classical by the shear of Claim 3. Their campaign proofs remain correct alternative proofs. This history correction does not import their Newton/Pfaffian identities and does not reopen those reviews.

---

## Claim 5 — `(6,9)` common-cubic stop

**CONFIRMED.**

In homogeneous variables `(t,z)` put `K=z^3+u t^2 z+v t^3`, `F=K^2`, `G=K^3`. An independent monomial multiplication, not imported from the Singular script, recovered

```text
F = z^6 + 2 u t^2 z^4 + 2 v t^3 z^3 + u^2 t^4 z^2 + 2 u v t^5 z + v^2 t^6,

G = z^9 + 3 u t^2 z^7 + 3 v t^3 z^6 + 3 u^2 t^4 z^5 + 6 u v t^5 z^4
    + (u^3 + 3 v^2) t^6 z^3 + 3 u^2 v t^7 z^2 + 3 u v^2 t^8 z + v^3 t^9.
```

There is no `z^5` term in `F` and no `z^8` term in `G`. The pair is monic of actual `z`-degrees `6,9`. The binary Jacobian `F_t G_z - F_z G_t` is the zero polynomial (zero nonzero monomials). At the normalized boundary `z=r`, `t=1` both equations are powers of `K(1,r)=r^3+u r+v`. The ideal `(k^2,k^3)=(k^2)` in `Q[r,u,v]` cuts out the same set as `k=0`, which is the graph `v=-r^3-u r`, of dimension two. This is the `gcd(6,9)=3` common-cubic locus, not a finite set of points.

Cubic Kummer: if `s^3=h` and `s↦ω s`, the stated weights are `z,r` weight one, `u` weight two, `v` weight zero modulo three. Every monomial of the dehomogenized `K=z^3+u z+v` has weight `0 mod 3`, so `K` is invariant and `(K^2,K^3)` together with the root equation descend. The family is not removed by the cubic Kummer descent that kills a constant depression mismatch when the leading core is not a cube.

The Jacobian is zero, not a nonzero constant. The family is not a Keller pair, is not congruent to the AS109 seed, and does not prove that no `(6,9)` Keller pair exists. It proves only the registered negative:

```text
the leading boundary/integral map is not finite on the (6,9) frontier;
the coprime binary common-factor lemma stops at a cubic, not a line.     (4.3)
```

*Gauges, challenged.* Weighted scaling that preserves monic `z^3` acts by `ũ=u(μ/λ)^2`, `ṽ=v(μ/λ)^3`. The parameter `v` has Kummer weight zero and is invariant under the cubic action; it cannot be scaled away by that action. After setting `r=1` on the open where `r≠0`, the boundary equation becomes `1+u+v=0`, a one-parameter family. The locus `r=0` forces `v=0` with `u` free, a second positive-dimensional stratum. The ideal in `Q[r,u,v]` remains two-dimensional because `r` is not gauge-fixed in that ring. After quotienting the one scaling, the moduli dimension is one, still positive. The finite-map stop fires either way. The producer's “two-dimensional family” is the raw `(u,v)`-family of maps, which is the honest count before gauge; the review does not treat that wording as a claim that the gauge quotient is two-dimensional.

No other `(6,9)` method is excluded.

---

## Claim 6 — AS109 integral specialization

**CONFIRMED.**

The seed congruence is `P ≡ x-x^{109} (mod 109)`, `Q ≡ y (mod 109)`. The first coordinate of the seed has `y`-degree `0`; the second has `y`-degree `1`. Every coefficient of `y^i` in `P` for `i≥1`, and every coefficient of `y^j` in `Q` for `j≥2`, therefore comes from the correction and is divisible by `109`. This is a statement about the lifted coordinate pair.

For a reduced pair of actual degrees `(6,9)`, write `P=a y^6+c y^5+...`, `Q=b y^9+d y^8+...`. The top row over `Q_{109}[x]` gives `a=α h^2`, `b=β h^3`. Scale `h` primitive in `Z_{109}[x]`. Gauss: `h^2` is primitive, `a∈Z_{109}[x]`, so `α∈Z_{109}` and `content(a)=content(α)`. But `v_{109}(content(a))≥1` by the seed, hence `A=v_{109}(α)≥1`. The same holds for `B=v_{109}(β)`. Likewise `C=v_{109}(content(c))≥1` and `D=v_{109}(content(d))≥1`, with the convention `∞` for a zero coefficient. There is no top-row reason for `A=B`.

The coefficient of `y^{13}` in the Jacobian is assembled from the pairs `(a y^6, d y^8)` and `(c y^5, b y^9)`:

```text
8 a' d + 9 c' b - 6 a d' - 5 c b' = 0.                       (5.4)
```

(The top `y^{14}` row is `9 a' b - 6 a b'`, matching (1.1) with `(m,n)=(6,9)`.) Independently: `P_x Q_y` contributes `8 a' d + 9 c' b` to `y^{13}`, and `P_y Q_x` contributes `6 a d' + 5 c b'`. Valuation lower bounds: `val(a')≥A`, `val(d)≥D`, so the first and third terms have valuation at least `A+D`; the second and fourth at least `B+C`. Every term is already `0` modulo `109^2`. Reduction modulo `109` or `109^2` cannot supply a contradiction.

The explicit control `h=x^3+1`, `α=β=109`, `P_0=109[h(y+x)^3]^2`, `Q_0=109[h(y+x)^3]^3` has `c=6·109·h^2·x`, `d=9·109·h^3·x`, both scalar valuations equal to one, and (5.4) the zero polynomial (independent polynomial arithmetic over `Z`). The full Jacobian of `(K^2,K^3)` is zero. This pair is not Keller and is not congruent to the seed (it has no linear `y^0` term matching `x-x^{109}`). It is a sharp integral valuation control: it rules out a *universal first-non-top-row valuation contradiction*, not a later-row or seed-specific obstruction, and not a lift.

---

## Claim 7 — conditional maximum-nine implication

**CONFIRMED.**

The reviewed Hensel lemma is a one-way implication: *if* an exact polynomial lift over `Z_{109}` of the seed `(x-x^{109},y)` with `det J=1` exists, *then* it is bijective on each residue ball, hence `109`-to-`1` onto balls over `(0,b)`, hence noninjective over `Q_{109}`. It does not assert that such a lift exists. The support-gate review's Claim 6 is consumed at exactly that hypothesis.

By (3.1), a pair of maximum actual `y`-degree at most eight is an automorphism, hence injective. An exact lift of maximum at most eight would therefore contradict Hensel. The field theorem is applied to the lift pair itself, not to a sheared pair, so chart-destroying source operations never enter the corollary. The seed contributes no `y`-degree above the correction bound.

Now suppose an exact lift has maximum actual `y`-degree exactly nine. Every unequal `(m,9)` other than `m=6` is classical by the table of Claim 3. For a raw `(9,9)` pair, (1.1) makes the leading-coefficient ratio a constant `k∈Q_{109}`. The two leadings lie in `Z_{109}[x]` and are constant multiples, so `v_{109}(k)` is the difference of contents. Choose the direction that cancels the coefficient of *larger* content using the one of *smaller* content:

- if `v(k)≥0` then `k∈Z_{109}` (in fact a unit when `v(k)=0`), and `P ↦ P-k Q` is integral;
- if `v(k)<0` then `k^{-1}∈Z_{109}`, and `Q ↦ Q-k^{-1} P` is integral.

This is a unipotent integral target operation. It preserves `Z_{109}`-coefficients, divisibility of all high `y` coefficients (linear combination), noninjectivity (target automorphism), and invertibility equivalence. It strictly lowers one actual degree to `(r,9)` with `r<9`. If `r≠6` that row is classical, contradicting Hensel. If `r=6`, Claim 3 forces `3|deg(h)` for the *reduced* pair's primitive common leading core. Thus

```text
If an exact AS109 lift has maximum actual y-degree exactly 9, then, after
an integral constant target GL_2 and possibly swapping coordinates, its
only possible nonautomorphic reduced degree pair is (6,9), and its
primitive common leading core satisfies 3 | deg(h).                    (5.6)
```

This is a target-equivalence statement, not a claim about unreduced raw labels. Existence of a lift, an arbitrary-support no-go, a bound on degree ten or higher, a constructed `(6,9)` pair, and JC2 are not implied.

---

## Claim 8 — artifact and scope audit

**CONFIRMED.**

Every frozen hash in the launch prompt matches the on-disk bytes. Both registered replays were rerun unmodified and printed the advertised terminal lines; those lines were not used as theorems. An independently implemented check, not imported from either producer script, recovered:

- `81` ordered pairs through degree eight, `0` open, lex termination;
- Dirichlet primes on a `m,n≤20`, `H≤15` grid, and `g=3` on `(6,9)` if and only if `3|H`;
- the exact `K^2` and `K^3` expansions, vanishing depressed rows, and zero binary Jacobian;
- the `y^{13}` row of the control pair identically zero;
- Kummer weights `{0}` on every monomial of `K=z^3+u z+v`.

No AWS resource was launched. No producer, canonical, ladder, freeze, or case file was edited. The smallest statement that would have failed under any discovered issue is (3.1) if Nagata's prime-gcd theorem or GGV's `2p` theorem had been mis-cited, or (4.3) if the cubic family had had a zero-dimensional boundary ideal. Neither occurred.

---

## Non-blocking precisions

None of the following changes a numbered verdict.

1. *Nagata PDF hash.* The named Kyoto bitstream currently serves HTML. Żoładek p. 447 and Moskowicz's page citations independently confirm that Nagata repairs Appelgate--Onishi and that the consumed statement is prime total-degree gcd. A later freeze may attach a retrievable PDF; no identity changes.

2. *GGV Corollary 7.9 wording.* Phrased as `B≠2p`. The first half of the corollary plus `a+b=G` and `a<b` exclude `gcd=2p` for every standard pair, which is what the abstract states and what the shear needs.

3. *Moskowicz 2.7 versus constant-leading `(6,8)` and `(8,9)`.* Theorem 2.7 does not cover those constant-leading pairs. The producer shear does. This is a modest strengthening, already used in Claim 3, not a hidden appeal to Moskowicz beyond what the producer claims as “consistent”.

4. *Coverage replay children.* Equal-degree `GL_2` and divisible shears are recorded as every strictly smaller pair of the surviving maximum. That over-approximation cannot hide a missing pair. Independent classification uses the same child set.

5. *`(1,1)` and `(2,2)` table labels.* The producer lists them as `E`. They are also `G`. Both routes are valid.

6. *Gauge dimension of the cubic family.* Raw `(u,v)` is two-dimensional; after weighted scaling the moduli dimension is one, still positive. The finite-map stop does not depend on the raw count being exactly two.

7. *Moskowicz Theorem 1.1 uses Żoładek for `2P` with GGV as “see also”.* The producer does not consume Moskowicz as the `2p` input. No gap is inherited.

8. *Heitmann `B≥16`.* Checked and not used. After a large shear the total gcd is already `≥16`. It does not close `(6,9)` with `3|H`.

---

## Attacks that did not land

The following were checked because they are the stated failure modes.

- *Magnus used as prime-gcd.* Theorem 2 of the official scan is coprime total degrees, over `C`, and concludes `k=0` when both degrees are at least two. After the shear the gcd is `p` or `2p`, not `1`. Not used.
- *Appelgate--Onishi cited alone.* Żoładek p. 447 records the error and the Nagata completion. The consumed statement is prime gcd, which is what `(8,9)` after shear needs; the two-prime-factors consequence would not cover `8p`.
- *Żoładek as `2p` input.* Lemma 4.10 is the diagnosed gap. GGV Corollary 7.9 is the input, and it excludes `2p` for every standard pair.
- *GGV only constrains the global minimum `B`.* The ingredients of Corollary 7.9 apply to every standard pair; every counterexample reduces to one with the same `v_{1,1}` gcd.
- *Shear orientation reversed.* Moskowicz `g(p)=p(x,y+x^L)` is precomposition. Automorphy is two-sided.
- *Cancellation of the top term.* `L>M` makes every lower row and every internal binomial term of strictly smaller total degree.
- *Constant leadings escaping.* `H=0` is included; `(6,8)` and `(8,9)` with constant leadings close by prime `L`.
- *Missing pair among the `81`.* Independent listing; `0` open.
- *`(9,9)` independently closed.* One `GL_2` step can land on `(6,9)` with `3|H`.
- *Cubic family a Keller pair or a lift.* Jacobian zero; not congruent to the seed.
- *First-row valuation contradiction.* Every term of (5.4) has valuation at least `2`; the control pair has valuations `(1,1)` and a zero Jacobian.
- *`(9,9)` `GL_2` leaving `Z_{109}`.* Content-directed choice puts the multiplier in `Z_{109}`.
- *Hensel used as existence.* Consumed only as noninjectivity of an exact lift.
- *Older theorem closing `(6,9)` with `3|H`.* Moskowicz Remark 4.2 records that residue as open pending a `3p` total-degree theorem. None is cited, and none was found.

---

## Promotion advice (repeated)

Accept the freeze as a completed characteristic-zero history stop: every Keller pair with both actual `y`-degrees at most eight is a polynomial automorphism of `A^2_K`. Accept `(6,9)` with `3|H` as the first fundamental remainder of this theorem at maximum nine, with `(9,9)` derivative. Accept the cubic-power family as a stop of the coprime finite-map mechanism, not as a Keller pair. Accept the quarantined AS109 corollaries that an exact lift cannot have maximum actual `y`-degree at most eight, and that a lift of maximum exactly nine reduces to `(6,9)` with `3|H`.

- Bank this as a history correction of the bounded-degree campaign, not as a replacement of Hensel or of the support grammar stop.
- Keep the `(4,6)`, `(5,6)`, and bounded-`y<=6` certificates as alternative proofs. Do not treat them as first exclusions, and do not reopen their Newton/Pfaffian identities.
- Do not launch consecutive-degree computations.
- Do not treat this as an arbitrary-support AS109 no-go, a found lift, a JC2 decision, or a claim of priority over Moskowicz 2018.
- Next calculation this review licenses: a transverse deformation gate about `(K^2,K^3)` as described in Promotion. It licenses no enumerator and no AWS.

No result in this review proves or disproves JC2.
