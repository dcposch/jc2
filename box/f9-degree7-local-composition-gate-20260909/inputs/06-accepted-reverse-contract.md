# F9 exact reverse-polynomiality and complete small source contract

PROVISIONAL, root/Astra, 2026-09-09. Pure factored prose; ZERO mathematical subprocesses, coefficient emission, source powers, CAS, old checker, AWS or SSH. No ideal decision, implementation, runtime or novelty claim. Different-model review is required. This is new post-0445-cross research, not a mutation of that frozen packet.

## 1. Dependencies and exact question

Accepted AUDIT16a/b, with their explicit imported-primary perimeter, supply a necessary normalized ordinary receiver A,B over C for EVERY actual ordinary degree84/140 nonzero-constant-Jacobian source. The root source proof is xmodel/f9-fixed-degree-source-composition-coordinator-20260909.md SHA8c88c02728753173733e206e50bb2003071a8ae18f312fba59d4f3a220765b82; map proof xmodel/f9-polynomial-receiver-interface-astra-20260909.md SHA8bad927c8ef369a211fe3b1467efe6f9f40f26141e6338c1a470eb918a2fa50c; ratio proof xmodel/f9-cubic-root-ratio-coordinator-20260909.md SHA571d1fae2682c64c86a13599f0db827b6371f9b5f63b50b186ab8112adb9594c. Joint different-model gate xmodel/f9-source-receiver-joint-gate-fable5-20260909.md SHAf33820d2bf5f4f75229938b3cfb6d03d21cd05bb8c09a9cf340e3edaa351f7bd was terminal, receipt-first and all16current-input/report/prompt/fallacy checked05:42:30 BEFORE whole root access. Those three complete proofs were already whole-read by root; their accepted interiors are not newly reproved here.

Let Delta=conv{(0,0),(2,0),(3,1),(0,7)}. For m=3 or5 write W_m=A orB. Its allowed ordinary support is

    S_m = {(i,j) in Z^2: i,j>=0, 2i+j<=7m, i-j<=2m}.

Put H=p(p^2-g)^2(p^2-3g/2), d=-3/2. The normalized faces are

    l_(2,1)(W_m)=H^m,
    l_(1,-1)(W_m)=d^m g^(2m)(gp+1)^m,
    [A,B]_(g,p)=c*g, c!=0.

These alone have not been shown to force ordinary reverse lifts. The exact reverse substitution to test is

    g=v^(-1), p=u*v^3-v.

Sections2--3 prove an elementary necessary-and-sufficient linear criterion for that substitution to be ordinary. Sections4--5 give an exact finite ideal contract. Properness and unit membership are UNDECIDED.

## 2. Linear reverse-polynomiality criterion

Over any characteristic-zero field K, write W=sum a_ij g^i p^j with finite ordinary support in S_m. Introduce q=gp+1. For each integer s define

    f_s(q)=sum_(i-j=s) a_ij (q-1)^j.

This is an ordinary polynomial in q because j>=0; the finite regrouping is W=sum_s g^s f_s(q). Negative s here is Laurent notation for the regrouping, not a new ordinary g claim. Under the reverse substitution q=u*v^2, hence

    W(v^-1,u*v^3-v)=sum_(s,k) [q^k]f_s(q) * u^k*v^(2k-s).

Distinct pairs(s,k) give distinct Laurent monomials: equality of u exponents gives k, then equality of v exponents gives s. Thus cancellation between distinct anti-diagonals is impossible. For s<=0 every exponent2k-s is nonnegative. For s>0 the expression is ordinary if and only if

    q^ceil(s/2) divides f_s(q).

The support has s=i-j<=2m, so only s=1,...,2m are relevant. Equivalently, for each such s and 0<=k<ceil(s/2), the following LINEAR coefficient row is zero:

    L_(m,s,k)=sum_(j: (j+s,j) in S_m)
                 (-1)^(j-k) binom(j,k) a_(j+s,j) = 0,

where terms with j<k are zero. This is an exact field statement and also an exact coefficient-ring identity: no division by a coefficient, radicalization, generic stratum or localization is used. Rational numerical coefficients are harmless in characteristic zero.

There are nominally12 rows for m3 and30 for m5, since the successive orders are1,1,2,2,...,m,m. The outer s=2m face already gives f_(2m)=d^m q^m, so its m rows are redundant after the face constraints. No independence or minimal generating-set count is asserted.

## 3. Lift, degree, bracket and full source coverage

If those rows hold, define P(u,v)=A(v^-1,u*v^3-v) and Q analogously. They are ordinary by section2. In each expanded term coming from g^i p^j, the u exponent k is at most j and its v exponent is2k+j-i. The support gives j<=7m, so k<=7m. Moreover

    2k+j-i <= 3j-i <= 21m,

since i>=0 and j<=7m. The rows guarantee the lower bound0. Therefore P has support in[0,21]x[0,63] and Q in[0,35]x[0,105]. The top face fixes the p^(7m) coefficient to1. It yields u^(7m)*v^(21m), and no other source term reaches that pair: k=7m forces j=7m, then2i+j<=7m forces i=0. Hence the corners are nonzero and the ACTUAL total degrees are28m, namely84 and140, with no top cancellation.

The rational inverse substitution has determinant

    det d(g,p)/d(u,v) = v.

Indeed g_u=0,g_v=-v^-2,p_u=v^3,p_v=3u*v^2-1. Thus the chain rule in K[u,v,v^-1] gives [P,Q]=c*v^-1*v=c. Since P,Q are ordinary, this equality holds in K[u,v], including v=0. Nondivisibility of84 and140, together with the plane automorphism degree-divisibility theorem, excludes automorphy. A point of the full guarded contract is a genuine JC2 counterexample, not merely a monomial-J receiver.

Conversely, check that16a/b's normalization has not destroyed reverse ordinaryness of an actual source. Before the final diagonal scaling,

    A_old(g,p)=P0(g^3*p+lambda*g^2-r0,g^-1),

and similarly for B_old. Write A_new(g,p)=A_old(kappa*g,mu*p)/(alpha*mu^21), with kappa*mu=lambda as in16b. Then

    A_new(g,p)=P0(kappa^3*mu*(g^3*p+g^2)-r0,
                  kappa^-1*g^-1)/(alpha*mu^21).

It is exactly P_new(g^3*p+g^2,g^-1), where P_new(u,v)=P0(kappa^3*mu*u-r0,kappa^-1*v)/(alpha*mu^21) is an ordinary affine source transform; Q has its own nonzero output divisor beta*mu^35. Substituting g=v^-1,p=u*v^3-v recovers P_new,Q_new. Thus EVERY actual84/140 source yields receiver coefficients satisfying all section2 rows. This necessity uses16a/b; the sufficient lift above uses only the explicit support/faces/rows/bracket equations.

Output constants are free. We can impose A(0,0)=B(0,0)=1 by independent output translations, which preserve both positive-weight faces, the Jacobian, the reverse rows, and actual degrees. These conditions guarantee the origin vertices and do not set c=1.

## 4. Exact finite rational ideal, specified but not emitted

Take one variable a_ij for every(i,j) in S_3, one b_ij for S_5, and c,z. Work over Q. Define A,B as their finite formal sums, without expanding them here. The ideal I_F9 consists of ALL of:

1. Every coefficient equality for the two prescribed faces of A and B. For (2,1) include every slot on2i+j=7m, equating it to the corresponding coefficient of H^m. For (1,-1) include every slot oni-j=2m, equating it to d^m g^(2m)(gp+1)^m. Include zero target coefficients as well as nonzero ones; coincident face constraints must both hold.
2. A_00-1 and B_00-1.
3. Every reverse row L_(m,s,k) in section2 for BOTH components, even if redundant with a face.
4. Every ordinary coefficient of [A,B]-c*g, and the guard z*c-1.

There is no truncation, modular specialization, root-profile stratum omission, free scale gauge for c, or reverse-polynomiality assumption. A safe exhaustive index rectangle for item4 is0<=I<=23,0<=J<=55: g degrees at most9 and15 lose one under the bracket, p degrees at most21 and35 lose one. Absent slots are identically zero and may be represented as such; the target slot(1,0) is included. Explicitly the coefficient at(I,J) is the sum of(i*l-j*k)a_ij b_kl over i+k-1=I,j+l-1=J, minus c at(1,0). No row has been emitted or solved.

For scale only, the ordinary coefficient envelopes have124 and321 slots. Hand counting: for m3, i0..6 have22,20,18,16,14,12,10 allowed j values, and i7..9 have7,4,1; for m5, i0..10 have36,34,...,16 allowed values, then13,10,7,4,1. This is445 coefficient variables,447 with c,z, BEFORE linear elimination and fixed faces. The reverse rows are42 nominal; the safe Jacobian rectangle has1344 slots. These are desk envelope counts, not a builder output, rank/dimension proof, complexity estimate or measured acceleration. No generic polynomial division or guessed pivot is needed to state this ideal.

By section3, every characteristic-zero field point of I_F9 reconstructs an actual84/140 Keller counterexample. Conversely every such complex counterexample yields a complex point of I_F9 at the imported16a/b tier. Consequently I_F9 is proper over Q if and only if an actual degree84/140 complex counterexample exists: weak Nullstellensatz gives a Qbar point from properness, while any complex point proves properness. A rational point or zero-dimensional ideal is not required. Neither side is known. A unit certificate would exclude precisely this actual degree pair, not all degree140 or JC2.

## 5. Changed-object controls and limits

The single monomial W=g is ordinary and lies inside S_3, but f_1=1 is not divisible by q: its reverse is v^-1. Thus support alone is insufficient. Adding epsilon*g to A preserves both prescribed positive faces, actual top degrees and its four vertices, yet changes L_(3,1,0) by epsilon and destroys an already polynomial reverse. This is a control for the reverse criterion, NOT an example retaining all Jacobian equations.

The factor W=g^2(gp+1) has f_2=q, so it passes and lifts to u. Its mate V=p passes with s=-1 and lifts to u*v^3-v. Their bracket is not asserted constant; they test the coordinate dictionary only. For the lower face W=d^m*g^(2m)(gp+1)^m, f_(2m)=d^m*q^m and the reverse is d^m*u^m. Replacing it by d^m*g^(2m)(gp+1)^(m-1) fails one required vanishing order and produces v^-2.

A genuine zero-Jacobian control for the guard is D=H+d*g^2. Its only positive anti-diagonal is s=2, with f_2=d*q; the other terms of H have s<=0. Thus D has an ordinary reverse. Set A=D^3+1,B=D^5+1. Factored powers, not expanded here, have the prescribed upper/lower faces, origin constants1, support3Delta/5Delta and ordinary reverses, but [A,B]=0. They satisfy the unguarded coefficient equations with c=0 and are not Keller pairs. Hence the nonzero guard is essential. This is not a solution of I_F9 and not a finite numerical test or full-source expansion.

## 6. History/composition/decision

The0445 Astra blind proposed a complete ordinary5222-variable rectangle source and correctly warned that a necessary-only receiver has no automatic reverse lift. This report supplies a different explicit finite sufficient lift plus necessity, without constructing the original rectangle ideal or identifying unrelated Moh ideals. Earlier F2 reverse contracts are not imported by changing their exponents. The object/obstruction fingerprint is F9-normalized21/35 receiver / poles of the explicit inverse / anti-diagonal divisibility at q=0 / all coefficient rows. No external novelty claim follows from being new to this current interface.

Next cheapest test is different-model review of the coefficient bijection, the affine compatibility of the normalization, and the complete guarded ideal. If any of those fails, retain only individually valid one-way implications and STOP a builder. If confirmed, this becomes a smaller honest CE/exclusion contract, not evidence that solving it is affordable; a later implementation still needs an explicit source-preserving linear elimination design and bounded cost pilot. Nondecision or a resource estimate is not a mathematical unit/properness result. This proposal earns neither an AWS allocation nor a full coefficient expansion now.

## OPEN(S) RAISED

None. Properness is explicitly undecided; no new named OPEN identifier is allocated.

## COLLISIONS

status: EMPTY

- NONE — no OPEN identifier is raised; own-only check, not a corpus audit.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11462`.
- Body SHA-256:
  `032bfcb31f1fbcdd40456e431cb8383dc995e36eb29d99c74bd7f6a14f0a1e99`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
