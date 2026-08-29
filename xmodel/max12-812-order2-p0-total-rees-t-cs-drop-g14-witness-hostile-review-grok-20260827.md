# Hostile review: V18R1 drop-grade-14 exact-Q witness

**Exact witness: CONFIRMED**

**Full-locus theorem: CONFIRMED**

**Secondary positive argument: CONFIRMED** (emptiness / Nullstellensatz only; not a V19 cofactor certificate)

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-p0-total-rees-t-cs-drop-g14-witness-opus5-20260827.md` against frozen V18/V18R1 |
| Charged claim | An explicit rational point of the compiler ring kills all 21 charted grade-10--12 rows and the four localizers, leaves `Tg14_5 = -21/320`, and therefore proves `1` is not in `Prefix12+Localizers` over `Q` and over `F_65521` |
| Producer status | `EXACT_WITNESS`. SHA-256 `d9e5f43954240eee13311c5f386231f9ed506c4bbe978211cdfa711e3e8c86d9` |
| Reviewer / model | Grok 4.6 (xAI). Hostile different-model reread. Producer parsers, reduced-row displays, and AWS stdout were not trusted |
| Method | Independent sparse monomial parser on the frozen raw `.poly` files; monomial-level chart `rs -> cs*qrs`, `c0 -> cs*qc0`, `c1 -> cs*qc1`; exact `Fraction` substitution; coefficientwise reduction identity over `F_65521`; polynomial (not pointwise) forcing-chain and restriction identities. No Groebner basis, no heavy local CAS, no AWS mutation, no `jc2-lean`, no web |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-27 |

The displayed point is a genuine exact-`Q` zero of the frozen negative-control generators and a non-zero of the dropped row. One such point is logically sufficient to retire the preregistered `NoG14` standard-basis computation on both lanes. The two live V18R1 engines may be terminated for that computation without losing mathematical nonunit evidence, provided their partial logs are kept as aborted protocol artifacts and the jobs are not recorded as `PASS-T-CS-RHO-UNIT-V18R1`. This review does not harvest or certify the V18R1 positive.

---

## Narrow reusable theorem

Work in the ordinary polynomial ring of the frozen V18 compiler

```text
R = Q[u, v, a0, a1, aa0, aa1, aaa0, aaa1, ac3, ac4, az3, az4,
      cs, cs1, cs2, cs3, cs4, e0, e1, ec3, ec4, ee0, ee1,
      ell1, ell2, ell3, ell4, ez3, ez4, k, k1, k10_3, k10_4, k2c,
      qc0, qc1, qrs, rho, rs1, rs2, rs3, rs4]
```

(`42` variables; `expression_names` plus `u,v`). Let `E1..E21` be the frozen exact-Q V9 coefficients `Tg10_1..Tg12_7` after the word-boundary chart substitution, and let `Localizers = (qrs, rho, 1-u*cs, 1-v*k)`. Then:

1. The point with every variable `0` except

   ```text
   cs = 1,   e1 = 1,   k = 12/5,   u = 1,   v = 5/12
   ```

   satisfies `E1 = ... = E21 = 0` and `Localizers = 0`, and the frozen V17 row evaluates to `Tg14_5 = -21/320 ≠ 0`. Hence `1` is not in `I = (E1..E21)+Localizers` over `Q`.

2. The same assignment reduces modulo `65521` (`k ≡ 39315`, `v ≡ 38221`, `Tg14_5 ≡ 20680`) and is a zero of the frozen F65521 generators. Hence `1` is not in the reduced ideal over `F_65521`. Independently, every charted F65521 polynomial is the coefficientwise reduction of the corresponding exact-Q polynomial (all `22` pairs, as an identity of sparse polynomials, not a sample).

3. After `qrs = rho = qc0 = qc1 = e0 = a0 = ell1 = 0`, nineteen of the twenty-one prefix rows vanish identically, `Tg12_2` is exactly `3/32 e1^2 - 5/128 cs^4 k`, and `Tg12_1` is linear in `ell2` with coefficient `-5/16 cs^3 k`. On `D(cs*k)` this is an irreducible rational `31`-dimensional special fibre of `I`. Restricting the frozen `Tg14_5` to the five-zero slice already yields `-3/64 cs e1^2 - 1/128 cs^5 k`, which on the conic is `-(21/320) cs e1^2 = -(7/256) cs^5 k ≠ 0`. So `V(I + (Tg14_5))` is empty over `Qbar`, and `1` lies in the full V18 ideal over `Q` by the weak Nullstellensatz and faithful flatness. That is not an explicit membership matrix, and it does not discharge V19.

This licenses replacing the V18R1 `noG14Unit==0` computation by the point. It licenses nothing about Gate T, the remaining charts, source provenance of V9/V17, or a harvested V18R1 PASS.

---

## Verdicts

| Claim | Verdict | Reason |
|---|---|---|
| Exact witness (42-tuple, 21 rows, 4 localizers, `Tg14_5 = -21/320`, F65521 transfer) | **CONFIRMED** | Independent substitution from the frozen raw files |
| Full-locus theorem (forcing chain + rational 31-dimensional special fibre) | **CONFIRMED** | Polynomial identities after the chart, not point samples |
| Secondary positive (empty special fibre over `Qbar`, no V19 cofactors) | **CONFIRMED** | Restriction identity is exact; Nullstellensatz supplies `1` in the ideal and does not produce `U,L` |

---

## Process-stop

**Yes: the two currently running V18R1 engines may be terminated without losing mathematical evidence of the drop-grade-14 nonunit**, on both the exact-Q and F65521 lanes.

Conditions, all required:

1. Preserve every partial log (`*.stdout`, `*.stderr`, `launch_registration.txt`, compiler result, freeze checks) as aborted protocol artifacts. Do not delete host working directories.
2. Do **not** record those jobs as `PASS-T-CS-RHO-UNIT-V18R1`. The frozen validator still demands `V18_DROP_G14_NONUNIT=1` and three nonempty artifact writes, which an abort will not produce.
3. The frozen script is one Singular process: `Special=std(E+Localizers)` prints `V18_SPECIAL_FIBRE_UNIT=1`, then `NoG14=std(Prefix12+Localizers)`, then the three `write`s. This review did not fetch AWS stdout. Local campaign notes assert both positives already printed and both engines are in `NoG14`. Before killing a host process, confirm that host's existing stdout already contains `V18_SPECIAL_FIBRE_UNIT=1` if the campaign wants to keep those tokens. If a host has not printed the unit token, killing it loses the unreproduced positive computation.
4. Do not touch V19. V19 independently recomputes the positive and extracts the 26-generator lift; its compiler already deletes the `NoG14` tail.

Mathematical content of `noG14Unit==0` is replaced by the point. Protocol PASS of V18R1 is not. Artifact files `special.ideal`, `drop_g14.ideal`, and `charted_inputs.polys` will be missing; that is a harvest-format loss, not a loss of the nonunit theorem.

---

## 1. Custody and SHA pins

Independently recomputed. Both freeze files rehash with zero mismatches. Every V9 coefficient named in `COEFFICIENTS.json` rehashes. Both V17 `RESULT.json` contracts rehash, and both coefficient files match the pinned `coefficient_sha256` fields.

| Artifact | SHA-256 |
|---|---|
| `PREREGISTRATION.md` | `b07e8e7ca19b9a90618e875c22dd797380cdd315bd9eec3ab5744d2f7b01ed95` |
| `PREREGISTRATION_V18R1.md` | `02be2839a80706511e0a7be8e60220e0dad5b114c6c66d9004f55a2b4a2164b3` |
| `compile_t_cs_rho_unit_v18.py` | `50596db3a7009fa887e1679a8dbbc636afd68af66f923bfe13e7b5c3599548e6` |
| `compile_t_cs_rho_unit_v18r1.py` | `c23c67a7f6f3e3071f384db229fe3ab4ba5578e0166dead85177a6923ef08ef6` |
| `validate_t_cs_rho_unit_v18.py` | `e09adc5d4c5e7c629a3326f0deaff6b2dedc7f6a93b2f25ea5651e7f989091d7` |
| `validate_t_cs_rho_unit_v18r1.py` | `8b29e8f46084ab0f527959ee55c6460d24d45c883280c0f7f667b9210418a249` |
| `FREEZE.sha256` | `200b291f786319a858c5653dead6eed3962e5c057c0a1507665eface124f1c74` |
| `FREEZE_V18R1.sha256` | `6e1652b1a30600ea2949454be432e32157a9c71deb9365601d16dbb6812c9c77` |
| `run_aws.sh` | `43c5f0dfa012729c285d2b07b2a6fc5c096894c9613676de7facb8289d212117` |
| `run_aws_v18r1.sh` | `09d3d73e7a2bcd858f1d325992603e70b0f1bbba9ad3f54a1fe3f4f3706b9409` |
| `launch_host.sh` | `368ffe25490d1e5daa1e85efc046bfba3c0e75a7a78293134f417c0cf7fe36c0` |
| `launch_host_v18r1.sh` | `bde7a0b8dc86051fbfd1777dcf319ef1cc8048e924934496f4aaeeba963dc0f2` |
| `FAILCLOSED_V18_IDENTIFIER_COLLISION.md` | `a250a9ac4c193827f93bb24aa8055aa984f991c483c0ae7bf3a6286a8225344f` |
| V9 exact-Q `COEFFICIENTS.json` | `86c535a370adc2c7fb31b6ec8454128d765f581200a1730c506306d8bfa63c0e` |
| V9 F65521 `COEFFICIENTS.json` | `dc7757090bac53482ff674794e4e45cf33ff052d10c34f4e29a1de4133befde4` |
| V17 exact-Q `RESULT.json` | `25d40556618983a350eda99d4fb6aae8d1e5cd2cf328041963b46d61729af543` |
| V17 F65521 `RESULT.json` | `5ec8fece264a6076c5536f3c2cbb7d9d8f485316036e7e10adf0a7209e2ce166` |
| `Tg14_5_q.poly` | `91d96924696ab19a59cd8661fdd778559ce8dc9c1bc0fbc886dbdf4956e838f7` |
| `Tg14_5_p65521.poly` | `760d4f3b155decdf0e847a587254ae701f2b5948d8dd6135c52f5f213c10835b` |
| `ops/aws_exact_lane.sh` | `ebe06a100ae8f6bcdbdc580be89954d4cbc560c97cd75014153d61292415959b` |
| producer report | `d9e5f43954240eee13311c5f386231f9ed506c4bbe978211cdfa711e3e8c86d9` |
| odd-sheet promotion (corroboration only) | `f48401b5a5635fa8212db76ac0f9f7eea44e8904e0b1aa18a4fbbc38389d56c3` |
| V17 promotion (named, not used) | `2c7f624cc6556ae2b106d58065391263f6e0f0c26da45e537b736815d0b593aa` |
| ideation synthesis (scope only) | `ceea3b67169ab04d48f5ed96fa562b98d3b1a4e89eae7f4d94edc8d04c0aa412` |

Exact-Q V9 row files, matching the V9 manifest and the producer list:

```text
9a055c5343e43abef6017f82d7aa0f9405d2152227dbd8d3ac4a0e74bac02fec  Tg10_1.poly
50c88196628dc04407c47c49059849f7f43265ade03afa13c9f27eecc1f928a6  Tg10_2.poly
4913e736b6713433411dc1513e8813968bace256b80e6597367ea9917f8a8cda  Tg10_3.poly
6c33503e153a1adda56810a62db220f74b1dfd8c71158d1f3794f128773c503d  Tg10_4.poly
5c1d7ae3fb821011d5c65bbd2bf81389587bbf82c515a9be03b095dfe095a5ec  Tg10_5.poly
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  Tg10_6.poly
080d52ab67b2d5a28c8a8cc35e912b9e99d4be8a53bfb73d1d9bc6d70b20b440  Tg10_7.poly
11f6bd635957677cb8a0b29cedc847369d68d6b695e844efdf32f683078db469  Tg11_1.poly
fa9c5c109541478fc56a0a4c9564a80cbdd9aeaa2bd8a1c2eabfa5076afb1093  Tg11_2.poly
52e685581979a789b4aa72457d982f269d0f344530fd1fab8af541f2570f1650  Tg11_3.poly
d56bce83a56222c76169b259f55b452be61cb892b55d71d0d34abdcdda5ca050  Tg11_4.poly
ca08b238d9d592e5736a167981857a6af60af908b2402e4ff43633fa6fc71ef2  Tg11_5.poly
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  Tg11_6.poly
3c298d36d1353ae5b7ec7e0ce597d2a2ab85ef6fbfe7eebe086e761343e0b156  Tg11_7.poly
799ccff5e54711c53da6498ac01f8ac3fae2290600fd19664238cb49ed8d6e54  Tg12_1.poly
b66a3e858c41d22b4ce3f4592cdee28664e5ba677f138860f840565625b073e6  Tg12_2.poly
b0d090f9000f6e74bd214a0c443450114994c3fd61a0a577453f8c69acc42f87  Tg12_3.poly
091117b510011acf659038b94b3c872423d7b568cb28b04fb2cf9555fd4da327  Tg12_4.poly
9389b34abad72debf6e621bb0082c2882c3cfcc02cbdcd1a00d03cdff89bf1aa  Tg12_5.poly
d545fc9b104202d5e4db12fbd56433ba7fd714f13669e9a11536dc47c9137ebf  Tg12_6.poly
68b897df93e18da37a237bbdddab4776f947d37bdc2444f4d2e3ea043ee79f75  Tg12_7.poly
```

`Tg10_6.poly` and `Tg11_6.poly` are the literal two-byte file `0\n`. V18R1 pins the V18 compiler hash in source; that pin matches. V9 manifests are `PASS-T-RS0-EXACT-COEFFICIENT-EXPORT-V9` at characteristics `0` and `65521`. V17 results are `PASS-T-CS-ROW5-G14-EXPORT-V17` with `coefficient_term_count = 304` on the exact-Q side.

---

## 2. Independent substitution of the charged point

Parser: signed Singular terms, fractions in `a/b` or `(a/b)` form, integer F65521 coefficients, exponents `var^n`. Chart applied at monomial level (`rs^e` becomes `cs^e qrs^e`, likewise `c0,c1`), not by evaluating a producer-reduced display. Word-boundary regex substitution on the raw strings leaves no residual `\b(rs|c0|c1)\b`. Collecting identifiers from both charted exact-Q and charted F65521 polynomials, then adjoining `{qrs,qc0,qc1,rho,cs,k}` as the compiler does, yields exactly the `40` names above plus `u,v`. Forbidden identifiers `{ideal,poly,std,ring}` do not occur.

Sixteen names occur in `Tg14_5` and in none of the twenty-one prefix rows:

```text
ac3 ac4 az3 az4 cs3 cs4 ec3 ec4 ell3 ell4 ez3 ez4 k10_3 k10_4 rs3 rs4
```

They remain ring variables of the negative-control script and are assigned (`0`). Producer §8's "ten" is a count error; the assignment itself is complete.

Point, all `42` variables: every chart variable `0` except `cs=1`, `e1=1`, `k=12/5`, together with `u=1`, `v=5/12`.

Exact residuals, charted evaluation and raw evaluation at `rs=cs*qrs`, `c0=cs*qc0`, `c1=cs*qc1` (the two agree):

| row | residual | row | residual | row | residual |
|---|---|---|---|---|---|
| `Tg10_1` | `0` | `Tg11_1` | `0` | `Tg12_1` | `0` |
| `Tg10_2` | `0` | `Tg11_2` | `0` | `Tg12_2` | `0` |
| `Tg10_3` | `0` | `Tg11_3` | `0` | `Tg12_3` | `0` |
| `Tg10_4` | `0` | `Tg11_4` | `0` | `Tg12_4` | `0` |
| `Tg10_5` | `0` | `Tg11_5` | `0` | `Tg12_5` | `0` |
| `Tg10_6` | `0` | `Tg11_6` | `0` | `Tg12_6` | `0` |
| `Tg10_7` | `0` | `Tg11_7` | `0` | `Tg12_7` | `0` |
| `Tg14_5` | `-21/320` | | | | |

Localizers:

```text
qrs        = 0
rho        = 0
1 - u*cs   = 1 - 1*1           = 0
1 - v*k    = 1 - (5/12)*(12/5) = 0
cs = 1 ≠ 0,   k = 12/5 ≠ 0
```

The only surviving monomials of `Tg12_2` at this specialization are `-5/128 cs^4 k + 3/32 e1^2 = -5/128*(12/5) + 3/32 = 0`. All other prefix rows vanish monomial-wise. This is the charged witness.

The five-parameter family `cs=b`, `e1=b^2 w`, `k=(12/5)w^2`, `u=1/b`, `v=5/(12 w^2)`, remaining variables `0`, was evaluated at `(b,w) = (1,1), (1,-1), (2,3), (-3/5, 7/2), (5, 1/4)`: all `21` residuals `0`, and `Tg14_5 = -(21/320) b^5 w^2` exactly in each case (values `-21/320`, `-21/320`, `-189/10`, `250047/4000000`, `-13125/1024`).

---

## 3. F65521 transfer

`65521` is prime and `65521 ≡ 1 (mod 2,3,5)`, so `2,3,5,16,32,128,256,320` are units. Reducing the Q-point:

```text
k ≡ 12 * 5^{-1} ≡ 39315
v ≡ k^{-1}     ≡ 38221
-21/320        ≡ 20680
```

All `21` charted exact-Q rows reduce to `0` at this F65521-point; frozen F65521 files give the same `21` zeros and `Tg14_5 ≡ 20680`; localizers vanish.

Stronger than the producer's six random points: for each of the `22` keys, the charted F65521 polynomial equals the coefficientwise reduction of the charted exact-Q polynomial as sparse polynomials (zero mismatches). The same holds before the chart. The compiler's `FAIL_MODULAR_INPUT_*` comparison is therefore an identity, not a sample.

---

## 4. One Q-point replaces `NoG14` on both lanes

Preregistration: "Dropping `Tg14_5` must leave a nonunit ideal." The generated script is

```text
ideal NoG14 = std(Prefix12+Localizers);
int noG14Unit = (reduce(1,NoG14)==0);
if (noG14Unit!=0) { print("FAIL_DROP_G14_CONTROL_UNIT"); quit; }
```

If `1 ∈ I`, then `1 = sum a_i g_i`. Evaluating at the Q-point yields `1 = 0`. So the point is a complete proof that `noG14Unit` is `0` over `Q`, independent of term order and of Singular. Reducing the point proves the same over `F_65521`. Logically this substitutes for the standard-basis nonunit computation on both registered lanes.

It does not substitute for:

- the positive `Special=std(E+Localizers)` unit test,
- a harvested validator PASS (the validator token-set still includes `V18_DROP_G14_NONUNIT=1` and three artifact files),
- V19's `matrix(ONE)*LiftUnit - matrix(RawSpecial)*LiftCertificate = 0` with constant nonzero `LiftUnit[1,1]`.

Those remain separate. The producer drew this line correctly in §8 and §9.

---

## 5. Forcing chain and 31-dimensional fibre

After `qrs=rho=0`, the twenty-one charted rows are exactly the producer's §3.1 display (all `21` parsed equalities hold). In particular:

```text
Tg10_4 = (3/32) cs^2 qc0^2
Tg10_2 |_{qc0=0} = (3/32) cs^2 qc1^2
Tg12_4 |_{qc0=qc1=0} = (3/32) e0^2
```

Over a field with `cs ≠ 0` this forces `qc0=qc1=e0=0`. After those substitutions the identity

```text
Tg12_3 + (1/2) ell1 * Tg11_1  =  -(3/8) a0^2 cs
```

holds as polynomials, so `a0=0` on `D(cs)`. Then `Tg11_1 = -(5/16) cs^3 ell1 k`, so `ell1=0` on `D(cs*k)`. The inverted integers are `2,3,5` only; the same chain is valid in characteristic `65521`.

After the five zeros `{qc0,qc1,e0,a0,ell1}` together with `{qrs,rho}`, the prefix rows that remain are exactly two:

```text
Tg12_2 = (3/32) e1^2 - (5/128) cs^4 k
Tg12_1 = (3/8) a1 ee0 - (3/8) a1^2 cs + (3/8) aa0 e1
         + (15/256) cs k rs1^2 - (5/16) cs^3 ell2 k
```

The other nineteen are the zero polynomial, not merely zero at a point. `deg_ell2(Tg12_1)=1` with coefficient `-5/16 cs^3 k`, invertible on `D(cs*k)`. Solving for `ell2` and imposing the conic `12 e1^2 = 5 cs^4 k`, together with `u=1/cs`, `v=1/k`, leaves the `29` names

```text
a1 aa0 aa1 aaa0 aaa1 ac3 ac4 az3 az4 cs1 cs2 cs3 cs4
ec3 ec4 ee0 ee1 ell3 ell4 ez3 ez4 k1 k10_3 k10_4 k2c
rs1 rs2 rs3 rs4
```

free. Parametrizing the conic by `(cs,e1)=(b, b^2 w)` with `b w ≠ 0` gives an open in affine `31`-space, irreducible and rational over any field inverting `2,3,5`. Five randomized points on that locus (seed `20260827`, random rationals in all `29` free slots, `ell2` solved) give all `21` residuals `0` and `Tg14_5 = -(21/320) b^5 w^2`.

---

## 6. Secondary positive, firewalled

After the same five zeros, and before solving `ell2` or using the conic, the frozen `Tg14_5` is already

```text
Tg14_5 = -3/64 cs e1^2 - 1/128 cs^5 k
```

with no `ell2` and none of the `29` free variables. This is stronger than restricting to the full §6 locus: the dropped row is insensitive to those coordinates once the five zeros hold. On the conic the two-term polynomial is

```text
-(21/320) cs e1^2  =  -(7/256) cs^5 k.
```

On `D(cs*k)` one has `cs ≠ 0`, and the conic plus `k ≠ 0` forces `e1 ≠ 0`, so `Tg14_5 ≠ 0` at every point of the special fibre of `I`. Therefore `V(I+(Tg14_5))` is empty in `A^{42}` over `Qbar`. Weak Nullstellensatz gives `1` in the extended ideal; faithful flatness of `Qbar/Q` brings `1` back over `Q`. That is preregistration claim (1).

It exhibits no cofactors. Frozen V19 is exactly the explicit lift

```text
matrix(ONE)*LiftUnit - matrix(RawSpecial)*LiftCertificate = 0
```

with `ONE=ideal(1)`, `deg(LiftUnit[1,1])=0`, and `V19_RAW_GENERATOR_COUNT=26`. The emptiness argument does not produce those matrices and does not discharge V19. It also inherits the V9/V17 source-provenance dependency and adds no independent evidence about the Faber source.

This review did not read V18R1 engine output and does not confirm the provisional positive tokens.

---

## 7. Findings

### High

None that change the witness, the nonunit, the locus, or the emptiness statement.

### Medium

None that change a verdict. One count error belongs here only as documentation:

**M1. "Ten" G14-only names.** Producer §1 lists the G14-only identifiers correctly by family; §8 then says "the ten that enter the ring only through the dropped `Tg14_5`". There are sixteen (listed in §2 of this review). All sixteen are assigned `0`. No algebraic effect.

### Low

**L1. Zero-polynomial monomial census.** Producer §11 counts parsed monomials `4,5,5,2,5,1,5 | 12,14,17,3,18,1,18 | 27,36,47,12,58,9,60` and `304` for `Tg14_5`. Independent sparse counts of the charted files are the same except `Tg10_6` and `Tg11_6`, which are the empty polynomial (count `0`), not a `1`-term constant. Harmless display convention.

**L2. F65521 input comparison was sampled.** Producer §7 checked six random points of `F_65521^{40}`. The identity of all twenty-two reduced pairs holds as polynomials. The claim survives; the method was weaker than necessary.

**L3. Odd-sheet comparison is post-hoc.** The numerical agreement with the promoted odd-sheet theorem (`f48401b5...`) is real (`E_(5,14)=-(21/320)b^5 w^2`, controls `20680 mod 65521`, map `b↔cs`, `k0↔k`). It is not an input to the witness and is not required for any verdict here.

---

## 8. Scope firewall and smallest safe promotion

Promote, and only this:

> On the frozen V18/V18R1 ring and inputs, `1` is not in `(Tg10_1..Tg12_7, qrs, rho, 1-u*cs, 1-v*k)` over `Q` or over `F_65521`, because the displayed rational point (and its reduction) is a zero of every generator and a non-zero of `Tg14_5`. The preregistered drop-grade-14 standard-basis control is mathematically redundant on both lanes.

Do **not** promote:

- a harvested `PASS-T-CS-RHO-UNIT-V18R1` or any validator artifact set from the aborted jobs,
- V18R1's positive as a reviewed theorem (emptiness is a Nullstellensatz cross-check only),
- V19's explicit 26-generator certificate,
- independence from frozen V9/V17 bytes,
- the charts `T-c0`, `T-c1`, `T-a0`, `T-a1`, the `A` charts, overlaps, the terminal receiver, or `k=0`,
- Gate T, order two, the `(8,12)` frontier, maximum twelve, JC2, TD6, the prime ray, AS109, or any Lean statement.

`jc2-lean` was not accessed. No AWS state was mutated. No campaign computation was launched. The only repository file written is this review.

Original V18 outputs remain the fail-closed identifier-collision record (`FAILCLOSED_V18_IDENTIFIER_COLLISION.md`, SHA `a250a9ac...`) and must not be cited as a chart verdict.
