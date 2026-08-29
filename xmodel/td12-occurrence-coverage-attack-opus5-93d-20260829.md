# Independent attack — global occurrence/coverage versus `td=12`

Date: 2026-08-29 UTC
Producer: Opus 5, independent whole-portfolio researcher (primary, not review)
Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`
Lifecycle: `PRIMARY / INTERFACE_NO_GO_PROVED / NO_OCCURRENCE_ASSERTED`
Writes: this path only, plus `/tmp/occ` scratch.
`charge_basis`: **ABSENT**. No new exit price is asserted anywhere below.
Every `lambda` used is a consumed **promoted `REPRESENTATIVE` AF2/P0 floor**;
no floor is read as attainment and no `FULL_ACTUAL_EXIT` is claimed.

---

## 0. Disposition

Four results, in decreasing order of confidence.

1. **The occurrence arrow is absent, and it is absent for a structural
   reason, not for want of effort.** Every promoted premise about a
   hypothetical minimal counterexample is one of: an existential selection,
   a `td`-preserving normalization, a **floor**, or a **fixed-`td`**
   finiteness statement. None of these four kinds can entail `td=12`, and
   their conjunction cannot either. Section 4 proves this at the level of
   logical interfaces.

2. **A concrete abstract admissible family escapes the proposed
   implication.** I construct `U1*(r)`: for every **odd** `r >= 3`, an
   abstract configuration of type `(2,3)` with `r` pole entries `(1,2,3)`,
   a `U1` star merge of arity `r` with equal arrivals `(mu,w)=(2,3/2)`,
   `eps=k=lex=0`, and `td = 4r`. It satisfies **every** promoted
   configuration-level axiom I could locate, including `T7`, `MP0`/`MP1`,
   `St 8.4`, the reviewed `U1` Theorem B/C/C' closed forms, `MP2`, `N1`,
   `R1.0`, `R1.3`/`R1.4`, Proposition 8.1(iv)/`T1`, the reviewed `ASM'`/`NM'`
   source-mass floors (with **equality**), and the repaired Corollary 7.1 /
   Statement 9.4 budget. Its `r=3` member **is** the campaign's reviewed
   `td=12`, `m=3`, `[2,2,2]` record, reproduced independently here, ratio
   `B/A=9/8` and all. Nothing in the recorded interface distinguishes `r=3`.

3. **The campaign's sharpest local mechanisms have the wrong monotonicity.**
   In `U1*(r)` the one-step trunk terminals are indexed exactly by the
   divisors `k | 3r-1` with `k <= r-1`, and satisfy the exact closed forms
   ```text
   nu_F = 3r + 2(3r-1)/k,   M_F = k+2,   w_F = (k+1)/(k+2),   j = 1,
   psi = k+1,   and at k=1: nu_F = 9r-2, kbar_F = 6r-1, X_F = 9r-2,
   lambda_floor = 3r - 1   (independent of k),
   budget = td - 1 - psi = 4r - k - 2,   slack = r - k - 1.
   ```
   The slack **grows linearly in `td`**. The `td=12` "slack one" and the
   sibling's "budget saturation" — the two facts that make the reviewed
   exact-charge theorem sharp — are the `r=3` specialisation of a family in
   which every later member is strictly looser. A budget layer whose kill
   power decays in `td` cannot supply an upper bound on `td`.

4. **The number `12` is `3 x 4`, where only the `4` is premise-derived.**
   `4 = min{ max(beta,2*alpha) : 2 <= alpha < beta, gcd = 1 }`, attained
   only at `(2,3)`. The factor `3` is a **hypothesised merge arity**. The
   reviewed source-mass floor therefore proves `td >= 4R` for a merge of
   arity `R` all of whose arrivals have multiplicity `>= 2`, with equality
   forcing type `(2,3)` and `R` poles `(1,2,3)`. Read `R`-uniformly, the
   reviewed statement says nothing about `12`.

**Decision on the prompt's question 3: NO.** Current premises cannot force
`td=12`, and cannot force the `U1` equality route. The no-go is proved in
Section 4 at interface level, and separately witnessed by `U1*(r)`.

Nothing here proves or disproves JC2, produces a `PairRef`, a source value,
an occurrence, an attainment, a degree ceiling, or a counterexample. A lower
floor is not attainment; a formal configuration is not an actual polynomial
map. `U1*(r)` is an **abstract admissible configuration**, not a Keller pair.

---

## 1. Sources read and rehashed

Recomputed on this basis before use:

```text
a98ad176a916c400f0aa0bc115ab69c6185b3986eedaac5542f1dd2a180ad849  xmodel/td12-source-interface-gap-coordinator-audit-sol56-20260829.md
f602fb81b6e90272462b2263eaeb0eb40550b7d4ce1b87d0e9916bb45322c10b  xmodel/ideation-20260829T1517Z-synthesis.md
b15eea584a99e7576c81d713dab549e6c2d00ee6fca3e78232fda489d750d981  APPROACHES.md
bc210a7a9a887d573fc5b870dc9eaace2fd12a434cefd5ddc547bb4342c87602  PROGRESS.md
3b8b00cdaedb6bbc4057206f280d219364bb397bd1186cb0779679c538605c7a  AUDIT.md
29270ff6192fcee2eecb4ba68578010b2b3f0c5519feb71dc67baa7f68bb784b  ladder/REDUCTION.md
9e23c5e79a5af2dc207e49481bbaf151173391c558ec86ddb4fae44603a0d297  ladder/TRANSPORT.md
b3993495eff1913b09f1fc6750b2af08ecf90a9f9f38c97f85be47ba9c9a54d0  ladder/BOOK-OFFAXIS.md
c66ff941d3954143b51f4dc2ac0dd77d6e1d5be81c0d6cdca3e1bd2a058b9a64  ladder/SHEET6-2POLE.md
28f9918e18eae42580584afbd98a36418ac98ecabf078c829e20484159baeb3c  xmodel/m2-u2-one-p0-source-mass-floor-r1-sol56-20260829.md
f9dd2035bbe5a47561cce263ba1288a9245526dec748c3ef031545e443bf510f  xmodel/m2-u2-one-p0-source-mass-floor-hostile-review-fable5-c359-20260829.md
09ac8eefc75cafa777b1164a65eecd520427ba61a7000c79d33d7d5e454f6219  xmodel/m2-u2-one-p0-source-mass-floor-hostile-review-fable5-c359-20260829-r1-erratum-sol56.md
63a1f15e4fc7bc46a746f18f51f7a5984863af09c749af1708c4592f725bf64c  xmodel/m2-u2-one-p0-td12-global-budget-kill-r1-correction-sol56-20260829.md
8cb13514cc5bd78ea31583af59892ea4cfc04413eef641f25620dec2bc34d95b  xmodel/m2-two-pole-full-actual-first-separation-coordinator-integration-sol56-20260829.md
599e2a9123194c580b89b822f5b7a218fa5e9735b16bcb744e0f0e4231584271  xmodel/m2-td12-u1-trunk-consumer-primary-grok46-20260829.md
52ffafa2e79823e275e084d9d3c3a36329401cc9449a6e572379ce1ee0390b69  xmodel/m2-td12-u1-sibling-exact-charge-r1-sol56-20260829.md
8755bd5d3d1cd2721d32e5956c5b139b2cc6e0e805662d5278ededff896135ba  xmodel/m2-equal-join-semilinear-primary-research-hostile-review-grok46-20260829.md
c6c1d5fe6df7796cac468fb81db16b3bbce777c305d869b9ad46cbb88a16f339  xmodel/td12-global-source-bridge-b-coordinator-integration-sol56-20260829.md
c253bd12d205eed7c01e42a21204c5735d0f5cba70dce1d962fb8744dbd95eb6  xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md
```

`ladder/REDUCTION.md` and `ladder/TRANSPORT.md` hash byte-identically to the
custody list of the coordinator source-interface audit (`29270ff6...`,
`9e23c5e7...`), so the interface I attack is the one that audit described.

No access of any kind was made to `jc2-lean`. No web, AWS, commit, push,
canonical edit, heavy CAS, or external message. All arithmetic below is
exact integer/`Fraction` desk arithmetic; the two short scripts are listed
in Section 7 and were run only under `/tmp/occ`.

---

## 2. Deliverable 1 — exact quantified implication graph

### 2.1 Conventions on quantifiers

Existential choices are **not** merged. I write `!E` for a choice made once,
and I tag every downstream object with the choices it depends on. The graph
below has three separate existential layers that later files sometimes
telescope:

- `!E1`: the choice of a counterexample (one pair, once);
- `!E2`: the choice of a fibre value `a` (per fibre; the entry datum, the
  tree, the merge skeleton and every route label are `a`-dependent);
- `!E3`: the choice of a route/record inside the fibre `a`.

Arrow marks: **P** proved (from premises listed, at the stated trust tier);
**C** conditional (needs a named unproved hypothesis); **F** false as
stated; **A** absent (no argument at all).

### 2.2 The graph

```text
(N0)  JC2 is false.
        | P    [definition; REDUCTION T1's corrected predicate:
        v       "F is not a polynomial automorphism", not "not linear"]
(N1)  !E1 exists a Keller counterexample F0=(f0,g0) over C.
        | P    [GGV1 Def 4.3 + standardisation + Cor 5.21, refereed;
        |       REDUCTION T2. QUANTIFIER: existential over ALL
        v       counterexamples; F0 is discarded, not normalised]
(N2)  !E1' exists a globally GGV-minimal standard pair (P,Q), coprime
      m,n>1, base A=(a,b) with 0<a<b, both NE corners present.
        | P    [TRANSPORT Thm 1.1 (coordinate-cusp LND), Thm 2.1 (orbitwise
        |       lex-minimality), Thm 3.1 (two-chart normal form) and
        v       (4.1)-(4.5); td preserved, GGV ledger recoverable]
(N3)  (f,g)=C o (P,Q) o R is Sigray-normalized of type (alpha,beta),
      2<=alpha<beta, gcd=1; deg(f,g)=(alpha(a+b), beta(a+b)); td unchanged.
        | P    [Zoladek 2008 Thm 6.12, refereed]
(N4)  td = d >= 6.
        |
        |--X-- A  NO ARROW to any upper bound on d.
        |         (see 2.3; the Bezout ceiling d <= alpha*beta*(a+b)^2 is
        |          real but conditional on an absent bound for a+b.)
        v
(N5)  FOR ALL a in C satisfying the promoted Prop 5.8 rider:
      the fibre R_a carries a decorated Eggers-Wall tree; T_{a,pole} is the
      pole-leaf set; d = sum_{P in T_{a,pole}} Lambda(P).
        | C    [Sigray SS3-6 + SIGRAY-AUDIT perimeter (audited only pp.7-30);
        |       SOL-PROP58 every-fibre repair consuming Chau99 Thm 4.4;
        v       MP0/MP1. Unrefereed thesis tier + distributed repairs.]
(N6)  Lambda(P) = a_P b_P alpha beta / nu_P >= beta >= 3, with
      (nu|alpha and nu|b*beta-1) or (nu|beta and nu|b*alpha-1);
      s := |T_{a,pole}| <= d/beta; beta <= d; entry menu E(d) is FINITE.
        | P (arithmetic) / C (the M=b pin and the pole identification)
        |
        |--X-- A  NO ARROW selecting a type, a value of s, on/off-axis
        |         status, or a particular member of E(d).
        v
(N7)  !E3 the actual merge skeleton and its labels inside U_a.
        |
        |  P : U_a is a finite rooted tree, s leaves, <= s-1 merges (MP0/MP1)
        |  P : arrival multiplicity mu_e | M_{H_e} (St 8.4)
        |  P : ASM'/NM' floors (reviewed): for an actual merge of arity R
        |      with arrivals mu_1..mu_R,  d >= sum_e c(mu_e),
        |      c(mu)=max(beta,2alpha) if mu>=2 else beta
        |  F : the producer's strong ASM min(2beta, mu*alpha) at mu>=3
        |      (refuted by Fable review A3/A9 -- merge-free does not give
        |       M_H | b_P; a b=2 pole may arrive at multiplicity 3)
        |  A : no arrow forcing R, forcing all mu_e>=2, or forcing s>=2
        v
(N8)  A NAMED ACTUAL OCCURRENCE (td12/U1 vertex, B25 cell, S17 cell).
        ^
        |--X-- A  ABSENT. This is the whole gap.
```

Two additional arrows that are sometimes read as part of the chain and are
not:

```text
(N3) --F--> "the GGV corner/admissible-chain datum determines a specified
             Sigray tree datum"                       [G2-PSC; REDUCTION
             CRITICAL 3; TRANSPORT SS4 last paragraph, SS8 CONJECTURE T]
(N7) --C--> "every all-b=1 configuration lands at its marked first
             jump/root event in BOOK(s,d)"            [T8 perimeter
             P1-P4/H1; local marked-event tier only; and see 3.2(a):
             the marking is UNDEFINED in the off-axis sector where
             td12/U1/B25/S17 live]
```

### 2.3 What the graph does and does not deliver at `td=12`

Independent desk reproduction of the entry layer (Section 7, script A):

| `td` | entries, all `s` | off-axis entries | types occurring |
|---:|---:|---:|---|
| 6 | 7 | 2 | `(2,3),(2,5),(3,4),(3,5),(5,6)` |
| 8 | 7 | 4 | `(2,3),(2,7),(3,4),(4,7),(7,8)` |
| 12 | 35 | 15 | 14 types, `(2,3)` among them |
| 20 | 93 | 51 | 20 types |
| 24 | 239 | 138 | 30 types |

The menu is nonempty for **every** `d >= 6`: at type `(2,3)` the pole
entries `(1,1,2)` and `(1,2,3)` realise `Lambda = 3` and `Lambda = 4`, and
`{3x+4y : x,y >= 0}` contains every integer `>= 3` except `5`. So the entry
layer excludes no topological degree at all above the published `d >= 6`.

At `td=12` my independent enumeration gives off-axis panels
`s=1: 10`, `s=2: 4`, `s=3: 1`, `s=4: 0`, and the unique `s=3` off-axis entry
is exactly

```text
type (2,3),  poles (a,b,nu) = (1,2,3)^3,  Lambda = (4,4,4),  M = [2,2,2],
```

reproducing `BOOK-OFFAXIS.md` SS1's headline row `td12 m3: [2,2,2]` from
first principles. **That uniqueness is a consequence of assuming
`td=12`, `s=3`, and off-axis; it is not a premise that produces `td=12`.**
It also degrades immediately: at `td=20, s=5` there are four off-axis
entries, at `td=28, s=7` there are ten. The apparent canonicity of the
`td12/U1` row is an artifact of it being the smallest case.

The single-pole escape is cheaper still: `td=12` has 10 off-axis `s=1`
entries and, per `REDUCTION.md` HIGH 1, 71 surviving single-pole TDU search
classes with four solver-`OPEN` kinds and one depth frontier. A single-pole
configuration has **no merge**, so `ASM'`, `NM'`, `U1`, `U2`, `B25` and
`S17` are all vacuous on it. Any occurrence theorem must first exclude
`s=1`, and nothing does.

---

## 3. Deliverable 2 — the strongest honest occurrence/coverage theorem,
## and where the construction fails

### 3.1 Theorem OC (first-separation coverage floor)

This is the strongest statement I can prove from the recorded interface. It
is deliberately weaker than any "landing" claim.

> **Theorem OC.** Assume JC2 is false. Select `(P,Q)` by `T2` and normalize
> by `TRANSPORT` Theorems 2.1/3.1 to `(f,g)` of type `(alpha,beta)`,
> `2 <= alpha < beta`, `gcd(alpha,beta)=1`, `td = d >= 6`. Let `a in C`
> satisfy the promoted every-fibre Proposition 5.8 rider. Then:
>
> 1. `d = sum_{P in T_{a,pole}} Lambda(P)` with
>    `Lambda(P) = a_P b_P alpha beta / nu_P >= beta`, and
>    `s := |T_{a,pole}| <= d/beta`, `beta <= d`;
> 2. the entry datum `E_a` lies in the finite menu `E(d)` of `T7`;
> 3. `U_a` is a finite rooted tree with `s` leaves and at most `s-1`
>    merges; over the set-theoretic union of the pole paths the actual
>    first-separation carriers form a complete set of pairwise-distinct
>    same-ray cv flags with unique outer attachments, shared suffix counted
>    once, pole arrivals removed before pricing, and total actual weight
>    `sum wt <= d - 1 - psi` (repaired Corollary 7.1* / Statement 9.4 (25));
> 4. for every **actual** merge `G` of arity `R` with arrival
>    multiplicities `mu_1,...,mu_R`,
>    ```text
>    d >= sum_{e=1}^{R} c(mu_e),   c(mu) = max(beta,2*alpha) if mu>=2,
>                                  c(mu) = beta              if mu=1;
>    ```
> 5. hence if some actual merge has arity `R` with **all** `mu_e >= 2`,
>    ```text
>    d >= R * max(beta, 2*alpha) >= 4R,
>    ```
>    and equality **forces** `(alpha,beta) = (2,3)`, `s = R`, and all `R`
>    pole entries equal to `(a,b,nu) = (1,2,3)` with `Lambda = 4`.

Proof of the new content, item 5. Clause 4 is the reviewed `ASM'`/`NM'`
pair (Fable review SS6, promotion item 1) composed with A5 disjointness of
the `R` incoming pole-leaf sets; I do not reuse the producer's refuted
strong `ASM` at `mu >= 3`. For the numeric part, minimise
`m(alpha,beta) = max(beta, 2*alpha)` over coprime `2 <= alpha < beta`:
`m(2,3)=4`, `m(2,5)=5`, `m(3,4)=6`, `m(3,5)=6`, `m(2,7)=7`, `m(3,7)=7`,
`m(4,5)=8`, and `m >= 2*alpha >= 6` for every `alpha >= 3`, while for
`alpha = 2` we have `m = max(beta,4) >= 4` with equality only at
`beta in {3,4}` and `gcd(2,4) = 2`. Hence `min m = 4` uniquely at `(2,3)`.
Equality in clause 4 forces each of the `R` incoming subtrees to carry pole
mass exactly `max(beta,2alpha) = 4` and forces no pole to lie outside them,
so `s = R`; a subtree with two poles would carry mass `>= 2beta = 6 > 4`,
so each carries exactly one pole with `Lambda = 4`; and `Lambda = 4` at type
`(2,3)` solves `6ab/nu = 4` with `nu | 3` and `nu | 2b-1`, whose only
solution is `(a,b,nu) = (1,2,3)`. QED.

**The `R`-uniform reading is the point.** The reviewed Fable statement
`td >= 3*max(beta,2alpha) >= 12` is clause 5 at `R = 3`. The `3` is the
route's hypothesised arity (two inner arrivals plus one sibling), the `4` is
the only premise-derived constant. Read as written, the reviewed theorem
proves `td >= 4R` and says nothing that singles out `12`.

### 3.2 The six required tests

I ran each construction the prompt names against Theorem OC and against the
`td=12` off-axis sector. Verdicts are definite.

**(a) Earliest-marked-event construction — `UNDEFINED` in the target
sector, not merely incomplete.**

`REDUCTION` `T8`(2) marks "the first event that breaks `M=1`", and `T8`(3)
uses the `w`-closure "on pure `M=1` segments". Both are predicated on an
all-`b=1` ancestry. In the off-axis sector `M_P = b_P >= 2` **at the pole
itself** (`MP4`/`TDUNIFORM` R2-R4 pin `M = b`), so there is no `M=1`
baseline and no first `M`-breaking event exists to mark. `BOOK-OFFAXIS`
SS2(c2) independently records the same collapse on the transport side:
"NO `w`-alphabet, NO equal-`w` join law, NO root `w<1` window on off-axis
chains at printed tier". This is a definitional obstruction, not a coverage
hole: the object `BOOK(s,td)` marks does not exist for `b >= 2` entries.
Since the entire `td12/U1/B25/S17` complex is off-axis (`b=2`), the
strongest reviewed landing theorem is *inapplicable to the sector it is
being asked to cover*.

Substitute marking: **first merge**. For each pole `P`, let `G(P)` be the
first merge on the path from `P` to the root. It exists whenever `s >= 2`,
because in a finite rooted tree with `>= 2` leaves every leaf-to-root path
passes through the deepest common ancestor of that leaf with another. It is
**undefined for `s = 1`**, and `s = 1` is live at every composite `td`
(10 off-axis entries and 71 TDU classes at `td=12`). So even the substitute
marking is not total.

**(b) Actual-path termination — `PROVED`, but with no effective length
bound.**

`MP0` makes `U_a` a finite rooted tree whose leaves are exactly the pole
vertices, so the actual path from any pole to the root is finite and the
walk terminates. That is genuine and needs no budget. What fails is
*effectivity*: `P0`/`P2` price arriving edges and `lex` at zero, and a clean
step (`k = 0`, no northeast orbit) costs `lambda = 0`. Arbitrarily long
zero-price neutral chains are therefore invisible to the Corollary 7.1
budget, which is exactly `CRITICAL 5`'s "neutral fibres retain unbounded
last-vertex indices and `kbar`". Termination without a length bound does not
produce a finite record.

**(c) Complete pole-side subtree — `PROVED as a floor only`.**

The promoted attachment theorem (`c2141599...` integration) gives, on one
fixed fibre, `I_P(t) = I_Q(t) iff t <= O(P,Q)`; separated rays cannot
remerge; every actual up non-chain microchild at `F in U` has a full set
`E_all(F,d)` of distinct same-ray cv flags with unique outer attachment `F`;
full sets from distinct directions or attachments are pairwise disjoint;
shared suffix vertices occur once. So the pole-side subtree *is* complete
and its carrier set is well defined. But the mandatory carrier dictionary is
explicit:

```text
FULL_ACTUAL_EXIT = FULL_ACTUAL_FIRST_SEPARATION
                 = complete set of distinct actual cv carriers + a lower
                   floor only.
```

Completeness of the carrier set is **not** attainment of the price. Every
number I use downstream is the weaker `REPRESENTATIVE` AF2 floor. No
upgrade by analogy is performed here.

**(d) Neutral-transition quotienting — `SOUND on chain edges`,
`UNSOUND at case-III merges and at every index-reading consumer`.**

This one has a positive part that I did not expect and should be recorded.
On a chain edge the promoted formulas are
`kbar_F = l * w_G * dq_F / E_F`, `w_F = w_G * l*(dq_F-1)/(nu_F * E_F)`
(`R1.4`, dirty) and the `R1.2` clean analogue; the successor's
`(w_F, M_F, kbar_F, X_F)` depends on the parent **only through `w_G`**, and
the parent's `M_G` enters only through the arrival constraint `l | M_G`.
Hence `(w,M)` is a sufficient statistic for the one-step priced chain menu,
and the reduced `(w,M)` automaton is a genuine bisimulation there. That is
why the cap-free chain theorem is legitimate.

It is **not** a bisimulation for:

- **case-III (0-arrival) merges**, where the printed handshake is
  `what_0 = nu_H * w_H` and the promoted E5 form is `what_0 = nu_G * w_U`;
  either way an index outside `(w,M)` is read (this is the FALLACY-v2
  "target/arrival index" item, and the Fable/Sol fork on which side is
  live);
- the **arrival-multiplicity certificate** `mu_e | M_{H_e}` at a merge,
  which reads the incoming vertex's `M`, not the reduced pair alone;
- **Statement 3.9 sheet transport**, which reads `deg p_{h,G}` and the
  tower index `i`, both invisible to `(w,M)`;
- **`N1` and `R1.0`** (`gcd(kbar,nu)=1`, `gcd(M,nu)=1`), which read `nu`.

So a blanket neutral quotient is unsound; a typed quotient (chain edges
only, case-I/II arrivals only) is sound and is what the automaton actually
proves. Any coverage theorem must carry the edge type with the state.

**(e) Unused branches — `RETAINED for price, DISCARDED for structure`,
and that is correct for `U_a` but not for the merge siblings.**

At a dirty chain vertex, `R1.3`(i) forces every non-chain orbit to be
northeast: a searrow non-chain root would make `F` a merge by the
`D5(c)`/Proposition 6.8 pole-manufacture. So the `k` unused orbits at a
chain vertex are **not** pole-side; they leave `U_a` upward and contribute
only price. Recording `(k, m_j)` suffices for the budget and no subtree is
lost. That part is sound.

The genuinely lossy case is the **merge sibling**: the other incoming
subtrees at a merge *are* pole-side, and their poles are counted in `d` by
the mass identity. The reviewed one-P0 U2 correction already had to discharge
an explicit "unused-sibling debt" via `lambda >= 1` plus disjointness. In
Theorem OC clause 4 the sibling appears as a full `c(mu_e)` mass term, which
is the honest accounting.

**(f) Downstream-context preservation — `NOT PRESERVED` in artifacts,
`NOT SPECIFIED` in theorems.**

`REDUCTION` `MEDIUM 2` is explicit: the on-axis engine aggregates a cell
over all supporting join contexts, uses "any-context survival wins", and
truncates entry tags. `CRITICAL 4` adds that the marked-first-event theorem
supplies "no typed configuration-to-record map, no fail-closed coverage
certificate, and no record of every unused branch and downstream context".
`CRITICAL 4` also settles the codomain question negatively: the reviewed
`U1` families are arithmetic progressions in the merge index `n`, so even at
**fixed** `td` and **fixed** entry the configuration set is infinite, and the
minimal codomain is family records, not a finite literal-cell list.

### 3.3 What Theorem OC cannot be pushed to, and why

Composing (a)-(f): the map `configuration |-> record` is (a) not total
(undefined off-axis by the `M=1` marking, undefined at `s=1` by the
first-merge marking), (b) terminating but not length-bounded, (c) complete
only as a floor, (d) quotientable only after edge typing, (e) sound on
chain extras but obligated on merge siblings, (f) not context-preserving in
any implemented artifact. Each failure is individually repairable in
principle. None of the repairs would produce `td=12`, because none of them
is `td`-monotone. Section 4 makes that last sentence a theorem.

---

## 4. Deliverable 3 — the no-go, and the escape family

### 4.1 The interface no-go

Let `Sigma_cfg` be the set of promoted premises that are statements about
the **configuration data** of an actual normalized counterexample and one of
its fibres. Concretely, `Sigma_cfg` is the conjunction of:

```text
(A1) type data: 2 <= alpha < beta, gcd(alpha,beta)=1                [T4/TRANSPORT 3.1]
(A2) td >= 6                                                        [Zoladek 6.12]
(A3) mass identity  td = sum_P Lambda(P), Lambda = a b alpha beta/nu [T7]
(A4) pole arithmetic: Lambda >= beta; (nu|alpha & nu|b*beta-1) or
     (nu|beta & nu|b*alpha-1); M_P = b                              [T7/TDUNIFORM R2-R4/MP4]
(A5) MP0: U_a finite rooted tree, leaves = poles;
     MP1: non-merge vertices regular, incoming subtrees disjoint,
          sum_G (R_G - 1) = s - 1
(A6) St 8.4: mu_e | M_{H_e} at every arrival
(A7) MP2: interior M >= 2
(A8) N1: gcd(kbar,nu)=1 at nu>=2;  R1.0: gcd(M,nu)=1, dq = 1 mod nu
(A9) chain calculus R1.1-R1.5 (shape, clean/dirty transport, w-closure),
     with (S), (NE), (R) and the divisor law E | l*num(w)*T
(A10) U1 Theorem B/C/C' closed forms at an equal-arrival merge
(A11) Prop 8.1(iv) / T1-GEN in the normalized l1_ode_check form
(A12) repaired Cor 7.1* / St 9.4 (25): sum lambda^exit <= td - 1 - psi,
      with the AF2/P0 floor lambda >= max(1, ceil(X/m - kbar)) per NE orbit
      and lambda = 0 on clean edges, merges, and pole vertices
(A13) reviewed ASM'/NM' arrival-subtree mass floors
(A14) the first-separation attachment/MFE theorem (disjointness, unique
      attachment, shared suffix counted once)
```

> **Theorem NG (interface no-go).** For every odd `r >= 3` there is an
> abstract configuration `U1*(r)` satisfying every axiom of `Sigma_cfg`,
> with `td(U1*(r)) = 4r`. Consequently `Sigma_cfg` does not entail
> `td = 12`, does not entail `td <= N` for any `N`, and does not entail the
> `U1` equality route at any particular arity. Any proof of
> "counterexample `=>` `td=12`" must therefore consume a premise outside
> `Sigma_cfg` — i.e. a statement about **actual realizability** that no
> current file supplies.

The theorem is a soundness/semantics statement about the recorded interface.
It does **not** assert that `U1*(r)` is realized by a polynomial pair for
any `r`, including `r = 3`. Its force is exactly this: no amount of further
work *inside* `Sigma_cfg` can produce `td=12`.

### 4.2 The escape family `U1*(r)`

Fix an odd `r >= 3`.

**Entry layer.** Type `(alpha,beta) = (2,3)`; `s = r` pole entries all equal
to `(a,b,nu) = (1,2,3)`; `Lambda = 1*2*2*3/3 = 4` each; `M_P = b = 2`;
`w_0 = a(b(alpha+beta)-1)/(b nu) = (2*5-1)/6 = 3/2`. Checks: `nu = 3 | beta`
and `nu = 3 | (b*alpha - 1) = 3`; `Lambda = 4 >= beta = 3`; `L6`
`gcd(a(alpha+beta),nu) = gcd(5,3) = 1`; mass `td = 4r`;
`s = r <= td/beta = 4r/3`. All of `(A1)-(A4)` hold, for every `r >= 1`. The
`a`-dependence, on-axis/off-axis status and `s` are *choices*, exactly as
Section 2.2 marks them.

**Tree layer.** One `U1` star merge `G` of arity `R = r`, all `r` pole
paths of length zero (pole-adjacent arrivals), each arriving with
multiplicity `mu = 2`, `eps = 0`, `k = lex = 0`, equal `w_e = 3/2`.
`MP0`/`MP1`: one merge, `sum(R-1) = r-1 = s-1`. `St 8.4`: `mu = 2 | M_P = 2`.
`(A5)`, `(A6)` hold for every `r >= 2`.

**Merge data.** The reviewed U1 closed forms (Theorem B, CONFIRMED in the
Grok hostile review SS4.1) give, at merge index `n`:

```text
dp = eps + nu*r*mu = 2rn,        dq = 1 + r n,      E = mu - eps = 2,
kbar = mu*w*dq/E = 3(1+rn)/2,    X = mu*w*dp/E = 3rn,
w_tr = mu*w*r/E = 3r/2,          M = gcd(mu-eps, r n + 1) = gcd(2, rn+1),
T = r(mu-eps) = 2r,              lambda_G = 0 (eps = 0).
```

`(A7)` `MP2` forces `M >= 2`, i.e. `rn` odd, so **`r` must be odd**;
`kbar in Z` is the same condition; `(A8)` `N1` gives
`gcd(kbar, n) = gcd(3, n) = 1`, i.e. `3 does not divide n`. So the
admissible merge indices are `n odd, 3 ∤ n`, i.e. `n = ±1 mod 6` — the
**same** progression for every odd `r`, and exactly the reviewed
`n mod 6 in {1,5}` of the `r=3` record. At `r = 3` this reproduces
`dp = 6n`, `dq = 3n+1`, `kbar = 3(3n+1)/2`, `X = 9n`, `w_tr = 9/2`, `M = 2`
byte-for-byte.

`r` even is `MP2`-dead here, which independently reproduces the campaign's
`m = 2` statement and is consistent with "every `td = 8` panel exclusion in
the target survives". So `U1*(r)` exists exactly for `r in {3,5,7,9,...}`,
i.e. `td in {12, 20, 28, 36, ...}`.

**Trunk layer.** One dirty `P0` step from `(w_G, M_G) = (3r/2, 2)` with
arrival `l = 2 | M_G`, `k` non-chain orbits all of multiplicity `m_j = 1`
(forced by `R1.3`(ii): `m_j < dp/dq < l = 2`), `lex = 0` (forced by
`R1.3`(iii): `dq < dp`), `eps = 0`. Then

```text
dp = nu(2+k),   dq = nu(1+k)+1,   E = 2 dq - dp = nu k + 2,
kbar = 3r*dq/E,  X = kbar*dp/dq = 3r*dp/E,  w_F = 3r(1+k)/E,  M_F = gcd(dp,dq).
```

Imposing the `P1` terminal conditions `w_F < 1`, `M_F >= 2`,
`j = M_F(1 - w_F) in N*`, together with `kbar in Z`, `N1`, `R1.0`, `(S)`,
`(NE)`, `(R)` and the divisor law `E | l*num(w_G)*T`, yields exactly:

> **Trunk law for `U1*(r)`.** The one-step `P1`-fitting dirty terminals are
> indexed precisely by the divisors `k` of `3r - 1`, and
> ```text
> nu_F = 3r + 2(3r-1)/k,       M_F = k + 2,        w_F = (k+1)/(k+2),
> j = 1,                        psi = ceil(M_F/j) - 1 = k + 1,
> per-orbit floor  X - kbar = (3r-1)/k,
> total floor      lambda = k(X - kbar) = 3r - 1     (independent of k),
> shared budget    td - 1 - psi = 4r - k - 2,
> slack            = (4r - k - 2) - (3r - 1) = r - k - 1,
> so the terminal fits iff  k <= r - 1.
> ```

Derivation of the two closed forms that carry the weight.
`w_F = (k+1)/(k+2)` forces `3r(1+k)(k+2) = (k+1)(nu k + 2)`, i.e.
`nu k = 3r(k+2) - 2`, so `nu = 3r + (6r-2)/k` and `E = nu k + 2 = 3r(k+2)`.
Then `nu - 1 = (3r-1)(k+2)/k`, and

```text
X - kbar = 3r(dp - dq)/E = 3r(nu - 1)/E = 3r * (3r-1)(k+2)/k / (3r(k+2))
         = (3r - 1)/k,
```

so the total charge floor over the `k` orbits is `k * (3r-1)/k = 3r - 1`,
identically in `k`. Verified exactly for all odd `r` from `3` to `59`
(Section 7, script B): the admissible `k` are precisely the divisors of
`3r-1`, all listed identities hold with zero failures.

`(A11)` **`T1` survives at every `r`.** At `k = 1` the cell has
`p = (t-A)^2(t-B)`, `q = eta (t-A)(t-B)`, `t = eta^{nu_F}`, and
`rho = dp/dq = 3nu_F/(2nu_F+1)`. The normalized Proposition 8.1(iv)
identity of `l1_ode_check.py` reduces to

```text
C_iv(t) = rho(t-A)(t-B) + nu_F t[(rho-2)(t-B) + (rho-1)(t-A)],
```

whose `t^2` coefficient `rho + nu_F(2rho - 3)` vanishes identically because
`rho = 3nu_F/(2nu_F+1)`; the remaining linear condition has one-dimensional
kernel with

```text
B/A = (nu_F + 2)/(nu_F - 1) = 3r/(3r - 1),      C_iv = rho A B != 0.
```

At `r = 3`: `nu_F = 25`, `rho = 25/17`, `B/A = 9/8`, `C_iv = rho A B` —
identical to the reviewed record. At `r = 5`: `nu_F = 43`, `rho = 43/29`,
`B/A = 15/14`. At `r = 7`: `nu_F = 61`, `B/A = 21/20`. `A != 0`, `B != 0`,
`A != B`, `rho notin {1,2}` in every case.

`(A13)` **`ASM'`/`NM'` is saturated at every `r`.** The star merge has
`R = r` arrivals, all `mu_e = 2 >= 2`, so `NM'` gives
`td >= r * max(beta, 2alpha) = 4r`, and `td = 4r` exactly. The reviewed
floor is met with **equality for every odd `r`**, and Theorem OC clause 5
then re-derives type `(2,3)` and `r` poles `(1,2,3)` — the same forcing the
campaign observed at `r = 3`, now visibly `r`-uniform.

`(A12)` **Budget.** All `r` pole vertices and the merge price zero; the
trunk terminal prices `3r-1`; the shared ceiling is `4r - k - 2`. Fits for
`k <= r-1`.

**Instances.**

| `r` | `td` | `w_tr` | fitting `k` | `nu_F` (`k=1`) | `kbar` | `X` | `lambda >=` | budget | slack |
|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|
| 3 | 12 | `9/2` | `1,2` | 25 | 17 | 25 | 8 | 9 | 1 |
| 5 | 20 | `15/2` | `1,2` | 43 | 29 | 43 | 14 | 17 | 3 |
| 7 | 28 | `21/2` | `1,2,4,5` | 61 | 41 | 61 | 20 | 25 | 5 |
| 9 | 36 | `27/2` | `1,2` | 79 | 53 | 79 | 26 | 33 | 7 |
| 11 | 44 | `33/2` | `1,2,4,8` | 97 | 65 | 97 | 32 | 41 | 9 |

The `r = 3` row is the campaign's reviewed `td=12` first trunk consumer,
including the two `P1`-fitting terminals `(2/3,3)` at `nu_F = 25` with slack
one and `(3/4,4)` at `nu_F = 17` with slack zero, and including the total
sibling floor `8 = 2 x 4`. I obtained it from the general law, not by
copying the record.

### 4.3 Three consequences that sharpen the no-go

**(i) The `12` is `3 x 4`.** Only `4 = min_{type} max(beta,2alpha)` is
premise-derived. The `3` is a hypothesised arity. Nothing in `Sigma_cfg`
constrains arity: `MP1` allows any `R <= s`, and `s <= td/beta` is an upper
bound *by* `td`, not on it.

**(ii) The campaign's sharpest local tools are anti-monotone in `td`.**
Slack `= r - k - 1` grows linearly, and the count of surviving one-step
trunk terminals `#{k | 3r-1 : k <= r-1}` grows on average. At `r = 3` there
are two, both tight (slack `1` and `0`); at `r = 7` there are four, the
loosest with slack `5`. The `td=12` "budget saturation" that licences the
reviewed exact-charge theorem is therefore a **strictly `r=3` phenomenon of
the tightest member**, and no amount of sharpening it can reach larger `td`.

For completeness, the *argument* of the reviewed sibling exact-charge
theorem does generalise, but never to a kill: at `k = 2` a flag with
`q_H >= 2` costs `>= 2(3r-1)/2 = 3r-1`, and adding the partner direction's
mandatory `(3r-1)/2` gives `>= 3(3r-1)/2 > 4r - 4 = budget` for every
`r >= 3` (`9r - 3 > 8r - 8`). So one unramified flag per direction and
exact charge `3r-1` are forced at every odd `r`, and `3r - 1 <= 4r - 4`
iff `r >= 3`, with equality only at `r = 3`. *This generalisation is a
replay of the reviewed `r=3` argument and has received no review; it is
recorded as an observation, not promoted, and no new price basis is
declared.*

**(iii) The occurrence gap is not an occurrence gap only.** Even granting
an occurrence of the `U1` state, `Sigma_cfg` cannot pin its arity, hence
cannot pin `td`. So `TD12-U1-ACTUAL-LANDING` as stated — "assume an actual
td12 U1 equality record; then every continuation meets a reviewed
contradiction or a named B25/S17 occurrence" — is a *conditional* whose
antecedent contains the entire missing content. Proving it would still leave
`Sigma_cfg |- td=12` false. That is not an argument against attempting it,
but it does mean the lemma cannot be the last step of an end-to-end proof.

### 4.4 Is `Sigma_cfg` missing something that would change this?

I checked the obvious candidates for an arity- or `td`-monotone premise and
found none in the promoted set:

- `s <= td/beta` — upper bound on `s` **by** `td`; no reverse arrow.
- `Lambda >= beta` — a floor.
- `MP1` `sum(R-1) = s-1` — combinatorial identity, arity-free.
- `Cor 7.1*` `sum lambda <= td - 1 - psi` — the only global inequality with
  a `td` on the *large* side, and its constant is `1`, independent of `s`.
  This is precisely the slot Section 5 attacks.
- `ASM'`/`NM'` — floors, saturated by `U1*(r)`.
- `KJN`/`RPMC` — would give a type-relative ceiling, but `RPMC(C)` is an
  open, single-model, not-yet-reviewed local conjecture (Section 6.3).

---

## 5. Deliverable 4 — one smallest new lemma

### 5.1 Statement

> **Lemma PCB (pole-count budget).**
>
> **Hypotheses.** Let `(f,g)` be a complex polynomial pair with
> `J(f,g) in C^*` that is not a polynomial automorphism, Sigray-normalized
> of type `(alpha,beta)`, `d = td(f,g)`. Let `a in C` satisfy the promoted
> every-fibre Proposition 5.8 rider, so that `g` has meromorphic degree `d`
> on the normalization of `f = a`. Let `T_{a,pole}` be the pole vertex set,
> `s = |T_{a,pole}|`, and let `T_{a,cv}` and `wt(F) = kappa_F(pi(F)-1)` be
> the actual critical-value flag set and weight of the repaired Corollary
> 7.1* (`c253bd12...`, Terra gate `727f5850...`).
>
> **Conclusion.**
> ```text
> d  >=  s  +  sum_{F in T_{a,cv}} wt(F),
> ```
> and hence, for every subset of pairwise-distinct first-separation exit
> flags with the Statement 9.4 terminal parameter `psi`,
> ```text
> sum lambda^exit  <=  d - s - psi.
> ```

At `s = 1` this is exactly the reviewed Corollary 7.1*, so `PCB` is a
conservative extension: it changes nothing that is currently proved.

### 5.2 Why this is the right lemma

It is the *minimal* edit — one constant, `1 -> s` — that makes the only
global inequality in `Sigma_cfg` **`s`-monotone**, and `s`-monotonicity is
exactly what Theorem NG proves is missing.

Applied to `U1*(r)`: the total floor is `lambda = 3r - 1` while the `PCB`
ceiling is `4r - r - psi = 3r - k - 1`, and `k >= 1` at every dirty terminal
by `R1.3`. So `PCB` kills **every one-step trunk terminal of `U1*(r)`, at
every odd `r` and every admissible `k`** — including the campaign's reviewed
`td=12` charged cell (`8 > 7`) and its sibling (`8 > 6`). It closes the
entire one-step escape family with one inequality, whereas the current budget
closes none of it. It does not by itself close hypothetical longer trunks;
those need the same inequality applied along the route, and any additional
priced step only widens the violation.

It is also *cheap to check against everything already reviewed*, because it
weakens nothing at `s = 1`:

| record | `td` | `s` | `sum lambda` | `psi` | current ceiling | `PCB` ceiling | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| `SHEET6-2POLE` two-pole cell | 6 | 2 | 2 | 2 | 3 | 2 | survives, tight |
| every single-pole TDU class | any | 1 | — | — | `d-1-psi` | `d-1-psi` | unchanged |
| `U1*(3)` charged trunk | 12 | 3 | 8 | 2 | 9 | 7 | **killed** |
| `U1*(3)` sibling | 12 | 3 | 8 | 3 | 8 | 6 | **killed** |
| `U1*(r)`, `k <= r-1` | `4r` | `r` | `3r-1` | `k+1` | `4r-k-2` | `3r-k-1` | **killed** |

### 5.3 Proof skeleton

The proof must live in the Section 7 Euler layer, not in Sections 8-9.

1. **Riemann-Hurwitz for `g` on the fibre.** Because `J(f,g) in C^*`, the
   fibre `R_a = {f = a}` is smooth (`grad f` never vanishes), and
   `g|_{R_a}` is **unramified**: a critical point of `g|_{R_a}` would need
   `grad g` parallel to `grad f`, i.e. `J(f,g) = 0`. Let `R~_a` be the
   smooth projective model, `g: R~_a -> P^1` of degree `d`. All ramification
   is at the places at infinity. Over `infinity in P^1` the ramification
   indices are the pole orders `Lambda(F)`, `F in T_{a,pole}`, summing to
   `d`. Hence
   ```text
   2 genus(R~_a) - 2 = -2d + (d - s) + sum_{non-pole places at inf}(e_F - 1),
   ```
   i.e.
   ```text
   sum_{non-pole places at infinity} (e_F - 1) = 2 genus(R~_a) - 2 + d + s.   (*)
   ```
   `(*)` is exact and is where `s` enters with a positive sign. Two
   immediate consequences worth recording separately: since the left side is
   `>= 0` and `genus >= 0`, one gets nothing new; but if *every* place at
   infinity were a pole of `g` the left side would be `0`, forcing
   `d + s <= 2 - 2 genus <= 2`, contradicting `d >= 6`. **So a generic fibre
   of a counterexample always has a non-pole place at infinity.**

2. **Transfer to the weight functional.** The repaired Corollary 7.1* is
   proved by compactly-supported Euler integration of the actual cluster
   weight `w_i(z) = sum_{P in C(i,z)} Lambda(P)` on the abstract quotient
   line `U_i = A^1_eta/Gamma_i`, with proper local-degree conservation at
   coefficient collisions. The `1` in `d >= 1 + sum wt` is the Euler
   characteristic of that one target line. The lemma asserts that the `s`
   pole clusters contribute `s` mutually independent units rather than one:
   concretely, that the pole clusters are disjoint from every finite-value
   direction cluster (this is Proposition 5.1's promoted sidedness repair —
   every finite threshold lies in `T_a^-`, every pole threshold in
   `T_a^+`, with a unique `T_a^0` flag typed by the leading-Jacobian
   predicate) and that each contributes its own compactly-supported unit.

3. **The open step, stated as such.** Step 2 is the whole content. It
   requires identifying the `s` positive-side clusters as `s` separate
   compactly-supported components in the same Euler integration, which the
   promoted Section 7 package does not currently do. FALLACY-v2 explicitly
   forbids identifying a cv flag, a physical place, and a cover series, so
   `(*)`'s left-hand side may **not** be equated with
   `sum_{T_{a,cv}} wt(F)` without a proof. `PCB` is therefore proposed as a
   lemma with a located proof obligation, not as a proved statement.

### 5.4 Dependencies

Proposition 5.1's forced-puncture/non-leakage repair (`a0470416...`,
`dc549047...`, `11059166...`) for the `T_a^+`/`T_a^-` sidedness; the
repaired Corollary 7.1* package (`c253bd12...`, Terra gate `727f5850...`);
`SOL-PROP58` every-fibre repair consuming Chau99 Theorem 4.4; `MP4`/`R2-R4`
for `Lambda`; standard Riemann-Hurwitz. It does **not** depend on Sections
8-9, on any route grammar, on `M`-divisibility, or on `H5a`.

### 5.5 Cheapest falsification test

The honest answer first: **`PCB` is not empirically testable inside the
Keller class.** `s >= 2` already forces `d = sum Lambda >= 2 beta >= 6`, so
any object separating `PCB` from Corollary 7.1* would itself be a
counterexample. On automorphisms (`d = 1, s = 1`) both statements are the
same and both are tight — I checked `(x,y)` and `(x, y+x^2)`: one place at
infinity, `Lambda = 1`, `sum wt = 0`, `d - s = 0`. So the test must be
internal, and it is cheap:

1. **Desk audit of the Euler integration (half a day, no compute).** In the
   proof of Corollary 7.1* replace the single `chi(A^1) = 1` term by the
   pole-cluster decomposition and check whether the `s` positive-side
   clusters are pairwise disjoint *as subsets of the quotient line* and each
   compactly supported. If two pole clusters can share a point of `U_i` at a
   coefficient collision, `PCB` is dead on the spot and the correct
   statement is at most `d >= 1 + (#distinct pole cluster values) + sum wt`.
2. **Sidedness stress test.** Exhibit, or refute, a configuration in which
   a pole threshold and a finite threshold occupy the same cluster. Prop
   5.1's repair says this cannot happen; if it can, `PCB` is dead.
3. **Consistency sweep (minutes).** Re-evaluate every reviewed record with
   both `s` and `sum lambda` recorded — the `SHEET6-2POLE` `td=6` cell, the
   `td=7` SS11a census cells, the `BOOK-ENUM` on-axis panels at
   `6 <= d <= 14`, and the `LL-1` reduced-superset rows — against
   `sum lambda <= d - s - psi`. A single *proved* (not merely formal) record
   violating it refutes `PCB`. My spot checks at `td=6, s=2` and the
   single-pole classes pass; a full sweep is mechanical.

### 5.6 Why this is not a duplicate

- **Not a landing theorem.** `PCB` asserts no configuration-to-record map,
  no marked event, no termination, no coverage certificate. It is a single
  numerical inequality on one fibre.
- **Not `G2-PSC`.** It says nothing about transporting a GGV packet/corner
  into a decorated Sigray tree; it never mentions the GGV frame.
- **Not `G2-BD`.** It is not a delay/carrier bound after residue-A, and it
  applies before any route grammar is chosen.
- **Not a source-constructor result.** It produces no completion, no
  Puiseux prefix, no coefficient map, no `PairRef`. It consumes only
  invariants that the promoted Section 5/7 package already defines.
- **Not the promoted actual-cluster-weight theorem.** That theorem proves
  exactly `d >= 1 + sum wt`; `PCB` is a strictly stronger inequality with a
  different constant, and reduces to the promoted one at `s = 1`.
- **Not `MFE`/the attachment theorem.** Those prove that the selected exit
  flags are pairwise distinct and counted once; `PCB` changes the ceiling
  they are compared against, not the partition.

---

## 6. Deliverable 5 — cross-connection audit

Nothing in this section is promoted. Each item is marked with the arrow it
would need.

### 6.1 Minimal topological degree

`Zoladek 2008` Theorem 6.12 gives `td >= 6` — **P**, refereed. There is no
companion upper bound. Sigray Theorem 9.1 claims the same conclusion with an
incomplete printed elimination and is not used. Note that `td >= 6` is
exactly what makes `PCB` untestable (Section 5.5) and what kills the
"all places at infinity are poles" configuration in step 1 of Section 5.3.
**Arrow to `td = 12`: ABSENT.**

### 6.2 Degree divisibility and the Bezout ceiling

For the normalized minimal pair, `deg(f,g) = (alpha(a+b), beta(a+b))`
(`TRANSPORT` Thm 2.1), so `gcd(deg f, deg g) = a+b = B_GGV`. Bezout in `P^2`
gives `td <= deg f * deg g = alpha beta (a+b)^2`, i.e.

```text
td <= alpha beta B_GGV^2.
```

So a `td` ceiling **does** exist — it is `CRITICAL 7`'s "no theorem bounds
`td` above" that is slightly overstated — but it is ineffective, because no
theorem bounds `B_GGV`. Two conditional readings:

- On the `(72,108)` branch of GGV22's dichotomy, `a+b = 36`, type `(2,3)`,
  so `td <= 7776` and `U1*(r)` is confined to `r <= 1944`. Finite, useless.
- On the `max(deg) >= 125` branch, nothing follows.

Turned around, `U1*(r)` at `td = 4r` forces `4r <= 6(a+b)^2`, i.e.
`a+b >= sqrt(2r/3)`: the escape family forces the polynomial degree to grow
at least like `sqrt(td)`. An independent *upper* bound on `B_GGV` would
therefore cap `r`. **Arrow: CONDITIONAL on an absent degree bound.**

At the entry layer, the achievable `Lambda` set at type `(2,3)` is
`{3a} u {4a} u {6ab} u {9a} u {10a} u ...`, and `3Z u 4Z` alone already
covers every integer `>= 3` except `5`. So divisibility at the entry layer
excludes no `td >= 6`. **Arrow: FALSE as a `td` selector.**

### 6.3 Finite / cofinal type control

At fixed `td`, `beta <= td/s <= td` and `alpha < beta`, so the type menu is
finite — **P**, elementary from `T7`. Cofinal control (a type menu uniform in
`td`) is **ABSENT**, and `REDUCTION` records it as a downstream obligation
alongside `RPMC(C)`.

The one real cross-connection here is worth stating precisely, and then not
promoting. `AUDIT.md` records the proved-in-lane reduction
`RPMC(C) => KJN(C)`, giving `td <= C alpha beta` at each provenanced fixed
type. At type `(2,3)`, `td <= 6C`. In `U1*(r)`, `td = 4r`, so
`r <= 3C/2`. In particular:

```text
KJN(2) at type (2,3)  =>  td <= 12  =>  r <= 3  =>  r = 3  =>  td = 12.
```

That is a sharp localisation of the missing arrow: **within the `U1` star
family, "the premises force `td=12`" is equivalent to a type-relative degree
ceiling with constant `2`.** But `RPMC(C)` is an open local conjecture, is
single-model (`xmodel/sol-kjn.md`), is explicitly "NOT YET Grok-reviewed",
and `KJN(1)` would already contradict the campaign's own live `td=12`
type-`(2,3)` panels. **Arrow: ABSENT; recorded as the cheapest known
sufficient condition, promoted for nothing.**

### 6.4 GGV minimality

`T2` is existential over all counterexamples and supplies no `td`, type,
fibre, branch, or Sigray occurrence — **P but existential**, exactly as
`CRITICAL 2` says. `TRANSPORT` closes the `T2 -> T4` fork at the
normalization layer with `td` preserved, and (4.1)-(4.5) keep the GGV ledger
recoverable, but Section 4's own closing paragraph is explicit that this is
"not a corner-to-tree functor". The `td` of the selected minimal pair bears
no proved relation to that of the counterexample one started with.
**Arrow to `td=12`: ABSENT.**

### 6.5 Boundary-tree Euler accounting

This is the only layer with an `s`-monotone identity, `(*)` of Section 5.3.
It yields, unconditionally from `J in C^*` plus the mass identity:

```text
sum_{non-pole places at infinity of R_a} (e_F - 1) = 2 genus(R~_a) - 2 + d + s,
```

hence `>= d + s - 2 >= 4 + s`, and hence the corollary that a generic fibre
of a counterexample has a non-pole place at infinity. I have **not** bridged
this to `sum_{T_{a,cv}} wt(F)`, and FALLACY-v2's flag/place/series rule
forbids doing so by identification. That bridge is precisely Section 5.3
step 2, i.e. `PCB`. **Arrow: the identity is proved; its consumer is the
proposed lemma, not a promotion.**

### 6.6 Monodromy

The reviewed `U1` record leaves an explicit coefficient/monodromy rider:
gluing `{c_e^n}` to the three cube roots of one `A_star` in
`Rad_G = t_G^3 - A_star`, for infinitely many admissible `n`. In `U1*(r)`
the corresponding object is `t_G^r - A_star` with `r` roots, and the reviewed
`ORB-FUSE` rigidity (`U1` fuses into one `mu_{r nu}`-orbit;
`nu`-primitivity kill REFUTED) applies verbatim with `r` in place of `3`. So
monodromy is another `r`-uniform layer: it cannot select `r = 3` either.
Printed Statement 3.9 does **not** relate `A_star` to the trunk ratio
`B/A = 3r/(3r-1)` (the two `t`-coordinates differ, `eta_G^n` versus
`eta_F^{nu_F}`, and the degrees are not count-exact), so no numerical tie is
available. **Arrow: ABSENT.**

---

## 7. Replay, scratch, and negative controls

Two short exact-arithmetic scripts under `/tmp/occ` (integer and
`fractions.Fraction` only; no CAS, no allocation beyond a few MB, both
finish in seconds).

**Script A — entry layer.** Enumerates all `T7`-admissible entry data at
given `(td, s)` from the pole conditions `Lambda = a b alpha beta/nu`,
`(nu|alpha & nu|b beta - 1) or (nu|beta & nu|b alpha - 1)`, `Lambda >= beta`,
`2 <= alpha < beta`, `gcd = 1`. Results used in Section 2.3. Negative
control: at `td = 12, s = 4` it returns the empty **off-axis** menu, which
is forced: `s <= td/beta` requires `beta = 3`, and `4 x 3 = 12` then makes
every `Lambda = 3`, i.e. every pole `(1,1,2)` with `b = 1`.

**Script B — `U1*(r)` closed forms.** For all odd `r` in `[3,59]` it
independently recomputes the merge data, the dirty `P0` menu, `N1`, `R1.0`,
`(S)`, `(NE)`, `(R)`, the divisor law, `M_F`, `w_F`, `j`, `psi`, the
per-orbit and total AF2 floors, the Statement 9.4 ceiling, and the
Proposition 8.1(iv) coefficient identity, and asserts every closed form in
Section 4.2. Output: `ALL CLOSED FORMS VERIFIED`, zero failures.

Negative controls actually exercised, all behaving as required:

- `r` even (`r = 2, 4`) is rejected at `MP2` because `M = gcd(2, rn+1) = 1`;
  this independently reproduces the campaign's `m = 2` no-jump-dead
  conclusion and the surviving `td = 8` exclusions.
- `k = 16` at `r = 3` and `k = 4, 28` at `r = 5` are rejected by
  `gcd(M_F, nu_F) = 2 != 1` (`R1.0`), which is why the admissible `k` are
  the divisors of `3r-1` and not of `2(3r-1)`.
- `B/A = 7/8` at `r = 3`, `A = B`, `A = 0`, and dropping the `Pfull_t` term
  all break the Proposition 8.1(iv) identity, matching the reviewed
  producer's own mutation list.

No file outside this path and `/tmp/occ` was written. No canonical file was
modified. `jc2-lean` was never read, listed, stat'ed, grepped, built,
modified, or touched.

---

## 8. Scope firewall and non-claims

This report does **not** assert, and nothing in it may be read as asserting:

- any occurrence, attainment, `PairRef`, source value, serialized packet,
  coefficient, or realized configuration;
- that `U1*(r)` is realized by a polynomial Keller pair for any `r`,
  including `r = 3`; it is an abstract admissible configuration only;
- any exit price, exit-set charge, or upgrade of a `REPRESENTATIVE` floor to
  `FULL_ACTUAL_EXIT`/`FULL_ACTUAL_FIRST_SEPARATION` attainment;
- `PCB`, which is proposed with a located open step and is **not** proved;
- the `r`-general sibling exact-charge replay of Section 4.3(ii), which is
  an unreviewed observation;
- any degree ceiling, type ceiling, `KJN`, `RPMC`, `G2-PSC`, `G2-BD`,
  landing, coverage certificate, panel closure, route kill, or JC2
  conclusion;
- any change to the status of `Avenue 2`, `Avenue 36`, the `B` or `S`
  bridges, or the `td=12` panel, which remains `OPEN`.

What it does assert: Theorem OC (Section 3.1, clause 5 being the new
`R`-uniform reading of the reviewed `ASM'`/`NM'` floor), Theorem NG
(Section 4.1) relative to the enumerated axiom list `Sigma_cfg`, the
`U1*(r)` closed forms (Section 4.2, exactly verified), the six coverage-test
verdicts of Section 3.2, the Riemann-Hurwitz identity `(*)` and its
non-pole-place corollary (Section 5.3 step 1), and the arrow marks of
Sections 2 and 6.

The correct campaign-level summary of this attack is a negative one:
**the missing occurrence/coverage arrow cannot be supplied from inside the
recorded configuration interface, because that interface is invariant under
pole inflation.** The cheapest identified repair is `PCB`; the cheapest
identified sufficient condition is a type-relative degree ceiling with
constant `2`; neither is proved.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `51552`.
- Body SHA-256:
  `19d15346303d23f10fdf3bae0fc153396434e4e8835585d063e98e3d6c95947d`.
- Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`.
- `charge_basis`: `ABSENT` (no exit price asserted).
