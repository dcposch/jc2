# Hostile review — direct nested U2 `nu=1` boundary finiteness (Fable 5, 2026-08-29)

Reviewer: Fable 5, independent adversarial lane.
Target: `xmodel/m2-u2-nested-nu1-boundary-r1-sol56-20260829.md`.
Full-file SHA-256
`99bbe233f8f6f7273b2e5f89705aa5f2189681ce649a8723a66a0f99fa92912b`
(recomputed, match). Body SHA-256
`11e44767526044590b2f3ed8ceaed6b0aa3eaa98b30008e15bc725149d8b90cf`
(recomputed as all bytes before the final separator line, match).

## 0. Verdict

**`PASS_WITH_REPAIR`**

The theorem is correct at its recorded reduced local arithmetic/transport
scope: with fixed `(a,r,mu,R,ell)` and the direct case-I edge, the set of
`(L_inner,L_outer)` pairs satisfying the printed edge law, typing,
equal-weight, and T1 conditions is finite, effectively enumerated by
(B1)-(B2), and the unique edge-arithmetic resonance `K=R(r-1)` is
T1-dead by a correct, theorem-grade ODE lemma.  Every load-bearing
formula recomputes exactly; brute force confirms the enumeration is
complete at its reading; no infinite family was found under any reading
the source licenses.  Three repairs are required, none of which breaks
the result: the quoted general case-I rule is misprinted (W1), the
headline "T1-alive" naming misattributes the generic kill (W2), and the
note consumes `n_e in N*` as its central kill without recording the
BOOK-OFFAXIS stage-R policy rider that quarantines exactly that
condition from census kill-duty (P1 — the substantive one).

| charge | finding |
|---|---|
| 1 frames/quantifiers | PASS; frame-vs-slope distinction correct; bounds even `(mu,ell)`-free |
| 2 direct case-I edge | PASS with W1 (misprinted general rule) and P1 (stage-R rider missing) |
| 3 (E)/(D)/bounds/resonance | PASS; enumeration complete; resonance real and unique; no missed family |
| 4 ODE lemma | PASS, theorem-grade; 18/18 exact linear-algebra kills, controls alive |
| 5 equal-weight siblings | PASS; not needed for the theorem; hides no unbounded parameter |
| 6 filters / `ell` range | PASS; bounds are `ell`-free, so finiteness survives any `ell` set |
| 7 perimeter | PASS as scoped, once the P1 rider is added |

No landing, realization, gluing, panel, degree-ceiling, `G2`, or JC2
consequence is licensed; R4 (`alive != existent`) applies to every
retained candidate.

## 1. Provenance

Hashes recomputed byte-exact for the target (full and body, above) and
for all seven pinned dependencies:

- `ladder/BOOK-OFFAXIS.md` `7679db8a...` — match;
- `xmodel/m2-u2-nu1-unbounded-lex-primary-grok46-20260829.md`
  `9c20947b...` — match;
- `xmodel/m2-u2-nu1-unbounded-lex-primary-hostile-review-fable5-20260829.md`
  `e156f94c...` — match;
- `xmodel/m2-u2-terminal-finiteness-r1-repair-sol56-20260829.md`
  `3989703a...` — match;
- `xmodel/m2-u2-terminal-finiteness-r1-repair-hostile-review-opus5-20260829.md`
  `9a1775f6...` — match;
- `xmodel/m2-u2-first-p2-boundary-finiteness-r1-sol56-20260829.md`
  `8c46e6bf...` — match;
- `xmodel/m2-u2-first-p2-boundary-finiteness-r1-hostile-review-fable5-20260829.md`
  `1117357659...` — match.

Constraint compliance: no `jc2-lean` access, no `ideation-20260829T0820Z`
file read, no web/AWS, no canonical edit, no commit/push.  Desk checks
were short exact Python (`int`/`Fraction`) under `/tmp/nestedrev/`;
writes: this file only.

## 2. Charge 1 — the two U2 frames and the quantifiers: PASS

**Inner frame.**  `dp_in=r*mu`, `dq_in=r+L`, `E_in=mu*L`,
`kbar_in=a(r+L)/L`, `W=a(L+r-1)/L`, `M_in=gcd(r*mu,r+L)` is exactly the
transport confirmed at pattern scope by the pinned Fable review of the
lex primary (its §5, with `a=w`), which I re-derived independently from
R2.1 + Prop 9.3(b) and re-verified on 300 random exact tuples.

**Frame weight vs ODE slope.**  The target's sentence that
`rho_in=a/L` is not `dp_in/dq_in` is correct and is precisely the
conflation repair (R2) of the pinned lex-primary review: the frame value
is `rho = X/dp = kbar/dq = a/L` (P1 case-IV normalization), while the
ODE slope is `r*mu/(r+L)`.  The consistency identity
`w_e = kbar_in - rho_in = a(L+r-1)/L = W` at `nu_in=1` (verified
exactly) is what makes the same state legally carry `kbar_in` in the
edge law and `W` in the outer equal-weight frame — the identification
the target's §6 asks the reviewer to check.  It checks.

**Outer frame.**  The outer merge is hypothesized to be of the same
reviewed U2 shape, so the frame is the same normal form under
`(r,mu,w,L) -> (R,ell,W,K)`: `dp_out=R*ell`, `dq_out=R+K`,
`E_out=ell*K`, `kbar_out=W(R+K)/K`, `M_out=gcd(R*ell,R+K)`,
`w_out=W(K+R-1)/K` (this last recomputes as
`kbar_out*(dq_out-1)/dq_out`, matching P2's trunk-start law).  Arrival
count (`r`,`R` = places, the `Rad` roots), multiplicity (`mu`,`ell`),
and extra degree (`L`,`K` = `deg S`) are kept distinct throughout; no
places/series conflation found.

**Quantifiers.**  Fixed `a=A/B>0` lowest terms, `r>=2`, `mu>=1`,
`R>=2`, `ell>=1`; varying `L,K in N*`.  As stated.  A strengthening the
target half-claims and fully earns: `kbar` frames are multiplicity-free
(`mu` and `ell` cancel in `kbar = mult*w*dq/E`), so (E), (D), (B1), (B2)
are independent of both `mu` and `ell`; the finite bound depends only on
`(a,r,R)`.

## 3. Charge 2 — the direct case-I edge: PASS with W1 and P1

**Case typing.**  BOOK-OFFAXIS R2 (§7): non-0 arrivals at a merge in
`V_{2,a}\V_{1,a}` are case I, and the reviewed U2 regime (Not 3.4)
forces `nu=1` exactly there; U2 arrivals are nonzero by shape.  So the
direct edge is case I.  Moreover R2.1 states one law for case-(I)/(II)
edges jointly, so even the I-vs-II typing is not load-bearing for (E).

**The rule, as printed in the source (W1).**  R2.1:
`kbar_G = (kbar_e + n_e)/nu_e`, eliminating
`n_e = nu_e*kbar_G - kbar_e in N*`.  At `nu_e=1` this is
`kbar_out = kbar_in + n`, which is what the target's derivation actually
uses.  But the target's displayed general rule
`kbar_out = kbar_in + n/nu_in` is NOT the R2.1 form for `nu_in>1`
(R2.1 divides the whole sum by `nu_e`).  Harmless in this proof, and
dangerous for the announced successor (the intervening-P0-chain case,
where the arriving trunk vertex has `nu>=2` by DS1(a)).  Repair W1: fix
the display to `kbar_out = (kbar_in + n)/nu_in`.

**No omitted term.**  Prop 9.3(c),(d) i-normalized give exactly two
laws; their elimination `X_G = mu_e(kbar_G - w_e)` is already consumed
in deriving the outer frame, and the residual content is exactly the one
scalar `n_e in N*`.  I found no second correction term, no orientation
ambiguity (R2.1's `G` is the downstream merge; a reversed reading is not
licensed, and — checked anyway — would still give finiteness: `n<0`
forces `L<a` and then `K` is determined per `(L,|n|)`).

**Direct-edge grammaticality.**  Inner-merge-child arrivals are recorded
grammar: the BOOK-OFFAXIS §3 census assigns inner arrivals
`mu_e | emitted M` (= the target's `ell | M_in`), §9's survivor anatomy
names "nodes with inner-merge arrivals" with the child `w`-formula, and
the pinned lex-primary review's R4 discussion prices exactly such
arrivals.  No printed clause mandates an intervening chain vertex.  The
target's own §6 fallback (replace (E) by the chain's terminal-frame
formula if a mandatory edge is found) is the correct guard and stays.

**P1 (the substantive repair): `n_e in N*` as a kill vs the stage-R
policy.**  The entire generic kill in this note is `n in N*` (T1 kills
only the resonance line; see §4 below).  BOOK-OFFAXIS §10's honesty
rider (ii) states: "`n_e in N*` and i-sync are never used to kill
(stage-R policy kept)", because `n_e`'s integrality rides on the
i-normalization `deg(p_{H_e}) = i_G*mu_e` and `i` is frame-blind at
census tier.  The lex primary explicitly inherited this rider; the
target never mentions it.  R2.1 is PROVED and listed as
review-confirmed in §10's trust perimeter, so consuming `n_e in N*` at
printed-lemma tier is legitimate for a reduced local arithmetic
statement — but the result then carries an obligation the note omits:
its finiteness verdict must not be fed into stage-R/P5 census verdicts
(or any consumer honoring the policy) as kills without first certifying
i-sync on this specific edge.  Repair P1: add the rider explicitly, and
state that the enumeration's kills are R2.1-tier, not census-tier.

## 4. Charge 3 — (E), (D), bounds, resonance, and the family hunt: PASS

**(E).**  `n = kbar_out - kbar_in = W(R+K)/K - a(r+L)/L` with
`W = a(L+r-1)/L` gives `(a/(LK))[(L+r-1)(R+K) - K(r+L)]
= a[R(L+r-1)-K]/(LK)`.  Re-derived by hand and verified on 300 random
exact tuples.  Equivalently `n = WR/K - a/L`, the form that makes the
frame consistency of §2 visible.

**(D).**  Clearing `a=A/B`: `L(BnK - AR) = A(R(r-1)-K)`.  Exact.  No
integrality of either individual `kbar` is used — correct, and worth
keeping, since `kbar in Q` is the legal case-I regime.

**Positivity and (B1)/(B2).**  `n>=1` gives `K(L+a) <= aR(L+r-1)`;
`(r-1)(L-1)>=0` gives `L+r-1 <= rL`, hence `K < aRr` strictly
(`L/(L+a)<1`), and `n < aRr/K` strictly (the `-a/L` term).  Both bounds
verified against every brute-force solution found below.

**Enumeration completeness.**  For each enumerated `(K,n)`:
`D = BnK-AR`, `N = A(R(r-1)-K)`; `D!=0` gives the sole candidate
`L=N/D`; `D=0!=N` empty; `D=N=0` iff `(RES)` `K=R(r-1)`,
`n=A/(B(r-1))` (with `B|A` forcing `B=1`, so the resonance exists only
when `(r-1)|a` in `N*`).  Desk check: exhaustive brute force over
`1<=L,K<=300` on seven tuples
(`a,r,R`) in {(2,2,2),(3/2,2,3),(2,3,2),(5/3,3,2),(1/2,2,2),(4,2,4),
(3,4,2)} matches the grid procedure exactly after removing the resonant
column; the resonant column, when `a/(r-1) in N*`, contains every `L`
in the window (e.g. all 300 at `(2,2,2)` with `(K,n)=(2,2)`), i.e. the
resonance is a REAL infinite edge-arithmetic family and the ODE lemma is
genuinely load-bearing, not decorative.  In every resonant instance
`R | K=R(r-1)` holds, as claimed.

**Missed-family attempts (all dead).**
- `n=0` reading: not licensed (`n_e in N*` in R2.1), but even if it
  were, `n=0` forces `K=R(L+r-1)`, a multiple of `R`, so the lemma
  kills the entire would-be family.  A free robustness strengthening
  the target does not claim.
- Reversed orientation: `L<a` bounded, `K` determined per `(L,|n|)`,
  finite (and unlicensed anyway).
- `ell` or `mu` varying: (E) is free of both; no effect.
- Sibling extra degrees `J` on the `a=b` synchronized ray: pinned by
  `L` (see §6); `a!=b` siblings: (EW2)-finite.
- Larger windows: (B1) caps `K` independently of `L`; nothing grows.

## 5. Charge 4 — the `R|K` lemma: PASS, theorem-grade

Statement re-proved by hand: `deg P=R>=2`, `K=mR`, `m>=1`, char 0; no
degree-`K` polynomial `S` and constant `c!=0` with `RPS'-KP'S=c`.
- The operator `T(S)=PS'-mP'S` annihilates `P^m`: exact.
- `T0=S-(lc(S)/lc(P)^m)P^m` has `deg T0<mR` strictly (leading terms
  cancel identically) and `T0!=0` since `T(T0)=c/R!=0=T(0)`.
- For `d=deg T0`, the coefficient of degree `R+d-1` in `T(T0)` is
  `lc(P)lc(T0)(d-mR)!=0` (as `d<mR`), and `R+d-1>=R-1>=1`; the `d=0`
  case (`T0` constant, `T(T0)=-mP'T0`) is covered by the same formula.
  One subtraction suffices; no iterated descent is needed.
- Characteristic zero is used twice (`d-mR!=0` as a scalar, `R`
  invertible) and is the recorded scope.  Repeated roots, non-monic
  `P`, and arbitrary coefficients are all covered — the proof never
  touches root structure, so T1-death holds for EVERY `Rad_out`, which
  is what killing a merge shape requires.

Desk check: exact `Fraction` linear algebra on the coefficient system
`RPS'-KP'S=1`, `deg S<=K` (note: a superset of the stated `deg S=K`),
for `R in {2,3,4}`, `m in {1,2}`, and for each `(R,m)` a power shape,
a fully repeated-root `(t-3)^R`, and a non-monic random `P`: 18/18
insolvable.  Positive controls: `R=2`, `K in {1,3,5}` and `R=3`,
`K in {1,4}` on power shapes are solvable — matching the reviewed
odd-`L`/`L≡1 (mod r)` survival record, so my checker is not
vacuously failing.

**Consistency with the absorbed record.**  The pinned lex-primary review
recorded universal (all-shapes) death only at `K=R` and power-shape-only
death at `R|K`; at `R=2` its parity iff already gives all even `K`
universally dead.  The lemma subsumes all three and extends to every
`m>=1` and every `R>=2`.  The target's sentence "every positive multiple
`K` of `R` is universally dead, not merely `K=R`" is an accurate
description of the strengthening.  The resonant `K=(r-1)R` is such a
multiple, so (RES) is T1-dead: correct.

## 6. Charge 5 — equal-weight siblings: PASS; not needed; hides nothing

(EW0): `a(L+r-1)/L=b` has no solution for `b<=a` (since `W>a` strictly)
and the single candidate `L=a(r-1)/(b-a)` otherwise: exact.
(EW1)->(EW2): the factorization
`((a-b)L+a(r-1))((a-b)J-b(s-1))=-ab(r-1)(s-1)` is an exact identity
modulo (EW1) (verified symbolically, 300 random tuples); with `r,s>=2`
the right side is a fixed nonzero rational, both factors become fixed
integers after clearing the fixed denominators, neither factor can
vanish, and each linear form is injective in its variable — finitely
many `(L,J)`.  `a=b` gives the synchronized ray `(r-1)J=(s-1)L`: exact.

**Is §3 needed?**  No — and the target says so ("without needing to
assume that any sibling is fixed"): (E) is derived from the outer U2
frame (which needs only the equal-`(ell,W)` hypothesis, itself forced by
R2.1(i) for a U2 merge) plus the selected edge; sibling identities never
enter.  **Does it hide an unbounded parameter?**  No: on the only
surviving ray (`a=b`), `J` is a fixed multiple of `L`, so pinning `L` by
(E)/(D) pins `J`; unequal bases are (EW2)-finite; fixed-weight (chain)
siblings give at most one `L` each from a finite alphabet.  A deeper
sibling whose own base data varies is excluded by the fixed-base-data
scope, and the target's §6 first bullet says so.  The same inner state
feeding several outer places imposes the same (E) — no new freedom.

## 7. Charge 6 — filters and the `ell` divisor range: PASS

`ell | M_in` is St 8.4 (`mu_e | M_{H_e}`) and is literally the census
grammar for inner arrivals ("inner `mu_e` | emitted `M`",
BOOK-OFFAXIS §3); its expansion `ell | r*mu` and `L ≡ -r (mod ell)` is
exactly `ell | gcd(r*mu, r+L)`: correct.  `M_out>=2` is interior MP2.
All four typing conditions only thin, as claimed.  Decisively: (B1),
(B2), (D), and (E) contain no `ell` (and no `mu`), so the reduced
`(L,K)` finiteness survives `ell` ranging over its licensed divisor set
— which is finite, `ell<=r*mu` — and would survive any range
whatsoever.  The claim "changes none of the bounds" is exact.  The T1
filters consumed are the two reviewed U2-ODEs (inner `(r,L)`, outer
`(R,K)`) plus the new lemma; nothing else is smuggled in.

## 8. Charge 7 — maximum safe consequence and sharp perimeter

Safe to promote, with the P1 rider attached:

1. **Direct-edge two-parameter finiteness** (the theorem): for fixed
   `(a,r,mu,R,ell)` (or `ell` over any subset of its licensed
   divisors), the pairs `(L_inner,L_outer)` satisfying R2.1's case-I
   edge law, the U2 typing/equal-weight conditions, and T1-aliveness of
   both merges form a finite set, computed by the (B1)-(B2)/(D)
   enumeration; the sole edge-arithmetic escape `(RES)` is T1-dead.
   Kills are at R2.1-printed tier; not census-consumable without
   i-sync certification (P1).
2. **The `R|K` universal-death lemma** as a standalone strengthening of
   the U2 transport record (all shapes, all multiples, char 0).
3. The equal-weight sibling trichotomy (§3) at first level.

Not established, correctly firewalled by the target's §6 and re-affirmed
here: recursive/nested variation of `(a,r,R)`; any configuration with a
nonempty P0 chain between the merges (the announced successor; W1's
corrected rule form will be needed there, since trunk vertices have
`nu>=2`); existence/realization of any retained candidate (R4);
full-cell finiteness, neutral-index control, landing, gluing, St 3.9,
panels, degree ceilings, `G2-PSC`, `G2-BD`, JC2.  The intended "first
nested boundary" of the campaign, per the pinned first-P2 note's §6, is
the general first-boundary problem; this note closes its direct-edge
slice only, and says so.

## 9. Required repairs

- **W1 (wording, blocking for the successor):** the displayed general
  case-I rule must read `kbar_out = (kbar_in + n)/nu_in` (R2.1), not
  `kbar_out = kbar_in + n/nu_in`; identical at `nu_in=1`, divergent on
  the intervening-chain successor.
- **W2 (wording):** §0's "the set of T1-alive pairs ... is finite" —
  the finite set is the (edge-law ∧ typing ∧ equal-weight ∧ T1)-alive
  set; T1 contributes only the resonance kill.  §1 already lists the
  hypotheses separately; align §0.
- **P1 (perimeter, substantive):** record the stage-R policy rider:
  the note's generic kill is `n_e in N*`, which BOOK-OFFAXIS §10(ii)
  quarantines from census kill-duty; state that the result is
  R2.1-tier and identify what would lift it to census tier (i-sync
  certification for direct inner-merge arrivals).

## 10. Desk-check record

`/tmp/nestedrev/check2.py`, exact `int`/`Fraction`, no CAS, no caps:
lemma insolvability 18/18 with 5 positive controls alive; enumeration
vs brute force on `1<=L,K<=300` for 7 `(a,r,R)` tuples — exact match
after removing the resonant column; resonant column full (every `L`)
exactly when `a/(r-1) in N*`, empty otherwise; (B1)/(B2) hold on every
brute-force solution; (E), `w_e=kbar_in-rho_in=W`, `w_out`, and (EW2)
identities on 300 random tuples each.  Source lines consumed:
BOOK-OFFAXIS R2/R2.1 (§7), R1.2/R1.4 (§6), §3 census grammar line
("inner `mu_e` | emitted `M`"), §9 survivor anatomy (ii), §10 P0/P1/P2
and honesty riders (i)-(v), §11 ZCH context; pinned reviews as listed
in §1.

## 11. Cheapest next discriminator

Certify or refute i-sync on the direct U2-to-U2 edge: produce the
printed citation chain grounding `deg(p_{H_e}) = i_G*mu_e` for an
inner-merge-child arrival (the merge analogue of R1.2's
St 8.3(ii) + Prop 8.1(i) grounding for chains, plausibly via the
St 3.17(i)-style chain pin already used in the td=8 parametric review).
One desk session; if it lands, P1's rider is dischargeable, the
enumeration's kills become census-consumable, and the same license
covers the successor note.  Independently of that, the successor itself
(one clean P0 step between the merges, terminal frame substituted into
the corrected W1 rule) is the next content step and will reuse
everything verified here.

No web, AWS, heavy computation, canonical edit, `jc2-lean` access, or
ideation-file read occurred.  This file is the only write.

---

Report-body SHA-256 (all bytes before the separator line above):
`0fcd5675bee9a8a10562507ceaa40cd8518e601759956235f63ae91b012ec3d5`.
