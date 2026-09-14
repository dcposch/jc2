# Independent source bridge: explicit remainders and the final minor face

The direct source chart uses the polynomial identity

    h2=h3^3+C2*h3+C3,
    degree_y(C2),degree_y(C3)<degree_y(h3)=11.

The canonical approximate-root depression excludes h3^2 by definition.
The prescribed homogeneous top of h2 equals the cube of the top of h3.
If a degree22 homogeneous part of C2 existed, multiplying it by the monic
in y degree11 top of h3 would have y-degree at least11 and could not cancel
against the homogeneous C3 part, whose y-degree is at most10. Thus C2 has
total degree at most21; likewise C3 has total degree at most32. These are
polynomial-division consequences of the top identity, not inferred support
caps. Normalizing as U=t^22*C2 and V=t^33*C3 gives supports

    U: r>=1, q<=10, r+q<=22,
    V: r>=1, q<=10, r+q<=33.

Moh p.149 Thm.1.2 at the complete coherent D2 system gives
ord_t C2>=-2/3 and ord_t C3>=-1. With the derived substitution
(t,z)=(s^3,pi*s^4), these become normalized weights64 and96.
Each raw coefficient below its floor gives an actual scalar zero equation.
Enumeration is:

| Block | Raw coefficients | Strictly-below equations | Equality | Above |
|---|---:|---:|---:|---:|
| U=t^22*C2 |187|154|4|29|
| V=t^33*C3 |308|271|4|33|

The equality U powers are pi^10,pi^7,pi^4,pi; the equality V powers are
pi^9,pi^6,pi^3,1. Their exponents are obtained by solving3r+4q=64 or96
inside the above full triangles. They are not a guessed list of terms.

The h3 equality face H has two raw lower coordinates in addition to pi^8.
Comparing the K2 face identity

    (pi^3-beta)^8 = H^3 + U_face*H + V_face

above max(deg(U_face*H),deg(V_face))=18 forces the coefficient of pi^5
in H to -8beta/3. The coefficient of pi^2 remains free. After that forced
row, the remaining face comparison consists of seven independent rational
leader rows, at pi powers18,15,12,9,6,3,0. Three solve U coefficients,
one chooses a rational pivot between U_1 and V_9, and three solve the
remaining V coefficients. There is no division by the second h3 equality
coordinate. This leaves70-7=63 C2/C3 coordinates at the D2 face stage.
The seven D1 h2 rows then leave56 such directions relative to the h3 base.
With the independently derived minor maps this predicts inner dimensions
64 for delta2 with all centres and62 for delta5/2. The parent should compare
these counts with its direct implementation, rather than import them as an
asserted rank.

By contrast, the gate diagnostic's106 independent low-q K2 output
coordinates before D1 are not a replacement for these63 source-remainder
directions once the correct C2/C3 floors are enforced. Generic inversion of
the diagnostic K2 output produces below-floor remainder coefficients.
The source model must retain those inverse-map constraints or construct the
remainders explicitly from the start. The direct formula above is the clean
option. It is a safe polynomial chart: every actual source object gives these
coordinates, and no Jacobian branch is removed by an arbitrary cap.

## Final minor endpoint equality, including at-level residue transfer

At the minor radii delta=2 and5/2, the root-factor valuations of g are
A=-18 and A=-9/2 respectively. Pair the27-root minor disc with the entire
72-root major packet at radius

    r_major=(A+27)/72 = 1/8 or5/16.

Both values lie strictly between the initial radius-1 and D2 radius1/3.
All72 major roots therefore lie in that disc. The two discs are disjoint,
cover all99 roots, and have the same generic g-order A: they form a coherent
complete system in the sense of Moh p.148, lines445-461. Their root counts
27 and72 are divisible by9, allowing Thm.1.1 twice.

There is a necessary further step: transferring only these two total counts
does not yet identify the minor leading polynomial. Refine the minor
points past their at-level first separation, to a slightly higher common
negative g-accuracy A' with A<A'<-3. Choose A' sufficiently close to A to
avoid any next separation. Different residue rays can have different
radii at that common accuracy. Prop.6.1(2), p.191, applies to every refined
minor point because its g-order remains negative and it lies in the same
principal minor packet. Def.3.1(4), p.161, makes it a distribution detector
for g,T1,T2 of degrees99,66,55, whose reduced ratio is9:6:5. Therefore each
refined g-multiplicity is divisible by9.

The major complementary disc now has radius(A'+27)/72<1/3 and still contains
all72 major roots. Together these discs again form a coherent complete
system with all multiplicities divisible by9. Thm.1.1, printed p.149,
applied successively to the canonical cube roots g->h2->h3 transfers the
refined multiplicities in two factors of3. By Prop.1.2, the at-level minor
residue roots of h3 have exactly the g-multiplicities divided by9.
The same distribution detector relation transfers the roots to G in ratio6.

The leading coefficient is fixed by monicity: roots in the other leading
packet contribute leading factor-1, raised to the even counts72 for F,
48 for G, and8 for h3. Thus if P is the monic degree3 h3 minor face obtained
as the split-root product, the endpoint faces are exactly

    F_face=P^9,   G_face=P^6.

Their normalized local powers are respectively81 and54 in t for delta2,
and189 and126 in s with t=s^2 for delta5/2. Strict lower powers vanish;
at equality one subtracts the derived product face. Neither "valuation
at least the floor" nor a total-multiplicity claim alone licenses setting
an equality face. This derivation was independently hostile-checked by the
print audit worker, whose refinement observation is incorporated above.
