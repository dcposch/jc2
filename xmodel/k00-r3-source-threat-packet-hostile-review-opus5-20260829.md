# Hostile review: K00 valuation-three source/threat packet

Reviewer: Claude Opus 5 (independent adversarial)
Date: 2026-08-29 UTC
Basis: `31777ce90994a106aade85064c0d868e32863f94`
Target: `xmodel/k00-r3-source-threat-packet-sol56-20260829.md`

## 0. Headline

The packet's mathematics is, with two exceptions noted below, **correct and
independently reproducible**. I rebuilt every load-bearing identity from
`tails.json` and the pinned compiler using my own polynomial/series engine,
importing nothing from the packet's replay or from the pinned R2 engine.
Every displayed exact identity in Sections 4, 5.1, 5.2, 5.3 and 5.4 reproduced
byte-for-byte in content.

Two findings dominate:

1. **Custody break.** The replay file in the tree is *not* the artifact whose
   SHA-256 the packet declares. This is a hard custody failure, not a
   formatting artifact.
2. **The residual list is not minimal.** All three cells the packet passes
   forward — `R3-00-ER1(+)`, `R3-00-ER1(-)`, `R3-00-ER2` — are **empty at
   grade 12**. The packet's grade-11 analysis is correct; its framing that
   these cells "carry the remaining grade-12--19 equations" overstates the
   residual by seven grades.

The Grok log was not opened and is not used as evidence anywhere below.

## 1. Custody

| artifact | declared | recomputed | verdict |
|---|---|---|---|
| packet, full | `6940e1ea…8dc4` | `6940e1ea…8dc4` | PASS |
| packet, body | `c2fffead…dcbd` | `c2fffead…dcbd` | PASS |
| body bytes | 19763 | 19763 | PASS |
| body-end marker | unique standalone | 1 occurrence | PASS |
| `tails.json` | `d72f774c…3848` | `d72f774c…3848` | PASS |
| canonical semantic tails | `6eed03d4…87e8` | `6eed03d4…87e8` | PASS |
| `compile_contracted_source_v20r2.py` | `2ac7653c…6d2b` | `2ac7653c…6d2b` | PASS |
| pinned R2 engine | `2c918d5b…e7c4` | `2c918d5b…e7c4` | PASS |
| **preflight replay** | **`bac4b688…86ba`** | **`a6eec646…3b94`** | **FAIL** |

The replay mismatch is real. It is not CRLF/LF, not a trailing-newline
variant, and not a locale artifact — I tested all four normalizations and none
reaches the declared digest. Two corroborating signals:

- mtimes: packet `2026-08-29 13:28:39`, replay `2026-08-29 13:30:05`. The
  replay was last written **86 seconds after** the packet body was sealed.
- The packet's Section 8 "Observed output" block omits the
  `RUNTIME_SECONDS=…` line that the present script unconditionally prints.

So the bytes I reviewed post-date the seal. The packet's Section 7 item 7
("Hash those exact public bytes, not a private shorthand") is violated by the
packet itself. **Repair: re-seal, or reissue the packet with the replay digest
recomputed from the shipped bytes.**

`h` = `63*d4+20` was read from the V14 witness and matches the packet's
`h=20+63d4`; the compiler's own `EXPECTED` dict pins that witness and the six
unit multipliers, so that part of the chain closes transitively through the
(correctly pinned) compiler.

## 2. Replay execution (item 9, first half)

Both runs PASS with identical banners:

```text
ordinary  : python3 …preflight….py            RUNTIME_SECONDS=13.397682
optimized : python3 -O …preflight….py         RUNTIME_SECONDS=13.289551
```

`-O` is safe here: there are **zero** bare `assert` statements in either the
preflight or the pinned engine (`assert_zero` raises explicitly via `fail`),
so optimized mode cannot vacuously pass. That is a genuine strength.

The packet's "observed runtime was under nine seconds in both ordinary and
optimized mode" did not reproduce (13.3--13.4 s here). Hardware-dependent;
noted, not scored.

## 3. Item-by-item verdicts

### Item 1 — source/open conditions, boundary zeros, custody, slots, census

**CONFIRMED, with a replay repair.**

- Exact valuation three, `x != 0`, and the honest cover
  `D(x0) union … union D(x5)` are correctly stated; no `xj`, `kappa` or
  `Jdet[0]` is normalized to one anywhere in the packet.
- **Five boundary zeros verified exactly.** The pinned compiler's
  `source_columns()` declares 169 columns of which exactly five carry
  `FIXED_ZERO_BEFORE_SOLVE`: `k6[0]`, `k2[0]`, `mu2[0]`, `mu4[0]`, `mu6[0]`,
  leaving **164 FREE**. The packet's "164 free columns after its five boundary
  zeros" is therefore correct and directly checkable — I initially failed to
  reconstruct it and was wrong to doubt it.
- 569 tails: reproduced by my own reconstruction, with the weight law
  `sum(monomial*weights) == 12+ell` and load-linearity re-verified per term.
- 98 root slots: `7 * 14 = 98` is correct arithmetic.
- **122-column census: correct, and I derived it structurally rather than
  accepting it.** From my reconstructed minimum homogeneous degrees
  (`R>=2`, `A10>=2`, `A6>=1`, `A2>=1`) and valuation three, the first grade at
  which each column can act is

  ```text
  d_j[16] -> 19,  d_j[17] -> 20
  k10[11] -> 19,  k10[12] -> 20
  k6[10]  -> 19,  k6[11]  -> 20
  k2[6]   -> 19,  k2[7]   -> 20
  mu2[5]  -> 19,  mu4[3]  -> 19,  mu6[1] -> 19,  Jdet[0] -> 19
  ```

  Every claimed-live frontier column lands exactly at 19 and every
  dormant-frontier column exactly at 20. The cutoff is tight in all eight
  blocks. `84+12+10+6+5+3+1+1 = 122`.
- **"Inert rather than zero" typing is correct** and is the right discipline;
  `frontier_dependency_controls()` genuinely tests it (bumping `d[17]`,
  `k10[12]`, `k6[11]`, `k2[7]` must not move any row in grades 6--19).

**REPAIR (replay).** Two of the three census checks in the replay are
tautologies over constants and cannot fail for any source:

```python
if 7 * len(range(6, 20)) != 98:          # 98 != 98
active = (6*len(range(3,17)) + len(range(0,12)) + …)
if active != 122:                        # 122 != 122
```

They verify the packet's arithmetic, not that the source has those slots or
that column can act. The only live support for the 122 is
`frontier_dependency_controls`, and that probes only the frontier at a
**single** numeric fixture. A one-point non-change is not a proof of
inertness. The structural argument above *is* a proof and should replace it.

### Item 2 — raw and contracted calendars

**CONFIRMED.**

My independent reconstruction reproduces Section 3.1 exactly:

```text
R    234 | 234 | 2345 | 2345 | 2345 | 3456 | 23456
A10  23  | 234 | 234  | 234  | 2345 | 2345 | 2345
A6   12  | 12  | 123  | 23   | 123  | 234  | 1234
A2   1   | 1   | 1    | 12   | 12   | 12   | 123
```

A structural fact worth naming, which the table encodes only implicitly and
which is genuinely load-bearing: **every `R_l` has zero degree-0 and degree-1
part**, although individual tail terms (e.g. row 4, `C0^1 C6^4`) supply both.
The cancellation is what makes grade 6 the first arrival rather than grade 0
or 3.

- raw K10 quadratic at `2+2*3 = 8` — CONFIRMED (`A10` min degree 2);
- raw K6 linear at `6+1+3 = 10` — CONFIRMED (`A6` min degree 1);
- contracted `D10` first at 11, `D6` first at 13 — CONFIRMED. I parsed the
  contracted vector and recovered the supports exactly as claimed:
  `D10:{3,4,5,6,7}`, `D6:{2,3,4,5}`, `D2:{2,3,4}`, `u2:{1,2,3}`, `u4:{1,2}`,
  `u6:{1}`, `-h/4:{0,1}`.

The contraction raises the minimum degree by one in each load block, delaying
each arrival by exactly three grades. The packet is right that this is the
principal calendar mutation to reject.

**REPAIR (custody).** The contracted supports are **not derivable from the two
artifacts Section 1 pins.** I could only verify them against
`cases/…kuranishi_v20_20260827/aws_r6b_r2_pass/output/K_VECTOR.txt`, a prior
AWS output that the packet does not pin. Pin it — sha256
`940d9e42e1fce079f4bfcb5e1a319884c4b606f32f50ba435d5dc294ed7ff24a` — or state
that Section 3.3 is conditional on a Singular run. Separately, the replay's
calendar "checks" compare hardcoded dicts to hardcoded arithmetic
(`raw_anchors["K10_2"] != 2+2*3`, `contracted["D10_3"] == raw_anchors["K10_2"]`)
and are vacuous as source checks.

### Item 3 — reduced leading cone and rank fan

**CONFIRMED.**

- All seven leading quadrics lie in `(A,B)`; the parameterization
  `x=(2b+2u,a,b,8a+v,b-u,16a+4v)` is exactly `V(A,B)` (injective, 4-dimensional,
  codimension 2).
- **Radical settled decisively and cheaply.** By exact linear algebra over `Q`
  I showed `A^3, A^2B, AB^2, B^3` all lie in the degree-3 part of the quadric
  ideal. Hence `(A,B)^3 ⊆ (Q) ⊆ (A,B)`, and since `(A,B)` is prime,
  `sqrt((Q)) = (A,B)`. This holds over any characteristic-zero field, not just
  the closure. No Groebner basis needed.
- `DQ` rows on `V(A,B)`: rows 1,3,5,7 are `(3/1024, -3/8192, -3/131072,
  -3/1048576)` times `(u,-v)`; row 2 is `((3/256)v, (3/16384)u)`; rows 4 and 6
  vanish identically. Exactly **four** of the 21 minors are nonzero and each is
  a rational multiple of `Delta = u^2+64v^2`. Fan confirmed.
- **Field/closure qualification is correct and is doing real work.** Over `Q`
  (or any real field) `Delta = 0` forces `(u,v)=(0,0)`, so rank one is empty;
  the `epsilon = ±1` branches exist only once `i` is adjoined. The packet says
  this correctly and replays both conjugates.

Two observations the packet should absorb:

- `Q6 ≡ 0`. The "seven leading quadrics" are really six. Harmless, but
  "seven" invites a producer to look for a seventh condition that is not there.
- Non-reducedness is real and I can localize it: `A^2` and `B^2` are **not** in
  the degree-2 span of the quadrics (only `A*B` is). So `(Q) != (A,B)` and the
  packet's warning to retain the original quadrics for any scheme or nilpotent
  claim is well-founded, not boilerplate.

### Item 4 — leading rank-two and rank-one exclusions at grade 9

**CONFIRMED (both exceptional branches, both Gaussian conjugates).**

Rank two. Grade 6 vanishes on the cone; grade 7 is *exactly* `DQ(x)(y)`, so
rank two forces `y` onto the cone. The grade-8 cokernel vanishes identically
and grade 8 vanishes identically at

```text
A(z) = (10/3)*kappa*v,   B(z) = -(10/3)*kappa*u.
```

At grade 9 the five cokernel rows are pure cubics in `(a,b,u,v)`: `y`, `z`,
`w`, `kappa` and `k10[1]` all cancel out of the cokernel while appearing in
the raw rows — I verified the cancellation is genuine, not an artifact.

```text
G9_6 = 3/1024*u*v^2 - 1/65536*u^3           = u(192v^2-u^2)/65536      MATCH
G9_4 = -3/32*a*u*v - 3/32768*b*u^2
       + 3/512*b*v^2 - 21/512*u*v^2
       + 3/32768*u^3                        = (3/32768)(…)             MATCH
```

- `u=0` branch: row 4 gives `(3/512)b*v^2 = 0` so `b=0`; then
  `row3+row1/8 = (1/4)v^2(3a+v)` and `row5+row1/128 = -(3/64)v^2(2a+v)` give
  `v+3a=0` and `v+2a=0` — exactly as claimed. There is in fact a **fourth**
  independent equation, `row7+row1/1024 = -(3/512)a*v^2`, forcing `a=0` and
  hence `v=0`. Over-determined; contradicts rank two.
- `u^2=192v^2` branch: **the packet's "exact two quotient constants `1/8` and
  `-1/64`" reproduce.** Working over `K = Q(r)`, `r^2 = 192`, with `a,b` free
  *in `K`* and `v=1` by homogeneity, row 4 reads
  `-3/256*b - (3/32*a + 3/128)*r = 0`, i.e.

  ```text
  b = -2r(1+4a).
  ```

  Substituting, `s3 = -2-6a` but `s5 = 1/8` and `s7 = -1/64`, both nonzero
  constants. Branch empty.

  I record a correction to my own first pass: I initially split these
  equations into rational and `sqrt(3)` parts, which is only legitimate if
  `a,b ∈ Q`. In the field-valued problem `a,b` range over the quadratic
  extension and the split is invalid. The packet's route is the correct one.

Rank one. `G8_4 = -(3/4096)v^2*lambda^2` for both `epsilon`, forcing
`lambda=0`. After the complete grade-8 solve — the six cokernel rows vanish
identically and row 1 gives `A(z) = -(i*epsilon/8)B(z) + (20/3)kappa*v`,
retaining `B(z)` as the tangent parameter — row 6 at grade 9 is

```text
G9_6 = epsilon*i*v^3/32,
```

**independent of the tangent parameter**, nonzero on `v != 0`. Both conjugates
die. Confirmed for `epsilon = +1` and `-1` separately, not by conjugation.

Consequently every survivor has `x = ell(s,t) = (2s,t/8,s,t,s,2t)` with
`(s,t) != (0,0)` — confirmed, including that `(s,t) != (0,0)` is exactly the
exact-valuation-three open and is not lost.

**REPAIR.** The packet never defines "quotient constants", never states the
row-4 relation `b = -2r(1+4a)` that produces them, and never says that `a,b`
range over the quadratic extension. As written the phrase is unreproducible;
the underlying claim is true. The relation is also buried in the imported
`qpair_branch_reduce` docstring, which reads as an R2 (valuation-two) artifact
— it happens to coincide, but a producer cannot know that from the packet.

### Item 5 — old-plane grade-11 and grade-12 exclusions

**CONFIRMED.**

On `x = ell(s,t)`: grades 6 and 7 vanish, and grade 8 is *exactly* `Q(y)=0`
because `kappa*A10^[2]` vanishes identically on the old plane — I verified
`A10^[2](ell(s,t)) = 0` for all seven rows. Grade 9 is exactly `DQ(y)(z)`.

Next rank two: grade-10 cokernel vanishes identically and grade 10 vanishes at
`A(w)=2st+(10/3)kappa*v`, `B(w)=s^2-64t^2-(10/3)kappa*u`. At grade 11

```text
G11_3 + (1/8)G11_1 = -(3/2048) D          MATCH
G11_4              = -(3/32768) F         MATCH
sD - tF   = -2uv(s^2+64t^2)               MATCH
sF + 64tD = (u^2-64v^2)(s^2+64t^2)        MATCH
```

**REPAIR (Section 5.2, load-bearing wording).** The sentence "The nonisotropic
and two isotropic source cases give the same exact contradiction with
`Delta_y!=0` as the displayed identities themselves" is **wrong as stated**.
On `s^2+64t^2 = 0` both displayed identities degenerate to `0=0` and supply
nothing. The correct argument uses `D` directly: with `s = epsilon'*8i*t`,

```text
F = 8i*epsilon' * D,     D = t*(u - 8i*epsilon'*v)^2,
```

so `D=0` with `t!=0` forces the *double* root `u = 8i*epsilon'*v`, whence
`Delta_y = 0` — contradiction. The conclusion stands; the stated reason does
not. A producer following the packet's sentence would leave the isotropic
cases unproved.

Next rank one: grade-10 row 4 gives `-(3/4096)v_y^2 lambda^2`, so `lambda=0`;
grade-11 row 4 is `(3v_y^2/256)(s - epsilon*8i*t)`, forcing `s=epsilon*8i*t`
and `t!=0`; the sixth cokernel row reproduces the packet's four-term
expression exactly for both `epsilon`, and it does force `tau != 0` (setting
`tau=0` leaves `-(epsilon*5i/16)t^3 kappa = 0`, impossible on `D(kappa*t)`)
and then fixes one linear combination of `(u_z,v_z)`. Finally

```text
G12_6 = epsilon*i*v_y^3/32     MATCH (both epsilon)
```

and it is **stronger than the packet states**: `G12_6` is independent of the
entire grade-11 image solution, every kernel/tangent parameter, `d[7]`, and
all available load coefficients. The producer need not solve grade 11 at all
to kill this cell. Localizers used — `v_y`, `Delta_y`, `t`, `kappa` — are all
correctly declared.

### Item 6 — next rank zero, third cone, and the K10 shift

**CONFIRMED. This is the strongest and most important part of the packet.**

Grade 9 vanishes identically on `y = ell(a,b)`. At grade 10

```text
G10_1 + 8*G10_3 = (3/2048) AZ*BZ                       MATCH
G10_4           = (3/524288)(BZ^2 - 64 AZ^2)           MATCH
```

which force `AZ=BZ=0` (if `AZ=0` then `BZ^2=0`; if `BZ=0` then `AZ^2=0`), and
all seven grade-10 rows then vanish — verified.

The central claim holds exactly. The complete grade-11 linear block is

```text
alpha_l(U,V) A(w) + beta_l(U,V) B(w),
U = u_z + (5/6)kappa*s,    V = v_z - (5/6)kappa*t,
```

with **no leakage into `w1..w4`** and with the *same* `alpha,beta` table as
`DQ`. I verified this in the opposite order (item 9): rather than assuming the
shift, I extracted the raw `7x2` coefficient matrix and **derived**

```text
row1 = [ 5/2048*kappa*s + 3/1024*u_z ,  5/2048*kappa*t - 3/1024*v_z ]
  =>  U = u_z + (5/6)kappa*s ,  V = v_z - (5/6)kappa*t
```

then confirmed `row2 = ((3/256)V, (3/16384)U)`, `row3,5,7 = -1/8, -1/128,
-1/1024` times row 1, `rows 4,6 = 0`, and that exactly four minors are nonzero
and each is a rational multiple of `Delta_eff = U^2+64V^2`.

**The mutation is decisive.** On the `DQ(z)` rank-zero locus `u_z=v_z=0` the
true effective pair is `((5/6)kappa*s, -(5/6)kappa*t)` with

```text
Delta_eff = (25/36) kappa^2 (s^2 + 64 t^2),
```

nonzero for generic `(s,t)`. So splitting by unshifted `DQ(z)` would label as
rank zero a cell that is in fact effective rank **two**. The packet's
insistence on `(U,V)` is not a stylistic preference; it is required for
correctness.

`E11_1` and `E11_2` reproduce exactly, and I can strengthen the packet's
"include": the remaining rows satisfy `E11_3 = -(1/8)E11_1`,
`E11_5 = -(1/128)E11_1`, `E11_7 = -(1/1024)E11_1`, and `E11_4 = E11_6 = 0`.
So the two displayed cubics are the **complete** independent set. Their
emptiness on `D(kappa) ∩ (D(s) ∪ D(t))` is correct: `t=0` forces `s^3=0`;
`3s^2=64t^2` gives `s*t^2*(64/3-192) = 0` hence `s=0` hence `t=0`.

### Item 7 — effective rank zero / one / two, and what actually remains

**CONFIRMED at grade 11; the residual list is REFUTED as minimal.**

Confirmed at the packet's own scope:

- effective rank zero empty at grade 11 (above);
- on `E1(epsilon)`, five of the six cokernel rows vanish **identically**, and
  the sixth is exactly `(5*kappa/65536)(s + epsilon*8i*t)^3`, forcing the wall
  `s = -epsilon*8i*t` with `t != 0`;
- on `E2`, all five cokernel rows vanish **identically**, so `E2` imposes no
  grade-11 condition at all. I confirmed this independently by showing all 35
  `3x3` minors of the augmented `[M | -c]` matrix vanish identically as
  polynomials, i.e. consistency is automatic wherever `rank M = 2`.

**New result — all three residual cells die at grade 12.**

*ER1(epsilon).* Solving the single grade-11 image coordinate on `D(t*kappa*V)`
and retaining `B(w)` as the tangent parameter, `d[7]`, `w1..w4`, `a`, `b`,
`z_a`, `z_b`, `k10[1]`, `k6[1]` all free, the grade-12 six-dimensional
cokernel contains two rows depending only on `(B(w), V, kappa, t)`, and they
satisfy the exact identity

```text
G12_row4 - (epsilon*i/2)(G12_row3 + (1/8)G12_row1) = (25/384) kappa^2 t^6 / V^2.
```

On `D(kappa*t*V)` the right side is a unit, so the two equations have no
common zero. `ER1(+)` and `ER1(-)` are **empty at grade 12**. Verified
symbolically in the localization and again by numeric specialization at four
independent points with no symbolic inverse.

*ER2.* Solving both normal coordinates by Cramer on `D(Delta_eff)` and
clearing `Delta_eff^2`, the five-dimensional grade-12 cokernel collapses to
**two** independent binary quadratics in `(U,V)` whose coefficients are
`kappa^2` times sextic forms in `(s,t)` — every other free parameter,
including `d[7]` and `w1..w4`, drops out. Their resultant is

```text
Res_{U:V}(Eq_A, Eq_B) = c * kappa^8 * (s^2 + 64 t^2)^12,
c = -390625/6120186961799060196950016  != 0.
```

So off the isotropic locus there is no common root at all. On the isotropic
walls `s = epsilon'*8i*t` both quadratics degenerate to the *same* perfect
square, with double root `U = -epsilon'*8i*V`, which gives
`Delta_eff = U^2+64V^2 = 0` — excluded from `ER2` by definition. Hence `ER2`
is **empty at grade 12** as well. Confirmed at five independent rational
points, including two on the isotropic walls.

The two results interlock consistently: `ER2`'s grade-12 equations degenerate
precisely onto the `ER1` locus, which dies by a different identity.

So the packet's Section 0 item 5 and Section 6 are true as *grade-11*
statements, but "The effective-rank-one cells carry the remaining
grade-12--19 equations and the effective-rank-two cell does likewise" is
misleading: none of them carries anything past grade 12.

### Item 8 — successor contract, localizers, mutation controls, coverage

**CONFIRMED, with the contract to be shortened.**

- Cokernel dimensions right: 6 on `ER1` (rank 1), 5 on `ER2` (rank 2).
- Localizers right and complete: `D(t*kappa*V)` on `ER1`;
  `D(kappa*(U^2+64V^2))` together with `D(s) ∪ D(t)` on `ER2`. On `ER1` the
  wall makes `D(t)` subsume `D(s) ∪ D(t)`, which is consistent.
- **No projectivization, and zeros are genuinely retained.** I checked the two
  places this could go wrong: `y = 0` is admissible and lands in `N0` — `a`
  and `b` do not appear anywhere in the grade-11 data, so nothing degenerates;
  `z = 0` gives `(U,V) = ((5/6)kappa*s, -(5/6)kappa*t) != (0,0)` and lands in
  `ER1` or `ER2` according to `s^2+64t^2`. Both are covered.
- The `L`/`N`/`E` tree is exhaustive and disjoint over a field containing `i`,
  and the packet correctly warns that `E` is the effective rank, not
  `rank DQ(z)`.
- Mutation control list is well chosen; see item 9 for which ones I exercised.

**REPAIRS.**

1. The contract should demand **one** further grade, not eight. Grade 12 is
   desk-scale (about one second per cell in my implementation).
2. The packet does not state the fact that makes the grade-12 continuation
   well-posed: the grade-12 linear block in `d[7]` carries the **same**
   `(U,V)` as the grade-11 block (`d[7]` pairs with `z` and, through `K10`,
   with `x`, exactly as `w` did). I verified this — the grade-12 cokernel rows
   are free of `d[7]`. A producer that re-derived a *new* effective pair at
   grade 12 would split unnecessarily; one that assumed `DQ(z)` would split
   wrongly.
3. Section 7's "Independent replay" list is a contract for the producer, but
   Section 8 presents the preflight as if it discharged it. The preflight does
   **not** implement the promised five boundary-zero negative fixtures, the
   grade-12--19 residual roots, or the contracted-vs-literal check. Say so.

### Item 9 — replay, opposite-order check, mutations

**DONE.** Ordinary and optimized runs in Section 2 above.

*Opposite-order exact check of the shifted fan.* Performed and passed — see
item 6. Rather than substituting `(U,V)` and confirming, I extracted the raw
grade-11 coefficient matrix and derived `U` and `V` from row 1, then
independently recovered the row proportionalities, the two zero rows, the four
nonzero minors and their `Delta_eff` factorization, plus the vanishing of all
35 augmented `3x3` minors.

*Live-tail mutation.* I rebuilt rows/loads from in-memory mutated copies of
`tails.json` (repository bytes untouched) and ran seven load-bearing
identities. 7 of 10 single-coefficient mutations were caught. The three
survivors are informative rather than alarming: they are `K10`/`K6` terms of
`d`-degree 3, or `K6` terms first acting at grade 16 — i.e. **the preflight's
grade-6--11 identities do not pin the whole 569-tail source.** Custody of
`tails.json` is therefore doing real load-bearing work and cannot be relaxed.

*192 control.* Live: `G9_6 - (193-variant) = -u*v^2/65536 != 0`.

*Unshifted-fan control.* Live and decisive, as quantified in item 6.

### Item 10 — scope audit

**CONFIRMED.** Section 9's firewall is accurate and I found no leakage: the
packet claims only field-valued finite-jet statements on one exact normalized
support, and explicitly disclaims periodicity, scheme-theoretic emptiness,
residual points, arcs, maps, Keller maps, other supports, and JC2. The
lifecycle banner ("NOT A GRADE-19 PRODUCER") matches the content.

Applying the same firewall to **my own** grade-12 result: it is a field-valued
finite-jet exclusion on one normalized support in characteristic zero. It is
not a residual point, not an arc, not a map, not a periodicity or attainment
or maximum-12 statement, and not JC2. By truncation it would exclude
same-source exact-valuation-three formal arcs — and nothing more.

## 4. Repairs

1. **Re-seal the replay.** Declared `bac4b688…`, actual `a6eec646…`; the file
   post-dates the packet seal by 86 s. Blocking for promotion.
2. **Fix Section 5.2's isotropic justification.** Use `D = t(u-8i*eps'*v)^2`,
   not "the displayed identities themselves", which degenerate to `0=0` there.
3. **Define the "quotient constants".** State `b = -2r(1+4a)` from row 4 over
   `K = Q(r)`, `r^2 = 192`, and note that `a,b` are extension-field elements.
4. **Pin the contracted artifact** (`K_VECTOR.txt`, sha256 `940d9e42…f24a`) or
   mark Section 3.3 conditional. It is not derivable from the two Section 1
   pins.
5. **Replace the tautological census checks** with the structural degree
   argument, which proves both liveness and dormancy outright.
6. **Correct the residual claim** and shorten the successor contract to one
   grade (see Section 5).
7. Minor: say "six nonzero leading quadrics" (`Q6 ≡ 0`); state that `R_l` has
   no degree-0 or degree-1 part; note that `G12_6` needs no grade-11 solve;
   note that `E11_3,5,7` are multiples of `E11_1` and `E11_4 = E11_6 = 0`;
   drop or re-measure the "under nine seconds" claim.

## 5. Maximum exact statement safe to promote

At the packet's own scope, and independently reconstructed here from the
frozen tails and compiler:

> On the frozen V20R2 source at the declared normalization
> (`C0=(1+d0)/256, C1=d1, C2=(1+d2)/16, C3=d3, C4=(3+d4)/8, C5=d5, C6=1`;
> `k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0`; `k10[0]=kappa != 0`, `Jdet[0] != 0`),
> for `d = Lambda^3 x + Lambda^4 y + Lambda^5 z + …` with `x != 0`, over any
> field of characteristic zero containing `i`:
>
> 1. the reduced leading locus is `A(x)=B(x)=0`, with `sqrt((Q)) = (A,B)` and
>    `(A,B)^3 ⊆ (Q)`; the fan of `DQ(x)` is `rank 2 ⇔ Delta != 0`,
>    `rank 1 ⇔ Delta = 0 != (u,v)`, `rank 0 ⇔ u=v=0`;
> 2. leading rank one and leading rank two are empty at grade 9;
> 3. hence `x = ell(s,t)`, `(s,t) != (0,0)`, and grade 8 is exactly `Q(y)=0`;
> 4. next rank two is empty at grade 11; next rank one is empty at grade 12
>    via `G12_6 = epsilon*i*v_y^3/32`;
> 5. on next rank zero, grade 10 forces `A(z)=B(z)=0`, and the complete
>    grade-11 linear block is `alpha_l(U,V)A(w)+beta_l(U,V)B(w)` with
>    `U = u_z+(5/6)kappa*s`, `V = v_z-(5/6)kappa*t` — **not** `DQ(z)`;
> 6. effective rank zero is empty at grade 11 by
>    `E11_1 = (5kappa/4096)t(3s^2-64t^2)` and
>    `E11_2 = (5kappa/65536)s(s^2-192t^2)`.

That is exactly the packet's content and I endorse promoting it, once repair 1
is discharged.

I additionally offer, as a **review-side result requiring independent producer
confirmation before promotion** (it was computed by me, not by the packet, and
campaign hygiene should not let a reviewer promote its own arithmetic):

> 7. `R3-00-ER1(+)`, `R3-00-ER1(-)` and `R3-00-ER2` are all empty at grade 12.
>    Hence the entire exact-valuation-three lane on this support is empty at
>    grade 12, and no residual cell survives.

## 6. Cheapest decisive successor

**One grade, three cells, desk-scale — not grades 12 through 19.**

Start from the packet's own minimal discriminator (`x = ell(s,t)`,
`y = ell(a,b)`, `z` on the cone, `U`,`V` as defined), then:

1. On `ER1(epsilon)`: impose `s = -epsilon*8i*t`, solve the one grade-11 image
   coordinate on `D(t*kappa*V)` keeping `B(w)` free, and evaluate the two
   grade-12 cokernel rows `row4` and `row3+row1/8`. Certificate: the exact
   identity `row4 - (epsilon*i/2)(row3+row1/8) = (25/384)kappa^2 t^6/V^2`,
   a unit on the retained localizer. Both signs, separately.
2. On `ER2`: solve both normal coordinates on `D(Delta_eff)`, clear
   `Delta_eff^2`, and extract the two independent binary quadratics in
   `(U,V)`. Certificate: `Res(Eq_A,Eq_B) = c*kappa^8*(s^2+64t^2)^12` with
   `c != 0`, plus the observation that on `s^2+64t^2 = 0` both quadratics are
   the same perfect square with double root `U = -epsilon'*8i*V`, forcing
   `Delta_eff = 0`, which `ER2` excludes.

Both certificates are checkable by direct substitution in the original
seven-row presentation and need no Groebner basis, no elimination, and no AWS.
The producer should reconstruct them independently from the tails rather than
importing them from this review. If they hold, the correct output is a
grade-12 emptiness result for the whole lane, not three serialized residuals.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `27921`.
- Body SHA-256:
  `c567c05ea41f3f8858efe5b235cab19ffc847915cd096482d2a97faf2f1ac057`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
