# Hostile review — R7R2 rank-two / irregularity typing audit

**Reviewer model:** Opus 5 (`claude-opus-5`), acting as different-model hostile
referee against Sol's R7R2 audit and against my own round-`20260827T1808Z`
proposal.  I re-derived rather than defended.

**Date:** 2026-08-27
**Target:** `xmodel/ggv-r7r1-rank-two-irregularity-typing-audit-sol-20260827.md`
**Status:** `CONFIRMED WITH REPAIR` overall — the no-go holds and is
**strengthened**, but three of its stated proofs are non-sequiturs, one
mutation control is wrong, and its headline sentence is false about the
object that actually decides the question.

---

## 0. Custody, hashes, scope firewall, execution gaps

### 0.1 Fail-closed hash check

```text
REQUIRED  bd742ac48bb8768b3ea67089e3e749f43d292b09077e3d178904c71c685acb2c
OBSERVED  bd742ac48bb8768b3ea67089e3e749f43d292b09077e3d178904c71c685acb2c
                            xmodel/ggv-r7r1-rank-two-irregularity-typing-audit-sol-20260827.md
VERDICT   MATCH — review proceeds.
```

### 0.2 Section-1 frozen dependencies, rechecked

All four Section-1 hashes were recomputed and all four resolve to unique
files in the repository:

```text
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1  MATCH
    xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md      (R7R1 producer)
7ab758fa002c75cd28d81540e8f63fd8cd0de97fad791afedfeb5fb610c6cb29  MATCH
    xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-hostile-review-fable5-20260827.md
a9b2eb9023ac78733dcbf100e9b584e0445a894edd4098026a073f8ec87e5cff  MATCH
    xmodel/ideation-20260827T1808Z-opus5.md                                        (the proposal under audit)
1cc41972d5049e68b8464a634c1cfae48ec5e0e1ba995475fa90998f7aad3984  MATCH
    xmodel/ideation-20260827T1808Z-opus5-hostile-review-fable5.md
```

Context (read, not a Section-1 dependency):
`b0e60671662953a50318e4989a20a08e5b84e28cb1bfaea075e241fc367a818a` (R7 producer),
`2dd9d8f11e0fadff303c8afade0c1f4e52f1a1df4b5afffcea17d5e3d7890a18` (R7 same-model audit),
`APPROACHES.md` rows 16 / 25 / 33 (read only).

### 0.3 Scope firewall

- `jc2-lean` was **never** entered, listed, grepped, read, built, status-inspected
  or edited.  Every `find`/`grep` in this session used
  `find . -path ./jc2-lean -prune -o ... -print`, i.e. the child was pruned
  before descent.  Verified: the only `ls` naming it was `ls -d jc2-lean`
  to confirm the exclusion target exists, which does not enter it.
- No canonical ledger, producer, frozen artifact or adapter was edited.
- No AWS mutation.  No heavy local algebra: the total verification cost was
  under two seconds of pure-Python exact rational arithmetic.
- Exactly one file written: this one.

### 0.4 Execution gaps — disclosed

1. **No web tool is exposed in this session.**  Read-only primary-source web
   access was authorised by the prompt, but no `WebFetch`/`WebSearch` tool is
   present in my tool list.  Every citation in Section 6 is therefore from
   model knowledge, **not fetched and not page-verified**.  Statement content
   I rely on is standard and I have restated it in a form I can defend from
   first principles; **the exact theorem numbers should be spot-checked
   against the printed sources before promotion.**  Where a citation is
   load-bearing I say so explicitly and give the self-contained argument
   alongside it.
2. **No `sympy`/CAS on this host.**  I wrote a ~40-line exact
   `Fraction`-coefficient polynomial and truncated-power-series engine from
   scratch (`/tmp/r7r2/{poly,series}.py`) and used it for every algebraic
   claim below.  This is an *independent engine*, not a re-run of the
   producer's or of Fable5's.  It is scratch, not frozen; the checks are
   reproducible from the code inlined in Section 1.4.
3. Truncation caveat, handled: derivatives do **not** commute with power-series
   truncation.  My first pass reported four spurious `False`s from exactly
   this.  All identity checks were redone with **untruncated** polynomial
   arithmetic (Check A), and the chart-change check (Check B) compares only
   inside a window two degrees below the working precision.

---

## 1. Independent re-derivation

I re-derived the whole conjugacy from `E = 12 F_X G - 8 F G_X - t(F_X G_t - F_t G_X)`
before reading the report's derivation, then machine-checked it exactly.

### 1.1 Check A — the two bivariate identities (untruncated, exact)

With `F = P^8`, `G = P^12 W` and `P` a generic unit-constant-term polynomial
(`P = 2 + 3X + X^2 + 5t + 7t^2 + Xt`, `W = 1 + X + 2t + Xt + 3t^2`;
`F` has 153 terms, `G` has 377):

```text
A3   12 F_X G - 8 F G_X            == -8 P^20 W_X                        TRUE (exact)
A4   F_X G_t - F_t G_X             == 8 P^19 (P_X W_t - P_t W_X)         TRUE (exact)
A1   E                             == -8 P^20 W_X - 8 t P^19(P_X W_t - P_t W_X)   TRUE
A2   E                             == 8 P^19 ((t P_t - P) W_X - t P_X W_t)        TRUE
```

A3/A4 are the two identities in my own §3.2 proposal; they are **correct**,
as Fable5 also found.  A2 is the report's displayed form.  All four hold
identically in the polynomial ring, no truncation.

### 1.2 Check B — the chart change (2.2), by independent series inversion

Rather than reuse the report's chain rule, I built the change of variables the
other way: choose `Ptilde(X,s)`, `Wtilde(X,s)` in the `(X,s)` chart, set
`t = s*Ptilde`, invert `s = t/Ptilde(X,s)` by `t`-adic fixed point, transport
`P,W` to the `(X,t)` chart, and compare.

```text
B0   round trip  s(X, t(X,s)) == s                                       TRUE
B1   s(X,t) == t / P(X,t)                                                TRUE
B2   E == -8 P^21 W_X|s / (P + s P_s)                                    TRUE
B3   J(s,W) == -W_X|s / (P + s P_s)      (= -s_t W_X|s)                  TRUE
B4   E == 8 P^21 J(s,W)                                                  TRUE
```

So report (2.1), (2.2) and (2.3) are **exactly right**.  My own hand
derivation agrees: the Jacobian of `(X,s) -> (X,t)` is `P + s P_s`, giving
`s_t = 1/(P+sP_s)`, `s_X|_t = -s P_X/(P+sP_s)`, and all the `W_s` terms cancel
in `J(s,W) = s_X W_t - s_t W_X`, leaving `-W_X|_s/(P+sP_s)`.

### 1.3 Check C/D — (1.1), the recurrence, and the R7R1 fixture

Working from the **implicit** equation `P^8 = F(X, sP)` (Fable5 R7R1 review
line 203, `CONFIRMED`):

```text
C1   the constructed P solves P^8 = F(X,sP) exactly (cubic-in-t F)        TRUE
C2   q0 == p^2                                                           TRUE
C3   q1 == F1/(4 p^5)                                                    TRUE
C4   q2 == F2/(4H) - F1^2/(16 H^3)                                       TRUE
C5   P (P + s P_s) == Q + (s/2) Q_s          (Q = P^2)                   TRUE
C6   Q + (s/2)Q_s == sum ((n+2)/2) q_n s^n   => w'_(n+22) = -(n+2)q_n/16  TRUE
D1   counterfixture F = X^8+4X^4 t:  (Q^4 - X^8)^2 == 16 X^8 s^2 Q       TRUE
D2   q0 == X^2                                                           TRUE
D3   q1 == 1/X   (residue 1 at X=0, so q1 dX is NOT exact)               TRUE
```

`E = t^22 = s^22 P^22` in (2.3) gives
`W_X|_s = -(s^22/8) P(P+sP_s) = -(s^22/8)(Q + (s/2)Q_s)`, and C5/C6 turn that
into `w'_(n+22) = -(n+2) q_n/16`.  Report (1.1) is **CONFIRMED**.

The degree obstruction in R7R1 also survives my check: `deg_s` of
`(Q^4-X^8)^2` is `8d`, of `16X^8 s^2 Q` is `d+2`, forcing `7d = 2`; and `d=0`
fails because the right side is then nonzero while the left vanishes.

### 1.4 Reproducibility

```text
/tmp/r7r2/poly.py     exact untruncated bivariate Q-polynomials (dict + Fraction)
/tmp/r7r2/series.py   truncated bivariate series with Newton inverse
/tmp/r7r2/checkA.py   Check A     /tmp/r7r2/checkB.py   Check B
/tmp/r7r2/checkC.py   Check C     /tmp/r7r2/checkD.py   Check D
```

Scratch, not frozen.  Runtime: `< 2 s` total.

---

## 2. The two results that decide the question

These are mine, not the report's.  Both are stronger than anything the report
states, and together they close more than the report claims to close.

### 2.1 THEOREM R1 — rank is not capacity (regular category, fixed `U`)

Let `U = A^1 \ Z(H)`, `r = #Z(H)` over an algebraic closure, so
`chi_top(U) = 1 - r` and `S = Z(H) union {infinity}` has `#S = r+1`.

For **any** short exact sequence of algebraic connections on `U`,

```text
0 -> A -> E -> B -> 0,
```

the de Rham long exact sequence gives

```text
h^1(E) = h^1(A) + h^1(B) - ( h^0(A) + h^0(B) - h^0(E) )   <=   h^1(A) + h^1(B),
```

with equality iff the connecting map `H^0(B) -> H^1(A)` vanishes.

**Consequence.**  Bundling determinant rows into a higher-rank object can
never increase total de Rham capacity; it can only lose capacity to a nonzero
connecting map.  Concretely, for a *regular* rank-two `E` on the same `U`,
`chi_dR(E) = 2(1-r)` gives `h^1(E) = h^0(E) + 2(r-1)`, and `h^0(E) <= 2` with
`h^0(E) = 2` iff `E` is trivial (hence a vacuous gate).  So

```text
regular rank two on U   :   h^1  <=  2(r-1) + 1     (nonvacuous)
two rank-one rows on U  :   h^1  =   2(r-1) + k_m1 + k_m2   <=  2(r-1) + 2
```

**The rank-two escape is quantitatively empty even if the object existed.**
This refutes proposal §3.2 item 1 on its own terms, independently of the
typing objection, and neither the report nor the Fable5 review noticed it.

The only term in
`chi_dR = rank * chi_top(U) - sum_x Irr_x` that can beat the bound is
`- sum Irr`.  So the entire escape reduces to irregularity, and Theorem R2
closes that for the campaign's clients.

### 2.2 THEOREM R2 — the client's object is holonomic **and regular**, so `Irr = 0`

The report's headline says the canonical linear object "is not holonomic".
That is true of the *equation's* module and **false of the client's module**,
and the client's is the one that decides the campaign question.

Let `(F,G)` be any pair of polynomials in `(X,t)` — in particular the
`F = t^8 f(t^3X, t^{-1})`, `G = t^12 g(t^3X, t^{-1})` of a fully typed
polynomial Keller pair in R7R1's "Exact clients" normalisation.  Put
`P = F^{1/8}`, `s = t/P`, `W = G/P^12`, `t = sP`.  Then

```text
P^8 = F(X, sP)                                      (frozen: Fable5 R7R1 review, CONFIRMED)
```

is a **nontrivial polynomial equation for `P` over `K[X,s]`**: writing
`F = sum_j F_j(X) t^j`, it reads `P^8 - sum_j F_j(X) s^j P^j = 0`, monic of
degree 8 when `deg_t F < 8` and of degree `deg_t F` with leading coefficient
`F_d(X)s^d != 0` otherwise.  Hence `P` — and therefore `Q = P^2` and
`W = G(X,sP)/P^12` — is **algebraic over `K(X,s)`**.

Algebraic functions generate **regular holonomic** `D`-modules: `D_(X,s)*P`
embeds in a localisation of `pi_* O_Y` for the finite normalisation
`pi : Y -> A^2` of the equation, `O_Y` and localisations are regular
holonomic, finite maps are proper, and regular holonomicity is stable under
direct image and passes to submodules.  Therefore

```text
D_(X,s)*P  and  D_(X,s)*W  are regular holonomic,
Irr = 0 along EVERY divisor: at s = 0, along Z(H), and at infinity.
```

**This is global, not generic.**  It does not degrade at roots of `H`, where
the report's coordinate-change hypothesis fails: the *algebraic* equation
never used `p in L^x`.  Ramification is not irregularity.

Verified against the frozen fixture: `F = X^8 + 4X^4 t` gives
`P^8 - 4X^4 sP - X^8 = 0`, i.e. `Q^4 - X^8 = 4X^4 sP` and
`(Q^4 - X^8)^2 = 16 X^8 s^2 Q` — R7R1's own displayed equation, reproduced by
my engine at `X = 3` (Check D1).  R7R1 and Fable5 both wrote down this
algebraic equation; **the word `holonomic` occurs zero times in all four
R7/R7R1 files**, so the conclusion had not been drawn.

**Net effect on the ledger:** proposal §3.2 item 2 moves from
`PROVISIONAL / untried` to **REFUTED at the polynomial-client scope**.  The
irregularity of the canonical `t`/`s`-direction object at `t = s = 0` is not
"undefined" and not "uncomputed": it is **provably zero**.

---

## 3. Item-by-item verdicts

### Item 1 — exact `P, W, s=t/P` conjugacy and scalar equation at fixed `P` — **CONFIRMED**

(2.1), (2.2), (2.3) and (1.1) are exactly right; Checks A, B, C above.  I
found no sign, factor or chain-rule error.  Two scope notes, neither a defect:

- (2.3) is affine, not linear: the inhomogeneity `-E(P+sP_s)/(8P^21)` is
  load-bearing later (see Item 3b).
- "`P` is free data as far as this one equation is concerned" is correct for
  the single equation and is correctly hedged in Consequence 2.1.  It must not
  be read as "`P` is unconstrained": `P^8 = F(X,sP)` with `F` polynomial is a
  hard algebraic constraint, and it is exactly the one that proves Theorem R2.
  The report leaves this constraint on the table.

### Item 2 — nonlinear scalar equation for two series vs. rank two — **CONFIRMED**, and the proposal is **REFUTED** on three further counts

The report's core typing point is right.  I re-derived it and extended it.

**(a) Before linearization — CONFIRMED.**  One bilinear scalar equation on a
pair is not a connection; a rank-two connection requires
`partial_X v = A v` with `A in gl_2`, plus a compatible `s`-matrix.  None is
supplied.

**(b) After linearization — the report does not check this; I did, and the
answer is worse for the proposal.**  Linearising the determinant map at a
solution gives one *linear* equation `L_1 (dF) + L_2 (dG) = 0` in two
unknowns.  The associated module is `M_2 = D^2 / D*(L_1, L_2)`.  Its symbol
module is `O_(T^*)^2 / O*(sigma(L_1), sigma(L_2))`, a rank-one quotient, so

```text
Char(M_2) = T^* A^2 ,    dim Char(M_2) = 4.
```

That is the *maximum possible* — worse than the report's `dim 3` — and its
solution sheaf is `{(u_1,u_2) : L_1 u_1 + L_2 u_2 = 0}`, infinite-dimensional
even after fixing `s`.  So "rank two" fails **before and after**
linearization.

**(c) "and which is not rigid" — REFUTED AS A GENERAL CLAIM, true only in the
campaign's regime.**  Rank two does not imply non-rigid.  Katz's index of
rigidity for an irreducible rank-`n` system on `P^1 \ S` with regular
semisimple local monodromies is
`rig = (2 - #S) n^2 + sum_x dim Z(local monodromy)`; rigid iff `rig = 2`.  On
`U = A^1 \ Z(H)` we have `#S = r+1`, so for `n = 2`

```text
rig = (2 - (r+1))*4 + (r+1)*2 = 6 - 2r,     rigid  <=>  r = 2.
```

The Gauss hypergeometric system `2F1` (`r = 2`, punctures `0,1,infinity`) is
rank two, irreducible, and **rigid**, with its entire invariant content a
finite list of local exponents.  So the proposal's inference "rank two ⟹ not
rigid ⟹ obstruction is not a finite list of residues" is invalid.  In fairness:
the campaign's promoted codimensions (3, 4, 4, 5 under `codim = r-1+k_m`)
correspond to `r >= 4`, where `6-2r <= -2 != 2` and rank two **would** be
non-rigid with moduli of dimension `2r-4`.  So the clause is true in the
campaign's regime and false as written.  It is not the load-bearing error.

**(d) The proposal's *premise* is REFUTED, and this is the load-bearing
error.**  §3.2 asserts "the row-by-row elimination of `G` (via
`R_n = G_n - (3/2) H F_n`) is what collapses the problem to rank one."  It is
not.  The row system is one equation in two unknowns; solving it for the
`G`-side variable and reading the obstruction as the cokernel of `L_m` is
**lossless**, which is precisely what the promoted gate law
`codim(row m) = r - 1 + k_m = h^1(nabla_m)` records.  Nothing is discarded, so
there is no suppressed rank to recover.  Combined with Theorem R1, the
"raise the rank" avenue is empty in both directions: the object does not
exist, and if it did it would carry no more capacity.

**Counterexample to the general sentence "keep them together and you get a
rank-two connection".**  On `U = G_m`, the coupled system `partial_X u_1 = u_2`
keeps two unknowns and one equation.  Its solution sheaf is
`{(u_1, u_1') : u_1 arbitrary}` — infinite rank, and `chi_dR` is not
`2 * chi_top(U) = 0`.  Two series is not rank two.

### Item 3 — `M = D_(X,s)/D_(X,s) partial_X` — **CONFIRMED WITH REPAIR**

**3a. Characteristic variety — CONFIRMED.**  `gr(M) = O[xi_X, xi_s]/(xi_X)`,
so `Char(M) = {xi_X = 0}`, of dimension 3 in the 4-dimensional `T^* A^2`.
By Bernstein's inequality a nonzero holonomic module on a smooth surface has
`dim Char = 2`; `3 > 2`, so `M` is coherent and not holonomic, and
`Sol(M) = ker(partial_X)` is all functions of `s`.  All correct.

**3b. Absolute vs relative — REPAIR REQUIRED; the report omits the reading
that is charitable to the proposal, and that reading still kills it.**
`M` is not *absolutely* holonomic, but it **is relatively holonomic** over the
`s`-line: `D_(X/S)/D_(X/S) partial_X ~= O_(U x S)`, a **rank-one, regular**
relative connection.  Its relative de Rham cohomology is
`h^0 = 1`, `h^1 = r` (residues), so `chi_rel = 1 - r = 1 * chi_top(U)` with
`Irr = 0`.  This matters because it is exactly the reading under which
Malgrange's formula *is* applicable — and under it the answer is
**rank one, irregularity zero**.  The report should state this: it is a
second, independent closure, and it forecloses the obvious rebuttal
"you audited the wrong category."

**3c. Malgrange applicability — CONFIRMED.**  `chi_dR = rank * chi_top - sum Irr`
is a statement about a holonomic module / finite-rank meromorphic connection
on a *curve*.  It does not apply to a nonholonomic module on a surface, and
"the missing equation is positive irregularity" is a category error: absence
of holonomicity is not a numerical invariant.  Correct as written.

**3d. Mutation controls — one is WRONG as stated.**  The report says
`partial_s W = s^(-2) W` manufactures irregularity, `partial_s W = 0` gives a
regular connection, and "**Both share (2.3)**."  They do not.  Integrability of
`{partial_X W = A, partial_s W = B W}` requires
`partial_s A = B A`.  With `A = -(s^22/8)(Q + (s/2)Q_s)`, whose lowest term is
`-(s^22/8) p^2 != 0`:

```text
B = s^(-2) :  partial_s A = s^(-2) A  forces  A = c(X) e^(-1/s)  -> A = 0.  INCOMPATIBLE.
B = 0      :  partial_s A = 0         forces  A  s-independent    -> A = 0.  INCOMPATIBLE.
```

So **neither** control is compatible with the affine equation (2.3); both are
controls on the *homogeneous* operator, i.e. on `M = D/D partial_X`.  The
controls remain sound in that role — `W = c e^(-1/s)` has slope 1 at `s=0`,
`W = const` is regular, both annihilated by `partial_X` — so the conclusion
("irregularity is not determined by the R7R1 data") stands.  **Required
edit:** replace "Both share (2.3)" with "Both share the homogeneous operator
`partial_X` of (2.3); neither is compatible with its inhomogeneity, by
`partial_s A = BA`."

### Item 4 — does `C_L[[s]]` really witness the missing `s`-relation? — **CONFIRMED WITH REPAIR**

**Computation is right.**  `partial_X` acts coefficientwise on `L[[s]]`, so
`ker = C_L[[s]]` exactly.  `C_L = ker(d/dX : L -> L)` is the algebraic closure
of `K` in `L`, a field with `[C_L : K] <= [L : K(X)] <= 4` (char 0), so
"one independent integration constant in every formal degree over `C_L`" is
accurate.

**Two repairs.**

1. **It does not witness "not finite rank"; it witnesses "relative rank one."**
   `C_L[[s]]` is a *free rank-one* `C_L[[s]]`-module.  As an object over the
   ring of `s`-constants it is as finite-rank as it is possible to be.  The
   report's sentence "A finite-rank connection in the `s` direction cannot be
   inferred" is a correct statement about *inference*, but the exhibited
   kernel does not support the intended reading of infinitude — it supports
   Item 3b's "rank one, `Irr = 0`", which is a **better** outcome for the
   no-go.  Rewrite accordingly.
2. **It is the kernel of the equation, not of any client.**  R7R1's own
   firewall already says `G_0 = H^3` forces `Phi(0) = 1` and "descent can add
   further coupled constraints."  Theorem R2 goes further: for a polynomial
   client, `W` is *algebraic*, so `Phi` is pinned outright and the kernel is
   not free at all.  The arbitrariness of `Phi` is an artifact of integrating
   in the field `L`, exactly as R7R1 warns.  The report uses "arbitrary
   `Phi`" as evidence about the campaign; it is only evidence about (2.3).

### Item 5 — generic formal-étale and zero-`s`-slope; the boundary at `Z(H)` — **CONFIRMED WITH REPAIR**

**Étale claim — CONFIRMED, correctly scoped.**  `s_t(X,0) = 1/p`, and `p != 0`
in the *field* `L`, so `L[[s]] <-> L[[t]]` is an isomorphism.  The report
correctly says "at the generic point used by R7R1" and "étale at `t=s=0` over
`L`".

**"Zero `s`-slope" — the conclusion is right, the stated proof is a
non-sequitur, twice.**

1. *Absence of a pole does not give a slope bound.*  Airy, `partial_s^2 - s`,
   has polynomial coefficients and no pole anywhere in the finite plane, yet
   is irregular at `infinity` with slope `3/2`.  "No pole at `s=0`, hence no
   positive formal slope" is not a valid inference pattern.
2. *Worse: there is no `s`-slope to compute.*  Slopes (Levelt–Turrittin along a
   divisor) are attached to a holonomic module.  The report has just proved
   `M` is **not** holonomic.  So "its generic formal `s`-slope is zero" is
   **ill-posed as stated**, not merely under-argued.

**Two correct proofs of the intended conclusion, which the report should
substitute:** (i) Item 3b's relative reading — relative rank one, regular,
`Irr = 0`; (ii) Theorem R2 — for polynomial clients `P, W` are algebraic hence
regular holonomic, so all slopes vanish.

**Boundary at `Z(H)` — the report stops one step short.**  It says removing
`P(0) = p in L^x` "can break the coordinate change ... it is a different
theorem obligation."  Sharpen: at every `X_0 in Z(H)` we have `v(p) > 0`
(with `v` the valuation on the ramified extension; `ord_(X_0) p = e_i/4` for
multiplicity `e_i`), so `s_t = 1/(P + sP_s)` has a **pole** there and the map
is not étale — indeed not finite flat — along `Z(H) x {t=0}`.  So `p` is a
unit of the field `L` but not of the local ring, exactly as the prompt says.
But this is **not** an open obligation: Theorem R2's algebraic equation
`P^8 = F(X,sP)` holds identically, without any unit hypothesis, so the
conclusion `Irr = 0` extends across `Z(H)`.  What happens at `Z(H)` is
ramification, not irregularity.  **Required edit:** replace the deferral with
Theorem R2.

### Item 6 — the regular-holonomic direct-image paragraph — **CONFIRMED WITH REPAIR; DO NOT DELETE IT**

The report offers, in Section 6, to delete this paragraph if "too broad for a
nonproper family."  **Do not delete it.**  It is correct as written in the
category it names, and after repair it becomes the sharpest part of the
argument.  Four checks, as the prompt requires:

**(a) Nonproper maps — the claim SURVIVES, but only because it says
"algebraic".**  In the **algebraic** category, `int_f` and `f^dagger` preserve
`D^b_rh` for an *arbitrary* morphism of smooth varieties — properness is not
needed, because algebraic regular holonomicity already includes regularity at
infinity (Deligne's condition).  In the **analytic** category the
corresponding stability of `D^b_rh` under `int_f` is known for *proper* `f`;
the non-proper analytic statement is not available, and analytic/algebraic
direct images agree in general only for proper maps.  **Required edit:** add
one clause making "algebraic" explicitly load-bearing, so the paragraph cannot
be transported to an analytic or formal family.

**(b) Algebraic vs analytic scope — REPAIR as in (a).**  The Fable5 gate-law
review already made the matching observation one level down ("algebraic-vs-
analytic: they agree here precisely because the connection is regular").
The report should reuse that framing.

**(c) Moving / open divisors and confluence — the report's hedge is too vague
and should be replaced by the actual criterion.**  In this family `H = H(X)`
is fixed, so `Z(H)` does **not** move with `s`; what moves is `{P = 0}`.  The
report writes "Confluence at roots of `H` may require a nontrivial extension
analysis", which reads as an open door.  It is not one, for a reason that can
be stated exactly:

```text
merging regular singular points with BOUNDED residues  ->  regular singular point (residues add);
irregularity by confluence requires a residue/parameter BLOW-UP or a rescaling.
```

Counterexample-pair proving the dichotomy is the right one: the family
`d + a dX/X + b dX/(X-eps)` with `a,b` fixed limits, as `eps -> 0`, to
`d + (a+b) dX/X` — regular.  The family
`d + a dX/X + (c/eps) dX/(X-eps)` — residue blowing up — is the classical
Kummer confluence `2F1 -> 1F1`, which *does* produce an irregular singularity
at infinity.  The campaign's residues are `m e_i / 4`, **constants**; nothing
blows up.  So no confluent irregularity is available here.  **Required edit:**
substitute this criterion for the hedge.

**(d) Gauss–Manin confluence — the report omits the sharper citation.**  For an
*algebraic* family, the Gauss–Manin connection is regular singular (Deligne;
Katz), including for non-proper morphisms.  This is a stronger and more
directly applicable statement than generic six-operations stability, because
Gauss–Manin is the object a "pushforward along `t`" would actually be.
**Required edit:** cite it alongside the six operations.

**(e) The observation that makes the paragraph decisive, which the report
misses.**  Since regular holonomicity is stable under the algebraic six
operations, *any* irregular object built from the campaign's current inputs
must import irregularity from outside them.  The canonical illustration is the
Fourier–Laplace transform,
`FL(M) = p_(2*)(p_1^* M tensor E^(xy))`: every functor there preserves regular
holonomicity **except** the twist by the exponential module `E^(xy)`, and `FL`
of a regular Kummer module on `G_m` is a confluent-hypergeometric / Bessel
module that *is* irregular at infinity.  So the exponential twist is not one
door among many — up to Levelt–Turrittin it is **the** door.  This converts a
vague "positive irregularity would require an additional irregular input" into
a precise and checkable revival condition (Section 5).

### Item 7 — does an honest holonomic object already exist elsewhere, and does it invalidate the no-go? — **YES, it exists; NO, it does not invalidate; it STRENGTHENS**

**It exists, in two families.**

1. *Already promoted.*  The reviewed row connections
   `nabla_m = d + (m/4) dH/H`, the operators
   `L_nu(S) = 4 H S' + 4 nu H' S`, and the endpoint operator
   `M(Y) = 4 H Y' + 6 H' Y` (`= L_nu` at `nu = 3/2 == 22/4 mod 1`) are rank-one
   connections on a curve: **holonomic**, and **regular** — log poles at the
   `r` finite points *and at infinity*, where the residue is `-(m/4) deg H`.
   The Fable5 gate-law review verified the point at infinity explicitly
   ("residue `-2m in Z` there").  `Irr = 0` at every puncture.
2. *New, and forced by exactly the support/descent data the prompt asks about.*
   Theorem R2: for polynomial `(F,G)`, `D_(X,s) P` and `D_(X,s) W` are
   **regular holonomic** on the `(X,s)` surface.  This is the genuine
   two-variable holonomic object the report says is missing, and it is forced
   by polynomiality of the client — i.e. by support, not by the differential
   equation.

**It does not invalidate the no-go.**  Every one of these is *regular*.  The
existence of holonomic objects was never the obstacle; the obstacle is
positive `Irr`, and all of them have `Irr = 0`.

**Required edit — the report's headline is false and must be rewritten.**
Verdict sentence "the canonical linear object supplied by the exact
determinant identity is not holonomic" conflates the module *presented by the
equation* (`D/D partial_X`: nonholonomic, correct) with the module *generated
by the solution a client actually supplies* (`D*P`, `D*W`: holonomic and
regular).  These are different modules, and the second is the one the campaign
cares about.  Replace with:

```text
The module presented by the determinant equation alone is not holonomic
(char dim 3), so no index/irregularity invariant is defined for it.  The
module generated by an actual polynomial client IS holonomic - and is
REGULAR, with Irr = 0 at s = 0, along Z(H) and at infinity.  Either way there
is no positive irregularity.
```

That is a strictly stronger no-go and it removes the report's most obvious
failure mode: a reader concluding "just supply a holonomic object and the
escape reopens."  Supplying the holonomic object is exactly what closes it.

### Item 8 — narrowest justified allocation change for avenues 16 and 25 — **CONFIRMED WITH REPAIR** (narrower on one side, wider on the other)

Frozen ledger text, read from `APPROACHES.md`:

```text
row 16  D-module / holonomic index ... "no concrete invariant named in any input"; Unscored
row 25  Fiber monodromy / dessins / Hurwitz passports ... escape: "S:7 for the coupled
        two-coordinate branch-cycle CSP"
```

**Avenue 16 — the report is too narrow; go further, on both sub-branches.**
The report closes only "the *automatic* irregularity escape *as presently
stated*."  Justified is more:

- **Irregularity sub-branch: CLOSE at the polynomial-client scope** (not merely
  "as presently stated").  Theorem R2 makes `Irr = 0` a *proved* value, not an
  uncomputed one.  The proposal's "decisive first computation" — the
  irregularity of the `t`-direction object at `t = 0` on one frozen face — is
  hereby answered: **zero**, for every polynomial client, at every divisor.
  Do not fund it.
- **Rank sub-branch: CLOSE at the regular category** by Theorem R1.  Even a
  well-defined regular rank-two connection on the same `U` carries
  `h^1 <= 2(r-1)+1`, never more than the two rank-one rows it packages.
- **KEEP the part of avenue 16 that is real:** the index law itself
  (`codim = r-1+k_m`, `chi_dR = rank * chi_top(U) - sum Irr` with `sum Irr = 0`)
  as promoted-with-repair by the Fable5 gate review.  Row 16's blocking
  condition — "no concrete invariant named" — **is** discharged; the invariant
  is the de Rham index.  It is a *bookkeeping law*, not an escape.  Score the
  row on that basis and stop.
- **Single revival condition** (replacing the report's four-item list, which is
  correct but not the binding constraint): an explicit **exponential factor**.
  Concretely, a proof that some Keller-forced gate is a class in
  `H^1_dR(U, d + df + nu dH/H)` for a nonconstant rational `f`, whence
  `Irr_infinity = deg_infinity f > 0` and the index genuinely gains.  Absent an
  `e^f`, Levelt–Turrittin plus six-operations stability say no irregular object
  is reachable from the campaign's algebraic inputs.  The report's items
  (i)–(iv) remain the right *hygiene* checklist for any such client.

**Avenue 25 — the report is correctly narrow but under-protects the row.**
"Two series is not rank two" is right and I have refuted the rank-two escape
twice over.  But row 25's own escape, as frozen, is **S:7, the coupled
two-coordinate branch-cycle CSP** — a *permutation-monodromy / Riemann-existence*
object, not a `D`-module.  Nothing in this audit, and nothing in Theorems R1
or R2, touches it: `chi_dR` additivity and algebraicity of `P` say nothing
about transitive tuples in `S_d`.  **Required edit:** the report's "Narrow
avenue 25's rank-two escape the same way" must carry an explicit carve-out:

```text
This audit closes the D-module reading of row 25's escape.  It does NOT
downgrade S:7 (coupled two-coordinate branch-cycle CSP), which is a
permutation-monodromy object outside the scope of every theorem here.
```

Without that clause the audit will be over-applied.  The report's §3.3
unification ("rank-one rigidity is *why* the 169-passport screen produced no
kill") was already marked by Fable5 as a heuristic, not a theorem; my
Section 2 makes that heuristic *weaker*, not stronger, since the rank-two
repair of it is now refuted.

**Row 33** is not in scope for this audit and is untouched: it was reopened at
the twisted rank-one scope, which Theorems R1 and R2 leave intact.

---

## 4. Counterexamples produced against broad sentences

As required, one attempt per broad sentence.  Results:

| # | Sentence (source) | Counterexample | Outcome |
|---|---|---|---|
| 1 | "Keep `(F,G)` together and the object is a rank-two connection" (proposal §3.2.1) | `partial_X u_1 = u_2` on `G_m`: two unknowns, one equation, infinite-rank solution sheaf, `chi != 2 chi_top` | **REFUTED** |
| 2 | "...and which is not rigid" (proposal §3.2.1) | `2F1`: rank two, irreducible, rigid; `rig = 6-2r = 2` at `r=2` | **REFUTED as stated**; true for the campaign's `r >= 3` |
| 3 | "The elimination of `G` is what collapses the problem to rank one" (proposal §3.2.1) | the elimination is lossless: `codim = r-1+k_m = h^1(nabla_m)` is the full row content | **REFUTED** |
| 4 | "The irregularity of the pushforward along `t` is a positive contribution" (proposal §3.2.2) | `P^8 = F(X,sP)` ⟹ `P,W` algebraic ⟹ regular holonomic ⟹ `Irr = 0` | **REFUTED** |
| 5 | "the canonical linear object ... is not holonomic" (report §0) | `D_(X,s) P` for any polynomial `F` **is** holonomic (and regular) | **REFUTED as stated**; conclusion survives |
| 6 | "rank one and logarithmic, hence regular singular" (report §4) | `d - dX` on `A^1`: no finite poles at all, yet `Irr_infinity = 1`, `chi_dR = 0 = 1*1 - 1` | inference pattern **REFUTED**; the specific instance `nabla_m` is fine (log at `infinity` too) |
| 7 | "no pole at `s=0` ... hence no positive formal slope" (report §4) | Airy `partial_s^2 - s`: no finite pole, slope `3/2` at infinity; and `M` is nonholonomic so no slope is defined | proof **REFUTED**; conclusion survives via Item 3b / Theorem R2 |
| 8 | "Both share (2.3)" (report §3 mutation controls) | integrability forces `partial_s A = BA`; `A in s^22 L[[s]]^x` kills both `B = 0` and `B = s^(-2)` | **REFUTED**; controls valid on the homogeneous operator only |
| 9 | "regular-holonomic ... preserves regularity" (report §4) | none found in the algebraic category — the theorem holds for arbitrary morphisms | **CONFIRMED**, with the algebraic hypothesis made explicit |
| 10 | "Confluence at roots of `H` may require a nontrivial extension analysis" (report §4) | bounded residues ⟹ regular limit; Kummer confluence needs `c/eps -> infinity` | **hedge unnecessary**; replaced by an exact criterion |
| 11 | Theorem R1 itself: "bundling rows can never increase capacity" | attempted: a rank-two `E` with `h^1 > h^1(A)+h^1(B)` would need `h^0(E) > h^0(A)+h^0(B)`, impossible by left-exactness of `H^0` | **survives** |
| 12 | Theorem R2 itself: "polynomiality ⟹ algebraic ⟹ regular" | attempted: `deg_t F >= 8` makes the equation non-monic — but the leading coefficient `F_d(X) s^d` is a nonzero polynomial, so `P` is still algebraic over `K(X,s)` | **survives** |

---

## 5. What remains a legitimate irregular / higher-rank avenue

Stated narrowly, because almost nothing does.

**Closed.**

- Rank two by retaining `(F,G)`: closed twice — no such connection exists
  (Item 2), and a regular one would carry no extra capacity (Theorem R1).
- Irregularity of the `t`- or `s`-direction object at `t = s = 0` for a
  polynomial client: closed, value **zero** (Theorem R2).
- Irregularity by confluence at `Z(H)`: closed — residues are the constants
  `m e_i/4` and nothing blows up (Item 6c).
- Irregularity by "just take a direct image": closed — regular holonomicity is
  stable under the algebraic six operations (Item 6a/6d).
- Higher rank by induction/descent along `p^4 = H`: closed by additivity —
  the rank-4 pushforward of a rank-one `L`-connection decomposes into its
  `mu_4`-isotypic pieces and `chi` is additive, so it repackages the same
  information.  (This is worth recording; it is the most tempting free
  rank-raise available and it buys nothing.)

**Open, narrowly.**

1. **An exponential twist — the only door.**  A theorem exhibiting some
   Keller-forced gate as a class in `H^1_dR(U, d + df + nu dH/H)` with `f`
   nonconstant rational.  Then `Irr_infinity(f) = deg_infinity f > 0`, the
   index gains a genuinely positive term, and the object is honestly
   irregular.  Levelt–Turrittin plus six-operations stability say this is,
   up to the classification, the *only* way to reach positive `Irr` from the
   campaign's algebraic inputs.  Nothing in the determinant identity produces
   an `e^f`; a Laplace/Fourier or exponential-period reformulation of a gate
   would.  **This is an honest, well-posed, currently unsupported avenue —
   not a computation waiting to be run.**
2. **Irreducible rank `>= 2` at strictly more punctures.**  Theorem R1 fixes
   `U`.  Raising `r` raises `h^1`, but `U` is determined by `H`; raising it
   means summing over several faces, which is the pre-existing `CORNER-COVER`
   idea and which the proposal itself declined to claim as new.
3. **Non-`D`-module non-rigidity.**  Row 25's S:7 coupled two-coordinate
   branch-cycle CSP.  Untouched by everything here, and explicitly protected
   in Item 8.
4. **Nonlinear / support / descent constraints.**  Untouched, as the report
   says.  Note that these are what supply Theorem R2's hypothesis, so they are
   *more* central after this review, not less.

---

## 6. Sources

**Not fetched.**  No web tool was available in this session (Section 0.4);
these are from model knowledge, and the theorem numbers in particular should
be spot-checked against print before promotion.  Every load-bearing use is
accompanied above by a self-contained argument.

- J. Bernstein, inequality `dim Char(M) >= dim X` for nonzero coherent
  `D_X`-modules; M. Kashiwara, *On the maximally overdetermined system of
  linear differential equations I*, Publ. RIMS 10 (1974).  — Item 3a.
- P. Deligne, *Équations différentielles à points singuliers réguliers*,
  Lecture Notes in Math. 163, Springer 1970.  Regular singular connections;
  regularity of Gauss–Manin for algebraic morphisms (Ch. II).  — Items 3c, 6d.
- N. Katz, *Nilpotent connections and the monodromy theorem*, Publ. Math.
  IHÉS 39 (1970).  Regularity of Gauss–Manin.  — Item 6d.
- B. Malgrange, *Sur les points singuliers des équations différentielles*,
  L'Enseignement Math. 20 (1974), 147–176; and *Équations différentielles à
  coefficients polynomiaux*, Progress in Math. 96, Birkhäuser 1991.  Index and
  irregularity on curves.  — Item 3c.
- N. Katz, *Rigid Local Systems*, Annals of Math. Studies 139, Princeton 1996.
  §2.9 Euler–Poincaré with irregularity; index of rigidity; middle
  convolution.  — Items 2c, 5.
- R. Hotta, K. Takeuchi, T. Tanisaki, *D-Modules, Perverse Sheaves, and
  Representation Theory*, Progress in Math. 236, Birkhäuser 2008, Chapter 6
  (Thm 6.1.5 in that edition, from memory).  Stability of `D^b_rh` under the
  six operations for arbitrary morphisms of smooth **algebraic** varieties;
  the analytic counterpart requires properness.  — Item 6a.  *This is the
  citation the report already uses; my repair is only to make "algebraic"
  explicit.*
- Z. Mebkhout, *Le théorème de positivité de l'irrégularité pour les
  `D_X`-modules*, Grothendieck Festschrift III, Birkhäuser 1990; C. Sabbah,
  *Équations différentielles à points singuliers irréguliers et phénomène de
  Stokes en dimension 2*, Astérisque 263 (2000).  Slopes/irregularity along a
  divisor in dimension 2 — the framework in which "the `s`-slope" would have
  to be defined at all.  — Item 5.
- Regular holonomicity of algebraic functions: `O_Y` regular holonomic,
  `pi_*` for finite (hence proper) `pi`, localisation, and closure under
  submodules — assembled from the above.  — Theorem R2.

---

## 7. Verdict summary

| Prompt item | Verdict |
|---|---|
| 1. Exact `P,W,s=t/P` conjugacy and scalar equation at fixed `P` | **CONFIRMED** (re-derived; Checks A–D exact) |
| 2. Nonlinear scalar equation for two series as "rank two", before/after linearization | **CONFIRMED**; proposal additionally **REFUTED** on `Char = T^*A^2` after linearization, on "not rigid" as stated, and on the "elimination collapses the rank" premise |
| 3. `M = D/D partial_X`: char variety, absolute vs relative, Malgrange | **CONFIRMED WITH REPAIR** — char dim 3 and Malgrange-inapplicability correct; must add the relative reading (rank one, `Irr = 0`); mutation control "Both share (2.3)" is **wrong** |
| 4. Does `C_L[[s]]` witness the missing `s`-relation | **CONFIRMED WITH REPAIR** — kernel exact; but it is a free rank-one `C_L[[s]]`-module, and it is the equation's kernel, not any client's |
| 5. Generic formal-étale, zero `s`-slope, boundary at `Z(H)` | **CONFIRMED WITH REPAIR** — étale claim correct and correctly scoped; the slope argument is a non-sequitur and the invariant is undefined for a nonholonomic module; the `Z(H)` deferral is unnecessary and is replaced by Theorem R2 |
| 6. Regular-holonomic direct-image paragraph | **CONFIRMED WITH REPAIR — DO NOT DELETE**; make "algebraic" load-bearing, add Gauss–Manin regularity, replace the confluence hedge with the bounded-residue criterion, add the Fourier–Laplace/exponential-twist characterisation |
| 7. Honest holonomic object elsewhere; does it invalidate the no-go | **Exists (two families, one new); does NOT invalidate — it strengthens.** The report's headline sentence is **false as stated** and must be rewritten |
| 8. Narrowest justified allocation change for avenues 16 and 25 | **CONFIRMED WITH REPAIR** — avenue 16 closes *harder* (irregularity proved zero, rank proved capacity-neutral) while its index law is *kept*; avenue 25 needs an explicit S:7 carve-out |

**New results contributed by this review, for independent re-audit before
promotion:**

- **Theorem R1** (capacity subadditivity): for regular connections on a fixed
  `U`, `h^1(E) <= h^1(A) + h^1(B)` across any short exact sequence; bundling
  rows into higher rank never increases de Rham capacity.
- **Theorem R2** (client regularity): for any polynomial `(F,G)`, `P` and `W`
  are algebraic over `K(X,s)` via the frozen `P^8 = F(X,sP)`, hence generate
  regular holonomic `D_(X,s)`-modules with `Irr = 0` along `s = 0`, along
  `Z(H)`, and at infinity.
- **The exponential-twist characterisation**: up to Levelt–Turrittin and
  six-operations stability, an exponential factor is the only route to
  positive `Irr` from the campaign's algebraic inputs.

Both theorems are elementary given already-frozen material; neither is a
substitute for independent re-derivation.

---

## 8. Scope and firewall

This is a typing/no-go review of a research instrument, plus two small
positive theorems about that instrument.  It proves no endpoint nonexistence,
no survivor-family exclusion, no `G2-PSC`, `G2-BD`, cofinality, landing
theorem, degree ceiling, Keller pair, counterexample, or JC2 result.  It does
not weaken the promoted R7R1 theorem or the promoted de Rham gate law; it uses
both.  It does not bound the `q_n` tower's capacity, does not count the
nonlinear or all-order algebraic constraints, and does not touch row 25's S:7
branch-cycle CSP or row 33's twisted rank-one reopen.

Theorem R2 is scoped to **polynomial** `(F,G)`.  It says nothing about the
field-level object over `L`, where R7R1's arbitrary `Phi(s)` genuinely lives —
that distinction is the whole point of Item 4's second repair.

`jc2-lean` was not entered, listed, grepped, read, built, status-inspected or
edited at any point.  No canonical ledger, producer, frozen artifact or
adapter was modified.  No AWS mutation.  One file written.
