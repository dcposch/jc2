# Additive review repair V2: uniform contact-shift naturality interface

Date: 2026-08-27

Status: **FORMULA THEOREM CONFIRMED AFTER DIFFERENT-MODEL REVIEW; NORMATIVE V46
SCHEMA/VERIFIER PRODUCER PASS, STILL PROVISIONAL PENDING ITS OWN DIFFERENT-MODEL
REVIEW.**  This is additive to, and does not rewrite, either artifact below.

```text
1cfa10b45d83ba4ecd98861c1f82e9bd41056d1cef7eaa43ad2802aa73aada5d
  xmodel/max12-812-order2-gate-t-uniform-contact-shift-naturality-interface-sol-20260827.md
b66f8c0cf342e497e9117306de3d4aaa5d8b537c5929f99d2b32765ed855f164
  xmodel/max12-812-order2-gate-t-uniform-contact-shift-naturality-interface-hostile-review-fable5-20260827.md
```

## R1: coefficient extraction

Replace the original proof phrase “coefficient extraction commutes with a continuous
sigma-adic homomorphism” by the following precise statement.

Let `R_tot` be the polynomial ring over `Z[1/2]` in the total jets and let `R_D1` be
the polynomial ring in the relative D1 jets.  For nonnegative `(a,c,r)`, define the
coefficient-ring map

```text
az_i,ac_i -> 0                                      (i<a)
az_(a+n),ac_(a+n) -> AzD1_n,AcD1_n                 (n>=0)
ez_i,ec_i -> 0                                      (i<c)
ez_(c+n),ec_(c+n) -> 2*CzD1_n,2*CcD1_n             (n>=0)
cs_i,rs_i -> 0                                      (i<r)
cs_(r+n),rs_(r+n) -> BzD1_n,4*BcD1_n               (n>=0),
```

fixing `p0`, every `ell_i`, all three load jets, every target, and `sigma`.  Extend it
coefficientwise to `R_tot[[sigma]] -> R_D1[[sigma]]`.  This extension sends the seven
actual-total primitives to the seven D1 primitives by direct substitution.  Because
the map fixes `sigma` and acts coefficientwise,

```text
delta([sigma^g] Phi_j^total) = [sigma^g] Phi_j^D1
```

for every row `j=1,...,7` and every `g>=0`.  No assertion about an arbitrary
continuous substitution is used.  This identity is over any `Z[1/2]`-algebra; neither
unique-`AC` inequalities nor `rho` localization is needed for it.

The later Kummer substitution `p0=-2*rho^2` and the shifted moving-root maps on
`D(rho)` remain separate operations.

## R2: valuation language

Cancellation in the frozen row polynomial can only raise sigma-adic valuation.
Therefore a raw primitive census cannot omit a jet that really occurs through `T`; it
can only over-retain jets and falsely predict an earlier row obstruction.  For the
moving `P` series, the raw bound from `F6=2P` is vacuous.  A useful `P`-jet maximum
must consume the complete reviewed polar inventory and its first surviving row grade.
This is why the finite bound is computed from the ten reviewed polar families, not
from unreduced `F_i` valuations.

## Frozen normative implementation

```text
796eb0847e7b0bb7972c2fd7b3db10bd2dcfd2fd85c5bbaa47e3a239f8b02673
  cases/max12_812_order2_gate_t_uniform_contact_naturality_v46_20260827/SCHEMA.json
8e49fc87ebeffb74e4c33f79ae248846c7de3ce4f4fb2ad07ac85751d8841ec7
  cases/max12_812_order2_gate_t_uniform_contact_naturality_v46_20260827/verify_uniform_naturality.py
25a5fb3e0a8dff1a0d841823dfe44265775e793431445878ab49193c846d67ce
  cases/max12_812_order2_gate_t_uniform_contact_naturality_v46_20260827/run_v0_v4/result.json
b39f66e2cb7cac16dd1c940814b44e8aff3cd7c7df1ad9347beb5f558187ae22
  cases/max12_812_order2_gate_t_uniform_contact_naturality_v46_20260827/FREEZE.sha256
```

V46 returned `PASS-UNIFORM-CONTACT-NATURALITY-V46-V0-V4`.  Its V0--V4 checks pin the
normative formulas and aliases, independently evaluate every one of the 569 frozen
tails in all seven rows at one representative of each of the eleven endpoint
families, exercise the mandatory mutations, verify the shifted Hensel/root maps on
both decks, recompute the polar support maxima, and bind endpoint lifecycle to exact
artifact hashes.

The current grade-20 representative `(a,c,r;T)=(2,5,3;20)` gives exactly
`p/A/C=3,R=1,k10=2,k6=k2=0`, with the last two marked inactive.  At the opposite
ceiling sentinel `(20,21,20;38)`, only `p,C,k6` are active at relative depth zero,
which mechanically rejects the false universal `T=10+2c` rule.

## Lifecycle and exact consequence

The repaired formula theorem removes serial `ACT-TOT-G22`, `ACT-TOT-G24`, and later
per-grade exporters as mathematical obligations: one coefficientwise identity
supplies every truncation.  The exporters may be retired from the campaign critical
path only after the V46 schema/verifier survives its own independent hostile review
and a concrete endpoint linker has discharged that endpoint compiler's semantic and
provenance checks.

Ten endpoint families in the frozen schema are promoted.  The exact
`(a,d,r)=(8,3,8)` family is separately pinned as
`confirmed_but_unpromoted`; its literal odd-row review is valid, but its union-level
use remains conditional until a narrow promotion exists.  The nearby artifact named
“promotion” has status only `PROMOTED ROUTE FALSIFICATION ONLY` and cannot be imported
as an emptiness theorem.

Nothing here promotes an endpoint, reconciles mixed theorem types/localizations,
handles `rho=0`, equality faces, positive-order leading loads, `k=0`, unlisted
contacts, the staged Rees/terminal receivers, either global `G2` obligation, Gate T,
order two, maximum twelve, JC2, or a counterexample.
