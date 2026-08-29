# Round 1808 Opus global-claim hostile audit

Auditor: Sol 5.6 internal adversarial lane  
Date: 2026-08-29 UTC  
Frozen campaign basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa`  
Lifecycle: `POST_BLIND_INTERNAL_AUDIT / MATERIAL_REPAIR / CROSS-MODEL REVIEW_PENDING`

## Verdict

Opus's `OP-1`--`OP-6` package contains correct local formulas, but the claimed
new selector synthesis requires material repair.  The central error identifies
a Sigray pole vertex with a proper root of the common leading form.  That makes
the advertised residue-A `RPMC(1)` equality false and invalidates the proposed
status raises.  Several other statements are already promoted history, and the
monodromy bypass omits an additional local-to-global block seam.

No numbered avenue should move on this package.  Retain only the corrected
formulas below and use the existing capacity and marked-inertia lanes.

## 1. `OP-1`: correct, already known

For a proper root `P`, the Bezout sign and localization are correct:

```text
n_P = alpha beta B mu_P
      - sum_(gamma over P) poleord_gamma(g),
Delta_P = sum_(gamma over P) poleord_gamma(g).
```

This is already proved in `xmodel/sol-rpmc.md` and recorded canonically as the
exact polar bridge.  Its pole-order form is `KNOWN-EQUIVALENT`, not a new
theorem.

## 2. `OP-2`: reject the pole-vertex/root identification

For each Sigray pole vertex `F`, the entry identity is

```text
Lambda(F) = alpha beta a_F b_F / nu_F.
```

A proper root `P` can carry several such vertices.  If `S_P` is the attachment
set, the correct root formula is

```text
Delta_P = sum_(F in S_P) Lambda(F),

RPMC(C) iff
  sum_(F in S_P) a_F b_F / nu_F <= C mu_P/B
  for every proper root P.
```

The attachment partition `S_P` is load-bearing and is absent from most filed
reduced records.

The residue-A control exposes the error.  Both pole entries of mass `3` attach
to the same `Y` root:

```text
(B,alpha,beta,mu_Y,Delta_Y) = (84,2,3,63,6),
(mu_X,Delta_X)              = (21,0).
```

Therefore

```text
B Delta_Y / (alpha beta mu_Y) = 4/3,
```

not `1`.  The global quantity `E_MR=1`, so `KJN(1)` is at equality while
rootwise `RPMC(1)` fails on this filed book-relative template.  This exact
`4/3` computation was already recorded in `AUDIT.md`; the blind novelty search
missed it.

## 3. `OP-3`: retain only the global disjunction

An actual `U1*(R)` with odd `R>=3` would have

```text
E_MR = 2R/3 > 1
```

and would therefore violate `KJN(1)`.  It cannot be called a rootwise
`RPMC(1)` countermodel because the formal reduced record lacks
`B`, the root multiplicities `mu_P`, the attachment sets `S_P`, and
polynomial-origin data.

The claim that the ceiling lives *exactly* in dropped scale data is false.
The summed conjecture

```text
sum_F a_F b_F/nu_F <= C
```

is already expressed in the reduced record.  Root weights are one possible
proof instrument, not the uniquely missing datum.  Any root-enriched interface
would need the full tuple `(B,{mu_P},{S_P})`, not just `mu_P/B`.

## 4. `OP-4`: formula correct, novelty and scope repaired

For a connected generic fibre of genus `G`, with `s` pole ends and `n` finite
ends,

```text
sum_(finite p) (e_p-1) = 2G-2+td+s,
sum_c delta(lambda,c)  = sum_(finite p) e_p
                       = td+s+n+2G-2
                       = td-chi(C_lambda).
```

This is Chau's already-promoted finite-end identity.  The conclusion
`sum_c delta >= td` uses the nonproper Keller scope and `n>=1`; it is false
for an automorphism.  The fact `n>=1` uses the known positive projection
degree of every asymptotic component, not Riemann--Hurwitz alone.

## 5. `OP-5`: repair local cycles; do not reopen passports

At a marked value, the local cycle decomposition contributed by finite ends
is correct, but the numerical conclusions must distinguish ends of contact
order one:

```text
support(sigma_c) = sum_(e_p>1) e_p,
index(sigma_c)   = sum_p (e_p-1),
delta(c)         = sum_p e_p.
```

Thus `support=delta` fails whenever an `e_p=1` finite end is present, and the
number of nontrivial cycles counts only ends with `e_p>1`.  The marked theorem
and its independent review are already promoted; ordinary passports forget
the `e=1` marked fixed points, and filed books do not fully group finite ends
by target value/component.  Its current residue-A consequence remains the
non-killing parity filter `169 -> 48`, with all 48 rows surviving.

The proposed dichotomy is also invalid: failure to display a transposition or
short prime cycle does not imply imprimitivity.  Primitive groups and
primitive generating tuples can avoid those meridian types.

Finally, imprimitivity of the one-dimensional vertical subgroup `G_lambda`
does not itself produce an intermediate field of
`C(x,y)/C(f,g)`.  Two distinct open seams precede a smaller Keller map:

1. extend a vertical block system to the full two-dimensional monodromy;
2. turn the resulting global intermediate field into an `A^2` polynomial
   Keller counterexample of strictly smaller `td`.

## 6. `OP-6`: correct selection, already on file

Well-ordering allows a globally minimal-topological-degree counterexample,
and arbitrary-pair Sigray normalization preserves `td`.  This pure-Sigray
branch is already explicit in `REDUCTION.md` and prior lateral work.  A
GGV-minimal pair is merely not guaranteed to be `td`-minimal; GGV selection
does not forbid running the pure-Sigray selection in parallel.

Minimality supplies leverage only after one constructs an actual
lower-degree polynomial Keller counterexample.  It repairs neither monodromy
seam above and inherits the existing Sigray source-trust obligations.

## 7. Card dispositions

`SCALE-PIN` / Card A must not launch as written.  It is the existing
`RPMC(1)` lane under new notation.  The proposed audit cannot compute rootwise
slack for most records because `(B,{mu_P},{S_P})` is unfiled; assigning one
root per pole entry would manufacture data.  The entry identities and
`td=sum Lambda` are valid consistency checks but not a decisive experiment.
A counterexample to `RPMC(1)` would not refute `KJN(1)` or `TDBOUND`, as the
residue-A `4/3`/global-`1` separation already demonstrates.  A repaired future
card could acquire exact root custody and study `RPMC(C)` at `C>=4/3`, or
attack summed `KJN` directly.

`INERTIA-EXACT` / Card B stage 1 is duplicate and must not be promoted again.
The proposed fully determined residue-A passport is unavailable until finite
ends, contact orders, and target component/value grouping are complete.  Park
stage 2 behind both monodromy seams above.

## Promotion recommendation

Withdraw the blind lowering of Avenue 1 and the proposed raises of Avenues 6,
7, 25, 26, and 43.  Retain the capacity and marked-inertia machinery at their
existing canonical tiers.  In round synthesis, record the `4/3` correction,
the proper-root/pole-vertex distinction, the `e=1` fixed-point correction, and
the vertical-to-global block seam.  Await different-model cross-pollination
before treating this internal audit as promotion evidence.

No occurrence, attainment, bound, map, counterexample, or JC2 conclusion is
asserted.  No canonical file was edited by the audit lane.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7183`.
- Body SHA-256: `8856538b1afe4969dc054eb20f502c95943715549513ed1d44e1bef7e7a58997`.
- Frozen basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa`.
