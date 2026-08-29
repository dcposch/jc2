# Hostile review: upper-endpoint origin odd-coupling lemma

Date: 2026-08-28
Reviewer: Fable 5 (compact independent hostile audit)
Verdict: **PASS** (no defect found; one non-blocking precision note, §7)

## 0. Frozen target (verified at start and end of the audit run)

| file | sha256 |
|---|---|
| `xmodel/ggv-upper-endpoint-origin-odd-coupling-sol-ultra-20260828.md` | `3e4a0f03acec2ee5e3cdfff558c481e14735408aa18486d23215958ed8d4bb3a` |
| `cases/ggv_8_28_upper_endpoint_origin_odd_coupling_20260828/verify_origin_odd_coupling.py` | `f23a6d959dc9a8854f051c16a1fe287dea91d5b66b01a63198a64715c08c04c8` |
| `cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json` | `28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876` |

The producer checker was **not** imported, executed, or trusted. Everything
below was rebuilt from the frozen `RAW_INPUT.json` and first principles by a
fresh standard-library checker,
`xmodel/ggv-upper-endpoint-origin-odd-coupling-hostile-review-fable5-20260828-check.py`,
run as `PYTHONDONTWRITEBYTECODE=1 python3 -B ...` from the repo root.
Replay marker: `PASS_HOSTILE_AUDIT_UPPER_ENDPOINT_ORIGIN_ODD_COUPLING_FABLE5`.

## 1. Raw slots and the upper-chart map — CONFIRMED

All 442 authoritative slots (141 F + 301 G in
`raw_slots_through_weight_22`) were re-parsed. For every slot the audit
verified: slot name `f_i_j`/`g_i_j` matches `raw_exponents`; the raw
monomial string matches; both exponents are nonnegative; and the chart map
`X = x*y^3`, `t = 1/y` holds literally — a weight-`w` F-slot `X^i` is
`x^i y^(8+3i-w)` and a G-slot is `x^i y^(12+3i-w)` (equivalently
`x^i y^j -> t^(8+3i-j) X^i`, resp. `t^(12+3i-j) X^i`, matching the frozen
`maps` strings byte-for-byte).

Window census (recomputed, not copied): the F slots at weight `w` are
exactly the contiguous range `max(0, ceil((w-8)/3)) <= i <= 16-w`
(nonempty for `w = 0..14`), and the G slots exactly
`max(0, ceil((w-12)/3)) <= i <= 24-w` (nonempty for `w = 0..21`). No slot
exists outside these windows through weight 22. The boundary facts the
`n = 22` enumeration needs were read directly off the frozen data:
`F_a[X1]` exists iff `a <= 11`, `F_a[X0]` iff `a <= 8`, `G_b[X0]` iff
`b <= 12`, `G_b[X1]` iff `b <= 15` (presence at 11/8/12/15 and absence at
12/9/13/16 each checked explicitly).

## 2. Complete literal enumeration of `D22[X0]` — CONFIRMED

Starting from `D_n = sum_{i+j=n} ((12-j) F_i' G_j + (i-8) F_i G_j')`, the
audit built each weight component `F_a(X)`, `G_b(X)` symbolically from the
frozen slot lists, applied the exact `X`-derivative (including the degree
factor `k` on `X^k -> k X^(k-1)`; the surviving contributions come from
`X^1 -> 1·X^0`, factor 1), took full symbolic products, and extracted the
`X^0` coefficient over **all** pairs `a + b = 22`, `0 <= a <= 22`. Result,
as a bilinear form in the slot variables:

```text
D22[X0] = +f_1_0*g_0_1 - f_0_1*g_1_0
        = +F11[X1]*G11[X0] - F7[X0]*G15[X1],
```

exactly the report's equation (1), signs and ordering derived
independently.

## 3. Neighbor audit — CONFIRMED

For the `(12-j) F_a' G_b` term the slot windows force `a in {10, 11}`;
`(10,12)` has both required slots but prefactor `12-j = 0` (structural
zero), leaving `(11,11)` with coefficient `12-11 = +1`. For the
`(i-8) F_a G_b'` term the windows force `a in {7, 8}`; `(8,14)` has both
slots but prefactor `i-8 = 0`, leaving `(7,15)` with coefficient
`7-8 = -1`. The checker classified every pair `a+b=22`: exactly two
contributors, exactly the two prefactor kills above, and every remaining
pair lacks at least one required `X0`/`X1` slot in the frozen data.

## 4. Slot identification and the Jacobian — CONFIRMED, target `+1`

From the frozen slot table: `F11[X1] = f_1_0` (raw monomial `x^1 y^0`),
`F7[X0] = f_0_1` (`x^0 y^1`), `G15[X1] = g_1_0`, `G11[X0] = g_0_1` — i.e.
the four original-coordinate linear coefficients `P_x(0), P_y(0), Q_x(0),
Q_y(0)`, uniquely (no other slot carries those monomials). Hence
`D22[X0] = P_x Q_y - P_y Q_x |_(0,0) = J(P,Q)(0)` literally.

The endpoint sign convention was re-derived, not assumed. With
`F(t,X) = t^8 P(X t^3, 1/t)`, `G(t,X) = t^12 Q(X t^3, 1/t)` and the chart
Jacobian `det d(x,y)/d(X,t) = -t`, one gets the exact Laurent identity

```text
sum_n D_n t^(n-21) = t * J_{x,y}(P,Q)(X t^3, 1/t),
```

verified by the checker over exact `Fraction` arithmetic on a generic
mixed-parity integer pair. Consequently Keller `J(P,Q) = +1` forces
`D_22 = +1` and every other `D_n = 0`; the checker confirms this on the
fixtures `(P,Q) = (x, y)` and `(x + y^3, y)`. **The target is `+1`, not
`-1`.**

## 5. Parity theorem — CONFIRMED

Every frozen slot satisfies `i + j = base + 4i - w ≡ w (mod 2)` (checked
for all 442). The four coupling slots carry odd raw weights
`(11, 7, 15, 11)`. If every odd-raw-weight coefficient vanishes, the
surviving (even-weight) slots all have even total degree, so `P` and `Q`
are invariant under `(x,y) -> (-x,-y)`; no degree-1 monomial survives, so
both gradients vanish at the origin; and restricting the §2 bilinear form
to even-weight slots gives identically `0`. Hence `D22[X0] = 0` on the
all-odd-weight-zero section, contradicting the target `D22 = +1`: **the
section is empty at the raw endpoint.**

## 6. Mutation grid — all 7 detected

Each mutation was injected into the fresh checker's own pipeline and each
one flips a check to FAIL: (a) sign flip on the `(7,15)` term; (b)
retaining the structural zero `(10,12)`; (c) retaining `(8,14)`; (d)
omitting the true `(7,15)` term; (e) wrong chart offset (`8 -> 9` in the
slot/weight map — slot verification fails on the first slot); (f) parity
law flipped to `w+1 mod 2`; (g) endpoint target asserted as `-1` (refuted
by the exact Keller fixture).

## 7. Firewall — adequate; no precision repair required

Item audited: does the report ever assert the converse "all odd de Rham
q-gates vanish ⟹ all odd raw-weight coefficients vanish"? It does not.
The only sentence touching the direction is §1's "It is not a survivor
merely because every odd de Rham gate vanishes there," which asserts the
*correct* direction (gate vanishing does not rescue the section). §3
explicitly labels the gate-to-raw inference "tempting but false," and §5
states "The lemma alone does not show that the intersection is empty. It
proves no endpoint exclusion, other-branch result, Keller theorem, or
JC2." All four firewall sentences are pinned byte-exactly by the checker
against the frozen report. Non-blocking note: §1's phrase "supplies the
smallest exact coupling between the reviewed q5–q15 odd fiber and the
endpoint target" could, read in isolation, suggest the fiber intersection
is already resolved; §5's explicit disclaimer removes the ambiguity, so
this is a style note, not a repair.

The lemma's scope is exactly: the raw all-odd-weight-zero section is
incompatible with `D22 = +1`. It does not by itself prove the q5–q15
fiber intersection empty, endpoint exclusion, Keller, or JC2.

## 8. Verdict

**PASS.** Every audited claim of the frozen report — chart map, window
census, complete `D22[X0]` enumeration, neighbor kills, slot/Jacobian
identification, `+1` target convention, and the parity emptiness theorem —
was independently reconfirmed by exact standard-library computation, with
all seven mutation controls detected and all three frozen hashes intact
at start and end. No defect found.

Evidence directory:
`cases/ggv_8_28_upper_endpoint_origin_odd_coupling_hostile_review_fable5_20260828/`.
