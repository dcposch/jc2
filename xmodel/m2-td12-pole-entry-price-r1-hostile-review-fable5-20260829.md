# Hostile review: td=12 pole-entry price r1 (POLE-EXIT-ZERO)

Reviewer: Fable 5, different-model hostile review.  Date: 2026-08-29 UTC.
Charge: adversarial, independent verification of the Sol 5.6 primary desk
audit; instructed not to accept the conclusion from older campaign echoes.

## 0. Verdict

**PASS.**

All six charged load-bearing points are confirmed against the literal
source and the promoted repairs.  The universal lemma `POLE-EXIT-ZERO` is
correct and, on inspection, overdetermined: three independent source-level
mechanisms each close it.  Every attempted counterexample within the
reviewed source grammar fails.  The findings below are documentation-level
and non-blocking; none touches a mathematical claim, so no repair is
required for the result to stand.

## 1. Provenance and custody

Target:

```text
8fd4d1d01bcb082b6f7dfd0ccb91cee072a1e7e2fdb6a319c099075b0b39a9de  (full)
9fcc2c5c1f987189cc1eaf0dcc98a6748da4b6ba4a67b2969c24f05340e1dcd7  (body)
  xmodel/m2-td12-pole-entry-price-r1-sol56-20260829.md
```

Both hashes recomputed and matched; the body convention (bytes before the
final separator line) reproduces the pinned value exactly.  Repository
basis re-verified: HEAD `cd770c92e8307cffe82e985e54ba99abf6713459`, equal
to the target's pinned basis.

All eight pinned inputs from the target's Section 1 were re-hashed and all
match byte-for-byte: `refs/sigray_full.pdf` (`9bf9f032...`), the
Proposition-5.1 forced-puncture-shift coordinator integration
(`11059166...`), the Section-7 full independent audit (`0159cdf1...`) and
its GPT5 hostile review (`af1ce600...`), the multipole selected-orbit
attachment coordinator integration (`c74fc0f9...`),
`ladder/SHEET6-A2P-REVIEW.md` (`859ff057...`), and the td=12 U1
trunk-consumer primary (`599e2a91...`) and Opus5 hostile review
(`91b36515...`).

One additional named dependency was read and hashed for this review
because the target discusses it without pinning it (finding F1):

```text
7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77
  ladder/BOOK-OFFAXIS.md   (Section 2 read)
```

Primary-source pages 25--27, 36, and 48--50 of `refs/sigray_full.pdf` were
re-read from page images, avoiding the known stacked-fraction and
dropped-glyph extraction hazards; text extraction was used only to locate
Notations 3.14, 5.1--5.2, 6.1, 7.1, 8.1, Statements 3.15, 3.18, 5.1, and
Propositions 4.2, 5.1.  No web, no AWS, no heavy computation (one small
exact-arithmetic desk script).  The separately owned formalization
repository was not accessed, listed, searched, built, or touched in any
way.  No canonical file, source packet, or the target was edited; nothing
was committed or pushed.

## 2. Charge 1 --- same-puncture witness in literal Notation 9.3: CONFIRMED

Literal Notation 9.3 (p. 49):

```text
Y(F) := {H in T_(a,cv) :
         exists P in Rbar_a\R_a :  F = I_P(u)  and  H = I_P(pi(H))},
lambda_F := sum_(H in Y(F)) kappa_H(pi(H)-1).
```

One existential puncture `P` binds both conjuncts, so the pole flag and
the critical-value flag lie on the ray of the same puncture; there is no
reading under which the witnessing punctures differ.  The variable `u` is
not free in effect: `F = I_P(u)` forces `u = pi(F)` because the height
projection is well defined on the quotient tree (Notation 3.1).

The typing gate holds: Notation 9.3 requires `F in V_a intersect
T_a^searrow`.  Pole vertices satisfy `F in V_a` by Proposition 5.3(iv).
For the searrow half, Statement 9.1's proof gives the Proposition 4.1
equality `d_F + d_(g,F) = 1 - u` at pole flags (the `m_F = 0` bracket
`J(f^+,g^+) = xi^(-u)` is nonzero); with `d_F > 0` (Notation 5.2) and
`d_(g,F) > 0` (Proposition 5.3(ii)) this forces `u < 1` and then
`d_F = (1-u) - d_(g,F) < (1-u) <= (1-u) deg(p_F)`, i.e. `F in
T_a^searrow` by Notation 6.1.  The Section-7 audit derives the same
membership via `d_g/d_A = beta/alpha` and `alpha/(alpha+beta) < 1 <= deg
p_A`; I recomputed `2/5 < 1` for this row.  The source itself consumes
this typing at Statement 9.5, which feeds `F_0 = F in T_(a,pole)` into
Statement 9.4's `V_a intersect T_a^searrow` sum.

Propositions 5.5 and repaired 7.2 both quantify over the same universe
`P in Rbar_a \ R_a` on the fixed fibre, and `g` extends to a single-valued
meromorphic function on the compactification, so `g(P) = infinity` and
`g(P) in C` are genuinely mutually exclusive.  The contradiction in the
target's Lemma proof is real.  Heights are unproblematic: `pi(F) in Q^+`
(vertices at height 0 are excluded by 5.3(i)) and `pi(H) > 1` (Statement
7.1), so both "exists u in Q^+" hypotheses are met.

## 3. Charge 2 --- pole-set non-leakage repair preserves the Proposition 5.5 identification: CONFIRMED

The promoted Proposition-5.1 integration proves the sidedness theorem

```text
g(P)=infinity <=> F_P^* in T_a^+,      g(P) in C <=> F_P^* in T_a^-,
```

with `F_P^*` never in `T_a^0`, and explicitly derives

```text
T_(a,pole) = {F_P^* : P a puncture} intersect T_a^+
           = {F_P^* : g(P) = infinity},
```

stating that Notation 5.2, Propositions 5.3--5.8, `Lambda(P)`,
`Lambda(F)` and the pole entry book are unchanged, and that at a pole
`b_P = 0`, `B_P = g`, with `h_0 = g`, `m_F = 0`, `M_F`, `Q(F)`,
`Lambda(F)` all literal.  This is exactly the `T_(a,pole)`
identification Proposition 5.5 needs.  The only typing exception the
integration records is the unique intermediate `d_A = 0` flag, which is
never `F_P^*` and in particular never a pole vertex; there is no fibre
exception (everything is on the fixed fibre `R_a`) and no endpoint
exception.

I additionally verified a flag-intrinsic second route that removes any
per-puncture threshold dependence: at a pole vertex, `p_F` and `p_(g,F)`
have no common root (Proposition 5.3(vi)) and `d_(g,F) > 0` (Statement
5.1 with `d_F > 0`); both facts are properties of the flag alone, so the
corrected Statement 3.15 value dictionary (the audited (i)/(iii) swap:
positive order means value infinity here) gives `g(P) = infinity` for
*every* puncture `P` whose ray passes through the pole vertex.  A third
route: on any pole ray `d_(g)` is strictly positive at every flag ---
`(l/k) d > 0` below the star by 5.3(viii), and constant `= d_(g,F) > 0`
above it by the 5.3 proof (`deg p_(g,G) = 0`, `d_(g,G) = d_(g,F)`) ---
while a critical-value flag needs `d_g = 0` (Notation 7.1).  So no cv
flag can sit on a pole ray at all.  The Lemma is overdetermined.

On the Proposition 7.2 side, the Section-7 audit proves `(7.2-r)`:
`g(P) in C` iff the ray of `P` contains a critical-value flag, from the
centred threshold and the leading-bracket equation, exactly as the
target reports.  The GPT5 hostile review of that audit is "VERIFIED"
with material qualifications that concern the Proposition 7.3 /
Notation 7.3 indexing, the countermodel's analytic category, and the
Euler resolved-direction lemma --- all downstream of 7.2; the review
raises nothing against `(7.2-r)` and consumes it in its own
coordinate-free cluster repair.  The target's tier framing (a consumer
refusing campaign repairs must label `(PZ)` conditional on printed
Proposition 7.2, not "unknown in both directions") is right; SHEET6
already recorded the printed-supported chain.

## 4. Charge 3 --- the selected first-separation replacement is also empty at poles: CONFIRMED

Under the promoted attachment/MFE lemma, each selected positive exit at a
base vertex has a Statement-7.3 cv witness "attached uniquely at its base
vertex," and the witness puncture realizes a corrected-Statement-3.18
direction at that vertex.  By the very construction of `F * c` (Notation
3.8), the realizing puncture `P` satisfies `F = I_P(pi(F))`: it cannot
avoid the base flag.  At a pole vertex the same value contradiction then
kills any candidate witness (`F` on the ray forces `g(P) = infinity`;
the cv flag forces `g(P) in C`), so `D_F^exit` is empty and
`lambda_F^exit = 0`.

The pole-endpoint branch from the attachment repair does not reopen
this.  When the pole segment ends at `F` (`u = v_j`), a puncture may
have contact exceeding `u`; but any such actual puncture passes through
`F` itself and is therefore a pole puncture, which cannot carry the
Statement-7.3 witness.  The abstract contact continuation beyond the
truncated union is never an actual finite-valued ray through a
`T_(a,pole)` vertex.  The target's disposal of this branch, and its
remark that the attachment theorem's selected set only shrinks, are both
correct.

## 5. Charge 4 --- the `(1,2,3)` row and its exhaustion: CONFIRMED

Recomputed exactly, in agreement with the target and the pinned primary
(`poles (a,b,nu)=(1,2,3)^3`, `Lambda=(4,4,4)`, `M=[2,2,2]`):

```text
(D_F, D_(g,F)) = (2,3),  (deg p_F, deg p_(g,F)) = (4,6),  nu_F = 3,
M_F = 2,  kbar_F = 5,  rho_F = 1/2,  w_F = 3/2,  Lambda(F) = 4.
```

One note (F2): Notation 8.1 defines `M_F` as the gcd over the full
`h`-ladder, so `M_F = gcd(4,6)` needs `m_F = 0` at pole vertices; that
is true (pole vertices are star flags) and is stated verbatim in the
pinned integration ("the printed `h_0=g`, `m_F=0`, `M_F`, `Q(F)` and
`Lambda(F)` are literal"), but the target leaves the step tacit.

Form forcing: Statement 5.2(ii)'s first alternative fails (`3 !| 2`,
`3 !| 5`) and its second holds (`3 | 3`, `3 | 3`); Proposition 5.4(i)
fails on degrees (`4 != 0 mod 3`) and 5.4(ii) fits (`4 = 1 mod 3`,
`6 = 0 mod 3`), so `p_F(eta) = eta p^*(eta^3)` with `deg p^* = 1`.
Squarefreeness (5.3(v)) forces the constant term nonzero, giving
`p_F = eta(eta^3 - A)`, `A != 0`, up to scalar --- exactly two effective
root orbits (`c = 0` and one `mu_3` orbit), by corrected Statement 3.18
realized as exactly two punctures through `F`.  A third puncture through
`F` is impossible: two punctures sharing a direction would separate at a
vertex strictly above `F` on the ray, contradicting 5.3(ix)
(`I_P((u,infty]) intersect V_a = empty`).  Formula (18) gives orders
`3/3 = 1` and `3`; the sum `1 + 3 = 4 = Lambda(F)` matches (19) with
zero residue, so no unaccounted puncture or hidden orbit exists.
Roots of `p_(g,F)` off `p_F` (all of them, by 5.3(vi); in particular
`q(0) != 0`) admit no `F * c` and hence no tree direction (Statement
3.18), and none of this affects the Lemma anyway, since every puncture
through `F` is a pole regardless of direction.  The exhaustion stands.

## 6. Charge 5 --- pole vertex versus interior off-axis child; the `+3`: CONFIRMED, a typing regression

`BOOK-OFFAXIS.md` Section 2(c1) was re-read in place.  Verbatim it
concerns "segment vertices in `V_(2,a)`" of off-axis chains: for
`M >= 2` the printed record does not exclude such interior separating
vertices, so *chains* can carry `Y(F) != empty`, with no positive lower
bound printed either.  The target's paraphrase (interior merge-free
segment vertex below a pole; a finite puncture may share the lower flag
and split away before reaching the pole vertex, so Proposition 5.5 does
not force it to be a pole) is faithful and identifies the correct
mechanism for why the interior uncertainty is genuine.

The pole vertex is a different object: sharing its flag is already the
hypothesis of Proposition 5.5, so no escape exists there, independently
of `b_e`, `M`, `w`, or `V_(2,a)` membership (the pole vertex here is in
fact in `V_(1,a) intersect V_(2,a)`, and both of its separating
directions are pole directions).  The Opus review's Section 6.2/9 step
applied (c1), the Section 3 "UNKNOWN in both directions" budget line,
and the MP5/MP8 `b=1` perimeter to the three pole vertices themselves;
given `POLE-EXIT-ZERO` that application is refuted, and the symmetric
`+3` at the pole vertices is not a mathematical possibility within the
reviewed source grammar.  The prior Opus question was legitimate to pose
at its tier, but its object was mistyped --- the imported uncertainty
belongs to interior chain vertices, which the reviewed route does not
even instantiate (the P2 arrival law licenses zero-length pole chains,
as the Opus review itself recorded).  If a longer entry route ever
inserts an interior child, that child's price is genuinely open and
needs its own `Q`-datum, exactly as the target's Section 5 says.

## 7. Charge 6 --- consequence perimeter: CONFIRMED

The derived consequence is exactly `(6)`: the three pole contributions
are zero, so no base charge changes the reviewed first-trunk budget.
The quoted numbers match the pinned Opus review: charged cell
`(2/3,3)@nu_F=25` floor `8`, ceiling `9 = 12 - 1 - 2`, possible exact
charge `{8,9}`; sibling `(3/4,4)@nu_F=17` with `lambda = 8`, `psi = 3`,
budget `8`, slack `0`, hence floor and ceiling both `8`.  The merge
price `lambda_G = 0` is separately derived (Opus Theorem B, `eps = 0`,
`k = 0`).  The target claims only `FAMILY_SURVIVES_FIRST_TRUNK`
strengthening and explicitly disclaims source/polynomial realizability,
landing, a td=12 panel exclusion, a counterexample, and JC2, in
Sections 0, 6, 7 and 8.  No overclaim was found; the epistemic upgrade
(assumption discharged at reviewed source tier; symmetry cannot amplify
an unknown pole unit; the pole discriminator closed with zero) is
accurate.

## 8. Counterexample attempts against POLE-EXIT-ZERO (all fail)

- **CX1, finite puncture through a pole vertex.**  Blocked
  flag-intrinsically: 5.3(vi) no-common-root + Statement 5.1 positivity
  + corrected 3.15 give `g(P) = infinity` for every `P` through `F`.
- **CX2, cv flag somewhere on a pole ray.**  Below the star `d_A` is
  even larger than `d_F > 0`, so no `T_a^0` flag; above it
  `d_g = d_(g,F) > 0` is constant, so the unique `d_A = 0` flag has
  `d_g != 0` and is not cv.  No cv flag exists on the ray.
- **CX3, alternative quantifier reading of Notation 9.3.**  `u` is
  pinned to `pi(F)`; `F = I_P(u)` literally says the ray passes through
  `F` in the contact quotient (Definition 3.3); no reading decouples
  the two flags from the shared puncture.
- **CX4, selected witness attached away from the base or in the other
  tree component.**  The promoted lemma attaches the witness uniquely at
  the base vertex, and Notation 3.8's `F * c` construction forces the
  realizing puncture through `F`; the x-side witness is a separate
  `psi` object and no direction at a y-side vertex realizes an x-side
  puncture.
- **CX5, pole-endpoint contact continuation.**  Contact beyond a
  segment-endpoint pole vertex still passes through the vertex, so the
  puncture is a pole and carries no witness.
- **CX6, smuggled `b_e`/`M`/`w` dependence.**  No step of the proof
  consumes `b_e`, `M`, `w`, regularity, a chain normal form, symmetry,
  or the withdrawn Euler equality; verified by inspection of each cited
  statement's hypotheses.
- **CX7, a pole vertex that is not a star flag of its punctures.**
  `F in T_(a,pole)` means `F = F_Q^*` for a puncture `Q` through `F` by
  definition; all other punctures through `F` fall to CX1.

Three independent closing mechanisms (the 5.5 + repaired-7.2 value
contradiction; Statement 7.2 as proved by the sidedness theorem; the
`d_g > 0` ledger on pole rays) would each have to fail simultaneously
for a counterexample to exist.

## 9. Findings ledger (non-blocking)

- **F1, custody.**  Sections 0 and 5 discuss and evaluate
  `BOOK-OFFAXIS.md` Section 2(c1) ("says something different and remains
  correct"), but the file is absent from Section 1's pinned-input list.
  The verbatim (c1) text does appear inside the pinned Opus review, and
  I verified the target's paraphrase against the file directly (hash in
  Section 1 above), so the mathematics is unaffected; the pin should
  nevertheless have been recorded.
- **F2, tacit step.**  `M_F = gcd(4,6)` under Notation 8.1 relies on
  `m_F = 0` at pole vertices; true and covered by the pinned
  integration, but unspoken in the target's Section 2.
- **F3, harmless narrowing.**  The Lemma is stated for y-side pole
  vertices while its proof is side-free.  No consumer effect at td=12.

None of these alters a stated mathematical claim, its hypotheses, or the
consequence perimeter, so they do not rise to `PASS_WITH_REPAIR`.

## 10. Verdict, maximum safe consequence, next discriminator

**PASS.**

Maximum safe consequence, at the reviewed Sigray/source-repair tier and
conditional on the target's hypothesis chain (normalized polynomial
Keller counterexample; repaired pole-set non-leakage; repaired
Proposition 7.2; literal Notation 9.3 or its promoted selected
replacement):

> Every actual pole vertex has empty literal `Y` and empty selected exit
> set, hence exact `lambda = 0`.  In particular each of the three td=12
> type-`(2,3)` poles with `(a_e,b_e,nu) = (1,2,3)`, `M = 2`, `w = 3/2`
> contributes exactly zero to the shared first-separation budget; the
> proposed symmetric `+3` kill is unavailable, and the reviewed U1
> first-trunk formal family survives with its trunk-jet, transport,
> landing, and realizability gaps intact.  Nothing here yields source
> realizability, landing, a td=12 panel exclusion, a counterexample, or
> JC2.

Next genuine td=12 discriminator: the trunk extra-branch cv jet at the
`B`-direction of the `(2/3,3)@nu_F=25` cell --- decide whether the jet
forces `lambda_F = 8` exactly, `>= 9` (still fits), or `>= 10` (kills
that cell while leaving the `(3/4,4)` sibling alive).  Secondary: the
Statement 3.9(i) instance `i_F = 3n*i_G`, the only place `n` enters and
the natural target for a cofinality argument.  The pole side holds no
further local unknown unless a longer entry route inserts an interior
chain vertex, which would then require its own `Q`-datum before any
charge.

---

Report-body SHA-256 (computed as the bytes before the separator line above):
`8c872c1251fcb24519bd2ee18338d7bcf2bbdc19de70384e7cb3ba79df18c1ea`.
