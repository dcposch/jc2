# Q2: exact faces and global primitive obstruction (frozen inputs only)

Source custody: root mechanically verified all hashes. I read only charged frozen packet, own-data/census-coverage/residual65 reports, roster, FALLACY, and Moh PDF (text layer), with no other ideation input, ledger, jc2-lean or artifact trees. Computations below used in-memory SymPy exact rationals; this is the sole written note.

## Facts from the frozen rows

`roster.jsonl:9`: R009 source `(192,128)`, M=(-128,148,190), d=(192,64,4,2), V=(2,3), radii=(19/24,5/16,-1), u=1,v=3. Child `(n',m',M'_last,ell)=(48,32,37,1)`, d_support=1/5, K=16, e:q=3:2; 388 coordinates (without saturation T), 600 coefficient rows. Alpha dimensions 37+88+138=263, h37, beta87, c1.

`roster.jsonl:50`: R050 source `(196,56)`, M=(-56,184,194), d=(196,28,4,2), V=(4,3), radii=(19/28,1/4,-1), u=1,v=3. Child `(49,14,46,1)`, d_support=1, K=7, e:q=7:2; 1392 coordinates, 1953 coefficient rows. Alpha dimensions 35+84+133+182+231+280+328=1273, h35, beta83, c1.

The integral support grading is w(x,y)=(5,1) for R009, with w(P,Q)=(48,32), and (1,1) for R050 with (49,14). Since J(P,Q)=c x, the distinguished c has weights 48+32-5-1-5=69 and 49+14-1-1-1=60. These are coefficient defect weights, different from local face gradings.

`residual65-structure-fable5-20260905.md:250,255-259` reports both Xu margins zero. `census-coverage-gate-opus5-20260905.md:267-291` supplies the inequality chain and explicitly leaves its major upper-bound link un-rederived. Thus equality can force every separately nonnegative slack to vanish ONLY after that major bound is licensed and all relevant refinements are enumerated. No floor-attainment assertion follows merely from the roster.

## Complete tiny top-face ODE calculation: four witnesses, zero kills

Moh p.171 proof of Proposition 4.6, equation (6) and following reduction through A.3/A.4, is the required r>=2 licence; p.170's final ODE statement alone concerns r=1. Moh p.205 Proposition A.3 gives the reduced equation

    N p(z) q'(z) - M p'(z) q(z) = kappa p(z), kappa != 0.

Here q' denotes derivative. The arithmetic GO condition only retains multiplicities, squarefreeness, root containment and a heavy root; it does not solve this coefficient equation (`residual65...:136-148`). For a monic p with an A-orbit symmetry, Reynolds-project any q to q=zS(z^A); the equation is preserved. For these rows deg q is 1 mod A, so its nonzero leading coefficient is preserved. Kernel uniqueness also holds: homogeneous q is proportional to p^(M/N), impossible polynomial for the listed multiplicities. Normalize chosen nonzero center a=1 and kappa=1; this is a field extension plus invertible scalar normalization, never a zero-center deletion.

R009: N=V3*d2/d3=48, M=V3*(n-M2)/d3=33, A=16, selected multiplicity V2=2. Degree and orbit congruence leave exactly two patterns, writing T=z^16:

    p=z^16(T-1)^2;        q= -z(T-1)(8T-3)/1440.
    p=(T-1)^2(T-6/5);     q=  z(T-1)(5T-6)/288.

R050: N=21, M=9, A=4, selected multiplicity 4. Exactly two patterns, T=z^4:

    p=z^5(T-1)^4;         q= -z(T-1)(7T-5)/120.
    p=z(T-1)^4(T-5/4);    q=  z(T-1)(4T-5)/60.

All four polynomial identities checked by expansion over Q, with residual identically zero, correct degree q, squarefree q and root containment. For the second pattern before fixing the extra center b, lex elimination gives factors b(b-1)^2(5b-6) and b(b-1)^2(4b-5), respectively; localizing b(b-1) proves b=6/5 or 5/4. The first pattern solutions are unique. Thus proposed face-only nilpotence of kappa is REFUTED by exact witnesses. In local coefficient grading w(z)=1, w(kappa)=M-1=32 or8. These are not the full-chart Jacobian c nor its weights69/60. Cheap positive control for a future gluing solver; actual runtime <1 second total, no disk artifacts.

Bottom ODE also has exact witnesses. Moh p.170 final statement at r=1: D(n,-M1,g_sigma,T1_sigma)=constant. With proportional degrees reduced, R009 N=6,M=4,A=3, R050 N=28,M=8,A=7. Normalize T=z^A and lower-degree face H=z(T-1). Then

    R009 F=T^2-(3/2)T+3/8; D(6,4,F,H)=-9/4.
    R050 F=T^4-(7/2)T^3+(35/8)T^2-(35/16)T+35/128;
          D(28,8,F,H)=-245/32.

Both checked exactly. They are necessary local face witnesses, not pairs or global gluing witnesses. The next lane must impose shared actual coefficients between these faces and the other place, not repeat isolated ODE tests.

## Chart reduction and invariant proposal

Fix smaller Q=h^q+beta tails and h. Write P=h^e+sum alpha_i h^(e-i). Differentiation is linear in the alpha coefficients, so the full exact equation is

    A(h,beta) alpha + r(h,beta) = c e_ell.

Eliminate alpha comprehensively: for every pivot rank chart invert the declared nonzero minors, perform exact row operations, retain all left-kernel compatibility equations, and recurse on vanished pivots. Generic rank alone never covers the chart. This removes263/1273 coordinates, leaving125/119 (including c). Run radicals/saturation only after extracting the ideal and checking the declared ring. This matches the root's main proposal.

Both q=2 cases admit a simpler base: every monic Q of the supported weighted degree has a unique monic approximate square root h with deg_y(Q-h^2)<K. Recursive coefficient comparison gives a polynomial bijection over Q (denominators powers2), preserving support. Thus replace (h,beta) by Q coefficients before forming differential matrices. R009 triangle5b+a<=32 has126 monomials; delete monic leader and constant gauge ->124=37+87. R050 triangleb+a<=14 has120; delete two ->118=35+83. This does not lower dimension; it avoids nested expansion. Symmetry gauges alone cannot credibly promise <70.

Uniform non-inherited necessary condition: on a geometrically integral generic fiber C_tau:Q=tau over k(tau), k algebraically closed characteristic0, monic Q in y and c!=0,

    dP = c x^ell dx/Q_y.

Therefore omega=x^ell dx/Q_y has zero class in Omega(k(tau)(C_tau))/d k(tau)(C_tau), with a primitive belonging to the actual P support. Residue zero is merely its cheapest necessary part. In rational-function Hermite reduction, retain the full reduced differential class and support bounds. A nonzero reduced class on every possible Q base chart forces c nilpotent; a rational primitive refutes that particular de Rham obstruction but is not yet an admissible P. In char0 a rational primitive of a differential regular on the affine smooth curve has no finite poles and is regular there; dependence on tau and the prescribed P support remain genuine extra conditions.

This identity follows directly by differentiating Q=tau and uses the printed monomial Jacobian in Moh Proposition6.3(3), pp.197-198, plus the roster support. It is not the descent-invariant lattice shadow: it couples the complete Q and all physical places simultaneously. Price: 2h derive support-aware Hermite matrix for R009, 2h exact rank compatibility on small strata; cap2GB RAM and30MB notes, no flat Groebner job. Refutation: exact admissible Q with nonzero c and zero reduced class, followed by testing the support-linear equations; no count change until the full necessary-chart cover is checked.

## Conditional global divisor/Riemann-Hurwitz alternative

Under the same hypotheses and geometrically integral generic C_tau, its affine part is smooth: J!=0 away from x=0, while Q(0,y)-tau has simple roots generically. There are m'=deg_yQ transversal x=0 points, and dP has exactly ell*m' finite zero order. On the smooth projective normalization let D=degree(P), E=the set of infinity PLACES and e_v(P) the ramification index (at a finite image use ord_v(P-P(v))). Then

    2g-2 = -2D + ell*m' + sum_{v in E}(e_v(P)-1).

If P has a pole at every infinity place, this simplifies to

    D = ell*m' + 2 - 2g - |E|.

For R009/R050 ell1, D<=34-|E| and D<=16-|E|. These do not currently contradict any roster row. Do not set |E|=2 merely because there are two points at infinity, or D=n'm'. Compute actual Puiseux branches, pole orders, finite-image ramification, and genus. Generic geometric integrality needs its own proof or componentwise treatment. The divisor-degree/Riemann-Hurwitz theorem is not printed in the charged packet; label this PROPOSED LEMMA with exact hypotheses, to prove directly or source-charge next round. Budget2-4h, output a finite valuation table with each branch's provenance; a nonnegative genus satisfying the equation is an explicit failure of this obstruction. Abhyankar-Moh cannot be invoked from two points at infinity: the usual line-embedding hypothesis A1 normalization and polynomial parametrization is missing.

## Addendum: remove h from P too; matrix and free gauges

For fixed monic supported h, repeated Euclidean division by h expresses EVERY monic supported P uniquely as h^e+sum alpha_i h^(e-i), deg_y alpha_i<K. Weighted bounds persist under each division. The constant gauge is a triangular correction in alpha_e. Thus P's263/1273 alpha coordinates are exactly arbitrary triangle coefficients (excluding monic leader/constant): R0095b+a<=48 has265 monomials; R050b+a<=49 has1275. Combined with the Q square-root bijection, the receiver is a direct weighted polynomial-pair chart, with no h expansions required.

For P monomial x^i y^j and Q monomial x^u y^v, matrix entry coefficient is i*v-j*u at output x^(i+u-1)y^(j+v-1), times the relevant Q coordinate. Entries are LINEAR in Q. Output row triangle5b+a<=74 has600 monomials; ordinary triangleb+a<=61 has1953. These exactly match the roster emitted coefficient-row counts.

Structural kernel: adding lambda Q to P preserves J and degree/support in R009; adding lambda1 Q+lambda2 Q^2+lambda3 Q^3 does so for R050. Monicity permits unit triangular gauges P[y^32]=0 and P[y^14]=P[y^28]=P[y^42]=0. This removes1/3 free variables or identifies an A^1/A^3 factor; rank analysis must not falsely assume full263/1273 column rank. This is a receiver-chart gauge, not a claim preserving every original marked tower datum.

Actual top-face gluing can be added before the linear system. Using the inversion multiplicity formula at `residual65...:209-217`, R009 has W0=16-5*sum(r)=6 or1, and each parent orbit becomes five child roots. Its leading H16 is y^6(y^5-a*x)^2 or y(y^5-a*x)^2(y^5-(6/5)*a*x). R050 has W0=7-sum(r)=3 or2 and one child root per orbit: H7=y^3(y-a*x)^4 or y^2(y-a*x)^4(y-(5/4)*a*x). In both cases a!=0; Qtop=H^2, Ptop=H^3/H^7. Ratio transport follows directly: for source y~r*t^(A/B), gamma=y^-1 and child pi~-b_source*r^(B/A)*gamma^(B/A-v). Here B/A>v, so omitted terms are lower. The A-th power of the child coefficient is (-b_source)^A*r^B, hence the same common unit multiplies all orbit centers. It preserves ratios6/5 and5/4.

With ratio fixed these faces have one scale parameter. R009 Q's boundary has6 free coefficients, reduced to1; R050 has14, reduced to1. Q-base counts including c become120/106, or119/105 after x->x/a normalizes the nonzero scale and rescales c by a unit. Also fixes9/49 leading P coefficients. This still exceeds70 and is not a promised full elimination. It converts the source-face witnesses into explicit gluing restrictions with the second-place receiver.
