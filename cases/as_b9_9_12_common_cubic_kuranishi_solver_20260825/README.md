# B9 common-cubic Kuranishi structural compression

This successor consumes the reviewed exact reduction
`K : F3^95 -> F3^176` for one fixed B9 mod-243 parent and compresses its
output coordinates without sampling.

- `AWS_STRUCTURAL_SPAN`: two-host, byte-identical exact relation certificate;
  rank 111 when distinct source-DAG atoms are treated formally.
- `AWS_STRUCTURAL_SPAN_CONSTANTS`: exact constant evaluation identifies the
  sole constant atom as zero and refines the rank to 110.
- `AWS_DEPENDENCIES`: exact syntactic input-support analysis.  Ten of 95 chart
  inputs are absent; the remaining 85 form one incidence component.
- `AWS_CONTROLS`: 447 sampled controls.  These are diagnostics only and do not
  establish the zero locus.
- `AWS_BITBLAST_NEGATIVE`: Z3 tactic failure (`table overflow`), not evidence.

The exact producer claim is only

```text
K(x)=0 iff K_i(x)=0 for the 110 certified original coordinate rows i.
```

No SAT/UNSAT, lift, all-depth, counterexample, maximum-12, or JC2 claim is
made.  Heavy replays are AWS-only; runners refuse non-Linux execution and
unregistered AWS tags.
