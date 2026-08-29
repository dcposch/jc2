# Preregistration: K00 local membership by global colon/syzygy V14

Date: 2026-08-27

Status: **FROZEN GLOBAL-COLON DISCRIMINATOR; NO RESULT AT REGISTRATION.**

Work at the reviewed normalized coefficient slice `C6=1` in
`R=Q[d0,...,d5]`, with maximal ideal `m=(d0,...,d5)`, unloaded tails
`r1,...,r7`, and `I=(r1,...,r6)`.  The local question has the exact global
reformulation

```text
r7 in I_m
  iff there exists h in (I:r7) with h(0) != 0
  iff (I:r7)+m = R.
```

V14 computes `C=(I:r7)` in a global `dp` ring.  Independently within the
producer it computes `syz(r1,...,r7)`, projects every syzygy to its seventh
coordinate, and requires that this projection generate the same ideal `C`.
Every syzygy and every colon-generator identity is replayed with the fixed
sign convention

```text
sum_{i=1}^6 L_i*r_i - h*r7 = 0.
```

The same ring first must show by toy controls that `d1` is globally absent
but locally present in `((1+d0)d1)`, while `d2` is locally absent.  The actual
source ideal must remain proper and `r7` globally nonmember, reproducing the
reviewed V8 control.

If `C+m=R`, save a generator `h` with `h(0)!=0` and its replayed lift; this is
an exact local-membership certificate.  If `C+m` is proper, every saved colon
generator must vanish at the origin; since they generate the full colon,
this is an exact local-nonmembership certificate.  Any failed equality,
replay, source pin, toy, or endpoint marker rejects the run.

The exact-Q AWS lane is mathematical evidence.  A separately serialized
`p=65521` lane is software/navigation control only.  Either result concerns
only unloaded local membership at normalized K00.  It does not decide mixed
Lambda/load/target reachability, closure-first incidence, Taylor realization,
order two, maximum twelve, or JC2.

