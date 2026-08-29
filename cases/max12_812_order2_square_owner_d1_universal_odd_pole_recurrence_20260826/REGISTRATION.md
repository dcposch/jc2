# Registration: universal odd-row pole-recurrence miner

Date: 2026-08-26

Status: **PREREGISTERED SYMBOLIC THEOREM / DUAL-AWS EXACT REPLAY.**

The first dual launch failed closed before mathematics because the wrapper
precreated the compiler's output directory. It produced only the expected
`output already exists` guard and has no verdict. V2 changes that single
wrapper line before a fresh source freeze and fresh tags.

## Theorem under test

Put `s=p/2` and encode the ordinary odd Laurent rows by

```text
Y(x)=sum_{m>=0} h_(2m+1) x^m.
```

The frozen lower-unitriangular Faber transport is equivalently

```text
Phi(x)=(1-s*x)^(-1/2) Y(x/(1-s*x)).                 (F)
```

An exact pole-`q` Laurent basis term has

```text
Y_(q,e)(x)=x^e/(1+s*x)^q,       0<=e<=q-1,
```

so (F) sends it to

```text
Phi_(q,e)(x)=x^e(1-s*x)^(q-e-1/2).                 (B)
```

Fix a terminal odd row `2M+1` and a certified source pole ceiling `r<=M`.
The coefficient vector of

```text
W_(M,r)(x)=(1-s*x)^(M-r-1/2)                       (W)
```

annihilates the terminal coefficient of every pole `q<=r`: multiplying
(B) by (W) gives a polynomial of degree

```text
M-r+q-1 <= M-1.
```

Thus `[x^M](W_(M,r) Phi_(q,e))=0`. This is a formal identity over
`Q[p]`, so substitution of an arbitrary moving connection `p(sigma)` and
reduction modulo any sigma ceiling commute with it.

The cutoff is sharp as a uniform pole statement. At the first outside pole
`q=r+1,e=r`, the same coefficient is `(-s)^(M-r)`; at
`q=M+1,e=M` it is `1`.

For `M=3` the two campaign specializations are

```text
r=2:  1, -p/4, -p^2/32, -p^3/128,
r=3:  1, +p/4, +3p^2/32, +5p^3/128.
```

## Mechanized acceptance

The standalone AWS miner must:

1. reconstruct (B) coefficientwise from the ordinary basis and the Faber
   matrix for every `1<=M<=24`, every `q<=M+1`, and every `e<q`;
2. verify all annihilations `q<=r<=M` exactly over Q and independently in
   `F_65521`;
3. run the first-outside-pole and terminal-pole negative controls for every
   tested `(M,r)`;
4. recover both row-seven coefficient vectors with exact signs;
5. when composed with the repaired D1 `a=10` inventory, rehash that inventory,
   require its mechanically derived full jet maxima
   `A7,C10,R6,k10_6,k6_10,k2_6,p10`, and reject any primitive family of pole
   greater than three through grade 38.

The finite grid is a software control. The unbounded statement is the formal
degree proof above; it is not inferred from the grid.

## Firewall

This artifact proves a reusable row functional once a complete source pole
ceiling and terminal-row placement have separately been established. It does
not establish any source inventory, target timing, chart cover, D1 fan cover,
square-component theorem, order-two theorem, maximum-twelve theorem, or JC2.
