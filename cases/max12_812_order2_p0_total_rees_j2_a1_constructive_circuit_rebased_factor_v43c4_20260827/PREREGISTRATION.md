# V43C4 preregistration: rebased exact circuit with factor-zero pruning

## Frozen question

In the ordinary polynomial ring `Q[X19_rho0]` on the frozen 65-variable raw
ordered-a1 alphabet, do the 51 named raw rows through grade 19 admit an exact
unsplit arithmetic-DAG certificate of `a1^104`?

This successor preserves the V43C3 derivation, including the exact assumption
rebasing

`e1 = (e1-4*a1*ell1) + 4*a1*ell1`,

`ee0 = (ee0+4*aa0*ell1) - 4*aa0*ell1`,

and every RowSpecialize, Add, Scale, Mul, ClearPower, CombineBranches,
checkpoint, literal-row custody check, and serialized replay guard.  The
frozen V43C3 run reached its final cleanup but exhausted its 4-GiB virtual
memory cap while naively expanding three large zero multipliers; it had no
mathematical verdict.

## Additive exact rule

`PruneZeroFactor(C, label, root, factor)` may delete a named generator term
only when all of the following are replayed exactly:

1. `label` occurs in certificate `C` with arithmetic-DAG root `root`;
2. `root` is literally a `Mul` node and `factor` is one of its direct children;
3. exact sparse expansion over Q of `factor` is the zero polynomial.

This is simply `root = factor * product(other children) = 0`; it is not a
probabilistic identity test and performs no localization.  Registered pairs,
from the exact V43C3F diagnostic, are

- `assume:ee1`: root 721 / factor 427;
- `assume:ez3`: root 723 / factor 401;
- `assume:rs2`: root 722 / factor 399.

The factors expanded to exact zero with peak sparse sizes 9, 3, and 3 terms.
The producer must replay these expansions and commit their telemetry.  It must
reject replacing each factor with direct nonzero factor 371 (`a1`).

## Pins and controls

- V43C2 invalidation and its additive freeze remain pinned exactly.
- V43C3F factor diagnostic SHA-256:
  `b9ebbaa4d73c12705096cad73a1c9e3b5b7a4c633a9dc94d7eaa86ff3d42b0cc`.
- Preserve the Tg19_7 final-row omission mutation, a ClearPower exponent
  mutation, and both `+4`/`-4` rebase-sign mutations.
- Final serialized replay must contain only literal raw-row labels and target
  exactly `a1^104`.

## Verdict and firewall

Only the exact terminal marker
`PASS-A1-RHO0-RAW-CONSTRUCTIVE-CIRCUIT-REBASED-FACTOR-A1-104-V43C4`,
with complete evidence hashes, is a provisional positive result.  It proves
only `a1^104` membership in the frozen rho-zero raw ideal.  It gives no
unspecialized-rho or saturated-Rees result without the separately reviewed
generic/special converter and an exact total replay.  Hostile review remains
required before promotion.

Run on AWS only, one core, 4 GiB virtual memory, ten minutes; fail closed on
any cap, exception, pin mismatch, or mutation acceptance.
