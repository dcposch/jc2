# Hostile review: V43C5 V2 exact total `a1^628`

Date: 2026-08-27
Reviewer: Grok 4.6 (xAI), adversarial algebra/custody, different-model lane
Charged object:

- `cases/max12_812_order2_p0_total_rees_j2_a1_total_converter_v43c5_v2_20260827/`
- freeze file SHA-256
  `dab07efa6090152cb8e427992e871c2300c7131d2478c6645bffe9fc200046cd`
- charged proof circuit SHA-256
  `f8426bcf6bb4acbe4a2c12e1897588a7b8ce92bc02da84b7fc02d64d64c145e4`
- charged result SHA-256
  `215a64b27e3ea43fd3238158a5e07e686d3de4c7d12ff5bde0e691f916938299`

**Overall: the exact converter theorem is confirmed at exactly the
claimed scope.**  Independently reconstructing the 950-node arithmetic
DAG from the freeze-pinned record, regenerating the 70-slot literal
total corpus from the hash-pinned V43 compiler, replaying the charged
C4 certificate, and multiplying the charged G4 certificate against
those same literal rows, without calling producer `main` and without
treating the AWS transcript as algebra, supports this statement and
no stronger one:

> In the ordinary polynomial ring `S = Q[t, X19_total]`, for the frozen
> literal total raw ordered-a1 rows through grade 19, there is an exact
> 25-row identity `a1^628 = sum_j M_j(t,X) R_j(t,X)`.  Under the exact
> ring map `t |-> rho^2`, this is a pure total certificate: `N=628` and
> `W=0`.  There is no localization or division by `t`.

This is a new review of the combined identity.  The charged C4 and G4
reviews are used only as audited source-file identities.  Their PASS
strings are not inherited as a review of this converter.  Both source
identities were replayed independently in this session.

This does not prove a terminal-receiver chain map, source reachability,
normalized K00, the order-two/maximum-twelve case, or JC2.  K00
transport remains separately untyped.

---

## 0. Constraints, method, and what was actually used

Session constraints honored: no Singular/Macaulay2, no AWS launch, no
web sweep, no canonical-ledger edit, no contact with `jc2-lean`, no
reading of a different model's unpublished V43C5 V2 review.  Producer
`main` was not called (it is AWS-gated and is the four-minute charged
replay).  The only repository file written is this report.

Git HEAD: `418e413593120d19e15e6546eb50c985f4b1f038`.  The charged C5
V2 tree is presently untracked; custody is the freeze/pin table below,
not git.

Local work:

1. Rehash of the V2 freeze file and all 21 freeze lines; of the C4
   freeze (16/16) and G4 freeze (133/133); of the harvested r6b
   evidence manifest (12/12).
2. Canonical `ExprStore.from_record` reconstruction of all 950
   converter expression nodes from the frozen proof, including a
   bit-for-bit check that the first 732 nodes equal the charged C4
   expression table.
3. Independent exact-`Q` check of the universal sixth-power identity
   in dummy variables, and of `(tH)^6 = t^6 H^6`.
4. Syntactic walk of every final-multiplier DAG node against the
   claimed formula `C_j * Phi * a1^4` and `(H^6/5) * G_i`.
5. One independent call of the pinned V43 `reconstruct_rows` (134.94 s
   wall, peak RSS 214,672 KiB, one core, zero swap).  Every named-slot
   hash was recomputed from the regenerated literal polynomial.
6. Independent `replay_record` of the charged C4 DAG against V37
   rho-zero rows (0.42 s).
7. Coefficientwise fibre and exact-`t` bridge for all 16 used special
   rows (0.03 s).
8. Independent sparse multiplication of all 11 G4 multipliers against
   the regenerated total rows, checking
   `5*t^6*a1^4 = sum_i G_i R_i` exactly (sub-second, residual one
   monomial).

No random evaluation was used as evidence.

---

## 1. Custody

The freeze file itself hashes to the charged value
`dab07efa6090152cb8e427992e871c2300c7131d2478c6645bffe9fc200046cd`.
Every listed byte matched.

| Artifact | SHA-256 | Role |
|---|---|---|
| V2 freeze file | `dab07efa6090152cb8e427992e871c2300c7131d2478c6645bffe9fc200046cd` | 21-entry combined pin |
| V2 preregistration | `87723161a058858c3b8c2647d97537aefe93eac0d1f1b4b32ad386c61134acf2` | frozen converter question |
| V2 RESULT.md | `fa8504ac701c8b36c47a8178b7338b0f7fe18241c26e9f07feed2271de848953` | human summary; not algebra |
| V2 producer wrapper | `d1238596e57adda1d40d07b07ce69943c15a26386bd622cfb72408133087e52c` | additive census repair |
| V2 `run_aws.sh` | `17605768ea4b8972205a274bf8f91345c12336765c83aa2f102ed3eb456679e9` | r6b launch; hashes the AWS source manifest |
| V2 evidence manifest | `c9605ac68895530e6fcd0c1d2b0731e6482cfad89f8eb7bf6415d7c7a1e763d4` | 12-entry harvest |
| V2 result JSON | `215a64b27e3ea43fd3238158a5e07e686d3de4c7d12ff5bde0e691f916938299` | charged result; identical to `RESULT.json` |
| V2 proof circuit | `f8426bcf6bb4acbe4a2c12e1897588a7b8ce92bc02da84b7fc02d64d64c145e4` | 653,350-byte DAG |
| AWS source manifest | `50cbf25bd443df66944fe0d704e415d0c38d69de0e4058b352d34b4c6f6f1e87` | 1,989-file remote snapshot pin |
| V1 preregistration | `93328781388f06e47933e193a1be10a5d86b52f3edd422bde0228f38e5364ac0` | immutable predecessor question |
| V1 producer | `00d3912a283aaac5319f3e1a6e541ab5e149851c5569663d0b963bf8373d7c1a` | converter algebra; inherited `producer_sha256` |
| V1 fail-closed note | `5ebe13ef0cd6e981c798c90061e0314fc734a5a9a00c3852195ca6f63b5432d1` | pre-certificate failure narrative |
| V1 fail-closed meta | `16c699e01d2febb17a7cb6a78eb85164484533af5455278db7ed8337c9247536` | r6b `rc=1` metadata |
| V1 fail-closed stderr | `7ee399df9a76105ac321aff599fa7109ef062f9f44dc0f62d0031ad10de88d85` | `('literal total map', 59, 70)` |
| C4 freeze file | `67c1bb917506a01ee23101f652da0bba747480c6c576877a111b942aefc068f6` | 16-entry special pin |
| C4 proof | `3e0e80c0c9ab07803d60ea6b3284daeae6dbdeb858c6af875a1457174f5b0862` | `a1^104` DAG |
| C4 result JSON | `629a0763f784e2d18c5acc433313c486d51b141a91d933b01303fb7d7959393c` | C4 status/census |
| C4 review | `6a8ab201171dbafbb4fb9726910f9f4cb4dacab74856d8dc0d90d30c385b310e` | audited C4 source identity |
| G4 freeze file | `777927795b59509c56c2d971b82db9be05ab7f33a7449b0f1947d28f4a201b91` | 133-entry generic pin |
| G4 certificate | `e737b9ef129e5022c47100553d3a1725dbd6bc67e2486760e6d3d523db07b740` | `5*t^6*a1^4` multipliers |
| G4 result JSON | `e97ebd6a893e73d8e3751692b56300f0df230a75184f20b05d91282ac455e962` | G4 status/census |
| G4 review | `8a34756e4b3433f4b4817fb711d923360f188a66fd9ff2975d703375136658f1` | audited G4 source identity |

C4 producer `cd3e17b8…21c7d633` and G4 rehomogenizer `62560313…0951e902`
are the bytes loaded by the V1 algebra and are freeze-pinned through
the C4/G4 freezes.  V43 compiler `0de6a2b2…e9438b00` is the G4/V43 pin
used to regenerate literal total rows.

r6b transcript, used only as a record of what that Python process
printed after the independently hashed input: `rc=0` at
2026-08-27T13:38:01Z--13:42:00Z on `ip-172-30-0-106`, one core, zero
swap.  Stdout prints the V1 algebra token first, then the V2 wrapper
token, with `V2_PROOF_SHA256` and `V2_RESULT_SHA256` equal to the
charged hashes.  Empty harvested launcher stdout/stderr hash to
`e3b0c442…7852b855`.

### 1.1 Dual producer pin: transparent, not a promotion blocker

The V2 wrapper is `d1238596…33087e52c`.  It imports the immutable V1
algebra `00d3912a…8373d7c1a` by hash, patches only `total_context` /
`build_record` / `reconstruct_converter` for the 70/59/11 census, then
calls `BASE_MODULE.main()`.  V1 `main` writes `producer_sha256` equal
to the V1 file.  The wrapper then overwrites the result JSON with V2
status and records both hashes:

- `producer_sha256 = 00d3912a…` (base V1 algebra, as written by V1 `main`);
- `v2_producer_sha256 = d1238596…` (this wrapper);
- `base_v1_producer_sha256 = 00d3912a…` (explicit alias).

The freeze lists both files.  The result JSON lists both hashes.  The
wrapper refuses to run if the V1 producer, V1 preregistration, or V1
fail-closed stderr bytes have moved.  This is a naming quirk, not a
custody hole: the algebra that built the 950-node DAG is the freeze-pinned
V1 file, and the census repair that allowed the DAG to be built is the
freeze-pinned V2 wrapper.  Not a promotion blocker.

### 1.2 V1 is only a preserved pre-certificate failure

Charged V1 stderr ends at

```text
RuntimeError: ('literal total map', 59, 70)
```

in V1 `total_context`, after source-chain replay and before
`build_record`.  The two integers are the V43 census: 59 nonzero
literal total row records, 70 named-slot hashes.  V1 required
`len(total_hashes) == 59` and therefore stopped.  No converter
certificate was serialized.  V1 is evidence only of that software
assertion, not of any earlier mathematical identity.  V2's only
algebraic change is to record and check both censuses; the converter
identity, sixth-power schema, and mutation list are the V1 algebra.

### 1.3 C4 and G4 bytes charged by this freeze

C4 freeze 16/16 and G4 freeze 133/133 live-matched.  The C4 proof,
C4 result, G4 certificate, G4 result, and both completed reviews are
exactly the freeze-listed bytes.  Those reviews are not a review of
this composition.  The converter identities used below were replayed
from those bytes in this session.

### 1.4 AWS source manifest: packaging nit, not a polynomial defect

The freeze pins a local copy of the 1,989-file AWS source manifest
`50cbf25b…6f6f1e87`.  Launch registration records that same hash.
`run_aws.sh` requires the AWS tree's `AWS_SOURCE_MANIFEST.sha256` to
hash to the launched pin, then `sha256sum -c`s every listed file
before running.  That is the immutable remote-source statement.

Locally, the 1,989 files themselves are not harvested:

- 907 entries are AppleDouble `._*` files, all with one hash
  `7b7e7036…cb748c6c`, and none are present in the working tree;
- 917 listed paths are absent locally (the AppleDouble files plus a
  handful of top-level AWS helper manifests);
- of the files that do exist at the listed relative paths, 1,071
  hash-match and one live path has drifted:
  `cases/.../total_dvr_w30_v43_20260827/run_dehom_aws.sh`
  (`db09b260…` in the AWS snapshot, `fbaf04c6…` live).

That launcher is not a converter producer, not a row compiler, and not
a charged C4/G4 byte.  The converter producers, V43 compiler, C4/G4
certificates, and this proof are independently freeze-pinned and
live-matched.  The missing AppleDouble files and the one live drift
are a snapshot-packaging nit.  They do not underwrite, and do not
defeat, the polynomial theorem.

---

## 2. Literal corpus and `t = rho^2` map

Pinned V43 `reconstruct_rows` regenerated the corpus.  Independent
rehash of every named slot against `canonical_t_polynomial` matched
the frozen proof table with zero mismatches.

| Census | Live | Frozen proof / result |
|---|---:|---|
| Named slots `Tg10_1`..`Tg19_7` | 70 | 70 |
| Unique nonzero total rows | 59 | 59 |
| Zero slots | 11 | 11 |
| Positive variables | 66 | 66 |
| Rho-zero variables | 65 | 65 |
| General-only variable | `['ez9']` | `['ez9']` |

Zero slots, exactly as claimed:

```text
Tg10_1, Tg10_2, Tg10_3, Tg10_4, Tg10_5, Tg10_6, Tg10_7,
Tg11_4, Tg11_6, Tg12_6, Tg13_6
```

Every zero slot hashes to the canonical empty encoding `json.dumps([])`,
SHA-256

`4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`.

`ez9` is present in the 66-variable total alphabet and absent from the
65-variable rho-zero alphabet.  `rho` is absent from both: it has been
compiled out.  `t` is not one of the 66 `X`-variables; it is the
ordinary-ring parameter coming from even `rho`-degree.

The source of the map is V43 `total_to_t`, executed inside
`reconstruct_rows` for every named slot:

- odd `rho` exponent is fail-closed (`fail(("odd rho exponent", ...))`),
  not dropped;
- even exponent `rho^{2k}` becomes `t^k`;
- each face is checked for exact sigma-weight homogeneity at its grade;
- the `rho=0` specialization of each total face is asserted equal to
  the frozen V37 rho-zero row (70 bridges).

Live regeneration raised no odd-`rho` failure, leaked no `rho` into
any `t`-form monomial, and matched all 70 frozen hashes.  That is the
justification that the compiler encodes `t = rho^2` rather than an
unrelated parameter.  After the map, the identity is already in
`Q[t, X19_total]`; substituting `t |-> rho^2` cannot reintroduce a
nontrivial `W` because the target is the monomial `a1^628`.

Largest regenerated total rows (ordinary-`t` term counts): `Tg19_7`
2011, `Tg19_5` 1445, `Tg18_7` 1112.  Smallest nonzero: several grade-11
rows with one term.  Max `t`-degree in the rows themselves is 4;
G4 multipliers supply the remaining `t`-powers on the left-hand side
`t^6 a1^4`.

---

## 3. Source identities and bridge

### 3.1 C4, independently replayed

Ring: `Q[X19_rho0]`, 65-variable ordered-a1 alphabet, 51 nonzero named
rows.  Charged proof: 732 expression nodes, 71 derivation nodes, final
target `{a1^104: 1}`, 16 surviving labels, all literal rows.

`replay_record` against independently loaded V37 rows returned
`final.target == a1^104`, 16 labels equal to the frozen
`final_certificate.terms`, and those labels a subset of the 51 named
rows.  Labels:

```text
Tg11_1, Tg12_1, Tg12_2, Tg13_1, Tg13_2, Tg13_4,
Tg14_1, Tg14_2, Tg14_3, Tg14_4, Tg15_3,
Tg16_5, Tg16_6, Tg17_5, Tg18_6, Tg19_7
```

The converter DAG's first 732 expression nodes are identical to this
C4 table.  The C4 multiplier roots used below are exactly those 16
committed roots.

### 3.2 G4, independently multiplied

Ring: `S = Q[t, X19_total]`.  Charged certificate identity
`5*t^6*a1^4 = sum_i H_i Tg_i`, `t_valuation=6`, `q_t=5=q_at_zero`,
exactly 11 multipliers, no negative exponents, all integer
coefficients.  Direct sparse multiply of those 11 polynomials against
the regenerated total rows produced the one-monomial polynomial
`5 t^6 a1^4`.  Independent `assert_equal` held.

Dividing by 5 is legal in `Q`: `generic_scale = 1/5` and
`(1/5)*q_t = 1`.  No `t` appears in any denominator.  The normalized
identity is `t^6 a1^4 = sum_i (G_i/5) R_i(t)` in `S`.  The converter
DAG's `generic_multiplier_roots` (nodes 780--790) are bit-identical to
the G4 certificate polynomials.

Used G4 labels:

```text
Tg11_2, Tg11_7, Tg12_2, Tg12_7, Tg13_5, Tg13_7,
Tg14_5, Tg14_7, Tg15_3, Tg15_5, Tg15_7
```

### 3.3 Coefficientwise bridges, including exact divisibility by `t`

For every used special label, independently, in the same ordinary-`t`
alphabet:

1. `fibre := R_j(t)|_{t=0}` equals the C4 rho-zero row as polynomials;
2. `R_j(t) - fibre` has no `t^0` term (else `divide_exact_t` fails);
3. `fibre + t * Delta_j` equals `R_j(t)` coefficientwise.

| Row | `\|Delta\|` | `\|R(t)\|` | `\|R(0)\|` |
|---|---:|---:|---:|
| Tg11_1 | 0 | 1 | 1 |
| Tg12_1 | 0 | 3 | 3 |
| Tg12_2 | 2 | 5 | 3 |
| Tg13_1 | 1 | 10 | 9 |
| Tg13_2 | 5 | 14 | 9 |
| Tg13_4 | 2 | 4 | 2 |
| Tg14_1 | 2 | 21 | 19 |
| Tg14_2 | 11 | 32 | 21 |
| Tg14_3 | 21 | 39 | 18 |
| Tg14_4 | 5 | 12 | 7 |
| Tg15_3 | 41 | 87 | 46 |
| Tg16_5 | 168 | 245 | 77 |
| Tg16_6 | 22 | 44 | 22 |
| Tg17_5 | 300 | 477 | 177 |
| Tg18_6 | 89 | 229 | 140 |
| Tg19_7 | 1459 | 2011 | 552 |

`Tg11_1` and `Tg12_1` are genuinely `t`-free: `Delta = 0`, and the
converter DAG records `delta_root = h_term_root = 0` for both.  The
hash-consed `delta_sum` therefore has 14 rather than 16 summands.
That is correct, not a dropped row.

### 3.4 Bridge sign

DAG node 760 is `sum_j C_j Delta_j`.  Node 761 is `Scale(760, -1)`,
which is `H`.  Node 764 is `t * H = y`.  Therefore

```text
sum_j C_j R_j(t)
  = sum_j C_j (R_j(0) + t Delta_j)
  = a1^104 + t * (sum C_j Delta_j)
  = x - t H
  = x - y.
```

The committed `bridge_sign` is `[-1, 1]`.  The opposite sign would
produce `x + y` and the sixth-power schema would not return `x^6`.

---

## 4. Circuit composition

This is the load-bearing point.  `final_sum_root=941`,
`schema_rhs_root=947`, and `target_root=949` are three distinct
hash-consed nodes.  That is expected: distributivity and the two
source identities are derivation rules, not DAG identifications.
The question is whether the frozen record plus the checked source
identities plus the exact sixth-power schema is a complete typed
derivation of

```text
sum M_j R_j = a1^4 ((x-y) Phi + y^6) = a1^4 x^6 = a1^628.
```

It is.  The producer annotates the equalities; the derivation below
is independent of those strings.

### 4.1 Independent universal identity

In `Q[x,y,z]`, with `Phi = sum_{k=0}^{5} x^{5-k} y^k`, the sparse
identity

```text
z x^6 = z ((x-y) Phi + y^6)
```

holds with both sides equal to the monomial `z x^6`.  Equivalently
`x^6 - y^6 = (x-y) Phi`.  Separately, `(t H)^6 = t^6 H^6` in
`Q[t,H]`.  These are exact polynomial identities, not evaluations.
Substitution of `(x,y,z) = (a1^{104}, tH, a1^4)` is therefore legal
in any `Q`-algebra, including `S`.

The converter DAG builds the substituted right-hand side explicitly:

| Node | Construction |
|---:|---|
| 762 | `x = a1^{104}` |
| 763 | `t` |
| 761 | `H = -sum C_j Delta_j` |
| 764 | `y = t H` |
| 765,767,770,773,775,776 | `x^5`, `x^4 y`, `x^3 y^2`, `x^2 y^3`, `x y^4`, `y^5` |
| 777 | `Phi` |
| 778 | `a1^4` |
| 779 | `H^6` |
| 942 | `-y` |
| 943 | `x-y` |
| 944 | `Phi (x-y)` |
| 945 | `y^6` |
| 946 | `(x-y) Phi + y^6` |
| 947 | `a1^4 * 946` = `schema_rhs` |
| 948 | `x^6` |
| 949 | `a1^4 x^6` = `target_root` |

Frozen `target` is the encoded monomial `a1^{628}`.  Exponent
`4 + 6*104 = 628` is the only integer compatible with the two source
exponents and converter power 6.

### 4.2 Final multipliers, walked from the frozen DAG

Overlap of the 16 C4 labels with the 11 G4 labels is exactly
`{Tg12_2, Tg15_3}`.  Union has 25 labels, equal to
`final_multiplier_roots` and to the result's `final_rows`:

```text
Tg11_1, Tg11_2, Tg11_7, Tg12_1, Tg12_2, Tg12_7,
Tg13_1, Tg13_2, Tg13_4, Tg13_5, Tg13_7,
Tg14_1, Tg14_2, Tg14_3, Tg14_4, Tg14_5, Tg14_7,
Tg15_3, Tg15_5, Tg15_7, Tg16_5, Tg16_6, Tg17_5, Tg18_6, Tg19_7
```

Hash-cons flattening of `Mul` was expanded and compared to the C4
multiplier roots and to `Phi=777`, `a1^4=778`, `H^6=779`,
`Scale(G_i, 1/5)`:

- 14 C4-only rows: `M_j` is `Mul` of `flatten(C_j)` with `{Phi, a1^4}`.
  Every factor list matched the C4 root bit for bit.
- 9 G4-only rows: `M_i = Mul(H^6, Scale(G_i, 1/5))`.
- 2 coincident rows: `M` is `Add` of the C4-form and the G4-form,
  once.  `Tg12_2` is nodes `(793, 812)`; `Tg15_3` is `(801, 825)`.

No row is listed twice.  No extra label appears.  That is exactly the
registered formula.

### 4.3 Typed derivation

Write `x = a1^{104}`, `y = t H`, `Phi` as above.  All steps are in `S`.

1. **C4, as a derivation rule, plus the 16 fibre equalities.**
   `sum_{C4} C_j R_j(0) = a1^{104} = x`.
   DAG: `special_fibre_sum_root=863` is that 16-term sum
   (the two `t`-free rows share the same summands with the total lift).
2. **16 coefficientwise bridges plus finite distributivity.**
   `sum_{C4} C_j R_j(t) = x + t sum C_j Delta_j`.
   DAG: `total_lift_sum_root=892` versus
   `bridge_expanded_root=894 = special_fibre + t * (sum C Delta)`.
   These are different nodes; equality is the ring axiom on a
   16-term explicit sum, each term of which was checked.
3. **Definition of `H` and `y`.**
   `H = -sum C_j Delta_j`, `y = t H`, so the previous display is
   `x - y`.
4. **G4, as a derivation rule, plus the scalar `1/5` in `Q`.**
   `sum_{G4} (G_i/5) R_i(t) = t^6 a1^4`.
   DAG: `generic_normalized_sum_root=915`, 11 terms, each
   `Scale(G_i, 1/5) * R_i`.
5. **Definition of `M_j`, plus finite distributivity on 25 terms,
   with the two coincident labels already added.**
   ```
   sum M_j R_j
     = a1^4 Phi * sum_{C4} C_j R_j(t)
       + H^6 * sum_{G4} (G_i/5) R_i(t)
     = a1^4 Phi (x-y) + H^6 t^6 a1^4.
   ```
   DAG: `final_sum_root=941` is the 25-term sum `M_j R_j`.
6. **Commutativity, independently checked.**
   `H^6 t^6 a1^4 = a1^4 (t H)^6 = a1^4 y^6`.
7. **Substitution of the universal identity.**
   `a1^4 ((x-y) Phi + y^6) = a1^4 x^6 = a1^{628}`.
   Left side is node 947; right side is node 949; both are `a1^4`
   times a polynomial that the dummy-variable identity proves equal.

No localization, no division by `t`, no unspecified completion, and
no untyped radical.  The derivation edges that are not hash-cons
identifications are exactly the ones the prompt names as derivation
rules (C4, G4, distributivity) plus the independently checked
sixth-power schema and commutativity of `t` with `H`.  That is a
complete typed derivation, not an unproved annotation.

---

## 5. Replay of the 950-node record, and the nine controls

`ExprStore.from_record` rebuilt all 950 nodes canonically (ops
`{Sparse:173, Scale:178, Mul:445, Add:140, Pow:14}`), then froze.
Bootstrap nodes 0 (zero) and 1 matched.  No negative exponents in any
`Sparse` leaf.  Every committed converter root listed in section 4
exists and has the stated operation.  Original C4 prefix length 732
matches `original_c4_expression_node_count`.

The nine registered controls, classified:

| Control | What it actually hits | Mathematical content |
|---|---|---|
| wrong bridge sign `+1` | reconstruct gate `bridge_sign != -1`, before any rebuild | The sign is load-bearing (§3.4).  The same mutation would also miss committed `h_root=761`.  Metadata-first, not identity-empty. |
| `1/5 -> 1/4` | gate `generic_scale * q_t != 1` | Would also miss every `Scale(G_i, 1/5)` in the 11 G4 contributions.  Metadata-first. |
| power `6 -> 5` | gate `power != 6` | Would change `Phi` and `H^6` and break `4+5*104=524 ≠ 628`.  Metadata-first. |
| target `628 -> 627` | gate `target_exponent != 628` | Frozen `target` is still `a1^{628}`; the subsequent `assert_equal` against `a1^{627}` would fail.  Metadata-first. |
| delete final `Tg19_7` multiplier | `expected_terms != record['final_multiplier_roots']` | Direct commitment of the 25-row support.  `Tg19_7` is C4-only and the largest total row.  Identity-level. |
| literal `Tg15_7` generic corruption | G4 direct multiply after `R += 1` on one monomial | Not routed through `reconstruct_converter`.  Tests the G4 identity's dependence on that row (independently, `G= -96 a1 t^4` times a 124-term row).  Identity-level. |
| literal `Tg19_7` special-fibre corruption | `specialize_t0` no longer equals the C4 row | Not routed through `reconstruct_converter`.  Tests the fibre equality used in every special bridge.  Identity-level. |
| delete one zero-row name | V2 `validate_v2_census` | Census complement, not the converter identity.  Additive V2 control, as advertised. |
| corrupt one zero-row hash | V2 `validate_v2_census` | Same: metadata of the 11-slot zero complement. |

The last two tests only the V2 census, not `sum M_j R_j = a1^{628}`.
That is a documented additive gate, not a missing algebraic control.
The first four are metadata-first but constrain quantities that the
DAG also commits.  The middle three test the identity or its
row-level hypotheses.

---

## 6. Scope firewall

Confirmed statement, and only this statement:

`a1^{628}` lies in the ideal generated by the frozen literal total raw
ordered-a1 rows through grade 19, in `Q[t, X19_total]`, hence also in
`Q[rho, X19_total]` after `t |-> rho^2`, with `W=0`.

Not proved, not claimed, and not to be inferred:

- a terminal-receiver chain map;
- source reachability of these rows;
- identification of this ideal with normalized K00;
- the order-two / maximum-twelve case;
- JC2;
- K00 transport, which remains separately untyped.

Using 25 of 59 nonzero rows is legitimate membership: a subcollection
that already produces `a1^{628}` produces it in the 59-row ideal.
It is not a claim that every unused named row is necessary, nor that
`Tg19_7` is irredundant.

---

## 7. Nonblocking custody and control nits

None of the following is a theorem blocker.

1. Result JSON `producer_sha256` remains the V1 file.  The V2 wrapper
   hash is in `v2_producer_sha256`.  Both are freeze-pinned (§1.1).
2. Local copy of the 1,989-file AWS source manifest is the manifest
   text, not a replayable source tree: 907 AppleDouble entries absent,
   one live drift in `run_dehom_aws.sh`.  Remote `sha256sum -c` is the
   custody statement for that snapshot (§1.4).
3. AWS stdout prints the V1 PASS token before the V2 wrapper overwrites
   the result JSON.  The charged result hash is the post-overwrite file.
4. Result field `general_only_nonzero_rows=59` is V43's count of
   nonempty `t`-forms, not a count of rows that mention `ez9`.  The
   sole general-only *variable* is `ez9`.  Naming leftover from V1.
5. Four of nine mutations are rejected by hardcoded reconstruct gates
   before the corresponding DAG commitments are rechecked.  The
   commitments exist and would also reject.  Two V2 mutations test
   only the zero-row census.

No mathematical defect was found.

---

GROK_CONFIRMED_TOTAL_A1_628_V43C5_V2
