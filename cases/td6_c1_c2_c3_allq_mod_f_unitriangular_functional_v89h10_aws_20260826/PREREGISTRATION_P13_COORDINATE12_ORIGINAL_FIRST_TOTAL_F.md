# TD6 V89H19R2 original-FIRST / total-F certificate producer

Date: 2026-08-26

Status: preregistered producer gate.  No result is claimed before two
independent AWS hosts return rc 0 with byte-identical mathematical outputs,
the pass banner, and the full telemetry block below.  This freezes Stages 4
and 5 of the independent H19 design
`xmodel/td6-h19-original-first-total-f-certificate-grok-20260827.md`.

This successor does **not** recompute another quotient normal form.  It emits
explicit original-FIRST membership multipliers for E3 coordinate 12 of the
literal CURRENT degree-13 parent, and then a denominator-cleared lift into the
total localized ring `D(U*H*B3)` in which `F` is divided, never inverted.

## Charged pins (all rehashed by the client before any algebra)

| Artifact | SHA-256 |
|---|---|
| H15 client `replay_v89h15_allq_p13_full_normal_form.py` | `6c06bed1dde0062d4eeed09b26f9cee11b10259f824fecd319fb3ae0c7a4fc7f` |
| H15 archive `source_p13_full_normal_form.tar.gz` | `2c13bd51601a64f3c2410bf4d36460f9f8741312aeef649299a22eb4fae3ff81` |
| H15 result | `29d5723b0d920840dbdfe72398624cfc0672843dbbf1d713b2fdd29dea52712c` |
| H15 freeze | `4048419e15f366baeb03d242f546f096ee22d4529e6c6fededf58b2aea951c18` |
| H15 evidence | `7c77bf767eea783d8d25a4c99c9201d039ed24d3a9037a1d2034accba569aa67` |
| H15 count erratum | `27d8289d7215d16806d1f1197b137acc7d49b0d75a05c766833eaaa38db44418` |
| H18 unit TSV `P13_COORDINATE12_UNIT.tsv` | `c5d136d942177882424a75a47c631fbd386d7fff6dbb09187effd32f1be4687f` |
| H18 result | `0f152a88ba6422b04a3b4274ad5a0e71996c1c65395c7518b6e725321ab32d7f` |
| H18 freeze | `0d3a9a6aad58635e9f02f160a3012b28dc351ecdbbafd97e59b7c1c2cda44974` |
| H18 evidence | `bc9590017fb0f6942c9b7d396ba2b95e56fd1cbad2fc8c2b84e2b753bf79932d` |
| H19R1 client | `7919aa9d3a769e456abadd54eea12008b0a9121760b8382bbf8bdc72b3ec1784` |
| H19R1 runner | `11d3c15d39e6a0155b74f46eb7e8abcfe9d4e4fc84bac6954e2206e34eb0e9f4` |
| H19R1 preregistration | `c578f6124f41fe69fa94be4b9cb02c56353b294f57d37a0c862d39405b1d836e` |
| H19R1 source manifest | `a60d6fdb1e503caad7861cf1acd7ebc22a39eaac3ae53f1e1499514937f9c7d5` |
| H19R1 producer result | `6573626441e58560935e6c4efac15f7a2cda873afc42f56e42ae5f4ca56837e8` |
| H19R1 freeze | `35368feef910383f6199c9c95e91d4adb1ac0819cd6f1e3f930bd14b78c7d6a4` |
| H19R1 coord-12 TSV | `7ed98587b0c42de16ada758263707cd273f1c5356b4893e106c85f337abe7eae` |
| H19R1 addend TSV | `40d186434a1aa73c2c770663accb200f3ae6215e0fc9f00d6495ac7b2a7ce0d4` |

Reconstructed frozen objects (recomputed, not read):

| Object | SHA-256 |
|---|---|
| `N = A0^{-1}A(q)-I` | `38fb14e38daa36d597cc7ae1cd2bd5dd402ef2cd1587337321b8c204eeeb7f36` |
| flag basis `S` | `05f9b3df78dc4abcf6ad39c36e1b48c54529b351459664cccfa3cd59d49d1542` |
| `S^{-1}` | `30e644c244f65b17cbf9d7a599b60883d1e8c0b1dd6c3fb326c8ae70cda87aac` |
| upper order | `35e88aa807ba6a4a0e275f946c23e86b0b3e8fa8aa155684103a08ae13cacb6a` |
| strict upper `N` | `946b75e5307941a81696ec68e1ae2fbcb6ce480294cead6076e434d8e819e913` |
| affine FIRST map | `cc31df859f8142c00ed7da8858f9c1d4f8a19bc4a0cfe1ee27511a245987bb27` |
| complete P13 normal form | `9af3240d4016ad99766122303465d2cea7a10dc5e71b489f62564b9c3540c2d8` |

The `N`, `S`, `S^{-1}`, order and upper-`N` digests are enforced inside the
frozen `h11.reconstruct_flag`, which this client imports rather than forks.

## Environment (refuse any other value)

```text
TD6_Q_EXPONENT=2
TD6_Q_SCOPE=q2-q14-q16-q24
TD6_PIVOT_POLICY=ascending
TD6_PIVOT_SCOPE=all-staged
TD6_F_SPECIALIZATION=exact-C-equals-V2-minus-U3-over-U
OMP_NUM_THREADS=1
OPENBLAS_NUM_THREADS=1
TD6_H15_ARCHIVE=<path to source_p13_full_normal_form.tar.gz>
AWS_RUN_TAG=td6_v89h19r2_p13_c12_first_total_*
```

`sys.flags.optimize` must be `0`.  Packages: `python-flint==0.9.0` only.  No
Sage, no Singular, no Groebner engine, no 132-column dense solve.  Virtual
memory cap `805306368` KiB, wall cap `43200` s, one thread, dual hosts.

`ALL_Q = (2..14, 16..24)`; `15 not in ALL_Q` is asserted and reported.
Normalization is `F=0, D(U*H*B3)`.

## Licensed polynomial identities (asserted in the total ring before any F=0 use)

```text
U*H - (V^2 - 4*U^3) = F
B3 - V^4 = F * 4*U*(C + 5*U^2)
```

`B3 = V^4` and `U*H = V^2-4U^3` are used only after `F=0`, and only in a
display copy that is explicitly not the total-ring identity.

## Algorithm (frozen order)

1. **Custody.**  Rehash every pin above, recursively verify
   `SOURCE_RAW_P13_COORDINATE12_AUDIT_R1.sha256` and, through the imported
   H19R1 client, `SOURCE_P13_FULL_NORMAL_FORM.sha256`,
   `SOURCE_P12_FULL_NORMAL_FORM.sha256`, `SOURCE_P12_FLAG.sha256` and the
   complete `PAYLOAD_CLOSURE.sha256`.  Hash the H15 archive at
   `TD6_H15_ARCHIVE`.  Assert the two licensed identities.  Assert that the
   coordinatewise `F=0` specialization is multiplicative on a live E3 probe.
2. **Rebuild (one transport only).**  `v87.build_bands()`,
   `v87.compile_first(bands)`, `h15.compile_current_degree(bands, 13)`.
   Assert `events == 2`, `len(first) == 38`, `len(p13) == 2757`, the
   complementary free section is exactly `range(132)`, the q census is the 22
   licensed exponents with multiplicity one, `max(map(len, p13)) <= 2`, every
   FIRST source has parameter degree `<= 1`, and the raw common denominator is
   `U*H` with `gcd(U*H, F)` of degree `0`.  Retain the generic `first`,
   generic FIRST sources and generic `p13` for Stage 5.
3. **Full-E3 addend census.**  Rebuild the ordered literal degree-13 addends
   with the frozen H19R1 `raw_degree_contributions`, assert their sum equals
   the H15 compiler output, and emit every nonzero
   `(stage, label, parameter, q, coordinate)` of the four preregistered active
   addends over all 18 E3 coordinates, raw and after `F=0`.  Rebuild the two
   frozen H19R1 TSV texts and assert their digests.  Classify whether
   `f1_times_dg2:i=13:j=1` is a multiple of transport variable 29 as a full E3
   polynomial.
4. **Specialize and replay H15.**  `h6.specialize_first`,
   `h6.specialize_polynomial`; reconstruct `A0`, `A`, `D`, `N`, `W`,
   `inverse_W`, `upper_N` through `h11.reconstruct_flag`; assert
   `(entries, terms, degree) == (532, 6069, 1)` and the `N` digest; solve the
   constant and all 94 free directions with the H15 triangular path; write and
   digest-check the affine pivot map; assert pivot position 13 is variable 29
   and its affine image is the zero E3 polynomial; substitute the complete map
   into literal P13 with the frozen `h15.affine_substitute` (which carries the
   H15 first-nonzero omission fixture); assert the normal-form digest and that
   its coordinate-12 record set is exactly the H18 unit
   `(((), (), "3500000000/9*U", "V"),)`.
5. **Original-row inverse.**  For `j = 0..37` solve `A x = e_j` with the same
   `inverse_A0 -> inverse_W -> strict-upper back-substitution -> W` path H15
   uses for the affine map (H15 keeps it as a `main()`-local closure, so it is
   recomposed verbatim from the frozen `h12` primitives; no new algebra).
   Replay each column directly in `A`, then assert `A A^{-1} = I` and
   `A^{-1} A = I` over `QPoly`.  Emit `P13_ORIGINAL_FIRST_INVERSE.tsv`.
6. **Polarization.**  With `z_i = x_i - x_aff_i` for pivot `i`:

   ```text
   constant             contributes 0
   x_i                  c (x_i - x_aff_i)
   x_i x_j, i != j      c x_i (x_j - x_aff_j) + c x_aff_j (x_i - x_aff_i)
   x_i^2                c (x_i + x_aff_i) (x_i - x_aff_i)
   ```

   Free-variable differences are zero.  Assert
   `P13_special - P13_special o affine = sum_i g_i z_i` directly, assert
   `z_i = sum_k A^{-1}[i][k] FIRST_k_special` for every pivot `i`, and set
   `b_k = sum_i A^{-1}[i][k] g_i` with the frozen `h5.linear_combination`.
   Emit `P13_COORDINATE12_FIRST_MULTIPLIERS.tsv` and the coordinate-12
   projection `P13_COORDINATE12_FIRST_IDENTITY_C12.tsv`.
7. **Direct expansion check (load bearing).**  Rebuild `sum_k b_k FIRST_k`
   with `v87.multiply` / `v87.add` and assert
   `P13_special - sum_k b_k FIRST_k` equals the H15 normal form as a full E3
   polynomial, then that its coordinate 12 is the H18 unit.
8. **Omission control.**  Rebuild the parent with the preregistered H19R1
   source addend `f1_times_dg2:i=13:j=1` dropped before aggregation, require
   `omitted_parent != parent`, repeat steps 6 and 7 on it, and report
   `omission_changes_endpoint` and `omission_changes_cofactor`.  Fail closed
   if both are false.  Which one is true is deliberately not preregistered.
9. **FIRST-row control.**  Zero the least-index nonzero `b_k` and assert the
   expansion check fails.
10. **Stage 5, denominator clearing.**  With `kappa = 3500000000/9`, let `d` be
    the monic lcm, through the frozen `t.denominator_record` /
    `m.denominator_for` stack, of every scalar-coordinate denominator of
    `{b_k} u {P13_special} u {kappa U/V}`.  Assert every prime factor of `d`
    is `U`, `V` or `V^2-4U^3` up to units, write `d = U^a V^e (V^2-4U^3)^c`
    with `e >= 1`, and multiply the `F=0` identity by `9 U^a V^e (V^2-4U^3)^c`:

    ```text
    9 U^a V^e (V^2-4U^3)^c coord12(P13_special)
      - 3500000000 U^{a+1} V^{e-1} (V^2-4U^3)^c
      = coord12(sum_k beta_k FIRST_k_special),   beta_k = 9 U^a V^e (V^2-4U^3)^c b_k
    ```

    Assert every scalar coordinate of every `beta_k` has denominator `1`.
11. **Stage 5, total-F lift.**  Apply the same `beta_k` to the retained generic
    FIRST sources and generic P13, form

    ```text
    residual = 9 U^a V^e (V^2-4U^3)^c coord12(P13_generic)
             - 3500000000 U^{a+1} V^{e-1} (V^2-4U^3)^c
             - coord12(sum_k beta_k FIRST_k_generic),
    ```

    assert that the generic coordinate-12 expansion and the generic
    coordinate-12 P13 term specialize to the cleared `F=0` expansion and its
    left-hand side, assert `residual` is nonzero and specializes to `0`, divide
    it by `F` with
    the frozen V85 `divide_polynomial_by_f`, and replay
    `residual = F h`.  Audit the denominators of `beta_k`, `h`, generic P13,
    generic FIRST and every coordinate-12 product term with the frozen V85
    `assert_denominators_allowed`; require every factor in `{U, H, B3}` up to
    units and `gcd(Delta, F)` of degree `0`.  Scale by `Delta`, assert the
    cleared total identity, and assert every cleared object is
    denominator-one.  Emit `P13_COORDINATE12_TOTAL_F_MULTIPLIERS.tsv` and
    `P13_COORDINATE12_TOTAL_F_H.tsv`.
12. **Stage 5 controls.**  Dropping the P13 left-hand term must break the
    cleared total identity; dropping `F (Delta h)` must break it as well.

Deviation from the design text, declared in advance: the design names
`{beta_k, h, P13_generic, FIRST_generic}` for the `Delta` audit.  This client
additionally audits the coordinate-12 product terms `beta_k FIRST_k_generic`
and the cleared left-hand terms, following the V85 precedent, because `Delta`
must clear the products for the emitted identity to be polynomial.  That is a
strengthening, never a relaxation.  The residual is projected to coordinate 12
before `F`-division, so the type-matched frozen `v85.specialize_polynomial`
replaces the design's `h6.specialize_polynomial` in that one assertion; both
apply the identical exact substitution `C = (V^2-U^3)/U`.

## Negative controls (complete)

| Control | Requirement |
|---|---|
| H19R1 source addend | drop `f1_times_dg2:i=13:j=1` before aggregation; endpoint and/or cofactor must change |
| FIRST row | zero the least-index nonzero `b_k`; the expansion check must fail |
| P13 left-hand side | omit P13 from the cleared total identity; it must fail |
| `F` term | omit `F (Delta h)`; the cleared total identity must fail |
| H15 substitution fixture | the frozen `affine_substitute` first-nonzero deletion assertion |
| q15 | `15 not in ALL_Q`; any appearance is fail-closed |
| unregistered inverse | any denominator factor outside `{U, V, V^2-4U^3}` on `F=0`, or outside `{U, H, B3}` in the total ring, is fail-closed |
| SHA replay | affine map, normal form, `N`, flag, H18 unit, both H19R1 census TSVs |

## Stop rule

Exit nonzero and print no `PASS` banner on any of: a pin, archive, flint
module or reconstructed-artifact hash mismatch; `sys.flags.optimize != 0`;
`len(p13) != 2757`, `len(first) != 38`, free section `!= 132`, q census
`!= 22`; nonzero affine image of pivot 29; reconstructed affine or normal-form
digest mismatch; reconstructed coordinate 12 not the H18 unit;
`A A^{-1} != I`; `P13 - sum b FIRST != NF`; an omission control that changes
neither endpoint nor cofactor; inexact `F` division, an inverted `F`, or a
total-ring denominator outside `{U, H, B3}`; use of `B3 = V^4` or
`U H = V^2-4U^3` before `F=0` outside the two licensed identities; a loaded
`singular` / `sage` / Groebner module or a 132-column dense matrix path; a
nonzero rc on either host; or mathematical outputs that are not byte-identical
across hosts.

Legal banner, only after both hosts agree:

```text
TD6-V89H19R2-P13-COORDINATE12-ORIGINAL-FIRST-TOTAL-F PASS
```

Required telemetry in `P13_COORDINATE12_FIRST_TOTAL_F_RESULT.txt`:

```text
q15_absent_target_shear=true
affine_pivot_map_equals_frozen_H12=true
full_normal_form_equals_frozen_H15=true
coordinate12_equals_frozen_H18_unit=true
original_FIRST_inverse_replay=true
original_FIRST_expansion_equals_NF=true
omission_changes_endpoint=...
omission_changes_cofactor=...
F0_denominators_in_U_V_V2minus4U3=true
total_F_division_exact=true
total_F_not_inverted=true
total_family_denominator_radical_subset_U_H_B3=true
B3_eq_V4_only_after_F=true
UH_eq_V2minus4U3_only_after_F=true
independent_total_F_unit_claim=true
whole_TD6_killed=false
source_landing_composed=false
JC2_resolved=false
```

## Nonclaim

A pass certifies only that, on the charged slice,
`coord12(P13) - (3500000000/9)(U/V)` lies in the original FIRST ideal after
`F=0` with registered denominators, and that this membership lifts to
`s coord12(P13) - n = sum_k B_k FIRST_k + F h` in `D(U*H*B3)` with polynomial
`s, n, B_k, h`.  It does not restore q15 as an independent source modulus,
cover any omitted TD6 modulus (orbit, pole, correction, centering, boundary or
other), produce a total-Rees or source point, combine P12, compose the source
landing, close TD6, prove SP-2, or resolve JC2.  The last three telemetry
lines stay `false` on a pass.
