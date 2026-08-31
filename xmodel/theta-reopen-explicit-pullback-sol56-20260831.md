# THETA reopen data: the explicit one-cusp pullback

## 0. Frozen inputs, scope, and notation

Before reading, `shasum -a 256` returned exactly

```text
1cf8f9d75e17efd2fc5d43861d721a1eb3b3c0d468e93c75d571f875576012fb  round1033-theta-staged-sol56-20260831.md
cad4a29d4ffd7c405b6530afaac48b2ec1f71617810987a43d038f085c50023b  round1033-theta-staged-hostile-review-grok46-20260831.md
2710e90fdcbf1c2c9f61d6a606cf1e6553de5de65e4899367005433bc4f4e5f5  block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
7a60ff245fc351a99a23815908909327dc6a9644f849a4d3b289079c98488474  block-descent-a1-one-cusp-fibre-connectedness-sol56-20260831.md
69970f4d2c4a2c5760e116400b1b27426edc41fdf6a8d15936df14cc567855c9  block-descent-a1-mprime-coordinator-integration-fable5-20260831.md
```

All paths were the frozen copies under the charged `inputs` directory.  Below
they are abbreviated `staged`, `review`, `structure`, `connectedness`, and
`integration`; citations are frozen-copy line numbers.  No CAS or literature
fetch was used, no charged or canonical file was edited, and `jc2-lean` was not
inspected.  The only written file is this report.

Fix the ordered generators `(A,U,Z)` and

```text
q=U^2-A-A^2Z,       R=C[A,U,Z]/(q),       S=Spec R,
Phi=V(A,U),         K=Frac(R),             kappa in C*.
```

The target pullback has the direction

```text
pi^#: C[xi,eta] -> R,       xi |-> f,       eta |-> g.       (0.1)
```

This is not the source-side chart `iota:R->C[x,y]` displayed in the packets
(`staged:25-68`; `review:273-307`).  The target infinity place, source places
on a generic coordinate fibre, the interior divisor `Phi`, and the generic
ramification divisor over the target curve will remain distinct.

## 1. Constraint system imposed by the promoted packets

### 1.1 Exact polynomial equations

Every element of `R` has a unique normal form (`structure:145-149`).  Write

```text
f=P(A,Z)+U Q(A,Z),       g=R_0(A,Z)+U S_0(A,Z),             (1.1)
```

where all four displayed coefficients are polynomials over `C`.  To avoid a
name collision, `R_0` is a polynomial and `R` without a subscript is the ring.
The Poisson bracket underlying `structure:(1.3)` is determined globally by

```text
{A,U}=2A^2,       {A,Z}=4U,       {U,Z}=2+4AZ.              (1.2)
```

It descends to the quotient: using antisymmetry, the three checks are

```text
{q,A}=2U(-2A^2)-A^2(-4U)=0,
{q,U}=-2A^2-A^2(-2-4AZ)-(4A^3)Z=0,
{q,Z}=2U(2+4AZ)-4U-(8AU)Z=0.
```

Put `H=A(1+AZ)` and `c=2(1+2AZ)`.  Expanding (1.2), replacing every
`U^2` by `H`, and collecting the unique even and odd normal-form parts gives

```text
{f,g}=E+U O,

E=2A^2(P_A S_0-Q(R_0)_A)
  +4H(P_A(S_0)_Z+Q_A(R_0)_Z-P_Z(S_0)_A-Q_Z(R_0)_A)
  +c(Q(R_0)_Z-P_ZS_0),                                    (1.3E)

O=2A^2(Q_A S_0-Q(S_0)_A)
  +4(P_A(R_0)_Z-P_Z(R_0)_A
       +H(Q_A(S_0)_Z-Q_Z(S_0)_A))
  +c(Q(S_0)_Z-Q_ZS_0).                                    (1.3O)
```

Thus the complete coefficient-level constant-Jacobian constraint is the
polynomial identity system

```text
E=kappa,                     O=0                            (1.4)
```

in `C[A,Z]`.  This is stronger and more useful than matching variable names:
every candidate can be checked coefficient by coefficient in the declared
quotient.

### 1.2 Intrinsic completion and first-jet constraints

Complete along the whole *interior* line `Phi` and set `u=U`.  The exact
whole-line completion and its generic-point complete DVR are
(`structure:55-115`)

```text
A=a(u,Z)=u^2-Zu^4+2Z^2u^6-5Z^3u^8+...,
completion_along_Phi=C[Z][[u]],
completion_of_R_(A,U)=C(Z)[[u]],
{u,Z}=2+4Za(u,Z).                                           (1.5)
```

Consequently, if

```text
p=P(0,Z), q_1=Q(0,Z), r=R_0(0,Z), s_1=S_0(0,Z),
```

then the constant term of (1.4), checked directly in (1.3E), is

```text
2(q_1 r'-p's_1)=kappa.                                    (1.6)
```

The promoted companion-curve interface additionally says that
`Z |-> (p(Z),r(Z))` is an immersive normalization with two distinct points
having the same image.  Neither coordinate is affine or constant, so
`deg p,deg r>=2` (`structure:164-189`; `review:58-81`).  This image is the
interior companion curve customarily called `C_0`; it is **not** the target
boundary curve `B`.

There is no charged upper bound on `deg_A P,deg_A Q,deg_A R_0,deg_A S_0`, nor
on their `Z`-degrees away from `A=0`.  In particular, the provisional identity
`mu=d1=2` and the normalization `t=A` belong to the inverse-Kummer/ruling
ledger (`structure:472-503`); they are not degrees of `f` or `g`.  The symbols
`c_0,E,r_E,kappa_B` there are not supplied as polynomials (`review:83-92`).

### 1.3 Global and boundary interfaces

An admissible solution of (1.4) must also realize the charged global data:

1. `[K:C(f,g)]=4`; `pi|_S` is etale, has cofinite image, and the mate on a
   general coordinate fibre has degree four (`review:120-125`;
   `connectedness:73-83,229-244,289-296`).  The packet's dynamical condition
   is **non**-local-finiteness of both Hamiltonian derivations, not a separate
   property called “`pi` locally finite.”  The restrictions in (1.6) already
   put both coordinates outside `C[A]`; see `structure:151-162` for the
   provisional LF formulation and `structure:281-295` for the independent
   boundary-valuation witness.
2. `C(f)` and `C(g)` are algebraically closed in `K`; hence both general
   coordinate fibres are smooth, geometrically irreducible and connected
   (`connectedness:169-225,249-279,432-443`).
3. At the interior companion over the cusp, with
   `p_c=f-f(u_c),q_c=g-g(u_c)`, etaleness gives
   `O^_(S,u_c)=C[[p_c,q_c]]`,
   `X_f=kappa partial_(q_c)`, `X_g=-kappa partial_(p_c)`
   (`structure:198-220`).
4. At the generic point of `B`--not at its infinity--there must be one
   ramified factor and two unramified factors, with

   ```text
   K_B[[b]] -> K_B[[s]], b |-> s^2,
   X_f(b)=kappa b_g,     X_g(b)=-kappa b_f,
   X_f~(kappa overline(b_g)/2)s^-1 partial_s,
   X_g~-(kappa overline(b_f)/2)s^-1 partial_s,
   v(D^j s)=1-2j.                                         (1.7)
   ```

   These are exactly `structure:(1.12)-(1.14)` (`structure:243-279`).  They
   do not determine the special cusp completion or identify `B`, `Phi`, or a
   deleted cyclic line (`structure:297-298`; `review:184-224`).
5. For `h` equal to either coordinate and `k` its mate, the general affine
   fibre is hyperbolic.  If its smooth completion has genus `gamma_h`, if
   `r_h` is the number of poles of `k`, and if their positive pole orders form
   the partition `lambda_h` of four, then (`connectedness:289-344`)

   | `r_h` | `lambda_h` | necessary `d_h` |
   |---:|---|---:|
   | 1 | `(4)` | `2gamma_h+3` |
   | 2 | `(3,1)` or `(2,2)` | `2gamma_h+4` |
   | 3 | `(2,1,1)` | `2gamma_h+5` |
   | 4 | `(1,1,1,1)` | `2gamma_h+6` |

   Equivalently `d_h=2gamma_h+2+r_h`, and the affine Euler characteristic is
   `-4gamma_h-2r_h<0` (`structure:415-444`).  This table is necessary only;
   the two coordinates have separate genera and partitions.

## 2. Lowest-complexity admissible shape and free parameters

Use lexicographic complexity

```text
(max(deg p,deg r), deg p+deg r,
 max(deg q_1,deg s_1),
 max(deg_A P,deg_A Q,deg_A R_0,deg_A S_0)).                (2.1)
```

This is a search convention, not a packet invariant.  The first two entries
minimize the residue curve, the third selects its least first jet, and the
packet gives no ceiling for the fourth.

### 2.1 Minimal residue curve

Degrees `(2,2)` cannot satisfy the companion interface.  Indeed, for

```text
p=a_2Z^2+a_1Z+a_0,       r=b_2Z^2+b_1Z+b_0,
```

equality at distinct `z,w` forces both
`a_2(z+w)+a_1=0` and `b_2(z+w)+b_1=0`.  If
`a_2b_1-a_1b_2` is nonzero there is no such pair; if it is zero, `r` is an
affine function of `p` and `p',r'` vanish together.  The image is then a line
and the parametrization is not immersive.  Hence the first possible unordered
degree pair is `(2,3)`.

All coefficient freedom at that degree, before (1.6), may be written

```text
p=a_2Z^2+a_1Z+a_0,             a_2!=0,
r=b_3Z^3+b_2Z^2+b_1Z+b_0,      b_3!=0.                    (2.2)
```

Put

```text
sigma=-a_1/a_2,
tau_0=sigma^2+(b_2 sigma+b_1)/b_3,
Delta=sigma^2-4tau_0
     =-3sigma^2-4(b_2 sigma+b_1)/b_3.                     (2.3)
```

The two roots of `X^2-sigma X+tau_0` are precisely the possible double
preimages.  They are distinct exactly when `Delta!=0`.  Moreover
`r'(sigma/2)=-b_3Delta/4`; thus the same inequality makes (2.2) immersive,
and the two tangent directions at the double image have nonzero determinant
`a_2b_3(z-w)Delta`.  It is an ordinary node.  Its function-field degree
divides both `deg p=2` and `deg r=3`, hence is one, so the parametrization is
the normalization.  The free scalar parameters in
the minimal residue family are therefore

```text
kappa in C*,
a_2,a_1,a_0,b_3,b_2,b_1,b_0 in C,
a_2 b_3 Delta !=0.                                       (2.4)
```

Since `gcd(p',r')=1`, choose any one Bezout pair `alpha,beta` with
`alpha r'-p'beta=kappa/2`.  Every first normal jet satisfying (1.6), and no
other one, is

```text
q_1=alpha+p' T_0,       s_1=beta+r'T_0,
T_0 in C[Z] arbitrary.                                  (2.5)
```

The swapped `(3,2)` family is obtained by interchanging the coordinate roles.
Equations (2.4)--(2.5) list all freedom at the lowest residue complexity.

### 2.2 Simplest point and mandatory ruling corrections

For an explicit bounded test--not as a “without loss of generality”
normalization of the fixed ring--select

```text
p=Z^2,       r=Z^3-Z.                                    (2.6)
```

The preimages `1,-1` meet at `(1,0)`; the derivatives `(2,2)` and `(-2,2)`
have determinant `8`.  All solutions of (1.6) are

```text
q_1=-kappa/2+2Z T_0(Z),
s_1=-3kappa Z/4+(3Z^2-1)T_0(Z).                          (2.7)
```

The lowest-degree jet takes `T_0=0`.  Every polynomial lift of that chosen
jet has exactly the shape

```text
f=Z^2-(kappa/2)U+A(P_1(A,Z)+UQ_1(A,Z)),
g=Z^3-Z-(3kappa/4)ZU+A(R_1(A,Z)+US_1(A,Z)),              (2.8)
```

where `P_1,Q_1,R_1,S_1 in C[A,Z]` are the remaining free polynomial
coefficients, subject only to the two full equations (1.4) and the global
interfaces of §1.3.  There are no further packet-supplied polynomial degree
caps.  Separate, mostly provisional global coordinates--cusp incidence,
collision location and tangency, `kappa_B`, `N`, and the two table tuples--are
quarantined from this coefficient ansatz (`structure:581-609`); none supplies
the slim gate's missing pullback.

The first two coefficient conditions beyond (1.6) are jointly consistent.
For example, put

```text
P_1(0,Z)= 3kappa^2/16,       Q_1(0,Z)=-9kappa^3/64,
R_1(0,Z)= 9kappa^2 Z/32,     S_1(0,Z)=kappa/6-27kappa^3Z/128.  (2.9)
```

For clarity, the `A^0` coefficient of (1.3O) is

```text
4[(3kappa^2/16)(3Z^2-1)-(2Z)(9kappa^2Z/32)]
 +2[(-kappa/2)(-3kappa/4)]=0.
```

For the `A^1` coefficient of (1.3E), its three summands are

```text
4M_0+2N_1+2kappa Z,
M_0=-kappa Z/3,       N_1=-kappa Z/3,
```

because, term by term,

```text
M_0=(-9kappa^3/64)
    +(-9kappa^3/64)(3Z^2-1)
    -2Z(kappa/6-27kappa^3Z/128)=-kappa Z/3,
N_1=(-9kappa^3/64)(3Z^2-1)
    +(-kappa/2)(9kappa^2/32)
    -2Z(kappa/6-27kappa^3Z/128)=-kappa Z/3.
```

Thus it is `(-4/3-2/3+2)kappa Z=0`.  This is only a checked finite jet, not a
polynomial construction: the remaining coefficients of both (1.3E) and
(1.3O) still have to vanish, and (2.9) supplies none of the global degree-four
or boundary data.

## 3. Construction or typed obstruction

### 3.1 First inconsistency: ruling degree zero

Suppose all four coefficients in (1.1) are independent of `A`.  Then (1.3E)
reduces exactly to

```text
E=2(1+2AZ)(Q(R_0)'-P'S_0).                               (3.1)
```

Its `A^0` coefficient forces `Q(R_0)'-P'S_0=kappa/2`; its `A^1`
coefficient is then `2kappa Z`, which cannot vanish.  Thus

```text
OBSTRUCTION[A-DEGREE-ZERO]: no constant-bracket pair in the charged
normal form has all four coefficient polynomials in C[Z].              (3.2)
```

This is independent of the choice of residue degrees.  It contradicts the
constant-bracket interface only in the stated complexity class; at least one
positive ruling correction is mandatory.

### 3.2 The full `A`-linear test at the simplest minimal jet

There is a stronger finite obstruction for (2.6)--(2.7) with `T_0=0`.  Assume
all four coefficients have `A`-degree at most one and write

```text
P=Z^2+AC,                 Q=-kappa/2+AD,
R_0=Z^3-Z+AE,             S_0=-3kappa Z/4+AL,             (3.3)
```

with `C,D,E,L in C[Z]`, and put `c_*=3kappa^2/16`.  Four necessary
coefficients of (1.4), obtained directly from (1.3E)--(1.3O), are

```text
[A^0]O:  2ZE-(3Z^2-1)C=c_*,                              (3.4)

[A^1]E:  kappa sigma'-9kappa Z sigma
          +6D(3Z^2-1)-12ZL+2kappa Z-(9/2)kappa c_*=0,     (3.5)

[A^1]O:  C'E-CE'=-(kappa/4)L'-(9kappa/8)D
                   +(3kappa Z/8)D'+(3kappa^2/8)Z,         (3.6)

[A^3]O:  DL'-D'L=0,                                      (3.7)
```

where all solutions of (3.4) have been written

```text
C=c_*+2Z sigma,       E=(3c_*/2)Z+(3Z^2-1)sigma,
sigma in C[Z].                                           (3.8)
```

Here is the complete degree contradiction.  If `D!=0`, (3.7) gives
`L=lambda D` for a constant `lambda`.  With `m=deg D`, the degree `m+2`
term of (3.5) forces

```text
deg sigma=m+1,       lc(sigma)=2 lc(D)/kappa.             (3.9)
```

Using (3.8), the left side of (3.6) then has uncancellable leading term

```text
-6 lc(sigma)^2 Z^(2m+4),                                 (3.10)
```

whereas its right side has degree at most `max(m,1)`.  This is impossible.

If `D=0` and `sigma` is zero or constant, every term of (3.5) except
`-(9/2)kappa c_*` is divisible by `Z`, so its nonzero constant term cannot
cancel.  If instead `n=deg sigma>=1`, (3.5) forces `deg L=n`.  The left side
of (3.6) has leading term `-6lc(sigma)^2Z^(2n+2)`, while the right side has
degree at most `max(n-1,1)`, again impossible.  All cases are exhausted:

```text
OBSTRUCTION[A-LINEAR-MINIMAL-JET]: for p=Z^2, r=Z^3-Z and T_0=0,
no choice C,D,E,L makes {f,g}=kappa when all four A-degrees are <=1.     (3.11)
```

This obstruction is deliberately narrower than the horn.  It does not cover
another point of the seven-parameter family (2.2), a nonzero polynomial
`T_0` in (2.5), or any maximum `A`-degree at least two.  The frozen packets
supply no finite cap with which to exhaust those cases.  The compatible
finite layer (2.9) also shows that there is no earlier universal jet
inconsistency to promote.

### 3.3 Why the remaining construction is counterexample-level

The source chart may be used as a consequence check, although never as the
pullback (0.1).  Substitute

```text
A=x^2,       U=x+x^3y,       Z=2y+x^2y^2                 (3.12)
```

and call the resulting polynomials `F=iota(f),G=iota(g)`.  Direct standard
Jacobian calculations give, term by term,

```text
J(x^2,x+x^3y)=2x^4=2A^2,
J(x^2,2y+x^2y^2)=4x(1+x^2y)=4U,
J(x+x^3y,2y+x^2y^2)
 =2+8x^2y+4x^4y^2=2+4AZ.                                (3.13)
```

Thus (1.4) would imply `J(F,G)=kappa`.  The packet records
`[C(x,y):K]=2` (`review:299-304`); the charged rank-four condition would give

```text
[C(x,y):C(F,G)]=[C(x,y):K][K:C(f,g)]=2*4=8.              (3.14)
```

So a landed admissible pair would, by explicit composition, be a
noninvertible plane Keller map of geometric degree eight.  This is not an
obstruction theorem and is not a reuse of `iota` in the wrong direction.  It
types the mathematical strength of the missing higher-`A` solution.

No such solution, and no all-complexities inconsistency, follows from the five
promoted inputs.  The construction disposition is therefore

```text
OPEN[THETA-EXPLICIT-PULLBACK]: equations (1.4), the minimal family
(2.2)-(2.5), and obstructions (3.2)/(3.11) are exact, but arbitrary finite
A-complexity and the charged degree-four boundary realization remain open.
```

## 4. Target curve and normalized parametrization

The curve required by the numerical gate is relational data, not an arbitrary
rational curve.  For a landed pair, let `Y` be the normalization of the target
`A2` in `K`.  One must identify the relevant component of `Y-S`, prove its
image is an irreducible curve `B`, and display

```text
b(xi,eta) in C[xi,eta] irreducible,
beta_B:A1_t -> B,       t |-> (F_B(t),G_B(t)),             (4.1)
ker(C[xi,eta] -> C[t])=(b),
C(F_B,G_B)=C(t).                                           (4.2)
```

Here `F_B,G_B` are polynomials, `C[t]` is the normalization of
`C[xi,eta]/(b)`, and the completion has its single omitted point
`q_infty` at `t=infinity` (`review:131-153`).  The curve is singular,
irreducible, neither vertical nor horizontal, and the charged surface-sheet
census is

```text
generic B: (2,1,1),       cusp c: (3,1),
omitted node n: (2,2),    e(T)=-3.                         (4.3)
```

See `structure:243-279,383-413`.  Equation (4.3) is data of the degree-four
normalization over the curve; an equation `b` by itself does not verify it.
Nor may one silently strengthen the interface to say that `B` is the entire
codimension-one branch image: that remains
`OPEN[CENSUS-EXHAUSTIVITY]` (`connectedness:445-453`).  What a construction
must verify is the promoted general-slice interface used in §1.3.

The residue curve from (2.6) illustrates the forbidden shortcut.  Its equation
is

```text
C_0: eta^2-xi(xi-1)^2=0,       Z |-> (Z^2,Z^3-Z).          (4.4)
```

This is `pi(Phi)`, not `B`.  Indeed `T=pi^(-1)(B) intersect S` is charged to
meet `Phi` in a finite number `N` (`structure:559-579`).  Setting `B=C_0`
would instead put all of `Phi` in `T`.  In particular `deg p=2` in §2 says
nothing about `d_f`: the former is measured on `Phi`, the latter at the
different target place `q_infty`.

No full pair was constructed or derived, so the normalization
`Y`, its deleted component, and hence `b,F_B,G_B` cannot be calculated.  The
frozen inputs only say “let `b(f,g)` be” and never supply (4.1)
(`review:83-96`).  Therefore item (2) of the slim gate remains

```text
OPEN[THETA-TARGET-B]: no equation or parametrization can be verified as the
boundary image belonging to the still-missing pullback.                  (4.5)
```

## 5. Independent computations of the numerical data

This section is not numerically entered because no construction landed.  It
is nevertheless possible to state exactly what the two independent checks
would be.

For `h=f`, (4.1) would give

```text
d_f=deg F_B=-ord_(q_infty)(F_B).                           (5.1)
```

The independent geometric check is the number, with multiplicity, of
intersections of `B` with a general vertical line; transversality in the
charged generic slice makes it the number of finite deleted index-two places.
For `h=g`, replace `F_B` and vertical by `G_B` and horizontal.  Thus the two
methods are polynomial pole order and general-line intersection/deleted-place
count (`structure:398-418`; `connectedness:318-330`).  Neither can be run
without (4.1) and its verified boundary realization.

For `r_h`, one algebraic method is to take the function field of
`R tensor_(C[h]) C(h)`, pass to its unique smooth projective curve, and count
the distinct valuations at which the mate `k` has negative order.  A separate
surface method is to complete and resolve a general fibre `R/(h-a)` and count
its distinct branches meeting the divisor `k=infinity`.
Their multiplicities must form a positive partition of four; `r_h` counts its
support, not its total degree.  Without `f,g`, both the generic curve and its
polar divisor are absent.

The promoted data consequently give only

```text
1<=r_h<=4,       d_h=2gamma_h+2+r_h,
Theta_h=d_h-r_h-2=2gamma_h in 2Z_(>=0).                   (5.2)
```

Equation (5.2) is a necessary interface, not a computed value and not
attainment of any row.  No partition row is selected.  In particular, the
minimal interior degree `2` in (2.6) is not inserted into (5.2).

## 6. Verdict and exact scope

There is one terminology fork to close explicitly.  Non-local-finiteness of
`X_f,X_g` is a charged/provisional dynamical input; it also follows
conditionally once the reviewed true-boundary realization supplies the exact
pole-growth witness.  By contrast, `pi|_S` is etale and hence locally
quasi-finite, while the separate normalization `Y->A2` is finite.  If the
launch phrase “locally finite” literally requires locally finite Hamiltonian
derivations, it contradicts `structure:151-162,281-295`.  This report uses the
only packet-compatible reading: locally quasi-finite for `pi`,
non-locally-finite for the Hamiltonians.

The requested supply does not land.  This is the slim numerical gate of
`integration:119-130`.  What is closed is the full unbounded polynomial
constraint system (1.3)--(1.4), the exhaustive residue and first-jet parameter
family at lowest residue complexity,
the universal ruling-degree-zero obstruction, and the complete `A`-linear
obstruction for the simplest minimal first jet.  What remains open is every
other point of (2.2), every nonzero `T_0` stratum, and arbitrary finite ruling
degree at least two, followed by the rank-four field-degree, boundary,
cusp/node, and general-fibre checks.
Because the packets impose no ruling-degree cap, a finite exhaustion cannot be
promoted.

Final disposition:

```text
OPEN[THETA-EXPLICIT-PULLBACK]
OPEN[THETA-TARGET-B]
Theta_f,Theta_g UNCOMPUTED; no partition row selected.
```

This is not a contradiction of the one-cusp horn.  The two obstructions have
exactly the scopes (3.2) and (3.11); extending either by analogy would be a
raw-degree/floor error.  Identities (1.7) were kept at their generic boundary
valuation, and no target place, source fibre place, interior divisor, or cover
series was identified with another.  No exit price is asserted.

<!-- BODY-END -->
