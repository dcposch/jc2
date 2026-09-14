# F9: the canonical polynomial reference has an ordinary reverse lift

Author: Astra /root/model_productivity, 2026-09-09. Status: NEW PURE-PROSE LEMMA, UNREVIEWED. Basis 0d39df3c9fd69c939a8420c54d03228b9077777d is provenance. Absolute deadline 06:55 UTC. ZERO mathematical subprocesses of any size.

## 1. Exact result and accepted-source perimeter

Let k be a characteristic-zero field. Put

    w(g^i p^j)=2i+j,       t(g^i p^j)=i-j,
    d=-3/2,               H=p*(p^2-g)^2*(p^2-(3/2)g),
    Delta=conv{(0,0),(2,0),(3,1),(0,7)}.

For a nonzero polynomial the w-degree and t-degree mean the respective maxima over its monomials; for zero both are minus infinity. Suppose A in k[g,p] has support in 3Delta, equivalently w<=21 and t<=6, with the two exact faces

    A_(w=21)=H^3,       A_(t=6)=d^3*g^6*(gp+1)^3.       (1.1)

Assume also that its accepted reverse image

    phi(A)=A(v^-1,u*v^3-v)

belongs to k[u,v]. These are hypotheses of accepted16a/b/c for the normalized first member of every actual degree84/140 source. No condition on B or its Jacobian is needed for the compatibility lemma itself.

Construct the canonical reference R and scalars alpha,a0 by the finite polynomial division in Section 2. Set

    F=A-R^3-alpha*R-a0.                                (1.2)

Then:

1. R is supported in Delta and has w-leading form H.
2. Both phi(R) and phi(F) are ordinary polynomials in k[u,v].
3. The entire t=6 and t=5 parts of F vanish: t-degree F<=4.
4. Writing q=gp+1, the only positive-t packets of R are

       R_(t=2)=d*g^2*q,       R_(t=1)=lambda*g*q

   for a scalar lambda in k, possibly zero. These are consequences, not an extra gauge.

In particular a nonzero scalar multiple of H^2/p cannot be the order8 coefficient of this canonical F under weighted dilation. This eliminates that previously useful face-only direction at the full accepted reverse-source interface. It does NOT eliminate all order8 possibilities, order9, the H-divisible branch, F9, actual84/140 or JC2. No assertion H|C implies H^2|F is made.

The new proof rederives every required part of the canonical A construction independently. The author's earlier weighted-reference theorem is currently UNREVIEWED and is used only to identify the same convention, not as a mathematical premise. In particular its centralizer, B kernels, F_j divisibility and bound j<=13 are not invoked. Thus this lemma can re-root directly to accepted16a/b/c. The 16a/b source arrow retains its imported-primary and complex-normalization scope; the algebraic lemma above is over any k satisfying its literal hypotheses. There is no new field descent, nilpotent-scheme assertion or existence claim.

## 2. Canonical construction and its support bound

Introduce a formal parameter s solely to keep distinct w-homogeneous components separate:

    A_s=s^21*A(s^-2*g,s^-1*p).

This is a finite polynomial. Give s weight1, g weight2 and p weight1. Start with H and successively form

    R_s=H+sum_(r=1)^7 s^r*R_(7-r),                    (2.1)

where R_(7-r) is w-homogeneous of weight7-r. At stage r, take the order-r coefficient of A_s minus the cube of the already constructed reference. Divide that polynomial by 3H^2, using ordinary single-divisor polynomial division with the fixed global lexicographic monomial order g>p. Choose its homogeneous quotient as R_(7-r).

Here the leading monomial of H is d*g^3*p and that of 3H^2 is 3d^2*g^6*p^2. Its coefficient 3d^2=27/4 is a fixed unit. Adding s^r R_(7-r) changes the cube at order r by exactly 3H^2 R_(7-r); every other change has later s-order. Therefore each of the first seven final residuals is normal with respect to the monomial g^6*p^2. No division by p, H, a source coefficient, or a localization parameter is performed.

The division preserves the needed second support bound. H has t-degree2, and H^2 has t-degree4, attained by its lex leading monomial g^6*p^2. Inductively the input A_s and the current reference cube have t-degree at most6. During single-divisor division, a reducible current monomial with t-degree T<=6 gives a quotient monomial of t-degree T-4<=2. All terms of its product with H^2 have t-degree at most T, because every term of H^2 has t-degree at most4. Thus no reduction introduces a monomial above6. Moving an irreducible monomial to the remainder does not alter that statement. The quotient has t-degree at most2. The induction therefore proves that every R_(7-r), and hence R_s coefficientwise, has t-degree at most2.

The divisor is w-homogeneous of weight14. Each quotient and remainder remains w-homogeneous; the quotient has weight7-r. Ordinary polynomial division also preserves nonnegative g and p exponents. Consequently

    R=R_s|_(s=1) has w-degree7, t-degree<=2,

which is exactly support in Delta. Its top w-part remains H.

For completeness, retain the original scalar convention rather than quietly changing the reference. At order14 divide the weight7 residual of A_s-R_s^3 by H with the same monomial order. Its quotient is a scalar alpha, possibly zero. Subtract alpha*s^14 R_s, then choose a0 so that the remaining order21 constant is killed. Put

    F_s=A_s-R_s^3-alpha*s^14*R_s-a0*s^21.             (2.2)

The alpha and a0 terms begin at orders14 and21 and do not change the first seven normal residuals. Specializing s=1 gives exactly (1.2), with w-degree F<=20 because the w=21 forms cancel. Also t-degree F<=6, because each term in (1.2) has that bound; alpha R and a0 have t-degree at most2 and0. The facts used below are precisely:

    (i) R is in Delta;
    (ii) F has w<=20 and t<=6;
    (iii) F_r for 1<=r<=7 contains no monomial divisible by g^6*p^2.

The subscript r in (iii) is s-order, so its monomials have w=21-r. It is not an anti-diagonal index. The map from an actual monomial of F to its s-order is unique. This prevents higher residuals or later scalar choices from changing the three coefficients used next.

## 3. Exact reverse criterion and the anti-diagonal2 packet of R

Accepted16c gives, and its terminal independent gate verifies, the following exact criterion. Write an ordinary polynomial W as

    W=sum_t g^t*f_t(q),       q=gp+1,
    f_t(q)=sum_(i-j=t) [g^i p^j]W*(q-1)^j.

This regrouping takes place in k[g,g^-1,q]; the original W is still ordinary. Under phi, the basis monomial g^t q^k becomes u^k v^(2k-t). The index map (t,k)->(k,2k-t) is injective. Therefore there is no cancellation between distinct anti-diagonals, and phi(W) is ordinary exactly when

    q^ceil(t/2) divides f_t(q) for every t>0.         (3.1)

For t<=0 no condition is necessary. This explanation uses the actual fixed inverse, not a presumed source-family inverse.

In R, a t=2 monomial has i=j+2 and weight3j+4<=7. Thus only g^2 and g^3*p occur. The latter is fixed by the w-leading form H with coefficient d. Write r20=[g^2]R. Then

    R_(t=2)=g^2*f2(q),       f2(q)=d*(q-1)+r20.

We now prove r20=d without assuming reverse ordinaryness of R. The t=6 part of R^3 can only be the product of three t=2 parts; every factor has t<=2. The alpha R and a0 terms contribute nothing there. By the fixed face of A,

    F_(t=6)=g^6*(d^3*q^3-f2(q)^3).                 (3.2)

The possible t=6 monomials of A are g^6,g^7*p,g^8*p^2,g^9*p^3. The last has weight21 and is absent from F by cancellation of the upper forms. The term g^8*p^2 has weight18, hence is in F_3, and is divisible by g^6*p^2; canonical normality makes its coefficient zero. The remaining t=6 packet of F is consequently of q-degree at most1.

Put epsilon=r20-d, so f2=d*q+epsilon. In (3.2) the q^3 coefficients cancel and the q^2 coefficient is -3*d^2*epsilon. It must be zero. Since 3d^2 is a nonzero scalar in k, epsilon=0. Substituting back into (3.2) kills the entire packet, including the potentially allowed g^6 and g^7*p terms. We have proved

    R_(t=2)=d*g^2*q,       F_(t=6)=0.              (3.3)

This comparison accounts for all reference cross terms: reaching t=6 with three factors of t<=2 forces all three to have t=2. No term of lower t can tie.

## 4. Reverse ordinaryness of A forces the anti-diagonal1 packet of R

A t=1 monomial of R has i=j+1 and weight3j+2<=7, so only g and g^2*p are possible. Set

    r21=[g^2*p]R,      r10=[g]R,
    f1(q)=r21*(q-1)+r10,
    R_(t=1)=g*f1(q).

The t=5 part of R^3 has only the anti-degree pattern (2,2,1), in its three orders. Using (3.3), it equals

    3*d^2*g^5*q^2*f1(q).                            (4.1)

Again alpha R and a0 cannot contribute at t=5. The entire t=5 list allowed by 3Delta is g^5,g^6*p,g^7*p^2,g^8*p^3. The last two have weights16 and19, respectively; they belong to F_5 and F_2. Both are divisible by g^6*p^2, so both coefficients vanish by the first-seven normality. There are no further slots: i=j+5 and 2i+j<=21 give 0<=j<=3. Hence for scalars gamma0,gamma1

    F_(t=5)=g^5*(gamma0+gamma1*(q-1)).              (4.2)

The accepted reverse criterion for the actual A requires q^3 to divide its t=5 packet. Equations (4.1)–(4.2) give this packet exactly as

    3*d^2*q^2*f1(q)+gamma0+gamma1*(q-1).           (4.3)

Its q^0 coefficient is gamma0-gamma1 and its q^1 coefficient is gamma1. Their vanishing first gives gamma1=gamma0=0. Its q^2 coefficient is then 3*d^2*f1(0), so f1(0)=0, equivalently r10=r21. Therefore

    F_(t=5)=0,       R_(t=1)=r21*g*q.              (4.4)

This is a forced coefficient equality, not setting r21 to1 or assuming it is nonzero. Since t-degree R<=2, (3.3) and (4.4) are all its positive anti-diagonals. Each is divisible by q as required by (3.1) for t=1,2. All nonpositive packets automatically reverse to ordinary polynomials. Thus phi(R) belongs to k[u,v]. Equation (1.2) and ordinaryness of phi(A) then give ordinaryness of phi(F). Equations (3.3) and (4.4), together with the earlier bound t<=6, prove t-degree F<=4.

No B equation was used. No unknown source coefficient was silently fixed, eliminated from the source, or divided out. Both possible vanishing and nonvanishing values of r21 are retained.

## 5. Exact effect on the p-sensitive direction; scope of the gain

The polynomial H^2/p is ordinary because p divides H. Its w-degree is13 and its t-degree is5. Its unique maximal-t monomial is d^2*g^6*p, whose coefficient d^2=9/4 is nonzero. This is a factored leading-term comparison, not a materialized source expansion.

If F_8 were lambda*H^2/p for lambda in k*, its contribution to the actual coefficient [g^6*p]F would be lambda*d^2. No F_r with r different from8 can contribute to that monomial, because its weight13 uniquely fixes r=21-13=8. This contradicts the vanishing of the entire t=5 part proved above. Thus this exact direction cannot be the first F_8, or indeed the whole F_8 coefficient, of the canonical decomposition of an accepted full reverse source.

This upgrades the prior control's typing, not the whole source theorem. The direction satisfied the upper and lower strict support bounds for A and the weaker H-divisibility conclusion; it was never claimed to satisfy all reverse rows and Jacobian rows. The new compatibility lemma identifies the specific reverse/canonical obstruction it misses.

If the separately UNREVIEWED weighted theorem later supplies F_j=H*C, this result would additionally give t-degree C<=2, because for nonzero polynomials over the field k the t-leading product cannot vanish and t-degree H=2. That is a conditional composition only. It does not imply H divides C. In particular no conclusion here excludes all remaining H-divisible first contacts, or substitutes a localization at p for source polynomiality.

The lemma itself also allows F=0 when the Jacobian premise is absent. For example D=H+d*g^2 has precisely the positive packet d*g^2*q, hence phi(D) is ordinary. The accepted reverse control A=D^3+1 has the required two faces and this construction gives R=D, alpha=0,a0=1,F=0. Pairing it with D^5+1 gives Jacobian zero, not a guarded source point. This shows exactly why the compatibility lemma by itself is not a nonexistence result.

## 6. Fixed source versus moving dilation; manual falsification controls

The proof of Sections 3–4 uses the actual s=1 source. It does not assert phi(R_s) is ordinary under the same fixed inverse for every s. In fact (3.3) determines the dilated t=2 part to be

    (R_s)_(t=2)=d*g^2*(gp+s^3).

The g^3*p term has weight7 and defect0, whereas the g^2 term has weight4 and defect3. The corresponding t=1 part is r21*s^2*g*(gp+s^3), since g^2*p and g have defects2 and5. Thus the natural displayed packet parameter is q_s=gp+s^3, not gp+1. Keeping the fixed inverse when s is an indeterminate would leave, already in the t=2 packet, the term d*(s^3-1)*v^-2. No fixed-lambda family assertion is smuggled into the compatibility proof. A claim about a whole moving source family would require its own precisely transported source statement.

The following changed-object checks are manual identities, not executed tests or full source witnesses:

1. Omit the canonical-normality requirement. Keep A=D^3+1 as above but choose a different reference R'=D+epsilon*g^2 with epsilon nonzero. Defining F'=A-(R')^3-1 yields t=6 packet g^6*(d^3*q^3-(d*q+epsilon)^3), whose q^2 coefficient is nonzero. Its forbidden g^8*p^2 term shows why an arbitrary polynomial reference cannot replace the specified canonical one.
2. Omit reverse ordinaryness of A while preserving both faces. Let R'=D+epsilon*g and A'=(R')^3+1. The support is in 3Delta and both faces in (1.1) remain fixed, but its t=5 packet is 3*d^2*epsilon*q^2, not divisible by q^3. Thus the reverse premise, rather than the two faces alone, supplies the second coefficient screen.
3. Retain the p-sensitive direction as a purported canonical F_8. Its coefficient lambda*d^2 at g^6*p violates the exact vanished packet (4.2). This is a changed-coefficient contradiction, not a count or rank heuristic.

These comparisons require no assumption of squarefree roots, a generic coefficient, a normalized nonzero r21, or a polynomial mate for a control. They have not been passed off as computational evidence.

## 7. Custody, dependency boundary and remaining obligations

The exact input vector is in box/f9-reference-reverse-compatibility-20260909/input-pins.json, with paths, byte counts, hashes and read scopes. The accepted reverse producer f1fd6624... and transaction a2c27170... and terminal different-model gate 81b6e559... were whole-read at their current pins. The source/map/ratio/joint-gate parents were previously whole-read at the same immutable bytes and are freshly rehashed. The author's weighted report d7fb64af... is only a convention comparison; its pending gate has not been accessed. The missing guessed standalone custody path is recorded in READ-SCOPE, and the actual reverse transaction supplied custody metadata.

No mathematical subprocess, toy execution, source expansion, CAS, AWS/SSH operation, model lane, external source lookup, protected-project inspection, live report read, shared-ledger edit or public write occurred. Hashing, reading and artifact lifecycle operations are metadata work only. The complete authored proof was read back before its final BODY-END; its raised-OPEN extraction and transaction are retained as metadata. No new OPEN is raised or corpus collision search needed. All writers stop after close/finalize/verify and terminal custody.

Result: a new unreviewed accepted-source compatibility lemma, with explicit ordinary reference and t-degree F<=4. Remaining source exclusions, any use of the unreviewed weighted theorem, any B reconstruction, and any ideal or nonexistence claim remain outside this task. No follow-on authority is created.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15644`.
- Body SHA-256:
  `83517ff61972a4ce097518a8f234f914641b84c5448d4b583d1e2adf07d349f4`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
