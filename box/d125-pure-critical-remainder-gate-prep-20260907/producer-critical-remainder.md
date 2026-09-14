# D125 pure source: the critical first remainder is regular

2026-09-07. **PROVISIONAL theorem: every genuine finite pure-center source
arc in the accepted14v first-contact setup has ord(alpha)>=j (allowing
infinity).** This excludes the entire remaining finite interval
2j/3<=ord(alpha)<j of15b. It does not exclude the case ord(alpha)>=j, prove
that a guarded point degenerates to this boundary, or prove source emptiness
or JC2. No subsequent mathematical child or computation is authorized here.

The new step is a filtered, coefficientwise division argument, NOT monic
division or an assumed Pell equation. It proves regularity only for the
first nonzero remainder. The exact source Jacobian then supplies a pole
contradiction. Root suggested the critical-target primitive and normality
bypass; the retained zero-fiber equation and filtered remainder proof below
are the producer's synthesis. This is pending independent review.

## 1. Inputs and exact coordinates

Use accepted14c/f/g/v and15b at their literal source and imported-centralizer
trust. The terminal2200 Astra cross was read completely as history; its
square-class controls are not premises. No live report was read. In the
notation of14v, over a characteristic-zero field, consider a genuine
K[[s]] arc with k(s)=kappa*s^m+..., kappa nonzero, and

    R_s=R+h(s)S, R=p^2 V, V=g^3+p^3-3p,
    S=p^3+gp^2-p, h(0)=0,
    F=A-R_s^3-alpha R_s, ord(F)=j<m,
    F_j=R C, ord(G)>=2j, ord(delta)=d>=j+1.

Here C is nonzero, even, regular, C(0)=0 and V does not divide C. Every
coefficient of F is polynomial of weight at most3 for w(g)=5,w(p)=-7;
w(R_s)=1. These are the actual source conclusions, not arbitrary rational
jet hypotheses. The saturated low rows remain imposed through14v; in
particular [p]F=alpha*h is NOT set to zero. All moving scalar references,
including every centralizer power and the mixed reference correction, remain
present. Assume for contradiction that a=ord(alpha) is finite and a<j.

As in15b, extend constants to Kbar and set L=Kbar(V). Formal implicit
coordinates at the generic point of V give g=g(s,z), R_s(g(s,z),p)=z.
The invertible initial derivative is 3p^2g^2 in L. Write

    Fhat=sum f_n(s) z^n, Ghat=sum g_n(s) z^n,
    D=partial/partial p at fixed z.

All f_n have order>=j and all g_n order>=2j. The involution sigma on L
satisfies sigma(f_n)=(-1)^(n+1)f_n, and similarly for g_n. Its scalar field
is fixed. Hence a nonzero leading coefficient of f_0 or g_0 is odd and
nonconstant, so differentiation D does not change its s-order. The constant
field of this nonzero derivation on the one-variable characteristic-zero
function field L is Kbar. No regularity of arbitrary higher implicit
coefficients is assumed.

## 2. Filtered first-remainder lemma

Let q=ord(f_0), allowing infinity. If finite, its leading coefficient is a
REGULAR function on the affine curve V=0.

Proof: recursively subtract s^i R_s Q_i from F whenever its current
coefficient P_i vanishes on V. The remainder still has weight<=3. Since V
is irreducible, V divides P_i. The accepted14v elementary weight lemma
gives R divides P_i: writing P_i=V U, w(U)<=-12 excludes all monomials of
p-degree0 or1, so p^2 divides U. Put Q_i=P_i/R. Then w(Q_i)<=2, and
w(R_s Q_i)<=3, preserving the induction. All objects are polynomials; their
degrees stay bounded since deg(F)<=13 and deg(R_s)=5. No ordinaryness of
Q_i is used or asserted.

The subtraction vanishes IDENTICALLY after setting R_s=0. Before order q,
the first nonzero coefficient of the current remainder must vanish on V,
so the next subtraction is available. At order q, the nonzero residue is
P_q modulo V, a regular polynomial residue. If q is infinite the same
recursion continues formally; no claim of convergent or rational quotient
is required. Thus this handles every intermediate order and moving h term.

The weight is essential. If it is dropped, the actual degree-three input
V satisfies, on R_s=0,

    V=h*(1/p-g-p).

Its first moving residue has a pole at the origin. V has weight15, and the
related input gpV has weight13 and is divisible by V but not R. These are
actual changed-object countercontrols, not source points. This explains why
unrestricted monic division or generic implicit regularity was unsafe.

Choose a scalar Puiseux root r_s^2=-alpha/3, with leading rho and order a/2.
Set U=Fhat(s,r_s), f=ord(U). The first-remainder lemma and parity give

    f=min(q,j+a/2),

and its leading coefficient psi is regular and nonconstant on affine V.
Indeed, below j+a/2 it is the regular nonzero odd remainder; at equality
it is that remainder plus rho*C, whose even part is nonconstant; if
q>j+a/2 it is rho*C alone. C modulo V is nonconstant since it vanishes at O but
is not zero. Taylor terms of z-degree>=2 start strictly after j+a/2.
This proves exactly the regularity needed, without claiming it for later
Taylor or remainder coefficients.

## 3. Exact zero-fiber equation bounds every cross term

The full source identity, not its truncation, is

    H=(3z^2+alpha)Ghat-delta Fhat-(5/3)z Fhat^2,
    D H+Fhat_z D Ghat-D Fhat*Ghat_z=T(s,z),
    T=-(5/9)k(s)^3*g(s,z)^2/R_g(s,g(s,z),p).

Here R_g=p^2(3g^2+h). Both T(s,0) and T(s,r_s) have exact order3m,
with leading coefficient -5*kappa^3/(27p^2). This uses the actual target,
including its sign and g^2 factor. All scalar b_s(R_s) differentiate away;
neither b1 nor b3 has been set to zero. In particular the corrected15b
identity with the b3*h^3 term is unchanged.

At z=0 the exact equation is

    (alpha+f_1)Dg_0-(delta+g_1)Df_0=T(s,0).

Let v=ord(g_0). Since a<j, ord(alpha+f_1)=a, and oddness makes
ord(Dg_0)=v when finite. Therefore

    v >= min(q+min(d,2j)-a, 3m-a).                 (1)

Infinity cases have their usual valuation meaning. Possible cancellation
inside delta+g_1 only raises its order. Thus no extra normalization of the
linear or cubic scalar kernels, and no assumed first-remainder balance,
has entered (1).

At z=r_s the non-cross part is exactly

    -delta DU-(10/3)r_s U DU.

Its order is

    M=min(d+f,a/2+2f).                            (2)

It cannot cancel internally: at equal orders its leading derivative is a
nonzero scalar quadratic polynomial in the nonconstant psi. The cross
bracket has order at least

    N=min(j+v,3j+a/2,2j+f).                       (3)

This follows directly from ord(Fhat_z)>=j, ord(Ghat_z)>=2j,
ord(DU)=f and ord(DGhat(s,r_s))>=min(v,2j+a/2).

For all the allowed orders, (1) implies

    N > min(M,3m).                               (4)

Here is the full inequality check, not sampled evidence. Since f<=j+a/2
and a<j, both 3j+a/2 and 2j+f exceed M. For j+v, the target branch
j+3m-a exceeds3m. The other branch exceeds M: if d<=2j, use
j+q+d-a >= j+f+d-a > M; if d>2j, use
3j+q-a >=3j+f-a > a/2+2f >= M, with last strict difference at least
2(j-a). Thus every intermediate cross contribution is retained and bounded.

The exact equation forces M=3m, and at that order the cross bracket is
absent. In particular the earlier weaker necessary inequalities
3a>=6m-4j and d>=3m-j-a/2 follow, but the proof does not stop there.

## 4. The actual target primitive gives the contradiction

Let lambda be delta_d if d+f=3m and zero otherwise; let mu=(5/3)rho if
a/2+2f=3m and zero otherwise. At least one is nonzero. The coefficient
equation at3m is

    -D(lambda*psi+mu*psi^2)=-5*kappa^3/(27p^2).

Consequently, in L,

    lambda*psi+mu*psi^2 = constant-5*kappa^3/(27p).

The left side is regular on affine V by Section2. The right side is not:
p vanishes at its affine point O=(0,0), so 1/p cannot be regular there.
The coefficient is nonzero. This contradiction excludes finite a<j.
No genus, Picard, properness, finite-map, Pell or global degeneration theorem
is imported. A rational square root of a regular function would indeed be
regular by normality, but that conditional bypass is not needed: the source
weight directly supplies the first remainder's regularity.

## 5. Evidence, exact limitations, and stop

Fourteen final capped ordinary/-O runs pass with byte-identical witnesses and
zero Assert nodes. Actual mutations freeze R_s, feed gpV to the filtered
input check, omit the formal cross bracket, change the critical factor,
change the target Jacobian factor, or reverse the primitive sign. Controls
expand only actual factors of degree<=5 and independent formal-coordinate
polynomials. The finite valuation checks illustrate, but do not prove, (4).
No degree15/25 source pair, high actual R power, full rows, CAS, AWS/SSH,
solver, live peer, new agent or canonical edit was used. The rational-string
witness (final-witness*.json/final-replay.json; the earlier pre-cosmetic-cleanup
run is retained but not charged as the final replay) SHA256 is
`a21b8c2a35768ca144a69f336fec870105bfbbc2882a2d40fe90b30098597377`.

This is a new PRODUCER-CHECKED, unreviewed source theorem, not a promotion.
It leaves ord(alpha)>=j, alpha=0, other centers and the existence of a
finite boundary degeneration outside its conclusion. It is neither a
guarded point nor a claim that a nilpotent jet extends. Custody pins the
terminal inputs and owned artifacts; the transaction is verified and all
writers are idle at handoff. STOP/IDLE.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9220`.
- Body SHA-256:
  `5ed0071e97027a4e09d10baf068b4ba0ad67d580c26db4517c7425734b70aca7`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
