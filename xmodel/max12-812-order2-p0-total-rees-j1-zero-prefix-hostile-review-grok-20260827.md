CONFIRMED

# Hostile review: exact `J1=0` specialization of the frozen total prefix

**Specialization census, `e1`-control, `A00`/`A10` zeros, first surviving grade 11: CONFIRMED**

**`a0`, `a1` not in the radical of the 22-row specialized ideal: CONFIRMED** (evaluation homomorphisms, not a radical computation)

**Standard `J2` charts of this prefix cannot be emptied by these rows: CONFIRMED**

**Terminal receiver `V(J1+J2)` of this prefix cannot be emptied by these rows: CONFIRMED as a fact, not as a corollary of `A00`/`A10`.** The origin/`rho`-line is the witness. See M1.

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-p0-total-rees-j1-zero-prefix-producer-sol-20260827.md` |
| Charged claim | Restrict the frozen 21 V9 exact-Q rows `Tg10_1..Tg12_7` and V17 exact-Q `Tg14_5` to `J1=(rs,cs,c0,c1)=0`; all seven grade-10 rows vanish; the five stage-one certificate rows vanish; twelve of twenty-two rows survive, first at grade 11; `Tg12_2` with only `e1` retained is `(3/32)e1^2`; `A00` and `A10` kill all 22 rows, hence `a0` and `a1` are not in the radical, hence this prefix cannot empty a standard `J2` chart or the terminal receiver |
| Producer status | `PASS — NAVIGATION ONLY.` SHA-256 `f9c8aab86af0f6c0ffd5c247a75b447bacb8723e172eec440806fd843c978e4b` |
| Reviewer / model | Grok 4.6 (xAI). Hostile different-model reread. Producer stdout, the restricted-AST replay, and AWS output were not trusted and were not executed |
| Method | Independent SHA-256 of the 22 frozen `.poly` bytes, preregistration, and replay file; recursive-descent parse of every character (word-boundary identifiers, `^`/`**`, exact `Fraction`); kill `rs,cs,c0,c1` by monomial support, not string replace; `Q[rho]` evaluation of `A00`, `A10`, and the origin; second sign-split term census. No `ast.parse`, no `eval`, no Groebner, no CAS, no AWS, no web, no `jc2-lean`, no execution of `replay_j1_zero_prefix.py` |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-27 |

The frozen bytes do what the producer says they do on `V(J1)`. The radical-nonmembership inference from the two unit points is valid over `Q` and does not need Nullstellensatz over an algebraic closure. The leap from those two points to the terminal receiver `V(J1+J2)` is not valid; the same bytes still make that receiver nonempty, by a third homomorphism the producer did not cite. Nothing here is a compiled Rees chart, a full source arc, or Gate T.

---

## Verdicts

| Claim | Verdict | Residual / reason |
|---|---|---|
| Preregistration SHA-256 | **CONFIRMED** | `3dae2b1786635de41f5e3501de7bb90bca08e491f21fb2975cfb53a911f2fabc` |
| Replay-file SHA-256 (bytes only; not executed) | **CONFIRMED** | `53ed677f8d60220480b37a87affd7958ce3c6cf59164ca373814e4993e7d1c60` |
| All 22 input SHA-256 pins | **CONFIRMED** | Independent `sha256` of the frozen exact-Q V9 `Tg*.poly` files and V17 `Tg14_5_q.poly`; match the previously reviewed V9 `COEFFICIENTS.json` / V17 `coefficient_sha256` |
| Restricted parse with exact `Q` | **CONFIRMED** | Recursive descent consumed every file; second census term counts `4,5,5,2,5,0,5,12,14,17,3,18,0,18,27,36,47,12,58,9,60,304` |
| `J1=(rs,cs,c0,c1)=0` by monomial kill | **CONFIRMED** | Identifiers `rs1..rs4`, `cs1..cs4` are distinct from `rs`,`cs`; no J1 name leaks into any specialized support |
| All seven grade-10 rows vanish | **CONFIRMED** | Specialized term count `0` on `Tg10_1..Tg10_7` |
| Five stage-one rows `Tg10_1..Tg10_4,Tg12_6` vanish | **CONFIRMED** | Subset of the previous line plus `Tg12_6=0`; also `Tg11_4=Tg11_6=0` |
| Surviving labels and first surviving grade | **CONFIRMED** | `Tg11_1,2,3,5,7` and `Tg12_1,2,3,4,5,7` and `Tg14_5`; 12 of 22; first grade `11` |
| Every survivor except `Tg12_4` has both `a0`- and `a1`-support | **CONFIRMED** | `Tg12_4` support is `{e0,e1,rho}` |
| `Tg12_2` with only `e1` retained is `(3/32)e1^2` | **CONFIRMED** | Unique `{e1}`-supported term in the 22 files |
| `A00` kills all 22 rows in `Q[rho]` | **CONFIRMED** | Residual `0`; no monomial supported in `{a0,rho}` |
| `A10` kills all 22 rows in `Q[rho]` | **CONFIRMED** | Residual `0`; no monomial supported in `{a1,rho}` |
| `a0 ∉ rad(I+J1)` from `A00` | **CONFIRMED** | Homomorphism to `Q[rho]` sending `a0↦1`; if `a0^N∈I+J1` then `1=0` |
| `a1 ∉ rad(I+J1)` from `A10` | **CONFIRMED** | Same with `a1↦1` |
| Standard `a0`-chart `D_+(a0)` of this prefix is nonempty | **CONFIRMED** | `A00` is a unit point of `a0` |
| Ordered `a1`-chart `V(a0)∩D_+(a1)` of this prefix is nonempty | **CONFIRMED** | `A10` has `(a0,a1)=(0,1)` |
| Terminal receiver `V(J1+J2)` nonempty *because* `A00`/`A10` | **NOT IMPLIED** | Those points have `a0=1` or `a1=1`, so they do not lie on `V(a0,a1)` |
| Terminal receiver of *this prefix* nonempty | **CONFIRMED** by a different witness | Origin/`rho`-line: all 22 rows vanish at `J1=a0=a1=0`, other names `0`, `rho` free |
| J2-chart emptiness search on these 22 rows is futile | **CONFIRMED** | The two standard charts of this prefix are nonempty |
| Whole covering emptiness search on these 22 rows is futile | **CONFIRMED** after adding the origin | Charts nonempty and `V(I,J1,J2)` nonempty for this prefix |
| Unexported grade-13 / other grade-14 / higher vanish on `V(J1)` | **GAP** | Not in the frozen prefix |
| A compiled `J2` Rees chart, including unwritten stage-two equations, is nonempty | **GAP** | Source-prefix sections only |
| Gate T, order two, maximum twelve, JC2 | **NONCLAIM** | Producer firewall is correct |

---

## Narrow reusable theorem

Work in the ordinary polynomial ring `R=Q[N]` on the 40 names occurring in the frozen bytes

```text
a0 a1 aa0 aa1 aaa0 aaa1 ac3 ac4 az3 az4
c0 c1 cs cs1 cs2 cs3 cs4
e0 e1 ec3 ec4 ee0 ee1 ell1 ell2 ell3 ell4 ez3 ez4
k k1 k10_3 k10_4 k2c rho
rs rs1 rs2 rs3 rs4
```

Let `Tg10_1,...,Tg12_7` be the frozen exact-Q V9 files and `Tg14_5` the frozen exact-Q V17 file (byte hashes below). Let `I` be the ideal they generate and `J1=(rs,cs,c0,c1)`. Chart names do not occur in the files. Then:

1. **Specialization.** The images of all seven grade-10 rows in `R/J1` are `0`. So are `Tg11_4`, `Tg11_6`, and `Tg12_6`. The other twelve rows remain nonzero. The first surviving grade is 11. Explicit specialized polynomials are recorded in the telemetry. In particular

   ```text
   Tg12_4 |_{J1=0} = (3/32) e0^2 + (3/32) rho^2 e1^2,
   Tg12_2 |_{all names except e1 = 0} = (3/32) e1^2.
   ```

   Every surviving row except `Tg12_4` has both `a0` and `a1` in its specialized support.

2. **Unit points.** The `Q[rho]`-algebra map `φ_00: R→Q[rho]` sending `a0↦1`, every other name except `rho` to `0`, and `rho↦rho`, kills `I`. The map `φ_10` with `a1↦1` likewise kills `I`. Both factor through `R/(I+J1)`. Hence `a0` and `a1` are units in the respective images, so neither is nilpotent in `R/(I+J1)`: `a0,a1∉rad(I+J1)`. Equivalently, `D_+(a0)` of this prefix is nonempty, and `V(a0)∩D_+(a1)` is nonempty. The `a0`-chart bilinear `a1-a0·qa1` holds at `(a0,qa1)=(1,0)`; the ordered `a1`-chart bilinear `a0-a1·qa0` holds at `(a0,a1,qa0)=(0,1,0)`.

3. **Terminal of this prefix.** The further map `φ_0: R→Q[rho]` sending `a0`,`a1`, and every other name except `rho` to `0` also kills `I`. So `R/(I+J1+(a0,a1))` admits `Q[rho]` as a quotient, and the terminal receiver `V(I+J1+J2)` of *these 22 rows* is nonempty. This is not a consequence of (2): a pair of points with `a0=1` or `a1=1` cannot witness `V(a0,a1)`.

Consequently: a search for emptiness of either standard `J2` chart, or of the terminal receiver, that uses only these 22 specialized rows is deciding a false statement about this prefix. The statement is about the exported source prefix on `V(J1)`, not about a compiled Rees chart and not about unexported source.

---

## 1. Custody and SHA pins

Independently recomputed this session. Producer pins for the preregistration and replay file match the on-disk bytes. The replay was hashed and read as text; it was not executed. Every V9 exact-Q `Tg*.poly` named in `COEFFICIENTS.json` rehashes. V17 `Tg14_5_q.poly` rehashes to the previously reviewed `coefficient_sha256`.

| Artifact | SHA-256 |
|---|---|
| producer report | `f9c8aab86af0f6c0ffd5c247a75b447bacb8723e172eec440806fd843c978e4b` |
| preregistration | `3dae2b1786635de41f5e3501de7bb90bca08e491f21fb2975cfb53a911f2fabc` |
| replay script (hashed; not executed) | `53ed677f8d60220480b37a87affd7958ce3c6cf59164ca373814e4993e7d1c60` |
| V9 exact-Q `COEFFICIENTS.json` | `86c535a370adc2c7fb31b6ec8454128d765f581200a1730c506306d8bfa63c0e` |
| V9 `FREEZE.sha256` | `ee87f8b94eb0d3bd87d58f1c8fd1cf9993caa013b7bfea7a319f0c260a7c24d7` |
| V9 `PREREGISTRATION.md` | `c0bdfe2f631c93c5a132846d81321b507571b419480bf7afd3ff5c9e60d5a5fb` |
| V17 exact-Q `RESULT.json` | `25d40556618983a350eda99d4fb6aae8d1e5cd2cf328041963b46d61729af543` |
| V17 `FREEZE.sha256` | `95f8c3a7961defb7daf779b5ee69d977a940b51f2b1ce983388c108e8d525933` |
| `Tg14_5_q.poly` | `91d96924696ab19a59cd8661fdd778559ce8dc9c1bc0fbc886dbdf4956e838f7` |
| sibling zero-section producer (named, not re-trusted) | `0ca4647acecbff0181478c98cbbec15c932beeba0a106df1d085958aaebf3fb0` |
| sibling zero-section hostile review (corroboration of `Q[rho]` zeros only) | `959603e311fb02254488c57c49edc1b79837dc72987d3b9253c8c176eebb1623` |

Exact-Q V9 row files:

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

`Tg10_6.poly` and `Tg11_6.poly` are the literal two-byte file `0\n` and share hash `9a271f2a…`. Paths: V9 `aws_q_v9/compiled/`, V17 `aws_q/compiled/Tg14_5_q.poly`. The F65521 copies in `aws_p65521_v9/` were not consumed.

---

## 2. Independent parser and `J1=0` census

Parser: recursive descent on the raw bytes. Tokens are identifiers `[A-Za-z_][A-Za-z0-9_]*`, decimal integers, `+ - * / ^ ** ( )`. Coefficients live in `fractions.Fraction`. A monomial is a sorted exponent vector. Division is licensed only by a nonzero scalar. No Python `ast`, no `eval`, no producer `Poly` class. Every character of every file was consumed. A second census, splitting on signed terms after masking parenthesized coefficients, agrees on all 22 files, empty polynomial counted as `0` terms.

Unspecialized sparse term counts:

```text
4,5,5,2,5,0,5 | 12,14,17,3,18,0,18 | 27,36,47,12,58,9,60 | 304
```

Forbidden names `{ideal,poly,std,ring,eval,exec}` do not occur. Prefix identifiers `{rs1,rs2,rs3,rs4,cs1,...}` were never rewritten as `rs` or `cs`.

Specialization is deletion of every monomial whose support meets `{rs,cs,c0,c1}`. Empty specialized polynomials have canonical digest SHA-256 of the empty byte string `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

Independent canonical form: one line per term `monomial<TAB>numerator<TAB>denominator`, monomial written `var` or `var^n`, terms sorted. A second digest uses the replay's documented monomial-tuple layout `('e1','e1')` reconstructed from this parse, not from executing the replay.

| row | grade | spec terms | deg | variables | zero | a0 | a1 | canonical SHA-256 | tuple-layout SHA-256 |
|---|---|---|---|---|---|---|---|---|---|
| `Tg10_1` | 10 | 0 | −1 | — | yes | no | no | `e3b0c442…852b855` | same |
| `Tg10_2` | 10 | 0 | −1 | — | yes | no | no | `e3b0c442…` | same |
| `Tg10_3` | 10 | 0 | −1 | — | yes | no | no | `e3b0c442…` | same |
| `Tg10_4` | 10 | 0 | −1 | — | yes | no | no | `e3b0c442…` | same |
| `Tg10_5` | 10 | 0 | −1 | — | yes | no | no | `e3b0c442…` | same |
| `Tg10_6` | 10 | 0 | −1 | — | yes | no | no | `e3b0c442…` | same |
| `Tg10_7` | 10 | 0 | −1 | — | yes | no | no | `e3b0c442…` | same |
| `Tg11_1` | 11 | 2 | 2 | `a0,a1,e0,e1` | no | yes | yes | `bfe9816bebfa26bdfdc364453f773737b95a022aa93ddf1e9e6da10eafc59b0b` | `c066536b46e15e63cb88f9bc7f60747a56ec967905f8ea201ce67305f93122fd` |
| `Tg11_2` | 11 | 2 | 4 | `a0,a1,e0,e1,rho` | no | yes | yes | `c84fafac1ed9c6855acd066e0e2edfee914034b894f72f4a0e2b7f0493e5f35a` | `5364385ef144d1e10a1ff609b38bda1a7697f662abf11cdd1a80f3da27bc75ae` |
| `Tg11_3` | 11 | 2 | 4 | `a0,a1,e0,e1,rho` | no | yes | yes | `2833289f0a2f194d2192cac47df6305a67b5fab3b7e146110681c357c8498a96` | `fd3ef9b721f335df70684eeaf692b1c0fdbac951d8e6c63e1f5313740add16c3` |
| `Tg11_4` | 11 | 0 | −1 | — | yes | no | no | `e3b0c442…` | same |
| `Tg11_5` | 11 | 2 | 6 | `a0,a1,e0,e1,rho` | no | yes | yes | `b2b0db41a20f291901cfda9bd3cb4d400c9d95d619a04a6f0b40292efe208ab1` | `336137af79662299461701e75b2c5a98a3dfa02c897984ad886b2fe550a6786b` |
| `Tg11_6` | 11 | 0 | −1 | — | yes | no | no | `e3b0c442…` | same |
| `Tg11_7` | 11 | 2 | 8 | `a0,a1,e0,e1,rho` | no | yes | yes | `9c2bd89892dbbd900b5b75fe7e0df9f5e6cd80663b4bc3d6444a38c900bdc3ac` | `9ac1bc1e8ef2e80efea39a2441d5b15468dd6c847cd2b9c2539b0f8e990a0a45` |
| `Tg12_1` | 12 | 4 | 2 | `a0,a1,aa0,aa1,e0,e1,ee0,ee1` | no | yes | yes | `139b05a65c3552036fdcbe8f9ca78d507c26998a97692a1a6fe92cfee54dae52` | `f7c5261c4b380180ee4729e186fb8574aac8a47590c0a30a353086484a974845` |
| `Tg12_2` | 12 | 6 | 4 | `a0,a1,aa0,aa1,e0,e1,ee0,ee1,ell1,rho` | no | yes | yes | `1c23ec1b8cb1e0cfcdd18bbeea9d5b7b850f572c28105109438535bc0f5871dc` | `d4b53832f5f4a5f5ef257f6e2ece7a6ef222635f6ddf50ba9faaed9147c74b3c` |
| `Tg12_3` | 12 | 7 | 4 | `a0,a1,aa0,aa1,e0,e1,ee0,ee1,ell1,rho` | no | yes | yes | `7fe44012b8534b75d9ee7b8deb078682e6b1a69311ecb450a505711ca8d28393` | `d38eb266cb20799535ad71bf112626dd8a56cf6db5c5c6303ee115f896c1b05e` |
| `Tg12_4` | 12 | 2 | 4 | `e0,e1,rho` | no | no | no | `9f9a38a11181016d1e111be33c0658d6eef87386dc2641132fc84de42222d2c9` | `f8cc09360d2694898c95599986e23f7a5430ff2c41e4924eeae5e05340389aea` |
| `Tg12_5` | 12 | 7 | 6 | `a0,a1,aa0,aa1,e0,e1,ee0,ee1,ell1,rho` | no | yes | yes | `9b41192188a50c3e4701d51e9d1470563c9927e388a028697bb3d136055baffd` | `3c7d4395f123bf7312be3a509c7544ae2f039b819744938919d7c2e8af5f2041` |
| `Tg12_6` | 12 | 0 | −1 | — | yes | no | no | `e3b0c442…` | same |
| `Tg12_7` | 12 | 7 | 8 | `a0,a1,aa0,aa1,e0,e1,ee0,ee1,ell1,rho` | no | yes | yes | `525e5a688f2af49674b8713731db4beba099c319d4493b9ff53e4fc757840305` | `ee8ffccc43bced1784393bd9d8be8c3d973b00f7c5808482947607d929a551cc` |
| `Tg14_5` | 14 | 62 | 10 | `a0,a1,aa0,aa1,aaa0,aaa1,ac3,az3,cs1,cs2,e0,e1,ec3,ec4,ee0,ee1,ell1,ell2,ell3,ez3,ez4,k,k1,rho,rs1,rs2` | no | yes | yes | `cf99756863e9c383543543a83340390cb2f91216f9c79c0784d311b19f1cc804` | `8d04d3452da1409ba90033c79c7c64c7cfe3c489852a7864f564bc500989af48` |

Surviving labels: `Tg11_1,Tg11_2,Tg11_3,Tg11_5,Tg11_7,Tg12_1,Tg12_2,Tg12_3,Tg12_4,Tg12_5,Tg12_7,Tg14_5`. First surviving grade: 11. Actual specialized names (26):

```text
a0 a1 aa0 aa1 aaa0 aaa1 ac3 az3 cs1 cs2
e0 e1 ec3 ec4 ee0 ee1 ell1 ell2 ell3 ez3 ez4
k k1 rho rs1 rs2
```

Ten source names occur only inside monomials that also carry a J1 factor, so they die with the specialization and are *not* specialized support: `ac4,az4,cs3,cs4,ell4,k10_3,k10_4,k2c,rs3,rs4`.

Explicit specialized polynomials, all coefficients in `Q`:

```text
Tg11_1 = (3/8) a0 e1 + (3/8) a1 e0
Tg11_2 = (3/8) a0 e0 + (3/8) a1 e1 rho^2
Tg11_3 = (3/16) a0 e1 rho^2 + (3/16) a1 e0 rho^2
Tg11_5 = -(3/64) a0 e1 rho^4 - (3/64) a1 e0 rho^4
Tg11_7 = (3/128) a0 e1 rho^6 + (3/128) a1 e0 rho^6
Tg12_1 = (3/8) a0 ee1 + (3/8) a1 ee0 + (3/8) aa0 e1 + (3/8) aa1 e0
Tg12_2 = (3/8) a0 ee0 - (3/8) a1 e1 ell1 + (3/8) a1 ee1 rho^2
         + (3/8) aa0 e0 + (3/8) aa1 e1 rho^2 + (3/32) e1^2
Tg12_3 = -(3/16) a0 e1 ell1 + (3/16) a0 ee1 rho^2
         - (3/16) a1 e0 ell1 + (3/16) a1 ee0 rho^2
         + (3/16) aa0 e1 rho^2 + (3/16) aa1 e0 rho^2 + (3/16) e0 e1
Tg12_4 = (3/32) e0^2 + (3/32) rho^2 e1^2
Tg12_5 = (3/32) a0 e1 ell1 rho^2 - (3/64) a0 ee1 rho^4
         + (3/32) a1 e0 ell1 rho^2 - (3/64) a1 ee0 rho^4
         - (3/64) aa0 e1 rho^4 - (3/64) aa1 e0 rho^4 + (3/32) e0 e1 rho^2
Tg12_7 = -(9/128) a0 e1 ell1 rho^4 + (3/128) a0 ee1 rho^6
         - (9/128) a1 e0 ell1 rho^4 + (3/128) a1 ee0 rho^6
         + (3/128) aa0 e1 rho^6 + (3/128) aa1 e0 rho^6 - (3/128) e0 e1 rho^4
Tg14_5 = (62 terms; digest cf997568… / 8d04d345…)
         (3/32) a0 a1 ell1 rs1 + (-5/128) a0 a1 k rho^4 + (-3/32) a0 a1 rho^2 rs2
         + (-3/8) a0 aa0 cs1 rho^2 + (-3/32) a0 aa1 rho^2 rs1 + (-3/16) a0 cs1 e0
         + (-3/32) a0 e1 ell1 ell2 + (3/32) a0 e1 ell3 rho^2 + (-9/128) a0 e1 rs1
         + (-3/64) a0 ee1 ell1^2 + (3/32) a0 ee1 ell2 rho^2 + (3/32) a0 ell1 ez3 rho^2
         + (-3/64) a0 ez4 rho^4 + (3/16) a0^2 cs1 ell1 + (-3/16) a0^2 cs2 rho^2
         + (-3/32) a1 aa0 rho^2 rs1 + (-9/32) a1 aa1 cs1 rho^4 + (-3/8) a1 cs1 e1 rho^2
         + (-3/32) a1 e0 ell1 ell2 + (3/32) a1 e0 ell3 rho^2 + (-9/128) a1 e0 rs1
         + (3/32) a1 ec3 ell1 rho^2 + (-3/64) a1 ec4 rho^4 + (-3/64) a1 ee0 ell1^2
         + (3/32) a1 ee0 ell2 rho^2 + (9/32) a1^2 cs1 ell1 rho^2 + (-9/64) a1^2 cs2 rho^4
         + (-3/64) aa0 e1 ell1^2 + (3/32) aa0 e1 ell2 rho^2 + (3/32) aa0 ee1 ell1 rho^2
         + (-3/64) aa0 ez3 rho^4 + (-3/64) aa1 e0 ell1^2 + (3/32) aa1 e0 ell2 rho^2
         + (-3/64) aa1 ec3 rho^4 + (3/32) aa1 ee0 ell1 rho^2 + (3/32) aaa0 e1 ell1 rho^2
         + (-3/64) aaa0 ee1 rho^4 + (3/32) aaa1 e0 ell1 rho^2 + (-3/64) aaa1 ee0 rho^4
         + (-3/64) ac3 e1 rho^4 + (-3/64) az3 e0 rho^4 + (5/64) cs1 e0 ell1 k rho^2
         + (-5/128) cs1 e0 k1 rho^4 + (-5/128) cs1 ee0 k rho^4 + (15/1024) cs1 ell1 k rho^2 rs1^2
         + (-15/1024) cs1 k rho^4 rs1 rs2 + (-15/2048) cs1 k1 rho^4 rs1^2 + (-15/128) cs1^2 cs2 k rho^6
         + (15/128) cs1^3 ell1 k rho^4 + (-5/128) cs1^3 k1 rho^6 + (-5/128) cs2 e0 k rho^4
         + (-15/2048) cs2 k rho^4 rs1^2 + (-3/32) e0 e1 ell2 + (-3/32) e0 ee1 ell1
         + (3/32) e0 ez3 rho^2 + (3/32) e1 ec3 rho^2 + (-3/32) e1 ee0 ell1
         + (5/256) e1 ell1 k rho^2 rs1 + (-5/512) e1 k rho^4 rs2 + (-5/512) e1 k1 rho^4 rs1
         + (3/32) ee0 ee1 rho^2 + (-5/512) ee1 k rho^4 rs1
```

The `e1`-only restriction of unspecialized `Tg12_2` is exactly the last summand of specialized `Tg12_2`. No other frozen row has a pure-`e1` term. `J1=0` is load-bearing for `A00`/`A10`: e.g. unspecialized `Tg12_4` contains `(-3/32) rs a0^2` and unspecialized `Tg12_1` contains `(-3/8) cs a1^2`. Those die with `J1` and are not `{a0,rho}` or `{a1,rho}` terms.

Monomial-support census, unspecialized and after `J1=0`: no constant term; no pure-`rho` term; no term supported in `{a0}`, `{a1}`, `{a0,rho}`, `{a1,rho}`, or `{a0,a1,rho}`. That is stronger than substitution, and it is why `A00`, `A10`, and the origin are `Q[rho]`-zeros rather than sampled points.

---

## 3. Attack: radical nonmembership

The producer infers `a0∉rad(I+J1)` from `A00` and `a1∉rad(I+J1)` from `A10`, without computing a radical. That inference holds.

If `a0^N ∈ I+J1`, apply `φ_00`. The left side becomes `1^N=1` and the right side becomes `0` in `Q[rho]`. Contradiction. The same for `a1` and `φ_10`. This is a ring homomorphism, valid over `Q`, and does not use Hilbert's Nullstellensatz over an algebraic closure, a Groebner basis, or an ideal-membership probe. The producer firewall sentence “No ideal membership or radical was computed; the nonmembership statements come only from explicit rational points” is the correct justification.

Two caveats, neither of which breaks the claim:

- The unexecuted replay's `evaluate_point` sums only pure powers of `a0` (resp. `a1`) after the J1 kill. That is a `Q`-point with `rho=0` as well, and would silently ignore a leftover `rho^k` or `a0^i rho^j` term. The producer *text* claims `rho` free. The bytes support the text: there is no such leftover term. This review checked the `Q[rho]` statement, not the weaker point check.
- “All other names zero, `rho` free” is an assignment, not a section of a compiled chart. Saturation at `a0` is vacuous at `a0=1`. The bilinear `a1=a0·qa1` holds at `(1,0)`. That is compatibility of the source prefix with the chart presentation, not a theorem about unwritten stage-two generators.

`A00` with `a0=1` therefore proves the standard `a0`-chart of this prefix nonempty. `A10` with `(a0,a1)=(0,1)` proves both the unordered `D_+(a1)` and the ordered `V(a0)∩D_+(a1)` of this prefix nonempty. Those are the two standard `J2` charts over `A/J1`.

---

## 4. Attack: terminal receiver and operational futility

The terminal receiver in the staged tree is `V(J1+J2)=V(rs,cs,c0,c1,a0,a1)`, not `D_+(a0)` and not `D_+(a1)`.

`A00` has `a0=1`. `A10` has `a1=1`. Neither point lies on `V(a0,a1)`. The implication

```text
a0,a1 ∉ rad(I+J1)  ⇒  1 ∉ rad(I+J1+(a0,a1))
```

is false in general (e.g. `I=(a0+a1-1)`). Preregistration interpretation bullet 2 and producer Consequence 2 therefore over-claim when they write that the two zero-section controls prove the prefix cannot empty the terminal receiver.

The operational conclusion is nevertheless true for *this* prefix, by a third map that the same specialization supplies and that the producer did not cite: `φ_0` above. There is no constant term and no pure-`rho` term, so the origin/`rho`-line is a `Q[rho]`-zero of all 22 rows on `V(J1+J2)`. An emptiness search of the terminal using only these rows is deciding a false statement. Repair of the producer sentence is to cite this origin section, not `A00`/`A10`.

Two further limits on “futile”:

- Futility is emptiness of the *charts of this prefix*. The specialized ideal is not the zero ideal on `V(J1)`: `Tg12_4=(3/32)(e0^2+rho^2 e1^2)` is a genuine `J2`-free relation, and specialized `Tg12_2` still contains `(3/32)e1^2`. A Groebner run aimed at those relations is a different task from a `J2` emptiness search, and is not licensed or forbidden by the census. The producer sentence “the next source task is not a Rees/Groebner launch” is accepted only as a prohibition on emptiness launches, not as a prohibition on reading the twelve surviving polynomials.
- Futility does not survive adjoining a new exported row. A row that vanishes at `A00` and `A10` can still cut the origin and empty the terminal of a larger prefix; a row nonzero at `A00` can still vanish on `V(a0,a1)`. The recommended next export (“first unexported row that is nonzero at `A00` or `A10`”) is the right cheap test for the *charts*, and is not a test for the terminal. Unexported grade 13 and the other grade-14 rows are not in evidence.

Consequence 1 is confirmed as a statement about this exported prefix: stage-one certificate rows `Tg10_1..Tg10_4,Tg12_6` vanish on `V(J1)`, and the first surviving grade is 11. It is not a statement that the full source first sees `J2` at grade 11.

---

## 5. Attack: source prefix versus Rees chart versus full source

The 22 files are a hash-pinned actual-total prefix: all V9 `Tg` rows through grade 12, and V17 row 5 at grade 14. No `Tg13_*` file exists in V9. No other grade-14 actual-total row is exported. Chart names `qa0,qa1,qrs,qc0,qc1,u,v` do not occur. Rees bilinears and saturations are not among the generators.

`A00` and `A10` are source-prefix sections compatible with the named `J2` chart relations after the base change `A/J1`. They are not points of a fully compiled stage-two chart, because unwritten stage-two equations and any genuine localizer that vanishes on the section are absent. Merely rewriting these 22 rows in a different standard presentation of `J1` or `J2` cannot delete the sections. Changing the blown-up ideal, adding a localizer that vanishes on the section, or adding new source rows can.

The producer firewall is the correct scope: no Gate T, no order-two, no maximum-twelve, no JC2, no claim on unexported source. The sibling `CS0` horizontal section of the unlocalized `k=0` prefix is a different assignment and was not recharged here; `k=0` is not load-bearing for `A00`/`A10` after `J1=0`, because no specialized term is supported in `{a0,k,rho}` or `{a1,k,rho}`.

---

## 6. Findings

### High

None that change the census.

### Medium

**M1. Terminal receiver as a corollary of `A00`/`A10`.** Preregistration interpretation bullet 2 and producer Consequence 2 attribute nonemptiness of `V(J1+J2)` to the two unit points. Those points do not lie on the terminal. The same bytes give a genuine origin/`rho`-line section of the terminal of this prefix. Repair: cite `φ_0`, or drop “terminal receiver” from the `A00`/`A10` sentence. Operational emptiness-futility for the terminal survives the repair.

**M2. Replay `evaluate_point` is weaker than the producer text.** The text claims `rho` free. The unexecuted replay's point check, read only as text, sums pure `a0` (resp. `a1`) powers, which is the special-fibre slice and would miss a pure-`rho` leftover. Independently, there is no such leftover. Do not treat replay stdout as a `Q[rho]` certificate.

### Low

**L1. Replay `SPECIALIZED_VARIABLES`.** The unexecuted script, read only as text, would print `all_source_names - J1`, which keeps ten names that do not appear in any specialized monomial (`ac4,az4,cs3,cs4,ell4,k10_3,k10_4,k2c,rs3,rs4`). That line is not reproduced in the producer markdown. Actual specialized support is the 26-name list above.

**L2. `Tg14_5` stem.** The V17 file is `Tg14_5_q.poly`. Cosmetic.

**L3. Producer markdown omits per-row specialized term counts.** The preregistration required the replay to print them. This review recorded them from the bytes. No algebraic effect.

---

## Accepted theorem

On the frozen exact-Q V9 rows `Tg10_1,...,Tg12_7` and the frozen exact-Q V17 row `Tg14_5`, after the base change `J1=(rs,cs,c0,c1)=0`:

- All seven grade-10 rows vanish identically, as do `Tg11_4`, `Tg11_6`, and the stage-one row `Tg12_6`.
- Twelve rows survive, first at grade 11, with the specialized polynomials and digests above. `Tg12_4` is `(3/32)(e0^2+rho^2 e1^2)` and has no `a0`/`a1` support. The `e1`-only restriction of `Tg12_2` is `(3/32)e1^2`.
- `A00` (`a0=1`, other source names `0`, `rho` free) and `A10` (`a1=1`, other source names `0`, `rho` free) are `Q[rho]`-zeros of all 22 rows. Hence `a0,a1∉rad(I+J1)`, the standard `a0`-chart of this prefix is nonempty, and the ordered `a1`-chart of this prefix is nonempty.
- The origin/`rho`-line (`a0=a1=J1=0`, other names `0`, `rho` free) is a `Q[rho]`-zero of all 22 rows, so the terminal receiver of this prefix is nonempty.

No emptiness certificate for either standard `J2` chart of this prefix, or for its terminal receiver, can be written from these 22 rows.

## Nonclaims (not accepted)

- Any unexported source row (grade 13, other grade-14 rows, higher grades, even-sheet `Fg*`, `Keep*` remainders, full source ideal, source-family coverage).
- A point of a fully compiled `J2` Rees chart, including unwritten stage-two equations, unchecked saturations, or additional genuine localizers.
- Emptiness or nonemptiness of the localized `T-cs` fibre on `D(cs*k)`, or any weakening of promoted `T-rs`, `T-c0`, ordered `T-c1`, or localized `T-cs`.
- Associated-prime / embedded-component analysis; a statement that every component of the specialized prefix is `rho`-torsion-free.
- A Groebner basis, a Rees bilinear, or an ideal-membership identity among the twelve survivors other than the explicit polynomials recorded here.
- A formal or algebraic arc, a Keller pair, Gate T, all order two, maximum twelve, JC2, TD6, AS109, or any Lean statement.

`jc2-lean` was not accessed. No AWS state was mutated. No campaign computation was launched. The producer replay was not executed. The only repository file written is this review.
