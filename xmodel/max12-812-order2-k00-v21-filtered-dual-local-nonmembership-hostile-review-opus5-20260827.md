# Hostile review: V21R1 exact filtered-dual local nonmembership (K00, order two, max 12)

Date: 2026-08-27
Reviewer model: **Claude Opus 5** (`claude-opus-5`), Claude Code agent.
Producer directory reviewed:
`cases/max12_812_order2_u2_62_k00_filtered_dual_local_nonmembership_v21_20260827/`

## Verdict

**PASS** at the exact charged scope.

Every producer PASS marker was treated as untrusted and independently
re-derived.  All three charged nonmembership statements were reproved from
the frozen V17 source text by two logically independent routes on this
review host, one of which does not use a Gröbner or syzygy computation at
all.  No defect was found that affects the charged conclusion.  Ten additive
corrections / scope clarifications are listed in §8.

## 0. Tool versions used

```text
host          macOS 14.6 (Darwin 23.6.0), arm64
python3       3.9.6 (/usr/bin/python3); no sympy / flint / numpy / sage present
Singular      4.4.1 (44105, 64 bit) arm64-Darwin, GMP 6.3.0, NTL 11.6.0, FLINT 3.6.0
sha256sum     GNU coreutils 9.11
```

The producer ran on registered AWS Box01 (x86-64 Linux).  This review ran on
arm64-Darwin with a different Singular build; the Singular transcript and the
serialized syzygy module reproduced **byte-for-byte** across that
architecture change.

All replay code was written fresh for this review (a hand-written
recursive-descent tokeniser/parser for the Singular polynomial and
`gen(i)` module grammar, independent of the producer's `ast`-based parser)
and staged under `/tmp/jc2rev/`.  Nothing in the producer tree, in
`jc2-lean`, or in any canonical ledger was modified.

---

## 1. Attack 1 — rehash, chronology, and the exact R1 delta

### 1.1 Charged hashes

All nine charged hashes reproduce exactly:

```text
27fb885a1602257c2885e89c194c2d5f5bb2e7a3709f88f366e0c2807a5ad5dc  PREREGISTRATION.md
137fdc18c349a549949e90c3d515b5e08e01d9f69a6be5f8efbbf97b78175d7d  PREREGISTRATION_R1.md
06544be839c794e452de101a75a0926d1a99acc4ba86b27470eaa9d2de15fd20  FAILURE_R0.md
fd97d0b80b48bd46afd45a21a29a50f18592a68aac9047ad94d9abfb438ad875  verify_filtered_dual_corollary_v21.py
4c35362b7223566317ca346bd261fb13023fbb3d8a48aef2908dd00d1a168026  SOURCE_FREEZE_R1.sha256
38c6dd45b888ec04a5c0b9bdd4b93625a1df491b4e4f63851f5546cb1d7d465f  INPUT_FLAT.sha256
b514ef728afd47518246727efc5a7b41efb768707c4fe08f5625a96a8d32efb9  RESULT.md
7341d67bb6abfba9ce1b99d6670360721214aaf6bbb51165dbf84964c65e7ad3  aws_q_box01_r1_pass/run/output/RESULT.json
00159ec022932932373fc294980541ca791a173e5bbdbe58072d84d6b3b74b49  aws_q_box01_r1_pass/EVIDENCE.sha256
83832f380ce11a491c9799e50ff8b36b5fbc3a6b0d5b5dc52d90b6239c129a7a  .../FRESH_SYZ6_MODULE.txt  (== input/syz6.txt)
```

Two hashes not in the charge but load-bearing:

```text
97e5721a21a169a3123bd843c59ea1241126a4b0a221e2f28a89a313481069ae  SOURCE_FREEZE.sha256      (R0 freeze)
2217222bbf07baf423dbc6c973cf1fc8931c2240466b085860f103ee89a2700c  AWS_REGISTRATION.md
```

### 1.2 Manifests

* `EVIDENCE.sha256`: **49/49 OK** after remapping the AWS-absolute prefix
  `cases/…_v21_20260827/aws_q_box01_r1_pass/`.  The harvested tree has 50
  files; the 50th is `EVIDENCE.sha256` itself, correctly self-excluded.
* `INPUT.sha256` / `INPUT_FLAT.sha256`: **31/31 OK**, and the harvested
  `input/INPUT.sha256` is byte-identical to the frozen source-tree
  `INPUT_FLAT.sha256`.
* R1 harvested source tree == `SOURCE_FREEZE_R1.sha256` (5/5).
* R0 harvested source tree == `SOURCE_FREEZE.sha256` (3/3), pinning the R0
  verifier at `c96a647a89f3730e7000a170c35cee88cee960eb99fa531b7c56b1cc796f3ee3`.

### 1.3 Chronology

```text
R0 lane   …_v21_20260827T120855Z_box01   PID 620534   exit 1, 8.26 s, 59 592 KiB RSS
R1 lane   …_v21r1_20260827T121323Z_box01 PID 621090   exit 0, 10.40 s, 59 536 KiB RSS
```

R1 strictly follows R0 by lane timestamp (12:08:55Z → 12:13:23Z) and PID.
Local freeze mtimes are consistent (`SOURCE_FREEZE.sha256` 05:08 PDT =
12:08 UTC, then `PREREGISTRATION_R1.md` / `FAILURE_R0.md` 05:12, R1 verifier
05:12, `SOURCE_FREEZE_R1.sha256` 05:13, `RESULT.md` 05:15).  R1's telemetry
matches `RESULT.md` (one core, 59 536 KiB, 10.40 s, zero swap).

The R0 packet is nonpromotable in fact, not only by declaration: it has no
`input/`, no `EVIDENCE.sha256`, and no `RESULT.json`.

### 1.4 The R1 delta — full diff audited

The complete `diff` of R0 vs R1 verifier source contains exactly three
hunks:

1. **Module comparison.**  `reduce(T,GF)`/`reduce(Tf,GT)` compared to the
   literal zero module, replaced by an explicit per-generator loop
   `vr=reduce(T[j],GF); if (vr!=0) {moduleeq=0;}` in both directions.
2. **`exit(integer)` → `quit`** at the four fail-closed guards and at the
   terminal statement.
3. **Additive** (not in the charge): an `EXPECTED_PREREG_R1` hash gate on
   `PREREGISTRATION_R1.md` plus the corresponding `r1_preregistration_sha256`
   field in `RESULT.json`.

Nothing else changed: the input manifest, hash gates, polynomial parsing,
syzygy/image/target formulas, matrix re-emission, dual replay, pairings,
lemma text, endpoint, dependency repair and firewall strings are byte-equal.

**I reproduced the R0 failure mode exactly** on this host:

```text
R0_STYLE rem1==0 : 0        size(rem1)=0   ncols(rem1)=66
R0_STYLE rem2==0 : 0        size(rem2)=0   ncols(rem2)=66
EVERY_COLUMN_OF_BOTH_RESIDUALS_IS_ZERO=1
```

So `FAILURE_R0.md` is precisely right: the residual modules retain 66 zero
columns, `module==0` is false for them in Singular 4.4.1, and the underlying
mathematics was already correct in R0.  The R1 repair tests exactly the right
predicate and is not a weakening.  The `exit(82)` diagnostic in the R0
transcript is likewise reproduced by the charged R0 source.

**Conclusion for attack 1: confirmed**, with the one additive finding that
the R1 delta is two semantic changes *plus* one administrative freeze gate.

---

## 2. Attack 2 — independent reconstruction of rows, loads, `h`, `u_i`,
syzygies, images and targets

Parsed with my own grammar implementation from the frozen bytes.

### 2.1 The six unloaded rows and the seventh row

`prelude_Q.sing` (`5b0a77e6…`) is **byte-identical to lines 1–8 of
`v17_Q.sing`**, and `v17_Q.sing` hashes to
`9e22780c0f9b38f2e502b08ac51c1b9d8fee21e7b40e9569d08d77a3683d8b5c`, which is
exactly the frozen V17 exact compiled source pinned by
`cases/…_firstorder_load_cokernel_v17_20260827/aws_q_box01_timeout_30m/compiled.sha256`
and required by V18R2's preregistration.  The row source map is therefore
closed, not assumed.

```text
r1  16 terms  ord 2 deg 4        r5  40 terms  ord 2 deg 5
r2  23 terms  ord 2 deg 4        r6  42 terms  ord 3 deg 6
r3  27 terms  ord 2 deg 5        r7  57 terms  ord 2 deg 6
r4  36 terms  ord 2 deg 5
```

All seven have zero constant term.  V17's own row audit is reproduced:
`rr_i == r_i` for i = 1…7.

### 2.2 `h`, `u_i`, and the V14R1 base relation

`h.txt` and `u1.txt … u6.txt` equal the `poly h`, `poly u1 … u6`
declarations in `v17_Q.sing`.  `h = 63*d4 + 20`, so `h(0) = 20 ≠ 0` and `h`
is a unit in `R_m` — the fact the whole target construction rests on.

Independently recomputed over `Q`:

```text
h*r7 - (u1*r1 + u2*r2 + u3*r3 + u4*r4 + u5*r5 + u6*r6) == 0     CONFIRMED
```

This is V17's `basereplay` gate and V14R1's relation `h = 63*d4 + 20`; it
holds exactly, which is what makes `D_X` the honest first-order variation of
that relation.

### 2.3 The 66 serialized syzygies

`syz6.txt` splits into exactly **66** top-level module vectors.  For every
`j`, `Σ_{i=1..6} T[j][i]·r_i = 0` exactly over `Q` — **66/66 confirmed** by my
own arithmetic, not by any engine.

### 2.4 Completeness of the serialized module — three independent arguments

The charge is right that this matters: nonmembership in a *sampled*
sub-ideal would not imply nonmembership in `J_X`.  I did not rely on the
producer's generator count.

**(a) Independent recomputation on a different architecture.**  My own
Singular script on arm64-Darwin:

```text
SERIALIZED_SIZE=66   SERIALIZED_IS_SYZ=1
FRESH_dp_GENERATORS=66
T_IN_FRESH=1   FRESH_IN_T=1        (132 per-generator two-sided reductions)
```

and `write(...,syz(I))` produced a file whose SHA-256 is
`83832f380ce11a491c9799e50ff8b36b5fbc3a6b0d5b5dc52d90b6239c129a7a` —
identical to `input/syz6.txt`, to the AWS R1 output, and to the AWS R0
output.  Cost: 5.67 s, 38 MB, i.e. fully consistent with R1's 10.40 s /
59.5 MB total.

**(b) A `mres` cross-check that I must report as ill-posed, not as a
discrepancy.**  `mres(I,2)` returns a second module with 20 generators that
reduces neither way against `std(T)`.  This is **not** a defect: diagnostics
show `nrows(rs[1]) = 1` and
`mres_generators_identical_and_ordered = 0` — Singular's `mres` re-minimises
and reorders the generating tuple of `I`, so `rs[2]` is the syzygy module of a
*different* tuple and componentwise comparison is meaningless.  Recorded here
so that a later reviewer does not mistake it for a contradiction.

**(c) A Gröbner-free argument that makes completeness irrelevant.**  This is
the strongest thing in this review and it is new, so I state it in full.

> Let `s ∈ Syz(r1..r6)` be arbitrary and let `μ` be a monomial of degree `e`.
> Since `ord(a^X_i) ≥ 1`, the value `λ(μ·Σ_i s_i a^X_i)` depends only on the
> terms of `s_i` of degree `≤ D − e − 1 =: L`.  Split `s = s̄ + s'` with
> `s' ∈ m^(Lc+1)` for any `Lc ≥ L`.  Because `ord(r_i) ≥ 2`,
> `Σ_i s̄_i r_i = −Σ_i s'_i r_i ∈ m^(Lc+3)`.  Hence the truncation of **every**
> true syzygy lies in the finite-dimensional `Q`-space
> `A(Lc) = { s̄ ∈ (R/m^(Lc+1))^6 : Σ_i s̄_i r_i ≡ 0 mod m^(Lc+3) } = ker M_Lc`,
> computable by pure linear algebra with no Gröbner basis.
> If the functional `φ_μ(s̄) = λ(μ·Σ_i s̄_i a^X_i)` lies in `rowspace(M_Lc)`,
> it annihilates `ker M_Lc ⊇ {truncated true syzygies}`, so
> `λ(μ·Σ_i s_i a^X_i) = 0` for *all* `s ∈ Syz`, whatever `Syz` is.
> (`e = D` is automatic: `ord(Σ s_i a_i) ≥ 1`, so `μ·Σ s_i a_i ∈ m^(D+1)`.)
> `A(Lc)` shrinks as `Lc` grows, so this is a terminating escalation ladder.

Result of running that ladder exactly over `Q`:

```text
K2   D=2  e=0 (Lc=2, 168 unk / 210 eq / rank 106)   PASS      [c = 1]
          e=1 (Lc=1,  42 unk /  84 eq / rank  28)   PASS      [c = 1]
K6   D=3  e=0 (Lc=2, 168 unk / 210 eq / rank 106)   PASS      [c = 0]
          e=1 (Lc=1)  PASS      e=2 (Lc=0)  PASS
K10  D=4  e=0 (Lc=3, 504 unk / 462 eq / rank 294)   PASS      [c = 0]
          e=1 (Lc=2)  PASS      e=2 (Lc=1)  PASS      e=3 (Lc=0)  PASS
```

K6 and K10 close at `c = 0`; K2 needs one escalation step, `c = 1` (at `c = 0`
the over-approximation is genuinely too coarse — that is expected behaviour
of a relaxation, not evidence against the claim).

**Therefore the three nonmembership conclusions do not depend on
`Syz(r1..r6)` being generated by the 66 serialized vectors at all.**  Even
if the module had been sampled, the certificates would still prove
`D_X ∉ (J_X)_m` for the true `J_X`.  Attack 2's completeness worry is
answered twice over.

### 2.5 The 66 syzygy images and the three targets

For each direction, `load_X.txt` equals `a{X}1 … a{X}7` from `v17_Q.sing`
(7/7), and independently over `Q`:

```text
E_X[j] = Σ_{i=1..6} T[j][i]·a^X_i   equals image_X.txt   66/66     all three X
D_X    = h·a^X_7 − Σ_{i=1..6} u_i·a^X_i  equals target_X.txt        all three X
sign-mutation control  (h·a7 + Σ u_i a_i) ≠ D_X                     all three X
```

Target sizes: `D_K10` 79 terms ord 3, `D_K6` 41 terms ord 2, `D_K2` 16 terms
ord 2.  All nonzero, so V17's `zero_X = 0` precondition holds.

I additionally verified, outside the charge, the frozen 87-generator
seven-row module `S87` in `v17_Q.sing`: 87 vectors, and
`Σ_{i=1..7} S87[j][i]·r_i = 0` for all 87.  That closes another V17
precondition by hand.

**Conclusion for attack 2: confirmed.**

---

## 3. Attack 3 — complete monomial and multiplier census, byte comparison

For each cutoff I enumerated all monomials of degree `≤ D` in six variables
myself, enumerated every generator multiplier through `D − ord(g)`, and
rebuilt the augmented matrix and both maps from the parsed polynomials.

```text
K10 D=4   rows 210 = C(10,6)   columns 603   nonzero entries 18 788
K6  D=3   rows  84 = C(9,6)    columns 492   nonzero entries  7 025
K2  D=2   rows  28 = C(8,6)    columns  70   nonzero entries    734
```

Generator order histogram (72 generators = `r1..r6` then the 66 images):

```text
rows      ord 2,2,2,2,2,3
E_K10     ord 3 ×65,  ord 4 ×1
E_K6      ord 2 ×65,  ord 3 ×1
E_K2      ord 2 ×65,  ord 3 ×1
```

**Omission audit.**  At `D = 4` and `D = 3` no generator is omitted.  At
`D = 2` exactly two are omitted — generator 6 (`r6`, ord 3) and generator 9
(`E_K2[3]`, ord 3).  Both lie in `m^3 = m^(D+1)`, so they and all their
multiples are zero in `R/m^3`; omitting them is forced, not optional.  I
also checked directly that the dual annihilates every **non-census**
monomial multiple of every generator (vacuously, but checked, not assumed):
`y also kills every NON-census monomial multiple : True` for all three
directions.  The predicted column counts `Σ_{ord(g)≤D} C(D−ord(g)+6,6)`
equal the observed 603 / 492 / 70 exactly.

**Byte comparison.**  My re-emitted artifacts:

```text
51b248fe8de573aa4c13071a59f4f710bfc93a99bf5d86b77be3bb6c27b1d365  matrix_K10_D4.tsv
9a8d078ef21f525693df4a10f47db3b7c64149cd9c6589321a9a98fadb6618b9  rows_K10_D4.json
d4d93f369f4b6ecd95c23bfe4320b53ebe7a7146913c43cd40962bfadaf7f631  columns_K10_D4.json
8dfd56a545c3861d82a5203aa74b6df61c122e233d0f2a3f7c4f8b2ff761a776  matrix_K6_D3.tsv
d2b606cc6d41b2c5ee82ef846d5fe1d28b726997f64c1adefbe2f33b879fc5b7  rows_K6_D3.json
e8e1a9941ea5b6950ab3705ace048b3dd4b4fb2381be864c57e28d6c8625988f  columns_K6_D3.json
423bd1dfc2f9d94f86afd98a9245b9bed12d98587edc27b7bc50300a762e9fee  matrix_K2_D2.tsv
6411c8497397ac76eefaecea6e17f714f52eddf1f88cd697884d18dd0af1f1ff  rows_K2_D2.json
a58a08f140404c1f93e2df90ed7b0af82b1611917744edfd7d5715e9248cac52  columns_K2_D2.json
```

All nine are **byte-identical** to the frozen inputs, and the three
`matrix_*.replayed.tsv` files in the R1 output are byte-identical to the
frozen inputs as well.  The three matrices are also byte-identical to
V18R2's own `output/emitted/matrix_{K10_D4,K6_D3,K2_D2}.tsv`, so V21 really
did consume V18R2's artifacts rather than re-derive convenient ones.

**Conclusion for attack 3: confirmed.**

---

## 4. Attack 4 — dual parse, annihilation, exact pairings, mutation

Each dual was parsed with my own reader and checked in two ways: against my
rebuilt sparse matrix, and — independently of that matrix — by recomputing
`λ(μ·g)` directly from the parsed polynomials for every one of the 603 / 492
/ 70 census columns.

```text
direction  cutoff  rows  ideal cols  dual support  Σ y·col   pairing ⟨y,D_X⟩
K10          4      210      603          37        all 0     25/45056
K6           3       84      492          11        all 0     45/11264
K2           2       28       70           4        all 0    -25/352
```

All three pairings equal the charged values exactly, and each equals the
`certificate_dot` metadata field.  Metadata `field Q`, `cutoff`, and
`consistent 0` were gated; every dual index lies in `[0, rows)`; no `x` lift
row is present in any of the three files.

**Mutation controls** (all required to break the replay, all did):

* target `+1·μ` at a supported row: `25/45056 → −720871/45056`,
  `45/11264 → 22573/11264`, `−25/352 → 2791/352`.
* one live matrix entry `+1`: that column's pairing becomes `−24`, `3`, `8`.
* **exhaustive dual perturbation**: `+1` at *each* supported row in turn —
  4 + 11 + 37 = 52 perturbed duals — **0** still certify.
* 5 random duals per direction — **0** certify.

So the certificate is not vacuous and is not robust to any single-entry
change.

**Independent second proof of truncated nonmembership, without the dual.**
I computed the exact rational ranks of the frozen matrices:

```text
K2   rank(M) = 6    rank([M | t]) = 7
K6   rank(M) = 30   rank([M | t]) = 31
K10  rank(M) = 108  rank([M | t]) = 109
```

Rouché–Capelli then gives `D_X ∉ J_X + m^(D+1)` directly.  These also
confirm the `rank` / `augmented_rank` / `inconsistent_row` metadata fields,
which V21 itself never checks.

**Conclusion for attack 4: confirmed.**

---

## 5. Attack 5 — audit of the local-unit lemma

Both implications are correct, and no colon computation is needed.

**(i) `D ∈ J·R_m ⟹ ∃ s, s(0) ≠ 0, sD ∈ J`.**  Write `D/1 = Σ (p_i/t_i) g_i`
in `R_m` with `t_i ∉ m`.  Put `t = Π t_i ∉ m`.  Then `u·(tD − Σ q_i g_i) = 0`
in `R` for some `u ∉ m`.  `R = Q[d0..d5]` is an **integral domain** and
`u ≠ 0`, so `tD = Σ q_i g_i ∈ J` with `t(0) ≠ 0`.  The domain hypothesis is
essential and holds.  The converse is immediate.

**(ii) `s(0) ≠ 0 ⟹ s̄` is a unit in `R/m^(D+1)`.**  Write `s = s(0) + n`,
`n ∈ m`, `n^(D+1) = 0` in the quotient.  Then `s̄` is invertible with
`s̄^{-1} = s(0)^{-1} Σ_{j=0}^{D} (−n/s(0))^j`.  Since the image of `J` is an
**ideal** of `R/m^(D+1)`, `sD ∈ J` gives `D̄ = s̄^{-1}·(sD)‾ ∈ J̄`, i.e.
`D ∈ J + m^(D+1)`.

Contrapositive: an exact functional on `R/m^(D+1)` that kills the complete
truncated image of `J` and is nonzero on `D` refutes `D ∈ J·R_m`.  **Yes —
the exact finite dual really does imply local nonmembership with no colon
standard basis.**  The two hypotheses the lemma silently uses are that `R` is
a domain and that the truncated image is the image of an ideal (so closed
under multiplication by the unit `s̄^{-1}`); both hold.

One completeness obligation is genuine and is where a bad packet would hide:
the functional must kill the *complete* truncated image, i.e. every monomial
multiple of every generator of the *true* `J_X`.  §2.4(c) and §3 discharge
exactly that, the former without any syzygy computation.

Finally, this is precisely V17's own branch predicate.  V17 sets
`local_X = (reduce(1, std(C_X + maximal)) == 0)` with `C_X = quotient(J_X, D_X)`;
`local_X = 1` iff `C_X + m = R` iff `C_X ⊄ m` iff some `s` with `s(0) ≠ 0`
has `sD_X ∈ J_X` iff `D_X ∈ (J_X)_m`.  So `LOCAL_NONZERO ⟺ D_X ∉ (J_X)_m`,
the statement proved.  (V17's `allzero_X` side-condition is *implied* by
`local_X = 0`, since then `C_X ⊆ m`.)

**Conclusion for attack 5: the lemma is sound as used.**

---

## 6. Attack 6 — dependency-order repair and circularity

### 6.1 What V18R2 actually gated on

`PREREGISTRATION_Q_PROVISIONAL.md` makes V18R2 nonpromotable until
**(a)** the live V17-Q producer independently returns the same three
`LOCAL_NONZERO` branches, **and (b)** the exact input artifacts agree
byte-for-byte.  Its navigation dependency was the *modular* V17 `p = 65521`
endpoint.

### 6.2 State of monolithic V17-Q

`TIMEOUT_Q_BOX01_30M.md` records that the exact-Q primary lane hit its
1800-second cap with exit 124 while still in `K10_START`, produced **no**
direction branch, and licenses no conclusion; it was relaunched under a
two-hour continuation tag.  **There is therefore no V17-Q exact endpoint in
existence for V21 to be circular with.**

### 6.3 What V21 consumes

Only: the frozen V17 **source text** (`9e22780c…`, the same hash V18R2
pinned), and V18R2's artifacts — all of which V21 re-derives.  Nothing
consumed is an output of the exact V17-Q colon computation.  I confirmed the
independent cross-links by hash: `row_prelude_sha256 = 5b0a77e6…`,
`h_sha256 = 87ced4af…`, and all six `u_sha256` in the V17 `p = 65521` result
JSON match V21's frozen inputs exactly.  **No hidden circular dependence on
the unknown exact endpoint.**

### 6.4 Ruling

V21R1 **does** discharge conjunct (a) — and more strongly than V17-Q would,
since it is a proof rather than a concurring run.  Conjunct (b) is
discharged at the semantic level (images and targets are shown equal to what
the V17 source constructs, and `syz6.txt` is shown byte-identical to a fresh
`write(...,syz(I))` from that source on two architectures); byte-equality of
`IMAGE_X`/`TARGET_X` against a *future* V17-Q serialization is not
established, but is immaterial, because the matrices are rebuilt from parsed
semantics and I reproduced those bytes from V17's declarations.

**V18R2's exact filtered results may now be consumed without waiting for
monolithic V17-Q — restricted to the three first-incompatible cutoffs.**
Specifically, licensed for consumption:

```text
dual_K10_D4  (== V18R2 solution_K10_D4.tsv, f316823a…)
dual_K6_D3   (== V18R2 solution_K6_D3.tsv,  773fea5f…)
dual_K2_D2   (== V18R2 solution_K2_D2.tsv,  53abc5f8…)
and the three conclusions  D_X ∉ (J_X)_m,  i.e. V17 branch = LOCAL_NONZERO.
```

**Not** licensed by this PASS: V18R2's *compatible*-cutoff lift claims
(K10 `D2`,`D3`; K6 `D2`), which V21 never replays; and everything the
monolithic V17-Q colon lane would additionally produce — the colon ideals
and their generator counts, `local_quotient_proper`, `global_class_zero`,
and the 87-generator representation-invariance gate `rep_X`.  V21 proves the
branch *predicate value*; it does not certify that V17-Q would reach and
print that branch, because `rep_X` is not replayed by V21 (nor by me: it
needs `std(E_X)`, which is plausibly the very step where V17-Q is stalling).

Cross-check status: the V17 `p = 65521` lane independently reports all three
`LOCAL_NONZERO`.  That is **agreement**, not a dependence, and the mandatory
disagreement-audit is not triggered.  The monolithic exact lane should still
be allowed to finish as the preregistered independent cross-check.

**Conclusion for attack 6: the repair is legitimate and correctly bounded.**

---

## 7. Attack 7 — scope firewall

Enforced, and I found no overreach in `RESULT.md`, `RESULT.json`, or the
preregistrations.  Even at PASS this proves only:

* three **separate** normalized first-order load classes in the K00
  coefficient-local ring `R_m`, `R = Q[d0..d5]`;
* it does **not** couple the three loads;
* it does **not** restore the honest `Lambda` weights (V17 records these as
  deferred: `k10 = 2`, `k6 = 6`, `k2 = 10`);
* it does **not** include `mu`/`Jdet` targets through grade 19;
* it does **not** establish honest-source reachability;
* it does **not** exclude an arc;
* it does **not** decide K00 closure incidence;
* it does **not** imply order two, maximum twelve, or JC2.

`RESULT.json`'s `scope` and `firewall` strings state exactly this.

---

## 8. Defects and additive corrections

None of the following changes the verdict.

1. **R1 delta is 2 + 1, not 2.**  Beyond the charged two changes, R1
   additively adds the `PREREGISTRATION_R1.md` hash gate and the
   `r1_preregistration_sha256` result field.  Administrative; verified by
   full diff.
2. **`quit` destroys the exit-code channel.**  Singular returns 0 after
   `quit`, so all fail-closed behaviour now rests on the 15 positive
   sentinels in `run_singular`'s `required` list.  I verified the list is
   complete: every guarded `=0` sentinel has a matching required `=1`, and
   `quit` fires before the terminal `SOURCE_REPLAY=PASS`.  Note nothing was
   actually lost — the R0 transcript shows Singular already returned 0 after
   `? exit(82) is undefined`, so the returncode channel was never load-bearing.
3. **Producer-authored JSON literals.**  `serialized_syzygies: 66`,
   `fresh_module_equal: true`, `source_images_targets_replayed: true`,
   `truncated_nonmembership: true`, `local_nonmembership_by_unit_lemma: true`
   and `v17_branch: "LOCAL_NONZERO"` are string/int literals in the Python
   source, not measurements read back from the run.  They are sound only
   because the preceding `fail()` guards would have aborted.  Downstream
   readers must not treat them as observed quantities.
4. **`K00_V21_FRESH_SYZ_GENERATORS` is printed but not gated.**  Harmless:
   the substantive gate is the two-sided `SYZ_MODULE_EQUAL=1`, and
   `size(T)!=66` is gated separately.
5. **`replayed_matrix_sha256` is tautological.**  The emitted file is written
   from the same bytes that were just compared to the frozen input, so its
   equality with `matrix_sha256` carries no independent information.
6. **The verifier never compares `input_dir/INPUT.sha256` with its own frozen
   `INPUT_FLAT.sha256`.**  It records the digest but does not gate on it, so
   custody closure requires the external comparison.  I performed it: both are
   `38c6dd45…` and byte-identical.
7. **Dual metadata is only partly gated.**  `rows`, `columns`, `rank`,
   `augmented_rank`, `inconsistent_row` are unchecked by V21.  Harmless (the
   certificate is self-contained), and I verified all of them exactly anyway
   (§4): 6/7, 30/31, 108/109.
8. **`RESULT.md` table wording.**  The column headed "matrix rank witness"
   holds column counts (603 / 492 / 70), not ranks.  The exact ranks are
   108 / 30 / 6.  Wording only; the numbers under it are correct as column
   counts and my §4 ranks confirm the inconsistency independently.
9. **Row provenance is asserted, not gated.**  The Python matrix rebuild takes
   `r1..r6` from `prelude_Q.sing` and never checks them against
   `v17_Q.sing`.  Not a live defect: the two files are byte-identical on
   lines 1–8, both are under the frozen 31-input manifest, and I verified
   `rr_i == r_i` independently.  A future revision should gate it.
10. **`mres` is not a valid cross-check here** (§2.4(b)); recorded so the
    20-generator second module is not later mistaken for a contradiction.

**Additive strengthenings contributed by this review** (not required by the
charge): the Gröbner-free `A(Lc)` completeness argument of §2.4(c), which
removes any reliance on `syz`; and the exact Rouché–Capelli rank proof of
§4, which re-derives truncated nonmembership without the duals.

---

## 9. Smallest proved statement

Let `R = Q[d0,d1,d2,d3,d4,d5]`, `m = (d0,…,d5)`, and let
`r1,…,r7`, `h`, `u1,…,u6`, and the three load septuples
`a^X_1,…,a^X_7` for `X ∈ {K10,K6,K2}` be **the polynomials literally declared
in the frozen V17 exact source `v17_Q.sing`,
SHA-256 `9e22780c0f9b38f2e502b08ac51c1b9d8fee21e7b40e9569d08d77a3683d8b5c`**.
Put

```text
Syz = Syz(r1,…,r6) ⊆ R^6
E_X = ideal generated by { Σ_{i=1}^{6} s_i · a^X_i  :  s ∈ Syz }
J_X = (r1,…,r6) + E_X
D_X = h·a^X_7 − Σ_{i=1}^{6} u_i · a^X_i
```

Then, for each of `X = K10, K6, K2` **separately**:

> **`D_X ∉ J_X · R_m`.**  Equivalently, there is no `s ∈ R` with `s(0) ≠ 0`
> and `s·D_X ∈ J_X`; equivalently `(J_X : D_X) ⊆ m`; equivalently the V17
> direction-`X` branch predicate evaluates to `LOCAL_NONZERO`.

Established en route, exactly over `Q`:
`rr_i = r_i` (i = 1..7); `h·r7 = Σ_{i=1}^{6} u_i·r_i` with `h(0) = 20 ≠ 0`;
the 66 serialized vectors are syzygies of `(r1,…,r6)` and generate the whole
of `Syz`; the 87 frozen seven-row vectors are syzygies of `(r1,…,r7)`;
`E_X` and `D_X` are as serialized; and for each `X` the frozen rational dual
annihilates the complete truncated image of `J_X` in `R/m^(D+1)` while
pairing with `D_X` to `25/45056`, `45/11264`, `−25/352` respectively.

Nothing about coupling of the three loads, `Lambda` weights, grade-19
targets or `Jdet`, honest-source reachability, arc exclusion, K00 closure
incidence, order two, maximum twelve, or JC2 follows.

---

## 10. Replay hashes independently obtained

Recomputed on this host from the frozen bytes; each equals the frozen value.

```text
--- charged freeze/evidence ---
27fb885a1602257c2885e89c194c2d5f5bb2e7a3709f88f366e0c2807a5ad5dc  PREREGISTRATION.md
137fdc18c349a549949e90c3d515b5e08e01d9f69a6be5f8efbbf97b78175d7d  PREREGISTRATION_R1.md
06544be839c794e452de101a75a0926d1a99acc4ba86b27470eaa9d2de15fd20  FAILURE_R0.md
fd97d0b80b48bd46afd45a21a29a50f18592a68aac9047ad94d9abfb438ad875  verify_filtered_dual_corollary_v21.py
4c35362b7223566317ca346bd261fb13023fbb3d8a48aef2908dd00d1a168026  SOURCE_FREEZE_R1.sha256
97e5721a21a169a3123bd843c59ea1241126a4b0a221e2f28a89a313481069ae  SOURCE_FREEZE.sha256  (R0)
c96a647a89f3730e7000a170c35cee88cee960eb99fa531b7c56b1cc796f3ee3  R0 verifier (harvested)
38c6dd45b888ec04a5c0b9bdd4b93625a1df491b4e4f63851f5546cb1d7d465f  INPUT_FLAT.sha256 == input/INPUT.sha256
2217222bbf07baf423dbc6c973cf1fc8931c2240466b085860f103ee89a2700c  AWS_REGISTRATION.md
b514ef728afd47518246727efc5a7b41efb768707c4fe08f5625a96a8d32efb9  RESULT.md
7341d67bb6abfba9ce1b99d6670360721214aaf6bbb51165dbf84964c65e7ad3  RESULT.json
00159ec022932932373fc294980541ca791a173e5bbdbe58072d84d6b3b74b49  EVIDENCE.sha256   (49/49 verified)
                                                                  INPUT.sha256      (31/31 verified)

--- source provenance ---
5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a  prelude_Q.sing == v17_Q.sing lines 1-8
9e22780c0f9b38f2e502b08ac51c1b9d8fee21e7b40e9569d08d77a3683d8b5c  v17_Q.sing (== V17 frozen compiled source)

--- artifacts I rebuilt from scratch and that came out byte-identical ---
51b248fe8de573aa4c13071a59f4f710bfc93a99bf5d86b77be3bb6c27b1d365  matrix_K10_D4.tsv
9a8d078ef21f525693df4a10f47db3b7c64149cd9c6589321a9a98fadb6618b9  rows_K10_D4.json
d4d93f369f4b6ecd95c23bfe4320b53ebe7a7146913c43cd40962bfadaf7f631  columns_K10_D4.json
8dfd56a545c3861d82a5203aa74b6df61c122e233d0f2a3f7c4f8b2ff761a776  matrix_K6_D3.tsv
d2b606cc6d41b2c5ee82ef846d5fe1d28b726997f64c1adefbe2f33b879fc5b7  rows_K6_D3.json
e8e1a9941ea5b6950ab3705ace048b3dd4b4fb2381be864c57e28d6c8625988f  columns_K6_D3.json
423bd1dfc2f9d94f86afd98a9245b9bed12d98587edc27b7bc50300a762e9fee  matrix_K2_D2.tsv
6411c8497397ac76eefaecea6e17f714f52eddf1f88cd697884d18dd0af1f1ff  rows_K2_D2.json
a58a08f140404c1f93e2df90ed7b0af82b1611917744edfd7d5715e9248cac52  columns_K2_D2.json
5020bea7f32775aee77f63a4d477fcfa33064055f8a0cf9884f3dde25bc11065  source_replay_v21.sing  (regenerated from the frozen verifier)
83832f380ce11a491c9799e50ff8b36b5fbc3a6b0d5b5dc52d90b6239c129a7a  FRESH_SYZ6_MODULE.txt   (local Singular 4.4.1, arm64-Darwin)
c47a0d8517383aa944c2a788fe2bb85151367b266ba881f44a79f486ed6d41f9  source_replay.stdout    (local run, byte-identical to AWS R1)
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  source_replay.stderr    (empty)

--- cross-links confirmed by hash ---
f316823aec28e2318e9df2c91f9d05d3980a17a01637acf8abc861e3e0d82b5e  dual_K10_D4.tsv == V18R2 solution_K10_D4.tsv
773fea5fc70fdcd5c05263c99c7486ccfee8646665a5a7d4bd4e310e9ec4e219  dual_K6_D3.tsv  == V18R2 solution_K6_D3.tsv
53abc5f8e1838cdab2b1c8b914895456faeb33cbb1f1ea1b841bbe269f9d2ffe  dual_K2_D2.tsv  == V18R2 solution_K2_D2.tsv
                                        matrix_{K10_D4,K6_D3,K2_D2}.tsv == V18R2 output/emitted/*
87ced4afe1680f11073eb62bda7c7894f297925283557b2ccf0e951daba09e04  h.txt (== V17 p=65521 result h_sha256)
```

---

## 11. Answer to the required question

**May V18R2's exact filtered results now be consumed without waiting for
monolithic V17-Q?**

**Yes**, for the three first-incompatible-cutoff certificates and the three
`LOCAL_NONZERO` conclusions they support, and only for those.  V21R1 replaces
V18R2's administrative `no-promotion-before-V17-Q` order with an exact proof
of the same three statements from the frozen V17 source; there is no exact
V17-Q endpoint in existence, hence no circularity; and the V17 `p = 65521`
lane independently agrees.  V18R2's compatible-cutoff lift claims, and every
other V17-Q colon output (`rep_X`, colon generators, `local_quotient_proper`,
`global_class_zero`), remain outside this PASS and still require their own
evidence.  The monolithic exact lane should keep running as the preregistered
independent cross-check; disagreement would remain a mandatory stop.

---

*Review produced by Claude Opus 5 (`claude-opus-5`) on 2026-08-27.  Replay
scaffolding lived under `/tmp/jc2rev/`; no producer file, canonical ledger,
or `jc2-lean` content was modified.*
