# Selected-Q8 sparse bidegree and residual-contact bound

Date: 2026-08-25  
Status: **PRODUCER-EXACT MOD-127 CYCLE BOUND; hostile review required**

## Exact bidegree bounds

Write the closure of the relevant pushed-forward source cycle in
`P1_w x P1_v` as class `(A,B)`.  With the convention `O(d_w,d_v)`, a vertical
fibre `w=alpha` has class `(1,0)` and intersects the cycle in `B`; a horizontal
fibre `v=beta` has class `(0,1)` and intersects it in `A`.

The same six exact source supports used in the frozen sparse-degree lemma were
paired separately with:

```text
vertical:    w-alpha=0,
horizontal:  v-beta=0, cleared as x3-(beta+2)*x5=0.
```

Origin-augmented seven-dimensional affine-BKK calculations on AWS give

```text
A <= 176    (horizontal fibre; Box02; controls 1,1),
B <= 550    (vertical fibre; Box03).
```

The generic `(1,1)` target-line calculation frozen previously also gives

```text
A+B <= 658.
```

The same generic-isolated-intersection audit applies: relevant curve
components are regular at the charged base points, their finite boundary and
collision values are avoided by the generic fibre, and Rojas's affine sparse
bound counts the resulting isolated roots even in the presence of unrelated
positive-dimensional components.

## Bound after the forced H component

The newly frozen breadth theorem supplies at least one pushed-forward
`H`-summand.  Since `H` has bidegree `(21,190)`, removing all `H`-supported
summands leaves an effective non-`H` residual class `(a,b)` satisfying, safely,

```text
a <= 176-21  = 155,
b <= 550-190 = 360,
a+b <= 658-(21+190) = 447.
```

On `P1 x P1`, intersection of `(21,190)` with `(a,b)` is

```text
I(H,R) = 190*a + 21*b.
```

Under the three constraints its maximum occurs at `(a,b)=(155,292)`:

```text
I(H,R) <= 190*155 + 21*292 = 35,582.                   (1)
```

This improves the separate-coordinate-only value `37,010`; the `(1,1)` bound
must not be discarded.

## Consequences and scope

Equation (1) is a fail-closed budget for **non-H residual components**:

- a single residual source point with verified local contact order at least
  `35,583` is impossible;
- if all eight corrected Q8 contacts are residual and each has verified order
  at least `M`, then `8M<=35,582`; hence `M=4,448` forces at least one of the
  eight contacts onto an H-supported source component.

It does not force all eight contacts, identify a unique source component, or
prove degree one.  Indeed `B<=550` still permits two `H` pushforward
multiplicities (`2*190<=550`), so the desired uniqueness shortcut would require
a sharper bound `B<380` or a different component argument.  The p127 Q8
factorization `1+1+1+5` also means Frobenius propagation from one contact gives
at most the quintic orbit; the three rational contacts remain separate.

No characteristic-zero no-merger, Taylor realization, terminal differential,
or trajectory conclusion follows from (1).

## Custody

```text
horizontal result.json  2c78f62cc63578bb99ad688e8fe0a8e06e2b49bb75a2ab1006c333461101ff56
vertical result.json    ec90ca1baa563c433b49a394db49ee2feba9c52cf32add5f31c7f22fa513652c
bidegree.py             a818bdbe69da12fd7b895a61348013e572288512b558c5b30250853fb131a608
run_remote.sh           c990bc5eb8748cec40214192aef926d5b16f551295de42f669564cf62aa3723d
```
