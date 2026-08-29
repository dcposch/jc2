# Hostile review: K00 syzygy-origin projection V16R1

| Field | Value |
|---|---|
| Charged case | `cases/max12_812_order2_u2_62_k00_syzygy_constant_projection_v16r1_20260827/` |
| Charged claim | Unloaded `C6=1` origin-evaluation of `Syz_R(r1,...,r7)` has rank one, with coordinates 2, 4, and 6 identically zero; every local representation `r7=sum_{i=1}^6 q_i r_i` in `R_m` therefore has `q2(0)=q4(0)=q6(0)=0` |
| Overall verdict | **PASS** |
| Smallest failing identity | none |
| Repairs required | none |
| Reviewer / model | Grok 4.6 (xAI). Independent SHA-256 of freeze and portable evidence; independent tail-to-row reconstruction; independent Singular 4.4.1 replay of all 87 frozen generators; independent origin evaluation of all 609 components; independent max-abs-pivot Gaussian elimination over `Q`; independent fresh `syz(r1,...,r7)` and two-sided module membership; independent replay of the seven serialized base-syzygy bytes. Producer `PASS`/`ENDPOINT`/`validator` strings, stored ranks, branch labels, and hash *claims* were not used as mathematical evidence |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-27 |

No producer status line is evidence. No integer in `RESULT.json` is evidence. The producer validator was read only to record what it *would* have accepted; every load-bearing integer below was recomputed here. Canonical ledgers, `jc2-lean`, and every file other than this review were left untouched.

---

## Line-item verdicts

| # | Required check | Verdict |
|---|---|---|
| 1 | Frozen source hashes and portable `EVIDENCE.sha256` from actual bytes; AWS-absolute `PRODUCER_ARTIFACTS.sha256` treated as provenance only | **PASS** |
| 2 | Original V16 is nonpromotable (`NO_COORD6_FREEDOM` made a process failure); V16R1 accepts both preregistered branches on new tags and new source bytes | **PASS** |
| 3 | Reconstruct the seven exact rows from the frozen replay prelude; parse the frozen 87-generator module; replay all 87 identities; confirm it is the full `syz(r1,...,r7)` of V14R1, not a subset | **PASS** |
| 4 | Independently parse all 609 origin constants; recompute the `7x87` rank over `Q`, the `(6,7)` projection rank, and vanishing of rows 2, 4, and 6 | **PASS** |
| 5 | Independently replay the seven serialized base-syzygy component bytes in a fresh exact-`Q` process; literal-zero residual; independent origin of the seventh component; claimed origin vector | **PASS** |
| 6 | Localization-completeness: clearing denominators in `R_m` and the sign in `r7=sum q_i r_i` | **PASS** |
| 7 | `p=65521` is a software control only; it did not silently substitute for exact `Q` | **PASS** |
| 8 | Omitted denominators, `syz(r1,...,r7)` vs `syz(r1,...,r6)`, incomplete generation, unsafe normalization, characteristic leakage, local evasion of the polynomial-span argument | **PASS** (no such defect in the charged claim) |
| 9 | Firewall: even a PASS is only unloaded order-zero local constants at `C6=1` | **PASS** (scope held) |

**Overall: PASS.**

---

## Strongest theorem justified by the bytes

Let `R=Q[d0,d1,d2,d3,d4,d5]` with maximal ideal `m=(d0,...,d5)`, and let `r1,...,r7` be the seven unloaded K00 coefficient polynomials at the Kummer chart `C6=1` (the frozen V14R1 replay prelude; independently equal, byte-for-byte, to the load-zero specialization of frozen `tails.json` under that chart). Let

```text
S = Syz_R(r1,...,r7)  subset R^7
```

be the full polynomial first syzygy module. Then:

1. The frozen 13 110 129-byte serialization `SYZYGY_MODULE.txt` (SHA-256 `788a836b729d3de5e9600de07244b5d4b836c91a7538e0b1e4ef307ad86d21fb`) is an 87-generator generating set of `S`. Independently recomputed `T=syz(r1,...,r7)` over `Q` in Singular 4.4.1 also has 87 generators, and the two generating sets define the same `R`-module: every frozen generator reduces to `0` against `std(T)`, and every generator of `T` reduces to `0` against `std(Frozen)`.
2. The origin-evaluation map `ev_m: S -> Q^7` has image of rank **one**, spanned by

```text
v = (-200, 0, -960, 0, -5120, 0, -40960).
```

3. Every vector in `im(ev_m)` has coordinates 2, 4, and 6 equal to `0`. Equivalently, the `(6,7)`-projection of `im(ev_m)` has rank one, not two.
4. There exists an explicit polynomial syzygy (the first frozen generator, independently serialized as the seven `BASE_SYZYGY_i` files) whose origin is exactly `v`, whose seventh origin coordinate `-40960` is a unit in `R_m`, and which satisfies the literal polynomial identity `sum_{i=1}^7 b_i r_i = 0`.
5. Consequently, for every representation

```text
r7 = q1 r1 + q2 r2 + q3 r3 + q4 r4 + q5 r5 + q6 r6
    in R_m,
```

one has `q2(0)=q4(0)=q6(0)=0`. Any such representation is the local syzygy `(q1,...,q6,-1)`. A common denominator `s notin m` clears it to a polynomial syzygy; origin evaluation multiplies the vector by the nonzero scalar `s(0)`. Hence the origin of every local representation lies in the line `Q·v`, which has zeros in coordinates 2, 4, and 6. Equivalently, after scaling a unit-seventh polynomial syzygy `(s1,...,s7)` one has `q_i = -s_i/s7` (the minus sign is required by `sum s_i r_i=0`), so `q_i(0)=-s_i(0)/s7(0)`; zeros remain zeros under the sign.

This is representation-independent: it uses the full first syzygy module of all seven rows, not a preferred lift of a colon witness.

Nothing stronger is justified. In particular this does **not** compute a first-order load/deformation class, does not restrict that class to an honest `Lambda<=19` source image, and is not a closure-incidence, Taylor-realization, order-two, maximum-twelve, or JC2 theorem.

---

## 1. Custody

All twelve lines of `FREEZE.sha256` verify against the files on disk. The self-hash of `FREEZE.sha256` is

```text
761c343fb278cce90fafcba36c5a486471082b661ea4757e24e02594ee50f6f8
```

equal to `freeze_sha256` in `AWS_REGISTRATION.md`. Independently recomputed pins:

| Artifact | SHA-256 |
|---|---|
| V16R1 `PREREGISTRATION.md` | `2ff4b6230e34797d4c67ff482871e846ebc254d2fc05ed6dd707edad3363c7ac` |
| `compile_syzygy_projection_v16r1.py` | `80a281fd01174b438c093766e295fc8dd19cc3e3e5f2f80ccabf05be1c4ed582` |
| `build_serialized_replay_v16r1.py` | `fc1d448f79e1c5f99a21ef4377e09a2e5426775925120130ee844bb569b09087` |
| `validate_syzygy_projection_v16r1.py` | `76d00a252853f31ff9e66d3e2c660f3b40ad87e2c2e86bf89a97443d319ae5b9` |
| `run_syzygy_projection_v16r1_aws.sh` | `39edb3fc928c8179830c866c39cc93308c2d2cec76a7280ef5ff21b599f20187` |
| V16 `compile_syzygy_projection_v16.py` | `38d9f4756c8606ac05073c904209dc8591a82db0007c54802b7f302e77d824c9` |
| V16 `FAILURE.md` | `0f5069b7fe3f69e519e4ab1d92c2cb7aa3c29c5e3eff2d6612f7039e2be5bf20` |
| V14R1 exact `RESULT.json` | `28be0ddf9d12529586817e6a7e96cb3ff2bc8e84e4983f7c2f25366f81b4f7e2` |
| V14R1 replay prelude | `5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a` |
| V14R1 `SYZYGY_MODULE.txt` | `788a836b729d3de5e9600de07244b5d4b836c91a7538e0b1e4ef307ad86d21fb` |
| `ops/aws_exact_lane.sh` | `ebe06a100ae8f6bcdbdc580be89954d4cbc560c97cd75014153d61292415959b` |
| `run_singular_in_dir.sh` | `c4707d963359b906739d3436a97c17db707d5af5392ec70429aaa2d650436a6c` |

Portable top-level `EVIDENCE.sha256`: **1300/1300 lines OK**, exit 0. That is the local custody check.

Producer-origin `run/PRODUCER_ARTIFACTS.sha256` uses absolute AWS paths of the form `/home/ubuntu/jobs/...`. Treated as provenance only. Remapping each of the 618 Q-lane (resp. 618 `p=65521`-lane) lines onto the harvested local `run/artifacts/` copy yields **618/618** hash matches on each lane. The Q-lane `ENDPOINT_EVIDENCE.sha256` remaps the same way: `RESULT.json` = `b6cd066a5d93fa81a4eb4217f44916969aa7b515b7e367befbe9018045a6d7ff`, residual = `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`, replay stdout = `3f4cfffe764b4df460100a8510b613750a3eab2e5af941fcc9e8434e4a1c21c4`.

The Q compiled input `k00_syzygy_projection_v16r1_Q.sing` has SHA-256 `f5b690787e812eb7029906a9ab61c1815136ad28ab2d8f70aadf139fa653d4c6` and inlines the V14R1 syzygy serialization **byte-identically** (13 110 129 bytes after `module S=`). It does **not** contain `syz(A)`; V16R1 consumes the frozen V14R1 output rather than recomputing it. Completeness relative to `syz` is therefore a V14R1 inheritance plus the independent recompute in §3.

Registered tags are new relative to V16:

```text
V16   Q: max12_812_order2_u2_62_k00_syzproj_v16_q_20260827T101653Z_box01
V16R1 Q: max12_812_order2_u2_62_k00_syzproj_v16r1_q_20260827T102631Z_box01
source_payload V16   = 8822a8a9ee280e250d025342b48690d7811b78a6e53abab90ffefa183243cbd3
source_payload V16R1 = f4bcb24e99524a84ac5b6f5f5b3aba226ce54fc0b44b6f17fc93c37a8faf70ba
```

---

## 2. Why original V16 is nonpromotable, and why V16R1 is a genuine repair

Original V16 is a design failure, not a mathematical endpoint. Both of its lanes replayed the 87 generators and wrote all 609 origin constants, then emitted

```text
K00_SYZPROJ_FAIL=NO_COORD6_FREEDOM
```

and died. Independently: those 609 V16-failed Q constants are **bytewise equal** to the V16R1 Q constants, so V16 had already computed the rank-one, coordinates-2/4/6-zero span and then refused to accept it.

The refusal is in the V16 compiler, not in the algebra. After searching for a generator whose `(6,7)` origin is linearly independent of a unit-seventh base, V16 does

```text
if (freedom_index==0) { print("K00_SYZPROJ_FAIL=NO_COORD6_FREEDOM"); quit; }
```

and never writes `BRANCH.txt`. Its validator additionally demands the markers `K00_SYZPROJ_FREEDOM_REPLAY=1`, `FREEDOM7_ZERO=1`, and `FREEDOM6_UNIT=1`. The V16 preregistration is more biased than `FAILURE.md` admits: although it says the endpoint must *decide* whether the `(6,7)` projection has rank two, the custody paragraph **requires** serialization of a freedom syzygy with sixth origin a unit. There is no V16 custody path for the no-freedom branch. Nothing from V16 is promotable as a theorem.

V16R1 is a new producer on new bytes:

- compiler SHA `80a281fd...` ≠ V16 `38d9f475...`;
- preregistration SHA `2ff4b623...` ≠ V16 `1bf2dc8c...`;
- validator SHA `76d00a25...` ≠ V16 `d9f4d892...`;
- runner SHA `39edb3fc...` ≠ V16 `c6b185c1...`;
- tags and `source_payload` as above;
- marker prefix changed from `K00_SYZPROJ_` to `K00_SYZPROJ_R1_`.

The V16R1 preregistration, frozen before the algebra, names both branches `M6_FORCED` and `M6_FREEDOM` and forbids a hard-coded expected rank. The compiler writes `BRANCH.txt` in both cases, and only rejects a third pattern (`freedom_index==0` but some sixth origin nonzero). The validator accepts either named branch and rejects inconsistency with the independently parsed matrix. This run took `M6_FORCED`, which is one of the two preregistered outcomes, not a process failure.

---

## 3. Rows, the 87-generator module, and completeness of `syz(r1,...,r7)`

**Rows.** The frozen V14R1 prelude is eight lines, `ring R=0,(d0,...,d5),dp;` followed by `poly r1=...` through `poly r7=...`. Independently reconstructed from frozen `tails.json` (raw SHA `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848`, canonical SHA `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`) by discarding every monomial with a load factor `(k10,k6,k2)` and substituting the Kummer chart at `C6=1`

```text
C6=1, C5=d5, C4=(3+d4)/8, C3=d3, C2=(1+d2)/16, C1=d1, C0=(1+d0)/256
```

the seven polynomials are **byte-identical** to the prelude (lengths 546, 819, 947, 1334, 1545, 2043, 2413). A fresh Singular 4.4.1 process reports `ROWℓ_PRELUDE_EQ_TAIL=1` for all seven, origins all `0`, and degrees `(4,4,5,5,5,6,6)`. Weight and load-linearity assertions on every tail monomial pass. The V16R1 Q compiled prelude is byte-identical to this V14R1 prelude.

**Module parse.** `SYZYGY_MODULE.txt` is a single line, 13 110 129 bytes, **86 commas** (87 generators), **zero** slashes, **zero** semicolons, **zero** newlines. It contains `gen(1)` through `gen(7)` and does not contain a ring declaration. The 125 occurrences of the digit string `65521` are interior digits of large integer coefficients (e.g. `...11465521673...`), not a characteristic.

V14R1's compiled script, not V16R1's, is the origin of those bytes:

```text
ideal A=r1,r2,r3,r4,r5,r6,r7;
module S=syz(A);
write("SYZYGY_MODULE.txt",S);
```

V14R1 stdout records `K00_COLON_SYZ_GENERATORS=87` with `K00_COLON_SYZ_REPLAY=1`. There is no filter, slice, or hand-picked subset between `syz(A)` and the write. V16R1 inlines that file and checks `size(S)==87`.

**Replay of all 87 identities.** A reviewer-written Singular script over `ring R=0,(d0,...,d5),dp` loaded the prelude rows and the frozen module as `Frozen`, then for each `j=1..87` computed `z=sum_{i=1}^7 r_i * Frozen[j][i]`. Result: `FROZEN_SIZE=87`, `ALL_REPLAY=1`. No identity failed.

**Not a subset of the full syzygy module.** Independently, in the same exact-`Q` process,

```text
module T=syz(A);          // A=(r1,...,r7)
```

returned `T_SIZE=87`. Two-sided membership against Gröbner bases:

```text
FROZEN_IN_FULL=1    // every Frozen[j] reduces to 0 against std(T)
FULL_IN_FROZEN=1    // every T[j] reduces to 0 against std(Frozen)
```

So `Frozen = T = Syz_R(r1,...,r7)` as `R`-modules, not merely an `R`-generating set of a submodule. Size coincidence alone would be weak; the two-sided reductions are the completeness check.

**Not `syz(r1,...,r6)`.** Independently, `module S6=syz(r1,...,r6)` has `S6_SIZE=66`, not 87, and lives in a free module of rank 6. The frozen serialization uses `gen(7)` (3938 times) and therefore cannot be a six-row syzygy. V14R1 also computed the six-row colon `quotient((r1,...,r6),r7)` separately; that object is not the charged module.

---

## 4. Independent origin matrix, rank, and vanishing

All 609 files `SYZ_CONSTANT_{i}_{j}.txt` for `i=1..7`, `j=1..87` exist; the glob has no extras. Independently parsed as rationals (alphabet `-0123456789/` only). All 609 have denominator **1**. Independently, Singular evaluated `subst` of every frozen component at the origin and wrote 609 `REV_CONST_*` files: **0 mismatches** against the harvested constants.

Independent Gaussian elimination over `Q` (largest-magnitude pivot, not the producer validator's first-nonzero-in-column scan), plus a second integer-clearing elimination:

| Quantity | Independent value |
|---|---|
| `7 x 87` rank over `Q` | **1** |
| rank of rows `{2,4,6}` | **0** |
| rank of the `(6,7)` projection | **1** |
| rank of rows `{1,3,5,7}` | **1** |
| row 2 identically zero | yes (0/87 nonzero) |
| row 4 identically zero | yes |
| row 6 identically zero | yes |
| row 7 not identically zero | 48/87 nonzero |
| nonzero columns | 48, all scalar multiples of `v` |
| first nonzero column (1-based index 1) | `v` itself |

The 48 nonzero columns are pairwise parallel to `v` with 48 distinct nonzero rational scales (the first scale is `1`). That is stronger than rank one: the origin span is exactly `Q·v`.

The producer integers `evaluation_rank=1` and `projection_rank_67=1` happen to match. They were not used as evidence.

Canonical JSON digest of the 609 independently parsed integers is `34640d1a2d9c2c4076b680ef5573dd8f1ceacb40c09caae918d6a0f12e32f791`, matching the stored `constant_matrix_canonical_sha256` as a custody cross-check only.

---

## 5. Serialized base-syzygy replay

The seven harvested component files contain no `/`, no `;`, no quotes, and no interior newlines. Their SHA-256 values are

| i | SHA-256 of `BASE_SYZYGY_i.txt` |
|---|---|
| 1 | `72c69ca11b1164f4ad18082ee0ae1ddae689f82551809d3a838d8752bf6eb5f7` |
| 2 | `16d387a899b393a2e49ca37d8d98a1ebe35fadec7453ff53e1bdb37fe7251ab0` |
| 3 | `329de4455ad06c67ce3c926845c1738e3edd0286714347d47d85faae8b8cac4f` |
| 4 | `73b1814fdf949396909865ae469accfbc0fdf344f980d36cc774cbff823fad25` |
| 5 | `1458a3faf5d9e42c382db12b99b593eb39cdff10abd7f3c1c533b3650dbf0aed` |
| 6 | `c0eead7a54873b3778dcbeef0001bb54fe4a65692724534bb83f8c2d860fadbf` |
| 7 | `bb137f2bcc6ad6fbfb4ab677506f4df494baf76584bbfc3a3d4191301d996464` |

A reviewer-written exact-`Q` Singular process, assembled only from the prelude and these seven bytes, computed `rb=b1 r1+...+b7 r7` and obtained the literal residual `0` (file SHA `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`, the SHA of the two-byte file `0\n`). Independently, `b_i` equals `Frozen[1][i]` for all seven components.

Hand evaluation of the serialized polynomials at the origin, without trusting Singular `subst`:

```text
b1 = ... + 46*d0 - 869*d2 + 423*d4 - 200          =>  -200
b2 = (no constant term)                            =>     0
b3 = ... - 336*d0 - 1968*d2 + 1728*d4 - 960        =>  -960
b4 = (no constant term)                            =>     0
b5 = ... + 6272*d2 - 384*d4 - 5120                 => -5120
b6 = -301056*d3 + 347136*d5                        =>     0
b7 = -129024*d4 - 40960                            => -40960
```

Singular `subst` agrees. The claimed origin vector is therefore the actual origin of a genuine polynomial syzygy whose seventh component is a unit in `R_m`. No normalization by `-40960` was performed; the producer (and this review) evaluate first.

There are no `FREEDOM_SYZYGY_*` files, consistent with `M6_FORCED` and with the independently verified vanishing of coordinate 6.

---

## 6. Localization-completeness and the sign

`R` is a polynomial ring over a field, hence a UFD and an integral domain. Localization at `m` is an exact functor, so

```text
Syz_{R_m}(r1,...,r7)  =  Syz_R(r1,...,r7) ⊗_R R_m  =  S_m.
```

Every local syzygy is therefore a polynomial syzygy divided by a single common denominator `s notin m`. Evaluating at the origin multiplies the vector by `s(0)≠0`. Conversely every polynomial syzygy is a local syzygy. Because the 87 generators span `S` as an `R`-module (§3), they span `S_m` as an `R_m`-module, and

```text
ev_m(S_m) = Q · ev_m(S) = Q · v.
```

A coordinate that vanishes on `ev_m(S)` therefore vanishes on every local syzygy.

A local *representation* `r7=sum_{i=1}^6 q_i r_i` is exactly the local syzygy `(q1,...,q6,-1)`. The seventh component is the unit `-1`, so this vector is a unit multiple of some element of `S_m` with nonzero seventh origin. Its origin therefore lies on `Q·v`, forcing `q2(0)=q4(0)=q6(0)=0`.

**Sign.** From a polynomial syzygy `sum_{i=1}^7 s_i r_i=0` with `s7(0)≠0`,

```text
s7 r7 = - sum_{i=1}^6 s_i r_i,
r7    = sum_{i=1}^6 (-s_i/s7) r_i.
```

So `q_i=-s_i/s7` and `q_i(0)=-s_i(0)/s7(0)`. For `v` this is `q(0)=v_{1..6}/40960`, with zeros in positions 2, 4, and 6. Dropping the minus would write `r7=-sum q_i r_i`, which is the wrong identity; it would not affect vanishing. The charged statement uses the correct sign and only claims vanishing.

No local syzygy can evade this span: localization is exact, `S` is finitely generated, and the generating set is complete. Formal-power-series syzygies in `Q[[d0,...,d5]]` that are not in `R_m^7` are not claimed and are not constrained.

---

## 7. Characteristic `p=65521` is a software control

The Q lane is `ring R=0,(d0,...,d5),dp;` throughout: compiled input, compiled prelude, serialized replay, and the reviewer script. The Q replay contains **zero** occurrences of `65521`. No Q-lane artifact file contains that digit string. Q `RESULT.json` has `"field": "Q"` and `"characteristic": 0`.

The finite-field lane is a one-character ring replacement `R=0` → `R=65521` of the same prelude, registered under a different tag on a different host. Independently, reducing the Q origin matrix modulo `65521` reproduces the `p=65521` origin matrix with **0 mismatches**, and `-40960 ≡ 24561 (mod 65521)`, which is the p-lane `BASE7_CONSTANT`. That is the expected reduction of a characteristic-zero computation. It is **not** evidence over `Q`. Rank one and vanishing of coordinates 2/4/6 over `F_{65521}` are recorded only as a software-control consistency check.

---

## 8. Defect search

| Attack | Finding |
|---|---|
| Omitted denominators | Syzygy serialization has no `/`. Origin constants are all integers. Row coefficients are rationals (e.g. `21/512`) and are present in the prelude; identities still hold over `Q`. Clearing in `R_m` is by a unit at the origin, not by a hidden polynomial denominator in `S`. |
| `syz(r1,...,r7)` vs `syz(r1,...,r6)` | Frozen module uses `gen(7)` and equals independent `syz` of all seven. Six-row `syz` has 66 generators. V14R1's colon of six rows is a different object. |
| Incomplete module generation | Two-sided Gröbner reduction against an independently recomputed `syz(A)` proves module equality. V14R1 wrote `syz(A)` with no filter. |
| Unsafe normalization | Origin is evaluated *before* any scaling. The base witness is `Frozen[1]` as written, not divided by `-40960`. No division by a possibly vanishing seventh component occurs. |
| Characteristic leakage | Q lane is `ring R=0`. Digit string `65521` in the module file is interior to large integers. Q artifacts contain no such string. p-lane constants are the Q constants reduced mod `65521`. |
| Local evasion of the polynomial span | Localization is exact; `S` is finitely generated and complete; evaluation of an `R`-linear combination is an `Q`-linear combination of origin vectors. Formal jets outside `R_m` are out of scope. |
| Hand-picked generators | 86 commas, V14R1 `size(S)=87`, independent `size(T)=87`, two-sided membership. |
| Validator as evidence | Not used. Independent max-abs-pivot rank over `Q` and independent Singular origins. |
| Expected-rank hard-coding | V16R1 preregistration forbids it. Compiler emits whichever of the two named branches the matrix supports. This run's `M6_FORCED` is one of those two. |

No defect in the charged claim.

---

## 9. Firewall

Even with the theorem of the opening section in hand, the following remain unproved and are **not** justified by this PASS:

- a first-order load obstruction, or the class `[b1-φ1(q0)]` in `(R/(r1,...,r6))/im(Syz(φ0)→R/(r1,...,r6))`;
- a representation-invariant deformation cokernel in the three load directions;
- honest `Lambda<=19` source-image reachability;
- closure-first incidence;
- Taylor realization of a jet;
- order two, maximum twelve, or JC2;
- any statement off the chart `C6=1`, or after restoring `(k10,k6,k2)`;
- any constraint on positive-order terms of the local multipliers `q_i` (only their values at the origin are forced in coordinates 2, 4, and 6);
- global polynomial membership of `r7` in `(r1,...,r6)` (V14R1 already recorded global *non*membership; this review does not revisit that).

The interpretive sentence in `RESULT.md` about “apparent unit `M6` freedom from the quadratic initial relation `Q6=0`” is colour. It is not charged and is not certified here.

---

## Checks performed (inventory)

1. `sha256sum -c FREEZE.sha256` (12/12 OK) and self-hash of the freeze file.
2. `sha256sum -c EVIDENCE.sha256` (1300/1300 OK).
3. Remap of both `PRODUCER_ARTIFACTS.sha256` files and the Q `ENDPOINT_EVIDENCE.sha256` onto local copies.
4. Independent reconstruction of `r1,...,r7` from frozen tails plus Kummer chart; byte equality with the prelude; Singular equality and origins.
5. Parse of the 87-generator serialization (size, commas, no `/`, V14R1 `syz(A)` write site).
6. Fresh Singular 4.4.1 replay of all 87 identities over `Q`.
7. Fresh `module T=syz(r1,...,r7)` and two-sided membership against `Frozen`; `syz` of the first six rows as a negative control (`size=66`).
8. Independent origin evaluation of all 609 components; 0 mismatches with harvested files.
9. Independent max-abs-pivot rank over `Q` of the `7x87` matrix, of the `(6,7)` block, and of rows `{2,4,6}`.
10. Parallelism of all 48 nonzero origin columns with `v`.
11. Fresh exact-`Q` replay of the seven serialized base components; residual `0`; hand evaluation of their constant terms.
12. Source diff V16 vs V16R1 (compiler, preregistration, validator, tags, payloads); confirmation that V16's 609 Q constants already equal V16R1's.
13. Ring-characteristic isolation of the Q lane; reduction check that the p-lane origin matrix is the Q matrix mod `65521`.

Singular used: Homebrew `Singular 4.4.1` (`arm64-Darwin`, GMP 6.3.0, NTL 11.6.0, FLINT 3.6.0), not the AWS engine. The identities, origins, and module equality are therefore not an echo of the producer process.

---

## Verdict

**PASS.**

The charged narrow theorem is independently established from the frozen bytes. Original V16 is nonpromotable. V16R1 is a genuine both-outcome producer on new tags and new source bytes, and this run's `M6_FORCED` branch is one of the two preregistered outcomes. The strongest justified statement is the unloaded `C6=1` origin-evaluation theorem in the section of that name; the firewall in §9 is mandatory.
