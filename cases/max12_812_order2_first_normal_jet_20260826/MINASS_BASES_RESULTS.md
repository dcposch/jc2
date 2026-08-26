# Dual-prime minimal-component bases for `Q1*`

Date: 2026-08-26

Status: **AWS MODULAR NAVIGATION; NOT A CHARACTERISTIC-ZERO RADICAL OR
SCHEME-THEORETIC DECOMPOSITION.**

## 1. Custody and endpoint

The frozen basis-print adapter was run independently on two registered AWS
hosts.  Both lanes ended with engine rc `0` and validator
`PASS_NAVIGATION_ONLY`.

| prime | host | tag | stdout SHA-256 |
|---:|---|---|---|
| `32003` | Box03 / `ip-172-30-0-249` | `max12_812_order2_first_normal_minass_p32003_20260826T044600Z_box03` | `c3b7f18cfc2f19e1e9477b131bd81d0ea585d457eeaffed647328373c226f94a` |
| `65521` | r6d / `ip-172-30-0-45` | `max12_812_order2_first_normal_minass_p65521_20260826T044600Z_r6d` | `8d642cfa93e9b4358ee30525042f7ddbd33a08335e1d3d19781ce9f1564e2744` |

Each lane prints exactly two minimal components.  The component match is
unambiguous from dimension, basis size, membership of `k10`, and containment
of the square-family ideal:

| component | dimension | basis size | `k10` reduces to zero | contains square ideal |
|---|---:|---:|---:|---:|
| nonsquare/discriminant candidate | `3` | `24` | `1` | `0` |
| square/load candidate | `4` | `10` | `0` | `1` |

These four signatures agree at both primes.  The bases also have identical
ordered monomial supports.  Their coefficients are reductions of the same
small rational coefficients displayed below; this is a comparison of the
two printed modular outputs, not a characteristic-zero lifting theorem.

## 2. Common rational display: dimension-three component

The following 24-polynomial list reduces coefficientwise to component 1 at
both primes (fractions are legitimate because both primes are odd):

```text
k10,
p*n2+(3/2)*c*n3-2*n0,
r*n3^2+n0*n2,
c*n3^2+n1*n2-n0*n3,
p*n3^2+n2^2-n1*n3,
p*n1*n3-c*n2*n3-n1^2+n0*n2,
c*n0*n3-r*n1*n3-n0^2,
p*n0*n3-r*n2*n3-n0*n1,
p*r*n3+(1/2)*c*n0-2*r*n1,
p*c*n3+p*n0-(3/2)*c*n1-2*r*n2,
p^2*n3-p*n1-(3/2)*c*n2-2*r*n3,
n2^3+(1/2)*n1*n2*n3+(1/2)*n0*n3^2,
r*n2^2+(1/2)*r*n1*n3-(1/2)*n0^2,
c*n2^2+(1/2)*c*n1*n3+r*n2*n3-n0*n1,
c*n0*n2-r*n1*n2+r*n0*n3,
p*n0^2-c*n0*n1+r*n1^2-r*n0*n2,
c^2*n0-2*p*r*n0-c*r*n1+4*r^2*n2,
p*c*n0-2*p*r*n1+3*c*r*n2+4*r^2*n3,
p^2*n0-(1/2)*p*c*n1+(3/2)*c^2*n2+5*c*r*n3-4*r*n0,
r^2*n2*n3+(1/2)*c*n0^2-r*n0*n1,
c*r*n2*n3+(1/2)*c*n0*n1-r*n1^2-r*n0*n2,
c^2*n2*n3+p*n0*n1-(1/2)*c*n1^2-3*r*n1*n2+r*n0*n3,
p*c^2*n1-4*p^2*r*n1-3*c^3*n2-19*c^2*r*n3+16*c*r*n0+16*r^2*n1,
p^3*c^2-4*p^4*r+(27/4)*c^4-36*p*c^2*r+32*p^2*r^2-64*r^3
```

This is the modular signature predicted by the exact `k10=0`
discriminant parameterization

```text
p=d-3*a^2,                 c=2*a*(a^2-d),
r=a^2*d,                   n3=lambda,
n2=a*lambda,               n1=(d-2*a^2)*lambda,
n0=-a*d*lambda,            k10=0.
```

The two modular bases do not by themselves prove that the displayed
rational list is the characteristic-zero kernel of that parameterization,
nor that the corresponding scheme is reduced.

## 3. Common exact display: dimension-four square/load component

Component 2 is byte-identical as a polynomial list at both primes:

```text
c,
p*n3-2*n1,
n1*n2-n0*n3,
p*n2-2*n0,
p*n1-2*r*n3,
p*n0-2*r*n2,
p^2-4*r,
r*n3^2-n1^2,
r*n2*n3-n0*n1,
r*n2^2-n0^2
```

It is the closure of

```text
K=(z^2+s)^2,
N=(z^2+s)*(alpha*z+beta),
k10 arbitrary.
```

The hand principal-part theorem proves directly that this family lies in
`V(Q1*)`.  The modular computation says that it is a minimal component at
each tested prime; it does not prove that the characteristic-zero ideal is
prime or that no embedded structure is present.

## 4. Exact scope split

The current exact theorem and the modular evidence must be kept distinct:

1. On `k10=0`, after the declared nonzero saturations, the exact
   principal-part/UFD argument proves the **reduced support** is the union of
   the square closure and the nonsquare discriminant closure.
2. For arbitrary `k10`, the square/load closure is an exact family of
   solutions.
3. For `k10!=0` away from the square closure, the two-prime calculation is
   only evidence that no additional minimal support occurs.  Excluding such
   support in characteristic zero is still the Padé lemma
   `k10!=0 => K square` (or an exact radical comparison).
4. Nothing here proves equality of nonreduced ideals, absence of embedded
   components, the existence of a strict Rees arc, or any higher divided
   jet condition.

The benign Singular `redefining Pai/kzero/sqsig` loop diagnostics are
preserved in the raw streams.  Both validation files record engine rc `0`;
there is no `?` diagnostic or failure sentinel.
