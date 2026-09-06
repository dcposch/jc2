# CQ-ELIM: the `F`-eliminated chart at (99,66) and D=108 — built, counted, partly decided

Lane `cq-elim-opus5-20260906`, basis `7fd46774`, start 2026-09-06 00:28:04 UTC, implementing
PROPOSAL CQ-ELIM from the sealed Opus ideation submission. No ledger edits, no `jc2-lean`, no
other `ideation-*` input.

**Headline.** (E1)/(E2) are correct as *consequences* and re-proved here in one line; the
submission's **biconditional is false as literally stated** (a `J(F,G) = -1` pair satisfies
`J(J(Q,G),G) = -2`), the correct exact equivalence being the *chart* identity
`J(F_def,G) = -(1/2)*J(J(Q,G),G)`. The restriction to `m_1 = 2` is **unnecessary**: the iterated
Jacobian eliminates `F` linearly at every `m_1`, so the reduction covers **66/66** roster rows, not
44. The eliminated chart is built and counted at (99,66) and D=108; its degree/attainment block is
**DECIDED PROPER** with an exact rational witness (and the cone family is excluded twice,
independently); the Keller block is **compute-bound** at weight `omega = 0`.

## 0. Custody

The receipt `xmodel/cq-elim-opus5-20260906.run.v2` carries seven numbered
`charged_input_<i>_sha256=`/`_basename=` pairs. I built the manifest mechanically with `awk`,
wrote it to `/tmp/cq_manifest.txt`, and ran `sha256sum -c` against
`/tmp/jc2-lane.qWrZD0/inputs`: **7/7 OK**, no content mismatch. Drivers and JSON are in
`box/cq-elim-20260906/` (76 KB total, manifest `evidence.json`). **Disk discipline:** `df -h /`
showed 2.8 GB free at start and 0.5 MB at the end — the host filled from other lanes during the
run. Nothing above 10 MB was retained by this lane; no artifact trees, no CAS dumps.

---

## 1. `(E1)`/`(E2)` verified myself — one correction, one extension

### 1.1 The identity, and why it is one line

For **any** `Phi(u,v)` and any `F,G`, the chain rule gives `P = Phi(F,G)`,
`P_x = Phi_u F_x + Phi_v G_x`, `P_y = Phi_u F_y + Phi_v G_y`, hence

```text
   J(Phi(F,G),G) = Phi_u(F,G)*J(F,G) + Phi_v(F,G)*J(G,G) = Phi_u(F,G)*J(F,G).      (CR)
```

At `m_1 = 2` Moh Prop 3.1's family is `Phi = v^{n_1} - u^2 + sum{ u^i v^j : n i + m j < n_1 m,
j < n_1 }`, and the weight inequality forces `i < m_1 = 2`, so `Phi_u = -2u + (poly in v)`. At
(99,66) (`n_1 = 3`, `m_1 = 2`) the licensed monomials are exactly `1, v, v^2, u, uv`, i.e.
`Phi = v^3 - u^2 + a v^2 + b u v + c u + d v + e_0` — confirming the submission's display.
With `J(F,G) = 1`, (CR) reads `J(Q,G) = -2F + bG + c`, which is (E1); applying `J(-,G)` again
gives `J(J(Q,G),G) = -2J(F,G) = -2`, which is (E2)'s forward direction.

`verify_e1e2.py` checks (CR) on three random dense `(F,G)` with symbolic `a,b,c,d,e_0`:
residual `0` in all three.

### 1.2 CORRECTION — the literal biconditional is false

The submission writes `J(F,G) = 1  <==>  J(J(Q,G),G) = -2`. Without assuming `J(F,G) = 1`,
(CR) gives, with `j := J(F,G)`,

```text
   J(J(Q,G),G) = -2 j^2 + Phi_u(F,G)*J(j,G),
```

so `j = -1` also yields `-2`. `verify_converse.py` exhibits this: `F = -x`, `G = y + x^2`,
`Phi = v - u^2 + b u + g` (the `n_1 = 1, m_1 = 2` shape) has `J(F,G) = -1`, `Q = y - b x + g`,
`J(Q,G) = -b - 2x` and `J(J(Q,G),G) = -2`. (E1) fails there — `(bG + c - J(Q,G))/2 = b + x` while
`F = -x` — which is exactly what pins the sign.

**The statement that is true, and is the one the chart uses.** Let `Q, G` be arbitrary and
*define* `F := (bG + c - J(Q,G))/2`. Then, unconditionally,

```text
   J(F,G) = (1/2)[ b*J(G,G) + J(c,G) - J(J(Q,G),G) ] = -(1/2)*J(J(Q,G),G),           (E2*)
```

so `J(F,G) = 1  <==>  J(J(Q,G),G) = -2` **as an identity in the chart unknowns**. Verified on
four random `(Q,G)` with symbolic `b,c`: residual `0`. This is the form I use below; the
correction does not damage the proposal, it repairs its direction.

### 1.3 EXTENSION — `m_1 >= 3` is in scope after all (44/66 -> 66/66)

The submission withdraws the reduction for `m_1 >= 3` because `Phi_u = -m_1 u^{m_1-1} + ...`
determines `F` only up to an `(m_1-1)`-th root. That is avoidable. Iterating (CR) with
`J(F,G) = 1`,

```text
   J^{(k)}(Q,G) := J(...J(Q,G)...,G)  (k times)  =  (d^k Phi / du^k)(F,G).            (ITJ)
```

Since the weight inequality forces `i <= m_1 - 1` in every lower monomial,
`d^{m_1-1}Phi/du^{m_1-1} = -m_1! * u + (m_1-1)! * C(v)` with `C(v) = sum_j c_{m_1-1,j} v^j`, and
`d^{m_1}Phi/du^{m_1} = -m_1!`. Hence, for **every** `m_1 >= 2`,

```text
   (E1-gen)  F = [ (m_1-1)! * C(G) - J^{(m_1-1)}(Q,G) ] / m_1!         -- linear in the iterate
   (E2-gen)  J(F,G) = 1   <==>   J^{(m_1)}(Q,G) = -m_1!                -- one scalar identity
```

and the chart-direction equivalence of §1.2 holds verbatim (`J(C(G),G) = 0`). `verify_e1e2.py`
checks (ITJ) for `k = 1..m_1` and both displays at `m_1 = 2,3,4` on genuine Keller pairs
(`(x, y+x^{m_1})` and a composed pair): `J^{(m_1)}(Q,G) = -2, -6, -24` as predicted, and the
`F`-recovery residual is `0` in every case.

Recounting `m_1 = m/gcd(n,m)` on `roster.jsonl` reproduces the submission's distribution exactly —
`{2: 44, 3: 14, 4: 5, 5: 2, 7: 1}` — so the extension moves the reduction's scope from **44** to
**all 66** rows. The 22 newly-covered rows carry an `(m_1-1)`-fold iterate instead of a single one:
that raises the differential order of the recovery, not the number of unknown blocks.

### 1.4 What the elimination does NOT carry — the relaxation gap, measured

`Q = Phi(F,G)` is **not** recovered by (E1)+(E2). With `F` defined by (E1),
`R := Q - Phi(F,G)` satisfies `J(R,G) = J(Q,G) - Phi_u(F,G)*J(F,G) = 0`, i.e. `R` lies in
`ker J(-,G)` (classically `R, G` are then both polynomials in a common `H`). `verify_converse.py`
demonstrates this concretely: replacing `Q` by `Q + rho*G^2` preserves (E2) and recovers the *same*
`F`, while `rho*G^2` is not in the `Phi`-family for `n_1 = 1`. So the eliminated chart is a genuine
**relaxation** of the `F`-chart. §5 argues why that is safe for a kill and unsafe for a survivor.

---

## 2. The eliminated chart at (99,66) — built and counted

### 2.1 Compact form

Write `Q = lambda*Qt` with `Qt` top-monic. `(E2*)` says the whole chart is one identity in the
derivation `D_G := J(-,G)`:

```text
   D_G^2 (Qt) = mu,   mu = -2/lambda != 0,       F = (bG + c - lambda*D_G Qt)/2.       (CQ)
```

`D_G(F) = 1` is `(CQ)`; nothing else of the Keller condition survives. Read backwards, `(CQ)` is
Moh's characteristic-degree condition in one line: *`F` has a `D_G`-antiderivative of degree `D_2`*.

### 2.2 The blocks, in the band (graded) presentation

Astra's licensed data for (99,66) is consumed unchanged: `P_0 = y^3(y-x)^8` (degree 11),
`F_top = P_0^9`, `G_top = P_0^6`, `D_2 = 55` and `Q_55 = lambda*y^15(y-x)^40 = lambda*P_0^5`
(char-degree r2, (3), from Prop 4.5 p.169 + Theorem A); ratios `99:66:55 = 9:6:5`. Top consistency
is automatic and checked: `G_top^3 - F_top^2 = 0` and `J(Q_top,G_top) = 0`.

Decompose into homogeneous parts and index by **band**: `Q_{55-p}` has band index `p`,
`G_{66-q}` has band index `q`. Binary forms are dehomogenised at `x = 1`; Euler's relation gives,
for homogeneous `A` (degree `a`), `B` (degree `b`),
`J(A,B)|_{x=1} = a*A*B' - b*A'*B` (`band.py`, checked against `J(P_0^5,P_0^6) = 0`).

The chart is then

```text
 (T)  Q_55 = lambda*P_0^5, G_66 = P_0^6                       [Prop 4.5 / Thm A, consumed]
 (I)  R_nu := sum_{p+q=nu} J(Q_{55-p},G_{66-q}) = 0,  nu = 1..19
      R_20 = -2*P_0^9                                          [deg F = 99 with its top form]
      localizer  Z*lambda - 1                                  [attainment]
 (II) sum_{a+b=omega} J(F_{99-a},G_{66-b}) = 0 (omega = 1..162), = 1 at omega = 163,
      with F_{99-a} := -(1/2)*R_{20+a} + (b*G_{99-a} + [c])/2  [ = (E2) as coefficient rows ]
 (S)  the delta = 2 [2,1] source faces, transported (§2.5)
```

Block (I) is *new*: in the `F`-chart it is implied by the characteristic block and never appears
as rows. It says exactly `deg J(Q,G) = 99` with the prescribed top, which is what makes (E1)
produce an `F` of the right degree.

Every row of (I) and (II) is **weight-homogeneous** for the band grading `w(Q_{55-p}) = p`,
`w(G_{66-q}) = q` (each term of `R_nu` has weight `nu` by construction; each `(II)` row at `omega`
has weight `20 + omega`). The only inhomogeneous generators are the two localizers. This is the
same "run graded" situation the campaign already records for Moh order charts.

### 2.3 The (I)-block obstruction is a two-point divisibility — exactly

At band `nu` the new unknowns enter through the fixed linear operator

```text
   L_nu(A,B) := J(A,P_0^6) + J(P_0^5,B) = P_0^4 * [ 6*P_0*J(A,P_0) - 5*J(B,P_0) ],
```

so band `nu` reads `L_nu(Q_{55-nu},G_{66-nu}) = -C_nu`, `C_nu := sum_{i,j>=1, i+j=nu}
J(Q_{55-i},G_{66-j})`. Exact rank computation (`profile.py`, `obstruction.py`) gives, for
`nu = 1..20`:

| `nu` | dom `(A,B)` | rows | `rank L_nu` | `ker L_nu` | obstruction rows |
|---:|---:|---:|---:|---:|---:|
| 1 | 121 | 119 | 66 | 55 | 53 |
| 2 | 119 | 118 | 65 | 54 | 53 |
| **11** | 101 | 109 | **55** | 46 | **54** |
| 12 | 99 | 108 | 55 | 44 | 53 |
| 20 | 83 | 100 | 47 | 36 | 53 |

and **`Im L_nu = D * {forms of degree 66-nu}` exactly for all `nu` but `nu = 11`**, where

```text
   D = y^14 (y-x)^39 = P_0^4 * y^2 (y-x)^7 = Q_top / (lambda * y * (y-x)),   deg D = 53.
```

So the obstruction at band `nu` is precisely **`D | C_nu`** — the accumulated cross-term must
vanish at each point at infinity to order `mult_xi(Q_top) - 1` (`14` at `y = 0`, `39` at `y = x`).
The `nu = 11` anomaly is a resonance: `11 | 55-11` and `11 | 66-11`, so both `J(-,P_0)` maps
gain a kernel and one extra row appears. Cumulatively over `nu <= 19`: **875** kernel
parameters against **955** obstruction rows.

### 2.4 Counts, against the `F`-based chart (`counts.py`)

| | (99,66) `F`-chart | (99,66) CQ-chart | D=108 `F`-chart | D=108 CQ-chart |
|---|---:|---:|---:|---:|
| `F`-block / `Q`-block | 5050 | **1596** | 5995 | **2080** |
| `G`-block | 2278 | 2278 | 2701 | 2701 |
| scalars `a,b,c,d,e_0,lambda,Z` | 7 | 7 | 7 | 7 |
| **unknowns** | **7335** | **3881** | **8703** | **4788** |
| Jacobian / (E2) rows | 13530 | 13530 | 16110 | 16110 |
| characteristic block | 10441 | — | 11936 | — |
| degree-drop block (I) | — | 2190 | — | 3025 |
| **rows** | **23971** | **15720** | **28046** | **19135** |

`Q`-block/`F`-block is **0.3160** at (99,66) — reproducing the submission's `0.316` — and
**0.3470** at D=108. Total unknowns fall to `0.529` / `0.550`; total rows to `0.656` / `0.682`.
So the honest accounting is a **~2x cut in both directions**, exactly as the submission claims,
and *not* more. One further correction: (E2) is a single *polynomial* identity but its coefficient
expansion is the same `C(165,2) = 13530` rows as the `F`-chart's Jacobian block. The saving is in
the unknown block and in trading a 10441-row characteristic block for a 2190-row degree block; it
is **not** "one row replaces the Jacobian band system".

### 2.5 The split-face rows on `(Q,G)` — declared, consumed, not re-derived

Astra's `delta = 2` engine sets `t = 1/x`, `z = t y - 1`, places the `D2` disc at `t = s^3`,
`z = pi*s^4`, and produces `F_face = P^9`, `G_face = P^6`, `K2_face = P^3` with `P = zeta^2(zeta +
3 rho)` for the `[2,1]` minor datum (`P = pi(pi^2 - c)` on the `[1,1,1]`/`delta = 5/2` branch).
The `9:6:5` tower and `h3 ~ P`, `h2 ~ P^3` place `Q` at `P^5`, so the transported row is
`Q_face = lambda * P^5` with the *same* `P`. **I declare this as consumed from
`g9966-corrected-engine-astra-20260905` §"faces are generated", not re-derived here**; Astra's ring map
and generator order are not rebuilt here. The source-support envelope for `Q`
follows from the theorem's `G_i` bounds because `Q = Phi(F,G)` is a polynomial in `(F,G)`; that
transport is likewise stated, not executed.

---

## 3. DECISION

### 3.1 The degree/attainment block `(T)+(I)+localizer`: **PROPER**, with an exact witness

Two facts settle this block without any Grobner computation.

**(a) Bands `nu = 1..19` can never be a unit.** The cone-vertex family `G = P^6`, `Q = lambda P^5`
(`P` of degree 11 with `P_top = P_0`; 66 free coefficients) has `J(Q,G) = 0`, hence satisfies every
band `nu = 1..19`. `controls.py` verifies this on a random rational cone point: all 19 rows vanish.
So the (I)-block minus its last row carries a solution family of dimension `>= 66`.

**(b) Band 20 excludes the cone, and is still satisfiable.** On the cone, band 20 is `0` while the
required target is `-2*P_0^9 != 0`: the cone is **EXCLUDED by the attainment row alone** — the
control the proposal demands, passing. Not vacuously, because an explicit witness of the *whole*
block exists: `Q = -2*P_0^5` (homogeneous, degree 55) and `G = P_0^6 + R` with `R` the unique
homogeneous degree-46 solution of `J(P_0^5,R) = P_0^9`. That system is `100 x 47` of rank `47`
with **zero inconsistent rows** (exact-rational Gauss elimination, `controls.py`; the reason is the
ODE `11 y(y-1) S' + (-484y + 127) S = c y^12 (y-1)^32`, whose homogeneous solution
`y^{127/11}(y-1)^{357/11}` is not polynomial, so the operator is bijective). There bands `1..19`
vanish, band 20 equals `-2*P_0^9` exactly, and `lambda = -2 != 0`, so `Z*lambda - 1` holds.

**Typed outcome: `PROPER` — an existential survivor of the eliminated chart's degree/attainment
block, exact over `Q`.** It is *not* a counterexample and not a survivor of the full chart: there
`J(F,G) = 9c*P_0^13`, so (E2) fails. It establishes that **no kill can come from
`(T)+(I)+attainment` alone** — all the weight sits in (E2) and (S).

A corollary: the band-`nu` obstruction rows are homogeneous in the accumulated band unknowns
(band 2's are 51 homogeneous quadrics in the 55-dimensional `ker L_1`), so they always have the
trivial zero and can never be a unit in isolation. I emitted that system for Singular and then did
**not** run it — it is provably non-decisive.

### 3.2 (E2) has independent teeth — a multiplicity law, proved and controlled

From `(CQ)`, `D_G^2 Qt = mu` a nonzero constant. If `Qt = s^e U` with `s` irreducible,
`D_G(s^e U) = s^{e-1}[e (D_G s) U + s D_G U]` and one more application leaves an explicit factor
`s^{e-2}`. Hence `s^{e-2} | mu`, so **every irreducible factor of `Q` has multiplicity `<= 2`**,
and in particular `Q = c*H^k` with `H` nonconstant is impossible for `k >= 3`. `e2div.sing`
verifies over exact `Q`: the identity `D_G^2(H^k) = k H^{k-2}[(k-1)(D_G H)^2 + H D_G^2 H]` for
`k = 2..6` (residual `0`), the divisibility `s^{e-2} | D_G^2(s^e U)` for `e = 2..5`, a **negative
control** showing `s^{e-1}` does *not* divide (so the law is sharp), and the parallel
`D_G(s^e U) = 1 ==> e <= 1` (`F` squarefree, the classical statement, recovered).

Two consequences. First, the cone-vertex family is excluded a **second** time, by (E2) alone and
with no appeal to attainment or to `d_2 = 33 ∤ D_2 = 55`. Second, the homogeneous-`Q` stratum
`Q = lambda P_0^5` — which is exactly where §3.1's witness lives — is **UNIT**: there
`D_G^2 Q = 5 lambda P_0^3 [P_0 D_G^2 P_0 + 4 (D_G P_0)^2]`, divisible by `P_0^3` of degree 33,
and a nonzero constant is not. So (E2) does kill, on that stratum, immediately.

### 3.3 The full eliminated chart: **compute-bound**, weight reached `omega = 0`

Block (II) has 164 homogeneous rows `omega = 0..163` (Astra's Jacobian-depth scale; their completed
`delta = 2` prefix is `J_0..J_70`). I completed `omega = 0`, which is automatic
(`J(F_99,G_66) = J(P_0^9,P_0^6) = 0`), and derived `omega = 1` in closed form —
`2*J(R_21,P_0) = -3*mu*P_0^3*J(P_0,G_65)`, forcing `P_0^3 | J(R_21,P_0)` — but did not run the
cascade. **Weight reached: (I) complete (`nu = 1..20`), (II) `omega = 0`.** That is far short of
Astra's `omega = 70` and I do not claim otherwise; this lane had one host, and the host's free disk
fell from 2.8 GB to 5 MB during the run.

One structural reason not to expect the eliminated presentation to move that wall by itself. In the
band grading of §2.2 the (II) row at `omega` has weight `20 + omega`, so the Keller localizer sits
at band weight `183 = 163 + 20`, i.e. **20 bands deeper** than the `F`-chart's Jacobian localizer,
the `20` being exactly the degree drop `D_2 + m - 2 - n`. Against that, the attainment question
moves from Astra's `t`-depth-143 leader row to band 20 of a cascade whose band 0 is automatic.
(The two depths are measured in *different* gradings — Astra's `t`-depth for a `Q`-coefficient is
`143 +` my band index, for a `G`-coefficient it is my band index — so this is a restructuring, not
a measured speedup.) The reduction is real and priced in §2.4; it is not a wall-crossing
instrument, which is what the submission itself said.

**Engineering note.** Singular 4.3.2 silently truncates long input lines and mis-tokenises
indexed names split across them (`ideal I = <48 KB on one line>`, `u(\n11)` both give
`skipping text ... error at token ')'`), and the failure is not fail-stop, so `S` is undefined
downstream. Emit plain names (`u11`), break only between terms, keep lines under ~70
characters, and wrap the ring's variable list.

---

## 4. D=108, `delta = 3` (`m_1 = 72/36 = 2`)

The transport is exact and mechanical (`d108.py`). With `P_0 = y^2(y-x)^7` (degree 9),
`F_top = P_0^12`, `G_top = P_0^8`, `D_2 = 63`, `Q_63 = lambda*y^14(y-x)^49 = lambda*P_0^7`
(Astra's (3)), the ratios are `108:72:63 = 12:8:7`; `G_top^3 - F_top^2 = 0` and
`J(Q_top,G_top) = 0` both check. The degree drop is `63 + 72 - 2 - 108 = 25` bands. The obstruction
divisor is again `Q_top/(lambda*y*(y-x)) = y^13(y-x)^48` (degree 61), and `Im L_nu` equals
`D * {degree 72-nu}` **exactly on 23 of the 25 bands** (two resonances, at the multiples of 9).
Obstruction rows are 61 per band (62 at the resonances); kernel dimensions run `63, 62, 61, ...,
39`, totalling 1238 parameters against 1405 rows for `nu <= 24`. Counts are in §2.4.

Both §3.1 facts transport verbatim: the cone family `Q = lambda P^7`, `G = P^8` satisfies bands
`1..24` and fails band 25, and §3.2's multiplicity law excludes it independently (`k = 7 >= 3`).
I did **not** build the `delta = 3` source faces or run a decision at D=108: the (99,66) branch
consumed the budget, and D=108's own `delta = 3` chart is separately charged elsewhere. **D=108
outcome: chart built and counted; not decided.**

---

## 5. FALLACY-v2

- **Why the eliminated chart is necessary (the argument the charge asks for).** Let `(F,G)` be any
  realisation — a Keller pair of degrees `(99,66)` satisfying the `F`-chart's rows — and set
  `Q := Phi(F,G)`. Then `(Q,G,a,b,c,d,e_0,lambda)` is a point of the eliminated chart: (T)/(A) hold
  for `Q` by Theorem A and Prop 4.5 (consumed); (I) holds because `J(Q,G) = -2F + bG + c` has
  degree 99 with top `-2F_99` by (CR) and `deg F > deg G`; (E2) holds by §1.1; (S) holds for `G`
  unchanged and for `Q` by the face transport of §2.5. So the map `(F,G) |-> (Phi(F,G),G,...)`
  sends every realisation into the eliminated chart, and **`UNIT` there is a kill**.
- **Floor/attainment.** The converse fails: §1.4 shows the chart only recovers
  `Q - Phi(F,G) in ker J(-,G)`, so the eliminated chart is a **relaxation**. A `PROPER` on it is
  strictly weaker evidence than a `PROPER` on the `F`-chart, and §3.1's witness is typed as a
  survivor **of the degree/attainment block only** — not of any branch, not of the `F`-chart.
- **Variable/ring map.** §2.5 declares that Astra's `delta = 2` face data is consumed, not
  reconstructed; no row of this lane depends on matching a variable name across engines. The
  band grading, the dehomogenisation `x = 1`, and the Euler form of `J` are all declared in §2.2
  and checked against `J(P_0^5,P_0^6) = 0`.
- **Prime label/derivative.** `'` in §2.2/§3.1 is `d/dy` on the dehomogenised form, defined there;
  `J^{(k)}` is iterated `J(-,G)`, defined at (ITJ). Neither is a label.
- **Raw remainder degree.** §2.3's obstruction rows are the remainder of `C_nu` on division by the
  explicit `D`, in the declared univariate ring, with quotient degree `66 - nu` fixed by the band
  row's homogeneous degree `119 - nu`; my first pass was off by one there and is corrected.
- **`sat()` wrapping.** Not used; no localisation was wrapped or unwrapped in this lane.
- No exit-price assertion is made here, so no `charge_basis` line is due: this lane consumes no
  exit price and asserts none.

---

## OPENS RAISED

```text
OPEN[CQ-ELIM-BICONDITIONAL-DIRECTION]
  QUANTITY: for a pair with Q = Phi(F,G), J(J(Q,G),G) = -2 j^2 + Phi_u(F,G)*J(j,G) with
    j = J(F,G), so J(J(Q,G),G) = -2 does NOT imply j = 1; the exact chart identity is
    J(F_def,G) = -(1/2)*J(J(Q,G),G) with F_def := (b G + c - J(Q,G))/2.
  STATUS: PROVED-HERE, with an explicit counterexample (F,G) = (-x, y+x^2) at j = -1 and a
    four-trial symbolic check of the chart identity.  Corrects OPEN[CQ-ELIM-EQUIVALENCE];
    kills 0 rows.
  CHEAPEST TEST: recompute J(J(Q,G),G) on any pair with J(F,G) = -1, ~1 min; agreement with
    -2 confirms the correction.
  BLAST RADIUS: every m_1 = 2 receiver chart must define F by (E1) rather than adjoin (E2)
    to a free F-block; otherwise the chart admits the j = -1 sheet.

OPEN[CQ-ELIM-ITERATED-SCOPE]
  QUANTITY: for every m_1 >= 2, J^{(k)}(Q,G) = (d^k Phi/du^k)(F,G) when J(F,G) = 1, hence
    F = [(m_1-1)! C(G) - J^{(m_1-1)}(Q,G)]/m_1! and Keller <=> J^{(m_1)}(Q,G) = -m_1!;
    scope is 66/66 roster rows, not 44/66 (m_1 distribution {2:44,3:14,4:5,5:2,7:1}).
  STATUS: PROVED-HERE from the Prop 3.1 weight inequality (which forces i <= m_1 - 1) and
    verified symbolically at m_1 = 2,3,4; not built as a chart, so 0 rows killed.
  CHEAPEST TEST: run the m_1 = 3 display on a tame pair (x, y+x^3), ~2 min; a nonzero
    F-recovery residual refutes it.
  BLAST RADIUS: extends CQ-ELIM to the 22 rows with m_1 >= 3, including both m_1 = 3 rows
    that carry a Xu margin.

OPEN[CQ-BAND-OBSTRUCTION-DIVISOR]
  QUANTITY: at (99,66) the degree-drop band operator has Im L_nu = D * {forms of degree
    66-nu} with D = Q_top/(lambda*y*(y-x)) = y^14 (y-x)^39, exactly on 19 of 20 bands
    (nu = 11 is one row smaller); at D=108, D = y^13 (y-x)^48, exact on 23 of 25 bands.
  STATUS: computed exactly over Q by rank comparison on every band; PROVED-HERE only as a
    computation, with no printed source; it kills 0 rows by itself.
  CHEAPEST TEST: recompute rank(L_nu) versus dim(D * {degree 66-nu}) at nu = 1 and nu = 11,
    ~3 min; inequality at any nu other than the resonances refutes the statement.
  BLAST RADIUS: replaces 53 (resp. 61) coefficient rows per band by one divisibility
    statement at the two points at infinity, on every m_1 = 2 receiver.

OPEN[CQ-MULTIPLICITY-LAW]
  QUANTITY: J(J(Q,G),G) = -2 forces every irreducible factor of Q to have multiplicity <= 2,
    hence Q != c*H^k for k >= 3 with H nonconstant; and the homogeneous stratum Q = lambda
    P_0^5 is empty because D_G^2 Q is divisible by P_0^3 while -2 is not.
  STATUS: PROVED-HERE by the derivation identity, verified over exact Q with positive and
    negative controls; it excludes the cone-vertex family independently of attainment but is
    an open condition elsewhere, so it kills 0 further rows.
  CHEAPEST TEST: divide D_G^2(s^e U) by s^{e-2} and by s^{e-1} at e = 3, ~1 min; divisibility
    by s^{e-1} would refute sharpness.
  BLAST RADIUS: supplies a second, attainment-free exclusion of Delta on every m_1 = 2 row,
    and the analogous k >= 3 exclusion at D=108 (k = 7).
```

## OPENS RETAINED

- `OPEN[AUGMENTED-CHART-WEIGHT-VACUITY]`, `OPEN[NPR-INFINITY-DICHOTOMY]`,
  `OPEN[PROP45-LICENCE-NOT-DESCENT-INVARIANT]` — not consumed here.

## References consumed

- `ideation-20260906T0000Z-opus5.md` §2.1 (CQ-ELIM) and its `OPEN[CQ-ELIM-EQUIVALENCE]`.
- `char-degree-instrument-astra-r2-20260905.md` §§3–5: Theorem A, `D_2 = 55/63`, display (3)
  `Q_55 = lambda y^15(y-x)^40`, `Q_63 = lambda y^14(y-x)^49`, depths `143/153/163`, the 13530
  Jacobian coefficients, and the `Delta` exclusion `33 ∤ 55`.
- `g9966-corrected-engine-astra-20260905.md`: `P_0 = y^3(y-x)^8`, `F_top/G_top/h2_top/h3_top`,
  `t = 1/x`, `z = ty-1`, the `delta = 2` `D2` cover `t = s^3, z = pi s^4`, and the `[2,1]`/`[1,1,1]`
  minor faces `P = zeta^2(zeta+3rho)` / `P = pi(pi^2-c)`.
- `source-support-closeout-opus5-20260905.md` §4 (source-support theorem, `G_i` bounds and the
  "necessary over-approximation" reading used in §2.5 and §5).
- `box/residual66-20260905/roster.jsonl` — `m_1` recount over all 66 rows.
- `FALLACY-v2.md` (floor/attainment, variable/ring map, prime label, raw remainder degree).
- Moh, *J. Reine Angew. Math.* **340** (1983): Prop 3.1 p.157 (target family, weight
  inequality), Prop 2.2 p.152, Prop 4.5 p.169 — consumed through the two Astra reports above; no
  page image was re-read in this lane.
- Drivers and JSON: `box/cq-elim-20260906/` (16 files, manifest `evidence.json`).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `24924`.
- Body SHA-256:
  `aef9102a2ae18870ec2903655eda5d3b10086b01ae8ac6a3d897bce4ac9ea7c0`.
- Frozen basis: `7fd467742d128a87375d614b1044247eac74e10d`.
