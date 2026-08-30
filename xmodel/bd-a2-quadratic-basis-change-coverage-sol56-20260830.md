# Quadratic trace-zero frames: exact low-degree rigidity and a normal counterexample

Date: 2026-08-30 UTC  
Producer: Sol 5.6 Ultra delegated lane `/root/whole_portfolio_ideation`  
Frozen basis: `f43ee99da2bc9f831d94e403dcd90622e87e8756`  
Lifecycle: **EXACT PROVISIONAL PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint

Let `A=C[u,v]`, let `B` be a finite locally free rank-three `A`-algebra,
and suppose its trace-zero module `E` is free.  In a global trace-zero frame
`e=(z,w)`, write the Miranda binary cubic as

```text
Phi_e(X,Y)=bX^3-3aX^2Y+3dXY^2-cY^3.                 (0.1)
```

This packet studies two frames `e,e'` for which all four coefficients have
total degree at most two.  It does **not** assume that an arbitrary cubic
block has such a frame.

The maximum exact conclusions are:

1. If `e'=e*g`, with `g in GL_2(A)`, then

   ```text
   Phi_(e')(x)=det(g)^(-1) Phi_e(gx).                 (0.2)
   ```

   Formula (0.2), or its four polarizations, is a complete exact criterion
   for a polynomial change to carry one quadratic coefficient quadruple to
   another.

2. For an arbitrary nonconstant `g`, let `g_m` be its highest homogeneous
   matrix.  The image line of the generic rank-one matrix `g_m` defines a
   rational section of `P1 times P1`, and that section is a component of the
   leading infinity cubic of `Phi_e`.  Its degree is at most two.  Applying
   the same statement to `g^(-1)` gives a section component of the other
   leading infinity cubic.  Thus a nonconstant quadratic-to-quadratic change
   is possible only between boundary-reducible presentations.

3. If every entry of `g` has degree at most one, then, up to constant changes
   of the two frames, every genuinely nonconstant `g` is one elementary
   shear.  The bounded-to-bounded orbit is classified explicitly in Section
   4.  It always has either a fixed generic root or a unit value in a
   constant fibre direction.  Therefore, for an integral cubic-field algebra
   satisfying the promoted proper-block nonmonogenicity obstruction, every
   affine-linear change between quadratic frames is constant.

4. The broader heuristic "nonconstant change forces a fixed root of the full
   generic binary cubic, nonunit intrinsic content, or nonfiniteness" is
   false.  Section 5 gives two nonconstant
   quadratic frames of a normal finite integral cubic algebra, with intrinsic
   content ideal `A`, finite affine and projective incidence, and no constant
   projective root.  The algebra is monogenic.  This is exactly why the
   nonmonogenic proper-block hypothesis is load-bearing.  A correctly typed
   boundary version does survive: Sections 2 and 4 force a section component,
   and in the affine-linear case a fixed double section, in the leading
   infinity cubic.

5. None of these orbit statements proves existence of a quadratic frame.
   The intrinsic minimum coefficient degree, existence of some degree-two
   frame, and invariance of the trace discriminant remain three distinct
   assertions.

## 1. Transformation law and the exact arbitrary-matrix criterion

For `t=Xz+Yw`, the trace-zero coordinates of `t` and `t^2` satisfy

```text
det(t,t^2)=Phi_e(X,Y).                                (1.1)
```

If `e'=e*g`, then the old coordinates of an element with new coordinate
column `x` are `gx`.  Passing the two trace-zero coordinate columns back to
the new frame multiplies their determinant by `det(g)^(-1)`.  This proves
(0.2).  Since

```text
det(g) in A^*=C^*,                                   (1.2)
```

the determinant twist never affects coefficient degree.

Let `T_Phi` be the symmetric trilinear polarization normalized by
`T_Phi(x,x,x)=Phi(x)`, and let `x,y` be the two columns of `g`.  If the new
coefficients are `a',b',c',d'`, then (0.2) is equivalently

```text
b'  = det(g)^(-1) Phi(x),
a'  =-det(g)^(-1) T_Phi(x,x,y),
d'  = det(g)^(-1) T_Phi(x,y,y),
c'  =-det(g)^(-1) Phi(y).                            (1.3)
```

Thus, for arbitrary `g`, both frames have coefficient cap two if and only if
the four polynomials in (1.3) do.  This is a literal characterization, but
not yet a structural classification of all polynomial matrices satisfying
the cancellations.

The rank-four representation in (0.2) and its inverse both have entries in
`A`.  Consequently the coefficient-content ideal

```text
I_B=(a,b,c,d)                                         (1.4)
```

is unchanged.  Independently, changing the full algebra basis by
`diag(1,g)` changes the trace Gram determinant by `det(g)^2`; hence the trace
discriminant is unchanged up to `C^*`.  These are intrinsic.  The maximum
coefficient degree of one frame, its leading infinity cubic, its coefficient
basepoints at infinity, and the normality of its chosen projective incidence
are not intrinsic.

## 2. The leading-section theorem for an arbitrary nonconstant change

Write

```text
Phi=Phi_0+Phi_1+...+Phi_d,       0<=d<=2,             (2.1)
g=g_0+g_1+...+g_m,              m>0,                 (2.2)
```

where subscripts denote homogeneous target degree and the last terms are
nonzero.  Because `det(g)` is constant, the degree-`2m` term of its
determinant vanishes:

```text
det(g_m)=0.                                           (2.3)
```

Over `C(P1)` the nonzero matrix `g_m` therefore has rank one.  Its image is
a rational line `L` in the fibre two-space.

The unique term of degree `d+3m` in `Phi(gx)` is

```text
Phi_d(g_m x).                                        (2.4)
```

Since `d+3m>2` and the transformed coefficients have degree at most two,
(2.4) vanishes identically.  As `g_m x` spans `L`, the cubic `Phi_d` vanishes
on `L`.

Choose coprime homogeneous forms `R,S` of the same degree `e` representing
the resulting map

```text
r:P1_target-infinity -> P1_fibre,       r=[R:S].      (2.5)
```

The graph of `r` is the irreducible divisor

```text
S(U,V)X-R(U,V)Y=0.                                   (2.6)
```

Equation (2.4) says that (2.6) divides the bihomogeneous polynomial `Phi_d`.
Comparing target degrees gives

```text
e<=d<=2.                                             (2.7)
```

This proves:

> **LEADING-SECTION.**  Every nonconstant polynomial change between two
> coefficient-cap-two frames forces the leading infinity cubic in the first
> frame to contain a section of bidegree `(e,1)`, `e in {0,1,2}`.

For an actual quadratic frame (`d=2`), the boundary factorization is
therefore restricted to the three class patterns

```text
(0,1)+(2,2),
(1,1)+(1,2),
(2,1)+(0,2).                                         (2.8)
```

The last residual `(0,2)` splits over `C` into two constant sections,
counted with multiplicity.  Formula (2.8) is only a divisor-class routing
statement; it does not assert reducedness, normality, physical attachment
counts, or realizability by a proper block.

Since `g^(-1)=det(g)^(-1) adj(g)` has the same entry degree `m`, the same
argument applies in the other direction.  Generically,
`im(adj(g_m))=ker(g_m)`, so the two forced section flags are the image and
kernel flags of the top matrix.

This theorem is stronger than a mere discriminant constraint: if either
leading infinity cubic has no section component, then every
quadratic-to-quadratic basis change is constant.  It is also weaker than the
heuristic under test.  The forced root belongs to the **top homogeneous
boundary cubic**.  It can move with `[U:V]`; it need not be a fixed root of
the full generic binary cubic, create affine coefficient content, or make the
affine incidence nonfinite.

## 3. Every affine-linear unimodular matrix is a constant conjugate of a shear

Assume every entry of `g` has degree at most one.  Its constant value `g(0)`
is invertible because its determinant is a nonzero constant.  After a
constant left multiplication, write

```text
g=I+L(u,v),                                           (3.1)
```

with `L` homogeneous linear.  Separating degrees in `det(I+L)=1` gives

```text
tr(L)=0,                 det(L)=0.                    (3.2)
```

Thus the image of the linear pencil `L` lies in the nilpotent cone in
`sl_2`.  Projectivizing that cone gives a smooth conic in `P(sl_2)`, which
contains no projective line.  Hence the coefficient matrices of `u` and `v`
in `L` span at most one dimension:

```text
L=p(u,v)N,              N^2=0,                       (3.3)
```

where `p` is a nonzero linear form and `N` is a fixed nonzero nilpotent
matrix.  A constant conjugation carries `N` to an elementary matrix.  After
constant changes of the old and new frames, and absorbing a sign into `p`,
we may therefore take

```text
g=[[1,-p],[0,1]],          Phi'(X,Y)=Phi(X-pY,Y).     (3.4)
```

Constant frame changes preserve the coefficient cap, existence of a fixed
constant fibre root, and monogenicity.  Thus (3.4) loses no relevant case.

## 4. Exact bounded orbit of one polynomial shear

For (3.4), direct expansion gives

```text
b'=b,
a'=a+bp,
d'=d+2ap+bp^2,
c'=c+3dp+3ap^2+bp^3.                                (4.1)
```

First let `p` be nonconstant linear, with its constant part absorbed by a
constant shear.  Write `q_i` for the homogeneous degree-`i` part of a
coefficient.  Requiring both sides of (4.1) to have degree at most two is
equivalent to

```text
b in C,
a_2=0,
d_2=-a_1*p-(b/3)*p^2,                                (4.2)
```

with `a_0,a_1,d_0,d_1,c_0,c_1,c_2` otherwise arbitrary.  Necessity follows
band by band.  The degree-three part of `a+bp` first gives `deg(b)<=1`; the
degree-three part of `d+2ap+bp^2` gives
`2a_2+b_1p=0`; and the degree-four part of `c'` is then
`-(1/2)b_1p^3`, so `b_1=0` and `a_2=0`.  Its remaining degree-three part is
exactly the last equation in (4.2).  Conversely (4.2) makes every term of
degree greater than two in (4.1) vanish.

There are only two possibilities:

```text
b=0:       Phi(1,0)=0, so the generic cubic has a fixed root;
b in C^*:  Phi(1,0)=b is a unit, so det(z,z^2) is a unit and B=A[z]. (4.3)
```

Thus an integral cubic-field algebra that is not monogenic admits no
genuinely nonconstant affine-linear change between quadratic frames.
The campaign corollary charges the binding nonmonogenic proper-block client

```text
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md.
```

All preceding orbit statements themselves are universal algebra over
`C[u,v]` and do not charge that client.

The same dichotomy holds for a single elementary shear with an arbitrary
nonconstant `p`.  If `deg(p)>=3`, the first three equations of (4.1)
successively force `b=a=d=0`.  If `deg(p)=2` and `b!=0`, degree comparison
first forces `b` constant and
`a_2=-(b/2)p_2`; the degree-six part of `c'` is then
`-(1/2)b p_2^3`, a contradiction.  Hence `b=0` whenever `deg(p)>=2`.
For `deg(p)=1`, (4.2)--(4.3) apply.

For an actual quadratic frame, (4.2) also shows that the leading infinity
cubic has the fixed double section `Y=0`:

```text
Phi_2=Y^2*(3d_2 X-c_2 Y).                            (4.4)
```

This is presentation-level nonreduced infinity, not a fixed root of the full
affine generic cubic.

## 5. A normal finite counterexample to the broad heuristic

Take `A=C[u,v]` and

```text
B=A[t]/(t^3-u^2t-v^2).                               (5.1)
```

The cubic is irreducible over `C(u,v)`.  Indeed a rational root of the monic
cubic would be integral over the integrally closed ring `C[u,v]`, hence a
polynomial root.  Specializing such a root at `u=0` would give a polynomial
root of `T^3-v^2`, which is impossible.

The only singular point of the hypersurface (5.1) is `(u,v,t)=(0,0,0)`:

```text
f_t=3t^2-u^2,          f_u=-2ut,          f_v=-2v.   (5.2)
```

Thus the integral hypersurface is regular in codimension one and
Cohen--Macaulay, hence normal.  It is visibly finite free of rank three over
`A`.

Put

```text
z=t,                     w=t^2-(2/3)u^2.             (5.3)
```

Both have trace zero.  In this frame the Miranda tuple and cubic are

```text
(a,b,c,d)=(0,1,v^2,-u^2/3),
Phi=X^3-u^2XY^2-v^2Y^3.                              (5.4)
```

Change to `z'=z`, `w'=w-uz`.  This is the nonconstant determinant-one matrix
in (3.4), and

```text
(a',b',c',d')=(u,1,v^2,2u^2/3),
Phi'=X^3-3uX^2Y+2u^2XY^2-v^2Y^3.                    (5.5)
```

Both coefficient quadruples have maximum degree two.  Both content ideals
are `A` because `b=b'=1`.  Neither cubic has a constant projective root: in
(5.4) the coefficient of `v^2` forces `Y=0`, after which the `X^3` term is
nonzero; the same argument applies to (5.5).  Their affine incidence is
finite, and their leading coefficient vectors have no common zero on target
infinity because `u^2` and `v^2` do not vanish simultaneously on `P1`.
Thus even the projective incidence is fibrewise finite.

The common intrinsic discriminant is

```text
Delta=4u^6-27v^4.                                    (5.6)
```

The two infinity cubics are nevertheless nonreduced:

```text
Phi_2 =-Y^2(u^2X+v^2Y),
Phi'_2= Y^2(2u^2X-v^2Y).                             (5.7)
```

Most importantly, this normal finite counterexample is monogenic:
`B=A[z]`.  It violates fixed-full-root, content, and nonfiniteness versions
of the heuristic, but not the strengthened proper-block dichotomy (4.3).

The still simpler variant over `C[u,v]` obtained by replacing `-v^2` with
`+1` gives `t^3-u^2t+1`, discriminant `4u^6-27`, and a smooth normal total
space; it has a projective coefficient basepoint at one infinity direction.
Example (5.1) is preferable because it removes that distraction.

## 6. What this buys, and what remains uncovered

Define the intrinsic minimum

```text
d_min(B)=min over global trace-zero frames
         max{deg(a),deg(b),deg(c),deg(d)}.            (6.1)
```

The results above concern the transition groupoid among frames already lying
in the sublevel set `d<=2`.

They buy three exact reductions:

1. If one quadratic presentation has a leading infinity cubic with no
   section component, it is unique up to constant frame change among all
   quadratic presentations.
2. In the proper-block integral and nonmonogenic scope, it is enough to search
   for genuinely new quadratic frames through matrices of entry degree at
   least two; affine-linear changes add no new presentations.
3. Every remaining nonconstant change supplies two explicit boundary section
   flags, of degrees at most two, from `im(g_m)` and `ker(g_m)`.  These can be
   routed into the already developed bidegree-`(2,3)` boundary classifications
   without treating them as intrinsic algebra data.

They do **not** prove `d_min(B)<=2`.  When the trace discriminant is nonzero,
trace-discriminant invariance only gives

```text
deg(Delta)<=4d for a displayed degree-d frame,
d_min(B)>=ceil(deg(Delta)/4).                         (6.2)
```

This is a lower bound, never an existence theorem.  Likewise the intrinsic
content orders give lower bounds on `d_min`, not upper bounds.  A proof that
every hypothetical proper cubic block admits some quadratic frame requires a
new input controlling multiplication-table growth, a canonical lattice at
infinity, or a reduction algorithm whose intermediate polynomial frames stay
global and unimodular.

The sharp next bounded problem is the entry-degree-at-least-two orbit:

```text
classify g in GL_2(C[u,v]) with deg(g)>=2 for which
Phi and det(g)^(-1)Phi(gX,gY) both have coefficient cap two,
under generic irreducibility and nonmonogenicity.     (6.3)
```

The leading-section theorem restricts (6.3) to section-containing infinity
types, but does not prove they are empty.  Factoring `g` into elementary
matrices is not by itself a proof: `GL_2(C[u,v])` has non-elementary phenomena,
and even an elementary factorization need not keep the intermediate cubic
inside the degree-two cap.  A safe successor is a valuation-at-infinity or
ruled-surface elementary-transformation classification, with the section
flags in Section 2 as the first invariant.

All statements here are algebraic theorems or explicit exact examples.  No
finite-prefix evidence, formal arc evidence, heavy local CAS, AWS result,
polynomial Keller map, counterexample to JC2, or arbitrary cubic-block closure
is claimed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16198`.
- Body SHA-256:
  `bef1361e4eb32211b857a67290ecf335b2f284d3938023c83dbdb121fe841130`.
- Frozen basis: `f43ee99da2bc9f831d94e403dcd90622e87e8756`.
