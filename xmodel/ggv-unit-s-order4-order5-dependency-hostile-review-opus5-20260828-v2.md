# Hostile review: unit-`S` order-four / order-five dependency chain

Date: 2026-08-28
Reviewer: **Opus 5, different-model hostile review** (retry lane v2; the prior
Fable 5 lane produced no report — CLI token overflow — so no prior verdict was
available to this review).
Method: independent desk derivation plus a private exact standard-library
recomputation in `/tmp` (no checker written into the repository, no CAS, no AWS).

## Terminal verdict

**REPAIR**

The mathematical core is correct. Every displayed identity in both packets
reproduces exactly under an independent reconstruction that is *stronger* than
the producers' (full jets, all modes through `m=14`, the `f5` term included).
The repair is documentary: the order-four checker verifies a hand-transcribed
surrogate for `f2` rather than the real normalized coefficient, one of its two
advertised mutations is decorative, one order-five assertion is a tautology,
and three wording points need caveats. None of these changes the conclusion.

## 0. Hash recomputation

All six charged SHA-256 values recomputed and **matched**: the order-four
report `874bcd98…`, its checker `a4e6f18b…`, the order-five report
`aa88f190…`, its checker `f683bd2a…`, the R12r extension report `da189b7f…`,
and its checker `112650dc…`. All three checkers run and print their markers;
each `print` is guarded by preceding `assert`s, so the banners are not
unconditional.

## 1. Independent setup

`F = sum_n F_n(X) t^n`, `t = eps*tau`, `eps = X-alpha`, `alpha` a simple root of
squarefree `A`. Then `eps^-4 F = sum_{n,d} F_n[d] eps^(n+d-4) tau^n`, so the
*relative* order is `n+d-4`. Write `A = eps(a+b*eps+…)` with `a = A'(alpha) != 0`,
`S = s+h*eps+…`, `Q = q+r*eps+…`, `U = u+v*eps+…`, `P1 = p+…`, `F6 = w+…`,
`F7 = f7+…`.

**Mode birth law.** Mode `m` of `G = F^(3/2) + sum_(m even) c_m t^m F^((12-m)/8)`
carries `eps^(m + 4(12-m)/8) = eps^((m+12)/2)`, i.e. relative order `m/2`.
Recomputed: `m = 0,2,4,6,8,10,12` are born at relative orders `0,1,2,3,4,5,6`.
So relative order four sees exactly `m = 0,2,4,6,8` and relative order five
exactly `m = 0,…,10`. **Both packets' mode censuses are complete.** Note the
campaign name collision: `L` denotes the face factor `A'(alpha)+S(alpha)tau/4`
in these two packets but `QS+4U` in R12r (there renamed `ell`). I keep the face
meaning and write `L_R = QS+4U`.

## 2. Order four

### 2.1 The abstract identity (1)

Substituting `f1 = L^2*K`, `f2 = B`, `f3 = C`, `f4 = D` and expanding all seven
modes `m = 0..12` exactly, the relative-order-four coefficient equals

`(3/2)L^2 D + (3/4)KC + (3/128)L^-2(4B-K^2)^2
 + c2 tau^2[(5/4)LC + (5/128)L^-1 K(8B-K^2)] + c4 tau^4 B
 + (3/4)c6 tau^6 LK + c8 tau^8 L^2`,

with minimal `L`-power `-2`. **CONFIRMED**, every coefficient. The delicate one
is `binom(3/2,4) = 3/128` (not `3/64`); I verified it twice. Modes `m >= 10`
contribute nothing, as the birth law predicts.

### 2.2 The literal prefix

I rebuilt `F0..F6` myself from the R12r primitives rather than copying the
order-four report: `V0 = A S`, `T = A U`, `Z = (S^2-AQ)/2` (from `S^2-2Z = AQ`),
`K = 64F4-Z^2 = A R` with `R = 4SU` (exact `D = R-4SU = 0`),
`P = 256F5-RS+2S^2U = A P1`, `E = 2048F6-2SP1-4QSU-8U^2 = A e1`. This gives

`F2 = A^2(3S^2-AQ)/8`, `F3 = AS^3/16 + A^2(U-SQ/2)/8`,
`F4 = (S^2-AQ)^2/256 + ASU/16`, `F5 = (AP1+2S^2U)/256`,
`2048F6 = Ae1 + 2SP1 + 4QSU + 8U^2`.

These reproduce the order-four report's displayed `F0,…,F5` **exactly — every
sign and every power of two**. Note `F4` and `F5` both consume `R = 4SU`, so
they are valid only on the exact-`D` branch, as claimed.

### 2.3 `f1`, `f2`, and the two lifts

Relative order zero is `(a+s*tau/4)^4 = L^4`. **CONFIRMED.**

With `U` left entirely free I get `f1(tau0) = f1'(tau0) = 0` unconditionally
(so `L^2 | f1` always, matching the earlier reviewed statement), and the exact
third-order obstruction

`s^3 * f1''(tau0) = -(a^3 s^2/4)(4u + sq)`.

Hence **`L^3 | f1` holds if and only if `(QS+4U)(alpha) = 0`** — the first D12
lift, which is precisely load-bearing rather than incidental. Under it,
`f1 = L^3(4b + h*tau - q*tau^2/8)`, i.e. (3). **CONFIRMED.**

With `u = -sq/4` imposed and `F6` free, my full-jet computation gives

`s^6 * B(tau0) = a^6(s^2 q^2 - 4sp + 4096w)`,

which is (4). **CONFIRMED — and in a strictly stronger form than the producer's:
all jets `b, h, r, v, a3, a4, s2, s3, q2, q3, ell_i, p1, e1_i` cancel
identically**, not merely after truncation. The second D12 lift
`2048F6 - 2SP1 - 4QSU - 8U^2 = 0` at the root, combined with `u = -sq/4`, is
exactly `4096w = 4sp - s^2 q^2`, i.e. (5). **CONFIRMED.** So `B(tau0) = 0` and
`L | B`.

### 2.4 Conclusion at order four

With `f1 = L^3 J1`, `f2 = L H2`, generic `f3, f4`, the minimal `L`-power of the
relative-order-four coefficient is `0`. **CONFIRMED.** Structurally,
`(4B-K^2)^2 = L^2(4H2-L J1^2)^2` and `L^-1 K(8B-K^2) = L J1(8H2-L J1^2)`; the
`L^-2` and `L^-1` classes both clear.

### 2.5 Mutations of the lifts

- Break the `L_R` lift (`u -> -sq/4 + delta`): `s^3 f1''(tau0) = -(3/2)s^2 delta`
  up to my normalization — nonzero, so `L^3 ∤ f1`. **Detected.**
- Break the `E` lift (`w -> w_root + delta`): `s^6 B(tau0) = 4096 a^6 delta != 0`,
  so `L ∤ B`. **Detected.**

## 3. Order five

### 3.1 The sole polar part

With `f1 = L^3 J1`, `f2 = L H2`, `f3 = C3`, `f4 = D4`, **and `f5 = E5` present**,
expanding modes `m = 0,…,14` gives minimal `L`-power `-1` and negative part
exactly

`L^-1 * H2 * (3C3/4 + 5c2 tau^2 H2/32 - 3J1 H2/16)`.

**CONFIRMED as the sole polar part.** The partition census behind it:
pure `k=2` gives `(3/4)L^-1 H2 C3`; pure `k=3` gives `-(3/16)L^-1 J1 H2^2`;
`c2` at `k=2` gives `(5/32)c2 tau^2 L^-1 H2^2`; everything else
(`pure k=1,4,5`; `c2 k=1,3,4`; `c4`; `c6`; `c8`) lands at `L`-power `>= 0`.

**The `c10` question.** Mode `m=10` is born exactly here and contributes exactly
`c10 * tau^10 * L` — a single, manifestly regular term. The producer checker's
failure to register `c10` is therefore **checker coverage only, not a
mathematical omission.** Likewise `f5` contributes exactly `(3/2)L^2 f5` (pure,
`k=1`) and nothing else; it is regular. Both verified symbolically.

### 3.2 The literal identifications

Reconstructing `F0..F7` under `QS+4U = A*ell` and `2048F6-2SP1-4QSU-8U^2 = A*e1`,
with **full** jets, and writing `Jc = p - s q^2/2`, `Nc = 8192 f7 - e1 s + q Jc`:

- `f2` vanishes at `tau0 = -4a/s`, so `L | f2`. **CONFIRMED.**
- `H2(tau0) = -4 a^5 Jc / s^5`. **CONFIRMED**, exact powers of `a` and `s`.
- `bracket(tau0) = -a^7(20 c2 Jc + 3 Nc)/(2 s^7)`. **CONFIRMED**, exact powers.
- `(H2 * bracket)(tau0) = 2 a^12 Jc(20 c2 Jc + 3 Nc)/s^12`. **CONFIRMED.**

**The `8192` load.** `F7` reaches this order only through `C3`, as
`(3/4) s^7 f7 tau0^7 = -12288 a^7 f7 = -(3/2)(8192) a^7 f7`, matching
`-a^7 * 3 * 8192 f7/2` in the target. The load is forced, and the
`8192 -> 8191` mutation **fails as required**.

### 3.3 The R12r licence

`J = P1 - SQ^2/2` and `N = 8192F7 - e1 S + QJ` evaluate at `alpha` to `Jc` and
`Nc` — definitional, verified. R12r states the complete residual D12 negative
part as `g12^- = J(20c2 J + 3N)/(8388608 A)`; polynomiality of that row forces
`A | J(20c2 J + 3N)`, hence, `A` being squarefree, `Jc(20c2Jc+3Nc) = 0` at every
root. Since `a != 0`, the order-five polar numerator vanishes at `tau0`.

**Is rootwise vanishing enough to divide by `L`?** Yes. `L = a + s*tau/4` is
degree one in `tau` over the coefficient field (char 0), so `L` is prime in
`k[tau]` and `L | X` iff `X(tau0) = 0`. **CONFIRMED.** I add a strengthening the
packet does not state: if `s = S(alpha) = 0` the `tau0` route degenerates, but
then `L = a` is a nonzero constant and there is *no* pole at all — so the
conclusion holds on the whole branch, and `S(alpha) = 3 lambda A'(alpha) != 0`
is convenience, not a load-bearing hypothesis.

**Staging.** The order-five residue is proportional to exactly the product the
D12 row already forces to vanish. So the correct reading is the packets' own:
*orders four and five impose no new cut beyond the existing determinant
cascade.* That is a conditional "no new information" theorem, not an
unconditional regularity theorem, and both reports say so.

## 4. Repair items (documentary; none affects the conclusion)

1. **`raw_f2` is not `f2`.** The order-four checker's hand-written `raw_f2`
   differs from the true normalized second coefficient by a gap supported in
   `tau`-degrees 0–4 — it has no `tau^0` or `tau^1` terms at all, although the
   true `f2` contains e.g. `[eps^6]A^4 = 4a^3 a3 + 6a^2 b^2`. The gap happens to
   vanish at `tau0`, so (4) still comes out right, but the checker validates a
   surrogate. My structural full-jet build establishes (4) properly.
2. **Jet truncation.** Both checkers truncate `A` at `eps^3`, `S`/`Q` at `eps^2`,
   `ell`/`P1` at `eps^1`, `e1` and `F7` at `eps^0`. Those higher jets genuinely
   appear in `f2` and `C3`; that they cancel at `tau0` is assumed, not shown. I
   verified the cancellation.
3. **Decorative mutation.** The order-four checker's `break_L_relation` control
   asserts `evaluate_tau_times_s_power((u_root+delta)*tau - a*q, 1) == -4a delta`
   on a hand-built expression unconnected to `f1`. The genuine mutation is
   `s^3 f1''(tau0) = -(a^3 s^2/4)(4u+sq)`, supplied above. (The `E`-lift
   mutation is genuine.)
4. **Tautological assertion.** In the order-five checker,
   `assert residue_clear - 2*a**12*campaign_product == 0` is vacuous:
   `residue_clear` is *defined* to be that. The real product identity (4) is
   never formed from `h2_clear` and `bracket_clear`. I formed and verified it.
5. **Symbol aliasing.** The order-five checker reuses `J, D, C, B, K, u, w,
   delta` for both abstract and literal roles. No live collision, but fragile;
   my run uses disjoint names and reproduces every identity.
6. **Wording, order-four §1.** "regularity would force `L|K` and `L|B`" silently
   needs active `c2` (and `a != 0`). At `c2 = 0`, `K = 2`, `B = 1+L` gives
   `4B-K^2 = 4L`, regular, with `L ∤ K`. The hypothesis is standing in the
   packet, but the sentence should carry it.
7. **Wording, order-five §1.** The displayed expansion stops at `eps^4 D4 +
   O(eps^5)`; the `eps^5` coefficient `f5` does contribute at relative order
   five, as `(3/2)L^2 f5`. Regular, but it should be named rather than dropped.
8. **Inherited status.** The chain is conditional on upstream not re-derived
   here: the q1-free D9 reduced prefix (`1874b9db…`), the D8 lifts `A|K` and
   `A|(S^2-2Z)`, `A|P` from D9/D10, the exact `D = 0` branch, and R11/R12/R12r —
   whose own packet carries a **REPAIR** verdict (its "`A|D` alone survives
   deepest D11" claim was refuted there). Both reports should name the parent's
   status explicitly.

## 5. Licence and scope firewall

Verified as claimed: simple root of squarefree `A` (`a != 0`, `A` has `eps`-
valuation one); characteristic zero (the loads `128, 2048, 8192, 8388608 = 2^23`
and the binomials require char `0`); active `c2` (load-bearing in R12r's passage
from `5c2 L_R^3 = 0` to `A | L_R`, and in the §1 remark); exact-`D` branch
(load-bearing in `F4`, `F5`); `S(alpha) = 3 lambda A'(alpha) != 0` (imported from
the q1 branch, convenience only — see §3.3).

This is **local face regularity at one simple root**. It is not a raw-window
statement, not an endpoint result, not a higher-order polynomiality claim, not a
Keller theorem, and not JC2. Both reports scope themselves correctly, and I
infer nothing beyond relative order five.
