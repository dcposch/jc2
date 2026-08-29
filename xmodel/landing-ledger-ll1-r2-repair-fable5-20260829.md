# LANDING-LEDGER LL-1 R2 — corrected `td=6, m=2` packet: family-I identification, D9 discharge, inverted acceptance tests

Date: 2026-08-29 (UTC). Lane: Fable 5, producer.
Charge: repair the sealed LL-1 design at its first exact discriminator and
implement the corrected `td=6, m=2` packet. The hostile review is treated as
an independent mathematical correction; the old Section 5.4 is not defended.

Status: **SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW.** No AWS launch and no
canonical promotion are authorized by this report.

## 0. Inputs (read in full; hashes computed this session)

- `xmodel/landing-ledger-primary-research-fable5-20260829.md` — full
  `26bdd150a5a4bace23069b65f3234de6080fc7fb083f46a92773ec276a6fc689`, body
  `83fe23123f35275e551ef8d1704da1181dea9c346a4915cd0e15c6db82998700`
  (both match the pins).
- `xmodel/landing-ledger-primary-research-fable5-hostile-review-grok46-20260829.md`
  — full `62d8f55ee6a34ccd960121e9e64498fbb3ee3a92a8a4681fec4290fc9c7bc5da`,
  body `88c1d66f09314e8717234b8617da84cd78a7fe95da90b31a120721272d678e79`
  (both match).
- Campaign sources cited by those two reports for the LL-1 laws, resolved to
  repository paths and read in full (`jc2-lean` untouched):
  `ladder/SHEET6-MULTIPOLE.md`
  (`93adb7acedf4cf0fd56ffc68e4571649a04eab12e1271431449a79465a964bcb`),
  `ladder/BOOK-OFFAXIS.md`
  (`34f5ea9db62caf1da8b436733752e86402ff3f3ee08bc5096f13f8bf0c80eb17`),
  `ladder/SHEET6-DEPTH.md`
  (`ad9ced6c0420902f8cf63edf3636bed8633be511e925f208d24a24c35d71036d`),
  `ladder/REDUCTION.md`
  (`6b9376e0f479545f012cd7451bd3eb1a9271fc312b9996c5848c5db159ebdb31`).

No web, AWS, Singular/msolve/Sage/PARI, no `git status`, no commit/push, no
canonical edit. All computation is bounded exact-rational Python inside the
fresh packet directory.

## 1. Deliverables

- Packet: `cases/landing_ledger_ll1_r2_20260829/`
  (`ll1_compiler.py`, `ll1_validator.py`, `test_ll1_r2.py`, `INVENTORY.md`,
  `MANIFEST.sha256`, `out/ll1_book.json`, `out/ll1_summary.json`).
- This report.

Packet manifest (verified with `shasum -a 256 -c`, all OK):

    882553136eb1bc06b87c1ef7177b13faa5d0104f10e26e1df8c808dc672e0710  ll1_compiler.py
    fd3170cbad68b3f7058065161dd1889ef5375103fc45351a6943f56e661e3fc9  ll1_validator.py
    3003a6bfd5731b6a921e9be17c0ce2026adb8a523eecd19065eddb9853313489  test_ll1_r2.py
    43a9e88dbc9b45c629579d2088755a55059050f4f2709523f68365cd7a3cc932  INVENTORY.md
    cb490d4e5db3db9ba7ac87320cdc11452cd5fa8c82efb55a8499b260d62154ce  out/ll1_book.json
    9fa89c424af89c78b3277f87c05b993f1af35983c7772e578a16f853780366e9  out/ll1_summary.json

## 2. The mathematical repair (adopted, not contested)

### 2.1 `nu=1` quotient (mandate 1)

At `nu=1` the packet no longer treats `eps_q` as an independent contribution
to `dq`. `normalize_nu1_merge` identifies every legacy `(l, eps_q)` record
with MP6 family I **before** classification:

> **One-line degree identification** (MP6(c): the eta-factor is absorbed at
> `nu=1`). The legacy `(l, eps_q=1)` record has `q = eta * p * s~`,
> `deg s~ = l`, i.e. `q = p s` with `s = eta * s~`: it IS family I at
> extra-count `L = l+1` with `s(0)=0`; `(dp,dq) = (2, 2+L) = (2, 3+l)`.
> Whether `q(0)=0` is a root-location predicate on the extras, not a degree
> increment.

The location flag `q0_zero` is retained as provenance and never consumed by
classification. At `nu>=2` the eta slot stays forced (R1.0: `eta || q`,
`dq = 1 (mod nu)`), and the packet checks `dq = 1 (mod nu)` on every emitted
`nu>=2` cell.

### 2.2 Family-I split replacing Section 5.4 and the machine-only row (mandate 2)

The old `UNCOVERED` row and the `l in {1,3}` machine-only row are replaced by
one exact line, entirely inside the licensed source (MULTIPOLE D9):

- **odd `L`**: `M = gcd(2, L) = 1`, killed at the interior trunk by MP2.
- **even `L`, every `L`, including `s(0)=0`**: identity (iv) reduces to
  `2 p s' - L p' s = c' != 0` with `rho = 2/(2+L)`; dividing by
  `p^{(L+2)/2}` gives `(s p^{-L/2})' = (c'/2) p^{-(L+2)/2}`, whose residue at
  each p-root is `C(-n, n-1)(a1-a2)^{1-2n}`, `n = (L+2)/2`, with
  `C(-n,n-1) = (-1)^{n-1} C(2n-2, n-1) != 0` for all `n >= 2`. The left side
  is an exact derivative (zero residues), so `c' = 0`, contradicting
  `theta != 0`. D9 never uses `s(0) != 0`: the residues sit at the two
  p-roots, not at 0. td-uniform.
- `L = 0`: `q = p` forces `deg p = 1` — impossible (MP7).

Machine verification (exact, in-packet): for `L = 2, 4, 6, 8` at two root
pairs, the linear system `2ps' - Lp's = 1` is **inconsistent** over
polynomial `s` (any degree up to `L+2`), the `s(0)=0` subcase equally, and
the `c=0` kernel is exactly `span{p^{L/2}}`; the residue closed form and the
binomials `2, 6, 20, 70, 252` (`n = 2..6`) are recomputed exactly. Positive
control: `L = 1` is solvable with the printed closed form
`s = t - (a1+a2)/2`, `c' = -(a1-a2)^2/2`. The old l1_ode_check B/B-eta kills
are now the `L = 2, 4` instances of D9 — negative controls, not a finite
certificate.

**No td-7 zero-chain extension is invoked or queued.** The sealed
"candidate closing lemma" (BOOK-OFFAXIS §11 extension) is retracted per the
review: `kbar = 2 + 4/(l+1)` lies in `{3,4}` only at `l in {1,3}`, so the
§11 equivalence package does not govern these cells; `dp | dq` here is
exactly integrality of the integrating-factor exponent `dq/dp = (L+2)/2`,
which is D9's own mechanism. The review's quarantine list 6.2 is adopted
wholesale.

### 2.3 Coherence repairs (mandates 3-4 support)

- `M` is derived as `gcd(dp, dq)` of the **child shape** at every vertex
  (Prop 8.1(v)); the clean-axis R1/R2 gcd lines are never cached. The
  mutation battery pins the (A)-cell counterexample: cached
  `gcd(l nu, nu+1) = 2` vs true `gcd(21,15) = 3`.
- One coherent `w_cert` token set: `{W-CLOSED-FORM, W-PRICED-COMPLETE,
  W-SYMBOLIC}`; root-window kills fire only on the first two; `W-SYMBOLIC`
  never kills. The admitted IIa merge child is stamped **`W-CLOSED-FORM`**
  (DS4 handshake of two `W-CLOSED-FORM` arrivals against a determined cell);
  `W-PRICED-COMPLETE` marks only P0-priced suffix children.

## 3. The corrected hand-run (compiled, validated)

Header: `Lambda=(3,3)`, type `(2,3)`, `b=1` forced (MP4, `Lambda=3` prime),
unique entry `(a,b,nu)=(1,1,2)` at both poles, `kbar=5`,
`(M,rho,w0)=(1,1,2)`; off-axis empty (MP4 + BOOK-OFFAXIS §4). `W(2)={2}`;
chains are the parametric family `(w,nu,kbar)=(2,nu,2nu+2)`, `mu=(1,1)`,
`lam=0`; depth unbounded (DS1 R1). Family-level parity with the recorded
26-shape / 351-route figures is asserted at the frame-formula level; the
engine instances are cited (DEPTH §6-§7), not re-run.

Merge partition (single merge, MP1) — eleven records, complete, no default:

| candidate class | verdict | certificate |
|---|---|---|
| root meet, `l>=1` parametric | DEAD | case-I mixed-root window `0<w<1` vs certified `w=2`; root `M=1` itself LEGAL (local `r=2,l=1`: `w=1/3`, `M_root=1`) |
| root meet, `l=0` | REJECTED | `0 = theta*p` impossible (MP7/D9 root clause) |
| ZCH, either pole at 0 (2 records) | REJECTED | case-III join `w_other = nu_e * w_0`, `nu_e>=2`; `2 = 2 nu_e` impossible (DEPTH 5c) |
| IIa, `l*nu` even | DEAD | `M = gcd(2, l nu + 1) = 1`, MP2 |
| IIa, `l,nu` odd, `!=(3,1)` | REJECTED | `kbar = 2 + 4nu/(l nu+1) not in Z`; uniqueness `d | 4` |
| **IIa `(2,3,1)`** | **ADMITTED** | unique cell: `(dp,dq)=(6,10)`, `kbar=5`, `X=3`, `M=2`, child `Q=(6,12,3,2,5)` at `i=2`, `w_trunk=3/2`, `W-CLOSED-FORM` |
| family I, odd `L` | DEAD | `M=1`, MP2 |
| family I, even `L` (incl. `s(0)=0`) | DEAD | D9 log-obstruction, all even `L` |
| family I, `L=0` | REJECTED | MP7 |
| mixed all-`mu>=2` | UNREACHABLE | `mu_e | M = 1` (St 8.4 + MP5); the general mixed emission menu stays OPEN elsewhere and is not decided here |

**`UNCOVERED` list of the real book: EMPTY** — and under the corrected A2
that is a pass, not a failure.

First P0 successor from `(3/2, 2)` (menu completeness cited to BOOK-OFFAXIS
§10 P0; the packet's bounded Diophantine sweep reproduces it exactly and
finds nothing else within the whole `lam <= 4` budget):

| step | result |
|---|---|
| neutral thick `l=2`, `nu` odd | `w=3/2` fixed, `M=2` (parametric) |
| neutral thick `l=2`, `nu` even | `M=1` -> DEAD (MP2/R6) |
| thin `l=1` | `M=1` -> DEAD |
| clean resonant | REJECTED (`Delta=3` forces `dq=5`; `kbar=5/2 not in Z`) |
| dirty (A) `(21,15)`, `nu=7` | `-> (2/3,3)`, `lam=2` |
| dirty (C) `(20,16)`, `nu=5` | `-> (3/4,4)`, `lam=2` |
| dirty eps `(7,5)`, `nu=2` | `M=1` -> DEAD, `lam=3` moot |
| pure-(b) doubling | `w->3`, `M=1` -> DEAD, `lam>=3` |

Boundary terminals (P1 + St 9.4): from `(2/3,3)`: `j=1`, `psi=2`, budget
`3 >= 2` -> **ALIVE, slack 1**; from `(3/4,4)`: `j=1`, `psi=3`, budget
`2 = 2` -> **ALIVE_FRAGILE** (equality). Direct terminal from `w=3/2`
rejected (`w>=1`); `(3/4,2)` rejected (`j=1/2 not in N*`).

### 3.1 Finding: the exact sub-boundary residue is larger than both reports' parentheticals

The sealed body expected "at most one further priced unit" from the slack-1
route and the review's parenthetical added "none from the equality route".
The exact budget-exhaustion enumeration (licensed P0 pricing + P1 terminals
+ St 9.4, `Sum lam <= td-2 = 4` since `psi >= 1`) shows both parentheticals
are too small — e.g. the priced `lam=1` cells `(35,15)@nu7` from `(2/3,3)`
(the same St 9.6-family `l=3` cell BOOK-OFFAXIS P4 uses at td=7) and
`(119,35)@nu17` from `(3/4,4)` open `psi=1` terminals at `w<=1/2`. The
complete derived residue book:

- **2 deeper slack-1 ALIVE terminals**: `(2/5,5)` at `Sum lam=3`
  (route (A) -> `(35,15)`), `(2/7,7)` at `Sum lam=3`
  (route (C) -> `(119,35)`), both `j in {3,5}`, `psi=1`, budget 4.
- **9 equality ALIVE_FRAGILE terminals at `Sum lam=4`**: `(1/2,2)`,
  `(1/2,4)`, `(2/5,5)`, `(2/7,7)`, `(2/9,9)`, `(2/11,11)`, `(2/13,13)`,
  `(3/8,8)`, `(3/10,10)` — every one at `psi=1`, exact St 9.4 equality, so
  any new printed unit kills it.
- **9 route-dead states** (no in-budget admissible terminal reachable;
  marked by an explicit fixpoint, never left implicit), including
  `(2/3,3)@lam4` (budget overrun), `(3/4,2)` (`j not in N*`), and the
  `w=1`/`w=3/2` pure-b landings.

Every ALIVE row is a conservative superset (realizability untracked). Every
step cell was re-verified by hand during production (shape, strict NE laws,
root-mult law, `kbar in Z`, AF2 price, `M = gcd`); the validator re-derives
all of them mechanically. Two review flags for the next model: (i) the
deeper cells are new exact rows, derived, not present in either sealed
report — their pricing floor is P0's (lam is a lower bound; more printed
units would only kill more); (ii) the `(21,7)@nu3` cell carries `kbar = 1`,
which no licensed law forbids, but a reviewer should confirm no promoted
statement imposes `kbar >= 2` at a chain vertex.

## 4. Acceptance tests as implemented (corrected A2/A4)

- **A1** — record parity: unique entry, `W(2)={2}` (+ DS3 parity samples
  `W(4)`, `W(6)`), root DEAD, ZCH REJECTED, admitted menu exactly
  `{IIa(2,3,1) -> Q(6,12,3,2,5)}` with `W-CLOSED-FORM` child, family-I split
  in place, no `l<=4` cap row anywhere, `dq = 1 (mod nu)` on every `nu>=2`
  cell, mixed sector UNREACHABLE (not silently covered).
- **A2 (inverted)** — `UNCOVERED` may be empty and IS empty; failure = an
  unclassified candidate, an `UNCOVERED` row lacking
  h/instance/blocked-consumers, or an `UNCOVERED` row killed by a cited
  promoted theorem (the planted sealed-5.4 row fails exactly this way).
  Coverage remains orthogonal to alive/dead. A synthetic cap probe (its
  hypothesis deliberately absent from the frozen trust snapshot, tier CAP)
  must surface as `UNCOVERED` with full fields — and does.
- **A3** — first-step partition and both boundary terminal budgets exactly
  as recorded; the finite sub-boundary residue enumerated to budget
  exhaustion (13 admissible terminals + 9 route-dead states, §3.1); P0
  completeness cited, not re-proved.
- **A4** — hostile battery (all caught): the four duplicate parametrizations
  of `(2,8)` (raw / legacy `(l=5,eps_q=1)` / family-I `L=6` / `L=6` with
  `s(0)=0`) classify identically D9-dead; the sealed 5.4 classifier as a
  mutant; wrong cached `M` (both functional and planted-in-book);
  inconsistent `w_cert` (merge child stamped `W-PRICED-COMPLETE`; stray
  token `W-PRICED(P0)`); root-`M=1` kill; root `l=0` omission; case-IV at a
  genuine merge; case-II model of the ZCH 0-edge; equal-`mu` unequal-`w`
  join; `l`-vs-`M` conflation; shared-suffix double count; equality-route
  extra unit; cap-as-rejection (CAP-tier cert on a COVERED record);
  rejecting the genuine synthetic cap; dropped eta slot at `nu>=2`;
  `W-SYMBOLIC` never killing; deleted residue row caught by
  re-enumeration.
- **A5** — provenance: pole-swapped arrangements and per-pole chains are
  distinct records; the IIa `l=1` q-extra is in `unused_registry` as
  `NO_TREE_VERTEX` and each chain records its `nu-1` `DECK_CONJUGATE` slots
  parametrically (the review's cheap additions); every `cert_chain` resolves
  to the frozen snapshot; residue rows carry path provenance.

## 5. Test and validation record (exact)

    python3 ll1_compiler.py        # deterministic emit; prints out-hashes
    python3 ll1_validator.py       # exit 0: re-derives all arithmetic + summary
    python3 test_ll1_r2.py         # mode: ordinary   passed: 122  failed: 0
    python3 -O test_ll1_r2.py      # mode: OPTIMIZED  passed: 122  failed: 0
    python3 -O ll1_validator.py    # exit 0 (validator is assert-free)
    shasum -a 256 -c MANIFEST.sha256   # all OK

**122/122 checks in both modes** (the suite uses an explicit `chk` helper,
never `assert`, so `-O` runs the identical logic). Re-compilation is
byte-identical (canonical JSON, sorted keys, no timestamps, no absolute
paths). The validator recomputes the summary and every record's arithmetic
from record level and fails closed on unknown tokens, CAP-tier certificates
under COVERED, `M != gcd(dp,dq)`, `w_cert` drift, residue drift, or a
theorem-killed `UNCOVERED` row.

## 6. Scope firewall and remaining obligations (mandate 6)

This packet tests the corrected LL-1 quotient and hand-run at `td=6, m=2`
and nothing else. It is **not** a proof that the candidate grammar equals
all geometric configurations (`Cand(s)` vs `CFG`); it does **not** bound
segment depth (DS1 R1); it proves **no** source landing, ceiling, Keller,
or JC2 statement; no output touches `G2-PSC`, `G2-BD`, `RPMC(C)`, or the
cofinal degree ceiling. Single-pole composite configurations (REDUCTION
HIGH 1) and realizability are out of scope; `ALIVE` families are
conservative supersets; the mixed all-`mu>=2` emission menu remains OPEN in
general (BOOK-OFFAXIS §3) — at this header it is unreachable, which is a
divisibility fact, not a completeness theorem.

Exact remaining LL-2 / `td=7` obligations (stated, not claimed): the
off-axis entry `(2,3)`, `Lambda=(3,4)`, `(1,1,2)+(1,2,3)` (the packet's
entry solver already reproduces it as an entry-layer parity check, with no
td=7 claims); first firing of `W-PRICED` certification, dirty pre-merge
steps, case-III/E5 with the `H5a_reading` pin, and the 17-vs-2 conditional
books (§11a Q-reading census as the A1 baseline); mixed-merge emission
completeness wherever reachable. No named-lemma dependency is queued: D9
plus the §2.1 identification closes the `nu=1` layer of this sector.

## 7. Verdict

The corrected LL-1 packet compiles the promoted perimeter, not the sealed
residue: the family-I identification is normalized before classification,
D9 discharges the whole eta-variant family including `s(0)=0`, the real
`UNCOVERED` list is empty and the acceptance tests treat that as the pass
condition, and the budget-exhaustion residue is now an exact derived book
(with two corrected parentheticals flagged for the next reviewer).
**SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW**; AWS and canonical promotion
are not authorized.

---
Report-body self-hash (sha256 of every byte above this line): 29e892dab4fa31c6ff122706fc751cde32108b200af30f116dce9949b3fecd2b
