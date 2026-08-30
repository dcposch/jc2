# Coordinator integration: normalized K00 `e=2,m=2,h10=1` closes at G13

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen basis: `4c91d6fc398d1b4f2b8ca1a11d69c4bb3fef9c0d`  
Lifecycle: **BINDING INTEGRATION / FINITE-JET FIELD-POINT SCOPE**

## 0. Disposition and custody

Opus 5 independently reviewed the two provisional generations

```text
eda4f40b452ef1f68d53d82ff22c5ec6a4a74147b7f6785b3dc9cc1148137db8
  G12 branch-split producer
cc8d84f8d5deeb8ee3852901b657e65b7499c397fbff66ba2b8361ad8cd4db15
  G12 replay
b352e26e7748e6b7eb31b5ae081a6ba6a8ea7843ce58e457c27e3557c5d88e44
  G13 closure producer
a508b9853490d82f8a9c7c6242331b5c33298104249a216a9bb418c949e5403d
  G13 replay
```

against the promoted G11 parent `8ba031e8...`, the frozen 569 tails, and the
exact sparse `Q(i)` engine.  It returned `CONFIRM_WITH_CORRECTIONS` for each
generation and `CONFIRMED` for their whole-cell composition.  Its
sandbox-attested raw review body is

```text
917ec18c19362298052fb15170d4a86a9d51b58fa378a405d6be8a15448d707e
  xmodel/k00-ram-e2m2-h10eq1-g12-g13-closure-hostile-review-opus5-20260830.md
```

and the sealed full-file SHA-256 is
`04b765363936656bb47fc03d71265c3181ff691f8cc17e257c3efe3e3cccba84`.
The schema-v2 receipt has exit code zero and unchanged prompt, adapter,
launcher, Seatbelt profile, validator, fallacy appendix, and composed-prompt
hashes.

The reviewer used a fresh sparse-polynomial/series engine over
`Q[I]/(I^2+1)` importing no campaign replay.  It rebuilt G12/G13 directly from
all 569 tails and supplied decisive row/image mutations.  The frozen compiler's
coordinate images, graph map, and load prefactor remain a shared modelling
layer; they were transcribed rather than rederived, and retain their separate
compiler review dependency.

## 1. Exact G12 theorem

Work over an algebraically closed characteristic-zero field on the normalized
generic K00 support

```text
Lambda=tau^2,       C6=1,             ord_tau(d)=2,
k10[0]=0,           k10[1]!=0,        Jdet[0]!=0,
d[2]!=0.
```

Relative to the reviewed G0--G11 transition tree, the old `n=4` rank-one
branch is empty at G12 on both Gaussian signs.  If

```text
s=epsilon*8i*t,       p=epsilon*8i*q,       q!=0,
A(N5)=B(N5)=0,
```

then, with all later displayed surface, normal, and K10 coefficients free,

```text
G11_6=0,                G12_6=epsilon*i*q^3/32.       (1.1)
```

No `kappa,kappa2,kappa3,N6,N7,N8` term can cancel (1.1).  Fresh `n=5`
rank-one points on both signs and rank-two points have exact fixtures through
G12, so the same open face is nonempty at G12.

Corrections adopted from review: the quoted raw row counts are after imposing
the leading cone form, not before all branch specialization; the old-branch
fixture fails all seven G12 rows rather than only row six; and the normal-map
kernel has dimension five on the rank-one wall `Delta=0`, not four.  None
affects (1.1) or the branch inventory.

## 2. Exact G13 closure

For every fresh `n=5` point, literal row-six extraction gives

```text
G13_6=(t/8)G11_1-(s/32)G11_2+(35*kappa/2^23)P4,
P4=s^4-384s^2*t^2+4096t^4.                           (2.1)
```

On rank one, `s=-epsilon*8i*t` and
`P4=32768t^4`, so both signs die because `kappa,t` are nonzero.

On the rank-two open `Delta!=0`, the `N8` image satisfies

```text
I3=-I1/8,            I5=-I1/128.
```

Thus

```text
T13=G13_5+G13_3/8+3G13_1/128                         (2.2)
```

annihilates every `N8` slot.  The review strengthens the producer: already on
`G11_1=G11_2=0`, without any G12 equation or reduction modulo `P4`,

```text
T13=(35*kappa/2^17)s*t*(s^2-64t^2).                 (2.3)
```

The sole rank-two image determinant is `-(9/2^20)Delta`.  Equations `P4=0`
and `s*t*(s^2-64t^2)=0` have no projective common point; they force
`s=t=0`, contradicting `d[2]!=0`.  Hence every fresh rank-one and rank-two
G12 survivor dies at G13.

The review also verifies that `N9,k10[4],S5,T5,S6,T6` cannot arrive, that row
six has minimum `d`-degree three, and that the producer's rank-one and
rank-two old-pass/new-fail controls reproduce exactly.

## 3. Binding whole-cell theorem

Combining the promoted G0--G11 tree, the independently rebuilt old-`n=4`
death (1.1), and the fresh-`n=5` closure (2.1)--(2.3) gives

```text
V(G0,...,G13) intersect V(k10[0]) intersect D(k10[1])
                intersect D(d[2]) = empty.            (3.1)
```

This is set-theoretic emptiness of field points over an algebraically closed
characteristic-zero field on exactly the declared normalized
`e=2,m=2,h10=1` support.  The G13 rank-two terminal does not consume the G12
survival equations, so the composition is stronger and less dependency-
sensitive than the producers stated.

Equation (3.1) is not ideal-theoretic or scheme-valued emptiness.  It says
nothing about `h10>=2`, `h10=infinity`, another `(e,m)` or support, compatible
higher jets, a formal arc, occurrence/source reachability, attainment,
algebraization, a polynomial Keller map, a counterexample, or JC2.

The cheapest nonduplicate literal cell gate is `h10=2` on the same
`e=2,m=2` support: the K10 load shifts by one and `A10` arrives two grades
later.  The independent global priority remains source occurrence and
scheme-theoretic truncation images rather than treating another isolated cell
as a completeness theorem.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5324`.
- Body SHA-256:
  `635cd9f4fe002087a8dfd337120acbd3163a1a97d03f03e3ec79782fc83258ba`.
- Frozen basis: `4c91d6fc398d1b4f2b8ca1a11d69c4bb3fef9c0d`.
