# The high-order r=12 mod49 mixed-scalar family

ROOT, September13,2026. MANUAL / PRODUCER-CHECKED / UNPROMOTED.
Quantity: nonvanishing of the SAME mixed scalar at every actual leading
root for every r=12 mod49, with no bound on the 7-adic order. No CAS ran.

## Claim and inputs

Let r>=2, t=(5r+2)/(3r+1), phi=1+u+Xu^2+Yu^3, T_h=trunc_7(phi^h), and
B=[u^14](phi'/phi)T_(2t-1)T_(4-t) in the accepted whole leading algebra
S_r=Q[X]/P, Y=V/U. For r=12 mod49 put

    e=(t-3)/7=-(4r+1)/(7(3r+1)), n=v_7(e)>=1.

The claim is that the seven roots counted with multiplicity divide into
one, four, and two roots with respective B valuations

    n, 7n/4, 2n.

In particular B is a unit of S_r for this entire infinite family.
No complete-source zero, all-r result, effective cutoff or JC2 conclusion.

Charged frozen mathematical inputs, all read WHOLE in the immediately
preceding ROOT intake and/or this continuation, with current pins checked:

- xmodel/f10-mixed-remaining-local-astra-20260913.md,
  cec05bddcbed1a0a9fc9e4ef9922f4b6eed3ca08684b52cec69bf1a9406bfd42;
  sections1-2 only; section3 is not a premise.
- xmodel/f10-mixed-five49-gate-fable5-20260913.md,
  8c9e1035093cb5b2619f7370320b3063b7ab5269d75dbdd74292c6d2281d7225;
  completed different-model FIRST, whole-source map and factorial carries.
- xmodel/f10-mixed-univariate-reduction-root-20260912.md,
  7b8545a623a771ebd423b441c4c1567389d0ca837d4e5b80c8990bc52b1075f8;
  accepted actual U,V,K,P interface supersedes its historical heading.

COORDINATION33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597
and finalizer0f6aaf7d549952de8f318bdd974ae4627e497783d809f94cfaba16607355cb8d
are unchanged administrative inputs. No live peer, linked source, protected
tree, worker, scientific code/interpreter/import/AST/syntax/test or network.

## 1. Exact polynomial integrality and the scalar initial form

Use R_b=(T_b-phi)/(b-1), b=1-7e, s=5+14e, and

    J=[u^14](phi'/phi)T_s R_b, G=7J, B=-eG.

The last identity is exact universally. The charged FIRST reconstructs the
monic division, the single possible factorial7 denominator of R_b and the
carry in T_s. More strongly, substitution b=1-7e makes 7R_b a polynomial
in e,X,Y,u over Z_(7), and s=5+14e makes T_s such a polynomial as well:
the only problematic binomial denominator is 7!, and its numerator has
the factor s-5=14e. Thus G belongs to Z_(7)[e,X,Y], not merely to the
valuation ring at a chosen point. Its coefficientwise reduction is

    G mod7 = 3c8(5)+2e,
    c8(5)=3X^3+5X^4+6XY+4X^2Y+2Y^2+2XY^2 mod7.

The exact source coefficient polynomials d6,d7 are also in Z_(7)[e,X,Y].
At e=0, d6=X^3+6XY+3Y^2 and d7=3X^2Y+3Y^2. Their deviations have a
factor 7e, except the pure u^7 binomial term in d7, which is e times a
7-integral polynomial reducing to 1. Consequently

    d6 mod7=X^3+6XY+3Y^2,
    d7 mod7=3X^2Y+3Y^2+e.

All these are coefficientwise identities BEFORE any root specialization.

A necessary exact support bound, beyond reduction mod7: G(0,X,Y) has no
monomial of weight below3 when wt(X)=1, wt(Y)=2. Indeed put R_1=T'_1
(derivative in the exponent). In the exact expression for J at e=0,
replace T_5 by phi^5-tail_(>=8)(phi^5). The first part is
phi' phi^4 R_1. A variable monomial of weight w in phi' phi^4 has
u-degree at most4+w; R_1 has u-degree<=7 and nonnegative variable weights.
Thus its u^14 coefficient needs w>=3. The tail part itself has no
variable monomial of weight<3, since phi^5 at weight w has degree<=5+w;
the other formal factors have nonnegative weights. This proves the bound
exactly over Q, so multiplying by7 cannot create hidden low-weight terms.
In particular G(0,X,Y) also has no monomial of ordinary degree below2.
Finally G-G(0,X,Y) is divisible by e in Z_(7)[e,X,Y].

## 2. Exhaustive Newton polygon of the actual septic

Use precisely

    U=3X^2-3(t-1)X-(t-3)(3t-4)/4,
    V=X^3+(t-3)(t-1)X^2+(t-3)(t-4)(4t-5)X/20
      +(t-3)(t-4)(t-5)(3t-4)/420,
    K=X^3+3(t-3)X^2/2+(t-3)(t-4)X/4
      +(t-3)(t-4)(t-5)/120,
    P0=(t-2)P=3V^2+(t-2)(6X+t-3)VU+(t-2)KU^2.

After t=3+7e these are in Z_(7)[e,X]. At e=0,
P0=3X^6(3X-5). Coefficientwise mod7,

    U=3X^2+X, V=X^3-e, K=X^3,
    P0=2X^7+6X^6+4eX^3+eX^2+3e^2.

For an exact e of valuation n>=1, write P0=sum a_i X^i. Then

    v(a0)=2n, v(a1)>=2n, v(a2)=n,
    v(ai)>=n for i=3,4,5, v(a6)=v(a7)=0.

Here a0 is exactly divisible by e^2, and a1 by e^2: in the displayed
formula U(0), V(0), K(0), V_X(0) are all divisible by e; direct
differentiation of each product proves the assertion for a1. All i<6
coefficients vanish at e=0, and the mod7 display proves the three exact
endpoint valuations and excludes cancellation there. This accounts for
possible coefficients divisible by7, rather than discarding them.

The lower polygon therefore has vertices (0,2n),(2,n),(6,0),(7,0).
It gives two X roots of valuation n/2, four of valuation n/4, and one
of valuation0, counted with multiplicity, over Q7bar. No root is omitted.

For a=v(X)>0 in either cluster, U has leading term -6X. For a=n/4,
V has leading X^3 and v(Y)=n/2. For a=n/2, V has leading e/6 and again
v(Y)=n/2. Indeed V's exact constant is (e/6) times a 7-integral unit
congruent to1, whereas its other new coefficients are divisible by7e.
For the unit root, Xbar=5/3=4 and Ybar=5, with Ubar nonzero.

## 3. Nonzero scalar on every cluster, for every n

Unit root: the charged source reduction Gbar=Y((3Y-1)X+Y) gives Gbar=4
at (Xbar,Ybar)=(4,5). Hence v(B)=n.

Four-root cluster: choose pi^4=7, put x=residue(X/pi^n),
y=residue(Y/pi^(2n)), E=residue(e/7^n). All are nonzero. The source
initial forms give x^3+6xy=0, so y=x^2. The support bound from section1
makes every term of G(0,X,Y) have valuation at least3n/4. Terms with
larger weight have strictly larger valuation; terms with a factor e also
have larger valuation because n>3n/4. Its initial form is therefore

    residue(G/pi^(3n))=2x^3+4xy=6xy !=0.

Thus v(G)=3n/4 and v(B)=7n/4. Coefficients divisible by7 cannot create a
smaller-weight term, by the exact bound, and are strictly higher at the
same weight. This remains true for arbitrarily large n.

Two-root cluster: choose rho^2=7, and put x=residue(X/rho^n),
y=residue(Y/rho^n), E=residue(e/7^n). Now the source initial forms are

    6xy+3y^2=0, 3y^2+E=0,

so x=-y/2. The ordinary-degree bound gives v(G(0,X,Y))>=n. The only
extra possible initial term from its e-multiple is its constant term;
the coefficientwise mod7 formula already records that as2e. Hence

    residue(G/7^n)=4xy+6y^2+2E=4xy=5y^2 !=0.

Thus v(G)=n and v(B)=2n. Dropping the divided carry2e would give an
incorrect initial coefficient; it has been retained at the exact order.

## Scope, controls and next gate

For r=12 mod49, n=v7(4r+1)-1 is any positive integer; e is never zero
for an actual positive integer r. The proof covers every valuation order
and every residue extension. Nonvanishing at all roots of the accepted
Artinian algebra proves unitness, including nilpotents and arbitrary
base change. This is inverse EXISTENCE, not computed Bezout DATA.

Control: the residual point (X,Y,e)=(0,0,0) does make Gbar zero. We do
not discard it using the rational guard: its six approaching branches
are precisely the two positive-valuation clusters analyzed above. The
n=0 boundary is deliberately excluded; the valuations used to separate
weights then no longer separate them. No conclusion for r=5 mod49,
r=0,4,6 mod7, source comparison/REG, full F10 or JC2 follows.

Cheapest independent test: reconstruct the exact coefficient divisibilities,
Newton polygon, support bound and three initial forms from the charged
formulas, manual estimate10minutes unmeasured. A different-model FIRST
must precede promotion. Own whole readback and unchanged postpins precede
the final marker and finalizer expected verification. No dependent lane
may consume a live partial or unverified final publication.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7899`.
- Body SHA-256:
  `3ac2dbfef6a91a4956c1aa3c106ba777612f2a699f8028608ea73b6bc359c0e0`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
