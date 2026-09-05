# LEMMA [DESCENT-INVARIANCE]: Moh's finite numerical necessary conditions are fixed points of Prop 6.3 descent

Lane `descent-invariance-lemma-opus5-20260905`; adapter opus. Thirteen page renders and two check
scripts in `box/descent-invariance-lemma-20260905/` (`handcheck.py|.out`, `handcheck-empty.out`,
`rostercheck.py|.out`). Basis `a780424de740396c064ce0cc6d388731108651dc`. No ledger edit, no
`jc2-lean`, no `ideation-*`, no Groebner, no `sat()`.

## 0. Verdict first

```text
LEMMA [DESCENT-INVARIANCE] (Sec. 3) is PROVED on hypotheses (H0)-(H5): every identity --
(I1) lattice, (I2) radius, (I3) bottom V, (I4) stabilizer, (I5) ODE degrees, (I6) second-
descent exponent -- is derived from the print in Sec. 4, the charged replay being an
independent count and never a step.  Two clauses fall short of the OPEN as posed and are
typed, not papered over: at s>=4 the replayed A'_1 = A_1^act is NOT proved (only
A'_1 | den(b_j delta_1) is; new OPEN), and P'=P, Q'=Q is claimed on the copied range only,
the ratio P'/Q' = P/Q holding at every level.  New here: the (SD) kill cell {l''<0, simple,
minor, delta'_s'=-1} is CONTRADICTORY, not merely census-empty -- it forces lo' = 1 = P'/Q',
which the child's own level-s' ODE bans.  COROLLARY (Sec. 6): the transported child passes
every finite numerical condition Moh prints whenever the parent passes its own; survival is
existential, so ONE surviving alternative suffices.  KILLS ADDED: 0.  Residual 65.
```

No new exit-price assertion is made, so no `charge_basis` line is licensed.

## 1. Custody

Manifest built with `awk` from the paired `charged_input_<i>_basename=` / `_sha256=` lines of the
`.run.v2` receipt, then `sha256sum -c` against `/tmp/jc2-lane.BXFIn8/inputs`: **6/6 `OK`**, no digest
retyped; `box/lib/descend_own.py` carries the same digest. Moh pages re-rendered at 140 dpi from the
charged PDF (printed page = PDF ordinal + 139); every quotation is read off an image.

## 2. Setting and hypotheses

**p.150** fixes `d_1 = n`, `d_{j+1} = g.c.d.(n,M_1,...,M_j)`, `M_j = min{i : f_i(x) != 0, d_j /| i}`,
`q_j = M_j-M_{j-1}`, `lambda_j = sum_{i<=j}q_i d_i`, `mu_j = lambda_j/d_j`. **Def 5.1** (p.179) gives
a hypothetical tower integers `V_i` with `V_{i+1}d_i/d_{i+1} >= V_i > d_i/(n-M_i)`, `V_{s+1} = d_{s+1}`
(clause 2), Prop 4.6 at every level with `v = V_{i+1}(d_i/d_{i+1})` (clause 4), and the radius
`delta_i = 1 - (n-M_i)prod_{k>i}[V_k(n-M_k)-d_k] / {(n-M_s-1)prod_{k>i}[V_k(n-M_{k-1})-d_k]}`
(clause 3). Write `P_i := V_{i+1}d_i/d_{i+1} = deg p`, `Q_i := V_{i+1}(n-M_i)/d_{i+1} = deg q`
(p.170), `lo_i := d_i/(n-M_i) = P_i/Q_i` (the p.190 major/minor threshold), `N := (n/d_2)V_2`,
`M := (m/d_2)V_2` (p.188). **p.201 (8)**: `L = lcm{den delta_i : i >= r}`,
`A_{r-1} = den(L delta_{r-1})`; **(12)/(13)**: `A_1 | N` and `A_1 | M-1`, or `n, m` swapped.

* **(H0) Normalized reduced source.** `M_s = n-2`, `delta_s = -1`, `0 < delta_1 < 1`, strict radius
  tower, `d_s >= 4`. By Prop 5.6 (p.188) with its p.190 deduction, a reduced counterexample's `D_1`
  is **nonzero-centred**.
* **(H1) Licensed descendant.** Prop 6.3 (p.197): `delta_s = -1` and `D*_{s-1}` has logarithmic
  radius `>= v_s/u_s`, `u_s := d_s-v_s`, `v_s := V_s`. At `u_s = 1` this is Prop 6.4 (p.198),
  unconditional; at `u_s >= 2` it is supplied (`OPEN[PROP6.3-RADIUS-US>1]`).
* **(H2) Jacobian exponent.** `ell := v_s-u_s-1 = 2v_s-d_s-1 >= 0`; by Prop 6.3(3) the child has
  `J_{gamma,pi} = -(u_s/b)gamma^ell`, so Prop 4.6 applies to it in the **p.171 Remark**'s form:
  "*with a verbatim proof, for … `J_{x,y}(f,g) = x^l` Proposition 4.6 is still valid with the
  condition (3) replaced by* (3)*: `lambda = (-1-l+delta)/(n-m_r) < (-1-l+delta)/(n-m_i)`".
* **(H3) Child radii** `:= (ell+1)` x Def 5.1(3) on the child datum — not a choice: Sec. 4.2
  reproduces all five of Moh's printed p.207 child radii with it.
* **(H4) Own-data route (recipe input, declared).** `V'_i = V_i` for `i <= j`; `V'_i = W_i` for
  `i > j`, `W_s = u_s`, `W_i = (d_i/d_{i+1})W_{i+1} - delta_i(P_i-V_i)`. The `W` recursion and the
  Mobius law at `i >= j` are two forms of one statement, their equivalence *checked* 66/66
  (`rostercheck.out`), not assumed twice.
* **(H5) Definedness.** With an empty own-`V` route set there is no licensed child tower: `A'_1`,
  `P'_i`, `Q'_i` are **undefined**; (I1), (I3), the (I5) threshold and (I6) stay defined (lattice and
  level-2 identity only). Undefined is not failure.

## 3. Statement

> **LEMMA [DESCENT-INVARIANCE].** Let a parent satisfy (H0)-(H2) and let the child be its Prop 6.3
> descendant with `c = u_s/d_s`, `s' = s-1` (less one if `M'_{s-1} = n'-1` is dropped by the p.174
> Definition-Remark) and the (H4) route. Then, with `delta_j = a_j/b_j` and `g = gcd(a_j,u_s)`:
>
> **(I1)** `n' = cn`, `m' = cm`, `M'_i = cM_i`, `d'_i = cd_i`, `mu'_i = c mu_i` (`i <= s-1`), so
> `n'/d'_2 = n/d_2` and `m'/d'_2 = m/d_2`. **(I2)** `delta'_i = (v_s-u_s)-(u_s/delta_j)(1-delta_i)`
> for `i <= j`, agreeing at `i = j` with `delta'_j = v_s-u_s/delta_j`. **(I3)** `V'_2 = V_2`, hence
> `N' = N` and `M' = M`, at every `u_s`. **(I4)** `A'_1 = den(L''(u_s/g)b_j delta_1)`; at `s = 3` this
> is `A_1` exactly when `u_s = 1` and a divisor of `A_1` when `u_s >= 2`, and at `s >= 4` it divides
> `den(b_j delta_1)`. **(I5)** `P'_i/Q'_i = P_i/Q_i` at every level `i < s`, and `P'_i = P_i`,
> `Q'_i = Q_i` exactly on the copied range `i+1 <= j`; `lo' = lo_{s-1}`. **(I6)**
> `l'' = u_s d_{s-1}/d_s - d_s + 2u_s - 2`, `= d_{s-1}/d_s - d_s` at `u_s = 1`; and
> `delta'_{s'} = -1` iff `n-M_{s-1} = d_s(d_s-1)`.

## 4. Proof

### 4.1 (I1) The lattice is transported by one scalar

Prop 6.3(2) (p.197, verbatim): `gbar(sigma), Tbar_1^psi(sigma), ..., Tbar_{s-1}^psi(sigma)` *are monic
in `pi` with `pi`-degree* `u_s n/d_s, u_s(-mu_1)/d_s, ..., u_s(-mu_{s-1})/d_s`. So `n' = cn`,
`mu'_i = c mu_i` (`i <= s-1`), `m' = -M'_1 = cm`. By p.201 (5), `d_s = gcd{n,M_1,...,M_{s-1}}`, so with
`n = d_s nhat`, `M_i = d_s Mhat_i` the scaled data are the integers `u_s nhat, u_s Mhat_i` and
`gcd(u_s nhat, u_s Mhat_1, ...) = u_s gcd(nhat, Mhat_.) = c d_i`: **`d'_i = c d_i`** (`i <= s`),
`d'_s = u_s`. The p.150 recurrence `mu_i = (d_{i-1}/d_i)mu_{i-1} + M_i - M_{i-1}` (from
`mu_i = lambda_i/d_i`, `lambda_i = lambda_{i-1}+q_i d_i`) determines `M` from `mu` and the `d`-ratios
and is homogeneous of degree 1 in `(M,mu)` at fixed ratios; `mu'` and `d'` being `c`-scaled,
`M'_i = c M_i`. (Cross-check: `child-top-us2` Sec. 2.2 proves `M'_i` is the parent's *x*-side p.150
datum; 8/8 there, 46/46 roster.) Hence `n'/d'_2 = n/d_2`, `m'/d'_2 = m/d_2`.  **(I1\*)**

### 4.2 (I2) Radius transport, from Def 5.1(3)

Put `F_i := (n-M_i)prod_{k>i}[V_k(n-M_k)-d_k] / {(n-M_s-1)prod_{k>i}[V_k(n-M_{k-1})-d_k]}`, so
`delta_i = 1-F_i`; `F'_i` is the same on the child datum (`s -> s'`), so
`delta'_i = (ell+1)(1-F'_i)` by (H3).

**(a)** `F_{i-1}/F_i = [(n-M_{i-1})/(n-M_i)]*[V_i(n-M_i)-d_i]/[V_i(n-M_{i-1})-d_i]` is a function of
level `i` alone. On `i <= j` the child has `V'_i = V_i` and, by (I1),
`V_i(n'-M'_i)-d'_i = c[V_i(n-M_i)-d_i]` and `(n'-M'_{i-1})/(n'-M'_i) = (n-M_{i-1})/(n-M_i)`; the `c`
cancels between the two factors, so `F'_{i-1}/F'_i = F_{i-1}/F_i` for `i <= j` and hence
**`F'_i = rho F_i`** there for one constant `rho`. Thus `delta'_i = (ell+1)(1-rho(1-delta_i))` is
affine in `delta_i` with fixed point `delta_i = 1 |-> ell+1 = v_s-u_s`.

**(b)** Imposing `delta'_j = v_s-u_s/delta_j` and using `2v_s-d_s = v_s-u_s = ell+1`, subtraction of
`v_s` gives `(ell+1)rho(1-delta_j) = u_s(1-delta_j)/delta_j`; `delta_j != 1`, so
`(ell+1)rho = u_s/delta_j` and `delta'_i = (v_s-u_s)-(u_s/delta_j)(1-delta_i)` for `i <= j`.

**(c) `j = s-1`: the Mobius value is itself proved.** With `n-M_s = 2`, `n-M_s-1 = 1` (H0) and
`X := n-M_{s-1}`, Def 5.1(3) at `i = s-1` reads
`delta_{s-1} = 1-X(2v_s-d_s)/(v_sX-d_s) = (u_sX-d_s)/(v_sX-d_s)`. The same telescoping run across the
deleted level `s` gives `F'_i = kappa F_i` (`i <= s-1`) with
`kappa = u_s(v_sX-d_s)/[(ell+1)(u_sX-d_s)] = u_s/[(ell+1)delta_{s-1}]`; at `i = s-1` it returns
`F'_{s-1} = cX/(cX-1)`, the child's own empty-product value, so nothing is assumed. Then
`(ell+1)kappa = u_s/delta_{s-1}`, and `i = j = s-1` in the affine law yields
`delta'_{s-1} = (v_s-u_s)-u_s/delta_{s-1}+u_s = v_s-u_s/delta_{s-1}`. **No recipe input here.** For
`j < s-1` the Mobius value at `i = j` is (H4), and (b) delivers the rest.

**Print control (pins (H3), and (I1), (I3) with it).** `(ell+1)` x Def 5.1(3) on the child data of
Moh's three descended p.207 rows, with `V'_2 = V_2`, gives
`(delta'_1,delta'_2) = (1/4,-1), (7/6,-1/2), (1/3,-1), (4/3,-1), (1/2,-1)` for the children
`(16,12,13;3), (21,14,16;2), (21,14,18;5), (15,10,11;2), (15,10,11;3)` — **exactly** the five values
Moh prints, main and bracketed. First by hand: `i=2`, `1-3/2 = -1/2`; `i=1`, `9-4 = 5`, `84-4 = 80`,
`1-28*5/(2*80) = 1/8`; times `ell+1 = 2`. The same table carries `M'_2 = 13,16,18,11,11 = cM_2`,
`(n',m') = c(n,m)` (**Moh's own table is (I1)**) and `V'_2 = 3,2,5,2,3 = V_2` (that is (I3)): 5/5.

### 4.3 (I3) `V'_2 = V_2`, hence `N' = N`, `M' = M`

`j >= 2` always (the route scan runs `i = s-1, ..., 2`) and `V'_i = V_i` for `i <= j` by (H4), so
`V'_2 = V_2` on every route. Its content is (H0): `D_1` is nonzero-centred, and inversion carries a
nonzero-centred selected disc over with its multiplicity (`descend_own.level2_identity`, "invert its
selected nonzero-centred D1"; `inverse_top`, "one source `b`-orbit produces a child coefficient disc
for each of `a` inverse coefficients" at unchanged `r`). With (I1\*), `N' = (n'/d'_2)V'_2 = N` and
`M' = M`; nothing uses `u_s = 1`, and it holds at `u_s >= 2` too (replay 310/310). *Declared recipe
rule with a 5/5 print control, not a root count: the child's roots are the minor cluster re-expanded,
disjoint from `D_{s-1}`.*

### 4.4 (I4) The bottom stabilizer

Let `delta_j = a_j/b_j` in lowest terms (`delta_j > 0` at a nonzero-centred level), `g = gcd(a_j,u_s)`.
By (I2) `den(delta'_i) = a_i/gcd(a_i,u_s)` for `i >= j`, so `L' := lcm{den delta'_i : 2 <= i <= s'}` is
divisible by `a_j/g`; write `L' = (a_j/g)L''`, `L'' in Z`. Since
`delta'_1 = (v_s-u_s)-(u_s b_j/a_j)(1-delta_1)` and `L'(u_s b_j/a_j) = L''(u_s/g)b_j` is an integer,
and subtracting integers does not move a denominator,
`A'_1 = den(L' delta'_1) = den(L''(u_s/g)b_j delta_1)`.

*`s = 3`.* Then `j = 2 = s-1` and `L' = den(delta'_2) = a_2/g`, so `L'' = 1`; and `L = b_2`, since
`delta_3 = delta_s = -1` contributes denominator 1. So `A'_1 = den((u_s/g)b_2 delta_1)` against
`A_1 = den(b_2 delta_1)`: **`A'_1 = A_1` exactly at `u_s = 1`** (`g = 1`), and `A'_1 | A_1` at
`u_s >= 2`, multiplication by the integer `u_s/g` only shedding denominator. At `s = 3` Moh-(8) and the
actual stabilizer coincide, the only accumulated level being `j` itself.

*`s >= 4`.* `A'_1 | den((u_s/g)b_j delta_1) | den(b_j delta_1)`, and `b_j | L` gives
`A_1^{moh} = den(L delta_1) | den(b_j delta_1)` too: both divide one quantity, neither divides the
other in general. `rostercheck.out`: `A'_1 | A_1^{moh}` on 64/66, exceptions **R026, R028**
(`A'_1 = 3,2` vs `A_1^{moh} = 1`) — the two rows the charged replay lists with `A'_1 = A_1^{act}`.
**`A'_1 = A_1^{act}` is NOT proved here**: `A_1^{act}` is defined by the `own_v_routes` witness,
outside the charged inputs. R022, R034, R039, R047 (`s = 4`, `j = s-1`) show `L'' > 1` occurs, so the
`s = 3` closed form does not extend verbatim.

### 4.5 (I5) The ODE degrees

By (I1), `P'_i = V'_{i+1}d_i/d_{i+1}` and `Q'_i = V'_{i+1}(n-M_i)/d_{i+1}`. So the **ratio**
`P'_i/Q'_i = d'_i/(n'-M'_i) = P_i/Q_i` holds at every level `i < s` with no condition on `V'`
(156/156 roster; 1,420/1,420 replay), while `P'_i = P_i, Q'_i = Q_i` **iff `V'_{i+1} = V_{i+1}`**, i.e.
exactly on the copied range `i+1 <= j` — the claimed scope; the replay's Sec. 5(c) exhibits 8 rows
where an overlapping index carries `V'_{i+1} = W_{i+1}`, the degrees differing though the ratio does
not. At the top, `lo' = lo_{s-1}`. Since Prop 4.6(3),(4),(5) and the A.3/A.4 conclusions constrain
`p, q` only through `P, Q` and multiplicities, and the p.171 Remark validates them verbatim for the
child's `J = gamma^ell` under (3)*, the child's Galois/ODE constraints at a copied level are the
parent's on the same integers.

### 4.6 (I6) The second-descent exponent, and why its window is contradictory

A second descent at a point of the child's top form of multiplicity `u`, `v' = d'_{s'}-u`, substitutes
`gamma = (gamma'^{-u}-e'-A'(gamma')-pi'gamma'^{v'})/b'`; the p.198 chain rule applied to the child
gives `J_{gamma',pi'} = c' gamma'^{(v'-u-1)-u l}(1-e'gamma'^u-A'(gamma')gamma'^u-pi'gamma'^{u+v'})^l`,
`l = ell`. The last factor has constant term 1, so polynomiality forces `l'' := (v'-u-1)-u l >= 0`. At
a **simple** point `l'' = d'_{s'}-3-ell`; with `d'_{s'} = c d_{s-1}`, `ell = d_s-2u_s-1`,
`l'' = u_s d_{s-1}/d_s - d_s + 2u_s - 2`, which at `u_s = 1` is `d_{s-1}/d_s - d_s`.

*The child's Prop 6.3 hypothesis is a lattice condition.* From 4.2(c),
`delta_{s-1} = (u_sX-d_s)/(v_sX-d_s)`, `X = n-M_{s-1}`; at `u_s = 1`,
`delta'_{s-1} = (d_s-1)-[(d_s-1)X-d_s]/(X-d_s)`, and `= -1` gives `d_s(X-d_s) = (d_s-1)X-d_s`, i.e.
**`delta'_{s'} = -1 <=> n-M_{s-1} = d_s(d_s-1)`**.

*The window is contradictory.* Assume `delta'_{s'} = -1`, `l'' < 0`, the point simple and MINOR, and
write `d_{s-1} = w d_s` (`d_s | d_{s-1}`, `w >= 2`). `l'' < 0` gives `w < d_s`; minority at a simple
point is `1 <= lo' = d_{s-1}/(n-M_{s-1}) = w/(d_s-1)` (p.190: minor iff the multiplicity is
`<= d_r/(n-M_r)`), i.e. `w >= d_s-1`. Hence `w = d_s-1` and `lo' = 1` exactly. Now the child's own
level-`s'` ODE: p.171's simplified equation with Prop 4.6(2) reduces to `P p q' - Q p' q = c p`,
`c != 0` (`P = P'_{s'}`, `Q = Q'_{s'}`; the degree-`P+Q-1` terms cancel, so it is degree-consistent).
Let `a` be a root of `p` of multiplicity `v`; all roots of `p` are roots of `q` (Prop 4.6(4)), so
`p = (pi-a)^v h`, `q = (pi-a)^{w0}G`, `h(a), G(a) != 0`, `w0 >= 1`, and

```text
   P p q' - Q p' q = (pi-a)^{v+w0-1}{ P h[w0 G + (pi-a)G'] - Q[v h + (pi-a)h']G } = c(pi-a)^v h .
```

`w0 > 1` forces the left order `> v`, hence `c = 0`; so `w0 = 1` (this *is* Prop 4.6(3)), and at
`pi = a`, `G(a)(P-Qv) = c != 0`, i.e. **`v != P/Q`**. By (I5) `P'_{s'}/Q'_{s'} = lo' = 1`, so the
child's top form has **no** simple root at all, zero-centred or not. The four hypotheses are jointly
contradictory: the (SD) kill window is empty for **every** parent satisfying (H0)-(H2), not merely on
the census (where the charged replay measures 0/24,063). At `u >= 2` the same chain rule gives
`l'' = d'_{s'}-2u-1-u*ell >= 0`, but the second descent then needs the child's minor radius `>= v'/u`,
its split window: `OPEN[SD-HEAVY-POINT-CONDITIONAL]`, retained.

## 5. Verification

### 5.1 The six p.207-type controls, by hand (`handcheck.out` agrees exactly)

All six have `s = 3`, `j = 2`, so `A_1 = den(b_2 delta_1)`, `A'_1 = den((u_s/g)b_2 delta_1)`.

| row | `(n,m)` `V`; `delta` | `u_s,ell` | `N,M ; A_1` | child `(n',m',M'_2)`,`V'_2`; `delta'` | `N',M' ; A'_1` | `l''` |
|---|---|---|---|---|---|---|
| R004 | (64,48) `(3,3)`; `9/16,1/4,-1` | `1,1` | `12,9 ; 4` | `(16,12,13)`,`3`; `1/4,-1` | `12,9 ; 4` | `16/4-4=0` |
| R001 | (84,56) `(2,3)`; `16/21,2/7,-1` | `1,1` | `6,4 ; 3` | `(21,14,16)`,`2`; `7/6,-1/2` | `6,4 ; 3` | `28/4-4=3` |
| R007 | (84,56) `(5,3)`; `7/12,1/4,-1` | `1,1` | `15,10 ; 3` | `(21,14,18)`,`5`; `1/3,-1` | `15,10 ; 3` | `3` |
| R002 | (75,50) `(2,4)`; `2/3,1/5,-1` | `1,2` | `6,4 ; 3` | `(15,10,11)`,`2`; `4/3,-1` | `6,4 ; 3` | `25/5-5=0` |
| R003 | (75,50) `(3,4)`; `1/2,1/5,-1` | `1,2` | `9,6 ; 2` | `(15,10,11)`,`3`; `1/2,-1` | `9,6 ; 2` | `0` |
| R015 | (99,66) `(8,8)`; `4/9,1/3,-1` | `3,4` | `24,16 ; 3` | `(27,18,21)`,`8`; `0,-1` | `24,16 ; 1` | `2` |

Bottom tests: R004 `4|12, 4|8` (12); R001 and R002 `3|6, 3|3` (12); R007 `3|15, 3|9` (12); R003
`2|6, 2|8` (13); R015 parent `3|24, 3|15` (12), child vacuous at `A'_1 = 1`. **R001** by hand:
`b_2 = 7`, `A_1 = den(7*16/21) = den(16/3) = 3`; child `L' = den(-1/2) = 2 = a_2`,
`A'_1 = den(2*7/6) = 3 = den(7*16/21)`; `n'/d'_2 = 21/7 = 3 = 84/28`, `m'/d'_2 = 2 = 56/28`, so
`N' = 6 = N`, `M' = 4 = M`; `l'' = d'_2-3-ell = 3 = 28/4-4`; `lo' = 7/5 = 28/20`. **R015 (`u_s = 3`)**:
`a_2 = 1`, `b_2 = 3`, `g = 1`, so `A'_1 = den(3*3*4/9) = 1` against `A_1 = 3` — divisibility only,
equality false, exactly the replay's Sec. 5(b) row `99 66 3 (8,8)`. **R004** has `delta'_{s'} = -1`
with `n-M_2 = 12 = 4*3`, Sec. 4.6's equivalence live, but `l'' = 0`.

### 5.2 Three random operative rows

Drawn from the 1,420 operative keys of `box/child-own-v-20260905/enumerated-source-rows.json` by
`random.Random(20260905).sample(range(1420), 3)` = indices `1202, 553, 171`; seed declared before the
draw, nothing redrawn. All three came out `u_s = 1` with an **empty** own-`V` route
(`EMPTY_NECESSARY_FIRST_SUPPORT`, the 1,354-row majority), so per (H5) `A'_1, P'_i, Q'_i` are undefined
there; the `u_s >= 2` divisibility branch is exercised by control R015 instead.

| idx | `(n,m)` `s`; `u_s,ell` | `n'/d'_2, m'/d'_2` | `V'_2` | `N', M'` | `l''` | `delta'_{s'}=-1?` | `lo_{s-1}` |
|---|---|---|---|---|---|---|---|
| 1202 | (192,128) `6`; `1,1` | `3=3, 2=2` | `1` | `3, 2` | `8/4-4=-2` | `20 != 12` no | `2/5` |
| 553 | (180,120) `5`; `1,2` | `3=3, 2=2` | `5` | `15, 10` | `10/5-5=-3` | `65 != 20` no | `2/13` |
| 171 | (144,96) `5`; `1,1` | `3=3, 2=2` | `2` | `6, 4` | `8/4-4=-2` | `52 != 12` no | `2/13` |

By hand on **171** (`M = (-96,-24,16,92,142)`, `d = (144,48,24,8,4,2)`): `c = 1/4` gives `n' = 36`,
`m' = 24`, `M' = (-24,-6,4,23)`, `d' = (36,12,6,2,1)` — each `c` times the parent's; `n'/d'_2 = 3 =
144/48`; `V'_2 = V_2 = 2`, so `N' = 6 = N`, `M' = 4 = M`. Thresholds
`d'_i/(n'-M'_i) = 3/5, 2/7, 3/16, 2/13` equal the parent's `144/240, 48/168, 24/128, 8/52` level by
level (I5), and `l'' = d_4/d_5-d_5 = -2 < 0`. All three drawn rows sit in the `l'' < 0` half and all
three are excluded by **two** independent clauses of Sec. 4.6 — `n-M_{s-1} != d_s(d_s-1)`, and
`lo_{s-1} < 1` so a simple point is MAJOR and (SD) does not apply. Mechanism, not luck:
`lo_{s-1} >= 1` with `l'' < 0` pins `w = d_s-1`, which forces `X = d_s(d_s-1)`.

*Scope replay (evidence, not a step).* `rostercheck.out`, 66 roster rows, every licensed route:
Mobius 66/0, affine 66/0, `(ell+1)Def 5.1(3) = metric` 66/0, `N'=N, M'=M` 66/0, threshold transport
156/0, copied `P,Q` 66/0, `lo' = lo_{s-1}` 66/0, `l''` 66/0; `A'_1` closed form 62/4 and
`A'_1 | A_1^{moh}` 64/2, both exception sets typed in Sec. 4.4.

## 6. Corollary, and what is not covered

> **COROLLARY.** Under (H0)-(H2) the transported child datum satisfies every finite numerical necessary
> condition Moh prints for the child — (W) Def 5.1(2), (GO) the p.201 (8)-(11) pattern with Prop 4.6/A.3
> at every level, (B) the (12)/(13) bottom test, (SD) `l'' >= 0` — whenever the parent satisfies its
> own. Hence no second arithmetic generation removes a row the first retains.

*Why one alternative suffices.* A row dies only if **every** admissible child tower fails; the lemma
exhibits one that does not. (W) at copied levels is the parent's Def 5.1(2) rescaled by `c` (I1); (GO)
at copied levels constrains the same `P_i, Q_i` (I5) under the p.171 licence (H2); (B) is the parent's
(12)/(13) on the same `N, M` (I3) at modulus `A'_1` (I4); (SD)'s window is contradictory (I6).

*NOT covered.* (1) **Chart-level conditions** — the `G_i` receiver (199-4,889 unknowns) is no condition
on `(n,M,d,V,delta)`; the lemma re-prices avenue (a) onto the chart and bounds nothing there. (2) **The
source-support envelope** — outer-radius constant `d = -delta_s`, descendant support cap, `ES` leaves.
(3) **Xu Thm 5.1 with exact contact** — `IM/Im` margins come from the skeleton, not the child datum;
R009/R050 stay reachable by a sharper Xu. (4) **`u_s >= 2`** — (H1) is supplied, the terminal pair is
open (`OPEN[CHILD-TERMINAL-SUPPORT-US>1]`; `child-top-us2` refutes `M'_{s'+1} = n'-1` as a consequence
of the descent), the clause is `A'_1 | A_1` not equality, and the top level is untested on the 20
prefixes. (5) **`A_1^{act}` at `s >= 4`** — the OPEN below. (6) **Not a tautology** — (B)/(GO) do bite
on child data that is *not* the transported one: 21 (B) and 2 (GO) failures among 215 outer vectors of
tree-empty rows (charged structure report).

## 7. FALLACY-v2 ledger

*Flag/place/series:* no child disc is identified with a parent disc; Sec. 4.2 transports Def 5.1(3)
**values** through the lattice scaling, the only geometric input being (H4), declared — the child's
roots are the minor cluster re-expanded, disjoint from `D_{s-1}`, so `V'_2 = V_2` is a recipe rule with
a 5/5 print control, never a root count. *Floor/attainment:* every conclusion is "necessary numerics
survive", never a witness pair; `l'' >= 0` is necessary, `l'' = 0` proves nothing. *Pole/interior:*
(SD) is applied only after checking the p.190 vertex class and Prop 6.3's `delta_s = -1`.
*Variable/ring map:* the descent is declared as `y = gamma^{-u_s}`, `x = (y-e-sigma)/b`, `sigma`
carrying `pi` at `theta^{v_s/u_s} = gamma^{v_s}`, its Jacobian computed as
`-(dx/dpi)(dy/dgamma) = -(u_s/b)gamma^{v_s-u_s-1}`, matching p.197 (3). **Print defect recorded:**
p.198's display `-u_s/(b gamma^{v_s-u_s-1})` and its matrix entry `-1/(b gamma^{v_s})` are not mutually
consistent; p.197 (3) is what the computation gives, and `ell = v_s-u_s-1 >= 0` uses (3). *Prime
label:* `'`/`''` are generation labels; `p', q', h', G'` are Moh's `d/dpi`. *Raw remainder degree:* the
multiplicity argument branches explicitly on `w0 = 1` vs `w0 > 1` and on `c != 0`. *Merge-free:*
prefixes keep the child terminal index open, no `M'_{s'+1}` is invented. *Target/arrival index:* child
level `i` is compared with parent level `i` for `P, Q, delta`, with parent level `s-1` only for `lo'`,
`d'_{s'}`. Undefined quantities stay undefined; no `sat()`, no Groebner.

## OPENS RAISED

```text
OPEN[DESCENT-INVARIANCE-ACT-STABILIZER-S>=4]
  QUANTITY: at s >= 4, u_s = 1, is A'_1 = A_1^{act} := den(L^{act} delta_1), L^{act} the lcm of
    den(delta_i) over levels i >= 2 whose SELECTED disc is nonzero-centred?  Proved instead:
    A'_1 = den(L''(u_s/g) b_j delta_1), hence A'_1 | den(b_j delta_1).
  STATUS: replayed 46/46 (charged grok46); the s=3 closed form holds 62/66 on the roster; A_1^{act}
    is defined in box/lib/own_v_routes.py, outside the charged print set.
  CHEAPEST TEST: prove a zero-centred selected level contributes no denominator to the bottom
    stabilizer, from p.201 (8)-(11) and the tbar -> omega tbar automorphism; ~1 lane.
  BLAST RADIUS: none on counts; upgrades (I4) at s >= 4 from divisibility to equality.
```

## OPENS RETAINED

```text
OPEN[SECOND-GEN-NUMERICS-DESCENT-INVARIANT] -- PROMOTABLE in the Sec. 3 form (I1)-(I6) plus the
  Sec. 6 corollary, EXCEPT its A_1^{act} clause at s >= 4, which splits off above.
OPEN[SD-HEAVY-POINT-CONDITIONAL], OPEN[PROP6.3-RADIUS-US>1], OPEN[CHILD-TERMINAL-SUPPORT-US>1],
OPEN[CTOP-EXTRA-CONDITION-E], OPEN[PROP42-ELL-CONDITION3] -- unchanged; (H1) and (H2) consume the
  last of these exactly as the source-support closeout does.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `23262`.
- Body SHA-256:
  `416e2fd9b714739e2f9a580a76ece649393e01ac2e1acfa7c474dbf9775961be`.
- Frozen basis: `a780424de740396c064ce0cc6d388731108651dc`.
