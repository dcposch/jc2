# Hostile review: all-degree linear-U submersions on the exact pseudo-plane

INTERNAL / DIFFERENT-MODEL HOSTILE REVIEW / MANUAL MATHEMATICS ONLY.
Reviewer: Fable 5.1 (claude-fable-5-1), 2026-09-11. Lane inputs frozen at
`/tmp/jc2-lane.y7sd28/inputs`. First action 08:27:49 UTC: both owned targets
absent, all four input hashes matched the charged pins before any body was
read. Reserve 08:39 UTC / HARD 08:42 UTC, never reset. No subprocess, CAS,
code, network, git, or process control was used; every identity below was
recomputed by hand from the four frozen inputs only. No linked report,
ledger or history was opened. PP-HOM-1 (a homogeneous H in this exact
characteristic-zero ring has no regular G with nonzero scalar bracket) is
imported from the parent Fable report at exactly its stated scope and is not
re-proved here.

## 0. Inputs and custody

```
86741d44fb280d0e0498bae7fb18ce01505b2d75814f50ce3f14aaf507b0f3bd  pseudoplane-linear-u-submersions-astra-20260911.md
29298c37d2f1b4f487fbaa624069ea2dee5fa0b0fd52a001da08a22f87df02aa  pseudoplane-linear-u-submersions-astra-20260911.md.artifact.json
e042b696f3dce19fe116fddc4fed328bb066dee86ef539fd2f13f9055a0f87b7  pseudoplane-homogeneous-gate-fable5-20260911.md
347b7e38435237c8e2ca77d830bdac82ae2d702898c50786b928bbf2adc1b9ad  pseudoplane-homogeneous-gate-fable5-20260911.run.v2
```
Administrative check: the first 10042 bytes of the Astra report end at its
unique standalone body-end line, newline included, and hash to
`4fc13293aa49b8c4444c4624c2d892ce837441500c76870ab19d15e765baf8fd`, the
body SHA-256 recorded in both its Seal and the artifact JSON. The run.v2
records the parent report hash `e042b6...` equal to the frozen parent file,
report_state BODY_SEALED, seal_boundary CLEAN. Detail in
`box/pseudoplane-linear-u-gate-fable5-20260911/input_custody.md`.

## 1. Overall verdict

All six verdicts are CONFIRMED. The candidate theorem holds exactly as
stated: over an algebraically closed characteristic-zero k, H=P(Z)+UQ(Z)
with P,Q in k[Z] of arbitrary degree is everywhere submersive on
Spec R, R=k[A,U,Z]/(U^2-A-A^2Z), if and only if H=aU+b or H=aZ+b with a
nonzero; and, composed with the accepted PP-HOM-1, no such H has any
regular G in R with {H,G} a nonzero scalar, in either order, over every
characteristic-zero field. No step of Sections 1-5 is refuted, no gap in
truth was found, and no silent repair is needed. Collateral notes, none
changing the mathematics: (i) Section 2's phrase "no division by a
potentially vanishing quantity" also relies on z nonzero for Q(z)/(2z),
which the chart states; (ii) Section 3's "every irreducible divisor of F
divides T" is correct because a prime dividing cT^(2m) divides T; (iii)
"ramification curve" in Section 5 is a label for the locus Phi_A=0, on
which nothing depends. The theorem is a manual candidate, not a
computational replay, not an all-source, all-R, mixed-H or JC2 claim.

## 2. Verdict A: smoothness, cotangent nondegeneracy, generator brackets

**CONFIRMED.** Smoothness: Phi_A=-1-2AZ, Phi_U=2U, Phi_Z=-A^2. A common
zero needs A=0 from Phi_Z, then Phi_A=-1. So the surface is smooth and
dPhi is nowhere zero on it. Bracket structure, recomputed: the matrix
Pi=({x_i,x_j}) is
```
[ 0      2A^2    4U     ]
[ -2A^2  0       2+4AZ  ]
[ -4U   -(2+4AZ) 0      ]
```
and Pi.(Phi_A,Phi_U,Phi_Z)^T has rows 4A^2U-4A^2U, 2A^2+4A^3Z-2A^2-4A^3Z,
4U+8AUZ-4U-8AUZ, all zero; so dPhi is in the kernel. Pi is nonzero at every
surface point (A=0 forces the entry 2+4AZ=2), and a nonzero 3x3
alternating matrix has rank 2 with one-dimensional kernel, so the kernel is
exactly the span of dPhi. Hence {a,b}(p)=Pi_p(da,db) descends to the
surface cotangent space T*_p(ambient)/span(dPhi_p), where it is a rank-2
alternating form on a 2-dimensional space, i.e. nondegenerate. Therefore
dH_p=0 on the surface iff Pi_p(dH,eta)=0 for all eta iff
{H,A}(p)={H,U}(p)={H,Z}(p)=0, since dA,dU,dZ span the ambient cotangent
space. This equivalence holds at every point including A=0 and Z=0; no
localization is used. The parent report's identity bracket=-2 det
d(a,b,Phi)/d(A,U,Z) is reconfirmed: {A,U}=-2Phi_Z=2A^2,
{A,Z}=-2(-Phi_U)=4U, {U,Z}=-2Phi_A=2+4AZ.

Generator brackets by Leibniz with H=P(Z)+UQ(Z):
```
{H,A} = P'{Z,A} + Q{U,A} + UQ'{Z,A} = -4UP' - 2A^2Q - 4U^2Q' = -4U(P'+UQ') - 2A^2Q
{H,U} = (P'+UQ'){Z,U}                = -(2+4AZ)(P'+UQ')
{H,Z} = Q{U,Z}                        = (2+4AZ)Q
```
All three match the report exactly. Submersive at p means dH_p is
surjective onto T_{H(p)}A^1, i.e. nonzero, for a morphism of smooth
varieties; the vanishing locus of the three brackets is closed, so over
algebraically closed k it is empty iff it has no k-point. Attack tried:
whether the criterion silently needs Q or 2+4AZ to be a unit; it does not,
because it is a statement about a bivector on the whole smooth surface.
No correction.

## 3. Verdict B: critical curve and the discriminator E

**CONFIRMED.** The locus 2+4AZ=0 on the surface: A nonzero, Z=-1/(2A),
U^2=A+A^2Z=A-A/2=A/2, so A=2U^2, Z=-1/(4U^2); with U=v this is exactly the
family p_v=(2v^2,v,-1/(4v^2)), v in k*, and v=0 is impossible. Check:
U^2=v^2 and A+A^2Z=2v^2-4v^4/(4v^2)=v^2; 2+4AZ=2-2=0. There {H,U}={H,Z}=0
automatically and
```
{H,A}(p_v) = -4vP'(z) - 4v^2Q'(z) - 8v^4Q(z),   z=-1/(4v^2).
```
The report's form -4v[P'(z)+v(Q'(z)-Q(z)/(2z))] expands to
-4vP'-4v^2Q'+2v^2Q/z and 1/z=-4v^2 gives 2v^2Q/z=-8v^4Q; equal. With
D=2ZQ'-Q this is -4v[P'(z)+vD(z)/(2z)], so criticality at p_v (v nonzero)
is exactly 2zP'(z)+vD(z)=0.

Discriminator E(Z)=16Z^3P'(Z)^2+D(Z)^2, z in k*, v^2=-1/(4z), the two
lifts v and -v distinct since char is not 2. Case D(z)=0: critical iff
P'(z)=0 (either lift), and E(z)=16z^3P'(z)^2=0 iff P'(z)=0 since z is
nonzero. Case D(z) nonzero: critical at p_v iff v=-2zP'(z)/D(z); this v
satisfies v^2=-1/(4z) iff 4z^2P'^2/D^2=-1/(4z) iff 16z^3P'^2=-D^2 iff
E(z)=0. Conversely E(z)=0 with D(z) nonzero forces P'(z) nonzero, so
v=-2zP'/D is nonzero, squares to -1/(4z), and p_v is critical. Subcase
P'(z)=0, D(z) nonzero: E(z)=D(z)^2 nonzero and criticality would need
vD(z)=0, impossible; consistent. So for z in k*: E(z)=0 iff at least one
lift is critical. E identically zero: then E(1)=0 with z=1 in k*, so a
critical point exists, contradicting submersivity; independently, E=0
would force P'=0=D by odd/even degree comparison, i.e. H constant. Nonzero
constant E: no root at all, no critical point on the curve; it is the
m=0 case of E=cZ^m, handled in C. E nonconstant with no nonzero root over
algebraically closed k: E=cZ^m, c nonzero, m>=1. Attack tried: critical
points off the curve; there 2+4AZ is nonzero, so Q(z)=0 and
P'(z)+uQ'(z)=0, and {H,A} vanishes automatically. The proof never needs
to enumerate these: it uses only the two loci (curve, boundary line) to
derive necessary conditions, then proves the converse directly. No
correction.

## 4. Verdict C: reflected-factor parity and D=0 implies Q=0

**CONFIRMED.** With iota^2=-1 and F(T)=D(T^2)+4 iota T^3P'(T^2):
F(T)F(-T)=D(T^2)^2-16 iota^2 T^6P'(T^2)^2=D(T^2)^2+16T^6P'(T^2)^2=E(T^2)
=cT^(2m), all degrees of P,Q simultaneously. Both factors are nonzero
since the product is. k[T] is a UFD and T is prime, so every prime divisor
of F divides cT^(2m), hence T; thus F=alpha T^n, alpha nonzero, and
F(-T)=alpha(-1)^nT^n, so alpha^2(-1)^nT^(2n)=cT^(2m) gives n=m. This
includes m=0: F=alpha, n=0. n even: F(T)-F(-T)=8 iota T^3P'(T^2)=0 in the
domain k[T], so P'(T^2)=0 and, Z->T^2 being injective on k[Z], P'=0
(uses 8 iota nonzero, char not 2). n odd: F(T)+F(-T)=2D(T^2)=0, so D=0.
Coefficientwise, Q=sum q_jZ^j gives 2ZQ'=sum 2jq_jZ^j and
D=sum(2j-1)q_jZ^j; in characteristic zero every odd integer 2j-1 is
nonzero, so D=0 forces every q_j=0, Q=0. No finite-degree cap, no source
coefficients, no specialization; T is a fresh indeterminate. Attack tried
(and it fires, see Section 8): in characteristic p odd, j=(p+1)/2 gives
2j-1=p=0 and Q=Z^((p+1)/2) has D=0 with Q nonzero, so this is exactly
where characteristic zero is consumed. Also checked: n even leaves
D=alpha Z^(n/2), so Q may be nonzero (e.g. Q=Z, D=Z, E=Z^2), which is why
the boundary line in D is indispensable; n odd leaves
P'=(alpha/4 iota)Z^((n-3)/2), n>=3. No correction.

## 5. Verdict D: boundary line, constants, converse

**CONFIRMED.** L={(0,0,z)}: Phi(0,0,z)=0 for every z, and
dPhi=(-1-2AZ)dA+2UdU-A^2dZ restricts to -dA there, so dU,dZ is a basis
of the surface cotangent space. Ambient dH=QdU+(P'+UQ')dZ, hence
dH|_(0,0,z)=Q(z)dU+P'(z)dZ, zero iff Q(z)=0=P'(z). All z in k including
z=0 are covered; the chart's exclusion of z=0 is thereby repaired. If
P'=0 then P=b is constant (characteristic zero: jZ^(j-1) has j nonzero).
Submersivity on L needs Q(z) nonzero for every z; over algebraically
closed k a polynomial with no root is a nonzero constant, and Q=0 is
excluded by the same condition, so Q=a in k*, H=aU+b. If Q=0 then P'(z)
nonzero for every z gives P'=a in k*, P=aZ+b. Constants (P'=0 and Q=0)
have dH=0 identically and fail both branches. Converse: {U,A}=-2A^2 and
{U,Z}=2+4AZ vanish together only if A=0 and 2=0, impossible, so U is
everywhere submersive. {Z,A}=-4U and {Z,U}=-(2+4AZ) vanish together only
if U=0 and 1+2AZ=0; on the surface U=0 gives A(1+AZ)=0, and A=0 gives
1+2AZ=1 while A nonzero gives AZ=-1 and 1+2AZ=-1; so Z is everywhere
submersive. d(aH+b)=a dH preserves the property for a nonzero. Both
directions of the classification are proved. Attack tried: H=UZ passes
the chart (E=Z^2) and dies at (0,0,0), H=U+Z dies on the curve at
16z^3=-1 with v=2z (direct check: -4v-8v^4=-8z-128z^4=-8z+8z=0). No
correction.

## 6. Verdict E: scalar bracket, unrestricted mate, field scope

**CONFIRMED.** If {H,G}=c nonzero with G in R, then at any k-point p
with dH_p=0 on the surface, H-H(p) lies in m_p^2 (p smooth), so Leibniz
puts {H,G} in m_p and {H,G}(p)=0, not c; equivalently
{H,G}(p)=Pi_p(dH_p,dG_p)=0. This uses G regular at p; a localized G would
break it at its poles, and the parent's countercontrol {A,U/(2A^2)}=1 in
R[A^-1] is exactly such a case (A is not in the envelope and dA_o=0). So
H is everywhere submersive and by D equals aU+b or aZ+b. Then
{aU+b,G}=a{U,G}=c gives {U,G}=c/a nonzero, and likewise {Z,G}=c/a; the
constant b is removed by {b,G}=0, not by a false homogeneity claim. U and
Z are homogeneous of weights 1 and -2 for wt(A,U,Z)=(2,1,-2), the parent's
exact grading; PP-HOM-1 ("homogeneous H in R, any G in R, {H,G} not a
nonzero scalar") applies verbatim, G arbitrary. Other order: {G,H}=c gives
{H,G}=-c, again a nonzero scalar. Field scope: for K of characteristic
zero, base change R_K to R_Kbar preserves the identity {H,G}=c and c stays
nonzero, so the algebraically closed proof applies; the normal form
R=K[A,Z] (+) U K[A,Z] is compatible with base change and K[Z]->Kbar[Z] is
injective, so P=b, Q=a (or P=aZ+b, Q=0) already have a,b in K. PP-HOM-1
is stated by the parent over every characteristic-zero field. The report
correctly refuses to replace geometric submersivity by K-rational-point
submersivity (e.g. Q=Z^2+1 over Q has no rational root). No positive
characteristic claim is made, and Section 8 shows none could be. No
correction.

## 7. Verdict F: nonlinear control and scope firewall

**CONFIRMED.** H=Z^2+U/4: P'=2Z, Q=1/4, D=-1/4, E=64Z^5+1/16, and
E(-1/4)=64(-1/1024)+1/16=0. z=-1/4 gives v^2=1, v=-2zP'/D=1, point
p_1=(2,1,-1/4): U^2=1=2+4(-1/4). dPhi=(Phi_A,Phi_U,Phi_Z)=(-1+1,2,-4)
=(0,2,-4); dH=(0,1/4,2z)=(0,1/4,-1/2)=(1/8)dPhi, so dH is zero on the
surface. Bracket check: {H,A}=-4(1)(-1/2)-2(4)(1/4)=2-2=0, and the other
two carry the factor 2+4AZ=0. On L, dH=(1/4)dU+2zdZ is never zero, so the
boundary test alone does not suffice and the curve is doing real work;
the sign of E is confirmed. Scope firewall: the report asserts nothing for
P(A,Z)+UQ(A,Z), for an added A S(Z), for arbitrary mixed H, for arbitrary
R, for all-source coverage or for JC2; it makes no novelty or frontier
claim; its history remark is explicitly non-exhaustive. The stopped
affine-linear A,U,Z task is not reopened here and I do not reopen it.
PP-HOM-1 is consumed only after the classification, as stated. No
correction.

## 8. Negative control, QUANTITY, CHEAPEST TEST, planning wall

**Negative control (own, meaningful, hypothesis mutation).** Drop
characteristic zero: k algebraically closed of characteristic 3,
H=Z+UZ^2 (P=Z, Q=Z^2). Then D=4Z^2-Z^2=3Z^2=0 with Q nonzero, so C's
coefficient step fails. Direct check that H is everywhere submersive:
{H,Z}=(2+AZ)Z^2 and {H,U}=-(2+AZ)(1+2UZ) (4=1 in char 3). Off the curve
2+AZ=0 both vanish only if Z=0, and then 1+2UZ=1. On the curve AZ=1,
U^2=2A, and {H,A}=-U(1+2UZ)-2A^2Z^2=-U-4U^2Z-2=-U-4(2A)(1/A)-2=-U-10=-U,
zero only at U=0, forcing A=0, contradicting AZ=1. So H is everywhere
submersive in characteristic 3 but is neither aU+b nor aZ+b: the
classification is FALSE there, and every other step (A, B, D, the parity
in C up to D=0) is characteristic-free away from 2. The control fires
exactly at the step where the report consumes characteristic zero.

**Remaining QUANTITY.** Whether every everywhere-submersive regular H in
R, with A allowed in P and Q, is an affine function of U or of Z. The
theorem is silent there and so am I; this is a question, not an
assignment, and it does not reopen the stopped affine-linear task.

**CHEAPEST TEST.** A static desk replay of the char-3 control above and of
the U+Z and UZ attacks in D by a third reader, reading nothing new.
Planning wall: approximately 10 minutes UNMEASURED manual time, no
subprocess, not run here. No charge_basis line: no exit-price assertion
is made. No new canonical OPEN identifier is needed.

## 9. Post-pins, readback, COLLISIONS

Post-pins measured 08:33:39 UTC, after sections 0-8 were written and
before this section:
```
86741d44fb280d0e0498bae7fb18ce01505b2d75814f50ce3f14aaf507b0f3bd  pseudoplane-linear-u-submersions-astra-20260911.md
29298c37d2f1b4f487fbaa624069ea2dee5fa0b0fd52a001da08a22f87df02aa  pseudoplane-linear-u-submersions-astra-20260911.md.artifact.json
e042b696f3dce19fe116fddc4fed328bb066dee86ef539fd2f13f9055a0f87b7  pseudoplane-homogeneous-gate-fable5-20260911.md
347b7e38435237c8e2ca77d830bdac82ae2d702898c50786b928bbf2adc1b9ad  pseudoplane-homogeneous-gate-fable5-20260911.run.v2
```
Identical to the pre-pins of 08:27:49 UTC; the input directory is
unchanged. Custody detail, the administrative body cross-check and the
whole-read record are in
`box/pseudoplane-linear-u-gate-fable5-20260911/input_custody.md`.

Own whole readback: both owned files were read back whole by cat after
this section was written and before the marker was appended; the marker
was appended only after that readback showed no placeholder and no stray
marker. Timing: skeleton 08:31:51 UTC, verdicts A-C 08:32:53, verdicts
D-F and section 8 08:33:27, post-pins 08:33:39, all inside the 08:39
reserve. Sections 2-4 and 5-8 were written by two apply_patch calls on
disjoint hunks; the section list was verified afterwards (ten headings,
all filled). No process control was exercised by this lane; TERM/KILL
arming belongs to the adapter.

COLLISIONS (own-only): none. Both owned targets were absent at 08:27:49
UTC; nothing outside the two owned paths was created or modified. No
Seal, charge_basis, or artifact transaction was authored. No exit-price
assertion is made, so no charge_basis line is declared. No new canonical
OPEN id and no follow-on lane, second task or dependent lane is
requested.

Final write: the marker append after readback, inside the 08:39 reserve.
ALL WRITERS IDLE after that line; the adapter seals.

<!-- BODY-END -->
