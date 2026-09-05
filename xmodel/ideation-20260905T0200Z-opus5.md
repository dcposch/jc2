# Ideation round 20260905T0200Z — blind submission (OPUS 5)

Seat: OPUS. Round: 20260905T0200Z (off-cycle, full-spectrum, Astra's first).
Inputs: four frozen files in `/tmp/jc2-lane.e4o07y/inputs`, manifest generated
mechanically from `xmodel/ideation-20260905T0200Z-opus5.run.v2` with awk
(pairing `charged_input_<i>_basename` / `charged_input_<i>_sha256`), verified
with `sha256sum -c`: **4/4 OK**, no digit retyped. Durable manifest
`box/abelfact-20260905/input-manifest.sha256`.

Blindness: no `ideation-20260905T0200Z-*` submission was read (I skipped
`box/ideation-20260905T0200Z-grok46/`, encountered in a grep). Both running
lanes were checked for `final_status` in their `.run.v2` — **neither had one**
— so `moh100-14rows-opus5-20260905.md`, `k16-f3abel-astra-20260905.md` and
`box/moh14-20260905/` were NOT read (see §13 for the one banked-AUDIT
exception). Banked material used: AUDIT 17(cccccc)–(jjjjjj), `notes.md`
LIVE STATE/EVENT tail, `k16-8point1-astra-20260905.md` (sealed),
`box/mohprog-drivers-20260903/{tree-independent-notes.md,independent_enumerator.py}`.
No ledger edited.

New work lives in `box/abelfact-20260905/`.

---

## 0. Disposition vector (changes only)

| # | Item | Previous | Mine | Why |
|---|---|---|---|---|
| D1 | K16 atom route | "coefficient-sensitive (F3)-Abel solution theorem" (Astra) | **REPLACE the target object**: (F3) is *identically* a factorization identity `Phi*Lam = Gee` in which `Phi = xW - b^2/4` and the C-side enters only through `K = x^2C - by`. Prove rigidity from the divisibility pair, not from Abel solution counts. | PROVED-HERE §1; the "Abel equation" framing hides that the equation is exactly `Phi | Gee` with `Gee` **W-free**. |
| D2 | K16 target strength | `B*W'(0)=0` (the atom) | **The atom is equivalent to `K | Gee`** — a divisibility of two explicit polynomials of degrees `t+1` and `4t+4`. Also: on `b != 0` the b=1 chart is *empty*, strictly stronger, and that is what the computation actually returns. | PROVED-HERE §1.3, MEASURED §1.5. |
| D3 | fixed-t compute status | "fixed-t Gröbner exhausted at t=7" (17(yyyy)) | **Downgrade that to 'exhausted in the frozen chart'.** A different chart with the same content decides t=5 in 54 ms and t=4 in 1 ms; the frontier is a chart property, not a t property. | MEASURED §1.5. |
| D4 | the 14 excess rows | "14 rows, 3 degrees x V-assignments" | **17 whole-tree survivors -> 5 descended classes; the 14 are <= 4 classes.** The sweep is 4 charts, not 14 rows. And `(84,56)` — one of the 17 — has `u_s = 2`, so the packet's "all 14 are u_s=1, radius-automatic" is a claim about the A.3 cut, not about the screen. | PROVED-HERE §2.1. |
| D5 | "the 14 rows are the residual" | asserted | **Three further residuals named and priced** (A.3 gate, condition-(3) branch, Moh's six printed rows). | §2.2. |
| D6 | (H1)/(H2) framing | `(census sweep) AND (K16-type rays) AND (routing maps)` | **The framing is missing the low-`l` regime.** Every kill the campaign owns is at `l = 4`; the residual classes are at `l = 1,2,3`, where the Jacobian band is nearly empty and the kill must come from incidence rows. | §3.1, §4.1. |
| D7 | binding routing map | unranked (`OPEN[ROUTING-MAPS]`) | **Rank them: receiver coverage is binding; first-separation is second; route-to-state and ordinary-support are downstream.** | §3.3. |

---
## 1. Q1 (K16, the atom): a new mechanism — (F3) *is* a factorization identity

### 1.1 PROVED-HERE: the master identity

Astra's (F3) (17(hhhhhh), `k16-8point1-astra-20260905.md` §4) is an Abel
equation of the second kind. **It is not really an ODE problem.** Put

```
  r  = b^2/4          Phi = x*W - r          (deg 2t+2)
  K  = x^2*C - y*b    M   = K + y*b = x^2*C  (deg t+1, monic; K(0) = -by)
```

Then, as a *rational-function identity in an arbitrary* `W`, `C`, and *free*
scalars `B`, `eta` (no use of (F1)), multiplying (F3) by `x^2` gives exactly

```
  Phi * Lam  =  Gee                                                    (F3')

  Lam = 2*x*Phi' - 3*Phi + (3/(2y^2))*K*M - B*x                  (deg 2t+2)
  Gee = (3/(16y^4))*K^3*(K + 2by) - (3/(4y^2))*B*x*K^2
        - (b*eta/(2y))*x^2*K - B*eta*x^3                         (deg 4t+4)
```

VERIFIED mechanically: `box/abelfact-20260905/verify_master.py` forms
`x^2*(LHS-RHS)` of (F3) with generic symbolic `W` (deg `2t+1`) and `C` (monic,
deg `t-1`) and subtracts `Phi*Lam - Gee`; the difference is **0** at `t=2,3,4`,
both with `B`,`eta` free and with `B=-W(0)`, `eta=W'(0)` imposed (6/6 zeros).

Four independent confirmations that (F3') is the right object, not an accident:

1. **`Gee` is `W`-free.** The whole `W`-dependence of the Abel equation sits in
   the single factor `Phi`. So (F3) says: *`Phi` divides an explicit polynomial
   built only from `(C, b, B, eta)`* — and `deg Gee = 2 * deg Phi` exactly.
2. **`Gee` is a quartic in `K`.** Writing `u = x^2C`, `v = by`, the
   `B`,`eta`-free part of `Gee` is `(3/(16y^4))*(u-v)^3*(u+v) = (3/(16y^4))*K^3*(K+2by)`
   — a perfect cube times a linear factor. `Gee` is a *binary quartic* in
   `(K, x)` with coefficients `1, 2by, -4By^2, -(8by^3/3)eta, -(16y^4/3)B*eta`
   (after scaling by `16y^4/3`).
3. **The scalars are the Taylor coefficients of `Phi`.** `Phi(0) = -b^2/4`,
   `Phi'(0) = -B`, `Phi''(0)/2 = eta`. So the atom `B*eta = 0` reads
   `Phi'(0) * Phi''(0) = 0` — a statement about one polynomial at one point.
4. **The leading coefficient of (F3') is the defining relation.** Comparing
   `x^(4t+4)` coefficients gives `(4t+1)om^2 + 3om/(2y^2) = 3/(16y^4)` with
   `om = 3(2d-1)/(4y^2(4t+1))`; `sympy` returns numerator `36d^2 - 12t - 12`,
   i.e. **exactly `3d^2 = t+1`** (`corollaries.py`, COR 3). A slip in the
   derivation would not reproduce `A_t`'s defining equation.

### 1.2 PROVED-HERE: the grading is the frozen grading

(F3') is weighted-homogeneous under

```
  wt(x)=1, wt(b)=t+1, wt(B)=2t+1, wt(eta)=2t, wt(phi_3)=2t-1,
  wt(c_i)=t-1-i   (C = c_0 + ... + c_{t-2}x^{t-2} + x^{t-1})
```

so `c_{t-2}` has weight 1, `c_{t-1-j}` has weight `j`, and `b` has weight
`t+1`. That is **verbatim** the frozen `wt(b4, u_2, ..., u_{t-1}, b_3) =
(1,2,...,t-1,t+1)` of `S_t` (Astra §1). The reformulation is not a change of
problem: `c_{t-2} = b4`, `c_{t-1-j} = u_j`, `b = b3`. Consequence: on `b != 0`
the `Gm`-action lets us **set `b = 1`** with no loss; `b = 0` is a separate
branch (the one Astra already isolates as "the simpler subcase").

### 1.3 PROVED-HERE: the atom is a divisibility, and there is a dual one

Reduce `Gee` modulo `K`: since `M = K + by`, all but the last term are
divisible by `K`, so

```
  Gee  ==  -B*eta*x^3   (mod K)      for t >= 3
```

(`corollaries.py` COR 1: remainder + `B*eta*x^3` is 0 at `t = 3,4,5`; at
`t = 2`, `deg K = 3` so `x^3` itself reduces — the t=2 anomaly is visible here
too and is exactly why the atom is stated for `t >= 3`). Since `K(0) = -by != 0`,
`gcd(K, x) = 1`, hence

> **RIGIDITY = DIVISIBILITY.** For `t >= 3` and `b != 0`:
> `B*eta = 0` **if and only if** `K | Gee`. If `eta = 0` then `K^2 | Gee`;
> if `B = 0` then `K | Gee`. Otherwise `gcd(K, Gee) = 1`.

Dually, reducing (F3') modulo `K` (using `M == by`, and the fact that all the
`b`,`B`-terms cancel identically — checked by hand and by COR 1) gives

```
  K  |  2*x*Phi*Phi' - 3*Phi^2 - B*x*Phi + B*eta*x^3
```

so at every root `theta` of `K`:
`(W(theta) - r/theta) * (2*theta*W'(theta) - W(theta) + 3r/theta - B) = -B*eta*theta`.

Taking the product over the `t+1` roots of the monic `K` and using
`Res(K,f) = Res(K, f mod K)` for monic `K`:

> **NORM LAW.** On any solution of (F1)-(F3) with `b != 0`,
> `Res(K, Phi) * Res(K, Lam) = -(B*eta)^(t+1) * b^3 * y^3`.

This is a *coefficient-sensitive* statement of exactly the kind the named next
step asks for, but it is a **norm identity in `A_t`**, not a solution count:
`(B*eta)^(t+1)` is pinned to a product of two resultants divided by `-b^3y^3`.
Both resultants are explicit polynomials in the `t+2` free coordinates.

### 1.4 The mechanism I propose (and why it dodges every refuted route)

`Lam` is not independent of `Phi`: `Lam = 2xPhi' - 3Phi + (3/2y^2)KM - Bx`.
Substituting and writing `P = Phi^2`, (F3') becomes

```
  x*P' - 3*P  =  Gee + Phi*(B*x - (3/(2y^2))*K*M)
```

The operator `x d/dx - 3` is **diagonal**, with eigenvalue `(n-3)` on `x^n`.
Therefore the coefficient equation at `x^n` **solves for `phi_n`** whenever
`n != 3` (the coefficient of `phi_n` is `(n-3)*2*phi_0 = -(n-3)b^2/2`, a unit
off `b = 0`), and the equations at `n = 0,1,2,3` are **vacuous identities**
(verified: all four cancel identically). Hence:

> **RECURSION THEOREM (PROVED-HERE).** For `b != 0`, a solution of (F1)-(F3) is
> uniquely determined by the `t+3` scalars `(b, B, eta, phi_3, c_0..c_{t-2})`
> via an explicit first-order recursion; the *entire* content of the atom is
> the **truncation condition** `phi_n = 0` for `n = 2t+3, ..., 4t+4`
> (`2t+2` equations; `n > 4t+4` is then automatic). Codimension of the
> expected solution set: `(2t+2) - (t+3) = t - 1`.

This is a *termination* problem for a recursion with an invertible symbol whose
only denominators are `(n-3)` and powers of `b^2`, `y`. That is a different
category of argument from everything on the refuted list — weighted Fröberg,
triangular coprime-leaders, degree-only Bézout/resultant, the pure degree-bound
tower are all **static** (Hilbert-series / degree) arguments; a recursion
termination argument is **dynamic**, and it is exactly the setting in which
p-adic (Dwork/Katz globally-bounded, or elementary `p`-divisibility of
`(n-3)^{-1}`) methods bite. Note the campaign's own `p = 4t+1` regularity
(memory `k16-4t1-padic-regularity`) and the fact that `4t+1` **cancels** out of
`lc(Lam) = 3(2d-1)/(4y^2)` — the recursion's symbol is regular at `4t+1`, so if
a p-adic obstruction exists it is at `p | (n-3)` for `n` in the truncation
window `[2t+3, 4t+4]`, i.e. `p in [2t, 4t+1]`. **That window is where I would
look.**

### 1.5 Cheapest decisive test — and what it already returns (MEASURED)

The reformulation is testable *today* because (F3') is a small, sparse,
quadratic system. `box/abelfact-20260905/abel_direct.sing` builds it over
`F_p` at `b = 1` (`3t` unknowns `B, eta, f_3..f_{2t+1}, c_0..c_{t-2}`;
`4t` equations = the coefficients of `Phi*Lam - Gee`), and runs `std` twice:
raw, and with the Rabinowitsch row `1 - z*B*eta`.

```
t=3  p=30013 fib=0  eqs=12 vars= 9   RAW dim=-1 (UNIT)    0 ms   RABINOWITSCH unit=1    0 ms
t=4  p=30059 fib=0  eqs=16 vars=12   RAW dim=-1 (UNIT)    0 ms   RABINOWITSCH unit=1    1 ms
t=5  p=30047 fib=0  eqs=20 vars=15   RAW dim=-1 (UNIT)   54 ms   RABINOWITSCH unit=1   61 ms
```

Two things to read off. (i) The chart returns the **strictly stronger** result
`RAW = unit ideal`: on `b != 0` the terminal cone is *empty*, not merely
`B*eta = 0`. (ii) `t = 5` in 54 ms where the frozen chart needed a dedicated
modular run (17(yyyy)); **the "fixed-t Gröbner is exhausted at t=7" verdict is a
property of the frozen chart, not of `t`.** (A companion route — substituting
the recursion of §1.4 to get `t+2` unknowns and `2t+2` equations — is
MEASURED **worse**: the `phi_n` densify and the build alone does not finish at
`t = 4` in 100 s. Reported as a negative result: use the direct sparse
coefficient system, not the substituted one.)

**THE CHEAPEST DECISIVE TEST (one lane, hours not days), in order:**

1. Run `abel_direct.sing` at `t = 6..12`, both fibres, three split primes each.
   Cost: minutes each if the `t=5` scaling holds. **This directly attacks
   `OPEN[K16-T11-FIBRE]`** (`t = 11`, `t+1 = 3*2^2`, the falsification target),
   which is the one place the atom could be *false*.
2. Promote whichever `t` come back unit to exact `Q(sqrt(3(t+1)))` with the
   Rabinowitsch certificate — the campaign's standard `UNIT_IDEAL_CHAR0`
   discipline. (Note: emitting over `Q(w)`, `w = 3d`, `w^2 = 3(t+1)`, needs
   coefficient-size care — Singular's algebraic-extension arithmetic stalled
   on the naive integer-cleared emission; use `p`-adic lifting or `modstd`.)
3. Only then attack the uniform-in-`t` statement, with the truncation window
   `n in [2t+3, 4t+4]` and the `t-1` excess equations as the target.

**Bounded quantities.** (F3') unknowns `3t` (at `b=1`), equations `4t`, excess
`t`; after the recursion substitution, unknowns `t+2`, equations `2t+2`, excess
`t-1`. `deg Gee = 4t+4`, `deg Phi = deg Lam = 2t+2`, `deg K = t+1`. The norm
law has RHS `-(B*eta)^(t+1) b^3 y^3`. Decision cost measured: `t=3` 0 ms,
`t=4` 1 ms, `t=5` 54 ms, `t=6` > 120 s at `p = 30013`.

**What would refute me.** If at some `t` the RAW ideal has `dim >= 0` with a
point at `B*eta != 0`, the atom is false at that `t` and (T) fails on the ray.
The chart is small enough that this is now a *decidable* question per `t`.

---
## 2. Q2 (full Moh <= 100): the 14 rows are **4 charts**, and they are not the only residual

### 2.1 PROVED-HERE: the excess rows collapse 17 -> 5 descended classes

I re-ran the descent law (`u_s = d_s - V_s`, `(n',m') = ((n/d_s)u_s, (m/d_s)u_s)`,
`l = d_s - 1 - 2u_s`; my 17(eeeeee)(2) result) on the **whole-tree-screen
survivor list** as banked in `box/mohprog-drivers-20260903/tree-independent-notes.md`
(the 23-line file, sha `f7e9fb5c...`, "six printed rows plus" 17 excess),
recovering each row from the frozen enumerator
(`independent_enumerator.py`, `numerical_skeletons(n, fixed_m=m)`): **17/17
matched, 0 missing** (`box/abelfact-20260905/descend14.py`).

```
(n,m)     M                 d-chain               d_s V_s u_s  (n',m')   l
84,56     (70, 77, 82)      (84,28,14,7,1)         7   5   2   (24,16)   2
90,60     (10, 45, 88) x2   (90,30,10,5,1)         5   4   1   (18,12)   2
90,60     (45, 80, 88) x2   (90,30,15,5,1)         5   4   1   (18,12)   2
96,64     (48, 68, 94) x3   (96,32,16,4,2)         4   3   1   (24,16)   1
96,64     (-48,-8,20,94)    (96,32,16,8,4,2)       4   3   1   (24,16)   1
96,64     (80,88,92,94)     (96,32,16,8,4,2)       4   3   1   (24,16)   1
96,72     (-60, 56, 94)     (96,24,12,4,2)         4   3   1   (24,18)   1
96,72     (36, 80, 94) x2   (96,24,12,4,2)         4   3   1   (24,18)   1
96,72     (84, 88, 94)      (96,24,12,4,2)         4   3   1   (24,18)   1
96,72     (36, 78, 94) x3   (96,24,12,6,2)         6   5   1   (16,12)   3
```

**DISTINCT DESCENDED CLASSES `(n',m',l)`: 5, from 17 rows** —
`(18,12,2) x4`, `(24,16,1) x5`, `(24,18,1) x4`, `(16,12,3) x3`,
`(24,16,2) x1`. The A.3 local-nondegeneracy cut takes `23 -> 20`, i.e.
`17 -> 14` excess; **the 14 therefore live in at most 4 classes.**

Two consequences the packet's framing misses:

* **The sweep is 4 charts, not 14 rows.** Rows inside a class share
  `(n', m', l)` and differ only in `V_2'`; per memory `band-engine-pivot-ledger`
  and 17(eeeeee) the descended chart is determined by `(n',m',l,V_2')`, so the
  work is 4-6 charts, each in the size class the `guided_gb` + lower-band
  method already closes (`(24,16)` **is** the D=108 descent target, 17(aaaaa)).
* **`(84,56)` has `u_s = 2`, not 1.** The packet says the 14 are "all `u_s = 1`
  so radius-automatic". That is true only if `(84,56)` is one of the three rows
  the A.3 cut removes. **This is a falsifiable claim and it should be checked
  before the "radius-automatic" line is repeated**: if `(84,56)` survives A.3,
  then a `u_s = 2` descent re-enters and 17(gggggg)'s
  window-exhaustion architecture must be redone for `(24,16; l=2)`.
  Cheapest test: run the A.3 predicate of `tree-independent-notes.md` §"A.3
  local and cyclic-quotient passport" on that single row — minutes.

### 2.2 Q2 answer: NO, the 14 rows are not the only residual

Three further residuals, each of which must be discharged before "Moh <= 100 is
closed" is sayable:

1. **`OPEN[A3-REALIZABILITY]` (new).** The `17 -> 14` cut is the A.3 *local
   nondegeneracy*, and the same banked note says in terms: "exact A.3
   *polynomial realizability* remains open; the two divisor/passport
   consequences do not recover Moh's output". So the campaign's own 14 is
   `17 minus an ungated screen`. Either gate A.3 or kill 17 rows (5 classes).
   Price: 3 extra rows = at most 1 extra class (`(24,16,l=2)`), so **killing 17
   instead of 14 costs one chart** — cheaper than gating A.3. **Do that.**
2. **The condition-(3) branch.** 17(ffffff) is careful and explicit: the (99,66)
   closure is *under condition (3)* (degrees not simultaneously reducible), and
   the simultaneously-reducible case "is a lower-degree instance of <= 100".
   That instance is not itself discharged anywhere I can find; it needs an
   explicit induction-bottoming statement. Cheap (it is bookkeeping), but it is
   *unwritten*, and a paper-grade `<= 100` theorem cannot omit it.
3. **Moh's six printed rows are cited, not re-killed.** 17(bb) reports the
   Appendix-2 compiler `SATURATED-EMPTY` on the *in-budget* two-point printed
   rows only. If the intended claim is "Moh <= 100 verified", the six printed
   rows need the same treatment as the excess; if the claim is "Moh's proof
   plus our completion", say so. This is a *scope* item, not a mathematical
   gap.

### 2.3 Is the descended-class sweep the right way? Yes — with one warning

Right, because the classes are `(18,12)`, `(24,16)`, `(24,18)`, `(16,12)` —
all smaller than `(27,18)` (the (99,66) case-(A) descent) and `(24,16)` is
already built. Warning, and it is the substantive one:

> **All four classes sit at `l = 1, 2, 3`. Every kill the campaign owns is at
> `l = 4`.** `l` is the descended Jacobian exponent (`l = v_s - u_s - 1`,
> 17(dddddd) ERRATUM). At `l = 1` the Jacobian band is nearly empty: the
> `(99,66)` schedule kills at stages 4 and 8 via *pole/Jacobian* rows, and
> 17(aaaaa) already found that D=108's branch dies instead at stage 0 on
> *incidence* rows. At `l <= 2` I expect the Jacobian rows to be vacuous and
> the kill (if any) to be forced entirely through the parameterized incidence
> compiler. **Predicted failure mode of the running lane: `POSDIM` /
> underdetermined charts at `l = 1`, not timeouts.**

**Uniform argument across the 14?** There is one *available*, and it is not the
one the packet implies. The three degree pairs are `90,60 = 30*(3,2)`,
`96,64 = 32*(3,2)`, `96,72 = 24*(4,3)`; twelve of the fourteen are on the same
`m/n = 2/3` ray as `(99,66) = 33*(3,2)`. But the descended data do **not**
share a line: `2K' + 3l` takes values `18, 19, 19, 22` and `(16,12)` is not
`n' = 3K'` at all. **So there is no single (K,l)-line argument for the 14** —
the honest answer to "is there a uniform argument across the 14" is
**no, but there is a uniform argument across each of the 4 classes**, which is
what a class sweep is. Anyone claiming a single uniform kill should be asked
which line it is; `2K'+3l = 30` is not it.

### 2.4 Price for full `<= 100` closure

**Superseded in part by §13.** My estimate at the time of writing: 5 descended
charts (`(18,12,2)`, `(24,16,1)`, `(24,16,2)`, `(24,18,1)`, `(16,12,3)`), of
which `(24,16)` has built infrastructure (D=108, 17(aaaaa)); plus one lane for
an incidence compiler at `l <= 2`; plus one gated note for the condition-(3)
branch; A.3 costs 0 because killing 17 rows is cheaper than gating it. The
operative price is 17(jjjjjj)'s: **89 chart instances at 78-335 unknowns**, i.e.
my chart count is a coarse-key undercount. What stands is the *shape* of the
answer — classes and instances, plus one unwritten induction note — not the
integer.

---

## 3. Q3 ((H1)/all degrees): the lattice is right; the ray is the wrong cofinal object

### 3.1 The path, and where it actually breaks

The proposed decomposition — **(descended-class census sweep) + (cofinal
K16-type rays) + (routing maps)** — is right in outline and wrong in one
detail that matters.

*Sweep.* Sound and mechanizable. `16 <= n <= 200`, `u_s >= 2`: `6209 -> 1359`
classes (4.57x), or `586` with `V_2'` a parameter (10.6x) (17(eeeeee)(2)).
Plus the `u_s = 1` stratum, which §2.1 shows compresses at least as hard (17
rows -> 5 classes = 3.4x on a tiny sample). A sweep over `(K, l)` lattice
points with `V_2'` a parameter is the correct engine. Bounded: **~586 charts**
to `n = 200`, of which the campaign has closed `l = 4` at `K = 7, 8, 9`.

*Rays.* Here is the detail. The k=4 ray is the slice `l = 4`; K16 is a ray in
that slice. **Cofinality is in `K`, but the census is unbounded in `l` too.**
`l = d_s - 1 - 2u_s` grows with `d_s`, so a census bounded in `n` is bounded in
`l`, but the *all-degree* statement needs every `l`. So "the cofinal rays" is
not one family indexed by `K`; it is a **two-parameter family indexed by
`(K, l)`, and the campaign has structural results for exactly one value of `l`.**
Worse for the near term (§2.3): the residual `<= 100` classes are at
`l = 1, 2, 3` — *below* the studied slice, where the Jacobian band thins out.
So the lattice has three regimes, not two:

| regime | status | what is needed |
|---|---|---|
| `l = 0, 1, 2` (thin Jacobian) | **unstudied**; contains the `<= 100` residual | incidence-driven kills; expect POSDIM from Jacobian-only charts |
| `l = 3, 4` (the studied slice) | `K = 7, 8, 9` closed; K16 is the atom at `K = 16` | the (F3')/rigidity theorem (§1) |
| `l >= 5` | unstudied | presumably easier (more Jacobian rows), unverified |

**The single most useful census experiment, and it is cheap:** run the descent
law over `16 <= n <= 200` and **tabulate the class count by `l`**. If the mass
sits at low `l`, the campaign's entire structural investment is in a thin
slice. Cost: one run of the frozen enumerator + `descend14.py`'s descent block
(minutes; my script already does it for a row list). I did not run the full
census in this lane (budget), so this is a **typed prediction**, not a
measurement: `PREDICT[l-MASS-LOW]`.

### 3.2 What the K16 reformulation buys the census

§1 is not only a K16 result. `(F3')` was derived from the *terminal normalized
receiver chart* of one ray. If the derivation is ray-generic — i.e. if the
elimination of `U', V'` from `D2, D1` that produced (F5) is available on every
`(K, l)` ray — then **every ray has its own `Phi | Gee` divisibility with its
own `K`**, and the census becomes a family of divisibility problems rather than
a family of Gröbner problems. Testing that is a well-posed, bounded question:
redo Astra §4's elimination on the `l = 4, K = 8` (D=108) ray and see whether
the same three structural facts survive (`Gee` W-free; `Gee` a quartic in `K`;
`x d/dx - 3` diagonal). **`OPEN[F3PRIME-RAY-GENERICITY]`.** This is the highest
-leverage question I can name, because a positive answer converts the
structural half of the census into one theorem.

### 3.3 Which routing map is binding — ranked

The packet leaves the four jointly `OPEN[ROUTING-MAPS]` and unranked. Ranked by
what each would have to supply and by failure mode:

1. **Receiver coverage — BINDING.** The others map *into* an already-fixed
   target; coverage is the claim that the two-point `M_s = n-2` stratum receives
   *all* the JC2 configurations the reduction claims to dispose of. A gap here
   is a **missing case**, not a repairable constant.
2. **First-separation — second.** FALLACY-v2 states that
   `REPRESENTATIVE != FULL_ACTUAL_EXIT` and that the latter supplies a floor,
   never attainment; the reduction consumes it as an equality somewhere. A
   known floor/attainment hazard with a named guardrail, i.e. auditable.
3-4. **Route-to-state, ordinary-support — downstream.** FALLACY-v2's own remedy
   ("missing route-to-state data means fallback") means the failure mode is
   degradation, not unsoundness.

**Cheapest test for the binding one:** do not try to prove coverage — try to
**falsify** it. Exhibit, or fail to exhibit in a bounded search over the
`n <= 60` census, one Keller configuration with `M_s = n-2` that no declared
receiver chart accepts. A day's work, and worth more than another structural
lane, because it is the only one of the four whose failure mode is fatal rather
than lossy.

---

## 4. Q4 (the finish / framing): where the framing is wrong

### 4.1 The challenge

`(H1) AND (H2)` reduces the **two-point `M_s = n-2` stratum along Moh's line**.
The packet says so honestly. My challenge is not to the scope disclaimer; it is
to the *decomposition inside* the scope.

> **The claim "two-point stratum = (census sweep) AND (K16-type rays) AND
> (routing maps)" is missing a case: the low-`l` regime.**

Concretely (§2.1, §3.1): the four descended classes that carry the residual of
Moh's own `<= 100` theorem sit at `l = 1, 2, 3`; the entire structural theory
(k=4 ray, D=108, case (A), K16) sits at `l = 4`. "Census sweep" is being asked
to absorb a regime in which the sweep's kill mechanism (top pin + lower-band
parametrization -> ~36 vars -> `guided_gb`) has **never been run** and where I
predict it returns POSDIM rather than a kill (memory
`guided-gb-perturbed-control-vacuous-on-cones`: on a positive-dimensional chart
the bad-hint control never fires and the run is *rejected*, not informative).
So the framing hides a third leg.

Second, smaller challenge: the packet calls K16 "the one true structural OPEN".
After §1 that is arguably no longer the right description — K16 is now a
*decidable-per-`t`* question in a chart that runs in milliseconds at `t <= 5`.
The genuinely undecided structural object is **uniformity in `t`**, and the
uniform statement I would now aim at is not "no solution" but the divisibility
`K | Gee` / the norm law `Res(K,Phi)Res(K,Lam) = -(B eta)^{t+1} b^3 y^3`.

### 4.2 The single most valuable next object

> **The `(K, l)`-lattice *fibred over `l`*, with the `(F3')` divisibility
> attached to each ray — i.e. "does every ray carry a `Phi | Gee`?"**

Not the census table (that is data), not the K16 atom (that is one point).
The object is the assignment `ray -> (K_ray, Gee_ray, divisibility)`. It is
valuable because (a) it subsumes K16 as one fibre, (b) it is *testable at one
extra ray today* (D=108, `l=4, K=8`), and (c) a positive answer replaces the
structural half of the all-degree program with a single theorem, leaving the
census sweep purely mechanical. If the answer is negative — some ray has no
`W`-free `Gee` — that is *also* decisive: it says K16 is special and the
all-degree route must be the sweep alone, which changes the campaign's
resource allocation immediately.

---
## 5. Three idea cards

### CARD A — `Phi | Gee`: the K16 atom as a polynomial divisibility (PRIMARY)

* **Claim.** (F3) is identically `Phi*Lam = Gee` with `Gee` W-free and quartic
  in `K`; the rigidity `B*W'(0) = 0` holds **iff** `K | Gee`; on solutions
  `Res(K,Phi)*Res(K,Lam) = -(B*eta)^(t+1)*b^3*y^3`.
* **Status.** Master identity PROVED-HERE and machine-verified (0/6 residual,
  `verify_master.py`); COR 1 and COR 3 machine-verified; the norm law is a
  derivation from those two (not independently machine-checked on a solution,
  because no solution exists to check it on — see the fallacy note in §8).
* **Why it is new.** All five prior K16 lanes treated the terminal cone as
  ideal membership in `S_t`. (F3') makes it a *factorization* of one degree-`4t+4`
  polynomial into two halves of degree `2t+2`, with the atom a divisibility by a
  *third* polynomial of degree `t+1`.
* **Cheapest test.** `box/abelfact-20260905/abel_direct.sing`, `t = 6..12`, both
  fibres. MEASURED so far: `t=3` 0 ms, `t=4` 1 ms, `t=5` 54 ms, all RAW-unit.
* **Kill condition.** A `t` with `RAW dim >= 0` and a point at `B*eta != 0`.

### CARD B — the low-`l` regime: charts where the Jacobian band is empty

* **Claim.** The residual of Moh `<= 100` sits at `l = 1, 2, 3`, and every kill
  the campaign owns is at `l = 4`. At `l <= 2` the Jacobian rows are (I predict)
  vacuous and the kill must come from incidence rows, as already observed once
  (17(aaaaa), D=108 dying at stage 0 on common-`h_3` minor incidence).
* **Status.** The `l` values are PROVED-HERE (`descend14.py`, 17/17 rows
  matched). The vacuity prediction is **typed, unmeasured**.
* **Cheapest test.** Take the single class `(24,16; l=1)` (5 of the 17 rows),
  emit its chart with the existing staged emitter, and **count the Jacobian
  band rows**. If that count is 0 or the chart is positive-dimensional after
  the Jacobian band, the prediction holds and the incidence compiler is the
  critical path. One run, minutes; no new machinery.
* **Value.** It tells the `<= 100` lane whether it is 3 days or 3 weeks from
  done, before the lane spends the time.

### CARD C — `l`-fibred census: is the campaign's structural theory in a thin slice?

* **Claim.** The `(K, l)` lattice's mass is not uniformly distributed in `l`,
  and the studied slice `l = 4` may be a small fraction of the `n <= 200`
  census.
* **Status.** Typed prediction `PREDICT[l-MASS-LOW]`; not measured here.
* **Cheapest test.** Run the frozen enumerator over `16 <= n <= 200` (already
  done once for 17(eeeeee): 6209 rows) and histogram by `l`. Minutes; the
  descent block is 6 lines and is written (`descend14.py`).
* **Value.** Resource allocation. If `l = 4` is 5% of the census, "the cofinal
  rays" is not a finishing move and the sweep must carry the weight.

---

## 6. The single first lane

**`k16-abelfact-<model>`** — *not* a K16 structural lane; a **chart-form** lane.

* **Charge.** Independently re-derive the master identity (F3') from Astra's
  (F3) as printed (do not take mine on trust — re-run `verify_master.py` and
  also derive it by hand); then run `abel_direct.sing` at `t = 6, 7, 8, 9, 10,
  11, 12`, both fibres, three split primes each, with a hard per-run cap; then
  attempt exact `Q(sqrt(3(t+1)))` promotion at every `t` that returns unit,
  using `modstd`/rational reconstruction rather than naive integer-cleared
  emission into `Singular`'s algebraic extension (which stalls).
* **Why this first, ahead of any structural K16 lane.** It is the only lane that
  can *falsify* the atom (`OPEN[K16-T11-FIBRE]`), it is cheap, and it settles
  whether the frozen-chart frontier `t = 7` was ever a real frontier.
* **Receipts.** Per `t` and fibre: `eqs`, `vars`, `RAW dim`, `size`, ms, and the
  Rabinowitsch unit flag. Exact-`Q` runs additionally report the certificate
  row and its coefficient, per the campaign's `UNIT_IDEAL_CHAR0` discipline.
* **Success.** `t = 11` decided (either way). **Stretch.** A `t` where the
  method visibly saturates, which localises the uniformity problem.

---

## 7. The two running lanes (receipts only — neither `.run.v2` has `final_status`)

### `moh100-14rows-opus5` — **CONTINUE, with one amendment**

The lane's direction (descend + kill the excess rows) is right and it is on the
critical path for the `<= 100` headline. Amendment, decidable from its receipt
without reading it: **the target is 5 descended classes, not 14 rows** (§2.1),
and one of the 17 screen survivors, `(84,56)`, has `u_s = 2`. Two receipt
checks the coordinator can apply on seal:

* Does the report kill **classes** or **rows**? If rows, the lane is doing
  3-4x redundant work and its successor should be class-indexed.
* Does it state the `l` of each class? If it reports kills at `l = 1` **by
  Jacobian rows**, that contradicts my §2.3 prediction and I am wrong — good
  outcome, and it should be recorded as such. If it reports POSDIM at `l = 1`,
  Card B is confirmed and the incidence compiler is the next lane.

### `k16-f3abel-astra` — **REDESIGN (retarget, do not stop)**

Astra's named next step is "a coefficient-sensitive polynomial solution theorem
for the (F3) Abel equation, using the linked coefficients `A = 3x^3C^2/(4y^2)`,
`D = 3bxC/(2y)` and fixed leading `omega`". §1 says the linkage between `A`
and `D` is not a coefficient coincidence to be exploited *inside* an Abel
solution theory — it is the statement that `A - D = (3xC/(4y^2))*(x^2C - 2by)`
and hence that the whole equation collapses to `Phi | Gee`. **A solution theory
for Abel equations is a strictly harder object than the atom needs.** Retarget
to: (i) `K | Gee` as the rigidity, (ii) the norm law, (iii) the truncation
recursion of §1.4 with its `[2t+3, 4t+4]` window. Do not stop the lane — if it
has already found (F3') independently, the two derivations gate each other,
which is worth more than either alone.

*Caveat I owe the reader:* I have not read that lane, so it may already be
doing exactly this. "Redesign" here means "the charge as written aims past the
target", which is a statement about the charge, which I *have* read (the
17(hhhhhh) NEXT STEP text), not about the lane's work.

---

## 8. One systems upgrade

**`ops/chartform.py` + a promotion rule: a TIMEOUT is never a frontier.**

Motivation, measured this round: 17(yyyy) recorded "`t = 7, 8, 11` TIMEOUT at
STD_START ... Fixed-t Gröbner is exhausted at `t = 7`; larger `t` need the
structural route". That verdict then shaped **four** lanes' scope. But a
different chart with identical mathematical content decides `t = 5` in 54 ms
and `t = 4` in 1 ms (§1.5). The frontier was a property of the chart form, and
the ledger recorded it as a property of the problem.

The upgrade, small and mechanical:

1. Any report asserting a compute frontier (`TIMEOUT`, `EXHAUSTED`,
   `INFEASIBLE`) must emit a `chartform` block: `{vars, eqs, ring, grading,
   ordering, dehomogenised_at, saturation}`. `ops/` rejects the seal otherwise.
2. Such a verdict is typed **`FRONTIER-CHART-CONDITIONAL`** and may not be
   cited as a reason to abandon a route until a **second chart form** (different
   variable count or different grading, same content) reproduces it.
3. `ops/chartform.py --compare A B` prints the two blocks side by side, so a
   reviewer can see at a glance whether "the same computation" was attempted.

Cost: a schema and ~80 lines. It would have saved this campaign four lanes'
worth of scope-narrowing, and it is exactly the guardrail FALLACY-v2 lacks
(FALLACY-v2 covers *mathematical* substitution errors; this covers *computational*
ones, where "the machine could not do it" silently becomes "it cannot be done").

---
## 9. Fallacy audit (FALLACY-v2)

* **Not engaged** (no such object appears in this report): flag/place/series;
  per-ray/exit-set charge (no exit claim is made, so no `charge_basis` line is
  owed or emitted — §1-§4 assert no new exit price and consume no promoted one);
  merge-free/M-descent (Statement 8.5 is not invoked); target/arrival index.
* **Carrier/attainment.** §2.1's descended classes are *carriers* of the rows,
  not kills; I claim only that the rows collapse to 5 classes, never that a
  class is dead.
* **Pole/interior.** (F3')'s only pole is the one Astra removes (`-b^2/(4x)`);
  I use `Phi = xW - r` after that removal, and every division by `x` in the
  derivation is justified by an explicit vanishing (`A` divisible by `x^3`,
  `B + W` by `x`), machine-checked by the identity test.
* **Floor/attainment.** §1.3's norm law is an *equality on solutions*, derived
  from `Gee == -B*eta*x^3 (mod K)`. It is **not** a floor and I do not use it
  as one. It is also **not** independently verified on data: a random
  `(W, C, B, eta)` does **not** satisfy (F3'), so a numeric check of the norm
  law on random data is meaningless — I ran one, it failed as expected, and I
  report that here rather than suppressing it. What *is* machine-verified is
  the two inputs (COR 1 and the master identity); the norm law follows from
  them by multiplicativity of the resultant and `Res(K,f) = Res(K, f mod K)`
  for monic `K`.
* **`sat()` wrapping.** No `sat()` is used. The `b != 0` localisation is done
  by dehomogenising at `b = 1` under a *proved* `Gm`-grading (§1.2), and the
  `B*eta != 0` localisation by an explicit Rabinowitsch row, with the raw
  (unlocalised) ideal reported alongside in every run.
* **Raw remainder degree.** COR 1 is a division in `F[x]` by the **monic** `K`,
  so no leader can vanish; the `t = 2` case where the remainder differs is
  reported explicitly rather than smoothed over.
* **Variable/ring map.** §1.2 declares the map `c_{t-2} = b4`,
  `c_{t-1-j} = u_j`, `b = b3` and justifies it by matching the *weights*
  `(1, 2, ..., t-1, t+1)`, not the names. The field is
  `A_t = Q(w)/(w^2 - 3(t+1))` with `w = 3d`; modular runs fix a square root of
  `3(t+1)` mod `p` and run **both fibres** (`FIB = 0, 1`).
* **Prime label/derivative.** `Phi'`, `W'`, `C'` are genuine `d/dx`
  (Astra's (F3) defines `W'` as a derivative). `V_2'`, `n'`, `m'`, `M_2'`,
  `d_j` primes in §2-§3 are **labels** (descended data), not derivatives; the
  two usages are kept in disjoint sections.

**Additional self-checks I owe.** (a) The master identity was verified with
`B`, `eta` *free*, so it does not smuggle in (F1). (b) The leading-coefficient
check independently reproduces `3d^2 = t+1`. (c) All 17 rows of §2.1 were
recovered from the frozen enumerator, not transcribed. (d) The modular results
are **screens**, not char-0 certificates; I do not claim `UNIT_IDEAL_CHAR0` at
any `t` from a mod-`p` run.

---

## OPENS RAISED

* `OPEN[F3PRIME-RAY-GENERICITY]` — Does every two-point ray carry a `W`-free
  factorization `Phi*Lam = Gee` with `Gee` a quartic in its own `K`, or is K16
  special? QUANTITY: the number of rays for which the Astra §4 elimination
  reproduces the three structural facts is at least 1 and at most the size of
  the `(K,l)` lattice; the decisive next datum is the single ray `l = 4`,
  `K = 8` (D=108). Cheapest test: redo the `D2, D1` elimination on that ray and
  compare `deg Gee = 4t+4` against `2*deg Phi`.
* `OPEN[K16-NORM-LAW]` — Can `Res(K,Phi)*Res(K,Lam) = -(B*eta)^(t+1)*b^3*y^3`
  be contradicted by a valuation or degree estimate on the two resultants?
  QUANTITY: `deg_x K = t+1`, `deg_x Phi = deg_x Lam = 2t+2`, so each resultant
  is a form of weighted degree at most `(t+1)*(2t+2)` in the `t+2` free
  coordinates; a lower bound on `v_p(Res(K,Lam))` exceeding `3*v_p(by)` would
  force `B*eta = 0`.
* `OPEN[L-LOW-REGIME]` — At descended Jacobian exponent `l <= 2`, is the
  declared two-point chart still determined? QUANTITY: the Jacobian band row
  count at `l = 1` is predicted to be at most 0 useful rows, against `l = 4`
  where it is the killing family; the residual of Moh `<= 100` is at least 14
  rows and at most 17, all in classes with `l <= 3`.
* `OPEN[A3-REALIZABILITY]` — The `17 -> 14` reduction of the whole-tree
  survivors uses Proposition A.3 local nondegeneracy, and exact A.3 polynomial
  realizability is recorded as open in the banked note. QUANTITY: the excess
  row count is at least 14 and at most 17; the extra descended classes cost at
  most 1 chart, so killing 17 is cheaper than gating A.3.
* `OPEN[MOH-100-REDUCIBLE-BRANCH]` — Moh's `<= 100` theorem under condition (3)
  is not the whole theorem; the simultaneously-reducible degrees reduce to
  lower-degree instances and that induction is not written down anywhere I
  found. QUANTITY: the number of unwritten induction steps is at least 1;
  the bottoming degree is at most 100.
* `OPEN[ORDCHART-SYMBOL]` — Does the `s' >= 3` order chart admit a linear
  operator in its own grading with invertible symbol, so that most unknowns are
  *determined* rather than solved for (as `x d/dx - 3` does for (F3'))?
  QUANTITY: the `s' >= 3` charts carry at least 78 and at most 335 unknowns
  across 89 instances (17(jjjjjj)); a symbol invertible off one hypersurface
  would leave at most the truncation window, which for (F3') is `2t+2` of `4t`
  equations. Cheapest test: one chart instance, look for a row family whose
  leading coefficient is a nonzero scalar multiple of a single unknown.

* `PREDICT[l-MASS-LOW]` (not an OPEN, a falsifiable prediction) — In the
  `16 <= n <= 200` census the class mass at `l = 4` is at most 25% of the
  total. Test: histogram the 6209 rows by `l`.

---

### Collision scan result

`python3 ops/open_collision.py xmodel/ideation-20260905T0200Z-opus5.md` ->
`status: CANDIDATES`. Five of the six raised OPENs return **NONE**.
`OPEN[MOH-100-REDUCIBLE-BRANCH]` returns candidates; I reviewed them and they
are **distinct**: the `reducible-branch-*` reports concern the *H2* reducibility
of `A_F` (17: "Moh's D <= 100 theorem itself has no H2"), not Moh's condition (3)
on *simultaneously reducible degrees*; the AUDIT 17(bbbbbb)-(jjjjjj) hits are
lexical matches on "Moh <= 100" and none of them states the reducible-degree
induction. The OPEN stands as raised. The scan also surfaced 17(jjjjjj), banked
after this lane began — see §13.

---

## 11. Reproduction

```
box/abelfact-20260905/
  input-manifest.sha256   generated from the .run.v2 with awk; sha256sum -c 4/4 OK
  verify_master.py        (F3) <-> (F3') identity, generic W and C, t=2,3,4     [0/6 residual]
  corollaries.py          COR 1 (Gee mod K), COR 2 (norm law, see §8), COR 3 (3d^2=t+1)
  descend14.py            17 screen-survivor rows -> 5 descended classes        [17/17 matched]
  abel_direct.sing        direct (F3') chart over F_p at b=1; RAW + Rabinowitsch
  abel_modp.sing          recursion-substituted chart (NEGATIVE result: densifies)
  abel_diag.sing          incremental-generator diagnostic
  sweep_hi.log            t >= 6 sweep (t=6 unfinished at seal; see below)
```

MEASURED at seal: `t=3` RAW unit 0 ms; `t=4` RAW unit 0 ms; `t=5` RAW unit
54 ms (`p = 30013 / 30059 / 30047`, fibre 0). `t=6` did not return within
120 s at `p = 30013` nor within the background window at `p = 1009`; **`t >= 6`
is UNDECIDED in this lane** and is the first item of the proposed lane (§6).
The `t = 3` result is also reproduced at `p = 32003` and at both fibres of
`p = 30013`.

---

## 12. What I would bet against

Ranked by how likely I am to be wrong: (1) **Card B's `l = 1` vacuity
prediction** — already weakened by §13(3), now ~35%; (2)
**`OPEN[F3PRIME-RAY-GENERICITY]` resolving positively** (~40%) — the
`(u-v)^3(u+v)` factorisation that makes `Gee` a quartic in `K` may be an
accident of `3d^2 = t+1` rather than ray-generic; (3) **the `t >= 6` sweep
finishing cheaply** (~50%) — `t=5` at 54 ms against `t=6` past 120 s is a bad
scaling signature, and the chart may hit the frozen chart's wall two steps
later. That would not touch §1's mathematics, but it would demote §1.5's "the
frontier is a chart property" from a general claim to a claim about `t <= 5`,
and I have stated it no more strongly than the measurements support.

---

## 13. ADDENDUM — state moved during this lane (AUDIT 17(jjjjjj), 02:16Z)

The collision scan (§10) surfaced a delta banked *after* I started:
**17(jjjjjj)**, the seal of `moh100-14rows-opus5`. I read the AUDIT entry only
(a banked canonical ledger, and the packet directs me to the AUDIT deltas); I
did **not** open the lane report or `box/moh14-20260905/`. Three corrections
and one reinforcement are owed.

**(1) My `(84,56)` flag (§2.1) resolves in the campaign's favour.** 17(jjjjjj)
reports `u_s = 1` on **14/14**, radius-automatic, with the descent map and the
descended-radius map validated fail-closed against Moh's own Appendix II table
(p.207, all five rows, both bracketed alternates). So `(84,56)` — the one
`u_s = 2` row among the 17 — is indeed removed by the A.3 cut. The packet's
"all 14 are `u_s = 1`" is correct. My §2.1 warning was a real hazard and it is
now discharged; I leave the reasoning in place because the *check* was the right
one to demand, and 17(jjjjjj) is the receipt that answers it.

**(2) My class count is coarser than the lane's, and the lane's is the
operative one.** I report **5 classes from 17 rows**; 17(jjjjjj) reports
**7 descended classes / 89 chart instances from 14 rows**. These are not in
conflict: my key is `(n', m', l)` and the lane's is finer (it must be, to reach
89 instances). **Use the lane's number.** What survives from §2.1 is only the
direction — the residual is class-indexed, not row-indexed — and 17(jjjjjj)
states that far more precisely than I did. Where §2.4 prices "full `<= 100` =
5 charts + 1 note", the correct price is **89 chart instances**, and my table
understates it.

**(3) My Card B / §2.3 prediction is not what happened.** I predicted the
`l <= 2` charts would come back **POSDIM** (Jacobian band vacuous). 17(jjjjjj)
reports the blocker is **compute**: `s' >= 3` order charts at **78-335 unknowns
x 89 instances**, exact-`Q` standard bases not finishing in a 180-minute
single-box lane. So the binding variable is descended *depth* `s'`, not
descended Jacobian exponent `l`. Card B is **not confirmed**; I would now rank
it below Card A and Card C. (It is not refuted either — nothing reported bears
on whether the `l = 1` Jacobian band is empty — but it is no longer the
question I would spend a lane on.)

**(4) Reinforcement, and it is the point I most want to leave behind.**
17(jjjjjj)'s genuinely new structural fact — *the operative screen is EXACT at
`s = 3` (212 rows -> Moh's six, zero excess), the whole residue is `s >= 4`
descending to `s' in {3,4}`, and Moh's four published Appendix II cases are all
`s' = 2`* — is a better characterisation of `OPEN[MOH-PROGRAM-ARTIFACT]` than
anything in §2, and it should be treated as the settled description: the
artifact is **exactly the descended-depth-`>= 3` shape Appendix II never
treats**. But note what the delta then does: it declares a compute frontier
("exact-`Q` standard bases do not finish") from **one chart form** — the
`s' >= 3` generalisation of the order chart — and routes to a fleet.

That is the second instance this round of the pattern §8 is about. §1.5 showed
`t = 5` moving from "needs a dedicated modular run" to **54 ms** by changing the
chart form with the content held fixed. Before spending 89 parallel exact-`Q`
solves at 78-335 unknowns, it is worth **one** cheap lane asking whether the
`s' >= 3` order chart has a `Phi | Gee`-style reformulation — a divisibility or
a recursion with an invertible symbol — that collapses the unknown count the
way (F3') collapses `I_{t,+}`. The fleet will work either way; it will just cost
89 times more if the answer was yes. **Concretely: apply §1.4's test — is there
a linear operator in the chart's own grading whose symbol is invertible off a
hypersurface? If yes, most of the 78-335 unknowns are determined, not solved
for.** That is `OPEN[ORDCHART-SYMBOL]` (§10), and it is a change to §6: keep
`k16-abelfact` as the first lane, and add **`ordchart-symbol-<model>`** as the
first *fleet-deferring* lane.

**Unchanged by 17(jjjjjj):** everything in §1 (K16), §3 (the `l`-fibred
lattice and the routing-map ranking), §4 (the framing challenge, whose low-`l`
leg is now weaker but whose ray/`l` two-parameter point stands), and §8.

---

*Seal.* Round 20260905T0200Z, seat OPUS. Inputs 4/4 verified by mechanical
manifest. No same-round submission and no in-progress lane report was read; the
one late banked item (AUDIT 17(jjjjjj)) is disclosed in §13. New artifacts in
`box/abelfact-20260905/`. `t >= 6` of the §1.5 sweep is UNFINISHED at seal and
is reported as undecided, not as a frontier.

<!-- BODY-END -->
