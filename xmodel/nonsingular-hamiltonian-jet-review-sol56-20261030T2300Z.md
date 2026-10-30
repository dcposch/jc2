# Independent hostile review: fixed nonsingular Hamiltonian jet control

Status: FINAL.
Verdict: PASS.
Review/body completion UTC: 2026-10-30T22:54:59.957258+00:00
Task: nonsingular-hamiltonian-jet-review-sol56-20261030T2300Z.
Configured model: gpt-5.6-sol. Hosted identity: UNVERIFIED.
Candidate: CANDIDATE.md, SHA-256 f1a101e51b918c6c45d8ba1b64afd03630498b023f24069e4ca7d17bc6617070.
Frozen public basis: f5926b84f588e6dbac090a51d4bc84dd2b6d436f.

## Scope and custody

The pinned packet preflight returned VERIFIED_PACKET for all 14 members and verified the candidate's canonical seal. I reviewed only the copied packet. I did not open links, inspect canonical originals, query history/repositories/sources, use a secondary model, run CAS or scientific computation, generate controls, or inspect helper source. Novelty is unassessed; no outside-packet collision search was performed.

Reading accounting is exact: 1,759 non-STATE LF and 169 STATE LF, 1,928 LF total, in 86 verified body windows. Repeated input LF: 0. Own ACK/report preview LF: 0. Failed body windows: 0. Cropped-line credit: 0. Metadata, hashing, preflight, and execution-only helpers received no reading credit. The required files, including the complete 142-LF candidate and its seal, were read in full.

## Findings

### 1. Fixed nonsingular P and no polynomial mate — confirmed

At CANDIDATE.md:24-25, P=x-x^3y^5 has P_x=1-3w and P_y=-5x^3y^4, w=x^2y^5. If P_y=0, then w=0 and P_x=1, so P is nonsingular.

At lines 26-36, weights wt(x)=5 and wt(y)=-2 make P homogeneous of weight 5 and D_P raise weight by 2. Thus D_P(Q)=1 would force the weight -2 component to map to 1. Its monomials are exactly y w^k, so it is yH(w). Direct differentiation gives

    D_P(yH(w))=(1-3w)H+5w(1-w)H'.

For nonzero H of degree d, the coefficient of w^(d+1) is -(5d+3) times its leading coefficient. It cannot equal 1; H=0 also fails. Hence 1 is not in D_P(C[x,y]). No cancellation between other weights can alter this conclusion.

### 2. All-n Jacobian recurrence — confirmed

With z=w-1, lines 40-49 use

    L=(-2-3z)-5z(1+z)d/dz.

For G_n=sum a_k z^k, the z^0 coefficient is -2a_0=1. For 1<=k<=n, the coefficient is

    -(5k+2)a_k-(5k-2)a_(k-1),

which vanishes by the stated recurrence. The sole remaining coefficient is -(5n+3)a_n at z^(n+1). Every a_n is nonzero, so c_n=(5n+3)a_n is nonzero and

    {P,Q_n}=1-c_n(w-1)^(n+1)

for every n>=0. The Jacobian is therefore nonconstant, so none of these pairs is Keller.

### 3. Global nonsingularity of every Q_n, including n=0 — confirmed

At lines 55-65, b_0=1 and 0<b_k<b_(k-1). In the identity for (1-s)h_n(s), the positive coefficients following b_0 telescope to b_0. For |s|<1 their weighted absolute sum is strictly smaller than b_0, proving h_n(s) is nonzero there. Also h_n(1)>0, hence G_n(0)<0.

At lines 66-68, |c_0|=3/2 and |c_(n+1)|/|c_n|=(5n+8)/(5n+7)>1. A common zero of G_n and G_n' would force |w-1|=|c_n|^(-1/(n+1))<1, contradicting the preceding zero-free disk. For n=0, G_0=-1/2 and G_0'=0, so the common-zero assertion is vacuous and Q_0=-y/2 is plainly nonsingular.

The derivatives at lines 69-71 are correct. On x=0 or y=0, (Q_n)_y=G_n(0) is nonzero. Otherwise simultaneous gradient vanishing would force G_n'=G_n=0. Thus every Q_n is globally nonsingular.

### 4. Fixed divisorial valuation and invariants — confirmed

At lines 75-77, u=xy^3 and t=(w-1)/u^2 are birational coordinates: w=1+u^2t, x=w^3/u^5, and y=u^2/w. The u-adic valuation has source value group Z, residue field C(t), and v(x),v(y),v(w-1)=(-5,2,2).

The substitutions and volume formula at lines 82-85 are correct:

    dx wedge dy=-(w/u^2) du wedge dt,
    P=-t w^3/u^3,
    Q_n=u^2G_n(w)/w.

Therefore v(P)=-3, v(Q_n)=2, and v({P,Q_n}-1)=2(n+1). The source volume order is -2, so the defined raw log discrepancy is -1.

At lines 87-91, a=1/(PQ_n), b=P^2Q_n^3 generate the full target field because P=1/(a^3b) and Q_n=a^2b. Their values are 1 and 0, with residue(b)=-t^2/8. Since this residue is transcendental, the restricted valuation is a-adic with residue field C(-t^2/8). Hence e=1 and f=[C(t):C(t^2)]=2. No proper target subfield is being substituted.

Finally dP wedge dQ_n=-(a^-2 b^-1) da wedge db, as in lines 92-96. Its a-order is -2, giving target raw log discrepancy -1. These conclusions hold for the same source valuation for every n.

### 5. Full graded rings and bracket — confirmed with the stated distinction

At lines 100-105, r=in_v(u), r^-1=in_v(xy^2), and s=in_v(x^2y^4(w-1)) generate

    gr_v C[x,y]=C[r,r^-1,s].

Indeed each polynomial has a u-expansion whose first coefficient is polynomial in t, while the displayed polynomial representatives supply r, r^-1, and s in the reverse inclusion. From the volume form, the ambient graded bracket has degree +1 and {r,s}=-r^2. Since r is a unit, this Laurent polynomial ring is smooth and symplectic.

At lines 109-115, p=-sr^-3 and q=-r^2/2 are algebraically independent. Weighted leading parts of a nonzero polynomial in P,Q_n therefore cannot cancel identically, so gr_v A_n=C[p,q]. Direct restriction of the ambient graded bracket gives {p,q}=1. This is a smooth symplectic polynomial ring, independent of n in the stated presentation.

The terminology at lines 115-116 is accurate: this is the restriction of the ambient graded bracket, not a bracket induced from a Poisson-closed filtered A_n.

### 6. Filtered nonclosure for every n — confirmed

At lines 117-120, fix q_0 nonzero. The point x=0, y=q_0/G_n(0) maps to (P,Q_n)=(0,q_0) and has Jacobian G_n(0)<0. A point with w=1, y=-2q_0, and x^2y^5=1 has the same image and Jacobian 1. Such an x exists because y is nonzero. Thus {P,Q_n} cannot be a polynomial in P,Q_n, so A_n is not closed under the ambient Poisson bracket for any n, including n=0.

### 7. Valuation-topology nonclosure and limits — confirmed

Equation (1) gives elements D_P(Q_n) converging to 1 because the differences have valuation 2(n+1), while the signed-weight argument proves 1 is absent from D_P(R). Hence D_P(R) is not closed in the stated linear valuation topology. The report correctly does not call this topology ideal-adic.

No failed implication or material arithmetic error was found. The candidate consistently limits the result to growing-degree non-Keller controls at one valuation. It proves no fixed-degree bound, full filtered compatibility, polynomial no-fold theorem, actual Keller example, or JC2 conclusion. The retained runtime sanity checks were not inspected and are unnecessary for this self-contained all-n audit. No external mathematical foundation remains unaudited beyond standard elementary polynomial, valuation, residue-field, and associated-graded facts used explicitly above.

## Verdict

PASS at the candidate's exact stated scope. This review makes no theorem promotion and no novelty claim.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6868`.
- Body SHA-256:
  `21904025bc3844c52554332c5d98cd170467622e4101453994733a7a6d5de2ba`.
- Frozen basis: `f5926b84f588e6dbac090a51d4bc84dd2b6d436f`.
