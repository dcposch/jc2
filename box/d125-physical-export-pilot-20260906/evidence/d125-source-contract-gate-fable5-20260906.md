# Bounded independent D125 original-source acceptance gate

2026-09-06. Gate lane (Fable 5.1), bounded 35 minutes, deadline 14:58 UTC. Charged producer: `xmodel/d125-client-interface-astra-20260906.md` (file SHA-256 `0c5270a432a6336c17c4693034e36cb496f139c3267843e3ac06628ec8c4b255`; body-through-marker SHA-256 `050fcbf8a1bac26bf8f35b518651afa18c385d5ffd448663f408773bc44b7d65`, 17,229 bytes, both recomputed here) plus its `box/d125-client-interface-20260906/` controls, inputs and public snapshots. Status: **PROVISIONAL CONTRACT GATE; NO SEARCH, NO OPENNESS/COVERAGE, NO PROPERNESS CLAIM**. Everything below concerns the *sufficient* direction of one exact chart. An empty chart's necessary direction is a different interface and is not gated here.

## 0. Verdict summary

| Arrow | Verdict | First missing hypothesis (for any use beyond the arrow) |
|---|---|---|
| 1. Finite supports, jets, five normalizations define actual `P,Q`; `Phi` injective; untranslate-first image test; chart `t=XY, z=Y^-1` bracket `-z`; layers `40..-200`, target `X^4`, sign, factor 5 | **CONFIRMED** | none for the identities; the chart choices (root 1, halfspaces `3/5`, band ceilings `15/25`, five scalars) are selections whose exhaustiveness is neither claimed nor needed |
| 2. All exact bracket coefficients + `Z*P_15_15*Q_25_25-1` imply ordinary `J=1/5`, exact degrees `75/125`, hence non-automorphism; no lower-polygon coverage theorem needed | **CONFIRMED** (sufficiency theorem, conditional on a point existing) | properness of the ideal is unknown and not claimed; the automorphism degree-divisibility theorem is an external citation; the public classifier digests rows and does not list them, so a client must regenerate every row from the formula |
| 3. Transformed rows generate exactly the ordinary coefficient ideal of `H=J(P,Q)-1/5` under the same guards; `4572` is arithmetic; counts `706+1901`, `53+136` | **CONFIRMED** | no actual nonzero-row count, term growth or runtime was measured by anyone; the `41,685` vs `4572` comparison is index bookkeeping only |
| 4. Moh `M2=90/105` parents, `(25,15;21;2;k=2)` receiver, Strinz carrier, Roy source charts kept distinct; no reverse lift or coverage import; HTTP success is not a digest | **CONFIRMED** (bookkeeping) | any composition needs the unbuilt Strinz map, a reverse Moh lift, and an `M2=90` versus `105` identification, none supplied |

Later measured source-preserving importer: **logically ELIGIBLE** under the conditions in Section 7. This is not launch authority.

## 1. Read scope and execution discipline

Read whole: the producer report, `controls.py`, `inputs.json`, `strinz-THEOREMS.md`, `roy-frontend.py`, `roy-MODIFIED-CHART-BRIDGE.md`, `FALLACY-v2.md`. Read in part: `roy-classify.py` lines 1–130 (`Band`, `make_band`), 184–380 (`band_record`, `digest_linear_constraints`, `classify_layer`), 3849–4050 (`build_payload` setup and schema), plus greps; `roy-DERIVATION.md` lines 150–240, 1327–1360, 1495–1525 plus greps; `row2515-order-gate-sol56-20260903.md` lines 1–140 plus greps. Not read or run: Roy's intermediate audit functions, the 4.27 MB public JSON (not downloaded), Strinz's Theorem A proof bundle, any live peer report, code, log, or D108/K16 gate.

Execution: one own script, `box/d125-source-contract-gate-20260906/gate_controls.py` (SHA-256 `25d04a93cf7fbb621ec0600ae91077c5757206596b53cf1eb9a1bd87c682ad3b`), stdlib only, exact `Fraction` arithmetic, run under `ulimit -v 524288` and `timeout 30`; elapsed 0.5 s; output `gate_controls.json` (SHA-256 `fc978008958fd188e741f5bb2149e0f10181b2e0c43e553c799aca2b59d86ea7`). Its verified checks raise explicitly through a `check()` helper, so they are not erased by `-O`; the producer's `controls.py` uses bare `assert` statements and was read whole and replayed in normal mode only (Section 6). No AWS, CAS, solver, shared ledger or tool edit, `jc2-lean`, or external post. No live D108 Euler result was used and no source support was trimmed.

## 2. Arrow 1 — source supports, injectivity, chart bracket, layer range, sign and factor 5

**Supports and actual polynomials.** The P support is `{(i,j): i,j>=0, i+j<=75, 5i-j<=15}` and the Q support `{i+j<=125, 5i-j<=25}`. Any assignment of the `706+1901=2607` coefficients over any field defines actual `P,Q` in `k[u,v]` of degrees at most `75` and `125`. The terminal jets are linear rows in those coefficients and the five normalizations are affine rows; they only cut the linear parameter space. Per band `ell=5i-j` the index range `max(0,ceil(ell/5))<=i<=floor((75+ell)/6)` is exactly `j>=0` and `i+j<=D`; every band `-75..15` and `-125..25` is nonempty (my direct double loop over `(i,j)` returns the same 91 and 151 bands).

**Injectivity of `Phi`.** `Phi(u)=X^5`, `Phi(v)=Y+X^-1` is a ring map `Q[u,v] -> Q[X^±1][Y]`. For `sum_j a_j(u)v^j` with `a_top != 0`, the image has leading `Y`-coefficient `a_top(X^5) != 0`, so the kernel is zero. The inverse on the image is untranslation `Y -> v-X^-1` followed by `X^5 -> u`. My control shows both failure modes of the wrong test: `Phi(v)=Y+X^-1` is in the image but has X-characters `{0,4}` before untranslation, while `X^5*Y` has only trivial characters before untranslation and is *not* in the image (untranslated it contains `-X^4`). Roy's frontend `terminal_kummer_characters` is a statement about `k[X^5,Y]` membership of the translated terminal block, not an image test; the producer's "untranslate first" is the correct reading.

**Chain rule and sign.** `det d(u,v)/d(X,Y) = 5X^4 * 1 - 0 * (-X^-2) = 5X^4`, so `J_(X,Y)(Phi P,Phi Q) = 5X^4 Phi(J_(u,v)(P,Q))`; bracket `X^4` means `J=+1/5`. Verified on random rational `P,Q` by literal substitution; the sign-flipped and factor-1 mutations are detected.

**Chart.** `t=XY`, `z=Y^-1`: `det d(t,z)/d(X,Y) = Y*(-Y^-2) - X*0 = -z`. Hence `J_(X,Y)(F,G) = -z * J_(t,z)(F,G)`, verified on the random images. Exponent matrix `[[1,1],[0,-1]]` has determinant `-1`, so `Q[X^±1,Y^±1] = Q[t^±1,z^±1]` and coefficient identities transfer exactly. `Phi(u^i v^j) = X^(5i)(Y+X^-1)^j = t^ell(1+t)^j z^ell` with `ell=5i-j`, verified by substitution on a `6x8` grid. For `p=t^ell(1+t)^j`, `q=t^m(1+t)^s`: `ell*p*q' - m*p'*q = (ell*s-m*j) t^(ell+m)(1+t)^(j+s-1)` and `ell*s-m*j = 5(i*s-k*j)`, the ordinary monomial Jacobian multiplier times the ramification factor; verified on seven index quadruples including `j+s=0` (multiplier zero, no negative binomial power).

**Layers.** `L=ell+m` ranges over `[-75,15]+[-125,25]=[-200,40]`, 241 layers; the target `X^4 = t^4 z^4` lives on layer 4 only. The six bottom layers `-200..-195` carry no row at all (every contributing pair has `i=k=0`), so 235 layers have rows; this is consistent with "retain every nonzero coefficient of the literal difference".

**Pinned public code against the contract.** `make_band` uses `source_i_min=max(0,ceil(ell/5))`, `source_i_max=(D+ell)//6`, `t_exponent_min=max(ell, ceil((17*ell-h)/12))`, `jet_order=t_exponent_min-ell`; on all 242 bands this equals the producer's `r_ell=max(0,ceil((5*ell-h)/12))` (checked band by band). `build_payload` builds `P` bands `-75..15` with `(75,3)`, `Q` bands `-125..25` with `(125,5)`, asserts `706/653/1901/1765`, fixes the five normalizations `P_3_t4=1, P_15_t21=1, Q_1_t1=-1, Q_13_t18=-3, Q_25_t35=-9/5`, and runs `classify_layer` over `range(40,-201,-1)` (241 layers, `rhs` `t^4` at layer 4 else `0`). `classify_layer` enumerates every `(ell,m)` with `ell+m=L`, multiplier `p_layer*q_power - q_layer*p_power`, generator degree `j+s-1`, exactly the contract. These five normalization slots are the frontend's `(4,1),(21,6),(1,0),(18,5),(35,10)` in `(X,Y)`, i.e. `t^4 z^3, t^21 z^15, t z, t^18 z^13, t^35 z^25`; each is the first post-jet coefficient of its band, and the exact rank of jets plus normalization row is `2,7,1,6,11` on `13,13,21,21,21` columns, so all five affine systems are consistent. Roy's normalized terminal edge `P=X^4 Y(1+s)`, `Q=-X(1+3s+9/5 s^2)`, `s=X^17 Y^5` has bracket `X^4` in my own arithmetic.

## 3. Arrow 2 — full guarded contract implies an ordinary Keller pair of exact degrees 75/125

Let `I` be the ideal in `R=Q[alpha, beta, Z]` (2607 source coefficients and `Z`) generated by: the 189 jet rows; the five normalization rows; for every `L=-200..40` every `t`-coefficient of `sum_(ell+m=L)(ell*p_ell*q'_m - m*p'_ell*q_m) - delta_(L,4) t^4`; and `Z*alpha_(15,15)*beta_(25,25)-1`.

Suppose `I` is proper. By the weak Nullstellensatz there is a `Qbar`-point. Define `P=sum alpha_(ell,i) u^i v^(5i-ell)`, `Q` likewise; these are actual polynomials of degrees at most `75,125`. The bracket rows say `J_(X,Y)(Phi P,Phi Q) = X^4` as an identity in `Qbar[t^±1,z^±1] = Qbar[X^±1,Y^±1]` (Section 2). By the chain rule `5X^4 Phi(J(P,Q)) = X^4`, so `Phi(J(P,Q)-1/5)=0`, and injectivity gives `J(P,Q)=1/5`. The guard forces `alpha_(15,15) != 0` and `beta_(25,25) != 0`; these are the coefficients of `u^15 v^60` (total degree 75) and `u^25 v^100` (total degree 125), so the degrees are exactly `75` and `125`. The characteristic-zero automorphism degree-divisibility theorem (Jung–van der Kulk / Abhyankar–Moh: for an automorphism one degree divides the other), cited and not re-proved, excludes an automorphism since `75` and `125` do not divide each other. Hence a point of `I` is a Jacobian counterexample. No lower-polygon, gamma-branch or coverage theorem enters; those belong to the converse.

Root warning respected: the bounds plus guard do not force a unique total-leading monomial. `v^75` sits on band `-75` with jet order 0 and is a free coordinate, so `P`'s degree-75 form can contain it. The argument above uses only "some degree-75 monomial has nonzero coefficient", never a leading-form statement.

Explicit non-claims, confirmed against the code: the public artifact is a specification. `classify_layer` hashes each contribution (`digest.update(f"{layer}:{p_layer}:{q_layer}:{p_i}:{q_i}:{factor}:{generator_degree}")`) and stores counts and intervals; it retains no literal scalar equation. `digest_linear_constraints` likewise digests jets and normalizations. Nothing in this gate verifies the public builder, the v9 JSON, the B0 survivors, the modified projection, or any truncation; the sufficiency theorem applies only to the full guarded row set regenerated from the definitions. The strings `P_15_15` and `Q_25_25` occur nowhere in the pinned classifier, derivation, or frontend (grep count 0 in all three), so the degree guard is the producer's explicit addition; Section 6 shows it is not implied by the linear rows.

## 4. Arrow 3 — transformed rows generate exactly the ordinary coefficient ideal of H

Write `H=J_(u,v)(P,Q)-1/5` with coefficients `h_(I,J) in R`. The transformed residual is `J_(X,Y)(Phi P,Phi Q)-X^4 = 5X^4 Phi(H)` (using `Phi(1/5)=1/5`); its `(t,z)` coefficients are `c_(e,L)`. Since `5X^4 Phi(u^I v^J) = 5 t^L (1+t)^J z^L` with `L=5I-J+4`, layer `L` of the residual is `sum_J 5 h_(I(J),J) t^L (1+t)^J`, so

- forward: `c_(e,L) = 5 sum_J binom(J, e-L) h_(I,J)` over `J ≡ 4-L (mod 5)`, an integer combination, hence `(c) ⊆ (h)`;
- inverse: with `s=1+t`, `t^-L g_L(t) = sum_J 5 h_J s^J`, so `h_(I,J) = (1/5)[s^J](t^-L g_L)(s-1) = (1/5) sum_(e>=L+J) (-1)^(e-L-J) binom(e-L,J) c_(e,L)`, the producer's formula, hence `(h) ⊆ (c)`.

Both maps have constant rational coefficients independent of the parameters, so the `Q`-spans of the two generating sets coincide and the ideals are equal in the polynomial ring `R` itself: no radical, no localization, no parameter pivot, no reduced-scheme step. Supports are finite on both sides. Jets, normalizations and guard are retained verbatim. My control builds a random 23-term nonzero `H`, transforms it by substitution (76 residual coefficients), recovers every `h_(I,J)` by the inverse formula and independently by "divide by `5X^4`, untranslate, read", checks the forward formula on every `c_(e,L)`, and rejects the sign-flipped and unscaled inverses.

Counts, recomputed by loops that do not use the band parametrization: P `706` coefficients, `53` jet rows, `653` dimensions on `91` bands; Q `1901`, `136`, `1765` on `151` bands; `2607` total, `2418` after jets, `2413` after the five normalizations, `2414` with `Z`. The jet matrices have full rank on every band. The physical index bound `#{(I,J): I,J>=0, I+J<=198, 5I-J<=36} = 4572` by direct enumeration (degree `75+125-2`, weight `40-4`). As a bonus, iterating the multiplier over all `706*1901` coefficient pairs reproduces the advertised public metadata exactly: `13,741` band-pair incidences, `1,327,026` active generators, `41,685` raw scalar row slots (six layers empty). That confirms the advertised counts follow from the stated formula; it does not verify the artifact's bytes, and no nonzero-row count, term growth, elimination cost or runtime was measured by the producer or here.

## 5. Arrow 4 — object distinctness; no reverse lift or coverage import

The producer's table keeps five objects apart, and I find no leakage between them:

- **Moh parents.** Two `(n,m)=(125,75)` numerical survivors, `M2=90` and `105`; the latter with `M=(-75,105,123)`, `d=(125,25,5,1)`, `V=(2,4,1)`, as in the row2515 gate. Census data, not coefficients.
- **Receiver `(25,15;21;2;k=2)`.** Obtained from `M2=105` by Proposition 6.3 with `u_s=1` (Proposition 6.4 minor radius), `J_(gamma,pi)=c*gamma^2`. The row2515 gate accepts only the parent-to-receiver direction; no reverse lift with polynomiality, original degrees, Jacobian unit and minor/pole compatibility exists in any charged input, and the producer imports none.
- **Strinz carrier.** Theorems B/C/D/E concern the normalized F2 carrier model; the ledger's non-composition statement says the map from Theorem A's output to the carrier data is not constructed. The producer quotes this and does not reprove Theorem A; neither do I.
- **Roy source charts.** `(u,v)` are coordinates of a *standard* pair after Theorem A's automorphism over `Kbar`, then `x=X^5`, translation root scaled to 1, then `(t,z)`. The modified `(xi,v)` chart `X=xi v^2`, `Y=xi^-2 v^-7` has `d(X,Y)/d(xi,v) = -7 xi^-2 v^-6 + 4 xi^-2 v^-6 = -3 xi^-2 v^-6`, target `-3 xi^2 v^2`, exponent determinant `-3`: a degree-three torus cover, not a coordinate change, matching the bridge's (5)–(6). Its projection discards tails and is not bracket preserving; nothing here transfers to or from it.

The common labels (degree 125, top multiplicities, `7/5`, `27T^2-9T+1`) supply no map, and the producer asserts none. The receiver's `h` top has total degree 5 while the public common polynomial has degree 25; no `R`-root-to-`M2` identification is claimed. Public availability: the v9 JSON returned HTTP 200 with 4,266,557 bytes at 14:06 UTC per the producer's manifest; its advertised SHA remains an author claim, and I did not download it either. Nothing in this section is a coverage, reduction or lower-bound statement.

## 6. Independent control and mutation

Own script, all checks fail closed (Section 1 for hashes and caps):

1. **Principal mutation, guard independence.** On P band 15 (13 columns, 6 jets plus the `[t^21]p_15=1` row) and Q band 25 (21 columns, 10 jets plus `[t^35]q_25=-9/5`), the exact rank is `7` and `11` both with and without the endpoint column, so `alpha_(15,15)=0` (resp. `beta_(25,25)=0`) is consistent with every linear row. The five normalizations do not imply the degree guard; it must be adjoined explicitly, as the producer does. A toy pair `(u+v^2, v/5)` with `J=1/5` passes a guard on nonzero slots and is rejected when the guard names a zero slot (the row becomes the unit `-1`).
2. Untranslate-first: `Phi(v)` accepted only after untranslation; `X^5 Y` rejected only after untranslation.
3. Chain rule, chart bracket `-z`, band formula, bilinear multiplier: substitution route agrees; sign and factor mutations detected.
4. Inverse formula on a nonzero 23-term `H`, both containments, two mutations rejected.
5. Scalar recounts `91/706/53/653`, `151/1901/136/1765`, `4572`, and the public metadata triple.

Producer's `controls.py`: read whole; replayed in normal mode from the read-only lane copy (result in Section 7's log line); it uses bare `assert`, so it certifies nothing under `-O`, and it contains no ideal, witness or solve.

## 7. First missing hypotheses and importer eligibility

- Arrow 1: nothing missing for the identities. The chart selections are not shown exhaustive and need not be for sufficiency.
- Arrow 2: **properness is unknown**; a point has not been exhibited by anyone. The automorphism degree criterion is an external citation. Any client must regenerate all rows from the definitions because the public record stores digests, not rows.
- Arrow 3: nothing missing for ideal equality. Missing for any performance statement: a measured nonzero-row count and elimination cost; not claimed.
- Arrow 4: missing for any composition: the Strinz Theorem-A-to-carrier map, a reverse Moh lift, and an `M2=90` versus `105` identification; none is claimed.

**Importer eligibility.** A later measured source-preserving importer is logically eligible if it (a) declares the same 2607 source coefficients plus `Z`, the 189 jets, the five normalizations and the explicit guard; (b) emits the ordinary coefficients of `H=J(P,Q)-1/5` (at most 4572 slots) or, equivalently, the full 241-layer transformed rows, without truncation, projection or tail deletion; (c) treats a returned point as a counterexample candidate to be re-verified by direct ordinary differentiation and degree reading; and (d) reports emptiness only as emptiness of this chart. Emptiness would not exclude `(75,125)` without the coverage interface (Theorem A at its tier, lower Newton boundary, normalization exhaustiveness), which is a different gate. No global 125 lower bound, full-case necessity, full-builder verification, properness or speedup is promoted here.

Producer control replay (normal mode, read-only lane copy):
`controls.py` exit 0, status PASS, 12/12 checks true, `physical_J_row_bound` 4572; replay output kept outside the report. Elapsed for this whole gate: 14:21–14:32 UTC.

<!-- BODY-END -->
