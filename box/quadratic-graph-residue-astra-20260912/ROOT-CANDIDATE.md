# ROOT raw candidate — quadratic graph source-local residue

September12,2026,11:19UTC. MANUAL CANDIDATE, UNREVIEWED. All identities and
universal quantifiers below need independent derivation. No computation.

Same literal P,Q,R/chart as the supplied context, now H=c+k*y^2 with
c*k!=0. For common-target pairs use

  u=a-b, v=a+b, C=(a+1)/(3b),
  s=delta(C+1)/2, s'=delta(C-1)/2,
  t=delta*v, t'=-delta*u, W=4b/delta,
  Y=(C+1)/2-v, Y'=(C-1)/2+u,
  y=delta*Y, y'=delta*Y'.

Define Z=5v^2-3(C+1)v/2-4b*v^3 and
Z'=5u^2+3(C-1)u/2+4b*u^3, so actual z=delta^2 Z and
z'=delta^2 Z'. The common-target equations themselves do not require
z=z'; each source must now lie on its respective H value.

Use the old POLYNOMIAL EXPRESSIONS, not the old theorem:

  E=-a^2-a+20ab^2-3b^2-8a^3b^2-24ab^4,
  K=(10-24b^2)a^2-4a-1+10b^2-8b^4.

Then Z-Z'=E/b and Z+Z'=K. The new branch equation and cover are

  E_k=E-(k/3)(1-2a)(a+1-6b^2)=0,
  K_k=K-k*(Y^2+Y'^2),
  delta^2=2c/K_k.

Reason Y-Y'=1-2a and Y+Y'=C-2b. These identities should make BOTH
delta^2(Z-kY^2)=c and delta^2(Z'-kY'^2)=c, on an actual nonempty open.
The source and common-target formulas must be checked directly, not just
the vanishing of an abstract E_k.

At u=0 (a=b), put

  P_k(b)=24b^3+24b^2+3(1+k)b+k.

Proposed identity E_k(b,b)=-(1-2b)^2*P_k(b)/3. For every nonzero k,
there should be a SIMPLE root b0 of P_k with b0!=0,1/2. Here is ROOT's
proposed universal justification to audit:

- P_k(0)=k; a triple root would have to be -1/3, but
  P_k(-1/3)=7/9 for every k. Hence at least one simple root exists.
- The only parameter with P_k(1/2)=0 is k=-21/5. In that case
  P_k(b)=(b-1/2)*(24b^2+36b+42/5), whose quadratic factor has
  discriminant2448/5!=0 and has neither0 nor1/2 as a root.

At such a b0, E_k is smooth and u is a local parameter: its b derivative
at fixed u is -(1-2b0)^2 P_k'(b0)/3 !=0. Also

  Y'_0=(1-2b0)/(6b0),
  K_k(0)=-2k*(Y'_0)^2 !=0.

Thus adjoining delta is locally UNRAMIFIED and delta0!=0; a locally split
cover still provides a legitimate normalized branch. Choose y0 with
y0^2=-c/k and delta0=y0/Y'_0. The first source tends to the FINITE point

  x_first=(1-2b0)/(12b0^2*y0), y_first=(6b0+1)*y0,

whereas the second source has x_second=-1/(delta*u) and y_second tends to
y0. The same target has finite limit

  U=(1+4b0)*y0^2/3,
  V=2(1+2b0)*y0,
  W=2(1-2b0)/(3*y0).

Do not substitute the limiting t'=0 expression as an actual finite source
point; the source maps only exist rationally near that normalized boundary.

Simpler residue calculation, not the old K=0 Laurent expansion: along the
second branch z'=c+k*y_second^2 and

  z'=delta^2*[5u^2+3(C-1)u/2+4b*u^3].

At u=0, differentiation would give
2k*y0*(dy_second/du)(0)=3delta0*y0,
so dy_second/du(0)=3delta0/(2k). Therefore

  Res(x_second dy_second)=-3/(2k),
  Res(x_first dy_first)=0,
  Res(eta)=3/(2k) !=0.

Check all terms, signs and normalization; variations of delta and C are
multiplied by u in z' and should not add a first-order term. The residue
is independent of c,b0 and the chosen sign of y0. No claim at k=0: this
unit-K argument breaks there, and the preceding fixed-constant proof is
NOT a premise. The original parameter-space infinity behavior changes.

If alpha is a target-polynomial one-form with d(phi_H*alpha)=dx wedge dy,
polynomial Poincare gives phi_H*alpha-x dy=dF on A2. Pullback to the two
identical target maps forces eta to be exact rational on the curve cover,
whose residue at this place must vanish. If f,g in the target subalgebra
have constant Jacobian j!=0, the target polynomial form f dg/j gives such
an alpha. This repeats the elementary logical interface independently;
it does not assume the previous residue theorem.

Scope: ONLY all c*k!=0 quadratic graphs for this explicit triple. No other
h(xy), arbitrary graph, all embedded planes, source classification or JC2
resolution. ROOT noticed that for nonconstant h the analogous source limit
can instead land on an omitted target line; do not assume a finite first
branch or automatic extension there. This remark is not an extra test.
