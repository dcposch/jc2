# Hostile review: SHEET-GATE report — is (M') really a theorem?

## 0. Integrity, scope, and verdict key

I created this report's header skeleton before analysis, then ran `shasum -a 256`
on the six frozen inputs.  All six values matched the charge exactly, in the
listed order:

```text
6d8f6667fc7d52d1e46fc4ac55f2aa2049603f06c1764ae4ac51b078435d90eb  round1033-sheet-gate-opus5-20260831.md
634940bb13bb0ad28a7bfa51f76abd987acc2b6382e3d5688262fcdb747ab23a  block-descent-a1-rank4-missing-multiplicity-identity-opus5-r2-20260831.md
221c2df9ebb4832da38cddd13b6b39c404a454946e0097338bfb2677b42d2ef1  block-descent-a1-rank4-irreducibility-coordinator-integration-fable5-20260831.md
8db5e5389e1aadf73447898748af8195a020e7150434a59d727a7758c6c2c10f  ideation-20260831T1033Z-crosspoll-grok46.md
426c7305fc215a3d55ef6a1d429f66c22071ac442384d6ca3d151b9d9029fad2  ideation-20260831T1033Z-crosspoll-sol56.md
2793104bcf746eab690ca75a2aaf2ef105b64e7be0c1826eb1fa9ed51ba992ef  ideation-20260831T1033Z-synthesis.md
```

I use `R` for `round1033-sheet-gate-opus5-20260831.md`, `P` for the
missing-multiplicity packet, `I` for the coordinator integration, and `G`, `S`,
`X` for the Grok, Sol, and synthesis cross-polls.  All citations are frozen-copy
line numbers.  No primary literature was fetched, no CAS was run, and
`jc2-lean` was not inspected.

Verdicts mean: **CONFIRMED** = the asserted statement follows at its stated
scope (minor proof clarifications are supplied here); **REFUTED** = the literal
statement is false or its advertised scope is too broad; **GAP** = it may be
true but the charged proof/custody does not establish it.

**Executive verdict.**  The core formula (M') and its defect form are genuine
theorems for a noninvertible plane Keller map under the *explicit assumptions*
(H2) `A_F` irreducible and (H3) `normalization(A_F)=A1`.  The ceiling and the
one-node exclusion also survive.  The report nevertheless does **not** pass as
charged without repairs: the frozen promoted packets establish irreducibility
of the charged branch `B subset A_F`, not `A_F` itself; the node-count row omits
`s>=1`; and the weighted-budget equivalence/global Keller-only scope is false.
The claimed `f(z)=2` closing datum is not promoted and its branch is vacuous.

## 1. Lemmas 2.1–2.3 and the category objection

1. **Lemma 2.1 — CONFIRMED.**  If `b in K` is integral over
   `A=C[F_1,F_2]`, the same monic equation makes it integral over the larger
   ring `C[x,y]`; factoriality/normality of `C[x,y]` puts `b` in `C[x,y]`.
   Thus `A subset B subset C[x,y]` exactly as claimed (`R:66-73`).  The
   finiteness of `B/A` at `R:75-76` is also true, but “Noether” is not the
   reason: one needs finiteness of normalization for the finitely generated
   complex domain `A` (equivalently, excellence/Nagata).
2. **ZMT, flatness — CONFIRMED.**  The inclusion gives an actual finite-type
   morphism `j:A2->Y`; it is birational and quasi-finite because each `j`-fibre
   lies in an `F`-fibre.  Normal-target ZMT makes it an open immersion.  Since
   a normal surface is Cohen--Macaulay and the base is a regular surface, the
   finite dominant map `q` is finite flat of rank `d`.  Grok's assertion that
   `B` need not lie in `C[x,y]` (`G:235-245`) is therefore **REFUTED**; its
   “wrong category” attack fails.
3. **Lemma 2.2 — CONFIRMED.**  If `U=Y`, then `q=F` is connected finite
   etale over `A2_C`, hence degree one.  For purity of `Y-U`, the Hartogs
   argument works: after isolating a hypothetical codimension-two component
   on an affine normal basic open, its affine complement has the same ring of
   functions, so that open immersion must be equality (`R:84-94`).  This is
   purity of the *open complement*, distinct from branch-locus purity below.
4. **Lemma 2.3 — CONFIRMED.**  Properness of finite `q` turns an escaping
   affine sequence with bounded image into a boundary limit, and analytic
   density supplies the converse.  Finite maps preserve dimensions of closed
   irreducible sets, so `q(Y-U)=A_F` is a union of curves (`R:96-106`).

The construction is airtight after replacing the single finiteness citation.
This review does **not** bootstrap the separate `Cl(Y)`, `pi_1(Y)`, or
log-Kodaira assertions merely from construction of `Y`; `R:108-114` itself
says their merits are outside this gate.

## 2. Four-box audit and Proposition 2.4

At a generic point of a selected irreducible component of `D`, the degree
identity

`d = a + sum_j delta_j e_j = a+b+sum_{e_j>=2} delta_j e_j`

is **CONFIRMED**, where only boundary components mapping to that selected
component occur in the sum.

- `(U,e>1)` **EMPTY — CONFIRMED.**  This uses Keller etaleness: on the open
  immersion `U`, `q` is `F`, so every affine fibre point has length one.
- `(U,e=1)` **NONEMPTY GENERICALLY — CONFIRMED.**  Dominance and
  quasi-finiteness make `F(F^{-1}(D_i))` dense in `D_i`.  The phrase “no
  hypothesis used” at `R:138-143` means no H2/H3; it still uses the standing
  dominant quasi-finite Keller setup.
- `(Y-U,e>1)` **NONEMPTY SOMEWHERE — CONFIRMED.**  If no boundary divisor
  were ramified generically, the branch locus would be finite.  Zariski--Nagata
  purity applies because the target is regular, the source normal, and `q` is
  finite generically separable; it makes the branch locus empty, whence `q`
  finite etale and `d=1` (`R:145-153`).  This proves existence over at least
  one component of reducible `D`; it proves it over the chosen component only
  when that component is a branch component.  Under H2 the unique component
  necessarily is one.
- `(Y-U,e=1)` **UNRESOLVED — CONFIRMED AS THE GAP.**  Its generic cardinality
  is `b=sum_{e_j=1}delta_j`; no preceding purity theorem excludes it.

**Proposition 2.4 — CONFIRMED at its literal scope.**  Over a branch component,
some `delta_j e_j>=2`; hence `sigma=a+b=d-sum_{e_j>=2}delta_j e_j<=d-2` and
`a<=sigma`.  Together with generic nonemptiness, `1<=a<=d-2`.  This also gives
`d>=3` for a noninvertible Keller map.  It is not a ceiling for an arbitrary
non-branch component when `D` is reducible.

## 3. Fibre orbits, openness, and reduced pullback

1. **Lemma 3.1 — CONFIRMED.**  Normal complex surface germs are analytically
   unibranch, and deleting a divisor from a sufficiently small irreducible
   germ leaves it connected.  Thus each centre `y` gives one connected
   covering of the punctured transverse bidisk, of degree equal to the flat
   fibre length `e_y`; centres are precisely meridian orbits.  Irreducibility
   of `D` makes `D_0` connected and its meridians conjugate, so the cycle type
   is constant.  “Unibranch” is used correctly here.
2. **Corollary 3.2 — CONFIRMED, with one omitted extension supplied.**  The
   stated Lemma 3.1 treats smooth `p`, while `R:208-211` asserts every `p`.
   At a singular `p`, repeat the same argument in each small normal germ
   `V_y`: `V_y-q^{-1}(D)` is connected, hence one `H_p`-orbit of size the
   local degree.  Its orbit is fixed iff that degree is one.  Therefore
   `s_p=#{y:e_y=1}=a_p+b_p` and `a_p=s_p-b_p` for all `p`.
3. **Lemma 3.3 — CONFIRMED as a covering of underlying reduced analytic
   spaces.**  It should not be read as saying the scheme-theoretic divisor
   `q^*D_0` is reduced or that `q` is etale transversely.  Constant centre
   count plus conservation of number makes
   `(q^{-1}(D_0))_red -> D_0` locally a finite proper bijection on each arc.
   For the attacked step (2), that arc is irreducible: a finite proper
   bijection to a disk has irreducible underlying one-dimensional space.
   Through a boundary point, purity gives a one-dimensional closed analytic
   subset of this arc, hence the whole arc.  Thus
   `B_Y intersect q^{-1}(D_0)` really is both open and closed, its complement
   is `F^{-1}(D_0)`, and the latter is an `a`-sheeted finite topological
   covering.  This closes the subtlety at `R:228-233`.
4. **Corollary 3.4 — CONFIRMED with wording repair.**  Locally at every affine
   source point, etaleness identifies the germ of `F^{-1}(D)` with the germ
   of `D`; it does not assert that every target point has an affine preimage.
   This gives lower semicontinuity and `a_p<=a`.  Etale base change of a
   reduced curve is reduced, so the claimed reducedness of `F^*(D)` is
   correct.  More precisely, the total local branch defect upstairs is
   `sum_p a_p(r_p-1)`; it is not an unweighted copy of `nu`.

## 4. Ramification formula and permutation enumeration

**Lemma 4.2 — CONFIRMED.**  Here `v_j(dx wedge dy)` is the divisor order of
the rational two-form on a smooth resolved compactification (poles negative).
At generic coordinates `D=(t=0)`, `L_j=(z=0)`, separability gives
`d(w o F)|_{L_j} != 0`, while `t o F=z^{e_j}T`.  The leading wedge term has
order `e_j-1`; Keller's constant Jacobian identifies the pulled-back target
form with `dx wedge dy`.  Thus `e_j=1+v_j(dx wedge dy)` with no missing
`delta_j` factor (`R:272-283`).

The attainability control is also **CONFIRMED**: `dx wedge dy` has order `-3`
on the original line at infinity; blowing up a point there changes the new
exceptional order to `-2`, and two further free blowups away from the strict
line give `-1,0`.  It produces a valuation with order zero, not a Keller
dicritical.  Consequently the sentence “no purely valuative or purely
topological argument can close” (`R:322-328`) is **REFUTED as an impossibility
claim**: the example only shows that the bare order/discrepancy condition does
not close the gate; a stronger valuative theorem using Keller-specific data is
not ruled out.

**Theorems 4.3 and 4.4 — CONFIRMED under H2; H3 is unused.**  For `d=3`,
`a=1` leaves boundary mass two, forcing `(delta,e)=(1,2)` and `b=0`.  For
`d=4`, hand partition of boundary mass `4-a` gives exactly

`a=2:(1,2)`; `a=1:(1,3)`; or `a=1:(1,2)+(1,1)`.

Their cycle types are respectively a transposition, a 3-cycle, and a
transposition.  If `G` means the full monodromy image, irreducible `D` normally
generates it by one meridian and connectedness makes it transitive.  A
transitive transposition-generated subgroup on four letters is `S4`; a
transitive 3-cycle-generated subgroup is `A4`.  Thus at degree four the only
sheet-location bit is the extra trivial dicritical in the transposition class,
`(a,b)=(1,1)` versus `(2,0)`.

## 5. Compactly supported Euler characteristic toolkit

**Lemma 5.1(a),(c) — CONFIRMED.**  Additivity is the compact-support long
exact sequence, and applying it off/on the finite singular set of a reduced
curve gives
`chi_c(C)=chi_c(C_tilde)-sum_p(r_p-1)`.

**Lemma 5.1(b) — CONFIRMED after a necessary wording repair.**  A noncompact
variety is not the realization of a finite ordinary simplicial complex.  Use a
finite semialgebraic triangulation of a compactification, inducing a finite
partition of `B` into locally closed open simplices.  Compact-support
additivity applies along the corresponding finite filtration, and
`chi_c(open n-simplex)=(-1)^n`.  A `k`-sheeted covering is trivial over each
open simplex, so every term is multiplied by `k`, including the noncompact
cells.  Thus the argument at `R:372-378` is valid for `chi_c`; it must not
silently assign ordinary Euler value `1` to every open simplex.

**Theorem 5.2 — CONFIRMED.**  Over `V=A2-D`, the Keller map is proper etale of
degree `d`.  Additivity and covering multiplicativity give

`1=d chi_c(V)+chi_c(F^{-1}(D))`
` =d(1-chi_c(D))+chi_c(F^{-1}(D))`.

Connectedness is true but not needed for the Euler multiplication.  Under H3,
`chi_c(D)=1-nu`; hence `chi_c(F^{-1}(D))=1-d nu` exactly as stated
(`R:385-399`).

## 6. Assembly of (M'), defect form, and weighted budget

**(M') — CONFIRMED.**  Under H2, Lemma 3.3 gives

`chi_c(F^{-1}(D))=a chi_c(D_0)+sum_p a_p`.

Under H3, `chi_c(D_0)=1-nu-s` and Theorem 5.2 makes the left side
`1-d nu`.  Rearrangement yields

`a(nu+s-1)-sum_p a_p=d nu-1`,

and subtracting from `sa` yields

`sum_p(a-a_p)=(a-1)+nu(d-a)`.

Every substitution at `R:437-455` checks.  H2 is used to have one connected
smooth stratum and one constant `a`; H3 is used only for
`chi_c(D)=1-nu`; Keller etaleness supplies the covering and reduced set counts.
The bounds `1<=a<=d-2` additionally use that the unique H2 component is a
branch component.  Thus (M') is a theorem under the explicit H2+H3 assumptions.

The relaxations are also **CONFIRMED with residual hypotheses made explicit**:

- Without H3 but retaining H2, putting
  `chi_tilde=chi_c(normalization(D))` gives
  `a(nu+s-chi_tilde)-sum_p a_p=d(nu-chi_tilde+1)-1`, exactly the formula at
  `R:458-459`.
- Without H2, one obtains the single coupled stratification identity
  `sum_i a_i chi_c(D_i-Sing D)+sum_p a_p=1-d chi_c(V)` at `R:460-467`.
  This is block-free, but it is not literally a separate copy of (M') or
  (M'-def) on each component: intersection/singular fibres remain globally
  coupled.  The §8 shorthand “component-wise otherwise” is therefore a
  **GAP/wording overclaim**.

**Weighted budget — theorem confirmed, advertised equivalences REFUTED.**  For
one selected component `D_i`, summing boundary primes above it gives the exact
identity

`sum_j delta_j e_j=d-a_i<=d-1`.

Consequently

`2 sum_{e_j>=2}delta_j + sum_{e_j=1}delta_j <= d-1`.

The second inequality is a consequence, not the “i.e.” equivalent form of the
first; it loses every excess `e_j-2`.  If all `delta_j=1`, it yields
`2m_nt+m_triv<=N-1`, but is equivalent to the exact budget only when every
nontrivial `e_j=2`.  Without H2 this is per target component, not one sum over
all dicriticals of all of `A_F`; the table's global “Keller only” scope is
**REFUTED**.  Under H2 it is a valid Orevkov-free global boundary budget.

Likewise `b=0` implies `m_Y<=floor((d-1)/2)`, but the converse at `R:475` does
not follow.  Already the admissible numerical data
`d=5,a=2,(delta,e)=(1,2),(1,1)` have `b=1` and
`m_Y=2=floor((d-1)/2)`.  The safe universal H2 bound is `m_Y<=d-2`; the strong
half-bound is a sufficient consequence of `b=0`, not an equivalent test for it.

## 7. Audit of the §8 promotion table and one-node exclusion

There is a promotion-custody gap before applying the conditional results.
`P:101-104` defines the charged branch only as `B subset A_F`; `I:12-15`
promotes `B` irreducible; and `I:28-35` says each `B_i` is an `A_F` component,
not that these exhaust `A_F`.  Indeed `P:573-577` explicitly warns about
components outside `B`.  Therefore `R:22`'s assertion that H2 for
`D=A_F` is promoted is **GAP**, most importantly in the transposition horn.

The exception is the rank-four 3-cycle horn: its `mu=3` owner exhausts the
promoted global Orevkov budget `N-1=3`; promoted dicritical surjectivity onto
`Irr(A_F)` (`I:36-44`) then excludes an extra component.  Together with the
promoted `A1` normalization at `I:30-33`, H2+H3 are covered there.  A
transposition owner costs only two and leaves room for one `mu=1` dicritical,
possibly over `B` or over another component.

Row-by-row disposition:

| §8 row | Hostile verdict and exact scope |
|---|---|
| (E) | **CONFIRMED / PROMOTE**, Keller only. |
| Covering lemma | **CONFIRMED / PROMOTE** for one irreducible `D` with degree `a`; for reducible `D`, promote only separately on each smooth component stratum. Actual rank-four transposition use is **PROVISIONAL** on H2. |
| Conversion law | **CONFIRMED / PROMOTE**, Keller; include the singular-point orbit argument supplied in §3 above. |
| Master identity | **CONFIRMED / PROMOTE AS A CONDITIONAL THEOREM** under explicit H2+H3. Replace “component-wise otherwise” by the aggregate formula of §6. Actual transposition-horn use is **PROVISIONAL**; the rank-four 3-cycle use is covered. |
| Ceiling | **CONFIRMED / PROMOTE** per actual branch component; H3 is unnecessary. Do not attach it to a purely trivial-inertia component. |
| Degree floor | **CONFIRMED / PROMOTE** for a noninvertible plane Keller map. |
| One-node exclusion | **CONFIRMED / PROMOTE conditionally** under H2+H3. Actual transposition-horn use remains **PROVISIONAL** on H2. |
| Smooth-`A_F` law | **CONFIRMED / PROMOTE conditionally**; same custody qualification. |
| Node-count bound | **REFUTED as written**; promote only with `s>=1`. Handle `s=0` by the smooth law. |
| Quota, `a`-form | **CONFIRMED / PROMOTE conditionally** under H2+H3; transposition-horn instantiation remains **PROVISIONAL**. |
| Quota, monodromy form | **CONFIRMED only if `b=0`**. Promote at `d=3` and in the covered rank-four 3-cycle horn; keep the transposition horn **PROVISIONAL/OPEN**. No classification for `d>=5` is supplied. |
| `d=4,A4,nu=0` | **CONFIRMED / PROMOTE** in the charged 3-cycle horn: quota forces every `a_p=1`; `b=0` gives `s_p=1`; a 3-cycle-generated subgroup fixing one letter is `Z/3`. |
| `d=4,S4,nu=0` | Correct only under H2+H3 and `b=0`; keep **PROVISIONAL**, as the report does, and also retain the H2 custody condition. |
| Orevkov/B-w | **REFUTED at the table's global Keller-only scope.** Promote the exact and weakened inequalities per `A_F` component, or globally under H2, with “implies” replacing “equivalent.” |
| `Y` structure | The construction is confirmed, but §2.1 did not audit every listed invariant. Retain each claim's prior disposition; do not promote the bundle from this gate alone. |
| Colouring-column experiment | **WITHDRAWN** correctly: it computes an infinity-series representation, not the required affine local groups. |

The promised independent one-node derivation is short and valid.  With one
singular point and `s=nu=1`, (M'-def) says

`a-a_p=(a-1)+(d-a)=d-1`.

But `a_p>=0` gives `a-a_p<=a<=d-2`, a contradiction.  This uses neither
`sigma` nor `b=0`.

For the node-count repair, (M') and `sum a_p>=0` give
`a(s-1)>=nu(d-a)-1>=2nu-1`.  Replacing `a` by `d-2` on the left requires
`s-1>=0`.  Hence, only for `s>=1`,
`(d-2)(s-1)>=2nu-1`; at `d=4`, integrality gives `s>=nu+1`.  For
`s=nu=0`, the adjacent smooth row instead gives `a=1`; the unqualified bound
would falsely say `-(d-2)>=-1` for `d>3`.

## 8. Coordinator-directed check of the claimed `f(z)=2` closure

**The coordinator's desk audit is CONFIRMED.**  The packet explicitly defines
`f(z)=#F^{-1}(z)` as the finite affine-source set count (`P:36-40,101-104`).
But its cycle formula is

`{mu_l repeated s_l times} union {1^{f(z)}}` (`P:485-519`),

so fixed 1-cycles include both affine points and `mu_l=1` dicritical centres.
In the transposition case it proves only
`f(z)=2-sum_{l != l_i}s_l` (`P:532-550`).  Exact `f=2` is introduced as an
*additional* companion equality at `P:537-540`; Corollary 5.5 expressly leaves
one extra `(mu,s_l)=(1,1)` dicritical and then `f=1` (`P:552-560`).  The binding
integration retains only a companion floor and marks the relevant stronger
route GAP (`I:57-71`).  The narrative reference at `P:110-112` to earlier
companion cardinalities is neither a proof in this packet nor a binding
promotion over that correction.

Thus Corollary 4.5's local conditional is **CONFIRMED**: under explicit H2, a
proved generic affine equality `f=a=2` forces `b=0`.  Its advertised charged
closure is **GAP/vacuous** because no frozen promotion proves that equality.
Moreover, without the missing `A_F=B` bridge, `f=2` on `B` alone would not
justify the whole global quota family.

What would close the local bit is either (i) a promoted exact generic affine
count `#F^{-1}(z)=2`, not merely `#Fix(g)=2` or a lower bound, or (ii) a theorem
excluding a `mu=e=1` dicritical over `B`.  What would close the entire charged
transposition application is (i) plus `A_F=B`, or the global version of (ii):
exclude every affine-image `e=1` dicritical.  The latter also excludes the only
budget-compatible extra component of `A_F`.

## 9. Compatibility with the charged (2.3') cycle-type formalism

**CONFIRMED; no contradiction.**  On a common resolved compactification, the
strict transform of a boundary prime `B_j` is the corresponding dicritical
`l`.  The transverse divisor order/local degree and mapping degrees identify

`e_j=mu_l`, `delta_j=s_l`, and `a=f(z)`

(`R:118-131`; `P:296-312,385-395,458-474`).  Proposition (5.1) of the packet
then says exactly what the four boxes say:

`sigma = a+b = f(z)+sum_{mu_l=1}s_l`,

while every `mu_l>=2` supplies `s_l` cycles of length `mu_l`.  The three
degree-four profiles translate to

`(f;(s_l,mu_l))=(2;(1,2)), (1;(1,3)), (1;(1,2),(1,1))`.

The last is precisely the packet's permitted `f=1` transposition alternative
(`P:558-560`), so the formalisms corroborate rather than conflict.  Keep packet
`s_l=deg(l->D)` distinct from report `s=#Sing D`.

## 10. Promotion recommendation, corrections, and next question

**Promotion decision.**  Promote the following mathematical statements now:

- Lemmas 2.1-2.3, the finite-normalization construction, all four-box claims
  at their corrected per-component scope, and Proposition 2.4 per branch
  component;
- Lemmas 3.1 and 3.3 in the reduced topological category, Corollaries 3.2 and
  3.4 with the supplied local qualifications, Lemma 4.2, and Theorems 4.3-4.4;
- the `chi_c` toolkit and (E);
- (M') and (M'-def) as conditional theorems under explicit H2+H3, their exact
  no-H3 formula, and the reducible aggregate formula;
- the ceiling, degree floor, conditional one-node exclusion, smooth law, and
  `a`-quota; the node bound only with `s>=1`; and the monodromy quota only
  where `b=0` is proved;
- the exact fibre budget per target component and its consequence
  `2 sum_nt delta_j+sum_triv delta_j<=d-1`; globalize this derivation only
  under H2.  When `delta_j=1`, promote
  `2m_nt+m_triv<=N-1` as a consequence, not an equivalent restatement.

At charged rank four, promote the 3-cycle/`A4` specialization: the promoted
global budget closes `A_F=B`, and `b=0` follows from the degree profile.  Keep
the following **PROVISIONAL** in the transposition horn: H2 (`A_F=B`), the
generic value `a=f(z)=2`, `b=0`, the global use of (M'), all H2-dependent
one-node/smooth/node/quota instantiations, and the `S4,nu=0` local-group row.
The conditional theorems remain promoted even while that instantiation does
not.

Correct the report as follows: cite excellence for finite normalization;
write Lemma 3.3 on reduced analytic supports; replace global “onto `D`” in
Corollary 3.4 by a germwise statement; weaken the claimed impossibility of a
valuative proof; replace “component-wise (M') otherwise” by the aggregate
identity; add `s>=1` to the node bound; replace both budget equivalences by
implications; replace `b=0 iff` by `b=0 implies`; and replace “H2 promoted at
rank four” by the `A4`/transposition split above.

**Single next question:** Can a degree-four plane Keller map have any
dicritical divisor with affine image and `e=mu=1`, equivalently
`v(dx wedge dy)=0`?

<!-- BODY-END -->
