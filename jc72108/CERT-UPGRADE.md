# CERT-UPGRADE — effective spreading-out certification of mod-p EMPTY verdicts

Lane: Fable "effective spreading-out certification" x Sol lateral #4 (certificate
mining, xmodel/sol-lateral.md §4). Date 2026-08-14. Phase-1 feasibility executed
locally (tiny exact runs only, per ops/FLEET.md; no fleet jobs launched, nothing
committed).

## VERDICT UP FRONT

- **Prime-size certification lane: DEAD.** The smallest system in the entire
  campaign (12-var conjE control) would need a certifying prime with ~5 x 10^9
  decimal digits under a dream-floor bound with every constant deleted
  (KPS-shaped bound: ~5 x 10^13 digits). The real (72,108) strata need
  10^33–10^92-digit primes. Our banked primes have 6 digits (105337…225961);
  msolve's mod-p ceiling is ~2^31 (10 digits). The gap is 9+ orders of
  magnitude **in the exponent** for the toy and ~90 orders for the farm. No
  larger-prime engine changes this; see §3 for the honest numbers, including
  the sharper multi-prime product criterion (still 2.7 x 10^8 GB-runs for the
  12-var toy).
- **Certificate-extraction sub-lane (Sol #4 substrate): ALIVE and demonstrated.**
  Phase 1(b) produced four exact, independently verified char-0 Nullstellensatz
  certificates on banked EMPTY systems — sparse (3 of 21 cofactors), integral
  (denominator a = 1), height log 2, and **literally identical across the whole
  B-subset family**, collapsing to a human-readable 2-row identity (§2.4).
  These upgrade msolve EMPTY verdicts to unconditional char-0 theorems with no
  prime bound at all. Empirical wall: instant at 12–14 vars, already
  infeasible at 27 vars (cCa2, consistent with AUDIT.md's 2026-08-13 lift
  retirement).

---

## 1. Phase 1(a) — does msolve emit cofactor certificates? NO

- `msolve --help` (v0.10.1, the installed engine) enumerates the full option
  surface: `-g` (print reduced GB), `-n` (normal forms), `-P` (rational
  parametrization of *solutions* — a NONEMPTY-side certificate only), `-L`
  (lift multiplication matrices), `-q` (signature-based algorithms), `-C`/`-S`
  (colon/saturation). **No flag emits cofactors h_i with 1 = Σ h_i f_i.**
  Checked against the Debian manpage and the msolve GitHub docs — no such
  feature exists in any released version.
- Caveat worth recording: per the help text, `-g` prints the reduced GB "for
  **first prime characteristic**" — i.e. even on char-0 input the printed `[1]`
  is the GB mod the first machine prime of the multi-modular run. A banked
  "char-0 [1]" header is therefore itself trace-level evidence, not a lifted,
  verified char-0 result. (Numerically irrelevant for `[1]`, semantically
  load-bearing: it is exactly the gap this lane was meant to close.)
- Signature-based runs (`-q 1`) compute data that in principle supports
  membership certificates, but msolve does not expose it.
- Adjacent tools: `f4ncgb` (arXiv 2505.19304) does track cofactors but is for
  free (noncommutative) algebras — not usable here. Singular's `lift()` is the
  practical char-0 extractor (used below); it needs its own GB over Q, which is
  the expensive step.

## 2. Phase 1(b) — actual certificates extracted and verified

### 2.1 Pipeline (all local, all tiny)

1. Parse banked char-0 `.ms` file; emit Singular script
   (`ring …,dp; ideal I = …; groebner(I); matrix T = lift(I, ideal(1))`).
2. Run Singular 4.4.1 under `timeout` (all successful runs < 2 s, < 50 MB).
3. **Independent verification**: re-parse the cofactors and check
   Σ h_i·f_i == 1 by exact rational arithmetic in python-flint 0.9.0
   (`fmpq_mpoly`) — a different engine than the one that produced them.

Scripts + artifacts: scratchpad `cert/` (`emit_lift.py`, `verify_cert.py`,
`bounds.py`, `*.cof.txt`); certificate inlined in §2.3 for durability.
Repro: `python3 emit_lift.py systems/conjE/i1l1B3.q.ms lift.sing cof.txt &&
Singular -q < lift.sing && python3 verify_cert.py systems/conjE/i1l1B3.q.ms cof.txt`.

### 2.2 Results ladder

| system | n vars | s eqs | max deg | max coeff | lift | verified |
|---|---|---|---|---|---|---|
| conjE i1l1B3.q (banked EMPTY ctl) | 12 | 21 | 6 | 216 | instant | YES (flint) |
| conjE i1l1B12.q | 13 | 21 | 6 | 288 | instant | YES |
| conjE i1l1B3x6.q | 13 | 21 | 6 | 288 | instant | YES |
| conjE i1l1B3x6x9x12.q | 14 | 21 | 6 | 288 | instant | YES |
| open_8_28_c2_chartG.q ((72,108) s2) | 27 | 46 | — | — | instant, **trivial** (−1 is a listed generator; 1-term cofactor) | prior art, reconfirmed |
| open_8_28_c2_cCa2.q ((72,108) s2) | 27 | 49 | 16 | 1.9e8 | **no result in 120 s probe** (634 MB RSS, climbing); historically timed out locally, retired on fleet (AUDIT.md 2026-08-13) | — |
| reg_9_24_c3_* (runs/) | 23 | — | — | — | **not liftable as-is**: only mod-p-reduced `.red.ms` inputs exist locally, no char-0 twin | — |

### 2.3 THE certificate (conjE i1l1B3, in full)

1 = h1·f1 + h13·f13 + h21·f21, all other 18 cofactors ZERO, where (msolve row
numbering of systems/conjE/i1l1B3.q.ms):

    f1  = 1 + f1n0*t - f1n1*t          (Rabinowitsch row for P1 != 0)
    f21 = f2n0 - f2n1
    f13 = (u + v*w)^2 + g*w^2          (26 expanded terms, coeffs in {±1,±2,±4})
          where u = f1n0-f1n1, v = g2n0-g2n1, w = f2n0-f2n1 (= f21), g = g1n0-g1n1

    h1  = -f1n0*t + f1n1*t + 1         ( = 2 - f1 )
    h13 = t^2
    h21 = -g2n0^2*f2n0*t^2 + 2*g2n0*g2n1*f2n0*t^2 - g2n1^2*f2n0*t^2
          + g2n0^2*f2n1*t^2 - 2*g2n0*g2n1*f2n1*t^2 + g2n1^2*f2n1*t^2
          - 2*g2n0*f1n0*t^2 + 2*g2n1*f1n0*t^2 + 2*g2n0*f1n1*t^2
          - 2*g2n1*f1n1*t^2 - g1n0*f2n0*t^2 + g1n1*f2n0*t^2
          + g1n0*f2n1*t^2 - g1n1*f2n1*t^2

**Actual heights**: 3/21 nonzero cofactors, 18 terms total, max cofactor degree
5, max |coefficient| = 2, lcm of denominators = 1 (the identity is over Z as
written: a = 1). Height h(cert) = log 2 ≈ 0.693 nats. Verified
Σ h_i f_i == 1 exactly in python-flint. This constitutes an unconditional
char-0 emptiness THEOREM for the system — no prime, no bound, no msolve trust.

### 2.4 Family uniformity + the human-readable core (Sol #4 payoff)

All four B-subset variants (B3, B12, B3x6, B3x6x9x12) produced **byte-identical
nonzero cofactor rows** — the B-hypothesis rows f2…f12 are never used. The
identity divides by t^2 (verified in flint) to the t-free statement

    (f1n0 - f1n1)^2  =  f13 + w·f21,
    w = -(g2n0-g2n1)^2*(f2n0-f2n1) - 2*(g2n0-g2n1)*(f1n0-f1n1)
        - (g1n0-g1n1)*(f2n0-f2n1)

i.e. the square of the P1-difference lies in the ideal (f13, f21): a 2-row
emptiness core with multiplier w of degree 3, coefficients {±1, ±2}. On
{f13 = f21 = 0} this forces f1n0 = f1n1, contradicting the Rabinowitsch row —
the entire 21-equation system is empty for **every** B-subset for this one
symbolic reason. This is exactly the motif-mining outcome idea #4 predicted
(sparse, family-uniform, interpolable), obtained on the pre-registered debug
family, within its D ≤ 6 kill window (actual D = 5).

## 3. Phase 1(c) — the effective bound, honestly instantiated

### 3.1 What the certification criterion actually is

Contrapositive of effective spreading-out: if V(f) is NONEMPTY over Qbar, then
every "bad" prime p (EMPTY mod p) divides one nonzero integer A(f) with
log A ≤ H1(n, d, h, s). Hence
- **single-prime form**: EMPTY at one p > e^{H1} proves char-0 EMPTY;
- **product form (sharper)**: EMPTY at distinct primes with Σ log p_i > H1
  proves char-0 EMPTY (if all were bad, their product would divide A).

H1 is governed by worst-case **heights of char-0 witness points** (arithmetic
Bezout/elimination), NOT by any observed cofactor height: our tiny log-2
certificate lives on the empty side and says nothing about the hypothetical
nonempty side that the bound must exclude. Reference shapes:

- H1_KPS = 4n(n+1)·d^n·(h + log s + (n+7)·log((n+1)d)) — the Krick–Pardo–Sombra
  (Duke 109, 2001, Thm 1) height constant; nonempty-side elimination constants
  (d'Andrea–Krick–Sombra, Ann. Sci. ENS 2013) have the same d^n·(h+…) shape.
- H1_dream = d^n·max(h,1) — an unrealistically generous floor (all
  combinatorial factors deleted). The d^Θ(n)·h shape is REAL, not proof slack:
  iterated-power families (x1 = c, x2 = x1^d, …, xn = x_{n-1}^d) have all
  char-0 points at height ~ d^{n-1}·h, so bad primes of that exponential size
  genuinely occur. No theorem of this type can undercut the shape.

### 3.2 The numbers (computed from each system's actual n, s, d, h)

Reference: banked verdict primes 105337…225961 (6 digits, log p ≈ 11.6);
largest prime ever used in the campaign 2147483629 ≈ 2^31 (10 digits,
log p ≈ 21.5); engine-independent 63-bit fantasy: 19 digits, log p ≈ 43.7.

| system | n | d | h(=ln maxcoeff) | digits of certifying prime, DREAM floor | digits, KPS shape | 63-bit runs, product form (dream) |
|---|---|---|---|---|---|---|
| conjE i1l1B3 (smallest object in campaign) | 12 | 6 | 5.4 | **5.1 x 10^9** | 5.4 x 10^13 | 2.7 x 10^8 |
| conjE 14-var variant | 14 | 6 | 5.7 | 1.9 x 10^11 | 3.0 x 10^15 | 1.0 x 10^10 |
| cCa2 ((72,108) open stratum) | 27 | 16 | 19.1 | 2.7 x 10^33 | 9.8 x 10^37 | 1.4 x 10^32 |
| leaf12_UZ (r1 sweep leaf, EMPTY at 8 primes) | 44 | 20 | 30.2 | 2.3 x 10^58 | 2.3 x 10^63 | 1.2 x 10^57 |
| farm 4_12 cCa23 chart (smallest farm chart) | 34 | 12 | 15.5 | 3.3 x 10^37 | 2.7 x 10^42 | 1.8 x 10^36 |
| farm 4_12 c1_core (smallest farm core) | 61 | 31 | 33.8 | 1.4 x 10^92 | 3.4 x 10^97 | 7.3 x 10^90 |

Inversion — what one 63-bit prime COULD certify under the dream floor (h = 1):
d = 2 → n ≤ 5; d = 3 → n ≤ 3; d = 6 → n ≤ 2. Nothing in this campaign is
remotely that small. A product of 10^6 63-bit EMPTY verdicts reaches only
d = 6, n ≤ 9.

### 3.3 The honest number, stated plainly

To upgrade the 12-var conjE toy by prime size alone we would need
log p ≳ 1.2 x 10^10 (a prime of ~5 billion digits) against our actual
log p ≈ 11.6–21.5. For the real strata the requirement is 10^33-plus digits.
**The lane as originally posed dies here**, at the smallest system it would
ever be applied to, under a bound more generous than any theorem can be.

## 4. Phase 2 — per the gate, no run plan; what survives

The phase-1 number is not "reachable with larger primes", so no fleet
recertification pipeline is specced. The surviving derivative lane is direct
certificate extraction (this file, §2), which needs no prime bound:

1. **conjE family sweep (local, minutes, worth doing)**: run the §2.1 pipeline
   over all banked conjE `.q.ms` controls (~96 systems, 12–14 vars). Expected
   output: one parametric identity per (i, ell) cell (the B-uniformity of §2.4
   suggests ~6 identities cover the whole bank), turning the conjE
   "holds"-table into theorem-grade rows. Kill criteria per sol-lateral §4
   pre-registration (D ≤ 6, support-orbit mismatch, NONEMPTY false-positive
   controls).
2. **Mod-p cofactor mining for the big strata (fleet, cheap probe first)**:
   char-0 GB is the bottleneck (cCa2 wall), but `lift(I,1)` **mod p** after a
   fast mod-p GB is cheap and yields cofactor degree/support lower bounds and
   mining substrate (Sol #4 step 2's "two good primes" plan). If mod-p
   certificates at 2–3 primes are small and support-stable, CRT + rational
   reconstruction + flint verification gives the char-0 certificate without
   ever running char-0 GB. Only if that probe shows small stable supports is
   any heavy Macaulay-style reconstruction (e.g. leaf12 at 44 vars, D ≤ 8:
   ~10^7-column sparse mod-p linear systems, Box02-scale) worth costing out.
3. **What stays mod-p-only**: farm cores (61+ vars) and anything cCa2-shaped.
   Their record continues to rest on the existing posture (exact mod-p
   verdicts at ≥3 independent primes + emission guards + two-machine
   agreement), per AUDIT.md's lift-retirement note. No prime-size theorem can
   rescue them; only a reconstructed certificate (2) or a human lemma mined
   from smaller relatives (1) can.

## 5. Anti-stall log

All compute local + tiny: 4 Singular lifts < 2 s each; 1 chartG rerun < 1 s;
1 cCa2 probe hard-capped at 120 s (killed, no result, as expected from AUDIT);
flint verifications < 1 s; no msolve runs; no fleet jobs; nothing committed.
Wall time bound respected end-to-end. reg_9_24_c3 lift skipped for a stated
structural reason (no char-0 input exists), not from laziness.
