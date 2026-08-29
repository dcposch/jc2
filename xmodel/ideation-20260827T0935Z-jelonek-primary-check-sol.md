# Primary-source check: Jelonek bounded-degree component proposal

Date checked: 2026-08-27

Status: coordinator source check for the conditional proposal in
`xmodel/ideation-20260827T0935Z-opus5.md`.  This is navigation, not a JC2
theorem promotion and not a canonical-ledger edit.

Primary source: Zbigniew Jelonek, *On mappings with Jacobian one*,
arXiv:2607.20597 (version displayed 2026-07-24),
<https://arxiv.org/abs/2607.20597>.

## What the paper actually supplies

Write `X(n,d)` for the affine variety of degree-at-most-`d` polynomial maps
with Jacobian one, and `A(n,d)` for its automorphism locus.  Lemma 2.1 states
that `A(n,d)` is Zariski closed.  Theorem 2.2 therefore gives, for every
irreducible component `Y` of `X(n,d)`, the dichotomy

```text
Y is contained in A(n,d),
or Y \ A(n,d) is a dense open subset of Y.
```

Thus Opus's useful inference is correct: if a bounded-degree component
contains one counterexample, counterexamples are generic *inside that
component*.  The recorded slogan that counterexamples must form a thin locus
inside every component is not justified.

## What it does not supply

The paper does not identify a counterexample-containing plane component, prove
`X(2,d)` irreducible, enumerate its components, or provide an efficient way to
sample a component.  The theorem therefore redirects a structured search
toward component discovery/decomposition; it does not make random sampling in
the full Keller variety effective.

In particular, merely finding an automorphism in a component does **not** show
that the component is generically automorphic.  The second branch of the
dichotomy may contain a proper closed automorphism locus.  This is compatible
with the normalized scaling deformation: an orbit can have a linear
automorphism as its `t -> 0` limit while its generic points are
nonautomorphisms.  Opus correctly refuted this stronger component-purity
bridge later in its report, but the proposed small-degree prediction that
every component containing an automorphism is generically automorphic must be
withdrawn.

## Campaign disposition

- Retain the componentwise-density reading as a correct reframing of avenues
  7 and 36.
- Do not raise random counterexample search on this theorem alone.
- A bounded component-decomposition experiment is useful only where the
  Keller parameter space is already computationally tractable and the result
  has a clear lift/ceiling interpretation.
- No current total-rho, K00, AS109, Gate-T, or JC2 claim changes.

Web/tool disclosure: the arXiv abstract and displayed paper text through
Theorem 2.2 and Corollary 2.3 were read via the web interface.  No other source
was used; no AWS or CAS computation was run; `jc2-lean` was not accessed.
