# Hostile review charge: TD6 V89H15 all-q P13 full normal form

Date: 2026-08-26

Independently audit the frozen producer package

```text
cases/td6_c1_c2_c3_allq_mod_f_unitriangular_functional_v89h10_aws_20260826/
```

with controlling hashes

```text
P13_FULL_NORMAL_FORM_RESULT.md        29d5723b0d920840dbdfe72398624cfc0672843dbbf1d713b2fdd29dea52712c
P13_FULL_NORMAL_FORM_EVIDENCE.sha256  7c77bf767eea783d8d25a4c99c9201d039ed24d3a9037a1d2034accba569aa67
P13_FULL_NORMAL_FORM_FREEZE.sha256    4048419e15f366baeb03d242f546f096ee22d4529e6c6fededf58b2aea951c18
PREREGISTRATION_P13_FULL_NORMAL_FORM  f2ee138eea05933266577ab287f1baa05f570d5bfc901bdbdb5b0a4ed068d5ce
SOURCE_P13_FULL_NORMAL_FORM.sha256    6cb1b86d34d90fe28f7bfa24b0f8e78819372c425554b31a65a17a30d9f4d88c
source_p13_full_normal_form.tar.gz    2c13bd51601a64f3c2410bf4d36460f9f8741312aeef649299a22eb4fae3ff81
client                                6c06bed1dde0062d4eeed09b26f9cee11b10259f824fecd319fb3ae0c7a4fc7f
V1 environment erratum               84c51a206fe2577ed273e3d36bc09a2896ed73c3a5bc9c8c84aa2b5027dcaa6c
```

Charge every load-bearing point:

1. Rehash the freeze, source archive, both failed V1 evidence trees, and both
   successful R1 AWS trees.  Require rc 0 for R1 and byte identity of stdout
   and every mathematical output.  Distinguish the expected timing-only
   stderr differences.  Verify V1 stopped at the missing-`flint` import before
   algebra and that R1 changed only `PATH`, not source bytes.
2. Confirm exact `F=0`, registered `D(U*H*B3)`, all 22 independent,
   untruncated coordinates `q2,...,q14,q16,...,q24`, and q15 absent only as
   the reviewed target shear.  Verify literal CURRENT degree 13 is compiled
   from the generic source formula and has all 2,757 literal parameter terms.
   Seek numerical q assignments, q/parameter-degree caps, or omitted terms.
3. Rebuild literal 38-row FIRST and distinguish 132 transported coordinates,
   38 pivots, and 94 quotient variables.  Audit the common flag orientation,
   constant solve, every one of the 94 direction solves, direct replay in
   original FIRST, and the active omission fixture.  Require affine-map SHA
   `cc31df859f8142c00ed7da8858f9c1d4f8a19bc4a0cfe1ee27511a245987bb27`
   and exact equality with frozen H12.
4. Audit complete substitution into literal P13 and its omission fixture.
   Independently parse or recompute artifact SHA
   `9af3240d4016ad99766122303465d2cea7a10dc5e71b489f62564b9c3540c2d8`:
   exactly 95 parameter records, 238 scalar-coordinate terms, parameter
   support empty plus all 94 singleton quotient variables, q support empty
   plus all 22 retained q variables, parameter degree one, q degree one, and
   no mixed-q monomial.  Do not turn separate affinity into joint affinity;
   `q_e*y_j` terms are allowed.
5. Verify every y-dependent coefficient is supported only in E3 coordinates
   0 and 1 while the empty coefficient is supported in coordinates 0 through
   17.  Thus rows 2 through 17 are exactly 16 y-independent affine-linear q
   compatibilities.  This is a structural normal-form statement, not a
   combined P12/P13 common-zero verdict.
6. Audit denominator ledger SHA
   `6ad157b3e9212bbe8c2dd139cf84e71b78930ceea988b34cbed4b67cd507e0c7`.
   Up to units, allow only `U^7 V^4 (V^2-4U^3)^2` for the affine map and
   `U^5 V^4 (V^2-4U^3)^2` for P13.  Reject hidden determinants or any
   unregistered inverse.
7. Confirm this uses custom exact arithmetic rather than unsafe Singular
   qring equality/substitution/differentiation semantics.
8. Enforce scope: no P12/P13 combined exclusion or section, source-point or
   total-Rees claim, later-CURRENT conclusion, whole-TD6 closure, or JC2
   result follows from this theorem alone.

Return exactly one verdict: `CONFIRMED`, `CORRECTED`, or `FALSIFIED`, with the
smallest repair if applicable.  Write the complete report only to

```text
xmodel/td6-v89h15-allq-p13-full-normal-form-hostile-review-report-20260826.md
```

Do not edit the producer package, campaign ledgers, or `jc2-lean`.
