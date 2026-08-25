# Hostile different-model review — pointwise common-cubic obstruction at `3^12`

| Field | Value |
|---|---|
| Producer | `xmodel/as-b9-9-12-common-cubic-point-mod3p12-obstruction-producer-20260825.md` (SHA-256 `9dfbcf8823bc5b5fda4b367ecb07802dc45e405e66ac6457b8eab7585cbfa242`) |
| Frozen case | `cases/as_b9_9_12_common_cubic_mod3p12_tangent_gate_20260825/` |
| Consumed matrix | sibling SNF gzip `65eb73affe9e8217607650e932f0c71ae243949aac26703474045da5a6adebaf` (`cases/as_b9_9_12_common_cubic_witness_jacobian_snf_20260825/`) |
| Witness | SHA-256 `a39bc9185a21df92173b356c027a00650ced4b92cfc15d587a91b39c8aca299a` (byte-identical to the frozen `3^{11}` independent SAT witness) |
| Overall verdict | **CONFIRMED** |
| Mathematics | **CONFIRMED** |
| Source typing | **CONFIRMED** |
| Software | **CONFIRMED** (non-blocking notes below) |
| Custody | **CONFIRMED** of the frozen Box03 gate and r6d singleton replay, plus this review’s dual-host re-execution of both programs and of a source-independent 299-row reconstruction |
| Wording / scope | **CONFIRMED**. The one-witness firewall is load-bearing and is not over-read. No statement covers the `3^{150}` family |
| Mathematical defects | none |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Evidence | source audit of `mod3p12_gate.py`, `independent_singleton_replay.py`, and the sibling Jacobian compiler; independent SHA-256 of freeze/manifest/closure/witness/matrix/result/certificate; combinatorial slot index of `[x^2 y^2]`; AWS Box03 and r6d reconstruction of all 299 rows from bivariate `P,Q,H` by finite difference at `3^{11}`; independent F3 ranks/kernel/gauges/cokernel; expansion of all `C(149,2)=11026` mixed differences of the singleton coefficient; byte-comparison of producer gate/singleton payloads after dropping the job-tag field. No python-flint. No local execution of the producer gate or singleton replay |
| Git HEAD | `d0f6edfbfcd8fbe4c77ffadcd336df349c11eb7e` (producer and this case uncommitted) |
| Review window | 2026-08-25 |

## Verdict

**CONFIRMED**

At the one frozen normalized common-cubic witness modulo `3^{11}`, the complete 299-row next-digit system

```text
J(w) u = -F(w)/3^{11}  (mod 3)
```

in all 149 coefficient/core digits is inconsistent. Independently reconstructed ranks are

```text
rank J                    = 94
rank [J | -F/3^{11}]      = 95
kernel dimension          = 55
exact-gauge dimension     = 3
non-gauge kernel dimension= 52
left-cokernel dimension   = 205.
```

Row 12 of the displayed ordering is the determinant coefficient `[x^2 y^2]`. That row of `J` is the zero vector in `F_3^{149}`, while `F_{12}(w)/3^{11} ≡ 1 (mod 3)` and the linear right-hand side is `2`. No fresh digit repairs the row. Every bilinear fresh-fresh increment of this coefficient vanishes modulo `3^{12}`, and the pure `P`-`P`, `Q`-`Q`, and `H`-mixed increments vanish identically. This is one literal point. It is not an exclusion of the `3^{150}` family.

## Strongest exact claim

Fix the normalized common-cubic witness of SHA-256 `a39bc918…`, with

```text
H ≡ y^3 + 119880 x y^2 + 40581 x^2 y  (mod 177147)
```

and with `P`, `Q` the stored supports of total degree at most `(9,12)`. Write `F` for the 299 integer rows consisting of the 276 coefficients of `det J(P,Q)-1` in total degree `≤22` together with the 10 coefficients of `P9-P_{(0,9)} H^3` and the 13 coefficients of `Q12-Q_{(0,12)} H^4`. Then `F(w) ≡ 0 (mod 3^{11})` on every row, the displayed Jacobian over `F_3` has rank 94, and the divided carry `-F(w)/3^{11}` does not lie in the column space. Equivalently, the standard basis vector `e_{12}` is a left-cokernel vector pairing to `2`. The three target gauges (constant translation of `P`, constant translation of `Q`, and the shear `Q += tP`) span a 3-dimensional subspace of the 55-dimensional `F_3` kernel. This rules out a simultaneous lift of this one point to modulus `3^{12}` inside the 149-digit box.

## Sharpest non-claim

One witness, one digit. Not the complete displayed `3^{150}` mod-`3^{11}` common-cubic parameterization, not the normalized locus, not B9, not an all-depth / `Z_3` / characteristic-zero point, not a Q8 landing, not a maximum-twelve theorem, not a counterexample, and not JC2. The next required object is a carry on the whole finite family, not a pointwise restatement of this row.

---

## Evidence layers (do not collapse)

1. **Source-independent reconstruction (this review, AWS).** A bivariate compiler that never imports `mod3p12_gate.py`, `independent_singleton_replay.py`, or `jacobian_snf.py` rebuilt `F` from the frozen witness, finite-differenced every one of the 149 unit digits at step `3^{11}`, and ranked the system over `F_3`. Script SHA-256 `512b62f7706e3cd7ea1561f227400c1a75576b4bc069d228797a551f2cb0fc99`. Dual-host run `as_b9_common_cubic_mod3p12_review_grok_20260825T1825Z` on Box03 (`ip-172-30-0-249`) and r6d (`ip-172-30-0-45`). Wall 0.56s, max RSS 21.4 MiB, rc 0 on both hosts. Mathematical fields of the two result JSONs are identical; hostnames and job tags differ.

2. **Producer programs, second host each.** The frozen Box03 gate and r6d singleton were re-executed on both hosts from the same pinned sources. After deleting the job-tag field, both `result.json` objects are equal to the frozen payloads. The compressed kernel/cokernel certificate is byte-identical to the frozen gzip at SHA-256 `fad11a18d785c6520e477141f0f18094561a714cbc282e6ba9a5900e6d65a4e5` on both review hosts. This is custody that the audited sources replay, plus one independent algorithm for the ranks.

3. **Frozen hashes.** Independently recomputed SHA-256 of freeze, manifest, both SOURCE_CLOSURE files, both witness copies, both producer results, the certificate gzip, and the sibling matrix gzip all match the published values. The witness is byte-identical across this case, the sibling SNF case, and `cases/as_b9_9_12_common_cubic_3p11_20260825/INDEPENDENT_AUDIT_BOX02/independent_witness.json`.

---

## Charge 1 — 299 source rows and 149 fresh variables

**CONFIRMED**

Combinatorial counts, independent of any matrix file:

- monomials of total degree `≤9` number `10·11/2 = 55`;
- monomials of total degree `≤12` number `13·14/2 = 91`;
- three non-monic coefficients of monic `H = y^3 + h_1 x y^2 + h_2 x^2 y + h_3 x^3`;
- `55+91+3 = 149`;
- determinant ambient of total degree `≤22` numbers `23·24/2 = 276`;
- top forms are 10 coefficients of `H^3` plus 13 of `H^4`;
- `276+10+13 = 299`.

The gate asserts `len(rows_z)==len(residual_z)==299` and `len(row)==149`. The sibling Jacobian compiler that emitted the consumed matrix uses the same supports and the same 299-row layout, with labels `det`, then `P9`, then `Q12`. The independent reconstruction builds `H` as a bivariate cubic, computes `H^3` and `H^4` by bivariate multiplication (not the producer’s univariate convolution), and obtains a length-299 residual identical to the stored matrix residual. Every residual coordinate is divisible by `3^{11}`. The 149 finite-difference columns are exactly the 55 `P` coefficients, 91 `Q` coefficients, and 3 `H` digits.

The gate consumes a precomputed Jacobian rather than rebuilding `F`. That is not a hole in the claim: the independent reconstruction from the frozen witness reproduces the stored residual exactly and the stored Jacobian modulo 3 exactly.

## Charge 2 — ranks `94/95`, kernel 55, exact-gauge 3, non-gauge 52, cokernel 205

**CONFIRMED**

On both review hosts, independent `F_3` Gaussian elimination of the finite-difference matrix gives rank 94 and kernel 55. The augmented matrix `[J | -F/3^{11}]` has rank 95, so the system is inconsistent. The transpose has kernel 205. Rank-nullity `94+55=149` and `94+205=299` is tautological given those ranks.

The three target gauges are constructed from the witness, not from the stored kernel basis: the `P_{(0,0)}` unit vector, the `Q_{(0,0)}` unit vector, and the primitive `F_3` reduction of the shear `Q += tP`. They are linearly independent and lie in the independently reconstructed kernel, so the exact-gauge dimension is 3 and the non-gauge quotient has dimension `55-3=52`. The gate’s hard-coded `gauge_dimension: 3` is therefore the dimension of this explicit subspace, not an unexplained constant.

The frozen certificate decompressed at SHA-256 `4393ae8d0899d4a834777f4c3c215b656bc90b3a588627a0cbb2d164747b5c71` stores 55 kernel vectors of length 149, 205 left-cokernel vectors of length 299, and a length-205 projection with 31 nonzero coordinates. The first cokernel vector is the singleton `e_{12}`. The count 31 is a fact about this emitted basis, not a basis-free invariant; inconsistency follows already from the singleton pairing.

Producer Box03 stdout is `rank_aug_kernel_cokernel 94 95 55 205` with `non_gauge_kernel 52` and `consistent False`. Both review re-runs print the same four integers.

## Charge 3 — row 12 is determinant coefficient `[x^2 y^2]`

**CONFIRMED**

The slot order

```text
slots = [(i, d-i) for d in range(23) for i in range(d+1)]
```

has 1+2+3+4=10 monomials of total degree `≤3`, then degree 4 begins `(0,4)`, `(1,3)`, `(2,2)`. Hence `slots[12]=(2,2)`. The stored matrix label at index 12 is `["det", 2, 2]`. The independently rebuilt residual at index 12 equals the independently rebuilt coefficient of `x^2 y^2` in `P_x Q_y - P_y Q_x`, namely `-42740965278`. The producer’s identification does not depend on the Gaussian solver.

## Charge 4 — singleton certificate: fresh row zero, divided carry nonzero

**CONFIRMED**

Independently:

- `F_{12}(w) = -42740965278`;
- `F_{12}(w) ≡ 0 (mod 3^{11})` and `F_{12}(w) ≢ 0 (mod 3^{12})`;
- `(F_{12}(w)/3^{11}) ≡ 1 (mod 3)` in Python floor division;
- the linear right-hand side `(-F_{12}(w)/3^{11}) ≡ 2 (mod 3)`;
- every one of the 149 finite-difference columns vanishes in row 12 modulo 3;
- the stored integer row 12 is *not* the zero integer vector, but it is the zero vector in `F_3^{149}`;
- the first emitted left-cokernel vector is `e_{12}` with pairing 2.

The producer’s two statements “right-hand side 2” and “divided carry 1” are the same congruence, opposite sign. No choice of fresh digits in `F_3^{149}` can satisfy row 12.

## Charge 5 — independent 149-column replay; fresh-fresh terms vanish modulo `3^{12}`

**CONFIRMED**

The frozen r6d singleton at SHA-256 `f89426d35ff08561d14172b7b42203eb65e6b37402f6a39df37186ad1523cf72` rebuilds only `[x^2 y^2]` from the literal `P,Q`, never opens the Jacobian gzip, and records 146 coefficient effects all zero together with three source-zero `H` columns. Re-execution on Box03 and r6d matches that payload except for the job tag.

The producer’s own mixed-term check is the identity `(3^{11})^2 ≡ 0 (mod 3^{12})` together with bilinearity of the Jacobian determinant. That identity is tautological as written. This review expanded the actual bilinear remainder: all `C(149,2)=11026` mixed pairs of fresh digits, evaluated on `[x^2 y^2]`, vanish modulo `3^{12}`. In addition

- all `C(55,2)=1485` pure `P` mixed increments vanish identically,
- all `C(91,2)=4095` pure `Q` mixed increments vanish identically,
- all 441 mixed increments that involve an `H` digit vanish identically,
- the 5005 mixed `P`-`Q` increments are the genuine quadratic terms and still vanish modulo `3^{12}`.

`H` was actually perturbed in the independent reconstruction, both in the full 299-row residual and in the singleton coefficient. The producer’s “record H as source-zero” is correct for a determinant row and is not a missing column in the certificate.

## Charge 6 — platform guards, hashes, AWS custody

**CONFIRMED**

Platform guards fail closed:

- `run_aws.sh` refuses non-Linux, requires `AWS_JOB_TAG` matching `as_b9_common_cubic_mod3p12_*`, and requires the matrix/witness hashes and output paths;
- `mod3p12_gate.py` asserts Linux and a tag prefix `as_b9_common_cubic_mod3p12_`;
- `independent_singleton_replay.py` asserts Linux and a tag prefix `as_b9_common_cubic_mod3p12_replay_`.

Independently recomputed SHA-256:

| Object | SHA-256 |
|---|---|
| `mod3p12_gate.py` | `020ad0858e170c7b3e04242526106c9795c2abcf15cd7df9d28f32c2b1d7a8ed` |
| `independent_singleton_replay.py` | `8bf2f77e5d5f94aede2e00b56ca4da65db2a04dbf321df6b5ba9e160a4bf81a0` |
| `run_aws.sh` | `06f82656a3e94d9d2754cc2aa9f5343e14f08ad04b504f44330ec20e0937ebd7` |
| witness (all copies) | `a39bc9185a21df92173b356c027a00650ced4b92cfc15d587a91b39c8aca299a` |
| matrix gzip (SNF Box03 and r6d) | `65eb73affe9e8217607650e932f0c71ae243949aac26703474045da5a6adebaf` |
| matrix payload | `0202da0d68e4dd7cd6998751469f0d3d6ae6facc66bd18bc88d80fead8823f36` |
| Box03 `result.json` | `9f4964a1a1f4250561e64869466d2c168969107814c5a7d759023fc20db9e1e4` |
| r6d singleton `result.json` | `f89426d35ff08561d14172b7b42203eb65e6b37402f6a39df37186ad1523cf72` |
| certificate gzip | `fad11a18d785c6520e477141f0f18094561a714cbc282e6ba9a5900e6d65a4e5` |
| certificate uncompressed | `4393ae8d0899d4a834777f4c3c215b656bc90b3a588627a0cbb2d164747b5c71` |
| producer report | `9dfbcf8823bc5b5fda4b367ecb07802dc45e405e66ac6457b8eab7585cbfa242` |
| `MANIFEST.sha256` | `fdec8739d752a21f4e1c0a4df47aeb89daaf7475744b3282af44e85650f5aaf4` |
| `jacobian_snf.py` | `f8d1a0008fc7ccaec0ca1e4fde893f42df6105069a02b2fab01583755c192911` |

These are exactly the hashes in `FREEZE.sha256`, `MANIFEST.sha256`, both `SOURCE_CLOSURE.sha256` files, and both producer results. Frozen Box03 `/usr/bin/time -v` records elapsed `0:00.07`, max RSS 19,968 KiB, exit 0, matching the producer. Frozen r6d singleton records elapsed `0:00.03`, max RSS 15,820 KiB, exit 0. Review re-runs of the same two programs were 0.07s / ~19.9 MiB and 0.03s / ~15.8 MiB.

The original producer split is one host per program, not two hosts of one program. That is the correct independence layout (Gaussian gate versus literal-row replay). This review additionally ran both programs on both hosts. Frozen results do not record `hostname`; the review runs do (`ip-172-30-0-249` versus `ip-172-30-0-45`). The job-tag suffixes `_box03` / `_r6d` are producer labels and were not treated as host evidence.

The matrix gzip is pinned by Box03 `SOURCE_CLOSURE` and by `result.json`, and lives in the sibling SNF case freeze, but is not a path in this case’s `FREEZE.sha256`. Non-blocking packaging: the load-bearing reconstruction uses the witness, which is frozen here.

## Charge 7 — one-witness firewall; no coverage of the `3^{150}` family

**CONFIRMED**

The licensed claim is this one mod-`3^{11}` point. The producer states that the obstruction “excludes only this one literal mod-`3^{11}` witness” and “does not exclude the complete `3^{150}` family”. The case README, preregistration, gate `refusal_scope`, and singleton `refusal_scope` all refuse the complete family, B9, all-depth, maximum twelve, a counterexample, and JC2. The result `scope` is “one complete 299-row lift gate from mod3^11 to mod3^12”. Nothing in the machine payloads, the source, or the producer report promotes the pointwise `UNSAT` to a family theorem.

The `3^{150}` count itself is the already-reviewed `F_3`-digit parameterization of the mod-`3^{11}` common-cubic family over one B9 parent. Survival of that family to `3^{12}` is a different gate. This review does not reopen that count and does not extend this obstruction off the displayed witness.

---

## Non-blocking notes

- The producer singleton records the three `H` columns as source-zero rather than perturbing `H`. Correct for a determinant coefficient; this review perturbed them anyway.
- The producer mixed-term check is the degree identity `3^{22}≡0 (mod 3^{12})`, not an expansion. The expansion was performed here and agrees.
- `nonzero_rhs_cokernel_coordinates = 31` depends on the emitted left-cokernel basis. Inconsistency does not.
- `mod3p12_gate.py` imports unused `math`.
- This case freeze does not vendor `matrix.json.gz`; the sibling SNF freeze does. The witness plus the reconstruction above make the file unnecessary for the obstruction theorem.

No repairs are required. Verdict remains **CONFIRMED**.
