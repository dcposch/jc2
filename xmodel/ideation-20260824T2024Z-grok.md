# Blind whole-portfolio ideation — Grok 4.6 — `20260824T2024Z`

Status: **FROZEN BLIND SUBMISSION**. Independent of every other
`xmodel/ideation-20260824T2024Z-*.md` file. No shared ledger, packet, code,
or artifact was edited except this report. No work is launched. No AWS.
No claim is promoted.

- Lane: xAI/Grok ideator
- Packet: `xmodel/ideation-20260824T2024Z-packet.md`
- Packet cutoff: `2026-08-24T20:24:00Z`
- Clean charged basis named by the packet: `2e6104a417cfe15a93a901aa0a9129094a2ae11b`
- Git HEAD at first hash check: `2e6104a417cfe15a93a901aa0a9129094a2ae11b`
- Newest `LIVE STATE` consumed: `2026-08-24 19:32Z` (canonical files lag the
  packet delta, as the packet warns)
- No post-cutoff synthesis was imported. No other `2024Z` submission was opened.

Evidence labels:

- **THEOREM** — different-model confirmed / packet-promoted statement
- **EXACT** — identity or finite calculation checked here or in a frozen
  producer, not a campaign promotion
- **PROVISIONAL** — exact producer/interim calculation, unreviewed
- **PACKET-CLAIM** — coordinator formula in the sealed packet
- **SPECULATION** — testable guess, not a fact

---

## 0. Hash verification and source access

Every packet-listed SHA-256 was recomputed on disk before ranking. All six
canonical files matched. The three named review/erratum hashes were located
as file contents and matched. Packet-named mathematical reports actually
read also matched their on-disk SHA-256.

| Input | Packet SHA-256 | Result |
|---|---|---|
| `APPROACHES.md` | `a069522025da7bef75cf0112dce8857b643f84ae7106cbd6756e959ee5afc965` | match |
| `AUDIT.md` | `b2b29c6bb666d5bc50616921db858e3daefa75d54d48471f6b71e7e187928c92` | match |
| `PROGRESS.md` | `9c29aae163268097978596ec448e6bac429044d81fa92bff3374e3852588bfc7` | match |
| `notes.md` | `813ccd6a15b8f00333b8ba66a4febff25d542660d86af723cad96124380d558d` | match |
| `COORDINATION.md` | `2bed8117d2137bd9f93d558d7b9aca98a02a21c5b42688fc181e99d683f537cd` | match |
| `ladder/REDUCTION.md` | `f0fca49811349483c437d674ab819065eb09500330516d161978868c71bf6371` | match |
| full-absorption review | `6d34908cbd2ead9769e4090fcab903ec5d5b7bd9db485db1d681708c5d36946e` | match (`xmodel/max12-912-order3-nu-belyi-collision-boundary-review-grok-20260824.md`) |
| AS D10 review | `8ccaa15fd9180660d5ab7e2957737c028a96bb5b28508378e0a3ca93964089b5` | match (`xmodel/as-fonly-d7-degree10-pointwise-review-grok-20260824.md`) |
| AS D9/D8 erratum | `26dd0908295bfbcc36ad2f0efe59b645ce1dd11411fd88ab8e37337a74fc0d7d` | match (`xmodel/as-fonly-d7-postd10-d98-f3-erratum-20260824.md`) |

Packet file actually consumed:

```text
6de4b6efe154807707a4e8393db5b1cf1b0fe20c34c66eb3a87e9181f70cf1df  xmodel/ideation-20260824T2024Z-packet.md
```

Additional files actually consumed, with on-disk SHA-256 (not `2024Z`
submissions):

```text
9b717712e59b70a6b06303f745a9c70b2152e3f624d03162741e3338ef1168b7  xmodel/max12-912-order3-nu-belyi-collision-boundary-20260824.md
f37376c96ab7e3c6ed7aa554dd04e2c72c9b2f5092ba6df03f524ea44765515d  xmodel/max12-912-order3-nu-parity-genus5-exclusion-20260824.md
dbf60b008f968033b7e91a5c5975bbedffc0529009aa53db6fb4b139bd844cb9  xmodel/td6-c1-line-kill-gate-20260824.md
8de47ff8f9639310c96d6a60f1d5ca5731ab42a963972a6a8325ffdf18eeaf10  xmodel/ideation-20260824T1820Z-synthesis.md
a6f1e651b57b07a859b8168da8f721c1c21e9721b9727fcabae7535ac2b4897e  xmodel/ideation-20260824T1820Z-grok.md
230752452cd88982ce9d9c10a2d06ae33e556b064f8b12b6247fd4ae3c9682b6  xmodel/ideation-20260824T1633Z-grok.md
```

The `1820Z` synthesis and prior Grok reports were read because
`APPROACHES.md` names the former as the last completed all-avenue record,
and because the history/priority checksum forbids relabelling those cards
as new. They are not `2024Z` submissions. Every other `ideation-20260824T2024Z-*.md`
file except the packet was left unread.

Independent checks performed on packet/producer formulae (not a promotion):

- `A5=33v^5+117v^4+131v^3+69v^2+18v+2` and `D=3v^2-2` are coprime over `Q`;
  `Res(A5,D)=97200`; `A5` and `D` are squarefree. Cube-factor accounting
  `v^6 (3v^2+3v+1)^3 / (3v^2-2)^4` yields `Y^3=A5/D`. Riemann–Hurwitz for a
  degree-3 cover ramified at seven finite points and unramified at infinity
  is `2g-2=8`, `g=5`. **EXACT**.
- Packet `wt(x5)=1` is the order-three character of the producer weight
  `wt(x5)=4`; both make `v=A/(p x5)` invariant. **EXACT** as conventions,
  not a disagreement.
- Reviewed `B=54 nu z^2+18 nu p+60 r8` has no linear term, so it is even,
  and `disc(B)=-1296 nu(3 nu p+10 r8)`. **EXACT** (re-derived from the
  reviewed quadratic). Hence `disc(B)=0` if and only if the weight-zero
  ratio `tau=r8/p` equals the constant `-3 nu/10`. **EXACT**.
- The genus-five rationalization `(3.2)--(3.6)` and the TD6 line-union
  theorem were not re-derived. They remain **PROVISIONAL**.

No proof or counterexample to JC2 exists at cutoff.

---

## 1. Disposition vector, avenues 1–46

Legend: `U` unchanged, `R` raise, `L` lower, `O` reopen. Overlay scores in
`APPROACHES.md` are historical (reviewed through `19:32Z`). This vector is a
post-delta ranking vote against that overlay, not a promotion. Reasons are
required for every non-`U` entry.

| ID | Call | Reason if not `U` |
|--:|:---:|---|
| 1 | U | Pinchuk 2021 is already banked as local identities. Full-absorption and the `c1` line do not empty a GGV corner or repair `G2-PSC`. |
| 2 | R | **PROVISIONAL:** the licensed normalized `c1` line is empty by an exact four-stratum cover, all reducing to the unit `-k/50`. First honest neighborhood/family client on sheet six since the q2 pencil. Not SP-2, not a class kill, not uniform in other moduli. |
| 3 | R | **THEOREM:** full-absorption passports `(18,2,2,1^{14})` and `(18,3,1^{15})` empty on the reviewed `(9,12)` order-three `k=mu=0, nu!=0` landing, without a unitree list. **PROVISIONAL:** parity slice empty by a genus-five cube descent. Live object is the leftover even-`B` stratification (Card A), not another fibre Groebner. |
| 4 | U | D-series remains a local maximum: no typed full source, no algebraization, no AWS. Empty AS structural bases are not a D-germ licence. |
| 5 | U | Amalgam rigidity still does not bite on non-automorphisms. Pinchuk 3.4 stays a source gap, not a JvdK engine. |
| 6 | U | Abhyankar–Moh remains the wrong object on residue-A fibres. |
| 7 | U | Polar-versus-`A_infinity` remains `TYPE-FAIL` as identification. |
| 8 | U | Formal-inverse combinatorics still lack a truncation bound. |
| 9 | U | Conjecture E remains an unbounded implication ladder. |
| 10 | U | HC4 quintic module remains `NO LEVERAGE`. |
| 11 | U | Zhao/Mathieu ladder remains dead. Cube descent is RH/Lüroth, not a moment tower. |
| 12 | U | No integer to send to infinity. |
| 13 | U | DC(2) still strictly stronger than JC2. |
| 14 | U | No candidate non-surjective `A_1` endomorphism. |
| 15 | U | Burchnall–Chaundy dictionary still incomplete. |
| 16 | U | No Keller-specific holonomic index is named. |
| 17 | U | Cubic-linear class in high dimension still contains genuine CEs. |
| 18 | U | Graded plane Keller maps remain automorphisms. |
| 19 | R | **THEOREM:** D10 pointwise gate. **PACKET-CLAIM / ERRATUM:** first post-D10 D9/D8 census retracted (`[K_Frob/3] mod 3` omitted); `50939` and `954` counts are not mathematics. Compiler honesty goes up; licensed emptiness does not. Live object is the corrected inhomogeneous column plus Fitting-forced digits (Card C), not the retracted census. |
| 20 | U | Tsuchimoto/p-curvature still consumes false PC(2)/JC(4). |
| 21 | R | Same map-only Hensel client as 19. D10 is now a theorem; D8 is the first potentially decisive vertical row, but only after the polarization column is rebuilt. D12 remains deferred until that predecessor exists. |
| 22 | U | Siegel still points the wrong way. Genus five used Lüroth/RH, as at the `(6,9)` genus-one fibre. |
| 23 | U | Holomorphic analogue remains false. |
| 24 | U | Real Pinchuk maps still have nonconstant `J`. The 2021 paper is a different object. |
| 25 | R | Three-point spectral passports now kill, **THEOREM**, on a Jacobian-coupled eliminant. Residue-A passport sufficiency remains too generous; this raise is the coupled `W`/`B` client, not a revival of the 169-tuple screen. Four-point leftovers are not a finite list (**SPECULATION** to treat them as one is `SCOPE-CONFLICT`). |
| 26 | U | Primitive-group `td` bound still has no proved support bound. Full-absorption used fixed-passport Hurwitz finiteness in `S_36`, not an `A_n`/`S_n` ceiling. |
| 27 | U | Admissible splice diagrams still outrun algebraic realizability. |
| 28 | U | Dual-pencil defect remains `JUMP-ONLY / TYPE-FAIL`. |
| 29 | U | Ordinary `kappa(P)` still has no universal receiver. |
| 30 | U | ML invariant still does not see the embedding. The 2022/2025/2024/2026 audits remain conditional Newton-frame restrictions with no typed bridge. |
| 31 | U | Integrality remains the missing global assertion. |
| 32 | R | The emptied `c1` line is a row-module/Fitting certificate, not a three-generator unit ideal. The bivariate first-stage denominator (Card B) is the cheapest neighborhood successor. No projective-connectedness revival. |
| 33 | U | Ordinary action residues remain exact-form `COSTUME`. |
| 34 | U | No spare coordinate to absorb a 2D pole. Pinchuk rational powers remain the same recovery gap as AS growing support. |
| 35 | U | Dim-3 mechanisms remain structurally 3-dimensional. |
| 36 | U | Generic sparse/SAT remains a dead category. Named F-only at a *named* degree is avenue 19/21. |
| 37 | U | Finite-field extras will not lift. Literal-`F_3` survivors are Witt digits, not a census. |
| 38 | U | No new tropical invariant. The even Wronskian is a polynomial identity, not a tropical rename. |
| 39 | U | No 10-line class attached to `J=1`. |
| 40 | U | Commutative `det=1` still does not give free invertibility. |
| 41 | U | Naive scaling remains falsified by the dim-3 CE. |
| 42 | U | Arrow still points the wrong way. |
| 43 | U | Ritt still collapses to GGV after Aut-reduction. |
| 44 | U | Moskowicz remains `REFUTED-AS-PROOF`. |
| 45 | U | Inverse PDE remains tautological. Genus-five and the terminal ODE `9 h rho'+6 h' rho=j` are coefficient trajectories, not Kovacic analysis of the inverse. |
| 46 | U | Formalization cannot manufacture the finite universe. |

Unchanged majority:
`1,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,22,23,24,26,27,28,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46`.

No avenue is reopened. No avenue is lowered relative to the `19:32Z` overlay:
the Pinchuk-Newton raise of `1820Z` had already been absorbed there as a
local identity, and the retracted AS census is a correction inside 19, not a
demotion of the F-only engine.

---

## 2. Reranked principal bottlenecks

### Proof

1. **Fail-closed split of the remaining `(9,12)` order-three `nu!=0` fibre,
   after full-absorption, by the even Wronskian rather than primary
   decomposition.**
   **THEOREM:** max-11; DZ20 undeformed coprime `k=mu=nu=0`; full-absorption
   of `B` by `W` empty on `k=mu=0, nu!=0`; automatic coprimality/squarefreeness
   on actual trajectories.
   **PROVISIONAL:** parity `q=x0=x2=x4=k=0` empty by genus five.
   **EXACT (this scan):** `B` is even; `disc(B)=0` iff `tau=r8/p=-3 nu/10`.
   Leftover strata are no-collision, one-collision, double-`B` off `W`, and
   equal non-`1` critical values. Four-point Hurwitz is positive-dimensional
   and is **not** the discriminator. Taylor boundaries stay charged.
   `(8,12)`, the order-one core, and nonzero `mu`/`k` remain separate cells.
2. **TD6 global realizability / opposite-side balance, now with a complete
   licensed `c1` line as a neighborhood seed.**
   Eight terminal classes remain. **THEOREM:** licensed q2 pencil empty;
   common-centering tangent rank 3 / kernel 0 at a nonsolution.
   **PROVISIONAL:** entire normalized `(C,1,1)` line empty.
   Sensitivity on a line is not a neighborhood. The missing object is an
   explicit first-stage denominator in at least one extra center coordinate
   whose vanishing locus is a finite raw-rebuild cover (Card B). SP-2,
   `G2-PSC`, and `G2-BD` remain.
3. **`G2-PSC` and complete landing/coverage.** Unchanged missing theorems.
   Neither full-absorption nor a `c1` line transports a GGV packet into a
   Sigray tree. KJN remains type-relative. First open sheet degree is still
   six. Max-11 and max-12 work are unbounded in `x`, not a `td` theorem.

### Disproof

1. **A polynomial point of actual degree `>=12` in the completed AS orbit,
   reached by a source-honest next-carry recursion that retains nonreduced
   structure.**
   **THEOREM:** every fixed simultaneous map/gauge cap dies at finite depth;
   D7 pointwise terminal residue; cyclotomic odd-degree finite-precision
   false positives; D10 vertical component plus two reduced endpoint
   supports.
   **ERRATUM:** post-D10 D9/D8 censuses retracted. Provisional replacement
   counts `314127/1594323` and `918/354294`, and the “twelve / 360 empty
   structural bases”, are **PACKET-CLAIM**, not licensed.
   First honest gate is the corrected D8 inhomogeneous column
   (old column plus `[K_Frob/3] mod 3`) on nonreduced `H`. D12 remains
   deferred until that predecessor is proof-carrying. Max-11 makes D7–D11
   characteristic-zero SAT a compiler bug.
2. **`A_infinity=0` and rational deck descent.** Unchanged reserve theorems.
   Not the current discriminator.
3. **An explicit leftover `(9,12)` pair that survives Taylor boundaries
   after even-`B` descent.** A surviving normalized orbit is a near-CE,
   not something to hide. Finite check, not a sparse search.

No result at this cutoff proves or disproves JC2.

---

## 3. Campaign-wide questions

### Q1. Genus-five from parity to leftover loaded strata

Do not copy `v=A/(p x5)` off the parity slice. That coordinate uses
`r2=r4=0` after odd-vanishing, which is exactly the specialization just
provisionally killed.

The invariant that exists on the whole reviewed `k=mu=0, nu!=0` landing is
the weight-zero Wronskian ratio

```text
tau = r8 / p,
delta = (3 nu p + 10 r8) / (nu p) = 3 + 10 tau / nu.
```

Both `p` and `r8` have Kummer weight 2, so `tau in C(x)` after writing
`p=u^2 pi`, `r8=u^2 rho`. **EXACT:** `delta=0` iff `B` has a double root
iff `tau=-3 nu/10`. The two critical points of `beta` are opposite,
`sigma,-sigma` with `sigma^2` a linear form in `(p,r8)`, because reviewed
`B` has no `z`-term.

Parity's `v` *determines* `tau` on that slice (`r6=p^9 R6(v)`,
`r8=p^{10} R8(v)` ⇒ `tau=nu R8(v)/R6(v)`), which is why genus five could
kill it. The recast through the quadratic Wronskian is: impose that the
symmetric value `Pi=W(sigma)W(-sigma)` is a cube in `C(x)` after removing
explicit Kummer cubes, and test the genus of the resulting superelliptic
curve in `tau`. **SPECULATION:** that curve has genus `>=2` on the generic
no-collision stratum. If it does, nonconstant `tau` is impossible and the
constant-`tau` ODE is the whole leftover. If genus `<=1`, character descent
does not finish and one-collision/equal-value must be treated separately.

Cheapest discriminator: Card A, not a coefficient primary decomposition.

### Q2. Smallest exhaustive split of `nu!=0` order three, Taylor kept

After full-absorption (**THEOREM**) and parity (**PROVISIONAL**), do not
primary-decompose. Ordered split that preserves both Taylor families:

| Leaf | Invariant | Instrument |
|---|---|---|
| `disc(B)=0`, `W(0)!=0` | `tau=-3 nu/10` constant | double-`B` off `W`; four-point with index 3 over a fourth value; terminal ODE on `rho` |
| one simple `B` root in `W` | `Pi=0` but not both | leftover RH unit 1; four-point `(18,2,1^{16})` plus one extra value |
| no `B` root in `W`, `beta(sigma)!=beta(-sigma)` | `Pi!=0`, anharmonic `!=1` | generic two extra values; superelliptic in `tau` |
| no `B` root in `W`, `beta(sigma)=beta(-sigma)!=1` | equal non-`1` values | still four-point `{0,1,c,infty}`; labels prevent folding `c` onto `1` |
| order-one core / `delta` unforced | polynomial `h=q^3` | separate, as in max-11 |
| original Taylor boundaries | charged on every branch | never drop |
| `(8,12)`, nonzero `k` or `mu` | other cells | do not steal the `(9,12)` worker |

Four-point Hurwitz geometry classifies the leftover *type* and shows it is
not a finite list. It does not empty a leaf. Equal-critical-value is not
three-point: `{0,1,c,infty}` remains four labelled values. Kummer character
descent on `tau` is the instrument that can avoid primary decomposition.
**SPECULATION** that every leftover leaf reduces to constant `tau` plus the
already-used ODE `9 h rho'+6 h' rho=j`. That ODE is **EXACT** on the whole
loaded landing (same as DZ20, now with `rho` coupled to `p` through `B`).

### Q3. From an empty `c1` line to a neighborhood

Do **not** argue that the confirmed centering differential `E^3 -> E^{10}`
of rank 3 empties a neighborhood. A nowhere-zero obstruction on a line can
still vanish nearby.

If hostile review confirms the line, the cheapest complete cover is the
same architecture that completed the line. On `(c1,c3)` — already the
cheaper dual by 6,763 typed entries — attempt the first-stage identity
with `c3` a second indeterminate:

```text
D(c1,c3) P12 = D(c1,c3) (-k/50) + sum M_i L_i
```

**SPECULATION:** such a polynomial `D` exists, because the one-parameter
`D(C)=(C-3)^2 J(C)/4` was a lift through 28 original first rows with
multipliers polynomial in `C`. Completeness, if `D` exists: every point of
the plane is either `D!=0` (generic identity, obstruction the unit
`-k/50`) or `D=0` (a plane curve, finitely many irreducible components,
each a raw 3,602-column rebuild exactly as `C=0,3` and `J=0` were). The
cover is the vanishing locus of an explicit polynomial, hence exhaustive
for that plane. It is not SP-2, not a three-center block, and not a
boundary/dead-stretch/F1/pole deformation.

If no polynomial `D(c1,c3)` exists, Card B stops. A first-order adjoint
along `c3` is a sensitivity gate, not a family obstruction.

### Q4. Literal-`F3` survivors and empty structural bases

The retracted census is not a next-carry recursion. The D10 review already
named the honest successor: attach remaining rows to the vertical and `g`
endpoints on original nonreduced `H`. The erratum supplies the missing
term: the D8 inhomogeneous column is the old column plus the first
polarization of `K` along the six Frobenius directions,

```text
K_Frob/3 = (UF_x/3) V0_y + (U0_x-x^2)(VF_y/3)
         - (UF_y/3) V0_x - U0_y (VF_x/3).
```

**EXACT** as the integer witnesses `2x^7+2x^8` and `2 x y^6+2 x^4 y^5`.
Empty structural bases, if they survive the corrected column, are Fitting
minors that force digits, not a field-point count. Those forced digits are
the first letter of a vertical automaton: cycle at bounded support is an
algebraization candidate; linear growth is the known restricted-analytic
control; a unit Cartier row kills the branch. Reduced-only calculation of
`sqrt(H)` remains `TYPE-FAIL` for this recursion (`I_4(A)=0` modulo
`sqrt(H)` and not modulo `H`).

### Q5. What is actually new

See §4. Close synonyms that are **not** new: `1820Z` spectral `W` / three-point
DZ/Belyi; `1633Z` Stothers/Zannier watch; parity genus-five as written;
`(c1,c3)` atlas as a cheaper dual; affine one-shot Smith (`1820Z`
`SCOPE-CONFLICT`); D12-direct-carry (deferred, no predecessor);
Cartier-first D7 recursion; D10 pointwise gate; divided-carry erratum.

---

## 4. New mechanism and new cross-avenue connection

### New mechanism — even-`B` opposite-root character descent

**KNOWN:** spectral eliminant `W`; three-point full-absorption; DZ20
undeformed face; genus-five on the parity coefficient `v`.

**NEW as an engine.** Reviewed `B` is an even quadratic. Its critical points
are opposite. The single weight-zero coordinate on the whole `nu!=0`
landing is `tau=r8/p`, and double-`B` is the constant value `-3 nu/10`.
Leftover ramification is therefore a problem in one rational function of
`x`, not a coefficient primary decomposition. Cube-norm of the symmetric
Wronskian values `W(sigma)W(-sigma)` is the direct generalization of
“`R(v)` is a cube”. This is not a four-point Hurwitz census, not a unitree
list, and not a claim that parity genus five already kills the fibre.

### New cross-avenue connection — denominator-complete covers

The TD6 identity `D(C) P12 = D(C)(-k/50)+sum M_i L_i` and the max-12 split
“three-point full-absorption versus four-point leftover” are the same
fail-closed architecture:

- generic / `D!=0` / three-point: obstruction is a parameter-free unit
  (`-k/50`, or `lambda` forced constant);
- exceptional / `D=0` / leftover ramification: finitely many strata, each
  a raw rebuild or a character descent.

Avenues 2, 3, 25, and 32 therefore share one proof engine: write the
explicit denominator (or ramification leftover), cover its vanishing, and
refuse to treat the generic identity as a family theorem. The AS analogue
is the inhomogeneous column: Fitting rank kills the generic digit, and the
polarization `[K_Frob/3]` is the exceptional correction that makes the
column source-honest. That is the cross-link to 19/21, not a slogan that
“all three roots are constants”.

---

## 5. Strongest proof attack and strongest falsification

### Strongest proof attack

Run Card A on the leftover `(9,12)` order-three `nu!=0` strata, consuming
full-absorption as a theorem and parity as a provisional negative control.
Do not wait for a global Groebner basis of the loaded fibre. Do not treat
four-point Hurwitz as a finite list.

Load-bearing frozen facts: max-11, DZ20, full-absorption, coprimality
firewall, even quadratic `B` (**THEOREM** / **EXACT**). Parity genus five,
the `c1` line, and post-D10 counts are **PROVISIONAL** / **PACKET-CLAIM**.

A confirmed empty leftover still does not close maximum 12: Taylor,
order-one, `(8,12)`, and nonzero `k`/`mu` remain. It does replace the
loaded fibre's positive-dimensional collision geometry by one rational
coordinate plus an ODE already used at DZ20.

Do not steal the in-flight fibre compiler; point it at Taylor and the
order-one core after Card A.

### Strongest counterexample / falsification attack

Two honest shots, in order of cheapness.

1. **A leftover even-`B` pair** with nonconstant `tau` whose superelliptic
   curve has genus `<=1`, or a constant-`tau` solution of
   `9 h rho'+6 h' rho=j` that reconstructs through original Taylor
   boundaries and `J=1`. Finite check. Failure of boundaries is a control,
   not a CE.
2. **A source-honest D8 SAT on the vertical or `g` branch** after adding
   `[K_Frob/3]` to the inhomogeneous column, independently expanded over
   `Z`, retaining nonreduced `H`. A SAT that uses the retracted census or
   `sqrt(H)` is not a candidate. Characteristic-zero SAT at D7–D11 remains
   a compiler bug (**THEOREM** max-11). Bounded-support all-depth cycle at
   D7 is the first genuine algebraization candidate; linear growth is the
   known restricted-analytic control.

`p=109` brute force, generic exponent rectangles, AWS, and treating the
retracted `50939`/`954` counts as evidence remain unlicensed.

---

## 6. Software accelerator / decisive experiment

**Even-`B` symmetric-value compiler, then the corrected D8 polarization
column as the same backend's nonreduced inhomogeneous test.**

Input: the reviewed Faber form on `k=mu=0, nu!=0`, and the frozen D10
nonreduced `H` together with the erratum witnesses.

Output, in this order, stdlib / Singular, no AWS, box01's
`build_tails43.py` core untouched:

1. From `B=54 nu z^2+18 nu p+60 r8`, form `sigma^2=-(p/3+10 r8/(9 nu))`
   and the elementary symmetric polynomial `Pi=W(sigma)W(-sigma)` by
   remaindering `W` modulo `B` (resultant in one variable). Print `Pi` as
   a polynomial in `(p,r8)`. Replay `disc(B)=0 iff tau=-3 nu/10` on a
   generic sample and on the double-root sample `B=54 nu z^2`.
2. Substitute `p=u^2 pi`, `r8=u^2 rho`, remove explicit cubes, and emit
   the cube-free curve `Y^3=F(tau)` (or a square-times-cube variant if
   that is what appears). Compute genus by Riemann–Hurwitz from the
   ramification of that model, with gcd/resultant as in the parity replay.
3. Separately, rebuild the D8 inhomogeneous column as old column plus
   formula (4) of the erratum, on all six Frobenius directions including
   `u6_0,v6_6`. Replay witnesses (5) and (6). Then recompute Fitting minors
   of the corrected matrix over nonreduced `H`.

Fail-closed: if `Pi` is not a polynomial in `(p,r8)`, or if `disc=0` does
not force constant `tau`, Card A stops. If the polarization column misses
`2x^7+2x^8` on the vertical witness, Card C stops. This is the cheapest
conversion of Q1–Q4 into checkable objects.

---

## 7. Idea cards (three)

### Card A — `EVEN-B-TAU-DESCENT`

**Mechanism.** Replace primary decomposition of the leftover `nu!=0`
order-three fibre by the weight-zero Wronskian coordinate `tau=r8/p`,
using that reviewed `B` is even. Split on `delta=0` (constant `tau`) versus
cube-norm of `W(sigma)W(-sigma)` (superelliptic curve in `tau`). Push
constant `tau` through the already-used ODE `9 h rho'+6 h' rho=j`. Keep
Taylor boundaries on every branch.

**Dependencies.** **THEOREM:** max-11; DZ20; full-absorption; coprimality
and squarefreeness; Faber landing `9 r8'=j/u`; quadratic `B`. **EXACT (this
scan):** evenness, `disc=0 iff tau=-3 nu/10`. **PROVISIONAL:** parity
genus five, used only as a negative control (`v` specializes `tau`). Does
not depend on TD6, AS D10, or Pinchuk 3.4. Does not consume `G2-PSC`.

**History/priority checksum.** `KNOWN:` spectral `W`; three-point
full-absorption; DZ20 ODE; parity `v` and genus five. `NEW:` `tau=r8/p` as
the fibre-wide invariant; opposite-root product as the cube observer;
`disc=0` as a constant-`tau` leaf. `DUPLICATE` if advertised as “run genus
five on the whole fibre” with coordinate `v`, or as a four-point Hurwitz
census. `SCOPE-CONFLICT:` not a maximum-12 theorem, not JC2, not a `k!=0`
or `(8,12)` theorem, not passport sufficiency, not a unitree list.

**Cheapest discriminator.** Resultant of `W` modulo `B` as in §6.1–6.2.
No AWS. Do not interrupt the in-flight fibre compiler.

**Interpretation of every outcome.**

- `Pi` is not a polynomial in `(p,r8)`, or `B` acquires a linear term on
  this leaf: reviewed quadratic is being mis-used. Stop. Return to the
  fibre compiler. Information gain still positive.
- Superelliptic model has genus `>=2`: nonconstant `tau` impossible.
  Leftover reduces to constant `tau` plus the ODE. Then: ODE forces `r8`
  constant, or produces a pair that fails Taylor, or produces a pair that
  survives Taylor — last case is a max-12 lead, not a CE until gauges,
  actual degrees, and `J=1` pass.
- Genus `1`: a possible elliptic parameter. Do not claim Lüroth. Treat as
  a genuine one-parameter leftover; only then consider one-collision and
  equal-value as elliptic pencils. Do not primary-decompose first.
- Genus `0`: character descent fails to bound. One-collision and
  equal-value become separate four-point problems. Fibre compiler remains
  necessary on those leaves.
- Using selected-root full-cubic reduction, or folding equal-value onto
  full-absorption by a target Möbius: `TYPE-FAIL`, discard.

**Stop condition.** Any sentence “hence JC2” or “hence maximum 12 empty”;
importing unreviewed parity identities as fibre theorems; treating
four-point Hurwitz numbers as a classification; interrupting Taylor /
order-one work.

**Expected information gain.** Either the loaded leftover becomes one
rational coordinate plus an ODE already in the bank, or the Wronskian
recast is refuted in an afternoon. Both beat a raw global Groebner basis.

### Card B — `TD6-BIVARIATE-DENOMINATOR`

**Mechanism.** If review confirms the licensed `c1` line empty, attempt the
same first-stage lift with `c3` free, producing a polynomial denominator
`D(c1,c3)` whose vanishing is a finite raw-rebuild cover of the
`(c1,c3)` plane. Completeness is the vanishing locus of `D`, not a tangent
rank and not a 110-by-132 affine certificate.

**Dependencies.** **THEOREM:** q2 pencil empty; centering differential rank
3 / kernel 0 (sensitivity only). **PROVISIONAL:** line-union theorem at
`C=0,3`, generic `D(C)!=0`, and `J=0`. Invalid affine Smith system stays
stopped. Does not depend on Card A, AS, or Pinchuk. Does not consume
`G2-PSC`.

**History/priority checksum.** `KNOWN:` `(c1,c3)` cheaper dual; generic
`c1` open empty; exceptional raw fibres `C=0,3`; first-stage identity
digest `31b56241…`. `NEW:` using the *denominator* of that identity as the
completeness certificate for a two-parameter neighborhood. `DUPLICATE` if
relaunched as “run the `c1,c3` atlas” without a bivariate `D`.
`SCOPE-CONFLICT:` one-shot affine Smith; promoting line emptiness to SP-2
or a center family; arguing a neighborhood from kernel-0 alone.

**Cheapest discriminator.** Re-emit the 28-row lift with `c3` an
indeterminate. Either `D` appears as a polynomial in `(c1,c3)` with the
same `-k/50` remainder, or the multipliers fail to stay polynomial. No
AWS. Do not widen to three centers until the plane exists.

**Interpretation of every outcome.**

- No polynomial `D(c1,c3)`: neighborhood architecture fails. Stop the
  family claim. Keep the line (if confirmed) as a one-parameter theorem
  and return to exceptional `c3` dual / other moduli. Sensitivity remains
  a gate, not a kill.
- Polynomial `D` exists and remainder is the unit `-k/50` off `D=0`:
  generic plane empty. Cover `D=0` by raw rebuilds, componentwise, with
  Bezout inverses as on `J`. Empty cover: licensed `(c1,c3)` plane empty,
  still not SP-2. Nonempty component: that curve is the new exceptional
  family, the honest SP-2 successor.
- Remainder depends on `c3` and vanishes somewhere off `D=0`: the unit
  `-k/50` was line-specific. Do not promote. Record the actual remainder
  as the new obstruction polynomial.
- Using previous/pole parameterization on a raw exceptional rebuild, or
  the rejected 110-by-132 model: `TYPE-FAIL`, discard.

**Stop condition.** Any SP-2 or JC2 sentence; three-center Groebner; AWS;
mutating frozen line certificates; launching boundary/dead-stretch/F1/pole
deformations from this card.

**Expected information gain.** A binary decision whether one empty line
plus an explicit denominator yields a genuine plane obstruction, or
whether `-k/50` does not survive the extra modulus. Completeness is
checkable because it is the vanishing of a written polynomial.

### Card C — `FROB-POLAR-AUTOMATON`

**Mechanism.** Rebuild the D8 inhomogeneous column as the D10 column plus
the Frobenius polarization `[K_Frob/3] mod 3`. Convert empty structural
bases of the *corrected* matrix, over nonreduced `H`, into Fitting-forced
digits. Those digits are the first letter of a vertical/g-endpoint
automaton: bounded cycle, linear growth, or unit death.

**Dependencies.** **THEOREM:** max-11; D10 pointwise gate; divided-carry
residual `L/3+K+C_x+D_y`; cyclotomic odd-degree false positives.
**ERRATUM:** retracted D9/D8 census; witnesses (5) and (6). **PACKET-CLAIM:**
new `314127/1594323`, `918/354294`, twelve / 360 empty bases — not inputs.
Does not depend on Card A or the `c1` line. D12 interpretation still
requires this predecessor.

**History/priority checksum.** `KNOWN:` Cartier-first D7; D10 Fitting
ranks; divided carry; D12-direct-carry deferred for missing predecessor;
`I_4(A)=0` only modulo `sqrt(H)`. `NEW:` polarization of `K` as the
derivation that repairs the column; empty bases as forced digits of a
finite automaton rather than a census. `DUPLICATE` if it re-runs the
quarantined D9/D8 generator or classifies D7 as a disproof target.
`SCOPE-CONFLICT:` radicalizing `H`; promoting literal-`F3` SAT; `p=109`;
all-depth lifting from field points of `sqrt(J)`.

**Cheapest discriminator.** Replay erratum witnesses (5) and (6) from
independent integer expansion. Emit the six-direction polarization, add it
to the frozen D8 column, and recompute `I_1` / `I_4` over nonreduced `H`.
Independent Singular pairing. The retracted census is not replayed as
evidence.

**Interpretation of every outcome.**

- Polarization misses the witnesses, or the quotient is not integral:
  engine `TYPE-FAIL`. Stop. Repair against `U=x^3 y^2`, `V=x^2 y` and the
  two named Frobenius witnesses.
- Corrected column kills the vertical global D9 section: previous
  “preservation” was false. Record the scope change; do not promote
  emptiness of `D=7`.
- Corrected Fitting forces a finite set of digits (the honest version of
  “empty structural bases”): freeze the forced pattern and push one more
  row. Unit Cartier: branch death, still not JC2. Bounded repeating
  support: algebraization candidate, freeze and hostile review, still not
  a characteristic-zero lift. Linear growth: restricted-analytic control,
  already known, stop as a CE hunt.
- D7–D11 SAT after integer expansion: compiler or history bug
  (**THEOREM** max-11). Fail closed.
- Using `sqrt(H)` or the retracted `13 x 14` `g`-system: `TYPE-FAIL`,
  discard.

**Stop condition.** Any `p=109` enumeration; promoting Z3 UNSAT;
radicalizing away the embedded component `E`; restoring a gauge cap;
identifying Cartier class with `A_infinity`; spending a research slot on
full D7 primary decomposition; treating packet census numbers as licensed.

**Expected information gain.** Converts the erratum into the missing
predecessor that later D12 work was correctly denied, or exposes that the
vertical D9 section does not survive source-honest D8. Either outcome is
strictly more than a new `F3` count.

---

## 8. Continue / redesign / stop — major lanes

| Lane | Call | Scope |
|---|---|---|
| Max-11 / `(6,9),3\|H` composition | **STOP** as research | **THEOREM**. Keep as input. |
| DZ20 undeformed coprime `k=mu=nu=0` | **STOP** as research | **THEOREM**. Keep as input. |
| Full-absorption `B` into `W` | **STOP** as research | **THEOREM**. Keep as input. Not the generic fibre. |
| Parity genus-five exclusion | **CONTINUE** as review only | **PROVISIONAL**. Do not promote. If confirmed, **STOP** as research and use as Card A negative control. |
| `(9,12)` leftover `nu!=0` strata | **REDESIGN** then continue | Even-`B` `tau`-descent (Card A). Raw global Groebner is a cross-check. Four-point Hurwitz is type, not a list. |
| `(9,12)` Taylor boundaries / order-one core | **CONTINUE** | Charged on every branch. Do not drop after Card A. |
| `(8,12)` | **CONTINUE** as spectral/DS control, not as a second fibre worker | Bound-5 on `g^2-f^3`; order-four raw-width control. Even-`B` is special to the quadratic `(9,12)` Wronskian. |
| Nonzero `k` or `mu` loaded cells | **CONTINUE** as residual cells | Do not fold into Card A. |
| Pinchuk 2021 Thm 3.4 | **STOP** as proof client | **GAP**. Retain Thm 4.1 as a local identity. Not avenue 24. |
| ML 2022/2025/2024/2026 | **STOP** as a campaign bridge | Conditional Newton-frame facts. Licensed clients: provenance-bearing row checker and bounded Faber packaging, only if a slot is idle. |
| TD6 licensed q2 pencil | **STOP** | **THEOREM** empty in the fixed normalized section. |
| TD6 centering 3,602-column tangent | **STOP** as a family search | **THEOREM** sensitivity at a nonsolution. Not a neighborhood. |
| TD6 `c1` line union | **CONTINUE** as review; **REDESIGN** if confirmed | Card B bivariate denominator. Do not promote to SP-2. |
| TD6 `c3` dual / remaining exceptional moduli | **CONTINUE** until Card B decides | If bivariate `D` exists, these become the `D=0` cover. If not, they remain the sheet-six successor. |
| TD6 SP-2 / eight classes / `G2-PSC` / `G2-BD` | **CONTINUE** as debts | No new licence from an empty line. |
| AS 29-row deep-branch package | **STOP** | Quarantined; omitted divided carry. Bytes not mutated. |
| AS D10 pointwise gate | **STOP** as research | **THEOREM**. Keep as input. Not a next-digit classification. |
| AS post-D10 D9/D8 census | **STOP** | Retracted. Frozen bytes immutable. Do not consume `50939`, `954`, or the new unlicensed counts. |
| AS vertical D9 section / D8 matrix | **REDESIGN** | Preserve only after the polarization column is rebuilt (Card C). Matrix/rank loci may survive; the inhomogeneous column does not. |
| AS F-only D8–D11 | **CONTINUE** only as theorem-consistent negative controls | Expected empty in characteristic zero by max-11. SAT is a bug. |
| AS F-only D12 | **DEFER** | Still no typed predecessor until Card C exists. Even D12 remains outside the odd cyclotomic motif. |
| Simultaneous map/gauge caps / linear law | **STOP** | **THEOREM** wrong category and false law. |
| Polar versus `A_infinity` / deck descent | **STOP** as current discriminator | Reserve theorems. |
| Ordinary action residues, dual pencil, HC4, secant connectedness, independent-slot AS, closed-support grammar | **STOP** | Dual-confirmed costume or no-grammar. |
| D-series, D75, B=168, unrestricted Witt depth | **STOP** | No typed source. |
| Generic sparse search, exponent rectangles, `p=109`, AWS expansion | **STOP** | Box01 core protected; boxes 02/03 stopped. Current bottlenecks are symbolic structure and certificates. |
| Real Pinchuk deformation (avenue 24) | **STOP** | Orthogonal. |
| Book-cell expansion, DIR/A-SCALE, primitive-group census without a support bound | **STOP** | Unchanged holds. |
| Broad web sweep #9 | **CONTINUE** (due `21:25Z`) | Competitors and old-but-newly-found sources, not only a date window. |

**Redesign, not stop:** leftover max-12 (even-`B` observer before Groebner),
TD6 family coverage (bivariate denominator before another 3,602-column
search), and AS next-carry (polarization column before any census).
Remaining unbounded disproof work is still `A_infinity=0`, rational deck
descent, or a bounded-support all-depth cycle — not another cap compiler.

---

## 9. What this scan refuses

- Reading any other `ideation-20260824T2024Z-*.md` submission.
- Treating parity genus five, the TD6 `c1` line, or any post-D10 census as
  a promoted theorem.
- Calling maximum 12 empty from leftover-leaf classification.
- Treating four-point Hurwitz, equal-critical-value, or a unitree list as
  a finite `C(x)` classification.
- Promoting a neighborhood from centering rank 3, or SP-2 from one empty
  line.
- Promoting finite-depth AS survivors, cyclotomic or not, to
  characteristic-zero lifts; promoting retracted or unlicensed `F3` counts.
- Relabelling the `1820Z` spectral/`W` card, the `1633Z` Zannier watch,
  parity genus five, the `(c1,c3)` atlas, D12-direct-carry, or Cartier-first
  D7 as new.
- Launching work that interrupts the `(9,12)` fibre compiler, the TD6
  line-review / `c3` arithmetic, or the AS source-audit of the erratum.
- AWS, `p=109` brute force, a new book cell, or editing any canonical /
  producer / reviewer / case / packet / run / log / prompt / source file.

No proof or counterexample follows from this packet.
