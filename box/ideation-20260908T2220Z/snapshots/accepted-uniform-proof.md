# A uniform cone Jacobian degree bound

2026-09-08. **UNREVIEWED, PRODUCER-CHECKED THEOREM.** The proposed bound
holds under the stated hypotheses. This proof derives the general source
arrow and consumer directly; it does not treat the recent nonodd D125
extension or any live review as an accepted theorem. No new JC2 source
attachment is claimed.

## 1. Statement, conventions, and history boundary

Let K be any characteristic-zero field. Let a,b be positive integers,
D=a+b, and assume

```text
5b>4a+1.
V(g,p) homogeneous of degree b, monic in g, squarefree, p not dividing V;
H=p^a V,    w(g)=5, w(p)=-(5b-1)/a.
A,B in K[g,p], deg A=3D, deg B=5D,
A_(3D)=H^3, B_(5D)=H^5, w(A)<=3, w(B)<=5.
```

Here w(f) is the maximum monomial weight; w(0)=-infinity. The bracket is
[U,W]_(g,p)=U_g W_p-U_p W_g. In particular [A,B]=A_g B_p-A_p B_g. Then

```text
[A,B]!=0  implies  deg_total[A,B]>=D+2.                 (THEOREM)
```

No parity, ordinary lift, face beyond these bounds, or geometric
degeneration assumption is made. The theorem is not a claim that an
additional JC2 receiver meets these hypotheses. The monomial-Jacobian
case is covered only if its actual degree and all source hypotheses do.

Put t=(5b-1)/a>4. Then D>=3, w(H)=1, and the leading monomial of H in
lexicographic g>p order is g^b p^a, with coefficient1. Every other H
monomial has smaller g-degree and strictly smaller weight. Throughout,
s has ordinary combined degree1 and receiver weight0; g,p have combined
degree1. Orders refer to s, and the order of zero is infinity.

History checksum was restricted to the four named terminal reports in
box/uniform-cone-jacobian-degree-20260908/history-pins.json, with targeted
APPROACHES retrieval. The D=5 reference identity and product-global
mechanism are known in the first-contact/nonodd reports. The older
monomial-J Euler-element no-go is a different assertion: it does not deny
the weighted derivation identity used below. Those texts are comparison,
not mathematical dependencies; the proof below rederives every needed
claim. This is a new uniform extension within that checked scope, not a
global literature-priority claim. No live gate or blind-round body was read.

## 2. Centralizer from the generic fiber, including arbitrary K

The rational Hamiltonian centralizer of H is K(H), and the polynomial
centralizer is K[H]. To prove this, let h0 be transcendental and
F0=K(h0). On H=h0, p is invertible. Set u=g/p and T=1/p. The generic
fiber becomes

```text
T^D=V(u,1)/h0.
```

Over an algebraic closure of F0, V(u,1) has degree b and b distinct
roots: homogeneity, monicity, squarefreeness and p not dividing V ensure
this, also in characteristic zero after scalar extension. At any one root
lambda, T^D-V(u,1)/h0 is Eisenstein for the prime u-lambda: its constant
coefficient has valuation1 and its leading coefficient is1. A nontrivial
monic factorization over the fraction field would, by Gauss's lemma over
this discrete valuation ring, reduce to two positive powers of T modulo
u-lambda; both factor constants would be divisible by u-lambda, contrary
to the product constant having valuation1. Thus it is irreducible and
remains a domain after inverting T. The original
generic fiber is geometrically integral. In particular F0 is relatively
algebraically closed in L=K(g,p), identifying h0 with H: a nontrivial
finite separable subfield extension would split after algebraic closure
of F0, contrary to the domain just proved.

For completeness, any z in L with [H,z]=0 is algebraic over F0. Since
H_g is nonzero, the derivation d=[H,-]/H_g fixes F0 and has d(p)=1.
The extension L/F0(p) is finite. Differentiate the monic minimal
polynomial of z over F0(p). Because d(z)=0, its differentiated
coefficients give a polynomial of smaller degree vanishing at z, so all
are zero. Constants of d/dp in F0(p) are F0 in characteristic zero.
Hence z is algebraic over F0 and therefore lies in F0.

Finally, if coprime r,q in K[X] have r(H)/q(H) polynomial, their Bezout
identity implies q(H) is a unit in K[g,p], forcing q constant. Thus the
polynomial centralizer is K[H]. Its homogeneous part of degree e>=0
is the scalar span K.H^(e/D) if D divides e, and zero otherwise.
The reducible special fiber H=0 was not used to assert generic integrality.

## 3. Source dilation and every A-reference coefficient

Suppose for contradiction that J=[A,B] is nonzero with degree L0<=D+1.
Define

```text
A_s=sum_d s^(3D-d) A_d, B_s=sum_d s^(5D-d) B_d,
J_s=[A_s,B_s]=sum_e s^(8D-2-e) J_e.
M=ord J_s=8D-2-L0>=7D-3.                         (1)
```

This is the ordinary chain rule, not a constant-J assumption. All three
expressions are polynomials in s,g,p; A_s,B_s have combined degrees
3D,5D and retain receiver weight bounds3,5.

Construct

```text
R_s=H+sum_(r=1)^D s^r R_(D-r),
deg R_(D-r)=D-r, w(R_s)<=1.                      (2)
```

At r=1,...,D, divide the current order-r residual of A_s-R_s^3 by
3H^2, using leading monomial g^(2b)p^(2a), and add its quotient to
R_(D-r). The new order-r cube coefficient is exactly3H^2R_(D-r).
Every replacement lowers g-degree, preserves total degree and does not
increase receiver weight; the quotient has degree D-r and weight<=1.
Only the fixed units1 and3 are inverted. The resulting order-r residual
is normal for that leading monomial. The degree-zero R_0 at r=D is
included, absorbing a possible scalar R^2 term rather than suppressing it.

Every monomial of the lower-degree part of R_s has g-degree<b: otherwise
its p-degree is at most a-1, giving weight>=5b-t(a-1)=1+t>5, impossible
at weight<=1. Thus the leading monomial of R_s remains g^b p^a; all
other terms have smaller g-degree, ordinary receiver degree<=D, and
weight<=1.

At order2D, divide the degree-D residual by H and take the scalar
quotient alpha. At order3D choose a scalar a0 to kill the constant
coefficient. Put

```text
alpha_s=alpha*s^(2D), a0_s=a0*s^(3D),
F=A_s-R_s^3-alpha_s R_s-a0_s.                   (3)
```

F_(2D) is H-leading-monomial normal, F_(3D)=0, and F_r is homogeneous
of degree3D-r, of weight<=3. The later alpha/a0 choices do not change
the order1,...,D normalities. If F=0, the nonzero J_s factors as
(3R_s^2+alpha_s)[R_s,B_s] in K((s))[g,p]. Its first factor has ordinary
degree2D>L0, contradiction. Therefore

```text
1<=j=ord F<=3D-1,       2j<=6D-2<M.             (4)
```

This treats arbitrary source constants, zero reference coefficients and
zero alpha; it does not assume the eventual bound on j in advance.

## 4. All five B kernels and the uniform first-contact bound

For i=0,...,4 let b_i,s=b_i*s^((5-i)D), initially with undetermined
scalars b_i in K. In the formulas below the suffix s on scalar parameters
is implicit. Define

```text
f_A(R)=R^3+alpha R+a0,
f_B(R)=R^5+b4 R^4+b3 R^3+b2 R^2+b1 R+b0,
q(R)=5R^2/3+(4b4/3)R+b3-5alpha/9,
tau=2b2-(4/3)b4 alpha,       ord tau>=3D,
delta=b1-b3 alpha+5alpha^2/9, ord delta>=4D,
G=B_s-f_B(R_s)-q(R_s)F.
```

Polynomial differentiation gives f_B'=(3R^2+alpha)q+tau R+delta.
Holding s and the scalar references constant in the bracket, one obtains
the exact identity

```text
J_s=[R_s,T]+[F,G],
T=(3R_s^2+alpha)G-(tau R_s+delta)F
  -((5/3)R_s+(2/3)b4)F^2.                     (5)
```

For example its dR wedge dF, dR wedge dG and dF wedge dG coefficients
are respectively -(tau R+delta)-q'F, 3R^2+alpha,1, exactly those of
[f_A(R)+F,f_B(R)+q(R)F+G]. All alpha, b4 and source constant terms
are retained. G has combined degree5D and weight<=5, and G_0=0 since
the top forms cancel and F_0=0.

If the first nonzero G_l is below2j, equation (5) gives
[H,3H^2G_l]=0, hence [H,G_l]=0. Indeed tau F begins at3D+j>2j,
delta F at4D+j>2j, RF^2 at2j, b4F^2 later, and [F,G] later than l.
The centralizer and degree5D-l allow only the positive-order kernels

```text
l=D,2D,3D,4D,5D, with leaders H^4,H^3,H^2,H,1.
```

In increasing order remove them with b4,b3,b2,b1,b0 respectively.
Their exact changes to G for scalar increment e are

```text
-e s^D (R_s^4+(4/3)R_s F),
-e s^(2D) (R_s^3+F),
-e s^(3D) R_s^2,
-e s^(4D) R_s,
-e s^(5D).
```

Each removes its designated order and changes only later ones. The
corresponding tau/delta changes preserve their orders3D/4D. This finite
induction gives ord G>=2j, including G=0. No rational negative-H kernel
is introduced. A whole b3 A_s shear would change both the R coefficient
to b1-b3 alpha and the constant to b0-b3 a0; neither can be silently
left unchanged. No such shear is needed to change the actual pair here.

At order2j, (5) becomes

```text
[H,T_(2j)]=0,
T_(2j)=3H^2G_(2j)-(5/3)H F_j^2,
deg T_(2j)=7D-2j>=D+2>D.                       (6)
```

Every possible homogeneous nonzero centralizer element in (6) is an
H-power of exponent at least2; the zero case has the same divisibility.
Hence T_(2j) is divisible by H^2. Dividing one H yields H|F_j^2.
Squarefreeness gives V|F_j. Write F_j=V Q. Weight additivity gives
w(Q)<=3-5b. But a monomial of Q with p-exponent<=a-1 has weight at least

```text
-t(a-1)=1-5b+t > 3-5b.
```

Thus p^a divides Q, and H divides F_j. At j=2D, F_j is a scalar H,
contrary to normality. At j>2D it has degree<D and is zero. We obtain

```text
1<=j<=2D-1, F_j=H C, C!=0,
deg C=2D-j>0, w(C)<=2.                         (7)
```

Also deg_g F_j<=2b-1. For j<=D use H^2-normality: a monomial with
g-degree>=2b would have p-degree<=2a-1 and weight>=2+t>3.
For j>D, ordinary degree3D-j<2D supplies the same p-degree bound.
Therefore deg_g C<=b-1, and V does not divide C. No parity or generic
nonvanishing of a scalar parameter was used.

## 5. Finite normal blocks and all simple branches together

Divide repeatedly by R_s using its unchanged leading monomial. The
algorithm terminates by decreasing g-degree, never increases ordinary
degree or receiver weight, and never lowers s-order. All coefficients
retain the combined grading. Consequently there are finite exact blocks

```text
F=P0+R_s P1+R_s^2 P2,       ord Pi>=j,  w(Pi)<=3-i,
G=sum_(i=0)^4 R_s^i Qi,    ord Qi>=2j, w(Qi)<=5-i,           (8)
```

normal for g^b p^a. F has ordinary receiver degree<=3D-1; G has degree
<=5D-2 because ord G>=2j>=2. These bounds justify the maximum block
powers2 and4, not a truncation assumption. At order j, (7) and deg_g C<b
give P0_j=P2_j=0 and P1_j=C. Thus q0=ord P0>j, allowing infinity.

A normal polynomial of weight<=5 has g-degree<b. Otherwise one normal
monomial has g-degree>=b and p-degree<=a-1, so weight>=1+t>5.
Over Kbar, write the b distinct roots of V(u,1) as lambda. The map

```text
normal polynomials of weight<=5 --> product_lambda Kbar(p),
                    g |-> lambda*p                         (9)
```

is injective: a polynomial of g-degree<b cannot vanish at all b distinct
points lambda*p over Kbar(p). This is a product assertion, not injection
on one component. We use the simple V components, not the repeated p=0
component; the weight argument makes this sufficient to detect the normal
residues needed here. A root lambda=0 is allowed.

On every component, R_s(X,p)=z has a unique solution
X=G_lambda(s,z), with constant term lambda*p, since

```text
R_(0,g)(lambda*p,p)=p^(D-1) (d/du)V(lambda,1) != 0
```

is a unit in Kbar(p). This is the formal implicit recursion with a
constant invertible linear coefficient. All corrections have positive
(s,z)-order. Choose

```text
eta=min(j/2,q0/3),
j/3<eta<=j/2<=D-1/2<D,       h=D-eta>0.          (10)
```

Pass to one finite Puiseux extension clearing denominators2 and3, and
put z=s^eta Z. Every implicit correction has positive extra s-order.
By (9), the leading normal coefficient of a block does not vanish on
the entire product. Thus the GLOBAL minimum of block order+i eta is
represented by the restrictions of those leading normal coefficients;
implicit corrections cannot enter it, and different Z-powers cannot
cancel each other. No branch is selected before this minimum, and no
regularity of later coefficients at p=0 is assumed.

The A_s initial has order3eta and is the monic depressed cubic

```text
P(Z)=Z^3+uZ+v,
```

where u is the restriction of C if j=2eta and is zero otherwise, and v
is the restriction of (P0)_q0 if q0=3eta and is zero otherwise. At least
one is nonzero in the product. The other blocks are later; alpha_s z has
order2D+eta>3eta, and a0_s has order3D>3eta.

The combined grading is important: z has degree D, so Z has degree
h=D-eta. A contributing s^r z^i block at order3eta has r+i eta=3eta;
its coefficient degree is 3D-iD-r=(3-i)(D-eta). Thus after removing
s^(3eta), P is homogeneous of combined degree3h, and u,v have
p-degrees2h,3h. These are rational-function Euler
degrees on each component, not an oddness claim. If such a degree is
nonintegral the coefficient is simply zero. The positive degrees ensure
a nonzero u or v is nonconstant.

## 6. The B initial and the strict Jacobian-order margin

Every scalar kernel b_i,s z^i for i<5 has order

```text
(5-i)D+i eta = 5eta+(5-i)(D-eta)>5eta.
```

In particular b4's new z^4 term is strictly above the window. The
composed F has order>=3eta, q has order>=2eta, and every R_s^i Qi with
i>=1 has order>=2j+i eta>=5eta. Below5eta the only possible B initial
is therefore a nonzero tuple e from Q0, with no lower dZ term. Its
p-degree is 5D-nu>0, where nu<5eta is its global order.

The exact z^5 term cannot cancel: all other potentially initial blocks
have z-degree<=4. Thus B has global order nu<=5eta. At nu=5eta its
initial is a monic quintic Q(Z) on EVERY component, with combined degree
5h. It has no Z^4: the R_s^2 P2 term inside qF has order>=j+4eta>5eta,
Q4 is later, and b4 was already treated. This last absence is consistent
with, though not needed by, the general Euler lemma below.

The exact transformed bracket is

```text
[A_s(G_lambda,p),B_s(G_lambda,p)]_(z,p)
       =J_s(G_lambda,p)/R_(s,g)(G_lambda,p).       (11)
```

On each component the denominator has order0 and is invertible, so (11)
has order AT LEAST M. For a general J its leading form may vanish on
some or all V components; no exact nonzero leading term on each branch
is assumed. That can only increase the order and is harmless.

The bracket of the initial forms is at order2eta+nu, and

```text
2eta+nu<=7eta<=7D-7/2 < 7D-3<=M.                (12)
```

Its coefficient must vanish on every field component. If nu<5eta this
coefficient is P_Z e', whose Z^2 coefficient is3e'. Then e'=0; its
positive homogeneous degree forces e=0 componentwise, contradiction.
Hence nu=5eta, and [P,Q]_(Z,p)=0 with both monic initials of degrees3,5
and Euler degrees3h,5h. Product zero divisors cause no inference of a
common scalar across components; the next lemma is applied separately.

## 7. A weighted Euler common-power lemma, proved here

Let F be any characteristic-zero field and let h be nonzero in F.
Suppose P,Q in F(p)[Z] are monic, of positive Z-degrees m,n, and

```text
E=p*d/dp+h*Z*d/dZ,
EP=mh P, EQ=nh Q, [P,Q]_(Z,p)=0.
```

Then, with d=gcd(m,n), there is a monic W in F(p)[Z] of degree d such
that

```text
P=W^(m/d), Q=W^(n/d).                           (13)
```

Indeed eliminate pP_p and pQ_p using Euler homogeneity:

```text
p[P,Q]=h*(n P_Z Q-m P Q_Z).                     (14)
```

Since h!=0, the Z derivative of Q^m/P^n vanishes. The constants of
d/dZ in F(p)(Z) are F(p), and equal leading degrees and monicity force
that constant to be1. Thus Q^m=P^n. Unique factorization in F(p)[Z]
gives (13): each irreducible multiplicity of P is divisible by m/d and
that of Q by n/d, with the same quotient; monicity removes all units.
The degree of W is d. This is an elementary algebraic identity, not an
imported Euler-element theorem and not a use of a nonexistent diagonal
constant field on the product.

For m=3,n=5, W=Z+r(p). The zero Z^2 coefficient of P forces3r=0, so
P=Z^3 and Q=Z^5. Applying this to every component in Section6 gives
u=v=0 throughout the product, contradicting Section5. This completes
the contradiction to L0<=D+1 and proves THEOREM.

The lemma also explains exactly why the old integration constants cause
no problem here: their coefficients obey a single nonzero Euler grading.
No integration or assumption that their values agree across branches is
needed.

## 8. Scope controls, replay, and limitations

The conclusion is nonvacuous as a degree estimate. For example the
factored pair A=H^3, B=H^5+p meets the support/weight hypotheses and has
nonzero bracket3H^2 H_g of degree3D-1. No expansion of those powers is
needed or performed. The bound D+2 is what this argument proves; no
optimality assertion is made. At L0=D+2 the half-unit strict margin in
(12) is lost, so that next degree is not silently covered.

Specific countercontrols to stronger readings:

- If h=0, P=Z^3+1 and Q=Z^5 are monic, commute, and have zero Euler
  degrees under p*d/dp, but Q^3!=P^5 (already at Z=0). Thus division by
  h is genuinely necessary in the consumer.
- If gcd(m,n)>1, take W=Z^2+p^2, P=W^3, Q=W^5, m=6,n=10,h=1.
  These satisfy the Euler and commutation equations by the chain rule,
  while the common W is quadratic. They do NOT yield the depressed
  coprime conclusion. Only W, a quadratic, is materialized in the check.
- At the excluded weight boundary a=b=1, t=4, H=p(g+p), the nonzero
  normal polynomial g+p has weight5 and vanishes on its V component.
  Thus normal-block injection is false if the strict inequality is
  replaced by equality.
- With a=1,b=2 and V=(g+p)^2, t=9 but squarefreeness fails. The nonzero
  normal polynomial g+p again vanishes on every distinct V component.
  The product injection cannot be transferred to repeated V by counting
  b roots with multiplicity. This is not a claim of a low-degree-J pair.

The standalone tiny checker SHA256
bf21db84db6fda0d1e98c102305505b18eab58ddc1ea6c86478fb15191efdec8
checks the full free-symbol reference identity, all five-kernel derivative
division, and universal Euler identity (14). It retains the h=0/gcd>1
counterobjects and the two injection controls. It never expands actual
H/R/A/B powers or a source row. Five (a,b) scalar examples illustrate
the inequalities; the universal proof is in the displayed algebra above,
not a finite enumeration.

Twelve runs (positive plus five intended refutations, normally and -O)
completed in3.288seconds with explicit30wall/25CPU/512MiB child caps,
Python -I -B and no gating asserts. Omitting b4 or b2 changes the actual
derivative division and is rejected; changing the Euler sign changes
the exact identity and is rejected. The remaining two modes demonstrate
the false h=0 conclusion and false gcd-one inference on their concrete
countercontrols. Full argv, rc, stdout/stderr and unchanged code hash are
in replay.json. The actual uniform hypotheses and UFD/implicit proofs
are not replaced by these tests.

The work is independent of the pending/recent nonodd review. All claimed
mathematics is presented here as UNREVIEWED. No golden/common receiver,
additional actual JC2 source, full degree125 exclusion, ideal certificate,
or resolution of JC2 is inferred. No new agent, AWS/SSH, CAS, solver,
production source expansion, live/peer blind report, protected-tree or
shared-ledger access/edit was used. Transactional publication and exact
history/output custody accompany this report. All children and writers
terminal at handoff. STOP/IDLE.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19256`.
- Body SHA-256:
  `3be0031dc6d19cbafc944931c151b297d29b419a5be6076b5696a127c89e3e35`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
