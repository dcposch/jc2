# D125 arc-closure interface gate (Fable 5.1, 2026-09-07)

Bounded 15-minute independent gate (launched 06:54:35 UTC) of the PROVISIONAL composition `xmodel/d125-arc-closure-interface-astra-20260907.md` (file `6f9e63a8…`, body `141f39e8…` re-hashed here over 6623 bytes, whole text read) with its `check.py` (`0861f4dc…`), `replay.json` (`b3bda0b7…`), and the frozen Stacks snapshots 0CM1 (`b8191936…`) and 0C0S (`d9968d0a…`), all read from `/tmp/jc2-lane.D0gf0z/inputs` only. Accepted at their scopes and NOT re-hardened: source 14c, field classification 14f, uniform generic obstruction 14p, exceptional-center discriminator 14q (their frozen texts and prior Fable gates were read to pin exact hypotheses). The tuned-center theorem is not a premise. No live peer, ledger, protected tree, AWS, SSH, CAS, solver, network or full source; only ≤5-factor pure-p multinomial projections and toy varieties were computed. No exit-price assertion is made, so no charge_basis line.

## Verdict table

| item | verdict |
|---|---|
| 1. Rings: S=Q[coefficients,k], I = all unguarded rows, no z/zk−1; J=I:k^∞; X=Spec S/J = schematic closure of D(k) in Spec S/I; U=D(k) dense in X | **CONFIRMED** |
| 2. Every q∈X∩V(k) receives a DVR arc Spec A→X, closed point ↦ q, generic point in U (Stacks 32.15.1 applied to the open immersion U→X); k∈m_A, k≠0; all S-coordinates in A | **CONFIRMED** |
| 3. Â≅L[[s]] with Q⊆L (Stacks 10.160.10(1)); k=s^m u(s), m≥1, u(0)≠0; rows hold in L[[s]], guard on L((s)) | **CONFIRMED** |
| 4. Explicit finite extension L'=L(u₀^{1/m}) + unit root v^m=u (pivot m·v₀^{m−1}≠0) + parameter τ=s·v(s) gives literal k=τ^m for 14p, preserving rows, center, (g,p)-supports | **CONFIRMED**; correctly typed as extension + parameter change, not same-field normalization |
| 5. H=A_(0,13)/3+3 = t+3 on every k=0 field point; 14p ⇒ H=0 at every arc center ⇒ H(q)=0 for all q∈X∩V(k) | **CONFIRMED** (own exact projection [p¹³]R_t³=3t) |
| 6. At t=−3: y=−3α, w=−3γ, v=−243+β; D=5y²+27(v+243)y−27w = 81Δ₀ exactly; 14q ⇒ D(q)=0; v=0 gauge gives 5y²+6561y−27w | **CONFIRMED** (own exact symbolic identity; 243/81/sign reproduced) |
| 7. Conclusion (C): H,D ∈ √(J+(k)), radical/set-theoretic only; not asserted in √J; no exponent or certificate | **CONFIRMED** at exactly that scope |
| 8. Negative controls kw=1 (no finite boundary arcs, yet J≠S) and h=k (boundary equation not global) | **CONFIRMED**; the over-reaching inferences are REFUTED as the producer says |
| 9. Producer checker and replay | **CONFIRMED** with two tautological gates noted (§6) |

## 1. Inputs and custody

All eleven frozen input SHA-256 values are pinned in `box/d125-arc-closure-gate-fable5-20260907/input_pins.sha256`. `replay.json` fields `code_sha256`, `report_sha256` and both `primary_snapshots` digests match the frozen bytes; the body hash `141f39e8…` was recomputed over the 6623 bytes through the BODY-END line. The transaction `f989207d…` appears only as replay.json's `manifest_sha256`; the manifest itself is not among the frozen inputs (typed **GAP-TRANSACTION**, uncharged, custody not proof authority).

## 2. Interface fit: ring and order

J=I:k^∞ is the kernel of S→(S/I)[1/k], so S/J embeds in (S/J)[1/k]=(S/I)[1/k]. Hence k is a nonzerodivisor on S/J, every associated prime of S/J avoids k, and every generic point of every irreducible component of X lies in U=D(k). So U is dense in X and X is the schematic closure of D(k)⊂Spec S/I, exactly as stated. Coordinate convention: A_(i,j)=[gⁱpʲ]A, consistent with the parity-normalization table (A_(2,1)=g²p=k, B_(8,5)=g⁸p⁵). The four coordinates A_(0,13), A_(0,3), B_(0,3), B_(0,15) are genuine free odd slots inside the polygons (5i−7j≤3, i≤2j for A; 5·Newt₀(S) for B), below the total faces, so H,D are elements of S. Including the optional B_(0,15)=0 gauge row in I is compatible with 14f (its exact condition β=−[p¹⁵]R_t⁵ = 243 at t=−3).

## 3. Arc existence and completion (primary sources read whole)

Stacks Lemma 32.15.1 (statement and proof read from the frozen 0CM1 snapshot): f:X→Y finite type, Y locally Noetherian, y in the closure of f(X) ⇒ a DVR A with Spec A→Y sending the closed point to y and Spec K→X, K=Frac A, landing at a generic point η of a component of X with K=κ(η). The producer applies it with f = the open immersion U→X, Y=X. U→X is finite type (open immersion of a Noetherian scheme is quasi-compact), X is Noetherian (finite type over Q), and every q∈X∩V(k) is in the closure of U by §2. The proof in the snapshot (Morphisms 29.6.5 for a specializing point, Krull–Akizuki 10.119.13 for the DVR) requires nothing further. The lemma applies to any scheme point q, not only geometric points; that only widens the producer's wording. Composing S→S/J→A: k∈A; k vanishes in the residue field of A because the closed point maps to q∈V(k); k≠0 in A because Spec K lands in D(k). So k=s^m·(unit), m≥1, and every S-coordinate is an element of A ("finite coefficients"). No properness of X→A¹ and no compactification is used; the producer states this correctly.

Completion: A→Â is injective (Krull intersection), Â is a complete Noetherian regular local ring of dimension 1 containing Q. Stacks Lemma 10.160.10(1) (frozen 0C0S, statement and proof read, including the clipped sentence "injective because otherwise the dimension of R would be <d by Lemma 10.60.13") gives Â≅L[[s]] over its residue field L⊇Q. All rows of I are polynomial identities in the coordinates, hence hold in A and in L[[s]]; k is invertible in L((s)), which is exactly how 14p and 14q interpret the guard. Nilpotents of S/J are killed by S/J→A, which is why (C) can only be radical. Fit is exact.

## 4. Parameter change to the literal k=τ^m of 14p

14p is stated for k=s^m literally; its Fable gate note N1 flagged that absorbing a unit needs an m-th root of u₀ and a parameter change. The producer supplies exactly that: extend L to L'=L(v₀), v₀^m=u₀ (finite; the arc base-changes along L[[s]]⊂L'[[s]]); solve v(s)^m=u(s) coefficientwise, the s^n pivot being m·v₀^{m−1}≠0 in characteristic 0; set τ=s·v(s), which has linear coefficient v₀≠0 and therefore a formal compositional inverse s=s(τ). Substitution s↦s(τ) is a continuous L'-algebra isomorphism L'[[s]]→L'[[τ]] fixing constant terms. Therefore every polynomial row still holds, the center (constant terms) is unchanged, the finitely many (g,p)-monomial supports are unchanged, and k=τ^m. 14p then applies with K=L' and excludes centers with t₀+3≠0. 14q needs no change: it admits any k(s) of positive order over K[[s]]. CONFIRMED; correctly declared as a field extension plus parameter change.

## 5. Boundary coefficients and the radical statement

The center (τ=0) is an L'-point of Spec S/(I+(k)) since I⊆J, so 14f classifies it: A₀=R_t³+αR_t, B₀=R_t⁵+βR_t³+γR_t. Own exact control (`gate_controls.py`): the pure-p part of R_t is p⁵+tp³−(t+3)p (g-monomials never reach a pure-p slot), and [p¹³]R_t³=3t as a polynomial in t (multinomial 3 from two p⁵ and one tp³), while deg R_t=5<13 kills αR_t. So H=t+3 at every k=0 field point; by 14p, t₀=−3 at the center, so H vanishes at the L'-point over q, hence at q (κ(q)→L' is injective). At t=−3 the exact symbolic projections are y=−3α, w=−3γ, v=−243+β ([p¹⁵]R₋₃⁵=(−3)⁵=−243 from five −3p³ factors, [p¹⁵]R³=1, [p¹⁵]R=0, [p³]R⁵=[p³]R³=0 by origin order 3), and D=5y²+27(v+243)y−27w=45α²−81αβ+81γ=81Δ₀ as an exact polynomial identity in (α,β,γ). 14q gives Δ₀=0 at every t₀=−3 center, so D(q)=0. The v=0 gauge is β=243, giving 5y²+6561y−27w (27·243=6561); dropping the 243 shift is a real changed object (own and producer mutation both fail). H and D vanish at every point of V(J+(k)); the radical is the intersection of the primes containing J+(k), so H,D∈√(J+(k)) with no Nullstellensatz needed. Neither H nor D is claimed in √J, no exponent is given, and the conditional y,w sentence (tuned theorem) is correctly left uncharged. CONFIRMED.

## 6. Negative controls, producer checker, own controls

kw=1 in Q[k,w]: J=I=(kw−1) (k already a unit mod I), 1=k·w−(kw−1) gives J+(k)=S, while (2,1/2) shows J≠S. So excluding every finite boundary arc proves only X∩V(k)=∅, i.e. k a unit on S/J, never J=S or properness of I+(zk−1). h=k in Q[h,k]: h∈√(J+(k))=(h,k) but h∉J and h=2≠0 on U; the boundary equation cannot be added to the k-nonzero solver input. Both inferences are REFUTED exactly as the producer says; these are toys, not Keller points. Producer `check.py` was replayed here from the frozen copy (`producer_check_replay.txt`): normal and −O PASS, the three mutations fail at the named gates, matching replay.json. Notes, uncharged: the gates `(0−0)==0 and (2−2)==0` and `1==k*w` are tautologies and not evidence; the multinomial and D=81δ gates are substantive. Own `gate_controls.py` (SHA `f2d65a84…`, stdlib, `-B` and `sys.dont_write_bytecode` first, RLIMIT 25 CPU s / 512 MiB, timeout 30, zero Assert nodes) expands only (p⁵+tp³−(t+3)p)^{3,5} and cubic symbolic products; witnesses `out.json`=`out-O.json` (`53cfb364…`); mutations `--omit-243`, `--gamma-sign`, `--claim-global-h`, `--drop-tp3` fail at the named gate in both modes (`run_log.txt`, `own_artifacts.sha256`).

## 7. Remaining global gap and FALLACY-v2 check

The composition constrains only the reduced k=0 boundary of the k-saturated closure. It cannot decide U: components on which k is a unit (kw=1 pattern), coefficients escaping to infinity, and any non-finite degeneration are untouched, and no theorem forces a guarded point to admit a finite-center arc. The tuned α≠0, Δ₀=0 and pure α=γ=0 strata remain open, so y,w are not in the boundary radical here. Typed gaps, none charged: GAP-TRANSACTION (§1); external-theorem trust inherited from 14f/14p/14q (Arzhantsev–Petravchuk, Stacks). FALLACY-v2: floor/attainment respected (radical only, no membership exponent claimed); no `sat()` or CAS wrapping, the saturation is defined algebraically and both toy controls are positive/negative; ring map, generator convention and coefficient field declared; no exit claim, so no charge basis. **Overall: CONFIRMED at the stated PROVISIONAL scope; no promotion beyond (C). STOP/IDLE.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10495`.
- Body SHA-256:
  `869fc4c4553021847c207bca360142d0b97a6ea5d0d7405e4775381cd5e621dd`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
