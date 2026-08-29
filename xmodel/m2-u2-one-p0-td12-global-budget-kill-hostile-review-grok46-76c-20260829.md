# Hostile review — labelled one-P0 U2 td12 global-budget kill R1

Date: 2026-08-29 UTC
Reviewer: Grok 4.6, independent adversarial referee, different model from
the Sol 5.6 producer.
Target:
`xmodel/m2-u2-one-p0-td12-global-budget-kill-r1-sol56-20260829.md`
Frozen pushed basis (verified `git rev-parse HEAD` at session start and
again before this verdict):
`76c746f698103d20019bfeb72654a361ccc5371d`

No `jc2-lean` access of any kind. No web, AWS, heavy local computation,
canonical edit, producer/checker edit, commit, or push. Bounded exact
`int`/`Fraction` Python only. Ordinary and optimized checker runs are
recorded below.

## 0. Verdict

**`PASS_WITH_REPAIR`**

The labelled-route kill is correct at the stated actual-landing scope.
Equality in the repaired source-mass floor forces type `(2,3)` and three
disjoint one-leaf `(a,b,nu)=(1,2,3)` chains with seed `(w,M)=(3/2,2)`.
Corrected `inner_u2.dq=3` makes the R2.1 handshake force both inner
arrivals to `w_H=1`, and Statement 8.4 requires `3 | M_H` at those
incoming vertices, not at the target merge. The cap-free budget-five
reduced P0 closure is a licensed consumer on each such chain: its unique
`(w,M,lambda_min)=(1,3,5)` state is a lower bound, not an attainment
claim. Zero-price P0 moves cannot raise the sibling from `w=3/2` to the
labelled outer weight `w=2`. The three pre-merge vertex sets are pairwise
distinct in the actual tree `U`. Representative AF2 prices on those
vertices attach to Statement 9.4/(26) by BOOK-OFFAXIS P1 and the promoted
MP8 selected-exit inequality; the unresolved LL-1 full-exit carrier
bridge is not used. Then `5+5+1=11 > td-2=10`.

One interface repair is required before promotion. The pinned BOOK-OFFAXIS
full-exit correction obliges every P0 consumer to declare
`REPRESENTATIVE` or `FULL_ACTUAL_EXIT`. This packet uses the displayed
AF2 summands and must be declared `REPRESENTATIVE`. That declaration does
not change `11>10`.

No charge_basis line is declared. The inner fives are reduced-state lower
bounds, and the sibling unit is a floor that some first-separation exit
set is nonempty. Neither identifies a cv flag with a physical place and a
cover series.

## 1. Custody, replay, independence

PRE hashes (before reading the producer body) and POST hashes (immediately
before this verdict) agree with the charged pins. No `INPUT_MUTATED`.

| item | pinned SHA-256 | PRE/POST |
|---|---|---|
| target, full | `6eb9b8882766a33a23cbd37564eed252b71c39c158cb1f572ffe0a6f721a9654` | match |
| target, body (7422 bytes) | `f37ce04ef928bcb99ff8528880b1ac3e5891f598d37397da554f811dfa31cbc6` | match |
| `check.py` | `f12565cef14e99e2b2f9c4114e98956711e3b8b0b352a3720469a41b4eaafbf8` | match |
| replay `README.md` | `7d98035fb03dc17e9c2e80ed609653ff2b66a6154fee6ef9617389a04d188d21` | match |
| `ladder/BOOK-OFFAXIS.md` | `1ae50f7925de2d63a718b48ab892c78a3313e4a505b8faf7385853d591c58840` | match |
| `ladder/SHEET6-AF2.md` | `570f4f18d46178d8b86fe2276dbb2e35cb91e845842530b8c56df80bc16461f0` | match |
| `ladder/SHEET6-H3.md` | `6bff49a12b9a2b8a97f137905ec87a7cbfb0025da39e59f54970458323b7344c` | match |
| finite-chain R2 repair | `3a7c604b1972681ef90982a94a10c61076d1f16502603ac39cefc802d7439398` | match |
| finite-chain R2 Opus review | `11d45ecaab58e82d3a5ef44bb14b5a90b617a8be8d287a1e947447fff43d1069` | match |
| `finite_chain_skeleton_r2.py` | `b6f363407af9ea16f83bb5c0b7ff5c659e0e69b372ef2ace47d1f53b8b768afb` | match |
| R2 tests | `99670c469b66e7639f3046169ca3a7f8bbcda24890b19fe2018674adc23f7e19` | match |
| family-record correction | `4dde1c471b04d88db466293bc197c78529bc16743cc7ccde176e594bceb622dc` | match |
| family-record Opus review | `84c648a721f42d8197a9c78648795e9830e5bb75521a3e00a8a9d5a80f495cb6` | match |
| Fable source-mass review | `f9dd2035bbe5a47561cce263ba1288a9245526dec748c3ef031545e443bf510f` | match |

Body convention of the target: all bytes through and including the unique
line `*End of sealed report body.*` and its trailing newline (7422 bytes);
the excluded remainder is exactly `\n---\n` plus the seal. Adequately
defined.

Checker, both modes, byte-identical stdout:

```text
PYTHONDONTWRITEBYTECODE=1 python3 check.py
PYTHONDONTWRITEBYTECODE=1 python3 -O check.py
stdout sha256 = 1c857adfc4a2614c948ea76a2a4000c076561999db0417b65ea0d34d01c87a1e
```

`require` is a real function, so `-O` is a meaningful replay. The
arithmetic below was rebuilt from the pinned laws and from a direct
call of `close_reduced_skeleton`; the checker JSON was not used as an
oracle.

## 2. Attack 1 — source-mass equality

Fable's source-mass review is `FAIL` at `td>=15` and is not a proof
oracle. Its salvage ASM′ is the lemma actually used. Independently:

For the labelled route every relevant arrival multiplicity is 3
(two inner children, sibling `h=3` forced by the outer quadratic
radical and `dp_2=6`). ASM′ therefore gives each of the three arrival
subtrees mass at least `max(beta,2*alpha)`. Over coprime
`2<=alpha<beta` the route floor `3*max(beta,2*alpha)` equals 12 only at
type `(2,3)`, where `max(3,4)=4`. Exhaustive scan of that coprime range
through `(19,29)` finds no other type with floor `<=12`.

At type `(2,3)`, TDUNIFORM R2/R3 rows with `Lambda=4` were enumerated
over `a,b<=19` and `nu<=20`. The unique survivor is case (B)
`(a,b,nu)=(1,2,3)`:

```text
Lambda = a*b*alpha*beta/nu = 1*2*2*3/3 = 4,
kbar = a(alpha+beta) = 5,  rho = a/b = 1/2,
w = (kbar-rho)/nu = (5-1/2)/3 = 3/2,  M = b = 2.
```

Two poles already cost at least `2*beta=6>4`, so each equality subtree
has exactly one pole leaf. In the rooted tree `U` (MP0/D1/D2) that
forces a merge-free path from the pole to the specified first merge,
and the three pre-merge vertex sets are pairwise disjoint. Extra poles
on the trunk would raise total mass above 12, so at `td=12` they are
absent. The withdrawn M-descent law is not used.

Attack 1: CONFIRMED, at actual-landing scope.

## 3. Attack 2 — corrected handshake and Statement 8.4

Target inner U2, after the pinned correction `dq=3`:

```text
nu_G = 1,  (dp,dq,kbar,mu) = (6,3,3,3).
X_G = kbar*dp/dq = 18/3 = 6.
R2.1, case I/II: X_G = mu_e*(kbar_G - w_H) => w_H = 3 - 6/3 = 1.
```

Both inner children have `mu=3` and are non-zero (quadratic radical,
`dp=3+3`). Equal-`mu` non-zero arrivals share `w` (R2.1(i)), so both
incoming weights are `w_H=1`. Inner `nu_G=1` places the merge in
`V_2\V_1`, hence case I rather than case II; R2.1 covers both. Case III
is a 0-edge at an interior `V_1` merge and does not apply.

Statement 8.4 is `mu_e | M_H` at the upper vertex `H`, not at `G`.
The filter is therefore `w_H=1` and `3 | M_H`. The merge's own state
`(w_G,M_G)=(2,3)` is a different vertex and a different index.
Incoming `nu_H` is eliminated by the handshake and is not a legacy
search index; the reduced closure quantifies over all legal `nu>=2`.
The displayed witness later realises `nu_H+1 ≡ 0 (mod 3)`, i.e.
`nu_H ≡ 2 (mod 3)`, which is an incoming residue, not `nu_G`.

The illegal `dq=4` would have given `X=9/2` and `w_H=3/2`, collapsing
the inner arrival to the pole seed and destroying the kill. The
correction is load-bearing and is the value used here.

Attack 2: CONFIRMED. Required writeup sharpening is N1 below.

## 4. Attack 3 — closure consumer, floor versus witness

The finite reduced P0 theorem (Fable `PASS_WITH_NARROWING`, Grok
`PASS_AT_STATED_CHAIN_SCOPE`, Opus `PASS_IMPLEMENTATION_R2`) computes
all reduced chain states from a fixed `(w,M)` at a fixed numerical
budget, cap-free. Each equality subtree is a one-leaf merge-free P0
chain, so the theorem is a licensed consumer of last-vertex *reduced*
data. Last-vertex full cells and merge families remain outside; they
are not needed.

Direct call of the pinned R2 closer at `(3/2,2,B=5)`:

```text
cap_free true, 69 states, 295 edges, max numerator 3, max M=25,
state-table sha256 c2835aaf8450ab938170ae3808b5852d53f2c7b1ae29b14ca77b7965bf37f1ad,
zero_cost_reduced_nonincrease true.
```

All `w=1` states:

```text
(1,1, lambda_min=4),  (1,2, lambda_min=4),  (1,3, lambda_min=5).
```

The `3|M_H` cut leaves exactly `(1,3,5)`. The two cost-four states fail
Statement 8.4 for `mu=3` and are illegal arrivals. That cut is
load-bearing: without it the inner pair would be `4+4`, and
`4+4+1=9<=10` would not kill.

Any path of modelled price at most four occurs in a cap-free budget-five
closure. None reaches `(w,3|M)=(1,3|M)`. Hence every legal inner chain
costs at least five, including putative routes that cost more than five.
Modeled AF2 is a lower bound of true lambda (Fable R1: modeled lambda
never overprices), so absence in the modeled superset is absence in the
true set.

The displayed two-step witness is attainment only and was rebuilt from
P0, not from the checker:

```text
(3/2,2) --dirty l=2, (dp,dq,nu)=(20,16,5), k=2, Sm=2, eps=0, lex=0,
         E=12, kbar=4, X=5, M=4, w=3/4, AF2: two simple extras,
         gap = 5-4 = 1 each, lambda >= 2-->
(3/4,4) --pure-epsilon (l,eps,E)=(4,1,3),
         w' = (4/3)*(3/4) = 1, cost = ceil(4*(3/4)/1) = 3,
         M' = gcd(3, nu+1) = 3 on residue nu+1 ≡ 0 (mod 3)-->
(1,3).
```

Path sum 5. Defects are integral, so a full-exit reading of these two
steps would not raise the representative prices. That is a check of the
witness, not a promotion of full-exit, and not a replacement for the
lower bound.

Attack 3: CONFIRMED.

## 5. Attack 4 — outer sibling `w=2`, zero-price obstruction

Outer record: `dp_2=6`, `dq_2=K+2`, `kbar_2=2(K+2)/K`, `X_2=12/K`,
`h=3`. For every repaired `K=6q+1`,

```text
w_e = kbar_2 - X_2/h = 2(K+2)/K - 4/K = 2.
```

Independent of `q`. The inter-merge P0 is clean-neutral from inner
`w_G=2`, so it arrives at weight 2; R2.1 then forces the unused sibling
to the same weight. Direct pole arrival is the seed `w=3/2 ≠ 2`.

Zero-price P0 menu, independently of the executable:

- clean-neutral: `w'=w`, `M' | M`;
- clean-resonant: `w' = w*n/Delta` with `n>=2`,
  `Delta=(n-1)nu+1 >= 2n-1 > n`, so `w'<w` strictly;
- every non-clean step has modeled lambda `>=1` (AF2 extras and
  epsilon each cost at least one), hence is not zero-price.

From this seed the budget-zero closer realises only the two neutrals
`(3/2,2)` and `(3/2,1)`. Resonance is empty here because `den(w)=2`
does not divide the unique candidate `dq=5`. The executable therefore
omits a resonance row at this seed, but the omitted family decreases
`w` and cannot produce `w=2`.

Cases the executable does not name:

- at-level parting is not a reduced-`w` transport;
- direct-arrival at the pole is the seed;
- the on-axis boundary `(3/2,1)` still has `w=3/2`;
- a `nu=1` `r=1` chain vertex is not a merge-free segment vertex of
  this pole (DS1: segment vertices lie in `V_{1,a}`, `nu>=2`); dirty
  `V_{2,a}` steps are already in P0 and are not free.

The cheapest modelled `w=2` state inside budget five is `(2,1)` at
lambda 3 (pure-epsilon doubling). That is a positive-price witness,
not a free path, and `M=1` would still fail sibling Statement 8.4
`h=3 | M_H`. The producer does not use that strengthening; the unit
floor from “some non-clean vertex exists” is enough.

Attack 4: CONFIRMED as a lower bound. Exact sibling price is not
proved.

## 6. Attack 5 — distinct vertices, St 9.5 attachment, `11>10`

The two inner pre-merge paths live in the two incoming subtrees of
inner U2. The sibling lives in the other incoming subtree of outer U2.
Inner U2 itself is not on the sibling path. MP0/D2 tree structure makes
the three vertex sets pairwise disjoint. Shared suffixes of `U` lie
strictly below the relevant first merges and are omitted; omitted
nonnegative merge/trunk prices can only strengthen the contradiction.

AF2 prices in the closer are the displayed per-step first-separation
summands. BOOK-OFFAXIS (2026-08-29 full-exit correction) splits P0
consumers into `REPRESENTATIVE` and `FULL_ACTUAL_EXIT`. This packet is
the former: it keeps those summands. Generic MFE-selected full-exit
reprices, and the quarantined LL-1 R3 book, are a different consumer.
They are not used.

Statement 9.4 (25) sums `lambda_F` over any pairwise-different down
vertices. P1 compiles that sum over the whole configuration. MP8, at
promoted MFE inequality scope, gives the same inequality on the
pole-path union with a shared suffix counted once. First-separation
assigns each climbing flag to a unique vertex, so distinct vertices
have disjoint exit sets. The x-side `psi` cluster is the other tree
component and is not among the three pre-merge sets. Thm 6.1 supplies
`l_f < k_f`, so `psi=1` is admissible and (26) is `td-2=10`. Terminal
psi-sharpening is not required; a larger `psi` would only tighten the
upper bound.

Strongest legitimate reading still against the kill: representative
(not full-exit) prices, inner floors exactly five, sibling floor
exactly one, merge/trunk zero, `psi=1` rather than larger. That is
already `11>10`. Full-exit, more expensive inner routes, or a sibling
that actually costs three, all strengthen.

The producer did not declare the consumer type. That is the repair.

Attack 5: CONFIRMED, after the `REPRESENTATIVE` declaration.

## 7. Attack 6 — typed countermodels and escapes

Attempted escapes, all either fail or lie outside the stated theorem:

1. Extra merge on an equality subtree. A merge has in-degree `>=2`, so
   at least two pole leaves, mass `>=2*beta=6>4`. Contradicts equality.
   Outside the equality profile, not a refutation.
2. Source sharing of a pole leaf. Leaves of `U` are the poles (MP0);
   a leaf cannot lie in two disjoint subtrees.
3. Branch remerging above outer U2. `U` is a tree.
4. On-axis vertices. Neutral drop to `(3/2,1)` does not raise `w`.
   Once `M=1`, `l | M` forces `l=1`, so no later dirty step and no
   return to `3|M`. The cost-four states `(1,1)` and `(1,2)` fail
   inner Statement 8.4. Not an inner escape. Sibling on-axis expansion
   `(2,1)` costs 3, not 0.
5. A different pole-to-chain map. Unique mass-four row, unique one-leaf
   path per subtree.
6. Uncorrected `inner_u2.dq=4`. Gives `w_H=3/2` and is illegal at
   `nu=1`. Outside the repaired labelled interface, not a countermodel
   of the repaired theorem.
7. Formal arithmetic ledger without actual landing. The theorem is
   conditional on an actual typed source landing. A formal ray is not
   an actual tree; this is the producer’s own firewall, retained.
8. Case III 0-edge at inner U2. Inner `nu_G=1` is not `V_1`.
9. Outer U2 as a genuine root merge. Root case-I handshake needs
   `0<w_e<1`, but the labelled children have `w=2`. Outer U2 is
   interior; a trunk below is a coverage-debt consumer and is omitted
   as a nonnegative price.
10. Charging only one MFE witness per pole instead of the path sum.
    An actual landing supplies actual vertices; St 9.4/MP8 sums every
    selected first-separation set of those vertices. Restricting to one
    witness per pole would be a different, weaker consumer, not a
    refutation of this one.

No typed actual countermodel of the stated theorem was found.

## 8. Required repair, nits, maximum safe theorem, exclusions

**R1 (must fix, interface only).** Declare the P0 consumer type
`REPRESENTATIVE`. Do not cite this packet as a `FULL_ACTUAL_EXIT`
consumer or as an LL-1 full-exit carrier. The numerical kill is
unchanged.

**N1.** Display the inner index split in one line:
target `(nu_G,X_G,kbar_G)=(1,6,3)`, incoming `(w_H,M_H)` with
`3 | M_H`, incoming `nu_H` free and distinct from `nu_G`.

**N2.** Do not read the sibling unit as an exact price. The closure’s
cheapest `w=2` state costs 3 and has `M=1`; sibling Statement 8.4 is
unused slack.

**Maximum safe theorem.** Assume an actual typed source landing at
`td=12` of the corrected labelled route `NESTED-U2-P0-U2-RAY/v1`
(inner `dq=3`, inner arity 2 with both arrival multiplicities 3, clean
neutral P0, outer arity 2 with both arrival multiplicities 3). Then
the configuration is impossible: the three disjoint one-leaf pre-merge
chains contribute representative AF2 at least `5+5+1=11` against the
configuration-wide bound `td-2=10`. The same kill applies to every
fixed-`t` member of the repaired semilinear ray, viewed as an actual
landing of that labelled route.

**Explicit exclusions.** Other U2 routes; other one-P0 labelings;
universal td12 emptiness; a landing-existence theorem; coefficient
gluing; realizability; a degree ceiling; a polynomial pair; a
counterexample; JC2; the formal family record as an actual tree; the
LL-1 inventory; full-exit numerical reprice; any exact (as opposed to
lower-bound) inner or sibling price; withdrawn M-descent.

The producer’s firewall fields `other_u2_routes`, `all_td12`,
`landing`, `realizability`, and `jc2` are load-bearing and are
retained.

## Verdict (repeated)

**`PASS_WITH_REPAIR`**

*End of sealed report body.*

---

Sealed body: 16,783 bytes.  SHA-256:
`8f489f453181f1a323c28baf81b7420e86e48f73961afb49aee707312bbc2388`.

The full-file digest is not inlined, because inlining it would change it.
Recompute both by

```python
from hashlib import sha256
from pathlib import Path
p = Path("xmodel/m2-u2-one-p0-td12-global-budget-kill-hostile-review-grok46-76c-20260829.md")
b = p.read_bytes()
marker = b"*End of sealed report body.*\n"
i = b.find(marker)
print(len(b[:i+len(marker)]), sha256(b[:i+len(marker)]).hexdigest(), "body")
print(sha256(b).hexdigest(), "full")
```
