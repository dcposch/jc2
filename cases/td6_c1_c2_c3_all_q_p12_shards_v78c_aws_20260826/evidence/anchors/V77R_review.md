# Hostile review: TD6 V77R corrected pure-q3 scalar audit

Inspection only of the charged producer case and producer report.  No
producer execution, no `verify.py` / `normalize_compare.py` run, no
`replay.py` run, no CAS, no solver, and no Lean.  Stored `PASS` strings
were ignored as proof.  Frozen file bytes were hashed with `openssl
dgst -sha256` and compared by exact equality.  Both portable archives
were listed and read by `tar -xOf`; they were not unpacked into the
tree.  Printed denominator expansions were reconstructed by rational
monomial arithmetic in `Q[C,V,U]`.  Flint was not invoked.

Charged surfaces:

- `cases/td6_c1_c2_c3_q3_gamma_dual_repaired_v77r_aws_20260826/`
- `xmodel/td6-c1-c2-c3-q3-gamma-dual-repaired-v77r-aws-20260826.md`

Six load-bearing charges are re-audited from frozen source, dual-AWS
stdout/stderr, V79a control logs, and the hash-pinned parent V32 /
jet-orbit / `compile_x_current` modules inside the corrected archive.

---

## Findings

**1. [Confirmed] Source typing is `q=t+gamma*t^3+t^25` at `beta=0`,
with singleton original transport source `('g','X',0,3)`, direct
`3*gamma*t^2`, and no hidden q2 contribution.**

The corrected replay
`jc2/cases/td6_c1_c2_c3_q3_gamma_dual_repaired_20260825/replay.py`
hashes to

```text
7a961c02002dabb5f8ae363e88a4a041b855ec03fc8ea370bea576ae12e47d80
```

and is the unique mathematical member that differs between the V79a
control archive and the V79b theorem archive (Finding 5).  It pins
parent V32

```text
dcc7003def824c0d2a88998cbf22a66f022a32714f05754c505e8d825bd91742
```

and rebuilds the frozen source-typed section

```text
y=s^{-1},
x=C s + V s^2 + U s^3 + t s^4,
p=t^{15},
q=t + gamma t^3 + t^{25}
```

with zero dead stretch and frozen `F1`/pole data.  The g-transport is
constructed from coefficient dict `{1: 1, 25: 1}` only: there is no
base `t^2` and no base `t^3`.  Gamma enters the affine transport RHS
through exactly one original key.  `source_vector_gamma` returns
`ONE_VECTOR = r.t.source_vector(('g','X',0,1))` if and only if
`key == ('g','X',0,3)`, otherwise the 18-zero vector.  The ordered
transport contains that q3 key once.  The q2 key `('g','X',0,2)` is
also present once, as a homogeneous jet slot, and is not a gamma
source.

The omission control `include_q3=False` makes every `pivot_rhs`
derivative vanish, while the theorem path retains
`transport_gamma_rhs_pivot_count=1`.  So the only transport gamma
source is that singleton.

Direct `q'` is installed after replacing the compiler table:

```text
qd.Q_PRIME = {0: EDual(1), 24: EDual(25)}
qd.Q_PRIME[2] = EDual(0, 3)    # coefficient of t^2 in 1 + 3 gamma t^2 + 25 t^{24}
```

That is exactly `d/dt(gamma t^3) = 3 gamma t^2`.  Omitting the
`Q_PRIME[2]` entry changes the packed first rows
(`first_rows_no_direct_qprime != first_rows`) and drops the first-gamma
coefficient count from 221 to 2.  The two surviving coefficients are
the expected transport-section residue, not a q2 leak.

Hidden q2 is excluded by two independent controls, both in source and
in the theorem stdout.

- Stale-`qd.B` inertness.  After `Q_PRIME` has been replaced, setting
  `qd.B = EDual(0,1)` and repacking `first_band_polynomials` yields
  `first_rows_stale_B == first_rows`.  On the theorem path
  `qd.B = EDual(0)` with both value and derivative zero.
- Genuine `Q_PRIME[1]` leakage.  Injecting `qd.Q_PRIME[1] = EDual(0,2)`
  — the V32 q2 slot `2 beta t` at `beta = gamma` — yields
  `first_rows_q2_qprime_leak != first_rows`.

Those tests are not informal.  Hash-pinned `jet_orbit_adjoint`
`first_band_polynomials` multiplies the first band by `Q_PRIME.get`,
not by `B`.  Hash-pinned `td6_boundary_q2_deformation`
`compile_x_current` likewise reads `Q_PRIME.get`; jet-orbit
`compile_current` copies the *replaced* `Q_PRIME` onto that base
global for the duration of the call.  The only live `B` reads in
jet-orbit are `source_rhs` (not called on the V77R path) and the
import-time formula `Q_PRIME[1] = 2*B` (overwritten before any first
or current compilation).  Therefore a stale nonzero `qd.B` after
`Q_PRIME` replacement cannot contribute a q2 tangent, while a real
q2 tangent through `Q_PRIME[1]` is detected.  The V79a control that
expected the stale-`B` assignment to change rows is a software-control
failure, not a q2 contamination (Finding 5).

Both theorem stdouts print

```text
q_gamma=t+gamma*t^3+t^25
q_gamma_prime=1+3*gamma*t^2+25*t^24
base_q2_beta=0
legacy_qd_B_state_is_semantically_inert=true
q2_Q_PRIME_leakage_negative_control=true
pure_q3_B_value_zero=true
pure_q3_B_derivative_zero=true
transport_q3_source_omission_negative_control=true
direct_qprime_omission_negative_control=true
```

The prior V77 source-typing scare is resolved in this clean source.
Old V77 already replaced `Q_PRIME` the same way and only wrote stale
`qd.B = EDual(0,1)`; V77R makes that inertness an asserted control and
sets `B` to exact zero on the theorem path.

**2. [Confirmed] Digest `c0730fa1…` is the exact zero selected-minor
derivative.  No rank-growth inference survives.**

After dual GE that pivots only on coefficients with nonzero *base*
value, the selected first minor is the product of the 38 pivot leads.
The source then asserts, before printing,

```text
zero_digest = e3_digest(E3())
assert zero_digest == "c0730fa1f8764164b2ac0a74523849b49f4362d41bc81845d086d6373fdb65c1"
assert not first_minor.derivative
```

and prints

```text
first_rank=38/132
first_dependent_count=0
first_minor_base_sha256=978690d3cc3a645c435b69f5b6558351c4eb57cb3663e315f52d4053efdbed52
first_minor_gamma_sha256=c0730fa1f8764164b2ac0a74523849b49f4362d41bc81845d086d6373fdb65c1
first_minor_gamma_is_exact_zero=true
zero_scalar_digest_semantics_asserted=true
```

Both AWS hosts emitted those lines and returned rc 0, so the assertions
held in the frozen execution.  The same digest is the reviewed V32
selected-minor *beta* derivative of the same base minor
`978690d3…`; V77R additionally identifies it with `e3_digest(E3())`.
That is the canonical 18-coordinate zero serialization, not a nonzero
Fitting generator.

Rank growth cannot be read from this digest.

- Dual GE never selects an `eps`-only pivot, so dual rank cannot exceed
  base rank by construction.
- `first_dependent_count=0`: every packed first row became a base
  pivot.  There is no leftover row in which a derivative-only variable
  could appear.
- The matrix is 38 rows of rank 38, already full row rank.  A first-order
  rank *increase* is impossible.
- The printed `c0730f…` value is the zero derivative of the selected
  38-minor, so that minor does not vanish at order `eps` either.

The original V77 report's sentence “the selected first pivot product
varies nontrivially with gamma” / “nonzero gamma derivative, SHA
`c0730fa1…`” is a direct misreading of its own serializer, independent
of the stale-`B` scare.  V77R removes that sentence and asserts the
zero semantics in source.  The surviving q3 variation is the four-term
genuine-P12 derivative and the three-term affine remainder derivative
(Finding 3), not first-minor rank growth.

**3. [Confirmed] Genuine P12 has original-row ancestry; source-row
omission, the exact reduced remainder, lambda-prime contribution and
omission, and termwise clearing all hold in source.**

`compile_current(...)[12]` is the genuine current P12 compiler, not a
staged N13 surrogate.  After restriction of original transport sections
to the dual free chart, the base projection is the already-reviewed
2,893-term polynomial

```text
8d5c3550fbad393c1e13061d9934ed79e29261db378f1d344c4ea5e587e704da
```

matching V32 / V43 / V57 / old V77.  The q3 derivative has four terms
and SHA

```text
70d253cd30303d5ae6ebf81e8de0b2c12a00b66b060c996f0a898dbaf708682c
```

matching old V77's *mathematical* P12-gamma object, as the producer
states.  `solve_cert_dual` replays every pivot and dependent from the
packed original first rows (`first_dual_original_row_replay=true`).
`exact_source_replay` rebuilds `P12 - remainder` as `sum lambda_i *
source_polynomial(first_row_i)` over those original rows, then drops
one nonzero multiplier row and asserts the identity fails
(`P12_source_row_omission_negative_control=true`).

Exact reduction against the 38 first pivots gives remainder base
`{(): -k/50}` with

```text
k = 252 - 342 S + 144 S^2 - 36 S^3
```

and SHA

```text
93121eef14c472c3c55b7acaeb1d0eff73b77d462ad8d5b197e8e21b9cda89c4
```

again matching V32 / old V77.  The q3 remainder derivative has three
terms, degree 1 (affine), SHA

```text
3dd07bb5e097ea920104e085d857e519915ba214145d862576bd9cb9d3792458
```

matching old V77.  `polynomial_inverse_of_dual_unit` produces a
three-term inverse whose product with the remainder is `EDual(1)`.
The square-zero remainder is a unit because the base remainder is
already a unit.  That is persistence of the reviewed generic-open
emptiness, not a new gamma-neighborhood theorem.

Differentiated source identity:

```text
raw_gamma - remainder_gamma
  = lambda0 * b' + lambda' * b0
```

Both Leibniz summands have 3,386 terms and *different* digests
(`3cddb132…` vs `6ccbc99e…`), so they are not the same polynomial.
`lambdaprime_b0` is nonzero.  Omitting it (`lambda0_bprime` alone)
fails the identity.  Counts: 28 original first rows support `lambda0`,
14 of those also support `lambda'`.  There is no purely `lambda'`-row.
`source_base_multiplier_terms=1489` is the frozen gamma-zero
projection sentinel; union support 1,531 is allowed to grow by
gamma-only monomials and is not asserted equal to 1,489.

Termwise clearing is the LCM of the 77,512 individual Leibniz products
`lambda0 * b'` and `lambda' * b0` formed from stored (nonzero)
multiplier coefficients against stored source-row coefficients, *before
summation*.  That is stronger than clearing after cancellation
(Finding 4).

**4. [Confirmed] Complete denominator support is exactly the radical
`{U, H, B3}` on the stated generic open.  The 77,512-slot check is
termwise Leibniz LCM, not a monomial count after summing.**

Write `H = C - 3U^2` and

```text
B3 = 4 C^2 U^2 - 4 C V^2 U + 24 C U^4 + V^4 - 20 V^2 U^3 + 20 U^6
```

as in V57/V76.  Every printed denominator expansion in both theorem
stdouts reconstructs, by hand, as a unit in `Q` times a product of
powers of `U`, `H`, and this `B3`:

| printed object | reconstructed form |
|---|---|
| `raw_base` / `first_base` `C U - 3 U^3` | `U H` |
| `raw_gamma` `1` | unit |
| `first_gamma` `C-3U^2` | `H` |
| `relation_base` (the 12-homogeneous expansion) | `(1/4) B3 U^2 H^2` |
| `relation_gamma` (the 11-homogeneous expansion) | `(1/4) B3 U H^2` |
| `termwise_dual` (the 13-homogeneous expansion) | `(1/4) B3 U H^3` |

The `relation_base` identity was checked monomial by monomial against
`(1/4) B3 · U^2 · H^2`; every coefficient matches, including
`-22 C^2 U^8`, `-3/2 C V^4 U^4`, `21 C V^2 U^7`, `9/4 V^4 U^6`, and
`45 U^{12}`.  `relation_gamma` is exactly that polynomial divided by
`U`.  `termwise_dual` is exactly `H · relation_gamma`.  The printed
`.factor()` tuples name the same generators.  Extra *powers* of `H`
and `U` grow under products (`H^3` in the termwise LCM); extra
*primes* do not.  Units `1/4` lie in `Q`.  The supported open is
therefore exactly `D(U H B3) = D(U*(C-3U^2)*B3)`, which is the stated
scope, and not a strictly larger principal open.

Meaning of `termwise_dual_slot_count=77512`.  For each of the 28
supporting original first rows the source walks the Cartesian product
of stored multiplier coefficients against stored source-row
coefficients and records *two* products per pair:

```text
multiplier.value * source.derivative      # lambda0 * b'
multiplier.derivative * source.value      # lambda' * b0
```

and increments the slot counter by 2, including pairs whose Leibniz
product happens to vanish (pure-base multipliers give `lambda'=0`).
Then `denominator_lcm` is taken over that list.  So 77,512 is

```text
2 * sum_{i=1}^{28} (#lambda coeffs of row i) * (#source coeffs of row i)
```

not the number of monomials in the summed identity, and not a
transport- or first-rank figure.  Dual-host stdout agrees on 77,512.
Independent recomputation of the integer from the unprinted
coefficient tables is a computational gap, not a source defect: the
*meaning* of the check is in the source, and the printed LCM is the
polynomial already reconstructed as `(1/4) U B3 H^3`.

**5. [Confirmed] Dual-host custody, source-archive closure, the
normalized-byte comparator, and V79a as a pre-math software-control
failure.**

Recomputed SHA-256 against the freeze:

| object | SHA-256 |
|---|---|
| corrected source archive | `5973b82953c919df1a28b1b86eed40feafbe4a3ea69bde14e7df68374e83942d` |
| V79a control archive | `cc7717b46d667726d0b4b51b51027b19dfbbb3823104018fca4a912af6eb6579` |
| corrected `SOURCE.sha256` bytes | `b1f1d48466b12748112dc054ee435051f1afdb67b816eaf1bc7c7ffe27742c2b` |
| corrected V77R replay | `7a961c02002dabb5f8ae363e88a4a041b855ec03fc8ea370bea576ae12e47d80` |
| Box02 stdout / stderr | `9f3be97b1f2ad2c04f896e031e9a5318b4e6dc2fe4ccdbb55c56dcf697dc49e3` / `0c9d05fa7891e877709a4bc0f4feac975ea54e082a77fa96844b6b661c377e97` |
| r6d stdout / stderr | `1d05d1be98e988a47032ae653dd71002cc42589e0c83a2189ff7ff76d5616ab9` / `b62380449015ffaed44ab0f998556f97f13fb55d12044e447d5eb68c05312198` |
| normalized stdout | `f6aaf1c9f4e9f1e6961525a5cf79fd53ac4e3ee226520e34d652a7642fdabf1e` |
| producer report | `546aca7bea8ea15eb279ae0450d06adc079b79505b94c49f81569e4230f5321f` |
| `MANIFEST.sha256` | `d27d5d1665e825690b220caba977c23a3870d6ee8ecb55fc4538632a4885047c` |

`FREEZE.sha256` hashes `MANIFEST.sha256`, the producer report, and the
review prompt.  `MANIFEST.sha256` hashes every regular file in the case
except itself and `FREEZE.sha256`.  Inside the corrected archive,
`SOURCE.sha256` hashes every member except itself; `sha256sum -c`
is the first action of `run_v77r.sh`, and both theorem `source_check`
logs are the same path-OK listing.  The wrapper refuses Darwin,
non-`ip-*` hostnames, and non-EC2 DMI, then prints exactly three
`aws_*` banner lines.  Deleting every line that starts with `aws_`
makes the two theorem stdouts byte-identical; `awk '!/^aws_/'` plus
`openssl dgst -sha256` recovers `f6aaf1c9…` on both.  The three-byte
raw-stdout gap is exactly `box02`/`186` versus `r6d`/`45` in those
banners.

Hosts are independent: Box02 `ip-172-30-0-186`, tag
`td6_v79b_v77r_box02_20260826T0002Z`, 19:13.74, RSS 567,644 KiB,
rc 0; r6d `ip-172-30-0-45`, tag `td6_v79b_v77r_r6d_20260826T0002Z`,
19:21.34, RSS 567,736 KiB, rc 0.  Each control and theorem launch
records a 12 GiB address-space cap and a 14,400 s timeout on the V79a
side; the V79b `launch.meta` is thinner but the same hosts, same
wrapper, and same four-hour `timeout` appear in stderr.

V79a versus V79b archives differ in exactly three members: the
repaired replay, `V79_PREREGISTRATION.md`, and `SOURCE.sha256`.  V79a
replay still names the q2-leak flag `leak_q2` and implements it as
`qd.B = EDual(0,1)` with *no* `Q_PRIME[1]` injection, then asserts
`first_rows_q2_leak != first_rows`.  Both V79a hosts hit that
assertion at replay.py:607 after ~37 s, printed transport rank
`3470/3602` and the q3-source omission flag, never printed
`first_rank`, never printed `TD6-V77R-PURE-Q3-SCALAR-AUDIT PASS`, and
returned rc 1.  That is a failed software negative control: it
demanded that dead state `qd.B` change the rows, and the rows did not
change, which is exactly the inertness V79b later asserts.  It is not
a mathematical counterexample to the q3 audit.  Classification as a
pre-math software-control failure is correct for the theorem
endpoints (first minor, P12, remainder, lambda identity, denominators).
Transport *did* run on V79a, so “before any q3 arithmetic” would be
too strong; “before the q3 theorem gates” is accurate.

**6. [Confirmed] Scope is first-order / source-support at the
already-empty generic open of the fixed A3 section.  Gamma-neighborhood,
family, full-TD6, SP-2, and JC2 implications are rejected.**

The coefficient ring is `E(C,V,U)[eps]/eps^2` at `gamma = eps`,
localized on `D(U*(C-3U^2)*B3)`.  Dual emptiness on that open is
automatic because the base remainder is already a unit; the source
prints this as
`dual_emptiness_is_automatic_over_unit_base_ideal=true` and
`result_use=source_support_degree_denominator_discriminator_only`.
The producer report and the replay docstring say the same thing in
prose.  Firewall flags in both theorem stdouts:

```text
finite_gamma_neighborhood_killed=false
full_gamma_family_killed=false
full_four_parameter_family_killed=false
whole_TD6_killed=false
SP2_killed=false
JC2_resolved=false
```

The nonzero three-term affine remainder derivative is Fitting / source
input for a later simultaneous nonlinear gate.  It does not kill a
finite gamma disk.  Zero selected-minor derivative forbids claiming
first-minor rank growth (Finding 2).  The four-term P12 derivative and
the 14 lambda-prime rows are q3 source support on the generic open,
not a family theorem.

`fixed_A3_q2_beta_slice=dependency_V76_provisional_complete_union` is a
parent-context banner.  V77R does not consume the V70/V71/V75 covers of
`U=0`, `H=0`, or `B3=0`; its localization is already `D(U H B3)`,
whose emptiness is the reviewed V57 original-source identity.  The
word “provisional” is stale relative to the filed V76 V2 `CONFIRMED`
(Finding-level nit only; see recommendations).  It does not enlarge
V77R to a whole-section or neighborhood claim.

---

## Load-bearing defects

None.

The six charged claims hold in the frozen source and in the dual-AWS
certificates.  No surviving inference of first-minor rank growth, no
hidden q2 tangent on the theorem path, and no family / neighborhood /
TD6 / SP-2 / JC2 implication is licensed.

---

## Custody / prose recommendations

These do not disturb the verdict.

1. V79b `launch.meta` omits the 12 GiB cap and timeout that V79a
   `launch.meta` records.  Stderr still shows `timeout 14400
   ./run_v77r.sh` on both theorem hosts.  Copy the V79a keys onto
   future theorem `launch.meta` files.
2. The stdout banner `dependency_V76_provisional_complete_union` is
   leftover.  V76 V2 is already `CONFIRMED`.  V77R does not need V76's
   complementary covers.  Rename the banner to a V57 generic-open pin,
   or drop “provisional”.
3. “V79a stopped before q3 mathematics” is right for the theorem
   gates and wrong if read as “transport never ran”.  Prefer “failed
   at the stale-`B` software control after transport, before
   first-rank / P12 / remainder”.
4. The four-term P12-gamma polynomial and the three-term remainder
   derivative are hash-pinned but not expanded in stdout.  A successor
   that wants those monomials as Fitting input should print them, or
   pin a coefficient ledger.  The audit claims do not require the
   expansions.
5. `verify.py` is a custody comparator, not a theorem.  It was not
   executed here; its hard-coded marker list is a proper subset of the
   dual stdout and matches the source prints that were checked by
   hand.

---

## Computational gaps (not defects)

Independent local replay of the 19-minute dual-number GE, the 2,893-term
P12, the 77,512 Leibniz products, and `e3_digest` was in-scope as a
gap and out of scope as a local computation.  Dual-host rc 0 on the
hash-closed source, plus the hand identities above, close the charged
claims without that replay.  Recomputing the integer 77,512 from the
unprinted per-row coefficient cardinalities, or expanding the four
P12-gamma monomials, would require rerunning the producer.

---

## Strongest exact theorem that survives

On the fixed source-typed A3 chart, at `beta = 0`, over the square-zero
extension in `gamma` localized on `D(U*(C-3U^2)*B3)`, the line
`q = t + gamma t^3 + t^{25}` is source-typed by the singleton original
transport key `('g','X',0,3)` together with the direct term
`3 gamma t^2` in `q'`, and by no q2 slot.  Stale `qd.B` is inert after
`Q_PRIME` replacement; a genuine `Q_PRIME[1]` leak is detected.
Transport rank is `3470/3602` and first rank is `38/132`.  The
selected first-minor gamma derivative is the zero element of `E`
(serializer `c0730fa1…`), so this digest is not first-minor rank
growth.  Genuine P12 is the reviewed 2,893-term base polynomial plus a
four-term q3 derivative, reduced against original first rows to base
remainder `-k/50` plus a three-term affine q3 derivative, with 28
original-row multipliers, 14 of them lambda-prime, both Leibniz
summands necessary, and termwise denominator radical contained in
`{U, H, B3}` (77,512 Leibniz slots, LCM `(1/4) U B3 H^3`).  Dual
emptiness on this open is automatic from the unit base remainder.
Nothing is claimed about a finite gamma neighborhood, the gamma
family, any higher-q family, the rest of TD6, SP-2, or JC2.

---

CONFIRMED
