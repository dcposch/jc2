# Grok lateral sweep 1 — post-reduction-audit, anti-coordinator edition

**Date:** 2026-08-16  
**Author:** Grok 4.6  
**Scope:** new attacks on the three load-bearing holes in `REDUCTION.md`
(no GGV↔Sigray transport, no off-axis completeness, no `td` upper bound),
plus two framings of JC2 that this repository has not touched. One file,
no other modifications, no git.

This is a generation pass, not a review. I am not proposing another
compiler increment, another dual of the tower, another certificate-mining
job, or another instrument on the residue-A Groebner cliff. Those are
what a coordinator or a GPT with this repo in context writes. The book
ladder just failed its own end-to-end audit; the right response is to
change the *object*, not to grind a taller book.

Checked against, and not repeating: `xmodel/sol-lateral.md`,
`xmodel/sol-accel2.md` Part 2, `xmodel/sol-avenues2.md`,
`xmodel/sol-normalform.md`, `RECON.md` (incl. unused 2608.05392 /
Skooi Picard / Wilson face-isolation), `REDUCTION.md` T1–T10 and the
executive five, `AUDIT.md` tail through the 2026-08-15 td-11 certificate,
`FACE-ISOLATION.md`, `SHEET6-CLASSICAL.md`, `GROK-MONODROMY.md`,
`SECTION4-AUTOMATION.md`, `lib/FAMILIES.md`. Witt–Bockstein, `ctl0`
continuation, LND descent, farm-certificate interpolation, Hall
deficiency, SOS, \(K_2\), \(p\)-adic cylinder mass, \(\mathbb A^1\)-degree,
CAP-DEN compilers, Fitting kernels, forbidden tower-minors, high-tail
gauge, fence-power identities, no-log pins, toric circuits, St 9.4
equality, Mittag-Leffler, coefficient holonomy, positive off-axis
Puiseux lifts, Gorenstein semigroups, Hermite–Padé, and fat-record /
NF-Z/P/M language quotients are all already on the board.

Novelty here means: no matching attack in that corpus. Each entry names
its nearest neighbor so the claim is falsifiable.

---

## What I would actually fund

| # | idea | gap it hits | why it is not a book increment |
|---:|---|---|---|
| 1 | Edge-power Bézout defect: \(td\le\Phi(m,n)\) | `td` upper bound | Uses GGV *as* the bound, throws the infinite ladder away |
| 2 | \(\mathrm{SL}_2\)-push of the admissible chain | transport | A dictionary, not a new cell kill |
| 3 | GGV6 intersection numbers \(=\) Sigray \(\Lambda\) | transport + mass | The unused half of a paper already in the ledger |
| 4 | Reciprocal-characteristic compactification | off-axis completeness | Compactifies the state space; does not list more words |
| 5 | Off-axis pole as Kummer cover of an on-axis book | off-axis completeness | Inherits `BOOK-ENUM`, does not extend `book_offaxis.py` |
| 6 | Class group of the compactified graph in \(\mathbf P^2\times\mathbf P^2\) | new framing, possible `td` bound | Skooi's "only \(d=3\) threads the needle," dualized to Keller graphs |

If only two pilots run: **#1 and #2**. They are finite, exact, and use
`lib/families.py` plus a handful of explicit automorphisms. They either
give the missing bound/dictionary or die in a week with a theorem-shaped
negative.

---

## 1. Edge-power Bézout defect: \(td\le\Phi(m,n)\)

**Gap:** CRITICAL 7 — no upper bound on topological degree.  
**Side:** proof. The payoff is that the sheet ladder becomes finite.

### Five-line pitch

1. For any dominant plane pair, Bézout is an identity
   \(td=\deg f\cdot\deg g-I_\infty(f,g)\), not an inequality.
2. A GGV-standard \((m,n)\)-pair is built so that every certified edge is
   a *power* (Cor. 7.4: \(\ell_{\rho,\sigma}(P)=\lambda R^{qm}\)). That is
   high-order contact at infinity, i.e. most of the Bézout budget is
   spent on \(I_\infty\).
3. The residual affine count — the thing called \(td\) — should therefore
   depend on the *shape* \((m,n)\) and the finite list of edge exponents
   \(q_h\), not on the overall scale \(B=\gcd(\deg f,\deg g)\).
4. Residue-A already looks like this: rectangular type \((2,3)\),
   \(\deg f=168\), \(\deg g=252\), product \(42336\), and \(td=6=2\cdot 3\).
   Almost every intersection lives at infinity.
5. A theorem \(td\le\Phi(m,n)\) (or even \(td\mid mn\cdot\prod q_h\))
   plus Żoładek \(td\ge 6\) plus GGV's remaining \((m,n)\)-list makes the
   book range finite, which is the one missing global reduction step.

### Nearest neighbor, and why this is not it

The campaign already uses Bézout as a *local* node-multiplicity check
(`SHEET6-CLASSICAL.md` T1/T4: \(\mu(F)=6\) on the template). It never
runs Bézout backwards on a GGV-standard *polygon* to bound \(td\) in
terms of \((m,n)\). GGV6's intersection numbers are cited in
`SECTION4-AUTOMATION.md` only as a discard filter for the 84-case and
are declared out of scope. Mixed volume appears in
`FACE-ISOLATION.md` as a char-\(p\) slogan, not as a `td` bound.
Sol's \(p\)-adic mass and \(\mathbb A^1\)-degree ideas sum local
contributions *after* a tree is chosen; this idea never builds a tree.

### First concrete test

Work *before* the Laurent move \(\psi_j\). That move leaves
\(\operatorname{Aut}\mathbf C[x,y]\) and lands at \([P,Q]=x^k\), which is
not a Keller pair (`REDUCTION.md` T3/T4). Use the polynomial supports
that `lib/FAMILIES.md` already emits.

1. For every row of `case_rows(150)` (the 34 GGV5 cases with
   \(\max(\deg P,\deg Q)\le 150\)), take \(S\) and the supports
   \(N(P)=mS\), \(N(Q)=nS\) from `supports(cd)`. Compute the mixed
   volume \(\mathrm{MV}(N(P),N(Q))\) and the axis-face corrections, so
   the BKK number of torus preimages is exact for *generic* coefficients
   on that support.
2. Separately, using only the certified edge-powers \((q_h)\) in
   `cd.steps`, write the obvious contact lower bound
   \(I_\infty\ge\sum_h(q_h-1)\cdot(\text{face length})\). Report the
   residual \(\Phi:=\deg P\cdot\deg Q-I_\infty^{\mathrm{lower}}\) next
   to \((m,n,B,\{q_h\})\).
3. Negative controls, all exact: \((x,y+x^k)\) and two nontrivial
   tame automorphisms whose Newton polygons can be put in GGV-standard
   shape. These have \(td=1\); any proposed \(\Phi\) that comes out
   \(<1\) is garbage. Positive shape-control: the residue-A rectangular
   hull \((k_f,l_f)=(126,42)\), \((k_g,l_g)=(189,63)\), which must
   return \(\Phi\ge 6\).
4. Ask one arithmetic question of the 34-row table: is \(\Phi\) bounded
   by a function of \((m,n,\{q_h\})\) alone, with no residual \(B\)
   growth? If yes, write \(\Phi\) down. If \(\Phi\) grows like \(j^2\)
   along a single family \((m_0+jd_1,n_0+jd_2)\), the crude contact
   bound is useless and the idea must pass to the *next* term in the
   edge-power (the actual leading-form factorization, not just \(q_h\)).

No `msolve`. This is lattice arithmetic plus one mixed-volume routine.

### Kill criterion

Kill the *crude* contact bound if the 34-row table shows \(\Phi\)
unbounded in \(B\) inside a single family, or if it is tautologically
equal to the mixed volume. Kill the *refined* leading-form version if a
Newton-nondegenerate pair on a GGV-standard support (coefficients
generic, not even Keller) already has more affine preimages than the
proposed \(\Phi(m,n)\). A bound that holds only after imposing \(J=1\)
is still alive — that is the actual theorem — but then the first test
must be redone on the *Keller-constrained* leading forms, i.e. the
Wronskian edge ODE already sitting in GGV, not on generic BKK. Do not
call \(\mathrm{td}\le\deg f\deg g\) a success; everyone has that, and it
does not truncate the ladder.

---

## 2. \(\mathrm{SL}_2\)-push of the admissible chain

**Gap:** CRITICAL 3 — no GGV-to-sheet arrow.  
**Side:** proof. This is the transport theorem, stated as a calculation
on the space of directional valuations rather than as a hope that two
normal forms "match."

### Five-line pitch

1. GGV and Sigray are two charts on the *same* valuative object: the
   walk of directional valuations of a pair at infinity.
2. GGV records that walk in the directions \((\rho,\sigma)\) of an
   admissible complete chain, after a source automorphism that
   standardizes the Newton polygon.
3. Sigray then applies a further nondegenerate *linear* source change
   (Lemma 2.1) that rectangularizes the two polygons, plus target
   automorphisms that mix \(f\) and \(g\) but do not move source
   valuations.
4. Linear source changes act by \(\mathrm{SL}_2\) on the space of
   directions. The missing dictionary is: push the GGV chain directions
   forward under the rectangularizing matrix, and read the Sigray type
   \((\alpha,\beta)\) and the pole/characteristic skeleton off the image
   walk.
5. If that works, the advertised reduction fork collapses to a single
   chain: select a GGV-minimal pair, rectangularize, and land in a
   *predicted* Sigray entry, with no new existence argument.

### Nearest neighbor, and why this is not it

A Sigray-rectangular pair still *has* a Newton polygon; reading
GGV-style valuations off that polygon is not transport of the
*minimal-chain* data (`xmodel/grok-reduction-review.md` finding 2).
The campaign's \(\psi_j\colon x\mapsto x^{-1},\;y\mapsto x^j y\) is the
wrong group element — it is not in \(\operatorname{Aut}\mathbf C[x,y]\)
and it is applied *after* the chain, to shrink polygons for the farm.
The valuative-tree *skim* flagged in `xmodel/sol-avenues2.md` was a
residue-A lane and is closed as such; this is a GGV-chain calculation
that never opens a Puiseux jet. Favre–Jonsson dynamics, Hall graphs,
and fat records do not appear.

Target automorphisms *do* mix the two polynomials. The pitch claims
they do not move *source* valuations of \((x,y)\). They *do* mix the
values \(v(f),v(g)\). The dictionary must track the pair
\((v(f),v(g))\) as an \(\mathrm{SL}_2^{\mathrm{target}}\)-orbit, not as
a pair of numbers. That is part of the test, not a reason to skip it.

### First concrete test

1. Take the four gate-B chains already reproduced in
   `lib/FAMILIES.md`: \((9,27)\), \((9,24)\), \((8,28)\), \((7,21)\).
   Their direction lists are
   \(((1,0),(3,-1))\), \(((3,-1))\), \(((4,-1))\), \(((7,-2))\).
2. From the *polynomial* start polygon \(S\) (before \(\psi_j\)),
   compute every linear \(L\in\mathrm{SL}_2(\mathbf Z)\) that sends the
   two positive corners onto the coordinate axes in the sense of Sigray
   Lemma 2.1 (rectangular Newton polygons, \(k_f/k_g=l_f/l_g\),
   \(k_g/k_f\notin\mathbf N_{>0}\)). There are finitely many candidates;
   the lemma says a nondegenerate one exists after a source linear
   change.
3. Push each chain direction by \(L\). Read off a candidate type
   \((\alpha,\beta)\) as the reduced ratio of the rectangular corners,
   and a candidate pole count from the number of pushed rays that land
   in the Sigray pole cone (the \(\searrow\) chamber of Notation 6.1).
4. Controls: do the same to \((x,y+x^2)\) and to
   \((x+y^2,y)\), which are automorphisms, hence \(td=1\), and whose
   Sigray type after Lemma 2.1 is computable by hand. The pushed chain
   must reproduce that type, not some other pair.
5. One farm-side check: for the \((8,28)\) support *before* \(\psi_j\),
   the dictionary must not output a Sigray entry that T7 forbids at
   every \(td\) compatible with the Bézout residual of idea 1. A
   forbidden output is a bug in the dictionary, not a JC2 theorem.

### Kill criterion

Kill if two distinct rectangularizing matrices, both satisfying Lemma
2.1's hypotheses, push the same GGV chain to two non-equivalent Sigray
types (different \((\alpha,\beta)\), or different pole-ray counts).
Kill if the image walk depends on the target automorphism — i.e. if
replacing \((f,g)\) by \((f,g+f^2)\) changes the pushed source
directions. That would mean the object being transported is not
Aut-target invariant, so it cannot be an input to Sigray. A dictionary
that works on automorphisms and fails on the four gate-B chains is
still information: it says the GGV *residual* polygons (the ones the
farm actually stores) are the wrong input, and the transport must start
from the unreduced complete chain. That is a repair, not a kill.

---

## 3. GGV6 intersection numbers are the Sigray masses

**Gap:** transport of *numerical* data, not just of directions.  
**Side:** proof. One paper, already in the dependency ledger, is sitting
on the missing numbers.

### Five-line pitch

1. GGV6 (*Pro Mathematica* 30, 2019) is titled "Approximate roots and
   intersection numbers." The campaign consumes only Proposition 2.5,
   as a predecessor filter for the \((8,28)\) branch
   (`REDUCTION.md` §2.1, `SECTION4-AUTOMATION.md` line 30).
2. Sigray's pole mass \(\Lambda(F)=D_{g,F}\deg p_F/\nu_F\) *is* an
   intersection number: the order of \(g\) at a place of a generic
   \(f\)-fiber at infinity, equivalently \(C_a\cdot E_F\) on the
   resolved compactification.
3. Approximate roots are the same objects on both sides (GGV's \(R\),
   Sigray's ladder of Proposition 4.2). The numerical dictionary should
   be \(\Lambda_i=I(R_i,Q)\) or a fixed small variant, summed to \(td\)
   by the every-fiber mass formula (T7 / Chau).
4. If that identification holds, T7's finite entry menu is not an
   independent Sigray fact: it is the GGV6 intersection table of the
   selected minimal pair, rewritten in sheet language.
5. Combined with idea 1, the entry \(E\) of a GGV-minimal counterexample
   is a function of the complete chain. The sheet engine then starts
   from a *computed* packet, not from a search over types.

### Nearest neighbor, and why this is not it

Chau's Theorem 4.4 is used to repair Sigray Proposition 5.8
(`SOL-PROP58.md`); it controls the *deficit set*, not the individual
pole masses as GGV intersection numbers. The classical battery computes
link multiplicities \(l_v\) by Bézout against curvettas, which are
intersection numbers *on the template*, after the sheet data are
already chosen. GGV6 Theorem 7.3 is named in `SECTION4-AUTOMATION.md`
and then explicitly not used. Approximate-root *ladders* are the tower
trust set; they have never been identified with GGV6's pairing.

### First concrete test

1. Bank the official GGV6 PDF (publisher page already linked from
   `REDUCTION.md`) next to `refs/`, and extract the exact statement of
   the intersection-number theorem (the object `SECTION4` calls
   Theorem 7.3) with hypotheses.
2. On the four gate-B chains, compute every pairing the theorem
   permits, using only lattice data and the certified edge-powers —
   no coefficients. This is a finite table of integers.
3. On the same four supports, run the T7 entry arithmetic formally:
   every legal \((\alpha,\beta,a,b,\nu)\) with
   \(\Lambda=ab\alpha\beta/\nu\) adding to a Bézout residual from
   idea 1. Ask whether the GGV6 table *equals* one of those partitions.
4. Control: residue-A has \(\Lambda=(3,3)\). Whatever pairing GGV6
   would assign to a rectangular \((2,3)\) hull of scale \(42\) must
   reproduce \((3,3)\), or the identification is wrong for Sigray
   rectangles and can only be tested on genuine GGV-standard (non-
   rectangular) polygons.
5. If the integers match on gate B, write the one-line translation
   \(\Lambda(F_i)=I_{\mathrm{GGV6}}(\,\cdot\,)\) and stop. That sentence
   is the transport theorem at the level of masses. Types and trees are
   then a separate (idea 2) problem.

### Kill criterion

Kill if GGV6's pairings are intersection numbers of *approximate roots
against each other* and cannot be rewritten as intersections against a
generic fiber of \(f\) or \(g\). In that case they are the wrong
numerical type. Kill if the gate-B table is strictly finer than any T7
partition (more nonzero numbers than poles T7 allows) or lives in a
different graded piece (e.g. only face-lengths, no \(\nu\)-denominators).
A mismatch on residue-A alone does not kill: residue-A is not known to
be GGV-standard. Do not treat "we already knew \(\sum\Lambda=td\)" as
success; the content is the termwise identification.

---

## 4. Reciprocal-characteristic compactification

**Gap:** CRITICAL 5 — generic off-axis grid has no completeness
certificate, because at fixed budget the post-jump state set has
unbounded numerator and \(M\).  
**Side:** proof. Completeness by compactifying the state space, not by
listing more cells.

### Five-line pitch

1. The td-7 book is complete for a *reason* that does not appear in
   the generic grid: a cap-free inversion (`BOOK-OFFAXIS.md` §11a,
   \((I5a)\)–\((I5d)\)) in which the infinite family \(w=2/(2k+1)\)
   terminates by closure, not by a guessed \(\nu\)-cap.
2. That inversion is a change of coordinate \(T=1/k\) (or \(1/\nu\))
   on the characteristic. The "unbounded numerator" is the chart
   \(T=0\) being missing.
3. Off-axis transitions (St 9.6 families, the priced menu P0, E5F, the
   merged-emission law) are rational in \((\bar\kappa,\rho,\nu,M)\).
   Clearing denominators, they become regular — or at worst mildly
   ramified — at \(T=0\).
4. The compactified state space is then a projective scheme of finite
   type over the finite entry menu of T7. Integral points with
   denominator controlled by the entry are a finite list. That list
   *is* the off-axis book.
5. NF-Z tries to quotient infinite *words*. This tries to add the
   missing point at infinity of the characteristic, so there are no
   infinite words left to quotient.

### Nearest neighbor, and why this is not it

`xmodel/sol-normalform.md` proves a Markov fat record and then
explicitly says fat-state enumeration is infinite without NF-Z/P/M.
Sol's forbidden-minor and Hall-dual ideas contract *already-killed*
routes. CAP-DEN is an early-clash test on a packet, not a compactification
of the state variety. The td-7 inversion is the existence proof that
*one* chart change compactifies *one* family; it has not been written
as a general change of coordinates on the priced menu.

### First concrete test

1. Take the priced menu P0 and the merged-emission law
   \(w'=\bar\kappa(d_q-1)/(\nu d_q)\), \(M'=\gcd(\ldots)\) (the FC5
   formula, `AUDIT.md` 2026-08-15). Rewrite every transition in the
   coordinates \((T,M,w)=(1/\nu,M,w)\), or \((1/\bar\kappa,M,w)\) if
   that is the quantity that actually unbounded in P5.
2. Evaluate the rewritten maps at \(T=0\). Record, for each St 9.6
   family, whether \(T=0\) is a regular point, a pole, or a
   base-point of a rational map.
3. Replay the 17 td-7 §11a cells in the \(T\)-chart. The
   \(w=2/(2k+1)\) family must become a *finite* set of \(T\)-integral
   points including a well-defined \(T=0\) limit, and that limit must
   be one of the already-classified closure cases, not a new living
   cell.
4. Do the same for the three td-11 L6 entries, using only the
   exact-core packets (the promoted clash theorem's input). If those
   packets compactify and the beyond-core residue (FC1) is exactly the
   locus where \(T=0\) fails to be regular, then FC1 has a geometric
   name and is no longer "the grammar is unbounded."
5. Nothing here emits a Groebner system. The output is a table:
   family \(\to\) behaviour at \(T=0\).

### Kill criterion

Kill if any legal priced transition has a pole or an essential
indeterminacy at \(T=0\) that cannot be resolved by a single further
blowup whose exceptional locus is already named in the Sigray trust
set (a merge, a jump, a root). In that case the compactification is
not cheaper than the fat record. Kill if the \(T=0\) limit of the
td-7 \(w=2/(2k+1)\) family is *not* one of the filed closure cases —
that would mean the inversion that closed td-7 is not this
compactification, and the idea has misidentified its one positive
example. A coordinate in which \(M\) remains unbounded after \(T\) is
set to \(0\) is the wrong coordinate, not a kill of the strategy;
switch the inverted variable and rerun the test.

---

## 5. An off-axis pole is a Kummer cover of an on-axis book

**Gap:** CRITICAL 5, by reduction rather than by enumeration.  
**Side:** proof. The on-axis marked-event book is the one object that
already has a landing theorem (`SHEET6-DEPTH.md` §8, T8/T9(b)).

### Five-line pitch

1. Off-axis means some pole has \(b_i\ge 2\), hence pattern degree
   \(b(\alpha,\beta)\) and \(M=b\) at entry (MP4). On-axis is the same
   sentence with \(b=1\).
2. A degree-\(b\) pattern \(p=\ominus(\eta^\nu-c^\nu)^\ell\) is the
   pullback of a simple pattern along \(\eta\mapsto\eta^b\) or along a
   Kummer extension of the base of the characteristic.
3. If that cover can be chosen so that the pulled-back pair satisfies
   the *on-axis* laws (M=1 propagation, \(w\)-alphabet, finite jump
   menu), then every off-axis configuration is a Galois orbit of an
   on-axis configuration in a cyclic extension of degree dividing
   \(b_1\cdots b_s\).
4. T7 already bounds the \(b_i\). The on-axis book is finite at each
   fixed \((s,d)\) (local marked-event landing). Completeness of the
   off-axis book is then Galois descent of a theorem the campaign
   already has, plus a check that the cover does not introduce new
   merge topologies.
5. The unique td-7 off-axis entry is the smallest possible probe:
   type \((2,3)\), masses \((3,4)\), \(M=(1,2)\). One pole is already
   on-axis; the other has \(b=2\). The cover has degree 2.

### Nearest neighbor, and why this is not it

`BOOK-OFFAXIS.md` §2 notes that St 8.5 / pattern shape still hold for
\(M\ge 2\), and that DS1 extends to \(l\ge 2\). That is "the same
formulas, more parameters," which is why the grid is unbounded. This
idea is the opposite: *change the base* so the formulas become the
\(M=1\) ones. It is not a positive Puiseux lift of an off-axis cell
(`sol-avenues2.md` #6), not a semigroup symmetry, and not "run
`book_enum.py` with the off-axis `continue` deleted."

### First concrete test

1. Freeze the td-7 entry
   \((2,3)\), \((a,b,\nu)=(1,1,2)\oplus(1,2,3)\), \(M=(1,2)\),
   \(w_0=(2,3/2)\) (`BOOK-OFFAXIS.md` §1a, `TOWER-UNIFORM.md` §0).
2. On the \(b=2\) pole, form the Kummer substitution suggested by the
   pattern: \(\eta=\zeta^2\), or \(p(\eta)=P(\eta)^2\), or the base
   change of the characteristic parameter that makes
   \(\deg P=1\cdot(\alpha,\beta)\). Write all three and discard any
   that take the pair out of the category of Puiseux series over an
   algebraic coefficient field.
3. Push the St 9.3 / Prop 8.1 data of that pole through the
   substitution. The question is binary: do the image \((w,M)\)
   satisfy \(M=1\) and the on-axis \(w\)-conservation DS2, or do they
   not?
4. If they do, take one filed td-7 route (the direct \((9,15)@2\) is
   the documented lead-pilot) and identify its image with a cell of
   `BOOK-ENUM` at \(td=7\) or at a small multiple. The on-axis prime
   panel is empty, so a *legal* image must land in a book the campaign
   already declares empty — which is a new proof of the td-7 off-axis
   kill, and a template for td-11.
5. If none of the three substitutions preserves the Keller ODE, stop
   and record the obstruction (extra ramification, non-integral
   \(\kappa\), broken Jacobian weight). That obstruction is the kill
   witness, not a prompt to invent a fourth substitution.

### Kill criterion

Kill if every candidate cover either (i) fails to be algebraic (logs,
essential singularities), or (ii) remains off-axis (\(M\) still
\(\ge 2\) at the image of the entry), or (iii) creates a merge that
the on-axis MP6 anatomy forbids and that the cover does not explain
as a Galois identification of two on-axis poles. In those cases the
off-axis world is not a cover of the on-axis world, and completeness
cannot be inherited. A cover that works at td-7 and fails at the first
td-11 entry with two \(b\ge 2\) poles is a limited theorem, not a
kill: restrict the claim to "exactly one off-axis pole" and rerun.
Do not claim completeness from a substitution that changes \(td\).

---

## 6. Class group of the compactified graph in \(\mathbf P^2\times\mathbf P^2\)

**Gap:** a framing of JC2 that `RECON.md` flagged and nobody ran; also
a possible independent `td` bound.  
**Side:** proof. Not a sheet argument.

### Five-line pitch

1. Skooi's observation on the 3-dimensional counterexample (Speyer
   thread, `RECON.md` §4) is that the forget-a-root map
   \(\mathbf P^1\times\mathbf P^{d-1}\to\mathbf P^d\) dies for
   \(d\ge 4\) because the discriminant class generates
   \(\mathbf Z/(d-2)\). Only \(d=3\) threads the needle.
2. A plane Keller map has a graph \(X=\{(p,F(p))\}\subset\mathbf A^2\times\mathbf A^2\).
   Its closure \(\overline X\subset\mathbf P^2\times\mathbf P^2\) is a
   rational surface (birational to \(\mathbf A^2\)) equipped with two
   projections of algebraic degrees \((\deg f,\deg g)\) and of mapping
   degree \(td\).
3. The discriminant / nonproperness divisor of the target projection
   is a class in \(\operatorname{Pic}(\overline X)\) or in a small
   resolution. Keller's \(J=1\) says the finite part of that projection
   is étale, so the whole class is supported at infinity.
4. Rationality of \(\overline X\) plus étale-in-the-finite plus a
   discriminant class of order depending on \(td\) is exactly Skooi's
   shape of obstruction. If the class is forced to have order
   \(td-2\) or \(td\), then only small \(td\) can occur on a rational
   surface with the available Picard rank (toric or
   Sigray-resolved).
5. This bounds \(td\) *without* Newton polygons, books, or GGV. It
   also explains, in the same breath, why the 3-dimensional
   constructions cannot descend: the plane graph does not have a
   \(\mathbf Z/(td-2)\) to host them.

### Nearest neighbor, and why this is not it

`GROK-MONODROMY.md` tests \(S_6\) *passports* of \(\hat g\) on a
generic *fiber* of the residue-A template. That is the monodromy of a
curve cover, not the class group of the graph. `SHEET6-CLASSICAL.md`
T1 computes splice determinants, which are minors of the intersection
matrix of the *fiber* at infinity, and T3 is log-BMY on that same
fiber. Jelonek T4 is about \(A(F)\) as a curve in the target, not
about \(\operatorname{Pic}(\overline X)\). Sol's \(\mathbb A^1\)-degree
is a bilinear form on a local algebra. None of these is the Picard
lattice of the graph in \(\mathbf P^2\times\mathbf P^2\). Shaska kills
graded-equivariant plane maps; this argument does not assume a
grading.

### First concrete test

1. For \(F=(x,y+x^2)\), form the closure of the graph in
   \(\mathbf P^2\times\mathbf P^2\) and resolve the two projections.
   Compute \(\operatorname{Pic}\) (or the numerical lattice) and the
   class of the nonproperness divisor of \(\pi_{\mathrm{target}}\).
   This is an automorphism, so the class must be zero or exceptional
   of a known type. The computation is the calibration.
2. Repeat for \(F=(x+y^2,y)\) and for one tame product of shears whose
   bidegree is at least \((2,3)\). All three must give the same
   qualitative answer: no torsion of order \(>1\) coming from \(td=1\).
3. Using only the residue-A Newton corners
   \((k_f,l_f)=(126,42)\), \((k_g,l_g)=(189,63)\), form the *toric*
   closure of a map with those bidegrees in \(\mathbf P^2\times\mathbf P^2\)
   (the graph of a monomial map with the same support hull). Compute
   the class group of that toric surface and the class of the
   toric discriminant. This is not residue-A, but it is the
   leading-form shadow of residue-A, and it is exact.
4. Ask whether that class has order dividing \(4=6-2\), or \(6\), or
   is of infinite order. If it has order \(4\) and the lattice cannot
   host a class of order \(4\) once the exceptional configuration of
   the *actual* residue-A splice diagram (`SHEET6-CLASSICAL.md` §1a)
   is blown in, residue-A dies by Picard, independently of D21.
5. If the toric shadow is too coarse, stop and write the missing
   data (which exceptional curves of the Sigray tree are not toric).
   Do not start a Groebner run to "refine" a lattice computation.

### Kill criterion

Kill if, on the three automorphism controls, the discriminant class in
\(\operatorname{Pic}(\overline X)\) is already of infinite order and
unconstrained by \(J=1\) — then the invariant cannot force \(td=1\)
and cannot bound \(td\). Kill if the class depends on the choice of
compactification (ordinary closure versus the Sigray resolution versus
a toric hull) by more than exceptional curves of self-intersection
\(-1\). Kill if every computation silently extends scalars in a way
that kills torsion (the whole point is a *finite* class group). A
toric shadow that does not see \(td\) is a failed first approximation,
not a kill of the graph-Pic idea; the kill is only if the same
independence of \(td\) persists after the Sigray exceptional lattice
is included. Do not recycle a positive splice-determinant as a Picard
success: positivity of minors is T1, already passed.

---

## What I am deliberately not proposing

- Anything that makes the residue-A window one instrument deeper.
  Hermite–Padé is closed (`xmodel/sol-algkill.md`). PILOT12 is
  already grinding. Another elimination order, another SOS, another
  Fitting kernel, is coordinator work.
- Anything that treats NF-Z/P/M as the off-axis completeness
  mechanism. That is the on-axis compiler's unfinished business,
  transplanted. Ideas 4 and 5 refuse that transplant.
- A dynamical Favre–Jonsson eigenvaluation argument. The valuative
  tree was already skimmed as a residue-A lane
  (`xmodel/sol-avenues2.md`). Idea 2 uses directional valuations as
  a *transport dictionary*, which is a different object.
- Markus–Yamabe / chain-realization (Castañeda–Honorato–Valenzuela-
  Henríquez, arXiv:2608.05392), even though `RECON.md` flagged the
  dim-2 converse. It is a real unused framing; it is also a vector-field
  theorem whose hypotheses (Hurwitz spectra) a Keller map need not
  satisfy. Idea 6 is the same instinct — steal a 2026 geometric
  obstruction and drop it on the plane — with hypotheses that a
  Keller graph actually has.
- "Enumerate off-axis by deleting the `continue` in
  `book_enum.py`." That is how the campaign got P5's 2691 `OPEN`s.

---

## Suggested order of death

```
idea 1 table (34 GGV5 cases)     →  Φ bounded in (m,n)?     yes: write the bound
                                   no: refine to leading forms or die
idea 2 on gate-B + 2 autos       →  unique pushed type?      yes: the dictionary
                                   no: die or drop to unreduced chains
idea 3 on the same four chains   →  integers = a T7 partition?  yes: mass transport
idea 4 T-chart of P0 / FC5       →  T=0 regular on td-7?     yes: compactness mechanism
idea 5 degree-2 cover of td-7    →  lands on-axis?           yes: inherit BOOK-ENUM
idea 6 Pic of three autos + toric shadow of residue-A
                                 →  torsion sees td?         yes: a bound with no books
```

Ideas 1–3 can share a single sitting with `lib/families.py` and the
GGV6 PDF. Ideas 4–5 share the td-7 entry packet. Idea 6 is
independent and can run on paper.

A successful #1 plus a successful #2 is the book-landing theorem the
audit said does not exist, except the landing is in a *predicted*
finite range of Sigray entries, not in a search. That is the point of
generating from the holes instead of from the existing engines.
