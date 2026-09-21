# Hostile FIRST audit: actual additive quotient and one-point scheme criterion

STATUS: audit body complete; completion footer appended after whole-author readback

Evidence tier of the audited claims: MANUAL with named classical imports. Hostile FIRST
verdict: all nine requested interfaces CONFIRMED at the report's exact conditional scope;
no unsupported implication found; the report proves no scheme neighborhood, no
separatedness, no properness and no JC2, and says so. Two citation-precision notes and
one reviewer deviation (my own failed primary-source read) are recorded below.

- author: Fable 5.1 (model id claude-fable-5-1), hosted; identity not independently attested
- task: keller-additive-quotient-first-20260921T013000Z
- started_utc: 2026-09-21T01:31:22Z
- audited: xmodel/keller-additive-quotient-swarmHQ-root-20260921T012300Z.md (frozen snapshot)
- contribution_commit: a450b715198107cfdc219256985756e4e5acffb9
- producer_basis: ee7e771e975e0244ad33fb154da9fd793d97a0d6
- hq_governance_basis: 47931f09369a6e1a522217f954b75955280b0349
- scope: one frozen proof audit; no quotient classification, no positive-premise search, no JC2 claim

## Pin manifest (pre)

All seven charged snapshots under /tmp/jc2-lane.YEzFKm/inputs were hashed before reading
(01:33 UTC) and every sha256 MATCHES the prompt pin:

- README.md 7181a9dd4cf928e5327ee5324ccf7861098e2b7321395852418aa8c7808fbbdf (5391 B)
- AGENTS.md 31f54fa5b1a9f76dc5455dd6c42615e565b47b96499c6fc69f389980e762a96f (1229 B)
- COORDINATION.md 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e (6042 B)
- APPROACHES.md 5b8df1534c2540629b2264b0cd54086aef084f647f8f062a9c36e28fdbe446db (50597 B)
- FALLACY-v2.md e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5 (1985 B)
- keller-additive-quotient-swarmHQ-root-20260921T012300Z.md 19d4f01376692efcd87b839dbbd088625b66c26e1bf5db94ecf98d8421b4ad3e (13347 B; artifact.json records body 13014 B, body sha256 dd57fcc5f09e476fba7ccc45585b40302ff471c035be2e4847a37cff974ed7d5, frozen basis ee7e771e)
- ...artifact.json 634e2e29dc229c07da5fe41e52ee56c7bf44df00109902a5732c01b45a424b8c (711 B)

HQ governance at 47931f09369a6e1a522217f954b75955280b0349 via `git show` (read-only), all MATCH:
AGENTS.md 06ba4c08... (1520 B), POLICY.md 29d6bcea... (5412 B), RESEARCH_POLICY.md 710fcf0c... (7008 B),
RUNBOOK.md ac18350c... (15416 B). Post pins are recorded at the end of this report.

## Verdicts on the nine interfaces

Reconstruction used throughout: F=(P,Q), det DF=c in C*, V=A5_(t,w,a), G=Ga^2,
Phi_b(t,w,a)=(t,w+tb,a-Delta(t,w,b)) with Delta=(F(w+tb)-F(w))/t, Y=F(w)+ta. Every
computation below was redone by hand from the frozen text; no CAS was used.

**1. Action, LNDs, scheme-theoretic freeness: CONFIRMED.** Delta is polynomial since every
Taylor term of F(w+tb)-F(w) carries t^|alpha| with |alpha|>=1, and Delta(0,w,b)=DF(w)b.
Telescoping gives Phi_b Phi_d=Phi_(b+d), Phi_0=id, so this is a polynomial Ga^2-action.
Differentiating at b=0 gives D_i=t d/dw_i - P_(w_i) d/da_1 - Q_(w_i) d/da_2. I recomputed
[D_1,D_2] on generators: zero on t,w_j; on a_1 both orders give -t P_(w_1 w_2), likewise
for a_2. D_i^k(a_j)=-t^(k-1) d^k F_j/dw_i^k, so each D_i is locally nilpotent. Freeness over
an arbitrary C-algebra R: the stabilizer of (t,w,a) in R^2 satisfies t b=0 and
Delta(t,w,b)=0. Expanding, Delta=DF(w)b + sum_(|alpha|>=2) d^alpha F(w) t^(|alpha|-1)
b^alpha/alpha!, and each higher term contains a factor t b_j, hence vanishes in R. DF(w)
is invertible over R (adjugate divided by c), so b=0. This holds for nonreduced R, so
G x V -> V x V is a monomorphism, which is the Stacks notion of a free action.

**2. Invariant ring C[t,Y]: CONFIRMED.** On V[1/t] the functions (t,Y,w) are coordinates
because a=(Y-F(w))/t, and D_i=t d/dw_i there; in characteristic zero the common kernel is
C[t,t^-1,Y], and t,Y_1,Y_2 are algebraically independent. Minimal denominator: an invariant
f in O(V) equals t^-k H(t,Y) with H(0,Y) nonzero when k>=1; then t^k f=H(t,F(w)+ta) lies in
t O(V), so H(0,F(w))=0 in C[w], impossible because P,Q are algebraically independent (their
Jacobian is nonzero). Hence k=0. Invariants of the action are the common kernel of the
generating LNDs, so O(V)^G=C[t,Y].

**3. Quotient, torsor, base change, diagonal, smoothness, dimension, irreducibility:
CONFIRMED.** The free-action lemma needs G flat and locally of finite presentation over
the base and a free action; G=Ga^2 over C and item 1 supply both, so X=V/G (fppf sheaf
quotient) is an algebraic space and p is a G-torsor. Invariant base change: for any Z->A3,
the presheaf map (V x_A3 Z)(T)/G(T) -> V(T)/G(T) x_A3(T) Z(T) is bijective and
sheafification commutes with fiber products. Diagonal: V x_(X x X) (V x V)=V x_X V, which
is G x V by freeness plus the sheaf-quotient definition, mapping to V x V by
(b,v)->(v,Phi_b v); this is a morphism of affine schemes, and affineness is fpqc-local on
the target, so Delta_X is affine and X is quasi-separated. Nothing here makes Delta_X a
closed immersion. p is smooth of relative dimension 2 since G is smooth, so smoothness and
local finite type of X over C descend (both are local on the source for the smooth
topology); quasi-compactness follows from surjectivity; dim X=5-2=3; |X| is the continuous
surjective image of irreducible |V|, so X is irreducible and t!=0 is dense.

**4. The four morphisms and fibers: CONFIRMED.** Over t!=0, (t,Y,s=w/t) are coordinates
on V[1/t] (inverse w=ts, a=(Y-F(ts))/t), the action is s->s+b, so X[1/t]=Gm x A2_Y and h is
an isomorphism there. At t=0, V_0=A4_(w,a) with action (w,a)->(w,a-DF(w)b); r=-DF(w)^-1 a
is a polynomial coordinate change making it translation in r, so X_0=A2_w and
h_0=Y|_(t=0)=F(w). Fibers: q over (lambda!=0,Y_0) is an A2_w (a is determined); q over
(0,Y_0) is F^-1(Y_0) x A2_a, possibly empty; h over (0,Y_0) is the finite, possibly empty,
scheme F^-1(Y_0); pi has geometric fiber A2 over every geometric point, by the same
base-change-compatible computation. Surjectivity of F or h is neither used nor asserted,
and no finiteness of h is claimed.

**5. Explicit chart Theta, descent, coverage, h etale: CONFIRMED.** S x_X V = S x_V (V x_X V)
= G x S, and its projection to V is Phi_b(t,u,0)=(t,u+tb,(F(u)-F(u+tb))/t)=Theta, so the
displayed square is cartesian. Determinant: with t fixed, the 4x4 block for (u,b)->(z,u)
is [[I,tI],[I,0]] with determinant +t^2, and (z,u)->(z,(F(u)-F(z))/t) contributes
det DF(u)/t^2=c/t^2, so det DTheta=c on t!=0, hence identically. Independent check at t=0:
Theta(0,u,b)=(0,u,-DF(u)b) has block-triangular Jacobian with determinant
det(-DF(u))=c for 2x2 blocks; sign positive both ways. A polynomial self-map of A5 with
unit Jacobian is etale, and etaleness is fppf-local on the target, so g is etale.
g_0=id on A2_u, so g(S) contains X_0; when F is not surjective, g(S) misses points of U,
so including U is necessary and the report does so. h g=(t,F(u)) and h|_U are etale and
{S,U} is an etale cover of X; etaleness is etale-local on the source, so h is etale with
no separatedness hypothesis on h or X. h is an isomorphism over the dense open t!=0.

**6. One-point Zariski scheme neighborhood forces F birational: CONFIRMED.** For x in X_0
with a scheme open subspace W, an affine open V_0 of W containing x is an open subspace of
X. h|V_0 is etale (restriction), quasi-compact between affines hence quasi-finite,
separated because V_0 is affine, of finite type, with qcqs target A3. V_0 is a nonempty
open of irreducible |X| and is smooth, hence integral; V_0 meets U and h maps V_0 cap U
isomorphically onto an open of A3, so C(V_0)=C(t,Y). ZMT applies in either the
integral-normalization form or its finite-factorization corollary: V_0 is open in an
integral scheme T' finite (or integral) over A3, O(T') sits in C(t,Y) integrally over
C[t,Y], and normality of the polynomial ring gives O(T')=C[t,Y]; so h|V_0 is an open
immersion. Base change along {t=0}: V_0 x_A3 {t=0}=V_0 x_X X_0=V_0 cap X_0, a nonempty
open of A2_w containing x, and the induced map is F; an open immersion from a dense open
of A2_w into A2_Y gives C(w)=C(P,Q). The etale chart is not substituted: for S the map
(t,F(u)) has degree N and normalization yields no contradiction; birationality is exactly
what the Zariski-open V_0 supplies. No local separatedness of X beyond V_0 affine is used.

**7. Birational Keller endpoint: CONFIRMED.** F is etale hence quasi-finite, separated
since A2 is affine; ZMT, closure and normality of C[Y] make F an open immersion onto an
open W isomorphic to A2_w. If A2_Y - W contained a divisor V(f) with f irreducible, f|_W
would be a unit of O(W)=C[w], hence constant, but f is nonconstant on the dense open W.
So the complement has codimension at least 2. For g=A/B in lowest terms in O(W) with B
nonconstant, an irreducible factor B_1 gives a curve V(B_1) meeting W along which g has a
pole; so O(W)=C[Y] and F^* is a ring isomorphism. Surjectivity is derived, never assumed.

**8. Translation coordinates, collision arcs, properness, equivalences: CONFIRMED.** With
G_0=F^-1 polynomial, s=(w-G_0(Y))/t is polynomial (numerator vanishes at t=0), the inverse
(w,a)=(G_0(Y)+ts,(Y-F(G_0(Y)+ts))/t) is polynomial, I checked both compositions are
identities, and the action becomes s->s+b, so X=A3 and the action morphism is an
isomorphism onto the closed subscheme {t=t',Y=Y'} of V x V, hence proper. Collision arcs:
for u!=v with F(u)=F(v), the w-coordinate forces b=(v-u)/t, which lies in C((t))^2 but
not C[[t]]^2, so the existence part of the DVR valuative criterion fails for the finite-
type action morphism over a Noetherian base, and it is not proper. Independent check: the
image of the action morphism contains ((t,u,0),(t,v,0)) for all t!=0 but not the limit
point at t=0, so the image is not closed and the map is not proper. Generic finite-etale
locus: a dominant quasi-finite morphism of integral varieties is finite over a nonempty
open Omega of the target (generic finiteness, a ZMT corollary), and finite etale there of
constant degree N=[C(w):C(Y)]>=2 when F is not birational, so closed fibers over Omega
have N distinct points; no global finiteness is used. Closure of the equivalences:
automorphism => translation coordinates => X affine => X a separated scheme => some
special point has a scheme neighborhood => F birational (item 6) => automorphism (item 7);
X separated => action proper because the action morphism is the base change of Delta_X
along V x V -> X x X; proper action => birational => automorphism.

**9. Controls and no stronger conclusion: CONFIRMED.** F=id gives Y=w+ta, s=-a. For the
non-Keller F=(w_1^2,w_2), Delta(0,w,b)=(2w_1 b_1,b_2) has stabilizer Ga in b_1 at w_1=0, so
freeness genuinely uses the constant unit Jacobian. The report proves exactly the
conditional equivalences and states that none of the positive conditions is established.
Under hypothetical noninvertibility the same equivalences show X is a smooth non-separated
non-scheme algebraic space with affine diagonal and an explicit etale chart; that is a
structural fact, not a counterexample and not a JC2 conclusion.

## First unsupported implication

NONE found. Each displayed implication is supported by the text or by a named classical
import whose hypotheses are met. Citation-precision notes, not gaps: (a) the report
paraphrases tag 05K0 as "open immersion followed by a finite morphism"; by my recollection
05K0 is the integral-normalization statement (matching the captured comment citing EGA
IV_4 18.12.13) and the finite factorization is the adjacent corollary for finite-type
source and qcqs target; either suffices for Sections 4 and 5, and I could not verify the
displayed text (see deviation). (b) Section 5's generic finite-etale locus imports generic
finiteness implicitly; it is standard and follows from the named ZMT. (c) "birational" for
the algebraic space X is used only as "isomorphism over a dense open"; substantive
birationality is invoked on the schemes V_0 and A2 only. Lifecycle: this different-model
FIRST supports PROVISIONAL -> PROMOTED/MANUAL for the exact conditional statement, with
the reviewer's own source-read failure recorded as a limitation of this review.

## Primary sources actually read

DEVIATION (author error, disclosed): each of the two allowed endpoints was acquired exactly
once with curl (-m 30, 01:33 UTC), both HTTP 200, effective URLs unchanged. The body bytes
were streamed only into shell-local variables; nothing was persisted. In the SAME shell call,
my tag-stripping filter used a sed line range on `<script`...`</script>` that swallowed the
page's main content, so the theorem statements and displayed proofs were NOT captured. The
one-acquisition/no-retry rule bars a second fetch, so I did not refetch. Captured scope:

- tag 06PH: title line "Lemma 80.11.7 (06PH) -- The Stacks project"; one comment (Kestutis
  Cesnavicius, 2015-02-18); "1 tag refers to this tag". Body chars 15979; sha256 of the body
  as captured by shell (trailing newlines stripped) 5d8505ccda745dad06c9eccfef119750aba0b6f46c45da420bcea05235613113;
  sha256 of the byte stream with every line newline-terminated c27771c849ad0a5608967b31a72ae308a161191e51f91c326e0879b14a17d341.
- tag 05K0: title line "Lemma 37.43.3 (05K0): Zariski's Main Theorem -- The Stacks project";
  comments by Johan and Takumi Murayama (2017-08-01) adding the reference EGA IV_4 18.12.13.
  Body chars 16722; shell-captured sha256 c54998016d99597d7a5223352bc0b33b0a21ea287ab6a800c1c545e400576f18;
  newline-normalized stream sha256 757323d0d7dd9e3bc7ec7745a98827d60394d31c8e47cd98bbe13f6f73455cc3.

Consequently the imported statements are audited below from my own knowledge of the Stacks
Project (Bootstrap chapter, quotient of an algebraic space by a free action of a flat locally
finitely presented group algebraic space; More on Morphisms, ZMT via the normalization of the
target in the source, EGA IV_4 18.12.13), NOT from a verified read of the displayed text.
The captured titles and comments are consistent with those identifications. Neither hash
certifies dependency bodies; no dependency page was read.

## Read manifest, gaps, deviations

Whole-read (bounded chunks to EOF, each tool output < 16 KiB): all seven snapshots; the four HQ
files at the pinned basis. No mutable STATE, peer payload, journal, extra corpus, jc2-lean or
jc2-web bytes were read. No Git mutation, no delegation, no CAS, no cloud. Authored files: the
444 startup ACK and this report only. Deviations: (1) the primary-source extraction failure
above; (2) the ACK was written once via apply_patch and locked 444 as instructed; (3) no
automatic persistence is known to me: CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 was observed, and
no memory, cache, scratch or download file was created by me. The collision checker was run
read-only on this report; its stdout is reproduced below.

## Pin manifest (post)

Re-hashed at 2026-09-21T01:44:05Z after all reads; every value equals the pre pin and the prompt pin:

- README.md 7181a9dd4cf928e5327ee5324ccf7861098e2b7321395852418aa8c7808fbbdf
- AGENTS.md 31f54fa5b1a9f76dc5455dd6c42615e565b47b96499c6fc69f389980e762a96f
- COORDINATION.md 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e
- APPROACHES.md 5b8df1534c2540629b2264b0cd54086aef084f647f8f062a9c36e28fdbe446db
- FALLACY-v2.md e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5
- keller-additive-quotient-swarmHQ-root-20260921T012300Z.md 19d4f01376692efcd87b839dbbd088625b66c26e1bf5db94ecf98d8421b4ad3e
- keller-additive-quotient-swarmHQ-root-20260921T012300Z.md.artifact.json 634e2e29dc229c07da5fe41e52ee56c7bf44df00109902a5732c01b45a424b8c

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

## Completion

Whole-author readback of every byte above completed at 01:45 UTC (two bounded chunks to EOF).
Measured author completion: 2026-09-21T01:44:22Z. Word count of the body is about 2200 including manifests.
Not sealed or finalized here; external legacy receipt/hash custody applies.

<!-- BODY-END -->
