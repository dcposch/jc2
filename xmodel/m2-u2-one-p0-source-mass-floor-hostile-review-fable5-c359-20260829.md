# Hostile review — nested U2 one-P0 source-mass floor (ASM / NM / U2F)

Date: 2026-08-29  
Reviewer: Fable 5 (`claude-fable-5`), independent hostile referee, single
invocation, local shell used only for SHA-256 custody and bounded
integer/rational desk arithmetic (bug-finding only; no CAS, no web, no AWS,
no jc2-lean access, no canonical edit, no commit, no push).  
Git basis (verified `git rev-parse HEAD` at session start):
`c3598b92598c1596e6c6331f4c877619b432a115`.

Target under review:
`xmodel/m2-u2-one-p0-source-mass-floor-r1-sol56-20260829.md`.

**Primary verdict: `FAIL` at the report's headline scope (ASM at `mu>=3`,
U2F `td>=15`, and the `td<=12` panel removal), with a proved partial
salvage.** The load-bearing step `M_H | M_P = b_P` on a merge-free segment
is not merely unproved: it is refuted inside the frozen basis, which
records a merge-free dirty step with `M: 2 -> 3` and a `b=2` pole arriving
with multiplicity `3`. The maximum safe promotion is the repaired floor
set of §6 below: `td >= 3*beta` (topological), `td >= 3*max(beta,2*alpha)`
for the corrected labelled family (minimum `12`, attained in bound value
only at type `(2,3)`), and ASM verbatim for `mu <= 2` only. These remove
the family from every `td <= 11` panel — in particular every `td = 8`
panel — and do **not** remove it from `td = 12`.

## 1. Target custody and body-convention adequacy

Recomputed this session, before reading:

- full file: `28f9918e18eae42580584afbd98a36418ac98ecabf078c829e20484159baeb3c`
  (matches producer claim); file length `8739` bytes;
- claimed body = first `8611` bytes: SHA-256
  `42993a409e5ed4d2f4c4bb253e05e6ebf1b0e2f22dbd2eaf80bf71aa076d7f71`
  (matches).

Byte-level inspection of the tail confirms the stated convention: byte
8611 is the newline immediately following the unique occurrence of
`*End of sealed report body.*`; the excluded remainder is exactly
`\n---\n\n` + the seal section (128 bytes total), whose recorded count (`8611`) and
hash agree with the recomputation.

**Adequacy assessment:** the convention is adequately defined. The byte
count is primary and unambiguous; the prose marker and the
excluded-remainder description are consistent with it and would expose
tampering in either direction. Sibling artifacts use different but
self-consistent conventions (the family record seals "all bytes strictly
before the final separator": I verified its body, 17559 bytes ending
before the final `\n---\n`, hashes to the
`ce5cf26906d3c736e75c791c3600be201b65279aabbbacbf0b12014d51497c29` value
cross-cited by the correction §0). No custody defect.

## 2. Frozen five-source manifest, pre/post

Recomputed immediately before reading (PRE) and immediately before this
verdict (POST). All ten values match the pinned manifest; no
`INPUT_MUTATED`.

| file | pinned SHA-256 (prefix) | PRE | POST |
|---|---|---|---|
| `ladder/SHEET6-MULTIPOLE.md` | `93adb7ac…964bcb` | match | match |
| `ladder/BOOK-OFFAXIS.md` | `40104334…0cfaaaa` | match | match |
| `ladder/SHEET6-TDUNIFORM.md` | `9034a987…f805d` | match | match |
| `xmodel/…family-record-r1-sol56-20260829.md` | `19fcd013…58f82` | match | match |
| `xmodel/…family-record-r1-correction-sol56-20260829.md` | `4dde1c47…622dc` | match | match |

No prior review or campaign verdict was used as a proof oracle; every
mathematical charge below cites one of these five files by line.

## 3. Charged passages (line-frozen citations)

- `ladder/SHEET6-MULTIPOLE.md:66` (global type `2<=alpha<beta`, coprime);
  `:68-71` (chain tree `U`, `r(G)`, merge, `mu_e = mult(p_G^red,c_e)`);
  `:80` (MP0); `:82` (MP1); `:92` (MP4, `M_P = b`; `b=1` forced iff
  `Lambda` beta-minimal or prime); `:94` (MP5, incl. "the chain arrives
  at `G_i` with `mu_i = 1`"); `:96` (St 8.4 orientation
  `mu_e | M_{H_e}`); `:138-141` (D1: leaves are exactly the poles, poles
  have in-degree 0, every non-pole vertex is some `F^o`); `:143-144`
  (D2: unique out-edge, finite tree); `:156-157` (D5: St 8.4 at
  `(K, H=K+c)` gives `mult(p_K^red,c) | M_H`); `:181` (`td = sum Lambda_i`,
  Props 5.7/5.8).
- `ladder/BOOK-OFFAXIS.md:25-27` (triple-review status: "R1.3-R1.5
  REFUTED …; the M-descent law contradicts St 9.6(iii)/(iv)");
  `:104-108` (§2(a): St 8.5 verbatim — `F in T_a^dn cap V_a`, `G=F^o`,
  **`G notin V_{2,a}`** implies `M_G | M_F` — followed by the overbroad
  gloss "So down every merge-free segment the M-value divides `b_i`
  non-increasingly"; St 8.4 verbatim, no `M=1` hypothesis); `:119-127`
  (§2(c1): for `M>=2` the printed record does NOT exclude segment
  vertices in `V_{2,a}`); `:276-289` (R1.3 dirty chain vertices = the
  `V_{2,a}` escape; none exist at `mu=1` arrivals; general arrival mult
  `l>=2`); `:291-301` (R1.4 dirty transport; contains the later-refuted
  `M_F | M_parent`); `:370-372` and `:384-389` (§8 retraction header:
  "Step 2's M-law is refuted"; Step 2 is the retracted use of St 8.5 at
  dirty cells, "`M_G = 3 ∤ M_H = 2` — dead (St 8.5)"); `:515-544`
  (§10 P0 priced menu replacing R1.3-R1.5, `M_F = gcd(dp,dq)` with **no
  divisibility into the parent**; `:540`: from state `(3/2, M=2)` the
  dirty (A)-step lands cell `(21,15)` with `w -> 2/3`, **`M -> 3`**,
  `lambda >= 2`); `:569-571` (P2: arrival mults divide the **current**
  arriving state `M_{H_e}`, not the entry `b_i`); `:639-647` (P4
  `(10,15)` route: `b=2` entry → (A)-cell `M -> 3` → **arrives
  `mu_0 = 3`**); `:76-86` (entry census; `:84-85`: `td12 m3: [2,2,2]`
  is a live L6-surviving off-axis entry); `:669-700` (P5: 69-state
  reduced `(w,M)` closure from `(3/2,2)`, `M` up to 25; "NO off-axis
  grid skeleton is certifiably DEAD at printed tier … 0 DEAD / 0 ALIVE /
  2691 OPEN"); `:807-811` (`w=1` states priced `lambda` 4/5 in that
  closure); `:313-314` (R2: `mu_e | M_{H_e}`, St 8.4); `:321-339`
  (R2.1 handshake `X_G = mu_e*(kbar_G - w_e)`); `:217-218` (R5:
  `td = sum Lambda` carries the Prop 5.8 generic-`a` rider).
- `ladder/SHEET6-TDUNIFORM.md:54-56` (R1); `:57-61` (R2: case (A)
  `nu|alpha`, `nu|b*beta-1`; case (B) `nu|beta`, `nu|b*alpha-1`);
  `:62-65` (R3: `Lambda = a*b*alpha*beta/nu`; `td = sum` over
  `T_a,pole`); `:66` (R4: `Lambda >= beta`, Prop 5.7); `:67-68` (entry
  `kbar = a(alpha+beta)`, `rho = a/b`); `:78-84` and `:330-331`
  (`M_F = b` at every pole vertex, multi-pole valid).
- family record `:106-111` (route `U0 --II,l=3--> P1 --I,h=3--> U2`,
  "two symmetric P1 arrivals"); `:113-118` (inner `a=1, r=2, mu=3`,
  `dp_0=6`, `M_0=3`); `:122-126` (P0 labels `l=3`, clean neutral);
  `:128-133` (outer `R=2, h=3`, two equal-weight arrivals `w_1=2`);
  `:151-159` (outer `dp_2=6`, `dq_2=K+2`); `:246-259` (record fields);
  `:265-269` (outer coefficient character: quadratic radical, i.e. two
  distinct root orbits); `:281-285` (coverage debt incl.
  `unused_siblings`, `landing`, `realization`); `:364-405` (i-sync
  compatibility; sibling scale is a landing obligation).
- correction `:26-34` (`inner_u2.dq: 4 -> 3` is the only field change);
  `:41-62` (five exact checks, `E = mu*dq - dp = 3 = mu*L`);
  `:68-76` (corrected fragment; coverage debt +=
  `absolute_index_or_prod_nu_bound`); `:84-98` (maximum safe result).

## 4. Itemized attack verdicts

**A1 (orientation; are the labelled arrivals St-8.4 edges?) — PASS,
conditional exactly as stated.** MP0/D1/D2 (`MULTIPOLE:80,138-144`) give:
`U` finite, rooted at `(0,y)` below, unique out-edge `F -> F^o`, leaves =
poles above, `U \ {(0,y)} = Ta& ∩ Va \ {(0,x),(0,y)}`, in-degree
`r(G) = #{H : H^o = G}`, arrivals `H = G + c` above `G`. `U_H` (component
above the incoming edge) is well defined: predecessors of any `K` in
`U_H` stay in `U_H`, so in-degrees agree with `U`. The producer's theorem
is explicitly conditional on landing (target `:85-88`, `:164`); under
that hypothesis every labelled arrival is a `U`-edge and St 8.4 applies
in its exact recorded orientation `mu = mult(p_G^red, c) | M_H` at the
**upper** vertex `H` (`MULTIPOLE:96,157`; `BOOK-OFFAXIS:106-107,313-314`).
The producer uses only this orientation. No overreach found here.

**A2 (one pole leaf ⟹ merge-free; and the stronger `notin V_{2,a}`) —
first part PROVED, second part REFUTED.** Proof of the first: in `U`
every maximal ascending path ends at an in-degree-0 vertex, which is a
pole (D1 `:141`); each incoming subtree at a vertex is nonempty and
finite, so `r(K) >= 2` forces `>= 2` pole leaves above `K` in disjoint
subtrees (D2 tree structure). Hence a one-pole-leaf `U_H` is a single
path `P -> … -> H`, and the merge `G = H^o` below it is the **first**
merge `G_P` of `C_P` — the fact needed later for MP5. The stronger
statement the producer actually needs — every child on that path lies
outside `V_{2,a}` — is false at the frozen basis: `BOOK-OFFAXIS:119-127`
states the printed record does not exclude `V_{2,a}` segment vertices
when `M >= 2`, `:276-289` pins their shape as real ("the escape is real
but RIGID"), and `:540` prices a concrete such step. `r(G)=1`
(Notation-9.2 regularity, MP1 `:82`) does **not** imply `G notin
V_{2,a}`; the producer's proof conflates exactly these two conditions.

**A3 (does "merge-free" compose St 8.5 to `M_H | b_P`?) — REFUTED at the
frozen basis; this kills ASM as proved for `mu >= 3`.** St 8.5 as
recorded (`BOOK-OFFAXIS:104-106`) requires `G notin V_{2,a}` at every
step. The gloss on `:106` ("down every merge-free segment…") overstates
the statement two lines above it, and the same file refutes the gloss
three independent ways: (i) the triple-review header `:25-27` refutes the
R1.3–R1.5 M-descent law outright ("contradicts St 9.6(iii)/(iv)");
(ii) §8 Step 2's use of St 8.5 at dirty cells is retracted by name
(`:370-372`, `:384-389`); (iii) the corrected §10 P0 menu (`:515-544`)
carries no parent-divisibility law and its sanity row `:540` exhibits a
merge-free dirty step from `(w,M) = (3/2,2)` to cell `(21,15)` with
`M_F = gcd(21,15) = 3 ∤ 2` (desk-recomputed: `E=9`, `kbar_F=5`,
`w_F=2/3`, `M_F=3`, N1 `gcd(5,7)=1` — all match the frozen values), and
the P4 route `:643-647` continues it to an actual `mu_0 = 3` arrival
from a `b_P = 2` pole. So a `V_{2,a}` escape is a genuine, recorded,
M-arithmetic-breaking event on a merge-free segment; it is priced in
`lambda` (`>= 2` on that step) but unpriced in the producer's
divisibility ledger. The zero-length case `H = P` is the only sound
subcase (`mu | M_P = b_P` by St 8.4 alone; target `:140-141` is correct
there). The producer's pinned clause 4 (target `:66-68`) quotes the
gloss, not the statement: a missing load-bearing theorem, not a wording
issue.

**A4 (conditional pole cases; then the unconditional floor) — conditional
arithmetic PASS; unconditional replacement is `b_P >= 2`, not
`b_P >= mu`.** Given `mu | b_P`: case (A) `nu|alpha`:
`Lambda = a*b_P*(alpha/nu)*beta >= b_P*beta >= mu*beta > mu*alpha`; case
(B) `nu|beta`: `Lambda = a*b_P*alpha*(beta/nu) >= b_P*alpha >= mu*alpha`
(TDUNIFORM `:57-65`). Both producer displays (target `:123-135`) are
exact. Unconditionally, MP5's arrival clause (`MULTIPOLE:94`: `b_i = 1`
forces arrival multiplicity `mu_i = 1` at the first merge `G_i`; proof
D5 `:157`) applies verbatim in the one-leaf case because A2 showed
`G = G_P`; its contrapositive gives `mu >= 2 ⟹ b_P >= 2`. Nothing
stronger survives: `b_P = 2` with `mu = 3` is exactly the recorded
(A)-step-then-arrive pattern (`:540`, `:643-647`), and the closure from
the same entry state reaches `M` up to 25 (`:674-681`). So for a
unique-leaf branch with arrival multiplicity 3, a `b_P = 1` pole is
excluded (it would arrive with multiplicity 1), `b_P >= 2` is forced,
and `b_P >= 3` is **not** forced. The corrected family's special `mu=3`
buys nothing beyond `mu >= 2` at this tier. Resulting per-pole mass:
`>= max(beta, 2*alpha)` (case (A) gives `>= 2*beta`, case (B)
`>= 2*alpha`, and R4 gives `>= beta` always).

**A5 (NM disjointness) — PROVED.** In the rooted tree `U` (D2), the `r`
incoming subtrees at the inner merge are pairwise disjoint, all lie
inside the one incoming subtree of the outer merge that contains the
inner merge (every descending path from them passes the inner merge,
then the intervening segment, then the outer merge), and the other
`R-1` incoming subtrees at the outer merge are disjoint from that one.
An intervening P0 vertex (in-degree 1) creates no side entry
(unique-predecessor structure, D2 `:143-144`); an adjacent merge edge,
shared suffixes (all strictly below the outer merge, hence containing no
leaves of these subtrees), and deeper nesting change nothing. No leaf is
summed twice. `td = sum_P Lambda(P)` is the recorded R3/Prop 5.8 law
(`TDUNIFORM:62-65`; `MULTIPOLE:181`) — noting it carries the inherited
generic-`a` rider (`BOOK-OFFAXIS:217-218`), which the producer consumes
silently along with the whole book layer (disclosed here; not a new
break).

**A6 (what the corrected family record fixes) — fixed exactly as
claimed, and the producer UNDERUSES it.** The correction changes only
`inner_u2.dq: 4 -> 3` (correction `:26-34`), no arity or multiplicity.
Fixed post-correction: inner U2 `nu=1, r=2`, both arrival
multiplicities `3` (`dp_0 = 6 = 3+3` at `nu=1`; `mu:3`;
`E = 3*3-6 = 3 = mu*L`, correction `:49-53`); P0 arrival `l=3`; outer
U2 `nu=1, R=2, h=3, dp_2=6` with quadratic radical (record `:265-269`),
which forces the **second (unused/symmetric sibling) arrival to have
multiplicity exactly `6-3=3`** — a non-chain reading of the second root
is impossible since `m_j*dq < dp` would need `3*(K+2) < 6`. Roles:
`l=3` and `h=3` are the two inter-vertex arrival multiplicities, `r=2`
and `R=2` the two arities. Unproved and explicitly ticketed: source
landing, sibling upstream structure and scale, coefficient gluing,
absolute index / `prod(nu)` bound, realization (record `:281-285`,
correction `:75`, `:100-103`). The producer overstates nothing about the
sibling — but uses only `>= beta` for its subtree (target `:185-189`),
discarding the certified `h=3` sibling multiplicity that upgrades the
repaired floor from `11` to `12` (§6).

**A7 (typed `td <= 14` counterexample attempt) — a fully typed `td = 12`
ledger EXISTS and is consistent with every pinned law checkable from the
five sources; it is FORMAL, not actual.** See §5.

**A8 (replacement minimization) — proved floors: `3*beta` (topological)
and `3*max(beta, 2*alpha)` (corrected family); minima 9 and 12 at
`(2,3)`.** See §6. The producer's `td >= 15` is not retained;
`2*min(2*beta,3*alpha)+beta` has minimum 15 at `(2,3)` but rests on the
refuted A3 step.

**A9 (compiler audit) — the recommendation is UNSAFE as written.** "Attach
(ASM) to every actual merge arrival" (target `:207-210`) attaches an
unproved bound whenever `mu >= 3`. Safe rule: attach the §6 ASM′ floor
(`beta` for `mu = 1`; `max(beta, 2*alpha)` for `mu >= 2`) to every
arrival; attach the strong `min(2*beta, mu*alpha)` only with a
certificate — pole-adjacent arrival (`H = P`), or an edgewise
`notin V_{2,a}` certificate for every child on the segment (e.g. the
all-clean R1.1 shape chain, which gives `M_F | l | M_parent` stepwise),
or a directly certified `M_H | b_P`. `M = 1` chains are automatically
certified (Cor 8.1 per `BOOK-OFFAXIS:120-121`) but then `mu = 1` anyway.

## 5. The `td = 12` typed ledger (counterexample attempt, fully typed)

Global type `(alpha,beta) = (2,3)`. Three pole leaves, each with
`(a,b,nu) = (1,2,3)` — desk-verified to be the **unique** TDUNIFORM row
with `Lambda = 4` at type `(2,3)` (case (B): `3 | 3`, `3 | 2*2-1`);
each has `Lambda = 4`, `M_P = b = 2`, entry frame
`kbar = a(alpha+beta) = 5`, `rho = a/b = 1/2`, `w_0 = (5 - 1/2)/3 = 3/2`,
L6/N1 `gcd(5,3) = 1`. Total `td = 3*4 = 12`. This entry multiset is the
recorded live off-axis entry `td12 m3: [2,2,2]` (`BOOK-OFFAXIS:84-85`).
Tree: two nested binary merges (`G_in` above, `G_out` below; MP1 count
`sum(r-1) = 2 = m-1` exact, `:82`), the two `G_in` subtrees and the
`G_out` sibling subtree each a single merge-free `(1,2,3)`-pole chain.
On each chain: one recorded dirty (A)-step from state `(3/2, 2)` to cell
`(dp,dq,nu) = (21,15,7)`, `kbar = 5` (N1: `gcd(5,7)=1`), `w = 2/3`,
`M = 3`, `lambda >= 2` (`:540`; desk-recomputed exactly); then arrival
at its merge with `mu = 3 | M_H = 3` (St 8.4 satisfied at exact
orientation; `b_P = 1` excluded by MP5 as required — here `b_P = 2`).
Merge arithmetic: at `G_in`, two `mu = 3` arrivals, equal `mu` with
equal `w = 2/3` (R2.1(i) consistent); e.g. `epsilon = k = l = 0` cells
`(dp,dq) = (6*nu_G, 2*nu_G+1)` satisfy the searrow law
`3*dq > dp` and emit `M_G = 3` when `nu_G ≡ 1 (mod 3)`, so the P0
arrival `l = 3 | M_{G_in}` and the outer arrival `h = 3` are
St-8.4-legal; the sibling chain is the third copy. Budget: three dirty
steps cost `sum lambda >= 6 <= 11 - psi` at `psi = 1` — no recorded
contradiction. Each subtree's pole mass is `4 < 6 = min(2*beta,
3*alpha)`: **every subtree violates ASM's claimed floor**, and the total
`12 < 15` violates U2F.

**Honest classification: FORMAL typed ledger, not an actual
counterexample.** Missing realization data, exactly: (i) T1-rigidity
solves of Prop 8.1(iv) at the two merge cells and the `(21,15)` cells
under these frames (`BOOK-OFFAXIS` R2.3(iii); never executed for these
cells); (ii) the full per-edge Prop 9.3 handshake/transport chain
including the inter-merge P0 segment and a root/terminal
`psi`-certificate; (iii) i-sync absolute scale and coefficient gluing;
(iv) an actual `(f,g)` realizing the tree — unobtainable short of
refuting JC2 itself. The frozen basis classifies all such skeletons as
OPEN (`0 DEAD / 0 ALIVE / 2691 OPEN`, `:686-691`). Two consequences,
kept distinct: the ledger **refutes the producer's proof** (any valid
derivation of ASM from the five sources would have to kill a
configuration the sources record as open and arithmetically consistent),
and it leaves ASM-as-inequality on actual trees typed `OPEN` for
`mu >= 3`, not refuted. Note also the ledger is *not* a member of the
labelled family route: the record's inner frame forces arrivals at
`w_e = 1` (R2.1: `6 = 3*(3 - w_e)`), whereas these chains arrive at
`w = 2/3`; whether the labelled route itself can land at `td = 12`
(needing `w = 1` arrival states, priced `lambda` 4/5 in the closure
`:807-811`, with `3 | M` unrecorded) is undecidable from the frozen
text: typed `OPEN`, not excluded.

## 6. Replacement lemmas actually proved

All floors; no attainment is claimed anywhere.

**ASM′ (arrival-subtree mass floor, repaired).** Let `H = G + c` be an
actual arrival at an actual merge `G` with `mu = mult(p_G^red, c)`, and
`L_H` the pole-leaf set of `U_H`. Then

```text
sum_(P in L_H) Lambda(P) >= beta                     always;
sum_(P in L_H) Lambda(P) >= max(beta, 2*alpha)       if mu >= 2.
```

Proof: `L_H` nonempty (MP0/D1) and each `Lambda >= beta` (R4) give the
first line and the `|L_H| >= 2` case (`>= 2*beta >= max(beta,2*alpha)`).
For `|L_H| = 1`: the subtree is a single merge-free path, `G` is the
first merge of `C_P` (A2), MP5's arrival clause forces `b_P = 1 ⟹
mu = 1`, so `mu >= 2 ⟹ b_P >= 2`, and R2/R3 give `Lambda >= 2*beta`
(case A) or `>= 2*alpha` (case B), hence `>= min(2*beta, 2*alpha) =
2*alpha`, and `>= beta` by R4. QED. Consequently the producer's ASM is
**true verbatim for `mu <= 2`** (`max(beta,2*alpha) >= 2*alpha =
min(2*beta, 2*alpha)`) and unproved exactly for `mu >= 3`. Basis: MP0,
MP1, MP4, MP5, St 8.4, R2-R4 (+ the inherited Prop 5.8 generic-`a`
rider); N1/L6, St 8.5, and all coefficient tiers unused.

**NM′ (nested-merge floor).** With the A5 disjointness, for an inner
merge (arrivals `mu_1..mu_r`) inside one incoming subtree of an outer
merge of arity `R`:

```text
td >= sum_(e=1)^r c(mu_e) + (R-1)*beta,
c(mu) = max(beta, 2*alpha) if mu >= 2, else beta.
```

**Topological route floor.** For any doubly-nested-merge skeleton with
`r = R = 2` (no multiplicity data at all): `td >= 3*beta >= 9`.

**Corrected-family floor.** The record fixes all three relevant arrival
multiplicities equal to 3 (two inner, one sibling; A6), so

```text
td >= 3*max(beta, 2*alpha) >= 12,
```

with minimum 12 over coprime `2 <= alpha < beta`, only at `(2,3)`; the
equality profile is forced to three `(1,2,3)` poles — precisely the
recorded open `td12 m3 [2,2,2]` entry, so no improvement to `td >= 13`
is available from the frozen basis. Under the producer's weaker
hypothesis set ("same inner/outer merge arities and inner multiplicity"
only, sibling multiplicity dropped), the proved floor is
`td >= 2*max(beta,2*alpha) + beta >= 11`.

## 7. Producer §5 checklist scorecard

1. arrivals are St-8.4 MP0 edges: **PASS** (conditional on landing, as
   stated; orientation exact). 2. one-leaf ⟹ merge-free: **PASS**, but
   insufficient — the needed `notin V_{2,a}` strengthening is false
   (A2). 3. St 8.5 composes to `M_H | b_P`: **FAIL** (A3; zero-length
   subcase only survives). 4. `nu|alpha` / `nu|beta` bounds given
   `mu | b`: **PASS** (conditional). 5. disjointness of the three pole
   sets: **PASS** (A5). 6. record fixes inner `(r,mu) = (2,3)`, outer
   `R = 2` after the `dq_0 = 3` correction: **PASS**, and outer `h = 3`
   on both edges is also fixed (A6). 7. `td <= 14` counterexample: a
   consistent `td = 12` typed ledger exists at the pinned-arithmetic
   tier (§5); actual-tier realization is open by nature.

## 8. Verdict, maximum safe promotion, exclusions

**Primary verdict: `FAIL`** for the target's headline results — (ASM) at
`mu >= 3`, (U2F) `td >= 15`, §0's "not a threat to any current
`td <= 12` panel", and §4's removal "from every … `td = 12` source
panel". The failing step is load-bearing and is refuted, not repairable
by wording: the frozen basis itself records merge-free M-jumps and a
`b = 2` pole arriving at multiplicity 3.

**Maximum safe promotion** (all proved here from the five frozen sources
alone, all floors, all inheriting only the Prop 5.8 generic-`a` rider):

1. ASM′, NM′, the `td >= 3*beta` route floor, and the corrected-family
   floor `td >= 3*max(beta, 2*alpha) >= 12` of §6;
2. hence: the corrected `t == 5 (mod 6)`, `K == 1 (mod 6)` family — and
   any local member with the same arities and all three arrival
   multiplicities `>= 2` — cannot land in an actual pole tree at
   `td <= 11`; in particular **every `td = 8` panel exclusion in the
   target survives** (even multiplicity-free at `td <= 8` via
   `3*beta >= 9`);
3. ASM verbatim for arrivals with `mu <= 2`;
4. strong ASM `min(2*beta, mu*alpha)` as a *conditional* consumer,
   attachable only with a pole-adjacent, edgewise-`V_{2,a}`, or direct
   `M_H | b_P` certificate (A9).

**Explicit exclusions from promotion:** the `td = 12` panel removal
(the `td12 m3 [2,2,2]` skeleton remains open and meets the floor with
equality); `td >= 15` in any form; ASM at `mu >= 3`; any compiler rule
attaching unconditioned `min(2*beta, mu*alpha)` to arbitrary arrivals;
any attainment reading of the floors; any claim that the §5 ledger is an
actual counterexample. The family's local/formal-tier validity
(N1-repaired ray, T1-alive) is untouched by this review.

---

## Seal

Body = the first 23137 bytes of this file: all bytes strictly before this
seal section's heading line, which is the only line of the file beginning
with the seal heading marker.

- Body byte count: `23137`.
- Body SHA-256:
  `1ca3948f97114d56e1c5aae916fa086d459d036550f2e218bcf31923710c3e12`.
