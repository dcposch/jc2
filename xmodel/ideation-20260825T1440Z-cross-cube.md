# Adversarial cross-pollination — cube/max-12 owner — `20260825T1440Z`

Date: 2026-08-25  
Inputs read after collection:

- Sol `86187db5ea142e783beb442a0536d162cc59734d14e8a9ef2271eb6807df5d7f`;
- AS `59ea8144a9aa65e690a0f5217a9e5201155fa7f1c1196e42ee08a2261bebffd2`;
- TD6 `0d7b454cf90f421b516894cfa781562fd283ba9265eceb3f785d9fbe8a7e9348`;
- cube `15a057a76a9776f6b05f58286ecb1f58d2bb47c0fc842018602aa48a06788959`,
  corrected nonmutatingly by the companion zero-partial erratum.

This is comparison and attack, not independent evidence or promotion.

## 1. Deduplicated convergence

All four reports independently converge on one operational claim: the three
front lanes are no longer limited by generating more raw equations.  They are
limited by a source-honest passage through a localization/transition:

| client | generic/local fact | missing operation |
|---|---|---|
| Q8 | unit over a frozen `Q(c)` slice | exceptional `c`, moving `d4`, weighted closure, and `c=∞` |
| TD6 | V64 unit on `D(U*V*P3*QH)` | exact four-divisor constructible cover |
| AS | nonempty `omega=0` hyperplane on every projected Q9 fibre | intersect it with all downstream restoration/carry rows |

The common compiler idea—source cofactors, exceptional factors, Fitting
strata, and explicit cover/transition data—is genuine convergence.  The
interpretation of AS omega in my blind note and parts of the TD6 note was not:
`zero-partial` is surjective/nonzero, not source-zero.  The companion erratum
withdraws that claim.

## 2. Attack on the AS `Z/9` / Bockstein-module card

The AS card's attractive step is not yet licensed globally over a varying Q3
fibre.  It observes that fresh corrections `27U+81V` have
`(27U)^2=729U^2`, hence the fresh-fresh quadratic term vanishes modulo 243
and after division contributes zero modulo 3.  But a lower Q3-kernel
coordinate can occur at order 9.  Bilinearity of the determinant then permits

```text
(9K) * (27U) = 243 K U,
```

which vanishes before division modulo 243 but survives as `K U` in the next
divided carry modulo 3.  Thus the system is linear over `Z/9` after fixing
`K`, but need not be one global linear congruence module over the entire Q3
affine kernel.  Canonical representatives can hide exactly this mixed term.
Degree/support restrictions may make the mixed matrix zero, but that must be
proved from the full source compiler, not inferred from `27^2=729`.

**Cheapest separating test.**  Keep a symbolic general Q3-kernel vector `K`
and one full fresh output vector `U`; extract the coefficient of every
`K_i U_j` in the divided mod-3 rows.  One nonzero coefficient refutes the
global `Z/9`-linear-module claim and routes to a bilinear/Fitting atlas.
All-zero with exact source replay licenses the module compression.  This
small mixed-block audit should precede the proposed three-fibre Smith solve.

## 3. Attack on TD6 cover completeness

The proposed five locally closed pieces are set-theoretically plausible:
`U=0`, then on `D(U)` split `V=0`; on `D(UV)` split `P3=0`, then `QH=0`,
then the generic open.  The displayed normalized Bezout identity proves only
that `P3=QH=0` is empty on `D(U)`; it proves neither divisor empty and does
not supply any original-row identity there.

Three hidden assumptions remain:

1. `{U,V,P3,QH}` must be the full radical support of every denominator in
   the composed source DAG, not only the displayed coefficient-leaf ledger.
2. Saturation must precede specialization on each locally closed leaf;
   otherwise vertical/torsion components can be silently added or lost.
3. If the goal is only set-theoretic emptiness, a Čech gluing equality is
   unnecessary once all five leaves are exactly empty.  If the goal is a
   single global cofactor identity, then actual overlap syzygies and
   nilpotent multiplicities are required.  These are different theorems.

**Cheapest separating test.**  Emit one machine-readable denominator radical
from the fully composed original-row DAG, compare it exactly with
`rad(U*V*P3*QH)`, and run the four missing saturated leaf ideals with literal
source remainders.  A nonunit leaf becomes the only client.  If every leaf is
unit, the decision-tree cover proves set-theoretic emptiness without first
building a global Čech cofactor.

## 4. Attack on Sol's asymptotic-genus bridge

The proposed bridge needs more than honest landing.  Even if an auxiliary
Q8/coefficient component maps dominantly to a rational component of the
nonproperness set `A(F)`, its positive genus is not contradictory: a
positive-genus curve can map nontrivially and finitely to `P1`.  Rationality
of the target normalization constrains the source only if the induced
function-field map is degree one/birational, or if the actual trajectory
already supplies a dominant map `P1 -> C` (the mechanism used in the existing
Q8 positive-genus exclusion).

Specialization adds a second firewall: genus information must pass through a
proper integral model and the relevant horizontal component, not merely a
point incidence or a projected root.

**Cheapest separating test.**  For the first source-landed component, compute
the subfield generated by the two asymptotic-value coordinates inside its
normalization function field.  A primitive-element/minimal-polynomial degree
of one licenses the birational bridge; degree greater than one refutes the
claimed genus contradiction while preserving the map.  Until then this card
should remain a 5% global reserve, not receive Sol's proposed 10%.

## 5. Allocation change and ranked experiments

The AS module shortcut is the strongest potentially invalid implication, so
run its mixed `K*U` audit first and do not preallocate a large Smith campaign.
TD6 has a short exact four-leaf decision tree; Q8 remains closest to a
selected-leaf closure.

Recommended temporary allocation:

- `42%` Q8 exceptional-`c` / moving-`d4` / `c=∞` closure;
- `28%` TD6 denominator-radical and four leaf saturations;
- `25%` AS mixed-block audit, then full restoration over the omega-zero
  hyperplane if it passes;
- `5%` global landing/cofinality, including the degree-one asymptotic map
  test.

Stop rules are sharp: stop Q8 generic fraction-field variants after an exact
denominator cofactor; stop TD6 pivot variants after the denominator radical;
stop the AS `Z/9` module on the first nonzero mixed coefficient; stop the
asymptotic-genus bridge unless degree one is proved.  Consensus here is only
an allocation signal; none of these reports proves or disproves JC2.
