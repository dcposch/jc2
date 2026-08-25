# Max12 `(9,12)` selected-Q8 infinity-contact passport gate

Date: 2026-08-24  
Status: **producer-exact successor from reviewed parents; hostile review required**

## 1. Statement and strict scope

Let `C_Q8` be the irreducible algebraic quotient component selected by one
of the eight corrected-Q8 smooth non-parity formal branches, and let
`q_Q8` be its point on the projective normalization.  Assume an actual
loaded order-three trajectory has nonconstant quotient image in `C_Q8`.
Then:

1. the trajectory meets `q_Q8` only at `x=infinity`;
2. in the reviewed balanced terminal passport,
   `e_pass=ord_infinity(T-lambda)` is a positive even integer;
3. for `T=A_T/B_T`, the coprime triple
   `A_T, -lambda*B_T, C_T=A_T-lambda*B_T` is Mason-sharp:

   ```text
   deg rad(A_T*B_T*C_T)=D+1,
   max(deg A_T,deg B_T,deg C_T)=D;                    (1.1)
   ```

4. evenness does not exclude the terminal/Kummer system: the exact
   `e_pass=2` noncube control in Section 6 satisfies the original row
   `9*r8'=j/u`, not merely its ninth-power consequence.

Here `e_pass` is the passport contact index; the Kummer order remains three.
The result is conditional on the trajectory's global image lying on the
component selected by the Q8 formal branch.  It neither proves that such a
global component carries a trajectory nor realizes a passport in the
original coefficient fibre.

## 2. Reviewed inputs versus new deductions

The inputs consumed at reviewed tier are:

- the corrected Q8 formal branch is a reduced smooth branch of the genuine
  seven-row fibre;
- on an actual trajectory on it, the original terminal row forbids contact
  with its Q8 node at every finite `x`-place;
- the Kummer-fixed local quotient has

  ```text
  theta=a0^2/p^9,
  S=r8^9=S0+S1*theta+O(theta^2),       S0*S1!=0,
  Z=S/nu^10;                                             (2.1)
  ```

- the global quotient has the necessary terminal identity

  ```text
  nu^10*h^3*(Z')^9=j^9*Z^8;                            (2.2)
  ```

- after explicitly adding `Z!=0`, the reviewed terminal classification gives
  `Z=T^3`, `h=C*T^2/(T')^3`, balanced degrees
  `deg A_T=deg B_T=D`, and passport

  ```text
  (alpha_i) over 0,    (beta_j) over infinity,
  (e_pass,1^(D-e_pass)) over lambda=T(infinity),
  r+s=e_pass+1,        deg(h)=3*(e_pass+1).             (2.3)
  ```

The `Z!=0` erratum is not left implicit here.  Along an actual trajectory,
`9*r8'=j/u` with `j!=0` makes `r8` nonconstant; hence
`S=r8^9` and `Z=S/nu^10` are nonzero and nonconstant in characteristic zero.

The new deductions in this report are the projective-surjectivity contact
argument, parity of `e_pass`, Mason equality, and the general
terminal/Kummer converse plus its `e_pass=2` control.  They remain
producer-tier pending a new hostile review.

## 3. Surjectivity forces the Q8 contact to `x=infinity`

All Kummer-fixed quotient coordinates of an actual trajectory lie in
`K=C(x)`, so they define a rational map

```text
phi:P1_x --> overline(C_Q8).                            (3.1)
```

After passing to the projective normalization, (3.1) extends across every
source point.  It is nonconstant because `Z` is nonconstant.  A nonconstant
morphism between complete irreducible curves is surjective, so `q_Q8` has a
preimage.

If a preimage lay at finite `x`, then after the harmless finite Kummer lift
the actual trajectory would meet the Q8 node at a finite place.  The reviewed
normalization theorem excludes this, including ramified and fractional
valuation lifts.  Therefore

```text
phi^(-1)(q_Q8)={infinity_x} set-theoretically.          (3.2)
```

This argument is deliberately conditional on `C_Q8` being the trajectory's
global image component.  As a useful future discriminator, if exact global
component grouping puts two distinct corrected-Q8 points on the same
normalization, (3.2) would exclude that component: the single source point
`infinity_x` cannot map to two distinct target points.

## 4. The passport contact index is even

At the Q8 node, `pi=p^9` and `S0` are units.  From (2.1), with
`Z0=S0/nu^10`,

```text
Z-Z0=unit*theta+O(theta^2),
theta=a0^2/pi.                                          (4.1)
```

Let `a=ord_infinity(a0)>0`; positivity follows from (3.2).  Since `pi` is a
local unit, (4.1) gives

```text
ord_infinity(Z-Z0)=2a.                                  (4.2)
```

Write `Z=T^3` and `lambda=T(infinity)`.  The unit `Z0=lambda^3` is nonzero,
so

```text
Z-Z0=(T-lambda)*(T^2+lambda*T+lambda^2),                (4.3)
```

and the second factor specializes to `3*lambda^2!=0`.  Thus

```text
e_pass=ord_infinity(T-lambda)=2a.                       (4.4)
```

In particular `e_pass` is even, `e_pass>=2`, and

```text
deg(h)=3*(e_pass+1) == 3 mod 6.                         (4.5)
```

This removes all odd-contact terminal passports from the selected-Q8
trajectory scope.  It is not an exclusion, because even passports survive
the terminal subsystem.

## 5. Every remaining passport is Mason-sharp

Set

```text
C_T=A_T-lambda*B_T.                                     (5.1)
```

Because `deg A_T=deg B_T=D` and
`e_pass=ord_infinity(T-lambda)`, leading cancellation gives

```text
deg(C_T)=D-e_pass.                                      (5.2)
```

The three polynomials `A_T,B_T,C_T` are pairwise coprime.  Moreover `C_T`
is squarefree: a multiple finite root of `C_T` would be a critical point of
`T` away from `A_T*B_T`, contradicting the reviewed polynomiality condition
that every finite Wronskian root lies in `supp(A_T*B_T)`.  Equivalently, the
finite part of the lambda-fibre in (2.3) is `1^(D-e_pass)`.

Let `r` and `s` be the numbers of distinct roots of `A_T` and `B_T`.
Using `r+s=e_pass+1`,

```text
deg rad(A_T*B_T*C_T)
  =r+s+(D-e_pass)
  =(e_pass+1)+(D-e_pass)
  =D+1.                                                 (5.3)
```

For the coprime equation

```text
A_T+(-lambda*B_T)=C_T,                                  (5.4)
```

Mason--Stothers says `D<=deg(rad)-1`; (5.3) is equality.  Thus plain
polynomial abc cannot eliminate any of these passports.  The equality is a
classification signal, not evidence of coefficient-fibre realization.

## 6. Exact `e_pass=2` noncube positive control

Take

```text
T=(x^2+1)/x^2,       A_T=x^2+1,       B_T=x^2,
lambda=1,            D=2,             e_pass=2.         (6.1)
```

Then

```text
W=A_T'*B_T-A_T*B_T'=-2x,
h=T^2/(T')^3=-x^5*(x^2+1)^2/8,
Z=T^3.                                                   (6.2)
```

The marked passport is

```text
over 0: (1,1),       over infinity: (2),       over 1: (2),
```

and `deg(h)=9`.  The finite zero multiplicities of `h` are `(5,2,2)`, so
`h` is not a cube; `3|deg(h)` holds.  Also `C_T=A_T-B_T=1` and

```text
deg rad(A_T*B_T*C_T)=3=D+1.                            (6.3)
```

This already satisfies (2.2) with `nu=1`, `j=3`:

```text
h^3*(Z')^9=3^9*Z^8.                                    (6.4)
```

It also lifts through the original terminal/Kummer subsystem.  Adjoin
`xi^3=T`, choose the deck generator `sigma(xi)=zeta^2*xi`, and set

```text
u=-x^3*xi^2/2,       r8=xi,
R=4/(x^4*(x^2+1)).                                    (6.5)
```

Direct calculation gives

```text
u^3=h,       r8=u^2*R,       r8^9=Z,
9*r8'=3/u.                                              (6.6)
```

The characters are `wt(u)=1`, `wt(r8)=2`, `wt(R)=0`.  Thus this is a
positive control for the full terminal/Kummer subsystem, not merely for the
ninth-power equation.

## 7. General terminal/Kummer converse

The control is an instance of an exact general converse at this subsystem.
Given nonconstant `T`,

```text
h=C*T^2/(T')^3,       Z=T^3,
C^3=j^9/(3^9*nu^10),                                 (7.1)
```

choose `alpha^3=C`, put `xi^3=T`, and define

```text
u=alpha*xi^2/T',       beta=j/(3*alpha),       r8=beta*xi. (7.2)
```

The scalar identity in (7.1) is exactly `beta^9=nu^10`.  Hence

```text
u^3=h,
r8^9=nu^10*Z,
9*r8'=3*beta*T'/xi^2=j/u.                              (7.3)
```

With `sigma(xi)=zeta^2 xi`, `u` has character one, `r8` character two, and

```text
r8/u^2=beta*(T')^2/(alpha^2*T) in C(x).                (7.4)
```

Therefore the descended terminal equation loses no information at the
Kummer-core/original-terminal-row tier once its scalar is retained.  It can
still lose essentially all coefficient-fibre information.
In the selected noncube scope, `xi` and `u` generate the same cyclic cubic
extension; in a cube specialization the construction simply becomes the
trivial Kummer branch.

## 8. What remains charged

Neither the general converse nor the positive control supplies:

1. a lift through the exact seven-row selected-Q8 coefficient component;
2. the global relation among `theta,pi,q,S,tau,Delta`;
3. either complete Taylor polynomiality family at the true center
   `r=A_source/9` (distinct from the terminal numerator `A_T`);
4. simplicity and coprimality of the original `f,g`, or every removed
   projective boundary;
5. an actual polynomial Keller pair.

Consequently no selected-Q8 trajectory, `(9,12)` cell, maximum-twelve case,
counterexample, or JC2 statement is closed.  The cheapest decisive successor
is exact global component grouping: one component containing two Q8 contacts
would die by Section 3; a one-contact component must be tested against the
global Taylor pole divisors, with the `e_pass=2` datum as mandatory positive
control.

## 9. Replay

```sh
python3 cases/max12_912_order3_nu_q8_infinity_contact_passport_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_q8_infinity_contact_passport_20260824/replay.json -
shasum -a 256 -c \
  cases/max12_912_order3_nu_q8_infinity_contact_passport_20260824/MANIFEST.sha256
```

The standard-library replay is a short exact diagnostic.  It pins the five
reviewed parent verdicts, checks the `e_pass=2` Wronskian, terminal identity,
Mason equality, and the cubic-extension identities (6.6).  Projective
surjectivity and the valuation arguments are the proof in Sections 3--5,
not a computational claim.
