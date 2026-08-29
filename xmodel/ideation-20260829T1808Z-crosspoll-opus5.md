# Adversarial cross-pollination — Opus 5 — round `20260829T1808Z`

Researcher: Opus 5 (equal standing).
Frozen basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa` (verified `git rev-parse HEAD`).
Lifecycle: `ADVERSARIAL_SYNTHESIS_INPUT / NO_PROMOTION / FAIL_CLOSED`.

This is adversarial synthesis input, not promotion. Nothing here proves or
disproves JC2, asserts an occurrence, an attainment, a `PairRef`, a source
value, a degree ceiling, a type menu, a polynomial Keller map, or a
counterexample. No new exit price is asserted, so no charge-basis declaration
appears anywhere in this report.

## 0. Custody, boundary, and the fence

### 0.1 Every charged hash, recomputed this session

Full-file SHA-256, and body SHA-256 over every byte through the unique
standalone `<!-- BODY-END -->` line including its terminating newline.

```text
f7a0b2a7e6a34cb8b8ae926adf95d36db46b0dc37e6aa75a17be3dcd7ce5fea2
  xmodel/ideation-20260829T1808Z-crosspoll-packet.md
  body 11344 / 0703f1f37b7dd445c4d8b74cb06e7f1f00b996c8af89d87dac6f2263628e1961
f58ee9b50d640860fa36f34f12f39bcbb0f8fb852e2ace90be8e62323e09ccfb
  xmodel/ideation-20260829T1808Z-state.md
  body 9040 / d48e33c594731b4e6f0761c21c28460a15e15a7a9ea80801692b2fdc1a62529b
bfa137c567e366dca26c6d0bc4a8824912cbba03d74df2bee27264000bcfb0cb
  xmodel/ideation-20260829T1808Z-sol56.md
  body 27206 / 190a5e108b767b99cdb0cbf7303bc64d8537bf0f4161324598735f8097308b88
37d1942a2ba6585c6b7d977aa5d20fd994008dbdef250a05c0425b92ac29f6ee
  xmodel/ideation-20260829T1808Z-fable5.md
  body 28151 / 1e530d1f69b8300b297e7c690b96a007b6ad85e58b62536ab017292d7800f1ee
2f65a96ff2ba2fc5d573b90c41aca57cfffb4efbe6c3bbdd2a3ea914079032cc
  xmodel/ideation-20260829T1808Z-opus5.md
  body 47459 / 486b11c0082831f295f0505fee5482d1ab1d955964e793b5a93914eed5ebdc86
190aae86c664627a8668dc219a49d8ffad7f09e4e90bc4559aa531e35288b6d5
  xmodel/ideation-20260829T1808Z-grok46.md
  body 34560 / 9257ea3daecedb627746d1b8da879776c0ccc4480fcfc77f01160a51681cb50a
2ebd1d78391a145c446d2113a1801e342118773c6fd9ce63be183dfd94f15a58
  xmodel/k00-r2-full-rank-fan-provisional-sol56-20260829.md
  body 11680 / c596347cf5e343854b6838f8b7f3241c623de78250676033fc364d07bc23098c
2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4
  xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py
66f119e0e46b56f067802baa9118d0080370dc404878f9db667284c2d45d54a0
  xmodel/u1-ham-kum-conn-stop-audit-sol56-20260829.md
  body 5520 / ad2d79d8e220234a315d63dd8e5b9d264084dbc824a3dc804a2588988e7813a9
59add10d8b291bb85a32c8f8a155d7ff0a7c4d6dd646fc164f48304b34fd80c1
  ops/seal.py
73f7e7bb554d3ba6936eb472539eebce3425eda619e8f118d1cf29f632a6ff49
  ops/test_seal.py
```

Frozen mathematical source consumed for the independent K00 reconstruction:

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/
  run/output/compiled_v2/tails.json
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/
  compile_contracted_source_v20r2.py
```

Also read by explicit path, uncharged (git-tracked at the basis, used for
definitions I was auditing myself against, not as inputs to a new claim):
`AUDIT.md` lines 9330–9400 (`KJN`/`RPMC`/energy-localization definitions),
`ladder/REDUCTION.md` T4 and T7, `ops/lane.sh`, `ops/validate_charge_basis.py`,
`.ignore`. All ten charged hashes matched on first recomputation.

### 0.2 Tool boundary actually observed

No web, no external message, no AWS action, no canonical edit, no commit, no
push, no heavy CAS. No report, prompt, log, or run record created after the
packet was opened. Exactly one file written — this one; scratch was passed on
standard input, never to disk. Every process stayed far below 60 CPU seconds
and 1 GiB; the largest single run was 42 s (a 450-term mutation census).

**Fence.** `jc2-lean` was not read, listed, searched, stat'ed, built, or
touched in any way. I issued **no recursive traversal rooted at the repository
root at all** — not `grep -r`, not `find`, not `ls -R`, and deliberately not
even `rg --files .`, which would have stat'ed the fenced directory entry in
order to skip it. Every search was either a single explicit path or `Grep`
(ripgrep, which consumes the repository `.ignore`).

### 0.3 Process-level correction of the disclosed fence failure

The disclosed failure is a **command shape**, not a tool inventory. The
repository root `.ignore` already contains `jc2-lean/` with the comment that
it is "intentionally stronger than a Git ignore rule; ripgrep and compatible
tools consume `.ignore` directly", so the ripgrep half of the fence is closed
today. Both disclosed traversals were bare recursive POSIX searches **rooted
at the repository root**, a shape no `.ignore` can constrain.

The smallest enforceable default is therefore a rule on the command before it
is issued, not a new binary:

```text
FENCE-DEFAULT/v2 (process rule, zero code, adopted here)
  Never issue a command that recursively traverses from the repository root.
  Search by explicit path, or with rg, which consumes .ignore.
  If a repository-wide sweep is genuinely required, name the subtrees.
```

This is checkable by inspecting the command string, costs nothing, and does
not restrict legitimate explicit-path work — which is the whole of this
session's evidence base. I therefore **withdraw my own blind
`FENCE-DEFAULT/v1`** (`ops/rgrep` + `ops/fence_check.sh` + a prompt line) as a
candidate for this checkpoint's single systems slot. The packet's own
observation is decisive: a wrapper helps only when used, so a wrapper cannot
be the enforcement mechanism, and spending the one bounded slot on it would
displace a change that a lane hook *can* enforce (§7). The wrapper remains
worth adding later as convenience, not as control.

Acceptance for the process rule is longitudinal and needs no artifact:
disclosed fence traversals per round go to zero and stay there. This round:
zero.

## 1. K00 valuation two — independent reconstruction and verdict

### 1.1 Verdict

```text
K00 V20R2 EXACT-VALUATION-TWO EXCLUSION THROUGH GRADE EIGHT:  PASS_WITH_REPAIR
```

All six rank cells are **confirmed exactly**, each displayed identity
reproduced to the last coefficient, by a reconstruction that shares no code
and no organizing choice with the sealed replay. The two repairs are to the
report's *stated reasons and scope*, not to any cell; no cell weakened, none
failed.

### 1.2 What I did, and why it is a reconstruction rather than a rerun

I rebuilt the seven rows directly from the 569 frozen tail terms and the
literal V20R2 affine map, in a deliberately different organization:

- the compiler's monomials are evaluated as **truncated Λ-series whose
  coefficients are sparse multivariate polynomials**, rather than as
  polynomials later sliced by grade;
- the isotropic branches are handled in the **quotient ring `Q[r]/(r²+64)`**,
  where `r` plays the role of `8i`, instead of Gaussian rational pairs. Both
  conjugate branches are then a single computation exchanged by the field
  automorphism `r ↦ −r`, so the conjugate branch is verified structurally, not
  by a second run;
- the `u² = 192v²` branch is handled in `Q[t]/(t²−192)` by the same device,
  which keeps the branch valid over base fields where 192 is not a square (the
  relation, not the root, is what is used);
- a wholly separate **univariate numeric path** (plain `Fraction` Λ-series at
  random rational jets) cross-checks the symbolic path.

Variable/ring map declared: `C0=(1+d0)/256`, `C1=d1`, `C2=(1+d2)/16`,
`C3=d3`, `C4=(3+d4)/8`, `C5=d5`, `C6=1`; tail exponent order
`(C0..C6, k10, k6, k2)` with weights `(8,7,6,5,4,3,2,2,6,10)`;
`d = Λ²x + Λ³y + Λ⁴z + …`; `k10 → Λ²(κ + k10₁Λ + …)`, `k6 → Λ⁶(k6₁Λ + …)`,
`k2 → Λ¹⁰(k2₁Λ + …)`; coefficient field `Q`, extended only as stated. Image
checks: every row is weighted-homogeneous of weight `12+l` (verified, all
seven), grades 0–3 vanish identically, and `Q6 = 0`.

### 1.3 Cell-by-cell result

```text
STRUCTURE  V(Q_1..Q_7) = V(A,B), A = 16x1-4x3+x5, B = x0-4x2+2x4       CONFIRMED
   independently: all seven Q_l lie in the ideal (A,B) (linear solve),
   Q1+8Q3 = (3/2048)AB and Q4 = (3/524288)(B^2-64A^2) hold exactly,
   so AB=0 and B^2=64A^2 force A=B=0.  The leading cone is the 4-plane.
   x=(2b+2u,a,b,8a+v,b-u,16a+4v) is a bijection onto it (inverse displayed).

CELL 1  rowwise factorization DQ_i(x)[q] = alpha_i A(q) + beta_i B(q),
        the seven-row (alpha_i,beta_i) table, and rank fan by Delta=u^2+64v^2
                                                                    CONFIRMED
   Residual zero in all seven rows against the published table.  Rows 1,3,5,7
   are proportional to (u,-v); row 2 is (3/256)(v, u/64); rows 4,6 vanish.
   Hence exactly four nonzero 2x2 minors, all rational multiples of Delta.

CELL 2  leading rank one dies at grade six                          CONFIRMED
   G6_6 = 3/1024 u v^2 - u^3/65536 = u(192v^2-u^2)/65536, independent of
   y, z, and every load.  On Delta=0 with (u,v)!=(0,0): v!=0, u!=0, and
   G6_6 = u v^2/256 != 0.  Field-independent: no passage to Qbar is needed.

CELL 3  leading rank two dies at grade six                          CONFIRMED
   Grade 5 forces A(y)=B(y)=0 (rank 2), so y lies on the cone and Q(y)=0.
   Zero-image rows 4,6 give H6 = u(192v^2-u^2) and
   H4 = u^3-448uv^2+64bv^2-bu^2-1024auv, reproduced exactly.
   u=0 branch: H4 -> 64bv^2 so b=0, then G6_3+(1/8)G6_1 = (1/4)v^2(v+3a)
     and G6_5+(1/128)G6_1 = -(3/64)v^2(v+2a), incompatible for v!=0.
   u^2=192v^2 branch: row 4 gives B0 = -2t(1+4A0) exactly, then
     S5 = v^3/8 and S7 = -v^3/64.  Both contradictions reproduced.

CELL 4  old plane, next rank two, dies at grade eight                CONFIRMED
   Grade 7 is DQ(y)[z] + source; rows 1 and 2 give the 2x2 system with
   determinant Delta_y, so A(z)=2st and B(z)=s^2-64t^2 uniquely.
   Grade 8: G8_1+8G8_3 = -(3/256)D and G8_4 = -(3/32768)F, exact;
   sD-tF = -2uv(s^2+64t^2) and sF+64tD = (u^2-64v^2)(s^2+64t^2), exact;
   and on s^2+64t^2=0, D = t(u -+ rv)^2 with r^2=-64, exact.

CELL 5  old plane, next rank zero, dies at grade eight               CONFIRMED
   Grade 7 vanishes identically for ARBITRARY z when y is on the old plane,
   and every grade-eight row is INDEPENDENT of the old-plane parameters
   (a2,b2) as an exact identity, not by sampling -- verified by symbolic
   absence of those variables.  Then G8_1+8G8_3 = (3/2048)WA*WB and
   G8_4 = (3/524288)(WB^2-64WA^2) force WA=WB=0, after which
   G8_1 = (5k/4096)t(3s^2-64t^2), G8_2 = (5k/65536)s(s^2-192t^2),
   with no common zero on D(kappa) cap (D(s) cup D(t)).

CELL 6  old plane, next rank one, dies at grade eight                CONFIRMED
   Both conjugate branches u2 = +- r v2 computed; the published grade-eight
   forms match exactly.  In brackets (r=8i):
     E1 = (3v^2/2048)[16rs + 1024t + r*lam^2],
     E2 = (3v^2/4096)[16s - 16rt - lam^2],
   and E1bracket - r*E2bracket = 2r*lam^2, so lam=0; then s=rt; then
     G8_2 + (r/16) G8_1 = -(5/128) r kappa t^3 = -(5i/16) kappa t^3,
   and the conjugate branch gives +(5i/16) kappa t^3.  kappa!=0 forces
   t=s=0, contradicting the valuation-two open x!=0.
```

### 1.4 Controls I ran that the sealed replay does not

- **Non-vacuity.** A random rational old-plane 7-jet satisfies grades 0–7
  identically and fails only at grade 8. The system is not inconsistent from
  the start, so the exclusions are not artefacts of an empty setup.
- **Full sensitivity census (the strongest control here).** I mutated **each
  of the 569 frozen tail coefficients in turn**. 119 carry `k6`/`k2` or have
  minimum Λ-degree above 8 and are correctly invisible through grade 8; of the
  450 live terms, **450/450** change some row at grade ≤ 8 (402 already at
  grades ≤ 7, 48 exactly at grade 8). The result depends on the frozen source
  term by term. The sealed replay's control is a single in-memory perturbation
  of one derived row-6 cubic coefficient — much weaker, and it does not
  exercise the `tails.json` → maps reconstruction path at all.
- **Load-arrival.** Perturbing `k6₁`, `k6₂` changes nothing through grade 8;
  perturbing `k10₁` changes nothing through grade 8 on the old plane.
- **`kappa` load-bearing.** With `kappa = 0`, cells 5 and 6 lose their
  obstruction (grade-8 rows 1 and 2 vanish). The source condition
  `k10[0] != 0` is genuinely load-bearing for exactly those two cells; cells
  1–4 are `kappa`-free.
- **Engine cross-check.** The independent univariate numeric path reproduces
  the Cell-4 grade-eight `D`/`F` values exactly at a random point.
- Supplementary: the sealed replay itself runs clean here in 2.53 s and its
  banner matches its report.

### 1.5 Repair 1 — the `k6` load-arrival reason is not the stated one

The report says: *"Since `k6[0]=0`, the first possible `Lambda^6 k6`
contribution has grade at least nine."* The **conclusion is correct**; the
**reason as stated is insufficient**. Rows 2, 4 and 6 each contain `k6`
monomials whose companion factors are drawn only from `C0, C2, C4, C6` — all
of which carry nonzero constants under the V20R2 map. Weight bookkeeping alone
therefore permits a `Λ⁶·k6₁·Λ = Λ⁷` contribution in those three rows.

What actually forbids it is an arithmetic cancellation: evaluating the
constant part of the `k6` load gives, in every one of the seven rows,

```text
sum over k6-monomials of coeff * prod C_j(const)^{e_j}  =  0.
```

(row 2, explicitly: `-45/2048 + (15/128)(3/8) - (3/32)(3/8)^2 - (3/16)(1/16)
+ (3/4)(1/256) = 0`.) Only after that cancellation does a `k6` term require a
`d`-factor, pushing it to `Λ⁹`. **Repair:** state the vanishing of the
constant-evaluated load coefficient as the reason, and record it as a checked
identity of the normalized source. The same substitution applies to the
report's `k10[1]`/`k10[2]` removals, which rest on `M4(ell)=0` and
`polar_M4(ell,y)=0`, not on weights.

### 1.6 Repair 2 — the composition claim needs one more line

The report concludes that promotion leaves "only valuations three, four, and
five". Composing with the promoted `r=1` and `r>=6` exclusions, that is right
for every **finite** valuation. It omits `v_Λ(d) = ∞`, i.e. `d ≡ 0`.

That case is not idle: I checked it, and **with `d ≡ 0` all seven rows vanish
identically in Λ through `Λ¹⁹`, for arbitrary `k10`, `k6`, `k2` series.** The
normalized constants are an exact solution of the loaded system, so nothing in
grades 0–19 obstructs them. The lane dies only at the target column:
`Φ₇ = −Λ¹⁹·Jdet/4`, so vanishing through grade 19 forces `Jdet[0] = 0`,
contradicting the declared source. **Repair:** add that one line. It uses a
different instrument (the grade-19 target and `Jdet[0] != 0`) at a different
grade from all six cells, so it must be stated, not absorbed.

### 1.7 Maximum typed theorem and source-scope consequence

```text
THEOREM (maximum typed form, reconstructed and confirmed).
Over any field K of characteristic zero, for the exact normalized V20R2 K00
source with C6=1, k10[0]=kappa != 0, k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0,
there is NO K-valued jet d = Lambda^2 x + Lambda^3 y + Lambda^4 z + ... with
x != 0 satisfying all seven rows through Lambda^8.
Cells 1-4 do not use kappa != 0; cells 5-6 do.  No cell uses Jdet[0] != 0.
No passage to an algebraically closed field is required: each isotropic
branch is either empty over K or dies by the displayed identity over K.
```

Scope, stated as narrowly as the packet requires: this is a statement about
**field-valued compatible finite jets on one normalized support through grade
eight**. It is not an arc, a formal family, an algebraic germ, a polynomial
map, a counterexample, or a JC2 result. It says nothing about the nonreduced
scheme structure of the cone, about any other K00 support or normalization, or
about attainment of any surviving valuation.

Source-scope consequence, with Repair 2 applied:

```text
v = 1        promoted dead
v = 2        dead through grade 8 (this reconstruction)
v = 3,4,5    REMAIN POSSIBLE, none attained
v >= 6       promoted dead
v = infinity dead at grade 19 by Jdet[0] != 0 (one line, different instrument)
```

## 2. The cross-cutting correction: the true load calendar

Three of the four blind reports schedule the remaining valuations with the
same table, and all three schedule the **wrong object**.

The minimum transverse degrees `(D10,D6,D2,u2,u4,u6,-h/4) = (3,2,2,1,1,1,0)`
and the arrival law `Λ² k10 D10 at 2+3v` describe the **contracted grade-19
equation `Rmix`**. They are used by Grok's `K00-V25-FIRST-LOAD-CALENDAR`, by
Fable's `LEADING-CONE-UNIVERSALITY`, and by my own blind §5.3 budget table as
if they scheduled the **seven-row source system** in which `Q_i`, `DQ(x)`, and
the whole rank fan live. They do not.

Measured directly, on generic points of the leading cone, confirmed across
three independent random seeds:

```text
v |  Q(x)=0 |  DQ(x)[y]=0 |  kappa=k10[0] enters | k10[1] | k6[1] | k2[1]
--+---------+-------------+----------------------+--------+-------+-------
2 |    4    |      5      |          6           |    7   |  10   |  13
3 |    6    |      7      |          8           |    9   |  11   |  14
4 |    8    |      9      |         10           |   11   |  12   |  15
5 |   10    |     11      |         12           |   13   |  13   |  16
                            (2+2v, not 2+3v)
```

`kappa` enters at `2 + 2v` through the quadratic part of the `k10` load, two
to five grades earlier than the tables say, and always in rows 1,2,3,5,7 —
**rows 4 and 6 remain `kappa`-free at that grade for every remaining
valuation**, which is exactly what makes the zero-image-row technique of Cells
2–3 work.

Consequences, each a separate verdict:

- **Grok `K00-V25-FIRST-LOAD-CALENDAR`: REFUTED as a schedule for the
  seven-row system.** The claimed load-free windows (grades 7–10 at `v=3`,
  9–13 at `v=4`, 11–16 at `v=5`) are wrong; `kappa` is already in grade 8, 10,
  12 respectively. Card 3's stated cheapest move, "expand valuation three at
  grades 6–10 as the cheapest remaining window before D10 enters at 11", is
  the error in its purest form. The calendar may still be correct **about
  `Rmix`**; the two objects must not share a table.
- **Fable `LEADING-CONE-UNIVERSALITY`: PASS_WITH_REPAIR — correct conclusion,
  wrong reason, and true more widely than claimed.** The right inequality is
  `2v < 2+2v`, which holds for **every** `v >= 1`, so the leading vector lies
  on the same `V(A,B)` with the same rank-`<=2` stratification at `v=2` as
  well. Fable's asserted asymmetry ("unlike `v=2` where grade 8 mixes in
  `kappa L_i`") is spurious: no load interferes at grade `2v` for any `v`; the
  `v=2` proof simply runs two grades past the first load.
- **My own blind §5.3 budget table and its ordering `v=5 < v=4 ≈ v=3 < v=2`:
  SCOPE-CONFLICT, self-refuted.** It is a statement about `Rmix` only. Under
  the seven-row schedule every remaining valuation has an identical opening:
  **load-free grades exactly `{2v, 2v+1}`, load at `2v+2`**. There is no
  cheapest case; the four cases differ only in their distance to grade 19. My
  recommendation to attack `v=5` first is withdrawn.

The positive form of this correction is the most useful mathematical output of
the round:

```text
UNIFORM OPENING (measured, all v).  On the leading cone V(A,B):
  grade 2v    : Q(x) = 0                    (same seven quadrics, same cone)
  grade 2v+1  : DQ(x)[y] = 0                (same rank fan, same Delta)
  grade 2v+2  : DQ(x)[z] + Q(y) + C3(x) + kappa*M4(x) = 0,
                with rows 4 and 6 zero-image and kappa-free.
```

Cells 2 and 3 of the `v=2` proof use **only** this structure. They therefore
transfer verbatim to `v=3,4,5`, which is what makes Launch 1 in §6 cheap and
near-certain to produce a verdict.

## 3. Hostile audit of my own OP-1 … OP-6

I attack these, not defend them. Two survive intact, one is materially
repaired, one is refuted as an equivalence, one is overstated, one is
downgraded in novelty.

### OP-1 (`Delta_P = Lambda_P`) — CONFIRMED, KNOWN-EQUIVALENT

The derivation holds under audit. `i_p = e·m_p + ord_p(g−ν)` is the standard
branchwise formula, valid because `(G−νZ^e)/L^e = (Z/L)^e (g−ν)` with
`ord_p L = 0`; `Σ_{p|P} m_p = α μ_P` because `F_d = ξH^α` cuts `α·div(H)` on
`L∞`; Noether's `i_P(C,D) = Σ_{branches p of C} ord_p(D)` licenses the sum.

New consistency check I ran that the blind report did not: Bézout closes the
loop. `de = Σ_P n_P + #(affine transverse intersections)` gives
`αβB² = αβB·Σμ_P − Σ_P Δ_P + td`, hence `Σ_P Δ_P = td` **independently** of
the promoted `Σ_F Λ_F = td`. The polar-bridge identification also checks:
`F_X = Z^{d−1} f_x`, and `dy = f_x dg` gives `ord_γ f_x = λ_γ − m_γ` at a pole
and `= −m_γ − e_γ` at a non-pole place, so
`ord_γ F_X − (d−2)m_γ = λ_γ` at poles and `< 0` elsewhere — which is exactly
what the promoted bridge's `max{0,·}` does. Self-classification
`KNOWN-EQUIVALENT` was correct.

**Retained theorem:** `Δ_P = Σ_{p|P} λ_p`, with `Σ_P Δ_P = td` by Bézout.

### OP-2 (`RPMC` in tree coordinates) — REFUTED AS AN EQUIVALENCE

This is the material failure, and the packet asks the right question.
`AUDIT` 9356 ff. defines

```text
RPMC(C):  E_i <= C mu_i / B,   E_i = (1/2) sum_{p > P_i} (R_p/alpha - S_p/beta)^2
```

— a **rooftop energy**, not a pole mass. My blind §3.2 wrote `E_P = Δ_P/(αβ)`
as a *definition* and then silently identified it with the audit's `E_i`. What
OP-1 plus the audit's no-cross-terms splitting actually give is only

```text
sum_P Delta_P/(alpha beta) = td/(alpha beta) = E_MR = sum_i E_i
```

— an equality of **sums**. The per-point identity `E_i = Δ_{P_i}/(αβ)` does
not follow from it and I did not prove it. Therefore:

```text
RPMC(C) becomes  a_P b_P/nu_P <= C mu_P/B   ONLY under an unproved bridge
   ENERGY = POLE-MASS :  E_i = Delta_{P_i}/(alpha beta) for each proper root.
Without that bridge, OP-1 + OP-2 deliver only the SUMMED statement, which is
KJN, not RPMC.  Per-point implies summed; summed does not imply per-point.
```

`OP-2` is downgraded from `NEW (per-point form)` to **`PROVISIONAL`, gated on
`ENERGY=POLE-MASS`**, which becomes Launch 2 in §6. I also note that `KJN(C)`
in my reformulation (`Σ_P a_P b_P/ν_P ≤ C`) is a restatement of `E_MR ≤ C`
via T7's `Λ(F) = a_F b_F αβ/ν_F`, not new content.

### OP-3 (the `(mu,B)`-forgetting quotient) — PASS_WITH_MATERIAL_REPAIR

The structural half is confirmed against `REDUCTION.md` T7: the entry datum is
`(α,β; s; {(Λ_i,a_i,b_i,ν_i)})` with `Λ(F) = a_F b_F αβ/ν_F`, and it carries
neither `μ_P` nor `B`. The arithmetic half is confirmed: at type `(2,3)` with
entries `(a,b,ν) = (1,2,3)`, `Λ_i = 4`, `E_MR = 2R/3`, `td = 4R`; the
td12 three-pole U1 entry **is** `U1*(3)`, with `E_MR = 2`.

But my headline sentence — *"the reduced merge/trunk laws cannot bound `td`
because they are scale-free and the bound is a statement about scale"* — is
**wrong**, and I withdraw it. `KJN(C)` is `E_MR ≤ C`, and `E_MR` is a function
of the reduced record alone. The conclusion is scale-free. What is not
scale-free is `RPMC`, the only currently named *sufficient local lemma*.
Corrected statement:

```text
The reduced interface can STATE and EVALUATE the ceiling (KJN is a predicate
on the entry datum).  What it cannot do is PROVE it, and the only named route
to a proof -- RPMC -- is stated in data (mu_P, B) the interface drops.
SCALE-PIN is instrumentation for the PROOF ROUTE, not for the STATEMENT.
```

This repair also **kills my blind §4.4 and the headline of my blind `SCALE-AUDIT/v1`.**
Since `KJN(1)` is decidable on the reduced record, the td12 entry's fate under
it needs no new instrument: `E_MR = 2 > 1` by hand. The integer-feasibility
search over `(B, μ_i)` I proposed has a predetermined outcome and is not a
discriminator. What survives of `SCALE-AUDIT` is only the consistency gate
`Λ_i =? αβ a_i b_i/ν_i`, `td =? ΣΛ_i` over the filed corpus — a data-defect
detector, a hygiene item, not a mathematical launch.

The disjunction itself survives, in a **stronger** form than I stated: it
needs only the weaker summed conjecture.

```text
KJN(1) + T5 (td >= 6)  =>  every type-(2,3) counterexample has td = 6 exactly,
so U1*(R) is impossible for every R (td = 4R is never 6), and the ENTIRE
conditional td12/U1/A7/C5/B25/S17/D13/E11 laboratory is vacuous.
Hence: either KJN(1) is false, or no U1*(R) occurs.  Not a verdict on either.
```

`KJN(1)` remains **type-relative**: it gives `td ≤ αβ`, so it is not an
absolute ceiling without a type menu. My blind §2.1 ranking (G2, the type
menu, is co-equal with G1) stands and is reinforced.

### OP-4 (non-properness defect ledger) — CONFIRMED, two repairs

Re-derived and checked. `dg` never vanishes on the affine fibre because
`dg` evaluated on the tangent `ker(df) = span(−f_y, f_x)` equals `J = 1` — the
Keller condition doing the work directly. Hence
`δ(λ,c) = Σ_{non-pole p, g(p)=c} e_p`, and Riemann–Hurwitz with all
ramification at infinity gives

```text
Delta(lambda) = sum_c delta(lambda,c) = sum_{non-pole p} e_p
              = td + s + n + 2G - 2 = td - chi(fibre).
```

Consequences confirmed: `Δ ≥ td` with equality iff `G = 0`, `s = n = 1`.

- **Repair 4a (notation).** I wrote `Σ_i δ_i·deg(f|_{S_i}) = Δ`. `S_F` lives
  in the target, where the first coordinate is a *value* of `f`; the correct
  object is `deg(pr₁|_{S_i})`, and the identity needs `δ` generically constant
  on each component and `λ` outside a finite bad set. Rename and qualify.
- **Repair 4b (upgrade, credit Fable).** My justification that `f` is
  primitive was a citation. Fable's is a proof and I adopt it: if `f = h∘u`
  then `J(f,g) = h'(u)·J(u,g) = 1`, so `h'(u)` is a unit in `C[x,y]`, hence
  `deg h ≤ 1`. Two-line, uses `J = 1`, needs no external input.

### OP-5 (exact inertia cycle type) — PASS_WITH_REPAIR, and I overstated it

The **local** theorem is correct and cheap. Over `C \ T_λ`, `g|_{F_λ}` is a
genuine degree-`td` covering (unramified affinely by the `J=1` argument;
proper by definition of `T_λ`), and over a small punctured disc at `c ∈ T_λ`
the preimage is `td − δ(λ,c)` trivial sheets plus one `e_p`-fold cyclic cover
per non-pole place `p` with `g(p) = c`. So

```text
cycle type of the meridian at c = ( e_p : g(p)=c, p non-pole ) + 1^{td-delta}.
```

Transitivity needs `F_λ` connected, which Repair 4b now supplies. Jordan's
theorem applies as stated (transposition under primitivity gives `S_td`; a
prime `p`-cycle with `p ≤ td−3` gives `A_td` or `S_td`).

**What I overstated.** The claim that "the passport is **determined**" and that
"you never need to construct `A(F)`" is not supported by the local theorem.
The cycle types are determined by the multiset `{e_p}` **partitioned by the
value `g(p)`**. That partition — which non-pole places share a critical value —
is a *global* datum about how boundary places organize into components of
`S_F`. The per-place contact orders that the books compute do **not** supply
it. Grok's blocker on Avenue 7 is therefore only partly answered:

```text
OP-5 verdict:  local meridian theorem  PROVED / NEW as stated.
               "determined passport"    OVERSTATED -> PROVISIONAL, gated on
                                        the g-value partition of non-pole
                                        places, which is not in the books.
               "never need A(F)"        REFUTED AS STATED.  Strictly less than
                                        A(F) is needed, but strictly more than
                                        per-place contact orders.
Avenue 25 raise: conditional on the partition, not unconditional.
Avenue 7 raise:  withdrawn to "unchanged" until the partition is typed.
Avenue 26:       unchanged; its seam is untouched by this correction.
```

### OP-6 (minimal-`td` selection) — KNOWN-EQUIVALENT plus a small increment

My statement that "`REDUCTION.md` T4 records that **arbitrary-pair** Sigray
normalization … preserves `td`" is **wrong**. T4 explicitly requires passing
first to the representative `F* = K∘F∘L` whose degree pair is
**lexicographically minimal in the automorphism-equivalence class**.

The conclusion nevertheless survives, and the reason is worth stating because
it is exactly what GGV-minimality lacks:

```text
td is an invariant of the polynomial-automorphism equivalence class, and a
positive integer.  So: select a class of minimal td; pass to its lex-minimal
representative (td unchanged, K and L bijective); apply T4 (td unchanged).
The selected pair is still of minimal td among all counterexamples.
GGV-minimality minimizes gcd(deg P, deg Q), which is not a td invariant, so
that selection cannot be composed with a td-minimality hypothesis.
```

T4's own text already records the fork ("One may apply T4 to the counterexample
selected in T2 … but then T3's polygon datum is logically unused"), so OP-6 is
**not** new as a spine statement. The genuine increment is one sentence: *td is
a class invariant, so td-minimal selection is free and survives normalization.*

Source-audit debt replacing GGV minimality, named exactly: Sigray Lemma 2.1
(unrefereed thesis) resting on **Abhyankar Theorems 18.13 and 19.2 as external
inputs with no promoted internal replacement**, with `SIGRAY-AUDIT.md` covering
§§2–5 and §6 only through Proposition 6.2. That is gap `HIGH 3`, and choosing
this branch makes it load-bearing rather than latent. The
block-quotient-to-smaller-Keller-map seam is untouched by any of this and
remains the single open step of the descent.

## 4. The other proof-side proposals

### 4.1 Fable `EXCESS-e` — arithmetic CONFIRMED, premise UNREVIEWED, value DEDUPLICATED

The consequence arithmetic checks. At `U1*(R)` (`s = R`), full PCB is
`EXCESS-(R−1)`; the adjusted budget `(4R−k−2)−(R−1) = 3R−k−1` against floor
`3R−1` gives slack `−k < 0` for every `k ≥ 1` — so under Fable's semantics
full PCB empties the family. `EXCESS-1` kills S17's one-step cell (`8 > 8−1`)
and the three zero-slack D13/E11 witnesses `(539,99)@49`, `(893,95)@47`,
`(154,22)@7` in the full-exit floor regime (`10 > 10−1`), while B25 and the
A7/C5 tails survive at zero slack. Internally consistent.

The load-bearing step is the **budget semantics** ("every printed ceiling is
rooted at total weight `td−1`, so `EXCESS-e` lowers every printed ceiling by
`e`"). Fable flags it as same-model and unreviewed and gates the card on it.
That gate is correct and I do not lift it. Scope rider: the argument runs at
**typical-fibre** records; any consumed record must be typed typical or the
result is `OPEN`, and a retreat to the atypical fibre is itself the finding.

**Dedup finding.** "Full PCB would eliminate `U1*(R)`" is a *low bar*: §3's
`KJN(1) + td ≥ 6` already eliminates every `U1*(R)` by pure arithmetic on the
entry datum, with no budget semantics and no Section-7 input. Two independent
unproved conjectures clear the same bar, so clearing it is **not** evidence for
either and must not be used to rank them. The distinguishing content of
`EXCESS-1` is its per-value, per-fibre reach at `td = 12` — which is
conditional laboratory work, not selector work.

### 4.2 Fable `ATYPICAL-EXISTENCE` — CONFIRMED, and provable more cheaply

The skeleton is correct: `J = 1` ⟹ `f` primitive (the `h'(u) | 1` argument,
adopted above); no atypical value ⟹ locally trivial fibration ⟹
`χ(fibre) = χ(C²) = 1` ⟹ `2 − 2g − n = 1` ⟹ `g = 0`, `n = 1`; then AMS plus
A¹-fibration triviality make `f` a coordinate; then `J(x,g) = g_y = 1` gives
`g = y + c(x)`, an automorphism.

**Independent convergence and a shorter proof.** OP-4's ledger closes the last
three steps without AMS or the Kambayashi–Miyanishi class input. Once
`g = 0, n = 1`, the single place at infinity either is or is not a pole of `g`:

```text
not a pole : g extends regularly to the compactified fibre P^1, hence is
             constant on the generic fibre, so dg ^ df = 0 and J = 0.  X
is a pole  : then s = 1, n = 0, so Delta(lambda) = 0, and
             Delta = td + s + n + 2G - 2 = td - 1 forces td = 1, i.e. an
             injective polynomial map, i.e. an automorphism.  X
```

So `ATYPICAL-EXISTENCE` is provable from `J = 1`, the Euler ledger, and
`td = 1 ⟹ automorphism`, with **one fewer external dependency** than Fable's
route. Verdict: `CONFIRMED / KNOWN (classical) / dependency-reduced`. The open
content is entirely `WEIGHT-AT-ATYPICAL`, exactly as Fable says.

### 4.3 Fable `AM2-PLACE-LEDGER` — KNOWN-EQUIVALENT to OP-1; no new equality

AM-2 is `ord_t(f_y) = ord_t(dx/dt) − ord_t(dg/dt)`. That is precisely
`dx = −f_y·dg`, the `x`-chart half of the same fibre identity whose `y`-chart
half, `dy = f_x·dg`, I used to verify OP-1's polar-bridge identification.
Both halves are `J = 1` restricted to the fibre. Therefore:

```text
AM2-PLACE-LEDGER  ==  OP-1  ==  the promoted EXACT POLAR BRIDGE,
in three charts, derived independently three times this round.
```

This is a strong independent-convergence signal about the identity and a
strong **dedup** about the instrument: at most one of these should hold a
slot. To the packet's precise question — does AM-2 per component of `A(F)`
supply a new equality before a full boundary contact table is known? — **no.**
The unknowns of Fable's feasibility system *are* the contact orders; the
identity constrains them but does not determine them. Fable's own
`UNDERDETERMINED(list)` outcome is the honest expected one, and its real
product is a **source-typing schema** for `DETOUR-EXCLUSION/v2`, not an
exclusion. What AM-2 genuinely adds over the promoted bridge is
disaggregation: OP-1 shows the aggregation `Σ_{p|P} λ_p = Δ_P` is exactly the
information the per-root form discards.

### 4.4 Sol `TD12-SEXTET-INDUCED-CHAR` — DUPLICATE at the separating tier

All six rows A7/C5/B25/S17/D13/E11 descend from **one** antecedent entry,
which §3 identifies as `U1*(3)`. Sol's test consumes parent data — the parent
deck group, the full-index relation `i_F = 3n·i_G`, shared coefficients,
shears and scales. A discriminator that is a function of the shared parent
acts **above** the split: it can only kill the common antecedent or say
nothing about the six. That is the same structural point I made blind about
`μ_P/B`, and it now applies to Sol's mechanism.

At the antecedent tier the question is already decided arithmetically by
`KJN(1)` (§3), so the character test adds nothing there either. Combined with
the U1 STOP audit's §4 firewall — characters are Fourier eigenspaces of one
cyclic orbit, not physical places, flags, or quotient lines — the verdict is
**`DUPLICATE` of existing character machinery for the purpose of separating
the sextet**, with no typed occurrence map. Demote; do not launch as a
discriminator.

### 4.5 Grok's actual-automorphism Section-7/PCB control — REFUTED as a discriminator

Grok asks whether the Section-7 objects are even defined at `td = 1` and makes
object-existence the cheapest discriminator. That is the right instinct, but
the outcome is **determined a priori** by OP-4's ledger and needs no run. For
an automorphism: `td = 1`; the generic fibre of the coordinate `f` is `A¹`, so
`G = 0` and there is exactly one place at infinity; that place must be a pole
of `g` (otherwise `g` is fibre-constant and `J = 0`); hence `s = 1`, `n = 0`,
`S_F = ∅`, `T_λ = ∅`. Then `s(a) − 1 = 0` and `PCB-EXCESS` reduces to
`Σ_i (I_i − wt_i(a)) ≥ 0`, which is exactly the nonnegativity repaired
Section 7 already proves.

So the experiment returns `COSTUME` with probability one and zero information.
Used constructively, as the packet directs: the sharpened hypothesis is that
**`PCB-EXCESS` has content only when `n ≥ 1`, i.e. only for non-proper maps**;
the automorphism case is vacuous, not false. The CE-only form is the right
form, and the general-map form should be retired as a target rather than
tested. Verdict: `REFUTED as a discriminator / hypothesis sharpened`. One
launch slot saved.

Grok's valuation calendar is handled in §2 (`REFUTED` for the seven-row
system). Grok's `DETOUR-FULL-EXIT-TIGHTNESS` (Card 2) is sound conditional
laboratory work and its zero-slack reading of D13/E11 matches the sextet
integration; it stays live but demoted, downstream of an antecedent that
`KJN(1)` would make vacuous.

### 4.6 Recheck of the U1 Hamiltonian–Kummer STOP audit — STOP UPHELD

I attacked it and it holds, with one repair to its reasoning and one addition
that strengthens it.

- §1's conditional identity `∇_j = d + (j/r) dlog(A)` is correct given a
  `D`-stable Kummer algebra, and the audit is right that `X_g` supplies only
  the `f` direction and does not define a connection on a two-dimensional base.
- §2 is correct: the reviewed U1 datum is `R(t) = t^r − A_*` at a **fixed**
  fibre with `A_* ∈ C^*` constant, so `dA_* = 0` and the characters are
  trivial. Promoting it would be the prohibited formal-data-to-map jump.
- **Repair to §3.** *"In its own twisted de Rham complex, `ω_j e_j = ∇_j(e_j)`.
  Hence the displayed connection form is automatically twisted-exact"* is a
  **tautology**: for any connection in any frame, `∇(e) = ω⊗e`. It proves
  nothing. The audit's next sentence carries the real argument — the connection
  becomes gauge-trivial on the Kummer cover via `T^{−j}`, so its monodromy is
  finite of order dividing `r` and its class is torsion. State that; delete the
  tautology.
- **Addition (strengthens the STOP, and independently reproduces both
  controls).** For a rank-one connection on a smooth affine curve `U` of genus
  `g` with `n` punctures, `χ_dR = χ_top(U) = 2 − 2g − n`, so a nontrivial
  character has `h⁰ = 0` and `h¹ = 2g − 2 + n`. This gives the audit's two
  controls exactly and for free: `G_m` (`g=0, n=2`) ⟹ `h¹ = 0`; `A¹∖{0,1}`
  (`g=0, n=3`) ⟹ `h¹ = 1`. It also gives the general statement the audit
  needs: the total receiver dimension is `(r−1)(2g−2+n)` — a Kummer index
  times an Euler characteristic **already in the ledger**. It grows with `r`
  only by counting the same topological number `r−1` times, and carries no
  datum beyond `(r, g, n)`. That is the load-bearing reason the receiver cannot
  be a new obstruction, and it is stronger than "torsion".
- §4's firewall is correct and decisive: `r−1` Fourier eigenspaces of one
  cyclic orbit are not `r−1` places, flags, quotient lines, or jumps.

Sol's blind Card 1 assumes rather than supplies all four reopen-gate objects
(actual occurrence over an open stratum; `D`-stable `T^r = A(f)`; a map to the
Section-7 quotient lines; an injective no-duplication assignment). The gate is
**not met**. `STOP` stands; the blind Avenue-16 raise is not consumed.

## 5. Deduplicated claim table

`IC` = independent convergence, recorded so it is not collapsed away.

| # | Claim | Origin | Verdict | Smallest exact thing worth keeping |
|--:|---|---|---|---|
| 1 | Leading cone `= V(A,B)`, a 4-plane; parametrization and rank fan by `Δ = u²+64v²` | Sol; Opus blind §5.1 (IC ×2) | **CONFIRMED** from source | `Q1+8Q3 = (3/2048)AB`, `Q4 = (3/524288)(B²−64A²)`, all `Q_l ∈ (A,B)`, `Q6 = 0` |
| 2 | Rowwise `DQ` factorization + `(α_i,β_i)` table, 4 nonzero minors | Sol | **CONFIRMED** | rows 1,3,5,7 ∥ `(u,−v)`; row 2 `= (3/256)(v,u/64)`; rows 4,6 zero-image |
| 3 | Leading rank one dies at grade 6 | Sol | **CONFIRMED** | `G6_6 = u(192v²−u²)/65536 = uv²/256 ≠ 0` on `Δ=0`, field-independent |
| 4 | Leading rank two dies at grade 6 | Sol | **CONFIRMED** | `H4`, `H6`; `u=0` ⟹ `v+3a=v+2a=0`; `u²=192v²` ⟹ `S5=v³/8`, `S7=−v³/64` |
| 5 | Old plane, next rank two, dies at grade 8 | Opus review (unreviewed) → Sol | **CONFIRMED** | `D`,`F` and the two syzygies; `D = t(u∓rv)²` on `s²+64t²=0` |
| 6 | Old plane, next rank zero, dies at grade 8; grade 8 invariant along the whole plane | Opus review → Sol | **CONFIRMED** as an exact identity | `WA·WB` and `WB²−64WA²`; the two `κ`-cubics |
| 7 | Old plane, next rank one, dies at grade 8 (both branches) | Sol (new) | **CONFIRMED** | `λ = 0`, `s = ±8it`, `∓(5i/16)κt³` |
| 8 | `k6` first contributes at grade ≥ 9 | Sol | **CONFIRMED, reason REPAIRED** | constant-evaluated `k6` load coefficient `= 0` in all seven rows |
| 9 | Composition leaves exactly `v ∈ {3,4,5}` | Sol / state packet | **PASS_WITH_REPAIR** | add `v = ∞`: rows vanish through `Λ¹⁹` at `d ≡ 0`, killed only by `Jdet[0] ≠ 0` |
| 10 | `κ` load arrives at `2+3v` in the valuation lane | Grok calendar; Fable lemma; Opus blind §5.3 (IC ×3, all wrong) | **REFUTED** for the seven-row system | `κ` arrives at `2+2v`; load-free grades are exactly `{2v, 2v+1}` |
| 11 | Same cone and stratification for all remaining `v` | Fable | **CONFIRMED, reason repaired, wider** | `2v < 2+2v` for all `v ≥ 1`, including `v = 2` |
| 12 | `Δ_P = Λ_P` (Bézout defect = pole mass) | Opus `OP-1`; Fable `AM-2`; promoted polar bridge (IC ×3) | **CONFIRMED / KNOWN-EQUIVALENT** | `Δ_P = Σ_{p|P} λ_p`, `Σ_P Δ_P = td` by Bézout |
| 13 | `RPMC(C) ⟺ a_P b_P/ν_P ≤ Cμ_P/B` | Opus `OP-2` | **REFUTED as an equivalence** | needs the unproved bridge `E_i = Δ_{P_i}/(αβ)` |
| 14 | The ceiling "lives in" the dropped scale data | Opus `OP-3` | **PASS_WITH_MATERIAL_REPAIR** | `KJN` is scale-free and reduced-decidable; only the proof route needs `μ,B` |
| 15 | `KJN(1) + td ≥ 6` empties every `U1*(R)` and the td12 laboratory | Opus `OP-3`, strengthened here | **CONFIRMED (arithmetic)** | type `(2,3)` ⟹ `td = 6` exactly; `td = 4R ≠ 6`. Type-relative, not absolute |
| 16 | Non-properness/RH ledger `Δ = td + s + n + 2G − 2` | Opus `OP-4` | **CONFIRMED**, 2 repairs | `dg\|_{ker df} = J = 1`; use `deg(pr₁\|_{S_i})`; primitivity by `h'(u)\|1` |
| 17 | Exact meridian cycle type at generic `(λ,c)` | Opus `OP-5` | **PROVED (local)** | `(e_p : g(p)=c) + 1^{td−δ}` |
| 18 | Passport determined; `A(F)` never needed | Opus `OP-5` | **OVERSTATED / REFUTED as stated** | missing datum: the `g`-value partition of non-pole places |
| 19 | td-minimal selection is free and survives normalization | Opus `OP-6` | **KNOWN-EQUIVALENT + small increment** | `td` is an automorphism-class invariant; T4 needs the lex-minimal representative |
| 20 | `EXCESS-1` kills S17 and the zero-slack D13/E11 witnesses | Fable | **arithmetic CONFIRMED / premise UNREVIEWED** | budget-semantics note must pass review first; typical-fibre scope |
| 21 | Full PCB empties `U1*(R)` | Fable | **CONFIRMED but DEDUPLICATED** | `KJN(1)` already does it; clearing this bar ranks nothing |
| 22 | `ATYPICAL-EXISTENCE` | Fable | **CONFIRMED / dependency-reduced** | provable from `J=1` + OP-4 ledger + `td=1 ⟹ aut`, without AMS |
| 23 | `AM2-PLACE-LEDGER` is a new place-global instrument | Fable | **KNOWN-EQUIVALENT to #12** | keeps value only as a source-typing schema, `UNDERDETERMINED` by design |
| 24 | `TD12-SEXTET-INDUCED-CHAR` is a new source discriminator | Sol | **DUPLICATE at the separating tier** | parent-level test cannot separate descendants of one entry |
| 25 | Automorphism Section-7/PCB control | Grok | **REFUTED as a discriminator** | outcome fixed: `s=1, n=0` ⟹ `PCB` reduces to proved nonnegativity |
| 26 | `U1-HAM-KUM-CONN` STOP | Sol audit | **UPHELD**, §3 reason repaired | receiver dimension `= (r−1)(2g−2+n)`: index × Euler number, no new datum |
| 27 | `D13/E11` zero-slack tightness as a first actual-weight cut | Grok Card 2 | **LIVE, demoted** | conditional; downstream of an entry `KJN(1)` would void |
| 28 | Body-seal validator | Fable (`ops/seal.py`), Grok (`verify_body_seal.py`), Sol (`INGESTCHECK`) (IC ×3) | **ACCEPT `ops/seal.py`** with 2 repairs | standalone-line marker rule; `ops/lane.sh` has no seal hook today |

## 6. Portfolio — three mathematical launches

Selected to cover proof, falsification, and bypass with no duplication, after
the dedup in §5 retired four proposals and my own two headline cards.

### Launch 1 (falsification) — `K00-V345-UNIFORM-OPENING`

- **Novelty.** `NEW` only as a corrected schedule; the target is the consensus
  next step of all four blind reports (Sol `JETFAN`, Fable Card A, Grok Card 3,
  Opus Card C). This card replaces their scheduling with §2's measured one.
- **Exact theorem to prove or break.** For each `v ∈ {3,4,5}`: on the same cone
  `V(A,B)`, the leading rank-one and rank-two strata are excluded at grade
  `2v+2` by the zero-image rows 4 and 6, and the rank-zero (old-plane) stratum
  reduces to a next-coefficient rank fan at grades `2v+2 … 2v+4`.
- **Why it is near-certain to return a verdict.** Cells 2–3 of the `v=2` proof
  use only the uniform opening `{2v : Q(x)=0}`, `{2v+1 : DQ(x)[y]=0}`,
  `{2v+2 : load arrives, rows 4 and 6 κ-free}`, and §2 measures that structure
  to be identical for every remaining `v`. The transfer is mechanical.
- **Dependencies.** The frozen `tails.json` and V20R2 map (hashes in §0); §2's
  calendar; the confirmed §1 theorem as positive control. Nothing unreviewed.
- **Both outcomes.** All three excluded ⟹ this support is empty at every finite
  valuation and Avenue 36's K00 lane closes on V20R2 (**not** K00 as a whole,
  and not a JC2 result). Any stratum surviving to grade `2v+4` ⟹ the first
  nonempty finite jet on this support; freeze it, and only then ask separately
  about grade 19, arcs, bounded support, algebraization, and occurrence.
- **Owner/reviewer.** Producer: any non-Sol model (Sol produced the `v=2`
  theorem). Falsifier: the 450-term sensitivity census re-run at each `v` inside
  the same process. Hostile reviewer: a third model, different from both.
- **Placement.** Desk. The `v=2` reconstruction cost 0.5–5 s per cell here; the
  `v=5` window is the largest and is well inside 60 s / 1 GiB. **No AWS.**
- **Stop.** First exact nonzero cokernel witness per stratum; or the first need
  for elimination beyond hand size, at which point preregister rather than run.

### Launch 2 (proof) — `ENERGY = POLE-MASS`

- **Novelty.** `NEW`; it is the precise gap my `OP-2` concealed.
- **Exact theorem.** For a Sigray-normalized Keller pair and each proper root
  `P_i` of the common leading form,
  `(1/2) Σ_{p > P_i} (R_p/α − S_p/β)² = (1/(αβ)) Σ_{p|P_i} λ_p`.
  Both sides are known to sum to `E_MR` over all roots; the question is whether
  they agree **termwise**.
- **Cheapest discriminator, before any general proof.** `RPMC(1)` **plus** this
  bridge forces `Λ_P ≤ αβ μ_P/B` at every root. At residue-A (`α,β = 2,3`, two
  poles, `Λ_P = 3`, `td = 6`) that reads `3 ≤ 6μ_P/B` at both poles, which with
  `Σμ = B` forces `μ₁ = μ₂ = B/2` **exactly** — independently of `B`. So the
  conjunction makes a falsifiable prediction about a filed record. Check the
  actual residue-A `μ` split first; it costs one lookup.
- **Both outcomes.** Bridge proved ⟹ `RPMC` becomes an inequality about pole
  mass with OP-1's geometric meaning, and `SCALE-PIN` is re-armed as proof
  instrumentation. Bridge refuted, or the residue-A split asymmetric ⟹ retire
  the whole `OP-2`/`SCALE-PIN`/`per-point-pole-mass` framing, and the capacity
  lane learns that its local lemma is **not** about pole mass — which is itself
  a genuine narrowing of the only named ceiling route.
- **Owner/reviewer.** Prove: capacity/`DIR` lane. Falsify: the residue-A `μ`
  check, different owner. Reviewer: different model from both.
- **Placement.** Desk (the discriminator is arithmetic); the theorem is proof
  work.
- **Stop.** Stop on the residue-A asymmetry, or on any promoted record where
  the two sides differ at a single root.

### Launch 3 (bypass) — `INERTIA-PARTITION`

- **Novelty.** Stage 1 is `PROVED` above (§3, `OP-5` local theorem). The card is
  the **partition question**, which is the only thing standing between the
  local theorem and a determined passport.
- **Exact question, fail-closed.** For the filed `td = 6` residue-A record, do
  the promoted boundary tables determine which non-pole places share a value of
  `g`? Three typed outcomes: `PARTITION_DETERMINED` (write the determined
  meridian cycle types and compare with the 169 admissible `S₆` passports);
  `PARTITION_UNDERDETERMINED(list)` (name exactly the missing datum — this is
  the honest expected outcome and is the correct input to Avenues 7/25/26);
  `OBJECTS_UNDEFINED` (the tables do not carry non-pole places at all, in which
  case Avenue 25 stays where it was).
- **Both outcomes.** Determined and strictly smaller than 169 ⟹ the method has
  kill power the 2026 admissibility test never had, and Avenues 7/25/26 rise
  together. Determined but reproducing all 169 ⟹ stage 1 is exact with no
  `td = 6` leverage and the value is entirely in the block-descent seam.
  Underdetermined ⟹ my `OP-5` raise of Avenue 7 is correctly withdrawn and the
  missing datum is named for the first time.
- **Owner/reviewer.** Producer: passport/Avenue-25 owner. Falsifier: a reader
  hunting for a flag/place/series identification in the partition step — the
  exact firewall this claim is most likely to violate. Reviewer: different model.
- **Placement.** Desk; bookkeeping against existing tables plus hand group
  theory at `td = 6`.
- **Stop.** Stop at the first place where a cv flag would have to be identified
  with a physical place or a cover series; return `OPEN` rather than bridge it.

## 7. The one bounded systems trial

**`SEAL-HOOK/v1` — repair `ops/seal.py` and wire it into `ops/lane.sh` at the
`2026-08-31T16:35Z` checkpoint.** Not now: the packet forbids modifying
`ops/lane.sh` while these lanes are active, and `seal.py`/`test_seal.py` are
uncommitted.

Review of the submitted tools, run here:

- `python3 ops/test_seal.py` — 6/6 pass in 0.35 s.
- `python3 ops/seal.py verify` over this round's **eight real sealed
  artifacts** — 8/8 `PASS`, and every reported `body_bytes`/`body_sha256`
  matches the value I computed independently in §0. That is the acceptance test
  that matters and it was not in the submitted suite.
- **Marker semantics are right, and right for the documented incident.** Only a
  standalone line counts, so an inline backticked mention is body text
  (verified), a marker at column 0 inside a fenced block correctly yields
  `found 2` and fails closed (verified — this is exactly the "recipe quoting the
  marker" case Grok cites), an indented or trailing-space marker yields
  `found 0` and fails closed (verified), CRLF is handled (verified). No `rfind`,
  no `find` — a line scan, which is better than Grok's proposed contract.
- TOCTOU and atomicity: `O_NOFOLLOW` + `fstat`/`S_ISREG` on the open fd;
  `lstat` dev/ino compared before and after staging; same-directory temp file;
  `os.replace`; directory `fsync`. Sound for the real threat, which is a
  concurrent lane, not an adversary.

Two repairs, both required before wiring:

1. **Failure attribution.** `verify a.md b.md c.md` evaluates all paths before
   printing anything, so a failure suppresses the `PASS` lines of already-verified
   files **and the error message does not name the failing path** (reproduced:
   `seal: INVALID: expected exactly one standalone BODY-END marker, found 0`,
   with no path). In a custody tool an unattributed failure is a defect. Print
   per path as you go, and wrap the error with the path.
2. **The frozen basis is reported but never checked.** A seal declaring basis
   `0000…0` verifies `PASS` (reproduced). Add `verify --expect-basis <hex40>`
   that fails on mismatch. Without it the tool cannot enforce the one property
   `ops/lane.sh` most needs.

Minor: `stamp` never re-reads and re-verifies what it wrote — add a post-stamp
`verify_path` so `STAMPED` means verified; `BODY_SHA_RE` tolerates a line break
after the label but `BODY_BYTES_RE` and `FROZEN_BASIS_RE` do not (asymmetric);
a near-miss marker (trailing space) reports "found 0", which reads as "missing"
rather than "malformed".

**Smallest measurable acceptance test.**

```text
1. ops/seal.py verify --expect-basis <basis> over the eight round artifacts
   -> 8 PASS, one line per file, exits 0.
2. Same command with a wrong --expect-basis -> nonzero, message names the
   file AND the declared vs expected basis.
3. verify over [good, bad, good] -> two PASS lines printed, one INVALID line
   naming the bad path, exit nonzero.
4. stamp then verify round-trips; re-stamp refuses; post-stamp self-verify
   is exercised (assert STAMPED implies a successful verify of the result).
5. ops/test_seal.py stays 6/6, plus new fixtures for (2) and (3).
6. Wired: lane.sh emits body_seal_status alongside charge_basis_status,
   and final_status is not DONE when the seal is invalid.
```

Ownership: systems owner implements; a different model reviews the diff
against `ops/validate_charge_basis.py` for scope creep. Placement: desk, under
one second. **Not selected:** `INGESTCHECK/v1` (a superset — dependency graphs,
supersession, instrumented path-scope proof — that should wait until the seal
hook is in and proven), and `FENCE-DEFAULT` in any coded form (§0.3).

## 8. Stop / defer list

```text
STOP (do not launch)
  TD12-SEXTET-INDUCED-CHAR as a sextet discriminator  (DUPLICATE, §4.4)
  AUT-SECTION7-EXCESS-CONTROL                          (outcome fixed, §4.5)
  U1-HAM-KUM-CONN as a lane; do not raise Avenue 16    (STOP upheld, §4.6)
  SCALE-AUDIT/v1 as a mathematical launch              (self-refuted, §3/OP-3)
  Opus blind FENCE-DEFAULT/v1 as a coded trial         (withdrawn, §0.3)
  Any use of the (3,2,2,1,1,1,0)/2+3v table to schedule the seven-row
    valuation system                                   (REFUTED, §2)
  Empirical RPMC/TDBOUND testing on automorphisms      (vacuous, blind §4.2)
  The grade-seven K00 Fitting packet; K00-RENORM; K00-SHIFT-LADDER;
    j=42; S j=13; quartet descendants; any AWS K00 job
  PCB or any EXCESS rung assumed as a premise anywhere

DEFER (live, demoted, not this checkpoint)
  AM2-PLACE-LEDGER, re-scoped as a source-typing schema for
    DETOUR-EXCLUSION/v2 rather than as a new instrument           (§4.3)
  EXCESS-e consequence table, behind its budget-semantics review  (§4.1)
  DETOUR-FULL-EXIT-TIGHTNESS on D13/E11                           (§4.5)
  TD12-U1-FAMILY-AWARE-DETOUR-EXCLUSION/v2                        (conditional)
  Block-quotient descent (OP-6 / Avenues 26,43), after Launch 3
  INGESTCHECK/v1, after SEAL-HOOK/v1 lands
  WEIGHT-AT-ATYPICAL, the only open half of ATYPICAL-EXISTENCE    (§4.2)
```

## 9. Synthesis recommendation

The round's real product is not the `v=2` theorem, which holds: it is that
three independent lanes scheduled the K00 valuation frontier with a table
belonging to a different object. Correcting it costs nothing and converts
`v=3,4,5` from three bespoke searches into three mechanical repeats of a proof
that is now confirmed twice, because every remaining valuation has the same
opening — `Q(x)=0`, `DQ(x)[y]=0`, then the load, with rows 4 and 6 always
zero-image and `kappa`-free. Run that first.

On the proof side, the honest news is a demotion of my own headline. `KJN` is
a predicate on the reduced entry record, not a statement about dropped scale
data; it already voids every `U1*(R)` and the whole td12 laboratory by
arithmetic, so no new instrument discriminates there. The one genuinely
missing step is small and exact — whether rooftop energy equals pole mass root
by root — and it has a one-lookup falsifier at residue-A. Fund that, not
another interface row.

Three lanes converged on one identity (`Δ_P = Λ_P` = AM-2 = the promoted polar
bridge). Treat that as evidence about the identity and as a reason to fund it
once. Two conjectures independently empty `U1*(R)`; that bar ranks nothing.

Keep the sextet, the detour work, and `EXCESS-e` alive but below the line:
each is downstream of an antecedent that one already-named conjecture would
make vacuous. Ship the seal hook, with attribution and a basis check, at the
scheduled checkpoint; keep the fence as a rule about command shape, which is
the only form of it anyone can enforce.

## 10. Non-claims

No occurrence, attainment, `PairRef`, source value, landing, coverage, degree
ceiling, type menu, algebraization, polynomial Keller pair, collision,
counterexample, or JC2 conclusion is asserted. The K00 result is a finite-jet
exclusion on one normalized support through grade eight; a finite jet is not a
formal arc, an algebraic germ, a polynomial map, or a counterexample, and a
reduced point-set statement is not a scheme statement. `U1*(R)` and the
`AUDIT` Lemma 3.1 family remain formal necessary-data configurations, not
maps; their collision with `KJN(1)` is a disjunction, not a verdict on either
side. `KJN`, `RPMC`, `PC`, `DIR`, `TDBOUND`, `PCB-EXCESS`, and every `EXCESS`
rung remain conjectural and are neither proved nor refuted here; `KJN(1)`
remains type-relative and is not an absolute ceiling. A lower floor is not
attainment, a floor fit is not a witness, and `REPRESENTATIVE` is not
`FULL_ACTUAL_EXIT`. Flags, physical places, and cover series are kept distinct
throughout; `B` and `S` remain route-separated. Where no safe replacement
exists I returned a typed `OPEN` or `UNDERDETERMINED` rather than filling the
gap by cap or analogy. No new exit price is derived or asserted, so no
charge-basis declaration appears in this report.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `57885`.
- Body SHA-256:
  `006fd2e67fecc8f545265c9dc834be739608d2c5b2cf68edf5f6c5d13bde2653`.
- Frozen basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa`.
