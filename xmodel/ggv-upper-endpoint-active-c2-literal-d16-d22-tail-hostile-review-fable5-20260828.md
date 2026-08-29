# Hostile review (Fable5): exact D16--D22 tail of the active-c2 literal survivor

Date: 2026-08-28
Reviewer: Fable 5, independent hostile mathematical review
Verdict: **PASS**

## Reviewed frozen inputs (bytes preserved, hashes rechecked before and after)

- `xmodel/ggv-upper-endpoint-active-c2-literal-d16-d22-tail-sol-ultra-20260828.md`
  SHA256 `a4bfbb1437c0e67a8f55439d6b9bd6d0a60a70340d41e6481068cf148ad50a3c`
- `cases/ggv_8_28_upper_endpoint_active_c2_literal_d16_d22_probe_20260828/probe_literal_tail.py`
  SHA256 `f3371687df3584bd1dbeac9e9ad05aca8212a6dd35b63c17209916ab9d11fb45`
- `cases/ggv_8_28_upper_endpoint_active_c2_d11_d13_extension_20260828/verify_active_c2_extension.py`
  SHA256 `112650dc27b0e13d76979d5adca9315919ee65cb8d9eaf717c1685f99d96de26`
- `cases/ggv_8_28_upper_endpoint_branch_p_20260827/compile_endpoint.py`
  SHA256 `7f840af57695eb0f4e124885a39eabdd0059dad984c917b826d077c77d396be1`
- `cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json`
  SHA256 `ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0`

## Independent checker

`xmodel/ggv-upper-endpoint-active-c2-literal-d16-d22-tail-hostile-review-fable5-20260828-check.py`,
run as `PYTHONDONTWRITEBYTECODE=1 python3 -B ...` (about 3.4 s, standard
library only, deterministic).  Nothing is imported from the producer probe
or the upstream extension checker.  The polynomial backend, the reduced
`N(X)/A(X)^k` rational arithmetic (a deliberately different representation
from the producer's Laurent dictionaries), the fractional-power series
recurrence, the mode ladder, the determinant rows, the born-row affine
solver, and the receiver operator are all rebuilt from the defining
identities.  Terminal marker:

```text
PASS_HOSTILE_FABLE5_ACTIVE_C2_LITERAL_D16_D22_TAIL
```

The producer probe was also replayed once and printed its own frozen marker
`PASS_EXACT_ACTIVE_C2_LITERAL_D16_D22_TAIL` (7.5 s).

## What was independently verified

**1. Prefix reconstruction (before any tail assertion).**  From
`A=X^4-1`, `V0=A`, `T=-A/4`, `Z=(1-A)/2` the displayed closed forms
reconstruct exactly: `F1=A^2*V0=A^3`, `F2=(V0^2+A^2*Z)/4`,
`F3=(V0*Z+A*T)/8`, `F4=(Z^2-A)/64`, `F5=(A-1)/512`, `F6=1/4096`,
`F7..F14=0` on their raw slots and `F15+` slotless.  With `c2=c6=1` and
`c4=c8=c10=c12=0`, the weight-14 base row has a genuine A-pole and the
unique polynomiality solution is the frozen `c14=-6139/2^34`
(re-solved here, not copied).  The characteristic rows `g0..g15` are all
polynomial with `g0=A^6`, `g12=4093/2^28`, `g13=g14=g15=0`, and a full
independent determinant replay gives `D0=...=D15=0`.  All prefix `F` and
`G` rows lie inside the authoritative windows.

**2. Complete mode registration.**  The ladder `c_b t^b F^((12-b)/8)`,
`b=0,2,...,20` (base `b=0` exponent `3/2`), matches the upstream MODES
table, and the exponent law was certified operator-theoretically: for the
weighted recurrence `D_n = sum_(i+j=n) (12-j)F_i'G_j + (i-8)F_iG_j'` one
has `D(t^b F^e) = (12-8e-b) t^b F' F^e`, so each scheduled mode
annihilates every determinant row; my checker verifies this row-by-row
through weight 22 for every registered mode, verifies the series ODE
`F y_t = e F_t y` coefficientwise for every exponent, and confirms that a
mutated exponent (`e_2=1` instead of `5/4`) fails.  No predecessor mode is
omitted from any row sum.

**3. Authoritative raw windows.**  Read directly from the frozen
`RAW_DIRECT_SYSTEM.json`: `F` slots exist only for weights 1..14
(`F_max_weight=14`, so there are **no legal raw F15+ slots**), `G` slots
only for weights 1..21 with `G22_present=false` (**no G22 receiver**), and

```text
G16: X^2..X^8, G17: X^2..X^7, G18: X^2..X^6,
G19: X^3..X^5, G20: X^3..X^4, G21: X^3.
```

All 303 raw variables are accounted for by the census slots plus
`tt_*`/`z_*`; the endpoint charge is `D22=1`.  A mutated expected window
(G19 lower bound 3 -> 2) is rejected by the census comparison.

**4. Born rows, uniqueness, and literal vanishing.**  At weights 16, 18,
20 the newly born mode enters the row exactly as `c*A^(-m)` with
`m=2,3,4`; the affine polynomiality condition has at most one scalar
solution (two solutions would differ by a nonpolynomial `(c-c')A^(-m)`),
and the solved values are exactly the frozen

```text
c16=0,  c18=16369/140737488355328 (=16369/2^47),  c20=0.
```

After solving, `G16=G17=G18=G19=G20=G21=0` **identically** (verified as
exact zero polynomials, not merely inside their degree windows).

**5. Determinant replay.**  With the literal raw `F` (no F15+ slot, F7..14
zero), raw `G0..G15` from the prefix, `G16..G21=0`, and the forced empty
`G22`, my independent replay gives `D0=...=D21=0` and homogeneous
`D22=0`.  This is kept distinct from the endpoint equation `D22=1`, which
this point **fails** (0 != 1): the survivor dies exactly and only at the
endpoint.

**6. The absent receiver.**  The weight-22 characteristic class reduces to

```text
g22 = (9207/144115188075855872) * A^-5   (=9207/2^57 * A^-5),
```

recomputed and reduced independently.  The receiver operator is derived,
not assumed: the only D22 term involving `G22` is `(i,j)=(0,22)`, giving
`(12-22)F0'R + (0-8)F0R' = -40A^3A'R - 8A^4R' = L22(R)`, so
`D22_raw = D22_char - L22(g22) = -L22(g22)`; sign convention confirmed by
the structural identity `D22_char = D22_raw + L22(g22) = 0`.
`-L22(g22)=0` holds exactly.  The kernel is exactly the scalar line
`Q*A^-5`: `L22(R)=0` is the first-order equation `R'/R = -5A'/A` over
`Q(X)`, whose solution space is one-dimensional over the constants.  This
does **not** show general deep-locus emptiness: it is one rational point
whose `g22` happens to be pure kernel; a general deep point may carry a
non-kernel `g22` part, and passing the endpoint requires `-L22(g22)=1`,
which no kernel element satisfies but which is not excluded for the full
locus by this computation.  Equivalently, the `b=22` rung of the mode
ladder (`t^22 F^(-5/4)`, leading term `A^-5`) *is* the kernel freedom: the
endpoint class is well defined only modulo `K*A^-5`.

**7. Mutations (all executed, all caught).**
`c18=0` leaves a genuine weight-18 pole (order 3); `c18` off by `2^-47`
leaves row 18 non-polynomial; dropping `c6` breaks row 14 and re-solves to
a different `c14=5/2^34 != -6139/2^34`; dropping `c14` makes row 14 the
first non-polynomial row; `-40 -> -39` in `L22` leaves the exact residual
`-k*A'/A^2 != 0` on the kernel (executed on the real operator, not just
arithmetic); `g22` denominator mutation `A^-5 -> A^-4` leaves operator
residual `8k*A'/A != 0`; `g22` sign and numerator mutations remain in the
kernel (still annihilated by `L22`) and are caught by the exact identity
comparison with the recomputed `g22` -- this kernel blindness is recorded
explicitly.

**8. q1 status.**  The producer report attaches no q1 label to this point,
correctly.  Informationally, the checker proves there is no `R0` with
`deg R0<=4` solving `V0=A'R0+2AR0'` (the exact linear system is
inconsistent: `6r1=1` vs `-2r1=-1`), so the point could not be called q1
in that sense either.

## Defects (none verdict-impacting)

1. **Producer's `-40 -> -39` mutation is a tautology.**  The probe asserts
   only `Q(39)-Q(8)*Q(5)==-1`, a bare arithmetic identity; the mutated
   operator is never applied to `g22`.  Impact: the report's sensitivity
   claim was hand-verified, not machine-replayed, by the producer.  This
   review executes the real mutation; the claimed residual is correct.
2. **No `g22` mutations in the producer battery.**  Sign/numerator
   mutations of `g22` are invisible to the endpoint operator (kernel
   blindness); the probe neither runs them nor states which layer would
   catch them.  Impact: none on conclusions; made explicit and
   machine-checked here.
3. **Window checks on zero rows are vacuous** as support constraints; the
   load-bearing facts are polynomiality and the exact zero values.  The
   probe does assert the zero values, so no impact; recorded so nobody
   later credits the window pass as independent evidence.
4. **"Complete characteristic schedule" wording.**  The ladder does not
   stop at `c20`: the `b=22` mode exists and is exactly the kernel
   `A^-5`.  Its omission is harmless (no G22 receiver to solve against,
   and `L22` annihilates it), and the report's "modulo `K*A^-5`" sentence
   is the correct statement, but the schedule phrasing should carry the
   caveat.  Wording only.
5. **Producer-side independence is limited.**  The probe dynamically
   imports the upstream extension checker and reuses its arithmetic
   backend, MODES table, and determinant routine (hash-pinned, `main()`
   not executed).  Legitimate as a discriminator, but the producer lane
   shares one arithmetic implementation; the independent implementation
   is supplied by this review.
6. **Chart provenance note (scope, not defect).**  The window census comes
   from the branch-P `c2=0` fixture (`F1=H=A^2`) while the active-c2
   literal point has `F1=A^2*V0=A^3`.  The windows are weight/X-degree
   slot-existence data reused across the lane per the frozen lineage
   (consistent with the D8--D15 hostile review); this review enforces
   them as the authoritative record without re-deriving their origin.

## Scope

This confirms exact identities of one rational specialization and its
death at the endpoint equation only.  It is not a universal deep-locus
theorem, not a scheme statement, not an endpoint or branch-P theorem, not
a Keller result, not a counterexample, and not a resolution of JC2.

## Custody

Case directory:
`cases/ggv_8_28_upper_endpoint_active_c2_literal_d16_d22_tail_hostile_review_fable5_20260828/`
with `README.md`, `RESULT.json`, `SOURCE.sha256` (all load-bearing inputs
plus this review's checker) and `EVIDENCE.sha256` (report, README,
RESULT; no self-reference).  All five frozen hashes were rechecked after
finalization; no frozen file was modified.
