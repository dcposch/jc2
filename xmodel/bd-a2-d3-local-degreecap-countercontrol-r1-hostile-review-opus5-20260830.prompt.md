# Hostile review: corrected D3 local raw-degree-three counter-control

You are Opus 5 acting as a fresh hostile reviewer for the plane Jacobian-
conjecture campaign. Work in `/Users/dc/code/math/jc2`. Reconstruct every
mathematical step independently and actively seek a counterexample. Do not
modify charged inputs, Git state, canonical ledgers, or unrelated files. Do
not read any sibling external-model prompt, log, report, or receipt. Do not
inspect, list, search, stat, build, modify, or control `jc2-lean`.

Hash-check and audit only these charged files:

```text
13677719b809be352f59b41ca3f2eb54e50a61a1225431f2fa3151aafdc38879
  xmodel/bd-a2-d3-local-degreecap-countercontrol-r1-sol56-20260830.md
71e17cace335d275e76521142dfda23d0a7a25298c816f804dfbbc448c1132db
  xmodel/bd-a2-d3-local-degreecap-countercontrol-r1-sol56-20260830.md.artifact.json
82f930fff174c2b599e5965459c6e2eb0c10117cfca084bc8116ddf82bbac79d
  xmodel/bd-a2-d3-local-degreecap-countercontrol-sol56-20260830.md
55b836a77ed4046a162bd04946d7496abacd27d22710c870f6c4f036340e96b2
  xmodel/bd-a2-d3-local-degreecap-countercontrol-sol56-20260830.md.artifact.json
c0ace16d2f8a7e1b86cafb6d2d2a829d3f35ac132a78fa6d636934174379c8ab
  xmodel/bd-a2-d3-sectioned-one-support-threat-map-sol56-20260830.md
95f2f9fc72d6560749aef090ce91dbd0ef3398ed705bcede69258425ad4ca9de
  xmodel/bd-a2-d3-hodge-level-divisor-coordinator-integration-sol56-20260830.md
```

Audit the corrected maximum-safe theorem, not the superseded draft.

1. Expand `Phi=(x+t*z)^3+t*y^3+t^3*x^2*y`; verify the literal raw
   coefficient-degree cap, primitivity, point `[-t:0:1]`, and determinant-one
   shear. Look for a hidden misuse of raw versus transformed degree.
2. Recompute both displayed transformations. Verify integrality, the exact
   CFS admissible Smith pair `(1,1)`, invariant character, and that each move
   really lowers level by one. Check coordinate ordering and all powers of
   `t` against the cited CFS definitions.
3. Independently project the terminal ternary cubic from its rational point.
   Derive the generalized binary quartic, square completion
   `W^2=-tZ(X^3+tZ^3)`, and Weierstrass form `V^2=U^3-t^4`. Recompute
   `c4,c6,Delta`, minimality, Kodaira type `IV*`, and the complete valuation
   ladder `(4,8)->(10,20)->(16,32)`. Check that exact CFS level two and
   `v(c6)<18` follow.
4. Recompute generic smoothness and the full projective total-space singular
   locus over `C[[t]]`. Audit the integrality argument, codimension count,
   `S2`, `R1`, and Serre normality. Try to find any omitted generic or closed-
   fibre point.
5. Compare the initial and R1 reports. Confirm that R1 explicitly retracts
   every consequence of the dropped factor of `t`, and identify any stale
   statement that still survives incorrectly.
6. Rerun the embedded exact replay under ordinary Python/SymPy and reproduce
   its hashes/output where stated. The replay uses `assert`, so do not promote
   optimized-mode evidence. Separate executable checks from hand proof.
7. Price the result narrowly: local counter-control versus global
   class-`(3,3)` surface, actual proper block, polynomial map, or JC2. Decide
   whether the proposed local raw-degree-three impossibility is genuinely
   refuted even if the natural global homogenization later fails.

Return itemized `CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or `REFUTED`,
then a maximum-safe theorem and cheapest useful successor. This review makes
no exit-price assertion: emit no `charge_basis={...}` line; receipt status
`ABSENT` is expected. Do not run heavy local CAS.

Write exactly one report and no other file:

```text
xmodel/bd-a2-d3-local-degreecap-countercontrol-r1-hostile-review-opus5-20260830.md
```

End it with one standalone `<!-- BODY-END -->` line and no seal block.
