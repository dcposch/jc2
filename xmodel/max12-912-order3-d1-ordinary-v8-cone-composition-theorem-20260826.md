# Composition theorem: ordinary D1 coefficient-infinity V8 cone

Date: 2026-08-26

Status: **EXACT RELATIVE CLOSURE OF GENUINE COEFFICIENT-INFINITY DIRECTIONS
IN THE FROZEN ORDINARY SOURCE/V8 CONE; NOT A GLOBAL D1 OR JC2 THEOREM.**

## Frozen reviewed inputs

| Input | SHA-256 |
|---|---|
| Exceptional common-cubic support review | `a274c8d8e0883ce7606f31f69803a293afb15ad48fe9d401191cac1cdbe1daee` |
| Squarefree order-20 theorem | `1b6e629affdc5a73995e0ab2d7f051ad772d92f75bb61e67362782fcb8f5b4ac` |
| Squarefree order-20 hostile review | `6883ef76710176ae9e091249224730e3ff181fa76c66c767b53b26c770c101d5` |
| V8 fixed-chart promotion | `b503f6a70c39c256ba27f27823d5788bf5787badc507efa3079433064eb142e3` |
| V8 hostile review | `2c3dbbd50089892197dd5ad5c0fb90776b5c2d2dea4ac2752f3b1a3218cc7d4c` |
| V9 unit-axis promotion | `b8a1122709bca351e396f7a2985cc65e79138c6079ec52d56cfb10fc93125df2` |
| V9 hostile review | `f81c5b054c2ff331176bd39005ad8f826b92efbfd5e16b1f7f20ae7dcbab7226` |
| V10 weighted two-chart promotion | `a4f6e8646f1f0bd198c0473f1588d3f21bfb6c167a23db48e173bcd83a7d3158` |
| V10 hostile review | `a497ce3e63569bedfaa3ba2c547e90bc86ade50e6db9d2895693332a67a8ad1e` |
| V11 producer result | `c7d42e2d38fc8ca3f283c768287a87f7e52dba0678aa41412f6be5b9d62db925` |
| V11 freeze | `466a0665f8c6a69a318a91ccd585517978767da9bf2b0f8b28ad098d1906d13d` |
| V11 hostile review | `fe00bdbb2d310dbd618b8b3334544ba983c8f7bd108961a28441e568c45e39b9` |
| V11 promotion | `abe8720ecdce3eb33f3c9f98a7016161fc7aad09286fae5073f06ace37524fac` |

The squarefree SHA in this table is the correct live and frozen theorem SHA.
The different value printed in the V10 review prompt was a prompt-only
transcription error, explicitly recorded by the V10 promotion; it never
entered a source closure, compiler, certificate, or theorem.

## Exact relative scope

Work over a characteristic-zero finite constant extension `L` in the
ordinary isotrivial eight-tail source charged by

```text
67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623
  independent_reconstruct.py.
```

Use the literal V8 multipliers, the strict positive radial/Rees coordinate
`Lambda`, and the registered V8 open weight cell

```text
alpha=15/2,  beta=5+u,  delta=5+v,
u>0, v>0, T=wt(tau)>0, eta>=0
```

after the licensed coordinate normalizations and weighted-chart changes.
Let `k,mu,nu` be arbitrary constants in `L`, with

```text
kbar=Lambda^6*k,
r_3=Lambda^15*mu,
r_6=Lambda^18*nu,
r_8=Lambda^20*(1+tau).
```

A **genuine coefficient-infinity direction in this theorem** means a
nonzero projective leading coefficient vector on this strict
associated-graded divisor, together with a positive radial/Rees direction,
inside the preceding source and weight cone.  The zero affine-cone vector,
a filtration in which `Lambda` is not radial-positive, and a leading form
that appears only after regrading are not points of this relative problem.

## Theorem

Within the exact scope above, the reviewed squarefree obstruction, the
smooth double-root V8/V9 obstruction, the weighted triple-root V10 cover,
the V11 all-constant-load uniformity, and projective retirement of the
central vertex exhaust every genuine coefficient-infinity direction.
Equivalently, no reduced projective leading direction in this frozen
ordinary source/V8 cone survives the eight loaded equations.

More precisely, the possibilities form the following exhaustive partition.

| Leading situation | Exact disposition |
|---|---|
| Common cubic with `Delta=-4p^3-27c^2 != 0` | The reviewed moving-cubic order-20 theorem excludes the squarefree open, uniformly in every constant `k,mu,nu` and every strict positive slope. |
| `Delta=0`, nonzero projective centre, double-root axis a unit | Put `p=-3a^2`, `c=2a^3+h`.  V9 transports the complete V8 identity etale-locally on `D(a)`; V8 gives unique least term `Lambda^20` throughout the registered open cell.  V11 restores all constant loads and proves that every load monomial has positive closed-corner margin, so the equality face is unchanged. |
| Positive-axis degeneration toward the weighted triple-root chart | V10 with `wt(a)=1`, `wt(h)=3` covers all noncentral directions by `h=a^3s` and `h=t^3,a=tb`.  The a-chart scans the full witness; the h-chart squarefree open is sent to the reviewed order-20 theorem; `4b^3+1=0` is the overlap `s=-4` and the opposite already-covered double-root wall.  V11 makes the cover uniform in all constant loads. |
| `a=h=0` at the selected leading order | All eight graph coefficients are zero.  By the reviewed support theorem this is the affine cone vertex, hence the irrelevant point of `Proj`, not a projective coefficient-infinity direction. |
| Nominal `v(Lambda/a)<=0` at a nonzero discriminant-zero point | Projective normalization makes `a` a unit, so positive radial `Lambda` gives `v(Lambda/a)=v(Lambda)>0`.  The nominal remainder is a finite/`Lambda`-leading order choice, or a zero leading vector requiring regrading; it is not another live point of this strict chart. |

## Why the partition is exhaustive

The hostile-reviewed exceptional-support theorem identifies the reduced
strict coefficient-infinity support with the common-cubic graph

```text
C=z^3+p*z+c,
```

projectively `P(2,3)`.  A nonzero point of that graph is either squarefree
or lies on `Delta=0`.  The squarefree open is the first row of the table.
Every nonzero discriminant-zero depressed cubic has

```text
p=-3*a^2,  c=2*a^3,  a!=0,
```

and all such representatives are the single weighted-projective class
`(-3:2)`.  V9 treats its unit-axis neighborhood; V10 treats every
noncentral weighted direction toward the affine triple-root vertex.  The
only remaining affine point is `(p,c)=(0,0)`, which is absent from `Proj`.
Thus there is no fifth reduced projective leading direction to test.

V11 closes the only load firewall in this partition.  Its 62-term witness
has SHA

```text
c0f1552c06650e321db954ab99788324f59e52dea94fd8e7dfbdfbb3931aeab6,
```

and its 14 load-sensitive terms have SHA

```text
dbd78a81294d473aa043af6e0b0c87ce8050ae3e906a20d07395143d4371d75f.
```

All 14 lie strictly above the old face, with minimum margin 1.  Hence
special, zero, and nongeneric constant load values cannot reveal a hidden
direction by cancellation on the equality face.

## Relative D1 verdict

**Yes, the strict coefficient-infinity direction problem is closed inside
this frozen ordinary source and registered V8 cone.**  If a cyclic-D1 client
has already been placed in this exact ordinary-tail chart, has constant-field
loads as declared by the source, and lands in the registered V8 weight cone,
then it has no genuine coefficient-infinity leading direction.

**No, this is not a closure of D1 as a whole.**  The composition does not
prove that every D1 client lands in this ordinary source chart or in this
normal cone; it does not establish a rational constant-field section,
Taylor landing/accessibility, or global source-chart coverage.  Accordingly
it is a relative no-direction theorem, not a global no-section theorem.

## Sharp outside-scope remainder

- In the frozen cyclic-D1 source, `k,mu,nu` are constants in `L`.  V11 covers
  every such value.  Formal- or Puiseux-series motion of the loads is a
  broader DVR-deformation problem, not a residual value of the actual D1
  load parameters; it is not claimed here.
- A regraded higher-order leading form, a `Lambda`-leading filtration, a
  different passport, or another ordinary/nonordinary source or normal
  chart is genuinely outside this source cone.  Such a regrading can be
  necessary when the selected leading vector is the cone vertex.
- Embedded or nilpotent thickness at the irrelevant ideal is not classified.
  It creates no additional reduced projective direction in this theorem,
  but no global thickness or lifting theorem is inferred.
- Global landing/accessibility, a full D1 exclusion, other passports and
  cells, maximum twelve, and JC2 remain open.

No new algebra computation is used in this composition: the theorem is the
set-theoretic/projective partition and exact logical composition of the
hash-pinned, independently reviewed inputs above.
