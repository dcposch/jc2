# Hostile review — `(8,12)` order two: corrected affine-`mu2` Faber connection and support

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-exact-square-affine-mu2-faber-connection-classification-20260826.md` |
| Target SHA-256 | `77a3a2f0a04263eb5a476b3e4f3ec9da7db5500481ec73a483d504906e63a89e` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. Charged artifacts were opened only because they are named; no producer status line, no `PASS` token, no proposed-component label, and no printed radical/standard basis is evidence |
| Method | source reading, SHA-256 of the target and the four charged pins, independent inverse-series expansion of `z(w)`, hand composition of every `R1,...,R7`, recurrence reconstruction of the needed Laurent coefficients, and direct expansion of the `c=0` `T`-series, Pell remainder, discriminant, and `R10`; no Singular, Sage, SymPy, msolve, Lean, or CAS Groebner/radical |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target is
`77a3a2f0a04263eb5a476b3e4f3ec9da7db5500481ec73a483d504906e63a89e`,
matching the required pin. Independently recomputed SHA-256 of the four
artifacts pinned in target §0 match those pins. Every path named in the
charged `EVIDENCE.sha256` and `FREEZE.sha256` rehashes to the printed
digest. Producer verdict language, the target's own status line, the
string `PASS_FABER_AFFINE_MU2_PROBE`, the printed radical and `minAssGTZ`
output, both exact-Q and `F_65521` endpoint tokens, and the prior Laurent
support theorem were not used as evidence. No file other than this review
was written.

---

## Verdict

**CONFIRMED.**

The monic inverse of `w=Q^{1/4}` is the displayed series `(1.2)`, with
vanishing `w^{-4}` coefficient. The seven connections `(1.4)` are the
ordinary inverse-root Faber tails of the exact square `f=Q^2` in the
frozen source convention, not a second Laurent numbering: they are the
coefficients of `(H-[H]_+)(z(w))`, which coincide with the frozen tails
because algebraic `H(z(w))` has no negative powers of `w`. In particular
`R4=h4+(p/2)h2` once `h1=0`, so the Laurent identity `h4=-(p/2)h2` on
`c=0` kills the Faber row `R4` without forcing `p*mu2=0`.

The raw polynomial identity
`c^5+128 R5-96 p R3-(12 p^2+32 r)R1=0` holds before any predecessor
equation, radical, localization, or base change. The ideal `(R1,R3,R5)`
therefore contains `c^5`. Every reduced point of `(1.6)` has `c=0`, and
the saturation at `c` is the unit ideal.

On `c=0` the only possibly nonzero Faber rows through seven are `R2`
and `R6`. The reduced support of `(1.6)` is the union of the square
locus `(2.2)` and the affine-Faber graph `(2.3)`. The coefficient in
the second generator of `(2.3)` is `2048*mu2`. The parameter `p` is
free on that graph. The Chebyshev ratios `(2.4)` are the zero-target
section `s=0`, not a third minimal prime.

Both displayed component ideals are prime of dimension three. After
geometric base change the reduced support is exactly their union, so
`rad(I)=I_square cap I_affine` with exactly two minimal primes. The
generalized Pell identity, its discriminant, and `R10=-D^4*(s+D)/512`
are correct algebraic identities on the graph and are not source rows.

This is the normalized seven-row ordinary-Faber face on the exact-square
chart `k10=1`. It is not total-Rees accessibility, not a strict-arc
statement, and not an order-two or JC2 verdict.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order2-exact-square-affine-mu2-faber-connection-classification-20260826.md` | `77a3a2f0a04263eb5a476b3e4f3ec9da7db5500481ec73a483d504906e63a89e` | target (matches required pin) |
| `cases/max12_812_order2_exact_square_faber_affine_mu2_20260826/RESULT.md` | `86d9da43b1f7823a4673ed219478b1c6ff60503eccbb2892894733979468b19c` | named producer result; opened only because it is charged; its radical, `PASS` token, and endpoint string are not evidence |
| `cases/max12_812_order2_exact_square_faber_affine_mu2_20260826/EVIDENCE.sha256` | `8e56b7ab944e956b9d67993e54bfc8996f02b16803889ac7dfbaa59e2ee0447c` | named evidence list; every listed file rehashes; not used as a calculation |
| `cases/max12_812_order2_exact_square_faber_affine_mu2_20260826/FREEZE.sha256` | `a779cdeb5be36ad70c09b1497c3719b8c0659c03b48798414d90464156993970` | named freeze list; every listed file rehashes |
| `cases/max12_812_order2_exact_square_faber_affine_mu2_20260826/compile_faber_affine_mu2.py` | `1a4b7a9de049eaf82c3fb2682511ebcb441004a30af03abac241165717c34a12` | named compiler; the affine equation actually emitted is `I=R1,R2-mu2,R3,R4,R5,R6,R7` |
| `xmodel/max12-812-order2-exact-square-affine-mu2-dvr-rigidity-p3-design-20260826.md` | `fec7c140b8ceae57926895c88c4d43ed49753c17a2858f2824e49d872df8d276` | named navigation-only predecessor; its Laurent-valuative theorem is for `(0.1)`, not for `(1.6)` |

All six hashes match the values printed in the target. The
characteristic-65521 lane is a software control only and is not used.
V1 is parser-negative custody and has no mathematical status.

The algebraic input actually used is: the monic inverse of `w=Q^{1/4}`;
the branch `sqrt(Q)=z^2+O(1)`; the logarithmic-differentiation recurrence
for `(1+p t^2+c t^3+r t^4)^alpha`; the inverse-root convention that the
ordinary Faber tail is the coefficient of `w^{-ell}` in
`(H-[H]_+)(z(w))`; and the exact-square substitution
`f=(z^4+p z^2+c z+r)^2`.

---

## Strongest exact theorem that survives

Work over a field `K` of characteristic zero. Write

```text
Q = z^4 + p z^2 + c z + r,
Delta = p^2 - 4 r,
H = sqrt(Q) (Q^2 + beta Q + gamma),
```

in the formal branch `sqrt(Q)=z^2+O(1)` at infinity, and let `h_ell` be
the coefficient of `z^{-ell}` in `H`. Let `z(w)` be the monic inverse of
`w=Q^{1/4}`, and define ordinary Faber tails by

```text
sum_{ell>=1} R_ell w^{-ell} = (H-[H]_+)(z(w)).
```

Let `I` be the ideal

```text
I = (R1, R2-mu2, R3, R4, R5, R6, R7)
```

in `K[mu2, gamma, beta, r, c, p]`. After base change to an algebraic
closure, the reduced support of the affine Faber receiver `(1.6)` is
exactly

```text
V(c, mu2, Delta)
  union
V(c,
  15 Delta^2 - 64 beta Delta + 256 gamma,
  Delta^2 (5 Delta - 16 beta) - 2048 mu2).
```

Equivalently, writing `I_square` and `I_affine` for the two displayed
component ideals,

```text
rad(I) = I_square intersect I_affine.
```

Each of those two ideals is prime of dimension three. The second
component is the only reduced support not already present in the
seven-zero-tail square receiver. On `D(Delta)` it is a rational graph
over `(p, Delta, beta)`, so `p` remains free. Its zero-target section is
the Chebyshev family `16 beta=5 Delta`, `256 gamma=5 Delta^2`, `mu2=0`,
which is not a third minimal prime.

The polynomial identity

```text
c^5 + 128 R5 - 96 p R3 - (12 p^2 + 32 r) R1 = 0
```

holds in `K[p,c,r,beta,gamma]` before any equation of `(1.6)`. On the
affine graph, writing `D=Delta/4` and `s=5 D-4 beta`, the identities
`(5.2)`, `(5.3)`, `(5.4)`, and `R10=-D^4 (s+D)/512` are correct; none
is a row of `(1.6)`.

This is the exact seven-row affine ordinary-Faber receiver on the chart
`k10=1`. It does not classify `k10=0`, does not pull the identity back
through a literal total-Rees source or a target/deck tie, does not impose
correction jets, the terminal `[6,2]` passport, or either Taylor family,
does not construct or exclude a strict arc, and does not close order two,
`(8,12)`, maximum twelve, or JC2.

---

## Attack 1 — inverse series `z(w)` and connections `R1,...,R7`

**CONFIRMED.** These are the frozen ordinary Faber tails, not another
Laurent convention.

Write `z=w+epsilon` with

```text
epsilon = a w^{-1} + b w^{-2} + d w^{-3} + e w^{-4} + f w^{-5} + O(w^{-6})
```

and impose `Q(z)=w^4`. Collecting powers of `w` through `w^{-2}` gives
the triangular system

```text
w^2:  4 a + p = 0,
w^1:  4 b + c = 0,
w^0:  4 d + 6 a^2 + 2 p a + r = 0,
w^{-1}: 4 e + 12 a b + 2 p b + c a = 0,
w^{-2}: 4 f + 12 a d + 6 b^2 + 4 a^3 + 2 p d + p a^2 + c b = 0.
```

The unique solution is

```text
a = -p/4,
b = -c/4,
d = p^2/32 - r/4,
e = 0,
f = p^3/128 - p r/16 - c^2/32,
```

which is `(1.2)`, including the missing `w^{-4}` term. (The `w^{-1}`
coefficient vanishes identically after substituting `a` and `b`; it is
not an extra constraint.)

Now write `z=w(1+sigma)` with `sigma=a w^{-2}+b w^{-3}+d w^{-4}+e w^{-5}+f w^{-6}+O(w^{-7})`.
Then `z^{-ell}=w^{-ell}(1+sigma)^{-ell}`, and only `ell<=n` can contribute
to `[w^{-n}]`. Expanding through `w^{-7}` produces

```text
R1 = h1,
R2 = h2,
R3 = h3 + (p/4) h1,
R4 = h4 + (p/2) h2 + (c/4) h1,
R5 = h5 + (3 p/4) h3 + (c/2) h2 + (p^2/32 + r/4) h1,
R6 = h6 + p h4 + (3 c/4) h3 + (p^2/8 + r/2) h2 + (p c/8) h1,
R7 = h7 + (5 p/4) h5 + c h4
      + (9 p^2/32 + 3 r/4) h3 + (3 p c/8) h2
      + (-p^3/128 + 3 p r/16 + 3 c^2/32) h1.
```

Every displayed sign matches `(1.4)`. When `h1=0` this collapses to
`(1.5)`. The identities are polynomial and require only that the
displayed powers of two be invertible.

These are the ordinary Faber tails of the frozen source. The inverse of
`w^8=f(z)` on the exact square `f=Q^2` is the same germ as the inverse
of `w^4=Q(z)`. Algebraically `H(z(w))=w^{10}+beta w^6+gamma w^2` has no
negative powers, so

```text
[w^{-ell}](H-[H]_+)(z(w)) = -[w^{-ell}][H]_+(z(w)).
```

The frozen ordinary tail is exactly that coefficient (the minus sign in
the inverse-root reconstruction is this identity). The target Faber
polynomial `F_12` contributes `w^{12}` and does not affect rows one
through seven. The exact-square substitution used by the charged
compiler is the expansion of `Q^2`,

```text
(a0,...,a6) = (r^2, 2 c r, c^2+2 p r, 2 p c, p^2+2 r, 2 c, 2 p),
```

with loads `(k10,k6,k2)=(1,beta,gamma)`. Coefficient checks against the
emitted frozen polynomials confirm the same convention: the `gamma`
parts of `R1`, `R2`, and `R3` are `c/2`, `-p^2/8+r/2`, and `-p c/8`,
matching `(1.4)` applied to the independently reconstructed `h_ell`.
The unitriangular connection is therefore load-bearing whenever `h2` is
nonzero, and `(0.1)` is not the ordinary source face.

---

## Attack 2 — raw identity `c^5+128 R5-96 p R3-(12 p^2+32 r)R1=0`

**CONFIRMED.** The identity is raw. It excludes reduced support on
`D(c)`, and it saturates the raw ideal at `c`.

Substitute `(1.4)` into the left-hand side of `(3.2)`. The `h3` terms
cancel and one obtains the equivalent Laurent form

```text
128 R5 - 96 p R3 - (12 p^2 + 32 r) R1
  = 128 h5 + 64 c h2 - 32 p^2 h1.
```

Thus `(3.2)` is equivalent to `128 h5 + 64 c h2 - 32 p^2 h1 + c^5 = 0`,
still with no equation of `(1.6)` imposed. Logarithmic differentiation
of `g^alpha` with `g=1+p t^2+c t^3+r t^4` gives

```text
n a_n(alpha)
  = p (2(alpha+1)-n) a_{n-2}
  + c (3(alpha+1)-n) a_{n-3}
  + r (4(alpha+1)-n) a_{n-4},
```

and `h_ell=a_{10+ell}(5/2)+beta a_{6+ell}(3/2)+gamma a_{2+ell}(1/2)`.
The identity is affine-linear in `(beta,gamma)`, so it is enough to
check the three coefficient blocks.

The `gamma` block uses only `a3(1/2)=c/2`, `a4(1/2)=-p^2/8+r/2`, and
`a7(1/2)=c(3 p^2-4 r)/16`:

```text
128 a7(1/2) + 64 c a4(1/2) - 32 p^2 a3(1/2)
  = 8 c (3 p^2-4 r) + 64 c (-p^2/8 + r/2) - 16 p^2 c
  = 0.
```

The `beta` block uses `a7(3/2)=-3 c Delta/16`,
`a8(3/2)=3(Delta^2-8 p c^2)/128`, and the independently reconstructed

```text
a11(3/2) = (-15 p^4 c + 72 p^2 c r + 24 p c^3 - 48 c r^2)/256.
```

Every monomial in `128 a11(3/2)+64 c a8(3/2)-32 p^2 a7(3/2)` cancels.
The load-free block is the recurrence for `alpha=5/2`. The coefficients
needed through weight fifteen reconstruct to

```text
a11(5/2) = (15 p^4 c - 120 p^2 c r - 40 p c^3 + 240 c r^2)/256,
a12(5/2) = (-5 p^6 + 60 p^4 r + 120 p^3 c^2 - 240 p^2 r^2
            - 480 p c^2 r - 40 c^4 + 320 r^3)/1024,
a15(5/2) = (35 p^6 c - 300 p^4 c r - 200 p^3 c^3 + 720 p^2 c r^2
            + 480 p c^3 r + 24 c^5 - 320 c r^3)/2048.
```

Clearing the common denominator `2048` in
`4 a15 + 2 c a12 - p^2 a11 + c^5/32` produces seven monomials, each of
which sums to zero (`p^6 c`, `p^4 c r`, `p^3 c^3`, `p^2 c r^2`,
`p c^3 r`, `c^5`, `c r^3`). The identity is therefore polynomial in
`(p,c,r,beta,gamma)` and precedes every predecessor equation, radical,
localization, and geometric base change. Equivalently `(3.1)` holds, and
`c^5` lies in `(R1,R3,R5)`.

In a reduced algebra over a field, `c^5=0` forces `c=0`. Hence `(1.6)`
has no reduced point on `D(c)`. Scheme-theoretically, `c^5 in I` implies
that the saturation `I:c^infinity` is the unit ideal, so `V(I)` does not
meet `D(c)` even before taking radicals. Along the transverse slice
`p=r=beta=gamma=0` one has `R1=R3=0` and `R5=-c^5/128`, so the displayed
exponent five is exact on that chart and is not an accidental multiple
of a lower raw power.

The same conclusion is recovered from the first two odd Laurent rows
without using later Faber rows. On `D(c)`, `R1=h1=0` and `R3=h3=0`. The
combination `512 h3 + p*256 h1` eliminates `gamma` and equals
`4 c^3 (5 p^2-20 r-8 beta)`. Thus `beta=5 Delta/8`, and `h1=0` then
gives `(3.3)`. Substituting into `h2` produces `h2=-5 U/1024` with
`U=Delta^3+8 p Delta c^2+8 c^4`, and the raw identity (or the direct
composition `R5=h5+(c/2)h2`) yields `R5=-c^5/128`. No Groebner basis
is used.

---

## Attack 3 — `c=0`: `T^{-1}`, `T^{-3}`, `R2`, `R6`, and the square versus affine-Faber union

**CONFIRMED.** The factor in the affine-Faber generator is `2048 mu2`.
The parameter `p` is free. Chebyshev is a section, not a third component.

On `c=0` put `T=z^2+p/2` and `D=Delta/4`, so `Q=T^2-D`. Then `H` is odd
in `T`. Expanding `sqrt(T^2-D)=T(1-D/T^2)^{1/2}` through `T^{-3}` and
multiplying by `Q^2+beta Q+gamma=T^4+(beta-2 D)T^2+(D^2-beta D+gamma)`
gives exactly `(4.2)`:

```text
a = [T^{-1}] H = -(D/16) (5 D^2 - 6 beta D + 8 gamma),
b = [T^{-3}] H = -(D^2/128) (5 D^2 - 8 beta D + 16 gamma).
```

The inverse substitution `T(w)=sqrt(w^4+D)` is

```text
T^{-1} = w^{-2} - (D/2) w^{-6} + O(w^{-10}),
T^{-3} = w^{-6} + O(w^{-10}),
```

so through row seven

```text
R2 = a,
R6 = b - (D/2) a = (D^2/128) (15 D^2 - 16 beta D + 16 gamma).
```

Odd Faber rows vanish because `z(-w)=-z(w)` and `H` is even in `z`. The
`z`-expansion `T^{-1}=z^{-2}-(p/2)z^{-4}+O(z^{-6})` with `T^{-3}`
starting at `z^{-6}` yields the Laurent identity `h4=-(p/2)h2` on `c=0`.
Connection `(1.5)` therefore makes `R4` vanish identically; it does not
force `p mu2=0`. That is the precise failure of the Laurent four-pivot
block as an ordinary-source import.

If `D=0`, then `Q=T^2` is a square, `H` is polynomial, and `(2.2)`
follows with arbitrary `(beta,gamma)` and `mu2=0`. If `D!=0`, `R6=0`
solves as `gamma=beta D-15 D^2/16`. Substituting into `R2=mu2` produces
`mu2=D^2(5 D-4 beta)/32`. Clearing `D=Delta/4` is elementary:

```text
256 gamma = 64 beta Delta - 15 Delta^2,
2048 mu2 = Delta^2 (5 Delta - 16 beta),
```

which is exactly `(2.3)`. The coefficient `2048` is forced by
`16*32*4=2048` and is not the Laurent factor `32`. At the slice
`p=c=0` one has `D=-r` and `mu2=-r^2(5 r+4 beta)/32`; this is a
specialization of the same graph, not a separate component, and it is
not the Laurent affine equation `h6=0` (on `p=c=0` one has
`R6=h6+(r/2)h2`).

On `D(Delta)` the two-row Jacobian of `(R6, R2-mu2)` in `(beta,gamma)`
has determinant `D^4/64=Delta^4/16384`. Thus `(beta,gamma)` are exact
correction pivots, while `(p,D)` remain free. No correct Faber argument
sets `p=0`.

The Chebyshev ratios `16 beta=5 Delta` and `256 gamma=5 Delta^2` are
the section `s=0` of `(4.6)`, where `mu2=0`. They cut a dimension-two
sublocus of the affine-Faber component and are not a third minimal
prime of `I`.

---

## Attack 4 — primality, dimensions, and exact-Q evidence

**CONFIRMED** for the numbered claims. The exact-Q stdout and the
validator do **not**, by themselves, prove the radical equality. The
equality is nevertheless true.

Write the two displayed ideals in `K[mu2,gamma,beta,r,c,p]`:

```text
I_square = (c, mu2, Delta),
I_affine = (c,
            15 Delta^2 - 64 beta Delta + 256 gamma,
            Delta^2 (5 Delta - 16 beta) - 2048 mu2).
```

Each is a graph over a polynomial ring in characteristic zero, hence
prime of dimension three:

- `I_square`: `c=mu2=0` and `r=p^2/4`, quotient isomorphic to
  `K[gamma,beta,p]`;
- `I_affine`: `c=0`, `gamma=beta Delta/4-15 Delta^2/256`,
  `mu2=Delta^2(5 Delta-16 beta)/2048`, quotient isomorphic to
  `K[beta,r,p]`.

The units used are powers of two; all are invertible in characteristic
zero. The intersection is proper: on `I_square` the second generator of
`I_affine` reduces to `256 gamma`, so

```text
V(I_square) cap V(I_affine) = V(c, Delta, mu2, gamma),
```

a surface already contained in the union. The Chebyshev ideal
`(c, mu2, 16 beta-5 Delta, 256 gamma-5 Delta^2)` is the section `s=0`
of `I_affine` and is not a minimal prime of `I`.

Set-theoretically, Attacks 2--3 give `V(I)_red=V(I_square) union V(I_affine)`
after geometric base change. Each component lies in `V(I)` by
substitution (square because `Q` is a square and `H` is polynomial;
affine because `(4.5)--(4.6)` were derived from `R2=mu2` and `R6=0`
with the other five rows already zero on `c=0`). The intersection `J`
of the two primes is radical. Nullstellensatz over an algebraic closure
of characteristic zero therefore yields `rad(I)=J`. Both sides are
defined over `Q`, so the equality of radicals descends to `Q`. Raw
dimension three follows because both components have dimension three;
the nilpotent `c^5 in I` does not raise dimension. Embedded associated
primes of the nonreduced scheme `Spec(K[...]/I)` are not classified.

The charged exact-Q compiler asks Singular for the seven connection
identities, for `rad(I)`, for `J`, for both reductions, for
`sat(I,c)`, and for `minAssGTZ`. Those strings are not a proof. The
independent reconstruction of `(1.4)` in Attack 1, the raw identity in
Attack 2, and the classification in Attack 3 supersede them. Finite-field
agreement is a software control only. V1 is parser-negative custody: the
failure mode is ambiguous power/division syntax, and no algebraic
endpoint is consumed. The printed `minAss` generators of the second
prime are a different spanning set of `I_affine` (the first two
generators are `c` and `15 Delta^2-64 beta Delta+256 gamma`; the rest
are graph consequences) and are not used.

---

## Attack 5 — generalized Pell identity, discriminant, and `R10`

**CONFIRMED.** None of `(5.3)`, `(5.4)`, or `(5.5)` is a source row.

On `(4.5)--(4.6)` put `s=5 D-4 beta`, so `beta=(5 D-s)/4` and
`gamma=D(5 D-4 s)/16`. Substituting into `Q^2+beta Q+gamma` with
`Q=T^2-D` produces

```text
P(Q) = T^4 - ((s+3 D)/4) T^2 + D^2/16.
```

The polynomial part of `sqrt(Q) P(Q)`, extracted from the binomial
expansion of `(1-D/T^2)^{1/2}` through the `T` term, is

```text
A = T^5 - ((s+5 D)/4) T^3 + (D (2 s+5 D)/16) T.
```

Write `X=T^2`, `u=(s+3 D)/4`, `v=u+D/2`, `w=D(2 s+5 D)/16`, and
`k=D^2/16`. Then `A^2=X(X^2-v X+w)^2` and `Q P^2=(X-D)(X^2-u X+k)^2`.
The coefficients of `X^5`, `X^4`, and `X^3` cancel identically. The
remaining coefficients are

```text
X^2: -D^2 s/16,
X^1:  D^2 s (s+3 D)/64,
X^0:  D^5/256,
```

which is `(5.3)`. As a quadratic in `X`, the discriminant is

```text
D^4 s [ s (s+3 D)^2 + 4 D^3 ] / 4096
  = D^4 s (s+D)^2 (s+4 D) / 4096,
```

because `s(s+3 D)^2+4 D^3=(s+D)^2(s+4 D)`. That is `(5.4)`.

The next even Faber coefficient after row seven is `R10`. On the graph
one needs the `T^{-5}` coefficient of `H` and the `w^{-10}` terms of
`T^{-1}` and `T^{-3}`:

```text
[T^{-5}] H = -D^4 (D-5 s)/512,
T^{-1} = w^{-2} - (D/2) w^{-6} + (3 D^2/8) w^{-10} + O(w^{-14}),
T^{-3} = w^{-6} - (3 D/2) w^{-10} + O(w^{-14}).
```

With `a=D^2 s/32` and `b=D^3 s/64` (the latter from `R6=0`), the
combination `a(3 D^2/8)+b(-3 D/2)+[T^{-5}]H` simplifies to
`-D^4(s+D)/512`. This is `(5.5)`. It uses `T^{-5}`, which is outside
the seven source rows. The loci `s=0`, `s=-D`, and `s=-4 D` are
respectively the Chebyshev constant-remainder section, the next-tail
sentinel `R10=0`, and the remaining repeated-remainder factor of
`(5.4)`. They are compiler and terminal/Taylor controls, not additional
equations of `(1.6)`.

---

## Attack 6 — weighted-section and application boundary

**CONFIRMED** as a firewall, not as a total-Rees, correction, terminal,
or JC2 theorem.

Faber homogeneity `(6.1)` is the weight `12+ell` of the frozen tails
under `wt(a_i)=8-i`, `wt(k10)=2`, `wt(k6)=6`, `wt(k2)=10`. The
exact-square weighted section `Q_lambda(z)=lambda^4 Q(z/lambda)` scales
the coefficients of `f=Q^2` by `lambda^{8-i}` and pulls the divided
ordinary rows back to `(1.6)`, not to the Laurent face `(0.1)`. A
correct source replay must reconstruct the ordinary Faber tails and then
verify `(1.2)--(1.6)` coefficientwise. Reusing only the Laurent
recurrence is a negative control, as the note states.

Three distinctions remain load-bearing.

- Raw Laurent `h` is not Faber `R`. On `c=0` one has `R4=h4+(p/2)h2=0`
  identically, while the Laurent receiver `h4=0` together with `h2=mu2`
  forces `p mu2=0`. The corrected support is strictly larger: `p` is
  free on `(2.3)`.
- Normalized source support is not total-Rees accessibility. The ideal
  `I` is the seven-row ordinary-Faber face on the exact-square chart
  `k10=1`. Interior- and `J`-saturated total-Rees pullback, square-normal
  defects, connection jets, and all load and target jets are unimposed.
- A `J=0` exact section is not a generically nonzero-`J` strict arc.
  The charged one-parameter presentation identifies the seventh target
  with `J/4`, so the displayed section has `R7=J/4=0`. An accessible
  strict arc must produce nonzero generic `J` through a later
  correction, potentially after ramification. Identity `(3.2)` is a
  contact-raising certificate and a negative control for a transverse
  chart; it does not license replacing a forced correction by `c=0`.

The hyperplane `k10=0` is a different two-load problem and is not a
silently lost affine family. Terminal `[6,2]`, both Taylor families,
square-normal forcing, order two, `(8,12)`, maximum twelve, and JC2 are
absent from `(1.6)`. Horizontal rigidity on a reduced-domain arc
specializing to `(2.3)` on `D(Delta)` is the statement that `c` vanishes
identically while `(p,D)` may move; transverse total-source forcing can
invalidate the unforced equations and must be emitted before that
valuative statement is consumed. The note states this. No strict arc is
constructed or excluded.

---

## Scope firewall

This review confirms only the reduced support of the affine seven-row
ordinary-Faber receiver `R1=R3=R4=R5=R6=R7=0`, `R2=mu2`, for
`H=sqrt(Q)(Q^2+beta Q+gamma)` over a characteristic-zero field, in the
affine chart `k10=1`, together with the raw identity `(3.2)`, primeness
of the two displayed component ideals, the radical equality
`rad(I)=I_square cap I_affine`, the parametrization `(4.5)--(4.6)`, the
generalized-Pell remainder, and the identity `(5.5)`. It does not:

- classify the two-load chart `k10=0`;
- pull `(2.2)--(2.3)` through the literal total-Rees rows, the
  substitutions `Lambda^2 k10`, `Lambda^6 k6`, `Lambda^{10} k2`, or a
  chosen valuation ray;
- absorb correction jets, target/deck ties, square-normal forcing, the
  terminal `[6,2]` condition, or either Taylor family into `(1.6)`;
- promote `R10` or `(5.3)--(5.4)` to a source or terminal equation;
- construct or exclude a strict `Lambda!=0` arc, including any
  generically nonzero-`J` correction of the displayed `J=0` section;
- import the Laurent four-pivot block of the navigation-only design
  `fec7c140...` into the ordinary source;
- close order two, `(8,12)`, maximum twelve, or JC2.

The exact-Q Groebner narrative and the token `PASS_FABER_AFFINE_MU2_PROBE`
are not part of the confirmed argument. The prior Laurent calculation of
`(0.1)` is a different face and is not part of the confirmed statement.

CONFIRMED
