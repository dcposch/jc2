# 0310 critical full-round blind: Fable 5.1 seat

Report: `xmodel/ideation-20260909T0310Z-fable5.md`. Lane `/tmp/jc2-lane.vTMuDp`. Frozen basis `0d39df3c9fd69c939a8420c54d03228b9077777d` (provenance only). Mathematical freeze 2026-09-09T03:10:37.217561Z; `ROOT-FINAL-MANIFEST.json` authoritative (final selection 03:16:06.538076Z).

**Actual start 03:30:50 UTC** (first command, after root's invitation release citing its sealed blind 03:29:24 UTC). Common absolute blind deadline 04:20:00 UTC. External-author lane custody; no artifact transaction, no `charge_basis` (no exit price is asserted or consumed).

**Tool boundary honoured:** zero mathematical subprocesses; only `cat/head/tail/sha256sum/date/ls` and one stdlib JSON metadata comparison of lane hashes against the manifest. Every derivation below is factored hand reasoning. No peer body, live gate, `.log`/`.run.v2`, root blind, all-D gate, uncharged local link, AWS, web, agent, or protected project was read or touched. The root 0310 blind `ideation-20260909T0310Z-coordinator.md` exists in `xmodel/` and was NOT opened.

## 0. Read scope and pins

All 32 charged files in `/tmp/jc2-lane.vTMuDp/inputs` were read WHOLE (two oversized files in two byte-halves, boundaries re-joined). `sha256sum` of the 32 lane files matched every manifest `sha256` for the 31 charged entries (0 mismatch, 0 missing, 0 extra) before any body was cited below. Generated pin table (sha256, basename):

    8575b68fcf482bcdd27733069d5057ccfd549074133ac6d58cd292de10e27685  ROOT-FINAL-MANIFEST.json
    9119b224b4af23f4b8fc8dd6ceea29f37cc9c58d4138c7527e42379cbab9765e  accepted-15q-through-15v.md
    c9a399a87dc91d78bfc4f811249996ea3e217eda075be679cf27b41af5795c26  accepted-15s-gate.md
    b541308788da31f52e9f7985c7767e206231e8f3251ff53c1b2bd9c96b64f097  accepted-15s-proof.md
    cc5f4ca64fef11197c84e6d19b6bc8b5c3d526adac05cb66b28d94573144525b  accepted-15t-gate.md
    1620f9ef6b2edc598d35cab274cdfcc24d71353d18132d3a35ffb59fd2c46099  accepted-15t-proof.md
    f3ab28a6b26345cfd4ce2bd74cf77a335acdf7865c650a4662964a2e738edc08  accepted-15u-contact-cover.md
    0d1d2e7ce9393f4fe316cf62521a7d5c963db7876117be83f4221e6c81e6da4f  accepted-15u-gate.md
    0ec157b262e8658e493b98ff0776bce4603cb8aa1b731fc93f38e58372637d83  accepted-15u-three-simple.md
    fb281624a480b34c8950e45035a141f43ae1af137fbdc3d86f1ce541899336dd  accepted-15v-gate.md
    7709b0da88c6fa42fcbea38b9209573855edb1d6167c2cb77c1f8e374a5d1368  accepted-15v-proof.md
    eade8ec8b9b9162bf3a6a9e60408094185b63b633e6343cce11b7e233e904284  actual-moh-source-gate.md
    07e53340002c48b29a97d567ceb9eb867a292e9cbdd932ce7f508e0694875c46  actual-moh-source.md
    d46f037fb89ce8a1eeffb0bcb0bb4047c11294a030d8d2d332165e39c85e60f0  approaches.md
    8a09ca2a1da7083582221a1f9d5d95c97e834cd057b46a3c1d82961a5118095f  audit-guide.md
    f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8  binding-bd-gal.md
    874b613c1b9bccaf697c78b4ee4aa657442136ed298f5887363c448f056410d8  coordination.md
    e97b254a0615cd583ac657cdf2a2ab0e11096f3f7a3d2c5ed6d56e690c8d1d3b  last-0040-synthesis.md
    ddf449017f34fd65f70d34085566e50221904c257fc1903edd65ef8051a9f8fb  last-0040-transaction.json
    364431f6267629e2f45e49785b18bf6393f4a9b4f2b59b4d3ee47047a70440dc  last-broad-sweep.md
    98aa0563d9bff343bb1625500e7f231ac2f0f3771c09582fbede6aca62f9dd7f  latest-live.md
    c235fca15b48d29860291e26b7c8056915110deb1a9dc15b7ff1a20926d8d4ac  master46-history.md
    7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413  minimal-receiver.md
    265632079f612afd77fda39b63310d82b836cb888abdfd5267717e6e20bd18ef  progress-sep9.md
    857b2e2fa93cc14acb24fa590a2ffa76961a0d136113908f12b213e126889672  provisional-allD-descent.md
    2dcff1644acdc77a4665916d71dd4865b6f8f35d0965fb43ece6dd3c671393fa  provisional-allD-direct.md
    8f8403bed0950dec54ab78d1ba5fdd0ac1dcb9e586bd3a181ada0b67c7c07ea1  reduction-interfaces.md
    0c5270a432a6336c17c4693034e36cb496f139c3267843e3ac06628ec8c4b255  remaining-m90-source-interface.md
    aae419fdf0051b915a44f5fd517ce06b7d9bfcd55efbd16985710e04e63dc67a  root-checked-allD-admissibility.md
    21903528cbd23cd64d96c6db936913bc285929b8cd6db515857d89bc55d52b03  root-final-contract.md
    a33636fe714d410ab0380e599230acc1e21a44a1e63f6c4a1e23ea4242ae16f7  root-final-packet.md
    9d1a8c3b743acd97e79a0645f7291dd12c3471b60d776105d3a75b5ce39d3f83  root-release.md

Scope reminders applied throughout: all 46 scores are historical; d2=[K:C(f,g)]=2 and proper Galois second-leg quotients are CLOSED (BD-GAL), d1=2 distinct; 0040 completed 01:57:40; both all-D reports remain PROVISIONAL under the 03:23 gate whose body is forbidden; the source-admissibility report is ROOT-CHECKED INTAKE, not a theorem; GGV Corollary 7.9 is printed p.45. Census coverage is all-degree necessary coverage; the 44+20 rows are the n<=200 population only.

## 1. Critical state read: what 15q–15v actually proved, and what it did not

The accepted chain is one method applied five times: dilate (s), build the canonical reference R with R_0=H by division by aH^{a-1}, split A_s=R^3+kernels+F, B_s=f_B(R)+q(R)F+G, use the exact wedge [A_s,B_s]=[R,T]+[F,G] and the polynomial centralizer K[H] to force ord G>=2j, then work locally at each root of H (simple inverse, Morse for multiplicity 2, cubic right-chart for multiplicity 3) and finish every regime by the same two lemmas: an earlier initial dies by top-coefficient differentiation plus Euler positivity, and commuting monic initials of degrees 3 and 5 satisfy Q^3=P^5, hence P=W^3 with W LINEAR, contradicting the nonzero remainder tuple. Three facts about this method decide the next round and are not stated in any charged input:

1. **The final step is a one-step approximate-root argument.** Q^3=P^5 forces P=W^3 with W linear ONLY because gcd(3,5)=1 and the local degree of P is 3. For tops H^a/H^b with g=gcd(a,b)>1 the same UFD step gives P=W^{a/g}, Q=W^{b/g} with W monic of degree g, and a perfect power IS attainable (Z^6+3bZ^4+3b^2Z^2+b^3=(Z^2+b)^3 has remainder degree 4, exactly the degree the 15q/15v controls flagged as the failure of the cubic-difference bound). So the campaign's local consumer terminates in one step precisely on coprime exponent pairs; otherwise it is the first rung of an Abhyankar–Moh approximate-root tower (avenue 6), with all the resonance/equality bookkeeping the 15u/15v mod-7 arguments handled for one rung.
2. **Every u_s=1 Moh child is coprime, and that is why the front was tractable.** For a licensed u_s=1 descent, (n',m')=(n/d_s, m/d_s) and the child's outer tops are H^{n'/d_2'}, H^{m'/d_2'} with d_2'=d_2/d_s, i.e. exponents (n/d_2, m/d_2)=(n/d_2, -M_1/d_2), coprime by definition of d_2=gcd(n,M_1). The (125,75) rows give (5,3) with deg H=5. The remaining 43 u_s=1 rows are coprime too; their difficulty is only deg H=d_2/d_s (multiplicities up to that degree) and the (a,b) values.
3. **The all-D constant-J framework is universal after reduction, and its "closed-H" hypothesis is vacuous.** For any Keller pair with deg f+deg g>2 the top forms commute, so f_top=lambda*H^a, g_top=mu*H^b with H the common form of degree gcd(deg f,deg g) (classical dependence of commuting binary forms; not re-cited from a pinned primary). McKay–Wang Theorem 5 at r=s=0 (as read in the admissibility report) gives H at most two distinct linear factors, and the report's own typing shows K[H_0] is the centralizer exactly when H_0=L or H_0=L_1^r L_2^s with gcd(r,s)=1. Writing H=H_0^e, every Keller pair is literally an (A,B)=(ea,eb) client of the reference frame with base H_0, D_0=deg H_0, constant J. The admissibility verdict NO ATTACHED CLIENT is therefore a statement about the (3,5)-ONLY theorem with unreduced H: the physical F2 lift u^15v^60/u^25v^100 is the (15,25) client with H_0=uv^4 (D_0=5, coprime (1,4)), not a failure. The genuine restriction of the provisional framework is the fixed (3,5) exponent pair and D>=3, nothing else.

Consequently: (i) the next uniform bridge is the (A,B)-general reference theorem with reduced base, whose late-contact half is probably routine (Card B) and whose early-contact half is the AM tower (the real wall, now named precisely); (ii) the counterexample side has NO sufficient client left at max degree 125: the complete guarded B0 contract's only built instance is the F2 (3,5) row, conditionally a unit by 15q; (iii) the finite 125 frame has exactly one named unretired Moh target, the M2=90 sibling (Card A).

## 2. Disposition vector, avenues 1–46 (each exactly once)

Format `#: disposition — reason if changed`. Old scores are history; "unchanged" means no new evidence in this packet moves the avenue.

- 1: unchanged (GGV frame supplies the two-point/standard-pair source; F2 (3,5) row closed conditionally; no farm).
- 2: unchanged. 3: unchanged. 4: unchanged (local maximum). 
- 5: unchanged — note only: the late-contact descent is a Moh-Cor-6.1-type degree descent, vacuous once the direct obstruction shows late contact never occurs; not a revival.
- 6: unchanged in rank, but RECONNECTED: the 15q–15v terminal step is a one-rung approximate-root argument (§1.1). No launch.
- 7: unchanged. 8: unchanged. 9: unchanged. 10: unchanged (NO LEVERAGE stands). 11: unchanged (refuted; Long 2026 is four-variable). 12–18: unchanged. 
- 19: unchanged (Witt tower at local maximum; no new Witt digit this round). 20–25: unchanged.
- 26: unchanged — d2=2/Galois closed by BD-GAL; d1=2, non-Galois d2>=3, primitive: no new discriminator; not renamed.
- 27, 28: unchanged.
- 29: unchanged AT its 0040 scoped raise — the reference/centralizer frame is exactly Hamiltonian-centralizer work; its next object is the reduced two-factor frame of §1.3, not a nilpotence claim.
- 30, 31, 32, 33 (Sol residue test automatic, stays stopped), 34, 35: unchanged.
- 36: LOWER — with all six F2 receivers and the named 105 parent closed, no sufficient CE client with degree <=125 exists; a guided search needs a NEW complete source (next GGHV row or a non-standard frame) plus a sufficiency contract first. The 0040 method-control raise bought nothing and is withdrawn.
- 37–46: unchanged (44 remains REFUTED-AS-PROOF; 46 non-blocking).

Count: 45 unchanged (one with a scoped-raise retained, one reconnected), 1 lower, 0 raise, 0 reopen. No global reranking follows from any scoped task result in this packet.

## 3. Reranked bottlenecks, mechanism verdict, new connection, strongest attacks

### 3.1 Principal PROOF bottlenecks (reranked)

1. **Uniform bridge = the AM tower in reference form.** In the reduced frame (§1.3) a counterexample has gcd(deg f,deg g)=e*D_0>=16 (GGV Cor 6.6), so EITHER e=gcd(A,B)>1 (multi-rung tower at each root) OR D_0>=16 (local charts of multiplicity up to 15 at one of two points). The campaign's consumers cover one rung with multiplicities <=3. This, not "source coverage" in the abstract, is the exact all-degree obligation. Replaces the 0040 wording "all-degree coverage, arbitrary multiplicities/degree ratios".
2. **(A,B)-general late-contact bound** (bounded, probably provable): the direct obstruction's degree argument uses only "L strictly between (A-1)D_0 and A*D_0 is not a multiple of D_0"; it should survive arbitrary (A,B) with D_0>=2 and fail exactly at D_0=1 (one point at infinity, where automorphisms live). Card B.
3. **Finite 125 frame:** the M2=90 sibling (Card A); then the 43 other u_s=1 rows by (a,b,k,deg H) shape; then the 20 class-C rows, still unlicensed.
4. **Trust perimeter of every u_s=1 closure:** the ell-shifted major-packet transport (Prop 5.3 with J=gamma^ell) is printed only as remarks plus Moh's p.207 usage (15r/15s gate residual 1). It is load-bearing for 15v's headline and carries a named doubt. Card C attacks it.
5. **K16** b*B_m*eta_m locus and b=0 boundary: unchanged, no discriminator here; G2-PSC/G2-BD: unchanged.

### 3.2 Principal DISPROOF bottlenecks (reranked)

1. **No sufficient client exists.** The only sufficiency contract (complete guarded B0 envelope, remaining-m90 interface) has one built instance, the F2 (3,5) row, now conditionally a unit. Any CE computation before a NEW complete source with its own acceptance theorem is spend without a target. STOP-tier.
2. **Falsify the chain, not the receiver.** The cheapest way a counterexample could still hide at 125 is a wrong import: the unprinted ell-shifted condition (3)/Prop 5.3 transport, the accepted child datum (25,15;21;2;2), or the GGHV 108 overlay. A countermodel detaches 15v's parent claim while leaving the receiver theorems true. Card C.
3. Avenue 19 Witt tower, 35, 32: unchanged local maxima.

### 3.3 Genuinely new mechanism: **reduced-base universality of the reference frame (RBU)** — NEW frame statement from KNOWN parts

Statement (hand-derived, §1.3): after replacing H by its reduced base H_0 (one linear factor, or two with coprime exponents), the centralizer hypothesis K[H_0] holds automatically, the constant-J reference/wedge/kernel construction applies to EVERY plane Keller pair with (A,B)=(deg f,deg g)/D_0, and the only non-universal hypotheses of the provisional all-D framework are the fixed (3,5) exponents and D>=3. History check: the LIVE line "the separate all-D closed-H candidate has no attached unresolved client" and the admissibility report treat closed-H as a restriction and refuse representative standardization; RBU needs no standardization because the common H is intrinsic to the given pair. Closest synonyms in the frozen map: avenue 1 (GGV standard frame), avenue 25/26 (points at infinity), the admissibility two-factor typing. None states RBU. Classification: NEW composition; components KNOWN (dependence of commuting top forms — classical, flagged for the synthesis to pin a primary statement; McKay–Wang Thm 5; the report's own centralizer typing). It is a reformulation of the open two-point case, NOT an exclusion, and it supplies no point.

What RBU changes operationally: (i) the physical F2 (75,125) lift becomes a literal (15,25)/H_0=uv^4 client of the general framework, a free CONTROL for Card B (already conditionally dead by 15q, so any survival there would signal an error); (ii) the original Moh parents are one-point objects in total degree (tops y^n,y^m; H_0 linear, D_0=1), so a total-degree reference argument at the parent level would have to recognise automorphisms, which is why the Moh descent to a monomial-J child (D_0=5, coprime (5,3)) is the correct move and cannot be bypassed by RBU alone; (iii) the admissibility "no client" verdict should be re-read as "no (3,5)-with-unreduced-H client".

### 3.4 New connection between existing avenues

**6 ↔ 29 ↔ 1:** the reference method's terminal Euler/UFD step is the first rung of an Abhyankar–Moh approximate-root tower (avenue 6), run inside Hamiltonian-centralizer bookkeeping (avenue 29) on the GGV/Moh two-point frame (avenue 1). Corollary: the 15u/15v arithmetic exclusions of resonance (7eta+2lambda=36, modulo 7) are the one-rung shadow of the semigroup/characteristic-sequence integrality that avenue 6 was "tried on the wrong object" for. The right object is now explicit: the local initial polynomials P,Q on each sheet. A second connection: **5 ↔ all-D descent:** the late-contact descent is an elementary-reduction mechanism that provably never fires (direct obstruction), so avenue 5's "amalgam rigidity never bites" verdict is confirmed by the campaign's own tool.

### 3.5 Strongest proof attack

Prove the (A,B)-general late-contact bound in the reduced frame (Card B), then attempt the two-simple-root base case H_0=xy with NON-coprime (A,B)=(8e',12e') (the smallest gcd>=8 shapes not closed by GGV): both local charts are simple roots, so the entire difficulty is the tower recursion P=W^{A/g}, Q=W^{B/g}. If a second-generation reference (reference of degree g in the local variable) closes it, the campaign owns the first all-degree two-point exclusion family; if it stalls, the stall is the exact tower obstruction and the all-degree proof front should be redesigned around it rather than around more finite receivers.

### 3.6 Strongest genuine counterexample / falsification attack

Not a receiver solve. Build by hand a monomial-J pair with nontrivial characteristic data (automorphism composed with (x, x^ell*y)-type maps, degrees <=6) and test the ell-shifted major-packet/Prop 5.3 transport literally on it (Card C). A failure would be a load-bearing scope reversal (critical trigger): 15v's receiver theorems survive but the named parent is no longer excluded, and every u_s=1 closure inherits the gap. This is the only cheap attack that can change the 125 verdict; every other CE lane is starved of a sufficient client.

## 4. Idea cards (three, the maximum)

### Card A — M2=90 sibling: same-receiver-shape test (finite 125 frame)

- **Object/field/hypotheses.** The second Moh (n,m)=(125,75) census survivor, M_2=90, "same V path" as the 105 row (remaining-m90 interface). Over a characteristic-zero field, under the SAME licensed u_s=1 Prop 6.3/6.4 descent and child-data transport imports as 15r–15v. Its exact row datum (M_3, d, V, u_s, v_s) is NOT in the charged inputs: **missing premise**, requested as root's equal supplement; nothing below reads an uncharged file.
- **Dependencies/tiers.** Accepted 15q/15r/15s/15t/15u/15v (PROMOTED, conditional on named Moh imports); the actual-Moh source map 07e53340/eade8ec8 (accepted). The receiver theorems are stated purely in (degrees 15/25, H, J=c*g^2); the parent datum enters ONLY through the map (centering needs radius delta_2'=-1, packet contact 7/5, total degrees 25/15).
- **Cheapest discriminator (hand, 30–60 min, zero compute).** Descend the row by the licensed law used for 105 (n'=(n/d_s)u_s, m'=(m/d_s)u_s, ell=v_s-u_s-1, and the child's M_2' by the same transport that gave 21=105/5 for the 105 row) and compare (n',m',M_2',V_2',k,delta_2',delta_1') with (25,15,21,2,2,-1,7/5). Consistency self-check on whatever datum results: a pi-monic P in K[gamma,pi] cannot have an ODD number of roots at a half-integral t-order (Galois pairing), so a transcription giving 15 non-packet roots at delta_2'=-1/2 is inconsistent and must be re-derived, not consumed. (Naive transcription M_2'=90/5=18 would give delta_2'=-3/6=-1/2 — I label this an ASSUMPTION from the 105 pattern, not a fact.)
- **Outcomes.** (a) Identical datum incl. delta_2'=-1: the whole chain attaches verbatim; M2=90 closes by theorem-interface composition after one short different-model map gate — the 125 Moh frame's last named survivor. (b) Same (25,15;k=2) but different M_2'/radii: the (1,1)-face centering fails; the receiver is a WEIGHTED-face object — first genuinely new receiver geometry; write its face/weights before any consumer. (c) u_s!=1 or inconsistent datum: the row is unlicensed for descent, or a census artifact to be corrected under the actual-stabilizer screen; no receiver work. (d) Nondecision (datum unavailable): zero cost, request supplement, no launch.
- **Stop condition.** Datum compared and one of (a)–(c) recorded. **Information gain:** high; decides whether any new mathematics is needed at max degree 125 in the Moh frame. No solver, no source emission.

### Card B — (A,B)-general late-contact bound in the reduced two-factor frame (uniform bridge)

- **Object/field/hypotheses.** Ordinary A,B in K[u,v], char 0, deg A=A*D_0, deg B=B*D_0 with A<B arbitrary (gcd NOT assumed 1), tops H_0^A, H_0^B with H_0=L_1^r L_2^s, gcd(r,s)=1, r+s=D_0>=2, [A,B]=c in K^*. Canonical reference R (R_0=H_0, division by A*H_0^{A-1}), all A-kernels (scalars times s^{(A-i)D_0}R^i, i<=A-2), all B-kernels, q(R)=quotient of f_B' by f_A', G, the exact wedge, ord G>=2j via K[H_0].
- **Dependencies/tiers.** Accepted finite late-T lemma (15s, PROMOTED, exact polynomial/homogeneous/centralizer scope). Provisional descent 857b2e2/direct 2dcff164 are pattern only, NOT premises (their gate body is forbidden). RBU (§3.3, this report, hand-derived, unreviewed).
- **Cheapest discriminator (hand, 1–2 h, then one different-model prose gate).** Derive T's top-degree candidates: (A-1)D_0+n from A*H_0^{A-1}g_n and (B-A-1)D_0+2m from q'(R)F^2/2-type terms, with m=A*D_0-j, n<=B*D_0-2j; late contact 3j>(A+B-1)D_0. Check whether "L not a multiple of D_0" (D_0>=2) forces the same contradiction as at (3,5), for (A,B)=(2,3),D_0=2 (H_0=xy) and (A,B)=(6,10),D_0=2 (non-coprime). Free control: the physical F2 lift (15,25), H_0=uv^4, must NOT survive (already conditionally dead by 15q).
- **Outcomes.** (i) Closes for all (A,B), D_0>=2: first all-degree, all-ratio theorem of the campaign's method in the exact open two-point case ("every Keller pair with two points at infinity has canonical contact j<=(A+B-1)D_0/3"); no exclusion, but the early-contact tower (bottleneck 3.1.1) becomes the sole obligation. (ii) Closes only for coprime (A,B): the tower obstruction already bites at the late step; record as the exact wall, stop generalising. (iii) Fails at D_0=2 or needs D_0>=3: the direct obstruction is special; note and stop. (iv) Inconclusive/nondecision: no change to any avenue. (v) Control survives: RBU or the map is wrong; quarantine RBU.
- **Stop condition.** One of (i)–(v) written with the exact failing/holding inequality. **Information gain:** locates the scope of the only all-D tool the campaign owns; no compute, no source construction, no promotion.

### Card C — Falsify the ell-shifted major-packet transport by a hand countermodel (trust perimeter)

- **Object/field/hypotheses.** Moh Prop 5.3 (major packet shrinks to the common minimal disc) and Prop 4.2/4.4 condition (3), used on a monomial-J child J=gamma^ell with the ell-shift, printed only as remarks plus Moh's p.207 usage; load-bearing for 15r/15s/15v's parent attachment and for every u_s=1 closure.
- **Dependencies/tiers.** Named import (EXTERNAL-TRUST, unreviewed by the campaign as a theorem); the accepted source gate's residual obligation 1. Resolution-first directive: hardening is default-off unless load-bearing AND a named doubt — both hold here.
- **Cheapest discriminator (hand, 30–45 min).** Construct a monomial-J pair with nontrivial characteristic data: (P,Q)=phi∘(x, x^ell y) for a tame automorphism phi of degree <=3 and ell in {1,2}, so [P,Q]=c*x^ell literally. Compute its Puiseux root packets at infinity by hand (degree <=6), the radii, and test the ell-shifted statement: does the major packet at the last level lie in one disc of the shifted radius -(ell+1)/(n-M_s-1), and does condition (3) hold in its shifted form? Honestly labelled hand control, no CAS.
- **Outcomes.** (a) Holds on the control: weak confirmation, no promotion, doubt narrowed; stop. (b) FAILS: the transport is false as used — critical trigger: 15v's receiver theorems stand, the named parent exclusion detaches, all u_s=1 closures inherit the gap; root abort/reseal decision. (c) Control has trivial characteristic data (single level): no test; try one deeper phi or stop after two attempts. (d) Inconclusive: record the exact untested clause.
- **Stop condition.** One control fully worked, or two attempts without a testable level. **Information gain:** proportional to fanout×fragility; this is the single cheapest thing that could still change the degree-125 verdict.

## 5. Decisive experiment, lane recommendations, systems check, history check, scope

### 5.1 One decisive experiment (no solver)

**Receiver-shape census of the 44 u_s=1 rows.** For each row apply the licensed descent law by hand or by a stdlib integer script run by root under normal custody (NOT in this blind), emitting (n',m',k,d_2',delta_2',delta_1', outer-H multiplicity partitions). Count rows whose child datum equals (25,15;21;2;2;-1;7/5): each such row inherits 15q+15r+15s–15v by theorem-interface composition after a per-row map gate, because those theorems are stated in receiver terms only. Rows with other (a,b,k,deg H) are binned by shape; a shape with deg H<=3 and coprime (a,b) is within the existing consumers' reach, deg H>=4 or a weighted face is not. Interpretation: a nonzero same-shape count is free closure; a zero count says the 125 closure is a singleton and the uniform bridge (Card B) is the only scalable path. Matching numerical labels is not a map: every hit still needs the centering/radius map checked. Time: under one lane-hour. No software acceleration is proposed beyond this metadata-tier script; no solver, farm or RAM escalation.

### 5.2 Continue / redesign / stop

- Named Moh 105 source and all six F2 receivers: **STOP** (closed; no solves, no localization, no reverse lift).
- All-D descent/direct-obstruction joint gate (live, deadline 03:23, body forbidden here): **CONTINUE** to terminal; then **REDESIGN** the framework to the reduced base H_0 and general (A,B) (Card B) before any client search. Do not search for (3,5)/K[H] clients: by §1.3 none can exist outside the reduced statement.
- Source-admissibility lane: **STOP** (done); re-read its verdict per §3.3.
- M2=90 sibling: **CONTINUE** as the sole finite 125 target (Card A), datum first.
- Trust-perimeter hand control: **CONTINUE/START** (Card C), one bounded slot.
- K16 product locus/b=0: unchanged, idle; no experiment earned.
- Counterexample solves of any retired or necessary-only receiver: **STOP**; a CE lane needs a NEW complete source plus acceptance theorem.
- Broad web sweep: continue on its 22:24:26.958594 clock; social holes since Sep 3 unchanged.
- AWS: zero allocation; preserve vol-0eb6450d18ffa89f1 and retained exact inputs.

### 5.3 Campaign-systems assessment: **UPGRADE (small)** — reference-method lemma sheet

Evidence: 15q, 15t, 15u (twice), 15v and the direct obstruction each re-derive the same four lemmas (finite late-T subtraction; wedge identity with kernel induction to ord G>=2j; earlier-initial kill by top-coefficient derivative plus Euler positivity; commuting monic a/b initials ⇒ common root via Q^a=P^b) and each gate re-verifies them (gate bodies 12–17 KB, 8–22 min). The 15v producer's one false sentence (whole-quintic "degree<=1") was a re-statement error of exactly this kind. Smallest measurable test: extract the four lemmas with EXACT hypotheses and AUDIT IDs into one hash-pinned sheet; require the next reference-method producer to cite sheet IDs in a "lemma citations" block and the gate to check hypothesis match only. Metrics: producer body bytes and gate wall time versus the 15t/15u/15v means, and the number of hypothesis mismatches found. Retain if bytes or time drop >=20% with zero mismatch; revert to inline derivation on any out-of-scope citation (the FALLACY analogy failure mode). Risk: error propagation — mitigated by admitting only PROMOTED lemmas. Routing/adapters/custody: all four 15s–15v gates ran inside their deadlines with zero mathematical subprocess and receipt-first collection; no change. Retrieval: this packet's 460 KB whole-read took 14 minutes of a 50-minute window; acceptable, no change. Not proposed: linters, schedulers, telemetry, new seats.

### 5.4 History/priority checksum of this report's mechanisms

- RBU (§3.3): NO exact hit in APPROACHES, the 46 table, BD-GAL, 0040 synthesis, admissibility report; nearest: admissibility two-factor typing (KNOWN component), LIVE "closed-H candidate" (SCOPE-CONFLICT resolved by reduction). NEW composition.
- One-rung/AM-tower diagnosis (§1.1, §3.4): NO hit; avenue 6 recorded as "tried on the wrong object". NEW connection.
- Card A: KNOWN target (LIVE/0040 name M2=90 as unexcluded); NEW discriminator (parity self-check, same-shape test).
- Card B: NEW generalisation of a PROVISIONAL result; not a promotion of it.
- Card C: KNOWN residual obligation (gate residual 1); NEW as a hand countermodel plan. Not a duplicate of any retired control.
- Avenue 36 lower: consequence of 15q/15v, not a new mechanism.
- Explicitly NOT revived: d2=2/Galois quotients, common4 localization, generic 9/15 toy, coefficient-residue test, K7/D108/(99,66) solves.

### 5.5 Exact scope and terminal writer status

This blind asserts no theorem, promotion, exit price, source existence, novelty or JC2 conclusion. Its mathematical content is hand reasoning at the stated tiers; RBU and the tower diagnosis are unreviewed observations for cross-pollination. Both all-D reports remain PROVISIONAL; the 105 closure remains conditional on the named Moh imports; nothing here narrows or widens any accepted scope. Partial: none — every contract obligation (46-vector, bottleneck rerank, mechanism, connection, attacks, experiment, lane recommendations, three cards, systems check, history check) is delivered above. **Actual end of substantive writing 03:47 UTC**, before the 04:20 common deadline. Terminal custody: external lane custody via the launcher's receipt-first procedure; this file is the only write, no shared ledger touched, no follow-on launched, all writers idle at seal.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries. No corpus scan was performed.

<!-- BODY-END -->
