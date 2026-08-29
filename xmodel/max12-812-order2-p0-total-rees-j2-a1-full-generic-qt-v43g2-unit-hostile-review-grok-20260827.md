# Hostile review: V43G2 full generic `Q(t)` unit decision

Date: 2026-08-27
Reviewer: Grok 4.6 (xAI), adversarial algebra/custody, different-model lane
Charged producer: `cases/max12_812_order2_p0_total_rees_j2_a1_full_generic_qt_v43g2_20260827/`
Prompt SHA-256:
`1596bff89eda343f44887b1d281dcd07b30fb8ba6a8124f06a9cabfd64d5a9d3`

**Overall: PASS at the exact claimed scope.**  Independently regenerated
literal source, all frozen hashes, and the harvested Box02 transcript
support this statement and no stronger one:

> After `a1=1` and the exact linear `ez9` pivot on the full 59-nonzero-row,
> 66-positive-variable ordered-`a1` corpus through grade 19, the remaining
> 58 rows generate the unit ideal in `Q(t)[X']`, `|X'|=64`, `t=rho^2`.
> The exact `dp` basis file is the single byte `1`; the normal form of `1`
> is the two bytes `0\n`.  This is provisional pending tracked multipliers
> and total rehomogeneous replay.

Do not promote this to an unrestricted total certificate, to
`K+(rho)=(1)` as a campaign identity, or to JC2.

---

## 0. Custody, constraints, and what was actually used

Session constraints honored: no Singular/Macaulay2 execution on any live
system, no AWS launch, no web sweep, no canonical-ledger edit, no contact
of any kind with `jc2-lean`.  Local work was hash recomputation, parsing
of the frozen 318,853-byte decision script, and one independent call of
the pinned V43 `reconstruct_rows` through the hashed V43G1 loader (130 s
wall, Python `Fraction` arithmetic, not a Gröbner run).  The only
repository file written is this report.

Git HEAD: `418e413593120d19e15e6546eb50c985f4b1f038`.  The charged G1/G2
trees and the repaired two-fibre theorem are presently untracked; custody
is the freeze/pin table below, not git.

| Artifact | SHA-256 | Role |
|---|---|---|
| G2 preregistration | `2545d70dd88700318c45a6a1a337f63b28379cef2f8760dd3481ba2d7bb2f6c8` | frozen question |
| G2 compiler | `4ce93300474ec1a86cb9a435fbb3d780b3e121a946796a07f1cd0f8a73bd0a99` | generic-only twin |
| G2 runner | `a0b4f78158ca9521cbaa378e2aba0f48916c7c04a86e04f1e12883487053e1ad` | Box02 launch |
| G2 result | `60b76bd4d3a8106a1e670073ae1f84218e1d62ae21187d79d75abf0bbcc48028` | claimed unit |
| G2 freeze file | `bbb8b2d637be3458c0e67cfabbe3fa594ea521cb6a1151a5a242f937abf4c04d` | 24-entry harvest pin |
| compiler result | `fac99098b36f5875b53c8d66439f34ca59b47e7f25a58f97dba1cb8cddd3806c` | census + pins |
| generated Singular | `7e3149d9ff89274e31c1068a51903dd9e2e716168141bd6286fa6b47d56328b3` | 58-row `Q(t)` input |
| basis file | `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b` | literal `1` |
| normal-form file | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | `0\n` |
| remote evidence manifest | `2cd5a6390d659caf3ffa52015bd1982534c72f15e5332c8cef46367a64077f61` | Box02 harvest |
| local harvest manifest | `65486fbb7ac8e6a0427149c4d2e1d2d73b3d4f8e46ee3049fbd004ac5e8dae9b` | same plus the evidence manifest |
| V43G1 compiler | `03b76b7b9592abf9c13ccb3a8ea716c9b43d601f7ce26a37428733435cf6e957` | loader + dehom text |
| V43G1 preregistration | `8a4727c2524134583885e06bd0d7d238068231ea971ac36f51f13ac13123afe3` | generic predicate |
| V43G1 field bridge | `25f5200017d0fb95ea0ff5aead291acfcef651c400cfcf4deb272653438a09df` | `Q(t)→Q(rho)` |
| V43 compiler | `0de6a2b279aeeab8c5a635c1d7658958f3f49f0f94f8473355d281cae9438b00` | literal regeneration |
| V43 census addendum | `266dfb8962cbeb1af73d4f03947670148b71a00eebd5e2a91fce9c78b99bf658` | 66/65/`ez9` |
| Fable5 V43 delta review | `ae8ecf1887a62afd873fc795d0eeec50ff0aac6e4954813931d09a34c8bfc31a` | G1 pin, unused by G2 |
| V42 replay | `f4ec72933793bf08aabc600df7cdcd47b8de2c54f45c0d30341e13ac0b676459` | special-fibre input |
| V42 report | `5d4c42fff1ad563586e8ae8736c3938efb1ae48467dfab96ae7fd9b861e7037f` | special-fibre input |
| V42 Opus5 review | `a4f6b93181526cd8907c6412faeef2ed2e69012a5820e939079ba4cf891f3439` | special-fibre input |
| repaired two-fibre theorem | `a7f96b0d8ac5867cefe7984f87a44ecd30ef3780df731e8b3acc3dc9db159ec6` | G2 pin |
| two-fibre hostile review | `bc539ba91600b95e5400e96635e8973ef6cb6454b9641c0c68d09a99aef0690f` | G2 pin |

Every row of this table was rehashed locally against current bytes and
matched the producer pin.  All 24 `FREEZE.sha256` entries matched.  All
18 `EVIDENCE.sha256` entries matched.  All 19 `LOCAL_HARVEST.sha256`
entries matched; the extra harvest line is the evidence manifest itself.

No producer PASS string was trusted as algebra.  The Box02 stdout was
used only as a transcript of what Singular printed after the independently
audited input was hashed.

---

## Verdict summary

| Attack | Charge | Verdict |
|---|---|---|
| 1 | Recompute hashes and manifests; AppleDouble inert vs custody ambiguity | **PASS**.  Nested harvest remark, not an algebraic defect |
| 2 | Literal 70/59/66/65 regeneration, eight rho-only rows, unique `ez9`, even-rho, row hashes | **PASS** |
| 3 | Linear pivot equivalence; nonzero in `Q(t)`; no other `ez9`; constraint not dropped | **PASS** |
| 4 | `ring K=(0,t),(...),dp` is `Q(t)`; `std` complete; `reduce(1,G)=0` plus basis `1` is unitness | **PASS** at decision scope |
| 5 | Skipping `G0` does not change the generic predicate; V42 enough for two-fibre special; separate multipliers | **PASS** |
| 6 | Compiler/pivot artifacts, bad serialization, coefficient-only input, collisions, stale hashes, `t=c` | **PASS** (none found that touch the verdict) |
| 7 | Exact remaining checks before promotion | **PASS** as a correctly withheld gate; listed below.  Not a defect of the scoped claim |

**Smallest statement actually proved.**  The 58-row ideal
`J ⊂ Q(t)[X']` compiled from the literal full corpus, after `a1=1` and
the quotient by the monic linear relation `(3/8)t·ez9 + h = 0`, contains
`1`.  Equivalently, by the pinned field bridge, the same ideal extended
to `Q(rho)[X']` contains `1`.

**Smallest statement not proved.**  An explicit identity
`a1^N U(rho^2) ∈ J` with `U(0)=1` against the 59 literal rows.  That is
the promotion gate, not a hidden extra hypothesis of the generic unit.

---

## 1. Attack 1 — hashes, manifests, AppleDouble

### 1.1 Freeze and harvest

All 24 freeze paths exist and rehash.  The two JSON compiler-result
copies are byte-identical.  Compiler stdout records
`RESULT_SHA256=fac99098…3806c`, matching both copies.  Lane metadata
stdout/stderr digests match the harvested files.  `launcher.stdout` and
`launcher.stderr` are the empty-file digest `e3b0c442…b855`.  Lanes log:

```text
2026-08-27T10:57:07Z ..._compiler rc=0
2026-08-27T10:57:07Z ..._singular rc=0
```

Compiler wall 244.43 s / 145,044 KiB RSS; Singular wall 0.10 s /
19,616 KiB RSS; both under the preregistered 640 GiB / 6 h cap.
Neither lane swapped.  No `FAIL_`, `Traceback`, `Killed`,
`out of memory`, `error occurred`, or `SPECIAL_FIBRE` marker occurs in
the run directory.  The runner would have exited 89 on a special-fibre
PASS string and 91 on those failure tokens.

Launch registration records

```text
source_manifest_sha256=b9b557d0ea1b3fc8c3335fa0589c5b0cc96096b9ebb07e39475f1d2152aa634c
memory_cap_kib=671088640
wall_seconds=21600
```

and `run_aws.sh` refuses to start unless that digest equals
`sha256sum AWS_SOURCE_MANIFEST.sha256` and `sha256sum -c` succeeds.
The source tree itself is **not** in the Box02 harvest.  That is the
same harvest omission previously flagged on V43 compiler-only lanes.

### 1.2 The six AppleDouble files

RESULT.md discloses six macOS AppleDouble sidecars in the AWS source
manifest, hashed, unread by the compiler.  The local G2 tree contains
zero `._*` files (only `com.apple.provenance` xattrs, which never
travel as file content).  Without the harvested manifest an auditor
cannot independently name the six paths.

Inertness does not depend on naming them.  AppleDouble objects are
`._filename` sidecars; the runner invokes
`python3 cases/.../compile_generic_only_qt_v43g2.py` by explicit path;
Python import and Singular `read` never open `._*` files.  More
strongly: this review regenerated the 58 generators from the local,
AppleDouble-free, hash-pinned V43→V43G1→V43G2 chain and obtained
**byte-identical** ideal entries against the harvested
`generic_only_qt_decision.sing`.  Whatever those six files were, they
did not enter the algebraic input.

**Verdict: PASS.**  Repairable follow-up, not required to accept the
unit: harvest `AWS_SOURCE_MANIFEST.sha256` so the six names and their
163-byte (or similar) payloads are inspectable.  That is a custody
hygiene item, not a hole in the `Q(t)` predicate.

---

## 2. Attack 2 — literal source regeneration

`compile_generic_only_qt_v43g2.py` does not rebuild rows itself.  It
imports the hashed V43G1 compiler, which imports the hashed V43
compiler, which calls `reconstruct_rows`.  That function:

- loads V35/V37/V33/V28/V20/parser under their pinned hashes;
- rebuilds grades 10–19 × rows 1–7 (70 named slots);
- specialises each total row onto the ordered-`a1` chart, then checks
  the `rho=0` face against the frozen V37 row, failing closed on drift;
- converts even `rho` exponents to `t=rho^2` via `total_to_t`, which
  **hard-fails on any odd rho exponent** and on sigma-weight mismatch.

This review executed that path through `g1.load_v43()`.  Live census:

```text
named source slots          70
nonzero total rows          59
nonzero_general             59
positive variables          66  (includes a1, ez9)
rho=0 positive variables    65
general-only variables      [ez9]
t in variables              False
rho-only rows               Tg11_2, Tg11_3, Tg11_5, Tg11_7,
                            Tg12_5, Tg12_7, Tg13_7, Tg14_6
zero total slots            Tg10_1..Tg10_7, Tg11_4, Tg11_6,
                            Tg12_6, Tg13_6          (11 = 70-59)
t-degrees present           {0,1,2,3,4}
wt(a1)=5, wt(ez9)=14        5+14=19, homogeneous on Tg19_2
```

Every `reduced_row_sha256` and `rho_only_row_sha256` in
`compiler_result.json` matched the independently recomputed
`canonical_t_polynomial` digest, including the pivot
`cc8957b85398036791e8193bc5864897412bdec6e30f2c363cce7bb345e31209`.
The 58 `generic_dehom_text` strings are byte-identical to the 58
Singular generators.  No generic row serialised as `0`.

The eight rho-only rows are exactly those whose every `t`-polynomial
has vanishing degree-0 coefficient.  After `a1=1` they remain nonzero
in `Q(t)` (first four become `((3/8)*t)*e1`, `((3/16)*t)*e0`,
`((-3/64)*t^2)*e0`, `((3/128)*t^3)*e0`).  They are part of the
mathematical input, as the G1 preregistration requires.

**Verdict: PASS.**

---

## 3. Attack 3 — linear pivot equivalence

Live reconstruction found **exactly one** monomial in the 59-row corpus
whose exponent vector has positive `ez9` power.  It is

```text
Tg19_2,  monomial (a1^1 ez9^1),  t-polynomial (3/8) t .
```

That is the G2 check, strictly stronger than G1's "after deleting `a1`,
the monomial is `ez9` and the `t`-polynomial is nonempty".  After
`a1=1` the pivot term is the nonzero element `(3/8)t ∈ Q(t)` times the
variable `ez9`.  In particular `(3/8)t` is a **unit** of `Q(t)`, inverse
`8/(3t)`.  It is not a unit of `Q[t]_{(t)}`; that is why the pivot is
generic-only, and why it is correctly not used on the special fibre.

`Tg19_2` is not a one-term row.  It has **476** stored terms, of which
**475 do not involve `ez9`**.  Write, after `a1=1`,

```text
Tg19_2 |_(a1=1)  =  c(t) ez9 + h,    c(t)=(3/8)t,    h ∈ Q(t)[X'].
```

The other 58 rows contain no `ez9` at all (live check).  In
`K[X', ez9]` with `K=Q(t)`,

```text
K[X', ez9] / (c ez9 + h, f1, …, f58)
  ≅  K[X'] / (f1, …, f58)
```

because `c` is a unit, so `ez9 ≡ -h/c`, and substitution into the `fi`
does nothing.  The 475-term `h` is absorbed into the definition of
`ez9`; it is **not** an extra constraint on `X'` and is **not** silently
dropped as a condition on the remaining variables.  Conversely, if the
58-row ideal is already `(1)`, then `1` lies in the 59-row dehomogenized
ideal with coefficient `0` on the pivot row.  Consuming `Tg19_2` is an
exact quotient-ring isomorphism, as the preregistration claims, not a
row omission.

The reduced alphabet is 64 variables, equal to
`(frozen 65) \ {a1}`: `ez9` is general-only, so after eliminating it the
generic and special variable lists coincide.  Live check matched
`compiler_result.json`.

**Verdict: PASS.**

---

## 4. Attack 4 — Singular coefficient field, `std`, unitness

The frozen ring line is

```text
ring K=(0,t),(aa0,aa1,aaa0,aaa1,ac3,...,rs7),dp;
```

Sixty-four identifiers, no `a1`, no `ez9`, no `t`, no `rho`, no
duplicates.  In Singular this is the polynomial ring in those variables
over the rational function field of characteristic 0 in the
transcendental `t`, i.e. `Q(t)[X']`, term order degrevlex.  It is not
`Q[t][X']`, not a numerical specialisation `t=c`, and not a modular
ring.  The script contains no `subst`, no `t=0`, no `mod`, no
`liftstd`, no `G0`.  `option(redSB)` requests the reduced standard
basis.

Over a field, Buchberger/`std` is a complete Gröbner algorithm.  Content
operations in `t` are legal in `Q(t)` because `t` is a unit: replacing
`t^k f` by `f` does not change the ideal.  That same inversion is
exactly why a `Q(t)` unit need not give a cofactor with `U(0)=1`; the
producer already prints `V43G2_UNIT_STATUS=requires-tracked-lift`.

The transcript is:

```text
V43G2_GENERIC_BASIS_SIZE=1
V43G2_GENERIC_OUTCOME=unit
V43G2_UNIT_STATUS=requires-tracked-lift
PASS_A1_GENERIC_ONLY_QT_V43G2
```

Basis file bytes: `31` (`"1"`, no newline), digest `6b86b273…5b4b`.
Normal-form file bytes: `30 0a` (`"0\n"`), digest `9a271f2a…86aa`.
`reduce(1,G)=0` is a sufficient membership certificate even without
completeness of `G`; combined with `write(G)` producing the unit, `G`
is the unit ideal.  `rc=0`, 0.10 s, 19,616 KiB, no Singular diagnostic
on stderr (only `/usr/bin/time -v`).  The 0.10 s wall is not a
suspicious abort: after `a1=1` the first generator is `((3/8))*e0`, so
`e0` is immediately in the ideal, matching the reviewed identity
`Tg11_1=(3/8)a1 e0`.  Degrevlex on a nearly triangular linear cascade
in 64 variables over a field is expected to collapse on that timescale.
No generator is a `Q(t)`-constant; unitness is computed, not planted.

This review did not re-execute `std`.  The decision semantics of the
frozen commands are standard.  CAS trust in Singular `std` over `Q(t)`
is the same assumption the campaign already uses for exact `Q` bases.
The intended independent strengthening is the separately frozen
`liftstd` identity `J·C = [1]`, not a second untracked `std` of the
same script.

**Verdict: PASS** for the generic `Q(t)` unit.  Completeness of a
tracked Bezout representation is Attack 7, not this one.

---

## 5. Attack 5 — skipped `G0`, V42 special, two-fibre vs multipliers

V43G1 computes `std(J0)` on the 51 nonzero `t=0,a1=1` rows as a
fail-closed positive control and prints `V43G1_SPECIAL_FIBRE_UNIT=1`.
V43G2 deletes that block, prints
`V43G2_SPECIAL_CONTROL=external-pinned-reviewed-V42`, and the runner
**fails closed** if `SPECIAL_FIBRE_UNIT` ever appears.  The generic
ideal, ring, pivot, and 58 generators are otherwise the G1 generic
stage.  Skipping `G0` cannot change the generic predicate.

The special conjunct used by the repaired two-fibre theorem is
`a1 ∈ √(J0)`, equivalently `J0|_{a1=1}=(1)` by the graded-unit lemma
already reviewed over any field.  Promoted V42, as scoped by the Opus5
review §10, supplies exactly that at radical/field-point strength:

- no point with `a1 ≠ 0` on the frozen `rho=0` ordered-`a1` system,
  over every field of characteristic outside `{2,3,7}` (in particular
  over `Q̄`);
- ordinary branch identity `a1^8 ∈ (six rows) + (e0,e1,ee0,ell1,rs1)`.

Characteristic 0 is inside V42's reach.  Faithful-flat descent of
radical membership from `Q̄` to `Q` is the two-fibre review's own
repair, not a new argument.  V42 is therefore enough for the
**theorem-level** special half of condition 5.  It is not an ordinary
unsplit `a1^N ∈ I_raw` certificate; Opus5 explicitly forbids that
overread.  G2 does not claim one.

Together with the generic unit, the two-fibre theorem gives
`K+(rho)=(1)` **abstractly** for this frozen grade-through-19 chart.
Campaign promotion still requires an explicit condition-2 identity.
The producer already separates those: RESULT.md status is "provisional
pending multipliers and total replay", and stdout carries
`requires-tracked-lift`.  That separation is correct.  This review does
not convert the abstract implication into a promoted identity.

**Verdict: PASS.**

---

## 6. Attack 6 — artifacts, collisions, specialisation, stale pins

Searched and not found:

- `t=c` or any other rational specialisation in the decision script.
- Modular coefficients, `bigint` rings, or `option(redTail)`-only
  reductions used as a verdict.
- Coefficient-only generators (every generator has at least one ring
  variable; the shortest is `((3/8))*e0`).
- Identifier collision: `t` is the parameter, not a variable; `k` and
  `k10_3` are declared ring variables; no `rho`.
- Unmatched parentheses in any of the 58 generators.
- Stale dependency hashes: V43, V43G1, field bridge, V42 triple,
  two-fibre pair, census addendum, and Fable5 review all match their
  pins.
- Pivot-row omission from the source question: the 59-row corpus is
  regenerated and hashed; only the quotient step removes it, with
  multiplier zero on a 58-row unit (Attack 3).
- Compiler writing a constant `1` into `J`.  The harvested script is
  318,853 bytes of genuine dehomogenized rows.

Two inert remarks, neither a verdict defect:

1. G2 does not re-hash the V43 census addendum or the Fable5 delta
   review at runtime, because it never calls `G1.main()`.  Both files
   currently match the hashes hardcoded in G1.  The addendum is
   documentation; the live census is `reconstruct_rows`.  Fable5's
   `leaf_peel_dual` delta is not on G2's call path.
2. RESULT.md's "source tree was made read-only" is not evidenced in
   the harvest.  The algebraic input is independently regenerated, so
   a post-run mutation of the remote tree could not have produced the
   hashed script.

**Verdict: PASS.**

---

## 7. Attack 7 — exact remaining checks before promotion

The producer already withholds promotion.  The next frozen producer
must do all of the following against the **same** 59-row corpus and the
**same** 58-row `Q(t)` ideal.  None of these is supplied by V43G2.

1. **Byte-compare** the ring declaration and all 58 generators to
   `generic_only_qt_decision.sing`
   (`7e3149d9…28b3`).  Any drift is fatal.
2. **Tracked Bezout.**  `liftstd(J,T)` over the same `ring K=(0,t)`,
   replay `matrix(J)*T = matrix(G)`, lift `1` through `G`, form
   `C = T*H`, replay `matrix(J)*C = [1]` exactly in `Q(t)`.  Serialise
   all 58 multipliers, `T`, `C`, and `G`.
3. **59-row map.**  Retain `Tg19_2` with multiplier zero in the source
   map (the quotient isomorphism, not an omission).  Replay the product
   against the 59 hashed total rows, not against a selected subideal.
4. **Minimal support.**  Record which of the 58 multipliers are
   actually nonzero.  Drop-one necessity is optional but the support
   itself is not.
5. **Sigma-residue projection.**  Decompose the dehomogenized identity
   into residue classes modulo `wt(a1)=5`.  Only the weight-zero
   component of the cofactor can become `U(rho^2)`.
6. **Weighted rehomogenization.**  Restore powers of `a1` by the graded
   inverse of `a1=1`, producing an explicit
   `v(t) a1^D` in the homogenised ideal.
7. **Denominator and content clearing.**  Clear `Q(t)` denominators and
   the content of `v(t)` in `Q[t]`.  Write `v(t) = t^s q(t)` with
   `q(0) ≠ 0` (or prove `s=0`).
8. **Special converter if `s>0`.**  Combine with an explicit special
   identity `a1^M − B = t H`, `B ∈ J`, by the repaired two-fibre
   converter of theorem §5, to obtain `q(t) a1^{D+Ms} ∈ J`.  The
   reviewed V42 field-point theorem is **not** a substitute for `B`
   and `H`.  If a constructive special certificate (the live `a1^104`
   lane, or any other ordinary membership) is used, it must be frozen
   and replayed at that step, not merely cited.
9. **Even cofactor.**  Optional averaging under `rho ↦ −rho` to force
   `U(rho)=V(rho^2)`, as permitted by the theorem, not required by it.
10. **Hostile review of that replay**, then and only then a campaign
    statement `K+(rho)=(1)` for this frozen chart.

Even after (1)–(10): the theorem decides only the literal ordered-`a1`,
grade-through-19, maximum-12/order-two chart that defines `J`.  It does
not prove source/landing coverage, the terminal receiver, Gate T, order
two, maximum twelve, or JC2.  V43G1 remains a live independent twin and
is not superseded by this review.

**Verdict: PASS** as a correctly withheld gate.

---

## 8. Firewall

Eligible to record, at the exact scope of the overall paragraph:

- exact generic-fibre unit of the full frozen 58-row/`Q(t)` decision
  after the audited `ez9` pivot;
- equivalently, by the pinned field bridge, generic-fibre unit over
  `Q(rho)`;
- still provisional, `requires-tracked-lift`.

Not eligible:

- unrestricted total certificate;
- promoted `K+(rho)=(1)` identity;
- ordinary unsplit `a1^N ∈ J`;
- any Gate T / Rees / order-two / maximum-twelve / JC2 consequence;
- treating V43G3, or any other unreviewed lift, as already done.

---

## Disclosure

I read the G2 preregistration, result, freeze, compiler, runner, and
the complete Box02 harvest; the G1 compiler, preregistration, and field
bridge; the V43 compiler and census addendum; the Fable5 V43 delta
review; the V42 report, replay pin, and Opus5 review; and the repaired
two-fibre theorem plus its Grok review.  I rehashed every freeze,
evidence, harvest, and pin path listed in §0.  I executed
`reconstruct_rows` once through the hashed G1 loader and byte-compared
the 58 dehomogenized rows to the harvested Singular script.  I did not
run Singular, did not launch AWS, did not edit `AUDIT.md` or
`jc2-lean`, and did not treat V43G3 as evidence.  This report is the
only repository file I created.
