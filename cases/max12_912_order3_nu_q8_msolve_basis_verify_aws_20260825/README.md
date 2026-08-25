# Selected-Q8 `msolve` basis verifier

Date: 2026-08-25

This successor independently checks a fixed-fibre elimination basis emitted by
`msolve`.  It reconstructs the exact original eight equations from the pinned
`.ms` input, parses the reported block-elimination basis, and asks Singular in
the identical finite field and block order to:

1. reduce every original generator by the reported basis;
2. report the basis dimension and vector-space dimension;
3. check squarefreeness and factor the univariate `v` eliminant.

The reduction is an exact old-system/new-basis certificate.  In particular it
guards against treating an `msolve` output-mode discrepancy as geometry.
Passing only proves that the reported shape basis cuts out genuine solutions
of the fixed modular fibre.  It does not prove the reverse ideal inclusion,
generic degree preservation, characteristic-zero lifting, component grouping,
or any trajectory statement.

Run on the authorized remote host, pointing to a completed elimination lane:

```sh
cases/max12_912_order3_nu_q8_msolve_basis_verify_aws_20260825/run_remote.sh \
  /home/ubuntu/jc2q8-generic/repo \
  /home/ubuntu/jc2q8-generic/out/fixed-msolve-verify \
  q8_fixed_p89_w1_msolve_verify_v1 \
  /home/ubuntu/jc2q8-generic/out/fixed-msolve/q8_fixed_p89_w1_msolve_elim_v1
```

Resource envelope: 30 minutes and 16 GiB virtual memory.  The computation is
remote-only under the standing local-memory directive.

