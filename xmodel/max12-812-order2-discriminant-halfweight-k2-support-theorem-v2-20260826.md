# `(8,12)` order two: K2 support theorem V2 scope repair

Date: 2026-08-26

Status: **NONMUTATING V2 REPAIR; ANALYTIC K2 SUPPORT THEOREM ONLY.
FULL-SOURCE PROMOTION REMAINS CONDITIONAL ON THE EXACT-Q V2
SOURCE/ANALYTIC ENDPOINT.**

## 0. Target and review

This note repairs, without mutating, the producer theorem

```text
20fa404c10c6fdafe59247967db8234f3479ae9a06740b521650b8a8aa88e341
  xmodel/max12-812-order2-discriminant-halfweight-k2-support-theorem-20260826.md
```

in response to the hostile review

```text
f93ecb4320fadff500638fc6fa7bdfca904ed5556b7a13add4cddb9b40a76b70
  xmodel/max12-812-order2-discriminant-halfweight-k2-support-review-terra-20260826.md.
```

The review confirmed the analytic mathematics and requested two scope and
custody corrections.  This V2 note is controlling wherever it differs from
the V1 target.

## 1. Ring-localization repair

Let

```text
R_m = Q[b,e,h,y,kappa,m][m^(-1)].
```

The ideal `I_K2`, all colons, and statements V1 (2.1)--(2.2) live in
`R_m`.  Statement V1 (2.3), its displayed exact standard basis, and its
radical statement live in the further localization

```text
R_bm = Q[b,e,h,y,kappa,m][(b*m)^(-1)].
```

Thus the exact repaired statements are

```text
(I_K2:kappa^infinity)=(1)                         in R_m,
((I_K2+(kappa)):e^infinity)=(1)                   in R_m,

I_K2=(kappa,e,U^2,V+6*y*U)                        in R_bm,
sqrt(I_K2)=(kappa,e,U,V)                          in R_bm,

U=h+b*y,  V=m^3+6*h*y.
```

No assertion is made on `m=0`.  That locus is excluded by the charged
first-contact saturation.  No assertion is made on `b=0`; inside `e=0`
it is routed to the rank-two square-intersection analysis.

## 2. Custody wording repair

At the freeze time of the V1 target, the two full-source modular V2 jobs had
reported remote PASS endpoints, but their output directories had not yet
been retrieved and frozen locally.  V1 Section 4's sentence that they
“verify” source/analytic equality is therefore replaced by:

> Two registered remote modular controls have reported PASS for the
> source/analytic ideal comparison and ordinary matched-unit sentinels.
> They are navigation controls until their complete outputs are retrieved,
> hashed, and frozen.  They do not replace the exact-Q promotion gate.

The direct-`m` analytic support package itself *is* locally frozen and has
the exact-Q and characteristic-32003 custody recorded in V1 Section 0 and
its charged `RESULTS.sha256`.

## 3. Surviving theorem and firewall

All other V1 statements survive unchanged.  In particular, in `R_bm` the
raw scheme is the doubled normal

```text
(kappa,e,U^2,V+6*y*U),
```

and its reduced support is exactly

```text
e=kappa=0,  h=-b*y,  6*b*y^2=m^3.
```

This is an analytic K2 support statement.  It becomes a theorem about the
frozen source rows only after the full-source exact-Q V2 ideal comparison
finishes, passes its fail-closed validator, and is retrieved with exact
custody.  Even then it is only an initial obstruction: the nonreduced
conormal must be carried into the correction-aware K3 receiver, with all
finite lower loads and terminal/Taylor typing retained.
