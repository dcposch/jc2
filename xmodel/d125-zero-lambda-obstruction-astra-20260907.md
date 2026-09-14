# D125 lift: the two lambdas generate the unit ideal

2026-09-07; root-suggested DESK lemma, PRODUCER-CHECKED. No baseline dependency or production authority. The terminal lift contract `433cc2fe…` and gate `4295593a…` were read wholly and hash-matched; full pins are in the owned `inputs.json`.

**Exact statement.** Let R be any commutative algebra over K=Q or Q[rho]/(rho²−3rho+1), including nonreduced quotients. Let A(g,p),B(g,p) be finite ordinary polynomials over R, and define

    phi(g)=v^-1, phi(p)=v^4*u−lambda2*v²−lambda3*v−v^-1,
    P=phi(A), Q=phi(B).

Assume ALL negative-v coefficients of P,Q vanish and [A,B]=c*g². Then **c belongs to (lambda2,lambda3) in R**. If c is a unit (fixed nonzero field constant, or zc=1), then (lambda2,lambda3)=R. Thus in the complete guarded source ring S/I, this is the exact ideal equality I+(lambda2,lambda3)=S, not merely a radical statement. It persists under any further coefficient quotient. The lemma needs neither degree15/25, monicity, faces, nor a domain hypothesis; the reviewed 30+75 rows supply ALL negative rows for the actual client.

**Proof and finite certificate form.** For C=sum c_ij*g^i*p^j, its Laurent coefficient f_C=[u^0*v^1]phi(C) is

    sum c_ij*(-1)^j*j!/(b!d!(j−b−d)!)*lambda2^b*lambda3^d,

over b,d≥0, b+d≤j, 3b+2d=i+j+1. Since i,j≥0, every summand has b+d>0. Partition the sum into b≥1 and b=0,d≥1, divide each part formally by lambda2 or lambda3 respectively, and call the resulting polynomials U_C,V_C. This defines an exact finite polynomial identity f_C=lambda2*U_C+lambda3*V_C without dividing by a parameter or assuming it invertible.

All negative rows make P,Q ordinary over R. The chain rule gives [P,Q]=v²*phi(c*g²)=c in R[u,v,v^-1]. The map R[u,v]→R[u,v,v^-1] is injective even with nilpotents, since multiplication by v shifts the free monomial basis. Therefore [P,Q]=c is also a polynomial identity, evaluable at the origin. Put p1=[u^1*v^0]P and q1=[u^1*v^0]Q. Then

    c=p1*f_B−q1*f_A=lambda2*M2+lambda3*M3,
    M2=p1*U_B−q1*U_A, M3=p1*V_B−q1*V_A.

These are coefficient-ring identities. With zc=1, the explicit quotient-ring witness is 1=lambda2*z*M2+lambda3*z*M3; use z=c^-1 for a fixed field unit. Equivalently these expressions give membership modulo the full negative/Jacobian/guard ideal, without assuming a point or properness.

**Ordinaryness is essential.** At lambda2=lambda3=0, A=g and B=g²*p+g³ have [A,B]=g² but lift to P=v^-1,Q=v²*u with [P,Q]=1. Their formal [u^0*v^1] coefficients are both zero; origin evaluation of the Laurent derivatives is invalid. The actual missing polynomiality row is [u^0*v^-1]P=1. This toy was already explicit in the charged contract §7 and gate §5; it is reused, not claimed new. Neither charged report explicitly states the unit-ideal lemma; no wider novelty claim is made.

**Consequence and controls.** Spec(S/I)=D(lambda2) union D(lambda3); both-zero specialization is the zero ring. This only licenses a two-open cover, not either lambda individually a unit, a normalization, or added global equations. For comparison, x and 1−x generate K[x] but neither is a unit. No point, unit certificate for I itself, reduced production model or global JC2 claim follows. Owned standard-library `check.py` verifies 36 monomial jets by repeated multiplication, both ordinary generator fixtures (f=-lambda2 and f=-lambda3), and the Laurent toy. Normal/-O pass; adding an actual +v to phi(p), or dropping the actual failed negative row, makes the same checks fail in both modes. Six-run batch:1.32s under30wall/25CPU/512MiB. No full client expansion, CAS, AWS, solve, extra lane, shared edit or live peer read; terminal custody has all writers idle.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3749`.
- Body SHA-256:
  `cbd401912ea78e75a86565c38d33d8af349e653b63b7641d7af3333edb5d9b05`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
