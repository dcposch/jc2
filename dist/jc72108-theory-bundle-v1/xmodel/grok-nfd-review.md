**VERDICT: STILL-SHORT — M1 permanence holds on cylinder (2.5) and td-7 D=4 is earned (Pi=11305=5·7·17·19, 15 multisets); td-11 D=0 is false: H8 is P/μ and μ=M (Class A) equalizes every quoted valuation, so the windows are infinite residue classes, not empty; CE3 and the OB2 keep-direction check out; the load-bearing compiler simplification is not earned.**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-14.
Target: `NF-D.md` (status PROVED for the H8-synchronized pure-neutral slice, relative to CONS, with per-entry computable `D`; honest reductions NF-D-OB1/OB2). Closed record: `NF-Z.md` (REDUCED-WITH-PROVED-IN-ZONE-CORE; quotient program closed post round-4 STILL-SHORT).
Prior NF-Z reviews: **NOT-PROVED** (`xmodel/grok-nfz-review.md`), **STILL-SHORT** (`xmodel/grok-nfz-rereview.md`), **STILL-SHORT** (`xmodel/grok-nfz-final.md`). This is round 1 of the depth-cap pivot.
Claims under review: (1) replay M1 monotonicity and permanence of `Omega` (hunt a letter that rescales rather than extends); (2) td-7 `D=4` via `Pi=11305=5·7·17·19` and the complete 15-multiset menu; (3) td-11: all three entries have `D=0` because the valuation windows are empty (11-A `v_2` promoted, 11-B `v_3` 0 vs 1, 11-C `v_2` 1 vs 2); (4) all six CE orders DEAD — verify at least CE3 (`den(α_*)=13566` forced, first `k` 39270 vs 87297210); (5) OB2 fail-closed direction: for a census, fail-closed must KEEP-AS-POSSIBLY-LIVE, not discard.
Method: line-read of `NF-D.md` against the closed `NF-Z.md` header, `xmodel/sol-normalform.md` (1.4)/(2.5)/(4.1)–(4.6)/Rule 6, `xmodel/sol-td11-13-scope.md` §3.1 packets, `TOWER-9-15.md` + `t9_15_direct.json:729` (ladder `2→22610`), `BOOK-OFFAXIS.md` P3 Class A. `python3 cases/nfd_check.py`: exit 0, **19/19 PASS**. Independent exact `Fraction` replay of CE3, of the 15 partitions of `{5,7,17,19}`, of all three td-11 valuation windows *with* `μ | M`, and of the (2.5) vs `CHAIN_SCALE`/`ν=1` degree laws. No other repo file modified. No git.

---

## Findings (worst first)

### 1. Severity: break — Claim (3), and the “D=0 at all three td-11 entries” half of the status. Mechanism B quotes the 11-A consumer as raw `v_p(P_0 Π)` equality. H8 is `P/μ`. With `μ=M` (the documented default, and td-7 Class A) every quoted window is inhabited, including the empty stack. `S` is an infinite residue class, not `∅`.

- File: `NF-D.md:72-79,115-124,152-173,216-221`; `cases/nfd_check.py:190-218`; `xmodel/sol-normalform.md:111-115,165,584-599`; `BOOK-OFFAXIS.md:521-530`
- Claim: H8 equal quotient requires `v_p(P_0^{(1)} Π_1) = v_p(P_0^{(2)} Π_2)` for every prime `p`. Letter domains pin those valuations, they mismatch on all three td-11 packets (including the empty stack), so `S=∅` and `D=0`. “This kills deep neutrals at td-11 outright.” Gate D2/D3/D4.
- How checked.

  **The law is (1.4), not the 11-A special case.** `sol-normalform.md:111-115`: `μ_e | M_{H_e}` of the *current* state, and `P_{H_e} = i_G μ_e`. Equal quotient consumes `P/μ` (`sol-normalform.md:165`). The promoted 11-A certificate compares raw `P` only because both arrivals have `M=1`, hence `μ=(1,1)`. Copying that predicate onto packets with `M∈{2,3}` is an illicit specialization.

  **`μ=M` is not an edge case.** `sol-td11-13-scope.md:30`: the current code *sets* `μ_e = M_child` (the defect is that it should be `μ | M`, not that `μ=M` is illegal). `BOOK-OFFAXIS.md:530-536` Class A, the main td-7 join, is exactly the unequal pair `(μ_1,μ_2)=(1,2)`.

  **Empty-stack arithmetic, exact.** Packet degrees are the `p=b·α` of §3.1. Cylinder (2.5) at depth 0 has `Π=1` and arrival `M` equal to entry `M`.

  | entry | packets | `μ=(1,1)` (what the gate tests) | `μ=(1,M_2)` (Class A / default) |
  |---|---|---|---|
  | 11-A | `[1@2;2]+[2@3;4]` | `2/1` vs `4/1`: `v_2` is 1 vs 2, empty | `2/1` vs `4/2`: both 2. **H8 holds** |
  | 11-B | `[1@3;2]+[3@4/3;6]` | `2/1` vs `6/1`: `v_3` is 0 vs 1, empty | `2/1` vs `6/3`: both 2. **H8 holds** |
  | 11-C | `[1@2;2]+2[2@3/2;4]` | `2/1` vs `4/1`: `v_2` is 1 vs 2, empty | `2/1` vs `4/2`: both 2. **H8 holds** |

  The letter-domain pins themselves replay (independently, and the gate’s D1–D3 are correct *as raw-`P` statements*):

  * `w=2` and `w=3/2`: `d | u+1` forces `u` odd, so `v_2(Π)=0`.
  * `w=3`: `gcd(3,u)=1` forces `3 ∤ u`, so `v_3(Π)=0`.
  * `w=4/3`: `3 | u+1` forces `3 ∤ u`, so `v_3(Π)=0`. (BOOK-N1 also forces `u` odd; not needed for `v_3`.)

  Those pins empty the *raw-`P`* comparison. They do not empty `P/μ`.

  **Nonempty M-preserving words, same pin.** Cylinder (2.5) is `P'=P u` with `M'=gcd(l,u+1)`. On an `M=2` seed, `l=2` and `u` odd preserve `M` and keep `μ=2` available. H8 then reads `P_0^{(1)} Π_1 = P_0^{(2)} Π_2 / M_2`, i.e.

  ```
  11-A / 11-C:  2 Π_1 = 4 Π_2 / 2   ⇒   Π_1 = Π_2
  11-B:         2 Π_1 = 6 Π_2 / 3   ⇒   Π_1 = Π_2
  ```

  Legal on both sides simultaneously: `Π` odd and `3`-free (11-A: left odd, right `3 ∤ u` and M-preserving ⇒ `u` odd; 11-B: left `3 ∤ u`, right `3 | u+1` and `gcd(4,u)=1`; 11-C: both odd, right also `gcd(3,u)=1`). Concrete word: `Π_1=Π_2=5` (letter `u=5` is legal at `w∈{2,3,3/2,4/3}`). Concrete infinite family: `Π=5^k` on both poles, depth `k` arbitrary, `i_G=2·5^k`.

  So `S`, computed from the actual H8 law plus the letter-domain valuations, is an infinite residue class. The formula `D = max_{s∈S} Ω(s/P_0)` is then infinite. Mechanism B produces a finite `D` only when the *correct* valuation system is unsatisfiable, or when a mechanism-A exact pin is present. Neither holds on these three packets.

  **11-A’s table row is the wrong comparison even as a citation.** It writes “`v_2(2Π)=1` vs resonance-side `≥3`” and D4 checks `1<3` as a hardcoded boolean. That is the promoted `H8_EQUAL_QUOTIENT_VP_MISMATCH` certificate (`sol-normalform.md:522-599`), independently replayed here (`P_1=2C` with `C` odd ⇒ `v_2=1`; resonance `P'=4·(2l)/l=8`, later odd multipliers keep `v_2=3`; a `w=3` prefix `A` gives `v_2(8AB)≥3`). It is a mixed charged/neutral comparison. The document’s own remarks put the `5/8` step in NF-P, “same carve as 11-A’s `5/8`.” It is not a computation of the *pure-neutral* window. The pure-neutral 11-A comparison at `μ=1` would have been `1` vs `≥2` (right packet `P_0=4`); at `μ=2` it matches, as above.

  **Why the gate is silent.** D2/D3 quantify over letter stacks and compare `v_p(P_0 Π)`, never `v_p(P_0 Π)−v_p(μ)`. D4 does not load the resonance side at all. Empty-stack is included, and is exactly the row that *passes* H8 at `μ=M`.

  **Two readings, one compiler conclusion.** Reading A (intended: “H8 equal quotient” means the (1.4) law): `D=0` is false. Reading B (charitable: “synchronized” means raw-`P` equal, and `μ`-compensated stacks are OB2): `D=0` holds on a thin slice, and the live Class-A family is an unbounded OB2 residue. Either way the slogan “kills deep neutrals at td-11 outright” is false, and a compiler that emits an empty synchronized-leg panel from D2–D4 is certifying emptiness with a stronger-than-true constraint.

  This is the soundness trap the review was asked to look for at OB2. It fires here.

### 2. Severity: clear — Claim (3) as status, and §8. “PROVED … with per-entry computable `D`” is earned for mechanism A (td-7) and not for the td-11 instances. §8’s “`D=0` entries contribute an empty synchronized enumeration” is an emptiness certificate the proof does not support.

- File: `NF-D.md:1-6,66-79,167-173,214-224`
- Claim: the theorem holds on the H8-synchronized pure-neutral slice; instances `D=4` (td-7) and `D=0` (all three td-11); compiler enumerates to depth `D` and treats `D=0` as an empty synchronized panel.
- How checked.

  The general lemma — *if* liveness pins `P_r` in a *finite* set `S`, *then* live depth is `≤ max Ω(s/P_0)` — is the unique-factorization corollary of M1 (finding 3). td-7 supplies a finite `S` by a certificate row. td-11 supplies `S=∅` by a wrong predicate (finding 1). The printed status conjoins them.

  §3’s finiteness sentence (“finitely many primes appear in the packet degrees, the valuation system is finite linear arithmetic”) describes a finite *constraint system*, not a finite *set of integers*. Valuation constraints on `{2,3}` cut out a residue class. That class is finite only if unsatisfiable. The sentence is the rhetoric that made `D=0` look like a computation rather than an unsat claim.

  §5’s own hedge is right and is then ignored: “`D=0` means the synchronized-leg neutral enumeration is EMPTY — it does not by itself kill the entries.” Combined with finding 1, even the synchronized-leg emptiness is unearned. Charged/resonant legs were already NF-P; the new content was supposed to be the pure-neutral `D=0`.

### 3. Severity: residual — Claim (1), the flagged hole. Cylinder (2.5) multiplies `P` by `u≥2`. `Ω` rises by `≥1` per letter, permanently. The rescaling classes exist and are correctly outside the slice.

- File: `NF-D.md:50-51,81-90,130-143`; `xmodel/sol-normalform.md:256-265,700-709`; `xmodel/grok-normalform-review.md` (the `ν=1` degree-preserving hole)
- Claim: `P_j = P_0·u_1···u_j` with `u_j≥2`, so `Ω(P_j)=Ω(P_0)+∑Ω(u_i)` is strictly increasing and leaving any finite scale set is permanent. Likeliest hole: a letter that rescales (`p·dp/l`) and drops `Ω`.
- How checked.

  **(2.5) is `P'=Pu`, not `(P/l)·u`.** `sol-normalform.md:256-259`:

  ```
  w'=w,   M'=gcd(l,u+1),   (ν, κ̄, ρ, P') = (u, w(u+1), w, P u).
  ```

  The general child formula `pdeg = p·dp/l` uses *unreduced* `dp`. The 11-A resonance computation is the witness: both `l=1,2` give `P'=4·(2l)/l=8=4·ν`. For clean `n=1`, `dp=l·u` and the `l` cancels. `ScaleExpr.NEUTRAL` is `P*u`; `CHAIN_SCALE` is the general constructor, and on a (2.5) letter it *is* `NEUTRAL`. `Ω(ab)=Ω(a)+Ω(b)` is an identity, so M1 is order-independent and the exit from a finite `S` is permanent. Independently: every permutation of `(3,5,7)`, `(3,5,7,11)`, `(5,323,13)` at `P_0∈{2,3,4,30002}` has `Ω` rising by `≥1` per letter; every scanned word of depth `r` has `Ω(Π)≥r`. Gate B1/B2.

  **Rescaling classes, one by one.**

  | constructor | degree law | `Ω` | in the NF-D slice? |
  |---|---|---|---|
  | (2.5) `u≥2` | `P·u` | `+Ω(u)≥1` | **yes** |
  | `ν=1`, `n=1` | `P'=P·dp/l=P` | **flat** | no (`u≥2`; NF-P; grok-normalform finding) |
  | `PURE_B` (2.6) | `P·(ε+lu)/l` | can stall or move either way | no (charged) |
  | `CHAIN_SCALE` with *reduced* `dp=u` | `P·u/l` | on filed `M≤3`, `Ω(l)≤1≤Ω(u)`: stall, not drop | not the (2.5) law |

  Even under the *wrong* reduced-`dp` convention, filed packets cannot *decrease* `Ω` (`M≤3`). They can stall (`11-C`: `P_0=4`, `l=2`, `u=5` gives `4→10`, `Ω: 2→2`). Stall would break permanence of “once `Ω>D`, dead forever” against an *exact* pin, and would not refill an empty window. The actual (2.5) law does not stall.

  M2 (`k'≥uu'≥4` vs td-7 window cap `k|2`) is the promoted N-closure corollary, not a new theorem. The gate’s proxy (denominator of `γ_{j+1}−γ_j`) equals `uv` on the scanned `(P_0,u,v)`; Z2’s actual formula `k'=uv P_0/gcd(uv−1,P_0)` is `≥4` on the same range. Stands as cited.

  Claim (1) holds. The hole that was likeliest a priori does not fire.

### 4. Severity: residual — Claim (5). OB2’s fail-closed direction is the right Rule-6 policy (KEEP on the fat record; no emptiness from an unproved cap). It is not where the census soundness trap lives.

- File: `NF-D.md:201-206,214-224`; `NF-Z.md:407-440`; `xmodel/sol-normalform.md:728-731`
- Claim: non-synchronized words stay on the exact fat record; no emptiness certificate may assume a depth cap there. Same interface as NF-Z†.
- How checked.

  Sol Rule 6: a run with an open obligation may emit `OPEN` / a symbolic candidate; it may **not** certify an empty panel. “Stay on the exact fat record; no emptiness certificate may assume a depth cap there” is KEEP-AS-POSSIBLY-LIVE. That is the correct direction for a census *and* for an emptiness claim. A live non-synchronized class is not discarded by the written policy.

  What the policy does *not* do is cover finding 1. `D=0` on the synchronized slice is itself an emptiness certificate. Applying it, with the written mechanism-B predicate, discards the Class-A family. That is fail-*open* on emptiness — the classic trap — and it is in §5/§8, not in OB2.

  OB1 (13-x ports uncomputed) is honest and is the same point as grok-nfz-final finding 2. No number is claimed; none is earned.

### 5. Severity: residual — Claims (2) and (4) as artifacts. td-7 `D=4` is a theorem. All six CE orders are dead. CE3 replays exactly, including the congruence that forces `den(α_*)=13566`.

- File: `NF-D.md:9-25,154-165,175-192,234-246`; `cases/nfd_check.py` blocks A, C, E; `TOWER-9-15.md:229-244`; `cases/towers/t9_15_direct.json:729`
- Claim: td-7 pin `Π=11305`, `Ω=4`, 15 odd multisets, max depth 4; every CE order violates at least one promoted boolean; CE3 has `den(α_*)=13566` in both orders and first-atom `k=39270 | P` vs `k=87297210 ∤ P`.
- How checked.

  **td-7 pin, independently.** Certificate row: “nu-product is forced to 11305 (odd) by the f-degree ladder `2→22610`.” `TOWER-9-15.md:237-239` is the same identity. Chain-1 is frozen at `(μ,w,M)=(1,2,1)` (`BOOK-OFFAXIS.md:522`), so `P=i_G·μ=22610` and there is no μ-hole on this packet. `11305=5·7·17·19`, `Ω=4`. `2·11305=22610`.

  **15-multiset menu, independently enumerated** (Bell number `B_4=15` on four distinct primes; every part a product of a block, hence `≥5` and odd):

  ```
  {5,7,17,19}
  {5,7,323}, {5,17,133}, {5,19,119}, {7,17,95}, {7,19,85}, {17,19,35}
  {5,2261}, {7,1615}, {17,665}, {19,595}, {35,323}, {85,133}, {95,119}
  {11305}
  ```

  `323=17·19` is present (CE3’s depth-lowering grouping). Max length 4, attained only by the fully split word. Any word of depth `≥5` has `Ω(Π)≥5>4` and cannot multiply to 11305; the exit is permanent by M1. `D(td-7)=4` is earned. (All 15 parts are distinct, so the ordered census is `4!+6·3!+7·2!+1=75` words; the document’s “15 multisets and their orderings” is the right finite set.)

  **CE3, independently, exact `Fraction`.** Interleave `Z=(3,5,7,9,11)` at `P_0=2` with the td-7 skeleton `{2/5, 1/34, 3/3230, 2/11305, 1/13566}`, start `α=3/2`. After G at `θ*=1/13566`:

  ```
  den(α_*) = 13566 = 2·3·7·17·19     in BOTH orders
  P after Z = 20790 = 2·3³·5·7·11    (no 17, no 19)
  ```

  The numerator of `ℓ+1−1/13566` is `13566(ℓ+1)−1 ≡ −1 (mod 2,3,7,17,19)` for every integer `ℓ`, so those primes never cancel. That is a proof, not a lattice; the gate’s `ℓ=1..5000` scan is weaker than the document’s congruence and both hold.

  Free tails, entirely below `1/13566`, equal `I` (same `τ`, `Z`, `u_r=17`, `Π_free=1070745`, all-odd classes):

  | tail | first `k` | `k | P_1` | `13566 | 20790·u_1` |
  |---|---:|---|---|
  | `(323,13,15,17)` | **39270** | `[T,T,T,T]` | yes |
  | `(13,15,323,17)` | **87297210** | `[F,T,T,T]` | no (`270270 % 13566 ≠ 0`) |

  First-atom μ-boolean `P_1(α_*-1)∈ℕ` flips the same way. Both orders miss the pin (`20790·1070745 ≠ 22610`). Gate A1–A5 and E3.

  **CE1 / CE2, independently.** CE1: `2·945=1890≠22610`; first gap `2/3` lies in `(2/5, 5/2)`. CE2: `30002·1155≠22610`; prefix-δ at `g=7/3`, `w=2` is `[F,T,T,T]` vs `[F,F,T,T]` (atom-2 flip; atom-1 fails in *both* orders because `3 ∤ 30002·5` — §6’s “order A: pin only” is slightly thin, not false). All six orders are dead. Consistency with NF-D, as the document says, not a proof beyond §4’s slice.

  Closed NF-Z record: the header correctly withdraws the SD-conditional exchange, records CE3, keeps the in-zone core / `Z` / `L*` / `θ*` / Z1–Z3 / fail-closed policies, and points at `NF-D.md`. That bookkeeping is honest.

---

## Attack scorecard (this round)

| attack | result |
|---|---|
| (1) M1: `Ω` rises by `≥1` per (2.5) letter, every order | **true.** `P'=Pu` is the cylinder law; `Ω` additive |
| (1b) permanence: no letter decreases `Ω` | **true on the slice.** Exit from a finite `S` is permanent |
| (1c) rescaling letter (`p·dp/l`, `ν=1`, `PURE_B`) drops `Ω` | **not in slice.** `ν=1` is flat (NF-P); reduced-`dp` can stall on `M≤3`, never drop; actual (2.5) does neither |
| (2) td-7 `Π=11305=5·7·17·19`, `Ω=4`, 15 odd multisets, max depth 4 | **true.** Independently enumerated; pin is a certificate row; chain-1 has `μ=1` |
| (3) 11-A `v_2(2Π)=1` vs `≥3` | **true as the promoted resonance certificate.** **Not a pure-neutral `S`.** D4 is `1<3` hardcoded |
| (3b) 11-B `v_3(2Π_1)=0` vs `v_3(6Π_2)=1` for all domain stacks | **true as raw-`P`.** **False as H8.** `μ=3` equalizes; `Π_1=Π_2` is an infinite class |
| (3c) 11-C `v_2(2Π_1)=1` vs `v_2(4Π_2)=2` | **true as raw-`P`.** **False as H8.** `μ=2` equalizes (Class A) |
| (3d) therefore `D=0` on all three td-11 entries | **no.** `S` is infinite (reading A) or the live family is OB2 (reading B) |
| (4) CE3 `den(α_*)=13566` forced; `k` 39270 vs 87297210 | **true**, both orders; congruence is a proof |
| (4b) all six CE orders DEAD | **true.** Dead-from-dead; consistency only |
| (5) OB2 fail-closed = KEEP, sound for emptiness | **policy yes** (Rule 6). Direction is right. Trap is finding 1, not OB2 |
| `python3 cases/nfd_check.py` | exit 0, **19/19 PASS** (document matches) |
| M2 / N-closure / in-zone `L*` / `θ*=1/13566` | **still true** (cited, not re-proved) |

---

## What may be treated as proved, today

1. Cylinder (2.5) degree law `P'=P u` (`u≥2`), M1, permanence of exit from a finite scale set, `r ≤ Ω(Π)`. Gate B. The rescaling hole does not fire on this slice.
2. **Theorem NF-D on a mechanism-A entry:** if a certificate pins `P_r` to a finite `S`, live synchronized (2.5)-depth is `≤ max_{s∈S} Ω(s/P_0)`. td-7 direct: `S={22610}`, `Π=11305=5·7·17·19`, `D=4`, complete 15-multiset menu, 75 ordered words. Chain-1 `μ=1` makes the pin μ-clean.
3. M2 / N-closure: window-zone runs of length `≥2` die against `k|2`. In-zone `L*` and `θ*=1/13566` survive from the closed NF-Z record.
4. CE1–CE3, all six orders, are dead. CE3’s register / cap / μ flip is a theorem (and is why the quotient program closed). Consistency with a depth cap, not a substitute for `S`.
5. OB1 is an honest port obligation. OB2’s *direction* is Rule-6 correct (KEEP; no emptiness from an unproved cap). NF-Z.md as a closed record is labelled honestly.

Everything else — `D=0` at td-11, mechanism B as a general producer of finite `S`, “kills deep neutrals at td-11 outright”, a compiler that emits an empty synchronized-leg panel from D2–D4, the status line as written — stays `OPEN`.

A repair that would earn the printed status would have to (i) case-split mechanism B on `μ | M` (at least `μ=1` and `μ=M`), recompute `S` as the set of `P` for which `P/μ` can match, and either exhibit unsat of *that* system or produce the actual (typically infinite) residue class and fall through to OB2, (ii) move the 11-A resonance row out of the pure-neutral instance table and back to the promoted certificate, (iii) put `μ`-aware empty-stack and `Π=5` rows into `nfd_check.py` D, and (iv) keep M1, the td-7 menu, CE3, and the OB2 keep-direction, which are the parts of round 1 that survive.

Until then the compiler-useful theorem is: *enumerate the 75 td-7 synchronized words; do not discard synchronized neutrals at td-11; keep non-synchronized words on the fat record.* That is a smaller pivot than the one written, and it is the one the arithmetic supports.
