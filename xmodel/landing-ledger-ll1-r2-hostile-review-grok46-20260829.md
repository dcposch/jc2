# Hostile review: Fable5 LANDING-LEDGER LL-1 R2 repair (2026-08-29)

Reviewer: Grok 4.6, independent adversarial mathematical referee.
Subject: `xmodel/landing-ledger-ll1-r2-repair-fable5-20260829.md` together
with packet `cases/landing_ledger_ll1_r2_20260829/`.
Date: 2026-08-29 (UTC).

Sealed-body verification (computed this session, SHA-256; body = every
byte through the final `---\n` separator, reproduced, not reinterpreted):

- producer full file:
  `19df817d055f4124fb92ce5ba2d08d7610814a9c3c11d8fcf4da6a0711457530`;
- producer body through `---\n`:
  `29e892dab4fa31c6ff122706fc751cde32108b200af30f116dce9949b3fecd2b`
  (matches the printed self-hash).

Prior sealed inputs, rehashed this session (both match their pins):

- `xmodel/landing-ledger-primary-research-fable5-20260829.md`
  full `26bdd150a5a4bace23069b65f3234de6080fc7fb083f46a92773ec276a6fc689`,
  body `83fe23123f35275e551ef8d1704da1181dea9c346a4915cd0e15c6db82998700`;
- `xmodel/landing-ledger-primary-research-fable5-hostile-review-grok46-20260829.md`
  full `62d8f55ee6a34ccd960121e9e64498fbb3ee3a92a8a4681fec4290fc9c7bc5da`,
  body `88c1d66f09314e8717234b8617da84cd78a7fe95da90b31a120721272d678e79`.

Campaign sources, read in full at the cited sections (`jc2-lean` untouched):

| file | producer pin | this session | status |
|---|---|---|---|
| `ladder/SHEET6-MULTIPOLE.md` | `93adb7acedf4cf0fd56ffc68e4571649a04eab12e1271431449a79465a964bcb` | same | MATCH |
| `ladder/SHEET6-DEPTH.md` | `ad9ced6c0420902f8cf63edf3636bed8633be511e925f208d24a24c35d71036d` | same | MATCH |
| `ladder/BOOK-OFFAXIS.md` | `34f5ea9db62caf1da8b436733752e86402ff3f3ee08bc5096f13f8bf0c80eb17` | `7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77` | **MISS** |
| `ladder/REDUCTION.md` | `6b9376e0f479545f012cd7451bd3eb1a9271fc312b9996c5848c5db159ebdb31` | `0a88db0d136001a6c18343f941a80ecfaef5ceffcbe84e05c739a853d13c1936` | **MISS** |

The two misses survive CRLF, strip, git-blob SHA-256, and git-SHA-1
variants. They are a producer-report provenance defect, not a packet-byte
defect: MULTIPOLE (load-bearing D9/MP6) and DEPTH match; the P0/P1/§4/T7
sentences the packet actually consumes are present in the files now in
`ladder/` and were re-derived against those current texts. Packet
`MANIFEST.sha256` verifies in full (all six files OK). Recompilation this
session is byte-identical to the sealed `out/` artifacts.

No web, AWS, heavy/local CAS, canonical edit, commit, or push. Local
computation was exact integer/`Fraction` Python in `/tmp` plus the in-packet
compiler/validator/tests. This is an audit of the R2 allegations, not a
promotion.

---

## 0. Verdict

**PASS_AT_LL1_SCOPE.**

The R2 packet implements the repair the prior review demanded. The `nu=1`
eta writing is identified with MP6 family I *before* classification; D9
discharges every even extra-count `L`, including `s(0)=0`, from the printed
identity rather than from a td-7 zero-chain extension; the real `UNCOVERED`
list is empty and A2 treats that as a pass; derived `M`, the three-token
`w_cert` set, the cap firewall, and fail-closed validator semantics hold.
An independent P0/P1/St 9.4 enumerator, written without importing the
packet and run with a strictly larger Diophantine window, reproduces the
producer's §3.1 residue exactly: 13 admissible terminals (2 boundary + 2
deeper slack-1 + 9 equality-fragile) and 9 route-dead states. No omitted
in-budget ALIVE candidate, no theorem-killed open row in the real book, and
no false completeness claim *at this header and this licensed rule set*.

Maximum licensed promotion: **SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW** of
the corrected LL-1 (`td=6`, `m=2`) packet only. No AWS launch and no
canonical promotion are authorized by this review.

Two provenance/test-quality items are not packet-killing and must not be
silently dropped: (i) the BOOK-OFFAXIS and REDUCTION pins above do not
reproduce; (ii) A1's "26-shape / 351-route" gate is a tautology
(`2*nu+2 == 2*nu+2`) and is not engine parity. Re-pin those two sources
before anyone treats the producer-report hash table as a trust snapshot.

---

## 1. What was independently reconstructed (not assumed from either old report)

### 1.1 `nu=1` family-I identification

MP6(c) (MULTIPOLE, hashed match): `q = eta * rad(p) * extras` is the
`nu>=2` normal form, "eta-factor absorbed at `nu=1`". At `nu=1` the point
`0` is an ordinary point of the line. Family I is `(dp,dq)=(r, r+L)` with
`q = p s`, `deg s = L`, `M = gcd(r,L)`.

Legacy merge grammar `dq = (r0+k+l)nu + eps_q` with `eps_q` free at
`nu=1` therefore splits one cell. The one-line identification:

    legacy (l, eps_q=1)  =>  q = eta * p * s~, deg s~ = l
                         =>  q = p s with s = eta * s~, deg s = l+1
                         =>  family I at extra-count L = l+1, s(0)=0,
                             (dp,dq)=(2, 3+l)=(2, 2+L).

`q(0)=0` is a location flag on the extras, not a degree increment.
Independent normalizations of the four presentations of `(2,8)` all give
`L=6`, `(dp,dq)=(2,8)`:

| presentation | L | dq | classifier |
|---|---:|---:|---|
| raw `(dp,dq)=(2,8)` | 6 | 8 | D9-DEAD |
| legacy `(l=5, eps_q=1)` | 6 | 8 | D9-DEAD |
| family I `L=6`, `s(0)` free | 6 | 8 | D9-DEAD |
| family I `L=6`, `s(0)=0` | 6 | 8 | D9-DEAD |
| legacy `(l=5, eps_q=0)` | 5 | 7 | MP2-DEAD (odd L, `M=1`) |

At `nu>=2` the eta slot stays forced (R1.0: `dq = 1 (mod nu)`). Checked on
the admitted IIa cell (`10 = 1 (mod 3)`) and on every independent dirty
cell in the residue (`dq % nu == 1`).

This is the prior review's repair R-1, now compiled. It is not a new
theorem: it is MP6(c) applied to the enumerator parameterization the
sealed body had treated as a degree slot.

### 1.2 D9 residue obstruction, including `s(0)=0` and all even `L`

D9 (MULTIPOLE, hashed match), interior `nu=1`, family I: identity (iv)
reduces to `2 p s' - L p' s = c' != 0` with `rho = 2/(2+L)`. Even `L`:
divide by `p^{(L+2)/2}`,

    (s p^{-L/2})' = (c'/2) p^{-(L+2)/2}.

Residue at each p-root `C(-n, n-1)(a1-a2)^{1-2n}`, `n=(L+2)/2`,
`C(-n,n-1)=(-1)^{n-1} C(2n-2,n-1) != 0` for all `n>=2`. Left side is an
exact derivative (zero residues), so `c'=0`, contradicting `theta != 0`.
The residues sit at the two p-roots, not at 0. D9 never uses `s(0)!=0`.
The argument is td-uniform and degree-uniform in `s`.

Independent exact checks (not the packet's `d9_ode_status`; larger degree
window `deg s <= L+4`, three root pairs including a p-root at 0):

| n | L=2n-2 | C(-n,n-1) | C(2n-2,n-1) |
|---:|---:|---:|---:|
| 2 | 2 | -2 | 2 |
| 3 | 4 | 6 | 6 |
| 4 | 6 | -20 | 20 |
| 5 | 8 | 70 | 70 |
| 6 | 10 | -252 | 252 |

For `L in {2,4,6,8,10}` and roots `{(1,3),(-2,5),(0,1)}`: the linear
system `T(s)=1` is inconsistent; the `s(0)=0` subcase is equally
inconsistent; `T(p^{L/2})=0` (kernel contains `span{p^{L/2}}`). Positive
control `L=1`: `s = t - (a1+a2)/2` gives `c' = -(a1-a2)^2/2` (at
`(1,3)` this is `-2`), and the solver reports solvable. The old
l1_ode_check B/B-eta cells are `L=2,4` (legacy eta `l=1,3`), negative
controls of D9, not a finite certificate.

Odd `L`: `M=gcd(2,L)=1`, interior trunk, MP2. `L=0`: `q=p` forces
`deg p=1`, MP7 (the Python `gcd(2,0)=2` is not used as a kill).

The sealed "candidate closing lemma" (BOOK-OFFAXIS §11) stays quarantined:
`kbar = 2 + 4/(l+1)` lies in `{3,4}` only at legacy eta `l in {1,3}`.
`dp|dq` here is the integrating-factor exponent `(L+2)/2 in N*`, which is
D9's own mechanism. No td-7 zero-chain extension is invoked, correctly.

MP9's printed cap flag ("eta-factor excluded only for `l<=4`") remains in
MULTIPOLE; this packet is not a canonical edit of that sentence. It is a
compiler that refuses to inherit the cap as a decision.

---

## 2. Eleven-way merge partition, empty `UNCOVERED`, fail-closed semantics

The merge section has exactly eleven records, no default branch:

| record | verdict | law |
|---|---|---|
| `MERGE/ROOT/parametric-l>=1` | DEAD | case-I window on certified `w=2`; local `r=2,l=1` cell `w=1/3`, `M_root=1` legal |
| `MERGE/ROOT/l=0` | REJECTED | MP7/D9 root clause |
| `MERGE/ZCH/0-edge=P1` | REJECTED | DEPTH 5c: `2 = nu_e * 2` impossible |
| `MERGE/ZCH/0-edge=P2` | REJECTED | same, distinct pole provenance |
| `MERGE/IIA/l-or-nu-even` | DEAD | `M=gcd(2,l nu+1)=1`, MP2 |
| `MERGE/IIA/l-nu-odd-nonintegral` | REJECTED | `d=l nu+1 \| 4`, `d` even `>=4` so `d=4`, only `(nu,l)=(3,1)` |
| `MERGE/IIA/admitted-(2,3,1)` | ADMITTED | `(dp,dq)=(6,10)`, `kbar=5`, `X=3`, `M=2`, `Q=(6,12,3,2,5)`, `w_trunk=3/2`, `W-CLOSED-FORM` |
| `MERGE/FAMILY-I/L-odd` | DEAD | `M=1`, MP2 |
| `MERGE/FAMILY-I/L-even` | DEAD | D9, `s(0)=0` included |
| `MERGE/FAMILY-I/L-0` | REJECTED | MP7 |
| `MERGE/MIXED/all-mu>=2` | UNREACHABLE | `mu_e \| M=1`; general mixed menu stays OPEN (BOOK-OFFAXIS §3) |

IIa uniqueness is a theorem, not a sweep: `kbar=2+4 nu/d` with
`d=l nu+1`, `gcd(d,nu)=1`, so `d|4`; `l nu` odd forces `d` even, hence
`d=4`, `l nu=3`, only `(3,1)`. Spot cells `(5,1),(3,3),(7,1),(5,3)` are
non-integral, as claimed. Independent recomputation of the admitted cell:

    kbar = 2 + 12/4 = 5,  X = 3,
    w_trunk = (5 - 3/6)/3 = 3/2,
    Q = (i X, i dp, nu, M, kbar) = (6, 12, 3, 2, 5).

`UNCOVERED` of the real book is `[]`. Under inverted A2 that is a pass:
failure is an unclassified candidate, an `UNCOVERED` row lacking
h/instance/blocked-consumers, or an `UNCOVERED` row a cited promoted
theorem already kills. The synthetic CAP-tier probe lives in
`synthetic_probes`, not in `uncovered`, and carries full fields. Coverage
is orthogonal to ALIVE/DEAD (DEAD rows are COVERED). Mixed is COVERED /
UNREACHABLE, not silently omitted and not pretended complete.

Independent validator mutations (in `/tmp`, packet tree untouched):

- extra merge record without `classification` -> fail-closed
  (`unclassified candidate` plus partition drift);
- planted family-I `L=6` as `UNCOVERED` ->
  `killed by a cited promoted theorem (DEAD: MP6;D9-LOG)`;
- compiler mutant emitting even-`L` as `UNCOVERED` -> 7 test failures
  including A1/A2/A4-1/A4-2.

Caps cannot reject: a COVERED record citing `SYN-1` (tier CAP) fails
validation. `W-SYMBOLIC` never fires the root window; `W-CLOSED-FORM` and
`W-PRICED-COMPLETE` do. The IIa child is stamped `W-CLOSED-FORM` (DS4 of
two closed-form arrivals); priced suffix children are `W-PRICED-COMPLETE`.
Stray token `W-PRICED(P0)` is rejected. `M` is `gcd(dp,dq)` of the *child*
shape at every vertex; the (A)-cell counterexample is exact:
cached `gcd(2*7, 8)=2` versus `gcd(21,15)=3`.

Entry (independent T7 arithmetic, current REDUCTION text): `Lambda=(3,3)`,
type `(2,3)`, prime/beta-minimal forces `b=1`, unique `(a,b,nu)=(1,1,2)`,
`kbar=5`, `(M,rho,w0)=(1,1,2)`, off-axis empty (BOOK-OFFAXIS §4, current
text). `W(2)={2}`. Chains parametric `(2, nu, 2 nu+2)`, depth unbounded
(DS1 R1). Family-level 26-shape / 351-route parity is *cited* to DEPTH
§6–§7, not re-run; the A1 check that supposedly pins it is
`all(2*nu+2 == 2*nu+2 ...)`, a tautology. The formula itself is correct
(DEPTH §6). Do not read A1 as engine replay.

---

## 3. Hostile audit of the new §3.1 residue

Neither sealed parenthetical is used as an oracle. The finite book is
re-derived from licensed P0 pricing, P1 terminals, and St 9.4 with
`psi >= 1` hence `Sum lam <= td-2 = 4`.

### 3.1 Independent first-step P0 from `(w,M)=(3/2,2)`

Soundness first-principles (kbar in Z, strict NE, root-mult, searrow
`E>0`, `dq=1 (mod nu)`, `M=gcd(dp,dq)`), completeness window the printed
P0 bound `E <= l * num(w) * T`, with lex/k pads strictly larger than the
packet's. Resulting priced extras-present cells, uniquely:

| cell | nu | kbar | lam | (w',M') | fate |
|---|---:|---:|---:|---|---|
| (21,15) | 7 | 5 | 2 | (2/3, 3) | ADMITTED |
| (20,16) | 5 | 4 | 2 | (3/4, 4) | ADMITTED |
| (7,5) | 2 | 5 | 3 | (2, 1) | DEAD MP2 |

Pure-(b) `eps=1`: `w' = 3`, `lam_min=3`, `M | 1` hence `M'=1`, DEAD.
Clean resonant: `Del | 3` forces `(n,nu)=(2,2)`, `dq=5`,
`kbar=(3/2)*5/3=5/2` not in Z, REJECTED. Neutral thick `l=2`: `w` fixed,
`M'=gcd(2,nu+1)=2` iff `nu` odd; even `nu` is MP2-dead. Thin `l=1`:
`M'=1`, DEAD. Nothing else in the enlarged window. This matches
BOOK-OFFAXIS §10's recorded one-step menu from `(3/2,2)` and the packet.

P0 *completeness as a theorem* is still cited, not re-proved. What is
proved here is: at this one state, a superset search under the printed
finiteness bound finds no extra cell.

### 3.2 Independent budget-exhaustion BFS

Start `(3/2, 2, lam=0)`. Edges: dirty/pure-b with `l | M` and remaining
budget, plus neutral shrink to proper divisors of `M`. Terminal attempted
at every state. Dedup key `(w,M,lam)` (first BFS path recorded; alternate
paths counted, not double-priced). Route-death is the explicit fixpoint:
a state can complete iff it has an in-budget admissible terminal or an
edge into a state that can.

23 states. 13 ALIVE / ALIVE_FRAGILE, 1 budget-DEAD terminal, 9
TERMINAL-REJECTED of which 8 plus the budget-DEAD terminal are
route-dead, and the boundary `(3/2,2,0)` is TERMINAL-REJECTED but not
route-dead (it completes downstream). Packet `residue_terminals` /
`residue_steps` match this set exactly (canonical comparison of the
ALIVE table and the route-dead list).

**2 deeper slack-1 ALIVE** (`psi=1`, `Sum lam=3`, budget 4):

| state | j | path (representative) |
|---|---:|---|
| `(2/5, 5, 3)` | 3 | (A) `(21,15)` then `(35,15)@nu=7`, `l=3`, `lam=1` |
| `(2/7, 7, 3)` | 5 | (C) `(20,16)` then `(119,35)@nu=17`, `l=4`, `lam=1` |

`(35,15)` is the St 9.6-family `l=3` cell BOOK-OFFAXIS P4 uses at td=7,
here consumed only as a P0 step from `(2/3,3)`. Independent arithmetic:
`E=10`, `kbar=3`, `w'=2/5`, `M'=5`, AF2 `lam=1`. `(119,35)`:
`E=21`, `kbar=5`, `w'=2/7`, `M'=7`, AF2 `lam=1`.

**9 equality ALIVE_FRAGILE** (`psi=1`, `Sum lam=4`, St 9.4 equality;
any new printed unit kills):

`(1/2,2)`, `(1/2,4)`, `(2/5,5)`, `(2/7,7)`, `(2/9,9)`, `(2/11,11)`,
`(2/13,13)`, `(3/8,8)`, `(3/10,10)` — all at `lam=4`. Each has
`j=M(1-w) in N*` and `psi=ceil(M/j)-1=1`. `(2/5,5)` and `(2/7,7)` appear
twice in the book, at `lam=3` (slack-1) and `lam=4` (equality): different
states, not a double count.

Plus the two first-step boundary terminals already in both old reports:
`(2/3,3)@lam=2` ALIVE slack 1 (`j=1`, `psi=2`, budget 3);
`(3/4,4)@lam=2` ALIVE_FRAGILE (`j=1`, `psi=3`, budget 2).

**9 route-dead** (no in-budget admissible terminal reachable):

`(2/3,3)@lam=4` (admissible terminal but `4>3`, verdict DEAD);
`(3/4,2)` (`j=1/2 not in N*`);
`(3/2,2)@lam=4` and `(1,2)@lam=4` (`w>=1`);
`(2/9,3)`, `(3/10,2)`, `(3/10,5)`, `(3/8,2)`, `(3/8,4)` (`j not in N*`).

Six states have alternate paths (same `(w,M,lam)`, different routes).
Dedup by state is the correct shared-suffix accounting: lam is already in
the key, so two routes to the same reduced state are not priced twice.
This is not the two-pole shared-trunk double-count A4-11 plants; that
mutant (`budget_verdict(4,3)` vs `(2,3)`) still flips ALIVE to DEAD.

### 3.3 `(21,7)@nu=3` with `kbar=1`, and the sibling the producer did not name

From `(2/5,5)@lam=3`, `l=5 | 5`:

    dp=21, dq=7, nu=3, eps=0, k=1, lex=0, mults=[2],
    E=14, kbar=1, X=3, lam=1, w'=2/7, M'=7.

Law-by-law: `dq=7=1 (mod 3)` (R1.0); `E>0`; `2*7=14<21` (strict NE);
`21 != 5*7` and `21 != 2*7` (root-mult); `M=gcd(21,7)=7`;
`rho=kbar/dq=1/7 < 1=kbar` (St 8.2); `l | M_parent`. No licensed
statement in MULTIPOLE, DEPTH, BOOK-OFFAXIS, or REDUCTION imposes
`kbar>=2` at a chain vertex. DS1(c)/Not 3.5 is integrality at `nu>=2`.
MP9's `kbar < nu` clause is the root-parent H1 residual, not a chain-child
floor. Packet filter `kbar>=1` is the only extra cut; `kbar=1` passes it.

A second `kbar=1` cell exists and is in the packet steps: `(55,11)@nu=5`
from `(2/7,7)@lam=3`, `l=7`, `E=22`, `w'=2/11`, `M'=11`, landing the
equality terminal `(2/11,11)@lam=4`. Same legal status. The producer
flagged only `(21,7)`; both survive.

Recorded `lam` is the AF2 *formula value* and, by P0 honesty rider (i), a
lower bound ("per-state lambda is the MIN over paths"). ALIVE is a
conservative superset: realizability untracked, more printed units can
only kill. Equality rows are FRAGILE for that reason. The packet does not
treat these lambda values as exact geometric prices.

### 3.4 Sought and not found

- **Omitted in-budget ALIVE candidate.** Enlarged-window P0 at every
  visited `(w,l)` produced no extra `M_child>=2` cell that the packet
  BFS missed. Clean resonant on every reachable alphabet with `num(w)=3`
  (namely `w in {3/2, 3/4, 3/8, 3/10}`) is the single pair `(n,nu)=(2,2)`
  and is non-integral at all of them. Thin `l=1` is always `M'=1`. The
  residue BFS does not *record* those deeper R2 rejects as COVERED rows
  (only the boundary `SUFFIX/clean-resonant` is explicit). That is
  ledger-silence on a uniformly dead candidate class, not a missed
  survivor. It is not a packet fail at LL-1 scope.
- **Theorem-killed open row.** Real `uncovered=[]`. The sealed 5.4 family
  planted as `UNCOVERED` fails the validator. Empty UNCOVERED is not a
  completeness theorem for `Cand(s)` vs `CFG`, and the packet does not
  claim that.
- **False completeness claim.** §6 firewalls: not CFG totality, not a
  depth bound, not a landing/ceiling/Keller/JC2 statement, mixed menu
  OPEN in general, ALIVE conservative, P0 completeness cited. The phrase
  "complete derived residue book" is scoped to P0+P1+St 9.4 at this
  header; the independent enumerator agrees. BOOK-OFFAXIS P5's finite
  reduced `(w,M)` theorem is not a substitute for a general chain-index
  census and is not used as one.

---

## 4. Tests, mutations, hashes

Packet hashes (this session = MANIFEST):

    882553136eb1bc06b87c1ef7177b13faa5d0104f10e26e1df8c808dc672e0710  ll1_compiler.py
    fd3170cbad68b3f7058065161dd1889ef5375103fc45351a6943f56e661e3fc9  ll1_validator.py
    3003a6bfd5731b6a921e9be17c0ce2026adb8a523eecd19065eddb9853313489  test_ll1_r2.py
    43a9e88dbc9b45c629579d2088755a55059050f4f2709523f68365cd7a3cc932  INVENTORY.md
    cb490d4e5db3db9ba7ac87320cdc11452cd5fa8c82efb55a8499b260d62154ce  out/ll1_book.json
    9fa89c424af89c78b3277f87c05b993f1af35983c7772e578a16f853780366e9  out/ll1_summary.json

Re-run this session (cwd the packet; no `assert` in tests or validator):

    python3 ll1_compiler.py        # byte-identical out-hashes
    python3 ll1_validator.py       # exit 0
    python3 test_ll1_r2.py         # mode: ordinary   passed: 122  failed: 0
    python3 -O test_ll1_r2.py      # mode: OPTIMIZED  passed: 122  failed: 0
    python3 -O ll1_validator.py    # exit 0
    shasum -a 256 -c MANIFEST.sha256   # all OK

122/122 in both modes is the exact count printed by the `chk` helper
(94 call sites, the rest from loops: D9 `n=2..6`, even-`L` root pairs,
IIa spots). Independent mutations in `/tmp` (packet not edited): requiring
nonempty `UNCOVERED` fails A2 (121/122); deleting the expected
`(2/13,13)@lam=4` row fails A3 (121/122); forcing even-`L` `UNCOVERED`
fails 7 checks. A4 already plants the historical bugs (cached M, stray
`w_cert`, root-`M=1`, case-IV at a merge, case-II ZCH, equal-mu unequal-w,
`l` vs current `M`, shared-suffix double count, equality extra unit,
cap-as-rejection, dropped eta slot, `W-SYMBOLIC` non-kill, deleted
residue row). Those still catch.

`td=7,m=2` entry-layer pointer (no td=7 claims): independent T7 solve
gives the unique off-axis witness `Lambda=(3,4)`, type `(2,3)`,
`(1,1,2)+(1,2,3)`, matching BOOK-OFFAXIS §1a. On-axis empty at td=7 as
the packet says.

---

## 5. Exact remaining LL-2 obligation

After this packet, and not licensed by it:

- LL-2 = `td=7`, `m=2`, including the off-axis entry above: first header
  at which `W-PRICED` certification, dirty pre-merge steps, case-III/E5
  with the `H5a_reading` pin, and the 17-versus-2 conditional books all
  fire. A1 baseline is the §11a Q-reading 17-cell census.
- Mixed all-`mu>=2` emission completeness wherever reachable
  (BOOK-OFFAXIS §3; REDUCTION Critical 5: the `s>=3` parenthetical is
  false in general, and is not used here).
- No named-lemma dependency is queued for the `nu=1` family-I layer: D9
  plus the §1.1 identification closes it at this sector.
- Re-pin BOOK-OFFAXIS and REDUCTION before treating the producer-report
  hash table as a snapshot. Replace the tautological A1 engine-parity
  check if LL-2 wants a real 26/351 gate.

---

## 6. Claim firewall

This review licenses nothing beyond a different-model review of the
corrected LL-1 packet at `td=6,m=2`. It is not a proof that `Cand(s)=CFG`;
it does not bound segment depth; it proves no source landing, ceiling,
Keller, or JC2 statement; no output touches `G2-PSC`, `G2-BD`, `RPMC(C)`,
or the cofinal degree ceiling. Single-pole composite configurations
(REDUCTION HIGH 1) remain open. `ALIVE` families are conservative
supersets. Lambda values are recorded AF2 lower bounds, not exact prices.
P0 menu completeness at a general state remains a cited BOOK-OFFAXIS §10
certificate. MP8 equality/(22)/(22-cl)/no-refinement rhetoric stays
quarantined. No AWS and no canonical promotion.

---

## 7. Verdict restated

**PASS_AT_LL1_SCOPE.** The R2 packet compiles the promoted perimeter at
`td=6,m=2`: family-I identification before classify, D9 for every even
`L` including `s(0)=0`, inverted A2 with empty `UNCOVERED` as a pass,
derived `M`, coherent `w_cert`, cap firewall, and an independently
reproduced 13+9 residue book. Maximum promotion:
`SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW`. Next obligation is LL-2 at
`td=7` as specified in §5. Two source pins fail to reproduce and A1's
engine-parity check is vacuous; neither falsifies the packet arithmetic.

No JC2, landing, or ceiling claim is licensed by the sealed R2 body or
by this review.

---
Report-body self-hash (sha256 of every byte above this line): 3673da4736301d645edc4ab08ea3cb60b1563df6c565200eac7cdaa57972472f
