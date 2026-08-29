# Hostile review — TD6 V89H9 q12 polynomial extension of the q14 functional

| Field | Value |
|---|---|
| Target | V89H9 `RESULT.md`, `FREEZE.sha256`, `EVIDENCE.sha256`, `SOURCE.sha256`, `source.tar.gz`, client; reviewed parent V89H8 `RESULT.md`; reviewed parent V89H7 `RESULT.md`; H7 and H8 hostile reviews |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest bad coefficient / denominator / omission | none |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile algebra review. Producer `PASS` banners, dual-host byte identity, and RSS/elapsed lines are custody only |
| Method | SHA-256 of every charged pin and every consumed manifest row; flint identities in `Q[C,V,U]` and `Q[V,U]`; independent parse of the frozen remainder/SCC/support artifacts; source review of V87 reconstruction (transport and `Q_PRIME`), H5 division-free adjugate, H6 full-pivot inverse and `F=0` map, and the H9 q12 projection/extension. No Singular, Sage, Lean, or `jc2-lean`. The AWS client was not re-executed (wrapper gated to Amazon Linux); the exact functional and q-support are recovered from the pinned source plus the frozen artifacts |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Prompt SHA-256 `57309c11d42e6b99bdaa9d6b70b39aeadd735b034a6b8ff205f0f69ee7d90118` matched. Independently recomputed SHA-256 of every required primary pin matches. Every path named in `FREEZE.sha256` (10/10), `EVIDENCE.sha256` (22/22), and `SOURCE.sha256` (21/21) rehashes to the printed digest. Every `SOURCE.sha256` row exists at the case root and as `source/<path>` inside `source.tar.gz`, and both copies match. All 56 payload-closure files exist inside the same tarball and on disk and match. Nested compiler hash pins consumed from that archive also match. Producer `TD6-V89H9-Q12-Q14-MOD-F-FUNCTIONAL-EXTENSION PASS` was not used as algebra. No file other than this review was written. The frozen producer package was not edited.

---

## Verdict

**CONFIRMED.**

Starting from reviewed V89H8, the client restores q12 as an independent untruncated variable, keeps `q2,...,q11=0`, omits q15 only under the reviewed target shear, and retains independent untruncated `q13,q14,q16,...,q24`. It rebuilds genuine P12 and all 38 original packed FIRST sources with both the g-X transport injection and the `Q_PRIME` direct path live, then imposes `F=CU-V^2+U^3=0` by the two-sided chart `C=(V^2-U^3)/U` on `D(U)`. The raw common denominator is exactly `U*H=U(C-3U^2)`, coprime to `F`.

The specialized 38-by-38 FIRST pivot graph has exactly one cyclic SCC

```text
(0, 1, 2, 3, 4, 5, 6, 11, 12, 13)
```

and that 10-node block's determinant is literally `QPoly(1)`. The adjugate inverse is division-free and refuses any other determinant; `QPoly.inverse` refuses a nonconstant q polynomial; the unitriangular condensation inverse multiplies only. No q polynomial and no new unregistered base factor is inverted. Both products of the full inverse are the identity, the original sources are recovered from the normalized rows, the normalized rows are monic in distinct pivot variables with pivot-free tails, and literal P12 is replayed against the original sources.

The canonical P12 normal form has nonconstant q-support exactly `(12,), (13,), (14,)`, total q-degree one, q12-degree one, and no `q12*q14` or higher term. The pure-q14 empty-parameter E3-coordinate-0 value equals the reviewed H7 functional

```text
N / [V^3 (V^2-4U^3)^2]
```

with the same nonzero `N`. Unique remainder on the restored ring makes this a well-defined K-linear quotient functional; absence of mixed q12-q14 terms makes its value on P12 independent of q12 as a polynomial.

This restores q12 only. It is not a unit ideal, a source-point exclusion, a q2..q11 cover, a q15 source theorem, total-Rees lifting, whole TD6, or JC2.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Frozen pins | hashes | all required pins match, including parent H8 / H7 `RESULT.md` and both hostile reviews |
| 0. Manifests | every named file | `FREEZE` 10/10, `EVIDENCE` 22/22, `SOURCE` 21/21, `PAYLOAD_CLOSURE` 56/56; tarball copies match |
| 0. Dual AWS | hosts, archive, rc | distinct Box02 / r6d; archive `1babd74c…`; both `rc=0`; math artifacts and stdout byte-identical |
| 1. Source custody | archive, dual hosts | holds |
| 2. Literal P12 / 38 FIRST / both q paths | V87 rebuild, 38 rows, transport + `Q_PRIME` | holds |
| 3. Literal q scope | q2..q11 zero, q15 absent, untruncated q12,q13,q14,q16..q24 | H9 `ALLOWED_Q` / `ZERO_LOW_Q`; V87 `Q_EXPONENTS` skips 15; untruncated `QPoly` |
| 4. Exact F=0 on `D(U)` and `U*H*B3` firewall | `C=(V^2-U^3)/U`; no hidden SCC inverse | holds; `gcd(U*H,F)=1`; adjugate refuses nonunit det |
| 5. 10-node SCC det=1 / two-sided inverse / recovery | SCC `(0,1,2,3,4,5,6,11,12,13)`, literal unit, recovery before division | holds; H5 hardcoded `SCC` unused |
| 6. NF q-support | exactly `(12,),(13,),(14,)`, 17 parameter terms, total q-degree 1, no mixed/higher term | remainder TSV independently confirms |
| 7. Pure-q14 empty coord-0 equals H7 | exact match to reviewed H7 `N/den`; unique-NF quotient functional | holds; H8 remainder is an exact subset |
| 8. No Singular-qring dependency | no qring/std/subst/diff; explicit FIRST quotient | holds |
| 9. Conclusion strength | q12 polynomial extension only | slogans and `RESULT.md` keep the firewall |

---

## 1. Charge 1 — exact source custody and dual-AWS byte agreement

Recomputed SHA-256 of the required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `RESULT.md` | `83eae9d383826a6b2bda259768f27324a1db152b3f3f6c544524b7053172c4c8` | producer result |
| `FREEZE.sha256` | `fbbd6d53b6bb75329142e8bef51361941062333f590c755042124984d23e78e2` | freeze |
| `EVIDENCE.sha256` | `374f7823948b88b956993fcbfe536792fd9070ac6a030dcec1ed1204258dfdd3` | evidence manifest |
| `SOURCE.sha256` | `fc4ca45fdbdea2855b1a4c32460331d63e0de9c1258fb0f3a49ef97502b9c3fc` | source manifest |
| `source.tar.gz` | `1babd74c3b823045b524699fcde5ff37b85614bcd39c4b3e52b938a898e71300` | source archive |
| client `replay_v89h9_q12_q14_mod_f_functional_extension.py` | `d5014ed29582a90384712403a103fcc05f60f42d995b7eb2194781e83d3ab6ab` | controlling replay |
| parent H8 `RESULT.md` / `H8_RESULT.md` | `646dd1162cc2e6aa36c3fe72bea5c64a44e19361323593a12fc4c7f137cc0292` | reviewed parent theorem |
| parent H7 `RESULT.md` / `H7_RESULT.md` | `49b9dcba0bb5956dfdbb10293b7bdf3e440a39b127929089c2402ffb06db32cd` | reviewed H7 functional |
| H8 hostile review | `49865ee96582302b6bb9a1aa6aa47733ab88dc738d28ed67861b804a2d90240a` | parent review, verdict `CONFIRMED` |
| H7 hostile review | `99f7124e50db3daded967f42fe7591c06e27cfa05fe681537fed3aab5013ad6b` | H7 review, verdict `CONFIRMED` |

Nested compiler pins reached from the frozen H9 client, independently rehashed:

| Pin | SHA-256 |
|---|---|
| H6 parent client | `1301a09f0497abac5197de6b4afc0eba54b5c8de2b05d2cf11db63fab454d757` |
| H5 parent client | `a81c358b58f8b97ec0dfd97128d0f9539782eda70e66a6747a4c2827a1539b9b` |
| V87 parent client | `7c0890abbce996a221f9389372fa3705742d6ecd72531891bfeb5dfc2f1b9463` |
| V86 parent client | `5b160a2bd18434e6142c33be6775e0c212c22ebc67a52d08b246dd0223decd7c` |
| V85 parent client | `ab9753073d694242d4359dc1edc86774724f62d28d15b7c671ba0b796262100e` |
| generic parent shard | `a4ccd5d81101fdb82ed2f61571c258e2054961d161f4a98461b8f8614d3fd85e` |
| V85 source inventory | `9a612bb64ee974a506a1f3b7fcb471fb8924220ca6d24320af0fc9b8a7de6b7a` |
| F-raw P12 certificate | `8e892ffa914e0f93969abb9722f926486843f59cf77f5861c5ce3d3438281482` |
| parent H8 freeze | `56c0f208bb3e988577b11ca375089cd4586f413a11bfff2619b79d183dd296bd` |
| parent H8 evidence manifest | `4d9ddd036dbdbddd04d465ecda34d4950eec23a6778bf946234e66c0b41e30b1` |
| parent H8 source manifest | `2db0723fb0b15fc7d7aa1b353eb6571c73b8d69187c6c1469ea319efb88ee761` |
| parent H8 client | `2bdaac1fbec33e8616ab7f1e2d79f4d5e61c03852369b2bac6a0a19108f432b6` |
| parent H7 freeze | `7115c67a564b1f174a2e7337a1e64566b8ad2a422405c7243dfee9e8de77a6e0` |
| parent H7 evidence manifest | `1565fea5f95c65db6112b44eca984fc103660bea722421bdaead77847db925d0` |
| payload closure | `cbe7e0be9d49f5aa994790332e2fe0368c32780eac81ee3ddededdf7bb3d5cff` |

Byte-identical mathematical stdout is `8d799a20b15f7206c7495ea837df943002f9849ba18aeaac9400f425fd00d039` on both hosts. Mathematical output files:

| Output | SHA-256 |
|---|---|
| `Q12_EXTENSION_SCC_DETERMINANTS.tsv` | `52188fe1c05d25ea82947334dca3e25bb54fa5f4909c409cedbd20a52d31fd79` |
| `Q12_EXTENSION_CANONICAL_REMAINDER.tsv` | `db55d372399375c4dd94fa3df91bf694ab23e9428b1b1ce7f1ec81d7b91a9911` |
| `Q12_EXTENSION_Q_SUPPORT.tsv` | `7ab50a6796be631896692a5e5465ac5e150a6855fc43eb19fbc48a16c66e3c15` |
| `Q12_FUNCTIONAL_EXTENSION_RESULT.txt` | `57f405a24c81597b00d89d73323382149ec57657cf5d8d5d1ab8f44d6db07db2` |

Box02 (`ip-172-30-0-186`, pid 309222, tag `…box02_20260826T192100Z`, finished `2026-08-26T19:57:40Z`) and r6d (`ip-172-30-0-45`, pid 329529, tag `…r6d_20260826T192100Z`, finished `2026-08-26T19:57:41Z`) are distinct hosts with the same archive `1babd74c…`, both `rc=0`, and zero swap. Mathematical stdout and the four output files are byte-identical. Host stderr differs only in `/usr/bin/time` counters (37:10.76 vs 37:12.64; RSS 304544 vs 305020 KiB). `launch.meta`, pids, and finish timestamps differ as they should. Dual-host equality is custody, not the identity.

`source.tar.gz` contains 102 members (78 files, 24 directories) and no bytecode. Every charged `SOURCE.sha256` and `PAYLOAD_CLOSURE.sha256` path is present and hash-correct. The archive also contains the runtime checksum file `source/SOURCE.sha256`, which is the freeze-pinned manifest. Nested `q2_beta_dual` compiler `dcc7003d…` is in the payload closure. The only case-root file in neither `FREEZE.sha256` nor `SOURCE.sha256` is `FREEZE.sha256` itself. The H8 client is in `SOURCE.sha256` and is not imported by H9; H9 reads `replay_v89h6_q14_mod_f_cokernel.py`, `H7_RESULT.md`, and `H8_RESULT.md` (hash pins at lines 12–20).

---

## 2. Charge 2 — literal P12, all 38 original FIRST rows, both q paths

Genuine P12 is the inlined degree-12 raw CURRENT formula `compile_current_degree12` (`replay_v87tfaq_total_f_allq.py` lines 260–310), not staged CURRENT/PREVIOUS/POLE. Genuine FIRST is `qd.pack("X-2", qd.first_band_polynomials(f1,g1))` (lines 250–257). H9 rebuilds both live (`replay_v89h9_q12_q14_mod_f_functional_extension.py` lines 122–124) and then projects by its own `ALLOWED_Q`. Original sources are the affine packing `v87.source_polynomial = v86.source_polynomial` (constant term plus linear jet variables).

Both q-injection paths are retained before projection:

- Transport: `build_bands` reconstructs f-transport from `{15: 1}` and g-transport from `{1: 1, 25: 1}`, then `propagate_all_q` injects `QPoly.variable(exponent)` on every `("g","X",0,exponent)` source (V87 lines 192–222, 313–338). V87 asserts `set(seen.values()) == {1}` for every exponent in `Q_EXPONENTS`; H9 additionally asserts `seen[exponent]==1` for every retained exponent including 12 (H9 line 128) and `events==2` with `len(first)==38` (line 127).
- Direct `Q_PRIME`: `configure_qd(None)` (the default of `compile_first` and the explicit argument of `compile_current_degree12`) sets `qd.Q_PRIME[exponent-1] = exponent * q_exponent` for every `Q_EXPONENTS` entry, including `Q_PRIME[11] = 12*q12` (V87 lines 225–236). FIRST consumes that table through `first_band_polynomials`; P12 consumes it at V87 lines 284–288. H9 never calls `omit_direct` or `omit_transport_path`.

H9 does not replay V87's omission inventory. That inventory is a V87 diagnostic, not an H9 gate. Independent remainder support `(12,)` after specializing `q2..q11=0` shows that q12 enters through monomials free of the killed variables, so the retained paths are not an empty mixed-only residue.

Before specialization H9 demands the raw common denominator of P12 and the 38 original sources (lines 132–133):

```text
assert raw_common == U*H and raw_common.gcd(F).total_degree() == 0
```

Stdout records `raw_source_common_denominator=(C*U - 3*U^3)`, which is `U*H`. Flint: `gcd(U*H, F) = 1` in `Q[C,V,U]`. Allowed factors of the V85 chart are `(U, H, B3)` (`replay_v85tf1_total_f.py` line 51), so `U*H` is a registered denominator.

---

## 3. Charge 3 — exact variable scope

V87 `Q_EXPONENTS = tuple(list(range(2, 15)) + list(range(16, 25)))` (`replay_v87tfaq_total_f_allq.py` lines 32–34) has length 22 and does not contain 15. `QPoly` is an untruncated sparse ring on that set (class docstring line 41; constructor lines 52–54 refuse any exponent outside `Q_ORDER`; `inverse` at lines 111–118 fail-closes unless the support is the empty q-monomial). Mixed monomials are stored as sorted tuples (lines 93–107), so `q12*q14` would appear as `(12, 14)` if present.

H9 splits that set as `ALLOWED_Q = (12, 13, 14) + tuple(range(16, 25))` and `ZERO_LOW_Q = tuple(range(2, 12))` (`replay_v89h9_q12_q14_mod_f_functional_extension.py` lines 30–31). The union is exactly `Q_EXPONENTS`. Projection keeps a monomial if and only if every exponent lies in `ALLOWED_Q` (lines 34–40). Empty monomials (q-constants) are kept. A mixed monomial such as `q11 q12` is dropped, which is the specialization `q2=…=q11=0`. A monomial `q12 q14` or `q12^2` is kept: q12 and q16…q24 are not truncated. H5's `TAIL = (14,) + range(16, 25)` and `LOW = range(2, 14)` (`replay_v89h5_q14_high_unimodular_total_f_v1.py` lines 26–27) are not used for this projection; H9 does not call `h5.project_first`. H8's `ALLOWED_Q` starts at 13; H9 is that split with q12 restored.

Why q15 is a legitimate quotient coordinate, not a silently omitted source modulus:

- f-transport is built from `{15: 1}` at degree 15 (V87 lines 317–320): frozen `p=t^{15}`.
- g-transport is built from `{1: 1, 25: 1}` only (lines 321–324): frozen `q=t+…+t^{25}`.
- Holding the degree-15 coefficient of `q` at zero is the reviewed target shear.

Wrapper environment `TD6_Q_SCOPE=q12-q13-q14-q16-q24` (`run_v89h9_q12_q14_mod_f_functional_extension.sh` line 11) matches this split. Stdout records `retained_q_exponents=12,13,14,16,…,24` and `zero_low_q_exponents=2,…,11`.

This is not a q2..q11 cover, an independent q15 source modulus, a total-Rees lift, or a TD6 statement.

---

## 4. Charge 4 — `F=0` on `D(U)` and the `D(U*H*B3)` firewall

`F = C*U - V**2 + U**3` and `H = C - 3*U**2` are the V85 literals (`replay_v85tf1_total_f.py` lines 44–45). The two-sided chart is `SPECIAL_C = (Rat3(V)**2 - Rat3(U)**3) / Rat3(U)` (line 47). `specialize_polynomial_value` (lines 149–161) substitutes that chart coefficientwise on `Q[C,V,U]`, which is regular precisely on `D(U)`. Substituting into `F` gives

```text
((V^2-U^3)/U)*U - V^2 + U^3 = 0.
```

H9 applies this map via `h6.specialize_first` / `h6.specialize_polynomial` (`replay_v89h6_q14_mod_f_cokernel.py` lines 30–59; H9 lines 138–139). Flint polynomial identities:

```text
U*H - F - (V^2-4U^3) = 0,
gcd(U*H, F) = 1 in Q[C,V,U],
gcd(U, F) = 1.
```

So on `F=0` one has `U*H = V^2-4U^3`. Restricting to `C=3U^2` leaves `4U^3-V^2 ≠ 0`, so `H` does not divide `F`. The same substitution `CU=V^2-U^3` sends the frozen B3 sextic (`payload/jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_trivariate.py` lines 53–56) to `V^4`.

No hidden SCC determinant inversion: cyclic blocks are inverted only after `determinant_subset` returns `QPoly(1)` (`adjugate_unit_inverse`, H5 lines 132–150). That determinant is division-free subset-DP (lines 112–129). A nonunit determinant takes the fail-closed branch (H9 lines 154–173) and never attempts P12 division. AWS took the unit path.

Remainder denominators, independently parsed from the frozen TSV, are all of the form `V^a U^b (V^2-4U^3)^c` (124 nonzero E3 coordinates, 0 unlicensed). Flint:

```text
V^4 - 8 V^2 U^3 + 16 U^6     = (V^2-4U^3)^2
V^5 - 8 V^3 U^3 + 16 V U^6   = V (V^2-4U^3)^2
V^7 - 8 V^5 U^3 + 16 V^3 U^6 = V^3 (V^2-4U^3)^2
```

and the six remaining dens are the same radicals times `U` powers. On `F=0` those radicals are factors of `U*H*B3`. Coefficient-field inversion of `A0` over `K=Frac(Q[V,U])` is not a q inverse and introduces no new unregistered base factor.

---

## 5. Charge 5 — 10-node SCC determinant one, two-sided inverse, recovery before division

H9 does not copy H8 remainder files and does not use H5's hardcoded `SCC = (0, 1, 2, 3, 4, 5, 6, 13)` (`replay_v89h5_q14_high_unimodular_total_f_v1.py` line 28). That constant is referenced only inside H5 `main()` (lines 559–588). The H9 diagnostic and the H6 inverter both recompute the graph of `N = A0^{-1}A - I` from specialized FIRST (`pivot_diagnostic`, H9 lines 63–88; `invert_full_q_pivot`, H6 lines 62–86). H9 asserts `telemetry["cyclic"] == cyclic` (line 176).

Stdout records

```text
q12_extension_FIRST_cyclic_components=((0, 1, 2, 3, 4, 5, 6, 11, 12, 13),)
q12_extension_FIRST_components=((0, 1, 2, 3, 4, 5, 6, 11, 12, 13), (7,), …, (37,))
q12_extension_all_SCC_determinants_one=true
```

Ten plus twenty-eight singletons is 38. Restoring q12 enlarges the H8 9-cycle by row index 11; these are pivot-block row indices, not q-exponents.

`Q12_EXTENSION_SCC_DETERMINANTS.tsv` contains exactly one record: component `(0, 1, 2, 3, 4, 5, 6, 11, 12, 13)`, q-monomial `()`, E3 coordinates `(1/1, 0, …, 0)`. That is literally `QPoly(1)`, not a cancelled ratio and not a unit of `K` other than `1`.

The inverse path is:

1. Invert the q-constant block `A0` over E3 (`h5.inverse_constant_matrix`). This is inversion in the coefficient field `K=Frac(Q[V,U])`, not a q inverse.
2. Cyclic blocks are inverted by `adjugate_unit_inverse`: the inverse is the cofactor matrix; any determinant other than `QPoly(1)` is refused before a single division. Both products of the adjugate against the block are asserted to be the identity.
3. The condensation is unitriangular in a topological order and inverted by `polynomial_matrix_inverse` (H5 lines 347–370), which only adds and multiplies.
4. `QPoly.inverse` cannot invert a nonconstant q polynomial (V87 lines 111–118).

H9 then asserts both `T A = I` and `A T = I` (lines 177–178). Normalized rows are original-source linear combinations via `T` (lines 179–181). Recovered rows via `A` equal the specialized original sources (lines 182–183) **before** P12 division. `base_pivot_columns` asserts 38 distinct pivots (H5 lines 167–197). H9 then checks that each normalized source has coefficient `1` on its own pivot monomial and that every other monomial is pivot-free (lines 184–189). `divide_by_normalized_first` additionally demands `source.get((pivot,)) == QPoly(1)` (H5 line 384). Tails therefore cannot reintroduce a pivot, so reduction order is irrelevant and the remainder is unique.

P12 division (H9 lines 193–200) pushes quotients through `T` and replays against the original sources: `sum relations_i * original_source_i + remainder = specialized_P12`. Stdout ends at `p12_division_pivot=38/38;remainder_terms=17`.

The two-sided coefficient-ring identities identify the original-FIRST ideal with the ideal generated by the normalized rows. Unique remainder then vanishes on the whole ideal. H9 does not re-loop `reduce_quiet` on the 38 generators the way H7 did; that loop is redundant given `T A = I`, recovery, and pivot-free tails, and it is not a charged gap.

Independent remainder check: the 17 parameter monomials are `(), 6, 8, 9, 11, 12, 13, 15, 16, 17, 18, 20, 21, 22, 24, 25, 27`. The H6/H7 q-constant pivot list

```text
[0, 2, 1, 3, 4, 5, 7, 10, 14, 19, 23, 26, 28, 29, 30, 31, 32, 33, 34, 35,
 39, 42, 46, 52, 57, 63, 71, 78, 86, 95, 103, 110, 116, 121, 125, 128, 130, 131]
```

is determined by `A0`, which is unchanged by restoring nonconstant q12. Those 17 remainder monomials are disjoint from the 38 pivots.

---

## 6. Charge 6 — literal P12 replay, 17-term remainder, exact q-support

`h6.qpoly_support` (`replay_v89h6_q14_mod_f_cokernel.py` lines 159–165) collects every non-empty q-monomial appearing in any parameter coefficient. H9 writes that list verbatim to `Q12_EXTENSION_Q_SUPPORT.tsv` (H9 lines 226–229) and also writes every `(parameter, q)` pair of the remainder via `h5.write_polynomial` (H5 lines 413–420). Mixed q12-q14 terms and higher powers would appear as `(12, 14)`, `(12, 12)`, `(14, 14)`, …; they are not truncated.

Independent parse of the remainder TSV: 52 data rows, 17 parameter monomials, q-monomials exactly `()`, `(12,)`, `(13,)`, `(14,)`. The empty q-monomial occurs once, on the empty parameter monomial (the q-constant unit). Every one of the 17 parameter monomials carries `(12,)`, `(13,)`, and `(14,)`. Support TSV lists exactly

```text
(12,)
(13,)
(14,)
```

Stdout: `q_support_count=3`, `max_total_q_degree=1`, `max_q12_degree=1`, `q12_q14_mixed_support_count=0`. There is no omitted mixed or higher term, including no `q12*q13`.

Hostile subset check against reviewed H8: every one of the 35 H8 remainder records appears byte-identically in the H9 remainder; the 17 new H9 records are exactly the `(12,)` slice. Restoring q12 did not perturb the q13 or q14 coefficients.

---

## 7. Charge 7 — extracted q14 functional equals reviewed V89H7

H9 extracts

```text
q14_empty = remainder[()].coefficients[(14,)]
functional = Rat3.coerce(m.r.scalar_coordinates(E3.coerce(q14_empty))[0])
assert functional == expected_functional and functional
```

(`replay_v89h9_q12_q14_mod_f_functional_extension.py` lines 202–217). `expected_functional` is the displayed H7 value `N / [V^3 (V^2-4U^3)^2]` with `N` copied from pinned `H7_RESULT.md` lines 45–50. The live remainder TSV empty-parameter `(14,)` coordinate 0 is exactly

```text
numerator   = 3856216/375*V^10*U^2 + 1625866424/375*V^8*U^5
            + 30525031264/375*V^6*U^8 - 10638708808/375*V^4*U^11
            - 4168187296/75*V^2*U^14 + 710528/15*U^17
denominator = V^7 - 8*V^5*U^3 + 16*V^3*U^6
```

matching reviewed H7 `Q14_DUAL_FUNCTIONAL_EXACT.txt` lines 6–7 (SHA `bdf711b8…`) and matching the H8 remainder empty-`(14,)` E3 element in all 18 coordinates. Coordinates 8–17 of that E3 element are `(0,1)`. Flint: the denominator equals `V^3 (V^2-4U^3)^2`, `N ≠ 0`, and `gcd(N, den) = 1` in `Q[V,U]`. Factorization of `N` is the H7 factorization

```text
(728/375) U^2 (5297 V^{10} + 2233333 V^8 U^3 + 41929988 V^6 U^6
             - 14613611 V^4 U^9 - 28627660 V^2 U^{12} + 24400 U^{15}).
```

Evaluation at the H7 fresh point `(V,U)=(4,1)` is `605650778369/9000`, which reduces to `159760` modulo `1000033`.

Well-definedness: unique remainder on the restored ring (charge 5) makes every coefficient of NF a K-linear functional of the input that vanishes on original FIRST. The selected coordinate is not a pivot (pivots are jet variables; the empty parameter monomial is not among them). It is not obtained by truncating q-support (charge 6). Because there is no mixed q12-q14 term, this coordinate of NF(P12) is independent of q12 as a polynomial, so the reviewed H7 functional extends polynomially across arbitrary q12 on this residue block.

H9 does not re-assert `B3=V^4` and `U*H=V^2-4U^3` live. Exact equality with the H7 functional plus the independent flint identities of charge 4 recover the same denominator firewall. The result-file slogan `functional_denominator_radical_subset_U_H_B3_on_F_zero=true` is therefore inherited, not assumed.

---

## 8. Charge 8 — no Singular-qring equality, substitution, or differentiation

The frozen clients and the 56-file payload contain no Singular `qring`, `std`, `subst`, or `diff` call, and no Sage session. The only `singular_` strings are fail-closed assert names (`singular_base_pivot_block`, `singular_prime_FIRST`). Coefficient arithmetic is python-flint `E3` / `QPoly`. The quotient is the explicit rewriting system `divide_by_normalized_first` (H5 lines 380–410): monic distinct pivots, pivot-free tails, and a replay identity `sum quotients_i * normalized_i + remainder = P12`. H9 then pushes those quotients through `T` and replays against original sources. That is an explicit polynomial quotient, not a CAS normal-form oracle.

---

## 9. Charge 9 — conclusion strength

Reporter writes such as `q12_extended_functional_equals_H7_exact=true` (H9 line 236) and `q12_polynomial_functional_extension=true` (result artifact line 10) are preceded by the unit-determinant gate, the two-sided maps, the remainder extraction, and `assert functional == expected_functional`. The fail-closed branch (H9 lines 154–173) would have stopped before P12 division if a cyclic determinant were non-unit; AWS took the unit path. Firewall slogans `unit_ideal_claim=false`, `whole_TD6_killed=false`, `JC2_resolved=false` are all present. No client assert takes the extension as a hypothesis.

The strongest statement supported by the package is:

> After exact `F=0` on `D(U)`, restoring independent untruncated q12 in the reviewed H8 residue (`q2=…=q11=0`, q15 absent only under the target shear, `q13,q14,q16,…,q24` independent and untruncated), the full original-FIRST pivot block remains polynomially invertible over `Frac(Q[V,U])[q12,q13,q14,q16,…,q24]`, with unique cyclic SCC `(0,1,2,3,4,5,6,11,12,13)` of determinant one. The H7 q14 empty-parameter E3-coordinate-0 functional remains a well-defined nonzero quotient functional of unique NF, and NF(P12) is linear in q12 with no mixed q12-q14 term.

`RESULT.md` lines 37–38 and the result artifact lines 13–15 refuse a unit ideal, source-point exclusion, q2..q11 restoration, q15 as a source modulus, total-Rees, whole TD6, and JC2. That is the correct strength.

---

VERDICT: CONFIRMED
