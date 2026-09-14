# Degree-seven local consumers and conditional F9 exclusion

Coordinator /root, 2026-09-09. NEW / UNREVIEWED. This is a full local proof
for explicitly stated reference hypotheses, followed by a CONDITIONAL
composition with the now accepted weighted-reference framework. It is not a
promoted F9 exclusion, maximum-degree theorem or resolution of JC2.
All mathematics below is factored prose; ZERO mathematical subprocesses.

## 1. Exact reference theorem and dependencies

Work in characteristic zero. Enlarge the coefficient field to its algebraic
closure k when necessary; nonexistence there implies nonexistence over the
original field. Put

    M=b²-a², V=b(b²-3a²/2), K=M²V.

Assume finite polynomial homogeneous dilations A_s,B_s of combined degrees
21,35 with s,a,b of degree1, a polynomial reference R_s of combined degree7,
and polynomial F,G such that

    R_s|s=0=K,
    [A_s,B_s]_(a,b)=2c*s^51*a³, c!=0,
    A_s=R_s³+alpha*s^14*R_s+a0*s^21+F,
    B_s=R_s^5+sum_(i=0)^4 b_i*s^(35-7i)*R_s^i+q_s(R_s)*F+G,
    q_s(z)=(5/3)z²+(4/3)b4*s^7*z+(b3-5alpha/9)*s^14,
    j=ord_s F>=1, ord_s G>=2j.

The scalars alpha,a0,b_i belong to k. F,G have combined degrees21,35;
R_s=K+sum_(i=1)^7 s^i R_(7-i). Infinite order is allowed for zero
coefficients and for G, not for F. The common top implies
ord_s(B_s-R_s^5)>=1. No receiver support, lower face, inverse polynomiality
or coefficient-degree restriction is assumed in this local theorem.

We prove three consumers:

- If F_j=K*C and C does not vanish at a chosen SIMPLE line factor of K,
  this is impossible for j<=13.
- At either DOUBLE line factor T=b-a or b+a, transverse multiplicity
  ord_T(F_j)=2 is impossible for j<=13.
- At either such double line, multiplicity3 is impossible for j<=9.

These three statements imply nonexistence whenever additionally

    F_j=K*C, 1<=j<=13, deg C=14-j, K does not divide C.       (1.1)

The separate source-framework candidate is
`xmodel/f9-weighted-reference-source-astra-20260909.md`, SHA
`d7fb64afe6c02c50aa2756c1e2600c8b3f3f05077f200c522a794cc121590c32`,
transaction `c56d203bae1c771dee24dffb4adf676af3c27616fb27ac757d171b9708af16a7`.
It asserts these hypotheses and (1.1) from the actual weighted source.
Root verified its terminal custody/current pins and read it WHOLE before
this proof. It was UNREVIEWED when this manuscript began. During drafting,
the independent Sol gate passed and root promoted its necessary theorem
as16d: gate SHA
`b6f75081feb3c8d6f6884659e7f002564daa0f08819c6149a58ec79cacee188d`,
receipt SHA `47fbbbf44beb0ab9722eac661fa1a0fcaf031179024577d05a42b8dd048909c0`.
Terminal/original absence and allninecurrent pins were verified06:50:13
BEFORE root read that gate WHOLE. This local theorem is independently
proved from explicit reference assumptions; its OWN review is still pending.

The accepted degree-five local proof motivated the mechanism:
`xmodel/d125-weightfree-local-consumer-coordinator-20260909.md`, SHA
`d4fd2a0e6549edbf9e65f8aa59e2fc2a1d6bbbc0299188fdd6adf96f340c8f51`.
Root checked that current hash and read all410 lines. Its old degree15/25,
target36 and endpoint resonance are NOT imported as the present theorem.
Every degree-seven bound and transformation below is rederived. No endpoint
resonance is needed here: all the decisive inequalities will be strict.

## 2. Charts, formal homogeneity and two elementary Euler lemmas

For EVERY selected line use y=b and X=a, so the original bracket is

    [A_s,B_s]_(y,X)=-2c*s^51*X³.                         (2.1)

The line is y=gamma*X; gamma is0 or +/-sqrt(3/2) for a simple line,
and +/-1 for a double line. X is a transcendental, nonzero generic
coordinate, not a sampled point. All local calculations are identities
over E=k(X^(1/2)), with its usual X-derivation. A finite Puiseux extension
in s is allowed when a square root or a rational balance requires it.

Formal inverses with unit transverse derivative have nonnegative s and
local-coordinate orders. All substitutions preserve the Euler grading:
s,X have degree1; the coordinate z=R_s has degree7; the Morse coordinate
zeta below has degree7/2; y has degree1. Their homogeneous coefficients
are scalar multiples of rational powers of X. Thus after a balance
z=s^eta Z or zeta=s^r Y, the initial coefficients retain the claimed
Euler identities in X,Z or X,Y. No arbitrary coefficient function is
silently replaced by a scalar. The relevant constants of E's derivative
are k, and all power identities can be tested in the polynomial UFD E[Z].

First lemma: suppose P is monic of degree m>=1 in Z, Q!=0 has degree n,
[P,Q]_(Z,X)=0, and (X*d_X+h*Z*d_Z)Q=Lambda*Q. If q_n is Q's leading
coefficient, the coefficient of Z^(m+n-1) in the bracket is m*q_n', since
P_X has degree at most m-1. Hence q_n'=0 and (Lambda-n*h)q_n=0.
In particular a nonzero value of Lambda-n*h is impossible. This includes
n=0 but not m=0; P=1,Q=X is a changed-hypothesis countercontrol.

Second lemma: monic commuting P,Q of degrees3e,5e and Euler degrees
3e*h,5e*h, with h!=0, satisfy

    X[P,Q]=h*(5e*P_Z*Q-3e*P*Q_Z)=0.

Thus Q³/P^5 is Z-constant; comparison of leading coefficients makes it1.
Unique factorization gives P=W³,Q=W^5 with monic W of degree e.
For e=1, a depressed cubic P=Z³+uZ+v forces W=Z, hence u=v=0.
For e=2, if P=(Y²+b0)³+U(Y) with deg U<=3, the coefficients of Y5
and Y4 force W=Y²+b0, so U=0. This latter conclusion would fail if
a degree4 correction were allowed; (Y²+b0+t)³ is a control.

## 3. Simple line consumer, all j<=13

At a simple line K_y is a unit over k(X). There is a formal inverse
R_s(y,X)=z near that line, including the moving root at z=0. Write the
entire transformed F as sum f_n(s,X)z^n. Every ord f_n>=j. Since
F_j=K*C with C nonzero at the line, ord f_1=j while q0=ord f_0>j.
Set eta=min(j/2,q0/3). Then0<eta<=13/2<7, and eta is finite.

After z=s^eta Z, all n>=2 terms of F are later than3eta, since their
orders are at least j+2eta>3eta. Its linear and constant terms are at
least3eta and at least one attains it. The A initial is therefore

    s^(3eta) P, P=Z³+uZ+v, (u,v)!=(0,0).

The A scalars are later by14-2eta and21-3eta. All B scalar kernels
are later than5eta by (5-i)(7-eta)>0. The two lower coefficients of
q_s are later by7-eta and14-2eta. Its leading (5/3)z²F contributes
at5eta, with Z-degree at most3.

The transformed G still has every coefficient of order>=2j. An earlier
initial at nu<5eta could have degree only0, because2j+eta>=5eta.
Choose it nonzero if it exists. Under the inverse, the bracket target
has s-order51, because y_z is a unit with nonzero initial coefficient;
passing to the Z-bracket multiplies by s^eta. Since

    2eta+nu < 7eta <=91/2 <51,

the earlier initial must commute with P. Its Euler factor35-nu is
positive, contradicting the first lemma. Thus there is no earlier B
initial. At5eta, G can contribute only a linear term and a constant.
Consequently B has a monic quintic initial Q. With h=7-eta>0, P and Q
have Euler degrees3h,5h. The same strict inequality gives [P,Q]=0.
The second lemma forces u=v=0, a contradiction. This proves the
simple-line consumer without any restriction at a sampled point.

## 4. Double line: exact Morse inverse and the coalesced regime

Fix y=epsilon*X, epsilon=+1 or-1. The coefficient of (y-epsilon*X)²
in K is -2epsilon*X5, a nonzero unit in k(X). The formal implicit
function theorem applied to R_y gives a moving critical point y_c(s,X).
Put xi_s=R_s(y_c,X), kappa=ord_s xi_s>=1, allowing infinity. Taylor
factorization gives exactly

    R_s(y_c+w,X)=xi_s+w² U_s(w,X), U_0(0,X)=-2epsilon*X5.

Define zeta=w*sqrt(U_s). Its formal inverse has nonnegative s,zeta
orders over E, and R_s=xi_s+zeta². Its leading derivative y_zeta is
a nonzero constant times X^(-5/2). This is a full formal inverse, not
a finite Taylor truncation; zeta has combined degree7/2.

Write the transformed F as sum c_n(s,X)zeta^n. If d=ord_T F_j is2
or3, then ord c_n>=j for every n, ord c_d=j, and ord c_n>j for n<d.
The last assertions follow by reducing the inverse modulo s; its linear
coefficient at the selected root is a unit. Define

    r=min_(0<=n<=d) ord(c_n)/(6-n), 0<r<=j/(6-d).

First suppose kappa>=2r, including xi=0. At zeta=s^rY all n<=d
terms have order>=6r and at least one attains it; n>d terms have
order>=j+(d+1)r>=7r>6r. Thus F has a nonzero polynomial initial
U(Y) of degree<=d. R has initial Y²+b0 at2r, where b0=0 unless
kappa=2r. For the stated ranges,

    d2,j<=13: r<=13/4<7/2, 15r<=195/4<51;
    d3,j<=9:  r<=3<7/2,    15r<=45<51.             (4.1)

All A scalar terms are later than6r. Hence A's initial is the monic
degree6 polynomial P=(Y²+b0)³+U(Y). For the WHOLE B, use
ord_s(B_s-R_s^5)>=1. After the nonnegative-order inverse, a possible
earlier initial at nu<10r has degree n with n*r<=nu-1; R_s^5 itself
has no earlier term. Its bracket with P is zero because5r+nu<15r<51.
Writing h=7/2-r>0, the first Euler lemma excludes it: its factor is

    35-nu-n*h > 35-7nu/(2r) >0.

At10r, R_s^5 supplies the unique monic degree10 term; all contributions
from B_s-R_s^5 have degree<10. Thus B has monic initial Q, of Euler
degree10h, and P has degree6h. The unit y_zeta leaves the target's
s-order51 unchanged, so (4.1) gives [P,Q]=0. The common-quadratic
lemma forces U=0 because d<=3, a contradiction. Equality kappa=2r
was INCLUDED; it must not be sent to a separated-sheet argument.

## 5. Separated double line: both sheets and the entire remainder

Now kappa<2r, so xi is nonzero and kappa is finite. For every n,

    ord c_n+n*kappa/2>3kappa.                       (5.1)

For n<=d use ord c_n>=(6-n)r; for n>d use
ord c_n>=j>=(6-d)r. Define the even/odd regroupings

    U(z)=sum_(m>=0) c_(2m)*(z-xi)^m,
    V(z)=sum_(m>=0) c_(2m+1)*(z-xi)^m.

Each coefficient U_l,V_l has order>=j. The m-th contribution to U_l,
for instance, is binom(m,l)c_(2m)(-xi)^(m-l), whose order tends to
infinity as m increases. The series are coefficientwise s-adically
convergent, and (5.1) implies

    ord U_l+l*kappa>3kappa,
    ord V_l+kappa/2+l*kappa>3kappa.                 (5.2)

Cancellation raises orders. Discreteness after a finite Puiseux extension
preserves the strict lower bounds. Put b_s=sqrt(-xi), ord b_s=kappa/2.
The exact two sheets and restrictions of F are

    zeta_pm=+/-b_s*sqrt(1-z/xi),
    F_pm=U(z)+/-b_s*sqrt(1-z/xi)*V(z).              (5.3)

These lie in a Puiseux Laurent coefficient field followed by [[z]].
Their individual z coefficients need NOT have nonnegative s-orders.
No proof below makes that false assertion. Homogeneity gives the leading
coefficient of xi as a scalar times X^(7-kappa), so adjoining b_s needs
only the stated algebraic/Puiseux extensions with rational X powers.

Without summing across signs define

    q0=min(ord U_0,kappa/2+ord V_0)>3kappa,
    q1=min(ord U_1,kappa/2+ord V_1)>2kappa,
    eta=min(q0/3,q1/2)>kappa.                      (5.4)

For d2, the c2 term gives ord U_1=j, all later terms being strictly
later; hence eta<=j/2. For d3, c3 gives ord V_1=j, so
eta<=j/2+kappa/4<2j/3. Thus eta is finite, eta<j, and eta<7 for
both stated ranges. Individual q0 or q1 may be infinite.

At z=s^eta Z every positive binomial shift in (5.3) is later than
its OWN base by a positive multiple of eta-kappa. Bases of degree
l>=2 are later than3eta, since j+2eta>3eta. The l0/1 bases are at
least3eta with at least one equality. At an attained degree the two
sheet coefficients have tuple (a+b,a-b), which cannot vanish on BOTH
sheets unless a=b=0. Different degrees do not cancel each other.
Consequently the actual A initials on the two sheets are

    P_pm=Z³+u_pm Z+v_pm,
    (u_+,v_+,u_-,v_-) !=(0,0,0,0).                (5.5)

One sheet's correction may vanish; it alone gives no contradiction.
The scalar references are later because eta<7. Both initials are Euler
homogeneous of degree3h for h=7-eta>0.

Apply the SAME regrouping to the ENTIRE G. Its even/odd coefficient
functions have orders>=2j. The earliest order across both sheets is
the minimum of their BASE orders ord U_(G,l)+l*eta and
kappa/2+ord V_(G,l)+l*eta. A positive binomial shift is strictly
later than its own base; it cannot attain a global minimum unless that
earlier base existed. At a minimum the two-sign tuple prevents
cancellation on both sheets. This controls all coefficients, not a finite
sampling. Bounds tending to infinity with l make these minima legitimate.

If an initial below5eta occurs, its degree is0 for d2, since2j>=4eta;
its degree is at most1 for d3, since2j>3eta. Select a sheet on which
an earliest such initial Q at nu<5eta is nonzero. The B scalar kernels
and lower q_s terms are all later than5eta by7-eta and its positive
multiples; z5 and (5/3)z²F begin at5eta. Thus Q is an actual earlier
B initial, not an isolated remainder coefficient mistaken for one.

The target in (z,X) is (2.1) times
y_z=y_zeta/(2zeta_pm). After substituting z=s^eta Z, its s-order is
51-kappa/2 with nonzero generic leading coefficient; X³ and y_zeta
do not vanish generically. Expressing the bracket in (Z,X) adds eta
by the chain rule, including the X dependence of the inverse. The bounds
that keep the leading bracket strictly below its target are

    d2: 7eta+kappa/2 <=7j/2+kappa/2 <15j/4<=195/4<51;
    d3: 7eta+kappa/2 <=7j/2+9kappa/4 <5j<=45<51.    (5.6)

Here kappa<2r<=2j/(6-d) is essential. Thus
2eta+nu<7eta<51-kappa/2 and [P_pm,Q]=0. If Q has degree0 its
Euler factor35-nu is positive. If it has degree1 the factor is
35-nu-h=28-nu+eta>28-4eta>0, since eta<7. The first lemma gives
a contradiction. There is no earlier G or B initial on either sheet.

At5eta the entire G can contribute at most a linear term and a
constant in both d2 and d3. Shifts of earlier bases cannot reappear at
this order: the preceding argument excluded every earlier base across
the pair of sheets. The complete B initial on each sheet is therefore

    Q_pm=Z5+(5/3)Z²(u_pm Z+v_pm)+ell_pm Z+e_pm.

It is monic5 with Euler degree5h. Inequality(5.6) again makes the
initial bracket zero. The common-linear lemma forces u_pm=v_pm=0 on
EACH sheet, contradicting(5.5). This proves the separated d2,j<=13
and d3,j<=9 consumers. A hypothetical eta=kappa would invalidate the
positive binomial-shift argument; (5.2)-(5.4) explicitly exclude it.
The case xi=0 belongs only to Section4, never to this division by xi.

## 6. Exhaustive factor cover and conditional actual-source consequence

Assume(1.1). K has THREE distinct simple lines, the factors of
V=b(b²-3a²/2), and TWO distinct double lines, the factors of M=b²-a².
These five lines are distinct in characteristic zero. Section3 forces
each simple line to divide C for every j<=13. At a double line not
dividing C the multiplicity of F_j=K*C would be exactly2, excluded by
Sections4-5 for all j<=13. Thus rad(K)=M*V divides C. Since it has
degree5 while deg C=14-j, necessarily j<=9.

But K does not divide C. Every simple line is already present, so at
least one of the two double lines has multiplicity EXACTLY1 in C.
Its multiplicity in F_j is exactly3, excluded by Sections4-5 for j<=9.
This contradiction proves the conditional nonexistence theorem.
It covers higher multiplicities at the other line without presuming them
equal. It uses both separated sheets at a selected double line, not a
symmetry assumption between the two distinct double lines.

The independently reviewed16d framework supplies the displayed reference
hypotheses and(1.1). Conditional on acceptance of THIS new local proof,
the conclusion is:

    No A,B in a characteristic-zero field's polynomial ring k[g,p]
    have (2,1)-weighted leaders H³,H5 with
    H=p(p²-g)²(p²-3g/2) and [A,B]=c*g, c!=0.

The cover g=a²,p=b is injective; its bracket is precisely2c*a³.
A source over a smaller field would persist in its algebraic closure,
where the local contradiction applies. No normalization descent to the
original field is asserted. Full lower faces and inverse polynomiality
are unnecessary to this nonexistence consequence.

Accepted16a/b attach every actual ordinary degree84/140 complex Keller
counterexample to that normalized weighted source, with their named
general-normalizer/enumeration/opposite-edge/Euler imports. Consequently
the accepted framework plus THIS local proof, if the latter passes review,
exclude all actual84/140 sources at those imports.16c's guarded ideal
would then be the unit ideal by the maximal-ideal/Nullstellensatz
argument; this is an existential ideal conclusion, NOT an explicit
cofactor certificate, emitted coefficient system or executed solve.
The exact inverse criterion is not a premise of this local proof.

None of this implies a maximum-degree140 bound or all-degree JC2.
In particular the primary2017 Section6 table also contains degree126,
128,132 and135 configurations; F9 is not a census of all smaller
unexcluded families. That whole table was read again at current SHA
`49df06d11bbc4556a9b09771cdd60ca40a75b7542d327bbb622e09434e6a467e`.
The pending D108 source-coverage review is not a mathematical premise.
No ordinary-source point or counterexample has been found.

## 7. Attacks, evidence boundaries and provenance

All checks here are MANUAL factored arguments, never executed controls:

- The cover contributes2a and the uniform chart swap contributes a minus
  sign. Omitting either changes(2.1). Each local target is evaluated at
  generic X, not at X=0; its coefficient is a nonzero rational function.
- Positive-degree monicity is required by the first Euler lemma. The
  degree4 common-quadratic correction is not excluded by the second.
- All five B kernels, alpha and the lower q_s terms are retained and
  shown strictly later at the ACTUAL selected balance. They are not
  set to zero or removed by an unlicensed target automorphism.
- Coalescence includes equality and xi=0. Separation forces eta>kappa
  and retains a two-sign tuple; a single sheet could have no correction.
- A Laurent sheet expansion may have negative s-orders termwise before
  rescaling. The proof instead bounds convergent bases of the whole F/G
  and uses both signs to stop global-minimum cancellation.
- The decisive maxima are91/2,195/4 and45, all strictly less than51.
  Replacing the target with an earlier one can defeat the consumers.
  No equation whose bracket reaches the target is set to zero here.
- Polynomial UFD, derivative constants and nonzero scalars require a
  field of characteristic zero. This proof is not a nilpotent-ring or
  positive-characteristic theorem.

No pending source-compatible-reference report was consumed; the proposed
anti-diagonal pruning is unnecessary to this factor-cover argument.
An Astra colleague was separately asked to attack the changed separated
regime while root wrote this independent full proof. Its advisory agrees
with the displayed target orders but is not a frozen premise, different-
model review, or substitute for the proof. Its terminal report, if useful,
can be charged later as independently authored same-model supporting work.

Root will whole-read this own body, verify current framework/accepted-source
pins and run owned OPEN extraction before transactional publication. There
was no source expansion, coefficient stream, scalar script, CAS, AWS/SSH,
old checker, external/public write or protected-project access in this
mathematical task. Original failed Fable review records are retained;
provider failure is not evidence for or against the theorem.

## OPEN(S) RAISED

None. The exact provisional dependencies and review requirement are stated
above; no new named global research question is registered here.

## COLLISIONS

status: EMPTY

- NONE — no explicit OPEN identifier is raised; no corpus scan claimed.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19699`.
- Body SHA-256:
  `4e79c2302d7b547f6c353898d0130f7319c3842efa3f4337755e847e5214f884`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
