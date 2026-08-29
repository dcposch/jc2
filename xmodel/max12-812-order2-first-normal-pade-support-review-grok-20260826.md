# Hostile review — exact nonzero-load Padé lemma and complete first-normal support of the `(8,12)` order-two first normal gate

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-first-normal-pade-support-theorem-20260826.md` |
| Target SHA-256 | `2c917b9fe9af3c23d615a3f9061a5c981d26e5e69a75138aacb33f308619ecf5` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. Charged reviews were opened only because they are named; no producer status line and no charged `CONFIRMED`/`REPAIR` string is evidence |
| Method | source reading and hand derivation only; SHA-256 of the target and the four frozen inputs; no Singular, Sage, msolve, Lean, CAS, or substantive exact Python |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target is
`2c917b9fe9af3c23d615a3f9061a5c981d26e5e69a75138aacb33f308619ecf5`,
matching the required pin. Independently recomputed SHA-256 of the four
artifacts pinned in target §0 match those pins. Producer verdict language,
the target's own status line, charged review tokens, and two-prime modular
calculations were not used as evidence. No file other than this review was
written.

---

## Verdict

**CONFIRMED.**

Vanishing of the first seven negative `w`-coefficients is equivalent, by
the charged unitriangular change, to vanishing of the first seven negative
`z`-coefficients of `F`. The polynomial part `P=[F]_+^z` therefore satisfies
`F-P=O(z^{-8})`. Multiplication by the monic quartic `K` yields
`k10*K^{7/2}-A=O(z^{-4})` with `A` a polynomial, so the coefficients of
`z^{-1},z^{-2},z^{-3}` in `K^{7/2}` vanish whenever `k10!=0`. Those three
coefficients are exactly `[t^{15}],[t^{16}],[t^{17}]` of
`(1+p t^2+c t^3+r t^4)^{7/2}` in the formal branch with leading term
`z^{14}`. Direct multinomial expansion recovers both displays `(1.7)`--
`(1.9)` term by term, and the substitution `d=p^2-4r` recovers `A0,B0,C0`.
The combination `B0+p*A0=2 c^2(-5 d^2+8 p c^2)` and the subsequent
substitutions `p c^2=(5/8) d^2`, `c^4=(5/2) d^3` turn `C0` into `76 d^4`.
Characteristic zero kills both the case `c=0` (by `C0=d^4`) and the case
`c!=0` (by `76 d^4=0` then `(1.12)`). The resulting square root
`z^2+p/2` already lies in `L[z]`.

Raw reduced support is the union of the arbitrary-load square family, the
zero-load discriminant family, and the zero-normal three-space. On
`k10!=0` the Padé lemma forces the square locus, after which the seven
rows are equivalent to divisibility of `N` by the quadratic square root of
`K`. Multi-generator saturation deletes only the component supported on
`V(n0,n1,n2,n3,k10)` and restores the full affine closures of `Lsq` and
`D`. The residual `E` of the frozen V2 erratum is empty, so the previously
conditional recovery `V(I*)_red intersect V(k10)=S union D` is now
unconditional. The firewall does not claim a strict arc, higher-contact
exclusion, order-two exclusion, closure of `(8,12)`, maximum twelve, or
JC2.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order2-first-normal-pade-support-theorem-20260826.md` | `2c917b9fe9af3c23d615a3f9061a5c981d26e5e69a75138aacb33f308619ecf5` | target (matches required pin) |
| `xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-20260826.md` | `4c9d9cfc58eb4ca2a33c9bf83beb485c15f0796fa36d2ffe4826c3fdeeac374d` | charged principal-part identity, unitriangular change, `k10=0` UFD classification, saturation notation, residual `E`, conditional recovery |
| `xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-review-grok-20260826.md` | `08a5ca51461afb1753b21ee7fcf4bf8ed3719cb6edafb7d2020043ad63ab9efa` | named parent of the V2 erratum; opened only to obey the inspection clause; confirmed identities charged as algebraic input, not as proof of the new Padé expansion |
| `xmodel/max12-812-order2-first-normal-divisibility-jet-theorem-20260826.md` | `827e76bde5d394ab17f7c05561a1bf254b6fdf8fc3453dd60400d16e80061fdc` | exact first-normal chart and identification of the seven `q_ell` with the first-normal gate `Q1` |
| `xmodel/max12-812-order2-first-normal-divisibility-jet-review-grok-20260826.md` | `27275f3d13471521bec0016d4fbc6e12d5bf8e539deeb4694fe0c01f04b025bd` | named parent of the jet theorem; opened only to obey the inspection clause |

All five hashes match the values printed in the target and in the review
prompt. Two-prime modular calculations are not used. The charged algebraic
input is: the principal-part identity `(0.1)` with both signs positive;
unitriangularity of the first seven negative `z`-coefficients against the
first seven negative `w`-coefficients; the exact `k10=0` criterion
`q1=...=q7=0` iff `K|N^2`; the UFD classification of that divisibility
into the square family, the discriminant family covering `[2,1,1]` and
`[3,1]`, and the zero-normal section; survival of both named closures in
`V(I*) intersect V(k10)`; the location of the residual `E`; and the
geometry of sequential multi-generator saturation
`I*=((I:A^infinity):B^infinity)`.

---

## Strongest exact theorem that survives

Work over a field `L` of characteristic zero, in the first-normal chart of
the charged jet theorem, with the charged identities above. Write
`K=z^4+p z^2+c z+r`, `N=n3 z^3+n2 z^2+n1 z+n0`, and
`F=(3/8) N^2/K + k10 K^{5/2}` in the formal branch at infinity with
`K^{1/2}=z^2+O(1)`. Let `I=(q1,...,q7)`, `A=(p,c,r)`,
`B=(n0,n1,n2,n3,k10)`, and `I*=((I:A^infinity):B^infinity)`. Define the
closed sets

```text
Lsq:  c=0, p^2=4r, 2 n1=p n3, 2 n0=p n2, k10 arbitrary,
D:    K=(z-a)^2 (z^2+2 a z+e),
      N=lambda (z-a) (z^2+2 a z+e),
      k10=0,
Z:    N=0, k10=0, K arbitrary,
S:    Lsq intersect V(k10).
```

Then:

1. `k10!=0` and `q1=...=q7=0` imply `c=0` and `p^2=4r`. Equivalently
   `K=(z^2+p/2)^2` already in `L[z]`.
2. As reduced closed sets after base change to an algebraic closure,
   `V(I)_red = Lsq union D union Z`.
3. `V(I*)_red = Lsq union D`.
4. `V(I*)_red intersect V(k10) = S union D`. The residual `E` of the
   charged V2 erratum is empty.

This closes the nonzero-load Padé gap in the exact first-normal gate. It
does not lift either family through the next divided jet, construct a
strict `Lambda!=0` arc, impose the terminal `[6,2]` passport or either
Taylor boundary, control higher-contact jets, exclude order two, close
`(8,12)`, prove maximum twelve, or prove JC2.

---

## Attack 1 — Laurent order after `w` to `z`, `P`, multiplication by `K`, and the three coefficients of `K^{7/2}`

**CONFIRMED.** There is no off-by-one and no branch error.

Charged `(0.1)` extracts the negative `z`-part of `F` first and then
substitutes `z=z0(w)`. The charged unitriangular statement says that the
map from the first seven negative `z`-coefficients of `F` to
`(q1,...,q7)` is unitriangular, hence in particular does not involve
`z^{-8}` or lower. Vanishing of `q1=...=q7` is therefore equivalent to
vanishing of the coefficients of `z^{-1},...,z^{-7}` in `F`. Writing
`P=[F]_+^z` for the polynomial part at infinity, this is

```text
F - P = O(z^{-8}).
```

`K` is monic of degree four, so `K=z^4+O(z^2)` and

```text
K (F-P) = O(z^{-4}).
```

The remainder `O(z^{-8})` has highest power `z^{-8}`; times `z^4` this
becomes highest power `z^{-4}`. Terms of degree `>= -3` are therefore
absent, while a `z^{-4}` term is permitted. Substituting the charged
formula for `F` gives

```text
K F = (3/8) N^2 + k10 K^{7/2},
```

and the polynomial `A=K P-(3/8) N^2` of `(1.4)` rearranges this into
`(1.5)`:

```text
k10 K^{7/2} - A = O(z^{-4}).
```

`A` lies in `L[z]`, so it has no negative powers and cannot cancel
`z^{-1},z^{-2},z^{-3}`. Those three coefficients of `k10 K^{7/2}` must
vanish. Since `k10!=0` in `L`, the same three coefficients of `K^{7/2}`
vanish. This necessary condition depends only on `(p,c,r)`. The four
coefficients of `N` are absorbed into `A` and are not needed for the
contradiction off the square locus.

The formal branch is the unique series with leading term `z^2` for
`K^{1/2}`. Then `K^{7/2}=(K^{1/2})^7=z^{14}+O(z^{12})`, matching the
target's display. The opposite square-root branch would send
`K^{7/2}` to `-z^{14}+O(z^{12})` and be absorbed into the free sign of
`k10`; vanishing of negative coefficients is unchanged. The expansion is
at infinity, not at a finite root, so there is no Puiseux branching in
`t=z^{-1}`.

The change of series variable is

```text
K^{7/2} = z^{14} (1+p t^2+c t^3+r t^4)^{7/2},
```

and `z^{14} t^k = z^{14-k}`. The powers `z^{-1},z^{-2},z^{-3}` are
exactly `k=15,16,17`. The next coefficient `z^{-4}` corresponds to
`t^{18}` and is not constrained by `(1.5)`. Off-by-one alternatives that
fail: treating “first seven negative” as `z^{0}` through `z^{-6}` (would
give `O(z^{-7})` after subtracting `P`, then `O(z^{-3})` after multiplying
by `K`, forcing only two coefficients); treating `O(z^{-8})*z^4` as a
two-sided window `z^{3}` through `z^{-3}` (the left half is polynomial
and is absorbed by `A`); demanding that `t^{18}` vanish as well
(unjustified by the remainder `O(z^{-4})`). The target takes precisely
the three coefficients that `(1.5)` forces.

`P` is a polynomial over `L`. Indeed `N^2/K=O(z^2)` at infinity and
`K^{5/2}=z^{10}(1+O(t^2))^{5/2}` has coefficients in `L` by the binomial
series of `(1+u)^{5/2}` with rational coefficients, so the nonnegative
part of `F` lies in `L[z]`. Polynomiality of `A` follows.

---

## Attack 2 — independent expansion of `(1+p t^2+c t^3+r t^4)^{7/2}` at `t^{15},t^{16},t^{17}`

**CONFIRMED.** Both displays `(1.7)`--`(1.9)` and the substitution
`d=p^2-4r` hold term by term.

Write `u=p t^2+c t^3+r t^4` and expand `(1+u)^{7/2}` by the multinomial
form of the binomial series. The coefficient of `p^i c^j r^k t^{2i+3j+4k}`
is `P_n/(i! j! k!)` with `n=i+j+k` and falling product

```text
P_n = (7/2)(5/2)...(7/2-n+1).
```

The values used below are

```text
P_4 = 105/16,
P_5 = -105/32,
P_6 = 315/64,
P_7 = -1575/128,
P_8 = 11025/256.
```

Only `n<=8` can contribute to degree `<=17`, because `u^n` has minimal
degree `2n`.

### Coefficient of `t^{15}`

The lattice `2i+3j+4k=15` with `i,j,k>=0` has seven points. Each
contribution, reduced over a common denominator `2048`, is:

| `(i,j,k,n)` | term | `2048 *` term |
|---|---|---|
| `(6,1,0,7)` | `-35/2048 p^6 c` | `-35 p^6 c` |
| `(3,3,0,6)` | `35/256 p^3 c^3` | `280 p^3 c^3` |
| `(0,5,0,5)` | `-7/256 c^5` | `-56 c^5` |
| `(4,1,1,6)` | `105/512 p^4 c r` | `420 p^4 c r` |
| `(1,3,1,5)` | `-35/64 p c^3 r` | `-1120 p c^3 r` |
| `(2,1,2,5)` | `-105/128 p^2 c r^2` | `-1680 p^2 c r^2` |
| `(0,1,3,4)` | `35/32 c r^3` | `2240 c r^3` |

Sample reductions: `P_7/(6!)=(-1575/128)/720=-1575/92160=-35/2048`;
`P_5/5!=(-105/32)/120=-105/3840=-7/256`;
`P_4/3!=(105/16)/6=105/96=35/32`. Summing and factoring `7c` recovers
exactly the first block of `(1.9)`:

```text
2048 [t^{15}]
 = 7 c (320 r^3 - 8 c^4 - 160 p c^2 r - 240 p^2 r^2
        + 40 p^3 c^2 + 60 p^4 r - 5 p^6).
```

### Coefficient of `t^{16}`

The lattice `2i+3j+4k=16` has ten points (`j` even). Over denominator
`32768`:

| `(i,j,k,n)` | `32768 *` term |
|---|---|
| `(8,0,0,8)` | `35 p^8` |
| `(5,2,0,7)` | `-1680 p^5 c^2` |
| `(2,4,0,6)` | `3360 p^2 c^4` |
| `(6,0,1,7)` | `-560 p^6 r` |
| `(3,2,1,6)` | `13440 p^3 c^2 r` |
| `(0,4,1,5)` | `-4480 c^4 r` |
| `(4,0,2,6)` | `3360 p^4 r^2` |
| `(1,2,2,5)` | `-26880 p c^2 r^2` |
| `(2,0,3,5)` | `-8960 p^2 r^3` |
| `(0,0,4,4)` | `8960 r^4` |

The `(8,0,0)` term is the binomial coefficient `C(7/2,8)=35/32768`.
Factoring `35` recovers the second block of `(1.9)` exactly.

### Coefficient of `t^{17}`

The lattice `2i+3j+4k=17` has eight points (`j` odd). Over denominator
`4096`:

| `(i,j,k,n)` | `4096 *` term |
|---|---|
| `(7,1,0,8)` | `35 p^7 c` |
| `(4,3,0,7)` | `-350 p^4 c^3` |
| `(1,5,0,6)` | `168 p c^5` |
| `(5,1,1,7)` | `-420 p^5 c r` |
| `(2,3,1,6)` | `1680 p^2 c^3 r` |
| `(3,1,2,6)` | `1680 p^3 c r^2` |
| `(0,3,2,5)` | `-1120 c^3 r^2` |
| `(1,1,3,5)` | `-2240 p c r^3` |

The `(7,1,0)` term is `8*C(7/2,8) p^7 c=35/4096 p^7 c`. Factoring `7c`
recovers the third block of `(1.9)` exactly.

### Substitution `d=p^2-4r`

Expand `d^3=(p^2-4r)^3=p^6-12 p^4 r+48 p^2 r^2-64 r^3` and
`d^2=p^4-8 p^2 r+16 r^2`. Then

```text
-5 d^3 + 40 p c^2 d
 = -5 p^6 + 60 p^4 r - 240 p^2 r^2 + 320 r^3
   + 40 p^3 c^2 - 160 p c^2 r,
```

so `A0=-5 d^3+40 p c^2 d-8 c^4` reproduces the parenthesis of
`2048[t^{15}]` after the overall factor `7c`. Next

```text
5 p d^3 = 5 p^7 - 60 p^5 r + 240 p^3 r^2 - 320 p r^3,
d(d+4 p^2) = 5 p^4 - 24 p^2 r + 16 r^2,
-10 c^2 d(d+4 p^2) = -50 p^4 c^2 + 240 p^2 c^2 r - 160 c^2 r^2,
```

so `B0=5 p d^3-10 c^2 d(d+4 p^2)+24 p c^4` reproduces the parenthesis of
`4096[t^{17}]`. Finally

```text
d^4 = p^8 - 16 p^6 r + 96 p^4 r^2 - 256 p^2 r^3 + 256 r^4,
-48 p c^2 d^2 = -48 p^5 c^2 + 384 p^3 c^2 r - 768 p c^2 r^2,
32 c^4 (d+2 p^2) = 96 p^2 c^4 - 128 c^4 r,
```

so `C0=d^4-48 p c^2 d^2+32 c^4(d+2 p^2)` reproduces the parenthesis of
`32768[t^{16}]`. Combined with the overall factors `7c/2048`,
`35/32768`, and `7c/4096`, this is `(1.7)`--`(1.8)`. No factorization
oracle is used: `(1.8)` is a rewriting of `(1.9)`.

---

## Attack 3 — identities `(1.10)`--`(1.13)`, the coefficient `76`, and both cases `c=0`, `c!=0`

**CONFIRMED.** Characteristic zero is essential and is used honestly.

Equation `(1.5)` forces all three expressions in `(1.7)` to vanish. The
prefactors `7/2048`, `35/32768`, and `7/4096` are nonzero in
characteristic zero, so `c A0=C0=c B0=0`.

**Case `c=0`.** Then `C0=d^4`. Characteristic zero gives `d=0`, which is
`p^2=4r`. This is `(1.1)`. (The same conclusion follows from
`A0=-5 d^3=0` in every characteristic other than `5`; using `C0=d^4`
avoids that restriction.)

**Case `c!=0`.** Then `A0=B0=0`. Direct expansion, with no substitution
yet:

```text
B0 + p A0
 = 5 p d^3 - 10 c^2 d(d+4 p^2) + 24 p c^4
   + p (-5 d^3 + 40 p c^2 d - 8 c^4)
 = (5 p d^3 - 5 p d^3)
   + (-40 p^2 c^2 d + 40 p^2 c^2 d)
   - 10 c^2 d^2 + 16 p c^4
 = 2 c^2 (-5 d^2 + 8 p c^2).
```

This is `(1.10)`. Since `c!=0` one has `2 c^2!=0`, so
`-5 d^2+8 p c^2=0`, which is `(1.11)`:

```text
p c^2 = (5/8) d^2.
```

Substitute into `A0=0`:

```text
40 p c^2 d = 40*(5/8) d^3 = 25 d^3,
A0 = -5 d^3 + 25 d^3 - 8 c^4 = 20 d^3 - 8 c^4.
```

Thus `8 c^4=20 d^3`, i.e. `c^4=(5/2) d^3`, which is `(1.12)`. The pair
`(1.11)`--`(1.12)` does not yet force `d=0`: over an algebraic closure
one may still take `d!=0` with `c^4=(5/2) d^3` and
`p=(5/8) d^2/c^2`. The third equation is required.

Now `C0`. Using `(1.11)` on the middle term,

```text
-48 p c^2 d^2 = -48*(5/8) d^4 = -30 d^4.
```

Using `(1.12)` and `(1.11)` on the remaining terms,

```text
32 c^4 d = 32*(5/2) d^4 = 80 d^4,
64 (p c^2)^2 = 64*(5/8 d^2)^2 = 64*(25/64) d^4 = 25 d^4.
```

The last identity is the rewriting `32 c^4*(2 p^2)=64 p^2 c^4=64(p c^2)^2`
already displayed in `(1.13)`. Therefore

```text
C0 = d^4 - 30 d^4 + 80 d^4 + 25 d^4
   = (1 - 30 + 80 + 25) d^4
   = 76 d^4.
```

The coefficient `76=4*19` is nonzero in characteristic zero, so `C0=0`
gives `d=0`. Then `(1.12)` gives `c^4=0`, hence `c=0`, contrary to the
case hypothesis. The case `c!=0` is empty.

Both cases together are `(1.1)`. In characteristic `19` the identity
`C0=76 d^4` would become `0=0` on the locus of `(1.11)`--`(1.12)` and a
nonzero-`c` family could survive; the restriction to characteristic zero
is therefore sharp for this argument and is stated at the start of §1.

---

## Attack 4 — square already over `L`, including the factor `p/2`

**CONFIRMED.** The square root lies in `L[z]`, not merely after algebraic
closure.

From `(1.1)`, `c=0` and `r=p^2/4`. Characteristic zero supplies
`2^{-1} in L` (every such field contains `Q`), so `p/2 in L` and

```text
K = z^4 + p z^2 + p^2/4 = (z^2 + p/2)^2
```

is an identity in `L[z]`. This is `(1.2)`.

Geometrically the same equations cut out the square locus. A monic
depressed quartic is a square in an algebraic closure if and only if it
is `(z^2+a z+b)^2` with `2a=0`, hence `a=0` in characteristic not `2`,
hence `c=2 a b=0` and `p=2b`, `r=b^2`. Thus `b=p/2` again lies in `L`.
For this specific shape, “square over `L`” and “geometrically square”
coincide; the target's stronger wording is nevertheless correct and is
the statement used later to write the affine equations `(2.3)` over `L`
without a quadratic extension.

---

## Attack 5 — raw-support equality `(2.2)`

**CONFIRMED.** No nonsquare `k10!=0` family, no zero-normal family with
`k10!=0` off the square locus, and no multiple-root family with
`k10!=0` is omitted. On the arbitrary-`k10` square locus the seven rows
force the displayed divisibility of `N`.

Work after base change to an algebraic closure, as the target does. On
`k10=0` the charged UFD criterion says `q1=...=q7=0` if and only if
`K|N^2`, if and only if `D_K|N` with `D_K=prod (z-a)^{ceil(m_a/2)}`.
With `deg K=4` and `deg N<=3` the odd-multiplicity kernel has degree
`0`, `2`, or `4`:

- degree `0` is the square family `S=Lsq intersect V(k10)`, including
  its zero-normal locus `alpha=beta=0`;
- degree `2` is the discriminant family `D`, including its zero-normal
  locus `lambda=0`, covering partitions `[2,1,1]` and `[3,1]` (for
  `[3,1]` one has `e=-3 a^2` and `D_K` of degree three, matching the
  displayed parameterization of `N`);
- degree `4` is squarefree `K` with `N=0`, the squarefree open of `Z`.

Every depressed quartic with a multiple root is of the form
`(z-a)^2(z^2+2 a z+e)` because the roots sum to zero. Thus on `k10=0`,

```text
V(I) intersect V(k10) = S union D union Z
```

as reduced sets, allowing the overlaps `Z intersect S` and `Z intersect D`.

On `k10!=0`, Attack 3 forces `K` to be square, i.e. `c=0` and `p^2=4r`.
Then `K^{5/2}=(z^2+s)^5` is a polynomial, so the load term does not
contribute to `[F]_-`. Polynomial division gives `N^2=Q K+R` with
`deg R<4` and `Q` of degree at most two, hence `N^2/K=Q+R/K` with
`R/K=O(z^{-1})` down to `O(z^{-4})`. Vanishing of the first seven
negative coefficients therefore vanishes all negative coefficients of
`N^2/K` and is equivalent to `R=0`, i.e. `K|N^2`. In a UFD this is
equivalent to the quadratic square root `z^2+s` dividing `N`, which is
precisely the parameterization of `Lsq`. Equivalently in affine
coordinates, `N=(z^2+s)(alpha z+beta)` expands to the two linear
relations `2 n1=p n3` and `2 n0=p n2` of `(2.3)`, using `p=2s`. Those
four equations are closed of expected dimension four on the eight-space
`(p,c,r,n0,n1,n2,n3,k10)`, matching parameters `(s,alpha,beta,k10)`. No
closure is hidden in `(2.2)`.

Conversely, each family of `(2.1)` lies in `V(I)`:

- on `Lsq`, both `N^2/K=(alpha z+beta)^2` and `K^{5/2}=(z^2+s)^5` are
  polynomials, so `F` is a polynomial and every negative coefficient
  vanishes, for arbitrary `k10` (charged);
- on `D`, `k10=0` and `K|N^2`, so the charged `k10=0` criterion applies;
- on `Z`, `N=0` and `k10=0`, so `F=0`.

Omitted-family check:

1. Nonsquare `K` with `k10!=0`. Forbidden by `(1.1)`.
2. Zero-normal with `k10!=0`. Then `F=k10 K^{5/2}`. The same multiplication
   by `K` still produces `(1.5)`, so `K` is square, and then `K^{5/2}` is
   a polynomial. This is `Lsq` at `alpha=beta=0`, not a missing family.
3. Multiple-root nonsquare `K` with `k10!=0` (the `[2,1,1]` or `[3,1]`
   shapes with nonzero load). Again `(1.1)` forces a square, so these
   points are absent from `V(I)`.
4. Square `K` with `k10` arbitrary but `z^2+s` not dividing `N`. Then
   `K` does not divide `N^2`, so the negative part of `N^2/K` is nonzero
   and the seven rows fail. Correctly excluded from `Lsq`.

The union `(2.2)` is therefore exact as a reduced-support statement.

---

## Attack 6 — saturation equality `(3.2)`

**CONFIRMED.** Sequential multi-generator saturation deletes exactly `Z`
as a component and restores the complete affine closures of `Lsq` and
`D`.

Charged saturation geometry:

```text
V((I:A^infinity):B^infinity)_red
  = cl( V(I) \ (V(A) union V(B)) ).
```

`V(A)` is the origin in `(p,c,r)`, not the union of the three coordinate
hyperplanes. `V(B)` is the simultaneous zero section `N=0` and `k10=0`.
Saturation by the product `(p c r)^infinity` is a different operation and
would delete `Lsq` entire, because `c=0` on `Lsq`; the target uses the
multi-generator ideal, consistently with `D(A)` meaning the complement of
the origin. For reduced support the order `A` then `B` is immaterial.

From `(2.2)`, `Z subset V(B)`, so

```text
V(I) \ (V(A) union V(B))
  = (Lsq union D) intersect D(A) intersect D(B).
```

Density on `Lsq`. In parameters `(s,alpha,beta,k10)` one has an
isomorphism with `A^4`. The locus `V(A) intersect Lsq` is the hyperplane
`s=0`; the locus `V(B) intersect Lsq` is the line `alpha=beta=k10=0`.
The complement `s!=0` and `(alpha,beta,k10)!=(0,0,0)` is a nonempty
Zariski-open of an irreducible affine four-space, hence dense. Its
closure is all of `Lsq`, including the face `s=0` and the zero-normal
line at `k10=0`.

Density on `D`. Expanding the parameterization gives

```text
p = e-3 a^2,   c = 2 a (a^2-e),   r = a^2 e.
```

If `a=0` then `p=e` and `r=0`, so `V(A)` forces `e=0`. If `a!=0` then
`r=0` forces `e=0`, after which `p=-3 a^2!=0`. Thus `V(A) intersect D`
is the single parameter point `(a,e)=(0,0)`, for arbitrary `lambda`.
Also `N=0` if and only if `lambda=0`, because `(z-a)(z^2+2 a z+e)` is
monic of degree three. The complement `lambda!=0` and `(a,e)!=(0,0)` is
a nonempty open of the irreducible image, hence dense. Its closure is
all of `D`, including the zero-normal plane `lambda=0` and the origin
`(a,e)=(0,0)`.

Therefore `cl(V(I)\(V(A) union V(B)))=Lsq union D`, which is `(3.2)`.
The component `Z` is supported wholly on `V(B)` and is deleted as a
component. Its intersections with `Lsq` and with `D` are restored as
boundary points of retained components, not as a residual piece of `Z`.
No other reduced component exists: `(2.2)` names them all, and neither
`Lsq` nor `D` is contained in `V(A)` or in `V(B)`.

The identity is reduced support, not equality of nonreduced ideals, not
absence of embedded primes along `Lsq` or `D`, and not reducedness of
`I*`. The target does not claim those.

---

## Attack 7 — identity `(3.3)` is the previously conditional recovery; firewall does not overclaim

**CONFIRMED.**

The charged V2 erratum records a residual

```text
E := (V(I*) intersect V(k10)) \ (S union D)
     subset V(k10,n0,n1,n2,n3) intersect {K nonsquare},
```

and states that the withdrawn V1 equality
`V(I*)_red intersect V(k10)=S union D` follows if one proves

```text
k10!=0 and q1=...=q7=0  =>  K is square.
```

That implication is the target's `(1.1)`, proved in characteristic zero
by Attacks 1--3. Every irreducible component of `V(I)_red` whose generic
point has `k10!=0` is then contained in the closed square locus `{c=0,
p^2=4r}`, whose special fibre at `k10=0` cannot meet the squarefree
locus. Combined with Attack 6 this empties `E` as a set of geometric
points, and with the charged survival `S union D subset V(I*) intersect
V(k10)` yields `(3.3)`. Here `S=Lsq intersect V(k10)` is exactly the
square family of the frozen erratum. This is the previously conditional
recovery, now unconditional. An embedded or nonreduced primary supported
on the squarefree zero-normal section has radical containing `B` and is
deleted by the colon; reduced support of saturation cannot acquire a new
closed point from nilpotents.

Section 4 of the target states that the nonzero-load Padé gap in the
exact first-normal gate is closed, and that the complete reduced support
of that gate (the saturated object `I*=Q1*` of the charged jet theorem)
consists of the arbitrary-load square family and the zero-load
discriminant family. It then refuses, in a single paragraph: lifting
either family through the next divided jet; realizing a strict
`Lambda!=0` arc; the terminal `[6,2]` passport and the two Taylor
boundaries; control of arcs whose first normal/load contact occurs after
order one; exclusion of order two; closure of `(8,12)`; maximum twelve;
JC2. No numbered identity claims any of those. The unsaturated fibre
still contains `Z`; the target's “complete reduced support of that gate”
refers to the saturated gate `I*`, which is the object the jet theorem
named as the first nonzero-normal-direction gate.

---

## Attacks that failed to break a numbered claim

Reading `O(z^{-8})*K` as forcing four vanishing negative coefficients
rather than three (`z^{-4}` is permitted by the remainder). Reading
“first seven negative” as `z^{0}` through `z^{-6}`. Using the opposite
square-root branch and expecting a sign change in `(1.7)` (absorbed by
`k10`). Treating `(1.11)`--`(1.12)` as already a contradiction without
`C0` (they cut out a one-parameter family off `d=0`, which `76 d^4`
kills). Claiming the factor `76` is a transcription of `-30+48` or
similar (the actual arithmetic is `1-30+80+25`). Claiming `K` is only
geometrically square because `p/2` might leave `L` (characteristic zero
forces `2^{-1} in L`). Saturating by the product `p c r` and deleting
`Lsq` (the target saturates by the ideal `(p,c,r)`). Claiming `Z`
survives in `V(I*)_red` because `Z intersect Lsq` is nonempty (that
intersection is a boundary of a retained component). Claiming a
multiple-root `k10!=0` family is missing from `(2.2)` (Padé forbids it).
Claiming zero-normal `k10!=0` is missing (it is `Lsq` at
`alpha=beta=0`). Claiming `(3.3)` still depends on a modular calculation
(the only input is `(1.1)` plus charged saturation geometry). Importing
a strict arc, a higher-contact emptiness statement, order-two exclusion,
closure of `(8,12)`, maximum twelve, or JC2 (none is used).

---

## Scope that remains open

Whether either family of `(3.2)` lifts through the next divided jet
`Theta_ell mod Lambda^2`. Whether a strict `Lambda!=0` arc exists on
either family. The characteristic-zero radical of `I*`, its reducedness,
and embedded primes along `Lsq` or `D`. Higher-contact jets, including
the zero normal section. The terminal `[6,2]` passport. Either Taylor
family. Emptiness or nonemptiness of a strict arc. Closure of order two,
of `(8,12)`, of maximum twelve, or of JC2.

CONFIRMED
