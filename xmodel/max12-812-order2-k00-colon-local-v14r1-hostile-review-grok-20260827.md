# Hostile review — K00 V14R1 exact local membership of unloaded `r7`

| Field | Value |
|---|---|
| Target | Exact-Q local membership `r7 in (r1,...,r6) R_m` at the normalized K00 coefficient germ, witnessed by a unit-denominator polynomial identity |
| Charged case | `cases/max12_812_order2_u2_62_k00_colon_local_v14r1_20260827` |
| Overall verdict | **PASS** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks the charged local-membership claim; mixed `Lambda`/load/target reachability, closure-first incidence, formal convergence, Taylor realization, order two, maximum twelve, and JC2 remain uncharged |
| Reviewer / model | Grok 4.6 (xAI). Independent SHA-256 of every charged pin and freeze entry; independent reconstruction of `r1,...,r7` from the frozen one-parameter tail JSON through the K00 transverse chart with loads dropped and `C6=1`; independent parse of `h,u1,...,u6` over `Q`; coefficientwise replay of `-h*r7+sum_i ui*ri` in an exact rational polynomial ring, with no Singular rerun and no producer marker used as evidence |
| Method | Desk-scale exact arithmetic over `Q` (Python `Fraction` monomial dicts). No AWS job, no heavy local CAS, no web sweep, no ledger edit, no `jc2-lean` entry |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-27 |

V14 remains custody-failed: its single `write("COLON_LIFTS.txt",L)` artifact is the first row of a `6 x 6` matrix (five commas, six polynomials) and is not accepted as a lift. V14R1 is a regenerated producer with byte-frozen 36-entry serialization and a second-process replay. Producer `PASS` / `ENDPOINT` / validator strings, `RESULT.md` prose, and the historical V14 `local_member=true` sentinel were not used as characteristic-zero evidence. No file other than this review was written.

---

## Line-item verdicts

| # | Task | Verdict |
|---|---|---|
| 1 | Rehash and type-check V14R1 preregistration, freeze, producer, serializer, validators, exact result, and both portable manifests; source map reconstructs seven unloaded normalized rows; `Jdet` kept distinct from `J1`/`J2` | **PASS** |
| 2 | Independent exact reconstruction of `r1,...,r7,h,u1,...,u6`; coefficientwise replay of `-h*r7+sum_i ui*ri=0`; `h(0)=20` | **PASS** (residual identically zero; no first nonzero coefficient) |
| 3 | All 36 `COLON_LIFT_i_j.txt` exist and match `EXACT_LIFT_ENTRIES.sha256`; six `UNIT_MULTIPLIER_i.txt` byte-identical to column 1; V14 matrix dump is not evidence and does not determine any missing R1 entry | **PASS** |
| 4 | Fresh replay script obtains `h,u_i` only from serialized polynomial files and the ring/rows from the frozen prelude; correct sign; literal-zero residual; no hidden in-memory matrix, wrong column, truncated matrix, unsafe parse, or false unit test | **PASS** |
| 5 | Polynomial identity `h*r7 in I` with `h notin m` implies `r7 in I R_m`; compatible with reviewed V8 global nonmembership; every finite `(d)`-adic truncation is compatible, so D9+ cannot discover a first filtered obstruction | **PASS** |
| 6 | Independently compiled `p=65521` lane is software control only | **PASS** (not used as a characteristic-zero claim) |
| 7 | Scope firewall: unloaded, normalized, local-ring theorem only | **PASS** |

**Overall: PASS.**

---

## Hashes and charged artifacts

Independently recomputed SHA-256. Every charged prompt pin matches.

| Artifact | SHA-256 | Role |
|---|---|---|
| `RESULT.md` | `039590c8524e98e0fce3f6ada46fdf338270ece56c3aea553644c83911b7f7d7` | producer prose; not mathematical evidence |
| `EVIDENCE.sha256` | `4e0ac1bb66c8c8fe16bb4b29f2cd43afae13f535a0949f55aa42827d501711de` | portable evidence manifest (35 entries, all match) |
| `EXACT_LIFT_ENTRIES.sha256` | `0e4159d5fe514da957b7963edb687583cbd97d76856d436c047505c2e0bddbdb` | portable 36-entry plus unit-column manifest (43 entries, all match) |
| exact `RESULT.json` | `28be0ddf9d12529586817e6a7e96cb3ff2bc8e84e4983f7c2f25366f81b4f7e2` | custody record; `local_member` token ignored |
| fresh exact replay input `replay.sing` | `8f35f7dcad0e678e7ec6a430b54546017e0798b16d69e8491e86b183331ddc07` | second Singular script; independently reconstructed byte-identical |
| fresh exact replay residual | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | literal polynomial `0\n` |
| exact unit witness | `87ced4afe1680f11073eb62bda7c7894f297925283557b2ccf0e951daba09e04` | `63*d4+20\n` |

Freeze and source pins, independently rehashed, match `FREEZE.sha256` (`8c6dd8e2e012d72519051a708975d892c0bed700fbfd17df7c1a15b899fde010`, 21/21) and the V14R1 compiler `EXPECTED` map:

| Artifact | SHA-256 |
|---|---|
| V14R1 `PREREGISTRATION.md` | `65ee7849741bd64adbb842139f12d538e63337aa9cd3c4d6c8c89c49782bbbfd` |
| V14R1 compiler | `b93179211ea9a32be719467534a9059c63e8a255451d3c01323b1a6bdb146bab` |
| serializer / replay builder | `bf7871e6a8b88c526af69d9e9127b7647b681875fc6ff1b341752e5f4975ad44` |
| V14R1 validator | `22788b9a69cb169e91d7aecfd265cb5ec8bb669320189a62ea76a62bd75fe374` |
| AWS runner | `fe7794e08d36eed10d9f7905b3bec28f34bd0ccd63970ca6dde1f18d1cc8021c` |
| AWS registration | `5db50a2180b464345848bae814d41ecb4253bf3f165ac0277b92bc20059f5872` |
| V14 preregistration | `144ff8f46c1d9bc2ef81d2aaa4a454ecb0d772ed345c91f3d446aa830871ea89` |
| V14 compiler | `d801d5518704aba4e1ccc738805506057526cea1875b2c7afdd62d4e3f17b2df` |
| V14 exact `RESULT.json` | `562943e3fa7ff01ecffb00161bf2f71317d0353f7d82e1628a79a47f3a47bbe1` |
| V14 base input `k00_colon_local_Q.sing` | `a57c05c5b0fa144dc421330cec809b8a44061960f4c98a8abe29c9870e666bfe` |
| V14R1 compiled `k00_colon_local_v14r1_Q.sing` | `bca920eb8330f840151383c94af5eaf92878a185178cafed52a4e9a1770fcb97` |
| V14R1 replay prelude | `5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a` |
| frozen `tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` |
| canonical all-tail digest | `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8` |
| V7 source map | `a7f335cdbc3e5525ce641ff10d8370a52d4cbb9c84e2417b17eea64a38154f70` |
| V8 compiler | `a1c4b18c65c053c4365a0b198aa5139206babaccbf02f37e7834583bb7714012` |
| V8 `RESULT.md` | `d3adc56fdbe98e68260489a265f1bbb34a1e062c0ee1fbb4ba6e961d157d3892` |
| V8/V9 hostile review | `6c4ebd6d61189e0f80fd9021edd509cbb323826774644d92828a0badd0943a29` |
| K00 design note | `9c5bf1229cf45dd7ea4d5d3907fd6033c88c0d9768934d01ea79e658f3d65a17` |
| one-parameter Rees reduction | `5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b` |

Unit-column hashes, independently recomputed, match both `EXACT_LIFT_ENTRIES.sha256` and `RESULT.json` `unit_multiplier_sha256`:

| File | SHA-256 |
|---|---|
| `UNIT_MULTIPLIER_1.txt` / `COLON_LIFT_1_1.txt` | `ed096c8246ff96cb5ab621a9a74061b24e1678ff061a98137a067c387969e1e5` |
| `UNIT_MULTIPLIER_2.txt` / `COLON_LIFT_2_1.txt` | `1f8369edbbb10bfbbb155250775399170e696e0fdbe33bb75f54bb5639f78791` |
| `UNIT_MULTIPLIER_3.txt` / `COLON_LIFT_3_1.txt` | `ce8b51a7e9a11f0fa3a3594480fbe3e4b556e9fd0a17cf29175b273474104f0f` |
| `UNIT_MULTIPLIER_4.txt` / `COLON_LIFT_4_1.txt` | `5d9f371cf8302502d05a56effbfe3bbbbeafd28d6dfdad8cf7f1bba3ebb60f18` |
| `UNIT_MULTIPLIER_5.txt` / `COLON_LIFT_5_1.txt` | `135c17e36fd53a438e98c36104e350e6ed362223dfba38e7e927c6dccf65a98e` |
| `UNIT_MULTIPLIER_6.txt` / `COLON_LIFT_6_1.txt` | `93762abdfa9b12b520a47848e55776176d9227eaca253deb80a6a9a13b4c3295` |

---

## Strongest exact theorem that survives

Work over `Q`. Let `R=Q[d0,...,d5]` and `m=(d0,...,d5)`. Let `r1,...,r7` be the unloaded ordinary tails obtained from the frozen 569-term source by dropping every monomial with a positive `k10`, `k6`, or `k2` exponent, substituting the K00 transverse chart

```text
C5=d5,           C4=(3*C6^2+d4)/8,
C3=d3,           C2=(C6^3+d2)/16,
C1=d1,           C0=(C6^4+d0)/256,
```

and imposing the normalized slice `C6=1`. Write `I=(r1,...,r6)`. Independently expanded term counts at this slice are `16,23,27,36,40,42,57`. Every constant term and every linear term in `(d0,...,d5)` vanishes.

There is an identity in `R`

```text
h = 63*d4+20,
h*r7 = u1*r1+u2*r2+u3*r3+u4*r4+u5*r5+u6*r6,
h(0) = 20 != 0,
```

with the six exact multipliers serialized at `UNIT_MULTIPLIER_1.txt` through `UNIT_MULTIPLIER_6.txt`:

```text
u1 = 273/128*d4*d5^2-175/8*d3^2-189/1024*d2*d4+19/64*d4^2
     +147/4*d1*d5+1627/64*d3*d5-689/64*d5^2+23/1024*d0
     -869/2048*d2+423/2048*d4-25/256
u2 = 91/8*d5^3-315/32*d3*d4+7/64*d2*d5+147/16*d4*d5
     +21*d1-21/4*d3+21/16*d5
u3 = -105/128*d4^2-357/8*d3*d5+705/16*d5^2-21/128*d0
     -123/128*d2+27/32*d4-15/32
u4 = -21/4*d4*d5+84*d1-43*d3+65/4*d5
u5 = 35*d5^2+49/16*d2-3/16*d4-5/2
u6 = -147*d3+339/2*d5.
```

The signed residual `-h*r7+sum_{i=1}^6 ui*ri` is the zero polynomial (zero coefficients in every degree). Since `h notin m`, `h` is a unit in the local ring `R_m`. Therefore

```text
r7 in I R_m.
```

This is compatible with the separately reviewed V8 theorem that `r7 notin I` in the global polynomial ring: `h` is not a unit of `R`. It is not mixed load/target or `Lambda`-order reachability, closure-first incidence, formal convergence, Taylor realization, order two, maximum twelve, or JC2.

---

## Attack 1 — freeze, source map, `Jdet` versus `J1`/`J2`

**PASS.**

`FREEZE.sha256`, `EVIDENCE.sha256`, and `EXACT_LIFT_ENTRIES.sha256` all verify entrywise. The V14R1 compiler pins the V14 compiler, V14 preregistration, V14 exact result, and its own preregistration, then transitively loads V8 and V7 and rechecks the canonical all-tail digest. Those pins match the bytes on disk.

The V7 source map `unloaded_tail` does exactly the charged reconstruction:

- monomials have length 10 and weight `12+ell` against `(8,7,6,5,4,3,2, 2,6,10)`;
- load exponents occupy the last three slots, lie in `{0,1}`, and sum to at most 1 (affine load linearity);
- any monomial with a positive load exponent is skipped (loads removed by literal omission, not by a later substitution of a live `k`-variable);
- the seven coefficient images in normalized mode are the K00 chart with `C6` replaced by the numeral `1`.

Independently re-emitting `v7.unloaded_tail(..., images=coefficient_images("normalized"))` is byte-identical to the eight-line frozen prelude

```text
ring R=0,(d0,d1,d2,d3,d4,d5),dp;
poly r1=...;
...
poly r7=...;
```

hash `5b0a77e6…ee7a`. The compiled exact-Q script is the frozen V14 emitter (`a57c05c5…6bfe`) with a unique replacement of `write("COLON_LIFTS.txt",L);` by the 36-entry serializer plus the explicit unit-column replay; the V14 prefix and suffix around that needle are unchanged.

No Jacobian variable occurs. The frozen tails contain zero occurrences of `Jdet`, `J1`, `J2`, or `"J"`. The compiled exact-Q script contains zero occurrences of `Jdet`, `J1`, `J2`, `k10`, `k6`, `k2`, or `Lambda`; the single `C6` hit is the mode label `NORMALIZED_C6_1_GLOBAL_DP`, not a ring variable. The design note keeps the terminal Jacobian `Jdet` distinct from the collision ideals `J1=(rs,cs,c0,c1)` and `J2=(a0,a1)`. This unloaded local claim never eliminates a Jacobian.

Type-check: ring is `R=0,(d0,...,d5),dp`; characteristic recorded as `0`; field `Q`; scope string `NORMALIZED_K00_UNLOADED_LOCAL_MEMBERSHIP_BY_GLOBAL_COLON_ONLY`; preregistration status is a custody repair with no promoted result at registration.

---

## Attack 2 — independent reconstruction and coefficientwise identity

**PASS.** Residual identically zero. No first nonzero coefficient.

Rows were rebuilt from `tails.json` in an exact rational polynomial ring, without parsing producer Singular output. Unloaded/load counts match the V8 audit:

```text
row   all  unloaded  load  expanded_terms  mindeg  maxdeg  const  lin
  1    36        19    17               16       2       4      0    0
  2    54        27    27               23       2       4      0    0
  3    58        30    28               27       2       5      0    0
  4    81        40    41               36       2       5      0    0
  5    89        44    45               40       2       5      0    0
  6   120        57    63               42       3       6      0    0
  7   131        63    68               57       2       6      0    0
```

Chart substitution used the binomial expansions of `((1+d0)/256)^{e0}`, `((1+d2)/16)^{e2}`, `((3+d4)/8)^{e4}` together with pure powers of `d1,d3,d5` and `C6=1`. The six `u_i` and `h` were parsed from the serialized files as expanded polynomials over `Q`. Then

```text
residual = -h*r7 + u1*r1 + u2*r2 + u3*r3 + u4*r4 + u5*r5 + u6*r6
```

was multiplied and added coefficientwise. Every coefficient vanished. Substituting `d0=...=d5=0` in `h` yields the constant `20`.

The displayed multipliers in `RESULT.md` match the six files as polynomials (the trailing period on the `u6` prose line is markdown, not a coefficient). This match is a consistency check, not evidence: the identity was replayed from the files and the independently expanded rows.

---

## Attack 3 — 36-entry custody, column 1, historical V14 gap

**PASS.**

All 36 files `COLON_LIFT_i_j.txt` exist, are nonempty single-line expanded polynomials over `Q`, parse, and hash to `EXACT_LIFT_ENTRIES.sha256`. The six `UNIT_MULTIPLIER_i.txt` are byte-identical to `COLON_LIFT_i_1.txt` (column 1) and are not byte-identical to `COLON_LIFT_1_i.txt` for `i>1` (that would have been the truncated first row). The first colon generator is `63*d4+20`, matching both `LOCAL_UNIT_WITNESS.txt` and `LOCAL_UNIT_WITNESS_R1.txt`. Witness index 1 is therefore the correct column for the charged identity, not a row-major mixup with Singular's truncated `write(L)`.

V14's `COLON_LIFTS.txt` is 1696 bytes, five commas, six polynomials, and is byte-identical to V14R1's still-truncated `COLON_LIFTS.txt`, which itself equals the comma-join of `COLON_LIFT_1_1` through `COLON_LIFT_1_6`. V14 artifacts contain no `COLON_LIFT_i_j.txt` and no `UNIT_MULTIPLIER_i.txt`. No polynomial from rows `i=2..6` of the R1 matrix occurs as a substring of the V14 dump. V14's in-memory `local_member=true` and its one-row serialization are not a 6-by-6 lift, and no missing R1 entry was inferred from them.

---

## Attack 4 — fresh replay construction

**PASS.**

`build_serialized_replay.py` is the only constructor of the second script. It:

- requires a unique `ring R=` line and seven `poly r{i}=` lines from the frozen prelude;
- reads `h` and `u1,...,u6` from `LOCAL_UNIT_WITNESS_R1.txt` and `UNIT_MULTIPLIER_i.txt`;
- rejects `;`, `"`, and raw newlines inside those files (trailing newline is stripped);
- wraps each serialized polynomial in parentheses;
- emits the signed residual `-h*r7+u1*r1+...+u6*r6`;
- substitutes all six `d_i` to `0` for the unit check;
- writes `SERIALIZED_IDENTITY_RESIDUAL.txt` and `SERIALIZED_UNIT_WITNESS.txt`;
- contains no `lift`, `quotient`, `syz`, `matrix L`, `std`, `ideal I`, `ideal C`, or `COLON_LIFT` token.

Independently replaying that construction from the prelude and the seven polynomial files reproduces `replay.sing` byte-for-byte (hash `8f35f7dc…dc07`). The residual artifact is the two-byte polynomial `0\n`. The serialized witness is byte-identical to `LOCAL_UNIT_WITNESS_R1.txt`. Replay stderr is empty (`e3b0c442…8255`).

Attacks on the construction:

- **Unsafe parsing.** The six unit files and the witness are single-line expanded polynomials with no quotes, semicolons, or embedded newlines. Parentheses wrapping cannot inject Singular commands.
- **Hidden in-memory matrix.** The second process is a new Singular invocation on a script that never mentions `L`. It cannot reuse the first process's lift matrix.
- **Wrong column.** Unit files match column 1, not row 1. The first colon generator is `h`. Using the truncated `COLON_LIFTS.txt` as six multipliers would have used row 1 and would have failed the identity already replayed in Attack 2.
- **Truncated matrix.** The charged identity uses only column 1, which is fully serialized. The other 30 entries exist as files and hash; they are not inputs to the charged residual.
- **False unit tests.** The V14 emitter contains a toy colon on `((1+d0)*d1)`. That toy is a software smoke test of `quotient`/`lift` and is not a certificate that `63*d4+20` is a unit at `m`. The charged unit check is the constant term of the serialized witness, independently `20`.

The first-process in-memory replay `chosen_replay=-chosen_h*r7+sum I[i]*L[i,witness_index]` uses the same sign as the fresh script. It was not trusted; the independent rational residual is the evidence.

---

## Attack 5 — local-from-global identity, V8, and filtered truncations

**PASS.**

In a polynomial ring, `h*r7 in I` means `h in (I:r7)` by definition. If also `h notin m`, then `h` is a unit of `R_m`, so `r7 = h^{-1} sum_i ui ri` lies in the extension `I R_m`. Equivalently, `(I:r7)+m = R`. This is the standard translation of local membership at the origin of `A^6`. No Gröbner computation in `R_m` is required once the polynomial identity and the nonzero constant term are in hand.

V8, independently reviewed at hash `6c4ebd6d…3a29`, is the global statement `r7 notin I` in `R` (and on `D(C6)` before the Kummer slice). That does not contradict local membership. Units of `R=Q[d0,...,d5]` are `Q^\times`. The denominator `63*d4+20` is nonconstant, so it cannot clear a global membership. It is invertible in `R_m` and in every `m`-adic truncation `R/m^N`, because its image in `R/m \cong Q` is `20 \neq 0`, and units lift along nilpotent extensions.

Consequently, for every `N\ge 1`,

```text
h*r7 in I  subset  I + m^N,
```

and multiplying by the inverse of `h` in `R/m^N` yields `r7 in I + m^N`. Every finite `(d)`-adic / filtered Macaulay cutoff is therefore compatible. V9's D2--D7 rank equalities are special cases of this exact identity, not independent local theorems. A D9+ filtered search cannot discover a first obstruction: there is no obstruction at any finite order. The only nonmembership is global, and its witness is this denominator.

The colon ideal has other generators with nonzero constants (`9261*d2+2540`, `194481*d0-74296`, `9261*d5^2-484`). They are not needed. One unit in `(I:r7)` suffices.

Producer claims about a 6-generator colon, an 87-generator syzygy module, and projection equality were not independently recomputed and are not part of the charged theorem.

---

## Attack 6 — `p=65521` is software control only

**PASS, as a control; no characteristic-zero inference.**

The `p=65521` lane is independently compiled: prelude ring `R=65521,(d0,...,d5),dp`, distinct input hash `c0d5deba…c353`, distinct witness file `d4-20800`, and unit-column hashes different from the exact-Q files. The monic form `d4-20800` is the reduction of `63*d4+20` by the inverse of `63` in `F_65521` (`20*63^{-1} \equiv 44721 \equiv -20800`). That is the expected modular image of a characteristic-zero identity, and it is not a proof over `Q`. The shared residual hash `9a271f2a…86aa` is the hash of the two-byte file `0\n` and likewise proves nothing in characteristic zero.

The exact-Q identity of Attack 2 is the only characteristic-zero certificate.

---

## Attack 7 — scope firewall

**PASS.**

The surviving theorem is membership of the unloaded, `C6=1` coefficient row `r7` in the extension of `(r1,...,r6)` to the local ring of `Q[d0,...,d5]` at the origin. It uses no load variables, no `Lambda`, no `Jdet`, and no target equation `Phi7`. It does not by itself imply:

- mixed load/target or `Lambda`-order reachability, including the honest one-parameter remainder `Lambda^{19} Jdet/4`;
- closure-first incidence or any saturation `(-):Lambda^\infty:Jdet^\infty`;
- formal convergence of a coefficient series, or a Taylor realization;
- order two, maximum twelve, or JC2.

`RESULT.md`'s closing sentence, that the identity "supplies a unit-denominator deformation relation for the next mixed `Lambda<=19` syzygy-cokernel calculation," is a campaign-routing remark, not a theorem. Clearing a pure-coefficient local obstruction is compatible with a later mixed obstruction and does not decide it.

---

## Verdict

**PASS.**

The smallest failed identity is none. The strongest exact theorem that survives is the charged one: for the independently reconstructed unloaded normalized K00 rows `r1,...,r7` in `R=Q[d0,...,d5]`, with `I=(r1,...,r6)` and `m=(d0,...,d5)`,

```text
(63*d4+20)*r7 = sum_{i=1}^6 ui * ri
```

holds identically, `63*d4+20` is a unit in `R_m`, and therefore `r7 in I R_m`.
