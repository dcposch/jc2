# Golden two-regime initial: source restriction and the j=12 resonance

2026-09-08. **UNREVIEWED, PRODUCER-CHECKED SOURCE IMPLICATION.** The
non-H-divisible first-correction branch is forced into a resonant case:

```text
j=12, ord_s xi>=5, ord_s P0(g_c,p)>=15,             (R)
```

where the canonical references, normal block P0, moving critical point
g_c and critical value xi are defined below; infinity orders are allowed.
This is NOT a golden exclusion. The H-divisible first-correction branch
remains separate, and the initial Jacobian in (R) is at order36, not
forced to commute. No source point or surviving full ideal is asserted.

The proposed regime-A commutation through j=12 was incorrect: the actual
ramified initial bracket order is3j, so j=12 is equality with the target.
Regime B can be controlled, including earlier constants, by choosing the
global minimum over its two separated sheets. The source restriction (R)
is derived here, not imported from a claimed j12 classification.

## 1. Literal source, dependencies and both coefficient-field conjugates

Let K be a characteristic-zero field containing rho, rho²-3rho+1=0.
Set

```text
t=1-rho, L=p+g, M=p+t*g, H=p² L M², Delta=p L M.
deg A=15, deg B=25, A_15=H³, B_25=H⁵,
w(g)=5, w(p)=-7, w(A)<=3, w(B)<=5,
[A,B]_(g,p)=A_g B_p-A_p B_g=c*g², c!=0.          (S)
```

No parity is imposed. The accepted minimal receiver composition supplies
this necessary system for the unequal golden case after independent
target monicity; it does not supply a reverse lift or exhaust other
polygon cases. Both roots rho and3-rho remain: t²=rho, t^-1=2-rho,
t-1=-rho and t(t-1)=2rho-1 are all nonzero. In particular p,L,M are
distinct factors. The leading g monomial of H is rho*g³p², not coefficient1.
Division below uses the fixed field units rho, rho² and3, not an extra
source normalization.

Read scope/history: the whole accepted minimal composition
7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413;
the already banked reference identities in the named nonodd producer
2b5a5013d4d7284957b0e69d108f4f1ac1a2b7e81648b1dd2f403223f4791732
as algebraic templates only; and the whole root-checked golden control
54a499bb55d401e88716dde5762ca39341817adaa7ea1f41faf5865570ac4b0e.
The latter already proves H|F² iff Delta|F and the failure of reduced-
branch injection. Those failures are respected here. The source argument
and critical-coordinate analysis are rederived below. The uniform theorem,
its pending acceptance, live cross/gates and any external j12 assertion
are NOT premises and were not read in this task.

## 2. Source-derived references and all first-contact alternatives

The centralizer is K[H], despite the repeated M. Indeed on H=h0, p is
invertible and u=g/p,T=1/p give

```text
T⁵=(1+u)(1+t*u)²/h0.
```

Over an algebraic closure of K(h0), the root u=-1 is simple, since
t!=1. Eisenstein at u+1 proves this generic fiber geometrically integral.
Hence K(H) is relatively algebraically closed in K(g,p). For a rational
Hamiltonian constant, use d=[H,-]/H_g with d(p)=1. Differentiating its
monic minimal polynomial over K(H)(p) shows all coefficients are
d/dp-constant, so it is algebraic over K(H), hence belongs to K(H).
Finally Bezout shows K(H) intersect K[g,p]=K[H]. A homogeneous polynomial
centralizer is a scalar H-power. This uses the simple generic-fiber root,
not a false assertion that the special fiber is reduced.

Form A_s=sum s^(15-d)A_d, B_s=sum s^(25-d)B_d, so
[A_s,B_s]=c*s^36*g². Give s,g,p combined degree1 and w(s)=0.
For r=1,...,5 successively divide the order-r A residual by3H² and put
its quotient into s^r R_(5-r). This gives

```text
R_s=H+sum_(r=1)^5 s^r R_(5-r), w(R_s)<=1,
F=A_s-R_s³-alpha*s^10 R_s-a0*s^15.               (1)
```

The leading division monomials are g⁶p⁴ and g³p², with the field units
noted above. Replacements lower g-degree, preserve total degree and do
not increase weight. The order1,...,5 residuals are H²-normal; alpha
makes F_10 H-normal, and a0 kills F_15. All constants are retained.
The lower terms of R_s have g-degree<=2: degree<5 and weight<=1 forbid
a g³ term. Thus R_s is cubic in g with leading coefficient rho*p².

F cannot be zero, since otherwise the degree10 factor3R_s²+alpha*s^10
would divide the nonzero degree2 target. Initially1<=j=ord F<=14.
Retain b_i,s=b_i*s^(25-5i), i=0,...,4, and, suppressing s suffixes
(so alpha in the following formulas means alpha*s^10),

```text
f_B(R)=R⁵+b4 R⁴+b3 R³+b2 R²+b1 R+b0,
q(R)=5R²/3+(4b4/3)R+b3-5alpha/9,
tau=2b2-(4/3)b4 alpha, delta=b1-b3 alpha+5alpha²/9,
G=B_s-f_B(R_s)-q(R_s)F.
```

Here ord alpha>=10, ord tau>=15, ord delta>=20. G_0=0, G has combined
degree25 and receiver weight<=5. Direct exterior
differentiation gives

```text
[A_s,B_s]=[R_s,T]+[F,G],
T=(3R_s²+alpha)G-(tau R_s+delta)F
  -((5/3)R_s+(2/3)b4)F².                        (2)
```

The three wedge coefficients in independent R,F,G are
-(tau R+delta)-q'F, 3R²+alpha,1; thus no b4 or alpha term is dropped.
The first G_l below2j must commute with H and has degree25-l.
The only positive-order kernels are l=5,10,15,20,25 with H⁴,H³,H²,H,1.
Their removals change G by scalar multiples of

```text
s⁵(R_s⁴+(4/3)R_s F), s^10(R_s³+F),
s^15 R_s², s^20 R_s, s^25,
```

respectively. They affect no earlier order and preserve the tau/delta
orders. Since15+j>2j for j<=14, this finite induction gives ord G>=2j.
At order2j<36,

```text
[H,3H²G_(2j)-(5/3)H F_j²]=0.
```

Its homogeneous degree35-2j permits only zero, scalar H⁵ at j5, or
scalar H³ at j10. All are divisible by H², so H|F_j². Unique
factorization now gives ONLY Delta|F_j, not H|F_j. Thus j<=12.
The same H²-normality/degree-and-weight argument gives deg_g F_j<=5.

Finite R-adic division, with ordinary receiver degree F<=14 and G<=23,
gives exact normal blocks

```text
F=P0+R_s P1+R_s² P2, ord Pi>=j, w(Pi)<=3-i,
G=sum_(i=0)^4 R_s^i Qi, ord Qi>=2j, w(Qi)<=5-i.   (3)
```

Division preserves combined homogeneity and never lowers s-order.
Every normal coefficient of weight<=5 has g-degree<=2: a g-degree>=3
monomial would need p-degree>=2 and would not be normal. This is NOT
injectivity on the two reduced golden branches.

Suppose first that H does NOT divide F_j. Then P0_j!=0. Subtracting H
multiples preserves Delta-divisibility, so P0_j is divisible by Delta.
Its g-degree<=2 and homogeneity force the exact shape

```text
P0_j=lambda*p^(13-j)*L*M=lambda*p^(12-j)*Delta,
lambda in K*, 1<=j<=12.                         (4)
```

This proves, rather than assumes, the vanishing on BOTH reduced lines.
At the double root g0=-p/t,

```text
(P0_j)_g(g0,p)=lambda*(t-1)*p^(14-j)!=0.         (5)
```

The alternative P0_j=0 means F_j=H C; it is not covered by (4).
It is retained explicitly in Section8 below.

## 3. Exact moving critical point and Morse field coordinate

At g0=-p/t, H_g=0 and

```text
H(g0+w,p)=t(t-1)p³ w²+rho*p² w³.               (6)
```

Therefore R_(s,g)=0 has a unique solution g_c(s,p) in K(p)[[s]] with
constant term g0. Put xi_s=R_s(g_c,p), kappa=ord xi_s>=1, infinity
allowed. Since R_s is cubic in g,

```text
R_s(g_c+w,p)=xi_s+w²(a_s+rho*p²*w),
a_s=(1/2)R_(s,gg)(g_c,p), a_0=t(t-1)p³!=0.      (7)
```

Work in E=Kbar(p^(1/2)), with the unique extended d/dp. Choose one
square root of a_0; the formal square root of the unit in (7) exists.
Set zeta=w*sqrt(a_s+rho*p²*w). Its inverse is a formal series
w=w_s(zeta) with coefficients in E[[s]] and invertible linear term.
Exactly,

```text
R_s=xi_s+zeta².                                (8)
```

All inverse coefficients have NONNEGATIVE s-order; p poles are allowed
and do not change s-order. This is a field chart, not the nilpotent
quotient by M². No Euler argument below is made on that quotient.

Uniqueness under simultaneous scaling of s,p shows g_c has combined
degree1, xi_s degree5, a_s degree3, and zeta degree5/2. Thus a coefficient
of s^r zeta^n in the transformed P0 has p-degree15-r-5n/2. Fractional
p powers occur only in E, where derivatives and Euler grading are literal.

In this coordinate write

```text
P0(g_c+w_s(zeta),p)=theta_s+ell_s*zeta
                       +sum_(n>=2) d_(n,s)*zeta^n.
q0=ord theta_s>=j+1 (or infinity), ord ell_s=j,
ord d_(n,s)>=j, ell_j!=0.                       (9)
```

The constant bound follows from P0_j(g0,p)=0; the linear assertion is
(5) divided by sqrt(a_0). All other bounds follow from the nonnegative
s-orders in the inverse, not from discarding moving-coordinate terms.
The same coordinate substitution preserves the lower bounds j for P1/P2
and2j for G whenever zeta has positive s-order.

Earlier constants REALLY can occur. The degree-five control R_s=H(g+s,p)
has g_c=g0-s, xi_s=0. At j10 choose the normal coefficient P0_10=p²Delta.
Then

```text
P0_10(g_c,p)=-(t-1)p⁴*s+t*p³*s².
```

The resulting constant order is11, below the suggested6j/5=12 balance.
This is a countercontrol to ignoring the shift, NOT a full source pair.
The next two sections allow and eliminate these earlier constants using
the actual source bracket; they do not assume them absent.

## 4. The field Euler lemma used in both regimes

If monic P,Q in E[Y] have degrees m,n and obey

```text
EP=mhP, EQ=nhQ, E=p*d_p+h*Y*d_Y, h!=0,
[P,Q]_(Y,p)=0,
```

then p[P,Q]=h(nP_Y Q-mP Q_Y). Consequently the Y derivative of
Q^m/P^n is zero, and monicity forces Q^m=P^n. UFD in the FIELD ring
E[Y] gives P=W^(m/d), Q=W^(n/d) for monic W of degree d=gcd(m,n).
No claim that this holds unchanged over a nilpotent ring is made.

For m6,n10 and

```text
P=(Y²+b)³+uY+v,
```

the monic quadratic W has zero linear coefficient, by P's Y5 term;
its constant is b, by the Y4 coefficient3b. Hence u=v=0. The common-
quadratic example alone does not defeat THIS special initial shape.
For m3,n5, a depressed P=Y³+v forces W=Y and v=0.

## 5. Regime A, with the correct adaptive constant balance

Assume kappa>=2j/5. Choose

```text
r=min(j/5,q0/6), zeta=s^r Y, 0<r<=12/5<5/2.
```

Then kappa>=2r and R_s has order2r, with initial S=Y²+b (b=0 unless
kappa=2r). From (9), the F initial has order6r and equals uY+v, with
at least one of u,v nonzero: ell_j contributes if j=5r, and theta_q0
if q0=6r. They have different Y-degrees and cannot cancel. Terms
d_n zeta^n for n>=2 are later since j+2r>=7r. R_s P1 and R_s²P2
are later by the same bounds. Scalars alpha_s R_s and a0_s are later
since10+2r>6r and15>6r. Thus

```text
A_initial=S³+uY+v, of order6r.                  (10)
```

Every scalar B kernel b_i,s R_s^i with i<5 is above10r by
(5-i)(5-2r)>0. In q(R_s)F only (5/3)R_s²F can enter10r;
the b4 term and b3/alpha terms are strictly later. G has order>=2j>=10r.
If equality holds, its initial after the coordinate substitution is a
constant e in E: evaluating its first coefficient at g0 gives the only
order2j term, since both g_c-g0 and w_s(s^rY) have positive order.
There is NO lower B initial and no hidden zeta-dependent G term in this
window. Therefore

```text
B_initial=S⁵+(5/3)S²(uY+v)+e, of order10r.        (11)
```

The exact transformed source bracket is
c*s^36*g(s,zeta,p)²*(partial g/partial zeta), with order exactly36:
g0=-p/t and (partial g/partial zeta)_0=1/sqrt(a_0) are nonzero.
The initial bracket of (10),(11) occurs at

```text
6r+10r-r=15r, NOT 7*(2r).                       (12)
```

If15r<36, it must vanish. Zeta has combined degree5/2, so Y has degree
h=5/2-r>0; the initials have Euler degrees6h,10h. Section4 then forces
u=v=0, contradiction. Thus regime A is excluded for all j<=11, since
15r<=3j<=33. At j12 it is also excluded if q0<72/5, equivalently q0<=14.
The only remaining A possibility is j12, q0>=15 and kappa>=24/5,
equivalently kappa>=5, giving r=12/5 and15r=36.

At this equality the initial bracket need NOT vanish: it must match a
nonzero target coefficient c*p²/(t² sqrt(a_0)). The proposed blanket
commutation claim at j12 is therefore invalid. This report does not
classify that nonzero-Jacobian initial system or assert its consistency.

## 6. Regime B: earlier constants and both separated sheets

Assume kappa<2j/5. First suppose q0<=3kappa. Put r=q0/6. Then
2r<=kappa, r<j/5, and the same coalesced calculation as Section5 has
only a nonzero constant v correction at6r. Its G bound is STRICTLY above
10r, and

```text
15r=(5/2)q0<3j<=36.
```

The strict inequality follows from q0<=3kappa<6j/5. The common-quadratic
argument excludes this case. Thus a hypothetical source here must have
q0>3kappa, including infinity.

Now the two roots of R_s=0 in the Morse coordinate are
zeta_+=sqrt(-xi_s), zeta_-=-sqrt(-xi_s), of order kappa/2. The leading
square roots belong to E after algebraic closure of constants: xi_kappa
is homogeneous in p of integer degree5-kappa. In one finite s-Puiseux
extension both signs are retained. At these roots, (9) has GLOBAL minimum

```text
nu=min(q0,j+kappa/2)>3kappa.                     (13)
```

Higher d_n terms have order>=j+kappa, hence are later. If the two displayed
orders tie, the leading values are theta_lead plus/minus a NONZERO
ell_lead*sqrt(-xi_lead); both cannot cancel in characteristic zero.
One may vanish, which is why selecting just one sheet earlier is invalid.

Take eta=nu/3>kappa and z=R_s=s^eta Z. Exactly on both sheets,

```text
zeta_±(z)=±sqrt(-xi_s)*sqrt(1-z/xi_s).            (14)
```

This expansion is legitimate precisely because eta>kappa. Its n-th
positive correction has additional order n(eta-kappa)>0 relative to
the root. In (9), all such corrections are strictly later than the global
minimum (13); coefficients d_n start at j and n>=2, so none can precede
the transverse/constant minimum after (14). The inverse Morse series
has nonnegative s-orders as proved above. This controls ALL implicit
corrections; it does not assume derivative denominators are harmless.

The R_s P1 term has order>=eta+j>3eta, since
2eta<=2(j+kappa/2)/3<j. The P2 term is later still. Thus, simultaneously
on the two sheets, the A initial is

```text
P(Z)=Z³+v, of order3eta,
```

with a nonzero constant tuple v in the product E². Scalar A references
are later because eta<2j/5<=24/5<5. Also

```text
5eta<=5(j+kappa/2)/3<2j.
```

Hence EVERY G term is strictly above5eta after the legitimate substitution,
and all scalar B kernels are later. The B initial is monic on both sheets:

```text
Q(Z)=Z⁵+(5/3)v Z², of order5eta.                (15)
```

The source bracket in z,p is
c*s^36*g²*(partial g/partial zeta)/(2zeta). Its order is36-kappa/2 on
each sheet, with a nonzero leading coefficient. Since

```text
7eta<=7(j+kappa/2)/3 < 36-kappa/2,
```

the initials commute. The strict inequality is exactly implied by
7j+5kappa<9j<=108. Their Euler degrees are3h,5h for h=5-eta>0.
Apply Section4 separately on each field factor: both v components vanish,
contradicting their global nonzero minimum. This excludes regime B for
ALL1<=j<=12 in the non-H-divisible branch.

## 7. Exact outcome and the two missing continuations

Combining Sections5–6 proves the source implication (R) whenever H does
not divide the canonical F_j. At that remaining j12, (4) is lambda*Delta,
as in the accepted degree-three control. This does not turn that control
into a full source point. The exact equality bracket needs its own source
coefficient argument; no such argument is imported or attempted here.

If H divides F_j, write F_j=H C. Then H-normality at j10 and degree
give j<=9; deg C=10-j, w(C)<=2, deg_g C<=2. If C vanishes on BOTH reduced
lines, C is a multiple of L M. The quotient has weight<=-8, which forces
p² (a constant or single p monomial has weight>=-7). Therefore deg C>=4
and j<=6. This verifies the proposed bound for that hidden-C subcase,
but no ramified W³ balance or exclusion of this alternative is claimed.
If C does not vanish on both lines, its source-global handling is likewise
outside this bounded non-H-divisible discriminator. These alternatives
cannot be silently absorbed into (R).

The precise correction to root's initial proposal is thus: regime A needs
the adaptive q0 balance and the Jacobian order15r; j12 at r12/5 is resonant.
Regime B needs either elimination of q0<=3kappa or the two-sheet global
minimum nu, not an assumed j+kappa/2 balance on one selected sheet.
The complete golden receiver/source and JC2 remain unexcluded.

## 8. Tiny exact controls, provenance and stop

Standalone check.py SHA256
e49907ee44870195b3d437ea7b095619ecd9f6bc315702dc6932cfe7937687f8
uses exact Q[rho]/(rho²-3rho+1) arithmetic for both conjugates. It
materializes only factors of degree<=5: (6), the transverse Delta jet,
and the H(g+s,p) moving-center/earlier-constant control. Scalar order
checks exercise the j12 equality and a q0=3kappa boundary; the opposite-
sign control admits cancellation on one sheet but not both. The common-
quadratic coefficient arithmetic is a control only; Section4 gives the
universal factor proof without expanding degree6/10 polynomials.

Ten modes (positive and four actual changed-object/order controls, normal
and -O) pass in2.675seconds. They alter the critical shift, discard the
earlier constant, use the wrong ramified bracket order, or identify the
two split signs; each intended failure is retained. Commands are direct
prlimit CPU25/512MiB with Python -I -B and outer subprocess30wall, with
no inner timeout and no gating asserts. No actual H²/H³/H⁵/R powers or
complete A/B/source rows were expanded.

Full source/report hashes, commands, rc/stdout/stderr and custody are in
the owned box. No uniform-theorem verdict, live cross/gate, blind report,
extra agent, AWS/SSH/CAS/solver, protected project or shared ledger was
accessed or changed. This report is an UNREVIEWED proof of a limited
source implication, not promotion. Transactional publication; all children
and writers terminal at handoff. STOP/IDLE.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17824`.
- Body SHA-256:
  `0c59263b73729ead96ffe504ff34d0f00f8f83927b37bce9f71f8d4d78b8921e`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
