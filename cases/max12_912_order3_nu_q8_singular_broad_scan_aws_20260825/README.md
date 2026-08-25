# Selected-Q8 pure-Singular broad fixed-fibre scan (AWS-only)

This successor searches fixed nonzero `w` fibres of the exact localized Q8
quotient using **Singular `std` on the original eight generators**.  It does
not consume any `msolve` basis or conclusion.

The first matrix is all `w in F_127^*` except the six already audited values
`1,2,63,71,95,126`.  The dispatcher permits at most 90 concurrent lanes and
uses the frozen fixed-fibre runner in
`cases/max12_912_order3_nu_q8_fibre_specialization_aws_20260825`.

Priority discriminator:

1. a squarefree irreducible degree-190 eliminant;
2. otherwise factor partitions incompatible with nontrivial block sizes, or
   containing useful prime cycles.

Strict scope: a degree-preserving irreducible fixed fibre certifies generic
irreducibility over the same finite field away from specialization poles.  It
is not, without an integral/good-reduction certificate, a characteristic-zero
component theorem.  All prior `msolve` outputs are negative controls only.

Run on AWS only:

```sh
nohup ./dispatch_p127.sh REPO OUT_ROOT 88 >dispatch.stdout 2>dispatch.stderr &
```

The lightweight `weight_audit.py` independently solves the exact linear
support equations for a diagonal quasi-homogeneous scaling.  Run it remotely
with `run_weight_audit.sh`; it is a falsifier for the proposed all-nonzero-`w`
twist shortcut, not a Groebner calculation.

