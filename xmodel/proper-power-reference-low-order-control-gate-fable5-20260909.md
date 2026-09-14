# Gate review: proper-power reference low-order control (Fable 5.1, hostile different-model reviewer)

tag=proper-power-reference-low-order-control-gate-fable5-20260909
frozen_basis=0d39df3c9fd69c939a8420c54d03228b9077777d
reviewer model: claude-fable-5-1. Date 2026-09-09, started 04:39 UTC, deadline 05:00 UTC.

## 0. Read scope, custody verification, subprocess statement

Read scope: exactly the two flat copies in /tmp/jc2-lane.gMw3p0/inputs
(the coordinator note and its artifact.json). No other file, blind, peer body,
log, receipt, memory topic file, or web source was opened. The three blinds
cited by the producer (Fable0310 ecd7305a..., Root 64d3b5a2..., Astra
47e1475a...) were NOT read; every statement below about "the target inference"
means the inference AS RESTATED in the charged input, section "Exact tested
inference" and section 1.

Custody, verified by sha256sum on the two inputs and by re-slicing the body:

- report file: 6460 bytes, SHA-256 619a1df848d9ba8dcb82971ff5dbcaa341acfa020d2d6d295268eb111bcece4e (matches invitation)
- artifact.json: 693 bytes, SHA-256 bfd133e0c0f54c994064d57545e13b3093543cb54c4e25edb3c0a2cd09647d3b (matches invitation)
- body: bytes 1..6128 through the unique standalone body-end marker line (line 143 of the input), SHA-256 8ded9ec00877446df422c24f9d99295e1f04f6c94f13a3d910eefb9723342652 (matches invitation, artifact.body_sha256 and custody.source_sha256)
- artifact.frozen_basis equals the invitation basis; published_mode 0444; custody closed and finalized 2026-09-09T04:24:18Z.

Mathematical subprocesses: ZERO. No Python, CAS, arithmetic script, numeric
toy, expansion, solver, package install, checker, SSH, AWS or agent launch was
run. The only commands were date, ls, sha256sum, cat, sed/head/awk on the two
inputs, and heredoc writes of this report. All mathematics below is hand prose
using the product rule, Leibniz for the Jacobian bracket, one monomial bracket
formula, and degree/order bookkeeping. No high power was expanded and no
source polynomial was materialised.

Sections 1-5 below follow the five required groups. Verdicts are given
separately in section 5 for (i) the identity, (ii) the concrete control and
(iii) the stated consequence.

## 1. Group 1: the scalar-reference identity, re-derived

Setting (as charged): K a field of characteristic zero, ring K[s,u,v], the
bracket [P,Q] = P_u Q_v - P_v Q_u differentiates u,v only, s is a parameter.
A = a(R)+F, B = b(R)+q(R)F+G with a,b,q in K[s][R], primes are d/dR, and
rho := b' - a'q (so b' = a'q + rho by definition; no division claim is needed
for the identity itself).

Product rule, no power expansion: dA = a' dR + dF, and
dB = (b' + q'F) dR + q dF + dG. Wedging,

dA ^ dB = a'q dR^dF + a' dR^dG + (b'+q'F) dF^dR + dF^dG
       = (a'q - b' - q'F) dR^dF + a' dR^dG + dF^dG
       = -(rho + q'F) dR^dF + a' dR^dG + dF^dG.

Now T := a'G - rho F - (q'/2)F^2. Then
dT = a''G dR + a' dG - rho' F dR - rho dF - (q''/2)F^2 dR - q'F dF, and every
dR-multiple dies against dR, so dR^dT = a' dR^dG - (rho + q'F) dR^dF.
Hence dA^dB = dR^dT + dF^dG, i.e. [A,B] = [R,T] + [F,G]. CONFIRMED, with all
scalar coefficients (a', rho, q'/2) exactly as displayed. The only ring
hypothesis actually used is that 2 is invertible (for q'/2) and that s is not
differentiated; characteristic zero is sufficient. Homogeneity is not needed
for the identity, only for the order bookkeeping in section 2.

Degree hypotheses: with a,b monic of degrees M<N in R, b' has degree N-1 and
a' degree M-1, so the Euclidean quotient q has degree N-M and the remainder
rho has degree at most M-2. CONFIRMED. Note the identity holds for ANY choice
of q; the Euclidean choice is a normalisation, and G = B - b(R) - q(R)F
depends on it. The control is therefore a control of the setup WITH this
normalisation, which is the setup the charged note states.

## 2. Group 2: first rho order and why e>1 differs from e=1

Combined grading: deg s = 1, deg R = d. If b(R) = sum_k b_k(s) R^k is
combined-homogeneous of degree Nd, then b_k(s) is homogeneous of degree
(N-k)d in s, i.e. b_k = c_k s^{(N-k)d}. Then b' = sum_k k b_k R^{k-1} is
weighted-homogeneous of degree (N-1)d, a' of degree (M-1)d, so q is
homogeneous of degree (N-M)d and rho of degree (N-1)d. The coefficient
rho_i(s) of R^i is therefore a monomial c s^{(N-1-i)d}, so its s-order, when
present, is (N-1-i)d. CONFIRMED. The lowest allowed order is at i = M-2:
(N-M+1)d, which is (2e+1)d for M=3e, N=5e. CONFIRMED.

Interference mechanism (hand): in [R,T] the term -rho[R,F] has s-order
ord(rho)+j and the term a'[R,G] has s-order ord(G) (a' is a unit times R^{M-1}
at s=0). For [A,B] to vanish below 2j, a nonzero rho_{M-2} term with
(N-M+1)d + j < 2j, i.e. (N-M+1)d < j, must be cancelled by a G term of order
(N-M+1)d + j < 2j. So the low-order inference "ord G >= 2j" fails exactly
when rho_{M-2} is present and (N-M+1)d < j.

Why the old 3/5 case is safe (my own hand derivation, since the old argument
is not a charged input): F is by definition not in K[s][R], so F has positive
(u,v)-degree and j <= Md - 1 < Md = 3ed. For e=1 interference needs
3d < j < 3d, impossible. So "3d > j" is automatic at e=1, not an extra
assumption. For e >= 2 the window (2e+1)d < j < 3ed is nonempty, and the
control sits in it: 60 < 79 < 84. CONFIRMED, and the producer's phrase
"no analogous automatic inequality when e>1" is exactly right.

Possible versus attained coefficient: what section 1-2 establish is only that
the scalar-reference setup PERMITS a nonzero rho_{M-2}. Nothing in the charged
input shows that a genuine Keller source (a pair with [A,B] a nonzero constant
at s=1) attains a nonzero rho_{M-2}. The producer says so explicitly and I
concur: the control shows non-derivability, not attainment.

## 3. Group 3: every displayed coefficient, sign and order of the factored control

Data: R = h = u v^3, deg u = deg v = deg s = 1, so d = 4; M = 21, N = 35
(e = 7, so 3e:5e = 21:35 as required); j = 79.

Centralizer: h_u = v^3, h_v = 3u v^2, so
[h, u^i v^k] = v^3 * k u^i v^{k-1} - 3u v^2 * i u^{i-1} v^k = (k-3i) u^i v^{k+2}.
CONFIRMED. The monomial map (i,k) -> (i,k+2) is injective, so a K[s]-linear
combination of monomials brackets to zero iff every monomial has k = 3i, i.e.
is a power of h. Kernel = K[s][h] (the note writes Q[h]; over Q[s,u,v] the
kernel is Q[s][h], a harmless imprecision). CONFIRMED.

Reference and remainder terms, with combined degrees:
- a(R) = R^21, degree 84; a' = 21 R^20. CONFIRMED.
- b(R) = R^35 + s^60 R^20, degrees 140 and 60+80 = 140; b' = 35 R^34 + 20 s^60 R^19. CONFIRMED.
- Euclidean division of b' by 21 R^20: quotient (35/21) R^14 = (5/3) R^14 = q; a'q = 35 R^34; remainder rho = 20 s^60 R^19, degree 19 = M-2 exactly, s-order 60 = (N-1-19)d = 15*4. CONFIRMED.
- F = s^79 R u = s^79 u^2 v^3, degree 79+5 = 84, ord_s F = 79 = j. CONFIRMED.
- qF = (5/3) s^79 R^15 u, degree 79+60+1 = 140. CONFIRMED.
- G = (20/21) s^139 u, degree 140, ord_s G = 139 = j + 60. CONFIRMED.
So A = R^21 + s^79 R u and B = R^35 + s^60 R^20 + (5/3) s^79 R^15 u + (20/21) s^139 u
are ordinary polynomials, combined-homogeneous of degrees 84 and 140, with
coefficients 1, 1, 5/3, 20/21 in Q. No fractional exponent, negative exponent
or gauge. CONFIRMED.

Cancellation: a'G = 21 R^20 (20/21) s^139 u = 20 s^139 R^20 u; rho F =
20 s^60 R^19 s^79 R u = 20 s^139 R^20 u. Difference 0. CONFIRMED.
q' = (5/3)*14 R^13 = (70/3) R^13, q'/2 = (35/3) R^13. CONFIRMED.
T = -(35/3) R^13 (s^79 R u)^2 = -(35/3) s^158 R^15 u^2. CONFIRMED.

Brackets: [R,u] from the monomial formula with i=1,k=0: (0-3) u v^2 = -3 u v^2;
[R,u^2] with i=2,k=0: -6 u^2 v^2. CONFIRMED. Since [R,R^15 u^2] = R^15 [R,u^2],
[R,T] = -(35/3) s^158 R^15 (-6 u^2 v^2) = 70 s^158 R^15 u^2 v^2. CONFIRMED.
[F,G] = (20/21) s^218 [R u, u]; R u = u^2 v^3, and [u^2 v^3, u] = -(u^2 v^3)_v = -3 u^2 v^2,
so [F,G] = -(60/21) s^218 u^2 v^2 = -(20/7) s^218 u^2 v^2. CONFIRMED.

Independent cross-check by the six direct term brackets (Leibniz only):
[R^21, (5/3)s^79 R^15 u] = 35 s^79 R^35 (-3 u v^2) = -105 s^79 R^35 u v^2 and
[s^79 R u, R^35] = 35 s^79 R^34 (-R[R,u]) = +105 s^79 R^35 u v^2 cancel (the
a'q cancellation); [R^21, (20/21)s^139 u] = -60 s^139 R^20 u v^2 and
[s^79 R u, s^60 R^20] = 20 s^139 R^19 (3 R u v^2) = +60 s^139 R^20 u v^2 cancel
(the a'G - rho F cancellation); [s^79 R u, (5/3) s^79 R^15 u]:
[R u, R^15 u] = R^15[R u,u] + u[R u,R^15] = -3 R^15 u^2 v^2 + 15 u R^14 (3 R u v^2)
= 42 R^15 u^2 v^2, times 5/3 gives 70 s^158 R^15 u^2 v^2; and
[s^79 R u, (20/21) s^139 u] = -(20/7) s^218 u^2 v^2. Sum equals the displayed
[A,B] = 70 s^158 R^15 u^2 v^2 - (20/7) s^218 u^2 v^2. CONFIRMED by two routes.

Orders and degrees: the two terms have s-orders 158 and 218, distinct, so no
cancellation; [A,B] is nonzero of s-order 158 = 2j; every coefficient of
order below 158 vanishes; combined degrees 158+60+4 = 222 and 218+4 = 222,
equal to 84+140-2. ord_s G = 139 < 158. All CONFIRMED. The "late interval"
arithmetic 3j = 237 > (M+N-1)d = 55*4 = 220 is also correct.

## 4. Group 4: canonical-reference compatibility at the scope stated

Claims checked, all at the note's own scope:
- Below order 79 every non-reference term of A vanishes: A - a(R) = F has order 79. CONFIRMED.
- F_79 = h u = u^2 v^3 has (u,v)-degree 5, h-adic valuation 1 < 20 = M-1, so it is not divisible by h^{M-1} and cannot be absorbed by a reference correction c s^4 R^20 (degree 84, but a multiple of h^20). CONFIRMED.
- F_79 is not in K[h]: its degree 5 is not a multiple of 4, and by the monomial-bracket proof [h,F_79] = (3-6) u^2 v^5 = -3 u^2 v^5 is nonzero. CONFIRMED.
- The scalar b term s^60 R^20 lies in K[s][h], so it belongs to the reference, not to G. CONFIRMED under the convention "reference = all K[s][h] terms". This convention is load-bearing: if it were dropped and s^60 R^20 were counted in G, then rho = 0 and ord G = 60 < j, a different and weaker object. The note uses the convention consistently.
- s = 1: A = u^21 v^63 + u^2 v^3 has degree 84 with top h^21; B = u^35 v^105 + u^20 v^60 + (5/3) u^16 v^45 + (20/21) u has degree 140 with top h^35. Actual 84/140, not just labels. CONFIRMED.
- Coprime description: tops (h^7)^3 and (h^7)^5, H = h^7 of degree 28. [H,P] = 7 h^6 [h,P], so ker[H,-] = K[s][h] strictly contains K[s][H]: H is not closed. CONFIRMED. Primitive root h = u v^3 has multiplicities 1,3, unequal, not the balanced uv. CONFIRMED.

What is NOT verifiable here: whether the canonical algorithm of the uncharged
Fable0310 blind produces exactly this (a, F, b, q, G) from (A,B). I did not
read that blind. The control is valid for the decomposition rule stated in the
charged note (monic K[s][h]-reference, Euclidean q, remainder G). If the
target's canonical algorithm imposes an extra normalisation (for example a
different quotient rule, or a reference chosen after a further approximate-root
step on the curve R -> (a(R),b(R))), the control must be re-read against that
rule. I narrow the consequence accordingly in section 5 rather than assume it.

## 5. Group 5: adversarial scope, sanity checks, verdicts

Which LOW-order inference is refuted. The inference, as restated in the
charged note: from (P) A,B polynomial, (C) ker[h,-] = K[s][h], (H) combined
homogeneity of A,B with tops h^M, h^N, and (V) vanishing of every coefficient
of [A,B] of s-order below 2j (j = ord_s F), conclude ord_s G >= 2j. The
control satisfies (P),(C),(H),(V) with 2j = 158 and has ord_s G = 139. So
that inference, with exactly those hypotheses and the note's decomposition
rule, is false. The mechanism is the identity of section 1: (V) forces
a'G - rho F = 0 at order j + ord(rho), which FORCES an early G whenever
rho_{M-2} is present and (N-M+1)d < j.

Why the nonzero higher terms do not refute any Keller-source theorem. A
Keller source at s = 1 needs [A,B] to be a nonzero constant, so in the
combined grading [A,B] = c s^222 with c nonzero in K. The control's bracket is
70 s^158 R^15 u^2 v^2 - (20/7) s^218 u^2 v^2: it has a nonzero order-158
coefficient, an order-218 term, no order-222 term, and every term is divisible
by u^2 v^2. It is therefore not a Keller pair and does not satisfy the
hypothesis of any theorem that uses the order-158, order-218 or order-222
equations. A theorem deriving ord G >= 2j from the FULL constant-Jacobian
identity is untouched; what is shown is only that such a derivation must use
equations at or above order 2j (or another structural input), not the
sub-2j equations alone.

Hand changed-object and failed-arrow checks (all by the section 3 brackets):
1. Drop the scalar term s^60 R^20 from b (so rho = 0) and keep G. Then
   a'G - rho F = a'G = 20 s^139 R^20 u, and [R,T] acquires
   20 s^139 R^20 [R,u] = -60 s^139 R^20 u v^2 at order 139 < 158. Hypothesis
   (V) fails; the object is no longer a control. So the rho term is the
   mechanism, not decoration.
2. Keep b but set G = 0. Then -rho[R,F] = -20 s^139 R^20 (-3 u v^2)
   = +60 s^139 R^20 u v^2 survives at order 139 < 158, so (V) fails again.
   The early G is forced by (V), which is precisely the claim.
3. Failed arrow at e = 1: with M = 3, N = 5 and any d, (N-M+1)d = 3d, and
   j <= 3d - 1 because F has positive (u,v)-degree. The interference window
   is empty, so the same construction cannot produce an e = 1 control. This
   matches the note's statement that the old 3/5 inequality is special.
4. Sign/coefficient sanity: the two surviving terms have s-orders 158 and
   218 and (u,v)-degrees 64 and 4; they cannot cancel, so [A,B] is nonzero
   regardless of the scalar values 70 and 20/7. The low-order verdict does not
   depend on the exact scalars, only on a'G - rho F = 0, which is exact.

Adversarial points that do NOT overturn the control but bound its scope:
- The decomposition convention (all K[s][h] terms into the reference,
  Euclidean q) is load-bearing; see section 4. The consequence is stated
  relative to it.
- The control has G divisible by neither h nor any power of it, and F of
  h-valuation 1. Whether a genuine Keller source can have F_j of h-valuation
  exactly 1 with rho_{M-2} nonzero is not addressed and not claimed.
- Nothing here excludes degree 140, realises a source, or bears on the 84/140
  actual pairs beyond the single explicit polynomial pair above. The note
  claims none of these; any promotion text must not either.
- The bracket order threshold 2j is the note's; the control's bracket order
  is exactly 2j, so the control is sharp against "below 2j" and says nothing
  about inferences that also use the order-2j coefficient.

Verdicts:
- Identity [A,B] = [R,T] + [F,G], T = a'G - rho F - (q'/2)F^2, b' = a'q + rho,
  in characteristic zero with s a parameter: CONFIRMED.
- Concrete factored control over Q[s,u,v] (R = uv^3, M = 21, N = 35, j = 79,
  all displayed coefficients, signs, orders, degrees, the a'G - rho F
  cancellation, T, the two bracket terms and their distinct orders):
  CONFIRMED, by the identity route and independently by six direct brackets.
- Stated consequence ("the low-order kernel induction cannot assert
  ord_s G >= 2j from polynomiality, closed centralizer, combined homogeneity
  and sub-2j Jacobian vanishing"): CONFIRMED for the decomposition rule
  stated in the charged note; GAP only in the sense that the exact canonical
  rule of the uncharged Fable0310 blind was not read here and must be matched
  by whoever consumes this control. No REFUTED verdict on any item.

Not advertised: degree-140 exclusion, source attainment, JC2 progress.
No new OPEN identifier is raised. No compute, artifact, or lane is authorised
by this review.

## COLLISIONS

status: EMPTY

- NONE — this report raises no `OPEN[...]` entries; the charged input raised none.

<!-- BODY-END -->
