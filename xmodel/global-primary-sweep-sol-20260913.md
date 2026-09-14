# Global primary sweep — all-degree JC2 mechanisms

Task: `global-primary-sweep-sol-20260913`  
Basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`  
First action: `2026-09-13T03:58:13.519869334Z`  
Network closed no later than: `2026-09-13T04:02:33.504077324Z`, before the fixed `04:13Z` cutoff.

## Verdict

**NO_NEW_CLIENT.** Three theorem-level mechanisms yield cheap, concrete discriminators, but none currently supplies the missing campaign-specific hypothesis. They are retained below as actionable *attachment tests*, not as progress on JC2 itself. This was a bounded primary-source sweep and does not discharge unrelated broad-coverage debts.

## 1. Nonproperness must self-intersect — useful local target, wrong strength

Jelonek, arXiv:2011.03472v1 (submitted 2020-11-06), Theorem 1.1 states: for a polynomial `F:C^2→C^2` with nowhere-vanishing Jacobian, its nonproperness set `S_F` cannot be a curve without self-intersections. The complete proof was read. Under the contrary hypothesis it first excludes disjoint reducible components, then treats irreducible `S_F` as a polynomially embedded copy of `C`; a covering/Euler-characteristic argument produces a source curve mapped homeomorphically to it, and plane-curve rectification plus the cited one-line injectivity criterion forces `F` to be an automorphism.

Version qualification matters: the current arXiv record is withdrawn v6 (2021-09-08), says v4/v5 are incorrect, and expressly labels v1/v2/v3 correct. This report uses the retained exact v1, not the withdrawn later body.

**Attachment assessment: GAP.** The frozen TRACE avenue needs a source-derived local divisor configuration strong enough for its trace/conductor obstruction (in particular controlled reduced branches/ordinary-node behavior). “Not without self-intersections” does not by itself state a transverse ordinary double point, the required local normalization/conductor structure, or a violating trace element. It therefore does not manufacture the missing TRACE node.

**Cheapest discriminator:** compare the precise singularity notion used in Jelonek's theorem with the actual reduced nonproperness divisor `D`; ask whether some guaranteed self-intersection has two reduced smooth transverse branches. If yes, apply the existing node trace calculation there. If only worse/nontransverse singularities are guaranteed, this client remains unattached.

## 2. Prime field degree — broad stratum, no prime-degree landing

Moskowicz, arXiv:2407.13795v1 (submitted 2024-07-16; only v1 shown at retrieval), claims that a plane Keller map cannot have prime field-extension degree. The complete relevant sections were read. Theorem 3.2 handles `xy∉k(p,q)` by proving nonconstant monomials primitive and then invoking the paper's quoted “Answer 2.21,” which says the resulting rare primitive-element property forces extension degree two. Theorem 3.3 handles `xy∈k(p,q)`: Wang's intersection theorem gives `xy=H(p,q)`; restriction to a line `y=mu`, followed by a line-embedding/injectivity theorem, yields invertibility.

Two source-level qualifications remain. First, the decisive rare-property implication is attributed to an external MathOverflow answer and is not proved in this PDF. Second, the Theorem 3.3 proof needs `mu≠0` to infer `k[x]=k[p(x,mu),q(x,mu)]`; the written choice excludes finitely many bad ordinates but does not explicitly add zero. Over an infinite field that omission appears repairable by choosing a nonzero good `mu`, but it should be recorded rather than silently supplied.

**Attachment assessment: GAP.** If independently validated, this eliminates every prime geometric field-degree stratum and goes beyond the campaign's degree-two/Galois and cubic-block closures. But no frozen campaign theorem forces a hypothetical source degree to be prime; composite primitive/no-block degrees remain.

**Cheapest discriminator:** independently reconstruct “rare property implies degree two,” repair/check the nonzero-line choice, then translate the theorem's field degree exactly into campaign `d1/d2`. Only after that should this become a prime-stratum client; it is not an all-degree closure.

## 3. Every equivariant plane Keller map is invertible — missing global action

Shaska, arXiv:2607.20210v2 (v1 2026-07-22; v2 2026-07-25; manuscript dated 2026-08-24), Theorem 3.4 states that a plane Keller map equivariant for nontrivial algebraic `G_m` actions on source and target is an automorphism. The full theorem proof was read. After polynomial linearization of both actions, target weights must permute source weights. Positive weights make the map triangular (linear when equal); one zero weight gives `(x f(y),g(y))`, whose constant Jacobian forces affine form; opposite-sign coprime weights give `(x f(u),y g(u))`, `u=x^q y^p`, and the induced one-variable map has derivative `f^(q-1)g^(p-1) det JG`. Degree comparison forces `f,g` constant.

**Attachment assessment: GAP.** This is genuinely all-degree once equivariance exists, but the frozen campaign has no implication from a leading weighted cone, kernel scaling, Hamiltonian/Liouville identities, or a special graded family to a global algebraic `G_m` action on an arbitrary Keller source. It therefore repeats no homogeneous-family proof, yet supplies no new arrow from the actual source.

**Cheapest discriminator:** solve the finite integer weight equations imposed by the actual supports of `(P,Q)` for nonzero source weights and matching target weights, allowing only already authorized coordinate normalizations. A solution attaches Theorem 3.4. Failure in current coordinates does not exclude a polynomially conjugate action, so it is only a positive detector.

## Screened exclusions and boundary

The 2015 “normality after adjoining a primitive element” criterion was screened as the already-known finite monogenic graph normality endpoint: it does not prove normality. The 2023 integral-curves claim was excluded because its current primary arXiv record is withdrawn and says the main result is false. Known BGV, generic-properness, conditional Markov/shuffle, pseudo-plane, slice, genus-zero, cubic-block, and homogeneous-family gaps were not relabeled as new clients.

Primary-domain queries covered nonproperness, trace/conductor/normality, Liouville/symplectic potential, D-modules, primitive extensions, affine-plane étale maps, polynomial algebraization, and graded actions. Abstracts/snippets were discovery-only. Generic GitHub/social noise was not followed; protected material was neither encountered nor retained. Exact URLs, versions, hashes, and read scopes are in `box/global-primary-sweep-sol-20260913/SOURCE-INDEX.md`.

## Publication status

Documentary research only. No theorem was promoted, no source or ledger changed, no scientific computation or external action occurred, and no launch/worker authority is implied.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6912`.
- Body SHA-256:
  `195078877ee2d358777a0268341da82ff5341754ef24fea3921a5983551597ee`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
