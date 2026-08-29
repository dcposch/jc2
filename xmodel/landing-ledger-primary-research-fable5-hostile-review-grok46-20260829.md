# Hostile review: Fable5 LANDING-LEDGER primary research (2026-08-29)

Reviewer: Grok 4.6, independent adversarial mathematical referee.
Subject: `xmodel/landing-ledger-primary-research-fable5-20260829.md`.
Date: 2026-08-29 (UTC).

Sealed-body verification (computed this session, SHA-256):

- full file: `26bdd150a5a4bace23069b65f3234de6080fc7fb083f46a92773ec276a6fc689` (match);
- body above the self-hash line: `83fe23123f35275e551ef8d1704da1181dea9c346a4915cd0e15c6db82998700` (match).

Authoritative comparison sources, read in full at the cited sections and used at statement level only: `ladder/REDUCTION.md` Critical 4--7 together with T6--T10, the §2 dependency ledger, and §5.1--§5.2; `ladder/SHEET6-DEPTH.md`; `ladder/SHEET6-MULTIPOLE.md`; `ladder/BOOK-OFFAXIS.md`. No other ideation report was opened. No `jc2-lean` access. No web, AWS, heavy/local CAS, canonical edit, commit, or push. Local computation was exact integer/`Fraction` scratch arithmetic on formulas printed in those four ladder files and in the sealed body.

This is an audit of claimed derivability, grammar totality, and the `td=6,m=2` hand-run. It is not stylistic commentary, and it does not extrapolate to JC2, a landing theorem for all `td`, or a degree ceiling.

---

## 0. Verdict

**REPAIR_REQUIRED.**

The compiler interface (typed family records, fail-closed three-way partition, cap-to-`UNCOVERED`, provenance keys, and the Section 7 firewalls) is the right object for REDUCTION Critical 4 items 2--5. The `td=6,m=2` *arithmetic* that the hand-run actually computes --- entry pin, `W(2)={2}`, root-meet death, ZCH unreachability, unique IIa cell, first post-jump P0 step, and both terminal budgets --- is correct and is promoted-safe. The packet as specified is not.

The load-bearing error is that Section 5.4's unique `UNCOVERED` family is not uncovered. It is a `nu=1` re-parameterization of MULTIPOLE D9's even-`l` family I, already killed td-uniformly by the exact log-obstruction. The "schema addition" that makes the family representable (`eps_q` as a degree slot at `nu=1`) is what hides the identification. Acceptance test A2 then *requires* a nonempty `UNCOVERED` list containing that family, so a compiler that applies D9 as written fails the packet, and a compiler that passes A2 has compiled the author's residue rather than the promoted perimeter. The recommended "one-page extension of the td-7 zero-chain law" is the wrong lemma: `dp|dq` is real in this family, but the td-7 equivalences `M=dp <=> kbar in {3,4}` already fail for every cell with `l>=5`, and the cheap discriminator is D9 itself.

Do not build LL-1 against A1--A5 as printed. Repair the `nu=1` grammar, retract the 5.4 `UNCOVERED` row and the named-lemma handoff as stated, and rewrite A2/A4 so a correct D9 discharge is a pass rather than a failure.

---

## 1. Schema sufficiency

### 1.1 What is actually derivable

The deleted-field table in §2.2 is correct *once a shape is known*.

- **`M = gcd(dp,dq)`.** Prop 8.1(v), used as MULTIPOLE D6(d) and R2.2(D). At entry, `(deg p, deg p_g)=b(alpha,beta)` gives `gcd(b alpha, b beta)=b` (MP4/D4). After a jump or dirty step the child `M` is the gcd of the *child* shape, not a transport of the parent `M`; that is why R3 must record a `V_2`-escape rather than invoke St 8.5. Retaining `shape` and deriving `M` is the right direction. The S-EDGE invariant `mu_e | M(parent)` remains checkable because edges retain full parent frames.
- **`rho = kbar/dq` after entry.** DS2 R4 / R1.2 / R1.4 give `kbar = rho * (own dq)` on chain transports. At a merge, Prop 9.3(b) is the consistency `X/kbar = dp/dq`, and the i-normalized coordinate is `rho = X/dp`, hence `rho = kbar/dq` tautologically on any cell that has already been solved. The entry clause `rho=a/b` is correctly *not* rewritten as `kbar/dq` (entry `q` is not the pole's `p_g`). Baking the identity into COVERED frames is safe. Baking it into an `UNCOVERED` mixed shape with unknown `dq` would be circular; R4's mixed residue, which refuses to emit a fake `M_G` menu, avoids that.
- **`w = (kbar-rho)/nu` and `X = kbar*dp/dq`.** Definitions. Downstream kills that quote a `w`-alphabet, `X>0`, or a root window `w<1` are views of `(kbar, shape, arrangement)`.
- **`psi = ceil(1/(1-w_G))-1 = ceil(M/j)-1` with `j=M(1-w) in N*`.** BOOK-OFFAXIS P1 / Prop 9.3(k),(m). Needs a terminal `w`, which is a view. The two surviving post-jump terminals in §5.5 have `j=1` and do not stress the formula.
- **`Lambda_i = a_i b_i alpha beta / nu_i`.** Prop 5.6 (19). Header-only; correctly deleted from the mutable frame.

Retaining `kbar` as the transported primary and `shape` as the merge unknown is the correct minimality direction for every COVERED rule in the table. Full parent/child frames on S-EDGE are what make later merge handshakes not need a stored `w` or `X`.

### 1.2 Attacks that survive

**(a) `eps_q` as a degree slot at `nu=1` is a false quotient.**

R1.0 forces `eta || q` only for `nu>=2`. MP6(c) says the eta-factor is *absorbed at `nu=1`*: `q = eta * rad(p) * extras` is the `nu>=2` normal form, and at `nu=1` the point `0` is an ordinary point of the line, not a cyclic orbit. Consequently, whether `q(0)=0` is a location predicate on the extra roots of family I, not an independent increment of `dq`.

Fable's merge grammar writes `dq = (r0+k+l)nu + eps_q` with `eps_q` free in `{0,1}` at `nu=1`. That splits one MP6 family-I cell `(dp,dq)=(r, r+L)` into two records `(l, eps_q=0)` and `(l-1, eps_q=1)` with the same degrees. The later ODE, log-obstruction, `M=gcd(r,L)`, and handshake depend only on `(dp,dq,w)`, which the split duplicates. This is exactly the failure mode the charge asked for: a later equation (D9) needs the identification the proposed quotient deleted.

At `nu>=2` the `eps_q=1` slot is not extra --- it is R1.0. The schema addition is load-bearing only in the one place it is wrong.

**(b) `arrangement` / `zero_dir` do not encode a free 0-root.**

The stored arrangement is "which arriving edge (if any) is the 0-direction." That distinguishes case II from case III. It does not distinguish a free 0-root of `p` (`eps_p>=1`, no arriving 0-chain), which P2 prices separately and which R2.2 puts in the shape. Packet 1 is saved by MP6(a): some `mu_e=1` forces `k=0` and every p-root to carry a chain, so a free 0-root cannot occur in the generated `td=6,m=2` interior. The field is insufficient for the mixed residue that R4 already marks `UNCOVERED`; that is honest only if mixed packets do not later treat `arrangement` as a complete 0-slot ledger. Shape's `eps_p` currently carries the missing bit; keep it there, and do not claim arrangement alone derives the case-III *versus free-0-root* handshake form.

**(c) `w_cert` is load-bearing, and §5.5 mislabels it.**

The mixed-root window (BOOK-OFFAXIS header 2026-08-28; DEPTH 5d) really does require a certification status: a `W-SYMBOLIC` inner-merge arrival must not fire R7. That justification stands. The schema lists `W-PRICED(P0,budget)` while R7's kill set is `{W-CLOSED-FORM, W-PRICED-complete}`. Those are not the same token. Worse, §5.5 stamps the IIa child `(w,M)=(3/2,2)` as `W-PRICED(P0)`. That `w=3/2` is the DS4/R4 handshake of two `W-CLOSED-FORM` arrivals against a determined cell, not a P0 dirty step. P0 starts on the *suffix*. For packet 1 the mislabel does not fire R7 (the root arrangement is already dead on the parent `w=2`). It will matter the first time a post-jump `w` is fed to a later root or mixed-root rule. Repair: merge-child `w` from all-`mu=1` DS4 is `W-CLOSED-FORM`; P0-priced suffix states are `W-PRICED`.

**(d) `M` after jumps is not an extra stored integer, but R1/R2's printed child formulas must not be used off the clean axis.**

R1 writes `M_child = gcd(l*nu, nu+1)` and R2 writes `gcd(l, n*nu+1)`. Both are the clean-shape gcd. After a `V_2` dirty step, `M` is `gcd(dp,dq)` of a different shape and need not divide the parent (St 8.5 inapplicable, as R3 says). Deriving `M` from `shape` at every vertex, rather than transporting those two formulas, is mandatory. The schema as designed permits this; an implementer who caches the R1/R2 lines as the definition of `M` will reproduce the refuted `W_off` alphabet (BOOK-OFFAXIS §8 Step 2, L2 autopsy). A4's `l`-vs-`M`-state mutation tests the entry-conflation, not this post-jump cache.

**(e) `psi` is a terminal view, not a running state.**

Correct. Equality routes in R9 are `FRAGILE` because `psi` can only increase if a new printed unit appears. No deleted field is needed to express that.

**(f) Zero-direction provenance is enough for packet 1, not as a general case-tag oracle.**

The derived case tag (II at non-0 `V_1`, III at 0-edge `V_1`, I at `V_2\V_1` including genuine root merge, IV at a non-`V_2` root endpoint) matches DEPTH 5c--5d and BOOK-OFFAXIS R2. `V`-membership derived from `(nu, merge?, root?)` is the right rule provided `nu>=2 => V_1` (Not 3.4) is not applied to a `nu=1` merge child. Packet 1's admitted child has `nu=3`. The `UNCOVERED` family, had it been live, would have been a `nu=1` case-I vertex whose first downward step is *not* R1 as written (R1 is case II). That is a further reason not to leave the family hanging as a suffix problem.

**(g) Equal-`mu` equal-`w` joins do not supply a third unbounded stored coordinate.**

§5.6 lists "kbar at equal-`mu` equal-`w` joins, a free parameter pre-integrality" as an independent unbounded direction. R2.1 plus `X/kbar=dp/dq` pins

    kbar = mu * w * dq / (mu*dq - dp)

and at `mu=1` this is DEPTH 5a's `kbar = w*dq/Del`. Once the cell is chosen, `kbar` is not free. Integrality/`kbar in Z` at `nu>=2` then finite-izes the cell list (DEPTH 5b). The unbounded axes that remain are depth, per-step `nu` on neutral edges, and whatever mixed-shape parameters sit in R4's `UNCOVERED` residue. Overstating a free `kbar` field would tempt an implementer to store a quantity the merge solve already determines.

**(h) Mixed later merges do not need a field the quotient deleted, except the `nu=1` identification.**

For `m=2` there is only one merge (MP1: `Sum(r-1)=1`). There is no downstream mixed merge in this packet. Generally, a later all-`mu>=2` merge needs parent `(kbar, shape, mu, zero_dir, w_cert)` --- all retained --- and a shape grammar whose `k>0` / `eps_p>0` emission menu is exactly the thing R4 refuses to complete. That refusal is correct (BOOK-OFFAXIS §3: the 700 mixed skeletons used `M_G | Sum mu_e` only on `eps=0,k=0`; omitted `k>0`/zero-root degrees are OPEN). It is not a deleted-field problem.

### 1.3 Schema verdict

Minimal-sufficient for every COVERED packet-1 transition, with three repairs: (i) at `nu=1`, `eps_q` is a location flag or is normalized away before classification; (ii) `w_cert` tokens in S-VTX, R7, and §5.5 must coincide, and the IIa child is `W-CLOSED-FORM`; (iii) `M` is always `gcd(shape)`, never a cached R1/R2 line. The declared additions `w_cert`, `arrangement`/`zero_dir`, `sym_constraints`, `H5a_reading`, and `cert_chain` are otherwise justified at the cited loads.

---

## 2. Grammar and the three-way classifier

### 2.1 Total typing versus finite enumeration

Section 4's `classify` is total as a *typing of `Cand(s)`*: every generated candidate is `COVERED`, `TERMINAL`, or `UNCOVERED`, and a cap may not reject. That is the exact repair Critical 4 item 5 and the sol56 "emit OPEN rather than omit" wording asked for. It is not a proof that `Cand(s)` equals the geometric fibre of full configurations, and it is not a decision procedure that enumerates infinitely many depths.

Section 6.1 states this distinction and is right to refuse both pure state enumeration (DEPTH DS1 R1: depth is not bounded by `(m,td)`) and a pure symbolic frontier that would discard DS3/DS4 and P0. Parametric family records with a symbolic frontier *at genuine `UNCOVERED` classes* is the correct representation.

### 2.2 Completeness of `Cand(s)` at this header

For `td=6, m=2, b=(1,1)` the promoted generators are:

- chains: MP5, single simple `nu`-orbit, `nu>=2` (DS1 / St 3.16 iff). R1's negative control against `nu_child=1` chain children is the recorded twopole over-generation. Complete on the axis.
- interior merge with some `mu=1`: MP6(a)--(e), families IIa / ZCH / I, plus the ZCH case-III handshake (DEPTH 5c). Complete as a *shape list*.
- root meet: case I, all-`mu=1` formula `w=l/(r+l)` (DEPTH 5d) and the mixed-root window (no `mu=1` hypothesis, but here `mu=(1,1)` anyway).
- mixed all-`mu>=2`: not generated, because `mu_e | M=1` (St 8.4 + MP5). R4's mixed `UNCOVERED` residue is unreachable, not silently covered.
- off-axis: empty at `td=6` (BOOK-OFFAXIS §4). Not inherited.

The grammar citations "R1.0 / St 3.18 / Prop 9.3 case list / MP6-R2.2, review-confirmed in BOOK-OFFAXIS Sec. 6" overclaim. BOOK-OFFAXIS §6 is Lemma R1 (q-rigidity and off-axis transport). It does *not* certify an independent `eps_q` degree slot at `nu=1`. Prop 9.3's case list I--IV is a partition of edges, not a partition of pattern degrees.

Fable does **not** silently mark the known-open mixed/off-axis families `COVERED`. That is a pass on charge (2)'s mixed/off-axis test. What it silently inherits is MULTIPOLE's *engine cap* on the `nu=1` eta-variant (MP9, §4 "Engine caps"), promoted into an `UNCOVERED` row, in conflict with D9's already-uniform even-`l` kill of family I (Section 3 below). That is an inherited *open tag*, not an inherited open geometric family.

### 2.3 Totality of the configuration-to-record map

LL-Soundness+Totality clause (1) requires every configuration in `CFG` to map to a unique leaf. At this header `CFG` is infinite in depth and in per-step `nu`. Mapping to a parametric family with a DS3/DS4 closure certificate is the only honest totality. Fable asserts that, and also asserts that grammar-completeness is "a theorem, not the enumerator's loop bounds." The second sentence is the one that fails: the `nu=1` split is an enumerator parameterization, not a theorem, and it is what produces the extra leaf.

Single-pole composite configurations (REDUCTION HIGH 1) are out of packet 1 by design. That is a packet boundary, not a totality proof for `CFG` at `td=6`. The Section 7 realizability firewall correctly forbids reading an empty `ALIVE` book as a `td`-exclusion.

---

## 3. Recomputation: `td=6, m=2`

All identities below are exact `Fraction` arithmetic.

### 3.1 Entry (R0)

`m=2`, `td=6` forces `Lambda=(3,3)`, hence type `(alpha,beta)=(2,3)` (`Lambda_i >= beta >= 3` and `Sum Lambda = td`). `Lambda=3` is prime and beta-minimal, so `b=1` (MP4). Mass `Lambda = 6 a b / nu = 3` gives `nu = 2 a b`. T7: either `nu|2` and `nu|b*3-1`, or `nu|3` and `nu|b*2-1`. With `b=1` the second branch is `nu|1`, so `nu=1`, then `2a=1`, impossible. The first branch with `nu=2a` and `nu|2` yields only `(a,b,nu)=(1,1,2)`.

Off-axis sector empty (BOOK-OFFAXIS §4). Entry menu has one member.

    kbar = a(alpha+beta) = 5,
    M = b = 1,  rho = a/b = 1,
    w0 = a(b(alpha+beta)-1)/(b nu) = 2,
    w_cert = W-CLOSED-FORM.

Header `3+3=6` holds. Match to Fable §5.1.

### 3.2 Pre-merge chains (R1/R2)

`W(2)={2}`: no `Del>=3` divides 2, so no R2 step (DS3; DEPTH check 2). Every step is R1, `nu_j>=2`, `w` fixed. Frames `{(w,nu,kbar)=(2, nu, 2 nu + 2)}`. Depth unbounded by `(m,td)` (DS1 R1). Arrivals `mu=(1,1)` (MP5), `lam=0`. Match.

### 3.3 Merge partition

Root meet: both arrivals have certified `w=2>=1`. DEPTH 5d / mixed-root window: `X_R = mu(1-w)` forces `w<1`. `COVERED(R7): DEAD`. Match.

ZCH (0-edge): case III handshake `kbar - X = nu_e w_0`. Non-0 edge `X = kbar - w_other`. Join `w_other = nu_e w_0`. Sole value 2 gives `2 = nu_e * 2`, so `nu_e=1`, forbidden by `nu_e>=2`. DEPTH check 7 (403 solves, none joinable). `COVERED(R4): REJECTED`. Match.

IIa, `l` even or `nu` even: `M = gcd(2, l nu + 1) = 1` (product even, plus one odd). Interior `G*`, MP2 kills. Match.

IIa, `l` odd and `nu>=3` odd. Handshake `X = kbar-2`, `X/kbar = dp/dq` gives

    kbar = 2 + 4 nu / (l nu + 1).

`nu>=2` demands `kbar in Z`, so `d := l nu + 1` divides `4 nu`. But `gcd(d,nu)=1`, hence `d|4`. Now `d = l nu + 1 >= 4` and `d` is even, so `d=4`, `l nu = 3`, only `(nu,l)=(3,1)`.

    (dp,dq)=(6,10), kbar=5, X=3, M=2,
    Q=(D, deg p, nu, M, kbar)=(6,12,3,2,5) at i=2,
    w_trunk = (kbar - X/dp)/nu = (5 - 1/2)/3 = 3/2.

Spot checks `(2,5,1),(2,3,3),(2,7,1),(2,5,3)` all fail integrality, as claimed; the uniqueness proof shows they are not a sample from a cap. `COVERED(R4): ADMITTED`, exactly one cell. Match. This is already DEPTH §0/§6's exact nonroot menu.

Plain `nu_G=1`, `eps_q=0`: family I `(dp,dq)=(2,2+l)`, `M=gcd(2,l)`. `l` odd => `M=1` => MP2. `l` even => D9 log-obstruction, all even `l`, td-uniform. Match.

Mixed all-`mu>=2`: not generated. Match.

### 3.4 The claimed `UNCOVERED` family

Shape as written: `SHAPE_MERGE(nu=1, eps_p=0, mu=(1,1), m=[], l, eps_q=1)`, `l` odd `>=5`. Then `(dp,dq)=(2,3+l)`, handshake

    kbar = 2(3+l)/(1+l),  X = 4/(1+l) > 0,  M = gcd(2,3+l) = 2.

Instances match: `l=5` gives `(2,8)`, `kbar=8/3`, `w_trunk=7/3`; `l=7` gives `(2,10)`, `kbar=5/2`, `w_trunk=9/4`. Searrow, `gcd(M,nu)=1`, N1/L6, and P2 (no free p-root at 0; q-extras price 0) all pass. `kbar in Q\Z` is legal at `nu=1` (BOOK-OFFAXIS P3). `n_e = 4 nu_e/(l+1) - 2` can lie in `N*` (e.g. `l=5`, `nu_e=6`, `n_e=2`); stage-R policy correctly does not use i-sync/`n_e` as a kill, and the integer-`kbar` congruence is the wrong condition at `nu=1` anyway. No missing lambda bound kills the family. No missing admissibility bound kills the family.

**The log-obstruction does.**

Set `L := dq - dp = l+1`. For `l` odd, `L` is even, and `(dp,dq)=(2, 2+L)` is MP6 family I with extra-count `L`. The handshake is the family-I handshake: `kbar = 2(2+L)/L = 2(3+l)/(1+l)`. Slope `dp/dq = 2/(2+L)`. MP6(c) absorbs eta at `nu=1`: `q(0)=0` is the specialization `s(0)=0` in D9's writing `q = p s`, `deg s = L`. D9 never uses `s(0)!=0`. The residues that produce the log sit at the two p-roots, not at 0.

D9, interior `nu=1`, `l` even: `(iv)` reduces to `2 p s' - L p' s = c' != 0` with `rho=2/(2+L)`; divide by `p^{(L+2)/2}`;

    (s p^{-L/2})' = (c'/2) p^{-(L+2)/2},

residue at each p-root `C(-n, n-1)(a1-a2)^{1-2n}` with `n=(L+2)/2` and `C(-n,n-1)=(-1)^{n-1} C(2n-2,n-1) != 0` for all `n>=2`. For Fable's cells:

| Fable `l` | `(dp,dq)` | `L` | D9 `n` | `C(2n-2,n-1)` |
|---:|---|---:|---:|---:|
| 1 | (2,4) | 2 | 2 | 2 |
| 3 | (2,6) | 4 | 3 | 6 |
| 5 | (2,8) | 6 | 4 | 20 |
| 7 | (2,10) | 8 | 5 | 70 |

The `l in {1,3}` machine kills (l1_ode_check B/B-eta, `l<=4`) are instances of this same identity, not a separate finite certificate. Restricting their validity to two cells is what manufactures the `UNCOVERED` tail.

The same obstruction is visible in the eta-normal form `q = eta p s` (`deg s = l` odd) without translating back to D9's `L`. Slope `2/(l+3)`, `m=(l+3)/2 = dq/dp in N*`, integrating factor `eta / p^{m-1}`, and `sigma' = K / (2 p^m)` has simple-pole residue

    (K/2) * (-1)^{m-1} C(2m-2, m-1) (a1-a2)^{1-2m}

nonzero for all `m>=2` unless `K=0`, i.e. unless `⊖=0`. This is D9's binomial with `n` renamed `m`. It is not a new theorem.

MULTIPOLE §6 item 6 already says "ν = 1 interior jump at m = 2: dead at all l --- even l by the exact log-obstruction (all l, beyond L1b's caps), odd l by M = 1 + MP2; only the η-factor subvariant remains cap-limited (l ≤ 4)." The cap flag is an engine-parameterization leftover. DEPTH §0/§6 states the nonroot menu as *exactly* IIa `(2,3,1)` and treats `nu=1` cells `l in {1,2,4}` as a historical diagnostic, not as a remaining residue. Fable's classifier prohibition 3 is the right rule for a genuine cap. Applying it here reopens a D9-closed class.

Classification required by the promoted perimeter: `COVERED(R4+D9): REJECTED` for every odd `l>=1` in the eta writing, equivalently every even `L>=2` in family I, including `q(0)=0`. No `UNCOVERED` row.

### 3.5 First post-jump from `Q=(6,12,3,2,5)`

Trunk `(w,M)=(3/2,2)`. The state is the same `(3/2,2)` whose one-step P0 menu BOOK-OFFAXIS §10 records as complete. Recomputed:

- Neutral thick `l=2 | M`, `n=1`: `w` fixed; `M_child=gcd(2, nu+1)=2` iff `nu` odd; else `M=1` and R6 kills (nonroot trunk). Parametric, `COVERED(R1)`.
- Thin `l=1`: `M=gcd(1, nu+1)=1`, R6 `DEAD`.
- Clean resonant: `Del | num(w)=3`, `Del>=3` forces `(n,nu)=(2,2)`, `dq=5`, `den(w)=2` does not divide 5. BOOK-OFFAXIS §8 Step 2 filter, now used as a *negative* control, not as an M-descent. `REJECTED`.
- Dirty (A) `(21,15)`, `nu=7`, `l=2`: `E=9`, `kbar=5`, `w=2/3`, `M=3`, `lam>=2`. `V_2`-escape, `M=3` need not divide parent `M=2`. Match.
- Dirty (C) `(20,16)`, `nu=5`: `E=12`, `kbar=4`, `w=3/4`, `M=4`, `lam>=2`. Match.
- Dirty eps `(7,5)`, `nu=2`: `E=3`, `w=2`, `M=1`, R6 `DEAD`, `lam>=3` moot.
- Pure-(b) doubling `l=2, eps=1`: `w=3`, `M=gcd(1, nu+1)=1`, R6 `DEAD`.

Terminals: from `(2/3,3)`, `j=M(1-w)=1`, `psi=2`, budget `6-1-2=3 >= lam=2`, slack 1, `ALIVE`. From `(3/4,4)`, `j=1`, `psi=3`, budget `2 = lam`, `ALIVE+FRAGILE`. Direct R8 from `w=3/2` fails `w<1`. Match.

P0's claim that these four dirty cells *are* the complete extras/pure-(b) menu from `(3/2,2)` is inherited from BOOK-OFFAXIS's session enumeration (`E | l num(w) T`, finite per `(w,l)`). The four displayed cells were re-derived here; a full Diophantine replay of P0(i)--(ii) at this one state was not. Packet 1 may cite that completeness as a named P0 certificate, not as a fact proved in the sealed body.

The finite sub-boundary residue (at most one further priced unit from the slack-1 route; none from the equality route) is a real compiler obligation and is in scope for `m=2` (no later merge). This is the one place the packet strictly exceeds the marked-first-event theorem of T8, and it is legitimate at this header because the St 9.4 budget is `<=3` after `psi`.

---

## 4. `dp | dq` versus the promoted td-7 zero-chain law

Every cell of the eta writing has `dp=2` and `dq=3+l` even, so `dp | dq` and `M=dp=2`. That observation is true and was not in the prose audit of D9.

It is not a bridge to BOOK-OFFAXIS §11 as stated.

The promoted law is a closed-form T1 decision on the td-7 class-B/C *0-chain* book: with `mu = dp - nu` and `l = (dq-1)/nu - 1`, the reduced Prop 8.1(iv) admits an admissible solution with nonzero RHS iff `dp` does *not* divide `dq`, equivalently T1-DEAD iff

    dp | dq  <=>  (mu+nu) | (mu(l+1)-1)  <=>  M = dp  <=>  kbar in {3,4}.

On-axis ZCH `(nu+1)|l` is the `mu=1` specialization. Dual verification is for that reduced equation `(rho-mu)(t-A)s + ... = C` derived from an arriving 0-chain in *p*. Fable's family is `eps_p=0`, `eps_q=1`: a 0-root of *q*, not of *p*. The law "does not literally apply" is Fable's own caveat, and it is decisive.

The remaining equivalences already fail on the family Fable wants to kill with this lemma: `kbar = 2 + 4/(l+1)` lies in `{3,4}` only for `l=1` (`kbar=4`) and `l=3` (`kbar=3`). For every odd `l>=5` one has `2 < kbar <= 8/3 < 3`. So even a reckless transcription "DEAD iff `dp|dq`" would agree with D9 on this family, while the advertised mechanism-package (`kbar in {3,4}`, 0-chain `mu`, class-B/C) would not.

What *is* real: `dp | dq` is exactly the condition that the eta-normal-form integrating-factor exponent `(l+3)/2 = dq/dp` is an integer, which is why `sigma' = K/(2 p^m)` has the D9 binomial residue. That is a family-I fact at `nu=1`, `r=2`, `w=2`, not a specialization of the td-7 0-chain theorem.

**Exact additional hypothesis that would make a dp-divides-dq law apply here.** The reduced identity at a `nu=1` all-`mu=1` interior merge, written `q = p s` or `q = eta p s`, has `dq/dp in N*` (equivalently D9's `(L+2)/2 in N*` for even extra-count `L`). No 0-chain in `p`, no `mu = dp-nu`, no `kbar in {3,4}`.

**Cheapest theorem / discriminator.** D9 as printed, plus the one-line identification `(dp,dq)=(2,3+l) <=> family I with L=l+1`. Cost: the identification sentence and, optionally, the eta-normal-form residue as a negative-control rewrite. Not a named extension of BOOK-OFFAXIS §11, and not a prerequisite for LL-1.

A secondary discriminator, strictly weaker and not recommended as the closer: instance ODE at `(2,8)` (the smallest `l>=5` cell) in the same l1_ode_check family that already killed `(2,4)` and `(2,6)`. That would be another cap, not a theorem.

---

## 5. A1--A5 and packet ordering

A1--A5 are mandatory and fail the process on any failure. That is the right shape for a compiler packet. Their content compiles the sealed hand-run, including its error.

- **A1 (record parity).** The admitted interior menu `{IIa(2,3,1) -> Q(6,12,3,2,5)}` is the correct COVERED-ADMITTED set (DEPTH, and Section 3.3 above). Root DEAD and ZCH rejected are correct. "Plain `nu=1` rejected with the two named certificates" is correct for `eps_q=0`. Cross-check against 26 phase-4 shapes and 351/351 depth-invariance is a useful engine-parity gate and is not a completeness certificate (REDUCTION MEDIUM 2: the engines aggregate). A1 does not test that family I even-`L` with `q(0)=0` is the same cell as the eta writing.
- **A2 (fail-closed).** Requires the `UNCOVERED` list to be *nonempty* and to contain `eps_q=1, l odd >=5` with smallest instance `(2,8)`. This is the fatal test. A compiler that discharges D9 and emits an empty `UNCOVERED` list exits nonzero. A compiler that passes has frozen Fable's residue. Additional `UNCOVERED` rows "are findings, not failures" --- so the test is one-sided: it punishes closing the author's gap and does not punish extra gaps. Fail-closed totality needs the opposite: unmatched candidates must appear as `UNCOVERED`, but a candidate killed by a cited promoted theorem must not.
- **A3 (post-jump boundary).** The §5.5 table and both terminal arithmetics recompute. Snapshot-equality to that table will not detect a missing P0 cell that BOOK-OFFAXIS also missed; it will detect drift against the sealed run. Acceptable as a regression gate if P0 completeness is cited, not re-proved.
- **A4 (mutation battery).** The listed historical bugs are the right permanent tests (root-`M=1` kill, `l>=1` at root, case-IV at a genuine merge, case-II model of ZCH, equal-`mu` unequal-`w`, `l` vs current `M`, shared-suffix double count, equality-route extra unit, cap-as-rejection). Missing, and currently anti-tested by A2: family I even-`L` with `s(0)=0` classified `UNCOVERED`; `eps_q` degree slot at `nu=1` producing a duplicate leaf; merge-child `w_cert` stamped `W-PRICED`. The planted cap-as-rejection test will *pass* if the eta family is emitted `UNCOVERED`, which is the bug.
- **A5 (provenance).** Addresses REDUCTION MEDIUM 2 (no any-context aggregation, pole-id swap, append-only ledgers, `cert_chain` to a frozen snapshot). Does not check that the `l` q-extra of IIa `(2,3,1)` is in `unused_registry` as `NO_TREE_VERTEX` (MP6(e)/R4), nor that each R1 step records `nu-1` `DECK_CONJUGATE` slots parametrically. Those are cheap additions.

**Ordering.** "Build LL-1 against A1--A5; then send the `eps_q` zero-chain extension to the named-lemma queue; then LL-2 at `td=7`" compiles the answer the sealed body was told. The lemma is unnecessary for this sector; A2 makes the unnecessary lemma a gate. LL-2 remains the first header at which off-axis entry, dirty pre-merge steps, case-III/E5, and the 11a 17-versus-2 H5a books all fire, and that ordering (after a corrected LL-1) is still right. The Card B stop condition (bounded pass, freeze a large uncompressed `UNCOVERED` list and report its shape) is sound and is not implicated by the false single-row residue.

A design that compiles only the answer it was told is not a completeness certificate. A2 is that design.

---

## 6. Promoted-safe / quarantined / repairs

### 6.1 Promoted-safe (may be used by LL-1 after the repairs in 6.3)

1. `td=6,m=2` entry menu is exactly `(a,b,nu)=(1,1,2)` at both poles; type `(2,3)`; `kbar=5`, `(M,rho,w0)=(1,1,2)`; off-axis empty.
2. `W(2)={2}`; no resonant pre-merge step; reachable M=1 frames `{(2, nu, 2 nu + 2) : nu>=2}`.
3. Root meet `DEAD` by case I / mixed-root window on certified `w=2`.
4. Interior 0-edge (ZCH) `REJECTED` by the case-III ratio `w_other = nu_e w_0`.
5. Interior IIa admits exactly `(r,nu,l)=(2,3,1)`, `(dp,dq)=(6,10)`, `kbar=5`, `X=3`, `M=2`, `Q=(6,12,3,2,5)`, `w_trunk=3/2`. Uniqueness is `d|4` with `d=l nu+1>=4` even, not a sweep.
6. IIa with `l` even or `nu` even is `M=1`, MP2-dead.
7. Family I at `nu=1` (`(dp,dq)=(2,2+L)`): even `L` dies by D9, all even `L`, td-uniform, including `s(0)=0`; odd `L` dies by `M=1` and MP2.
8. Mixed all-`mu>=2` is unreachable at this header (`mu | 1`).
9. First suffix step from `(3/2,2)`: the R1/R2/R6 lines of §5.5, the four displayed P0 dirty cells with the stated `(w,M,lam)`, and the two terminal budgets `psi in {2,3}` with slack 1 and equality. P0 *completeness* of that dirty menu is cited from BOOK-OFFAXIS §10, not re-proved here.
10. Section 7 firewalls: no ledger certificate into `G2-PSC`, `G2-BD`, `RPMC(C)`, or a cofinal `td` ceiling; `ALIVE` is a conservative superset; trust-perimeter changes invalidate only citing records.
11. Fail-closed architecture: unmatched candidates are `UNCOVERED`; caps are not rejections; records are keyed by full S-HDR plus path; `ALIVE`/`DEAD` is orthogonal to `COVERED`/`UNCOVERED`.
12. Representation: parametric families with a symbolic frontier at genuine `UNCOVERED` classes.

### 6.2 Quarantined (must not be consumed)

1. Section 5.4 `UNCOVERED(h)` for interior `nu_G=1`, `eps_q=1`, `l` odd `>=5`.
2. The claim that this is the sector's only open family, and that "menu = exactly IIa(2,3,1)" is a capped record rather than a theorem.
3. The candidate closing lemma as an extension of the td-7 generalized zero-chain law (BOOK-OFFAXIS §11 / 11a), including any implication that `kbar in {3,4}` or `mu = dp - nu` governs these cells.
4. `eps_q` as an independent degree slot at `nu=1`; the claim that this slot is the schema addition which makes the family representable.
5. A2 as printed (nonempty `UNCOVERED` list containing that family).
6. Grammar-completeness as a totality theorem covering the `nu=1` eta writing, and the citation of BOOK-OFFAXIS §6 as that certificate.
7. `w_cert = W-PRICED(P0)` on the IIa merge child.
8. "Three independent unbounded directions" including a free pre-integrality `kbar` at equal-`mu` equal-`w` joins.
9. Any reading of packet 1 as a full-configuration book for all `td=6` configurations (single-pole composite remains HIGH 1; realizability untracked).
10. MP8 equality/(22)/(22-cl)/no-refinement rhetoric; literal St 9.4 equality as a kill (R9 already quarantines this; keep it).
11. Off-axis mixed-merge emission completeness; H5a 17-versus-2 books; anything at `td=7`. (Correctly deferred, but not to be filled by the quarantined lemma.)

### 6.3 Minimal repairs

1. **Grammar normalize.** At `nu=1`, either drop `eps_q` from the degree formula (`dq = r0+k+l`) and record `q(0)=0` as a location flag, or identify `(l, eps_q=1)` with family I at extra-count `L=l+1` *before* `classify`. Keep `eps_q=1` forced at `nu>=2`.
2. **R4 table.** Replace the 5.4 row and the `l in {1,3}` machine-only row by a single family-I line: even `L` => D9; odd `L` => MP2. Machine B/B-eta becomes a negative control that D9 already covers, not a finite kill.
3. **A2.** `UNCOVERED` may be empty. Every remaining `UNCOVERED` row (if any) carries `h`, smallest instance, and blocked consumers. Failure is a generated candidate that is neither classified nor emitted `UNCOVERED`, or an `UNCOVERED` row that a cited promoted theorem already kills.
4. **A4.** Plant family I with even `L` and `s(0)=0` (equivalently Fable's `(2,8)`); the compiler must emit `DEAD`/`REJECTED`, not `UNCOVERED`. Plant a cap-as-rejection on a *different* genuinely capped locus if one remains.
5. **A1.** Keep "admitted exactly IIa(2,3,1)". Drop any implication that eta `l>=5` is outside that completeness statement.
6. **Retract the named-lemma handoff as stated.** If a one-pager is still wanted, its title is "D9 applies to `s(0)=0` / eta-normal form at `nu=1`", and it is not a dependency of LL-1. Do not queue a td-7 §11 extension for this sector.
7. **`w_cert`.** Unify the token list; stamp the IIa child `W-CLOSED-FORM(DS4)`.
8. **Do not implement LL-1 against A1--A5 as printed.** After 1--7, LL-1 is still the right first packet; LL-2 at `td=7` remains the first off-axis/H5a packet.

---

## 7. Scope notes the sealed body got right

Critical 4's missing object is a typed configuration-to-record map with unused-branch provenance and fail-closed coverage. The LL interface is that object. Critical 5 (off-axis completeness) and the mixed emission menu are not claimed solved. Critical 6's post-jump hole is addressed at *this* header by a budget-bounded suffix after a single merge; that does not extend to `m>=3` later mixed merges or to `td>=8` where BOOK-OFFAXIS P5 already says budget cannot close panels. Critical 7 / cofinal ceiling is firewalled. No output is a `G2-PSC` or `G2-BD` estimate. `ALIVE` is not a counterexample. Those separations survive the repair.

The hand-run's correct arithmetic (Section 3.1--3.3, 3.5) is the right A1/A3 oracle once A2 no longer contradicts D9.

---

## 8. Verdict restated

**REPAIR_REQUIRED.** Promoted-safe core: unique entry, `W={2}`, root death, ZCH unreachability, unique IIa `(2,3,1) -> Q(6,12,3,2,5)`, first P0 suffix step, both terminal budgets, fail-closed architecture, firewalls. Quarantined: the 5.4 `UNCOVERED` family, the td-7 zero-chain "closing lemma", the `nu=1` `eps_q` degree slot, and A2 as printed. Minimal repair is D9-identification plus acceptance-test inversion, not a new named lemma and not a rebuild of the compiler shape.

No JC2, landing, or ceiling claim is licensed by either the sealed body or this review.

---
Report-body self-hash (sha256 of every byte above this line): 88c1d66f09314e8717234b8617da84cd78a7fe95da90b31a120721272d678e79
