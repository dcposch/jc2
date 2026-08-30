# Binding integration: morphic rational-forest correction

Date: 2026-08-30 UTC  
Integrator: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `d4cc6554c3f2d64561259dc2cbef1de9ea956e3f`  
Lifecycle: **REVIEWED BINDING CORRECTION / DOWNSTREAM SCOPE CLOSED**

## 0. Decision

Promote the correction that the rational-forest gate requires an everywhere-
defined dominant morphism from `A2`.  Retract the former extension to an
arbitrary dominant rational map.  GPT-5.5 independently reconstructed the
counterexample, proof, shrinking interface, actual proper-block client and
downstream inventory, returning `CONFIRM_WITH_CORRECTIONS`; its sole requested
correction is the same image-control qualification already present in the
binding correction.

The promoted theorem is:

> Let `U` be a smooth quasi-projective complex surface.  If there is an
> everywhere-defined dominant morphism `A2 -> U`, then for every smooth
> projective strict-SNC completion `U=X minus D`, one has
> `p_g(X)=q(X)=0`, `barP_m(U)=0` for all `m>=1`, every component of `D` is
> rational, and the dual multigraph of `D`, retaining parallel edges, is a
> forest.

Surjectivity, global quasi-finiteness and etaleness are not hypotheses of this
theorem.  Dominance between surfaces supplies generic finiteness.  In the
proper-block application etaleness is used upstream to make
`V=g1(A2)` open and smooth; `g1:A2 -> V` is then an everywhere-defined
surjective morphism and licenses the theorem.

## 1. Frozen evidence

The binding correction is

```text
d49a44ce65f13f0aba35e0a034923a1362594ba8a21fef27c63cc866ec7b667a
  xmodel/bd-a2-rational-forest-morphic-correction-sol56-20260830.md
  body 6040 / 6e97a5c2bdb8aa679e53338d507bd684161eb53af96cd09fa4f2662fcbba08f0
  manifest d14702bb98d3fd347a9b96ffaa531fefd55aad28df58d37601f6336bfb29029f
```

The receipt-first different-model rereview is

```text
47afb97312fbe7ddcb519129ae7605b024364060cf13504db050db3405cda528
  xmodel/bd-a2-rational-forest-morphic-correction-hostile-rereview-gpt55-20260830.md
  raw body 14308 / 4031939eab4b9533d3afccedbb15df468055b087d8e7ce09f18e6b361f511c44
  run 35b64466a81ebb3314a8b48083434f2bf278bb9f0cc47b8a952c8d98a61ebd2b
  verdict CONFIRM_WITH_CORRECTIONS
```

Before the report was read, every receipt hash was reproduced: frozen prompt,
adapter, launcher, Seatbelt profile, charge-basis validator and snapshot,
fallacy appendix, composed model prompt, raw report and log.  Receipt status
is `DONE`, exit code zero, and charge-basis status is the expected `ABSENT`.
The raw body hash was preserved by the canonical seal.

The first attempt is retained only as a failed custody record.  It left a
confirming body in its log but created no report, so it has no evidentiary role
in this promotion.

## 2. Counterexample and exact failed step

Let `E` be a smooth plane cubic and `U=P2 minus E`.  The identity on `P2`
restricts on `A2 minus (E intersect A2)` to a dominant rational map
`A2 dashrightarrow U`.  Yet `(P2,E)` is already a smooth SNC completion and

```text
K_P2+E=0,
barP_m(U)=1 for every m>=1,
tau(E)=g(E)=1.                                        (2.1)
```

Thus arbitrary rational domination imposes no forest condition.  The false
step was to resolve a rational map to the nonproper `U` while pretending that
the resolved morphism still has open source `A2`.  Resolving the map to a
projective completion does not make it factor through `U`: the interior pole
divisor maps to the omitted boundary.  Deleting that divisor changes the
source and its log invariants.

## 3. Proof of the morphic theorem

Embed `A2` in `P2` with boundary line `L`.  For an everywhere-defined
dominant `f:A2 -> U subset X`, the rational map `P2 dashrightarrow X` has no
indeterminacy over `A2`.  Resolving only over `L` gives

```text
W --F--> X,
W minus B=A2,
F^(-1)(D) subset B,                                  (3.1)
```

with `W` rational, `B` strict SNC after boundary blowups, and `F` dominant
generically finite.  Logarithmic pullback injects

```text
H0(X,m(K_X+D)) -> H0(W,m(K_W+B)).                    (3.2)
```

The target is zero because `(W,B)` is a log resolution of `(P2,L)` and
`K_P2+L=-2H`.  Ordinary differential and pluricanonical pullback into the
rational surface `W` also gives `p_g(X)=q(X)=0`.

For a possibly disconnected reduced strict-SNC boundary, residue,
normalization and Serre duality give

```text
barP_1(U)=p_g(X)+tau(D)-rank(partial),
rank(partial)<=q(X),
tau(D)=sum_i g(D_i)+b1(Gamma_D).                      (3.3)
```

Equations (3.2)--(3.3) force `tau(D)=0`.  Both summands are nonnegative, so
all components are rational and the multigraph is a forest.  Parallel
intersections are separate edges; two components meeting twice already make
a cycle.

Shrinking is purely numerical: adding boundary cannot decrease log
plurigenera or erase an existing positive-genus component/cycle.  It does not
create a morphism.  One may replace `U` by a smaller open only if the full
image `f(A2)` remains inside it.

## 4. Proper-block interface and persistence

For every actual proper block, the promoted descent theorem supplies

```text
A2 --g1--> Y --g2--> A2,
V=g1(A2) subset Y_sm minus Ram(g2),
g1:A2 -> V everywhere-defined, surjective and etale. (4.1)
```

Hence `V` satisfies the theorem.  A singular point or ramification component
missed by `V` has its complete strict transform and exceptional fibre in the
boundary of any common smooth completion.  Positive component genus survives
birational strict transform.  Blowing up an SNC boundary subdivides edges or
adds trees, so a pre-existing cycle, including a two-edge cycle, also
persists.  Contracting it on a singular model is irrelevant because the
obstruction is evaluated on the resolved boundary.

## 5. Downstream disposition

- Sections 1 and the rational-map wording of the old integration
  `6a8558e42...` are retracted and superseded here.  The old Opus review is
  likewise refuted only where it invented the rational-map upgrade.
- The residue formula, disconnected-boundary ledger, exact multisection
  formula, parallel-edge accounting and reduced bidegree-`(2,3)`
  classification remain correct as pure mathematics.  Their campaign
  exclusions require the morphic first leg (4.1).
- The `d>=3` smooth projective positive-`p_g` exclusion remains valid even
  under rational domination, because ordinary pluriform pullback to a
  resolution is enough.  The generic `d=2` positive-genus infinity exclusion
  is morphic, not an abstract rational-domination theorem.
- Every audited proper-block consumer remains valid: smooth, nonnormal and
  normal-singular quadratic closures; the q8 and q6 fixed-presentation
  closures; ramification attachment/lattice and ruling/Euler clients; and the
  provisional D3 weighted-boundary obstruction all invoke the actual morphic
  first leg.  Their stated presentation and occurrence scopes remain.
- Any claim about a merely rationally dominated open surface whose only
  obstruction is boundary genus, a boundary cycle or positive log
  plurigenus is `OPEN` unless independently reproved.

This integration is a reviewed interface correction, not a proper-block
existence theorem, presentation-selector theorem, polynomial map,
counterexample, or resolution of JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7280`.
- Body SHA-256:
  `c07e64782cf0ed608cab896b35d7bd0de45828f20d8ba3f279e4cb00eb870a98`.
- Frozen basis: `d4cc6554c3f2d64561259dc2cbef1de9ea956e3f`.
