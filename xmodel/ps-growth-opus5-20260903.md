# PS-GROWTH / TRACE-CONSTANCY — the identity family proved, measured, and priced

Lane: flagship, Opus 5, 2026-09-03. Report for the charge
"prove PS-0..PS-3 and TRACE-CONSTANCY, build `psgrowth.py`, attack the residue
lower bound, verify RES-DEGREE, and read the route".

## 0. Custody

Charged inputs verified by SHA-256 against the frozen read-only copies in
`/tmp/jc2-lane.u6KapB/inputs` (7/7 OK) before anything was read:
`ideation-20260903T1015Z-opus5.md` `b13149ec`,
`ideation-20260903T1015Z-opus5-coordinator.md` `52af9fca`,
`integration17-coordinator-fable51-20260902.md` `126d9c84`,
`d1-subtree-opus5-20260902.md` `26479b06`,
`exact-n-rigidity-opus5-20260902.md` `e639fdbf`,
`census-rebase-opus5-20260902.md` `fb137b92`,
`box/tfe-drivers-20260902/bottomode.py` `69ff5bde`.
No other `ideation-20260903T1015Z-*` file was opened; no running lane's report
was opened; `jc2-lean` was not inspected; no canonical ledger was edited.
Files written: `box/psgrowth-drivers-20260903/` (new) and this report.
Also read (tooling, not reports): `box/moh_skeleton_N.py`,
`box/tfe-drivers-20260902/{control4.py,devcensus.py,pick105.log}`.

Types used below: **PROVED-HERE/UNREVIEWED**, **MEASURED**, **CONJECTURE**,
**SOURCE-UNVERIFIED**, **CORRECTION**.

---

## 1. Verdict, up front

```text
(1) PS-0, PS-1, PS-2, PS-3 and TRACE-CONSTANCY are TRUE and are PROVED HERE with
    exact hypotheses.  Two of them are stronger than charged:
      PS-1' : dP_{k+1}/dx = (k+1)[y^{n-1}](J f^k mod (g-c_2))  needs NO hypothesis
              on J at all; Keller enters ONLY to pull J out of the bracket.
      PS-3+ : deg_x R_k <= floor((k+1)c_max) - 1  (deg_x is an integer).
    1495 exact checks over Q on 10 Keller pairs and 6 non-Keller pairs, 0 failures.

(2) THE ROUTE IS NOT A CEILING ROUTE, AND THE REASON IS STRUCTURAL, NOT A GAP.
    PS-3 is an equality generically.  I compute the leading coefficient of R_k
    exactly (THEOREM RESIDUE-LEAD, sec.4) and it is NONZERO whenever an exponent
    congruence holds.  A bound that is attained cannot be contradicted, so no
    "residue lower bound" of the shape the charge asks for can exist: any lower
    bound exceeding (k+1)c_max - 1 is FALSE, with witnesses.

(3) THE ONE NEW THEOREM THE LANE PRODUCED IS THE LEADING COEFFICIENT ITSELF.
    THEOREM RESIDUE-LEAD.  At a bottom-major disc with Moh star (p_f, p_g) of type
    (d, e, V_2), the disc's contribution to the leading x-term of R_k is, up to a
    nonzero tower constant,
        S_k = sum_{p_g(pi)=0} p_f(pi)^k / p_g'(pi)  =  (d/kappa) * ptilde_{k+1},
        ptilde_j := sum_{p_g(pi)=0} p_f(pi)^j ,   kappa = BOTTOM-ODE's constant.
    The leading coefficient of R_k is a PS-GROWTH power sum ONE LEVEL DOWN, for
    the Davenport-Stothers pair of the bottom star.  Verified end-to-end on five
    genuine Keller pairs: the predicted set {k : PS-3 is ATTAINED} equals the
    measured set, 5/5, including the charged degree-15 composition.

(4) THE D = 105 TRIO IS NOT TOUCHED.  For group A (q = 1/2, e = 3, c_max = 1/6)
    PS-3 forces R_0..R_4 == 0 and R_5..R_10 in C[c_2] -- confirmed, with one
    correction to the charge (R_11 may have deg_x 1, not 0).  The vanishing is
    forced by EXPONENT ARITHMETIC ((k+1)c_max < 1), not by any coefficient
    cancellation: the per-disc star sum ptilde_{k+1} for the (2,3,1) star is
    NONZERO for every k >= 1 (MEASURED, saturated Groebner).  So NO identity among
    the top-form coefficients is forced and Davenport-Stothers extremality of the
    bottom star is NOT contradicted.  Answer to charge (3)(c): NO.

(5) OPEN[PS-VACUITY] IS ANSWERED, AND IT IS THE ROUTE'S EPITAPH.  R_k is not
    identically zero on Keller pairs (it is nonzero for a positive-density set of
    k on every control).  But the genuine Keller pair (x+y^5, y+(x+y^5)^3) -- the
    charged composition, n = 15, m = 5 -- has R_k == 0 for ALL k <= 13 and
    deg_x R_k = 0 for all k <= 20.  Its forced-vanishing range (13) is LONGER than
    the D = 105 trio's (4).  Long vanishing is what genuine Keller pairs do; it is
    evidence for nothing.

(6) RES-DEGREE AS CHARGED IS FALSE, AND THE CORRECTED FORM CARRIES NO NEW
    INFORMATION.  deg_x Res_y(g-c_2, f-c_1) = N for generic (c_1,c_2) -- that is
    CONTACT-DEFICIENCY restated.  deg_x Res_y(g-c_2, f) = N - shed_0 with
    shed_0 = sum over NON-PROPER branches of ord_t f(tau_i) >= 0, which is NOT
    sum_i (1-delta^0_i)^-.  REFUTATION WITNESS: g = y^3+xy, f = y+1 has
    sum_i (1-delta^0_i) = 0 and deg_x Res_y(g-c,f) = 1.  Consequently the proposed
    "ORTHO-DEFECT minus RES-DEGREE" skeleton kill test COLLAPSES: both sides price
    the same N.  Not run on the trio, because there is nothing to run.

(7) READING.  PS-GROWTH is a SHAPE CONSTRAINT on (e, q_max), never a ceiling, and
    on the frontier it is currently VACUOUS.  Structural reason: every quantity in
    the identity family is a function of (m, n, q_max, e); D = n = K*e and K is
    invisible to it.  Even a perfect residue floor yields e <= C(N), never D <= C(N).
    PIN-NOT-CEILING is NOT being over-applied here -- the ideation's rebuttal of it
    (sec.2.1 of the charged file) is withdrawn by this lane's own measurements.
```

---

## 2. The identity family, proved

### 2.1 Setting and the four hypotheses, separated

Let `k0` be a field of characteristic 0 (`C` below; nothing needs algebraic
closure except where the roots are named). Fix

```text
  f, g in k0[x,y] ,  g MONIC in y of degree n ,  m := deg_y f ,
  c a new indeterminate,   R := k0[x,c] ,   A := R[y]/(g - c) ,
  J := f_x g_y - f_y g_x ,
  chi(T) := Res_y(g - c, T - f)  in R[T] ,
  P_k := Tr_{A/R}(f^k) ,   R_k := [y^{n-1}]( f^k mod (g - c) ) .
```

The four hypotheses, and exactly what each buys:

| tag | hypothesis | what fails without it |
|---|---|---|
| **(MON)** | `g` monic in `y` of degree `n` | `A` is not `R`-free, `P_k` acquires denominators `lc_y(g)^j`, and `chi != prod_i (T - f(tau_i))` (a leading-coefficient factor appears). PS-0 fails. |
| **(SEP)** | `disc_y(g - c) != 0`, i.e. `c` generic | `Tr = sum over roots` and the Euler-Jacobi formula are unavailable. Automatic here: `Res_y(g-c, g_y)` is a nonzero polynomial in `c` of degree `n-1`. |
| **(KEL)** | `J in k0^*` | PS-1 as charged fails (PS-1' survives); PS-3 fails. |
| **(GAU)** | Moh's gauge: `f, g` monic in `y`, `deg = deg_y` for both, `m < n` | Only the *sharpened per-root* form (sec.2.7) and TRACE-CONSTANCY's `km <= n-2` clause need it. PS-0..PS-3 do not. |

`deg_y f = m < n` is **not** needed for PS-0..PS-3.

### 2.2 PS-0 (PROVED-HERE)

Under (MON), `g - c` is monic in `y`, so `A` is a free `R`-module with basis
`1, y, ..., y^{n-1}` (division with remainder). Hence `mu_f` (multiplication by
`f`) has a matrix over `R`, `chi(T) = det(T I - mu_f) in R[T]` is monic of degree
`n`, and `P_k = tr(mu_f^k) in R = k0[x,c]`. Under (SEP), over an algebraic closure
of `Frac R` we may name the roots `tau_1..tau_n` of `g - c` and then
`chi(T) = prod_i (T - f(x,tau_i))` (no leading-coefficient correction, by (MON)),
so `P_k = sum_i f(x,tau_i)^k` is the `k`-th Newton power sum of `chi`. ∎

### 2.3 The trace lemma (Euler-Jacobi / Lagrange)

> **LEMMA EJ.** Under (MON) + (SEP), for every `h in A`,
> `Tr_{A/R}(h/g_y) = [y^{n-1}](h mod (g-c))`, i.e.
> `sum_i h(tau_i)/g_y(tau_i) = [y^{n-1}] hbar` where `hbar` is the normal form.

*Proof.* `g_y(tau_i) = prod_{j != i}(tau_i - tau_j)` because `g - c` is monic with
simple roots. Lagrange interpolation of `hbar` (degree `<= n-1`) at the `tau_i`
and comparison of the `y^{n-1}` coefficients gives the identity; both sides are
`R`-linear in `h` and `h` and `hbar` agree at every `tau_i`. ∎

So `R_k = Tr(f^k/g_y)`, and `R_k = 0` automatically whenever `deg_y(f^k) <= n-2`.

### 2.4 PS-1 and PS-1' (PROVED-HERE), and the one-line proof via `log chi`

> **PS-1' (no hypothesis on `J`).** Under (MON)+(SEP), for every `k >= 0`
> ```text
>        d P_{k+1} / dx  =  (k+1) * [y^{n-1}]( J f^k mod (g - c) ) .
> ```
> **PS-1 (adds (KEL)).**  `d P_{k+1}/dx = (k+1) J R_k`.

*Proof.* Differentiating `g(x,tau_i(x)) = c` gives `tau_i' = -g_x/g_y` and hence
`d/dx f(x,tau_i) = f_x + f_y tau_i' = J(x,tau_i)/g_y(x,tau_i)` — this is
JAC-FIBRE's identity `(star)`, and **it needs nothing about `J`**. Then
`dP_{k+1}/dx = (k+1) sum_i f(tau_i)^k J(tau_i)/g_y(tau_i)`, which is
`(k+1) Tr(J f^k / g_y)`, and LEMMA EJ finishes. Under (KEL), `J` is a constant and
comes out of the trace. ∎

*Second proof, and the reason the identity exists.* Under (KEL), by the same
JAC-FIBRE step,
```text
   (GF-P)   sum_{k>=0} P_k T^{-k-1} = chi'(T)/chi(T)     = d/dT  log chi ,
   (GF-R)   sum_{k>=0} R_k T^{-k-1} = -(1/J) d/dx log chi .
```
`(GF-R)` because `d chi/dx = -chi * sum_i (d f(tau_i)/dx)/(T - f(tau_i))
= -J chi sum_i 1/(g_y(tau_i)(T - f(tau_i)))`, then expand in `T^{-1}` and use EJ.
**PS-1 is exactly the equality of the two mixed partials of `log chi`**: applying
`d/dx` to (GF-P) and `d/dT` to (GF-R) and comparing coefficients of `T^{-k-2}`
gives `dP_{k+1}/dx = J(k+1)R_k`. This is the structural reason the family exists.
Both generating functions are verified exactly to order `T^{-9}` on six Keller
pairs (MEASURED, `genfun.log`, 108 checks, 0 failures), which is an independent
control on PS-1 that does not go through Newton's identities at all. The same
computation explains the companion identity (verified in the driver):
```text
   (PS-1c)   d P_k / dc  =  [y^{n-1}]( (f^k)_y mod (g - c) )   (no hypothesis on J).
```

**Corollary TRACE-CONSTANT.** For `n >= 2`, `R_0 = [y^{n-1}](1) = 0`, so under
(KEL) `P_1 = Tr(f)` is independent of `x`. This is a *Keller test on its own*: all
four non-Keller negative controls are refuted by PS-1 **at `k = 0`** (MEASURED).

### 2.5 What "pole" means, and why `deg_x` is controlled by branch growth

Put `t = x^{-1}` and let `ord = ord_t` be the valuation on the Puiseux field
`C<t> = union_N C((t^{1/N}))`, normalised by `ord_t x = -1`. Fix a value
`c_2 in C` and let `tau_1(t),...,tau_n(t) in C<t>` be the `n` branches at infinity
of the affine curve `{g = c_2}` (they exist and are `n` in number by (MON)). For a
polynomial `h`, the **growth exponent of `h` along the branch `tau`** is
```text
        gamma_h(tau) := - ord_t h(x, tau)   in (1/N) Z ,
```
i.e. `|h| ~ |x|^{gamma}` along that branch. This is what "pole of `f` on a root"
means throughout; it is the *x*-growth exponent, **not** a pole order of a
meromorphic function on a curve and **not** a contact order. FRONTIER-EXACT
(promoted, integration #17 A.2) states `gamma_f(tau) = 1 - delta^0_tau` at every
**proper** branch (`gamma_f > 0`); at a non-proper branch `gamma_f(tau) <= 0`, and
there `1 - delta^0` is `-ord_t(f(tau) - a_0)`, which is a **different** number
(sec.5 turns on exactly this).

> **LEMMA DEG.** Let `Q in C[x,c]`, `Q != 0`, and for `c_2` outside a finite set
> let `Q(., c_2) != 0`. Then `deg_x Q = -ord_t Q(t^{-1}, c_2)` for all but finitely
> many `c_2`. Hence any bound `-ord_t Q(t^{-1},c_2) <= B` valid at one such `c_2`
> is a bound on `deg_x Q`.

*Proof.* Write `Q = sum_j a_j(c) x^j`, `d := max{j : a_j != 0}`. For `c_2` outside
the finite set `{a_d = 0}` we get `deg_x Q(.,c_2) = d`. ∎

This is used **per `k`**: for each `k` separately choose `c_2` avoiding (i)
`disc_y(g-c) = 0`, (ii) the finitely many `c_2` at which the top coefficient of
`P_{k+1}` or `R_k` vanishes, and (iii) the finitely many `c_2` at which the branch
profile `{delta^0_i}` differs from its generic value. The intersection of three
cofinite sets is nonempty; the bound is independent of the choice. **The quantifier
order matters and is stated here because getting it wrong is the standard way this
argument goes vacuous.**

### 2.6 PS-2, PS-3, PS-3+ (PROVED-HERE)

Set `c_max := max_i (gamma_f(tau_i))^+ = max_i (1 - delta^0_i)^+`.

> **PS-2.** Under (MON)+(SEP): `deg_x P_{k+1} <= (k+1) c_max`.  *(No (KEL).)*

*Proof.* `-ord_t sum_i f(tau_i)^{k+1} <= max_i (k+1) gamma_f(tau_i)`, and the
left-hand side is `>= 0` or the sum is `0`; apply LEMMA DEG. The further
inequality `c_max <= N = sum_i (1-delta^0_i)^+` is trivial (all summands `>= 0`)
and is the only place `N` enters. **No attainment is claimed for `N`.** ∎

> **PS-3.** Under (MON)+(SEP)+(KEL): `deg_x R_k <= (k+1) c_max - 1`, and
> `R_k == 0` whenever `(k+1) c_max < 1`.
> **PS-3+.** Since `deg_x R_k in Z`: `deg_x R_k <= floor((k+1) c_max) - 1`.

*Proof (direct, not through `P_{k+1}`).* By JAC-FIBRE under (KEL),
`ord_t f(tau) + ord_t g_y(tau) = -1` at every proper branch, so
`ord_t g_y(tau) = c(tau) - 1` with `c(tau) := gamma_f(tau)`, and
```text
   - ord_t ( f(tau)^k / g_y(tau) )  =  k c(tau) - (c(tau) - 1)... = (k+1) c(tau) - 1 .
```
At a non-proper branch, `ord_t g_y(tau) = -delta^0 < -1` and `gamma_f <= 0`, so the
same expression is `< -1 < 0`. Now `R_k = sum_i f(tau_i)^k/g_y(tau_i)` (LEMMA EJ)
and `-ord_t` of a sum is at most the max, giving
`-ord_t R_k <= max_i [(k+1)c(tau_i) - 1] = (k+1)c_max - 1`. LEMMA DEG converts this
to `deg_x`; if the right-hand side is `< 0` then `R_k` has no `x`-monomials at all,
i.e. `R_k == 0`. ∎

*(The route through `dP_{k+1}/dx` gives the same bound but needs a case split at
`P_{k+1}` constant; the direct proof does not, and it also exhibits the leading
coefficient, which is what sec.4 uses.)*

### 2.7 TRACE-CONSTANCY, and the sharpened per-root form

> **TRACE-CONSTANCY (PROVED-HERE).** Under (MON)+(SEP)+(KEL)+(GAU): if
> `km <= n - 2` then `f^k` is already reduced mod `(g-c)` and `R_k = 0`, hence
> `P_{k+1} in C[c]` — the `(k+1)`-st power sum of `f` along the fibre is
> independent of `x`.

This is the *trivial* half. The content is the sharpened form:

> **PS-3-SHARP (PROVED-HERE from D1-PIN, which is promoted).** Add to
> (MON)+(SEP)+(KEL)+(GAU) the hypotheses of D1-PIN (Moh's tower exists,
> DETECTOR-NULL, MINOR-FRONTIER; integration #17 A.3-A.4). Then every root of `g`
> either lies in a bottom-major disc `B`, where FRONTIER-EXACT + D1-PIN give
> ```text
>       c(tau) = (1 - delta_1(B)) d/(d+e) = q(B)/e ,     q(B) := (1-delta_1)de/(d+e),
> ```
> the SAME value for all roots of `B` (D1-STAR(c)), or lies in a minor disc, where
> `delta^0 > 1` and `c(tau)^+ = 0`. Hence
> ```text
>       c_max = max_B q(B)/e ,          deg_x R_k <= (k+1) q_max/e - 1 ,
>       R_k == 0                       for all k <= K0 := ceil(e/q_max) - 2 ,
>       R_k in C[c_2]  (x-independent) for all k <= K1 := ceil(2e/q_max) - 2 .
> ```

**Scope note on `delta_1 >= 0` (the charge's "Lemma 6.1" clause).** The charge
sharpens further to `q_max/e <= d/(d+e) < 1`, using `delta_1 >= 0`. That extra step
is **SOURCE-UNVERIFIED** here (Moh's paper is not on this machine) and it is
**false on the automorphism controls**: `(y, x+y^3)` has `delta_1 = -1/3`,
`q = 1`, `c_max = 1/3 > d/(d+e) = 1/4` (MEASURED — `c_max` is read off `chi`'s
Newton polygon, sec.3). The controls are invertible and lie outside NU-TWO, so
this is a scope statement, not a refutation of Moh; but **the sharpened bound must
be quoted as `c_max = q_max/e`, never as `<= d/(d+e)`**, unless `delta_1 >= 0` is
separately certified for the pair at hand. Nothing below uses `delta_1 >= 0`.

**CORRECTION to the charge (arithmetic).** For D = 105 group A (`q = 1/2, e = 3`,
`c_max = 1/6`): `K0 = 4` and `K1 = 10`, i.e. `R_0..R_4 == 0` and
`R_5..R_10 in C[c_2]`; `R_11` may have `deg_x = 1` (indeed `(11+1)c_max - 1 = 1`).
The charge's "`R_5..R_11 in C[c_2]`" is off by one at the top. MEASURED,
`box/psgrowth-drivers-20260903/trio105.log`.

**Where the content is.** For group A the *trivial* (degree) vanishing range is
`km <= n-2`, i.e. `k <= 1`. So `R_2 = R_3 = R_4 = 0` is genuinely non-trivial:
`deg_y f^k = 140, 210, 280` against `n - 1 = 104`. That much of the charge stands.

---

## 3. The instrument — `box/psgrowth-drivers-20260903/psgrowth.py`

Built as charged. Given `(f,g)` it computes `chi(T) = Res_y(g-c, T-f)`, `P_k` by
Newton's identities from `chi`, `R_k` by reduction, checks PS-0, PS-1', PS-1,
PS-1c, PS-2, PS-3, PS-3+, and prints `deg_x R_k` against the bound.

**A capability worth banking separately.** The driver reads `c_max` and the whole
multiset `{gamma_f(tau_i)}` off the **Newton polygon of `chi` with respect to
`ord_t`**: with `chi = T^n + a_1 T^{n-1} + ... + a_n`,
```text
      ord_t a_j = -deg_x a_j  (generic c) ,   {ord_t f(tau_i)} = slopes of the
      lower hull of {(j, ord_t a_j)}_{j=0..n} ,   c_max = max(0, max_j deg_x a_j / j).
```
**No tree, no Puiseux expansion, no exponent semigroup, no Moh data.** On the
charged composition `(x+y^5, y+(x+y^5)^3)` it returns `c_max = 1/15` and
`{gamma_f} = {1/15}^15`, independently reproducing `exact-n-rigidity` sec.6(c)
row 4 (`a_1 c = 1/5 = N/5`, five conjugate `D_1`'s). That is a free, exact,
one-resultant computation of the DICT-N data on any explicit pair.

### 3.1 Controls, as charged (MEASURED: 1495 checks, 0 failures, 12 s)

```text
POSITIVE (Keller, Moh's gauge; polynomial automorphisms are the only Keller pairs
available):  (y,x+y^2) (y,x+y^3) (y,x+y^3+y^2) (y,x+y^4) (y,x+y^5+3y^2) (y,x+y^6)
             (x+y^2, y+(x+y^2)^2)   n=4
             (x+y^2, y+(x+y^2)^3)   n=6, m=2  [the charged degree-6 tame automorphism]
             (x+y^3, y+(x+y^3)^2)   n=6, m=3
             (x+y^5, y+(x+y^5)^3)   n=15, m=5 [the charged composition]
   all of PS-0/PS-1'/PS-1/PS-1c/PS-2/PS-3/PS-3+ exact for k <= 20;
   P_k cross-checked by a second, independent route (trace of the multiplication
   matrix on A) for k <= 8 on every n <= 6 control.
NEGATIVE (non-Keller, monic in y):  (y, y^2+xy+x) ; (y^2-x, x+y^3) ;
   NOTT two-tower rows 0 and 6 (box/tfe-drivers-20260902/control4.py).
   PS-1' holds on all four (as it must -- it has no hypothesis).
   PS-1 with a constant J is REFUTED on all four, first at k = 0, i.e. by
   TRACE-CONSTANT: Tr(f) depends on x.                          4/4 as required.
VACUITY GUARD: (y, x+y^3) with c_max deliberately understated as 1/5 instead of
   1/3 -- the understated PS-3 bound is VIOLATED, first at k = 2.  As required.
```

**Honest limitation of the negative battery.** PS-3 was *not* violated by the four
non-Keller rows, because their `c_max` (1, 1, 3/2, 3) is large enough that the
bound is slack. PS-3's dependence on (KEL) is real (the proof uses JAC-FIBRE) but
this battery does not exhibit it. Bounded `OPEN[PS3-NEG]`: exhibit one non-Keller
monic pair with `deg_x R_k > (k+1)c_max - 1`, or prove PS-3 needs no (KEL).

### 3.2 OPEN[PS-VACUITY] — answered (MEASURED, `k <= 20`, `n <= 6` plus `n = 15`)

`R_k` is **not** identically zero on Keller pairs. The measured `{k : R_k != 0}`:

| pair | `n` | `m` | `c_max` | `{k <= 20 : R_k != 0}` |
|---|---|---|---|---|
| `(y, x+y^2)` | 2 | 1 | 1/2 | 1,3,5,7,9,11,13,15,17,19 |
| `(y, x+y^3)` | 3 | 1 | 1/3 | 2,5,8,11,14,17,20 |
| `(y, x+y^3+y^2)` | 3 | 1 | 1/3 | 2,3,4,5,... (all `k >= 2`) |
| `(y, x+y^4)` | 4 | 1 | 1/4 | 3,7,11,15,19 |
| `(y, x+y^6)` | 6 | 1 | 1/6 | 5,11,17 |
| `(x+y^2, y+(x+y^2)^3)` | 6 | 2 | 1/6 | 5,8,10,11,13,14,15,... |
| `(x+y^3, y+(x+y^3)^2)` | 6 | 3 | 1/6 | 5,7,9,10,11,12,... |
| **`(x+y^5, y+(x+y^5)^3)`** | **15** | **5** | **1/15** | **14, 17, 20 only** |

So outcome (i)/(iii) of the charged card, not outcome (ii): the route does not die
by universal vanishing. **But the last row is the finding.** A genuine Keller pair
in Moh's gauge has `R_k == 0` for every `k <= 13` and `deg_x R_k = 0` for every
`k <= 20`, while the "generic" expectation quoted in the ideation is
`deg_x R_k = Theta(km) = Theta(5k)`. At `k = 20` that is `0` against `100`.
**The `Theta(km)` expectation is refuted by a witness**, and with it route (P-b)
of the charged sec.5.2.

---

## 4. The residue lower bound — THEOREM RESIDUE-LEAD, and why the lemma cannot exist

Charge (3) asks: is the leading `x`-term of `R_k` determined by the initial forms /
the `g`-adic expansion of `f^k`, and can it be shown nonzero with
`deg_x >= phi(k,m,n) -> oo`?

### 4.1 The leading coefficient, computed (PROVED-HERE)

At a bottom-major disc `B` of radius `delta_1`, Moh's general point is
`sigma_1(pi) = w(t) + pi t^{delta_1}` and, by D1-STAR, the `a_1 = eV_2` roots of
`g` in `B` separate pairwise exactly at `delta_1`, so
`p_g` has `a_1` **simple** roots `pi_1..pi_{a_1}`, and `lambda_f` is constant on
`[delta_1, delta^0]`. With
`f(sigma_1(pi)) = t^{lam_f}(p_f(pi) + O(t^eps))`,
`g(sigma_1(pi)) = t^{lam_g}(p_g(pi)+O(t^eps))` and `g_y = t^{-delta_1} d/dpi`:

```text
   ord_t f(tau_i)   = lam_f = -c ,        ord_t g_y(tau_i) = lam_g - delta_1 = c - 1
                                          (the last equality IS Phi(delta_1) = 1),
   f(tau_i)^k / g_y(tau_i) = t^{1 - (k+1)c} * [ p_f(pi_i)^k / p_g'(pi_i) ] * (1 + O(t^eps)).
```

Summing over the disc, the disc's leading coefficient is
`S_k := sum_i p_f(pi_i)^k/p_g'(pi_i)`, and by LEMMA EJ one level down,
`S_k = [pi^{a_1-1}](p_f^k mod p_g)`.

> **THEOREM RESIDUE-LEAD (PROVED-HERE/UNREVIEWED).** With BOTTOM-ODE
> `d p_f p_g' - e p_g p_f' = kappa in C^*` (`box/tfe-drivers-20260902/bottomode.py`),
> evaluation at a root `pi_i` of `p_g` gives `d p_f(pi_i) p_g'(pi_i) = kappa`, hence
> ```text
>          S_k  =  (d/kappa) * ptilde_{k+1} ,     ptilde_j := sum_i p_f(pi_i)^j .
> ```
> The bottom-disc leading coefficient of `R_k` is the `(k+1)`-st **power sum of the
> Davenport-Stothers pair of the bottom star** — PS-GROWTH one level down.
> In particular `ptilde_1 = (kappa/d) S_0 = (kappa/d)[pi^{a_1-1}](1) = 0` for
> `a_1 >= 2`, always.

**Answer to "is it determined by the initial forms?" — NO, and this matters.**
The leading term is determined by the **bottom** star `(p_f, p_g)` at level 1 plus
the tower constants. The initial forms `l(f) = alpha H^d`, `l(g) = beta H^e`,
`H = L_1^u L_2^v` are the level-`s` data at the TOP of the tower, `s - 1` levels
away. They fix `(d, e)` and hence the *type* of the bottom star, and nothing more
of the leading coefficient. Any claim that the top forms compute the leading term
of `R_k` is a **flag/place conflation** in the FALLACY-v2 sense.

**Cross-disc Galois sum.** If the bottom discs form one orbit of size `nu` under
the Galois action `t^{1/L} -> zeta_L t^{1/L}` of `C<t>/C((t))`, then for
`sigma` a generator, `sigma(kappa_i t^theta) = zeta_L^{L theta} kappa_{sigma(i)} t^theta`,
and `R_k` is `sigma`-invariant, so `sum_i kappa_i = zeta_L^{L theta} sum_i kappa_i`:
**the top term survives only if `theta = 1 - (k+1)c_max in Z`.** That is exactly
PS-3+ read on the leading term, and it is the mechanism behind every zero in the
table of sec.3.2.

### 4.2 Verified end-to-end (MEASURED, `leadcheck.log`, 10 checks, 0 failures)

`starres2.py` solves BOTTOM-ODE by **saturated Groebner** (`z*kappa - 1`) and tests
`ptilde_j == 0` on the star variety by ideal membership (`w*ptilde_j - 1`), with a
positive and a negative control on the test itself. Then `leadcheck.py` predicts
`{k : the PS-3 bound is ATTAINED}` from the star and `nu` alone, and measures it:

| pair | star | `nu` | `c_max` | predicted `{k : PS-3 attained}` | measured |
|---|---|---|---|---|---|
| `(y,x+y^2)` | (1,2,1) | 1 | 1/2 | 1,3,...,23 | **same** |
| `(y,x+y^3)` | (1,3,1) | 1 | 1/3 | 2,5,...,23 | **same** |
| `(y,x+y^4)` | (1,4,1) | 1 | 1/4 | 3,7,...,23 | **same** |
| `(y,x+y^6)` | (1,6,1) | 1 | 1/6 | 5,11,17,23 | **same** |
| `(x+y^5,y+(x+y^5)^3)` | (1,3,1) | 5 | 1/15 | 14 | **same** |

For the `(1,e,1)` family the star is `p_g = pi^e + p_0`, `p_f = q_1 pi`, so
`ptilde_j != 0` iff `e | j` — and the *whole* `R_k` vanishes off that congruence
class. For the `nu = 5` composition the two conditions compose: `R_k != 0` needs
`15 | (k+1)` for the leading term, and `R_17, R_20, R_23` are nonzero at a
**strictly lower** order (the prediction governs the top term only; this is stated
as such and is the only place where a naive reading of RESIDUE-LEAD would
over-claim).

### 4.3 The `D = 105`-type ansatz (charge (3)(c)) — answered NO

For the trio, `(d, e, V_2) = (2, 3, 1)`, `a_1 = 3`, `b_1 = 2`,
`gamma = V(de-d-e)+1 = 2`. Solving BOTTOM-ODE (MEASURED, exact):

```text
   p_g = pi^3 + (3 q_0/(2 q_2)) pi ,    p_f = q_2 pi^2 + q_0 ,    kappa = 3 q_0^2/q_2 ,
   free parameters q_0, q_2 only (the pi-scaling and the p_f-scaling): ONE orbit,
   field of moduli Q -- confirming the charged "unique DS pair of type (2,3)".
   Normalised (q_2 = 1, q_0 = -2/3): p_g = pi^3 - pi , p_f = pi^2 - 2/3 ,
   roots of p_g = {0, 1, -1} , values of p_f = {-2/3, 1/3, 1/3} ,
   ptilde_j = 3^{-j}( (-2)^j + 2 )  =  0  iff  j = 1 .
```

**So `ptilde_{k+1} != 0` for every `k >= 1`: the per-disc leading coefficient of
`R_k` never vanishes for the trio's star** (MEASURED for `j <= 12` by ideal
membership over the whole 2-parameter family, not only at the normalised point).

Consequence, typed:

> For `k = 2, 3, 4` the forced vanishing `R_k == 0` at group A comes **entirely
> from the exponent**: `1 - (k+1)c_max = 1 - (k+1)/6 > 0`, so the summands have
> *positive* `ord_t` and there is no `x`-monomial to cancel. **No coefficient
> identity is required, hence none is forced, hence Davenport-Stothers extremality
> of the bottom star is NOT contradicted.** The charge's hoped-for contradiction
> does not arise, and the reason is not that a cancellation is possible but that
> nothing needed to cancel.

### 4.4 The seven two-tower rows (charge (3)(b))

The NOTT two-tower rows are **non-Keller** (`control4.py` certifies this and it is
re-certified here on rows 0 and 6: `J` is a nonconstant polynomial of degree 3 and
7 respectively). They therefore do not satisfy JAC-FIBRE, so RESIDUE-LEAD's
`ord_t g_y = c - 1` step is unavailable and the bottom bracket is not a nonzero
constant (`control4.py`'s (ODE) test). What they *do* deliver here is the negative
control for PS-1, which they pass as required: PS-1 refuted at `k = 0` on both
rows tested. **They cannot be used to probe the residue lower bound**, because the
lower bound is a statement about Keller pairs and these rows fail the hypothesis
that produces the bound. Recorded so that no future lane reads their large
`c_max` (3/2, 3) as evidence about the Keller locus.

### 4.5 The verdict on the lower bound: it cannot exist as posed

This is the decisive paragraph of the lane.

```text
   PS-3 says      deg_x R_k <= (k+1) c_max - 1 .
   RESIDUE-LEAD says the bound is ATTAINED whenever (k+1)c_max in Z and the star
   power sum ptilde_{k+1} != 0 -- which, for the trio's star, is EVERY k >= 1.
   A bound that is attained is not a constraint on the pair; it is a computation.
```

Therefore a "residue lower bound" `deg_x R_k >= phi(k,m,n)` with
`phi > (k+1)c_max - 1` is **false**, not merely unproved: the witnesses are the
automorphism controls, on which `deg_x R_k` equals `(k+1)c_max - 1` exactly and
`c_max` is as small as `1/15`. Concretely, the ideation's two proposed closings:

- **(P-b), the growth route** — "`deg_x R_k >= c k m/n` for some `c > 0` on any
  Keller pair" — would give, on `(x+y^5, y+(x+y^5)^3)`, `c k/3 <= 0` for all
  `k <= 20` (MEASURED `deg_x R_k = 0` there). **REFUTED for every `c > 0`.**
- **(P-a), the resultant route** — dealt with in sec.5: its identity is `N` on
  both sides.

What *is* still available, and is the honest residual, is the **weak** direction:

> **LEMMA NEEDED (RESIDUE-FLOOR), exact statement.** Let `(f,g)` be a
> **non-invertible** Keller pair in Moh's gauge. Show, by an argument that does
> **not** use the branch data (e.g. from the polynomiality of `f` as the Lagrange
> interpolant of `int dx/g_y`, or from elimination on `chi`), that there exists
> `k <= psi(m,n)` with `R_k != 0`. Then PS-3 forces
> `(k+1) q_max/e >= 1`, i.e. `q_max >= e/(psi(m,n)+1)`.

and its consequence, which is **not** a ceiling:

```text
   N = sum_B V_2(B) q(B) >= q_max >= e/(psi+1)   =>   e <= N (psi+1) <= 16 (psi+1).
```

**This bounds `e`, never `D`.** `D = n = K e` and `K = gcd(m,n)` is invisible to
the entire identity family: every quantity in PS-0..PS-3 is a function of
`(m, n, q_max, e)` and `q_max <= N <= 16` already. On the frontier the bound is
vacuous anyway: the D = 105 trio has `e = 3`. **PS-GROWTH is structurally
incapable of producing `D <= C(N)`.**

**CORRECTION to the charged ideation sec.2.1/2.2.** "PIN-NOT-CEILING is being
over-applied" is withdrawn. PIN-NOT-CEILING says the boundary computes an `O(1)`
quantity; PS-GROWTH turns out to be a *second computation of the same `O(1)`
quantity* (`c_max = q_max/e`), dressed as an identity in a free integer `k`. The
free `k` buys no `D`-growth because it multiplies a quantity that is already
bounded. The `Theta(km)` "generic size" of the residue, which was the whole
premise, is refuted by the automorphism witnesses (sec.3.2).

---

## 5. RES-DEGREE (charge (4)) — corrected, and the kill test collapses

**Charged:** `deg_x Res_y(g - c_2, f) = sum_i (1 - delta^0_i) = N - shed`,
`shed = sum_i (1-delta^0_i)^-`.

**What is true (PROVED-HERE).** `g - c_2` is monic, so
`Res_y(g-c_2, h) = prod_i h(x, tau_i)` and
```text
     deg_x Res_y(g-c_2, h) = sum_i gamma_h(tau_i) = - sum_i ord_t h(x,tau_i) .
```
Two specialisations:
```text
   (RD-1)  h = f - c_1 , generic c_1 :  gamma = (1-delta^0_i)^+ at every branch, so
           deg_x Res_y(g-c_2, f-c_1) = N .   <-- this is CONTACT-DEFICIENCY/FRONTIER-N
                                                 restated; it is the geometric degree.
   (RD-2)  h = f :  deg_x Res_y(g-c_2, f) = N - shed_0 ,
           shed_0 := sum over NON-PROPER branches of ord_t f(tau_i)  >= 0 ,
           i.e. the vanishing order of f at the places at infinity of {g=c_2}
           where f stays finite.  shed_0 = 0 unless f VANISHES there.
```
`shed_0` is **not** `sum_i (1-delta^0_i)^-`. At a non-proper branch,
`1 - delta^0 = -ord_t(f(tau) - a_0)` with `a_0 = lim f(tau)`, while the resultant
sees `-ord_t f(tau)`; the two agree iff `a_0 = 0`.

**REFUTATION WITNESS (MEASURED, `resdeg.log`).** `g = y^3 + xy` (monic in `y`,
`deg = deg_y = 3`). Branches of `{g = c}`: `tau_+- ~ +-sqrt(-x)` (proper,
`1-delta^0 = 1/2` each) and `tau_0 ~ c/x` (non-proper, `1-delta^0 = -1`), so
`sum_i (1-delta^0_i) = 0`.
```text
   f = y   (a_0 = 0):   deg_x Res_y(g-c, f) = 0  -> charged form HOLDS.
   f = y+1 (a_0 = 1):   deg_x Res_y(g-c, f) = 1  -> charged form REFUTED (0 != 1).
```

**Measured on the Keller library** (10 pairs, `resdeg.log`, 32 checks, 0 failures):
every branch is proper, `shed_0 = 0`, and `deg_x Res_y(g-c_2,f) = N = 1` on all
ten automorphism controls. So on the Keller locus the charged form is *true but
vacuous*: there is nothing to shed.

### 5.1 The shed term on the three `D = 105` groups (charge (4))

**It is not computable from the tree data, and I decline to state a number.**
What D1-PIN/DETECTOR-NULL/MINOR-FRONTIER pin is that minor-disc roots have
`delta^0 > 1`; they do **not** pin `delta^0` there, and `shed_0` additionally
depends on whether `f` vanishes at those places. What *is* tree data is the split
of the `n = 105` roots of `g`:

| trio group | `q` | `e` | `u` | admissible `k_B = sum_B V_2(B)` → `N` | `A_bot = e k_B` proper roots | minor roots |
|---|---|---|---|---|---|---|
| `m=70 M=[28,103] V_s=5` | 1/2 | 3 | 25 | 12→6, 14→7, …, 24→12 | 36, 42, …, 72 | 69, 63, …, 33 |
| `m=70 M=[28,103] V_s=6` | 9/13 | 3 | 30 | 13→9 | 39 | 66 |
| `m=70 M=[40,103] V_s=4` | 9/17 | 3 | 28 | 17→9 | 51 | 54 |

`OPEN[RES-SHED]` (raised in the charged ideation, bounded at 1,908 MOH-4 groups)
should be **RETYPED, not answered**: the quantity it names,
`sum_i (1-delta^0_i)^-`, is not the shed of RES-DEGREE, and neither quantity is a
skeleton function.

### 5.2 ORTHO-DEFECT minus RES-DEGREE — the kill test collapses

The proposal was: ORTHO-DEFECT `2deN = sum_nu (e m_nu - d m'_nu)^2` prices `N` on
the base-point cluster; RES-DEGREE prices `N - shed` on the resultant; subtracting
gives the shed in cluster terms, hence a skeleton kill test.
**Both sides price `N`** (RD-1), so the difference is identically `0` and the test
is empty. Not run on the trio; there is nothing to run. The third consequence in
the charged sec.6 ("row 1 / GGV reopened as a computer of `deg_x Res`") survives
in the weakened form: GGV would compute `N`, which the boundary already computes
exactly (integration #17 C).

---

## 6. Reading (charge (5))

**Ceiling route, shape constraint, or vacuous?** *Shape constraint on `(e, q_max)`,
and currently vacuous on the frontier.*

1. **Not a ceiling, for a structural reason.** Every quantity in the identity
   family is a function of `(m, n, q_max, e)`; `K = gcd(m,n)` never appears, and
   `D = Ke`. Even a perfect residue floor yields `e <= C(N)` (sec.4.5), and the
   frontier already has `e in {3,5}`. The free integer `k` does not help: it
   multiplies `c_max = q_max/e <= N/e`, a quantity the boundary already bounds.
2. **Not vacuous as an instrument.** `c_max` and the full `{gamma_f(tau_i)}` come
   off one resultant with no tree, no Puiseux data, no exponent semigroup and no
   outer/inner split (sec.3). That is a new, cheap, exact certificate applicable to
   any *explicit* pair — the first tool in the campaign that can be pointed at a
   candidate pair rather than a skeleton, which is what the charged ideation
   sec.4.2 wanted from it and is the part of that claim that survives.
3. **The vanishing pattern is not a discriminator.** `(x+y^5, y+(x+y^5)^3)` is a
   genuine Keller pair with `R_k == 0` for all `k <= 13`; D = 105 group A has
   `R_k == 0` only for `k <= 4`. A long forced-vanishing range is what a Keller
   pair with many conjugate bottom discs *looks like*. MEASURED over the census
   (`trio105.log`), `max K0` grows with `D` (14 at D=48, 62 at D=108 and D=120)
   while the **median stays at 2-3** — the growth is a divisor-structure artefact
   of `q_max`, exactly as PIN-NOT-CEILING predicts, and not a signal.

**The exact statement of the lemma still needed** — for the record, so that no
future lane re-derives a false one:

> **RESIDUE-FLOOR.** For a non-invertible Keller pair in Moh's gauge, exhibit
> `k <= psi(m,n)` with `R_k != 0`, proved **without** the branch data. Its payoff
> is `q_max >= e/(psi+1)`, hence `e <= N(psi+1)` — a `V-FLOOR`-type filter, **not**
> a ceiling. Any statement of the form `deg_x R_k >= phi(k,m,n)` with
> `phi > (k+1)c_max - 1` is FALSE (sec.4.5, witnesses given). **Do not charge a
> lane with proving it.**

**The single cheapest next experiment.** Not on PS-GROWTH as a proof route — on
PS-GROWTH as the *interpolation engine in symmetric-function form*:

> **EXPERIMENT NEXT-COEFF (1 h, one core, exact).** For the controls, expand `R_k`
> in `x` **completely** (not only the leading term) and identify, order by order,
> which tower level each coefficient sees. RESIDUE-LEAD says the top coefficient
> is the bottom-star power sum `ptilde_{k+1}`. If the coefficient at order
> `(k+1)c_max - 1 - j` is a function of the tower data down to level `j` only, then
> the coordinator's `n - m - 1` trace identities `Tr(f s_k / g_y) = 0` (charged
> sec.0.3) are computable as **resultant coefficients over `Q`** — no Puiseux
> expansion, no exponent semigroup, no outer/inner split, which are precisely the
> three unknowns Sol's review said block the order-by-order engine. Gate: on
> `(x+y^2, y+(x+y^2)^3)` the level-2 data is known, so the level-2 prediction is
> checkable. Payoff if positive: the global-interpolation lane re-bases onto exact
> polynomial algebra. Payoff if negative: PS-GROWTH is a one-coefficient instrument
> and the lane closes.

The `s_k`-weighted trace identities of the coordinator's sec.0.3 are, in this
report's notation, `R_k^{(s)} := [y^{n-1}](s_k(hat tau) f mod (g-c_2))` — the
driver's `residues(..., weight=w)` already computes them for any weight `w`, so
NEXT-COEFF is a parameter change, not a new instrument.

---

## 7. OPENs, bounded

```text
OPEN[PS-VACUITY]      ANSWERED.  R_k is not identically zero on Keller pairs
                      (k <= 20, n <= 6 and n = 15, 10 pairs).  But vanishing over
                      an initial range of length 13 occurs on a genuine Keller
                      pair, so the vanishing test discriminates nothing.  CLOSE.
OPEN[PS3-NEG]         NEW, bounded: exhibit ONE non-Keller monic pair with
                      deg_x R_k > (k+1)c_max - 1, or prove PS-3 without (KEL).
                      Search space: the 7 two-tower rows + any monic pair with
                      c_max < 1.  One CAS hour.
OPEN[STAR-PTILDE]     NEW, bounded: for which (d,e,V) census stars is
                      ptilde_j == 0 for some j >= 2?  MEASURED for
                      (1,2,1),(1,3,1),(1,4,1),(1,6,1),(2,3,1): only the
                      congruence-forced zeros of the (1,e,1) family and
                      ptilde_1 = 0.  The (2,3,2) ptilde row did not finish inside
                      the lane's compute budget (saturated Groebner + ideal
                      membership, 12 unknowns); its EXISTENCE is settled
                      (existence.log).  Remaining ptilde rows: (2,3,2), (2,3,3),
                      (2,5,1), (2,5,2), (3,4,1), (3,5,1), (4,5,1) -- 7 rows.
OPEN[RES-SHED]        RETYPE, do not answer.  The named quantity
                      sum_i (1-delta^0_i)^- is not the shed of RES-DEGREE, and
                      neither is a skeleton function (sec.5.1).
OPEN[DELTA1-SIGN]     NEW, bounded, SOURCE-UNVERIFIED: is delta_1 >= 0 for every
                      NU-TWO Moh tower (the charge's "Lemma 6.1")?  It is FALSE on
                      the automorphism controls (delta_1 = -1/3 on (y,x+y^3)).
                      One page lookup; nothing in this report depends on it.
```

**CORRECTION to a driver, recorded because it nearly became a finding.**
`starres.py`'s first version used `sympy.solve` on the BOTTOM-ODE system and
reported "**no (2,3,2) star exists**". That is a **solver artefact**: the saturated
Groebner basis of the same ideal (`z*kappa - 1`) is **not** `{1}`, so a `(2,3,2)`
star **does** exist (MEASURED, 0.11 s, `existence.log`). Had it been believed it
would have looked like a proof of MAJOR-MULT's opposite at `V_2 = 2`.
`starres.py` is retained but marked SUPERSEDED in the driver README;
`starres2.py` does the ideal-theoretic version with positive and negative
controls on the vanishing test itself, and `existence.py` decides existence alone
for all twelve census-relevant `(d,e,V)` types:

```text
   (1,2,1) (1,3,1) (1,4,1) (1,6,1) (2,3,1) (2,3,2) (2,3,3)
   (2,5,1) (2,5,2) (3,4,1) (3,5,1) (4,5,1)      -- a star EXISTS for all 12,
   gamma = V(de-d-e)+1 = 0,0,0,0,2,3,4,4,7,6,8,12 respectively.  14 checks, 0 fail.
```

**Note for `OPEN[MAJOR-MULT]`, unsolicited but cheap:** existence of the bottom
star at `V_2 = 1` is therefore *not* an obstruction anywhere in this list, so
MAJOR-MULT (`V_j >= 2`) does not follow from `OPEN[STAR-REALISABILITY]` at the
level of the star alone. This neither supports nor refutes the clause; it removes
one candidate proof of it.

---

## 8. FALLACY-v2 audit

- **Flag/place/series.** `c_max = max_i gamma_f(tau_i)^+` (a *place* quantity, one
  branch) is kept strictly distinct from `N = sum_i (...)^+` (a *series* quantity)
  throughout; the only inequality between them used is the trivial `max <= sum`,
  and no attainment is claimed (sec.2.6). Strict-below vs at-level parting: the
  bottom-disc separation `delta_1` (at-level) and the frontier `delta^0`
  (strict-below) are never identified; `lambda_f` constant on `[delta_1, delta^0]`
  is quoted from D1-STAR(b), not assumed.
- **Per-ray/exit-set charge.** No new exit price is asserted in this report; no
  `charge_basis` line is due. Consuming D1-PIN's promoted per-root price `q(B)/e`
  needs none.
- **Carrier/attainment.** RESIDUE-LEAD gives ATTAINMENT of PS-3 only where the
  congruence `(k+1)c_max in Z` holds AND `ptilde_{k+1} != 0`; at other `k` the
  report claims only a floor of `-oo` (i.e. nothing), and the D15 row is displayed
  precisely because it separates "R_k != 0" from "PS-3 attained".
- **Pole/interior.** "Pole" is defined once (sec.2.5) as the `x`-growth exponent
  `-ord_t h(tau)`, and every use of FRONTIER-EXACT checks the vertex class first:
  `gamma_f = 1 - delta^0` is applied **only at proper branches**; sec.5's
  refutation witness is exactly the non-proper case where the charged form
  conflated the two.
- **Floor/attainment.** sec.4.5 states explicitly that PS-3 is a ceiling that is
  generically attained, hence cannot be contradicted; no lower bound is promoted.
- **`sat()` wrapping.** The star existence and the `ptilde_j` vanishing tests both
  extract the saturated ideal (`z*kappa - 1`), assert the polynomial ring and the
  generator order explicitly, and run a positive and a negative control on the
  membership test (`starres2.py`). The `sympy.solve` route is retracted (sec.7).
- **Raw remainder degree.** `R_k` is a normal form in the declared quotient
  `k0[x,c][y]/(g-c)` with `g - c` monic (so the quotient is free and reduction is
  canonical); the zero case is branched on everywhere (`deg_x 0 = -oo`, printed as
  `None`), and the "leader vanished" case is exactly the `PS-3 slack` column.
- **Variable/ring map.** `R = k0[x,c]`, `A = R[y]/(g-c)`, basis `1..y^{n-1}`,
  `chi in R[T]`; the map to the Puiseux side is `x = t^{-1}`, `ord_t x = -1`,
  stated once and used with LEMMA DEG's quantifier order made explicit.
- **Prime label/derivative.** `p_g'` means `d p_g/d pi` (`pi` is Moh's disc
  coordinate; the differentiation is defined in BOTTOM-ODE, which is charged).
  `P_k` (power sum) and `p_f, p_g` (star polynomials) are disjoint namespaces;
  `P` never carries a prime.
- **Merge-free/M-descent, target/arrival index.** Not touched by this lane.

---

## 9. Typed verdict block

```text
LANE         PS-GROWTH / TRACE-CONSTANCY (flagship), Opus 5, 2026-09-03
PROVED-HERE  PS-0; LEMMA EJ; PS-1' (no hypothesis on J); PS-1 (Keller);
             PS-1c; LEMMA DEG; PS-2 (no Keller); PS-3 (direct, Keller);
             PS-3+ (integrality); TRACE-CONSTANT (P_1 x-independent);
             TRACE-CONSTANCY; PS-3-SHARP (from promoted D1-PIN);
             THEOREM RESIDUE-LEAD (S_k = (d/kappa) ptilde_{k+1}); ptilde_1 = 0;
             the corrected RES-DEGREE (RD-1) and (RD-2).
MEASURED     psgrowth.log 1495 checks / 0 failures (10 Keller pairs n=2..6 and
             n=15, k<=20; 6 non-Keller); leadcheck.log 10/0 (RESIDUE-LEAD
             predicted == measured, 5 pairs); resdeg.log 32/0 (+ refutation
             witness); starres2.log (star existence + ptilde vanishing, saturated
             Groebner, with controls on the test); existence.log 14/0 (all 12
             census-relevant (d,e,V) stars exist); genfun.log 108/0 ((GF-P),(GF-R)
             to order T^{-9}); trio105.log (trio ranges and the census growth of
             K0).  Whole directory < 13 min, one core, < 1 GB.
REFUTED      "deg_x R_k = Theta(km) generically on Keller pairs"  (witness
             (x+y^5,y+(x+y^5)^3): deg_x R_k = 0 for all k <= 20, km = 100);
             route (P-b) of the charged ideation sec.5.2 for every c > 0;
             RES-DEGREE as charged (witness g = y^3+xy, f = y+1);
             the "ORTHO-DEFECT minus RES-DEGREE" kill test (both sides are N);
             "no (2,3,2) bottom star exists" (a sympy.solve artefact of this
             lane's own first driver, caught and retracted).
CORRECTED    the charge's trio arithmetic: K1 = 10, so R_5..R_10 in C[c_2] and
             R_11 may have deg_x 1 (not R_5..R_11);
             the charge's "c_max <= d/(d+e) < 1" -- true only if delta_1 >= 0,
             which FAILS on the controls; quote c_max = q_max/e;
             "the leading term is determined by the initial forms" -- it is
             determined by the BOTTOM star, s-1 levels down;
             "PIN-NOT-CEILING is over-applied" -- withdrawn.
NOT CLAIMED  any ceiling D <= C(N); any kill of the D = 105 trio; attainment of
             N by c_max; delta_1 >= 0; anything about Moh's Appendix II.
READING      PS-GROWTH is a SHAPE CONSTRAINT on (e, q_max), structurally incapable
             of a D-ceiling, and currently vacuous on the frontier.  Its surviving
             value is (a) an exact tree-free certificate for c_max and the whole
             {gamma_f} multiset on any explicit pair, and (b) EXPERIMENT
             NEXT-COEFF, which would re-base the global-interpolation program onto
             resultant coefficients over Q.
NEXT         EXPERIMENT NEXT-COEFF (1 h).  Do NOT charge a lane with RESIDUE-FLOOR
             in the form "deg_x R_k >= phi(k,m,n)": that statement is false.
```

## 10. Reproduction

```text
box/psgrowth-drivers-20260903/
   psgrowth.py   python3 psgrowth.py 20     -> psgrowth.log    (1495 checks, 0 fail)
   leadcheck.py  python3 leadcheck.py       -> leadcheck.log   (10 checks, 0 fail)
   resdeg.py     python3 resdeg.py          -> resdeg.log      (32 checks, 0 fail)
   trio105.py    python3 trio105.py         -> trio105.log
   existence.py  python3 existence.py       -> existence.log   (14 checks, 0 fail)
   genfun.py     python3 genfun.py          -> genfun.log      (108 checks, 0 fail)
   starres2.py   python3 starres2.py [d,e,V ...]  -> starres2.log
   starres.py    SUPERSEDED (sympy.solve; incomplete solution sets) -> starres.log
   README.md     the table above
sympy 1.12, python3, one core.  No ledger edited.  No network.
```

<!-- BODY-END -->
