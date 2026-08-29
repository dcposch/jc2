# AS109 `n=6` top two `y`-bands — face isolation

Date: 2026-08-27T10:51Z  
Attacker: Grok 4.6 (xAI), desk-scale exact algebra  
Repo HEAD: `418e413593120d19e15e6546eb50c985f4b1f038`  
Python: 3.14.6, stdlib only (`math.gcd`, integer sparse dicts)  
AWS / Singular / CAS / web / `jc2-lean`: none  

**Verdict: `TWO_BANDS_TAUTOLOGICAL`.**

The top two `y`-degree bands of `det J(P,Q)=1` produce **no new exact
integral constraint** on the promoted residual `n=6` leading data beyond
the already-composed common-core / divisibility conditions.  Card F3
therefore **stops**.  The proposed W2/W3 gauge-conductor is a
bounded-category history duplicate of the reviewed polar-conductor and
wild-symplectic gates, and is **not** an unrestricted-state successor.

---

## 0. Charged question and one-line answer

Let `R=Z_109`, `K=Q_109`, and let

```text
P = x - x^{109} + 109 A,     Q = y + 109 B
```

lie in `R[x,y]` with `det J(P,Q)=1`.  Conditionally on this being an exact
integral polynomial AS109 lift, the reviewed one-sided floor-six composition
forces the first residual corner

```text
n = deg_y Q = 6,
m = deg_y P >= 12,     3 | m,
6 | deg_x(q_6),
d = gcd(m,6) in {3,6},
p_m = alpha h^{m/d},   q_6 = beta h^{6/d},
d=3 => 3|H,            d=6 => 6|H,          H = deg_x h.
```

Fable5 Card F3 asked whether the coefficients of `y^{m+5}` and `y^{m+4}`
in `J:=P_x Q_y - P_y Q_x`, together with 109-adic / Kummer-carry
bookkeeping, yield any further exact constraint.

They do not.  Band one is the already-derived leading Wronskian, and is
identically zero on the common core.  Band two is a first-order linear
relation among the *next* coefficients `p_{m-1}, q_5`; every summand has
`v_{109}>=2`, so reductions modulo `109` and `109^2` are `0=0`; after
dividing by the universal `109^2` the remaining ODE is underdetermined in
the leadings and is occupied by both a determinant-one automorphism and a
zero-Jacobian common-power family.  The only degree consequences of the
localized mismatch branch restate `3|H` or `6|H`, already promoted.

---

## 1. History checksum

Load-bearing files reread in full before any identity was written.  SHA-256
recomputed on the charged tree:

| Artifact | SHA-256 |
|---|---|
| `xmodel/as109-one-sided-prime4-composition-sol-20260827.md` | `3d6d09fd1c9d1548dc6af78221f74c83276eb89378ee06cecac5fd19b46fcb36` |
| `xmodel/as109-one-sided-prime4-composition-hostile-review-grok-20260827.md` | `bc13662108e6521ed2ea63a4840b13fd14e0e0b3a6e939caffefea6097958bea` |
| `xmodel/as109-partial-y-history-stop-20260824.md` | `6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe` |
| `xmodel/as109-partial-y-history-review-grok-20260824.md` | `f9d547f0f17dc3557ed8edce19912b4930dc2125542c7f9b3e4782c554a03afd` |
| `xmodel/ideation-20260827T0935Z-fable5.md` (Card F3) | `098b81d19cba6f278e93a809e60a3a4892eea7979758ffe6b0bb2997163b98c0` |
| `xmodel/ideation-20260827T0935Z-grok-crossreview.md` (§7.2 / Card 4) | `e74ade19a9be1b31c476668da44665564f5c2ad84b8a3b700e9d1c6ac19bd490` |

History / comparison inputs, read for novelty and successor custody only:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/as109-sextic-frontier-preflight-20260824.md` | `bbe95d911077baa1c32fedc062807ce754c68ddd58c26a4b209d56333678f9a4` | already-derived `n=6` top row; `(4,6)`/`(5,6)` second rows |
| `xmodel/as109-sextic-preflight-review-grok-20260824.md` | `5bf1a677a59975defb33a58da74d7c7c1381535d84f91e7f1584d21624a385ff` | confirmed general `n=6` top identity `(1.1)` |
| `xmodel/as109-bounded-polar-conductor-gate-20260824.md` | `2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b` | W2/W3 duplicate test |
| `xmodel/as109-bounded-polar-conductor-review-grok-20260824.md` | `bda4dda7d24d36bf75b6c55b566f708ee300c80aeb3344c4bb724bfc7e7787fa` | `CONFIRMED` polar conductor |
| `xmodel/as109-wild-symplectic-conductor-gate-20260824.md` | `c7ad3660c136bbee7105e786cc8b717d025534b67ac63cababb33c4b6de29e7c` | W1 gauge-trivial / unique analytic orbit |
| `xmodel/as109-wild-symplectic-conductor-review-grok-20260824.md` | `a59c7ccbf39971ad7ab47f8e865926c93e4ac9d46305be076f4bd0193b2b1a9a` | `CONFIRMED` wild gate |
| `xmodel/ideation-20260827T0935Z-sol.md` (Card 3) | `98a494a561f39cfef770eec11c07eca3e17e4e9fac61a1a3d143f614d991b90c` | proposed W2/W3 gauge-conductor |

No canonical ledger, producer, freeze, or case file was edited.  This file
is the only write.

---

## 2. History search: genuine novelty versus already-derived bands

Write `P=sum_{i=0}^m p_i(x) y^i` and `Q=sum_{j=0}^n q_j(x) y^j`.  A pair of
terms `(p_i y^i, q_j y^j)` contributes

```text
(j p_i' q_j - i p_i q_j') y^{i+j-1}
```

to `J`.  Lower `y`-coefficients cannot produce a given top degree.

Already in the record:

1. **General top band**, history-stop (1.1):  
   `n p_m' q_n - m p_m q_n' = 0`.  UFD (1.2) is the common core.
2. **General `n=6` top band**, sextic-preflight review (1.1):  
   `6 a_m' b_6 - m a_m b_6' = 0`.  This is exactly the charged
   `y^{m+5}` row, for arbitrary `m`.  Not new.
3. **Specific second bands**, not the residual corner:  
   - `(4,6)`: `[y^8]J = H(2H N'-5 N H')`, `N^2=kappa H^5`;  
   - `(5,6)`: `[y^9]J = h^{10}(6(a_4/h^4)'-5(b_5/h^5)')`;  
   - `(6,9)`: `[y^{13}]J = 8 a'd + 9 c'b - 6 a d' - 5 c b'`, every term
     already `0` modulo `109^2`, with an explicit zero-Jacobian control.  
   All three are first-nontop rows of the same shape as (3.2) below.
4. **Bounded `y<=6` and the pairs `(4,6)`, `(5,6)`** are classical by the
   history-stop source-shear / target-reduction coverage.  They are
   alternative proofs, not first exclusions, and they do not treat
   `m>=12`.
5. **No prior report writes the residual `(m,6)` second band** for
   `m>=12`, `d in {3,6}`, with 109-adic contents, unequal `alpha,beta`,
   zero next coefficients, and the `(12,6)` automorphism control all in
   one place.

What is new in this file is the residual-corner bookkeeping, not the
shape of either identity.  Band one is a history duplicate as an
*equation*.  Band two is new as a written `(m,6)` residual identity and
is tautological as a *constraint on the promoted leadings*.

---

## 3. Coefficientwise derivation of the two charged bands

Fix `n=6` and `m>=12`.  The identity `J=1` in `R[x,y]` forces
`[y^k]J=0` for every `k>=1`; the unit `1` lives only in `y^0`.  Both
charged degrees satisfy `m+5>=17>0` and `m+4>=16>0`.

**Band `y^{m+5}`.**  Need `i+j=m+6` with `0<=i<=m` and `0<=j<=6`.  The
only solution is `(i,j)=(m,6)`.  Hence

```text
[y^{m+5}] J  =  6 p_m' q_6 - m p_m q_6'  =  0.              (3.1)
```

**Band `y^{m+4}`.**  Need `i+j=m+5`.  The only solutions are
`(m,5)` and `(m-1,6)`.  Handle a vanishing next coefficient by reading
the corresponding summand as zero.  Hence

```text
[y^{m+4}] J
  = 5 p_m' q_5 - m p_m q_5'
    + 6 p_{m-1}' q_6 - (m-1) p_{m-1} q_6'
  = 0.                                                      (3.2)
```

No other pair contributes.  In particular Fable Card F3's parenthetical
that both bands “involve only the leading coefficients `p_m(x), q_6(x)`”
is false for (3.2).  The extra unknowns `p_{m-1}, q_5` are named here and
are included in every subsequent identity.  That is a design defect in
the card, not a missing datum that blocks interpretation: after including
them, the band still yields no leading-form constraint.  The verdict is
therefore not `REPAIR_DESIGN`.

Seed terms cannot enter either band.  The seed contributes `i=0` in `P`
and `j in {0,1}` in `Q`.  Any pair with `j<=1` has `i+j-1 <= m`, which is
strictly below `m+4`.  Equivalently: all coefficients of `y^{>=1}` in `P`
and of `y^{>=2}` in `Q` come from `109 A` and `109 B`.

---

## 4. Common-core substitution, named rings

Over `K[x]`, (3.1) is the Wronskian `(p_m^6 / q_6^m)'=0`.  With
`d=gcd(m,6)`, `a=m/d`, `b=6/d`, unique factorization in `K[x]` gives the
already-promoted form

```text
p_m = alpha h^a,     q_6 = beta h^b,     alpha, beta in K^*,   h in K[x].
```

Scale `h` primitive in `R[x]`.  Gauss: `h^a` is primitive, `p_m in R[x]`,
so `alpha in R` and `v_{109}(alpha)=v_{109}(content(p_m))`.  The seed
forces every coefficient of `y^{>=1}` in `P` to be divisible by `109`,
and `m>=12>=1`, hence

```text
A := v_{109}(alpha) >= 1,     B := v_{109}(beta) >= 1.        (4.1)
```

There is no top-row reason for `A=B`.  Constant `h` (`H=0`) is included
and satisfies both residual divisibilities `3|H` and `6|H`.  Do not
assume monicity.

Directly in `R[x]`, without localization,

```text
p_m' = alpha a h^{a-1} h',     q_6' = beta b h^{b-1} h',
```

and (3.1) is the zero polynomial:

```text
6 (alpha a h^{a-1} h') (beta h^b) - m (alpha h^a) (beta b h^{b-1} h')
  = alpha beta h^{a+b-1} (6 a - m b) h'
  = alpha beta h^{a+b-1} a (6 - d b) h'
  = 0,
```

using `m=a d` and `6=b d`.  Band one is identically tautological on the
promoted core, including `h'=0` and including unequal contents of
`alpha, beta`.

Now (3.2).  This identity lives in `R[x]` as written.  To compare with
the classical depression form, pass to the localized ring `K(x)` and set

```text
U := p_{m-1} / (alpha h^{a-1}),     V := q_5 / (beta h^{b-1}),
```

with the convention that a zero next coefficient gives `U=0` or `V=0`.
Division by `h`, `alpha`, or `beta` is used **only** in `K(x)`, and is
not an integral conclusion.  Substituting and cancelling the unit
`alpha beta` together with the power `h^{a+b-2}` (permitted in `K(x)`
when `h != 0`) yields the exact ODE

```text
d h (b U' - a V') + (d-1) h' (a V - b U)  =  0.              (4.2)
```

Specializations, as a novelty check only:

- `d=1` (the classical coprime case, e.g. `(5,6)`): `b U - a V` is
  constant, recovering sextic-preflight (4.4).
- `d=2` (e.g. `(4,6)`): `W:= b U - a V` satisfies `2 h W' = W h'`, and
  `N:= h^2 W` recovers `N^2 = kappa H^5`.

For the residual values:

```text
d=3 (b=2):   W := 2 U - a V,     3 h W' - 2 W h' = 0,
             hence W^3 / h^2 in K  (in K(x), h != 0).         (4.3a)

d=6 (b=1):   W := U - a V,       6 h W' - 5 W h' = 0,
             hence W^6 / h^5 in K  (in K(x), h != 0).         (4.3b)
```

If `h` is constant then `h'=0`, so `W` itself is constant.  If `W=0`
then (4.2) holds for every `h`.  The aligned family

```text
U = a r,     V = b r     (common generator K = h y^d + r y^{d-1} + ...)
```

has `W=0` and occupies the `kappa=0` / `lambda=0` branch.

On the mismatch branch in `K(x)`, treating `W` and `h` as polynomials
with `kappa != 0` (resp. `lambda != 0`):

```text
d=3:  3 deg W = 2 H  =>  3 | H,
d=6:  6 deg W = 5 H  =>  6 | H,     because gcd(5,6)=1.
```

Both arrows are **already** the promoted residual (5.4) of the floor-six
composition.  The mismatch branch does not shrink `H` further.  The
aligned branch imposes no condition on `H` at all.

None of (4.2)--(4.3) may be copied back into `R[x]` by dividing by `h`.
A constant `p_{m-1}` need not be divisible by `h^{a-1}` in `R[x]`.  The
integral statement is (3.2), which is linear in the free next
coefficients and always has solutions in `R[x]` (zero next coefficients;
common-power families after multiplying by `109`; the `(12,6)`
automorphism, which is not AS109 but shows that `det J=1` is compatible
with (3.2) at the residual numerical type).

---

## 5. Scalar-content lower bounds; moduli `109` and `109^2`

Write `C:=v_{109}(content(p_{m-1}))` and `D:=v_{109}(content(q_5))`, with
the convention `C=infty` or `D=infty` for a zero polynomial.  The seed
gives `C>=1` and `D>=1` (`m-1>=11>=1` and `5>=2`).  Characteristic
`0` and `109 != 2,3,5` make the integer prefactors `5,6,m` of valuation
zero except in the irrelevant special case `109 | (m-1)`, which only
*raises* a valuation.  Differentiation does not drop `109`-adic content.
Therefore every summand of (3.2) has

```text
v(5 p_m' q_5)      >= A + D >= 2,
v(m p_m q_5')      >= A + D >= 2,
v(6 p_{m-1}' q_6)  >= C + B >= 2,
v((m-1) p_{m-1} q_6') >= C + B >= 2.
```

The same holds for (3.1) with `v>= A+B >=2`.  Consequently:

- modulo `109`, both bands are `0=0`;
- modulo `109^2`, both bands are `0=0`;
- unequal contents `(A,B,C,D)` cannot produce a leftover of valuation
  `0` or `1`;
- there is no mixed-valuation sum whose carry could equal a unit.  The
  target of both bands is `0`, not `1`.  Kummer-carry / face isolation
  has nothing to push against.

After proving `109^2` divides every coefficient of (3.1) and (3.2),
division by `109` (indeed by `109^2`) is legitimate in `R[x]`.  Write
`p_m=109 tilde p_m` and likewise for `q_6, p_{m-1}, q_5`.  The divided
second band is

```text
5 tilde p_m' tilde q_5 - m tilde p_m tilde q_5'
  + 6 tilde p_{m-1}' tilde q_6 - (m-1) tilde p_{m-1} tilde q_6'  = 0,
```

which is the same characteristic-zero identity (3.2) on the 109-free
parts.  It is one ODE for two unknown next coefficients given the
leadings.  It does not constrain `(h, alpha, beta, d, H)`.

The first modulus at which a *normalized* relation can even be nonzero
as a polynomial is therefore the divided characteristic-zero equation
itself.  That relation is tautological as a constraint on the promoted
core: it is the Keller first-nontop row, satisfied by every control in
§6.

Reduction of the *undivided* leadings modulo `109` is even more
vacuous: `p_m ≡ q_6 ≡ p_{m-1} ≡ q_5 ≡ 0 (mod 109)` by the seed, so both
high bands vanish before any Wronskian is computed.

Finite-field arithmetic was used only as a check that sampled integer
polynomials are `0` modulo `109` and `109^2`.  No characteristic-`109`
identity is promoted.

---

## 6. Controls

### 6.1 Exact `(12,6)` automorphism (scope control, not AS109)

```text
u = x+y,     v = y+u^6,     (P,Q) = (u+v^2, v).
```

Independent sparse expansion: `J={(0,0):1}`, actual `y`-degrees `(12,6)`,
both top `x`-degrees `0`, so `d=6` and `H=0`.  Leading coefficients are
the units `p_{12}=1`, `q_6=1`.  Next coefficients include `q_5=6x` and
`p_{11}=12x`.  Both charged bands vanish (they are coefficients of
`y^{17}` and `y^{16}` in the constant `1`).  The constant-leading
reduction of (3.2) is

```text
6 p_{11}' q_6 = 12 p_{12} q_5',
```

i.e. `6·12=12·6`, and the localized mismatch is `W=U-aV=12x-2·6x=0`.
The numerical residual type is occupied by a determinant-one
automorphism.  This map is not congruent to the AS109 seed (`v_{109}(q_6)=0`).
It forbids any claim that (3.1)--(3.2) raise the one-sided floor from
six to seven, and it forbids “`H=0` implies `p_{m-1}` constant”.

### 6.2 Common-power zero-Jacobian families

For every residual pair `(m,6)` there is a polynomial family with those
exact top degrees and Jacobian zero, hence with both charged bands zero:

```text
d=3:  K in R[x][y] of actual y-degree 3,
      P = alpha K^{m/3},   Q = beta K^2.     (smallest m=15)

d=6:  K of actual y-degree 6,
      P = alpha K^{m/6},   Q = beta K.       (smallest m=12)
```

Taking `alpha, beta` divisible by `109` and `h` the leading `x`-coefficient
of `K` makes the 109-adic contents satisfy (4.1).  The family is not a
Keller pair and is not the seed.  It is the exact analogue of
history-stop (5.5): it rules out a *universal first-nontop valuation
contradiction*, not a later-row or seed-specific obstruction.

Zero next coefficients (`p_{m-1}=q_5=0`) sit on this family with `r=0`
and satisfy (3.1)--(3.2) on the nose.

### 6.3 Constant leading core, both residual `d`, unequal contents

- `H=0`: (3.1) is `0=0` because both leadings are constant.  (3.2)
  collapses to `6 p_{m-1}' q_6 = m p_m q_5'`, a relation among next
  coefficients, occupied by §6.1.
- `d=3` and `d=6`: both (4.3) and the polynomial form (3.2) hold on
  the aligned family and on polynomial mismatch samples satisfying the
  power relation for `W` (which force the already-promoted divisibility
  of `H`).
- Unequal contents, e.g. `(A,B,C,D)=(1,2,1,3)` or `(2,1,3,1)`: every
  summand of (3.2) still has valuation at least `2`.  A deliberately
  uncoupled choice of next coefficients makes (3.2) a nonzero polynomial
  of valuation `>=2`, which is consistent because that choice is not
  Keller.  Coupling them restores identical vanishing.

### 6.4 Seed-specific lower coefficients

They do not enter either charged band, as recorded after (3.2).  The
constant `1` in `J=1` does not enter either charged band.  Face isolation
of the top two `y`-degrees cannot see the seed and cannot see the unit
Jacobian.  Any band that sees `q_1=1+109 beta_1` starts at `y^m`; any
band that sees `p_0=x-x^{109}+109 A_0` starts at `y^5`.  Card F3
explicitly forbids descending.

---

## 7. Strongest surviving conclusion

**Integral statement.**  Let `(P,Q)` be an exact integral polynomial
AS109 lift with `deg_y Q=6` and `deg_y P=m>=12`.  Write coefficients as
in the charged question.  Then in `R[x]`:

```text
6 p_m' q_6 - m p_m q_6'  =  0,                               (7.1)

5 p_m' q_5 - m p_m q_5'
  + 6 p_{m-1}' q_6 - (m-1) p_{m-1} q_6'  =  0,               (7.2)
```

every summand of both identities is divisible by `109^2`, and (7.1) is
the already-promoted common core.  Identity (7.2) is a linear first-order
condition on `(p_{m-1}, q_5)` given the leadings.  It imposes no further
restriction on `(h, alpha, beta, d, H)` beyond the residual
classification already confirmed by the floor-six composition and its
hostile review.

This is not emptiness of `n=6`, not a floor seven, not a support bound,
and not a statement that an AS109 lift exists or does not exist.

No finite replay is required to promote a new constraint, because none
was found.  The identities (3.1)--(3.2), the valuation bounds, the
`(12,6)` Jacobian, the common-power vanishing, and the degree
equivalences `3|2H iff 3|H` and `6|5H iff 6|H` were checked by an
independent `/tmp` sparse-arithmetic script (stdlib integer dicts, not
imported from any campaign replay).  Finite-field reductions were
checks only.

---

## 8. W2/W3 gauge-conductor is not an unrestricted successor

Card F3 / cross-review Card 4 named Sol Card 3 as the successor if the
two bands return no constraint: quotient the outermost polar coefficient
at the first `n=6` support by every bounded polynomial Keller gauge, at
Witt levels W2 and W3.

That object is a **history duplicate of the reviewed bounded-category
conductor program**, not a new commutative-algebra theorem and not a
changer of the unrestricted exact-lift state.

- The wild-symplectic gate, confirmed, already gives a unique
  identity-branch restricted-analytic symplectic orbit through the
  special fibre, and shows that the first Witt digit is a single affine
  orbit under the divergence-free gauge, occupied by the rational
  cotangent control.  Unrestricted completed cohomology has one orbit.
- The bounded polar-conductor gate, confirmed, already proves that the
  cotangent polar divisor cannot be cancelled by any polynomial Keller
  right map, and that a hypothetical polynomial lift `F` has algebraization
  conductor `kappa_n(F) -> infinity` from that basepoint.  Every *fixed*
  simultaneous map/gauge degree cap becomes empty at some finite Witt
  depth.  The first natural cap is empty at depth three for odd primes
  (machine-checked at `p=3,5`; the structural identity is not
  `p=109`-specific).  No `p=109` enumeration was claimed or needed.

Sol Card 3 re-runs that bounded-cap test at W2/W3, restricted to an
`n=6` support rectangle.  The residual leading-form conditions
`6|deg_x(q_6)` and `3|m` are not inputs to either confirmed conductor
theorem, and do not remove the support/degree cap that makes the
computation bounded.

Both outcomes fail to change the unrestricted exact-lift state:

| Bounded W2/W3 outcome | Why it does not promote |
|---|---|
| Empty at a degree cap | Strict subset of “no lift inside this cap”.  Same stop class as an `n=2` Newton rectangle after floor six |
| Finite-depth survivor | Truncated Witt point, not an exact polynomial lift |
| Nonzero stable class | Finite-depth evidence toward unbounded conductor, which is already the polar-conductor theorem `kappa_n -> infinity` |
| Explicit cancelling gauge | A bounded direction; polar conductor already says it cannot polynomialize `C_p`.  Not an AS109 lift |

The prompt licenses one executable successor only if it changes the
unrestricted exact-lift state in *both* outcomes.  None is available
from two-band face isolation, from a third `y`-band (Card F3 hard-stop:
combinatorial blowup, seed still absent until `y^m` or `y^5`), or from
W2/W3 at a support cap.

---

## 9. Launch / stop

```text
verdict              = TWO_BANDS_TAUTOLOGICAL
card_F3              = STOP-AS109-N6-TWO-BANDS
floor_six            = unchanged
residual_n=6         = unchanged  (not empty, not floor seven)
new_integral_claim   = none beyond (7.1)--(7.2) as tautologies on the core
w2w3_gauge_conductor = HISTORY-DUPLICATE of polar-conductor / wild-symplectic
                       bounded-category gates; do not launch as a
                       state-changing job
unrestricted_successor = none
lift_found           = false
lift_excluded        = false
jc2_inference        = false
```

**Stop under Card F3.**  Two bands fully analyzed, no new constraint.
Do not descend to lower `y`-bands without a fresh mechanism.  Do not
reopen `n=2..5` or prime target degrees.  Do not launch unstructured
support search on the surviving leading forms.  Do not launch the W2/W3
gauge-conductor as if it were an independent unrestricted test.

Bank the null: nobody should pay a second time for “top two Jacobian
`y`-bands at residual `n=6`”.

---

## 10. Scope firewall

This report does not prove that an AS109 lift exists or does not exist.
It does not bound `x`-support, route every `n=6` pair, construct a
marked collision, decide any other characteristic-`109` seed, prove a
characteristic-zero counterexample, or decide JC2.  Partial `y`-degree
is chart-dependent; the identities are for the displayed AS109
coordinates.  The `(12,6)` automorphism is a Keller-equation occupancy
control, not a lift.  The common-power families have Jacobian zero, not
one.  Finite-field vanishing is not a characteristic-zero proof; the
proofs are the coefficient assembly (3.1)--(3.2), the identical
vanishing of (3.1) on the core, the valuation bounds in `R[x]`, and the
named-ring status of (4.2)--(4.3).
