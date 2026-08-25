# Reviewed successor: selected-Q8 mod-127 projected component

Date: 2026-08-25  
Status: **REVIEW-CLEARED EXACT MOD-127 COMPONENT THEOREM**

## Theorem

Over `Fbar_127`, the corrected selected-Q8 localized six-row source has an
irreducible curve component whose cycle-theoretic image in the `(w,v)` plane
is the geometrically irreducible candidate curve `H(w,v)=0`.

This successor incorporates the repairs required by the independent Claude
review

```text
xmodel/max12-912-order3-nu-q8-sparse-contact-component-review-claude-20260825.md
SHA256 ebd0024dfe2ea1623f22ba483b93d76dd9ff2aabe5f9f96eabc7b115928c7164
verdict CONFIRMED WITH REPAIRS.
```

It does not mutate the earlier producer reports or their frozen cases.

## Repaired projection-cycle argument

At every charged fixed-fibre source point, the relative six-by-six Jacobian
with respect to `(c,d2,d4,x1,x3,x5)` is a unit.  The completed local source
ring is therefore `Fbar_127[[w-w_i]]`; the point lies on one reduced regular
curve branch and `w-w_i` is a uniformizer.  In particular, `dw` is nonzero
there.  Hence the relevant component-to-`A1_w` function-field extension is
separable, and so is the intermediate generically finite extension from the
component to its plane image.  A generic plane line therefore has the full
cycle degree number of distinct reduced preimages; no inseparable degree is
lost in the sparse root count.

Define the pushforward precisely as follows.  For each relevant component,
take the normalization of the projective closure of the graph of its regular
localized map to `(w,v)`, then push its fundamental cycle to `P2`.  Choose the
generic target line to avoid:

- localization-boundary and source-closure points outside the affine chart;
- intersections with every other source component;
- singular, ramification, and component-collision images; and
- all points at infinity of the plane images.

These are finite sets.  The resulting pullback points are distinct isolated
roots of the seven sparse polynomials in the licensed affine chart.  The
arbitrary-characteristic affine isolated-root theorem, applied after adjoining
the origin to every support, and support monotonicity under reduction modulo
127 give

```text
deg(pi_*Z) <= 658.
```

No row can vanish identically modulo 127 because the charged relative
Jacobian determinant is a unit.  Unrelated positive-dimensional boundary
components do not affect the isolated-root bound.

At a squarefree degree-190 fixed fibre, an exact lift over

```text
F_127[s,v]/(s^N,H(w_i+s,v))
```

splits over `Fbar_127` into 190 length-`N` jets.  The unit source Jacobian
identifies each with the order-`N` truncation of the unique source branch, so
the pullback of `H` has valuation at least `N` at each point.  On the proper
graph model, the projection formula identifies these valuations with local
terms of `I(H,pi_*Z)`, including the correct source-to-image pushforward
multiplicities.  Distinct `w_i` give disjoint plane points, so the terms add.

Use only the stored positive-order lifts:

```text
80 distinct order-8 fibres, all excluding w=25:  640
the separately frozen w=25 order-64 fibre:         64
normalized contact:                               704 > 658.
```

If no projected component were `H`, the irreducible degree-190 projective
curve `H` and the effective projected cycle would share no component.  Bezout
would give

```text
I(H,pi_*Z) = 190*deg(pi_*Z) <= 190*658,
```

whereas the charged affine terms alone give at least `190*704`.  This is the
required contradiction.

## Numerical and provenance hygiene

The reviewed count is only `80*8+64=704`.  The immutable older
`123+63+68*7=662` count is superseded and is not consumed here.  The current
count can lose at most five order-8 fibres, but it cannot lose the order-64
`w=25` lane: `75*8+64=664>658`, while `80*8=640<658`.

The Box03 value `658` is an independent execution replication of the pinned
Normaliz pipeline, not an independent implementation.  This wording does not
affect the exact bound.

The theorem also consumes the pinned predecessor facts that `H` is monic in
`v`, geometrically irreducible, and of exact total degree 190.  It is a
geometric theorem over `Fbar_127`; the Galois orbit gives the corresponding
`F_127` cycle statement.

## Scope firewall

The theorem proves only existence of an `H`-supported projected source
component modulo 127.  It does not prove source degree one, a global coordinate
graph, coverage of all 190 branches or all eight corrected-Q8 contacts,
characteristic-zero no-merger, Taylor realization, the terminal differential
row, a rational trajectory, a maximum-12 exclusion, or any Jacobian-conjecture
conclusion.

## Immutable dependencies

```text
xmodel/max12-912-order3-nu-q8-sparse-contact-component-lemma-20260825.md
  78fb3e1b08556498d79ed180f9b64e243f88dd80780936bc47e15b3749b5ce77

xmodel/max12-912-order3-nu-q8-p127-breadth-component-self-contained-erratum-20260825.md
  2aa3479c8e5ad3b4904e126936bc6cbb01a1772ed16357defa654f203384850e

cases/max12_912_order3_nu_q8_p127_component_self_contained_count_20260825/
  manifest 2ed765028d6bca6f065367605a64f1ecf3e39152e9995f3e41c55aaace54c5c9
```
