You are Opus 5 acting as an independent exact-algebra researcher for the JC2
campaign.

Goal: replace the long-running V18R1 `drop grade 14` standard-basis negative
control by an explicit exact-Q witness, if one exists.

Read completely:

- `cases/max12_812_order2_p0_total_rees_t_cs_rho_unit_v18_20260826/PREREGISTRATION_V18R1.md`;
- its V18/V18R1 compilers and validator;
- the exact-Q V9 grade-10--12 coefficient exports consumed by the compiler;
- the relevant frozen odd-sheet/special-fibre reports and case artifacts
  found by source search;
- `xmodel/ideation-20260826T2350Z-synthesis.md` for current scope only.

On the ordered `T-cs` special fibre (`qrs=0`, `rho=0`, `cs` and `k`
inverted), seek an explicit rational assignment to every remaining variable
that kills all 21 grade-10--12 charted rows but does not use `Tg14_5`.
It is enough to give a parametric specialization with one concrete rational
point.  Verify every row by direct sparse substitution or exact hand algebra;
do not run a Groebner basis or any heavy local computation.  The equations
`1-u*cs=0` and `1-v*k=0` must also hold, so `cs,k` must be nonzero.

If no witness is found, identify the smallest exact obstruction and whether
the negative-control computation remains necessary.  Do not infer anything
from the main positive or from a specialized normalized analogy without a
literal substitution map.

Return `EXACT_WITNESS`, `NO_WITNESS`, or `INCONCLUSIVE`, with the full
assignment, all 21 exact residuals, source hashes, and scope firewall.  Write
only
`xmodel/max12-812-order2-p0-total-rees-t-cs-drop-g14-witness-opus5-20260827.md`.
No web, AWS mutation, heavy local computation, or `jc2-lean` access.
