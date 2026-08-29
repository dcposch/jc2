# Hostile review: corrected quarter-root characteristic/de Rham tower R7R1

Reviewer: Fable5 (independent different-model hostile)  
Date: 2026-08-27  
Charge: corrected R7R1 theorem (field setup, exact conjugacy, coefficient
tower, truncation schedule, counterfixture, trace/rational descent,
mu4-conditional characters, non-truncation of `Q`, raw-client scope and the
D0..D35 successor proposal).

## Overall verdict

**Items 1-7: CONFIRMED.  Item 8: CONFIRMED except one sub-claim, which is
GAP/REPAIR: the possible determinant maximum for the frozen D3 polygons is
34, not 35.  `D35` is identically zero.**

The exact differential-algebra theorem over `L` is correct in every charged
detail, including all signs, powers, and constants; I rederived every
identity by hand and verified the whole pipeline end-to-end with an
independent exact engine, including two sharp predicted failure
coefficients that test the entire sign/power chain at once.  The single
repair is confined to the successor-compiler sentence: the top determinant
row `D35` vanishes identically because the unique top-weight raw slots
`f_2_0=x^2` and `g_3_0=x^3` are `y`-free and `[x^2,x^3]=0`.  Nothing in the
R7R1 theorem, tower, truncation schedule, counterfixture, characters, or
firewall depends on that row; the repair does not roll anything back.

## Charged artifacts (custody verified)

All six charged SHA-256 hashes were recomputed and match:

```text
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md
489647cf5726c46401f4c48c394de64d01ff73fff3a5d3168231428add1c0ea5  cases/ggv_quarter_root_characteristic_r7r1_20260827/FREEZE.md
1cdf577a2775e7cb1b9c44d0f92edeb6f612a1b52aa659a280390b37d49babaa  cases/ggv_quarter_root_characteristic_r7r1_20260827/verify_r7r1.py
b0e60671662953a50318e4989a20a08e5b84e28cb1bfaea075e241fc367a818a  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7-sol-20260827.md
2dd9d8f11e0fadff303c8afade0c1f4e52f1a1df4b5afffcea17d5e3d7890a18  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7-hostile-audit-sol2-20260827.md
4dedc255ea4de97dace097d201e7f61599f0a13b23e42c3a74cf3481d0ba6d08  cases/ggv_quarter_root_characteristic_r7_20260827/FREEZE.md
```

I also recomputed the transitively pinned
`cases/ggv_quarter_root_characteristic_r7_20260827/verify_r7.py`
= `c40820e300f39d92d757de698ecf6c8a5ad0b79711e369275b2de93dd6488244`,
matching the `PINS` table inside `verify_r7r1.py`.  Both case directories
contain exactly `FREEZE.md` and the verifier, nothing else.

## Execution disclosure

This session had a shell.  I ran:

* the producer's pinned replay
  (`python3 -B cases/.../verify_r7r1.py`): PASS, exit 0; it re-verifies the
  four `PINS` and re-executes `verify_r7.py`'s free-variable Laurent-ring
  identity checks, which I audited by reading;
* `/tmp/fable5_r7r1_series.py`: my own exact Laurent-in-`X` / truncated
  series engine (Fractions only, no producer code), which computes `E(F,G)`
  directly from constructed `G` on three fixtures and matches two exactly
  predicted defect coefficients (details under Items 2-4);
* `/tmp/fable5_r7r1_chart_slots.py` plus follow-up one-liners: a universal
  monomial-pair proof of the chart identity, and the frozen D3/D5G data
  analysis that produced the `D35` finding.

No file inside `jc2-lean` was read or touched.  No repository file was
written except this review.  Producer `PASS` strings, the R7 prose, and the
Sol2 audit were treated as claims, not evidence.

---

## Item 1 — Field setup

**Verdict: CONFIRMED.**

* Existence of `P`: `F_0=H^2` (nonzero, per R7's retained setup) and
  `p^8=H^2=F_0`, so `P=p*(1+u)^(1/8)` with `u=(F-F_0)/F_0 in tK(X)[[t]]`
  is a well-defined binomial branch in `L[[t]]` (characteristic zero,
  rational binomial coefficients), and `P^8=p^8(1+u)=F`, `P_0=p`.
* Uniqueness: if `P~^8=F` with `P~_0=p`, then `v=P~/P` satisfies `v^8=1`,
  `v_0=1`; if `v=1+ct^k+...` with `c!=0` then `v^8=1+8ct^k+...!=1`.  So
  `v=1`.
* `p` itself: `Z^4-H` need not be irreducible over `K(X)`; `L=K(X)(p)` is a
  field of degree 1, 2, or 4, and nothing in Items 1-5 uses the degree.
  The counterfixture (`H=X^4`, `p=X`, `L=K(X)`) is exactly the degree-one
  degenerate case and all identities hold there (verified numerically).
* `d/dX` extends uniquely to the finite separable extension `L/K(X)`;
  concretely `p'=H'p/(4H)`.  The constant field is
  `C_L=ker(d/dX)` = the algebraic closure of `K` in `L` (it can exceed `K`,
  e.g. `2^(1/4)` for `H=2X^4`), which is exactly how (0.3) uses it.
* `s=t/P=(1/p)t+O(t^2)` has invertible linear coefficient `1/p in L^x`,
  hence a unique compositional inverse `t=T(X,s) in sL[[s]]`; `d/dX`
  commutes with the substitution by the formal chain rule.

## Item 2 — Exact signs and powers in the conjugacy

**Verdict: CONFIRMED.**

Independent product-rule derivation with `F=P^8`, `G=P^12W`:

```text
12F_XG-8FG_X = 96P^19P_XW-(96P^19P_XW+8P^20W_X) = -8P^20W_X,
F_XG_t-F_tG_X = 8P^19(P_XW_t-P_tW_X),
E = 8P^19((tP_t-P)W_X-tP_XW_t).
```

With `s_X=-tP_X/P^2`, `s_t=(P-tP_t)/P^2`:

```text
J(s,W)=s_XW_t-s_tW_X=((tP_t-P)W_X-tP_XW_t)/P^2,   so   E=8P^21J(s,W).
```

Passing to `(X,s)`: `J=-s_t*W_X|s`, `1/s_t=t_s=P+sP_s`, `t^22=s^22P^22`,
and `P(P+sP_s)=Q+(s/2)Q_s` for `Q=P^2`.  Under `E=t^22` this gives exactly

```text
W_X|s=-(s^22/8)(Q+(s/2)Q_s).
```

(The first equation of (0.2) is unconditional; the second and third hold
under the target, as the producer's phrasing states.)

End-to-end numeric confirmation of every sign and power at once.  For
arbitrary `W`, the derivation above gives the exact defect law

```text
E-t^22=-8P^21R/(P+sP_s),   R:=W_X|s+(s^22/8)(Q+(s/2)Q_s),
```

so if `R=rho_m s^m+O(s^(m+1))`, the first defect coefficient in `t` is
`-8p^(20-m)rho_m`.  My engine computed `E(F,G)` directly (no transform)
from constructed `G` and matched this prediction exactly:

* `F=X^8+4X^4t`, `G=P^12-(X^3/24)t^22P^-10`:
  `E=t^22-(3/2)X^-4 t^23+O(t^24)`, with
  `-(3/2)X^-4=-8p^-3*(3/16)q1`, `q1=1/X`.
* `F=X^8+X^6t`, `G=P^12+w22t^22P^-10+w23t^23P^-11+w24t^24P^-12` (rows
  0-2 integrated): `E=t^22+O(t^25)` and
  `E_25=-55/(1024X^6)=-(5/2)X^-5*q3` with `q3=11/(512X)`
  (hand-derived and independently reproduced by the implicit series
  solver).

A wrong power of `P`, a wrong sign, or a wrong `-(n+2)/16` anywhere in the
chain would have broken these equalities.

## Item 3 — Coefficient theorem, converse, full kernel, `G0=H^3`

**Verdict: CONFIRMED.**

* Coefficient comparison: `Q+(s/2)Q_s=sum((n+2)/2)q_n s^n`, so the target
  equation reads `w_(n+22)'=-(1/8)((n+2)/2)q_n=-(n+2)q_n/16`, and rows
  `m<22` read `w_m'=0`.  Every scalar `(n+2)/16` is nonzero in
  characteristic zero, so exact `E=t^22` forces every `q_n dX=d(-16
  w_(n+22)/(n+2))` exact in `L`: forward necessity holds.
* Converse over `L`: given primitives `q_n=a_n'`, set
  `w_(n+22)=-(n+2)a_n/16`, `w_0=...=w_21=0`, `G=P^12W(X,t/P) in L[[t]]`;
  reversing the (all-formal, all-invertible) steps gives `E=t^22`.
  Verified concretely on two fixtures whose rows 0-2 are exact
  (`E=t^22+O(t^25)` from the constructed primitives, including the
  `F2/(4H)` term via `F=X^8+X^6t+X^4t^2`, `q2=3/16`).
* Full kernel: solutions of each row differ by `C_L`; the homogeneous
  space is all of `C_L[[s]]`, i.e. *every* coefficient, `w_m` for `m<22`
  and every `w_(n+22)`, carries an independent constant.  My engine
  verified the invariance exactly: adding `5s^22` and `7s^3` to `W`
  (i.e. `5t^22P^-10+7t^3P^9` to `G`) left `E` unchanged through `t^26`.
  The R7R1 repair of R7's `w0..w21`-only kernel phrase is correct.
* `G0=H^3  <=>  Phi(0)=1` holds under the audit's particular-solution
  normalization `w_0=...=w_21=0` (then `G_0=p^12Phi(0)=H^3Phi(0)`).  Nit,
  not a defect: (0.3) leaves `W_particular` unnamed, and the constant
  shifts if a different particular solution is chosen; the intended
  reading is the constructed one.  The frozen D5G client is consistent
  with this normalization: its pinned leading rows are `F0=H^2`,
  `G0=H^3` with `H=X^8-1` (recomputed from `DIRECT_DETERMINANT.json`).

## Item 4 — Sharp truncation rule and the counterfixture

**Verdict: CONFIRMED.  The counterfixture really separates `q0` from `q1`.**

* Rule: for `N>22`, `E=t^22+O(t^N)` transforms to the row equations
  modulo `s^N` (all divided factors are units, `ord_s=ord_t`), forcing
  exactly `q_n dX` exact for `n+22<N`; and conversely, integrating only
  those rows (higher `w_m:=0`) reconstructs `E=t^22+O(t^N)`.  So the
  licensed rows are exactly `n+22<N`; `mod t^23 -> q0`;
  `mod t^24 -> q0,q1`; `mod t^25 -> q0,q1,q2`.  Sharp in both directions.
* Counterfixture `H=X^4`, `p=X`, `F=X^8+4X^4t` (here `L=K(X)`):
  independent implicit-solve gives `q0=X^2` (exact, `X^3/3`),
  `q1=1/X` (residue 1 at `X=0`; a rational derivative has zero residues,
  so `q1 dX` is not exact in `K(X)`; also robust to the root choice:
  `p=zeta X` gives `q1=zeta^-5/X`, still a nonzero residue),
  `q2=-1/X^4`.
  My engine confirmed the separation concretely:
  `G=P^12-(X^3/24)t^22P^-10` gives `E=t^22-(3/2)X^-4t^23+O(t^24)` --
  the endpoint identity `mod t^23` holds, and the `t^23` failure is
  exactly the non-integrable `(3/16)q1` row, which no choice of
  `w23 in K(X)` (or of the free constants) can remove.  So
  `mod t^23` solvable, `mod t^24` unsolvable: real separation.
* Beyond the charge, my second fixture `F=X^8+X^6t` separates the
  schedule again two rows higher: `q0,q1,q2` exact (`X^2, X/4, -1/16`),
  `mod t^25` solvable, but `q3=11/(512X)` has a residue, and the
  computed defect `E_25=-55/(1024X^6)` appears exactly where the rule
  says.  The schedule is sharp at every displayed cutoff.

## Item 5 — `q0,q1,q2`, trace descent, R5, rational `q2`, degenerate Kummer

**Verdict: CONFIRMED.**

* Independent implicit expansion of `P^8=F(X,sP)` with
  `P=p+as+bs^2+O(s^3)`:
  `a=F1/(8p^6)`, `b=F2/(8p^5)-5F1^2/(128p^13)`, hence

  ```text
  q0=p^2,  q1=2pa=F1/(4p^5),
  q2=2pb+a^2=F2/(4p^4)-F1^2/(16p^12)=F2/(4H)-F1^2/(16H^3).
  ```

  All three verified numerically on three fixtures, including a nonzero
  `F2`.  The producer's constants are exact; the audited `1/15` mutation
  control in `verify_r7.py` guards the only fragile denominator.
* Trace descent of `q0`: `Tr_(L/M)` commutes with the unique extended
  derivation on a finite separable extension, so `q0 dX=da` in `L` gives
  `q0 dX=d(Tr a/[L:M])` in `M=K(X)(p^2)`; converse trivial.  In
  `M=K(X)(w)`, `w^2=B` (`H=A^2B`, `B` squarefree), a general primitive
  `r+uw` forces `A=u'+uB'/(2B)`; substituting `u=vB` gives exactly
  `A=Bv'+(3/2)B'v` with `v in K(X)`.  The pole argument (rederived: at a
  non-root of `B`, a pole of order `m` survives with leading `-mB(x0)`;
  at a simple root, with leading `(3/2-m)cB'(x0)`, never zero) forces
  `v in K[X]`.  This is literally the reviewed R5 criterion (0.2),
  including its polynomial-`v` form; R5 is the grade-zero shadow of
  R7R1, as claimed.
* Rational `q2` descent: `q2 in K(X)`; if `q2 dX` is exact in `L`,
  tracing to `K(X)` and dividing by `[L:K(X)]` gives a rational
  primitive.  So whenever rows through weight 24 are licensed
  (`E=t^22+O(t^25)`), rational exactness of `q2 dX` is a genuine
  base-field necessary condition.  Correct as stated.
* Reducible/small Kummer: none of Items 1-5 uses `[L:K(X)]=4`.  The
  degree-one case is the verified counterfixture; the degree-two case
  (`H` a square) makes `q0` descend to `K(X)` where a polynomial `A`
  always integrates -- consistent with R5's `b=0` branch passing the
  endpoint automatically.  No constant or formula breaks.

## Item 6 — Repaired character statement

**Verdict: CONFIRMED, including the necessity of both conditions.**

After adjoining `mu_4` (base `K'=K(zeta)`) *and* assuming `p->zeta p`
defines an automorphism `sigma` of `L'=K'(X)(p)` over `K'(X)` (this
requires `Z^4-H` irreducible over `K'(X)`): apply `sigma` coefficientwise
to the implicit equation `P^8=F(X,sP)`.  Then `sigma(P)` and
`R(X,s):=zeta P(X,zeta s)` both solve it with constant term `zeta p`, and
the order-by-order linearization `8(zeta p)^7 != 0` gives uniqueness, so

```text
P^sigma(X,s)=zeta P(X,zeta s)   =>   Q^sigma(X,s)=zeta^2 Q(X,zeta s)
   =>   q_n^sigma=zeta^(n+2) q_n.
```

That is the correct action on `s` (`s -> zeta s` inside the argument,
`sigma` on coefficients), and the exponent pattern `(n+2) mod 4 =
2,3,0,1,...` matches.  Spot-checks: `q0=p^2 -> zeta^2 q0`;
`q1=F1/(4p^5) -> zeta^-5 q1=zeta^3 q1`; `q2` rational `-> zeta^4 q2=q2`.
Both hypotheses are necessary: for `H=X^4`, even over `K(i)` no
automorphism fixing `K(i)(X)` can send `p=X` to `iX`, so the unqualified
four-character claim fails there and only the exponent grading survives --
exactly the R7R1 repair.  The producer's conditional wording is correct.

## Item 7 — No truncation of `Q`; algebraic equation; no finite bound

**Verdict: CONFIRMED.**

For the counterfixture, the implicit equation gives in two lines
`Q^4=P^8=X^8+4X^4sP` and `(Q^4-X^8)^2=16X^8s^2P^2=16X^8s^2Q`; my engine
verified the displayed equation as an exact series identity through
`s^8`.  If `Q` were a polynomial in `s` of degree `d>=1`, the two sides
have exact degrees `8d` and `d+2` (leading coefficients `q_d^8` and
`16X^8q_d`, nonzero in a characteristic-zero domain), forcing `7d=2`,
impossible; `d=0` fails directly (`0!=16X^8s^2X^2`).  A power series that
is not a polynomial has infinitely many nonzero coefficients, so this
bounded (t-degree 1!) polynomial `F` yields infinitely many nonzero
`q_n`.  Bounded raw support therefore does not truncate `Q`, R7's
"effectively finite" phrase was genuinely false, and its deletion is the
correct repair.  R7R1 infers no finite decision bound and no finite
recurrence certificate; none may be inferred.  (Distinct and compatible:
for a bounded-polygon client the *determinant target* is finitely
decidable -- see Item 8 -- but that decides `E=t^22`, not the tower
row-by-row.)

## Item 8 — Raw-client scope, chart identity, D3/D5G, successor range

**Verdict: chart identity, support maxima, and D5G licensing CONFIRMED;
the "possible determinant maximum 35" / "full possible determinant range
D0,...,D35" sub-claim is GAP/REPAIR: `D35` is identically zero and the
sharp possible maximum is `D34`.**

* Chart identity, proved universally.  For monomials `F=X^aT^b`,
  `G=X^cT^d`, both sides of `[f,g]_(x,y)=t^-22E(F,G)` under
  `x=t^3X, y=t^-1, f=t^-8F, g=t^-12G` are the single monomial
  `x^(a+c-1)y^(3(a+c)+19-(b+d))` with the *same* coefficient
  `12a-8c-ad+bc`; by bilinearity this proves the identity for all
  polynomial pairs.  Machine sweep over all `7^4` monomial pairs plus 20
  random dense pairs: all equal.  Hence exactly `[f,g]=1 <=> E=t^22`,
  and a fully typed polynomial Keller pair licenses (0.1) and every row.
* D3 support maxima.  From the frozen `RAW_INPUT.json`: 141 `F` slots
  with weights exactly `0..14`, 301 `G` slots with weights exactly
  `0..21`; the weight formulas `3a-b+8` / `3a-b+12` hold slot-by-slot.
  Maxima 14/21 CONFIRMED.
* Which rows current D5G licenses.  `DIRECT_DETERMINANT.json` contains
  exactly the 23 rows `D0..D22` (weights `0..22`), with the recurrence
  string `D_n=sum_(i+j=n)((12-j)F_i'*G_j+(i-8)F_i*G_j')`, which I
  rederived independently from `E`.  A client certified through D5G with
  `D0=...=D21=0, D22=1` has `E=t^22+O(t^23)` and is licensed exactly the
  `q0` row (`n+22<23`), nothing more; and D5G itself asserts no Keller
  specialization (`claims_not_made` checked), so unconditionally it
  licenses nothing.  The producer's "no `q1` or `q2` conclusion by
  itself" is exactly right.
* **The finding: `D35 == 0` identically on the frozen polygons.**  The
  only weight split for `D35` is `(i,j)=(14,21)`.  The frozen data has
  exactly one `F` slot of weight 14, `f_2_0` (raw monomial `x^2`,
  `X`-exponent `u=2`), and exactly one `G` slot of weight 21, `g_3_0`
  (raw `x^3`, `v=3`).  The `D_n` coefficient of a slot pair is
  `((12-j)u+(i-8)v)X^(u+v-1)`; here `(12-21)*2+(14-8)*3=-18+18=0`.
  Structurally this is forced: `y`-free raw monomials satisfy
  `[x^u,x^v]=0`, and I verified the general statement that every pair of
  `y`-free slots contributes zero to every `D_n`
  (`(12-(3v+12))u+((3u+8)-8)v=0` identically).  Both polygon corners are
  `y`-free, so the top row is dead.  By contrast every row `D23..D34` is
  generically nonzero (explicit slot-pair witnesses computed for each,
  e.g. `D34` via `f_2_1*g_3_0` with coefficient `-3` and `f_2_0*g_3_4`,
  `f_2_0*g_4_4` with `+2,+8`).  So `14+21=35` is only the support-degree
  bound; the sharp possible determinant maximum is **34**.
* Repaired successor scope.  The smallest honest compiler successor for
  the whole tower is a direct extension of reviewed D5G through
  `D0..D34`, with exact target mutations at `D23` and `D24` as proposed;
  `D35` should be carried, if at all, only as a proven
  identically-zero row, never as a live "possible" row.  A genuine
  Keller specialization imposes the **35** nontrivial conditions
  `D0=...=D21=0, D22=1, D23=...=D34=0` (`D35=0` is automatic), and --
  since `E` is then a `t`-polynomial of degree `<=34` -- this is
  equivalent to exact `E=t^22` and licenses the whole tower, exactly as
  the producer intends.  If the goal is only the currently derived new
  rows `q1,q2`, the smaller extension `D0..D24` already suffices; the
  producer's "smallest" is correct only relative to the full-tower goal
  and the corrected endpoint `D34`.
  The `verify_r7r1.py` line `assert 14+21==35` is arithmetically true
  and stays green; it is its comment ("the full determinant can run
  through weight 35") and the producer sentences naming `D35` that need
  the one-row repair.

Context notes, recorded for the successor (no verdict impact):

* The pinned artificial-face leading rows are `F0=H^2, G0=H^3` with
  `H=X^8-1`, squarefree of degree 8.  By reviewed R5's degree law
  (`b=8` excluded; rederived here) plus R7R1's `q0` row and trace
  descent, `q0 dX` is not exact even in `L`, so *no* slot values on the
  current pinned polygons can reach `E=t^22+O(t^23)`.  The exact-target
  determinant system on the current artificial fixture is infeasible;
  this substantiates the producer's firewall sentence and means the
  `D0..D34` successor pays off on re-sourced polygons/faces, or as an
  independent second exclusion route for this one.
* D5G's `D0="ZERO"` replay is consistent:
  `12F0'G0-8F0G0'=(24-24)H^4H'=0` identically for `F0=H^2, G0=H^3`.

## Verifier quality note

`verify_r7r1.py` is honest but thin: beyond the four `PINS` and the D3
maxima re-read, its new asserts are arithmetic stand-ins
(`Fraction(1,3)*3==1`, `Fraction(-3,24)==Fraction(-1,8)`,
`8d!=d+2`, the `(n+2)%4` pattern, `14+21==35`) that *pin* the corrected
claims but do not machine-check the analysis.  The mathematical load is
carried by `verify_r7.py`'s free-variable Laurent-ring identities (audited
by reading: conjugacy (1.1)/(1.2), the `P*t_s` identity, the implicit
`q0/q1/q2` rows with the `1/15` mutation, the R5 primitive identity) plus
prose.  My independent engine now supplies the missing end-to-end machine
checks (direct `E` computation from constructed `G`, exact predicted
defects, kernel invariance, a `w23` denominator mutation).  No vacuous
pass was found; the replay is deterministic and off-line.

## Theorem versus proposed finite computational use

The theorem is an exact statement over `L[[s]]`/`L[[t]]`: conjugacy,
row-by-row de Rham necessity, converse over `L` with kernel `C_L[[s]]`,
truncation schedule, trace-descended `q0`/`q2` conditions, and the
conditional character law.  Its computational use is strictly as a
necessary-condition generator: finitely many determinant rows
(`D0..D34` for the frozen polygons) decide the exact identity for a
bounded client, and each licensed `q_n` row is a Hermite-reducible test
that can only kill or silently pass a client.  R7R1 proves no descent of
the converse to `K(X)`, no polynomiality, no finite tower bound and no
finite recurrence certificate, no raw landing, no face/family exclusion,
no `G2-PSC`, no `G2-BD`, no Keller pair, no counterexample, and no JC2.
The producer's firewall states exactly this and is CONFIRMED.

## Promotion wording

Exact wording under which R7R1 may be promoted:

> **PASS-R7R1-QUARTER-ROOT-DE-RHAM-TOWER-OVER-L (different-model hostile
> review, Fable5, 2026-08-27).**  Over any characteristic-zero `K` with
> `F_0=H^2!=0`, `p^4=H`, `L=K(X)(p)`: the unique branch `P=F^(1/8)` with
> `P_0=p` exists in `L[[t]]`; `s=t/P` is formally invertible;
> `E=8P^21J(s,W)` identically for `W=G/P^12`; `E=t^22+O(t^N)` (`N>22`)
> holds for some `G` over `L` iff `q_n dX` is exact in `L` for every
> `n+22<N`, via `w_(n+22)'=-(n+2)q_n/16`, with full solution space
> `W_particular+C_L[[s]]` (and `Phi(0)=1` iff `G_0=H^3`, in the
> normalization `w_0=...=w_21=0`); `q0=p^2`, `q1=F1/(4p^5)`,
> `q2=F2/(4H)-F1^2/(16H^3)`; `q0` trace-descends to the reviewed R5
> criterion `A=Bv'+(3/2)B'v` and licensed `q2`-exactness descends to
> `K(X)`; `q_n^sigma=zeta^(n+2)q_n` exactly after a `mu_4` base change in
> which `p->zeta p` is an automorphism; bounded raw support does not
> truncate `Q` and no finite decision bound is proved; for the typed
> `8/28` chart, `[f,g]_(x,y)=t^-22E`, so `[f,g]=1 <=> E=t^22`; frozen
> D5G (`D0..D22`) licenses exactly the `q0` row.  **Successor repair
> (required before any D-range freeze):** on the frozen D3 polygons
> `D35==0` identically (`y`-free corners `x^2`,`x^3`); the sharp possible
> determinant maximum is `D34`; the full-tower successor is `D0..D34`
> with exact target mutations at `D23`,`D24`, and a genuine Keller
> specialization imposes the 35 nontrivial rows
> `D0..D21=0, D22=1, D23..D34=0`.  No descent of the converse, no
> polynomiality, no finite tower bound, no raw landing, no face/family
> exclusion, no `G2-PSC`, no `G2-BD`, no counterexample, no JC2.

R7R1's own text may be promoted as-is on Items 1-7; the two sentences
naming `D0,...,D35` (successor range and Keller specialization) and the
`verify_r7r1.py` comment line are the only places requiring the
`D34` correction, preferably as a one-paragraph additive erratum rather
than an edit to the frozen bytes.
