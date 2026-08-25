# General Faber exceptional-support theorem

Date: 2026-08-25  
Status: **PRODUCER THEOREM (REDUCED SUPPORT ONLY)**

## Statement

Let `L` be a characteristic-zero field.  Let

```text
f(z)=z^m+sum_(i=0)^(m-2) B_i z^i,       m>=2,
w=f(z)^(1/m)=z+O(z^-1),
```

and let `g=F_n(f)` be the monic degree-`n` Faber polynomial characterized by

```text
g(z(w))=w^n-T(w),       T(w)=sum_(ell>=1) r_ell w^-ell.
```

Put

```text
d=gcd(m,n),       a=m/d,       b=n/d,       N=lcm(m,n)=an=bm.
```

If

```text
r_1=...=r_(m-1)=0,                                      (1)
```

then there is a unique monic depressed polynomial `K` of degree `d` such
that

```text
f=K^a,       g=K^b.                                     (2)
```

Conversely, (2) makes every Faber tail vanish.  Consequently the reduced
zero scheme of the first `m-1` tails in the affine coefficient space of
depressed monic degree-`m` polynomials is exactly the common-`d`th-root
locus.  This locus is a closed prime copy of `A_L^(d-1)`.  For `d>=2`, its
weighted-projective reduction is

```text
P(2,3,...,d),
```

with coordinates the coefficients of a depressed monic degree-`d`
polynomial.  For `d=1`, the affine locus is only the irrelevant origin, so
its projectivization is empty.

## 1. Spectral degree bound

Define

```text
W=g^a-f^b.
```

In the `w` coordinate, condition (1) is `T=O(w^-m)`, and hence

```text
W(z(w))
 = (w^n-T)^a-w^N
 = sum_(j=1)^a binom(a,j) w^(n(a-j))(-T)^j.             (3)
```

The `j`th summand is `O(w^(N-j(n+m)))`.  Thus the largest possible
exponent occurs at `j=1`, and

```text
deg_z W <= D:=N-m-n                                      (4)
```

whenever `W` is nonzero.  Indeed, substitution
`z(w)=w+O(w^-1)` preserves the degree and leading coefficient of every
nonzero polynomial in `z`.  If `D<0`, (3) therefore already forces `W=0`.
This includes the divisibility edge `a=1`, where (3) is simply `W=-T` and
`D=-m`.

## 2. Mason--Stothers forces `W=0`

It remains to treat `D>=0`.  Suppose that `W` is nonzero, and set

```text
D_0=gcd(g^a,f^b),       e=deg D_0.
```

Since `D_0` divides `W`, (4) gives `0<=e<=deg W<=D`.  In particular
`e<N`.  Put

```text
A=g^a/D_0,       B=-f^b/D_0,       C=-W/D_0.
```

Then `A+B+C=0`, the three polynomials are pairwise coprime,

```text
deg A=deg B=N-e,       deg C<=D-e,
```

and the roots of `A B` are among the roots of `f g`.  Mason--Stothers gives

```text
N-e
 <= deg rad(A B C)-1
 <= (m+n)+(D-e)-1
 = N-e-1,
```

a contradiction.  A nonzero constant `W` is covered: then `e=0` and the
constant factor `C` contributes no roots.  The apparent edge `e=N` is
impossible under `e<=D=N-m-n<N`; directly, a monic degree-`N` common
divisor of the two monic degree-`N` powers would also give `W=0`.
Therefore `W=0` in every case.

## 3. UFD and the reduced scheme

The equality `g^a=f^b` in the UFD `L[z]`, together with `gcd(a,b)=1`,
forces the exponent of each irreducible factor of `f` to be divisible by
`a` and that of `g` to be divisible by `b`.  Monicity removes the unit
ambiguity, so a unique monic degree-`d` polynomial `K` satisfies (2).
Writing

```text
K=z^d+c_(d-1)z^(d-1)+...+c_0,
```

the absent `z^(m-1)` coefficient of `f=K^a` is `a c_(d-1)`.  Characteristic
zero therefore makes `K` depressed.

Conversely, if `f=K^a`, then `f^(n/m)=K^b` is already a polynomial.  Its
Faber polynomial is `g=K^b` and all tails vanish.

The power locus is closed and prime.  More explicitly, in descending
coefficient order the coefficient of `z^(m-d+j)` in `K^a` is `a c_j` plus
a polynomial in the already recovered `c_(j+1),...,c_(d-2)`.  Since `a` is
invertible in `L`, these equations give a triangular polynomial inverse to
the power parametrization.  The locus is therefore isomorphic to
`A_L^(d-1)`.  Equality of geometric zero sets over an algebraic closure,
followed by contraction, proves that the radical of `(r_1,...,r_(m-1))` is
the prime ideal of this locus.  The parameter `c_j` has weight `d-j`, which
gives the stated projective space and the `d=1` edge.

## 4. Exact maximum-twelve clients

- For `(m,n)=(9,12)`, `(d,a,b)=(3,3,4)`.  The first eight unloaded tails
  therefore have reduced support
  `f=K^3, g=K^4`, with `K=z^3+pz+c`; projectively this is `P(2,3)`.
- For `(m,n)=(8,12)`, `(d,a,b)=(4,2,3)`.  The first seven unloaded tails
  therefore have reduced support
  `f=K^2, g=K^3`, with depressed monic quartic `K`; projectively this is
  `P(2,3,4)`.

In a weighted Rees client containing lower Faber terms or nonzero target
loads, this theorem applies to the exceptional fibre only after the charged
source proves that those terms acquire positive Rees weight and vanish, and
that the descended exceptional rows are the ordinary first `m-1` tails.

## Firewall

This is a reduced-support theorem.  It does not prove that the tail ideal is
reduced, determine its embedded or nilpotent structure, give a formal
lifting or exclusion theorem, bound contact order, turn an algebraic arc
into a rational constant-field section, establish Taylor polynomiality, or
close any passport or JC2.
