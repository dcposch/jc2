# REP-96-INNER: the `(9,6)` representation question — family 2, `g = 3`, inner case

Lane: `REP-96-INNER`. Observed start 2026-09-01T22:26Z. Agent: Opus 5.
Desk-scale exact reasoning; finite group / integer scripts used as confirmation
of hand computations, and one exact rational Puiseux expansion. No Groebner
basis, no resultant, no ideal saturation, no CAS decision procedure.

## 0. Scope, custody, method

The three charged frozen copies were hashed with `shasum -a 256` before being
read; all three match the charge exactly:

```text
7247cef3961576b9919a2ca6e67c484f9f84e6e0af5bca4ceaa353d900bbd4ed  row-86-prebuild-opus5-20260901.md
a3c7137cdb2cf46c7d9026cfbcba54b0b6e5b47a6ef36ad7ee2976a905c8b196  encoding-faithfulness-audit-r2-sol56-20260901.md
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc  block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
```

Below: **PB** = the ROW-86 prebuild, **AUD** = the encoding-faithfulness audit,
**RK** = the rowkill coordinator integration. Campaign documents read on disk
and cited by file and section, not re-hashed as primary:
`shape-kill-uniform-opus5-20260901.md` §§1, 3.1–3.4 (cage, family-2 outer
relation, SK-4, the typed `OPEN[SHAPE-2-INNER-g>=3]` this lane attacks, and the
descent/classification split); `pi1-s4-decision-opus5-20260831.md` §§2, 3, 3.3
(local braids `(T)`/`(N_k)`, the disjointness verdict, Theorem A, the block-level
`delta_{d'}` action); `pi1s4-close-residual-r2-opus5-20260831.md` §§3.1–3.3
(tubular factorisation, Lemma 3.3, `A'(5)` held as GAP);
`nori-bc-extension-opus5-20260831.md` §3.5 ((M-INF-T), N-A-RES, Lemma 4.3);
`round1033-sheet-gate-opus5-20260831.md` §0, §5, `(M')`/`(M'-def)`;
`reducible-all-n-opus5-20260901.md:130-134, :459` (the `N = 4` profile and the
`b` census); `b0-reducible-n5-opus5-20260831.md:496-500` (`corr = 0` on both
`N = 4` dicriticals). No ledger or charged file was edited; `jc2-lean` was not
inspected.

**Method disclosure.** Four scripts were run, each re-doing a computation also
done by hand and recorded below in hand-checkable form:

1. enumeration of the `60` solutions of the outer word equation in `S_4`, of the
   `1080` block subtuples, of the Hurwitz action of `B_3` on `3`-tuples, and of
   the fixed sets of `delta^k . c_h` for every `k` (§3, §5);
2. the same machinery at `g = 2` on the promoted `(6,4)` row, as a positive and
   a negative control (§4);
3. an exact rational Puiseux expansion at infinity of three explicit curves,
   recovering `beta_1` from the curve rather than from a conversion table (§1);
4. exact verification of the realized `(9,6,2)` curve's identity, semigroup,
   node set, and vertical-tangency set (§1, §7).

Every permutation identity is a two-line hand check and was hand-checked;
`h = Y X^2 Y` at `(6,4)` was hand-evaluated to `X` before the script agreed.

**What this lane delivers.** A derivation, from scratch, of the family-2
block/cable structure at `g = 3`, a new theorem (§3, `PROVED-HERE`,
`UNREVIEWED`) that supplies the inner-braid ingredient which
`OPEN[SHAPE-2-INNER-g>=3]` names as missing, and its verdict on both live
`(9,6)` types. The verdicts concern the **`S_4` representation**, not
realizability. As at PB §0, a kill here removes a type from the `PI1-S4`
residual and asserts nothing about the existence of a polynomial curve.

## 1. The two types: data re-derived from the curves, not from a table

`(d,n) = (9,6)`, `a = d - n = 3`, `g = gcd(d,n) = 3`, `d' = 3`, `n' = 2`,
`p_a = (d-1)(d-2)/2 = 28`. The Galindo conversion for this row (AUD §3, quoting
NODAL-REALIZATION lines 19–25) is `beta_1 = d^2/g - c = 27 - c`, and the germ at
`P_inf` is one place with a single characteristic pair `(a; beta_1) = (3; beta_1)`,
`gcd(3, beta_1) = 1`, so

```text
delta_inf = (a-1)(beta_1-1)/2 = beta_1 - 1 ,     delta_aff = 28 - delta_inf = 29 - beta_1 ,
M_emb = a + beta_1 - 1 = beta_1 + 2 = M_inf .
```

I re-list the affine semigroups independently of AUD:

| type | `Delta` | `S_aff` | gaps | `delta_aff` | `beta_1` | `delta_inf` | `M_inf` |
|---|---|---|---|---:|---:|---:|---:|
| **`(9,6,2)`** | `(9,6,2)` | `<2,9>` | `1,3,5,7` | 4 | 25 | 24 | 27 |
| **`(9,6,4)`** | `(9,6,4)` | `<4,6,9>` | `1,2,3,5,7,11` | 6 | 23 | 22 | 25 |

Both are symmetric (Frobenius `7 = 2*4 - 1`, resp. `11 = 2*6 - 1`), as they must
be for one place at infinity, and `delta_aff + delta_inf = 28` on both rows. The
`delta_aff` values `4` and `6` are exactly the "four affine nodes" and the
"six-node target" of the charge. Nodality is the extra condition that every
affine double point be an `A_1`; every gate in §§2–5 depends only on the total
`delta_aff` and is blind to its partition into local `delta_p`.

**`beta_1` re-derived from the curves.** A conversion table is where a
flag/place/series confusion would hide, so `beta_1` was recomputed from the
parametrisations. With `t = 1/z`, `x = z^{-d}P(z)`, `y = z^{-n}Q(z)`,
`P = z^d p(1/z)`, `Q = z^n q(1/z)`, `P(0) = Q(0) = 1`, set `xi := x^{1/d}` and
invert `z = xi^{-1}P(z)^{1/d}` as a series in `xi^{-1}`; then
`y = xi^{n}(P^{-n/d}Q)(z(xi)) = sum_k c_k x^{k/d}`, and `k_*` is the largest `k`
with `a nmid k` — the second, and here last, characteristic exponent at
infinity. Exact rational arithmetic on the two explicit curves returns

```text
q = t^6+8t^2 ,   p = t^9+12t^5+24t :        nonzero k = 6, -6, -10, -14, ... ;  k_* = -10 ;
q0 = t^6+2t^4+(5/2)t^2 ,
p  = t^9+3t^7+(21/4)t^5+(35/8)t^3+(63/32)t : nonzero k = 6, 0, -8, -10, ... ;   k_* = -8 .
```

The general relation, derived once below at (2.3), is `k_* = 2d - a - beta_1`,
i.e. `beta_1 = 15 - k_*` here. So `beta_1 = 25` for the realized `(9,6,2)` curve
and `beta_1 = 23` for the `(9,6,4)` HF-twin curve — matching the table above,
computed with no conversion formula. Note in passing that the coefficients at
`k = 2` and `k = -2` **vanish** on the `(9,6,2)` curve: that vanishing is the
Abhyankar–Moh structure of the row, and it is exactly the datum the old raw
`(9,6)` ideals destroyed (AUD §1, §6 `type96_B`).

**The realized `(9,6,2)` curve, re-verified.** All of the following were
checked exactly:

```text
p^2 - q^3 - 64 q - 64 t^2 = 0                    (identity, exact)
deg p = 9 , deg q = 6 , gcd(p',q') = 1           (immersive, proper)
S_aff = <2,9> : gaps {1,3,5,7} , delta_aff = 4 , Frobenius 7 = 2*4-1
p = t (t^8 + 12 t^4 + 24) ,  p' = 3(3t^8 + 20t^4 + 8) ,  gcd(p,p') = 1
```

Four affine nodes: `p(-t) = -p(t)`, `q(-t) = q(t)`, so `t` and `-t` have the
same image exactly when `p(t) = 0`, `t != 0`; that is `w := t^4` a root of
`w^2 + 12w + 24`, giving `w = -6 +- 2*sqrt(3)` and eight values of `t` in four
`{t,-t}` pairs. Their four `q`-values are numerically distinct (`+-4.50413 i`,
`+-8.70131 i`), so the four images are four distinct points, and
`4 = delta_aff` exhausts the affine budget: **there are no other affine
singularities.** This reproduces AUD §6 by an independent route.

Two further facts about this curve, both used in §7 and neither in AUD:

* **all four nodes lie on the single line `x = 0`.** The eight node parameters
  are precisely the eight nonzero roots of `p`, so the fibre `x = 0` meets `D` in
  the four nodes (multiplicity `2` each) and the one smooth point `t = 0`,
  total `9 = d`.
* **the eight affine vertical tangencies are simple, at smooth points, in eight
  distinct fibres.** `p'` has eight distinct roots (`3t^8+20t^4+8` has two
  distinct nonzero `t^4`-values), `gcd(p,p') = 1` so none is a node, and the
  eight values of `p` at those roots are pairwise distinct.

So the braid monodromy factorisation of this curve over the `x`-line has exactly
nine singular fibres: eight simple tangency fibres and one fibre carrying all
four nodes. Exponent-sum ledger: `8*1 + 4*2 = 16`, and independently
`e(rho_inf) = 2 delta_aff + d - 1 = 8 + 8 = 16`. The two agree.

**Plücker class.** `m = d(d-1) - sum_p (mu_p+m_p-1) = 72 - (8 + 50) = 14` on
`(9,6,2)` (`4` nodes at `2` each; at `P_inf`, `mu_inf = 2 delta_inf = 48` and
multiplicity `a = 3`), and `72 - (12+46) = 14` on `(9,6,4)`. Positive on both:
a consistency check, not an obstruction. No Hessian or inflection kill is
claimed; no sourced Hessian multiplicity was consumed.

## 2. The family-2 block and cable structure at `g = 3`

`(9,6) = (3*3, 2*3)`, so the reduced shape is `(d',n') = (3,2)`, coprime, with
`d' = u = 3` odd and `n' = 2`: **`(9,6)` is the `g = 3` member of family 2**, in
the SHAPE-KILL classification (`shape-kill-uniform-opus5-20260901.md:275`,
`:363`). It is **not** family 3; PB's `3`-periodic block products, its cable
exponent `e(C_2(delta_4^3)) = 36` at `d' = 4`, and its gate `3 | e(iota)` are
`(4,3)`-shape statements and are not transported here. Everything in this
section is re-derived at `(3,2)`.

**Tubes.** Over `|x| = R` the `d = 9` roots `y_j(x) = sum_{k <= 6} c_k zeta_9^{jk} x^{k/9}`
fall into `d' = 3` blocks `B_i = {j : j = i mod 3}` of size `g = 3`: the leading
terms `c_6 zeta_9^{6j} x^{2/3} = c_6 zeta_3^{2j} x^{2/3}` take exactly three
values, one per residue of `j` mod `3`. The promoted tubular factorisation
(`pi1s4-close-residual-r2-opus5-20260831.md:186-206`) reads

```text
(2.1)   rho_inf = C_3(delta_3^2) . iota ,   iota in B_{3,1} x B_{3,2} x B_{3,3} ,
(2.2)   e(iota) = (d-1) + 2 delta_aff - n(d-g) = 8 + 2 delta_aff - 36 = 2 delta_aff - 28 ,
```

with `C_3` blackboard cabling, `e(C_3(delta_3^2)) = g^2 n'(d'-1) = 9*2*2 = 36`,
and `e(rho_inf) = 2 delta_aff + d - 1`. Numerically: `(9,6,2)` gives
`e(iota) = -20`, `(9,6,4)` gives `e(iota) = -16`.

**The outer datum.** `BP(T) = (Pi_1, Pi_2, Pi_3)` is a fixed point of the Hurwitz
action of `delta_{d'}^{n'} = delta_3^2` and is `n' = 2`-periodic (promoted
`A'(2)`), so it takes at most two values

```text
X := Pi_1 = Pi_3 ,   Y := Pi_2 ,
```

and, since `r = d' mod n' = 1`, conjugation by `Pi` is the shift by `-1`:
`Pi X Pi^{-1} = Y`, `Pi Y Pi^{-1} = X`. The total product is the alternating word
`Pi = Pi_1 Pi_2 Pi_3 = X Y X`. Substituting into the first conjugation relation,
`Pi X Pi^{-1} = XYX * X * X^{-1}Y^{-1}X^{-1} = XY X Y^{-1} X^{-1}`, and setting
this equal to `Y` gives, after right-multiplying by `XY`,

```text
(SK-3.1 at u=3)      X Y X = Y X Y ,
```

the **braid relation** — SHAPE-KILL's deformed braid relation `X W^m X = W^{m+1}`
at `m = 1`, `W = XY`. The conversion is an identity, not a transplant: at `u = 3`
the two forms coincide.

**Parity fork.** Each block product `Pi_i` is a product of `g = 3` transpositions,
hence an **odd** permutation: a transposition or a `4`-cycle. This is the exact
point at which family 2 at `g = 3` diverges from family 2 at `g = 2` (where
`X,Y in A_4`) and from family 3 (where `Pi_i in A_4` because `g = 2` there too);
SHAPE-KILL §3.3 item 1 names precisely this divergence. Correspondingly
`sgn(Pi) = (-1)^d = -1`, so `Pi` is a transposition or a `4`-cycle and **`Pi` is
never in `V_4`** — with consequences in §6.

**The outer solution set, exhaustively.** Solving `XYX = YXY` over the `12` odd
elements of `S_4` gives exactly `60` pairs, in four strata:

| stratum | description | count | `W = XY` | `Pi = XYX` | `h := Y X^2 Y` |
|---|---|---:|---|---|---|
| `const-T` | `X = Y` a transposition | 6 | `e` | `X` | `e` |
| `const-4c` | `X = Y` a `4`-cycle | 6 | `X^2` | `X^{-1}` | `e` |
| `noncst-T` | `X != Y` transpositions meeting in one letter | 24 | `3`-cycle | transposition | `e` |
| `noncst-4c` | `X != Y` `4`-cycles | 24 | double transposition | transposition | double transposition |

There are **no mixed solutions** (one transposition and one `4`-cycle). The
promoted `A'(4)` (`Pi^{n'} = Pi^2 in Z(H)`, `H = <Pi_1, Pi>`) holds in all `60`
cases and therefore carries no information at this shape — the `g = 3` analogue
of PB §3's "Route 2 is vacuous" verdict, confirmed here by enumeration rather
than transported. Note also that at `g >= 3` the constant stratum is **not** free
to kill: SHAPE-KILL §3.3 item 3 records that Lemma SK-2 needs the block
`(tau,tau)`, which is not `B_g`-fixed for `g >= 3`. The constant stratum is
therefore carried through §3 and disposed of there on its merits, not by
analogy.

**The block-level cable action, derived at `d' = 3`.** With the promoted left
Hurwitz convention `sigma_i . (.., t_i, t_{i+1}, ..) = (.., t_i t_{i+1} t_i^{-1}, t_i, ..)`
and `(beta gamma).T = beta.(gamma.T)`, `delta_3 = sigma_1 sigma_2` acts on a
`3`-tuple by

```text
delta_3 . (u_1,u_2,u_3) = sigma_1 . (u_1, u_2 u_3 u_2^{-1}, u_2) = ((u_1u_2) u_3 (u_1u_2)^{-1}, u_1, u_2) ,
```

so the conjugator is `u_1 u_2`, i.e. `Pi Pi_{d'}^{-1}` and **not** `Pi`. Cabling
by `C_g` (promoted Lemma 3.3, `C_g(sigma_i).(A,B) = (Pi_A B Pi_A^{-1}, A)`
entrywise) gives, on block tuples with block products `(P_1,P_2,P_3)`,

```text
(2.4)   C_3(delta_3) . (B_1,B_2,B_3) = ( c_{P_1 P_2}(B_3) , B_1 , B_2 ) ,
```

`c_h` denoting entrywise conjugation. Internal check: applying block products to
`(2.4)` at `(P_1,P_2,P_3) = (X,Y,X)` sends the block products to
`(XY X (XY)^{-1}, X, Y) = (Y, X, Y)` by the braid relation, and a second
application returns `(X, Y, X)`. So `C_3(delta_3^2)` preserves the block-product
sequence, as it must; a mis-assigned conjugator would break this.

**The winding computation, and the general exponent identity.** As `x` traverses
one loop, `x^{k/9} -> x^{k/9}zeta_9^{k}`, so `y_j -> y_{j+1}`: `rho_inf` has
permutation the `9`-cycle `j -> j+1` (the one-place-at-infinity condition), and it
cycles the three tubes, so a tube returns to itself after **three** loops. Within
tube `B_i` the mean of the three strands retains only the `3 | k` terms, and the
three deviations are `sum_{3 nmid k} c_k zeta_9^{jk} zeta_3^{rk} x^{k/9}`,
`r = 0,1,2`: at the largest such `k`, namely `k_*`, they are the vertices of an
equilateral triangle, `zeta_3^{k_*}` being a primitive cube root, and that term
dominates all later ones as `R -> infinity`. So for `R` large the tube is a
**rigidly rotating triangle**, turning by `3k_*/9 = k_*/3` full turns over the
three loops. Rotation of a regular `g`-gon by `1/g` turn is
`delta_g := sigma_1 ... sigma_{g-1}`, `e(delta_g) = g-1`, and a full turn is the
full twist `delta_g^g`; hence the accumulated inner braid is `delta_g^{k_*}` and

```text
(2.3)   k_* = 2d - a - beta_1 ,        e(iota) = k_*(g-1) .
```

Left half: at `P_inf` the place is `v = s^a`, `u = sum_{k >= d}c_k s^k` with first
non-`a`-divisible exponent `beta_1`; `y = v/u = s^{a-d}U^{-1}`,
`U = sum c_k s^{k-d}`, whose first non-`a`-divisible power `s^{beta_1-d}` survives
inversion; `s ~ x^{-1/d}` then gives `k_* = 2d - a - beta_1`. At `(9,6)`,
`k_* = 15 - beta_1` and `e(iota) = 2k_*`; both halves are checked in §4.

## 3. THEOREM CABLE-3 — the inner gate at `g = 3`

SHAPE-KILL §3.3 types `OPEN[SHAPE-2-INNER-g>=3]` and names the missing
ingredient: *the inner braid `iota`, numerically pinned by (1.1) to `e(iota)`
but not otherwise constrained*. At `g = 2` the tube group `B_2 = Z` is abelian
and the exponent sum is a complete invariant, which is what PB §4 exploits. At
`g = 3` the tube group `B_3` is **not** abelian and the exponent sum is **not**
complete — PB §5 ("Where TUBE-2 stops") says so explicitly. The move made here
is different, and it is the reason the `g >= 3` case opens: for a curve with one
place at infinity and a **single** characteristic pair at infinity, `iota` is not
merely constrained by its exponent sum, it is **rigid** — pinned to a rotation by
the Puiseux data, by §2's winding argument. The exponent sum survives only as a
check.

> **THEOREM CABLE-3 (`PROVED-HERE`, `UNREVIEWED`).** *Let `D` be a residual
> branch curve of family-2 shape `(d,n) = (3g, 2g)`, `g >= 2`, with one place at
> infinity carrying a single characteristic pair `(a; beta_1)`, `a = d - n = g`,
> `gcd(a, beta_1) = 1`; and suppose `phi : pi_1(C^2 - D) ->> S_4` sends every
> meridian to a transposition. Put `k_* := 2d - a - beta_1` and
> `h := Y X^2 Y`, where `(X,Y) = (Pi_1, Pi_2)` is the outer datum of §2. Then the
> block subtuple `T_1` of any `rho_inf`-fixed tuple satisfies*
>
> ```text
> (3.1)     T_1  =  delta_g^{k_*} . c_h(T_1) ,        delta_g = sigma_1 ... sigma_{g-1} ,
> ```
>
> *up to replacing `T_1` by a point of its `B_g`-orbit; and*
>
> ```text
> (3.2)     im(phi)  =  < entries of T_1 ,  entries of c_{XY}(T_1) > .
> ```

*Proof.* Write `T = (T_1,T_2,T_3)` in blocks and `S := iota . T`, so `S_i = iota_i . T_i`
and each `S_i` has the same block product as `T_i`. Since `(beta gamma).T = beta.(gamma.T)`,
`rho_inf . T = T` reads `C_3(delta_3^2) . S = T`. Applying `(2.4)` twice, with block
products `(X,Y,X)` before the first application and `(Y,X,Y)` before the second,

```text
C_3(delta_3^2) . S = ( c_{YX}(S_2) ,  c_{XY}(S_3) ,  S_1 )  =  (T_1, T_2, T_3) .
```

Conjugation commutes with the Hurwitz action (the action is by words in the
entries), so composing the three relations around the cycle
`T_1 <- T_2 <- T_3 <- T_1` gives

```text
T_3 = iota_1 . T_1 ,
T_2 = c_{XY}(iota_3 . T_3) = (iota_3 iota_1) . c_{XY}(T_1) ,
T_1 = c_{YX}(iota_2 . T_2) = (iota_2 iota_3 iota_1) . c_{(YX)(XY)}(T_1) ,
```

that is `T_1 = beta . c_h(T_1)` with `beta := iota_2 iota_3 iota_1 in B_g` and
`h = (YX)(XY) = Y X^2 Y`. **Only the ordered product `beta` survives; the
distribution of `iota` among the three tubes is irrelevant.** Its exponent sum is
`e(beta) = e(iota)`.

By §2's winding computation, over the three loops of `x` that return a tube to
itself the `g` strands of that tube move as a rigidly rotating regular `g`-gon
through `k_*/g` full turns; blackboard cabling adds no twist. The accumulated
inner braid is therefore `delta_g^{k_*}`, and `beta` — which is exactly that
accumulated braid, read from whichever tube carries the basepoint and under
whichever identification of the tube's strands with `{1,..,g}` — is **conjugate
in `B_g`** to `delta_g^{k_*}`. Write `beta = gamma delta_g^{k_*} gamma^{-1}`.
Since `c_h` commutes with the Hurwitz action,

```text
T_1 = gamma delta_g^{k_*} gamma^{-1} . c_h(T_1)
   <=>  (gamma^{-1}.T_1) = delta_g^{k_*} . c_h(gamma^{-1}.T_1) ,
```

so replacing `T_1` by `gamma^{-1}.T_1` — which changes neither the block product,
nor the subgroup generated by the entries, nor therefore `(3.2)` — puts the
condition in the form `(3.1)`.

For `(3.2)`: `T_3 = iota_1 . T_1` and `T_2 = (iota_3 iota_1).c_{XY}(T_1)` lie in
the `B_g`-orbits of `T_1` and of `c_{XY}(T_1)`, and the Hurwitz action preserves
the subgroup generated by the entries of a tuple. Hence the nine entries of `T`
generate `< T_1 > . < c_{XY}(T_1) >` as claimed. `[]`

**Consistency at `g = 2`.** There `delta_2 = sigma`, `e(iota) = k_*`, and on the
promoted `(6,4)` row `X,Y` are distinct `3`-cycles (SK-4) with `h = YX^2Y = X` —
hand-evaluated, e.g. `(234)(124)^2(234) = (234)`. Since `sigma^2 = c_{uv} = c_X`
on a block `(u,v)` with `uv = X`, `(3.1)` becomes `T_1 = sigma^{k_*+2}.T_1`,
solvable exactly when `3 | k_*+2` — verbatim PB §5's Control 2 gate. CABLE-3
**specialises to the promoted `g = 2` statement**; it is not a new convention,
and §4 Control 2 runs both halves of it.

**Solution at `g = 3`.** The tuple `T_1 = (t_1,t_2,t_3)` runs over triples of
transpositions with product `X`; there are `1080` pairs (outer solution, `T_1`)
in total. `delta_3^3` is the full twist and acts as `c_X`, so the fixed set of
`delta_3^{k}.c_h` depends only on `k` modulo `3 * ord(X) in {6,12}`. Exhaustive
evaluation over all `60` outer solutions and all `1080` subtuples, for every
residue of `k`, gives the following table; entries are (number of fixed `T_1`
with `im(phi) = S_4`) / (number of fixed `T_1`).

```text
   k   |  const-4c   const-T    noncst-4c   noncst-T
  -----+---------------------------------------------
   0   |    96/96      0/120        0/0      264/480
  -1   |     0/0        0/6         0/0        0/24
  -2   |     0/0        0/30       96/96      48/120
  -3   |     0/0        0/24        0/0       72/96
  -4   |    24/24       0/30        0/0       48/120
  -5   |     0/0        0/6         0/0        0/24
  -6   |     0/0        0/120     384/384    264/480
```

(the table is `12`-periodic in `k`; `k = -7,...,-12` repeat `k = -1,...,-6`).
Reading it:

* **`const-T` is dead at every `k`.** Here `W = XY = X^2 = e`, so by `(3.2)`
  `im(phi) = <T_1>`, and `T_1` is three transpositions with product a
  transposition, which generates a subgroup of order at most `6`. This is the
  `g = 3` replacement for Lemma SK-2, proved on its merits rather than assumed.
* **`const-4c` requires `4 | k_*`;** **`noncst-4c` requires `k_* = 2 (mod 4)`;**
  **`noncst-T` requires `k_*` even, given `3 nmid k_*`.**
* `3 nmid k_*` is automatic: it is the definition of `k_*` together with
  `a = g = 3`, and it is equivalent to the permutation of `rho_inf` being a
  `9`-cycle, i.e. to one place at infinity.

Combining the three live strata:

> **GATE-3.** *On a family-2 row with `d' = 3`, `g = 3` (i.e. `(d,n) = (9,6)`),
> one place at infinity and a single characteristic pair, a `rho_inf`-fixed tuple
> with `im(phi) = S_4` exists only if*
>
> ```text
> (3.3)     k_*  is EVEN   <=>   4 | e(iota)   <=>   2 | delta_aff   <=>   2 | c .
> ```
>
> *Moreover the stratum is then pinned: `k_* = 2 (mod 4)` allows only `noncst-4c`
> and `noncst-T`; `k_* = 0 (mod 4)` allows only `const-4c` and `noncst-T`.*

The equivalences in `(3.3)` are `k_* = 15 - beta_1`, `delta_aff = 29 - beta_1`
(so `delta_aff - k_* = 14` is even), `beta_1 = 27 - c` (so `k_* = c - 12`), and
`e(iota) = 2k_*`.

**The exponent sum alone would give nothing.** For each of the `1080` pairs
(outer solution, `T_1`) the twisted stabiliser `{beta in B_3 : beta.c_h(T_1) = T_1}`
is a coset of `Stab(T_1)`, and its exponent-sum image was computed modulo
`24` (a period, since `delta_3^{3 ord(X)}` acts trivially and
`6 ord(X) | 24`). At `e(beta) = -20` and at `e(beta) = -16` alike, **all `1080`
pairs admit some `beta` of the required exponent sum**, `744` of them with full
image. So the `g = 2` argument shape — pin `iota` by `e(iota)` and read off a
stabiliser index — is *provably vacuous* at `g = 3`, exactly as SHAPE-KILL §3.3
predicted. Every bit of GATE-3 comes from rigidity, not from the exponent sum;
the exponent sum survives only as the consistency check `e(delta_3^{k_*}) = 2k_*
= e(iota)` of §4.

**GATE-3 is not vacuous.** The residues `k_* = 1, 5, 7, 11 (mod 12)` — that is,
`gcd(k_*, 6) = 1` — admit **no** fixed tuple with full image, in any stratum.
Half the admissible residues die. This is the exact `g = 3` analogue of the
`g = 2` gate `3 | e(iota)+2`, derived from scratch, and it has a different
modulus and a different arithmetic content, as the charge anticipated.

## 4. Verification: three routes and four controls

CABLE-3 is worthless if `k_*` is wrong or if the block reduction has a
convention error, so both are checked by routes that share no step.

**Route 1 (discriminant bookkeeping).** `e(rho_inf) = deg_x disc_y F = sum_p (mu_p+m_p-1)`
over affine points; `mu_p+m_p-1 = 2 delta_p + (m_p-r_p)`, and `sum_p (m_p-r_p)`
plus the smooth vertical tangencies is the affine ramification `d-1` of
`p : P^1 -> P^1`. So `e(rho_inf) = 2 delta_aff + d - 1` unconditionally, for any
affine singularity types; subtracting `e(C_3(delta_3^2)) = 36` gives `(2.2)`.
`(9,6,2)`: `-20`. `(9,6,4)`: `-16`.

**Route 2 (Puiseux winding).** `(2.3)` gives `e(iota) = k_*(g-1) = 2k_*` with
`k_* = 15 - beta_1`. `(9,6,2)`: `2(15-25) = -20`. `(9,6,4)`: `2(15-23) = -16`.
The two routes agree identically, and the identity behind the agreement is
general: `(d-1)^2 - (a-1)(beta_1-1) - n(d-g) = (2d - a - beta_1)(g-1)` for
`d = gu`, `n = 2g`, `a = g(u-2)` at `u = 3`.

**Route 3 (from the curves).** §1 computed `k_*` by exact rational Puiseux
expansion of the two explicit parametrisations and got `-10` and `-8`, i.e.
`beta_1 = 25` and `23`, with no conversion formula in the loop.

**Control 1 — parity / one place at infinity.** The permutation of
`C_3(delta_3^2)` on nine strands is three disjoint `3`-cycles (blackboard
cabling preserves within-block order, and the tube permutation is a `3`-cycle).
The composite with `iota` is a `9`-cycle iff the product of the three tube
permutations is a `3`-cycle, i.e. iff `3 nmid k_*`. That is exactly the
one-place-at-infinity condition and it holds on both rows (`k_* = -10, -8`).

**Control 2 — the promoted `(6,4)` row, positive.** Running the *same* block
reduction at `g = 2` (blocks of size two, `B_2 = <sigma>`): the outer solutions
of `XYX = YXY` in `A_4` number `36`, of which `24` are the SK-4 non-constant
`3`-cycle pairs; on every one of them `h = Y X^2 Y = X` and `Pi = WX` is a double
transposition, reproducing SK-4 `(3.3)`. The fixed-tuple count as a function of
`E = k_*`: `72/72` full-image tuples at `E = -8, -5, -2` and `0` at every other
residue — the gate `3 | E + 2`. The realized `(6,4,3)` row has `E = -5` and
**passes**; the hypothetical `delta_aff = 4` row has `E = -3` and is **killed**.
Both match PB §5 Control 2 exactly, including the negative half.

**Control 3 — the `(6,4)` row through Route 3.** The exact Puiseux routine of §1,
run on the ROW-NF sextic `x = r(t)^2`, `r = t^3+bt+c`, `y = t^4+(2b/3)t^2+(4c/3)t`
at `b = c = 1`, returns `k_* = -5`, `beta_1 = 15`, `e(iota) = -5`: PB's Control-2
value, obtained from the curve.

**Control 4 — `A'(4)` and the outer relation.** `Pi^{n'} = Pi^2 in Z(<Pi_1,Pi>)`
was verified on all `60` outer solutions (it holds identically, hence is
information-free here), and the braid relation was cross-checked against the two
conjugation relations `Pi X Pi^{-1} = Y`, `Pi Y Pi^{-1} = X` rather than assumed.

**Where CABLE-3 stops.** The rigidity step uses that the germ at infinity has a
**single** characteristic pair, so that exactly one Puiseux exponent separates the
strands within a tube and the tube configuration is asymptotically a regular
`g`-gon. With two or more pairs at infinity the inner braid is itself an iterated
cable and `(3.1)` acquires a second layer. Both `(9,6)` rows have one pair, so
the theorem covers them; the general family-2 statement at `g >= 3` does not
follow, and is left as `OPEN[SHAPE-2-INNER-MULTIPAIR]`.

## 5. Verdicts per type

```text
type        Delta      delta_aff  beta_1  delta_inf  M_inf   k_*   e(iota)   GATE-3
(9,6,2)   (9,6,2)          4        25       24       27    -10     -20     PASSES (k_* = 2 mod 4)
(9,6,4)   (9,6,4)          6        23       22       25     -8     -16     PASSES (k_* = 0 mod 4)
```

**Both types survive GATE-3.** Neither is killed at the representation level by
the inner braid. The residual is not merely non-empty, it is small and explicit;
up to simultaneous `S_4`-conjugacy the surviving data `(X, Y, T_1)` are:

```text
Delta = (9,6,2)  (6 classes, each a 24-element conjugacy orbit; 144 tuples in all)
   noncst-T :  X=(34) Y=(23) Pi=(24) ,  T_1 = ((13),(14),(13))  or  ((14),(13),(14))
   noncst-4c:  X=(1234) Y=(1243) Pi=(34) ,
               T_1 = ((12),(23),(34)) , ((23),(34),(14)) , ((34),(14),(12)) , ((14),(12),(23))

Delta = (9,6,4)  (3 classes; 72 tuples in all)
   noncst-T :  the same two classes as above
   const-4c :  X=Y=(1234) , Pi=(1432) ,  T_1 = ((34),(14),(12))
```

with `T_2, T_3` then determined by `T_1` and `iota` through the displayed
relations, and `im(phi) = S_4` verified on each class by `(3.2)`. In particular
`Pi` is a transposition on every `(9,6,2)` class and on two of the three
`(9,6,4)` classes, and a `4`-cycle on the third — never in `V_4`, as §2's parity
fork requires.

**Typed:** `Delta = (9,6,2)` — **survives GATE-3**, `OPEN` at the finer inputs of
§7. `Delta = (9,6,4)` — **survives GATE-3**, `OPEN`, and additionally sits
exactly on the N-A boundary (§6), so a YES on
`OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]` would kill it while leaving `(9,6,2)`
untouched. **The `(9,6)` row does not die at the representation level by any
gate this lane can construct.** Combined with AUD's realization of `(9,6,2)`,
the charge's dichotomy resolves in the direction that keeps the row alive.

## 6. Every other promoted gate, run against `(9,6)`

A missed kill costs a false alarm; a falsely applied one costs a missed
counterexample. Every promoted gate in the residual machinery is therefore run
explicitly, with its scope stated.

**(M-INF) and (M-INF-T) (Corollary N-A-RES).** `M_inf <= 3d-3 = 24` implies
`pi_1(C^2-D) = Z`; here `M_inf = beta_1+2` is `27` and `25`, missing by `3` and by
`1` (equivalently the kill fires iff `beta_h <= 2d+n-2 = 22`, and
`beta_1 = 25, 23`). With the tangential refinement, slack
`= 24 - M_inf - 2T = -3-2T` and `-1-2T`: monotone the wrong way, impossible at
every `T`, nodal or not. Both go **silent** on both types at every affine
configuration; silence is not `pi_1 != Z`.

**The N-A boundary.** With `r_1 = delta_aff`, `T = T_x = 0`, the promoted Lemma
4.3 gives `C'^2 - 2 delta_aff = 3d - 2 - M_inf = 25 - M_inf`:

```text
(9,6,2):  C'^2 - 2 r_1 = -2   (N-A reads 6 > 8 , false by two units)
(9,6,4):  C'^2 - 2 r_1 =  0   (N-A reads 12 > 12 , false by one unit — exactly on the boundary)
```

`(9,6,4)` therefore joins `(8,6,11)`, `(6,4)` and `(8,4)` on the N-A boundary: a
YES on `OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]` would kill it. I record the
coincidence and do **not** relax `>` to `>=`; the promoted sharpness datum
concerns the `T_x` coefficient on a reducible configuration and settles nothing
for irreducible `C`. `(9,6,2)` has deficit `2` and is out of reach of any such
relaxation.

**Shirane Cor 0.6 / torus-type exclusion / the `S_3` resolvent.** The `(6,4)`
chain (RK §1) descends `pi_1(A^2-D) ->> S_4 -> S_4/V_4 = S_3` to
`pi_1(P^2-Dbar)`, builds the triple cover, applies Shirane's classification of
normal triple covers with **degree-6** branch divisor to force torus type, and
contradicts NO-TORUS. Two independent reasons it does not reach `(9,6)`:
(i) *the descent does not exist* — it needs the loop at infinity to die in `S_3`,
i.e. `Pi in V_4`, whereas `sgn(Pi) = (-1)^9 = -1` (§2), confirmed on all `60`
outer solutions and all `9` surviving classes of §5, where `Pi` is a
transposition or a `4`-cycle; this instantiates SHAPE-KILL §3.4's "family 2 has
no surviving odd-`g` row that admits the `S_3` descent". (ii) *the classification
input is degree-6-specific*: `deg Dbar = 9`, and the weighted `Dbar + 2L_infty`
has degree `11`. RK §3's stop is respected: the row-kill covers the **explicit**
degree-6/8 families, and THEOREM EXHAUST identifies one-place curves *with the
row invariants in the reviewed gauge* — which degree `9` is not.
**Not a kill; not applicable.**

**INF-TRIVIAL (the even-word mechanism).** At `(6,4)` it runs off `x = r(t)^2`:
the fibre `x = 0` is tritangent, ZvK identifies `g_1=g_2`, `g_3=g_4`, `g_5=g_6`,
and `gamma_inf = g_5^2 g_3^2 g_1^2` is a product of squares, killed by any
involution-meridian representation — contradicting `phi(gamma_inf) = Pi != 1`. At
`(9,6)` the mechanism is not merely unavailable, it is **refuted unconditionally
by parity**: every fibre of the `x`-projection meets `D` with multiplicities
summing to `d = 9`, so the meridian word has odd length and
`sgn(phi(gamma_inf)) = -1`. No fibre degeneration can present `gamma_inf` as a
product of squares at odd `d`. (PB §7 proves the `(8,6)` corollary conditionally
on `phi` via SK-5; at odd `d` it is unconditional.) On the realized curve the
`x = 0` fibre carries the four nodes plus one smooth point, and at a node the two
branch meridians go to **disjoint** transpositions (promoted, `pi1-s4-decision`
§2), giving `Pi in V_4 * tau` — odd, consistent, no contradiction.
**Not a kill.**

*Corollary, recorded:* PB §7's item-2 criterion — a line through four affine
nodes and nothing else forces `phi(gamma_inf) in V_4` — fails on this curve **by
exactly one unit of degree**. The line `x = 0` does pass through all four nodes,
but `deg Dbar = 9 = 4*2 + 1` leaves one residual smooth intersection. Had the
degree been `8` this configuration would have been a kill.

**THEOREM TB / Proposition TB-2.** Family-3 (`(4,3)`-scaling) results: mixed
cover with `S_pi = Dbar`, `T_pi = L_infty`, weighted branch degree `4g+2`,
`k = 2g+1`, chart orders `(g,4g)`. At `(9,6)` the shape is `(3,2)` and the chart
orders are `(a,d) = (3,9)`. No promoted family-2 analogue exists.
**Not applicable**; recorded as `OPEN[TB-FAMILY-2]`, not filled by analogy.

**Theorem A, SK-1/SK-4/SK-5, degree.** Theorem A needs `gcd(d,n) = 1`; here
`gcd = 3` (its block-level consequence `sgn(Pi) = (-1)^d` is used). SK-1 is
family `(u,1)`, SK-4 family 2 at `g = 2`, SK-5 family `(4,3)`: `(9,6)` is
outside all three, which is why it was typed `OPEN[SHAPE-2-INNER-g>=3]`.
`OPEN[CAMPAIGN-PIN-D1-DMIN-BOUND]` is open and NO-DEG-CAP says no degree, genus
or delta gate can close the reducible cage, so degree `9` is not itself an
obstruction.

## 7. CRITICAL FORK — what stands between `(9,6,2)` and a Keller map

`(9,6,2)` is realized as a curve (AUD §6, re-verified in §1) and survives the
representation gate (§5). It is therefore the campaign's strongest
counterexample-candidate substrate to date, and the honest question is what is
still missing. Four things are, in increasing order of cost.

**(R1) The full braid-monodromy factorisation, not the product.** `rho_inf`-fixedness
is one relation — the *product* of the local relations. A representation exists iff
the nine-tuple `T` is fixed by **every** local braid. For this curve the
factorisation census is exact (§1): eight simple vertical tangencies, in eight
distinct fibres, at smooth points, each contributing a `sigma_i` whose fixed-tuple
condition is the identification `(T)`: `xi_i = xi_{i+1}`; and **one** fibre,
`x = 0`, carrying all four nodes, contributing four commuting `sigma_i^2` whose
fixed-tuple condition is `(N_1)`: `[xi_i, xi_{i+1}] = 1`, satisfied exactly by
disjoint transpositions. Exponent ledger `8*1 + 4*2 = 16 = 2 delta_aff + d - 1`:
the census is complete, no local braid is missing.

Two structural consequences are available without computing the transports:

* the eight tangencies form a **tree** on the nine sheets. `p : C -> C` is degree
  `9` with eight simple critical points and connected total space, so
  Riemann–Hurwitz gives `1 = 9 - 8` and the eight sheet-transpositions generate a
  transitive subgroup of `S_9` with eight edges on nine vertices: a spanning
  tree. In `H_1` this collapses all nine meridians and gives `H_1 = Z`, as it must;
  it does **not** force equality of the `phi`-images, because each ZvK relation is
  `xi_a = w xi_b w^{-1}` for a transport word `w`. No cheap kill here, and none is
  claimed.
* the `x = 0` fibre pins `Pi` further than `sgn` does. `Pi = phi(gamma_inf)` is the
  product of the nine fibre meridians; grouping them by the degeneration at
  `x = 0` gives `Pi in V_4 * tau`, `tau := phi(g_9)` the meridian at the smooth
  point `t = 0` (each node contributes a product of two disjoint transpositions,
  which lies in the normal subgroup `V_4`). By §5, `Pi` is a **transposition** on
  every surviving `(9,6,2)` class. Hence `Pi tau in V_4` forces `tau = Pi` or
  `tau` disjoint from `Pi`: **two of the six transpositions**, not six. That is a
  genuine additional pin on any realization, obtained from the curve.

What is not available at desk scale is the transport data itself. Computing the
eight tangency transports for this degree-9 curve and intersecting the nine fixed
sets is a finite, decidable computation, and it is the **cheapest decisive next
step**: it either produces an explicit `phi` on `pi_1(C^2 - D)` — the first in the
campaign — or kills `(9,6,2)` outright. Typed `OPEN[REP-96-BM-FACTORISATION]`.

**(R2) Covering-space realization (Riemann existence), and the source.** A `phi`
fixed by the whole factorisation gives only a degree-4 branched cover `Y -> C^2`
with branch locus `D` and meridian data `T`. A Keller map additionally requires
the **source** to be the affine plane, `Y ~ C^2`, plus the normality and
miracle-flatness step RK §1 records as gate-inserted into the `(6,4)` descent.
Riemann existence supplies `Y` as a normal surface and nothing about its
isomorphism type; `Y ~ C^2` follows from no promoted result and is not implied by
`pi_1`. Then `F : Y = C^2 -> C^2` must have `Jac F in C^*` with non-properness set
`A_F`. **This is the largest single gap, and it is not numerical.** Typed
`OPEN[REP-96-SOURCE-IS-C2]`.

**(R3) The `b = 0` / budget constraints.** Two distinct symbols `b` are in play and
must not be merged: in THEOREM 7.B (all-degree H2 integration §1) `b = 0` is the
count of dicriticals with affine image and `mu = 1`, a **consequence of H2**;
in the reducible cage (`reducible-all-n-opus5-20260901.md:130-134`) `b` is the
number of **branched components** of `A_F`, and `(RC2)` forces `b = 1` at
`N = 4, 5`. I use only the second.

The `N = 4` residual profile is a single row: core `(2,1,0)`, `W = (1,2)`
(`ibid.:459`), i.e. `A_F` has one branched component `D_1` of weight `2` and one
trivial-dicritical component of weight `1`; and `corr = 0` on both dicriticals, so
the branched component carries **only double points of smooth branches**
(`b0-reducible-n5-opus5-20260831.md:496-500`). Checked against the realized curve:
its four affine singularities are ordinary nodes of two smooth branches
(§1) — **consistent**. The generic-meridian datum matches too: `a^{(1)} = N - W_1 = 2`
and independently `a^{(1)} = #Fix(transposition) = 2`. The budget therefore does
not obstruct `(9,6,2)`; but it does demand a **second component**, of degree at
least `2` (Lemma NL), about which the numerical type says nothing. A counterexample
needs that companion curve as well.

**(R4) The `(M')` identity.** `(M')`
(`round1033-sheet-gate-opus5-20260831.md:442`) is
`a(nu + s - 1) - sum_{p in Sing A_F} a_p = d nu - 1` with `1 <= a <= d-2`,
`0 <= a_p <= a`, `nu = sum_p (r_p - 1)`, `s = #Sing A_F`, `d = N`. **Its
hypotheses are Keller + (H2) + (H3)**, and `(H2)` is `A_F` irreducible. Two
statements, kept apart:

*Under `(H2)` it is fatal — and it is exactly the promoted `N = 4` H2 closure.*
For a nodal `A_F` with `s` nodes, `nu = s`, so `(M'-def)` reads
`sum_p (a - a_p) = (a-1) + s(4-a)`, whose left side is at most `s a`. At `a = 2`:
`2s >= 1 + 2s`, false for every `s >= 0`. At `a = 1`: `s >= 3s`, false for every
`s >= 1`. So no nodal `N = 4` residual survives `(M')` under `(H2)` — which
reproduces the promoted "B0 holds at `N = 4` under H2". This is a control on my
use of the identity, not a new kill.

*The `(9,6,2)` candidate does not live under `(H2)`.* The `N = 4` residual is the
reducible-`A_F` case (the H2 branch is closed), so only the block-free form
applies:
`sum_i a^{(i)} chi_c(D_i \ Sing D) + sum_p a_p = 1 - d chi_c(V)`
(`ibid.:462-466`). Instantiating it on the `N = 4` profile — `D = D_1 u D_2`,
`a^{(1)} = 2`, `a^{(2)} = N - W_2 = 3`, `D_1` with `s_1` nodes and normalization
`A^1`, `D_2` with `sigma_2` nodes and `chi_c(D_2) = chi_2`, meeting `D_1`
transversally in `j` points; `a_p = 0` at a node of `D_1` (two disjoint size-2
clusters exhaust the four letters), `a_p = 1` at a transverse `D_1 u D_2` point
(clusters `2 + 1`), `a_p = 2` at a node of `D_2` (clusters `1 + 1`) — the identity
collapses to

```text
(7.1)     chi_2 + sigma_2 = 1 ,   i.e.   D_2 also has normalization A^1 ,
```

**with `s_1` cancelling identically.** So at the `N = 4` reducible profile `(M')`
is *blind to the affine node count of the branched component*: it constrains only
the companion component's topology. It neither kills nor supports `(9,6,2)`, and
it must not be quoted as doing either. Typed `OPEN[REP-96-MPRIME-COMPANION]`: the
identity becomes binding only once `D_2` is pinned.

**Summary of the fork.** Between "`(9,6,2)` is a realized numerical type with a
surviving `S_4` representation datum" and "a Keller counterexample exists" stand:
`OPEN[REP-96-BM-FACTORISATION]` (finite, decidable, cheapest);
`OPEN[REP-96-SOURCE-IS-C2]` (the hard geometric step);
`OPEN[REP-96-MPRIME-COMPANION]` (needs `D_2`); plus the construction of `D_2`
itself. **No promoted theorem kills `(9,6,2)`.** The row is alive on the merits,
not by a gap in the search.

## 8. Typed verdict block, OPENs, deviations

```text
LANE            REP-96-INNER  (family 2, g = 3, inner case)
THEOREM CABLE-3 PROVED-HERE, UNREVIEWED.  Specialises to the promoted g=2 gate
                (PB Control 2) on both its positive and its negative half.
GATE-3          k_* even  <=>  4 | e(iota)  <=>  2 | delta_aff  <=>  2 | c.
                Non-vacuous: gcd(k_*,6) = 1 admits no full-image fixed tuple.

Delta = (9,6,2) : delta_aff 4 , beta_1 25 , delta_inf 24 , M_inf 27 , k_* -10 ,
                  e(iota) -20 .   GATE-3: PASSES .   VERDICT: SURVIVES the
                  representation gate; OPEN at OPEN[REP-96-BM-FACTORISATION].
                  Residual pinned: 6 classes up to S_4-conjugacy (§5).
Delta = (9,6,4) : delta_aff 6 , beta_1 23 , delta_inf 22 , M_inf 25 , k_*  -8 ,
                  e(iota) -16 .   GATE-3: PASSES .   VERDICT: SURVIVES; OPEN,
                  and additionally exactly on the N-A boundary, so a YES on
                  OPEN[NA-R1-SHARPNESS-IRREDUCIBLE] kills it. 3 classes (§5).

ROW VERDICT     The (9,6) row is NOT killed at the S_4 representation level.
                Given AUD's realization of (9,6,2), the row is alive.
```

**Scope, stated exactly.** GATE-3 is a necessary condition for a `rho_inf`-fixed
tuple with image `S_4`. Passing it is **not** existence of `phi`: `rho_inf`-fixedness
is the product of the local relations only (§7 R1). Nothing here asserts that a
Keller map exists, and nothing here asserts a curve is non-realizable.

**OPENs raised or sharpened.**

* `OPEN[REP-96-BM-FACTORISATION]` — compute the eight tangency transports of the
  realized `(9,6,2)` curve and intersect the nine local fixed sets against the six
  pinned classes of §5. Finite and decidable. Highest value in the campaign right
  now: it either yields the first explicit `phi` or kills the row.
* `OPEN[REP-96-SOURCE-IS-C2]` — the Riemann-existence source-identification step.
* `OPEN[REP-96-MPRIME-COMPANION]` — pin `D_2`; `(M')` binds only through `(7.1)`.
* `OPEN[SHAPE-2-INNER-MULTIPAIR]` — CABLE-3's rigidity uses a single
  characteristic pair at infinity; family 2 at `g >= 3` with two or more pairs is
  untouched.
* `OPEN[TB-FAMILY-2]` — no promoted family-2 analogue of THEOREM TB exists.
* `OPEN[SHAPE-2-INNER-g>=3]` is **narrowed, not closed**: GATE-3 settles the
  `d' = 3` sub-family with one pair at infinity (it kills half the residues), and
  in particular decides both `(9,6)` types; `d' >= 5` odd and `g >= 4` remain.

**Deviations from the charge, logged.**

1. The charge anticipated that GATE-3 might kill a type. It does not: both live
   `(9,6)` types satisfy it. The gate is non-vacuous — `gcd(k_*,6) = 1` is fatal —
   but the two admissible `c` values on this row, `2` and `4`, are both even, so
   the gate is **non-binding on the `(9,6)` row while being binding in general.**
   That is reported as found rather than strengthened to fit.
2. The charge lists the `(M')` identity among the residual constraints. I found
   it inapplicable in its promoted `(H2)` form and computed its block-free form
   explicitly; the outcome `(7.1)` is a constraint on the companion component and
   is blind to `delta_aff(D_1)`. I record this rather than quoting `(M')` as a
   pending gate on `D_1`.
3. The charge asked for `beta_1` and `delta_inf` "recomputed from the Galindo
   conversion". I did that and, because a conversion table is exactly where a
   flag/place/series error would hide, also recomputed `beta_1` from the two
   curves by exact Puiseux expansion. Both routes agree.
4. Scripts were used (four, listed in §0). PB's lane ran two; this lane's third
   and fourth are new in kind (exact rational series; explicit curve arithmetic).
   Every conclusion is stated so that it can be re-derived by hand.
5. **Size.** The charge paced this report at 25–35 KB of body. It is about 46 KB.
   The overrun is in §§2–3 (the from-scratch derivation the charge required
   instead of a transplant), §5 (the pinned residual, which a successor lane
   consumes directly) and §7 (the fork, itemised rather than summarised). I chose
   completeness over the pacing target and log the choice rather than dropping the
   `(M')` computation or the control ledger.

## 9. FALLACY-v2 audit

* **Flag/place/series.** Four objects at `P_inf` are kept apart: the contact
  `(Dbar . L_infty)_{P_inf} = d = 9`; the multiplicity `a = 3`; the characteristic
  numerator `beta_1 in {25,23}`; the second Puiseux exponent
  `k_* = 2d-a-beta_1 in {-10,-8}`. `k_*` is derived twice (§2, §4) rather than read
  off a table. AUD's warning that the `a` conjugate series are **one** place, not
  `a` places, is honoured: the germ is one place throughout.
* **Floor/attainment.** `e(iota)` is an exact value, never a bound. `(M-INF)` and
  `(M-INF-T)` failing are sufficient criteria going silent, never `pi_1 != Z`. The
  N-A boundary coincidence at `(9,6,4)` is recorded and **not** consumed:
  `C'^2 > 2 r_1` is not relaxed to `>=`.
* **Carrier/attainment.** The §5 residual is group-theoretic data, not a witness;
  `REPRESENTATIVE` is not `FULL_ACTUAL_EXIT`. Passing GATE-3 is a necessary
  condition met, not a representation exhibited.
* **Per-ray/exit-set charge.** No exit price is asserted; no `charge_basis` line.
* **Pole/interior.** The winding is taken on `|x| = R` in the tube regime where
  `(2.1)` establishes tube disjointness, and rigidity is justified by dominance of
  the `k_*` term as `R -> infinity`, not by a pole identity off its vertex class.
* **Prime label/derivative.** `p'`, `q'` are genuine derivatives. `Pi`, `Pi_i`,
  `X = Pi_1 = Pi_3`, `Y = Pi_2` are distinct symbols, never conflated; the two
  campaign symbols `b` are separated explicitly in §7 R3.
* **Variable/ring map.** The chart at `P_inf` is declared with orders
  `(a,d) = (3,9)`; the Hurwitz convention is the promoted left action, permutation
  words compose right-to-left, and the block conjugator is **derived** as
  `Pi Pi_{d'}^{-1}`, then checked by the block-product round trip in §2.
* **`sat()` / raw remainder degree.** Not in play: no ideal computed, no degree
  substituted for a normal form. The one degree-like quantity `c` is taken in
  AUD's corrected sense — the degree of the **reduced** second approximate root —
  and §1 verifies `S_aff` from the semigroup, not from a raw binomial.
* **Merge-free / target index.** No `M`-descent or `nu_G` indexing is used.
* **Not filled by cap or analogy.** The family-3 gate `3 | e(iota)` was **not**
  transported: the family-2 structure was re-derived at `(3,2)`, where the block
  periodicity is `2`. Where a promoted tool does not reach — TB at family 2,
  Shirane at degree 9, INF-TRIVIAL at odd `d`, `(M')` without `(H2)` — the verdict
  is `not applicable` with the reason typed, and an `OPEN` is raised instead of an
  analogue being assumed.

**Review routing.** THEOREM CABLE-3 and GATE-3 are `PROVED-HERE, UNREVIEWED` and
flagship-shaped; they should be paired (hostile gate + independent verification)
before promotion. The verification arm's cheapest independent target is §4
Control 2 — re-derive the `(6,4)` gate `3 | e(iota)+2` from the block reduction
`h = Y X^2 Y` and confirm both `E = -5` passes and `E = -3` fails — since a
convention error in the cycle composition would surface there immediately. The
second cheapest is the rigidity step of §3, which is the one genuinely new
ingredient relative to PB.

## 10. Custody and sources

Charged inputs: hashes in §0, all three matching. Campaign documents consumed on
disk and cited by file and line or section rather than re-hashed as primary are
listed in §0. No external literature was fetched this lane; no new primary source
is claimed. Shirane is cited as Shirane, per RK §3. The Galindo–Monserrat
conversion and the delta-sequence axioms are used exactly as quoted in AUD §3;
the `(9,6,2)` and `(9,6,4)` parametrisations are AUD §6's, re-verified here. No
canonical ledger was edited and no charged file was modified.

No `charge_basis` line: this report asserts no new exit price.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `48365`.
- Body SHA-256:
  `5a2957df82245da3044925515be68cee8a10da7dd73ecda3b2aeb16434a3ffc5`.
- Frozen basis: `45e4c7bc5ae54713799f84d7b7faea5de6e18afd`.
