# Hostile review: GLOBAL-INTERPOLATION — exact conditions, n−m−1, Galois, log block, counts, driver

**Reviewer.** grok-4.6 (different-model gate).
**Date.** 2026-09-03.
**Lane.** `GLOBAL-INTERPOLATION-REVIEW`.
**Charge.** Default to refutation. Desk-scale exact CAS (sympy 1.12) over `Q`. Frozen inputs only. `FALLACY-v2` in force. No `charge_basis` line: no new exit price. No canonical-ledger edit; `jc2-lean` not opened. No `ideation-20260903T1015Z-*` file and no sibling running-lane report was read.

**Headline.** The interpolation identities, the `n-m-1` degree count, polynomiality-after-descent, the log-block implication, the bare-tuple information obstruction, the existential quadratic lift, and the charged driver numbers all survive independent re-derivation and rerun. Two binding repairs: “one constant per orbit” does **not** need `NO-RESIDUE` for the count (only to land in the Puiseux field), and averaging does **not** need the orbit to be the full `μ_R`; and `U(Q)=h+u_0+|Z_Q|` in (4.13) is inconsistent with the stationary model used for (4.16). The requested extra Keller two-orbit control is empty in `Aut(C^2)`; coupling of invariant integer-order coefficients across distinct local orbits is nevertheless real, and is exhibited on an explicit two-orbit polynomial pair.

## Verdict table

| # | Claim | Verdict | Promote? |
|---|---|---|---|
| (1) | Lagrange `A_q` (1.3); moments (1.5); triangular conversion (1.6) | **CONFIRMED** | CAN |
| (2) | Degree conditions are `n-m-1` homogeneous identities plus monic `M_{n-m-1}=1`; “`n-m` degrees to kill” is false | **CONFIRMED** | CAN |
| (3) | Polynomiality is the support test (1.9)/(1.10), reducing after descent to (1.11) | **CONFIRMED** | CAN |
| (4) | Exact tree factorisation (2.1)–(2.2); BOTTOM-ODE is the leading local block | **CONFIRMED** | CAN |
| (5) | Galois: one constant per orbit (2.4), fractional cancellation (2.5), support (2.6); not integer-order vanishing nor inter-orbit relations | **CONFIRMED** with hypothesis repair at (2.4) | CAN after repair |
| (6) | `NO-RESIDUE` is the log block; (DEG)+(POLY) in `K[log x]` imply it (3.2); computationally independent in the Puiseux-field implementation | **CONFIRMED**; log-aware (DEG) is not circular | CAN |
| (7) | No unknown count on the bare tuple (§4.1); exact counts (4.7)–(4.16) on a decorated skeleton | **CONFIRMED** for §4.1 and (4.7)–(4.12),(4.15); **GAP** at (4.13) vs (4.16) | CAN §4.1; repair `U(Q)` |
| (8) | Quadratic lift (4.17) is existentially equivalent | **CONFIRMED** on the nonzero-separation open set | CAN |
| (9) | Controls, composition (5.4)–(5.5), residues (5.6), two-tower `λ` table, driver 40/0, 50/0, example rank 26 | **CONFIRMED**; driver’s five-disc check is combinatorial, not a reversion | CAN the math; not the combinatorial proxy |

No item is **REFUTED**. No exit price is asserted.

---

## 0. Custody, method, scope

Frozen copies were hashed with `sha256sum` **before any was opened**. All six match the charge exactly:

```text
20d554a0b19c563093ec35caad58664f800d7517490f530a07f511d7042393b6  global-interpolation-sol56-20260902.md
49ba5a019714e30a952c998fb39a88aff38505a80fcac6df3c5883bb16599588  globalinterp.py
9e485492940818ea25b955af1713de53bc823af78f9f00a8991aaba9372f527d  time-function-endgame-review-sol56-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  integration17-coordinator-fable51-20260902.md
e639fdbf5cdbdf0756d9d8287b52c0183b07e2bf8ab7d4b293c242ea2c35f37c  exact-n-rigidity-opus5-20260902.md
69ff5bdea265adc37c9518f381eccfe6a6162c430a51075b6c2069f709894473  bottomode.py
```

Live `box/globalinterp-drivers-20260902/globalinterp.py` and live `box/tfe-drivers-20260902/bottomode.py` have the same hashes. Line citations `SOL:L` refer to the frozen Sol report. `TFE-R` is the frozen time-function-endgame review. Two-tower pairs are the seven `TWO_TOWER` rows of live `control4.py` (the pairs, not that file’s buggy `lambda_g`). Campaign `FALLACY-v2` is in force. No `sat()`, no `jc2-lean`, no ledger edit.

**Ring map.** Coefficient field `Q` (sympy `EX`/`QQ` as indicated). Puiseux uniformizer `x=z^{-R}` with `R` as declared. Jacobian convention `[f,g]=f_x g_y-f_y g_x`. Prime marks: `p_g'=d/dπ`, `F_i'=d/dx`. Matching names are not used as a map proof.

---

## 1. Item (1) — (1.3), (1.5)–(1.6). **CONFIRMED**

Let `G(y)=∏_{i=1}^n (y-τ_i)` be monic of degree `n`, `D_i=G_y(τ_i)=∏_{j≠i}(τ_i-τ_j)`, and `e_r^{(i)}` the `r`-th elementary symmetric function of `{τ_j:j≠i}`. Then

```text
∏_{j≠i}(y-τ_j) = ∑_{q=0}^{n-1} (-1)^{n-1-q} e_{n-1-q}^{(i)} y^q.
```

The unique interpolant of degree `<n` through values `H_i` at nodes `τ_i` is `L=∑_i H_i ∏_{j≠i}(y-τ_j)/D_i`, so

```text
A_q = (-1)^{n-1-q} ∑_i H_i e_{n-1-q}^{(i)} / D_i.     (1.3)
```

This is the coefficient of `y^q` in the Lagrange formula, not a leading-order analogy. Independently, partial fractions at infinity give

```text
L(y)/G(y) = ∑_i H_i / (D_i (y-τ_i)) = ∑_{r≥0} M_r y^{-r-1},
M_r := ∑_i H_i τ_i^r / D_i.                            (1.5)
```

Write `G(y)=∑_{j=0}^n (-1)^j e_j y^{n-j}` with `e_0=1`. The product of this expansion with `∑_r M_r y^{-r-1}` has nonnegative part `∑_q A_q y^q`, and the coefficient of `y^q` is exactly

```text
A_q = ∑_{j=0}^{n-q-1} (-1)^j e_j M_{n-q-j-1}.          (1.6)
```

The conversion is unit-triangular: `A_{n-1}=M_0`, `A_{n-2}=M_1-e_1 M_0`, and so on, with diagonal `e_0=1`. Thus (1.3) and (1.4)–(1.6) are equivalent.

**CAS.** Generic nodes/values in `n=2,3,4`: `(1.3)` matches the Lagrange interpolant identically; `(1.6)` matches `(1.3)` identically, including `A_{n-1}-M_0=0` and `A_{n-2}-(M_1-e_1 M_0)=0`. For `n=5`, (1.8) on nodes `{1,2,3,4,5}` gives `M_0=⋯=M_3=0`, `M_4=1` (below). The identities are polynomial in the nodes and hold in every degree; the `n=5` generic-symbol expansion was not needed.

**Repair.** None. `SOL:129-156` can be promoted as written.

---

## 2. Item (2) — (DEG) count and (1.8). **CONFIRMED**

Moh’s monic gauge `[y^m]f=1` with `m<n` is `A_{n-1}=⋯=A_{m+1}=0` and `A_m=1`. That is `n-m-1` homogeneous vanishings plus one affine normalisation. Unit-triangularity of (1.6) translates this into

```text
M_r = 0  for  0 ≤ r ≤ n-m-2,     M_{n-m-1}=1.           (DEG)
```

The first range is empty when `m=n-1`. Displayed total in (DEG): `n-m`. If one only asks `deg_y L=m` without a prescribed leader, the exact condition is the `n-m-1` vanishings together with the open condition `M_{n-m-1}≠0`. Calling all `n-m` equations “degrees to kill” is therefore false. This is the off-by-one in `I17:97-98` (“`n-m` compatibility conditions”).

**CAS counts** `(m, n-m-1, n-m)` for `n=2,3,4` match the table. Driver metadata on the example `(n,m)=(2,1)` reports `series_count=0` high-degree relations and a separate `B_1=1`.

The universal identity

```text
∑_i τ_i^r / D_i = 0  (0≤r≤n-2),    =1  (r=n-1)         (1.8)
```

is the case `H_i=1` of (1.5): `L=1`, so `1/G=∑_r M_r y^{-r-1}`, and `1/G=y^{-n}+⋯`. Residue at infinity of `y^r/G(y)` is `1` iff `r=n-1`. **CAS:** generic `n=2,3,4`; integer nodes `n=5` as above.

For `m≥1` one has `n-m-1≤n-2`, so adding the same constant to every `H_i` does not change (DEG); it changes only `A_0`. `SOL:197-199` is correct.

**Repair.** None. Promote `SOL:163-199`.

---

## 3. Item (3) — polynomiality (1.9)–(1.11). **CONFIRMED**

After (DEG), the remaining condition is `A_q∈C[x]=C[t^{-1}]` for `0≤q≤m`. In `z=t^{1/R}` one has `x=z^{-R}`, so `C[x]` is the series whose support lies in `{-Rd:d∈Z_{≥0}}`. That is (1.9)–(1.10). After Galois descent to a `Γ`-invariant element of `C((t))`, only integer `t`-powers remain, and polynomiality is `[t^h]A_q=0` for `h≥1`. An element of `C((t))` already has finitely many negative terms; a total-degree cap on `A_q` is a stronger, optional condition, and the driver exposes it as `moh_total_degree` versus a bounded slice of bare (POLY).

Minor nonblocking observation: after (DEG), `A_m=1` already, so the `q=m` row of (1.11) is redundant. The later count (4.9) correctly drops it. Not a refutation of (POLY).

**Repair.** None required for promotion. Optional: state that (1.11) for `q=m` is already in (DEG).

---

## 4. Item (4) — tree factorisation and BOTTOM-ODE. **CONFIRMED**

Every `j≠i` has a unique first-separation vertex `v` on the path from leaf `i` to the root of the cluster tree. Writing `S_v(i)` for the leaves in the siblings of the child of `v` that contains `i`, one has a partition of `{j≠i}` and therefore the exact product identities (2.1)–(2.2). These are set-partitions, not leading-order analogies. Substitution into (1.3) makes every ancestor packet visible in every `A_q`.

BOTTOM-ODE as the leading local block is a citation of reviewed `LOCAL-KELLER` plus `D1-PIN`, not a new derivation. In interpolation language: the leading star values of `f` on a completed bottom disc interpolate to `p_f`, and (JF) converts the Wronskian into the displayed bracket. The converse (a formal solution of `LOCAL-KELLER` need not come from a polynomial in `C[x,y]`) is the content of (DEG)+(POLY), and is the correction already made by `TFE-R:101-133`. Frozen `bottomode.py` is the reviewed local solver; it is not re-audited here beyond hash identity.

**Repair.** None. Promote (2.1)–(2.2) as exact. Promote the BOTTOM-ODE sentence as a reviewed citation, not as a new local existence theorem.

---

## 5. Item (5) — Galois (2.4)–(2.6), and the extra two-orbit control. **CONFIRMED** with hypothesis repair

### 5.1 Re-derivation of (2.4)–(2.6)

Let `Γ=μ_R` act by `z↦ωz`. Then `x=z^{-R}` is invariant, so `d/dx` commutes with `Γ`, and `γ(τ_i)=τ_{γi}` implies `γ(D_i)=D_{γi}` and `γ(R_i)=R_{γi}`. If primitives `F_i` exist in the Puiseux field `K=C((z))`, one has `γ(F_i)-F_{γi}∈C` because constants of `K` are `C`. This is an additive cocycle of the finite group `Γ` with values in `(C,+)`. In characteristic zero, `H^1(Γ,(C,+))=0`, so averaging

```text
F̃_i = (1/|Γ|) ∑_γ γ^{-1} F_{γ i}
```

produces equivariant primitives, hence `a_{γi}=a_i`. Consequently there is **one free integration constant per Galois orbit**.

**Exact hypothesis for “one constant per orbit”.**

1. The set `O` is a genuine orbit of a finite group of field automorphisms acting `C`-linearly (a `Γ`-orbit, or an orbit of a quotient through which `Γ` acts on a subfield). It need **not** be the full set of `n` branches, and the group need **not** be the full `μ_R`: averaging over `μ_R` or over the image group gives the same equivariant primitive, because the action on a proper subfield factors through a quotient and the extra summands repeat.
2. Averaging over a set that is **not** Galois-closed does not apply. A geometric cluster that is not an orbit is not a legal input to (2.4).
3. `NO-RESIDUE` is required to have primitives **in `K`**. It is **not** required for the count of free additive constants. In `K[log x]`, writing `H_i=H_i^P + c ρ_i log x`, the residue `ρ_i` is Galois-invariant on an orbit (one scalar equation per orbit, not a free constant), and the `z^0` terms of `H_i^P` still form an additive cocycle with `H^1=0`. The number of free constants remains `h=#orbits` with or without `NO-RESIDUE`; without it one cannot form `F_i` inside `K`.

**Line repair for `SOL:319-327`.** Replace “Once `NO-RESIDUE` holds, primitives can be chosen equivariantly… averaging over the finite group” by: primitives in `K` exist iff `NO-RESIDUE`; given primitives in `K` or in `K[log x]` with a chosen additive Galois action, averaging over the finite Galois group of the common field (not necessarily the full `μ_R`, and not requiring the orbit to be all `n` branches) kills the additive cocycle. The free constant count is one per orbit either way.

(2.5) is then immediate: each orbit sum `M_{r,O}` is `Γ`-invariant, so `[z^k]M_{r,O}=0` unless `R∣k`. Cancellation is internal to each complete orbit. Distinct orbits are not related by symmetry.

(2.6) is the residual character of a disc stabilizer `π↦χπ` of order `Δ` acting on monic leading polynomials: `p_g(χπ)=χ^a p_g(π)`, `p_f(χπ)=χ^b p_f(π)`, hence supports in one residue class modulo `Δ`. A nonzero constant Wronskian forces `Δ∣a+b-1`. Simple roots give `a≡0` or `1 (mod Δ)`. These are star/Galois constraints, not extra copies of (DEG)/(POLY).

What Galois does **not** give for free (`SOL:362-371`) is correct: it does not kill an invariant integer-order coefficient, does not relate distinct orbits, and does not turn a formal tail into a polynomial tail. Those are the global sums in §2.4.

### 5.2 The charged extra control: two distinct local orbits

A polynomial automorphism `(f,g)` has polynomial inverse. On a generic fibre `g=c_2` one has `(x,y)=(X(u,c_2),Y(u,c_2))` with `X,Y` polynomial in the time coordinate `u=f`. The equation `X(u)-x=0` at `x=∞` has a unique Newton segment of length `n=deg_u X`. Local monodromy `μ_n` is therefore transitive on the `n` Puiseux branches of a generic `g`-fibre at `x=∞`. **There is no polynomial automorphism with two local Galois orbits of bottom branches at `x=∞`.** Among known Keller pairs (all automorphisms), the requested extra control is empty. A hypothetical non-automorphism Keller pair is `OPEN[KELLER-TWO-LOCAL-ORBITS]` below (0 known examples).

The coupling claim of item 5 is nevertheless testable off the automorphism locus. Take the polynomial pair

```text
f=y,   g=(y^2-x)(y^2-4x)=y^4-5x y^2+4x^2,
```

Jacobian `-8x+5y^2∉C^*` (not Keller). Four Puiseux branches at infinity, `s=√x`:

```text
O1={s,-s},    O2={2s,-2s}.
```

The involution `s↦-s` preserves each pair and does not mix them: two local Galois orbits. Exact denominators `D=( -6s^3, 6s^3, 12s^3, -12s^3 )`. Interpolating `H_i=τ_i` (i.e. `f=y`, so `m=1`, `n=4`, (DEG) is `M_0=M_1=0`, `M_2=1`) gives

| moment | orbit `O1` | orbit `O2` | sum |
|---|---|---|---|
| `M_0` | `-1/(3x)` | `+1/(3x)` | `0` |
| `M_1` | `0` | `0` | `0` |
| `M_2` | `-1/3` | `+4/3` | `1` |

Both invariant integer-order contributions to `M_0` and to the monic moment `M_2` are **nonzero**; only the sum across orbits is the global (DEG) value. This is exactly `SOL:377-379` and the “not for free” half of item 5.

The emitter, run on the corresponding two-orbit decoration (`x=z^{-2}`, branches `±z^{-1}` and `±2z^{-1}`, two verified orbits), produces two integration constants and evaluation identities

```text
evaluate[a1,0]:  Hconst_orbit_A - A_0_0 = 0,
evaluate[b1,0]:  Hconst_orbit_B - A_0_0 = 0.
```

The shared polynomial coefficient `A_0_0` identifies the two orbit constants at the invariant order `z^0`. Rank: 68 raw / 66 deduplicated equations, 52 unknowns, ambient Jacobian rank 51; `NO-LOG` effective count 2. Coupling is through the shared interpolant, not through an intra-orbit character.

**Repair.** Keep `SOL:362-371`. Add the hypothesis repair of §5.1. Do not advertise a Keller two-orbit control; the automorphism obstruction is structural.

---

## 6. Item (6) — `NO-RESIDUE` and (3.2). **CONFIRMED**; not circular

Write `1/D_i = ρ_i x^{-1} + (exponents ≠ -1)`. A Puiseux primitive of `c/D_i` exists in `K` iff `ρ_i=0`. In `z=t^{1/R}`, `dx=-R z^{-R-1} dz`, so the `z^{-1} dz` term in `W_i dx` is produced by `[z^R]W_i`. That is `NO-RESIDUE`. Galois conjugate branches have the same residue: `h` independent scalar equations, one per orbit.

If residues are not zero, `H_i=H_i^P + c ρ_i log x` in the differential extension. The logarithmic part of the interpolant is `c log x · R(y)` with `R(y)=∑_i ρ_i ℓ_i(y)` of degree `<n`, and `R(τ_i)=ρ_i`. Interpret (DEG) and (POLY) in `K[log x]`: every coefficient of `L`, high and low, lies in `C[x]⊂K` and in particular has vanishing log coefficient. Then `R=0` as a polynomial, hence every `ρ_i=0`. This is (3.2).

**Circularity.** None. Log-aware (DEG) is the same geometric condition `deg_y L≤m` and `[y^m]L=1`, read in the coefficient ring in which the interpolant actually lives. It does not assume `NO-RESIDUE`; it concludes it. Interpreting (DEG) only on Puiseux parts would leave a logarithm in a high coefficient uncontrolled, which is why `SOL:451-457` correctly distinguishes the log-aware system from the Puiseux-field implementation. In the latter, primitives are formed in `K` before interpolation, so `NO-RESIDUE` is an independent well-formedness equation and must be imposed first. Both positions are accurate.

**Repair.** None. Promote `SOL:399-457`.

---

## 7. Item (7) — impossibility §4.1 and the count formulas. **CONFIRMED** / **GAP**

### 7.1 Bare-tuple obstruction

There is no function `U_Q(n,m,M_*,V_*,δ_*,u,v)` equal to the number of independent tame unknowns through order `Q` for every realisation of that skeleton. This is an **information obstruction**, not a slogan that “`k` is missing.”

The tuple supplies a capacity `∑_B V_2(B)≤u` (`SOL:474-476`), not an attained packet. The reviewed `D=105` row with `u=20`, `V_2=1` permits `k=20` and does not attain it (`TFE-R:18-19`, `I17:26`). A one-disc packet and a twenty-disc packet have different tail slots and different junction sharing. Even after `k` is supplied, the tuple does not determine the Galois-orbit partition, the cluster tree on `n` labelled leaves, coefficient sharing along ancestors, or the tame support semigroup. Level numbers `a_r=n V_{r+1}/d_{r+1}` along one distinguished chain are cluster sizes of a representative chain, not `FULL_ACTUAL_FIRST_SEPARATION` of the packet (`FALLACY-v2` carrier/attainment).

**The charge’s question: does a count exist as a function of the tuple plus `(k, orbit partition)`?** No. Those two decorations still omit the rooted tree, ancestor-sharing, and the support of tails. Different trees with the same `(k, orbits)` have different `|Z_Q|`. The exact input on which a closed count exists is the decorated skeleton `D_Q` of (4.3). Then the unknown count is a function of `D_Q`, not of the Moh tuple.

**Repair.** None for §4.1. Promote `SOL:461-514`. Optional strengthening: state explicitly that adjoining `(k, orbit partition)` is still insufficient.

### 7.2 Formulas (4.7)–(4.16)

`N_R(a,Q)=max(0,⌊Q/R⌋-⌈a/R⌉+1)` counts multiples of `R` in `[a,Q]`. Checked on mixed signs (`a=-4,Q=6,R=2` gives 6). `C_deg` and after-descent `C_poly` (dropping the already-monic `A_m`) are the right raw slot counts, and (4.11a) matches the specialisation (4.12):

```text
C(K)=h+(n-m)(K+1)+mK = h+(n-m)+nK.
```

Arithmetic identity verified on `(h,n,m,K)∈{(1,2,1,1),(1,15,5,3),(2,4,1,2)}`. `Q_count` in (4.15) is correctly typed as a counting bound, not a kill. The example system (below) is a witness that raw excess is not a kill.

**GAP at (4.13) vs (4.16).** `SOL:655-658` sets `U(Q)=h+u_0+|Z_Q|` with `u_0` the unspecialized leading/star parameters and `Z_Q` the tame symbols affecting equations through `Q`. `SOL:691-696` then uses the stationary model `|Z_K|=u_0+pK` and compares `C(K)=h+(n-m)+nK` to `U=h+u_0+pK`. That comparison is consistent with `U=h+|Z_K|`, not with `U=h+u_0+|Z_K|`. Using both sentences as written double-counts `u_0`. The first integer `K` at which `nK-pK > u_0-(n-m)` is correctly `⌊(u_0-(n-m))/(n-p)⌋+1` only for the second reading.

**Line repair for `SOL:655-658`.** Declare one convention: either `Z_Q` includes leading/star parameters and `U(Q)=h+|Z_Q|`, or `Z_Q` is tails only and `U(Q)=h+u_0+|Z_Q|` with `|Z_K|=pK` in the stationary model. Do not add `u_0` twice. Formula (4.16) can be promoted as a counting bound under the stationary support hypothesis after this repair.

The producer’s `OPEN[PACKET-COUNT-AUGMENTATION(Q)]` is well-posed and is left open: it is the finite enumeration from a bare tuple to decorations, bounded by `n L_Q` raw branch-tail slots before sharing (`SOL:905-913`).

---

## 8. Item (8) — quadratic lift (4.17). **CONFIRMED**

Prefix products `P_new=P_old·(τ_i-τ_j)`, inverse convolutions `D_i W_i=1`, integration `q h_{i,q}=-c R w_{i,q+R}`, powers, and evaluation `H_i=∑_{r=0}^m A_r τ_i^r` with `A_r` supported on (1.9) are an exact straight-line encoding. Every multiplication is bilinear. On the open set where first-separation leaders are nonzero, eliminating auxiliaries recovers the direct finite-order interpolation system. Conversely, the original products and interpolant realise the auxiliaries at their stated values. That is existential equivalence at the retained order, not a quadratic approximation of the eliminated ideal.

The integration identity is the chain rule: `x=z^{-R}`, `dH/dz=c W dx/dz=c W (-R z^{-R-1})`, hence `q h_q=-c R w_{q+R}` for `q≠0`. Matches `SOL:537-538` and the driver. Nonlinear input coefficients can raise equation degree above 2; the driver retains and flags them (`globalinterp.py:679-683`). The lift is quadratic in the auxiliaries when the displayed branch terms are linear in the tame symbols.

**Repair.** None. Promote `SOL:711-735` with the open-set qualification the driver already prints.

---

## 9. Item (9) — controls, composition reversion, two-tower `λ`, driver. **CONFIRMED**

### 9.1 Charged driver reruns

From the frozen `globalinterp.py`:

```text
controls: 40 checks, 0 failures
selftest: 50 checks, 0 failures
example, symbolic Jacobian:
  raw equations 36 / deduplicated 35
  unknowns 27 (integration_constant 1, inverse 8, polynomial_coefficient 2,
               prefix 8, time_value 8)
  degrees {1: 28, 2: 8}, all ≤ 2
  ambient symbolic Jacobian rank 26
```

These match `SOL:890-901`. Raw 36 exceeds 27 unknowns; rank 26 does not. Raw excess is not a kill.

Independent residue/interpolation checks, not relying on the driver’s `Checks` object:

- `(y,x+y^k)`, `k=3,5`: Jacobian `-1`; `[x^{-1}](1/g_y)=0` (series in `z=x^{-1/k}` has `[z^k]=0`); quotient interpolant recovers `y`; moments `μ_0=⋯=μ_{k-2}=0`, `μ_{k-1}=1`.
- `(y+x^2, x+(y+x^2)^2)`: Jacobian `-1`; two-node barycentric interpolant is `y+x^2`; `[z^2](1/(2√(c_2 z^2-1)/z))=0`.
- Sheared Moh-gauge form (5.2): `f=y+(x+y)^2`, `g=x+y+f^2`, Jacobian `-1`, `deg_y=(2,4)`, remainder interpolant recovers `f`, coefficients `(A_0,A_1,A_2,A_3)=(x^2,2x+1,1,0)`.
- Negative `g=y^2-x^2-x`: plus branch `[x^{-1}](1/(2√(x^2+x+c_2)))=1/2`, independently of `c_2`; series `z/2 - z^2/4 + (3/16-c_2/4)z^3+⋯` matches (5.6). Minus branch is the negative.

### 9.2 Composition (5.4)–(5.5) by direct reversion. **CONFIRMED**

On `g=c_2`, `y=c_2-u^3`, `x=u-(c_2-u^3)^5`. Set `x=t^{-15}`, `u=t^{-1} v(t)`, `v(0)=ω` with `ω^{15}=1`. The identity `(v^3-c_2 t^3)^5 + t^{14} v =1` is solved coefficient-wise. At `ω=1`:

```text
v = 1 + (c_2/3) t^3 - (c_2^2/9) t^6 + (5 c_2^3/81) t^9
    - (10 c_2^4/243) t^{12} - (1/15) t^{14} + ⋯
y = c_2 - t^{-3} v^3 = - t^{-3} + (1/5) t^{11} + O(t^{12}),
```

with **no** intermediate `y`-coefficient between `t^{-3}` and `t^{11}`, including for generic `c_2` (the `c_2` terms in `v` cancel in `y`). For general `ω`, `β=ω^3`, the same calculation gives

```text
τ_{β,ω} = -β t^{-3} + ω/(5 β^4) t^{11} + higher,     (5.4)
```

and `ω/(5β^4)=ω^4/5`, matching the `ω=1` value `1/5`. Cubing `μ_{15}→μ_5` has image 5 and kernel 3: five bottom discs indexed by `β^5=1`, three branches per disc. The order-three subgroup `ω↦ζ_3 ω` stabilizes a disc. The driver’s “five discs” check (`globalinterp.py:1153-1161`) is only the cyclic set `{(3k) mod 15}` of size 5; it does not revert. The mathematics of (5.4) is confirmed by reversion, not by that proxy.

Differentiating the inverse: `X'(u)=1+15 u^2 (c_2-u^3)^4`, so `1/g_y=1/X'`. At `ω=1`,

```text
[t^{14}](1/X')=1/15,   [t^{15}]=[x^{-1}]=0,   [t^{16}]=0,   [t^{17}]=-2 c_2/45.
```

Thus (5.5) holds, and `O(x^{-17/15})` is sharp for generic `c_2`. Residue zero is exact.

### 9.3 Two-tower `λ` table. **CONFIRMED**

`lambda_h^{(σ)}(δ)=∑_j min(δ, ord_t(σ-h_j))` over **all** roots `h_j`, including the self-term `min(δ,∞)=δ` for `h=g` when `σ` is a `g`-root. `control4.py:71-73` drops that self-term. Restoring it on the seven NOTT pairs:

| row | `δ_1` | `λ_f` | `λ_g` corr. | sum | `δ_1-1` | `deg W` | Keller? | (ORD)? |
|---:|---|---|---|---|---|---:|---|---|
| 0 | `-1/2` | `-3/2` | `-2` | `-7/2` | `-3/2` | 2 | no | fails |
| 1 | `-1/2` | `-2` | `-3` | `-5` | `-3/2` | 3 | no | fails |
| 2 | `-2/3` | `-10/3` | `-3` | `-19/3` | `-5/3` | 4 | no | fails |
| 3 | `-1/2` | `-5/2` | `-3` | `-11/2` | `-3/2` | 2 | no | fails |
| 4 | `-1/3` | `-3` | `-2` | `-5` | `-4/3` | 2 | no | fails |
| 5 | `-1/2` | `-3` | `-4` | `-7` | `-3/2` | 5 | no | fails |
| 6 | `-1/3` | `-3` | `-4` | `-7` | `-4/3` | 2 | no | fails |

This is exactly `TFE-R:735-743` and `SOL:845-848`. Bottom-bracket degrees `2,3,4,2,2,5,2`. All seven fail order matching; all seven are non-Keller. They disprove the supplied pairs, not the existence of some other mate, which is the qualification `SOL:850-851` already makes.

---

## 10. FALLACY-v2 audit

- **Flag/place/series.** Branches `τ_i`, bottom discs, tree vertices, and completed-chart series are kept distinct. A representative Moh chain is not treated as the full packet.
- **Carrier/attainment and floor/attainment.** `∑_B V_2(B)≤u` is a cap. `k=20` is not asserted attained. `Q_count` is a counting bound, not a kill.
- **Galois/orbit charge.** Only a declared complete orbit is traced. Distinct invariant orbit contributions remain coupled; the extra control in §5.2 is a witness.
- **Raw remainder and rings.** Base `C(s)((z))`, `x=z^{-R}`. Unit leaders are inequations. The quadratic lift is existential. No `sat()`.
- **Prime/derivative.** `p_g'` is `d/dπ`; `F_i'` is `d/dx`.
- **Variable/ring map.** Declared in §0. Matching names are not a proof.
- No exit-price assertion, so no `charge_basis` line.

---

## OPENS RAISED

- `OPEN[KELLER-TWO-LOCAL-ORBITS]`. Existence of a Keller pair whose generic `g`-fibre has at least two local Galois orbits of Puiseux branches at `x=∞`. Bound: 0 known examples; the set is empty in `Aut(C^2)`, because `X(u,c_2)-x` has a unique Newton segment of length `n=deg_u X`. A non-automorphism Keller pair is a Jacobian-conjecture hypothetical, not a desk example.

- `OPEN[U0-Z-SPLIT]`. Which of the two readings of `U(Q)` in (4.13) versus (4.16) is intended. Bound: the two readings differ by the integer `u_0`, and `u_0` is at most the number of unspecialized leading/star parameters of the decorated skeleton (finite, at most `n` plus the number of free star coefficients of the packet).

## OPENS UNTOUCHED

- `OPEN[PACKET-COUNT-AUGMENTATION(Q)]` (producer). Left open at the bound already stated: at most `n L_Q` raw branch-tail slots before sharing, once the finite decoration is supplied.

---

## 12. Typed verdict block

```text
REVIEWED INPUT
  JAC-FIBRE; D1-PIN; LOCAL-KELLER; BOTTOM-ODE as a reviewed local block;
  TFE-R correction of the two-tower lambda table (self-root restored).

CONFIRMED / CAN PROMOTE
  (1.3), (1.5), (1.6), (1.8); n-m-1 high-degree vanishings plus one monic;
  support test (1.9)-(1.11); exact tree factorisation (2.1)-(2.2);
  (2.5), (2.6), and "Galois does not kill integer-order coefficients";
  (3.2) and computational independence of NO-RESIDUE in the Puiseux-field
  implementation; information obstruction §4.1; (4.7)-(4.12), (4.15) as
  raw/counting-bound formulae; existential quadratic lift on the
  nonzero-separation open set; automorphism and g-alone controls;
  composition (5.4)-(5.5) by direct reversion; two-tower lambda table
  with bracket degrees 2,3,4,2,2,5,2; driver 40/0, 50/0, example rank 26.

CONFIRMED WITH REPAIR
  (2.4): one free constant per finite Galois orbit; NO-RESIDUE is for
  primitives in K, not for the count; averaging does not need the full μ_R.

GAP / REPAIR BEFORE PROMOTING THE SENTENCE
  (4.13) U(Q)=h+u_0+|Z_Q| versus (4.16) U=h+u_0+pK: do not add u_0 twice.
  Driver composition "five discs" check is combinatorial, not a reversion
  (the reversion itself CONFIRMED independently).
  Requested extra Keller two-orbit control: empty in Aut(C^2); coupling
  exhibited on f=y, g=(y^2-x)(y^2-4x) and on a two-orbit emitter decoration.

COUNTING-BOUND ONLY
  Q_count is the first possible raw excess. The example has 36 lifted
  equations, 27 unknowns, rank 26: raw excess is not a kill.

NOT CLAIMED / NOT PROMOTED
  sufficiency from one numerical target; attainment of a Moh packet;
  a skeleton-only unknown count; a count as a function of the tuple plus
  only (k, orbit partition); independence of raw equations.

OPENS
  OPEN[PACKET-COUNT-AUGMENTATION(Q)] (producer; ≤ n L_Q raw slots);
  OPEN[KELLER-TWO-LOCAL-ORBITS] (0 known; empty in Aut(C^2));
  OPEN[U0-Z-SPLIT] (the two U(Q) readings differ by u_0).
```

No `charge_basis` line: no new exit-price assertion.

<!-- BODY-END -->

