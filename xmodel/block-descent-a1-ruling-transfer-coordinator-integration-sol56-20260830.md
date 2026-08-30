# Binding integration: qualitative `A1` ruling on every proper block open

Date: 2026-08-30 UTC  
Integrator: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `81c1db3fb787749562894c83439d327a10d19d70`  
Disposition: **PROMOTE WITH REVIEW CORRECTIONS / QUALITATIVE BLOCK-GENERAL THEOREM**

## 0. Binding verdict

Promote the repaired proper-block ruling theorem.  For the hypothetical
proper intermediate factorization supplied by the binding block theorem,

```text
A2 --g1, etale quasi-finite dominant--> Y
   --g2, finite flat surjective--> A2,
```

let `R=NonEt_Y(g2)` be the full **source** non-etale support and put
`U=Y minus R`.  Then

```text
U is smooth, rational, and affine;
O(U)^*=C^*;                         bar-kappa(U)=-infinity;
g1:A2 -> U is the actual dominant etale quasi-finite first leg;
rho:U -> C is a surjective A1-fibration, C=A1 or P1;
every fibre with its reduced structure is a disjoint union of A1s.
```

This theorem is independent of a quadratic presentation.  It applies only
inside the proper-intermediate-field horn.  It transfers no quadratic Euler
constant, `D9` marking, Picard cap, `F5` data, bounded completion, coefficient
occurrence, or conclusion about the primitive/no-proper-block horn.

The different-model review returns `CONFIRM_WITH_CORRECTIONS`.  Its one
refutation concerns only an optional fallback proof in the producer: absolute
affineness does **not** descend from an affine fpqc cover.  The promoted
argument instead uses Stacks Tag `0ECD` directly, so the false fallback has no
downstream consumer and is quarantined here.

## 1. Frozen evidence

```text
acfcd839a4f7af77c54a75bc30c2909f26c6afb8ec35b1862dc685e27b270819
  xmodel/block-descent-a1-ruling-transfer-audit-sol56-20260830.md
b52d063d2801885c30fe92212b86d9cda1de7c97a6438a3cc1d243de1c6b30bc
  xmodel/block-descent-a1-ruling-transfer-audit-sol56-20260830.md.artifact.json

259ad683e97daadeaf82b737dcc467ea7d1d07faa8ce40039f13e100b2da64aa
  xmodel/block-descent-a1-ruling-transfer-hostile-review-fable5-20260830.md
  body f2b0d3ae2f800e3a9958bc9c467db219cd16025ddfd42d459b78341eddd86d6f
0009fa4ddd787144c006eb425221054233a0346f44c1ae91fea940c03cca442d
  xmodel/block-descent-a1-ruling-transfer-hostile-review-fable5-20260830.run.v2

ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
```

Root reproduced the schema-v2 receipt, immutable prompt, Claude adapter,
launcher, Seatbelt profile, charge-basis validator, `FALLACY-v2.md`, composed
model prompt, report, log, and all five charged mathematical hashes before
reading the review.  The body was then stamped against basis
`5cc7b50274df491cb09dbb91a8b528de77fc5ef4` and independently verified.
`charge_basis_status=ABSENT` is correct: the review made no new exit-price
assertion.

## 2. Direct reconstruction

The binding block theorem gives `Y` integral, normal, affine, and finite over
`A2_C`; hence `Y` is a finite-type excellent complex surface.  It also gives
that `R` is nonempty and pure of codimension one,
`g1(A2) subset Y_sm minus R`, and `Sing(Y) subset R`.

### 2.1 Affineness and smoothness

Apply Stacks Project Theorem 58.29.3, Tag `0ECD`, with Stacks-source `Y`,
Stacks-target `A2_C`, and morphism `g2`.  Its literal conclusion is that the
inclusion of the maximal etale open into the normal source is an **affine
morphism**.  The maximal etale open is exactly `U=Y minus R`; since `Y` is
affine, `U` is affine.  One must not shorten the theorem to the false absolute
claim that every such maximal etale open is affine without the affine-source
hypothesis.

This direct route uses normality of `Y`, finite type of `g2`, and the excellent
regular target over a field.  It does not need dimension two, purity, or
nonemptiness for this affineness step, although those properties remain
promoted block data and enter other block arguments.  The Nagata
normal-excellent-surface divisor-complement theorem supplies an independent
route using purity.

By definition `g2|U` is etale.  Since its target is smooth, `U` is smooth.
Because `g1(A2)` avoids `R`, `g1` factors uniquely through `U`; density in
`Y` implies density in the nonempty open `U`, and etaleness and
quasi-finiteness are unchanged.

### 2.2 Units, rationality, and logarithmic Kodaira dimension

Dominance makes

```text
g1^*:O(U) -> C[x,y]
```

injective.  A unit therefore pulls back to a scalar, and injectivity applied
to its difference from that scalar gives `O(U)^*=C^*`.  The finite extension
`C(U) subset C(x,y)` makes `U` unirational; Castelnuovo in characteristic zero
makes its smooth projective model rational.

For a dominant generically finite morphism of smooth open varieties,
log-pluricanonical pullback gives

```text
bar-kappa(A2) >= bar-kappa(U).
```

Since `bar-kappa(A2)=-infinity`, necessarily
`bar-kappa(U)=-infinity`.  Etaleness without properness does not upgrade this
to a general equality theorem; only the displayed direction is consumed.

### 2.3 The ruling, its base, and its fibres

The Miyanishi--Sugie cylinder theorem together with the standard
cylinder-to-global-fibration extension for smooth affine surfaces yields an
actual surjective morphism on all of `U`,

```text
rho:U -> C,
```

whose general scheme fibre is `A1`; no base or field extension is inserted.
Rationality of `U` and Luroth make `C` rational.  Pullback along the
surjective `rho` injects `O(C)^*` into `C^*`, so a smooth rational affine base
has at most one puncture.  Thus `C=A1` or `P1`.  The projective-base branch is
real for general smooth affine surfaces and is not excluded here.

The charged Gurjar--Miyanishi fibre lemma says that every fibre, after taking
its reduced structure, is a disjoint union of affine lines.  This controls
neither Cartier multiplicities nor the number of bad fibres or components.

If `q_t` is the number of reduced components at a bad value, Euler additivity
over the complement of the finite bad-value set gives the presentation-free
identity

```text
e(U)=e(C)+sum_t(q_t-1).                                (2.1)
```

Hence `e(U)>=1`, and `e(U)>=2` on the `P1` branch.  Formula (2.1) transfers;
the quadratic evaluation `e(U)=12-r-c` does not.

## 3. Review corrections and attack controls

1. **False fallback removed.**  If `V=g1(A2)`, the surjective etale
   quasi-compact map `A2 -> V` is fpqc, but affine total space does not force
   affine base.  The explicit cover
   `D(x) disjoint_union D(y) -> A2 minus {0}` is a counterexample.  Whether
   `V` omits isolated points of the affine `U` remains open and is unused.
2. **Source and target loci stay distinct.**  `R` is source non-etaleness.
   The target discriminant, its full inverse image, and `g1(A2)` are different
   objects.  An unramified sheet over a branch value can lie in `U`, so
   deleting the full inverse image of the target discriminant would be too
   strong.
3. **Weil support is sufficient.**  Neither the direct route nor the Nagata
   route assumes `R` Cartier, principal, or `Q`-Cartier.  Multiplicities do
   not define `U`.
4. **Purity is correctly source-side.**  The promoted divisoriality is also
   compatible with Stacks Tag `0EA4`; an isolated non-etale residue would
   violate purity.  Deleting only selected components would retain
   non-etale or singular points and break the surface-theorem hypotheses.
5. **The complete-base control survives.**  Complements of ample sections in
   Hirzebruch surfaces exhibit smooth rational affine `A1`-fibrations over
   `P1` with constant units.  No qualitative transferred hypothesis chooses
   the affine base.

## 4. Maximum-safe theorem and firewalls

> **Proper-block ruling theorem.**  Assume a hypothetical noninvertible
> complex Keller map has a proper intermediate field and charge the promoted
> block factorization above.  For the full source non-etale support
> `R=NonEt_Y(g2)`, the open `U=Y minus R` is a smooth rational affine complex
> surface, the actual first leg factors as a dominant etale quasi-finite
> `A2 -> U`, `O(U)^*=C^*`, and `bar-kappa(U)=-infinity`.  The surface admits
> a surjective `A1`-fibration over `A1` or `P1`, directly over `C`, and every
> fibre with reduced structure is a disjoint union of affine lines.  Its
> Euler number satisfies (2.1).

This is an exact qualitative theorem conditional on a proper block.  It does
not prove that a proper block exists.  It does not transfer the quadratic
constant `12`, a Picard or boundary-rank cap, `F5`, `D9`, a finite
presentation, a ruling on a particular raw completion, or any result about
the primitive sector.  A full control satisfying the whole sandwich would
itself be a noninvertible Keller map and cannot be priced as a routine
example.

## 5. Theorem-interface composition and successor

The composition pass finds one exact new bridge: the presentation-free
fibre Euler identity (2.1) can be compared with a sandwich-side computation
of `e(U)=e(Y)-e(R)` without importing any quadratic marking.  No current
promoted theorem evaluates that second ledger, so the bridge is `OPEN`, not a
numeric exclusion.

The cheapest decisive successor is `BD-A1-EULER-LEDGER`: stratify the finite
flat `g2` over its target discriminant and separately account for
nonproperness of the etale quasi-finite `g1` to compute or bound `e(U)` in
terms of `d1,d2` and block-general branch data.  In parallel, test whether
`d1>=2` rules out the `P1` base.  Neither successor should wait for the other,
and neither imports a quadratic Euler constant.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9690`.
- Body SHA-256:
  `469f1f68e1dd11c901ed467e5d95046a26fb3d036186c8298044309457196e56`.
- Frozen basis: `81c1db3fb787749562894c83439d327a10d19d70`.
