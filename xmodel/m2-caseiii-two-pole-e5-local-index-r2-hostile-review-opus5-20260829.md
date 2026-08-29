# Hostile review: Fable Q+E5 two-pole merge-local index theorem (R2)

Reviewer: Opus 5 (different-model hostile review). Date: 2026-08-29 UTC.
Target: `xmodel/m2-caseiii-two-pole-e5-local-index-repair-fable5-20260829.md`
(full SHA-256 `6624f295…9da2` verified; body `01deb67e…a1e8` verified) and
packet `cases/m2_caseiii_two_pole_e5_local_index_r2_20260829/` (all four
file hashes and the embedded sealed field `bf8e25eb…9c6a` verified;
ordinary and `-O` suites both pass with exactly **1,264,851 checks**,
0.72 s each; no CAS ran). Sources read in full: R1
(`…incoming-index-bound-sol56-20260829.md`) and the Fable R1 review
(`…-hostile-review-fable5-20260829.md`, body `9cbb1a7c…`),
`xmodel/sol-h5a.md` (Props 1–2, §6.2 (17)/(18)), `xmodel/grok-h5a-review.md`,
`ladder/BOOK-OFFAXIS.md` §§6–11a, `ladder/SHEET6-DEPTH.md` §2/§5c–5d,
`ladder/SHEET6-MULTIPOLE.md` MP1–MP4, `cases/book_offaxis.py`
(`merge_cells`/`expand2`/`node_solve`/`solve_arr`/`cell_check`/`NUCAP`),
`cases/td7_census_e5.py` (`DEAD56`, `nu_legal`, `arrival_menu`,
`e5_cells_C`), and only the directly relevant clauses of my own earlier M2
reports. Clean-room scripts were built and run under `/tmp/opus_r2/`;
neither the packet nor any canonical file was modified.

## VERDICT: `REPAIR_REQUIRED`

The theorem layer is right. Lemma A, Theorem B, Theorem C, the equality
characterisations, the 12-of-17 attainment claim, the no-incoming-bound
proposition and the corrected Opus adjudication all survive hostile
re-derivation and independent exact sweep — I found **zero** counterexamples
in 2,158,158 pattern cells, 29,518,848 regime-3 handshake samples and a
from-source rebuild of the promoted book. R1's inverted headline is
correctly repaired, and the M-graded refinement is a genuine new result.

PASS is denied on one load-bearing new claim and one migration law:

* **§7.4 is false.** Its "infinite pattern fibre at fixed `(kbar, nu_G)`"
  is not merely unsupported — three of its five named members violate the
  strict (NE) law the report itself lists in H4, the canonical engine's own
  `cell_check` rejects them, and the general statement is refuted: the fibre
  is **always finite**, with an explicit bound I derive below. The claim is
  sealed into `certificate_r2.json`, and §8.3's justification rests on it.
* **§8.3 would hard-code a false law into `book_offaxis.py`.** The T1
  encoding "`dp | dq <=> kbar in {3,4}`" is the `w = 2` specialisation of the
  frozen td-7 chain-1 partner. At general `w` (which `solve_arr` sees) the
  law is `kbar in {w + d : d | w}`; the packet's own `e5_solve_mu1` raises
  `ValueError` on `w = 1` and `w = 3`.

Neither defect touches Lemma A / Theorem B / Theorem C. After the two
repairs and a certificate regeneration this is `PASS_AT_QE5_TWO_POLE_SCOPE`
at the theorem tier. **Engine migration is NOT authorised** independently
of that: three of the seven §8 gates fail source-level certification (§F5).
`NUCAP = 500` stays.

---

## Findings, severity order

### F1 — BLOCKER. §7.4's infinite pattern fibre does not exist; its witnesses are NE-illegal, `cell_check` rejects them, and the fibre is provably always finite

**(a) The named family dies at `s >= 4`.** At `(mu, w, mu0) = (4,1,5)`,
`nu_G = 3`, `kbar = 2` the family `A = 3+2s`, `Sm = 2s-3` gives
`dq = 4+3s`, `dp = 8+6s`, `D = 8+6s`, i.e. **`dp = 2*dq` identically**.
H4's strict (NE) law `m_j*dq < dp` therefore forces `m_j < 2`, i.e.
`m_j = 1` for every non-chain orbit — not `m_j <= mu-1 = 3`. Hence
`Sm = k`, and with `s = k + lex`, `lex >= 0`:

    k = Sm = 2s-3,   lex = s - k = 3 - s >= 0   <=>   s <= 3.

Only `s = 2` → `(20,10)` and `s = 3` → `(26,13)` are legal cells. The
report's explicitly named `(38,19)` (`s=5`) and `(62,31)` (`s=9`), the
module's `(134,67)` (`s=21`), and the test's inline `s = 45` member
(`fix-fibre-inline`) are **not two-pole case-III pattern cells at all**.
`M = |T|` does not "grow without bound"; the fibre is `{(20,10),(26,13)}`.

**(b) The canonical engine agrees with me, not with the packet.** Feeding
each member to a verbatim extract of `book_offaxis.py:219-265`
(`cell_check(kbar=2, X=4, mus_non0=[4], mu0=5, M_G=gcd(dp,dq))`):

    s=2 (20,10) True | s=3 (26,13) True | s=4 (32,16) False | s=5 (38,19) False
    s=6 (44,22) False | s=7 (50,25) False | s=8 (56,28) False | s=9 (62,31) False

`cell_check`'s own `mm = (dp-1)//dq` is exactly the NE bound `1` here, and
its `Q >= r0 + kmin` test is exactly `1+s >= 1 + (2s-3)`, i.e. `s <= 3`.
So the packet contradicts the very existence solve §8.3 proposes to retain.

**(c) The general claim is refuted, with a closed form.** Fix
`(mu, w, mu0, kbar, nu_G)`; then `r := dq/D = kbar/(mu*w)` is fixed and
`u := mu - 1/r > 0`. (NE) gives `m_j < mu - 1/r`, so
`m_max = ceil(u) - 1` and `mu - m_max - 1/r = 1 + u - ceil(u) in (0,1]`.
From `A = mu*s - Sm >= s*(mu - m_max)` (using `k <= s`) and
`A = (1+nu+nu*s)/(r*nu) + delta/nu` (from `dq = r*D`),

    **s * (1 + u - ceil(u))  <=  (1+nu)/(r*nu) + delta/nu**,

so `s` — hence the whole fibre — is bounded. For the §7.4 parameters this
gives `s <= 3`, matching (a) exactly. Empirically: over **92,772** distinct
`(mu, mu0, nu_G, dq/D)` fibres in the box `mu<=7, delta<=8, nu<=30, k<=5,
lex<=8` the largest fibre has **5** members (histogram
`{1:92083, 2:486, 3:136, 4:63, 5:4}`), zero bound violations; and in a
targeted deep search over **57,960** fibres restricted to §7.4's own regime
(`mu>=2`, `kbar < mu*w`) with `s` allowed to **400**, the largest fibre has
**9** members and terminates at `s = 27`.

**(d) Root cause, and why it is load-bearing.** `counterfixtures()` never
calls `gap_pattern_certificate` — the one helper that was repaired to
enforce the true (NE) law (`all(m*dq < dp for m in mults)`, F7.1 of the R1
review). Instead it applies the *derived* bound `m_j <= mu-1` as
`any(k <= sm <= 3*k …)`. Substituting the actual law
(`k*((dp-1)//dq)`) makes `certificate()` die with
`ValueError: fibre NE census infeasible` (my mutation `O1`, §F7). The
sealed certificate `bf8e25eb…9c6a` therefore carries a field literally
named `pattern_fibre_infinite_at_fixed_kbar_nu_G` containing three illegal
cells, and §7's preamble claim that every counterfixture satisfies "every
recorded law of its shape" is false for that family.

**Consequence.** §8.3's stated reason — "the §7.4 fibre caveat forbids cell
enumeration at `mu >= 2`" — collapses. Keeping `cell_check` remains
*conservative and safe*, so the migration action is unharmed; but the
justification must be replaced, and §4's finiteness product (iii) is
actually **strengthened**: the pattern layer is finite too, so per-state
two-pole cell books at `mu >= 2` are finite objects, not existence-only.

**Repair.** Withdraw §7.4; replace with the finiteness lemma of (c);
route `counterfixtures()` through `gap_pattern_certificate` (or apply
`(dp-1)//dq`); truncate the family to `{(20,10),(26,13)}`; regenerate the
certificate; add a mutation that flips the NE bound in the fixture path.

### F2 — MAJOR. §8.3's T1 law is `w = 2`-only; as written it would put a false law into the canonical engine, and the packet's own solver crashes off `w = 2`

§8.3 instructs: at `mu == 1` "apply T1 (`dp | dq <=> kbar in {3,4}`)". At
`mu = 1` the reading-free law is `kbar = w*dq/D`, `dp = dq - D`, so

    dp | dq   <=>   (kbar - w) | kbar   <=>   (kbar - w) | w
              <=>   kbar in { w + d : d | w }.

`w=1 -> {2}`, `w=2 -> {3,4}`, `w=3 -> {4,6}`, `w=4 -> {5,6,8}`,
`w=6 -> {7,8,9,12}`. The `{3,4}` encoding is the frozen td-7 chain-1
`(mu,w) = (1,2)` specialisation of BOOK-OFFAXIS §11's law; the `w`-free
statement is `dp | dq <=> M = dp`, which §11 also prints.

This is not academic. `solve_arr` runs over the whole `w_closure_off`
alphabet, and the packet's `e5_solve_mu1` hard-gates the identification:

    e5_solve_mu1(w=2, mu0=3, w_U=2/3) -> 3 cells [(7,21,3),(8,16,4),(10,15,6)]
    e5_solve_mu1(w=1, mu0=3, w_U=1/3) -> ValueError: T1 encodings dp|dq and
                                          kbar in {3,4} disagree
    e5_solve_mu1(w=3, mu0=3, w_U=1)   -> ValueError: (same)

So the reference implementation both encodes the false law and *raises*
rather than returning a verdict on legitimate in-scope input — a behaviour
`solve_arr` cannot tolerate. §8.3's citation of
`td7_census_e5.e5_cells_C`'s "(I5a)-(I5d) inversion" as the model compounds
this: that routine hard-codes `mu*w = 2` throughout (`g*r > 2`,
`kb = 2*dq/c`, `(m*g*r - 2)/(m-1)`), so it is a td-7 instrument, not a
general-`w` one. **Repair:** state T1 as `M = dp` (or
`kbar - mu*w | mu*w` at `mu = 1`), and make `e5_solve_mu1` return rather
than raise.

### F3 — MAJOR. §7.1's countercells are all `M = 1`, i.e. MP2-dead as interior merges — the same caveat §2/§5 applies to Lemma A but not here; and no MP2-alive `r0 = 2` countercell can exist

Every one of the six listed `r0 = 2` cells has `D = 1`, and `M | D` forces
`M = 1`:

    (13,7) M=1 | (19,10) M=1 | (20,7) M=1 | (38,13) M=1 | (109,22) M=1 | (195,28) M=1

This is exactly the property the report is careful to disclose for Lemma
A's sharpness witnesses ("every sharpness witness is MP2-dead as an
interior merge", §2/§5) and silently omits for the countercells.

It is worse than an omission. Generalising the report's own proof to
arbitrary arity gives (same two branches; `dq <= 1 + (r0+1)*y`,
`D = y - delta >= M`):

    **dq/D <= (r0+1) + ((r0+1)*delta + 1)/M**       (0 violations at r0=2,3,4)

At `r0 = 1` this is Theorem B; at `r0 = 2, M = 1` it is exactly the
report's `3*delta+4`, attained. But an `r0 = 2` cell can exceed the
two-pole constant `2*delta+3` only if `M < (3*delta+1)/(2*delta) <= 2`,
i.e. only if `M = 1`. Exhaustive search confirms it: **0** MP2-alive
(`M >= 2`) violators at `r0 = 2` and `r0 = 3` in the wide box
`mu<=8, delta<=12, nu<=60, k<=3, lex<=7` (closest approach is exact
equality, gap 0). Violators first appear at `r0 = 4`, e.g. `(44,46)`
`mu=1 mu0=8 delta=7 nu=9 D=2 M=2`, `dq/D = 23 > 17` — but `TDMAX = 14`
with `m in range(2, td//3 + 1)` caps `m <= 4`, and MP1 gives
`r(G) <= m`, so `r0 <= 3` in the campaign's actual range.

**§7.1's conclusion nevertheless stands, and I certify it independently.**
`M_G = 1` rows genuinely reach `solve_arr`: `expand2` yields
`MG in divisors(sum(mus))` (including 1), `cell_verdict`/`node_solve` apply
no MP2 filter on that path (the filter lives only in `merge_cells`), and
MP3 exempts strict ancestors of `G*` from MP2 anyway. Feeding the six
countercells through the canonical `cell_check` at `w = 1`:

    (13,7) kbar=14 X=26 -> True   [two-pole bound mu*w*(2d+3) = 10]
    (19,10) kbar=20 -> True [14] | (20,7) kbar=21 -> True [15]
    (38,13) kbar=39 -> True [27] | (109,22) kbar=110 -> True [75]
    (195,28) kbar=196 -> True [133]

All six are accepted at a `kbar` far above the two-pole bound. So wholesale
cap replacement is indeed unsound — but only on `M_G = 1` rows within the
campaign's `r0 <= 3` range. **Repair:** disclose `M = 1` on the
countercells; state the `r0`-graded bound; and note that gate (G-e) as
written (§8.6) tests only `M_G = 1` rows plus three F1-illegal fibre rows,
which makes it a weak and partly vacuous gate.

### F4 — CONFIRMED. Charges 1–5: the scope, both bounds, both equality laws, the elimination, the 12-cell attainment, and the freedom of `nu_U`

Re-derived by hand and by clean-room sweep; nothing imported from the
packet.

**Charge 1 — scope and pattern identities.** H1–H4 are exactly the recorded
laws. R2.2 gives `p_red = ⊖η^ε·Π_e(η^ν−c_e^ν)^{μ_e}·Π_j(η^ν−d_j^ν)^{m_j}`
with `ε = μ₀` when a 0-chain arrives and `dq = (r₀+k+l)ν+1`; with `r0 = 1`
that is the report's `dp = mu0 + nu*(mu+Sm)`, `dq = 1 + nu*(1+s)`,
`s = k+lex`. `nu_G >= 2` is forced (DEPTH §5c: "I-family merges
(ν_G = 1) are case (I)"), and `kbar in Z` follows from DS1(c) at `V_{1,a}`
(DEPTH §2:116) — this licenses regime-3's integer menu. `(S)`, strict `(NE)`
and `(R)` are R2.2 verbatim. The identity
`D = mu*dq - dp = nu*(mu*s - Sm) - delta = nu*A - delta` is exact;
`A >= k + mu*lex >= s >= 1` follows from `m_j <= mu-1` (itself from
`m_j*dq < dp < mu*dq`) and `s = 0 => D = -delta < 0`. `M | D` is immediate
from `M | dp`, `M | dq`. Verified on **2,158,158** box cells / **219,667**
`(S)+(NE)+(R)`-legal cells (`mu<=8, delta<=10, nu<=40, k<=4, lex<=6`) with
**0** violations of any of `D`-identity, `s`/`A` laws, `M | D`.

The one notation trap is flagged correctly by the report: its `s = k+lex`
excludes the arriving orbit, whereas my `s = r0+k+lex = s+1`.

**Charge 2 — Lemma A and equality.** Both branches check.
`nu*s <= delta => nu <= delta => dq <= 1+2*delta`, `D >= 1`, ratio
`<= 2*delta+1`. Otherwise `y = nu*A >= delta+1`, `D = y-delta`,
`dq <= 1+2y`, and `(1+2y)/(y-delta) = 2 + (2*delta+1)/(y-delta)` is
decreasing, equal to `2*delta+3` at `y = delta+1`. Equality forces
`s = 1`, `A = 1`, `nu = delta+1`, `D = 1`, hence `M = 1`. The two shapes
listed are the only `s = A = 1` patterns (`(k,lex) = (1,0)` needs
`m_1 = mu-1 >= 1`, so `mu >= 2`; `(k,lex) = (0,1)` gives `A = mu`, so
`mu = 1`). Attained at **every** `delta` in 1..10 (8 cells per delta in my
box). `kbar = mu*w*dq/D` from the case-II handshake `X = mu*(kbar-w)` and
Prop 9.3(b) `X/kbar = dp/dq`; case II is untouched by H5a (grok-h5a
Finding 3), so the bound is reading-independent as claimed.

*Widening counterexamples:* I looked for them and found none in scope. The
only failures are out of scope and are exactly the report's own §7.1–7.3
families (with the F3 correction), plus §7.4 which does not exist (F1).

**Charge 3 — the M-graded bound and the 12 cells.** `M | D => D >= M`;
branch 2 evaluated at `y = delta + M` gives `2 + (2*delta+1)/M`. Equality
iff `s = A = 1`, `nu = delta+M`, `D = M`, and then `dq = 2*delta+2M+1`, so
`M | dq <=> M | 2*delta+1` (hence `M` odd). The converse construction is
sound: `gcd(dp,dq) | D = M` and `M` divides both, so `gcd = M` exactly, and
the cell passes `(S)`, strict `(NE)` (`M < dq`) and `(R)`. My sweep's
graded-equality `M`-census is **exactly the set of divisors of `2*delta+1`**
for every `delta` in 1..10, with **no even `M` anywhere** — an exact match
to the theorem, not merely consistency.

Independent reconstruction of the promoted book, parsed by regex directly
out of `ladder/BOOK-OFFAXIS.md` §11a (not from the packet's typed copy):
17 rows; `kbar` histogram `{5:4, 6:12, 7:1}`; Theorem-B equality on
**exactly 12** rows, all `kbar = 6`, `mu0 in {3,5,7,…,25}`; each satisfies
`M = 2*delta+1`, `nu_G = delta+M`, `D = M`; the graded `nu_G` bound is
attained exactly on those same 12; Lemma A equality on **0** rows
(consistent with "MP2-dead"). The `(4m-2, 6m-3)` closed form checks
(`m=3 -> (10,15)`, `m=5 -> (18,27)`, `m=25 -> (98,147)`).

**Charge 4 — the Q+E5 elimination in all three regimes.** Setting
`mu*(kbar-w) = mu0*(kbar - nu_G*w_U)` gives
`mu0*nu_G*w_U = delta*kbar + mu*w` identically. This is the campaign
normalisation of sol-h5a (18) `X_G = mu0(kbar_G - nu_G w_U)`, and for the
frozen `(mu,w) = (1,2)` it reduces to §11a's promoted (I4)
`kbar = (mu0*nu_G*w_U - 2)/(mu0-1)` — I re-derived that reduction
symbolically. 200,000 random exact-rational instantiations: **0** failures.
Regime `mu0>mu`: `nu_G = (delta*kbar+mu*w)/(mu0*w_U)` per `kbar`, one per
`kbar`, bounded by Lemma A / Theorem B; equality on the 12 rows verified.
Regime `mu0=mu`: `nu_G*w_U = w`, at most one value. Regime `mu0<mu`: the
strict `nu_G < w/w_U` rests on `kbar > w`, which is *not* an assumption —
`kbar - w = w*dp/D > 0` whenever the case-II edge is searrow — and it is
genuinely sharper than R1's `mu*w/(mu0*w_U)`; **29,518,848** exact samples,
**0** failures. `ceil_fraction(strict)-1` is the correct strict endpoint at
both integral and non-integral `w/w_U`.

**Charge 5 — `nu_U` free, irrelevant, menu-not-bound.** Confirmed on all
three legs. (i) E5 contains no `nu_U`: it cancels into
`w_U = (kbar_U - rho_U)/nu_U`, so the cell data factor through
`(w_U, M_U)`. (ii) `td7_census_e5.nu_legal` returns `'neutral'` for *any*
`nu` with `(nu+1) % mu0 == 0`, uncapped, and §11a records those classes per
cell ("neutral ν≡4(5)" etc.) with the enumeration explicitly "CAP-FREE …
under E5 there is no ν_U to bound". (iii) On `(18,27,13,9)@5` the control
reproduces:

    nu_U = 4, 9, 14, 10^20+4  (all neutral)  ->  kbar_E5 = 6 invariant;
    kbar_mixed = 3/2, 4, 13/2, 100000000000000000003/2 — never the cell;
    nu_U = 13 = nu_G           ->  kbar_mixed = 6 (only match).

So `h_mixed = nu_G` identically (17/17 verified from the parsed book) and no
finite incoming bound is derivable. A state/congruence menu is the right
representation. **One precision correction to §4's gloss:** at this cell
`nu_U = 13` is *not* a legal arrival at `(2/5, 5)` — neutral is `4 (mod 5)`
and the direct arrivals are `2, 7, 12` (sol-h5a §6.2; BOOK-OFFAXIS:759). So
imposing the mixed pin here does not leave the cell `U_7C`-conditionally
alive; it kills it. §5 states this correctly via the 2-cell forced-ν
sub-book, so the report is internally consistent — but §4's parenthetical
and the `no_incoming_bound_demo` docstring overstate.

**Opus adjudication (§6) — CONFIRMED in both directions, against my own
prior report.** Clause 4 `nu <= mu0*num(w_0)` binds neither index:
16 of 17 promoted cells violate it as a `nu_G` bound, the sole non-violator
being `(25,35,17,5)@8` (`17 <= 24`); and as an incoming bound it fails on
`(9,15,7,3)@2`, legal under both readings with recorded `nu_U = 7 > 2`.
The report's diagnosis of the root cause — Theorem 4(4a)'s case-II
transport applied to the 0-edge — is correct, and its statement that my
§10c declined to adjudicate H5a rather than confusing two symbols is also
correct; R1's "notation correction" was the inverted move. My
congruence-quotient claim for 0-edges under E5 is confirmed by Theorem C.
This matches the errata already carried in my equal-join report.

*Charged slice (§5).* Reproduced under both pins. E5: `3*nu_G = kbar+2`,
`kbar <= 10` gives `nu_G in {2,3,4}` → `(4,8)` T1-dead / `(5,7)` `M=1`
MP2-dead / `dq = 15/2` non-integral. Mixed: `h <= 4`, odd ray leaves
`h = 3`, same `(5,7)`. Kill is reading-stable. The provenance flags
(RETRACTED §8 Step 3; promoted `@2` cell on the untouched `w_U = 1/2`
slice; "h odd" is `nu_U` language) are accurate and are carried in the
sealed JSON.

### F5 — Migration plan: scope guard sound, but three gates fail source-level certification

**Sound.** The line references are exact against the working tree:
`:305-309` (pinned-branch `nuH = (kbar - X/mu0)/w0`), `:320-323`
(`mu0 == mu`), `:325-328` (`mu0 < mu` cap), `:329-336` (`mu == 1` doc-9
cap), `:337-357` (NUCAP loop), `:165` (`NUCAP = 500`), `:343` (loop pin).
The scope guard (`zero` a pole leaf, `len(non0) == 1`, `inner_mus == []`,
`inner0_mu is None`) is well-formed and *sufficient*: with
`len(non0) == 1` the R2.1(ii) pin is unreachable, so the row always lands
in the no-pin branch. Fall-through for out-of-scope rows is mandatory and
correctly identified. Step 4's replacement of `nu_ok` by the state gate
`mu0 | M_U` + menu recording is faithful to §11a and `nu_legal`. Step 5's
`reading=promoted-Q+E5` tagging and the `U_7C`-conditional restatement of
the scoped mixed-pin cap are correct and correctly firewalled.

**Failing gates.**

1. **(G-a…G-e) are stated but §8.3 is unsound (F2).** No gate in the list
   would catch the `{3,4}` T1 encoding, because (G-a)/(G-b)/(G-c) all
   replay td-7 rows where `w = 2` by construction. A gate on
   `w != 2` in-scope rows is missing and must be added.
2. **(G-e) is weak and partly vacuous (F1, F3).** "The packet's
   counterfixture cells must remain OPEN/capped" tests six `M_G = 1`
   `r0 = 2` rows and three cells that are not cells. It certifies nothing
   about `M_G >= 2` behaviour and nothing about `r0 = 3`.
3. **§8's regime numbering is swapped relative to §4.** §4 numbers
   `1 = mu0>mu` (difficult), `3 = mu0<mu`; §8 step 2 says "regime 1 loops
   `nu_G < w/w_U`" (that is §4's regime 3) and "regime 3 loops the finite
   menu `kbar`" (that is §4's regime 1). The prose disambiguates; an
   implementation spec must not require that.
4. **The site list is broader than the licensed scope.** `:305-309` is
   unreachable under §8.1's own guard, and `:320-336` also fire on
   `len(non0) >= 2` equal-`(mu,w)` rows. "Retire" must read "bypass on the
   scoped path only", or out-of-scope verdicts change and (G-d) fails.
5. **Regime 2 has no `kbar`.** Step 2 forces `nu_G = w/w_U` at `mu0 = mu`
   but step 3 says "per `(kbar, nu_G)`: keep `cell_check`" — at `delta = 0`
   the two handshakes are the same equation and `kbar` is unpinned. The
   legacy branch (`:320-323`) does no `cell_check` at all; the plan should
   say so. Not a soundness hole (`dq/D <= 5/2` at `delta = 0`, so
   `kbar in Z ∩ (w, 3*mu*w]` is finite), but the spec is incomplete.
6. **Missed strengthening (not a defect).** `M_G` is already an argument to
   `solve_arr`, and `cell_check` makes `gcd(dp,dq) = M_G` exactly, so
   Theorem B's `kbar <= mu*w*(2 + (2*delta+1)/M_G)` is directly usable and
   is dramatically smaller than Lemma A's bound (on the promoted family it
   is `6` instead of `2*(2*delta+3)`, e.g. `6` vs `102` at `mu0 = 25`).
   Step 2 uses only Lemma A.

**Therefore: no source-level migration is authorised by this review.**
`NUCAP = 500`, the OPEN fallback, and every line of `book_offaxis.py` stay
exactly as they are.

### F6 — Packet integrity, replay, and published counts: all reproduce

* Four packet hashes reproduce (`e2643ec7…`, `741fb063…`, `40954869…`,
  `02586a42…`), report full `6624f295…` and body `01deb67e…` reproduce,
  and the embedded `certificate_sha256` recomputes to `bf8e25eb…9c6a`
  from the payload minus that field.
* `python3 test_caseiii_two_pole_e5_r2.py` and `python3 -O …` both print
  `CASEIII_TWO_POLE_E5_R2_TEST_PASS checks=1264851`, 0.72 s each.
* §9's published sweep counts reproduce **exactly** on an independent
  re-implementation of the same box: **299,447** `D > 0` cells and
  **49,791** NE-legal cells. The "NE-illegal tuples have `dq/D <= 1`" claim
  holds on all **249,656** of them.
* `DEAD56` membership is faithful: `(7,21,4,7)`, `(8,16,5,8)`,
  `(5,15,2,5)`, `(5,10,3,5)` are all in `td7_census_e5.DEAD56`; the
  `mu0 = 3` solver menu is exactly `{(7,21,4,7), (8,16,5,8), (10,15,7,5)}`
  with T1-flags `[True, True, False]`, i.e. the two DEAD56 candidates plus
  the promoted cell, as §5 claims.
* The certificate's firewall is all-`False` on 14 keys and the
  `notation_correction` field is genuinely regenerated in the corrected
  direction (R1's F7.3 repair discharged).
* Circularity: the §5 book battery and the test's `BOOK_INDEP` copy are
  independently typed and cross-check, and the sweep recomputes `dp, dq, D`
  inline — genuine theorem-level checks. The elimination checks remain
  partly definitional (`nu_G` is *defined* by the elimination and then
  re-asserted), the same transparency defect the R1 review noted; it is not
  a soundness hole because my clean-room derivation is independent.

### F7 — Mutation coverage: the packet's six are real, and eight of mine are detected — but the fixture path is the hole

The packet's `MUT_A`–`MUT_F` all fire (control passes; I re-ran the whole
battery inside each mutant). Eight independent mutations of my own, staged
on `/tmp` copies with the packet untouched:

| mutation | detected | signature |
|---|---|---|
| `O1` fibre proxy → true NE law `(dp-1)//dq` | YES | `ValueError: fibre NE census infeasible` |
| `O2` fibre list → its two legal members | YES | `CHECK_FAILED:fix-fibre-M` |
| `O3` bogus 18th book cell `(14,21,10,7)@4` | YES | `solver failed to recover book cell alive` |
| `O4` graded row count 12 → 11 | YES | `graded equality must hold exactly on the 12 kbar=6 rows` |
| `O5` drop `A == 1` from the equality profile | YES | `plain equality law failed` |
| `O6` regime-1 strict endpoint off-by-one | YES | `regime-1 strict menu changed` |
| `O7` `kbar` menu low endpoint `w` → 1 | YES | `kbar menu lower endpoint broken` |
| `O8` graded `kbar` bound forced to `M = 1` | YES | `graded nu_G bound not tight on equality row` |

`O1` is the diagnostic one: the packet is *pinned to the wrong NE bound*.
Correcting the law breaks certificate generation, which proves the F1
defect is load-bearing rather than cosmetic. `O2` shows the illegal members
are load-bearing in the tests too (`fix-fibre-M` asserts the five-element
`M` list `[10,13,19,31,67]`, three of whose entries are not cells).

### F8 — Nits

1. §3's "`(4m-2, 6m-3)` … exactly the promoted §11a `kbar = 6` family"
   needs two qualifiers: even-`m` members are N1-dead
   (`gcd(kbar, nu_G) = gcd(6, 3m-2) >= 2`), which is why §11a lists
   `(14,21,10,7)@4`, `(22,33,16,11)@6`, `(30,45,22,15)@8`,
   `(38,57,28,19)@10` as N1 kills; and the family terminates at `m = 25` by
   closure exhaustion (§11a), not by the theorem.
2. §9's mutation table says "manual spot-run of MUT_C dies with 'solver
   failed to recover book cell alive'" — reproduced.
3. `e5_solve_mu1(w, mu0, w_U)` advertises a general `w` but is `w = 2`-only
   (F2); either freeze the signature or generalise the T1 gate.
4. The lifecycle line says "authorizes no canonical engine change"; §8's
   verb "retire" for engine sites reads as an instruction. Recommend
   "bypass on the scoped path".

---

## Charge-by-charge summary

1. **Scope H1–H4, `D = nu*A - delta`, `M | D`** — CONFIRMED, exactly the
   R2.2/R2.1/DEPTH-§5c record; 2,158,158-cell sweep, 0 violations (F4).
2. **Lemma A and all equality conditions** — CONFIRMED and sharp; equality
   iff `nu = delta+1, s = 1, A = 1`, forcing `D = M = 1`; attained at every
   `delta`; no widening counterexample in scope (F4).
3. **M-graded bound, equality iff, exactly 12 promoted cells** — CONFIRMED;
   graded-equality `M`-census is exactly the odd divisors of `2*delta+1`;
   independent re-parse of §11a gives 12/17, all `kbar = 6`,
   `mu0 = 3,5,…,25`, graded `nu_G` bound tight on the same 12 (F4).
4. **`mu0*nu_G*w_U = delta*kbar + mu*w` in all three regimes** — CONFIRMED;
   matches sol-h5a (18) and reduces to §11a (I4); 200k random + 29.5M
   regime samples, 0 failures; the `mu0<mu` strict form is genuinely
   sharper than R1's (F4).
5. **Incoming `nu_U` free, irrelevant, menu not bound** — CONFIRMED on all
   three legs, including the `10^20+4` control; one loose gloss in §4 about
   `nu_U = 13`'s legality (F4).
6. **New infinite pattern fibre at `mu >= 2`** — **REFUTED.** Members
   NE-illegal beyond `s = 3`; `cell_check` rejects them; fibres are always
   finite with an explicit `s`-bound; largest fibre found anywhere is 9
   (F1). The engine may still keep the existence solve — for a different,
   conservative reason.
7. **Migration plan** — scope guard sound and fall-through correct; but
   §8.3 encodes a `w = 2`-only law (F2), (G-e) is weak/partly vacuous
   (F1, F3), the regime numbering is swapped, the site list overreaches
   scope, and regime 2 lacks a `kbar` (F5). **Cannot safely remove the
   legacy cap even on the exact two-pole leaf scope until F2 and the gate
   set are repaired.**

## Exact safe consequence (narrowest maximum)

Under this verdict, **none** at the engine tier: `NUCAP = 500`, the OPEN
fallback, `solve_arr`, `cell_check` and every other canonical line stay
byte-untouched. For the record, what the repaired report would license at
the theorem tier and nothing more:

* At every interior merge satisfying H1–H4 with `delta = mu0 - mu >= 1`,
  **reading-independent**: `dq/D <= 2*delta+3` and
  `kbar = mu*w*dq/D <= mu*w*(2*delta+3)`; equality forces `D = M = 1`,
  hence never on an MP2-surviving interior cell.
* **M-graded**: `dq/D <= 2 + (2*delta+1)/M` and
  `kbar <= mu*w*(2 + (2*delta+1)/M)`, equality iff `M | 2*delta+1` (`M`
  odd) on the `s = A = 1`, `nu_G = delta+M`, `D = M` cell; realised on 12
  of the 17 promoted cells.
* Under the **promoted Q+E5 pin only**:
  `mu0*nu_G*w_U = delta*kbar + mu*w`, with
  `nu_G <= mu*w*(delta*(2 + (2*delta+1)/M) + 1)/(mu0*w_U)` per arriving
  state at `mu0 > mu`, `nu_G = w/w_U` forced at `mu0 = mu`, and the strict
  `nu_G < w/w_U` at `mu0 < mu`.
* **No incoming-index bound exists, follows, or is required**; the arrival
  layer is a state/congruence menu.
* Two facts this review adds, offered for the repair and not claimed as
  promoted: the arity-graded bound
  `dq/D <= (r0+1) + ((r0+1)*delta+1)/M`, and the pattern-fibre finiteness
  bound `s*(1 + u - ceil(u)) <= (1+nu)/(r*nu) + delta/nu`,
  `u = mu - 1/r`, `r = kbar/(mu*w)`.

Nothing here certifies `U_7C`, the legacy `cell_check` grammar, equal-join
`kbar` bounds, multipole or inner-merge trees, realizability, source
landing, any topological-degree ceiling, Keller counterexamples, JC2, or
any AWS/fleet action. The report's own §10 firewall is otherwise accurate.

## Repair path

R1. Withdraw §7.4; replace with the finiteness lemma (F1c); truncate the
fixture family to `{(20,10),(26,13)}`; route `counterfixtures()` through
`gap_pattern_certificate` (or use `(dp-1)//dq`); regenerate
`certificate_r2.json` and rename the field. Restate §8.3's reason for
keeping `cell_check` as conservatism, not necessity.
R2. Replace §8.3's T1 gate by the `w`-free `dp | dq <=> M = dp` (or
`(kbar - mu*w) | mu*w` at `mu = 1`); make `e5_solve_mu1` return instead of
raising off `w = 2`; drop or scope the `e5_cells_C` citation.
R3. Disclose `D = 1 => M = 1` on the §7.1 countercells; add the
arity-graded bound and the statement that no MP2-alive `r0 in {2,3}`
countercell exists; strengthen (G-e) to cover `M_G >= 2` and `r0 = 3`.
R4. Fix the §4/§8 regime numbering; restate the site list as "bypass on the
scoped path"; specify regime 2's absent `kbar`; add a `w != 2` in-scope
gate. Optionally adopt the `M_G`-graded menu (F5.6).
R5. Soften §4's `nu_U = 13` gloss and §3's "exactly the §11a `kbar = 6`
family" per F8.1.

## Verification log

Hashes: `shasum -a 256` on the report (`6624f295…9da2`), body bytes before
the final `---` (`01deb67e…a1e8`), and the four packet files (match
`e2643ec7…`, `741fb063…`, `40954869…`, `02586a42…`); sealed field
recomputed from the payload (`bf8e25eb…9c6a`).

Runs (all local, exact-rational Python, no CAS, < 5 min each):

    python3 test_caseiii_two_pole_e5_r2.py        # PASS checks=1264851, 0.72 s
    python3 -O test_caseiii_two_pole_e5_r2.py     # PASS checks=1264851, 0.72 s
    /tmp/opus_r2/book_parse.py    # 17 cells regex-parsed from BOOK-OFFAXIS s11a
    /tmp/opus_r2/sweep.py         # 2,158,158 box / 219,667 legal, 0 violations
    /tmp/opus_r2/counts.py        # packet box: 299,447 / 49,791 reproduced
    /tmp/opus_r2/fibre.py         # s7.4 member-by-member NE legality
    /tmp/opus_r2/fibre_theory.py  # 92,772 fibres, max size 5, 0 bound violations
    /tmp/opus_r2/fibre_deep.py    # 57,960 mu>=2/r<1 fibres, s<=400, max size 9
    /tmp/opus_r2/r02.py, r0gen.py, r03wide.py   # arity-graded bound, MP2 census
    /tmp/opus_r2/regimes.py       # 200,000 random + 29,518,848 regime samples
    /tmp/opus_r2/mut/run_mut.py   # 8 independent mutations, all detected
    # cell_check verbatim extract of book_offaxis.py:219-265 used read-only

No `jc2-lean` access of any kind, no workspace-wide git or search, no
network, no AWS or fleet action, no commit or push, no CAS, no canonical
edits, no long-running or high-memory process. The only file written in the
repository is this review; all scratch lives in `/tmp/opus_r2/`.

To verify this review's integrity: `shasum -a 256` on this file gives the
full hash; the body hash below covers all bytes strictly before the final
`---` separator line (recompute with
`python3 -c "import hashlib,sys; b=open(sys.argv[1],'rb').read();
print(hashlib.sha256(b[:b.rfind(b'---\n')]).hexdigest())" <file>`).

---
Review-body SHA-256 (bytes before the separator line above): `c12bbca2d6dc093a71a5907b3032f031d042590553ffbe86fb41761c7d357b4c`
