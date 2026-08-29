# Adversarial cross-pollination — Fable 5 — round `20260829T1808Z`

Identity: Fable 5, cross-poll synthesis-input lane  
Frozen basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa` (matches `git rev-parse HEAD`)  
Lifecycle: `CROSSPOLL_ADVERSARIAL_INPUT / NO_PROMOTION / FAIL_CLOSED`

## 0. Custody and boundary

Every charged file was rehashed this session and matches its charge. Full-file
SHA-256, with body seals (bytes/SHA through the unique standalone `BODY-END`
line) verified for every sealed document both by inline hashing and by the
under-review `ops/seal.py verify` (results identical):

```text
f7a0b2a7e6a34cb8b8ae926adf95d36db46b0dc37e6aa75a17be3dcd7ce5fea2
  xmodel/ideation-20260829T1808Z-crosspoll-packet.md   body 11344/0703f1f3...
f58ee9b50d640860fa36f34f12f39bcbb0f8fb852e2ace90be8e62323e09ccfb
  xmodel/ideation-20260829T1808Z-state.md              body 9040/d48e33c5...
bfa137c567e366dca26c6d0bc4a8824912cbba03d74df2bee27264000bcfb0cb
  xmodel/ideation-20260829T1808Z-sol56.md              body 27206/190a5e10...
37d1942a2ba6585c6b7d977aa5d20fd994008dbdef250a05c0425b92ac29f6ee
  xmodel/ideation-20260829T1808Z-fable5.md             body 28151/1e530d1f...
2f65a96ff2ba2fc5d573b90c41aca57cfffb4efbe6c3bbdd2a3ea914079032cc
  xmodel/ideation-20260829T1808Z-opus5.md              body 47459/486b11c0...
190aae86c664627a8668dc219a49d8ffad7f09e4e90bc4559aa531e35288b6d5
  xmodel/ideation-20260829T1808Z-grok46.md             body 34560/9257ea3d...
2ebd1d78391a145c446d2113a1801e342118773c6fd9ce63be183dfd94f15a58
  xmodel/k00-r2-full-rank-fan-provisional-sol56-20260829.md  body 11680/c596347c...
2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4
  xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py
66f119e0e46b56f067802baa9118d0080370dc404878f9db667284c2d45d54a0
  xmodel/u1-ham-kum-conn-stop-audit-sol56-20260829.md  body 5520/ad2d79d8...
59add10d8b291bb85a32c8f8a155d7ff0a7c4d6dd646fc164f48304b34fd80c1  ops/seal.py
73f7e7bb554d3ba6936eb472539eebce3425eda619e8f118d1cf29f632a6ff49  ops/test_seal.py
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py
2fcf8b9d9d0f7a28c9425bf73d30ba893015c69074afef57d2425309826ace50
  xmodel/td12-u1-first-nonneutral-sextet-coordinator-integration-sol56-93d-20260829.md
4c2fd1de827361f06bcbfdd465e0cdb6f03c63203c9943f89af60b8aaaa7637d
  xmodel/u1-star-interface-no-go-coordinator-integration-sol56-93d-20260829.md
bff17fd8acb0f71fbf1ddc0b5f9d1ca30886222e03ea1f9309a92ac5cff707a0  AUDIT.md
2adfb3b6c25552654e3bc6fbac3b54e6d3ace56a861125cde201317455450c57  ladder/REDUCTION.md
ccf96a7e17c28ced128529bcadb87962d960672727cb3da10615333499560a98  ladder/TDBOUND.md
```

No web, AWS, commit, push, canonical edit, or `jc2-lean` access of any kind;
all repository searches used `rg` (ignore-respecting) or explicit paths. Desk
computation: one independent exact reconstruction, `/tmp/fable_xpoll_k00.py`
(scratch, not part of the round record), 2.4 s runtime, trivial memory, pure
stdlib `Fraction`; plus the `ops/test_seal.py` suite (0.4 s). Only this one
repository file is written. No new typed exit price is asserted anywhere, so
`charge_basis` is absent.

## 1. K00 valuation-two theorem: independent reconstruction

### 1.1 Method (not a rerun of Sol's replay)

I rebuilt the seven unloaded rows and three load-row families directly from
the frozen 569-tail JSON under the compiler-pinned affine map
(`C0=(1+d0)/256, C1=d1, C2=(1+d2)/16, C3=d3, C4=(3+d4)/8, C5=d5, C6=1`),
with my own sparse exact arithmetic and my own organization, sharing no code
with the replay. Differences that matter:

- **Structural gates computed, not assumed**: unloaded rows have zero
  constant and linear parts; K10 rows have min degree exactly 2 in all seven
  rows; K6 rows have zero constant part (so `k6` cannot enter before grade 9
  given `k6[0]=0`); K2 first possible grade is 11. These license the
  grade-by-grade bookkeeping that Sol's report asserts in prose.
- **All removable unknowns kept symbolic**: `k10[1]`, `k10[2]`, `k6[1]`,
  `k6[2]`, and the grade-six jet coefficient `d[6]` (six free components)
  ride through every old-plane computation as ring variables. Every claimed
  cancellation is then an assertion output, not an omitted-coefficient side
  identity. All cancel exactly.
- **Own cokernel bases**: I derived the rank-two grade-six cokernel myself
  (rows 4 and 6, whose `(alpha,beta)` vanish identically, plus the three
  null combos `R3+R1/8`, `R5+R1/128`, `R7+R1/1024`), and killed the
  `u^2=192v^2` branch through a *different* route than Sol: my combos reduce
  to `-2-6a`, `3/8+(3/4)a`, `(3/64)a` — pairwise incompatible linear
  equations — while Sol's `S5=1/8`, `S7=-1/64` constants are confirmed as
  exact linear combinations of mine.
- **Grade-7 forcing proved in the strong form**: on the old plane, grade
  seven equals `alpha_i(y)(A(z)-2st) + beta_i(y)(B(z)-(s^2-64t^2))`
  *identically in all variables*, so the rank-two forcing of `A(z),B(z)` and
  the rank-one one-parameter `lambda`-line are exact consequences of the
  rank of `M(y)`, not a substitute-and-check.
- **Ideal-membership closure of the one replay under-check** (§1.4).

### 1.2 All six cells confirmed

1. **Leading cone.** `Q1+8Q3=(3/2048)AB`, `Q4=(3/524288)(B^2-64A^2)` hold
   as polynomial identities, every `Q_i` vanishes under the 4-parameter
   solution `x=(2b+2u,a,b,8a+v,b-u,16a+4v)` of `A=B=0` (an exact bijective
   parametrization), so `V(Q)=V(A,B)` set-theoretically in characteristic
   zero — this also independently confirms Opus §5.1 (one 4-plane, no other
   components). Rowwise `DQ_i(x)[q]=alpha_i A(q)+beta_i B(q)` with exactly
   Sol's table; all four nonzero 2x2 minors are rational multiples of
   `Delta=u^2+64v^2`; `Q6` is identically zero.
2. **Leading rank one** (`u=+-8iv`, `v!=0`, existing only when `-64` is a
   square): row 6 is `u(192v^2-u^2)/65536 = +-(i/32)v^3`, kappa-free,
   `y,z`-free, a unit. Dead at grade six.
3. **Leading rank two** (`Delta!=0`): grade five forces `A(y)=B(y)=0`; the
   five cokernel conditions are kappa-free; branch `u=0` forces `b=0` then
   `v+3a=0` and `v+2a=0`; branch `u^2=192v^2` is killed by incompatible
   linear reductions (and Sol's constants replicate). Dead at grade six.
4. **Old-plane next rank two**: `A(z)=2st`, `B(z)=s^2-64t^2` forced;
   `R1+8R3=-(3/256)D`, `R4=-(3/32768)F` are free of every unknown;
   `sD-tF=-2uv(s^2+64t^2)`, `sF+64tD=(u^2-64v^2)(s^2+64t^2)`, and on
   `s=+-8it` one has `D=t(u-+8iv)^2`; `D=F=0` forces `Delta_y=0` on both
   branches. Dead at grade eight.
5. **Old-plane next rank zero** (`y=ell(a,b)` arbitrary, including 0):
   grade eight is exactly `(a,b)`-independent; the two combos force
   `W_A=W_B=0`; then `G8_1=(5kappa/4096)t(3s^2-64t^2)` and
   `G8_2=(5kappa/65536)s(s^2-192t^2)` **modulo the ideal `(W_A,W_B)`** (see
   §1.4), with no common zero for `kappa!=0`, `(s,t)!=(0,0)`. Dead at grade
   eight.
6. **Old-plane next rank one**, both conjugate branches run separately:
   grades 4–7 vanish identically along the whole `lambda`-line; the two
   grade-eight combos force `lambda=0`, `s=8i*sign*t`; then
   `R2+(i*sign/2)R1 = -(5i*sign/16) kappa t^3` exactly, in *all* remaining
   variables. `kappa!=0` forces `t=s=0`, contradiction. Dead at grade eight.

Controls: tails/compiler custody; a perturbed row-6 cubic tail coefficient
breaks cell 2; a wrong affine constant (`C4: 3->2`) breaks the boundary
gate; a wrong `B(z)` sign breaks grade seven; `kappa -> 0` erases the
rank-zero and rank-one kills (load-bearing). Coverage is complete: exact
valuation two forces `x` onto `V(A,B)\{0}` = (rank0 minus 0) ∪ rank1 ∪
rank2, and on the old plane grade six forces `y` onto the same cone, whose
three `y`-strata are cells 4–6.

### 1.3 Verdict, maximum theorem, consequence

**Verdict: `PASS_WITH_REPAIR`** — the *mathematics passes in full*; both
repairs are to the promotion package, not the statement.

**Maximum typed theorem.** On the exact normalized V20R2 source over any
field of characteristic zero (licensed opens `C6=1`,
`k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0`, `kappa=k10[0]!=0`; `Jdet[0]!=0`
licensed but unused through grade eight), there is no field-valued
compatible jet of exact valuation two through grade eight; hence no
same-source formal arc of valuation two. Composed with the promoted
valuation-one kill and the valuation-`>=6` impossibility, **precisely
valuations 3, 4, 5 remain possible on this support, none attained.** Not a
formal arc theorem elsewhere, not a germ, polynomial map, other support or
normalization, scheme-structure claim, counterexample, or JC2 result.
Promotion recommended with the two repairs folded.

### 1.4 The two repairs, and the replay inspection

**R1 (replay control).** For cell 5, the replay checks the terminal rows via
`zero_vars(..., ("WA","WB","w1","w2","w3","w4"))`, which *drops* every
monomial containing a free component `w1..w4` without proving none exists.
If `G8_1` had contained a `w_j`-monomial free of `W_A,W_B`, the replay would
still print PASS while the displayed kill would be unsound (a `w`-dependent
row is a solvable constraint, not an obstruction). I checked the needed
statement directly: `G8_1 - expected` and `G8_2 - expected` lie in the ideal
`(W_A,W_B)` — **they do**, so the theorem is sound and the replay merely
under-verifies. Repair: replace that control with the membership check
before promotion custody. (Cells 3, 4, 6 have no analogous gap: their
`zero_vars`/`replace` uses are genuine substitutions of forced values, and
their terminal assertions are full-polynomial equalities.)

**R2 (load-calendar scope note; corrects three of the four blind reports).**
Computed fact: all seven K10 rows have min degree 2; the quadratic part `M4`
does **not** vanish on the leading cone (rows 1, 2, 3, 5, 7 survive; rows 4
and 6 vanish there), and on `Delta!=0` the vector `M4(x)` lies in the image
of `DQ(x)` (all five cokernel functionals annihilate it). Consequences: in
the seven-row jet system, `kappa` arrives at grade `2v+2` for *every*
valuation `v` — absorbable on the rank-two stratum, identically absent on
the old plane (`M4(ell)=0`), and killed in rows 4/6 — while the promoted
min-degree table `(D10,D6,D2,u2,u4,u6,-h/4)=(3,2,2,1,1,1,0)` belongs to the
*contracted grade-19 target row* (`DK10 = h*aK10_7 - sum u_i aK10_i`), a
different object. Hence: Grok's `K00-V25-FIRST-LOAD-CALENDAR` claim of a
"load-free window, grades 7–10" at `v=3` is **wrong at grade 8** (and at
9–10 via polars once `y,z` leave the cone); Opus's §5.3 first-arrival column
`2+3v` is correct only for the contracted row (its `v=5`-cheapest *ordering*
survives at that tier); my own blind `LEADING-CONE-UNIVERSALITY` stated the
right conclusion (grade-`2v` equations are exactly `Q(x)=0` for every `v`,
because `2+2v > 2v`) with the wrong arrival formula and a spurious `v=2`
caveat. Sol's `JETFAN` template — `kappa M4(x)` at grade `2r+2`, `C3(x)`
only at `3r` — is the **only** correctly scheduled version and should be the
one implemented, plus the `M4`-absorbability fact above (after eliminating
`z`, `kappa` cascades into later-grade inhomogeneities; the fan is not
kappa-free below the contracted row).

Replay inspection, other notes: marker semantics (`splitlines`-free body
convention) fine; the custody, weight, and load-linearity gates replicate
mine; the mutation controls are meaningful (the row-6 mutation key search
guarantees non-vacuity); runtime class as reported. With R1 folded the
replay is promotion-grade.

## 2. Global-selector audit (Opus OP-1 … OP-6)

- **OP-1** (`Delta_P = Lambda_P`): **KNOWN-EQUIVALENT, verified.** I
  re-derived the local Bezout computation independently (generic `nu`
  splits `i_p = e*m_p + ord_p(g-nu)`; `sum m_p = alpha*mu_P` from
  `F_d=xi H^alpha`); it also follows from the promoted `EXACT POLAR BRIDGE`
  plus `a_gamma = -ord_gamma(omega) - 1` already in AUDIT. Signs,
  multiplicities, and the global sum `sum Delta_P = td` all check. Smallest
  retained theorem: the identification of the capacity-lane defect with the
  Sigray pole decoration, i.e. the two coordinate systems are one problem.
- **OP-2** (`RPMC(C) <=> a_P b_P/nu_P <= C mu_P/B`): **KNOWN-EQUIVALENT**
  (downgrade from Opus's "NEW per-point form"): AUDIT's RPMC is *already*
  per-root (`E_i <= C mu_i/B`); TDBOUND §1 already records
  `Lambda = alpha*beta*a*b/nu`. What is new is only the packaging in entry
  decorations. The rewriting is an *equivalence* of the existing per-point
  lane (not merely sufficient), modulo the promoted generic-`(lambda,nu)`
  hypotheses. `mu_P/B` is genuinely absent from the reduced interface:
  REDUCTION.md's entry datum is `e_i=(Lambda_i,a_i,b_i,nu_i)` with type and
  pole count — no `mu`, no `B`. Confirmed.
- **OP-3** (interface = `(mu,B)`-forgetting quotient; disjunction "RPMC(1)
  false or no `U1*(R)` occurs"): **NEW (diagnosis), verified.** Arithmetic:
  `E_MR = 2R/3 >= 2` for odd `R>=3` against `RPMC(1) => E_MR <= 1`; AUDIT
  Lemma 3.1 is indeed the first instance of the same phenomenon. One
  structural addition of mine: the claimed `RPMC(1)` *equality* at
  residue-A is forced by the symmetric two-pole split alone
  (`mu_P/B = 1/2` gives `alpha*beta*mu/B = 3 = Lambda_P` for type (2,3),
  `Lambda=3`), so the tightness evidence does not depend on the
  unverified `B=84`; it does depend on `mu_1=mu_2`, which SCALE-AUDIT
  should confirm from the filed leading form. Smallest retained theorem:
  the disjunction, stated exactly as Opus stated it.
- **OP-4** (nonproperness defect ledger): **NEW-form over KNOWN pieces,
  verified.** Riemann–Hurwitz with poles ramified to order `lambda_p` gives
  `sum_nonpole e_p = 2G-2+td+s+n`; `delta`-sum equals the same; `c=1`
  because `J=1` forces `f` primitive (a composite `f=h(u)`, `deg h>=2`,
  would have critical points at `u = root of h'`), so the generic fibre is
  irreducible. `Delta >= td` with the stated equality case; `n>=1` for a
  counterexample. Retain as stated.
- **OP-5** (exact inertia cycle type): **NEW; PASS_WITH_REPAIR.** The
  *local* cycle type at one value `c` — `(e_p : g(p)=c) + 1^{td-delta}` —
  is correct (affine sheets fixed; each non-pole boundary place contributes
  one `e_p`-cycle; transitivity from connectedness; `G_lambda` primitive
  implies `G` primitive since `G`-blocks restrict to `G_lambda`-blocks).
  The *global determined passport* needs one more datum the claim glosses:
  the partition of non-pole places by shared boundary value — equivalently
  the component structure of `A(F)` over the `lambda`-line with
  `deg(f|_{S_i})` — which is global, not per-place. The books' contact
  tables give the `e_p`; the partition must be computed or bounded
  separately (Opus's own `sum delta_i deg(f|S_i) = Delta` is the start).
  With that repair, stage 1 is exact and cheap. Avenue raises: **7 and 25
  small raise justified at stage-1 scope; 26 reopen only if the descent
  seam (below) gains a gate — no raise yet.**
- **OP-6** (free td-minimal selection in the pure-Sigray branch): **NEW as
  spine statement; licensed.** REDUCTION T4 normalizes an *arbitrary*
  nonautomorphic pair after lex-minimizing its own Aut-orbit, preserving
  `td`; selecting a minimal-`td` counterexample first is well-ordering.
  Verified trade: the GGV/T3 polygon datum is forked away, and the branch
  rests on Sigray Lemma 2.1's external Abhyankar inputs (Thms 18.13/19.2)
  plus the unaudited §§7–9 layer — the G5/HIGH-3 debt, exactly as Opus
  says. One small *unchecked* step I add: the `td>=6` and fixed-`td`
  entry-menu arrows must be confirmed to consume only the Sigray normal
  form and not the GGV selection; this looks routine but is not yet
  written. The block-quotient-to-smaller-Keller-map seam remains **OPEN**
  and must stay explicit; stage 2 gets no launch until stage 1 lands.

## 3. Other proof-side proposals

- **Fable `EXCESS-e` (self-attack).** The consequence arithmetic replays
  against the printed records: one-step cells have `floor=3R-1`,
  `budget=4R-k-2`, `slack=R-k-1` (no-go integration §1), so `EXCESS-1`
  kills exactly `k>=2` cells (S17) and `EXCESS-2` kills all `k>=1`; the
  D13/E11 zero-slack witnesses (floor 10 = ceiling 10) die under
  `EXCESS-1` in the full-exit regime. But the table stands on **two**
  unproved identifications, not one: (i) the printed `td-1`-rooted budgets
  must be the same ledger as the Section-7 `I_i` (my blind rider), and
  (ii) **new this session**: cross-value additivity — weight at an
  atypical value must decrement the capacity available at a typical value
  *within the same quotient line* `I_i`; without (ii), `WEIGHT-AT-ATYPICAL`
  proves nothing about typical fibres. Classification: **PROVISIONAL**,
  consequence table remains gated behind the budget-semantics note; no
  lane may consume it. The "PCB kills the U1 sector" fragment is
  qualitatively DUPLICATE of the integration; the graded ladder and
  per-cell arithmetic are the additions.
- **Fable `ATYPICAL-EXISTENCE`.** The existence half is sound in shape and
  I verified each step (primitivity; no atypical value ⟹ locally trivial
  ⟹ `chi(fibre)=1` ⟹ genus 0, one place ⟹ Abhyankar–Moh ⟹ coordinate ⟹
  `g=y+c(x)` contradiction); it needs its external inputs pinned to exact
  published statements. The bridge to `EXCESS-1` stops at **two** missing
  lemmas (weight-at-atypical ≥ 1, and additivity (ii) above). **Typed
  OPEN at the bridge; do not launch as a lane.**
- **Fable `AM2-PLACE-LEDGER`.** Against the packet's question: applied per
  actual component of `A(F)` *before* a boundary contact table is known,
  AM-2 is **UNDERDETERMINED** on the sextet witnesses — the reduced rows do
  not pin the contact data the identity consumes; the underdetermined
  output is still the typed input schema for `DETOUR-EXCLUSION/v2`, which
  is real but conditional value. Not duplicative of `SCALE-PIN` (per-place
  valuation identity vs per-root scale mass), but the *diagnosis*
  converges: both name actual-source scale/place data invisible to the
  reduced interface. **Defer behind SCALE-AUDIT**; the symmetric `U1*(R)`
  instance may close enough to run later as a refinement.
- **Sol `TD12-SEXTET-INDUCED-CHAR`.** KNOWN character machinery, NEW
  client (Sol's own honest labels). It is a necessary-condition census
  with no typed occurrence map, the ORB-FUSE precedent shows one prior
  character kill refuted, and Opus's repricing (the whole laboratory sits
  at one entry with `E_MR=2` against `RPMC(1)`) is correct: T2 dominates
  T1. **Defer to background; not a launch slot.** If run at all, share one
  source packet with Grok's Card-2 tightness cut (same Statement-3.9
  transport input).
- **Grok actual-automorphism Section-7 control.** At `td=1` the promoted
  ledger gives `td-1=0=sum I_i`, so all `I_i=0`, weights 0, `s(a)-1=0`:
  the objects either fail to exist under the normalization frame (T4
  requires nonautomorphic) or exist vacuously with excess `0>=0`. Either
  outcome only types the `td>=6`/nonautomorphic hypothesis every reader
  already expects `PCB-EXCESS` to carry. Sound, cheap, **low information;
  optional rider, not a slot.** Grok's calendar: see R2 — partially
  refuted; correct before any reuse. Grok's Card-3 replay half is
  superseded by Sol's executed fan plus this review (convergence
  preserved: Grok specified the same reconstruction and controls).
- **U1 Hamiltonian–Kummer STOP audit: recheck CONFIRMS the stop.** I
  verified the conditional identity `DT=(1/r)(A'/A)T` and the character
  form; the reviewed U1 datum is fixed-fibre (`t^r - A_*`, `A_*` constant,
  `dA_*=0` ⟹ trivial connection) so the instantiation is a
  formal-data-to-map scope jump; the displayed form is twisted-exact
  (`omega_j e_j = nabla_j e_j`) hence not an obstruction class; the `G_m`
  control (`n+j/r` never 0) and the puncture control (attachable to the
  identity map) are correct; counting `r-1` characters as `s-1` events
  would violate the flag/place/series firewall. None of the four reopen
  objects is supplied by anything in this round. **STOP stands; the blind
  Avenue-16 raise is not consumed.**

## 4. Deduplicated claim table

| claim | owner(s) | class | verdict / smallest retained theorem |
|---|---|---|---|
| K00 v=2 full rank fan | Sol (exec); Fable A / Grok 3 / state packet (spec) | NEW exact exclusion | **PASS_WITH_REPAIR** (§1.3–1.4); retain Sol §0 statement + R1/R2; leaves exactly v∈{3,4,5} |
| v=2 leading cone is the 4-plane `V(A,B)` | Opus §5.1 | NEW scope stmt | CONFIRMED (identities verified); old-plane-restriction worry resolved by the full fan |
| k10 first-arrival calendar | Opus §5.3 / Grok §3.1 / Fable §6 | — | contracted-row column correct (Opus ordering `v=5` cheapest survives); seven-row-system versions REFUTED/REPAIRED per R2; Sol JETFAN schedule correct |
| `Delta_P=Lambda_P` | Opus OP-1 | KNOWN-EQUIVALENT | verified; retain the two-coordinate identification |
| per-point `RPMC` in tree coords | Opus OP-2 | KNOWN-EQUIVALENT (novelty downgraded) | equivalence verified; `mu,B` absent from entry datum confirmed |
| `(mu,B)`-forgetting diagnosis + disjunction | Opus OP-3 | NEW | verified; retain disjunction verbatim; residue-A tightness is symmetry-forced |
| defect ledger | Opus OP-4 | NEW form | verified incl. `c=1`; retain |
| inertia cycle type / determined passport | Opus OP-5 | NEW | PASS_WITH_REPAIR: local type exact; passport needs the place-value partition (`A(F)` components) |
| free td-minimal selection | Opus OP-6 | NEW spine | licensed by T4; G5 debt; seam stays OPEN; one routine arrow-scope check owed |
| `EXCESS-e` ladder | Fable | PROVISIONAL | arithmetic replays; gated on budget-semantics + new additivity gap (ii) |
| `ATYPICAL-EXISTENCE` | Fable | PROVISIONAL/OPEN | existence half sound-shaped; bridge = two missing lemmas |
| `AM2-PLACE-LEDGER` | Fable | PROVISIONAL | UNDERDETERMINED pre-contact-table; defer behind SCALE-AUDIT |
| sextet induced character | Sol | KNOWN mech / NEW client | defer (T2 dominates T1; ORB-FUSE precedent) |
| detour full-exit tightness | Grok 2 | NEW attack on KNOWN numbers | defer with td12 lab; share source packet with char census |
| automorphism Section-7 control | Grok 1 | NEW experiment | sound, low information (vacuous at td=1); optional rider |
| U1-HAM-KUM composition | Sol (blind) | DUPLICATE/SCOPE-CONFLICT | STOP confirmed; four-object reopen gate retained |
| body-seal validation | Fable §8 + Grok §7 + Sol INGESTCHECK | convergent (3x independent) | realized as `ops/seal.py`; adopted as the systems trial (§6) |

Independent convergences preserved: (1) three separate seal-validator
proposals; (2) three specifications of the same K00 reconstruction, executed
once, reviewed here; (3) two independent "missing selector datum is
actual-source scale/place data" diagnoses (Opus `mu_P/B`, Fable AM-2); (4)
two independent named conjectures each of which would empty the `U1*(R)`
sector (`RPMC(1)` scale-side, PCB/`EXCESS` budget-side) — keep both, merge
neither; (5) three of four blind reports made the same calendar error from
the same contracted-row table — now corrected by computation.

## 5. Portfolio: three mathematical launches + one systems trial

1. **`K00-R345-JETFAN` with v=5 first** (falsification lane). Promote the
   v=2 theorem with R1/R2; implement Sol's JETFAN schedule (the only correct
   one), with the R2 absorbability fact built in; run `r=5`, then 4, then 3.
   Ownership: implementation by Opus or Grok (non-author), hostile review by
   a model that has not touched the fan (Grok if Opus implements). Desk
   exact; AWS only by preregistration if a surviving stratum must be pushed
   to grade 19. Outcomes: all dead ⟹ V20R2 support empty (major
   falsification result); survivor ⟹ frozen jet + preregistered extension.
   Stop: first exact nonzero cokernel witness per stratum; no shift-period
   inference; no local CAS.
2. **`SCALE-AUDIT/v1`** (proof lane / selector). Opus's §6 exact integer
   feasibility pass over the filed corpus + `U1*(R)` + controls, with
   riders: sextet counts as ONE sample; free consistency gate
   `Lambda_i =? alpha*beta*a_i*b_i/nu_i` first; verify `mu_1=mu_2` at
   residue-A (the tightness hinge). Ownership: Opus produces, Fable
   reviews. Desk. Outcomes: data defects (cheap wins), an unconditional
   `NO_ADMISSIBLE_SCALE` kill, or the typed
   `ADMISSIBLE_WITH_RPMC1_VIOLATION` conversion of the td12 entry into
   "exactly one named conjecture decides". Feeds the `RPMC(1)`/`SCALE-PIN`
   proof target, which is the round's best-named global crux. Stop: first
   unconditional kill or first independent `E_MR<=1` kill (would retire the
   ceiling lane).
3. **`INERTIA-EXACT` stage 1 with the partition repair** (bypass lane).
   Prove the local cycle-type theorem at the stated scope and run the
   residue-A determined-passport computation, computing the place-value
   partition from the filed contact data rather than assuming it.
   Ownership: Opus produces (its OP-5), Grok reviews. Desk. Outcomes:
   determined passport ⊊ 169 admissible ⟹ kill power exists, raise
   Avenues 7/25; equals-all ⟹ stage-1 exact but value moves entirely to
   the (unlaunched) stage-2 descent seam. Stop: do not open stage 2 (the
   block-quotient seam) this checkpoint.

**Systems trial (exactly one): adopt `ops/seal.py`.** Acceptance evidence
recorded this session: 6/6 fixture tests pass; live `verify` on ten sealed
round artifacts PASSes with bytes/hashes byte-identical to my independent
computation; inline/backticked marker mentions are correctly ignored; a
standalone marker inside a code fence fails closed ("found 2" — stricter
than Grok's first-marker contract, and safer; document the writing rule
"never put the marker on its own line inside a fence"); symlinks,
non-regular files, and non-UTF-8 post-body bytes are refused; stamping is
atomic (same-directory temp + `os.replace` + dir fsync), re-stamp refused,
mode preserved; residual TOCTOU window between the last `lstat` and
`os.replace` is inherent without `renameat2` and acceptable for this
threat model. It answers the recurring malformed-seal class all three of us
independently flagged. `INGESTCHECK` (superset) and lane-wiring (Grok's
`verify_body_seal` hook) are deferred to the 2026-08-31 checkpoint —
`ops/lane.sh` is frozen while lanes are active. `FENCE-DEFAULT/v1`
adjudication: Opus's wrapper+check is necessary but "helps only when used";
the smallest *enforceable* default is a deny-by-default guard on bare
recursive POSIX searches from the repository root (session hook or shell
profile function wrapping `grep -r`/`find` with `--exclude-dir=jc2-lean`,
with explicit-path invocations untouched), with `ops/rgrep` and
`fence_check.sh` as the audit layer; schedule it for the checkpoint, not
now.

## 6. Stop / defer list

**Stopped (do not launch or consume):** `U1-HAM-KUM-CONN` (audit
confirmed); PCB or any `EXCESS` rung as a premise; the grade-seven K00
Fitting packet; `j=42`; S `j=13`; quartet descendants; any valuation-one
K00 client; the empirical TDBOUND lane (close it, per Opus — the round-2
COINCIDENCE-RISK already downgraded it); Grok's v=3 "load-free window
7–10" claim (correct per R2 before any reuse); my `EXCESS`
consequence table as an input to any lane (gated); K00 AWS work (nothing
currently justifies it); all `jc2-lean` access.

**Deferred:** td12 laboratory as a whole (sextet char census + Grok Card 2
+ AM-2 witnesses) behind SCALE-AUDIT's typing of its entry; `EXCESS`/
`ATYPICAL` until the budget-semantics note (with the new additivity gap)
is written and different-model reviewed; OP-6 stage-2 block descent until
stage 1 lands; INGESTCHECK and FENCE-DEFAULT to the systems checkpoint.

## 7. Synthesis recommendation (under 250 words)

Promote the K00 valuation-two rank-fan theorem with two repairs: strengthen
the replay's rank-zero terminal-row control to the `(W_A,W_B)`-membership
check, and attach the load-calendar scope note (K10 quadratic part is
nonzero on the cone; the min-degree table governs only the contracted
grade-19 row). That leaves valuations 3, 4, 5 on V20R2, none attained, and
arms Sol's JETFAN — the only correctly scheduled template — for `r=5`
first. Launch three lanes: JETFAN (falsification), SCALE-AUDIT
(proof/selector — it converts the td12 entry into "one named conjecture,
`RPMC(1)`, decides", and it is the cheapest test of the round's best
selector idea), and INERTIA-EXACT stage 1 with the place-value-partition
repair (bypass — the only architecture needing neither ceiling nor type
menu). Keep the td12 laboratory, character census, tightness cuts, and my
own EXCESS/ATYPICAL program deferred: each is either downstream of an entry
that `RPMC(1)` would make vacuous or gated on an unreviewed semantic
identification. Confirm the U1 Hamiltonian–Kummer stop. Adopt `ops/seal.py`
as the single systems trial; it just live-verified ten round artifacts
byte-for-byte against independent hashing. The deepest cross-poll lesson:
three of four blind reports propagated the same wrong load calendar from
one promoted table applied outside its object — desk-checkable in minutes,
and exactly the class of error the mandatory-reconstruction discipline
exists to catch. Keep that discipline.

## 8. Nonclaims

Nothing here asserts an occurrence, attainment, `PairRef`, source value,
degree or type ceiling, formal arc beyond the stated same-source scope,
algebraization, polynomial Keller map, counterexample, or JC2 conclusion.
`RPMC(1)`, `PC(1)`, `DIR(1)`, PCB, and every `EXCESS` rung remain
conjectural. Floors are floors; reduced equality is not scheme equality; B
and S stay separate; flags, places, and series stay distinct. All six K00
cells were re-proved from the frozen tails, not trusted. No exit price is
asserted; `charge_basis` is intentionally absent.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `30232`.
- Body SHA-256:
  `a0c7f687d2c77004ca5a8f521e8b152ebff4ea30842c525cd60c3bfcdb9c0ca3`.
- Frozen basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa`.
