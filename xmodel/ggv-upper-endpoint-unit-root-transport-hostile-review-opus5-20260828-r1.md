# Hostile review: unit-root transport to the `D22` endpoint

Reviewer: Opus 5, independent hostile lane
Date: 2026-08-28
Charged report:
`xmodel/ggv-upper-endpoint-unit-root-transport-sol-ultra-20260828.md`
Charged packet:
`cases/ggv_8_28_upper_endpoint_unit_root_transport_20260828/`
Reviewer checker:
`cases/ggv_8_28_upper_endpoint_unit_root_transport_review_opus5_20260828/verify_unit_root_transport_review_opus5.py`

## Verdict

# `REPAIR`

The **mathematical conclusion is true**, and I have proved it independently:
under the reviewed reduced branch-P prefix and complete mode schedule, a
*simple* root `alpha` of `A` with `V0(alpha) != 0` is impossible at the
endpoint.  I rebuilt the entire local ladder `D7 --> D22` from the general
pre-`D7` prefix in my own Laurent ring and obtained `ord_alpha(g22) >= -2`
and `D22_raw in (X-alpha)` with no producer import.

The **charged statement is overstated and its central bridging claim is
false as written**, on three points that a promotion must not inherit:

1. Section 2's assertion that the normalized prefix `(6)` "is exactly the
   reviewed fixed prefix in the local coefficient ring" is **false**.  `(6)`
   carries `Fbar_3=(Zbar+A*Tbar)/8` with `A^1`; the recursively pinned fixed
   cascade starts from `F3=(z+A^2*v)/8` with `A^2`, and from
   `F4=v/16+z^2/64+A^2*r`.  The pinned cascade begins *after* `D7`--`D15`.
2. The verdict clause "This uses neither q1 nor the provisional D9 repair" is
   half wrong.  The `q1` half is correct.  The `D9` half is not: the pinned
   cascade's starting normal form **is** the `D7` conclusion `A|T` and the
   `D9` conclusion `A|W`, and the local rungs `D7`, `D8`, `D9` at `alpha` are
   genuinely used.  What is legitimately avoided is the *global* `A|T`
   theorem with its `C`-root / `-8B^4U^3` argument.
3. The one new load-bearing step -- localizing `D7`--`D15` from the general
   `V0` prefix -- is asserted in one sentence of Section 3 with no derivation,
   no displayed polar form, no pinned source, and no line of checker support.
   I supply it (checker `S7`); each of the five rungs is load-bearing
   (checker `S7m`).

Separately, the charged checker is **tautological on precisely the
load-bearing items** and must not be cited as evidence for the bridge
(Section 6 below).

The repaired theorem I certify is stated in Section 2.  It is in two
respects *stronger* than the charged one (squarefreeness of all of `A` is not
needed, and absence of a raw `G22` receiver is not needed) and in one
respect *weaker* (the `D7`/`D8`/`D9` local rungs are consumed).

## Frozen input hashes

All seven charged hashes match the live bytes, and both pin files verify.

```text
98f5e97d570e4d73f4824888731162eb63588e51edfba8cff9c309fae619005f  xmodel/ggv-upper-endpoint-unit-root-transport-sol-ultra-20260828.md
48d5393afff34c02925566413da07cf3578a7045413e44aa85060ebbf0ee2412  verify_unit_root_transport.py
22c4ad5065cd22635c96816c118f7981c1da4235d3b27c93aee550f4ae959903  RESULT.json
fbe61174523d4650df006dbc5ce2bf3885130e16b506da7e276cf55ea78af2b8  TARGET.json
203aa3482192126f3079ec90af98ce1a98c54e23cdc07cdaac659b6fefe2515f  README.md
538d8b8c784d17f0544a94abba3742f880abef080122d4610cadf6bdec972e21  SOURCE.sha256
d51bd6e1797ab3b7811f35ca187ae8a3a9514d8ea61d2dbb22b1c0eeac465eb4  EVIDENCE.sha256
```

`shasum -a 256 -c SOURCE.sha256` -> 11/11 OK (all ten recursive pins).
`shasum -a 256 -c EVIDENCE.sha256` -> 4/4 OK.

Additional bytes I pinned myself (not in the charged `SOURCE.sha256`):

```text
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0  cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
8ebe5f4f099e6cf15b0a4703dfb348aa6cc72df8fdbc60b1d095925fa3746d21  cases/ggv_8_28_upper_endpoint_uniform_d10_fullmodes_audit_20260828/verify_uniform_d10.py
```

The second is the base desk that defines `common_F_prefix`, `continuation`,
`la_operator`, and `MODES`.  **It is the object the charged Section 2 claims
to match and it is not pinned by the charged packet** -- the charged
`SOURCE.sha256` reaches it only transitively through the `D18`--`D22`
checker's `PREDECESSOR` chain.

My checker's hash:

```text
cbf8498e77c639ebb08cda6c9f02a849e0b40f32c680cad4fe1120d30b6c9b6b  cases/ggv_8_28_upper_endpoint_unit_root_transport_review_opus5_20260828/verify_unit_root_transport_review_opus5.py
```

---

## 1. What the object actually is (reconstructed, not quoted)

The authoritative raw system serializes the row operator

```text
D_n = sum_(i+j=n) ( (12-j) F_i' G_j + (i-8) F_i G_j' ),      ' = d/dX.
```

Summing against `t^n` and writing `theta = t d/dt` this is the single PDE

```text
D = 12 F_X G - F_X (theta G) + (theta F) G_X - 8 F G_X.
```

Two facts follow by direct differentiation, and I verified both symbolically
in a free differential ring (`S6`):

* `G = F^(3/2)` gives `D = 0` identically;
* `G = c(X) t^m F^beta` gives `D = c'(X) t^m F^beta (theta F - 8F)`, which
  vanishes **iff** `12 - m - 8beta = 0` **and** `c' = 0`.

So the indicial exponents are `beta_m=(12-m)/8`, the mode is rational only
for even `m` (else `A^((12-m)/2)` is not in the field), and **the mode
coefficients `c_m` are forced to be ground-field constants by the raw row
itself**.  The `j = n` block of `D_n` is exactly

```text
L_n(R) = 4(12-n) A^3 A' R - 8 A^4 R',        ker L_n = K * A^((12-n)/2),
```

verified for `n = 4..22`.  Hence `D_n = 0` for `n <= 21` with `G_0 = A^6`
pins

```text
G = F^(3/2) + sum_(m in {4,6,...,20}) c_m t^m F^((12-m)/8) + O(t^22),
```

and, since the row is linear in `G_22` with block `L_22`,

```text
D22 = L22(G22 - g22)   for ANY G22;   with G22 absent, D22 = -L22(g22).
```

Raw fixture facts I re-read from the frozen JSON (`S2`): 303 variables, 513
generators, `A=X^4-1`, `F1=H=A^2`, `c2=0`, charged zero rows `D7..D21`,
affine target row 22 value `1`, `D23` not imposed, no `G22` and no `F22`
window, `G18..G21` windows of dimensions `5,3,2,1` at degrees
`2..6, 3..5, 3..4, 3..3`.  The single `x_degree = 0` generator of row 22
carries the constant `-1`, confirming the target sign `+1`.

---

## 2. The repaired theorem

> **Theorem (certified).**  Let `K` have characteristic zero and let
> `L/K` be an extension.  Suppose given the reduced branch-P data
> ```text
> F0 = A^4,  F1 = A^2 V0,  F2 = (V0^2 + A^2 Z)/4,  F3 = (V0 Z + A T)/8,
> F4,...,F14  and  G0 = A^6, G1,...,G21   all polynomial,
> ```
> with the branch-P condition (`c2 = 0` or `A | V0`), satisfying
> `D7 = ... = D21 = 0` and `D22 = 1`.
> Let `alpha in L` be a **simple** root of `A` at which `V0(alpha) != 0`.
> Then no such data exist.
>
> The conclusion also holds if a *regular-at-`alpha`* raw receiver `G22` is
> present; and it does not require `A` to be squarefree away from `alpha`.
>
> **Corollary** (this one *does* need `A` squarefree): with
> `C = gcd(A,V0)`, every stratum with `C != A` is field-point empty at the
> endpoint, because every root of `B = A/C` is then a simple root of `A`
> with `V0 != 0`.

Everything is *field-valued/geometric*.  Two steps fail over a ring with
nilpotents -- "`ord(Delta^2) >= 1  =>  ord(Delta) >= 1`" and "a nonzero
scalar is a unit" -- so this is **not** scheme-theoretic emptiness, exactly
as the charged scope firewall says.

Note that `c2 = 0` is **automatic**: the branch-P alternative is `A | V0`,
which `V0(alpha) != 0` excludes.  The same hypothesis that powers the
theorem kills the deepest mode.  The charged report does not say this; it
should, because a live `c2` (indicial `5/4`) would put `g22` at `A^-35`.

---

## 3. Claim-by-claim table

Labels: `EXACT-OPUS` = I recomputed the exact object; `DERIVED-OPUS` =
I proved it from recomputed objects; `REPLAY-ONLY` = I checked only bytes /
consequences; `UNPROVED` = asserted by the producer and not established
by the charged artifact.

| # | Charged claim | Verdict | Label |
|---|---|---|---|
| 1 | Newton identity (1) `H = Q^2 + eps^2(...) + eps^3 aTs^3/8 + sum eps^(2i-4)F_i s^i` | correct, exact | `EXACT-OPUS` |
| 2 | Leading square (2) `H(0,s) = (A'(a)^2 + V0(a)s/2)^2` | correct | `EXACT-OPUS` |
| 3 | Coefficient comparison (3) `(F^b)_k = eps^(4b-2k)[s^k]H^b` | correct; equivalent to `ord_alpha(P_k) >= 2k` in the exact form `(F^b)_k = A^(4b-4k)P_k` | `EXACT-OPUS` |
| 4 | Mode valuation (4) `ord >= 6+3m/2-2n` | correct as a **bound**; sharp exactly when `C(2b,k) != 0` | `EXACT-OPUS` |
| 5 | Mode/pole table `c6@8,c10@11,c14@14 -> -1; c16 -> -2; c18 -> -3; c20 -> -4`, coefficients `3/32, 1/4, 1, 1, 1, 1` | correct; I also verified the general-parameter law `C(2b,k) a0^(4b-2k) (v0/2)^k` at `a0=-4, v0=8` | `EXACT-OPUS` |
| 6 | Normalization `Fbar_i=nu^-i F_i => gbar_n=nu^-n g_n` for all nine modes and the principal branch | correct; verified by *running* the recurrence twice at 3 rational points x 10 exponents x weights 0..22 | `EXACT-OPUS` |
| 7 | "`(6)` is exactly the reviewed fixed prefix in the local coefficient ring" | **FALSE**: `(6)` has `A^1` in `Fbar_3`; the pinned prefix has `A^2` (and `A^2` in `F4`) | `EXACT-OPUS` (refuted) |
| 8 | "the reviewed fixed cascade ... never differentiates `cbar_m`" | true of the emptiness proof; **false** of the pinned packet's linked-mode firewall assertions, which differentiate `c18`,`c20` as constants | `EXACT-OPUS` |
| 9 | "(5) is not asserted to be a symmetry of the raw determinant equation" | correct and necessary: a non-constant mode coefficient is **not** a raw solution (`D = c' t^m F^b(theta F - 8F) != 0`) | `EXACT-OPUS` |
| 10 | "D7--D15 ... the local ladder is therefore the same one" | **true but not delivered**: no derivation, no polar form, no pin, no checker line.  I prove it in `S7` | was `UNPROVED`, now `DERIVED-OPUS` |
| 11 | `D16`/`D17` local quotients `M,N`; no square-root sheet | correct | `EXACT-OPUS` |
| 12 | `D18`--`D21` local quotients `O,P,S,U`; `c18`,`c20` killed at birth | correct | `EXACT-OPUS` |
| 13 | `g22 = qbar + Wbar/A^2`, i.e. `ord_alpha(g22) >= -2` | correct: A-exponent support `{-2,0,2,4,6,8}` | `EXACT-OPUS` |
| 14 | `D22_raw = -L22(g22)`, `L22(R) = -40A^3A'R - 8A^4R'` | correct; sign and coefficients confirmed from the serialized row operator | `EXACT-OPUS` |
| 15 | `L22(c22 A^-5) = 0` | correct, exact | `EXACT-OPUS` |
| 16 | `ord >= -2  =>  D22_raw in (X-alpha)`, contradicting `D22=1` | correct (432 terms, min A-exponent 1) | `EXACT-OPUS` |
| 17 | "independent of q1" | correct: `q1` only parameterizes `V0`; nothing local uses it | `DERIVED-OPUS` |
| 18 | "does not use the provisional D9 repair" | **overstated**: the local `D7`,`D8`,`D9` rungs *are* used; only the global `A|T` theorem is avoided | `EXACT-OPUS` (refuted as stated) |
| 19 | Every `C != A` stratum is field-point empty | correct, **given `A` squarefree** (needed to make `B`-roots simple `V0`-unit roots of `A`) | `DERIVED-OPUS` |
| 20 | D12 fixture: `gcd(B,V0)=gcd(B,Nred)=gcd(B,B')=1`, exact order-2 pole at all three `B`-roots, `A'(-1)=-4, V0(-1)=8, C(-1)=-2, H(0,s)=(16+4s)^2, Nred(-1)=-3969/4096` | all correct and recomputed; `Nred` itself is `REPLAY-ONLY` | `EXACT-OPUS` / `REPLAY-ONLY` |
| 21 | Charged checker "verifies ... recurrence and mode scaling through weight 22 ... the endpoint order/kernel calculation" | the cited assertions are integer tautologies; `g22_order >= -2` is a **literal string** in `RESULT.json` | `EXACT-OPUS` (refuted) |
| 22 | Not a raw-normal-form landing / coverage / Keller / JC2 | correct, and I add nothing to it | `DERIVED-OPUS` |

---

## 4. The `D7`--`D21` dependency ledger

Notation: `nu = V0`, all objects in the DVR `O = O_alpha` with uniformizer
`eps = X - alpha`; bars dropped.  `Delta_n := F_n - (base_n)` and
`K := 64F4 - Z^2`.  Every "polar form" below was computed by my own Laurent
ring from the **general** prefix (checker `S7`); none is quoted.

| row | polar form I recomputed | what the row consumes | new local object |
|---|---|---|---|
| `D7` | `polar(g7) = 3T(AK-2T)/(2048 A^2)` | regularity + `ord(A)=1` | `ord(T)>=1`, **`V := T/A`** |
| `D8`a | `polar(g8) = (3/8)(F4-V/16-Z^2/64)^2/A^2 + (3/32)c6/A` | regularity + DVR square root `ord(D^2)>=1 => ord(D)>=1` | `W0 := F4-V/16-Z^2/64`, `ord(W0)>=1` |
| `D8`b | same row, `A^1` class | **scalar constancy of `c6`** | `c6 = 0` |
| `D9` | `-3W^2/(16A^2) + (3/4)F5 W/A - (3/256)VWZ/A` | regularity + DVR square root | `ord(W)>=1`, **`R := W/A`** |
| `D10` | `(3/8)Delta5^2/A^2`, `Delta5=F5-R/2-ZV/64` | regularity + DVR square root | `ord(Delta5)>=1` |
| `D11` | `-3S^2/(16A^2) + A^-1(...) + c10/(4A)` | square root, then **scalar constancy of `c10`** | **`Q := S/A`**, `c10=0` |
| `D12` | `(3/8)Delta6^2/A^2`, `Delta6=F6-Q/2-RZ/8-V^2/256` | regularity + DVR square root | `ord(Delta6)>=1` |
| `D13` | `-3T1^2/(16A^2) + O(A^-1)` | regularity + DVR square root | **`T := T1/A`** (`F6` quotient) |
| `D14` | odd class is exactly `c14/A`; even class carries `(3/8)Delta7^2/A^2` | square root, then **scalar constancy of `c14`** | `ord(Delta7)>=1`, `c14=0` |
| `D15` | `-3Y1^2/(16A^2) + O(A^-1)` | regularity + DVR square root | **`Y := Y1/A`** (`F7` quotient) |
| `D16` | `(3B^2/8 + c8 B/2 + c16)/A^2` | regularity only | **`M := (3B^2+4c8B+8c16)/(8A^2)`** |
| `D17` | `((3B+2c8)C/4 - M/2)/A^2` | regularity only | **`N := ((3B+2c8)C-2M)/(4A^2)`** |
| `D18`a | `c18/A^3 + P18/A^2` | reduce mod `A`; **scalar constancy of `c18`** | `c18=0` |
| `D18`b | remaining `A^-2` class | regularity only | **`O := P18/A^2`** |
| `D19` | `P19/A^2` | regularity only | **`P := P19/A^2`** |
| `D20`a | `c20/A^4 + P20/A^2` | reduce mod `A`; **scalar constancy of `c20`** | `c20=0` |
| `D20`b | remaining `A^-2` class | regularity only | **`S := P20/A^2`** |
| `D21` | `P21/A^2` | regularity only | **`U := P21/A^2`** |
| `D22` | support `{-2,0,2,4,6,8}` | -- | `ord_alpha(g22) >= -2` |

**First failing dependency: none.**  Every row uses only

* `ord_alpha(G_n) >= 0` (weaker than global polynomiality),
* `ord_alpha(A) = 1` (simplicity of `alpha`),
* integrality of the valuation (`2 ord(D) >= 1 => ord(D) >= 1`),
* "a nonzero element of the constant field has order `0`".

No row uses a global degree, a rank, a value at a second root, an `X`
derivative of a quotient or of a mode, a square-root sheet, or algebraic
closure beyond adjoining `alpha`.  **Replacing the global quotient
polynomials by DVR elements is therefore legitimate at every row**: each is
introduced only after an order inequality that localizes, and is thereafter
used only additively/multiplicatively inside further order bookkeeping.
(They *are* differentiated once, inside `L22(g22)` at the endpoint; that
lowers order by at most one, which the `k+3` margin absorbs.)

Two ledger corrections to the charged Section 3:

* the named-quotient list `R,Q,T,Y,M,N,O,P,S,U` is **missing `V = T/A`** --
  the very first quotient, created by the `D7` rung the report skips.  With
  `V` there are eleven, not ten.
* the surviving modes are `c4, c8, c12, c16`, and they survive for two
  *different* reasons, which the report does not distinguish:
  `c4` and `c12` have `2beta in {2,0}` so `C(2beta,k) = 0` for `k > 2beta`
  and their mode series `(F^1)_k = F_k`, `(F^0)_k = delta_{k0}` are
  **regular at every weight** -- they are never polar and can never be
  killed; `c8` and `c16` *are* polar (from weight 13 and 16) but never
  form the unique deepest class, so they are absorbed into the `D16`
  relation `3B^2+4c8B+8c16 = 8A^2 M` rather than killed.

### Load-bearing mutations of the ladder (checker `S7m`)

Dropping any single prefix rung deepens the polar order of `g16` from `-2`:

```text
baseline            -2
skip D7  (F3 A^1)  -20
skip D9  (F4 A^1)  -16
skip D11 (F5 A^1)  -12
skip D13 (F6 A^1)   -8
skip D15 (F7 A^1)   -4
```

Retaining `c18` at `D18` leaves exactly `c18/A^3` after its quotient
relation, so the polar part does not clear.

---

## 5. Normalization algebra (charged item 2)

`Fbar_i = nu^-i F_i`, `gbar_n = nu^-n g_n`, `cbar_m = nu^-m c_m` is the
substitution `t -> t/nu(X)`.  I verified `gbar_n = nu^-n g_n` by **running**
the recurrence on genuinely different data (3 rational points, 10 exponents,
weights `0..22`), and the mutation `Fbar_i = nu^-(i-1)F_i` fails at all 570
nontrivial checks.

Answers to the four charged questions:

* **Does the fixed proof need `cbar_m` to be a ground-field scalar?**  No,
  and it must not: `cbar_m = nu^-m c_m` is a local function.  What the proof
  needs is that the **unnormalized** `c_m` is a scalar, which is *forced by
  the raw row* (Section 1), and that `nu` is a unit so
  `ord_alpha(cbar_m) = ord_alpha(c_m)`.  Every mode kill then reads
  `ord_alpha(c_m) >= 1` and concludes `c_m = 0`.  This is sound.
* **Does it differentiate `cbar_m`?**  The emptiness proof does not.  But
  the recursively pinned `verify_uniform_d18_d22.py` *does* differentiate
  `c18`/`c20` (as constants, via `la_derivative` with no entry in
  `DERIVATIVES`) in its `linked_mode_firewalls`.  Those assertions do **not**
  survive the normalization and would be false for `cbar_m`.  They are
  robustness statements ("the kill happens at the birth row, not the
  successor"), not premises, so the theorem is unaffected -- but the charged
  sentence "It never differentiates `cbar_m`" is true only of the subset of
  the pinned packet that the proof actually consumes, and should say so.
* **Does it compare `cbar_m` at another root?**  No.  My ladder never
  evaluates anything at a second root.  (The pinned `D16`/`D17` packet does
  record a per-root quadratic `Bhat(alpha)^2 = -8 J16/3` "at every alpha with
  `A(alpha)=0`"; that is a consequence, not an input, and is not used here.)
* **Does it transport a raw determinant equation under `t -> t/nu`?**  No,
  and the firewall is necessary.  The raw row is **not** invariant: an easy
  computation gives, for the pulled-back data,
  `D_new = D_pullback + (nu'/nu)(8 Fbar theta Gbar - 12 (theta Fbar) Gbar)`,
  and correspondingly a non-constant mode coefficient is not a raw solution
  (checker `S6`, live mutation).  The charged report is right to do the
  endpoint in the original coordinates.

**Assessment of the normalization's role.**  Because it is used only through
`ord_alpha(nu) = 0`, the normalization is *cosmetic*: it makes `Fbar_1 = A^2`
and `Fbar_2 = (1+A^2 Zbar)/4` so the pinned symbols can be reused, but it
does not by itself import anything.  The bridge still has to re-run the
ladder, which is exactly the step the report omits.  A cleaner future
statement drops the normalization entirely and tracks `ord_alpha` directly.

---

## 6. The charged checker is tautological where it matters

Not evidence for the new bridge:

* lines 342-343: `assert all((-i) + (-(n-i)) == -n ...)` -- an integer
  identity, independent of the recurrence, `F`, `A`, `nu` or anything else.
* lines 346-353: `assert -m - (n-m) == -n` and
  `assert -(m-1) - (n-m) != -n` -- likewise.  The advertised "99 causal
  mode/weight checks" is `sum_m (23-m) = 99` iterations of that tautology.
* lines 359-360: `endpoint_orders = {k: k+3}; assert min(...) == 1` -- an
  integer identity, not a computation on `L22`.
* `RESULT.json -> transport_conclusion.g22_order_without_optional_kernel`
  is the **string** `">=-2"`.  The single load-bearing quantity of the whole
  report is a literal, never computed.
* `local_newton_trial` (lines 170-207) builds `correction` from the *same
  summands* it put into `h`, so `assert h - q^2 == correction` collapses to
  `a^4 + a^2 v s + v^2 s^2/4 == (a^2 + v s/2)^2`, and `eps0 == q0sq` is then
  automatic.  Nothing checks that `h` equals `eps^-4 F(alpha+eps, eps^2 s)`
  for the reduced prefix: the prefix is hard-coded into `h`'s construction,
  not substituted into it.  So the "three nontrivial exact Newton identities"
  of the Replay section are one trivial square identity run three times.

Genuine content in the charged checker: `mode_table()` (generalized
binomials), `-40 + (-8)(-5) == 0`, the recursive hash pins, and
`check_d12_fixture()`.  That is roughly 40 of its 440 lines.

For contrast, my `S3`--`S5` substitute the prefix into a truncated local ring
and *derive* `H`, and `S7` recomputes `ord_alpha(g22) >= -2` from scratch.

---

## 7. Raw receiver firewall (charged item 4)

* The `G18..G21` windows are `dim 5,3,2,1` at degrees `2..6, 3..5, 3..4,
  3..3` (re-read from the frozen JSON).  These bounds are **not** load-bearing
  for the endpoint containment.  The pinned `characteristic_calculation` uses
  only `la_negative(...) == {}`, i.e. absence of a polar part, which follows
  from `ord_alpha(G_n) >= 0` alone.  The lower window bounds (`G19` "cannot
  store degree 2") are *extra* necessary equations at a hypothetical point;
  retaining them can only strengthen emptiness.
* The "rank `5,3,2,1`, nullity `0`" certificates are **recovered locally
  without any rank computation**: `ker L_n = K * A^((12-n)/2)`, which for
  `n = 18, 20` is `A^-3, A^-4` (not regular, hence excluded by regularity at
  `alpha`) and for odd `n` is not in the field at all.  So no global rank
  condition is load-bearing.
* **The `t -> t/nu(X)` guard holds.**  I checked the sharp form: a mode with
  a non-constant coefficient fails the raw row because
  `D = c'(X) t^m F^beta (theta F - 8 F) != 0`.  Consequently the normalized
  picture is not a raw picture, and the endpoint must be (and is) computed
  unnormalized.  No determinant equation is silently transported.

---

## 8. The `D22` endpoint (charged item 5)

In the original, unnormalized coordinates the `i=0, j=n` block of the
serialized row is exactly

```text
L_n(R) = 4(12-n) A^3 A' R - 8 A^4 R',        L_22(R) = -40 A^3 A' R - 8 A^4 R'.
```

Applying it to `A^k * (unit)`:

```text
L22(A^k u) = -(40 + 8k) A^(k+3) A' u  -  8 A^(k+4) u',
```

so the A-order rises by exactly `3`, **except** at `k = -5` where `40+8k = 0`
and it rises by `4`.  I verified `orders[k] = k+3` for `k in [-6,6] \ {-5}`
and `orders[-5] = -1`.  Hence:

* `ord_alpha(g22) >= -2  =>  ord_alpha(D22_raw) >= 1`, i.e.
  `D22_raw in (X-alpha)`.  Recomputed on the full 432-term image: min
  A-exponent `1`.
* The optional homogeneous mode `c22 A^-5` is annihilated exactly
  (`-40 + (-8)(-5) = 0`); the `-40 -> -39` mutation leaves the residual
  `+ c22 A^-2 A'`.  `c22` **is** a scalar (it is a `ker L_22` constant, by
  the same differential argument as the other modes), and the operator kills
  it outright, so it cannot rescue the point.  No non-kernel homogeneous
  direction exists (`L22(c22 A^-4) != 0`).
* The target really is the unit `1`: `per_row["22"]["target"] == 1`, and the
  unique `x_degree = 0` generator of row 22 carries the constant `-1`
  (i.e. `D22_raw - 1`).
* **Absent `G22` is not needed.**  Since the row is linear in `G22` with
  block `L22`, `D22 = L22(G22 - g22)` for any `G22`.  A raw `G22` receiver
  that is merely *regular at `alpha`* still gives `ord(G22-g22) >= -2` and
  `D22 in (X-alpha)`.  The charged hypothesis can be weakened accordingly.

---

## 9. Scope and independence (charged item 6)

| ingredient | used? |
|---|---|
| `q1` (`V0 = A'R0 + 2AR0'`) | **no** -- `q1` only parameterizes `V0`; nothing local mentions `R0` |
| global `D9` repair theorem `A | T` (`C`-root / `-8B^4U^3` argument) | **no** |
| local `D7` rung at `alpha` (`ord_alpha(T) >= 1`) | **YES** -- and it is the first rung of that same lane |
| local `D8`/`D9` rungs (`c6=0`, `ord_alpha(W) >= 1`) | **YES** |
| `D23` | no (`D23_imposed: false` in the source) |
| square-root sheet choice | no; the DVR step `ord(D^2)>=1 => ord(D)>=1` is not a sheet choice |
| algebraic closure | no; only the residue field extension `L = K(alpha)` |
| squarefreeness of all of `A` | **no** for the single-root theorem; **yes** for the `C != A` stratum corollary |
| simplicity of the selected root `alpha` | **YES**, essential |
| `c2 = 0` | **YES**, but automatic from `V0(alpha) != 0` under branch-P |

On multiplicity: if `alpha` had multiplicity `e >= 2`, the *endpoint* step
still works (`ord >= 2e-1 >= 1`), but the ladder's square-root rungs
(`ord(Delta^2) >= e => ord(Delta) >= e`) fail for `e >= 2`.  Simplicity of
`alpha` is what the ladder needs; squarefreeness of the rest of `A` is not.

**Field scope.**  Geometric / field-valued only.  Not scheme-theoretic
emptiness: the DVR square-root step and the scalar-unit step both fail over
nilpotents.  Not a raw-normal-form landing, not branch coverage, not a
Keller-pair theorem, not JC2.  I add nothing to the charged firewall on
these points and confirm all of it.

---

## 10. The mixed `D12` fixture (charged item 7)

Independently recomputed from the frozen `RESULT.json` (`S10`):

* `C*B = A` with `C = X-1`, `B = 1+X+X^2+X^3 = (X+1)(X^2+1)`;
  `gcd(B,B') = 1`, so `B` has three simple roots `-1, +-i`.
* `gcd(A,A') = 1`, `gcd(B,C) = 1`, `gcd(B,V0) = 1`, `gcd(B,Nred) = 1`, and
  the serialized Bezout identity `s*Nred + t*B = 1` rechecks.  So **all three
  `B`-roots are simple `V0`-unit roots of `A`.**
* The serialized denominator equals `C^3 B^2 = C * A^2` exactly, so at each
  `B`-root `ord(denominator) = 2` and `ord(Nred) = 0`: the pole is of
  **exactly order two**, independently of the `C`-root (where it is order
  three, `Nred(1) = -12`, which I recomputed).
* At `alpha = -1`: `A'(-1) = -4`, `V0(-1) = 8`, `C(-1) = -2`,
  `H(0,s) = (16+4s)^2`, `Nred(-1) = -3969/4096`.  All as charged.

**Is it evidence smuggled into the general proof?**  No, and I add a
positive cross-validation.  My locally derived `D12` normal form is
`polar(gbar_12) = (3/8) Delta6bar^2 / A^2`, so with `g12 = nu^12 gbar_12`
the fixture's `A^-2` coefficient at `alpha = -1` must equal
`(3/8) * V0(-1)^12 * Delta6bar^2`.  Numerically

```text
Nred(-1)/(12 C(-1)) = 1323/32768,
(8/3) * (1323/32768) / 8^12 = 441/2^48 = (21/2^24)^2.
```

An exact rational square -- which is what my normal form predicts and is not
a coincidence available to arbitrary data.  So the fixture is a genuine local
instance of the *same* mechanism (it dies because the local `D12` rung
`ord_alpha(Delta6) >= 1` fails at every `B`-root), and it is used only in the
charged Section 5 illustration, not as a premise of Sections 1-4.

Caveat: `Nred` itself is `REPLAY-ONLY` here.  I did not rebuild the
weight-12 characteristic numerator from the fixture's `F`/`G` slots; neither
does the charged checker.  Every structural consequence drawn from `Nred` is
recomputed.

---

## 11. Exact checker output

Run:

```bash
cd cases/ggv_8_28_upper_endpoint_unit_root_transport_review_opus5_20260828
python3 -B verify_unit_root_transport_review_opus5.py
```

Wall time 7.8 s, exit code 0, standard library only, no producer import.
Full transcript (elided only in the hash-pin block, which is 11/11 PASS):

```text
Opus 5 hostile-review checker: unit-root transport to D22
========================================================================
S1  custody of charged bytes
  PASS  sha256 ... (11 pins, all OK)
  INFO  desk source .../verify_uniform_d10.py sha256 = 8ebe5f4f099e6cf15b0a4703dfb348aa6cc72df8fdbc60b1d095925fa3746d21
  INFO  this checker  sha256 = cbf8498e77c639ebb08cda6c9f02a849e0b40f32c680cad4fe1120d30b6c9b6b
S2  authoritative raw fixture facts
  PASS  recurrence is the bilinear differential row
  PASS  303 variables / 513 generators
  PASS  fixture A=X^4-1, F1=H=A^2, c2=0
  PASS  charged zero rows are D7..D21, affine target row 22 value 1
  PASS  row 22 target is the unit 1
  PASS  no raw G22 and no raw F22 window
  PASS  G18..G21 window dimensions 5,3,2,1   [degrees [(2, 6), (3, 5), (3, 4), (3, 3)]]
  PASS  row-22 degree-0 generator carries the constant -1 (target +1)   [generators at x_degree 0: 1]
S3  exact eps^2 Newton model  (X=alpha+eps, t=eps^2*s)
  PASS  alpha is a simple root of A   [A'(alpha)=-4, V0(alpha)=8]
  PASS  eps^-4 F_0 is regular   [ord F_0 = 4]
  PASS  eps^-2 F_1 is regular   [ord F_1 = 2]
  PASS  identity (1)  H = Q^2 + eps^2(a^2 Z s^2/4 + V0 Z s^3/8) + eps^3 a T s^3/8 + sum_{i>=4} eps^(2i-4) F_i s^i
  PASS  identity (2)  H(0,s) = (A'(alpha)^2 + V0(alpha)s/2)^2   [a0^2=16, v0/2=4]
S4  valuation lemma, identity (3), and the mode schedule
  PASS  valuation lemma ord_alpha(P_k) >= 2k, hence ord (F^b)_k >= 4b-2k, all 10 exponents, k<=22
  PASS  leading coefficient of [s^k]H^b equals C(2b,k)*a0^(4b-2k)*(v0/2)^k
  PASS  charged mode/pole schedule reproduced exactly (c6@8,c10@11,c14@14 -> -1; c16@16 -> -2; c18@18 -> -3; c20@20 -> -4)
        [c6@g8:ord=-1,C=3/8 c10@g11:ord=-1,C=1/2 c14@g14:ord=-1,C=1 c16@g16:ord=-2,C=1 c18@g18:ord=-3,C=1 c20@g20:ord=-4,C=1]
  PASS  c4,c8,c12 have 2b in Z_{>=0}: C(2b,k)=0 for k>2b, so the bound 6+3m/2-2n is NOT attained for them
  PASS  c4 mode series is polynomial in t: (F^1)_k = F_k is regular for all k
  PASS  c12 mode series is (F^0)_k = delta_{k0}, always regular
S5  coefficientwise V0 normalization (run, not asserted)
  PASS  Fbar_i=nu^-i F_i implies ybar_n=nu^-n y_n, 3 rational points x 10 exponents x weights 0..22
  PASS  MUTATION Fbar_i=nu^-(i-1)F_i breaks the law at every nontrivial (point,exponent,weight)   [570 nontrivial checks, 0 survivors]
  PASS  reduced prefix: 4*F2 = V0^2 + A^2 Z, hence Fbar_2 = (1+A^2 Zbar)/4
  PASS  reduced prefix: 8*F3 = V0*Z + A*T, hence Fbar_3 = (Zbar + A*Tbar)/8   -- A power ONE
  PASS  with generic T, ord_alpha(Tbar)=0, so Fbar_3 is NOT of the pinned shape (Zbar+A^2*Vbar)/8 before the local D7 rung   [ord_alpha(T) = 0]
S6  the raw differential row and mode scalarity
  PASS  the j=n block of the raw row is exactly L_n(G_n) = 4(12-n)A^3A'G_n - 8A^4G_n'
  PASS  G = F^(3/2) annihilates D_n for n=0..11
  PASS  G = c_m t^m F^((12-m)/8) with a CONSTANT c_m annihilates D_n, all nine modes
  PASS  MUTATION wrong indicial exponent (beta=1/2 born at m=6) fails
  PASS  MUTATION NON-CONSTANT mode coefficient fails: c'(X)t^m F^b(tF_t-8F) does not vanish -> the normalized cbar_m=nu^-m c_m is NOT a raw mode
S7  the complete local ladder D7..D22 from the GENERAL reduced prefix
  PASS  D7 polar closed form: polar(g7) = 3*T*(A*K-2*T)/(2048*A^2), K=64F4-Z^2  (equals the q1-free lane's A^2 | T(AK-2TV0) at V0=1)
  NOTE  D7 rung, LOCAL: ord(T)=0 would give ord(T(AK-2T))=0<2, so ord_alpha(T)>=1 at a simple V0-unit root; write T=A*V.
  PASS  D8 polar closed form: polar(g8) = (3/8)*(F4-V/16-Z^2/64)^2/A^2 + (3/32)*c6/A
  NOTE  D8 rung, LOCAL: mod A gives ord(W0^2)>=1 so ord(W0)>=1 (DVR); then the A^1 class forces ord(c6)>=1, and c6 is a scalar, so c6=0.
  PASS  D9 polar closed form after c6=0: -3W^2/(16A^2) + (3/4)F5*W/A - (3/256)V*W*Z/A
  NOTE  D9 rung, LOCAL: mod A gives ord(W^2)>=1, so ord(W)>=1; W=A*R.
  PASS  D10 polar closed form: polar(g10) = (3/8)*Delta5^2/A^2, Delta5=F5-R/2-Z*V/64
  PASS  D11 polar closed form: -3S^2/(16A^2) + A^-1(...) + c10/(4A) -> ord(S)>=1 then c10=0
  PASS  D12 polar closed form: polar(g12) = (3/8)*Delta6^2/A^2, Delta6=F6-Q/2-R*Z/8-V^2/256
  PASS  D13 polar: -3*T1^2/(16A^2) + O(A^-1) -> ord(T1)>=1
  PASS  D14: the A^-1 (odd) class of polar(g14) is exactly c14, and the A^-2 class contains (3/8)Delta7^2 -> c14=0 and ord(Delta7)>=1
  PASS  D15 polar: -3*Y1^2/(16A^2) + O(A^-1) -> ord(Y1)>=1
  PASS  D16: polar(g16) = (3B^2/8 + c8*B/2 + c16)/A^2
  PASS  D16 relation 3B^2+4c8B+8c16 = 8A^2M clears the polar part
  PASS  D17: polar(g17) = ((3B+2c8)C/4 - M/2)/A^2
  PASS  D17 relation (3B+2c8)C-2M = 4A^2N clears the polar part
  PASS  D18: polar(g18) = c18/A^3 + ((3B+2c8)E/4+3C^2/8-N/2)/A^2
  PASS  L_18 annihilates c18/A^3 (so D19 cannot kill it; the birth row does)
  PASS  D18 relations c18=0 and (...)=A^2 O clear the polar part
  PASS  D19: polar = A^-2 only, and its relation clears it
  PASS  D20: polar = c20/A^4 + P20/A^2, L_20 kills c20/A^4, relation clears
  PASS  D21: polar = A^-2 only, and its relation clears it
  PASS  ENDPOINT: complete g22 has A-exponent support {-2,0,2,4,6,8}, so ord_alpha(g22) >= -2   [support [-2, 0, 2, 4, 6, 8]]
  PASS  D22_raw = -L22(g22) lies in (A): every term has A-exponent >= 1   [432 terms, min A-exponent 1]
S7m load-bearing mutations of the local ladder
  PASS  each prefix rung D7,D9,D11,D13,D15 is load-bearing: dropping one deepens polar(g16) from -2 to -20/-16/-12/-8/-4
        [{'baseline': -2, 'skip D7  (F3 keeps A^1)': -20, 'skip D9  (F4 keeps A^1)': -16, 'skip D11 (F5 keeps A^1)': -12, 'skip D13 (F6 keeps A^1)': -8, 'skip D15 (F7 keeps A^1)': -4}]
  PASS  MUTATION retaining c18: the D18 quotient relation alone leaves exactly c18/A^3, so the polar part does not clear
S8  the endpoint operator L22 in the original coordinates
  PASS  L22(R) with R of A-exponent k has A-exponent >= k+3 (exactly k+3 except on the kernel direction k=-5, where 40+8k=0 gives k+4)
        [k=-2 -> 1, k=0 -> 3, k=-5 -> -1]
  PASS  hence ord_alpha(g22) >= -2 forces D22_raw in the maximal ideal (X-alpha)
  PASS  EXACT kernel: L22(c22*A^-5) = 0  (-40 + (-8)(-5) = 0)
  PASS  MUTATION -40 -> -39 destroys the c22*A^-5 cancellation (residual +1*c22*A^-2*A')
  PASS  no other homogeneous endpoint mode: ker L_n is spanned by A^((12-n)/2), which for n=22 is A^-5 and for odd n is not rational
  NOTE  STRENGTHENING: the raw row is linear in G22 with block L22, so for ANY G22 one has D22 = L22(G22 - g22).  If a regular raw G22 receiver existed, ord(G22-g22) >= -2 still gives D22 in (X-alpha).  'Absent raw G22' is therefore not load-bearing for the contradiction.
  NOTE  Multiplicity: if alpha had multiplicity e>=2 the endpoint step still gives ord >= 2e-1 >= 1, but the ladder's square-root rungs (ord(Delta^2)>=e => ord(Delta)>=e) fail.  Simplicity of alpha, not squarefreeness of all of A, is what the ladder needs.
S9  the prefix gap between the charged (6) and the pinned cascade
  PASS  charged report displays Fbar_3=(Zbar+A*Tbar)/8   (A power ONE)
  PASS  charged report claims '(6) is exactly the reviewed fixed prefix'
  PASS  recursively pinned common_F_prefix has F3 = (z + A^2*v)/8   (A power TWO)
  PASS  pinned D8/D9 stage starts from F4 = v/16+z^2/64+A^1*w, i.e. after the D7 rung A|T
  NOTE  The charged normalized prefix (6) is the PRE-D7 general prefix; the recursively pinned fixed cascade starts one A-power deeper at F3 (post-D7 A|T) and at F4 (post-D9 A|W).  The identification asserted in the charged section 2 is false as written; the bridge needs the local D7..D15 rungs, which S7 supplies.
S10 the mixed-root D12 fixture (independent recomputation)
  PASS  C*B = A and B = (X+1)(X^2+1) has three simple roots -1, +-i
  PASS  serialized denominator equals C^3*B^2 = C*A^2
  PASS  Bezout identity s*Nred + t*B = 1 rechecked
  PASS  gcd(B,V0)=gcd(B,Nred)=gcd(B,C)=gcd(A,A')=1: every B-root is a SIMPLE V0-unit root of A
  PASS  pole order at each B-root is EXACTLY 2 (ord den = 2, ord Nred = 0)
  PASS  literal local data at alpha=-1: A'=-4, V0=8, C=-2, H(0,s)=(16+4s)^2, Nred=-3969/4096
  PASS  Nred at the C-root X=1 recomputed as -12 (matches the record)
  PASS  cross-validation: the fixture's A^-2 coefficient at the B-root -1 equals (3/8)*V0^12*Delta6bar^2 with Delta6bar = +-21/2^24 exactly as the locally derived normal form demands   [Delta6bar^2 = 441/281474976710656]
  NOTE  Nred itself is REPLAY-ONLY here (not recomputed from the fixture's F/G data); every structural consequence drawn from it is recomputed. The fixture is used only in the charged section 5 illustration and is not a premise of sections 1-4.
========================================================================
RESULT: ALL CHECKS PASSED
        7 reviewer notes recorded above
```

`git diff --check` on the two authored paths reports nothing (both are new
untracked files; whitespace-clean by `git diff --no-index --check`).  No
canonical top-level file, adapter, producer artifact, or other case was read
into, edited, or written.  `jc2-lean` was never entered.

---

## 12. What may and may not be promoted

**May be promoted, after this review:**

* the exact `eps^2` Newton model (1)-(3) and the valuation lemma
  `ord_alpha((F^beta)_k) >= 4beta - 2k`, with the sharp leading coefficient
  `C(2beta,k) A'(alpha)^(4beta-2k) (V0(alpha)/2)^k`;
* the coefficientwise `V0` normalization (5)-(8), **as a bookkeeping
  identity only**, with the explicit statement that it is not a symmetry of
  the raw row;
* the scalarity of the modes `c_m` and the indicial law `beta_m=(12-m)/8`,
  both as consequences of the raw differential row;
* the **repaired theorem of Section 2** and its `C != A` corollary;
* the `D7`--`D21` dependency ledger of Section 4, including the statement
  that no global degree, rank, second-root value, or sheet choice is
  load-bearing.

**May NOT be promoted:**

* the sentence "`(6)` is exactly the reviewed fixed prefix" -- it is false;
* the sentence "This uses neither `q1` nor the provisional `D9` repair" in
  its present form -- replace with the Section 9 table;
* the charged packet's `PASS_EXACT_UNIT_ROOT_TRANSPORT_DISCRIMINATOR` as
  *evidence* for `ord_alpha(g22) >= -2`; that value is a string in its
  `RESULT.json`;
* anything about the deep `A | V0` stratum;
* preservation of raw global windows under the normalization;
* a raw-normal-form landing, a branch-coverage theorem, scheme-theoretic
  emptiness, a Keller-pair theorem, or JC2.  The universal
  arbitrary-squarefree-quartic bridge flagged by the pinned `A`-dependency
  audit remains open and is untouched by this review.

## 13. Minimal correction wording required

Even a reader who accepts the conclusion must apply these four edits before
the report is quoted:

1. Section 2, replace "So (6) is exactly the reviewed fixed prefix in the
   local coefficient ring" with:
   *"(6) is the general reduced prefix in the local coefficient ring.  It is
   one `A`-power short of the recursively pinned fixed prefix
   `F3=(z+A^2 v)/8`, `F4=v/16+z^2/64+A^2 r`, which already encodes the `D7`
   (`A|T`) and `D9` (`A|W`) conclusions.  The gap is closed by re-running the
   `D7`--`D15` rungs in the DVR; at a `V0`-unit simple root each is
   immediate."*
2. Verdict and Section 6, replace "does not use the provisional `D9` repair"
   with: *"does not use the global `D9`-repair theorem `A|T` or its `C`-root
   argument; it does use the local `D7`, `D8`, `D9` rungs at `alpha`, which
   at a `V0`-unit simple root follow from `ord_alpha(T(AK-2TV0)) >= 2` and
   two DVR square-root steps."*
3. Add `V = T/A` to the named-quotient list, and state that `c2 = 0` is a
   hypothesis which `V0(alpha) != 0` supplies automatically under branch-P.
4. Weaken two hypotheses, since they are not used: replace "squarefree `A`"
   by "`alpha` a simple root of `A`" in the single-root theorem (keeping
   squarefreeness only for the `C != A` corollary), and replace "absent raw
   `G22`" by "no raw `G22`, or a raw `G22` regular at `alpha`".

## 14. Ledger line

```text
GGV upper endpoint / unit-root transport (single-root SRT):
  REPAIR by Opus 5 hostile review 20260828-r1.
  Theorem TRUE and independently reproved from the general reduced prefix;
  the charged prefix identification is false, the D9-independence claim is
  overstated, and the load-bearing D7--D15 localization was undelivered.
  Repaired statement + ledger in this report; checker
  cbf8498e77c639ebb08cda6c9f02a849e0b40f32c680cad4fe1120d30b6c9b6b.
  Deep A|V0 stratum, raw-normal-form landing, coverage, JC2: untouched.
```
