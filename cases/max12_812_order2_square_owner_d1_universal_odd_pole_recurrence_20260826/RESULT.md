# Result: universal odd-row Laurent-to-Faber pole recurrence

Date: 2026-08-26

Status: **DUAL-AWS EXACT PRODUCER PASS; AWAITING HOSTILE REVIEW.**

The first wrapper launch failed closed before mathematics because it
precreated the miner output directory. It printed only `output already
exists` and has no verdict. The single-line V2 wrapper repair was frozen and
run under fresh tags.

## Formal theorem

Let `s=p/2`, and encode the odd ordinary Laurent and Faber rows by

```text
Y(x)=sum_(m>=0) h_(2m+1) x^m,
Phi(x)=sum_(m>=0) Phi_(2m+1) x^m.
```

The campaign's frozen Faber transport is

```text
Phi(x)=(1-s*x)^(-1/2) Y(x/(1-s*x)).                 (1)
```

For a Laurent term with exact pole order `q`, use the basis

```text
Y_(q,e)(x)=x^e/(1+s*x)^q,     0<=e<=q-1.
```

Substitution in (1) gives exactly

```text
Phi_(q,e)(x)=x^e(1-s*x)^(q-e-1/2).                 (2)
```

Fix terminal odd row `2M+1` and a certified pole ceiling `r<=M`. Define

```text
W_(M,r)(x)=(1-s*x)^(M-r-1/2).                      (3)
```

For every `q<=r` and `e<q`, the product of (2) and (3) is

```text
x^e(1-s*x)^(M-r+q-e-1),
```

a polynomial of total degree `M-r+q-1<=M-1`. Therefore

```text
[x^M](W_(M,r) Phi_(q,e))=0.                        (4)
```

This proves the recurrence for all `M,r`, not merely for the finite replay
range. Since (4) is a polynomial identity over `Q[p]`, substituting an
arbitrary moving series `p(sigma)` and reducing modulo any sigma ceiling
commute with it.

The uniform cutoff is sharp. At the first outside pole `q=r+1,e=r`, the
coefficient is `(-s)^(M-r)`; at `q=M+1,e=M` it is `1`.

## Campaign specializations

For row seven, `M=3`. The two source pole ceilings give

```text
r=2: W=(1-s*x)^(+1/2)
     -> 1, -p/4, -p^2/32, -p^3/128;

r=3: W=(1-s*x)^(-1/2)
     -> 1, +p/4, +3p^2/32, +5p^3/128.
```

Thus the previously observed order-two and order-three vectors are forced
by the same generating functional.

## Mechanized controls

The exact AWS miner independently reconstructs (2) coefficientwise from the
ordinary basis and the lower-unitriangular Faber matrix for every
`1<=M<=24`, every `q<=M+1`, and every `e<q`. Each lane records:

```text
38,024 Laurent-to-Faber transform checks;
17,550 q<=r annihilation checks;
300 first-outside-pole sharp negative controls;
all terminal-pole negative controls;
both exact row-seven coefficient vectors.
```

The exact-Q and `F_65521` outputs agree. The finite grid is a software
control; the unbounded theorem is the degree proof above.

The miner also rehashes the repaired D1 `a=10` complete inventory
`884922fede...`, requires its mechanical maxima
`A7,C10,R6,k10_6,k6_10,k2_6,p10`, and verifies that all eleven primitive
families through grade 38 have pole at most three. This composes the general
functional with that particular source ceiling; it does not independently
prove the inventory's completeness.

## AWS custody

The V2 source freeze SHA is
`9990ba104bb7d5bf4e494e5faad59545b6a6500cbdd3db571ee25429d3e13ed0`.
Exact Q ran on Box03 and `F_65521` on r6d under separate tags. Both returned
rc zero, validator PASS, zero swaps, and the same eight marker lines. Exact Q
is the characteristic-zero software endpoint; the theorem itself is the
formal proof above. All retrieved evidence is pinned by `EVIDENCE.sha256`.

## Firewall

This result supplies a reusable odd-row functional after a complete source
pole ceiling and target placement have separately been proved. It does not
prove an inventory, target timing, fan/chart cover, D1 composition, square
component, order two, maximum twelve, or JC2.
