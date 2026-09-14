# Unrestricted two-chart test: no closing discriminator

Owner /root/contact_collision_geometry. Actual first action2026-09-11 13:20:57UTC; original reserve13:38/HARD13:42UTC unchanged. Sole input ROOT TASK SHAae88357e459ab1441f24e8542827fd17c17e4986f1694f78eef2c17e37168c67 was read FRESH_WHOLE after its hash. Report/manifest/PINS/custody were absent; the existing ROOT TASK is preserved.

MANUAL CO-RESEARCH / UNREVIEWED. The target is unrestricted regular H,G on T, not the invariant quotient ring. No symmetry, degree cap or sparse ansatz is imposed on that target. The known 2009 provenance is imported only as ROOT's TASK attribution, not a new literature claim.

## Result and exact negative scope

NO_NEW_DISCRIMINATOR for the FULL identity dH wedge dG=c*omega. No regular scalar pair or all-degree obstruction is obtained. The concrete output is an all-order countercontrol to replacing the full identity by any fixed finite normal-jet test at BOTH chart boundaries. The control is globally polynomial on T, its bracket is exactly1 modulo arbitrarily high powers of x, and the pair agrees with the standard Darboux coordinates to that order on each chart. Nevertheless it has critical points away from both boundaries, and its first coordinate x has no exact global mate.

This is the known formal-versus-global barrier in an explicit two-chart polynomial family, not a new route or theorem promotion. The fixed H=x appears ONLY as a countercontrol to the finite-jet test, not as a restriction on the unrestricted question.

## 1. An exact family, uniform in the requested normal order

Use the accepted relation t²-1=x²Z and omega=dx wedge dt/x². Hence {x,f(t)}=x² f'(t) on the dense x!=0 chart. For each integer r>=1 define the nonzero rational number

    I_r = integral_0^1 (s²-1)^r ds
        = sum_(j=0)^r (-1)^(r-j)*binomial(r,j)/(2j+1),
    c_r = -1/I_r,
    g_r(t) = t+c_r*integral_0^t (s²-1)^r ds.

These are ordinary polynomial antiderivatives with rational coefficients, not analytic functions required on T. I_r is nonzero because the integrand has the constant sign (-1)^r on the real interval(0,1); equivalently its explicit rational sum is nonzero. Thus every c_r is a nonzero scalar in C. No computation or coefficient artifact is being supplied.

The polynomial g_r is odd and satisfies g_r(1)=0, hence also g_r(-1)=0. Write g_r(t)=(t²-1)q_r(t), with q_r a polynomial of degree2r-1. Then

    H_r=x,                 G_r=Z*q_r(t) in O(T).

In the rational chart G_r=g_r(t)/x², so direct differentiation gives the GLOBAL polynomial identity

    {H_r,G_r}=g_r'(t)
              =1+c_r(t²-1)^r
              =1+c_r*x^(2r)*Z^r.                         (*)

The dense-chart calculation extends to all of the integral surface T because both sides are regular. For every prescribed integer M>=1, choosing2r>=M gives {H_r,G_r}=1 modulo(x^M) on the ENTIRE double boundary, not merely at finitely many points or on one component.

For a direct low-order check, I_1=-2/3 and c_1=3/2. Thus g_1=(t³-t)/2, G_1=tZ/2, and {x,G_1}=1+(3/2)x²Z. This example is only a check of the general identity, not a degree scan.

## 2. Both chart maps match the desired finite jets

Since g_r'(t)-1=c_r(t²-1)^r and g_r(1)=0,

    g_r(t)-(t-1) is divisible by (t-1)^(r+1).

Likewise g_r(t)-(t+1) is divisible by (t+1)^(r+1). On the first chart t-1=x²y and on the second t+1=x²v. Dividing these two identities by x² gives POLYNOMIAL identities

    G_r(x,1+x²y,2y+x²y²) = y+x^(2r)*A_r(x,y),
    G_r(x,-1+x²v,-2v+x²v²) = v+x^(2r)*B_r(x,v),

for polynomials A_r,B_r. Thus the globally regular pair (x,G_r) agrees with (x,y) and (x,v), respectively, to every requested fixed normal order by taking r sufficiently large. It satisfies the exact transition, not an approximate gluing: G_r itself belongs to O(T).

For s>=r, the differences G_s-G_r vanish modulo x^(2r) on both charts and hence globally, since the two charts cover T and divisibility by the global principal ideal is local. Therefore the family also defines a compatible element of the x-adic completion, with bracket exactly1 there. No regular function on T is inferred from that completion element.

The degree and support of G_r grow with r. Neither all finite normal-jet tests nor their compatible formal limit supplies a fixed polynomial degree bound or a regular global pair. This is precisely the quantifier that a transition-only finite-order argument would lose.

## 3. Global failure and the exact algebraization barrier

Here T means Spec C[x,t,Z]/(t²-1-x²Z). The plus and minus charts omit D_- and D_+, respectively, where D_± is x=0, t=±1. They cover T; their overlap has x invertible. Thus the preceding divisibility assertion is local on an actual open cover, not just a comparison of two formal expansions.

For each r, the nonconstant polynomial 1+c_r(t²-1)^r has a complex root t_0. It cannot have t_0=±1. The point x=1, t=t_0, Z=t_0²-1 belongs to T and has bracket zero by (*). Hence the map (H_r,G_r) has a critical point away from BOTH boundary components. No member of this family is a scalar pair, even though all its sufficiently short boundary jets are those of one.

For completeness, the KNOWN fixed-coordinate no-mate control from TASK has an immediate transition proof. If a regular G satisfied {x,G}=c with c nonzero, the two polynomial chart expressions would necessarily be

    G_+(x,y)=c*y+a(x),        G_-(x,v)=c*v+b(x),

with a,b in C[x], because their derivatives with respect to y and v are c. The transition v=y+2/x² then forces

    a(x)-b(x)=2c/x²

in C[x,x^-1], impossible for polynomials a,b and c nonzero. This proves that the compatible formal element constructed above has no regular global algebraization. It does NOT prove that a different first coordinate H has no mate.

The missing unrestricted implication is a global consequence of BOTH exact polynomial chart Jacobian identities and their transition, for arbitrary H and G. Finite normal jets cannot supply that consequence alone: the displayed global family meets every prescribed finite normal order without meeting the full identity. A method using all global coefficients, a justified degree bound, or another global invariant is not refuted here. No such new method or bound is obtained in this attempt.

## 4. Scope, readback and stopping record

QUANTITY: existence of unrestricted regular H,G on T with {H,G} a nonzero constant. Status: NO_NEW_DISCRIMINATOR. The countercontrol is proved manually; the unrestricted quantity remains unresolved. No quotient-invariance, parity or degree restriction is silently added. There is no JC2 conclusion, novelty claim, literature certification, computation plan or successor request.

CHEAPEST TEST performed: substitute the explicit polynomial antiderivative family into the exact bracket and check both chart divisibilities and its off-boundary zero. Numeric planning wall: at most 15 minutes of manual reasoning, UNMEASURED as a predictive cost; administrative UTC observations are not a scientific runtime measurement. No scientific process or coefficient artifact was run or emitted.

READ SCOPE: only ROOT's pinned TASK was a scientific input, read FRESH_WHOLE. No linked paper, old report, ledger, code, peer body or live artifact was read. ROOT's optional ring-description and two-bracket-sum observations were not used as premises or duplicated. The already-known x no-mate control and formal-versus-polynomial limitation are explicitly identified, not promoted as new mechanisms.

OPEN: the unrestricted scalar-pair question, with no claimed solution or finite-degree reduction. No new open task or descendant is authorized. Publication checks consist only of own report/PINS WHOLE reads, the sole input's postpin, own-target collision checks, marker-last sealing and the existing documentary transaction.

## COLLISIONS

status: EMPTY for owned destination collisions at first action and before sealing. ROOT's pre-existing TASK remains untouched. Only the leased report partial and the two owned documentary JSON files are authored; the ordinary transaction creates the report/manifest. No canonical/shared artifact is edited. All scientific reasoning stops with the countercontrol above.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8258`.
- Body SHA-256:
  `1f2c575f446664157c2f9c797758ac1c6cb8f42c321d0af7466277e499794554`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
