# JOINTDEFECT2110 — full tensor defect versus whole-source sheet budget
Status: EXPLICIT RESIDUAL FORMULA / GAP; internal manual co-research, not independent review.
Launch/report basis c970400652a6b795efb8d9aff19997ec13b1a589.
Selection basis 8c7823001ffbaec2db14d9bd4268a9a9416b5870; public basis 378addbd9bc3fc040d7c2bfdf0e2ee1ce040e145.
No proof or counterexample of JC2, promotion, all-method no-go or automatic successor.

## Scope and changed information
Use the adopted actual divisorial finite h:W→Y of degree e>1 and proper birational k:W→Y.
U=A2 is the WHOLE marked source, C≅B, h*B=eC, k*B=C+Z, and h*Omega=k*Omega.
The normal projective surfaces have rational singularities; exceptional centres lie in {p0,q}.
Set E=Omega_Y^[1](log B), A=h^{[*]}E, Q=E/k_*A and T=R1k_*A.
All assertions below concerning vanishing assume the hypothetical attached noninvertible Keller map.
The accepted web consumer then gives H0(E)=0; the retained stability argument gives H2(E)=0.
We do not assume the proposed global sheet budget or the tensor/sheet inequality.

New information: the whole A2 source proves the needed logarithmic extension and acyclicity
at this conditional scope. The finite defect epsilon_h has an explicit exceptional/evaluation formula.
After retaining and cancelling its evaluation terms, the desired inequality becomes a precise
bound on degrees and torsion in a differential-cokernel filtration plus an exceptional intersection.
The provisional scalar sheet budget supplies no such estimate. The residual formula is given below.

## Target log resolution and acyclicity
Choose pi:S→Y a projective log resolution, isomorphic away from q; D_S=(pi^-1 B)_red.
Every component of D_S is P1 and S\D_S=A2. Put L_S=Omega_S^1(log D_S).
The divisor-class localization sequence, with units(A2)=C* and Pic(A2)=0,
makes the component classes [D_j] a free basis of Pic(S).
For a smooth projective rational surface, H0(Omega_S^1)=H2(Omega_S^1)=0 and
H1(Omega_S^1)=Pic(S) tensor C. These classical smooth-surface facts are explicit premises.
In the residue sequence 0→Omega_S^1→L_S→direct_sum O_Dj→0,
the connecting map sends 1_j to c1(D_j), hence is an isomorphism.
Since H1(O_P1)=0, H^a(S,L_S)=0 for a=0,1,2.

M=pi_*L_S embeds in E by rational-form identification; E/M is finite-length at q.
Leray gives H1(M)=0, and H0(M)=0. Thus H0(E)≅H0(E/M).
Our conditional H0(E)=0 forces M=E and H1(E)=0.
Using H2(E)=0, Leray also gives R1pi_*L_S=0. Consequently chi(E)=0 and gamma_Y=2.
This proves no generation statement about pi*E and no equality pi^{[*]}E=L_S.

## The full source boundary supplies extension, not a thickening bound
Let D_W=(W\U)_red=C+sum E_i and H=Omega_W^[1](log D_W).
This is the reflexive extension from the smooth SNC locus; only finitely many points are excluded.
Rational-form pushforward embeds k_*H in E, with finite quotient, so H0(H)=0.
For any log resolution rho:Z→W, isomorphic over U, put D_Z=(Z\U)_red and L_Z=Omega_Z^1(log D_Z).
The same rational-surface Pic/residue argument gives H^a(Z,L_Z)=0.
The injection rho_*L_Z⊂H has finite quotient. H1(rho_*L_Z)=0, so H0(H)=0 kills that quotient.
Thus rho_*L_Z=H and H1(H)=0. Also H2(k_*H)=H2(E)=0;
Leray for k, whose higher direct images are supported at points, gives H2(H)=0.
Leray for rho now gives R1rho_*L_Z=0. Thus H is acyclic.
The finite quotient k_*H⊂E and their H0,H1 vanishings further give k_*H=E and R1k_*H=0.
No general logarithmic extension theorem has been imported.

At every codimension-one point, finite pullback differentials embed A in H.
Both are reflexive, so the inclusion extends globally; evaluation gives rho*A→L_Z.
This is justified by the preceding whole-source argument, not by determinant-zero alone.
Let N=H/A. Along E_i its generic length is r_i: ordinary ramification contributes r_i-1,
and the source logarithmic normal frame contributes one more. Along C the length is zero.
Here r_i is the ramification index in EULER1755, allowed to equal 1.
N is pure one-dimensional: the depth lemma for the two reflexive surface modules excludes
zero-dimensional submodules. Finite torsion in later curve quotients still must be retained.
The exact sequence and acyclicity give H0(N)=H1(A), H1(N)=H2(A)=0, and
    chi(N)=h1(A)=ell(Q)+ell(T).                                      (1)
Indeed pushing to Y gives 0→Q→k_*N→T→0 and R1k_*N=0.
This produces an actual differential module for the defect; it does not bound its global sections.

A useful controlled part is G=Omega_W^[1](log C), with A⊂G⊂H.
On Z remove residues only on the strict E_i: L'=ker(L_Z→direct_sum O_(strict E_i)).
Each strict E_i is P1, so chi(L')=-s, s=#omitted primes, and H0(L')=H2(L')=0.
The injection rho_*L'⊂G has finite quotient J'; R1rho_*L' has finite length.
Hence chi(G)=-s+ell(R1rho_*L')+ell(J')≥-s.
As for H, k_*G⊂E gives H0(G)=H2(G)=0. Therefore 0≤h1(G)≤s.
Only the residue-one part is controlled. The module G/A retains ramification thickenings and cusp terms.

## A finite model over the smooth target
Let S' be the normalization of the dominant component of W×_Y S.
It is finite nu:S'→S of degree e and proper birational p:S'→W.
Choose a projective resolution v:Z→S' also resolving the full boundary; write rho=pv and f=nu v.
This is the same type of Z used above, still with whole complement U=A2.
Rationality of W gives R1rho_*O_Z=0. In the Leray sequence for pv, R2p_*O_S'=0
because all fibres have dimension at most one. Thus p_*R1v_*O_Z=0.
R1v_*O_Z has finite support, so it vanishes: S' has rational singularities.
Since S' is a normal surface, it is CM; finite nu to smooth S is flat.
Thus V=nu_*O_S' is a vector bundle of rank e, and R1f_*O_Z=0.
Rationality gives chi(S,V)=chi(Z,O_Z)=1. No trace splitting is needed.

The logarithmic differential f*L_S→L_Z is defined because f^-1(D_S) is supported in D_Z.
It is injective (generically a characteristic-zero finite differential is an isomorphism).
Write N_f=coker(f*L_S→L_Z). It is supported on D_Z, since F is étale on U.
At a strict omitted E_i its Smith orders are (0,r_i); hence generic length r_i.
At strict C the logarithmic differential is invertible, hence length zero.
All other resolution components can contribute nonnegative generic lengths m_alpha.
Neither these lengths nor their thickenings are discarded.

Let Delta=c1(L_S)=K_S+D_S, represented by div(pi*Omega)+D_S.
Delta is supported on the pi-exceptional curves over q; it need not be effective or zero.
Projection formula and R1f_*O_Z=0 give chi(Z,f*L_S)=chi(S,L_S tensor V).
For bundles B,F of ranks b,f on a smooth surface, Riemann–Roch gives
chi(B tensor F)=f chi(B)+b chi(F)-bf chi(O)+c1(B).c1(F).
Applying it here, using chi(L_S)=0, chi(V)=chi(O_S)=1, yields
    chi(N_f)=2(e-1)-Delta.c1(V).                                    (2)
This is smooth-surface RR on S, not a Chern scaling formula for a reflexive sheaf at q.

## Explicit cusp evaluation and resolution corrections
Let I=image(rho*A→L_Z), and I0=image((h rho)*E→L_Z).
Let J_pi=coker(pi*E→L_S), C_h=I/I0, and U_rho=R1rho_*I.
The quotient J_pi is supported on the target exceptional locus, with all its scheme structure.
C_h is supported over h^-1(q): outside q, E is locally free and A=h*E.
More explicitly C_h is a quotient of rho*(A/image(h*E→A)); the latter downstairs quotient
has finite support. Pulling it back can produce entire exceptional thickenings, not just point lengths.
U_rho has finite length; no vanishing is assumed.
By evaluation and reflexivity rho_*I=A: local sections of A evaluate into I,
and any pushed section extends across the finitely many missing points of the normal W.
Thus chi(I)=chi(A)-ell(U_rho).

The common subsheaf I0 lies in both I and f*L_S inside L_Z.
Right exactness of pullback gives (f*L_S)/I0=f*J_pi; no flatness of f is assumed.
Comparing these two quotients gives exactly
    chi(L_Z/I)=chi(N_f)+chi(f*J_pi)-chi(C_h).
Since L_Z is acyclic, (1) gives the full formula
    ell(Q)+ell(T)=chi(N_f)+K_cusp,
    K_cusp:=chi(f*J_pi)-chi(C_h)-ell(U_rho).                          (3)
The name K_cusp includes the resolution term U_rho, which may also lie over other source points.
These are Euler characteristics of concrete coherent sheaves; they are not presumed positive lengths.
Using gamma_W=2-chi(A), gamma_Y=2 and (2), the finite defect is now explicit:
    epsilon_h=-Delta.c1(V)+K_cusp.                                  (4)
Thus the evaluation terms cancel in the FULL difference only after being retained on both sides.
No pullback-generation, determinant equality on resolutions, or Tor-free assumption was used.

## Exact residual estimate required by the sheet budget
Choose a product of component ideals of D_Z annihilating N_f. Multiply successively by its
individual component ideals to obtain a finite filtration N_f=N_0⊃N_1⊃...⊃N_t=0.
Each quotient F_a is a coherent sheaf on the corresponding smooth P1 component.
Let tau_a be its finite torsion subsheaf and B_a=F_a/tau_a its vector-bundle quotient.
Then chi(F_a)=rank(B_a)+deg(B_a)+ell(tau_a).
The sum of ranks on a component is exactly the generic DVR length of N_f there.
Consequently, with Theta:=sum_a[deg(B_a)+ell(tau_a)],
    chi(N_f)=sum_i r_i + sum_alpha m_alpha + Theta.                  (5)
This is an actual thickening filtration, not restriction to the reduced exceptional curves.
Its presentation depends on the chosen filtration, but the total in (5) does not.
Curve-degree terms can have either sign; no deletion of finite torsion is legitimate.

Let S_sheet=sum_i r_i delta_i, with delta_i the normalization degree in EULER1755.
Combining (3)–(5), the proposed tensor/sheet bridge is EQUIVALENT to
    sum_alpha m_alpha + Theta + Delta.c1(V)
        ≤ sum_i r_i(delta_i-1).                                    (6)
All evaluation corrections in (3) have cancelled; the exceptional intersection remains explicit.
Equation (2) also gives the exact check
    sum_i r_i + sum_alpha m_alpha + Theta + Delta.c1(V)=2(e-1).      (7)
Thus there is no hidden favorable sign obtained by moving epsilon_h across the old identity.
The provisional global sheet budget controls S_sheet, but contains no estimate of the bundle
quotient degrees, torsion lengths, or exceptional intersection appearing on the left of (6).
The reduced-curve splitting in CURVEORBIT2015 controls none of their higher thickening layers.
The controlled bound h1(G)≤s accounts only for the residue layer, not these remaining terms.
No data here proves (6); nor is (6) refuted by an actual Keller counterexample.

## Disposition and dimension-two scope
Terminal outcome: explicit residual module/formula with a new whole-source extension reduction;
the closing estimate (6) remains unproved. If it held, the provisional S_sheet≤e-1 together
with (7) would contradict e>1. Neither provisional inequality is adopted by this report.
Dimension two is essential in the reflexive/CM depth arguments, point-supported higher images,
cohomological dimension-one fibres, smooth surface RR, and filtration by rational curves.
No claim extends this argument to higher-dimensional Jacobian maps.
The LOGVOLUME1202 k-only countertest remains correctly scoped: it does not refute (6)
for an actual finite h with ample boundary. No new control family or historical test was run.

## Reading and custody
Fresh47 pins, both canonical input verifiers, eleven archives at both selection/launch blobs,
and frozen STATE315 equality with launch STATE passed before mathematical reliance.
Whole STATE315 was personally read by21:13:14 UTC; own unchanged readings were reused only after hashes.
The task was read as the individually hashed bootstrap before the full gate, then matched in that gate.
Two separately gated ROOT addenda were checked without changing the fixed47 registry.
DRAFT/INCOMPLETE was saved in secure capability-bound staging21:14:06; checked partial21:21:54.
The preliminary potential pole-twist issue was resolved by the proved full-source extension argument;
no unproved logarithmic extension statement survives in the final construction.
No external source, CAS, paid lane, child, new history query, shared-doc edit or Git mutation was used.
Detailed windows, conservative LF charge, postpins and measured custody are in companion receipts.
OPEN(S) RAISED
None: estimate (6) refines the assigned existing gap; no new lane is requested.
## COLLISIONS
The terminal scan is retained separately against this exact verified report and the frozen public basis.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12523`.
- Body SHA-256:
  `6b1fa719d404c6a022767b82f4f6eaf6cfbe15d94229c101a8b8450b6944ea2e`.
- Frozen basis: `c970400652a6b795efb8d9aff19997ec13b1a589`.
