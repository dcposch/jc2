# Hostile reconstruction of the complete `e=3,m=1` G0--G9 ramified rank fan

Reviewer: Opus 5 (different-model hostile reconstruction)
Date: 2026-08-29
Frozen campaign basis: `0f7ee003be45ee40d51d4048897cdacf63821172`
Reviewed packet: `xmodel/k00-ram-e3m1-g0-g9-complete-rankfan-sol56-20260829.md`

## Verdict

**CONFIRM_WITH_CORRECTIONS.**

Every mathematical claim in the packet -- the surface identity, the whole
rank fan, both G8 cokernel forms, the G8 normal form, `G9_6`, the fresh
`n=4` cone, both `n=4` terminals, and the banked fixture -- reproduced
**literally and exactly** in a clean-room rebuild that did not read the
producer replay's algebra. Several claims came out *stronger* than stated.
The corrections are custody labelling, two check-side "mutations" mislabelled
as negative controls, one unnamed branch in the exhaustiveness enumeration,
one unstated reason why the imported G0--G3 premise transfers across `e`, and
one over-retention statement. None changes the endpoint.

No exit-price assertion is made in this review, so no `charge_basis` line is
declared.

### Itemized verdicts

| # | item | verdict |
|---|---|---|
| 1a | source custody: 3 declared digests, 9 charged sources, canonical tails pin | CONFIRM_WITH_CORRECTIONS (C1) |
| 1b | normalization: `C6=1`, coordinate map, seven rows from 569 tails | CONFIRM |
| 1c | surface identity (2.1) `R_r(D(S,T))==0` | CONFIRM |
| 1d | exact `e=3,m=1` calendar G20/G32/G43/G49/G55/G57 and (1.1) | CONFIRM |
| 1e | `C6` / `k10[0]` / `Jdet[0]` opens | CONFIRM_WITH_CORRECTIONS (C6) |
| 1f | every positive/infinite boundary load face has identical G0--G9 | CONFIRM |
| 2a | `G(2n)=Q`, same quadrics at `n=2,3,4` (2.3) | CONFIRM (strengthened) |
| 2b | reduced support = 4-plane, `sqrt(Q)=(A,B)` (2.4) | CONFIRM |
| 2c | `C`, `E`, both determinant identities (2.6)--(2.7) | CONFIRM |
| 2d | rank stratification 2/1/0 by `Delta` | CONFIRM |
| 2e | rank-one charts and the same-`epsilon` coupling (2.8) | CONFIRM (derived, not assumed) |
| 2f | rank-zero recentering is a reparameterization | CONFIRM |
| 2g | imported G0--G3 leading plane | CONFIRM_WITH_CORRECTIONS (C1, C5); re-derived |
| 2h | `n=2` fan: rank 2 dead G5, rank 1 dead G6 (3.1), rank 0 recenters | CONFIRM |
| 2i | exhaustiveness of the whole tree incl. `n>=5` | CONFIRM_WITH_CORRECTIONS (C4) |
| 3a | `n=3` G8 cokernel forms (4.2)--(4.4) | CONFIRM |
| 3b | localized pair and reduced support (4.5)--(4.6) | CONFIRM |
| 3c | G8 normal form `H` and the kernel basis (4.7) | CONFIRM |
| 3d | `G9_6 = eps*i*q^3/32` (4.8) with `S3,T3,N6,k10[0..3]` retained | CONFIRM (strengthened) |
| 3e | banked fixture (4.9): 63 zeros then `i/32` | CONFIRM |
| 4a | fresh `n=4` G8 cone, all three ranks G8-compatible | CONFIRM |
| 4b | (5.1) decomposition incl. the cubic middle term | CONFIRM |
| 4c | `n=4` rank two dead at G9 with the K10 term included | CONFIRM |
| 4d | `n=4` rank one terminal (5.2) `-eps*5i*k0*t^3/16` | CONFIRM |
| 4e | `n=4` rank zero cubics (5.3) and their common-zero argument | CONFIRM |
| 4f | `ord(N)>4` subbranch | CONFIRM_WITH_CORRECTIONS (C4) |
| 4g | localization and algebraic-closure case splits | CONFIRM |
| 5a | old fixture pass/fail control | CONFIRM |
| 5b | `SURFACE_-4_TO_-3` control | CONFIRM (genuine input mutation) |
| 5c | `DELTA_64` control | CONFIRM_WITH_CORRECTIONS (C2: check, not mutation) |
| 5d | `W2_192` control | CONFIRM_WITH_CORRECTIONS (C2: unreachable branch) |
| 5e | `K10_OPEN` control | CONFIRM (independently reproduced from the source) |
| 5f | source/tail mutation in the packet | OPEN in the packet; supplied here (§6.2) |
| 6a | field-valued vs scheme-valued language | CONFIRM |
| 6b | radical and rank splits | CONFIRM |
| 6c | imported G3 scope | CONFIRM_WITH_CORRECTIONS (C5) |
| 6d | finite jets vs formal cells | CONFIRM_WITH_CORRECTIONS (C7, understated) |
| 6e | nonclaims register | CONFIRM |

Nothing is REFUTED.

## 0. Custody

All three declared digests reproduce byte-exactly:

```text
full        22e9752761f3bb4ee94b4dccf18cb72ff49bd0d92453ad4cf39eb401cc45f84a  OK
body 13038  2e3086f577cc4e0b228cfe55df92413ca749e0b3230ddb71208735b49809bc8e  OK
replay      bcd4004e671091c7d1ffc265affbd160b1d2b2a712f62dd97b698150dfc9fcba  OK
```

The body definition (every byte through the terminating newline of the unique
standalone BODY-END marker line) is honoured; the seal is outside the body.

All nine charged source hashes in packet §1 resolve to files present at this
basis (hashed the whole tree, 15,569 candidates, unique matches). One label
is wrong -- see **C1**. Two independent extra pins that the packet does not
claim but that I checked:

* the canonical (`sort_keys`, tight separators) re-serialisation of
  `tails.json` hashes to `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`,
  exactly the compiler's own `EXPECTED_CANONICAL_TAILS` pin;
* the engine is imported through `importlib` from
  `xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py`, which **does** carry
  an `if __name__ == "__main__"` guard, so `exec_module` runs no side effects.
  (This is the failure mode recorded for a different probe in the campaign;
  it is not present here.)

The replay runs, and both `-B` and `-B -O` print byte-identical output
matching packet §1 verbatim, including
`CERTIFICATE_BYTES=17825` and
`CERTIFICATE_SHA256=96279f6994f3af485913d33d3f0a175c582b02da450a0b344fb82fc65f2129a0`
(11.7 s wall). Its imports are stdlib only.

## 1. Method: independent rebuild

I did not use the producer replay as an oracle. I wrote a fresh sparse
polynomial/truncated-series engine over `Q[u]/(u^2+64)` and rebuilt from
`tails.json` directly:

* 569 monomials, weight test `sum(a_i w_i)=12+ell` with
  `w=(8,7,6,5,4,3,2 | 2,6,10)`, load-linearity test, census 569 -- all pass;
* coordinate map `C=( (1+d0)/256, d1, (1+d2)/16, d3, (3+d4)/8, d5, 1 )`
  read off the charged compiler (`coordinate_images`, byte-identical to the
  runtime `k00_coordinate_series`), so `C6=1` is hard-wired, not assumed;
* seven unloaded rows `R_1..R_7` (min `d`-degrees `2,2,2,2,2,3,2`) and seven
  `K10` rows `A10_1..A10_7` (min `d`-degree 2) as exact rationals.

The single variable `u := 8*i*epsilon` with `u^2=-64` carries both the
Gaussian unit and the sign `epsilon in {+1,-1}` simultaneously; the two roots
of `u^2+64` *are* the two charts, so nothing is lost and both signs are
always computed at once. Dictionary: `eps*8i = u`, `eps*24i = 3u`,
`eps*i/32 = u/256`, `eps*(5i/16) = 5u/128`.

Total desk cost: every step under 6 CPU s, peak RSS 13 MB; two Singular calls
(radical of a 6-quadric cone in 6 variables, and one elimination in 12
variables) under 2 s each. Well inside the 60 CPU s / 1 GiB envelope. No
AWS packet was needed.

## 2. Attack 1 -- source, normalization, calendar, rows, opens, load faces

### 2.1 The surface identity (2.1) -- CONFIRM

Substituting `D(S,T)=(2S+S^2,(1+S)T/8,S+16T^2,T,S,2T)` into the rebuilt rows:

```text
R_r(D(S,T)) == 0  identically,  r = 1..7.
```

Also computed, and used later: `K10_4(D)=K6_4(D)=K2_4(D)=0` identically, and
`K10_6(D)` has `(S,T)`-order 4 while `K10_1,2,3,5,7(D)` have order 3. These
two facts are exactly what make row 4 load-free and row 6 K10-blind at G9.

### 2.2 The exact `e=3,m=1` calendar -- CONFIRM

The charged compiler carries the Lambda-grade shift table literally
(`source_columns`/`tail_dag_rows`/`direct_tail_rows`):

```text
k10:2  k6:6  k2:10  mu2:14  mu4:16  mu6:18  Jdet:19
```

Under `Lambda=tau^e` these become tau-shifts `e*` that table. With `e=3`, the
declared minimum orders of (0.1), and the min `d`-degrees I measured
(`A10`:2, `A6`:1, `A2`:1, targets: 0), the earliest possible tau-grades are

```text
K10  6 + 0 + 2 =  8      K6   18 + 1 + 1 = 20
K2  30 + 1 + 1 = 32      mu2  42 + 1      = 43
mu4 48 + 1     = 49      mu6  54 + 1      = 55      Jdet 57 + 0 = 57
```

reproducing packet §1's `G20, G32, G43, G49, G55, G57` exactly, and (1.1).
The packet's "these are lower bounds, not exact-order assumptions" is the
correct hedge.

**Stronger than claimed, and worth adding.** The K10 sector cannot in fact
reach G8 at all: `[tau^2]A10_r(d(tau)) = A10_r^{[2]}(ell(s,t))`, which is the
`(S,T)`-degree-2 part of `A10_r(D(S,T))`, and that is zero for every row.
Consequently through G8 the source is **purely unloaded**, and the *only*
load term anywhere in G0--G9 is `k10[0]` times a cubic at G9. I confirmed
this by literal variable support: `n=2` G8 support contains no `k`, `n=2` G9
support contains `k0` and no `k1,k2,k3`.

### 2.3 Seven rows, opens, and load-face uniformity -- CONFIRM

`Jdet` first appears at G57, so packet §1's "the `Jdet[0]` open labels the
cell but its equation does not enter this truncation" is exact. Every
boundary-load face -- each of `k6,k2,mu2,mu4,mu6` of any positive order or
identically zero -- yields the *same* `G0..G9`, because the earliest of them
is G20. That is the content of the packet §0 uniformity sentence and it
holds. (See **C6** for the `k10[0..3]` wording.)

## 3. Attack 2 -- the complete rank tree and its exhaustiveness

### 3.1 `G(2n)` is one fixed quadric system -- CONFIRM, strengthened

With `S,T` fully symbolic to order 8 and `N` symbolic from order `n` to 8:

```text
n=2:  G0..G3 == 0 identically,  first equations at G4
n=3:  G0..G5 == 0 identically,  first equations at G6
n=4:  G0..G7 == 0 identically,  first equations at G8
```

and in every case `G(2n)` is literally the *same* system, depending on
`N_n` **alone** -- not on any surface coefficient at all:

```text
term counts (rows 1..7):  8, 11, 9, 12, 8, 0, 6      (identical for n=2,3,4)
Q_1 = 3/1024 x0x3 - 3/2048 x0x5 + 3/64 x1x2 - 3/64 x1x4
      - 3/128 x2x3 + 9/1024 x2x5 + 9/512 x3x4 - 3/512 x4x5
Q_6 = 0
```

This is stronger than "the same seven raw quadrics after recentering": there
is no recentering to do at grade `2n`, because the quadrics are independent
of `S,T` outright. The mechanism is that `Q_r(x + ell(a,b)) = Q_r(x)`
identically (verified), i.e. the whole tangent plane sits in the radical of
every `Q_r`. (See **C8** on "seven".)

### 3.2 Reduced support and the rank stratification -- CONFIRM

With `A(x)=x5+16x1-4x3`, `B(x)=x0-4x2+2x4`:

* every `Q_r` vanishes on the parameterization `w=ell(a,b)+(2p,0,0,q,-p,4q)`,
  and `A(w)=B(w)=0`, and the parameterization is a bijection onto `V(A,B)`
  (inverse `a=w2, b=8w1, p=w2-w4, q=w3-8w1`);
* Singular: `dim = 4`, exactly **one** minimal prime `(16x1-4x3+x5, x0-4x2+2x4)`,
  `radical(I) = (A,B)` with **both** containments checked
  (`reduce(rI,std(J))` and `reduce(J,std(rI))` both empty);
* positive/negative controls on the ideal itself: `A*B, A^3, B^3 in I` but
  `A^2 not in I`, and by exact linear algebra over `Q` neither `A^2` nor
  `B^2` lies in the degree-2 piece. So the cone is genuinely non-reduced and
  the packet is right to speak only of field-valued/reduced support.

`DQ_r(w)` factors as `alpha_r*A + beta_r*B` for every row (verified), with

```text
alpha = ( 3p/1024, 3q/256, -3p/8192, 0, -3p/131072, 0, -3p/1048576 )
beta  = (-3q/1024, 3p/16384, 3q/8192, 0,  3q/131072, 0,  3q/1048576 )
```

so `rank DQ(w)` equals the rank of the `7 x 2` matrix `[alpha,beta]`, whose
every nonzero `2 x 2` minor is a nonzero rational multiple of
`Delta = p^2 + 64q^2`. Hence rank 2 iff `Delta != 0`; rank 1 iff `Delta = 0`
and `(p,q) != (0,0)`; rank 0 iff `p=q=0`. Exactly (2.4) and the sentence
after it. Note `Delta=0` with `(p,q)!=(0,0)` forces `q != 0`, which is the
localization every downstream kill uses.

### 3.3 The odd-grade fan (2.5)--(2.8) -- CONFIRM

`G(2n+1)` depends only on `(s1,t1,N_n,N_{n+1})` (plus `k0` at `n=4`); no
higher surface coefficient occurs at all. The `n=2` grade-5 fan and the
`n=3` grade-7 fan are **literally equal** polynomials. Both claimed
identities reproduce exactly:

```text
det( [alpha,beta,N]  rows 1,2,3 ) = (27/2^35) * Delta * C          EXACT
G(2n+1)_4                          = (3/2^15) * E                   EXACT
det[ (C,E) ; (s,t) ]               = -Delta^2                       EXACT
```

Row 6 of the odd fan is identically zero, and row 4 has `alpha_4=beta_4=0`,
so row 4 is a pure equation -- this is what makes the rank-2 kill work.

**Rank two.** A solution forces the augmented `3 x 3` minor to vanish, so
`Delta*C = 0`, hence `C = 0`; row 4 gives `E = 0`; and `det[(C,E);(s,t)] =
-Delta^2 != 0` forces `s=t=0`, contradicting the promoted plane open.
Confirmed.

**Rank one.** I *derived* rather than assumed (2.8). Setting `p = u q`
(`u^2=-64`) in row 4 gives `(3/256) q^2 (s - u t)`, so `q != 0` forces
`s = u t` -- the **same** `epsilon` in both places, and it comes from row 4
alone. Then every one of the seven rows becomes

```text
row_r = c_r * ( Y - u X + 128 t q ),
c = ( -3q/1024, 3uq/16384, 3q/8192, 0, 3q/131072, 0, 3q/1048576 )
```

so the odd fan is exactly the single relation `Y - eps*8i*X = -128 t q`.
Confirmed, and the `a,b` plane parameters drop out identically on this chart.

**Rank zero.** Every odd-grade row vanishes at `p=q=0` (each `normal_r` is
divisible by `p` or `q`, and `alpha,beta` are multiples of `p,q`).

### 3.4 Recentering is a reparameterization -- CONFIRM

The `tau^n` coefficient of `D(S(tau),T(tau))` is `ell(S_n,T_n)` plus terms in
lower `S_j,T_j` only. I verified that `d[n]` is invariant under
`(a,b,S_n,T_n) -> (a+da, b+db, S_n-da, T_n-db)`, and for `m>n` the free
6-vector `N_m` absorbs the induced change in `d[m]`. So the family of arcs
with `(a,b)` free and the family with `a=b=0` are the *same* set of arcs.
That is precisely the packet's "coordinate change, not deletion of a branch".
(A naive shift that does **not** re-absorb into the higher `N_m` does change
higher grades for `n=2,3`; the packet's wording "the later coefficient block
remains arbitrary" is what makes it correct, and it is load-bearing.)

### 3.5 The imported G0--G3 premise -- CONFIRM, re-derived

I did not consume this by custody. `G0` and `G1` vanish identically
(all rows have min `d`-degree >= 2). Eliminating `d[2]` from `{G2, G3}`
in `Q[x0..x5,y0..y5]` gives an ideal `J` with

```text
radical(J) = ( 2x3-x5, x2-x4, 16x1-x5, x0-2x4 )
```

which is exactly the ideal of the plane `{ell(s,t)} = {(2s,t/8,s,t,s,2t)}`,
with both containments checked. Since `V(J)` is the closure of the
projection, every solution has `d[1] in P`; `ell` is injective, so
`(s,t)` is unique and `d[1] != 0` gives `(s,t) != (0,0)`. Confirmed. See
**C5** for why this transfers from the promoted `e=2` statement.

### 3.6 `n=2`: section 3 -- CONFIRM

On the rank-one chart with the G5 relation imposed and `s2..s6, t2..t6`,
`N_3` (constrained), `N_4, N_5, N_6` and `k0..k3` all symbolic:

```text
(3/128)G6_1 + (1/8)G6_3 + G6_5   = -q^3/16        EXACT
G6_6                              =  u q^3/256  ( = eps*i*q^3/32 )   EXACT
(1/512)G6_1 + (1/128)G6_3 + G6_7 =  q^3/128       EXACT
```

`G6_6` is in fact a *single term* after the reduction, so it is
coefficient-blind on its own. Rank one dies at G6 on `D(q)`. Confirmed.

### 3.7 Exhaustiveness -- CONFIRM_WITH_CORRECTIONS

The packet's table reproduces row by row. `n >= 2` because `d[1]=ell(s,t)`
can always be absorbed. At each `n` the three strata of the 4-plane
(`Delta != 0`; `Delta = 0, (p,q) != 0`; `p=q=0`) partition it, so the fan is
exhaustive at each level, and rank zero strictly increases the order of `N`.
The one branch the packet never *names* is `N == 0` -- the arc lying exactly
on the surface `D(S,T)`. I computed it, and also `ord(N) = 5,6,7,8`
explicitly: in every case `G0..G8 == 0` identically and

```text
G9_r = k10[0] * W_r(s,t)  with the same W_1, W_2,
```

so all of them die by the same two cubics. The claim is true; the branch
should be listed (**C4**).

## 4. Attack 3 -- `n=3`, the two G8 components and `G9_6`

Chart: `s1 = u t`, `p = u q`, plane absorbed, G7 relation imposed on `N_4`,
`X := A(N_4)`. Retained symbolically throughout: `alpha=S2`, `beta=T2`,
`gamma=S3`, `eta=T3`, `S4..S8`, `T4..T8`, all six `N_4` coordinates (four of
them free after the relation), **all six** `N_5` coordinates, all six `N_6`,
`N_7`, `N_8`, and `k10[0..3]`.

```text
G8_3 + (1/8)G8_1 = eps*(3i/2048) * F512     EXACT
G8_4             = -(3/4096)     * F640     EXACT
F512 - F640 = 32 q^2 (4t^2 + alpha - eps*8i*beta)     EXACT
F512 + F640 = 2 (X - eps*24i*t*q)^2                   EXACT
```

so on `D(q)` the pair generates
`(4t^2 + alpha - u*beta, (X - 3u t q)^2)`, whose field-valued support is
(4.6). That is exactly the packet's (4.5)/(4.6), and the packet is correct
to call `(X-3utq)^2` a visible non-reduced thickness rather than an ideal
identification.

On that reduced support, rows 4 and 6 vanish identically and the other five
are *exactly* scalar multiples of one form:

```text
G8_1 = (-3q/1024) H     G8_2 = (3uq/16384) H     G8_3 = (3q/8192) H
G8_5 = (3q/131072) H    G8_7 = (3q/1048576) H

H = Bz - u*Az + 128 q*beta + 136 u t^2 q
    - 512 t*y1 - u t*y2 + 64 t*y3 + u t*y4
```

which is (4.7) coefficient for coefficient, with
`(y1,y2,y3,y4) = (N4_1, N4_2, N4_3, N4_4)` -- the packet does not pin the
kernel basis, and this is the basis that makes its displayed constants
(`-512, -eps*8i, +64, +eps*8i`, and `eps*1088i = 136u`) come out right.
`H` is monic in `z0`, so each sign gives one irreducible component with a
5-dimensional `z` fibre. Confirmed.

**The terminal (4.8) -- CONFIRM, strengthened:**

```text
G9_6 = u q^3 / 256   =   eps * i * q^3 / 32
```

with variable support exactly `{u, q}`. Three strengthenings over the
packet's statement, all verified:

1. I did **not** impose `H = 0`. The constant already holds on the larger
   locus cut out by (4.6) alone, so it kills a strictly larger set than the
   two G8 components.
2. It is independent of `N_7` and `N_8` as well (the packet stops at `N_6`);
   the structural reason is that `ell(s,t)` lies in the radical of the
   quadratic part of every row, so `R^{[2]}(ell, ·) == 0` and `N_7` cannot
   reach G8, `N_8` cannot reach G9.
3. The literal variable supports confirm the packet's §6 truncation
   discipline exactly: `n=3` G8 involves only `{s1,s2,t1,t2,N_3,N_4,N_5}` and
   `n=3` G9 only `{s1,s2,s3,t1,t2,t3,N_3..N_6,k0}` -- no `S4,T4`, no `N_7`.

**The banked fixture (4.9) -- CONFIRM.** With `eps=+1`, `t=q=k10[0]=1`,
`beta=gamma=eta=y=0`, `z=(-1088i,0,0,0,0,0)` (whence the propagated
`alpha=-4`, `X=24i`, `Y=-320`, `N_4=(-320,0,0,0,0,24i)`), all **63**
coefficients `G0..G8` vanish and

```text
G9 = ( 65/2, 169i/8, -91/16, -51i/32, -29/256, i/32, -23/2048 ).
```

`G9_6 = i/32`. The old pass is still a pass and its first failure is exactly
where the packet says.

## 5. Attack 4 -- fresh `n=4`

`G0..G7` vanish identically and `G8 = Q(N_4)`, so all three reduced ranks are
G8-compatible; there are no further G8 constraints. The G9 fan is

```text
G9(n=4) = [ the n=3 grade-7 fan, verbatim ] + k10[0] * W,
W = ( (5/4096)t(3s^2-64t^2),  (5/65536)s(s^2-192t^2),  ..., 0, ..., 0, ... )
```

with `W_4 = W_6 = 0`, reproducing (5.3) coefficient for coefficient. I also
verified (5.1)'s middle term literally: `normal_r` is exactly
`[tau^9] R_r^{[3]}(ell*tau + w*tau^4)`, for all seven rows.

* **Rank two.** Row 4 carries no K10 term (`W_4=0`), and the `3 x 3`
  determinant *with* the K10 terms included is still exactly
  `(27/2^35)*Delta*C` -- the K10 contributions cancel in the determinant
  (difference computed and it is the zero polynomial). So the packet's "the
  same identities hold with the K10 term included" is exact, and `s=t=0`
  follows. Dead at G9.
* **Rank one.** `p=u q`; row 4 still forces `s = u t`; then

  ```text
  G9_2 + (eps*i/2) G9_1 = -(5u/128) k0 t^3 = -eps*(5i/16) k10[0] t^3   EXACT
  ```

  Nonzero on `D(t) cap D(k10[0])`. Dead at G9.
* **Rank zero.** `p=q=0` gives `G9 = k10[0]*W` exactly. Common zeros of
  `W_1, W_2`: `t=0 => s^3=0 => s=0`; `s=0 => -64t^3 * (5/4096) = 0 => t=0`;
  on `D(st)`, `s^2 = 64t^2/3` and `s^2 = 192t^2` give `512 t^2 = 0`. Only
  `(s,t)=(0,0)`. Dead at G9, and identically for `ord(N) = 5,6,7,8` and
  `N == 0`.

**Localization and closure splits.** Every division is tracked: `D(q)` on
rank one (forced by `Delta=0, (p,q)!=0`), `D(Delta)` on rank two, `D(t)` on
rank one at `n=4` (forced by `(s,t)!=0` and `s=ut`), `D(k10[0])` on the
`n=4` terminals, and `D(st)` in the `W` case split, which is complemented by
the two coordinate-vanishing cases. `Delta=0 => p=+-8iq` needs `i` and
char `!= 2`; `512 != 0` needs char `!= 2`; all tail denominators are powers
of 2 and the numerators carry 3 and 5, so the stated characteristic-zero,
algebraically-closed, Gaussian/Kummer-extended hypothesis is genuinely used
and is not vacuous.

## 6. Attack 5 -- controls and mutations

### 6.1 What the packet's replay actually does

| declared | what the code does | class |
|---|---|---|
| `CUSTODY` | SHA-256 of the seven charged inputs | custody gate |
| `OLD_PASS_FAIL` | re-evaluates the fixture from the rebuilt rows; asserts 63 zeros then `i/32` | **genuine** |
| `SURFACE_-4_TO_-3` | re-evaluates the *whole literal source* at `alpha=-3` and asserts G8 becomes nonzero | **genuine input mutation** |
| `DELTA_64` | compares a hand-built `det` against `-(p^2+63q^2)^2` | **check-side**: tests the hand identity `det=-Delta^2`, not any generator |
| `W2_192` | `if wrong_w2 == expected_w2: fail`, both hand-built | **check-side, unreachable branch** |
| `K10_OPEN` | zeroes `k0` in the hand-built terminal monomial | **check-side** |

`DELTA_64`, `W2_192` and `K10_OPEN` each become informative only in
combination with the `assert_equal` that immediately precedes them and ties
the hand-built object to the computed one. Taken on their own, `W2_192`'s
failure branch can never fire for any source whatsoever. This is a weaker
form of the defect Fable recorded as F1 on the parent packet (a banner entry
with no control behind it); here every entry does exist in code, but three of
six are checks rather than mutations. See **C2**.

**There is no source/tail mutation in the replay.** I supplied one.

### 6.2 My own mutations

*Positive controls.* Old fixture passes G0--G8 and fails at G9 with `i/32`
(reproduced independently). `alpha: -4 -> -3` makes G8 nonzero on rows
1,2,3,4,5,7 (reproduced). Perturbing `z0` from `-1088i` to `-1087i` breaks
G8 on rows 1,2,3,5,7 (`H=0` is exactly `z0 = -136u` for `beta=y=0,t=q=1`).

*Source/tail mutation (the one the replay lacks).* Perturbing a single one of
the 569 frozen coefficients, choosing monomials of `d`-degree >= 2:

```text
R1 [0,0,0,0,0,3,2,0,0,0] -15/128 -> +1/7 : surface identity BREAKS; W1 gains
                                            9 spurious terms in t2..t7,N5,N6,N7
R2 [0,0,0,0,0,2,4,0,0,0] 105/1024 -> +1/7 : surface BREAKS; W2 gains 8 terms
R4 [0,0,0,0,0,2,5,0,0,0] -63/1024 -> +1/7 : surface BREAKS; G8_4 becomes
                                            16 terms on the reduced support
R6 [0,0,0,0,0,2,6,0,0,0] 735/32768 -> +1/7: surface BREAKS; G9_6 becomes a
                                            14-term expression in t3,t4,t5,t6,
                                            N4,N5,N6 instead of u*q^3/256
R7 [0,0,0,0,0,3,5,0,0,0] 2601/131072 -> +1/7: surface BREAKS; G8_7 27 terms
```

So the surface identity, the two rank-zero cubics, the row-4 pure equation
and the `G9_6` terminal are all genuinely properties of the frozen 569 tails,
not artefacts of the framework. This is the decisive control the packet was
missing.

*K10-open failure (independently reproduced, not a check).* Setting
`k10[0]=0` and recomputing the `n=4` G9 fan from the source:

```text
rank one, k0=0 : every row = c_r * (Y - uX + 128 t q)  -> SOLVABLE, cell SURVIVES G9
rank zero, k0=0: all seven G9 rows identically zero    -> cell SURVIVES G9
```

so the open is load-bearing exactly where the packet says. Complementarily,
the `n=2` and `n=3` kills are **k10-free**: `G9_6 = eps*i*q^3/32` was computed
with `k0..k3` fully symbolic, and the fixture with `k10[0]=0` still gives
`G9_6 = i/32`. This scoping matters for promotion (§8).

*Terminal sign/coefficient.* Both Gaussian charts are computed
simultaneously as the two roots of `u^2+64`; `G9_6 = u q^3/256` is linear in
`u`, so both signs give a nonzero terminal, and the packet's
`eps*i*q^3/32` is correct for both. `(5.2)` matched as an exact polynomial
identity, so any perturbation of `-5/128` or of the sign fails by
construction.

## 7. Attack 6 -- language, scope, nonclaims

* **Field-valued vs scheme-valued.** Correct throughout. The three places
  where reducedness is used -- `sqrt(Q)=(A,B)`, `(X-3utq)^2=0 => X=3utq`, and
  `Delta=0 => p=+-8iq` -- are all statements about points over an
  algebraically closed field, and §6 explicitly declines to identify the G8
  ideal, transport multiplicities, or claim lifting. `A^2 not in (Q)` and
  `A^3 in (Q)` show the non-reducedness is real, so the hedge is necessary
  rather than decorative.
* **Radical / rank splits.** Both containments were checked in both
  directions; the rank split is by explicit `2 x 2` minors, all proportional
  to `Delta`, so the three strata are a genuine partition, not a case list.
* **Imported G3 scope.** Re-derived from scratch (§3.5), so the packet's
  reliance on it is safe. But see **C1** and **C5**.
* **Finite jets vs formal cells.** The packet is conservative. Since any
  formal arc in the cell truncates to a 9-jet in the cell, the G9 emptiness
  *does* exclude formal arcs **within this cell and these opens** -- a free
  strengthening the packet declines to take. It remains no statement about
  arcs outside the cell, about reachability, or about attainment.
* **Nonclaims.** §6's final paragraph is accurate and complete for what was
  proved. I add none: this review infers no source completeness, no
  reachability, no map, no other ramification pair, and nothing about JC2.

## 8. Exact maximum theorem safe for promotion

Let `K` be an algebraically closed field of characteristic zero. Take the
frozen K00 contracted source of the 569 charged tails under the charged
compiler's coordinate map (so `C6 = 1`), specialized at `Lambda = tau^3` with
the compiler's load shifts multiplied by `e = 3`, and restricted to the cell

```text
ord_tau(d) = 1,   k10[0] != 0,   Jdet[0] != 0,
k6, k2, mu2, mu4, mu6  each in tau*K[[tau]] or identically zero.
```

Then the G0--G9 truncation has **no `K`-point**:

```text
{ d[1],...,d[8] in K^6 ,  k10[0] in K  :
      G_{g,r} = 0 for 0 <= g <= 9, 1 <= r <= 7,
      d[1] != 0,  k10[0] != 0 }   =   empty,
```

uniformly over every admissible value of `k6, k2, mu2, mu4, mu6, Jdet`
(they cannot reach G9). Equivalently: no formal arc lies in this cell.
Through G9 the source is `R(d) + tau^6 k10(tau) A10(d)`, and the only load
term that occurs at all is `k10[0]` times the grade-9 cubic.

Scope conditions that must travel with it: char 0 and algebraic closure are
used; `i` is required; the `tau`-shift `= e *` (compiler Lambda-shift)
convention is a charged premise (cross-checked against the promoted `e=2`
lane, where it gives the confirmed `tau^4`), not derivable from `tails.json`
alone. Nothing is claimed about `e=3,m=2`, any other `(e,m)`, the face
`k10[0]=0`, attainment, reachability, a map, or JC2.

**Freely available upgrade** (I verified it; it is not in the packet): the
open `k10[0] != 0` can be weakened to `k10 != 0`. If `nu = ord(k10)`, the
`n>=4`/`ord(N)>4` branch dies at grade `9 + nu` by the *same* `W_1, W_2` with
`k10[nu]` in place of `k10[0]` -- checked literally for `nu = 0,1,2`, and
uniform in `nu` by the shift argument. The `n=2` and `n=3` kills need no K10
open at all. Promoting this needs the truncation extended to `G(9+nu)`, so it
is a separate (cheap) packet, not part of the G9 theorem.

## 9. Correction register

| id | severity | where | binding correction |
|---|---|---|---|
| C1 | material (custody) | §1 source list | `d453b9563d8f...` is labelled "promoted G3 leading-plane integration". It is `xmodel/k00-rank5-rankle1-coordinator-integration-sol56-20260829.md`, titled "K00 rank-five / grade-three rank-at-most-one coordinator integration", frozen at basis `92ebe92ad598...` (not this campaign basis), and contains no leading-plane incidence statement. The charged carrier of that premise is `0eb501b414f2...` §2 item 1. Fix the label. No math change: I re-derived the premise. |
| C2 | material (controls) | §6 items 3--5, replay banner | `DELTA_64` and `K10_OPEN` are check-side comparisons against hand-built expected values, and `W2_192`'s failure branch (`wrong_w2 == expected_w2`, both hand-built) is unreachable for any source. Relabel these three as *checks*, keep `OLD_PASS_FAIL` and `SURFACE_-4_TO_-3` as mutations, and add a real tail mutation (§6.2 supplies five). |
| C3 | minor (wording) | §0 (0.2) | `(s,t)` are not coordinates on the ambient jet space. State the open as `d[1] != 0` (equivalently, after the promoted plane theorem, `(s,t) != (0,0)`). |
| C4 | minor (completeness) | §0 table, §5 | Name the branch `N == 0` (the arc lying on `D(S,T)`) alongside `ord(N)>4`. It is killed by the identical `G9 = k10[0]*W`; verified for `ord(N)=5,6,7,8` and `N==0`. |
| C5 | minor (scope) | §0, §1 | State why the promoted G0--G3 premise transfers from `e=2` to `e=3`: no load can reach G2 or G3 for any `e >= 1` (K10's first grade is `2e+2 >= 4`), so the grade-2/3 analysis is `e`-independent. |
| C6 | minor (precision) | §4, §5, §6 | "`k10[0..3]` retained" over-retains. Only `k10[0]` can occur through G9, because `[tau^2]A10_r(d(tau)) = A10_r^{[2]}(ell) = 0` for every row. Retention is honest; the exact statement is stronger and free. |
| C7 | minor (understated) | §6 final paragraph | Within this cell the G9 exclusion *does* rule out formal arcs. Keep the nonclaim for everything outside the cell, but say the in-cell arc statement is available. |
| C8 | wording | §2 | "the same seven raw quadrics": row 6's quadric is identically zero, so there are six nonzero quadrics among seven rows. Likewise the odd fan has row 6 identically zero and row 4 free of the newest coefficient -- both are load-bearing and worth stating. |

None of C1--C8 changes the endpoint, the table, any identity, or the exact
maximum theorem.

## 10. Next cheapest ramified discriminator

**Recommendation: `e=3, m=2`, i.e. `Lambda = tau^3` with `ord_tau(d) = 2`.**

Rationale and a costed reconnaissance I already ran (4.8 CPU s, `CUT=13`):

* `m in {1,2}` are the only ramified residues for `e=3`; `m=0 mod 3` is the
  unramified lane. So `m=2` is exactly what is missing to close `e=3`.
* At `m=2` the first equation grade drops to **G4**, and the grade-4 system
  has term counts `(8,11,9,12,8,0,6)` -- **the same quadric cone `Q`**. The
  entire §2 machinery (4-plane, `A`/`B`, `alpha`/`beta`, `Delta`, `C`, `E`,
  the two Gaussian charts) transfers unchanged.
* The K10 load first reaches **G10** at `m=2` (`6 + 4`), so the whole G0--G9
  window is purely unloaded there. The `W_1,W_2` terminal that closes `m=1`
  is unavailable until G10, which is the substantive new work and the reason
  this is a real discriminator rather than a rerun.
* Cost: the same engine at `CUT = 13` runs in seconds; the work is rank-fan
  bookkeeping, not arithmetic. No AWS packet needed.

Second choice (strictly cheaper but less informative, and already half-done
above): promote the `k10 != 0` generalization of §8 by extending this same
`m=1` computation to `G(9+nu)`.

I did **not** freeze an AWS packet: nothing in this review approached the
desk envelope.

## 11. Coverage and non-coverage of this review

Covered: custody of all declared digests and all nine charged sources; a
clean-room rebuild of all seven unloaded and all seven K10 rows from the 569
tails; the surface identity; the calendar; the full rank tree at `n=2,3,4`
and `ord(N)=5,6,7,8,infinity`; every displayed identity in §§2--5; the G8
normal form and kernel basis; both G9 terminals; the fixture; six mutations
of my own including five tail mutations; the radical of the quadric cone in
both containment directions; and an independent re-derivation of the imported
G0--G3 plane.

Not covered, and not claimed: the `mu2/mu4/mu6/Jdet` sector bodies (they are
not in `tails.json`; I verified only their shift entries in the charged
compiler and that they cannot reach G9); the `tau`-shift `= e *` Lambda-shift
convention (charged premise, cross-checked, not derived); anything at grade
`>= 10`; the face `k10[0] = 0` beyond showing it survives G9; any other
`(e,m)`; scheme structure of the G8 ideal; attainment, reachability,
algebraization, a polynomial map, or JC2.

<!-- BODY-END -->
