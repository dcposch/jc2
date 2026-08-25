# Corrected-Q8 unloaded overlap: exact normal-rank/Fitting split

Date: 2026-08-25  
Status: **PRODUCER-EXACT; REVIEW PENDING**

## Scope and source

On the raw special-fibre overlap

```text
A3: w=x1=x3=x5=0
```

of the hash-pinned six-row corrected-Q8 source, let `M` be the `6 x 3`
normal Jacobian in `(x1,x3,x5)` and let `N=[M|F_w]`.  This report computes
the exact-Q Fitting stratification for ordinary tangents with
`delta w=1`.  It does not decide weighted/ramified arcs, horizontal
saturation, projective escape, Taylor/terminal realization, or trajectories.

## Rank-drop scheme

All six source rows vanish on `A3`, and their tangent columns in
`(c,d2,d4)` vanish there.  The ideal of all `3 x 3` minors of `M` has reduced
Groebner basis

```text
d2^2 - 2*d2*d4 + d4^2 - 2*d2 + 2*d4 + 1
  = (d2-d4-1)^2.
```

Thus the support of the normal-rank-drop scheme is the rational line
`d2-d4=1`, with the displayed doubled scheme structure.  In particular,
the previously contemplated blanket rank-three statement on all of `A3`
is false and is quarantined.

## Exact rank-stratified tangent incidence

Using all Fitting minors, the four incidence closures are

```text
K3 = I4(N) : I3(M)^infinity,
K2 = (I3(M)+I3(N)) : I2(M)^infinity,
K1 = (I2(M)+I2(N)) : I1(M)^infinity,
K0 = I1(M) + (entries of F_w).
```

Both exact-Q engines return

```text
K3 = (d2,d4),
K2 = K1 = K0 = (1).
```

The origin is off the rank-drop line, so it lies in the exact rank-three
stratum.  Localizations of `K3` at `D(d2)` and `D(d4)` are empty.  On every
lower exact-rank stratum there is no ordinary `delta w=1` tangent.  This
does not exclude ramified or weighted arcs through the rank-drop line,
because their first nonzero deformation need not be an ordinary tangent
with `w` as uniformizer.

## AWS endpoints and replay

Accepted exact-Q lanes:

```text
Box02 std/dp:
  input  680aae8ccae647552f8518f41a86a25f4c701b040f1b8e4590084ba655e2ac94
  stdout 2e5bf84301ff416c1b1134afd02ccfb81977a96408072416475ca712ede0d485
  wall 0.05 s, max RSS 12700 KiB

Box03 slimgb/block:
  input  2355ec4a339ebf1b2c1cd229baa951b4221f7b002a88ad43b5576e487ed21efb
  stdout 90a0b2574116bfa2189e7b8a6d2c6b3ee978b5b3b80cffff6966a11fb72a7e0c
  wall 0.03 s, max RSS 13548 KiB
```

The AWS-only fail-closed replay checks both endpoint and input hashes,
transitive source pins, unique bases and markers, zero return codes, and
absence of banned diagnostics.  It returns

```text
Q8_W0_OVERLAP_NORMAL_RANK_FITTING_REPLAY_PASS
```

with stdout SHA256
`c80c5c62bff716a84ab0ea20d2787bd061fc8fceee80623682419a80d598c54a`.

## Exact remaining gate

The ordinary first-order overlap is exhausted.  The only local finite gap
visible to this stratification is a genuinely ramified/weighted arc through
the rank-drop support `d2-d4=1`.  Its normal cone must be rebuilt from the
original six rows with `w` and the selected load
`x5*(x3-2*x5)` retained.  The still-running global selected saturation is
independent and remains decisive.

