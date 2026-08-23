# Sol lateral sweep, round 3: after the reduction audit

**Date:** 2026-08-16  
**Scope:** new theorem and falsification avenues prompted by `REDUCTION.md`; no
item below is a promoted result

## Ranked verdict

The audit changes the objective. Killing another filed cell is secondary to
proving that a selected counterexample reaches the same normalization and then
lands in a proved-cover book. I rank by foundational payoff, distance from work
already in flight, and cost of the first exact falsification.

| rank | avenue | principal prize |
|---:|---|---|
| **1** | simultaneous GGV--Sigray normal form by cusp peak reduction | normalization transport |
| **2** | proof-carrying symbolic off-axis book | typed landing, conditional on local-case completeness |
| **3** | paired fiber-tagged Newton-cut/Eggers--Wall functor | corner-to-tree transport |
| **4** | primitive-monodromy bound or block descent | a nontrivial `td` bound from degree/boundary data |
| **5** | contextual live-kernel quotient | finite neutral-sector quotient |
| **6** | first-disagreement rigidity for neutral words | multiword off-axis depth control |
| **7** | codifferent trace moments | residue-A endgame |
| **8** | symbolic \(C_6\) prolongation module | residue-A higher-row decision |

The strongest immediate bet is Rank 1: the polynomial GGV standard pair seems
already to satisfy the *conclusion* of Sigray's rectangle lemma. The real
problem is not moving its polygon; it is proving that no target coordinate
automorphism can exploit the common-power leading forms to lower the degree
pair. Rank 2 deliberately separates **coverage** from **finite adjudication**:
an exact recursive book can prove landing even while named cylinders remain
open. Rank 4 is the high-risk item: Bézout or BKK already bounds `td` by
polynomial degree, so the worthwhile target is a much sharper primitive-group
bound or a descent that removes large degrees.

In audit terms, Ranks 1 and 3 attack the missing GGV-to-Sigray arrow; Ranks 2,
5, and 6 attack universal off-axis landing and finiteness; Rank 4 attacks the
unbounded-`td` wall; and Ranks 7--8 replace the two algebraic residue-A bets
closed today. The existential GGV quantifier is repaired by choosing the
global-minimal pair, not by new mathematics, while the conditional Sigray
entry menu needs dependency repair rather than a lateral invariant.

---

## 1. Simultaneous GGV--Sigray normal form via a coordinate-cusp lemma

### Five-line pitch

1. Write the polynomial GGV standard minimal pair with common corner \(A=(a,b)\): \(\operatorname{Supp}P\subset[0,ma]\times[0,mb]\), \(\operatorname{Supp}Q\subset[0,na]\times[0,nb]\), with both northeast corners present, \(\gcd(m,n)=1\), and \(m,n>1\).
2. For a source automorphism \(L=(u,v)\), put \(H=u_+^av_+^b\) for its top forms; then \((P\circ L)_+=cH^m,(Q\circ L)_+=dH^n\) with \(c,d\ne0\), and the exact degrees \(m(a\deg u+b\deg v),n(a\deg u+b\deg v)\) are at least \(m(a+b),n(a+b)\).
3. Prove the missing target lemma: no coordinate \(h(U,V)\) has \((m,n)\)-initial face in the cusp ideal \((d^mU^n-c^nV^m)\) when \(U=cZ^m,\ V=dZ^n\).
4. Weighted Jung--van der Kulk peak reduction would then forbid every target automorphism from lex-lowering the nondividing pair after any source automorphism.
5. Component and source-axis swaps alone make the same pair Sigray-normalized of type \((m,n)\), carrying every pre-Laurent corner of that polynomial standard pair only by relabeling or \((i,j)\leftrightarrow(j,i)\).

**Why now.** GGV's `primera condicion estandar`/`todos son Smp` rectangle
already gives Sigray Lemma 2.1(i)--(iv): after \(m<n\) and an axis swap
making the second corner coordinate no larger than the first, the corner
ratios are \(m/n\), both inequalities are strict, and
\(n/m\notin\mathbb N\). Thus almost-normalized minimality is the only serious
missing property. One must attach this theorem before the later Laurent cuts
and \(x\mapsto x^{-1},y\mapsto x^jy\), which are not polynomial Sigray
equivalences. Ordinary degree divisibility is insufficient:
\(P^n-Q^m\) really can cancel at the top; the load-bearing assertion is that
such a cusp binomial (or a multiple) cannot be the top weighted face of a
*coordinate*.

**First concrete test.** Enumerate reduced Jung words over \(\mathbb Q\) of
length at most five, triangular exponents \(2,\ldots,6\), small normalized
affine coset representatives, all coprime \(2\le m<n\le13\), and
\(c,d\in\{\pm1,\pm2\}\). Reduce each coordinate's \((m,n)\)-initial face
modulo \(d^mU^n-c^nV^m\), and demand both a nonzero remainder and evaluated
weighted multidegree at least \((m,n)\). Broaden the falsification sweep over
\(\mathbb F_{101},\mathbb F_{103}\) to word length eight, then replay every
bounded GGV family rectangle to verify the source-degree formula and type map.
This is a test, not the proof; the proof target is the coordinate-cusp/peak
lemma.

**Kill criterion.** One exact characteristic-zero coordinate whose weighted
initial face lies in the cusp ideal kills the route. So does one actual
polynomial pair in the scope of GGV's standard-minimal theorem without the
proportional rectangles, unique northeast corners, or positive \(a,b\) used
above. A finite-field-only failure is a lead, not a kill.

**Novelty guard.** The nearest existing argument is GGV's use of the unique
top corner for one chosen automorphism. No prior Sol lateral file upgrades it
to all \(K\circ(P,Q)\circ L\), isolates the coordinate-cusp lemma, or identifies
the unchanged pair with Sigray type \((m,n)\).

---

## 2. A proof-carrying symbolic off-axis book

### Five-line pitch

1. Define \(B_{\mathrm{off}}(d,E)\) first as a finitely presented parametric grammar, not as a finite list of fully expanded cells.
2. Its productions are finite entry/tree choices, bounded positive-price nodes, exact `NEUTRAL_STAR` and pure-\(b\) cylinders, merge schemas, and full retained NF-M ideals with observable root labels.
3. Every derivation evaluates to the complete fat record, provenance, and any explicit `NEEDS_NF_M` obligation at each vertex.
4. Prove an exhaustive local-transition theorem containing reviewed R1.0--R1.2/R2 laws, all \(\eta,\varepsilon,\nu=1\) variants, and only the declared subadditivity scopes.
5. Conditional on that theorem, induction parses every finite configuration; exact `OPEN` nonterminals remain visible, so symbolic landing is proved before finite adjudication.

**Why now.** `sol-normalform.md` has already isolated the infinity and supplied
the `NEUTRAL_STAR`, fat-record, symbolic-`OPEN`, and fail-closed ingredients:
priced events and merges have bounded schemas, while unboundedness lives in named
neutral, pure-\(b\), and coefficient cylinders. A recursive book can represent
those exactly without repeating NF-Z's false identification of differently
ordered histories. This would supply the missing typed total map requested by
the reduction audit once the local cases are proved complete. The new object is
the derivation-certificate grammar and independent checker, not the individual
normal-form constructors. It sharply separates “this configuration landed”
from “this landed record is dead.”

**First concrete test.** Compile only the unique \(td=7\) off-axis entry.
Require every route in the Section 11a filed perimeter, every zero-slot and
\(\varepsilon\)-variant, and adversarial mixed-subadditivity mutations to parse
and emit a constructor-by-constructor witness. Then replay the all-\(b=1\)
`BOOK-ENUM` output as the finite-language specialization. The test succeeds
only if an independent checker can reconstruct the exact fat record from the
derivation, not merely recognize a route label. This is a parser and witness
regression on a conditional filed perimeter; it is not evidence that the local
transition theorem is universally complete.

**Kill criterion.** Kill this registered grammar if the printed local cases
are not exhaustive for an actual configuration, or if soundness forces an
unconstrained wildcard whose parameters and consumers are not checkable.
Needing one new *exactly specified* constructor is a repair; needing `TOP`
means the proposed book has proved nothing.

**Novelty guard.** The constructors and the request for a typed map already
exist. Neither `BOOK-ENUM` nor the normal-form specification gives each accepted
configuration a checkable derivation in a finitely presented parametric
language. That certificate compiler is the contribution; this is coverage
infrastructure, not a renamed off-axis kill.

---

## 3. A paired, fiber-tagged Newton-cut/Eggers--Wall functor

### Five-line pitch

1. Fix a fiber \(P=a\), expand every selected \(P-a\) edge into all root factors, and carry the paired residual initial form of \(Q\) at every root.
2. In the lower-side chart \(\rho>0>\sigma\), \(x=t^{-\rho},\ y=t^{-\sigma}(\lambda+\cdots)\) reads contacts directly; other directions, \(\sigma=0\), and \(L^{(l)}\) denominators require explicit companion charts.
3. Each cut deletes the next Puiseux coefficient, while the paired record retains the lattice denominator, both valuations, residual cancellations, root labels, and whether \(Q\) is finite or has a pole.
4. Map that record first to the full fiber infinity tree \(T_a\); only then filter the pole subtree and derive those Sigray decorations actually determined by the paired residual data.
5. Prove the construction for one coherent polynomial/formal pair and fixed fiber, then combine it with Rank 1 rather than treating later Laurent cuts as maps of Keller pairs.

**Why now.** Even a proof that the same pair is simultaneously normalized
does not identify a GGV *complete chain* with Sigray's decorated Eggers--Wall
tree. The bare Newton--Puiseux/Eggers--Wall dictionary is standard and also
insufficient: a \(P\)-edge alone does not determine \(D_g\), the pattern of
\(g\), \(M\), or even pole status after common-leading-form cancellation.
Moreover \(T_a\) depends on the fiber. The repair is therefore a two-function,
fiber-tagged, all-root record, with the familiar GGV cut used only as a
computational chart. A single GGV chain follows one chosen root; the sheet
object needs the coherent factor-expanded forest.

**First concrete test.** Start with two coherent global polynomial controls
having the same \(P\)-contact forest but different \(Q\)-behavior at one
infinity branch (finite in one, a pole in the other); a \(P\)-only extractor
must conflate them and the paired extractor must not. Then instantiate one
coherent paired formal jet through the first two cuts of each of the four
Section 4 chain templates, satisfying their recorded bracket/edge equations,
and compare both functions' residuals with an independent Puiseux/Eggers--Wall
extractor at a fixed generic fiber. Independently chosen “generic edge
polynomials” do not count, because they need not come from one pair.

**Kill criterion.** Kill the proposed sufficient record if two coherent pairs
on the same fixed fiber have identical enriched \(P/Q\) cut records but
different labelled \(T_a\) images. Also kill it if factor-expanding every
certified GGV chain still misses an infinity branch needed by \(T_a\). Landing
outside the pole subtree is not a failure; it is a correct output whose
finite-\(Q\) status must be retained.

**Novelty guard.** The dictionary itself is classical. The proposed new object
is its certified application to a coherent paired GGV cut forest with a fiber
tag and a fail-closed pole filter. It claims no Sigray label that the retained
residual data do not determine.

---

## 4. Primitive monodromy as a \(td\) bound: blocks or \(A_d/S_d\)

### Five-line pitch

1. Choose a counterexample of minimal topological degree \(d\); over the complement of its nonproperness curve it gives a connected finite étale cover with transitive monodromy \(G\le S_d\).
2. Translate a full boundary/book record into inertia permutations and seek a degree-dependent bound \(s(D)\) on their supports and cycle lengths, with \(D=\max(\deg f,\deg g)\).
3. Primitive-group minimal-degree/Jordan theory should then force, above an explicit \(B(D)\), either a nontrivial block system or the exceptional alternatives \(A_d,S_d\).
4. A block system gives an intermediate field; prove that its normalization has an \(\mathbb A^2\) open model and that the induced lower-degree map is again polynomial, Keller, and nonproper.
5. Use discriminant parity to distinguish \(A_d\) from \(S_d\), then exclude the surviving case by an independent boundary/canonical-class constraint, yielding \(td(F)=d\le B(D)\).

**Why now.** Bézout already gives the uninteresting
\(td\le\deg f\deg g\); the audit needs a bound sharp enough to make a
degree/type theorem and the sheet ladder cooperate. The fat record contains
the local inertia candidates that were previously used only for a fixed
\(S_6\) passport test. Minimal-\(td\) selection makes imprimitivity potentially
fatal, while quantitative primitive-group theory offers a route from bounded
boundary support to a numerical \(B(D)\). There are two explicit new seams,
neither to be hidden: an inertia-support theorem from the geometry, and the
descent of an abstract block quotient back to a polynomial Keller map.
Even success gives a bound in terms of \(D\), not an absolute truncation:
an independent upper bound on \(D\) is still required, and GGV22 supplies a
lower-bound dichotomy rather than that missing upper bound.

**First concrete test.** Convert every filed survivor through \(td=14\) into
its allowed inertia partitions and enumerate transitive realizations with
passport SAT plus Schreier--Sims. The 169 residue-A passports already known to
admit full \(S_6\) are mandatory negative controls: the test must report
“primitive, no descent,” not invent a block. Then run scalable repeated-\(b\)
and repeated-\(M\) packet families through \(d\le60\), recording minimal
permutation support, forced blocks, and \(A_d/S_d\) survivors as functions of
\(d,D\). On the first forced-block hit, construct the intermediate fixed field
and audit normality, class group, canonical divisor, and polynomiality before
claiming a lower-degree Keller map.

**Kill criterion.** An infinite scalable family of geometrically admissible
primitive \(A_d\) or \(S_d\) passports with the same proposed degree-controlled
inertia data kills the group-theoretic bound unless the exceptional case is
independently excluded. Even a universally forced block does not prove descent:
one exact example where the intermediate normalization has no
\(\mathbb A^2\) model, or the induced map is not polynomial Keller, kills the
minimality bridge as stated.

**Novelty guard.** `GROK-MONODROMY.md` asks whether fixed residue-A branch
cycles exist and finds full \(S_6\). This asks an all-\(d\) primitive-group
question, followed by a geometric intermediate-field descent theorem. It is
also deliberately different from the same-day cross-model
Bézout/mixed-volume proposal.

---

## 5. Contextual live-kernel quotient: death before distinction

### Five-line pitch

1. Encode simultaneous neutral histories as tuples/shuffles of data words: finite event tags plus their unbounded integer registers, not as words over a falsely finite alphabet.
2. Fix the non-neutral remainder \(C\) and a declared closed symbolic domain for divisibility, cap, coefficient-ideal, and existential-completion predicates; let \(L_C\) be the live encoded histories.
3. Compute symbolic backward preimages of TERM, H8, E5F, tower, merge, and coefficient consumers inside that domain.
4. Quotient two histories only when they have the same full feasible-continuation set, including parameter valuations and provenance before existential projection: a context-indexed residual equivalence for \(L_C\).
5. Finite contextual index would quotient the neutral-history sector only; NF-P cylinders, retained NF-M ideals, and other arithmetic `OPEN`s remain explicit in Rank 2's book.

**Why now.** The NF-Z counterexamples show that equality of endpoint/product
data does not imply equality of all futures. They do *not* show that a fixed
remaining context can distinguish infinitely many histories before killing
them. The audited td-11 pure-neutral entry contexts supply a planted positive
example: arbitrarily deep co-scaled \(5^k\) tuples die at the same earlier
\(X\), so their later arithmetic is observationally irrelevant there. This
says nothing about the refile, beyond-core, NF-P, or NF-M regions, and symbolic
backward preimages are an algorithmic theorem to prove, not a free consequence
of fixing \(C\).

**First concrete test.** Build exact backward residuals for the td-11 A/B/C
pure-neutral contexts and derive a single absorbing
`DEAD-before-deep-zone` residual for all \(k\) directly from the existing DIE
horn theorem; direct tuples through depth eight are regression only. As a
mandatory negative control, use a synthetic context that explicitly reads
CE3's flipped first-cap boolean; the quotient must split that pair. Then try
the td-13 2b context, where live intruders should prevent premature collapse.

**Kill criterion.** An explicit infinite fooling set of pairwise distinguishable
*live* encoded records in one fixed filed context kills finite contextual
index. Failure to close backward preimages in the declared symbolic domain
kills the proposed algorithm even without such a set. Rank 2's exact recursive
landing book survives either failure.

**Novelty guard.** NF-D and the td-11 DIE horn already exploit death before
deep history. The new claim is a context-indexed residual construction for
multi-branch data words. It is not `sol-accel2`'s hereditary forbidden-minor
contraction or NF-Z endpoint compression, and its equivalence is intentionally
allowed to change with the consumer context.

---

## 6. First-disagreement rigidity for simultaneous neutral words

### Five-line pitch

1. Define the exact interleaved consumer ledger for two co-scaled neutral words, including an explicit end-of-word symbol, and first prove that either one-word restriction recovers the Z2 death law.
2. Within one run, consecutive factors \(u,v\) give \(k'=uvP_0/\gcd(uv-1,P_0)\ge uv\ge4\); no cross-branch use is allowed before the interleaving lemma.
3. At the first unequal prefix, add a divisibility edge only when a named competing vertex and exact tower/cap law require that denominator to divide its still-live exponent.
4. On a sector with a proved finite starting cap/divisor set, show that every live mismatch either dies immediately or strictly decreases a registered well-founded divisor state.
5. This bounds only the relative-mismatch skeleton; a synchronized common tail remains an exact symbolic cylinder in Rank 2 and need not have bounded depth.

**Why now.** CE1--CE3 identify the precise defect in commutative/product-only
normal forms: introducing the same primes in a different order flips later
caps. A genuine multi-branch configuration may be more rigid than an isolated
word because *both* sides must stay alive through those cap changes. The td-11
coupling audit suggests cap shrinkage across its audited branches, but the Z2
formula is presently a one-run statement and general off-axis caps can be
unbounded. The proposal therefore starts with the missing interleaving lemma
and is sector-relative until a finite initial divisor set is proved.

**First concrete test.** Enumerate all legal pairs of neutral words of depth at
most six in the td-11 and td-13 co-scaling windows, grouped by equal final
\(P/\mu\). Construct the exact cross-cap dependency graph and test whether
each pair that is jointly live by the *raw consumer equations* is equivalent under a fully specified
prefix-divisibility/register relation; no adjacent grouping is declared
harmless in advance. Include all CE1--CE3 anagram pairs as mandatory probes and
record the exact consumer law and first irreversible divisor drop rather than
only a final verdict.

**Kill criterion.** One exact jointly live mismatch in the registered finite-cap
sector with no decrease in the stated well-founded measure kills the lemma as
stated. An infinite family with unbounded mismatch skeletons kills the broader
avenue even after finite repairs.

**Novelty guard.** NF-Z† already poses the cross-branch problem, and a prior
idea contracts an already common neutral string. The new content is only the
proposed first-mismatch monovariant plus the interleaved-law bridge; the ordered
fat history is retained until both are proved.

---

## 7. Codifferent trace moments on the 126 residue-A conjugates

### Five-line pitch

1. Put \(K=\mathbb C(a)(x)\), \(A=K[y]/(f-a)\), \(n=\deg_y(f-a)=126\) in the residue-A orientation, and use the finite-algebra trace rather than choosing a completion branch.
2. The derivation along \(f=a\), \(\delta=\partial_x-(f_x/f_y)\partial_y\), satisfies \(\delta(g)=-1/f_y\) when \(f_xg_y-f_yg_x=1\).
3. Lagrange interpolation gives \(\operatorname{Tr}(h/f_y)=[y^{n-1}](h\bmod(f-a))/a_n(x)\), where \(a_n\) is the \(y\)-leading coefficient.
4. Hence \(\partial_x\operatorname{Tr}(g^r)=-(r/a_n)[y^{n-1}](g^{r-1}\bmod(f-a))\), and in particular \(\partial_x\operatorname{Tr}(g)=0\).
5. These trace/norm recurrences mix all \(f\)-conjugates using the joint coefficients of \(g\), and may expose constraints invisible to separate Hermite--Padé algebraization and Row-24 symbol rank.

**Why now.** The algebraicity kill failed because every D23 prefix can be
completed *separately*; the trace identity instead consumes the joint Keller
derivation before eliminating the 126 conjugates. It is valid for a finite
separable algebra, so neither irreducibility nor a guessed global branch is a
hidden hypothesis. For
\(Q(Z)=\operatorname{Norm}_{A/K}(Z-g)\), the same calculation gives
differential recurrences for the coefficients of \(Q\) via Newton identities.
This is an elimination instrument, not a claim that a new equation independent
of \(J=1\) has appeared.

**First concrete test.** Work first at \(a=0\), with \(K_0=\mathbb C(x)\).
Compute the identities by polynomial remainder in \(K_0[y]/(f)\): reconstruct
the joint polynomial \(g\) from its 189-root orbit product and known
\(y\)-leading coefficient, then evaluate \(g(x,y_i)^r\) on the 126
registered roots \(f(x,y_i)=0\), for \(r=1,\ldots,6\), through the D23-known
order. The 189 roots of \(g=0\) are *not* the trace conjugates. Before promising
D23 visibility, audit whether each remainder depends on unpinned B/x or later
tails; a generic \(a\) requires an \(a\)-adic/Hensel deformation of the
\(f-a\) roots. Compare any visible row with the earlier-row ideal at two primes,
then pull it back from the compressed chart and verify it in the original
saturated ring. The exact control \(f=x+y^{126},g=y\) passes;
\(g=y+\epsilon x\) is a non-Keller fail control.

**Kill criterion.** Kill this as a D23 endgame if every coefficient whose
dependency audit closes at D23 is already a same-depth Jacobian/no-log syzygy
and the first non-syzygetic moment necessarily uses unpinned post-D23 tails.
It may still compress PILOT12, but it is then not an independent obstruction.

**Novelty guard.** The orbit code uses Newton power sums internally, and the
prior global avenue used Mittag--Leffler pairings on one primitive. Neither
forms the finite-algebra traces of powers of \(g\) nor applies the exact
Lagrange/codifferent identity above.

---

## 8. A symbolic \(C_6\) selector recurrence and prolongation test

### Five-line pitch

1. Derive the first-occurrence Jacobian operator directly from the orbit-product selector formula with symbolic level \(k=6j+r\), separately for \(r=0,2,4\).
2. Obtain exact character-split matrices \(A_r(j)\) and source terms \(b_r(j)\), including no-log exceptions, instead of interpolating a recurrence from the observed row counts.
3. On each constant-rank chart, compute the full symbol cokernel/Spencer obstruction with preregistered degree and denominator bounds for rational-in-\(j\) identities.
4. A nonzero reduced source defect is a finite compatibility row; vanishing plus unit pivots proves only chartwise prolongability through the regime covered, with determinant-zero strata kept separately.
5. Because the pure-\(y\) regime ends at Row 41, any post-42 claim requires a new symbolic operator containing both x- and y-side variables; otherwise the theorem stops at Row 40.

**Why now.** `sol-algkill.md` correctly closes the naive claim “Row 24 is a
resonance,” but the proved \(C_6\) support congruence says nothing by itself
about constant symbol dimension or recurrence. The exact selector/product
formula is the only honest place from which a level law could come. This is a
symbolic theorem-discovery pass that uses the Rows 26--40 job now in flight as
regression data; it is not an independent solver lane, the D21 Fitting
compression, or another PILOT12 ordering.

**First concrete test.** Derive \(A_r(j),b_r(j)\) symbolically for each residue
class and only then regress against
\((24,30,36)\), \((26,32,38)\), and \((28,34,40)\) on every
sign/pole-scale fiber. Row 30 is an explicit exception test because the no-log
pins remove its \(\eta^{29}\) character and that character returns at Row 36.
Reduce the exact Spencer/source defects against the original earlier-row ideal,
cover all selected pivot and rank-drop charts, and make no post-42 extrapolation
until a combined x+y selector formula is derived. A planted triangular family
and a one-row perturbation are controls.

**Kill criterion.** Kill the recurrence avenue if the selector formula does
not yield bounded-degree rational \(A_r(j),b_r(j)\), if any exact regression row
fails, or if nonlinear source syzygies escape the computed Spencer cokernel.
A chartwise involutive symbol closes only that finite/prescribed regime; it
does not decide post-42 rows or prove that residue-A exists.

**Novelty guard.** Fitting compression eliminates one finite D21 window, and
the active job generates individual higher rows. This asks for a
selector-derived parameterized symbol and its chartwise Spencer obstruction.
It neither revives the false Row-24 resonance nor presents finite row generation
as an all-orders theorem.

---

## Recommended order of attack

1. Try to break the coordinate-cusp lemma computationally before investing in
   its proof. If it survives, prove it from the Newton polygon theorem for
   plane coordinates/weighted peak reduction.
2. Specify the symbolic-book grammar and certify the td-7 replay in parallel;
   this buys an honest landing theorem even if every finiteness idea fails.
3. Build the factor-expanded GGV forest only after the Rank-1 polynomial
   perimeter is pinned; carry paired residuals and do not transport through the
   later Laurent map.
4. Run the trace moments as the cheapest residue-A sidecar. Use the higher-row
   data already being generated only as regression for the symbolic selector
   theorem, not as a duplicate solver lane.
5. Run the passport/group pilot before attempting the hard block-descent
   geometry; a persistent primitive \(A_d/S_d\) family can kill Rank 4 cheaply.

The deliberate non-idea is a Hamiltonian-LND shortcut. For
\(D_f=f_y\partial_x-f_x\partial_y\), one has \(D_f(g)=-1\), but \(D_f\) is
locally nilpotent exactly when \((f,g)\) is already an automorphism. Indeed, if
it were LND, \(-g\) would be a slice; the slice theorem and
\(\ker D_f=\mathbb C[h]\) would give \(\mathbb C[x,y]=\mathbb C[h,g]\).
Writing \(f=P(h)\), the identity
\(1=J(f,g)=P'(h)J(h,g)\) forces \(P\) linear. The converse is
\(D_f=-\partial_g\) in coordinates \((f,g)\).

There is also a direct boundary witness. At any finite-\(g\) puncture, if
\(g-c\sim ut^e\) and a coordinate \(z\sim vt^{-m}\), then

\[
 D_f^N z\sim \frac{v}{(eu)^N}
   \prod_{j=0}^{N-1}(m+je)t^{-m-Ne}\ne0.
\]

Thus any actual realization of residue-A's pinned finite-\(g\) B/x punctures
certifies the opposite of the hoped-for lowering filtration; that avenue is
killed before it enters the ranked list.
