# V82P3 typed-composition erratum

All four immutable V82P runs and the completed V82P2 controls returned rc 1
before previous/pole parameterization.  At the first-to-previous composition
boundary, `allq.compose_forms` attempted to coerce a 33-axis `AxisJet` scale
through the q-only `EJet` constructor.  The eventual trivariate conversion
raised `TypeError`.  The failure is a software/source-typing defect, not a
compatibility result.  One still-running V82P2 lane was stopped with rc 143
after this identical defect was known; its state and logs are preserved.

V82P3 uses a dedicated `compose_axis_forms` whose constants, coefficients,
scales, parameterization forms, and results are asserted to be `AxisJet` and
not `EJet`.  Before transport it replays a nontrivial one-variable
square-zero composition against a directly formed expected answer.  Before
and after the actual first-to-previous/pole composition it audits every
affine form at the type boundary.  The V82S2 source is hash-pinned, and the
empty-table `ONE` positive control remains.  The full algebra is rerun on two
independent AWS hosts; no V82P/P2 mathematical output is consumed.
