# Hostile review: td12 U1 sibling T1 ratio solve

Date: 2026-08-29
Reviewer: Grok 4.6, different-model expert referee
Charge: sealed Sol 5.6 producer
`xmodel/m2-td12-u1-sibling-t1-ratio-solve-r1-sol56-20260829.md`

No AWS, web, canonical edit, commit, push, or `jc2-lean` access.  Arithmetic
is exact `Fraction` polynomial expansion, not a CAS Gröbner run.  The
provisional sibling-charge report was not used as a mathematical source.

## Verdict

**PASS.**

The charged P0 cell is coefficient-compatible with reduced Proposition
8.1(iv).  The printed squared arrival factor in `q` is incompatible with
both the R1.0 valuation and the cell degree.  The Wronskian reduces to a
triangular two-coefficient identity whose only admissible solution is the
stated one-scale template.  After genuine gauges the quotient is a single
unordered ratio point.  T1 does not kill the sibling.

| # | Attack | Verdict |
|--:|---|---|
| 1 | Literal `p/q` shapes; printed squared arrival in `q` vs valuation and degree | **CONFIRMED** (display unusable) |
| 2 | Wronskian reduction; every factor `17` and `13`; every division | **CONFIRMED** |
| 3 | Independent solve: `B+C=9A/4`, `BC=45A^2/32`, `B/A=(9±3i)/8` | **CONFIRMED** |
| 4 | Distinctness, nonzero roots, noncollision with `A`, nonzero RHS, degree/gcd, P0 side conditions | **CONFIRMED** |
| 5 | Gauge quotient: common dilation vs translation; ordered vs unordered ratios; no surviving continuous modulus | **CONFIRMED** |
| 6 | Logical independence from the provisional sibling-charge report; maximum safe downstream interface | **CONFIRMED** |

This review licenses no tree-occurrence, source-child pass, formal germ,
polynomial Keller pair, `td=12` panel decision, or JC2 conclusion.

---

## 0. Custody

Charged producer, SHA-256 recomputed on this host before reading:

```text
9a9e948cafbea9fa448b84435c0ce004dec92903ba56984759353bf6a8d132bc  xmodel/m2-td12-u1-sibling-t1-ratio-solve-r1-sol56-20260829.md
```

Producer body SHA-256 (bytes before that file’s seal heading, length
`11879`) recomputed after reading:

```text
d505e3668a9c2152762e8beb7101e12a52db48c4c1d110ab55fcac2b383892ba
```

Both match the prompt pins.

Cited local files actually read, SHA-256 recomputed after reading:

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77  ladder/BOOK-OFFAXIS.md
2d71e31116c6b4ff3dd7a5188d0dc923ed162e07c1f9156f68f45b5abbfcc0da  ladder/BOOK-OFFAXIS-REVIEW.md
e766bfe27ac9a06ef6eab053dbea666f8b3d3e70a48ee8c76b88e45246c3bea9  cases/l1_ode_check.py
599e2a9123194c580b89b822f5b7a218fa5e9735b16bcb744e0f0e4231584271  xmodel/m2-td12-u1-trunk-consumer-primary-grok46-20260829.md
91b36515950f038d08a444df16f9c09ee9763adb7950d46e9c50e43451f25c0f  xmodel/m2-td12-u1-trunk-consumer-hostile-review-opus5-20260829.md
```

Printed source: Proposition 8.1(i)–(v) and Statement 8.2 (pp. 39–41);
Statement 9.6 case (II) displays (pp. 51–53).  BOOK: R1.0, the reviewed
replacement of R1.3 by P0, and the 2026-08-29 resolvent correction (not
used in the ODE).  The trunk consumer is used only as an independent
carrier of the sibling discrete data `(nu,k,l,eps,lex)=(17,2,2,0,0)` and
the parent reduced state `(w,M)=(9/2,2)`.  The sibling-charge file listed
in the producer’s custody block was not opened for any theorem.

Scope fence.  Charge `4+4`, budget saturation, source-child gates, landing,
gluing to a merge radical, and existence of a configuration are out of
charge.

Notation.  The P0 pattern polynomials are the T1 unknowns, of `η`-degrees
`(dp,dq)`, as in reviewed R1.0 / `l1_ode_check.py` / the `(7,5)` and
`(75,51)` ODE realisations.  Derivatives are in `η` unless a subscript
`t` is written.  `t=η^17`.

---

## 1. Attack 1 — literal shapes; squared `q` is unusable

### 1.1 Charged tuple, reconstructed from P0, not from charge theorems

P0, for a chain vertex of arrival multiplicity `l` with `eps` a northeast
zero-root, `k` simple northeast orbits, and `lex` extra simple `q`-only
orbits, gives

```text
p = α η^eps (η^ν−A)^l Π_j (η^ν−d_j)^{m_j},
q = β η · (each distinct nonzero p-orbit once) · (lex extras),
```

`α,β ≠ 0`, with the strict NE laws `m_j dq < dp < l dq` and `E := l dq − dp > 0`.
Reviewed R1.0 (BOOK-OFFAXIS-REVIEW Front 1, re-derived from Prop. 8.1(iv)
on pp. 40–41) forces every `p`-root to be a simple `q`-root, every other
`q`-root simple, and `η ‖ q` for `ν ≥ 2`.

The charged discrete data are `ν=17`, `l=2`, `k=2`, `Sm=1+1=2`, `eps=0`,
`lex=0`.  The only integer partition of `Sm=2` into `k=2` positive
multiplicities compatible with `m_j < dp/dq < 2` is `m_j=1,1`.  Hence the
only source-typed shapes are, up to `α,β`,

```text
p(η) = (t−A)^2 (t−B)(t−C),
q(η) = η (t−A)(t−B)(t−C).
```

Degrees, with no interpretation:

```text
deg p = 17(2+1+1) = 68,
deg q = 1+17(1+1+1) = 52.
```

The remaining P0 arithmetic of the charged cell, reconstructed from the
parent reduced state `(w_G,M_G)=(9/2,2)` and `l | M_G`, is

```text
E = 2·52−68 = 36 > 0,
kbar = 2·(9/2)·52/36 = 13,
X    = 13·68/52 = 17,
w    = 2·(9/2)·51/(17·36) = 3/4,
M    = gcd(68,52) = 4,
gcd(4,17) = 1,
52 < 68 < 104.
```

This matches the producer tuple
`(ν,dp,dq,E,kbar,X,l,k,Sm,eps,lex)=(17,68,52,36,13,17,2,2,2,0,0)`.
The Wronskian ratio below uses only `dp:dq = 68:52 = 17:13`; parent `w`
is not an extra ODE input.

Root-mult law: `68 ≠ 1·52` and `68 ≠ 2·52`.  Searrow of the arrival:
`2·52 > 68`.  Northeast of each extra: `1·52 < 68`.  N1 / R1.0:
`gcd(M,ν)=1`.

### 1.2 Printed Statement 9.6(II)(a) `q`-display

On printed p. 52 the case-(II)(a) display is

```text
p(η) = (η^ν−c^ν)^2 Π_{i=1}^k (η^ν−c_i^ν),
q(η) = η (η^ν−c^ν)^2 Π_{i=1}^{k+1} (η^ν−c_i^ν).
```

The squared arrival factor in `q` is a thesis defect, independently of this
cell:

- R1.0 valuation at a `p`-root of multiplicity `μ★ ≥ 1`: `v(q)=0` gives
  LHS-`v = μ★−1 < μ★`; `v(q) ≥ 2` gives LHS-`v ≥ μ★+1` (cancellation only
  raises `v`); both contradict RHS-`v = μ★`.  So `v(q)=1` exactly.  A
  squared factor at the arrival orbit is forbidden.
- On this cell, replacing the arrival radical in `q` by its square and
  keeping the two simple NE orbits produces `deg q = 1+17(2+1+1) = 69`,
  not `52`.

The printed Diophantine on the same page uses `dq = (k+1)ν+1` (the radical
degree), so the thesis is internally inconsistent between display and
degree.  The controlling `q`-shape is BOOK R1.0 / P0: retain multiplicity
two in `p`, replace every `p`-orbit in `q` by its radical, retain the
forced simple `η`, and add no `lex` extras.  That repair is load-bearing
for T1.  The same typo was already recorded for case (II)(b) in
BOOK-OFFAXIS-REVIEW §3b; the valuation does not distinguish (a) from (b).

`A,B,C` are orbit values of `t=η^17`, not 51 raw `η`-roots.

---

## 2. Attack 2 — Wronskian reduction, every `17` and `13`

Proposition 8.1(iv), printed p. 40, is

```text
δ p q' − (1−u) p' q = ⊖ p,     ⊖ ≠ 0.
```

Top-degree cancellation (Statement 8.2’s proof, p. 41) forces
`δ/(1−u) = dp/dq = 68/52 = 17/13`.  Clearing the denominator gives the
integer form

```text
17 p q' − 13 p' q = Θ p,     Θ ≠ 0.                 (2.1)
```

The coefficient `17` here is the reduced numerator of `dp:dq` (equally
`X`, which happens to equal `ν` on this cell).  The coefficient `13` is
the reduced denominator (equally `kbar`).  These are not a priori the
chain-rule factor `ν`; that identification is checked below and happens
to be numerically degenerate on this cell.

Work with unit-leading representatives `p_0=(t−A)r`, `q_0=η r`,
`r=(t−A)(t−B)(t−C)`, absorbing `α,β` into `Θ`.  Chain rule in `η`, with
`t=η^17`:

```text
q_0' = r + 17 t r',                 (the 17 is ν)
p_0' = 17 η^{16} p_{0,t},           (the 17 is ν)
p_0' q_0 = 17 t p_{0,t} r.
```

Substitute into (2.1) and divide by the nonzero polynomial `p_0`
(equivalence on a Zariski-open, hence as polynomials):

```text
17 (r + 17 t r') − 13 · 17 t (p_{0,t}/p_0) r = Θ/β.
```

The outer `17` is the Wronskian numerator `X`.  Divide by that `17 ≠ 0`:

```text
r + 17 t r' − 13 t (p_{0,t}/p_0) r = χ,     χ := Θ/(17 β) ≠ 0.
```

The remaining `17` in `17 t r'` is `ν`, from `q_0'`.  The `13` is `kbar`.
Now `p_0=(t−A)r`, so `p_{0,t}/p_0 = 1/(t−A) + r'/r`, and

```text
r + (17−13) t r' − 13 t r/(t−A) = χ,
r + 4 t r' − 13 t r/(t−A) = χ.
```

The `4` is `ν − kbar`, not an unidentified `X − kbar`.  On this cell
`X=ν=17`, so the two readings are numerically identical; they are not
logically identical.  The reduction uses `ν` in the chain rule and `X:kbar`
in the Wronskian, and both are `17:13` here.

Finally `r=(t−A)s` with `s=(t−B)(t−C)`:

```text
(t−A)s + 4 t (s + (t−A) s') − 13 t s = χ,
4 t (t−A) s' − (8 t + A) s = χ.                     (2.2)
```

No root, degree, or genericity hypothesis cancelled a potentially zero
scalar.  Characteristic zero is used once, to divide by `17`.

Cross-check against the `l1_ode_check.py` family-C dictionary, which the
reviewed trunk T1 also used.  With `ρ = dp/dq = 17/13`, `P=p_0`, `W=r`,

```text
E(t) := ρ P W + ν ρ t P W_t − ν t P_t W
```

is the `t`-form of `ρ p q' − p' q`.  Then (2.1) is `13 E = Θ P`.  The two
normalisations differ by the constant `13` and are equivalent.

---

## 3. Attack 3 — independent coefficient solve

Insert `s=t^2−σ t+π`, `s'=2t−σ` into (2.2).  Independent monomial
expansion in `(A,σ,π)`, with `t^3` cancelling identically:

```text
4 t (t−A) s' − (8 t+A) s
  = (4σ − 9A) t^2 + (5 A σ − 8 π) t − A π.          (3.1)
```

(The `t^0` coefficient is the monomial `−A π`; `t^1` is `5 A σ − 8 π`;
`t^2` is `4σ − 9A`; `t^3` is empty.)  For this to be the constant `χ`,

```text
4σ − 9A = 0,
5 A σ − 8 π = 0,
χ = −A π ≠ 0.
```

Unique solution, `A ≠ 0` already from P0:

```text
σ = 9A/4,     π = 45 A^2/32,     χ = −45 A^3/32.
```

So `B+C=9A/4` and `BC=45 A^2/32`.  The quadratic `z^2−(9A/4)z+45 A^2/32`
has discriminant

```text
(9A/4)^2 − 4·(45 A^2/32) = 81 A^2/16 − 45 A^2/8 = −9 A^2/16,
```

hence over `C`

```text
B = (9+3i)A/8,     C = (9−3i)A/8
```

up to interchange.  The ordered ratios are `B/A=(9±3i)/8`.  The cross
ratio is

```text
B/C = (9+3i)/(9−3i) = (4+3i)/5,
C/B = (4−3i)/5.
```

At gauge `A=1`, `s=t^2−(9/4)t+45/32` and (2.2) evaluates to the constant
polynomial `−45/32`, matching `χ=−Aπ`.

The integer Wronskian constant is `Θ = 17 β χ = −765 β A^3/32 ≠ 0`.
Equivalently, in the family-C normalisation, `E(t) = C_{iv} P` identically
at `A=1` with `C_{iv}=−765/416` and zero remainder, and `13 C_{iv}=−765/32`
recovers `Θ` at `β=1`.  Existence is over `Q` at coefficient level and
over `Q(i)` at root level.

---

## 4. Attack 4 — admissibility

On the solution, with `A ≠ 0`:

1. NE roots distinct: discriminant `−9 A^2/16 ≠ 0`.
2. NE roots nonzero: `BC=45 A^2/32 ≠ 0`.
3. No collision with the arrival: `s(A)=A^2−(9/4)A^2+45 A^2/32=5 A^2/32 ≠ 0`.
4. Zero is not a `p`-root: `p_0(0)=A^2 BC=45 A^4/32 ≠ 0`.  The forced `η`
   in `q` is a simple `q`-only zero, as R1.0 requires at `ν ≥ 2` with
   `eps=0`.
5. RHS is not the homogeneous branch: `χ=−A π ≠ 0`.  Conversely `χ=0`
   forces `A π=0`, contradicting (2) and the nonzero arrival.
6. Degree/gcd data of §1.1 hold on the nose and do not use the ratios.
7. `ρ=17/13` lies strictly between `1` and `2`, so the order-`μ★`
   coefficient of (iv) at each `p`-root is nonzero (R1.0 / Statement 8.2).

All stated P0 side conditions are strict.

---

## 5. Attack 5 — gauges; no continuous modulus

Harmless continuous rescalings of the raw presentation:

- `p ↦ α p` cancels from (2.1) and changes no roots.
- `q ↦ β q` rescales `Θ` by the same factor and changes no roots.
- `η ↦ γ η` sends `t ↦ γ^{17} t`, hence
  `(A,B,C) ↦ λ(A,B,C)` with `λ=γ^{17}`.  Over `C` every `λ ∈ C*` occurs.
  Equations (3.1) are homogeneous of weights `(1,1,2,3)` in
  `(A,σ,π,χ)`.

The deck `γ^{17}=1` fixes `t` and only rescales the displayed `η` in `q`,
already absorbed by `β`.  The remaining symmetry is the discrete swap
`B ↔ C`.

Translation is **not** a gauge.  Sending every `t`-orbit value by `h`
takes `(A,σ,π)` to `(A+h, σ+2h, π + h σ + h^2)`.  The first equation of
the coefficient system acquires residual `4(σ+2h)−9(A+h)=−h`.  Only
`h=0` preserves T1.  This matches the typing: `η=0` is a distinguished
simple `q`-root, so the `t`-chart is not translation-invariant.

After quotienting by genuine gauges the raw cone `A ∈ C*` becomes a
single unordered ratio point, or two ordered points `{B/C, C/B}`.  That
is finite ratios, not a positive-dimensional moduli family.

Two coefficients `(σ,π)` and two independent linear equations, triangular
after the first: no hidden continuous ratio survives inside the shape.

---

## 6. Attack 6 — independence and maximum safe interface

The T1 algebra is a closed problem on the charged tuple
`(ν,dp,dq)=(17,68,52)` with the R1.0/P0 shape of §1.  It does not use:

- charge `4+4`, budget saturation, or any source-gate theorem;
- occurrence of the cell in a complete tree;
- the sibling-charge report, which was not read.

Parent `(w,M)=(9/2,2)` reconstructs `kbar` and `X` but does not enter the
ODE except through `dp:dq`.  A later retraction of the charge packet
would retract the *existence of the charged tuple as a configuration
object*, not this coefficient identity on that tuple.

**Maximum safe downstream interface.**  A conforming campaign execution
may treat the sibling P0 cell as **T1-ALIVE**, with unique rigid
one-scale template

```text
p ∼ (t−A)^2 (t^2 − (9A/4) t + 45 A^2/32),
q ∼ η (t−A)(t^2 − (9A/4) t + 45 A^2/32),
```

`A ∈ C*`, unordered ratio a single point.  The next layer is the two
first-child coefficient vectors and their coupled Keller recurrences,
and only after the provisional charge/source-gate packet clears its own
independent review.  This review does not prove that the cell occurs, that
the top pattern lifts, that either child condition passes, that a formal
germ or polynomial Keller pair exists, or that any `td=12` configuration,
counterexample, or JC2 statement follows.

---

## 7. Mutations / negative controls

Executed as exact residual polynomials, not as prose.

1. **Printed squared arrival in `q`.**  `W=(t−A)^2 s = P`.  Family-C `E(t)`
   has degree `8` and is not a constant times `P`.  Separately,
   `deg q=69 ≠ 52` and `v_A(q)=2 ≠ 1`.
2. **Omit `η`.**  `deg q=51 ≠ 52`, and `e_0=0` makes the order-zero term of
   (iv) vanish against `⊖ p(0) ≠ 0` (R1.0, `ν ≥ 2`).
3. **Shift `σ`.**  At `A=1`, `σ=9/4+1`, `π=45/32`, (2.2) becomes
   `4 t^2 + 5 t − 45/32`, not a constant.  The `t^2` residual is exactly
   `4σ−9A=4`.
4. **Shift `π` after fixing `σ`.**  At `A=1`, `π=45/32+1`, residual
   `−8 t − 77/32`.  The `t` residual is `5Aσ−8π=−8`.
5. **Translation `h=1` of all three orbit values.**  Residual contains
   `t^2` coefficient `−1`, matching `−h` from §5.
6. **Wrong Wronskian ratio `ρ=1` (using `ν` in both slots, dropping
   `kbar`).**  Family-C `E` has degree `7`, not a constant times `P`.
7. **Coincident NE roots, zero NE root, arrival collision, `A=0`.**  Each
   makes one of discriminant, `π`, `s(A)`, or `χ` vanish, and is excluded
   by §4.

These kill the standard false positives: uncorrected printed `q`, a
translation modulus, a hidden ratio, a homogeneous `Θ=0` solution, and a
mis-identified `17`.

---

## 8. What is not licensed

- Occurrence of the cell in an actual configuration, or survival of the
  sibling-charge theorem.
- Twin source-child tests, extra-branch jets, or exact `λ`.
- A numerical relation between `{A,B,C}` and any merge radical.
- A `td=12` panel decision, a cofinal ceiling, or JC2.

*End of sealed report body.*

## Seal (outside the sealed body)

- Body length: `16073` bytes (the complete file before this seal heading,
  including the blank separator after `*End of sealed report body.*`).
- Body SHA-256:
  `438c6054a44b2f8e309929647880dc4a8c505bfc86773a7af17a0222c66bc918`.
