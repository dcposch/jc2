# Registration: discriminant half-weight K3 normalized-ray source separator

Date: 2026-08-26

Status: **IMMUTABLE SOURCE PREREGISTRATION; NO RESULT AT FREEZE.**

This client keeps the raw analytic K2 scheme
`(kappa,e,U^2,F)` on `D(b*m)` and compiles its primitive normalized ray
`wt(U,e,kappa,F)=(1,2,2,2)` by setting `rho=sigma^2`.  It extracts the
complete frozen-source `sigma^14` coefficient after checking the
`sigma^12` base and `sigma^13` kernel grades.  Each of all seven source rows
is compared with the exact unitriangular Laurent-to-Faber transform of the
analytic row; comparing two already-unit ideals is explicitly forbidden.
The compiler also inserts independent first tangent coefficients in
`b,t,q,s` and requires their derivatives in every `sigma^14` source row to
vanish.  This charges, rather than assumes, that tangent variation changes
the intrinsic exact-family coefficient only at `sigma^15` and that normal
cross terms have weight greater than two.

Registered lanes:

```text
tag=max12_812_order2_disc_halfweight_k3nr_q_20260826T071500Z_box03
host=Box03 / 98.80.65.144
job=/home/ubuntu/jobs/max12_812_order2_disc_halfweight_k3nr_q_20260826T071500Z_box03

tag=max12_812_order2_disc_halfweight_k3nr_p32003_20260826T071500Z_r6d
host=r6d / 100.26.198.153
job=/home/ubuntu/jobs/max12_812_order2_disc_halfweight_k3nr_p32003_20260826T071500Z_r6d
```

Both use one core, a 16-GiB virtual-memory cap, a 300-second compiler cap,
and a 900-second Singular cap.  Exact Q is the characteristic-zero endpoint;
the prime is an independent control.  A timeout or failed sentinel is no
mathematical verdict.

Scope: a PASS excludes the explicitly parametrized nonsquare discriminant
normalized-ray tail branch.  Exhaustive frozen-source discriminant coverage
still consumes the separately frozen exact-Q K2 source/analytic equality
promotion.  The square route, both Taylor families, order two, `(8,12)`,
maximum twelve, and JC2 remain open.
