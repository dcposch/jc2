# Hostile text-only review — exact D1 control-2 Rees v2

| Field | Value |
|---|---|
| Claim under review | Source-distinct v2 package for the exact finite eight-row control-2 Rees degeneration, plus the already-emitted r6d encoding-B unit. Encoding A may still be live and is not read as a result |
| Overall verdict | **REES_V2_CONFIRMED** as source algebra, contraction/saturation theory, v2 custody, and one-encoding B unit. Dual mathematical endpoint **not promoted** |
| Smallest failing identity | none in the frozen v2 sources or in the r6d B stream |
| Smallest missing hypothesis for a dual theorem | encoding A torus basis, and a cross-encoding comparison of the two emitted `Htor` bases, as preregistered |
| Evidence tier | hand expansion of the nine coefficient images; hand residue evaluation of every emitted B initial form; SHA-256 of frozen text and already-emitted AWS files; inspection of v1 `SOFTWARE_CONTROL.md`. No local Python, Singular, Sage, msolve, Lean, Gfan, or other substantive symbolic computation |
| Reviewer / model | Grok 4.6 (xAI). Text-only algebraic-geometry / computer-algebra referee |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `4fe628a133ae62e16b1bec5e4ed6fcee420dd880` (this package uncommitted) |
| Host | Darwin. Charged reconstruct, v2 compiler, and Singular were not run |

No local substantive computation was run. Hashes were checked with `shasum -a 256`. Git identity was read with `git rev-parse` / `git status --porcelain`. The r6d B streams were read as emitted text.

Frozen hashes charged in the prompt, recomputed and matched:

```text
6ca862b7e0569e58ab04e3bfd18c6230ffe24d83e9461f97dd753396dd8dee95  SOURCE_CLOSURE.sha256
bc57933f4b8d96837e9598dd340077f83099861ddca992060d55449cd6bed876  PRESOLVE_FREEZE.sha256
77c933be81b3242ccf8bf06ef96ca458584b94519a10028431a92e0a69ac2a36  aws_r6d_B/singular.stdout
ec9fe740de4d330fbeaba7a5af5db4e56b36d62f417f051f3c35f85599edd3f1  xmodel/max12-912-order3-d1-double-root-newton-correction-review-grok-v2-20260825.md
```

Nested hashes used below also match, including charged source `67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623`, compiler `dd25bb5bc1196ef41966eed7ab3e903b409a753e47b866f30e9056fdfaa3be48`, worker `45ce271a8c5055be9ea4ffea105d39ea16ae31a9c2d93e888aff59692347d1a6`, empty CAS/compiler stderr `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`, r6d B input `c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b`, r6d payload `0dcd183b4b051b12882d32be54659a312b5ecc03369ee892a188613438070635`, and the freeze chain `SOURCE_CLOSURE → PRECOMPILE_FREEZE → PRESOLVE_FREEZE`.

Read in full before the verdict: `PREREGISTRATION.md`, `compile_control2_rees_v2.py`, `remote_worker_v2.sh`, `AWS_REGISTRATION.md`, `COMPILE_CUSTODY.md`, every r6d B file present in the package, v1 `SOFTWARE_CONTROL.md` together with the v1 worker/compiler as quarantine controls, and the charged Newton v2 correction review.

---

## Promotion

**Accept `THE V2 SOURCE IS AN EXACT, UNTRUNCATED SPECIALIZATION OF THE CHARGED EIGHT-TAIL SYSTEM TO f=(z^3-3z+2)^3+(z^3-3z+2)(q1 z+q0)+(r2 z^2+r1 z+r0) WITH a=1, h=q2=k=nu=0, mu=2/3, TARGETS (2/3)Lambda^15 ON ROW 3 AND Lambda^20(1+tau) ON ROW 8, AND Lambda=tau^3 rho. THE WEIGHT (4,1,1,22,22,30,30,30) IS THE INTEGRAL RAMIFICATION OF (alpha,beta)=(15/2,11/2). THE DISPLAYED RESIDUE (1,1,1,1,-1,1,1,-2) IS THE LEADING PART OF THE ALREADY CERTIFIED CONTROL-2 JET; -t^38/2 IS A LATER COEFFICIENT OF r0. SUBSTITUTING X |-> s^w X AND SATURATING BY s, OR ELIMINATING FROM u s-1, THEN SETTING s=0, COMPUTES THE FULL INITIAL IDEAL, NOT THE GENERATOR-INITIAL PREVARIETY. TORUS SATURATION BY THE PRODUCT OF ALL EIGHT COORDINATES, OR THE INDEPENDENT INVERSE v, LOCALIZES TO THAT TORUS. THE R6D B STREAM IS CUSTODY-CLEAN AND PRINTS Htor=(1), HENCE THIS FROZEN-AXIS FIXED-LOAD WEIGHT HAS EMPTY TORUS SPECIAL FIBRE IN ENCODING B, AND THE DISPLAYED RESIDUE HAS NO LIFT IN THAT ENCODING. V1 IS QUARANTINED AND CANNOT SUPPORT MATH. ENCODING A IS NOT A RESULT. THIS IS NOT D1 AND NOT JC2.`**

Do not promote this to: a dual-encoding theorem; emptiness of coordinate-hyperplane loci; moving axis; `q2!=0`; other weights, residues, or loads; the full double-root fan; a formal D1 arc; or JC2.

---

## Charge 1 — nine specialized coefficient images, loads, targets, toric relation

**CONFIRMED**

Work at the frozen centre `K=L^2 U=(z-1)^2(z+2)=z^3-3z+2` and

```text
f = K^3 + K(q1 z + q0) + (r2 z^2 + r1 z + r0),
```

with `q2=k=0` identically. Expand by hand.

**K^3.** Write `K=z^3+(2-3z)`. Then

```text
K^3 = z^9 + 3 z^6(2-3z) + 3 z^3(2-3z)^2 + (2-3z)^3
    = z^9 + (6z^6-9z^7) + (12z^3-36z^4+27z^5) + (8-36z+54z^2-27z^3)
    = z^9 - 9z^7 + 6z^6 + 27z^5 - 36z^4 - 15z^3 + 54z^2 - 36z + 8.
```

No `z^8` term: `K` has no `z^2` term.

**KQ.**

```text
(z^3-3z+2)(q1 z+q0) = q1 z^4 + q0 z^3 - 3 q1 z^2 + (2 q1 - 3 q0) z + 2 q0.
```

**Nine images** of `(a0,...,a7,k)`, lowest degree first, matching `independent_reconstruct.py` names and the compiler's `coefficient_images()` / `COEFFICIENT_REES_STRINGS`:

| atom | polynomial | Rees-scaled compact form |
|---|---|---|
| `a0` | `8+2 q0+r0` | `8+2 s^22 q0+s^30 r0` |
| `a1` | `-36-3 q0+2 q1+r1` | `-36+s^22(-3 q0+2 q1)+s^30 r1` |
| `a2` | `54-3 q1+r2` | `54-3 s^22 q1+s^30 r2` |
| `a3` | `-15+q0` | `-15+s^22 q0` |
| `a4` | `-36+q1` | `-36+s^22 q1` |
| `a5` | `27` | `27` |
| `a6` | `6` | `6` |
| `a7` | `-9` | `-9` |
| `k` | `0` | `0` |

These are identical, as polynomials, to the nine compiler images. No `q2` monomial occurs. The ninth image is empty, so this is the constant-load slice `k=0`. Coordinates `a` and `h` do not appear: the cubic is the frozen double-root polynomial, not a moving axis. That is `a=1`, `h=0`.

**Loads and D1 targets.** The charged source defines `tails[ell]=-[w^{-ell}] g(z(w))` on `(a0,...,a7,k)`, so the finite equations are `r_ell(f,0)=Lambda^{12+ell} gamma_ell` with the standard D1 loads

```text
gamma_3=mu,   gamma_6=nu,   gamma_8=1+tau,
gamma_ell=0 otherwise.
```

The support mask freezes `mu=2/3` and `nu=0`. Therefore the only nonzero targets are

```text
row 3:  (2/3) Lambda^15,
row 8:  Lambda^20 (1+tau),
```

and row 6 is not a missed target: `nu=0` makes `Lambda^{18} nu=0`. After the Rees map `v(Lambda)=4`, `v(tau)=1` these become `(2/3) s^{60} la^{15}` and `s^{80} la^{20}(1+s tau)`, which is what encoding A subtracts and what encoding B writes as the two leading terms of `E3` and `E8`. Sign convention: charged row = raw tail minus target. The Newton v2 correction review, re-hashed to `ec9fe740…`, already recorded the full-source replay vector `(0,0,2/3,0,0,0,0,0)` at `t^{60}=Lambda^{15}` on this jet; a flipped sign would have produced `-2/3`.

**Toric relation.** `Lambda=tau^3 rho` is homogeneous of weight `4`. Encoding A writes `s^4 (la-tau^3 rho)`; encoding B writes `s^4 la - s^4 tau^3 rho`. Same generator.

---

## Charge 2 — support mask, weight, residue, and `-t^{38}/2`

**CONFIRMED**

Support mask, identically zero as ring coordinates: `a-1`, `h`, `q2`, `k`, `nu`. Remaining finite-ring coordinates `(Lambda,tau,rho,q1,q0,r2,r1,r0)` with weight vector

```text
(4, 1, 1, 22, 22, 30, 30, 30).
```

This is the ramification of normalized `(alpha,beta)=(15/2,11/2)` along the already certified strict chart `Lambda=t^4`, `tau=t`, `rho=t`:

```text
4 · (11/2) = 22,     4 · (15/2) = 30,     4 · (15-11/2) = 38.
```

The window `5<beta<6` contains `11/2`. The jet displayed in the Newton v2 review is

```text
Q = t^{22} L = t^{22}(z-1),
R = t^{30} N - t^{38}/2 = t^{30}(z-1)(z+2) - t^{38}/2,
```

so the leading coefficients are

```text
(q1,q0)=(1,-1),     (r2,r1,r0)=(1,1,-2),     (Lambda,tau,rho)=(1,1,1).
```

That is the residue `(1,1,1,1,-1,1,1,-2)`. The correction `-t^{38}/2` is a constant in `z`, hence a later coefficient of the same coordinate `r0`, of relative valuation `8`. It is not a ninth finite-ring variable, not a `q2` direction, and not a moving-axis parameter. Exact Rees closure in the eight-variable ring is precisely the question whether some higher terms of these same eight coordinates exist.

The compiler reports minimum weights `52` on rows `1,2,3,4,5,7,8`, `60` on row `6`, and `4` on the relation. Row 6 of the emitted B polynomial has `s`-powers `{60,66,74}` and no `s^{52}`; the recorded `60` is therefore the minimum, not the maximum. That is direct evidence against weight reversal, read from emitted text, without rerunning the compiler.

---

## Charge 3 — sparse substitution, targets, generator-initial check, encodings, identities, loads

**CONFIRMED**

**Sparse substitution.** The compiler loads the charged source at the pinned SHA-256, refuses a names mismatch with `(a0,...,a7,k)`, refuses a tails-key mismatch with `{1,...,8}`, builds a power table of the nine unscaled images, and substitutes every source monomial by table lookup. Encoding A never expands those tails: it writes the same source monomials on the Rees-scaled compact images. Encoding B expands `tails(a(q,r))-target` in the eight finite variables, then attaches `s^{w(m)}` to each monomial `m`. These are the same Rees map: if `F(X)=Φ(a(X))`, then `Φ(a(s^w X))=F(s^w X)=∑ c_α s^{w·α} X^α`.

**Target subtraction** is applied after substitution, and only on rows 3 and 8, with the scaled monomials of Charge 1. The common-cubic sanity check is on the raw substituted rows, before targets, and demands that the `(q,r)`-free part vanish. That is `r_ell(K^3,0)=0`, the correct vanishing of ordinary tails of the unperturbed cubic. It passed on AWS: the compiler would otherwise have raised `common cubic did not vanish` and would not have printed `PASS_D1_DOUBLE_ROOT_CONTROL2_REES_V2_COMPILER`.

**Minimum-weight generator check.** `initial_data` takes the *minimum* of `∑ w_i α_i`, evaluates that initial form at the residue, and fails the compile if the value is nonzero. The r6d compiler payload records `residue_value=0` on all nine generators, with initial supports `2,3,4,5,5,5,5,5,2`. Direct evaluation of the emitted B polynomials at the residue, using only the lowest `s`-power of each:

| gen | lowest `s`-piece | value at residue |
|---|---|---|
| `E1` | `(4/9)(q1 r1+q0 r2)` | `(4/9)(1-1)=0` |
| `E2` | `(4/3)q1 r2+(4/9)q1 r0+(4/9)q0 r1` | `4/3-8/9-4/9=0` |
| `E3` | `(-8/9)q1 r2+(8/9)q1 r1+(8/9)q0 r2+(4/9)q0 r0` | `-8/9+8/9-8/9+8/9=0` |
| `E4` | `(4/3)q1 r2-(16/27)q1 r1+(4/9)q1 r0-(16/27)q0 r2+(4/9)q0 r1` | `4/3-16/27-8/9+16/27-4/9=0` |
| `E5` | `(-8/9)q1 r2+(4/9)q1 r1-(8/27)q1 r0+(4/9)q0 r2-(8/27)q0 r1` | `-8/9+4/9+16/27-4/9+8/27=0` |
| `E6` | `(4/3)r2^2-(8/9)r2 r1+(8/9)r2 r0+(4/9)r1^2+(2/9)r0^2` | `4/3-8/9-16/9+4/9+8/9=0` |
| `E7` | `(8/9)q1 r2-(40/81)q1 r1+(8/27)q1 r0-(40/81)q0 r2+(8/27)q0 r1` | `8/9-40/81-16/27+40/81-8/27=0` |
| `E8` | `(-28/27)q1 r2+(16/27)q1 r1-(28/81)q1 r0+(16/27)q0 r2-(28/81)q0 r1` | `-28/27+16/27+56/81-16/27+28/81=0` |
| `LT` | `la-tau^3 rho` | `1-1=0` |

Supports match the payload. This check is the tropical *prevariety* of the submitted generators. It is not the result; the solver is.

**Encoding A** (source inspected; result not inferred): factored images, `sat(-,s)` contraction, global `dp` on `(s,la,...,r0)`, then principal saturation by the eight-fold product. Rational targets are parenthesized `(2/3)`, so the predecessor `q^2/3` parse failure is not present.

**Encoding B** (source and r6d input inspected): independently expanded, inverse `u s-1`, product order `(lp(3),dp(8))` on `(u,v,s,la,...,r0)`. The first block is exactly the two inverses and the Rees parameter. Both encodings include the same nine generators plus the chosen contraction device.

**Normalized dual-host compile identities.** `COMPILE_CUSTODY.md` records both compilers at rc zero, empty compiler stderr, the unique v2 compiler PASS marker, identical nine generator-initial records, and, after replacing only the embedded job tag,

```text
8775a4831d1dab28974b93ceee9e24294f5cce864eb0ef32d12b1cb078b8268c  A.normalized
3475b11f23a9e2508181c7cb7fe4e7a868c86428ebe526e7f5db0fedf49698dc  B.normalized
```

Locally, the r6d raw hashes match the files that are actually present: B input `c905f1b5…`, r6d payload `0dcd183b…`, A compiled hash claimed as `2b416cb8…`. Box02 compiled files are not in this package, so the normalized cross-host identity is a custody claim that was not recomputed here. That is not a source-equation defect. No solver verdict is encoded in `COMPILE_CUSTODY.md`.

**Fixed-load semantics.** `k`, `mu`, `nu` are not ring variables. `mu=2/3` is a numeric coefficient of the row-3 target. `nu=0` deletes the row-6 target. `tau` in `gamma_8=1+tau` is the chart coordinate, not a load. There is no hidden permission to vary loads, `q2`, `a`, or `h`.

---

## Charge 4 — contraction from `s!=0`, and full initial degeneration

**CONFIRMED. The claim is proved, not rejected.**

Let `R=Q[X]` with `X=(la,tau,rho,q1,q0,r2,r1,r0)`, and let `I⊂R` be the ideal generated by the eight specialized rows minus targets together with `la-tau^3 rho`. Let `φ_s:R→Q[s,X]` be the graded substitution `X_i ↦ s^{w_i} X_i`. This is a ring homomorphism, so `φ_s(I)=⟨φ_s(g_i)⟩` is generated by the images of the submitted generators.

**Contraction.** The localization of `φ_s(I)` at `{s^N}` intersected back into `Q[s,X]` is

```text
C = φ_s(I) : s^∞ = { g ∈ Q[s,X] : s^N g ∈ φ_s(I) for some N }.
```

Singular `sat(φ_s(I), ⟨s⟩)` is that colon. Independently, the Rabinowitsch extension `⟨φ_s(g_i), u s-1⟩ ⊂ Q[u,s,X]` satisfies

```text
⟨φ_s(g_i), u s-1⟩ ∩ Q[s,X] = φ_s(I) : s^∞,
```

which is encoding B's `eliminate(-,u)`. The two devices compute the same contraction `C`. The synthetic controls check exactly this: `⟨s⟩:s^∞=(1)`, and `⟨s(q1-1)⟩:s^∞=⟨q1-1⟩`. Both passed on r6d B.

**Special fibre.** `H=C+(s)`. If `f∈I` has lowest weight `d`, then `φ_s(f)=s^d in_w(f)+s^{d+1}(⋯)`, so `in_w(f)+s·(⋯)∈C` and `in_w(f)∈H`. Conversely, any element of `C` is killed by a power of `s` into `φ_s(I)`; the lowest `s`-piece of that identity is a `Q[X]`-linear combination of initial forms of elements of `I`. Thus `H∩Q[X]`, equivalently the image of `H` in `Q[s,X]/(s)≅Q[X]`, is the initial ideal `in_w(I)`.

**S-polynomials.** `in_w(I)` is generated by `in_w(f)` for every `f∈I`, not by `{in_w(g_i)}` of a presented generating set. The contraction is an ideal operation on `φ_s(I)`: a Gröbner basis of `φ_s(I)` after inverting `s` includes every S-polynomial consequence. Setting `s=0` therefore sees those consequences. The compiler's generator-initial vanishing is strictly weaker, and the code does not treat it as the answer.

---

## Charge 5 — torus localization, B blocks, `GHT[1]=1`

**CONFIRMED for encoding B as a one-host computation. Encoding A is not a result.**

**A, source only.** After `H=C+(s)`, encoding A saturates the principal ideal `⟨la·tau·rho·q1·q0·r2·r1·r0⟩`. For a single polynomial `f`, `I:f^∞=I:⟨f⟩^∞`. Saturating by the product removes every primary component contained in `V(product)=⋃ V(X_i)`, which is localization to the torus `{all eight coordinates nonzero}`. That is the correct principal saturation. Its numerical output is not inferred.

**B, source and r6d output.** After the same `H`, encoding B forms `⟨H, v·TORUS-1⟩` and eliminates `v`. That is the independent Rabinowitsch inverse of the same product. The ring is

```text
R=0,(u,v,s,la,tau,rho,q1,q0,r2,r1,r0),(lp(3),dp(8)).
```

The first lex block is `(u,v,s)`; the second is `dp` on the eight finite coordinates. This is an elimination order for `u` (largest variable) and for `{u,v}` jointly. Singular `eliminate` additionally builds its own elimination order, so the second elimination of `v` does not depend on `u` remaining lex-larger than `v`. The variable `v` is idle during the first Gröbner basis of `J=⟨E1..E8,LT,u s-1⟩`. That is ring hygiene, not a change of ideal: `v` does not appear in those generators, and it is introduced only in `v·TORUS-1`. Both eliminations are well-formed. The synthetic inverse-elimination controls passed.

Emitted B:

```text
B_CONTRACTION_GENERATORS=403
B_SPECIAL_FIBRE_GENERATORS=35
B_TORUS_SPECIAL_FIBRE_GENERATORS=1
TORUS_SPECIAL_FIBRE_IS_UNIT=1
GHT[1]=1
RESIDUE_IDEAL_IS_UNIT=1
CONTROL2_REES_RESIDUE_SURVIVES=0
```

With `option(redSB)`, a unit ideal has reduced basis `{1}`. `GHT[1]=1` together with `size(GHT)=1` and `reduce(1,GHT)==0` is therefore `Htor=(1)` in this encoding.

**Does that empty the stated stratum?** On the open torus of this frozen-axis, fixed-load, fixed-weight special fibre, yes: `Htor=(1)` means `V(H)∩(G_m)^8=∅`. Every residue with all eight coordinates nonzero is absent, including the displayed one. It does *not* empty the coordinate-hyperplane loci of `H`, other weights, moving axis, `q2!=0`, other loads, the rest of the fan, D1, or JC2. Dual confirmation with encoding A is still required before that torus-emptiness is a theorem.

---

## Charge 6 — residue annihilates generator initials, yet the full torus initial ideal is unit

**CONFIRMED, and consistent.**

Charge 2 and Charge 3 show that the displayed residue lies on every tropical hypersurface `in_w(g_i)=0` of the submitted generators. That is prevariety membership.

It is not tropical membership. Tropical membership of `w` for the ideal `I` is the condition that `in_w(I)` contain no monomial, equivalently that `in_w(I)` meet the torus emptily, equivalently that `sat(in_w(I), product)≠(1)`. That is exactly `TORUS_SPECIAL_FIBRE_IS_UNIT=0`. Encoding B printed the opposite.

A polynomial consequence can have a monomial initial form even when every presented generator has a binomial (or otherwise non-monomial) initial form that vanishes at the residue. Concretely: the weight-52 pieces of `E1,...,E8` vanish at the residue, but they are not the whole of those polynomials. The weight-60 piece of submitted `E3`, evaluated at the same residue, is

```text
(-2/3) la^{15} + (4/9) r2 r1  ↦  -2/3 + 4/9 = -2/9 ≠ 0.
```

That leftover is *higher* than `in_w(E3)`, so it does not disturb the generator-initial check. An S-polynomial (or other combination) that cancels the weight-52 layer can promote such a higher piece, or a combination of several rows, to a lowest-weight monomial. The contraction is designed to see that monomial; torus saturation then yields `(1)`.

The code path is:

1. compiler: residue misses a generator initial → compile failure (negative control that the residue is on the prevariety);
2. solver: contraction, then torus saturation, then `Htor + m_residue`;
3. `CONTROL2_REES_RESIDUE_SURVIVES` is set from the latter, never from the former.

No assignment equates prevariety membership with tropical membership. The printed firewall string does not say otherwise.

The same distinction explains why a finite jet through `t^{60}` can match the D1 targets while the exact eight-variable ideal still has empty torus initial fibre: the Newton successor is a truncated coefficient identity in a series; the Rees computation asks whether some arc in this finite ring has the displayed leading weight and torus residue.

---

## Charge 7 — exact result semantics

**CONFIRMED, with the dual-endpoint firewall enforced.**

Definitions, as implemented:

- `RESIDUE_IDEAL_IS_UNIT=1` / `CONTROL2_REES_RESIDUE_SURVIVES=0` means `Htor + m_residue = (1)`, where `m_residue=⟨la-1,tau-1,rho-1,q1-1,q0+1,r2-1,r1-1,r0+2⟩`. This residue, on this support, weight, and load, has no point in the torus-localized special fibre, hence no lift with that exact leading residue.
- `TORUS_SPECIAL_FIBRE_IS_UNIT=1` means `Htor=(1)`. This is strictly stronger: the whole torus is empty, so every nonzero residue of this weight/support is excluded, not only the displayed one. For a torus point the weaker flag is implied.

A dual clean unit (both encodings, compared bases, both `Htor=(1)`) would exclude the entire open torus of this frozen-axis, fixed-load, fixed-weight degeneration. It would still exclude nothing else:

- moving axis (`a,h` unfrozen);
- `q2≠0`;
- other weights, including the same ray with some coordinate of strictly higher valuation (residue `0` on that coordinate, i.e. the axes of this torus);
- other residues on those axes;
- other loads `(k,mu,nu)`;
- the rest of the double-root Newton fan;
- D1 as a global statement;
- JC2.

The converse language in the preregistration (`SURVIVES=1` plus algebraic curve selection / valuative criterion after finite ramification) is the other branch. It is not invoked by the B stream. It is the standard char-0 reading of a closed point on the special fibre of the closure, firewalled to this support, and explicitly not a polynomial Keller counterexample. B's emitted verdict is the unit branch.

Compiler prose “dual units exclude only that datum” is a correct *upper bound* on what `RESIDUE_SURVIVES=0` may be used to say. The stronger torus-unit flag is printed separately and must be read as Charge 5, not collapsed into “only the displayed residue.” Encoding A is live, so neither flag is a dual theorem.

---

## Charge 8 — v2 custody and v1 quarantine

**CONFIRMED**

**Timing.** V2 worker runs `/usr/bin/time -v -o singular.time /usr/bin/Singular …`, so CAS stderr is not used for telemetry. The r6d `singular.time` is `/usr/bin/time -v` output: wall `0:05.21`, user `5.20`, max RSS `32340` kB, `Exit status: 0`, command `Singular -q compiled/control2_rees_v2_B_expanded_inverse_lpdp.sing`. Hash `de1189f3…` matches `result.sha256`.

**CAS stderr.** `singular.stderr` is empty (0 bytes, SHA-256 `e3b0c442…`). `compiler.stderr` is likewise empty. The worker requires both.

**Source hashes before compile and before solve.** The worker will not compile without `sha256sum -c compile_source.sha256`, and will not solve without `sha256sum -c solve_source.sha256`. Those check files were not copied into the local `aws_r6d_B/` tree. The worker writes `PASS_REMOTE_WORKER` only after both checks and both fail-closed validations, and that line is present. Compiler rc `0`, solver rc `0`.

**Fail-closed gates.** Compile fails on nonzero rc, nonempty compiler stderr, or a PASS-marker count other than 1. Solve fails on nonzero rc, nonempty `singular.stderr`, PASS-marker count other than 1, any of the three `[01]` flags missing or duplicated, or any `FAIL_` line. Caps: compiler `64 GiB / 3600 s`, solver `256 GiB / 21600 s` (`memory_kib=268435456`), nice 10, AWS/Linux/tag refusals, v2-only tag prefix. r6d metadata records `WAITING_COMPILE` then `WAITING_SOLVE` then `PASS_REMOTE_WORKER`, matching the GO-sentinel contract. Unique markers:

```text
PASS_B_SYNTHETIC_CONTROLS
PASS_D1_DOUBLE_ROOT_CONTROL2_REES_V2_COMPILER
PASS_D1_DOUBLE_ROOT_CONTROL2_REES_V2_B
```

No `FAIL_`, no duplicate `[01]` lines, no resource kill.

**V1 quarantine.** V1 directed `/usr/bin/time -v` into `singular.stderr` while requiring that file empty. `SOFTWARE_CONTROL.md` states that every completed v1 solve therefore failed its own custody contract; Box02 A was stopped; r6d B's underlying Singular rc `0` still produced wrapper `SOLVE_FAILED`. Those streams are not evidence for lift or no lift. V1 tags overlap the v2 prefix as strings, but v2's worker accepts only `…_rees_v2_*` and compiles `compile_control2_rees_v2.py`. V1 cannot support a mathematical endpoint.

Local artifact gap, non-blocking: r6d `aws_r6d_B/` contains the B input and all solver/compiler streams listed in `result.sha256` except the compiled A `.sing` file whose hash is recorded there as `2b416cb8…`. Encoding A may still be live; that file is not needed to audit B.

---

## Charge 9 — directed defect search

**No defect found that reverses the v2 source or the r6d B custody.**

| hunted defect | finding |
|---|---|
| Minimum/maximum weight reversal | `initial_data` uses `min`. Row 6 of emitted B has `s`-powers `{60,66,74}` and is recorded as minimum `60`. Initial forms used for the residue check are the lowest `s`-pieces. Not reversed |
| Missed target coefficient | Rows 3 and 8 carry the only nonzero D1 targets at these loads. Row 6's `Lambda^{18} nu` is zero because `nu=0`. Other `gamma_ell` are zero. Both encodings subtract the same scaled targets |
| Inadequate saturation | Contraction saturates by `s` or inverts `s`. Special fibre then saturates by the *product of all eight* nonzero residue coordinates, or inverts that product. This is torus localization, not saturation only by `s` and not saturation only by a proper subproduct |
| Hidden load variation | `k,mu,nu,a,h,q2` are not variables. Numeric `mu=2/3` is the row-3 coefficient. No path in the compiler introduces a load or `q2` monomial |
| Malformed Singular ideal/elimination | Nine generators plus `u s-1`, then `v·TORUS-1`. `elim.lib` is loaded. Product order matches the two inverses and `s`. `eliminate(u)` then `eliminate(v)` are the two Rabinowitsch steps. Residue equations are `q0+1` and `r0+2`, i.e. `q0=-1`, `r0=-2`. Parenthesized rationals. Synthetic controls passed |
| Overstrong curve-selection language | Present only on the `SURVIVES=1` branch, already firewalled to this support and to a formal point of the coefficient ideal. The B stream is the unit branch and does not claim an arc. Firewall string is printed |

Non-blocking notes, not repairs: (i) `v` is idle in B's first Gröbner basis; (ii) Box02 compiled files and the r6d compiled A `.sing` are not in the local package; (iii) compiler prose “dual units exclude only that datum” is weaker than torus-unit, which is printed as its own flag; (iv) encoding A is live.

---

## Sharpest non-claim

One-encoding, one-host, one-order emptiness of the torus special fibre of this frozen-axis, fixed-load, weight-`(4,1,1,22,22,30,30,30)` degeneration of the exact eight-row D1 coefficient ideal. Not dual-encoding emptiness. Not emptiness of the axes. Not a statement about any other ray, residue, load, or chart. Not a classification of the double-root fan. Not a formal D1 trajectory. Not JC2. The already certified control-2 finite successor through `t^{60}` remains a truncated identity; B says that this leading torus residue is not a point of the exact initial degeneration.

---

## Evidence layers (do not collapse)

1. Hand algebra of `K^3+KQ+R` and of the ramified control-2 jet, against the compiler images, targets, relation, mask, weights, and residue.
2. Hand evaluation of every emitted B generator-initial at the residue.
3. Algebra of contraction, Rabinowitsch, initial ideals, and torus saturation, against both encodings' source text.
4. SHA-256 of the freeze chain, charged source, r6d B streams, and the Newton v2 correction review.
5. Inspection of v1 `SOFTWARE_CONTROL.md` and the v1 worker's `/usr/bin/time` redirection, as a negative custody control.

Encoding A is not among these layers.

REES_V2_CONFIRMED
