# Registration — exact maximum-12 partial-`y` Kummer preflight

Date: 2026-08-24

## Registered question

Starting only from the hostile-reviewed partial-`y` shear/UFD history, what
is the exact first route for the two primitive maximum-twelve frontiers
`(8,12)` and `(9,12)`?

The registered producer claim is limited to:

1. the residual conditions on `H=deg h` and the leading UFD powers;
2. the minimal Kummer-order splits, including the proper order-two class for
   `d=4`;
3. the exact next Jacobian row, depression, and first mismatch constant;
4. retention of every original Taylor boundary;
5. the common `(dr,ds)` binary-W/common-power algebra; and
6. a two-metric comparison: raw constant-W width versus Kummer branch-tree
   width.

It does not register a high-row Faber landing, a component classification,
emptiness of either frontier, maximum-twelve coverage, or a JC2 inference.

## Frozen theorem inputs

```text
xmodel/as109-partial-y-history-stop-20260824.md
  6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe
xmodel/as109-partial-y-history-review-grok-20260824.md
  f9d547f0f17dc3557ed8edce19912b4930dc2125542c7f9b3e4782c554a03afd
```

No maximum-eleven composition theorem or `(6,9)` exclusion is an input.

## Exact claims to review

For `m=dr`, `n=ds`, `gcd(r,s)=1`, after normalizing
`a_m=h^r`, `b_n=h^s` and adjoining `u^d=h`, put

```text
A=a_(m-1)/u^(m-1),   B=b_(n-1)/u^(n-1),   delta=sA-rB.
```

The next row must be independently reconstructed as

```text
d*u^(d(r+s)-1)*(sA-rB)'=0,
```

and the depression `z=uy+A/(dr)` must have second mismatch `-delta/r`.
For every nontrivial class order `e|d`, both `A` and `B` have character one,
so the fixed constant `delta` is zero.  For the trivial class, Gauss makes
`u` polynomial and no character forces `delta`.

The cell routes must be exactly

```text
(8,12): 4|H; orders 4,2,1; delta=3A-2B;
(9,12): 3|H; orders 3,1;   delta=4A-3B.
```

The order-two branch must retain every even lower target weight; it may not
inherit mod-four vanishing.  The depressed `z^11` slot is not a later target
constant and must not be counted.

Both original coordinate boundaries must be retained through

```text
u^ell/ell! * partial_z^ell f(A/m) in k[x],
u^ell/ell! * partial_z^ell g(A/m) in k[x].
```

Conditionally on a constant binary-Jacobian landing, the exact algebra must
be

```text
W=r*f*g_z-s*f_z*g,
W=0  <=>  f=K^r,g=K^s,deg K=d,
f*(f^s-g^r)'-s*f'*(f^s-g^r)=-W*g^(r-1).
```

## Mandatory adversarial controls

The replay must type these divisor classes exactly:

```text
d=4 order 4: h=x(x-1)(x-2)(x-3)
d=4 order 2: h=x^2(x-1)^2
d=4 order 1: h=x^4
d=3 order 3: h=x(x-1)(x-2)
d=3 order 1: h=x^3
```

At `K=z^d+z+1`, the exact depressed constant-W tangent data must be

```text
(8,12): ambient 18, positive rows 17, rank 11, kernel 7;
(9,12): ambient 19, positive rows 18, rank 11, kernel 8.
```

The producer may say only that the raw gate is smaller for `(8,12)` and the
Kummer branch tree is simpler for `(9,12)`.  It may not assert an overall
cheaper cell before high-row integration.

## Replay / stop rules

Run:

```sh
python3 cases/max12_partial_y_preflight_20260824/replay.py
```

Any theorem-input hash mismatch, residual-class mismatch, missing proper
Kummer order, nonzero common-power Wronskian, binary-identity failure, or
tangent-rank change stops the claim.  PASS strings are regression markers,
not substitutes for the report's exact derivations.

The frozen canonical JSON payload SHA-256 is
`eb1e72d69193cded40438981907f62972725945c39a18e34891dd8f5b3645bf1`.

No canonical, ladder, coordination, or frozen predecessor file is in scope.
