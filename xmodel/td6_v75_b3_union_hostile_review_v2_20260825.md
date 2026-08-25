# Hostile review V2: repaired TD6 V74/V75 `B3=0` atlas plus custody overlay

Inspection only of the charged surfaces.  No producer, no `verify.py`
execution, and no `replay_v74.py` / `replay_v75.py` execution.  Stored
`PASS` / `CONFIRMED` strings were ignored as proof.  Frozen file bytes
were hashed with Python `hashlib` and compared by exact equality.
Polynomial identities were expanded independently in `Q[C,V,U]`,
`Q[x,y]`, and `Q[x,t]`; named omission witnesses were evaluated in `Q`
and, for the quadratic factor, in `Q(√2)`.

Charged surfaces:

- `cases/td6_c1_c2_c3_q2_b3_atlas_union_repaired_v75_aws_20260825/`
- `xmodel/td6-c1-c2-c3-q2-b3-atlas-union-repaired-v75-aws-20260825.md`
- `cases/td6_c1_c2_c3_q2_cminus5_v73_review_repair_20260825/`
- `xmodel/td6-c1-c2-c3-q2-cminus5-v73-review-repair-20260825.md`
- `cases/td6_c1_c2_c3_q2_b3_atlas_union_v75_review_repair_20260825/`
- `xmodel/td6-c1-c2-c3-q2-b3-atlas-union-v75-review-repair-20260825.md`
- load-bearing V73K:
  `cases/td6_c1_c2_c3_q2_cminus5_previous_x11_v73_aws_20260825/`
  and filed review `xmodel/td6_v73k_hostile_review_v2_20260825.md`

The eight load-bearing charges are re-audited from source, evidence,
and the consumed leaf reviews.  The V1 required custody findings are
then checked against the nonmutating V75 supplement.

---

## Findings

**1. [Confirmed] V74's constructible cover of the raw line
`V=0,C=-5U^2` is exact.**

On that line, `Q[C,V,U]/(V, C+5U^2) ≅ Q[U]`.  The standard affine
cover is `Spec Q[U] = D(U) ∪ V(U)`, and the two pieces are disjoint.
Substituting `U=0` into `(C,V,U)=(-5U^2, 0, U)` yields the origin
`(0,0,0)`; equivalently `(V, C+5U^2, U)=(C,V,U)`.

The `D(U)` leaf is the V73K original-row unit on
`V=0,C=-5U^2,D(U)`:

- residual digest `3884ec0c…`, normalized target `-1`, only `U`
  localized;
- identity `be5b6bc8…`, DAG `27a26a20…`, leaf ledger `112776f2…`,
  residual-factor ledger `8763f53f…`;
- theorem stdout `d4bb078c…` / `35b88e5a…` (Box02 / Box03), matching
  the standalone V73K theorem streams, not the predecessor q-prime
  control `c698dca9…`;
- filed V73 V2 review ends with a standalone `CONFIRMED`.  The V73
  custody overlay pins predecessor stdout/stderr `c698dca9…` /
  `12994f40…` as six-odd-row/per-edge support, not a V73K pass gate.

The `V(U)` leaf is reviewed V70 origin only.  That is the right
special case for this line: the unique closed point is `C=V=U=0`.
V74 pins origin stdout `90df496c…` (`source_center=C=V=U=0`, complete
denominator `(1)`) and the V70 review `2a352086…`.  V33 and V70
`u-h-zero` are not required for this one line.

**2. [Low] V74 is a marker-composed union, not a source replay.**

`replay_v74.py` hashes `fe25b93a…` on both hosts and finishes in
0.04 s.  The substitution is Python `{"C": -5*0**2, "V": 0, "U": 0}`.
The cover check is a two-element set identity.  Frozen omission
controls delete dictionary keys `generic_U_nonzero` / `origin_U_zero`.
`replay_v73.py` (`dcaa920a…`) is not in the V74 tree.  A residual
OR-gate still accepts either V73K aggregate lift markers or a
predecessor per-edge banner; on this freeze the pinned stdout is the
aggregate (`Xminus1_11_dependency_aggregate_reduction_exact=true` and
`Xminus1_11_aggregate_lift_to_original_first_rows=true`), and the
predecessor identity `c7b45865…` would fail the pinned identity hash
`be5b6bc8…`.  The overlay states that the per-edge OR is not
authority.  The scheme cover in Finding 1 does not depend on those
Python tautologies.

**3. [Confirmed] Coefficient-wise raw `B3`, weighted lift, and
line-pencil factorization.**

Independent expansion:

```text
B3 = 4C²U² - 4C V²U + 24C U⁴ + V⁴ - 20 V²U³ + 20 U⁶
B3|_{V=0} = 4U²(C+U²)(C+5U²)
b(x,y) = 4x² - 4xy + 24x + y² - 20y + 20
B3(C,V,U) = U⁶ b(C/U², V²/U³)
y = t(x+5)  ⇒  b = (x+5)·((t-2)² x + 5t² - 20t + 4)
b(-5,y) = y²
t=0  ⇒  b = 4x²+24x+20 = 4(x+1)(x+5)
t=2  ⇒  b = -16(x+5)
```

V75's lift loop sends `(xdeg, ydeg)` to
`(xdeg, 2 ydeg, 6-2 xdeg-3 ydeg)` and asserts equality with `B3`.
The `t=0` / `t=2` specializations match the displayed coefficient
dicts.  Wrong-coefficient, missing-line, and wrong-`t=2` controls
are genuine polynomial inequalities.  The overlay does not change
this algebra.

**4. [Confirmed] The six constructible emptiness leaves cover affine
`B3=0` overlap-safely.  V68 is a route lemma, not an emptiness leaf.**

`B3|_{U=0}=V⁴`, so `B3=0 ∩ {U=0}` is the C-axis `{U=V=0}`.  On
`D(U)∩{V=0}` the two lines are V46 and V74.  On `D(UV)`:

- `x=-5` forces `b=y²=0`, hence `y=0`, hence `V=0`, contradiction;
- `t=0` forces `y=0`, hence `V=0`, contradiction;
- `t=2` forces `b=-16(x+5)≠0` on `D(x+5)`.

The remaining points lie in the V66 birational chart

```text
U0 = w²(t-2)²/(16t),  V0 = w U0,
C0 = w⁴(t-2)²(-5t²+20t-4)/(256 t²),
```

with inverse `w=V/U`, `t=y/(x+5)` on that open.  Finite factors
`2t-1` and `t²-4t+2` are V67 on `D(w)`.  They do not meet each other
(`t=1/2` gives `t²-4t+2=1/4≠0`).  Extra pencil points at those `t`
with `x=-5` are already on the V74 line.  Chart poles `t=0`, `w=0`,
`t=2` route to `U=0` and the two `V=0` lines.

V66 ring names `(C,V)` are chart parameters `(t,w)`, not raw
`(C0,V0)`.  Ledger primes `{2C-1, C, C-2, C²-4C+2, V}` are
`{2t-1, t, t-2, t²-4t+2, w}`.  There is no raw-`C=0` hole in V66.

Leaves as written are pairwise disjoint except at the origin, which
is in the `U=0` leaf and is also the `U=0` endpoint of V74; both
owners empty it.  V68 is the reviewed translation of `{t,w,t-2}`
into those raw strata.  V75 independently replays the same
identities, so omitting V68 uncovers no new `B3=0` point.

**5. [Confirmed] Consumed leaf scopes match the tree.  Stale V33
whole-`U=0` and V45 / staged-N13 are not emptiness authority.**

| Leaf | Review | Exact open used |
|---|---|---|
| V66 | grok `CONFIRMED`; stdout `c7c3342a…`; review `57d00b8c…` | `B3=0`, `D(t w (t-2)(2t-1)(t²-4t+2))` |
| V67 | grok `CONFIRMED`; half `148fd9ef…`, quad `46a1608b…`; review `a124abb2…` | `2t-1=0` and `t²-4t+2=0` on `D(w)`; `w=0` separate |
| V68 | grok `CONFIRMED` as a standalone line, appendix after the verdict; stdout `c84447f9…`; review `b9ac3c7c…` | route lemma only |
| V70 origin | grok `CONFIRMED`; stdout `90df496c…`; review `2a352086…` | `C=V=U=0` |
| V70 `u-h-zero` | same review; stdout `2431ed02…` | `C=U=0 ∩ D(V)`, off `B3=0` (`B3=V⁴`) |
| V33 | grok `CONFIRMED_WITH_REPAIRS`; stdout `94e2267d…`; review `706f6ad4…` | `U=0 ∩ D(C)` |
| V46 | grok `CONFIRMED_WITH_REPAIRS`; stdout `01fa0f2e…`; review `2e76f499…` | `V=0,C=-U²,D(U)`, first-J, independent of N13 |
| V73K | V2 `CONFIRMED`; identity `be5b6bc8…` | `V=0,C=-5U²,D(U)` |
| V74 | this union | whole raw `C=-5U²` line |

Bundled V66/V67/V68/V46/V70 review bytes are identical to the xmodel
reviews.  V73 copies in V74 match the standalone V73K theorem
artifacts, not the predecessor.  V45 stdout is not in the V75
closure.  V73 `return`s before the dead V72 current/N13 body.  V46
returns before copied P12/N13.  Frozen V68 stdout still prints
`U_zero_direct_source_dependency_verified=true` and
`Cplus5_direct_source_dependency_verified=true` (stale V33/V45
pins); the overlay disclaims those pins as V75 source-theorem
authority.

**6. [Confirmed] The V75 supplement discharges the V1 custody
repairs without changing the atlas algebra.**

V1 required: file V73 review or consume the V73 custody overlay; pin
all three pieces of the V33/V70 whole-`U=0` union; replace weak
verdict tokens by exact SHA plus a standalone verdict line; treat the
V46 unpaid-`C=-5` sentence as historical.  The overlay does this as
follows.

- V73 is consumed as the aggregate twelve-previous-row V73K identity
  already pinned by V74, plus the V73 review-repair freeze
  `372ac71e…`.  Predecessor q-prime bytes remain support-only.  The
  now-filed V73 V2 report is a standalone `CONFIRMED` of that same
  identity; no positive V73 byte changed.
- Whole `U=0` is the reviewed three-piece union
  `V(U)=[V(U)∩D(C)] ∪ [V(C,U)∩D(V)] ∪ V(C,V,U)`.  Overlay copies
  are byte-identical to the original producers:
  V33 `94e2267d…` (`cases/td6_c1_c2_c3_q2_beta_u_zero_aws_20260825/evidence/n13-u-zero.stdout`),
  V70 `u-h-zero` `2431ed02…`, V70 origin `90df496c…`, and both
  reviews `706f6ad4…` / `2a352086…`.  On `B3=0` only the C-axis and
  origin remain; `u-h-zero` is retained as the middle piece of the
  cover and is empty on `B3=0`.
- Overlay review gates for those newly pinned files are SHA identity
  plus a standalone verdict token.  V33 ends `CONFIRMED_WITH_REPAIRS`;
  V70 ends `CONFIRMED`.  Frozen original `endswith` / substring tests
  are producer sentinels and are not overlay proof.  V66, V67, V46
  reviews already end with the intended token and are SHA-pinned by
  original V75 `SOURCE.sha256`.  V68's `CONFIRMED` is a standalone
  line with a residual-obligations appendix; original V75 already
  cannot use last-byte `endswith` on that file.
- The V46 erratum sentence that `C=-5U²,D(U)` is “the precise
  remaining staged-N13 source-DAG debt” remains in the frozen
  erratum (`9cdcba8c…`) and is still a frozen V75 producer marker.
  The overlay classifies it as historical pre-V73 state, superseded
  by V73/V74.  It is not a live atlas premise.
- Named constructible omission witnesses, independently checked:

  | Owner | Witness | `B3` | Unique leaf |
  |---|---|---|---|
  | V33 C-axis | `(C,V,U)=(1,0,0)` | 0 | `U=0 ∩ D(C)` |
  | V46 | `(-1,0,1)` | 0 | `V=0,C=-U²,D(U)` |
  | V74 / V73 | `(-5,0,1)` | 0 | `V=0,C=-5U²,D(U)` |
  | V67-half | chart `(t,w)=(1/2,1)` → `(171/1024, 9/32, 9/32)` | 0 | `2t-1=0`, `w=1≠0` |
  | V67-quad | chart `(t,w)=(2+√2, 1)` | 0 in `Q(√2)` | `t²-4t+2=0`, `w≠0` |
  | V66 | chart `(t,w)=(1,1)` → `(11/256, 1/16, 1/16)` | 0 | generic open |

  Each point lies in its named leaf and outside the other five leaf
  conditions.  Deleting that owner leaves that point uncovered.  The
  quadratic has no `Q`-rational `t` (discriminant 8); the named
  witness is constructible over `Q(τ)`, `τ²-4τ+2=0`.  Overlay
  `verify.py` evaluates `B3=0` at the five `Q`-points and checks that
  `t=1` is generic; it does not instantiate the quadratic point or
  encode leaf-exclusion in code.  The named points themselves are
  the theorem-level witnesses.

The overlay contains none of the V74/V75 identity or replay bytes
and does not alter `B3`, the pencil, or the six-leaf split.

**7. [Confirmed] Dual-host source closure and output agreement.
The deployment/provenance-failure firewall is README-asserted.**

Walking original V75 `MANIFEST.sha256` (`9e0dcee2…`) gives zero
mismatches.  `FREEZE.sha256` hashes to `0baf6347…` and pins that
manifest plus producer-report `1a385e44…`.  V73 original
`MANIFEST` / `FREEZE` / producer report are `1282f908…` /
`d50d8844…` / `716717ab…`.  Both review-repair manifests and
freezes likewise walk with zero mismatches; V73-repair freeze is
`372ac71e…`, V75-repair freeze self-hash `4327e42f…`.

`replay_v74.py` = `fe25b93a…` and `replay_v75.py` = `0c9cb1fe…` on
both hosts.  All four `rc` files are the single byte `0\n`
(`9a271f2a…`).  Canonical stdout (drop `aws_run_tag=` /
`aws_hostname=`) agrees for both stages.  V74 SOURCE lists differ
only in per-host V73 theorem stdout (`d4bb078c…` vs `35b88e5a…`);
V75 SOURCE lists differ only in per-host V74 stdout (`69b06c29…`
vs `df2810f7…`).  Every other evidence file is byte-identical
across hosts.  Hostnames `ip-172-30-0-186` / `ip-172-30-0-249` and
distinct tags are registered dual-host provenance, not a copy.

Tags `td6_v74_retry_bash_…T2139Z` and
`td6_v75_repaired_atlas_d_…T2146Z` match the “later clean run”
story.  Frozen `source_path` still names autochain `T2110Z` / `v75c`
`T2144Z` trees.  Failed invocations are not in this freeze; the
claim that they died on provenance markers rather than algebra is
README-asserted, not freeze-witnessed.  `verify.py` is
marker/custody only.

**8. [Confirmed] Scope firewall holds.**

V74 prints `whole_B3_killed=false` and sibling A3/TD6/SP-2/JC2
denials.  V75 prints
`scope=fixed_source_typed_A3_q2_beta_section_only` and
`whole_A3_killed=false`, `whole_TD6_killed=false`,
`SP2_killed=false`, `landing_proved=false`, `JC2_resolved=false`.
README, preregistration, producer report, and overlay xmodel all
deny whole A3, another TD6 modulus, TD6, SP-2, landing, and JC2.
Nothing here licenses a transverse-center, boundary, dead-stretch,
F1-orbit, or pole-modulus statement.

---

## Strongest exact claim that survives

In the already fixed, source-typed A3 section with
`q_β=t+β t²+t²⁵` and direct `q_β'=1+2β t+25 t²⁴`, the raw affine
divisor `B3=0` is empty for every β, as the constructible union of:

- the reviewed three-piece cover of raw `U=0` (needed because
  `B3|_{U=0}=V⁴`): erratum-corrected V33 on `U=0 ∩ D(C)`, V70
  `u-h-zero` on `C=U=0 ∩ D(V)` (off `B3=0`), and V70 origin;
- reviewed V46 on `V=0`, `C=-U²`, `D(U)`;
- V73K’s original-row unit on `V=0`, `C=-5U²`, `D(U)` (residual
  `3884ec0c…`, normalized `-1`, only `U` localized), with reviewed
  V70 origin at the closed point (V74);
- reviewed V67 on `2t-1=0` and `t²-4t+2=0` over `Q(w)`;
- reviewed V66 on `B3=0` in `D(t w (t-2)(2t-1)(t²-4t+2))`;

together with the polynomial identities `b(-5,y)=y²`, `t=0 ⇒ y=0`,
and `t=2 ⇒ b=-16(x+5)` on `D(UV)`.

V68 is a reviewed route lemma whose stale V33/V45 source pins are
not V75 emptiness authority.  The predecessor six-odd-row q-prime
control is not a V73K or V74/V75 theorem gate.  This is a
dependency union in that one section.  It is not whole A3, another
TD6 modulus, TD6, SP-2, a landing theorem, or JC2.

---

## Remaining required repairs

None.

The V1 required custody findings are discharged by the nonmutating
V75 supplement together with the filed V73 V2 `CONFIRMED` review.
No algebraic change to `B3`, the pencil, or the six-leaf case split
is required.  No positive V74/V75 identity byte changed.

Recommended, not required:

1. Overlay `verify.py` instantiates five `Q`-rational witnesses and
   the generic `t=1` factor test; instantiate the quadratic witness
   in `Q(τ)` and encode leaf-exclusion in the checker, matching the
   README claim already verified by inspection.
2. Apply the overlay standalone-verdict helper to the SHA-pinned
   V66/V67/V68/V46 reviews as well as V33/V70.  The frozen files
   already carry the intended tokens; V68’s appendix is why last-byte
   `endswith` is the wrong test.
3. Pin the filed V73 V2 report
   `xmodel/td6_v73k_hostile_review_v2_20260825.md`
   (`6cd2ebd85df69d3e88a1fe4fb962f6721075f98140e2ae6e7ba1fd9ad121dad6`)
   next to the V73-repair freeze.  The overlay currently pins the
   V1 custody overlay, which is sufficient because V2 confirmed that
   overlay without algebraic change.
4. Overlay-assert that V74’s unused per-edge OR is not taken, and
   that V68’s `U_zero` / `Cplus5` pins are not V75 authority.  Both
   are already stated in prose.
5. The frozen original `replay_v75.py` still `require()`s the V46
   unpaid-`C=-5` sentence and still uses `endswith` sentinels.
   Mutating it would break the original freeze; the overlay is the
   theorem-level gate.
6. Freeze-witness the failed autochain / `v75c` jobs if the
   deployment firewall needs more than README assertion.
   `source_path` still names those trees.

---

CONFIRMED
