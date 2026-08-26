# TD6 V77R corrected pure-q3 scalar audit

**Producer verdict:** exact dual-AWS PASS, hostile review pending.  **Scope:**
strictly the first-order q3 source audit at `beta=gamma=0` on the fixed
source-typed A3 generic open `D(U*(C-3U^2)*B3)`.

The corrected source sets the legacy q2 coordinate `qd.B` to zero and pins
the actual q3 coordinate through the singleton original transport source
`('g','X',0,3)` together with the direct q-prime term `3*gamma*t^2`.
Changing stale `qd.B` after replacement of `Q_PRIME` is proved inert; a real
q2 leak through `Q_PRIME[1]` is separately detected.  Thus the prior concern
about hidden q2 contamination is resolved in the clean source.

Both independent AWS executions returned rc 0.  Their raw stdout hashes are
`9f3be97b...` (Box02) and `1d05d1be...` (r6d); after deleting only the three
`aws_platform`, `aws_hostname`, and `aws_run_tag` environment banner lines,
the bytes agree exactly with SHA-256
`f6aaf1c9f4e9f1e6961525a5cf79fd53ac4e3ee226520e34d652a7642fdabf1e`.

Exact endpoints:

- transport rank `3470/3602` and first rank `38/132`;
- the selected first-minor q3 derivative is **zero**.  The digest
  `c0730fa1...` is explicitly replayed as the canonical zero serialization;
- genuine P12 q3 derivative: four terms, SHA `70d253cd...`;
- reduced q3 remainder: three affine terms, SHA `3dd07bb5...`, over base
  remainder `-k/50`;
- exact original-row source identity: 28 supporting rows, 14 lambda-prime
  rows, with omission of lambda-prime detected;
- termwise clearing: 77,512 slots; denominator radical supported only on
  `U`, `C-3U^2`, and `B3`.

The square-zero remainder is a unit because the base remainder is already a
unit; this is the base change of the reviewed fixed-A3 emptiness, not a new
gamma-neighborhood conclusion.  The nonzero affine derivative is useful
source/Fitting input for a simultaneous nonlinear successor, while the zero
selected-minor derivative rules out claiming first-minor rank growth.

The first V79a dual run is preserved as a software-control negative.  It
changed only stale `qd.B` and correctly saw no row change, so its assertion
failed before q3 mathematics.  V79b replaces it with a genuine `Q_PRIME`
q2 leak and passes.

**Firewall:** no finite gamma neighborhood, full gamma family, higher-q
family, full TD6, SP-2, or JC2 claim follows.

Frozen case:
`cases/td6_c1_c2_c3_q3_gamma_dual_repaired_v77r_aws_20260826/`.
