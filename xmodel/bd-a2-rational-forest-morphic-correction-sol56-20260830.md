# Binding correction: the rational-forest gate is morphic, not rational

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen basis: `7ef0f3d9799b196dea26a82315c8ac79a0fbb00d`  
Lifecycle: **BINDING CORRECTION / FALSE STRENGTHENING RETRACTED**

## 0. Disposition

The original producer proved the rational-forest theorem under an
everywhere-defined dominant morphism `A^2 -> U`.  The hostile review and the
coordinator integration strengthened this to an arbitrary dominant rational
map.  That strengthening is false.  This packet retracts it and restores the
producer's morphic hypothesis.

The correction does not invalidate actual proper-block clients: their first
leg `g1:A^2 -> Y` is an everywhere-defined dominant étale morphism.  It does
invalidate any use based only on abstract rational domination of an open
surface.

The affected promoted packet is

```text
6a8558e42a67f1ec5c8bcf12321b6e6805b30a570eba17862c6e7e24cd631b08
  xmodel/bd-a2-rational-forest-coordinator-integration-sol56-20260830.md
```

Section 1 of that packet is superseded by the theorem below wherever it says
"rational map".  Its residue formula, multisection formula and graph/genus
calculations are unchanged.

## 1. Counterexample to the rational-map extension

Let `E` be a smooth plane cubic and put

```text
U=P^2 minus E.
```

The identity on `P^2` gives a dominant rational map from the standard affine
chart `A^2` to `U`: it is defined on the dense open
`A^2 minus (E intersect A^2)`.  Yet `(P^2,E)` is already a smooth SNC
completion and its boundary contains the genus-one curve `E`.  Thus

```text
tau(E)=sum genus(E_i)+b1(Gamma_E)=1.
```

An arbitrary dominant rational map from `A^2` therefore imposes no
rational-forest boundary condition.

The failed proof step was the assertion that resolving
`A^2 dashrightarrow U` gives a proper birational `W -> A^2` with the same
logarithmic Kodaira dimension as `A^2` and a morphism `W -> U`.  A rational
map to the nonproper `U` may have poles into the omitted boundary at points
inside `A^2`; resolving the map to a proper completion does not produce a
morphism to `U` on all of a proper-birational model with open part `A^2`.
The cubic example exhibits exactly this failure.

## 2. Correct morphic rational-forest theorem

Let `U` be a smooth quasi-projective complex surface and let

```text
f:A^2 -> U
```

be an everywhere-defined dominant morphism.  For every smooth projective
strict-SNC completion `U=X minus D`, every component of `D` is rational and
the dual multigraph of `D` is a forest.

Indeed, embed `A^2` in `P^2` with boundary line `L`.  The morphism to `U`
followed by `U subset X` extends to a rational map `P^2 dashrightarrow X`
whose indeterminacy lies entirely on `L`.  Resolve its graph without changing
`A^2`:

```text
W --F--> X,
W minus B = A^2,
F^{-1}(D) subset B.
```

Here `W` is rational, `B` is a strict-SNC boundary after further boundary
blowups, and `F` is dominant and generically finite.  Logarithmic pullback
injects

```text
H0(X,m(K_X+D)) -> H0(W,m(K_W+B))
```

for every `m>=1`.  The right side is zero because
`bar-kappa(A^2)=-infinity`; hence `bar-P_m(U)=0`.  Ordinary pullback of
one-forms and pluricanonical forms along the generically finite `F` also gives

```text
p_g(X)=q(X)=0.
```

For reduced strict-SNC `D`, residue, normalization and Serre duality give

```text
bar-P_1(U)=p_g(X)+tau(D)-rank(partial),
rank(partial)<=q(X),

tau(D)=sum_i g(D_i)+b1(Gamma_D).
```

Therefore `0=bar-P_1(U)=tau(D)`.  Both summands are nonnegative, proving the
claim.

Equivalently, any complete boundary subconfiguration containing a
positive-genus component or a graph cycle forbids an everywhere-defined
dominant morphism from `A^2`.  Passing to a larger resolved boundary cannot
erase positive component genus or the first Betti number of an existing
subgraph.

## 3. Correct actual-first-leg interface

For a hypothetical proper block,

```text
A^2 --g1--> Y --g2--> A^2
```

the promoted block-structure theorem supplies that `Y` is normal affine and
that `g1` is everywhere-defined, dominant, quasi-finite and étale.  Its image

```text
V=g1(A^2)
```

is an open smooth subscheme of `Y`, and `g1:A^2 -> V` is a surjective
morphism.  Apply Section 2 directly to `V`; no equality `V=Y minus R`, no
properness of `g1`, and no rational-map strengthening is needed.

Consequently, if a projective or local model of the actual block surface has
a point `p` outside `V`, then every complete exceptional curve over `p` is a
boundary curve in a smooth completion of `V`.  A positive-genus exceptional
component or a resolved exceptional cycle is an immediate contradiction.

This remains true when `p` is singular: the étale first leg from the smooth
source misses `Sing(Y)`.  It also remains true if `V` is a proper open subset
of the usual non-branch open `Y minus R`, because the theorem is applied to
`V` itself.

## 4. Scope repair for existing clients

The following rules supersede the old wording.

1. A boundary-genus or boundary-cycle exclusion is binding when its client
   supplies an everywhere-defined dominant morphism `A^2 -> U`.  Every actual
   proper-block first-leg client supplies this.
2. A claim about an abstract open surface with only a dominant rational map
   from `A^2` is not covered and must be retyped `OPEN` unless it has another
   proof.
3. For a proper projective target, a dominant rational map from `P^2` still
   forces `p_g=q=0` by ordinary pluriform pullback on a resolution.  This
   projective statement does not imply a rational-forest theorem for a chosen
   open complement.
4. Open-subset monotonicity of logarithmic plurigenera remains true, but it
   cannot convert a rational map into an everywhere-defined morphism.

The exact multisection identity and all purely combinatorial evaluations of
`tau` in the corrected packet remain available.  Each application must now
charge the morphic interface explicitly.

No block occurrence, polynomial map, counterexample, or JC2 conclusion is
proved here.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6040`.
- Body SHA-256:
  `6e97a5c2bdb8aa679e53338d507bd684161eb53af96cd09fa4f2662fcbba08f0`.
- Frozen basis: `7ef0f3d9799b196dea26a82315c8ac79a0fbb00d`.
