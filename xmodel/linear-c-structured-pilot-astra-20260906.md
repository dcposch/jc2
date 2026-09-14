# Structured C-prefix discriminator: no construction win in this generation

2026-09-06. Producer: Astra, /root/nonemptiness_certificate.
Evidence: exact Q prefix reconstruction and closed-partial measurement.
The 189-pivot dependency remains PROVISIONAL pending its independent gate.
Verdict: NO_CONSTRUCTION_WIN_PREFIX24 / WALL_TIMEOUT. No solve was launched.

The first three high-degree C blocks are extremely cheap: 24 reconstructed
coordinates occupy only414 exact terms, maximum degree3 in the h-lift ring.
But substituting that prefix into the remaining Jacobian coefficients is not
a construction improvement in this measured implementation. The stream reached
its300-second wall cap while still at physical Jacobian degree70. Its829
complete emitted generators already contain9,967,234 terms. The earlier
complete600-variable presentation contained11,299,180 terms and was exported
in137.145 seconds.

Keep the tiny prefix reconstruction as a reusable block. Do not extend this
direct expanded stream automatically, and do not mistake it for a complete
smaller ideal. This result does not refute the constant-pivot theorem or all
possible circuit-preserving designs.

## Exact experiment, fixed before the run

Only the frozen (99,66),delta2 source was used:

- source SHA256:
  778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea;
- 192-column filtered basis/minor certificate SHA256:
  c2b5965278e0fa30f0490b7f5a019434abe5291e50b748d3a3c0795c8175f906;
- dependency report:
  xmodel/linear-c-filtered-pilot-astra-20260906.md,
  full SHA256 dbfa3716deb005f68858984ffab01d1897ebc64e0c0f56b2d0062628497a4119.

The physical source reconstruction is unchanged:
X=x,W=y-x; normalizers11,22,33,65,98 for h3,C2,C3,B2,A3;
h=h3^3+C2*h3+C3, D=physical(B2), C=physical(A3). Set

    G=h^2-bh/3+D,
    K=((3D+a+bh)/2) J(h,D),
    J(F,G)=K+J(C,G).

The source residual list is empty. All coefficients are polynomials over Q.
Physical degrees are exactly99,66 for F,G and at most99 for their Jacobian.
There is no new chart, parameter specialization or localization.

The same160 monic h-coefficient definitions as in the earlier lifted
presentation are retained. Reconstruct ONLY the first24 selected C coordinates,
covering physical C degrees35,34,33, using the certified unit lower-triangular
matrix evaluated on the actual lifted G coefficients. All165 lower active C
coordinates remain explicit q nodes, together with v22,v11. The unused additive
constant is removed. Thus the coefficient ring has

    247 base-source +160 h-lift +165 q +2 v +1 Zj =575 variables.

No unrestricted189-fold substitution was attempted. Prefix caps were100,000
terms per reconstructed coordinate and500,000 terms in total. Remaining-row
caps were100,000 terms per row and12,000,000 total terms; the external
300-second/8-GiB process cap fired first. These limits were not raised.

Under the provisional pivot theorem, recursively substituting these24
coordinates is an exact global graph elimination over the base ring. The
producer independently recomputed the corresponding24 physical Jacobian
coefficients from C,G and checked all were identically zero.

The planned full residual presentation still consists of EVERY remaining
positive-degree coefficient of K+J(C,G), the160 h definitions, and
Zj*J0-1. No smaller-equation criterion replaces this contract. The actual
retained stream is incomplete.

## Exact prefix and measured residual growth

The completed prefix is:

| C degree | Reconstructed coordinates | Exact terms | Maximum h-lift degree |
|---|---:|---:|---:|
| 35 | 7 | 34 | 2 |
| 34 | 8 | 96 | 2 |
| 33 | 9 | 284 | 3 |
| Total | 24 | 414 | 3 |

The prefix loop took0.00604 seconds after lifted-base construction.
The whole run had reached prefix completion at0.545 seconds. Its largest
reconstructed coordinate has96 terms; one coordinate is identically zero.
The resulting C has199 nonzero physical coefficients and1,736 terms, maximum
h-lift degree3. These are actual expanded Q counts, not DAG upper bounds.

The residual stream was ordered by descending physical Jacobian degree.
Selected measured checkpoints were:

| Last physical degree | Emitted terms, including definitions/inverse | Payload wall |
|---|---:|---:|
| 90 | 427,241 | 4.67 s |
| 81 | 2,768,731 | 43.53 s |
| 77 | 5,254,973 | 99.35 s |
| 74 | 6,659,157 | 139.87 s |
| 72 | 8,286,720 | 202.92 s |

The supervisor stopped the run at300.081 seconds, with exact-PGID identity
confirmation, TERM and complete cleanup. Peak sampled process-group RSS was
2,200,305,664 bytes, about2.05 GiB. There was no RAM-cap event.

A read-only exact parse AFTER writer termination found:

- 829 complete generators:160 h definitions,1 inverse row,668 positive J rows;
- 9,967,234 literal terms, ending at J_10_60, physical degree70;
- largest retained J row:76,969 terms, h-lift degree5;
- no malformed or partially written final line, but NO terminal completion
  footer and many required rows not emitted.

Every closed generator was reparsed in FLINT over the explicit Q/575-variable
ring, and its exact term count and degree were checked. The414-term prefix
was also reparsed. This audit took77.16 seconds, peak219.4 MiB; it did not
resume the expansion or solve any equations.

The full earlier presentation in
xmodel/factored-jacobian-pilot-astra-20260906.md had600 variables,1,629
generators,11,299,180 terms, maximum J-row size30,218 and J degree4. Its complete
export took137.145 seconds with1.71-GiB process high-water. The new partial
presentation reduces only25 variables and has already produced a J row over
2.5 times as large and one degree higher.

Timing used the same worker but was not a repeated isolated benchmark;
concurrent independent review work may have existed. The row sizes and
degrees are exact structural measurements. The missing total term count is
NOT extrapolated. Also, this pilot combines a rational C-basis change and
prefix substitution; it does not isolate their separate contributions to
the growth. The defensible conclusion is no demonstrated construction
advantage for THIS direct-prefix expansion, not a universal impossibility.

## Constant Jacobian and instrument controls

J0 was extracted separately and checked exactly against
F_X(0)G_W(0)-F_W(0)G_X(0) using the reconstructed physical linear jets.
It has12 terms and h-lift degree4. Zj*J0-1 was included near the start of the
stream, never replaced by J0=0 or omitted. The final audit reparsed it and
retained its linear-jet PASS record.

The first launch failed before arithmetic when the native polynomial-string
parser rejected a source expression. Its original script and child-exit1
telemetry are retained under the explicit initial-parser-failure filename.
A small exact AST parser repair accepts the pinned source syntax, rejects
parameter denominators and non-polynomial powers, and was rerun with unchanged
mathematical scope/caps. NORMAL_EXIT in that first supervisor record does NOT
mean the payload succeeded. This repair was not a second speculative
representation generation.

## Analytic shortcut: valid identities, no licensed polynomial truncation

The suggested square completion and target shear are exact. With

    s=h-b/6, E=D-b^2/36, A=a/2+b^2/8,
    R=C-bD/4+ab/12+b^3/54,

one has

    G=s^2+E,
    F-(b/2)G=s^3+(3E/2+A)s+R.

The target shear has determinant1 and preserves the Jacobian. It is an exact
polynomial coordinate expression over the source ring, not a specialization.

For the branch with leading term s, the formal binomial series gives

    G^(3/2)+A G^(1/2)
      =s^3+(3E/2+A)s
       +3E^2/(8s)-E^3/(16s^3)+AE/(2s)
       -AE^2/(8s^3)+...

The signs and rational coefficients were verified exactly. The displayed
correction terms have leading physical degree bounds35,3,1,-31 respectively;
the next E^4/s^5 term has bound-29. This potentially organizes a finite
nonnegative-degree homogeneous computation.

However, homogeneous truncation takes place in a rational-function
coefficient localization, not automatically in Q[X,W]. An exact attained
source-top negative control makes this concrete. Let
H=(X+W)^3 W^8 and choose B2c_47_13=1 with every other B2 parameter zero.
Then D_34=X^9 W^25, while s_top=H^3. The degree35 term is

    3 D_34^2/(8H^3) = 3 X^18 W^26 / (8(X+W)^9),

which is not a polynomial. Lower-degree corrections cannot repair that
highest homogeneous pole. This is an unconstrained SOURCE point, not a
claimed highest-face or Keller solution.

Accordingly no rational truncation was used as a source map in this pilot.
The polynomiality/divisibility conditions must still be imposed and proved
equivalent to the intended constraints. Likewise the matching leading degrees
of G^(1/3),G^(1/6) do not license identifying their formal truncations with the
actual polynomial free C columns. The identities remain potentially useful
organization, but this experiment establishes no computational shortcut from
them and drops no Jacobian row.

## Terminal custody and replay artifacts

All writers are DONE. No solver, instance launch, termination, retag or
second chart was used. The four capped subprocess records are: initial
parser failure; corrected producer WALL_TIMEOUT with cleanup; analytic
controls PASS; closed-stream exact audit PASS. Their total supervisor wall
was about377.9 seconds, below the900-second allowance. At most producer and
tiny analytic controls overlapped, within the16-GiB aggregate allowance.

Only the new directory
/home/ubuntu/linear-c-structured-pilot-20260906 on the existing root-owned
i-0da0cebfc97c9fd54,172.30.0.56 was written. Prior artifacts, Fable/Opus
scratch, live reports and all blind ideation submissions were untouched.
Root retains worker custody; the producer promises no further edits.
All new worker artifacts are read-only.

Key artifact hashes:

- prefix_reconstruction.jsonl,21,911 bytes:
  f405cc8d942d64cdf90e1f7d2b843c8435bc35f6305814c52d6a2af4174aff9b.
  Complete reusable24-coordinate block, copied locally.
- prefix_reduced_ideal.partial.jsonl,437,891,326 bytes:
  d13810f3af8789b6b2c1bd0098d28a2bdd3b9a4949d7a5dad0b538680b0bcb5f.
  INCOMPLETE worker-only stream, not a complete ideal.
- structured_prefix.py:
  6aa2a1b0e54223af6044c0a40e7c821caf2b042e6b0d0c46657ab316ddb7f8d7.
- analytic_controls.py:
  60903a74440288303a56161ca66f4d9fbd4137d64fe4df573914ce68821dab23.
- audit_closed_stream.py:
  8345597083c8f845857aee68f5e4956ce2a41af1bb943fa6c212bb1d42a6bfcd.

All file sizes/hashes, job caps/states, scope and no-live-edit promise are in
box/linear-c-structured-pilot-20260906/custody.json,
SHA256 b6c476d325b1f4eea6aebb12da0cf06e4839047166c93f2b4b0f41fea6d73b26.
Compact controls, telemetry and exact prefix bytes are local; the large
partial stream was not copied to math-hq.

Replay uses the registered worker environment and unchanged run_capped.py
with300-second/8-GiB per-command caps, as recorded in REGISTRATION.md.
Fresh-scratch replay requires a reviewed adjustment of the copied guard path,
not modification of charged artifacts. Do not automatically rerun or extend
this failed construction discriminator.

No complete reduced ideal, solver win, properness result or counterexample
has been obtained.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11222`.
- Body SHA-256:
  `eeb2a58adfb20ee97489c7e28af60f7a96c087982cd6432a5795fc0f1bbfe2f2`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
