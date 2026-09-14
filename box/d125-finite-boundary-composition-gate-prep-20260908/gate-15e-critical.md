# Fable gate: D125 pure critical first remainder (independent hostile review)

2026-09-07, 23:24-23:45 UTC. **Verdict: all six arrows CONFIRMED; the
provisional theorem "every genuine finite characteristic-zero pure-center
source arc in the accepted 14v setup has ord(alpha) >= j (alpha = 0 included)"
stands at the imported 14c/f/g/v and 15b trust stated below.** No concrete
counterexample and no missing arrow was found. The replay reproduces the
charged witness byte for byte in both modes and all six mutations fail with
their markers. Four independent changed-object controls of my own pass and
their mutations fail. Section 4 records evidence-description defects of the
producer checker and one notational clash; none changes a verdict. This is
review only: no promotion, launch, degeneration or JC2 conclusion.

## 1. Inputs and pins

The fourteen frozen files under /tmp/jc2-lane.UxqXJu/inputs were hashed
before reading and after every run; both listings equal input-pins.json
(box: input-pins-pre.sha256, input-pins-post.sha256, zero mismatches).
Producer report 7d7993d2bca7cd84bd2c7c7f40b7567c1f5be9b69c119c18c98f6d2b97ca7c74, checker 994958d87f223c75b474d4839e4c946e2f655762075bba65ec2014d09ca7bdf0, helper 25be0862730df8b66076eb59a2d1d0909fbcf563ea73ce16924affdc7c70ad66, charged witness a21b8c2a35768ca144a69f336fec870105bfbbc2882a2d40fe90b30098597377.
Sources 14c/f/g/v and 15b were read whole and consumed only at imported
trust; the 15b gate's section 3 defects were not used as support. The 2200
cross is omitted: no square-class or Pell statement is a premise anywhere
in the surviving argument, and none is needed.

## 2. Claim-by-claim verdicts

**Arrow 1, source and coordinates: CONFIRMED.** The setup is the 14v one:
R = p^2 V, V = g^3+p^3-3p, S = p^3+gp^2-p, R_s = R + h(s)S with h(0) = 0,
F = A - R_s^3 - alpha R_s of order j < m, F_j = RC, ord G >= 2j,
ord delta >= j+1, every F coefficient odd, degree <= 13, weight <= 3 for
w(g) = 5, w(p) = -7. The pure center forces a = ord(alpha) >= 1:
alpha(0) = ([p^3]R^3 + h(0)^3)/t(0) = 0 because R^3 = p^6 V^3 has no p^3
term, so r_s has order a/2 >= 1/2 and every substitution z = r_s converges.
The mixed [p]F = alpha h is an ordinary weight -7 coefficient of F and is
carried by the recursion untouched; beta, gamma enter only through delta and
q_s; F and G are odd because A, B, R_s are odd and q_s is even. The scalar
kernels b1, b3 never enter: D kills every scalar polynomial in z, so nothing
is normalized away. The coefficients e = [p]B and [g]B of 14g never appear;
the letter d in this packet is ord(delta) only (clash noted in section 4).

**Arrow 2, filtered coefficientwise division: CONFIRMED.** If V | P and
w(P) <= 3 then P = VU with w(U) <= 3-15 = -12, while every monomial of
p-degree 0 or 1 has weight >= -7; hence p^2 | U, Q = P/R has w(Q) <= 2 and
deg Q <= 13-5 = 8 (deg U <= 10). The correction -h_(l-i) S Q_i has weight
<= -5 and degree <= 11, so weight <= 3 and degree <= 13 persist at every
step and the recursion has bounded degree; it depends on h only through the
scalars h_k. Subtracting s^i R_s Q_i leaves F(g(s,0),p) unchanged, so
f_0 = F^(q)(g(s,0),p) = s^q (P_q^(q) mod V) + O(s^(q+1)); the leader lies in
Kbar[g,p]/(V), regular on all of affine V. V is prime, so "vanishes on V"
is "V divides". If the recursion never stops, f_0 = 0 and q is infinite.
Control A computes, by exact linear algebra on the 64 monomials of degree
<= 13 and weight <= 3, the 27-dimensional kernel of reduction mod V; it
equals V times the 27 predicted monomials, every element is divisible by
p^2 V, and the quotients have weight <= 1 and degree <= 8. At weight bound
8 the element pV enters the kernel and without a bound gpV and V do, exactly
the producer's countercontrols. Control E runs the recursion on an actual
input with two forced steps and checks it against an independent Newton root
of R_s(G,2) = 0 over Q[g]/(g^3+2) at the point (g0,2) of V: the s^2 and s^3
coefficients of f_0 vanish, the s^4 coefficient equals the recursion leader
at the point; ignoring the moving hS Q_i correction predicts q = 3 falsely,
and a prepended weight-15 term sV blocks the recursion at s^1 while the
Newton leader at s^2 is exactly h_1 (1/p0 - g0 - p0), the pole term.

**Arrow 3, implicit map: CONFIRMED.** L is the fraction field of
Kbar[g,p]/(V); V is absolutely irreducible because a root in Kbar((p)) would
have valuation 1/3, and it is primitive over Kbar[p]. In L[[s,z]] the
polynomial R_s(X,p) - z has X = g as a root mod (s,z) with derivative
3g^2 p^2 + h p^2, a unit, so Hensel gives the unique g(s,z) with no negative
powers. Oddness of R_s and uniqueness give sigma(g(s,z)) = -g(s,-z), hence
sigma(f_n) = (-1)^(n+1) f_n; scalars are sigma-fixed. A nonzero
anti-invariant element is never a constant, so the leaders of f_0 and g_0
are nonconstant. D is coefficientwise d/dp on L with s, z constant; its
kernel is Kbar since a derivation vanishing on a transcendental subfield of
a one-variable function field in characteristic zero vanishes identically.
f = min(q, j+a/2): below j+a/2 the leader is the odd remainder; at equality
it is psi_0 + rho C|V, nonzero because the eigencomponents cannot cancel and
nonconstant because its even part rho C|V is; above it, rho C|V alone.
C|V is nonconstant: a constant value is forced to zero at O = (0,0) in V,
contradicting V not dividing C. Terms with n >= 2 begin at >= j+a. Only
p and g are inverted, in L, as a proof device; no source inverse is used.

**Arrow 4, exact equation and inequalities: CONFIRMED.** I re-derived
[A,B] = [R_s,H] + [F,G] with a_s q_s - b_s = -delta and
[R_s,(5/3)R_s F^2] = (10/3)R_s F[R_s,F]. With D g(s,z) = -R_(s,p)/R_(s,g)
and g_z = 1/R_(s,g), the chain rule gives [R_s,Phi]hat = R_(s,g)hat D Phihat
and [F,G]hat = R_(s,g)hat (Fhat_z DGhat - DFhat Ghat_z), so
D Hhat + Fhat_z DGhat - DFhat Ghat_z = T with T = -(5/9)k^3 g(s,z)^2 /
(p^2(3g(s,z)^2+h)). At z = 0 this is (alpha+f_1)Dg_0 - (delta+g_1)Df_0 =
T(s,0); the left side has exact order a+v when v is finite, giving (1). At
z = r_s the G term vanishes exactly and D commutes with the scalar
substitution, so the non-cross part is -delta DU - (10/3) r_s U DU of exact
order M: at equal orders its leader is -D(delta_d psi + (5/3) rho psi^2),
nonzero because psi is transcendental over Kbar. The cross bound N follows
from ord Fhat_z >= j, ord Ghat_z >= 2j, ord DU = f and
ord DGhat(s,r_s) >= min(v, 2j+a/2). The four strict inequalities hold for
every finite a < j: 3j+a/2 > 2j+3a/2 >= M; 2j+f > a/2+2f because
a/2+f <= j+a < 2j; j+v > 3m on the target branch; on the other branch
j+q+d-a > d+q >= M when d <= 2j, and 3j+q-a >= 3j+f-a > a/2+2f with
margin 2(j-a) when d > 2j. Infinite q gives f = j+a/2 and the target branch;
infinite d gives M = a/2+2f; infinite v is trivial. Hence the equation forces
M = 3m, including the half-integral cases where M is not an integer, and the
cross bracket contributes nothing at 3m. Control B tests the full chain
rule with a genuinely moving, non-trivial coordinate g + p^2 + h g p
(R_g = 1+hp, inverse computed mod h^4) and random F, G: the identity with
its Jacobian factor, the zero-fiber equation and the critical-root factor
hold, and fail under omitted cross, fixed-g derivative, dropped Jacobian
factor and -5/3. Control C checks N > min(M,3m) with v at its bound (1)
and at infinity over 439,104 tuples with zero failures; allowing a = j gives
36,963 failures, the first at j = 1, a = 1, q = 2 where M = N = 7/2, so
a < j is load-bearing precisely where the proof uses it.

**Arrow 5, sign, target factor and primitive: CONFIRMED.**
R_(s,g) = p^2(3g^2+h) by direct differentiation. Since g(s,r_s) = g + o(1)
and g, p are nonzero in L, T(s,r_s) has exact order 3m with leader
-5 kappa^3/(27 p^2); the g^2/(3g^2) cancellation is what makes the leader a
pure function of p. Because M = 3m, at least one of lambda = delta_d,
mu = (5/3) rho is nonzero, and the s^(3m) coefficient reads
-D(lambda psi + mu psi^2) = -5 kappa^3/(27 p^2) = D(-5 kappa^3/(27 p)),
hence lambda psi + mu psi^2 + 5 kappa^3/(27 p) lies in ker D = Kbar. The
left side is in Kbar[g,p]/(V) by arrow 2, but 1/p is not: p X = 1 mod V
evaluated at the affine point O in V gives 0 = 1. No genus, normality,
properness or Picard statement is used; the contradiction is on affine V at
O. The sign of the primitive is immaterial to the contradiction, but the
producer's sign is correct as printed.

**Arrow 6, scope: CONFIRMED as stated.** The argument assumes a finite and
a < j and derives a contradiction; it says nothing about a >= j or alpha = 0,
about centers with t_0 not -3 or alpha_0, gamma_0 nonzero, about Laurent
coefficients, about whether any guarded point degenerates to this boundary,
about properness or emptiness of the complete ideal, jet extension, or JC2.
Infinite q, d, v are valuations of vanishing series inside a K[[s]] arc,
not an escape of the arc to geometric infinity.

## 3. Replay and custody

Fresh scratch subtree /tmp/jc2-gate-fable5-crit-scratch-2755099 holding only the two byte-copied files at the
repository-shaped paths; both hashes equal the charge before and after every
run and no bytecode was written. Each child ran under timeout 30, ulimit -t
25, ulimit -v 524288 with /usr/bin/python3 -I -B, then -O. Positive stdout
a21b8c2a35768ca144a69f336fec870105bfbbc2882a2d40fe90b30098597377 (normal) and a21b8c2a35768ca144a69f336fec870105bfbbc2882a2d40fe90b30098597377 (-O), byte-identical to the charged witness;
stderr empty. All twelve mutation runs exit 1 with the markers "actual
moving derivative", "actual filtered input fails without weight", "full
formal moving identity retains cross", "critical derivative factor", "target
factor after Jacobian division", "primitive sign". A scratch --record
reproduced all fourteen (mutation, optimized, returncode, stdout hash) rows
of the charged final-replay with the identical witness; mutation stderr
hashes differ only through the relocated traceback path (scratch
final-replay 2e071c935d6c30fa0c8fd967c3f9add4ac3984f7782309d33c3375e418105685). The producer's frozen outputs were never written to.

Owned controls, all zero Assert nodes, run under the same caps normally and
-O with byte-identical stdout:

| control | script sha256 | positive stdout sha256 |
|---|---|---|
| A weight lemma (arrow 2) | 79cd996f8b23d33d97e170640b9780d4cf6835eab399eeb7f72b404b7c678ae8 | a5078dd7afd2a7431c84c31e67eff8397e5bdad218f7564080d0ec0d9ac5569c |
| B moving chain rule (arrows 3/4) | 8355069266b6c62ae9e10b48e069e2a62cb1f3042289979bfbf28d6b83b86b4f | b1f49e37de7f6a50f99e23821a11e2486ce8bda63d9fa28393467cb498bd80fd |
| C valuation box (arrow 4) | 38a136abe94e7f167eb7d930d50a0ea9e800132bd4f24a47c7de083f96b8fd3b | 3d7a34eaa5b7843d9441b28cf80d0c30ca9ef28215ad269aa0a278b7f852edb6 |
| E recursion vs Newton root (arrow 2) | 723aac7a775e577041ee33ff8718ce487fab3d4beac183bd33794362a2cb3ef2 | 6dbe57610c373ee98efaf4eaa8f78a19b5f859a27f7315ae23c34843c1ebc748 |

Commands, return codes and markers of all 26 owned runs are in
controls/runs.tsv, the 14 replay runs in replay/runs.tsv, outputs in
controls/out and replay, hashes in controls/*.sha256 and
replay/replay-artifacts.sha256, all under
box/d125-pure-critical-remainder-gate-fable5-20260907/. Control A's first
version mis-predicted the quotient dimension with deg U <= 8 instead of
deg U <= 10 (V has degree 3); the divisibility verdict was already true, the
bookkeeping was corrected and all its modes rerun before charging.

## 4. Evidence-description defects and observations (no verdict change)

- The checker's --wrong-filtered-input mutation only tests that gpV has
  weight 13 and a p-linear monomial; it never exercises the division
  lemma's conclusion. Control A supplies that test at the stated bounds.
- The "full formal moving identity" and zero-fiber checks use the
  coordinate z = g, where R_(s,g) = 1, so the Jacobian factor and the
  moving implicit map are untested by the checker; the "critical root" is
  z = 1 with the constant alpha = -3. Control B covers the moving case.
- The four valuation tuples illustrate (4) only, as the report says.
- The letter d is ord(delta) here but the coefficient 5k^2/9 = [g]B in
  14g; e = [p]B never appears in this packet. Harmless, worth renaming.

## 5. Imported trust and unchecked boundaries

From 14v: F_j = RC with C even, C(0) = 0, V not dividing C, ord G >= 2j,
ord delta >= j+1, j < m, the odd/degree-13/weight-3 bounds on F, and the
reference normalization that fixes alpha by [p^3]F = 0. From 14c: odd
parity and the target -(5/9)k^3 g^2. From 14f: the centralizer K[R], used
only inside those 14v normalizations; this packet's own proof never calls
it. From 14g: nothing beyond notation. From 15b: the construction of L, the
implicit map and the parity law, each re-verified above rather than
imported. Polygon edges beyond the displayed constraints and the existence
of any arc at all are outside this review. Strongest surviving claim: for
every genuine characteristic-zero K[[s]] arc in the accepted 14v pure-center
setup, ord(alpha) >= j, alpha = 0 allowed; status PRODUCER-CHECKED and now
independently REVIEWED, not promoted. All children exited; no background
process, CAS, solver, AWS/SSH, live peer or shared edit was used. STOP/IDLE.

<!-- BODY-END -->
