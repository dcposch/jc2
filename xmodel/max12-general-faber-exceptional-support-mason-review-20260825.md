# Independent review — general Faber exceptional-support theorem

Date: 2026-08-25  
Target:

```text
7d5271e8caf6d6d071819e8b2a670ac79d2063882a90d4916060b3e4deb95919  xmodel/max12-general-faber-exceptional-support-mason-20260825.md
```

Verdict: **CONFIRMED**.

The statement implicitly uses the standard positive Faber index `n>=1`.
Writing that inequality explicitly would improve wording but is not a
mathematical repair: a monic degree-`n` Faber polynomial already carries
that convention in this client.

## Independent reconstruction

Let `d=(m,n)`, `a=m/d`, `b=n/d`, and `N=an=bm`.  Depression gives
`w=f^(1/m)=z+O(z^-1)` and hence `z(w)=w+O(w^-1)`.  With

```text
g(z(w))=w^n-T,       T=O(w^-m),
```

one has

```text
g^a-f^b
 =sum_(j=1)^a binom(a,j)w^(n(a-j))(-T)^j.
```

The `j`th term has exponent at most

```text
n(a-j)-jm=N-j(n+m),
```

strictly decreasing with `j`.  A nonzero polynomial retains its degree and
leading coefficient after `z=z(w)`.  Therefore

```text
deg(g^a-f^b)<=N-m-n.                                  (1)
```

If the right side is negative, the polynomial is zero.  This explicitly
covers both divisibility directions:

- `a=1` (`m|n`) gives bound `-m`; in fact `F_n(f)=f^b` for every `f`.
- `b=1` (`n|m`) gives bound `-n`; under the stated tail vanishing this
  forces `F_n(f)^a=f`.

Suppose next that `W=g^a-f^b` is nonzero and the bound
`D=N-m-n` is nonnegative.  For the monic gcd `D_0=(g^a,f^b)` of degree `e`,
divisibility `D_0|W` gives

```text
0<=e<=deg W<=D<N.
```

After dividing the equation by `D_0`, its three terms are pairwise coprime,
the two power terms have degree `N-e`, their radicals have roots only among
those of `f g`, and the third term has degree at most `D-e`.  Thus
Mason--Stothers gives the impossible chain

```text
N-e <= deg rad(A B C)-1
    <= m+n+D-e-1
     = N-e-1.
```

The count does not assume that `f` or `g` is squarefree.  A nonzero constant
`W` has `e=0` and contributes no radical roots, so it is included.  The edge
`e=N` is excluded already by `e<=D<N`; independently, it would make the two
monic degree-`N` powers equal.  Hence `W=0` in every case.

Since `(a,b)=1`, unique factorization in `L[z]` gives a monic `K in L[z]`
with `f=K^a,g=K^b` and `deg K=d`.  No algebraic closure is needed for this
step.  The missing `z^(m-1)` coefficient is `a` times the `z^(d-1)`
coefficient of `K`, so `K` is depressed in characteristic zero.

Conversely `f=K^a` makes `f^(n/m)=K^b` polynomial, so its Faber polynomial
is `K^b` and every tail vanishes.  Over an algebraic closure this proves
equality of the geometric zero set of the first `m-1` tails with the power
locus.  Faithfully flat contraction returns the same radical equality over
`L`; no claim that the original tail ideal is reduced is used.

Finally, the coefficient of `z^(m-d+j)` in `K^a` is `a c_j` plus a
polynomial in the higher coefficients of `K`.  This triangular recovery
makes the power image closed and isomorphic to `A^(d-1)`, so its ideal is
prime.  Under the Faber scaling, `c_j` has weight `d-j`; after depression
the weights are exactly `2,3,...,d`.  Hence the reduced projectivization is
`P(2,3,...,d)`.  For `d=1` there are no positive-degree parameters, the
affine locus is only the irrelevant origin, and `Proj` is empty.

## Client and firewall audit

The substitutions are correct:

```text
(m,n)=(9,12): d=3,a=3,b=4, N-m-n=15, first 8 tails,
(m,n)=(8,12): d=4,a=2,b=3, N-m-n=4,  first 7 tails.
```

Thus the respective reduced exceptional supports are the common cubic and
common quartic loci once a charged client proves that lower Faber terms and
loads vanish in its exceptional Rees fibre and that its descended rows are
the ordinary first tails.  The producer states this condition and does not
promote reduced support to scheme reducedness, deformation exclusion,
rationality, Taylor polynomiality, a passport closure, or JC2.
