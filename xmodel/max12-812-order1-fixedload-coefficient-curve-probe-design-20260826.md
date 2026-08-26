# `(8,12)` order one: fixed-load coefficient-curve reconnaissance

Date: 2026-08-26

Status: **PREREGISTERED AWS-ONLY NAVIGATION PROBE; NO COMPONENT-COVERAGE,
GENUS, OR ORDER-ONE VERDICT.**

## 1. Exact source and gauges

```text
69f9e12c0fa1e98bb7bc4dda87ab00c7f87ce2fd9c80a4bf210d216ee1bd2d9f
  cases/max12_high_row_probe_20260824/shared_faber_probe.py
d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036
  xmodel/max12-partial-y-shared-faber-probe-20260824.md
e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c
  xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md
a4d7d6a1173b5a0b785aa61a4c80ad5f46e4ea83f1d73103917c425608666633
  xmodel/max12-812-terminal-power-belyi-order1-theorem-20260825.md
e322d508c2af66aebb408b2794bd017b05e96cf9ca67f0fc74be8407406f67e1
  xmodel/max12-812-terminal-power-belyi-order1-review-grok-20260825.md
```

For a monic depressed octic

```text
f=z^8+a6 z^6+a5 z^5+...+a0,
w=f^(1/8),
F_j=[w^j]_+,
g=sum_(j=0)^12 h_j F_j,
```

the reviewed target gauges set `h0=h4=h8=0`, while `h12=1`.  On the
order-one leaf there is no character deletion.  The nine post-gauge constants
are therefore exactly

```text
h1,h2,h3,h5,h6,h7,h9,h10,h11.                       (1.1)
```

With the reviewed convention

```text
H(w)-g(z(w))=sum_(ell>=1) r_ell w^(-ell),             (1.2)
```

the first six `r_ell` are constants along a genuine source and
`8 r7'=j/u`.  Since `j!=0`, the genuine source map into coefficient space is
nonconstant through `r7`; this does not license saturation by `r7`, which may
vanish at isolated points or even on an unrelated fixed-load component.

## 2. Two preregistered fibres

Write the nine entries in the order (1.1), followed by the six fixed values
of `(r1,...,r6)`.

```text
tuple A:
  h=(2,3,5,7,11,13,17,19,23)
  r=(29,31,37,41,43,47)
  characteristic=32003

tuple B:
  h=(53,59,61,67,71,73,79,83,89)
  r=(97,101,103,107,109,113)
  characteristic=65521
```

These are deterministic navigation samples, not generic points in a
theorem.  Prime/load agreement is evidence only for choosing a successor.

## 3. Exact compiler contract

The AWS compiler must pin every source byte above and run the reviewed shared
Faber reconstruction before emitting a client.  For each tuple it must:

1. reconstruct `F_0,...,F_12` and `g` with precisely the gauges in §1;
2. verify all eleven high Jacobian rows against every `a_i` direction;
3. revert `f(z(w))=w^8` far enough to compute `r1,...,r7`, with the sign in
   (1.2), and verify the inverse identity through the consumed order;
4. emit the six exact equations `r_l-r_l^fixed=0`, `1<=l<=6`, in
   `F_p[a0,...,a6]`, and retain `r7` as a separately printed/hashed graph
   function;
5. compute standard-basis dimension, a capped minimal-prime decomposition,
   and whether `r7` is constant on each returned component when that check is
   computationally available;
6. compute a preregistered plane graph using

   ```text
   s=a0+2a1+3a2+5a3+7a4+11a5+13a6,
   t=17a0+19a1+23a2+29a3+31a4+37a5+41a6,
   ```

   and report its eliminant without calling its arithmetic genus a
   normalization genus;
7. separately report the `a6!=0` chart and the `a6=0` complement, without
   treating either one as full component coverage.

The client must not saturate by `r7`.  It may graph a fresh variable
`rho-r7`, compare contractions, and reduce `r7-c` on minimal primes.  Any
timeout or failed decomposition is no verdict.

## 4. Interpretation firewall

A genuine order-one source with the sampled constants would give a
nonconstant rational map from `P1_x` into a component of this necessary
coefficient fibre, and its `r7` coordinate would be nonconstant.  A proven
positive genus of the normalization of every source-relevant component would
exclude that sampled fibre.  A positive genus of a plane eliminant, or of
only the `a6!=0` chart, does not.

Random fibres do not cover the fifteen-dimensional load space.  This probe
does not prove generic flatness, characterize the exceptional discriminant,
impose the reviewed pure-power terminal core, impose either original Taylor
boundary family, close order one, close `(8,12)`, prove maximum twelve, or
prove JC2.
