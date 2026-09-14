# Hostile gate: smooth rational finite cubic donors (Fable 5.1)

tag: smooth-cubic-donor-gate-fable5-20260912
reviewer: Fable 5.1, independent different-model reviewer of ROOT/Astra
skeleton written 2026-09-12 02:41 UTC; body edit 1 at 02:50 UTC
publication reserve 02:58 UTC, HARD 03:01 UTC, 2026-09-12, no extension
Manual review only: no code, CAS, network, Git, linked files or other model.

## 0. Source-read scope and input pins

All four snapshots in /tmp/jc2-lane.acoq3N/inputs were hashed at
02:41:49 UTC BEFORE any read; every digest matched the task's expected value.

| basename | SHA-256 (prepin) |
|---|---|
| smooth-cubic-donor-exclusion-root-20260912.md | 3045abc0d003ae4116ddb25449d4bd795fa84001e9e33c68bfe71efca6234628 |
| smooth-cubic-adjunction-astra-20260912.md | b06de62a462a216d5e0e92ba347e24fe3c3f524944e95d8815b97de8482e57e3 |
| INTERFACE.md | 6db62bf681fb4a1f8515b81044de05ed2071181ffcced29634f1440adc6ffbb8 |
| eghp-minimal-degree.pdf | 39c85a00fe9b133134acadddbeb0bdaeafbffb5d1bcb9f71536624e8597032b4 |

Exact read scope: the three Markdown files were read fresh and WHOLE by
cat to stdout (12633, 9516, 2574 bytes). The EGHP PDF was read ONLY on
printed pages 1--2, completely, by `pdftotext -f 1 -l 2 <pdf> -` to
stdout; no other page was opened. Those two pages contain inequality (*)
deg(X) >= 1 + codim(X, span X) and Theorem 0.1 (linear space, quadric
hypersurface in a linear space, rational normal scroll, cone over the
Veronese surface in P5). Per INTERFACE the F1 lemma CUBIC-SCROLL-DONOR-1
is accepted; neither linked report was opened, and only the reduction to
its stated interface is checked here.

## 1. Claim under review

SMOOTH-CUBIC-DONOR-1: Y smooth rational projective complex surface,
phi:Y->P2 finite of degree 3, ell any target line,
U = Y minus (Supp Ram(phi) union Supp phi^*ell): no dominant regular
A2->U of any degree. Nothing about singular normalizations, generically
finite completions, other degrees, other cubic intermediates or JC2.
ROOT proves g>=1 and g=0; Astra proves g>=1 independently (shared
valuation hint acknowledged in INTERFACE).

## A. Local structure of a finite smooth cubic: CONFIRMED

Independent derivation. O_{Y,p} is Cohen--Macaulay and finite over the
regular ring O_{P2,phi(p)} of the same dimension, so phi_*O_Y is locally
free of rank 3 (miracle flatness) and every scheme fibre has length 3;
the local length n at p satisfies 1<=n<=3. If d phi_p = 0, the centred
target parameters f,g lie in m^2; O_p/(f,g) surjects onto
O_p/((f,g)+m^3), whose length is 1+2+(3-dim<f_2,g_2>) >= 4: contradiction.
So rank d phi_p >= 1, one target coordinate pulls back to a coordinate s,
and analytically phi=(s,h(s,t)) with n = ord_t h(0,t) = dim C{t}/(h(0,t)).
The Jacobian is h_t. n=1: unit. n=2: h_t(0,t)=2ct+..., c!=0, so h_t is a
coordinate and R is smooth reduced there. n=3: h_t is t-regular of order 2,
Weierstrass gives unit(t^2+b(s)t+c(s)), and t -> t+b/2 (fixing s and
ds wedge dt) gives unit(t^2+a(s)), a(0)=0. a==0 is the doubled smooth
divisor; a=s^m u(s) gives Astra's t^2+s^m after s -> s u^{1/m}.
Every point of Y has n in {1,2,3}, so point coverage is complete. The
coefficient of R on a prime component is 1 unless the component is
doubled (coefficient 2), consistent with e-1<=2; a byproduct neither
author states but which is harmless: a doubled component meets no other
component of R. Valuation coverage is item B's job; A only supplies the
normal form. Analytic coordinates are legitimate because divisorial
orders and log discrepancies are intrinsic and are computed on the
analytic germ of the same algebraic blowups. ROOT's degree-4 control
(s^2,t^2) correctly marks the rank argument as degree-bound.

## B. All-valuation inequality, iterated blowup, LC of (Y,R/2): CONFIRMED (both routes)

Inequality (1), rederived. Let E be a prime divisor on a smooth model
over p, v=ord_E, z a local equation of E at its generic point, w a second
coordinate there. Write f=z^a f_1, g=z^b g_1 with f_1,g_1 units of the
DVR O_E. Then
df wedge dg = z^{a+b-1}(a f_1 dz wedge dg_1 - b g_1 dz wedge df_1)
              + z^{a+b} df_1 wedge dg_1,
every term of order >= a+b-1 relative to dz wedge dw. So
ord_E(df wedge dg) >= v(f)+v(g)-1; the -1 is exactly dz wedge dz = 0,
and the direction is >=, which is the direction both proofs use. With
f=s, g=t: A_v := 1 + ord_E(ds wedge dt) >= a0+b0, and ord_E(ds wedge dt)
is the discrepancy k_E of E over (Y,0), so A_v is the log discrepancy.
Identity: r=t^2+a(s), dr = 2t dt + a'(s) ds, so dr wedge ds = 2t dt wedge ds
exactly (a' ds wedge ds = 0), valid also when a==0. Apply (1) to (r,s):
v(r)+a0-1 <= ord_E(2t dt wedge ds) = b0 + A_v - 1, hence
v(r) <= A_v + b0 - a0 <= A_v + (A_v - 2a0) <= 2A_v.
Units: R = div(unit r) locally and a unit of O_{Y,p} has v=0 for every
valuation centred at p or along a curve through p. Coordinate changes:
A_v and v(R) are intrinsic. Hence the log discrepancy of (Y,R/2) at E is
A_v - v(R)/2 >= 0. Non-exceptional divisors: A_v=1, v(R)=mult<=2 by A.
Valuations centred off R: v(R)=0. So (Y,R/2) is LC at EVERY divisorial
valuation, with no use of R_red. I found no hidden cancellation
assumption. For a==0 the bound is A_v - v(t) >= a0 >= 0: LC, not klt.

Astra's blowup route, rederived. For t^2+s^m, m>=3, in the chart t=s t1:
pi^*(t^2+s^m) = s^2(t1^2+s^{m-2}), so pi^*R = R' + 2E, and
K_1 = pi^*K + E gives K_1 + R'/2 + 0E = pi^*(K + R/2): crepant,
exceptional coefficient 0. In the chart s=t s1 the strict transform
1+t^{m-2}s1^m misses E. R' meets E only at t1=s=0 with the same normal
form and exponent m-2. Old exceptional curves carry coefficient 0, so
pi^*(0 E_old)=0 at every later step and they never acquire a coefficient;
tangency of R' to a coefficient-0 curve is irrelevant to the pair. The
chain ends at m=1 (smooth half-divisor) or m=2 (two transverse
half-lines): SNC with coefficients < 1, klt. Crepant pullback preserves
every discrepancy, so (Y,R/2) is klt for a!=0 and LC for a==0. Imports:
crepant invariance and the SNC criterion, both named by Astra. Confirmed
and independent of ROOT's route except for the shared normal form.

## C. Adjoint section, boundary-resolution inequality, pole 6 vs 2: CONFIRMED

RR: chi(K+L) = chi(O_Y) + (K+L).L/2 = g since chi(O_Y)=1 (rational);
h^2(K+L) = h^0(-L) = 0 because L = phi^*O(1) is ample (finite pullback);
so h^0(K+L) >= g >= 1 when g>=1. The dichotomy g>=1 / g=0 is exhaustive
only because g>=0, which needs a smooth connected general member: Bertini
(L base point free) plus connectedness of ample divisors (Hodge index).
That import is load-bearing and both reports name it. R = div(det d phi)
is a section of omega_Y (x) phi^*omega_{P2}^{-1} = O(K+3L), so
2K+R ~ 3(K+L) and tau = sigma^3 is a nonzero element of
H^0(2K+R) = H^0(omega^{(x)2}(R)): a rational tensor-square two-form with
poles bounded by R and none along phi^*ell.

Boundary inequality, rederived. rho:Y'->Y is a log resolution of
B = Supp R union Supp phi^*ell with centres in B, so every exceptional E
lies in B' = rho^{-1}(B)_red. With K_{Y'} = rho^*K_Y + sum k_E E and
rho^*R = R_strict + sum m_E E, the coefficient of
2(K_{Y'}+B') - rho^*(2K_Y+R) is 2k_E+2-m_E = 2(A_E - m_E/2) >= 0 on E
(item B); 2-mult >= 0 on strict R components; 2 on strict components of
phi^*ell off R; 0 elsewhere. The multiplicity of phi^*ell never enters:
B' is reduced and tau has no pole there. A nonreduced pullback, a line
inside R, a tangent or flex line, or coincident components only change
WHICH points are blown up, and B covers every valuation over every point.
So rho^*tau is a nonzero element of H^0(Y', 2(K_{Y'}+B')).

Logarithmic pullback. f dominant regular into U and rho iso over U give
f':Z->Y' with f'^{-1}(B') contained in D := Z - A2, where Z is P2 blown
up at finitely many points of the infinity line L (indeterminacy is
finite and off A2) and D is the SNC total transform of L. At z in Z a
boundary equation y_i of B' at f'(z) pulls back to a nonzero function
(dominance) vanishing only on D, hence in the UFD O_{Z,z} equals
unit x prod x_j^{e_j} with x_j equations of D; its dlog is logarithmic,
and non-boundary coordinates pull back to regular forms. So
f'^*Omega^2(log B') -> Omega^2_Z(log D) exists, and its tensor square
sends rho^*tau to a section of 2(K_Z+D), nonzero because f' is
generically etale in characteristic 0 and tau is a nonzero rational
section. On A2, disjoint from D, it is h(x,y)(dx wedge dy)^{(x)2} with
h a nonzero polynomial. At the generic point of the strict transform of
L, x=1/t, y=s/t give dx wedge dy = -t^{-3} dt wedge ds and
h(1/t,s/t) = t^{-deg h}(h_top(1,s)+...), so the pole order is
deg h + 6 >= 6. A section of omega^{(x)2}(2D) has pole order <= 2 along
every component of D, and the strict transform of L is such a component
with coefficient 1; blowups at points of L do not change a generic-point
order. Contradiction. Hypotheses of the imports (surface RR and Serre
duality, embedded resolution of curves, resolution of indeterminacy by
point blowups, generic smoothness) are all met on the objects used.

## D. Genus-zero branch (ROOT only): CONFIRMED

g=0 gives (K+L).L = -2, K.L = -5. chi(L) = 1 + L.(L-K)/2 = 1+(3+5)/2 = 5;
h^2(L) = h^0(K-L) = 0 since (K-L).L = -8 < 0 forbids an effective K-L
against ample L. So h^0(L) >= 5 and r >= 4. |L| contains phi^*|O(1)|, so
it is base point free; psi contracts no curve (L ample), proper and
quasi-finite hence finite; Z = psi(Y)_red is an irreducible nondegenerate
surface (H^0(O(1)) = H^0(L)). Projection formula: 3 = L^2 = deg(psi)deg(Z).
EGHP (*), page 1: deg Z >= 1 + (r-2) >= 3. Hence r=4, deg Z=3,
deg psi=1, and Z is a surface of minimal degree in P4. Theorem 0.1,
page 2: linear space (deg 1) no; quadric (deg 2) no; cone over the
Veronese surface (deg 4) no; rational normal surface scroll S(a,b) in
P^{a+b+1} = P4 with a+b=3, so (a,b) in {(0,3),(1,2)}: exactly ROOT's
list. The Eisenbud--Harris convention cited on page 2 counts the cone
S(0,3) as a scroll, and ROOT treats it in any case. Both are normal:
S(1,2) is smooth; the vertex of S(0,3) is Spec C[u,v]^{mu_3}, an
invariant ring of a normal domain. Finite birational onto normal gives
psi an isomorphism; Y smooth excludes S(0,3), whose vertex has embedding
dimension 4. So Y = S(1,2) = F1 with L the hyperplane class E+2f.
Independent cross-check without the classification: a finite degree-3
pullback aE+bf on F1 needs a>0, b>a, a(2b-a)=3, forcing (1,2).
Interface fit: the accepted lemma quantifies over EVERY finite degree-3
phi:F1->P2 and EVERY line with no net genericity; transporting phi
through psi carries U exactly to F1 minus (Supp Ram union Supp phi^*ell).
The genus-zero case is discharged with no residual hypothesis. The
positive-genus method truly cannot replace it: on F1, K+L = -E-f is not
effective, so h^0(K+L)=0, matching ROOT's first control.

## E. Exhaustiveness, controls, first-leg factorization, boundary: CONFIRMED

g is an integer >= 0 (C), so g>=1 and g=0 exhaust the stated family.
Nothing depends on deg f, on ell being generic, or on the net being
generic. Controls verified: the degree-4 rank-zero map bounds A to
degree 3; the F1 double-root example shows Supp phi^*ell cannot be
dropped; a singular normalization loses flatness and the length bound;
a merely rational first leg may have indeterminacy inside A2, defeating
the infinity-only pole count. First-leg factorization: if a Keller map
F = phi o f with f:A2->Y regular, then det dF = (det d phi)(f) det df is
a nonzero constant, forcing f(A2) off Supp R; F(A2) inside P2 minus ell
forces f(A2) off Supp phi^*ell; F dominant and phi finite force f
dominant. So the theorem excludes exactly this route. Boundary:
smoothness (CM, coordinates), finiteness (flatness, ampleness, length
<= 3), rationality (chi(O_Y)=1 in both RR uses) and projectivity (RR,
global sections) are each used, and the statement claims nothing about
singular Y, generically finite completions, other degrees or JC2.
Strongest surviving statement: SMOOTH-CUBIC-DONOR-1 exactly as stated.

## Verdict

CONFIRMED at manual-proof tier. A CONFIRMED; B CONFIRMED on both the
all-valuation route and the iterated-blowup route; C CONFIRMED;
D CONFIRMED; E CONFIRMED. No item REFUTED, no GAP. Dependencies: the
accepted CUBIC-SCROLL-DONOR-1 interface (F1, all nets, all lines), EGHP
inequality (*) and Theorem 0.1 as printed on pages 1--2, and the named
standard imports. No novelty claim, no external theorem hunt, no
next-family proposal, no charge_basis (no exit-price assertion is made).

## Postpins

At 02:49 UTC an attempted second hash run was redirected to a path
inside the read-only lane directory and produced NO output; no digest
was observed by that attempt. The actual postpin run was made at
02:49:51 UTC to stdout, after sections 0--E were final, and all four
digests equal the prepins in section 0:

| basename | SHA-256 (postpin) |
|---|---|
| INTERFACE.md | 6db62bf681fb4a1f8515b81044de05ed2071181ffcced29634f1440adc6ffbb8 |
| eghp-minimal-degree.pdf | 39c85a00fe9b133134acadddbeb0bdaeafbffb5d1bcb9f71536624e8597032b4 |
| smooth-cubic-adjunction-astra-20260912.md | b06de62a462a216d5e0e92ba347e24fe3c3f524944e95d8815b97de8482e57e3 |
| smooth-cubic-donor-exclusion-root-20260912.md | 3045abc0d003ae4116ddb25449d4bd795fa84001e9e33c68bfe71efca6234628 |

After this final edit the report is read back WHOLE and the inputs are
hashed once more; the body-end marker is appended only if that run
matches these values. No artifact_finalize; the launcher owns custody.

<!-- BODY-END -->
