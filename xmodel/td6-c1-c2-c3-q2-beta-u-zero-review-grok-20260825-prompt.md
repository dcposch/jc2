# Hostile bounded review charge: TD6 fixed-A3 q2-beta whole `U=0`

Act as an adversarial algebra/source/custody reviewer.  Read-only, bounded
audit: do not edit producer/canonical files and do not run the substantive
replay or any local CAS/heavy computation.  You may hash, extract the archive
to private `/tmp`, inspect source, and do short hand checks.  Write only the
requested review report.

Read in full:

- `xmodel/td6-c1-c2-c3-q2-beta-u-zero-aws-20260825.md`;
- `cases/td6_c1_c2_c3_q2_beta_u_zero_aws_20260825/README.md`;
- that case's `DEPENDENCIES.sha256`, `MANIFEST.sha256`, `FREEZE.sha256`, all
  frozen evidence, and portable source archive;
- the archive's source manifests, V33 producer, and exact imported parent
  portions that define the center, transport, direct q-prime term, first
  original rows, compatibility gcd/Bezout, and source certificate.

Adversarially verify or refute:

1. Exact source scope: fixed normalized A3 center `(C,V,U)`, raw `U=0`
   specialization with `C,V` retained, `q_beta=t+beta*t^2+t^25` and
   `q_beta'=1+2 beta t+25t^24`, frozen remaining TD6 moduli.
2. Transport rank `3470/3602`, first rank `36/132`, and exactly the dependent
   original first row `('X-2',14)` used by the incompatibility.
3. Its compatibility is beta-degree zero, the original 14-row source
   combination replays exactly, and the compatibility ideal has monic gcd
   `1` with exact Bezout identity.  Check signs and that this is an original-
   row certificate rather than only an echelon assertion.
4. The complete certificate denominator is really `1`, including any
   `C,V`, constant-field, normalizer, or Bezout denominator.  Check that no
   exceptional beta/C/V stratum is silently discarded.
5. Custody: dependency/freeze/manifest/source hashes, rc=0, stdout/stderr,
   source-check closure, and whether the archive contains the actual code
   run.
6. Scope: strongest allowed result is the entire `U=0` center divisor empty
   for every beta over extensions of `E`, but only in the fixed normalized
   A3 q2-beta section.  It does not cover `U!=0`, whole A3, other moduli,
   TD6, SP-2, landing, or JC2.

Try to flip through source specialization, q-prime omission, rank/dependency
mistyping, beta specialization, gcd/Bezout sign, hidden denominator, source-
row ancestry, archive mismatch, or scope overreach.  Separate theorem defects
from expository/custody nits.

Write
`xmodel/td6-c1-c2-c3-q2-beta-u-zero-review-grok-20260825.md` and end with
exactly one verdict token on its own line: `CONFIRMED`,
`CONFIRMED_WITH_REPAIRS`, or `FAILED`.
