# Hostile different-model review — AS109 wild-symplectic completed-bidisc gate

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
artifacts on top. Read in full:

- `xmodel/as109-wild-symplectic-conductor-gate-20260824.md`
- every file under `cases/as109_wild_symplectic_gate_20260824/`
- the reviewed AS109 Hensel/degree and `A_infinity` parent reports named by
  the manifest
- Stacks Tags `0ALJ` and `09ZL`, checking the actual hypotheses rather than
  trusting the citations

Frozen hashes:

- producer report:
  `c7ad3660c136bbee7105e786cc8b717d025534b67ac63cababb33c4b6de29e7c`
- preregistration:
  `7a1cb33ac03676834adb6d490e1d5f6d31385818be64bd94eede177a18b38864`
- replay:
  `3c8d7d7c0c29d029f0d2bf098adb195f74e9ec85a097e9e9b97d231632bbc01e`
- manifest:
  `34ba6939c8daa2c4a386eafdc96d27e457f801d5de631c739ff0b41e2fe91a8c`

Rerun the registered replay, then independently attack:

1. **Tate-algebra map and basis.** Check that the substitution
   `Z_p<U,V> -> Z_p<x,y>` is injective and that reduction modulo `p` really is
   `F_p[x,y]` free of rank `p` over `F_p[x-x^p,y]`. Audit every completeness,
   convergence, torsion-freeness, and separatedness step in the successive
   division proof that `1,x,...,x^(p-1)` lifts to a finite free basis. Do not
   assume topological Nakayama without its hypotheses.
2. **Etaleness and torsor lifting.** Verify finite presentation/flatness and
   the Kahler/Jacobian argument. Read the Henselian-pair finite-etale
   equivalence and check it applies to `(B,pB)`. Determine whether individual
   translations, their group law, and the special torsor isomorphism all lift
   uniquely, yielding an actually free constant `C_p` action. Challenge the
   words `torsor`, `free`, and `unique` separately.
3. **Symplectic determinant and firewall.** Recompute the chain rule. Confirm
   that the action is determinant one on the restricted bidisc but supplies
   neither a rational/polynomial deck map, action on `A_infinity`, nor
   `d=p`. Find any hidden completion-to-global step.
4. **Completed right-equivalence.** For arbitrary two determinant-one
   restricted-analytic lifts with the same special fibre, check multivariate
   Hensel over the coefficient Tate algebra gives a unique
   `phi=id mod p` with `F o phi=G`; prove it is an automorphism and has
   determinant one. Attack composition order and whether uniqueness applies
   to the inverse equations. Verify `Z_p<x,y>/p^n=(Z/p^n)[x,y]` in the exact
   sense used. Decide whether the honest conclusion is one unrestricted
   completed gauge orbit, while minimal uniformly bounded representatives
   may still grow.
5. **First Witt digit.** Independently derive `N(a)=-1`, `N(b)=0`,
   `a_x+b_y=0`, `a=c-Delta(P1)`, `b=-Delta(Q1)`, and
   `P1_x+Q1_y=x^(p-1)`, including signs and the definition of `c`. Check that
   all solutions form one affine orbit under exactly the allowed
   divergence-free right gauges; distinguish map corrections from action
   corrections.
6. **Forced support floor.** Prove or break the universal coefficient claim
   `[x^(p-1)y]Q1=1`, including outside the registered `y<=1` rectangle and
   under all allowed first-digit gauges. Ensure characteristic-`p`
   differentiation, possible higher `y` rows, and polynomial versus formal
   primitives do not supply a loophole. Keep it a first-digit floor, not an
   unbounded-growth theorem.
7. **Independent finite compiler/control.** Write a second small exact engine
   or hand row reduction at `p=3,5`; verify dimensions `10/10/0` and
   `14/14/0`, the displayed carries, norm/order equations, determinant and
   invariance modulo `p^2`. Check the cotangent tower through depths 2--4 and
   its support lists without treating that representative as minimal.
8. **Scope and stop.** Decide whether `GAUGE-TRIVIAL/CONTROL-ONLY` is the exact
   admissible result. Quarantine a global deck action, `A_infinity=0`, fixed-
   support exclusion, p=109 brute force, lift construction, and JC2. State
   the smallest valid successor category precisely.

Do not edit producer/canonical/ladder files or launch AWS. Write exactly one
report:

`xmodel/as109-wild-symplectic-conductor-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim, with
hashes, independent checks, smallest failing statement, scope, and promotion
advice.
