# Erratum: staged-N13 localization was omitted from P12/N13 atlas claims

Frozen status: **scope reversal and quarantine.**  This erratum does not
alter any previously frozen byte.

## Exact defect

The V43/V44/V45 replays prove a genuine polynomial identity between P12,
the first-row module, and an abstract staged compatibility
`N13=(k/25)beta`.  They correctly emit denominators for P12, the first rows,
the P12 lift, and the multiplier of N13.  They do **not** compose the N13
left-null vector through previous/pole, first, and transport rows in the same
file:

```text
N13_full_source_lift_in_this_file=false
```

Consequently, lines such as

```text
all_denominator_radicals_subset_U_H_B3=true
```

apply only to the in-file P12 side and N13 multiplier.  They do not license
descent of the separately staged N13 certificate across its own pivot
denominators.  The V34/V41 staged producer itself says

```text
raw_substrata_from_emitted_denominators_still_charged=true.
```

Thus the congruence

```text
P12 - (25/k)*T*N13 = -k/50  modulo the displayed equation rows
```

is exact on the common fraction-field localization, but no current package
proves it on all of `D(U*H*B3)` or across the whole H/B3/rational-line raw
strata.

## Complete emitted factor custody

The exact V34 factor lists are frozen verbatim, one factorization per file:

- `GENERIC_FACTORS.txt`: 44 printed irreducible factors, total-degree/term
  summary `(731,29782,4fa9cae7...)`; 41 are additional to `U,H,B3`.
- `H_ZERO_FACTORS.txt`: 36 factors, summary
  `(571,188,30b24760...)`; 33 are additional to `U,V,P3`.
- `B3_PARAM_FACTORS.txt`: 37 factors, summary
  `(263,258,92cc7da6...)`; its intersection with the V44 chart charge is
  only `tau`, `2tau-1`, and `tau^2-4tau+2`, leaving 34 additional factors.

The full original outputs are retained under `evidence/`; the attachment
files are literal extractions of their
`N13_full_stage_denominator_factor=` lines.  The factor lists are pivot-
order dependent upper bounds, not asserted intrinsic exceptional divisors.

## Affected frozen packages

The following immutable packages remain valuable exact fraction-field or
chart computations but their stated whole-open/whole-divisor conclusions
are quarantined:

- `td6_c1_c2_c3_q2_beta_generic_open_aws_20260825`: the sentence claiming
  every beta is excluded on all `D(U*H*B3)` is unsupported until the staged
  N13 localization is removed or covered.
- `td6_c1_c2_c3_q2_beta_h_divisor_aws_20260825`: the stated whole-`H=0`
  conclusion omits the specialized V34 N13 factors in
  `H_ZERO_FACTORS.txt`.
- `td6_c1_c2_c3_q2_beta_b3_divisor_aws_20260825`: the stated whole-`B3=0`
  conclusion omits the chart-specialized V34 N13 factors in
  `B3_PARAM_FACTORS.txt`.
- `td6_c1_c2_c3_q2_beta_rational_raw_lines_aws_20260825`: the V45
  `V=0,C=3U^2` and `V=0,C=-5U^2` all-beta claims consume abstract N13
  without a frozen full staged source lift on those lines.  The V46 direct
  first-stage unit incompatibility on `V=0,C=-U^2` is independent of N13
  and remains valid.

Any atlas or fixed-A3 all-beta promotion descendant is withdrawn.  No such
atlas package was frozen; its empty staging directory was removed.

## Unaffected narrow results

The all-beta `U=0` theorem remains valid: it is a denominator-one unit
incompatibility already in the first original rows and does not consume
N13.  The exact P12 identities, ranks, term counts, denominator expressions,
canonical serialization, and fraction-field identities in V43/V44/V45 also
remain valid in their corrected localized scope.

## Clean repair gate

The preferred repair is not immediate 41-factor recursion.  Produce a fully
composed original-source certificate for
`P12-(25/k)T*N13`, and audit the denominator after multiplying the actual
N13 ancestry by `T`.  In parallel, compute the full staged ancestry in an
independent row/variable/pivot order.  If the two residual denominator
radicals are comaximal after removing `U,H,B3`, an explicit Bezout
combination gives a polynomial source identity covering `D(U*H*B3)`.
Otherwise every surviving factor-zero stratum must be rebuilt exactly.

Precisely, in `R=(center ring)[1/(U*H*B3)]`, two staged certificates must
emit cleared original-source identities
`d_i*(N13-k*beta/25) in I` and explicit coefficients with
`a*d_1+b*d_2=1` in `R`.  Only those three checked identities imply
`N13-k*beta/25 in I`; composing that result with V43 then puts `-k/50` in
`I`.  A printed gcd or radical comparison without the cleared identities
and Bezout replay is insufficient.

No whole fixed-A3, whole TD6, SP-2, landing, or JC2 claim is licensed.
