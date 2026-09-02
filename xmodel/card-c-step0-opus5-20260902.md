# CARD-C-STEP0: pinning the degrees for the direct `F` solve

Lane: `CARD-C-STEP0`. Agent: Opus 5. Desk-scale exact reasoning. No CAS decision
procedure, no Groebner basis, no resultant, no saturation was run: the charge
forbids it and nothing below needs it. Three short scripts re-did by machine what
was also checked by hand; disclosed in SS0.3, every number re-derivable on paper.

## 0. Custody, method, scope

### 0.1 Input verification

The three frozen charged copies hash as declared; this was the first action.

```text
dcd40a425b2a2782deebec3f01c3b6859a8aa8d46b3e60639f9865a807d5ddba  ideation-20260902T0022Z-opus5.md
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  rep-96-inner-opus5-20260901.md
bdd857c9d8c55fa000fcffee05f9f3084c5d073fb4d06285edf2af0d3c369339  reducible-all-n-r2-opus5-20260901.md
```

**IDE** = the ideation report (Card C is its SS6/SS9), **REP** = REP-96-INNER,
**CAGE** = CAGE-N-R2. Also read on disk, cited by file/line, not re-hashed as
primary: `ideation-20260902T0022Z-fable5.md:134-166` (GGV firewall SS4c),
`ideation-20260902T0022Z-packet.md:63-66` (the GGV bound as the packet states it),
`notes.md:5802-5806` (campaign custody line for `gcd >= 16`),
`reducible-all-n-opus5-20260901.md:36-100` (r1 SS1, the `(mu,s,K)`/`W_i`/`(LOC)`
definitions r2 uses without restating).

### 0.2 Typing

`[D]` derived here; `[P]` promoted/consumed from a charged input at its stated
scope; `[O]` typed OPEN; `[X]` withdrawn/refuted; `[A]` audit against a consumed
item. Nothing below is an attainment claim. No exit price is asserted, so no
`charge_basis` line is given (FALLACY-v2).

### 0.3 Machine disclosure

1. exact rational check of the `(9,6,2)` identity, degrees, `gcd(q',p')`, the
   orders `ord_s(X/Y)=3`, `ord_s(Z/Y)=9` at `P_inf`, and the gaps of `<2,9>` —
   already in REP SS1, redone independently because SS2.1's divisibility
   conclusion is load-bearing;
2. integer enumeration of the contact profiles of SS2.3 (11 of them);
3. degree arithmetic confirming `deg(f o S_k) = k deg_y f + deg_x f_a` and
   `Jac(f o S, g o S) = Jac(f,g) o S` on a worked pair (SS3.1).

## 1. What the charge fixes, and the shape of the answer

### 1.1 The configuration

`F = (f,g) : C^2 -> C^2` polynomial, `Jac(f,g) = 1`, topological degree
`td = N = 4`, non-proper. `A_F = D_1 u D_2` (CAGE SS3.5: the unique `N = 4`
profile is core `(2,1,0)` plus one trivial on a second owner, `W = (1,2)`,
class `[2]`, `b = 1`). So:

* `D_1` owns one carrier `(mu,s,K) = (2,1,0)`, `W_1 = 2`, `a_1 = 2`, meridian a
  transposition; `D_1` = the realized `(9,6,2)` curve, parametrised
  `eta_1 : t -> (q(t),p(t)) = (t^6+8t^2,\ t^9+12t^5+24t)`.
* `D_2` owns one trivial carrier `(1,1,0)`, `W_2 = 1`, `a_2 = 3`, `gamma_2 = id`.
  `D_2` is **not known** (`OPEN[REP-96-MPRIME-COMPANION]`, REP SS7 R4).
* Budget `(BUD)` `2+1 = 3 = N-1` is saturated, so there are **exactly two**
  affine-image dicriticals `l_1 -> D_1`, `l_2 -> D_2`, both with `s = 1`. `[P]`

### 1.2 The `(9,6,2)` place, re-derived

At `P_inf = [0:1:0]`, local coordinates `u = X/Y`, `v = Z/Y`, `s = 1/t`:

```text
   ord_s(u) = 3 = mult_{P_inf}(D_1) = a ,     ord_s(v) = 9 = (D_1 . L_inf)_{P_inf} = deg D_1 .
```

Both machine-confirmed, together with `p^2 - q^3 - 64q - 64t^2 = 0` exactly,
`deg q = 6`, `deg p = 9`, `gcd(q',p') = 1`, `S_aff = <2,9>`, gaps `{1,3,5,7}`,
`delta_aff = 4`. This reproduces REP SS1 by an independent route and supplies the
number SS2.1 needs: the **tangential ratio at `P_inf` is `9/3 = 3`.**

### 1.3 The shape of the answer, stated before the work

Step (1) asks for three things; two are pinned and one is not.

| asked for | verdict |
|---|---|
| contact order of `F` with `L_inf` | **PINNED** to a finite list of 11 profiles (SS2.3) |
| `deg f`, `deg g` | **NOT PINNED**; the admissible set is empty-or-infinite (SS3) |
| a finite admissible degree list | **DOES NOT EXIST** (SS3.2) |

By the card's own stop condition (IDE SS9 Card C: "*Unbounded/degenerate -> step 0
failed; re-cost, do not drift into the banked-tried GGV degree farm*") this is
the `SCOPE-CONFLICT` branch. It is typed as such in SS6 and not drifted.

## 2. Step (1a): what the charged data does pin

Let `d := max(deg f, deg g)` and let

```text
   Phi : P^2 --> P^2 ,   [X:Y:Z] |-> [ Z^{d-n} f^ : Z^{d-m} g^ : Z^d ] ,   n = deg f, m = deg g,
```

`f^`, `g^` the homogenisations. The three forms have no common factor (a common
factor divides `Z^d`, and `Z | f^` would force `deg f < n`), so `Phi` has degree
`d` and its base locus lies on `L_inf`. Let `pi : X -> P^2` resolve the
indeterminacy by blowups over `L_inf`, `Phi~ = Phi o pi : X -> P^2` a morphism,
`E := pi^{-1}(L_inf)`, `X \ E = C^2`. Write `M := Phi~^*(L)` for a general target
line `L`, `H := pi^*(line)`. `[D]` throughout SS2. Four one-line facts:

```text
 (i)   M^2 = deg(Phi~) . L^2 = N = 4                        (projection formula)
 (ii)  M . C = L . Phi~_*(C) = 0    for every contracted C  (contracted: Phi~_*C = 0)
 (iii) M . l = deg(Phi~|_l) . deg(Phi~(l))   for a dicritical l
 (iv)  M . H = d
```

and one more: `Phi~^{-1}(L_inf^{tgt})` misses `C^2` because `F(C^2) subset C^2`,
so the divisor `Phi~^*(L_inf^{tgt}) = sum_{C subset E} c_C . C` is **supported on
the boundary**, with `c_C = 0` exactly on the affine-image dicriticals.

**`L~_inf` is contracted** `[D]`: on `Z = 0`, if `n < m = d` then
`Phi = [0:G_m:0] = [0:1:0]`; if `n = m = d` then `Jac(F_n,G_m) = 0` (the
degree-`n+m-2` part of `Jac(f,g) = 1` vanishes), so `F_n = alpha H_0^{n/e}`,
`G_m = beta H_0^{m/e}` for a form `H_0` and `Phi = [alpha:beta:0]`. Constant either
way. This is used twice below.

### 2.1 `deg D_2` is divisible by 3

CAGE SS4 cl.1 `[P]`: all components of `A_F` meet `L_inf` in **one common point**,
one place each, of a **common** Newton-Puiseux type `u = c v^{d_0/e_0}`, and all
degrees are positive multiples of `max(d_0,e_0) >= 2`. (CAGE's letters `d_0,e_0`
are renamed here: `d` and `e` are already taken, by `max(deg f,deg g)` and by the
germ index of SS5.1.) SS1.2 computes the type on `D_1`: the place has
`(mult, contact) = (3,9)`, ratio `3`, lowest terms `(3,1)`, so `max(d_0,e_0) = 3`
— consistent with `3 | 9`. Therefore

```text
   deg D_2 = 3 . mult_{P_inf}(D_2) ,   so   3 | deg D_2   and   deg D_2 >= 3 .   [D]
```

(Lemma NL alone gives only `deg D_2 >= 2`; the floor below is stated both ways.)
Two further profile consequences, recorded because they constrain any later `D_2`
job: `corr_{l_2} = mu(s-1) + K = 0` forces `eta_2` **immersive**, and Gate EMB
forbids a smoothly embedded `A^1`, so `D_2` is a singular immersed rational curve
— a cuspidal companion is excluded outright, and degree 3 forces a **nodal** cubic
with contact 3 at `P_inf`. `[D]`

### 2.2 The degree identity and its floor

`pi^*L_inf = L~_inf + sum_j nu_j E_j` with every `nu_j >= 1`. Pairing with `M` and
using (ii), (iv) and the contraction of `L~_inf`:

```text
 (DIAM)   d  =  max(deg f, deg g)  =  sum over dicriticals l  of  nu_l . (M . l) .
```

Evaluate with (iii) and `s_{l_1} = s_{l_2} = 1`:

```text
   l_1 :  M . l_1 = 1 . deg D_1 = 9          contributes  9 nu_1  >= 9
   l_2 :  M . l_2 = 1 . deg D_2 >= 3         contributes  >= 3
   l at infinity : M . l = delta_l >= 1      contributes  >= 1     (at least one exists, SS2.3)
```

```text
 (FLOOR)   max(deg f, deg g)  >=  13 .              [D]
           ( >= 12 if one declines CAGE cl.1 and uses Lemma NL only.)
```

This is a **floor, not an attainment**: nothing here says `13` is achieved, and
SS4 shows GGV pushes the real floor to `16`. FALLACY-v2 floor/attainment: held.

### 2.3 The contact order of `F` with `L_inf` — pinned

Pair `M` with its own divisor `Phi~^*(L_inf^{tgt}) = sum c_C C`. By (ii) only
dicriticals survive, and `c_l = 0` on the affine-image ones, so with
`delta_l := deg(Phi~|_l : l -> L_inf^{tgt})`:

```text
 (CONTACT)   sum over dicriticals l at infinity  of  c_l . delta_l  =  M^2  =  N  =  4 .   [D]
```

`c_l = ord_l Phi~^*(L_inf^{tgt}) >= 1` is exactly "the contact order of `F` with
`L_inf`" along the end `l`, and `delta_l >= 1`. So that part of the charge has a
**complete finite answer**: the multisets `{(c_l,delta_l)}` with
`sum c_l delta_l = 4`. There are **11**, machine-enumerated:

```text
  r=1 : {(1,4)}  {(2,2)}  {(4,1)}
  r=2 : {(1,1),(1,3)}  {(1,1),(3,1)}  {(1,2),(1,2)}  {(1,2),(2,1)}  {(2,1),(2,1)}
  r=3 : {(1,1),(1,1),(1,2)}  {(1,1),(1,1),(2,1)}
  r=4 : {(1,1),(1,1),(1,1),(1,1)}
```

Necessary conditions only; no claim that any is realised. This pins the *contact*,
and `(DIAM)` then reads `d = 9 nu_1 + nu_2 deg D_2 + sum_{l at inf} nu_l delta_l`
with the `nu_l` (depths in the boundary tree) still free. That is where the degree
escapes, and SS3 shows the escape is real, not an artefact of this route.

## 3. Step (1b): the degrees are not pinned

### 3.1 The source action

> **Lemma SRC `[D]`.** Let `S in Aut(C^2)`. Then `F o S` is Keller, has the same
> topological degree `N`, the **same** `A_F`, the same monodromy `rho`, and the
> same carrier profile `{(mu_l,s_l,K_l)}` with the same owner partition.

*Proof.* `Jac(F o S) = (Jac F) o S . Jac S = 1` (machine-confirmed on a worked
pair). `N = [C(x,y):C(f,g)]` is unchanged: `S^*` is a field automorphism fixing
`C(f,g)`. `A_F = {z : exists z_k -> infinity, F(z_k) -> z}` and `S` is a
homeomorphism with `S(z_k) -> infinity iff z_k -> infinity`, so `A_{F o S} = A_F`.
The covering `C^2 \ (F o S)^{-1}(A) -> C^2 \ A` is `C^2 \ F^{-1}(A) -> C^2 \ A`
precomposed with the isomorphism `S^{-1}`, i.e. **the same covering**; so `rho`,
all cycle types, all `a_i` and all `W_i = N - a_i` are identical. `S` permutes the
divisorial valuations at infinity and the local data of `F o S` at `v` is that of
`F` at `S_* v`, so the carrier multiset, its owners, and `K_tot` transfer. []

> **Lemma DEG `[D]`.** With `S_k(x,y) = (x, y + x^k)`: for all large `k`,
> `deg(f o S_k) = k . deg_y f + deg_x f_a` where `f_a` is the coefficient of
> `y^{deg_y f}`. In particular `deg(f o S_k) -> infinity`.

*Proof.* `f(x,y+x^k) = sum_j f_j(x)(y+x^k)^j`; the `y^0` part has degree
`max_j(deg f_j + kj) = deg f_a + ka` for large `k`, leading coefficient
`lc(f_a) != 0`, and the `y^i` part (`i >= 1`) has degree `deg f_a + ka - i(k-1)`,
strictly less. Machine-confirmed on `f = x^5+y^2+3xy` (`k = 3,4,7` give
`6,8,14 = 2k`). And `deg_y f >= 1`: `f = f(x)` makes `Jac = f'(x)g_y = 1` force `f`
affine and `g_y` constant, i.e. `F` invertible, against `N = 4`. []

### 3.2 The verdict

> **PROPOSITION CARD-C-0 `[D]`.** Let `S_C` be the set of pairs
> `(deg f, deg g)` over all `F` realising the charged data (Keller, `N = 4`,
> profile core `(2,1,0)` + trivial, `W = (1,2)`, `A_F = D_1 u D_2` with `D_1` the
> fixed `(9,6,2)` curve). Then **`S_C` is either empty or infinite**, and in the
> second case `max` is unbounded on `S_C`.

*Proof.* Lemma SRC preserves every listed datum, including `D_1` **as a set**;
Lemma DEG makes the degrees unbounded along `{F o S_k}`. []

Three consequences, all `[D]`:

1. **No finite enumeration of degree pairs is complete**: the card's fallback
   ("enumerate the finite set of admissible degree pairs if one exists") has no
   instance here.
2. **`EMPTY` at any finite set of degree pairs is not a kill of `(9,6,2)`.** IDE
   SS6's headline ("*EMPTY kills `(9,6,2)` at the strongest possible level*") is
   **not available** at any bounded degree. `[X]` against IDE SS6 as written; the
   card's `NONEMPTY` half survives intact (SS5.2).
3. The failure mode is *exactly* the banked one — the search always has a next
   degree pair. That is the `SCOPE-CONFLICT` with Avenue 1 (GGV degree farm) that
   IDE SS11 pre-registered, now realised rather than hypothetical.

### 3.3 What would revive the card

Precisely one missing object, stated so it can be charged:

> `OPEN[CARD-C-SOURCE-NORMAL-FORM]` — a bound on
> `d_src-min(F) := min_{S in Aut(C^2)} max(deg(f o S), deg(g o S))`
> in terms of `N` and `A_F` alone.

This is the **source-side twin** of the promoted target-side `d_min` discipline
(CAGE SS2.5: "*every degree statement must be phrased for `d_min = min_T deg T(D)`*").
CAGE handles post-composition and is silent on pre-composition; nothing promoted
bounds `d_src-min`. The two are genuinely different: target automorphisms move
`A_F` and are controlled by `d_min` on the curve; source automorphisms **fix `A_F`
exactly** and are therefore invisible to every gate in CAGE SS4 and every
invariant in REP SS7. A bound on the depths `nu_l` in `(DIAM)` would serve equally,
since `d` and the `nu_l` bound each other. `[O]`

A third unboundedness blocks the card independently: `deg D_2`. `(DIAM)` gives
`deg D_2 <= d - 10`, a bound *by* `d`, hence circular; and `D_2` is unknown
(`OPEN[REP-96-MPRIME-COMPANION]`). So "the two germ conditions" of the charge
cannot both be written — the second has no boundary data. SS5 drops it and proves
that safe. `[A]` against the charge's step (2) as worded.

## 4. Step (3): the GGV firewall

### 4.1 Typing check first

Fable SS4c `[P]` (`ideation-20260902T0022Z-fable5.md:159-166`): the bound is on
`(deg P, deg Q)` **of the map**, not on branch-curve parametrisation degrees, and
"*must NOT be consumed against `(9,6)` (gcd 3 there means nothing)*". Held:
`gcd(9,6) = 3` is **not** fed to GGV anywhere below. Three series are kept apart
throughout — the parametrisation degrees `(9,6)` of `eta_1`, the curve degree
`deg D_1 = 9`, and the map degrees `(n,m) = (deg f, deg g)`.

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

**Result: NO VIOLATION, no desk-level kill.** `(FLOOR)`'s `d >= 13` is strictly
weaker than GGV's `d >= 16`, and the two are compatible (`(n,m) = (16,16)` meets
both; `16 = 2^4` is not `2p`). GGV does not kill this configuration, but it
**raises the working floor 13 -> 16**, the number SS5.4 costs the job at.

### 4.3 A derived consequence, and a custody warning it forces

Lemma SRC makes every `F o S` a counterexample whenever `F` is one, so GGV applies
to **every** pair `(deg(f o S), deg(g o S))`, not just one normalised pair. Write
`a = deg_y f`, `b = deg_y g`, `alpha = deg_x f_a`, `beta = deg_x g_b`,
`Delta := b alpha - a beta`; Lemma DEG gives `n_k = ka+alpha`, `m_k = kb+beta`.

* `Delta != 0`: `gcd(n_k,m_k) | b n_k - a m_k = Delta`, so `>= 16` forces
  `|Delta| >= 16`. `[D]`
* `Delta = 0`: with `e = gcd(a,b)`, `a = ea'`, `b = eb'`, `gcd(a',b') = 1`, one gets
  `a' | alpha`; with `gamma := alpha/a'`, `gcd(n_k,m_k) = ke+gamma`, so `!= 2p` must
  hold along a whole arithmetic progression. Put `g_0 = gcd(e,gamma)`. If `g_0` has
  an odd prime factor `qq`, then `qq | ke+gamma` and `ke+gamma = 2p` forces
  `p = qq`, one `k`: safe. `4 | g_0`: likewise (`p = 2`). `e` even and `gamma` odd:
  `ke+gamma` always odd, safe. In the two remaining cases (`g_0 = 2`; `g_0 = 1`
  with `e` odd) the halved progression has difference coprime to its first term and
  **Dirichlet supplies infinitely many primes**, contradicting GGV. `[D]`,
  conditional:

```text
  (GGV-ORBIT)  4 | gcd(e,gamma) ,  or  gcd(e,gamma) has an odd prime factor ,
               or  e even and gamma odd .
```

This is a cheap necessary condition the campaign is not currently consuming. But
it is **conditional on GGV applying to every Keller pair rather than to a
minimal/normalised one**, and the derivation is exactly the pressure test of that
hypothesis: if `!= 2p` held for all pairs with no further hypothesis, the
`g_0 in {1 (e odd), 2}` branch would close JC2 in two lines of Dirichlet — strong
evidence that a scope hypothesis is being dropped in the campaign's transcription
of GGV, not that JC2 is closed. I therefore do **not** promote `(GGV-ORBIT)`, and
raise instead

> `OPEN[GGV-SCOPE-ALL-PAIRS]` — read the GGV/Heitmann statement at
> `arXiv:1401.1784` (custody `8b426751`) and record whether `gcd >= 16` / `!= 2p`
> is asserted for *every* non-invertible Keller pair or only for a degree-minimal
> one. Every campaign consumer inherits the answer. Until it is answered, SS4.2's
> check stands (it uses only `>= 16`, monotone under either reading) and
> `(GGV-ORBIT)` does not. `[O]`

## 5. Step (2): the ideal specification

Delivered as charged, conditional on discrete data SS3 shows is not pinned. Spec
only; **no CAS was run**.

### 5.1 Discrete data that must be fixed before the ideal exists

```text
  (n, m)                     degrees of f and g            -- NOT pinned (SS3.2)
  (e; E_1 > ... > E_{k+1})   the germ type of the dicritical l_1, integers,
                             gcd(e, E_1, ..., E_{k+1}) = 1  -- bounded only once d is
```

Germ model: a divisorial valuation at infinity of `C[x,y]` with residue field
`C(T)` is the generic Puiseux branch

```text
   X(tau) = tau^{-e} ,      Y(tau,T) = sum_{i=1}^{k} c_i tau^{-E_i}  +  T tau^{-E_{k+1}} ,
```

`v(h) := ord_tau h(X,Y)` computed in `C[T]((tau))`. Primitivity makes `tau` a
uniformiser along `l_1`; without it `v` is a proper multiple and every order below
is off by that factor. This is the variable/ring-map hygiene item of FALLACY-v2 and
needs both controls in the run (SS5.5).

### 5.2 What to impose, and the proof that the short list is the right one

> **Lemma SPEC `[D]`.** Suppose `(f,g)` satisfies `Jac(f,g) = 1` together with
> (G1a)+(G1b) below for some primitive germ type. Then `F = (f,g)` is a Keller map
> that is **not** an automorphism, i.e. a JC2 counterexample.

*Proof.* (G1a)+(G1b) exhibit a one-parameter family of source points going to
infinity whose `F`-images converge to the non-constant curve `t -> (q(t),p(t))`.
So `F` is not proper; polynomial automorphisms are proper. []

So the job should impose **less**, not more, than the charge lists:

* **Drop `td = 4`.** Not expressible at coefficient level at any reasonable cost,
  and Lemma SPEC shows it is not needed: dropping it enlarges the solution set, so
  `EMPTY` becomes *stronger* and `NONEMPTY` still resolves JC2 negatively.
* **Drop the `l_2` germ condition.** It cannot be written (`D_2` unknown, SS3.3);
  dropping it is safe for the same reason.
* **Drop `mu_1 = 2` exactness.** Keeping only `mu_1 >= 2` (tangency (G1c)) avoids
  an inequation and a `sat()` call. `mu_1 >= 3` is excluded by `(BUD)` under the
  full profile; without `td = 4` it is not, but by Lemma SPEC that does not matter.
* **Keep (G1c).** Not needed for Lemma SPEC, but it is the only place the charged
  `W = (1,2)` datum enters and it cuts the system hard. Run both variants: with
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
 (J)    coefficients of  Jac(f,g) - 1  in QQ[x,y]                    (n+m-1)(n+m)/2 scalars
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

**Derivation of (G1c)** (the charge asks for the germ conditions *as coefficient
equations*). Write `Ff = q(T) + f_1(T)tau + O(tau^2)`,
`Gg = p(T) + g_1(T)tau + O(tau^2)`; let `Psi` be the reduced equation of `D_1`
(distinct from SS2's `H = pi^*(line)`). Then
`Psi(Ff,Gg) = [Psi_x(q,p) f_1 + Psi_y(q,p) g_1] tau + O(tau^2)`. Differentiating
`Psi(q(T),p(T)) = 0` gives `Psi_x q' + Psi_y p' = 0`, and `(q',p') != (0,0)` for
every `T` (`gcd(q',p') = 1`, SS1.2), so `(Psi_x,Psi_y) = lambda(T)(p',-q')` with
`lambda != 0` generically. Hence

```text
   mu_1 = ord_tau Psi(Ff,Gg) >= 2   <=>   p'(T) f_1(T) - q'(T) g_1(T) = 0 in QQ[T] ,
```

which is (G1c) with `f_1 = Phi^f_1`, `g_1 = Phi^g_1`. `[D]` The unknown `Psi` is
eliminated: the equation uses only the parametrisation, which is the point of
prescribing `D_1` by `(q,p)` rather than implicitly.

### 5.4 Size at the smallest GGV-admissible instance

At the GGV floor `(n,m) = (16,16)` (SS4.2), machine-counted:

```text
   coefficient unknowns          306   ( + k germ unknowns )
   (J) scalar equations          496
   (G1a) scalar equations        <= 2 . n . max(e,E_1) . (n+1)  -- e.g. 4896 at max(e,E_1) = 9
   (G1b)+(G1c) scalar equations  ~ 3(n+1) + (n + deg p)
```

Roughly **310 unknowns against several thousand equations over `QQ`**; the next
admissible pair if `n != m` is `(16,32)`, with **714 unknowns**. msolve 0.10.1
decides dense rational systems in the tens of variables. Even with the degrees
granted, this instance is outside the solver by two orders of magnitude in the
variable count — a second, independent block, and one no luckier degree pair
removes, since GGV forbids everything below `16`.

### 5.5 Run discipline, if the job is ever unblocked

Mandatory, from the standing lane discipline and FALLACY-v2:

1. **Gauge.** The solution set is invariant under the 5-dimensional source group
   `SL_2 |x C^2` (it preserves `Jac = 1` and all degrees), so it is never
   zero-dimensional and point extraction fails unless `(N)` is added; the germ type
   partially consumes this group, so the residual gauge must be computed.
2. **`sat()`.** Only in the `mu_1 = 2`-exact variant; if used, extract the ideal
   component, assert its ring, run both controls.
3. **Controls.** Positive: a *non-Keller* map with a known weight-2 dicritical over
   a known curve must return NONEMPTY. Negative: replacing `(q,p)` by a
   parametrisation with `gcd(q',p') != 1` must break (G1c)'s derivation and be
   caught, not silently pass.
4. **Verdict typing.** `EMPTY` at `(n,m,germ type)` means only that; by
   PROPOSITION CARD-C-0 it is not a statement about `(9,6,2)`.

## 6. Verdict, OPENs, deviations

```text
LANE          CARD-C-STEP0  (blocking desk step for IDE SS6/SS9 Card C)
STEP (1)      CONTACT ORDER: PINNED -- (CONTACT) sum c_l delta_l = 4 ; 11 profiles.
              DEGREES: NOT PINNED.  PROPOSITION CARD-C-0: the admissible set of
              (deg f, deg g) is EMPTY OR INFINITE; no finite admissible list exists.
              Floor (FLOOR): max(deg f,deg g) >= 13  [>= 12 without CAGE cl.1].
              Also derived: 3 | deg D_2 , deg D_2 >= 3 , D_2 immersed and singular.
STEP (2)      DELIVERED as a spec family indexed by (n,m; e,E_*), SS5.3, with the
              (9,6,2) parametrisation embedded and (G1c) derived at coefficient
              level.  Three charged conditions SAFE TO DROP (Lemma SPEC); one
              UNWRITABLE (the l_2 germ -- D_2 unknown).
STEP (3)      GGV: NO VIOLATION.  gcd >= 16 raises the floor 13 -> 16 (32 if n != m).
              Typing firewall held: gcd(9,6) = 3 not consumed.
CARD VERDICT  DIES AT STEP 0 as charged: SCOPE-CONFLICT with the banked-tried GGV
              degree farm, the pre-registered failure branch (IDE SS11).  Dies a
              second, independent time on solver size at the GGV floor (SS5.4).
              The NONEMPTY half is unaffected in principle but has no bounded search.
NOT CLAIMED   Nothing about the realizability of (9,6,2).  No gate closed, no row
              killed, no exit price asserted.
```

**OPENs raised.**

* `OPEN[CARD-C-SOURCE-NORMAL-FORM]` (SS3.3) — bound `d_src-min` in terms of `N`
  and `A_F`. This is the *only* thing that revives Card C, and it is the
  source-side twin of the promoted target-side `d_min` discipline. Highest-value
  successor here.
* `OPEN[GGV-SCOPE-ALL-PAIRS]` (SS4.3) — does GGV's bound hold for every Keller
  pair or only a minimal one? Cheap (one primary-source read), and every campaign
  consumer of the bound inherits the answer.
* `OPEN[CARD-C-D1-MODULI]` — the charge fixes *the* realized `(9,6,2)` curve, and
  nothing consumed says such curves form a single `Aut(C^2)`-orbit. Even a
  hypothetical `EMPTY` would be about this curve, not about the numerical type.

**Deviations from the charge, logged.**

1. "Derive `deg f`, `deg g`": they are not derivable. I derived instead the exact
   obstruction (PROPOSITION CARD-C-0), the floor, and the pinned contact data, and
   reported the failure in the card's own typed language rather than substituting a
   bounded search — the charged behaviour for the unbounded branch.
2. "The two germ conditions": only one is writable (SS3.3, SS5.2), and dropping
   the second is proved safe.
3. `[X]` against IDE SS6's headline "`EMPTY` kills `(9,6,2)` at the strongest
   possible level", as a description of any *bounded-degree* run. IDE SS6's
   `NONEMPTY` half is not withdrawn.
4. `(GGV-ORBIT)` is derived but deliberately **not promoted**: it would make an
   implausibly strong claim depend on an unverified scope reading. Parked behind
   `OPEN[GGV-SCOPE-ALL-PAIRS]`.
5. **Size.** Body is about 28 KB against a 15-25 KB target. The overrun is in SS2
   (the intersection-theoretic derivation had to be done, not asserted) and SS5.3
   (the generator block a successor transcribes verbatim). Logged, not hidden.

## 7. FALLACY-v2 audit

* **Flag/place/series.** SS4.1 keeps three series apart: `eta_1`'s parametrisation
  degrees `(9,6)`, the curve degree `deg D_1 = 9`, the map degrees `(deg f,deg g)`;
  `gcd(9,6)` is never fed to GGV. In SS2, `c_l` (contact with the *target* line at
  infinity) is never merged with `nu_l` (multiplicity in the *source* `pi^*L_inf`).
* **Floor/attainment.** `(FLOOR) d >= 13` is a floor throughout, explicitly not
  claimed attained; SS4.2 shows the operative floor is 16. `(CONTACT)`'s 11
  profiles are necessary conditions, not realisations.
* **Carrier/attainment.** Lemma SPEC is a proved *sufficient* condition for a
  counterexample (the `NONEMPTY` branch); no `EMPTY` result is claimed or
  simulated, and SS5.5(4) types what `EMPTY` would and would not mean.
* **`sat()` / raw remainder.** No Groebner, saturation or normal form was run.
  SS5.5 carries the ring assertion and both controls forward to any successor run.
* **Variable/ring map.** SS5.1 declares the substitution, the coefficient field
  `QQ`, and the primitivity that makes `tau` a uniformiser, and flags that all
  order bookkeeping is off by a constant factor without it.
* **Pole/interior.** GGV is consumed only through `>= 16`, monotone under either
  reading of its scope; `!= 2p` appears only inside an explicitly conditional
  derivation whose purpose is to test that scope.
* **Label hygiene.** Three letter collisions were found and repaired rather than
  tolerated: CAGE cl.1's `(d,e)` -> `(d_0,e_0)` (SS2.1), the target curve equation
  `H` -> `Psi` (SS5.3), both against SS2's `d = max(deg f,deg g)` and `H = pi^*(line)`.
* **Prime label/derivative.** `q'`, `p'` in SS5.3 are genuine `d/dT` derivatives,
  written out; the expansion coefficients carry subscripts (`f_1`, `g_1`), not
  primes, for exactly this reason.
* **Exit claim.** None; no `charge_basis` line, because no exit price is asserted.

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
