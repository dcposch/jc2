# Hostile review: V43G4 exact total `5*t^6*a1^4` identity

Date: 2026-08-27
Reviewer: Grok 4.6 (xAI), adversarial algebra/custody, different-model lane
Charged producer: `cases/max12_812_order2_p0_total_rees_j2_a1_generic_rehom_v43g4_20260827/`
Prompt SHA-256:
`040af28fb9c9d94f8912b026e8c3fa0e05459b5b0f5d0f8eefaa21acd2d10b93`

**Overall: PASS at the exact claimed scope.**  An independent exact-`Q`
replay, regenerating the 59 literal total rows from the hash-pinned V43
compiler and reparsing all 58 frozen V43G3 Laurent multipliers under a
stricter fail-closed grammar than the producer, supports this statement
and no stronger one:

> In the literal total ring `S = Q[t, X19_total]`, `t = rho^2`, for the
> frozen ordered-`a1` grade-through-19 corpus,
> `5*t^6*a1^4 = sum_i H_i Tg_i`.
> Exactly eleven multipliers are nonzero, all on grades 11--15.
> The identity is an honest sparse polynomial equality.  It is not a
> cofactor-nonzero-at-zero certificate, because the left coefficient has
> `t`-valuation 6.

Do not promote this to an `a1^N U(t)` identity with `U(0) != 0`, to
chart closure, to `K+(rho)=(1)`, or to JC2.  The converter that would
raise the exponent from 4 to `4+6M` is a successor, and `M=104` is a
citation, not a replayed input.

---

## 0. Custody, constraints, and what was actually used

Session constraints honored: no Singular/Macaulay2 execution, no AWS
launch, no web sweep, no canonical-ledger edit, no contact with
`jc2-lean`.  Local work was hash recomputation of every freeze and
evidence path, a fail-closed reparse of all 58 Laurent files, one
independent call of the pinned V43 `reconstruct_rows` (134 s wall,
Python `Fraction` arithmetic), and exact sparse multiplication of the
four claimed layers.  The producer rehomogenizer was read, not executed
(it is AWS-gated).  The only repository file written is this report.

Git HEAD: `418e413593120d19e15e6546eb50c985f4b1f038`.  The charged G3/G4
trees are presently untracked; custody is the freeze/pin table below,
not git.

| Artifact | SHA-256 | Role |
|---|---|---|
| G4 preregistration | `20bce356839fef3b25746d7b5c895ab0a0f2dfcfb3223e1fc06624831a9ecdb4` | frozen question |
| G4 rehomogenizer | `62560313f046b8a7935852bc75e5ba5125c6db5441c19e5f75083a3c0951e902` | four-layer exact replay |
| G4 runner | `ed3779565ca39647bc6a181a9c1b47f482d4e7737993e0f5ab0a64e41bfa66d6` | r6b launch |
| G4 result | `ae7beed3e677a46bda82778ae6bbeb1a8aef74dcbf8db35df07f02d183b70015` | claimed identity |
| G4 freeze file | `777927795b59509c56c2d971b82db9be05ab7f33a7449b0f1947d28f4a201b91` | 133-entry harvest pin |
| G4 evidence manifest | `e64b8e8e3874ae02759a7ea8e3287d0cf1e09900fca472537b3d3ee4e28af18c` | 128-entry harvest |
| G4 result JSON | `e97ebd6a893e73d8e3751692b56300f0df230a75184f20b05d91282ac455e962` | derived telemetry |
| G4 certificate JSON | `e737b9ef129e5022c47100553d3a1725dbd6bc67e2486760e6d3d523db07b740` | serialized `H_i` |
| G3 result | `6db87ebacaa175c68dca5739dbad35390d36ff62ff914859c82a1d60e79270c4` | G4 pin |
| G3 freeze file | `8f60b30576e1712479e09cc01c3244c6ff5c7053c0d3cd08e9d4fbad8745ca45` | 83-entry G3 pin |
| G3 compiler result | `1c00aef261a3d674cb1b63f4fad18cf0121b9bcb6711a2103e893bab7a83758e` | 58/64/`ez9` census |
| G3 Singular script | `0bca5e57db93e620c8f1f9ad52ea50b3f16ab4d01ad0326cab96009bbe803893` | liftstd input |
| G3 compiler source | `7331343bb19b95ae3854218b85e00780826b413dbe4065fea59a3f8749bc6e7a` | G3 freeze entry |
| G2 freeze file | `bbb8b2d637be3458c0e67cfabbe3fa594ea521cb6a1151a5a242f937abf4c04d` | G3 pin |
| G2 result | `60b76bd4d3a8106a1e670073ae1f84218e1d62ae21187d79d75abf0bbcc48028` | G3 pin |
| G2 compiler result | `fac99098b36f5875b53c8d66439f34ca59b47e7f25a58f97dba1cb8cddd3806c` | G3 pin |
| G2 decision script | `7e3149d9ff89274e31c1068a51903dd9e2e716168141bd6286fa6b47d56328b3` | 58-row `Q(t)` ideal |
| G2 compiler source | `4ce93300474ec1a86cb9a435fbb3d780b3e121a946796a07f1cd0f8a73bd0a99` | G3 pin |
| V43 compiler | `0de6a2b279aeeab8c5a635c1d7658958f3f49f0f94f8473355d281cae9438b00` | literal regeneration |
| V35 | `843a66318dc36ecacee05f1df3616d36e375d8f93f714cf667b1fb67992543dc` | V43 pin, live-matched |
| V37 | `ba034c8cebaa27c5630872b9cf06d152e4577170486ac34ad7f695ead871845b` | V43 pin, live-matched |

Every row of this table was rehashed locally against current bytes and
matched the producer pin.  All 133 `FREEZE.sha256` entries matched.
All 128 `EVIDENCE.sha256` entries matched; the five freeze-only paths
are preregistration, result, rehomogenizer, runner, and the evidence
manifest itself.  All 83 G3 freeze entries matched, including all 58
individual Laurent multiplier files.  All 24 G2 freeze entries matched.

No producer PASS string was trusted as algebra.  The r6b stdout was
used only as a transcript of what the AWS Python process printed after
the independently audited input was hashed.  The four-layer identity
was replayed from the frozen multipliers and the regenerated literal
rows, not from that transcript.

---

## Verdict summary

| Attack | Charge | Verdict |
|---|---|---|
| 1 | Transitive custody: G3 freeze, 58 multipliers, V43 compiler, 59/66 and 58/64, unique `ez9`, AWS source manifest | **PASS**.  Harvest omits the remote source manifest; not an algebraic defect |
| 2 | Fail-closed Laurent parser; signs, parens, powers, rationals, `t`-only poles; quarantined matrix writes unused | **PASS** |
| 3 | Independent exact replay of all four layers | **PASS** |
| 4 | LCM 5, Laurent `t`-clearing 6, content 1, levels 3 and 4, zero dropped terms; not global minimality | **PASS**.  PREREG “15 and 20” is raw weight, not a second claim |
| 5 | Eleven named rows, source-row hashes, zero pivot, `Tg15_7` mutation; no aliasing/specialization/reconstructed last layer | **PASS**.  Producer mutation is a one-monomial product; independently strengthened |
| 6 | Weighted homogenization `wt(t)=0`, `wt(a1)=5`, residue mod 5, level-4 target; serialization cannot hide a failed replay | **PASS** |
| 7 | Converter boundary: `v=5 t^6`, `v(0)=0`; formula `4+6M`; what must be replayed before promotion | **PASS** as a correctly withheld gate |
| 8 | Scope firewall: frozen ordered-`a1` literal rows only | **PASS** |

**Smallest statement actually proved.**  There exist eleven explicit
polynomials `H_i ∈ Q[t, X19_total]` such that

```text
5 t^6 a1^4 = H_{11_2} Tg11_2 + H_{11_7} Tg11_7 + H_{12_2} Tg12_2
            + H_{12_7} Tg12_7 + H_{13_5} Tg13_5 + H_{13_7} Tg13_7
            + H_{14_5} Tg14_5 + H_{14_7} Tg14_7 + H_{15_3} Tg15_3
            + H_{15_5} Tg15_5 + H_{15_7} Tg15_7
```

as an equality of sparse maps in `S`, against the literal (not
dehomogenized) total rows of those names, with the `Tg19_2` pivot
multiplier identically zero.

**Smallest statement not proved.**  An identity `q a1^N ∈ J` with
`q(0) ≠ 0`.  That requires a separately exact special certificate
`a1^M − B = t H`, `B ∈ J`, composed by the converter of attack 7.

---

## 1. Attack 1 — transitive custody

### 1.1 G4 freeze, harvest, and lane

All 133 freeze paths exist and rehash.  `RESULT.json` and
`output/result.json` are byte-identical
(`e97ebd6a…e962`).  Lane metadata records

```text
stdout_sha256=e3478b5346b834ad64d7baafac40e87dd9196ae665885bceb3502d2f21daeac1
stderr_sha256=5d85bac03bf871837779560b343e61240e7954b9d1f8f8e7e34fba0b3240ab91
rc=0
```

matching the harvested stdout/stderr files.  `launcher.stdout` and
`launcher.stderr` are the empty-file digest `e3b0c442…b855`.  Lanes log:

```text
2026-08-27T11:24:13Z ..._exact_rehom_r6b_python rc=0
```

Python wall 249.54 s / 147,380 KiB RSS; no swap; exit 0.  Both under
the preregistered 64 GiB / 1 h cap.  No `FAIL_`, `Traceback`,
`Killed`, `out of memory`, or `error occurred` token occurs in the
run directory.  The runner would have exited 91 on those tokens, and
would have exited 125--128 on a non-Linux host, a wrong tag, a wrong
memory/wall cap, or a source-manifest mismatch.

Launch registration records

```text
tag=...v43g4_20260827T111531Z_exact_rehom_r6b
host=ip-172-30-0-106
start_utc=2026-08-27T11:20:04Z
memory_cap_kib=67108864
wall_seconds=3600
source_manifest_sha256=89a4b9a0e33ce84b8e3dda793d2ddd37ef384951ba6fa7b1d0cccf6d94305fe7
```

and `run_aws.sh` refuses to start unless that digest equals
`sha256sum AWS_SOURCE_MANIFEST.sha256` and `sha256sum -c` succeeds.
RESULT.md claims 755 files, 23 MiB, made read-only before launch.
The source tree itself is **not** in the r6b harvest.  Zero AppleDouble
`._*` files exist in the local G4 tree.

### 1.2 G3 freeze, 58 multipliers, and the G2 payload

G4's `verify_freeze()` walks the G3 freeze file
(`8f60b305…ca45`, 83 entries).  This review did the same walk:
mismatch 0, missing 0.  The 58 `generic_multiplier_NN_TgG_R.poly`
files are freeze entries.  Eleven of them are nonzero; 47 are the
two-byte file `0\n` (digest `9a271f2a…86aa`).  G3 stdout markers
required by G4 each occur once:

```text
V43G3_LIFTSTD_BASIS_REPLAY=1
V43G3_NONZERO_MULTIPLIERS=11
V43G3_GENERIC_UNIT_REPLAY=1
PASS_A1_GENERIC_QT_LIFT_V43G3
```

The two G3 `compiler_result.json` copies are byte-identical
(`1c00aef2…758e`).  Independently, the G2 decision script and the G3
lift script have **byte-identical** ring declarations and **byte-identical**
58 ideal entries (G3 then appends `liftstd`/`write` lines).  That is
the G3 flag `g2_ring_and_all_58_entries_byte_equal=true`, checked
here from the files rather than from the flag.

The quarantined Singular matrix writes

```text
generic_bezout_coefficients.matrix
generic_lift_transform.matrix
```

are the single byte `0`.  G3 RESULT.md already discloses this.  The G4
source never names `.matrix`, `generic_lift_basis`, or
`generic_bezout`.  The G3 basis file contains `(5*t^6)` — a unit in
`Q(t)`, consistent with the later cleared product, and also unused by
G4.

### 1.3 Literal census, unique `ez9`, reduced 58/64

Independent `reconstruct_rows` through the pinned V43 compiler
(`0de6a2b2…8b00`), which itself hash-pins V35 and V37 (live-matched):

```text
named source slots          70
nonzero total rows          59
positive variables          66  (includes a1, ez9)
rho=0 positive variables    65
general-only variables      [ez9]
unique ez9 occurrence       Tg19_2 : (3/8) t * a1 * ez9
pivot row hash              cc8957b85398036791e8193bc5864897412bdec6e30f2c363cce7bb345e31209
reduced rows                58  (Tg19_2 excluded)
reduced variables           64  (a1 and ez9 dropped)
```

All 58 `reduced_row_sha256` values in the G3 compiler result equal the
independently recomputed `total_hashes`.  The pivot hash matches.
There is no second `ez9` term.

G4 does not itself re-derive the G2/G3 `Q(t)` generators; it multiplies
the saved Laurent files against regenerated literal rows.  Stale V43
bytes would have failed the G4 `load()` hash check on AWS and fail
here.  They did not.

### 1.4 Mutable dependencies and the missing source manifest

The remote AWS source manifest is not harvested, so an auditor cannot
name the 755 files that were read-only at launch.  The algebraic
inputs that actually enter the identity — V43 compiler, G3 freeze, 58
multiplier files, G3 compiler result — are in the local tree, hash-pinned,
and were regenerated/reparsed here.  A post-run mutation of an unused
remote file could not have produced the hashed multipliers or the
hashed rows.

**Verdict: PASS.**  Repairable follow-up, not required to accept the
identity: harvest `AWS_SOURCE_MANIFEST.sha256`.  G3 itself has no
hostile-review file in `xmodel/`; that is not a hole in G4, because
this review independently multiplied the 58 frozen files and obtained
`1` (attack 3).  The G3 `liftstd` run was not re-executed.

---

## 2. Attack 2 — Laurent parser and quarantined writes

The producer parser is fail-closed on the grammar the G3 `write(C[i,1])`
files actually emit.  This review reparsed every file with an independent
grammar that is strictly tighter on two points: nested denominator
parens are rejected, and `t` is forbidden as a monomial factor (negative
`t` exponents may arise only from a denominator).  All 58 files parsed.
Findings:

- Zero files are exactly `0` plus one newline.
- Every nonzero file is a single line of signed rational monomials.
- First factor of every term is a scalar `[+-]?\d+( / denom )?`.
- Multi-factor denominators are parenthesized: `(5*t^4)`, `(t^5)`,
  `(5*t)`.  The unparenthesized form `4/5` occurs once (`Tg15_3`).
- Denominator factors are only decimal digits, `t`, or `t^N` with
  unsigned `N`.  No `t^(-N)` monomial syntax occurs; the parser would
  reject it (`\d+` is unsigned).
- Integer denominators that appear are only `{1, 5}`.
- Negative exponents occur only for `t`, and only via denominators.
- No file places `t` in the monomial (positive-power) part.
- Signs are carried on the scalar (`-4/(5*t^4)*…`, `4/5`).  Additive
  splitting is at depth-0 `+`/`-`.
- Variable names match `[A-Za-z_][A-Za-z_0-9]*` with optional
  unsigned `^N`.  Observed names: `cs1,cs2,e0,ell1,ell2,ell3,ell4,rs1,rs2`.

A leading variable without coefficient, a nested paren, a negative
non-`t` exponent, or `t` as a monomial factor would have failed both
parsers.  None occurred.

The two Singular matrix files are the byte `0` and are never opened.
G4 reads only the 58 individual `.poly` files named in
`compiler["multiplier_paths"]`, after taking `Path(path).name` against
the frozen G3 compiled directory.  Path-absolute AWS leftovers in the
JSON cannot redirect the read.

**Verdict: PASS.**

---

## 3. Attack 3 — independent four-layer exact replay

The producer AWS process is gated on `Amazon EC2` plus a registered
tag.  It was not run here.  The algebraic core was reimplemented
against the frozen files and the pinned V43 rows.

Let `C_i` be the parsed Laurent multiplier for reduced row `i`,
`Tg_i` the regenerated literal total row as a polynomial in
`Q[t, X]`, and `Tg_i(1)` that row with every `a1` exponent dropped
(ordinary `a1=1` dehomogenization).  Homogeneity of every total
monomial at its row grade, with `wt(t)=0`, implies that distinct `a1`
powers of the same remaining monomial cannot occur, so dropping `a1`
does not merge distinct terms.  Empirically: zero such collisions.

**Layer 1.**  `sum_i C_i · Tg_i(1) = 1` in `Q(t)[X]`, as sparse maps.
Live result: the one-term polynomial `{(): 1}`.

**Layer 2.**  Least common integer denominator of all `C_i`
coefficients is 5.  Least `t`-valuation of any monomial in any `C_i`
is −6.  Clearing `5 t^6` and removing integer content (attack 4)
gives primitive polynomials `D_i` with

```text
sum_i D_i · Tg_i(1) = 5 t^6.
```

Live result: `{(('t', 6),): 5}`.

**Layer 3.**  For each term of each `D_i`, keep the term iff
`grade(Tg_i) + σ(monomial) ≡ 0 (mod 5)`.  Zero terms are dropped.
The surviving product is again `5 t^6`.

**Layer 4.**  Homogenize every surviving term to the common maximum
level 4 by multiplying by `a1^{4 − level}`.  Multiply the resulting
`H_i` against the **original literal total rows** `Tg_i`, not against
`Tg_i(1)`, not against a reconstructed dehomogenization, and not
against the G2/G3 `Q(t)` generators.  Live result:

```text
{(('a1', 4), ('t', 6)): 5}
```

with zero other terms.  That is exactly `5 t^6 a1^4`.

The same layer-4 product was then replayed from the harvested
`total_homogeneous_multiplier_*.poly` files after an independent
polynomial parse.  Same one-term result.  The certificate JSON
`multipliers` map equals the in-memory `H_i` map, termwise.

**Verdict: PASS.**  Four sparse equalities, none of them a status
string.

---

## 4. Attack 4 — LCM, clearing, content, levels, dropped terms

Derived from the 58 serialized files and the regenerated grades, not
from RESULT.md:

| Quantity | Live value | Claim |
|---|---|---|
| rational denominator LCM | 5 | 5 |
| least Laurent `t` clearing | 6 | 6 |
| integer content of `5` and all cleared numerators | 1 | 1 |
| `q_t` after content | 5 | 5 |
| sigma-residue dropped terms | 0 | 0 |
| product levels (`(grade+σ)/5`) | `{3, 4}` | `{3, 4}` |
| corresponding raw sigma totals | `{15, 20}` | PREREG wording |
| used-row count | 11 | 11 |

Content is 1 because, among other terms, `Tg15_3 = 4/5` clears to the
integer 4, which is coprime to 5.  The valuation 6 is forced by
`Tg11_7`, whose leading term is `-352/(5 t^6) ell1^4`.  Per-row
levels:

```text
Tg11_2 : {3, 4}
Tg11_7, Tg12_2, Tg12_7, Tg13_5, Tg13_7,
Tg14_5, Tg14_7, Tg15_3, Tg15_5, Tg15_7 : {3}
```

So the only level-4 (raw weight 20) survivors are four `e0`-terms on
`Tg11_2`.  Everything else is level 3 and receives one `a1` at
rehomogenization.

PREREGISTRATION.md predicted “product levels 15 and 20”.  Those are
the raw sigma totals, not the integers the code stores after dividing
by `wt(a1)=5`.  The runner greps `V43G4_PRODUCT_LEVELS=3,4`.  The
algebra derives 3 and 4; the grep is a post-hoc stdout check, not a
hard-coded verdict inside the product.  This is documentation drift in
the preregistration, not a second identity.

These figures are **for these eleven multipliers**.  They are not a
proof that no other 58-tuple of Laurent polynomials witnessing
`sum C_i Tg_i(1) = 1` has smaller support or smaller pole order.  A
successor, not V43G4, tests global minimality.

**Verdict: PASS.**

---

## 5. Attack 5 — named rows, hashes, pivot, mutation, last-layer source

Used rows, in reduced-row order, not sorted by name:

```text
Tg11_2 Tg11_7 Tg12_2 Tg12_7 Tg13_5 Tg13_7
Tg14_5 Tg14_7 Tg15_3 Tg15_5 Tg15_7
```

All eleven have grades in `{11,12,13,14,15}`.  Raw term counts match
RESULT.json: 6, 7, 1, 4, 2, 2, 1, 1, 1, 1, 1.  Homogeneous `a1`
powers: `Tg11_2` has `{0,1}` (the level-4 `e0` terms keep `a1^0`);
every other used `H_i` is `a1^1` times a dehomogenized monomial.

Source-row hashes: all 58 `reduced_row_sha256` values plus the pivot
hash `cc8957b8…1209` match the independent `total_hashes`.  The pivot
multiplier is the empty polynomial, serialized as `[]` in the
certificate and as `"0"` in result JSON.  `Tg19_2` is absent from
`reduced_rows` and from the 58 multiplier files.  The unique `ez9`
term cannot contribute.

Last layer: `total_source_rows = ordinary_t_polynomial(by_name[name]["polynomial"])`
for `name in selected`, then `H_i * Tg_i`.  That is the regenerated
literal total row, with `t` unpacked from the `TPolynomial` values,
not a reconstruction from the G2/G3 dehomogenized generators and not
`dehom_a1` of the same row.  Compiler aliasing is blocked by
`load(V43, V43_SHA256, …)`.  Accidental `t=c` specialization is
absent: every coefficient is a `Fraction`.

### 5.1 The `Tg15_7` mutation is a weak producer control

Producer code, compressed:

```text
mutation_index = last used row          # Tg15_7
mutation_monomial = sorted(Tg15_7)[0]   # a1 * aa0 * ell1 * rs1 * t
residual = H_15_7 * {that monomial: 1}
```

It does **not** recompute `sum H_i Tg_i` against a coefficient-mutated
literal row.  It checks that one product of two nonzero sparse
polynomials is nonzero.  That is a support/sensitivity check, not a
full negative control, and it is not a target-only or tautological
mutation of `5 t^6 a1^4`.

Independently:

- The saved residual is the one-term polynomial
  `-96 a1^2 aa0 ell1 rs1 t^5`, digest
  `fdf66d5f6d37244ba5c598d301cc6ad0b3e1c6f05c92fb09b314a2d82563949b`,
  matching the harvest.
- Replacing the entire `Tg15_7` row by that monomial and replaying
  the full eleven-row sum yields a 124-term nonzero residual.
- Adding `+1` to the coefficient of that monomial on the literal
  `Tg15_7` row and replaying the full sum yields **exactly**
  `H_15_7 * monomial`.  So the saved residual is the genuine
  first-order sensitivity of the identity to that coefficient, even
  though the producer did not compute the full mutated sum.

No target-only mutation, no reconstructed last layer, no
specialization.  Repairable producer follow-up: persist the full-sum
residual of a one-coefficient mutation.  Not required to accept the
identity, which layer 4 already binds to the literal rows.

**Verdict: PASS.**

---

## 6. Attack 6 — weighted homogenization and serialization

Facts checked live against the V23 parser loaded by V43:

- `σ(t)` is defined to be 0 in G4 (`t` is not a parser name; calling
  `parser.sigma_weight("t")` would fail closed).
- `σ(a1) = 5`.
- Every monomial of every regenerated total row has sigma weight equal
  to the row grade.  So `Tg_g` is homogeneous of weight `g`.
- Residue projection keeps a `D_i` term iff `g + σ(monomial) ≡ 0
  (mod 5)`.  Dropped-term count 0, so there is no silent discard.
- Surviving levels are 3 and 4; homogenization is to exponent 4.
  Every `H_i` term then satisfies `σ(H_i) + grade(Tg_i) = 20`.
- The target `5 t^6 a1^4` has weight `0 + 20 = 20`.

Why the residue filter is the correct one, not an extra hypothesis:
after `a1=1`, a term of `Tg_g` that originally carried `a1^k` has
remaining weight `g − 5k`.  A multiplier term of weight `w` produces
product weight `w + g − 5k`.  The layer-2 target `5 t^6` has weight 0,
so only residue class `w + g ≡ 0 (mod 5)` can contribute.  Off-residue
terms of the `D_i` cannot appear in a weight-0 target; here there were
none to cancel.

Why rehomogenization recovers a total identity: `D_i · Tg_i(1) = 5 t^6`
and each row is homogeneous, so inserting `a1^{4−level}` into `D_i`
and restoring `a1` in `Tg_i` multiplies both sides by `a1^4`.  Layer 4
is the check of that argument, not a restatement of it.

Serialization cannot hide a failed in-memory replay:

1. The producer compares sparse maps **before** writing any `.poly`
   or JSON file.
2. `polynomial_text` emits every remaining term, sorted, with
   `Fraction` coefficients; the empty polynomial is `0`.
3. This review reparsed every harvested `.poly` file and obtained
   the in-memory maps, then remultiplied the `H_i` files against the
   literal rows and again obtained `{a1^4 t^6: 5}`.
4. The certificate JSON is a second, independently compared encoding
   of the same `H_i`.

A failed in-memory product would have raised, and a silently truncated
write would have failed the file-level remultiply.

JSON field `q_at_zero` is set to `unit_scalar` (5), i.e. the cofactor
in `v = t^s q` with `q = 5`.  In that notation `q(0) = 5 ≠ 0`.  The
full left coefficient `5 t^6` does vanish at `t=0`.  RESULT.md and
`promotion_gate` use the second reading and withhold promotion.  The
field name is easy to misread and should be `q_cofactor` or similar.
It is not a hidden claim that the chart is already closed.

**Verdict: PASS.**

---

## 7. Attack 7 — converter boundary

V43G4 proves `v a1^D ∈ J` with `v = 5 t^6`, `D = 4`.  Writing
`v = t^s q` gives `s = 6` and `q = 5`, so `q(0) = 5 ≠ 0` as a
polynomial in `t`, while `v(0) = 0`.  The chart is not closed.
RESULT.md states this; the runner outcome string is
`exact-total-identity-5-t6-a1-4-replayed-requires-special-converter`.

Conditional on a separately exact special identity

```text
a1^M − B = t H,     B ∈ J,
```

in the **same** ring `S` against the **same** literal rows, the
binomial identity `(a1^M)^s − (t H)^s ∈ J` gives

```text
q a1^{D + M s}
  = q a1^D (a1^M)^s
  ≡ q a1^D (t H)^s
  = (t^s q) a1^D H^s
  = (v a1^D) H^s
  ∈ J.
```

No nonzerodivisor hypothesis on `t` is used.  Substituting the live
numbers:

```text
5 a1^{4 + 6 M} ∈ J.
```

For the cited candidate `M = 104` this is exponent `4 + 6·104 = 628`,
coefficient 5, then rationally normalized to `a1^{628}`.  The
arithmetic `4+6*104=628` is correct.  **`M=104` is not an input of
V43G4.**  RESULT.md calls it “separately live”; that is a pointer, not
a replay.

What must be replayed before any promotion of a cofactor-nonzero-at-zero
certificate, against this frozen 59-row corpus:

1. An explicit special identity `a1^M − B = t H` with polynomial
   multipliers over `Q[t]`, `B` a combination of the literal total
   rows.  A certificate `a1^M ∈ J0` computed after setting `t=0` does
   **not** automatically supply such `B` and `H`.  The constructive
   `a1^104` candidate is not usable until that total-ring replay
   exists.
2. The generic identity of this review, already in hand:
   `5 t^6 a1^4 = sum H_i Tg_i`.
3. The binomial `(a1^M)^s − (t H)^s` as a polynomial identity, not as
   a Gröbner reduction.
4. The composed combination `5 a1^{4+6M} = (sum H_i Tg_i) H^s` plus
   the special contribution, serialized, with a one-coefficient
   mutation of a literal source row.
5. Hostile review of that converter run.  Then and only then a
   campaign statement `K+(rho)=(1)` for this frozen chart.

V42's field-point / branch identity is not a substitute for `B` and
`H`.  Even after (1)--(5) the theorem would still decide only this
ordered-`a1` grade-through-19 corpus.

**Verdict: PASS** as a correctly withheld gate.  The formula giving
exponent `4+6M` holds; the special input does not.

---

## 8. Attack 8 — scope firewall

Eligible to record, at the exact scope of the overall paragraph:

- the displayed eleven-row identity `5 t^6 a1^4 = sum H_i Tg_i` in
  the frozen ordered-`a1` literal total ideal through grade 19
  (indeed in its grade-through-15 subideal on the named rows);
- equivalently, after `a1=1`, the cleared identity `5 t^6 ∈ J|_{a1=1}`
  and the raw identity `1 ∈ J|_{a1=1}` over `Q(t)`;
- still provisional, `requires-special-converter`.

Not eligible, and not claimed by RESULT.md:

- terminal receiver theorem;
- source/landing coverage;
- `G2-PSC` or `G2-BD`;
- Gate T;
- order-two;
- maximum-twelve;
- JC2;
- unrestricted total ordered-chart closure;
- `a1^N U(t)` with `U(0) ≠ 0`;
- treating `a1^104`, or any other unreplayed special certificate, as
  already composed.

The producer firewall paragraph is accurate.  This review does not
widen it.

**Verdict: PASS.**

---

## Repairable, non-blocking

None of the following touches the sparse identity.

1. Harvest `AWS_SOURCE_MANIFEST.sha256` so the 755 read-only source
   paths are inspectable.
2. Correct PREREGISTRATION.md “product levels 15 and 20” to “raw
   sigma totals 15 and 20, stored levels 3 and 4”.
3. Rename JSON `q_at_zero` to a cofactor name, or store both `v(0)=0`
   and `q(0)=5`.
4. Persist a full-sum residual of a one-coefficient mutation of
   `Tg15_7`, not only `H * first_monomial`.
5. A successor, not a G4 repair, tests minimal support and minimal
   pole order among all Laurent witnesses of the generic unit.

---

## Disclosure

I read the G4 preregistration, result, freeze, rehomogenizer, runner,
and the complete r6b harvest; the G3 preregistration, result, freeze,
compiler, runner, compiler result, Singular script, all 58 Laurent
multipliers, and the quarantined matrix/basis files; the G2 freeze,
result, compiler result, and decision script; and the V43 compiler
through `reconstruct_rows`.  I rehashed every freeze, evidence, and
pin path listed in §0.  I executed one independent exact replay of
the four layers over Python `Fraction` arithmetic.  I did not run
Singular, did not launch AWS, did not edit `AUDIT.md` or `jc2-lean`,
and did not treat `a1^104` as a theorem.  This report is the only
repository file I created.
