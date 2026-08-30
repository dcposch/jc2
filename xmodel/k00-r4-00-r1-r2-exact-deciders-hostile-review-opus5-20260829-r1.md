# Hostile review: exact `R4-00` R1/R2 grade-19 deciders

Reviewer: Opus 5 (independent hostile review lane; not the producer model)
Date: 2026-08-29 UTC
Reviewed producer: `xmodel/k00-r4-00-r1-r2-exact-deciders-sol56-20260829.md`
Output path override in effect: this file only; no seal block appended.

## 0. Verdicts

```text
CELL-R2  (D != 0)                    CONFIRM_WITH_CORRECTIONS
CELL-R1+ (p = +8i q, q != 0)         CONFIRM_WITH_CORRECTIONS
CELL-R1- (p = -8i q, q != 0)         CONFIRM_WITH_CORRECTIONS
```

The mathematical content of all three cell-emptiness claims is confirmed
without qualification. The corrections are to the producer's *framing* of why
the certificate works, and to one wording of a replay control; they widen the
result rather than narrow it. Promotion recommendation is in Section 8.

The producer's displayed identity is exactly right. I did not take it on
trust: I rebuilt the seven literal rows from the 569 frozen tails, then
*derived* the six cofactors by exact linear algebra over `Q` from my own rows
(Section 5.1) and separately replayed all three sealed cofactor vectors in
fresh reviewer-owned Singular processes on audited AWS hosts (Section 6).

The headline correction: the certificate needs **neither route substitution
nor any of the cell localizers**. It is one identity on the whole `R4-00`
stratum, so it kills CELL-R0, CELL-R1+, CELL-R1- and CELL-R2 simultaneously.

## 1. Custody

All five pinned inputs verified byte-exact on the working tree:

```text
4bd52f063289aa6dbd22b393ebec35cd90024b4ea2031a2fd21f227a5de65042  producer report
  body: 8478 bytes through the unique standalone <!-- BODY-END --> line,
        6e420952b432f6d22d676c98431cd7bc8842fe4c9ce8c28dca54828813862083  MATCHES
a6e2b54fa0ca8ef3f96144d11c776a09d42175761be302745d02b8b14367ce79  FULL_DECIDER_FREEZE.sha256
0ffc4f741eb2b6a8257dd90c47f194f950752150f57468d81a7779406ab60ed3  entry-solve (Fable 5)
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848  tails.json
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b  compile_contracted_source_v20r2.py
```

`FULL_DECIDER_FREEZE.sha256`: **66/66 entries verify**. The 20-entry
`frozen/compiled_v1/PACKETS.sha256` also verifies 20/20. Every one of the
148 per-generator `sha256` fields across the six packet JSONs verifies under
the builder's stated convention `sha256(singular_text + "\n")`.

Firewall observed: no access to, inspection of, or git operation on
`jc2-lean`; no canonical ledger edited; only this report written. The
producer's `build_r400_packets.py` / `run_exact_packet.py` were never
executed or imported, and were read only after my own rebuild was complete
(and then only to identify the `sha256` field convention and the declared
`r1_substitution`, both cross-checked against my independent result).

## 2. Clean-room reconstruction of the seven literal rows (attack 1)

A stdlib-only sparse `Q`-polynomial / `Lambda`-series engine
(`/tmp/k00rev/engine.py`, `rows.py`, `stratum.py`) expands all seven rows to
`Lambda^20` directly from `tails.json`, under conventions re-read from the
frozen compiler source, not from any prose:

```text
coordinate images  C0=(1+d0)/256, C1=d1, C2=(1+d2)/16, C3=d3,
                   C4=(3+d4)/8,   C5=d5, C6=1
load shifts        k10 -> Lambda^2,  k6 -> Lambda^6,  k2 -> Lambda^10
targets            row2 -1*Lambda^14 mu2, row4 -1*Lambda^16 mu4,
                   row6 -1*Lambda^18 mu6, row7 -(1/4)*Lambda^19 Jdet
truncation         TRUNCATION = 20   (grades 0..19)
```

Census re-verified independently: 569 tail terms; per-term weight
`sum(monomial . [8,7,6,5,4,3,2,2,6,10]) == 12 + ell`; load linearity
(`sum(monomial[7:]) <= 1`, entries in `{0,1}`). All three assertions hold for
every term.

The `R4-00` stratum was instantiated with `d[1]=d[2]=d[3]=0`,
`d[4]=ell(s,t)`, `d[5]=ell(s1,t1)`, `d[6..13]` fully general 6-vectors in
adapted coordinates, **and `d[14..19]` left as fully generic free 6-vectors**
rather than assumed absent. Full symbolic build: 0.84 s, ~138 variables.

Audited grade slots — all 140 row/grade slots inspected:

* grades 0-11 of all seven rows vanish **identically** (not merely on a
  subvariety); row 6 additionally vanishes at grades 12 and 13;
* none of the 36 generic `d[14..19]` variables occurs anywhere in grades
  <= 19, confirming the dropped columns without assuming them;
* the columns absent from the whole window are exactly `a12, a13, b12, b13,
  k10_8..k10_17, k2_6..k2_9, k6_8..k6_13` (pre-forcing), and after the
  forcing of Section 3 the absent set grows to exactly the 20 columns the
  producer lists in `SOURCE_CONTROLS.json` (`a10..a13, b10..b13, u12, u13,
  v12, v13, k10_6..k10_9, k6_6..k6_9`).

Independent numeric control: a **second, structurally different** evaluator
(plain `Fraction` series, no symbolic engine, `/tmp/k00rev/numcheck.py`)
reproduces grades 0-11 vanishing and the Section-5 identity exactly at six
independent random rational stratum points, and reports a nonzero residual
when the forcing is dropped.

## 3. The logical reductions before the packets (attack 2)

All three reductions verified as exact polynomial identities of my rebuilt
rows over the **full** base, with no radical replacement, chart choice, or
normalization.

**Grade 12 (cone forcing).** On the raw stratum:

```text
G3,12 + G1,12/8    = (3/16384) Az Bz
G5,12 + G1,12/128  = -(3/131072) Az Bz
G7,12 + G1,12/1024 = -(3/2097152) Az Bz
G4,12              = (3/524288)(Bz^2 - 64 Az^2)
G6,12              = 0
```

each an identity with zero remainder. Over any field, `Az Bz = 0` and
`Bz^2 = 64 Az^2` force `Az = Bz = 0`. This uses only the imposed rows
`G1,12`, `G3,12`, `G4,12`.

**Grade 13 (`T` ladder).** After `Az = Bz = 0`, with
`p = 6uz + 5 kappa s`, `q = -6vz + 5 kappa t`:

```text
G1,13 = (1/2048)( p A7 + q B7 )      G2,13 = (1/2048)( -4q A7 + (p/16) B7 )
G3,13 = -(1/8) G1,13   G5,13 = -(1/128) G1,13   G7,13 = -(1/1024) G1,13
G4,13 = G6,13 = 0
```

exact, zero remainder. Grade 13 is therefore exactly `T (A7,B7) = 0` and
imposes nothing beyond the `T`-kernel condition.

**Grade 14 (`A7 = B7 = 0`).** After `Az = Bz = 0`:

```text
G3,14 + G1,14/8 = (3/16384) A7 B7        G4,14 = (3/524288)(B7^2 - 64 A7^2)
G5,14 + G1,14/128 = -(3/131072) A7 B7    G6,14 = 0
G7,14 + G1,14/1024 = -(3/2097152) A7 B7
```

with **no inhomogeneous remainder at all**. Over any field this forces
`A7 = B7 = 0`, using only imposed rows `G1,14`, `G3,14`, `G4,14`.

**Omitted rows.** The packets omit `G4_14, G6_14, G4_15, G6_15, G6_16,
G6_17`. Each of the six is **identically zero** on the forced stratum in my
rebuild — not small, not absorbable, exactly zero. Nothing is silently
dropped.

**Radical vs. scheme (accidental strengthening check).** I re-derived the
cube certificates

```text
Az^3 = (1/64)[ Bz (16384/3)(G3,12 + G1,12/8) - Az (524288/3) G4,12 ]
Bz^3 = Bz (524288/3) G4,12 + Az (1048576/3)(G3,12 + G1,12/8)
```

both exact. So `Az, Bz` lie in the **radical** of the grade-12 row ideal but
not in the ideal itself; the same holds for `A7, B7` at grade 14. The
substitutions `Az=Bz=A7=B7=0` that define the packets are therefore
*field-valued (reduced)* steps, not ideal-theoretic ones. Consequently:

* the three sealed unit certificates are scheme-theoretic statements about
  the **substituted** packets, and
* the passage from the original `R4-00` ideal to those packets is valid for
  `K`-points of a field `K`, which is exactly the declared scope.

No scheme-theoretic or nilpotent strengthening is claimed by the producer,
and none should be read in. (A Nullstellensatz argument would upgrade the
set-theoretic conclusion, but no explicit cofactor for the unsubstituted
ideal is exhibited anywhere, so that upgrade is not certified here.)

## 4. Literal audit of the three cells (attack 3)

I rebuilt each route's rows in my own engine and compared, term by term,
against every packet generator.

**CELL-R2.** The R2 packet applies *no* substitution beyond
`Az=Bz=A7=B7=0`; `uz, vz` survive as ring variables and `p, q, D` appear only
inside the localizer. Verified:

* `OPEN_D_KAPPA = 1 - kappa*D*zinv` expands exactly to
  `1 - zinv*(36 kappa uz^2 + 60 kappa^2 s uz + 25 kappa^3 s^2
  + 2304 kappa vz^2 - 3840 kappa^2 t vz + 1600 kappa^3 t^2)`,
  i.e. `D = p^2 + 64 q^2` with `p = 6uz+5 kappa s`, `q = -6vz+5 kappa t`;
* `OPEN_ST = 1 - t*wt - s*ws` correctly encodes `(s,t) != (0,0)`;
* `OPEN_JDET = 1 - Jdet_0*jinv` correctly encodes `Jdet_0 != 0`;
* all **36/36** retained grade-14..19 generators equal
  `stated_normalization * my_row` exactly, with term counts matching
  one-for-one (`10,11,10,10,10 | 28,31,28,28,28 | 68,73,70,16,70,67 |
  126,132,131,40,131,124 | 224,236,239,104,241,21,225 |
  357,375,389,198,398,64,371`);
* the packet's 62 mathematical variables are **exactly** the set of
  variables that actually occur in my forced rows — no missing column, no
  phantom column.

**CELL-R1, both signs.** The declared substitution
`uz = (8*eps*ii*q - 5*kappa*s)/6`, `vz = (5*kappa*t - q)/6` is the correct
parametrization of `{D = 0, (p,q) != (0,0)}`: it gives `p = 8*eps*ii*q` and
recovers `q` as `-6vz + 5 kappa t`; on `D = 0`, `q = 0` would force `p = 0`,
so `q != 0` holds on the cell and the sign `eps` is then uniquely determined.
The two branches are therefore disjoint and exhaust CELL-R1. Verified:

* **36/36** generators of R1+ and **36/36** of R1- equal
  `stated_normalization * my_row` exactly;
* `II2_PLUS_1 = 1 + ii^2`; `OPEN_Q_KAPPA = 1 - kappa*q*zinv`; same
  `OPEN_ST` and `OPEN_JDET`;
* **conjugation**: applying `ii -> -ii` to all 40 R1+ generators reproduces
  the 40 R1- generators exactly, up to the overall sign that the
  primitive-integer normalization fixes (12 of 40 flip sign, and in every
  such case the packet's own `normalization.sign` field flips to match).
  Zero mismatches.

For all six packets the `.sing` ideal text and generator order are
byte-identical to the JSON `generators` list, and the `.sing` ring variable
order equals the JSON `variables` list.

## 5. The six-row identity (attack 4)

### 5.1 Derived, not merely checked

On the stratum with `Az=Bz=0` and `A7=B7=0` and **nothing else imposed**, I
posed the ansatz `Jdet_0 = sum c_{i,n} G_{i,n}` with cofactors in
`span{1, s, t, s1, t1, kappa}` over the support
`{G1,14, G1,15, G1,19, G3,19, G5,19, G7,19}` — 36 unknowns against 2579
monomial equations built from my own rows. The system has rank 36 modulo
`p = 2^61-1`; since `rank_Q >= rank_Fp` and there are only 36 columns, the
solution over `Q` is **unique**. It is

```text
Jdet_0 = -(s1/64) G1,14 -(s/64) G1,15
          -(5/256) G1,19 -(3/32) G3,19 -(1/2) G5,19 - 4 G7,19
```

re-verified exactly against my rebuilt rows: residual identically zero.
This reproduces the producer's displayed identity coefficient for
coefficient, obtained without reading their cofactor vector.

### 5.2 What the identity actually requires

Checked at three forcing levels against my rows:

```text
raw stratum (nothing forced)      residual: 64 terms
Az = Bz = 0 only                  residual: 15 terms, every one in (A7,B7)
Az = Bz = 0 and A7 = B7 = 0       residual: 0
```

So the identity holds after the two forcings and **no route substitution**.
It is a plain polynomial ideal membership — the cofactors `-s1/64`, `-s/64`
and four rationals are polynomials, so **no localization is used**: not
`kappa != 0`, not `D != 0`, not `q != 0`, not `(s,t) != (0,0)`.

This is corroborated inside the producer's own evidence: in all three sealed
cofactor vectors the entries against `OPEN_D_KAPPA` / `OPEN_Q_KAPPA` and
`OPEN_ST` are **zero**. Only `OPEN_JDET` carries a cofactor, and it is `1`.

### 5.3 Reviewer theorem (clean-room)

> Over any characteristic-zero field, on the `R4-00` stratum
> `d = Lambda^4 ell(s,t) + Lambda^5 ell(s1,t1) + sum_{m>=6} Lambda^m d[m]`
> of the frozen normalized V20R2 source, the eleven imposed equations
> `G1,12 = G3,12 = G4,12 = 0`, `G1,14 = G3,14 = G4,14 = 0`,
> `G1,15 = 0`, `G1,19 = G3,19 = G5,19 = G7,19 = 0`
> force `Jdet_0 = 0`.

Proof: grade 12 gives `Az Bz = 0`, `Bz^2 = 64 Az^2`, hence `Az = Bz = 0`;
grade 14 then gives `A7 B7 = 0`, `B7^2 = 64 A7^2`, hence `A7 = B7 = 0`;
the Section-5.1 identity then gives `Jdet_0 = 0`. Every step is an imposed
packet equation, so the argument is order-independent.

**Corollary.** `R4-00` has no field-valued finite jet through grade 19 with
`Jdet_0 != 0`. In particular CELL-R2, CELL-R1+, CELL-R1- and CELL-R0 are all
empty, with no case split, no localizer, and no `kappa != 0` or
`(s,t) != (0,0)` hypothesis.

### 5.4 Why the Rabinowitsch unit identity is decisive

Each sealed certificate is an exact rational identity `1 = sum c_g g` in the
polynomial ring `Q[vars, zinv, ws, wt, jinv]` (plus `ii` for R1), verified by
direct expansion. Hence the ideal generated by the packet's rows and encoded
opens is the unit ideal, so the packet has no solution over any commutative
`Q`-algebra, in particular over every characteristic-zero field — not one
prime, not a screen. A cell point with `Jdet_0 != 0`, `kappa D != 0` (resp.
`kappa q != 0`) and `(s,t) != (0,0)` would supply such a solution by setting
`jinv = 1/Jdet_0`, `zinv = 1/(kappa D)` and any `ws, wt` with
`s ws + t wt = 1`. This is theorem-tier under the campaign's own standard
(`AUDIT.md` / `ops/FLEET.md`: an independently verified `1 = sum h_i f_i`).
No `msolve` output, characteristic-zero `[1]` or otherwise, was consumed
anywhere in this review; none appears in the freeze, and
`LAUNCH.meta` records `msolve_unit_basis_consumed=false`.

Notably, for R1± the identity holds in the **plain** polynomial ring
`Q[..., ii]` with the cofactor of `ii^2+1` equal to zero: the Gaussian
relation is not even needed, which is exactly what one expects from a
certificate that is really a substitution-independent fact.

### 5.5 Translation of the frozen primitive normalizations

Each route's cofactor vector, read from
`frozen/*/output/EXACT_UNIT_COEFFICIENTS.matrix`, translates into the
literal-row identity by `literal_coefficient = (cofactor / jinv) *
normalization`:

```text
generator  route  packet normalization  cofactor / jinv   literal coefficient
G1_14      R2         -4096                 s1/262144           -s1/64
G1_15      R2         +4096                 -s/262144           -s/64
G1_19      R2         +8192                 -5/2097152          -5/256
G3_19      R2         -65536                 3/2097152          -3/32
G5_19      R2        -1048576                1/2097152          -1/2
G7_19      R2        -8388608                1/2097152          -4
G1_14      R1+       +36864                -s1/2359296          -s1/64
G1_15      R1+       +36864                 -s/2359296          -s/64
G1_19      R1+      -147456                  5/37748736         -5/256
G3_19      R1+     +1179648                 -1/12582912         -3/32
G5_19      R1+    -18874368                  1/37748736         -1/2
G7_19      R1+   -150994944                  1/37748736         -4
G1_15      R1-       -36864                 +s/2359296          -s/64
           R1-   (all other rows identical to R1+)
```

All three routes translate to the **same** literal identity, and the R1-
sign flip on the `G1_15` cofactor is exactly cancelled by the R1- packet's
`normalization.sign` flip on that generator. This is the expected signature
of a route-independent identity, and it is what my clean-room derivation
predicts.

## 6. Fresh reviewer-owned AWS replay (attack 5)

Scripts were authored by me from the frozen packet JSON (generator order
preserved) and the frozen cofactor matrices — **not** derived from the
producer's `replay.sing`. Pre-launch audit of both hosts, then a bounded
synchronous run under `setsid --wait` with a recorded PGID and
`timeout --foreground` (no unrecorded inner process group), stdin at
`/dev/null`, every script terminated by explicit `quit;`, and the reaped
child status authoritative.

```text
Box02  i-010201a5da47795c4  34.203.207.55  ip-172-30-0-186  x2idn.32xlarge
  pre-launch load 1.16/1.24/1.09, 1983 GiB available, swap used 0 kB
  Singular for x86_64-Linux version 4.3.2 (4330, 64 bit) Apr  1 2024
  R2.sing  a25b1ff13617572e63de4304dee43db3d232a61da81b1b67665c8afe06b43c6f
  PID/PGID 467218/467218   2026-08-29T23:01:48Z -> 23:01:49Z
  exit 0, wall 0.052 s, max RSS 15,656 kB
  R2.out   54dc7af25fdc628af98ec6ef6dda5cc4506c628aac966580e281d936c6ea239e

Box03  i-0ece0b9a3b4a7512f  98.80.65.144   ip-172-30-0-249  r6i.16xlarge
  pre-launch load 2.15/2.21/2.02, 460 GiB available, swap used 0 kB
  R1P.sing 673b159544e640d8b7a604faedd6d6f0746bc133bc4df5723cdaf90846f9bdbf
  PID/PGID 418583/418583   23:02:26Z -> 23:02:27Z  exit 0, 0.052 s, 17,636 kB
  R1P.out  7223a869d27a2ff5edc970628516256f98ad9c76b63ef522fde7aed87317d772
  R1M.sing 878808c260cbb211e716407521d537d6d1fa6af7c2d31d640676263686febfb3
  PID/PGID 418686/418686   23:02:28Z -> 23:02:28Z  exit 0, 0.053 s, 17,580 kB
  R1M.out  cfbec3547e41a8fec23ed79fbd31faad9fed1ef6cad71803bcdf776c8edbfdda
```

Replay receipt, identical shape on all three routes:

```text
REV_OPUS5_NGENS = 39 (R2) / 40 (R1+) / 40 (R1-)
REV_OPUS5_UNIT_IDENTITY = PASS
REV_OPUS5_COFACTOR_DROPS_DETECTED = 7/7
REV_OPUS5_GEN_MUTATION_DETECTED = 1
REV_OPUS5_JDET_LOCALIZER_SIGN_DETECTED = 1
REV_OPUS5_STD_DIM = -1        (independent, cofactor-free)
REV_OPUS5_REDUCE_ONE = 0      (independent, cofactor-free)
REV_OPUS5_RESULT = UNIT_IDEAL_CONFIRMED
```

The sub-0.1 s runtimes are genuine, not a parse failure: a separate
integrity probe had Singular print `size(J[i])` for all 39 R2 generators, and
the returned term-count vector matches my local vector exactly, element for
element. The certificate's cofactors have monomial degree <= 2, so `std`
reaches `1` at very low degree.

**Process safety.** No signal was sent to any process. The twelve protected
base-diagnostic PIDs (`448323/448356/448357/448359` on Box02;
`379369/379402/379403/379405/379465/379498/379500/379502` on Box03) were
verified alive before and after every run and were left untouched; a
post-run sweep shows the only live `Singular` processes on either host are
those three protected base jobs. No orphan, zombie, or leftover process from
my runs remains. The separately owned formalization instance was neither
inspected nor touched. The still-running base-locus jobs were **not**
consumed as theorem evidence anywhere in this review.

Additionally, all three unit identities were verified a second time
**locally and independently of Singular**, by direct expansion of
`sum(cofactor * generator) - 1` in my own polynomial engine: exactly zero in
each case.

## 7. Negative controls (attack 6)

Detected:

* **Per-tail source sensitivity, 302/569.** Because the rows are linear in
  the tail coefficients, I computed the exact identity sensitivity of every
  one of the 569 frozen tail terms. A `+1` mutation of any of **302** of
  them breaks the identity, including **all 36** row-1 tails, 57/58 row-3,
  86/89 row-5 and 123/131 row-7. The 267 insensitive terms are the 255 tails
  of rows 2, 4, 6 (which the identity does not use at all) plus 12 terms of
  rows 1/3/5/7 that contribute only outside grades 14, 15, 19.
* **Coordinate normalization.** Mutating any of `1/256`, `1/16`, `1/8`, the
  constant `3` in `(3+d4)/8`, or either constant `1` in `(1+d0)`, `(1+d2)`
  breaks the identity with a large nonzero residual. All six detected.
* **`Jdet` target.** `-1/4 -> +1/4` (residual `-8/5`), `-1/4 -> -1/2`
  (`4/5`), and moving the `Jdet` target from row 7 to row 6 (`12/5`) are all
  detected.
* **Stratum geometry.** Mutating any single entry of `ell(s,t)` or of
  `cone(a,b,u,v)`, or changing the valuation from 4 to 3, breaks the
  identity. Dropping either forcing (`Az=Bz=0`, `A7=B7=0`) breaks it.
* **In-Singular, on AWS.** Zeroing each of the 7 nonzero cofactor entries in
  turn breaks the unit identity (7/7); doubling the leading term of a used
  generator breaks it; flipping the `Jdet` localizer to `1 + Jdet_0*jinv`
  breaks it. All on all three routes.

Not detected, and honestly so:

* **The three load shifts** (`k10:2`, `k6:6`, `k2:10`) and **the three `mu`
  target signs and the `mu2` target shift** are invisible to this identity.
  This is not a weak control, it is structural: `k10_j`, `k6_j`, `k2_j`,
  `mu2_j`, `mu4_j`, `mu6_j` are free unknown columns, so a shift or sign flip
  is a relabelling of free variables and cannot change the solution set. The
  correct reading is a *positive* one: the emptiness conclusion does not
  depend on the load-shift or `mu`-sign conventions at all. (The `k10` shift
  does matter for the *meaning* of `kappa = k10_0`, hence for the packet
  definition, but not for this certificate.) I record this rather than
  claiming a clean sweep.

Evidence independent of producer code: everything in Sections 2, 3, 5.1,
5.2, 7 (first five bullets) and the local re-expansion in Section 6 uses only
my own engine, `tails.json` and the frozen compiler's declared conventions.
Dependent on producer artifacts (but attacked, not trusted): the packet JSON
contents, the cofactor vectors, and the AWS metadata — each independently
re-derived or re-verified above.

## 8. Disposition, corrections, and maximum safe scope (attack 7)

**Disposition.** This is a **new, correct implication of the frozen literal
source**. It is not a packet error, not a compiler error, not a source error,
and not a producer error. No discrepancy of any kind was found between the
frozen source, the compiler conventions, the serialized packets, the sealed
cofactors and the claimed conclusion.

**Corrections to carry into promotion.**

1. *The route substitution is not required.* The producer presents the
   identity as holding "after the previously certified grade-12/13/14 forcing
   and the route substitution". The forcing is required; the route
   substitution is not. The identity holds on the common forced stratum and
   is inherited by every specialization, which is why all three routes
   produce the same literal identity.
2. *No localizer is used.* `D*kappa != 0`, `q*kappa != 0` and
   `(s,t) != (0,0)` carry cofactor zero in all three sealed certificates and
   are not needed. Only `Jdet_0 != 0` is used. The promoted statement should
   not advertise the cell localizers as hypotheses.
3. *The result is uniform over `R4-00`, not cell-by-cell.* The same eleven
   equations kill CELL-R0 as well, at grade 19. The separate grade-18
   rank-zero unit kill remains valid and is a sharper (lower-grade) result
   for that cell, but it is no longer needed to close the packet.
4. *Minor wording.* The producer writes "A deliberate mutation of one used
   generator failed the identity." The frozen `replay.sing` in fact zeroes a
   used **cofactor** entry (`CDROP[1,1]=0`); the generator-side mutation lives
   in the builder controls, not in the replay. My replay performed both, and
   both were detected, so nothing substantive turns on this — but the
   sentence should be corrected.

**Maximum safe scope.** Exactly this and no more:

> On the normalized frozen V20R2 support, on the `R4-00` stratum, over every
> characteristic-zero field: there is no field-valued finite jet satisfying
> the literal coefficient equations `G_i,n = 0` through grade 19 together
> with `Jdet_0 != 0`. Equivalently CELL-R2, CELL-R1+ and CELL-R1- are empty
> as field-valued finite-jet cells through grade 19.

Explicitly **not** established, and not to be inferred: arcs, germs,
compatible infinite jets, convergence, polynomial-map attainment, any other
support or valuation, any other normalization, non-reduced/scheme-theoretic
structure of the unsubstituted `R4-00` ideal, a counterexample, or JC2.
Finite jets are not arcs; a cell being empty is not a statement about any
map.

**One scope dependency, verified and flagged.** I probed whether the
stratum shape is forced by the equations. It is not, and the boundary is
sharp:

* `d[4]` on the cone **is** forced (grade-8 equations are the same
  certificate pair in `A(d[4]), B(d[4])`);
* `d[5]` on the cone **is** forced (grade 10 is `Q(d[5])`, same pair);
* but `d[5] = ell(s1,t1)`, i.e. the vanishing of the two transverse cone
  coordinates `u5, v5`, is **not** forced. With `d[5] = cone(a5,b5,u5,v5)`
  the grades 8-10 still vanish identically and grade 11 is exactly
  `T(6u5, -6v5) . (Az,Bz) = 0` — which becomes vacuous the moment grade 12
  forces `Az = Bz = 0`. So `(u5,v5)` is a free cell parameter, and on the
  wider family the six-row identity does **not** extend (residual 89 terms
  on the 4-parameter `d[5]`, 445 terms on a generic `d[5]`).

This is the grade-11 `y`-level fan, and it is exactly what the `R4-0k`
packet index encodes: `R4-00` is the `u5 = v5 = 0` cell. The complementary
cells are the separately owned `R4-02` branch-closure packet and its own
hostile review, which are **outside my pinned custody and were not verified
here**. Therefore: this review closes `R4-00`; the further statement "the
valuation-four grade-19 residual is now closed" is licensed only in
combination with that separate, separately reviewed result, and should be
recorded with that dependency explicit.

**Promotion recommendation.** `PROMOTE` the corrected statement above, as an
exact characteristic-zero field-valued finite-jet emptiness theorem for
`R4-00` through grade 19, at evidence tier `EXACT` / lifecycle
`PROMOTED`, with the three certificate seals, the eleven-equation
reviewer proof of Section 5.3, and the scope dependency of the preceding
paragraph recorded verbatim. The producer's per-cell framing should be
replaced by the uniform statement; the rank-zero grade-18 kill should be
retained as the sharper result for that cell rather than as a necessary
ingredient. Do not promote any consequence for valuation four as a whole
until the `R4-02` dependency is checked against its own review record.

No exit-price assertion is made anywhere in this review, so
`charge_basis` is `ABSENT`; that absence is a scope statement, not a
mathematical pass.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `26072`.
- Body SHA-256:
  `8ff0abb2be95f93276c682b617a3be67be53105914d5b3093c30f874fd6c55ca`.
- Frozen basis: `9b64db896b65e100839f6d75fbeea661cd818b9c`.
