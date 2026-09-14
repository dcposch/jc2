# R050 parent-residue pilot: one physical place, four coefficient equations, and the full-Jacobian redundancy

Date: 2026-09-06. Author: Astra, delegated residue pilot.
Basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
Evidence: elementary characteristic-zero derivations and exact symbolic checks.
Lifecycle: PRODUCER-CHECKED; no promotion or configuration exclusion is asserted.

## Result

The R050 degree-56 member has a particularly accessible final-major infinity
place. Its physical ramification degree is **4**, not the 28 of the other
major place and not the number of displayed cover series. In the local chart

```
x = u^-4,
y = u^-4 + c0 + alpha*u + beta*u^2 + u^3*v,    alpha != 0,
f = H(u,v) = A*v+B + u*H1(v) + O(u^2),        A != 0,
```

the genuine generic-fibre residue is

```
Res_P(dx/f_y) = (4/A^2) H1'((T-B)/A),   on f=T.
```

The R050 face bound proves `deg H1 <= 4`. Therefore vanishing identically in
the generic parameter T is equivalent to **H1 being constant**, four explicit
coefficient equations. This is coefficient information, not another divisor
count. A 19-term polynomial family of degree 56 below preserves the displayed
top, D2 and final-major faces and has residue
`epsilon/(kappa^2*(1-a)^2)`, proving that those faces alone do not imply the
condition.

The exact limitation is equally explicit: these equations are consequences
of the FULL constant-Jacobian ideal. If the mate has the licensed expansion
`g=b/u+G0(v)+...`, then `[u^-1] J_{u,v}(f,g)=b*H1'(v)`. No independence from
the full source chart is claimed. No R050 row is killed, and the displayed
family is not a full R050 source-tree realization or a Keller pair.

## 1. Inputs and notation

I read APPROACHES and the completed coordinator synthesis, Sol's sealed
Q2.A proposal, the sealed KELLER-PENCIL-GENUS report, the original exact-contact
report, and its superseding Astra gate. The four external report hashes were
checked against their terminal receipts; the coordinator synthesis passed
`artifact_finalize.py verify`. No live report, fleet, or `jc2-lean` was used.

Use **f for the smaller degree-56 member** and **g for the degree-196 mate**,
as in Xu and the exact-contact gate. Put
`J(f,g)=f_x*g_y-f_y*g_x=j`. Then on `f=T`,

```
omega_f = dx/f_y = -dy/f_x,      dg = -j*omega_f.
```

Thus this tests the same parent mechanism as Sol Q2.A, with the generic member
swapped and the sign recorded. T remains transcendental throughout.

The accepted numerical input is the pinned R050 pattern in
`xmodel/exact-contact-gate-astra-20260906.md`, section 4, not the producer's
refuted sibling search. Its final majors are four discs, each containing
eight f-root series, at delta `19/28`. At D2 the reduced pattern is
`pi*(pi^4-c1)^4*(pi^4-c2)`, with distinct nonzero c1,c2. The f leading form at
D2 is its square. On a final major disc,

```
lambda_f = -1/14,       lambda_g = -1/4,
lambda_f + lambda_g + 1 = 19/28.
```

Xu's root-derivative formula and Lemma 4.4 are directly visible in
`box/exact-contact-gate-20260906/xu.txt`, pp.3-4. They give
`ord_t f_y = lambda_f-delta = -3/4` at a simple final-major root.

## 2. The actual physical place and the ring map

Work first over any algebraically closed field k of characteristic zero
containing a specialization of the necessary source coefficients. The same
coefficient formulas work over a parameter ring after the displayed leaders
are inverted; a field specialization is used when speaking about a place.

After placing the major direction at y=x, the D1 centre has the form

```
eta = t^-1+c0+alpha*t^(1/4)+beta*t^(1/2),    alpha != 0.
```

The coefficients are independent of T: before the final-major level the
orders of f are negative, so subtracting the constant T changes no such
centre coefficient. Set t=u^4. The increment denominator from D2 to D1 is
7. The squarefree final f-face of degree 8 consequently has shape
`C*pi*(pi^7-d)`, with `C*d != 0`: seven nonzero roots and one simple zero.

The **zero** root has no nonzero `t^(19/28)` coefficient. Its four conjugate
series have the already nonzero `alpha*t^(1/4)` term. The polynomial implicit
function argument below constructs the complete series in k(T)[[u]]; no
later denominator is required. The coefficient alpha excludes a smaller
cover. Thus the deck orbit has four series and defines one physical
normalization place P, with x-pole degree e=4.

For comparison, the seven nonzero roots in each of the four conjugate D1
discs have a nonzero `t^(19/28)` term. Simple-root Hensel lifting introduces
no larger denominator, so their 28 series form the other physical major
place, of e=28. This comparison is not used as a substitute for the explicit
place map at P.

Write z=y-eta. The D1 floor says that every nonzero Laurent coefficient term
`u^i*z^q` of `f(u^-4,eta+z)` satisfies

```
i + (19/7)q >= -2/7.
```

The integers i are essential. Substitute z=u^3*v. The new exponent is
`N=i+3q >= ceil((2q-2)/7)`. In particular, there are no negative powers of u;
the u^0 coefficient has degree at most one in v, and the u^1 coefficient has
degree at most four. The simple zero of the final face makes the linear
coefficient A nonzero. This proves the asserted H expansion and degree bound.

In a source parameter ring R, impose these literal coefficient/floor rows
and invert A and alpha. The source map is

```
R[x,y] -> R[u,u^-1,v],
x |-> u^-4,
y |-> u^-4+c0+alpha*u+beta*u^2+u^3*v.
```

The generic-fibre equation becomes `H(u,v)=T`. Since H_v(0,v)=A is a unit,
there is a unique formal solution
`v(u) in R[A^-1,T][[u]]`, with `v(0)=(T-B)/A`.
For a field specialization the evaluation map to k(T)((u)) has the prime
kernel selecting this curve branch; the induced valuation on its function
field is the physical place just identified. One does not map the entire
possibly reducible generic curve injectively into a field without selecting
that component.

## 3. The residue and its precise dependence on source coefficients

At fixed x (hence fixed u), `f_y=u^-3*H_v`. Also `dx=-4*u^-5 du`. Therefore

```
omega_f = -4*u^-2/H_v(u,v(u)) du,
H_v(u,v(u)) = A + u*H1'((T-B)/A) + O(u^2).
```

Taking the reciprocal proves the residue formula. If
`H1=h0+h1*v+h2*v^2+h3*v^3+h4*v^4`, its vanishing for the generic T is
equivalent to `h1=h2=h3=h4=0`. Substituting a numerical fibre first would
lose this equivalence.

These coefficients are computable without a Puiseux expansion past the
first implicit step: expand the actual source polynomial under the displayed
ring map only through u^1. The centre and leader must be genuine source
coordinates or justified algebraic extensions. Matching receiver variable
names is not such a map.

At any final minor place, the squarefree order-zero face instead gives
`ord_u omega_f=e*(delta-1)-1 >= 0`, since delta>1 and the order is an integer.
Its residue is automatically zero. The minor contact counts therefore do
not supply further residue equations at this stage.

## 4. A polynomial family showing independence from the displayed faces

Let `a*kappa*(a-1) != 0`, let epsilon be free, and define in k[x,y]

```
w = y-x,
q = y*w^4-1,
r = y*w^4-a,
f_epsilon = r^2 * (y^4*w^2*q^8 - kappa*y*w^2*q + epsilon*y*w^3*q).
```

This has degree 56 and top form `y^14*(y-x)^42`. There are 19 expanded
monomials in the linear coordinates (y,w).

At D2, set `x=u^-4, y=u^-4+pi*u`. The u^-14 face is exactly

```
pi^2*(pi^4-1)^8*(pi^4-a)^2,
```

the square of the R050 pattern. At the selected final major disc, set
`x=s^-28, y=s^-28+s^7+pi*s^19`. The s^-2 face is exactly

```
(1-a)^2*((4*pi)^8-4*kappa*pi).
```

It is squarefree with a simple zero and a seven-element nonzero orbit. Both
faces and the top form are independent of epsilon. On the zero branch put
`x=u^-4, y=u^-4+u+u^3*v`. Direct polynomial expansion gives

```
H0 = -4*kappa*(1-a)^2*v,
H1 =  4*epsilon*(1-a)^2*v,
Res_P(omega_f) = epsilon/(kappa^2*(1-a)^2).
```

The implicit-function map keeps T generic and proves that P is an actual
physical infinity place of the generic fibre of this polynomial, not a
decorative face flag. Epsilon=0 and epsilon!=0 have exactly the same displayed
faces and different residues. This establishes nonredundancy **only on those
displayed faces**.

The family is deliberately not offered as an R050 source realization: it
has factors and unverified data at other places, and no polynomial mate is
provided. Its role is the local-face countercontrol. Neither the complete
R050 source equations nor their realizability follow from these three faces.

## 5. Why the full source Jacobian already implies these equations

For an actual R050 mate, the g face floor is
`i+(19/7)q >= -1`. After z=u^3*v, the only negative power is

```
g = b/u+G0(v)+u*G1(v)+...,    b != 0.
```

The coefficient b is nonzero because the simple zero of the final f-face
is not a zero of the final g-face. Differentiating in the literal (u,v) ring,

```
[u^-2] J_{u,v}(f,g) = A*b,
[u^-1] J_{u,v}(f,g) = b*H1'(v).
```

But the source-coordinate determinant is `J_{u,v}(x,y)=-4*u^-2`, so the
constant-Jacobian equation requires `J_{u,v}(f,g)=-4*j*u^-2`. Thus
`A*b=-4*j` and `b*H1'=0`; b is already a unit on this face stratum.

More explicitly, `b*H1'=-4*[u^1] J_{x,y}(f,g)` after the source substitution.
This is an algebraic combination of the nonconstant source-Jacobian
coefficient rows. It is not an additional independent hypothesis beyond the
full parent system. It might be useful as a short elimination/projection
constraint before constructing a large system, but no speed gain or new
exclusion has been measured here.

The roster's 1,392-variable child receiver is not a substitute for the
source map in section 2. The residue of its untwisted differential can be
nonzero. A reverse embedding into source coordinates, or retention of the
twisted primitive with its extension data, would have to be supplied.

## 6. Required controls and the previous pencil report

**Positive automorphism.** `(f,g)=(y+x^2,-x)` has J=1 and polynomial inverse
`x=-g, y=f-g^2`. On f=T, `omega_f=dx`, with zero residue at infinity;
`dg=-omega_f`, as the sign convention requires.

**Mandatory negative control.** Put `h=x+x^2*y`. There are no affine critical
points: `(1-2xy)h_x+4y^2 h_y=1`. On h=T with T nonzero,

```
y=(T-x)/x^2,    omega_h=dx/x^2=d(-1/x).
```

Both residues vanish. At h=0 the two components are disjoint: x=0 and xy=-1.
On the first, use `omega_h=-dy/h_x=-dy=d(-y)`; on the second use
`dx/x^2=d(-1/x)`. Thus even every individual fibre, not just the generic
one, carries a regular primitive.

Nevertheless no polynomial p satisfies `J(p,h)=j!=0`. Substituting
`y=(T-x)/x^2` gives `A(T,x) in k[T,x,x^-1]` with
`partial_x A=j/x^2`. Hence `A=-j/x+C(T)` with C polynomial in T. Returning
to k(x,y), `p=-j/x+C(h)`. Multiplication by x followed by x=0 gives `0=-j`.
The obstruction is global polynomial extension of the primitive.

**Twisted receiver, with a corrected exponent.** For ell>=1 take

```
Q=gamma*pi,    P=gamma^ell/ell.
J(P,Q)=gamma^ell,
omega_Q=d gamma/gamma,    residues at 0,infinity = +1,-1,
gamma^ell*omega_Q=dP.
```

Sol Q2.A prints `P=gamma^(ell+1)/(ell+1)`. Its Jacobian is actually
`gamma^(ell+1)`. The repaired P above proves the intended contrast.

KELLER-PENCIL-GENUS section 2 correctly identifies its divisor **count**
with Riemann-Hurwitz once an actual mate exists. The present coefficient
calculation does not improve that count. Its section 2.3 also says a mate
exists iff the form is exact on every fibre, while adding the caveat
**"algebraicity is the residual"**. The negative control shows why that
caveat is indispensable: independent fibre primitives do not give a global
polynomial mate. Read the exact iff sentence as an unresolved globalization
step unless a compatible extending primitive is assumed. No broader
historical theorem or campaign result is reclassified by this report.

## 7. Verification, retained evidence, and disposition

Run `python3 box/r050-parent-residue-20260906/check.py`. The exact SymPy checks
pass in under one second here: degree/top, both face extractions, the generic
T residue, the degree-four bound, the full-Jacobian coefficient identity,
the positive automorphism, the negative control, and the corrected twisted
example for ell=1,...,5. No modular or numerical computation is consumed.
An initial structural-equality assertion needed polynomial expansion; no
mathematical formula changed.

Checked file SHA-256 values:

```
9866819ac6977dd9f5287c4ccf9f582e65b41fb3304857108e6feba4bcc52370  box/r050-parent-residue-20260906/check.py
23fd5cca53b615f3d93b0fd4b1126a26916c7ea493523e4d2ed8bbd9808f13b7  xmodel/ideation-20260906T0000Z-sol56.md
5d2723e36476903392fd79b3791d1bd9830a0dea6f4693070ae8f89ccc06d6e1  xmodel/keller-pencil-genus-opus5-20260902.md
cd0880f0a7c4122118f59e330f60830f9b2d772762ec346a970138858a62cedf  xmodel/exact-contact-gate-astra-20260906.md
59c3def135e7bb701e118736de9d7a2cafc608b0873c8a570cb0d65941cd173c  box/exact-contact-gate-20260906/xu.txt
fa34c4559974e5b6bfb5fef29b4c5485fcefeb4d53e5aee8a091ea6bd149207c  xmodel/coordinator-strategy-synthesis-astra-20260906.md
```

Disposition: **EXACT LOCAL RESIDUE CONSTRAINT; INDEPENDENT OF THE DISPLAYED
FACES; REDUNDANT ON THE FULL CONSTANT-JACOBIAN CHART; NO CONFIGURATION KILL.**
The pilot supplies a concrete source coefficient projection. Any next claim
of nonredundancy must name the exact intermediate parent ideal and retain
the map and units above. Repeating the numerical contact census or computing
an untwisted child residue does not answer that question.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13561`.
- Body SHA-256:
  `ac05d3338ac15c42c2cde80d3f9d3162e022e9fd9da0e8664904eaf163ad0b83`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
