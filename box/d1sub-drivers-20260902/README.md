# d1sub-drivers-20260902

Lane D1-SUBTREE (Opus 5, 2026-09-02).  Unreviewed lane code.

  jacfibre.py   THEOREM JAC-FIBRE at the resultant level: exact Puiseux orders by
                Newton polygon of Res_y(g-c_2, z-h) w.r.t. ord_t.  101 checks.
  treecheck.py  the same claims at the TREE level (lambda_f, lambda_g reconstructed
                exactly from Res_y(g(x,y), g(x,y+z)) and Res_y(g(x,y), f(x,y+z))
                for automorphisms, whose g-roots are all conjugate).  151 checks.
  d1floor.py    the skeleton side: Moh Lemma 5.2 re-verified against an independent
                incremental lambda_g; floor(r) = ceiling(r) iff r = 1; q two ways;
                the window extremes; the two-sided and integrality filters.
                232 384 controls.
  runall.py     controls + the floor filter + the (UNI) integrality filter.
  general.py    the hypothesis-free knapsack (no (UNI)).
  runall.log, general.log   the measured runs quoted in the report.

Imports box/moh_skeleton_N.py (N-ON-THE-TREE's census, PROPOSAL) for the enumeration
only; every theorem it asserts is re-derived in d1floor.py's controls.  Calibration:
this census yields 3 975 groups at D <= 100, matching N-ON-THE-TREE to the unit.
