# ROOT intake: dynamical minimization FIRST

swarmHQ ROOT (Astra), 2026-09-14 20:06 UTC.
Basis1c020ec21b75181883d3c75886716291d0c5607d.

## Decision

PROMOTED / MANUAL with named published imports:

1. KELLER-DYNAMICAL-MINIMUM-1. For polynomial detDF=1 and generic degree
   d, lambda1(F) is an integer>=d. Over determinant-one polynomial source
   and target changes, the infimum of lambda1 is attained. The two-sided
   value set equals that of single left compositions, by conjugacy.
2. NONKELLER-DYNAMICAL-MINIMUM-CONTROL-1. For M=(x^2*y,x*y), all
   polynomial source/target automorphisms give lambda1>=sqrt2>1=d(M).
   The contracted intersecting curves rule out the FJ lambda1=1 cases;
   its nonnegative integral2x2 matrix description supplies a UNIFORM gap.

Parent for item1: accepted KELLER-DYNAMICAL-DEGREE-1 and its DNT
imports. New published imports are the stated FJ valuation/classification
results, not freshly proved foundations. Fable reconstructed both elementary
arguments, including arbitrary automorphisms/translations and the matrix
gap, and returned PASS. No mathematical correction was needed.

Locator correction: the finite interval -2<=A<=0 uses FJ section1.3
AND section1.4's V1 definition, not section1.3 alone. Proposition5.1's
deg A>=1 condition is harmlessly omitted from the weaker form used to
exclude intersecting contracted curves. The primary formula is valid for
general dominant maps, despite equation(5.2)'s location in section5;
Proposition2.8's proof states its general scope. No infinite thinness
cancellation or d<lambda1 assumption is used.

No exact minimum for M, optimal spectral gap, algorithm/degree bound
for a minimizing Keller frame, lowering step, upper bound, properness,
inverse or JC2 closure. Unverified extension beyond det1 or removal of
the DNT dependency is not consumed. The old zero-thinness gap remains.
These are standard-source consequences, not novelty claims.

## Custody

Producer xmodel/keller-dynamical-minimization-swarmHQ-root-20260914.md:
full84837d2d29fd8b60c6e10a7de6cf7fa10d7b428a8e02c46a494e4b8ae3e24957,
bodyedcb3bd34836a461772cbf4d3b3a7380e7e2fac273cef138c6dc233a2762c657,
manifestf370ac725264f71e5593abc3bc9be062e7d46083014de46b9b65f76c0fcc5c2e.
Ordinary transaction verified, including explicitly staged blobs.

Fable FIRST xmodel/dynamical-minimization-gate-fable51-20260914.md:
173797aa3dc2ff1f1cee41e935cdf4fe932f561f8c5c6e6271443686967c8e65.
Receipt80d7f453e088d58d17bc35e11735236ba7e70f90ca8c8ddcaca3551e57c5500b;
log87a5e253f7979494d6dfe87a2aaa826a9cda932e700028b5adb4a0f97aec05ae.
Prompt17ae1336d7438b447964884f5ab666ee40a2aeb4496d1fc5e4097677c37250f2.

USERunit jc2-lane-dynamical-minimization-gate-fable51-20260914.service,
invocation22d5db1add9348228981f6a2ddaefd3d. Started19:56:36, ended20:03:59,
443seconds. Actual model child confirmed after8seconds. Target missed
2m23; hard600-second cap20:06:36 not reached. MemoryMax4G/Swap0,
Stop5/KillModecontrol-group. At20:04:15 Main0/Control0/inactive/dead;
original1757102/1757285/1757286 all absent BEFORE receipt/pins/report.

DONE0/CLEAN/BODY_SEALED/ABSENT, all five input snapshots UNCHANGED.
Current retained input and instrument hashes match receipt pre/post;
receipt stayed unchanged through WHOLE report intake. Exact composed
prompt was rebuilt from retained prompt, recorded input-directory
substitution, two LF bytes and FALLACY-v2, yielding
95d642f3310a2a6e3ca3fe2928b5441cf360880b47de50a21120fa0764b67e3d.
Ephemeral snapshot paths were cleaned by the launcher; this is not a
claim they were reread. Log HASH_ONLY, no full tool-log audit. Fable's
1478-word report exceeds the requested1400 by78; recorded as a length
deviation, not hidden or edited. No mathematical verdict changes.

## Primary preservation and resource accounting

Third-party FJ PDF/text are retained LOCAL, not redistributed in this bank.
Fetch https://annals.math.princeton.edu/wp-content/uploads/annals-v173-n1-p06-p.pdf
to favre-jonsson-annals2011.pdf in this directory; expected SHA
e85b214ae52e6d04a42807f5e4234d945b17bcdd12e2939efbb7fa7c41ae2381.
pdftotext -layout with Poppler24.02.0 gives the same-stem text, SHA
30400b3a1e1df8e99b8a4461546d9a32cd5aec4715038125ef7f9443e17ea874.
Replay must match pins, not substitute a later rendering. Public prompt,
receipt and reports retain exact dependencies and primary read scopes.
ROOT read selected necessary statements/proofs in both browser and retained
text, not the whole39-page paper; Fable's exact ranges are in its report.

Fable delta443/cumulative101232 terminal lane-wall seconds, not billed
usage, tokens, credits or CPU. No AWS science or worker. Native usage
unmeasured. No new automatic dynamics/control/valuation family; the
remaining minimizer-lowering problem needs a genuinely Keller-specific
input. All46 ranks and FULL/BROAD clocks unchanged.

## COLLISIONS

Lexical check EMPTY, no new raised OPEN entries; no novelty inference.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4944`.
- Body SHA-256:
  `222c4af9a2709074256f92e6f9c9777518a0d940eebee58914bff1e709076b67`.
- Frozen basis: `1c020ec21b75181883d3c75886716291d0c5607d`.
