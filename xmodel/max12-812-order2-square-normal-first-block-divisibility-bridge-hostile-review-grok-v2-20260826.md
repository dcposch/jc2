# Hostile review V2 — square-normal first-block divisibility bridge

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-square-normal-first-block-divisibility-bridge-theorem-20260826.md` |
| Target SHA-256 | `56123a6f2b110284871fe65d664ffed89cb5004d1498e59a81719c2278c59f23` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. The target status line, campaign titles, and any producer `PASS` token are not evidence |
| Method | source reading; SHA-256 of the charged bytes; independent Euclidean division of a general cubic square by a depressed monic quartic; reciprocal series of `1/Q` at infinity over `Q`; multivariate polynomial identities for `(1.1)` and `(4.1)`; UFD valuations in `k[z]`; binomial expansion of `(1+X)^{3/2}`; inspection of the ordinary inverse-root Faber connection. No Singular, Sage, msolve, or Lean |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target is
`56123a6f2b110284871fe65d664ffed89cb5004d1498e59a81719c2278c59f23`,
matching the required V2 pin. V1 was cancelled with no report after an
imprecise unused `z^{-4}` term in the displayed reciprocal; this review
attacks only the V2 bytes. Producer verdict language and the target's own
status line were not used as evidence. No file other than this review was
written. The theorem, producer cases, shared ledgers, and `jc2-lean` were
not edited.

The elementary algebra is polynomial division in `k[z]`, unique
factorization, an incidence-chart discriminant, and one binomial
coefficient in characteristic zero. Filenames and section titles that
say order two, square-normal, `(8,12)`, or maximum twelve are campaign
scope labels, not theorems.

---

## Verdict

**CONFIRMED.**

Write `Q=z^4+q2 z^2+q1 z+q0` and `N=n3 z^3+n2 z^2+n1 z+n0`, and divide
`N^2=A Q+R` with `deg R<=3`. The expansion `N^2/Q=A+sum_{j>=1} h_j z^{-j}`
satisfies the triangular identities

```text
h1=r3,
h2=r2,
h3=r1-q2*r3,
h4=r0-q2*r2-q1*r3,                                  (1.1)
```

with diagonal one. Consequently `h1=h2=h3=h4=0` if and only if `R=0` if
and only if `Q|N^2` if and only if `h1=...=h7=0`. Four rows are sharp:
the realizable remainder `R=1` (take `N=1`) gives `h1=h2=h3=0` and
`h4=1`. The V2 reciprocal

```text
1/Q=z^{-4}(1-q2 z^{-2}-q1 z^{-3}+O(z^{-4}))
```

is exact for this block: the `z^{-4}` coefficient of `1/(1+q2 z^{-2}+...)`
feeds only `h_j` with `j>=5`.

Over the UFD `k[z]`, `Q|N^2` if and only if `Q_half|N` with
`Q_half=prod_f f^{ceil(e_f/2)}`. On the coprime squarefree type
`Q=A^2 D` with `deg A=1`, `deg D=2`, the half-divisor has degree three,
so `N=M A D` for a unique scalar `M`. Squarefreeness of `D` is essential
and the displayed `D=B^2` control is a genuine counterexample. The
conditions `E!=0` and `(4a)^2-4E!=0` on the depressed incidence
`D=A^2+4a A+E` are exactly coprimeness of `A` with `D` and squarefreeness
of `D`. Expanding `(4.1)` recovers the central specialization
`U=V=R0=W0=0` of the delayed-`A` coefficient chart; the root coordinate
`a` is not promoted to a global regular function of quartic coefficients.

In characteristic zero the unloaded quadratic term of
`(Q^2+epsilon^d N)^{3/2}` is `(3/8) epsilon^{2d} N^2/Q`, and `3/8` is a
unit, so vanishing of a complete initial ordinary block is equivalent to
`Q|N^2` precisely when the Laurent-to-ordinary connection is lower
unitriangular of diagonal one and no load, target, or lower correction
occupies the same grade. At a tied grade the lemma classifies only that
unloaded summand.

This is a first-block divisibility and routing bridge. It does not prove
higher-jet absorption, a Rees kernel or torsion statement, a literal
source/affine-Faber overlap, total fan coverage, order two, `(8,12)`,
maximum twelve, or JC2.

**CONFIRMED**

---

## Attack 1 — hash and algebra versus campaign language

Recomputed SHA-256 of the charged file is the V2 pin
`56123a6f2b110284871fe65d664ffed89cb5004d1498e59a81719c2278c59f23`.
The file is presently untracked in git; `HEAD` at review time is
`418e413593120d19e15e6546eb50c985f4b1f038`.

Algebra actually proved:

- the four-coefficient identities `(1.1)` and the equivalences `(1.2)`
  over an arbitrary field;
- the UFD criterion `(3.1)` in `k[z]`, with the degree-three conclusion
  `(3.2)` under the written factor-type hypotheses;
- the incidence open `E!=0`, `(4a)^2-4E!=0` in §4;
- the characteristic-zero binomial `(5.1)` and the unloaded vanishing
  criterion at an untied grade.

Campaign language, not algebra: the title words “order-two”,
“square-normal”, “first-block”; the routing names
“collision/Pell/`p=0`/`D=0` receiver”; the citation of a “promoted
delayed-`A` theorem”; every firewall clause that refuses total-Rees,
total-fan, order two, maximum twelve, or JC2. Those refusals are
enforced below rather than treated as extra theorems.

Notation collision, non-failing: §1 uses `A` for the Euclidean quotient
`N^2=A Q+R`; §§3–4 reuse `A` for the monic linear factor `z-a`. The two
uses never appear in the same displayed identity.

---

## Attack 2 — independent division and the triangular formulas

Let `t=z^{-1}` and write `Q=z^4(1+q2 t^2+q1 t^3+q0 t^4)`. The geometric
series for the depressed reciprocal is

```text
(1+q2 t^2+q1 t^3+q0 t^4)^{-1}
  = 1 - q2 t^2 - q1 t^3 + O(t^4),
```

because `q3=0` kills the `t^1` term and the square of `q2 t^2+...` begins
at `t^4`. Thus

```text
1/Q = t^4 - q2 t^6 - q1 t^7 + O(t^8).
```

(The coefficient of `t^5` in `1/Q` vanishes; the coefficient of `t^8` is
`q2^2-q0` and is not needed.) Multiplying by `R=r3 z^3+r2 z^2+r1 z+r0`
gives the negative powers

```text
z^{-1}: r3,
z^{-2}: r2,
z^{-3}: r1 - q2 r3,
z^{-4}: r0 - q2 r2 - q1 r3.
```

No other monomial from `1/Q` reaches `z^{-4}`: `r3 z^3` against the
`t^4` coefficient of the unit factor produces `z^{-5}`, and there is no
`z^{-5}` term in `1/Q` to pair with `r1 z`. This is the source of the
four signs in `(1.1)`. In matrix form, ordering
`(r3,r2,r1,r0)` to `(h1,h2,h3,h4)`,

```text
[ 1    0    0    0 ]
[ 0    1    0    0 ]
[-q2   0    1    0 ]
[-q1  -q2   0    1 ].
```

The matrix is triangular with diagonal one over `Z[q2,q1]`, hence over
every field. Inverse:

```text
r3=h1,   r2=h2,   r1=h3+q2 h1,   r0=h4+q2 h2+q1 h1.
```

The same identities were recomputed in two independent ways: as
multivariate polynomial equalities in
`(q2,q1,q0,r3,r2,r1,r0)`, and by Euclidean division of a general cubic
square `N^2` followed by multiplication by the reciprocal series of `Q`.
A generic numeric cross-check, `N=2z^3+3z^2+5z+7` and
`Q=z^4+11 z^2+13 z+17`, gives quotient `4z^2+12z-15` and remainder
`-126 z^3+8 z^2+61 z+304`, and the series of `N^2/Q` at infinity
reproduces both the quotient as the polynomial part and the four `h_j`
from `(1.1)`. The coefficient `q0` does not appear in `h1,...,h4`.

V2's `O(z^{-4})` remainder is the correct truncation for this block.
An explicit unused `z^{-4}` term in the unit factor would not have
changed `(1.1)`, which is why V1's imprecision was unused; it is no
longer present.

---

## Attack 3 — four negative coefficients, necessity, sufficiency, sharpness

Sufficiency. Vanishing of `h1,...,h4` forces `R=0` by the inverse just
displayed, hence `Q|N^2` in `k[z]`. If `R=0`, then `N^2/Q` is a
polynomial, so every negative coefficient vanishes, and in particular
`h1=...=h7=0`. This is `(1.2)`.

Necessity of four, as a linear statement on remainders. The first three
rows determine only `(r3,r2,r1)`. They leave `r0` free. The remainder
`R=1` is realized by the cubic `N=1` (degree at most three is allowed)
for every monic quartic `Q`: `N^2=1`, the Euclidean remainder is `1`,
and `(1.1)` returns `h1=h2=h3=0`, `h4=1`. Three vanishing coefficients
therefore do not force `Q|N^2`, even after restricting to actual squares
of cubics. Four rows are sharp, uniformly in `Q`.

The same remainder also shows that “any four of the first seven” is the
wrong count: for `R=1` and `Q=z^4+3z^2+5z+7` one has
`h5=0` while `h4=1` and `h6=-3`. Only a complete initial block of
length four is equivalent to `R=0`.

---

## Attack 4 — UFD criterion and the degree-three conclusion

Let `k` be any field. Then `k[z]` is a UFD. For each irreducible `f`,

```text
v_f(Q)=e_f <= 2 v_f(N)    iff    v_f(N) >= ceil(e_f/2).
```

This is `(3.1)`: `Q|N^2` iff `Q_half|N`. No algebraic closure is used.
Squarefree means not divisible by a square in `k[z]`, which is the UFD
sense required here.

Degree counting on a monic quartic `Q` and a cubic `N`:

1. If `Q` is squarefree then `Q_half=Q` has degree four, so `Q_half|N`
   forces `N=0`. Control: `Q=z^4-1`, `N=z^3` has remainder `z^2` and
   `h2=1`.

2. If `Q=A^2 D` with `deg A=1`, `deg D=2`, `gcd(A,D)=1`, and `D`
   squarefree, then `e_A=2` and every irreducible factor of `D` has
   exponent one, so `Q_half=A D` has degree three. A degree-three monic
   divisor of a degree-at-most-three polynomial is a scalar multiple,
   uniquely `N=M A D`. This is `(3.2)`.

3. More degenerate types have strictly smaller `deg Q_half` or a
   different generator:
   - two double factors, `Q=A^2 B^2`: `Q_half=A B` of degree two;
   - quadruple factor, `Q=A^4`: `Q_half=A^2` of degree two;
   - triple plus simple, `Q=A^3 B`: `Q_half=A^2 B` of degree three, but
     the generator is `A^2 B` rather than a coprime `A D`.

Squarefreeness of `D` is essential for `(3.2)`. If `D=B^2` then
`Q=A^2 B^2` and `Q|N^2` requires only `A B|N`, not `A D|N`. Explicit
depressed control: `A=z-a`, `B=z+a`, `Q=(z^2-a^2)^2`, `N=z^2-a^2`
satisfies `Q|N^2` identically, while `A D=A B^2=(z-a)(z+a)^2` does not
divide `N`. This is the displayed degenerate countercontrol, and it is
the locus `E=4a^2` of §4.

The companion sentence that `gcd(A,D)=1` is likewise “essential” is
stronger than the algebra of `(3.2)` requires. If `D` is squarefree of
degree two and `A` divides `D`, then `D=A B` with `B!=A`, `Q=A^3 B`, and
`Q_half=A^2 B=A D`, so `N=M A D` remains the correct kernel. The gcd
hypothesis is used to isolate the coprime type that §4 charts, and §3
already routes `[3,1]` separately; it is not a missing hypothesis that
breaks the numbered implication `(3.2)`, and the only displayed
counterexample is the squarefree failure `D=B^2`.

---

## Attack 5 — repeated-`A` incidence chart

On the depressed repeated-root incidence put `A=z-a` and
`D=A^2+4a A+E`. Expanding in `z`,

```text
D = z^2 + 2a z + (E-3a^2),
Q = A^2 D
  = z^4 + (E-6a^2) z^2 + 2a(4a^2-E) z + a^2(E-3a^2),
N = M A D
  = M( z^3 + a z^2 + (E-5a^2) z - a(E-3a^2) ).
```

The `z^3` coefficient of `Q` vanishes, so the chart is depressed. The
value `D(a)=E`, so `A` divides `D` if and only if `E=0`. The discriminant
of `D` as a quadratic in `z` is

```text
(2a)^2 - 4(E-3a^2) = 16a^2 - 4E = (4a)^2 - 4E.
```

Thus `E!=0` and `(4a)^2-4E!=0` are exactly coprimeness of `A` with `D`
and squarefreeness of `D`. In characteristic two the second polynomial
is identically zero, so the open is empty and the implication is
vacuous; the theorem does not claim the open is nonempty in every
characteristic. In characteristic not two the two equations cut out:

- `E=0`, `a!=0`: triple plus simple, `Q=(z-a)^3(z+3a)`;
- `E=4a^2`, `a!=0`: two double roots, `Q=(z^2-a^2)^2`;
- both zero: quadruple root `Q=z^4`.

On the complementary open, `(3.2)` identifies the kernel as the line
`N=M A D`. That is the nonzero first square-normal kernel of this
factor type (the zero section is `M=0`).

The same expansion is the central specialization `U=V=R0=W0=0` of the
delayed-`A` coefficient isomorphism on `D(M)`:

```text
qp=E-6a^2,     qc=2a(4a^2-E),     qr=a^2(E-3a^2),
n3=M,          n2=a M,            n1=(E-5a^2)M,
n0=-a(E-3a^2)M.
```

These were expanded independently from `(4.1)` and match. The coordinate
`a` here is the distinguished double root on the incidence chart. It is
not a globally regular function of `(q2,q1,q0)`: the double-root locus
is `Res(Q,Q')=0`, and extracting the root is a branched cover. On
`D(n3)` in the joint `(Q,N)` chart one has the regular function
`a=n2/n3`, which agrees with the double root on the kernel, but that
regularity is after localizing at `M` and is not claimed. The target
already refuses the silent promotion.

Control: `Q=z^2(z^2+p)`, `N=z(z^2+p)` is `(4.1)` at `a=0`, `E=p`, `M=1`,
and `Q|N^2` holds identically for every `p`. For `p!=0` one is on the
incidence open.

---

## Attack 6 — binomial `3/8` and the Faber license

Work in characteristic zero. The binomial series

```text
(1+X)^{3/2}
  = 1 + (3/2)X + (3/2)(1/2)/2! X^2
      + (3/2)(1/2)(-1/2)/3! X^3 + O(X^4)
  = 1 + (3/2)X + (3/8)X^2 - (1/16)X^3 + O(X^4)
```

is the unique characteristic-zero expansion. For
`C=Q^2+epsilon^d N+higher` one has, at fixed `z`,

```text
C^{3/2}
  = Q^3 (1 + epsilon^d N/Q^2 + ...)^{3/2}
  = Q^3 + (3/2) epsilon^d N Q + (3/8) epsilon^{2d} N^2/Q
      + O(epsilon^{3d}) + contributions of "higher".
```

The first two summands are polynomials in `z` (`deg Q^3=12`,
`deg N Q<=7`). The first term that can have a negative principal part
is therefore `(3/8) epsilon^{2d} N^2/Q`, which is `(5.1)`. The constant
`3/8` is a unit in characteristic zero, so vanishing of the negative
part of `(5.1)` is equivalent to vanishing of the negative part of
`N^2/Q`, which by `(1.2)` is equivalent to `Q|N^2`. In characteristic
three the same coefficient is zero and the argument would collapse; the
target correctly restricts §5 to characteristic zero.

Ordinary Faber replacement. Let `w=Q^{1/4}=z+O(z^{-1})` in the monic
branch, with inverse `z(w)=w+O(w^{-1})`. Then `z(w)^{-j}=w^{-j}+` terms
of degree at most `-(j+1)`. The map sending the first seven negative
`z`-coefficients `(h1,...,h7)` to the first seven ordinary inverse-root
coefficients `(Phi_1,...,Phi_7)` is therefore lower unitriangular with
diagonal one, and `Phi_k` does not involve `h_j` for `j>k`. The reviewed
explicit connection

```text
R1=h1,
R2=h2,
R3=h3+(p/4)h1,
R4=h4+(p/2)h2+(c/4)h1,
...
R7=h7+(5p/4)h5+c h4+...
```

is one such matrix (denominators are powers of two, units in
characteristic zero). For any such connection, a complete initial block
of length `k<=7` vanishes if and only if `h1=...=h_k=0`. Combined with
`(1.2)`, vanishing of the first four ordinary rows is equivalent to
`Q|N^2`, and then all seven ordinary rows vanish.

The license fails, and the target does not invoke it, in each of the
following situations:

- the target is not a complete initial block (the affine-`mu2` system
  `R2=mu2` with the other six rows zero is the standard example:
  `R4=h4+(p/2)h2` need not force `h4=0`);
- a load, target, or lower correction occupies the same grade as
  `(5.1)`, producing an inhomogeneous summand that is not a function of
  `(h1,...,h7)` alone;
- one substitutes a connection that is not lower unitriangular of
  diagonal one (a finite-point expansion, a logarithmic Faber
  convention, or a numbering that skips a row);
- characteristic two, for the displayed connection with denominators
  `2,4,8,32,128` (not claimed: §5 is characteristic zero).

Only the unitriangular diagonal-one property is used, as stated.

---

## Attack 7 — timing firewall

At an untied grade, `(5.1)` is the complete contribution to the first
ordinary block, and Attack 6 applies. At a tied grade the same algebraic
description of the unloaded summand remains, but:

- forcing from the tied load, target, or lower correction must be
  retained;
- predecessor reduction is mandatory before any vanishing criterion is
  read as a kernel statement;
- successive corrections, torsion, and two-sided overlap data are not
  evaluated and are not deleted.

The lemma therefore classifies only the unloaded first-block summand.
It does not cancel a higher jet, a relative Newton cone, or an overlap
identity. Section 5 states this restriction in those words, and the
routing table that follows is the unloaded classification

```text
squarefree Q              -> N=0;
Q=A^2 D, D squarefree     -> N=M A D;
more degenerate Q         -> separate receiver.
```

The second line, as written in §5, omits `gcd(A,D)=1`. As recorded in
Attack 4 that omission is algebraically correct on the nose of `(3.1)`
whenever `D` is squarefree; the triple-plus-simple type is the overlap
with the third line and is already flagged in §3 as a separate
receiver. This is routing language, not a second kernel formula.

---

## Attack 8 — rejected strengthenings

The target states, and this review enforces, that the lemma does not
prove any of the following:

- higher-jet absorption;
- a relative Newton cone;
- a Rees kernel or torsion statement;
- a literal source / affine-Faber overlap;
- total-Rees accessibility;
- total-fan coverage;
- order two;
- `(8,12)`;
- maximum twelve;
- JC2.

No such strengthening is confirmed. The elementary equivalences `(1.2)`,
`(3.1)`, `(3.2)`, the incidence open of §4, and the unloaded
characteristic-zero identity `(5.1)` are the entire surviving content.

---

## Controls replayed

| Control | Independent result |
|---|---|
| Squarefree: `Q=z^4-1`, `N=z^3` | remainder `z^2`, `h2=1`, first block nonzero |
| Repeated-`A`: `Q=z^2(z^2+p)`, `N=z(z^2+p)` | `Q\|N^2` identically; `Q_half=A D` divides `N` |
| Four-row sharpness: `R=1` | `h1=h2=h3=0`, `h4=1`, realized by `N=1` |
| Degenerate `D=B^2`: `Q=(z^2-a^2)^2`, `N=z^2-a^2` | `Q\|N^2` holds; `A D=(z-a)(z+a)^2` does not divide `N` |
| Triple plus simple: `Q=(z-1)^3(z+3)` | `Q\|(A^2 B)^2` holds; `Q` does not divide `(A B)^2` |
| Reciprocal series of `1/Q` | `z^{-4}-q2 z^{-6}-q1 z^{-7}+O(z^{-8})`, matching V2 |

---

## Strongest exact theorem that survives

Let `k` be a field, `Q=z^4+q2 z^2+q1 z+q0`, and `N` of degree at most
three. Euclidean division `N^2=A Q+R` and the expansion of `R/Q` at
infinity give the triangular identities `(1.1)`. The following are
equivalent: `h1=h2=h3=h4=0`; `h1=...=h7=0`; `Q` divides `N^2` in `k[z]`.
Four rows are sharp by `R=1`. Unique factorization gives `Q|N^2` iff
`Q_half|N`. On the coprime squarefree type `Q=A^2 D` this is
`N=M A D`. On the depressed incidence `D=A^2+4a A+E`, the open
`E!=0` and `(4a)^2-4E!=0` is exactly that type; `(4.1)` is its kernel,
as a chart statement, not as a global regular section of quartic
coefficients. In characteristic zero, at a grade where no load, target,
or lower correction ties `(3/8) epsilon^{2d} N^2/Q`, vanishing of a
complete initial ordinary block of length four (equivalently seven)
obtained from `(h_j)` by a lower-unitriangular diagonal-one connection
is equivalent to `Q|N^2`. At a tied grade this is only the unloaded
summand.

**CONFIRMED**
