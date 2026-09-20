# Hostile FIRST review: INVARIANT-WEB-KELLER-1 (invariant finite webs and Keller maps)

status=FINAL (hostile FIRST complete; not sealed; parent owns custody)
lane=invariant-web-first-20260920T124000Z
reviewer=Fable5.1 effortmax (requested; hosted identity not independently attested; self-reported id claude-fable-5-1)
role=hostile FIRST independent review of one frozen proof; not ideation, not a descendant
startup_utc=2026-09-20T12:41:45Z
early_draft_utc=2026-09-20T12:42:42Z
partial_saved_utc=2026-09-20T12:50:34Z
contribution_commit=3006516257882da2649f8ccbd28eabd765825d06
producer_basis=2db51ba4dae686f7bc8c60a9521ff3b8f9ec8306
hq_governance_basis=d21f44aaf3cc27090b02a6de75d54345ab5be875
reviewed_report=xmodel/invariant-web-keller-swarmHQ-root-20260920T123400Z.md
reviewed_full_sha256=2aa6cea16f98b04be251fed7a4c13bc156d271958583359be58a636a62758ede
reviewed_body_sha256=ce95a1b0455d3eeeb3ad0f9d28c58ff563109c6952ab23c9d06ae09eb396f4af (recomputed from first 11336 bytes; matches artifact.json)

## 1. Verdict

**INVARIANT-WEB-KELLER-1 is CONFIRMED at its stated conditional scope.** A polynomial
map F of the complex affine plane with Jacobian determinant c in C*, whose pullback
preserves a reduced finite algebraic k-web W on the SAME original plane, k>=1, is a
polynomial automorphism; the same holds if a positive iterate preserves such a web.
All six charged interfaces are CONFIRMED. No unsupported implication was found.

Exact dependencies: accepted INVARIANT-FOLIATION-KELLER-1 (any c, pullback-invariant
algebraic foliation given by a primitive polynomial one-form, singularities allowed,
iterate clause) and accepted RATIONAL-PENCIL-UNIFICATION-1 (any c, any nonconstant
rational pencil r(F)=phi(r), no primitivity/genus/base-point restriction), both at
their binding integration scopes; classical facts: a Keller map is etale and
quasifinite; proper plus quasifinite implies finite; a finite etale cover of A2_C is
a disjoint union of copies of A2_C (C2 simply connected, Riemann existence/GAGA).
No web existence, stabilization, finite-cover descent, necessity, JC2 or novelty
claim is confirmed or implied; none is made by the producer.

## 2. Independent reconstruction

Notation: R=C[x,y], K=C(x,y), F=(P,Q), det DF=c. A reduced k-web is a primitive
W=sum a_i u^(k-i) v^i in R[u,v] with k distinct roots in P1(Kbar). Pullback:
(F*W)(x,y;u,v)=W(F(x,y); DF(x,y)(u,v)). Preservation: F*W and W have the same
root set in P1(Kbar), i.e. DF_p maps the web directions at a generic p onto the
web directions at F(p).

Step A (constant multiplier). Substituting (u,v)->DF(u,v) acts on coefficient
vectors by Sym^k of DF (transpose action on linear forms), a matrix over R whose
inverse is Sym^k(DF^-1), also over R since DF^-1=adj(DF)/c. Hence the coefficient
ideal of F*W equals (a_0(F),...,a_k(F)). If an irreducible q divides all a_i(F), the
irreducible curve V(q) maps into V(a_0,...,a_k), which is finite because a curve
component with irreducible equation p would give p | a_i for all i (p prime, so
I(V(p))=(p)); the image is then one point, contradicting quasifiniteness. So F*W is
primitive. Two degree-k forms in K[u,v] with the same k distinct projective roots are
proportional, F*W=lambda W with lambda in K*; writing lambda=n/d reduced in the UFD R,
d divides every a_i and n divides every coefficient of F*W, so both are units:
lambda in C*. Only coprimality is used; no unit ideal, properness or surjectivity.

Step B (discriminant). Over a splitting field W=prod_j (beta_j u - alpha_j v) and
Disc(W)=prod_{i<j}(alpha_i beta_j - alpha_j beta_i)^2, which agrees with the classical
a_0^(2k-2) prod (r_i-r_j)^2 when a_0 != 0 (the prod beta_j^(2k-2) factors cancel).
Substituting (u,v)->M(u,v) multiplies each row pair's 2x2 determinant by det M,
giving det(M)^(k(k-1)) over the k(k-1)/2 pairs; scaling W by a scales one row and
hits k-1 pairs, giving a^(2k-2). These are identities of polynomials with integer
coefficients, valid over any ring, roots at infinity included. Since Disc is a
polynomial in the a_i, Disc(coefficients a_i(F))=Delta(F). Applying both to (1):
c^(k(k-1)) Delta(F) = lambda^(2k-2) Delta. Checks: k=2, W=uv, F=(ax,by): Delta=1,
lambda=ab=c, c^2=lambda^2. F=(y,x): c=-1, lambda=1, (-1)^2=1. k=3, W=uv(u+v),
F=(ax,ay): Delta=1, c=a^2, lambda=a^3, a^12=a^12. W=u^2-v^2, F=(ax,-ay): c=-a^2,
lambda=a^2, Delta=4, a^4=a^4.

Step C (branches). Delta != 0 because W is reduced (k>=2). If Delta is nonconstant,
Delta(F)=mu Delta with mu=lambda^(2k-2)c^(-k(k-1)) in C*, a preserved nonconstant
polynomial pencil with phi(t)=mu t; the accepted pencil theorem gives automorphy.
If Delta in C*: for k>=2 Disc is homogeneous of degree 2k-2>=2 in the coefficients,
so at EVERY point the specialized form is nonzero with k distinct roots in P1
(no coefficient-base points). H={W=0} in A2 x P1 is closed, the projection is
projective, fibers are k reduced points, so proper plus quasifinite gives finite.
In chart v!=0 (t=u/v) or u!=0 (s=v/u, covering the root [1:0]) a simple root has
nonzero t- or s-derivative, so the Jacobian criterion makes H->A2 etale at every
point. Finite etale of degree k over the whole A2 (A2 connected), hence H is the
disjoint union of algebraic connected components H_i, each irreducible (H smooth),
each with connected analytification (SGA1 XII 2.4, implicit in the producer's
text), each a finite covering of simply connected C2 of degree 1, so finite etale
of degree 1, i.e. an isomorphism onto A2 (rank-one locally free with unit section;
or birational finite onto normal A2). H_i is the graph of a section sigma_i:A2->P1,
i.e. [u_i:v_i] with u_i,v_i in R without common zero (Pic(A2)=0), so
omega_i=v_i dx - u_i dy is a nonzero primitive polynomial one-form, a regular
algebraic foliation on the ORIGINAL plane; no branched cover is involved.

Step D (permutation). Phi((x,y),[u:v])=(F(x,y),[DF(x,y)(u,v)]) is a morphism of
A2 x P1 because DF is invertible everywhere; (1) evaluated pointwise sends H to H.
Phi(H_i) is connected so lies in one open-closed H_sigma(i); the index is constant.
At any single point p, DF_p maps the k distinct directions over p injectively into
the k directions over F(p), so i->sigma(i) is injective, hence a permutation;
surjectivity of F is not used. With m=ord(sigma) (dividing k!), Phi^m is the direction
map of F^m and sends each H_i to itself, i.e. D(F^m)_p(u_i,v_i)(p) is proportional to
(u_i,v_i)(F^m p) at every p, so (F^m)*omega_i annihilates the direction field of
omega_i and equals rho omega_i, rho in K: pullback invariance exactly as the accepted
foliation theorem defines it. Its iterate clause gives F an automorphism.

Step E (k=1, iterates). For k=1, W=a_0 u+a_1 v is itself a primitive one-form (u,v <->
dx,dy) and the web pullback is the one-form pullback, so preservation is foliation
preservation and the accepted theorem applies directly. If F^m preserves W, F^m is
Keller with determinant c^m, so F^m has a polynomial inverse G; G commutes with F
(F=G F F^m gives F G=G F), so G F^(m-1) is a two-sided polynomial inverse of F.

## 3. Interface verdicts

1. CONFIRMED. Any algebraic k-web on A2 (a symmetric k-differential over K with k
   distinct generic roots) becomes primitive polynomial W after clearing denominators
   and the coefficient gcd; isolated base points remain allowed. Sym^k(DF) invertible
   over R; quasifiniteness preserves gcd 1; lambda constant by the reduced-fraction
   argument using coprimality only. Control (x^2,y), W=uv: F*W=2xW, non-Keller, as stated.
2. CONFIRMED. Delta != 0 for k>=2 by reducedness; identity (3) with exponents
   k(k-1) and 2k-2 verified as above, including nonmonic forms and roots at
   infinity (projective determinant form of Disc), factors over a splitting field
   (polynomial identity), and repeated special roots (zeros of Delta, which form a
   preserved curve in the nonconstant branch). The accepted pencil criterion applies
   with r=Delta, phi(t)=mu t; Delta need not be irreducible, primitive or smooth.
3. CONFIRMED. Delta in C* excludes coefficient-base points and root collisions at
   every point; both P1 charts retain infinite slope; fibers are reduced k-point
   schemes; properness is that of the projection A2 x P1 -> A2 restricted to closed
   H, not of F; etaleness by the Jacobian criterion, so flatness and multiplicity
   questions do not arise. Algebraic splitting follows: connected components of the
   finite etale H are algebraic and open-closed, their analytifications are connected
   coverings of C2, hence degree one, hence isomorphisms. Riemann existence and
   connectedness of analytifications are the only inputs beyond simple connectivity.
4. CONFIRMED. Sections give regular primitive one-forms on the original A2;
   constant index by connectedness; permutation by pointwise injectivity of DF_p
   on the k-point fibers; an iterate fixes each sheet and preserves the foliation in
   the pullback sense. This is a foliation on A2 itself, not on a branched cover,
   and the web is the same on source and target (F*W=lambda W), not a moving web.
5. CONFIRMED. k=1 reduces verbatim to the foliation theorem. Iterates: F^m is
   Keller; automorphy of F^m gives a polynomial inverse of F. The two dependencies
   are used exactly at their binding scopes (any c; polynomial pencil with Mobius
   phi; regular primitive foliation preserved by an iterate). Neither dependency
   uses webs, so there is no circularity. No new classification or source import.
6. CONFIRMED. All four Section 7 controls recomputed: (ax,by) and (y,x) on uv
   (exponents; genuine sheet swap); v^2-xu^2 is primitive, reduced, Delta=4x,
   branched over x=0, and is routed to the pencil branch, not asserted to split;
   (x^2,y) shows nonconstant multiplier; F=(x+y^2,y) pulls uv(u+v) back to
   (u+2yv)v(u+(2y+1)v), roots [-2y:1],[1:0],[-(2y+1):1], not the standard web. The
   stated exclusions are correct and complete: sufficiency only, no invariant web
   for a hypothetical noninvertible map, no direction-orbit growth bound, no
   invariant line on a cover, no algebraization. Nothing further is appended.

## 4. Attacks tried without finding a gap

- Nonconstant lambda in (3): would break the pencil; excluded by Step A.
- Zero binary form at a point when Delta in C*: impossible, deg Disc=2k-2>=2.
- k=1 with the discriminant route: Disc trivial, so k=1 is correctly routed away.
- Etaleness of a projective non-finite map: not needed; properness plus finite
  fibers gives finiteness first.
- Non-Galois-stable direction sets: not algebraic webs on A2; excluded by the
  definition of W over R, which is the theorem's stated hypothesis.
- A component H_i mapping onto a different H_j for different base points: excluded
  by connectedness; injectivity of sigma needs only one base point.
- Preservation only up to a rational function for the split foliation: pullback
  invariance is defined up to a rational scalar, so nothing is lost.
- FALLACY-v2 ring-map item: the coefficient ring R, tangent coordinates u,v, the
  substitution (u,v)->DF(u,v) and the identification u,v<->dx,dy are declared. No
  exit-price claim is made, so no charge_basis line is required.

## 5. Dependencies, scope, custody

Dependency status at the producer basis: INVARIANT-FOLIATION-KELLER-1 is promoted
by commit 2db51ba4 ("Promote invariant-foliation Keller criterion after independent
FIRST"; APPROACHES snapshot lines 367-381) and RATIONAL-PENCIL-UNIFICATION-1 is
PROMOTED/MANUAL (APPROACHES lines 383-398). The producer's Section 8 pins of the
foliation producer, foliation integration and pencil integration equal the charged
input hashes. Neither dependency was re-audited: no specific doubt affecting this
use arose. Favre--Pereira Corollary B and the pencil theorem's curve, Stein,
hyperbolic-moduli and no-A1 imports remain inherited through those integrations.

Read scope: all ten charged snapshots whole-read, pre- and post-read SHA256 equal to
the charged list; the four HQ governance documents whole-read via git show at basis
d21f44aa with all four pins matched. Omitted: mutable STATE, live peer payloads,
additional history, the uncharged earlier Bass/web source-fit report, the uncharged
foliation FIRST report and the Favre--Pereira PDF. No network, source retrieval, CAS,
science code, delegation, jc2-lean/jc2-web access, protected access or Git mutation.
Tools run: date, command -v/test -x, sha256sum, head, git ls-tree/show on swarmHQ at
the pinned basis with submodule recursion disabled, and the trusted
ops/open_collision.py under python3 -B (stdlib-only imports; no bytecode written).

Delivery deviations: the first apply_patch of the ACK (stdin form) and the first
attempts of both the early draft and the partial failed on a missing End Patch
line; each was repaired within a minute, the draft before evidence reading and the
partial before its deadline. The harness persisted two oversized tool outputs (the
dependency reports and APPROACHES) to its own tool-results cache; these are
harness-owned display files, not authored outputs, and were read in place. Authored
outputs are the 444 ACK and this report only. CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 was
observed; absence of other side effects is self-reported, not externally certified.
Model identity and cost are self-reported. Promotion is AUDIT's decision; this file
is not sealed.

## 6. Read manifest (excluded from word count)

charged inputs (pre-read = post-read SHA256, /tmp/jc2-lane.40Lo7P/inputs):
7181a9dd4cf928e5327ee5324ccf7861098e2b7321395852418aa8c7808fbbdf README.md
31f54fa5b1a9f76dc5455dd6c42615e565b47b96499c6fc69f389980e762a96f AGENTS.md
9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e COORDINATION.md
4262aa32ae05f6328c0d377d7becffa42613bd9bf930655f543c2925bd556b1d APPROACHES.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5 FALLACY-v2.md
2aa6cea16f98b04be251fed7a4c13bc156d271958583359be58a636a62758ede invariant-web-keller-swarmHQ-root-20260920T123400Z.md
d215629ce966ef0b9b9d8e78a3870468e1ada9384c2434950afd14e01b5161e6 invariant-web-keller-swarmHQ-root-20260920T123400Z.md.artifact.json
1ccc0fc8d9f70ca9d9743efee2d63aa5d390219f0f87fb045be88d543e7a9054 invariant-foliation-keller-swarmHQ-root-20260920T100525Z.md
5bf434b3d273ffaf5cecbae754556553e0f27f8b5c3058edea84dd0b1e335a16 invariant-foliation-first-integration-swarmHQ-root-20260920T103300Z.md
433840900e0edd661cce65557e1f05b8fbf8acc4dd00f90ece863c9d82896926 rational-pencil-unification-integration-swarmHQ-root-20260920T040300Z.md
HQ governance at d21f44aaf3cc27090b02a6de75d54345ab5be875 (git show, hashes matched):
06ba4c0898c8a4272478b16f8b72f2877cf235ed3a8af5016059d1114dd0c34f AGENTS.md
29d6bcea7ed4fa1031846705c765ce27f487f76ea330c6312cbad6ca38c42393 POLICY.md
710fcf0c3b2bfca649677365fb4094b6527f172981016696ee67095fca910778 RESEARCH_POLICY.md
67f2cbffb19b407f7c9094de193f43ba28fd4c960b9509745d4c007b73557c81 RUNBOOK.md

## OPEN(S) RAISED

None. No web-existence, classification, control-family or descendant task is raised.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Trusted `python3 -B ops/open_collision.py <this-report> --root .` returned EMPTY on
the partial (12:51:00Z) and again on this final body (12:53:40Z); it checks
recorded identifiers, not novelty or mathematical correctness.

Author completion: 2026-09-20 12:53:56 UTC, after whole-body readback, post-read
input hash check and the trusted collision check.

<!-- BODY-END -->
