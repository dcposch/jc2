# Preregistration: first transverse-cusp transport

Date: 2026-08-26 UTC

Restore exactly one omitted normal direction after full q2: fix the axis
`a=1`, put `p=-3`, `c=2+h`, so

```text
K=z^3-3z+2+h,
f=K^3+K*(q2*z^2+q1*z+q0)+(r2*z^2+r1*z+r0).
```

Keep fixed loads `k=nu=0,mu=2/3`, exact targets, all eight charged ordinary
tails, and the corrected q2 multipliers

```text
F1'=F1+q2/12, F2'=F2-q2/9, Fi'=Fi (i>=3).
```

Construct the full polynomial `W_h=sum F_i' E_i(h)` from the hash-pinned
ordinary source.  Require `W_h|h=0` to equal the reviewed corrected q2
witness with canonical SHA
`ddb451c4d591f312a27b34ba517235a684c53f2884040624abe704ac243ab33b`.
Factor the exact difference by h, retain every monomial/coefficient, and emit
the full affine weight forms in `(alpha,beta,delta,eta)` where
`eta=wt(h)/L`.

At `alpha=15/2`, write `beta=5+u`, `delta=5+v`.  Determine exactly the
least threshold `eta_0` for which the unchanged corrected witness has unique
least term `la^20` uniformly for `u,v>0`; list every threshold face term.
If any term is below target for allowed `eta>0`, label the result only
`OLD_CORRECTED_WITNESS_DOES_NOT_TRANSPORT` and pass its first graded
coefficient to a new syzygy-lift problem.  Do not infer a surviving branch.

As a separate exact checksum, verify ordinary homogeneity of every charged
source monomial: row ell has weight `12+ell` under coefficient weights
`wt(a_i)=9-i`, `wt(kbar)=6`.  This supports, but does not by itself promote,
the unit-axis normalization

```text
f(z)->a^-9 f(a z), Lambda->a^-1 Lambda, rho->a^-1 rho.
```

Run forward/reverse traversals on two AWS hosts.  No local exact execution.
No moving-load, formal-lift, equality-face, whole fan, D1, or JC2 claim.
