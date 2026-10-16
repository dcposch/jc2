# Finiteness does not repair the polynomial-moment shortcut

ROOT, 2026-10-16. MANUAL / UNREVIEWED at production; subsequent review must
be read separately. One fixed countercontrol, not a Keller map or JC2 result.

The marked smooth affine surface below contains a whole affine plane with
complement one affine line. Its distinguished two-form has that line as its
simple zero divisor. A finite degree-six map to the plane has ALL polynomial
moments zero for this form, but is not etale on the affine-plane open.
Thus adding finiteness does not make these moment identities a sufficient
Keller obstruction. The actual Jacobian condition is not assumed or recovered.

## 1. Surface and finite algebra: no generation theorem imported

Glue X=Spec C[U,V] to Z=Spec C[g,p] by

    V=1/g,  U=g^2+g^3 p,
    p=UV^3-V.

The overlap is V!=0, equivalently g!=0. Denote this surface by Y and its
complement Y\X by D={g=0} in Z. In particular D is A1_p, not a complete curve.

Define an affine ring independently by

    B=C[a,b,c,p]/(b^2-ac, b(c-1)-ap, c(c-1)-bp).

There are compatible chart maps to Spec B:

    X: a=U, b=UV, c=UV^2, p=UV^3-V;
    Z: a=g^2(1+gp), b=g(1+gp), c=1+gp, p=p.

We check these maps identify Y with Spec B, rather than assuming the displayed
functions generate its global ring. The opens D(c),D(c-1) cover Spec B.
On D(c), put g=b/c. The relations give gp=c-1 and a=g^2 c, so

    B_c = C[g,p,(1+gp)^-1].

Conversely those formulas satisfy all three relations, establishing the equality
as an isomorphism, including scheme structure. On D(c-1), put V=p/(c-1).
The second and third relations give b=aV and c=bV=aV^2, hence

    B_(c-1) = C[a,V,(aV^2-1)^-1].

These too are mutually inverse substitutions. On the intersection gV=1 and
a=g^2+g^3p. These open pieces cover Y: an X-point with UV^2=1 has V!=0
and lies in the Z-piece D(c); a Z-point with 1+gp=0 has g!=0 and lies in
the X-piece D(c-1). This proves the asserted affine presentation. In particular
B is a domain, since it is the ring of the glued integral surface Y.

The relations imply

    c(c-1)^2=ap^2,   b^2=ac.

Thus c is integral over C[a,p], and b is integral over C[a,p,c]. The whole
ring B is finite over C[a,p]. Since p is integral over C[a,p^2], B is also
finite over C[a,p^2]. Therefore

    f:Y -> A2,  f=(p^2,U)

is finite. The base variables a,p are algebraically independent: in the function
field C(a,V), p=aV^3-V is transcendental over C(a). The polynomial
aV^3-V-p is irreducible over C(a,p): over C(a)[V,p] it is a primitive linear
polynomial in p with quotient C(a)[V], and Gauss's lemma applies in V.
Consequently [C(Y):C(a,p)]=3 and [C(a,p):C(a,p^2)]=2; f has degree six.
Its proof of finiteness did not require any hypothesis on a Keller pair.

## 2. Exact polynomial-moment criterion on this surface

The form omega=dU wedge dV on X extends to

    omega=g dg wedge dp

on Z, with divisor D of multiplicity one. For R in B, regard R as a polynomial
in U,V on X, set H(U,V)=integral_0^U R(s,V) ds, and define

    L(R)=[g^1] H(g^2,g^-1).

All integrals here mean polynomial antiderivatives over C; no limiting integral
or numerical sample is used. The same formula defines a linear functional on
C[U,V], even though only its restriction to B describes global forms.

Claim: R omega has a global regular one-form primitive on Y iff L(R)=0.
Indeed alpha=H dV is a primitive on X. On Z let H_Z=H(g^2+g^3p,g^-1).
Since partial_p H_Z=g^3 R_Z and R_Z is polynomial, H_Z-H(g^2,g^-1) belongs
to g^3 C[g,p]. Hence

    alpha=-g^-2 H(g^2,g^-1) dg + a regular one-form on Z.

All polar terms are independent of p. The only logarithmic residue is -L(R).
If it vanishes, integrate the remaining negative powers to K(g), a polynomial
in g^-1=V, and subtract dK from alpha. This is regular on both charts and
still has differential R omega.

Conversely, if beta is a global primitive, alpha-beta on X is a closed
polynomial one-form, hence dF for a polynomial F(U,V) by elementary polynomial
integration. Restrict the transformed equality to p=0. The pullback of beta
is regular in g, and d(F(g^2,g^-1)) has zero Laurent residue. Thus L(R)=0.

For nonnegative integers r,s the extended functional has the simple formula

    L(U^r V^s) = 1/(r+1) if s=2r+1, and 0 otherwise.

For example p is global and L(p)=L(UV^3-V)=1/2-1=-1/2, so L|B is nonzero.
This is a proper kernel containing1, not a Mathieu subspace assertion.

## 3. ALL moments of the finite map vanish, while its Jacobian does not

For i,j>=0, expand the finite binomial

    U^j p^(2i) = sum_(k=0)^(2i) binom(2i,k)(-1)^(2i-k)
                            U^(j+k) V^(2i+2k).

A nonzero L-value would require 2i+2k=2(j+k)+1, impossible by parity.
Therefore L((p^2)^i U^j)=0 for EVERY i,j>=0, including i=j=0.
Equivalently, each such multiple of omega has a global regular primitive.
This is a uniform calculation, not inference from finitely many checked moments.

On X the actual Jacobian is

    J_(U,V)(p^2,U)=-2p(3UV^2-1).

It is nonzero but nonconstant and vanishes in X, for example on V=0 where p=0.
On Z, d(p^2) wedge dU=-2pg(2+3pg) dg wedge dp. Besides the simple D factor,
there is additional ramification; this is explicitly NOT the stipulated
Keller/simple-boundary-only situation. No counterexample to JC2 is constructed.

## 4. Relation to prior evidence and stop

The September7 [higher-moment report](d125-higher-moment-discriminator-astra-20260907.md)
already gives algebraically independent all-moment controls on a DIFFERENT,
index4 marked surface and explains why complete Jacobian equations imply the
moments. It does not establish their finiteness. The present fixed index3
control tests that additional hypothesis directly, without importing the older
surface classification or its marked-coordinate claims.

This does not test the complete guarded F10 equations, their prescribed degree
faces, or any actual Keller map. It only refutes the broad inference from a
finite map plus vanishing moments on the marked carrier. A useful successor
would need a genuinely new consequence of the constant-Jacobian condition;
none is supplied here. Stop this sufficiency test; no family or degree farm.
All arguments above are elementary manual chart, algebra and residue checks.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6260`.
- Body SHA-256:
  `8f896a09a356ea80a2f74a0225df4bd53daa3708898fb1a09ff8c9f04090a404`.
- Frozen basis: `4f06b4425ca61f1827c4daf4d66fcfb198732425`.
