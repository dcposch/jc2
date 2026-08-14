# The priced inter-merge normal form

1. **STATUS — REDUCED-TO-3-LEMMAS.** The exact Markov state is proved below, and its fixed-input P0 and `nu>=2` merge skeletons are finite; a finite *symbolic* quotient still needs NF-Z, NF-P, and NF-M.
2. **Invariant list:** context/budget ledger; `(w,M,nu,kbar,rho,pdeg,i)`; complete last-cell and factor data; cost-coupled arrival provenance; exact scale expression; charged/tower history; merge/ODE certificate.
3. **PROVED finite part:** at most `td-2` positive-price events, pointwise strict numerator descent for concrete clean resonances, cap-free bounds for `k`, multiplicity partitions, and `ell_ex`, and at most `m-1` merges.
4. **CONJECTURE NF-Z / NF-P / NF-M:** finite neutral-word quotient; free-parameter/`nu=1`-schema quotient; finite coefficient type for general multi-orbit/mixed merge ODEs.
5. **11-A:** the pole-adjacent `5/8` route is **PROVED merge-impossible** by `v2(pdeg)=1` versus `3`; any preceding neutral pad scales the alleged intruder to at most `5/16`.

## 0. Verdict and meaning of “normal form”

Fix `td`, an L6-surviving entry, a labelled merge hierarchy, and a remaining
rootward context.  A **future** of a branch prefix means every continuation
through that fixed context, labelled with the data later consumers actually
use: price and terminal budget, arrival vertex and E5F offset, merge
multiplicities and full-degree synchronization, and tower gaps/exponent caps.
This is stronger than merely giving the same final ALIVE/DEAD bit.

There are two different finiteness claims which must not be conflated.

* A finite-arity exact Markov invariant exists and is proved in §1.  Its
  integer values and its neutral history have infinite range.
* A finite compiler quotient requires finitely many exact symbolic families,
  closed under transition, merge, E5F, and tower queries.  That claim is
  reduced in §3 to three independent lemmas and is **not proved**.

The literal finite-index quotient of concrete vertices is obstructed.  On any
nonempty unbounded neutral residue cylinder (for example the `w=2,M=1`
odd-characteristic family used in §4),

\[
 (w,M,\lambda)\longmapsto (w,M,\lambda),\qquad
 (\nu,\bar\kappa,\rho,P')=(u,w(u+1),w,Pu),                 \tag{0.1}
\]

with unbounded characteristic `u` in an arithmetic progression.  E5F sees
`u` and `kbar`, while H8 and the tower see `P'`.  The filed td-7 data give a
concrete counterexample to quotienting by `(w,M,price)`: at the same state
`w=2/23, M=23`, the direct vertex `(nu,kbar)=(11,1)` has E5F offset `-1`,
whereas the clean pad `(45,4)` has offset `+2`
(`TOWER-UNIFORM.md:147-173,184-201`).  These vertices do not have identical
futures.

Cost provenance is independently indispensable.  The td-7 implementation
stores `dist[(w,M)]=minimum price` but unions direct arrivals from other paths.
For example, `(w,M)=(2/3,3)` has minimum price `2`, while its direct
`nu=4` landing first costs `4`; `(2/5,5)` has minimum price `3`, while direct
`nu=12` first costs `4`.  Combining either direct vertex with the cheaper
unrelated path is not an exact route.  This is the superset-only rider already
acknowledged at `BOOK-OFFAXIS.md:640-646`.

Thus the compiler must use symbolic scale families, not a capped list and not
the td-7 `(w,M,lambda_min)+cellmap` projection.

## 1. Exact normal form

Write `P_U = deg p_{f,U}` for the **full** f-pattern degree, reserving `D_U`
for the first coordinate of `Q(U)`.  Thus

\[
 \rho_U=D_U/P_U,\qquad
 w_U=(\bar\kappa_U-\rho_U)/\nu_U.                         \tag{1.1}
\]

An exact inter-merge state is the following immutable record, with derived
fields retained as checked redundancies rather than silently recomputed under
a different convention:

\[
\boxed{
 \mathsf{NF}(U)=
 (\chi,\mathcal L;
  w,M,\nu,\bar\kappa,\rho,P,i;
  \mathcal C,\mathcal A,\mathcal S,\Theta,\Omega)
}                                                            \tag{1.2}
\]

The fields are:

| field | exact contents | future consumer |
|---|---|---|
| `chi` | `td`, entry id and packet, hierarchy id, current edge/node, branch mask, zero-slot orientation if already chosen | fixes the remaining context and prevents cross-entry/tree deduplication |
| `L` | canonical charge atoms `(vertex_id,lambda_variable,lower_bound,exact_value?,authority,multiplicity_partition,cv_inventory)`, the exact constraint system on those variables/slack, and the gross cap | shared St 9.4 budget, unresolved slack allocation, and charged predecessor strata |
| frame | exact `(w,M,nu,kbar,rho,P,i,dp,dq,X)`; derived identities are checked | P0, E5F, H8, N4, terminal P1 |
| `C` | complete last cell: Prop. 9.3 case, `(l,epsilon,n_pattern,n_edge,k,sorted(m_j),ell_ex,dp,dq)`, factor-exponent multiset, price variable/lower/exact authority, and direct/clean/pure tag | next degree transport, direct arrivals, pricing, ODE and tower caps |
| `A` | one cost-coupled endpoint witness `(kind,nu,kbar,rho,M,spent_expr,path_id,cell_id)` or an exact symbolic endpoint family | E5F and `mu | M`; never an unpriced union |
| `S` | exact full-degree expression and its constraints, plus cached valuation/gcd residues justified from that expression | equal quotient, H8 synchronization, N3/N4 |
| `Theta` | every created tower atom in canonical order: pole anchor, full degree/index, gap, factor exponents, cap witness, prefix-delta data, and maximum-gap witness | tower-tier arithmetic; no atom is forgotten before NF-Z proves a summary |
| `Omega` | canonical coefficient history, including each root-labelled local `p,q` certificate, Prop. 8.1(iv) verdict/ideal, and any coefficient type not proved local | multi-orbit legality and later coefficient consumers |

At a merge, append the following node record before starting the emitted
inter-merge chain:

\[
 \mathsf{Merge}=(
  \{\mathsf{NF}(H_e),\mu_e,\mathrm{case}_e\}_e,
  \epsilon,\nu_G,\mathsf{etaMode}_G,k,(m_j),\ell_{ex},d_p,d_q,
  \bar\kappa_G,X_G,M_G,i_G,P_G,w_{tr},
  \{n^{E5}_e\}_e,\lambda_G,\Omega_G).                     \tag{1.3}
\]

Here `mu_e | M_{H_e}` uses the **current** state, not the entry `b_e`, and

\[
 P_{H_e}=i_G\mu_e,\qquad P_G=i_Gd_p,\qquad
 w_{tr}={\bar\kappa_G-X_G/d_p\over\nu_G}.                 \tag{1.4}
\]

The record also carries whether `M_G | sum(mu_e)` was proved in its valid
scope (`epsilon=0=k` in R2.2(D)); it must not turn that conditional law into a
blanket mixed-merge filter.

### 1.1 Equality and dominance

Two concrete prefixes have the same normal form only when all fields of
(1.2), including cost-coupled provenance and canonical histories/certificates,
agree.  Symbolic records compare after alpha-renaming their integer and
coefficient variables and canonically normalizing their constraints.

A cheaper label may dominate a dearer one only if every non-budget field,
including `A`, `Theta`, `Omega`, and the charge-atom witnesses, is identical,
and the budget values are exact.  With symbolic prices, dominance additionally
needs a proved implication between the complete feasible-price/slack
constraint sets.  A lower bound or minimum price cannot dominate a different
direct arrival, charged predecessor, or cv inventory merely because `(w,M)`
agrees.

### 1.2 Sufficiency theorem

**Theorem (exact Markov sufficiency).** Two concrete inter-merge prefixes,
including concrete values of every budget/inventory variable in `L`, with
equal records (1.2) have identical labelled futures in the fixed remaining
context.  The same statement holds setwise for symbolic records only when
their complete feasible-value constraint systems agree.

**Proof.**

1. **Onward price.**  P0 chooses `l | M` and computes the next normalized
   frame from the complete current frame and chosen cell data.  The ledger `L`
   gives the exact already-used vertices, their price/inventory valuation, or
   the exact set of still-feasible valuations.  P1 uses only the final
   `w,M` plus that same global ledger:
   `psi=ceil(1/(1-w))-1` and `M(1-w)` must be a positive integer.
2. **E5F.**  At an arrival `U -> G`, the test is exactly

   \[
     n^{E5}=\nu_U\bar\kappa_G-\nu_G\bar\kappa_U\ge1,      \tag{1.5}
   \]

   equivalently `nu_U*X/mu - nu_G*rho_U` when the relevant handshake is
   installed.  The actual endpoint frame and its own cost/path occur in
   `A`; no omitted history is consulted.
3. **Merge legality.**  `mu | M` is in the incoming records.  R2.1 consumes
   `(mu,w)` on a recorded case-I/II edge and `(mu,nu*w)` only on a recorded
   case-III edge; in particular a zero edge into `nu_G=1` remains case I.
   Equal quotient consumes `P/mu`; the cell, eta mode, zero slot, root
   multiplicities, gcd, and valid subadditivity scope occur in (1.3).
4. **Tower arithmetic.**  Full scales and indices occur in `S`, and every
   already-created charged/neutral tower atom occurs in `Theta`.  In
   particular N4 uses the poleward full degree, while cap intersections use
   the recorded factor exponents.  The remaining tower transition is
   therefore a function of `(S,Theta)` and the newly appended atom.
5. **Coefficients.**  Anything not proved to disappear after the local
   Prop. 8.1(iv) solve remains in `Omega`; hence no two distinguishable
   coefficient futures are identified.

Every legal one-step extension is consequently the same relational update
from equal records.  Induction on the remaining chain/merge tree proves
equality of all labelled futures.  QED.

This theorem proves sufficiency, not finite range.  A record containing only
`lambda_lb` without its slack/cv-inventory variables is not an exact record
and has no such theorem.  Retaining an arbitrary neutral word in `Theta` is
exact but is not the desired compiler quotient.

## 2. What is already finite

### 2.1 Cap-free P0 skeleton bound

Let `b` be remaining gross price, let `w=a/d` be reduced, and consider a P0
step with arriving multiplicity `l | M`.  Put

\[
 S=\sum_{j=1}^k m_j,\quad x=\ell_{ex},\quad
 C=l(k+x)-S,\quad
 T=S+l-\epsilon(1+k+x),
\]

\[
 E=l d_q-d_p=\nu C+l-\epsilon.                            \tag{2.1}
\]

For a dirty step, P0 gives `C,T >= 1` and

\[
 E\mid l\,a\,T.                                           \tag{2.2}
\]

The following bounds are therefore cap-free.

* Every northeast orbit costs at least one, so `k <= b`.
* The searrow/NE inequalities give `1 <= m_j <= l-1`; hence there are
  finitely many sorted partitions of `S` for fixed `l,k`.
* `0 <= epsilon < l`.
* If `epsilon > 0`, `T >= 1` gives

  \[
    x\le \left\lfloor{S+l-1\over\epsilon}\right\rfloor-1-k. \tag{2.3}
  \]

* If `epsilon=0`, then `T=S+l` and, since `nu>=2`,

  \[
    2\{l(k+x)-S\}+l\le E\le la(S+l),                     \tag{2.4}
  \]

  which gives an explicit finite upper bound for `x`.
* Having fixed these data, (2.2) gives finitely many `E`, and
  `nu=(E-l+epsilon)/C` is determined.

This proves the missing budget-dependent `k`, multiplicity-partition, and
`ell_ex` stopping rule for every dirty **one-step** P0 expansion.  The hard
loops `k<7` and `ell_ex<41` in the exploratory td-7 code have no place in the
new compiler.

Changing clean resonances are also finite for each fixed concrete `w`: with
`Delta=(n-1)nu+1`, integrality gives `Delta | num(w)` and a changing step has
`w' = w*n/Delta <= 2w/3`.  Thus the numerator strictly descends.  Strict
neutral `M`-drops traverse only the finite divisor poset of `M`.  Every
`M`-preserving neutral step still changes its endpoint frame and scale and
remains in cylinder (2.5); it is never erased as stuttering.  Since every
non-clean step has price at least one, there are at most `td-2` such steps on
a gross-budget route (at most 9 for td-11 and 11 for td-13).

Once a complete ledger constraint system is supplied, budget coordinates add
no fourth unbounded family: every positive integer `lambda` lies in
`[1,b]`, there are at most `b` positive atoms, and their slack/inventory
assignments are retained as a finite feasible relation.  If the available
theorems provide only lower bounds and do not determine that relation, the
record is `UNRESOLVED_BUDGET_INVENTORY` and cannot support an emptiness
certificate; this is missing input authority, not permission to use the
minimum-price projection.

Only two one-step chain cylinders remain unbounded.

**Neutral cylinder (`n=1`).**

\[
 w'=w,\quad M'=\gcd(l,u+1),\quad
 (\nu',\bar\kappa',\rho',P')=(u,w(u+1),w,Pu).             \tag{2.5}
\]

Here and in (2.6), `u>=2`.  If `w=a/d` is reduced, vertex integrality and
BOOK-N1 are exactly
`d | u+1` and `gcd(a,u)=1`.  Together with the prescribed `M'`, these are a
finite union of residue classes modulo `lcm(l,a,d)`.

**Pure-(b) cylinder (`1 <= epsilon < l`, no extras).**  With
`e=l-epsilon`,

\[
 w'={lw\over e},\quad M'=\gcd(e,u+1),\quad
 (\nu',\bar\kappa',\rho')=(u,w'(u+1),w'),
\]

\[
 P'=P{\epsilon+lu\over l},\qquad
 \lambda\ge\left\lceil{lw\over\epsilon}\right\rceil.  \tag{2.6}
\]

Writing `w'=a'/d'` reduced, the allowed `u` again form finitely many residue
classes: `d' | u+1`, `gcd(a',u)=1`, and
`gcd(e,u+1)=M'`.  The parameter is nevertheless unbounded, and unlike a
neutral loop it occurs at one positive-price event.

Consequently P0 has a finite non-parametric skeleton plus the exact cylinders
(2.5)-(2.6).  This is stronger than the old capped closure, but it is not yet
a finite future quotient of their scale parameters.

### 2.2 Discrete merge reduction

The same calculation gives a useful finite reduction before the coefficient
ODE is solved.  Fix incoming exact records and a zero-slot choice.  This
subsection first treats `nu>=2`.  The exceptional `nu=1` branch is Prop. 9.3
case I even when a zero-chain arrives; its eta-absorbed convention and its
legal eta-factor subvariant are different schemas.  No finite reduction of
those schemas is claimed here: they are retained verbatim and assigned to
CONJECTURE NF-P below.  For `nu>=2`, let

\[
 A=\sum_{\text{nonzero arrivals}}\mu_e+\sum_{j=1}^k m_j,
 \qquad Q=r_0+k+x,
\]

so that

\[
 d_p=\epsilon+\nu A,\qquad d_q=1+\nu Q.                  \tag{2.7}
\]

Here `r_0` counts nonzero arriving orbits and `x=ell_ex`.  There are finitely
many arrival multiplicities because `mu_e | M_e`; `r_0 <= m`; budget gives
`k <= b`; and the NE inequalities give
`m_j < min_e(mu_e)` (and the analogous finite bound on a free zero-root
multiplicity).

Each edge supplies an affine handshake in `(kbar_G,X_G)`:

\[
 X_G=\mu_e(\bar\kappa_G-w_e),\qquad
 X_G=\mu_0(\bar\kappa_G-\nu_e w_e)\ \text{on a zero edge}. \tag{2.8}
\]

If two affine rows differ, they either contradict or pin `(kbar_G,X_G)`.
Writing the pinned ratio `X_G/kbar_G=p/q` in lowest terms, (2.7) gives

\[
 \nu(qA-pQ)=p-q\epsilon.                                 \tag{2.9}
\]

The right side cannot vanish: that would say `d_p=epsilon*d_q`, forbidden by
R1.0's root-multiplicity law.  Hence `qA-pQ` is a signed divisor of the fixed
nonzero right side; `x` and `nu` are determined from finitely many divisors.

The only unpinned case is when every affine row is the same: all arrivals
have one multiplicity `mu` and one effective weight `h` (where a zero edge
uses `h=nu_e*w_e`).  Put `h=a/b` reduced and

\[
 C=\mu Q-A,\qquad E=\mu d_q-d_p=\mu-\epsilon+\nu C,
 \qquad
 \bar\kappa_G={a\mu(1+\nu Q)\over bE}.                   \tag{2.10}
\]

For `nu>=2`, integrality bounds every non-pure case:

* if `epsilon=0`, the identity
  `C*dq-Q*E=-(A-epsilon*Q)` gives `E | a*mu*A`;
* if `0<epsilon<mu` is a free NE zero root,
  `A-epsilon*Q>0` bounds `Q`, and then the same identity bounds `nu` unless
  `C=0`;
* if `epsilon=mu` is an arriving zero edge, `E=nu*C`; integrality in
  (2.10) gives `nu | a*mu` and `C | a*(nu*A+mu)`.

For auditability, these divisibilities do not assume a hidden characteristic
cap.  Integrality of (2.10) says `b*E | a*mu*dq`; multiplying
`C*dq-Q*E=-(A-epsilon*Q)` by `a*mu` gives the first two bounds.  In the last
case, reduction modulo `nu` gives `nu | a*mu`, while
`mu*dq=nu*A+mu+nu*C` gives the displayed divisor bound for `C`.  Moreover

\[
 C=\mu(k+x)-\sum_j m_j
   =\mu x+\sum_j(\mu-m_j),                              \tag{2.11}
\]

so `C=0` is exactly `k=x=0` under the strict NE inequalities.

Thus only one parametric shape survives the proved `nu>=2` arithmetic
reduction, while one exceptional family is deliberately left unreduced:

1. `C=0`, necessarily with no nonzero NE or q-extra orbit, giving a pure
   `nu`-cylinder (with or without one free zero root);
2. **UNREDUCED:** `nu=1` case-I schemas, retaining both the eta-absorbed and
   legal eta-factor variants, where rational `kbar` can allow an `x`-tail
   such as td-7's `(2,2t)` family.

All pinned `nu>=2` joins (including pinned examples with every `mu>=2`)
therefore have a finite discrete menu for fixed incoming records.
Equal-handshake `nu>=2` joins have a finite menu plus the pure cylinder.
Retaining every case-I/eta branch separately is conservative and cap-free,
but its finite canonicalization is unproved.  Thus this subsection proves
finite discrete **schemas only for `nu>=2`**; it does **not** prove a finite
coefficient type or a terminating projection when the incoming records
themselves contain symbolic scale parameters.

### 2.3 What the depth theorem contributes

On an M=1 merge-free segment, the promoted depth theorem proves a finite
`w`-alphabet and finite **cumulative jump-cell menu**.  It does not prove that
equal `w` (or equal `(w,M,price)`) gives equal E5F/tower futures.  Its safe
proved representative bound is

\[
 d_0\le 2\,\mathrm{gen}(W)+2,                             \tag{2.12}
\]

not the sharper `gen(W)+2` still printed in the body of
`SHEET6-DEPTH.md`; see `SHEET6-DEPTH-REVIEW.md:183-218,245-267`.
Equation (2.12) may be used only for the menu-existence projection.  It may
not truncate endpoint frames, degree products, E5 pads, or tower histories.

## 3. The exact remaining lemma list

These three obligations are independent relative to the cited kernels: NF-Z
already occurs with no charged step, NF-P occurs in one fixed-depth charged
step, and NF-M remains after every integer characteristic is fixed.

### CONJECTURE NF-Z — neutral-word future quotient

For every fixed `(td,entry,hierarchy)` and bounded non-neutral skeleton, the
arbitrary word of neutral cells (2.5) admits one of finitely many effective
canonical **symbolic summary schemas**, with exact parameter domains and a
closed concatenation operation, such that a schema specialization determines
exactly:

1. the endpoint `(nu,kbar,rho,M)` and every legal cost-coupled E5F reroute;
2. the total full-degree scale needed by equal quotient and H8;
3. all tower gap, live-factor cap, and prefix-delta predicates contributed by
   every neutral vertex, not merely their maximum under a td-7 window; and
4. the result of attaching any remaining charged/merge skeleton.

N1 and N4 are useful update identities, not a proof of this statement.  N4
controls gaps monotonically; it does not by itself quotient the unbounded
degree product or all H8/cap congruences.  A proof may use a finite transition
monoid of consumer predicates, but it must exhibit that monoid and prove it
closed.  A depth sample or `d0` menu representative is insufficient.

### CONJECTURE NF-P — parameter/exceptional-schema quotient

Every bounded collection of free parameters from pure-(b) cells (2.6), pure
equal-handshake merge cylinders, and **every** `nu=1` case-I merge schema
(including the eta-absorbed and legal eta-factor variants) admits an
effective finite canonical partition on which P0 divisibility, current `M`,
E5F, degree synchronization, and tower predicates have exact symbolic
updates and decidable emptiness.  This includes proving a complete discrete
schema and correct case-I handshakes for `nu=1`.

The partition must also be closed under the **full reflexive-transitive
closure of the non-neutral/state-changing P0 relation**, including every
zero-cost changing clean resonance generated by a parameterized `w`, and must
return only finitely many exact successor summaries.  Each intervening
`M`-preserving neutral block is represented by the NF-Z summary.  Pointwise
numerator descent for each concrete specialization does not imply this
uniform symbolic closure.

This is not NF-Z: a single positive-price pure-(b) vertex has an unbounded
characteristic even at depth one, and it changes both the frame and full
degree by the affine factor `(epsilon+l*nu)/l`.  The existing conjecture
“pure-b characteristic invariance” at
`xmodel/sol-gluing-design.md:1149-1154` is a special case, not a proof.

### CONJECTURE NF-M — multi-orbit coefficient locality

For every fixed discrete merge schema from §2.2 **or produced by NF-P**,
including every `nu=1` eta mode and every parametric cylinder, the exact
Prop. 8.1(iv) equation modulo orbit permutation and the allowed scaling has a
finite computable certificate type with this property:
two solutions of the same type and the same emitted frame have identical
chain/E5F/tower futures.  The procedure must either return an impossibility
certificate or retain every coefficient/root label that a later edge can
observe.

This is the missing generalized multi-factor ODE theorem.  Solving one fixed
cell does not prove it uniformly in a pure `nu`- or `x`-tail, and forgetting a
positive-dimensional solution family without a locality proof is not sound.

### Conditional completeness theorem

**Theorem (conditional).** If NF-Z, NF-P, and NF-M hold, then for each fixed
`(m,td)` the records (1.2)-(1.3) have a finite, computable,
completeness-preserving symbolic quotient.

**Proof.**  The entry and labelled hierarchy sets are finite, with at most
`m-1` merge nodes.  Section 2.1 bounds every non-parametric P0 choice and the
number of positive-price atoms; for each concrete rational `w`, a changing
clean resonance strictly decreases its reduced numerator.  Section 2.2
reduces every `nu>=2` merge to finitely many fixed schemas and a pure
cylinder.  NF-Z replaces every arbitrary neutral word by a member of a finite
closed summary set; NF-P handles the bounded number of free integer
cylinders, every exceptional `nu=1` schema, and their **uniform** clean-
resonance closures; NF-M replaces every local coefficient family by a finite
future-local type.  The exact transition formulas of §1 then map a finite set
of canonical records to a finite set.  Induction over the hierarchy proves
that every concrete route specializes one record and that every symbolic
transition specializes only legal concrete transitions.  Exact Markov
sufficiency (§1.2) proves that quotienting equal records loses no future.
QED, conditional on the three labelled conjectures.

These are three distinct obligation classes after the complete symbolic P0
closure has been folded into NF-P and exact budget/inventory constraints have
been made part of `L`.  None of the three conclusions follows from the cited
kernels or from either of the other two as stated: without NF-Z there is
unbounded zero-cost depth; without NF-P there is an unbounded characteristic
at one charged vertex and an unclassified `nu=1` merge; without NF-M there is
unclassified coefficient data even after all integer parameters are frozen.

## 4. Worked example: td-11 entry 11-A

The entry packet is

\[
 [M=1,w=2;P=2]\quad+\quad[M=2,w=3;P=4]
\]

of type `(2,3)` (`xmodel/sol-td11-13-scope.md:290-296`).

### 4.1 Strict branch

The first branch has `M=1,w=2`.  MP5 makes every later pre-merge vertex a
simple clean cell.  Since `W(2)={2}`, no changing clean resonance exists.
For a neutral characteristic `u`,

\[
 (\bar\kappa,\rho,w)=(2(u+1),2,2).
\]

BOOK-N1 gives

\[
 1=\gcd(2(u+1),u)=\gcd(2,u),
\]

so every multiplier is odd.  Every possible arriving full degree has

\[
 P_1=2C,\qquad C\ \text{odd},\qquad v_2(P_1)=1.          \tag{4.1}
\]

Its pole-adjacent tower vertex `X` has

\[
 g_X={\nu_X+1\over2\nu_X},\qquad \nu_X\ \text{odd}.     \tag{4.2}
\]

Thus `5/8 > g_X` exactly for the advertised odd `nu_X>=5` family.

### 4.2 The off-axis resonance

On the second branch the clean cell

\[
 (\Delta,n,\nu)=(3,2,2),\qquad d_q=5,
\]

sends `(w,M)=(3,2)` to `(2,1)` at price zero.  With no preceding vertex,

\[
 (\nu,\bar\kappa,\rho,w,P,g)=(2,5,1,2,8,5/8).           \tag{4.3}
\]

Both allowed arrival multiplicities `l=1,2` give the same full degree because
`P'=P*d_p/l=4*(2l)/l=8`.

After (4.3), `M=1,w=2`; the preceding argument forces every later
characteristic multiplier to be odd.  Hence every arrival on a route
containing the pole-adjacent resonance has

\[
 P_2=8B,\qquad B\ \text{odd},\qquad v_2(P_2)=3.          \tag{4.4}
\]

For completeness, zero-cost neutral padding *before* the resonance is also
symbolic.  At `w=3` its characteristic `u` obeys \(3\nmid u\) by N1 and
multiplies the full degree by `u`.  If `A` is the product of such prefix
indices, the resonance has

\[
 P_2=8AB,\qquad g_R={5\over8A},\qquad v_2(P_2)\ge3,       \tag{4.5}
\]

where `B` is the odd post-resonance product.  Only `A=1` is the actual `5/8`
intruder.  Any nonempty prefix has `P_before>=8` (every genuine chain vertex
at least doubles full degree), hence `g_R<=5/16<g_X`; it is already outside
the dangerous window.

### 4.3 Merge rejection

There is exactly one merge when `m=2`.  If it is the root, R2.1 case IV
requires every arriving `w<1`; for this resonance family both branches arrive
with `w=2`, so the route dies.

If it is interior, current `M=1` on both branches forces
`(mu_1,mu_2)=(1,1)`.  MP6(b)'s equal-quotient law, independent of the
zero-slot orientation, requires

\[
 P_1=i_G\mu_1=i_G=P_2.                                  \tag{4.6}
\]

Equations (4.1) and (4.4), or the stronger (4.5), contradict (4.6) by their
2-adic valuations.  Therefore the direct `5/8` family is **PROVED
unrealizable at the unique merge**; E5F and the local ODE never fire.

The compiler can record the finite rejection certificate

```text
H8_EQUAL_QUOTIENT_VP_MISMATCH {
  prime: 2,
  arrivals: [(mu=1, vp_pdeg=1), (mu=1, vp_pdeg>=3)]
}
```

This removes the specific conjecture at
`xmodel/sol-td11-13-scope.md:337-355`.  It does not close every other charged
route of entry 11-A, and it does not prove NF-Z globally; here only the
two-adic projection of the neutral scale monoid is needed, and it already
separates the branches.

## 5. Compiler interface

The census engine should expose immutable records equivalent to the following
schema.  Integers and rationals are exact; symbolic variables carry an exact
domain, never an enumeration cap.

```text
PricedState {
  version: "priced-intermerge-nf/v1"
  context: ContextKey
  budget: BudgetLedger
  frame: Frame
  producer: EntryAtom | ChainRecord | MergeRecord
  endpoint: ArrivalWitness | SymbolicEndpointFamily
  scale: ScaleExpr
  tower: TowerHistory
  merge_history: PersistentList<MergeRecord>  # equality expands parent ids
  coefficient_history: CoefficientHistory
  open_obligations: Set<NEEDS_NF_Z | NEEDS_NF_P | NEEDS_NF_M |
                        UNRESOLVED_BUDGET_INVENTORY>
}

Frame {
  w, M, nu, kbar, rho
  Q_first_D, pdeg_full, index_i
  red_dp, red_dq, X
}

CellAtom {
  prop93_case, l, epsilon, n_pattern, n_edge, nu
  k, sorted_ne_multiplicities, ell_ex
  dp, dq, emitted_M
  lambda_var, lambda_lb, lambda_exact_if_proved, lambda_authority
  cv_inventory
  factor_exponents, direct_or_pad_tag
}

ChainRecord { parent_state_id, cell: CellAtom }

ArrivalWitness {
  kind: ENTRY | DIRECT | CLEAN_RESONANCE | NEUTRAL_PAD | MERGE_EMISSION
  nu, kbar, rho, M
  spent_expr, path_id, producing_record_id
}

ScaleExpr {
  exact_expression
  integer_domains_and_gcd_congruences
  cached_prime_valuations_and_cap_residues  # derived, checked
}

BudgetLedger {
  gross_cap
  lambda_vars[]
  charge_atoms[]  # vertex id, var, lb, exact?, partition, cv inventory, authority
  feasible_price_slack_inventory_constraints
  spent_expr
  concrete_spent_if_instantiated
}

TowerHistory {
  pole_anchor
  charged_atoms[]
  neutral_summary_or_exact_word
  live_factor_cap_witnesses[]
  max_gap_and_witness
  prefix_delta_signature
  H8_scale_constraints
}

MergeRecord {
  child_state_ids[]
  arrival_mu[]
  zero_slot, prop93_cases[]
  family1_eta_mode: NOT_APPLICABLE | ETA_ABSORBED | ETA_FACTOR
  equal_quotient_i
  epsilon, nu_G, k, sorted_ne_multiplicities, ell_ex
  dp, dq, kbar_G, X_G, M_G, pdeg_full_G, w_trunk
  e5_offsets[]
  subadditivity_authority
  lambda_atom
  coefficient_certificate
}

CoefficientHistory {
  root_labelled_local_pq_certificates[]
  prop81iv_verdicts_and_ideals[]
  coefficient_variables_and_constraints
  locality_type_if_proved
}
```

`ScaleExpr` needs at least these constructors:

```text
CONST(P)
CHAIN_SCALE(P, l, dp)                 # (P/l)*dp, exact integrality constraint
NEUTRAL(P, u, domain)                 # P*u
PURE_B(P, l, epsilon, u, domain)      # P*(l*u+epsilon)/l
MERGE(i_G, dp)                         # i_G*dp
PRODUCT(left, right)
NEUTRAL_STAR(base, domain, summary)   # forbidden for a final census until NF-Z
```

The compiler rules are:

1. Keep a separate state label for every distinct endpoint/path/cost/tower
   signature.  Do not attach a unioned `cellmap` to `lambda_min`.
2. Canonicalize a multiplicity vector by sorting only genuinely symmetric
   orbit labels; never sort labelled incoming branches.
3. Apply E5F to each actual or symbolic endpoint witness.  Rejection of one
   witness does not reject its state until every cost-legal pad/reroute family
   is exhausted.
4. At every inner merge, choose `mu | current M`, enforce all
   `pdeg_full/mu` equalities before emitting the trunk, and retain the full
   merge frame.
5. Deduplicate only on the full future signature.  Pareto-prune two concrete
   labels only when every non-budget field and charge witness is identical
   and both prices are exact; for symbolic ledgers require a proved feasible-
   set implication as in §1.1.
6. A run with any open obligation, including
   `UNRESOLVED_BUDGET_INVENTORY`, may emit a symbolic candidate or `OPEN`; it
   may not certify an empty panel.  A scalar lower bound is never promoted to
   an exact ledger.
7. No production loop may use the exploratory `k`, `ell_ex`, `nu`, state,
   numerator, or `M` caps.  It must attach the stopping proof from §2 or a
   named conjecture status.

Minimum regression gates before compiler construction:

* distinguish td-7 direct `(w,M,nu)=(2/3,3,4)` at cost `4` from the same
  state's minimum cost `2`;
* distinguish the td-7 `w=2/23,M=23` E5F offsets `-1` and `+2`;
* assert the safe depth metadata `d0=2*gen(W)+2`, not `gen(W)+2`;
* emit the 11-A `H8_EQUAL_QUOTIENT_VP_MISMATCH` certificate for every odd
  `nu_X>=5`, without enumerating that family.

Until NF-Z/NF-P/NF-M are proved, this interface is the safe stopping point:
it is an exact, auditable normal form and a finite bounded-arity schema, but
not yet a terminating finite census quotient.
