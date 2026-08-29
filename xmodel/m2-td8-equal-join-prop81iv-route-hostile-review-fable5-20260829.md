# Fable 5 hostile review — td=8 Prop. 8.1(iv) route certificate (Sol 5.6)

Lane: Fable 5, different-model adversarial referee. Date: 2026-08-29 UTC.

Target: `xmodel/m2-td8-equal-join-prop81iv-route-sol56-20260829.md`.
Packet: `cases/m2_td8_equal_join_prop81iv_r1_20260829/`.
Licensed sources read: the charged D2 route report
`xmodel/m2-td8-equal-join-route-family-sol56-20260829.md` and its
different-model review
`xmodel/m2-td8-equal-join-route-family-hostile-review-grok46-20260829.md`;
`refs/sigray_full.pdf` printed pp. 39–41 (Notation 8.1/Prop. 8.1) plus the
definition sites pp. 4, 13, 16, 41, 48 needed to pin the frame; promoted
`ladder/SHEET6-L1.md` (§§0–5), `ladder/SHEET6-A3L1-REVIEW.md` (front 6),
`cases/l1_ode_check.py`, `ladder/BOOK-OFFAXIS.md` §§6–7 (R1.0–R2.3),
`ladder/SHEET6-DEPTH.md` §§0–2 (i-normalized frames). No Opus or Grok
parametric-consumer output was searched for, listed, or read.

No web, AWS, commit, push, canonical edit, heavy CAS, long/high-memory
process, global `git status`, workspace-wide search, or `jc2-lean` access
of any kind. Arithmetic: hand algebra plus bounded exact `Fraction`
Python; all scratch in `/tmp`. Only this file was written.

---

## 0. Custody

Independently recomputed SHA-256:

```
aeb7714e656b7c112ce2933b48b6da6c18fdec3136b2d2651c44e6d9874c5584  target, full (7,556 bytes)
514a099191a4eb5df6ab8bace742f0d734afd33705132768306ac5600b2622b4  target, body (first 7,427 bytes,
                                                                  through the separator line) — matches
                                                                  the target's own body-hash line
89d739b09f15e0f03dc82bf1555d195337516b2199e4d0c082ced9e74901b1ed  td8_equal_join_prop81iv_r1.py
d4314f24fdbe375a37de0f66689ba7df341986d79837ce008d0907980acd92ad  test_td8_equal_join_prop81iv_r1.py
6317bc761e99b3bb189efc6ad29a871a15c310d5eda1bf9dfe7af8ea73a980f8  README.md
```

all matching the target's §1/§7. Charged route report full
`9a778862…`/body `bd35c43b…` (body = bytes before its separator; the
target uses through-separator — both conventions verified as stated),
Grok route review full `d3f378a1…`/body `a53a78db…` (first 20,342 bytes),
`refs/sigray_full.pdf` `9bf9f032…`, and the four comparison files
`ladder/SHEET6-L1.md` `69e6e4c1…`, `ladder/SHEET6-A3L1-REVIEW.md`
`dd25e00a…`, `cases/l1_ode_check.py` `e766bfe2…`, `ladder/BOOK-OFFAXIS.md`
`7679db8a…` all match the target's §1 prefixes.

---

## 1. Verdict

**`PASS_AT_LOCAL_PATTERN_SCOPE`**

Every displayed identity, admissibility condition, rigidity claim, and
forced root ratio was re-derived from scratch and holds exactly. Both
test modes replay at the claimed 5,031 checks. The frame identification
charged first is sound in the only sense Prop. 8.1(iv) can see (§2
below): the book pair `(X, kbar)` occupies the printed `(delta, 1−u)`
slots up to one common positive factor `kappa_F`, which the printed
right-hand symbol `⊖` absorbs, so the displayed identities are exactly
equivalent to the printed ones; their ratio matches the printed
requirement `delta/(1−u) = deg p/deg q` verbatim.

**Narrowest maximum consequence.** For every `t ≥ 0` the reviewed td=8
equal-join merge cell, and the two fixed neighbor cells `(21,15)` and
`(85,35)` on the recorded route, each admit an explicit admissible
reduced-pattern solution of printed Proposition 8.1(iv), rigid within
the reviewed cell shape up to the stated scale gauges. Hence no
vertex-local ODE/log-residue discriminator can remove this D2 family;
the completeness program must proceed through cross-vertex coefficient
compatibility, lambda-exactness, source landing, or a global argument.
This PASS authorizes canonical promotion of exactly that local formal
theorem and nothing else — no AWS, no landing, no realizability, no
exact lambda, no degree ceiling, no JC2.

---

## 2. Charge 0 — does the charged frame really identify `delta=X`, `1−u=kbar`?

**The printed (iv), glyph pinned.** `pdftotext` silently drops one glyph
after `=` in items (i)/(iii)/(iv) of Prop. 8.1 (a ~13 pt bbox gap; item
(v) has none). `mutool` stext maps it to U+2296 from `QSZEVB+CMSY10`,
and a 300 dpi render read visually confirms:

```
(iv)  δpq′ − (1 − u)p′q = ⊖p
```

Notation 1.1 (printed p. 4) defines it: "We use the symbol ⊖ for a
non-determined constant in C∗", with `⊖² = ⊖` and `c⊖ = ⊖` for
`c ∈ C∗`. So (iv) demands equality to *some nonzero constant* times `p`.
The target's explicit constants (`delta`, `42`, `204`) are instances;
"the right-hand constant is nonzero" is exactly the `⊖ ∈ C∗` demand.

**Slot normalization.** Printed: `u := π(F)`, `i := deg(p_F)/M_F^*`,
and `δ` is the ξ-exponent with `(ξ^δ p(η))^i = ⊖f_F^+`, so `δ = d_F/i`
(SHEET6-L1 §1, promoted). Book: `X := D_F/i` and `κ̄ := κ_F(1−π(F))`
(Not 9.1, p. 48; DEPTH §1; R1/R2 headers), where `D_F` is the *integer
κ-numerator* of the weight — Not 3.10 (p. 13) defines `h_F^+ = ξ^{j/κ}p_j`
with `D` the integer `j`, and St 9.1's printed proof (p. 48) converts
`d_F + d_{g,F} = 1−u` into `D_F + D_{g,F} = κ_F(1−u)`, i.e. `D = κ·d`.
Therefore

```
(X, κ̄) = κ_F · (δ, 1−u),   κ_F ∈ N* ("suitable").
```

The literal equalities `δ = X`, `1−u = κ̄` hold exactly iff `κ_F = 1`;
in general the identification is **ray-level**. That is harmless and
exact-as-used: multiplying (iv) through by `κ_F` gives
`X·pq′ − κ̄·p′q = ⊖p` with the same `⊖` (Notation 1.1(ii)), so the
solution set of the displayed identity equals that of the printed one.
Machine check: common rescales of the pair by `2`, `3`, `5/2` pass with
the rescaled constant; breaking the ratio (`2X` alone, or `κ̄+1`) kills
the identity for *every* constant. The ratio itself is printed twice:
St 8.2's proof (p. 41) states `deg(p)/deg(q) = δ/(1−u)` from (iv), and
the route's reviewed frames satisfy `X/κ̄ = dp/dq` at all three cells
(`(16+12t)/(6+4t) = (24+18t)/(9+6t)`, `7/5 = 21/15`, `17/7 = 85/35`).
Promoted precedent uses the same convention: `l1_ode_check.py` family C
solves (iv) at the `(42,126,7,3,5)` cell with ratio `ρ = 21/15` and free
constant, giving `B = (3/2)A` — reproduced by A3L1 front 6 and again by
the target's §6.1. **The charge-0 allegation fails: no displayed
identity is invalidated.** (Recorded as a LOW diction finding only.)

---

## 3. Charge 1 — affine merge identity, re-derived

With `R = η^{2ν}+1`, `p = R³`, `q = ηR`: `p′ = 6νη^{2ν−1}R²`,
`q′ = R + 2νη^{2ν}`, so for any `(delta, b)`:

```
delta·pq′ − b·p′q = R³·[delta + (delta(2ν+1) − 6νb)·η^{2ν}].
```

The η^{2ν} coefficient with `delta = 4ν`, `b = 2(2ν+1)/3` is
`4ν(2ν+1) − 4ν(2ν+1) = 0` — verified as a *polynomial identity in* `t`
over Q: `4(4+3t)(9+6t) − 6(4+3t)(6+4t) ≡ 0`. Hence LHS `= delta·R³ =
delta·p` exactly, with nothing nonconstant hidden by cancellation (the
quotient LHS/p is computed in closed form, not sampled). RHS
`delta = 16+12t > 0` identically. `b ∈ Z` iff `3 | 2ν+1` iff
`ν ≡ 1 (mod 3)`; `ν = 4+3t` is the `ν ≥ 2` slice of that class (DS1(a)
excludes `ν = 1`), matching the reviewed route. Independent dense-poly
replay of the full identity at 45 values including `t = 10^5`
(`ν = 300004`, `deg p = 1,800,024`): exact zero residual. The top-ratio
recovery `delta/b = 6ν/(2ν+1) = dp/dq` and the frame readings
`delta/dp = 2/3 = ρ_book` (ρ := D/deg p_full = δ/dp, DEPTH §1 — this
one is κ-free) and `(b − 2/3)/ν = 4/3 = w_tr` all check. **Confirmed.**

---

## 4. Charge 2 — two-orbit rigidity `A+B=0`

For the general shape `p = P(T)³`, `q = ηP`, `P = (T−A)(T−B) =
T²−σT+π`, `T = η^ν`, dividing by `(1−u)` and by `P³`:

```
r·P + ν(r−3)·T·P′,   r := delta/(1−u) = 6ν/(2ν+1).
```

`ν(r−3) = −3ν/(2ν+1) = −r/2` — re-derived, correct — giving
`r(π − σT/2)`. In the un-divided `(delta, b)` scale the T-coefficient is
`(A+B)·(−delta(1+ν) + 3bν) = −(delta/2)·σ`, whose σ-coefficient
`−delta/2 = −8ν... /` is nonzero for every `t` (machine-checked
symbolically). So within the reviewed cell shape the identity holds with
a nonzero constant **iff `σ = A+B = 0` and `π = AB ≠ 0`**, constant
`= delta·π`. All-and-only: confirmed by exact division at random
rational `(A,B)` — a constant quotient exists exactly when `σ = 0`.
Side conditions on the exhibit `P = T²+1`: roots `±i` distinct, nonzero,
*distinct ν-orbits* (a ν-orbit is determined by its T-value; `i ≠ −i`,
and in the general family `disc = −4π ≠ 0` — no orbit collision
anywhere in the solution set); each orbit has p-multiplicity 3 (the two
equal `(μ,w) = (3,2/3)` arrivals, reduced multiplicities per St 8.4
usage in the route), q-multiplicity exactly 1; `η ‖ q` and `p(0) = 1 ≠ 0`
(R1.0 root/eta laws); searrow `3dq = 6ν+3 > 6ν` and root-mult
`dp ≠ 3dq` strict. The shape itself (`ε = k = l_ex = 0`, `r₀ = 2`,
`q = η·rad(p)`) is forced by promoted R1.0/R2.2 at the reviewed cell
labels, so the rigidity computation covers the *entire* admissible
pattern space of this cell, not a subfamily. The `T²+1` exhibit is one
member of the `σ=0` family (existence is all the consumer needs; the
rigidity statement is computed gauge-free). **Confirmed.**

---

## 5. Charge 3 — both fixed consumers and the trunk

General two-orbit `p = (T−A)^{m_A}(T−B)^{m_B}`, `q = η(T−A)(T−B)`:
LHS/p is the quadratic-in-T bracket

```
[delta(1+2ν) − bν(m_A+m_B)]·T² + [−delta(1+ν)(A+B) + bν(m_A B + m_B A)]·T + delta·AB,
```

whose T² term vanishes exactly at the frame ratio (Cor 6.1 top
cancellation) — closed form verified by exact division at random
rational `(A,B)` for all five shapes used.

- **Incoming `(21,15)`** (`ν=7`, `m=(2,1)`, `(delta,b)=(7,5)`):
  T-coefficient `= (−21A + 14B)`; constant iff `2B = 3A`, i.e.
  `B/A = 3/2` — *forced*, reproducing promoted L1 family C / A3L1
  (`B=(3/2)A` unique over C). At `(A,B)=(2,3)`: `7pq′ − 5p′q = 42p`
  exact (`42 = 7·AB`). Degrees `(21,15)`, `gcd = 3 = M`; searrow split
  matches the recorded cell: chain orbit mult 2 searrow (`2·15 > 21`),
  extra orbit mult 1 northeast (`15 < 21`) — the priced
  `ceil(X−kbar)=2` escape; root-mult `21 ∉ {30,15}`; `dq ≡ 1 (mod 7)`.
  Swapped multiplicities (`m=(1,2)` on the same roots) are dead
  (T-coefficient `−35 ≠ 0`) — the mult-to-root assignment matters and
  the displayed one is the recorded one.
- **Trunk `(85,35)`** (`ν=17`, `m=(3,2)`, `(delta,b)=(17,7)`):
  T-coefficient `= (−68A + 51B)`; constant iff `3B = 4A` — *forced*. At
  `(A,B)=(3,4)`: `17pq′ − 7p′q = 204p` exact (`204 = 17·12`). Degrees
  `(85,35)`, `gcd = 5 = M`; chain mult 3 searrow (`105 > 85`), extra
  mult 2 northeast (`70 < 85`) — consistent with the route's general-gap
  price `ceil(17/2 − 7) = 2`; root-mult `85 ∉ {105,70}`;
  `35 ≡ 1 (mod 17)`. Swap dead (`−119 ≠ 0`).

Mutated root pairs (`(2,4)` with would-be constant 56; `(3,5)` with
255) leave T-terms `14T`, `51T`: no constant works — the packet's
mutation tests are genuine kills, not wrong-constant artifacts.
**Confirmed, including the forced ratios.**

---

## 6. Charge 4 — degree/gcd/frame matches; printed-condition sweep

Frames used are verbatim the reviewed route's: `(X,κ̄) = (16+12t, 6+4t)`,
`(7,5)`, `(17,7)`; degrees `(24+18t, 9+6t)`, `(21,15)`, `(85,35)`;
`gcd = 3` (`= gcd(3, 2ν+1)`, `ν ≡ 1 mod 3` — the target's residue
diction is correct here), `3`, `5`. Swept for a printed condition
outside the ODE that would make a pattern inadmissible: root law and
eta law (R1.0, derived from (iv) itself), semi-invariance (all patterns
are `T`-polynomials, resp. `η`·`T`-polynomial), searrow law (S), root-mult
law (R), `M = gcd(dp,dq)` (8.1(v)), `dq ≡ 1 (mod ν)` and
`gcd(M,ν) = 1` (R1.0/R2.2), Cor 6.1's deg-q pin (`dq = κ̄·dp/X` at all
three cells), St 8.2's continuation dichotomy at every root, arrival
divisibility `μ_e | M` (route tier, already reviewed), `ν ≥ 2`/DS1(a),
MP2 (`M ∈ {3,3,5} ≠ 1`). **Nothing printed excludes any of the three
patterns.** Note the off-residue behavior: at `ν ≢ 1 (mod 3)` the
identity (EJ) *still holds* with the rational `b = 2(2ν+1)/3` (verified
at `ν = 5`); those classes die by `κ̄`-integrality (DS1(c) typing), not
by the ODE — the packet correctly *refuses* them rather than claiming an
ODE kill, and no consumer may cite this packet as an ODE obstruction on
other residues.

---

## 7. Charge 5 — local solutions vs one global coefficient system

The exact distinction, re-derived: the three solution sets live in
*different* η-charts (`ν = 7`, `4+3t`, `17`) and are each rigid only up
to one scale gauge (`A` free with `B=(3/2)A`; `π ≠ 0` with `σ = 0`; `A`
free with `B=(4/3)A`). A single global coefficient system would in
addition require (a) transport of each incoming `(21,15)` gauge through
its case-II edge onto the merge's orbit values — print pins only degrees
and top coefficients at that tier (St 3.9; SHEET6-L1 §5 leaves the same
transport layer open at td=6); (b) the merge's two orbit values to be
*opposite* (`σ = 0`) simultaneously with both incoming transports; (c)
merge→trunk transport onto a `3B = 4A` pair. The target claims none of
this: §2 "not cross-vertex coefficient gluing", §6 "does not identify
their root parameters across vertices", §8 firewall "compatibility of
the four local gauges" unproved. **Distinction correctly drawn and
firewalled.**

---

## 8. Sought failure modes — all absent

- **Missing power of `i` / full-vs-reduced mismatch.** (iv) is stated
  for the *reduced* `(p,q)`; the book's `(dp,dq)` are reduced degrees
  (DEPTH §1: `deg p_full = i·deg p_red`; the route's degrees are
  reduced). The target's patterns have exactly the reduced degrees.
  Probe: substituting the full pattern `p²` (i.e. `i = 2`) for `p`
  kills the identity for every constant.
- **Illicit coordinate gauge.** None used: the exhibit is an existence
  witness; the rigidity computation is gauge-free over `(σ,π)`/`(A,B)`;
  the κ-common-rescale of the slot pair is licensed by `⊖` (verified).
- **Collision of the two ν-orbits.** Impossible on the whole solution
  set (`disc = −4π ≠ 0`); a forced collision (`A = B`) is refused by the
  packet and kills the identity directly (probe).
- **Nonconstant RHS hidden by cancellation.** Excluded in closed form:
  LHS/p is computed as an exact T-quadratic whose T² and T coefficients
  vanish identically (symbolically in `t`, resp. by the forced ratio),
  leaving exactly `delta·AB`.
- **Wrong-slot/ratio errors.** Ratio-break probes (`2X` alone; `κ̄+1`;
  η²-q; missing-η q; extra simple orbit appended to q) all dead.

---

## 9. Replay and independent fixtures

Packet replay (exact commands, from the packet directory):

```
python3 test_td8_equal_join_prop81iv_r1.py        →  TD8_EQUAL_JOIN_PROP81IV_R1_TEST_PASS checks=5031  (1.45 s)
python3 -O test_td8_equal_join_prop81iv_r1.py     →  TD8_EQUAL_JOIN_PROP81IV_R1_TEST_PASS checks=5031  (1.45 s)
python3 td8_equal_join_prop81iv_r1.py --t 0       →  ν=4, degrees (24,9,M=3), frame (16,6), RHS 16, all checks true
python3 td8_equal_join_prop81iv_r1.py --scan 1000 →  1,001 certificates, all checks true, last ν=3004
```

Check census recount: `1,003 t-values × 5 + 16 singles = 5,031` —
matches both modes. The suite's scan is `t = 0..1000, 10^4, 10^6` as
claimed; the target's replay block and the README's are both honored.

Independent fixture (`/tmp/fable5_td8_prop81iv_independent.py`, dense
exact polynomials, no packet imports, seed 20260829):
`FABLE5_INDEPENDENT_PASS checks=481` in 19 s — family identity at 45
t-values through `ν = 300004`, symbolic-in-t bracket and RHS
positivity, closed-form bracket verification for all five shapes at
random rational roots, iff-characterization of constancy by exact
division, forced-ratio and swap/mutation kills, κ-ray invariance,
ratio-break/full-pattern/η²/no-η/collision/zero-root/extra-orbit
probes, off-residue ODE-alive control, both fixed consumers with
displayed data, searrow/northeast splits, root-mult and `dq mod ν`
laws.

Packet code notes (no verdict impact): `certificate()` recomputes the
fixed consumers on every call (harmless); the booleans `affine_nu`
(tautological), `two_nonzero_nu_orbits` (`ν ≥ 2` proxy), and
`eta_simple_q_only` (fingerprint) are regression-tier and weaker than
their names — the proof burden sits in the report's §§3–5, as the
README itself states; `--scan 0` falls back to `--t` (falsy-zero
quirk, documented behavior unaffected).

---

## 10. Findings, severity order

No CRITICAL, HIGH, or MEDIUM finding. The theorem, its rigidity, both
fixed consumers, and the firewall all stand.

**LOW (normalization diction, no math impact).** "`delta = X` and
`1−u = kbar`" are literal equalities only when `κ_F = 1`; in general
`(X,κ̄) = κ_F·(δ,1−u)` (printed `D = κ·d`, `κ̄ = κ(1−u)`: Not 3.10,
Not 9.1, St 9.1's proof). The pair enters (iv) only through its ray
because the RHS is `⊖`, so every displayed identity is exactly
equivalent to the printed one. Suggested one-line erratum for the
promotion copy: "up to the common factor `κ_F`, absorbed by `⊖`".

**LOW (diction).** §4's "the nonzero RHS does not vanish at a root" is
a loose rendering of R1.0's order-μ★ coefficient condition
`δ − (1−u)μ★ ≠ 0 ⟺ dp ≠ μ★·dq`; the inequality actually checked
(`dp ≠ 3dq`, and its analogues implied by the identity at the fixed
cells) is the correct condition.

**NOTE (scope clarification, not a defect).** "The whole displayed
route survives the local ODE consumer" means the four Prop. 8.1(iv)-
scoped pattern vertices, as §6 states precisely. The two pole vertices
(`(Λ,a,b,ν) = (4,1,2,3)`, governed by the Prop. 5.3 pole-pattern ODE)
and the `(0,y)` terminal are outside (iv)'s scope and were not — and
did not need to be — solved here.

**NOTE.** Off-residue classes are excluded by `κ̄`-integrality, not by
the ODE (§6 above); the packet's refusal semantics are the correct
encoding.

---

## 11. Scope firewall

This review asserts nothing beyond the §1 consequence. In particular it
does not assert: exact lambda or that any recorded lower bound is an
exact cost; compatibility of the four local gauges or any cross-vertex
coefficient system; source landing; geometric realizability of any
member; completeness of the td=8 cell book; a degree ceiling; a Keller
map; or any JC2 conclusion. It does not authorize AWS or landing. No
canonical consumer may treat the two pole patterns or the terminal as
ODE-checked. Files written: this report only. Compute: the four replay
commands above, the `/tmp` independent script, hash recomputation, and
PDF glyph forensics (`pdftotext -bbox`, `mutool draw` stext + 300 dpi
render of printed p. 40, Notation 1.1 located on printed p. 4). No
`jc2-lean`, web, AWS, commit, push, global status, or workspace-wide
search.

**Verdict: `PASS_AT_LOCAL_PATTERN_SCOPE`.**

---
Report-body SHA-256 (bytes through the separator line above): d6e743dda2a613cd6264f4d36eb66ae15f00a4fdeda335281e72bc1955acf1b8
