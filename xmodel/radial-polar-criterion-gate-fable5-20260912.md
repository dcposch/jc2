# Independent FIRST: finite radial derivative generation and the two-polar criterion

Fable 5.1 gate, 2026-09-12, ROOT collector. Different-model hostile review by
hand; no computation, no literature, no source repair. Charged inputs read
WHOLE from /tmp/jc2-lane.e5svmL/inputs (pre-pins):

- CLAIM.md 3576962bed4195916367c80cb57b60d6041fc7766395f55a9ca59d8031627386 (2700 B)
- canonical-polar-trace-discriminator-root-20260912.md b8374142f0aa8373a3126ec5c934f02b3ed1abe1dd5230a055cb22189a90309b (5029 B)
- COORDINATION.snapshot.md 33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597 (48725 B)

Sections: 1 generation lemma; 2 two-polar criterion; 3 hypothesis audit and
controls; 4 out-of-scope items; 5 verdict table and post-pins.

## 1. Finite radial derivative generation — CONFIRMED

Frame: R=C[x,y], A=C[f,g], f_x g_y - f_y g_x = 1, E=(x d_x + y d_y)/2.

Signs. The inverse Jacobian is [[g_y,-f_y],[-g_x,f_x]], so the chain rule
gives d/df = g_y d_x - g_x d_y = D_f and d/dg = -f_y d_x + f_x d_y = D_g.
D_f f = D_g g = J = 1, D_f g = D_g f = 0. The commutator kills f and g, and
a derivation a d_x + b d_y killing both has (a,b)M = 0 with det M = 1, so
[D_f,D_g] = 0. Exactness: d((x dy - y dx)/2) = dx^dy and d(-f dg) = -J dx^dy,
so dH is closed, hence exact in R; H is a polynomial, unique up to a constant
that B = A[H] does not see.

Radial identities. H_x = -y/2 - f g_x, H_y = x/2 - f g_y. Then
D_f H = -(x g_x + y g_y)/2 = -E(g) and D_g H = (x f_x + y f_y)/2 - fJ = E(f) - f.
Directly, E(H) = -f E(g) = f D_f H.

Graph relation. f,g algebraically independent (J != 0, char 0), tr.deg B = 2,
so ker(A[W] -> R, W -> H) is a nonzero height-one prime of the UFD C[u,v,W],
hence (P) with P irreducible of positive W-degree. P_H(f,g,H) != 0 because
P_H has smaller W-degree than P and is nonzero in char 0. Applying D_f, D_g:
P_f = -P_H D_f H, P_g = -P_H D_g H, so a = E(g), b = f - E(f);
a,b lie in R with no inverse of P_H needed.

Basis expansion. (D_f,D_g) is an R-basis of Der_C(R) (unit determinant),
so E = E(f) D_f + E(g) D_g = (f-b) D_f + a D_g.

Filtration. E = (f + D_g H) D_f - (D_f H) D_g has coefficients in J_1.
E(f), E(g) lie in J_1, so E(A) is in J_1 (s=0 case). For a generator
D_f^i D_g^j H with i+j <= s, E of it is a J_1-combination of order i+j+1
derivatives; Leibniz on products keeps everything in J_{s+1}. Hence
E^k f, E^k g lie in J_k.

Spectral projection. On polynomials of total degree <= D the E-eigenvalues
are j/2, 0 <= j <= D, with eigenspaces the homogeneous components. The
Lagrange product pi_1 = prod_{j != 1} (E - j/2)/((1-j)/2) has D factors,
kills every component j != 1 and fixes the degree-one component. Constant
terms of f, g (and of H) sit in the j=0 eigenspace and are killed; they
are irrelevant. So f_1 = pi_1 f and g_1 = pi_1 g are C-combinations of
E^k f, E^k g with k <= D, hence lie in J_D. Their coefficient matrix is the
Jacobian at the origin, determinant J(0) = 1, so x,y are in J_D and
R = J_D = A[D_f^i D_g^j H : 1 <= i+j <= D]. Count: sum_{s=1}^D (s+1) = D(D+3)/2.

D = 1 sanity: pi_1 = 2E, f = x, g = y, H = -xy/2, D_f H = -y/2, D_g H = -x/2,
generators 2 = D(D+3)/2. Punctured control f = x^2, g = y/(2x): J = 1,
dH = 0 by direct expansion, so every derivative of H vanishes and the
A-algebra is A itself; the proof fails exactly at the invertible linear
part (f_1 = 0) and at g not in R. Both controls CONFIRMED. The statement
proves finite A-algebra generation only; it gives no A-module finiteness,
integrality, properness, or trace retraction, and D is frame-dependent.

## 2. Two-polar criterion (CLAIM.md) — CONFIRMED, self-contained

Claim: for a Keller pair in C[x,y] with B = A[H], (1) F automorphism,
(2) B = R, (3) D_f H and D_g H in B, are equivalent.

(1)=>(2): A = R. (2)=>(3): D_f H, D_g H are in R = B. (3)=>(2): D_f(A) in A
since D_f f = 1, D_f g = 0; if D_f H in B then D_f(sum a_k H^k) =
sum (D_f a_k) H^k + sum k a_k H^{k-1} D_f H lies in B, likewise D_g. So all
D_f^i D_g^j H lie in B and Section 1 gives x,y in B.

(2)=>(1), reconstructed with ordinary algebra only. Omega_{R/A} =
(R dx + R dy)/(R df + R dg) = 0 because (df,dg) = (dx,dy)M with det M = 1.
With B = R and ker = (P) as in Section 1, the conormal sequence of
R = A[W]/(P) gives Omega_{R/A} = R dW/(P_W(f,g,H)), so P_W(f,g,H) is a
unit of C[x,y], i.e. a constant lambda != 0. Then P_W - lambda is in (P)
with W-degree below deg_W P, so it is the zero polynomial, P = lambda W +
p_0(u,v), H = -p_0(f,g)/lambda is in A, and R = B = A. Finally C[u,v] -> R,
u -> f, v -> g is surjective and injective, so F is an automorphism.
No Formanek, Wang, or normality input is used.

Scope note, not a defect: the (2)=>(1) argument never uses the radial
identity. It shows that a Keller pair with R = A[h] for ANY h in R is an
automorphism. The whole content specific to H sits in (3)=>(2), i.e. in
the generation lemma. Condition (3) reads E(f), E(g) in C[f,g,H].

## 3. Hypothesis audit — nothing REFUTED

Load-bearing, all stated in CLAIM.md: characteristic zero (P_H, P_W
nonzero; independence), R the whole polynomial ring (constant units), J = 1
exactly, one fixed frame for E, H, D. Localized control: R' = C[x,1/x,y],
f = x^2, g = y/(2x), h = 1/x gives R' = A[h], P = uW^2 - 1, P_W = 2x a
nonconstant unit, F not injective. So constant units cannot be dropped.

## 4. Out of scope

Mixed-trace section: the h_u h_v expansion and the t^2-u, s^3-v branch
example are correct hand computations; the imported "accepted trace image
S[1/u]+S[1/v]" is not reviewed here. One-polar question: not attempted.

## 5. Verdicts and post-pins

- Radial identities, commutation, a,b, E-expansion, E(H): CONFIRMED.
- E(J_s) in J_{s+1}, pi_1, R = J_D, D(D+3)/2, both controls: CONFIRMED.
- Two-polar (1)<=>(2)<=>(3), (2)=>(1) self-contained: CONFIRMED.
- No integrality/properness/membership from generation: CONFIRMED scope.

Post-pins: CLAIM.md 3576962bed4195916367c80cb57b60d6041fc7766395f55a9ca59d8031627386; discriminator b8374142f0aa8373a3126ec5c934f02b3ed1abe1dd5230a055cb22189a90309b; snapshot 33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597.

<!-- BODY-END -->
