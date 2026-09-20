# Hostile FIRST review: RATIONAL-PENCIL-UNIFICATION-1 (arbitrary rational pencils, polynomial Keller maps)

Reviewer seat: FIRST (hostile), different-model. Requested model Fable5.1 at
effortmax; hosted identity self-reported as claude-fable-5-1 and NOT
independently attested. Evidence tier: MANUAL, relative to the producer's
explicitly named classical and campaign imports. Lifecycle: independent
review of a PRODUCER-CHECKED/PROVISIONAL claim; promotion authority belongs
to ROOT/AUDIT. Date: September 20, 2026 UTC. Startup measured 03:45:55Z.

## 1. Verdict

Overall: CONFIRMED at the producer's stated statement-level import scope.
All six charged interfaces are CONFIRMED after independent reconstruction.
No refutation, no GAP, and no hidden circularity, exact-area dependency,
modulus dependency or lost hypothesis was found in the composition.
Nothing here certifies literature novelty, supplies a preserved pencil
for an arbitrary Keller map, extends to rational F, or bears on JC2.

Exact claim reviewed. F:A2_C->A2_C polynomial, det DF=c in C*, |c|
unrestricted; a nonconstant r in C(x,y) and a rational phi satisfy
r F=phi r. Then F is an automorphism. The iterate form holds because an
invertible F^m gives the polynomial inverse F^(m-1)(F^m)^-1.

Inherited imports retained at the producer's stated scope and NOT
re-audited: Jelonek's polynomial parametrization of nonproper components;
the no-abstract-A1-component theorem for constant-nonzero-Jacobian maps
(arXiv:0905.3939v3, Section 2(i)/Theorem 4, as recorded by the prior
FIRST); the birational Keller theorem; triviality of finite etale covers
of A2_C; the coarse-moduli/Isom/descent chain inside
HYPERBOLIC-MOVING-PENCIL-1; the accepted RATIONAL-POLYNOMIAL-PENCIL-1
theorem. No source retrieval was performed; a missing hypothesis in any
of these would propagate, but I found none missing at their stated scope.

## 2. Interface 1, primitive replacement: CONFIRMED

Resolve r on P2 to f:X->P1 with X a smooth projective rational surface;
Stein-factor X->C->P1. With pi_*O_X=O_C the Leray five-term sequence
injects H1(C,O_C) into H1(X,O_X)=0, so C=P1 and K:=C(C)=C(h). K is the
relative algebraic closure of C(r) in L=C(x,y): pi_*O_X=O_C makes K
algebraically closed in L, and K/C(r) is finite. F* is injective (c!=0
gives dominance). Since h is algebraic over C(r), F*h is algebraic over
F*C(r)=C(phi(r)), a subfield of C(r), hence F*h lies in K: hF=psi(h)
with psi in C(s). The identity R psi=phi R in C(h) and multiplicativity
of degrees give deg psi=deg phi=d; psi is nonconstant. Generic
smoothness in characteristic zero plus primitivity make the resolved
geometric generic fiber smooth and integral. The report correctly
withholds that for the affine equation a-tb until base points are gone.

## 3. Interface 2, independent pair: CONFIRMED for every c

Let h=a/b reduced, a,b independent, psi=[A:B] with coprime forms of
degree d, so V(A,B)={0}. (i) gcd(aF,bF)=1: a common prime P would map
the curve V(P) into the finite V(a,b), contradicting quasifiniteness of
the etale F. (ii) A(a,b),B(a,b) are nonzero (independence) and coprime:
their common zeros form H^-1(0)=V(a,b), finite. (iii) aF B(a,b)=bF A(a,b)
in a UFD with both pairs coprime forces aF=uA(a,b), bF=uB(a,b) for ONE
unit u in C*; no nonconstant cancellation is possible. (iv) Tower law on
L over F*L over F*H*C(u,v)=H*G0*C(u,v): N(H)N(F)=N(H)N(G0), and the finite
homogeneous G0 has N(G0)=d^2 (d directions, d radial roots each), so
N(F)=d^2. The modulus of c never enters. (v) d>1: G0(0)=0 gives
F(Z) inside Z=V(a,b); a finite nonempty Z contains a periodic z with
F^k(z)=z. F^k is etale at z, so (F^k)* induces an automorphism of the
completion C[[s,t]] preserving m-adic order: min ord(aF^k,bF^k)=ell>=1.
But HF^k=G0^kH with G0^k homogeneous of degree d^k, so both components
lie in (a,b)^(d^k), inside m_z^(d^k ell). Thus ell>=d^k ell, impossible.
Z is empty and h is a morphism on the unchanged A2. Attacks: nonreduced
ideals are irrelevant, only the ideal power and m-adic order are used;
properness of F is never used. Control (x^2,y^2), h=x/y: (i)-(iv) hold
with N=4=d^2, but F is not etale at the periodic base point 0 and
ord(x F)=2, exactly the failed hypothesis.

## 4. Interface 3, dependent pair: CONFIRMED, no generator theorem

C(a,b) has transcendence degree one and contains h, so it is algebraic
over K, and relative closure puts a,b in C(h). V(a,b) is empty: H=(a,b)
maps A2 dominantly onto an irreducible curve Gamma, every nonempty fiber
has dimension at least one, but H^-1(0,0)=V(a,b) is finite; the
normalization variant is also correct. Take a=q(h) nonconstant with a
pole v. If h^-1(v) were nonempty, the pullback of a local parameter at v
is a nonzero nonunit of the UFD O_z; along one of its prime factors
q(h) has negative order, contradicting regularity of a. So h omits v; a
Mobius M with M(v)=infinity makes p=M(h) a regular function, hence a
polynomial, with C(p)=K and pF=chi(p), chi=M psi M^-1 of degree d.
(5.1): if U(p)/V(p) is a polynomial with U,V coprime, Bezout makes
U(p),V(p) comaximal, and V(p) dividing U(p) forces V(p) a unit, hence V
constant since p is nonconstant. So chi is a polynomial of degree d and
p is primitive. I checked that no closed-generator theorem is needed at
any step; the argument lives entirely in C[x,y].

## 5. Interface 4, full-fiber comparison for a morphism: CONFIRMED

Let h:A2->P1 be primitive, hF=psi(h), deg psi=d, K=C(h), K0=sigma(K)
with sigma=F*, [K:K0]=d. L/K is regular, so sigma(L)/K0 is regular and
sigma(L) tensor_K0 K is a field of degree d over sigma(L), equal to the
compositum sigma(L)K. Hence N=[L:sigma(L)K] d=dk. Over Kbar the source
over the target chart t=a/b is the disjoint union of the d FULL fibers
h=s_i: the ring C[x,y,1/bF] tensor Kbar modulo aF/bF-t equals
Kbar[x,y,1/bF]/(prod(a-s_i b)); the factors are pairwise comaximal
because (a,b)=(1), and on a=s_i b both b and bF=uB(a,b) are units for
generic t. A point with bF=0 would have psi(h)=infinity, so no source
point of D(bF) is lost and nothing outside D(bF) is needed. Each
component is a base change of the geometric generic fiber by an
automorphism of Kbar, so it has the same (g,n); n>=1 since an affine
curve is not complete. Regularity on affine fibers gives
f^-1(S_t) inside S_s, ramification over S_t at least kn-n, and
Riemann-Hurwitz gives (k-1)(2g-2+n)<=0; only nonconstancy of the
restricted map (quasifiniteness) is used, not etaleness. delta>0 forces
k=1 and, with equal puncture counts, an isomorphism of full affine
curves. n=1: polynomial map A1->A1, finite. n=2: unit of Kbar[z,1/z],
z->alpha z^m with m!=0, finite. n>=3: k=1. Finiteness over Kbar descends
to C(t) by faithfully flat descent. Conjugacy under Gal(Kbar/C(t)),
psi(s)-t being irreducible (linear in t, A,B coprime), equalizes the
component degrees. Target is D(b), source is D(bF): CONFIRMED.

## 6. Interface 5, genus-zero morphism lemma: CONFIRMED at import scope

B'=C[x,y,1/bF]=F*(A')[x,y]. Finiteness of S^-1B' over S^-1A' with
S=C[t]-0 gives monic equations for x,y whose finitely many denominators
lie in C[t]; one q(t) clears them, so B'[1/q(psi h)]=A'[1/q(t)][x,y] is
finite. F is finite over h^-1(U), U={q!=0}, and A_F lies in the finitely
many fibers over P1-U, including the fiber over infinity; each component
of A_F is a whole component of one affine fiber. This is base denominator
clearing, not field degree. Resolving [a:b] only over the line at
infinity leaves A2 unchanged and gives f:X->P1 with geometrically
integral generic fiber; f is flat, so a general closed fiber G is a
smooth P1, nef, G^2=0, K_X.G=-2. For any scheme fiber D~G,
(K_X+D).G=-2 kills H0(K_X+D) because G is nef; Serre duality kills
H2(O(-D)); with H1(O_X)=0 the fiber sequence gives H1(O_D)=0. For a
reduced component C, the kernel of O_D->O_C has support of dimension at
most one, so H1(O_C)=0 and p_a(C)=0: C is a smooth P1. Nonreduced and
reducible D are covered, and no whole-fiber smoothness is assumed. A
component of A_F is thus P1 minus a nonempty finite set; a nonconstant
polynomial parametrization forces one puncture (two would give inverse
regular units z,1/z pulling back to constants), so it is abstractly A1,
excluded by the Keller import. Then A_F is empty; F is proper and
quasifinite, hence finite etale of degree one over simply connected C2,
hence an isomorphism. Control (x,xy), h=x: generic fiber maps finite,
A_F the line x=0, abstractly A1; only the Keller endpoint fails.

## 7. Interface 6, degree-one lemma and composition: CONFIRMED

Section 8 uses only Sections 3-6, (4.1) and RATIONAL-POLYNOMIAL-PENCIL-1.
Independent d=1 gives N=1. Dependent gives a primitive p with affine
linear chi; genus zero uses the accepted theorem (primitive polynomial,
genus zero, polynomial psi of degree >=1, any c: all met); positive genus
has delta>=1, so (6.1)-(6.2) give N=k=1. A fixed invariant has phi=id,
so its replacement psi is Mobius; degree one is all that is needed. In
Section 9 the dependent d>=2 positive-genus branch consumes ONLY the
general dominant conclusion of HYPERBOLIC-MOVING-PENCIL-1. Its
hypotheses are met: dominant F, primitive polynomial p, polynomial chi
of degree >=2, smooth full geometric generic fiber (automatic in
characteristic zero), delta>0. The conclusion supplies nonconstant r
with rF=r, and Section 8 finishes. That general conclusion depends on no
Keller, area-form, DNT or modulus input; the J=1 corollary is unused.
Dependency graph: Sections 3-8 and RATIONAL-POLYNOMIAL-PENCIL-1 do not
cite the hyperbolic theorem, and the hyperbolic theorem does not cite
them. No circularity; no lost hypothesis. Reading aid only: in the
independent d>1 branch both subcases end in a contradiction with N=d^2
(Section 7 yields N=1, positive genus yields N=d), so that configuration
cannot occur; the logic is sound and needs no change.

## 8. Non-binding observations

- Section 6's phrase "dominant etale maps" is stronger than needed;
  nonconstancy suffices for (6.2), and etaleness of the restriction is
  not used anywhere.
- Section 5's second (normalization) argument and the fiber-dimension
  argument are both valid; either alone suffices.
- The three controls behave as stated. (x^2y,xy^2): aF,bF share xy,
  the lift fails, N=3 with d=1, F not quasifinite, non-Keller.

## 9. Scope and exclusions retained

No pencil existence for arbitrary F, no JC2 resolution, no rational-F
extension, no assertion that every automorphism preserves a pencil, no
literature-novelty determination (ROOT owns bounded history/source
intake). This is not a new exit-price claim; no charge_basis line.

## 10. Custody, reads, limitations, deviations

Whole-read: all 13 charged snapshots by basename under
/tmp/jc2-lane.JkBDRY/inputs, pre-read sha256sum -c all OK; post-read
recheck recorded below. HQ AGENTS/POLICY/RESEARCH_POLICY/RUNBOOK
whole-read via git show at a3c3bee (resolved once, read-only, to
a3c3bee653177ee99355579448f8592bfdd43629; HQ HEAD 977879e7 not used); all
four hashes match the pins. Producer sealed body: first 18269 bytes hash
b98f5986..., matching the artifact manifest, BODY-END at line 338.
No mutable STATE, other-seat report, source discovery, history search,
network, CAS, interpreter, cloud, delegation or protected access;
jc2-lean and jc2-web untouched; Git commands read-only.
Authored outputs: the startup ACK (03:46Z, mode 444) and this report,
every edit via apply_patch. Deviation: one scratch checksum manifest was
written to /tmp/fable_expected_hashes.txt for sha256sum -c; it is not a
memory, index, settings, notes, credential, shared-doc or Git mutation.
Early draft 03:46Z; partial saved 03:55:44Z, 44 seconds after the 03:55
partial target. No tool output was clipped; no automatic persistence
observed; CLAUDE_CODE_DISABLE_AUTO_MEMORY=1. Model identity, billing and
the completeness of any external log are not certified by this text.
Mathematical confirmation is manual, import-dependent, and same-scope;
it is not formal verification.

## Pins and read manifest

contribution_commit=060df43f6461ce1119b2c5c188a8eb1ab51b2a14
producer_basis=a91c8ad9829fb9417e9650787a185126274e058e
hq_governance_basis=a3c3bee653177ee99355579448f8592bfdd43629
README.md 7181a9dd4cf928e5327ee5324ccf7861098e2b7321395852418aa8c7808fbbdf
AGENTS.md 31f54fa5b1a9f76dc5455dd6c42615e565b47b96499c6fc69f389980e762a96f
COORDINATION.md 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e
APPROACHES.md 0b52fc2170aa459cbf91f071071d49cdf62ee6d0ea02bb3e4c3a8a9b0e44c053
FALLACY-v2.md e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5
rational-pencil-unification-swarmHQ-root-20260920T033600Z.md 3e0fa8f18601be655958dd3712df60fdcf9b30e0ab07daa4c39928f1a2c022b9
rational-pencil-unification-swarmHQ-root-20260920T033600Z.md.artifact.json 38a4de7badfec4d4c663d8ff7d38b2e71b8138a883d8ffb175c3339b1cd9090b
homogeneous-pencil-composition-swarmHQ-root-20260919T175300Z.md 45c5c50e94a73272b5b5ad6c387035d1defc9553c7dcb825ead2b85e8db9a854
homogeneous-pencil-first-integration-swarmHQ-root-20260919T181000Z.md 16060675d9b95f2a1cc106bc4bf376140f4b1b859e1e5c96571a12210d6fca01
rational-polynomial-pencil-swarmHQ-root-20260920T011100Z.md f06a1d0c931f1e7270f6b63132dbfd5b01588928e0f9e5e2ee8f115665367e88
rational-pencil-first-integration-swarmHQ-root-20260920T013400Z.md 4fc8f4f6a2d978a2335bcd75e8a21297f78ac089c17e055bd31f81fd03dda382
hyperbolic-moving-pencil-swarmHQ-root-20260919T203700Z.md bcb4e3c3851f50db05654c9acfcba11131d55df4f29302a28cf89dceeb42370a
hyperbolic-pencil-first-integration-swarmHQ-root-20260919T205600Z.md 6c1be9fd3a3f81baa73cbfae5a6e426e25434f55d09cb04815440130e3c790a5
HQ AGENTS.md 06ba4c0898c8a4272478b16f8b72f2877cf235ed3a8af5016059d1114dd0c34f
HQ POLICY.md 29d6bcea7ed4fa1031846705c765ce27f487f76ea330c6312cbad6ca38c42393
HQ RESEARCH_POLICY.md 710fcf0c3b2bfca649677365fb4094b6527f172981016696ee67095fca910778
HQ RUNBOOK.md 67f2cbffb19b407f7c9094de193f43ba28fd4c960b9509745d4c007b73557c81

## OPEN(S) RAISED

None. No descendant, experiment, family or successor is raised.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Post-read recheck: all 13 charged snapshot hashes unchanged after every
read (sha256sum -c, 13 OK). The trusted ops/open_collision.py output is
reproduced above verbatim. Body word count before the pin manifest: 1790.

Author completion: 2026-09-20 04:00:22 UTC, measured after whole-body readback of all
authored text; this line and the marker below are the last writing.
Not sealed or finalized here; legacy parent custody applies.

<!-- BODY-END -->
