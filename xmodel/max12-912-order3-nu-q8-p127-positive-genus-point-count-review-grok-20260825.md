# Hostile review: positive genus of the pinned geometrically integral plane curve `H(w,v)` over `F_127`

Date: 2026-08-25
Reviewer: independent hostile algebraic-geometry / exact-software referee
(Grok; different model from the producer lane and from the Claude
integrality review this producer consumes).
Target claim: `xmodel/max12-912-order3-nu-q8-p127-positive-genus-point-count-20260825.md`
Case: `cases/max12_912_order3_nu_q8_p127_extension_point_count_aws_20260825/`
Consumed input: CONFIRMED review
`xmodel/max12-912-order3-nu-q8-p127-candidate-plane-integrality-review-claude-20260825.md`
of
`xmodel/max12-912-order3-nu-q8-p127-candidate-plane-integrality-20260825.md`.
Verdict: **CONFIRMED** — no mathematical, source, or custody defect that
breaks the standalone theorem; optional wording hardenings in §9.

This review closes the "hostile different-model review required" status
line carried by the producer report. It proves, from the frozen two-host
count and the consumed geometric-integrality theorem, that the smooth
projective normalization of the pinned curve has positive genus, and
nothing larger.

## 0. Execution-environment disclosure

This review session has **no Bash, no CAS, and no network access**. I
could not execute python-flint, could not recompute any SHA-256, and
could not unpack the two harvest tarballs. Consequently the verdict
rests on two explicitly separated tiers:

- **Hand-verified this session (independent of the producer):** every
  line of `count_shard.py`, `aggregate.py`, `direct_control.py`,
  `replay.py`, `dispatch.sh`, `run_shard.sh`, `run_aggregate.sh`,
  `run_direct_control.sh`, `run_replay.sh`; the integer-division
  partitions for 16 and 8 shards; the quadratic-reciprocity proof that
  `x^2-x+3` is irreducible over `F_127`; the fibre-formula argument of
  §5, including squarefreeness, gcd-degree conventions, both partials,
  and missed-affine-point attacks; the genus argument of §7, including
  uncounted points at infinity and singular branches; every shard
  endpoint `(start,stop,w_count,total,smooth,singular)`; pairwise
  Box02-pair versus r6d block-sum identities; the four control fibres
  against both hosts' `per_w` rows; and the complete V1/V2 wrapper
  separation.
- **Trusted from the frozen fail-closed attestation web (not
  re-executed):** python-flint `0.9.0` `FQ_NMOD` evaluation of
  `gcd`, `pow_mod`, and derivatives on each fibre; all SHA-256
  equalities (`run.meta`, `MANIFEST.sha256`, `FREEZE.md`, producer
  §3, `replay.py` pins), which are mutually consistent to the byte
  across those surfaces; and the consumed geometric-integrality
  theorem, which this session re-read in full but did not re-prove.
  Residual engine trust (one library family, two hosts) is disclosed,
  not eliminated.

The two `.tgz` files were not unpacked here. The harvest trees are the
unpacked shard/V1-wrapper contents and were read as such.

## 1. Files read (complete, read-only)

- `xmodel/max12-912-order3-nu-q8-p127-positive-genus-point-count-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-candidate-plane-integrality-20260825.md`
- `xmodel/max12-912-order3-nu-q8-p127-candidate-plane-integrality-review-claude-20260825.md`
  (verdict CONFIRMED)
- Every file of
  `cases/max12_912_order3_nu_q8_p127_extension_point_count_aws_20260825/`
  except the two binary harvest tarballs, which were audited by their
  MANIFEST / `replay.py` pins and by the unpacked harvest trees:
  `README.md`, `REGISTRATION.md`, `FREEZE.md`, `MANIFEST.sha256`,
  `count_shard.py`, `aggregate.py`, `direct_control.py`, `replay.py`,
  `dispatch.sh`, `run_shard.sh`, `run_aggregate.sh`,
  `run_direct_control.sh`, `run_replay.sh`;
  both V2 aggregates (`result.json`, `run.meta`, `stderr.log`, empty
  runner streams); the r6d direct-control and portable-replay
  endpoints; both dispatch ledgers; both failed V1 aggregate wrappers
  (`run.meta` truncated, empty runner streams, no `result.json`);
  all 16 Box02 shard directories and all 8 r6d shard directories
  (`result.json`, `run.meta`, `stderr.log`, empty runner streams).
- Pinned candidate, header / monic tail / endpoint only (full 8,893-line
  census is the consumed integrality review's work):
  `cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/interpolation_candidate.json`
- Off-case consistency control cited by producer §3, not load-bearing
  here:
  `cases/max12_912_order3_nu_q8_p127_candidate_point_count_aws_20260825/`
  (two-host stdlib enumerator, stdout SHA
  `e5c9d9bcdca1a568ab2dba6f9fa123573b5e2a8477920f7896d054770bd33777`,
  counts 126 affine / 124 smooth / 2 singular over `F_127`).
- Repo search for errata naming this producer: none.

## 2. Exact claim under audit

Let `H(w,v) ∈ F_127[w,v]` be the pinned polynomial of SHA-256
`9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce`.
The consumed CONFIRMED review proves that the affine plane curve
`H=0` is geometrically integral over `k=F_127` and that `(w,v)=(71,50)`
is a smooth `k`-rational point. Let `C` be the smooth projective
normalization of this curve (equivalently: the unique smooth projective
geometrically integral `k`-curve with function field `k(H=0)`).

**Claimed:** `g(C)>0`.

**Not claimed:** quotient membership, source-component identity,
characteristic-zero specialization, selected-contact trajectory
exclusion, maximum twelve, or any JC2 conclusion. The numerical
inequality `16168>16130` is load-bearing only after geometric
integrality is attached; the aggregator key
`genus_positive_if_geometrically_integral` is named accordingly.

## 3. Item 1 — candidate pin, construction of `F_(127^2)`, irreducibility of the quadratic modulus

**3.1 Pin chain.** `count_shard.py` and `direct_control.py` refuse to
run unless `sha256(candidate)` equals the hard pin `9061…a7ce`, then
(in the shard path) additionally require `status=="PASS"`, `prime==127`,
`degree_v==190`, and `nonzero_support["190"]==[[0,1]]`. `run_shard.sh`
and `run_direct_control.sh` resolve the candidate to
`cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/interpolation_candidate.json`.
Every one of the 24 shard `run.meta` files, both V2 aggregate metas
(via the shard metas they hash), and the direct-control meta record
that same SHA on the box path. The JSON itself, as read, has
`"190": [[0,1]]` immediately followed by `"2"`, `"prime": 127`,
`"degree_v": 190`, `"status": "PASS"`, and
`"maximum_support_count": 21`. Coherent with the consumed integrality
pin.

A key above 190 would `IndexError` on the length-191 coefficient
buffer; a `w`-exponent above 21 would `IndexError` on `w_powers`.
Both are fail-closed. Per-fibre the shard also asserts
`h.degree()==190` and leading coefficient `1`, so a drifted leading
term cannot silently drop degree. Stronger runtime monicity than the
integrality generator, which only checked the `"190"` key.

**3.2 Field construction.** Both hosts construct
`fq_default_ctx(127, 2, "a", fq_type="FQ_NMOD")` under python-flint
`0.9.0`. Every shard and both aggregates record
`field_modulus = "x^2 + 126*x + 3"`, i.e. `x^2 - x + 3` in
`F_127[x]`. Enumeration is
`w = (index mod 127) + (index // 127)·a` for
`index ∈ [0, 16129)`, equivalently
`{ i + j a : 0 ≤ i,j < 127 }`. Linear independence of `{1,a}` over
`F_127` is exactly irreducibility of the modulus, proved next, so
this is a complete set of field elements, in the same order used by
`direct_control.py` (`for j in range(P) for i in range(P)`).

**3.3 The modulus is irreducible.** Discriminant of `x^2 - x + 3` is
`1-12 = -11 ≡ 116 (mod 127)`. Euler's criterion says this is a square
if and only if `116^63 ≡ 1 (mod 127)`. Independently of that power,
quadratic reciprocity gives the Legendre symbol:

```text
(116/127) = (4·29/127) = (29/127)
          = (127/29)     because (29-1)/2 · (127-1)/2 = 14·63 is even
          = (11/29)      because 127 ≡ 11 (mod 29)
          = (29/11)      because (11-1)/2 · (29-1)/2 = 5·14 is even
          = (7/11)
          = -(11/7)      because (7-1)/2 · (11-1)/2 = 3·5 is odd
          = -(4/7) = -1.
```

So `x^2 - x + 3` has no root in `F_127` and is the quadratic field.
The producer's displayed identity `116^63 ≡ -1 (mod 127)` is Euler's
criterion for the same symbol; I did not recompute the power.

## 4. Item 2 — the fibre formula, attacked

Fix `K = F_(127^2)`, `Q = 16129`. For each `w ∈ K` the code forms
`h = H(w,·) ∈ K[v]`, asserts it is monic of degree 190, and sets

```text
R_w = gcd(h, v^Q - v),
S_w = gcd(R_w, h_v, h_w),
```

implemented as `h.gcd(v.pow_mod(Q, h) - v)` and
`rational_roots.gcd(hv).gcd(hw)`.

**4.1 `v^Q - v` is squarefree with roots exactly `K`.** Its derivative
is `Q v^{Q-1} - 1 = -1` in characteristic 127, hence coprime to
`v^Q-v`. The roots are the elements of `K` by Fermat. Consequently
`R_w` is squarefree, and `deg R_w` equals the number of *distinct*
`K`-roots of `h`. Repeated roots of `h` in `K` are counted once, which
is the correct convention for points of the set `V(H)(K)`.

**4.2 `pow_mod` identity.** In `K[v]`,
`gcd(h, v^Q-v) = gcd(h, (v^Q-v) mod h) = gcd(h, v^Q mod h - v)`.
The call `v.pow_mod(Q, h) - v` is that remainder. The monicity gate
makes the modulus of `pow_mod` monic of degree 190. This is the
standard Euclidean reduction, not an extra hypothesis.

**4.3 Zero and constant gcd degrees.** Over a field, a nonzero gcd is
defined up to units. python-flint's `degree()` of a nonzero constant
is 0, not `-1`: empty fibres are present in the frozen `per_w` tables
and are recorded as `[index, 0, 0, 0]` (examples: indices 5, 1008,
16127, on both hosts). A `-1` convention would have tripped
`min(fibre_total, fibre_singular, fibre_smooth) < 0` and failed the
shard closed. The zero polynomial cannot occur as a gcd because `h`
is monic of degree 190. Empty fibres contribute 0 points, as required.

**4.4 Both partials.** `hv = h.derivative()` is `∂H/∂v` evaluated at
the specialized `w`. `hw` is assembled from the support as
`Σ_{e≥1} (c·e mod 127) w^{e-1} v^d`. Operator precedence
`coefficient * w_degree % P` is left-to-right, so this is
`(c e) mod 127` times `w^{e-1}`. Every recorded `w`-exponent is at
most 21, hence nonzero in `F_127`; there is no vanished-derivative
accident from `e ≡ 0 (mod p)`. The `e=0` terms are correctly omitted.
Leading `v`-degree of `H` is the constant 1, so
`∂H/∂v` has leading term `190 v^{189}` with `190 ≡ 63 ≠ 0 (mod 127)`:
`hv` is never the zero polynomial, so `gcd(R_w, hv)` is never `R_w`
for the trivial reason `hv=0`.

`S_w = gcd(R_w, hv, hw)` is, because `R_w` is squarefree, the product
of `(v-α)` over those `α ∈ K` at which `H(w,α)=H_v(w,α)=H_w(w,α)=0`.
For a hypersurface in `A^2` over a perfect field, the Jacobian
criterion says precisely that these are the singular points of the
fibre. Geometric reducedness of `H=0` is part of the consumed
geometric-integrality theorem, so the criterion applies. Left-associated
`.gcd(hv).gcd(hw)` is the three-input gcd up to units; degrees are
invariant.

A vertical tangent (`H_v=0`, `H_w≠0`) is a smooth point and is *not*
placed in `S_w`. That is correct, and the squarefree `R_w` still
counts it once.

**4.5 Smooth count.** `fibre_smooth = deg R_w - deg S_w`. `S_w` divides
`R_w`, so this is nonnegative; the negative-count gate is a second
closure. Summing over a complete set of `w` therefore counts every
smooth affine `K`-point of `V(H)` exactly once, and every singular
affine `K`-point exactly once.

**4.6 Missed affine points.** The loop is over all `w ∈ K`, and for
each `w` over all `v ∈ K` at which `h(v)=0`. That is `A^2(K)`. Degree
of `h` never drops, so there is no hidden fibre in which `H(w,·)`
vanishes identically. Points at infinity are deliberately uncounted
(§7).

**4.7 Direct-enumeration cross-check of the formula.** On fibres
`w=0, 39, 71, a+1` (indices 0, 39, 71, 128), `direct_control.py`
evaluates `h(v)` at every element of `K` and classifies each zero by
the two partials. All four fibres match the gcd counts exactly:

| `w` | gcd `(total, smooth, singular)` | direct | both hosts' `per_w` |
|---|---|---|---|
| `0` | `(8,7,1)` | `(8,7,1)` | `(8,7,1)` |
| `39` | `(4,3,1)` | `(4,3,1)` | `(4,3,1)` |
| `71` | `(3,3,0)` | `(3,3,0)` | `(3,3,0)` |
| `a+1` | `(2,2,0)` | `(2,2,0)` | `(2,2,0)` |

The fibre `w=71` is the consumed smooth rational point; it is smooth
on the count, as required. Two of the four sampled fibres are
singular. The control is a same-engine method split (evaluation versus
gcd), not an independent library. It is a real attack on the fibre
formula, and the formula survives.

## 5. Item 3 — partitions, reconciliation, two-host aggregates, V1/V2, independence

**5.1 Intervals.** `dispatch.sh` uses
`start = index * 16129 / shard_count`,
`stop = (index+1) * 16129 / shard_count`
in integer division. The ledgers match the arithmetic:

Box02, 16 shards, host `ip-172-30-0-186`, prefix
`q8_p127_fq2_points_box02_v1`, dispatched 2026-08-25T09:30:42Z:

```text
[0,1008), [1008,2016), …, [14112,15120), [15120,16129)
```

fifteen width-1008 blocks and a final width-1009 block
(`16·1008 = 16128`).

r6d, 8 shards, host `ip-172-30-0-45`, prefix
`q8_p127_fq2_points_r6d_v1`, dispatched at the same UTC second:

```text
[0,2016), [2016,4032), …, [12096,14112), [14112,16129)
```

seven width-2016 blocks and a final width-2017 block
(`8·2016 = 16128`). Disjoint, adjacent, covering `[0, 16129)`
exactly. Every shard `result.json` repeats its `(start,stop,w_count)`
and its `per_w` index list is the integer range
`[start, stop)` (spot-checked at 0, 39, 71, 128, 1007/1008/1009,
16127/16128 on both hosts). `aggregate.py` re-asserts this, plus
internal sum reconciliation
`total = smooth + singular = Σ per_w`, before accepting a shard.

**5.2 Per-shard endpoints, summed by hand.**

Box02:

| shard | interval | total | smooth | singular |
|---|---|---:|---:|---:|
| i00 | [0,1008) | 1112 | 1110 | 2 |
| i01 | [1008,2016) | 1077 | 1077 | 0 |
| i02 | [2016,3024) | 999 | 999 | 0 |
| i03 | [3024,4032) | 990 | 990 | 0 |
| i04 | [4032,5040) | 1020 | 1020 | 0 |
| i05 | [5040,6048) | 999 | 999 | 0 |
| i06 | [6048,7056) | 980 | 979 | 1 |
| i07 | [7056,8064) | 986 | 985 | 1 |
| i08 | [8064,9072) | 974 | 973 | 1 |
| i09 | [9072,10080) | 1008 | 1007 | 1 |
| i10 | [10080,11088) | 956 | 956 | 0 |
| i11 | [11088,12096) | 1052 | 1052 | 0 |
| i12 | [12096,13104) | 973 | 973 | 0 |
| i13 | [13104,14112) | 991 | 991 | 0 |
| i14 | [14112,15120) | 1082 | 1082 | 0 |
| i15 | [15120,16129) | 975 | 975 | 0 |
| **sum** | **[0,16129)** | **16174** | **16168** | **6** |

r6d:

| shard | interval | total | smooth | singular |
|---|---|---:|---:|---:|
| i00 | [0,2016) | 2189 | 2187 | 2 |
| i01 | [2016,4032) | 1989 | 1989 | 0 |
| i02 | [4032,6048) | 2019 | 2019 | 0 |
| i03 | [6048,8064) | 1966 | 1964 | 2 |
| i04 | [8064,10080) | 1982 | 1980 | 2 |
| i05 | [10080,12096) | 2008 | 2008 | 0 |
| i06 | [12096,14112) | 1964 | 1964 | 0 |
| i07 | [14112,16129) | 2057 | 2057 | 0 |
| **sum** | **[0,16129)** | **16174** | **16168** | **6** |

Every Box02 adjacent pair equals the corresponding r6d block
(e.g. `1112+1077=2189`, `980+986=1966`, `1082+975=2057`), including
singular subtotals. That is a genuine partition-refinement identity,
not only a match of global sums. All 24 shards have `rc=0`,
`status=PASS`, candidate SHA, modulus string, and empty
`runner.stderr` / `runner.stdout` (empty-input SHA
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`).
Maximum shard RSS is 33,508 KiB on Box02 (i06) and 33,664 KiB on r6d
(i00), matching the producer. Wall times are ~10 s per 1008-fibre
Box02 shard and ~21 s per 2016-fibre r6d shard, a consistent rate.

**5.3 V1 versus V2 aggregates.** The V1 wrapper
`run_aggregate.sh` of SHA
`de449e44bb3f2ac4f0f9e138036800f80198f78da922dd0fdd62f18711a448ec`
is the file hashed into both V1 `run.meta` files. Those metas stop
after the four source hashes: no shard hashes, no `rc=`, no
`result.json`. Both V1 wrappers started at 09:37:04Z and aborted
inside the pre-aggregation `grep` over shard JSON. This is exactly
an over-strict indentation-sensitive match against
`json.dumps(..., indent=2, sort_keys=True)` output (in which
`"status"` is not the last key of a shard record, so the line carries
a trailing comma). The V1 directories are non-evidentiary. They are
*not* "only inside the raw custody tarballs": they are also unpacked
under `harvest_box02/` and `harvest_r6d/`. That is a README wording
defect, not a custody defect. The accepted endpoints are the V2
aggregates, which hash a different wrapper
(`83819ad66a4aefe264b8e57d4ed7b53e9649cb454fbfd4fad7b04588e95c88e2`)
and the *same* shard `result.json` bytes already frozen at 09:30.
V2 is a re-wrap, not a re-count. Both V2 runs exited 0 at 09:39:26Z
with counts `(16174, 16168, 6)`, `p1_rational_point_count=16130`,
`genus_positive_if_geometrically_integral=true`, and result SHAs

```text
Box02  031da7561db2eaffad4ec12310b79ded986964accd35b65e356da4b3b7ac7614
r6d    528de912e52df836de5d65219cbb8b29fcdd513817bd88b86777ce7bc01f66bd
```

matching producer §3, `FREEZE.md`, `MANIFEST.sha256`, and
`replay.py`. The two JSON files differ only in `shard_count`
(16 versus 8), as claimed.

**5.4 Source and hash pins.** `replay.py` hard-pins the seven
executable sources, both V2 aggregate JSON files, both harvest
tarballs, and the direct-control JSON, then re-walks every shard:
`rc=0`, source SHA substring in `run.meta`, empty runner streams,
modulus string, interval integrity, internal sums, and global totals
`[16174, 16168, 6]`. The r6d portable replay of that auditor (Python
3.12.3, no flint) exited 0 with SHA
`1cd4051ed8b099a64d68c934f2d7be14832b30f5de6b25aa685e591ff6eeb202`.
Every hash I can compare across `MANIFEST.sha256`, V2 `run.meta`,
shard `run.meta`, `replay.py` constants, and producer §3 agrees to
the byte. I did not recompute SHA-256.

**5.5 The two host runs are identical-source replay, not independent
engines.** Phrase this accurately. Both hosts ran the same
`count_shard.py`
(`ec1fafa373f2f46c6f6899bfb424dc2510323f8930ac1d52408e32d35efaec12`),
the same candidate, the same python-flint `0.9.0` `FQ_NMOD` context,
and recorded the same modulus string. They are two machines
(`ip-172-30-0-186` versus `ip-172-30-0-45`, distinct repo checkouts
`jc2q8-box02` versus `jc2q8`), dispatched at the same UTC second,
with distinct partition widths. What this is: concurrent two-host
identical-source execution, plus a partition-refinement identity on
every 2016-wide block, plus a same-engine evaluation-versus-gcd
control on four fibres. What this is not: an independent
implementation, an independent library, or an independent field
construction. The producer body ("independently partitioned AWS
runs", "JSON differs only in the recorded shard count") is accurate.
The section title "Independent exact execution" is slightly stronger
than the evidence. Residual python-flint trust remains; it is
mitigated by the four-fibre direct loop and by the blockwise
cross-host identity, not cancelled.

**5.6 The four fibre controls, and the off-case base-field enumerator.**
The four fibres are one program, tag
`q8_p127_fq2_points_direct_control_r6d_v1`, SHA
`9cc104c5d826c607c8e134cbaaf0a187220a0b42fdcc9e54863bf721d1bc24b3`,
rc 0 in one second of wall time, RSS 34,624 KiB. They include two
singular fibres (`w=0,39`) and two smooth fibres (`w=71` and
`w=a+1`). They do not cover the other four singular fibres (one each
in Box02 i06, i07, i08, i09). README's "including both singular
fibres" is true of the sample and false if read as completeness of
the singular locus; see §9(H2).

The base-field stdlib enumerator cited in producer §3 lives in a
sibling case, agrees on two hosts, and records 126 affine
`F_127`-points, 124 smooth and 2 singular, versus `#P1(F_127)=128`.
The inequality `124 ≤ 128` goes the wrong way for a genus lower
bound, which is why this producer moved to `F_(127^2)`. It is a
consistency control only, as the producer states, and is not in this
case's MANIFEST. I treat it as non-evidentiary for the theorem.

## 6. Item 4 — the genus argument, proved, including infinity and singular branches

Let `k = F_127` and `K = F_(127^2)`. Let `X = Spec k[w,v]/(H)`. By
the consumed theorem, `X` is geometrically integral and
`x = (71,50) ∈ X(k)` is smooth. Let `F = k(X)`. Because `k` is
perfect and `X` is geometrically integral, `F/k` is a regular function
field of one variable (constants exactly `k`, separable). Let `C/k`
be the unique smooth projective geometrically integral curve with
`k(C)=F`. Equivalently, `C` is the normalization of any projective
model of `X`, in particular of the projective closure of `X` in
`P^2`.

**6.1 Smooth affine `K`-points inject into `C(K)`.** Let `U ⊂ X` be
the smooth locus. `U` is a smooth curve, hence normal, and the
birational map `U ⇢ C` is a morphism; a birational morphism of smooth
curves is an open immersion. Open immersions remain open immersions
after base change to `K`, so `U(K) → C(K)` is injective. The Jacobian
criterion identifies `U(K)` with the 16,168 counted smooth affine
`K`-points. Therefore `#C(K) ≥ 16168`.

Two distinct smooth affine points cannot collide on `C`: the
normalization is an isomorphism over the regular locus. A node or
cusp is singular, hence among the 6, not among the 16,168. A vertical
tangent with `H_w ≠ 0` is smooth and is counted once, correctly.

**6.2 Genus zero with a `k`-point is `P^1_k`.** A geometrically
integral smooth projective curve of genus 0 over any field, possessing
a rational point, is isomorphic to `P^1` over that field:
Riemann-Roch gives `ℓ([pt])=2`, hence a degree-1 map to `P^1`, hence
an isomorphism. The consumed smooth point `x` is regular, so it lifts
to a unique point of `C(k)`. Thus `g(C)=0` would imply
`C ≅ P^1_k`, hence `#C(K) = #P^1(K) = Q+1 = 16130`.

(Over a finite field the `k`-point is actually redundant: every
genus-0 curve over a finite field has a rational point, by
Chevalley–Warning on the anticanonical conic. The producer does not
need this, and does not claim it. The consumed point makes the
classification elementary.)

**6.3 `16168 > 16130` is sufficient, including uncounted infinity and
singular branches.** The comparison is a *lower* bound on `#C(K)`
against the exact count on `P^1(K)`. Points of `C` lying over the
line at infinity of the plane model, and extra branches of `C` over
the 6 singular affine points, can only increase `#C(K)`. They cannot
cancel any of the 16,168 injected smooth affine points. The
inequality therefore survives both omissions, and in the direction
that matters. The numerical excess is 38, well inside the Weil range
`2g√Q` already for `g=1` (`2√16129 = 254`); this is a sanity check,
not a proof, and is not used.

Hence `g(C)=0` is impossible, so `g(C)>0`.

## 7. Item 5 — standalone-plane scope enforced

Checked surfaces: producer §4, case README, `REGISTRATION.md`
forbidden-inference clause, `FREEZE.md` exclusions, aggregator key
name `genus_positive_if_geometrically_integral`, and `replay.py`
`"scope": "standalone pinned H over F_127 only"`. They agree. No
sentence of the producer or the case asserts quotient membership,
component identity, characteristic-zero specialization, trajectory
exclusion, maximum twelve, or JC2. The title's lane label ("Max12
`(9,12)` selected-Q8") is naming, as in the consumed integrality
review, not scope leakage. The already-frozen specialization bypass
is correctly described as a future composition, not a conclusion of
this report.

## 8. Custody web

Mutual byte-consistency, on every surface I can compare without
re-hashing:

| object | SHA-256 prefix |
|---|---|
| `count_shard.py` | `ec1fafa373f2…faec12` |
| `aggregate.py` | `b068081d154e…451c43` |
| `dispatch.sh` | `6d863b475710…564072eb` |
| `run_shard.sh` | `cd1bed208596…f9d02c2f` |
| V2 `run_aggregate.sh` | `83819ad66a4a…e95c88e2` |
| V1 `run_aggregate.sh` (rejected wrapper) | `de449e44bb3f…11a448ec` |
| `direct_control.py` | `933ca69de6fb…71bdba65` |
| `replay.py` | `343238d8577a…71e2e925` |
| Box02 V2 `result.json` | `031da7561db2…b7ac7614` |
| r6d V2 `result.json` | `528de912e52d…c01f66bd` |
| direct-control `result.json` | `9cc104c5d826…d1bc24b3` |
| portable-replay `result.json` | `1cd4051ed8b0…6eeb202` |
| candidate | `906172629508…54daa7ce` |
| empty runner streams | `e3b0c44298fc…852b855` |

`FREEZE.md` quotes `MANIFEST.sha256` as
`8de0e649576e…c12578b7` and the producer report as
`c4c4ebdf59a9…f64a00a`; those two hashes were not recomputed here.
`FREEZE.md` itself is correctly not listed in the MANIFEST (a freeze
file that hashed itself would be circular). The candidate JSON is
not listed in this case's MANIFEST; it is pinned by the runtime gate
and by every `run.meta`, the same pattern the integrality review
recorded as optional H3.

## 9. Findings and smallest repairs

No defect requiring repair was found. Ranked observations, all
optional:

- **(H1) Independence wording, producer §3 title.** The two AWS runs
  are concurrent identical-source replay with distinct partitions, not
  independent engines. The body already says this. Smallest repair:
  retitle §3 to "Two-host identical-source partitioned execution".
  Non-blocking.
- **(H2) "Both singular fibres".** There are six singular affine
  `K`-points on six fibres; the four-fibre control hits two of them.
  Smallest repair, in README and producer §3: "including the two
  singular fibres among the four sampled". Non-blocking: the control
  is a formula check, not a census of singularities.
- **(H3) V1 location.** README says the failed V1 aggregate
  directories "remain only inside the raw custody tarballs". They are
  also unpacked in `harvest_*/`. Smallest repair: "remain in the
  harvest trees and the custody tarballs, without `result.json`".
  Non-blocking: V2 is the accepted endpoint, and `replay.py` never
  reads V1.

## 10. Verdict

Conditional only on the consumed CONFIRMED geometric-integrality
theorem, the smooth projective normalization of the pinned curve
`H=0` over `F_127` has positive genus. The candidate pin and the
quadratic modulus are sound; `v^Q-v` is squarefree with roots exactly
`K`; `deg gcd(H(w,v), v^Q-v)` counts distinct affine `K`-points of
the fibre and `deg gcd(R_w, H_v, H_w)` counts the singular ones,
including empty-fibre degree-0 and repeated-root-once conventions;
both 16-shard and 8-shard partitions cover `F_(127^2)` exactly, every
shard reconciles internally, and the two host block-sums agree; V1 is
a failed indentation-sensitive wrapper and is not evidence; V2 is the
accepted re-wrap of the original shard bytes. The 16,168 smooth affine
`K`-points inject into `C(K)`; a genus-zero curve with the consumed
smooth `k`-point is `P^1_k` with `16130` points over `K`; uncounted
points at infinity and singular branches only enlarge the left-hand
side. Scope is the standalone plane curve. Execution-environment
limits (no shell/CAS/network: flint evaluations and SHA-256 taken
from the interlocking frozen attestations) are disclosed in §0 and
do not affect the verdict.

CONFIRMED
