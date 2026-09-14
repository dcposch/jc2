# Uniform K16 X-emptiness attempt: exact reductions and remaining obstruction

Author: Astra subtask `/root/uniform`, 2026-09-05.

**Verdict: OPEN uniformly.** No uniform cofactor identity, elimination resultant,
valuation argument, or closed descent in the marked category was established.
The notes below give an additional exact, degree-independent differential
presentation and identify a literal defect in the simplest suggested second
descent. Neither is promoted to an emptiness theorem. The primary agent owns
the finite-index calculations and their final verdict.

Only the charged frozen reports in `/tmp/jc2-lane.Fz7unY/inputs` were used as
internal mathematical sources; the primary agent verified their hashes before
delegation. No ledger, jc2-lean, or uncharged ideation source was read or edited.
The short algebra checks used foreground `stdbuf -oL python3`, one core, and
finished. There is no running subtask process.

## 1. The t=2 control has to say X is empty

Frozen `ideation-20260905T1200Z-astra.md`, Sections 2.2 and 2.4, says both that
`U = G_m × X` and that the full slice and its two charts are UNIT on both t=2
factors. Frozen `k16-f3abel-astra-20260905.md`, Sections 5 and 8, explicitly
corrects the negative control: on t=2, d=-1, y=1/5, it is V0 that fails, while
the product B eta is forced to vanish. Thus requiring this X to be nonempty
on that fibre conflicts with the named equations and reduction. The actual
exceptional family is

```
C=x,
W=-25*x^5/4+(5*b/2)*x^2,
B=eta=0,
b arbitrary.
```

It is outside U and X because each localization makes B invertible. Its
positive-dimensionality cannot be used as a NONUNIT control for X.

## 2. A t-independent polynomial differential equation

Use `N=t+1`, so `q=2N-1`. Avoid overloading the slice determinant H by naming
the differential factor `Hdiff`. Starting from the charged RC1-RC2 identity,
put

```
L = K/y = x^2*C/y-b,
P = x*W-b^2/4,
Hdiff = 2*x*P'-3*P-B*x+(3/2)*L*(L+b),
Rfree = (3/16)*L^2*(L*(L+2*b)-4*B*x)
        -eta*x^2*(b*L/2+B*x).
```

Then the full Abel equation is exactly

```
P*Hdiff = Rfree.                                      (UF)
```

All coefficients in (UF) are rational constants: y and t have disappeared
from the differential equation. They occur only in the degree and leading
coefficient constraints. The initial jets are

```
L(0)=-b,    L'(0)=0,
P(0)=-b^2/4,    P'(0)=-B,    P''(0)=2*eta.              (UJ)
```

The complete normalization is

```
deg L=N,    lc(L)=1/y,
deg P=2*N,  lc(P)=omega,
3*d^2=N,
omega*y^2=1/(4*(2*d+1)).                              (UL)
```

Conversely, (UJ) makes

```
C=y*(L+b)/x^2,
W=(P+b^2/4)/x
```

polynomials with the prescribed constant/linear jets. The leading conditions
make C monic of degree t-1 and W normalized of degree 2t+1. Substitution into
the charged polynomial identity gives `x^2*F=P*Hdiff-Rfree`. Multiplication by
x is injective in any coefficient ring's polynomial ring, so the equation is
equivalent scheme-theoretically; it is not merely an equivalence on reduced
points or away from x=0. This last fact also keeps all root collisions.

The new form follows by replacing `K` with `y L` in RC1:

```
3*K*(K+yb)/(2*y^2) = (3/2)*L*(L+b),
Q = y^2*(L*(L+2*b)-4*B*x),
J_RC = b*L/2+B*x.
```

No variable denominator is introduced. A direct exact symbolic expansion,
with W,W',C,b,B,eta,y,x independent and y inverted, checked

```
x^2*F-(P*Hdiff-Rfree)=0.
```

This formulation makes an especially compact single uniform residual:

> There is no polynomial pair P,L over an algebraically closed field of
> characteristic zero satisfying (UF), (UJ), and (UL) for any N>=4 and either
> d, with eta=B nonzero.

That statement is exactly the slice target, not a weaker support theorem.
It remains open in these notes.

### The leading comparison remains consistent at every N

Let `a=lc(L)` and `p=lc(P)/a^2`. The top coefficient of (UF) is

```
(4*N-3)*p^2+(3/2)*p-3/16=0.                           (UT)
```

With `N=3*d^2`, the selected solution is

```
p=1/(4*(2*d+1)).
```

Exact substitution checks (UT). Thus removing t from the differential
equation does not produce a degree contradiction: the required leading
ratio solves the top equation for each index and factor. To finish through
(UF), one must classify its polynomial solutions with all the linked jets.
No assertion that a generic Abel equation of the same degrees is impossible
is made.

### The exceptional proportional-square family in this form

At t=2, d=-1, y=1/5, the exceptional family becomes

```
L=5*x^3-b,
P=-L^2/4,
B=eta=0.
```

This is an exact explanation of the boundary rather than an omitted chart.
More generally, when B=eta=0 and P=-L^2/4, expansion of (UF) gives

```
P*Hdiff-Rfree = L^3*(x*L'-3*L-3*b)/4.                 (US)
```

Over a field, nonzero L therefore forces
`x*L'=3*(L+b)`, hence `L=a*x^3-b`. This proportional-square family has degree
N=3, i.e. t=2. If b is nonzero and P is proportional to L^2 at all, the
constant jet already forces its proportionality factor to be -1/4. This
classification concerns the proportional-square locus only; no argument
here forces an arbitrary solution onto that locus.

## 3. Why the elementary degree descent does not close

An obvious degree-lowering attempt is to remove a linear factor of C and
two degrees from W. At the marked origin, B is a unit on the target, so

```
W(0)=-B != 0.
```

In particular W cannot be divided by x^2, even on the stratum `C=x*Ctilde`.
The canonical polynomial substitute is instead

```
W=-B+eta*x+x^2*V,    deg V=2*t-1.
```

After this substitution, `F/x^2` is polynomial: the constant and linear
coefficients of F vanish identically by the marked jets. Its coefficient
of V' is exactly

```
2*x^3*V+2*eta*x^2-2*B*x-b^2/2.                       (UD)
```

This was checked directly over Q with independent symbols. The same Abel
category at t-1 would require a V' coefficient of the form
`2*x*V-b_new^2/2`. To obtain the coefficient of xV from (UD), division by
x^2 yields

```
2*x*V+2*eta-2*B/x-b^2/(2*x^2).
```

The pole `-2B/x` is present on the entire target, including b=0. Consequently
this literal truncation does not define a polynomial Abel equation of the
same category. A successful second descent would need a different
transformation, or a larger marked rational category with a proved return
to polynomiality, and would have to track these terms. Decreasing the
displayed degree of V alone is not a closed induction.

The same issue appears at other C roots in a different form. The charged
RC9 bound says

```
deg gcd(C,P*Hdiff)<=3   on B*eta != 0.
```

In particular `deg gcd(C,P)<=3`. Thus for t>=5 the whole degree-(t-1)
polynomial C cannot divide P. A proposed global root removal which assumes
that divisibility is false on the target. On repeated-root fibres the
correct bound counts gcd multiplicity; it does not assert the existence
of a distinct root outside the exceptional locus. A root can remain in C
with excess multiplicity even when the gcd has small degree.

This is a defect of the stated simple transformations, not a proof that
every conceivable marked descent is impossible.

## 4. Local and infinity arguments still leave polynomial truncation

The new form does not evade the charged local obstruction. At b=0 and
B nonzero, prescribing C and the marked jets yields a unique formal W:
the coefficient of w_n in the x^n residual is `-(2*n-1)*B`, a unit for
n>=2. In particular, when C has a zero at the origin, the initial
unforced coefficients are

```
w2=eta^2/(3*B),
w3=4*eta^3/(15*B^2).
```

They are nonzero on the target. They show why subtracting two jets is
natural, but also why local consistency cannot prove emptiness: the
formal series exists before polynomial truncation is imposed. For b
nonzero the charged recurrence instead has the unit diagonal
`(1-n)*b^2/2` on w_(n+1), with w2 free. Both b charts remain present.

At infinity, the known linearized diagonal

```
lambda_k=2*omega*(k+2*t+3+6*d)
```

is nonzero at the high reconstruction indices. Its unique possible
negative resonance occurs at `k*=-2*t-3-6*d`. Nonintegrality of this
number allows a formal tail to be solved; it does not show that a
polynomial solution cannot have that tail identically zero. At a split
index `t=3*m^2-1`, the negative factor has its compatibility coefficient
at exponent `6*m-2`. The compatibility equation is a retained residual,
not an automatic obstruction. No all-t result follows by relabelling
that row.

## 5. A bounded external applicability check did not supply a theorem

The general second-kind equation in (UF), when solved for P*P', has a
linear coefficient

```
B*x-(3/2)*L*(L+b),
```

whose top degree is 2N and whose leading coefficient is nonzero. Thus it
is outside the equivariant hypothesis used by the second-kind theorem
in [Valls, Polynomial Solutions of Equivariant Polynomial Abel Differential
Equations](https://doi.org/10.1515/ans-2017-6043): that hypothesis sets the
linear coefficient to zero. Moreover the cited result bounds the number
of polynomial solutions of one fixed equation; such a bound does not
exclude one coefficient-sensitive solution. No external classification
theorem is imported.

There is also no safe shortcut from the reconstructed source map having
a linear Jacobian. A statement about arbitrary polynomial maps with
Jacobian a coordinate is already strong: composing any constant-Jacobian
map with the source map `(u,v)->(u,v^2)` produces Jacobian proportional to
v. This elementary observation does not establish an equivalence of the
marked K16 problem to the full Jacobian conjecture; it does show why
linear-Jacobian classification cannot be assumed without a source and
the exact marked hypotheses. The actual needed induction is the
category-closure theorem named in the charged ideation source.

## 6. Global rational parametrization of the quartic factor curve

Assume B*eta is nonzero throughout this subsection. There is an
additional global reduction behind (UF). Regard Rfree as a
polynomial in the two independent variables x and L, with b,B,eta fixed.
On the locus xL nonzero, its zero curve is rational. Put

```
f(v)=-2*b*v+4*B*v^2+(8*b*eta/3)*v^3+(16*B*eta/3)*v^4,
g(v)=f(v)/v
    =-2*b+4*B*v+(8*b*eta/3)*v^2+(16*B*eta/3)*v^3.
```

The exact identity is

```
Rfree(x,L)=(3*L^4/(16*x))*(x-f(x/L)).                 (UR1)
```

Consequently the inverse rational parameter is `v=x/L`, and the
parametrization is

```
x=f(v),    L=g(v).                                    (UR2)
```

These identities were checked by exact symbolic expansion. The rational
expression is used only in the explicitly localized ring; its numerator
is the original polynomial Rfree. Geometrically the plane quartic has a
triple origin, which the open condition xL nonzero removes. The formulas, not
a generic smoothness assumption, establish the parameterization on the
open set for every parameter value.

### The b nonzero chart: an exact finite-algebra transform

Assume b B eta nonzero and a solution of (UF), and write

```
R(x)=Rfree(x,L(x))=P(x)*Hdiff(x),
Q(v)=L(f(v))-g(v).
```

Since L(0)=-b, the constant R(0) is `-3*b^4/16`, hence x is a unit in
`k[x]/(R)`. Reducing R modulo L gives `-B*eta*x^3`, so L is also a unit
there. Define v=x/L. Equation (UR1) gives x=f(v); dividing by the unit v
gives L=g(v). Conversely, in `k[v]/(Q)`, g is a unit because

```
gcd(g,Q)=gcd(g,L(0))=1.
```

Also Q(0)=b is nonzero, so v and f(v)=v g(v) are units. These calculations
give literal inverse k-algebra maps

```
k[x]/(R)  <-->  k[v]/(Q),
v=x/L(x),       x=f(v).                               (UR3)
```

The maps are valid on all multiplicities. Both algebras have dimension
4N: the leading term of R is nonzero of degree 4N, and f has degree four
because B eta is nonzero. Under (UR3), the factor P selects a degree-2N
factor `M_P(v)` of Q, and Hdiff selects its complementary degree-2N
factor. In particular

```
M_P = monic gcd(P(f(v)), Q(v)),
deg M_P=2*N.
```

The finite-algebra isomorphism proves this including repeated factors;
it is not a comparison only of distinct roots. Equivalent descriptions
can use resultants or norms, but they must keep the differential equation
defining Hdiff. An arbitrary half-degree factor of Q does not provide
that differential factor.

### The b zero chart: the distinguished triple point is removable explicitly

If b=0 and B eta is nonzero, then L has a factor x^2, P has order one
at x=0, and Hdiff has order two. Thus

```
Rbar=R/x^3,
Pbar=P/x,
Hbar=Hdiff/x^2
```

are polynomials, with `Rbar=Pbar*Hbar` and `Rbar(0)=-B*eta` nonzero.
Their degrees are 4N-3, 2N-1, and 2N-2. Write `L=x^2*Ltilde`. Here
`f=v*g`, with g of degree three, and

```
Q/g = v^2*g(v)*Ltilde(f(v))-1.                        (UR4)
```

This polynomial has degree 4N-3 and is coprime to g; it is also nonzero
at v=0. The same mutually inverse maps as in (UR3) therefore give

```
k[x]/(Rbar)  <-->  k[v]/(Q/g).                        (UR5)
```

The two factors now have degrees 2N-1 and 2N-2. This is the correct
version of the transform on b=0; using the b nonzero quotient unchanged
would silently omit the marked x=0 behavior or count the three
extraneous parameter roots.

### What the global order count does and does not prove

The transformed total intersection length is 4N on b nonzero and 4N-3
after the explicit b=0 removal. The differential factors have exactly
the complementary lengths above. All these integers are consistent for
every N>=4. No integrality condition on d follows from this count.
The branch curve being rational likewise supplies no forbidden genus.

For a check useful in any subsequent residue calculation, differentiation
of Rfree before specialization gives

```
(partial Rfree/partial L)(f(v),g(v))
    =(3/16)*g(v)^2*f'(v).                             (UR6)
```

Thus a calculation dividing by f' must branch on its zeros; they are
not absent by the parameterization. On the graph, the derivative of
R at an intersection is

```
R'(x)=(3/16)*L(x)^2*Q'(v),    v=x/L(x),
```

evaluated at the intersection. This relates multiplicities correctly
but, together with `R'=P'Hdiff+P Hdiff'`, remains compatible with (UF).
It did not yield a residue whose nonzero value contradicts polynomiality.
The first still-missing statement is precisely that no factor of the
prescribed size in (UR3) or (UR5) satisfies the linked differential
formula for Hdiff and the initial jets. The degree transform alone
does not lower N, so it is not a terminating second descent.

## 7. Precise residual after finite computations

The primary agent's verified finite computations can be substituted into
the following quantifier without changing its remaining content:

```
For every as-yet-unproved integer t>=3 and every field factor k of
Q[d]/(3*d^2-t-1), there exist polynomial cofactors over k certifying

  1 in (F_2,...,F_(2t),1-u*Delta*Hslice),

and

  1 in (E_2,...,E_(2t),Delta,A,1-s*(M+b*N)).
```

The cofactor degrees may depend on t; no fixed square-nilpotence or
fixed-degree identity is assumed. Equivalently, use the single
degree-independent differential residual in Section 2, with N=t+1.

The original quotient lemma glues the two tests and gives

```
X empty <=> U empty <=> B*eta in radical(J)
        <=> tau in radical(I_positive)
        <=> (8.1) => (T) at that t.
```

This logical chain is available at every index for which emptiness is
proved. These notes do not supply its all-t antecedent.
