## 6. Linked polynomial factors and contacts on the full ordered-root cover

Put n=t-1, N=t+1, and define new auxiliary polynomials

    P=xW-b^2/4,
    H=2xP'-3P-Bx+3K(K+yb)/(2y^2),
    Q=K(K+2yb)-4By^2*x,
    J=bK/(2y)+Bx,
    R=3K^2*Q/(16y^4)-eta*x^2*J.                        (RC1)

Here P is a factor, not the coefficient ring P_t and not the temporary
P0,P1 notation of Section 3. Direct expansion gives the exact identity

    x^2*F=PH-R.                                        (RC2)

In particular F3 is equivalent to PH=R in the polynomial ring. No
polynomial denominator is introduced. The leading degrees of P and H
are both 2t+2, and their leading coefficients are respectively omega
and `(4t+1)*omega+3/(2y^2)`. The leading equality in (RC2) is precisely
the already satisfied normalizer identity; it gives no contradiction.
The quartic factor in K in (RC1) uses the actual coefficient linkage
between A and D. It is absent from a generic Abel equation having only
the same degrees.

### 6.1 Units and exact contact in the possibly nonreduced K algebra

On bB eta!=0 one has P(0)=-b^2/4 and K(0)=-yb. Reducing PH=R modulo K,

    PH=-B*eta*x^3 in k[x]/(K).                           (RC3)

The right side is a unit. Therefore both P and H are units in this
finite algebra, whether or not K is squarefree:

    gcd(P,K)=gcd(H,K)=1.                                (RC4)

Because K is monic and `Res(K,x)=(-1)^(N+1)yb`, multiplicativity gives
the exact norm identity

    Res(K,P)*Res(K,H)=-(B*eta)^N*(yb)^3.                 (RC5)

This identity is compatible with a nonzero right side; it does not
force vanishing of the product. It does justify division by P and H
in the declared K quotient on this chart.

For the next contact order define

    E0=2xPP'-3P^2-BxP+B*eta*x^3.

Then

    E0=-bK(3P+eta*x^2)/(2y) modulo K^2.                 (RC6)

At a multiplicity-m root rho of K, this gives order at least m for
E0. If `3P(rho)+eta*rho^2` is nonzero, that order is exactly m. If it
vanishes, the higher contact remains in the argument. A derivative
formula at simple roots is a consequence of (RC6); it is not a
replacement that permits discarding the multiple roots.

### 6.2 A cubic intersection bound in the actual C-root algebra

Define

    Qc=16B*eta*x^3-8b^2*eta*x^2+12B*b^2*x+3b^4.

Expanding R in powers of C gives

    R=3x^8*C^4/(16y^4)-3b*x^6*C^3/(8y^3)
        -3B*x^5*C^2/(4y^2)
        +b*x^2*(3b^2+12Bx-4eta*x^2)*C/(8y)-Qc/16.       (RC7)

Consequently every solution satisfies

    PH=-Qc/16 modulo C,
    PH+Qc/16=b*x^2*(3b^2+12Bx-4eta*x^2)*C/(8y)
                                                 modulo C^2. (RC8)

These identities include b=0. On B eta!=0, Qc has degree exactly
three. Taking monic gcds yields the uniform coefficient-sensitive bound

    gcd(C,PH)=gcd(C,Qc),
    length k[x]/(C,PH)=deg gcd(C,PH)<=3.                 (RC9)

It counts intersection multiplicity, rather than just distinct roots.
In particular each of gcd(C,P) and gcd(C,H) divides Qc and has degree
at most three. The bound becomes a nontrivial restriction relative to
deg C as soon as t>=5. The norm version is

    Res(C,P)*Res(C,H)=(-1/16)^(t-1)*Res(C,Qc).            (RC10)

Common roots with C are allowed on the cubic exceptional locus. One
must not assert gcd(C,P)=1 globally. Nor can one divide C by its gcd
with PH and assume the quotient is coprime to PH: C can retain excess
multiplicity at such a root.

For an explicit audit of the exceptional discriminant,

    Disc(Qc)=768*eta*b^6*
                 (8eta^2*b^4-177B^2*eta*b^2-144B^4).    (RC11)

If this is nonzero and rho is a multiple C root where PH vanishes,
then exactly one of P,H has a simple root at rho and the other is
nonzero. On the discriminant-zero locus the correct assertion is

    min(ord_rho C,ord_rho P+ord_rho H)
        =min(ord_rho C,ord_rho Qc).                     (RC12)

Both loci remain present. At b=0 the cubic is `16B*eta*x^3`, so the
same formula keeps the distinguished zero-root collision automatically.

There is a further useful guard for a proposed rational-function
argument. On bB eta!=0, J of (RC1) need not be a unit modulo P.
If P(rho)=J(rho)=0, then Q(rho)=0. Substituting
`B*rho=-bK(rho)/(2y)` gives `Q(rho)=K(rho)(K(rho)+4yb)`.
By (RC4), K(rho)!=0, hence every such exception is supported at

    rho=2b^2/B, K(rho)=-4yb,
    C(rho)=-3yb/rho^2, W(rho)=B/8.                     (RC13)

This is a retained exceptional chart, not an impossibility proof.
Dividing by J without treating it would omit part of the target.

### 6.3 Repeated roots on the finite free ordered-root cover

Write `C=product_(i=1)^n(x-rho_i)` on the finite free cover from
Section 4. The equations `P(rho_i)H(rho_i)=-Qc(rho_i)/16` alone do
not impose divisibility by C on repeated-root fibres. The following
polynomial recursion preserves the full information. Starting with
`f0=PH+Qc/16`, define

    a_i=f_(i-1)(rho_i),
    f_i=(f_(i-1)-a_i)/(x-rho_i), i=1,...,n.              (RC14)

Each quotient is polynomial in x, the coefficients, and the ordered
roots. Vanishing of every a_i is equivalent to C dividing f0. On a
fibre where ordered roots coincide, (RC14) imposes the successive
Hermite jets with no Vandermonde inversion. For the C^2 contact in
(RC8), apply the same rule to the ordered list twice, starting with
`f0-b*x^2*(3b^2+12Bx-4eta*x^2)*C/(8y)`. This subtracts the prescribed
first-order contact before testing divisibility by C^2.

The universal driver `rootcover_identities.py` checks (RC2), (RC6)–
(RC8), (RC11), and the algebra used in (RC13) over Q. Its eight PASS
markers include repeated-root resultant identity controls. Those
control polynomials check identities; they are not asserted to be
normalized F3 solutions. The unresolved condition is still the
prescribed differential factor

    H=2xP'-3P-Bx+3K(K+yb)/(2y^2)

together with PH=R. Existence of an arbitrary factor of R does not
supply this differential factor. The contacts and norms do not
currently contradict that global requirement.

## 7. Infinity resonance, generic indices, and why local recursions do not close

For a formal Laurent perturbation `W -> W+h*x^k` with k<0, holding
C,B,b,eta fixed, the leading linear coefficient at x^(q+k) is still

    lambda_k=2omega*(k+2t+3+6d).

There is exactly one possible vanishing index,

    k*=-2t-3-6d=-6d(d+1)-1.                             (L1)

It is negative on both embeddings for t>=2, so it cannot invalidate
Theorem H. It is integral if and only if d is an integer. Indeed an
integral k* makes d rational. Writing d=a/c in lowest terms in
`3a^2=(t+1)c^2` forces c^2 to divide 3, so c=1. Conversely integer d
makes k* integral. Thus the arithmetic split of indices is exact:

| factor | Laurent resonance k* | coefficient exponent q+k* |
|---|---:|---:|
| generic t, d irrational | no integral resonance | none |
| t=3m^2-1, d=+m | -6m(m+1)-1 | -6m-2 |
| t=3m^2-1, d=-m | -6m(m-1)-1 | 6m-2 |

For m>=2, the negative factor's exponent 6m-2 lies in the actual
residual range 2,...,2t. At the first such index t=11 it is x^10.
At t=2,d=-1 it is x^4. On the positive factor the resonance is below
degree zero and outside the polynomial residual list. This identifies
where a Laurent recurrence must impose a compatibility equation
instead of solving for one additional negative coefficient.

It does **not** prove generic-index nonexistence. For generic d all
negative Laurent coefficients can be solved recursively, producing
a formal tail. The unresolved assertion is that these negative
coefficients cannot all vanish on B eta!=0. A finite nonempty
negative tail would still violate polynomial normalization. Where
the relevant diagonals are
nonzero, the residual rows correspond triangularly to the first
q-2 negative coefficients; requiring all of those to vanish is the
same polynomial truncation problem. At a resonance the corresponding
compatibility row has to be retained, not suppressed or interpreted
as automatic nonvanishing.

There is a complementary local obstruction to a finite-jet proof at
x=0. For arbitrary formal C and fixed B,eta, expand

    W=-B+eta*x+w2*x^2+w3*x^3+....

The coefficients x^0 and x^1 of F vanish identically. If b!=0, w2 is
free and, for every n>=2, the x^n row is affine in w_(n+1) with
diagonal `(1-n)b^2/2`, a unit. It uniquely solves the subsequent local
coefficients. If b=0 and B!=0, the x^n row for n>=2 instead has the
diagonal `-(2n-1)B` on w_n, again a unit. In particular
w2=eta^2/(3B) on b=0. Thus local formal solutions exist with B eta!=0
for a fixed polynomial C as input; they need not truncate or have
the required normalized leading term at infinity. This is not a
polynomial counterexample to (PS).

The diagonal assertions follow directly by collecting the highest
local unknown. `infinity_structure.py` checks the universal infinity
identities and several exact local coefficient instances; the proof
above supplies all n. A successful proof must couple polynomial
truncation with the linked coefficients globally. No missing finite
jet or nonintegral resonance alone can replace that task.

## 8. Fresh exact full-cone controls, including the t=2 correction

`controls_emit_direct.py` constructs F from the displayed equation,
solves exactly the high coefficients of Theorem H, and emits the
remaining rows. It imports no prior generated spine rows. The residual
generator order is `(c1,...,c_(t-1),b)` with weights
`(1,...,t-1,t+1)`. Its coefficient field is Q for each t=2 factor and
`Q[d]/(3d^2-t-1)` at t=3,4. These latter polynomials are irreducible;
exact identities over their fields cover both embeddings after
algebraic closure. The high and low row assertions are checked before
forming any standard basis.

| exact field/factor | dim R_t/J_t | field length | B eta in J_t? | (B eta)^2 in J_t? |
|---|---:|---:|---|---|
| t=2, d=-1, y=1/5 | 1 | infinite | yes | yes |
| t=2, d=+1, y=2/5 | 0 | 12 | yes | yes |
| t=3, 3d^2=4 | 0 | 66 | no | yes |
| t=4, 3d^2=5 | 0 | 338 | no | yes |

These are exact characteristic-zero computations. In particular
replacing radical membership by ideal membership would already fail
at t=3,4. The nilpotence exponent two there is not extrapolated to
all t. Standard-basis files and the declared ring and rows are saved
per factor. Their lengths agree with the charged controls; the new
calculation uses the direct F3 reconstruction.

The exceptional t=2 calculation can be displayed in full. Put c=c1,
C=x+c, d=-1, y=1/5. The reconstructed polynomials are

    B=18c^5/125-3c^2*b/5,
    eta=3c^4/10+9c*b/2.

The direct residuals are

    E2=441c^8/2500-6c^5*b/25-9c^2*b^2/4,
    E3=102c^7/25-93c^4*b/5,
    E4=177c^6/50-33c^3*b/2.

There is an explicit polynomial identity over Q[c,b]:

    B*eta=(6c/5)E2-(72c^2/1025)E3+(171c^3/5125)E4.     (C1)

The ideal also has the standard basis, up to nonzero rational
normalizations,

    59c^6-275c^3*b, c^4*b, c^2*b^2.                    (C2)

Its radical is (c): c^2*b^2=0 gives c=0 or b=0 at a geometric point,
and b=0 in the first equation forces c=0. Thus its reduced support
is exactly the free b-axis. Substituting c=0 gives (M5), so B=eta=0
at every point, while b can be nonzero. This is an actual surviving
positive-dimensional cone, not a numerical dimension artifact.

Equation (C1) proves that the product is forced zero even in the
nonreduced coordinate ring on this fibre. The weaker (8.1) criterion
holds and V0 fails, exactly as in the frozen reports. The prompt's
negative-control wording for B eta cannot hold simultaneously with
(F1)–(F3). The corrected negative control is preservation of this
free b-axis. At y=2/5 the exact Q computation gives length 12 and
another saved direct row certificate for B eta, while (M6) excludes
the b-axis away from zero.

The small independent `controls_t2_certificate.py` verifies (C1), the
y=2/5 certificate, and both explicit monomial families in SymPy.
This checks signs and the constant normalization without relying
only on the same standard-basis engine used for the dimension table.

## 9. Exact split-index theorem on the maximally coincident-root locus

**Theorem C (finite indices).** At each t in {11,26,47}, on both factors
d=+2,-2; +3,-3; +4,-4 respectively, every normalized solution with

    C=(x-a)^(t-1)

has a=b=B=eta=0 and W=omega*x^q. This theorem includes arbitrary b
and the full multiplicity t-1 of the root a. It is a statement on
this entire stratum, not a proof at the corresponding whole index.

For a=0, Section 5 applies. If a!=0, the weighted action sends a to
one and b to an arbitrary new scalar. Set

    alpha=3/(4y^2), V=W/alpha, beta=B/alpha,
    e0=eta/alpha, u=b*y,
    a0=x^3*C^2, delta=2u*x*C, K0=x^2*C-u.

The notation a0 here denotes a polynomial, not the split-tail scalar.
The normalized residual F/alpha^2 is exactly

    2xVV'-V^2-beta*V+2a0*V-delta*V-a0^2/3+a0*delta/3
       +beta*(a0-delta)-(2u^2/3)*V'+(2u/3)*e0*K0
       +beta*e0*x-(2u^2/3)*a0/x+(4u^2/3)*(beta+V)/x.   (C3)

The quotients are polynomial. The leading V coefficient is
`1/(6d+3)`. With C=(x-1)^(t-1), Theorem H constructs the unique
candidate using exact rational arithmetic in u on each split factor.
V's coefficients and beta are affine in u. The top two lower residuals,
those at x^(2t) and x^(2t-1), are quadratic polynomials in Q[u]. At
each of the six listed factors their gcd is one. Therefore they have
no common root even over the algebraic closure, proving the theorem.

The driver `rigidity_coincident_allb.py` performs this construction
from the equation and binomial coefficients, with no imported row
files. Every high row and both automatic low rows are checked before
the two residuals are used. It stores the exact coefficient field,
row degrees, gcd result, and unit-certificate checks. At t=11 there
are also durable integer certificates independent of the gcd routine:

    rigidity_coincident_t11_dplus2_certificate.json
    rigidity_coincident_t11_dminus2_certificate.json.

Each records primitive quadratics `f=a*u^2+b*u+c` and
`g=A*u^2+B*u+C` (letters local to this certificate), and integers

    Delta=a*B-A*b, epsilon=a*C-A*c,
    N=a*epsilon^2-b*epsilon*Delta+c*Delta^2 !=0.

The verified identity is

    [Delta^2+A*(a*Delta*u+b*Delta-a*epsilon)]*f
      -a*(a*Delta*u+b*Delta-a*epsilon)*g=N.              (C4)

Dividing by the exact nonzero integer N gives a Q[u] unit certificate.
Its magnitude is irrelevant to the proof; the files contain all
integers without rounding. At t=26,47 the exact rational gcd and
integer identity checks also pass. This is exact Q, not a modular
Rabinowitsch inference.

The same driver excludes a!=0 at both t=2 factors, preserving the
a=0 exceptional family. For d=-1 the primitive top two residuals in
u are `1375u+59` and `-775u-34`; their gcd is one. Thus this control
also retains, rather than contradicts, Section 8.

No uniform formula or sign proof for the two-row resultant has been
obtained. A possible Euler-derivative relation between the two rows
does not hold in the exact t=11 checks. The measured nonzero
resultants at t=11,26,47 are not extrapolated to other split indices
or generic indices. Proving their nonvanishing uniformly would close
the maximally coincident-root stratum, still a proper subcase of (PS).

## 10. Bounded t=8 homogeneous computations and promotion gate

The direct t=8 reconstruction was generated afresh modulo p=32003,
at d=31750 (so d^2=3), equivalently y=11288. All sixteen w pivots and
the B pivot were nonzero. The leading and automatic low rows passed.
The fifteen residuals were checked monomial by monomial for weights
32,31,...,18 in the ring with variable weights (1,2,3,4,5,6,7,9).
The reconstructed B, eta, and product have weights 17,16,33. All rows
vanish at the origin. Independent positive dimension-zero and negative
positive-dimensional controls passed before the main basis calls.

Two one-core foreground jobs used the frozen guided_gb policy and
fixed wall timeouts. Their completed outcomes are:

| homogeneous ideal in R_8 modulo p | wall limit | completed outcome |
|---|---:|---|
| J_8=(E2,...,E16) | 1800 seconds | INCONCLUSIVE_TIMEOUT |
| J_8+(b), the b=0 slice | 900 seconds | INCONCLUSIVE_TIMEOUT |

Both stopped inside the standard-basis computation. Neither returned
an accepted basis or a dimension. The wrappers reaped the CAS
processes and returned typed timeout records; their wrapper exit
codes are not mathematical results. No t=8 full or slice assertion,
and no length or nilpotence assertion, is promoted from these runs.
The logs and complete guided result objects are saved in
`controls_t8_guided.log` and `slice_t8_guided.log`, with the emitted
scripts and captured stdout/stderr in their corresponding directories.
No predicted Hilbert series was used as a proof or a basis hint.

For a future successful replay, the exact promotion gate is as
follows. Work over the local domain obtained from Z[d]/(d^2-3) at
the prime (32003,d-31750), inverting the fixed scalar denominators,
y, and the actual high pivots. Their nonzero residues were checked,
so the modular direct recurrence is the reduction of the
characteristic-zero recurrence over this local domain. The rows are
homogeneous in positive weights, and the b=0 slice is homogeneous
as well. An accepted dimension-zero special fibre would have empty
weighted projectivization. The latter is proper over the local
domain: one may take a standard graded Veronese to see properness.
Its closed image could not contain the generic point while omitting
the closed point. Thus empty special projective fibre would imply
empty generic projective fibre and a zero-dimensional homogeneous
characteristic-zero cone. Extension to the algebraic closure covers
both embeddings of this irreducible quadratic field. This argument
would promote dimension zero only, not the measured modular length.

That antecedent did not occur in either completed run. In particular
no inhomogeneous Rabinowitsch ideal was tested modulo p and then
incorrectly promoted by this properness argument.

## 11. Exact residual, remaining t-range, and next mechanism

The uniform theorems in Sections 3–7 hold for every t>=2 on both
factors, with the explicitly stated t>=3 restrictions on the unit
cubic coefficient and monomial uniqueness. The exact full-cone
controls are t=2,3,4. The new maximally coincident-root theorem holds
at t=11,26,47, both factors. None of these partial strata resolves a
new whole index. Consuming the banked range through t=7, the unresolved
whole-index range remains t>=8, except for any explicitly completed
whole-index computation recorded in Section 10.

At an unclosed index the exact missing statement is still

    for every normalized monic C and W satisfying F1–F3,
    B*W'(0)=0,

or equivalently

    1 in (I_(t,+),1-z*b2*(U'(b4)+b3*C(b4))) in S_t[z].

In the new direct coordinates this is

    1 in (E2,...,E_(2t),1-z*B_C,b*eta_C,b) in R_t[z].   (OPEN-F3)

The report proves that any counterexample must lie on an actual
support Sigma with both 2t and 2t+1 in its semigroup. Such a point has
trivial scaling stabilizer. Its ordered-root lift must satisfy the
full synthetic-division contacts (RC8),(RC14), the cubic intersection
bound (RC9), and, on b!=0, the unit and norm conditions (RC3)–(RC6),
retaining the exceptional point (RC13) if J vanishes. At the listed
split indices its C cannot have all roots equal. These are precise
restrictions on the residual, not replacements for it.

For generic t, there is no integral Laurent resonance, but polynomial
truncation on this remaining support locus is unproved. For split
t=3m^2-1, m>=2, both factors remain unclosed globally: on d=-m one
must enforce the x^(6m-2) compatibility row, and on d=+m the formal
resonance lies below the polynomial residual range. The maximally
coincident slices at m=2,3,4 are closed separately. No assertion is
made that the ordered-root cover is reduced, or that excluding its
distinct-root open subset would exclude its whole source.

The next concrete mechanism is to combine the *prescribed*
differential factor H with the finite free root-algebra contacts and
the infinity recurrence. One must prove that these linked equations
cannot simultaneously give a polynomial W on the semigroup-admissible support
locus with B eta!=0. The cubic intersection bound isolates at most
three units of intersection length with C; it does not presently
control the remaining differential contacts. A successful proof needs
that missing global condition, not merely the existence or number of
factors of R. The two-row resultant of Section 9 gives a smaller
explicit next problem on the maximally coincident locus, with repeated
roots fully retained.

Typed status: **OPEN[K16-8.1-RADICAL]**, all-t **OPEN[PS-F3]**. No
all-t promotion to theorem (T) and no milestone notification is due.
The complete conditional dependency chain to such a promotion is (DEP2).

## 12. Fallacy audit, reproduction, and completion

- The homogeneous tau and inhomogeneous T_(t,0)=yg+tau are separated.
  Both t=2 factors pass direct coefficient and explicit family checks.
  The exceptional fibre disproves V0, not product vanishing or (8.1).
- Every ring, generator order, coefficient field, and scalar division
  is declared. The high reconstruction is polynomial and preserves
  nonreduced fibres. The ordered-root extension is finite free and
  faithfully flat; no discriminant or Vandermonde is inverted.
- Radical membership is not replaced by ideal membership: exact
  t=3,4 have nonzero product classes but square zero. No finite
  nilpotence exponent or degree-only Hilbert bound is extrapolated.
- The norm, contact, and factor identities retain their hypotheses.
  At b=0 the K-unit assertion is not used. The C contact includes
  b=0, repeated roots, and discriminant-zero strata. Any rational
  division by J retains (RC13).
- A nonzero modular homogeneous dimension computation can only be
  promoted through the explicit properness model in Section 10.
  No modular inhomogeneous unit ideal, measured length, or predicted
  Hilbert series is promoted to characteristic zero.
- Formal Laurent solutions, local formal series, polynomial
  solutions, and actual terminal cone points are distinct objects.
  Formal nonresonance is not a nonexistence theorem. Root contacts
  alone do not replace the prescribed differential factor.
- No unproved EN height, CM dimension, DVR normalization, rank-one
  chart denominator, generic Abel solution count, or degree-blind
  argument enters a promotion. The support exclusion is confined
  to the explicit coordinate strata where its homogeneous monomial
  proof applies; it does not decide the full residual ideal.
- No new exit-price or exit-set assertion is made, so no
  charge_basis declaration is due.

Representative exact foreground reproductions, using this lane's
durable drivers, are:

    timeout 120 stdbuf -oL python3 box/k16f3abel-20260905/infinity_structure.py
    timeout 60 stdbuf -oL python3 box/k16f3abel-20260905/rootcover_identities.py
    timeout 60 stdbuf -oL python3 box/k16f3abel-20260905/controls_t2_certificate.py
    timeout 120 stdbuf -oL python3 box/k16f3abel-20260905/rigidity_coincident_allb.py 2
    timeout 120 stdbuf -oL python3 box/k16f3abel-20260905/rigidity_coincident_allb.py -2

The direct full-cone scripts `controls_t2_d-1.sing`,
`controls_t2_d1.sing`, `controls_t3.sing`, and `controls_t4.sing` run
with `timeout 1800 stdbuf -oL Singular -q SCRIPT`. They can be
regenerated by `controls_emit_direct.py`; regeneration writes this
lane's own row and basis files, so a replay should choose a fresh
`--root` directory. Drivers for the finite split slices accept other
integer d but make no result claim until their exact checks finish.

Independent same-lane review audited the scalar pivots, semigroup
criterion, the all-b normalization in (C3), the t=2 correction, and
the t=11 integer certificates. It caught and corrected the distinction
between the actual support semigroup and the enlarged binomial
semigroup. A second exact symbolic check independently verified (C3).
The final inventory and accepted outcomes are in `run_outcomes.json`
and `artifacts.sha256` under the driver directory.

All lane-owned CAS jobs have finished and been reaped. The two t=8 timeouts are recorded as inconclusive; all accepted exact controls and universal identity checks completed. Final mathematical review found no load-bearing gap in the stated partial results after the recorded notation corrections. The report was completed within the 180-minute budget and is sealed only after the artifact and process audit. Final verdict: PARTIAL; the all-t theorem remains OPEN.
