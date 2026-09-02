# COMPANION-CURVE-ALLN: the forced companion, and why (M') cannot see it

Lane: COMPANION-CURVE-ALLN · 2026-09-02 · Opus 5
Path-2 flagship. Desk-scale exact reasoning; CAS used and disclosed.

## 0. Custody, typing, scope, execution disclosure

Hash verification was the first action. All three frozen inputs matched the boxed
manifest exactly; the stop condition did not fire.

```text
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  rep-96-inner-opus5-20260901.md
bdd857c9d8c55fa000fcffee05f9f3084c5d073fb4d06285edf2af0d3c369339  reducible-all-n-r2-opus5-20260901.md
48d417d6980e52d61550a733f0dcded7d26a0c4e127677ac73bd544a8a00713b  b0-reducible-n5-opus5-20260831.md
```

Below **REP96**, **CAGE**, **N5** denote them in that order.

**Two files were consulted that are not charged inputs**, and both are disclosed
because load-bearing statements are read out of them:

- `xmodel/round1033-sheet-gate-opus5-20260831.md` — the *source* of `(M')`, which
  REP96 SS7 R4 quotes by line number but does not reproduce in full. Its SS7 gives
  the block-free form, its Prop 2.4 gives the ceiling, its (E)/Thm 5.2 gives the
  Euler budget. Nothing is consumed from it beyond those three items, each of
  which is re-derived here before use. Typed `[S]` (source-of-a-charged-quote).
- `refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf`,
  `8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f` — read here
  as primary literature, typed `[L]`. N5 SS5.3 attributes the shared-point-at-
  infinity clause and CAGE clause 1 attributes the common Newton-Puiseux type to
  it; the charge sends the whole existence question through those clauses, so the
  paper was opened rather than paraphrased. Theorem 1, Corollaries 1 and 2 and
  the surrounding normalisation discussion (pp. 1-2) were read.

**Typing.** `[P]` promoted; `[D]` derived here; `[L]` primary literature read
here; `[S]` consulted non-charged campaign file; `[A]` audit against a consumed
item; `[C]` machine-checked here. Nothing below is an attainment claim for a
Keller map: SS5's witness is a *curve pair*, not a counterexample, and is typed as
such throughout.

**Execution disclosure.** A shell was available and used. All computations are
exact (sympy 1.14.0 over `Q`, resultants and gcds only; no floating point except
where a numeric root list is printed as a cross-check, and no conclusion rests on
it). Scripts are in `/tmp/comp/` and every number quoted in SSSS2, 4, 5 was produced
by them; the randomised control in SS2.5 ran 33116 admissible configurations. No
AWS, no `msolve`, no `qqideal`, no `jc2-lean`, no canonical ledger.

**Scope.** The reducible-`A_F` branch RED-N of CAGE: `F` a noninvertible plane
Keller map of geometric degree `N >= 4`, `A_F = D_1 u ... u D_m` with `m >= 2` and
at least one affine-image dicritical with `mu = 1`. Notation is CAGE SS0's:
`c_l = mu_l s_l + K_l`, `W_i = sum_{l->i} s_l mu_l`, `a^{(i)} = N - W_i`,
`K_tot = sum_p K_p`.

**The two `b`s, kept apart, as the charge demands.** `b_dic` is the count of
affine-image dicriticals with `mu = 1` (THEOREM 7.B's symbol; a *consequence* of
H2). `b_br` is the number of **branched components** of `A_F`, the symbol of
`(RC2)` and of CAGE clause 2, forced to `1` at `N = 4, 5`. **Only `b_br` is used
below, and it is written `b_br` everywhere**, never `b`. A third `b` appears in
the source of `(M')` (`sigma = a + b`, the unramified-dicritical box count); it
occurs here only inside the quotation of Prop 2.4 in SS2.4 and is written `b_box`.

## 1. Verdict

## 2. Task (1): the block-free (M') at general N

## 3. The forced companion datum at general N

## 4. Task (2): existence — THEOREM COMPANION-EXISTS

## 5. Task (3): the (9,6,2) substrate, complete forced datum, and a witness

## 6. The machine job

## 7. Typed verdict block, OPENs, deviations

## 8. FALLACY-v2 self-check

## 9. Custody and sources
