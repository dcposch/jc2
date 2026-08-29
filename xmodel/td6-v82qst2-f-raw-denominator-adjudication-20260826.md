# TD6 V82QST2 raw-`F` denominator adjudication

Date: 2026-08-26

Status: bounded producer-side adjudication plus a passing direct specialized
certificate.  No top-level ledger is promoted by this report.

## Verdict

1. The two V82QST2 `rc=0` endpoints are valid exact **fraction-field staged
   CURRENT** results.  On the source-rebuilt specialization
   `C0=(V^2-U^3)/U`, hence `F=0`, they find ten base-inconsistent CURRENT rows
   over the degree-18 coefficient field above `Q(U,V)`.  In particular the
   already-parameterized row keyed `('X0',12)` is a nonzero constant field
   element.  At minimum this is an exact fraction-field inconsistency; under
   the wrapper's staged-chart contract it excludes the smaller principal open
   obtained by also inverting the emitted certificate denominator.  It does
   not emit a single polynomial original-source membership witness for that
   claim.  Campaign consumption of the staged-CURRENT conclusion remains
   conditional on the preregistered Gate-1 alternate-pivot comparison.
2. `F_RAW_registered_generic_open_killed=false` is mathematically correct for
   the certificate actually emitted.  The P12 residual has denominator one
   and cleared coordinate gcd one, but the staged substitution path used to
   produce that row was rational.  The reporter deliberately folds every
   FIRST, PREVIOUS/POLE, and CURRENT row and pivot lead into one denominator;
   thirteen irreducible factors of that denominator are outside the registered
   multiplicative set.  A unit residual cannot retroactively remove those
   localizations.
3. There is a denominator-free combination **inside the final CURRENT row
   list**: the P12 record is row 12 itself with coefficient one.  V82QST2 does
   not emit an unwind of that row to the genuine P12 and earlier source rows,
   so that endpoint alone neither proves nor disproves a denominator-free or
   divisor-safe original-source combination.  Independently, the
   hostile-reviewed V78B/C theorem already gives a genuine-P12/original-FIRST
   replay on generic fixed A3 with denominator radical `{U,H,B3}`.  Base change
   to `F=0` sends `H` to `(V^2-4U^3)/U` and `B3` to `V^4`; hence its
   restriction is divisor-safe on the registered `F=0` open.  A cleaner
   source certificate therefore exists abstractly, although V82QST2 did not
   emit it.  Its `false` Boolean is safe but conservative.
4. The cleanest exact successor is not a thirteen-branch divisor recursion.
   Compile genuine raw P12 directly on `F=0`, divide it only by the 38 exact
   FIRST pivots, lift the quotient DAG to the packed FIRST source rows, and
   clear the coefficients termwise.  Accept only an identity

   ```text
   s = h_P*P12 + sum_i h_i*FIRST_i
   ```

   with every cleared coordinate in `Q[U,V]` and radical
   `rad(s) subset {U,V,V^2-4U^3,V^2+8U^3}`.  This is V82QST3 below.

## Frozen evidence

The local V82QST2 case is
`cases/td6_c1_c2_c3_q_current_raw_f_v82qst2_aws_20260826`:

- preregistration SHA-256:
  `ad3bb74a73e22e79f72667dac318e5e248b6e6732615a08b34f6aa86160af87b`;
- source manifest SHA-256:
  `85200a68849c1345375f3ec4a44c463c2ea67f8cbf885727658a7aef1b58cf1c`;
- source archive SHA-256:
  `731eed3fdbaaf17b9f14468ca885f16bf4008f1b43bb8b276a99a530966a6d5c`;
- V82QST2 wrapper SHA-256:
  `5a1054269237d9a2da5c7f5e51ae001ad59f61607ac36f2e7a9b059c972c74d5`;
- frozen compiler SHA-256:
  `a4ccd5d81101fdb82ed2f61571c258e2054961d161f4a98461b8f8614d3fd85e`;
- nested hostile review, promotion, and Gate-2 design pins:
  `a3e1315041dafdeefaf26a3a9f2f79e945c2ab70fad18436ddb416f161f9de5b`,
  `6037e902a0e9c9fe3c9115d77753559060913f8d64412455de75430ab526d56b`,
  and `6c21b402a3b25c9437f655fadfb4f4966d6295ba8106e48fc3417b0879913484`.

The audited AWS endpoint is Box02
`/home/ubuntu/runs/td6_v82qst2_f_raw_box02_20260826T105625Z`.  q2 and q10
started at `2026-08-26T10:56:44Z`, finished at `10:57:53Z`, and returned
`rc=0` with no swap.  Endpoint hashes are:

| lane | stdout SHA-256 | stderr SHA-256 |
|---|---|---|
| q2 | `ae696eb1547ecce13940aa94dd940742aa813aea684394daf92dc3ebda035d2b` | `07725f3a8fa7e853d2ae0429f104811081d178263818f6b7d88034c8730b370e` |
| q10 | `66cb37fe8dd60221ae0f740cfc4229779877f04272e1f60b8049ae413112bb47` | `ae61ec95d4a23d3cfa7acfcf9744a9ecc39990918688c6c445e2358258fdf8e5` |

Both lanes verify, before reconstruction,

```text
F=0,
G=V^4,
L=V^8*(V^2+8U^3),
H=(V^2-4U^3)/U,
B3=V^4,
```

and register
`D(U*V*(V^2-4U^3)*(V^2+8U^3))`.  They agree on transport rank
`3470/3602` with two events, FIRST rank `38/132` with no dependent row,
PREVIOUS/POLE rank `38/94` with one dependent row but no obstruction
coordinate, and CURRENT rank `25/56` with eleven dependent rows and ten base
incompatibilities (row indices `0,2,5,6,7,8,9,10,11,12`).

The strongest and cleanest final-row record is P12:

```text
key=('X0',12)
residual_sha256=834755fff2d27f19cb46714f2ceb3faf1503624098746681db65610d673a1033
residual_exact=(126/25,-171/25,72/25,-18/25,0,...,0)
residual_denominator=1
cleared_numerator_gcd=1
source_combination=((12,('X0',12),1),)
source_certificate_sha256=adfcd27b740cafb978260bf9d5af8330bcdd71dd3f82476f8a73917d1bfcab23
```

Because the coefficient algebra is a field, this nonzero constant element is
a unit there.  That establishes a contradiction after the staged
localizations.  It says nothing by itself about points on divisors where an
earlier pivot used to build the parameterization vanishes.

## Why the registered-open Boolean is false

The implementation makes the criterion explicit.  Lines 206--213 of the
frozen wrapper collect coefficient values from **all** FIRST rows and pivot
leads, all PREVIOUS/POLE rows and pivot leads, and all CURRENT rows and pivot
leads.  Lines 226--231 take a common denominator with the selected row
combination and residual, then require both the residual numerator gcd and
that full denominator to have no factors outside the registered set.

For every incompatibility the global denominator has the factorization

```text
(1/74844) * U^10 * V^11 * (V^2-4U^3)^2
* (V^2-3U^3) * (V^2-2U^3) * (3V^2-8U^3)
* (V^4-12V^2U^3+16U^6)
* (V^4-6V^2U^3+16U^6)
* (2V^4-11V^2U^3+16U^6)
* (11V^6-84V^4U^3+256V^2U^6-256U^9)
* (V^8-19V^6U^3+126V^4U^6-320V^2U^9+256U^12)
* (6V^8-37V^6U^3+188V^4U^6-384V^2U^9+256U^12)
* (V^10-8V^8U^3+20V^6U^6-8V^4U^9+96V^2U^12-256U^15)
* (7V^10-142V^8U^3+1136V^6U^6-4000V^4U^9
   +6400V^2U^12-4096U^15)
* (9V^10-204V^8U^3+1744V^6U^6-6720V^4U^9
   +12288V^2U^12-8192U^15)
* (3V^14-104V^12U^3+1457V^10U^6-10216V^8U^9
   +40576V^6U^12-96768V^4U^15+126976V^2U^18-65536U^21).
```

The first three displayed powers are registered; the other thirteen
irreducibles are not.  Hence the reporter must return false even for P12,
whose residual contributes no base denominator or outside numerator factor.
The denominator is dependency-insensitive: most factors may come from rows
and pivots that the P12 derivation does not need.  Consequently it is an
upper bound on the localization required by this certificate, not a minimal
denominator and not a divisor-by-divisor obstruction theorem.

There is also no valid shortcut from multivariate gcd one to a polynomial
Bezout certificate in general.  Here P12 is stronger--its residual is already
a constant field unit--but the unresolved denominators live in the derivation
of the staged row, not in that residual.  Clearing only the residual therefore
does not repair the missing source-row unwind.

## Divisor-safe successor and present endpoints

There is already an independent existence argument.  The reconciled V78B/C
result, SHA-256
`76a0b548e40c9f234c780f11054aac1e68dcab4f4de9b4e558e61c844200c627`,
and its hostile review, SHA-256
`a3599e65f88015f60a3131572716affda748d8dc5963e3648bb35842246a1861`,
verify genuine P12, its lift to original packed FIRST rows, the unit base
remainder `-k/50`, and denominator radicals contained in `{U,H,B3}` on
`D(U*H*B3)`.  On `F=0`,

```text
U -> U,
H=C-3U^2 -> (V^2-4U^3)/U,
B3 -> V^4.
```

No denominator becomes identically zero, and all are units on the registered
`F=0` open.  Exact localization and base change therefore restrict that
identity to the desired special fibre.  This establishes divisor-safe
existence; it does not provide V82QST2 with a missing staged-CURRENT ancestry
record, and it is still limited to the fixed-A3 genuine-FIRST/P12 system.

The frozen successor directory is
`cases/td6_c1_c2_c3_f_raw_p12_source_v82qst3_aws_20260826`.  Its wrapper
imports V82QST2 by hash, captures the exact 38 FIRST pivots, compiles genuine
raw P12 before PREVIOUS/POLE and CURRENT parameterization, lifts the division
relations to the packed FIRST rows, verifies the source identity and an
omitted-row negative control, and audits the common clearer and every
termwise product coordinate.

The first launch is excluded because its callback was overwritten and it
only reran V82QST2.  A second launch reached the post-identity,
post-allowed-factor coordinate audit in both lanes, then exited 1 on a
reporter-only FLINT context-construction TypeError; it emitted no PASS and is
quarantined.  The corrected wrapper SHA-256 is
`6977d0acb3d178447effe225f80f7f415a23042090092a648a8bbfbfc462a497`.

Identical q2/q10 clients were launched independently at:

- Box02:
  `/home/ubuntu/runs/td6_v82qst3_f_p12_v3_box02_20260826T1131Z`;
- r6a:
  `/home/ubuntu/runs/td6_v82qst3_f_p12_v3_r6a_20260826T1133Z`.

Each lane is capped at 4 GiB and 1,800 seconds.  All four endpoints returned
`rc=0` with the distinct banner
`TD6-V82QST3-F-RAW-GENUINE-P12-SOURCE PASS`.  Box02 and r6a, q2 and q10,
emit byte-identical 2,298,293-byte certificates with SHA-256
`8e892ffa914e0f93969abb9722f926486843f59cf77f5861c5ce3d3438281482`.
Their selected base-result lines are also identical with SHA-256
`1e21693abf0f0354aa438c056b391ec2cf6aa0ecab6935b5186597c13b73dd91`.

The direct result is

```text
genuine P12 terms = 2893
genuine P12 SHA-256 = da0d595ecbdc1922b127bba6b54d935a4631618eed617fb99c9fa95cbdec534f
nonzero FIRST multipliers = 28 rows / 1489 terms
residual = (-126/25,171/25,-72/25,18/25,0,...,0)
residual SHA-256 = b9445255e063a82f827a01b7e18c3bdd2f3da41de14903a73fc2ae68121df7a0
clearer = V^4*U^9*(V^2-4U^3)^3
outside factors = ()
cleared coordinates audited = 612828
```

Thus the replay verifies in the polynomial coordinate ring the explicit
identity

```text
V^4*U^9*(V^2-4U^3)^3
  = h_P*P12 + sum_(28 active FIRST rows) h_i*FIRST_i.
```

The certificate is stronger than the preregistered target: it kills
the fixed-A3 `F=0` open `D(U*V*(V^2-4U^3))`, without needing
`V^2+8U^3` to be a unit.  It is independent of Gate 1 because it never uses
PREVIOUS/POLE or staged CURRENT.  The completed r6a replay supplies an
independent custody/host check.

## Scope firewall and later total-`F` computation

Even a passing V82QST3 proves only emptiness of the fixed source-typed A3
`F=0` registered open at the genuine-FIRST/P12 gate.  It does not adjudicate
the staged CURRENT tangent table and does not itself require Gate 1 for that
narrow base conclusion.  It freezes q/dead-stretch/correction data and does
not emit a total-family identity, so it proves no positive-`F` valuation arc,
whole fixed A3 case, TD6, SP-2, or JC2.

The cross-interface report
`xmodel/cross-empty-special-fibre-valuative-propagation-20260826.md`, SHA-256
`22d32f1840f47da09660fd8f6b37966562b6532e8bad12544953a7cbb6185c85`,
requires a stronger object

```text
s = sum_i h_i*f_i + F*h
```

in one total chart with `F` not inverted and all transverse variables
retained.  The clean follow-on design is frozen as `TOTAL_F_LIFT_DESIGN.md`:
introduce an independent `t` through
`C0=(V^2-U^3+t)/U`, retain a complete source DAG, lift the special
certificate, and verify exact divisibility of its total-family residual by
`t`.  That is the earliest successor licensed to feed the valuative
propagation interface.

If this total chart uses a blowup or ordered divisor routing, the stronger
base-change warning in
`xmodel/cross-iterated-blowup-cech-valuative-propagation-20260826.md`,
SHA-256
`6995a991b1e7803a26bbf5374b10d54a0cda7d17158ad9f1595db76218aadb92`,
also applies: form the actual total Rees algebra before `t=0`, use its Rees
kernel (or a proved saturation) rather than a naive symmetric-algebra chart,
and audit `t`-torsion.  A specialized-first blowup may not be the base change
needed by the arc-lifting theorem.
