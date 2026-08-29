# Hostile cross-review: row-28 universal class zero and the row-30 symbolic nonlinear prefix

Reviewer: Grok 4.6 (xAI), different-model hostile referee  
Pinned model ID: `grok-4.6`  
CLI/version: `grok 1.0.5 (5115b46bc909)` (`/Users/dc/.grok/bin/grok`)  
Host: Python 3.14.6, Darwin 23.6.0 arm64  
Date: 2026-08-27  
Charged source:
`xmodel/ggv-quarter-root-r28-nonlinear-class-test-r0-sol-ultra-20260827.md`  
Producer: Sol Ultra (different model family ⇒ this is a valid promotion
leg if it survives)

No JC2 theorem, endpoint decision, raw-`D28`/`D30` decision, family
exclusion, polynomial-`G` witness, or landing claim is made.

## 0. Headline verdict

**Every charged exact claim survives independent rederivation. Nothing
charged is REFUTED. One motivational citation is not recomputed as a
matrix in this session and is recorded as a non-load-bearing GAP.**

| # | Charged claim | Verdict |
|--:|---|---|
| 1 | `q_6=F_6/4`, `R_6=0`, gauged row-28 class identically `(0,0,0,0;0)` | **CONFIRMED** (unrestricted source-ring identity; universal, not a point observation) |
| 2 | Named frozen endpoint fixture is unusable as a row-23+ class prefix | **CONFIRMED** (`D23_imposed: false` on all four systems; `F_1=H=A^2` is the reviewed `q1` negative control; no algebraic witness) |
| 3 | Every coefficient of the gauged `q_8` remainder (4.1) | **CONFIRMED** (all eight binomial prefactors, all seven `A`-exponents, `A^{15}p^{-30}=ε`) |
| 4 | Slice (5.1) respects frozen windows and passes class rows 23–29 over `Q[u,v]` | **CONFIRMED** |
| 5 | Row-30 substitution, root residues, infinity residue, ideal `(uv,u^4)`, nonlinear carry nonzero on this exact prefix slice | **CONFIRMED** |
| 6 | Scope firewalls (not raw determinant, not polynomial-`G`, not endpoint, not family exclusion, not JC2) | **CONFIRMED** |

The earlier `R28-CLASS` proposal in the cited carrier review, which treated
`R_6(F_1,...,F_5)` as a possibly nonzero remainder, is correctly identified
as dead: `(n+2)/8=1` at `n=6` forces `binom(1,d)=0` for every `d>=2`.  That
correction is already in the cited Opus5 `NU-LAW` hostile review.  The first
honest uncancellable nonlinear class on branch P is row 30, and it is
nonzero on the exact two-parameter slice (5.1).

**Promotion recommendation.** Promote the two decided exact atoms at
desk-class scope, and nothing wider.  See §8.

---

## 1. Custody

Charged SHA-256, recomputed on live bytes before the algebra below:

```text
e487bd6f54be9762dd551abe7bd25cabed4b9daa053b57a9a424441ef269848e
  xmodel/ggv-quarter-root-r28-nonlinear-class-test-r0-sol-ultra-20260827.md
```

Every additional local file opened is one the charged report names.
Recomputed hashes match the producer’s §1 block exactly:

```text
67c4038230829b7b9abea540d78ec15af8f87aa66259c0c8b79873de6106251e
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/SOURCE.sha256
60e6b274ca6daa64dd5dc2ddb9cd62984dbefff3ae04d612f2ec36fe1e1e26bf
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/PREREGISTRATION.md
93db31ce9d3c7d41e42d496039eda9f58bc1d92938d16bb71e60b0722929b96e
  cases/ggv_8_28_upper_endpoint_branch_p_20260827/TERMINAL_CUSTODY.md
6e3d9104effe39c0dd0e34377bb7bdc6ede4f25f472f9f9c0098706aceffb60a
  xmodel/ggv-8_28-upper-cascade-w3-w6-sol-ultra-20260827.md
7358e6623a84ddd6b1aaad1a9b07a1c0c8966f74f75203977c0314bf3588e7ec
  xmodel/ggv-8_28-upper-cascade-w3-w6-hostile-review-fable5-20260827.md
46736edc8aa391e50d3c6a1604937bcad85361c25c25f9e3b4c184e19f8afed1
  xmodel/ggv-survivor-q1-q2-de-rham-gates-fable5-hostile-review-opus5-20260827.md
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1
  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md
71befadb3496f5f6c8e3136e7019de95dec2f205f2655734eac2c84d8e0e24d1
  xmodel/ggv-quarter-root-sector-gate-rec-theorem-r8-sol-ultra-20260827.md
60670d0a7066ab0a1d1f72ad05a0ff44a858fa39dbf4d18fd225913d26b6d114
  xmodel/ggv-quarter-root-sector-gate-rec-theorem-r8-crossreview-opus5-20260827.md
70fd8be4d3e00b4e14869166186cedf218fd3cd4370d0dcc049543a6853eb762
  xmodel/ideation-20260827T2259Z-opus5-hostile-review-sol-ultra.md
9c8c61a1ca6f71c3a04c396b176da4798817eff75f67e7508ed5be047d988c26
  xmodel/ideation-20260827T2259Z-carrier-hostile-review-sol-ultra.md
b3f3886c7783ce22e060865206a700f0aab356caf6f708f75f355e99b684517a
  xmodel/ideation-20260827T2137Z-opus5-crossreview-fable5.md
```

The four named system JSON files were opened only for the field
`D23_imposed`.  All four carry `false`:

```text
RAW_DIRECT_SYSTEM.json                 charged_rows.D23_imposed: false
ROW_RREF/ROW_RREF_SYSTEM.json          D23_imposed: false
PREFIX_QUOTIENT/PREFIX_QUOTIENT_SYSTEM.json
                                       D23_imposed: false
HOMOGENIZED/HOMOGENIZED_SYSTEM.json    D23_imposed: false
```

`SOURCE.sha256` was hashed and not replayed with `shasum -c`.  It pins a
path outside the named case
(`cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json`).
No byte from that outside path is used.  The case directory listing was
consulted only to confirm the absence of a rational witness/result file;
`TERMINAL_CUSTODY.md` already records that both terminal runs returned no
algebraic result.

Lagrange–Bürmann (2.1) is taken as the independently reviewed R8 input
(Opus5 re-derived it by reversion).  The `F`-degree expansion, every
binomial coefficient, both gauges, the `T_A` rank/nonmembership check, the
slice identities, the Laurent residues, and the residue ideal are
re-derived here.  Licensed inputs used but not re-proved as theorems:
the R8 formula (1.1)/(2.1), the connection `nabla_m(f)=(f'+(m/4)(H'/H)f)dX`,
the branch-P `q1` image theorem `T_A(Q)=2AQ'-3A'Q` with `deg Q<=12`,
and the D3 upper windows `deg F_n <= 16-n`.

No unrelated `2259Z` peer submission was read.  No path under `jc2-lean`
was listed, opened, searched, read, built, statused, or modified.  No AWS
host/job was contacted.  No canonical ledger was edited.  Local work is
exact `fractions.Fraction` desk arithmetic only: binomial coefficients,
a `16 x 13` matrix rank over `Q`, polynomial arithmetic in `Q[X]`, and
truncated Laurent series at `X=1` and at infinity.  No CAS, Groebner
basis, random seed, or hidden file input.

This file is the only write.

---

## 2. Charge item 1 — `q_6=F_6/4`, row-28 gauge, universal class zero

**Verdict: CONFIRMED.**

### 2.1 Source-ring identity

Write `F=H^2(1+g)` with `g=sum_{i>=1}(F_i/H^2)t^i` and `p^4=H`.  The
reviewed formula

```text
q_n = 2/(n+2) [t^n] F^{(n+2)/8}
```

and the binomial theorem give, for `d>=1`,

```text
[q_n]_d = 2/(n+2) binom((n+2)/8, d) p^{n+2-8d} S_(n,d),
S_(n,d) = sum_{i_1+...+i_d=n, i_j>=1} F_{i_1}...F_{i_d}.
```

This is the producer’s (2.2).  At `n=6`, `(n+2)/8=1`, so
`binom(1,1)=1` and `binom(1,d)=0` for every `d>=2`.  The `d=0` term
contributes only at `n=0`.  Hence, over the unrestricted source ring,

```text
[q_6]_1 = (2/8) p^{0} F_6 = F_6/4,
[q_6]_d = 0  (d>=2),
q_6 = F_6/4,
R_6 = 0.
```

Rows 23–27 are not used.  The identity is independent of `H`, of the
prefix equations, and of the choice of Kummer component.  **CONFIRMED.**

This is the same vanishing the cited `NU-LAW` review records as
unconditional class-row death at `m == 4 (mod 8)`: if `8` divides `n+2`
and `N=(n+2)/8>=1`, then `q_n=(1/(4N))[t^n]F^N` is a polynomial in `X`
whenever the `F_i` are, hence has a polynomial primitive in characteristic
zero.  Row 28 is the first instance (`n=6`, `m=28`).

The cited carrier `R28-CLASS` proposal wrote
`q_6=(1/4)F_6+R_6(F_1,...,F_5)` and asked for the residue of `R_6 dX`.
That remainder does not exist.  **CONFIRMED as a correction, not as a
new identity.**

### 2.2 Normalization and ordinary residues

Campaign row `m=n+22=28`.  R8 typing: the class representative is
`c_{28}=p^{-28}q_6`.  Then `p^{28}=H^7`, so

```text
c_{28} = F_6/(4H^7) in A,
nabla_{28}(f) = (f' + 7(H'/H)f) dX.
```

The product rule gives `d(H^7 f)=H^7 nabla_{28}(f)` identically.
The gauged ordinary form is therefore `(F_6/4)dX`.  For polynomial
`F_6` this is a polynomial 1-form on `P^1`:

- at every finite point, including the four simple roots of `A=X^4-1`,
  it is holomorphic, residue `0`;
- at infinity, `X=u^{-1}`, `dX=-u^{-2}du`, and
  `sum_{k>=0} a_k X^k dX = -sum_{k>=0} a_k u^{-k-2} du` has no
  `u^{-1}` term, so `res_infinity=0`.

The five-entry ordinary residue coordinate, adjoining `i` only to label
the roots `1,-1,i,-i`, is `(0,0,0,0;0)`.  This is an identity in the
source ring, not a vanishing at one numeric prefix.  **CONFIRMED.**

---

## 3. Charge item 2 — named frozen fixture is not a row-23+ prefix

**Verdict: CONFIRMED.**

The case preregistration is titled “fixed branch-P upper endpoint before
row 23” and freezes, verbatim,

```text
A = X^4-1,  H=A^2,  F1=H,
D7=...=D21=0,  D22=1,
```

and states that neither `D23=0` nor the `q1` image equation is an input.
All four serialized systems repeat `D23_imposed: false`.  R7R1 licenses
`q1` only once row `D23` is imposed.  So the case is not a class-prefix
run through row 23, let alone through 27 or 29.

Independently of that custody fact, the frozen value fails the first
upper gate on the nose.  The reviewed branch-P `q1` theorem says
`[q_1 dX]=0` iff `F_1` lies in `im(T_A)`,

```text
T_A(Q) = 2 A Q' - 3 A' Q,     deg Q <= 12.
```

For `A=X^4-1` I recomputed the `16 x 13` matrix of
`T_A(X^d)`, `d=0..12`, in the window `deg<=15` by exact Gaussian
elimination over `Q`: rank `13`.  Adjoining `H=A^2=X^8-2X^4+1` raises
the rank to `14`.  Hence `H` is outside the image.  The same
nonmembership is the reviewed negative control `F1=A^2` in the cited
Opus5 `q1` table (passes weight-3, fails `q1`), and it is the cascade
separator `V=1` in the cited W3–W6 report.  As a second functional
check, the reviewed cokernel coordinate `phi_1=c_0/3-c_4/15+c_8/3+c_{12}`
takes the value `4/5` on `H`, not `0`.

`TERMINAL_CUSTODY.md` records no algebraic result from the terminal
runs (memory halt; `SIGTERM` with empty stdout; Box02 refused before
`RUN_STARTED`).  The allowed evidence therefore supplies no nontrivial
numeric row-29 class prefix with exact replay bytes.  Inventing a
numeric point would have been a scope violation; the producer did not
do so.  **CONFIRMED.**

---

## 4. Charge item 3 — every coefficient of gauged `q_8`

**Verdict: CONFIRMED.**

Row 30 has `n=8`, `m=30`, `(n+2)/8=5/4`.  This is not mod-8 dead.
On branch P, `p^2=ε A` with `ε in {+1,-1}`.  The connection is

```text
nabla_{30}(f) = (f' + (30/4)(H'/H) f) dX
             = (f' + 15 (A'/A) f) dX,
```

because `H=A^2` gives `H'/H=2A'/A`.  Multiplication by `A^{15}` gauges
it to ordinary `d`.  The prefactor of the physical series is

```text
A^{15} p^{-30} = A^{15} / (p^2)^{15} = A^{15}/(ε^{15} A^{15}) = ε^{-1} = ε.
```

So the ordinary representative is `ε q_8`.  Expanding `q_8` by (2.2) and
substituting `p^{10-8d}=ε A^{5-4d}` (using `ε^{4d}=1` and `ε^5=ε`)
cancels the remaining `ε`, independently of the component:

```text
ε [q_8]_d = c(8,d) A^{5-4d} S_(8,d),
c(n,d) := 2/(n+2) binom((n+2)/8, d).
```

The `A`-exponents at `d=2,...,8` are `-3,-7,-11,-15,-19,-23,-27`,
matching (4.1).  The linear term is `A F_8/4`, a polynomial, hence
ordinary-exact in characteristic zero.  `F_8` occurs only in `S_(8,1)`,
so it cannot cancel the remainder.  **CONFIRMED.**

The eight prefactors, computed independently from the Pochhammer ratio
`α(α-1)...(α-d+1)/d!` at `α=5/4`, are exactly

```text
c(8,1..8) = 1/4, 1/32, -1/128, 7/2048,
            -77/40960, 77/65536, -209/262144, 4807/8388608.
```

Hand reductions that match the last three claimed values:

```text
binom(5/4,4) = 35/2048,     (1/5) that = 7/2048;
binom(5/4,5) = -77/8192,    (1/5) that = -77/40960;
binom(5/4,6) = 17325/2949120,
  (1/5) that = 17325/14745600 = 77/65536
  (cancel 25 then 9);
binom(5/4,7) = 17325/2949120 * (-19/4)/7
             = -329175/82575360,
  (1/5) that = -209/262144;
binom(5/4,8) gives 4807/8388608.
```

Formula (4.1), with no `F_8`, is the correctly gauged row-30 nonlinear
class.  **CONFIRMED, every coefficient.**

Receiver dimension, used only as motivation: `e_i=2`, `4` divides
`30·2=60`, so `k_{30}=1` and `dim V_{30}=r-1+k_{30}=4`.  The five
ordinary residues with sum zero are a complete coordinate.

Non-load-bearing GAP, motivational only: the producer cites a reviewed
rank-three `F_7` newest-slot map at row 29 as the reason row 29 is not a
clean obstruction.  I independently confirm the *receiver* dimension
`dim V_{29}=3` (`4` does not divide `29·2=58`, so `k_{29}=0`,
`r-1=3`).  The *realized rank three* is present in the cited `NU-LAW`
P-measured table (row 29 entry `3`) and in the cited carrier review.  I
did not reassemble the `F_7`-window matrix.  Nothing in items 1–5 or in
the residue vector uses that rank.

---

## 5. Charge item 4 — symbolic slice, windows, class rows 23–29

**Verdict: CONFIRMED.**

The slice is a two-parameter map `Q[u,v] ->` (branch-P prefix ring at
`A=X^4-1`), *not* a point of the named `F_1=H` fixture (that fixture
already failed row 23):

```text
F_1=F_3=F_5=F_7=0,
F_2=4u A^2 A',
F_4=2u^2 (A')^2,
F_6=v.
```

Frozen D3 upper windows `deg F_n <= 16-n`:

```text
F_2 = 16u (X^{11}-2X^7+X^3),     deg 11 <= 14,
F_4 = 2u^2 · 16 X^6,            deg  6 <= 12,
F_6 = v,                        deg  0 <= 10,
F_odd = 0,                      in every window.
```

The `91` count is the sum of the seven raw windows
`16+15+14+13+12+11+10`.

`F(X,-t)=F(X,t)`, so `F^{(n+2)/8}` is even in `t` as a formal series
even for non-integral exponents.  Every odd `q_n` vanishes identically
on the slice, including `q_1,q_3,q_5,q_7`.  Rows 23, 25, 27, 29 are
therefore class-exact.

Row 24: with `F_1=0` and `H=A^2`,

```text
q_2 = F_2/(4H) = u A' = d(u A)/dX.
```

The physical form is already ordinary-exact; after the `p^{-24}`
normalization the `A^{12}` gauge returns the same ordinary form
`u A' dX`.  **CONFIRMED.**

Row 26: the `ε`-stripped combination displayed by the producer is the
bracket in `q_4=ε[F_4/(4A)-F_2^2/(32 A^5)]`.  Substituting the slice
gives

```text
F_4/(4A) = (u^2/2) (A')^2/A,
F_2^2/(32 A^5) = (1/2) u^2 (A')^2/A,
```

so the bracket is the zero polynomial (verified as an identity in `Q[X]`
after clearing `A^5`, at several `(u)` specializations and hence in
general).  Thus `q_4=0` as a function, not merely as a class.
**CONFIRMED.**  (The omitted overall twist `ε` is harmless because the
bracket vanishes.)

Row 28: `q_6=v/4=d(v X/4)/dX`, ordinary-exact.  **CONFIRMED.**

The slice therefore factors through the exact class-prefix coordinate
ring for rows 23–29 over `Q[u,v]`.  It is not asserted to satisfy any
raw `D_n`, to have a polynomial `G`, or to satisfy `D_{22}=1`.  Those
are the producer’s own firewalls.

---

## 6. Charge item 5 — row-30 substitution, residues, ideal, nonzero carry

**Verdict: CONFIRMED.**

### 6.1 Surviving compositions and the rational identity (5.3)

On (5.1) the only even ordered compositions of `8` with parts in
`{2,4,6}` are

```text
S_(8,2) = 2 F_2 F_6 + F_4^2,
S_(8,3) = 3 F_2^2 F_4,
S_(8,4) = F_2^4,
```

and `S_(8,d)=0` for `d>=5` (five or more even positive parts sum to at
least `10`).  Substituting into (4.1) and collecting,

```text
(1/32) A^{-3}(2 F_2 F_6+F_4^2)
  = (uv/4) A'/A + (1/8) u^4 (A')^4/A^3,
(-1/128) A^{-7}(3 F_2^2 F_4)
  = -(3/4) u^4 (A')^4/A^3,
(7/2048) A^{-11} F_2^4
  =  (7/8) u^4 (A')^4/A^3.
```

The `u^4` coefficients sum to `1/8-3/4+7/8=1/4`, hence

```text
R_8 = (uv/4) A'/A + (u^4/4) (A')^4/A^3.
```

This was rechecked as a polynomial identity after multiplying through by
`A^{11}`, at the specializations
`(u,v) in {(1,1),(1,0),(0,1),(2,3),(-1,5)}`.  All five differences are
the zero polynomial.  **CONFIRMED.**

### 6.2 Finite residues

For a simple root `α` of `A`, write `t=X-α`,
`A=a_1 t+(a_2/2)t^2+(a_3/6)t^3+O(t^4)`, `a_1=A'(α)≠0`.  Direct Laurent
expansion of `(A')^4/A^3 dX` yields residue

```text
(3/2) ( A'''(α) + A''(α)^2 / A'(α) ),
```

which is the producer’s (5.4).  For `A=X^4-1` one has `A'=4X^3`,
`A''=12X^2`, `A'''=24X`, and `α^4=1`, so the combination is `90α`.
Independent of (5.4), the series at `t=X-1`

```text
A(1+t)=4t+6t^2+4t^3+t^4,    A'(1+t)=4+12t+12t^2+4t^3
```

gives residue `90` as the coefficient of `t^2` in
`(A')^4/(A/t)^3`.  **CONFIRMED.**

Also `res_α((A'/A)dX)=1` at each simple root.  Therefore, in the order
`1,-1,i,-i`,

```text
res_α(R_8 dX) = uv/4 + (45/2) u^4 α.
```

This is the printed four-tuple.

### 6.3 Infinity residue and the sum-zero check

With `u=1/X`, `dX=-u^{-2}du`:

```text
(A'/A) dX = -4 u^{-1}/(1-u^4) du,          res_infinity = -4,
(A')^4/A^3 dX = 256 (1-u^4)^{-3} (-u^{-2}) du.
```

The second expansion involves only powers `4k-2`, never `u^{-1}`, so
its infinity residue is `0`.  (Equivalently: `sum` of residues of
`d log A` on `P^1` is zero, four simple zeros contribute `+1` each, so
infinity contributes `-4`.)  Hence

```text
res_infinity(R_8 dX) = (uv/4)(-4) + 0 = -uv.
```

The five entries sum to `uv-uv=0`, as required by the residue theorem
on `P^1`.  **CONFIRMED.**

The complete ordinary residue vector on the slice, in the order
`1,-1,i,-i,infinity`, is therefore exactly

```text
( uv/4 + (45/2) u^4,
  uv/4 - (45/2) u^4,
  uv/4 + (45/2) i u^4,
  uv/4 - (45/2) i u^4;
 -uv ).
```

### 6.4 Ideal and nonvanishing

Let `I=(v_1,...,v_5)` in `Q(i)[u,v]`.  Then `-v_5=uv` and
`v_1-v_2=45 u^4`, so `(uv,u^4) subset I`.  Each `v_j` lies in
`(uv,u^4)`, so `I=(uv,u^4)`.  The contraction to `Q[u,v]` is the same
ideal.  Its radical is `(u)`: the zero set is the line `u=0`, and `(u)`
is prime.  **CONFIRMED.**

The vector is the zero element of `Q(i)[u,v]^5` if and only if `u=0`.
On `u=0` one has `F_2=F_4=0` and `R_8=0`, recovering the exact
`F_6`-only direction already known to be class-exact at row 28.  For
`u≠0` — in particular as a polynomial vector, e.g. the coefficient of
`u^4` in the first slot is `45/2≠0` — the class is nonzero.  Newest-slot
`F_8` cannot cancel it.  Row-30 nonlinear carry is therefore genuinely
nonzero on this exact licensed symbolic prefix family.  **CONFIRMED.**

This is a two-parameter slice, not a theorem on the whole prefix
coordinate ring, and not a numeric survivor.  The producer does not
claim otherwise.

---

## 7. Charge item 6 — scope firewalls

**Verdict: CONFIRMED.**  Every firewall in the producer’s §7 is
respected by the mathematics and by this review.

* Class exactness of (5.1) is a necessary condition for a polynomial
  determinant solution, not a sufficient one.  The slice is not claimed
  to have a polynomial `G`, to satisfy `D_{22}=1`, or to satisfy any
  raw row `D_{23}...D_{30}`.
* Universal class-row death at row 28 does not imply that raw `D_{28}`
  is the zero polynomial, nor that its polynomial-window descent
  condition is vacuous.
* The row-30 vector is not a generic theorem for a 71-dimensional
  prefix locus, not a numeric witness, and not an endpoint result.
* No face/family exclusion, Keller pair, landing, counterexample,
  finite tower bound, or JC2 conclusion follows.
* No AWS was contacted.  No heavy local computation ran.  No canonical
  file was edited.  `jc2-lean` was not entered.

The maximum licensed conclusion remains exactly the producer’s:

```text
R28-CLASS = IDENTICALLY ZERO (universal exact control).
R30-CLASS = NONZERO on the exact symbolic prefix slice (5.1),
            with every raw/endpoint firewall.
```

This review supplies the independent different-model leg that the
producer’s status line requested.  It does not widen the claim.

---

## 8. Promotion recommendation

**PROMOTE** the two decided exact atoms, at desk-class scope, as a
different-model confirmation of the charged Sol Ultra r0 report:

1. `q_6=F_6/4` and `R_6=0` as a polynomial identity; after the licensed
   `p^{-28}` / `H^7` gauge, the ordinary residue vector of row 28 is
   identically `(0,0,0,0;0)`.  This is universal class-row death at
   `m=28==4 (mod 8)`, and it retires the cited carrier `R28-CLASS`
   remainder test.
2. On the exact slice (5.1), which passes class rows 23–29 over
   `Q[u,v]` and lies in the frozen D3 windows, the gauged row-30
   nonlinear remainder has ordinary residue vector as printed in §0 of
   the charged report, equivalently the nonzero element of
   `Q(i)[u,v]^5` with common residue ideal `(uv,u^4)`.

**DO NOT PROMOTE** any of: a raw-determinant prefix; a polynomial-`G`
witness; a `D_{22}=1` endpoint; a generic statement on the whole prefix
locus; a family/face exclusion; a finite tower bound; a Keller pair;
a landing; a JC2 result.

The `F_7` rank-three motivational sentence may be retained as a citation
of the reviewed P-measured table; it is not a newly proved atom of this
report and should not be promoted from here.

---

## 9. Exact replay

Independent of the producer’s script.  Exact `fractions.Fraction` only.

```bash
python3 - <<'PY'
from fractions import Fraction as Q
from math import factorial

def binom(a,d):
    z=Q(1)
    for j in range(d):
        z *= a-j
    return z/factorial(d)

def c(n,d):
    return Q(2,n+2)*binom(Q(n+2,8),d)

assert c(6,1)==Q(1,4)
assert all(c(6,d)==0 for d in range(2,7))
cs=[c(8,d) for d in range(1,9)]
assert cs==[Q(1,4),Q(1,32),-Q(1,128),Q(7,2048),
            -Q(77,40960),Q(77,65536),-Q(209,262144),Q(4807,8388608)]
print('q6', [str(c(6,d)) for d in range(1,7)])
print('q8', [str(x) for x in cs])

def add(a,b):
    n=max(len(a),len(b)); r=[Q(0)]*n
    for i,x in enumerate(a): r[i]+=x
    for i,x in enumerate(b): r[i]+=x
    return r
def sc(s,a): return [s*x for x in a]
def mul(a,b):
    r=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            r[i+j]+=x*y
    return r
def deriv(a): return [Q(i)*a[i] for i in range(1,len(a))]

A=[Q(-1),Q(0),Q(0),Q(0),Q(1)]
Ap=deriv(A)
def TA(Qp):
    return add(sc(Q(2),mul(A,deriv(Qp))), sc(Q(-3),mul(Ap,Qp)))

cols=[]
for d in range(13):
    Qp=[Q(0)]*(d+1); Qp[d]=Q(1)
    t=TA(Qp)
    while len(t)<16: t.append(Q(0))
    cols.append(t[:16])

def rank(cols, extra=None):
    M=[list(c) for c in (cols if extra is None else cols+[extra])]
    n,m=len(M[0]),len(M)
    Amtx=[[M[j][i] for j in range(m)] for i in range(n)]
    h=0; piv=0
    for col in range(m):
        pr=None
        for r in range(h,n):
            if Amtx[r][col]!=0:
                pr=r; break
        if pr is None: continue
        Amtx[h],Amtx[pr]=Amtx[pr],Amtx[h]
        pv=Amtx[h][col]
        Amtx[h]=[x/pv for x in Amtx[h]]
        for r in range(n):
            if r==h: continue
            f=Amtx[r][col]
            if f==0: continue
            Amtx[r]=[Amtx[r][k]-f*Amtx[h][k] for k in range(m)]
        piv+=1; h+=1
        if h==n: break
    return piv

H=mul(A,A)
while len(H)<16: H.append(Q(0))
assert rank(cols)==13 and rank(cols,H[:16])==14
phi1=Q(1)/3 - Q(-2)/15 + Q(1)/3
assert phi1==Q(4,5)
print('T_A rank 13; adjoining H rank 14; phi1(H)=', phi1)

uv=cs[1]*2*4
u4=cs[1]*4 + cs[2]*3*(4**2)*2 + cs[3]*(4**4)
assert uv==Q(1,4) and u4==Q(1,4)
print('slice_R8=(1/4)uv A\'/A + (1/4)u^4 (A\')^4/A^3')

def smul(a,b,N):
    r=[Q(0)]*(N+1)
    for i in range(N+1):
        for j in range(N+1-i):
            r[i+j]+=a[i]*b[j]
    return r
def spow(a,n,N):
    r=[Q(0)]*(N+1); r[0]=Q(1)
    for _ in range(n): r=smul(r,a,N)
    return r
def sinv(a,N):
    b=[Q(0)]*(N+1); b[0]=Q(1)/a[0]
    for n in range(1,N+1):
        s=Q(0)
        for k in range(1,n+1): s+=a[k]*b[n-k]
        b[n]=-s/a[0]
    return b
N=6
Ap_s=[Q(4),Q(12),Q(12),Q(4)]+[Q(0)]*(N-3)
core=[Q(4),Q(6),Q(4),Q(1)]+[Q(0)]*(N-3)
prod=smul(spow(Ap_s,4,N), sinv(spow(core,3,N),N), N)
assert prod[2]==Q(90)
print('Laurent res_{X=1} (A\')^4/A^3 dX =', prod[2])

def cadd(z,w): return (z[0]+w[0],z[1]+w[1])
def cmul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def cdiv(z,w):
    d=w[0]*w[0]+w[1]*w[1]
    return cmul(z,(w[0]/d,-w[1]/d))
def csc(a,z): return (a*z[0],a*z[1])
def cpow(z,n):
    r=(Q(1),Q(0))
    for _ in range(n): r=cmul(r,z)
    return r
roots=[(Q(1),Q(0)),(-Q(1),Q(0)),(Q(0),Q(1)),(Q(0),-Q(1))]
res=[]
for a in roots:
    A1=csc(Q(4),cpow(a,3)); A2=csc(Q(12),cpow(a,2)); A3=csc(Q(24),a)
    res.append(csc(Q(3,2), cadd(A3, cdiv(cmul(A2,A2),A1))))
assert res==[(Q(90),Q(0)),(-Q(90),Q(0)),(Q(0),Q(90)),(Q(0),-Q(90))]
print('Res_roots (A\')^4/A^3 dX =', res)
print('row30_slice_residue_vector = '
      '(uv/4+45u^4/2, uv/4-45u^4/2, '
      'uv/4+45i u^4/2, uv/4-45i u^4/2, -uv)')
print('ideal (uv, u^4); radical (u); nonzero iff u != 0')
print('PASS')
PY
```

Exact output of this session:

```text
q6 ['1/4', '0', '0', '0', '0', '0']
q8 ['1/4', '1/32', '-1/128', '7/2048', '-77/40960', '77/65536', '-209/262144', '4807/8388608']
T_A rank 13; adjoining H rank 14; phi1(H)= 4/5
slice_R8=(1/4)uv A'/A + (1/4)u^4 (A')^4/A^3
Laurent res_{X=1} (A')^4/A^3 dX = 90
Res_roots (A')^4/A^3 dX = [(Fraction(90, 1), Fraction(0, 1)), (Fraction(-90, 1), Fraction(0, 1)), (Fraction(0, 1), Fraction(90, 1)), (Fraction(0, 1), Fraction(-90, 1))]
row30_slice_residue_vector = (uv/4+45u^4/2, uv/4-45u^4/2, uv/4+45i u^4/2, uv/4-45i u^4/2, -uv)
ideal (uv, u^4); radical (u); nonzero iff u != 0
PASS
```

---

## 10. Ledger

*Proved by hand in this session:* the `n=6` binomial vanishing and
`q_6=F_6/4`; both gauge identities `d(H^7 f)` and `d(A^{15} f)`;
`A^{15}p^{-30}=ε` and cancellation of `ε` in the remainder; the eight
`c(8,d)` Pochhammer reductions; surviving compositions `S_(8,2..4)` on
the slice; the rational identity (5.3); the general simple-root residue
(5.4); the specialization `90α`; the two infinity Laurent series;
`I=(uv,u^4)` and `rad I=(u)`; `q_2` and `q_4` exactness on the slice;
odd-vanishing from evenness of `F`; window degrees; `phi_1(H)=4/5`.

*Script-only exact rational arithmetic:* the `16 x 13` `T_A` rank and
the adjoining-`H` rank; the `A^{11}` polynomial identity for (5.3) at
five `(u,v)` points; the `t=X-1` Laurent residue `90` without (5.4);
complex arithmetic at `±i`.

*Not done:* a re-derivation of Lagrange–Bürmann from reversion (licensed
R8 input); a reassembly of the `F_7`-window matrix; any raw `D_n`
identity; any polynomial `G`; any AWS or CAS computation; any path
under `jc2-lean`.

**Review verdict: charged atoms 1–6 CONFIRMED; one non-load-bearing GAP
on the unrecomputed `F_7` rank-three citation; no REFUTED atom.
Promote R28-CLASS identically zero and R30-CLASS nonzero on slice (5.1),
at desk-class scope only.  No raw/endpoint/family/JC2 inference.**
