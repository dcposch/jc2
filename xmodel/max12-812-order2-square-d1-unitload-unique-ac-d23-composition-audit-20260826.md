# Audit: unit-load D1 strict unique-`AC`, `d=2,3` composition

Date: 2026-08-26

Status: **LITERAL COVERAGE AUDIT; COMPOSITION NOT YET PROMOTED.**  Every
finite baseline now has an exact-Q producer verdict; the only unresolved
finite lifecycle gate is independent review and narrow promotion of
`a=8,d=3`.  This file does not import a navigation-only support census as a
theorem.

## Exact domain

On the normalized integral unit-load horizontal chart put

```text
q=ord(k10)=0,  a=ord(A)>=1,  c=ord(C)>=3,
r=ord(R)>=2,   d=c-a in {2,3},  s=r-a>=0.
```

Strict comparison of the five unit-load lower-hull weights

```text
AC=a+c, C2=2c, R3=3r, RC=1+r+c, A2=4+2a
```

gives the strict unique-`AC` condition

```text
a+3*s>d.
```

Together with `r>=2`, its least integral `s` is

```text
d=2: s_min=1 for a=1,2; s_min=0 for a>=3;
d=3: s_min=1 for a=1,2,3; s_min=0 for a>=4.
```

Thus the finite `a<=9` residue has exactly eighteen closed `R`-order
baseline tails, one for every `(a,d)` with `1<=a<=9` and `d in {2,3}`.
The two omitted `s=0` points `(a,d)=(2,2)` and `(3,3)` satisfy equality
`a+3s=d`; they are equality faces, not gaps in this strict cell.

## Literal finite partition and custody

The following rows are disjoint and exhaust those eighteen baselines.
`r_floor=a+s_min`; each theorem is a closed tail and does not invert a
leading coefficient of `R`.

| baselines | count | lifecycle state | immutable authority |
|---|---:|---|---|
| `(1,2,2)`; `(2,2,3),(2,3,3)`; `(3,2,3),(3,3,4)`; `(4,2,4),(4,3,4)`; `(5,2,5),(5,3,5)`; `(6,2,6),(6,3,6)` | 11 | promoted empty on `D(p*k0)` | promotion `8b92c22bebae73e3efd793c7c7541c53caf8e956f5ce181240c164f3362864da`; review `841f0d6ccbb596fa4ace3f08760f039eb288030efa91075112e915d1320592a3` |
| `(1,3,2)` | 1 | promoted empty on `D(p*k0)` by the exceptional pole-three client | promotion `2ff74f6914a3316104d7a406ca6d6d4ede2cf8332221dfcccd7461f9d925176e`; review `984783eab8342d2523a6e1d7365785f5d37746d0393fc30cfad206bb5658b774` |
| `(7,2,7),(7,3,7)` | 2 | promoted empty on `D(p*k0)` by the load-tie client | promotion `b5c38f1b2e2e5ec6f2ac32fb350f11686dac5cb45eabe8cf1ea67d20726bd362`; review `1ae7f6d95b7d707b3fe54b07a59fbd103435d13b4a0a764b6495215785d26530` |
| `(8,2,8)` | 1 | promoted empty on `D(p*k0)` by the load-first split | promotion `9cc6870289ec0697e438c3999616194d3955e3bc875cd69cad855fd16d28c3b9`; review `0558ea1e668245b983e217ef329a6ccf0baf5a8f5769f669f43a245d24990e21` |
| `(8,3,8)` | 1 | producer triple PASS; hostile review live | target-shadow split producer freeze `4c9b9e441d666b91d8255af8aca3978eeccd8263775b33184a1e3334f0fd51b2`; exact `Q`, `F_65519`, and `F_65521` passed with zero swap; no promotion is imported before review |
| `(9,2,9),(9,3,9)` | 2 | promoted empty on `D(p*k0)` | promotion `551ca2f6f8aaf75fd67019d055e43ae862150de62d51cb0bd8755d4d0085a19a`; review `f922fab0828ff0470ada62fa22bd84a9383233b27948bca12726f1c3aa7785f5` |

The low-`a` support miner was used only to navigate to this chamberwise
partition.  Its allocated-root rule is not an authority for the `a=7`
load tie or the `a=8,9` load-first/target-shadow chambers.

## Infinite tail

The separately promoted `C`-contact source-ceiling theorem closes every

```text
a>=10, c>=a+1, r>=a
```

source on `D(J)`.  Therefore it contains both `d=2,3` strict unique-`AC`
tails, for every `s>=0`, and has immutable custody

```text
promotion 470ea478c9463d62d39a428962fd9dd5845f4bf882388f84594c82a211634fb8
review    f75d885da6b39af85127540fa8ede8a17d1f83a3a2d5279bb5c641f2bd98e15b
```

Raising `C` or `R` is part of that closed theorem; it is not an inference
from sampled exact contacts.  For a common composition statement the open
is `D(p*k0*J)` after the registered square/D1 gates.  Since a Keller source
has `J` a unit, the campaign normally names this `D(p*k0)`.  Until the two
finite lifecycle gaps above close, this localization reconciliation is only
an audited route, not a new composition theorem.

## Exact remaining gate

No strict unique-`AC`, unit-load `d=2,3` contact is unassigned.  Promotion
of their union requires, in order:

1. completion of the live independent hostile review and a narrow promotion
   for the frozen `(8,3,8)` producer;
2. a distinct hostile review of this literal partition, including
   localizations, exact/closed-contact language, load-jet timing, and the
   equality-face firewall;
3. only then, a composition promotion whose conclusion is arcwise emptiness
   on the common open.  It must not silently upgrade mixed theorem types to
   a uniform scheme-theoretic assertion.

## Firewall

This audit says nothing about the equality faces `a+3s=d`, another primary
or tied leading face, positive-order leading `k10`, `p=0`, `k0=0`, an
excluded zero/infinity or terminal/Taylor chart, global source landing, the
whole square component, exact order two, `(8,12)`, maximum twelve, or JC2.
In particular, `(8,3,8)` remains unpromoted until its live hostile review
returns; neither the passing producer, neighboring cells, nor the support
miner may be extrapolated beyond the producer's exact scope.
