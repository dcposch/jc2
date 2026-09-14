# Exact de Rham moments on the quartic-tower surface

Status: uniform necessary relations, with the first nonconstant moments
computed exactly. They do not close the K16 atom. The first relation and
a useful specialization of the P-moment are already consequences of the
banked spine; no independent promotion is claimed.

## 1. The surface and its second de Rham class

Work over an algebraically closed characteristic-zero field K. Let X be
the surface obtained by gluing

    U0=Spec K[z,pi],  Uinf=Spec K[h,x]

over pi!=0 and x!=0 by

    x=pi^(-1),
    z=(h-b4)x^3-b1-b2x-b3x^2.                         (M1)

This is an affine-line torsor over P^1 under O(-3): its linear transition
is h=pi^3 z plus the specified translation. In particular it is a
separated smooth surface. Affineness of the whole surface is not needed
in what follows and is not inferred merely from the two affine charts.

The two charts have zero positive-degree algebraic de Rham cohomology.
Their intersection is A^1 times G_m, with first de Rham group generated
by dx/x. The Mayer–Vietoris sequence for algebraic de Rham
hypercohomology therefore identifies

    H^2_dR(X) = K,

via the residue of the difference of polynomial local primitives on the
overlap. This can also be understood from homotopy invariance for the
affine-line torsor over P^1.

The tower pair Q,P is polynomial on both charts and hence consists of
global regular functions on X. On the cone its two-form is

    dQ wedge dP = J(h,x) dh wedge dx,
    J=tau+c b1 x+c b2 x^2+c b3 x^3-c(h-b4)x^4,
    c=-yg.                                          (M2)

Equivalently on U0 this is

    (c z-tau pi) dz wedge dpi.

For every a,b>=0, the form

    omega_ab=Q^a P^b dQ wedge dP

is globally exact, with primitive

    Q^(a+1)P^b dP/(a+1).

Thus every one of its residue classes must vanish.

## 2. A coefficient formula for every moment

Set L=h-b4 and expand all coefficient polynomials in L. Write

    Q=U(L)+(L^2 C(L)-yb3)x+yLx^2,
    P=V(L)+A(L)x+B(L)x^2+gLx^3,

where in this note V=P0, A=P1, B=P2. These are translated coefficient
arrays, not the determinantal split-tail B_r,C_r.

Define the polynomial local primitive

    beta_ab(L,x)=integral from 0 to L of Q^a P^b J dL.

In the original chart a polynomial primitive can be obtained by
integrating with respect to z from z=0. This lower integration limit
corresponds under (M1) to

    L0(x)=b1 x^(-3)+b2 x^(-2)+b3 x^(-1).

Consequently the difference of the two local primitives is, up to the
irrelevant global sign convention, beta_ab(L0(x),x) dx. The uniform
moment equations are precisely

    M_ab:=Res_{x=0} beta_ab(L0(x),x) dx=0.             (M3)

There is no quotient-ring normal-form step here: this is ordinary
coefficient extraction from a Laurent polynomial over K.

For an explicit finite formula, put r=1/x and

    H(r)=b3 r+b2 r^2+b1 r^3.

If

    Q^a P^b J = sum_{m,j>=0} d_mj L^m x^j,

then

    M_ab=sum_{0<=m<=j} d_mj/(m+1) [r^(j+1)]H(r)^(m+1). (M4)

Since deg_x(Q^aP^bJ)<=2a+3b+4, only translated L-jets of order at most
2a+3b+4 enter this formula, regardless of t. This is an exact bounded
jet formula for each selected moment, not a claim that a fixed number
of moments decides the infinite ray.

One may package the whole family as the coefficientwise formal identity

    Res_{x=0} [integral_0^L J/((1-uQ)(1-vP)) dL]
                       at L=L0(x) dx = 0

in K[[u,v]]. It is only a generating function for (M3), with all
coefficients interpreted by the finite rule (M4).

## 3. First exact moments

Use U_i=[L^i]U and C_i=[L^i]C. The driver
`moment_residues.py` gives

    M_00=c b1 b2+tau b3.                              (M5)

After subtracting the constant multiple U_0 M_00, the Q-moment is

    M_10-U_0 M_00 = c/60 * (
        20 C_0 b1 b3^3 + 30 C_0 b2^2 b3^2
      + 15 C_1 b2 b3^4 + 2 C_2 b3^6
      + 30 U_1 b1 b3^2 + 30 U_1 b2^2 b3
      + 20 U_2 b2 b3^3 + 3 U_3 b3^5
      + 30 b1 b2^2 y).                                (M6)

The P- and Q^2-moments are printed without truncation in
`moment_residues.log`. The driver integrates generic arrays symbolically;
the finite-jet selection is performed before every coefficient is
assembled. It ran in the foreground under `timeout 1800 stdbuf -oL`,
finished in approximately six seconds, and exited zero.

The structural agent independently found on the cone

    R_0=U'(b4)+b3 C(b4),
    b1=-b3 R_0/y,  tau=-g b2 R_0.

These imply (M5) exactly since c=-yg. Thus the first cohomological
constraint is already present in the boundary factorization.

There is a second useful consistency check. If b3=b1=0, set
A_0=-g b2, B_0=0, A_1=S_0 as supplied by the tower. The centered
P-moment reduces to

    b2^2(-3g tau+c S_0 b2)/6.

But D2 gives y S_0=3g U_1, while D0 gives tau=-g b2 U_1. Hence this
specialization also vanishes identically by the spine. It is not an
additional obstruction.

## 4. The remaining obstruction in this language

Under tau!=0, U' and V' generate the unit ideal in K[h]. The moments
arising by pullback from the target, however, have coefficients in the
smaller algebra K[U,V], not arbitrary K[h]. One cannot use a Bezout
identity in K[h] as if its coefficients were polynomials in Q,P.

The mismatch is concrete: the boundary collision scheme in
`moh-linear-jacobian.md` has length 6t^2 and is entirely off diagonal
under tau!=0. Functions in K[U,V] identify the values at every such
collision, while general elements of K[h] do not. An extension of the
moment argument must therefore control this conductor/collision
obstruction or derive a genuinely new relation from the full marked
surface. Neither (M5), the checked specialization, nor the existence of
the formal moment family removes it by itself.

No job remains running.
