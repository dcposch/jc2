# Promotion: TD6 V89H10T all-q FIRST unitriangular flag

Date: 2026-08-26

Lifecycle: **PROMOTED / DIFFERENT-MODEL HOSTILE-REVIEW CONFIRMED.**

## Promoted theorem

On the frozen normalized three-center source slice, impose

```text
F=C*U-V^2+U^3=0,
q15 absent only under the reviewed target shear,
q2,...,q14,q16,...,q24 independent and untruncated,
```

and work on `D(U*H*B3)`.  For the pivot coefficient matrix `A(q)` of all
38 literal packed FIRST rows, put

```text
B=A(0)^(-1)*A(q),  N=B-I.
```

The unique 14-node strongly connected block of `N` involves only
`q2,...,q14`.  Its thirteen coefficient matrices admit one complete common
invariant flag.  The frozen constant basis `S` and its displayed inverse are
exact two-sided inverses, and each conjugated low-q coefficient matrix is
strictly upper.  Extending this basis by the identity to all 38 coordinates
and applying the frozen topological permutation makes the complete all-22-q
matrix `N` strictly upper.

Consequently

```text
N^38=0,
(I+N)^(-1)=I-N+N^2-...+(-N)^37
```

as exact polynomial matrix identities over the localized q-polynomial
coefficient ring.  Thus the full literal FIRST pivot block is unimodular;
no q polynomial is inverted.  All denominators of the two-sided basis maps
factor only through `U`, `V`, and `V^2-4U^3`, which are licensed on the
specialized `D(U*H*B3)` open.

## Validation and custody

- Producer result
  `cases/td6_c1_c2_c3_allq_mod_f_unitriangular_functional_v89h10_aws_20260826/FLAG_RESULT.md`,
  SHA256 `612b57bcfc20228152d37e5acef08ea41539481be99dff5878af8a790e4c6d1f`.
- Producer evidence manifest SHA256
  `69ebde85ff4ea117f887d9f56d9ef53da3a3676b0b4726bb653efa3bb6be022c`;
  freeze SHA256
  `a156f8394a2966effb006cdfdbb7e64a7da5cefa6e586022a67d29776167d2d9`.
- Hostile review
  `xmodel/td6-v89h10t-allq-simultaneous-triangular-flag-hostile-review-report-20260826.md`,
  SHA256 `16bfd903027a44bed2406017dec7a83eaa4a3b265edcc68c137192c6fe8ac317`,
  verdict `CONFIRMED`.
- Both AWS producer runs returned rc 0 with byte-identical stdout and all
  mathematical artifacts.  The reviewer rehashed the complete custody,
  checked the exact two-sided maps and conjugations, and independently
  reconstructed the flag at four registered-open specializations.

## Scope firewall

This theorem concerns the FIRST pivot module after the exact `F=0`
specialization.  It does not compile or reduce P12, prove a unit ideal or
source-point exclusion, license q15 as a source coordinate, provide a
total-Rees/source map, close TD6, or resolve JC2.
