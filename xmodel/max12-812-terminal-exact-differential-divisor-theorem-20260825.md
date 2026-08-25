# `(8,12)` terminal exact-differential and divisor-profile theorem

Date: 2026-08-25  
Status: **PRODUCER THEOREM; FROZEN FOR HOSTILE REVIEW**

## Theorem

Let `L` be a characteristic-zero field enlarged harmlessly to contain the
needed roots of unity.  Consider a nontrivial Kummer client of the reviewed
partial-`y` `(8,12)` high-row reduction.  Normalize the monic leading core
as

```text
h in L[x],       deg h=H=4U,       u^4=h,
```

and let the class of `h` in `L(x)^*/L(x)^{*4}` have order `e=4` or `e=2`.
Let `j in L^*` be the constant Jacobian.  The terminal Faber identity is

```text
8 r_7'=j/u.                                           (0.1)
```

Then the following statements hold.

1. **Exact base ODEs.**

   - If `e=4`, there is a unique `A in L(x)` with `r_7=u^3 A`, and (0.1)
     is equivalent to

     ```text
     8h A'+6h'A=j.                                    (0.2)
     ```

   - If `e=2`, write uniquely up to the harmless sign
     `h=v^2`, with `v in L[x]` monic and not a square, and choose `u^2=v`.
     There is a unique `A in L(x)` with `r_7=uA`, and (0.1) is equivalent
     to

     ```text
     8v A'+4v'A=j.                                    (0.3)
     ```

   Thus a terminal trajectory exists in the Kummer function field if and
   only if the corresponding rational first-order ODE has a solution.

2. **Infinity.**  Every place above `x=infinity` is unramified.  With
   `q=1/x` and `t=q^Uu`, one has

   ```text
   dx/u=-q^(U-2)t^-1 dq.                              (0.4)
   ```

   Hence `U=1` gives a nonzero logarithmic residue and is impossible.
   For `U>=2`, `dx/u` is regular at infinity.

3. **Finite roots, order four.**  If `a` is a root of `h` of multiplicity
   `k`, put `g=gcd(4,k)`.  At every normalized place above `a`,

   ```text
   ord(dx/u)=(4-k)/g-1.                               (0.5)
   ```

   Multiplicity `k=4` gives a simple pole with nonzero residue and is
   impossible.  If `U>=2`, exactness forces at least one finite root of
   multiplicity `k>=5`.  In particular, a profile all of whose
   multiplicities are at most three is impossible.

4. **Finite roots, order two.**  If `a` is a root of `v` of multiplicity
   `k`, put `g=gcd(2,k)`; its multiplicity in `h` is `2k`.  Then

   ```text
   ord(dx/u)=(2-k)/g-1.                               (0.6)
   ```

   A double root of `v` (multiplicity four in `h`) gives a simple pole
   with nonzero residue and is impossible.  If `U>=2`, exactness forces a
   root of `v` of multiplicity at least three, equivalently a root of `h`
   of multiplicity at least six.

5. **The first surviving order-two degree.**  At `U=2` (`H=8`), the only
   order-two divisor partition compatible with the preceding necessary
   conditions is

   ```text
   mult(v)=[3,1],       mult(h)=[6,2].                 (0.7)
   ```

   It is not merely necessary: its terminal differential is exact.  For
   distinct `a,b in L`, take

   ```text
   v=(x-a)^3(x-b),       h=(x-a)^6(x-b)^2,
   u^2=v,                 T=u/(x-a)^2.
   ```

   Then

   ```text
   T^2=(x-b)/(x-a),
   dx/u=(2/(b-a)) dT,
   r_7=(j/(4(b-a)))T
       =j u/(4(b-a)(x-a)^2).                          (0.8)
   ```

   The two finite branch points of the normalized quadratic cover are
   exactly `a` and `b`.  At `a`, `dx/u` has a double pole and zero residue;
   at `b` it is regular; it is regular at both points above infinity.

Statement (0.8) proves only the terminal equation for the unique first
order-two source profile.  It does not produce the other coefficient
functions, solve the seven tail equations, or establish Taylor
polynomiality.

## 1. Charged inputs and character of the terminal tail

This theorem consumes only:

```text
30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07  xmodel/max12-partial-y-kummer-preflight-20260824.md
e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c  xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md
```

The reviewed Faber theorem gives (0.1).  If the Kummer generator sends
`u->zeta u`, then the depressed coordinate and inverse root transform as
`z->zeta z` and `w->zeta w`.  In

```text
H_F(w)-g(z(w))=sum_(ell>=1) r_ell w^-ell,
```

each summand is invariant, so `r_ell->zeta^ell r_ell`.  Since `e` divides
eight,

```text
zeta^7=zeta^-1.                                       (1.1)
```

Thus `r_7` lies in the inverse-character eigenspace.  In a degree-four
Kummer field the basis `1,u,u^2,u^3` identifies that eigenspace with
`u^3L(x)`.  In the genuine quadratic field the basis `1,u` identifies it
with `uL(x)`.  The monic-core normalization ensures that the constant
field is the scalar field, so no hidden character-valued integration
constant occurs.  This proves the asserted unique forms of `r_7`.

## 2. Derivation of the base ODEs with exact constants

For `e=4`, logarithmic differentiation of `u^4=h` gives

```text
u'/u=h'/(4h).
```

Writing `r_7=u^3A`, one obtains

```text
r_7'=u^3(A'+3h'A/(4h)),
j/(8u)=j u^3/(8h).
```

After division by `u^3` and multiplication by `8h`, equation (0.1) is
exactly (0.2).

For `e=2`, write `u^2=v`; then `u'/u=v'/(2v)`.  With `r_7=uA`,

```text
r_7'=u(A'+v'A/(2v)),
j/(8u)=j u/(8v).
```

Division by `u` and multiplication by `8v` gives exactly (0.3).  Both
implications reverse, proving equivalence rather than only necessity.

The rational solution is unique on each nontrivial class.  A difference of
two solutions of (0.2) is `C h^(-3/4)`; if this were a nonzero rational
function, then `h^3` would be a fourth power and coprimality of three and
four would make `h` a fourth power, contradicting `e=4`.  A difference of
two solutions of (0.3) is `C v^(-1/2)`, rational only if `v` is a square,
contradicting `e=2`.  This also excludes an uncharged inverse-character
integration constant.

## 3. Local normalization at infinity

Because `h` is monic of degree `4U`, write

```text
h(q^-1)=q^-4U eta(q),       eta(0)=1.
```

For `e=4`, `t=q^Uu` satisfies `t^4=eta(q)`.  Hensel's lemma and separability
of `T^4-1` show that the selected local branches are unramified and that
`q` is their uniformizer.  For `e=2`, `v` is monic of degree `2U`, and the
same argument uses `t^2=q^(2U)v(q^-1)`.  On either client,

```text
dx=-q^-2dq,       u=q^-Ut,
```

which proves (0.4).  At `U=1` the residue is `-t(0)^-1`, nonzero on every
sheet.  A rational exact differential has zero residue at each individual
place, so no cancellation between sheets is possible.  At `U>=2` the
display has nonnegative order.

## 4. Local normalization at finite roots

### Order four

Let

```text
h=(x-a)^k c(x),       c(a)!=0,       g=gcd(4,k),
E=4/g.
```

At any place of the normalization above `a`, choose a uniformizer `tau`
so that

```text
x-a=tau^E,       u=tau^(k/g) epsilon(tau),
epsilon(0)!=0.
```

Therefore

```text
dx/u=E epsilon(tau)^-1
     tau^(E-1-k/g)d tau,
```

and `E-1-k/g=(4-k)/g-1`, proving (0.5).  At `k=4`, `E=1` and the residue
is `epsilon(0)^-1`, nonzero.  For `k<=3`, the respective orders are
`2,0,0`; for `k>=5` they are at most `-2`.

If `U>=2` and every finite multiplicity is at most three, (0.4)--(0.5)
make `dx/u` a nonzero global holomorphic differential on the smooth
projective normalization.  If it were `dR`, then `R` could have no pole
(the derivative of a rational function with a pole has a pole), hence `R`
would be a global regular function and therefore constant.  This would
make `dR=0`, a contradiction.  So some multiplicity is at least four;
the nonzero residue excludes equality four, proving the `k>=5` claim.

### Order two

Let `v=(x-a)^k c(x)` with `c(a)!=0`, put `g=gcd(2,k)`, and use

```text
x-a=tau^(2/g),       u=tau^(k/g)epsilon(tau).
```

The identical calculation gives (0.6).  At `k=1` the order is zero; at
`k=2` it is `-1` with nonzero residue; at `k>=3` it is at most `-2`.
If all roots of `v` are simple, (0.4) and (0.6) make `dx/u` holomorphic
for `U>=2`, contradicting exactness as above.  A multiple root is needed,
the double-root case is forbidden by its residue, and therefore some root
has multiplicity at least three.

At poles of order at least two, vanishing of the residue is still required
but is not automatic from the order formula.  Even zero residues are only
local necessary conditions: the global rational ODE (0.2) or (0.3) is the
exact test.

## 5. Classification and exact primitive at `U=2,e=2`

Here `deg v=2U=4`.  Exactness requires a root of multiplicity at least
three and prohibits multiplicity two.  The only partitions of four with a
part at least three are `[4]` and `[3,1]`.  The `[4]` polynomial is a square
over the algebraically closed constant extension and makes the Kummer
class trivial, contrary to `e=2`.  Hence `[3,1]` is the unique order-two
profile.

For distinct roots `a,b`, monicity gives

```text
v=(x-a)^3(x-b).
```

With `T=u/(x-a)^2`, direct division by `u^2=v` gives the first identity in
(0.8).  Differentiating it gives

```text
2T T'=(b-a)/(x-a)^2,
1/u=1/((x-a)^2T)=(2/(b-a))T',
```

which proves the remaining identities and the exact constant in `r_7`.

For completeness, the normalized quadratic cover can be written

```text
Y=u/(x-a),       Y^2=(x-a)(x-b).
```

Its finite branch points are `a` and `b`.  At `a`, take `x-a=tau^2`; then
`ord_tau(u)=3` and `ord_tau(dx/u)=-2`.  The explicit primitive `T` has a
simple pole, so its derivative has no residue.  At `b`,
`ord_tau(u)=1` and `ord_tau(dx/u)=0`.  Since `U=2`, (0.4) has order zero at
both unramified points above infinity.  This checks every place directly.

An affine source change sends `(a,b)` to `(0,1)` (with the reciprocal
linear scaling in `y` if determinant one is desired).  The canonical
profile for a concrete compiler is therefore

```text
h=x^6(x-1)^2,       v=x^3(x-1),       u^2=v,
T=u/x^2,            r_7=(j/4)T.                       (5.1)
```

## Prioritized consequence

The first source-typed order-two coefficient-infinity Rees client should
use (5.1), not the degree-four preflight control
`h=x^2(x-1)^2`, which the infinity residue excludes.  It must retain the
reviewed order-two Faber loads `k_10,k_6,k_2`, the constant tail loads
`mu_2,mu_4,mu_6`, and both finite Taylor boundaries.  The common-quartic
special fibre remains only a reduced-support gate until an exact
saturation is computed.

## Scope firewall

This theorem is an exact terminal necessary condition and a complete
classification of the first `U=2,e=2` divisor profile.  Equation (0.8)
shows that this profile passes the terminal equation; it does not show that
the other six tail equations, coefficient rationality, polynomial Taylor
boundaries, or the Keller pair exist.  The theorem does not close the
order-two client, the order-four client, `(8,12)`, maximum twelve, or JC2.
