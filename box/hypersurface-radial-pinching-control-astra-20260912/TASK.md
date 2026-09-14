# Decisive new control: hypersurface, free dualizing, FULL A2 and radial descent

ROOT September12,2026,14:47UTC. Astra co-research, not FIRST.
Original reserve15:00UTC / HARD15:03UTC NEVER RESET, includes custody.
Basis0d39df3c9fd69c939a8420c54d03228b9077777d. One scientific report:
xmodel/hypersurface-radial-pinching-control-astra-20260912.md.

Hash/read COORDINATION.md FIRST WHOLE (expected
33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597), then
this TASK WHOLE with invitation pin. EXACTLY two scientific inputs;
no inherited/prior/peer/linked/corpus body. ROOT found this independently
while the preceding GAP task ran. No conclusion from that task is needed.
Use unchanged finalizer transaction, own PINS/custody allowed, apply_patch
only in leased partial. No shared/TASK/old artifact edits.

Quantity: check/refute this ONE explicit counterexample to the proposed
global Gorenstein/radial normality criterion, including the STRONGER affine
A3 hypersurface condition. It is NOT claimed to be a polynomial Keller
pair, or a JC2 counterexample. Cheapest test is manual exact ring/form
reconstruction within this reservation. No family or successor is authorized.

## ROOT MANUAL/UNREVIEWED proposal — reconstruct every charged step

Let R=C[x,y], z=x-1, T=zy+3, c=zT-1=yz^2+3z-1. Define

    U=z^2,       V=zc,       W=(1+3z)y+9,
    B=C[U,V,W] subset R.

1. Exact finite presentation and normalization:

    c=UW-3V-1,        cz=V,        z^2=U,
    y=(1+9U)W-27V-9-3Wz.

Hence R=B[z]=B+Bz is finite, and z=V/c gives Frac B=Frac R.
The relation is

    P(U,V,W)=V^2-U(UW-3V-1)^2.

Prove this is the full irreducible hypersurface relation, not merely one
vanishing polynomial: over C(U,V), solving for W requires sqrt(U), and
the polynomial in W is primitive over C[U,V]. The normalization is smooth
R. In particular B is CM with a GLOBALLY FREE dualizing module by
hypersurface adjunction, unlike the preceding five-generator control.

2. Exact pinching and conductor, INCLUDING all points:
cR subset B because R=B+Bz and cz=V. Modulo c,

    R/(c)=C[t,t^-1],     z=t^-1, y=t^2-3t, x=1+t^-1,
    T=t, U=t^-2, V=0, W=t^2.

Thus B/(cR)=C[t^2,t^-2], and B is the EXACT inverse image of this even
subring. It identifies the free pairs t~-t on the smooth embedded C* curve
D={c=0}; there are no fixed points since t!=0. It is proper: T mod c is
odd, so T not in B. Conversely if rR subset B, r and rT restrict to even
Laurent polynomials; since t is an invertible odd element, r mod c=0.
The exact conductor is I=cR. No radical-only or higher-congruence shortcut.

3. Unramifiedness: off c=0 the map is an isomorphism. On D, z!=0 and
J(U,c)=2z^3 is a local unit, so dU,dc generate source cotangents.
Hence Omega_(R/B)=0 everywhere. The hypersurface's singular locus is
V=c=0,UW=1: if U=0, P=0 forces V=0 but P_U=-1, so those points are
smooth. With U invertible, coordinates(U,V,c) give P=V^2-Uc^2,
an ordinary double surface along V=c=0. Do not infer global nonnormality
just from an excessive generator count; exact ring/properness already proves it.

4. SPECIFIC radial KAEHLER descent, not just arbitrary area exactness:
for alpha=(xdy-ydx)/2, direct substitution on D gives

    alpha|D=(t-3/t)dt
           = ((1-3t^-2)/2) d(t^2).

This is invariant under t->-t, indeed in image Omega_(B/I)^1 -> Omega_D^1.
Take beta0=((1-3U)/2)dW in Omega_B^1. Its pullback agrees with alpha on D.
To prove an ACTUAL global Kahler lift exists (not merely curve agreement),
put M=image(Omega_B^1 -> Omega_R^1). Since Omega_(R/B)=0 and cR subset B,

    c Omega_R^1 subset M.

Also a dc=d(ca)-c da belongs to M for EVERY a in R. The conormal exact
sequence gives kernel(Omega_R^1 -> Omega_(R/(c))^1)=c Omega_R^1+R dc.
Therefore alpha-beta0 belongs to M, and alpha itself has a global lift
beta in Omega_B^1; d beta pulls back to dx wedge dy. Audit this exact
module argument carefully. An explicit finite expression for beta is
welcome if short, but not required when this existence proof is complete.

5. Free dualizing/residue sanity and Euler failure:
P_W=-2U^2 c and J(U,V)=2z^4. Thus the rational adjunction generator
dU wedge dV/P_W pulls back to -dx wedge dy/c. The cancellation is an
identity in rational forms, not a claim that J(U,V) is globally a unit.
Along D, Res(dx wedge dy/c)=dt with the dc-first convention; under t->-t
it changes sign as required. This checks that freeness genuinely survives.
Directly E=(x partial_x+y partial_y)/2 satisfies

    E(c)|D=t-3/t,

an odd nonzero Laurent polynomial. Therefore E(c) not in B, although c in
B, and E(I) not subset I. The generic paired values are opposite, not
equal nonzero constants, in agreement with the prior necessary identity.

## Scope and attacks

If all steps survive, this refutes EVEN finite birational unramified
normalization from ALL A2 + affine A3 hypersurface/free dualizing module
+ radial form descent => normality or Euler stability. The extra
Keller hypothesis still matters: NO pair f,g in B with J(f,g)=1 and
beta=dH+f dg, H in B, is supplied. The coordinate pair(U,V) has Jacobian
2z^4 and is NOT Keller. Do not call this a JC2 counterexample, exclude
all possible Keller pairs in B without proof, or infer global polynomial
Darboux from an arbitrary descended one-form.

Give independent checks of finite module, irreducibility, exact conductor,
curve embedding and free involution, EVERYWHERE unramifiedness, the
conormal/Kahler lifting argument, adjunction volume factor and Euler values.
Retain at least one meaningful negative/positive check (B=R is the positive
case; the nonunit J(U,V) is a negative check against a false Keller reading).
If any step gaps, isolate it rather than expanding into another family.
No primary/literature novelty claim, descendant, FIRST or canonical OPEN.

Manual math only. NO scientific interpreter/CAS/helper/import/AST/test/
syntax/compile/dummy, network/AWS/SSH/agent/protected-tree operation.
Inert text/hash/UTC and existing administrative finalizer only. Never
enter/enumerate/search/read/status/control jc2-lean or its public mirror.
Max scientific body about12000bytes. Own WHOLE and BOTH input postpins
before unique BODY-END LAST. Final report/manifest WHOLE, expected verify,
custody SHA FIRST and actual ALL WRITERS IDLE before FINAL; no later writes.
