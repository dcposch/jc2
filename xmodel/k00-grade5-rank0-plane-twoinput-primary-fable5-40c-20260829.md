# K00 literal grade-five gate over the rank-zero plane, two input variants

Author: Fable 5, equal-standing primary researcher
Date: 2026-08-29
Lifecycle: **PRIMARY EXACT DESK + CAPPED-ENGINE THEOREM / PROVISIONAL /
CONDITIONAL ON THE PARALLEL GRADE-FOUR REVIEW / NO CANONICAL PROMOTION**
Frozen campaign basis: `40c1ab3448209e3d87173feb947a733f6fe54f7f`
(verified by `git rev-parse HEAD` at start of work; working tree carried
only untracked xmodel lane artifacts and the pre-existing `jc2-lean`
modification, which I never touched).

## 0. Binary disposition

```text
K00_G5_RANK0_PLANE_TWOINPUT
  SCHEME VARIANT  I5S              = PROPER (rational witness; NF(1)=1 in
                                     the completed L-frame std)
  RADICAL VARIANT I5R              = PROPER (same witnesses; NF(1)=1)
  GEOMETRIC LOCI OF THE VARIANTS   = IDENTICAL (desk certificates)
  DIMENSION (both variants)        = 9  (u-frame, z determined)
  d*_4  BLOCK ON THE PLANE         = DISAPPEARS IDENTICALLY (proved, not
                                     merely observed: shifted-matrix law)
  k10_1 ON THE PLANE               = DISAPPEARS IDENTICALLY (same)
  d*_3 = v BLOCK                   = RETURNS in rows 1,2,3,4,5,7
  k10_0                            = RETURNS in rows 1,2,3,5,7
  BASE COLLAPSE                    = s,t both nilpotent: s^13, t^13 in I5R,
                                     s^12, t^12 not in I5R
  MINIMAL PRIMES OF I5R            = exactly 3, all dim 9 (P_A, P_B, P_C)
  LOCALIZER z*k10_0-1              = LOAD-BEARING: dim rises 9 -> 11
                                     without it; kills the only
                                     (s,t)-nonzero branch (forced k=0)
  CONDITIONAL BRANCH KILL          = NOT AVAILABLE (nonempty stratum)
  charge_basis                     = ABSENT (no exit price asserted)
```

Four engine sub-computations hit the 60 s CPU cap and are typed
`RESOURCE_CAP_NO_VERDICT`; every headline above rests only on completed
exact computations, and the capped items are preregistered for AWS
(§12).  Fail mode closed throughout.

## 1. Conditionality and charged inputs

The upstream grade-three plane is consumed as **promoted** via
`xmodel/k00-rank5-rankle1-coordinator-integration-sol56-20260829.md`
(full SHA-256
`d453b9563d8f6cc23319d6bc0d8edce8a83f657b9e3a60cb244b00f181459860`,
re-hashed here).  Opus's grade-four primary
`xmodel/k00-grade4-rank0-plane-primary-opus5-92e-20260829.md`
(`0d2a9861126c8857e04a9170c8586b6b4eabe67d2e65d3b4d3b7e991774b614f`,
re-hashed) is charged **only as a provisional branch specification**;
it is under a simultaneous Grok review, and every formula I consume
from it (the plane, `mu`, `CF4`, the radical pair `RA,RB`) is
**independently reconstructed from the frozen atlas below and
re-proved in this file**.  Every conclusion here is conditional on that
review; if the grade-four statement is repaired, §5–§9 must be re-derived
on the repaired object.

Independently re-hashed charged inputs (`sha256  path`, repository-relative):

```text
d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501
  cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827/aws_box02_r2_held_compile/output/ATLAS_EXACT_POLYNOMIALS.json
5de20da0d3501db668fca38db3c678ba4719745e3df7b32d0d0a8d2867e4da32  .../output/COMPILED_SOURCE.sha256
ea2f8a4519a5a0bb1dcf35edbb02bc9600971f8b16eb90cb2b64367c6b1bafd8  .../output/CONTROLS.json
72dd452d67a1674f463fab4690c277fa1ff2dc0ab2c72548823100a3b6c0a379  .../output/SOURCE_RECONSTRUCTION_FIXTURES.json
439844a080fcc6fa738bc81efc78a46c72a2ef965ec281168f49aa2870145dc2  .../output/V24R2_DEPENDENCY.json
f1a6f1fc988fc77816daaab13b294b1321de7e476d2891cf7fbfa2e033868d97  .../output/RESULT.json
24640d0dacec16b27b4c7eb83419188aa86e3fc80b481b0ba64aa136348fc892  cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827/compile_fitting_atlas_v26.py
ce5063930117bc8fe9869dc80f1535459dd41209a35406ed7edacde1213618dd  cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827/aws_r6a_alt_full_p6_rank2_chart_r5r7_c6c7/output/P6_LITERAL_SOURCE_LABELS.json
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
```

The atlas hash equals the entry inside `COMPILED_SOURCE.sha256`.
`V24R2_DEPENDENCY.json` still records
`release_allowed=false / HELD_MISSING_EXACT_Q_V24R2_ENDPOINT`; nothing
here is a release.  `CONTROLS.json` booleans are not charged as
evidence; every control relied on was re-run here.  No web, commit,
push, canonical edit, AWS, or external message; `jc2-lean` never read,
listed, or touched.  Scratch lived only in `/tmp/k00g5/`; the only
repository file created is this report.

## 2. Source reconstruction and label verification

All 49 literal rows `(Lambda_grade 0..6, row 1..7)` were rebuilt from
`exact_terms` alone with exact `Fraction` arithmetic (term-record length
`ncols` as the positional bound, `KeyError` on any unmapped name, no
`size`-proxies), then verified against **four** independent label
conventions:

```text
OK_DIGEST 49/49   (producer p_digest: sha256(canonical_json(payload)))
OK_TEXT   49/49   (producer p_text singular string, byte-exact)
OK_TERMS  49/49   (stored term counts)
OK_XLABEL 49/49   (V27 cross-artifact sha256(text.strip()+"\n"))
Q1TO6_MATCH_LITERAL_G2 6/6  (atlas Q1_to_Q6 section == literal grade-2 rows)
```

The digest and text conventions were read from the producer
`compile_fitting_atlas_v26.py` (producer-declared, not divined); the
contents are independently reconstructed.  Ring metadata:
`ring_variables` = the declared 33 names, `honest_newest` =
`d*_6, k10_3`.  Per-grade support (computed, not assumed):

```text
grade 2: d*_1            grade 3: d*_1,d*_2
grade 4: d*_1,d*_2,d*_3,k10_0
grade 5: d*_1,d*_2,d*_3,d*_4,k10_0,k10_1
grade 6: d*_1..d*_5,k10_0,k10_1,k10_2
```

The 49 payloads were distilled to `/tmp/k00g5/rows.json`
(`142403fb28532db0138f9e476b713a737becf7bdcdb048c99752d22dedf5cf54`,
155567 bytes); every later stage reads only this file.

## 3. Declared rings and maps

Coefficient field `Q` throughout; exact rationals; no floats, no
modular reduction.  `dp` ordering in every Singular ring.

```text
T   = Q[s,t,u0..u5,v0..v5,k,z]                    (u-frame, 16 gens)
phi5: d*_1 -> Pi = (2s, t/8, s, t, s, 2t)          (the promoted plane)
      di_2 -> ui,  di_3 -> vi,  di_4 -> xi,  k10_0 -> k,  k10_1 -> k1
mu  = (s^2, s*t/8, 16*t^2, 0, 0, 0);   w := u - mu
RA  = 16*u1-4*u3+u5-2*s*t = A(u-mu),  RB = u0-4*u2+2*u4-s^2+64*t^2 = B(u-mu)
A(x)= 16*x1-4*x3+x5,  B(x) = x0-4*x2+2*x4
y1  = 2*u3-u5,   y2 = u2-u4-16*t^2    (chart-free quotient coordinates)
```

Independent replays of the branch spec (all from my own reconstruction):
`G2_IMAGE_ZERO_SLOTS 7/7`, `G3_IMAGE_ZERO_SLOTS 7/7`, and the grade-four
closed form `CF4: phi(Lambda_{4,r}) = Q_r(u-mu)` generatorwise
(`CF4_MATCH 7/7`, term counts 16,21,20,24,19,0,14).  These replays are
verification of formulas consumed, not a review of the upstream claim.

## 4. The two-input grade-five question (as built)

`x = d*_4` and `k1 = k10_1` disappear identically on the plane (proved
in §5), so by the retention rule (every variable at the first grade
where it genuinely survives) the ring is `T` above: `z*k10_0-1` retained,
full `u` and `v` blocks retained, `k10_0` never projected away.

```text
G5S = ( phi5(Lambda_{5,1}), ..., phi5(Lambda_{5,7}) )   (7 literal images)
G4S = ( phi(Lambda_{4,1}),  ..., phi(Lambda_{4,7})  )   (= Q_r(u-mu); row 6 = 0)

I5S := G4S + G5S + (z*k-1)         (scheme-input variant)
I5R := (RA, RB) + G5S + (z*k-1)    (radical-input variant)
```

Questions: unit/proper; dimension; the cheapest exact discriminator for
each; whether the variants share their geometric locus; and the
structural form of the new constraints.  Machine-readable exact copies:
`g4sub.txt`
`9f34a6d817a8bb38cd8a0d3d96a14d6e79bca7d56b07ed694d6ee4df3146bfe6`,
`g5sub.txt`
`2b3a8a35c625fca47da82802a0d8496cce1747a27ecea696c02197b46dd2bbaa`.

## 5. Literal grade-five structure (all exact identities)

Class census of the un-substituted rows (block exponents
`(e_d1,e_d2,e_d3,e_d4,e_k10_0,e_k10_1)`, all weight 5, 0 bad terms):

```text
(0,1,1,0,0,0) d2*d3      rows 1-5,7      (1,2,0,0,0,0) d1*d2^2   rows 1-7
(1,0,0,1,0,0) d1*d4      rows 1-5,7      (2,0,1,0,0,0) d1^2*d3   rows 1-7
(1,1,0,0,1,0) d1*d2*k0   rows 1-7        (3,1,0,0,0,0) d1^3*d2   rows 1-7
(2,0,0,0,0,1) d1^2*k1    rows 1-7        (5,0,0,0,0,0) d1^5      rows 3-7
(3,0,0,0,1,0) d1^3*k0    rows 1-7
ABSENT classes: d3*k10_0, d1*k10_0^2, d2*k10_1, k10_0*k10_1
```

Hence no `k*v` or `k^2` monomial can occur after substitution: the
substituted system is **affine-linear in `(v,k)` jointly** over the
base — before any ideal work.

**Shifted-matrix laws (proofs of disappearance).**

```text
coeff of d_j4  in Lambda_{5,r}  ==  coeff of d_j2 in Lambda_{3,r}   42/42
coeff of k10_1 in Lambda_{5,r}  ==  coeff of k10_0 in Lambda_{4,r}   7/7
(re-verified: coeff of d_j3 in Lambda_{4,r} == coeff of d_j2 in
 Lambda_{3,r}, 42/42 — the branch spec's C-matrix law)
```

The first matrix is `C = A[:,1..6]`, all of whose entries vanish on the
plane by the promoted integration; the second is the quadratic `M_r`,
which vanishes on the plane (grade-four fact, replayed).  So `d*_4` and
`k10_1` disappearance is structural, not coincidental.  Substitution
confirms: **no `x`, no `k1` in any of the seven images**; `v` present in
rows 1,2,3,4,5,7; `k` present in rows 1,2,3,5,7; image term counts
`42,49,57,53,64,33,61` (from `83,106,133,160,186,184,235`).  This
reproduces the branch spec's §8.4 scan exactly, from an independent
reconstruction.  Row 6 is a pure `(s,t,u)` constraint at grade five.

## 6. The exact grade-five closed form (CF5)

For every `r`, as polynomial identities:

```text
phi5(Lambda_{5,r}) = B_r(u-mu, v)  +  k*H_r(s,t,u)  +  W2_r(s,t, u-mu)
```

* **v-part = polar, 42/42.**  The coefficient of `v_j` equals
  `(dQ_r/dw_j)(u-mu)` — the polarization of the grade-two quadric at the
  shifted argument.  So the `v`-block enters exactly as the polar
  `B_r(u-mu, v)`.
* **No v-shift and no pure part: `nu = 0`.**  Writing the `(v,k)`-free
  remainder in the shifted frame `u = w + mu`, its `w`-linear and
  `w`-free parts vanish identically for all seven rows (`R1 = R0 = 0`).
  The grade-five analog of `mu` is the zero vector.
* **k-coefficient, unique decomposition.**
  `H_r = phi_r(s,t)*A(u) + psi_r(s,t)*B(u) + eta_r(s,t)` solved uniquely
  (nullity 0) for every row; `H_4 = H_6 = 0`.  Rewriting via
  `A(u) = A(w)+2st`, `B(u) = B(w)+s^2-64t^2` gives
  `H_r = phi_r*A(w) + psi_r*B(w) + h_r(s,t)` with **two cubic channels**:

  ```text
  chi_1 = t*(3s^2-64t^2)          chi_2 = s*(s^2-192t^2)
  rows 1,3,5,7:  h_r = (5/12)*c_r*chi_1     (exact ratio law)
  row 2:         h_2 = (5/65536)*chi_2
  where c_r = 3/1024, -3/8192, -3/131072, -3/1048576  (rows 1,3,5,7)
  ```

* **W2 (the `w`-quadratic remainder).**  `(s,t)`-linear times
  `w`-quadratic.  `W2_6 = (3/32)t*Q1(w) - (1/32)s*Q2(w) - (1/4)t*Q3(w)`
  exactly, so **row 6 lies in the scheme-input ideal** (and a fortiori in
  the radical input).  For rows 1,2,3,4,5,7, `W2_r` is **not** in
  `span{s,t}·{Q_j(w)}` and **not** in the ideal `(A(w),B(w))`
  (INCONSISTENT solves), and the shared-shear ansatz
  `W2_r = B_r(w, rho(w;s,t))` fails.  This failure is a theorem, not a
  gap: its consequences are the base cuts below.

**Membership certificates** (exact linear algebra, both directions of
the locus comparison):

```text
Q_j(w) = lamA_j(w)*A(w) + lamB_j(w)*B(w)   for all 6 nonzero rows
         (explicit linear lamA_j, lamB_j printed in the transcript)
A(w)*B(w) = (2048/3)*Q1(w) + (16384/3)*Q3(w)
A(w)^3, B(w)^3, A(w)^2*B(w)  in  (Q_j(w))-ideal (linear coefficients)
A(w)^2, B(w)^2               NOT in Q2 (INCONSISTENT — negative controls)
POLARIZATION_VIA_LAMBDA 6/6:
  B_r(w,v) = lamA_r(w)A(v) + lamA_r(v)A(w) + lamB_r(w)B(v) + lamB_r(v)B(w)
```

Consequences: `V(G4S) = V(RA,RB)` set-theoretically, `G4S subset (RA,RB)`
as ideals (also re-verified by the substitution kernel: 7/7 grade-four
images reduce to 0), hence `I5S subset I5R` as **ideals**, and the two
variants have **identical geometric loci**.  On `K = V(A(w),B(w))` every
`lamA_r, lamB_r` restricts to a form in the quotient coordinates only:

```text
rows 1,3,5,7: (lamA_r, lamB_r)|K = c_r*(y2, y1/2)
row 2:        (-3/512*y1, 3/16384*y2)        row 4: (0, 0)   row 6: (0, 0)
```

Row 4's polar and `k`-parts both vanish on `K`.

## 7. Base cuts, reduction chain, and the essential ideal

Reduction mod `(RA,RB)` is the substitution homomorphism
`u1 -> (2st+4u3-u5)/16`, `u0 -> s^2-64t^2+4u2-2u4` (kernel exactly
`(RA,RB)`; `reduce(RA)=reduce(RB)=0` checked).  Writing `FKr :=
reduce(phi5(Lambda_{5,r}))`, the following are **exact identities**:

```text
FK6 = 0
FK4 = (3/32768) * PHI,   PHI := s*(16*y1^2 - y2^2) + 64*t*y1*y2
FK3 = (-1/8)   FK1 + (3/2048)   PSI
FK5 = (-1/128) FK1 - (3/16384)  PSI      PSI := 16*t*y1^2 - t*y2^2
FK7 = (-1/1024)FK1 - (3/262144) PSI             - s*y1*y2
```

with `y1 = 2u3-u5`, `y2 = u2-u4-16t^2` — chart-free.  So modulo the
radical grade-four input the seven grade-five rows are generated by
`FK1, FK2, PHI, PSI`: **two affine-linear rows, plus two pure base
cubics**.  Row 4 of grade five *is* the base cut `PHI` on the reduced
locus; `PSI` is forced by the row-{3,5,7}-vs-row-1 differences.  In the
matrix form `[PHI; PSI] = G(y)·(s,t)^T` one has
`det G = (16*y1^2 + y2^2)^2`.

After the further changes of variables `u-block -> (y1,y2,w4,w5)`
(polynomial automorphism over `Q[s,t]`) and `v -> (av,bv,v2..v5)` with
`av = A(v)`, `bv = B(v)` (linear), the variables `v2..v5` disappear
entirely and

```text
I5R  ~  Q[v2..v5]  (x)  ESS,
ESS = ( E1, E2, PHI, PSI, z*k-1 )  in  Q[s,t,y1,y2,w4,w5,av,bv,k,z]

E1*(1024/3) = av*y2 + (1/2)bv*y1 + (5/4)k*s^2*t - (80/3)k*t^3
              - s*w4*y1 - s*w5*y2 - 2t*w4*y2 + 32t*w5*y1 - 32t*y1^2
E2*(16384/3)= -32av*y1 + bv*y2 + (5/12)k*s^3 - 80k*s*t^2
              - 2s*w4*y2 + 32s*w5*y1 - 32s*y1^2 + 64t*w4*y1
              + 64t*w5*y2 - 128t*y1*y2
```

Every step is a certified ideal-preserving operation (substitution
quotient; polynomial automorphisms fixing `Q[s,t]`; linear changes;
cylinder), so `dim I5R = 4 + dim ESS`, `s^m, t^m` membership and the
`(s,t)`-, `v`-, `(k,z)`-eliminations transport verbatim.  Multiplicities
do **not** transport across the non-linear steps and are reported
per declared frame only.

## 8. Geometry: collapse, three components, witnesses

Completed engine results on `ESS` (Singular 4.4.1, 1.0 s + 0.6 s):

```text
ESS_STD:  NF1=1  DIM=5  MULT=128   (slimgb agrees, mutual reduction 0)
=> dim I5R = 9  (u-frame; z determined by k)
S_POW_IN_ESS = 13   T_POW_IN_ESS = 13     (indices exactly 13; none <= 12)
minAssGTZ: exactly 3 primes, each dim 5, matching the predicted primes
both ways (mutual NF = 0):
  P_A = (s, t, av, bv, z*k-1)
  P_B = (s, t, y1, y2, z*k-1)
  P_C = (s, t, 16*y1^2+y2^2, 64*av^2+bv^2,
         32*y1*av - y2*bv, 2*y2*av + y1*bv, z*k-1)
radical(ESS) = P_A cap P_B cap P_C   (mutual reduction 0; RAD dim 5 mult 8)
ELIM  ESS cap Q[s,t] = 8 generators, degree up to 13 (contains t^13,
      s*t^11, t^9*(11s^2-64t^2), s*t^6*chi_1, ...; radical (s,t))
ELIM  ESS cap Q[av,bv] = (0)         ELIM  ESS cap Q[k,z] = (z*k-1)
```

Pulled back to the u-frame, the three minimal primes of `sqrt(I5R)` are

```text
P_A: s=t=0,  A(u)=B(u)=0,  A(v)=B(v)=0,  k != 0        (dim 9)
P_B: s=t=0,  u in the plane L itself (4 linear forms),  v free,  k != 0
P_C: s=t=0,  A(u)=B(u)=0,  16*y1^2+y2^2 = 0,  the conjugate coupling
     {y2 = ±4i*y1, B(v) = ∓8i*A(v)} (Q-irreducible, geometrically two
     conjugate components), k != 0                      (dim 9)
```

**Witnesses**, each certified by direct exact substitution into the
literal atlas rows (grades 2,3,4,5 all 7/7 zero):

```text
V_A: s=t=0, u=(-2,1/4,1,2,3,4), v=(10,3/4,-1,5,-7,8), k=7
V_B: s=t=0, u=2e_a+3e_b=(4,3/8,2,3,2,6), v=(1,2,3,4,5,6), k=5
V_C: s=t=0, u=(16i,1/8,4i,1/2,0,0), v=(-8i,1/16,0,0,0,0), k=3   (Q(i))
NEG controls: v not in K at y!=0 -> 2/7;  s=t=1 -> grade-4 1/7, grade-5 0/7
```

**Death of the fourth branch and the role of `k10_0`.**  The only
candidate branch with `(s,t) != (0,0)` lives over the conjugate lines
`y2 = ±4i*y1`, `s = ∓8i*t`.  Three exact Gaussian-rational probes
(different `t, y1, w4, w5, v`-support) all force **`k = 0` exactly**
there; the localizer kills the branch.  So `k10_0` returns in the rows,
is unconstrained on the surviving locus, and is load-bearing precisely
in eliminating the `(s,t) != 0` branch and the `y=0, (s,t)`-free branch
(`ESS` without the localizer: `NF1=1 DIM=7 MULT=2`, i.e. dim 11 in the
u-frame; the `z*k` mutation admits `k=0` with dim 7; `ESS + (k)` is the
unit ideal).

**What grade five constrains, blockwise** (contrast with grade four,
where every single-block projection was surjective): `s,t` are killed
(nilpotently, index 13); `u` is confined to the 4-plane
`A(u)=B(u)=0` (both forms vanish on every component; the two plane
directions inside `u` stay free on every component); `v` is cut to
`A(v)=B(v)=0` on `P_A`, quadratically coupled on `P_C`, and free on
`P_B`; `k` is free.  `I5R cap Q[v-block] = (0)` and
`I5R cap Q[k,z] = (z*k-1)` (both also forced by the witnesses); the
`(s,t)`-elimination is the nontrivial degree-13 ideal above.

## 9. Answers and cheapest exact discriminators

* **Unit/proper.**  Both variants **PROPER**.  Cheapest discriminator:
  the rational witness `V_A` (or the weight argument at
  `s=t=u=v=0, k=1`), evaluated on the literal generators — no Groebner
  at all.  Engine confirmations: `NF(1)=1` for `ESS` (=> `I5R`) and for
  the completed L-frame std of the scheme variant.
* **Dimension.**  Both variants **dim 9**.  Cheapest for `I5R`: the
  certified cylinder `4 + dim(ESS)` with `dim(ESS)=5` (1 s).  Cheapest
  for `I5S`: no scheme-variant Groebner is needed — the desk
  certificates `G4S subset (RA,RB)` and `A^3,B^3 in Q2` force
  `sqrt(I5S) = sqrt(I5R)`, and dimension depends only on the radical.
  Independent confirmation: the completed sparse-frame
  `std(I5SL)` printed `NF1=1 DIM=9 MULT=242` before its slimgb tail
  capped.
* **Same geometric locus.**  **YES** — by the §6 certificates (ideal
  containment one way, cube membership the other).  This is a desk
  theorem; no engine run is charged for it.
* **Scheme vs radical as schemes.**  `I5S ⊊ I5R` strictly:
  containment by the substitution-kernel certificate; strictness because
  at the witness `P0 = (s=t=0,u=0,v=0,k=z=1)` every `I5S` generator has
  zero differential except `z*k-1` (differential `dz+dk`), while
  `dRA(P0) = 16du1-4du3+du5` is independent of it — a cotangent
  obstruction, so `RA not in I5S`.  Nilpotent structure transported from
  the completed L-frame std: `RA, RB` have nilpotency index **exactly 3**
  modulo `I5S` (the index loop rejected the first powers and squares and
  accepted the cubes: `AW_POW=BW_POW=3`, and `RA -> aw` under the
  frame maps).  `s,t` indices modulo `I5S` exceed 16 (AWS item A1 pins
  them; they are >= 13 by containment).
* **Multiplicities (frame-declared).**  `mult(ESS) = 128`,
  `mult(radical ESS) = 8 = 2+2+4` (the `z*k-1` torus doubles each
  linear piece; `P_C` is two conjugate degree-2 pieces).  Scheme variant
  in the L-frame: `mult 242`.  u-frame multiplicities: not computed
  locally (capped); AWS item A1.

## 10. Engines, controls, mutations

Engines: Singular 4.4.1 (44105, arm64-Darwin, GMP 6.3.0) and CPython
3.9.6 `fractions.Fraction` — two independent implementations; every
structural identity in §5–§7 was established in Python and every
ideal-theoretic number in Singular, with the bridge files hashed (§11).
`option(redSB)` everywhere; positional loops bounded by `ncols`;
`sat()` unused.

Controls: `CTL_UNIT_NF1=0` (unit reduces), `CTL_PROPER (s)`: `NF1=1
DIM=9` (essential ring); localizer sign gauge `(z*k-1)==(1-z*k)` as
ideals, `z*k+1` same dims (gauge), `z*k` admits `k=0` (caught),
`+(k)` unit (caught); no-localizer dims rise 5->7 (u-frame 9->11).

Identity-level mutation battery (all caught; observables per row):

```text
BASE            g2z=7/7 g3z=7/7 cf4=7/7 xrows=0 k1rows=0 polar_bad=0/42
M1a t/8->t/7    g2z=5/7 g3z=0/7 cf4=0/7 xrows=6 k1rows=7 polar_bad=27/42
M1b 2t->3t      g2z=5/7 g3z=0/7 cf4=0/7 xrows=6 k1rows=7 polar_bad=41/42
M1c 2s->2.001s  g2z=6/7 g3z=1/7 cf4=0/7 xrows=6 k1rows=6 polar_bad=20/42
M1d s->2s(d4_1) g2z=5/7 g3z=0/7 cf4=0/7 xrows=6 k1rows=7 polar_bad=39/42
M-mu 16->15     cf4=1/7 polar_bad=17/42          (plane checks unchanged)
M2a (5,1) d3-coeff x2   polar_bad=1/42            (the exact slot)
M2b (5,1) k0-coeff x2   H1_DECOMP=INCONSISTENT    (unique solve breaks)
M2c (5,4) d2-coeff x2   row4_phi identity fails
```

Every plane mutation resurrects the `d*_4` block and `k10_1` — the
disappearance is pinned to the exact plane.

## 11. Resources and stdout custody

Per-process caps: `RLIMIT_CPU = 60 s` (in-child `setrlimit`); the 1 GiB
RSS bound is enforced by an external `ps`-polling watchdog (0.2 s), as
this Darwin 23.6.0 kernel refuses to lower `RLIMIT_AS/DATA/RSS` — the
same weaker-guarantee disclosure as the grade-four primary.  No run
breached RSS (peak 608 MB, the atlas load).  `vm_stat` swapouts never
moved (31308602 throughout); swapins moved <= 369 pages across the whole
session (background activity).

```text
run         rc   wall_s  cpu_s   rss_kb  stdout_sha256(16)
build        0    2.52    2.45   608000  23c32be2e7cac436
explore5     0    0.21    0.07    14992  6536e94da7bf4c68
cf5          0    0.43    0.29    15472  ea9ace966dcac187
struct5      0    0.43    0.31    15792  b2e75edfda5cb93b
onk          0    0.21    0.08    14784  2691e11e781cc4e1
shift2       1    0.20    0.08    14656  40de22c1a797020a (NameError after
             the shared-shift solve returned INCONSISTENT; the script's
             witness path was built on the refuted hypothesis and is
             superseded by gauss; disclosed, nothing charged)
gauss        0    0.63    0.54    14336  95625308a06f3fc4
verify_psi   0    0.21    0.07    14240  d0499f724a775a83 (2nd run; 1st
             crashed on a missing substitution image, fixed)
vd2          0    0.21    0.12    14064  7b40ba8ab417c0b3
gen_sing     0    0.20    0.07    14672  dcaae56a4b8eb23c
cert_gens    0    0.21    0.09    14784  337820dd99d386ef
ess_gen      0    0.21    0.07    14560  85b3160b666f2bdb
m5           0    1.04    0.94    21056  213a2fabdf76168b
m6           0    0.62    0.44    20880  517c273ec03599c3
schemeframe  0    0.21    0.08    14704  eee384c5151bd5e2
mut5         0    0.64    0.44    14624  47b59bbe5458ea21
mut5b        0    0.20    0.12    14368  3d9630c74842690f
mut5c        0    0.21    0.03    13840  51743220ba03a65f
g6scan       0    0.21    0.08    14000  7841804978faa875
--- capped (SIGXCPU, rc=-24), typed RESOURCE_CAP_NO_VERDICT: ---
m1   60.52s cpu 59.70  rss 605408  empty stdout   (u-frame literal std)
m1a  60.12s cpu 60.05  rss 234400  empty stdout   (u-frame small-gens std)
m1b  60.24s cpu 59.97  rss 197456  empty stdout   (w-frame scheme std)
m7   60.32s cpu 59.93  rss 160816  b1218f7323f95b6c (L-frame scheme:
     std COMPLETED and printed NF1/DIM/MULT/AW,BW indices; only the
     slimgb cross-check tail was killed)
```

No claim rests on any killed portion; the four capped items are exactly
the AWS jobs below.  Scratch artifact hashes (`/tmp/k00g5/`):

```text
59a34b5e59fe3159e99906b19cd0e0e1381a528806e16d2bd385e6a370b734b4  runcap.py
e7e3c41fff8f7ca3d5a340eb7d878492d3da25c71420477f567c42083d39362d  poly.py
344677db25b3afe0ec72d8b97ed7ea1c8e9c025a2305ccf607bb8f231d6b8e07  build.py
891b2348cf580696b1ddedaa00f56b77e5d56b172cf1ff9ee647390b1981f4fb  explore5.py
44306b8d1ecbfc2a669d9e3d8c3cb1ee528de2dad0290b4aa3023c2d821c3c9e  cf5.py
1bf1cb1fc7a93b4bdfd11eb81782c8a7480520c0848201d44b9c2aab1ac5de1f  struct5.py
519a7631bf4ebcc75c1807aafe9c22f2d5e5c3b6d9dc1f3023c2b19836333f06  onk.py
d7fdd88c85139ca43c7c24f1ab5aa5bd42d04f94f3ee693c1a2c6823f5e364a8  shift2.py
2edda9a66150ccf8845f72aae7a5b22948de5545bf1677de5f0d828f50f0ec52  gauss.py
679e9e79f167a153cfa76190e35ab2d5ec284953202c0f8588f2bea1acc178c8  vd2.py
01623ca1a3b3101a848803c89904daef0732ad1d7647884177af44b4b01314a7  verify_psi.py
906f1f7e8a55b03014651b8db8a996070ee650e5adef2b39319e81cc75b9168c  cert_gens.py
ee4491e22739eef5a08f0edf84cf285d223228d99ef31ce590bbe3c61df29354  ess_gen.py
8684fe4f981847c986064886837519890a313b859e7a547f1f330355e1f78163  schemeframe.py
4d86a56c477904496e3ce4577624ce230cc1ac17bff22c6d80e81a173cacfc1e  mut5.py
3ef5ec3d456d3ee1f9e319c26bcf8329909b2a93c5a38f31bd4463747d116fb1  mut5b.py
155e44e4de0364689378fecb49690f8aac7d2b8837477fe67fa04e7175d2109a  mut5c.py
ad7eabdf8580c5e5cddc7ee67b1ba2c87dac3c284cac8e7c2bbd355ad0c33792  gen_sing.py
142403fb28532db0138f9e476b713a737becf7bdcdb048c99752d22dedf5cf54  rows.json
50dd9e18cf480acb281165d733ee9001e9448dadb8dabb792c0c6fc7abc4110d  raw16.sing
49ecef1755492db740f5c7056b07eacb6ccf0bf45b2a52f379b2870ba4f2178f  raw16b.sing
ae54b5ce46decc3fd4ae5d7e760dd04cf7e9da69d364e931505646377a7a6a68  raw16w.sing
89ada2ce0f868bdb2477df2721faa3a78ec11aaaff874f80857d8e1e188f93c8  raw16s.sing
b4ef35cfb870496942cf9ec8844e68803beee486122f1a36e84ac3518421df41  ess.sing
1d84310146ad77274cbda4be7061d418db1fcbecbbfc2784b83384b5d7271b5d  m1_dims.sing
808d4b7a622ceb7e59477782493033a343527c186e5b9fce2095230a9b33372b  m1a_dims.sing
98a4693d0bf007f931c9955226cf4197053af10aaea4aa819f8dd8f020f40302  m1b_wframe.sing
d340e22e3af6c253b42193596053e97080c54d08a881fa6c81285d7e05eb8a1c  m2_controls.sing
844824ccb51173ad0cb3137d783cff0ceeb1a95bf938ebf3f8c9cfd90cdab3e1  m3_minass.sing
2a9c5b9de474970fd62ef23c2e40636de1232cb6dc4eecea7be1a214d1c6a85d  m4_elim.sing
366c04dae7264918ea13fbe512c2fe6bc28e17e4b060dbf303ae19f4821f0c4b  m5_ess.sing
8dd6a3b23f3d3861a317c3896f7e11552937d4f23cba4722fb53f79bcb029dbf  m6_extra.sing
b87762d9a1bc5ad7aa2439317c722e0d6006584a2ee31c219a5ff31f1d31962b  m7_scheme.sing
b80e70dbf15b24f3ceaae4366369e0fc3b594a35f46ca7083300fe12c0e2edbe  g6scan.py
```

Note: `m2_controls.sing`, `m3_minass.sing` and `m4_elim.sing` were
authored for the u-frame and then superseded by the essential-frame
runs `m5/m6` before ever being executed; they were **never run**, no
claim cites them, and they are hashed only for custody.  Their AWS
descendants are jobs A1/A3/A4.

## 12. Preregistered AWS packet (frozen)

Any replay must first regenerate `rows.json` from the atlas
(`d7ec6d18...`) and match
`142403fb28532db0138f9e476b713a737becf7bdcdb048c99752d22dedf5cf54`,
then regenerate the four `raw16*.sing` bridges and `ess.sing` and match
the hashes above.  Literal inputs: the hashed bridge files; ring maps:
§3 and §7 exactly; the two ideals: §4 verbatim.

```text
JOB A1 (u-frame ground truth): m1_dims.sing on raw16.sing and
  raw16b.sing: std+slimgb of I5S and I5R, mutual reduction, NF(1),
  dim, mult (u-frame), s^m/t^m indices m<=25 for both variants,
  RA/RB powers mod I5S, containment NF table.
  Expected: NF1=1, dim 9 both; s,t index 13 for I5R; RA index 3;
  I5S mult >= its radical's.
JOB A2 (scheme cross-basis): finish m7's slimgb + mutual reduction on
  raw16s.sing; expected agreement with std (372 gens, dim 9, mult 242).
JOB A3 (scheme primary structure): minAssGTZ + equidimensional/primary
  data of I5SL (raw16s.sing); expected minimal primes = images of
  P_A, P_B, P_C; embedded structure OPEN (no prediction).
JOB A4 (u-frame eliminations): eliminate I5R and I5S onto Q[s,t],
  Q[u-block], Q[v-block], Q[k,z] in the u-frame; expected radicals
  (s,t), (A(u),B(u)), (0), (z*k-1); generator lists OPEN.
JOB A5 (second-host custody): Linux replay of the complete local suite
  (build -> ... -> m6, g6scan) pinning every stdout hash of §11.
Caps per job: wall 2 h, RSS 8 GiB, no-swap; exact Q only.
Semantics: UNIT / PROPER / RESOURCE_CAP_NO_VERDICT, fail closed;
a cap on any job leaves the corresponding §9 line at its current
evidence level and must not be relabelled.
```

## 13. Grade-six successor scan (preregistration only)

Exact literal identities at grade six (desk, from the same atlas):

```text
coeff of d_j5  in Lambda_{6,r} == coeff of d_j2 in Lambda_{3,r}   42/42
coeff of k10_2 in Lambda_{6,r} == coeff of k10_0 in Lambda_{4,r}    7/7
coeff of d_j4  in Lambda_{6,r} != coeff of d_j3 in Lambda_{4,r}    0/42
```

so on the plane `d*_5` and `k10_2` disappear at grade six, while the
substituted grade-six rows contain `x = d*_4` (rows 1-5,7) and
`k1 = k10_1` (rows 1,2,3,5,7): each block genuinely enters two grades
after its literal debut.  The smallest grade-six question therefore
lives over the grade-five survivor of this file, in
`Q[s,t,u,v,x,k,k1,z]`, with both grade-five input variants inherited.
Nothing about grade six is asserted beyond these three identities and
the support scan.

## 14. Nonclaims

Not a grade-six or later statement (§13 is a scan, not a theorem); not
a formal or convergent arc; a witness is a point, not attainment, and
no floor or price is asserted (`charge_basis` absent by design); not a
source-reachability, order-two, Keller-pair, or JC2 conclusion; not a
review, endorsement, or promotion of the grade-four primary or of the
grade-three exhaustiveness — if the parallel Grok review repairs the
grade-four object, everything from §5 on must be re-derived.  The
scheme variant's u-frame multiplicity, its exact `s,t` nilpotency
indices, its embedded primary structure, and all u-frame elimination
generator lists are typed **OPEN** pending A1–A4.  The `V_D` death
(`k=0` forced) is proved at three exact probe configurations and by the
component census `radical(ESS) = P_A cap P_B cap P_C`; the census is
the binding statement.  Multiplicities are meaningful only in their
declared frames.  Both engines ran on one host under one custody chain;
A5 is the cross-host control.

## 15. Blockers

1. **Parallel grade-four review** (Grok, running): sole upstream
   condition; this file consumes the plane from the *promoted*
   integration and re-proves everything else it uses.
2. **AWS A1–A5**: the four capped computations and the cross-host
   replay.
3. **Successor**: the grade-six question over this survivor (§13),
   both input variants, same guardrails; `x`/`k1` must be retained
   there since they genuinely survive at grade six.

<!-- BODY-END -->

## Seal

```text
body_definition = every byte of this file from offset 0 through the end of
                  the line "<!-- BODY-END -->" inclusive (that marker line
                  occurs exactly once); this Seal section is not body
body_bytes      = 30378
body_sha256     = c3b4293509e741f42ea0df1ad301b2a859ecb2aa46f31b2d5c7afda707327271
frozen_basis    = 40c1ab3448209e3d87173feb947a733f6fe54f7f
atlas_sha256    = d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501
disposition     = PROPER_DIM9_TWOINPUT_SAME_LOCUS_PROVISIONAL
charge_basis    = ABSENT (no new exit price asserted)
fail_mode       = closed
```

The lane runner records the full-file hash out of band.
