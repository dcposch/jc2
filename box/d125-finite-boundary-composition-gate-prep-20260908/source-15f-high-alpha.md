# D125 pure center: high-alpha Newton-initial obstruction

2026-09-07. **PROVISIONAL theorem: no genuine finite pure-center source arc
in the accepted14v first-contact setup has ord(alpha)>=j, including
alpha identically zero.** This is independent of the pending low-alpha
critical-remainder theorem: that report, its conclusion, and its gate are
NOT premises. The accepted parents are14c/f/g/v; accepted14y and15b were
read as history. No global degeneration-existence or guarded-emptiness
conclusion is made. The new theorem requires independent review.

The argument uses a finite, weight-preserving R_s expansion, regular Newton
initials on the affine cubic, and a direct formal degree3/5 coefficient
lemma. Root independently supplied matching exposure checks and the pole
and coefficient-elimination advisories. No common-generator theorem on a
new coefficient ring, genus argument, or square-class census is imported.

## 1. Exact incoming source and monomial-normal division

Work over K[[s]], characteristic zero, with k=kappa*s^m+..., kappa nonzero.
Use the actual14v references at the pure exceptional center:

    V=g^3+p^3-3p, R=p^2V, S=p^3+gp^2-p,
    R_s=R+h(s)S, h(0)=0,
    F=A-R_s^3-alpha R_s, ord(F)=j<m, F_j=RC,
    ord(G)>=2j, ord(delta)>=j+1.

C modulo V is regular, even, nonconstant; C(0)=0 and V does not divide C.
Every F coefficient has total degree<=13 and weight<=3 for w(g)=5,w(p)=-7.
G has total degree<=23 and weight<=5: this follows directly from its exact
definition in14v, using deg(R_s)=5, w(R_s)=1 and the source A/B bounds.
All coefficients have the actual odd parity. The saturated low rows remain
part of the incoming source; [p]F=alpha*h has NOT been replaced by zero.
Assume a=ord(alpha)>=j, with a=infinity allowed.

Use ordinary polynomial division by R_s with leading monomial g^3p^2 in
lexicographic order g>p. Its leading coefficient is exactly1. Replacement
of g^3p^2 uses only

    -p^5-h gp^2+(3-h)p^3+h p.

Each replacement strictly lowers g-degree, does not raise total degree,
and does not raise weight. The quotient lowers total degree by5 and weight
by1. Thus repeated division is FINITE, coefficientwise over K[[s]], and
produces normal remainders with no monomial divisible by g^3p^2. In
particular there are exact expansions

    F=P0+R_s P1+R_s^2 P2,
    G=Q0+R_s Q1+...+R_s^4 Q4,                    (1)

with deg(Pi)<=13-5i, w(Pi)<=3-i and ord(Pi)>=j, and analogous bounds
deg(Qi)<=23-5i, w(Qi)<=5-i and ord(Qi)>=2j. These are proofs of finite
representations, not instructions to materialize source coefficients.

The normal remainder spaces of weight<=5 inject into K[g,p]/(V).
Indeed, if V divides a polynomial P of weight<=5, write P=VU.
Then w(U)<=-10 excludes all monomials of p-degree0 or1, so p^2 divides U
and R divides P. But a nonzero multiple of R has leading monomial divisible
by g^3p^2, impossible for a normal remainder. This rederives the needed
filtered fact directly from the accepted14v factorization; it does not use
the pending low-alpha lemma or assume ordinaryness of any quotient.

Let q=ord(P0). Since F_j=RC, q>j (possibly infinity), and the leading
coefficient of P1 modulo V is C modulo V. Define

    eta=min(j/2,q/3), so j/3<eta<=j/2.             (2)

## 2. Why these Newton initials really are regular

Extend constants to Kbar and put L=Kbar(V). The generic derivative
R_g(0)=3p^2g^2 is invertible in L. Formal implicit coordinates give
g=g(s,z) in L[[s,z]], initially g, with R_s(g(s,z),p)=z. Pass to a finite
Puiseux parameter extension so eta is integral in the new normalization,
and substitute z=s^eta Z. The variable Z remains independent.

For each nonzero normal coefficient Pi or Qi, its first s-coefficient has
nonzero residue on V by Section1. Composing with g(s,s^eta Z) therefore
does not change that first coefficient: it is a REGULAR polynomial residue
on V. Every implicit correction has strictly positive s-order. Multiplying
by s^(i*eta)Z^i gives the corresponding initial weight. Distinct i give
distinct powers of Z, so they cannot cancel in the initial polynomial.

This is only an initial-form statement. Later implicit Taylor coefficients
can have affine poles; they are not declared regular. Their positive extra
orders prevent them entering the minimum weight. Differentiating at fixed
Z or fixed p does not lower s-order, apart from the explicit common
s^(-eta) for partial/partial z. This establishes the initial bracket rule
without discarding moving h, nonmultiple orders, or higher remainders.

Consequently A has weight3eta and initial

    P(Z)=Z^3+u Z+v,                              (3)

where u is even and v odd in L, both regular on affine V, and at least one
is nonconstant. If eta=j/2, u=C|V+alpha_j is nonconstant. If eta=q/3<j/2,
u=0 and v is the nonzero odd residue of P0_q, hence nonconstant. Both may
occur at equality. The R_s^2 term starts at j+2eta>3eta, so no Z^2 term
has been omitted. For alpha=0 exactly the same proof uses alpha_j=0.

## 3. Retain all B terms and the exact target order

For the proof only, subtract the scalar series beta(s) times the ENTIRE A
from B. This preserves the bracket and all degree/weight/parity bounds;
no source or production presentation is modified. The exact14v identity
then reads

    B*=R_s^5+(delta-5alpha^2/9)R_s
                    +(5R_s^2/3-5alpha/9)F+G.     (4)

In the normal expansion (1), its R_s^4 coefficient has order>=j, its R_s^3
coefficient order>=j, and its R_s^2 coefficient order>=min(q,2j).
Hence their weights are respectively >5eta, >=5eta and >=5eta. Below
5eta the R_s coefficient can only come from the SCALAR delta, since all
other contributions have order>=2j; the R_s^0 coefficient may be a regular
odd function from Q0. Thus if B* has weight nu<5eta, its nonzero initial is

    Q(Z)=d Z+e,                                  (5)

with d scalar and e odd regular. Its bracket with (3) cannot vanish. If it
did, the Z^2 coefficient gives De=0 for D=d/dp on L; oddness then gives
e=0. Nonzero Q forces d!=0, and the remaining coefficients force
Du=Dv=0, contradicting Section2. The case d=0 is included.

Here D is the nonzero derivation of L with Dp=1; its constants are Kbar.
The exact transformed target is

    [A,B*]_(z,p)=-(5/9)k^3*g(s,z)^2/R_g(s,g(s,z),p),
    R_g=p^2(3g^2+h),

and its first coefficient at order3m is -5*kappa^3/(27p^2), independent
of Z. A nonzero initial bracket for weights3eta and nu occurs at
2eta+nu. If this is below3m, the target requires that bracket to vanish;
if above3m, the target arrives before any possible bracket. At equality
there is also a contradiction, from the following explicit local bound.

At O=(0,0) on V, g is a local parameter, ord_O(p)=3, and

    dp/dg=g^2/(1-p^2), D=(1-p^2)/g^2*d/dg.

Thus D takes a regular local function to a function with pole order at
most2. A coefficientwise bracket of polynomials in Z with regular
coefficients has poles of order at most2. It cannot equal the target
coefficient, which has pole order6. This is a direct local calculation,
not a finiteness or normality assumption about the source map.

It follows that nu<5eta is impossible. The leading R_s^5 term ensures
nu<=5eta, so necessarily nu=5eta. Its initial Q is monic of degree5,
has no Z^4 term, and has the same total odd parity as P. The bracket weight
is now7eta. All comparisons with3m have been retained: if 7eta>3m there
is an immediate order contradiction; equality is excluded by the same pole
bound; if 7eta<3m the initial polynomials must commute. No inequality
3m>7eta was silently assumed.

## 4. A direct degree3/5 commuting lemma

Let P=Z^3+uZ+v and Q=Z^5+cZ^3+dZ^2+eZ+f over the differential field L.
Assume their bracket is zero, P,Q have the preceding odd parity, u is even
and v odd. Write primes for D. Successive coefficient comparisons give

    c=5u/3+c0,
    d=5v/3+d0,
    e=5u^2/9+c0*u+e0,
    f=10uv/9+c0*v+(2/3)d0*u+f0,

with scalar constants c0,d0,e0,f0. These constants are NOT all set to zero:
d and v are odd, so the scalar d0 must be zero; similarly f0=0 by parity.
c0 and e0 remain unrestricted. Equivalently, without parity one may shift
v by3d0/5 in the calculation below; the actual parity makes that unnecessary.

The two remaining coefficient equations, with K=9e0/5, are

    (u^2-K)u'-6v v'=0,
    2uv u'+(u^2-K)v'=0.                           (6)

The first integrates to u^3/3-Ku-3v^2=L0, a scalar. If u' is nonzero,
the determinant of (6) vanishes. Substituting that first integral gives

    (7/3)u^4-6K u^2-4L0 u+K^2=0.                 (7)

This nonzero scalar polynomial forces u algebraic over Kbar, hence scalar,
a contradiction. Therefore u'=0, and the first equation of (6) gives
v'=0 as well (including v=0). Thus u and v are both scalar. This
contradicts (3). The lemma is proved by these explicit identities, not by
transferring a polynomial-common-generator theorem to L[Z].

Every target-order case in Section3 is now impossible. Hence there is no
genuine source arc with a>=j, including a=infinity, as claimed.

## 5. Evidence, independence, and exact stop

Twelve capped normal/-O runs pass with byte-identical rational-string
witnesses and zero Assert nodes. The checker verifies actual degree<=5
monomial division and reconstruction/weight bounds, the cubic derivatives
and target factor, and the universal formal3/5 coefficient, first-integral
and determinant identities. Actual mutations remove h*p from the divisor,
feed gpV to the filtered input, change the target factor, change the
constant coefficient of Q, or change the quartic coefficient. The same
equality/input verifiers reject them. The finite valuation controls are
illustrations; the universal inequalities are proved above. Witness SHA256
`85b3e0ea5469e2867296af390bd3d4fd03bd7619e1ae22b0f88a08c7ee938c25`.

No actual A15/B25, R^3/R^5 or full source row stream was expanded. Only
small actual generators and independent formal polynomials were used.
There was no AWS/SSH/CAS, new lane, solver, source edit, live peer read or
canonical edit. The pending low-alpha report is not charged as an input;
this proof rederives its own division and valuation statements from the
accepted parents. No separate counterexample to JC2, guarded properness,
source coverage, or finite degeneration from every guarded point follows.
This report's high-alpha theorem is PRODUCER-CHECKED, not promoted.

The transaction is verified; custody pins inputs and owned artifacts, and
all writers are idle before handoff. No descendant is launched. STOP/IDLE.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10533`.
- Body SHA-256:
  `610ddcb4c4f26d16d5ae9ac8ab038b503482a47bd07ce46533c20c8c487fc034`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
