# Hostile review V2: TD6 V76C fixed-A3 q2-beta complete union

Inspection only of the charged surfaces.  No producer execution, no
`verify.py` run, and no `replay_v76.py` / `replay_v75.py` / `replay_v57.py`
run.  Stored `PASS` / `CONFIRMED` strings were ignored as proof.  Frozen
file bytes were hashed with Python `hashlib` and compared by exact
equality.  The portable archive was listed and read, not unpacked into
the tree.  Ledger products were reconstructed by rational monomial
arithmetic in `Q[C,V,U]`; named cover witnesses and the raw/normalized
`B3` identities were evaluated in `Q`.  Flint was not re-invoked.

Charged surfaces:

- `cases/td6_c1_c2_c3_q2_fixed_a3_complete_union_v76_aws_20260825/`
- `xmodel/td6-c1-c2-c3-q2-fixed-a3-complete-union-v76-aws-20260825.md`
- `cases/td6_c1_c2_c3_q2_generic_source_dag_v57_review_repair_20260825/`
- `xmodel/td6-c1-c2-c3-q2-generic-source-dag-v57-review-repair-20260825.md`
- `cases/td6_c1_c2_c3_q2_cminus5_v73_review_repair_20260825/`
- `xmodel/td6-c1-c2-c3-q2-cminus5-v73-review-repair-20260825.md`
- `cases/td6_c1_c2_c3_q2_b3_atlas_union_v75_review_repair_20260825/`
- `xmodel/td6-c1-c2-c3-q2-b3-atlas-union-v75-review-repair-20260825.md`
- separately frozen V57, V70, V71, V75 packages and their reviews,
  including the filed V57 / V73K / V75 V2 reports and the V76
  review-surface overlay
  `cases/td6_c1_c2_c3_q2_fixed_a3_v76_review_surface_repair_20260825/`

V76 itself is a hash-closed Boolean composition, not a new elimination.
The six load-bearing charges are re-audited from source, evidence, and
the consumed leaf reviews.  Freeze-time `V57_hostile_review_pending` /
`V75_hostile_review_pending` banners are then checked against the
nonmutating overlay.

---

## Findings

**1. [Confirmed] Exact source, scope, and review status of the four
leaves.**

Write `H = C - 3U^2` and

```text
B3 = 4C^2U^2 - 4C V^2 U + 24 C U^4 + V^4 - 20 V^2 U^3 + 20 U^6
```

in the already fixed source-typed A3 section with center `(C,V,U)` and
`q_beta = t + beta t^2 + t^{25}`.  The four V76 leaves, as actually
consumed, are:

| Leaf | Exact open | Source theorem | Review status actually used |
|---|---|---|---|
| `D(U*H*B3)` | principal open of `U H B3` | V57 original-source N13/P12 DAG | V1 `CONFIRMED_WITH_REPAIRS`; overlay freeze `3d68c16d…`; V2 standalone `CONFIRMED` of that overlay |
| `V(U)` | whole raw plane `U=0` | reviewed V70 three-piece union (erratum-corrected V33 on `U=0 ∩ D(C)`, V70 `u-h-zero` on `C=U=0 ∩ D(V)`, V70 origin) | grok `CONFIRMED`, SHA `2a352086…`; V33 piece `CONFIRMED_WITH_REPAIRS`, SHA `706f6ad4…` |
| `V(H)` | whole raw divisor `H=0` | V71 five-piece Boolean cover (V64, V62D, V65 `P3`, V65 `QH`, V70) | grok `CONFIRMED`, SHA `4ec0f26f…` |
| `V(B3)` | whole raw divisor `B3=0` | repaired V75 six-leaf atlas | V1 `CONFIRMED_WITH_REPAIRS`; overlay freeze `4327e42f…`; V2 standalone `CONFIRMED` of that overlay |

V76 copies are byte-identical to the standalone frozen objects they
name:

- V57 DAG `a906b803…`, ledger `69c1086b…`, r6d stdout `2bb3374c…`,
  original FREEZE `c42633c4…`, producer report `b3d34387…`;
- V70 report `9013ec37…`, review `2a352086…`, FREEZE `3807f223…`;
- V71 report `7b51c5f0…`, review `4ec0f26f…`, FREEZE `41bb693a…`;
- V75 Box02 stdout `66b0d925…`, report `1a385e44…`, FREEZE `0baf6347…`.

Every leaf hostile review ends on a lone standalone verdict line with
exact SHA identity against the xmodel file.  V64 / V62D / V65 reviews
pinned by V71 `DEPENDENCIES.sha256` recompute (`e78af060…` /
`ec0ada3d…` / `e9f585da…`) and also end `CONFIRMED`.  No unreviewed
leaf sits in the union.  Freeze-time producer banners that V57 and V75
reviews were still missing are historically accurate at V76 freeze and
are not the present review surface (Finding 7).

V76 is a marker composition: `replay_v76.py` hashes `dd9bb146…` on both
hosts and finishes in 0.04 s.  It does not rerun V57/V70/V71/V75
algebra.  That is the licensed representation of a reviewed
constructible cover, the same design as V71, not a hidden new source
theorem.

**2. [Confirmed] V57's complete denominator support is exactly contained
in `{U,H,B3}`, with a genuine original-source N13/P12 identity on
`D(U*H*B3)`.**

Independent reconstruction of every claimed ledger product (eleven data
rows, rational monomial arithmetic, no Flint) recovers exactly:

| denominator | reconstructed factors |
|---|---|
| `1` | unit |
| `C-3U^2` | `H` |
| `CU-3U^3` | `U H` |
| `C^2-6CU^2+9U^4` | `H^2` |
| line 5 (9 terms) | `(1/4) H B3` |
| line 6 | `(1/4) U H B3` |
| line 7 | `(1/4) H B3 U^2` |
| line 8 (11 terms) | `(1/4) B3 H^2` |
| line 9 | `(1/4) U B3 H^2` |
| line 10 | `(1/4) U^2 B3 H^2` |
| `U` | `U` |

No extra prime appears.  Units `1/4` are in `Q`.  All three of `U`,
`H`, and printed `B3` occur, so the supported open is `D(U H B3)` and
not a strictly larger principal open.  V43's termwise clear
`(1/4) U B3 H^3` is a parent pin with the same radical; extra **powers**
of `H` can grow under products, extra **primes** cannot.  Flint's
treatment of `B3` as irreducible over `Q` is not a V57 theorem; the
claim is leaf-coefficient support inside `{U,H,B3}`.

The complementary identity is original-source, not quarantined staged
N13.  Frozen DAG `a906b803…`:

- unique current-row support `('X0', 13)`, `previous_nonzero_rows=1`,
  `composed_first_nonzero_rows=28`;
- staged left-null, remainder56, and target share digest `fd4415b2…`;
- `each_current_edge_original_row_replay=true`;
- raw P12 base digest `8d5c3550…` (the 2,893-term V43 polynomial);
- live glue named in the DAG as
  `P12_minus_multiplier_times_N13_equals_minus_k_over_50=true`.

The V57 overlay reads that last flag as the first-remainder identity
`R - M N13 = -k/50` with `k` a unit of `E` (`k * k^{-1} = 1`); the
fully expanded original-row identity remains the pinned V43
certificate `a53cc30d…`, parent SHA `3cc0fc3b…`.  The fourteen printed
previous keys are a P12/N13 lift cache, not N13 ancestry; N13 has one
unnamed original `X-1` previous summand and no original pole summand.
The singleton omission control drops current row 13, not a downstream
previous edge.  Dual-host DAG and ledger are byte-identical; r6d and
Box03 stdout agree on 94 mathematical lines after dropping the two
absolute artifact paths.  V76 copies the r6d stream `2bb3374c…` on both
composition hosts; that is a copy of one of two agreeing theorem
streams, not a second V57 run.

This is the repair the staged-N13 erratum demanded for `D(U*H*B3)`.
It does not kill `U=0`, `H=0`, or `B3=0`.

**3. [Confirmed] Reviewed V70 supplies all `U=0`, reviewed V71 all
`H=0`, and repaired V75 all `B3=0`, in this same fixed section, for
every beta.**

Whole `U=0`.  The scheme identity

```text
V(U) = [V(U) ∩ D(C)] ∪ [V(C,U) ∩ D(V)] ∪ V(C,V,U)
```

is exact and the three pieces are disjoint.  V33 in its repaired scope
is first-J emptiness on `U=0 ∩ D(C)` (complete chart `C^3`, review
`706f6ad4…`).  V70 rebuilds `C=U=0 ∩ D(V)` from original source (events
`-V,-V`, complete chart `V^3`, stdout `2431ed02…`) and the origin as a
transport incompatibility (row 6460, key `('g','X',-19,20)`, complete
chart `1`, stdout `90df496c…`).  Neither V70 leaf specializes the V33
echelon through `C=0`; event columns move `193/1289 → 194/1290` and the
numerator `C → V`.  Both V70 residuals are beta-degree 0 with monic
gcd 1.  V70's own two pieces do not cover `U=0 ∩ D(C)`; the reviewed
three-piece union does.  V76 pins that review in full, and V70 FREEZE
transitively pins the V33 review via `DEPENDENCIES.sha256`.  V75's
overlay additionally copies the three producer stdouts; V76 does not
need a second copy because V70 is consumed as the already-reviewed
union, the same consumption V71 was confirmed to make.

Whole `H=0`.  On `H=0`, either `U=0` or `U ≠ 0`.  If `U=0` then `H=C`,
so `V(H,U)=V(C,U)`, a subset of reviewed `V(U)`.  On `D(U)` the
standard principal-open split in `(V,P3,QH)` is

```text
V(H) ∩ D(U)
  = [V(H) ∩ D(U V P3 QH)]
    ∪ [V(H,V) ∩ D(U)]
    ∪ [V(H,P3) ∩ D(U)]
    ∪ [V(H,QH) ∩ D(U)],
```

with `P3 = V^4 - 32 V^2 U^3 + 128 U^6` and
`QH = V^4 + 8 V^2 U^3 - 64 U^6`.  Those four opens are exactly V64,
V62D, V65-P3, and V65-QH.  On `D(U)`, `V=0` forces `P3 = 128 U^6 ≠ 0`
and `QH = -64 U^6 ≠ 0`, so V62D does not meet either V65 curve; that
is consistency, not a cover step.  The P3/QH Bezout

```text
((5T-136)(T^2+8T-64) - (5T+64)(T^2-32T+128))/512 = 1
```

expands to difference `[512,0,0,0]` in `Q[T]` and is unused by
exhaustiveness.  Direct `q'` is retained on every leaf that reaches
`configure_qd`; V70 origin returns in transport, which is correct.
Each leaf is an original-row unit or beta-degree-0 gcd-1
incompatibility, so there is no beta-root leftover to carry across
the cover.

Whole `B3=0`.  Independent expansion recovers the V75 atlas algebra:

```text
B3|_{U=0} = V^4
B3|_{V=0} = 4U^2 (C+U^2)(C+5U^2)
B3(C,V,U) = U^6 b(C/U^2, V^2/U^3)
b(-5,y) = y^2
t=0 ⇒ b = 4(x+1)(x+5)
t=2 ⇒ b = -16(x+5)
```

so `B3=0 ∩ {U=0}` is the C-axis, the two `V=0` lines are V46 and
V74/V73K, and on `D(UV)` the remaining points lie in the V66 chart or
the V67 finite factors.  V68 is a route lemma, not an emptiness leaf.
V73K is the aggregate twelve-previous-row unit on
`V=0, C=-5U^2, D(U)` (residual `3884ec0c…`, normalized `-1`, only `U`
localized), with V70 origin at the closed point; the predecessor
six-odd-row q-prime control is not a V73K or V75 theorem gate.  Named
constructible witnesses, independently evaluated:

| Owner | Witness | `B3` | Off the other three V76 leaves? |
|---|---|---|---|
| V57 generic | `(0,1,1)` | `1` | yes: `U,H,B3` all nonzero |
| V33 C-axis | `(1,0,0)` | `0` | in `V(U)` (and `V(B3)`); not needed uniquely |
| V70 `u-h-zero` | `(0,1,0)` | `1` | in `V(U)` and `V(H)`, `B3 ≠ 0` |
| V46 | `(-1,0,1)` | `0` | `U=1`, `H=-4 ≠ 0` |
| V73/V74 | `(-5,0,1)` | `0` | `U=1`, `H=-8 ≠ 0` |
| V71 generic `H` | `(3,1,1)` | `97` | `U=1`, `H=0`, `B3 ≠ 0` |

V75's overlay copies V33/V70 producer bytes and pins V73 repair freeze
`372ac71e…`.  V76 consumes that repaired atlas, not a stale whole-`U`
or staged-N13 B3 sentence.

All four emptiness theorems are stated in the same normalized section
`(c1,c2,c3)=(C,V,U)` with polynomial `beta` and, where the stage is
reached, live `q_beta' = 1 + 2 beta t + 25 t^{24}`.  No leaf uses a
weighted `b3half` center as theorem typing.  No leaf leaves a beta-root
to be specialized later.

**4. [Confirmed] The set identity
`Spec Q[C,V,U] = D(U*H*B3) ∪ V(U) ∪ V(H) ∪ V(B3)` is exact, and each
deletion uncovers a genuine constructible point.**

In any ring, `Spec R = D(f) ∪ V(f)` and `V(fgh) = V(f) ∪ V(g) ∪ V(h)`.
Here `R = Q[C,V,U]` and `f = U H B3`, so the four-branch union is an
identity of schemes, not a sampled cover and not a Python tautology.
Overlaps are allowed (the origin lies on all three divisors; the C-axis
lies on `U=0` and `B3=0`; `C=U=0` lies on `U=0` and `H=0`).

V76's checker models a *partition* refinement

```text
{U=0} ⊔ {H=0, U≠0} ⊔ {B3=0, U≠0, H≠0} ⊔ D(U H B3)
```

by four disjoint string labels, then deletes one owner.  That is
stronger than needed for a union and does not instantiate a point.
The overlay reads the four controls constructibly: deleting the generic
leaf leaves a generic point of `D(U H B3)`; deleting a divisor leaf
leaves a generic point of that divisor outside the other two.  Named
witnesses, independently checked in `Q`:

| Deleted owner | Uncovered point | Why uncovered |
|---|---|---|
| V57 | `(0,1,1)` | `U=1`, `H=-3`, `B3=1` |
| V70 | `(1,1,0)` | `U=0`, `H=1`, `B3=1` |
| V71 | `(3,1,1)` | `H=0`, `U=1`, `B3=97` |
| V75 | `(-1,0,1)` | `B3=0`, `U=1`, `H=-4` |

Integer sampling over `C ∈ [-6,6]`, `V,U ∈ [-4,4]` produced 910 open
points, 117 on `U=0`, 27 on `H=0`, and 21 on `B3=0`, and every sample
satisfied `U H B3 = 0` if and only if it lay on one of the three
divisors.  That is a sanity check of the identity, not a substitute for
it.

The overlay is explicit that these controls assert the set cover, not
a second emptiness proof.  Emptiness of each summand is the leaf
theorem of Finding 3.

**5. [Confirmed] Dependency custody holds.  Stale whole-`U` V33, V45,
and quarantined staged-N13 are not authority.**

Independent SHA-256:

| object | SHA-256 |
|---|---|
| V76 `MANIFEST.sha256` | `e46ad84030c75342844f3fe50ec23cf475eb2afcf45faec12b9c298afcffc980` |
| V76 `FREEZE.sha256` | `41990e3d6cbdfe0deee6be1abb21d00721cbe29f2d618c3a54cfb4b2dce59c41` |
| V76 producer report | `0281a5fcac3d74fb050360f3095c87f08f3baaa4a54b7729418351a626a5d656` |
| V76 replay | `dd9bb146e43bf778d83e3b6420442bc4e4b42effd388be75cb3c3d00f609157a` |
| V76 tarball | `eb8858ccf5a21acdd7d413876ab44e2402faea7913a97d35b849acff61d22b8a` |
| V76 Box02 / Box03 stdout | `dd726a31…` / `8a7d9aa2…` |
| both `rc` | `9a271f2a…` (`0\n`) |
| V57 repair FREEZE | `3d68c16dc608cf3a89bc6211558e32988c31690c041cd53f3213c5a338493950` |
| V73K repair FREEZE | `372ac71e69e162b50ecc93d41fb5f0e3c343335a14e2ff515c9cd52602205c1f` |
| V75 repair FREEZE | `4327e42f77edef0f47b665d700c416c360bddfd3a5f2309ddd05197e2b673328` |
| V76 overlay MANIFEST / prompt | `b78be9ca…` / `53eb132d…` |

Walking original V76 `MANIFEST.sha256` (53 entries) gives zero
mismatches.  Both hosts' `SOURCE.sha256` walks give zero mismatches
and are complete against the source tree.  Walking V57 / V70 / V71 /
V75 original manifests and the three review-repair manifests likewise
gives zero mismatches.  Nested leaf `FREEZE.sha256` / `MANIFEST.sha256`
files are listed in `SOURCE.sha256` and not duplicated in the package
manifest; `verify.py` still walks `SOURCE.sha256`, so those sixteen
files are pinned.  Dual V76 runs are independent, not a copy: tags
`…_c_box02_…T2208Z` / `…_c_box03_…T2208Z`, hostnames
`ip-172-30-0-186` / `ip-172-30-0-249`, canonical stdout (drop
`aws_run_tag=` / `aws_hostname=`) identical, both `rc` the single byte
`0`.  Canonical V75 Box02/Box03 stdout likewise agrees; V76 copies the
Box02 stream.

Stale / quarantined authority, checked off:

- Withdrawn V33/V69 whole-`U=0` sentence.  Not consumed.  V70 review
  and the V33 scope erratum restrict V33 to `U=0 ∩ D(C)`.  V71
  Charge 5 already recorded this for the `H=0` leaf.  V75 overlay
  copies the three-piece union rather than the withdrawn sentence.
- V45 rational-line staged-N13 (`V=0, C=3U^2` and `V=0, C=-5U^2`).
  No V45 file is in the V76 tree.  V46 (first-J, N13-independent) is
  the `C=-U^2` owner; V73K is the `C=-5U^2` owner.  V68's frozen
  `U_zero` / `Cplus5` pins remain in original V75 and are disclaimed
  by the V75 overlay as V75 source-theorem authority.
- Quarantined generic-open / whole-H / whole-B3 staged-N13 packages
  named in
  `cases/td6_c1_c2_c3_q2_n13_localization_scope_erratum_20260825/`.
  V76 does not consume those producer reports.  `D(U*H*B3)` is V57's
  composed original-source DAG, not V43/V44's in-file P12 side.
  V43 is a parent pin of the full P12 original-row identity, which
  V57 V2 already classified as licensed rather than as a second
  staged-N13 shortcut.
- Predecessor V73 six-odd-row q-prime control.  V73 overlay and V75
  overlay exclude it from the theorem gate.  V76 does not pin those
  bytes.

V76 `require()` still tests producer `PASS` substrings.  Those strings
are non-authoritative under this charge; the leaf reviews and the
reconstructed cover/ledger identities are the theorem.

**6. [Confirmed] Scope firewall holds.  This is only the fixed
`(C,V,U,beta)` normalized family.**

V76 stdout, README, preregistration, producer report, overlay README,
and overlay xmodel all keep:

- `other_source_moduli_vary=false`
- `whole_TD6_killed=false`
- `SP2_killed=false`
- `landing_proved=false`
- `JC2_resolved=false`
- `promotion_licensed=false` at freeze time

No additional center, boundary, dead-stretch, F1-orbit, or pole
modulus varies.  No transverse neighborhood of this section is
claimed.  V57 still prints `raw_U_H_B3_strata_still_separate=true`
and `full_A3_beta_family_killed=false`; those divisor strata are
killed only by the other three leaves of *this* composition, still
inside the same section.  Nothing here licenses whole TD6, SP-2, a
landing theorem, a ceiling, a counterexample, or JC2.

The freeze-time line `promotion_licensed=false` was the correct
producer gate while V57 and V75 reviews were missing.  After those
reviews and this composition review, promotion of the *fixed-section*
emptiness statement is a documentation act, not a broadening of
scope.

**7. [Confirmed] The nonmutating V76 overlay discharges the freeze-time
pending-review and constructible-cover findings without changing any
positive identity byte.**

Original V76 producer bytes are unchanged: replay `dd9bb146…`, DAG /
ledger / leaf reviews as in Finding 1, dual stdout `dd726a31…` /
`8a7d9aa2…`.  The overlay directory contains none of those files.

What the overlay repairs, and only these:

- V57 is consumed as the repaired original-source identity on
  `D(U*H*B3)`, via V57 repair FREEZE `3d68c16d…`, not as an
  unreviewed producer `PASS`;
- V75 is consumed as the repaired six-leaf `B3=0` atlas, via V75
  repair FREEZE `4327e42f…`, which itself pins V73K custody repair
  `372ac71e…`;
- V70 / V71 remain the already-reviewed whole-`U=0` and whole-`H=0`
  unions, SHA-pinned inside original V76;
- the four deletion controls are read as constructible witnesses of
  the scheme cover, not as sampled-point algebra;
- promotion remains gated on this different-model review of the
  repaired dependency surface, still only for the fixed
  `(C,V,U,beta)` family.

The filed V57 / V73K / V75 V2 reports all end with a standalone
`CONFIRMED` of those same overlays.  This review independently
re-checked the load-bearing ledger, cover, B3, and hash claims rather
than treating those tails as proof.  Overlay `verify.py` pins the V76
MANIFEST/FREEZE, both leaf-repair FREEZEs, and the V2 prompt SHA
`53eb132d…`; those five hashes recompute.

Leftover producer banners (`V57_hostile_review_pending=true`,
`V75_hostile_review_pending=true`, `promotion_licensed=false`) are
immutable freeze-time text.  They are read through the overlay, the
same way leftover V57/V73/V75 producer banners were read through
theirs.  Because the original package is immutable, those banners are
not remaining required repairs.

Custody nits, not algebraic:

- portable archive member prefix
  `td6-v76-fixed-a3-union-20260825.5UzFu3/` versus the frozen filename
  `td6-v76-fixed-a3-union-20260825-v3.tar.gz`;
- run tags `T2208Z` versus evidence `end_utc=2026-08-25T21:59:36Z`;
- package MANIFEST omits the sixteen nested FREEZE/MANIFEST files that
  `SOURCE.sha256` already pins;
- V76 copies r6d V57 stdout and Box02 V75 stdout onto both composition
  hosts (mathematical streams already dual-agreed);
- overlay `verify.py` does not instantiate the four named witnesses or
  pin the filed V57/V73/V75 V2 reports (it pins the repair freezes
  those V2 reports confirmed).

---

## Strongest exact claim that survives

In the already fixed, source-typed normalized A3 section with center
`(C,V,U)`, `q_beta = t + beta t^2 + t^{25}`, and live compiler
derivative `q_beta' = 1 + 2 beta t + 25 t^{24}`, the normalized
compatibility system has no solution at any point of
`Spec Q[C,V,U]`, for every polynomial beta.

The argument is the exact scheme cover

```text
Spec Q[C,V,U] = D(U H B3) ∪ V(U) ∪ V(H) ∪ V(B3)
```

together with four reviewed emptiness theorems in that same section:

1. V57: original-source current-row N13 identity through first rows and
   one original previous `X-1` row, glued to the genuine 2,893-term P12
   by residual `-k/50` with `k` a unit of `E`, on the principal open
   whose leaf-coefficient denominator radical is exactly `{U, H, B3}`.
2. V70: the three-piece constructible cover of raw `U=0`, using
   erratum-corrected V33 only on `U=0 ∩ D(C)`, V70 `u-h-zero` on
   `C=U=0 ∩ D(V)`, and V70 origin; both V70 residuals beta-degree 0
   with monic gcd 1.
3. V71: the five-piece cover of raw `H=C-3U^2=0` by reviewed V64, V62D,
   V65-P3, V65-QH, and V70, each an original-row unit or gcd-1
   incompatibility on its stated open.
4. V75: the six-leaf atlas of raw `B3=0` (three-piece `U=0`, V46 on
   `C=-U^2, V=0, D(U)`, V73K/V74 on `C=-5U^2, V=0`, V67 on the two
   finite pencil factors, V66 on the complementary chart open), with
   V68 only as route algebra and with the predecessor q-prime control
   excluded.

This is emptiness of one normalized `(C,V,U,beta)` family.  It is not
a transverse neighborhood of that section, not whole TD6, not SP-2,
not a landing theorem, and not JC2.

---

## Remaining required repairs

None.

The freeze-time pending-review and constructible-cover findings are
discharged by the nonmutating V76 overlay together with the filed V57,
V73K, and V75 V2 `CONFIRMED` reviews of those leaf overlays.  No
algebraic change to `H`, `B3`, the four-branch scheme cover, or any
leaf identity is required.  No positive V76 identity byte changed.
The strict fixed-section `(C,V,U,beta)` scope is preserved.

Recommended, not required:

1. Overlay `verify.py` instantiates the four named witnesses of
   Finding 4 and pins the filed V57 / V73K / V75 V2 reports
   (`cf832722…` / `6cd2ebd8…` / `2460a03f…`) next to the repair
   freezes.  The freezes already suffice because those V2 reports
   confirmed the overlays without algebraic change.
2. List the sixteen nested FREEZE/MANIFEST files in the package
   MANIFEST, or record that `SOURCE.sha256` is the completeness
   manifest.  They are already hash-pinned.
3. Rename the portable archive member prefix away from the
   `.5UzFu3` staging suffix.  V57's analogous archive-name nit was
   treated as custody only.
4. The frozen original `replay_v76.py` still `require()`s producer
   `PASS` markers and still prints `V57_hostile_review_pending=true`.
   Mutating it would break the original freeze; the overlay is the
   theorem-level gate.
5. Freeze-witness PYTHONHASHSEED and the T2208Z / 21:59:36Z tag drift
   if deployment provenance needs more than dual-host identity.

---

CONFIRMED
