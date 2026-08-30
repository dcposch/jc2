# Singular F5 local polar: balanced A-type factorization and contracted-carrier multiplicity

Date: 2026-08-30 UTC  
Producer: Sol 5.6 Ultra sublane `/root/singular_p0_local_different`  
Frozen basis: `5f285393f481bfb8f8767fa0ad09b1eeeb1d9f91`  
Lifecycle: **EXACT PROVISIONAL LOCAL THEOREM / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint

In the charged normal, reduced, finite-near-infinity F5 quadratic-incidence
scope, the balanced singular rows have a coefficient-invariant completed
local polar factorization.  Write the balanced fibre tag as

```text
B_s/A_(s-1),                 5<=s<=9.
```

Then the strict source different over the singular F5 point has exactly

```text
s odd:   three reduced germs of A-degrees 2,3,3;
s even:  two reduced germs of A-degrees 2,6.             (0.1)
```

The degree-two germ meets a smooth point of the first exceptional component.
For odd `s`, the two degree-three germs meet distinct smooth points of the
middle component `E_((s-1)/2)`.  For even `s`, the degree-six germ passes
through the exceptional node

```text
E_((s-2)/2) cap E_(s/2).                                (0.2)
```

These are strict analytic germs, not formal lattice entries.  Every germ has
Cartier different coefficient one.  The exceptional different coefficient
and strict-contact vectors are exactly

```text
m_i=min(i+1,s-i),       1<=i<=s-1,
n=C_(A_(s-1))*m,

s odd:   n=e_1+2e_((s-1)/2),
s even:  n=e_1+e_((s-2)/2)+e_(s/2).                    (0.3)
```

The physical attachment sites in (0.2)--(0.3) are distinct.  If two strict
germs were branches of one global irreducible ramification prime, that prime
and the connected exceptional tree would form a cycle in the resolved full
first-leg boundary.  Therefore distinct local germs in (0.1) lie on distinct
global primes.

Combining this with the binding Euler cap `rho+k<=8` eliminates

```text
B_7/A_6, B_8/A_7, B_9/A_8.                             (0.4)
```

The `A8` row was already dead from `k>=1`; the new content is the exact death
of `B_7/A_6` and `B_8/A_7`.  The remaining balanced rows sharpen to

```text
B_5/A_4: k>=3, hence r_aff<=1;
B_6/A_5: k>=2, hence r_aff+k<=3.                       (0.5)
```

The packet also gives an exact generic-DVR classification for an affine
coefficient-basepoint carrier `Z`.  Its Cartier multiplicity in the source
different is one of `1,2,3,4`, determined by the first nonconstant
coefficient in a four-stage tangential expansion.  In particular

```text
1<=nu_Z<=4,                                             (0.6)
```

and `nu_Z>1` forces the first base jet to have rank one and forces a
length-three singular scheme on `Z`.  This does not force `nu_Z=1`.

The unbalanced `U_3,U_5,U_6` rows are not promoted by this packet.  Their
explicit normal forms are recorded only as a successor at the end.  Formal
normal forms, finite jets, and numerical contact vectors remain distinct
from physical analytic germs and global primes throughout.

## 1. Frozen inputs and exact local equation

This packet charges the corrected carrier theorem and its mandatory
corrigendum:

```text
f942e743dc206d958f31892e838d7517fe23eacbc863b56c9441b60152bc0cb4
  xmodel/bd-a2-normal-f5-decorated-carrier-effectivity-reduction-sol56-20260830.md
  body e4823537bbaa3bb6142790456c11814d9be32c8b3f4c93f2563a2a13eb2a641d;

94f5bc5ce509809b951f5189bb6d3f863c09133dfda77522965d791a7419ee2e
  xmodel/bd-a2-normal-f5-contracted-carrier-compatibility-corrigendum-sol56-20260830.md
  body 488da252288cd9cc14ea797529d49b2d9db3c0a74bcab4308965ac07205182b6;

f092a7152dea8bdee387825fa8181dffeb8145fc99cf65973d74f528491f57a0
  xmodel/bd-a2-a1-ruling-euler-boundary-cap-coordinator-integration-sol56-20260830.md.
```

Use target coordinates `(u,v)` with infinity `u=0` and the source-line
coordinate `z`, all zero at the F5 point.  The exact reduced infinity germ is

```text
h(v,z)=z(z-v)((1+v)z-v).                              (1.1)
```

Because the incidence has target degree two, its completed equation before
any unit division is exactly

```text
f(u,v,z)
 =h(v,z)+u(a(z)u+b(z)v+c(z)),                         (1.2)
```

with analytic one-variable coefficients.  Singularity of the surface at the
origin says `c(0)=0`.  Its quadratic tangent cone is

```text
u(a(0)u+b(0)v+c'(0)z).                                (1.3)
```

The balanced `B_s` rows are exactly the nondegenerate rank-two case
`b(0)!=0`.  Multiplication of `f` by a unit and a constant target shear,
which preserve the ramification divisor, normalize

```text
b(0)=1,                a(0)=0.                        (1.4)
```

The analytic critical point `(u_0(z),v_0(z))` in the two target variables is
unique by the parametric Morse lemma.  Centering there and factoring the
nondegenerate quadratic form gives completed coordinates `(X,Y,z)` in which

```text
f=XY+phi(z),            ord_z(phi)=s,                 (1.5)
```

for the tag `A_(s-1)`.  These are source analytic coordinates used to compute
the divisor; they are not a change of the target map.

The cubic homogeneous part of (1.1) is

```text
h_3=z(z-v)^2.                                          (1.6)
```

If `v_0=tau*z+O(z^2)`, evaluation at the critical point gives

```text
phi=(1-tau)^2 z^3+O(z^4).                             (1.7)
```

Thus every `s>=5` balanced row forces `tau=1`.  The critical equations and
the Hessian factorization then give, after multiplying `X,Y` by reciprocal
units,

```text
v=z+X+O(z^2,zX,zY),
u=u_0(z)-zX+Y+O(z^2X,zY),       ord(u_0)>=3.           (1.8)
```

Every omitted term lies strictly above the Newton edges used below.  This is
the point at which the full coefficient family is retained: `a,b,c` have not
been specialized to a chosen representative.

## 2. The invariant balanced polar factorization

On the smooth locus of (1.5), use the residue generator

```text
omega=dX wedge dz / X.
```

Writing `du wedge dv=r*omega` defines the source Cartier different.  Direct
differentiation of the full linear-in-`X,Y` inverse Hessian transformation,
using `Y=-phi/X`, shows that `P=Xr` has Newton-principal form

```text
P
 =unit*X^3-unit*zX^2+unit*phi'(z)X+unit*phi(z)
  +(terms strictly above the lower Newton polygon).    (2.1)
```

The four displayed coefficients are nonzero.  The lower polygon has vertices

```text
(3,0), (2,1), (0,s).                                  (2.2)
```

Its first edge has one simple nonzero root, hence one smooth strict polar
germ

```text
X=unit*z+O(z^2).                                      (2.3)
```

The second edge is

```text
X^2=unit*z^(s-1).                                     (2.4)
```

If `s` is odd, (2.4) has two distinct Hensel roots in `C[[z]]`; if `s` is
even, its odd exponent makes one reduced irreducible Puiseux branch, with
parameter `z=t^2`.  The spurious vertical curve in `div(P)=div(X)+div(r)` is
not counted: (2.3)--(2.4) have `X!=0` generically and are precisely the
strict different germs.

There is no coefficient cancellation on either edge.  In particular the
factorization is invariant under all higher coefficients in `a,b,c` that
retain the named `A_(s-1)` tag.

## 3. Exact A-degrees, Cartier coefficients, and exceptional vectors

The local Cartier intersection remains

```text
length O_(X,p)/(u,r)
 =length C[[v,z]]/(h,h_z)=8.                          (3.1)
```

No strict polar germ is contained in `u=0`.  From (1.8), the germ (2.3) has

```text
ord_C(u)=2.                                           (3.2)
```

For an odd `s`, each root of (2.4) has `ord(u)>=3`; for an even `s`, its one
Puiseux branch has `ord_t(u)>=6`.  Additivity with the exact total (3.1)
forces the equalities

```text
s odd:   8=2+3+3;
s even:  8=2+6.                                      (3.3)
```

The Newton edge factors are squarefree in characteristic zero, so every
strict prime in (3.3) occurs with Cartier coefficient one.  The numbers in
(3.3) are local orders of the Cartier function `u` on normalizations of
strict source-different germs.  They are therefore the local contributions
to the global `A.C` degrees.  They are not exceptional coefficients, target
discriminant multiplicities, or normalization indices.

Use the standard `A_(s-1)` numbering with `E_1` adjacent to the strict F5
fibre component `L`.  On the toric minimal resolution of
`XY+unit*z^s=0`,

```text
ord_(E_i)(X)=i,
ord_(E_i)(Y)=s-i,
ord_(E_i)(z)=1.                                      (3.4)
```

Equation (2.1), divided by `X`, then gives

```text
m_i=ord_(E_i)(r)=min(i+1,s-i).                        (3.5)
```

At the equality index, the initial forms of `zX` and `Y` are distinct
nonconstant functions on `E_i`, so they do not cancel identically.  Applying
the Cartan matrix yields (0.3).  Physically:

* (2.3) meets a smooth point of `E_1`;
* an integral exponent `X=lambda*z^j`, with distinct nonzero `lambda`, meets
  a smooth point of `E_j`, and distinct `lambda` give distinct points;
* a half-integral exponent `j+1/2` gives one irreducible germ through the
  node `E_j cap E_(j+1)`.

The exact table is

| tag | `m` | `n=Cm` | strict A-degree partition | physical sites |
|---|---|---|---|---|
| `B_5/A_4` | `(2,3,2,1)` | `e1+2e2` | `2+3+3` | smooth `E1`; two distinct smooth points of `E2` |
| `B_6/A_5` | `(2,3,3,2,1)` | `e1+e2+e3` | `2+6` | smooth `E1`; node `E2 cap E3` |
| `B_7/A_6` | `(2,3,4,3,2,1)` | `e1+2e3` | `2+3+3` | smooth `E1`; two distinct smooth points of `E3` |
| `B_8/A_7` | `(2,3,4,4,3,2,1)` | `e1+e3+e4` | `2+6` | smooth `E1`; node `E3 cap E4` |
| `B_9/A_8` | `(2,3,4,5,4,3,2,1)` | `e1+2e4` | `2+3+3` | smooth `E1`; two distinct smooth points of `E4` |

For comparison, the three strict F5 boundary branches have

```text
a_H=e_1+e_2+e_(s-3).                                 (3.6)
```

In the decisive `B_8/A_7` row this is

```text
a_H=e_1+e_2+e_5,
h_H=C^(-1)a_H=(2,3,3,3,3,2,1),                       (3.7)
```

whereas the different has

```text
m_R=(2,3,4,4,3,2,1),
n_R=e_1+e_3+e_4.                                     (3.8)
```

Thus the degree-two and degree-six polar germs use the distinct sites
`E_1^sm` and `E_3 cap E_4`; neither a formal coefficient nor a branch flag
has been substituted for a physical attachment.

The small replay

```text
ops/f5_singular_polar_replay.py
```

checks (3.5), every row of the table, and (3.8) using only Python's standard
library.  It is an arithmetic replay, not evidence for the analytic Newton
argument.

## 4. The globalization-cycle lemma and the A7 death

Every `E_i` belongs to the reduced full first-leg boundary: it occurs in the
total transform of `H`, with positive coefficient (3.7), and in the total
different, with positive coefficient (3.8).  Every strict polar germ belongs
to the closure of the affine non-etale boundary.

Suppose two strict local germs at distinct sites of the connected exceptional
tree were branches of one global irreducible prime `C`.  The proper transform
of `C` is irreducible.  In the resolved boundary dual graph, its one connected
vertex/subgraph attaches to the exceptional tree at the two sites.  The path
inside `C` together with the unique path inside the exceptional tree is a
cycle.  If one germ initially passes through an exceptional node, the first
embedded blowup only subdivides that node and its attachment; it cannot
identify the two sites or lower the first Betti number.

The binding first-leg boundary is a rational forest, so this is impossible.
Consequently every pair of strict germs at distinct sites in Section 3 lies
on distinct global primes.  Hence

```text
s odd:  k>=3;
s even: k>=2.                                         (4.1)
```

This is stronger than the false inference "distinct local germs imply
distinct global primes": the actual reason is the two-site cycle in the
full boundary, with all objects typed.

For `B_8/A_7`, (4.1) gives `k>=2`.  The binding Euler theorem gives

```text
rho+k<=8,       rho>=7,                               (4.2)
```

so it simultaneously requires `k<=1`.  This contradiction kills the row.
Similarly `B_7/A_6` has `rho>=6,k>=3`, and `B_9/A_8` has
`rho>=8,k>=3`; both are impossible.  The first of those is new, while the
last was already impossible from the weaker `k>=1` test.

No claim is made that the surviving `B_5` or `B_6` tags are effective.

## 5. The q=6 balanced modulus and why no universal 3+5 exists

For `B_3/A_2`, retain the critical tangent modulus

```text
v_0=tau*z+O(z^2),       tau!=1,       sigma=1-tau.     (5.1)
```

Here `phi=sigma^2 z^3+O(z^4)`.  The homogeneous polar polynomial in
`T=X/z` factors exactly as

```text
(T-sigma)
 [T^2-(1+2sigma)T+sigma(sigma-1)].                   (5.2)
```

The first factor is the branch tangent to the two section branches of `H`.
It never equals a root of the quadratic because `sigma!=0`.  Thus there are
at least two distinct physical polar sites for every value of the modulus.

If `tau!=0` and

```text
Delta=1+8sigma=9-8tau !=0,                            (5.3)
```

there are three reduced smooth strict germs, all at distinct smooth points
of `E_1`, with exact A-degree partition

```text
4+2+2.                                                (5.4)
```

If `Delta=0`, the tangent degree-four germ remains separate while the
quadratic block has total A-degree four.  Its higher discriminant decides
whether it is one irreducible germ or two tangent germs; a nonreduced
divisorial prime is forbidden by the charged fixed-sheet coefficient-one
theorem.  For `tau!=0` the exceptional vectors are exactly

```text
m=(2,1),             n=3e_1.                         (5.5)
```

If `tau=0`, the two distinct nonzero principal roots `T=1,3` still give two
distinguished `E_1` sites, while a higher-order residual block is centered at
the opposite endpoint.  Its splitting, Cartier multiplicity, and possible
increase of exceptional valuations depend on higher coefficients and are not
promoted here.  In the exact simple representative `f=uv+h`, that block is a
vertical prime of Cartier coefficient two; this representative is outside
the fixed-sheet coefficient-one subcell.

Thus `B_3/A_2` has at least two global ramification primes after the same
two-site forest argument, but its finer local partition is genuinely
modulus-dependent.  There is no coefficient-independent singular `3+5`
analogue.

## 6. Exact generic-DVR multiplicity of a contracted carrier

Let `Z={q} times P1` be an affine coefficient-basepoint carrier and work at
its generic point, where the normal surface is smooth.  Choose target
parameters `(s,t)` at `q` and put `K=C(Z)`.  The target-degree-two incidence
has the exact expansion

```text
F=sP+tQ+s^2A+stB+t^2C,       P,Q,A,B,C in K,          (6.1)
```

with `(P,Q)!=(0,0)`.  Assume `P!=0`, divide by it, and solve the surface
equation uniquely as

```text
s=a_1(z)t+a_2(z)t^2+a_3(z)t^3+... .                  (6.2)
```

In parameters `(t,z)` on the surface, the map to `(s,t)` has Jacobian
`partial s/partial z`.  Therefore

```text
nu_Z=min{j>=1 : a_j is nonconstant in K}.             (6.3)
```

Characteristic zero is used here: a rational function has zero derivative
exactly when it is constant.

The quadratic target degree bounds the first nonconstant stage sharply.

1. `a_1=-Q/P`.  If it is nonconstant, `nu_Z=1`.
2. If `a_1` is constant, a constant linear target shear makes `Q=0`.  Write
   `s=t^2w`; then
   `w+A t^2w^2+Btw+C=0`.  If `C` is nonconstant, `nu_Z=2`.
3. If `C=c` is constant, then `c!=0`; otherwise the unique local component
   is `s=0` and the map is not generically finite.  The coefficient of `t`
   is `cB`, so nonconstant `B` gives `nu_Z=3`.
4. If `B` is also constant, the coefficient of `t^2` is a nonzero affine
   function of `A`, so nonconstant `A` gives `nu_Z=4`.
5. If `A,B,C` are all constant, (6.1) is independent of `z` up to a unit;
   the map again has rank at most one on a neighbourhood, contradicting
   generic finiteness.

This proves (0.6) and gives an exact decision tree, not merely the already
known global budget `sum nu<=4`.

Moreover `nu_Z>1` is equivalent to the first-jet pencil `[P:Q]` being
constant.  Then `P,Q` are proportional cubic sections.  At every zero of
their common cubic, all three partial derivatives of `F` vanish along `Z`.
Thus `nu_Z>1` forces a singular subscheme of total length three on `Z`.
The packet does not convert that length into an ADE-rank lower bound and does
not exclude higher multiplicity.

## 7. Remaining U rows and scope firewall

The exact tangent-cone split of (1.3) also gives

```text
b(0)=0, c'(0)!=0:                 U_3/A_3;
b(0)=c'(0)=0, a(0)!=0:           U_5/D_5 or U_6/D_6. (7.1)
```

Completing the square in `u` writes these as

```text
x^2+w(z)h(v,z)-d(v,z)^2=0.                            (7.2)
```

Explicit representatives indicate the provisional patterns

```text
U_3/A_3: 4+4;
U_5/D_5: 2+3+3;
U_6/D_6: 3+5,                                        (7.3)
```

with respectively two, three, and two strict germs.  This packet does not
promote (7.3): the full-family square-completion units, exceptional contact
vectors, and modulus-special polar discriminants still require the same
invariant check completed above for the balanced rows.

Nothing here proves analytic realization or global effectivity of a marked
tag, a proximity history, an incidence surface, a finite first-leg algebra,
or a polynomial map.  It gives no counterexample and no JC2 conclusion.
The source Cartier different, its strict reduced germs, exceptional
coefficients, target discriminant, conductor, normalization index, physical
places, global primes, and formal lattice vectors remain distinct.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17590`.
- Body SHA-256:
  `ba54edd2f1dc28b6f4222aeb371f7b4f7379863c7db867d14bfcf78cab86d7b2`.
- Frozen basis: `5f285393f481bfb8f8767fa0ad09b1eeeb1d9f91`.
