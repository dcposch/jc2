# V89H1 V1 deployment erratum

The first dual launch at stamp `20260826T162000Z` exited before importing the
generic parent because the wrapper did not export the three frozen ancestry
sentinels `TD6_Q_EXPONENT=2`, `TD6_PIVOT_POLICY=ascending`, and
`TD6_PIVOT_SCOPE=all-staged`.  Both hosts failed at the same environment
assertion in `replay_v85tf1_total_f.py`; no transport or algebra ran and no
mathematical output was emitted.

V2 adds exactly those import sentinels.  They select the frozen generic
compiler and do not alter the V89 high-q scope, which remains independently
registered as `TD6_Q_SCOPE=high-16-24`.
