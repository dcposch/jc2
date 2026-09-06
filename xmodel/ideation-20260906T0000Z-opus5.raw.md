# Ideation 2026-09-06T00:00Z — opus5 (blind sealed submission)

**Thesis. The characteristic-degree instrument is not one more row-block to bolt onto the
two-point chart: it changes which pair the chart is about.**

```text
VERDICT
 Q1  CHART REDUCTION = ELIMINATE F.  PROVED-HERE (identity, verified symbolically):
       if Q = Phi(F,G), Phi = v^3 - u^2 + a v^2 + b u v + c u + d v + e0 (Moh Prop 3.1 family),
       and J(F,G) = 1, then    F = (bG + c - J(Q,G))/2                          (E1)
       and the Keller row is EQUIVALENT to   J(J(Q,G), G) = -2                  (E2)
       Verbatim whenever m_1 := m/gcd(n,m) = 2, i.e. on 44/66 rows; for m_1 >= 3 the
       elimination is (m_1-1)-valued (algebraic) - stated, not used.  Q-block raw coefficient
       count is a median 0.369 of the F-block; 36/66 rows get D_2 < m, so the smallest member
       of the necessary pair drops (99,66) -> (55,66).
 Q1' NON-CHART DICHOTOMY (NPR, one-line Newton-polygon proof, no genus, no properness):
       for EVERY divisorial valuation nu at infinity of A^2,
         nu(F) >= 0 and nu(G) >= 0,   OR   (nu(F), nu(G)) is a negative multiple of (n_1, m_1),
         OR   nu(Q) = min(m_1 nu(F), n_1 nu(G)) < 0.
       Cor: {Phi = -s} has ONE place at infinity, semigroup <n_1,m_1>, genus
       (n_1-1)(m_1-1)/2 >= 1 on 66/66 rows.  Cheap; refutable in minutes.
 Q1'' COST FIX: the augmented chart is weighted-homogeneous with lambda at weight L - D_2 =
       143 / 153.  BEFORE another compute-bound run, compute the TOP WEIGHT of the graded
       quotient; if it is < 143 no unit exists at any truncation and all three compute-bound
       clients are vacuous (socle-vacuity, cf. K16 t<=8).
 Q2  NOT DESCENT-INVARIANT: Moh p.169 Prop 4.5's hypothesis M_r = n - 2.
       ROSTER: parent M_s = n-2 on 66/66; child M'_{s'} = n'-2 on 3/66, = n'-2-ell on 48/66
       (the roster's delta'_{s'} = -1 in disguise), neither on 15/66.  So the attainment block
       is available at EVERY parent and at almost no child.
 Q3  Weak.  The contact divisor of L on the residual cubic C has total degree 3N
       (D = Norm_{C/A^1}(L - Y)); j_0 is its part at x=0, and Disc_Y(C)(0) != 0 forces
       j_0 = ord_0(L - Ltilde_{i0}) for ONE root.  Prove j_0 >= 3 by a ramification ledger at
       infinity (Thm 3.1's three branches), not by involution/Abel/residues.  No theorem here.
 TOP-3 for 12 h: (1) socle/weight gate on the augmented chart; (2) the (Q,G) chart on R002/R003;
       (3) NPR + Prop-4.5-licence screen census-wide.  Lane specs in Sec. 5.
```

No new exit-price assertion is made, so no `charge_basis=` line is licensed.
## 0. Custody and blindness

The manifest was built mechanically from `xmodel/ideation-20260906T0000Z-opus5.run.v2` by pairing
its numbered `charged_input_<i>_sha256=` and `_basename=` fields with `awk -F=` and prefixing
`lane_inputs_dir`; `sha256sum -c` returned **OK for all 12**, exit 0, before any input was opened.
No digest was retyped. `xmodel/ideation-20260906T0000Z-fable5.md` exists at the wake and is a
same-round submission: it was **not** read — listed by `ls`, never opened; no other `ideation-*`
file was consumed. No ledger edit, no `jc2-lean`. Root had 2.9 GB free; the only writes are this
report and `box/ideation-20260906T0000Z/opus5/char-degree-census.tsv` (7.3 KB). Everything
numerical below is my own computation from `roster.jsonl` plus Moh's printed p.150 definitions as
transcribed in the charged char-degree report; (E1)/(E2) were verified with `sympy`.

## 1. What I established in this lane (roster-wide, exact)

Computed for all 66 rows from `source.{n,m,M}` by Moh p.150 (`d_1=n`, `d_{i+1}=gcd(n,M_1..M_i)`,
`q_1=M_1`, `q_i=M_i-M_{i-1}`, `Lambda_i=sum_{j<=i} q_j d_j`, `D_i=-Lambda_i/d_i`):

| fact | result |
|---|---|
| `M_s = n - 2` (Prop 4.5 hypothesis, p.169) | **66/66** |
| `D_i` integral for every `i` | 66/66 |
| `d_s | D_i` for every `i < s` | **66/66** |
| target-curve genus `g_Gamma = (n_1-1)(m_1-1)/2 >= 1` | **66/66** (40 rows at `g_Gamma = 1`) |
| `m_1 = m/gcd(n,m) = 2` (clean F-elimination) | **44/66** |
| `D_2 < m` | 36/66 |
| `(n_1, m_1)` parent = child | **66/66** (so the Newton datum IS descent-invariant) |
| child `M'_{s'} = n' - 2` | **3/66**; `= n'-2-ell` 48/66; other 15/66 |

**The char-degree instrument is uniformly licensed on the whole residual.** Theorem A and the
total-degree block were established for two clients; `M_s = n-2` and `d_s | D_i (i<s)` on 66/66
say the *licence* is present on every one of the 65. With `F`'s top form `L_1^A L_2^B` (`A+B=n`,
`gcd(A,B) = n/d_s`), the common-form conclusion forces `T_i^psi` top
`= lambda_i L_1^{A D_i/n} L_2^{B D_i/n}`, integral exactly because `d_s | D_i`; so the
whole-target subtraction is available verbatim on all 65. **A licence check, not a kill: 0 rows
die from it, and `d_s | D_i` is a divisibility that could have failed and does not.**

Per-row table: `box/ideation-20260906T0000Z/opus5/char-degree-census.tsv`.

## 2. Q1 — a non-truncation instrument for split branches

### 2.1 PROPOSAL CQ-ELIM: eliminate `F`; the Keller row becomes one second-order identity

**Statement.** `(F,G)` Keller, `deg F = n`, `deg G = m`, `g = gcd(n,m)`, `n_1 = n/g`, `m_1 = m/g`.
Moh Prop 3.1 (p.157: expansion, weight inequality, unique equality term) gives the necessary
target family; its equality-weight monomial has weight `n_1 m = lcm(n,m) = n m_1`, i.e. it is
`F^{m_1}`. With `T_1^psi = G + const` absorbed,

```text
   Q := T_2^psi = Phi(F,G),    Phi(u,v) = v^{n_1} - u^{m_1} + (monomials u^i v^j, n i + m j < n_1 m, j < n_1).
```

**Theorem CQ-ELIM (PROVED-HERE, one line).** `J(Q,G) = Phi_u(F,G) * J(F,G) = Phi_u(F,G)`, since
`J(G,G)=0`. When `m_1 = 2`, `Phi_u = -2u + b v + c` is **linear in `u`**, so

```text
   (E1)   F = ( b G + c - J(Q,G) ) / 2 ,
   (E2)   J(F,G) = 1   <==>   J( J(Q,G), G ) = -2 .
```

Verified on `(x+y^2,y)`, `(x+(y+x^2)^3, y+x^2)`, `(x+7y^5,y)`: both identities hold for symbolic
`a,b,c,d,e0`.

**Why this is a reduction and not a re-labelling.** The complaint against the augmented chart is
that Theorem A's rows sit at depth 143/153 and *add* unknowns. (E1) says the opposite: on the 44
rows with `m_1 = 2` the `F`-block is not an unknown block at all — it is a first-order
differential expression in the `Q`- and `G`-blocks. The chart becomes

```text
   unknowns: G (deg m, top W^{m/d_s}), Q (deg D_2, top lambda W^{D_2/d_s}, lambda != 0), the
             scalars a,b,c,d,e0, and the source-branch coordinates;
   rows:  (E2) J(J(Q,G),G) + 2 = 0                 [the whole Keller condition]
          (A)  deg Q = D_2 with unit leader        [Theorem A, printed p.152 Prop 2.2]
          (T)  Q_{D_2} = lambda W^{D_2/d_s}        [Prop 4.5 p.169, licensed 66/66 by Sec. 1]
          (S)  the source D2/D1 faces, unchanged.
```

`F` never appears. **Prices.** `C(D_2+2,2)/C(n+2,2)`: median **0.369**, `0.316` at (99,66),
`0.320` at R009, `0.369` at R002/R003; 36/66 rows get `D_2 < m`. A ~2x cut, **not** 70x — I do not
claim it crosses the Gröbner wall alone. What it buys is that (E2) is a *single* scalar identity
replacing the whole Jacobian band system, in the pair of smallest degrees.

**Refutation check (~10 min).** Replay (E1)/(E2) on Moh's p.207 children and a tame pair; then
check that `{(E2),(A),(T),(S)}` *excludes* the cone-vertex family `Delta` — attainment excludes it
because `deg h2 = d_2 ∤ D_2` (`33 ∤ 55`; `36 ∤ 63`). If a `Delta` point survives, the reduction has
lost a row and is wrong.

**Scope.** For `m_1 >= 3` (22 rows: `m_1 = 3` 14, `4` 5, `5` 2, `7` 1) `Phi_u = -m_1 u^{m_1-1}+...`
and (E1) determines `F` only up to an `(m_1-1)`-th root; the reduction as stated does not apply.
Both Xu-margin-0 rows, R009 `(192,128)` and R050 `(196,56)`, have `m_1 = 2` and ARE in scope.

### 2.2 PROPOSAL NPR: Newton-polygon rigidity at infinity (chart-free)

**Statement.** For any divisorial valuation `nu` of `k(x,y)` centred at infinity, exactly one of:

```text
 (a)  nu(F) >= 0 and nu(G) >= 0            [both bounded: a deficiency / finite-pole direction]
 (b)  (nu(F), nu(G)) = -t (n_1, m_1),  t > 0   [the n:m ray]
 (c)  nu(Q) = min( m_1 nu(F), n_1 nu(G) ) < 0  [Q blows up along nu]
```

**Proof.** `nu(Phi(F,G)) >= min_{monomials} (i nu(F) + j nu(G))`, with equality unless the
minimum is attained at two or more Newton vertices. `Phi`'s Newton polygon in the weights `(n,m)`
has exactly one compact upper edge, `(m_1,0)`–`(0,n_1)`, every other monomial strictly below. So
if `nu(F) < 0` or `nu(G) < 0` and the minimum is attained twice, the attaining monomials are the
two endpoints, giving `m_1 nu(F) = n_1 nu(G)`; otherwise it is attained once, no cancellation,
case (c). ∎

**Corollary NPR-1 (the target curve).** `Gamma_s := {Phi = -s}` has principal part
`v^{n_1} - u^{m_1}`, `gcd(n_1,m_1)=1`, hence **exactly one place at infinity**, `v_P(u)=n_1`,
`v_P(v)=m_1`, semigroup `<n_1,m_1>`, genus `(n_1-1)(m_1-1)/2`; one place forces irreducibility. On
the roster the genus is `1` on 40 rows, `3` on 11, `4` on 4, `6`/`9` on 3, `2`/`12` on 2, `27` on
1 — **>= 1 everywhere**. At `(n_1,m_1)=(3,2)` (40 rows, incl. (99,66) and D=108) `Gamma_s` is a
**punctured elliptic curve in Weierstrass position**.

**Corollary NPR-2 (an identity, not a floor).** On `{F = alpha}`, `nu(F) = 0` and `nu(G) < 0` at
each place at infinity, so the Newton minimum is attained *only* at `v^{n_1}`: `v_P(Q) = n_1 v_P(G)`
exactly, no cancellation, and `sum_P v_P(Q) = n_1 d` with `d = deg(F,G)`.

**What it is worth, honestly.** NPR-2 is an identity in the tree data; I expect a consistency
check like the RH fibre identity, not a kill. The *operative* content is the dichotomy: at every
branch at infinity, either `F` and `G` are simultaneously bounded — the campaign's
`EMPTY_PROP6.3_FINITE_POLE` typing — or the pole-order vector lies on the `n:m` ray. That is a
per-leaf constraint on family C's 38 typed `ES_NECESSARY_LEAF` orders: it forbids any leaf whose
`(ord F, ord G)` is off the ray while either order is negative.

**Cost.** Arithmetic only: per leaf, read `(ord_gamma F, ord_gamma G)` off its typed order and
test the alternative. Minutes on one core. **Refutation.** Run Moh's five p.207 rows and (99,66)
case (A)/(B) first: a *known admissible* leaf off the ray with a negative order means the test is
mis-stated (most likely a `gamma`/`pi` order confusion) and must be withdrawn.

### 2.3 PROPOSAL SOCLE-GATE: decide whether the augmented chart CAN produce a unit

The augmented chart is weighted-homogeneous under the residual dilation
`F_alpha = alpha^{-n}F(alpha x, alpha y)`, `G_alpha = alpha^{-m}G(alpha x, alpha y)`; Astra
records the leader's weight as `L - D_2 = 143` at (99,66) and `153` at D=108, and the only
inhomogeneous generator is `Z*lambda - 1`. The campaign's own rule for such charts: run graded,
and a membership above the top weight of the graded quotient is weight-forced, hence vacuous.

**Instrument.** In the graded chart `I_gr` (all rows but the two localizers), compute `dim`,
`vdim`, and the **maximal weight of `kbase`**:

```text
   top weight of k[chart]/I_gr  <  143 (resp. 153)   ==>  lambda^N notin I_gr for every N >= 1
                                                     ==>  no unit at any truncation; the three
                                                          compute-bound clients are VACUOUS.
   top weight >= 143                                 ==>  the decision is real; spend the CPU.
```

**Cost.** One `std` with `degBound` on the graded chart, or just its weighted Hilbert series —
the cheap half of what times out, since the inhomogeneous localizers are dropped. Minutes to an
hour per client, against 36 attempts that all returned `T1`/`M14`.
**Refutation.** Positive control: the same graded object for a toy `k=2` chart with a known unit
must have top weight exceeding the toy leader's weight. After 36 attempts at `600-900 s` and `>= 15 GiB` the campaign
still does not know whether the augmented decision is *decidable in principle at this weight*.

## 3. Q2 — a uniform necessary condition that is NOT descent-invariant

The fixed-point theorem is about *arithmetic* conditions, and its mechanism is the p.171 Remark:
every printed condition survives verbatim with `J = x^l` under the shifted (3)*. So a non-invariant
condition must have an **`l`-sensitive printed hypothesis**. Exactly one is in play, and it is not
an inequality on radii:

**Moh p.169 Proposition 4.5 requires `M_r = n - 2`.**

I checked it on the roster:

```text
  parent  M_s = n - 2                    66 / 66     (the licence for the common highest form)
  child   M'_{s'} = n' - 2                3 / 66
  child   M'_{s'} = n' - 2 - ell         48 / 66     (= the roster's delta'_{s'} = -1)
  child   neither                        15 / 66
```

The child's Prop-6.3 Jacobian is `J = c gamma^{v_s-u_s-1}`, so the `l`-shifted `delta = -1` reads
`M' = n'-2-ell`, which is the 48. But **Prop 4.5's printed hypothesis is `M_r = n-2` with no
`ell`**, and its `ell`-shifted form (unlike Props 4.2/4.4) is *not printed* —
`OPEN[MOH-ELL-REMARKS-INCOMPLETE]` already records that the Remarks license 4.2/4.4 and that
condition (3) must also shift, unprinted. Therefore:

* the common-highest-form conclusion, hence the whole-target subtraction, hence Theorem A's
  total-degree block, is licensed at **every parent** and at **no child** without an unproved
  `ell`-shift of Prop 4.5;
* it is consequently a **uniform necessary condition on the 65 that is not a fixed point of the
  descent**, which is precisely what Q2 asks for; and
* it explains structurally why the second arithmetic generation returned 0 kills: the descent
  discards the very hypothesis that makes the characteristic block available.

**Instrument and cost.** (i) *Free part, done here:* the licence check, 66/66, minutes.
(ii) *Operative part:* emit, per row, `F`'s top split `(A,B)` and the forced targets
`lambda_i L_1^{A D_i/n} L_2^{B D_i/n}` for every `i < s`, and adjoin them to that row's receiver
chart. On the 22 rows with `s = 4` that is **three** whole-target subtractions, not one — R066 at
degrees 108, 90, 243; R059 at 128, 96, 176, 348. The emission is arithmetic; the decision is the
same Gröbner problem, which is why §2.3 comes first.

**Refutation check.** If some row has `gcd(A,B) != n/d_s` the forced target is not integral and
the Sec. 1 licence claim fails for that row. `(A,B)` must be read from the row's D2 face; the two
clients' faces (`(pi^3-1)^{24},(pi^3-1)^{16}`, `(pi^4-1)^{21},(pi^4-1)^{14}`) are `A/B = 27/72`
and `24/84`, both consistent. **I checked the arithmetic (`d_s | D_i`), not the face, on the
other 64.**

**Two candidates declined.** (a) The Newton datum `(n_1,m_1)`, hence `g_Gamma`: **parent = child
on 66/66** — descent-invariant, dead. (b) Xu Thm 5.1 with exact contact at R009/R050:
`xu_margins` already gives margin 0 on exactly these two, and the Xu-screen gate showed the major
leaf expression is a Def 5.1(3) identity, so a sharpening must come from outside the skeleton.
Not a Q2 answer — but both have `m_1 = 2` and are natural first clients of §2.1.

## 4. Q3 — the K16 uniform statement

Fable's Theorem 5.1 is the useful move: `T_2 = 0` iff `6P_0P_4 + 9P_1P_3 + 5P_2^2 = 0` iff
`ord_0 Disc_Y(Q_P) >= 6` iff `j_0 >= 3`, `j_0 = ord_0 D`, `D = d_Y Q_P(x,L)`, `deg D = 3N`. I have
no theorem; I have one route the three dead ones do not cover, and one negative.

**Negative first.** `D = ±Norm_{C/A^1_x}(L-Y)` over the residual cubic `C`, irreducible over
`k(x)` (Thm 3.1), so one might hope the decomposition group at `x=0` acts transitively on the
three roots and forces `j_0 >= 3`. But `Disc_Y(C)(0) != 0`, so `C` is unramified and split at
`x=0`, the decomposition group is trivial, and exactly one root can osculate `L`. **The local
Galois route is empty.**

**Route (RAM-LEDGER).** `L - Y` has poles on `C` only over `x = infinity`, so

```text
   sum_{P : x(P) finite} ord_P(L - Y)  =  deg D  =  3N ,      j_0 = the part over x = 0.
```

Thm 3.1 pins infinity: `L` continues onto one of three branches with leading coefficients
`-1/y`, `±sqrt(omega/ptilde)`, which fixes the pole divisor of `L-Y` at infinity and hence the
*distribution* of the 3N contact zeros. To prove: `div_0(L-Y)` has no multiplicity-2 component at
`x=0`. **Hypotheses required:** (i) the three `∞`-branches distinct, `ord_infinity(L-Y)` computed
not bounded; (ii) `C` smooth over `x=0` (given); (iii) that the K16 normalisation of `x=0` is a
*Weierstrass-type* condition on `C` — the gap, and where uniformity in `t` must come from.
**Cost.** One exact pole-divisor computation at infinity from Thm 3.1's three leading
coefficients, at `t = 3,4,5` against the frozen certificates: hours on one core.

**Refutation.** The `t = 2` family has `j_0 = 3 = N` with `B = eta = 0` for the independent reason
`c = 0`; a ledger that *forces* `j_0 >= 3` must not also force it at `t=2` for the wrong reason.

**Second, cheaper item.** `T_2` sits at weight `4t` and the socle degrees of `J_t` are
`7,14,21,30,39,49,61` at `t = 3..9`, so `4t < socle(t)` throughout: `T_2 in rad J_t` is **never
weight-vacuous** and the socle argument that decided the exact-square question does not apply.
Reported so the next lane does not spend a run rediscovering it.

**What I did not do.** No CAS ran in this lane; every number above is arithmetic on
`roster.jsonl` plus three `sympy` checks. (E1)/(E2) is an identity, not a built chart: no row is
killed, no chart below 70 unknowns is claimed, and I computed no top weight for §2.3.

## 5. Top-3 avenues for the next 12 hours, with lane specs

```text
RANK 1  lane  cd-socle-gate-20260906
        ASK   For each of the three char-degree clients ((99,66) delta2, delta5/2, D=108
              repaired free mean), build the AUGMENTED chart WITHOUT the two localizers, declare
              the dilation grading (x^i y^j coefficient of F/G/Q at weight n-i-j / m-i-j /
              D_2-i-j; a,b,c,d,e0 at 66,33,99,132,198 for (99,66)), and report dim, vdim and max
              weight of kbase against w(lambda) = 143 / 153.
        GATE  top weight < w(lambda) on all three ==> type the augmented decision VACUOUS and
              stop the compute-bound schedule; otherwise report the margin.
        COST  <= 60 min per client on the existing r7i.8xlarge; exact Q, dp, degBound allowed.
        CTRL  toy k=2 chart with a known unit: top weight MUST exceed its leader weight.
        RISK  the grading may fail once the whole-target subtraction is adjoined - check row
              homogeneity FIRST and name any inhomogeneous generator.

RANK 2  lane  cq-elim-chart-20260906
        ASK   Build the (Q,G) chart of Sec. 2.1 for R002/R003 ((75,50), D_2 = 45, m_1 = 2, the
              two smallest receivers at 199 unknowns) and R015 ((99,66)).  Rows:
              J(J(Q,G),G) + 2 = 0 ; deg Q = D_2 with unit leader ; Q_{D_2} = lambda W^{D_2/d_s} ;
              the row's D2/D1 source faces.
        GATE  (i) the chart must EXCLUDE the four-constant Delta family (25 does not divide 45) -
              if a Delta point survives the build lost a row, stop; (ii) then msolve -g 2 for
              [1]: (the Prop 7.1 affine half is msolve, not std).
        COST  emission ~1 h; decision unknown - budget 3 h, three watchdogs, not one.
        CTRL  replay (E1)/(E2) on Moh's p.207 children and a tame pair before emitting.
        RISK  ~2x in coefficient count, NOT 70x; on timeout the lane still delivers the
              reduced necessary system as a reusable object.

RANK 3  lane  npr-licence-screen-20260906
        ASK   (a) NPR (Sec. 2.2) on the 38 typed ES_NECESSARY_LEAF orders of family C: per leaf,
              is (ord F, ord G) on the n_1:m_1 ray, or are both orders >= 0?  (b) Per-row emission
              of the Prop 4.5 forced targets lambda_i L_1^{A D_i/n} L_2^{B D_i/n} for every i < s
              on all 65, with (A,B) read from the row's D2 face - NOT assumed from d_s.
        GATE  (a) must give "no kill" on Moh's five p.207 rows and (99,66) case (A)/(B);
              (b) must give gcd(A,B) = n/d_s on 66/66 or name the exceptions by row_id.
        COST  minutes for (a), ~2 h for (b) (faces recomputed per row).
        RISK  (a) is likely an identity; charge it only if it fires on a leaf the whole-tree
              screen does not already kill.
```

## 6. FALLACY-v2 ledger

*Floor/attainment.* (E1)/(E2) are identities verified symbolically, not bounds; `deg Q = D_2` is
cited as Astra's Theorem A (printed Prop 2.2(1), p.152, `M_i <= e`), never inferred from a support
picture. The Sec. 1 divisibilities are checks that **passed** and are reported as such, not
promoted. NPR-2 is an identity, explicitly not a kill. *Flag/place/series.* NPR is stated for
divisorial valuations at infinity of `A^2`; such a valuation is never identified with a place of
a fibre, and NPR-2 is stated on `{F=alpha}` with its own places. `Gamma_s`'s single place at
infinity is never identified with a source branch. *Pole/interior.* The semigroup `<n_1,m_1>` is
read off the Newton polygon's one compact edge after checking every other monomial of `Phi` lies
strictly below it (Prop 3.1's weight inequality); the vertex class is checked, not assumed.
*Prime label/derivative.* `'` on `M'`, `n'`, `s'` is a generation label; the only
differentiation is `Phi_u`, `d_Y`, `J`, each written with its variables. *Variable/ring map.* `Phi` is declared
with `u <-> F`, `v <-> G`, weights `wt u = n`, `wt v = m`; the identity was verified in
`Q[x,y,a,b,c,d,e0]`, not matched by name. *Merge-free/M-descent.* No `M'_{s'+1}` is invented;
Sec. 3 uses the roster's own `M_prime` and `ell`. *Target/arrival index.* Parent `s` and child
`s'` are kept distinct in Sec. 3; the `n-2` vs `n'-2-ell` comparison names both. *`sat()` / raw
remainder degree.* No Gröbner run here. *Per-ray charge.* No exit claim.

## OPENS RAISED

```text
OPEN[CQ-ELIM-EQUIVALENCE]
  QUANTITY: for a Keller pair with m_1 = m/gcd(n,m) = 2 and Q = Phi(F,G) the Moh Prop 3.1
    target, F = (b*G + c - J(Q,G))/2 and J(F,G) = 1 <=> J(J(Q,G),G) = -2.
  STATUS: PROVED-HERE as a formal identity (J(Q,G) = Phi_u(F,G)*J(F,G), Phi_u linear in u);
    verified symbolically on three Keller pairs with symbolic a,b,c,d,e0.  Applicable to 44/66
    rows; NOT built as a chart, so 0 rows killed.
  CHEAPEST TEST: replay both identities on Moh's p.207 children, ~10 min; one pair with
    J(J(Q,G),G) != -2 refutes it.
  BLAST RADIUS: replaces the F-block of every m_1 = 2 receiver chart by a Q-block of median
    0.369 the coefficient count; 36/66 rows get D_2 < m.

OPEN[PROP45-LICENCE-NOT-DESCENT-INVARIANT]
  QUANTITY: Moh p.169 Prop 4.5's hypothesis M_r = n-2 holds on 66/66 parents and 3/66 children
    (48/66 satisfy only the ell-shifted M'_{s'} = n'-2-ell, 15/66 neither); the ell-shifted form
    of Prop 4.5 is not printed.
  STATUS: computed exactly from roster.jsonl (char-degree-census.tsv); the non-invariance is a
    consequence, not a promoted theorem, and it kills 0 rows by itself.
  CHEAPEST TEST: recount M_s vs n-2 on the 1,420 operative rows, ~3 min; one parent row with
    M_s != n-2 refutes Sec. 1's uniformity claim.
  BLAST RADIUS: licenses the characteristic block on all 65 and answers Q2.

OPEN[NPR-INFINITY-DICHOTOMY]
  QUANTITY: for every divisorial valuation nu at infinity, nu(F) >= 0 and nu(G) >= 0, or
    (nu(F),nu(G)) = -t*(n_1,m_1) with t > 0, or nu(Q) = min(m_1*nu(F), n_1*nu(G)) < 0; and
    {Phi = -s} has exactly 1 place at infinity, semigroup <n_1,m_1>, genus
    (n_1-1)(m_1-1)/2 >= 1 on 66/66 rows.
  STATUS: PROVED-HERE from Phi's Newton polygon (one compact edge, by Prop 3.1's weight
    inequality and unique equality term); genus computed on all 66 rows. Not applied to any leaf.
  CHEAPEST TEST: run the ray/boundedness alternative on the 38 typed ES leaves of family C and
    on Moh's five p.207 rows, ~5 min; a known-admissible leaf off the ray with a negative order
    refutes the application (most likely a gamma/pi order confusion).
  BLAST RADIUS: possibly family C's split-window leaves; 0 elsewhere, NPR-2 being an identity.

OPEN[AUGMENTED-CHART-WEIGHT-VACUITY]
  QUANTITY: the leader lambda has dilation weight L - D_2 = 143 at (99,66) and 153 at D=108; if
    the top kbase weight of the graded augmented chart is < that, no lambda^N lies in the ideal
    and the augmented decision is vacuous at every truncation.
  STATUS: proposal only; no top weight computed in this lane.  Homogeneity of every emitted
    augmented row under the dilation is asserted by Astra's beta=1 section and has NOT been
    verified generator-by-generator.
  CHEAPEST TEST: weighted Hilbert series / kbase with both localizers dropped, <= 60 min per
    client; an inhomogeneous generator refutes the whole gate.
  BLAST RADIUS: decides whether to continue or abandon 36 compute-bound attempts; no count
    changes either way.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone body-end marker line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `24983`.
- Body SHA-256:
  `a7ee66808eb8688a568d9da98ec5840e9bb55fe0c76af21e6ac9852fb5cad89f`.
- Frozen basis: `de78ca950def644a22c1bf5b6c877be8d043d0de`.
- Charged inputs: 12/12 verified `OK` by `sha256sum -c` against a manifest built by `awk` from
  the receipt's paired `charged_input_<i>_basename=` / `_sha256=` lines.
