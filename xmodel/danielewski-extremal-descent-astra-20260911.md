# Two-sided extremal descent: exact gap and full-row control

Owner /root/contact_collision_geometry. Actual first action 2026-09-11 16:34:03 UTC. Original publication reserve 16:47 UTC / HARD 16:50 UTC, unchanged. MANUAL / UNREVIEWED; no scientific execution.

Exactly three scientific inputs were pinned before their fresh WHOLE reads: ROOT TASK, the completed two-chart interface and the completed finite-jet countercontrol. Their exact pins are in PINS.json. All formulas used below are independently derived; no linked provenance, live report or other source was read. The prior finite-jet family is not recycled as a new discriminator.

## Verdict and unrestricted scope

NO_DESCENT / GAP. No strictly decreasing invariant for EVERY stipulated regular scalar pair is proved. The report isolates a sufficient two-ended shear criterion and the first missing implication: the complete scalar identity would have to force a suitable polynomial-power relation at an end, with an opposite-end growth bound, or supply another reduction. Commuting extremes and even the EXACT weight-zero scalar block do not force this.

The explicit control below is a genuine globally regular TWO-SIDED pair, with commuting top and bottom terms and weight-zero bracket block exactly 1. Its natural interval-width invariant is already minimal under affine target changes and cannot decrease by a polynomial shear. Crucially, another bracket block is nonzero: this is NOT a scalar pair and does NOT refute a theorem that uses every full-bracket equation. No surface exclusion, regular scalar pair or JC2 conclusion is claimed.

## 1. Endpoint arithmetic and the conditional shear criterion

On T=Spec C[x,t,Z]/(t^2-1-x^2Z), put s=t^2-1. On x invertible, Z=x^-2*s and the symplectic form is dx wedge dt/x^2, so

    {x^m p(t),x^n q(t)}=x^(m+n+1)*(m*p*q'-n*p'*q).

For negative m, regularity of x^m p requires divisibility by s^ceil(-m/2). Indeed substituting t=1+x^2y or t=-1+x^2v forces the respective root multiplicity; different Laurent blocks cannot cancel a fixed pair of x- and y-exponents. The two coprime root factors give the stated criterion.

For a nonzero finite-support F define lo(F),hi(F) to be its least and greatest Laurent weights. Assume the genuinely two-sided case

    lo(H)=a<0<A=hi(H),   lo(G)=b<0<B=hi(G).

The candidate positive integer is

    N(H,G)=(A-a)+(B-b).

Since the extreme bracket weights A+B+1 and a+b+1 are nonzero, a scalar pair must satisfy

    A*p_A*q_B'-B*p_A'*q_B=0,
    a*p_a*q_b'-b*p_a'*q_b=0.                                 (1)

For A=d*alpha,B=d*beta with alpha,beta positive coprime, the first relation implies p_A=c*R^alpha and q_B=e*R^beta for some polynomial R and nonzero constants c,e. Proof: the logarithmic derivative gives p_A^beta/q_B^alpha constant in C(t), and unique factorization compares each root multiplicity. This includes constant R. The same argument applies to -a,-b. At the negative end the common generator x^-d*S(t) is itself regular: if S^alpha is divisible by s^ceil(d*alpha/2), integer root multiplicity forces ord_(±1)S>=ceil(d/2).

These are power relations, not divisibility of alpha or beta by the other. Coprime exponents such as 2 and 3 are permitted by (1).

A precise sufficient upper-end reduction is: B=k*A for an integer k>=1, G_B=c*(H_A)^k, and k*a>=b. Then replacing G by G-c*H^k strictly lowers hi(G), does not lower lo(G), and therefore strictly decreases N unless the process already reaches the stopping case of a one-sided coordinate. All functions remain regular, and the FULL bracket is preserved. A symmetric lower-end criterion is b=k*a, G_b=c*(H_a)^k and k*A<=B. Exchange H,G as needed.

When the opposite-end inequality fails, the same shear introduces the exact endpoint k*a<b (or k*A>B); a decrease of N no longer follows. Thus two independent facts are missing from leading commutation: an integral-power cancellation available to a polynomial target shear, and a bound preventing its opposite-end growth. No other invariant is silently asserted to solve either issue.

## 2. A two-sided control with the ENTIRE scalar-weight block

The following are actual regular polynomials on T:

    R=x+Z,   L=x+(3/2)Z,   M=t(x+2Z),
    H=R^2+L,             G=R^3+M.                             (2)

Their endpoint data are

    H: [-4,2],  bottom Z^2, top x^2, width 6;
    G: [-6,3],  bottom Z^3, top x^3, width 9.

Thus both ends commute, with the same coprime powers 2 and 3. Both coordinates are genuinely two-sided. From the relation and form one directly derives {x,t}=x^2, {x,Z}=2t, {t,Z}=2xZ. These give

    {R,L}=t,
    {R,M}=x^3-4xZ^2+2t^2,
    {L,M}=1+x^3-6xZ^2.

Consequently the FULL bracket, with nothing suppressed, is

    {H,G}=1+x^3-6xZ^2
          +2(x+Z)(x^3-4xZ^2+2t^2)-3t(x+Z)^2.                (3)

Since t has weight zero and t^2=1+x^2Z is homogeneous of weight zero, every term after the initial 1 has nonzero Laurent weight. Therefore the ENTIRE weight-zero block of (3) is exactly the polynomial 1, not just its evaluation at t=±1. But the weight-four block is exactly 2x^4. In particular (2) is NOT a scalar-bracket pair. The constant block here uses the known two-bracket-sum control embedded in a new two-sided endpoint configuration; it is not advertised as a new bracket-span mechanism.

For this control, N=15 is the minimum under invertible affine target changes. A nonconstant affine combination with nonzero G coefficient has interval [-6,3]; one without G has interval [-4,2]. Two independent combinations must include a G coefficient, giving minimum width sum 9+6=15. Constants have interior weight and do not change this.

From any affine-minimal representative, a degree-k>=2 polynomial in the smaller coordinate has interval [-4k,2k], strictly containing [-6,3] at both ends. Subtracting it from the larger coordinate cannot cancel either of its new extreme terms and increases N. A nonconstant polynomial in the larger coordinate likewise cannot reduce the smaller coordinate's interval. Degree-one shears can leave N unchanged or increase it; a degree-one cancellation from an affine representative with both coordinates large merely restores N=15. Thus no affine change followed by a polynomial shear produces a strict decrease below 15 from the affine-minimal representative.

This establishes a local obstruction to that PARTICULAR invariant from weakened data. It neither excludes a route with temporary increases nor refutes another invariant. Most importantly, it is not a counterexample to a descent lemma whose hypothesis is the COMPLETE nonzero scalar identity: (3) explicitly fails that hypothesis.

## 3. What the non-extremal equations actually add

For a genuine scalar pair, EVERY integer ell must satisfy the exact polynomial equation

    sum_(m+n+1=ell)(m*p_m*q_n'-n*p_m'*q_n)
                    = c*delta_(ell,0).                       (4)

Absent blocks mean zero polynomials. Nothing in this report replaces (4) by the endpoint and constant equations. Those weakened equations alone would accept the control (2).

The next rows are already nontrivial. In the restricted TOP NORMALIZATION of this control, namely hi(H)=2, hi(G)=3 and p_2=q_3=1, the ell=5 and ell=4 equations respectively are

    2*q_2' -3*p_1' =0,
    2*q_1' +p_1*q_2' -2*p_1'*q_2 -3*p_0' =0.                (5)

They follow by listing the pairs (2,2),(1,3), and then (2,1),(1,2),(0,3). They are NOT an assumption about arbitrary leading coefficient polynomials. The control has p_1=1, q_2=0, p_0=0, q_1=t: it passes the first equation but fails the second by 2. Thus the omitted rows do contain a concrete extra condition.

However these first transport equations do not force the coprime leading powers to change. With p_1=1 and q_2=0, the second equation is solved polynomially by p_0=(2/3)q_1+constant for ANY polynomial q_1. This observation only solves those two rows; all remaining positive, negative and scalar rows in (4) still have to hold. No fully compatible completion is inferred.

The first unresolved FULL-HYPOTHESIS implication is therefore precise: does simultaneous satisfaction of ALL (4), together with two-chart regularity, force at least one polynomial-power endpoint cancellation whose opposite endpoint obeys the bound in section 1, after permissible affine changes? Neither (1), the entire ell=0 equation, nor the first two upper transport equations proves it. I have not shown that the remaining equations permit a complete coprime-power configuration, nor that they exclude every such configuration. A claim of descent would need this missing step (or a genuinely different invariant), not just leading commutation.

## 4. Stopping scope and documentary record

QUANTITY: a strictly decreasing positive-integer target-coordinate invariant for every unrestricted regular pair with full nonzero scalar bracket, until a one-sided coordinate appears. Result: NO_DESCENT / GAP. The specified N has a rigorously proved conditional move and an exact weakened-data local-minimum control, but no universal full-pair descent theorem.

CHEAPEST TEST performed: manual endpoint UFD analysis, interval arithmetic, the exact global control (2)-(3), and two explicit non-extremal equations. Planning wall: at most 15 minutes, UNMEASURED predictive cost. No scientific subprocess, degree scan, source payload or numerical computation was used. No new canonical OPEN ID, successor, implementation or review is requested.

The known one-sided-fibre and homogeneous exclusions are not re-proved or promoted. The prior normal-jet controls are not used as a new mechanism. Failure of this N under weakened hypotheses does not stop all two-chart, valuation or coordinate-change methods. No scalar pair on T, no exclusion of all such pairs, and no reduction of arbitrary JC2 to this fixed surface follows.

READ SCOPE: exactly TASK and its two pinned reports, all FRESH_WHOLE. They were supplied at manual/unreviewed scope; the algebra used here is derived above. No linked primary sources or live ROOT history work were read. Own report/PINS WHOLE readback, all three postpins, own-only OPEN/quantity/collision check and marker-last transaction complete publication.

COLLISIONS: EMPTY for owned targets at first action; the existing ROOT TASK remains untouched. Earlier reports and all canonical/shared artifacts are immutable for this task. All scientific exploration stops with the exact gap above.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10436`.
- Body SHA-256:
  `419dfb95c9915e483808074adc01a1d1fc706f0405c9513ab2ea7cbb7428ba2f`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
