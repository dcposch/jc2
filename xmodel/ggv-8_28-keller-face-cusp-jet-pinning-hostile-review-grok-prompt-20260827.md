You are Grok, the independent hostile reviewer for the bounded `8_28`
Keller-face cusp-jet pinning control.  Work only in
`/Users/dc/code/math/jc2`.  Never enter, read, build, status-inspect, or modify
`jc2-lean`.  Do not edit frozen producer files, launch AWS, run heavy CAS,
perform a web sweep, or edit canonical ledgers.

Review these exact charged artifacts:

```text
ef9acfa90935b32e244367dada67ab35d6454f431f6d43dc35d144b3d08fe46c
  cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/verify.py
46e1b3434badcea007a914ec71bf60d9758ee76d312dc00d252342d52beed76d
  cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/RESULT.json
79a16f282f0a3a3e5409b3e0b6d4a8dc61e2fedaa6babdf673b5645d64c38530
  cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/README.md
3e4e608d32c44b1b0208bd5472257ba1dbe4cadf4ef5efb2ace49d3d47d756be
  xmodel/ggv-8_28-keller-face-cusp-jet-pinning-sol-20260827.md
6928428f9cc46641a80275e2bbfa62e784c4290ff041f5089ae789507fa8804f
  cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/FREEZE.sha256
```

Do not accept the producer `PASS`, symbolic engine, reported identities, or
the prior non-Keller `8_28` prototype as evidence.  Independently rederive and
attack:

1. **Custody and additive scope.** Rehash the charged artifacts and every
   pinned dependency.  Confirm that the prior control remains immutable and
   that the history/dedup statement correctly distinguishes the old
   approximate-root proposal from the new recurrence and provenance test.
2. **Coordinate and sign.** Starting with `x=t^3 X`, `y=t^-1`,
   `f=t^-8 F`, `g=t^-12 G`, recompute the determinant and Jacobian sign.
   Decide whether `[f,g]=1` is exactly

   ```text
   E=12 F_X G-8 F G_X-t(F_X G_t-F_t G_X)=t^22.
   ```

   A sign, exponent, component-order, or bracket-convention error is a
   refutation of the downstream ODE as stated.
3. **Face replacement.** Expand `B=x(xy^4-1)^7` and independently check that

   ```text
   f_face=B^2-2*x^8*y^32+y^8
   g_face=B^3-3*x^16*y^60+3*x^8*y^36-y^12
   ```

   have `y`-edge `H^2/H^3`, `H=X^8-1`, while retaining the entire maximum
   `(4,-1)` faces `B^2/B^3` at weights 8/12.  Check squarefreeness of `H`.
4. **General recurrence.** Independently derive for all `n`

   ```text
   E_n=sum_(i+j=n)((12-j)F_i'G_j+(i-8)F_iG_j').
   ```

   Audit the producer's tiny symbolic ring for aliasing, omitted derivative
   terms, hard-coded expected output, or a substitution that proves only a
   specialization.
5. **`E_1/E_2` algebra.** Prove or refute the squarefree-polynomial
   uniqueness step from

   ```text
   E1=2H(11H'D-4HD'), D=G1-(3/2)HF1.
   ```

   Check carefully whether a nonzero polynomial `D` can occur over an
   algebraic extension.  Independently expand `E2`, reduce modulo `H`, and
   verify `E2 mod H=-(21/2)H'F1^2`.  Decide whether `E1=E2=0` really forces
   `H|F1`, and then verify both existence and uniqueness of

   ```text
   G2=(3/2)H F2+(3/8)H a^2, F1=H a.
   ```

6. **Rejected first jet.** Recompute the exact modulo-`H` remainders for
   `F1=-14X^15+lambda`, `lambda=13,14`, with `G1=(3/2)HF1`.  Check that the
   tempting root cancellation at `lambda=14` is genuinely nonextendable at
   `E2`; do not accept any pole-count conclusion from that invalid jet.
7. **Cusp normalization and provenance map.** At every simple root `c`,
   justify the allowed formal Morse/source and target cleanup to

   ```text
   F=u^2+U(t), G=u^3+V(t)u+W(t), u=H(X).
   ```

   State exactly what is local/formal versus global/polynomial.  Independently
   verify the first raw map
   `U1(c)=F1(c), V1(c)=3F1(c)/2, W1(c)=0`, its behavior under cleanup, and the
   conclusion `U1(c)=0`.  Flag any omitted unit, `H'(c)`, deck, or chart
   factor.
8. **Fibre ODE and genericity.** On `F=a*t^8`, independently derive

   ```text
   d(t^-12*G)/dt=-t^9/F_X.
   ```

   Check sign and powers.  Precisely characterize when `ord_t(F_X)=4` and
   when a cusp-discriminant/special-fibre collision invalidates it.  Decide
   whether the narrow conclusion is exactly: on generic tagged branches of
   this square edge, `g` is finite with `g-g(0)=O(t^6)`.  Reject any broader
   claim about all fibres, all edges, or absence of global poles.
9. **Formal root-sign mutations.** Independently verify the two displayed
   `S_+,S_-`, their identical `(t,X)` support, `S^2=1 mod H`, exact
   `Q_S=3(S^2-1)/(8H)`, factor sign patterns, `a=1` degeneracy degrees 7/3,
   generic `a=2` residue squares 25/4 and 27/4, and every coefficient
   `E_0..E_21=0`, `E_22=0`.  Then check the producer's crucial rejection:
   `t^16 X^i` in `G` pulls back to `x^i y^(3i-4)`, so nonzero `i=0,1` terms
   are Laurent, not polynomial.  Prove or refute the general low-coefficient
   argument that `q0=q1=0` forces a uniform root-sign packet.  These examples
   must not be called polynomial-source or Keller mutations.
10. **Determinant carrier and global gap.** Independently derive the first
    local/rootwise unit carrier

    ```text
    6 H'(c)V8(c)U14(c)=1.
    ```

    Check that `U14=X,V8=1/48` works modulo all eight roots of `H`, and expand
    the global coefficient to confirm or refute
    `E22=1+(13/12)H`.  Decide whether the remaining `13H/12` is an explicit
    unsolved higher-`u`/global polynomial lift, rather than something the
    rootwise fixture already removes.
11. **Scope firewall.** The maximum permitted result is one exact
    square/cube-edge recurrence, generic finite-pole pinning statement, two
    rejected formal mutations, and a bounded cusp provenance interface.  It
    is not a Keller pair, a counterexample, a global GGV-to-tree functor,
    source/landing coverage, `G2-PSC`, `G2-BD`, or JC2.

Return separate `CONFIRMED`, `REFUTED`, or `GAP/REPAIR` verdicts for custody,
coordinate/Jacobian sign, native face, general recurrence, squarefree
uniqueness/divisibility, `G2` coefficient formula, cusp normalization/map,
fibre ODE/generic-finite scope, both formal mutations, polynomial provenance
rejection, determinant carrier, global `13H/12` gap, and final scope.  Give
the smallest failing identity, root, source exponent, or missing hypothesis
and the minimal additive repair if anything fails.

Desk-scale hashes and exact arithmetic only.  Write the complete review to
exactly

`xmodel/ggv-8_28-keller-face-cusp-jet-pinning-hostile-review-grok-20260827.md`

and touch no other campaign artifact.
