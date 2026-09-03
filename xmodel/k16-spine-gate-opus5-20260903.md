# Hostile gate: the PROVED second affine spine of the K=16 normalised systems

Date: 2026-09-03.  Lane: `k16-spine-gate-opus5-20260903`.
Charged report under audit: `xmodel/k16-middle-spine-sol56-20260903.md`.

## Verdict

**GAP — one named step, everything else CONFIRMED.**

Sections 2, 3, 4, the section-5 pivot table, the split-index obstruction and
its bypass, the terminal data at `t=1,...,6`, and the logical chain
`1 in <T_(t,k)>  <=>  gauged chart empty  <=>  (T) at t` all reproduce under
independent re-derivation.  The reduction is a genuine quotient-ring
equivalence: **no projection and no untyped localisation**.  Every pivot in
the section-5.1 order has a norm that is a nonzero polynomial in `t` with no
positive-integer root, including on the split ray, and no zero divisor is
inverted anywhere.

The single unclosed step is the **derivation** of the closed high-`E_t` pivot
forms (5.9)-(5.15).  The charged driver `laurent_pivot_formulas.py` verifies
that `p_C`, `p_Q`, `p_b2` agree with a stated linearization `b_j, d_j, n_j`,
but `b_j, d_j, n_j` are asserted in that file and derived nowhere in the
charged material.  They are exactly reproduced by the exact nonlinear records
at `t=2,3,4,5` (32 pivot coefficients), and the structural argument that the
linearization is exact is sound; but "for every `t`" is not yet proved.
Because (8.1)'s residual variable list (4.2) is what remains **after** those
`2t+1` eliminations, the gap propagates into the exact statement of (8.1).

Therefore: the spine and the reduction are promotable **once (5.9)-(5.15) are
derived symbolically in `(t,j)`**; the charged file's own `PROVED-HERE` label
for the `t>=2` spine is one derivation short.  Its `PARTIAL` verdict on (T)
itself, and its refusal to promote the fixed-`t` terminal ideals to an
induction, are both correct and conservative.

Cheapest test to close it: section 8 below.

## 0. Frozen inputs

The manifest was generated from the receipt by `awk` over
`charged_input_i_basename` / `charged_input_i_sha256`; no digit was retyped
into the check command.

```text
awk -F= '...' xmodel/k16-spine-gate-opus5-20260903.run.v2 \
  > box/k16spinegate-20260903/inputs.sha256
sha256sum -c box/k16spinegate-20260903/inputs.sha256
```

All 19 charged files returned `OK`.  Drivers and artifacts are confined to
`box/k16spinegate-20260903/`; no ledger was edited and no file in
`box/k16spine-20260903/` was modified.

Orientation convention, fixed once: the charged generator
`t_order_system.jac` uses `J(f,g)=f_gamma g_pi - f_pi g_gamma`, and
`J(Q,P)=c*gamma`.  Under that orientation the coordinate Jacobian is `-p^3`
and `c=-y g`.  Every sign below is in that convention.  This is a declared
convention, not a fallacy; the same choice is made in `compact_remainder.py`,
so charged report and charged generator agree.

## 1. Section 2 re-derived (`gate1_compact.py`, `gate1e_chart.py`)

Nothing was imported from `compact_remainder.py`.  The Jacobian was rebuilt
from the six brackets among `h,A,B,z`, reduced modulo the monic relation
`h(pi,gamma)-X`, and compared with the report's displayed formulas.  **35/35
symbolic checks pass.**

- **(2.4), (2.5): CONFIRMED symbolically with generic `U,R,V,S,T`.**  The tag
  support is exactly the seven charged tags; `C12`, `C11`, `C00`, `C01` match
  term for term; the three syzygies are identities; `c=-y g` is forced by the
  `(1,0)` tag, not assumed.
- **(2.2): CONFIRMED, derived not assumed.**  `gamma(X,p)=p+b1+b2/p+b3/p^2
  -L/p^3` was obtained by inverting `X=h(p,gamma)` and checked to invert it;
  `A`, `B`, `z`, `Q1,Q2,P0,...,P3` follow exactly.
- **(2.3): CONFIRMED.**  `(J(Q,P)-c*gamma)p^3` has `p`-coefficients
  `-(D0+c),...,-(D4-c L)` and nothing else.  New observation: **`D4-c L`
  vanishes identically**, so (2.3) is four conditions plus the definition of
  `c`, not five.
- **Equivalence (2.3) <-> (2.4): CONFIRMED with an explicit certificate.**
  The two systems are two coordinate readings of one element (substituting
  `gamma=gamma_L, pi=p` forces `X=h` and kills the `(h-X)` multiple).  The
  change of basis is triangular:

```text
D0 = -b2 C12 - b1 C11 - C01
D1 = -b3 C12 - b2 C11 - C00
D2 =  L  C12 - b3 C11
D3 =  L  C11
D4 =  0
```

  The backward direction divides by `L=X-b4`, which is legitimate because `L`
  is **monic in `X`, hence a nonzerodivisor** — this is a cancellation, not a
  localisation.  The report's "no division by `p`" claim is right, and the
  `L`-step it does not mention is harmless for the same reason.
- **(2.6), (5.6), (5.7), (5.7b): CONFIRMED.**  `C11|_(X=b4)=-2gR` gives
  `R(b4)=0`; `C11/L = 2yT'-g(5C+3LC')` gives `T'`, at which `C11` vanishes;
  `C12=0` is *literally* the Euler identity (5.7) after `R=LC` and that `T'`.
  Both band forms in (5.7b) are exact.

**Instantiation against the charged generator at `t=2,3,4`: 30/30 checks
pass.**  With no preprocessing at all, `Q_chart = U(h)+A R(h)+y B` and
`P_chart = V(h)+A S(h)+B T(h)+g z + a_(e,0) gamma` exactly; `y=q_(2t+1),1`,
`g=a_(3t+1),3`, `x=q_(t+1),1`, `deg R=t`, `deg S=2t`, `deg T=t`.  After
`a_(e,0)=0`, **every** charged row at `(band k, tag)` equals `[X^k]` of the
corresponding section-2 tag, and no charged row lies outside that support.

The one thing the report leaves implicit — the "already proved constant
spine" that sets `a_(e,0)=0` — is a genuine unit pivot: `a_(e,0)` occurs in
`11t+2` charged rows, and in band `2t`, tag `12`, its coefficient is the
rational constant `3q` (15, 21, 27 at `t=2,3,4`).  **No issue.**

## 2. Section 3: support, counts, duplicates (`gate2_support.py`)

**41/41 checks pass.**

- `G(Z)=(1+Z+yZ^2)^(e/q)` gives `g1=e/q`, `g2=e(2qy+t)/(2q^2)`,
  `g3=t(3t+1)(6qy-(t+1))/(6q^3)` — the last literally the charged `g`.
  (5.1) holds at `n=0..4`; `g4=(t(3t+1)/(24q^4))H_t` is an exact multiple of
  `H_t`, so `g4=0` in `A_t`; (5.2) holds mod `H_t` in both displayed forms.
- **(5.7a): all three identities CONFIRMED symbolically in `t`.**
- **Where `H_t` comes from is now explicit.**  `[X^t]C11 = t(3t+1)H_t/(6q^3)`:
  the band-`t` tag-`11` row *is* `H_t`.  This matches the charged audits,
  which record `H_band = t` at `t=3,4,5,6`, and the primitive `H_t` in each
  audit agrees with `12q^2y^2-12q(t+1)y+(t+1)(3t+2)` and
  `disc = 48q^2(t+1)` at `t=3,4,5,6` (9408, 19440, 34848, 56784).
- Boundary vanishings: `[X^(2t)]C12=0` by (5.7a)#2, `[X^(3t+1)]C00=0` by
  (5.7a)#3, `[X^(4t+1)]C01=0`.  Hence `deg C12=2t-1`, `deg C11=t`,
  `deg C00=3t`, `deg C01=4t`, confirmed by explicit construction at
  `t=2,...,6`.
- **`2t` zero/duplicate rows: PROVED, not sampled.**  All `2t` tag-`02` rows
  in bands `0..2t-1` are exactly `-b1[X^k]C12-[X^k]C11`, verified at
  `t=2,...,6`; the identity `C02=-b1 C12-C11` is symbolic, so this holds for
  every `t`.  The tag-`03` copy is the rational associate `-C12`.
- Raw tag inventory is uniformly `14t+9` rows — matching the measured
  51/65/79/93 at `t=3,4,5,6` — and the post-`H/c` counts `9t+2` rows,
  `6t+2` auxiliaries reproduce at `t=2,...,6` with
  `tag_pattern_checked = true`.
- Pivot arithmetic is internally consistent: the schedule (4.1) consumes
  tag `12` (2t) + tag `11` (t) + tag `00` (2t+1) + tag `01` at band `2t` (1)
  `= 5t+2`, leaving exactly tag `01` in bands `0..2t-1`, `= 2t` rows, and
  `(9t+2)-(5t+2)-2t = 2t`.
- The post-`H/c` auxiliary set decomposes uniformly as
  `R (t) + U (2t-1) + V (3t-1) + b (4) = 6t+2`, exactly matching the measured
  variable lists.

**One presentational imprecision, not a gap.**  §3 says the support "follows
from the degree bounds in (2.4) together with the charged coefficient-space
boundaries".  Degree bounds alone give `deg C00=3t` and `deg C01=4t`, not
`2t`: the `t+1` rows of `C00` in bands `2t+1..3t+1` and the `2t+1` rows of
`C01` in bands `2t+1..4t+1` are removed by the *first* spine, not by degree.
That first spine is banked as uniform elsewhere — `k16-uniform-structure`
§4.2 item 2, "`3t+4` Q-constant quotient pivots, descending from band `4t+1`
through band `2t`" — and `3t+2` of those are precisely these rows, with
`a_(e,0)` and one more making `3t+4`.  The dependency is real and the
citation is implicit; the conclusion stands.

Independent of all this, **§5.1 does not need §3**: it consumes `C11`, `C12`,
`C00` (through `D1`) and `C01` directly on the full model (2.1).

## 3. Section 5.1: pivot norms for all positive `t` (`gate3_norms.py`)

**38/38 checks pass.**  `H_t((d+t+1)/(2q)) = 3d^2-(t+1)` and

```text
Res_y(H_t, a d + b) = 4 q^2 (3 b^2 - a^2 (t+1))            (1.1)
```

both hold symbolically in `t`.  Every entry of the section-5 table matches
(1.1) exactly.  Norms of the **section-5.1 proof order**, with integer roots:

| pivot | class | `Res_y(H_t, ·)` | integer `t`-roots |
|---|---|---|---|
| (5.7c) `T`,`S` diagonals `2my`, `(2m+1)y` | `d+(t+1)` | `4(t+1)q^2(3t+2)` | `{-1}` |
| (5.7c) `g` | `3d+2(t+1)` | `12(t+1)q^2(4t+1)` | `{-1}` |
| `D1` divisibility (`b1`) | `y g = -c` | product of the two above | `{-1}` |
| gauge `alpha_t=0` (`T(0)`) | `q/y` | product of the two above | `{-1}` |
| (5.10) `C_j`, `1<=j<=t-1` | `L_C` | `-4q^2(3t+2)^3 F_C(t,j)` | none in range |
| (5.13) `q_j`, `t<=j<=2t` | `L_Q` | `-4q^2(t+1)(3t+2)^2 F_Q(t,j)` | none in range |
| (5.15) `b2` | `3q d+(t+1)` | `-12q^2(t+1)(3t+2)(4t+1)` | `{-1}` |

The only integer root anywhere is `t=-1`, which is not positive.  For the two
indexed families the certificates are positivity, not root-finding:

- `3B_C^2-A_C^2(t+1) = -(3t+2)^3 F_C` exactly, and `F_C(t,t-n)` is the
  displayed quartic whose **every coefficient is nonnegative with constant
  term 32**; `n=t-j>=1`, so `F_C>0` for every `t>=2` and every `j` in range.
- `3B_Q^2-A_Q^2(t+1) = -(t+1)(3t+2)^2 F_Q` exactly, and
  `F_Q(t,q-n)=n^2+4nt+6n+4t^2-3 >= 12` on `1<=n<=t+1`, `t>=1`.

Exhaustive range scan for `t<=40` finds no zero for either family.  Rational
denominators are positive on their ranges: `4t-2j+1 >= 2t+3` on `1<=j<=t-1`,
`4t-2j+1 >= 1` and `q-j >= 1` on `t<=j<=2t`.  `D_top(t)=60(2t+1)^5` has only
the root `-1/2`; `lc(H_t)=12(2t+1)^2` never vanishes.  (5.3), (5.11a),
(5.14a), (5.15) all reproduce exactly.

### The obstruction and its bypass

`Res_y(H_t, d+s) = 4q^2(3s^2-(t+1))` vanishes **exactly** on `t=3s^2-1`, i.e.
`t = 2, 11, 26, 47, 74, 107, ...`; `disc(H_t)=48q^2(t+1)` is a square on the
same set, so `H_t` splits there.  Reproduced concretely:

```text
t= 2, s=1 : H_t = 12(5y-2)(5y-1)   ; gcd(H_t, d+s) = y-1/5   ; invertible = NO
t=11, s=2 : H_t = 12(23y-7)(23y-5) ; gcd(H_t, d+s) = y-5/23  ; invertible = NO
t=26, s=3 : H_t = 12(53y-15)(53y-12); gcd(H_t, d+s) = y-12/53; invertible = NO
```

`d+s` is a **nonzero zero divisor**: nonzero mod `H_t`, yet `sympy.invert`
refuses it.  The charged `t=2` deferral is exactly right: candidate `5y-1`
has resultant `0` (it is literally a factor of `H_2`), is deferred without
inversion, and the later pivot `39y-10` has resultant `-3696 != 0`.

**The bypass is structural, not a repair.**  The section-5.1 order never
schedules `d+s`: its classes are `y`, `3d+2(t+1)`, `L_C`, `L_Q`, `L_2`, all
with norms proved nonzero for every positive integer `t`.  Split-safety of
the proof spine is therefore not a case analysis at all.  `terminal_laurent_
model.Algebra.inverse` enforces this operationally: it inverts only through
`sp.invert` in `Q[y]/(H_t)`, which is an extended-gcd, and then re-checks
`u u^-1 = 1`.  No component is discarded; FALLACY-v2 `sat()`-wrapping and
raw-remainder clauses are respected.

### The gap

`p_C_derived`, `p_Q_derived` in `laurent_pivot_formulas.py` are built from

```text
b_j = g3(3t+2-3j)/(2y(t-j)),
d_j = (g2(t+1-2j)+b_j(t+1+j))/(y(4t-2j+1)),
n_j = -g1(t+j)+(j-t)d_j+2q b_j,
```

and the analogous `dq_j, nq_j`.  These are **asserted**.  They are not
derived from (5.7b) anywhere in the charged material, and the report's text
does not exhibit the perturbation calculation that produces them.  The
structural claim that justifies linearizing — each new elimination variable
sits in its own weight, so its affine coefficient has weight zero and lies in
`A_t`, hence equals its value at the homogeneous origin — is sound and is
what makes the linear calculation exact rather than tangential.  What is
missing is the symbolic `(t,j)` propagation of the perturbation through
`T'`, the Euler inverse for `S`, and the `E_t` coefficient.

Evidence status: `p_C`, `p_Q`, `p_b2` agree with the **exact nonlinear**
Laurent records at `t=2,3,4,5` up to rational associates — 32 pivot
coefficients in all (I re-ran the checker with all four records present; the
frozen inputs directory contains only `t=2`, so the charged run of that file
sees one record).  This is strong but finite.

## 4. Terminal family (`gate4a_rebuild.py`, `replay/`)

- **(6.1) `E_t` is `C01`: CONFIRMED** — it is the same expression, and the
  records use `-E_t`.  `deg_X E_t = 4t`, and the `2t+1` bands `4t..2t`
  eliminate `C_1..C_(t-1)`, `q_t..q_(2t)`, `b2`, exactly as (5.8) states.
  The charged records confirm this band-by-band: at `t=3` the recorded
  `high_pivots` are bands `12,11,10,9,8,7,6` on `C1,C2,q3_0,q4_0,q5_0,q6_0,
  b2`; at `t=5`, bands `20..10` on `C1..C4,q5_0..q10_0,b2`.  The residual is
  `b3,b4,q_(2,0),...,q_(t-1),0` — exactly (4.2) — at `t=2,3,4,5`.
- **Independent rebuild.**  Re-running `terminal_laurent_model.build` and
  comparing against the charged JSON: at `t=2` and at `t=3`, `H_t`, the
  normalizer (`g1,g2,g3,c`), **every** high pivot (5 and 7 respectively) and
  **every** terminal row (4 and 6) match exactly — `matches_H`,
  `matches_normalizer`, `matches_charged_pivots`, `matches_charged_terminal`
  all `true`.  Residual variables `[b3,b4]` and `[b3,b4,q2_0]`, as (4.2)
  predicts.  The `t=4` rebuild was stopped at the wall-clock cap; that record
  was instead audited through the closed-form pivot check above and the
  Singular replays below, both of which pass.
- **Unit ideals, replayed independently in Singular (17 jobs, all `UNIT`):**

```text
t=1  full gauged chart, 23 rows / 18 unknowns, sat(I,<c>) -> G = [1]
     with CONTROL_ACTUAL_PAIR / RING / EMPTY / NONEMPTY all PASS
t=2  product algebra, both fibres y=1/5, y=2/5, both charts b4=0,1 -> [1]
t=3  b4=0 (4 rows) and b4=1 (6 rows), char 0, exact               -> [1]
t=4  b4=0 (8 rows) and b4=1 (8 rows), char 0, exact               -> [1]
t=5  b4=0 (10 rows), char 0, exact                                -> [1]
t=5  mod 1009, y=433 and y=760, b4=0 and b4=1                     -> [1]
t=6  mod 1009, y=380 and y=940, b4=0 and b4=1                     -> [1]
     (both the Laurent and the canonical side-first emitters)
```

  `12q^2y^2-12q(t+1)y+(t+1)(3t+2) = 0` at `y=433,760` mod 1009 for `t=5` and
  at `y=380,940` for `t=6`, so both fibres really are covered.  The `t=2`
  product-algebra rows were regenerated by me, not read from the charged
  artifact.
- **`t=5, b4=1` in characteristic zero remains `INCONCLUSIVE_TIMEOUT`**, not
  `NONUNIT`.  The charged status file types it correctly and does not promote
  the modular success across characteristic.  Correct.
- **Relation to the banked uniform-structure lane.**  At `t=3` both terminal
  systems live in the *same* ring `A_3[b3,b4,q_(2,0)]`, with the same six
  bands `0..5` and the same degree profile `13,...,8 = 4t+1,...,2t+2`.  Both
  are `[1]`, as is their union, so as ideals they coincide — trivially, both
  being the unit ideal.  The exact relation is stronger than "unit and
  coordinate change" and weaker than "same generators": each is the image of
  one and the same ideal under a different composite of **unit affine
  substitutions**, which are ring isomorphisms of the ambient `A_t[...]`.
  The relating map is that composite, not a relabelling of printed variables.
  The charged report is right that the Laurent subsets are not the banked
  side-first subsets.
- Row/variable counts `2t / t` and band range `0..2t-1` agree between the two
  lanes at `t=2,3,4`, and the uniform-structure lane declines to promote them
  — consistent.

## 5. The logical chain, step by step

```text
(T) at t   :  the gauged order chart of the (12t+4, 8t+4; 12t+1, 3) ray,
              a NECESSARY SUPERSET, has no point with c != 0.
```

1. **chart -> tags.**  `J(Q,P)=c*gamma` in `Q[gamma,pi][params]`, reduced
   modulo the monic `h-X`.  Monic division is exact and branch-free, so the
   `14t+9` tagged coefficients generate the same ideal as the original
   equation.  *Justification: `gate1e` E1-E3, exact at `t=2,3,4`; the tag
   inventory `14t+9` is uniform and matches the measured 51/65/79/93.*
2. **tags -> Laurent rows.**  `(pi,gamma) -> (X,p)` with
   `gamma=p+b1+b2/p+b3/p^2-L/p^3`; coefficient comparison in `R[p,p^(-1)]`,
   free over `R` on `{p^k}`.  Forward is the triangular matrix above,
   backward is division by the **monic** `L`; both are `R`-linear over
   `Q[X,b]`.  *Not a projection: mutually inverse.  Not a localisation: `L`
   is a nonzerodivisor and no power of `p` is inverted.  Justification:
   `gate1` B0-B3, C1-C3.*
3. **`c` and the algebra.**  `C10 = -yg` forces `c=-yg`; `[X^t]C11` is a
   nonzero rational multiple of `H_t`, defining `A_t = Q[y]/(H_t)`; `x=1` is
   a weighted rescaling on the `c != 0` locus.  `A_t` is squarefree
   (`disc = 48q^2(t+1) != 0`), hence `Q[y]/(H_t)` is a field or `Q x Q`; both
   are handled, never assumed to be a field.  *Justification: `gate2`
   L1-L3, S1-S4; `gate3` N6.*
4. **spine.**  `5t+2` unit affine substitutions in the section-5.1 order.
   Each is `v -> (linear in the remaining variables)/u` with `u` a unit of
   `A_t`; such a substitution is an **isomorphism of the quotient ring**, so
   it preserves "the ideal is `[1]`" in both directions.  *Justification:
   `gate3` N9, P1-P9, E1-E5 — for the reconstruction block and for `L_2`,
   fully; for `L_C`, `L_Q`, modulo the derivation gap of section 3 above.*
5. **grading slice.**  `wt(b4)=1`, `wt(b3)=t+1`, `wt(q_(i,0))=i`,
   `wt(T_(t,k))=4t+1-k`.  Each pivot coefficient has weight zero, hence lies
   in `A_t` and cannot involve a residual variable; this is what makes the
   linearization at the homogeneous origin *exact*.  The `b4 != 0` chart form
   (6.4) is a consequence, and the report correctly insists it must be paired
   with `b4=0`.
6. **terminal.**  What remains is `<T_(t,0),...,T_(t,2t-1)>` in
   `A_t[b3,b4,q_(2,0),...,q_(t-1),0]`.  By steps 1-5 this ideal is `[1]` iff
   the chart is empty on `c != 0`, i.e. iff (T) holds at `t`.
7. **base case.**  `t=1` does not instantiate the spine (the coefficient-space
   boundaries collide); it is discharged separately, and I re-verified it
   directly from the chart: `sat(I, <c>)` gives `[1]` with all four controls
   passing.

Step 6 is the report's (8.1).  **So (8.1) is exactly (T) on the ray**, with
the one caveat that the *variable list* in (8.1) is the post-(5.8) residual
and therefore inherits the section-3 gap.  Fixed `t<=6` bases are tests, not
an induction, and the report says so.

## 6. FALLACY-v2 audit of the charged report

- **`sat()` wrapping** — the emitter extracts `LS[1]`, asserts
  `typeof == "ideal"` and `nameof(basering)=="R"`, and runs both an empty and
  a nonempty control plus an independent actual-pair control.  All PASS in my
  replay.  **Clean.**
- **Raw remainder degree** — all reductions are polynomial remainders modulo
  the declared `H_t`; vanished leaders are branched on (the deferral
  mechanism) and zero is handled.  **Clean.**
- **Variable/ring map** — the map, generator order, coefficient field, and
  image checks are declared and I verified the images at `t=2,3,4`.  **Clean.**
- **Prime label/derivative** — the report states explicitly that a prime is
  `d/dX`, not a label, and `compact_remainder.py` carries `Up,...,Tp` as free
  symbols consistently.  **Clean.**
- **Floor/attainment, carrier/attainment** — the report does not convert the
  finite `t<=6` unit ideals into an all-`t` statement, and types the `t=5`
  `b4=1` timeout as `INCONCLUSIVE_TIMEOUT`.  **Clean.**
- **Denominators** — `D_top(t)=60(2t+1)^5` and the listed factors are positive
  on their index ranges; no `D_terminal(t)` is declared, correctly.
  **Clean.**
- The `t=3s^2-1` indices are correctly refused as a "finite denominator
  exception set"; they are infinite and are handled by the product algebra.
  **Clean.**

One over-claim to record: `laurent_pivot_formulas.py` prints
`LAURENT_PIVOT_FORMULAS_PASS` on an `assert` that compares a closed form to
an **asserted** linearization.  The message reads as a verification of
(5.9)-(5.15); it is a consistency check between two statements of the same
unproved formula, plus an exact-record comparison.  That distinction should
be visible in any promotion text.

No new exit-price assertion is made in this audit, so no `charge_basis` line
is due.

## 7. Where the report is stronger than it says

- (2.3) is four identities, not five: `D4 = c L` is automatic.
- The provenance of `H_t` is a theorem, not an observation: `[X^t]C11 =
  t(3t+1)H_t/(6q^3)`.
- The `2t` duplicate recurrence is fully symbolic and needs no band table.
- The `a_(e,0)` elimination that (2.1) presupposes is a constant unit pivot
  `3q` at band `2t`, tag `12`, for every `t`.

## 8. Cheapest test to close the gap

Derive (5.9), (5.12), (5.15) symbolically in `(t,j)` over
`Q(t,j)[d]/(3d^2-t-1)`:

1. perturb `C` by `s^(t-1-j)` (resp. `U` by `s^(q-j)`) with an indeterminate
   coefficient;
2. propagate through `T' = (g/2y)(5C+3sC')` band-by-band using (5.7b), then
   through the Euler inverse `[L^m]S = e_m/(y(2m+1))`;
3. read `[s^(4t+1-j)]` of `E_t` and take the derivative in the perturbation.

This is exactly what `terminal_laurent_model.build` does at fixed `t`; the
only change is symbolic `t`.  Success yields `b_j`, `d_j`, `n_j` and closes
the `t>=2` spine as `PROVED`.  Expected cost: one short driver, minutes, not
hours — the recurrences are already triangular and every diagonal is
`2my`, `(2m+1)y`, or `g`.

Two smaller items, both cheap: make §3's dependence on the banked
`3t+4` Q-constant first spine an explicit citation rather than "the charged
coefficient-space boundaries"; and note the `L`-division in the (2.3)->(2.4)
direction with its nonzerodivisor justification.

## 9. Reproduction

```text
box/k16spinegate-20260903/
  inputs.sha256                 receipt-generated manifest, 19/19 OK
  gate1_compact.py              35/35 PASS   section 2 re-derivation
  gate1e_chart.py               30/30 PASS   section 2 vs charged generator
  gate2_support.py              41/41 PASS   support, (5.7a), duplicates
  gate3_norms.py                38/38 PASS   every pivot norm + split obstruction
  gate3b_pivot_formulas.py      closed forms vs exact records t=2,3,4,5
  gate4a_rebuild.py             independent Laurent rebuild; t=2 and t=3
                                match the charged records field by field
  regen_terminal_laurent_t{2,3}.json
  gate4b_t2_product.json        both fibres x both charts at split t=2
  t1_chart.sing                 t=1 base case from the frozen chart builder
  replay/                       17 Singular replays, all UNIT
```

Total independent checks: **144 symbolic PASS, 0 FAIL**, plus 17 Singular
`UNIT` verdicts and one `t=1` chart certificate with four controls.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `23302`.
- Body SHA-256:
  `9b01ee5348ae30ff078472c161ba7700cf096fe72359eb001f95f0a5435acc2c`.
- Frozen basis: `285610bcb24ed60d1a69ea3c06521d157437651e`.
