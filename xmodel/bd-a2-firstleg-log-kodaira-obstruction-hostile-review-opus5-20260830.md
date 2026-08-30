# Hostile review: `BD-A2-FIRSTLEG` log-Kodaira obstruction

Reviewer: Opus 5 (different-model hostile review)
Date: 2026-08-30 UTC
Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`
Lifecycle: **HOSTILE REVIEW / CONFIRM_WITH_CORRECTIONS / STRENGTHENED TO AN EXACT VALUE**

## 0. Verdict

```text
Overall:  CONFIRM_WITH_CORRECTIONS
```

The abstract theorem is true, its proof is essentially correct, and the
hunted off-by-one in `t^(m-k-1)` is **not present**.  I reconstructed the
result twice by independent routes -- the producer's blowup-chart audit, and
an intersection-theoretic discrepancy computation that never opens a chart --
and they agree exactly, including on every intermediate exceptional order.

The result is in fact stronger than claimed.  The correct statement is an
equality, and `bar-kappa(U)` does not depend on the contact multiplicities at
all:

```text
bar-P_m(U) = m*(#S-2)+1   for #S>=2 and every m>=1,

bar-kappa(U) = -infinity  (#S<=1),
                        0  (#S=2),
                        1  (#S>=3).
```

Corrections required, none fatal:

- **C1 (load-bearing fill-in).**  The local normal form `phi=w/(w-a(t))`
  "up to a base rational function" is used but not justified.  The
  *invariance* direction proved in section 2 is the wrong half.  Without the
  missing half a local unit factor would reintroduce an interior pole along
  the fibre over `s`.  The step is true; the one-line proof is supplied in
  section 3 below.
- **C2 (statement gap).**  The packet never states the conclusion that
  actually discharges the "no hidden interior pole" obligation, namely
  `ord_(F_s)(omega)=m_s-1+ord_s(h)>=0`.  It is implicit in (3.1) only.
- **C3 (attribution).**  Section 1's "Since `B` is smooth, it is a section"
  is right, but the operative hypothesis is *normality* of `B` plus
  finiteness of `D_0->B`; smoothness alone does not give it.
- **C4 (sign, cosmetic).**  Section 5's chart form is `(-1)` times (3.1), not
  "exactly (3.1) with `m=2`", because (5.1) wedges with `dlog` of the
  displacement `= dlog(1/phi)`.  Verified symbolically.
- **C5 (scope of section 5).**  The explicit replay is an *instantiation* of
  the same construction, not an independent check.  A genuinely independent
  confirmation is supplied in section 10 below.

Nothing here promotes `BD-FIX3`, primitivity, or JC2.  A cover-side model is
not a Keller map, and closure of the affine-linear cubic subfamily is
neither primitivity nor JC2.

No exit-price assertion is made in this report, so no `charge_basis` line is
declared.

## 1. Custody, seal, basis, and dependency scope

Basis pinned and matched.

```text
git rev-parse HEAD = 0d7544ebd5cb12def6bac892646010301098be3c
0d7544eb  2026-08-29 18:01:15 -0700  Promote sharp K00 and block-sandwich closures
```

All three charged full-file digests reproduce byte-exactly:

```text
cc836852f92ee0a30dab9bfef3cb37b6f818ea2bb76d125ad95c8eecab44248f  PASS
  xmodel/bd-a2-firstleg-log-kodaira-obstruction-producer-sol56-20260830.md
67e1305ba8dc452af6e120b37e24c102856ac5236d9140ffae9a0446c28261bc  PASS
  xmodel/bd-fix3-affine-linear-residual-control-producer-sol56-20260830.md
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778  PASS
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
```

Seal audit of the producer:

```text
standalone '^<!-- BODY-END -->$' occurrences  = 1  (line 373)
body = head -n 373                            = 11262 bytes   (claimed 11262)  PASS
body SHA-256 = 0238ee718560116ef9672f05de7bad23d75dfefba5d302ce10bfd0f1d1127ef6 PASS
```

The only other occurrence of the token `BODY-END` is at line 377, inside the
seal block, and is not standalone.  No smuggling channel.  Custody: **PASS**.

### 1.1 Exact dependency scope

The **abstract theorem is self-contained**.  It consumes neither input
producer.  I checked this line by line: sections 1--4 use only

```text
B=P^1, an affine-line torsor Y->B under a line bundle,
a closed R with q|R : R -> B minus S an isomorphism, #S>=2,
and dominance of A^2 -> U.
```

`O_(P1)(-3)`, Miranda data, etaleness, quasi-finiteness, `Cl(U)`, units,
`chi_c`, degree of the finite normalization, and redundant boundary sheets
are all genuinely absent from the proof.  Section 0's claim of strength is
accurate, and it is a real strengthening: the coordinator's item 3 supplies
`g1` étale + quasi-finite + dominant, of which only *dominance* is used.

The **application** consumes three things, with these custody states:

```text
AL3-REDUCE  (BD-FIX3 sec 3.1-3.4)   UNREVIEWED at charge time
                                     (Fable 5 review in flight)
coordinator item 4: g1(A^2) subset Y_sm minus R   PROMOTED,
                                     but at ancestor basis 0f7ee003
BD-GAL/BD-D2 filters                 reviewed CONFIRM_WITH_CORRECTIONS,
                                     and NOT used by this proof
```

Custody note: the coordinator packet declares frozen basis
`0f7ee003be45ee40d51d4048897cdacf63821172`, the parent of the review basis.
That is an ancestor, not a mismatch, but the promotion string should be
re-pinned when `BD-FIX3` lands.

**No unreviewed stronger premise is consumed by the theorem.**  The
unreviewed premise `AL3-REDUCE` is consumed only by the *application*
sentence, and the producer marks that "provisionally".  Correct typing.

## 2. The ruled completion and the closure of `R`

### 2.1 Completion: CONFIRMED

An `A^1`-torsor under a line bundle `L` on `B` is Zariski-locally trivial
with transitions `y_i = ell_ij y_j + a_ij`, `(ell_ij)` the cocycle of `L`
and `(a_ij)` a `1`-cocycle in `L` (torsors are classified by `H^1(B,L)`).
These are affine, hence the matrices

```text
[[ell_ij, a_ij],[0,1]]
```

glue a rank-two bundle `E` with `Y = P(E) minus P(sub-line-bundle)`.  So
`qbar:P->B` is a smooth `P^1`-bundle, `D_infinity` is a section fixed by the
transitions, and `Y = P minus D_infinity`.  **CONFIRMED.**

### 2.2 `D_0` is a smooth section: CONFIRMED, with correction C3

I attacked the four listed failure modes.

- *Vertical components.*  `R ≅ P^1 minus S` is irreducible, so its closure
  `D_0` is irreducible.  An irreducible curve dominating `B` has no
  component contracted to a point.  **No vertical component.**
- *Finiteness.*  `D_0 -> B` is proper (`D_0` closed in `P`, `qbar` proper),
  dominant, and all fibres are finite (a `1`-dimensional fibre would be a
  component of `D_0` mapping to a point, contradicting irreducibility plus
  dominance).  Proper + quasi-finite ⟹ **finite**.
- *Singular closure.*  Finite + birational onto a **normal** target forces
  `qbar_*O_(D_0) = O_B`, hence `D_0 -> B` is an isomorphism.  The operative
  hypothesis is normality of `B`, not smoothness (correction C3); smoothness
  implies it, so the conclusion stands.  `D_0` is therefore a section of a
  smooth morphism, hence smooth and embedded, and `D_0 ≅ P^1`.
- *Multiplicity.*  The scheme-theoretic closure of a reduced scheme is
  reduced, and a section is reduced.  No multiplicity issue.

### 2.3 `Supp(D_0 ∩ D_infinity) = S` and `U = P minus (D_0 ∪ D_infinity)`

Over `b ∉ S` the point of `D_0` is the point of `R`, which lies in `Y`, so
`D_0` misses `D_infinity` there.  The stated hypothesis that the closure
meets `D_infinity` precisely over `S` then forces, for `s ∈ S`, that
`D_0 ∩ q^(-1)(s) ⊂ D_infinity`, hence `D_0 ∩ Y = R` and `R` is **closed** in
`Y`.  Therefore

```text
U = Y minus R = P minus (D_0 union D_infinity).           CONFIRMED
```

Worth recording: given `R` closed in `Y`, the collision hypothesis is
*automatic*.  Conversely, given the collision hypothesis, closedness is
automatic.  The hypothesis set is consistent and non-redundant in the sense
that exactly one of the two must be assumed.  There is no third reading in
which `U` and `P minus (D_0 ∪ D_infinity)` differ.

## 3. `D_infinity - D_0 = qbar^*E`, `phi`, and vertical zeros/poles

### 3.1 The class statement: CONFIRMED

For a `P^1`-bundle over a curve, `Pic(P) = Z[D_infinity] ⊕ qbar^*Pic(B)`.
Both sections have fibre degree one, so `D_infinity - D_0` has fibre degree
zero and lies in `qbar^*Pic(B)`.  Pick a divisor `E` in the corresponding
class; then `D_infinity - D_0 + qbar^*E ~ 0` and a rational `phi` with

```text
div(phi) = D_infinity - D_0 + qbar^*E
```

exists.  **CONFIRMED.**  (`B=P^1` is not needed here; only `Pic(B)` acting
by pullback.)

### 3.2 Correction C1: the missing half of the normal-form step

Section 2 proves that multiplying `phi` by `qbar^*g` leaves `omega`
unchanged.  That is invariance.  What sections 3 and 5 actually *use* is the
converse normalization: that near a collision point one may **take**
`phi = w/(w-a(t))` up to `qbar^*` of a base function.  This is not proved,
and it is load-bearing: if `phi` differed from that model by a genuine local
unit `v` with `dv/v = A dt + B dw`, then

```text
qbar^*eta ^ dlog(v) = (h(t)/t)*B * dt ^ dw,
```

which has a **simple pole along the interior fibre `F_s`** whenever
`B(0) != 0`.  Every claim of "no hidden interior pole" would fail.

The step is nevertheless true.  Proof (one line, supplied here):

> Let `V ⊂ B` be open with `D_0|_V` disjoint from the zero section, let `g`
> be a rational function on `V` with `div(g) = E|_V`, and set
> `psi = phi / (qbar^*g · w/(w-a))`.  Then `div(psi) = 0` on `qbar^(-1)(V)`,
> so `psi` and `psi^(-1)` are regular there; restricted to any fibre `P^1_b`
> this is a regular function on `P^1`, hence constant.  So `psi` is
> fibrewise constant, i.e. `psi = qbar^*c` for `c ∈ O(V)^*`.  ∎

Hence `phi = qbar^*(cg) · w/(w-a)` exactly, and by the invariance already
proved, `omega` is computed by the model.  With C1 filled in, **CONFIRMED**.

### 3.3 Vertical zeros and poles: CONFIRMED, with correction C2

At the generic point of any fibre `F_b`, write `phi = (qbar^*t)^n · psi`
with `ord_(F_b)(psi)=0`.  Then

```text
qbar^*eta ^ dlog(phi) = qbar^*eta ^ (n*qbar^*(dt/t)) + qbar^*eta ^ dlog(psi)
                      = 0                             + qbar^*eta ^ dlog(psi),
```

the first term vanishing because both factors are pulled back from a curve.
So the *integer* `n` is genuinely irrelevant, exactly as section 2 says.

But that alone does **not** give `ord_(F_b)(omega) >= 0` when `b ∈ S`,
because `qbar^*eta` already contributes `-1`.  The producer's blanket
sentence in section 2 is therefore true but insufficient, and the packet
never states the fact that closes the obligation.  From (3.1),

```text
ord_(F_s)(omega) = ord_s(h) + (m_s - 1) >= 0     since m_s >= 1.
```

The apparent pole of `eta` is paid for by the collision factor `a(t)`, which
is what the producer means; the inequality itself should be displayed.  For
`b ∉ S`, `eta` is regular and `ord_(F_b)(omega) >= 0` trivially.

Finally, `omega` has **no other** polar divisor: poles of
`qbar^*eta ^ dlog(phi)` are contained in
`Supp(div phi) ∪ qbar^(-1)(poles of eta) = D_0 ∪ D_infinity ∪ (fibres)`, all
of which are now accounted for.  `omega != 0` because `phi` restricted to a
general fibre has its zero and pole at distinct points, hence is nonconstant.

**No hidden interior pole.  CONFIRMED with C1, C2.**

## 4. Existence and dimension of `eta`

`Omega^1_(P^1)(log S) ≅ O_(P^1)(#S - 2)`, so

```text
h^0(P^1, Omega^1(log S)) = max(#S-1, 0).
```

Nonzero **iff** `#S >= 2`.  **CONFIRMED**, including the borderline case:
for `#S = 2` the space is exactly one-dimensional, spanned by `dt/t` for the
coordinate with `S = {0, infinity}`, with nonzero residue at *both* points.
The proof handles `h(s) = 0` (possible only for `#S >= 3`) correctly, since
that only raises `ord_(F_s)(omega)`.

Section 3's "Because `eta` has at most a simple pole at `s`, write
`eta = h(t) dt/t` with `h` regular" is exactly right.

## 5. The tangency formula: no off-by-one

### 5.1 (3.1) is exact

With `eta = h dt/t`, `phi = w/(w-a)`:

```text
dlog(phi) = dw/w - (dw - a' dt)/(w-a),
```

the `a' dt` term dies against `dt`, leaving

```text
omega = -h(t) * (a(t)/t) * dt ^ dw / (w*(w-a(t))).       (3.1)  EXACT
```

Verified symbolically (sympy, seconds-scale): the computed coefficient
`-a(t)h(t)/(t w (w-a(t)))` matches (3.1) identically.

### 5.2 The chart exponent

In the chain chart `w = t^k w_k` one has `dt ^ dw = t^k dt ^ dw_k`,
`w = t^k w_k`, `w - a = t^k(w_k - t^(m-k) u)` with `a = t^m u`, `u(0) != 0`.
Hence

```text
omega = -h u t^(m-1) * t^k / (t^k * t^k) * dt^dw_k / (w_k (w_k - t^(m-k) u))
      = -h u t^(m-k-1) dt ^ dw_k / (w_k (w_k - t^(m-k) u)).
```

Machine-checked for all `1 <= k <= m <= 5`; every case returned exactly
`t^(m-k-1)`.  **The exponent is correct; there is no off-by-one.**

### 5.3 Independent invariant recomputation (no charts)

I redid the whole audit divisorially.  Let `p_1,...,p_m` be the blown-up
points, `E_i` the exceptionals, `rho: P~ -> P` the composite.  Because
`p_(k+1)` lies on `E_k`, on the strict transform of `D_0` (for `k <= m-1`)
and on that of `D_infinity`, but **not** on `E_(k-1)` nor on the strict
transform of `F_s`:

```text
K_(P~) = rho^*K_P + sum_i i * E~_i,
rho^*D_infinity = D~_infinity + sum_i i * E~_i,
rho^*D_0        = D~_0        + sum_i i * E~_i,
rho^*F_s        = F~_s        + sum_i 1 * E~_i.
```

Since `div_P(omega) = (m-1)F_s - D_0 - D_infinity` locally,

```text
ord_(E_i)(rho^*omega) = (m-1)*1 - i - i + i = m - 1 - i,
```

**identical to the chart answer**, obtained without opening a single chart.
Likewise `ord_(F~_s)(omega) = m-1 >= 0`.  Two independent routes agree on
every component.

### 5.4 Resolution is SNC after exactly `m` blowups

At stage `k < m` the strict transforms satisfy `w_k = 0` and
`w_k = t^(m-k)u`, so both still meet `E_k` at the origin: a triple point, so
`k = m` blowups are genuinely needed.  At `k = m` they meet `E_m` at
`w_m = 0` and `w_m = u(0) != 0`, distinct, and `E~_(m-1)` meets `E_m` in the
complementary chart at a third point.  The exceptional locus is a chain
`E~_1 - ... - E~_m` with `D~_0`, `D~_infinity` attached to `E~_m` only.  No
triple points, all components smooth: **`D~` is SNC**.  The producer asserts
the separation but not the absence of exceptional triple points; verified
here.

### 5.5 Pole orders on all components

```text
ord(omega) + [component in D~] >= 0  on:
  D~_0, D~_infinity            :  -1 + 1 = 0     simple log poles      OK
  E~_i, i < m                  :  (m-1-i) + 1 >= 1                     OK
  E~_m                         :  -1 + 1 = 0     simple log pole       OK
  F~_s (NOT in D~)             :  (m-1) + 0 >= 0  no interior pole     OK
  every other prime divisor    :  >= 0                                 OK
```

For a surface with SNC boundary, `Omega^2(log D~) = O(K+D~)`, and
membership in `H^0(O(K+D~))` is exactly the divisorwise condition above --
there is no additional pointwise obligation at crossings.  The audit is
therefore complete.  **CONFIRMED.**

The producer's remark that "the complementary blowup charts give the same
valuation statement" is correct, since a divisorial order is chart-free;
5.3 establishes it without relying on the remark.

## 6. From one section to `bar-kappa(U) >= 0`, and the compactification

`rho` blows up only points of `D_0 ∩ D_infinity ⊂ P minus U`, so `rho` is an
isomorphism over `U` and

```text
P~ minus D~ = rho^(-1)(P minus (D_0 union D_infinity)) = U.
```

`D~` is SNC by 5.4, so `(P~, D~)` is a log-smooth compactification of `U`
and computes `bar-kappa(U)` (independence of the choice is Iitaka's).  A
nonzero `omega ∈ H^0(K_(P~)+D~)` gives `bar-P_1(U) >= 1`, hence
`bar-kappa(U) >= 0`.  **CONFIRMED**, and the compactification does have
exactly `U` as its open part.

### 6.1 The tangency audit is load-bearing (not removable)

A tempting shortcut fails, and it is worth recording why the producer's
blowup work cannot be skipped.  On `P` itself, adjunction on `D_infinity ≅
P^1` and fibre degree `-2+1+1 = 0` give

```text
K_P + D_0 + D_infinity ~ (sum_s m_s - 2) * F,
h^0(K_P + D_0 + D_infinity) = sum_s m_s - 1.
```

But `(P, D_0+D_infinity)` is **not log canonical** at a collision with
`m >= 2` (log discrepancy `1-i < 0` for `i >= 2`), and the resolution
correction is strictly negative:

```text
K_(P~) + D~ = rho^*(K_P + D_0 + D_infinity) - sum_(s,i) (i-1) E~_(s,i).
```

So `h^0` drops from `sum_s m_s - 1` to `#S - 1`.  Most sections on `P` do
**not** survive.  The producer's `omega` survives precisely because of the
`a(t)/t` factor.  A reviewer who replaced the audit by the naive count on
`P` would over-report the plurigenus (in the explicit control, `3` instead
of `1`) and would wrongly conclude the theorem for `#S = 1, m = 2`.

## 7. Logarithmic monotonicity (Lemma 4.1)

Hostile-checked on all four sub-questions; all four pass.

- *Direction.*  `bar-kappa(X) >= bar-kappa(W)` for dominant generically
  finite `X -> W` is the standard consequence of effectivity of the
  logarithmic ramification divisor, and it is standard for **nonproper**
  `f` -- that is precisely the strength of the log invariant.  The producer
  proves the case it needs in-packet, so the citation is decorative.
- *Boundary-only centers.*  `f: X -> W` is a morphism on the interior, so
  the indeterminacy locus of `Xbar --> Wbar` is closed and disjoint from
  `X`, hence contained in `D_X`.  Resolving uses centers in `D_X` only, the
  modification is an isomorphism over `X`, and the reduced total transform
  keeps the complement equal to `X`.  In dimension two, blowing up points of
  an SNC divisor preserves SNC.
- *`fbar^(-1)(D_W) ⊂ D_X` is automatic*, since `f(X) ⊂ W` and
  `D_W ∩ W = ∅`.  Hence locally `fbar^*y_i` has zero divisor supported in
  `D_X`, so `fbar^*y_i = (monomial in the boundary coordinates)·(unit)` and
  `d(fbar^*y_i)/(fbar^*y_i) = sum a_j dx_j/x_j + dv/v` is logarithmic.
  Regular forms pull back to regular forms.  Tensor powers likewise.
  **Pullback of log pluricanonical forms stays logarithmic.**
- *Injectivity.*  Generically finite in characteristic zero ⟹ separable ⟹
  the Jacobian determinant is not identically zero, so
  `fbar^*(g dy_1^...^dy_n) = (fbar^*g)·J·dx_1^...^dx_n != 0` for `g != 0`.

**Lemma 4.1: CONFIRMED as stated and as proved.**

## 8. `bar-kappa(A^2) = -infinity` and generic finiteness

`(P^2, H_infinity)` is log smooth with complement `A^2`;
`K_(P^2)+H_infinity = -3H+H = -2H`, so `h^0(m(K+H)) = h^0(O(-2m)) = 0` for
every `m >= 1` and `bar-kappa(A^2) = -infinity`.  **CONFIRMED.**

A dominant morphism of irreducible surfaces has generic fibre of dimension
`2-2 = 0`, hence is generically finite.  **CONFIRMED.**  The chain

```text
-infinity = bar-kappa(A^2) >= bar-kappa(U) >= 0
```

is therefore a genuine contradiction, and the conclusion upgrades from "no
dominant *generically finite* morphism" to "**no dominant morphism**
`A^2 -> U` at all", which is what section 4 in fact states.

## 9. The explicit control (5.1)

All of section 5 reproduces.  Symbolic replay from the `BD-FIX3` equations:

```text
q0 = 3u lam^2 + 2lam + 1
u_R = -(2lam+1)/(3lam^2),   v_R = -lam(lam+2)/3          matches BD-FIX3
u - u_R = q0/(3 lam^2)                                    displacement OK
w = 1/u on D_0 :  w = -3lam^2/(2lam+1),  ord_lam = 2  ->  m = 2          OK
(5.1) in the w chart:  -3lam dlam^dw / ( w (3lam^2+(2lam+1)w) )
                        == producer's displayed formula                  OK
q0 = -q_infinity/mu, i.e. q_infinity = -lam^(-1) q0       matches BD-FIX3
symmetric chart:  omega = -3mu dmu^dv / q_infinity  ->  m = 2 at infinity OK
interior order:   coefficient 3lam, q0(0,u)=1  =>  ord_(F_0)(omega)=1=m-1 OK
```

Two findings.

- **C4 (sign).**  `(3.1)` with `h=1`, `a = -3lam^2/(2lam+1)` gives
  `+3lam/(w(3lam^2+(2lam+1)w))`; the chart form is its negative.  The ratio
  is exactly `-1`, from `dlog(displacement) = dlog(1/phi) = -dlog(phi)`.
  Immaterial (a nonzero scalar), but "exactly (3.1) with `m=2`" is
  literally false and should read "`-1` times (3.1)".
- **C5 (scope).**  The replay instantiates the same construction, so it
  cannot independently confirm the theorem.  It *is* nonvacuous: `#S = 2`
  and `m = 2` at both collisions are computed from the equations, not
  assumed.  A genuinely independent check is given in section 10.

The independent numbers all interlock.  `rho = [X^3:Y^3]` has Wronskian
`W = P_1P_2' - P_1'P_2 = -3X^2Y^2`, so `Crit(rho) = {0, infinity}` with
multiplicity two each; and independently `(D_0·D_infinity)_s = m_s = 2` at
both, with `sum_s m_s = 4 = deg W = 2·3-2`, the Riemann-Hurwitz degree.  The
identification `m_s = ord_s(W)` is not stated in either packet and is a
useful invariant reformulation: **the collision multiplicities are the
ramification orders of `rho`.**

The redundant-sheet control is correctly kept separate.  Its target
`G_m x A^1 = (P^1)^2 minus (F_0 + F_infinity + H_infinity)` has
`K+D = -H`, so `h^0(m(K+D)) = 0` and `bar-kappa = -infinity`; its source
`(G_m minus {1}) x A^1` also has `bar-kappa = -infinity`.  Lemma 4.1 reads
`-infinity >= -infinity`: consistent, and no challenge to the theorem.
**CONFIRMED.**

## 10. Counterexample hunt: none exists, and `#S >= 2` is sharp

I attacked the abstract theorem by computing `bar-kappa(U)` exactly for
**every** configuration of two sections in **every** ruled surface over
`P^1`, which is the full hypothesis class.

Numerically, `Pic(P) = Z[D_infinity] ⊕ Z[F]` with `Num = Pic`, `K_P·F = -2`,
and adjunction on `D_infinity ≅ P^1` gives `K_P·D_infinity + D_infinity^2 =
-2`.  Hence

```text
(K_P+D_0+D_infinity)·F          = 0,
(K_P+D_0+D_infinity)·D_infinity = -2 + sum_s m_s,
K_P+D_0+D_infinity ~ (sum_s m_s - 2) F.
```

Combining with the discrepancy identity of 6.1 and
`(qbar∘rho)_* O_(P~) = O_(P^1)`, a section of `m(K_(P~)+D~)` is exactly a
divisor `Z_B` on `P^1` of degree `m(sum_s m_s - 2)` with
`ord_s(Z_B) >= m(m_s-1)`.  The residual degree is
`m(sum m_s - 2) - m·sum(m_s - 1) = m(#S-2)`, so

```text
bar-P_m(U) = m*(#S-2) + 1        (#S >= 2),
bar-P_m(U) = 0                   (#S <= 1),
```

giving the exact values quoted in section 0.  Because this is an equality
covering the entire hypothesis class, **no counterexample exists and no
hypothesis is missing.**  In particular `bar-kappa(U)` is independent of
every contact multiplicity `m_s`; the `m`-dependence in `t^(m-k-1)` cancels
exactly against the discrepancy correction, which is the structural reason
the hunted off-by-one could not have existed.

**Sharpness witness (refutes any weakening to `sum_s m_s >= 2`).**  Take
`P = P^1_z x P^1_w`, `D_infinity = {w=0}`, `D_0 = {w = z^2}`.  Then `D_0` is
a section, `D_0 ∩ D_infinity = {(0,0)}` with `m = 2`, `S = {0}`, `#S = 1`,
`sum_s m_s = 2`, and `Y = P minus D_infinity` is a (trivial) affine-line
torsor with `R = D_0 ∩ Y ≅ P^1 minus {0}` mapping isomorphically to
`P^1 minus S`.  Every hypothesis of the theorem holds except `#S >= 2`.
Here `D_0 ≡ H+2F`, so `K_P+D_0+D_infinity ~ 0`, and

```text
K_(P~) + D~ = rho^*(0) - E~_2 = -E~_2,     h^0(-m E~_2) = 0 for all m>=1,
bar-kappa(U) = -infinity.
```

So the conclusion `bar-kappa(U) >= 0` is **false** for `#S = 1` with
`m = 2`.  `#S >= 2` is necessary, not merely convenient, and the borderline
`#S = 2` case is genuinely borderline: `bar-kappa(U) = 0` exactly, with a
one-dimensional log-canonical system for every `m`.

(Honesty note per FALLACY-v2 floor/attainment: this witness refutes the
*inequality* `bar-kappa >= 0` at `#S = 1`.  It does not exhibit a dominant
`A^2 -> U` there; it shows only that the log-Kodaira obstruction goes
silent.)

Cross-check on the explicit control, `#S = 2`, `m_0 = m_infinity = 2`:
`h^0(K_P+D_0+D_infinity) = 3` on `P`, dropping to `#S-1 = 1` after
resolution, the survivor being the unique `Z_B = [0]+[infinity]`.  The
producer's `omega = 3lam dlam^du/q_0` vanishes on `F_0` (the factor `3lam`)
and, in the symmetric chart `-3mu dmu^dv/q_infinity`, on `F_infinity`.  It
is exactly the predicted survivor.  This is the independent confirmation
promised in C5.

## 11. Itemized verdict

```text
 1  hashes / seal / basis / dependency scope           PASS
 2  ruled completion; D_0 a smooth section; U          CONFIRMED  (C3)
 3  D_infinity-D_0 = qbar^*E; phi; vertical poles      CONFIRMED  (C1, C2)
 4  eta exists iff #S>=2; dim = #S-1; #S=2 borderline  CONFIRMED
 5  (3.1) exact; t^(m-k-1) exact; SNC after m blowups;
    no interior pole; NO off-by-one                    CONFIRMED
 6  one section => bar-kappa>=0; compactification = U  CONFIRMED
 7  log monotonicity for nonproper gen. finite maps    CONFIRMED
 8  bar-kappa(A^2) = -infinity; generic finiteness     CONFIRMED
 9  explicit control (5.1)                             CONFIRM_WITH_CORR (C4, C5)
10  counterexample hunt / missing hypothesis           NONE EXISTS; #S>=2 sharp
11  overall                                            CONFIRM_WITH_CORRECTIONS
```

### 11.1 Maximum exact theorem safe to promote

Unconditional, no unreviewed input, stronger than the producer's:

> **Theorem `BD-A2-FIRSTLEG` (exact form).**  Let `qbar:P->P^1` be a
> `P^1`-bundle with a section `D_infinity`, `Y = P minus D_infinity` (the
> general affine-line torsor under a line bundle over `P^1`).  Let
> `R subset Y` be closed with `q|R : R -> P^1 minus S` an isomorphism for a
> finite `S`, let `D_0` be its closure and `m_s = (D_0·D_infinity)_s`, and
> put `U = Y minus R = P minus (D_0 union D_infinity)`.  Then for every
> `m >= 1`
>
> ```text
> bar-P_m(U) = m*(#S-2)+1   if #S>=2,        0   if #S<=1,
> ```
>
> so `bar-kappa(U) = -infinity, 0, 1` according as `#S <= 1`, `#S = 2`,
> `#S >= 3`, independently of all `m_s`.  In particular
> `bar-kappa(U) >= 0` **iff** `#S >= 2`, and in that case there is no
> dominant morphism `A^2_C -> U` (a fortiori none that is étale,
> quasi-finite, or almost surjective).

Conditional, and to be re-typed when its input lands:

> **Application (conditional on `AL3-REDUCE`).**  For an affine-linear
> Miranda cubic block with no common coefficient zero, `W != 0`,
> `S_X = empty` and irreducible `R`, the residual `U = Y minus R` has
> `S = Crit(rho)` with `#S >= 2` by Riemann-Hurwitz in degree three, so
> `bar-kappa(U) = min(#Crit(rho)-2, 1) >= 0` and no first leg `A^2 -> U`
> exists.  Combined with `AL3-REDUCE` this closes the affine-linear cubic
> subfamily.  `AL3-REDUCE` is **not yet reviewed**; until it is, the
> subfamily closure stays typed `CONDITIONAL`, not `EXCLUDED`.

The verified sharp value on the explicit control is `bar-kappa(U) = 0`
(`#S = 2`, `m_0 = m_infinity = 2`), i.e. the borderline case, exactly as the
producer says.

### 11.2 Cheapest successor if the affine-linear cubic family closes

In priority order.

1. **Land `AL3-REDUCE`.**  It is the sole unreviewed link in the closure
   chain, and specifically its sections 3.3 (reducible `R` excluded via
   `Cl(Y)=Z`) and 3.4 (`R ≅ P^1 minus Crit(rho)`, inconsistency at critical
   directions).  If 3.4's inconsistency claim fails, `R` acquires a vertical
   component and `BD-A2-FIRSTLEG` does not apply at all -- that is the one
   place where a defect upstream silently voids this theorem.  Nothing else
   here is at risk.
2. **`BD-A2-FIRSTLEG-MULTI`: drop "section" to "multisection."**  This is
   the cheap desk generalization and is the shape the nonlinear case will
   need.  If `D_0·F = k >= 2` then `(K_P+D_0+D_infinity)·F = k-1 >= 1`, so
   the class has *positive* fibre degree before resolution -- the log
   positivity is a priori stronger, and the only work is bounding the
   discrepancy loss from resolving singularities of `D_0` and its tangencies
   with `D_infinity`.  Same machine, one new estimate.
3. **`BD-A2-FIRSTLEG-DEG`: raise the Miranda coefficient degree.**  For
   degree-`d` coefficients the fibre of `Y -> P^1_[X:Y]` is the affine plane
   curve `{Phi(u,v;X,Y)=0}`, so `q` becomes a family of degree-`d` affine
   plane curves rather than a torsor.  For `d = 2` this is a conic bundle
   over `P^1`, `Pic` is still rank two plus components, and the same
   `qbar^*eta ^ dlog(phi)` construction and the same
   `K+D~ = rho^*(K+D) - sum(i-1)E~` bookkeeping apply verbatim.  That is the
   first honest step toward removing the affine-linear hypothesis.
4. Record for reuse: `m_s = ord_s(W)`, `W = P_1P_2' - P_1'P_2`.  This turns
   the collision data into Wronskian data and makes `sum_s m_s = 2 deg rho -
   2` and `#S = #Crit(rho)` immediate for any degree.

## 12. Execution disclosure and nonclaims

Executed in a shell session at basis `0d7544eb`.  I ran: `git log -1`,
`git rev-parse HEAD`, `shasum`, `wc`, `grep`, `sed`, and two seconds-scale
`sympy` scripts in `/tmp` (verification of (3.1), of the exponent
`t^(m-k-1)` for `1<=k<=m<=5`, and of the section-5 chart transforms).  No
Singular, no heavy local CAS, no AWS, no formalization tree, no web access.
No unscoped `git status`; `jc2-lean` was not inspected, listed, searched,
stat-ed, built, modified, or controlled in any way.  No canonical file,
script, dependency, or producer was edited.  This report is the only file
written.

This review promotes no statement about a cubic block outside the
affine-linear reduction, no primitivity theorem, and no form of JC2.  A
cover-side model is not a Keller map, and closure of the affine-linear cubic
subfamily is neither primitivity nor JC2.

<!-- BODY-END -->
