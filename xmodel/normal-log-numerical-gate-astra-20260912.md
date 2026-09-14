# FIRST — normal-surface numerical logarithmic criterion

MANUAL FIRST. Reviewer Astra, distinct from producer Fable. First action2026-09-12 10:12:26 UTC; original reserve10:36/HARD10:39 unchanged. TASK and five inputs matched before charged bodies; own destinations absent. No scientific execution, network or tree test.

## Verdict by claim

- A: **CONFIRMED as an explicitly NUMERICAL criterion**, with the definitions and singular-open argument below. Ordinary non-Q-Cartier LC language is not justified merely by renaming it.
- Adjoint existence: **CONFIRMED under H1(O_Y)=0 and a smooth connected general section of positive genus**; actual-source H1 has the trace/Leray derivation below. Normality alone is insufficient.
- B valuation identities: **CONFIRMED with normalized restrictions, numerical R, Cartier line orders, and the FULL-field Keller scope for the source identity**.
- Quadratic automorphism control: **CONFIRMED manually**, including its three blowups and contraction matrix.
- Finite resolution check: **CONFIRMED for a genuine log resolution with its actual contraction data**. Printed-tree/source consumer: **GAP**; no class exclusion or tree launch follows.

## A. Definition, effectivity, and exact form

Let rho:X→Y resolve the normal projective surface and Supp(R+H). For a Weil Q-divisor D define rho_num^*D as its strict transform plus the unique exceptional rational combination orthogonal to every exceptional curve. The exceptional intersection matrix M is negative definite, hence invertible. This pullback is linear, equals ordinary pullback for Cartier divisors and principal divisors, and is compatible with further resolutions by the projection formula and uniqueness.

It preserves effectivity. Write rho_num^*D=D_strict+sum a_i E_i for D≥0. Then Ma=−b, b_i=D_strict.E_i≥0. If a has negative part a_-, the disjoint supports of a_+ and a_- and nonnegative off-diagonal intersections give

    a_-^t M a = a_-^t M a_+ - a_-^t M a_- > 0,

contradicting a_-^t(−b)≤0. Thus a≥0. No parameter factor or Cartier assumption on D is involved.

Choose compatible canonical divisors, using v=Phi^*(du∧dv), so K_Y=R−3H. Put

    A_Y^num(w)=1+coeff_w(K_X-rho_num^*K_Y),
    r_w=coeff_w(rho_num^*R).

The criterion assumes r_w≤2A_Y^num(w) for EVERY divisorial valuation over Y. For a nonzero sigma∈H0(omega_Y(H)), E=div(sigma)+H is an effective Weil divisor. The rational bicanonical form mu=sigma^3/v has divisor3E−R on Y and exactly

    div_X(mu)=3rho_num^*E-rho_num^*R+2(K_X-rho_num^*K_Y).

Indeed both expressions agree off the exceptional locus and each has intersection2K_X.E_i with every exceptional curve. Their difference is exceptional and orthogonal, so negative definiteness gives equality. Equivalently use linearity and principal-divisor compatibility. This is an equality of divisors, not merely numerical equivalence.

Effectivity of rho_num^*E and the assumed inequalities bound every boundary pole of mu by2. On strict R components A=1 gives coefficient(R)≤2. Elsewhere the form is regular. Hence mu is a nonzero section of2(K_X+D_X), with D_X the reduced total boundary.

**Singular-open issue.** For a finite normal complex surface over a smooth surface, Sing(Y) lies in Supp R. One local justification avoids assuming rational singularities: finite normal surfaces are CM, hence finite-flat over the regular target. After henselian localization isolate the finite local factor. Its canonical module is the reflexive B-module Hom_A(B,A); the trace section has divisor R, because its order at a height-one tame prime is e−1. If R misses the point, that section generates in codimension one and therefore everywhere by reflexivity. The trace pairing is perfect; reducing a finite-flat algebra to residue fields, perfect trace excludes nilpotents and gives a separable algebra, hence the morphism is étale there. Its source is smooth. These are standard finite-duality/reflexivity/trace facts, explicitly used, not a primary-text audit.

Consequently rho can be chosen isomorphic over U=Y−Supp(R+H). A dominant regular A2→U lifts to X−D_X. The accepted smooth logarithmic pullback argument applies without requiring Phi rho finite: resolving only source-infinity indeterminacy pulls mu to a nonzero logarithmic bicanonical section. On A2 it is h(dx∧dy)^2; at the original infinity line its pole is deg(h)+6≥6, but logarithmicity permits at most2. Contradiction. No Q-Gorensteinness is asserted or needed for this numerical criterion.

## Adjoint input is separate

A normal surface is CM. A smooth connected Cartier C∈|H| avoiding the finite singular set gives the exact sequence

    0→omega_Y→omega_Y(H)→omega_C→0.

Near C this is smooth adjunction; away from C multiplication is invertible, including at singular points. Serre duality gives H1(omega_Y)=H1(O_Y)^*. Thus H1(O_Y)=0 implies h0(omega_Y(H))≥g(C). Finite pullback makes H ample and spanned; Bertini and ample connectedness supply such a general C. Positive genus is still required.

For an actual dominant plane source, resolve its rational projective extension by blowups Z of P2 and take Stein factorization Z→Y'→Y. Normalized trace splits O_Y→(Y'→Y)_*O_Y'; low-degree Leray injects H1(O_Y') into H1(O_Z)=0. Hence H1(O_Y)=0, without a rational-singularity assumption. The already accepted generic-genus input supplies positivity for the stated hypothetical noninvertible source; it is not a fact about every arbitrary finite cover.

## B. Valuations and the finite test

Normalize w to value group Z and write its restriction to the target field as e*w', where w' also has value group Z. Finite field extension makes w' divisorial. Set n=w(H), an ordinary Cartier order. Locally a target uniformizer is a unit times t^e; differentiating contributes e−1, while residue-field separability makes the transverse differential a unit generically. Thus a pulled-back two-form has order e times its original order plus e−1. In characteristic zero this gives

    ord_w(Phi^*(du∧dv)) = e*A_tgt(w')-1-3n,
    A_Y^num(w)=e*A_tgt(w')-r_w.

The second follows by subtracting rho_num^*(R−3H). Therefore numerical half-ramification LC is exactly3A_Y^num(w)≥e*A_tgt(w'). The notation w(R) must mean r_w; a non-Cartier Weil divisor has no unspecified ordinary function-order.

For the FULL normalization of a Keller pair, its field is the source C(x,y). With m=w(L_source), ordinary discrepancy A_src over the source P2, and the ACTUAL affine coordinate volume du∧dv=c dx∧dy,

    e*A_tgt(w')=A_src(w)+3(n-m).

Here target H and source L are the respective actual infinity lines. This does not automatically apply to an arbitrary changed projective affine chart or a proper intermediate field with a nontrivial first-leg index. For a missed divisor over an affine target curve n=0. At a prime divisor of Y, A_Y=1 and r=e−1, so the test reduces to e≤3. Exceptional valuations require the full formula, not that generic-prime shortcut.

To reduce ALL valuations to a finite check, on a genuine log resolution put

    B_X=(rho_num^*R)/2-(K_X-rho_num^*K_Y).

Its support is SNC within the resolved boundary; the test is every coefficient≤1. Further point blowups produce coefficient b1+b2−1 at a crossing, or b1−1 at a smooth boundary point, hence still≤1. Numerical-pullback compatibility makes these the required discrepancies. This proves sufficiency on that actual resolution.

Computing relative canonical coefficients a on its contracted exceptional configuration requires

    M*a = (2g(E_i)-2-E_i^2)_i.

Fable's RHS−2−E_i^2 needs rational exceptional curves. Even when those come from the actual source blowups, one must identify the actual contracted subset, full intersection matrix and SNC resolution of R+H. A diagram with unspecified source map is not this data. For infinity profiles, {e_F repeated f_F} applies to the PRIME COMPONENTS ABOVE the chosen target infinity line, at general unramified intersection points of a general target line; sum e_F f_F=N. It does not include arbitrary affine dicriticals, and coordinate profiles need not be general-direction profiles.

## Controls and source limit

For (x+y^2,y), homogenization near its base point is [v+u^2:uv:v^2]. The charts v=u*t and then t=u*z yield [z+1:u*z:u^2*z^2]; the third base point is u0,z−1. Blowing it up leaves the contracted chain L(−1)−E2(−2)−E1(−2), with the last exceptional mapping onto target infinity. Its matrix times(3,2,1) is(−1,0,0), exactly the rational adjunction RHS. Thus A_Y(L)=4, while A_src(L)=1,n=2,m=1 gives1+3(2−1)=4. No unsupported graph is needed. Here R=0 but H0(K_P2+H)=0: dropping the adjoint premise would falsely exclude the automorphism.

The supplied finite cusp control (x^5+y^7,xy) has reduced ramification and generic e2 but at weights(7,5) satisfies A=12,r=35, so A−r/2=−11/2. It independently prevents replacing the all-valuation test by generic inertia≤3. Neither control is a new source family or Keller counterexample.

At original source infinity the displayed inequality specializes correctly to A_Y^num(L)≥d−2/3, when n=d,m=1,A_src=1. No numerical degree threshold or class data are imported from that formal identity. The candidate tree consumer remains GAP: no actual contraction/resolution matrix or all-source numerical bound is supplied. Normality is not that bound. A standard numerical extension survives, not a td6 exclusion, novelty claim, genus ceiling or JC2 result. No automatic tree test or further gate on a stopped consumer is recommended.

## Scope and closeout

Fable cross and both cubic texts were read FRESH_WHOLE after pins. ROOT postblind reused exact-pin WHOLE09:51; coordination reused exact-pin same-agent WHOLE05:51–05:53. TASK fresh WHOLE. Named standard foundations include resolution/negative definiteness/projection, CM finite duality/reflexivity/trace, Serre duality/Stein/Leray/Bertini and tame differential orders. Their applications are derived here; no primary text or linked source was newly read. The accepted smooth logarithmic pullback is reused at its exact scope.

Quantity: validity of the numerical criterion and identities versus actual tree availability. Cheapest test was this finite manual derivation and the supplied controls; no runtime estimate or computation is asserted. No new canonical OPEN/charge_basis. Own complete readback, six postpins and destination collision check precede final marker.

## COLLISIONS

status: EMPTY

- Own-only manual scope/identifier check; no canonical OPEN added, no corpus search. All six postpins matched and final report/manifest/custody destinations were absent at10:23:00. Own report/PINS/read-scope whole readback and exact quantity/control/scope check completed before the marker.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10824`.
- Body SHA-256:
  `08886b18b6df832b4c3df22e9e1dc2fca09afba7d767ee6ce19f0d956450e457`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
