# Hostile review: `D43-NF-FID`

| Field | Value |
|---|---|
| Claim | `D43-NF-FID` (modular source-to-normal-form fidelity only) |
| Verdict | **CONFIRMED WITH GAPS** |
| Reviewer | Grok 4.6 (adversarial different-model verifier) |
| CLI | `grok 1.0.5 (5115b46bc909) [stable]` |
| Python | 3.14.6 (`/opt/homebrew/opt/python@3.14/bin/python3.14`) |
| Host | Darwin arm64, 2026-08-24 |
| UTC | 2026-08-24T01:36:37Z |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD at start | `d3c0edeb5fe4fe088124c9a512276e908a11c9d0` |
| Git HEAD at write | `8bf25a52f5f6c20886b77c6d9aeeb879eb18f8e4` (workspace moved under parallel work; banked D43 artifacts re-hashed unchanged) |
| Scratch | `/tmp/d43-nf-fid-ygpcsO` (fresh `mktemp -d`; banked files not overwritten) |

**Promotion.** The recovered 218-row census and the recorded canonical hashes at both primes may be promoted off producer-checked provisional. The 184-row `R_raw = R_NF + sum_j Q_j G_j` clause may be promoted only as modular fidelity corroborated by a spanning independent sample plus hashed producer output, not as a fully regenerated 24.8-million-term remainder. Nothing past modular source-to-D23-NF fidelity may be promoted.

**Quarantine if this review is treated as a failure.** Do not feed `D43-NF-FID` into a common integral 218-row model, an all-218 `p^2` lift, a standard-smooth / Stacks 02H6 certificate, a `Z_p` or characteristic-zero point, a compatible germ, or a polynomial Keller pair. Least-residue lifts of the prime-specific parked/NF coefficients remain an unverified model. Band-42 `Xf_alpha`/`Xg_beta` terms are assembled, not source-reduced. A timeout is not a mathematical failure; the fat-row remainder gap below is computational.

---

## Claim under review (not enlarged)

1. At `p=105337` and `p=105673`, fiber `a00pp`, the recovered `cases/d43red/` family is the stated 184-variable, 218-row modular presentation: 34 parked + 95 old graph (bands 6–24) + 89 late graph (bands 26–42), with the recorded canonical hashes.
2. At `p=105337`, all 184 pristine source rows independently replay as `R_raw = R_NF + sum_j Q_j G_j` over `F_p`, and the recomputed normal forms agree dictionary-exactly with the recovered checkpoints.
3. This is only modular source-to-normal-form fidelity. It does **not** establish a common integral presentation, all-row mod-`p^2` lift, flatness, standard smoothness, a characteristic-zero point, a compatible germ, or a polynomial Keller pair.

---

## Verdict table

| Clause | Verdict | What would have flipped it |
|---|---|---|
| 184 vars, 218 rows = 34+95+89 at both primes, fiber `a00pp` | **CONFIRMED** | eta set ≠ `S30`; silent empty `rung_kernel` row; parked ≠ 34; union ≠ 184 |
| Recorded canonical hashes at both primes | **CONFIRMED** (recovery audit rerun byte-identical to banked JSON) | parked/old/late/compat hash mismatch vs `sol-d43int.md` |
| Checkpoint schema / prime / band / fiber / `GBVARS` / no traces | **CONFIRMED** | extra payload keys; stale prime/fiber/band; trace fields present |
| `p=105337` source-to-NF identity, 184/184, dictionary-exact vs checkpoints | **CONFIRMED WITH GAPS** | independent remainder mismatch; group-key bijection failure; GB not 509 / not grevlex / wrong characteristic |
| Claim boundary (not integral, not all-218 `p^2`, not flat, not char-0, not Keller) | **HONEST** | hidden promotion of Hensel / Stacks 02H6 / common `Z_p` model |

---

## 1. What was rerun, independently, and not

Recovery audits, written only under the scratch directory:

```bash
python3 cases/d43_full_family.py --audit \
  --ckdir cases/d43red --root cases --prime 105337 \
  --out /tmp/d43-nf-fid-ygpcsO/recovery_audit_p105337.json
python3 cases/d43_full_family.py --audit \
  --ckdir cases/d43red --root cases --prime 105673 \
  --out /tmp/d43-nf-fid-ygpcsO/recovery_audit_p105673.json
```

Both printed `PASS 34+95+89=218`. SHA-256 of the rerun JSON equals the banked files:

| prime | SHA-256 of `cases/d43_integral_recovery_audit_p*.json` |
|---|---|
| 105337 | `9eb34da6bd409172553489650807956796f87751b153f91e4018669f35d6bce0` |
| 105673 | `a1cc85db21d4871a4a132590eac915b837f9d914498c125a9d608c091312c35f` |

Independent work, **not** `d43_nf_trace_replay.reconstruct` / packed `nf_trace`:

- Recomputed `S30` eta census and compared it to every checkpoint key.
- Parsed `directionb_det23_gb_p105337.out.txt` to exponent-tuple polynomials; verified 509 elements, monic printed leading terms, grevlex-max LTs, characteristic 105337, variable order = `GBVARS`.
- Evaluated all 509 `G_j` at the parked `a00pp` origin: **0/509 nonzero**. Independently `W1·uW1 ≡ 1` and `W2·uW2 ≡ 1` in `F_{105337}` at the derived witness `(W1,W2,uW1,uW2)=(31931,9457,64754,22756)`.
- Packed LT-divisibility reducedness probes on checkpoint NFs through band 24 (all groups) and samples of bands 26, 32, 42: **0 reducible terms**.
- Grouped the rebuilt Euler bank with a producer-matching classify (20 template/`W` names base; `uW1`/`uW2` **not** source-bank variables; PIN42 names absent from the bank).
- Tuple grevlex remainder + tuple reconstruct `NF + Σ Q_j G_j` on **2355** groups across **62** rows, including every group of bands 6–14 and the sparsest eta of every later band through 42: **0 mismatches** vs both the raw group and the checkpoint NF.
- Origin evaluation of **all 382824** groups of all **184** rows at that `V(G)` point: **0 failures**; group-key bijection **0 extra / 0 missing**; PIN42 drops **0**; max exponent **15** (no 8-bit packed overflow).

Limits that prevent full replay (not mathematical failures):

- `d43_nf_trace_replay.py` was **not** regenerated (banked run 1150.173 s, 3 workers). Input hashes of that JSON match the files on disk.
- `build_tails_modp.py` was **not** rebuilt (`--validate-points 0` would be a long Euler run). The rebuilt pickle was inspected and hashed.
- Independent remainder was **not** run on the fat late-band groups (band 42 eta 2 has 16414 groups). Origin evaluation at `FREE=0` is inconclusive for any group that vanishes there.
- No source-to-NF replay exists at `p=105673` (the claim does not ask for one).

---

## 2. Census, hashes, provenance

Independent `S30` sizes:

```
6:9, 8:10, 10:9, 12:9, 14:10, 16:10, 18:9, 20:10, 22:10, 24:9   → 95
26:10, 28:10, 30:9, 32:10, 34:10, 36:10, 38:10, 40:10, 42:10  → 89
```

At both primes, every checkpoint had exactly those etas, no cross-band keys, payload keys exactly `{band, fiber, gbvars, prime, rows}`, `fiber=a00pp`, matching prime/band, `GBVARS` the 22 det23 names, and **no** trace fields. Parked `d25fam_p*_a00pp.ms` files parse as 34 rows in the 28-name cell `FREE(14)+DEP(10)+FIXED(4)`. External graph names after `uf30` deletion: 156. Union: 184. `rung_kernel(...).get(h, {})` never saw a missing eta, so the silent-empty census bug is not live here.

Recorded hashes vs files vs rerun audit (all agree with `sol-d43int.md`):

| object | p=105337 | p=105673 |
|---|---|---|
| parked file | `ef6db7e9ad36666537475fabf8238887de0c7e6d8f02c9381eaa7c810cbe4fe2` | `43b81c4ea5f77a5d0d32f433a23e867e9ef4c7228f5d6e7624f43561aa976175` |
| old graph rows | `3cbb13d166529c043502ccc070692e610357c4dcab99ccf337b2296b41803651` | `d681bc8f36372cecadcb5cee6ffc95e8d4ef3657e0baf9c60196daa95da7c85f` |
| late graph rows | `43dc1d54e121e25fe03a6f95ab4666fc6d117c3835dc971c050af9209af15807` | `1f72d049b1ec50c64ffa22b1a15d47f7f9c664cb0e7c8bf52a67ee8654f94d3e` |
| late compatibility | `536e2c3fe5516ae51adeb456477d4546d4820eeb369db1e32290d9191f9af59a` | `60b20bee7fa418d22eb598638d91ae3446790470fd4bc3e2745c3efaf22c1205` |

Late graph and late-compat hashes byte-regress against `cases/d43_graph_emission_p*.json`. The old-graph hash is a **fresh** content hash of `serialize_grouped` on the current checkpoints; there is no frozen old-graph emission file. That is a weaker audit than the late-graph regression, already noted in the D43-full review. It is not a hash mismatch with the recorded claim.

Parked hashes are file hashes of `cases/d25fam_p*_a00pp.ms`, not of checkpoint pickles. The 218-row object is assembled: 34 parked rows from those `.ms` files plus `rung_kernel` of the 184 checkpoint graph rows. At band 42, `rung_kernel` **adjoins** constant `Xf_alpha`/`Xg_beta` terms (`P4P1` correction). Those names are **absent** from every checkpoint payload. The 184 source-to-NF traces therefore cover checkpoint NFs, not the assembled band-42 correction. This is an assembly step, not a census error.

`uf30` occurs in 6202 deep groups at each prime and is dropped from the serialized graph-row hashes and from the 156-name external census. PIN42 names do not appear in checkpoint deep keys and are absent from the rebuilt source-bank variable list.

Selected input hashes used by the banked `p=105337` trace replay (recomputed here, unchanged):

| artifact | SHA-256 | size |
|---|---|---|
| `cases/d43modp_p105337_a00pp_rebuilt.pkl` | `19a4f73ce8dd271406610fc2e716eea583e259ce6478abf8580b895a9ed4588a` | 909942294 |
| `cases/directionb_det23_gb_p105337.out.txt` | `3ba965d8d57439fce5e6febd6a3f7a3ab3bcad74337768eec18681bf0e2a2acc` | 15177980 |
| `cases/d43_nf_trace_p105337.json` | `2db9d8556b3c615c1d71536e7dc2c7128cf2fa7b613bef2ecfb816f93975f510` | 70265 |
| `cases/directionb_det23_gb_p105673.out.txt` | `cda3a0d61c6ab8973f3d6f4ec6b45abba0007514789323445200a948738e72de` | 15179068 |

`p=105673` GB header: characteristic 105673, same 22-variable grevlex order, length 509.

---

## 3. Source-to-NF identity, circularity, source vs parked

Producer path: `d43_reduce_modp.py` grouped the Euler bank and reduced with `d25_reduce.nf_trace` against a 509-element `gbcache` pickle. The banked replay `d43_nf_trace_replay.py` regroups the **rebuilt** Euler pickle, reduces with the same `nf_trace`, reconstructs `NF + Σ Q G` in packed 8-bit monomials, and compares NFs to checkpoints. That JSON reports:

```
184/184 membership, 184/184 checkpoint dictionary-exact,
raw 24882668, NF 38871970, quotient-trace 102883725,
aggregate 59f795b6489b3ecafa316bbf75a6d4bce318812fac868da479e047f7314170ed
```

Zero `FAIL` strings. Per-band row counts match `S30`. PIN42 drops 0. Inputs hash as above. The rebuilt bank is a 189-variable Euler source (`D=43`, fiber `a00pp`, 184 `(h,s)` cells), **not** a parked model and **not** a relabel of the checkpoints. `uW1`/`uW2` are GB coordinates, not source-bank variables.

Circularity that was actually tested:

| risk | result |
|---|---|
| Raw bank derived from checkpoints | Rejected: 189-var Euler pickle, 184 cells, group keys bijective with checkpoints |
| Replay tautological on producer `nf_trace` | Independent tuple grevlex remainder, first-matching LT in file order, tuple reconstruct; 2355/2355 groups match raw and checkpoint |
| Packed 8-bit exponent wrap | Independent max exponent 15 |
| Replay GB (`.out.txt`) ≠ producer `gbcache` | Sampled NFs agree, so they agree on those groups |
| `rung_kernel` counting empty etas | Eta sets exact |
| Traces establishing parked-generator membership | They do not; identity is modulo the 509 D23 reducers over `F_p` |
| Unique remainder in the quotient | Inherited from the parent D23 GB claim; this review only certifies this division |

The membership identity holds by the division algorithm even if `G` failed to be a Gröbner basis. Reducedness of sampled checkpoint NFs plus vanishing of all 509 `G_j` at the parked origin is additional evidence that the remainders are actually reduced, not a new GB certificate.

**Gap (why the verdict is not a plain CONFIRMED).** Independent dictionary remainder covers 62/184 rows (all of bands 6–14, plus one sparse eta per later band, including band 42 eta 29). The other 122 rows have group-key bijection, sampled reducedness, and origin agreement only. Origin agreement at `FREE=0` is the wrong strength for groups that vanish there (band 10 is independently dictionary-exact; fat late rows are not). The banked 184/184 producer replay was not regenerated into scratch.

That is a completeness gap in the independent remainder, not a counterexample.

---

## 4. Boundary (must not be enlarged)

Checkpoints contain only `band, fiber, gbvars, prime, rows`. No integral coefficients, no traces, no `p^2` data. The identity stops at the 509-element D23 basis over `F_p`. The 34 parked rows are the prime-specific `d25fam` modular files. None of the following is certified by this claim or this review:

- common integral / `Z_p` 34-row parked presentation from the source radical algebra
- membership of the 509 reducers in integral parked generators
- all-218 `F(x_1)/p` in one integral 184-coordinate ring
- local dimension 53, generation by the 131-row minor, `p`-flatness, standard smoothness, Stacks 02H6
- a `Z_p` point, a characteristic-zero D43 point, a compatible germ, a polynomial Keller pair

`sol-d43int.md` and `AUDIT.md` already state this. The local-fiber band-34 timeout is outside this claim; a timeout is not a nonzero remainder.

---

## 5. Downstream

Safe to consume: the recovered modular 218-row presentation at both primes, and modular source-to-D23-NF fidelity of the 184 graph rows at `p=105337` as producer-hashed plus independently sampled remainder.

Not safe to consume as a consequence: any integral re-emission, any Hensel/flatness/smoothness certificate, any characteristic-zero point, any algebraization-stage-2 close. Descendants that treat `D43-NF-FID` as an integral membership trace, as unique reduced remainders without the parent D23 GB, or as a license to lift displayed residues as ordinary integers, must stay quarantined.

---

## Artifact hashes (review scratch)

| file | note |
|---|---|
| `/tmp/d43-nf-fid-ygpcsO/recovery_audit_p105337.json` | byte-equal to banked audit |
| `/tmp/d43-nf-fid-ygpcsO/recovery_audit_p105673.json` | byte-equal to banked audit |
| `/tmp/d43-nf-fid-ygpcsO/independent_nf.json` | independent remainder / origin / reducedness report |
| `/tmp/d43-nf-fid-ygpcsO/fast_census.json` | schema / eta / stale-checkpoint census |

This file is the only repository write.
