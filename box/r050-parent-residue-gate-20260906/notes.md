# Independent notes — R050 physical-place residue gate (Fable, 2026-09-06)

Inputs: only the seven frozen files in /tmp/jc2-lane.xD53BS/inputs (SHA 7/7 OK against
the run.v2 receipt). Moh's paper is NOT among them; every Moh-dependent arrow is consumed
from the exact-contact gate and marked as such in the report.

## A. Centre of the final-major disc (licensed pattern: D2 at 1/4, D1 final at 19/28)
Galois group of K((t^{1/28}))/K((t)) is Z/28, tau_k: t^{1/28} -> zeta^k t^{1/28}.
* Orders in (-1, 1/4): only integer 0 (unsplit, denominators divide den(delta_3)=1).
* Orders in (1/4, 19/28) with no split: an unsplit term at order d' must be fixed by the
  stabiliser of the prefix (k = 0 mod 4, i.e. Z/7), forcing 4 d' in Z, so d' = 1/2 only.
  Split terms there are excluded by the licensed pattern (level-2 sibling goes directly to
  finality; exact-contact gate s.3-4, Moh Prop 5.3 — consumed, not re-read here).
Hence eta = t^{-1} + c0 + alpha t^{1/4} + beta t^{1/2}, alpha^4 = c1 != 0.

## B. Semi-invariance of the D1 face
For k = 4j: tau(eta) = eta and tau(pi t^{19/28}) = zeta_7^{5j} pi t^{19/28}; tau(t^{-1/14})
= zeta_7^{-2j} t^{-1/14}. So f_sigma(w pi) = w f_sigma(pi) with w a primitive 7th root of 1.
Every monomial pi^q has q = 1 mod 7; degree 8 and squarefree => f_sigma = pi (C pi^7 + A),
A C != 0. Same result from the floor: 7i + 19q = -2 has solutions (i,q) = (-3,1), (-22,8).
The zero root is FORCED (not a choice) and simple. The four discs are conjugate under
t^{1/4} -> i t^{1/4}, so the 4 residue equations on one disc are conjugate to the others.

## C. Floors (u = t^{1/4}, z = u^3 v, N = i + 3q)
f: 7i + 19q >= -2  =>  N >= ceil((2q-2)/7): N=-1 none; N=0 q<=1; N=1 q<=4; N=2 q<=8.
g: 7i + 19q >= -7  =>  N >= ceil((2q-7)/7): N=-1 q=0 only (b/u); N=0 q<=3; N=1 q<=7.
Both from Lemma 2.1(i) orders lam_f = -1/14, lam_g = -1/4 (t-units) = -2/7, -1 (u-units).

## D. Residue and the Keller row
omega_f = dx/f_y, dx = -4u^-5 du, f_y = u^-3 H_v  =>  omega_f = -4 u^-2 du / H_v(u, v(u)).
Res_P = 4 H1'(v0)/A^2, v0 = (T-B)/A (exact SymPy: independent_checks.json "residue_formula").
J_{u,v}(x,y) = -4u^-2; [u^-2] J_{u,v}(H,G) = A b; [u^-1] = b H1'(v); so A b = -4 j and
b H1' = -4 [u^1](J_{x,y}(f,g) o phi). Cross-check: Xu Lemma 4.4 display at pi = 0 gives
J = lam_g * f'_sigma(0) * g_sigma(0) = -A b /4. Same sign.

## E. Residue theorem corollary (new here)
omega_f is regular on the whole affine generic fibre (smooth: f_y = 0 => f_x != 0), and every
final-minor place has ord_u omega = e(delta-1)-1 >= 0. Places over x = inf on the pattern:
P (e=4), P' (e=28), principal-minor and level-2-minor places. Hence Res_P + Res_P' = 0:
the seven-order expansion at P' is redundant with the four equations at P.

## F. Weight bookkeeping for "early-row compression"
[u^1](J o phi) = sum_{a,b} J_{ab} [u^{4a+4b+1}] (1 + c0 u^4 + alpha u^5 + beta u^6 + u^7 v)^b.
The pure-y row y^D contributes D c0^{D-1} alpha + ... for EVERY D >= 1, so the residue row is a
combination of Jacobian rows of all total degrees 1..250, not of a degree-bounded top band.
Membership in the ideal of any proper band subset is OPEN (not decided here).
