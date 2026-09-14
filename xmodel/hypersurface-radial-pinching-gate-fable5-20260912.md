# FIRST (Fable 5.1) — full-plane hypersurface radial pinching control

Tag hypersurface-radial-pinching-gate-fable5-20260912. Different-model FIRST of
the Astra co-research report. Status: MANUAL/PROVISIONAL pending ROOT intake.
NOT a JC2 counterexample. No finalizer, no charge_basis.

First action 2026-09-12 15:03:45 UTC. Reserve 15:10 UTC, hard 15:13 UTC, never reset.
Inputs pre-pinned before any body (both match expected):
- COORDINATION.md 33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597
- hypersurface-radial-pinching-control-astra-20260912.md 08457a1dbf44378f9b4b066247d7f8c8311addced8ddeee430848b8c0aeb0a3d

Read order: COORDINATION.md whole first, then the report whole. No other body.
All algebra below was recomputed by hand from the definitions z=x-1, T=zy+3,
c=yz^2+3z-1, U=z^2, V=zc, W=(1+3z)y+9; nothing was taken on the producer's word.

## A. Ring, finiteness, conductor — CONFIRMED

Recomputed: UW=z^2y+3z^3y+9z^2, 3V=3yz^3+9z^2-3z, so UW-3V-1=z^2y+3z-1=c.
(1+9U)W=(1+3z+9z^2+27z^3)y+9+81z^2 and 27V+9=27yz^3+81z^2-27z+9, so
A=(1+3z+9z^2)y+27z and A-3Wz=(1+3z+9z^2-3z-9z^2)y+27z-27z=y. The producer's
side remark (1-3z+9z^2)(1+3z)=1+27z^3 is true but is not the identity actually
used; harmless. Hence x=1+z, y in B+Bz, z^2=U in B, so R=B[z]=B+Bz, finite.
z=V/c with c nonzero gives Frac B=Frac R; R normal, so R is the normalization.

Relation: V^2=z^2c^2=U(UW-3V-1)^2, so P=v^2-u(uw-3v-1)^2 vanishes. As a quadratic
in w: -u^3 w^2+2u^2(3v+1)w+(v^2-u(3v+1)^2). A common factor divides u^3, but the
constant term is v^2 mod u, so content 1 (primitive). A root w in C(u,v) would make
u=(v/(uw-3v-1))^2 a square, impossible (odd u-adic valuation). Gauss: P irreducible
in C[u,v,w]. Kernel of C[u,v,w]->B is prime of height 3-2=1 containing the height-1
prime (P), so equals (P). B=C[u,v,w]/(P): hypersurface, CM, Gorenstein, omega_B free.

Conductor. cR=cB+VB subset B (both inclusions of cR in B and of cR in the conductor
are immediate, since cR is an R-ideal). D=V(c): zT=z^2y+3z=c+1=1 mod c, so z is a
unit with inverse t=T; y=(t-3)t=t^2-3t, x=1+1/t; c is linear in y with coprime
coefficients so R/(c) is a domain, and z parametrizes it: R/(c)=C[t,t^{-1}], smooth
(c_y=z^2 unit). Residues U->t^{-2}, V->0, W->(1+3/t)(t^2-3t)+9=t^2. So B/cR=C[t^2,t^{-2}]
and B is the full inverse image of the even ring: even residue r, choose b in B with
the same residue, r-b in cR subset B. Both inclusions hold. The map D->image is t->t^2,
free (t nonzero), pairs exactly {t,-t}; off D, B_c=R_c since z=V/c. T has odd
residue t, so T not in B: B is a proper subring. Spec R->Spec B is finite, hence proper
and surjective. Exactness: rR subset B forces residues q and tq both even, so q=0 and
r in cR. Ann_B(R/B)=cR as ideals. All checks pass.

## B. Everywhere unramified — CONFIRMED

Global identity: dU=2z dz, dV=c dz+z dc, so (T/2)dU-dV+z dc=(Tz-c)dz=dz using
zT=c+1. From y=A-3Wz, dy=dA-3z dW-3W dz. With A,W,U,V,c in B, dz and dy lie in the
R-span of dB, so Omega_(R/B)=0 globally: finite unramified. Not etale at the double
curve (a flat finite birational map is an isomorphism), and the report does not claim it.

Target singular locus: P_w=-2u^2 C0, P_v=2v+6u C0, P_u=-C0^2-2uw C0 with C0=uw-3v-1;
all recomputed. At u=0, P=v^2 forces v=0, C0=-1, P_u=-1: smooth, correctly kept.
On u invertible, (u,v,C0) are coordinates, P=v^2-uC0^2, singular locus exactly
v=C0=0 i.e. v=0, uw=1; etale-locally P=(v-sqrt(u)C0)(v+sqrt(u)C0), ordinary double
curve. Consistent with the image of D: (U,V,W)=(t^{-2},0,t^2) satisfies V=0, UW=1.

## C. Global Kähler lift — CONFIRMED

alpha|D: dx=-t^{-2}dt, dy=(2t-3)dt, x dy-y dx=[(1+1/t)(2t-3)+(t^2-3t)/t^2]dt=(2t-6/t)dt,
so alpha|D=(t-3/t)dt=((1-3t^{-2})/2)d(t^2)=beta0|D with beta0=((1-3U)/2)dW. Correct,
and correctly flagged as insufficient alone.

Module step: M=im(Omega_B->Omega_R) is a B-module (image of a B-linear map).
Omega_(R/B)=0 gives Omega_R=R.M; multiplying coefficients by c lands them in cR subset B,
so c Omega_R subset M. For a in R, ca in B, so a dc=d(ca)-c da in M. The second
fundamental sequence for R->R/(c) (applicable: any surjection of C-algebras) gives
ker(Omega_R->Omega_D)=c Omega_R+R dc subset M. alpha-beta0 is in that kernel, beta0 in M,
so alpha in M. Sound; this is a global module statement, no gluing.

Finite beta, independently expanded. alpha-beta0 has dy-coefficient
(1/2)[(1+z)-(1-3z^2)(1+3z)]=z(9z^2+3z-2)/2 and dz-coefficient -y(4-9z^2)/2.
With a=(9z-3-2zy)/2 and dc=z^2dy+(2yz+3)dz: a z^2+cz=(9z^3+3z^2-2z)/2 (match) and
a(2yz+3)+c(4y-9)/2=(9yz^2-4y)/2 (match; the y^2z^2 terms cancel). da=(9/2-y)dz-z dy, so
a dc=d(ca)+c[(y-9/2)dz+z dy] and alpha-beta0=d(ca)+c[3(y-3)dz+2z dy]. Substituting
dy and dz: c[3(y-3)dz+2z dy]=ck dz+2V dA-6cU dW with k=3(y-3)-6zW, and
ck dz=(ckT/2)dU-ck dV+ckz dc. So
beta=((1-3U)/2-6cU)dW+d(ca)+(ckT/2)dU-ck dV+ckz dc+2V dA, exactly as displayed.
Coefficients: (1-3U)/2-6cU in B; ca, ckT/2, ck, ckz in cR subset B; 2V in B.
Differentials: dW,d(ca),dU,dV,dc,dA of elements of B. No inverse of c,z,U or any
parameter appears (only the scalar 1/2). Its image in the free module Omega_R is alpha
exactly. Naturality of d: pullback(d beta)=d alpha=dx^dy. This is a descended one-form,
not a Darboux form dH+f dg with J(f,g)=1; no Keller pair is exhibited or excluded.

## D. Dualizing, Euler, limits — CONFIRMED as stated, with limits enforced

J(U,V): U_x=2z, U_y=0, V=yz^3+3z^2-z, V_y=z^3, so J=2z^4 (vanishes on x=1, not a unit).
P_w(U,V,W)=-2U^2 c=-2z^4 c. eta=dU^dV/P_w=2z^4 dx^dy/(-2z^4 c)=-dx^dy/c, a rational
identity only. Adjunction applicability: B is a proved hypersurface in a regular ring,
so omega_B is free on eta regardless of normality. Residue: dc=T dz+z dT, dT=y dz+z dy,
dc^dT=Tz dz^dy=(c+1)dx^dy; c+1 is a unit near D; residue of (dx^dy)/c along D is dt,
which the involution pulls back to -dt: the opposite-residue matching for an ordinary
double curve holds, so eta genuinely lies in omega_B (consistent, not additional).
E(c)=[(z+1)(2yz+3)+yz^2]/2; on D, yz=t-3, yz^2=1-3/t, so E(c)|D=[2t-1-3/t+1-3/t]/2=t-3/t,
odd and nonzero (zero only at t^2=3). Hence E(c) not in B and not in cR while c is in
both: E(B) not subset B, E(I) not subset I. The relaxed package (hypersurface in A^3, free
dualizing, finite birational everywhere-unramified normalization from all of A^2, global
Kähler lift of the radial alpha) is satisfied by a nonnormal, non-Euler-stable B. That
implication is REFUTED. Limits: J(U,V)=2z^4 is not constant; no pair with J=1 and
beta=dH+f dg is supplied or excluded; no global polynomial Darboux theorem follows; the
example says nothing about JC2 and must not be filed as a counterexample.

## Own control (descent criterion, positive and negative instance)

Since ker(Omega_R->Omega_D) subset M, a form omega in Omega_R descends iff omega|D lies
in im(M->Omega_D). M is B-generated by dU,dV,dW, whose residues are -2t^{-3}dt, 0,
2t dt, so im(M->Omega_D)=(odd Laurent polynomials).dt. Criterion: omega descends iff
its D-restriction has odd coefficient. Positive: alpha|D=(t-3/t)dt, odd. Negative:
x dy|D=(2t-1-3/t)dt and y dx|D=(-1+3/t)dt are not odd, so neither x dy nor y dx
descends although each has d=+-dx^dy; only the symmetric radial combination does.
The criterion is therefore non-vacuous and explains why this specific alpha lifts.
Cross-check of A against D: finite duality omega_R=Hom_B(R,omega_B)=conductor.eta gives
R dx^dy=conductor.(-dx^dy/c), forcing conductor=cR, matching section 2 independently.

## Verdict summary and custody

A CONFIRMED. B CONFIRMED. C CONFIRMED. D CONFIRMED (relaxed normality/Euler implication
refuted by this explicit B), with the stated non-JC2 limits enforced. No GAP found in the
one explicit control. Producer wording defects: none load-bearing (one decorative identity
in section 1). Same-model producer agreement was not used as evidence. Result remains
MANUAL/PROVISIONAL pending ROOT intake. No family, jet, descendant, OPEN or extra report.

Custody: no scientific interpreter, CAS, helper, network, git, process inspection or
shared edit. Only apply_patch writes to this single file, read-only cat/sha256sum/date.
Postpins at 15:08:07 UTC after whole readback, both unchanged:
COORDINATION.md 33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597;
report 08457a1dbf44378f9b4b066247d7f8c8311addced8ddeee430848b8c0aeb0a3d.
Scientific words about 1130 (cap 2400). Marker appended last; no writes after.

<!-- BODY-END -->
