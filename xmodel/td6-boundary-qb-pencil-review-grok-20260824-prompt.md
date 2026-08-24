# Hostile different-model review — TD6 exact `q_B` boundary pencil

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`c327bdc8d02472feba42573760325099f34b8cdf`. Read in full:

- `xmodel/td6-boundary-qb-pencil-gate-20260824.md`;
- every payload in
  `cases/td6_boundary_qb_pencil_20260824/MANIFEST.sha256`;
- the frozen adjoint producer/review
  `xmodel/td6-jet-orbit-adjoint-gate-20260824.md` and
  `xmodel/td6-jet-orbit-adjoint-review-grok-20260824.md`;
- the parent q2 point-probe and uniform-third-band producer/reviews named by
  the report.

Frozen hashes:

- producer report:
  `5e1f6b44e143360a41550ae552b20bef02325414f96c5fd469ba4d016eb5eb22`;
- exact `E[B]` replay:
  `fab27e808ce0f840e82359d01f83834c874c168f6414f550e253d94aac42360c`;
- canonical replay stdout:
  `9326e8430ce76afb4c57d868fa0659a690c5c3a0cd3b6a7225c5095fefac7f48`;
- canonical transport cache:
  `3855b1d8aa98d3602bbba3630512600b4af66eba81103fea1bc8be286fabebb4`;
- raw-cache verifier / stdout:
  `78d06b9f64c80bd1fd328e5960b4512fe6a9c574ef53c47d63a58d56b9326328` /
  `cd8e8e070d055ebaa339f34ae524d0e163b29c2b929c5d546448068ae036e032`;
- transport field/cache library:
  `11521a7e25d85c7f8bb6ab5173c6489d08a13edf705e6e742c10211e6e152724`;
- manifest and freeze:
  `6df1eca8846adf23a5e2c45a4450857a6ae99e25ae0a2fd6a2cdc98e6fb9de58`.

Verify the freeze from the repository root. Rerun both registered programs:

```text
python3 cases/td6_boundary_qb_pencil_20260824/build_transport_cache.py
python3 cases/td6_boundary_qb_pencil_20260824/replay.py
```

The first is a provenance regression, not independent evidence. Then attack
every load-bearing claim by a genuinely separate exact reconstruction:

1. **Field and source scope.** Verify the degree-18 field presentation and
   every inherited pin: rectangles, three charts, sextic point, pole scale,
   centering, zero dead stretch, F1 pattern, and
   `p=t^15`, `q_B=t+B*t^2+t^25`. Recheck that q2-only is transverse only
   after the registered chart/source quotient and that centering/dead stretch
   remain frozen licensed moduli. Look for any source or target gauge that
   absorbs `B`.
2. **Portable transport provenance.** Independently compare the canonical
   JSON sections with a reconstruction from all raw 3,602 transport columns.
   Audit that no row or parameter used in the first, previous/pole, or current
   bands is absent from the cache. Treat byte equality as provenance only;
   do not use the producer cache as the sole mathematical engine.
3. **Exact polynomial elimination.** Build a second untruncated solver over
   `E[B]` (or equivalent fraction-free exact engine) without importing the
   producer's normalized forms. Verify ranks
   `3470/3602 -> 38/132 -> 38/94 -> 25/56`. Audit all 101 normalized pivots,
   prove each is a nonzero B-independent unit, and check every residual
   homogeneous row coefficientwise. A single hidden B-only pivot or
   denominator factor creates an exceptional stratum and flips the claim.
4. **Affine rebuild and compatibilities.** Substitute both affine
   parameterizations into every original first and previous/pole equation.
   Independently derive all current left-null conditions and at minimum
   verify against the original rows, not reduced output, that

   `N4=rho-(4720/29)B+(11364/145)B^2-(4096/145)B^3+16B^4`

   and

   `N13=((252-342S+144S^2-36S^3)/25)B`.

   Recompute their supports, degrees, and syzygy identities. Check that
   continuing elimination after the first affine failure is algebraically
   legitimate for extracting the compatibility ideal.
5. **Units, gcd, and exceptional roots.** Prove in the exact residue field
   that `k=252-342S+144S^2-36S^3` and `rho` are nonzero units. Verify the
   displayed inverse of `k`, the exact Bezout identity, and
   `gcd(N4,N13)=1` over `E[B]` and after arbitrary field extension. Audit
   `B=0`, every quartic root of `N4`, all sextic conjugates, any reducibility
   or zero-divisor issue in the field presentation, and every pivot/resultant
   locus. Do not infer unit ideal merely from sampled points.
6. **Adjoint/point controls.** Independently check that the coefficient of B
   in `N4` is the reviewed varying-syzygy derivative `-4720/29` and that
   `N4(1)-N4(0)=-14012/145`. Confirm that neither equality is used as
   interpolation evidence and that the full polynomial solve supersedes,
   rather than circularly imports, the adjoint and two-point gates.
7. **Logical scope and successor.** Decide whether the exact conclusion is
   only emptiness of this one licensed q2 pencil in the fixed normalized
   section. Attack every inference to centering/dead-stretch families, other
   boundary jets, full SP-2, any terminal class, or JC2. Assess whether the
   smallest honest successor is the first matrix-changing common-centering
   pencil followed by first-entering dead-stretch blocks.

Use exact arithmetic throughout. Producer replay plus prose comparison is not
independent evidence. Do not edit producer, case, canonical, ladder, notes,
or erratum files and do not launch AWS. Keep all scratch work outside tracked
paths. Write exactly one report:

`xmodel/td6-boundary-qb-pencil-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
hashes, independent derivations, the smallest failing identity if any,
precise promotion scope, and quarantine language at both ends.
