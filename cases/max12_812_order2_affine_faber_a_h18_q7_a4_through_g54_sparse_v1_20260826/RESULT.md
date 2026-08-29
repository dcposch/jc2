# Result: H18/q7/a4 rows through grade 54

Date: 2026-08-26

Status: **DUAL-AWS PASS; NORMALIZED NAVIGATION ONLY.**

Exact Q and the independent F65521 control reconstruct all seven frozen
ordinary-Faber rows through grade 54 with the registered H18/q7/a4
normalized weights.  Both lanes verify:

- the affine graph through grade 47;
- the two `mu4`-only predecessor grades 48 and 49;
- the complete grade-50 row control;
- `mu6` first at 54 and `J` first at 57;
- the exact grade-54 functional

```text
H54=-2*m^3*p^2+(5/4)*kappa*a4^3*p^7.
```

The raw grade-54 companion `K` has ten terms, all preserved in the emitted
JSON.  No sequential elimination was run, so this package records the
receiver equations rather than a unit or survivor verdict.

The source-descent erratum is controlling: on the balanced slope-four
ray, `q=7` and `ord(a)=4` are not `mu_3`-fixed source valuations.  This
calculation is therefore a normalized support/control artifact and cannot
be cited as rational-source accessibility.

## Evidence

- source manifest SHA `a3167b43faa94c5ad7a350ed14d842e39d844ed3bdc91b18475773e453c35a93`;
- exact-Q rows/functionals SHAs `ee5e56c67a2939a44f7e03c7c7439f678bf96a629405b18a0333608919ff9915` / `88ba95c34cf4019d60c31b7910787fbe1c72eb681647b8f5aa22416267603ac7`;
- F65521 rows/functionals SHAs `fde63767823ccd09c5b66a4ec2c314e6bc042e2b0e9b311528d93cbd658938da` / `7536c84f637c39494d9fa3153bfa82ce947c66922905c35eac4cd5d928fa96b9`;
- both validators say `PASS_A_H18_Q7_A4_THROUGH_G54_V1`.

No source atlas, Taylor, order-two, maximum-twelve, or JC2 conclusion is
licensed.
