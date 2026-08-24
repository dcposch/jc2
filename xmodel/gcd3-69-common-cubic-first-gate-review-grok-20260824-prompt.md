# Hostile different-model review: GCD3 `(6,9)` common-cubic first gate

Act as a hostile independent mathematical reviewer. Review the frozen producer

`xmodel/gcd3-69-common-cubic-first-gate-20260824.md`

at SHA-256

`f63bf74fd1013c74645f9f7fe9292db69199572b390b5b19d160c5ed13b373e8`.

Charged clean-bank basis is
`6f2e49e63d74493910fa357a8adc82f0e40d219a`. Verify both frozen manifests from
the repository root:

`cases/gcd3_69_common_cubic_first_gate_20260824/MANIFEST.sha256`

at SHA-256
`ea2353e008b9ce1d52810fc792c23b3ce8c3246812e8912432dbf37677707e2c`, and

`cases/gcd3_69_common_cubic_first_gate_20260824/FREEZE.sha256`

at SHA-256
`65370031b04014f96efc3ac814477a6689d5d5fef6b2695066ba6d60658ee585`.

Reread the cited reviewed partial-`y` history stop. Do not import a persistent
common root, orbit degree three, pure Davenport--Stothers entry, polynomial
Kummer depression, or a nonlinear `(6,9)` exclusion. Return a self-contained
Markdown report with an overall verdict and a numbered verdict for every
claim below. Re-run both registered replays, and independently reconstruct
every load-bearing finite calculation with a second derivation or engine. Do
not edit producer, case, canonical, ladder, or notes files.

1. **Top row and Kummer split.** Starting from actual `y`-degrees `(6,9)` and
   `a_6=h^2,b_9=h^3`, verify the `y^13` identity
   `s^14(9A'-6B')`, the depression `r=A/6`, and the residual mismatch
   `-delta/2`, where `delta=3A-2B` is constant. Check carefully that a
   nontrivial cubic Kummer action forces `delta=0`, whereas a cube core only
   says `h` is a constant times a polynomial cube and leaves `delta!=0`
   live. Police the fact that `z=sy+r` is over a coefficient extension and
   that its two boundary values are polynomial but need not vanish.
2. **Eight high source rows.** Independently integrate/differentiate the
   triangular `z^12,...,z^5` system. Check the Kummer weights of all eight
   constants, the vanishing of `c_7,c_5,c_4,c_2,c_1`, removal of `c_6,c_0`
   by constant target gauges, and the exact surviving normal form with five
   moving `a_i` plus essential `kappa=c_3`. Verify that on the persistent
   common component it is exactly `f=K^2,g=K^3+kappa K` and has zero source
   bracket, while an associated-graded common point does not prove such
   persistence.
3. **Cubic provenance and strata.** Check the UFD derivation of
   `F_0=K^2,G_0=K^3`, the depressed cubic and its squarefree/double/triple
   strata. Audit the selected-root correction: a boundary equation licenses
   reduction only modulo the root's minimal polynomial, not the full cubic
   without orbit degree three. Recompute the split control
   `K=z^3-t^2z,rho=0,phi=z t^5,psi=3Kphi/2`.
4. **Linear, quadratic, and singular controls.** Verify
   `L_K=K{K,2psi-3Kphi}`, the nonzero constant cokernel class, and under the
   exact zero-RHS filtration assumptions the squarefree implication
   `q_2=9phi^2K_z mod K`, hence `K|phi`, with the three displayed coefficient
   rows. Confirm the RHS/boundary caveat. Independently check the double- and
   triple-root Artinian two-jets and their precise non-Keller scope.
5. **Complete normalized constant-W scheme.** Reconstruct all eight solved
   `b` rows and the four residual equations. Independently verify that the
   radical is exactly the intersection of the common-cubic prime and one DS
   prime, that these are the only reduced components, and that they meet
   only at the triple-cubic origin. Distinguish the radical classification
   from the nonreduced original residual scheme. Recheck the DS
   parameterization, `f^3-g^2`, constant Wronskian `378 lambda^7`, and the
   exact nonzero resultant.
6. **Boundary timing and literature scope.** Verify that the DS curve meets
   the common component only at the triple point, `f_lambda(0)` first turns
   on at `lambda^3`, and the constant row at `lambda^7`. Check that this is a
   negative control against filtered boundary persistence. Source-check only
   the historical claims actually used; the exact component calculation
   must stand independently of the literature.
7. **Conditional pure-DS closure.** Under—and only under—the explicit
   pure-entry hypothesis, derive weighted Euler, `J_(lambda,z)=567lambda^6`,
   the chain rule, and `(lambda^7)'=j/(81s)`. Audit every finite-place and
   infinity valuation case in (7.4)--(7.8), including `h` constant,
   cancellation, leading coefficients, and why the historical
   `3|deg(h)` forces the cube-core form. Then check the two polynomial
   boundary valuation argument and resultant endpoint. Freeze the smallest
   counterexample if any valuation case was omitted.
8. **Exact scope and successor.** The maximum licensed promotion is:
   Kummer-aligned versus cube-mismatch normalization; full-cubic boundary
   reduction `TYPE-FAIL` absent orbit degree three; the exact two-component
   constant-W classification; conditional exclusion of a pure DS source
   path; and high-row reduction to five variables plus `kappa`. It does not
   solve the four lower Pfaffian rows, terminal Keller row, filtered
   component/boundary persistence, cube mismatch, `(6,9)`, or JC2. Judge
   whether those lower rows, treated componentwise with the true minimal
   boundary factor, are the smallest honest successor.

For each claim label `CONFIRMED`, `PARTIAL`, `REFUTED`, or `TYPE-FAIL`, give
the smallest failing identity if any, and state the exact promotion and
quarantine at the top and bottom of the report.
