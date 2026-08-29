# Hostile review: V43C1/C2 crossed-assumption invalidation

Date: 2026-08-27
Reviewer: Grok 4.6 (xAI), adversarial algebra/custody, different-model lane
Charged objects:

- `cases/max12_812_order2_p0_total_rees_j2_a1_constructive_circuit_v43c2_20260827/INVALIDATION.md`
  (`dbea733345b2a707ee5834b90889eca6b41013b6694786317f54362e97d96b89`)
- freeze manifest
  (`10217738bc86e415050b667f226907b891bf2bb8e94e6f331fad8939bc562abe`)
- v3 resource-cap and v4 exact-failure artifacts in that case
- `xmodel/max12-812-order2-p0-total-rees-j2-a1-constructive-cascade-invalidation-v43c2-sol-20260827.md`
  (`59d1e39c5abc1c1afd68bdc71cac8ff12654dc95e48aeb3ed1516cc4e4d64b1c`)

**Overall: the negative result is confirmed at exactly the claimed
scope.**  The uncorrected V43C1/V43C2 constructive tree does not derive
`a1^104` in the frozen raw ordered-`a1`, `rho=0`, grade-through-19
ideal.  Independently rebuilding the arithmetic DAG from the freeze-pinned
producer, expanding node 170 with a memoizing evaluator that does not
share `ExprStore.expand_exact`, and inspecting nodes 619 and 642 as
circuits (not as AWS transcript) supports this statement and no stronger
one:

> The right `a1^57` certificate, advertised as modulo `(e0,G)` with
> `G=e1-4*a1*ell1`, retains a nonzero polynomial multiplier of the old
> assumption `assume:e1`.  That multiplier is the interned circuit
> `root 642 = a1^3 * Z * K` with `Z` the 24,429-term polynomial at root
> 170 and `K=a1^36+a1^18*m*ell1+(m*ell1)^2`.  The strict
> `CombineBranches(e1,G)` guard is correct to reject it.

This withdraws only the explicit special exponent `M=104` and the
conditional converter exponent `4+6*M=628` **from the uncorrected
derivation**.  It does not touch reviewed V42 radical/set-theoretic
closure, and it does not touch the exact V43G4 identity
`5*t^6*a1^4 in J`.  The proposed change-of-basis

```text
e1 = G + 4*a1*ell1,     ee0 = Q0 - 4*aa0*ell1
```

is an exact polynomial identity and a legitimate successor sketch.  It
is not a replayed certificate.

---

## 0. Constraints, method, and what was actually used

Session constraints honored: no Singular/Macaulay2 execution, no AWS
launch, no web sweep, no canonical-ledger edit, no contact with
`jc2-lean`.  The only repository file written is this report.

Git HEAD: `418e413593120d19e15e6546eb50c985f4b1f038`.  The charged C2
tree is presently untracked; custody is the freeze/pin table below, not
git.

Local work:

1. Rehash of every freeze line, the freeze file itself, the Sol note,
   and the C1/V42/V37 pin chain.
2. Import of the freeze-pinned producer
   `replay_constructive_circuit_v43c2.py` (`7d8c9635…ee5a90`) with
   `require_aws` never called.  Rows were loaded through the pinned V42
   → V37 loader, which itself rehashes all 70 row files before
   returning.
3. Reconstruction of the derivation DAG through the final
   `CombineBranches` attempt, with `PruneZeroTerms` intercepted so it
   cannot expand the large root-642 circuit and cannot delete a label.
4. Independent memoizing expansion of node 170 over `Q` using only V42
   `add`/`multiply`/`scale`/`power`, plus a second producer-style
   non-memoizing walk used solely to replay the v4 telemetry counters.
5. Direct inspection of interned nodes 170, 174, 619, 642 and an
   `ell1 |-> 0` DAG homomorphism on node 619.
6. Independent replay of the exponent-three `ClearPower` schema, the
   `CombineBranches` schema, and the proposed rebase identity, including
   both signed-`4` mutations.

No producer `PASS` string exists in the charged artifacts.  The v4
stderr was treated as a transcript of what that AWS Python process
printed, not as algebra.  The algebra below is from the reconstructed
DAG.

---

## 1. Custody

Every freeze line was rehashed against current bytes.  All 27 matched.
The freeze file itself hashes to the charged value
`10217738bc86e415050b667f226907b891bf2bb8e94e6f331fad8939bc562abe`.

| Artifact | SHA-256 | Role |
|---|---|---|
| INVALIDATION.md | `dbea733345b2a707ee5834b90889eca6b41013b6694786317f54362e97d96b89` | charged negative result |
| freeze file | `10217738bc86e415050b667f226907b891bf2bb8e94e6f331fad8939bc562abe` | 27-entry pin |
| Sol note | `59d1e39c5abc1c1afd68bdc71cac8ff12654dc95e48aeb3ed1516cc4e4d64b1c` | charged summary |
| PREREGISTRATION.md | `c6c6a57b9900a5111d028e522727dff44a084e4820d01a3141c35e56c48df8b1` | frozen question `a1^104 in I0` |
| live producer | `7d8c9635c16c0642341bd446745300b7bd8ec9dce3dd6d402f50660340ee5a90` | freeze-pinned DAG builder |
| probe helper | `6e66c706dcd5884f8229729c94d440f5b717075c4eeda5e89ae85647b2417ef7` | freeze-pinned; not used as algebra |
| C1 source | `af590ff872552944528dda41497329e1b1534cc211290d622034defd70bac2ca` | C2 and preregistration pin |
| V42 replay | `f4ec72933793bf08aabc600df7cdcd47b8de2c54f45c0d30341e13ac0b676459` | C1 pin, live-matched |
| V42 Sol | `5d4c42fff1ad563586e8ae8736c3938efb1ae48467dfab96ae7fd9b861e7037f` | C1 pin, live-matched |
| V42 hostile review | `a4f6b93181526cd8907c6412faeef2ed2e69012a5820e939079ba4cf891f3439` | C1 pin, live-matched |
| V37 loader | `ba034c8cebaa27c5630872b9cf06d152e4577170486ac34ad7f695ead871845b` | V42 pin, live-matched |
| V3 evidence manifest | `37946eefba5b3c42dec8fed4956fcc9d8adee0d056ee8b18251ca1d415fc6b41` | freeze and INVALIDATION pin |
| V3 stop record | `1580c6c8c0a97e20d1c31e50948b5c1af216e5d824d7f75160b06bf37ea9433d` | 14-GiB gate, no algebraic verdict |
| V4 evidence manifest | `bef7f72a556a470b95dff05796937f8410347045f44b787f5050e09fc93d4ac8` | freeze and INVALIDATION pin |
| V4 stderr | `8b7a83b33b95a36213c1e247a55dad7a9651c0d8ad4ad1fc08546b038b99d2d1` | AWS transcript of node-170 telemetry |
| G4 freeze file | `777927795b59509c56c2d971b82db9be05ab7f33a7449b0f1947d28f4a201b91` | untouched by this invalidation |
| G4 RESULT.md | `ae7beed3e677a46bda82778ae6bbeb1a8aef74dcbf8db35df07f02d183b70015` | exact `5*t^6*a1^4` identity |

All four V42 input pins consumed by `load_v42` also matched.  The V37
loader accepted the closed census **51 nonzero rows / 70 files / 65
positive variables**, with `rho` and `ez9` absent.  Empty AWS
stdout/launcher files hash to `e3b0c442…7852b855`, the SHA-256 of the
empty byte string.

Row-specialization leaves in the reconstructed DAG use the V42 divided
difference, and the producer asserts
`P = P|_(x=v) + (x-v) Q` coefficientwise before committing each leaf.
That is the same identity already used by the reviewed C1/V42 chain; it
was not re-attacked here except to confirm the loader pin is live.

### 1.1 Producer-byte gap, closed for the charged algebra

INVALIDATION quotes a v4 producer SHA-256
`1a21fd304579b5da1dd8df020bb066a74dbc8d4c8f6f3ac32932bacc105c8e75`
and source manifests `f82c4c12…` (v3), `71b7fcc0…` (v4).  Those three
hashes are **not** freeze entries; the AWS source tarballs are not in
the case directory.  The freeze instead pins the live producer
`7d8c9635…ee5a90`.

This is a real snapshot gap, not a mathematical one.  Node 170 is the
`assume:e1` multiplier of the `a1^18` checkpoint, which is interned
**before** any `PruneZeroTerms` site (v4's early prune at that
checkpoint, or the live producer's prune at the first crossed
`CombineBranches`).  Rebuilding that checkpoint from the freeze-pinned
producer and expanding root 170 independently reproduced the v4 stderr
telemetry bit for bit (section 2).  The missing v4 bytes therefore do
not underwrite, and do not defeat, the negative result.

The v3 stop record is telemetry only.  RSS 14,778,700 KiB crossed the
registered 14,680,064 KiB gate at 24m39s; stdout is empty; `rc=143`.
The human `reason=` line attributing that cap to “node170 expansion”
is interpretive.  The live (and, by the addendum, the v3) producer
invokes `PruneZeroTerms` at the first crossed-label boundary, which is
the final split, i.e. root 642 rather than root 170.  That does not
matter: v3 has no algebraic verdict, and v4 plus the independent
expansion do.

---

## 2. Nodes 170, 619, 642

Checkpoints from the reconstructed DAG, with targets asserted equal to
the named monomials by the producer kernel before any prune:

| checkpoint | target | `assume:e1` root | other relevant labels |
|---|---|---|---|
| `a18 modulo ell1` | `a1^18` | **170** | `ell1=174`, `ee0=172`; `rs1` absent |
| `a56 modulo e0gq` | `a1^56` | 623 | `G`, `Q0`, leftover `ee0` |
| `a57 modulo e0g` | `a1^57` | **642** | `G` present, `Q0` absent, leftover `ee0=643` |
| `a46 modulo e0e1` | `a1^46` | 604 | `G` absent |

`rel_ell3` (`a2 ell3`) terms are `{Tg13_4, assume:e0, G, Q0}`.
`rel_q0` (`a q0`) terms are `{Tg12_1, assume:e0, G}`.  Neither
relation carries `assume:e1`.  There is therefore no extra `e1`
summand that could cancel the inherited factor in either `ClearPower`.

Interned circuits (hash-consed, args sorted):

```text
#170 Add[157, 169]
     157 = Mul[116, 152, 153]     # a1^2 * (a1^8 + m_rs * rs1) * c
     169 = Mul[145, Pow(119,2)]   # m_rs^2 * d
#174 Add[159, 173]                # m := a18's assume:ell1 multiplier
#619 Add[614, 616, 618]
     614 = Sparse(a1^36)
     616 = Mul[174, ell1, a1^18]
     618 = Pow(Mul[174, ell1], 2)
#642 Mul[153, 170, 371, 619]
     153 = Sparse(a1^2)
     371 = Sparse(a1)
```

So, as polynomials,

```text
Z  := node170 = a1^2*(a1^8 + m_rs*rs1)*c + m_rs^2*d
K  := node619 = a1^36 + a1^18*m*ell1 + (m*ell1)^2
root642      = a1^2 * Z * a1 * K = a1^3 * Z * K
```

with `m = node174` exactly the `ell1` multiplier of the `a1^18`
certificate.  This is the factorization claimed by INVALIDATION and by
the erratum, not an isolation guess.  The v5 probe's “unique 3-argument
`Add` among the `Mul` args of root 642” heuristic happens to select
619 uniquely (170 is a 2-argument `Add`; 153 and 371 are `Sparse`),
but the review did not rely on that heuristic.

### 2.1 Independent expansion of node 170

A memoizing DAG walker, decoding each `Sparse` leaf with a fail-closed
non-duplication check and combining through V42 sparse arithmetic,
expanded root 170 over `Q` to **24,429** nonzero terms.  An independent
canonical encoder (sort monomials, JSON `separators=(",",":")`,
SHA-256) hashed that polynomial to

```text
3c4dcc5f62f3c501f08581369525ca088b15a4ec3d3fa6f56251da288e229a72
```

A second, producer-style non-memoizing walk of the same circuit
returned the same polynomial and the v4 telemetry counters:

```text
visited_nodes          61
evaluated_node_calls   92
peak_sparse_terms      24429
term_cap               1000000
expanded_term_count    24429
expanded_sha256        3c4dcc5f62f3c501f08581369525ca088b15a4ec3d3fa6f56251da288e229a72
```

That is the dict printed in the frozen v4 stderr.  Node 170 is not the
zero intern (index 0).  It is not the zero polynomial.  Evaluating it
at the all-ones point of its 35-variable support yields the nonzero
scalar `-634801821235/917504`.

The 24,429-term claim, the hash, and the “nonzero” verdict are
confirmed.  The separately frozen addendum that treated node 170 as
zero is already superseded by the erratum; that addendum is an
immutable historical artifact and is not a live claim.

---

## 3. Exponent-three `ClearPower` geometric factor

The kernel identity, for `exponent = n >= 1`, `T` the current target,
`f` the cleared generator, `m` its multiplier, and `factor` the
ordinary clearing polynomial, is the difference-of-powers expansion

```text
T^n - (m f)^n = (T - m f) * sum_{i=0}^{n-1} T^{n-1-i} (m f)^i.
```

If the input certificate is exact, `T - m f` is the rest of the
certificate, and multiplying through by `factor` replaces `f^n` by the
relation.  Independently expanding the universal schema in the V42
ring for `n=3` gave residual `{}`.  Directly,
`T^3-(m f)^3 - (T-m f)(T^2 + T(m f) + (m f)^2)` is also `{}`.

For the charged step `ClearPower(a18, ell1, 3, rel_ell3, a1^2)` one
has `T=a1^18`, so the geometric sum is

```text
K = a1^36 + a1^18*(m*ell1) + (m*ell1)^2.
```

Inherited non-`ell1` multipliers, including `Z`, are multiplied by
`a1^2 * K`.  The subsequent linear `ClearPower` of `Q0` with factor
`a1` has geometric sum `1`, so it multiplies those inherited
multipliers by one more `a1`.  That is exactly interned node 642.

`K` need not be expanded.  The evaluation homomorphism `ell1 |-> 0`
kills every summand that carries a positive power of `ell1`,
regardless of whether `m` itself involves `ell1`, and leaves the first
summand.  Walking node 619 under that homomorphism produced the
one-term polynomial `a1^36`.  Hence `K ≠ 0` in `Q[X19_rho0]`.

`Q` is a field, so `Q[X19_rho0]` is an integral domain.  The factors
`a1`, `Z`, and `K` are all nonzero as polynomials.  Therefore
`a1^3 Z K ≠ 0`.  Vanishing of `Z` along `ell1=0` (which occurs: `Z`
has no pure `a1`-power) is irrelevant to that domain argument.

The `CombineBranches` schema was likewise expanded in the V42 ring and
has residual `{}`.  It is not a licence to ignore a leftover split
label.

---

## 4. The right `a1^57` certificate cannot enter the strict split

The advertised last split is

```text
left:  a1^46 modulo (e0, e1)
right: a1^57 modulo (e0, G),    G = e1 - 4*a1*ell1
split: e1 * G = (32/3) Tg12_2   modulo e0
```

Reconstructed labels at that call:

- left `a46` has `assume:e1` (root 604) and does **not** have `G`;
- right `a57` has `G` (root 657) and **does** have `assume:e1` (root
  642);
- `G` is the interned polynomial `e1 - 4*a1*ell1`, matching the extra
  generator `assume:e1_minus_4a1ell1`.

The live `combine_clean` therefore attempts `PruneZeroTerms` on the
right label `assume:e1`.  That is root 642, which is nonzero by
section 3, so a faithful prune must fail closed.  Intercepting the
prune and leaving the label in place, the kernel then raises

```text
('combine crossed assumptions require PruneZeroTerms',
 {'right_in_left': None, 'left_in_right': 642})
```

which is the specified guard.  Removing the guard, or deleting a
nonzero multiplier, would be a different rule, not a verification of
this tree.

Additional structural fact, not needed for the `e1` obstruction and
not expanded here: `a57` still carries `assume:ee0` (root 643).  The
advertisement “modulo `(e0,G)`” is therefore structurally false in a
second label as well.  `rel_q0` does not consume `ee0`; `Q0` and `ee0`
are distinct generators.  This is why the successor sketch rebases
**both** `e1` and `ee0` before the cubic `ell1` clear.  It is not a
second expanded countercertificate, and it is not claimed as one.

---

## 5. Scope firewall

The charged invalidation withdraws two numbers from **this uncorrected
derivation**:

- the explicit special-fibre exponent `M=104`;
- the conditional total exponent `4+6*M=628`.

The arithmetic `4+6*104=628` is correct and was already recorded as
arithmetic, not as a theorem, in the V43G4 hostile review.  That
review treated `M=104` as a citation.  Withdrawing the citation does
not touch G4.

Live G4 pins were rehashed in this session and still match the G4
review table: freeze file `77792779…01b91`, RESULT.md
`ae7beed3…b00015`, preregistration `20bce356…ecdb4`.  The identity
`5*t^6*a1^4 = sum_i H_i Tg_i` is an honest sparse equality in the
literal total ring; nothing in the C2 DAG is an input of that
equality.

V42 is a radical / field-point cascade.  Its C1 pins are live (section
1).  It uses one set-theoretic step from the product branch-cover to
`A1 ∪ A2`.  That is a different theorem, in a different category, and
it does not produce an ordinary-ideal certificate `a1^104 in I0`.
Failing to compile that cascade into such a certificate does not
reopen the cascade.

Firewalls that remain in force:

- ambient ring `Q[X19_rho0]` after `rho=0` and the ordered chart
  `rs=cs=c0=c1=a0=0`;
- no unspecialized-`rho`, saturated-Rees, Gate-T, order-two,
  maximum-twelve, or JC2 statement;
- no claim that a corrected special-fibre certificate is impossible;
- no claim that the branch-combination *theorem* is false, only that
  this representation of it is not a certificate.

---

## 6. Prospective repair, not a certificate

Generator conventions in the freeze-pinned producer:

```text
G  = e1 - 4*a1*ell1
Q0 = ee0 + 4*aa0*ell1
```

The two displayed rearrangements are then tautologies in the
polynomial ring.  Independently,

```text
e1  - (G  + 4*a1*ell1)   = 0
ee0 - (Q0 - 4*aa0*ell1)  = 0
```

and, with indeterminate multipliers `c_e1, c_ee0, c_ell`,

```text
c_e1*e1 + c_ee0*ee0 + c_ell*ell1
  = c_e1*G + c_ee0*Q0
    + (c_ell + 4*a1*c_e1 - 4*aa0*c_ee0)*ell1.
```

The residual of that identity is `{}`.  Flipping the sign of the `4`
in front of `a1*c_e1`, or of the `4` in front of `aa0*c_ee0`, each
produces a nonzero residual (one term).  A successor that serializes
this as a `RebaseAssumptions` rule must reject both mutations, must
apply the rewrite **before** `ClearPower(ell1,3)`, must drop the old
labels `assume:e1` and `assume:ee0` only after the rewrite, and must
retain every existing clear/branch/prune guard.

This review does not execute, and does not accept, any successor
producer.  In particular it does not treat the uncharged rebased
sketch in `constructive_circuit_rebased_v43c3` as evidence.  No
`M=104` claim resumes until a complete successor passes and is
hostile-reviewed.

---

## 7. Alternative explanations that would defeat the negative result

Each was checked and rejected.

| Candidate rescue | Finding |
|---|---|
| Wrong node isolation (170 is not the `e1` multiplier of `a18`) | `a18.terms["assume:e1"] == 170` in the reconstructed DAG. |
| Node 619 is not `K` | Interned as `Add(a1^36, Mul(m,ell1,a1^18), Pow(Mul(m,ell1),2))` with `m` exactly `a18.terms["assume:ell1"]`. |
| Node 642 is a different circuit, or mixed with a cancelling relation summand | `Mul(a1^2, 170, a1, 619)`; `rel_ell3` and `rel_q0` contain no `assume:e1`. |
| Expansion / hash-consing / compiler artifact | Memoizing walker, non-memoizing walker, and an independent canonical encoder agree with each other and with v4 stderr.  `Add`/`Mul` argument sorting is legitimate because those operations are commutative over `Q`. |
| Zero divisor | `Q[X19_rho0]` is a domain; `a1`, `Z`, `K` are nonzero polynomials. |
| Sign convention on `G` or `Q0` | Extra generators are `e1-4*a1*ell1` and `ee0+4*aa0*ell1`.  Right-branch row specs use `e1=4*a1*ell1` labelled by `G` and `ee0=-4*aa0*ell1` labelled by `Q0`.  Consistent. |
| Stale C1/V42/row source | All charged pins live-matched; V37 rehashed 70/70 files on load; alphabet 65 with no `rho`. |
| `PruneZeroTerms` or `CombineBranches` kernel bug that should have accepted the tree | The prune rule may delete a label only after an exact empty expansion.  Node 170 is nonempty.  Node 642 is a nonempty product involving it.  The combine guard matches the specified schema, whose residual is empty. |
| v3 14-GiB stop meaning the circuit is too large to be a counterexample | Resource cap is not a zero certificate.  v4 and the desk-scale independent expansion of the *small* factor `Z` already suffice. |
| Leftover `e1` is only structural, cancelled later in the DAG | Root 642 is the value that would be handed to the split.  There is no later rewrite in this tree. |

No rescue holds.  The tree is not a certificate of `a1^104 in I0`.

---

## 8. What this review is not

- Not a proof that no ordinary-ideal `a1^N` certificate exists on this
  corpus.
- Not a proof that the rebased `(G,Q0,ell1)` branch is exact.
- Not a replay of V43C1's expanded (non-DAG) job, which INVALIDATION
  correctly records as not having reached a verdict.
- Not an expansion of node 619 or root 642.  Those expansions are
  unnecessary once `K|_(ell1=0)=a1^36` and `Z ≠ 0` are known.
  The uncharged v5 4-GiB probe of node 619 is corroborative telemetry
  only and is not a freeze entry.

Nits that do not move the verdict: missing AWS source tarballs for v3
and v4 (section 1.1); interpretive v3 `reason=` line; the live
`a57` still structurally carrying `assume:ee0` in addition to
`assume:e1`.

---

## Verdict

The charged negative result is exact, independently replayed, and
correctly scoped.  The uncorrected constructive derivation does not
prove `a1^104`.  The converter exponent 628 is unavailable from that
derivation.  V42 and V43G4 are untouched.  The displayed rebase is a
prospective repair, not a theorem.

GROK_CONFIRMED_INVALIDATION
