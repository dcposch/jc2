# R2: stronger conditional first-principles row180 computation

This is a conditional local computation for a census row. It is not an exhibited
polynomial Keller pair or a proof of source realizability. It tests the claimed
identity between inherited labels and the child's own characteristic/disc data.
See `r2-child-firstprinciples.md` for source renders and the full Hensel argument.
Unlike the96/72 example, the enumerator agent's additional recorded-centre
stabilizer diagnostic does not immediately refute this row.

Parent row:

n=180,m=120,M=(-120,132,150,178),d=(180,60,12,6,2),
V=(V2,V3,V4)=(2,4,5) or(3,4,5).

Here us=1,vs=5,ds=6,ell=3; Prop.6.3 supplies a child F,G monic in pi
of degrees20,30, with J(F,G)=c gamma^3. It carries H=T2^psi(F,G) and
Q=T3^psi(F,G). The p.150 recurrence independently gives

mu1=-120,
mu2=3*(-120)+(132-(-120))=-108,
mu3=5*(-108)+(150-132)=-522.

Thus deg_pi H=18 and deg_pi Q=87 by Prop.6.3(2).

## Characteristic data on the child's own expansion

Put eta=G^(-1/30), holding gamma fixed. Work in k[gamma]((eta));
G=eta^-30,F=eta^-20+higher. Proposition3.1 and its specialized form
(pp.157-159) give

H=F^3-cG^2+lower terms of (20,30)-weight<60,
Q=H^5-c'G^3+lower canonical terms of (20,30,18)-weight<90,

with c,c' nonzero constants. In the latter basis F has exponent<3 and H
has exponent<5. The unique monomial of weight90 in that basis is G^3:
20a+30b+18e=90, 0<=a<3,0<=e<5, forces(a,b,e)=(0,3,0).
All canonical weights are even.

Let A be the root of H(U,eta^-30)=0 with leading eta^-20.
Hensel recursion gives A in k((eta^10)); H_U(A,G) has order-40.
Exact ord_eta H(F,G)=-18 forces

F=A+a eta^22+terms of order>22, a nonzero.

Thus the first exponent after-20 not divisible by10 is22. Now put
U=A+eta^22 W in Q. The initial equation is a nondegenerate fifth-degree
equation in W with nonzero simple roots. Choose the root corresponding
to a; Hensel recursion produces B in k((eta^2)). Its Q_U derivative has
order4*(-18)+(-40)=-112. All canonical lower terms have strictly later
derivative order. Since actual ord_eta Q(F,G)=-87, we obtain

F=B+b eta^25+terms of order>25, b nonzero.

There is no odd exponent before25. The first-principles p.150 chain is
therefore exactly

M'=(-20,22,25), d'=(30,10,2,1), M'_4=infinity.

Chain-rule control F_gamma|eta=J(F,G)/G_pi shows every coefficient below
eta^29 is constant in gamma; a,b are nonzero constants, which p.150
explicitly counts. No original fixed-x Puiseux series has been substituted
term by term into the new chart. The campaign M,d labels are correct here.

## Own disc data by literal inverse expansions

The parent D3 radius is1/6; it contains(180/6)*5=150 roots of g.
Proposition4.6 gives its g leading polynomial as p^15, deg p=10.
The selected D2 root has multiplicityV3=4 in p. Normalize D3's common
constant centre to y=0. Galois over k((x^-1)) makes every nonzero leading
coefficient at exponent1/6 lie in an orbit of6. A nonzero root with
multiplicity4 would need degree24>10. Hence the selected root is0,
with multiplicity4. The remaining six roots are one nonzero orbit,
each simple. Thus exactly90 source roots have

y=C x^(-1/6)+higher, C nonzero,

while the60 roots in D2 have y-order>1/6.

The actual transformation at us=1 is

gamma=y^-1,
z=sum_(j<5) a_j gamma^j+pi gamma^5,
x=(y-e-z)/b.

For each nonzero orbit write x=s^-6,y=C s+...; inversion yields
x=C^6 y^-6+..., and therefore

pi=-b C^6 gamma+terms of smaller gamma-growth.

Six conjugate source cover series become one inverse series in y. The90
source roots therefore give90/6=15 actual child pi-roots at a single
nonzero leading coefficientC_* gamma. The roots of source order>1/6,
and any finite-x branches above y=0, have strictly smaller pi-growth.
Degree_pi G=30 leaves precisely15 roots at coefficient0. Thus G's own
top leading polynomial is const*pi^15*(pi-C_*)^15 after scaling by gamma.

The full tower's top is also checked, including Q. Proposition4.6 gives
source Q leading p^41 q, with deg q=25 and q squarefree containing the
roots of p. Galois consequently gives q=0 plus four nonzero6-orbits.
The p-orbit has Q multiplicity42 at each of its six coefficients and
becomes42 child roots atC_*. The other three q-only orbits become one
child root each at three further distinct nonzero coefficients. The
remaining87-42-3=42 child Q roots have smaller growth, at coefficient0.
H and F distribute with G by Proposition4.6(1). The child's own top disc
therefore has radius-1 and leading p_child of degree2 with two simple
roots0,C_*, while q_child has degree5 with five simple roots.

Because n'/d'_3=30/2=15, either proper major subdisc containing G roots
has its own normalized multiplicity

V'_3=15/(30/2)=1.

The inherited label in descend() is4. Own C-TOP is1<=2 and holds; the
labelled screen instead tests4<=2 and reports failure. The same conclusion
holds for both parent V2 variants above: the top calculation uses neither.
This is a concrete inverse-series demonstration of wrong V inheritance.

## Scope

The result is not a construction of either180/120 Keller counterexample.
It shows what the actual Prop.6.3 child top would be if either source row
were realized. Both rows pass the own-child C-TOP test under this
first-principles local computation and fail the inherited-label test.
No source obstruction currently known to this lane repairs that identity.
Use REFUTED for the claimed labelled kill licence, with explicit OPEN for
source realization and the numerical number of truly surviving rows.
