# Hostile review: generic PCB as quotient-collision surplus

Reviewer: Claude Opus 5, independent adversarial lane  
Date: 2026-08-29 UTC  
Frozen basis: `31777ce90994a106aade85064c0d868e32863f94` (`git log` confirmed)  
Target: `xmodel/pcb-generic-collision-surplus-sol56-20260829.md`  
Lifecycle: `IDENTITIES CONFIRMED / DEPENDENCY-BARRIER CLAIM GAP / SUCCESSOR PACKET GAP`

No web. No Singular, no CAS, no AWS, no heavy computation: every number below
comes from desk-scale `int`/`gcd`/permutation arithmetic in `/tmp`. `jc2-lean`
was never entered, listed, searched, read, built, stat'ed, or modified. No
canonical ledger, producer, or other repository file was written. No `git`
command other than the read-only basis check. This review asserts no exit
price, so no `charge_basis` line is declared.

## 0. Verdict summary

| # | Item | Verdict |
|---|---|---|
| 1 | fixed-fibre Euler--Fubini identity `d-chi_a = sum_i sum_(P_i(z)=a) w_i(z)` and its hypotheses | **CONFIRMED** |
| 2 | `d-chi_gen = sum_i d_i b_i`, `n = sum_i d_i`, `E_gen = sum_i b_i(d_i-1)+chi_gen-1` | **CONFIRMED** |
| 3 | collision formula `(FC)`, its sign, distinct-root convention, `epsilon(a)>=0` | **CONFIRMED** |
| 4 | `sum_a(d_i-q_i(a))=d_i-1`, `sum_a epsilon(a)=sum_i(I_i-b_i)`, Suzuki compatibility | **CONFIRMED** |
| 5 | generic PCB `<=>` `sum_i b_i(d_i-1)>=2G+2s+n-2`, conventions, margin `Xi` | **CONFIRMED** |
| 6 | Section 4.1 boundary germ: two-form, degrees, baseline five, non-polynomial scope | **CONFIRMED** (and strengthened) |
| 7 | Section 4.2 permutations, product, transitivity, RH genus, punctures, collision topology | **CONFIRMED** (recomputed) |
| 8 | matched controls establish the stated dependency barrier | **GAP** |
| 9 | `QCS-MARGIN/v1` is the cheapest honest next discriminator | **GAP** |

Short form. **Every exact identity in the producer is correct and I
reconstructed all of them independently.** The producer's genuine
contribution is that it converts the open half of the atypical route into a
single named integer, and it does so without an illicit flag/place/series
identification. **The two claims that fail are the meta-claims**: the matched
germ + passport is not a model of the inputs it is said to be independent of,
so the non-derivability sentences are not proved; and the proposed successor
packet omits the one field that would make it computable and is knowably
`UNDERDETERMINED` on the only client it names.

## 1. Custody

Recomputed on disk (`shasum -a 256`), all match:

```text
41209192...e0813f  xmodel/pcb-generic-collision-surplus-sol56-20260829.md   (full)
a2cf302a...a147f   producer body, 15043 bytes through its terminal body marker
c253bd12  sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md
727f5850  sigray-section7-weighted-euler-inequality-hostile-review-terra-20260828.md
b96a6564  dual-pencil-definition-gate-20260824.md
57e6d4a1  dual-pencil-review-grok-20260824.md
aec8bd7e  sigray-section7-resolution-free-coordinator-repair-sol-ultra-20260828.md
758c0226  sigray-section7-resolution-free-coordinator-final-delta-gate-terra-20260828.md
90546ffb  d73-strict-or-equality-20260824.md
3c0df200  d73-strict-or-equality-review-grok-20260824.md
47eef092  sigray-prop58-every-fiber-independent-audit-sol-ultra-20260828.md
```

Every abbreviated hash the producer cites resolves to a real file at this
basis. The producer's byte count and body seal are exact.

Two inputs the producer **uses but never cites** are recorded here because the
review depends on them: the definition of `PCB` and of `PCB-EXCESS`, which
live only in `xmodel/u1-star-pcb-independent-audit-sol56-93d-20260829.md` §5
(`d >= s + sum_(F in T_cv(a)) wt(F)`, `wt(F)=kappa_F(pi(F)-1)`), whose Claim B
was reviewed `FALSE/UNSUPPORTED` by Grok 4.6; and the reviewed
`counterexample => td>=6` result (`PROGRESS.md`, internal-repair tier, `td=6`
explicitly not excluded). See repairs R1 and R6.

## 2. Item 1 --- fixed-fibre Euler--Fubini identity: `CONFIRMED`

I rederived `(2.1)` without using the producer's text.

Fix `a`. `Phi=(f,g)` is etale, so every `f`-fibre is smooth and every affine
preimage is simple; `b |-> N(a,b)` is constructible with finite values, and
compact-support Fubini for `g : f^-1(a) -> A1` gives

```text
integral_(b in A1) N(a,b) dchi_c = chi_c(f^-1(a)) = chi_a,
integral_(b in A1) d dchi_c       = d*chi_c(A1) = d.
```

Restricting the promoted pushforward identity `d-N = sum_i (phi_i)_! w_i` to
the line `{a} x A1` and integrating, each `(phi_i)_! w_i` contributes
`sum_(z: P_i(z)=a) w_i(z)`, because compact-support integration over a finite
set is plain summation and the grouping by `Q_i`-value is undone. Hence

```text
d - chi_a = sum_i sum_(z: P_i(z)=a) w_i(z),
```

with `z` ranging over **distinct** geometric roots. The producer's remark that
`Q_i`-collisions are harmless is correct and is exactly the reason no
ramification multiplicity may be inserted --- the same point on which Terra
killed the original Lemma 3.2.

Hypotheses actually required, each checked against a named input:

| hypothesis | source | status |
|---|---|---|
| `deg(g on normalization of f^-1(a)) = d` on **every** fibre, incl. reducible | `47eef092` §3 and `(R5)`: `sum Lambda = d - Delta_a`, `Delta_a=0` for a Keller pair; `g` nonconstant on every component since `df^dg != 0` | licensed |
| affine preimages simple; all `f`-fibres smooth | `J=1` etale | licensed |
| clusters `C(i,z)` **partition** the finite-value punctures of every fibre | `758c0226`-passed no-duplication/EW1 clauses; `c253bd12` §5 | licensed |
| `P_i` nonconstant, so `phi_i` has finite fibres | `aec8bd7e`/`758c0226` passed clause | licensed |
| `w_i` integer-valued and constructible | `727f5850` §6 | licensed |
| index set `{i}` finite | **not stated by the producer**; derivable, since `sum_i I_i = d-1 < inf` with `I_i >= b_i > 0` | repair R2 |

The identity holds for *every* `a`, not only generic `a`. That is the whole
point of the every-fibre Proposition 5.8 replacement, and the producer is
entitled to it.

## 3. Item 2 --- generic identities: `CONFIRMED`

Let `S_i = {0} union Crit(P_i)`, finite. For `a` outside the finite set
`union_i P_i(S_i)`: `P_i-a` has `d_i` simple roots, none zero, and each lies
off `S_i`, so `w_i = b_i` there. Hence `d-chi_a = sum_i d_i b_i` on a cofinite
set of `a`, so that constant **is** `d-chi_gen`, and `(2.2)` holds. A free
corollary the producer does not state: the atypical set of `f` is contained in
`union_i P_i(S_i)`.

`n = sum_i d_i`. This is the one identification in the paper, and it is the
licensed one: for `z != 0` with `P_i'(z) != 0`, `727f5850` §5 gives a
**singleton** cluster of weight `b_i^+` (every covered lift nonzero and simple;
the orbit is counted once, not `m_i` times). Since clusters partition the
finite-value punctures, a generic fibre has exactly `sum_i d_i` of them. This
is a quotient-point/place identification valid **only at generic `a`**; at a
collided value it is false (`q_i(a) < d_i` clusters, possibly several punctures
each), and the producer correctly never uses it there. No flag is identified
with a place or a series anywhere.

`E_gen = sum_i b_i(d_i-1) + chi_gen - 1`. Two independent derivations, both of
which I reproduced:

```text
(A)  sum over a of (2.3), using (3.1),(3.3) and sum_a (chi_a-chi_gen) = 1-chi_gen;
(B)  E_gen = sum_i(I_i-b_i) = (d-1) - sum_i b_i,  and  d = chi_gen + sum_i d_i b_i.
```

Derivation (B) uses **no** Suzuki input. Consequently the Suzuki total-defect
identity is *derivable* inside this framework rather than assumed --- a real
consistency hit, and the strongest evidence in the packet that `(2.1)`-`(3.4)`
are right. `chi_gen = 2-2G-s-n` additionally requires the generic fibre to be
**connected** (`c=1`); with `c` components it reads `2c-2G-s-n` and every
downstream margin shifts by `2(c-1)`. Suzuki primitivity supplies `c=1` for an
actual pair; it is not automatic for a source *packet* (repair R3).

## 4. Item 3 --- collision formula `(FC)`: `CONFIRMED`

From `(2.1)`, `d-chi_a = sum_i q_i(a) b_i + epsilon(a)`; subtracting from
`(2.2)` gives

```text
chi_a - chi_gen = sum_i b_i(d_i-q_i(a)) - epsilon(a).
```

Sign confirmed: a collision **raises** `chi_a`, weight excess lowers it. The
distinct-root convention for `q_i(a)` is the same convention as in `(2.1)` and
`(3.1)`, consistently throughout. `epsilon(a) = sum_i sum_(P_i(z)=a)[w_i(z)-b_i]`
is a finite sum of nonnegative integers by amended Lemma 3.2 (`w_i >= b_i^+`
everywhere, `b_i = b_i^+`), so `epsilon(a) in Z_{>=0}`. Confirmed.

Two consequences the producer has but does not draw, both of which sharpen
its own thesis. Combining `(FC)` with the licensed Ha--Le/Suzuki criterion in
`b96a6564` (`c in B_infinity <=> chi_c(h^-1(c)) - chi(G_h) > 0`, all defects
`>= 0`):

```text
0 <= J(a) <= C(a)  for every a,
so an atypical value forces a COLLISION (q_i(a)<d_i for some i),
never a weight excess.
```

That is a clean, exact statement of why the atypical route points the wrong
way, and it needs no control at all.

## 5. Item 4 --- ramification sum, grouping, Suzuki: `CONFIRMED`

`sum_a [d_i-q_i(a)] = sum_z ord_z(P_i') = deg P_i' = d_i-1` in
characteristic zero for nonconstant `P_i`; the degenerate case `d_i=1` gives
`0` correctly. `(3.2)` and `(3.3)` are the compact-support integral of a
function that is `0` off the finite set `S_i`, plus regrouping by
`a = P_i(z)`; both confirmed.

Suzuki compatibility. `b96a6564` (`CONFIRMED` by `57e6d4a1`) gives
`delta(h) = 1-chi(G_h) = 2g_h + r_h - 1` with `r_h` the total puncture count.
With `r = s+n` this is exactly the producer's `delta(f) = 2G+s+n-1`.
Compatible, and as noted in §3 it is here a *check*, not a premise.

**Notation collision (repair R4).** `b96a6564` writes `epsilon_c(h)` for the
Euler jump `chi_c(h^-1(c))-chi(G_h)`; the producer writes `epsilon(a)` for the
weight **excess**, which is `C(a)-J(a)`. These are different objects and in
the zero-excess control they take the values `5` and `0` at the same value
`a=0`. Any reader crossing the two documents will invert the argument.

## 6. Item 5 --- equivalence with `(QCS)` and the margin: `CONFIRMED`

Recomputed:

```text
E_gen - (s-1) = [sum_i b_i(d_i-1) + 1 - 2G - s - n] - (s-1)
              = sum_i b_i(d_i-1) - (2G + 2s + n - 2)  = Xi.
sum_i b_i(d_i-1) - delta(f) = sum_i b_i(d_i-1) - 2G - s - n + 1 >= s-1  <=>  (QCS).
```

Euler conventions are consistent throughout: `chi_c = chi` for complex
algebraic varieties, `chi_c(A1)=chi_c(A2)=1`, `chi_c(G_m)=0`,
`chi_gen = 2-2G-s-n` for a connected genus-`G` curve with `s+n` punctures.

The equivalence with generic PCB is correct, and the cleanest form of it is
not displayed by the producer:

```text
generic PCB  <=>  sum_i b_i <= d - s,
```

immediate from `sum_i I_i = d-1` and `wt_i(a_gen) = b_i` (valid because a
generic `a` avoids `P_i(0)`, so `kappa_i(a)=kappa_i^+`). The producer's value
added is real: it trades the inaccessible `d` for fibre-level data
`(G,s,n,d_i)`.

Two scope facts must be attached (repairs R1, R5).

- The equivalence needs `sum_(F in T_cv(a)) wt(F) = sum_i wt_i(a)`, i.e. the
  cv-flag set on the fibre is in **bijection with the quotient lines**, one
  term per line. That is exactly how repaired Corollary 7.1 is proved in
  `c253bd12` §5 / `727f5850` §7, so the producer inherits it legitimately ---
  but a per-*cluster* reading (`sum_i q_i(a)` terms) would break the
  equivalence, and the report never says which it is. This is the live
  flag/place/series exposure in the paper.
- `(QCS)` is the **generic-fibre** statement. Transport to the every-fibre
  `PCB` of the U1\* audit is available in one direction only: since
  `wt_i(a) <= b_i` for all `a`, `E_gen >= s(a)-1` implies PCB at `a`. So
  `(QCS) => every-fibre PCB` needs the unfiled `max_a s(a) <= s`. The producer
  types its claim as generic and does not overreach, but §5.2's `QCS` is
  quantified "for every nonproper polynomial Keller pair" with no fibre
  rider on `s`.

The §5.4 budget arithmetic is correct: `sum_(selected) b_i <= sum_(all) b_i
= d-1-E_gen`, and the report correctly conditions consumption on injective
flag-to-line mapping.

## 7. Item 6 --- the Section 4.1 germ: `CONFIRMED`, and strictly stronger than stated

Exact recomputation of every displayed quantity.

```text
x = t s^6, y = s^-1  ->  x_s y_t - x_t y_s = 0 - s^6*(-s^-2) = s^4
f = t^2 + s^5/5, g = t ->  f_s g_t - f_t g_s = s^4 - 0        = s^4
```

so `dx ^ dy = df ^ dg` exactly; the local Jacobian is one. On `s=0`,
`P(z)=z^2`, `Q(z)=z`. The branch has integer exponents in `y`
(`x = z y^-6 + c y^-11 + ...`), so `K=1`, `m=1`, `kappa^-=kappa^+=1` and
`b = kappa(u-1) = 5` at height `u=6` --- the same height convention Terra
already used at `u=3` in `727f5850` §2. Generic local degree: for `z != 0`,
`t - z = -(1/(10z)) s^5 + O(s^10)`, so `Lambda = 5`. Collided: `t^2 = -s^5/5`
with `gcd(2,5)=1`, one Puiseux branch `s ~ tau^2`, `t ~ tau^5`, so
`Lambda = ord_tau(t) = 5`. Hence `w == 5` on all of `A1_z`, `I = 5`,
`I - b = 0`. Non-polynomial scope confirmed: `f = x^2 y^12 + y^-5/5`.

**The germ is not special, and I can say exactly what it pays.** In the chart
`x = t s^u`, `y = s^-1` one has `dx ^ dy = s^(u-2) ds ^ dt`, so a Jacobian-one
pair with `g = t` forces `f_s = s^(u-2)`, i.e.

```text
f = s^(u-1)/(u-1) + phi(t),      phi arbitrary,      P(z)=phi(z), Q(z)=z, b=u-1.
```

At a quotient point `z_0` with `m = mult_(z_0)(phi - phi(z_0))`, the germ is
`(t-z_0)^m * unit = const * s^(u-1)`, which has `delta = gcd(m,u-1)` branches,
each with `ord_tau(t-z_0) = (u-1)/delta`. Therefore

```text
w(z_0) = delta * (u-1)/delta = u-1 = b     for EVERY u, EVERY phi, EVERY m.
```

Verified for all `u <= 12`, `m <= 8`. It reproduces both frozen charts as
special cases: Terra's `u=3, m=2` gives `delta=2` branches of `Lambda=1` each,
`w=2=b` (matching `727f5850` §2 exactly); the producer's `u=6, m=2` gives one
branch of `Lambda=5`, `w=5=b`.

So the local barrier is much sharper than §4.1 claims: **zero excess is
identically forced on this entire family of exact Jacobian-one boundary
germs, at every collision, of every multiplicity.** And the price is equally
sharp and equally forced: `s^(u-1) = y^-(u-1)` makes `f` have a boundary pole
of order exactly `b`. This converts the producer's vague "must use the common
global polynomial `A2` filling" into one named integer, and it is the basis of
my successor proposal in §12.

## 8. Item 7 --- Section 4.2 recomputation: `CONFIRMED`

Independently recomputed in `/tmp` on letters `{0,...,5}`.

```text
sigma_+     = (1 2 3 4 5)      fixes 0     type (5,1)   index 4
sigma_-     = (0 1 2 4 3)      fixes 5     type (5,1)   index 4
sigma_infty = (0 3 1 5 2)      fixes 4     type (5,1)   index 4
```

- **Product.** `sigma_+ sigma_- sigma_infty = 1` holds under right-to-left
  (standard function) composition and **fails** under left-to-right, where it
  equals `(0 5)(1 4 2 3)`. The producer declares the convention rather than
  assuming it, and the *same* convention makes `sigma_+ sigma_- =
  sigma_infty^-1 = (0 2 5 1 3)`, type `(5,1)`. Both §4.2 claims are true under
  one consistent convention. Confirmed with the convention made explicit.
- **Transitivity.** Orbit of `<sigma_+,sigma_-,sigma_infty>` is all of
  `{0,...,5}`; the producer's reason (finite cycles with different fixed
  letters) is correct.
- **Riemann--Hurwitz.** Total index `4+4+4=12`; `2g-2 = 6(-2)+12 = 0`, so
  `G = 1`. Confirmed.
- **Punctures.** `sigma_infty` type `(5,1)` gives `s=2` poles of orders `5,1`
  summing to `d=6`; removing the `5`-cycle point over each of the two finite
  branch values gives `n=2`; `chi_gen = 2-2-2-2 = -4`. Confirmed.
- **Collision topology.** `<sigma_+sigma_-, sigma_infty> = <sigma_infty>` has
  orbits `{0,1,2,3,5}` and `{4}`. Component RH: size 5 with `(5),(5)` gives
  `2g-2 = -2`, `g=0`; size 1 gives `g=0`. Removing the finite `5`-cycle point
  and both poles leaves `G_m` and `A1`, `chi_special = 0+1 = 1`, jump `5`.
  Confirmed, and it matches `b(d_1-q_1(0)) = 5(2-1) = 5` with `epsilon(0)=0`.
- Margin arithmetic reconfirmed: `delta(f)=5`, `sum b_i(d_i-1)=5`, `E_gen=0`,
  `Xi = 5-(2+4+2-2) = -1`, and independently `E_gen = d-1-sum b_i = 5-5 = 0`.
- An exhaustive lex search over triples of `(5,1)` permutations in `S_6` with
  `sigma_+sigma_-` of type `(5,1)`, product `1`, transitive, returns the
  producer's triple as its **first** solution. The passport is reproducible.

**Two consistency properties a real family would need, which the producer did
not check and which I verified pass.** (a) `g` is unramified on the declared
affine part of *both* configurations --- generic: all ramification sits at the
four removed points; collided: `z |-> z^5` on `G_m` is etale, and the
degree-one component is an isomorphism. This is a genuine Keller requirement
(`J=1` forces `g|_(R_a)` unramified) and the passport satisfies it. (b) The
pointwise deficit `d-N(a,b) = sum Lambda(P)` holds at every `b` in both
configurations: over each finite branch value `N=1` and the puncture carries
`Lambda=5`, giving `1+5=6=d`; over any other `b`, `N=6` with no puncture.
Both pass. The control is better built than its own report shows.

**What follows from the permutation data, and what does not.**

Follows (Riemann existence): a connected genus-one degree-six cover of `P1`
with those three branch points exists; a split degree-`5`+degree-`1` cover of
`P1` with two branch points exists; their Euler characteristics after the
declared point removals are `-4` and `1`.

Does **not** follow, and would require an actual algebraic family: that the
two covers are fibres of one family --- the naive limit as two branch points
collide is an admissible cover whose base acquires a bubble carrying
`sigma_+` and `sigma_-`, so `chi_special` as computed is the Euler
characteristic of a hand-chosen main-component cover, not a limit computed
from a family; that the set of removed points is the boundary of a
compactification rather than a declaration; that there is an affine surface,
a polynomial `f`, or a second polynomial coordinate at all. The producer's
own §4.2 closing paragraph says most of this, correctly.

## 9. Item 8 --- the dependency barrier: `GAP`

The producer's honest core is right, and it does not need the control.
Section 7's entire content is `w_i >= b_i`; `E_gen = sum_a epsilon(a)` is
exactly the slack in that inequality; `EXCESS-1` is exactly `epsilon(a)>0`
somewhere. Nothing in an inequality proves its own strictness. That much is
`CONFIRMED` and is the report's best sentence (`(3.7)`, "merely proving that
some `J(a)>0` proves no strictness").

What is **not** established is the stated non-derivability. A dependency
barrier of the form "`X` does not follow from inputs `Y`" requires a single
structure satisfying `Y` and failing `X`. The producer supplies two structures
--- a boundary germ and a Hurwitz passport --- which agree on every number
they share, but which are never glued, and it says so itself
("**not** one global polynomial pair"). Numerical joint satisfiability of the
*recorded* invariants is strictly weaker than independence. Specific sentences
that outrun what is proved:

1. §0: "Hence `ATYPICAL-EXISTENCE` **does not imply** `EXCESS-1` from the
   reviewed Section-7, Suzuki, fibre-cover, or local Jacobian-one inputs."
   No model of that input set is exhibited. True replacement: "does not follow
   from the numerical and topological content of those inputs recorded here."
2. §5.1: "the degree-six control show that **no argument confined to** local
   Proposition 7.3, Riemann--Hurwitz, Suzuki defects, or fibre monodromy
   **can supply it**." This quantifies over all possible arguments. Nothing
   here proves that. In particular Riemann--Hurwitz is not independent input
   at all: on the generic fibre, `sum_(finite-value)(e_P-1) = d-chi_gen-n =
   2G-2+d+s` is an *identity* forced by `(2.2)`,`(3.5)`, so the control cannot
   fail it and its satisfaction is evidence of nothing.
3. Lifecycle header: "`PROPOSED ATYPICAL BRIDGE REFUTED AT DEPENDENCY SCOPE`".
   `REFUTED` is the wrong type for a non-model. `NOT DERIVABLE FROM RECORDED
   NUMERICAL CONTENT` is what was shown.
4. §0: "sharp at the **first relevant topological degree**." The stated
   reason --- "`d=6, s=2` is the smallest nonvacuous pole count" --- does not
   yield `6`. The zero-excess family closes at `d = b+1` for every odd `b>=3`
   with `G=(b-3)/2`, `s=n=2`, `d_1=2`, and `Xi=-1` throughout; I verified
   transitive passports at `b=3,5,7`, i.e. `d=4,6,8`, and the `d=4, G=0`
   member has the identical `Xi=-1` together with a matching `u=4` germ
   (`f = t^2+s^3/3`, `w == 3 == b`). What actually makes `6` first is the
   uncited reviewed `counterexample => td>=6`. The sentence is true; its
   stated justification is not.

No sentence overclaims a refutation of `WEIGHT-AT-ATYPICAL`, of `PCB`, or of
any theorem about actual polynomial maps. §4.2's closing paragraph and the
`Nonclaims` section are accurate and appropriately scoped; the report does
not claim a Keller counterexample, does not claim `QCS`, and does not claim
to decide JC2. The `GAP` is confined to the modality of items 1--3 above.

The one thing the controls **do** prove, at exact local-analytic scope and by
the precedent Terra already accepted in `727f5850` §2, is that a boundary
collision does not force strict weight excess. Per §7 above that is now known
for the whole germ family and every collision multiplicity. That is a real
kill of the cheapest available route to `EXCESS-1`.

## 10. Item 9 --- `QCS-MARGIN/v1`: `GAP`

The packet is well-typed and its outcome table (including the
`UNDERDETERMINED` branch and the refusal to manufacture quotient degrees from
reduced orbit counts) is sound. It is not the cheapest honest discriminator,
for a reason checkable at the desk.

**On the only named client the answer is already known to be
`UNDERDETERMINED`.** For residue-A, `SHEET6-CLASSICAL` §4a pins
`mu(F)=6=td=deg ghat` and two `g`-poles, so `d=6`, `s=2` and therefore

```text
Xi = E_gen - (s-1) = (d-1-sum_i b_i) - 1 = 4 - sum_i b_i,
```

independently of `G`, `n` and the `d_i`. But §4a itself records the finite-end
partition as two *families* with unpinned B-side and x-side place partitions
(§2b, §2c, §3b), and `acs-tdic-hostile-review-grok46-20260829.md` §4.6 already
files that as not a determined set. Taking §4a's own sample assignment (one
B-place `e=1` plus six x-places `e'=2`, giving `G=0`, `n=7`,
`sum_i d_i b_i = d-chi_gen = 13`), I enumerated all 111 feasible multisets
`{(d_i,b_i)}` with `sum d_i = 7`, `sum d_i b_i = 13`, `d_i,b_i >= 1`:

```text
Xi realized over the feasible set:  -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, +1
e.g. {(1,1),(6,2)} -> Xi=+1 ;  {(2,4),(5,1)} -> Xi=-1 ;  {(1,1)^6,(1,7)} -> Xi=-9
```

Both signs occur. The margin test cannot discriminate on residue-A, and this
was determinable from filed data before running it.

**Missing required fields.**

1. `d = td(f,g)`. Omitted, yet it is the single cheapest field: on residue-A
   it is *already pinned* and reduces the whole test to `sum_i b_i <= d-s`
   with no `G`, `n`, or `d_i` needed. Its omission also drops the strongest
   internal check available, `E_gen = d-1-sum_i b_i` versus
   `sum_i b_i(d_i-1)+chi_gen-1` --- the same kind of redundancy the packet
   correctly demands for `n` against `sum_i d_i`.
2. `c`, the number of connected components of the generic fibre, or a filed
   primitivity certificate. `chi_gen = 2-2G-s-n` silently assumes `c=1`;
   otherwise `Xi` moves by `2(c-1)`.
3. The no-duplication / injective-transport certificate for that source, plus
   an explicit statement that the flag sum in `PCB` is one term per quotient
   line and not one per cluster (see §6). Without it the equivalence being
   tested is not the one stated.
4. `kappa_i^+` and `u_i` separately, with the lattice data `K_i, e_i, n_i`, so
   that `b_i = kappa_i^+(u_i-1)` is auditable rather than asserted, plus the
   properness check `u_i > 1` (otherwise `b_i = 0` and the flag is not
   proper).
5. The exact genericity rider: `a not in union_i P_i(S_i)`, `S_i = {0} union
   Crit(P_i)`. "generic fibre value/rider" does not name the exclusion set,
   and `a = P_i(0)` is precisely where `wt_i(a) = kappa_i^- (u_i-1) < b_i`
   and the identification `wt_i(a_gen)=b_i` fails.
6. `max_a s(a)`, if the packet is ever to license every-fibre `PCB` rather
   than generic `PCB`.

## 11. Maximum exact theorem safe to promote

Everything below is `EXACT` at the reviewed perimeter of `c253bd12`/`727f5850`,
`aec8bd7e`/`758c0226`, `47eef092`, and `b96a6564`/`57e6d4a1`, with the generic
fibre connected.

> **QCS-IDENTITY.** Let `Phi=(f,g)` be a polynomial Keller pair,
> `d = td(f,g)`, with the delta-gate-passed quotient package
> `{U_i ~= A1_z, P_i, Q_i, phi_i}` indexed by the proper cv flags, actual
> cluster weights `w_i`, baselines `b_i = kappa_i^+(u_i-1)`,
> `I_i = integral_(U_i) w_i dchi_c`, `d_i = deg P_i`,
> `q_i(a) = #P_i^-1(a)`, and
> `epsilon(a) = sum_i sum_(P_i(z)=a)[w_i(z)-b_i]`. Then:
>
> 1. for every `a in A1`, `d - chi_c(f^-1(a)) = sum_i sum_(P_i(z)=a) w_i(z)`;
> 2. `epsilon(a) in Z_{>=0}` and
>    `chi_a - chi_gen = sum_i b_i(d_i-q_i(a)) - epsilon(a)`;
> 3. `sum_a epsilon(a) = sum_i (I_i-b_i) =: E_gen = d-1-sum_i b_i`;
> 4. with the generic fibre connected of genus `G`, `s` pole places and `n`
>    finite-value places, `n = sum_i d_i` and
>    `E_gen = sum_i b_i(d_i-1) + chi_gen - 1`;
> 5. `Xi := E_gen-(s-1) = sum_i b_i(d_i-1) - (2G+2s+n-2)`, and generic-fibre
>    `PCB` is equivalent to `Xi >= 0`, equivalently `sum_i b_i <= d-s`;
> 6. combining with the Ha--Le/Suzuki criterion, `0 <= chi_a-chi_gen <=
>    sum_i b_i(d_i-q_i(a))` for every `a`; hence every atypical value of `f`
>    lies in `union_i P_i({0} union Crit(P_i))` and carries a collision, and an
>    atypical value alone gives no positive lower bound on `epsilon`.

> **GERM-ZERO-EXCESS (exact local-analytic germ scope; not a polynomial map).**
> In the chart `x = t s^u, y = s^-1` (`u >= 2`), a Jacobian-one pair with
> `g = t` is exactly `f = s^(u-1)/(u-1) + phi(t)` for a polynomial `phi`. Its
> boundary quotient line is `A1_z` with `P=phi`, `Q=z`, `kappa=1`, `b=u-1`, and
> the actual cluster weight is identically `w == b`, hence `I-b = 0`,
> **for every `phi` and at every collision of every multiplicity**. Every such
> germ has `f` with a boundary pole of order exactly `b`.

Explicitly **not** safe to promote: `(QCS)` itself; every-fibre `PCB` from
generic `PCB`; any non-derivability or independence theorem; the phrase
"first relevant topological degree" without citing `counterexample => td>=6`;
any consumption of `Xi` by a td12/U1/B25/S17 budget; anything about actual
Keller counterexamples or JC2.

## 12. Repairs

- **R1.** Restate `PCB` and `PCB-EXCESS` verbatim in the report and cite
  `u1-star-pcb-independent-audit-sol56-93d-20260829.md` §5 by hash, noting
  that its Claim B carries a `FALSE/UNSUPPORTED` different-model verdict.
  The equivalence claim in §0/§3 is unauditable from the report alone.
- **R2.** State finiteness of the index set `{i}` and discharge it from
  `sum_i I_i = d-1` with `I_i >= b_i > 0`.
- **R3.** Add the connectedness hypothesis `c=1` wherever
  `chi_gen = 2-2G-s-n` is used, and record the `2(c-1)` shift otherwise.
- **R4.** Rename the weight excess (`epsilon(a) -> E(a)` or `xi(a)`); it
  collides head-on with `epsilon_c(h)` for the Euler jump in `b96a6564`,
  which the report cites as its Suzuki source.
- **R5.** State explicitly that `sum_(F in T_cv(a)) wt(F)` is one term per
  quotient line (as in the promoted proof of Corollary 7.1), not one per
  cluster; and attach the `max_a s(a) <= s` rider to any transport of `(QCS)`
  to every-fibre `PCB`.
- **R6.** Replace the four sentences listed in §9 with their non-derivability-
  from-recorded-content forms; retype the lifecycle from `REFUTED` to
  `NOT DERIVABLE FROM RECORDED NUMERICAL CONTENT`; cite
  `counterexample => td>=6` for the degree-six choice.
- **R7.** Replace §4.1 with the whole-family statement of §7 above; it is
  strictly stronger, covers every collision multiplicity, reproduces Terra's
  `u=3` chart as a special case, and names the exact price (`ord_y f = -b`).
- **R8.** Add the six missing fields of §10 to `QCS-MARGIN/v1`, and record in
  the packet that residue-A is currently `UNDERDETERMINED` with `Xi` ranging
  over `[-9,+1]`, so that the packet is not spent on it.

## 13. Cheapest decisive successor

Not a margin computation. The margin is unpinned on every filed client, and
`Xi = E_gen-(s-1)` is a restatement, so no arithmetic on existing packets can
decide anything. §7 has already localized the entire question to one integer.

> **`GERM-POLARITY-OBSTRUCTION/v1`** (desk-scale, local, no CAS, no source
> packet needed). The complete zero-excess family is
> `f = s^(u-1)/(u-1) + phi(t)`, `g = t`, in `x = ts^u`, `y = s^-1`, and every
> member has `ord_y f = -(u-1) = -b` at the boundary while `g = x y^u` is a
> polynomial. Decide exactly one question:
>
> ```text
> (STRICT-COLLIDE-POLY)  For a Jacobian-one boundary germ in which BOTH
> boundary functions are restrictions of global polynomials -- equivalently
> ord_s(f) >= 0 along every boundary component -- does a collision
> q_i(a) < d_i force w_i(z_0) > b_i ?
> ```
>
> Falsifier: exhibit one Jacobian-one germ with `ord_s(f) >= 0`, a collision,
> and `w = b`. Positive outcome: a proof that `ord_s f >= 0` forces
> `w(z_0) >= b + 1` at a collided point, which by `(FC)` and item 6 of
> QCS-IDENTITY yields `epsilon(a) >= 1` at every atypical value, hence
> `E_gen >= #{atypical values}` --- the first genuine strictness theorem, and
> the exact input the matched controls are missing.

This is decisive in both directions, is local, requires no `G`, `n`, `d_i`,
no source-complete generic-fibre packet, and no unpinned residue-A partition.
It also has a bounded stop condition: `E_gen >= #{atypical}` still needs
`#{atypical} >= s-1` for full `(QCS)`, so a positive outcome must be reported
at exactly that scope and not as `PCB`.

## 14. Nonclaims

This review promotes nothing. It does not prove or refute `PCB`, `QCS`,
`PCB-EXCESS`, `WEIGHT-AT-ATYPICAL`, or JC2; does not construct a polynomial
Keller pair or a counterexample; does not select `td=12`, type `(2,3)`, `U1`,
`B25`, or `S17`; does not land, lower, or consume any book budget or ceiling;
and asserts no exit price. The `d=4` and `d=8` family members and the
`GERM-ZERO-EXCESS` statement are exact at local-analytic germ and Hurwitz
passport scope only --- formal boundary data are not a polynomial map, a germ
plus a passport is not one global source, and `E_gen >= 0` is a floor, not
attainment. Verdicts are `CONFIRMED` for items 1--7 and `GAP` for items 8--9;
no item is `REFUTED`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `30893`.
- Body SHA-256:
  `7d2ab10a696a94f3160310fc7a985fd649e6bd006d83c7e6439e391466e816c3`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
