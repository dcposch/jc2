# Contractible whole nonproper curve: independent hostile review

Verdict: PASS_CONDITIONAL
Lifecycle effect: none by this worker; ROOT decides promotion. Configured model: gpt-5.6-sol/ultra; hosted identity UNVERIFIED.
Started UTC: 2026-10-31T12:30:54.764855+00:00
Completed UTC: 2026-10-31T12:37:37.263245+00:00

## Exact object and conclusion

I reviewed complete `CANDIDATE.md`, SHA-256 `6fc089fd693149cb177c52623a8869c161edd543adbde057e3af15e536599043`. Under the hypotheses below, its exclusion of a nonempty contractible WHOLE nonproper-value curve is correct, including reducible curves. This says nothing about noncontractible curves and does not prove JC2.

## Hypotheses retained, not strengthened

1. `F:A2_C -> A2_C` is an actual noninvertible polynomial Keller map of geometric degree `N>1`, and `D` is its nonempty reduced WHOLE nonproper set.
2. The accepted finite-normalization package has the WHOLE source open, smooth pairwise-disjoint omitted `A1` curves `E_i`, image-component normalizations `A1`, generic counts `d_j=N-sum_(E_i->D_j) r_i delta_i`, and the whole-source identity `N-1=sum_i r_i delta_i+S`, with all local slack terms nonnegative.
3. `ZEROSLACK.md` applies at its stated smooth-`E_i`, completion, finite-flat, and cyclic-model scope: local slack is zero exactly for an immersed selected image branch.
4. The named affine-curve Euler and finite-etale-cover facts, Lin-Zaidenberg, Abhyankar-Moh, and injectivity-on-an-actual-line Keller theorem are available.
These inherited foundations were not source-reaudited. `BUDGET.md` and `ZEROSLACK.md` are consumed only at their stated scopes.

## Six-step hostile check

### 1. Positive Euler component and unibranchness: confirmed

For `Z=F^{-1}(D)_red`, etaleness makes the scheme pullback reduced. Over `A2-D`, `F` is finite etale of degree `N`, so additivity gives `1=N(1-chi(D))+chi(Z)=chi(Z)`. For each irreducible affine curve `H`, `chi(H)=2-2g-s-b<=1`; positivity forces normalization `A1` and no finite branch identification. Since Euler characteristic of a reduced union is at most the sum for its irreducible components, `Z` has a component `Gamma` homeomorphic to `C`. A contractible `D` is obtained from its `A1` normalizations with an acyclic gluing graph. A self-identification would be a loop, so every normalization `A1 -> D_j` is bijective. No multibranch injectivity is inferred.

### 2. Actual line injectivity: confirmed

If `Gamma` is smooth, Abhyankar-Moh rectifies that actual source curve to a line. On normalizations, its map to `D_j` is a polynomial `a(t)`. A zero of `a'` would make the derivative of `F` vanish along the line, contrary to etaleness; hence `deg(a)=1`. The preceding bijectivity of `A1 -> D_j`, not normalization degree one alone, makes `F` injective on the actual line. The named theorem contradicts noninvertibility. Thus `Gamma` is singular, and Lin-Zaidenberg gives `Gamma={x^p-y^q=0}` with coprime `p,q>1` after a source automorphism.

### 3. Cusp-disjointness, including the torus substitution: confirmed

Let closed irreducible `H` be disjoint from `Gamma`. If its smooth affine normalization has nonnegative Euler characteristic, it is `A1` or `G_m`. Writing its coordinates as `a,b`, the nowhere-zero function `a^p-b^q` is constant on `A1`, or `c t^k` on `G_m`. The smooth completion of `A^p-B^q=c` has genus `(p-1)(q-1)/2>=1`, so a map from `P1` to it is constant. For `G_m`, after `t=z^(pq)`, set `A=z^(-kq)a(z^(pq))`, `B=z^(-kp)b(z^(pq))`; then `A^p-B^q=c`. Constancy gives `a(z^(pq))=alpha z^(kq)` and `b(z^(pq))=beta z^(kp)`. For `k>0` both coordinates tend to `(0,0)` as `z->0`, and for `k<0` as `z->infinity`; zero `alpha` or `beta` is harmless. Closedness puts the origin in `H`, contradiction. Thus every such normalization has negative Euler characteristic.

### 4. Whole-inverse connectedness: confirmed

Let `Z0` contain `Gamma`. Every irreducible component of another connected component is disjoint from `Gamma`, so its normalized Euler characteristic is negative; finite gluing only lowers it. Thus every other connected component has negative Euler characteristic. But `chi(Z0)<=1` and `chi(Z)=1`, so none exists. Equality in the connected-curve bound forces all component normalizations of `Z` to be `A1` and the branch-gluing graph to be a tree. This concerns the whole inverse curve, not a residual slice.

### 5. Finiteness without assumed properness: confirmed

Each irreducible `H` of `Z` maps dominantly to some `D_j` by quasifiniteness. The induced nonconstant polynomial `A1=H~ -> D_j~=A1` is finite. Since `C[D_j]` has finite normalization, `C[H~]` is finite over `C[D_j]`; its intermediate subring `C[H]` is a finite module by Noetherianity. The reduced ring `C[Z]` injects `C[D]`-linearly into the finite product of the `C[H]`. That product is finite over `C[D]`, so its submodule `C[Z]` is finite. No properness was assumed. The restriction `Z->D` is finite etale by base change. The budget gives every `d_j>=1`; finiteness makes the map surjective. Its rank is constant on connected `D`, and Euler multiplicativity gives `1=chi(Z)=k chi(D)=k`. A rank-one finite etale map is an isomorphism, so every `d_j=1`.

### 6. Degree-one cover and budget contradiction: confirmed

If `ell` is the number of `D_j`, then `d_j=1` gives omitted mass `N-1` over each component. The single whole-source budget yields `N-1=ell(N-1)+S`. For `ell>=2` this contradicts `N>1` and `S>=0`. For `ell=1`, it gives `S=0`; the isomorphism makes `Z=Gamma` and `D` a singular unibranch curve. Some omitted `E_i` maps finitely and surjectively onto `D`, hence has a point over the nonimmersed branch. `ZEROSLACK.md` makes that local slack positive, contradicting `S=0`.

## Exact prior-result comparison

`INTEGRATION9.txt:14-15` already records SMOOTH-KILL: the whole nonproper set of a noninvertible Keller map is never homeomorphic to `C`. That is exactly the `ell=1` endpoint recovered above and is not new here.

The intact `PRIOR-REDUCIBLE.md` has narrower RED-N assumptions (reducible locus and a `mu=1` dicritical), proves conditional CAGE-N restrictions, and explicitly leaves the multi-component `PI1-S_N` family open (lines 410-456 and 556-582). It does not state or prove exclusion of a contractible reducible WHOLE nonproper set. Thus the candidate is not `EXACT_PRIOR_RESULT`; no novelty assertion follows from these selected records.

## Audit and limits

Packet preflight verified 18 members and four declared report seals. Required reading was complete in 79 verified body windows: 2556/3000 non-STATE LF in 68 windows and 199/199 STATE LF in 11 windows. Every returned `next_start` was followed to EOF; repeats 0, failed body windows 0, omitted/cropped lines 0. Packet-reader help outputs: 2 non-body outputs. Own-report body previews: 0. Startup-ACK body previews: 0.

No web/source/history/repository query, secondary model, model probe, CAS/scientific computation, Git action, or protected-tree access occurred. A useful unsealed draft was saved at 2026-10-31T12:35:54.382550+00:00. No exit-price assertion is made.

Noncontractible nonproper curves and JC2 remain unresolved.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7150`.
- Body SHA-256:
  `dbb06614e862e09b518b9021e39a961a55f0e9d6bce3f1d0aeb8df435ebc41a6`.
- Frozen basis: `a8564152a8ea83c377848837381ca4e036db3aef`.
