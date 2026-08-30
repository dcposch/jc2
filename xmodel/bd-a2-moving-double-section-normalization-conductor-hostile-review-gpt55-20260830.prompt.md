# Hostile review: moving-double-section normalization and conductor

You are GPT-5.5 xhigh, an independent hostile algebraic-geometric reviewer
for the plane Jacobian-conjecture campaign. Work in
`/Users/dc/code/math/jc2` on frozen git basis
`f43ee99da2bc9f831d94e403dcd90622e87e8756`.

Read and review this sealed exact provisional producer in full:

```text
9557f2c1396daba190927e6a220774362a02068b4197103357d30e8cfc78b75e
  xmodel/bd-a2-moving-double-section-normalization-conductor-sol56-20260830.md
  body 18927 / dfd050e37b97b119f6170259f7417ac69e8109723abec4abe8260e3c7a33be57
  manifest 6675be2beab682f5da3230db4631c5859ce76018ce1e73b21dea62eedcbc408a
```

Its frozen authorship basis is `dca72076aa1615b0b1286fd4428a1acac7b65963`;
its producer commit is the review basis above. Read every charged input named
in Section 0 and enforce its exact scope.

Independently reconstruct and attack:

1. Verify that the predecessor really leaves exactly the integral form
   `F=Q^2L+TQS+T^2R`, with `C=(T,Q)` of type `(1,1)`, and that bidegrees make
   the transverse equation exactly homogeneous rather than merely its normal
   cone. Audit the assertion that `ell,s,r` never vanish simultaneously.
2. Check that integrality forces `delta_C=s^2-4ell*r` nonzero and nonsquare
   in `C(C)`. Then scrutinize the stronger squarefree step: the blowup chart
   must be genuinely independent of the radial parameter, a multiple root
   must give a codimension-one singular locus, and its nonexceptional points
   must land inside the already-proved-normal affine incidence. Cover the
   `ell=0` chart and all quartic multiplicity types.
3. Rebuild the blowup calculation in both charts. Verify every fibre is
   zero-dimensional, so the strict transform is finite birational over `X`,
   and prove `S_2` and `R_1` everywhere before identifying it with the
   normalization. Look for unhandled singularities along the residual section
   or at branch fibres.
4. Compute the conductor algebra from the local ring, not just generically.
   Verify that the conductor downstairs is exactly `(T,Q)`, upstairs is
   `O(-E)`, and `nu_*O_Xnu/O_X=O_C(-2)`. Audit the double-cover trace line,
   branch degree, pushout square, and canonical formula
   `K_Xnu+E=nu^*K_X` including signs and multiplicity.
5. Recompute the hypersurface cohomology and the long exact normalization
   sequence. Check the exact conclusions `h1(O_Xnu)=1`, `h2=0`, injection into
   every resolution, factorization/lifting of the dominant `A2` first leg,
   and the claim that the resulting dominant map from a rational surface
   forces `q=0`.
6. Independently audit the rational-forest contradiction: prove that the
   smooth genus-one conductor is an actual boundary component in the charged
   first-leg compactification. Check the claim that the residual section
   attaches at exactly one physical point, including the unramified fibre.
7. Separate the degenerate-quartic curve threat map from the charged surface
   normalization. Reject any implicit claim that a nodal/cuspidal first
   blowup is already normal, or that curve arithmetic genus alone closes it.
8. State the maximum theorem safe to promote. Keep fixed quadratic
   presentation, arbitrary basis coverage, normal-singular ADE incidences,
   polynomial maps, counterexamples, and JC2 distinct.

Return an itemized verdict (`CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or
`REFUTED`), precise repairs, and the cheapest decisive successor. Hard cap:
8,000 tokens and 28,000 UTF-8 bytes. Do not inspect, list, search, stat, build,
modify, or control `jc2-lean`; the process sandbox also enforces this. Do not
run local heavy CAS or Singular. Do not edit inputs, canonical files, scripts,
or dependencies. Write exactly one report:

```text
xmodel/bd-a2-moving-double-section-normalization-conductor-hostile-review-gpt55-20260830.md
```

End with one standalone `<!-- BODY-END -->` line and no seal block.
