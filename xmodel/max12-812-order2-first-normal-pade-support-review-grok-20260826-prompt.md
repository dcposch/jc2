# Hostile review: exact nonzero-load Padé lemma and complete first-normal support

You are an independent hostile mathematical reviewer. Work in
`/Users/dc/code/math/jc2`. Read this target in full:

```text
xmodel/max12-812-order2-first-normal-pade-support-theorem-20260826.md
SHA-256 2c917b9fe9af3c23d615a3f9061a5c981d26e5e69a75138aacb33f308619ecf5
```

Read only the four frozen inputs pinned in target §0 as needed. Treat their
reviewed principal-part identity, unitriangular change, `k10=0` UFD
classification, and saturation facts as charged input; do not use the
two-prime modular calculations as evidence. Independently audit every new
step. Do not run CAS, Python algebra, Lean, or substantive computation. Do
not inspect or print the full dirty-worktree status.

Attack these points explicitly:

1. From `q1=...=q7=0`, check the exact Laurent order after passing from `w`
   to `z`, taking `P=[F]^z_+`, multiplying by `K`, and defining `A`. Check
   that this really forces precisely the `z^-1,z^-2,z^-3` coefficients of
   `K^(7/2)` to vanish when `k10!=0`; look for an off-by-one or branch error.
2. Independently expand the `t^15,t^16,t^17` coefficients of
   `(1+p*t^2+c*t^3+r*t^4)^(7/2)`. Verify both displays (1.7)--(1.9) and the
   substitution `d=p^2-4*r` term by term.
3. Independently verify (1.10)--(1.13), especially the coefficient `76`,
   and test both `c=0` and `c!=0` cases over characteristic zero.
4. Decide whether the conclusion is square over the base field, including
   the factor `p/2`, or only geometrically square.
5. Audit raw-support equality (2.2). In particular, verify that on the
   arbitrary-`k10` square locus the seven-row condition forces the displayed
   divisibility of `N`, and that no nonsquare `k10!=0`, zero-normal, or
   multiple-root family is omitted.
6. Audit saturation equality (3.2): identify which irreducible components
   are deleted by each multi-generator saturation and whether density really
   restores the complete affine closures of `Lsq` and `D`.
7. Check that (3.3) is exactly the previously conditional recovery and that
   the firewall does not claim a strict arc, higher-contact exclusion,
   order-two exclusion, `(8,12)`, maximum twelve, or JC2.

Give exactly one overall verdict: `CONFIRMED`, `REPAIR`, or `REFUTED`. If
not confirmed, identify the smallest failing identity or sentence and give
the clean exact correction. Pin the target SHA and all charged-input SHAs.
Explain the independent derivation sufficiently that coefficient agreement
is auditable.

The only permitted write is:

```text
xmodel/max12-812-order2-first-normal-pade-support-review-grok-20260826.md
```
