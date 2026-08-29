You are Fable 5 acting as an independent hostile mathematical reviewer in the
plane Jacobian-conjecture campaign.  Work only in `/Users/dc/code/math/jc2`.
Do NOT enter, list, search, read, build, status, or modify `jc2-lean`.

Task: independently audit the frozen deep active-c2 D8--D15 repair/extension
from the authoritative fractional-power recurrence.  Do not trust or merely
replay the producer narrative/checker.  Reconstruct the recurrence and all
load-bearing coefficients yourself with a new self-contained Python
standard-library exact checker.  This is light desk algebra only: do not run
Singular, Sage, Mathematica, or any heavy/local parallel computation.

Frozen inputs (read-only; preserve bytes):

1. Authoritative recurrence implementation:
   `cases/ggv_8_28_upper_endpoint_q1_prefix_d7_d8_target_20260828/verify_q1_prefix_target.py`
   expected SHA256
   `fceb189badafad877c1142b8925480516111790707954d2000421b8190fde119`.
2. Original charged producer report/checker:
   `xmodel/ggv-upper-endpoint-active-c2-d8-d11-prefix-sol-ultra-20260828.md`
   SHA `e3b777f851dcb49c1a2caeafa3048fd20771319ecd9f74e8ca74321602b4d1f6`;
   `xmodel/ggv-upper-endpoint-active-c2-d8-d11-prefix-sol-ultra-20260828-check.py`
   SHA `00111feefcddd0532aa70204b69d90e5943b3e08b5ef7d97b44fcfa62f5b0372`.
3. Same-model audit/extension report and frozen case:
   `xmodel/ggv-upper-endpoint-active-c2-d8-d13-independent-audit-extension-20260828.md`
   SHA `da189b7fa2ce12656dfbd965c2ed76a0f26b90255a4c99e0fa1322d0c98d5577`;
   `cases/ggv_8_28_upper_endpoint_active_c2_d11_d13_extension_20260828/verify_active_c2_extension.py`
   SHA `112650dc27b0e13d76979d5adca9315919ee65cb8d9eaf717c1685f99d96de26`;
   its README SHA `c4c2263ec64f1a41ee0ae0f25a1fd5403a53a69041d9933950a300318ea60d2e`;
   RESULT SHA `568934cecfd224cfdff6f8af0791f71f54426ccc0fc5384fc4d0d90a2712c02e`.

Audit every load-bearing point below from the recurrence, not by importing
the producer checker.  Your checker may inspect/have hashes for frozen files,
but must implement its own sparse Laurent/polynomial arithmetic and
fractional-series recurrence.

A. Complete modes and setup

- Reconstruct `F^(3/2) + sum_{m=2,4,...,20} c_m t^m
  F^((12-m)/8)` through at least weight 15.
- Register all ten modes c2,c4,...,c20 and retain every born/predecessor mode;
  no mode may be deleted just because it is regular in an earlier row.
- Check the reduced prefix and substitutions are coefficientwise exact.

B. Charged D8--D11 identities and valuation repair

- On `V0=A*S`, `T=A*U`, `K=64F4-Z^2`, verify complete deepest D8
  `3K^2/(32768A^2)`, then after K=A*R complete remaining D8
  `-5c2(S^2-2Z)^3/(65536A)`.
- On c2!=0 and H=S^2-2Z=A*Q, with
  `D=R-4SU`, `P=256F5-RS+2S^2U`, verify complete D9
  `3DP/(65536A)` and deepest D10
  `3P(P-2SD)/(524288A^2)`, including the rootwise deduction A|P.
- With P=A*P1 verify complete residual D10
  `D(20c2D+3Egen)/(524288A)`, where
  `Egen=2048F6-2SP1+Q(R-8SU)-8U^2`.
- Verify deepest D11
  `D*B11/(1048576A^2)` with the displayed B11 in the extension report.
- Explicitly audit the repaired distinction: `A|D` alone is NOT the exact
  equation D=0 and generally leaves a simple pole.  Determine whether this is
  the only mathematical defect in the original charged report.

C. Exact D=0 paired forcing

- Impose the exact polynomial equation D=0 (not merely D mod A = 0).  Verify
  the COMPLETE negative D11 part
  `N11/(4194304A)` for
  `E=2048F6-2SP1-4QSU-8U^2`, `L=QS+4U`, `M=P1+2QU`,
  `N11=5c2*L*(4E+L^2)+6E*M`.
- Independently verify deepest D12
  `(3E^2-2S*N11)/(33554432A^2)`.
- Audit the characteristic-zero squarefree-root argument that D11+D12 force
  A|E and then A|L on the open c2!=0.  State exactly field/radical scope and
  whether any hidden unit/nonvanishing assumption is used.

D. Post-lift D12/D13

- With E=A*e1, L=A*ell and the resulting U,F6 substitutions, verify all D11
  poles vanish.
- Put `J=P1-SQ^2/2`, `N=8192F7-e1*S+QJ`.  Verify the COMPLETE remaining D12
  polar part `J(20c2J+3N)/(8388608A)` and entire A^-2 D13 class
  `-S*J(20c2J+3N)/(33554432A^2)`.
- Inspect the complete subleading D13 row enough to ensure no omitted mode
  invalidates the later literal survivor.

E. Literal raw D0--D15 survivor and legal windows

- Independently reconstruct the exact rational fixture in section 5 of the
  extension report, including c2=c6=1, the claimed c14, all F0..F15 and
  G0..G15.
- Check literally, as polynomials in X, D0=...=D15=0 and the legal windows
  `deg F_n <= 16-n`, `deg G_n <= 24-n` for every relevant n.
- Verify D14 really uniquely forces the displayed legal nonzero c14 under
  the stated frozen remaining data, and D15 then vanishes.  Verify G12--G15.
- Include mutations that separately catch: a wrong D8 factor/coefficient;
  treating A|D as D=0; dropping c6; wrong c14; perturbing F7; and at least one
  omitted born/predecessor mode.  Mutation assertions must fail for the
  intended reason.
- Be precise: the fixture is q1-free/non-q1 only if this is actually checked;
  otherwise label that claim unverified.

F. Separate c2=0 companion

- Without using the c2!=0 H-lift, verify complete c2=0 D9
  `3D*P0/(65536A)` and deepest D10
  `3[P0(P0-2SD)+H D^2]/(524288A^2)`, with
  `P0=256F5-RS+2S^2U+2UH`.
- Audit the field-rootwise conclusion A|P0 and H*D^2=0, and do not merge this
  stratum with the active open.

G. Deliverables and custody

Create, without modifying frozen inputs:

- `xmodel/ggv-upper-endpoint-active-c2-d8-d15-hostile-review-fable5-20260828.md`
- `xmodel/ggv-upper-endpoint-active-c2-d8-d15-hostile-review-fable5-20260828-check.py`
- directory
  `cases/ggv_8_28_upper_endpoint_active_c2_d8_d15_hostile_review_fable5_20260828/`
  containing `README.md`, `RESULT.json`, `SOURCE.sha256`, `EVIDENCE.sha256`,
  and either an independent verifier or a pinned copy/linkage to the xmodel
  checker.  Prefer one authoritative checker and make the replay command
  unambiguous.

Run your checker with `PYTHONDONTWRITEBYTECODE=1 python3 -B`.  Make it
self-contained, standard-library only, deterministic, and print one explicit
terminal marker.  Include positive identities and sensitivity mutations.
Compute hashes only after files are final.  SOURCE.sha256 must cover every
load-bearing executable/source dependency; EVIDENCE.sha256 must cover report,
README, RESULT, and checker as appropriate without self-referential hashes.
Verify all frozen input hashes again at the end.

Your report and RESULT must give one explicit verdict: PASS, REPAIR, or FAIL.
Any defect, even repairable, must be named precisely with mathematical impact.
Separate proven identity, field/radical consequence, literal fixture
existence, and anything merely suggestive.  Do not overclaim scheme
membership, endpoint emptiness, branch-P exclusion, Keller, or JC2.

Do the work autonomously.  At completion, respond concisely with verdict,
paths, hashes, replay output, and any defect.
