# Binding integration: quadratic trace-zero basis-change rigidity

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen integration basis: `bbe3a039f85002826f71484b0275a6f28f6647da`  
Lifecycle: **PROMOTED ORBIT THEOREMS / QUADRATIC-BASIS EXISTENCE OPEN**

## 0. Verdict, custody, and charged inputs

This integration binds the transactional producer

```text
b15c7c7db287ddd1b6e0aae8caa48eff9e225d910f9735f9ad9b2ab947ba4f46
  xmodel/bd-a2-quadratic-basis-change-coverage-sol56-20260830.md
  body 16198 / bef1361e4eb32211b857a67290ecf335b2f284d3938023c83dbdb121fe841130
  manifest 473539389e1c03da32685a42e24a7ff1487873906ba59abc56380c8122dfa694
```

to the independent GPT-5.5 xhigh hostile review

```text
e1d038769a86843b099fe0324c5e3f8cdc57a0e028f99036b4f987b018a78204
  xmodel/bd-a2-quadratic-basis-change-coverage-hostile-review-gpt55-20260830.md
  verdict CONFIRM_WITH_CORRECTIONS.
```

The producer was sealed on basis
`f43ee99da2bc9f831d94e403dcd90622e87e8756`, published at
`002d4a88b3496838a3ff8cf3bf55ec5cedbdb5a4`, and reviewed on that exact
publication basis.  The receipt was root-hash-checked before the present
integration basis.  The saturated-graph, constant-frame-action, and
provenance corrections are binding below.

The universal basis-change statements need no proper-block hypothesis.  The
final proper-block affine-linear corollary separately charges

```text
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  proper cubic-block structure;
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  promoted non-Galois and nonmonogenic proper-block theorem.          (0.1)
```

The first file alone does not prove nonmonogenicity and must not be used as a
substitute for the second.

## 1. Exact transformation law and intrinsic data

Let `A=C[u,v]`, let `B` be a finite locally free rank-three `A`-algebra with
free trace-zero module, and let `e=(z,w)` be a trace-zero frame.  Write

```text
Phi_e(X,Y)=bX^3-3aX^2Y+3dXY^2-cY^3.                  (1.1)
```

For another frame `e'=e*g`, `g in GL_2(A)`, the exact law is

```text
Phi_(e')(x)=det(g)^(-1) Phi_e(gx).                    (1.2)
```

It follows directly from `Phi_e(X,Y)=det(t,t^2)` in trace-zero coordinates:
old coordinates are multiplied by `g`, while returning the two determinant
columns to the new frame multiplies by `det(g)^(-1)`.

The induced rank-four coefficient matrix is invertible over `A`; therefore

```text
I_B=(a,b,c,d)                                         (1.3)
```

is frame-invariant.  The trace Gram determinant changes only by the scalar
square `det(g)^2`.  Coefficient maximum degree, the leading infinity cubic,
projective coefficient basepoints, and projective incidence normality are not
intrinsic.

## 2. Leading-section theorem for every nonconstant change

Assume both frames have coefficient maximum at most two.  Write `Phi_d` for
the highest nonzero homogeneous target part, `d<=2`, and `g_m` for the highest
nonzero homogeneous matrix part of a nonconstant `g`, `m>0`.  Constancy of
`det(g)` gives `det(g_m)=0`; the nonzero matrix `g_m` has generic rank one.
The unique term of target degree `d+3m` in `Phi(gx)` is

```text
Phi_d(g_m x),                                         (2.1)
```

and must vanish because the transformed coefficients again have degree at
most two.

Cancel the common factor of a generic image vector of `g_m` and write its
line as `[R:S]`, with coprime homogeneous forms of degree `e`.  This is a
morphism `P1->P1`; its graph ideal `(SX-RY)` is principal and saturated.
Vanishing of `Phi_d` on the graph therefore implies actual divisibility by
`SX-RY`, and bidegrees give

```text
e<=d<=2.                                              (2.2)
```

Thus every nonconstant quadratic-to-quadratic change forces a section
component in the first leading infinity cubic.  Applying the same argument to
`g^(-1)=det(g)^(-1)adj(g)` supplies the kernel-flag section in the other
leading cubic.  Special rank drops and common factors do not create
basepoint exceptions; they are removed before the saturated graph is formed.

For exact quadratic frames, extracting the section leaves only the class
patterns

```text
(0,1)+(2,2),       (1,1)+(1,2),       (2,1)+(0,2),    (2.3)
```

and the residual `(0,2)` splits over `C`, with multiplicity allowed.  These
are presentation-level boundary divisor classes, not reducedness,
realizability, or intrinsic algebra data.

Consequently, if either quadratic presentation has no section component at
infinity, every change to another quadratic trace-zero frame is constant.

## 3. Complete entry-degree-at-most-one classification

Suppose every entry of `g` has degree at most one.  Its constant value is
invertible.  After a constant left normalization write `g=I+L`, with `L`
homogeneous linear.  From `det(I+L)=1`,

```text
tr(L)=0,             det(L)=0.                        (3.1)
```

The image of the linear pencil lies in the nilpotent cone of `sl_2`.  Its
projectivization is a smooth conic containing no projective line, so
`L=p(u,v)N` for one linear form `p` and one fixed nilpotent `N`.  Constant
frame changes act as `g -> C^(-1)gD`; after `g(0)=I`, take `C=D` and conjugate
`N` to an elementary nilpotent.  Hence every genuinely nonconstant case is

```text
g=[[1,-p],[0,1]],       Phi'(X,Y)=Phi(X-pY,Y).         (3.2)
```

The exact expansion is

```text
b'=b,
a'=a+bp,
d'=d+2ap+bp^2,
c'=c+3dp+3ap^2+bp^3.                                 (3.3)
```

For nonconstant linear homogeneous `p`, both coefficient sets have maximum
at most two exactly when

```text
b in C,       a_2=0,
d_2=-a_1p-(b/3)p^2.                                  (3.4)
```

For an arbitrary single elementary shear, `deg(p)>=2` forces `b=0`; for
`deg(p)>=3`, it successively forces `b=a=d=0`.  In the linear case (3.4)
gives the exact dichotomy

```text
b=0:       Phi(1,0)=0, a fixed generic projective root;
b in C^*:  det(z,z^2)=b is a unit, so B=A[z].         (3.5)
```

The first branch contradicts the generic cubic-field condition: a nonzero
trace-zero element with dependent `1,z,z^2` would generate degree at most two.
The second is excluded only by the separately promoted nonmonogenicity in
(0.1).  Therefore:

> In the promoted integral nonmonogenic proper cubic-block scope, every
> entry-degree-at-most-one change between two already existing quadratic
> trace-zero frames is constant.

For an exact quadratic shear satisfying (3.4), the leading infinity cubic has
the fixed double section `Y=0`.  This is not a fixed root of the full affine
generic cubic.

## 4. Exact counterexample to the broader heuristic

Let

```text
B=C[u,v,t]/(t^3-u^2t-v^2).                            (4.1)
```

The monic cubic is irreducible: a rational root would be integral and hence
polynomial, while specialization at `u=0` would give a polynomial cube root
of `v^2`.  Its hypersurface singular locus is only the origin; being a
codimension-one-regular hypersurface, it is normal.  It is finite free of rank
three over `C[u,v]`.

For the trace-zero frame

```text
z=t,        w=t^2-(2/3)u^2,                           (4.2)
```

one obtains

```text
(a,b,c,d)=(0,1,v^2,-u^2/3),
Phi=X^3-u^2XY^2-v^2Y^3.                              (4.3)
```

The nonconstant determinant-one change `z'=z`, `w'=w-uz` gives

```text
(a',b',c',d')=(u,1,v^2,2u^2/3),
Phi'=X^3-3uX^2Y+2u^2XY^2-v^2Y^3.                    (4.4)
```

Both frames have coefficient cap two and unit content.  Neither full cubic
has a constant projective root; both affine and projective incidences are
fibrewise finite; and their intrinsic discriminant is

```text
Delta=4u^6-27v^4.                                    (4.5)
```

Their infinity cubics nevertheless share the fixed double section `Y=0`.
The algebra is monogenic, `B=A[t]`.  Thus nonconstant quadratic-to-quadratic
changes do not generally force a fixed root of the full cubic, nonunit
content, or nonfiniteness.  This example does not contradict the
nonmonogenic proper-block corollary; it proves why that input is load-bearing.

## 5. Exact frontier and firewall

These theorems classify changes **between frames already known to be
quadratic**.  They do not prove that a proper cubic block has such a frame or
that

```text
d_min(B)=min_e max(deg a_e,deg b_e,deg c_e,deg d_e)   (5.1)
```

is at most two.  Discriminant invariance gives only

```text
d_min(B)>=ceil(deg Delta/4),                          (5.2)
```

a lower bound, never an existence theorem.

The exact remaining orbit gap is entry degree at least two:

```text
g in GL_2(C[u,v]), deg(g)>=2,
Phi and det(g)^(-1)Phi(gX,gY) both coefficient-cap two,
generic cubic field and nonmonogenicity.              (5.3)
```

The image/kernel section flags are necessary but do not eliminate (5.3).
An elementary factorization is insufficient: `GL_2(C[u,v])` has
non-elementary phenomena, and intermediate frames need not remain inside the
degree cap.  The smallest successor compares the descending homogeneous bands
for the three factor classes in (2.3), or equivalently studies the associated
elementary transformations at infinity, seeking either a fixed generic root,
a unit value, or a genuine nonmonogenic counterexample.

This integration makes no claim about arbitrary basis existence, higher
coefficient degree, a polynomial map, counterexample, finite-prefix or formal
arc evidence, or JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9386`.
- Body SHA-256:
  `418d6f52b7158098265200abba6b7c0d669b6aab95d78127460ec48e77f049d6`.
- Frozen basis: `bbe3a039f85002826f71484b0275a6f28f6647da`.
