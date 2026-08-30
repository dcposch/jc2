# Bounded hostile review: affine-linear cubic block closure

You are Fable 5, an independent hostile mathematical reviewer for the plane
Jacobian-conjecture campaign. Work in `/Users/dc/code/math/jc2` on frozen git
basis `a619157b73c1dee1ca0599db47321ffd7588d748`.

Your sole charged claim is:

> No proper cubic intermediate block of a hypothetical Keller map can have
> affine-linear Miranda coefficients in any fixed global trace-zero basis.

Review only the load-bearing chain needed for that theorem. Do not audit the
producer's auxiliary explicit control, almost-surjectivity section, or general
cubic corollaries; those are deliberately outside this bounded rerun.

Frozen inputs:

```text
67e1305ba8dc452af6e120b37e24c102856ac5236d9140ffae9a0446c28261bc
  xmodel/bd-fix3-affine-linear-residual-control-producer-sol56-20260830.md
  body 16015 / 0a82cca57e2a3d58fec256256c581f87483dae3301459a6b202cb057e6f1902b
ff25ba27388c02698013483e2e5537f18ed39e918e5cb0cb4c099a75ef42f298
  xmodel/bd-a2-firstleg-log-kodaira-coordinator-integration-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
```

Independently verify, without re-copying the inputs:

1. Re-derive the Miranda multiplication table and
   `det(t,t^2)=Phi(r,s)`, hence monogenicity iff `Phi` represents a unit of
   `C[u,v]`. State every Gorenstein, normality, and basis hypothesis.
2. Repair the producer's phrase “integrality makes the common zero unique.”
   Use normality at the generic DVR of a hypothetical common-zero line: the
   Miranda special fibre has a two-dimensional square-zero radical, whereas
   a normal rank-three totally ramified DVR extension has nonzero radical
   square. Confirm or refute this argument explicitly.
3. In the isolated common-zero case, prove the missing bridge rather than
   identifying two different spaces: the binary-cubic incidence surface is
   `Tot O_{P1}(-3)` and maps to the actual finite normal cover by affinization,
   contracting exactly its zero section. One valid route is the homogeneous
   Miranda algebra with Hilbert function `3n+1` and twisted-cubic Proj. Check
   the literal map `(u,v)=tau*(-P2,P1)`. Then verify units `C*`, class group
   `Z/3`, and the localization/unit contradiction for the first leg.
4. With no common coefficient zero, justify the separate Gorenstein/incidence
   bridge identifying `Spec B` with
   `{P0+uP1+vP2=0} subset A2 x P1`. Prove that the field condition forbids a
   common zero of all `Pi`; nonmonogenicity forces `S_X=empty`; `P1,P2` are
   basepoint-free; `rho=[P1:P2]` has degree three; and `W!=0`, including the
   cases where one of `P1,P2` vanishes identically. Verify the resulting
   smooth `O(-3)` affine-line torsor has units `C*` and class group `Z`.
5. If ramification support is reducible, verify that localization
   `Z^(components)->Cl(Y)=Z` has nonzero kernel and that its resulting unit on
   the etale complement contradicts dominant pullback to `A2`. Do not assume
   individual component classes are nonzero unless proved.
6. If the support is irreducible, audit `F=dF=0`: off `Crit(rho)` it is one
   graph point; compatibility at a critical direction gives an entire
   vertical fibre and a second component, so irreducibility forces no point
   there. Use the binding fixed-sheet/transposition input and Cartier purity
   to justify the reduced scheme
   `R ~= P1 minus Crit(rho)`. Riemann--Hurwitz must give at least two distinct
   critical directions. In the ruled completion, prove the graph closure is a
   section meeting infinity exactly at those directions.
7. Match the hypotheses of the binding log theorem `ff25ba27...`: for
   `U=Y minus R`, `#S>=2` forbids every dominant `A2->U`. Match the binding
   sandwich to obtain `g1(A2) subset U` and dominance, hence contradiction.

Return an itemized verdict (`CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or
`REFUTED`) and the maximum exact theorem safe to promote. Keep the
basis-dependent affine-linear scope explicit. Make no nonlinear cubic,
primitivity, map-existence, counterexample, or JC2 claim.

Hard output cap: at most 8,000 tokens and at most 28,000 UTF-8 bytes. Do not
restate long inputs or explore optional successors. Do not inspect, list,
search, stat, build, modify, or control `jc2-lean`; the process sandbox also
enforces this. Do not run local heavy CAS or Singular. Do not edit any input,
canonical file, script, or dependency. Write exactly one report:

```text
xmodel/bd-fix3-affine-linear-log-closure-bounded-hostile-review-fable5-20260830.md
```

End with one standalone `<!-- BODY-END -->` line and no seal block.
