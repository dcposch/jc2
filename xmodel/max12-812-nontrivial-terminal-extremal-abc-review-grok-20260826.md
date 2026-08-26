# Hostile review — `(8,12)` nontrivial terminal maps are balanced extremal abc triples

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-nontrivial-terminal-extremal-abc-classification-20260826.md` |
| Target SHA-256 | `149691f1784ffccea9473a63efaec4a7d0eea56f9c1e1ba267610b104022920e` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. The charged terminal-power review is same-model and is not used as a PASS/CONFIRMED certificate; the terminal identity, exact Kummer order, finite dictionary, absence of off-fibre finite critical points, and the two infinity alternatives are taken as the *statements* of the charged theorem, then the Wronskian, zero-at-infinity elimination, balanced abc equality, fibres, radicand, and converse are re-derived below from those statements alone |
| Method | source reading and hand derivation only; SHA-256 of the target and the two named parents; no CAS, solver, substantive Python, Lean, or other heavy local computation |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `4fe628a133ae62e16b1bec5e4ed6fcee420dd880` (named producer artifact uncommitted) |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target is `149691f1784ffccea9473a63efaec4a7d0eea56f9c1e1ba267610b104022920e`, matching the launch pin. Both charged sources match the hashes printed in the target's Charged input section. Producer verdict language, the target's own status line, the coordinator summary, and any prior PASS/CONFIRMED token were not used as evidence. No file other than this review was written.

---

## Verdict

The charged classification is correct as a terminal necessary-and-sufficient passport theorem on both nontrivial `(8,12)` Kummer leaves. Independently: the identity `d(T')^m=C T^{m-1}` with `C=(m j/8)^m` forces `d=C A^{m-1} B^{m+1}/W^m` and the local Wronskian orders `ord(W)=alpha-1`, `ord(d)=m-alpha` at a numerator root and `ord(W)=beta-1`, `ord(d)=m+beta` at a denominator root, with no finite zero of `W` off `AB`; the strict unequal-degree case has Wronskian leading coefficient `(a-b)\mathrm{lc}(A)\mathrm{lc}(B)\neq 0`, hence `deg W=a+b-1=a+b-r-s` and `r+s=1`, so `s=1`, `r=0`, a unique geometric pole, `d=c(x-b_1)^{mU}`, and after the licensed scalar extension an `m`-th power, contradicting exact order `m` for both `m=2` and `m=4`; the remaining branch is balanced of some degree `D\geq 1` with `T(\infty)=\lambda\in L^*` and `U\geq 2`; after `T\mapsto T/\lambda` one has `C_{\mathrm{hat}}=C/\lambda`, monic coprime `A,B`, `deg G=D-U+1`, `G` squarefree (constants allowed), Wronskian leading coefficient `(1-U)\mathrm{lc}(G)\mathrm{lc}(B)\neq 0`, `deg W=2D-U`, `r+s=U`, `deg\mathrm{rad}(ABG)=D+1`, and `W=\kappa AB/(\mathrm{rad}(A)\mathrm{rad}(B))`; the three fibres are exactly `(0.8)` and saturate Riemann--Hurwitz; both degree bounds hold, with the edges `U=2`, `D=U-1`, and `D=m(U-1)` consistent (the last is excluded by the gcd condition, not by the inequality); the radicand is the displayed product of degree `mU`, its Kummer order is `m/\gcd(m,\mathrm{all}\,\alpha_i,\mathrm{all}\,\beta_j)`, and exact order `m` is the gcd condition; the converse hypotheses suffice, with no omitted scalar, coprimality, degree, or separability hypothesis that breaks a numbered claim. Passing these identities does not solve the other six tails, produce Taylor polynomiality, close either nontrivial leaf, or touch JC2.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-nontrivial-terminal-extremal-abc-classification-20260826.md` | `149691f1784ffccea9473a63efaec4a7d0eea56f9c1e1ba267610b104022920e` | target (matches required pin) |
| `xmodel/max12-812-terminal-power-belyi-order1-theorem-20260825.md` | `a4d7d6a1173b5a0b785aa61a4c80ad5f46e4ea83f1d73103917c425608666633` | charged terminal identity `(0.2)`, exact order `e\in\{2,4\}`, `deg d=eU`, finite dictionary `(0.5)`, no finite critical point off `{T=0,\infty}`, two infinity alternatives `(0.6)` |
| `xmodel/max12-812-terminal-power-belyi-order1-review-grok-20260825.md` | `e322d508c2af66aebb408b2794bd017b05e96cf9ca67f0fc74be8407406f67e1` | same-model audit of the charged theorem (read; unused as a verdict) |

Both parent hashes match the target's Charged input table. The charged theorem is consumed only for the rewritten identity `d(T')^m=(m j/8)^m T^{m-1}` with `d=h` on order four and `d=v` on order two, exactness of the class, `deg d=mU`, the finite local dictionary, absence of finite critical points off the zero and pole fibres, and the two local forms at infinity (in particular: no pole of `T` at infinity, and `ord_\infty(T-\lambda)=U-1` on the finite-nonzero branch). Its order-one classification is not an input. No scope-firewall sentence of either parent is an input.

---

## Strongest exact theorem that survives

Let `L` be a characteristic-zero field after the already licensed finite constant extension (roots of unity and leading scalar roots). Let `m\in\{2,4\}` be the exact order of a nontrivial Kummer leaf, let `d\in L[x]` be its minimal polynomial radicand of degree `mU` with `U\geq 1`, and suppose

```text
d (T')^m = C T^{m-1},       C=(m j/8)^m \in L^*,       T\in L(x) nonconstant.
```

Then `T(\infty)=0` is impossible, necessarily `U\geq 2` and `T(\infty)=\lambda\in L^*`, and after replacing `T` by `T/\lambda` (which replaces `C` by `C/\lambda`) one may write `T=A/B` with `A,B` coprime monic of equal degree `D\geq 1`. Putting `G=A-B` and `W=A'B-AB'`, writing `alpha_1,\ldots,alpha_r` and `beta_1,\ldots,beta_s` for the geometric multiplicities of `A` and `B`, one has `1\leq alpha_i\leq m`, `beta_j\geq 1`, `r+s=U`, `deg G=D-U+1`, `G` squarefree (a nonzero constant allowed), `W=\kappa AB/(\mathrm{rad}(A)\mathrm{rad}(B))` for some `\kappa\neq 0`, and `deg\mathrm{rad}(ABG)=D+1`. Thus `A-B=G` is an equality case of polynomial abc. The rational map `T` has fibres

```text
over 0:        (alpha_1,...,alpha_r),
over infinity: (beta_1,...,beta_s),
over 1:        (U-1, 1^{D-U+1}),
```

the first slot over `1` being `x=\infty`, and these three fibres saturate Riemann--Hurwitz. In particular `U-1\leq D\leq m(U-1)`. The radicand is, up to its nonzero scalar,

```text
d = C_{\mathrm{hat}} A^{m-1} B^{m+1}/W^m
  = c \prod_i (x-a_i)^{m-alpha_i} \prod_j (x-b_j)^{m+beta_j},
```

of degree `mU`, with `C_{\mathrm{hat}}=C/\lambda`. Its class in the Kummer quotient has order `m/\gcd(m,alpha_1,\ldots,alpha_r,beta_1,\ldots,beta_s)`, hence exact order `m` if and only if that gcd is `1`.

Conversely, a coprime equal-degree triple `A-B=G` satisfying the displayed numerical and squarefreeness conditions, together with the gcd condition, produces through the radicand formula a polynomial of degree `mU` and an exact solution of the terminal identity, after the harmless scalar normalization. This converse reconstructs only the terminal equation.

This is only the terminal classification and passport enumerator. It does not produce the other six tails, Taylor polynomiality, a Keller pair, order-two or order-four closure, `(8,12)`, maximum twelve, or JC2.

---

## Attack 1 — Wronskian formula and every local order

**CONFIRMED.** Formula `(1.2)` is the identity rewritten in coprime coordinates; the three local computations `(1.3)`, `(1.4)`, and vanishing of `W` off `AB` are exact; `(1.5)` follows as a polynomial identity, equivalently `(0.6)` once the degrees are balanced.

Write a reduced presentation `T=A/B` in `L(x)`, with `A,B\in L[x]` coprime and `W=A'B-AB'`. Nonconstancy of `T` gives `W\neq 0`. Differentiation in characteristic zero yields `T'=W/B^2`, hence `(T')^m=W^m/B^{2m}`. Substitute into the charged identity `d(T')^m=C T^{m-1}`:

```text
d W^m / B^{2m} = C A^{m-1} / B^{m-1},
```

and therefore

```text
d W^m = C A^{m-1} B^{m+1},       d = C A^{m-1} B^{m+1}/W^m.
```

This is `(1.2)`, with no equal-degree hypothesis.

Work over an algebraic closure. Characteristic zero is used at every order computation: if a polynomial has multiplicity `n\geq 1` at a finite point then its derivative has multiplicity `n-1`, because the leading coefficient is multiplied by the nonzero integer `n`.

**Numerator root, multiplicity `alpha\geq 1`.** Coprimality makes `B` a unit there. Write `A=(x-a)^alpha \tilde A` with `\tilde A(a)\neq 0`. Then

```text
W = \bigl(alpha (x-a)^{alpha-1} \tilde A + (x-a)^alpha \tilde A'\bigr) B
    - (x-a)^alpha \tilde A B',
```

so the leading term is `alpha \tilde A(a) B(a) (x-a)^{alpha-1}` with all three factors nonzero. Thus `ord(W)=alpha-1`. From `(1.2)`,

```text
ord(d) = (m-1)alpha - m(alpha-1) = m-alpha.
```

Polynomiality of `d` forces `m-alpha\geq 0`, hence `alpha\leq m`. Combined with `alpha\geq 1` this is the first line of `(0.5)`. (An uncharged zero of `T` is the endpoint `alpha=m`, giving `ord(d)=0`, which is exactly the charged dictionary's uncharged zero of order `e` at a point with `k=0`.)

**Denominator root, multiplicity `beta\geq 1`.** Coprimality makes `A` a unit. The same expansion with the roles reversed gives leading term `-beta A(b)\tilde B(b)(x-b)^{beta-1}`, hence `ord(W)=beta-1`, and

```text
ord(d) = (m+1)beta - m(beta-1) = m+beta \geq m+1 > 0.
```

This matches the charged dictionary: a pole of order `beta` is a root of `d` of multiplicity `m+beta`.

**Finite point off `AB`.** Here `ord(A)=ord(B)=0`, so `ord(d)=-m\,ord(W)`. A zero of `W` of order `gamma\geq 1` would be a pole of `d` of order `m gamma`, positive and divisible by `m`. Impossible for a polynomial. Hence `W` has no finite zero off the support of `AB`. (A pole of `W` cannot occur: `W` is a polynomial.)

**Global formula.** A nonzero polynomial is determined, up to a scalar in `L^*`, by its finite zeros with multiplicity. Therefore

```text
W = \kappa \prod_i (x-a_i)^{alpha_i-1} \prod_j (x-b_j)^{beta_j-1},       \kappa\neq 0.
```

This is `(1.5)`. If `A` and `B` are written with those geometric roots, the same identity is `W=\kappa AB/(\mathrm{rad}(A)\mathrm{rad}(B))`, which is `(0.6)`, with `rad` the monic squarefree kernel; leading coefficients of `A,B` are absorbed in `\kappa`. Simple roots (`alpha_i=1` or `beta_j=1`) contribute the factor `1` and do not appear in `W`, as required.

The identity `(1.5)` does not need equal degrees. Its degree is `a+b-r-s` if `a=\deg A` and `b=\deg B`. That degree comparison is used next.

---

## Attack 2 — elimination of `T(\infty)=0`

**CONFIRMED.** Unequal-degree Wronskian leading terms, the conclusion `r+s=1`, unique-root descent, the scalar-class issue, and exact order for both `m=2` and `m=4` all survive.

The charged theorem supplies: `T` has no pole at infinity, hence `deg A\leq deg B` in any reduced presentation. Suppose strictly `a=\deg A < b=\deg B`.

**Leading term.** `A=\mathrm{lc}(A)x^a+\cdots`, `B=\mathrm{lc}(B)x^b+\cdots`, so

```text
A'B = a\,\mathrm{lc}(A)\mathrm{lc}(B)\, x^{a+b-1}+\cdots,
AB' = b\,\mathrm{lc}(A)\mathrm{lc}(B)\, x^{a+b-1}+\cdots,
```

and the Wronskian leading coefficient is `(a-b)\mathrm{lc}(A)\mathrm{lc}(B)`. Characteristic zero, `a\neq b`, and nonzero leadings give `deg W=a+b-1`. This is `(2.1)`. The competing formula `(1.5)` has degree `a+b-r-s`. Therefore `r+s=1`.

**Unique-root descent.** `B` is nonconstant (`b\geq a+1\geq 1`), so `s\geq 1`. Combined with `r+s=1` and `r\geq 0` one has `s=1`, `r=0`. Over an algebraic closure, `r=0` means `A` has no root, hence `A` is a nonzero constant (`a=0`). Then `B` has a unique geometric root, so `B=b_0(x-b_1)^b`. The unique geometric root of a polynomial already in `L[x]` is Galois-stable over `L`; in characteristic zero the minimal polynomial is separable, hence linear, so `b_1\in L` with no further extension. Formula `(1.4)` gives `d` a single geometric root of multiplicity `m+b`. Since `deg d=mU`,

```text
m+b=mU,       b=m(U-1),       d=c(x-b_1)^{mU}.
```

(The case `U=1` would force `b=0`, contradicting `a<b`. It is already empty in the charged theorem. Thus `U\geq 2` on this branch, and `b=m(U-1)\geq m\geq 2`.)

**Scalar class, then exact order.** In `L(x)^*/(L(x)^*)^m` the class of `d=c(x-b_1)^{mU}` equals the class of the constant `c`: both finite and infinite valuations of the geometric part are multiples of `m`. The charged opening enlarges `L` so that leading scalar roots are present, and the target's Section 5 records that this makes the leading scalar an `m`-th power. Thus `c=\gamma^m` in `L`, and `d=(\gamma(x-b_1)^U)^m` is an `m`-th power in `L(x)`. The class has order `1`, contradicting exact Kummer order `m\in\{2,4\}`.

Equivalently, `T=A/B=\mathrm{const}/(x-b_1)^{m(U-1)}` is itself an `m`-th power after the same scalar extension, and the class of `d` equals the class of `T^{-1}` modulo `m`-th powers (Attack 5), hence is likewise trivial.

**Both `m=2` and `m=4`, with the constant-class fake named and killed.** Without the licensed scalar extension the class of `d` would equal the class of `c` in `L^*/(L^*)^m`.

- For `m=2`, exact order two would survive if `[c]` had order two. That is a constant-class artifact: adjoining a square root of the leading coefficient, which the charged theorem already licenses, collapses the class to order one.
- For `m=4`, exact order four would survive only if `[c]` had order four (i.e. `c` not a square). If `[c]` had order two, the class of `d` would have order two, already the wrong leaf. Adjoining a fourth root of the leading coefficient, again licensed, collapses every constant class to order one.

In both live orders the strict inequality `deg A<deg B` is therefore impossible. Combined with the charged prohibition on poles at infinity, one has `deg A=deg B=D` for some `D\geq 1` (nonconstancy of `T` forbids `D=0`) and `T(\infty)=\lambda=\mathrm{lc}(A)/\mathrm{lc}(B)\in L^*`. The charged finite-nonzero form at infinity then requires `U\geq 2`. This is `(0.2)`--`(0.3)`.

The charged `T(\infty)=0` alternative is not left open as a descriptive branch: it is empty on both nontrivial leaves.

(As a parenthetical, the complementary inequality `deg A>deg B` is already excluded by the charged absence of a pole at infinity. Independently, the same Wronskian comparison would give `r+s=1` with `r=1`, `s=0`, a unique geometric zero, `ord(d)=m-a=mU`, hence `a=m(1-U)\leq 0`, a contradiction. The classification does not need this, and does not claim it.)

---

## Attack 3 — balanced degree, squarefreeness, radical degree, and `(0.6)`

**CONFIRMED.** Normalization by `lambda`, `deg G=D-U+1`, squarefreeness including constant `G`, `deg W=2D-U`, `r+s=U`, `deg\mathrm{rad}(ABG)=D+1`, and `W=\kappa AB/(\mathrm{rad}(A)\mathrm{rad}(B))` all survive.

**Normalization.** Set `\lambda=T(\infty)\in L^*`. Replace `T` by `T/\lambda`. If the original identity is `d(T')^m=C T^{m-1}`, the new functions satisfy

```text
d\,(\lambda T_{\mathrm{new}}')^m = C\,(\lambda T_{\mathrm{new}})^{m-1},
```

hence `d(T_{\mathrm{new}}')^m=(C/\lambda)T_{\mathrm{new}}^{m-1}`. The new constant is `C_{\mathrm{hat}}=C/\lambda\in L^*`, independent of `m` as an exponent on `\lambda`. Now `T_{\mathrm{new}}(\infty)=1`. Clearing a common scalar makes the coprime degree-`D` polynomials `A,B` monic; equal degree and value `1` at infinity force `\mathrm{lc}(A)=\mathrm{lc}(B)=1`.

**Degree of `G`.** The charged infinity formula, transported to the normalized map, is `ord_\infty(T/\lambda-1)=U-1`. But `T/\lambda-1=G/B` with `G=A-B\neq 0` (else `T` is constant). Thus `D-\deg G=U-1`, so `deg G=D-U+1`. In particular `D\geq U-1`. This is `(3.2)`.

**Squarefreeness.** Suppose a finite root of `G` has multiplicity at least two. Coprimality of `A` and `B` together with `G=A-B` forbids that point from being a root of `A` or of `B`, so `T` is finite and equal to `1` there, with local degree at least two. That is a finite critical point of value `1`, off `{T=0,\infty}`, contradicting the charged finite local dictionary. Hence every finite root of `G` is simple. A nonzero constant has no finite root and is squarefree as a convention; this is the case `deg G=0`, i.e. `D=U-1`. Thus `G` is squarefree, constants allowed.

**Pairwise coprimality.** `A` and `B` are coprime by construction. A common root of `A` and `G` would be a root of `B`, and likewise for `B` and `G`. So `A,B,G` are pairwise coprime.

**Degree of `W`.** Substitute `A=B+G` into the Wronskian:

```text
W = G'B - G B'.
```

Now `deg G=D-U+1` and `deg B=D`, so both `G'B` and `GB'` have degree `(D-U+1-1)+D=2D-U`. The leading coefficient is

```text
(\deg G - D)\,\mathrm{lc}(G)\,\mathrm{lc}(B) = (1-U)\,\mathrm{lc}(G)\,\mathrm{lc}(B).
```

This is nonzero: `U\geq 2` so `1-U\neq 0`, and both leadings are nonzero because the degrees of `G` and `B` are exact. Hence `deg W=2D-U`. (The equal-degree cancellation of the naive `x^{2D-1}` terms is already accounted for: those cancel, and the next surviving degree is `2D-U` rather than `2D-1`.)

The formula `(1.5)` has degree `2D-r-s`. Comparison gives `r+s=U`.

**Radical degree and abc equality.** `G` squarefree implies `deg\mathrm{rad}(G)=\deg G` (and `=0` when `G` is a nonzero constant, taking `\mathrm{rad}(G)=1`). Therefore

```text
deg\mathrm{rad}(ABG) = r+s+\deg G = U+(D-U+1) = D+1.
```

Mason--Stothers for a coprime triple `A-B=G`, not all constant, reads `\max(\deg A,\deg B,\deg G)\leq\deg\mathrm{rad}(ABG)-1`. Here the maximum is `D` (since `U\geq 2` gives `deg G\leq D-1`), and `D\leq(D+1)-1=D`. Equality. This is the polynomial abc equality case. Formula `(1.5)` is exactly `(0.6)`.

**Positive degrees.** `D\geq 1` and an algebraic closure give `r,s\geq 1`. Combined with `r+s=U` one has `r\leq U-1`. Then `D=\sum alpha_i\leq m r\leq m(U-1)`. Together with `D\geq U-1` from `(3.2)`, this is `(0.9)`.

**Bookkeeping of `(0.10)` against the original `d`.** The original (un-normalized) presentation `T=A_0/B_0` has `\lambda=\mathrm{lc}(A_0)/\mathrm{lc}(B_0)` and Wronskian `W_0`. The monic choice `A=A_0/\mathrm{lc}(A_0)`, `B=B_0/\mathrm{lc}(B_0)` gives `W=W_0/(\mathrm{lc}(A_0)\mathrm{lc}(B_0))`. Substituting into `C_{\mathrm{hat}} A^{m-1} B^{m+1}/W^m` produces

```text
(C/\lambda)\cdot A_0^{m-1} B_0^{m+1}/W_0^m \cdot \mathrm{lc}(A_0)/\mathrm{lc}(B_0)
  = C A_0^{m-1} B_0^{m+1}/W_0^m = d,
```

because `\mathrm{lc}(A_0)/\mathrm{lc}(B_0)=\lambda` cancels the denominator of `C_{\mathrm{hat}}`. Formula `(0.10)` is the original radicand, not a scalar multiple of it.

---

## Attack 4 — three fibres, edges `U=2`, `D=U-1`, `D=m(U-1)`, RH saturation, both bounds

**CONFIRMED.** The passport `(0.8)` is exact, including the unramified and constant-`G` edges; Riemann--Hurwitz is saturated; both degree bounds hold.

**Fibres.** The fibre over `0` is the list of multiplicities of `A`. The fibre over `\infty` is the list of multiplicities of `B`. The fibre over `1` consists of the finite roots of `G`, each simple, together with `x=\infty` of local degree `U-1`. There are `deg G=D-U+1` finite points. This is `(0.8)`, and the local-degree sum over `1` is `(U-1)+(D-U+1)=D`.

Finite preimages of `1` are unramified (local degree one). This is required by the charged prohibition on finite critical points off `{0,\infty}`: the value `1` is neither `0` nor `\infty`, so it cannot be a finite critical value. The only possible ramification over `1` is at `x=\infty`, and only when `U\geq 3`.

**Riemann--Hurwitz.** Total ramification of a degree-`D` map `P^1\to P^1` is `2D-2`. The three displayed fibres contribute

```text
\sum_i (alpha_i-1) + \sum_j (beta_j-1) + (U-1-1) + \sum_{\mathrm{finite}\,G}(1-1)
  = (D-r)+(D-s)+(U-2)
  = 2D-(r+s)+U-2
  = 2D-2,
```

using `r+s=U`. Equality, so there is no remaining ramification and no hidden fourth branch value. (The charged three-value statement already names the branch locus; the computation shows those three fibres *exhaust* the ramification, not merely contain it.)

**Edge `U=2`.** Then `r+s=2` with `r,s\geq 1`, so `r=s=1`, and `1\leq D\leq m`. The slot over `1` at infinity has local degree `1`, so `U-2=0` and infinity is unramified. Finite preimages of `1` are likewise unramified. The value `1` is never a branch value when `U=2`. This matches the charged “may be unbranched when `U=2`”, and is in fact always unbranched on the surviving `T(\infty)\in L^*` branch. If additionally `D=1`, then `2D-2=0` and the map is a Möbius transformation; the branch locus is empty and `(0.8)` remains valid as a fibre description.

**Edge `D=U-1`.** Then `deg G=0`, `G` a nonzero constant, and there is no finite preimage of `1`. The fibre over `1` is the single point `x=\infty` of index `U-1`. Squarefreeness holds by the constant convention. The Wronskian is `W=-G B'` of degree `D-1`, and `2D-U=2(U-1)-U=U-2=D-1`, matching. Leading coefficient: `-G\cdot D\cdot\mathrm{lc}(B)=(1-U)G\mathrm{lc}(B)` since `D=U-1`. Riemann--Hurwitz still reads `2D-2` as an identity in `r+s=U`. For `U=2` this is the degree-one case already named. For `U\geq 3` the unique ramified preimage of `1` is infinity.

**Edge `D=m(U-1)`.** Equality in `D\leq m r\leq m(U-1)` forces `r=U-1` and `alpha_i=m` for every `i`, hence `s=1` and `beta_1=D=m(U-1)`. All zeros of `T` are uncharged. The numerical bound holds. The gcd condition does *not*: `\gcd(m,m,\ldots,m,m(U-1))=m\neq 1`. So this edge is compatible with the inequality `(0.9)` and is excluded from exact order `m` by `(0.11)`, not by the degree bound. The enumerator `(7.1)` therefore correctly lists `D\leq m(U-1)` and then drops this vertex by the gcd filter.

**Both bounds.** Lower: `deg G\geq 0` gives `D\geq U-1`, attained. Upper: `alpha_i\leq m` and `r\leq U-1` give `D\leq m(U-1)`, valid as an inequality, never attained at exact order `m`. No further constraint comes from Riemann--Hurwitz: the ramification identity is tautological once `r+s=U`.

---

## Attack 5 — radicand factorization and exact Kummer order

**CONFIRMED.** The product formula has degree `mU`; infinity does not contribute; zero exponents do not corrupt the gcd; constant extensions are the licensed ones; exact order four is distinguished from its order-two degeneration.

**Product formula.** Local orders from Attack 1 give `ord_{a_i}(d)=m-alpha_i\geq 0` and `ord_{b_j}(d)=m+beta_j\geq m+1`, and `ord(d)=0` off that support. Hence

```text
d = c \prod_i (x-a_i)^{m-alpha_i} \prod_j (x-b_j)^{m+beta_j}
```

for some `c\in L^*`. The degree is

```text
\sum_i (m-alpha_i)+\sum_j (m+beta_j) = m(r+s) - D + D = mU.
```

Substituting `(0.6)` into `(1.2)` produces the same product, with `c` determined by `C_{\mathrm{hat}}` and `\kappa`. This is `(0.10)`. Polynomiality is exactly `alpha_i\leq m`.

**Class order.** After the licensed extension the leading scalar is an `m`-th power, so the class of `d` in `L(x)^*/(L(x)^*)^m` is the class of the divisor of exponents modulo `m`. Those exponents are `m-alpha_i\equiv -alpha_i\pmod{m}` and `m+beta_j\equiv beta_j\pmod{m}`. The valuation at infinity is `-mU\equiv 0\pmod{m}` and does not contribute. Therefore the order is

```text
m / \gcd(m,\,alpha_1,\ldots,alpha_r,\,beta_1,\ldots,beta_s).
```

This is `(5.2)`, and exact order `m` is `(0.11)`.

Equivalently, modulo `m`-th powers one has `[d]=[B/A]=[T]^{-1}` (leadings being `m`-th powers after the same extension), so the order of `[d]` is the order of `[T]`, which is `m/\gcd(m,\mathrm{all\ parts\ of\ }A\mathrm{\ and\ }B)`. Same formula.

**Zero exponents.** If `alpha_i=m` then the factor `(x-a_i)^{m-alpha_i}` is `1` and that prime is absent from `d`. Including `alpha_i=m` in the gcd with `m` does not change the gcd. Omitting those places and taking the gcd of the actual exponents of `d` yields the same value: `\gcd(m,\{m-alpha_i:alpha_i<m\},\{m+beta_j\})=\gcd(m,\mathrm{all\ }alpha_i,\mathrm{all\ }beta_j)`. No corruption.

**Constants.** The licensed finite constant extension is present from the first sentence of the charged theorem and of the target. It is what makes the leading scalar an `m`-th power and removes constant-class artifacts. Without it, the order of `[d]` would be `\mathrm{lcm}(\mathrm{order}[c],\,m/\gcd(m,\mathrm{parts}))` rather than `(5.2)`. That is not the setup.

**Order two versus exact order four.** The positive divisors of `4` are `1,2,4`. Thus `\gcd(4,\mathrm{parts})=1` if and only if some part is odd. An all-even order-four passport has `\gcd\geq 2`: if some part is `2\bmod 4` the class has order `2` and belongs to the order-two leaf; if every part is `0\bmod 4` the class has order `1` and belongs to the order-one leaf. An order-two passport (`m=2`) needs at least one odd part for the same reason. The target's last sentence of Section 5 is exact.

---

## Attack 6 — converse hypotheses

**CONFIRMED.** The stated hypotheses suffice for a polynomial radicand, the exact terminal identity, and exact class. No omitted scalar, coprimality, degree, or separability hypothesis breaks a numbered claim.

Take a coprime equal-degree triple `A-B=G` of degree `D\geq 1` satisfying `(0.5)` — i.e. `1\leq alpha_i\leq m`, `beta_j\geq 1`, `r+s=U`, `deg G=D-U+1`, `G` squarefree with a nonzero constant allowed — together with `(0.11)`. Characteristic zero is standing.

**Recovery of `(0.6)`.** Local differentiation, as in Attack 1, makes `A/\mathrm{rad}(A)` and `B/\mathrm{rad}(B)` divide `W`, independently of `G`. Their total degree is `(D-r)+(D-s)=2D-U`, using `r+s=U`. The identity `W=G'B-GB'` together with `deg G=D-U+1` gives leading coefficient `(1-U)\mathrm{lc}(G)\mathrm{lc}(B)`. This is nonzero: `r,s\geq 1` (positive degree over an algebraic closure) forces `U=r+s\geq 2`, and the degree of `G` is exact. Thus `deg W=2D-U`, there is no remaining factor, and `(0.6)` holds.

Squarefreeness of `G` is in fact redundant for this degree count, but not optional as a geometric condition: a multiple root of `G` off `AB` would be an extra zero of `W=G'B-GB'`, pushing the zero-order of `W` strictly above `deg W` and forcing `W\equiv 0`. So squarefreeness is a consequence of the other numerical hypotheses in the balanced case, and listing it in `(0.5)` is correct.

**Polynomial radicand and the identity.** Define `d` by `(0.10)`. Then `alpha_i\leq m` makes every exponent `m-alpha_i` nonnegative, so `d` is a polynomial, of degree `mU` by `(5.1)`. The algebraic substitution `T=A/B`, `T'=W/B^2` into `d(T')^m` returns `C_{\mathrm{hat}} T^{m-1}` by construction of `(1.2)`. This is `(0.1)` after the harmless scalar normalization already used in the forward direction (absorbing `\lambda` and matching `C=(m j/8)^m` by the choice of `j\in L^*`, or by taking `j=8/m` so that `C=1`).

**Leading scalar of the produced `d`.** With monic `A,B` and `T(\infty)=1`, the Wronskian leading coefficient is `(1-U)\mathrm{lc}(G)`, and

```text
\mathrm{lc}(d) = C / \bigl((1-U)\mathrm{lc}(G)\bigr)^m,
```

which is an `m`-th power in `L` as soon as `C` is. No further constant extension is required for `(5.2)`. (If one prefers to start from non-monic equal-degree data, the bookkeeping of Attack 3 converts to this case by a scalar in `L^*`.)

**Exact class.** Formula `(5.2)` then gives order `m` under `(0.11)`. Infinity remains valuation `-mU`. Zero exponents remain harmless.

**Implied, not omitted.** Equal degree plus `deg G=D-U+1\leq D-1` forces `\mathrm{lc}(A)=\mathrm{lc}(B)`, hence `T(\infty)=1` after scaling; `U\geq 2` is forced by `r,s\geq 1`; `D\geq 1` is forced by nonconstancy; pairwise coprimality of the triple is the stated coprimality of `A,B` together with `G=A-B`; `G\neq 0` is nonconstancy of `T`. Separability of `G` is stated. Separability of `A` or `B` is not required and not used: multiple roots are the data `alpha_i`, `beta_j`. The gcd is taken after splitting over an algebraic closure, equivalently as the gcd of multiplicities of irreducible factors over `L`; conjugate roots share a multiplicity, so the gcd is unchanged.

**What would have been a missing hypothesis, and is not.** A converse that produced a polynomial `d` whose leading coefficient was not an `m`-th power would need an extra scalar hypothesis, or would have to re-license a constant extension. The produced leading coefficient is visibly an `m`-th power. A converse that omitted `alpha_i\leq m` would fail polynomiality. That bound is in `(0.5)`. A converse that omitted coprimality of `A` and `B` would lose `ord(W)=alpha-1`. Coprimality is stated. A converse that omitted `deg G=D-U+1` would lose `deg W=2D-U`. That degree is in `(0.5)`.

The converse reconstructs only the terminal identity and the minimal radicand. It does not reconstruct `f,g` or any lower tail, as the target states.

---

## Attack 7 — firewall

**CONFIRMED**, with one non-blocking campaign sentence named below.

The theorem is a classification of solutions of the terminal identity on the two nontrivial leaves, together with a passport enumerator at each fixed `U`. Every numbered conclusion stays inside that scope.

Section 7 says that for each fixed `U` the nontrivial terminal search is finite at the passport level, via `(7.1)`, and that each surviving passport asks for an extremal polynomial abc triple, hence a finite dessin problem at fixed `D`, with the exact differential remaining the source condition. That is an enumerator, not a census of realized passports, not a lift to the lower Faber fibre, and not a bound on `U`. The immediately following paragraph states that nothing here bounds `U`, verifies the six lower Faber tails, fixes the nine remaining Faber constants, proves either Taylor polynomiality family, constructs or excludes an original polynomial Keller pair, closes order two or order four, resolves `(8,12)` or maximum twelve, or proves or disproves JC2. That paragraph matches the required firewall.

The converse paragraph restricts itself to the terminal differential equation and explicitly refuses the other six tails and a Keller pair.

No sentence claims lower-tail compatibility, Taylor polynomiality, `(8,12)` closure, maximum twelve, or JC2.

The single sentence that *names* a surface outside the firewall is Section 7, “This supplies a clean enumerator and a bridge to the live coefficient/Taylor clients.” It does not assert a theorem about those clients. It is campaign language, not a licensed implication, and is immediately cancelled by the explicit refusal paragraph. It is not a numbered failure.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | `d=C A^{m-1} B^{m+1}/W^m`; `ord(W)=alpha-1`, `ord(d)=m-alpha` at numerator roots with `alpha\leq m`; `ord(W)=beta-1`, `ord(d)=m+beta` at denominator roots; `W` has no finite zero off `AB`; `(1.5)` and `(0.6)` | **CONFIRMED** | `T'\neq W/B^2`; `char\mid alpha` so `ord(W)>alpha-1`; a finite zero of `W` off `AB` giving a pole of `d` of order divisible by `m`; `W\equiv 0` for nonconstant `T` |
| 2 | Unequal degrees give leading coefficient `(a-b)\mathrm{lc}(A)\mathrm{lc}(B)\neq 0`, `deg W=a+b-1`, `r+s=1`, unique geometric pole, `d=c(x-b_1)^{mU}` an `m`-th power after licensed scalars, contradiction to exact order for both `m=2` and `m=4`; hence `T(\infty)=\lambda\in L^*`, `U\geq 2`, `deg A=deg B` | **CONFIRMED** | leading terms of `A'B` and `AB'` failing to cancel only to order `a+b-1`; `r=1,s=0` surviving `a<b`; unique root not descending; constant class of `c` surviving the licensed extension and supplying exact order `m`; `m=4` collapsing only to order two rather than one |
| 3 | `C_{\mathrm{hat}}=C/\lambda`; `deg G=D-U+1`; `G` squarefree including constants; `deg W=2D-U` from leading coefficient `(1-U)\mathrm{lc}(G)\mathrm{lc}(B)`; `r+s=U`; `deg\mathrm{rad}(ABG)=D+1`; Mason--Stothers equality; `(0.6)` | **CONFIRMED** | `ord_\infty(T-\lambda)\neq U-1`; a finite multiple root of `G` compatible with the charged dictionary; `U=1` making the Wronskian leading coefficient vanish; `r+s\neq U`; `rad(G)` dropping degree |
| 4 | Passport `(0.8)`; RH saturation `2D-2`; edges `U=2` (value `1` unbranched), `D=U-1` (constant `G`), `D=m(U-1)` (bound valid, gcd kills exact order); `U-1\leq D\leq m(U-1)` | **CONFIRMED** | a fourth branch value; finite ramification over `1`; `U=2` ramified at `1`; constant `G` breaking `deg W=2D-U`; `D=m(U-1)` violating the inequality; `r=U` with `s=0` |
| 5 | Product `(0.10)` of degree `mU`; order `m/\gcd(m,\mathrm{all\ }alpha_i,\mathrm{all\ }beta_j)`; infinity valuation `-mU`; zero exponents harmless; exact order four needs an odd part, all-even data are order two or one | **CONFIRMED** | a leftover `m`-th power in the degree count; infinity contributing a non-multiple of `m`; `gcd` taken on `{m-alpha_i}` without reducing modulo `m` and changing the value; an all-even exact order-four class |
| 6 | Converse: stated hypotheses produce a polynomial radicand of degree `mU`, the terminal identity, and exact class; no missing scalar / coprimality / degree / separability hypothesis | **CONFIRMED** | produced `\mathrm{lc}(d)` not an `m`-th power; omitted `alpha_i\leq m`; omitted coprimality of `A,B`; omitted `deg G=D-U+1`; `U=1` sneaking into the leading-term count |
| 7 | Terminal classification and passport enumerator only; no lower tail, Taylor polynomiality, leaf closure, `(8,12)`, maximum twelve, or JC2 | **CONFIRMED** | a hidden promotion in the theorem statement, Section 7, or the converse |

---

## Remarks (non-blocking)

1. The vertex `D=m(U-1)` of the degree box is never occupied at exact order `m`, because it forces every `alpha_i=m` and a single `beta=m(U-1)`, hence `\gcd=m`. The inequality `(0.9)` is still correct, and `(7.1)` drops the vertex by the gcd filter. Not a numbered failure.
2. For `U=2` and `T(\infty)\in L^*`, the third value is always unbranched, not only possibly. The charged parent already had this strengthening as a remark; the present target inherits the weaker “first entry over `1` is `U-1`” fibre description, which remains correct when that entry is `1`.
3. Squarefreeness of `G` in `(0.5)` is redundant with the other converse hypotheses (a multiple root would over-count zeros of `W`), and is independently forced in the forward direction by the charged finite dictionary. Listing it is correct.
4. Section 7's “bridge to the live coefficient/Taylor clients” names surfaces outside the firewall without asserting a theorem about them. The following refusal paragraph is the actual scope line.
5. Characteristic zero is essential and present: `m\neq 0`, `ord(W)=alpha-1`, `a-b\neq 0` in the unequal-degree leading term, `1-U\neq 0`, and `D\neq 0` in `W=-G B'` on the constant-`G` edge.
6. The notation `d(T')^m` is `d\cdot(T')^m`, as in the charged parent. Formula `(0.10)` makes the parsing unambiguous.

None of these remarks changes a numbered verdict.

---

## Strict scope firewall

This review confirms a terminal classification and passport enumerator: on both nontrivial `(8,12)` Kummer leaves, solutions of `d(T')^m=C T^{m-1}` are precisely the balanced extremal abc triples with the displayed fibres, degree box, and gcd condition, and the zero-at-infinity alternative is empty. It does **not**:

- solve `r_1'=\cdots=r_6'=0` or determine the algebraic fibres of those constants;
- produce the remaining Faber coefficient functions, a rational or polynomial trajectory, either original Taylor-boundary family, a strict Rees boundary, or a Keller pair;
- bound `U`, realize an arbitrary passport, or lift a passport to the lower Faber fibre;
- close the order-four client, the order-two client, the cell `(8,12)`, maximum twelve, or JC2.

The target's own Section 7 matches this boundary. No creep was found in any numbered claim.

---

## Terminal boundary (accepted, not enlarged)

```text
wronskian_formula_and_local_orders=PROVED
T(infinity)=0_empty_both_m=2_and_m=4=PROVED
balanced_deg_G_squarefree_deg_W_r+s=U_rad=D+1=PROVED
W=kappa_A_B/(rad(A)rad(B))=PROVED
three_fibres_RH_saturation_degree_box=PROVED
edges_U=2_D=U-1_D=m(U-1)=PROVED
radicand_product_degree_mU=PROVED
kummer_order_m/gcd(m,all_parts)=PROVED
converse_hypotheses_suffice=PROVED
passport_enumerator_at_fixed_U=PROVED
other_six_tails=NOT_SOLVED
Taylor_polynomiality=NOT_CLAIMED
U_bounded=NOT_CLAIMED
any_Kummer_leaf_closed=false
(8,12)_empty=false
maximum_twelve=NOT_CLAIMED
JC2=NOT_CLAIMED
```
