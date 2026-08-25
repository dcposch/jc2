# Self-contained count erratum for the selected-Q8 component theorem

Date: 2026-08-25  
Status: **PRODUCER-EXACT MOD-127 COMPONENT THEOREM; hostile review required**

The immutable earlier breadth report used the count

```text
123 + (64-1) + 68*(8-1) = 662>658,
```

which assigns order one to 42 fixed fibres without a stored positive-order
moving lift.  Their exact lex-shape/source/Jacobian custody is available, so
the count is defensible, but it is unnecessary and creates a review surface.
The old report and case remain byte-immutable.

The replacement proof uses **only explicitly lifted fibres**:

```text
80 distinct order-8 fibres:  contact 80*8 = 640,
w=25 order-64 fibre:         contact       64,
total normalized contact:                  704 > 658.
```

The breadth set excludes `w=25`, so all 81 fibres are distinct.  Each breadth
lane certifies squarefree degree-190 `H`, unit `H_v`, unit full six-by-six
source Jacobian, moving length `190*8`, and exact vanishing of all six rows,
the ratio, and localizer through order eight.  The frozen `w=25` lane certifies
the same through order 64.  Hence the local intersection contribution is at
least

```text
190*704 > 190*658.
```

The frozen sparse contact-to-component lemma therefore forces an irreducible
mod-127 source component whose projected image is `H`.  The strict margin is
46 normalized orders.

This successor supersedes only the numerical contact-count paragraph of

```text
xmodel/max12-912-order3-nu-q8-p127-breadth-component-20260825.md
```

and not its scope firewall.  The exact conclusion remains mod-127 projected-
component existence only.  Degree one, all-contact grouping, characteristic-
zero no-merger, Taylor realization, and trajectory consequences remain open.

Portable replay:

```text
cases/max12_912_order3_nu_q8_p127_component_self_contained_count_20260825/replay.py
```
