# Hostile review: normalized K00 `e=2,m=2,h10=1` closure through G13

Date: 2026-08-30 UTC
Reviewer: Opus 5 (independent, different-model)
Review basis: `4c91d6fc398d1b4f2b8ca1a11d69c4bb3fef9c0d`

## 0. Verdict

```text
G12  branch split              CONFIRM_WITH_CORRECTIONS
G13  fresh n=5 closure         CONFIRM_WITH_CORRECTIONS
conditional whole-cell (0.3)   CONFIRMED  (field-point scope, on the reviewed G0-G11 tree)
```

The whole-cell emptiness is stronger than the producers claim: it needs
**only** §3 of the G12 report (old `n=4` rank-one death), which I rebuilt
from scratch in full generality.  None of the G12 *survival* content is
load-bearing for (0.3).

## 1. Custody

All seven charged files hash exactly as prompted (`eda4f40b`, `cc8d84f8`,
`b352e26e`, `a508b985`, `8ba031e8`, `d72f774c`, `2c918d5b`).  Body seals
recompute exactly: G12 `9501`/`b1e79f46...`, G13 `9494`/`82c277ca...`,
G11 parent `3793`/`74d1b341...`, under the stated "through the unique
standalone `<!-- BODY-END -->` line, including its newline" definition.  The
second `<!-- BODY-END -->` occurrence in each file is backtick-quoted inside
the seal prose, not standalone; no seal ambiguity.  Both replays run in both
`-B` and `-B -O` modes, print byte-identical banners matching the producers,
and reproduce the stated `CERTIFICATE_SHA256` values.

## 2. Reviewer-owned reconstruction

I wrote a fresh engine (`/tmp/rv/eng.py`, ~140 lines) that imports **no**
campaign replay: own sparse `Q[d0..d5]`, own polynomial ring over `Q(i)`
implemented as `Q[I,...]/(I^2+1)` with reduction at multiplication (a
different representation from the engine's `(re,im)` pairs), own truncated
`tau`-series, own row assembly from `tails.json`.

Independently reconfirmed from the 569 tails:

```text
569 terms; row labels exactly {1..7}; weight law sum(m*W)=12+ell on all 569;
every load slot 0/1 and at most one per monomial;
min d-degree of R: 2 in rows 1-5,7 and 3 in row 6;
min d-degree of A10: 2 in every row.
```

The `min degree 3` in row six is the independent origin of "the quadratic
sixth row is zero", which the G13 producer asserts without derivation.

**Shared-modelling exposure (unavoidable, characterized).**  The coordinate
images `((1+d0)/256, d1, (1+d2)/16, d3, (3+d4)/8, d5, 1)`, the graph map
`D(S,T)=(2S+S^2,(1+S)T/8,S+16T^2,T,S,2T)`, the cone form, and the load
prefactor `tau^4*k10(tau)` are pinned by the frozen compiler
`compile_contracted_source_v20r2.py`; I transcribed them by hand rather than
re-deriving them (running the compiler is heavy CAS, excluded here).  I
mutated that layer as a control: replacing the constant `3/8` in image 4 by
`1/4` destroys both G13 identities, so the layer is load-bearing and the
exposure is real but bounded to the compiler, which is separately reviewed.

## 3. G12

**Reproduced exactly**, with a general surface `S,T` at grades 2..4, a cone
leading normal, and general `N6..N9`, `k10[1..4]`:

```text
fresh n=5 raw G12 counts   22, 25, 23, 15, 22, 0, 20     (matches §2)
fresh n=5 raw G13 counts   51, 55, 57, 33, 56, 15, 51    (matches G13 §2)
G11_6 = 0 and G12_6 = 0 identically; row six first fires at G13.
```

**Arrival audit.**  With `N9` and `k10[4]` *and* `S5,T5,S6,T6` all carried as
live symbols, no G12 or G13 row depends on any of them.  `k10[3]` is absent
at G12 (confirming the producer's negative control) and present at G13 in
rows 1,2,3,5,7 only, matching `L6_r=[tau^6]A10_r(D(S,T))`.  `S5,T5` are
absent because the old plane lies in the radical of every `Q_r`, so
`DQ_r(ell(S5,T5))[.]=0`; the producers never state or test this, and it is a
genuine additional omitted-variable exposure that I closed.  `K6`/`K2` cannot
arrive: my degree audit gives min `A6`-degree 1 (rows 1-3,5,7) and 2 (rows
4,6), min `A2`-degree 1, which with the reviewed prefactors `tau^12*k6` and
`tau^20*k2` and `k6,k2 in tau*K[[tau]]` gives first arrivals G15/G17 and G23.

**Old `n=4` rank-one death — independently rederived in full generality.**
On `s=eps*8i*t`, `p=eps*8i*q`, with arbitrary `alpha,beta,gamma,eta`, all six
slots of `N6,N7,N8`, and both `kappa,kappa2,kappa3` free, and imposing only
`A(N5)=B(N5)=0`:

```text
G11_6 = 0   and   G12_6 = eps*i*q^3/32   exactly, zero residual terms.
```

`G12_6` carries no `kappa`, `kappa2`, `kappa3`, `N6`, `N7`, or `N8`, so the
producer's "neither `kappa2` nor the new `kappa` load can alter (3.2)" is
CONFIRMED, and the further hypothesis `B(N6)-eps*8i*A(N6)+128tq=0` in (3.1)
is not needed.  `q!=0` is forced by rank one (`q=0` with `Delta=0` is rank
zero).  Death CONFIRMED on both signs.

**Fixtures.**  All four reproduce on my engine: the `n=4` fixture passes
G0-G11 and gives `G12_6 = eps*i/32`; the rank-two fixture passes G0-G12 and
its `B(N7): -2 -> -1` mutant fails with `G12_2 = 3/16384` in exactly one row;
the rank-one fixtures pass G0-G12 on both signs and the `N7[0]: eps*128i ->
eps*127i` mutant gives `G12_1 = eps*3i/1024`.

**Corrections to G12.**
1. The quoted raw counts are *after* imposing the cone form on the leading
   normal, not "before branch specialization" / "before lower-equation
   specialization" as §2 says.  With a fully general `N5` the fresh counts
   are `85,97,107,83,115,58,110`.  Labeling only.
2. §3's fixture is described as failing "exactly as `G12_6=eps*i/32`"; all
   seven rows fail (two terms each).  The row-six value is as stated, so the
   death claim stands, but the fixture is not row-six-sharp.
3. §3 says "all four kernel coordinates in each normal block".  On the old
   rank-one wall `Delta=0` and the kernel is five-dimensional; the "four" is
   imported from the rank-two setting.  Harmless here because I kept all six
   slots free.
4. The G11 dependency label is now stale in the right direction: the G11
   parent is promoted, so §1's "PROVISIONAL" is conservative.

## 4. G13

**Row six.**  Rebuilt directly, the identity holds as an exact polynomial
equality in `s,t,alpha,beta,gamma,eta,p,q,kappa,kappa2,kappa3` and all
`N6,N7,N8,N9` slots:

```text
G13_6 = (t/8)*G11_1 - (s/32)*G11_2 + (35*kappa/2^23)*P4,
P4 = s^4 - 384*s^2*t^2 + 4096*t^4.
```

No `N8` appears (rows 4 and 6 have identically zero `DQ(w)` image).  The
rank-one substitution is correct on both signs: `P4(-eps*8i*t,t)=32768*t^4`,
verified symbolically and by hand (`s^2=-64t^2` gives
`4096+24576+4096=32768`).  With `kappa` a unit and `t!=0` (forced, since
`t=0` on the wall gives `s=0`, i.e. `d[2]=0`), rank one is dead at G13 on
both Gaussian signs.  CONFIRMED.

**Rank two.**  I did not use (4.1)-(4.3).  Instead: the `DQ(w)` image
functionals satisfy `I4=I6=0`, `I3=-I1/8`, `I5=-I1/128`, `I7=-I1/1024`, so
the image is spanned by `I1,I2` and the kernel is exactly four-dimensional
(this is the independent derivation of the rank stratification; the `2x2`
determinant of `(I1,I2)` on slots 0,1 is `-(9/2^20)*Delta`, so `Delta` is
literally the rank-two locus and is the sole denominator).  Hence

```text
T13 = G13_5 + (1/8)G13_3 + (3/128)G13_1
```

annihilates every `N8` slot (`-1/128 - 1/64 + 3/128 = 0`), verified.
`T13` is linear in `N6`, has **zero** `N7` dependence, and is already free of
`alpha,beta,gamma,eta,kappa2,kappa3` before any substitution.  Its `N6`
covector lies in `span{I1,I2}` on all six slots (verified), and the G11
`N6`-map equals the G13 `N8`-map (verified), so `G11_1=G11_2=0` pins exactly
the part of `N6` that `T13` sees.  Clearing the single power of `Delta`:

```text
T13 = (35*kappa/2^17) * s*t*(s^2 - 64*t^2)     EXACTLY, on {G11_1=G11_2=0}.
```

**Correction (in the producer's favour).**  This is an *exact* identity; no
reduction modulo `P4` is required.  The producer's "reduce only by `P4=0`"
step and its (4.3)/`H1,H2,C,D` substitution are both superfluous — `T13`
never sees `N7`.  This removes the only denominator-clearing step I would
have attacked, and makes the second terminal independent of every G12
equation.

**No common point.**  With `P4=0`: `s=0 => 4096t^4=0 => t=0`; `t=0 =>
s^4=0 => s=0`; `s^2=64t^2 => P4=-16384t^4 => t=0 => s=0` (verified
symbolically).  So `s=t=0`, hence `d[2]=ell(s,t)=0`, excluded by `D(d[2])`.
Rank two is dead at G13.  CONFIRMED.

**Controls.**  Reproduced on my engine: the rank-one control passes G0-G12 on
both signs with `G13_6=-21/64`; the rank-two control with `N8=(32,0,0,0,0,0)`
passes G0-G12 and has *only* row six nonzero at G13, equal to `21/524288`.

**Corrections to G13.**
1. §4's "Substitute (4.1), (4.3), clear the sole power of `Delta^{-1}`, and
   reduce only by `P4=0`" overstates what is used: (4.3) is unused and the
   `P4` reduction is unnecessary.  (4.1)/(4.2)'s closed forms `W1,W2` I did
   not verify; they are not load-bearing.
2. §2's "before lower-equation specialization" has the same labeling slip as
   G12 §2 (counts are post-cone).
3. §1 calls `8ba031e8` the "promoted G11 coordinator integration"; that
   integration itself records the G12 producer as provisional, so the
   conditionality flag in §0 is correctly placed.

## 5. Mutation and falsifiability

Reviewer-owned mutations on my own engine, not the producers':

```text
scale row 1 x2  -> row-six identity FAILS, N8 annihilation FAILS
scale row 2 x2  -> row-six identity FAILS
scale row 6 x2  -> row-six identity FAILS
scale row 3 x2  -> N8 annihilation FAILS
scale row 5 x2  -> N8 annihilation FAILS
image[4] const 3/8 -> 1/4 -> both FAIL, all G13 counts change
```

Single-coefficient bumps on high-weight tail monomials leave grade-13 output
unchanged, as expected (those monomials cannot reach G13); this is not a
vacuous-pass hole, since the row-scaling controls above are decisive.  No
identity checked here is a same-status trap: every one has an exhibited
failing mutation.

## 6. Maximum promotable theorem

**(a) G12.**  Over an algebraically closed characteristic-zero field, on the
normalized generic K00 support with `Lambda=tau^2, C6=1, ord_tau(d)=2,
k10[0]=0, k10[1]!=0, Jdet[0]!=0, d[2]!=0`, and relative to the reviewed
G0-G11 transition tree: the old `n=4` rank-one branch is empty at G12 on both
Gaussian signs, with the exact literal identity `G12_6 = eps*i*q^3/32` valid
for arbitrary `alpha,beta,gamma,eta,N6,N7,N8,kappa,kappa2,kappa3` subject to
`A(N5)=B(N5)=0`.  The fresh `n=5` rank-one (both signs) and rank-two branches
have exact fixtures surviving G0-G12, so
`V(G0..G12) ∩ V(k10[0]) ∩ D(k10[1]) ∩ D(d[2]) != empty`.

**(b) G13, fresh `n=5`.**  On the same face, every fresh `n=5` point with
nonzero leading normal is empty at G13: the exact identity
`G13_6=(t/8)G11_1-(s/32)G11_2+(35*kappa/2^23)P4` forces `P4=0`, which on the
rank-one wall gives `32768*t^4!=0`; on `Delta!=0` the exact identity
`T13=(35*kappa/2^17)st(s^2-64t^2)` on `{G11_1=G11_2=0}` forces
`st(s^2-64t^2)=0`, and `P4` and `st(s^2-64t^2)` have no common projective
zero, so `s=t=0`, contradicting `d[2]!=0`.

**(c) Whole cell.**  `V(G0,...,G13) ∩ V(k10[0]) ∩ D(k10[1]) ∩ D(d[2]) =
empty`, at **field-point scope over an algebraically closed characteristic-
zero field**, on the reviewed G0-G11 tree.  This is now unconditional in the
sense the producers hedged: it consumes from the G12 report only §3, which I
rebuilt independently and in greater generality.

Explicitly **not** established: nonreduced or scheme-valued emptiness (the
argument is set-theoretic; no ideal-membership or primary decomposition was
computed); any statement about `h10>=2`, `h10=infinity`, another `(e,m)`,
another K00 support; compatible higher jets; formal arcs; occurrence or
source reachability; attainment; algebraization; a polynomial Keller map; a
counterexample; JC2.  Emptiness at finite jet order is a *finite-prefix*
statement and supplies no floor or bound for any of these.

## 7. Cheapest next nonduplicate gate

Not another grade on this face.  The `h10=1` calendar for `e=2,m=2` is now
closed through the first fresh-`n=5` terminal, and `n>=6` recenterings are
governed by the same K10 surface cubic that already killed `n=5` rank zero at
G11.  The cheapest nonduplicate gate is the **`k10[1]=0` boundary face**
(i.e. `h10=2`) on the same `e=2,m=2` support, reusing this engine with
`k10 = tau^2*kappa' + ...`: the load prefactor shifts by one, so `A10` arrives
two grades later and the entire G0-G11 tree recomputes at a strictly cheaper
grade budget than a new `(e,m)`.  Second cheapest, if a source gate is wanted
instead of a cell gate, is a compiler-level re-derivation of the coordinate
images and load prefactors, which is the one modelling layer this review had
to transcribe rather than rebuild.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12546`.
- Body SHA-256:
  `917ec18c19362298052fb15170d4a86a9d51b58fa378a405d6be8a15448d707e`.
- Frozen basis: `4c91d6fc398d1b4f2b8ca1a11d69c4bb3fef9c0d`.
