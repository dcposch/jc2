# Hostile different-model review — TD6 licensed c1 line exclusion

Work in `/Users/dc/code/math/jc2`.  Review the exact logical union of three
separately frozen packages.  Read in full:

- `xmodel/td6-c1-line-kill-gate-20260824.md`;
- every file named by the manifests in
  `cases/td6_c1_quadratic_stratum_20260824/`,
  `cases/td6_c1_first_stage_ideal_20260824/`, and
  `cases/td6_c1_raw_transport_fibres_20260824/`;
- the generic first-stage and raw-fibre reports;
- the reviewed TD6 whole-qB pencil, adjoint, and centering-tangent packages
  that license the normalized section and source typing.

The charged combined report and final-stratum hashes are:

```text
combined report  dbf60b008f968033b7e91a5c5975bbedffc0529009aa53db6fb4b139bd844cb9
J MANIFEST       767af7e5de63b3a08dc495107b22a8ef568bca467eda9884a275dba1533905f0
J FREEZE         767af7e5de63b3a08dc495107b22a8ef568bca467eda9884a275dba1533905f0
J replay.py      86a7931e31e6d1387e3797a58094c6bfd69444910e2fdf7d27a374d9942a1e7f
J stdout         4a9f3022fb7fd1dcc0933dd17d636c423729c70cc58ce0fb4399323b486f5dd2
```

Recompute every manifest and registered replay as regression only.  Then
independently reconstruct and attack every load-bearing step:

1. Identify the exact normalized line `(c1,c2,c3)=(C,1,1)` and prove that
   the generic transport chart has exactly the exceptional fibres `C=0,3`.
   Check no boundary, dead-stretch, F1, pole, or other center modulus has been
   silently fixed after the advertised normalization.
2. Rebuild the generic transport and first-band systems from source.  Retain
   the genuine quadratic current `P12`; independently verify the original-
   row identity
   `D(C)P12=D(C)(-k/50)+sum M_i L_i`, its 28 source rows/1489 terms, and
   `D=(C-3)^2(4C^2+20C+1)/4`.  Check that polynomial multipliers make it
   valid across first-rank jumps and that only `D=0` remains on the transport
   chart.
3. Independently audit the raw `C=0,3` rebuilds: original 3602-column
   transport rank 3470, first rank 38, genuine current polynomial, and full
   original-row reduction to `-k/50`.  Never specialize a singular generic
   parameterization as evidence.
4. Rebuild the original transport rows over
   `E[C]/(J)`, `J=4C^2+20C+1`, without sampling a root.  Reproduce the
   transport/first ranks, zero compatibilities, 2893-term degree-two current
   polynomial, and full 28-row/1530-term source identity with all documented
   digests.
5. Do not assume `J` is irreducible over `E`.  Verify every one of the 38
   claimed Bezout inverses modulo `J` and explain why this covers all
   geometric components if the quotient splits.  Attack nilpotents,
   inseparability, zero divisors, and overlap with `C=0,3`.
6. Independently verify the exact inverse of
   `k=252-342S+144S^2-36S^3`; hence `-k/50` remains a unit after all scalar
   extensions in scope.
7. Prove or refute that the strata
   `C=0`, `C=3`, `C(C-3)J!=0`, and `J=0` exhaust the parameter line over
   every field extension.  Check every handoff between the three freezes and
   refuse any unsupported whole-line conclusion if a point is uncovered.
8. Enforce scope: even a confirmed result empties only this licensed fixed
   normalized one-parameter section.  It does not cover simultaneous center
   motion or other moduli and is not TD6, SP-2, a terminal class, or JC2.

Use exact arithmetic and genuinely independent scratch reconstruction;
producer PASS strings are not evidence.  Keep scratch outside tracked paths.
Do not edit producer, case, canonical, prompt/log/run, coordination, ladder,
or predecessor files.  Do not launch AWS.  Write exactly:

`xmodel/td6-c1-line-kill-review-grok-20260824.md`

Give one overall and per-item verdict from `CONFIRMED`, `GAP`, or `REFUTED`,
checked hashes, the smallest failing identity or missing hypothesis, exact
promotion language, and exact quarantine language.
