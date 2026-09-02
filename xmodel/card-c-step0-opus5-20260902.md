# CARD-C-STEP0: pinning the degrees for the direct `F` solve

Lane: `CARD-C-STEP0`. Agent: Opus 5. Desk-scale exact reasoning.
No CAS decision procedure, no Groebner basis, no resultant, no saturation was
run: the charge forbids it and nothing below needs it. Three short scripts
(`sympy` series/degree arithmetic and one integer enumeration) were used to
re-do by machine four things also checked by hand; they are disclosed in SS0.3
and every number they produced is re-derivable on paper.

## 0. Custody, method, scope

### 0.1 Input verification

The three frozen charged copies hash as declared; this was the first action.

```text
dcd40a425b2a2782deebec3f01c3b6859a8aa8d46b3e60639f9865a807d5ddba  ideation-20260902T0022Z-opus5.md
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  rep-96-inner-opus5-20260901.md
bdd857c9d8c55fa000fcffee05f9f3084c5d073fb4d06285edf2af0d3c369339  reducible-all-n-r2-opus5-20260901.md
```

Below **IDE** = the ideation report (Card C is its SS6/SS9), **REP** = REP-96-INNER,
**CAGE** = CAGE-N-R2. Also read on disk and cited by file/line, not re-hashed as
primary: `xmodel/ideation-20260902T0022Z-fable5.md:134-166` (the GGV firewall,
SS4c), `xmodel/ideation-20260902T0022Z-packet.md:63-66` (the GGV bound as the
round packet states it), `notes.md:5802-5806` (the campaign's own custody line for
`gcd >= 16`), `xmodel/reducible-all-n-opus5-20260901.md:36-100` (r1 SS1, for the
`(mu,s,K)`/`W_i`/`(LOC)` definitions r2 uses without restating).

### 0.2 Typing

`[D]` derived here; `[P]` promoted/consumed from a charged input at its stated
scope; `[O]` typed OPEN; `[X]` withdrawn/refuted; `[A]` audit against a consumed
item. Nothing below is an attainment claim. No exit price is asserted, so no
`charge_basis` line is given (FALLACY-v2).

### 0.3 Machine disclosure

1. exact rational check of the `(9,6,2)` identity, degrees, `gcd(q',p')`, the
   orders `ord_s(X/Y)=3`, `ord_s(Z/Y)=9` at `P_inf`, and the gaps of `<2,9>`
   (SS1.2, SS2.2) — all four already in REP SS1, reproduced independently here
   because SS2.2's divisibility conclusion is load-bearing;
2. integer enumeration of the contact profiles of SS2.4 (11 of them);
3. degree arithmetic confirming `deg(f o S_k) = k deg_y f + deg_x f_a` and
   `Jac(f o S, g o S) = Jac(f,g) o S` on a worked pair (SS3.1).

## 1. What the charge fixes, and the shape of the answer

### 1.1 The configuration

`F = (f,g) : C^2 -> C^2` polynomial, `Jac(f,g) = 1`, topological degree
`td = N = 4`, non-proper. `A_F = D_1 u D_2` (CAGE SS3.5: the unique `N = 4`
profile is core `(2,1,0)` plus one trivial on a second owner, `W = (1,2)`,
class `[2]`, `b = 1`). So:

* `D_1` owns one carrier `(mu,s,K) = (2,1,0)`, `W_1 = 2`, `a_1 = N - W_1 = 2`;
  the meridian `gamma_1` is a transposition. `D_1` is the realized `(9,6,2)`
  curve, parametrised `eta_1 : t -> (q(t),p(t)) = (t^6+8t^2,\ t^9+12t^5+24t)`.
* `D_2` owns one trivial carrier `(1,1,0)`, `W_2 = 1`, `a_2 = 3`, `gamma_2 = id`.
  `D_2` is **not known**; that is `OPEN[REP-96-MPRIME-COMPANION]` (REP SS7 R4).
* Budget `(BUD)`: `2 + 1 = 3 = N - 1`, saturated. Hence there are **exactly two**
  affine-image dicriticals, `l_1 -> D_1` and `l_2 -> D_2`, both with `s = 1`.
  `[P]` (CAGE SS4 cl.2 + SS3.5.)

### 1.2 The `(9,6,2)` place, re-derived

At `P_inf = [0:1:0]` in local coordinates `u = X/Y`, `v = Z/Y`, with `s = 1/t`:

```text
   ord_s(u) = 3 = mult_{P_inf}(D_1) = a ,     ord_s(v) = 9 = (D_1 . L_inf)_{P_inf} = deg D_1 .
```

Both machine-confirmed. One point, one place, and `p^2 - q^3 - 64q - 64t^2 = 0`
exactly, `deg q = 6`, `deg p = 9`, `gcd(q',p') = 1`, `S_aff = <2,9>` with gaps
`{1,3,5,7}`, `delta_aff = 4`. This reproduces REP SS1 by an independent route and
supplies the number SS2.2 needs: the **tangential ratio at `P_inf` is `9/3 = 3`.**

### 1.3 The shape of the answer, stated before the work

Step (1) asks for three things. Two of them are pinned and one is not:

| asked for | verdict |
|---|---|
| contact order of `F` with `L_inf` | **PINNED** to a finite list of 11 profiles (SS2.4) |
| `deg f`, `deg g` | **NOT PINNED**; the admissible set is empty-or-infinite (SS3) |
| a finite admissible degree list | **DOES NOT EXIST** (SS3.2) |

By the card's own stop condition (IDE SS9 Card C: "*Unbounded/degenerate -> step 0
failed; re-cost, do not drift into the banked-tried GGV degree farm*") this is
the `SCOPE-CONFLICT` branch. It is typed as such in SS6 and not drifted.

## 2. Step (1a): what the charged data does pin

Set up once. Let `d := max(deg f, deg g)` and let

```text
   Phi : P^2 --> P^2 ,   [X:Y:Z] |-> [ Z^{d-n} f^ : Z^{d-m} g^ : Z^d ] ,   n = deg f, m = deg g,
```

`f^`, `g^` the homogenisations. The three forms have no common factor (a common
factor divides `Z^d`, and `Z | f^` would force `deg f < n`), so `Phi` has degree
`d` and its base locus lies on `L_inf`. Let `pi : X -> P^2` resolve the
indeterminacy by blowups over `L_inf`, `Phi~ = Phi o pi : X -> P^2` a morphism,
`E := pi^{-1}(L_inf)` the boundary, `X \ E = C^2`. Write `M := Phi~^*(L)` for a
general target line `L`, and `H := pi^*(line)`. `[D]` throughout SS2.

Four facts, each one line:

```text
 (i)   M^2 = deg(Phi~) . L^2 = N = 4                        (projection formula)
 (ii)  M . C = L . Phi~_*(C) = 0    for every contracted C  (contracted: Phi~_*C = 0)
 (iii) M . l = deg(Phi~|_l) . deg(Phi~(l))   for a dicritical l
 (iv)  M . H = d
```

and one more: `Phi~^{-1}(L_inf^{tgt})` misses `C^2` because `F(C^2) subset C^2`,
so the divisor `Phi~^*(L_inf^{tgt}) = sum_{C subset E} c_C . C` is **supported on
the boundary**, with `c_C = 0` exactly on the affine-image dicriticals.

### 2.1 `L~_inf` is contracted

On `Z = 0`: if `n < m = d` then `Phi = [0 : G_m : 0] = [0:1:0]`; if `n = m = d`
then `Jac(F_n,G_m) = 0` (the top-degree part of `Jac(f,g) = 1` must vanish, since
`n+m-2 > 0`), so `F_n = alpha H_0^{n/e}`, `G_m = beta H_0^{m/e}` for a form `H_0`,
and `Phi = [alpha : beta : 0]`. Constant either way. `[D]`

### 2.2 `deg D_2` is divisible by 3

CAGE SS4 cl.1 `[P]`: all components of `A_F` meet `L_inf` in **one common point**,
one place each, of a **common** Newton-Puiseux type, and all degrees are positive
multiples of `max(d,e) >= 2` for that type. SS1.2 computes the type on `D_1`: the
place has `(mult, contact) = (3, 9)`, ratio `3`, in lowest terms `(3,1)`, so
`max(d,e) = 3` — consistent with `3 | 9`. Therefore

```text
   deg D_2 = 3 . mult_{P_inf}(D_2) ,   so   3 | deg D_2   and   deg D_2 >= 3 .   [D]
```

(Lemma NL alone gives only `deg D_2 >= 2`; the floor below is stated both ways.)
Two further consequences of the profile, recorded because they constrain any later
`D_2` job: `corr_{l_2} = mu(s-1) + K = 0` forces `eta_2` **immersive**, and Gate
EMB forbids a smoothly embedded `A^1`, so `D_2` is a singular immersed rational
curve — a cuspidal companion is excluded outright, and degree 3 means a **nodal**
cubic with contact 3 at `P_inf`. `[D]`

### 2.3 The degree identity and its floor

`pi^*L_inf = L~_inf + sum_j nu_j E_j` with every `nu_j >= 1`. Pairing with `M`,
using (ii), (iv) and SS2.1:

```text
 (DIAM)   d  =  max(deg f, deg g)  =  sum over dicriticals l  of  nu_l . (M . l) .
```

Evaluate the three groups of terms with (iii) and `s_{l_1} = s_{l_2} = 1`:

```text
   l_1 :  M . l_1 = 1 . deg D_1 = 9          contributes  9 nu_1  >= 9
   l_2 :  M . l_2 = 1 . deg D_2 >= 3         contributes  >= 3
   l at infinity : M . l = delta_l >= 1      contributes  >= 1     (at least one exists, SS2.4)
```

```text
 (FLOOR)   max(deg f, deg g)  >=  13 .              [D]
           ( >= 12 if one declines CAGE cl.1 and uses Lemma NL only.)
```

This is a **floor, not an attainment**: nothing here says `13` is achieved, and
SS4 shows GGV pushes the real floor to `16`. FALLACY-v2 floor/attainment: held.

### 2.4 The contact order of `F` with `L_inf` — pinned

Pair `M` with its own divisor `Phi~^*(L_inf^{tgt}) = sum c_C C`. By (ii) only
dicriticals survive, and `c_l = 0` on the affine-image ones, so with
`delta_l := deg(Phi~|_l : l -> L_inf^{tgt})`:

```text
 (CONTACT)   sum over dicriticals l at infinity  of  c_l . delta_l  =  M^2  =  N  =  4 .   [D]
```

`c_l = ord_l Phi~^*(L_inf^{tgt}) >= 1` is exactly "the contact order of `F` with
`L_inf`" along the end `l`; `delta_l >= 1`. So the answer to that part of the
charge is a **complete finite list**: the multisets `{(c_l,delta_l)}` with
`sum c_l delta_l = 4`. There are **11**, machine-enumerated:

```text
  r=1 : {(1,4)}  {(2,2)}  {(4,1)}
  r=2 : {(1,1),(1,3)}  {(1,1),(3,1)}  {(1,2),(1,2)}  {(1,2),(2,1)}  {(2,1),(2,1)}
  r=3 : {(1,1),(1,1),(1,2)}  {(1,1),(1,1),(2,1)}
  r=4 : {(1,1),(1,1),(1,1),(1,1)}
```

Necessary conditions only; no claim that any is realised. Note this pins the
*contact*, and `(DIAM)` then reads
`d = 9 nu_1 + nu_2 deg D_2 + sum_{l at inf} nu_l delta_l` — with the `nu_l`
(depths of the dicriticals in the boundary tree) still free. That is where the
degree escapes, and SS3 shows the escape is real, not an artefact of this route.

## 3. Step (1b): the degrees are not pinned

### 3.1 The source action

> **Lemma SRC `[D]`.** Let `S in Aut(C^2)`. Then `F o S` is Keller, has the same
> topological degree `N`, the **same** `A_F`, the same monodromy `rho`, and the
> same carrier profile `{(mu_l,s_l,K_l)}` with the same owner partition.

*Proof.* `Jac(F o S) = (Jac F) o S . Jac S = 1` (machine-confirmed on a worked
pair). `N = [C(x,y):C(f,g)]` is unchanged because `S^*` is a field automorphism
fixing `C(f,g)`. `A_F = { z : exists z_k -> infinity, F(z_k) -> z }` and `S` is a
homeomorphism of `C^2` with `S(z_k) -> infinity iff z_k -> infinity`, so
`A_{F o S} = A_F`. The covering `C^2 \ (F o S)^{-1}(A) -> C^2 \ A` is the covering
`C^2 \ F^{-1}(A) -> C^2 \ A` precomposed with the isomorphism `S^{-1}`, i.e. **the
same covering**; so `rho`, all cycle types, all `a_i` and all `W_i = N - a_i` are
identical. `S` permutes the divisorial valuations of `C(x,y)` at infinity, and the
local data of `F o S` at `v` is the local data of `F` at `S_* v`; so the multiset
of carriers, their owners, and `K_tot` transfer. []

> **Lemma DEG `[D]`.** With `S_k(x,y) = (x, y + x^k)`: for all large `k`,
> `deg(f o S_k) = k . deg_y f + deg_x f_a` where `f_a` is the coefficient of
> `y^{deg_y f}`. In particular `deg(f o S_k) -> infinity`.

*Proof.* `f(x,y+x^k) = sum_j f_j(x)(y+x^k)^j`; the `y^0` part has degree
`max_j(deg f_j + kj) = deg f_a + k a` for large `k`, with leading coefficient
`lc(f_a) != 0`, and the `y^i` part (`i >= 1`) has degree
`deg f_a + ka - i(k-1) <` that. Machine-confirmed on `f = x^5+y^2+3xy`
(`k = 3,4,7` give `6, 8, 14 = 2k`). Finally `deg_y f >= 1`: if `f = f(x)` then
`Jac = f'(x) g_y = 1` forces `f` affine and `g_y` constant, i.e. `F` invertible,
contradicting `N = 4`. []

### 3.2 The verdict

> **PROPOSITION CARD-C-0 `[D]`.** Let `S_C` be the set of pairs
> `(deg f, deg g)` over all `F` realising the charged data (Keller, `N = 4`,
> profile core `(2,1,0)` + trivial, `W = (1,2)`, `A_F = D_1 u D_2` with `D_1` the
> fixed `(9,6,2)` curve). Then **`S_C` is either empty or infinite**, and in the
> second case `max` is unbounded on `S_C`.

*Proof.* Lemma SRC preserves every listed datum, including `D_1` **as a set**;
Lemma DEG makes the degrees unbounded along `{F o S_k}`. []

Three consequences, all `[D]`:

1. **No finite enumeration of degree pairs is complete.** The card's fallback
   ("enumerate the finite set of admissible degree pairs if one exists") has no
   instance here.
2. **`EMPTY` at any finite set of degree pairs is not a kill of `(9,6,2)`.** The
   card's headline interpretation (IDE SS6: "*EMPTY kills `(9,6,2)` at the
   strongest possible level*") is **not available** at any bounded degree. `[X]`
   against IDE SS6 as written — the card's `NONEMPTY` half survives intact (SS5.2).
3. The failure mode is *exactly* the banked one: the search always has a next
   degree pair. That is the `SCOPE-CONFLICT` with Avenue 1 (GGV degree farm) that
   IDE SS11 pre-registered, now realised rather than hypothetical.

### 3.3 What would revive the card

Precisely one missing object, stated so it can be charged:

> `OPEN[CARD-C-SOURCE-NORMAL-FORM]` — a bound on
> `d_src-min(F) := min_{S in Aut(C^2)} max(deg(f o S), deg(g o S))`
> in terms of `N` and `A_F` alone.

This is the **source-side twin** of the campaign's promoted target-side `d_min`
discipline (CAGE SS2.5: "*every degree statement must be phrased for
`d_min = min_T deg T(D)`*"). CAGE handles post-composition and is silent on
pre-composition; nothing promoted, and nothing I could find in the consumed
literature, bounds `d_src-min`. Note the two are genuinely different: target
automorphisms move `A_F` and are controlled by `d_min` on the curve; source
automorphisms **fix `A_F` exactly** and are therefore invisible to every gate in
CAGE SS4 and every invariant in REP SS7. A second, weaker object would also do:
any bound on the depths `nu_l` in `(DIAM)`, since `d` and the `nu_l` bound each
other. `[O]`

A third unboundedness, worth recording because it blocks the card independently:
`deg D_2` is itself unbounded. `(DIAM)` gives `deg D_2 <= d - 10`, a bound *by*
`d`, hence circular; and `D_2` is unknown (`OPEN[REP-96-MPRIME-COMPANION]`). So
"the two germ conditions" of the charge cannot both be written: the second one has
no boundary data. SS5 handles this by dropping it, which is the logically correct
move and is proved to be safe there. `[A]` against the charge's step (2) as worded.

## 4. Step (3): the GGV firewall

### 4.1 Typing check first

Fable SS4c `[P]` (`ideation-20260902T0022Z-fable5.md:159-166`): the bound is on
`(deg P, deg Q)` **of the map**, not on branch-curve parametrisation degrees, and
"*must NOT be consumed against `(9,6)` (gcd 3 there means nothing)*". Held:
`gcd(9,6) = 3` is **not** fed to GGV anywhere below. The objects `9` and `6` in
this report are `deg D_1` and `deg_x`-side parametrisation data of `eta_1`; the
objects `n, m` are `deg f, deg g`. Flag/place/series: three distinct series are
kept apart throughout — the parametrisation degrees `(9,6)`, the curve degree
`deg D_1 = 9`, and the map degrees `(n,m)`.

### 4.2 The check

GGV/Heitmann `[P]` (packet SS4, custody `8b426751`; campaign custody line
`notes.md:5802-5806`): for a counterexample,
`gcd(deg_total(P), deg_total(Q)) >= 16` and `!= 2p` for a prime `p`.

Applied to `(n,m) = (deg f, deg g)`:

```text
   gcd(n,m) >= 16   ==>   min(n,m) >= 16   ==>   d = max(n,m) >= 16 ;
   and if n != m then max(n,m) >= 2 gcd(n,m) >= 32 .
   gcd(n,m) not in {22, 26, 34, 38, 46, ...} = {2p : p prime, 2p >= 16} .
```

**Result: NO VIOLATION, and no desk-level kill.** The geometric floor `(FLOOR)`
`d >= 13` is strictly weaker than GGV's `d >= 16`; the two are compatible
(`(n,m) = (16,16)` satisfies both, and `16 = 2^4` is not `2p`). So GGV does not
kill this configuration, but it does **raise the working floor from 13 to 16**,
which is the number SS5.4 costs the job at.

### 4.3 A derived consequence, and a custody warning it forces

Because Lemma SRC makes every `F o S` a counterexample whenever `F` is one, GGV
applies to **every** pair `(deg(f o S), deg(g o S))`, not just to one normalised
pair. Write `a = deg_y f`, `b = deg_y g`, `alpha = deg_x f_a`, `beta = deg_x g_b`,
`Delta := b alpha - a beta`. Lemma DEG gives `n_k = ka+alpha`, `m_k = kb+beta`.

* If `Delta != 0`: `gcd(n_k,m_k) | b n_k - a m_k = Delta` for all large `k`, so
  GGV's `>= 16` forces `|Delta| >= 16`. `[D]`
* If `Delta = 0`: write `e = gcd(a,b)`, `a = ea'`, `b = eb'`, `gcd(a',b') = 1`;
  then `a' | alpha`, and with `gamma := alpha/a'` one gets `gcd(n_k,m_k) = ke+gamma`.
  GGV's `!= 2p` must then hold along a whole arithmetic progression. Let
  `g_0 = gcd(e,gamma)`. If `g_0` has an odd prime factor `qq`, then `qq | ke+gamma`
  and `ke+gamma = 2p` forces `p = qq`, one value of `k`: safe. If `4 | g_0`: safe
  likewise. If `e` is even and `gamma` odd, `ke+gamma` is always odd: safe. In the
  two remaining cases (`g_0 = 2`; or `g_0 = 1` with `e` odd) the halved progression
  has difference coprime to its first term, and **Dirichlet supplies infinitely
  many primes**, contradicting GGV. Hence `[D]`, conditional:

```text
  (GGV-ORBIT)  4 | gcd(e,gamma) ,  or  gcd(e,gamma) has an odd prime factor ,
               or  e even and gamma odd .
```

This is a necessary condition on any counterexample that the campaign is not
currently consuming, and it is cheap. But it is **conditional on GGV applying to
every Keller pair rather than to a minimal/normalised one**, and the derivation
above is exactly the pressure test of that hypothesis: if the `!= 2p` clause held
for all pairs with no further hypothesis, then the `g_0 in {1 (e odd), 2}` branch
would close JC2 in two lines of Dirichlet — which is strong evidence that a scope
hypothesis is being dropped somewhere in the campaign's transcription of GGV, not
that JC2 is closed. I therefore do **not** promote `(GGV-ORBIT)` and instead raise

> `OPEN[GGV-SCOPE-ALL-PAIRS]` — read the GGV/Heitmann statement at
> `arXiv:1401.1784` (custody `8b426751`) and record whether `gcd >= 16` / `!= 2p`
> is asserted for *every* non-invertible Keller pair or only for a
> degree-minimal one. Every campaign consumer of the bound inherits the answer.
> Until it is answered, SS4.2's check stands (it only uses `>= 16`, which is
> monotone and survives either reading) and `(GGV-ORBIT)` does not. `[O]`

FALLACY-v2 pole/interior: source hypotheses checked before use, and the one that
could not be checked in-lane is named rather than assumed.

## 5. Step (2): the ideal specification

Delivered as charged, conditional on discrete data that SS3 shows is not pinned.
Spec only; **no CAS was run**.

### 5.1 Discrete data that must be fixed before the ideal exists

```text
  (n, m)                     degrees of f and g            -- NOT pinned (SS3.2)
  (e; E_1 > ... > E_{k+1})   the germ type of the dicritical l_1, integers,
                             gcd(e, E_1, ..., E_{k+1}) = 1  -- bounded only once d is
```

The germ model: a divisorial valuation at infinity of `C[x,y]` with residue field
`C(T)` is the generic Puiseux branch

```text
   X(tau) = tau^{-e} ,      Y(tau,T) = sum_{i=1}^{k} c_i tau^{-E_i}  +  T tau^{-E_{k+1}} ,
```

`v(h) := ord_tau h(X,Y)` computed in `C[T]((tau))`. Primitivity
`gcd(e,E_1,...,E_{k+1}) = 1` is what makes `tau` a uniformiser along `l_1`; without
it `v` is a proper multiple and every order below is off by that factor. This is
the variable/ring-map hygiene item of FALLACY-v2 and must carry a positive and a
negative control in the run (SS5.5).

### 5.2 What to impose, and the proof that the short list is the right one

> **Lemma SPEC `[D]`.** Suppose `(f,g)` satisfies `Jac(f,g) = 1` together with
> (G1a)+(G1b) below for some primitive germ type. Then `F = (f,g)` is a Keller map
> that is **not** an automorphism, i.e. a JC2 counterexample.

*Proof.* (G1a)+(G1b) exhibit a one-parameter family of source points going to
infinity whose `F`-images converge to the non-constant curve `t -> (q(t),p(t))`.
So `F` is not proper. Polynomial automorphisms are proper. []

Consequently the job should impose **less**, not more, than the charge lists:

* **Drop `td = 4`.** It is not expressible at coefficient level at any reasonable
  cost, and Lemma SPEC shows it is not needed: dropping it enlarges the solution
  set, so `EMPTY` becomes *stronger* and `NONEMPTY` still resolves JC2 negatively.
* **Drop the `l_2` germ condition.** It cannot be written — `D_2` is unknown
  (SS3.3). Dropping it is safe for the same reason.
* **Drop `mu_1 = 2` exactness.** Keeping only `mu_1 >= 2` (the tangency (G1c))
  avoids an inequation and a `sat()` call. Under the *full* charged profile
  `mu_1 >= 3` is excluded by `(BUD)` anyway; without `td = 4` it is not, but by
  Lemma SPEC it does not matter.
* **Keep (G1c).** Not needed for Lemma SPEC, but it is the only place the charged
  `W = (1,2)` datum enters, and it cuts the system hard. Run both variants: with
  (G1c) as the charged job, without it as the strictly stronger `EMPTY` claim.

### 5.3 Variables and generators

Variables in `QQ[.]`:

```text
   a_{ij} , 0 <= i+j <= n           (n+1)(n+2)/2      coefficients of f
   b_{ij} , 0 <= i+j <= m           (m+1)(m+2)/2      coefficients of g
   c_1, ..., c_k                    k                 germ coefficients
```

Substituting `x = X(tau)`, `y = Y(tau,T)` gives, for `Ff := f(X,Y)` and
`Gg := g(X,Y)`, Laurent expansions with coefficients in `QQ[a,c][T]`, resp.
`QQ[b,c][T]`:

```text
   Ff = sum_{nu >= -n.max(e,E_1)} Phi^f_nu(a,c;T) tau^nu ,      Gg = sum_nu Phi^g_nu(b,c;T) tau^nu .
```

Generators (each line means: expand in `T` and take every coefficient):

```text
 (J)    coefficients of  Jac(f,g) - 1  in QQ[x,y]                    (n+m-1)(n+m)/2 + ... scalars
 (G1a)  Phi^f_nu(a,c;T) = 0  and  Phi^g_nu(b,c;T) = 0   for all nu < 0     [regularity: the germ
                                                                            has a finite limit]
 (G1b)  Phi^f_0(a,c;T) = q(T)  and  Phi^g_0(b,c;T) = p(T)                  [residue = D_1, s = 1;
                                                                            embeds the (9,6,2) data]
 (G1c)  p'(T) . Phi^f_1(a,c;T)  -  q'(T) . Phi^g_1(b,c;T)  =  0            [mu_1 >= 2]
 (N)    5 gauge-fixing linear/affine conditions                            [see SS5.5]
```

with the boundary data entered verbatim:

```text
   q(T) = T^6 + 8T^2 ,        q'(T) = 6T^5 + 16T ,
   p(T) = T^9 + 12T^5 + 24T , p'(T) = 9T^8 + 60T^4 + 24 .
```

**Derivation of (G1c)**, since the charge asks for the germ conditions *as
coefficient equations*. Write `Ff = q(T) + f_1(T)tau + O(tau^2)`,
`Gg = p(T) + g_1(T)tau + O(tau^2)`, and let `H` be the reduced equation of `D_1`.
Then `H(Ff,Gg) = [H_x(q,p) f_1 + H_y(q,p) g_1] tau + O(tau^2)`. Differentiating
`H(q(T),p(T)) = 0` gives `H_x q' + H_y p' = 0`, and `(q',p') != (0,0)` for every
`T` (`gcd(q',p') = 1`, SS1.2), so `(H_x,H_y) = lambda(T)(p', -q')` with
`lambda != 0` generically. Hence

```text
   mu_1 = ord_tau H(Ff,Gg) >= 2   <=>   p'(T) f_1(T) - q'(T) g_1(T) = 0 in QQ[T] ,
```

which is (G1c) with `f_1 = Phi^f_1`, `g_1 = Phi^g_1`. `[D]` The unknown `H` has
been eliminated — the equation uses only the parametrisation, which is the whole
point of prescribing `D_1` by `(q,p)` rather than implicitly.

### 5.4 Size at the smallest GGV-admissible instance

At the GGV floor `(n,m) = (16,16)` (SS4.2), machine-counted:

```text
   coefficient unknowns          306   ( + k germ unknowns )
   (J) scalar equations          496
   (G1a) scalar equations        <= 2 . n . max(e,E_1) . (n+1)  -- e.g. 4896 at max(e,E_1) = 9
   (G1b)+(G1c) scalar equations  ~ 3(n+1) + (n + deg p)
```

Roughly **310 unknowns against several thousand equations over `QQ`**, and the
next admissible pair if `n != m` is `(16,32)` with **714 unknowns**. msolve 0.10.1
decides dense rational systems in the tens of variables. So even with the degrees
granted, this instance is outside the solver by two orders of magnitude in the
variable count — a second, independent block, and one that does not go away by
picking a luckier degree pair, since GGV forbids everything below `16`.

### 5.5 Run discipline, if the job is ever unblocked

Mandatory, from the standing lane discipline and FALLACY-v2:

1. **Gauge.** The solution set is invariant under the 5-dimensional source group
   `SL_2 |x C^2` (which preserves `Jac = 1` and all degrees), so it is never
   zero-dimensional and point extraction will fail unless 5 normalisation
   equations `(N)` are added; the germ type partially consumes this group, so the
   residual gauge must be computed, not assumed. Verdict typing must otherwise be
   `dim >= 0`, never "no points".
2. **`sat()`.** Only needed in the `mu_1 = 2`-exact variant; if used, extract the
   ideal component, assert its ring, and run both controls.
3. **Controls.** Positive: a *non-Keller* map with a known weight-2 dicritical over
   a known curve must make the corresponding system NONEMPTY. Negative: replacing
   `(q,p)` by a parametrisation with `gcd(q',p') != 1` must break (G1c)'s
   derivation and be caught, not silently pass.
4. **Verdict typing.** `EMPTY` at `(n,m,germ type)` means *only* that: by
   PROPOSITION CARD-C-0 it is not a statement about `(9,6,2)`.

## 6. Verdict, OPENs, deviations

```text
LANE            CARD-C-STEP0  (blocking desk step for IDE SS6/SS9 Card C)
STEP (1)        CONTACT ORDER: PINNED -- (CONTACT) sum c_l delta_l = 4 ; 11 profiles.
                DEGREES: NOT PINNED.  PROPOSITION CARD-C-0: the admissible set of
                (deg f, deg g) is EMPTY OR INFINITE.  No finite admissible list exists.
                Derived floor (FLOOR): max(deg f,deg g) >= 13  [>= 12 without CAGE cl.1].
                Derived: 3 | deg D_2 , deg D_2 >= 3 , D_2 immersed and singular.
STEP (2)        DELIVERED as a spec family indexed by (n,m; e,E_*), SS5.3, with the
                (9,6,2) parametrisation embedded and (G1c) derived at coefficient level.
                Three charged conditions shown SAFE TO DROP (Lemma SPEC), one shown
                UNWRITABLE (the l_2 germ: D_2 unknown).
STEP (3)        GGV: NO VIOLATION.  gcd >= 16 raises the floor 13 -> 16 (-> 32 if n != m).
                Typing firewall held: gcd(9,6) = 3 not consumed.
CARD VERDICT    Card C DIES AT STEP 0 as charged: SCOPE-CONFLICT with the banked-tried
                GGV degree farm, exactly the pre-registered failure branch (IDE SS11).
                It dies a second, independent time on solver size at the GGV floor (SS5.4).
                The NONEMPTY half is unaffected in principle but has no bounded search.
NOT CLAIMED     Nothing about the realizability of (9,6,2).  No gate is closed, no row
                is killed, no exit price is asserted.
```

**OPENs raised.**

* `OPEN[CARD-C-SOURCE-NORMAL-FORM]` (SS3.3) — bound `d_src-min` in terms of `N`
  and `A_F`. This is the *only* thing that revives Card C, and it is the
  source-side twin of the promoted target-side `d_min` discipline. Highest-value
  successor here.
* `OPEN[GGV-SCOPE-ALL-PAIRS]` (SS4.3) — does GGV's bound hold for every Keller
  pair or only a minimal one? Cheap (one primary-source read), and every campaign
  consumer of the bound inherits the answer.
* `OPEN[CARD-C-D1-MODULI]` — the charge fixes *the* realized `(9,6,2)` curve.
  Nothing consumed says `(9,6,2)` curves form a single `Aut(C^2)`-orbit, so even a
  hypothetical `EMPTY` would be about this curve, not about the numerical type.

**Deviations from the charge, logged.**

1. The charge asks to "derive `deg f`, `deg g`". They are not derivable; I derived
   instead the exact obstruction (PROPOSITION CARD-C-0), the floor, and the
   pinned contact data, and reported the failure in the card's own typed language
   rather than substituting a bounded search. This is the charged behaviour for
   the unbounded branch.
2. The charge asks for "the two germ conditions". Only one is writable; SS3.3 and
   SS5.2 say why and prove that dropping the second is logically safe.
3. `[X]` against IDE SS6's headline: "`EMPTY` kills `(9,6,2)` at the strongest
   possible level" is withdrawn as a description of any *bounded-degree* run. The
   `NONEMPTY` half of IDE SS6 is not withdrawn.
4. `(GGV-ORBIT)` (SS4.3) is derived but deliberately **not promoted**, because
   promoting it would make an implausibly strong claim depend on an unverified
   scope reading. It is parked behind `OPEN[GGV-SCOPE-ALL-PAIRS]`.

## 7. FALLACY-v2 audit

* **Flag/place/series.** Three series kept strictly apart in SS4.1: the
  parametrisation degrees `(9,6)` of `eta_1`, the curve degree `deg D_1 = 9`, and
  the map degrees `(deg f, deg g)`. `gcd(9,6)` is never fed to GGV. In SS2 the
  boundary `E`, the dicriticals `l`, and the target line `L_inf^{tgt}` are three
  different objects, and `c_l` (contact with the *target* line at infinity) is
  never confused with `nu_l` (multiplicity in the *source* `pi^*L_inf`).
* **Floor/attainment.** `(FLOOR) d >= 13` is stated as a floor throughout and is
  explicitly *not* claimed attained; SS4.2 then shows the operative floor is 16.
  `(CONTACT)`'s 11 profiles are necessary conditions, not realisations.
* **Carrier/attainment.** Lemma SPEC gives a sufficient condition for a
  counterexample (`NONEMPTY` branch) and is proved; no `EMPTY` result is claimed
  or simulated, and SS5.5(4) types what `EMPTY` would and would not mean.
* **`sat()` wrapping / raw remainder.** No Groebner computation, saturation or
  normal form was run in this lane. SS5.5 carries the discipline forward to any
  successor run, including the ring assertion and both controls.
* **Variable/ring map.** SS5.1 declares the substitution `x = tau^{-e}`,
  `y = sum c_i tau^{-E_i} + T tau^{-E_{k+1}}`, the coefficient field `QQ`, the
  primitivity condition that makes `tau` a uniformiser, and flags that the whole
  order bookkeeping is wrong by a constant factor if primitivity is dropped.
* **Pole/interior.** GGV is consumed only through `>= 16`, which is monotone under
  either reading of its scope; the `!= 2p` clause is used only inside an
  explicitly conditional derivation whose purpose is to test that scope.
* **Prime label/derivative.** `q'`, `p'` in SS5.3 are genuine `d/dT` derivatives of
  the given polynomials, written out explicitly; `f_1`, `g_1` are `tau`-expansion
  coefficients and carry a subscript, not a prime, for exactly this reason.
* **Exit claim.** None. No `charge_basis` line, because no exit-price assertion is
  made anywhere in this report.

## Seal

```text
REPORT   xmodel/card-c-step0-opus5-20260902.md
INPUTS   dcd40a42... ideation-20260902T0022Z-opus5.md      VERIFIED
         a47945ab... rep-96-inner-opus5-20260901.md        VERIFIED
         bdd857c9... reducible-all-n-r2-opus5-20260901.md  VERIFIED
CAS      none run (charge: spec only).  Scripts: sympy degree/series arithmetic
         and one integer enumeration, disclosed SS0.3, all results hand-checkable.
STATUS   Step (1) answered NEGATIVE with proof; steps (2) and (3) delivered.
         Card C: DEAD AT STEP 0, SCOPE-CONFLICT (typed), revivable only by
         OPEN[CARD-C-SOURCE-NORMAL-FORM].
```
