You are the hostile independent commutative-algebra/tropical referee for an
exact first omitted-support witness in the plane Jacobian-conjecture campaign.
This is a text/source/custody review only.  On the local Mac do not run
Singular, Sage, msolve, gfan, Lean, Python algebra, or any solver.  You may
read files, recompute SHA-256, use cmp/diff/sed, and do hand algebra.  If a
new substantive computation is required, fail closed and request AWS replay.

Review the complete frozen package

```text
cases/max12_912_order3_d1_double_root_control2_q2_syzygy_lift_v2_20260826/
```

Required hashes:

```text
994ef6231c4ec705c8b14bda418f046ce0ce45603e6b597141eac6d1884e4c34  FREEZE.sha256
5c81cd8bfaf80d34ad9211fafdc50ab58a4582c68988f5de4c6bdeb593a66213  RESULT.md
f6938514c9d050e45f46a3a37b331d1ef8904d32939acdfc902e21757e81b2d5  SOURCE_CLOSURE.sha256
```

Also audit the predecessor negative control and reviewed fixed-support
witness rather than inheriting their conclusions:

```text
cases/max12_912_order3_d1_double_root_control2_q2_first_lift_v1_20260826/RESULT.md
cases/max12_912_order3_d1_double_root_control2_la20_syzygy_v2_20260826/WITNESS_RESULT.md
xmodel/max12-912-order3-d1-double-root-control2-la20-witness-review-grok-20260826.md
```

Charges:

1. Recompute every `FREEZE.sha256` entry.  Audit both AWS host/tag/job/PID,
   compiler/solve hash gates, source closure, caps, rc, empty compiler and CAS
   stderr/diagnostics, timing/RSS/swap, selected expanded input, and result
   custody.  The retrieved per-host source closure refers to sibling source
   files retained at the package top and on AWS; use the frozen remote
   `source.check` plus top source closure rather than treating the harvested
   subdirectory alone as a new source root.
2. Trace construction of all eight full-`q2` rows from the hash-pinned charged
   ordinary-tail compiler and pinned expanded-B base.  Confirm the historical
   erroneous factored A/E8 source is not consumed.  Audit the literal
   `q2=0` comparisons for all eight rows and exact full polynomial identity.
3. Recompute by hand the first bad coefficient and reconcile, as equal
   polynomial representations, both

   ```text
   C52=(1/9)in52(E2)-(1/12)in52(E1)
   C52=(2/81)GH3-(1/27)GH5+(2/27)GH6.
   ```

   Verify that solving `sum g_i in52(E_i)=-C52` gives the pinned correction
   `(g1,g2,g3,...,g8)=(1/12,-1/9,0,...,0)`.  Charge signs and row numbering.
4. Audit that `F1'=F1+q2/12`, `F2'=F2-q2/9` and the unchanged other
   multipliers give an **exact full polynomial** `W'`, not only a congruence
   modulo `q2^2`.  Confirm both encodings give the same canonical `W'` and
   correction hashes despite tag/ring-dependent printed monomial order.
5. Independently charge every term weight at
   `(L,T,H;D;beta L;alpha L)=(4,1,1;23;22;30)`.  Confirm or refute that the
   unique least term of all 37 terms is `la^20` at weight 80, hence there is
   no remaining below-target layer at this weight and `la^20` belongs to the
   exact submitted row ideal's weighted initial ideal.  Explain precisely why
   this empties the coordinate torus.
6. State the strongest licensed theorem and firewall.  Do not promote this
   one weight to a full Groebner cone, all q2 valuations, moving axis/cusp,
   moving loads, another support mask, formal-arc obstruction, whole
   double-root fan, D1, or JC2.  Distinguish `old witness does not transport`
   (V1 negative control) from `a corrected witness exists at this weight`.

Write exactly one review to

```text
xmodel/max12-912-order3-d1-double-root-control2-q2-syzygy-lift-review-grok-20260826.md
```

Do not edit any producer file, top-level file, or other report.  Include
recomputed hashes, exact promotion text (or smallest repair), and end with
exactly one of `Q2_SYZYGY_LIFT_CONFIRMED`, `Q2_SYZYGY_LIFT_REPAIRED`, or
`Q2_SYZYGY_LIFT_REJECTED`.
