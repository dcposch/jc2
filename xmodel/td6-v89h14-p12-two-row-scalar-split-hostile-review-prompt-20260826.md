# Hostile review charge: TD6 V89H14 P12 two-row/six-scalar split

Date: 2026-08-26

Independently audit the frozen producer package

```text
cases/td6_c1_c2_c3_allq_mod_f_unitriangular_functional_v89h10_aws_20260826/
```

with controlling hashes

```text
P12_TWO_ROW_SCALAR_RESULT.md       88f4354b7b639d098e91b96e07ffbed1793d5c73aed8cc8014ba2b5996adf2e3
P12_TWO_ROW_SCALAR_EVIDENCE        4b19cfa4d518ffbcbccf4fde2dfc21bae435a50a61817e1f7fcb804365a45dec
P12_TWO_ROW_SCALAR_FREEZE          0e2aa4a0cb1c0e01b025f2de061cf0d70f093a68654fcc40eccc1929a0d811e7
PREREGISTRATION                    34338772b99db1616e1f6bf6d860655e58ec67d89136f844cd7eebc7aa4dcdbf
SOURCE manifest                    1103a905a378d885f607253ae8888d26fcb961d19a08d72b94ab87a4194f0100
source archive                     0a4c6eed75888e72fad759709b608f10de6f859d3dca6e6cdd515ede6076d381
client                             3c842d74ee9aa4da01e6474970e342d2f15cb1df8db68a1046cbb900234615c7
V89H12 normal form                 c8a738b6024ac02e56455674efa8c89c37684a87e0312141a5ca4259ca02e4c4
```

Charge every load-bearing point:

1. Rehash the freeze, archive, source and evidence manifests.  Verify both
   AWS lanes returned rc 0 and have byte-identical stdout and every exact
   artifact.  Reparse the frozen 166-record V89H12 TSV independently.
2. Verify that every coefficient of a nonempty parameter monomial is exactly
   zero in E3 coordinates 2 through 17 and that coordinates 0 and 1 both
   genuinely occur.  Verify the empty-parameter coefficients occur only in
   coordinates 0 through 7, all eight occur, and coordinates 8 through 17
   vanish in every record.  Reject any inference based only on finite-field
   sampling or noncanonical string formatting.
3. Confirm coordinates 2 through 7 give exactly six quotient-variable-
   independent affine-linear equations with q support q3 through q14; q2 and
   q16 through q24 must be absent after the complete literal reduction, not
   omitted by this client.
4. Verify the q2 block in rows `(0,1)`, columns `(y24,y27)` is exactly
   `[[6,8],[0,4]]`, all other q2 parameter records are absent, and the
   displayed determinant has q2-squared coefficient 24.  Check carefully
   that higher/mixed q terms cannot cancel this monomial coefficient.  This
   must prove generic coefficient-matrix rank exactly two, not a global rank
   or unit-minor claim.
5. Recompute the 6-by-12 scalar coefficient matrix in q3 through q14 at the
   denominator-safe point `(U,V)=(1,3)`.  Verify pivot columns
   `q3,q4,q5,q6,q7,q9` and exact determinant
   `-1656161280873829337287680`.  Confirm a nonzero valid evaluation proves
   generic rank six over `Q(U,V)`, while supplying no right to invert that
   minor throughout `D(U*H*B3)`.
6. Hostile-audit the fraction-field rational-section corollary.  Because the
   six scalar equations have full row rank, solve them over `Q(U,V)` for the
   six pivot q variables in terms of the remaining q variables.  Confirm q2
   is absent and may remain transcendental.  After this substitution, prove
   the `(y24,y27)` determinant remains a nonzero polynomial in q2 with
   leading coefficient 24; then rows 0 and 1 can be solved for those two y
   variables, while rows 2 through 7 and 8 through 17 are already zero.
   Seek any hidden dependence, denominator-zero issue, or mismatch between
   quotient coordinates and the original FIRST normal form.
7. Decide explicitly whether that rational section really rules out a global
   claim `q_ideal subset sqrt(P12,FIRST,F)` on the registered open.  It must
   not be promoted to a literal total-source point, later-CURRENT solution,
   total-Rees chart, or JC2 counterexample.  Explain why it does not conflict
   with pure-axis exclusions such as V89H7: mixed low q is essential.
8. Confirm no Singular qring semantic hazard and enforce scope.  The theorem
   is an exact P12/FIRST structure and negative routing result only; later
   CURRENT grades/source conditions remain open.

Return exactly one verdict: `CONFIRMED`, `CORRECTED`, or `FALSIFIED`, with
the smallest repair if applicable.  Report exact file/line evidence for every
material issue.

Write the complete report only to

```text
xmodel/td6-v89h14-p12-two-row-scalar-split-hostile-review-report-20260826.md
```

Do not edit the producer package, campaign ledgers, or `jc2-lean`.
