# Gate (Fable 5.1 FIRST): fixed constant graph, collision residue

Different-model hostile FIRST of the Astra producer report
`graph-collision-residue-astra-20260912.md`. Manual reconstruction only; no
CAS, interpreter, code, network, or process inspection. The producer claim
stays PROVISIONAL regardless of this verdict; nothing here is promotion.

First action 2026-09-12T11:11:54Z. Reserve 11:33Z, HARD STOP 11:36Z.

## Custody (pre-read)

Inputs hashed in `/tmp/jc2-lane.gNTS2C/inputs` before any body was read; all
three match the expected values:

| basename | bytes | SHA-256 |
|---|---|---|
| COORDINATION.md | 48725 | 33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597 |
| constant-graph-subalgebra-control-astra-20260912.md | 4917 | 590609a7a6f52f72e940a01604c5e6f0c1444277c54bfbb9c69e0fa0c55fd679 |
| graph-collision-residue-astra-20260912.md | 8170 | ac8456a4358484631ececeb4480684adf8e017d48f9713260e703844d7458e9d |

Read order: COORDINATION whole (four unclipped chunks), then both Astra
reports whole. No inherited reuse; no other path, literature or peer output.

## Exact claim under review

For the literal P,Q,R of the control report restricted to z=1 (p,q,r), no
polynomial one-form alpha on the target A^3 satisfies d(phi^*alpha)=dx^dy,
phi=(p,q,r); hence no f,g in C[p,q,r] have nonzero constant Jacobian, with
no degree bound. Extension E: the same for every graph z=c, c nonzero.

Sections A–E and the combined verdict follow.

## A. Source chart and collision correspondence — CONFIRMED

Literal input: u=1+xy, P=z u^3+y^2 u(3u+1), Q=y+3xz u^2+3xy^2(3u+1),
R=2x-3x^2 y-x^3 z. Chart x=1/t, y=s-t gives u=s/t and
R=5/t-3s/t^2-z/t^3, so z=5t^2-3st-Wt^3 with W=R. Expanding
(s-t)^2(3s+t)=3s^3-5s^2t+st^2+t^3 by hand, the z-terms 5s^3/t-3s^4/t^2
cancel the negative powers of the y^2u(3u+1) term, leaving
P=s^2+st-Ws^3; likewise Q=(s-t)+(15s^2/t-9s^3/t^2-3Ws^2)
+(9s^3/t^2-15s^2/t+3s+3t)=4s+2t-3Ws^2. Both reproduced exactly.

Collision: from V, 2t=V-4s+3Ws^2; substituting into U gives
2U=Ws^3-2s^2+Vs, so s,s' are roots of Ws^3-2s^2+Vs-2U. Dividing the
difference by delta=s-s' (nonzero by hypothesis) gives
V=2sigma-W(sigma^2-ss'). Then t=(2(sigma-2s)+W(3s^2-sigma^2+ss'))/2 with
sigma-2s=-delta and 3s^2-sigma^2+ss'=delta(2s+s'), so t=delta(W(2s+s')/2-1)
=delta(a+b) for a=3W sigma/4-1, b=W delta/4; symmetrically t'=-delta(a-b).
C=(a+1)/(3b)=sigma/delta, so s=delta(C+1)/2, s'=delta(C-1)/2. Converse:
with V so defined the two cubic values differ by delta[W(sigma^2-ss')
-2sigma+V]=0, so U is common; the step is reversible off {delta=0, b=0},
so there is no extraneous branch. s=y+1/x is a function of the source
point, so s≠s' proves the two source points distinct; also x=x' needs
a=0 and y=y' needs a=1/2 (y-y'=delta(1-2a)), never both.

z,z': with u=a-b, v=a+b, W=4b/delta I expanded
(z-z')/delta^2=5(v^2-u^2)-3[C(v+u)+(v-u)]/2-4b(v^3+u^3)
=20ab-3aC-3b-8a^3b-24ab^3, and with 3aC=(a^2+a)/b this is E/b with
E=-a^2-a+20ab^2-3b^2-8a^3b^2-24ab^4. Similarly
(z+z')/delta^2=10(a^2+b^2)-3(bC+a)-24a^2b^2-8b^4=K with
K=(10-24b^2)a^2-4a-1+10b^2-8b^4. Hence z=z'=1 iff E=0 and delta^2=2/K.
The collision locus is the double cover delta^2=2/K of the plane curve
E=0; at generic points b,K,u,v,delta are nonzero and finite, so both source
maps are defined: nonempty generic open. Common (U,V,W): U,V by the cubic
argument, W literally shared. The 3D determinant identity and the module
certificate of the control report are consistent (at the origin p=1,q=r=0,
J(q,r)=-2 gives -(p/2)J(q,r)=1) but are not premises of anything below.

Naming note: the control report's u=1+xy and the producer's u=a-b are
different objects; no confusion enters the residue report.

## B. The one-form eta and the local structure — CONFIRMED

x dy=(ds-dt)/t. Branch 1 (s,t)=(delta(C+1)/2, delta v):
[(C+1)/2-v] dlog delta/v+dC/(2v)-dv/v. Branch 2
(s',t')=(delta(C-1)/2,-delta u): -[(C-1)/2+u] dlog delta/u-dC/(2u)-du/u.
Difference: dC coefficient (u+v)/(2uv)=a/(uv); dlog delta coefficient
(C+1)/(2v)+(C-1)/(2u)=[C(u+v)+(u-v)]/(2uv)=(aC-b)/(uv); remainder
-dv/v+du/u=-dlog(v/u). With delta^2=2/K, dlog delta=-(1/2)dlog K:

    eta = a/(uv) dC - (aC-b)/(2uv) dlog K - dlog(v/u),

exactly the producer's form. Every coefficient is a function on the base
curve, so eta descends; it is invariant under delta -> -delta (both source
points map to (-x,-y), x dy invariant), consistent with descent.

At a=b: E(b,b)=-4b^2-b+20b^3-32b^5 and
(2b-1)^2(8b^2+8b+1)=32b^4-20b^2+4b+1, so E(b,b)=-b(2b-1)^2 Q(b). Let
Q(B)=8B^2+8B+1=0, B^2=-B-1/8, B^4=-3B/4-7/64.
E_a=-2a-1+20b^2-24a^2b^2-24b^4 gives E_a(B,B)=14B+7/4=-14B^2 (nonzero:
8B+1≠0). E_b=40ab-6b-16a^3b-96ab^3 gives E_b(B,B)=38B+29/4, so
(E_a+E_b)(B,B)=52B+9, norm 2704/8-468+81=-49≠0. Smooth point; u=a-b is
a local parameter since du restricted to the tangent line vanishes iff
E_a+E_b=0. Slope d=-E_a/(E_a+E_b)=14B^2/(52B+9); both 14B^2·28 and
(20B+9)(52B+9) reduce to -392B-49, so d=(20B+9)/28.

Identity: substituting a=b+u into E-bK and collecting, the u^0 terms
cancel (b^2:-1-3+4; b^3:20-10-10; b^5:-8-24+24+8), u^1 gives 2b-1, u^2
gives -10b-1, u^3 gives -8b^2. So E=bK+(2b-1)u-(10b+1)u^2-8b^2u^3 holds
identically. On E=0, K=(1/b-2)u+(10+1/b)u^2+8bu^3; with
1/b=1/B-(d/B^2)u+O(u^2), k1=1/B-2=(1-2B)/B≠0 (B≠1/2) and
k2=10+1/B-d/B^2. K has a simple zero, 2/K has valuation -1, so
delta^2=2/K is not a square in the base function field: the cover is a
genuine quadratic extension, irreducible, ramified with index 2 at the
unique place above (B,B). Residues pull back multiplied by 2 there.

## C. Full residue at the place above (B,B) — CONFIRMED

Write M=(aC-b)/(2v); since v(C-1)+u(C+1)=2aC-2b, M=(C-1)/4+u(C+1)/(4v).
Then eta=(a/v)C' du/u - M(K'/K) du/u - dv/v + du/u, with
K'/K=1/u+k2/k1+O(u), a/v -> 1/2, v0=2B≠0, C regular (B≠0). Simple-pole
contributions: (1/2)C1 from the dC term; -M1-M0 k2/k1 from the double
pole; 0 from dv/v; +1 from du/u. With C=1/3+(u+1)/(3b):
C0=(B+1)/(3B), C1=(B-d)/(3B^2), M0=(C0-1)/4=(1-2B)/(12B),
M1=C1/4+(C0+1)/(8B). The cancellation (C0-1)/k1=1/3 is exact, so the
double-pole term is k2/12=(10B^2+B-d)/(12B^2). Over 24B^2:

    Res = [24B^2+2(B-d)-(4B+1)-2(10B^2+B-d)]/(24B^2)=(4B^2-4B-1)/(24B^2),

d cancelling exactly. With 4B^2=-4B-1/2 and 24B^2=-24B-3 this is
(16B+3)/(6(8B+1)), and (8B+1)(8B+5)=64B^2+48B+5=-16B-3, so
Res=-(8B+5)/6. The producer's check 6Res+(8B+5)=(4B-1)Q(B)/(4B^2)
also reproduces: 32B^3+24B^2-4B-1=(4B-1)(8B^2+8B+1). Norm of 8B+5 is
64/8-40+25=-7, so neither conjugate residue vanishes; cover residue
-(8B+5)/3, nonzero. Sign of delta does not enter (descent).

Controls (not hash repeats). (i) Independent route: on E=0,
K=uG/b with G=(1-2b)+(10b+1)u+8b^2u^2, so
K'/K=1/u+G'/G-b'/b; at u=0 this gives (10B+1-2d)/(1-2B)-d/B
=(10B^2+B-d)/(B(1-2B))=k2/k1, confirming the double pole's simple part
by a second expansion. (ii) Positive control on the machinery: the
alternative primitive -y dx yields eta'=eta-dF with
F=(C+1)/(2v)+(C-1)/(2u) (F is xy∘pi_1 - xy∘pi_2, verified). dF has a
double pole at u=0; the same Laurent rules give Res dF=C1/2-0-C1/2=0, so
Res eta'=Res eta as exactness demands, and an omitted simple part of the
double pole would have broken this. (iii) Ramification sign: replacing
dlog delta by +(1/2)dlog K (wrong branch relation) gives
1+(20B^2+12B+1-8d)/(24B^2), which does not simplify and retains d; the
correct sign is the only one in which d cancels. All arithmetic is exact
in Q(B); no floating point was used.

## D. Global necessity — CONFIRMED

Suppose alpha=A dU+B0 dV+C0 dW polynomial with d(phi^*alpha)=dx^dy. Then
omega=phi^*alpha-x dy is a closed polynomial one-form on A^2, hence
omega=dH with H=∫_0^1(xA'(tx,ty)+yB'(tx,ty))dt polynomial (each monomial
integrates to a rational multiple; characteristic 0). On the cover Gamma
(irreducible by B) with rational maps pi_1,pi_2 to A^2 satisfying
p∘pi_1=p∘pi_2 etc. identically in the function field (chart identities
plus z=z'=1), pi_1^*(phi^*alpha)=pi_2^*(phi^*alpha) literally, so
eta=pi_1^*(x dy)-pi_2^*(x dy)=-d(H∘pi_1-H∘pi_2). This is the
differential of an element of the function field of Gamma; at every place
of the complete nonsingular model its residue is zero, because
differentiating a Laurent series never produces dw/w. Poles of x∘pi_i or
y∘pi_i at the place (here x'->∞ since t'~omega and y->∞ since
delta->∞) are irrelevant: H∘pi_i is still a rational function. No
injectivity, normality of the image, or finiteness of pi_i is used; only
the existence of the irreducible cover and two rational maps with equal
composite, which B and A supply. Contradiction with C. Arbitrary Keller
pair: f=F(p,q,r), g=G(p,q,r), J(f,g)=c≠0 gives alpha=F dG/c with
d(phi^*alpha)=(1/c)df^dg=dx^dy. So no such pair exists, with no degree
bound; this is a residue obstruction to exactness, not a nonclosed
candidate beta nor a failed bounded ansatz.

## E. Transport to every nonzero constant graph — CONFIRMED

Under (x,y,z)->(λ^-1 x,λ y,λ^2 z), u=1+xy is invariant, so
P->λ^2 P (both terms carry λ^2), Q->λ Q (y, 3xz u^2, 3xy^2(3u+1) each
scale by λ), R->λ^-1 R (2x, 3x^2y, x^3z each scale by λ^-1); checked term
by term. Take λ^2 c=1 and L=L_λ=(λ^-1 x,λ y), det L=1. Then
p_1∘L=λ^2 p_c, q_1∘L=λ q_c, r_1∘L=λ^-1 r_c, so L^*B_1=B_c and
phi_1∘L=D∘phi_c with D=diag(λ^2,λ,λ^-1) invertible. If alpha_c is
polynomial with d(phi_c^*alpha_c)=dx^dy, set alpha_1=(D^-1)^*alpha_c
(polynomial); then phi_c^*alpha_c=L^*(phi_1^*alpha_1) and
L^*d(phi_1^*alpha_1)=dx^dy=L^*(dx^dy), so d(phi_1^*alpha_1)=dx^dy,
contradicting A–D. Pairs: f,g in B_c Keller give f∘L^-1,g∘L^-1 in B_1
with J=J(f,g)∘L^-1·det L^-1, still a nonzero constant. Arrow direction is
sound (L is an automorphism, so both directions hold). c=0 is excluded
(no λ); nonconstant H is not touched.

## Verdicts and surviving statement

A CONFIRMED, B CONFIRMED, C CONFIRMED, D CONFIRMED, E CONFIRMED.

Surviving statement: for the literal P,Q,R and every nonzero constant c,
with phi_c=(P,Q,R)|_{z=c}, no polynomial one-form alpha on A^3 has
d(phi_c^*alpha)=dx^dy; consequently no f,g in C[p_c,q_c,r_c] have
nonzero constant Jacobian, for any degree. Evidence tier: PROVED by
manual reconstruction in this gate; lifecycle remains PROVISIONAL until
ROOT records it. Not claimed: other graphs z=H(x,y), c=0, other
subalgebras, general plane maps, or any JC2 conclusion. No new OPEN.

## Closeout and custody (post-read)

Notation: in C, C' and K' are u-derivatives; in D, A' and B' are labels
for the components of omega, not derivatives.

Quantity: the gate decides the single yes/no residue question and the
five sub-verdicts; all decided, none GAP. Controls: three exact controls
in C (second expansion of the double pole, exactness of dF with a double
pole at the same place, ramification-sign sensitivity). Scope: literal
P,Q,R only, graphs z=c with c nonzero, polynomial target one-forms,
Keller pairs inside C[p_c,q_c,r_c]; nothing about JC2. No charge_basis
line: no exit price is asserted. No artifact_finalize; launcher custody
unchanged. No box or scratch file authored; the launcher's own
`.log`/`.run.v2` sidecars and its `box/.../fable-invite.prompt.md`
predate this report and were not touched. Destination is the unique
report path for this tag.

Postpin 2026-09-12T11:19:21Z, after the whole readback, all three inputs
unchanged:

| basename | SHA-256 |
|---|---|
| COORDINATION.md | 33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597 |
| constant-graph-subalgebra-control-astra-20260912.md | 590609a7a6f52f72e940a01604c5e6f0c1444277c54bfbb9c69e0fa0c55fd679 |
| graph-collision-residue-astra-20260912.md | ac8456a4358484631ececeb4480684adf8e017d48f9713260e703844d7458e9d |

Tools used: sha256sum, date, cat/sed/ls/grep/wc, heredoc appends. No CAS,
interpreter, code, network, git, or process inspection. Sealed at
completion; no edits follow the marker.

<!-- BODY-END -->
