# SHEET6-R1-25LOCUS — solution locus of the (2,5)-chain R1 core

Input: runs/r1/r1_25chain_core.out (reduced GB, char 0, 487 elements,
grevlex, vars r3,z,A1,A2,W1,HW1,W2,HW2,EB,x0..x28,s1,cL,t1; msolve -g 2,
55 s). System: systems/r1/r1_25chain_core.ms — 44 eqs = 7 radical + 37
banked chain rows (11 WG-quot + 2 quot-deg + s1-tie + s1-inv + 22
h2-tie; ALL 37 emitted — the "12 deferred" of SHEET6-R1 §11 are the 12
interior W_G^2 slot-pair families of §9.4: ties r=4..12 even (pairs
(8,8);(8,10);(8,12),(10,10);(8,14),(10,12);(8,16),(10,14),(12,12)) and
the r=14 quotient (pairs (8,18),(10,16),(12,14)) vs pq46, farm-sized).

## 1. Dimension

- Leading terms of the 487-elt reduced GB parsed (first monomial per
  element; grevlex, header var order); dim R/LT(I) = dim R/I.
- Singular (dp, same var order), monomial ideal of the 487 leads:
  **dim V(I) = 27** (in A^41). STATUS: BANKED.
- 24 vars appear in NO leading monomial (HW1, HW2, x7..x28); free-ish.

## 2. Variable-occurrence census of the GB (structure certificate)

- W1, HW1, W2, HW2 occur ONLY in the two radical rows 3W1^2-2HW1^2,
  3W2^2-2HW2^2 => the W-pole factors are COMPLETELY DECOUPLED:
  V = V' x C_W1 x C_W2 (each C a 1-dim pair-of-lines). Every
  irreducible component of V contains points with W1*W2 != 0.
- z occurs only in Phi42(z) (12 points, all nonzero); EB only in
  2EB^7-3 (+ one band relation), EB != 0.
- Moduli-only relations (5): s1*t1-1; 2^30 cL^2 = 508021860739623365322188197652216501772434524836001 * s1;
  r3^2-3; A1^3-r3-3; A2^3+r3-3. => s1, cL are UNITS on V (s1 = c*cL^2,
  c != 0): sigma-type collapses s1=0, cL=0 IMPOSSIBLE on V.
- A1=A2 (merge-orbit collapse): IMPOSSIBLE on V: A1^3-A2^3 = 2r3,
  r3^2 = 3 => A1 != A2 at every point. Structural kill of that divisor.
- Band vars x6..x11 (bf_13..18), x20..x25 (bg42_13..18), x26..x28
  (bg21_14/16/18): occur in exactly ONE GB element (elt 278, a single
  EB-weighted relation, linear in x11, x25, x28) => 15 band vars
  contribute 14 free dims.
- Coupled block: r3, A1, A2, x0..x5 (vf1/vf2_34, tf*_38/40),
  x12..x19 (tg*_38/40), s1, cL, t1 — carries the other ~480 relations.
  Accounting: 27 = 2 (W-lines) + 14 (band) + 1 (cL scale) + 10
  (coupled x-block: 14 vars, effective codim 4).

## 3. Degeneracy strata table

| divisor | status on V |
|---|---|
| s1 = 0, cL = 0 (sigma-type) | EMPTY (units: s1*t1=1, cL^2 = c^-1 s1) |
| A1 = A2 (merge collapse) | EMPTY (A1^3-A2^3 = 2r3 != 0) |
| W1 = 0 (or W2 = 0) | codim-1 substratum; NO component inside it (W decoupled) |
| all-x = 0 (scale locus) | EMPTY (e.g. GB elt "...+65536*A2*cL+..." forces x2/x12/x16-combo != 0 when A2*cL != 0) — guard C confirmed at GB level |
| tie-collapse x0=x1=0 (vf1_34=vf2_34=0) | NONEMPTY, dim 25 (39-elt GB, /tmp/r1_25_degB.out) |
| partial-zero x strata (other) | see section 4 |

Tie-collapse identification (engine-verified, chainF.pkl + blocks.pkl):
F5(n,2) = f^5 slot-2 content is LINEAR HOMOGENEOUS in (x0,x1) =
(vf1_34, vf2_34) for all 20 keys n = 1..58, and the 20x2 coefficient
matrix has rank 2 (verified mod p=105337; rank over the char-0 radical
field is >= its mod-p rank). Hence on V: h2-tie right side F5(.,2) == 0
<=> x0 = x1 = 0, and (since s1, cL are units and the tie rows hold)
also <=> (p5 conv WG(.,8)) == 0. The BOTH-SIDES-DEAD (collapsed-tie)
locus is EXACTLY V ∩ {x0 = x1 = 0}: dim 25. On its complement the
level-2 tie is genuinely alive (nonzero on both sides).

## 4. Nondegenerate part: dimension + point

**VERDICT: NONDEGENERATE SOLUTIONS EXIST (char 0), dim 27 = full.**

- Run A (/tmp/r1_25_ndA.ms): the 44 core eqs + Rabinowitsch rows
  u*x0 - 1 (tie-aliveness: x0 = vf1_34 invertible => F5(.,2) != 0 =>
  both sides of the h2-tie alive) and uw*W1*W2 - 1 (both pole W-scales
  nonzero). msolve char 0, -g 2, ~40 s: reduced GB = 598 elements,
  **NOT [1]** => by the Nullstellensatz the locus with
  x0 != 0, W1 != 0, W2 != 0, s1 != 0, cL != 0, A1 != A2 (last three
  automatic) is NONEMPTY over Qbar. Output: /tmp/r1_25_ndA.out.
- LT-ideal dimension of the saturated system (Singular, dp):
  **dim = 27** in the 43-var graph ring = same as V. The nondegenerate
  part is FULL-DIMENSIONAL; all listed degeneracy strata are proper
  (tie-collapse dim 25, W_i = 0 dim 26).
- Maximal independent set (transcendence basis of a top component):
  {HW1, HW2, x0, x1, x5, x7..x28} (27 coords) — the level-2 tie data
  (vf1/vf2_34), one tf-tail, ALL b-band vars, all tg-tails x12..x19
  minus dependents, and the two pole W-scales are free; everything else
  (r3, z, A1, A2, EB, x2, x3, x4, x6, s1, cL, t1, W1, W2) is algebraic
  over them.

Strata dimension table:

| stratum | GB size | dim |
|---|---|---|
| V (all solutions) | 487 | 27 |
| V ∩ {x0=x1=0} (tie-collapse) | 39 | 25 |
| V ∩ {W1=0} (or W2=0) | structural | 26 |
| V \ (all degeneracy divisors) | 598 (graph) | **27** |

## 4b. WARNING — msolve mod-p input handling (campaign-relevant)

Feeding the char-0 .ms (huge unreduced/negative integer coefficients)
to msolve 0.10.1 with the characteristic line set to p > 0 SILENTLY
CORRUPTS the system: r1_25chain_core at p = 105337, 105673, 999999937
all returned GB = [1] (empty), while the SAME system with coefficients
pre-reduced into [0,p) returns a 487-element GB whose normalized
leading-monomial sequence is IDENTICAL to the char-0 GB
(/tmp/r1_25_redmod.out, p = 999999937). All mod-p screens MUST use
pre-reduced coefficient files (the emitted *_p<prime>.ms / wfree files
are already reduced and are fine). Any past mod-p verdict obtained by
editing the char line of a char-0 artifact is INVALID.

Corollary: char-0 nonemptiness of the (2,5) core is corroborated at an
independent random prime (999999937) with byte-identical LT structure;
the 487-elt char-0 GB is NOT a multi-modular artifact.

## 4c. Explicit nondegenerate point (mod p = 105337, fully verified)

Extraction: wfree model (radicals z,r3,A1,A2,EB specialized at the
standard radical point) + pins of the 27-coordinate independent set
{HW1,HW2,x0,x1,x5,x7..x28} at random values (seed 9000) => msolve
0-dim, rational parametrization deg 24 (= 6 x6-branches x 2 W1-signs
x 2 W2-signs); eliminating polynomial has 4 F_p-rational roots;
decode convention: coordinates = -C_i(theta) (denominator 1).
The decoded point satisfies ALL 66 sliced-wfree eqs, and after adding
the radical values it satisfies **ALL 44 equations of
systems/r1/r1_25chain_core.ms mod 105337** (independent parser):

r3=795, z=2779, A1=50630, A2=10114, W1=23639, HW1=45084, W2=91765,
HW2=44025, EB=24069, x0=78047, x1=4118, x2=38997, x3=62108, x4=104796,
x5=70788, x6=25856, x7=19242, x8=56813, x9=60455, x10=99802,
x11=104944, x12=22626, x13=59584, x14=47281, x15=65392, x16=56151,
x17=9245, x18=8510, x19=23563, x20=71386, x21=10008, x22=27029,
x23=25788, x24=41169, x25=72303, x26=53340, x27=58999, x28=84213,
s1=6114, cL=77575, t1=25826.

Nondegeneracy at the point: x0 != 0 (tie alive both sides), W1, W2,
s1, cL != 0, A1 != A2. (Banked: /tmp/full_point_p105337.pkl.)
Char-0 refinement: char-0 sliced run in progress; existence at char 0
is already certified by section 4 (Nullstellensatz).

## 5. Deferred-row evaluation at the point

Scope fact (variable census, xWG.pkl): the 12 deferred slot-pair
families involve W_G slots 10..20 whose entries contain **90 interior
variables beyond the core's 29** (slot 10: +8, slot 12: +34, slot 14:
+44, slot 16: +54, slot 18: +80, slot 20: +90), plus ~39 more f-side
vars in F5 slots 4..14, plus the quotient lead qL. The deferred rows
are therefore NOT functions on the core locus: at a core point they
form a FIBER SYSTEM in the interior unknowns. "Deferred rows vanish at
the point" is decided by the CONSISTENCY of that fiber system.

Construction (engine-exact, at the verified point, mod p = 105337):
specialize every xWG.pkl entry (core 29 + radicals pinned; interior
vars symbolic) — interior slots collapse to 105/437/745/1546/3198/4899
monomials (slots 10..20); f^5 slots 0..14 from blocks.pkl (truncation-
first, exact; 163 keys); W_G^2 slot S = sum over ordered pairs
(sa,sb), 6 <= sa,sb <= 20 (pairs with a partner slot < 6 vanish
structurally — the census is CLOSED for S <= 26); rows
(W_G^2)[n,S] - s1*F5[n,S-12] = 0 for S = 16..24 (ties r=4..12) and
= qL*pq46[n] at S = 26 (quotient, qL != 0 by R6 4.2 B').
Result: 142 rows, 91 unknowns (90 interior + qL), no constant row.

SOUNDNESS GUARD: the same assembly code applied to the EMITTED slots
S = 12, 14 (r = 0, 2) returns 41 rows ALL IDENTICALLY ZERO at the
point — the pipeline reproduces the banked core rows exactly.

**RESULT (fiber verdicts, msolve mod p, seconds each):**

| subsystem | point 1 (seed 9000) | point 2 (seed 7001, independent) |
|---|---|---|
| ties r = 4 (S=16) | consistent (GB 2) | — |
| ties r <= 8 (S<=20) | consistent (GB 11) | consistent (GB 11) |
| ties r <= 10 (S<=22) | **[1] INCONSISTENT** | **[1] INCONSISTENT** |
| ties r <= 12 | [1] | [1] |
| all 12 families + qL != 0 | [1] | [1] |

At BOTH independently sliced nondegenerate points the deferred fiber
is EMPTY, with the kill entering exactly at rung r = 10 (W_G^2 slot
22, pairs (6,16),(8,14),(10,12)). The deferred rows DO NOT vanish on
the core locus: they are genuinely discriminating. (Both fiber tests
are mod p = 105337 at specific points; two independent points and the
S=12/14 zero-guard make a slice artifact very unlikely, but the
char-0/global statement needs the farm emission.)

## 6. Verdict + consequences

Under the pre-registered table (SHEET6-R1 SS1, SS11):

1. **The (2,5)-chain core locus is REAL, not a degenerate artifact.**
   dim V = 27; the nondegenerate part (tie alive on both sides, W_i
   != 0, s1/cL units, A1 != A2, origin excluded) is NONEMPTY at char 0
   (Nullstellensatz certificate, 598-elt GB != [1]) and
   FULL-DIMENSIONAL (dim 27); all degeneracy strata are proper
   (dim <= 26). Explicit fully-verified nondegenerate points exist
   (SS4c; mod-p certificates at p = 105337, plus reduced-coefficient
   mod-p GBs at 105337 and 999999937 with LT structure identical to
   char 0). SS11's "not killed by the subset" verdict is UPGRADED:
   the 25-row core (all 37 emitted rows) is satisfiable
   NONDEGENERATELY, i.e. the formal candidate genuinely deepens at
   the core level.

2. **But the 12 deferred families bite — the branch's survival now
   hangs exactly there.** At two independent nondegenerate core
   points the deferred fiber system (levels r = 4..14 of the h2 tie/
   quotient, 91 unknowns) is INCONSISTENT, entering at rung r = 10.
   So V(core) is NOT the surviving locus: the true target is the
   proper closed subvariety V* = proj(V(core + 12 deferred families)),
   which excludes the generic core point. V* may still be nonempty
   (the deferred rows can trade against the 27 free moduli — 142 fiber
   rows vs 91 fiber unknowns leaves a 51-row load that the 27-dim base
   must absorb; not decidable by point sampling).

3. **Next phase (the campaign's counterexample frontier):** the farm
   emission of the deferred families, PRIORITIZED: rungs r = 4..10
   only (~1.7e8 of the ~2.0e9 term-pairs, i.e. <10% of the 9.4 farm
   sizing) already decide the generic-point kill observed here: if
   msolve on core + r<=10 rows returns [1] (char 0 or 2 good primes,
   REDUCED coefficients), the (2,5) branch DIES at level 2 and the
   verdict flips to a kill under the pre-registered table; if not, the
   surviving V* is the real candidate locus and the ladder (level-3
   band at 267/42, J-closure) applies to IT. The (1,2)/ninth-case and
   (2,3)-chain queues are unaffected.

4. Bookkeeping corrections banked: (i) SS11's "NONEMPTY at p=105337"
   is now established for the FULL system (reduced-coefficient GB, 487
   elts, LT-identical to char 0) — previously it rested only on the
   wfree screen; (ii) the msolve raw-coefficient mod-p hazard (SS4b)
   invalidates any past mod-p verdict obtained by editing the char
   line of a char-0 artifact; (iii) msolve -P 2 parametrization decode
   convention is x_i = -C_i(theta) with denominator [0,[1]] (SS4c).

## 7. Artifacts

- /tmp/r1_25_ndA.{ms,out}: nondegeneracy saturation (598-elt GB).
- /tmp/r1_25_degB.{ms,out}: tie-collapse stratum (39-elt GB, dim 25).
- /tmp/r1_25_red105337.out, /tmp/r1_25_redmod.out: reduced-coefficient
  mod-p GBs (487 elts each; LT sequence == char-0 GB).
- /tmp/full_point_p105337.pkl, /tmp/full_point2.pkl: verified points.
- /tmp/fiber.ms(+.out), /tmp/fib*.ms, /tmp/p2_*.ms: deferred fiber
  systems and verdicts at the two points.
- /tmp/lt25.txt, /tmp/ltA_leads.txt: parsed leading-term data.
- Char-0 sliced explicit-point run: /tmp/r1_25_pt.ms (msolve -P 2,
  small-int slice) TIMED OUT at 1500 s (0-dim char-0 parametrization
  in 41 vars is heavy); char-0 existence is independently certified
  (SS4), so nothing rests on it. A char-0 explicit point, if wanted,
  should be extracted by CRT/lifting the (cheap) per-prime wfree
  parametrizations across the round-trip prime family instead.
- Single-rung isolation runs (r=12-only, quot-only) were still in
  the msolve queue at write-up; the r<=8 / r<=10 bracketing above is
  complete and decision-grade.
