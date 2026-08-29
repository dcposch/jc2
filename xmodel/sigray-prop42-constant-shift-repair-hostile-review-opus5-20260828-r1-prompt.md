You are Opus 5 acting as a genuinely different-model hostile mathematical
reviewer in the plane Jacobian-conjecture campaign.  Work only in
`/Users/dc/code/math/jc2`.

Review this frozen producer, recomputing its live hash before reading:

```text
10bc55d53f9cf9a9e6a4535787f6e208a25f0ebfbd6dbd803f68b00f8ca8f5cd  xmodel/sigray-prop42-constant-shift-repair-sol-ultra-20260828.md
```

Frozen primary source and auxiliary exact artifacts:

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
8396a44c5f81f011a8a343124bd0de21329d0f1756a99fcf4cc9df718baf3e14  cases/sigray_prop42_constant_shift_repair_20260828/verify_constant_shift.py
c57abd5f0a49dd39fc1b2aa5acf763e3df7948d16034f867fb1aef6b52b0f183  cases/sigray_prop42_constant_shift_repair_20260828/CUSTODY.md
```

The checker should print PASS with grouped total 125788.  Re-run it, but do
not treat its output or the producer's conclusion as evidence.  Read the
primary source directly: at minimum printed pp. 13, 18--21, 29, 39--40, and
48--50, using the custody map.  You may read the charged parts of
`ladder/SIGRAY-AUDIT.md`, `xmodel/sol-landing1.md`,
`xmodel/sol-gluing-design.md`, and the typed source hostile review for
downstream scope, but those are not primary mathematical authority.

Reconstruct or refute the argument independently.  Charge every item below:

1. **Fiber residual.** Is `p_F` necessarily nonconstant for every genuine
   `F in T_a^+` in both charts?  Check the use of `f` versus `f-a`, zero next
   coefficient, axes, and finite truncations.
2. **Negative order.** For `f^+=xi^d p`, `H^+=xi^e q`, audit the transformed
   Jacobian and the implication at `e<0`.  Check denominator clearing and the
   derivative of `q^A p^B`; actively seek zero polynomials, monomials,
   cancellations, roots at infinity, and inverse/Laurent countermodels.
3. **Zero order and legality.** At `e=0`, prove or refute that `q` is a
   nonzero constant.  Decide whether `(k,l,s)=(1,0,c)` is unique under the
   exact coprimality convention, whether `f^0` is legal, and whether
   `h-c` remains a nonconstant global polynomial.
4. **Immediate termination.** Verify that the shifted member has negative
   leading order, nonzero leading Jacobian, satisfies the exact terminal
   equation (including harmless `C*` scalars), and forces `delta_next=0`, not
   merely `delta_next<delta`.  Check all alpha/index/off-by-one formulas.
5. **Degrees and typing.** Independently derive or refute
   `deg p_(h_m,F)=(mu-1)deg p_F+1`, the stated `M_F` gcd, and preservation of
   every slot of `Q(F)`.  Check rational `mu`, degree cancellation, degree
   zero, and whether any downstream theorem silently divides by the newly
   allowed `l=0` (especially Props. 4.4, 5.2, 6.3--6.4, Notation/Prop. 8.1,
   and the characteristic-sequence uses).  Distinguish definitional labels
   from propositions needing a separate patch.
6. **Pole-path scope.** Independently verify or refute the derivation that a
   constant corner forces `d_F>(1-u)deg p_F`, hence `T_a^nearrow`, and that
   the pole characteristic paths consumed by Statements 9.4--9.5 and
   Proposition 9.3 are indeed `T_a^searrow`.  Look for endpoint, root,
   equality, and chart exceptions.
7. **Firewalls.** Decide exactly what this repairs: Prop. 4.2 globally on
   `T_a^+`, only pole-spanned paths, or less.  Do not merge Prop. 4.3's
   `T_a^-`/condition-(7) tower with this result, and do not silently repair
   Prop. 5.1's finite-nonzero-puncture threshold gap, landing, coverage,
   bounded delay, a degree ceiling, or JC2.
8. **Checker quality.** Audit whether the checker supplies genuine mutation
   controls and whether its enumeration leaves a mathematical hole.  A
   theorem must rest on proof, not sampling.

If the result is correct only after a wording or downstream-typing repair,
give the smallest exact repair and downgrade accordingly.  State whether
`SIGRAY-AUDIT.md` may eventually change from `GAP` to an erratum with a
complete replacement, but do not edit it.

Write a self-contained report to exactly

`xmodel/sigray-prop42-constant-shift-repair-hostile-review-opus5-20260828-r1.md`

with terminal verdict exactly one of `PASS`, `REPAIR`, or `REFUTE`.  State
that you are Opus 5 and this is different-model review.  Include all live
hashes, exact source pages/statements, the checker replay, and a concise
downstream impact table.  Preserve the producer byte-for-byte.  Your only
write may be the required review; do not create another checker unless a
counterexample absolutely requires it.

Never enter, list, search, read, build, status, or modify `jc2-lean`.  Do not
edit any existing artifact or any canonical/top-level file.  Do not use web,
AWS, or heavy local CAS.  Preserve the dirty shared worktree.
