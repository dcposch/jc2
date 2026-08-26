# Preregistration: repaired global-`dp` `la^20` witness cone

- Scope/source/support/weight: exactly the same single fixed control-2 point as
  the LPDP witness preregistration.
- Input: the nine exact expanded Rees generators `E1,...,E8,LT` from frozen B.
- Order: one global `dp` block on `(s,la,tau,rho,q1,q0,r2,r1,r0)`, independent
  of the LPDP witness order.
- Only source repair from quarantined V1: replace four uses of reserved `GCD`
  by `CDSTD`; the AWS tag is also replaced. Before repair, reconstruct and
  hash-match the exact V1 global-`dp` source.
- Exact cone test: after an independently computed and checked Rees preimage,
  enumerate every term of the `s=1` witness. At the registered target weight,
  require no term below weight 80 and exactly one weight-80 monomial, `la^20`.
- Positive endpoint: all lift/equality and cone checks pass exactly once, rc is
  zero, stderr is empty, and the hardened stdout diagnostic file is empty.
- Negative endpoint: any source/hash/parser/CAS/lift/term/marker/rc/timeout or
  memory failure gives no verdict.
- Firewall: a successful result proves only that this explicit fixed-source
  witness has `la^20` as unique initial term at the registered weight, hence on
  the strict inequalities determined by its finite support. It is not the full
  Gröbner fan and does not cover moving parameters, other supports, or D1.
