# Preregistration: V24R4 modular tracked-certificate lift fallback

Date: 2026-08-27

Status: **FROZEN DESIGN; HELD, NO EXECUTION.**

Activation: only if the live tracked exact-Q V24R2 gate has no endpoint after
60 minutes, or on coordinator instruction.  V24R2 remains live and untouched.
This fallback may use spare Box02 cores but must stop if it creates material
memory contention.

## Objective

The localized V24 prior ideal is the unit ideal at every tested prime.  Learn
tracked modular Bezout multipliers, then attempt exact rational
reconstruction of those multiplier coefficients.  The only consumable PASS
is a fresh coefficientwise identity over `Q`; modular agreement, stable
support, and CRT reconstruction are discovery stages only.

## Frozen algebra

Use the exact same 35 prior generators and localization generator

```text
zinv*k10_0*W - 1
```

as V24R2.  Reconstruct them from the frozen rational V24 source lines; do not
reinterpret a file whose coefficients were first normalized as finite-field
residues.  Generator order, variable order, signs, `W`, and the restriction
`k6_0=0` are immutable.

Initial preregistered primes are

```text
1000003, 2147483629, 2147483587, 2147483579,
2147483563, 2147483549, 2147483543, 2147483497.
```

All are prime and avoid the frozen rational denominators.  Each is a separate
one-core, 64-GiB, 20-minute AWS job.

## Modular producer

For each prime `p`:

1. compute `G,T=liftstd(P)`;
2. replay `matrix(P)*T=matrix(G)`;
3. require `G=(1)` by exact finite-field normal form/dimension markers;
4. compute a 36-entry column `C_p` with `matrix(P)*C_p=1` and replay it;
5. serialize every multiplier as canonical sorted `(monomial,residue)` pairs;
6. fire a coefficient/sign mutation and a generator-order mutation.

No prime with a failed replay, changed generator support, resource cap, or
nonunit result enters reconstruction.

## Support comparison and exact lift

Compare the 36 multiplier supports across primes.  If a support is stable,
CRT each coefficient in that fixed labelled support.  Apply standard rational
reconstruction only within its uniqueness bound and only after at least four
independent primes.  Re-emit the resulting exact rational multiplier column
against the original frozen exact-Q generators.

The candidate must pass, in a fresh exact Singular process,

```text
matrix(P_Q)*C_Q - 1 = 0
```

coefficientwise.  A second independent sparse-rational replay must agree.
Deleting one nonzero multiplier term and changing one reconstructed
coefficient must each make the identity nonzero.

If supports differ, reconstruction is nonunique, rational reconstruction
fails its bound, or the exact replay is nonzero, report
`NO_STABLE_EXACT_CERTIFICATE_NO_VERDICT`.  It is permissible then to use the
union of modular supports as the columns of a finite exact rational Macaulay
linear system, but that solve requires a separately frozen descendant and
the same exact replay firewall.

## Allowed outcomes

```text
PASS_EXACT_Q_LOCALIZED_PRIOR_IDEAL_UNIT_WITH_REPLAYED_36_ENTRY_IDENTITY
NO_STABLE_EXACT_CERTIFICATE_NO_VERDICT
RESOURCE_CAP_NO_VERDICT
SOURCE_OR_REPLAY_FAILURE
```

An exact PASS independently proves the same narrow chart-empty conclusion as
the expected unit branch of V24R2: no point of the normalized valuation-one
finite prefix through grade six on `D(k10_0*W)`.  It does not cover `W=0`,
other unit/valuation strata, grade seven or later, a full jet or arc, K00
closure incidence, order two, maximum twelve, or JC2.  Every modular-only or
failed reconstruction outcome proves nothing over `Q`.
