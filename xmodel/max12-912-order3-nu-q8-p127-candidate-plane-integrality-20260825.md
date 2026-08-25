# Max12 `(9,12)` selected-Q8 candidate plane curve over `F_127`

Date: 2026-08-25  
Status: **producer-exact for the explicit candidate `H`; hostile different-model review required**

## 1. Exact specializations

Let `H(w,v)` be the pinned monic degree-190 interpolation candidate of SHA
`9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce`.
Pure Singular factorization over `F_127` gives squarefree specializations

```text
w=25: factor degrees 2 + 188,
w=47: factor degrees 1 + 3 + 186.
```

Both specialized polynomials retain `v`-degree 190.

## 2. Arithmetic irreducibility

Suppose `H=A B` nontrivially in `F_127(w)[v]`.  Since `H` is monic in `v`
and `F_127[w]` is integrally closed, the factors may be taken monic in
`F_127[w][v]`.  Their `v`-degrees therefore do not drop at `w=25` or
`w=47`.

A proper factor degree would consequently have to belong simultaneously to
the proper subset-sum sets

```text
{2,188}
{1,3,4,186,187,189}.
```

The sets are disjoint.  Hence `H` is irreducible in `F_127(w)[v]`.

## 3. Geometric integrality

The same exact replay gives

```text
H(71,50)   = 0,
H_v(71,50) = 104 != 0  in F_127.
```

Thus the arithmetically integral curve has a smooth `F_127`-rational point.
If it split geometrically, Galois would act transitively on its geometric
components.  The rational point is Galois-fixed, so it would lie on every
conjugate component and would be singular, a contradiction.  Therefore the
explicit candidate plane curve is geometrically integral.

## 4. Exact AWS replay

The fail-closed replay ran on AWS Box02 host `ip-172-30-0-186`, tag
`q8_p127_candidate_plane_integrality_box02_v1`, and exited zero.  The
independent audit rechecks factor degrees, squarefreeness, both subset-sum
sets, the point, and its nonzero `v` derivative.

```text
generate.py       ef82e789bb728660fc6a573431d8498859afa3c85f278708240b078ad9b9c9c5
audit.py          f75e28808833c94b4593c16dcf47a14c05b2b064a96ee0723b5354976807b7e4
run_remote.sh     8f5dd3740d55b4f8b9f9e232921911d507ac288a448ca02fd047af27294305b0
input.sing        ae40ca50011ace583f31e815191640320f2ce2da0181ba4c39150cf28e0bc507
result.out        3e2b15c1304fed5ab31335a2c4b3834926929ae57f4a56a99a36969bb47c6919
audit.json        0665a7cdced0a0da6286ffff0e5d5662fcce59a936fed6f09d164bbbfb4c2ced
stderr files      e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The portable case is
`cases/max12_912_order3_nu_q8_p127_candidate_plane_integrality_aws_20260825`.

## 5. Scope firewall

This theorem concerns the standalone explicit polynomial `H` only.  It does
not prove `H` lies in the selected-Q8 quotient ideal, that its curve is a
component of that quotient, that the reconstructed coordinate functions are
rational, that all eight Q8 contacts lie on it, or any characteristic-zero,
trajectory, maximum-twelve, or JC2 conclusion.

