# V18R1 negative-control engines aborted after exact witness

Date: 2026-08-27T01:09Z

Status: **ABORTED BY COORDINATOR; NOT A V18R1 PASS.**

Both V18R1 engines had printed the provisional positive token
`V18_SPECIAL_FIBRE_UNIT=1` and were still computing the preregistered
drop-grade-14 standard-basis control.  Opus5 then supplied an explicit
rational point of the frozen negative-control ideal, and Grok independently
reparsed the raw frozen rows and confirmed all 21 exact zeros, all four
localizer equations, and `Tg14_5=-21/320`:

```text
d9e5f43954240eee13311c5f386231f9ed506c4bbe978211cdfa711e3e8c86d9
  xmodel/max12-812-order2-p0-total-rees-t-cs-drop-g14-witness-opus5-20260827.md
7fbd9423b6840e4f3017687897e0dad373a04d2683589ccb432682553053c3cf
  xmodel/max12-812-order2-p0-total-rees-t-cs-drop-g14-witness-hostile-review-grok-20260827.md
```

One exact point proves that `1` is not in the dropped-row ideal, independently
of term order.  The same point reduces to the registered F65521 lane.  On the
reviewer's explicit stop recommendation, the coordinator terminated only the
two exact V18R1 process trees; V19 and unrelated host jobs were untouched.

## Exact stopped lanes

```text
Box02/Q
  tag=max12_812_order2_p0_total_rees_t_cs_rho_unit_v18r1_20260826T232600Z_q
  session/process group=346794, with nested engine groups 346812 and 346814
  partial stdout SHA=80958e0027e720519327eac6cc2fc6a7eb25db7ba316b5c91a9a373c9271802b
  partial stderr SHA=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

r6d/F65521
  tag=max12_812_order2_p0_total_rees_t_cs_rho_unit_v18r1_20260826T232600Z_p65521
  session/process group=358621, with nested engine groups 358639 and 358641
  partial stdout SHA=a2d5715642fb93b711a1434b13a0d10c1994641b8fb97921329f396b20cf2457
  partial stderr SHA=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The partial remote directories are preserved.  Neither lane reached
`engine.validation`, `validator.validation`, `RESULT.json`, or
`EVIDENCE.sha256`; neither may be reported as
`PASS_T_CS_RHO_UNIT_V18R1`.  The provisional positive stdout tokens remain
producer observations only.  The reviewed exact witness replaces the
negative-control computation mathematically, not the V18R1 validator or
V19's explicit cofactor obligation.
