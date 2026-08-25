# Squarefree Poisson recurrence through degree 15

## Exact result

Dual AWS runs verify the complete original determinant-row identities in the
squarefree chart `K=x*y*(x-y)` from degree 18 through degree 15.  The
independent exact centralizer checker gives a one-dimensional homogeneous
centralizer precisely in degrees divisible by three and zero otherwise
through degree 18.  The Singular checker verifies the displayed recurrence,
including the complete degree-18 package and solution, the degree-17,
degree-16, and degree-15 packages, and the reduced squarefree family with
predicted base dimension 16 plus fresh dimension 6.

The consequences `K|P8`, `K|R5`, and `K|P7` use squarefreeness at reduced
geometric points.  They do not identify the nilpotent incidence scheme.

## Positive endpoints

- r6d, `ip-172-30-0-45`, tag
  `max12_912_order1_squarefree_poisson_recurrence_v4b_r6d_20260825T1927Z`;
- Box02, `ip-172-30-0-186`, tag
  `max12_912_order1_squarefree_poisson_recurrence_v4b_box02_20260825T1929Z`.

Both are rc zero.  Their algebraic stdout bytes are identical.  The two
hosts are custody mirrors of the same implementations; source independence
is between `verify_centralizer.py` and the Singular identity checker, not
between hosts.

## Quarantine

- V1 failed closed with a Python `IndexError`.
- V2 printed apparent PASS markers after Singular parse/undefined-symbol
  errors.  It is an executable false-PASS control and contributes no result.
- V3 is a clean precursor through degree 15 but lacks the V4 degree-18
  control.
- the first V4 launcher returned rc126 because the staged runner lacked its
  executable bit; V4b invokes the pinned bytes through `bash`.

## Scope firewall

This is a source-row and reduced-point recurrence theorem.  It does not prove
lower bands or a full Keller pair.  Moreover, the strict total-degree
`(9,12)` box is already counterexample-closed by the classical
`gcd(deg P,deg Q)>=16` bound.  The reusable target is a weighted or
partial-`y` unbounded-total adapter, which still requires its own filtration
and centralizer proof.  No selected-Q8, maximum-twelve, counterexample, or
JC2 conclusion is made here.

Run `python3 replay.py` for the hash/custody replay.
