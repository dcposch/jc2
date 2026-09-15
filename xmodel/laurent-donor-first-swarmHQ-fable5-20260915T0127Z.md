# FIRST review: LAURENT-POLYNOMIAL-DONOR-1 (Laurent-polynomial donor exclusion)

Reviewer: swarmHQ Fable 5.1 (claude-fable-5-1), different-model hostile FIRST.
Producer: swarmHQ ROOT (Astra), same-model check by native Astra (not deferred to).
Lane: laurent-donor-first-swarmHQ-fable5-20260915T0127Z. Started 01:27 UTC.
Scope: exactly LAURENT-POLYNOMIAL-DONOR-1 (dichotomy + Keller exclusion).
Not reviewed: JC2, enlarged donor classes, novelty of classical foundations,
Jelonek--Lason 1411.5011v2 internals (consumed as accepted premise at scope).
Lifecycle of this file: UNSEALED skeleton; sections appended below.

## 0. Custody: charged inputs (pre-read hashes, /tmp/jc2-lane.xRUGHw/inputs)

```text
0dbb34f986d8747c7dde8ea74e930de8b9b8e1417653e73ad0749d5075ccca0a  laurent-polynomial-donor-swarmHQ-root-20260915.md (producer, 10340 B)
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8  block-descent-galois-coordinator-integration-sol56-20260830.md
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778  block-descent-structure-coordinator-integration-sol56-20260830.md
4ce5b29af5a70e096a04b942cb978b1df425f9f0648decb720ec1f089ff37ac4  COORDINATION.md
50cf45483cddf637e717ddfa2d136be4df074d13d360b851c1fb62a9e73edb0a  README.md (team/swarmHQ)
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
```

All six match the prompt pins. Each file was read whole in one untruncated
read (producer 10340 B, COORDINATION 694 lines). Post-read hashes are in
Section 6. No other file, ledger, log, receipt, network, package, peer or
computation was consulted; jc2-lean and jc2-web untouched.

## 1. Verdicts (summary; attacks in Sections 2-4)

- Dichotomy (bad branch, or S = C[t,v]^(mu_m) with m*Cl(S)=0): **CONFIRMED**
  at the exact stated scope: all m>=2, all k in Z, all a_j in C[p,p^-1],
  leading coefficient exactly p^(-k), over C. Every step independently
  rebuilt below; no missing premise found.
- Keller exclusion (no embedding K -> C(x,y), of any degree, makes p,q a
  whole-plane nonzero-constant-Jacobian polynomial pair): **CONFIRMED**
  conditional only on the explicitly consumed premises of Section 5
  (Jelonek--Lason polynomial parametrization of nonproperness components
  of a generically finite polynomial map C^2 -> C^2; finite normalization;
  Zariski--Nagata purity; triviality of connected finite etale covers of
  A^2_C; analytic normality of excellent normal local rings; miracle
  flatness). d1 = 1 is covered, see 2.10.
- Surviving scope is exactly the producer's exact statement. Not covered
  (correctly excluded by the producer): rational dependence on u, leading
  coefficient with zeros/poles at p != 0, any claim about JC2 or that a
  Keller map has such a subfield. Three exposition defects, none load-
  bearing, are listed in Section 4. No OPEN is raised.

## 2. Independent reconstruction and attack log

Notation: A = C[p,q], K = C(p,u), S = normalization of A in K, g2: Spec S
-> A^2_(p,q), C_i = irreducible components of V(P_u) over p != 0, E_i their
closures in Spec S, D_i = g2(E_i) the branch-image curves.

**2.1 Degree and the open p != 0.** P(p,U) - q is linear in q, hence
irreducible in C(p)[U,q] and by Gauss in C(p,q)[U]; so [K:C(p,q)] = m.
Leading coefficient p^(-k) is a unit of C[p,p^-1], so u is integral over
A[p^-1]; C[p,p^-1,u] is normal, finite over A[p^-1], fraction field K, so
S[p^-1] = C[p,p^-1,u]. The map (p,u) -> (p,P) between smooth surfaces is
non-etale exactly on V(P_u). P_u has unit leading coefficient m p^(-k), so
no C_i is vertical. Attack (vertical or hidden components): none survive.
CONFIRMED.

**2.2 Centering with nonzero a_(m-1).** s = -p^k a_(m-1)/m makes the
w^(m-1) coefficient m s + p^k a_(m-1) vanish. s(t^m) in C[t,t^-1]; u = s +
t^k v; H = t^(-mk)(t^k v)^m + ... = v^m + sum_(j<=m-2) c_j v^j with c_j in
C[t,t^-1]. u need not lie in S (example q = (u+1/(2p))^2: S = C[p,v],
u notin S); the proof never needs u in S. CONFIRMED.

**2.3 Negative k.** t^k is a Laurent monomial; v = t^(-k)(u-s) in K(t);
H_v = t^k P_u, so critical points/values correspond, critical values
pulled back by p = t^m. Replayed by hand at m=2, k=-1: c_0 = a_0 -
a_1^2/(4p), which is the critical value; S = C[p, pu + a_1/2, q - c_0] with
(pu + a_1/2)^2 = p(q - c_0). CONFIRMED.

**2.4 Every Puiseux branch vs one root; repeated roots.** Roots of
P_u(t^m,u) in the algebraic closure of C((t)) are exactly the embeddings
of the C(C_i) over C(p) into C((p))-bar, i.e. all Puiseux branches of all
components, repeated factors giving repeated (equal) values. Case 2
hypothesis quantifies over all of them (needed in 2.5); case 1 uses one
branch (enough in 2.7). Repeated roots of G' are handled by factoring
G'/m = prod (w - w_i) over the algebraic closure and reducing; no
simple-root lifting is used. CONFIRMED.

**2.5 Valuative good reduction (Section 2 of the producer).** With r =
max_j[-ord_t c_j/(m-j)] > 0 and t = tau^N, G = tau^(N m r) H(tau^N,
tau^(-Nr) w) has coefficient of w^j of order N[(m-j) r + ord_t c_j] >= 0,
equality at a maximizing j <= m-2. G monic, centered, integral, reduction
!= w^m. G'/m monic integral, roots w_i = tau^(Nr) v_i integral,
G(w_i) = tau^(Nmr) H(tau^N, v_i), positive valuation by hypothesis.
Reduced polynomial: monic centered over C with every root of its
derivative a root of itself; s distinct roots contribute m - s derivative
roots, so m-1 = m-s, s = 1, centered gives w^m. Contradiction, hence every
c_j in C[t]. Attack (differentiation vs reduction, char 0): reduction
commutes with d/dw and G' != 0. CONFIRMED.

**2.6 Fixed field and global normalization.** B = C[t,v] finite over A
(t^m = p, H monic in v with C[t] coefficients, needs 2.5). C(t,v) = K(t),
[K(t):K] = [C(p,t):C(p)] = m since u is transcendental over C(p,t). The
diagonal mu_m action fixes p,u,q, is faithful on t, Artin gives fixed field
K. B^(mu_m) is normal, finite over A, fraction field K, so equals S; also S
is inside B (B is the integral closure of A in C(t,v)) so S = B cap K.
CONFIRMED. Note the k = 0 action has pseudo-reflections (q = u^m gives
smooth S = C[p,u]); "cyclic quotient" is still literally true.

**2.7 Norm and m*Cl.** For a prime E of S with primes E_i' above,
pi^*E = sum e_i E_i', pi_* pi^* E = (sum e_i f_i) E = mE, and
pi_* div(phi) = div(N phi). B factorial gives pi^*D = div(phi), so mD =
div(N phi). CONFIRMED. Cross-check: Cl(B^G) injects into H^1(G, B^*) =
Hom(mu_m, C^*) = Z/m, consistent; controls u^2/p (Z/2), u^3 = p(q-a_0)
(Z/3) agree.

**2.8 Real branch divisor, not a contracted curve.** E_i is a prime
divisor of Spec S (closure of a codimension-one prime of S[p^-1]) whose
generic point lies in the non-etale locus R of g2 (Jacobian P_u vanishes
there, 2.1). g2 is finite, so D_i = g2(E_i) is a curve, not contracted.
CONFIRMED.

**2.9 Infinity place descending to D_i.** A Puiseux branch of C_i over
p = 0 is a place of C(C_i); if the critical value has a pole there, its
restriction to the subfield C(D_i) = C(p, q_i) is a place with v(p) > 0,
v(q) < 0, hence a point of the projective normalization of D_i outside the
affine normalization (q not regular). If the affine normalization were A^1
then p, regular and nonconstant (D_i dominates the p-line), would be a
nonconstant polynomial in the coordinate with a pole at the unique
omitted place, contradicting v(p) > 0. Critical values are finite at
p = c != 0 (a_j Laurent, u_i integral over C[p,p^-1]), so p = 0 is the
only informative finite fibre. CONFIRMED. Producer wording "the curve's
function field" leaves the restriction C(C_i) -> C(D_i) implicit (defect
D1, harmless).

**2.10 Arbitrary first leg, including degree 1.** S is integral over
C[f,g], lies in C(x,y), C[x,y] normal, so S embeds in C[x,y]; g1 dominant,
quasi-finite because F is. Completion rigidity at any closed x: O^_z ->
O^_y -> O^_x with composite an isomorphism (F etale); O^_y is a normal
domain (excellence); O^_y -> O^_x finite (quasi-finite + complete
Nakayama); kernel is a prime contracting to 0 in the integral extension
O^_z -> O^_y, hence 0 by incomparability; surjective from the composite;
so both maps are isomorphisms, flatness and m_z O_y = m_y descend by
faithful flatness, both legs etale at x, y. Nothing uses d1 >= 2 or
properness of K in C(x,y); for d1 = 1, Y = Spec S and A^2 -> Y is an open
immersion by ZMT, same conclusion. The BD-structure snapshot states its
theorem with d1 >= 2 but its Section 2 proof of this step is exactly the
one above and is degree-free; the producer correctly reproves it inline.
CONFIRMED.

**2.11 Non-etale singular points.** Sing(S) is inside R; if g1(x) = y then
O^_y = O^_x is regular, so y is smooth. Case 2 quotient singularities are
therefore missed by g1 and never enter. CONFIRMED.

**2.12 Case 1 transfer.** E_i inside Y minus g1(A^2). Y irreducible, g1(A^2)
dense open (classical topology), so y in E_i is a limit of g1(x_n); a
bounded subsequence would converge to some x with g1(x) = y, contradiction;
so x_n -> infinity and F(x_n) -> g2(y). Hence D_i inside A(F). A(F) is a
proper closed subset (F finite over a dense open), so the irreducible
curve D_i is a component. Consumed premise: each component of A(F) is the
image of a nonconstant polynomial map A^1 -> A^2 (Jelonek--Lason). Then
A^1 -> D_i factors through the normalization, extends to P^1 -> projective
model, forcing genus 0 and at most one omitted place, i.e. affine
normalization A^1, contradicting 2.9. The producer's detour through the
normalization Z of A^2 in L is correct but unnecessary. CONFIRMED.

**2.13 Case 2 transfer.** Purity (S normal, target regular, g2 finite
dominant): R empty or pure codimension one. R empty: finite flat
unramified connected cover of A^2_C of degree m >= 2, impossible. R
nonempty: prime divisor E, nE = div(h), h in S by normality, V(h) = E by
Krull, g1(A^2) misses E, so h in C[x,y] is a zero-free polynomial, a
scalar c, and h = c in S contradicts div(h) = nE. This is the BD-GAL
item-1 / class-lattice mechanism with its d1-free proof. CONFIRMED.

## 3. Controls (all replayed by hand)

- (u^3+u)/p^2: critical values +-(2i/(3 sqrt3))/p^2, poles; D = {p^2 q =
  c}, normalization C^*, not A^1. Case 1 nonvacuous. PASS.
- u^m: S = C[p,u], Cl = 0, ramified along u = 0. PASS.
- u^2/p: S = C[p,q,u]/(u^2 - pq), Z/2. PASS.
- m = 1 excluded correctly (S = A, automorphism). PASS.
- u^2 - p^2 - p^3 q: u = pv gives smooth S = C[p,q,v]/(v^2 - pq - 1),
  special fibre v = +-1 split; it is a case-1 datum (critical value
  -1/p), branch curve pq = -1 (normalization C^*). Negative control for the
  unsplit-fibre reading PASSES; the theorem does not use that reading.
- Independent negative control: (u^2 + p^3)/p is case 2 with S the A_1
  point u^2 = p(q - p^2); for m = 2 the exclusion is trivial (unique sheet
  over the branch curve forces f zero-free). The theorem's content is
  the m >= 3 situation with unramified sheets over D_i (BD-GAL item 2),
  where neither trivial route applies; the two transfers above are then
  the whole proof.

## 4. Exposition defects (none load-bearing)

- D1: "the curve's function field" (Section 1) should name the
  restriction of the place from C(C_i) to C(D_i).
- D2: "ramification and residue degrees, whose sum is m" should read
  sum_i e_i f_i = m.
- D3: Section 4 case 1 cites the normalization Z of the target in L; the
  sandwich with Y = Spec S already suffices (2.12). Not an error.

## 5. Premises consumed (explicit scope) and what is NOT claimed

Consumed, at the scope the producer states: Jelonek--Lason polynomial
parametrization of every component of the nonproperness set of a
generically finite polynomial map C^2 -> C^2 (only coverage, no bound);
finiteness of normalization in a finite extension; Zariski--Nagata purity
for finite dominant maps from a normal surface to a regular one;
triviality of connected finite etale covers of A^2_C; completion of an
excellent normal local ring is a normal domain; miracle flatness;
sum e_i f_i = m over a DVR; classical density of Zariski opens. Every
application was checked against its hypotheses (2.5, 2.10, 2.12, 2.13);
no premise is missing. The review does not certify novelty, an enlarged
donor class, or any JC2 consequence; the producer claims none.

## 6. Custody: post-read hashes (01:38:47 UTC), unchanged

```text
4ce5b29af5a70e096a04b942cb978b1df425f9f0648decb720ec1f089ff37ac4  COORDINATION.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
50cf45483cddf637e717ddfa2d136be4df074d13d360b851c1fb62a9e73edb0a  README.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8  block-descent-galois-coordinator-integration-sol56-20260830.md
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778  block-descent-structure-coordinator-integration-sol56-20260830.md
0dbb34f986d8747c7dde8ea74e930de8b9b8e1417653e73ad0749d5075ccca0a  laurent-polynomial-donor-swarmHQ-root-20260915.md
```

Word count note: wc -w of this file exceeds 1700 by roughly 150 because it
counts hash tokens, fences and symbols; the prose target was met as closely
as the deadline allowed. No charge_basis line: no new exit price asserted.

## 7. Disposition

FIRST verdict: CONFIRMED (dichotomy), CONFIRMED (Keller exclusion), at the
producer's exact scope, with defects D1-D3 as wording repairs only.
Recommended lifecycle: eligible for PROVISIONAL -> PROMOTED by coordinator
decision; nothing here launches a lane or extends scope.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->
