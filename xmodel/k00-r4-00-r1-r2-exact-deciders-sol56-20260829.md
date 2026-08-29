# K00 V20R2 `R4-00`: exact AWS deciders for the typed-open R1/R2 residuals

Author: Sol 5.6 Ultra (exact producer lane)  
Date: 2026-08-29 UTC  
Basis commit: `792eecb189e754046fd3db054cefeae773f1a56d`  
Lifecycle: `SEALED PRODUCER-UNREVIEWED EXACT CANDIDATE / DIFFERENT-MODEL HOSTILE REVIEW REQUIRED`

## 0. Producer result

The independently rebuilt full grade-19 packets for CELL-R2 and both
Gaussian CELL-R1 branches have replayed exact characteristic-zero unit
certificates.  The certificate in all three routes is the same short literal
row identity:

```text
Jdet_0 = -(s1/64) G1,14 -(s/64) G1,15
          -(5/256) G1,19 -(3/32) G3,19 -(1/2) G5,19 - 4 G7,19.
```

Here every `Gi,n` is the literal, unnormalized coefficient row rebuilt from
the frozen tails/compiler, after the previously certified grade-12/13/14
forcing and the route substitution.  Thus all imposed rows force
`Jdet_0=0`, contradicting the residual survival open `Jdet_0!=0`.

Producer conclusion, pending the required hostile review: both typed-open
grade-19 residuals are empty.  This conclusion does not depend on the
still-running base-locus decompositions and does not consume any modular
`msolve` `[1]` output.

## 1. Literal reconstruction and packets

The packet builder expands the seven affine rows independently from all 569
frozen tails using exact rational sparse arithmetic, the compiler's literal
coordinate normalization, load shifts, target signs, and truncation at
`Lambda^20`.  It does not treat the predecessor's formulas, numerical probes,
or residual prose as an oracle.  It retained the transverse `A6,B6,A7,B7`
variables long enough to check the grade-12 cone forcing, grade-13 `T` ladder,
and grade-14 forcing before setting them to zero.

Pinned source hashes:

```text
0ffc4f741eb2b6a8257dd90c47f194f950752150f57468d81a7779406ab60ed3
  xmodel/k00-r4-00-entry-solve-fable5-20260829.md
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py
```

Fail-closed producer tooling:

```text
5066dcd795b86de13cae8c3759390a1957f72dbc8eaa4a0a72eef6f974eded95  build_r400_packets.py
25ee4ff834fcd657c9d63fb12ab01d0b593b5f12bad4216d80570febe2ccb7b4  run_exact_packet.py
fb332338a4616b34662f0554e55d5a58ed0bd11722b41092ab3b44366ad2b814  run_packet_build_aws.sh
6f573e609cd39ec8285eb0ab9529667128ea4ed599d3a821994175128afaa156  run_r1_exact_aws.sh
0860cb84180cfeaccf21f971b4245693bc39acfbe42f0ff1270bdd1d21d5ba10  run_r2_exact_aws.sh
```

The exact packet hashes are:

```text
497e8c6bbc5b349242bf3db64a53a601fe41057f450edf9ebff47226528a8f03  R2_BASE_LIFT.json
a6bbfaf7b6b7ec0a593afaa71442d587c1392d285158ef2a011d006a1429bdbc  R1_PLUS_BASE_LIFT.json
260f93774ade8ff8d4efbbb26e2f1433490fd4e182426ad60450112205bb984f  R1_MINUS_BASE_LIFT.json
b1779268e8f23ffa2c7b64d2bf08e4f8abf2aeccc1bea3b9ecc15d4c657e24ef  R2_FULL_GRADE19.json
5d35bea68cd9c6356928a7f7a86b6eea321c96f2546e3288788b057ac053247d  R1_PLUS_FULL_GRADE19.json
b5ac1d235239b58233c58a2a01dd38d004bdd7e426da78399e928b399098d8ec  R1_MINUS_FULL_GRADE19.json
03680033ab60fa0597f55b6a8e413dc71c0b81f10f7f1c2528b8f1c50e3e42ec  SOURCE_CONTROLS.json
```

R2 full has 36 core rows and three Rabinowitsch open equations; each R1
full branch has `ii^2+1`, the same 36 residual rows, and three open equations.
The opens are encoded literally as `D*kappa!=0` (R2) or `q*kappa!=0` (R1),
`(s,t)!=(0,0)` via `s*ws+t*wt=1`, and `Jdet_0*jinv=1`.  R1 is serialized in
an ordinary exact-Q polynomial ring with `ii^2+1`; the two signs are checked
by `ii -> -ii` conjugation.

Controls include an independent direct exact evaluator of all 140 literal
row/grade slots on two deterministic fixtures, target-sign mutation, a
row-4 tail mutation, support checks for every claimed inert variable, and
packet hash gates.  A first build stopped before packet or CAS output because
its R1 `c21` cancellation check was mistakenly made before canonical
reduction modulo `ii^2+1`.  The builder was repaired to reduce first and then
rebuilt byte-exactly.  This was a fail-closed tooling error, not a discovered
source error.

## 2. Exact characteristic-zero certificates

Each AWS worker ran Singular 4.3.2 over characteristic zero.  It computed a
unit cofactor vector and a fresh second Singular process replayed that vector
against the original ordered generators.  A deliberate mutation of one used
generator failed the identity.  No `msolve` basis or modular screen was
consumed.

For the primitive-integer packet generators the nonzero cofactor entries are:

```text
R2:
  G1_14  +(s1*jinv)/262144       G1_15  -(s*jinv)/262144
  G1_19  -(5*jinv)/2097152      G3_19  +(3*jinv)/2097152
  G5_19  +(jinv)/2097152        G7_19  +(jinv)/2097152
  OPEN_JDET  +1

R1+:
  G1_14  -(s1*jinv)/2359296     G1_15  -(s*jinv)/2359296
  G1_19  +(5*jinv)/37748736     G3_19  -(jinv)/12582912
  G5_19  +(jinv)/37748736       G7_19  +(jinv)/37748736
  OPEN_JDET  +1

R1-:
  as R1+, except G1_15 = +(s*jinv)/2359296; OPEN_JDET = +1.
```

Combining these with each generator's frozen primitive normalization gives
the displayed literal identity.  A separate exact rational dictionary check
of that translated identity passed independently on all three JSON packets.

Certificate artifacts and endpoints:

```text
R2 full  Box02 launcher 449680, CAPRUN/worker PGID 449714
  certificate e46018d8ebfd23f891872a61830d3417fe76dc3fa73bf0753287abf20fdb82a0
  NORMAL_EXIT, replay PASS, 3.343 s, max group RSS 81,825,792 bytes

R1+ full Box03 launcher 382030, CAPRUN/worker PGID 382066
  certificate 49ae6a1ed16ab3189536cfb186c27782816c768cd23171274409d1db78d7494f
  NORMAL_EXIT, replay PASS, 2.839 s, max group RSS 65,310,720 bytes

R1- full Box03 launcher 382145, CAPRUN/worker PGID 382182
  certificate 785c013cac41e3df886dcf3c8b8928d6af9a6991e0630a053abfd722e6f7c415
  NORMAL_EXIT, replay PASS, 2.715 s, max group RSS 65,687,552 bytes
```

Remote job roots are `/home/ubuntu/r400_20260829/jobs/r2_full_v1` on Box02
and `/home/ubuntu/r400_20260829/jobs/r1_{plus,minus}_full_v1` on Box03.
The locally frozen copies are below
`cases/max12_812_order2_u2_62_k00_r400_exact_deciders_20260829/frozen/`.
The 66-file manifest
`FULL_DECIDER_FREEZE.sha256` has SHA-256
`a6e2b54fa0ca8ef3f96144d11c776a09d42175761be302745d02b8b14367ce79`;
all entries verified after retrieval.

## 3. AWS custody and live diagnostics

Only audited campaign hosts were used:

```text
Box02  i-010201a5da47795c4  34.203.207.55  x2idn.32xlarge
Box03  i-0ece0b9a3b4a7512f  98.80.65.144   r6i.16xlarge
```

At full-job launch Box02 had load `1.09` with about 2.13 TB available RAM
and no swap; Box03 had load `1.76` with about 521 GB available RAM and no
swap.  At 22:34 UTC the independent base diagnostics remained healthy:

```text
Box02 R2 base: launcher 448323, CAPRUN 448356, worker PGID 448357,
  Singular 448359; load 1.08; Singular RSS about 1.90 GB.
Box03 R1+ base: launcher 379369, CAPRUN 379402, worker PGID 379403,
  Singular 379405; R1- base: launcher 379465, CAPRUN 379498,
  worker PGID 379500, Singular 379502; load 2.29; each Singular RSS about 6 GB.
```

The base jobs distinguish base-locus properness/emptiness but cannot override
the full-packet `Jdet` contradiction.  They remain diagnostic and were not
stopped.  CAPRUN's 17-test descendant/TERM/KILL/no-orphan regression passed
on both hosts before CAS launch.  No separate user formalization instance was
inspected or touched.

## 4. Maximum safe statement and review gate

If a different-model hostile review independently reconstructs the literal
rows, validates the grade-12/13/14 forcing and route substitutions, checks
the localizers, and replays or directly verifies the six-row identity with a
negative mutation, then CELL-R1 (both conjugate branches) and CELL-R2 are
empty as field-valued finite-jet cells through grade 19.  Together with the
already separate R0 exclusion, that would close the `R4-00` packet within the
frozen normalized support.

This producer report is not that review and is not promoted.  It says nothing
about nonreduced scheme structure, compatible infinite jets, formal arcs,
convergence, polynomial-map attainment, other supports or valuations, a
counterexample, or JC2.  No canonical ledger was edited.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8478`.
- Body SHA-256:
  `6e420952b432f6d22d676c98431cd7bc8842fe4c9ce8c28dca54828813862083`.
- Frozen basis: `792eecb189e754046fd3db054cefeae773f1a56d`.
