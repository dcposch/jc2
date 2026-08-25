# Hostile combined review: AS F-only `p=3,D=7` full-C5 D7 gate and first following Cartier gate

Different-model hostile review (Claude, model `claude-fable-5`, 2026-08-24)
of the conjunction of two frozen targets.  The successor consumes the parent,
so the verdict below is for the conjunction at its exact frozen scope, with
separate promotable sentences for each target.

| Item | Value |
| --- | --- |
| Target 1 (parent) | `xmodel/as-fonly-d7-vertical-full-c5-d7-gate-20260824.md`, charged SHA-256 `907dcc72523eb228a7ac6581826460601030e56c996d4df583b2fad274f09a6e` |
| Target 1 case | `cases/as_fonly_d7_vertical_full_c5_d7_gate_20260824/`, charged manifest `9454ffa7cc0f14c2eaa5095b8ba45f78d3033c2022967d6c0011550e5e198cb7`, charged freeze `c0299b4637131bb1e8f637f25d692a4d41ff86a6c6567d258f567917032858e3` |
| Target 2 (successor) | `xmodel/as-fonly-d7-vertical-next-cartier-20260824.md`, charged SHA-256 `cfd77aacacf5c47c74e001c26cfb5369e69b7545bd1d301627135f06fd30af15` |
| Target 2 case | `cases/as_fonly_d7_vertical_next_cartier_20260824/`, charged manifest `0c0d88b80038ed266bc57431cde7d395ebe592497ccdd0e9830480d26a41551f`, charged freeze `e7742fbfaee95fa4e2e88cd34635fb3c38374ac3cd3d637257eaa563beb88444` |
| Git HEAD (frozen basis, per both FREEZE files and session snapshot) | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` |
| Smallest false identity | none found |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking remarks in Section 9; the two degree-5/6 divergence-surjectivity facts used by the successor are witnessed by frozen unit-pivot asserts in the consumed generators, not restated in the reports) |
| Overall verdict | **CONFIRMED** (conjunction, exact frozen scope) |

## 0. Execution capability and method

This review session had no shell: `Bash` is unavailable.  I therefore could
not run either replay, recompute any SHA-256, or rerun the `3^7`-base
enumerations.  Per the registered protocol for shell-less review sessions,
the verdict rests on (i) full byte-level inspection of every program in both
cases and of the consumed frozen generator chain, (ii) independent hand
algebra over the integers reproving every displayed identity that is
hand-computable, (iii) exhaustive cross-checking of the frozen attestation
web (reports, FREEZE, MANIFEST, EXPECTED_OUTPUT, upstream reviews), and
(iv) internal-consistency arithmetic that the frozen counts must satisfy and
do.  Section 8 lists exactly which items rest on frozen attestations and
embeds the staged commands that close every such gap on any shell-enabled
session.  No producer, case, canonical, coordination, prompt, log, run, or
review byte was edited; this file is the only file written.

Read in full: both target reports; all eight files of the parent case; all
seven files of the successor case; the consumed
`cases/as_fonly_d7_vertical_d7_source_license_20260824/audit_full_e1_degree7.py`;
the consumed `cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/generate_corrected.py`;
the consumed `cases/as_fonly_d7_degree10_pointwise_20260824/generate_degree10_gate.py`;
`xmodel/as-fonly-d7-vertical-d7-source-license-20260824.md`;
`xmodel/as-fonly-d7-vertical-d7-cap-boundary-combined-review-claude-20260824.md`
(CONFIRMED, licenses the source-license identity and the eight-row slice);
`xmodel/as-fonly-d7-postd10-d98-f3-corrected-source-review-grok-20260824.md`
(CONFIRMED, licenses `det J-1=3L+9(K+C_x+D_y)+27M+81N` and the D9/D8 core);
`xmodel/as-fonly-d7-vertical-state-sufficiency-review-grok-20260824.md`
(CONFIRMED, licenses the `7 x 5` core as a state theorem).

## 1. Framework identity, re-derived

From `P=x-x^3+3U+9C+27W`, `Q=y+3V+9D+27Z` I re-derived by hand

```text
det J-1 = 3L + 9(K+C_x+D_y) + 27(M+W_x+Z_y) + 81N',
L=U_x+V_y-x^2,  K=(U_x-x^2)V_y-U_yV_x,
M=(U_x-x^2)D_y+C_xV_y-U_yD_x-C_yV_x,
```

where `N'` collects `C_xD_y-C_yD_x`, the `27`-digit crosses
`(U_x-x^2)Z_y+W_xV_y-U_yZ_x-W_yV_x`, and higher terms.  With `W=Z=0` this is
exactly the licensed identity `(det J-1)/27=E1+M+3N`,
`E=L/3+K+C_x+D_y=3E1`, confirmed independently twice upstream (grok
corrected-source review; claude combined review).  Two consequences used
below, both checked by hand:

- the Jacobian matrix of the seed is the identity modulo three
  (`P_x≡Q_y≡1`, `P_y≡Q_x≡0 mod 3`), so every cross term of a `27`-level
  digit with anything else lands at order 81;
- on the charged vertical normal form
  (`U0=h x^2y+p y^4+2r xy^3+q x^3y+2t x^4`,
  `V0=2h xy^2+x^2y+r y^4+s xy^3+t x^3y+w x^4`, `u5=v5=0`, Frobenius layer
  `UF=fua y^6+fa x^3y^3+fb x^6`, `VF=fc y^6+fd x^3y^3+fvb x^6`),
  `L=6h xy+6r y^3+3q x^2y+9t x^3+3s xy^2+3fa x^2y^3+6fb x^5+6fc y^5+3fd x^3y^2`
  is formally divisible by 3 with `deg L1<=5` and degrees `{2,3,5}` only.

## 2. Charge 1 — integer divided-carry source of the eight full D7 rows

**No lost divided term.** Adjoining `C5,D5` leaves `[E1]_7` unchanged:
`L/3` and `K` contain no current digit, and `[C_x+D_y]_7=0` because
`deg C,D<=7` gives derivative degree at most six.  So
`[E1]_7=[K]_7/3=[single-Frobenius K/3]_7` survives verbatim from the license
(K0 caps at degree 6; the double-Frobenius bracket is divisible by nine).  I
re-expanded `[K_single/3]_7` by hand and got exactly the licensed raw row
values (`y^7: 2fua h`; `xy^6: fc h+2fua`; `x^2y^5: fc`; `x^3y^4: 2fa h`;
`x^4y^3: 2fa+fd h`; `x^5y^2: 2fd`; `x^6y: 2fb h`; `x^7: 2fb+fvb h`).

**No premature reduction.** `audit_full_c5_source.py` builds
`Mfull=A·D_y+C_x·v_y-u_y·D_x-C_y·v_x` with the source license's integer
arithmetic (`sl` namespace: integer `eadd/emul`, no `%3`), with the full
six-direction Frobenius first digit inside `A,v_y,u_y,v_x` and
`C=C5+C6+C7`, `D=D5+D6+D7`, and reduces modulo three only in
`residual7=degree_part(mod3(Mfull+E1_7),7)`.  The Frobenius first-digit
derivatives are all `3`-divisible, so they die in `M mod 3` — asserted in
the frozen license (`mod3(M)==mod3(M0)`) and reproved by hand.

**No unlicensed carry representative.** The only divisions in the whole
parent chain are `[K]_7/3` (formal: every integer coefficient of
`K_single` is `3`-divisible) and the licensed `L/3`.  All substitutions
(`sub_digits`, `normal`, `pivot_sub`, `coord`) are mod-3 unit-pivot
eliminations and an invertible triangular change; no integer lift of a
solved row is chosen anywhere.

**The new degree-seven layer, fully hand-expanded.** Modulo three the
degree-three parts of the four derivative fields are spanned by the cubes
`x^3,y^3`:

```text
[A]_3=2r y^3+2t x^3,  [v_y]_3=r y^3+t x^3,
[u_y]_3=p y^3+q x^3,  [v_x]_3=s y^3+w x^3,
```

because every non-cube coefficient (`3q x^2y`, `3s xy^2`, `6r xy^2`,
`3t x^2y`) is `3`-divisible.  Hence the `C5,D5` contribution to degree seven
is `M5_7=c5_x[v_y]_3+[A]_3 d5_y+2[u_y]_3 d5_x+2[v_x]_3 c5_y`, and after the
triangular coordinates (write `rho=Rr+sh`, `tau=Tt+wh`, `pi=Pp+Rr h+2sh^2`,
`kappa=Qq+Tt h+2wh^2`) the eight rows of the gate are, by my independent hand
computation,

```text
(0,7): 2fua h + rho(c5_1+d5_0) + 2pi d5_1 + s c5_0
(1,6): fc h+2fua + 2rho(c5_2+d5_1) + pi d5_2 + 2s c5_1
(2,5): fc
(3,4): d6_1+2fa h + rho(c5_4+d5_3) + 2pi d5_4 + s c5_3
        + tau(c5_1+d5_0) + 2kappa d5_1 + w c5_0
(4,3): Rr+fd h + 2rho(c5_5+d5_4) + pi d5_5 + 2s c5_4
        + 2tau(c5_2+d5_1) + kappa d5_2 + 2w c5_1
(5,2): 2fd
(6,1): d6_4+2fb h + tau(c5_4+d5_3) + 2kappa d5_4 + w c5_3
(7,0): Tt+fb+fvb h + 2tau(c5_5+d5_4) + kappa d5_5 + 2w c5_4
```

(expanded in the frozen rows; the slice parts were re-derived from scratch,
including the `sub6` eliminations `d6_2 -> -(K5_(2,3)+fa)` and
`d6_5 -> -(K5_(5,0)+2fb)` whose charged values `r+2hs` and `t+2hw` are
absorbed exactly by `coord` to give `Rr+fd h` and `Tt+fb+fvb h`).

**Why exactly six rows change and `fc=fd=0` survive.** The two degree-seven
Cartier monomials `(2,5),(5,2)` (both exponents `≡2 mod 3`) can be reached
from a cube shift `(0,3)` or `(3,0)` only from a digit-derivative monomial
with residues `(2,2)`, i.e. `x^2y^2`; but `[x^2y^2]c5_x=3c5_3`,
`[x^2y^2]d5_y=3d5_2`, `[x^2y^2]d5_x=3d5_3`, `[x^2y^2]c5_y=3c5_2` all vanish
modulo three.  So rows 2 and 5 receive nothing, while each of rows
`0,1,3,4,6,7` receives a generically nonzero form (displayed above).  The
frozen asserts `slice_rows==sl["actual"]` and `changed==[0,1,3,4,6,7]` pin
this bytewise, and the compiler independently rebuilds the same rows by the
incremental path (`old7 + M5`) and asserts exact equality with the audit
(`assert d7_rows == source_ns["d7_rows"]`).  The negative control against
the licensed slice is genuine and correctly load-bearing.

## 3. Charge 2 — accepted degree-four block and lower completion

**Block (8), verified over the integers.**
`[E]_4=[K0]_4+[C5_x+D5_y]_4` since `[L1]_4=0` (asserted and hand-checked:
`L1` has degrees `2,3,5`) and `K_single` starts at degree seven.  By hand,
`[K0]_4=6h^2 x^2y^2-4h x^3y-x^4` over `Z`, i.e. `2h x^3y+2x^4` mod 3, and
the five coefficients are

```text
y^4: c5_1+2d5_0;  xy^3: 2c5_2+d5_1;  x^2y^2: 3c5_3+3d5_2+6h^2 ≡ 0;
x^3y: c5_4+2d5_3+2h;  x^4: 2+2c5_5+d5_4,
```

exactly (8), with the `x^2y^2` row identically zero modulo three because
its integer coefficient is `3(c5_3+d5_2+2h^2)` — the universal first-carry
Cartier class vanishes source-honestly, and its formal quotient is exactly
the successor's row.  Four nonzero rows enter the system.

**Table (9), verified.** `audit_lower_divergence.py` builds the true
divergence matrices (`c`-column `i` hits target row `i-1` with coefficient
`i`; `d`-column `i` hits row `i` with coefficient `d+1-i`) and checks the
brute rank against `dim - #Cartier`.  I verified by hand that the ranks and
cokernels for target degrees `0..4` are `(1,0),(2,0),(3,0),(4,0),(4,1)`
with unique low cokernel `x^2y^2`.  Digits of degree at most four have
derivative degree at most three; crossed with the degree-`<=3` mod-3
first-digit derivatives they reach mixed-carry degree at most six, so they
cannot alter the D7 rows, and their accepted rows (degrees 0–3) are
divergence-surjective, hence completable after (1).  Correct.

**Spectators.** The six derivative-zero degree-six directions are exactly
`c6_0,c6_3,c6_6,d6_0,d6_3,d6_6` (cube monomials); they occur in no accepted
row, no pivot expression, and no D7 row, and are rightly excluded from the
17 visible unknowns.  The reports and README repeatedly state that (3) is
not a count of distinct maps.  Honest.

## 4. Charge 3 — the `19 x 17` affine rank formula and counts

Rows: 7 reviewed D9/D8 core rows (labels
`M_0_9,M_3_6,M_6_3,M_9_0,M_0_8,M_3_5,M_6_2`) + 4 accepted-degree-4 rows + 8
full D7 rows = 19.  Unknowns: `d7_1,d7_4,d7_7,d6_1,d6_4` + twelve `c5,d5`
= 17.  The compiler asserts (frozen PASS, code inspected line by line):
every equation's monomials lie in unknowns∪structural∪Frobenius; matrix
entries are structural-only; the affine remainder contains no digit monomial
(exact affine-linearity) and is affine in the six Frobenius names (at most
one per monomial).

**Formula.** For fixed structural base, solvability in the digits for a
given Frobenius value `phi` is `F·phi+b0 ∈ Im(A)`.  The projected Frobenius
map into `coker(A)` has rank `c-r`, so the compatible `phi` form an affine
subspace, nonempty iff `rank[A F]=rank[A F b0]` (`c=d`), of cardinality
`3^(6+r-c)`; each compatible `phi` carries `3^(17-r)` visible digit
solutions, so the per-base visible total is `3^(6+r-c)·3^(17-r)=3^(23-c)`.
Both exponents in the report are correct; `3^6=729` is the literal
per-base Frobenius sweep.

**Enumeration logic.** The literal path row-reduces `[A|F|b0]` with pivots
restricted to the 17 digit columns (`for col in range(len(unknowns))`),
asserts `prow==r`, and tests each of the 729 `phi` against the cokernel rows
`work[r:]` — a correct and independent decision procedure — then asserts
per-base equality with the formula (`assert literal_here==fcount`).

**Arithmetic of (2)/(3).** `172+100+1539+376=2187=3^7`;
`3·100+9·1539+27·376=300+13851+10152=24303` compatible states out of
`3^13=1594323`; `3253689=Sigma 3^(23-c)` over compatible bases, i.e. the
total of (state, visible-digit-solution) pairs over the 24,303 states —
average `3^(17-r)≈134`, i.e. mean rank `≈12.5`, sensible for 19 rows.  The
stream hash (11) equals the FREEZE value.  All internally consistent.

## 5. Charge 4 — the successor row over the integers

By direct integer expansion (all coefficients exact):

- `[x^2y^2]L=0` and `[x^2y^2]L/3=0` (no such monomial in `L1`);
- `[x^2y^2]K=[x^2y^2]K0=8h^2-2h^2=6h^2` (from `A0_2·V0y_2-U0y_2·V0x_2`;
  `K_single` starts at degree seven, `K_double` at ten);
- `[x^2y^2](C_x+D_y)=3c5_3+3d5_2` (degree-2/3/4/6/7 digits cannot reach it:
  `C4_x` has degree three, `C3_x` degree two, `C6_x` degree five);
- hence `[x^2y^2]E=6h^2+3c5_3+3d5_2`, formally divisible by three with no
  equation cleared and no representative chosen, and
  `[x^2y^2]E1=c5_3+d5_2+2h^2` — identity (1)/(5), verified;
- `[x^2y^2]M` over `Z` equals
  `3h d3_1+6h c3_2-3c3_1-3d3_0+6(q d2_0+s c2_2-2r d2_2-t c2_0) ≡ 0 mod 3`
  (hand expansion of all four products against the `C2,C3` layer; degrees
  0/1/4/5/6/7 digits contribute nothing at `(2,2)`) — `[x^2y^2]M=0`,
  verified.

**Decoupling.** The accepted degree-1 and degree-2 rows are, by hand,
exactly (6): `c2_1+2d2_0`, `2c2_2+d2_1`; `c3_1`, `2c3_2+2d3_1+2h`, `d3_2`
(the `2h` from `[L1]_2=2h xy`).  Each has a unit digit pivot, is solvable
for every structural value, and shares no variable with (1).  Accepted
degrees zero and three are divergence-surjective by (9); degree four was
closed in the parent with its `x^2y^2` row identically zero.  Adjoining
`C2,C3` alters no parent row (their mixed-carry reach is degree `<=5`).

**Uniqueness of the cokernel class.** Cartier monomials `x^a y^b` need
`a≡b≡2 mod 3`, forcing `a+b≡1 mod 3`; through total degree six the only one
is `(2,2)`.  Divergence-surjectivity onto target degrees 5 and 6 (needed to
absorb everything else) is witnessed by frozen unit-pivot asserts in the
consumed generators: the six `sub6` pivots (`c6_1,c6_2,d6_2,c6_4,c6_5,d6_5`)
cover all six degree-5 monomials, and the seven degree-10-gate pivots
(`c7_1,c7_2,d7_2,c7_4,c7_5,d7_5,c7_7`) cover all seven degree-6 monomials.
So (1) is the complete lower Cartier condition, not a chosen slice.

## 6. Charge 5 — sufficiency for one next digit

Given a compatible state of the `20 x 17` gate: degrees ten (identically
zero on the vertical branch), nine and eight (core rows), and seven (the
eight D7 rows) of the order-27 residual vanish; every accepted row of
degree `<=6` is solved; the carries of solved rows land on their own
monomials, all of degree `<=6` and all non-Cartier except `x^2y^2`, whose
carry is the formal, representative-independent (1) and vanishes.  The
residual mod 3 therefore has total degree at most six and zero `x^2y^2`
coefficient, so by Section 5 there is a pair `W,Z` with `deg<=7` (cap
seven, divergence degree `<=6`) and `F+W_x+Z_y≡0 mod 3`.

**Exact order bookkeeping, no missing cross terms.** Adding `27W,27Z` to
the coordinates changes `det J` by
`27[W_x Q_y+P_x Z_y-W_y Q_x-P_y Z_x]+729[W_xZ_y-W_yZ_x]`; since
`P_x≡Q_y≡1` and `P_y≡Q_x≡0 mod 3` (seed Jacobian is the identity modulo
three — literally true on `P=x-x^3+3U+9C`, `Q=y+3V+9D`), the order-27
coefficient changes by exactly `W_x+Z_y` mod 3.  All candidate missing
terms sit strictly higher: `W,Z` crosses with `3U,3V` at order 81, digit
crosses `C_xD_y-C_yD_x` at order 81, the seed twist `-3x^2·27Z_y` at order
81.  No off-by-one: the gate solves the coefficient of `27` in `det J-1`,
i.e. Keller modulo 81, exactly one finite next digit.  No degree overflow:
`W,Z` respect the cap `D=7` and their divergence caps at six, matching the
degree-`<=6` residual.  The earlier gates are unperturbed because the added
terms are `≡0` at orders 3, 9, and 27-at-degrees-`>=7`.  Claim (7) and the
FREEZE sentence "every compatible point admits a cap-seven next digit" are
correct.  `W,Z` choices are correctly excluded from (3).

## 7. Charge 6 — the `20 x 17` compiler, counts, hashes, and scope

**Compiler.** `compile_next_cartier.py` appends the independently derived
`F22=c5_3+d5_2+2h^2` (post-`coord`, trivially: no `p,q,r,t` occur) to the
parent's 19 equations, whose structural asserts re-run at replay time via
`runpy` of the parent compiler; the appended row is manifestly digit-linear
and Frobenius-free.  Rank formula and literal cokernel enumeration are the
parent's, re-instantiated; per-base equality asserted.

**Counts.** `208+180+1435+364=2187`; `3·180+9·1435+27·364=23283`;
`1085103=27·40189` visible.  A sharper internal check the two frozen
histograms must jointly satisfy, and do: appending one row moves each base
at most one fibre notch down (`r'∈{r,r+1}` forces `c'∈{c,c+1}` with
`c'-r'>=c-r`), and the migration balances exactly —
`12` bases leave fibre 27 (`376->364`), `116` leave fibre 9
(`1539-116+12=1435`), `36` leave fibre 3 (`100-36+116=180`), and those 36
all empty (`172+36=208`), with no fibre-1 entry, consistent with dependent
rows on the surviving bases.  Mean visible rank rises by about one
(`≈12.5 -> ≈13.5`), as one added row should give.

**Hash web.** Every hash quoted in more than one frozen byte agrees:
report (6)=`FREEZE full_D7_rows` (`b4a52256…`); report (11)=`FREEZE
compatible_literal_states` (`2a4857f1…`); successor report (8)=`FREEZE`
(`71ed86c8…`); `EXPECTED_OUTPUT_SHA256.txt` equals the FREEZE output hashes
in both cases (`619a6cd9…/59eef6ea…/e6d39a00…` and `1020cb61…/e005fdf9…`);
the consumed-artifact hashes in the parent report §4 equal the parent
FREEZE and equal the upstream reviews' self-declared hashes
(`156053c5…`, `772d3627…`, `6ab373bf…`); the successor pins the parent
report at the charged `907dcc72…`.  Zero discrepancies.  The two freeze
self-hashes (`c0299b46…`, `e7742fbf…`) appear only in the charged prompt,
as expected.

**Scope separation.** Both reports and both FREEZE files state: one finite
next-digit lift only (successor), no following divided carry (parent), no
recurrence, no all-depth lift/no-lift, no characteristic-zero
algebraization, no counterexample, no JC2; visible counts omit spectators,
divergence kernels, and (successor) the new next-digit kernel; the
13-component slice theorem is retained as a slice and none of its
components is promoted.  No smuggled claim found in any frozen byte.

## 8. Items resting on frozen attestations (execution gaps)

Unverifiable in this shell-less session; every item is pinned by at least
one frozen assert or attested hash, and none contradicts any hand result:

1. All SHA-256 values (charged report/manifest/freeze hashes, expected
   output hashes, internal row/stream hashes).
2. The replay PASS lines and the frozen asserts' actual execution
   (`slice_rows==sl["actual"]`, `changed==[0,1,3,4,6,7]`,
   `accepted_rows`/`d7_rows` two-path equality, `assert accepted_all[2]=={}`,
   `divide_expr_mod3` divisibility, `literal_here==fcount` per base,
   `prow==r`, the linearity/affineness asserts).
3. The exhaustive `2187`-base enumerations, rank-triple histograms, and the
   two literal-state streams (their totals, fibre histograms, and migration
   arithmetic are verified above; the per-base data are not re-run).

Staged closure on any shell session:

```sh
cd /Users/dc/code/math/jc2
shasum -a 256 xmodel/as-fonly-d7-vertical-full-c5-d7-gate-20260824.md \
  xmodel/as-fonly-d7-vertical-next-cartier-20260824.md
( cd cases/as_fonly_d7_vertical_full_c5_d7_gate_20260824 && ./replay_all.sh )
( cd cases/as_fonly_d7_vertical_next_cartier_20260824 && ./replay_all.sh )
shasum -a 256 -c cases/as_fonly_d7_vertical_full_c5_d7_gate_20260824/MANIFEST.sha256
shasum -a 256 -c cases/as_fonly_d7_vertical_next_cartier_20260824/MANIFEST.sha256
```

## 9. Non-blocking remarks

1. The parent's "7 reviewed D8 rows" are the D9/D8 core (four rows have
   total degree nine).  The shorthand matches the upstream "D8 state"
   naming; not an error.
2. `compile_next_cartier.py` does not re-assert digit-linearity,
   Frobenius-affineness, or the allowed-monomial check for the appended
   row (the parent's asserts re-run for its 19 via `runpy`; `F22` is
   verified linear here by hand).  A successor package should pin it.
3. The successor's (6) presents the degree-1/2 rows as rows that "could
   interact with (5)"; in fact `[x^2y^2]M≡0` closes the only channel, as
   the report itself then proves.  Phrasing only.
4. The sufficiency sentence "because the seed Jacobian is the identity
   modulo three" is correct but compressed; citing the licensed order-27
   identity and the order-81 location of all cross terms would make it
   self-contained.
5. The degree-5/6 divergence-surjectivity used in Section 5 lives in frozen
   asserts of consumed generators (`sub6`, degree-10 `sub`) rather than in
   either report's text.  True and frozen; worth one sentence in a
   successor.
6. `psubstitute` in `audit_full_c5_source.py` is dead code.
7. `homogeneous` differs between namespaces (license: poly; generator:
   poly+names).  Both uses are locally correct; no confusion occurs in the
   frozen code paths.

None of these changes a verdict.

## 10. Promotable sentences

**Parent (accept exactly this, no more):**
`ON THE CHARGED VERTICAL p=3,D=7 F-ONLY BRANCH, ADJOINING ALL TWELVE
HOMOGENEOUS DEGREE-FIVE CURRENT-DIGIT COEFFICIENTS TO THE REVIEWED D9/D8
CORE AND THE LICENSED D7 SOURCE YIELDS AN EXACT 19 BY 17 AFFINE GATE: SEVEN
CORE ROWS, THE FOUR NONZERO ACCEPTED-DEGREE-FOUR ROWS (WHOSE x^2y^2
COEFFICIENT IS IDENTICALLY ZERO OVER THE INTEGERS, BEING
3(c5_3+d5_2+2h^2)), AND EIGHT FULL D7 ROWS OBTAINED FROM THE INTEGER SOURCE
[E1+M]_7 WITH REDUCTION ONLY AFTER CONSTRUCTION; EXACTLY ROWS
0,1,3,4,6,7 DIFFER FROM THE ZERO-C5,D5 SLICE AND THE TWO CARTIER ROWS
fc=0, fd=0 ARE INVARIANT.  CURRENT DIGITS OF DEGREE AT MOST FOUR CANNOT
REACH DEGREE SEVEN AND THEIR ACCEPTED ROWS ARE DIVERGENCE-SURJECTIVE, SO
THEY COMPLETE AFTER THE GATE.  OVER ALL 2187 STRUCTURAL BASES THE EXACT
RANK FORMULA (COMPATIBLE FROBENIUS FIBRE 3^(6+r-c) WHEN c=d, ELSE EMPTY;
VISIBLE DIGITS 3^(23-c)) AND AN INDEPENDENT LITERAL ENUMERATION OF ALL 729
FROBENIUS VALUES AGREE BASE BY BASE: FIBRE HISTOGRAM 0^172,3^100,9^1539,
27^376, 24303/1594323 COMPATIBLE STRUCTURAL-PLUS-FROBENIUS STATES, AND
3253689 VISIBLE CURRENT-DIGIT SOLUTIONS, WHERE THE VISIBLE COUNT EXCLUDES
SIX DERIVATIVE-ZERO DEGREE-SIX SPECTATORS AND LOWER DIVERGENCE KERNELS AND
IS NOT A COUNT OF MAPS.  THIS IS THE FULL VERTICAL D7 COMPATIBILITY GATE
THROUGH THE D7 BOUNDARY ONLY; IT SUPPLIES NO FOLLOWING DIVIDED CARRY, NO
RECURRENCE, NO ALL-DEPTH LIFT OR NO-LIFT, NO CHARACTERISTIC-ZERO STATEMENT,
NO COUNTEREXAMPLE, AND NO JC2 CONCLUSION.`

**Successor (accept exactly this, no more):**
`AFTER THE FULL-C5 D7 GATE, THE FIRST FOLLOWING DIVIDED CARRY ON THE
CHARGED VERTICAL BRANCH HAS EXACTLY ONE BOUNDED DE RHAM OBSTRUCTION: THE
FORMALLY DIVIDED, REPRESENTATIVE-INDEPENDENT ROW
[x^2y^2]E1 = c5_3+d5_2+2h^2 = 0, WITH [x^2y^2]M = 0 OVER THE INTEGERS,
ALL OTHER ACCEPTED LOWER ROWS UNIT-SOLVABLE AND VARIABLE-DISJOINT FROM IT,
AND x^2y^2 THE UNIQUE DIVERGENCE-COKERNEL MONOMIAL THROUGH TOTAL DEGREE
SIX.  APPENDING IT GIVES AN EXACT 20 BY 17 AFFINE GATE WITH FIBRE HISTOGRAM
0^208,3^180,9^1435,27^364, 23283/1594323 COMPATIBLE STATES, AND 1085103
VISIBLE CURRENT-DIGIT SOLUTIONS BY THE SAME DOUBLY-CHECKED CENSUS.  FOR
EVERY COMPATIBLE STATE THERE EXISTS A CAP-SEVEN PAIR W,Z WITH
F+W_x+Z_y=0 MOD 3, AND ADDING 27W,27Z CHANGES THE ORDER-27 JACOBIAN
COEFFICIENT BY EXACTLY W_x+Z_y BECAUSE THE SEED JACOBIAN MATRIX IS THE
IDENTITY MODULO THREE; HENCE EACH COMPATIBLE STATE ADMITS EXACTLY ONE MORE
FINITE 3-ADIC DIGIT (KELLER MODULO 81).  THIS IS ONE FINITE NEXT-DIGIT
LIFT ONLY: NO SUBSEQUENT DIVIDED CARRY, NO RECURRENCE, NO ALL-DEPTH LIFT OR
NO-LIFT, NO CHARACTERISTIC-ZERO ALGEBRAIZATION, NO COUNTEREXAMPLE, AND NO
JC2 CONCLUSION.  VISIBLE COUNTS OMIT ALL SPECTATOR AND KERNEL CHOICES.`

**Do not promote either target to:** a reviewed following (order-81)
carry; a recurrent bounded state; all-depth lifting or non-lifting;
emptiness or nonemptiness of the F-only `D=7` stratum; a characteristic-zero
or algebraic-closure statement; a counterexample to JC; any JC2 inference;
a count of distinct maps; or a byte-verified hash chain until the staged
commands in Section 8 have been run on a shell-enabled session.

## Verdict

CONFIRMED
