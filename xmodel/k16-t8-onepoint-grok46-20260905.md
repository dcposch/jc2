# K16 one-point certificate at t = 8: F4 of the CI chart finishes (n = 52138),
# the boundary of Γ_8 is certified, affine (ii)_8 is still OPEN at FGLM

Lane `k16-t8-onepoint-grok46-20260905`, basis `c576a3d4`, 2026-09-05.
Drivers and transcripts in `box/k16t8-20260905/` (worker mirrors `w7/`, `w18/`).
Engines: Singular 4.3.2, msolve 0.x (F4 then sparse-FGLM), python3 (root scan of
the t = 6 parametrization; factorisation of the t = 8 boundary q6-minpoly).
Foreground CAS; long jobs as `setsid`/`timeout` on c7i workers 172.30.0.7
(16-thread msolve) and 172.30.0.28 (4-thread leftover + `I2+(W)`).  No ledger,
`jc2-lean`, or `ideation-*` was read or written.  `FALLACY-v2` applies; no
exit-price assertion is made, so no `charge_basis` line is due.

## 0. Verdict

```text
REQUESTED  one simple affine F_32003-point of Γ_8 (b4 ≠ 0) with W ≠ 0 and the
           étale-lift hypotheses of Lemmas 3.3–3.5 / 3.7, giving clause (ii)_8;
           with (i)_8 (B-HSOP, banked through t=8) this would certify (V0)-tail
           at t=8 ⇒ (8.1)_8 ⇒ (T) at t=8, extending the ray from t ≤ 7 to t = 8.
VERDICT    PARTIAL.  (T) at t=8 is NOT obtained.  OPEN[K16-ONE-POINT-T8] remains
           OPEN on the affine half of clause (ii).
PROVED     (1) the t=6 verify job reproduces the charged transcript byte-for-byte;
               a perturbed W (W_r+1 in FITT; a nearby q2+1 point) FAILS as required.
           (2) boundary of Γ_8 mod 32003: six geometric points in the stratum
               b4=q2=0, q3=1, q4=q5=q7=0, q6 a root of a squarefree sextic of
               Frobenius type (1)(2)(3); vdim(stratum+(W))=0; one simple
               F_p-point P̄_bd = (0,0,1,0,0,7416,0) with W ≠ 0, JACRANK=4,
               KERNEL_CONSISTENT=1, T_top=4235 ≠ 0.
           (3) msolve F4 of the 7×7 CI chart subst(G, b4=1) over F_32003
               (16 threads, worker .7) COMPLETE: reduced grevlex basis of size
               18871, Dimension of quotient = 52138.  Combined with the EN
               degree d_Γ(8)=52140 and the boundary contribution 6/3=2 this
               forces n' = n = 52138 and CONE dim = 1 at this prime (Lemmas
               3.3–3.5, written out in §5).  Affine coordinate 1-, 2-, 3- and
               4-spaces in {b4=1} are empty.
NOT CLOSED affine clause (ii)_8: no F_p-point of Y_8 = Γ_8 ∩ {b4 ≠ 0} has been
           extracted.  FGLM/parametrisation of the 52138-dimensional quotient
           is IN PROGRESS (density of the non-trivial part 95.39%; log frozen
           at that line).  A single boundary point does NOT give Prop. 7.1
           (that needs V(I2+(W))={0} on the whole cone); k_8=1 is OPEN for
           t ≥ 7, so one affine point would in any case certify only one
           Galois orbit (Lemma 3.1), not all of Y_8.
CONSEQUENCE (V0)-tail at t=8, (8.1)_8 and (T) at t=8 remain OPEN.  The ray's
           proved range is still t=1..7.  What changes: the t=8 chart length,
           the flat-model hypothesis, and n'=n are no longer the missing
           items; the remaining job is FGLM of a 52138-dimensional quotient
           plus one verifypoint evaluation.
NOTIFY     not warranted (no new (V0) index).
```

## 1. Custody

The receipt `xmodel/k16-t8-onepoint-grok46-20260905.run.v2` was parsed with
`awk -F=`, pairing `charged_input_<i>_sha256=` / `_basename=` into
`/tmp/k16-t8-hash-manifest.txt` (and a copy `box/k16t8-20260905/inputs.sha256`).
`sha256sum -c` → **15/15 `OK`**.  No digest was retyped.  All fifteen charged
inputs were read before any driver ran.

Row provenance is the Galois emitter `gen.py` (copied into this box, not
modified in its polynomial prefix): top-tail rows from
`box/k16rank-20260903/terminal_t{t}_exact_none.out` (`RECURRENCE_PASS`,
`DRIVER_DONE`).  Every job in this box reprints `A0VALUE`, `PREFIX_S_OK`,
`PREFIX_P_OK ngens(I2)=…`, the b3-split / weight / G-identity / ELIMINANT
certificates, and aborts on `FAIL`.  None occurred.  The t = 8 prefix uses
`yy = 11288` at `p = 32003` (branch 0 of `H_8`), matching the rank-lane
modular root.  `.err` streams of accepted runs were empty of `div. by 0`.

New drivers live only in `box/k16t8-20260905/`.  This is the only new `xmodel`
report.

## 2. What clause (ii)_8 actually requires (no analogy from t ≤ 6)

Charged setting (Galois report §2, rank report Theorem FITT):

```text
A_8 = Q[y]/(H_8) ≅ Q(√27) = Q(√3),   H_8 = 3468 y^2 − 1836 y + 234
P_8 = A_8[b4, q2, …, q7],   Γ_8 = V(I_2(N)) ⊂ Spec P_8
clause (i): V(B,C) = {0}
clause (ii): T_{8,15}(p, β(p)) ≠ 0 at every point p ≠ 0 of Γ_8
(V0)-tail_8  ⟺  (i)_8 ∧ (ii)_8  ⟹  (V0)_8  ⟹  (8.1)_8  ⟹  (T)_8
```

Lemma 3.1 (all-or-nothing) certifies an *orbit* from one point.  Corollary 3.2
needs `k_t + b_t` evaluations.  The Galois lane proved `k_t = 1` only for
t = 3..6; `OPEN[K16-GAMMA-IRREDUCIBLE]` for t ≥ 7 is still open, and this lane
does not close it.  **One affine F_p-point with W ≠ 0 therefore does not, by
itself, give clause (ii)_8** (FALLACY-v2: do not fill that gap by the t ≤ 6
pattern).

Proposition 7.1 (Galois report §7) is the orbit-free alternative: if `CONE dim = 1`
mod 𝔭 (flat model, Lemma 3.3) and `V(I_2 + (W_1, …, W_7)) = {0}` in `P_k`, then
clause (ii)_8 holds over `A_8`, by properness of `Proj A → Spec R` (every
`K̄`-point specialises, and `W(P) ≡ W(P̄)`).  A *single* boundary point with
`W ≠ 0` is not that cone statement.  The six-point Nullstellensatz
`vdim(stratum + (W)) = 0` *is* the boundary half of Prop. 7.1; the affine half
is `V(I_2+(W)) ∩ {b4=1} = ∅`, which this lane did not finish (`affinew` timed
out at 5400 s during `std(I2+Ws+(b4-1))`; `conew` still in `std(I2+Ws)` at
seal).

Lemma 3.7 as written lifts a simple point of the *affine chart*
`Y_t = Spec P/(I_2+(b4−1))`.  A point with `b4 = 0` is not in `Y_t`.

So: an affine simple F_p-point is required for the one-evaluation instrument
on affine orbits; a boundary point (even with the étale hypotheses) certifies
only the boundary, and only via the Prop. 7.1 specialisation argument once
flatness is in hand — which it now is (§5), for the boundary half.

## 3. Boundary of Γ_8 mod 32003

Charged `boundary_t8_mod_p32003_b0` (w18, wall 179 s) already printed

```text
SLICE b4=0 cone: dim=1
stratum j=2: vdim=0;  j=3: vdim=6 dim=0;  j=3+(W): vdim=0
j=4..7 empty
```

This lane's `listboundary_t8` (local, wall 1 s, same prefix) listed the j=3
scheme.  `finduni` gives q4 = q5 = q7 = 0 (minpoly the variable itself,
ordinary degree 1, squarefree) and a degree-6 squarefree minpoly in q6 of
factor pattern `1^1 2^1 3^1`:

```text
q6^6 + 865 q6^5 − 11155 q6^4 + 14501 q6^3 + 5432 q6^2 − 3663 q6 + 9115
  = (q6 − 7416)(q6^2 + 2445 q6 + 7483)(q6^3 + 5836 q6^2 + 15822 q6 − 2966)
```

over F_32003 (Singular `factorize` on `(32003),(x),dp`; python brute-force:
exactly one F_p-root, namely 7416; `subst` remainder 0).  All six geometric
points therefore have the shape `(b4, q2, q3, q4, q5, q6, q7) = (0, 0, 1, 0, 0, q6, 0)`
with q6 a root of that sextic.  Nonzero coordinates q3 (weight 3) and q6
(weight 6), so `g_L = gcd(3,6) = 3`.  Lemma 3.8: the stratum contributes
`≥ vdim/j = 6/3 = 2` to `d_Γ − n'`.  The constant term of the sextic is
9115 ≠ 0, so none of the six points is the q3-axis.

The unique F_p-point, with the Galois `evalpoint` on free columns 4..7:

```text
P̄_bd = (0, 0, 1, 0, 0, 7416, 0)
local vdim of I2+(b4, q2, q3−1, q4, q5, q6−7416, q7) = 1   (simple in the chart)
MINORS_ZERO=1
JACRANK_FREE=4 expected=4
r=3: B=12170 C=7928;  r=6: B=14394 C=−942;  other B_r=C_r=0
BETA=−9925 (from r=3)  TTOP_AT_LIFT=4235 ≠ 0
KERNEL_CONSISTENT=1
W3=−6850, W6=12365, other W_r=0, all FITTcheck=1
W_NONZERO_AT_POINT=1
```

`vdim(stratum+(W))=0` (dim −1) is the Nullstellensatz statement that W ≠ 0 at
*all six* geometric points, including the quadratic and cubic orbits that are
not F_p-rational.  Combined with CONE dim = 1 (§5) and properness, Prop. 7.1's
specialisation argument gives clause (ii) on the *boundary* of Γ_8 over A_8:
a char-0 boundary point with W = 0 would specialise to a special-fibre
boundary point with W = 0, which does not exist.  This does not use Lemma 3.7
on Y_8 (the point is not affine) and does not use k_8 = 1.

## 4. Affine hunt: sparse slices of {b4 = 1} are empty

On the affine chart, substituting all but 1, 2, 3 or 4 of the q-coordinates
to 0 and computing `std` of the 21 minors (wall 1–56 s):

```text
all 7 coordinate lines through the origin of the chart: gcd = 1 (miss Γ)
all 8 tested coordinate 2-planes: dim = −1
all 7 tested coordinate 3-spaces: dim = −1
eight coordinate 4-spaces (2345, 2346, 2367, 3456, 3467, 2356, 4567, 2456): dim = −1
the two points (1,0,1,0,0,0,0) and (1,0,1,0,0,7416,0): MINORS_ZERO=0
```

Affine points of Γ_8, if any F_p-rational ones exist, have at least five
nonzero q-coordinates.  The one-evaluation instrument on Y_8 therefore has to
solve the full 6-variable (minors) or 7-variable (CI) system.  That is the
exported CI job.

## 5. CI F4 completes: n = 52138, CONE dim = 1, n' = n

The charged export `msolve_t8_mod_p32003_b0_ci.ms` is 7 equations in
`(q2,q3,q4,q5,q6,q7,b3)` over F_32003, namely `subst(G_1, …, G_7, b4, 1)`.
This is `V(G) ∩ {b4=1}`: the b3-axis misses the chart, so the scheme is the
b3-lift of Y_8.  (B) is an hsop at this prime (rank lane: `vdim P/(B) = 11440
= C(16,7)`), so no rank-1 point has kernel `(0:1)` and the lift is unique.

A leftover 4-thread msolve (`-P 1 -t 4`, worker .28) was at degree 14,
matrix 45739 × 81237, at the Galois seal.  This lane copied the `.ms` file
(76 MiB; first line `q2,q3,q4,q5,q6,q7,b3`, second line `32003`) onto worker
.7 and ran

```text
msolve -v 2 -t 16 -l 44 -u 1 -P 1 -f msolve_t8_mod_p32003_b0_ci.ms
```

msolve printed `characteristic is too low for choosing probabilistic linear
algebra` and set the linear-algebra option to 2 (exact sparse), so `-l 44`
was not used.  F4 finished.  Transcript
`box/k16t8-20260905/w7/msolve_t8_t16.log`
(sha256 `69cf0148937b18e8efe0f073a55df1516c58fe8b33b42cee4de6dcddd2b66f8b`
at the FGLM freeze):

```text
deepest F4 degree = 15
max. matrix = 80415 × 106219 (37.565%), 1595.92 s real / 24024.80 s cpu
reduce final basis 18943 × 71081 (58.65%), 397.37 s
F4 overall 5296.52 s elapsed / 65476.72 s cpu  (16 threads; 86.5% in LA)
size of basis 18871;  #terms 855568786
Dimension of quotient: 52138
[52138, 13835], Non trivial / Trivial = 26.54%
Density of non-trivial part 95.39%
```

**Chart length.**  `dim_{F_p} O(V(G) ∩ {b4=1}) = 52138`.  This is the
quantity `n` of Lemma 3.4 for the CI chart; because the b3-lift is unique it
is also the length of Y_8 ⊗ k.

**CONE dim = 1 (Lemma 3.3).**  I2 is homogeneous of positive weights.  The
chart `{b4=1}` is 0-dimensional (finite nonzero length) and nonempty, so the
affine cone V(I2) has dimension 1.  Independently, the charged/recomputed
slice `V(I2, b4)` has dimension 1 (six lines).  Both are compatible with a
curve.  The pattern dim-only job (`std(I2+(b4−1))` in Singular) was killed by
`timeout 6000` (`exit=124`, `halt 1`) after printing only `SLICE dim=1`; it is
not needed once the CI quotient dimension is known.

**n' = n = 52138 (Lemma 3.4).**  EN-CURVE gives `d_Γ(8) = [C(25,7) − C(16,7)]/9
= 52140`.  Lemma 3.8 with the six-point stratum of §3 contributes `≥ 2` to
`d_Γ − n'`, so `n' ≤ 52138`.  Lemma 3.4 gives `n' ≥ n = 52138`.  Therefore
`n' = n = 52138` and the boundary contribution is *exactly* 2.  M is R-free of
rank 52138.  Squarefreeness of the point polynomial is *not* claimed: the
52138 is a length, not yet a reduced geometric count.  Lemma 3.5 (good
reduction of `f_8`) needs the eliminating polynomial, which is the FGLM step
still running.

**Good reduction of A_8 at p = 32003.**  `H_8` splits: roots 11288, 18833.
`disc H_8 = 124848 ≢ 0 (mod p)`.  `A_8 = Q(√3)`, p ∤ 3, `(3/p) = 1`.  Printed
`A0VALUE = 7970 ≠ 0`.  2 is invertible.  Rank-lane p-integrality of the t = 8
rows at this prime is DETECTOR-ONLY (absence of `div. by 0`, no `PINT PASS`;
rank report §8).  This lane reprints the same `A0VALUE` and empty `.err`.

Together: Lemmas 3.3 and 3.4 hold at `(p, yy) = (32003, 11288)` for t = 8.
Lemma 3.5 is pending the eliminating polynomial.  Lemma 3.7 on an affine
simple point is pending the point.

## 6. Clause (i)_8, cited, and what is not claimed

Rank report, modular run `rank_t8_mod_p32003_b0_parti`: `PARTI (B,C): dim=0
vdim=5224`; `PARTI (B) alone: dim=0 vdim=11440 = C(16,7)`.  Both are
positive-weight cone statements, promoted to characteristic zero by the
banked properness lemma, with the DETECTOR-ONLY caveat just named.  `(B)` hsop
⇒ clause (i) (rank report §4.2).  This is the banked `(i)_8` / B-HSOP through
t = 8 of 17(rrrrr).  This lane does not re-run that `std`.

What this lane does *not* claim: `(V0)-tail_8`, `(8.1)_8`, `(T)_8`, `k_8 = 1`,
reducedness of Y_8, or Prop. 7.1 on the whole cone.

## 7. Controls

**Positive, t = 6.**  Charged `verifypoint_t6_mod_p32003_b0.sing` replayed
locally (`run.sh`, wall 0 s).  The `.out` is byte-identical to the charged
file (sha256 `6b87efdd1b671a76270f6bf341a57d886acb9347274dcb0582ba563849d6a2ef`
both sides): local vdim 1, POINT `(1, 4339, 9016, −15982, −6895)`, JACRANK 4,
KERNEL_CONSISTENT=1, all five FITTcheck=1, `W_NONZERO_AT_POINT=1`,
`TTOP_AT_LIFT=13229`.

**msolve parser.**  Charged `msolve_point.py` on the Galois t = 6
parametrization (`w254/msolve_t6_param.txt`) prints
`ROOT 12955 COORDS [4339, 9016, 16021, 25108]`.  16021 ≡ −15982, 25108 ≡ −6895
(mod 32003); 12955 is the charged `BETA`.  The same parser is the one-line
post-FGLM job at t = 8 (`verify_from_msolve.sh`).

**Negative, perturbed W.**  Same t = 6 point, FITT identity run with `W_r+1`
in place of `W_r`: all five `FITTcheck=0`, marker
`PERTURB_FITT_FAILS_AS_REQUIRED=1`.  The nearby point with q2 ↦ q2+1 has
`MINORS_ZERO=0` and local vdim 0 (`PERTURB_NEARBY_FAILS_AS_REQUIRED=1`).

## 8. FALLACY-v2

No exit-price assertion; no `charge_basis` line.

**Modular → char 0.**  The only char-0 promotion made here is the boundary
half of clause (ii), via Prop. 7.1's specialisation argument, after CONE
dim = 1 was obtained from the CI quotient dimension (not assumed).  Affine
non-vanishing is *not* promoted: there is no affine F_p-point, and
`std(I2+(W)+(b4−1))` did not finish.  Lemma 3.7 is not applied to P̄_bd
(that point is not in Y_8).  `k_8 = 1` is not inferred from t ≤ 6.

**Floor/attainment.**  `d_Γ(8) = 52140` is the EN value, used only after the
CI chart was measured 0-dimensional of length 52138 and the boundary
contribution was bounded below by Lemma 3.8; the two ends squeeze `n'` to
equality, they are not an interpolation.  The 52138 is a *length*; reducedness
is not claimed.

**`sat()`, raw remainder degree.**  None.  Memberships are `reduce` against
`std`; the FITT checks are ring identities evaluated at a point.

**Variable/ring map.**  Declared in §1–2; generator order
`b4, q2_0, …, q7_0, b3`, weights `1,2,3,4,5,6,7,9`, coefficient field
`GF(32003)` with `yy = 11288`.  Image checks: split of `H_8`, `A0VALUE ≠ 0`,
`MINORS_ZERO`, `FITTcheck`, `KERNEL_CONSISTENT`.  msolve's t = 6
parametrization was checked against the Singular point before being used as
the t = 8 parser.

**Prime label.**  p is the field characteristic; 𝔭 | p in A_8.  No derivative
notation.

## 9. Computation record (`box/k16t8-20260905/`)

```text
inputs.sha256, inputs.check.log          15/15 OK (awk from the receipt)
emit_jobs.py, gen.py (copy), run.sh      emitter / runner
verifypoint_t6_*.{sing,out,err,time}     t=6 replay, wall 0 s, byte-equal
perturb_t6_*.{sing,out,err,time}         W_r+1 and nearby-point negatives
t6_msolve_points.{txt,err}               parser control on the t=6 param
listboundary_t8_*.{sing,out,err,time}    six-point listing, wall 1 s
minpoly_listboundary_t8_q{4,5,6,7}.txt   finduni univariates
boundary_q6_factor.out                   (1)(2)(3) factorisation over F_32003
linesearch / planesearch / triplesearch / foursearch_t8_*.out
                                         empty sparse affine slices
goodred_p32003_t8.out                    H_8 split / disc / (3/p)
msolve_t8_mod_p32003_b0_ci.ms            76 MiB CI system (copied from .28)
w7/msolve_t8_t16.log                     16-thread F4 + FGLM freeze
w7/affinew_t8_*.out                      std(I2+W+(b4-1)), timeout 5400 s
w18/pattern_t8_*_dimonly.{out,time}      SLICE dim=1; MAIN std timeout 6000 s
cone / conew / hunt / affinew .sing      emitted; conew still running on .28
verify_from_msolve.sh                    post-FGLM pipeline, not yet runnable
```

Wall clock: t = 6 controls 0 s; listboundary 1 s; sparse affine slices 1–56 s;
CI F4 5297 s (16 threads); FGLM still running at seal (see §10).  The 4-thread
msolve on .28 was left in place as a backup and was still in its first degree-15
matrix (80415 × 106219) when the 16-thread F4 finished.  Other-lane Singular
jobs on .7 (exact chart t = 5, minors export) were not killed.

## 10. OPEN and the exact remaining job

`OPEN[K16-ONE-POINT-T8]` is not closed.  Quantity: number of verified simple
affine `F_p`-points of `Γ_8 ∩ {b4 ≠ 0}` with `W ≠ 0` is still `= 0`.  The
chart length, the flat-model hypothesis, and `n' = n` at this prime *are*
closed.

Exact remaining job, in order:

1. Finish msolve FGLM + rational parametrisation of the already-computed
   grevlex GB of `subst(G, b4=1)` over F_32003 (quotient dimension 52138,
   non-trivial/trivial = 13835/52138, density 95.39%).  Process at seal:
   pid 64330 on 172.30.0.7, `msolve -v 2 -t 16 -l 44 -u 1 -P 1`, 16 threads,
   RSS 18 GiB, log frozen after `Density of non-trivial part 95.39%`,
   param file still 0 bytes.  Scaling the t = 6 sequence-generation time
   (0.25 s at D = 1548, 8.69 Gops/s, ~D³) suggests several hours; it may
   finish after this lane's 180 min cap.
2. `python3 msolve_point.py w7/msolve_t8_param_t16.txt` (validated at t = 6).
3. `gen.py 8 --mode mod --prime 32003 --branch 0 --job verifypoint --point 1,q2,…,q7`
   and the charged `evalpoint` checks: local vdim 1, JACRANK 6, MINORS_ZERO,
   KERNEL_CONSISTENT, W ≠ 0, FITT.
4. *Then*, to pass from one affine orbit to clause (ii)_8: either the
   eliminating polynomial's degree pattern plus Corollary 3.6 (to get
   `k_8 = 1`), or `vdim(I2+(W)+(b4-1)) = 0` (the affine half of Prop. 7.1).
   Neither is in hand.  Do not infer `k_8 = 1` from t ≤ 6.

Until (1)–(4) complete, `(V0)-tail_8` and `(T)_8` stay OPEN.  The jobs on
.7/.28 were left running.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18614`.
- Body SHA-256:
  `9a01b66ab811018c08f3ce19fb7f2237f5ef99b32d8d0b8cea7bb1018913ce55`.
- Frozen basis: `c576a3d40d4d1ec51e2bdc4657aea38397c1af37`.
