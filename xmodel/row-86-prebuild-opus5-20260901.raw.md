# ROW-86-PREBUILD: the S_4 kill chains for the two live (8,6) types

Lane: `ROW-86-PREBUILD`. Date: 2026-09-01. Agent: Opus 5.
Desk-scale exact reasoning; no CAS. Runs in parallel with the
`(8,6)`/`(9,6)` nodal-realization computation; its conclusions are
independent of that computation's outcome.

## 0. Scope, custody, method

Charged frozen copies were hashed with `shasum -a 256` before they were read. All
three match the charge exactly:

```text
3985fbedea72315c0ff3ffd4185de465ba16922bca872623fe2f02fe34cffc08  nodal-realization-86-96-grok46-20260831.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
abba04527ce7d0847bee3df9319e4e92d974218996e42745fee2c83590ed8e1a  shape-3-finish-hostile-review-grok46-20260901.md
```

Below: **NR** = the realization report, **Coord** = the coordinator integration,
**S3FR** = the SHAPE-3-FINISH hostile review. Campaign documents read on disk but
not re-hashed as primary: `shape-kill-uniform-opus5-20260901.md` (Theorem A', SK-2,
SK-4, SK-5, the `g=2` constant-stratum kill), `pi1s4-close-residual-r2-opus5-20260831.md`
(tubular factorisation (3.1)–(3.2), Lemma 3.3, Theorem A'), `nori-bc-extension-opus5-20260831.md`
((M-INF-T), Corollary N-A-RES), `pi1s4-64-torus-check-opus5-20260831.md` (Theorem
INF-TRIVIAL), `pi1-s4-decision-opus5-20260831.md` (Theorem A). No canonical ledger
or charged file was edited; `jc2-lean` was not inspected.

**Method disclosure.** No computer algebra was run: no Groebner basis, no
resultant, no ideal saturation. Two integer/finite-group scripts were used as
*confirmation only*, both re-doing computations already done by hand in this
report: (i) listing gaps of the numerical semigroups `<8,6,c>` and evaluating
`e(iota)` and one congruence; (ii) enumerating the 24 elements of `S_4`, the
solutions of the word equation `ABCA = Pi` in `A_4`, and the Hurwitz orbit of a
`2`-tuple under `B_2`. Every number and every permutation identity below is
hand-checkable in a few lines and was hand-checked; §5 records the hand routes.

**What this lane delivers.** A kill chain per type, assembled from promoted
machinery, plus one new theorem (§4) that is `PROVED-HERE` and `UNREVIEWED`. The
verdicts concern the *`S_4` representation*, not realizability: killing a type
here removes it from the `PI1-S4` residual, and does **not** assert that no
polynomial curve with that `delta`-sequence exists. NON-REALIZABLE from the
parallel lane would make this moot but cheap; REALIZED makes §4 the immediate
promotion.

## 1. The two types: data re-derived

`(d,n) = (8,6)`, `a = d-n = 2`, `g = gcd(d,n) = 2`, `p_a = (d-1)(d-2)/2 = 21`.
Galindo conversion `beta_1 = d^2/gcd(d,n) - c = 32 - c` (NR §1.1); one-pair germ
`(a;beta_1) = (2;beta_1)` with `gcd(2,beta_1) = 1`, so `2 delta_inf = beta_1 - 1`,
`M_emb = a + beta_1 - 1 = beta_1 + 1 = M_inf`, and `delta_aff = 21 - delta_inf`.
Gaps re-listed independently of NR:

| type | `Delta` | `S_aff` gaps | `delta_aff` | `beta_1` | `delta_inf` | germ at `P_inf` | `M_inf` |
|---|---|---|---:|---:|---:|---|---:|
| **A** | `(8,6,11)` | `1,2,3,4,5,7,9,10,13,15,21` | 11 | 21 | 10 | `A_20` | 22 |
| **B** | `(8,6,9)` | `1,2,3,4,5,7,10,11,13,19` | 10 | 23 | 11 | `A_22` | 24 |

Both semigroups are symmetric (Frobenius `21 = 2*11 - 1`, resp. `19 = 2*10 - 1`),
as they must be for a curve with one place at infinity; `delta_aff + delta_inf = 21`
on both rows. This reproduces NR §1.1 by an independent listing.

**Nodal count, re-derived.** The residual class (NR §0, promoted) forces every
affine singular point to be a double point of two smooth branches, i.e. an
`A_{2k_p - 1}` with `delta_p = k_p`, and `delta_aff = sum_p k_p`. Nodality is the
extra condition `k_p = 1` for all `p`, giving **11 nodes** (type A) and **10 nodes**
(type B). The "three-nodes-only" figure the charge flags is the `delta_aff = 3` of
the promoted `(6,4)` row `Delta = (6,4,3)`; it is that row's number, not a class
constraint, and it does not transfer. Non-nodal configurations with the same
`delta_aff` are *not* excluded a priori at this stage — and, importantly, every
gate below except (M-INF-T) depends only on the total `delta_aff`, not on its
partition. `P_inf = [1:0:0]` is the unique point of `Dbar` on `L_infty`, with
`(Dbar . L_infty)_{P_inf} = d = 8`, `L_infty` the tangent; the germ is
analytically `A_{beta_1 - 1}` (contact `8` with `L_infty` and contact `beta_1` with
its own analytic maximal-contact line are different data and are not identified).

Plücker class `m = d(d-1) - sum_p (mu_p + m_p - 1) = 56 - 43 = 13` on both rows
(NR §2, §3): positive, hence a consistency check, not an obstruction. No Hessian /
inflection kill is claimed, since no sourced Hessian multiplicity for `A_{2n}` was
consumed. Orevkov and Matsuoka–Sakai are cuspidal-only and do not apply (NR §8).

## 2. Gates first: (M-INF), (M-INF-T), and the N-A boundary

**(M-INF)** (promoted): `M_inf <= 3d - 3` implies `pi_1(C^2 - D) = Z`, which kills
every `S_4` quotient. Here `3d - 3 = 21`.

```text
type A:  M_inf = 22 = 3d-2 ,  misses by 1
type B:  M_inf = 24 = 3d   ,  misses by 3
```

**(M-INF-T)** (promoted, Corollary N-A-RES): `M_inf + 2T <= 3d - 3` with
`T = sum over tangential double points of k_p`, and `T = 0` exactly on the nodal
locus. Since `T >= 0`, the gate is *monotone in the wrong direction*: type A would
need `2T <= -1` and type B `2T <= -3`. Both are impossible at every `T`. Recorded
precisely:

```text
(M-INF-T) slack  =  3d - 3 - M_inf - 2T  =  -1 - 2T  (type A) ,  -3 - 2T  (type B).
```

So the **N-A / Nori route fails for both types, at every affine singularity
configuration**, nodal or not. This is a failure of a *sufficient* criterion; it
carries no information about `pi_1` beyond "the criterion is silent". The `(6,3)`
tangency table of the Nori lane (where `(M-INF-T)` closes all but two
configurations) has no analogue here: there the gate had slack to spend, here it
has none.

**The N-A boundary, exactly.** With `r_1 = delta_aff`, `T = T_x = 0`, the charged
N-A inequality is `C'^2 > 2 r_1`, and the promoted Lemma 4.3 gives
`C'^2 - 2 delta_aff = 3d - 2 - M_inf`. Hence

```text
type A:  C'^2 - 2 r_1 = 0     (the inequality reads  2*11 > 2*11 , false by one unit)
type B:  C'^2 - 2 r_1 = -2    (reads 18 > 20 , false by two units)
```

Type A therefore sits **exactly on the boundary** of N-A, in the same position as
the promoted `(6,4)` and `(8,4)` rows: a YES on `OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]`
(may `C^2 > 2 r_1` be relaxed to `>=` for *irreducible* `C` with `T = T_x = 0`?)
would kill type A outright. The promoted sharpness datum is about the `T_x`
coefficient (two bitangent conics, `4 > 4`, reducible), so it does **not** settle
the irreducible `r_1` question either way. I record the coincidence and do **not**
relax the inequality: that would be a floor/attainment substitution. Type B is not
on the boundary and is untouched by any such relaxation.

## 3. The cable structure: outer (4,3) coprime, g = 2

`(8,6) = (4*2, 3*2)`: **`(8,6)` is the `g = 2` member of family 3**, reduced shape
`(d',n') = (4,3)`, coprime, `d' > n'`, `g = gcd(d,n) = 2`. So the promoted family-3
machinery applies verbatim, with `g = 2`.

**Tube structure (promoted, (3.1)–(3.2)).** Over `|x| = R` the `d = 8` roots
`y_j(x) = sum_{k<=6} c_k zeta_8^{jk} x^{k/8}` fall into `d' = 4` blocks
`B_i = {j : j = i mod 4}` of size `g = 2` (leading terms `zeta_8^{6j} x^{3/4}` take
exactly 4 values). The braid at infinity is tubular:

```text
(3.1)   rho_inf = C_2(delta_4^3) . iota ,   iota in B_{2,1} x B_{2,2} x B_{2,3} x B_{2,4} ,
(1.1)   e(iota) = (d-1) + 2 delta_aff - n(d-g) = 7 + 2 delta_aff - 36 = 2 delta_aff - 29 .
```

`C_2` is blackboard cabling, `e(C_2(delta_4^3)) = g^2 n'(d'-1) = 36`, and
`e(rho_inf) = 2 delta_aff + d - 1 = (d-1)^2 - 2 delta_inf`.

**Outer datum (promoted A'(1)–(3), SK-5).** `BP(T) = (Pi_1,...,Pi_4)` is
`delta_4^3`-fixed, hence `3`-periodic: `Pi_4 = Pi_1 =: A`, `Pi_2 =: B`, `Pi_3 =: C`,
with `conj_Pi` cycling `A -> C -> B -> A` and `Pi = ABCA`. Each `Pi_i` is a product
of `g = 2` transpositions, hence lies in `A_4`; `sgn(Pi) = (-1)^d = +1`.

**Order/parity fork at outer `(4,3)`, as the charge asks.** Theorem A(3) reads:
either (`ord(Pi) = 3`, `3 | n`, `d` even) or (`ord(Pi) = 4`, `4 | n`, `d` odd). Read
on the *outer* datum `(d',n') = (4,3)`: the second horn needs `4 | n' = 3`, false,
and `d' = 4` is even; so the fork is entered on the first horn only, `ord(Pi) = 3`,
`3 | 3`, `4` even — all three conditions are identities of the shape and carry no
new information. This is the "Route 2 is vacuous" verdict of S3FR §6, and I confirm
it: the block-collapsed A'(3) gives only `Pi^{n'} = Pi^3 in Z(H)`, which is empty
once `ord(Pi) = 3`. The order is supplied instead by **SK-5** (promoted, review
CONFIRMED): in the non-constant stratum `A,B,C` are pairwise distinct, `conj_Pi`
permutes them in a `3`-cycle, `S_4` is centreless, so `3 | ord(Pi) <= 4` and
`ord(Pi) = 3`.

**The `g = 2` split (promoted, SHAPE-KILL §4.3).**

* *Constant stratum* `A = B = C = c`: dead. `c = 1` gives `im(phi) = Z/2` (SK-2,
  using `gcd(d',n') = 1`); `c` a `3`-cycle confines all eight meridians to `supp(c)`,
  so `im(phi) <= S_3`; `c` a double transposition pins each block to its two disjoint
  factors, so `im(phi) <= V_4`. None surjects.
* *Non-constant stratum*: taking `Pi = (123)`, the word equation `A phi^2(A) phi(A) A = Pi`
  over `A_4` has exactly one non-constant solution orbit,
  `{A,B,C} = {(134),(243),(142)}` — the three `3`-cycles whose supports contain the
  fixed letter of `Pi`. I re-ran this enumeration independently and reproduce
  SHAPE-KILL exactly: with `A = (134)`, `C = conj_Pi(A) = (142)`, `B = (243)`, and
  `ABCA = (123) = Pi`.

Consequence used throughout §4: **every block product is a `3`-cycle**, so each block
subtuple `T_i = (u_i, v_i)` is a factorisation of a `3`-cycle into two transpositions
sharing exactly one letter. For `A = (abc)` there are exactly three such:
`(u,v) in {((ac),(ab)), ((ab),(bc)), ((bc),(ca))}`.

Everything in this section is degree-blind in `beta_1` and in `delta_aff`: it is
identical for type A and type B. The separation is in §4.

## 4. THEOREM TUBE-2: the inner-braid gate at g = 2

SHAPE-KILL §3.3 names the exact missing ingredient for every `g`-cabled row: *"the
missing ingredient is the inner braid `iota`, numerically pinned by (1.1) to
`e(iota) = (d-1) + 2 delta_aff - n(d-g)` but not otherwise constrained without a
`delta_aff` census."* At `g = 2` the tube braid group is `B_2 = <sigma> = Z`, which
is **abelian**, so the exponent sum is a *complete* invariant of each tube factor,
and (1.1) is not a partial pin but the whole of `iota` up to the distribution among
tubes — which, as the proof shows, drops out. This lane has the `delta_aff` census
(§1). So the ingredient is available here and nowhere else in the campaign.

> **THEOREM TUBE-2 (PROVED-HERE, UNREVIEWED).** *Let `D` be a residual branch curve
> of type `(d,n)` with `g = gcd(d,n) = 2`, `d' = d/2`, `n' = n/2`, `gcd(d',n') = 1`,
> `d' > n'`, and suppose `phi : pi_1(C^2 - D) ->> S_4` sends every meridian to a
> transposition and has non-constant block products. Put `E := e(iota)` as in (1.1)
> and `h := Pi^{d'-1} Pi_{d'}^{-(d'-1)}`. Then the block subtuple `T_1 = (u,v)` of the
> `rho_inf`-fixed tuple satisfies*
>
> ```text
> (4.1)     T_1  =  c_h ( sigma^E . T_1 ) ,        c_h(x) := h x h^{-1} entrywise.
> ```
>
> *In family 3 (`(d',n') = (4,3)`) one has `h = 1` and hence `T_1 = sigma^E . T_1`;
> the stabiliser of a non-constant `T_1` in `B_2 = Z` is exactly `3Z`, so*
>
> ```text
> (4.2)     3 | e(iota)   is NECESSARY  for  phi  to exist on a family-3, g=2 row.
> ```

*Proof.* Write `T = (T_1,...,T_{d'})` in blocks, `S := iota . T`. Since the left
Hurwitz action satisfies `(beta gamma) . T = beta . (gamma . T)`, `rho_inf . T = T`
reads `C_2(delta_{d'}^{n'}) . S = T`. The block-level action of `delta_{d'}` is
`(u_1,...,u_{d'}) -> (Pi u_{d'} Pi^{-1}, u_1, ..., u_{d'-1})` (promoted, §3.3 of the
decision report), and its blackboard cable acts on block tuples by
`(B_1,...,B_{d'}) -> (P B_{d'} P^{-1}, B_1,...,B_{d'-1})` with `P = Pi_1 ... Pi_{d'-1}
= Pi Pi_{d'}^{-1}` (entrywise conjugation; the promoted Lemma 3.3 computation
`C_g(sigma_i).(A,B) = (Pi_A B Pi_A^{-1}, A)` composed along `delta_{d'} = sigma_1...sigma_{d'-1}`).
Note the conjugator is `Pi Pi_{d'}^{-1}` and **not** `Pi`: for a single entry the two
agree, for a block they do not. Internal check on the assignment: applying block
products to the four relations gives `Pi(T_1) = Pi B Pi^{-1} = A`,
`Pi(T_2) = Pi C Pi^{-1} = B`, `Pi(T_3) = Pi A Pi^{-1} = C`, `Pi(T_4) = A` — all four
match `(Pi_1,...,Pi_4) = (A,B,C,A)`, which a mis-assigned conjugator would break.

At `(d',n') = (4,3)`, three applications give
`C_2(delta_4^3) . S = (c_{Pi B^{-1}}(S_2), c_{Pi C^{-1}}(S_3), c_{Pi A^{-1}}(S_4), S_1) = T`.
Since `iota` acts blockwise and preserves block products, `S_i = sigma^{a_i} . T_i`
with `sum a_i = E`. Conjugation commutes with the Hurwitz action (the action is by
words in the entries), and `B_2` is abelian, so composing the four relations around
the cycle `T_1 <- T_2 <- T_3 <- T_4 <- T_1` gives
`T_1 = c_h(sigma^{a_1+a_2+a_3+a_4} . T_1)` with
`h = (Pi B^{-1})(Pi C^{-1})(Pi A^{-1})`. Using `Pi^{-1} B Pi = C`, `Pi^{-1} C Pi = A`
(i.e. (4.1) of SHAPE-KILL) this collapses to `h = Pi^3 A^{-3}`, and `ord(Pi) = 3`
(SK-5) with `ord(A) = 3` give `h = 1`. **Only the sum `E` survives; the distribution
of `iota` among the four tubes is irrelevant.**

Finally, the `B_2`-orbit. With `A = uv = (abc)`, `sigma . (u,v) = (uvu^{-1}, u)` sends
`((ac),(ab)) -> ((bc),(ca)) -> ((ab),(bc)) -> ((ac),(ab))`: `sigma` permutes the three
factorisations in a `3`-cycle. Hence the stabiliser of any one of them is `3Z`, and
`sigma^E . T_1 = T_1` iff `3 | E`. (Equivalently: `sigma^2 = c_A`, so `sigma^6` acts
trivially, `sigma^{2k}` fixes iff `3 | k` — `Z(S_3) = 1` — and `sigma^{2k+1}` fixes iff
`k = 1 mod 3`; the two branches merge to `3 | E`.) `[]`

**Application to the (8,6) row.** `E = e(iota) = 2 delta_aff - 29`, and equivalently
(§5) `E = 14 - beta_1 = c - 18`. So the gate `3 | E` reads, in three interchangeable
forms,

```text
(4.3)     3 | c    <=>    beta_1 = 2 (mod 3)    <=>    delta_aff = 1 (mod 3).
```

| type | `Delta` | `delta_aff` | `E = e(iota)` | `3` divides `E` ? | verdict at this gate |
|---|---|---:|---:|:--:|---|
| **A** | `(8,6,11)` | 11 | `-7` | **no** | **KILLED** |
| **B** | `(8,6,9)` | 10 | `-9` | yes | passes |
| (8,6,7) | `(8,6,7)` | 9 | `-11` | no | KILLED (bonus) |
| (8,6,3) | `(8,6,3)` | 7 | `-15` | yes | passes (bonus) |

**Type A kill chain, complete.** (i) The constant stratum is dead (SK-2 / SHAPE-KILL
§4.3, promoted). (ii) In the non-constant stratum `Pi` and all `Pi_i` are `3`-cycles
(SK-5 + the `A_4` word equation, promoted). (iii) `rho_inf . T = T` forces
`T_1 = sigma^{E} . T_1` (Theorem TUBE-2). (iv) `E = -7`, `3 nmid 7`, and the
stabiliser is `3Z`. Contradiction. Hence **no `rho_inf`-fixed tuple with image `S_4`
exists for `Delta = (8,6,11)`, and the row is dead** — the same inference shape as the
promoted THEOREM SK-4. The kill is independent of the partition of `delta_aff = 11`
into `k_p`'s, hence independent of nodality, and independent of the realization
question.

## 5. Verification of e(iota): two routes and three controls

Theorem TUBE-2 is worthless if `E` is wrong, so `E` is computed twice, by routes
that share no step, and the gate is run on three controls.

**Route 1 (discriminant bookkeeping).** `e(rho_inf) = deg_x disc_y F = sum_p (mu_p + m_p - 1)`
over affine points. For a singular point `mu_p + m_p - 1 = 2 delta_p + (m_p - r_p)`, and
`sum_p (m_p - r_p)` plus the smooth vertical tangencies is the total affine
ramification `d - 1` of `p : P^1 -> P^1` (which has a single pole of order `d`). Hence
`e(rho_inf) = 2 delta_aff + d - 1` **unconditionally** — for any affine singularity
types, tangent fibres included. Subtracting `e(C_2(delta_4^3)) = g^2 n'(d'-1) = 36`
gives (1.1). Type A: `29 - 36 = -7`. Type B: `27 - 36 = -9`.

**Route 2 (Puiseux winding at infinity).** In the chart `(v,u) = (y/x, 1/x)` at
`P_inf` the place is `v = s^2`, `u = sum_{k>=8} c_k s^k` with first odd exponent
`beta_1`. Then `x = u^{-1}`, `y = v/u = s^{-6} U^{-1}` with `U = sum c_k s^{k-8}`
whose first odd `s`-power is `s^{beta_1-8}`; inversion does not move it. So the
first odd `s`-power of `y` is `s^{beta_1-14}`, i.e. in `y = sum_k c'_k x^{k/8}` the
leading **odd** `k` is `k_odd = 14 - beta_1`. Within a tube the two strands differ by
`y_j - y_{j+4} = sum_{k odd} 2 c'_k zeta_8^{jk} x^{k/8}`, dominated by `x^{k_odd/8}`.
The tube permutation of `C_2(delta_4^3)` is a `4`-cycle, so a tube returns to itself
after `4` loops of `x`, during which the difference vector turns by
`4 k_odd/8 = k_odd/2` full turns, i.e. `k_odd` half-twists; blackboard cabling adds
none. Hence `E = k_odd = 14 - beta_1`.

The two routes agree identically: `2 delta_aff - 29 = 2(21 - (beta_1-1)/2) - 29 = 14 - beta_1`,
and with `beta_1 = 32 - c` also `E = c - 18`. Type A `-7`, type B `-9`.

**Control 1 (toy row, both routes).** `p = t^8 ... ` is not needed; take the smallest
`g = 2` instance `p = t^4 + t`, `q = t^2`, `(d,n) = (4,2)`, `d' = 2`, `n' = 1`. Here
`S_aff = <1>` (because `p - q^2 = t`), `delta_aff = 0`, `delta_inf = 3`. Route 1:
`e(rho_inf) = 0 + 3 = 3`, `e(C_2(delta_2)) = 4`, so `E = -1`. Direct check of
`e(rho_inf)`: the vertical tangencies solve `-4y(x-y^2) = 1` with `(x-y^2)^2 = y`,
i.e. `y^3 = 1/16` — three simple tangencies, `e = 3`. Route 2: `y = x^{1/2} - (1/2)x^{-1/4} + ...`,
so `k_odd = -1` and `E = 2 * (-1)/4 * 2 = -1`. Both routes give `-1`.

**Control 2 (the promoted `(6,4)` row — positive control for the gate).**
`Delta = (6,4,3)`, `delta_aff = 3`, `d' = 3`, `n' = 2`, `E = 5 + 6 - 16 = -5`. Here
family 2 at `g = 2`: block products are `2`-periodic (`Pi_3 = Pi_1 = X`), the
surviving configurations have `X, Y` distinct `3`-cycles and `Pi = WX in V_4`
(promoted SK-4 (3.3)). Theorem TUBE-2 gives `h = Pi^2 X^{-2} = X` (since `Pi^2 = 1`),
and `c_X = sigma^2` on the block, so the gate is `3 | E + 2`. And `E + 2 = -3`.
**The promoted, realizable `(6,4)` row passes the gate, and passes it non-trivially**
(`E = -5` is itself not divisible by `3`; it is the shift by `+2` that lands it). Had
`delta_aff` been `4` instead of `3`, the same row would have been killed. This is the
strongest available check that TUBE-2 is not vacuously true and not uniformly false.

**Control 3 (parity / one-place-at-infinity).** `D` has one place at infinity, so the
link at infinity is a knot and the permutation of `rho_inf` is a `d`-cycle. The
permutation of `C_2(delta_4^3)` is two disjoint `4`-cycles; `iota` swaps inside tube
`i` iff `a_i` is odd; the composite is an `8`-cycle iff `#{i : a_i odd}` is odd, i.e.
iff `E` is odd. `E = 2 delta_aff - 29` is odd on every `(8,6)` row. Consistent, and it
is an independent confirmation of the parity of (1.1).

**Group-theoretic control.** The `A_4` word equation `ABCA = Pi` and the `B_2` orbit
were both re-enumerated: solutions `{(134),(243),(142)}` plus the constant `A = Pi`,
reproducing SHAPE-KILL §4.3 line for line; `h = e`; stabiliser `sigma^3`; `sigma^{-7}`
fixes none of the three factorisations, `sigma^{-9}` fixes all three.

**Where TUBE-2 stops.** At `g >= 3` the tube group `B_g` is non-abelian, the exponent
sum is not a complete invariant, and (1.1) pins only `e(iota)`; the argument does not
run. This is exactly why `A'(5)` was held as a GAP and why `OPEN[SHAPE-2-INNER-g>=3]`
is open. TUBE-2 does not close either; it closes the `g = 2` case only.

## 6. THEOREM TB and TB-2 against these delta-sequences

The promoted family-3 results (S3FR §10) are: the mixed cover `Z -> P^2` with
`S_pi = Dbar`, `T_pi = L_infty`, weighted branch `deg Delta-bar = 4g + 2 = 10`;
`k = -deg det T = 2g + 1 = 5`; THEOREM TB `k_0 + m = 0 (mod 3)` giving
`m = g + 2 = 1 (mod 3)` with `0 <= m <= 2g = 4`; and Proposition TB-2, `m = 4` exactly
at `g = 2`, with `ord_y rho = 4`, `gamma = 0`.

**These apply to both types, identically, and separate neither.** Every input to TB
and TB-2 is a function of `(d,n) = (8,6)` and of the infinity chart orders
`(ord v, ord u) = (g, 4g) = (2,8)`: the weighted branch degree, `k = 2g+1`, the
Puiseux count `ord_sigma f(0,sigma) = g`, `ord_y f(y,0) = 4g`,
`ord_y (df/dsigma)|_{sigma=0} = 4(g-1)`, and readings (a)–(c) of the discriminant
expansion. **None of them sees `beta_1`, `delta_aff` or `c`.** In particular:

* `m = 4` is forced for type A and for type B alike, and for `(8,6,7)` and `(8,6,3)`.
* `m = 4 != 0`, so the conditional `m = 0 => g = 1 (mod 3)` kill does **not** fire on
  `(8,6)`; S3FR §6 says this in terms and I confirm it.
* `0 <= m <= 2g = 4` is a floor-and-ceiling, and `m = 4` saturates the ceiling; with
  reading (a) `2m + 2 gamma = 4g` this pins `gamma = 0`. No further constraint follows
  from the leading `sigma`-jets: S3FR §4(H) records that the leading jets are exhausted
  at `g = 2` once `m = 4` is established.

**So the charge's question is answered NO.** Combining TB-2's `m = 4` with the
singularity budgets `delta_aff = 11` resp. `10` yields **no contradiction and no
pinned residual**, because the budgets never enter TB. The two types are
TB-indistinguishable. The separation is achieved instead by the inner braid (§4),
which is the exact complement: TUBE-2 is `beta_1`-sensitive and `m`-blind, TB is
`m`-sensitive and `beta_1`-blind.

**What TB does buy for the surviving type.** The named successor
`OPEN[S3-TB-G2]` ("kill `m = 4` at `g = 2`") acquires a sharper input from this lane:
after §4 only `beta_1 in {23, 29}` remains on the `(8,6)` row (`beta_1 = 21, 25` are
dead), so a TB-G2 attack no longer has to cover `beta_1 = 21`. The place where
`beta_1` first enters the local analysis at `P_inf` is explicit: the two Puiseux
branches `sigma_+(y), sigma_-(y)` of `Dbar` at `P_inf` agree to order `y^{beta_1/2 - 1/2}`
and first differ at `y^{beta_1/2}` — i.e. at `y^{23/2}` for type B. Any deeper layer of
TB must reach that order to see the difference between the surviving rows; the
leading-jet layer provably cannot.

## 7. The INF-TRIVIAL analogue at A_20 and A_22

Theorem INF-TRIVIAL (promoted, `(6,4)` lane): *if `chi : G -> H` sends every meridian
of `D` to an involution, then `chi(gamma_inf) = 1`.* Its proof is one line —
`gamma_inf = g_5^2 g_3^2 g_1^2` — and the whole content is the **even word**: at
`(6,4)` the row normal form gives `x = r(t)^2` with `deg r = 3`, so the fibre `x = 0`
is a *tritangent* line, the six points of the nearby fibre collide in three adjacent
pairs, Zariski–van Kampen identifies `g_1 = g_2`, `g_3 = g_4`, `g_5 = g_6`, and the
product of a geometric basis becomes a product of squares. (The product of a geometric
basis of a punctured disc is the boundary class, independent of the basis, so it may be
read off in any degeneration.)

**At `(8,6)` the analogue is not merely unavailable — it is refuted, conditionally on
`phi`.** If `phi` exists then `phi(gamma_inf) = Pi` is a `3`-cycle (SK-5), and a
`3`-cycle is not a product of squares of involutions. So:

> **COROLLARY (PROVED-HERE).** *On a family-3 `g = 2` row admitting `phi`, no
> INF-TRIVIAL-type even-word mechanism can exist. Equivalently: every even-word
> mechanism, if exhibited, is a `kill` of the row rather than an obstruction to be
> circumvented.*

Concretely, each of the following is now a **kill criterion** for either type, and
each was checked and found *not* to be forced:

1. *Totally tangent line.* `alpha p + beta q + gamma - c = alpha w^2` with `deg w = 4`
   in some admissible pencil (`alpha != 0`, base point `[beta:-alpha:0] != P_inf`).
   The FOLD mechanism that forces this at `(6,4)` runs off `3 in S_aff` together with
   `delta_0 = 6 = 2*3`: an element `r` of `C[p,q]` of degree `3` exists, `p - lambda r^2`
   has degree in `S_aff cap [0,5] = {0,3,4}`, and a triangular target automorphism plus
   completing the square gives `p = r^2`. The analogue needs `4 in S_aff` with
   `delta_0 = 8 = 2*4`. **`4` is a gap of `<8,6,11>` and of `<8,6,9>`** (§1), so no
   element of `C[p,q]` has degree `4` and the FOLD mechanism does not run on either
   type. A square `p - c = w^2` with `w` outside `C[p,q]` is not excluded by this, but
   it is `4` conditions on the `2`-parameter pencil `p + lambda q + mu`, expected
   codimension `2`, and it is not forced by any promoted datum.
2. *Four collinear affine nodes.* At an affine double point the two branch meridians
   go to **disjoint** transpositions (promoted), so a line meeting `Dbar` in four such
   points has `phi(gamma_inf) in V_4`, again contradicting SK-5. Four of the `11`
   (resp. `10`) nodes being collinear is `2` conditions on a `2`-dimensional family of
   lines; not forced.
3. *A quadruple point of the dual curve.* `Dbar^*` has degree `m = 13` and
   `delta(Dbar^*) = 66`; an ordinary `4`-fold point costs `delta = 6`. Numerically
   possible up to eleven times, hence not obstructed and equally not forced.

**The germs themselves.** The infinity germs are `A_20` (type A) and `A_22` (type B):
unibranch, multiplicity `2`, `mu = 2 delta_inf = 20` resp. `22`, tangent to `L_infty`
with contact `8`. The even-word content of a multiplicity-`2` place is precisely the
tube: the two strands of each tube are the two sheets of the double cover
`v = s^2`, and the *odd* part of the Puiseux expansion — the part that distinguishes
`A_20` from `A_22` — is exactly the inner braid exponent `E = 14 - beta_1` of §5. So the
"even-word mechanism at the infinity germ" is not a separate tool: it *is* Theorem
TUBE-2, read at the germ. `A_20` gives `E = -7` and no fixed tuple; `A_22` gives
`E = -9` and three fixed tuples per block. That is the whole of the INF-TRIVIAL
analogue at this row, and it is where the two types part.

## 8. Verdicts, residual, successors

### Type A — `Delta = (8,6,11)`, `(beta_1; delta_inf, delta_aff; M_inf) = (21;10,11;22)`

**KILLED**, at the `S_4`-representation level. Chain, each link with its status:

```text
(1) residual class: all affine sings are double points of two smooth branches   PROMOTED
(2) (8,6) = (4*2,3*2) is family 3 at g=2; tubular rho_inf = C_2(delta_4^3).iota  PROMOTED (3.1)
(3) e(iota) = 2*delta_aff - 29 = -7                                             PROMOTED (1.1) + §1 census
(4) constant stratum has im(phi) != S_4                                         PROMOTED (SK-2, SHAPE-KILL 4.3)
(5) non-constant stratum: Pi and every Pi_i is a 3-cycle                        PROMOTED (SK-5 + A_4 word eq.)
(6) rho_inf-fixedness collapses to T_1 = sigma^{e(iota)} . T_1 (h = 1)          PROVED-HERE (Thm TUBE-2)
(7) stabiliser of a non-constant block subtuple in B_2 = Z is 3Z                PROVED-HERE
(8) 3 does not divide 7  =>  no rho_inf-fixed tuple with image S_4  =>  row dead
```

Scope, stated exactly: this kills the *type as a `PI1-S4` residual candidate*. It does
**not** claim `Delta = (8,6,11)` is non-realizable as a polynomial curve, and it does
not depend on nodality, on the partition of `delta_aff = 11`, or on the outcome of the
realization lane. If that lane returns REALIZED for type A, the curve exists and
carries no meridional-transposition surjection onto `S_4`. Corroboration, not used as
a second proof: type A is the unique `(8,6)` type sitting exactly on the N-A boundary
`C'^2 = 2 r_1` (§2), so a YES on `OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]` would kill it a
second way.

### Type B — `Delta = (8,6,9)`, `(beta_1; delta_inf, delta_aff; M_inf) = (23;11,10;24)`

**OPEN at named tools**, with the residual pinned exactly. It survives every gate in
this lane, and the survival is not accidental: `E = -9` sits on the allowed residue
class `3 | E`.

Pinned residual (the complete outer + inner datum, up to `S_4`-conjugacy and cyclic
relabelling of blocks):

```text
Pi = (123) ;  {Pi_1,Pi_2,Pi_3,Pi_4} = {A,B,C,A} with (A,B,C) = ((134),(243),(142)) ;
T_1 = (u,v) any of the three factorisations of A into two transpositions ;
(a_1,a_2,a_3,a_4) in Z^4  with  sum a_i = -9  and  #{i : a_i odd}  odd ;
T_4 = sigma^{a_1}.T_1 ,  T_3 = c_{Pi A^{-1}}(sigma^{a_1+a_4}.T_1) ,
T_2 = c_{Pi C^{-1}} c_{Pi A^{-1}}(sigma^{a_1+a_3+a_4}.T_1) ;  closure automatic since 3 | 9 .
```

The three supports `{1,3,4},{2,3,4},{1,2,4}` exhaust all six transpositions, so
`im(phi) = S_4` is achievable: the datum is non-empty and the row is genuinely open at
this level.

Named tools, in decreasing value:

1. **The realization lane** (`I_23` plus reduced `I_DP` of length `10`, NR §3). A
   NON-REALIZABLE verdict closes the type outright.
2. **`OPEN[S3-TB-G2]`** with the sharpened input of §6: only `beta_1 in {23,29}`
   survives on the row, and the branch separation sits at `y^{beta_1/2}`.
3. **Braid monodromy of an actual witness**, if REALIZED: `rho_inf`-fixedness is only
   the *product* of the local relations; each singular fibre imposes its own, and
   `V = d - 1 = 7` vertical tangencies plus `10` node squares is a `17`-factor
   factorisation to test.
4. `OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]` does **not** reach type B (deficit `2`, §2).

### Ledger increments beyond the charge

* `(8,6,7)` (`delta_aff = 9`, `E = -11`) is **KILLED** by the same chain; `(8,6,3)`
  (`delta_aff = 7`, `E = -15`) **passes**. So the `(8,6)` row of the six-type residual
  drops from four types to two, `{(8,6,9), (8,6,3)}`, with the clean criterion `3 | c`.
* **Family 2 at `g = 2`** (rows `(2u,4)`, `u = 3 (mod 6)`, the SK-4 survivors): TUBE-2
  gives `h = Pi^{u-1} Pi_1^{-(u-1)}`, `Pi^2 = 1` by SK-4 (3.3), `c_{Pi_1} = sigma^2`,
  hence the gate `E = 1 - u (mod 3)`; with `E = 2 delta_aff - 6u + 7` this is
  **`delta_aff = u (mod 3)`**, i.e. `3 | delta_aff` on every SK-4 survivor. The
  promoted `(6,4)` row (`u = 3`, `delta_aff = 3`) satisfies it. This is a uniform
  sharpening of SK-4 awaiting a `delta_aff` census per row; it is stated, not consumed.
* `(9,6)` types are **untouched**: there `g = 3`, `B_3` is non-abelian, and TUBE-2 does
  not run.

## 9. FALLACY-v2 audit

* **Flag/place/series.** Three distinct objects at `P_inf` are kept apart: the contact
  `(Dbar . L_infty)_{P_inf} = 8` with the *specific* line `L_infty`; the analytic type
  `A_{beta_1-1}` of the germ; and the characteristic numerator `beta_1`. They are
  `8`, `A_20`/`A_22`, `21`/`23` and are never identified. Likewise the reduced branch
  `Dbar + L_infty` (degree `4g+1 = 9`, odd) and the weighted `Dbar + 2 L_infty`
  (degree `4g+2 = 10`, even) are kept apart in §6, per S3FR §5.
* **Floor/attainment.** `0 <= m <= 2g` is a bound; `m = 4` is quoted as TB-2's *exact*
  value, not as the ceiling being attained by fiat. `(M-INF)`/(M-INF-T) failing is
  reported as a sufficient criterion going silent, never as `pi_1 != Z`. The N-A
  boundary coincidence at type A is recorded and **not** used: `C'^2 > 2 r_1` is not
  relaxed to `>=`, since no source licenses that for irreducible `C`.
* **Carrier/attainment.** No residual curve is asserted to exist. The pinned residual
  of type B is *group-theoretic data*, explicitly not a witness; `REPRESENTATIVE` is
  not `FULL_ACTUAL_EXIT`.
* **Per-ray/exit-set charge.** No exit price is asserted anywhere; there is no
  `charge_basis` line, as the charge requires.
* **Pole/interior.** The Puiseux winding of §5 is taken on `|x| = R` in the tube
  regime `k/d < theta < n/d` where the promoted (3.1) establishes disjointness; it is
  not a pole identity used off its vertex class.
* **Prime label/derivative.** `p'`, `q'`, `df/dsigma` are genuine derivatives of named
  polynomials/local equations. `Pi` (total product) and `Pi_i` (block products) are
  distinct symbols and are never conflated; `T_pi` (total-branch divisor) versus the
  Tschirnhausen module is inherited notation, disambiguated in §6 by context only where
  S3FR already did so.
* **Variable/ring map.** The chart change `(x,y) -> (v,u) = (y/x, 1/x)` at `P_inf` is
  declared with its orders `(2,8)`; the Hurwitz action convention is the promoted left
  action `sigma_i . (..,t_i,t_{i+1},..) = (.., t_i t_{i+1} t_i^{-1}, t_i, ..)`, and
  §4 checks that the conclusion `3 | E` is unchanged under the opposite factorisation
  convention `rho_inf = iota' . C` (the two `iota`'s have the same exponent sum).
* **`sat()` / raw remainder.** Not in play; no ideal was computed.
* **Named risk in the new theorem.** The one step where a wrong convention would
  matter is the cabled conjugator: it is `Pi Pi_{d'}^{-1}` and not `Pi`. The report
  derives it and flags it; had `Pi` been used, `h` would still have collapsed to `1`
  at `(4,3)`, so the verdict is robust to that particular error, but the general
  formula `h = Pi^{d'-1} Pi_{d'}^{-(d'-1)}` is not.
* **Not filled by cap or analogy.** `g >= 3` (both `(9,6)` types and family 3 at
  `g >= 3`), `OPEN[S3-TB-G2]`, `OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]`, and the realization
  ideals are left OPEN at named tools.

**Review routing.** Theorem TUBE-2 and the type-A kill are `PROVED-HERE, UNREVIEWED`
and are flagship-shaped: they should be paired (hostile gate + independent
verification) before promotion, per the coordinator's stop at Coord §3. The
verification arm's cheapest independent target is Control 2 of §5 — re-derive the
`(6,4)` gate `3 | E + 2` from scratch and confirm `E = -5` — since a sign or
convention error there would surface immediately.

## 10. Custody and sources

Charged inputs: hashes in §0, all matching. Campaign documents consumed on disk and
cited by file and section rather than re-hashed as primary:
`shape-kill-uniform-opus5-20260901.md` §§1, 3.2–3.3, 4.1–4.3 (Theorem A' summary,
SK-2, SK-4 and (3.3), SK-5, the `g = 2` constant-stratum kill, the `A_4` word-equation
enumeration, and the explicit statement that the inner braid is the missing
ingredient); `pi1s4-close-residual-r2-opus5-20260831.md` §§3.1–3.3 ((3.1), (3.2),
Lemma 3.3, Theorem A'(1)–(4), and A'(5) held as GAP);
`nori-bc-extension-opus5-20260831.md` §3.5 (Corollary N-A-RES, (M-INF-T), Lemma 4.3
in the form `C'^2 - 2 delta_aff = 3d - 2 - M_inf`, and the `T_x` sharpness datum);
`pi1s4-64-torus-check-opus5-20260831.md` §§5.2–5.4 (Theorem INF-TRIVIAL and the
`x = 0` tritangent mechanism); `pi1-s4-decision-opus5-20260831.md` §3.3 and Theorem A.
No external literature was fetched this lane; no new primary source is claimed. The
Galindo–Monserrat conversion and the `delta`-sequence axioms are used exactly as
hashed and quoted in NR §0.

No `charge_basis` line: this report asserts no new exit price.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `34766`.
- Body SHA-256:
  `7247cef3961576b9919a2ca6e67c484f9f84e6e0af5bca4ceaa353d900bbd4ed`.
