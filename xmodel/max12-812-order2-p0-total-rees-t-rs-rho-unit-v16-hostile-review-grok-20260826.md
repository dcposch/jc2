# Hostile review: T-rs grade-12 rho-unit certificate V16

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_p0_total_rees_t_rs_rho_unit_v16_20260826/` |
| Upstream pins | frozen V14, V13, V12 compilers; exact-Q V9 coefficient export |
| Charged claim | on the actual total-Rees T-rs chart `cs=rs*qcs, c0=rs*qc0, c1=rs*qc1`, the complete source prefix through grade 12, after saturation by `rs` and restriction to `D(k)`, forces `rho` to be a unit, with explicit inverse `-32*rho*qcs^2*(8*rho^2*qcs^2+3)` |
| Producer status | **ignored.** Printed `PASS` tokens, `RESULTS.md` prose, and F65521 agreement are not the characteristic-zero proof |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile reread and exact rederivation |
| Method | SHA-256 of every freeze line, harvested artifact, and V9 key; complete source reading of V16/V14/V13/V12/V15/V9; conceptual reverse-patch of the generated scripts; exact multivariate polynomial arithmetic over `Q` (Python stdlib fractions, no Singular/Sage/msolve); commutative-algebra check of saturation and localization encodings against the Singular 4.3.2 `std`/`sat`/`eliminate` signatures |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

The characteristic-zero lemma is a polynomial identity plus a saturation/localization implication over `Q`. Both were rederived here. Finite-field output is an encoding control only. Nothing larger than the T-rs chart on `D(k)` at the grade-12 prefix is claimed or accepted.

---

## 0. Custody and SHA pins

No `AGENTS.md` exists in or above the repository. Inspection was read-only except for writing this report. No local Singular, Sage, or Groebner engine was launched.

Independently recomputed SHA-256 of freeze-listed sources (every line of every charged `FREEZE.sha256` rehashed to the printed digest):

| Artifact | SHA-256 |
|---|---|
| V16 `FREEZE.sha256` | `ff208908297e52bd284dcf9e4ba869e4f169d242df3ed63f2fa232eacfffcd1a` |
| V16 `PREREGISTRATION.md` | `7c9f4d09beea1df620e8870c39c68222b305a6c3ae4c15f3493ab72b51318c32` |
| V16 `compile_rho_unit_v16.py` | `dad0f1e53eb4edb56de9b8a258a38cde0d8ea08004270071bb82adff40e2e62b` |
| V16 `validate_rho_unit_v16.py` | `8659199d1e0cfb7cd8864c31bc766aac018f427f9536a689f8a43423e678e70f` |
| V16 `run_aws.sh` | `a02b380709ec1ae11ad5becabfc1a7568bfa03fa403440bcfe9b3528925a84b6` |
| V16 `launch_host.sh` | `2d66200d51d14fa98cc4e77b9f225f5e99d4280c88977c35f02544fa0eb954e5` |
| V14 `FREEZE.sha256` | `d71ed1886c59447455bb67101b13690fd1219f770054982ec78be1a3ae044ed7` |
| V14 `PREREGISTRATION.md` | `efd1df057760c4ab0a1eea9ff6075e4f85558659ffdea5db3243d75ba902cc37` |
| V14 `compile_rho_unit_v14.py` | `809a1d660ee911eaad9c7e73f4f4202755776d79ece3f3d80a1e51630732460c` |
| V14 `validate_rho_unit_v14.py` | `554eb93706ee3d6b6ac78b83de85b249cf09ff25effc526bd60bee9dbb1c400a` |
| V13 `compile_rho_unit_v13.py` | `329bfb0fffcc3bf6587ac800afc577770100fb8e5cba5a2116503c24be396749` |
| V12 `compile_rho_unit_v12.py` | `9805bce184294bfdd3c81797192d9257e17865e4741d0df56bbbd334d6fdb2fd` |
| V12 `PREREGISTRATION.md` | `f6e741b8d135e1ebd3e6f22144045a13a8cad09c8a732ec5b3c4e4bda656e809` |
| V9 exact-Q `COEFFICIENTS.json` | `86c535a370adc2c7fb31b6ec8454128d765f581200a1730c506306d8bfa63c0e` |
| V9 F65521 `COEFFICIENTS.json` | `dc7757090bac53482ff674794e4e45cf33ff052d10c34f4e29a1de4133befde4` |
| V9 exact-Q `Tg10_1.poly` | `9a055c5343e43abef6017f82d7aa0f9405d2152227dbd8d3ac4a0e74bac02fec` |
| V9 exact-Q `Tg10_2.poly` | `50c88196628dc04407c47c49059849f7f43265ade03afa13c9f27eecc1f928a6` |
| V9 exact-Q `Tg10_3.poly` | `4913e736b6713433411dc1513e8813968bace256b80e6597367ea9917f8a8cda` |
| V9 exact-Q `Tg12_6.poly` | `d545fc9b104202d5e4db12fbd56433ba7fd714f13669e9a11536dc47c9137ebf` |

V16's literal `V14_COMPILER_SHA256` is the frozen V14 compiler. V14's literals `V12_COMPILER_SHA256` and `V13_COMPILER_SHA256` match the frozen V12/V13 compilers. V12's exact-Q and F65521 manifest pins match the V9 files above. Runtime hash chain:

```text
V16 FREEZE.sha256
  -> compile_rho_unit_v16.py
       -> V14_COMPILER_SHA256 -> V14 compiler
            -> V12_COMPILER_SHA256 -> V12 compiler
                 -> INPUTS[0] -> V9 exact-Q COEFFICIENTS.json
                      -> coefficient_sha256[key] -> Tg10_1, Tg10_2, Tg10_3, Tg12_6
            -> V13_COMPILER_SHA256 -> V13 compiler (custody hash only; compile_job is not executed)
```

`run_aws.sh` checks V16 `FREEZE.sha256` and V14 `FREEZE.sha256` from their package directories before compile. Both harvested lanes recorded `v16_freeze_check.stdout` and `v14_freeze_check.stdout` with five `OK` lines each. `launch_host.sh` ships V16, V14, V13, V12, V9, and `ops/aws_exact_lane.sh`. Those are exactly the files the hash chain reads. V15 is not in the tarball and is not imported.

Harvested result/script/stdout/stderr/artifact hashes independently recomputed against each lane's `EVIDENCE.sha256` and against `RESULTS.md`:

| Artifact | SHA-256 | Note |
|---|---|---|
| exact-Q `RESULT.json` | `f30365d06e64bd94fbea17c9b1d5a0ab4ee364d883c55bbeb71fb863d342a905` | matches RESULTS and EVIDENCE |
| F65521 `RESULT.json` | `8a9962dfe4e610e186c3d493faece07fc1db53260bfff256c5f32308988edbe3` | matches RESULTS and EVIDENCE |
| common `certificate.polys` | `890aede0abfef6fae6a574e44fa0883415cd8943b2b6d81905f65ff6374d9e28` | identical bytes in both lanes |
| common `special_dk.ideal` | `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b` | SHA-256 of ASCII `1` |
| exact-Q script | `74171d25364f6577b567bfa39e81aac10afa63f7581ee70bbbb1db5e34d51e9d` | |
| exact-Q stdout | `cf8f4a19ac755af076517166555a63ee7aebd400f4ba08f3f137f542cd3987ac` | |
| exact-Q resource stderr | `bc7e43bd5d8774789c17cc0bcbd615cd933c5b2fc01f3275b3f50cdc915b9a40` | Exit status 0, 0.03 s, 11484 KiB, 0 swap |
| exact-Q `jactual.ideal` | `598900a22c65f25b864621d6337d926a20007e222313e4e0fb23ba4854479f90` | 57 generators |
| exact-Q `dk.ideal` | `97ccdc67fa4f4974e8c421e27abc4b129e8fb1d7376093e8177989b0232adc59` | 67 generators |
| F65521 script | `5fec10670d096f113a25f0d40b5f371afc26c0e5139d7a482b91f7c723c2fffc` | |
| F65521 stdout | `b653ab472f90c65f09342958e06b8ee91d92520187b57a5e7c74f3f4a3b2e414` | |
| F65521 resource stderr | `bd3e5fa9aa54e3537b82f1cbb2b38ed1fa5fc484bc01fdabb31c22ca6d6fd39a` | Exit status 0, 0.02 s, 11804 KiB, 0 swap |

Every EVIDENCE line in both lanes matched the on-disk bytes. Compiler JSON in both lanes records the same V12/V13/V14/V16 source pins and `special_dk_repair_count=1`. Both launch registrations record source archive `5f9fe385066d1db5827f512b1732ef3493e6882bd3d88f61fd67456a76ad244a`, Singular 4.3.2 (4330), stamp `20260826T212522Z`. Exact-Q host `ip-172-30-0-186` (Box02); F65521 host `ip-172-30-0-45` (r6d).

**Custody gap, stated not used as a hole in the algebra.** The remote tarball itself is not present in the workspace, so the archive digest `5f9fe385…` cannot be recomputed here. `RESULTS.md` is post-harvest and is not freeze-listed. V12/V13/V9 `FREEZE.sha256` are not `sha256sum -c`'d by V16 `run_aws.sh`; they are pinned one hop down by compiler literals. That is a valid one-hop chain, the same pattern already accepted for other packages in this campaign. No source/harvest hash mismatch was found.

---

## 1. V16 versus frozen V14: one registered `SpecialDk` line

V16 `compile_job` imports frozen V14 `compile_job`, which itself imports frozen V12 `compile_job` and applies the three V13/V14 valuation repairs. V16 then does exactly two textual edits:

```text
ideal SpecialDk=std(J,rho,1-v*k);     -->  ideal SpecialDk=std(std(J,rho),1-v*k);
V14                                   -->  V16
```

The repair census requires the old `SpecialDk` line to occur once and the new line to be absent before the replace. Reverse-patching the harvested exact-Q script (`V16` back to `V14`, nested `std` back to the three-argument form) produces a unique preimage with no leftover V16 tokens and no leftover nested call. The F65521 script differs from the exact-Q script only by characteristic, the four `I_*` modular comparison lines, and the saturation-versus-elimination block; the `SpecialDk` line is the same nested call.

Singular 4.3.2 documents `std(ideal, poly)` as: take an already-computed standard basis and adjoin one extra generator. It also documents `std(ideal, bigintvec, intvec)` as Hilbert-driven `std`. Therefore:

- `std(J, rho)` is the standard basis of `J+(rho)`;
- `std(std(J,rho), 1-v*k)` is the standard basis of `(J+(rho))+(1-v*k) = J+(rho, 1-v*k)`;
- `std(J, rho, 1-v*k)` is the three-argument Hilbert-driven signature, which is **not** the ideal extension. That is the V15 failure, not a mathematical defect.

No coefficient, generator, term order, certificate, negative control, chart substitution, or saturation/elimination encoding changes. Both harvested scripts contain zero `qring` declarations, zero copies of the three-argument call, exactly one nested `SpecialDk` line, `P3=E_Tg10_3/rs` (not `/rs^2`), and three copies of `8192*qcs*P3` (not `8192*rs*qcs*P3`). The compiled filename still says `v12`; that is label debt from V12 `compile_job` and does not affect the algebra.

---

## 2. Trace of `Tg10_1, Tg10_2, Tg10_3, Tg12_6` to exact-Q V9

V12 `load_input(0)` is called unconditionally and supplies every `E_*` polynomial. The F65521 files are loaded only as `I_*` comparison inputs in the characteristic-65521 script. The exact-Q harvested script contains no `I_*` polynomials at all.

Exact-Q V9 files, verbatim:

```text
Tg10_1 = 5/16*rho^2*cs^3*k + 15/256*cs*rs^2*k + 3/8*a0*c1 + 3/8*a1*c0
Tg10_2 = 15/64*rho^2*cs^2*rs*k + 3/8*rho^2*a1*c1 + 5/1024*rs^3*k + 3/32*c1^2 + 3/8*a0*c0
Tg10_3 = 5/32*rho^4*cs^3*k + 15/512*rho^2*cs*rs^2*k + 3/16*rho^2*a0*c1 + 3/16*rho^2*a1*c0 + 3/16*c1*c0
Tg12_6 = 15/128*rho^4*cs^4*k + 45/1024*rho^2*cs^2*rs^2*k
       - 3/64*rho^2*rs*a1*c1 - 3/16*rho^2*cs*a0*c1 - 3/16*rho^2*cs*a1*c0
       + 15/32768*rs^4*k - 3/256*rs*c1^2 - 3/64*rs*a0*c0 - 3/64*cs*c1*c0
```

These are `Q`-rational. Every denominator is a power of two (maximum `2^15`). None of `32003`, `65521`, `1000033` divides any denominator. File hashes match the V9 exact-Q manifest pins, which match V12 `INPUTS[0]`. Chart substitution is a word-boundary replace `cs -> (rs*qcs)`, `c0 -> (rs*qc0)`, `c1 -> (rs*qc1)` with a residue check; the harvested `E_*` lines are exactly that substitution.

This review does not re-derive the V9 export from the total source family. It verifies that the characteristic-zero client consumes the pinned exact-Q files and no modular polynomial. Independently, the F65521 V9 files are the reduction of these same four `Q` polynomials modulo `65521` (every monomial coefficient matches); that comparison is a software control, not an input to the `E_*` identities.

---

## 3. Chart substitution and multiplication-back valuations

After the T-rs substitution, exact `rs`-adic valuations in `Q[rho,rs,qcs,qc0,qc1,a0,a1,k]` are:

| polynomial | `v_rs` | exact quotient | not exact |
|---|---:|---|---|
| `E_Tg10_1` | 1 | `/rs` | `/rs^2` |
| `E_Tg10_2` | 1 | `/rs` | `/rs^2` |
| `E_Tg10_3` | 1 | `/rs` | `/rs^2` |
| `E_Tg12_6` | 2 | `/rs^2` | `/rs^3` |

The obstruction to `rs^2 | E_Tg10_3` is the monomial `3/16 * rho^2 * rs * qc1 * a0` (and its `a1*qc0` twin). These are the chart images of `3/16*rho^2*a0*c1` and `3/16*rho^2*a1*c0`, each carrying a single factor of `rs`. Specializing `rho=0` would raise the valuation to 2; the **total** row does not. V12's `P3=E_Tg10_3/(rs^2)` is therefore false on the actual chart, which is why V12 stopped at multiplication-back.

Independent multiplication-back, as polynomial identities over `Q`:

```text
rs*P1     = E_Tg10_1
rs*P2     = E_Tg10_2
rs*P3     = E_Tg10_3
rs^2*P126 = E_Tg12_6
```

all hold, and `rs^2*P3 = E_Tg10_3` does not. The V16 script encodes the correct four checks. The residue of `P3` at `rs=0` is the nonzero polynomial `3/16*rho^2*qc1*a0 + 3/16*rho^2*qc0*a1`.

---

## 4. Four-term Delta, B decomposition, certificate, negative controls

All expansions below were performed independently over `Q` from the charted V9 polynomials. Producer tokens were not used.

Write

```text
V = 8*rho^2*qcs^2 + 3
U = 1 + 32*rho^2*qcs^2*V
  = 256*rho^4*qcs^4 + 96*rho^2*qcs^2 + 1
B = 5120*rho^2*rs^2*qcs^4*k + 2640*rs^2*qcs^2*k - 4608*qcs*(a0*qc1 + a1*qc0)
Delta = 32768*E_Tg12_6 - 35*k*rs^4 + 4096*rs*E_Tg10_2 + 8192*rs*qcs*E_Tg10_3
```

**Delta identity.** `Delta - rho^2*rs^2*B = 0` as a polynomial.

**B decomposition.** `B + 12288*qcs*P1 - 1120*rs^2*qcs^2*k*V = 0` as a polynomial. (Note `1120 = 35*32`.)

**Certificate.** Substituting the two identities and dividing the Delta relation by `rs^2` (legitimate because every term in Delta is visibly divisible by `rs^2` once the valuations of §3 are used) yields

```text
35*rs^2*k*U
  = 32768*P126 + 4096*P2 + 8192*qcs*P3 + 12288*rho^2*qcs*P1
```

The residual of this identity is the zero polynomial. The V12 multiplier `8192*rs*qcs*P3` with the repaired `P3=E_Tg10_3/rs` leaves a 10-term nonzero residual; that is the V12 formula error, not a present defect.

**Negative controls, expanded, not inferred from tokens.**

Dropping the `P1` term:

```text
35*rs^2*k*U - (32768*P126 + 4096*P2 + 8192*qcs*P3)
  = 3840*rho^4*rs^2*qcs^4*k + 720*rho^2*rs^2*qcs^2*k
    + 4608*rho^2*qcs*qc1*a0 + 4608*rho^2*qcs*qc0*a1
```

Replacing the `32` in `U` by `31`:

```text
35*rs^2*k*UWrong - (32768*P126 + 4096*P2 + 8192*qcs*P3 + 12288*rho^2*qcs*P1)
  = -280*rho^4*rs^2*qcs^4*k - 105*rho^2*rs^2*qcs^2*k
```

Both are nonzero as polynomials. Both match the harvested `certificate.polys` bytes exactly, as do `U`, `V`, `RhoInverse`, and the two zero residuals.

---

## 5. Saturation, localization, and the encodings

Let `E = (P1, P2, P3, P126)` in `Q[rho,rs,qcs,qc0,qc1,a0,a1,k]`. The certificate is the statement `35*rs^2*k*U ∈ E`. Saturation by `rs` is the colon ideal `J = E : rs^∞`. By definition of colon, `rs^2 · (35*k*U) ∈ E` puts `35*k*U ∈ J`. Over `Q`, `35` is a unit, so `k*U ∈ J`. In the localization at `k` (the open `D(k)`), `U` lies in the extended ideal `J · Q[…]_k`.

This implication does not require a Groebner basis. It is the definition of saturation plus the fact that `Q` is a field of characteristic zero.

**Exact-Q encoding, inspected not trusted.**

```text
list Sat = sat(std(E), ideal(rs));
ideal J  = std(Sat[1]);
```

No `qring`. Polynomial division is guarded by multiplication-back. `size(Sat)=1` on Singular 4.3.2 is the kernel `sat` returning an ideal, then coerced to a one-element list; `Sat[1]` is that saturated ideal. (The `elim.lib` documentation of a two-element list `(saturated ideal, exponent)` is not what this Singular build returned. The encoding still implements `J = std(sat(E,rs))`, not a first-generator truncation: harvested `jactual.ideal` has 57 generators and includes `k*U` itself.)

**Elimination encoding, F65521 lane only.**

```text
ideal Lift = E, 1-u*rs;
ideal J    = std(eliminate(std(Lift), u));
```

This is the Rabinowitsch trick for `E : rs^∞`. The ring is `(u,v, rho,rs,…,k)` with product order `(dp(2), dp(8))`, so `u` is in the first block. Only `u` is eliminated; `v` is reserved for inverting `k`. Harvested exact-Q `jactual.ideal` contains neither `u` nor `v`.

**`D(k)` encoding.** `ideal Dk = std(J, 1-v*k)` adjoins the extra generator `1-v*k` to an already-computed standard basis of `J`. Harvested exact-Q `dk.ideal` contains the generators `v*k-1` (the same principal ideal as `1-v*k`) and `U = 256*rho^4*qcs^4+96*rho^2*qcs^2+1` itself. That is the localization statement, written as a basis element, not a token.

**Harvested exact-Q `jactual.ideal` contains the generator**

```text
256*rho^4*qcs^4*k + 96*rho^2*qcs^2*k + k
```

which is exactly `k*U`. Combined with `35` being a unit in `Q`, this is independent artifact-level confirmation that `k*U ∈ J`, not a reading of `V16_SATURATED_KU_MEMBERSHIP=1`.

The four generators are a subset of the complete grade-12 prefix export. A subset relation goes the right way for a “forces rho to be a unit” claim: if `U` already lies in `sat(E,rs)` localized at `k`, it lies in any larger prefix ideal as well. V12 preregistration is explicit that the client consumes only these four files.

---

## 6. Explicit inverse, `J+(rho)` contains `k`, unit ideal

**Inverse identity, expanded over `Q`, no engine.**

```text
RhoInverse = -32*rho*qcs^2*V
           = -256*rho^3*qcs^4 - 96*rho*qcs^2

rho*RhoInverse - 1 = -32*rho^2*qcs^2*V - 1 = -U
```

the residual `rho*RhoInverse - 1 + U` is the zero polynomial. Therefore, once `U ∈ J_{D(k)}`, one has `rho * RhoInverse ≡ 1` in the quotient, i.e.

```text
rho^{-1} = -32*rho*qcs^2*(8*rho^2*qcs^2+3)    on this chart, on D(k).
```

**Special fibre, without Groebner.** `U ≡ 1 (mod rho)` as polynomials, because every non-constant term of `U` is divisible by `rho^2`. From `k*U ∈ J` one gets `k*U ∈ J+(rho)`, hence `k = k*U - k*(U-1) ∈ J+(rho)`.

**Unit ideal, without Groebner.** `J+(rho, 1-v*k)` contains both `k` and `1-v*k`, hence contains `1 = v·k + (1-v*k)`.

The sequential Singular call of §1 implements this same extension. Harvested `special_dk.ideal` in both lanes is the one-byte file `1`, whose SHA-256 is the well-known digest of ASCII `1`. That is the unit ideal as a written basis, not a banner. Exact-Q `dk.ideal` is 8985 bytes and is not the unit ideal, so the unit was not obtained by forgetting to adjoin `rho`.

---

## 7. Role of the F65521 elimination lane

The F65521 lane is an independent software/encoding control. It is not the characteristic-zero proof.

What it does check, and what this review independently rechecked:

- the same four exact-Q `E_*` polynomials, reduced in the ring `Z/65521`, agree coefficientwise with the V9 F65521 export (every monomial, independently);
- `35, 4096, 8192, 12288, 32768` remain nonzero in `F_65521`;
- the Rabinowitsch encoding of saturation, as opposed to `elim.lib` `sat`, also puts `35*k*U` in `J` and produces the unit ideal after adjoining `(rho, 1-v*k)`;
- `certificate.polys` is byte-identical to the exact-Q artifact, as required for a characteristic-independent polynomial identity.

What it does not do: it does not supply any polynomial that enters the `E_*` identities, and agreement modulo `65521` is not evidence over `Q`.

---

## 8. Fail-closed history V12–V15

None of the failed predecessors is evidence for the V16 lemma. V16 re-executes the certificate from frozen V12+V14 source plus the one-line `SpecialDk` repair.

| Version | Why it is not evidence |
|---|---|
| V12 | Both lanes stopped at `FAIL_MULTIPLICATION_BACK`. Preregistered `P3=Tg10_3/rs^2` and multiplier `8192*rs*qcs*P3`. The total-row valuation of `Tg10_3` is 1, not 2. Documented in `FAILCLOSED_MULTIPLICATION_BACK.md`. |
| V13 | Both lanes stopped in the compiler. The repaired multiplier occurs three times (certificate and two negative controls); V13's census expected two. Documented in `FAILCLOSED_REPAIR_CENSUS.md`. No algebra ran. |
| V14 | Mathematics of the three V13 substitutions with census 3, but `run_aws.sh` does `cd "$aws_root"; sha256sum -c "$package/FREEZE.sha256"` while V14 `FREEZE.sha256` lists bare filenames. The freeze check cannot succeed from the repository root. Stopped before compilation. |
| V15 | Deployment-only successor: frozen V14 compiler/validator, freeze check `cd`'d into each package directory. Tag is `…_v14_${stamp}_v15_${suffix}`, so V14 `require_aws` accepts it. Generated script still contains `std(J,rho,1-v*k)`. V15 has no local `aws_*` harvest in this workspace; it is not in the V16 tarball; V16 does not import it. Whatever V15 did or did not print is not used here. |

V16 is the first package that has (i) the correct `Tg10_3` valuation, (ii) the census-3 certificate repair, (iii) freeze checks from the package directory, and (iv) the two-argument nested `std` for `J+(rho,1-v*k)`.

---

## 9. Scope

The lemma that was actually proved, and the only lemma accepted, is:

> On the actual total-Rees T-rs chart `cs=rs*qcs`, `c0=rs*qc0`, `c1=rs*qc1`, let `E=(P1,P2,P3,P126)` be the four charted grade-10/12 rows `Tg10_1/rs`, `Tg10_2/rs`, `Tg10_3/rs`, `Tg12_6/rs^2` taken from the frozen exact-Q V9 prefix through grade 12, and let `J=E:rs^∞`. Then on `D(k)` one has `U ∈ J[1/k]` with `U=1+32*rho^2*qcs^2*(8*rho^2*qcs^2+3)`, hence `rho` is a unit with inverse `-32*rho*qcs^2*(8*rho^2*qcs^2+3)`. Equivalently `J+(rho)` contains `k` and `J+(rho,1-v*k)` is the unit ideal.

This is one standard chart, on `D(k)`, at the grade-12 truncation. It does not cover:

- the other total-Rees charts, including any specialized `rho=0` chart, `D_+(cs)`, or the secondary A fan;
- the locus `k=0`;
- global Gate T, the remaining chart obligations, or a comparison of saturation versus specialization at an earlier prefix;
- order two as a whole, maximum twelve, or JC2.

V12 preregistration's phrase “T-rs Gate-T obligation” is the chart-level reading of that obligation, not a global Gate-T theorem. V16 `RESULTS.md` already firewalled the larger claims. The compiled-script scope token is `T_RS_ACTUAL_CHART_DK_RHO_UNIT_PREFIX_ONLY`.

Upstream V9 correctness (that these four polynomials are the actual total-source coefficients) is a frozen pin, not re-proved in this package. If that pin were wrong, this lemma would be about the wrong rows. The pin was hash-checked; the rows were not re-extracted from the total family here.

---

## Independent algebraic skeleton

The characteristic-zero argument, with no engine and no finite field:

1. Chart-substitute the four exact-Q V9 polynomials. Valuations `(1,1,1,2)`.
2. `Delta = rho^2*rs^2*B` and `B = -12288*qcs*P1 + 1120*rs^2*qcs^2*k*V` as polynomial identities.
3. Therefore `35*rs^2*k*U ∈ E`, with `U=1+32*rho^2*qcs^2*V`.
4. Saturation by `rs` puts `35*k*U ∈ J`; over `Q`, `k*U ∈ J`.
5. On `D(k)`, `U ∈ J[1/k]`.
6. `rho*(-32*rho*qcs^2*V)-1 = -U`, so `rho` is a unit on this open.
7. `U ≡ 1 mod (rho)` gives `k ∈ J+(rho)` and then `1 ∈ J+(rho,1-v*k)`.

Steps 1–3 and 6 were expanded termwise. Steps 4, 5, 7 are commutative algebra, implemented by the inspected `sat` / `std(J,1-v*k)` / `std(std(J,rho),1-v*k)` encodings, and independently visible in the harvested exact-Q bases (`k*U` in `J`, `U` in `Dk`, `1` in `SpecialDk`).

VERDICT: CONFIRMED
