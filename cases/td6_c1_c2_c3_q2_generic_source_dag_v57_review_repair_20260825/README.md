# V57 generic-source-DAG hostile-review repair

This is a nonmutating supplement to
`../td6_c1_c2_c3_q2_generic_source_dag_v57_aws_20260825/`.  It preserves
the producer source, dual-host outputs, N13 proof DAG, denominator ledger,
archive, and all mathematical hashes.

The hostile review in `evidence/hostile-review-adapter.log` returned
`CONFIRMED_WITH_REPAIRS` and confirmed the exact localized source identity
on `D(U*H*B3)` in the fixed source-typed A3 q2-beta section.  This
supplement makes its required scope/terminology/custody repairs:

1. The fourteen printed `previous_rows_source_lifted_keys` are a union lift
   cache for P12 and N13 plus a quadratic positive control.  They are not
   the N13 ancestry.  N13 has exactly one nonzero original previous-row
   summand, of type `X-1`; no original pole row is an N13 summand.  The
   frozen producer does not print that singleton key, so this supplement
   does not invent it.
2. `one_required_edge_omission_negative_control` is read only as
   `N13_singleton_current_row_omission_negative_control`: it drops the
   unique current row, not the downstream previous edge.
3. The live V57 glue proves
   `P12_first_remainder_minus_M_n13_equals_minus_k_over_50`; the fully
   expanded original-row P12/N13 identity remains the hash-pinned V43
   dependency, not a second V57 expansion.
4. The q/q-prime prose banners precede configuration and are not evidence.
   The live post-transport call `configure_qd(direct_qprime=True)` installs
   `q'=1+2*beta*t+25*t^24`.  The source asserts `k*k.inverse()==1`; hence
   `k` is a residue-field unit even though the old stdout lacks that named
   marker.
5. The eleven-line denominator table is a leaf-coefficient ledger for the
   N13 DAG plus the P12 tail/unit/multiplier.  Its radical is exactly
   contained in `{U,H,B3}`.  V43's termwise clear has an additional power
   `H^3` but the same radical and is a parent pin.
6. Four helper files lacking import-time SHA assertions are nevertheless
   byte-pinned by `V57_SOURCE.sha256`; this is archive-custody pinning, not
   an import-time assertion.  The internal v55/v56 archive name, unused
   members, pyc, and one-second r6d timestamp drift are custody nits only.
7. The old `two_chart_glue_required_form` line is withdrawn as an unproved
   design banner.  V57 proves one principal-open identity only.

The surviving theorem is exactly the V57 original-source N13/P12 identity
on `D(U*H*B3)`.  It proves no divisor cover, whole A3, transverse
neighborhood, TD6, SP-2, landing, or JC2 statement.
