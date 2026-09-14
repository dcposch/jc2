# Quartic divisor mechanism and its adversarial controls

Same-model exploratory contribution to the blind Astra round, 2026-09-05.
This file is a scratch mathematical derivation, not an independent promotion.
No running lane report/artifact, blind-round submission, canonical ledger, or
jc2-lean file was opened. The receipts of the sealed 8point1, BRCR, RANK,
TOPTAIL, and DEP reports were checked for final_status=DONE before report reads.
Mathematical inputs actually read were the first three named reports.

## 1. Exact all-b product reduction

Use precisely F1--F3 of `xmodel/k16-8point1-astra-20260905.md:300` through
`:388`, over an algebraic closure of each characteristic-zero field factor
of A_t. Put b=b3, B=b2, eta=W'(0), q=2t+1, and take y and omega from that
report. All primes below denote ordinary x derivatives. Define

    z=xW-b^2/4, K=x^2 C-yb,
    Q=-Bx+3K(K+yb)/(2y^2),
    H=2xz'-3z+Q,
    Psi=3K^3(K+2yb)/(16y^4)-3BxK^2/(4y^2)
        -b eta x^2 K/(2y)-B eta x^3.

Then the exact polynomial identity is

    zH-Psi = x^2 * (left side of F3 - right side of F3).

No residual nonunit was inverted in this identity. Consequently F3 is
EXACTLY equivalent to zH=Psi, including b=0 and every root collision. Here

    deg z=deg H=2t+2, deg Psi=4t+4,
    z(0)=-b^2/4, z'(0)=-B, z''(0)=2eta,
    lead z=omega, lead H=(4t+1)omega+3/(2y^2).

The equality of the leading product to lead Psi=3/(16y^4) reduces to
3d^2=t+1. It is an identity, not the obstruction.

On b B eta !=0, K(0)=-yb !=0 and reduction modulo K gives

    z(2xz'-3z-Bx) = -B eta x^3 mod K.

Thus x and z are units in the finite Artin algebra k[x]/(K), even when K
has repeated roots. In particular gcd(K,z)=1. This is a proved useful
restriction, but being a unit in this quotient is not a contradiction.

## 2. Fixed quartic, one dimensionless parameter

Put u=K/(yx). Direct substitution gives

    Psi = x^3/16 * [3x u^4+6b u^3-12B u^2-8b eta u-16B eta].

On b B eta !=0 define

    lambda=b^2 eta/B^2, chi=Bx/b^2, v=bu/B, w=1/v.
    Phi_lambda(w)=(16lambda/3)w^4+(8lambda/3)w^3+4w^2-2w.

At a root of Psi, neither x nor K vanishes: at x=0,
Psi=-3b^4/16, and at K=0, Psi=-B eta x^3. Hence these fractions are
legitimate on that root scheme. The vanishing equation becomes

    chi=Phi_lambda(w).

The variable w is the rational function Byx/(bK); this is not a free
change of the base-line coordinate, nor a global polynomial automorphism.
It turns the actual scalar quartic into a fixed family independent of t.
The t dependence survives in K and the divisor z, and cannot be discarded.

Set r=w+1/8. Then

    Phi_lambda=(16lambda/3)r^4+(4-lambda/2)r^2
               +(lambda/12-3)r+5/16-lambda/256.

Write Delta=3lambda^2-69lambda-32. Exact discriminants are

    disc_w(Phi_lambda')=(4096/3)lambda Delta,
    resultant_w(Phi_lambda-chi,Phi_lambda')
       =-(65536/81)lambda^2 R_lambda(chi),
    R_lambda(chi)=256lambda^2 chi^3
       +(9lambda^3-336lambda^2+384lambda)chi^2
       +(-24lambda^2+660lambda+144)chi
       -4lambda^2+132lambda+36,
    disc_chi(R_lambda)=432lambda^3(lambda-36)^2 Delta^3.

These are distinct assertions: the first detects collisions of critical
POINTS of the quartic; the last detects collisions of critical VALUES.
For nonzero lambda, exactly three exceptional parameter values occur:
36 and the two roots of Delta. At lambda=36,

    Phi_36=192(r^2)^2-14r^2+11/64,
    R_36(chi)=36(12chi+1)^2(64chi-11).

This is an exact quadratic composition, with two critical points sharing
value -1/12 and the remaining critical value 11/64. It is a concrete
special family, not a generic-cover heuristic. No inference is made that
F3 forces lambda=36 or Delta=0. The generic lambda chart remains mandatory.
The b=0 chart cannot be put into this normalization and must stay separate.

In original variables, the exceptional equations can be written without
extending the scalar field:

    E36=b^2 eta-36B^2=0,
    EDelta=3b^4 eta^2-69b^2 B^2 eta-32B^4=0.

Within bB eta !=0 the three closed parameter values are covered by these
two equations. The complementary chart inverts E36 EDelta. The use of
'quartic' refers to Phi, not to a claimed bounded-degree equation in all
of the original residual variables.

## 3. Differential-compatible factor criterion

Let n=2t+2. Suppose a polynomial z of degree n has the required leading
coefficient and jets, and z divides Psi. Set Htilde=Psi/z, with exact
polynomial division by the known nonzero leading scalar omega. The leading
balance makes Htilde-H have degree at most n-1. If z is squarefree, then

    zH=Psi
    iff  2x(z')^2+Qz'-Psi' = 0 mod z.

Proof: differentiation of Psi=z Htilde gives Psi'=z'Htilde modulo z.
The displayed congruence is therefore z'(H-Htilde)=0 modulo z. Because
z' is a unit in k[x]/(z), it forces H-Htilde=0 modulo z; the degree bound
makes that equality literal. The converse is immediate.

This changes generic Abel reasoning into a concrete selection problem:
select a degree-(2t+2) factor of the actual degree-(4t+4) Psi whose derivative
satisfies a residue condition at all its roots. It is a reformulation, not
an emptiness theorem. Over an algebraically closed field every generic Psi
has many such half-degree factors before the differential condition. Mere
factorization or a quartic passport has no exclusion power.

For a root xi of z of multiplicity m, the first congruence loses m-1 jets.
One must instead retain Htilde-H modulo (x-xi)^m. A division-free-in-roots
implementation computes Htilde by polynomial long division and tests its
remainder modulo z; equivalently use confluent jets. The necessary jets of
H are

    H^(j)(xi)=2xi z^(j+1)(xi)+(2j-3)z^(j)(xi)+Q^(j)(xi),
                    0<=j<m.

The relation to Htilde jets is triangular from differentiating Psi=zHtilde
starting at derivative order m. No discriminant saturation is allowed to
stand in for the omitted collision strata.

## 4. New all-b formal non-obstruction

The sealed report already constructs formal solutions on b=0 (lines
506--530); a local-root proof cannot close that chart. The product equation
shows the same point across b!=0. Fix ANY C in k[[x]], arbitrary units
b,B,eta,y, and seek

    z=-b^2/4-Bx+eta x^2+a3 x^3+a4 x^4+...

The coefficients of zH-Psi through x^3 vanish identically. The coefficient
of x^n, n>=4, has diagonal coefficient

    -(b^2/2)(n-3) * a_n.

Therefore a3 is free, and all a_n for n>=4 are determined recursively.
The scalar diagonal is nonzero in characteristic zero on b!=0. This
constructs a formal F3 solution W=(z+b^2/4)/x for every C and every nonzero
B eta, including every local root multiplicity pattern of C. It does not
construct a polynomial of degree 2t+1 or satisfy its prescribed leading
coefficient. Global truncation remains the entire obstruction.

For example one can take b=B=eta=1, hence lambda=1. Its quartic has distinct
critical points and critical values because Delta(1)=-98 and 1!=36; yet
formal solutions exist. Thus local compatibility cannot force lambda into
the exceptional locus. Root-cover work earns continuation only after it
supplies a global divisor/truncation restriction.

## 5. Cheap tests, controls, and stopping rule

The single exact script `quartic_audit.py` is self-contained SymPy algebra
and ran in roughly 1.2 seconds with all final assertions passing. It imports
no previous generated row file. The first launch used a Python expression
identity for the centered quartic instead of algebraic expansion, so that
assertion failed; changing the comparison to exact expanded difference
resolved this implementation comparison issue. No failed suffix is counted
as a mathematical test. The final log records ALL_CHECKS_PASS.

Positive and negative controls include:

- A squarefree z for which Psi=zH passes the derivative congruence, and
  Psi=z(H+1) fails despite divisibility and the same leading data.
- The collision control z=x^2, Q=x^2, H=2x^2, Psi_mut=z(H+x): the first
  derivative congruence passes while Psi_mut-zH=x^3 !=0. This proves that
  the squarefree hypothesis cannot be silently dropped. It is an abstract
  criterion control, not a K16 counterexample.
- A coefficient-sensitive K16 degree control at t=11,d=2,y=7/23,
  omega=529/980, b=B=eta=1, C=x^10, z=omega x^24+x^2-x-1/4.
  The artificial Psi_mut=zH and the TRUE quartic Psi both have degree48
  and identical leading coefficient. Their jets through x^3 also agree,
  but [x^4](Psi_mut-Psi)=1. The true Psi does not even divide by this z
  (remainder degree14). Same degrees plus the leading normalizer cannot
  certify the actual coefficient problem.

The cheapest next mathematical discriminator is to identify a global
constraint on differential-compatible divisors of Phi_lambda, then test
it on the three exceptional lambda values and one generic lambda with
confluent factors included. A desk CAS lane could first use the banked
spine at fixed t, add E36 or EDelta, and localize at b B eta, with a hard
8-minute/<4GB cap and exact scalar field maps. A result is a fixed-chart
certificate only, even if obtained at t=8 or t=11. A modular localized
unit ideal has no automatic characteristic-zero promotion.

Stop this direction if the proposed global constraint is just the first
squarefree residue congruence, a generic degree4 passport, or the existence
of a degree-n factor. All three have explicit reasons for being too weak.
Continue only if there is a new all-t condition that uses the derivative
link and normalized polynomial truncation and retains the generic lambda
and b=0 charts. No recommendation here alters or reads the running Abel lane.
