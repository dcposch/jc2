# V28 preregistration: prolong the ordered-a1 rho=0 boundary point to grade 16

Date: 2026-08-27

The exact V27 dual shows that `a1^3` is not in the degree-15 part of the
registered ordered-a1 ideal after `rho=0`.  Direct restricted-AST evaluation
then found the rational grade-15 point

`a1=1, aa0=1, cs1=1/6, ec3=1/6, rs2=-2/3`,

with `rho=0` and every other registered coordinate zero.  All 42 V23R1 rows
of grades 10--15 vanish there.

V28 will reconstruct the seven actual-total source rows one order farther,
to grade 16.  It must bridge all 42 old ordered-a1/rho-zero rows exactly to
the hash-pinned V23R1 exports before using the new coefficients.  After
substituting the point above and setting every old unlisted coordinate to
zero, it will verify that the grade-16 equations are affine-linear in the
new weight-16 coordinates and solve them over Q.

- If consistent, emit an exact extension and replay all seven new rows.
- If inconsistent, emit a rational combination of the seven affine equations
  equal to one.

Run blind in characteristic zero and 65521 on separate AWS hosts.  Each lane
has a 400 GiB virtual-memory cap and a 30-minute compiler/engine wall cap.
The result concerns only this literal finite source prefix; it is neither a
formal-arc extension nor a Jacobian-conjecture conclusion.

