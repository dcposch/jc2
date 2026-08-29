# Independent J2 grade-15 certificate design

You are Fable 5, an equal blind co-researcher. Work in
`/Users/dc/code/math/jc2`. Do not edit canonical files, case inputs, or
`jc2-lean`. Your sole repository write is:

`xmodel/max12-812-order2-p0-total-rees-j2-grade15-certificate-design-fable5-20260827.md`

This is a speculative, reversible child of provisional V22R1; its Grok
review is already running. Read the V20/V21/V22 producer and review artifacts,
then audit the lightweight exact census case

`cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827/`.

Notice and respect the V1 control erratum: V1 confused the full a0 chart with
the point `qa1=0`; only `output_r1/RESULT.json` is accepted. Rehash the R1
freeze and result before use. Independently inspect the literal specialized
polynomial bytes rather than trusting its summary.

Research question: what is the fastest exact route from the new grade-15
cubics to a correctly typed direct total-source certificate on each of the
two stage-two charts over `A/J1`, `J1=(rs,cs,c0,c1)`?

- `T-a0`: substitute `a1=a0*qa1`, saturate only by the exceptional coordinate
  `a0`; retain every genuine localizer (notably `k` if used).
- ordered `T-a1`: work on the closed complement `a0=0` and the `a1` chart;
  do not invert `rho`, jet coordinates, or any exceptional coordinate in the
  polynomial identity.

Try to prove or disprove low-degree certificate shapes from the literal rows.
The strongest target is an honest identity putting a power of `a0` or `a1`
(possibly times a genuine `k` power, and with a correctly typed
`1+rho*W`) in the appropriate source-plus-chart ideal. Focus first on the
small grade-11/12 core and the sparse grade-15 row 6 before attempting broad
elimination. Track the full pure a0-chart cubic vector:

```text
Tg15_3: -(1/16)a0^3 qa1^3
Tg15_4: -(3/16)a0^3 qa1^2
Tg15_5: -(3/16)a0^3 qa1 -(3/32)a0^3 qa1^3 rho^2
Tg15_6: -(1/16)a0^3 -(3/16)a0^3 qa1^2 rho^2
Tg15_7: -(3/32)a0^3 qa1 rho^2 -(3/128)a0^3 qa1^3 rho^4
```

and the ordered a1 pure terms in rows 3,5,7, but verify them yourself.

Deliver one of:

1. an explicit exact certificate with every cofactor printed and a direct
   residual-zero replay; or
2. a precise algebraic obstruction/counterpoint to the proposed certificate;
   or
3. a hash-ready AWS experiment specification with ring, generators, target,
   grading bounds, saturation/localizer semantics, controls, resource cap,
   and stop rule.

You may combine these outcomes and stratify the charts if that is genuinely
forced. Distinguish point killing from chart emptiness, ideal membership from
radical membership, and source rows from unwritten Rees equations. Use only
bounded local read-only checking (temporary files under `/tmp`, under one
minute/1 GiB per exact desk probe); all uncertain/heavy CAS belongs on AWS
and must not be launched by this lane. No web, no AWS mutation. End with a
ranked immediate successor queue and explicit dependency/scope firewall.
