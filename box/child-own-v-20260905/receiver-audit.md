# Receiver consumer audit for the own-child-V repair

This note audits code and saved receiver artifacts. It does not calculate the
child's own V or promote any source row to a polynomial pair. The root lane
verified the frozen charged inputs mechanically before delegation. Reads of
the closeout and child-data reports used `/tmp/jc2-lane.wwyG4k/inputs/`. No
ledger, Lean, ideation, existing receiver, or frozen input was edited.

## 1. Concrete finding

The copy error changes purported child data, child radii below the terminal
radius, `B_safe`, raw `D_i` inventories, V-labelled fibre grouping, U-NEGATIVE
and C-TOP filters, and several job-routing decisions. It does **not**, by
itself, invalidate a verified free-leading receiver containing the proved
`G_i` in every block at the correct `(n',m',M_last',ell)`.

The distinction is a direct code fact. In the corrected s'=3/4 compiler,
`coeff_inventory_source_complete` returns the set union `D_i | G_i`
(`box/moh14-charts-20260905/sprime3_compiler.py:255`). Its `G_i` comes from
`d=-delta_s` and K (`:239`), and the terminal expression
`delta_s=-(ell+1)/(n'-M_last'-1)` is independent of V. `build_spec` uses
`h=y^K+sum(free parameters*monomials)` (`:305`), free alpha/beta coefficients,
and saturation **c alone** (`:335`). It fixes no V-dependent leading face,
root multiplicity, partition, or nonzero slope. Thus the V-dependent part
adds independent coordinates; wrong labels cannot remove the `G_i` subset.

For clarity, `|G_i|` also uses `K=gcd(n',m')`, already fixed by the receiver
degree pair. The statement that G depends only on `(n',M_last',ell)` refers
to variation among V-labelled fibres inside a fixed degree class; m' and K
are held fixed there.

This survival statement retains the source-support theorem's explicit
hypotheses, including that `M_last'` is the child's **actual effective
terminal** characteristic index. The old code's use of `s'=s-1` is not a
proof that this index is terminal for `u_s>1`. A saved `G_i` built from a
mere prefix does not acquire coverage just because its formula is
V-independent. The six historical s'=3/4 classes audited here came from
the compiler's `u_s=1` descent (`:116`), so that separate open-chain problem
does not arise in this particular group.

## 2. Mechanical verification of saved receiver charts

Run:

```text
python3 box/child-own-v-20260905/audit_receiver_support.py
```

Result: **DETERMINED — 6 degree/characteristic classes, 18 saved charts,
108 coefficient blocks PASS**. This consists of 12 labelled fibre charts
and 6 union charts. The driver reads
`box/moh14-charts-20260905/hsupport-gate-20260905/source-complete/classes_manifest.json`
and each saved metadata/builder pair. It computes G from n,m,M_last,ell,
without reading any child V value. After the terminal constant-translation
gauges it checks:

* G is contained in the actual h, alpha_i, and beta_i inventories.
* The builder's polynomial setup is exactly the saved inventory with one
  independent coefficient per listed monomial.
* h has free leading form with its sole fixed term y^K; partition is empty,
  omega=1, and saturation is c.
* Only terminal constant translations are used in these saved charts; no
  V-sensitive scalar shear removes another block.

The detailed per-block output, including the current metadata and builder
SHA-256 digests, is `receiver-support-audit.json`. These are counts of saved
artifacts and inventory containments, not counts of realizable pairs.

| Fixed class (n',m'; middle labels; ell) | d | G_h size | Saved union h size |
|---|---:|---:|---:|
| (16,12; 6,13; 3) | 2 | 24 | 36 |
| (18,12; 2,9; 2) | 3/8 | 11 | 19 |
| (24,16; -12,-2,5; 1) | 1/9 | 8 | 11 |
| (24,16; 12,17; 1) | 1/3 | 17 | 48 |
| (24,18; -15,14; 1) | 2/9 | 8 | 8 |
| (24,18; 9,20; 1) | 2/3 | 18 | 27 |

Every number in this table is **DETERMINED** arithmetic on saved supports.
No solver was run and no UNIT result was promoted in this audit.

An exact UNIT certificate on any one of these G-containing saved charts
continues to rule out the G-supported receiver class. For an actual
source, specialize the independent chart coordinates to its normalized
G-supported coefficients and set all decorative coordinates outside G to
zero. This uses the receiver's real coefficient ring and c inversion,
not an identification of same-named root labels. An existing NONUNIT or
timeout still says nothing about realization of any own-V fibre. New
own-V values do not require covering new V labels with additional charts
when one already has a class-level G receiver.

## 3. Actual consumers, with entry points

### A. The copy-producing functions

* `box/lib/census_sweep.py:175`: `descend` scales M and d, then copies
  `V2={i:skel.V[i] ...}` at `:207`. It also installs terminal V=d at `:208`.
* `box/moh14-charts-20260905/sprime3_compiler.py:116`: `descend_once` has
  an independent copy at `:127`, followed by terminal V=d at `:128`.
* `box/moh14-20260905/descend14.py:30`: another copy at `:38`, consumed by
  `phi` at `:42` and serialized to `descend14.json` at `:94`.
* `box/scopeleaks-20260905/scope_enum.py:37`: its standalone `descend`
  copies `Vp`, `V2p`, and `up=K'-V2` at `:45`. Consequently its saved own-child
  fields are copy diagnostics, not independently established data.

An adapter added only to census_sweep does not automatically repair the
other independent entry points. Historical artifacts should keep their
provenance and be called copied-label artifacts rather than silently
relabelled as newly reconstructed characteristic data.

### B. Quantitative child-data consumers that must be retyped/recomputed

* `sprime3_compiler.py:149` computes every `delta_i'` by `phi_eff`; the
  product at `:100` uses all upper V values. `closed_form_sprime` at `:160`
  uses V2 for `u`, `B_safe`, `B_tight`, `lambda_P`, and `lambda_Q`.
  It serializes these purported child values at `:696`.
* Its `D_i` floor at `:222` uses `delta1` and B. Thus raw h/alpha/beta
  inventories, unknown counts, “zero delta1” statistics, and comparisons
  between D and G change when own V changes. Existing D_i metadata remains
  an exact description of the old polynomial system, but its interpretation
  as the child's own D1 valuation floor is not established by the copied row.
* `box/lib/census_sweep.py:284` calls these formulas through
  `child_closed_form`; `inventory_counts` at `:308` propagates them to
  raw and source-complete unknown counts. `k4ray_shape` at `:338` uses
  `u==1`, hence uses copied V2. `solvable_unknowns` at `:359` selects an
  engine and sorting size from those values.
* `census_sweep.py:382` includes the whole V tuple in `class_key`;
  `four_int_key` at `:400` includes V2. Thus V-labelled class IDs, equality
  groupings, fibre sizes, counts of these keys, and paths derived from
  them are labels for the old census grouping. The coarser key
  `(n',m',ell)` at `:408` does not use child V. The special s'=3 compiler's
  class key at `:565` already omits V, though its fibre stems at `:766`
  include it.

### C. Decision filters and accounting that actually consumed V as data

* `box/operative-sweep-20260905/run.py:66` computes C-TOP by comparing
  copied top V with d after `drop_p174`; `:90` computes U-NEGATIVE from
  copied V2. `build_inventory` at `:192` assigns the tiers
  `live_us1`, `us_ge2`, `ctop_killed` from those booleans (`:211`).
  The associated `inventory.json`, frozen tier partitions, and `ctop_*`
  fields require the root lane's corrected interpretation.
* `run.py:419` refuses to emit a class whenever `n_uneg` is nonzero,
  writing `U-NEGATIVE_no_honest_chart`. This is a substantive loss of
  work caused by copied child V, even though the output verdict is OPEN.
* `box/operative-sweep-20260905/pull_tally.py:79` consumes this field,
  places rows in the U-NEGATIVE bucket at `:84`, and writes
  `hard-rows.jsonl` at `:138`. The file contains class/job records with
  derived counts and labels; it is not itself an independent source
  enumeration or realization witness.
* `box/scopeleaks-20260905/ctop.py:36` directly tests the parent V at the
  would-be child top (`:45`); its `ctop.json` therefore measures that
  copied-label predicate. `box/child-data-20260905/test12_childdata.py`
  builds child root-count expressions from the same assumption. Agreement
  of their arithmetic is not a proof of the root-disc identification.

The printed universal inequalities for a child's **own** normalized root
counts remain valid. The invalid step is asserting that a copied V is
that normalized count and counting the resulting failures as source kills.

### D. Emission gates remain V-sensitive even for G-completed charts

`census_sweep.py:589` computes the copied-data closed form and skips
emission when B>=0 (`:590`). The `S3.build_spec` gate at `:307` also raises
when B>=0. Neither gate is needed to define the proved finite G inventory
once the actual terminal radius is known and negative. A fresh G-only
emitter should derive d from the confirmed effective terminal data and
avoid such D1-specific gates, copied-V-dependent sorting, and the U-NEG
short-circuit. Merely replacing names on the old job map is insufficient.

For a chart that **was** emitted with `support="source-complete"`, the
union is explicit in `census_sweep.py:596`; no later V equation is inserted.
The per-fibre and class unions at `:610` and `:626` carry all free
coordinates. The row's V2 in `OB.Row` is only metadata for S3.build_spec;
the generated Jacobian target uses ell and the block degrees e,q.

## 4. Receivers where V is not merely decorative

The older s'=2 order/shape path really restricts the polynomial family
using V. `box/appendix2-k16-20260903/shape.py:141` tests U-NEGATIVE; its
`shape_bundle` uses `u=K-V2` to cap x degree, and at `:161` fixes a
V-dependent two-point leading form when its radius test succeeds.
`box/orderbasis-20260903/order_basis_full.py:136` uses V2 in its radii
and B; `h_inventory` at `:190` imposes the x-width `u`; `allowed_partitions`
at `:174` partitions that u. Its `top_face` at `:232` explicitly inserts
V2 copies of y and a complementary partition of nonzero slope factors.
`build_full_spec` at `:435` puts this fixed face into h and saturates by
`c*omega` (`:481`). Thus replacing V may alter coefficients, strata,
saturation, the parameter ring, and the actual ideal. A UNIT result on
one such slice is not a kill for a different own-V datum without a proved
map or a separate G-containing enlargement. The old cap regressions in
the charged source-support closeout remain an independent problem;
correcting V does not restore those caps.

There is a further case-by-case distinction for later “source-complete”
s'=2 emitters retaining a partition face as an affine coordinate origin.
For example, `box/s56-recert-20260905/s56_emitter.py:291` takes D∪G but
at `:367` still builds the partition face. Whether that face is decorative
depends on its separate `affine_origin_map` and whether every face shift
is represented by a free support coordinate (`:423`); the label alone
does not decide coverage. The present audit establishes the 18 s'=3/4
free-leading charts above, and makes no blanket certification of all
partition-based historical charts.

## 5. What survives independently of copied child V

The source census `(1)-(13)`, source M,d,V, source top u_s/v_s, licensed
descent degrees n',m' and ell, and the source split-window arithmetic are
not changed by this repair. `box/lib/split_window.py` reads the **source**
skeleton; it never asks CS.descend for child V. Its necessary split
screens remain source-data statements with their original scope. They
do not manufacture a new U-NEG kill when the no-split branch has lost its
copied-count contradiction. Likewise, exact polynomial ideal arithmetic
on a saved chart remains arithmetic on that chart. What needs rebuilding
is the asserted source-to-receiver coverage whenever that assertion
actually relied on own V, and the tier/routing/accounting based on it.

No new exit-price assertion is made, so no charge_basis line is asserted.
