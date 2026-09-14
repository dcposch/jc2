# D108 literal source → GGHV interface; independent C-rank portability

Evidence: exact small source/coordinate checks and proofs below. Lifecycle: **PRODUCER-CHECKED / PROVISIONAL pending a different-model gate**. This is post-12:10-round work, not an addition to that sealed blind round. No mathematical point, properness, source-configuration exclusion, or JC2 claim is made.

Outcome: the literal D108 source matches substantially more of GGHV's starting geometry than its `(8,28)` label: it gives the standard-pair degree ratios, the complete starting weighted edge, and an explicit q=4 homogeneous auxiliary. A complete two-branch coefficient transport is **not yet instantiated**. Separately, the actual D108 C-space supports the uniform full-C rank191 theorem and the abstract W190 constant-pivot lemma. The map gap does not erase those source-valid statements.

## History and exact input boundary

At 2026-09-06T12:27:14Z the history checksums were:

| File | SHA256 |
|---|---|
| APPROACHES.md | `46147a6af9775156efd5a22f3175f36546c9a7a943cc0a561cfdf4664cf2626d` |
| AUDIT.md | `0bcbd9a45262fbaaf75d8f882c859ec2463253520112a238e650575508c0b151` |
| ladder/REDUCTION.md | `7f901db6c8e6fbc80c85581a331c247d5c219e23bf286136f77fbc0182ebbe1b` |

The relevant history already separates exact exclusion of the two explicit GGHV systems from the conditional reduction/transcription bridge. `jc72108/CROSSCHECK.md` records the earlier external exact-certificate route; this task does not replay those large artifacts or revive superseded msolve-header claims. `ladder/REDUCTION.md` distinguishes standard pairs from globally minimal pairs and warns against universal use of Proposition 4.3.

Literal source: `box/char-degree-20260905/d108/selected/meanfree_stage8_slimgb/d108_meanfree_stage8_strongfront.input.json`, SHA256 `1c927d83aa4684ae91bfffc8d03500fbabb73a500faa222fa349a6d129a10814`. Its 14 residual strings are retained in exact original order in `source_interface.json`, with individual hashes and sequence SHA256 `d527f88903c747b1d888e71d5dfad8a62861082465499aaff94c2d08c4d3a4d9`. They are **not** replaced by their radical or silently omitted.

The pinned direct-builder code is `box/t2t3-direct-20260906/build_direct.py`, SHA256 `77ef23b86f655e08a11913cf838a037c82adbb89cd1bc4a7e86c6471d034be3e`. The one-way full-ideal→Keller gate is `xmodel/full-ideal-counterexample-gate-fable5-20260906.md`, SHA256 `5fc61ae7f4f78e7d28cde6ac3eaa7c24e7ca98966ebf94de7cbaf5ea69fb059e`. The gate is consumed for that direction only; no converse necessity of the source chart is inferred.

The primary GGHV v1 PDF/text pins are `ac18e80cc2391f204f73b908a6a6557eb1141d9fbb5ebdb9f6e0a22121db80bd` and `f3eca2a560b98784ec787104c8b9049ca44bc3dde4bacb38f121376736d02368`. Proposition 4.3, pp. 10–12, was read directly. For the distinction between standard/minimal and the actual first auxiliary hypotheses, the local GGV1 primary text was read at Definition4.3, Theorem2.6, Corollary7.4 and Proposition8.2; its SHA is `e3694dde3f83c2ab6ed8d957fc6b53472e6a6dd55486af1dff345eade39e37b1`. No live 12:10 cross-report body or log was read.

## Rings, order, and honest polynomial degrees

Physical coordinates are `X=x_old`, `W=y_old−x_old`. A normalized coefficient `e tt^r zz^z` for normalizer N becomes `e X^(N−r−z)W^z`. All exponent/nonnegative-support and symbol checks passed. Coefficients are rational polynomials in the declared source names; there are no variable denominators.

| Object | Normalizer | Physical slots | Minimum r | Honest total-degree bound |
|---|---:|---:|---:|---:|
| h | 36 | 185 | 0 | 36 |
| D | 71 | 191 | 34 | 37 |
| C | 107 | 197 | 69 | 38 |

Every h,D,C monomial has X exponent at most eight and `4*X_exponent−W_exponent<=4`. The only X^8 term of h is `X^8W^28`, coefficient one. Also `h_top=(X+W)^8W^28` exactly, independently of every parameter and every residual equation.

With `a=target_a`, `b=target_b`, define the actual source polynomials

`F=h³+(3D+a)h/2+C`, `G=h²−bh/3+D`.

Then `deg(F)=108`, `deg(G)=72` at every semantic base point. Corrections have degrees at most 73 and 37, respectively, strictly below the leading powers. No F or G expansion was built to establish this. The factored-J identity also bounds the raw physical Jacobian by total degree108, but no D108 full-J stream was generated here.

The frozen source has 502 named coordinates. The complete direct ring is Q in `sorted(set(names)∪{Zc})`, followed by `t3eq,t3_fgq,t3_fq2,lambda3,Z3`: 507 coordinates, order SHA `4c8952648ab814be891a76e4b0fc8b2f650ccf0689ebfba882a96ac2a83f1ad4`. The complete ideal retains all 14 residuals, all T2/T3 equations, and `Z63*leader63−1`, `Z3*lambda3−1`, `Zc*c−1`. Here c is minor separation, **not** `target_c`.

The actual frozen builder order is: sorted T2 upper/R-high rows; source residuals0…13; sorted T2 strict then face/support traversal; T3 equality; sorted T3 strict; T3 face; then the three inverse rows in T2,T3,separation order. The previously reviewed completion-count assertion defect remains a builder defect, not a new validated full output. This task did not run the builder.

## Exact portion of the GGHV interface

Set `A=X+W`, `B=W`, equivalently `X=A−B,W=B`; the determinant is one. The unique highest-X slot implies, without expanding F/G,

`ell_(1,0)(F)=A^24B^84`, `ell_(1,0)(G)=A^16B^56`.

Thus at every actual Keller point the ordered pair `(F,G)` is a **standard (3,2)-pair in the literal sense of GGV1 Definition4.3**: both degree ratios are3/2, and the two st/en points on each (1,0)-face coincide, giving `v_(1,−1)(24,84)=−60<0` for F. This does not prove global GGV minimality, but neither Definition4.3 nor the literal Corollary7.4 assumptions automatically require that extra condition.

The frozen weight-(4,−1) h face is exactly

`H=X(XW^4−1)^7`.

Changing X to A−B preserves its highest-weight part, so F/G have faces `[A(AB^4−1)^7]^3` and its square, with attained normalized endpoints `(1,0),(8,28)`. This is a complete edge identity, not an inference from the top form. After swapping A,B, it is `y(yx^4−1)^7`.

The six-term polynomial

```text
E = 2048 X^6W^21/3315 −3584 X^5W^17/1105
    +448 X^4W^13/65 −112 X^3W^9/15 +21 X²W^5/5 −XW
```

satisfies `J(E,H)=H` exactly. Hence `J(E/m,H^m)=H^m`; E has weight3 and far endpoint `(6,21)=(3/4)(8,28)`, or `(21,6)` after the swap (with sign corrected for the bracket). These are the concrete q=4 auxiliary data used at the beginning of Proposition4.3. GGV1's homogeneous uniqueness statement applies because the corresponding one-variable face has multiple distinct factors; alternatively this report only needs the explicit displayed auxiliary identity. Endpoint sets are stated explicitly to avoid confusing the papers' st/en ordering conventions.

The final major-edge cut parameter is fixed at1 in these normalized coordinates:

`[y(yx^4−1)^7]_(y→y+x^−4)=x^28y^8+x^24y^7`.

Earlier x^−2/x^−3 shifts have lower (−1,4) weight and do not change that edge. The unresolved part concerns the **other** boundary, its root cuts, and successor-tail classification.

## Both branches, Jacobian chain, and first remaining gap

For any coefficient-field parameters ell2,ell3,ell4, the fixed linear change, swap, Laurent shears and final inversion compose to the exact partial map

```text
T(X)=x^4 y+ell2*x²+ell3*x³+ell4*x^4−x^−1,
T(W)=x^−1.
```

Its coordinate Jacobian is `x²`. It is an isomorphism between the appropriately localized rings `K[X,W,W^−1]` and `K[x,x^−1,y]`, not an automorphism of the polynomial plane. The final operation by itself sends `(x,y)` to `(x^−1,x^4y)`, with Jacobian `−x²`; it is involutive on the Laurent ring. The swap accounts for the other minus sign.

If the input has `J(F,G)=j∈K×`, use **ordered** output `P=T(G)`, `Q=−T(F)/j`; then `J(P,Q)=x²`. The j inverse is justified only on the Keller locus; it is not a gauge setting j=1 in the source chart. Splitting edge polynomials may require passing to an algebraic closure. Choosing roots is not a globally rational coefficient map.

The final monomial map is `(i,j)→(4j−i,j)`. It maps the paper's terminal pre-polygons exactly as follows:

| Branch | Pre-inversion P / Q additions | Final P / Q polygons |
|---|---|---|
| Smaller, Prop4.3(2), paper cases a/b | P:`{(−1,0),(0,0),(56,16),(48,14)}`; Q:`{(2,1),(0,0),(84,24),(72,21)}` | P:`{(0,0),(1,0),(8,14),(8,16)}`; Q:`{(0,0),(2,1),(12,21),(12,24)}` |
| Larger, Prop4.3(1), paper case c | Add P:`(32,8)` and Q:`(48,12)` | Add P:`(0,8)` and Q:`(0,12)` |

Every nonorigin vertex coefficient must be nonzero to assert equality of Newton polygons; the larger branch additionally requires its two extra vertices. A coefficient-system encoding must retain the corresponding product-inverse constraint. Origin coefficients may remain free under the conservative convention. The single/two-root split on the preceding (1,−3) edge requires its own leading-coefficient and root-distinctness conditions; the repeated-root specialization belongs to the other branch and cannot be thrown away. Nothing identifies those GGHV root differences with the source separation c. Neither branch permits setting `minor_mean=0` or identifying it with a Laurent-cut root.

**First still-uninstantiated hypothesis/map contract: `GGV-CUT-EXHAUSTIVENESS`.** Starting from this actual source standard pair and fixed edge, prove that the opposite predecessor/edge factors satisfy the cases used in GGHV's proof, choose the allowed x^−2/x^−3 cuts (including their exceptional loci), and prove that their *whole* transformed supports and successor tails lie in and attain one of the two pre-polygons above. The published reduction may supply this after a targeted applicability review; the current packet has not certified that whole implication or supplied the remaining coefficient functions ell2/ell3. It is therefore an exact **partial interface**, not a completed source-point→target-point map. It does not assert that GGHV is false or that a new mathematical obstruction beyond its proof is necessary.

An ambient support mismatch is not a counterexample on the residual locus. For example the leading B^33 coefficient of `h(A=0,B)` is `L=−K2c_3_26+8*jet0*jet1−8*jet2`, and source residual0 is exactly `L²`. Hence L vanishes at field points satisfying that residual, though it need not vanish scheme-theoretically. We explicitly did not treat its ambient nonzero expression as refuting the interface.

Direction remains crucial: a complete source-ideal point gives an actual Keller pair by the earlier one-way gate; a correctly transported pair could then feed the old GGHV polygon exclusions. Conversely, neither a target polygon point nor a standard-pair numerical match gives a source-chart point. No global-minimality replacement preserving this literal source pair was assumed. History suggests auditing this narrow existing-proof interface before commissioning another D108 solve.

## Separate exact scoped result: full-C191 and W190 port

The actual C-space has dimension192, with197 slots and an exclusive coefficient-one identity slot for each of its192 parameters. All 14 residuals are independent of **every** C parameter. h and D are also C-independent. The source has

```text
h(X,0)=eta−X,                 eta=K2c_36_0,
D(X,0)=d1 X+d0,              d1=B2c_70_0, d0=B2c_71_0,
C(X,0)=beta X+gamma,
beta=(2/7)A3c_96_8+(3/35)A3c_86_16+(8/35)A3c_91_12,
gamma=A3c_107_0.
```

Consequently `G(X,0)=X²+(−2eta+b/3+d1)X+eta²−b eta/3+d0` is monic quadratic at **every** base point, including specializations of the residual quotient. C has degree at most38 and W exponent at most35. Its degree36 W exponents are exactly28…35; W^36 is absent globally.

For a nonconstant `P∈V_C` with `J(P,G)=0`, the characteristic-zero common-polynomial theorem gives `G=phi(R),P=psi(R)` (Arzhantsev–Petravchuk, arXiv:math/0608157, Lemmas4–5, as used in the prior source-rank report). Restriction to W=0 forces `deg(phi)` to divide2. Degree one gives `deg(R)=72`, impossible for nonconstant P of degree≤38. Degree two gives `deg(R)=36` and `deg(psi)=1`. Then `R_top` is a nonzero scalar multiple of `h_top=(X+W)^8W^28`, with a nonzero W^36 term, impossible in V_C. Thus the full coefficient map `C→J(C,G)` has kernel exactly the constants and rank191 at every characteristic-zero field-valued base point. This is not a claimed constant191 coefficient minor or cheap Bezout construction.

The restriction map V_C→span{1,X} has rank2. An exact fixed rational coordinate change is

`A3c_96_8=(7/2)beta−(3/10)A3c_86_16−(4/5)A3c_91_12`.

It gives a190-dimensional kernel V0 of restriction, while preserving all nonconstant tails of the actual source columns. Adapt any Q-basis of V0 by increasing W order and decreasing X degree within each order. For leading `X^iW^r`, r≥1, the selected Jacobian row `(i+1,r−1)` has coefficient `−2r`; later columns give zero there. Rescaling by `−1/(2r)` gives **190 universal constant positive pivots**, over any base Q-algebra. Here selected degrees are at most38 and r≤35. No concrete D108 W190 matrix or dense substitution was emitted; this is the proved portable interface, not a measured performance result.

Do not conflate the full map with the positive-only map: the latter's kernel means `J(P,G)` is constant. Only at actual Keller points does the earlier centralizer subtraction prove uniqueness for the positive `(C,a)` block modulo the additive constant: subtract `(k/j)F`, use centralizer `K[G]`, and note108 is not divisible by72. The W^36 coefficient then forces the a difference to vanish. Gamma is literally a constant column and is absent from the 14 residuals, so it is rowless for the **raw physical Jacobian plus those residuals**. This statement is not transferred to all T2/T3 characteristic rows, which can couple target constants.

## Root-suggested post-cutoff critical-jet delta

This subsection follows root's later suggestion; it is not independent blind ideation. Exact frozen W1 jets are

`h_W(X,0)=−(K2c_9_21+5K2c_4_25)X+K2c_35_1`,

`D_W(X,0)=B2c_69_1 X+B2c_70_1`.

At `x*=eta−b/6−d1/2`, the resulting critical quantity is

```text
Delta = [B2c_69_1−d1*(K2c_9_21+5*K2c_4_25)]*x*
        + d1*K2c_35_1+B2c_70_1
      = −J(h,D)(x*,0).
```

All 14 residuals are B2-independent, and Delta is monic in the independent coordinate `B2c_70_1`. Hence `Delta∈(residuals14)` iff `1∈(residuals14)`; no properness of that ideal is asserted. At a full Keller quotient, `G_X(x*,0)=0` and `j=F_X(x*,0)Delta`, so `Delta*(Zj*F_X(x*,0))=1`. This is an induced unit, not a generic localization that discards Keller components. Also `J(C,G)(x*,0)=beta*Delta`; the evaluation row kills all V0 columns and could append a last block pivot of determinant Delta to W190. No such elimination was implemented. No inverse variable was introduced here; an implementation adjoining a separate Delta inverse would add one coordinate and one inverse equation and must account for them and all residual rows.

## Controls, replay, and terminal custody

`source_interface.json` SHA `0bc1b54ffd08792074ea576fa817e979b5643c2ecfd866b65f537da3038cde36` contains every source coefficient and all14 residual strings/order. `map_controls.json` SHA `08a75d8888ff2fd17c8e443f88834cfb6eb519d1e4840b0044dbe4d456261086` verifies the partial coordinate map, both terminal polygon maps, C/residual independence, and the literal transverse line. The real polynomial Keller control `F=X+W²,G=W` transforms to bracket x² in the declared order; it is not a D108 source point. Six mutated inputs fail the actual verifier: C constant inserted into a residual, altered first residual square, changed h slope, wrong inversion exponent, reversed output sign, and an incorrect extra vertex. No control claims a full source realization.

`edge_interface.json` SHA `4d231b39741c94994b7e6b315a337afc023c987b934b447c0c8d60cb92a05ef5` records the fixed edge and Euler identity. `critical_jet.json` SHA `a068be43b43bbae55d6722825581c7a45d34d73e39e0c56511068fcdcd2ad06f` records the separate root-suggested delta.

Read-only main replay:

```sh
python3 box/d108-source-frontier-interface-20260906/replay_all.py
```

It recomputes and compares all three main JSON objects, excluding only measured seconds/RSS. Final code hashes are recorded in `custody.json`. The first replay exposed a tuple-versus-JSON-list comparison bug, not a mathematical failure; it is preserved as an exit1 harness rejection. JSON normalization repaired that comparison, and `replay2` completed with `D108_INTERFACE_READ_ONLY_REPLAY=PASS`. No charged mathematical output changed. Read-only wrappers were added after the one generation; final wrapper code was used in replay2.

All arithmetic commands were capped at30 s /512 MiB locally. Initial source inspection took1.135 s/54,940 KiB; the six-control pass11.882 s/64,908 KiB; the edge auxiliary0.135 s/49,700 KiB. No AWS action, solve, full F/G/J expansion, shared-ledger write or jc2-lean edit occurred. `custody.json` records all exact hashes, terminal PGIDs, the one typed rejected harness run, and no live writers. Source bytes and earlier charged artifacts are untouched. After transactional publication, the producer yields for root's targeted different-model gate.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17378`.
- Body SHA-256:
  `ab097e662a6f59edb7ec07423010cebb16dab904f1c19cce47be773de34eff87`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
