# Hostile review: V43C4 exact rho-zero `a1^104`

Date: 2026-08-27
Reviewer: Grok 4.6 (xAI), adversarial algebra/custody, different-model lane
Charged objects:

- `cases/max12_812_order2_p0_total_rees_j2_a1_constructive_circuit_rebased_factor_v43c4_20260827/`
- `FREEZE.sha256`
  `67c1bb917506a01ee23101f652da0bba747480c6c576877a111b942aefc068f6`
- producer
  `replay_constructive_circuit_rebased_factor_v43c4.py`
  `cd3e17b8b08617fb6d576d36313e8d08ec0d488bc63f375d62d11da321c7d633`
- proof
  `evidence/r6b/output/a1_104_exact_derivation_dag_rebased_factor.json`
  `3e0e80c0c9ab07803d60ea6b3284daeae6dbdeb858c6af875a1457174f5b0862`
- result JSON
  `evidence/r6b/output/result.json` (identical to `evidence/r6b/RESULT.json`)
  `629a0763f784e2d18c5acc433313c486d51b141a91d933b01303fb7d7959393c`
- precursor factor diagnostic
  `cases/max12_812_order2_p0_total_rees_j2_a1_constructive_circuit_factor_diagnostic_v43c3f_20260827/evidence/r6b/output/factor_expansions.json`
  `b9ebbaa4d73c12705096cad73a1c9e3b5b7a4c633a9dc94d7eaa86ff3d42b0cc`
- reviewed predecessor invalidation
  `xmodel/max12-812-order2-p0-total-rees-j2-a1-constructive-cascade-invalidation-v43c2-hostile-review-grok-20260827.md`
  `008e0d524147c1b28af00b9b2d6f1f099750d6f0ea2aebfeb80e1a0aee6fd8cb`

**Overall: the exact theorem is confirmed at exactly the claimed
scope.**  Independently reconstructing the arithmetic DAG from the
freeze-pinned producer and frozen 51-row corpus, without calling
producer `main` and without treating the AWS transcript as algebra,
supports this statement and no stronger one:

> In the ordinary polynomial ring `Q[X19_rho0]` on the frozen
> 65-variable ordered-a1 alphabet, the 51 named raw rows through
> grade 19 generate an ideal containing `a1^104`.  The serialized
> certificate is an exact unsplit arithmetic DAG: 732 expression
> nodes, 71 derivation nodes, 29 checkpoints, final target the
> monomial `a1^104`, and 16 surviving labels that are literal raw
> rows.

This does not resume a total-`rho`, saturated-Rees, or converter
exponent `4+6*104=628` theorem.  Those remain firewalls.  The
predecessor invalidation of the uncorrected V43C1/C2 tree is
untouched: that tree still is not a certificate.  This successor
repairs the crossed `assume:e1` obstruction by an exact change of
basis before the cubic `ell1` clear, then deletes three leftover
assumption multipliers only after a literal direct-factor expansion
to the zero polynomial over `Q`.

---

## 0. Constraints, method, and what was actually used

Session constraints honored: no Singular/Macaulay2 execution, no AWS
launch, no web sweep, no canonical-ledger edit, no contact with
`jc2-lean`, no reading of unrelated same-round model reports.  The
only repository file written is this report.  The charged predecessor
invalidation report was read because it is a charged pin.

Git HEAD: `418e413593120d19e15e6546eb50c985f4b1f038`.  The charged C4
tree is presently untracked; custody is the freeze/pin table below,
not git.

Local work:

1. Rehash of every C4 freeze line, the freeze file itself, the C2
   invalidation freeze (39 lines), and the live C1 → V42 → V37 → V23
   row-loader chain, including V42's four input pins and V37's later
   grade-16..19 result pins.
2. Import of the freeze-pinned C4 producer
   (`cd3e17b8…21c7d633`) with `require_aws` / `main` never called.
   Rows were loaded through pinned V42 → V37, which rehashed all 70
   row files before returning.
3. Canonical reconstruction of all 732 expression nodes from the
   frozen record via `ExprStore.from_record`, then a full
   `replay_record` of all 71 derivation nodes against those rows.
4. A second reconstruction via `build_proof` from the same pinned
   producer and rows, compared bit-for-bit to the frozen expression
   table, derivation table, checkpoints, and final certificate.
5. Independent memoizing expansion, using only V42
   `add`/`multiply`/`scale`/`power`, of prune factors 427, 401, 399
   and of the attack node 371; a second producer-style
   `expand_exact` walk used only to compare telemetry.
6. Coefficientwise expansion of the rebase identities and of the
   universal `ClearPower` / `CombineBranches` schemas in the V42
   ring, including both signed-`4` mutations.
7. Independent replay of every registered mutation against the
   frozen record.

No AWS process was started.  The harvested r6b stdout/stderr/meta
were treated as a transcript of what that Python process printed,
not as algebra.  The algebra below is from the reconstructed DAG.

---

## 1. Custody

Every C4 freeze line was rehashed against current bytes.  All 16
matched.  The freeze file itself hashes to the charged value
`67c1bb917506a01ee23101f652da0bba747480c6c576877a111b942aefc068f6`.
The predecessor invalidation report hashes to the charged value
`008e0d524147c1b28af00b9b2d6f1f099750d6f0ea2aebfeb80e1a0aee6fd8cb`.

| Artifact | SHA-256 | Role |
|---|---|---|
| C4 freeze file | `67c1bb917506a01ee23101f652da0bba747480c6c576877a111b942aefc068f6` | 16-entry pin |
| PREREGISTRATION.md | `43a24404df011e797ec1c31ae5dfcd9bfcd0eb75bf6c955abccb9bc15582f49f` | frozen question `a1^104 in I0` |
| live C4 producer | `cd3e17b8b08617fb6d576d36313e8d08ec0d488bc63f375d62d11da321c7d633` | freeze-pinned DAG builder |
| run_aws.sh | `3dae8bf783b32f1e299d74b6fb3033ca5679719def955c1d20cd6d48e46e158f` | freeze-pinned launcher |
| RESULT.md | `604c39f9cfb3071ecc02906a18b37284ee889c3c762ba31fc6938e92fab924b7` | human summary; not algebra |
| proof JSON | `3e0e80c0c9ab07803d60ea6b3284daeae6dbdeb858c6af875a1457174f5b0862` | serialized certificate |
| result JSON | `629a0763f784e2d18c5acc433313c486d51b141a91d933b01303fb7d7959393c` | census/status; matches `RESULT.json` |
| EVIDENCE.sha256 | `88cad66d11b885197437e87350709fd81cff887421332d1ff090461fd3e1a1b3` | harvested r6b manifest |
| V43C3F diagnostic | `b9ebbaa4d73c12705096cad73a1c9e3b5b7a4c633a9dc94d7eaa86ff3d42b0cc` | precursor expansions |
| C2 INVALIDATION.md | `dbea733345b2a707ee5834b90889eca6b41013b6694786317f54362e97d96b89` | C4 pin; negative predecessor |
| C2 invalidation freeze | `8c3f2ecab6b16ee9c6e3c338f9f88883a33e20baf2cf7aabe69c0bdfca9bd787` | 39-entry pin, all live |
| C2 FREEZE.sha256 | `10217738bc86e415050b667f226907b891bf2bb8e94e6f331fad8939bc562abe` | C2 invalidation-freeze entry |
| C1 source | `af590ff872552944528dda41497329e1b1534cc211290d622034defd70bac2ca` | C4 pin, live-matched |
| V42 replay | `f4ec72933793bf08aabc600df7cdcd47b8de2c54f45c0d30341e13ac0b676459` | C1 pin, live-matched |
| V42 Sol | `5d4c42fff1ad563586e8ae8736c3938efb1ae48467dfab96ae7fd9b861e7037f` | C1 pin, live-matched |
| V42 hostile review | `a4f6b93181526cd8907c6412faeef2ed2e69012a5820e939079ba4cf891f3439` | C1 pin, live-matched |
| V37 loader | `ba034c8cebaa27c5630872b9cf06d152e4577170486ac34ad7f695ead871845b` | V42 pin, live-matched |
| V23 parser | `14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501` | V37 pin, live-matched |
| V23 RESULT.json | `ce4d0adbbe94e1337bed5047da0417e3b17cb86530715fb62316086cabd14641` | V37 pin, live-matched |
| predecessor review | `008e0d524147c1b28af00b9b2d6f1f099750d6f0ea2aebfeb80e1a0aee6fd8cb` | charged C2 invalidation review |

All four V42 input pins consumed by `load_v42` also matched.  V37's
four later compiled-result pins (grades 16, 17, 18, 19) matched.
The V37 loader accepted the closed census **51 nonzero rows / 70
files / 65 positive variables**, with `rho` and `ez9` absent.  The
frozen proof's `row_sha256` table equals the live loader table.
Eleven empty row files (`Tg10_*`, `Tg11_4`, `Tg11_6`, `Tg12_6`,
`Tg13_6`) share one empty-content hash; that is the V37 empty-file
census, not a C4 defect.

Empty harvested AWS launcher stdout/stderr hash to
`e3b0c442…7852b855`, the SHA-256 of the empty byte string.  Every
file under `evidence/r6b/` except the manifest itself is listed in
`EVIDENCE.sha256` and live-matched.

Row-specialization leaves in the reconstructed DAG use the V42
divided difference, and the kernel asserts
`P = P|_(x=v) + (x-v) Q` coefficientwise before committing each
leaf.  That is the same identity already used by the reviewed
C1/V42 chain.

### 1.1 Producer-byte gap, closed for the charged algebra

Launch registration quotes an AWS source-manifest SHA-256
`27f42f0f280ea30101d6f5aab193953ee0581eefc59ad673f9b398e1b86cd89f`.
That hash is **not** a C4 freeze entry; `AWS_SOURCE_MANIFEST.sha256`
and the AWS source tarball are not in the harvested case directory.
The freeze instead pins the live producer `cd3e17b8…21c7d633`.

This is a real snapshot gap, not a mathematical one.  Locally
calling `build_proof` on the freeze-pinned producer against the
pinned rows reconstructed the frozen expression table, derivation
table, checkpoints, and final certificate bit for bit.  The missing
AWS tarball therefore does not underwrite, and does not defeat, the
exact theorem.  Historical V43C3 producer bytes (the 4-GiB OOM
predecessor) are also not freeze-pinned; V43C4 is a complete
successor and V43C3F is pinned only as a diagnostic.

---

## 2. Independent replay of the serialized proof

`replay_record` was invoked on the frozen JSON against independently
loaded rows and independently reconstructed generators.  Producer
`main` was not called.

| Check | Result |
|---|---|
| Expression nodes | 732, ops `{Sparse:106, Scale:165, Mul:329, Add:129, Pow:3}` |
| `from_record` canonical rebuild | identical to the frozen table; store then frozen |
| Negative exponents in Sparse leaves | none |
| Derivation nodes | 71: `RowSpecialize 26`, `Scale 16`, `Mul 10`, `ClearPower 9`, `Add 5`, `CombineBranches 3`, `RebaseAssumptions 1`, `PruneZeroFactor 1` |
| `PruneZeroTerms` nodes | **zero** (the C2 crossed-label prune is gone) |
| Checkpoints | 29, every committed target equal to the named monomial |
| Final proof index | 70 |
| Final target | `{a1^104: 1}` exactly |
| Final labels | 16, all literal named rows, no assumption labels |
| `build_proof` vs frozen record | expression, derivation, checkpoints, final certificate identical |

Final labels, matching the claimed list:

```text
Tg11_1, Tg12_1, Tg12_2, Tg13_1, Tg13_2, Tg13_4, Tg14_1, Tg14_2,
Tg14_3, Tg14_4, Tg15_3, Tg16_5, Tg16_6, Tg17_5, Tg18_6, Tg19_7
```

Seventeen distinct rows appear as `RowSpecialize` leaves.  The extra
leaf is `Tg15_4`, consumed as the `rel_rs2` relation and not retained
in the final certificate.  Using a subset of the 51 named rows is
legitimate: if those rows already produce `a1^104`, so does the
51-row ideal.  This is not a claim that every unused named row is
algebraically necessary, and it is not a claim that `Tg19_7` is
irredundant (section 6).

Checkpoints include the repaired right branch:

| checkpoint | proof | target |
|---|---:|---|
| `a18 modulo ell1` | 18 | `a1^18` |
| `a18 rebased modulo e0 G Q0 ell1` | 61 | `a1^18` |
| `a56 modulo e0gq` | 62 | `a1^56` |
| `a57 modulo e0g` | 63 | `a1^57` |
| `a46 modulo e0e1` | 56 | `a1^46` |
| `a103 modulo e0` | 66 | `a1^103` |
| `global a104` | 70 | `a1^104` |

The proof record itself commits `producer_sha256=cd3e17b8…`,
matching the freeze pin, and commits the C1 / C2 / C3F pins listed
in section 1.

---

## 3. `RebaseAssumptions`, coefficientwise

Generator conventions in the freeze-pinned producer, independently
rebuilt:

```text
G  = e1 - 4*a1*ell1
Q0 = ee0 + 4*aa0*ell1
```

The two displayed rearrangements are tautologies in
`Q[X19_rho0]`.  Independently,

```text
e1  - (G  + 4*a1*ell1)   = 0
ee0 - (Q0 - 4*aa0*ell1)  = 0
```

The committed scalars at derivation node 61 are
`e1_ell_scalar = [4,1]` and `ee0_ell_scalar = [-4,1]`, i.e. exactly
those two rearrangements.  With indeterminate multipliers
`c_e1, c_ee0, c_ell`,

```text
c_e1*e1 + c_ee0*ee0 + c_ell*ell1
  = c_e1*G + c_ee0*Q0
    + (c_ell + 4*a1*c_e1 - 4*aa0*c_ee0)*ell1.
```

The residual of that identity is `{}`.  The kernel update pops the
old labels, adds `c_e1` onto `G`, adds `c_ee0` onto `Q0`, and adds
`4*a1*c_e1` and `-4*aa0*c_ee0` onto `ell1`.  Both signs match the
identity.

Flipping the sign of the `4` in front of `a1*c_e1`, or of the `4`
in front of `aa0*c_ee0`, each produces a one-term residual
(`8*a1*ell1` and `-8*aa0*ell1` respectively).  Replaying the frozen
record with `e1_ell_scalar` flipped to `-4`, or `ee0_ell_scalar`
flipped to `+4`, is rejected by the kernel identity check with
those same residuals.  Flipping both signs is rejected on the `e1`
identity.  The registered controls are therefore the actual
coefficientwise identities, not transcript flags.

Old labels after the rebase and before the cubic clear:

| node | rule | `assume:e1` | `assume:ee0` | `G` | `Q0` | `ell1` |
|---|---|---|---|---|---|---|
| 18 | ClearPower `rs1^2` | present | present | absent | absent | present |
| 61 | RebaseAssumptions | **absent** | **absent** | present | present | present |
| 62 | ClearPower `ell1^3` | **absent** | **absent** | present | present | absent |
| 63 | ClearPower `Q0` | **absent** | **absent** | present | absent | absent |

The cubic `ClearPower(ell1, 3)` is node 62.  It consumes the
rebased certificate.  The old labels `assume:e1` and `assume:ee0`
are already gone.  That is the repair the C2 invalidation demanded:
do not carry the old `e1` multiplier through `K = a1^36 + …` and
into the right `a1^57` certificate.

---

## 4. `PruneZeroFactor` as a universal exact rule

The rule may delete a named generator term only when:

1. the label occurs in the certificate with DAG root `root`;
2. `root` is a `Mul` node and `factor` is one of its direct
   children;
3. exact sparse expansion of `factor` over `Q` is the empty
   polynomial.

This is `root = factor * (other children) = 0` in the polynomial
ring.  It does not invert, localize, reduce modulo a prime, or
consult a hash as an identity test.  The kernel expands `factor`
and fails closed on a nonempty result (`if polynomial: fail`).
The SHA-256 in `zero_checks` is telemetry of that empty expansion
(`sha256(b"[]") =
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`),
not a substitute for it.

Registered pairs at derivation node 70, after the last
`ClearPower(e0)`:

| label | committed root | committed factor | `Mul` args contain factor | multiplicity |
|---|---:|---:|---|---:|
| `assume:ee1` | 721 | 427 | yes | 1 |
| `assume:ez3` | 723 | 401 | yes | 1 |
| `assume:rs2` | 722 | 399 | yes | 1 |

Interned circuits:

```text
#721 Mul[118, 118, 153, 153, 174, 371, 371, 427, 428, 428, 666]
#723 Mul[118, 118, 153, 153, 174, 371, 371, 371, 401, 428, 428, 666]
#722 Mul[118, 118, 153, 153, 174, 371, 371, 371, 399, 428, 428, 666]
#371 Sparse(a1)
```

Independent memoizing expansion over `Q`, and a second
producer-style `expand_exact` walk, agree:

| node | terms | peak | SHA-256 | zero? |
|---|---:|---:|---|---|
| 427 | 0 | 9 | `4f53cda1…b945` | yes |
| 401 | 0 | 3 | `4f53cda1…b945` | yes |
| 399 | 0 | 3 | `4f53cda1…b945` | yes |
| 371 | 1 | 1 | `26ef9f6d…ea39` | **no**; polynomial `a1` |

Those peaks, emptiness verdicts, and hashes match the frozen
V43C3F diagnostic for the same four indices.  The diagnostic is
corroborative only.  Deletion in C4 is replayed from the C4 DAG.

Node 371 is a direct child of all three roots (multiplicity 2, 3,
3).  Replacing each registered factor by 371 therefore still
satisfies the direct-child test and is rejected only because the
expansion is the nonzero monomial `a1`.  That is the registered
attack, and it fires for each of the three labels.

The rule is not a `PruneZeroTerms` expansion of the huge product
roots 721/722/723.  Expanding a proven-zero direct factor is
enough, because the polynomial ring is a ring.

### 4.1 Telemetry clobber, not a soundness hole

Committed `zero_checks` record `"root": 427/401/399` rather than
the multiplier roots 721/723/722.  Cause: `prune_zero_factors`
builds a dict with the true `root`, then unpacks
`expand_exact(factor)` telemetry on top of it; that telemetry also
has a `"root"` key equal to the *factor*.  The `label_factors`
payload still carries the correct multiplier roots, and replay
re-checks `terms[label] == expected_root` from that payload before
testing direct-child containment.

This is a committed-telemetry naming bug.  It is not how the
assumption terms are deleted.  Repair is documentation/control
only (section 8).

---

## 5. `ClearPower` and `CombineBranches` guards

Independently in the V42 ring, for `n in {1,2,3}`:

```text
T^n - (m f)^n - (T - m f) * sum_{i=0}^{n-1} T^{n-1-i} (m f)^i  =  {}
```

The universal combine schema residual is also `{}`.  Used exponents
in this tree are one `n=2` (the `rs1` clear, node 18), one `n=3`
(the rebased `ell1` clear, node 62), and seven linear clears.
Mutating node 18 from exponent 2 to 3 is rejected by the relation
check (`a2 * rs1^2` versus `a2 * rs1^3`).

No derivation node has a `Div` operation.  Sparse leaves have no
negative exponent.  `Pow` exponents in the expression table are
nonnegative.  There is no localization and no implicit division.

`CombineBranches` is used three times.  Committed outputs of the
inputs, inspected before the kernel call:

| node | split | left has right-label? | right has left-label? |
|---|---|---|---|
| 50 | `ell1` vs `cs1` | no | no |
| 53 | `ell1` vs `rs1` | no | no |
| 66 | `e1` vs `G` | **no** | **no** |

The C2 obstruction was the right `a1^57` certificate still carrying
`assume:e1` (nonzero root 642) into this last split.  After rebase,
node 63 (`a57 modulo e0g`) has labels

```text
rows … , assume:e0, assume:e1_minus_4a1ell1
```

and does **not** have `assume:e1` or `assume:ee0` or `Q0`.  The left
`a46` certificate has `assume:e1` and does not have `G`.  The strict
crossed-assumption guard therefore passes with no
`PruneZeroTerms`.  That is why the derivation census contains zero
`PruneZeroTerms` nodes.  Removing the guard is unnecessary; the
repaired representation already satisfies it.

The last split relation is `e1 * G` equal to a scalar multiple of
`Tg12_2` modulo `e0`, with combine factor `1`.  Checkpoint
`e1 split` holds.

No set-theoretic step appears.  V42's radical/field-point cascade
is an ancestor of the row corpus, not a step in this DAG.  This
certificate is ordinary ideal membership by exact polynomial
identities.

---

## 6. Mutations, and the Tg19_7 control in particular

Registered mutations, independently replayed against the frozen
record, all reject:

| Mutation | What actually changes | Rejection |
|---|---|---|
| Tg19_7 omission | `final_certificate.terms` only | `final certificate commitment` |
| ClearPower exponent 2→3 at node 18 | derivation payload | `clear_power relation` residual |
| `e1_ell_scalar` 4→−4 at node 61 | derivation payload | `rebase e1 identity` = `8 a1 ell1` |
| `ee0_ell_scalar` −4→4 at node 61 | derivation payload | `rebase ee0 identity` = `-8 aa0 ell1` |
| factor 427/401/399 → 371 | prune payload, one label at a time | `PruneZeroFactor nonzero` (`a1`) |

**Tg19_7 omission is a commitment-integrity check, not an
independent source-row deletion test.**  The producer does

```text
omission["final_certificate"]["terms"].pop("Tg19_7")
```

and leaves `expression_nodes`, `derivation_nodes`, and the node-70
output certificate untouched.  Independently: after that pop, the
derivation table is identical to the frozen table, expression
nodes are identical, and node 70's committed output still contains
`Tg19_7` at root 718.  Replay rebuilds the same final certificate
(with `Tg19_7`) and fails only because it does not equal the
mutated `final_certificate` commitment.

That control does **not** prove that deleting the source row
`Tg19_7` from the 51-row corpus would break the membership, and
this review does not promote it into a row-dependency test.  The
exact theorem does not rest on that control.  It rests on complete
replay: `RowSpecialize` of `Tg19_7` is derivation node 10, the
multiplier survives as root 718 through node 70, the reconstructed
final certificate includes it, and the target is `a1^104`.

An unregistered stronger mutation that also pops `Tg19_7` from
node 70's committed output is rejected by the derivation-output
commitment, as expected of a serialized DAG, and is not a
row-file deletion test either.

The other registered mutations are load-bearing in the sense that
they attack the actual algebraic payloads (exponent, rebase
scalars, prune factors).  They all fail for the mathematically
correct reason.

---

## 7. Claimed census, runtimes, hashes, and AWS

| Claim | Evidence |
|---|---|
| 16 final rows, named list | reconstructed certificate; matches RESULT.md / result JSON |
| 732 / 71 / 29 | reconstructed and frozen record |
| proof 163236 bytes | live file size and result JSON |
| proof SHA-256 `3e0e80c0…` | live rehash |
| result SHA-256 `629a0763…` | live rehash; `RESULT.json` is a copy of `output/result.json` |
| status marker | stdout line and result JSON; **not** used as algebra |
| AWS host r6b `ip-172-30-0-106` | launch registration / meta |
| wall 7.03 s, RSS 36,764 KiB, 0 swap | `/usr/bin/time` stderr; `rc=0` |
| memory cap 4 GiB, wall cap 600 s | launch registration |
| lane prefix | matches `run_aws.sh` / producer `TAG_PREFIX` |

The AWS transcript is consistent with a short exact-Python job.
It is not the proof.  The proof is the serialized DAG, replayed
locally in about one second from freeze-pinned bytes.

RESULT.md's firewalls match the preregistration: this is raw
`rho=0` membership only.  Combined with the separately reviewed
generic identity `5*t^6*a1^4 in J` it would be an *input* to a
prospective exponent-628 converter.  No such converter is replayed
here, and none is accepted.

---

## 8. Nonblocking documentation/control repairs

None of the following moves the exact theorem.

1. **Tg19_7 omission is commitment-integrity only.**  Say so in
   the producer/RESULT prose if this control is kept.  Do not
   advertise it as a source-row deletion test.  The theorem
   already rests on complete replay.
2. **`zero_checks` clobbers `root` with the factor index.**  Build
   the telemetry dict after `expand_exact`, or rename the
   expansion's `root` key.  `label_factors` already has the
   correct multiplier roots.
3. **AWS source tarball / source-manifest `27f42f0f…` is not a
   freeze entry and is not harvested.**  Same class of snapshot
   gap as the C2 review.  Closed for the algebra by the
   freeze-pinned producer and the bit-identical local
   `build_proof`.
4. **`ExprStore.scale` does not fold `Scale(zero intern)` to the
   zero intern.**  Factor 399 has a summand `Mul[Scale(-8/3, #0),
   …]`.  Expansion is still empty.  Folding would only shrink
   the DAG.
5. **The charged tree is untracked at HEAD `418e4135…`.**  Custody
   is the freeze, not git.

---

## 9. Alternative explanations that would defeat the positive result

Each was checked and rejected.

| Candidate defeat | Finding |
|---|---|
| Frozen DAG is not canonically reconstructed from the 51 rows | `from_record` plus `replay_record` plus bit-identical `build_proof` |
| Final target is not `a1^104`, or assumptions survive | reconstructed `{a1^104:1}`; assumption ∩ final labels = ∅ |
| Rebase signs are wrong, or old labels survive into `ell1^3` | identities residual `{}`; old labels absent at nodes 61 and 62; sign flips rejected |
| `PruneZeroFactor` deletes on a hash / modular / numeric test | deletion follows `if polynomial:` after exact expansion of a direct `Mul` child |
| Factors 427/401/399 are not zero, or not direct children | independent expansion empty; `factor in node["args"]`; 371 is nonzero `a1` |
| Right `a57` still carries `assume:e1` into the last split | node 63 labels have `G`, not `assume:e1`; combine 66 has no crossed labels |
| Localization, negative exponents, or a set-theoretic step | no `Div`; no negative Sparse exponents; ordinary ring identities |
| Tg19_7 omission is being used as the existence proof | it is a commitment check; replay of the intact DAG is the proof |
| AWS transcript substituted for algebra | local replay from freeze-pinned bytes; AWS used only as runtime census |
| Stale C1/V42/V37/row source | all charged pins live-matched; V37 rehashed 70/70 files; alphabet 65, no `rho` |
| Scope creep to total `rho` / saturated Rees / exponent 628 | not replayed; firewalls in preregistration, RESULT.md, and this review |

No defeat holds.  The tree is a certificate of `a1^104 in I0`.

---

## 10. What this review is not

- Not a proof that `a1^104` is the least such exponent.
- Not a proof that every one of the 16 final rows is irredundant.
- Not a total-`rho`, saturated-Rees, Gate-T, order-two,
  maximum-twelve, or JC2 statement.
- Not a replay of a converter, and not an exponent-628 theorem.
- Not a rehabilitation of the uncorrected V43C1/C2 tree.  That
  invalidation remains: without the rebase, the right `a1^57`
  certificate retains a nonzero `assume:e1` multiplier.

---

## Verdict

The charged exact theorem is independently replayed and correctly
scoped.  In `Q[X19_rho0]`, the frozen 51 named raw ordered-a1 rows
through grade 19 contain `a1^104`.  The C2 crossed-assumption
obstruction is repaired by an exact rebase before the cubic
`ell1` clear.  Three leftover assumption multipliers are deleted
only after a literal direct-factor expansion to zero over `Q`.
Nonblocking control/documentation nits are listed in section 8
and do not bear the theorem.

GROK_CONFIRMED_A1_104_V43C4
