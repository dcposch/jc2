# Disabled uniform-parameter elimination contract

Status: source-only, `INTERNAL-UNREVIEWED`, `DISABLED/UNBOUND`.

The generator works once over `Q(nu)[X,Y,z]`. It derives coefficients through
degree 7 from `phi*T'=s*phi'*T`, derives `phi'/phi` through degree 14 by formal
series inversion, and forms the stipulated coefficient `B`. It asks whether

`(d6,d7,B,z*Y*d5-1)=(1)`.

On a generic unit result, `lift` must emit cofactors and the generator clears
every rational-function coefficient denominator by their product `N(nu)`.
The retained identity is

`A1*d6 + A2*d7 + A3*B + A4*(z*Y*d5-1) = N(nu)`.

The separate checker reconstructs every source polynomial and checks this
identity exactly. It factors `N` over `Q[nu]`, records all factors, and rejects
any linear root corresponding to `nu=(5r+2)/(3r+1)` for an integer `r>=2` via
`r=(2-nu)/(3nu-5)`. Irreducible nonlinear factors have no rational roots.
The `nu=5/3` root, if present, is reported but excluded because it has no
finite integer `r`; the known cube control is not hidden. This discrete
predicate is exact even if `N` has irrational real roots in
`(5/3,12/7]`. A stronger whole-real-interval nonvanishing claim is not made.

Interpretation: checker pass proves only that generic unitness specializes to
every actual integer parameter without crossing a retained denominator. A
generic unit over `Q(nu)` without checker pass proves no all-r result. Generic
nonunit, timeout, malformed lift, `N=0`, identity failure, or an actual-r
denominator root is terminal `GAP`; it is not a source point or counterexample.

Future execution requires a different-model source review, hashes bound into
`run-aws.template.sh`, genuine ROOT registration, complete native/source pin
closure, an ordinary interpreter/tool invocation, a fresh AWS host, and the
campaign's reviewed independent cap/cleanup machinery. The wrapper's EC2 DMI
test occurs before `exec` of Singular; it is necessary, not sufficient
authority. Proposed one-job envelope (unexecuted and unregistered): wall
3600s, CPU 3300s, memory 34359738368 bytes, aggregate output 268435456 bytes,
one worker/process group. Stop after one generic run and one checker run; no
prime, parameter, interpolation, or retry farm.

Outputs to retain: complete stdout/stderr, `RESULT.txt`, `certificate.sing`,
`DENOMINATOR-FACTORS.txt`, source/native/registration hashes, cap telemetry,
and identity-validated cleanup receipt. No result alone implies the forcing
attachment, REG, source zero, all F10, or JC2.
