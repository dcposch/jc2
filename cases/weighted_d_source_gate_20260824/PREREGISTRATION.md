# Preregistration — `WEIGHTED-D-SOURCE-GATE-20260824`

Frozen: `2026-08-24T06:34:26Z`  
Basis: `dd11599b07eb05591b5c006791005eef19457d8e`  
Frozen synthesis SHA-256:
`76d9b7685771f65138fcb3c3dba1cfdd1ab104a9a5b21a7e3262c971f96ff790`

## Scope and first-stop rule

This gate asks whether the promoted, producer-owned full polynomial source
already supplies enough typed x-side data to put the exact weighted change

```text
C = U_g/U_f,                 R = U_f^3/U_g^2,
U_f = R*C^2,                 U_g = R*C^3
```

into a declared linear/recognizable state category.  It uses the unreduced
Euler product and the first two genuine factor levels, `q=t^42` and `q^2`.
It does not infer a source map from modular D rows, graph witnesses, origin
assignments, or the external P4P1 sidecar symbols.

The first missing producer registry, tangent classification, or chain-rule
map stops the gate.  No band 28/deeper D, D43 integral work, syzygy, solver,
or generic state search is allowed.

## Predeclared source tangent

The required domain is the producer-certified Zariski tangent

```text
T_src = T_s(S_full)
```

of one named normalized full-polynomial source scheme `S_full` at one named
completion `s`.  It must have stable source labels and must provide, through
factor level two,

```text
Dalpha_1, Dbeta_1, Dalpha_2, Dbeta_2 : T_src -> k,
```

together with every relation, held/derived/independent classification, and
the chain rule from the registered y-source coordinates.  The free formal
ambient span on `dalpha_i,dbeta_i` is permitted only for algebraic identity
replay; it is not a substitute for `T_src` and cannot support `TWO-DRIVER`, a
Hankel pivot, or a recurrence verdict.

In weighted coordinates, the tangent outputs are

```text
Dc_i, Dr_i : T_src -> k,
```

obtained by differentiating the exact rational change at the named unit
series.  No relation such as `U_g^2=U_f^3`, `3 alpha_1-2 beta_1=0`, or
`Dc_i=0` is admitted unless it is present in the producer source ideal with a
replayable tangent consequence.

## Predeclared codomain

The codomain is the unreduced two-level residual target

```text
Y_[1,2] = k[eta] * e_q  direct-sum  k[eta] * e_(q^2),
q=t^42,
```

obtained from

```text
B(Phi,Gamma)
 = (theta Phi-12 Phi)*Gamma_eta
   - Phi_eta*(theta Gamma-18 Gamma)
```

after substituting `Phi_full=U_f*Phi_y` and
`Gamma_full=U_g*Gamma_y`.  Every product-rule and chain-rule term is retained
before any eta selector, row reduction, ideal normal form, or origin
specialization.  The inhomogeneous `42*t^20` does not contribute at these two
factor levels but remains outside the factor multiplication exactly as in the
producer formula.

## Allowed state category

The only allowed category is a causal finite-dimensional `k`-linear
recognizable transducer on the factor index `m` (`q^m=t^(42m)`), with the
Euler counter admitted through the Ore relation

```text
S*m = (m+1)*S.
```

Equivalently, transition/output matrices may be affine in `m`; after the
standard counter augmentation they must give a fixed finite-dimensional
linear representation.  Inputs are the producer-typed letters `Dr_m,Dc_m`,
not freely invented formal letters.  A Hankel verdict requires a nonzero
exact block minor exceeding a producer-declared state dimension in this
category.  A finite window is only a lower bound and cannot prove an
all-depth recurrence.

## Frozen verdict order

Return exactly the first applicable verdict:

1. **`NO-TYPED-SOURCE/NO-QUOTIENT`** — no producer-owned full-source
   registry supplies the named completion, `Dalpha_1,Dbeta_1,Dalpha_2,
   Dbeta_2`, and their chain rule; or the weighted action is not a covariant
   action on that source.
2. **`TWO-DRIVER`** — the source is typed, but the `C` tangent survives in
   `Y_[1,2]` independently of the `R` tangent after every sourced relation.
3. **certified linear-state/Hankel pivot** — the source and declared state
   dimension are typed and an exact minor exceeds it.
4. **complete sourced recurrence** — a producer-derived all-depth recurrence,
   projection, and dependency list are proved in the declared category.

The universal identities at levels one and two may be banked under verdict
1, but they do not upgrade missing source provenance into a typed quotient.
