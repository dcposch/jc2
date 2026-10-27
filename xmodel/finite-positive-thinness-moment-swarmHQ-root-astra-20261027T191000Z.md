# A finite positive-thinness moment for a normalized plane Keller map

Producer: swarmHQ coordinator ROOT and retained Astra-role co-researcher; actual hosted model identities were not independently measured.
Date: 2026-10-27 UTC.
Basis: public `70fb69ae689bb8077e5a33a80316bbbb668f6421`; internal proof bank `422953fbd6423f09028bebf809ebc61c1b58277d`, independent review bank `8e71d5e24c83c25c074cba4eb3cdab843feabe49`.
Evidence tier: MANUAL / PASS_CONDITIONAL on the explicitly named geometric and valuative foundations below.
Lifecycle: PROVISIONAL. The independent reviewer did not co-produce the proof; different actual hosted model identities have not been attested, so no different-model promotion credit is claimed.

## Statement and scope

Let `F=(P,Q): A²_C -> A²_C` be a polynomial map with nonzero constant Jacobian and function-field degree `N`. After one target polynomial automorphism, one can choose a representative `H` of degree `d>N` with algebraically stable degree sequence `deg H^n=d^n`, such that every actual nonproper-image curve has its only point at infinity at the same regular fixed point `q` of `H`.

Write `theta = lim d^(-n) H^(n*)L` for its normalized nef pullback eigenclass. Assume the FRAME, THIN and convergence foundations specified below, and let `mu` be the resulting representing probability measure on normalized valuations at infinity. Put `a=N/d`, `A+=max(A,0)`, `A-=max(-A,0)`, and `K={rho=0}`, the directions whose images leave infinity. Let `E_i` be the actual omitted divisors in the finite normalization containing the **whole** source `A²`. Write `D_i` for their affine image curves, `r_i` for generic transverse ramification indices, `delta_i` for normalization degrees `E_i -> D_i`, and `b_i` for generic source-line pole orders. Coincident images are counted with their individual coefficients. Set

`W = deg C_H = sum_i r_i delta_i deg D_i`, where `C_H` is the affine missing-sheet cycle.

Then, at the stated conditional tier,

1. `M := integral A+ dmu = W/(d-N) < infinity`, and `mu(A<0)=0`.
2. `mu|K = sum_i (b_i delta_i deg D_i/d) delta_(nu_i)`, where `nu_i=b_i^(-1) ord_(E_i)` and `A(nu_i)=r_i/b_i>0`.
3. `mu|{A>0}` is carried by the countable union of finite-depth inverse images of those omitted divisorial valuations. No individual weight away from `K` is asserted.

In particular, the previously open finite-positive-moment premise is supplied for this **same** normalized map. The assertion does not give `W=0`, whole-measure atomicity, valuativity, Cartierness, properness, or `N=1`. The zero-thinness part is not classified by this report. JC2 remains unresolved.

## Dependencies and prior work

The [all-Keller sheet budget](all-keller-sheet-budget-swarmHQ-root-astra-sol56-20261026T005000Z.md) supplies the actual finite-normalization setup and polynomial-curve normalizations. The [composition report](keller-deficit-composition-and-iteration-neutrality-swarmHQ-root-astra-20261026.md) supplies degree-one transport on these curve normalizations and the deficit-cycle composition rule. The [boundary-moment report](dicritical-isotropic-obstruction-and-boundary-moment-swarmHQ-root-astra-sol56-20261026.md) retains the positive correction and explains why an unbounded signed canonical functional cannot simply be passed through an L2 limit.

The following inputs retain their exact conditional scope; the present publication is not a new full proof audit of them. Byte-identical internal proofs and the independent review are in the [evidence bundle](../box/finite-positive-moment-swarmHQ-20261027T191000Z/README.md).

- **FRAME.** Every normalized nef Weil class `D` has a unique positive Radon probability measure `mu_D` representing it against finite Cartier duality tests. For normalized nef Cartier `D` determined on a boundary model, this is the finite measure `sum_E b_E(D.E) delta_(nu_E)`. The continuous kernels `g_u(v)=alpha(u meet v)` for divisorial `u` determine the measure. The pullback/pushforward adjunction and boundary pushforward identity give `Hbullet_*(rho mu_D)=mu_(P D)`, with affine-image directions contributing zero; for `theta`, `P theta=a theta`. This is the FRAME internal result, not an application of the properness-only inverse formula.
- **THIN.** For a constant-Jacobian map, on live directions `rho>0` the identity is `A(v)=rho(v) A(Hbullet v)`. On the killed set `K`, `A>=epsilon_H>0`. The weighted measure identity implies `mu(A<0)=0`; if `M` is finite, it also implies `(1-a)M=integral_K A dmu`. These are the THIN internal results; finiteness of `M` is proved below, not assumed in the theorem's conclusion.
- **Convergence and topology.** The FJ pullback convergence theorem gives `theta_n=d^(-n)H^(n*)L -> theta` in the named Riemann-Zariski/L2 setting, hence convergence against finite Cartier tests. The normalized valuation space is compact Hausdorff, the measures are Radon, and thinness has its usual increasing ancestor parameterization. In particular `A+` is lower semicontinuous for the weak tree topology.
- **Finite geometry.** Resolution and boundary intersection duality, generic tame ramification in characteristic zero, and finiteness/divisoriality of extensions of divisorial valuations in a finite function-field extension are used at their standard named-foundation tier.

Primary references are Favre–Jonsson, [Eigenvaluations (2007)](https://www.numdam.org/article/ASENS_2007_4_40_2_309_0.pdf), for thinness and its normalization, and [Dynamical compactifications of C² (2011)](https://annals.math.princeton.edu/wp-content/uploads/annals-v173-n1-p06-p.pdf), for the operator and convergence framework. The independent reviewer inspected 113 selected cached text lines of statements, with exact windows and hashes in the custody record; the cited primary proofs were not fully audited. In particular, the properness hypothesis on the inverse class-expansion formula is never dropped.

## Proof

### 1. One representative satisfies both geometric requirements

Parametrize each of the finitely many actual nonproper-image curves of `F` by `(u_i(t),v_i(t))`. Choose an integer `m` so that `m deg P>max(deg Q,N)` and, for every nonconstant `u_i`, `m deg u_i>deg v_i`. For constant `u_i`, the coordinate `v_i` is nonconstant. The target shear `tau(u,v)=(u,v+u^m)` therefore sends every such curve's infinity to `e_2`.

Choose `B in SL_2(C)` with `q=B e_2` and `P_top(q)!=0`. Then `H=B tau F` has degree `d=m deg P>N` and leading homogeneous map `q P_top^m`. Its value at the projective direction `q` is defined and equals `q`; the leading map iterates without cancellation. Thus `deg H^n=d^n`. Target automorphisms carry the actual nonproper-image set to its actual transformed set, so every image curve of this same `H` has only infinity `q`. No sequence of new generic choices or common resolution of all iterates is assumed.

### 2. Exact growth of the affine deficit cycle

The cited composition rule gives

`C_(H^n) = sum_(j=0)^(n-1) N^(n-1-j) H^j_* C_H`.

Each induced map of polynomial-curve `A¹` normalizations has degree one by the all-Keller/composition parents. Since the only infinity is the regular fixed point `q`, a generic linear form pulled back along `H^j` has pole degree multiplied by `d^j` on each normalization. Hence `deg(H^j_* C_H)=d^j W`, and

`W_n := deg C_(H^n) = W (d^n-N^n)/(d-N)`.

The generic omitted-boundary degrees `delta_i` have not been replaced by one. They describe `E_i -> D_i`, not the ambient étale map restricted to an affine polynomial-curve normalization.

### 3. Finite Cartier approximants have explicit nonnegative moments

On a resolution `g_n:X_n -> P²` of `H^n`, the class `theta_n=d^(-n)g_n*L` is normalized nef Cartier, and FRAME gives

`mu_n = sum_E b_E(theta_n.E) delta_(nu_E)`.

It is a probability measure on the full valuation space: on every refinement, newly exceptional divisors pair to zero with the pulled-back Cartier class and the weights of strict transforms stay unchanged. This is not merely a finite trace chosen in place of the global representing measure.

Let `a_E=1+ord_E(dx wedge dy)`, so `A(nu_E)=a_E/b_E`. The constant global Jacobian of `H^n` and the generic ramification formula split the boundary exhaustively:

- If `E` dominates the target line at infinity with transverse index `r_E` and residual degree `f_E`, then `ord_E(dx wedge dy)=-3r_E+(r_E-1)`, so `a_E=-2r_E`, while `g_n*L.E=f_E`.
- If `E` dominates an affine curve `D`, then `a_E=r_E>0` and `g_n*L.E=f_E deg D`.
- If `E` maps to a point, `g_n*L.E=0`, regardless of the discrepancy.

All omitted affine components are included in the second sum, whose total is `W_n`; over the target line at infinity, `sum r_E f_E=N^n`. Therefore

`integral A+ dmu_n = W_n/d^n = W(1-a^n)/(d-N)`,

`integral A- dmu_n = 2a^n`.

This is a sign-separated, nonnegative calculation; there is no discarded ramification term or cancellation of an unbounded signed expression.

### 4. Lower semicontinuity gives the missing integrability bound

Convergence of the Cartier tests, compactness of probability measures, and FRAME uniqueness imply `mu_n -> mu` weak-*. One may use convergent cluster subnets; sequential compactness is not being assumed. For completeness, if `A(v)>c>=0`, choose a strict ancestor `w` with `A(w)>c` using the inherited thinness parameterization. The forward weak-open tree component beyond `w` containing `v` has `A>c`. The same ancestor argument applies at the allowed ends. Thus `A+` is nonnegative lower semicontinuous.

Radon Portmanteau now gives

`M=integral A+ dmu <= liminf integral A+ dmu_n = W/(d-N) < infinity`.

Only this one-sided inequality is used. It does not assert continuity of thinness or of the signed canonical pairing. THIN independently gives `mu(A<0)=0`.

### 5. Actual omitted divisors supply all killed mass

Choose one resolution of `H` retaining all actual omitted divisors `E_i`. Its complete `E_i` maps onto the projective closure of `D_i` with normalization degree `delta_i`. Every `H^j` is regular on that whole curve, including its point `q` at infinity. Consequently each `H^n` is regular near the whole `E_i` on this fixed source; the neighborhood may depend on `n`. The restriction has total line degree `delta_i d^(n-1) deg D_i`.

Every additional exceptional divisor over a point of `E_i` maps to a point for each such iterate and pairs to zero. Thus on all these refinements the normalized Cartier measure retains weight

`k_i = b_i delta_i deg D_i/d`

at `nu_i`. Equivalently, the fixed-model/refinement positive-test argument in the attached NORM proof gives `mu({nu_i})>=k_i`. No boundary degree has been assumed one and no common global resolving model for all iterates is needed. These valuations lie in `K`, and `A(nu_i)=r_i/b_i`, so

`integral_K A dmu >= sum_i A(nu_i) k_i = W/d`.

Finiteness of `M` now licenses THIN's balance `(1-a)M=integral_K A dmu`. Combining the lower bound with `M<=W/(d-N)` forces equality throughout. Hence `M=W/(d-N)` and `integral_K A dmu=W/d`. Each atom lower bound is exact, and the strict lower bound `A>=epsilon_H>0` on `K` rules out any residual killed mass. This proves the first two assertions, including the case `W=0`.

### 6. The positive part exits through divisorial valuations

Define the finite positive Radon measure `tau=A+ mu`. The live thinness identity and weighted FRAME transport yield

`Hbullet_*(tau|{rho>0}) = a tau`.

Use nonnegative tests and monotone convergence; no meaning is assigned to `0 times infinity`. The set `A=infinity` is `mu`-null because `M` is finite. If `L_n` is the Borel set of points staying live for their first `n` steps, induction gives `tau(L_n)=a^n M`. Therefore `tau`-almost every valuation reaches `K` after finitely many steps.

The restriction of `tau` to `K` is supported on the finite set `{nu_i}`. Each normalized live preimage of a divisorial valuation is among the finitely many valuation extensions in the degree-`N` function-field extension, and those extensions are divisorial. Each depth therefore has finitely many such preimages. Their countable union carries all `tau`, and hence all `mu` on `A>0`, since there `A` is positive and finite almost everywhere. This uses finite valuation-extension geometry, not the properness-only inverse class formula.

## Replay and negative controls

Desk-only mathematical proof; no CAS, random seeds, finite-degree search, paid computation or new primary-source fetch. The [bundle README and SHA256SUMS](../box/finite-positive-moment-swarmHQ-20261027T191000Z/README.md) give exact original proof/review bytes and qualifications. Original internal proof/review records remain unchanged.

For a normalized polynomial automorphism, the actual affine deficit cycle is empty: `W=0`. The theorem then says only that the positive-thinness part vanishes; it does not exclude the automorphism or force its eigenmeasure to be a finite divisorial measure. Thus the argument has no contradiction with known Keller automorphisms.

The attempted generic-fibre shortcut is preserved as a failed stronger route. Euler integration gives `chi({ell composed H^n=c})=N^n-W_n` for suitable generic `ell,c`, chosen separately for each iterate. This is the existing canonical correction evaluated on a pencil. It supplies no independent sub-`d^n` Betti bound and no reason for `W` to vanish. The useful new step is the nonnegative approximation and killed-atom squeeze, not that Euler identity alone.

The attached fixed non-Keller NORM example has a positive omitted divisorial atom without generic valuativity or Cartier rigidity. Its nonconstant Jacobian is explicit. It rejects a broader geometric shortcut, not a Keller-specific closing argument.

## Limitations and next test

The remaining closing implication is still to force the actual affine defect `W` to vanish, or to obtain another sufficient global Keller constraint. Finite `M`, exact killed weights and a countable divisorial positive carrier do not supply that implication. Countably many atoms do not make a class Cartier on one finite model. This result neither classifies nor eliminates the zero-thinness part and does not interchange an unbounded signed functional with a limit.

The independent review accepted the sign split, lsc bound, fixed-divisor weights, equality argument and survivor transport without mathematical repair. Its separate custody supplement corrects an initial reused-versus-fresh reading description and discloses missing dedicated raw streams for two earlier metadata gates. Later current checks are labeled as such; they are not retroactive originals. This report retains those qualifications and the unaudited primary-proof dependencies.

## OPENS RAISED

None newly registered. This removes the earlier integrability premise at the declared conditional scope; the existing global defect-vanishing/valuativity gap remains open. No automatic source, family, control, or computation successor is authorized by publication.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `70fb69ae689bb8077e5a33a80316bbbb668f6421` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15149`.
- Body SHA-256:
  `d86f6c0f7fe33153f06f61bd87eaee0a9eb9852588ee893b9a6602bbaa8ca1f7`.
- Frozen basis: `70fb69ae689bb8077e5a33a80316bbbb668f6421`.
