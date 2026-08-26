# `(8,12)` order two: principal-part formula and exact `k10=0` UFD split

Date: 2026-08-26

Status: **PRODUCER EXACT THEOREM FOR THE PRINCIPAL-PART IDENTITY AND THE
`k10=0` REDUCED SUPPORT; FULL `Q1*` SCHEME EXHAUSTION NOT CLAIMED.**

## 0. Frozen inputs

```text
827e76bde5d394ab17f7c05561a1bf254b6fdf8fc3453dd60400d16e80061fdc
  xmodel/max12-812-order2-first-normal-divisibility-jet-theorem-20260826.md
27275f3d13471521bec0016d4fbc6e12d5bf8e539deeb4694fe0c01f04b025bd
  xmodel/max12-812-order2-first-normal-divisibility-jet-review-grok-20260826.md
092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e
  xmodel/max12-812-order24-coefficient-infinity-source-audit-20260825.md
aa90155ec8a182f4f451c77fc9548cf8035889efc230afdaea622f84eb18c495
  xmodel/max12-812-order24-coefficient-infinity-source-audit-erratum-v2-20260825.md
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
c474e05fa61be48ed9271c1b5c458a875882d8554163b82566138b4eab5da46a
  cases/max12_812_order2_first_normal_jet_20260826/RESULTS.md
818f5d158af41eb93c7a945f46ad143340e9afaa0086eaabd7869c5a0d1d9715
  cases/max12_812_order2_first_normal_jet_20260826/RESULTS.sha256
```

The dual-prime result is consumed only as navigation in §5, not as evidence
for the exact theorem in §§1--4.

## 1. Principal-part identity, with sign and constant

Write

```text
K=z^4+p z^2+c z+r,
N=n3 z^3+n2 z^2+n1 z+n0,
f_Lambda=K^2+Lambda N,
w_Lambda=f_Lambda^(1/8),
w0=K^(1/4).
```

In the reviewed one-parameter family the first active lower load is
`Lambda^2 k10`, and

```text
H_Lambda(T)=T^12+Lambda^2 k10 T^10+O(Lambda^6).
```

For a Laurent series in `z`, let `[ ]_-^z` denote its strictly negative
part after subtracting its `z`-polynomial part.  Let `z0(w)` be the inverse
of `w0=K^(1/4)=z+O(z^-1)`.  Then the exact coefficient of `Lambda^2` in the
full Faber tail is

```text
sum_(ell>=1) q_ell w^(-ell)
 = [ (3/8) N^2/K + k10 K^(5/2) ]_-^z evaluated at z=z0(w).     (1.1)
```

In particular the seven rows of the reviewed first normal gate are the first
seven coefficients of (1.1).

Proof.  At fixed `z`,

```text
(K^2+Lambda N)^(3/2)
 = K^3+(3/2)Lambda K N+(3/8)Lambda^2 N^2/K+O(Lambda^3).
```

The constant and linear terms are polynomials in `z`; the Faber polynomial
removes them.  The quadratic remainder is therefore
`[(3/8)N^2/K]_-^z`.  The load term has the reviewed sign of `H-g`, hence is

```text
k10 (w0^10-F_10(K^2)) = k10 [K^(5/2)]_-^z.
```

Both contributions begin at `Lambda^2`.  Substitution of
`z_Lambda(w)=z0(w)+O(Lambda)` can change them only in order at least three,
so the second-order coefficient uses `z0(w)` exactly.  This proves (1.1).
The coefficient is `+3/8`, not `-3/8`, and the load sign is positive because
the frozen convention is `H(w)-g(z(w))=sum r_ell w^-ell`.

## 2. Exact `k10=0` criterion

Assume `k10=0`.  Then

```text
q1=...=q7=0       iff       K divides N^2 in L[z].              (2.1)
```

Here `L` is any characteristic-zero coefficient field.

Indeed `w0=z+O(z^-1)`, and therefore `z0=w+O(w^-1)`.  Composition by
`z0(w)` gives a unitriangular change between the first seven negative
`z`-coefficients and the first seven negative `w`-coefficients.  Thus
vanishing of `q1,...,q7` forces at least the first four negative
`z`-coefficients of `N^2/K` to vanish.

Divide `N^2=AK+R` with `deg R<=3`.  The first four coefficients of the
proper fraction `R/K` are a unitriangular linear transform of the four
coefficients of `R` (the diagonal is one, since `K` is monic).  Their
vanishing forces `R=0`, hence `K|N^2`.  Conversely, if `K|N^2` then
`N^2/K` is polynomial, the negative part in (1.1) is zero, and every `q_l`
vanishes.  Only four rows are needed for this equivalence; seven are
available.

## 3. UFD/root-multiplicity classification

Over an algebraic closure factor

```text
K=prod_a (z-a)^(m_a),
D_K=prod_a (z-a)^ceil(m_a/2).                         (3.1)
```

UFD valuations give the exact equivalence

```text
K|N^2       iff       D_K|N.                          (3.2)
```

Because `deg K=4` and `deg N<=3`, the squarefree kernel of `K` has even
degree `0`, `2`, or `4`.  Degree four forces `deg D_K=4` and hence `N=0`.
After removing the zero normal/load section on `k10=0`, only the following
two closures remain.

### 3.1 Square closure

Depression forces a monic square quartic to be

```text
K=(z^2+s)^2,
N=(z^2+s)(alpha z+beta).                              (3.3)
```

Equivalently, in the first-normal variables,

```text
c=0,
p^2=4r,
2n1=p n3,
2n0=p n2.                                             (3.4)
```

On the `k10=0` slice this has dimension three.  In the full first gate the
same formulas solve every row for arbitrary `k10`, because both
`N^2/K=(alpha z+beta)^2` and `K^(5/2)=(z^2+s)^5` are polynomials.  Thus
(3.4) supplies an exact dimension-four square/load family inside `V(Q1)`.

### 3.2 Nonsquare discriminant closure

When the squarefree kernel has degree two, write canonically
`K=L^2 S` with `L` monic linear and `S` monic squarefree quadratic; `L`
and `S` may share a root on the `[3,1]` stratum.  Depression gives

```text
L=z-a,
S=z^2+2az+d,
K=(z-a)^2(z^2+2az+d),
N=lambda (z-a)(z^2+2az+d).                            (3.5)
```

This covers root partitions `[2,1,1]` and `[3,1]`, and its closure meets the
square locus when `S` specializes to a square.  It has dimension three in
`(p,c,r,n0,...,n3,k10)` after imposing `k10=0`.  The explicit coordinates
are

```text
p=d-3a^2,
c=2a(a^2-d),
r=a^2 d,
n3=lambda,
n2=a lambda,
n1=(d-2a^2)lambda,
n0=-a d lambda,
k10=0.                                                (3.6)
```

The squarefree partition `[1,1,1,1]` forces `N=0` and is absent from the
nonzero first-contact slice.

## 4. Saturation and exact scope

The conclusions above classify geometric points/reduced support on the
`k10=0` slice.  They do not prove an equality of nonreduced ideals, exclude
embedded components, or compute scheme multiplicities.  Under the reviewed
saturations:

- `(p,c,r)^infinity` removes components supported wholly at the
  weighted-projective origin.  The relevant source open excludes `s=0` in
  (3.3) and `(a,d)=(0,0)` in (3.5), although those boundary points can remain
  in the affine closure of a retained saturated component.
- `(n0,n1,n2,n3,k10)^infinity`, restricted to `k10=0`, removes components
  supported wholly on `N=0`.  The relevant first-contact open has
  `(alpha,beta)!=(0,0)` in (3.3) and `lambda!=0` in (3.5), while their affine
  closures can retain the zero-normal boundary.
- the removed zero section is the higher-contact stratum of the full divided
  Rees family and remains mathematically live; its removal here is only the
  definition of contact order one.

The exact theorem is therefore:

```text
support_red(V(Q1*) intersect V(k10))
```

is exactly the union of the square closure (3.3) and discriminant closure
(3.5): both have points in both saturation opens, so neither closure is
deleted, while every point on the `k10=0` slice satisfies (2.1).  The source-
relevant locus is their intersection with the two opens just described.  This
is a reduced-support statement, not a statement that the full `Q1*` scheme
is reduced.

## 5. What is and is not known for `k10!=0`

The square/load family (3.3)--(3.4) is an exact solution for arbitrary
nonzero `k10`.  The present hand theorem does **not** yet exclude cancellation
of the first seven coefficients in (1.1) at a nonsquare `K` with
`k10!=0`; doing so is a finite Padé/ideal lemma, not a consequence of the
full-negative-part UFD argument.

As navigation only, two frozen primes independently gave exactly two minimal
components for `Q1*`, with dimensions `3` and `4`.  This is the signature
predicted by the `k10=0` discriminant closure and the arbitrary-`k10` square
closure.  The modular bases/signatures are being printed independently.
Until an exact characteristic-zero certificate or a hostile-reviewed Padé
proof lands, this does not establish that those two closures exhaust the full
scheme or even its characteristic-zero radical.

## 6. Next exact gate

The next producer should:

1. prove the Padé lemma `k10!=0 => K is square`, or give the smallest
   nonsquare counterexample;
2. compare the exact characteristic-zero radical with the two explicit
   prime closures, separately from nilpotents/embedded structure;
3. substitute (3.3) and (3.5) into the next divided `Lambda` coefficient
   before any new monolithic Rees saturation.

This theorem does not prove a strict arc, impose the terminal `[6,2]`
passport or either Taylor boundary, exclude order two, close `(8,12)`, prove
maximum twelve, or prove JC2.
