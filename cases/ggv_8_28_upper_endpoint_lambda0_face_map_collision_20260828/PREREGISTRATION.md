# Lambda-zero rescaled face-map collision screen preregistration

Date: 2026-08-28

This packet freezes a bounded collision discriminator for the lambda-zero face
before any AWS Groebner computation.  It does not consume any peer ideation
submission and does not change the fixed-q1 or HENS-CT namespaces.

## Exact map and scope

For each point `u=(a,b,c)` use the literal rescaled polynomial

```text
p_u(z)=(1+a*z)^2+b*z^3+c*z^4.
```

With shared lower modes `d1,d3,d4,d5` (and `d2=d6=0`), expand

```text
p^(3/2) + sum_{k in {1,3,4,5}} d_k z^k p^((6-k)/4).
```

Recursively choose the born modes `B7,B8,B9,B10` to cancel coefficients
seven through ten.  The frozen compiler independently asserts the root
derivation's identity `B10=0` as a zero polynomial.  The base collision ideal
therefore has only

```text
B7(u)-B7(v), B8(u)-B8(v), B9(u)-B9(v).
```

It is localized by `d1!=0` (the active `c2` condition) and by one of the three
charts `ua-va!=0`, `ub-vb!=0`, or `uc-vc!=0`.  These charts exactly cover the
off-diagonal locus.  The coefficient at order eleven is recorded as `rho`.
An optional second modular screen appends `rho(u)-rho(v)=0`; this only tests
collisions that also have equal rho and is not a symbolic-delta classification.

## Frozen desk validation

The compiler source hash is

```text
e5ecc267f4ee5393dca0e2afb3e2a6ccd253e6048528f6dc6c75e72e0c6b7c00  compile_face_collision.py
```

Its standard-library desk check completed locally in under one second and has
stdout SHA-256

```text
b840d7f2954bdf63bfe51a087896c04efe5dc4a7469c0ce4334eccc78dce1a50  DESK_CHECK.stdout
```

At the independently converted seed `a=-1/16,b=c=0,d1=d3=1`, it reproduces

```text
B7=-6139/17179869184, B8=0,
B9=16369/140737488355328, B10=0,
rho=9207/144115188075855872.
```

The exact encoded formulas, their individual hashes, and generated Singular
inputs are produced afresh on AWS.  The pinned recurrence sources are listed
in `SOURCE.sha256` and rechecked inside the compiler.

## AWS-only bounded screen

Run only on an audited idle Amazon EC2 Linux host in a fresh namespace.  The
registered first host is r6a, `ip-172-30-0-34`, instance
`i-02cb2b4a379ffcc64`, product `r6i.16xlarge`.  Require one core, exactly zero
swap before and after every stage, at least 450 GiB available RAM, at least
100 GiB free disk, a 32-GiB address-space cap, an 8-GiB file-size cap, a
one-hour master wall cap, and a PID/PGID/SID/starttime guard with no orphans.

Order:

1. replay every source hash and the desk check;
2. compile the exact map and all three off-diagonal chart inputs;
3. run the base chart ideal at primes `65521,65519,65497`, each with a
   180-second cap;
4. if at least two primes are nonunit on a chart, label that chart a modular
   collision candidate, run at most one capped `minAssGTZ` factor screen at
   `65521`, and run the three rho-equal modular screens;
5. only if all three primes are unit on a chart, run the tracked exact-Q ideal
   with a 900-second cap.  An exact-empty chart requires both standard-basis
   replay and a replayed unit cofactor certificate.

No modular nonunit or factor is promoted to a rational collision.  Global
off-diagonal emptiness requires exact replayed unit certificates on all three
charts.  A modular survivor is only evidence that the map is not eliminated
by this screen.  Timeout, resource cap, source drift, host/job conflict,
nonzero swap, Singular disagreement, or missing replay yields `NO-VERDICT`.

No raw endpoint survivor, primitive-value collision, family landing, Keller
theorem, JC2 conclusion, HENS result, `jc2-lean` change, or canonical-file
change is in scope.
