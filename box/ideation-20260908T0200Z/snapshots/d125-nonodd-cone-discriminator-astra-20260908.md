# D125 nonodd cone: provisional unequal/rational extension

2026-09-08. **PROVISIONAL DESK PROOF, NOT PROMOTED.** Dropping odd parity
does not break the direct unequal/rational receiver argument: the additional
scalar kernels can be retained, and positive homogeneity replaces parity
in the initial calculation. This is one speculative child of the current
PROVISIONAL cone source/consumer work. Their live hostile review was not read.
The centralizer lemma below is consumed from the provisional source parent;
the nonodd changes and the needed initial argument are derived explicitly.

**Exact claim, conditional on that stated provisional parent lemma:** no
polynomial pair A,B over a characteristic-zero field satisfies

```text
deg A=15, deg B=25, A_15=H³, B_25=H⁵,
H=p²V0, V0=g³+p³, w(g)=5,w(p)=-7,
w(A)<=3, w(B)<=5, [A,B]=c*g², c!=0.              (S)
```

No parity, lift-polynomiality, moving-lift theorem or actual source point
is assumed. The accepted minimal receiver interface identifies this as a
necessary family for the UNEQUAL/RATIONAL branch after target monicity.
It does not cover common_3/common_4, whose weight bounds differ, or golden H,
whose cubic has a repeated factor. No JC2 or global degree125 claim follows.

## 1. Parents and the nonodd A-reference

The whole accepted minimal receiver composition was read, SHA
7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413.
Its §§2–4 preserve the exact squarefree H and allow independent target
monicity without fixing an additional scalar. The sole mathematical lemma
borrowed here is K[g,p]'s polynomial centralizer of H being K[H], proved
elementarily in §2 of the PROVISIONAL cone first-contact source, SHA
bf1dfa72a6a3dc8210ed8fd8354bb0d8bcda6dfcc447a1e9ba386048e177955f.
That proof uses geometric integrality of H=h, not irreducibility of H=0,
and does not use oddness. No reviewer verdict is presumed.

Use A_s=sum s^(15-d)A_d and B_s=sum s^(25-d)B_d. Their exact bracket is
c*s^36*g². Give s,g,p combined degree1 and keep receiver weight w(s)=0.

Construct

```text
R_s=H+sum_(r=1)^5 s^r R_(5-r),  deg R_(5-r)=5-r, w(R_s)<=1.
```

Recursively at orders r=1,...,5 divide the current order-r A residual by
3H², using leading monomial g⁶p⁴, and put the quotient into R_(5-r).
The new coefficient of R_s³ at that order is exactly3H²R_(5-r);
all other terms are already fixed. Division lowers g-degree, preserves
homogeneity, and gives quotient weight<=1. Therefore the order1,...,5
residuals are normal for g⁶p⁴. In particular the reference constant R_0
at r=5 absorbs the possible scalar R² term; it is NOT suppressed by parity.

Choose alpha at order10 by division of the degree5 residual by H, and
choose a0 to kill the scalar order15 residual. Put

```text
alpha_s=alpha*s^10, a0_s=a0*s^15,
F=A_s-(R_s³+alpha_s R_s+a0_s).
```

F_10 is H-leading-monomial normal; F_15=0. Every F_r is homogeneous of
degree15-r and weight<=3. Thus if F is nonzero, 1<=j=ord F<=14.
F cannot vanish: otherwise the degree10 polynomial3R_s²+alpha_s divides
the nonzero degree2 target c*s^36*g² in K((s))[g,p]. This also treats
nonzero source constants correctly.

## 2. All five B kernels, exact remainder and the first contact

Set b_i,s=b_i*s^(25-5i), 0<=i<=4, and

```text
f_A(R)=R³+alpha_s R+a0_s,
f_B(R)=R⁵+b_4,s R⁴+b_3,s R³+b_2,s R²+b_1,s R+b_0,s,
q(R)=5R²/3+(4b_4,s/3)R+b_3,s-5alpha_s/9,
tau_s=2b_2,s-(4/3)b_4,s alpha_s,
delta_s=b_1,s-b_3,s alpha_s+5alpha_s²/9.
```

Literal polynomial division gives

```text
f_B'(R)=(3R²+alpha_s)q(R)+tau_s R+delta_s,
ord tau_s>=15, ord delta_s>=20.
```

With G=B_s-f_B(R_s)-q(R_s)F the EXACT identity is

```text
[A_s,B_s]=[R_s,T]+[F,G],
T=(3R_s²+alpha_s)G-(tau_s R_s+delta_s)F
  -((5/3)R_s+(2/3)b_4,s)F².                    (I)
```

In independent variables R,F,G, its wedge coefficients are respectively
-(tau R+delta)-q'F, 3R²+alpha,1. Neither the linear remainder, the
b4 contribution to q', nor an alpha term has been deleted.

G has combined degree25 and w(G)<=5. For any tentative j<=14,
15+j>2j,20+j>2j and5+2j>2j. If a first G_l occurs below2j, (I)
gives [H,3H²G_l]=0. Homogeneity and the provisional centralizer lemma
allow precisely the following positive-order polynomial kernels:

```text
l=5,10,15,20,25, with leaders H⁴,H³,H²,H,1.
```

Remove them, in increasing order, using b4,b3,b2,b1,b0 respectively.
Their exact changes to G are

```text
-b4_increment*s⁵*(R_s⁴+(4/3)R_s F),
-b3_increment*s^10*(R_s³+F),
-b2_increment*s^15*R_s²,
-b1_increment*s^20*R_s,
-b0_increment*s^25.
```

Each changes only its designated order and later orders. The changes to tau
and delta keep the orders15/20 above, so the induction is valid.
Consequently ord G>=2j. If a whole b3_s A_s target shear is used, its
constant changes b0_s to b0_s-b3_s a0_s and its R coefficient changes
b1_s to b1_s-b3_s alpha_s. The checker retains these terms; no partial
shear is used in the proof.

At2j<36, (I) reduces to

```text
[H,3H²G_(2j)-(5/3)H F_j²]=0.                   (II)
```

The polynomial inside is homogeneous of degree35-2j. For integers
1<=j<=14, the only centralizer exceptions are j=5 (scalar H⁵) and
j=10 (scalar H³). In both, and when the polynomial is zero, division of
one H shows H|F_j². Squarefreeness of V0 then gives V0|F_j; writing
F_j=V0 Q gives w(Q)<=-12, hence p²|Q, so H|F_j.

Order10 normality kills j=10; degree<5 kills j=11,...,14. Thus

```text
j in {1,...,9}, F_j=H C,
C homogeneous degree10-j>0, w(C)<=2, C!=0.       (FC)
```

For j<=5, H²-normality and weight<=3 imply deg_g F_j<=5: any monomial
with g-degree>=6 has p-degree>=4 and would not be normal.
For j>=6, total degree<=9 and weight give the same bound.
Thus deg_g C<=2 and V0 does not divide C. No oddness was used.

## 3. Product-ring initial, with all scalar terms kept above it

Pass to Kbar and let lambda run through the three distinct roots of
lambda³=-1. Work simultaneously in

```text
L=product_lambda Kbar(p), via g=lambda*p.
```

This is the total quotient ring of V0=0, NOT its unlocalized coordinate
ring. No component is selected before orders or initials are computed.
A polynomial normal for g³p² of weight<=5 has g-degree<=2; hence its
image in L vanishes only when that polynomial is zero.

Division by R_s uses the unchanged leading monomial g³p². All other
terms have smaller g-degree, receiver degree<=5 and weight<=1; this
includes R_0*s⁵. It preserves s-order and the combined grading.
It gives finite exact expansions

```text
F=P0+R_s P1+R_s²P2,   ord Pi>=j,
G=sum_(i=0)^4 R_s^i Qi, ord Qi>=2j,
```

with normal coefficients of weights<=3-i and<=5-i. At order j, (FC)
and normality give P0_j=0, P1_j=C, P2_j=0.
These are finite blocks, not an assumed truncation: every ordinary receiver
coefficient of F has degree<=14, while ord G>=2j>=2 and combined degree25
give ordinary degree G<=23. Division by degree-five R_s therefore permits
at most its second and fourth powers, respectively.
Therefore q0=ord P0>j, allowing q0=infinity, and ord P1=j.

On each factor of L, R_s(X,p)=z has a unique formal solution
X=G_lambda(s,z) with G_lambda(0,0)=lambda p: its X derivative is
3lambda² p⁴, a unit in Kbar(p). Use all three solutions at once.
Put

```text
eta=min(j/2,q0/3),  j/3<eta<=j/2<=9/2<5, z=s^eta Z.
```

A finite Puiseux extension of s clears denominators2/3. Every implicit
correction G_lambda-lambda p has positive (s,z)-order and hence positive
order after this substitution. Normal coefficient leading residues do
not all vanish, so no such correction enters the global initial forms.
No regularity of later implicit coefficients at p=0 is asserted.

The initial of A_s is

```text
P(Z)=Z³+uZ+v
```

of s-order3eta. Here u is the residue of C if j=2eta (else0), and v is
the residue of (P0)_q0 if q0=3eta (else0). At least one is nonzero in L.
The scalar terms alpha_s z and a0_s have weights10+eta and15, both
strictly above3eta because eta<5.

All coefficients are homogeneous in p on each component. Put h=5-eta>0.
Precisely, z has combined degree5 and z=s^eta Z gives Z combined degree h.
After the factors s^(3eta) and s^(5eta), the initial polynomials have
combined degrees3h and5h; their Z^i coefficients thus have degrees
(3-i)h and (5-i)h. This is an inherited grading, not a parity claim.
Then u,v have degrees2h,3h. A nonzero homogeneous rational function of
positive degree on a component is nonconstant; if the indicated degree
is nonintegral, that coefficient must simply be zero. At least one of
u,v is nonzero globally, so the initial is not coefficientwise constant.

The scalar B term b_i,s z^i has weight
25-5i+i eta=5eta+(5-i)(5-eta)>5eta for every i<5.
Thus b4's new Z⁴ term is strictly too high; the other four kernels are
also too high, not discarded by parity. Likewise q(R_s)F has weight
at least5eta, and every term R_s^i Qi with i>=1 has weight at least
2j+eta>=5eta. Only Q0 can appear below5eta.

The exact z⁵ term cannot cancel (all other expansions have z-degree<=4).
Hence B's global initial has order nu<=5eta. If nu<5eta it is e in L,
with positive homogeneous degree25-nu. Otherwise it is a monic quintic

```text
Q(Z)=Z⁵+cZ³+dZ²+eZ+f,                          (III)
```

with no Z⁴: the P2 contribution there has weight>=j+4eta>5eta,
the Q4 contribution is later, and b4 was treated above.
In (III), c,d,e,f have degrees2h,3h,4h,5h.
These are normal leading residues, not later pole-bearing implicit terms.

The transformed exact bracket is c_source*s^36 G_lambda²/R_(s,g),
whose initial is c_source*s^36/(3p²) on every component.
The bracket of initials occurs at2eta+nu<=7eta<=63/2<36.
Consequently [P,Q]_(Z,p)=0 in L[Z]. If nu<5eta, its Z² coefficient
is3e'=0. Positive homogeneity then gives e=0 on every component,
contradicting the nonzero global initial. Therefore (III) applies.

## 4. Homogeneity replaces parity in all degree3/5 scalar cases

Work componentwise, allowing u or v to vanish. Direct coefficient
comparison for [P,Q]=0 gives

```text
c=5u/3+c0, d=5v/3+d0,
e=5u²/9+c0*u+e0,
f=10uv/9+c0*v+(2/3)d0*u+f0,
```

where c0,d0,e0,f0 are constants in Kbar; they may differ between components.
Because the compared coefficients have the positive homogeneous degrees
2h,3h,4h,5h, respectively, each constant is zero. No parity assertion,
nonzero u/v assumption, or unlicensed common scalar across components
is involved.

The two remaining rows are

```text
u²u'-6vv'=0,         2uvu'+u²v'=0.
```

Euler homogeneity gives p u'=2h u and p v'=3h v. Since h>0 in
characteristic zero, the equations become

```text
u³=9v²,             u²v=0.
```

Each component is a field. If u=0 then v=0; if v=0 then u=0.
Thus u=v=0 on every component, contrary to Section3.
This proves the claimed nonodd exclusion at the explicitly provisional
parent trust. It does not rely on choosing a component where an arbitrary
normal coefficient happens to survive.

## 5. Scope, controls and terminal custody

The geometric coefficient comparison above is a field-point proof, not an
explicit unit certificate or a claim about a nonreduced ideal presentation.
The minimal receiver contract supplies unequal/Q scope only. The repeated
golden cubic invalidates the squarefree step; common_3/common_4 do not
satisfy the stated weight bounds. Those clients remain untouched.

Current source parent bf1dfa72... remains PROVISIONAL. This child does not
read, harvest or anticipate the joint Fable review, nor promote either
parent or itself. The consumer's needed initial reasoning is written out
above rather than imported as an accepted theorem. No moving-lift
report or finite-boundary15g theorem is a premise.

Owned check.py SHA256
9fac34837695f549a64746bdbf2daae661f1ab09a6971937e82e3644a77a650a
uses free-symbol degree3/5 polynomials, never actual H³/H⁵ or A15/B25.
It checks the derivative division, all wedge coefficients, constant-sensitive
whole b3 A shear, all scalar kernel/order cases, the final cubic/quintic
rows and their Euler substitution. Omitting b4, omitting b2, omitting the
constant in the full shear, or changing the final quintic coefficient each
rejects the actual changed expression normally and with -O.
The final ten-mode replay completed in2.620s; each child had30wall/
25CPU/512MiB limits and -I -B, with no Assert gate. A prior output collection
was truncated by the tool display budget; the final complete replay is the
charged receipt. No truncated receipt supports a claim.

Input/output hashes and full commands/rc/stdout/stderr are retained in the
owned box; source originals are unchanged. No CAS, AWS/SSH, actual source
expansion, solver, new lane, review launch, protected/live-peer read, shared
ledger edit or additional-generation work occurred. New report publication
is transactional. All children/writers terminal at handoff. STOP/IDLE.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12836`.
- Body SHA-256:
  `6b9028c42f366e0e0f19c726940e97e95e395a47ebd40d88123a2b6022f2858d`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
