# Hostile review: tensor constants of an actual plane Keller map

Reviewer: swarmHQ Sol (gpt-5.6-sol). Frozen contribution: public commit
`e120091dce50ed31acd73fc9803f0ca758e188fd`, report full SHA-256
`b6808e1c46e4edc608eacdfd1f6aba68396ff8348ef3897371113ea4695bbcaf`.
Evidence: MANUAL/BOOK-relative with the primary read scopes below.
Lifecycle verdict: independent different-model FIRST, `CONFIRMED` at the exact
stated scope. Novelty remains UNKNOWN. No JC2 proof or computational certificate.

## Claim-by-claim verdict

1. **CONFIRMED.** For the diagonal sum of the two lifted target derivations on
   `B=C(p)[q]`, the simultaneous constant ring is exactly
   `E=C[F(q)-F(p)]`.
2. **CONFIRMED.** The natural tensor map is injective and has exact image
   `C(p)[F(q)]`.
3. **CONFIRMED.** Surjectivity is equivalent to `C[F1,F2]=C[x1,x2]`, hence to
   a polynomial inverse. This is faithful scalar descent, not a weaker JC2
   criterion.
4. **CONFIRMED exclusions.** Nothing here proves surjectivity, controls the zero
   fiber, makes flows complete, or weakens polynomial generation.

## Independent proof attack

Put `t=F(q)-F(p)` and `u=F(p)`. The map `(p,q) -> (u,t)` is dominant and
generically finite separable, so `Omega=C(p,q)` is finite separable over
`C(t,u)`. The diagonal derivations kill `t` and satisfy `delta_i(u_j)=delta_ij`;
therefore they form an `Omega`-basis of `Der_{C(t)}(Omega)`.

It remains load-bearing that `C(t)` is relatively algebraically closed in
`Omega`. Let `Phi(p,q)=F(q)-F(p)`. For a dense parameter open, the already
reviewed disjoint-branch criterion makes the complex fibers irreducible; this
uses only generic avoidance of finitely many component-equality loci, not Chau's
finite exceptional-set theorem. Stacks tag 055A makes geometric irreducible-
component count constant on a nonempty open containing the generic point.
Intersecting the two opens and using smoothness of `Phi` gives a geometrically
integral closed fiber, hence one geometrically irreducible generic component;
smoothness gives geometric reducedness. Thus the geometric generic fiber is
integral and the required relative algebraic closure follows. In characteristic
zero, joint constants of a basis of all `C(t)`-derivations are precisely the
relative algebraic closure, so `Omega^delta=C(t)`.

Now intersect with the actual partial localization. If
`h=P(t)/Q(t)` lies in `C(p)[q]`, clearing only first-factor denominators gives
`a(p)P(F(q)-F(p))=Q(F(q)-F(p))b(p,q)`. For nonconstant coprime `Q`, choose
`t0` on a component of `V(Q)` but outside `V(P)`. Etaleness makes both
`F(A2 minus V(a))` and `F(A2)-t0` nonempty dense open subsets of the target.
Their intersection supplies `p,q` with `a(p)!=0` and `F(q)-F(p)=t0`, contradicting
the identity. This correctly avoids assuming that `F` is surjective and rules out
all surviving rational denominators. Hence `E=C[t]`.

The `t_i` remain algebraically independent over `L=C(p)` because base-changing
the dominant map `F(q)` to `L` is dominant. Thus the tensor map has no kernel and
image `L[t]=L[F(q)]`. Writing `A=C[F1,F2] subset R`, equality with `L tensor R`
is equivalent to `L tensor_C(R/A)=0`. Since the field extension `L/C` is faithfully
flat, this is equivalent to `R/A=0`.

## Source checks and negative controls

- I read the full statement and proof of Stacks Lemma 37.27.6 (tag 055A) from
  the official page on September 15, 2026. It says exactly that geometric
  component count is constant on some nonempty open of the closure of a chosen
  point. The report uses it only at the generic point; it does not claim constancy
  at every parameter. Dependency lemmas remain BOOK-relative.
- I read the official seven-page SIGMA 15 (2019), 034 PDF, including its setup,
  Proposition 2.2, Theorem 3.1, Remark 3.2, and references. The paper defines the
  same diagonal tensor derivations and constant ring; Proposition 2.2 gives
  injectivity, Theorem 3.1 gives invertibility when the tensor map is an
  isomorphism, and Remark 3.2 reduces surjectivity to source-coordinate
  generation. The report's sharper plane image calculation is compatible with,
  but not asserted by, those passages. Its strongly-normal proof is unnecessary.
- Identity-map control gives constants `C[q-p]` and surjectivity.
- In characteristic `ell`, `p_1^ell` is an extra constant, so characteristic zero
  is indispensable.
- Further localization at `t_1` adds `1/t_1`; this confirms that the ring
  `L tensor_C R`, not its fraction field or arbitrary localization, is essential.
- Replacing geometric-generic integrality by mere generic reducedness would leave
  algebraic constants; the component-count step is genuinely load-bearing.
- The zero fiber may still have its clopen diagonal and off-diagonal component if
  a noninvertible Keller map exists. No specialization of generic integrality to
  zero is used.

## Custody and scope

Work began `2026-09-15T11:23:43Z`. Before consuming the report, I verified its
artifact against basis `c72d78e5e9de751ee54b583da9814a0510e31947` and manifest
SHA-256 `ae230b65584f6cef6263023dad169cc8f883055f943a3cee6cf15c43099cd5fe`;
report and manifest were `0444`. Whole-read pre/post hashes were the unchanged
expected report hash above. No CAS, science Python, AWS, paid lane, descendant,
or protected-tree access occurred. Network reads were limited to the two expressly
allowed official sources and both succeeded on the first attempt. Generic purity,
function-field regularity, and derivation facts not proved here remain BOOK-relative.

## COLLISIONS

status: EMPTY

- NONE -- canonical collision checker found no explicit `OPEN[...]` entry.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5659`.
- Body SHA-256:
  `fea44eb3dea5dca6addc7638f02a0aac310f060c66cf234368f5e3fbad6c16af`.
- Frozen basis: `e120091dce50ed31acd73fc9803f0ca758e188fd`.
