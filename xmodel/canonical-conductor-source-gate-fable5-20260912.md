# Fable5.1 FIRST: actual conductor constraint and full-plane descent control

Tag canonical-conductor-source-gate-fable5-20260912. Different-model hostile
FIRST of two completed independent manual producers: Astra
(canonical-conductor-euler-residue-astra-20260912) and ROOT
(full-plane-radial-descent-control-root-20260912). First action
2026-09-12T14:07:34Z; reserve 14:20Z, HARD 14:23Z. All three snapshots in
/tmp/jc2-lane.UnTdCm/inputs were hashed before any body was read and match the
expected pins (table in Custody). Fresh WHOLE unclipped reads, COORDINATION
(806 lines) first, then Astra, then ROOT. No inherited reader, corpus, linked
body, peer output, interpreter or CAS; manual reconstruction only. Result
stays PROVISIONAL pending ROOT intake; no JC2 conclusion.

## Verdict summary

- A (exact conductor I=P_H(f,g,H)R, not its radical): CONFIRMED, conditional
  on the packet hypothesis that B is finite in R with normalization R.
- B (paired Euler identity, transverse-double reduction, exclusion of
  (h_d-a)R with d>0, a nonzero): CONFIRMED in exactly that scope.
- C (full-plane pinching ring, conductor uR, descended beta, both Euler
  failures): CONFIRMED, elementary, no standard theorem consumed.
- D (nontrivial dualizing line, B not a hypersurface): CONFIRMED under the
  two named standard facts, whose applicability I audited, plus my own
  elementary non-freeness check; kept separate from C.
- No REFUTED item; no GAP beyond the explicit conditionality in A/B.

## A. Exact Keller conductor

Hypotheses audited, not deferred. R=C[x,y], J(f,g)=1, dH=alpha-f dg with
alpha=(x dy-y dx)/2; H exists because alpha-f dg is closed (d of both terms
is dx wedge dy). B=C[f,g,H] finite in R with Frac B=Frac R is a PACKET
ASSUMPTION; neither producer proves it for any actual Keller pair, and every
A/B statement is conditional on it. Given it: dim B=2, the kernel of
C[U,V,W]->B is a height-one prime of a UFD, so B=C[U,V,W]/(P) with P
irreducible; hypersurface, hence CM and Gorenstein. f,g are algebraically
independent: a minimal relation F(f,g)=0 gives F_U(f,g)df+F_V(f,g)dg=0,
wedging with dg and df kills F_U(f,g),F_V(f,g), and minimality plus char 0
forces F constant. So P has positive W-degree, P_W is nonzero of lower
W-degree, P does not divide it, c=P_W(f,g,H) is nonzero in B. No monicity in
W and no finiteness of the Keller map (R over C[f,g]) is used anywhere.

Canonical generator: the Poincare residue of dU wedge dV wedge dW/P is the
global generator eta=dU wedge dV/P_W of omega_B (equal to dV wedge dW/P_U
and -dU wedge dW/P_V where those are defined); omega_B is torsion-free of
rank one, so omega_B=B*eta inside the rational two-forms of L=Frac R. Its
pullback is df wedge dg/c=dx wedge dy/c, using J(f,g)=1 exactly here.

Finite duality: R is maximal CM over B (a system of parameters of B_m
generates an ideal primary to each of the finitely many maximal ideals of
R above m, and R there is regular), so Ext^i_B(R,omega_B)=0 for i>0 and
omega_R=Hom_B(R,omega_B) via the trace. The trace pi_* omega_R -> omega_B is
the identity over the dense open where the birational finite map is an
isomorphism; both sheaves are torsion-free, so on rational forms it is the
identity, no twist. Hom_B(R,B)={q in L: qR in B}=I (q=q*1 in B), so
Hom_B(R,omega_B)=I*eta as submodules of Omega^2_L, and omega_R=R dx wedge dy.
Hence I*dx wedge dy/c=R dx wedge dy, I=cR as ideals, c in I. R^*=C^*, so c is
the unique generator up to a nonzero constant. CONFIRMED.

Volume-factor control (Astra D) recomputed: U=t^2-1,V=s,W=t(t^2-1),
P=W^2-U^2(U+1); R0=A0+tA0, B0=A0+UtA0 (A0=C[U,s]); r=a+tb has r,rt in B0
iff U divides a and b, conductor U R0; P_W=2tU differs by the volume Jacobian
J(U,V)=2t, and dU wedge dV/P_W pulls back to dt wedge ds/U, so I*eta=omega_R0
holds while c=P_W fails: J=1 is load-bearing, not decorative. Own ramified
check: U=t^2,V=s,W=t^3, P=W^2-U^3, P_W/J(U,V)=2t^3/2t=t^2, the known cusp
conductor t^2 R0; so A needs no unramifiedness, only finite, birational, MCM.

## B. Paired Euler identity and shape exclusion

Local factorization. Over a target point b with source preimages a_1,a_2,
J(f,g)=1 makes (U,V)=(f,g) local coordinates at each a_i, so each source germ
is a graph W=H_i(U,V); finiteness lets the two germs exhaust the image germ,
birationality forbids H_1=H_2 identically. P is reduced, so in the analytic
local ring P=u(W-H_1)(W-H_2), u a unit. Differentiating and restricting,
c_1=u_1 delta, c_2=-u_2 delta with delta=H_1-H_2, u_i=u(U,V,H_i), and u_1=u_2
on delta=0. These are restrictions of the one global c, not renormalized.

Identity. i_E(dx wedge dy)=alpha with E=(x d_x+y d_y)/2, and alpha=dH+U dV,
so in the chart i_(E_i)Omega=dH_i+U dV and i_(E_1-E_2)Omega=d delta.
Evaluating on E_1-E_2 gives Omega(E_1-E_2,E_1-E_2)=0=(E_1-E_2)(delta), so
E_1(delta)=E_2(delta) on the base. On delta=0 the delta*E_i(u_i) terms
vanish: E(c)(a_1)+E(c)(a_2)=u_1E_1(delta)-u_2E_2(delta)=0. No transversality
and no residue sign convention enter. Local opposite-nonzero control
recomputed: H_1=V+U,H_2=V,u=1 gives P_W=2W-2V-U, restrictions U and -U,
E_1=(1+U)d_U-d_V, E_2=(1+U)d_U, values 1 and -1 on U=0; paired equality,
not individual vanishing. CONFIRMED.

Sum of orders. Over an unramified finite birational map a target point with
one preimage is normal (R_a=B_b+m_bR_a and Nakayama), so a conductor point
has r>=2 graph branches and c_i=u_i prod_(j!=i)(H_i-H_j). Along a conductor
component C_i through a_i, ord(c)=sum over companions j of ord(H_i-H_j),
each term a positive integer, non-companions contributing zero after
shrinking. By A this ord is the conductor multiplicity; value one forces one
companion with simple contact, i.e. d delta nonzero generically, a transverse
double curve. CONFIRMED; it is derived from the actual P_H, not assumed.

Exclusion. If I=(h_d-a)R, d>0, a nonzero: by A, c=lambda(h_d-a), lambda in
C^*. Euler gives E(h_d)=d h_d/2, so E(c)=lambda d a/2 on the whole level set,
which is nonempty (nonconstant polynomials are surjective on C^2), smooth and
reduced (gradient nonzero there). Every multiplicity is one, so a generic
transverse double pair exists and B gives lambda d a=0, contradiction.
CONFIRMED for the exact ideal shape. Not excluded by this: a=0, non-reduced
conductors with the same support, arbitrary r>=3 traces, conicality,
normality, or any claim that c is constant.
conductors with the same support, arbitrary r>=3 traces, conicality,
normality, or any claim that c is constant.

## C. Full-plane ring control

Independent derivation. u=x^2-1, sigma=-id, S=C[x^2,xy,y^2]=R^sigma (every
even monomial is a product of the three), R=S+Sx+Sy. S+uR is a ring
(uR*uR in uR), contains a,b,c,d=ux,e=uy; conversely uR=uS+dS+eS and
u=a-1 in S, so B=C[a,b,c,d,e]=S+uR=S+Sd+Se, both inclusions. Pinching:
S-elements and u-multiples satisfy r(1,t)=r(-1,-t); conversely the odd part
of such r satisfies r_odd(1,t)=-r_odd(1,t)=0 and likewise on x=-1, so the
coprime factors x-1,x+1 divide it and r in S+uR. Finite: R=S+Sx+Sy.
Birational: x=d/u,y=e/u. R regular, so R is the normalization. x is not in
B: x(1,t)=1, x(-1,-t)=-1. Unramified everywhere: off u=0, dx=(dd-x du)/u; on
x=+-1 the matrix of (da,db) in (dx,dy) is [[2x,0],[y,x]] with determinant
2x^2=2, so dx,dy lie in R_p dB and Omega_(R/B)=0 at every point of A^2.
Conductor: uR*R in B; conversely r,rx in B give v(t)=r(1,t)=r(-1,-t) and
v=-v from rx, so r vanishes on both lines and u divides r. I=uR, both
inclusions. beta=(1/2)db-e dd-((4-3a)/2)b da is a Kaehler one-form of B;
db=y dx+x dy, da=2x dx, dd=(3a-1)dx, and (a-1)(3a-1)+(4-3a)a=1, so beta pulls
back to alpha and d beta to dx wedge dy, with no source puncture. Euler
failures: E(u)=x^2=1 on u=0, so E(I) is not in I; E(d)=(3/2)d+x, E(e)=(3/2)e+y
with x,y not in B, so E(B) is not in B. The positive control B=R is
E-stable. CONFIRMED; the refuted inference is exactly ROOT's section 4 display.

## D. Hypersurface boundary of the control

Local node: B is the fiber product of R with C[t] over the value map
r->(r(1,t),r(-1,-t)); completing at a glued point (completion is exact on
finite modules) gives C[[t,n_+]]x_(C[[t]])C[[t,n_-]], and the map from
C[[t,n_+,n_-]] is onto (h+n_+f_1+n_-g_1) with kernel exactly (n_+n_-).
So the value-only gluing yields the stated normal-crossing node, Gorenstein,
omega_B invertible; elsewhere B is smooth. Duality under a hypothetical
global generator eta: R is MCM over B and the map is finite birational, so
the A argument applies verbatim: I*eta=R dx wedge dy, I=uR, R^*=C^*, hence
eta=kappa dx wedge dy/u. Residues with one convention (coefficient of
dn/n wedge dy, n the local normal): (kappa/2)dy at x=1, -(kappa/2)dy at
x=-1; the gluing has t=y on x=1 and t=-y on x=-1, so both become
(kappa/2)dt and the sum is kappa dt, nonzero. The nc dualizing condition
(log poles on the normalization, residues summing to zero along the double
curve, model pair dt and -dt for n_+n_-=0) is violated, so no global
generator exists: omega_B is a nontrivial line bundle and B is not a
hypersurface, nor a complete intersection. CONFIRMED, conditional only on
the two named standard facts, whose hypotheses (finite birational, MCM
source, nc double curve) I verified above; it is separate from elementary C.

Own elementary cross-check. The residue condition reads phi(1,t)+phi(-1,-t)=0
for xi=phi dx wedge dy/u, so omega_B=M dx wedge dy/u with M=Sx+Sy+uS. Then
(M:R)={phi: phi,phi x,phi y in M}=uR, so Hom_B(R,omega_B)=R dx wedge dy=omega_R,
the two standard facts agree on this ring. M is not free: a generator would
divide x and y in R, hence be a nonzero constant, but constants are not in M.
Descended beta and area give no dH+f dg with J(f,g)=1 in B and no Keller
pair; ROOT claims neither, and I add no such claim.

## Scope and boundaries

A and B are conditional on the packet hypothesis that the actual source
B=C[f,g,H] is finite in R with normalization R; they give the exact ideal
cR, the paired identity on generic double pairs, and exclusion of (h_d-a)R.
C and D are one full-plane discriminator: finite, birational, everywhere
unramified, alpha descends, yet E stabilizes neither B nor I, and the ring
is not a hypersurface, so it never meets A's hypotheses. Nothing here is a
Keller pair, a normality statement, a conicality statement, or JC2. No
family, degree, jet, parameter or control expansion, no descendant, no
canonical OPEN, no charge_basis.

## Custody

| basename | expected = observed SHA256 |
|---|---|
| COORDINATION.md | 33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597 |
| canonical-conductor-euler-residue-astra-20260912.md | 0b5aba8a38c17b17669c3c7f057b0d6c1457333c6d6923a65502a5371ffb5a66 |
| full-plane-radial-descent-control-root-20260912.md | 712af8433ded82a8449000a02c24a1b58c6ee33ec0c84f18f810af3662fdf92a |

Pre-read hashes taken 14:07:34Z; postpins below. Only apply_patch wrote this
file; commands used were sha256sum, wc, ls, sed, cat, date. No interpreter,
CAS, network, git, process inspection, agent, corpus or shared edit.

Postpins 14:15:13Z after all bodies and section writes: all three input
hashes unchanged and equal to the table above. Own WHOLE readback and
quantity/scope/control/destination check performed before the marker; sole
destination xmodel/canonical-conductor-source-gate-fable5-20260912.md.

<!-- BODY-END -->
