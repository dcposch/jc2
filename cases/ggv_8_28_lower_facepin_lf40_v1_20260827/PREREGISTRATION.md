# GGV `8_28` actual lower FACEPIN / LF40 exact sequential preregistration

Date: 2026-08-27  
Lane: `GGV-8_28-LF40-v1-reviewed-repair-targetfix-R1`  
Lifecycle: **producer-unreviewed; no result is promoted evidence pending independent review**

## Target-custody repair R1

The R0 JSON artifacts correctly encoded `Dtil_17=-1`, but the R0 Singular
serializer emitted the homogeneous polynomial `Dtil_17` at degree zero.  The
resulting AWS process therefore tested the wrong ideal and was terminated at
`2026-08-27T20:57:32Z` before any mathematical conclusion was consumed.  R1
changes exactly one solver generator, from

```text
f_0_1*g_1_0-f_1_0*g_0_1
```

to

```text
1+f_0_1*g_1_0-f_1_0*g_0_1.
```

All other generated payloads are byte-identical; only the Singular program
and its compiler evidence manifest change.  The compiler also carries a
fail-closed generated-program assertion for this target.  The complete
diagnosis, stopped-lane hashes, and replay evidence are in
`TARGETFIX_R1_ERRATUM.md`.

## Frozen mathematical object

The authoritative input is the literal raw pre-final pair

```text
f in 2S, g in 3S,
S=conv{(0,0),(1,0),(8,28),(0,4)}, J(f,g)=1,
F_0=a[ xi(xi-rho)^7 ]^2,
G_0=b[ xi(xi-rho)^7 ]^3,
a*b*rho != 0.
```

The desk gate consumes the reviewed repair rather than the unavailable
simple-edge route: the edge is **not simple**; the generated corner gives
`gamma=7`, hence `m_lambda=3*7=21=deg(pbar)`, which forces one nonzero root of
full multiplicity.  The typed ledger records both GGV22 defects: TeX line 1132
prints the mixed-frame `(1,0)` where the flipped vertex is `(0,1)`, and the
paper silently relabels P/Q after line 1110.  Compiler orientation is by
polygon (`2S` square, `3S` cube), never by source letter.

The degree-preserving hostile mutation

```text
K'=xi*(xi-rho)^6*(xi-rho2), rho*rho2*(rho-rho2)!=0
```

must pass degree, order, endpoint, and `Dtil_0=0` checks, then fail only the
single-root family pin.  The frozen desk replay instantiates `(rho,rho2)=(1,2)`.

The compiler emits all rows

```text
Dtil_n = sum_(r+s=n) ((12-s) F_r' G_s + (r-8) F_r G_s'), 0<=n<=40,
Dtil_17=-1, Dtil_n=0 for n!=17.
```

The raw and direct-coordinate engines are required to agree pairwise and
coefficientwise.  Frozen exact censuses are:

```text
442 raw slots = 141 F + 301 G
774 raw nonzero coefficient generators
34 raw row-0 positions, all killed identically by FACEPIN
405 positive slots + a,b,rho = 408 substituted variables
740 substituted target generators
row 39 = 1 generator; row 40 = structural zero
```

The coefficient ring is exactly `QQ[a,b,rho,405 slots]`.  Modular work is not
part of this lane and cannot yield a characteristic-zero verdict.

## Localization and solver object

Saturate by **exactly**

```text
a*b*rho*f_0_8*g_0_12.
```

No additional factor is licensed.  The exact test uses the one-equation
Rabinowitsch representation

```text
w*a*b*rho*f_0_8*g_0_12-1=0,
```

so its final literal system has **741 equations in 409 variables**.  No
normalization `a=1`, `b=1`, or `rho=1`, no `H=X^8-1`, and no D3 upper-face
equation is admitted.

Singular 4.3.2 runs over characteristic zero with `dp` and `slimgb`.  Starting
with the Rabinowitsch equation, it adds rows in the exact order `0,1,...,40`;
after each addition it computes an exact standard basis.  A prior basis may
replace the prior generator list because it generates the same ideal.

Stop at exactly one of:

1. the first row whose prefix standard basis contains `1`; preserve that
   basis and every completed earlier proper-prefix marker;
2. all rows through 40 with a proper exact standard basis; preserve that full
   basis as the lower-system fixture; or
3. the resource cap, which is `RESOURCE_CAP_NO_VERDICT`.

A row-17 or row-24 prefix is never a terminal fixture.  The synthetic proper
and forced-unit controls must pass before the main system.

## Frozen inputs

The charged report SHA is
`94c10fd8c95424d7161ef4b13b7321529109426282dd0da0da2c94f6594f61c7`.
The hostile review SHA is
`681357cef07f9b3fb053a320f72375f65a3c988369e002281e8179c4c874b950`.
`SOURCE_FREEZE_TARGETFIX_R1.sha256`, the deterministic desk-gate manifest, the
deterministic compiler manifest, and the target-fix R1 source-archive SHA are
mandatory remote inputs.
The remote runner regenerates both gate and compiler and requires byte-identical
manifests before invoking Singular.

The old `SOURCE_FREEZE.sha256` and unqualified source archive identify R0 and
must not be used for a mathematical run.  They remain available solely to
replay the retired wrong-target lane.

## Registered AWS envelope

Selected node after live audit: AWS `r6b`, instance
`i-0f089e64c378f5da3`, IP `34.204.74.226`, host `ip-172-30-0-106`,
`r6i.16xlarge`, us-east-1a.  Audit at `2026-08-27T18:47:45Z` found no Singular,
msolve, or campaign Python process; 527,184,838,656 bytes were available,
swap was zero/unconfigured, root disk had 190 GiB free, and Singular was
4.3.2.  Existing `/home/ubuntu/jobs` outputs are preserved; the lane uses a
fresh unique source directory and a fresh unique output directory.

```text
workers                  = 1
nice level               = 5
virtual-memory cap       = 503316480 KiB (480 GiB)
outer wall cap           = 43200 seconds
inner Singular wall cap  = 42600 seconds
required swap count      = 0
```

The source tree is made read-only.  Registration, EC2 identity, environment,
process/output snapshot, source/archive hashes, replay hashes, solver version,
stdout/stderr, wall/RSS/swap telemetry, validation, and a complete relative
evidence manifest are retained.

## Non-consumed checksum and scope firewall

The live Fable endpoint report suggests that lower row 17 can be compared,
after its own normalization, with the promoted `4K*g'-3K'*g` ODE.  That is an
independent checksum only.  It cannot modify the literal chart identity,
target sign, variables, equations, saturation, or row order frozen here; any
sign or scaling mismatch is reported rather than repaired in flight.

An exact unit result would conditionally remove the last `(72,108)` GGV case
(`9_27` is the already-discarded sibling) and, through GGV22's dichotomy, raise
that conditional lower bound from 108 to 125.  It would not prove arbitrary
GGV landing, a cofinal bound, `G2-PSC`, `G2-BD`, or JC2.  A proper full fixture
would be only a lower necessary-system survivor, not a chain point,
counterexample, or noninvertibility witness.
