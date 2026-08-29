# Hostile review: H18/q6/a6 grade-54 direct unit

Work in `/Users/dc/code/math/jc2`.  Write the unique report

```text
xmodel/max12-812-order2-affine-faber-a-h18-q6-a6-g54-direct-unit-hostile-review-grok-20260826.md
```

Do not edit charged artifacts, shared ledgers, or `jc2-lean`.

Charged producer custody:

```text
f1a463578cf622c9082241858e4ea56a74055a361ed9894a37efa8c5fbdf9382
  cases/max12_812_order2_affine_faber_a_h18_q6_a6_g54_direct_unit_v1_20260826/FREEZE.sha256
ec8e0ecc9e97cc70cc0da5030210139aa9783a305077b4eed941fc101d8665d2
  cases/max12_812_order2_affine_faber_a_h18_q6_a6_g54_direct_unit_v1_20260826/RESULT.md
ca10926b5243706791424b10387f02903663ed2df8792562fb98a12abb6f7c9b
  cases/max12_812_order2_affine_faber_a_h18_q6_a6_g54_direct_unit_v1_20260826/EVIDENCE.sha256
55b6fc500cf48c1049a4df126762c948ac45f99a6efe97d40450a783c2b7e421
  cases/max12_812_order2_affine_faber_a_h18_q6_a6_g54_direct_unit_v1_20260826/RESULTS.sha256
```

The source compiler SHA is `1e04a8badb47f557b7daa5388d007eebb3ada950a6b0e248779a6db13d9c2c6a`.
The exact-Q serialized functional SHA is `1c761b1aac81006bdbbcb3fbec1fd476b7749c0b8ea64875234a9bf1b8c9676c`;
the F65521 control SHA is `35763b3650ef00a041570d48ca4abcd2fc9e14e00e82be3d8be237638cd02e8c`.

Independently attack:

1. Reconstruct the normalized weights `lambda=18`, `a=X=Y=6`,
   complements `12`, loads `42`, and `J=57`.  Check every center,
   `E,M`, kernel/complement, load, and load-deviation jet that can reach
   grade 54 is present; identify any omitted term.
2. Starting from the complete frozen Faber tails, independently verify the
   raw odd-row functional
   `H=2E^2 P3+16E P5+64P7-(E^3/2)P1`, its vanishing below grade 54,
   and the exact coefficient `[s^54]H=-2m^3p^2` over Q.  Do not infer the
   Q identity from the modular run.
3. Check that moving-center/tangent corrections and the affine load graph
   `K6=(15/32)K10 E^2+s^48 d6`,
   `K2=(15/256)K10 E^4+s^48 d2` cannot alter the grade-54 unit.
   Check all target modes, including whether any `J`, `mu4`, or `mu6`
   contribution was suppressed too early.
4. Check that localization on `D(p*m)` really makes the coefficient a
   unit and that this proves emptiness only of the fixed normalized graph
   cell.  Distinguish producer evidence from an exhaustive q-cell/fan
   theorem.
5. Enforce the source firewall: `(H,q,a)=(18,6,6)` satisfies the leading
   slope-four congruence, but a literal rational-source germ needs the
   full `mu_3` fixed-locus condition on every series coefficient.  Do not
   infer total-Rees/Taylor realization, order two, maximum twelve, or JC2.
6. Audit software semantics: ordinary exact sparse dictionaries are
   charged; no Singular quotient-ring equality is licensed.  Treat stale
   diagnostic labels `H17Q7_*` as cosmetic only if the actual overridden
   valuations and jet sets are correct.

Start with a pin/verdict table, state the smallest exact defect if any, and
end with exactly one standalone verdict token `CONFIRMED`, `REPAIR`, or
`REFUTED`.
