# Exact certificate transport to the two X pieces

This note concerns a fixed t and the declared characteristic-zero field
k. It supplies a polynomial unit certificate for each X piece from a
verified source identity

    (B*eta)^2 = sum_{k=2}^{2t} a_k E_k.                 (1)

The coefficients a_k are the entries LL[k-1,1] of a matrix over
k[c1,...,c_(t-1),b]. `transport_certificates.py` loads the fresh literal
F3 residuals, the emitted chart coefficient data, and the lift matrix.
It rechecks (1) by exact polynomial arithmetic, independently of the
command that produced the lift. Its mathematical argument uses no
modular specialization, no properness claim, and no finiteness claim
about the original cone.

Write

    d_k=deg_b(E_k), e_k=deg_b(a_k),
    m=max(4,max_k(d_k+e_k)), r=max(m-4,4).

For a polynomial f of b degree at most e, define the finite arithmetic
circuit

    C_e(f)=sum_{j=0}^e [b^j]f * A^j * Delta^(e-j).

This is the polynomial Delta^e f(c,A/Delta); its sum expression makes
sense even at Delta=0. Zero rows and zero coefficients use degree zero.
The main rows are F_k=C_(d_k)(E_k). Put

    Q_k=Delta^(m-e_k-d_k)*C_(e_k)(a_k).

All exponents are nonnegative by the definition of m. Homogenizing (1)
in b to degree m, with formal numerator Y and denominator Z, gives an
identity in the polynomial ring k[c,Y,Z]. Substituting Y=A, Z=Delta
is a ring homomorphism, and the checked affine coefficient identities

    M*Delta+N*A=H,
    rho*Delta+sigma*A=H

show that the left side becomes Delta^(m-4)*H^4. Therefore

    sum Q_k F_k = Delta^(m-4)*H^4.                    (2)

Equation (2) is a literal polynomial identity. The arithmetic circuits
are explicit finite formulas for its coefficients; leaving powers
unexpanded does not weaken the identity to a localization assertion.
The verifier checks all source b coefficients and the degree bounds.
With `--expand-main` it additionally expands (2) after substituting the
actual coefficient polynomials and compares the two sides exactly.

In the main polynomial ring k[c,u], set

    W=u^r*Delta^(r-m+4)*H^(r-4),
    G=sum_{j=0}^{r-1}(u*Delta*H)^j.

Again all exponents are nonnegative. Multiplying (2) by W and adding
the geometric-series identity gives the exact unit certificate

    1=sum_k (W*Q_k)*F_k + G*(1-u*Delta*H).             (3)

The verifier checks this last arithmetic identity in a universal
polynomial ring over Q with independent symbols for u, Delta and H.
This avoids expanding large inverse factors while verifying precisely
the finite circuit used in (3).

For the boundary ring k[c,b,s], the checked slice equation is
B-eta=b*Delta-A. Thus

    B^4=(B*eta)^2-B^2*(eta+B)*(A-b*Delta).

Using (1) and multiplying by s^4 gives a second literal unit certificate:

    1=sum_k s^4*a_k*E_k
      -s^4*B^2*(eta+B)*A
      +s^4*B^2*(eta+B)*b*Delta
      +(1+s*B+(s*B)^2+(s*B)^3)*(1-s*B).               (4)

The actual coefficient-ring difference-of-squares identity and the
universal geometric-series identity are both expanded and checked.
The coefficients in (4) may involve eta although eta is not an extra
variable: it is exactly the saved reconstructed polynomial in c,b.

The t=3 replay passed every check, including expansion of (2) with the
actual number-field coefficient polynomials. Its degree vectors are

    (d_2,...,d_6)=(3,2,2,2,2),
    (e_2,...,e_6)=(3,3,4,4,4), m=6, r=4.

Consequently its cleared source identity is sum Q_k F_k=Delta^2 H^4,
and W=u^4 Delta^2. Its artifacts are `t3_transport.sing`,
`t3_transport.log`, and `t3_transport_circuit.json`. The JSON records
the exact field, generator order, input hashes, row degrees, circuit
formulas, verifier script hash and log hash. The successful final
marker is `TRANSPORT_ALL_EXACT_ASSERTIONS_PASS`.

The t=4 replay also passed every circuit check. Its exact source
cofactors were obtained by the separate targeted linear solve,
independently replayed in Singular, and then rechecked by this transport
driver. Its degree vectors are

    (d_2,...,d_8)=(3,3,2,2,2,2,2),
    (e_2,...,e_8)=(0,0,4,4,4,4,4), m=6, r=4.

The first two cofactors are zero. As at t=3, its cleared identity has
right side Delta^2*H^4, with multiplier W=u^4*Delta^2. The t=4
verification retains coefficients as circuits rather than expanding
their large products. Both t=3 and t=4 additionally recompute every
F_k and compare with the literal saved main-chart generators. The
map is explicitly c_i->c_i,d->d,b->0 after asserting b independence.

The same driver accepts t=5 when its source lift matrix exists.
Merely generating a circuit without successfully checking its
source identity is not recorded as a proof. Its manifest explicitly
distinguishes `GENERATED_NOT_YET_REPLAYED`, `FAILED`, `TIMEOUT`, and
`ALL_EXACT_ASSERTIONS_PASS`.

## General homogeneous power and a bounded inverse multiplier

Suppose, at one fixed t, that (B*eta)^n belongs to J. Because J is
positively homogeneous, projecting any membership identity to total
weight D=n(4t+1) gives homogeneous cofactors a_k of weights D-w_k,
where w_k=4t+2-k. Any coefficient with a negative required weight is
zero. Their b degrees and those of E_k obey

    e_k+d_k <= floor((D-w_k)/(t+1))+floor(w_k/(t+1))
               <= floor(D/(t+1)) < 4n.

Thus m=max(2n,max(e_k+d_k)) satisfies 2n<=m<=4n-1. Homogenization
gives sum Q_k F_k=Delta^(m-2n)*H^(2n), and the multiplier can always
be chosen as

    W=u^(2n)*Delta^(4n-m).

No H factor is needed in W. The inverse coefficient is the finite
geometric sum from j=0 through 2n-1. This proves a uniform *transport
bound*, conditional on the existence of the homogeneous source
membership identity. It proves neither existence of that identity nor
a bound on n as t varies.

For a corresponding general boundary formula let

    L=B^n*sum_{j=0}^{n-1}B^(n-1-j)*eta^j.

Then B^(2n)=(B*eta)^n-L*(A-b*Delta), and

    1=sum_k s^(2n)*a_k*E_k-s^(2n)*L*A
      +s^(2n)*L*b*Delta
      +(sum_{j=0}^{2n-1}(s*B)^j)*(1-s*B).

For n=2 the verifier now checks the homogeneous cofactor weights
directly and asserts m<=7, r=4. This is an audit of the actual saved
cofactors, in addition to the general homogeneous-projection argument.
