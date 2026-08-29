# Adjudication V2 — delayed-load `A` review versus the higher-jet countercertificate

| Field | Value |
|---|---|
| Prior review | `xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-hostile-review-grok-20260826.md` |
| Prior-review SHA-256 | `0dca581aa2b2e65b964b701695b094c93a2197789e95757066c0b0384e366e4c` |
| Prior-review token | `CONFIRMED` (not used as evidence) |
| Producer | `xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-20260826.md` |
| Producer SHA-256 | `9419c08b4be09fee8ecae9b73c8c9c610770a7166e17a973251312d28b69a695` |
| Countercertificate | `RESULT.md` + `EVIDENCE.sha256` + independent audit, hashes below |
| Overall verdict | **PRIOR_REVIEW_REPAIR** |
| Smallest failing claim | correction-completeness of the `r=0` source exclusion: leading `e0=0` plus the cubic `A5` unit do not freeze the delayed-load arc |
| Smallest missing hypothesis | the legal even jet `n0=t^4 m0+...` with `m0=v x/2`, and the remaining unloaded/source grades through `sigma^57` |
| Reviewer / model | Grok 4.6 (xAI). Independent hand expansion of the assigned `t^7` residue. No producer, review, audit, or AWS status line is algebraic evidence |
| Method | SHA-256 of every charged pin; independent binomial expansion of `(3/8) E^2/Q` on `r=0`; inverse-root conversion of the first two negative `z`-coefficients; independent substitution of the charged `A1,A3,A5`. No Singular, Sage, SymPy, msolve, Lean, or other CAS |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the prior review is
`0dca581aa2b2e65b964b701695b094c93a2197789e95757066c0b0384e366e4c`.
Independently recomputed SHA-256 of the producer is
`9419c08b4be09fee8ecae9b73c8c9c610770a7166e17a973251312d28b69a695`.
Both match the assignment pins. The three countercertificate hashes match
below. Characteristic 65521 is a software control and is not used. No file
other than this report was written.

---

## Verdict

**PRIOR_REVIEW_REPAIR.**

The prior review's displayed identities survive: delayed-load timing, the
primitive tie `3 v(t)=5 v(Lambda)`, the first-normal UFD split, the
normalized no-further-correction cubics `A3=5 x^3 D/128` on `D(r)` and
`A5=5 x^3 p^3/1024` on `r=0`, and the squarefree rational-witness rows
`R2=3/3200`, `R6=3/6400`. Its `CONFIRMED` of a primitive unit-`J` source
exclusion does not survive.

On `r=0` the leading cubic null vector produces no unloaded quadratic, but
a source arc need not stop there. Independent expansion of the next mixed
receiver gives

```text
[t^7 z^{-1}](3/8 E^2/Q) = (3/4) v m0 - (3/8) v^2 x.
```

The even jet `m0=v x/2` cancels this coefficient exactly. Leading `e0=0`
removes only the `t^2` coefficient of `n0`. Parity allows the cancellation
(even coefficient at even order). A DVR/domain argument against
`N^2=0` with `N\neq 0` does not apply: the leading `N3` already satisfies
`Q0 | N3^2` with `N3^2/Q0` a polynomial, and `m0` is a genuine higher
coefficient, not a nilpotent. The charged dual exact ordinary rows are the
same identity together with its unitriangular companions, and they vanish
on the same jet. Those rows therefore contradict the prior review's claim
that, after `e0=e2=0` and `u=(p/2)v`, the normalized `A5` unit may be
imposed as a delayed-load source obstruction.

The `A5` identity remains correct as a zero-higher-correction initial form.
It is not a source row at grade `t^3` on the delayed ray. Under
`Lambda=sigma^3`, `t=sigma^5` the loaded face is `sigma^42` and the unit-`J`
cubic tie is `sigma^57`; `t^7=sigma^{35}` still precedes both. A later
normalized `A5` unit cannot be imposed without solving the intermediate
source grades.

No complete formal arc through `sigma^57` is exhibited, so the existence
statement is unproved rather than counterexemplified. The prior
`CONFIRMED` must be withdrawn to the narrower theorem of §7.

**PRIOR_REVIEW_REPAIR**

---

## Hashes

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-hostile-review-grok-20260826.md` | `0dca581aa2b2e65b964b701695b094c93a2197789e95757066c0b0384e366e4c` | prior review (matches required pin) |
| `xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-20260826.md` | `9419c08b4be09fee8ecae9b73c8c9c610770a7166e17a973251312d28b69a695` | producer (matches required pin) |
| `cases/max12_812_order2_affine_faber_a_source_early_null_20260826/RESULT.md` | `2ca188fc31a1889ecaba5434d927b691f4569a8e986d5a79779a34925ee0e69a` | charged dual exact rows (matches required pin) |
| `cases/max12_812_order2_affine_faber_a_source_early_null_20260826/EVIDENCE.sha256` | `2db358d86a6a146b23a1a7b635d50761b83611e0493291e2e8540ae25dfaf79e` | charged evidence manifest (matches required pin; every listed file rehashes) |
| `xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-independent-audit-20260826.md` | `dfb1cc84f4fb30c198dc646ba4416b5cc118b9d74cebead302db9b428594e7b8` | charged audit (matches required pin; its `REPAIR` token is not evidence) |
| `xmodel/max12-812-order2-affine-faber-exceptional-cubic-forms-source-ray-triage-20260826.md` | `40b6d15eb23fc85038182146d8f044dee3d37c7c7e6fc4880e0ac3d223297d5f` | charged `A1,A3,A5`; substituted by hand |
| `xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-20260826.md` | `4c9d9cfc58eb4ca2a33c9bf83beb485c15f0796fa36d2ffe4826c3fdeeac374d` | first-normal `Q0\|N^2` and UFD divisor; independently used on the delayed ray |

---

## 1. Independent expansion of `[t^7 z^{-1}](3/8 E^2/Q)` on `r=0`

Work over a field of characteristic zero. On the repeated-root divisor
`r=0` one has `D=p^2/4`, so `p` is a unit on `D(D)`, and

```text
Q0 = z^2 (z^2+p),
N3 = v z (z^2+p).
```

As rational functions, `N3/Q0 = v/z`. In particular

```text
N3^2/Q0 = v^2 (z^2+p)
```

is a polynomial, so the leading unloaded quadratic receiver vanishes
identically. Retain the next jets specified by the assignment:

```text
Q = Q0 + t x z + O(t^2),
E = t^3 N3 + t^4 N4 + O(t^5),
N4 = m3 z^3 + m2 z^2 + m1 z + m0.
```

Then

```text
E^2 = t^6 N3^2 + 2 t^7 N3 N4 + O(t^8),
1/Q = 1/Q0 - t (x z)/Q0^2 + O(t^2).
```

The `O(t^2)` summand of `Q` multiplies `E^2=O(t^6)` into `O(t^8)` and does
not enter grade seven. Collecting `t^7`,

```text
[t^7](E^2/Q) = 2 N3 N4 / Q0 - N3^2 (x z) / Q0^2,
```

hence

```text
[t^7](3/8 E^2/Q)
  = (3/4) N3 N4 / Q0 - (3/8) N3^2 (x z) / Q0^2.
```

The two rational functions collapse by `N3/Q0=v/z`:

```text
N3 N4 / Q0 = v N4 / z,
N3^2 (x z) / Q0^2 = v^2 x / z.
```

Now `N4/z = m3 z^2 + m2 z + m1 + m0/z`. The unique negative term is
`m0/z`. Therefore the `z^{-1}` coefficient is

```text
[t^7 z^{-1}](3/8 E^2/Q) = (3/4) v m0 - (3/8) v^2 x.          (1.1)
```

The coefficients `m1,m2,m3` contribute only non-negative Laurent terms at
this grade. Substituting the even jet

```text
m0 = v x / 2                                                 (1.2)
```

gives `(3/4) v (v x/2) - (3/8) v^2 x = 0`. This is an exact cancellation,
not a modular numerical residual.

If the next normal is omitted (`m0=0`), (1.1) reduces to the monomial-slice
sentinel `-(3/8) v^2 x`. That sentinel is an omission control. It is not a
source obstruction once (1.2) is admitted.

---

## 2. Ordinary companions and the charged dual rows

The change from the first seven negative `z`-coefficients to the first
seven ordinary Faber rows is unitriangular, with `R1=h1`. On the present
rational function the only negative terms at `t^7` are `h1 z^{-1}+h2 z^{-2}`.
In the assignment slice `Q=Q0+t x z+O(t^2)` one has `h2=0`. Vanishing of
(1.1) is therefore vanishing of all seven ordinary rows at this grade.

For comparison with the charged `RESULT.md` rows, enlarge the `t`-jet of
`Q` to `Q1=pp z^2 + x z + rr`. Then

```text
N3^2 Q1 / Q0^2 = v^2 pp + v^2 x / z + v^2 rr / z^2,
```

so the negative part of `[t^7](3/8 E^2/Q)` is

```text
h1 = (3/4) v m0 - (3/8) v^2 x,
h2 = -(3/8) v^2 rr,
```

with `h3=\cdots=h7=0` at this order, and with `pp` purely polynomial. The
monic inverse root of `Q0=z^4+p z^2` (the case `r=0`, `c=0`) is odd,

```text
z(w) = w + a w^{-1} + b w^{-3} + d w^{-5} + O(w^{-7}).
```

Imposing `Q(z(w))=w^4` yields `a=-p/4`, `b=p^2/32`, `d=p^3/128`. Then

```text
1/z = w^{-1} + (p/4) w^{-3} + (p^2/32) w^{-5} - (p^3/128) w^{-7} + O(w^{-9}),
z^{-2} = w^{-2} + (p/2) w^{-4} + (p^2/8) w^{-6} + O(w^{-8}).
```

The `t`-jet of `c` and of `p` multiplies an already `t^7` negative series
into `O(t^8)`. Hence at grade seven,

```text
R1 = h1,
R2 = h2,
R3 = (p/4) R1,
R4 = (p/2) R2,
R5 = (p^2/32) R1,
R6 = (p^2/8) R2,
R7 = -(p^3/128) R1.                                          (2.1)
```

These are exactly the dual exact rows displayed in the charged
`RESULT.md`, under the transcription `w0=m0`. They vanish if and only if
`m0=v x/2` and `rr=0`. The moving-`p` coefficient `pp` and `m1,m2,m3` do
not enter. Independently of that display, the assignment slice already
has `rr=0`, so (1.2) alone kills the seven-row coefficient.

The AWS endpoint strings `PASS_A_SOURCE_EARLY_NULL` and
`PASS_CORRECTION_COMPLETE_T7_CANCELLATION_AND_CUBIC_IDENTITIES` are not
used.

---

## 3. Legality of `m0=v x/2` after leading `e0=0`

The normalized `A`-face weights write `n0=t^2 e0` with `e0` a closed-point
coordinate. The first-normal theorem on `r=0` forces every
degree-at-most-two leading normal to vanish, hence the leading identity
`e0=0`. That identity is the coefficient of `t^2` in `n0`. It does not
constrain the series

```text
n0 = t^4 m0 + O(t^6),
```

equivalently `e0(t)=t^2 m0+...`. Equation (1.2) is precisely such a
higher coefficient. The first quadratic receiver, at `t^6`, never sees it.

**Parity.** The source involution `z\mapsto -z` requires even octic and
normal coefficients at even orders of `t`, and odd coefficients at odd
orders. The direction `n0` is even. Grade `t^4` is even. Therefore `m0` is
parity-allowed. The prior review's parity remark — even normals at odd
orders break the involution — is the opposite selection rule and does not
forbid (1.2). The same rule *does* forbid an order-`t` jet of the even
coordinates `p` and `r`; in particular `rr` at order `t` is already
illegal, so the `R2` factor `-(3/8) v^2 rr` is killed by parity before it
is killed by the row. Odd coefficients `m1,m3` at even order `t^4` are
likewise illegal; they were never needed for (1.1).

**DVR / domain.** Formal arcs have domains as value rings, so
`N^2=0` forces `N=0`. That statement is true and irrelevant. Here
`N3^2 = Q0\cdot v^2(z^2+p)\neq 0`, and `Q0` divides `N3^2` in the
polynomial ring. The coefficient `m0` deforms a nonzero null vector; it is
not a nilpotent. Localization on `D(x p)` likewise cannot absorb a unit
*after* a correction-complete solve; it cannot be invoked to skip the
solve.

Thus (1.2) is a legal source jet after the leading normalized coordinate
`e0=0`. Neither parity nor a DVR forbids it.

---

## 4. The normalized `A5` unit is not yet a source row

Under the primitive ramification `Lambda=sigma^3`, `t=sigma^5` forced by a
unit source `J` against a cubic normalized terminal,

```text
leading odd normal t^3:     sigma^{15},
next k[[t]] even jet t^4:   sigma^{20},
mixed receiver t^7:         sigma^{35},
delayed loads Lambda^{14}:  sigma^{42},
unit-J cubic tie:           sigma^{57}.
```

The charged forms `A1,A3,A5,J3` are the `t^3` initial forms of the
normalized ordinary-Faber system in which the three loads are already at
leading scale. On the delayed ray those forms occur only after the
unloaded predecessor tower and after the grade-forty-two loaded face.
Equation `(3.10)` of the producer, namely `A5=5 x^3 p^3/1024`, is an
identity in the normalized cubic initial form with every unprinted higher
jet set to zero. It may be tested against a source row only after every
earlier contribution to that row has been recursively cleared or uniquely
eliminated.

The prior review's implication

```text
quadratic UFD null + e0=e2=0 + u=(p/2)v
  + substitution of charged A5
  => no literal primitive source cubic
```

therefore skips the correction tower. A later normalized `A5` unit cannot
be imposed without solving the intermediate source grades through
`sigma^{57}`.

Products of intermediate jets can still tie later unloaded grades (`t^8`
is `sigma^{40}`, still before the loaded face). The UFD condition on the
*first* normal coefficient does not set those later coefficients to zero.
This adjudication does not classify that recursion; it only records that
the recursion is mandatory and that its first positive/negative pair is
(1.1)--(1.2).

---

## 5. Dual exact rows versus the prior correction-completeness claim

The prior review's concrete exclusion on `r=0` is the paragraph that, after
the divisor constraint, `A1` and `A3` solve `v=-x^3/(5 p^2)` and
`g=45 x^2 p/128 + 3 b p^2/8`, every `b` term cancels in `A5`, and the
residual is the unit `5 x^3 p^3/1024`. Its omissions section then asserts
that earlier normals, even-at-odd-order parity, and DVR nilpotents do not
cancel that unit, and that there is no formal arc through the cubic grade.

The charged dual rows (2.1) are the first post-null unloaded coefficient.
They are cancelled by a jet that the leading coordinate `e0=0` does not
remove, that parity permits, and that the DVR remark does not address.
That is a direct contradiction of the completeness claim: the argument
that was used to pass from the UFD null vector to the loaded cubic
residual is missing a legal source variable already at `t^7`.

The contradiction is to the *argument*, not to the existence statement by
counterexample. No arc through `sigma^{57}` is produced. The squarefree
direct rejection in the prior review's §5 is unaffected, because that
witness has `Q0=z^4-1` squarefree and a nonzero first normal at
`Lambda^{10}`, before any later jet can enter.

---

## 6. Surviving exact identities

The following identities were re-derived by hand and still stand.

**Delayed-load timing.** The graph `k10=Lambda^{12} K10`,
`k6=Lambda^8 K6`, `k2=Lambda^4 K2` places every effective lower load at
`Lambda^{14}`. On an exact square the unloaded `F12` tail vanishes, so the
grade-fourteen face is the ordinary affine-`mu2` system, with later
targets at relative orders two, four, and five. The graph ring is a
domain. The chart `K10=1` is a chart of `D(K10)`, not a weighted Kummer
normalization and not a fan-exhaustion theorem.

**Primitive terminal tie.** A unit source `J` against a cubic normalized
terminal forces `3 v(t)=5 v(Lambda)`, primitively `Lambda=sigma^3`,
`t=sigma^5`.

**First-normal UFD.** For `deg N\le 3`, the first seven tails of
`(3/8) N^2/Q0` vanish if and only if `Q0 | N^2`. On `D(r D)` the quartic
is squarefree, so `N=0`. On `r=0`, `D_{Q0}=z(z^2+p)` and the only cubic
null vector is `N=v z(z^2+p)`, i.e. `u=(p/2)v`.

**Normalized cubics, zero higher jets.** On `D(r)`, after `e0=e2=u=v=0`,
the charged `A1` solves `g=(5/16) x^2 p+(3/2) b D`, and substitution in
`A3` leaves the unit `5 x^3 D/128`. On `r=0`, after `e0=e2=0` and
`u=(p/2)v`,

```text
A1 = -5/32 x^3 p - 3/16 b x p^2 + 1/2 g x + 25/256 p^3 v,
```

and the combinations independent of `g` are

```text
512 (A3 + (p/4) A1) = 5 p^2 (x^3 + 5 p^2 v),
```

hence `v=-x^3/(5 p^2)` on `D(p)`, then
`g=45 x^2 p/128 + 3 b p^2/8`. Every `b` term cancels in `A5`, and

```text
A5 = 5 x^3 p^3 / 1024.
```

Equivalently,
`1024(A5-(p/4)A3+(p^2/32)A1)=5 x^3 p^3` after the same substitutions.
These are compiler-control / initial-form identities. They are not
correction-complete source residues.

**Squarefree rational witness.** At `(D,p,x,v)=(1,0,1,-1/20)` one has
`r=-1`, `Q0=z^4-1`, and `N=-(t^3/20) z^3`. Then

```text
(3/8) N^2/Q0 = (3/3200) t^6 z^6/(z^4-1),
z^6/(z^4-1) = z^2 + z^{-2} + z^{-6} + ...,
```

so `h2=h6=3/3200`. The ordinary connection at `p=0`, `r=-1` gives
`R2=3/3200` and `R6=3/6400`. This is the first nonzero normal grade on a
squarefree quartic; no later correction can cancel it. The specific
natural lift is rejected at `Lambda`-order ten.

---

## 7. Narrowest valid theorem

Work over a field of characteristic zero, on the integral delayed-load
ray, in the centered ordinary-Faber chart, for a primitive unit-`J` cubic
`A` client after `Lambda=sigma^3`, `t=sigma^5`.

1. Before the loaded face, the first square-normal coefficient must
   satisfy `Q0 | N^2`. On `D(r D)` it vanishes. On `r=0`, `D\neq 0` the
   only cubic direction is `N3=v z(z^2+p)`.
2. In the normalized cubic initial form with all unprinted higher normal
   and tangent corrections set to zero, the eliminations `A3=5 x^3 D/128`
   on `D(r)` and `A5=5 x^3 p^3/1024` on `r=0` hold. This is not a literal
   source exclusion.
3. On `r=0`, the first mixed unloaded coefficient is (1.1). The legal
   even jet (1.2) cancels it. Leading `e0=0`, parity, and a DVR do not
   remove that jet. The normalized `A5` unit may not be imposed until the
   source is solved grade by grade through `sigma^{57}`.
4. The frozen squarefree point `(D,p,x,v)=(1,0,1,-1/20)` is rejected by
   its first unloaded rows `R2=3/3200`, `R6=3/6400`.

This is not a total-Rees overlap, an exhaustive load Newton-fan theorem, a
later-`J` theorem, a `K`-face theorem, a `D=0` or `K10=0` theorem, a
terminal/`[6,2]`/Taylor theorem, or an order-two, `(8,12)`, maximum-twelve,
or JC2 result. It does not classify the repeated-root recursion past
`t^7`, and it does not produce a formal source arc.

---

## 8. What the prior review missed

The prior review independently re-derived every identity in §6 and then
treated the leading UFD coordinates as the entire jets of `n0,n2,n3,n1`.
Its omissions section examined *earlier* normals, even coefficients at
*odd* orders, and nilpotents of a leading `N`. The assigned falsifier is a
*later* even jet at *even* order of a nonzero null vector. Those three
omission clauses therefore do not cover (1.2). The step from the UFD null
on `r=0` to the loaded cubic residual is the smallest incomplete inference
in the `CONFIRMED` writeup.

A wording-only repair of that writeup is to replace `CONFIRMED` of a
source exclusion by the initial-form theorem of §7.2, and to record (1.1)
as the first mandatory correction. A source-theorem repair must run the
predecessor through `sigma^{57}` with all four square-normal corrections
and all moving `Q`, load, and target jets retained, emitting a raw
localized unit or a frozen survivor only after that recursion.

---

## Scope

Smallest failing claim of the prior review: correction-completeness of the
`r=0` source exclusion.

Smallest missing hypothesis: the legal jet (1.2), and the remaining source
grades through `sigma^{57}`.

Strongest exact theorem that survives: §7.

This adjudication does not compute the full repeated-root formal
recursion, disprove a normalized `A` arc, exhaust delayed-load rays,
classify the `K` face, impose terminal or Taylor conditions, or close
order two, `(8,12)`, maximum twelve, or JC2.

PRIOR_REVIEW_REPAIR
