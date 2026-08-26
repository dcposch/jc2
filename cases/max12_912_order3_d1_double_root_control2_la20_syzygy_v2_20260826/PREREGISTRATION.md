# Preregistration: repaired LPDP `la^20` witness

- Scope: the single fixed control-2 source/support/weight already certified by
  corrected A: `a=1`, `h=q2=k=nu=0`, `mu=2/3`, weight
  `(4,1,1,22,22,30,30,30)` on `(la,tau,rho,q1,q0,r2,r1,r0)`.
- Input: the nine exact expanded Rees generators `E1,...,E8,LT` from frozen B.
- Only source repair from quarantined V1: replace the four uses of reserved
  identifier `GCD` by `CDSTD`; the AWS tag is also replaced. The compiler must
  reconstruct and hash-match the exact V1 source before applying this diff.
- Algorithm: compute `C=I:s^infinity` with `sat_with_exp`; verify it equals a
  direct `sat`; express `la^20` in `(C,s)`; lift only used `C` generators back
  to `I` after the certified saturation exponent; print and exactly check the
  resulting Rees identity and its `s=1` witness.
- Positive endpoint: all explicit lift identities reduce to literal zero,
  required PASS markers occur exactly once, rc is zero, stderr is empty, and
  the hardened stdout diagnostic file is empty.
- Negative endpoint: any hash, parser/CAS diagnostic, lift, marker, rc, timeout,
  or memory failure gives no verdict.
- Firewall: this run extracts a witness only. Cone stability is a separate
  global-`dp` job. It says nothing about moving loads/axis, another support or
  weight, the whole fan, D1 globally, or JC2.
