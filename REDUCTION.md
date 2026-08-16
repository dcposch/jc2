# REDUCTION.md — from a planar Keller counterexample to the campaign books

**Status (2026-08-16): hostile dependency audit / consolidation master.**

## Executive verdict

The advertised end-to-end reduction

\[
  \text{Keller counterexample}
  \Longrightarrow \text{GGV polygon data}
  \Longrightarrow \text{sheet data of degree }d
  \Longrightarrow \text{an enumerated book entry}
\]

is **not a theorem in the repository or in the cited literature**.

What is presently supportable is weaker:

1. If the plane Jacobian conjecture is false, GGV's published minimal-pair
   theorem permits the selection of **some** globally minimal counterexample
   in a standard Newton-polygon frame. This is an existential selection from
   all counterexamples, not a normalization theorem for every given
   counterexample.
2. Independently, any chosen counterexample can be minimized in Sigray's
   source/target polynomial-automorphism equivalence class and put in
   Sigray's rectangular normal form without changing its field-extension
   degree. No theorem transports the GGV corner/admissible-chain data through
   this second normalization. The GGV data are therefore not an input to the
   sheet construction as currently written.
3. A Sigray-normalized counterexample has pole/tree data and, after the
   promoted repair of Sigray's unproved Proposition 5.8 (modulo the
   review-identified one-line patch recorded in T7), a finite **entry menu**
   at each fixed topological degree. This is the strongest general finite
   reduction presently justified.
4. The passage from an entry menu to a complete **full-configuration** book
   is not general. In the all-\(b=1\) sector, `MP` plus the reviewed depth
   theorem does assert a conditional landing of every configuration at a
   marked first jump/root event in a finite local `BOOK(s,td)`. That is a
   genuine local landing theorem. It does not classify every downstream
   all-\(\mu\ge2\) / \(M\ge2\) continuation needed to treat the record as a
   complete configuration. The implementation also skips every off-axis
   entry, and the generic off-axis audit expressly reports that no
   completeness certificate exists for any \(b\ge2\) entry. Only bounded or
   specially hand-classified sectors have been concretely enumerated.
5. No theorem bounds the topological degree of a counterexample above. A
   run over \(td=6,\ldots,14\) therefore cannot be an end-to-end reduction of
   JC2 even if every one of those books were complete.

Thus the correct campaign-level conclusion is:

> **There is no unconditional theorem sending an arbitrary planar Keller
> counterexample to a configuration in a currently enumerated book
> \(B(td,\mathrm{entry})\).** The repository proves or promotes several
> valuable necessary-data reductions, but the universal book-landing link is
> missing.

The rest of this document states the attempted chain theorem by theorem,
records every external dependency used by it, and separates gaps from claims
that are actually false.

---

## 0. Conventions and status language

Work over \(\mathbf C\). Write \(F=(f,g):\mathbf A^2\to\mathbf A^2\), with
\(J(f,g)=1\). A **counterexample** means that \(F\) is not a polynomial
automorphism. This is stronger than saying that \(f,g\) are not
*linearly* equivalent to the coordinate pair. Sigray's statements allow any
nonzero constant Jacobian. When a source linear map changes \(J=1\) to a
different nonzero constant, a target coordinate scaling restores \(J=1\)
without changing noninvertibility or \(td\).

The **topological degree** is

\[
 d=td(F)=[\mathbf C(x,y):\mathbf C(f,g)].
\]

For a dominant complex polynomial map this is also the cardinality of a
generic fiber. Source and target polynomial automorphisms preserve \(d\).

The symbols \((m,n)\) are reserved below for GGV's coprime degree-ratio
parameters. The number of pole vertices in a fixed Sigray fiber is denoted
by \(s=|T_{a,\mathrm{pole}}|\), not by \(m\).

For a Sigray-normalized pair of type \((\alpha,\beta)\), a pole entry is
written

\[
 e_i=(\Lambda_i,a_i,b_i,\nu_i),\qquad
 (D_i,D_{g,i})=a_i(\alpha,\beta),\qquad
 (\deg p_i,\deg p_{g,i})=b_i(\alpha,\beta).
\]

The full entry datum, unordered in the poles, is

\[
 E=(\alpha,\beta;s;\{e_1,\ldots,e_s\}).
\]

The campaign calls a multi-pole entry **on-axis** when every \(b_i=1\), and
**off-axis** when some \(b_i\ge2\). The entry invariant \(M_i\) is pinned to
\(b_i\) in the promoted sheet analysis.

There is no repository definition of a single object
`B(td, entry)`. Three different objects are called books:

- the single-pole TDU search classes;
- the all-\(b=1\) marked jump-cell object `BOOK(s,td)` specified in
  [SHEET6-DEPTH-REVIEW.md](SHEET6-DEPTH-REVIEW.md) §6 and implemented for
  \(6\le td\le14\) by [BOOK-ENUM.md](BOOK-ENUM.md);
- special off-axis priced-cell/route/tower censuses, most completely the
  \(td=7\) census in [BOOK-OFFAXIS.md](BOOK-OFFAXIS.md) §11a.

Until a canonical endpoint is defined, this document uses
\(B_{\rm sp}(d,E)\), \(B_{\rm on}(s,d,E)\), and
\(B_{\rm off}(s,d,E)\) for those three distinct intended objects. This is
notation for the audit, not a claim that all three objects have been
constructed.

Status labels have the following meanings:

- **UNCONDITIONAL**: the implication follows from the stated hypotheses,
  without an additional open campaign hypothesis. Its evidence tier is
  still recorded separately.
- **CONDITIONAL**: the implication needs the listed thesis reading, promoted
  replacement, route perimeter, or other unproved hypothesis.
- **NOT ESTABLISHED**: the required implication has no proof at present.
- **FALSE AS STATED**: a literal assertion has a counterexample or conflicts
  with an explicit later audit.

“Internal-promoted” is not synonymous with peer reviewed.

---

## 1. The attempted chain, T1–T10

### T1. The literal starting condition does not define a counterexample

**Proposed statement.** If \(J(f,g)=1\) and \((f,g)\) is not linearly
equivalent to \((x,y)\), then \((f,g)\) is a Keller counterexample.

**Verdict: FALSE AS STATED.** For example,

\[
  (f,g)=(x,y+x^2)
\]

has Jacobian one and is not a linear coordinate pair, but is a triangular
polynomial automorphism. Every subsequent theorem needs the exact
hypothesis

\[
  J(f,g)=1\quad\text{and}\quad (f,g)\text{ is not a polynomial automorphism}.
\]

Equivalently, the campaign may begin with the conditional assumption “JC2
is false” and choose a counterexample. Merely excluding linear equivalence is
not enough.

**Source.** Elementary; no external dependency.

---

### T2. Existence of a GGV-minimal standard pair

**Statement.** Assume JC2 is false. Define

\[
B_{\mathrm{GGV}}=\min\{\gcd(\deg P,\deg Q):(P,Q)\text{ is a counterexample}\}.
\]

Then there exists a counterexample realizing \(B_{\mathrm{GGV}}\). After a polynomial-ring
automorphism, one can choose coprime \(m,n>1\) so that the selected pair is a
minimal standard \((m,n)\)-pair, with the subrectangular/standard support
properties of GGV.

**Exact hypotheses.** Over a characteristic-zero field \(K\), take
\(P,Q\in K[x,y]\) with \([P,Q]\in K^*\). GGV Definition 4.3 requires
coprime integers \(m,n>1\) and

\[
 \frac{v_{1,1}(P)}{v_{1,1}(Q)}
 =\frac{v_{1,0}(P)}{v_{1,0}(Q)}=\frac mn,
 \qquad
 v_{1,-1}\!\left(\operatorname{en}_{1,0}(P)\right)<0.
\]

“Standard” adds
\(v_{1,-1}(\operatorname{st}_{1,0}(P))<0\). “Minimal” here means the
**global** condition

\[
 \gcd\bigl(v_{1,1}(P),v_{1,1}(Q)\bigr)=B_{\mathrm{GGV}},
\]

where the minimum is over all counterexamples, not merely the source/target
equivalence class of a given pair. The subrectangular support properties are
conclusions of the cited standardization results, not extra hidden
hypotheses.

**Source.** Guccione–Guccione–Valqui, *On the shape of possible
counterexamples to the Jacobian Conjecture*, J. Algebra 471 (2017), §4,
especially Definition 4.3, the proposition labelled `primera condicion
estandar`, the standardization proposition labelled `todos son Smp`, and
Corollary 5.21 (`B finito`) in the arXiv source. Repo map:
[SECTION4-AUTOMATION.md](SECTION4-AUTOMATION.md) §§0–2.

**Verdict: UNCONDITIONAL, but existential.** It proves

\[
  \text{a counterexample exists}\Longrightarrow
  \text{a GGV-minimal standard counterexample exists}.
\]

It does **not** prove that every given counterexample is itself minimal or
that it can be made minimal inside its source/target automorphism class. In
particular, the topological degree of the newly selected global-minimal pair
need not equal the degree of the arbitrary counterexample with which one
started.

---

### T3. GGV polygon constraints

**Statement actually available.** A standard minimal \((m,n)\)-pair has the
starting-corner, regular-corner, lower-side, and admissible-chain restrictions
proved in the GGV papers. Under additional numerical bounds, the GGV
algorithms enumerate possible corner families. In the special residual case
\((A_0,m,n)=((8,28),3,2)\), arXiv:2204.14178 Proposition 4.3 produces two
explicit Laurent-polynomial polygon systems with bracket \([P,Q]=x^2\).

**Exact hypotheses and scope.**

- The general lower-side results assume a **standard minimal** pair, and the
  pinned GGV2 text also assumes \(P(0,0)Q(0,0)\ne0\) where stated.
- GGV5's family lists are bounded enumerations, not a list of all possible
  counterexamples at arbitrary degree.
- The 2022 theorem says that a counterexample either has
  \(\max(\deg P,\deg Q)\ge125\) or has degree pair \((72,108)\) or its
  transpose. This is a lower-bound dichotomy, not an upper bound.
- Proposition 4.3 assumes the particular \((8,28)\) family. Its conclusion
  is not a Keller pair: the final map
  \(x\mapsto x^{-1},\ y\mapsto x^j y\) is not in
  \(\operatorname{Aut}\mathbf C[x,y]\), and changes the bracket to a power
  of \(x\); see [SECTION4-AUTOMATION.md](SECTION4-AUTOMATION.md) §1 and §3.

**Sources.** GGV1 (published); the pinned arXiv text 1605.09430 (GGV2);
arXiv:1708.07936 (GGV5); GGV6, *Pro Mathematica* 30 (2019), Proposition
2.5 where used; and arXiv:2204.14178, Theorem in §2 and Proposition 4.3.

**Verdict.**

- Necessary polygon restrictions for a standard minimal pair:
  **UNCONDITIONAL** within each cited theorem's hypotheses.
- An exhaustive finite GGV polygon catalog for all counterexamples:
  **NOT ESTABLISHED**.
- Proposition 4.3 as a universal reduction step: **FALSE AS STATED**. It is
  conditional on one bounded residual family and lands outside the Keller
  category used by the sheet theory.

No GGV result cited here bounds \(td(F)\), and none maps a GGV admissible
corner chain to a Sigray decorated Eggers–Wall tree.

---

### T4. Passage to Sigray normal form preserves `td`, but not the GGV frame

**Statement.** Given a counterexample \(F\), choose a representative of its
equivalence class

\[
 F^*=K\circ F\circ L,
\]

where \(K,L\) are polynomial automorphisms, for which
\((\deg f^*,\deg g^*)\) is lexicographically minimal. After a nondegenerate
linear source change, followed if necessary by a target coordinate scaling
that restores the Jacobian to one, Sigray's Lemma 2.1 gives rectangular
Newton polygons
with positive corners \((k_f,l_f)\), \((k_g,l_g)\),

\[
 \frac{k_f}{k_g}=\frac{l_f}{l_g},\qquad
 k_f<k_g,\quad l_f<l_g,
\]

and \(k_g/k_f\notin\mathbf N_{>0}\). Reducing the ratio defines a type
\((\alpha,\beta)\) with \(2\le\alpha<\beta\) and
\(\gcd(\alpha,\beta)=1\). The topological degree is unchanged.

**Exact hypotheses.** A genuine nonautomorphic pair with Jacobian in
\(\mathbf C^*\); minimization under both source and target polynomial
automorphisms; and a suitable nondegenerate linear source map as in Lemma
2.1. If the convention \(J=1\) is retained literally, include the harmless
target scaling just described.

**Sources.** Sigray thesis, Notations 2.1–2.4 and Lemma 2.1, printed pp.
7–9; [SIGRAY-AUDIT.md](SIGRAY-AUDIT.md) supplies an independent
rederivation/correction audit of §§2–5 and §6 only through Proposition 6.2
(printed pp. 7–30).

**Verdict: UNCONDITIONAL as a mathematical implication if the cited theorem
statements are accepted; evidence tier: unrefereed thesis plus published
monograph.** Polynomial automorphisms preserve the field extension and
noninvertibility. The internal audit rederives the concrete uses of
Abhyankar's Lemma 18.2 and Proposition 17.4, but Abhyankar Theorems 18.13 and
19.2 remain external inputs to Sigray Lemma 2.1; this is not a wholly internal
proof.

However, the following stronger link is **NOT ESTABLISHED**:

\[
 \text{GGV corner/admissible-chain datum of }F
 \Longrightarrow
 \text{a specified Sigray tree datum of }K\circ F\circ L.
\]

The Sigray re-normalization can destroy the GGV standard frame, and no file
proves invariance or a translation dictionary for the two data sets. One may
apply T4 to the counterexample selected in T2, preserving that selected
pair's \(td\), but then T3's polygon datum is logically unused. The honest
diagram is a fork, not a chain:

\[
\begin{array}{c}
\text{chosen counterexample}\\[-2pt]
\swarrow\hspace{45pt}\searrow\\[-2pt]
\text{GGV standard polygon frame}\qquad
\text{Sigray normalized sheet frame}.
\end{array}
\]

---

### T5. A counterexample has topological degree at least six

**Statement.** If \(F\) is a complex polynomial Keller map and
\(td(F)\le5\), then \(F\) is invertible. Hence a counterexample has
\(d=td(F)\ge6\).

**Source.** H. Żołądek, *An application of Newton–Puiseux charts to the
Jacobian problem*,
Topology 47 (2008), 431–469, Theorem 6.12; local official PDF
[refs/zoladek2008_official.pdf](refs/zoladek2008_official.pdf).

**Verdict: UNCONDITIONAL; refereed-published.** This is the clean source for
the lower bound. Sigray's thesis Theorem 9.1 claims the same conclusion, but
the campaign found its printed §9 elimination incomplete; that proof is not
used for T5.

There is no corresponding upper bound on \(d\).

---

### T6. Sigray-normalized pairs carry sheet/tree data

**Statement.** For every fiber \(R_a=f^{-1}(a)\), its branches at infinity
give a decorated Eggers–Wall tree. The pole vertices
\(T_{a,\mathrm{pole}}\), their characteristic sequences, merge vertices,
pattern polynomials, indices \(\nu_F\), multiplicities, and the decorations
used in §§5–9 are attached to the normalized Keller pair. The pole vertices
are the leaves of the relevant finite rooted subtree, and the characteristic
sequences descend to \((0,y)\).

**Exact hypotheses.** A Sigray-normalized counterexample of type
\((\alpha,\beta)\); the corrected readings of the thesis definitions and
statements used to form the tree; and, for the campaign's `MP0`–`MP1`
completeness assertions, the hypotheses listed in
[SHEET6-MULTIPOLE.md](SHEET6-MULTIPOLE.md) §§1–4.

**Sources.** Sigray thesis §§3–6 and the tree statements from §§7–9;
[SIGRAY-AUDIT.md](SIGRAY-AUDIT.md) audits only §§2–5 and §6 through
Proposition 6.2, printed pp. 7–30. In particular, Propositions 6.7–6.8 on
printed pp. 33–34 are outside that audit even though Proposition 6.8 is used
in `MP5`–`MP6` to manufacture a same-branch pole.
[SHEET6-MULTIPOLE.md](SHEET6-MULTIPOLE.md) Theorem MP, `MP0`–`MP1`,
supplies the promoted multi-pole synthesis.

**Verdict: CONDITIONAL on the corrected Sigray/MP trust perimeter.** Basic
Eggers–Wall-tree existence is standard, but the exact campaign subtree
coverage and decorations consumed by the book are not available as one
refereed theorem or one complete internal replacement. The audit stops at
Proposition 6.2; later §6 and all of §§7–9 remain outside its systematic
scope, and the thesis contains both errors and omitted proofs.

---

### T7. Pole mass gives a finite entry menu at each fixed `td`

**Statement.** For every \(a\in\mathbf C\),

\[
 d=\sum_{F\in T_{a,\mathrm{pole}}}\Lambda(F),\qquad
 \Lambda(F)=\frac{D_{g,F}\deg p_F}{\nu_F}.
\]

For a pole of a normalized pair of type \((\alpha,\beta)\), the promoted
entry calculation gives

\[
\begin{aligned}
 (D_F,D_{g,F})&=a_F(\alpha,\beta),\\
 (\deg p_F,\deg p_{g,F})&=b_F(\alpha,\beta),\\
 \Lambda(F)&=\frac{a_Fb_F\alpha\beta}{\nu_F},\\
 M_F&=b_F,
\end{aligned}
\]

with either

\[
 \nu_F\mid\alpha,\quad \nu_F\mid b_F\beta-1,
 \qquad\text{or}\qquad
 \nu_F\mid\beta,\quad \nu_F\mid b_F\alpha-1.
\]

Moreover \(\Lambda(F)\ge\beta\ge3\). Therefore, at a fixed \(d\):

- \(s\le d/3\);
- \(\beta\le d\);
- only finitely many partitions \(d=\sum_i\Lambda_i\) occur; and
- only finitely many entry data \(E\) occur.

**Exact hypotheses.** A normalized complex Keller counterexample with the
type data of Notations 2.3–2.4/Lemma 2.1/Statement 2.1; the audit-corrected
forms of Sigray Proposition 5.3, Proposition 5.4, Statements 5.1–5.2, and
Propositions 5.5–5.7; and the every-fiber mass identity. The equality
\(M_F=b_F\) specifically uses Notation 5.2, Proposition 5.1(i),(iii), the
ladder of Proposition 4.2 with \(h_0=g\), Notation 8.1, and Statement
5.2(i)/Statement 2.1. It is not a consequence of the mass formula alone.

**Sources.** Sigray thesis pp. 25–28; [SHEET6-TDUNIFORM.md](SHEET6-TDUNIFORM.md)
§§1–2, [SHEET6-AF3.md](SHEET6-AF3.md) §1, and
[SHEET6-TDU-REVIEW.md](SHEET6-TDU-REVIEW.md) §§1–3 and §6;
[SHEET6-MULTIPOLE.md](SHEET6-MULTIPOLE.md) `MP4`. Sigray prints no proof
of Proposition 5.8. Its every-fiber form is replaced by
[SOL-PROP58.md](SOL-PROP58.md), whose external input is Chau's published
Theorem 4.4 excluding a vertical exceptional component. The review identifies
one owed line not incorporated into that promoted file: before equating a
generic fiber count with \(\deg(g|_{\overline R_a})\), prove that \(g\) is
nonconstant on every component \(\Gamma\subset f^{-1}(a)\). If \(g\) were
constant on \(\Gamma\), both \(df\) and \(dg\) would annihilate
\(T\Gamma\), contradicting \(J(f,g)\ne0\). One must then avoid the finitely
many branch values as well as finite puncture values.

**Verdict.**

- The every-fiber mass identity: **UNCONDITIONAL relative to Chau's
  published theorem and the one-line repair written above**. At the artifact
  level, `SOL-PROP58.md` remains stale: its header says all review patches
  are incorporated although N2 is absent from its body. This master document
  supplies that missing micro-step; the status drift must still be fixed in
  the promoted source before external publication.
- The complete entry parameterization and \(M=b\) pin:
  **CONDITIONAL on the corrected Sigray/TDU/MP package**.
- Finiteness of the entry menu once those formulas hold: **UNCONDITIONAL**
  elementary arithmetic.

This theorem produces a finite **entry list**, not a finite list of complete
characteristic-sequence configurations.

---

### T8. Tree calculus produces a case split, not yet a complete book

**Statement available in the promoted perimeter.** Let
\(s=|T_{a,\mathrm{pole}}|\).

1. The relevant pole/characteristic subtree has \(s\) leaves and at most
   \(s-1\) merges (`MP0`–`MP1`).
2. On an all-\(b=1\) ancestry, \(M=1\) propagates along merge-free segments,
   and the first event that breaks \(M=1\) has the resonant jump anatomy of
   `MP5`–`MP7`.
3. The invariant \(w=(\bar\kappa-\rho)/\nu\) has a finite closure on pure
   \(M=1\) segments. Thus, for a fixed on-axis entry, the local menu for a
   marked first jump/root event is finite up to menu equivalence.

**Exact hypothesis/trust crosswalk.** In addition to T6–T7 and the
all-\(b_i=1\) entry hypothesis, Theorem MP and the depth theorem consume:

- `P1`: Proposition 8.3's hypothesis under the promoted reading that its
  printed typo means Notation 9.2 regularity;
- `P2`: the exact root/order and eta/residue laws derived from the printed
  identity in Proposition 8.1(iv);
- `P3`: the \(y\)-side convention that Proposition 9.2 characteristic
  sequences terminate at \((0,y)\), with the \((0,x)\) placement used in
  Statement 9.4;
- `P4`: the entry pin—Notation 5.2, Proposition 5.1(i),(iii), Proposition
  4.2 with \(h_0=g\), Notation 8.1, Statement 5.2(i), and Statement 2.1;
- the corrected continuation/tree inputs Statements 3.9, 3.17(i), 3.18,
  Proposition 6.2, and the unaudited Proposition 6.8 used to manufacture a
  same-branch pole; and
- `H1`: Proposition 9.3(a)–(d) for MP9's root-residual clause, enlarged to
  Proposition 9.3(a)–(m) for the depth theorem's chain, jump, and root
  layers.

The depth theorem expressly says that its local landing result does not use
the separate E9/H2 mid-segment branch reading.

**Sources.** [SHEET6-MULTIPOLE.md](SHEET6-MULTIPOLE.md) Theorem MP;
[SHEET6-MP-REVIEW.md](SHEET6-MP-REVIEW.md) §5;
[SHEET6-DEPTH.md](SHEET6-DEPTH.md) §§2–9; and
[SHEET6-DEPTH-REVIEW.md](SHEET6-DEPTH-REVIEW.md) §§4–7. The corrected depth
metadata are \(d_0\le2\,\mathrm{gen}(W)+2\), although the body of
`SHEET6-DEPTH.md` §8 still prints the stale \(\mathrm{gen}(W)+2\).

**Verdict: CONDITIONAL, and local rather than full-configurational.**
`SHEET6-DEPTH.md` §8 explicitly states the named **finite jump-vertex book**
theorem for every fixed \((s,d)\), and `SHEET6-DEPTH-REVIEW.md` §6 gives its
finite E/T/C′/J′/R/S specification. Within the exact perimeter above, it
asserts that every all-\(b=1\) configuration lands at its marked first
jump/root event in that finite local book. The same files expressly leave
out of a full downstream configuration:

- downstream merges all of whose arrivals have \(\mu_e\ge2\);
- a first resonant jump followed by an \(M\ge2\) chain and a later merge;
- general \(M\ge2\) suffix chains; and
- absolute polynomial realizability.

See [SHEET6-MULTIPOLE.md](SHEET6-MULTIPOLE.md) §4,
[SHEET6-DEPTH.md](SHEET6-DEPTH.md) §9,
[BOOK-BASH-R2.md](BOOK-BASH-R2.md) §6, and
[TEMPLATE-ATTACK.md](TEMPLATE-ATTACK.md) §§1c and 6. Consequently, “every
\((s,d)\) reduces to a finite book” is a promoted conditional theorem when
“book” means the local marked-event object. It is **not established** when
“book” means an exhaustive set of complete configurations.

The named theorem also does not supply a typed configuration-to-record map,
a fail-closed coverage certificate, or a record of every unused branch and
downstream context. Those are specification/provenance gaps, not grounds for
denying the local landing theorem it actually states.

---

### T9. Sector-by-sector landing

This is where the universal chain breaks.

#### T9(a). Single pole, `s=1`

The entry formulas of T7 are finite for fixed \(d\). If \(d\) is prime,
[SHEET6-TDUNIFORM.md](SHEET6-TDUNIFORM.md) §2 proves that every row has
\(b=1\), and the single-pole Proposition 8.4 mechanism excludes it.

**Exact hypotheses.** Besides T4 and T7, the prime kill assumes \(s=1\),
\(d\) prime, the `P4` entry pin expanded in T8, and Proposition 8.4. To meet
Proposition 8.4's hypothesis \(F\in T_a^\searrow\cap V_a\), the promoted
argument also consumes Notation 6.1/Statement 6.1, the pole-to-
\(\searrow\) glue in `SHEET6-A3L1-REVIEW.md` §1, and Statement 3.16. These
items were omitted from the older TDU perimeter list and are restored here.

**Verdict.** Prime \(d\), single pole: **CONDITIONAL theorem on the exact
thesis/promoted perimeter just stated**. Composite \(d\): **no complete
landing or exclusion**.
The TDU breadth-first searches leave surviving classes at every composite
\(d=6,8,9,10,12,14,15,16\). Depth frontiers are hit at \(d=12,15,16\).
At \(d=14\) the depth frontier is zero, but two solver kinds remain `OPEN`;
the reported 48 classes are still not a completeness certificate. The TDU
audit treats the \(d\ge12\) survivor totals as lower bounds and states that
there is no finite residual list uniform in \(d\).

#### T9(b). Multi-pole, all `b_i=1`

T8 supplies, under its explicitly expanded P1–P4/H1 perimeter, conditional
landing of every all-\(b_i=1\) configuration at a marked first jump/root
event in a finite local book for each fixed \((s,d)\). The implementation in
[cases/book_enum.py](cases/book_enum.py) enumerates conservative cells only
for

\[
  6\le d\le14,\qquad 2\le s\le\lfloor d/3\rfloor.
\]

It is not a full-configuration compiler: post-jump mixed/two-jump contexts
are quarantined. Nor does it preserve complete per-entry provenance: cells
are aggregated over contexts and only a bounded prefix of entry tags is
written to survivor records.

**Verdict.** Landing in the abstract on-axis marked-event book is a
**CONDITIONAL theorem under T8's exact perimeter for every fixed \(d\)**.
Landing in the implemented on-axis artifact is available only for
\(6\le d\le14\). Coverage of every on-axis **complete downstream
configuration** is **NOT ESTABLISHED**, especially for \(s\ge3\).

#### T9(c). Multi-pole, some `b_i>=2`

`cases/book_enum.py` explicitly increments `entries_offaxis` and executes
`continue`; no cell is generated for such an entry. The later off-axis work
finds that at a fixed printed budget the post-jump state set has unbounded
numerator and \(M\), while the grid loop bounds scale with those quantities.
[BOOK-OFFAXIS.md](BOOK-OFFAXIS.md) §10 P5 therefore records:

\[
  0\ \mathrm{DEAD}/0\ \mathrm{ALIVE}/2691\ \mathrm{OPEN}
\]

and says that no completeness certificate exists for any \(b\ge2\) entry at
any \(d\).

The \(d=7\) §11a census is a special cap-free inversion producing 17 cells,
and [TOWER-UNIFORM.md](TOWER-UNIFORM.md) kills all 17. But that theorem is
expressly over the **filed route perimeter**: a route outside the filed
closure is classified as under-enumeration, not silently covered. At
\(d=11\), an attempted program artifact constructs and stamps 159 diagnostic
rows, but [TOWER-TD11.md](TOWER-TD11.md) §10 and
`xmodel/sol-census-review.md` find no certified complete census; the latter
classifies the attempted universal certificate as broken. The \(d=13\)
sector is open (§13).

**Verdict.** A general off-axis book-landing theorem is
**NOT ESTABLISHED**. The \(d=7\) endpoint is **CONDITIONAL on the filed
route/classification perimeter**, notwithstanding the cap-free arithmetic
inside that perimeter.

---

### T10. Landing in an enumerated `B(td,entry)`

**Desired statement.** Every Keller counterexample has a normalized sheet
configuration which occurs in an enumerated object \(B(d,E)\).

**Verdict: NOT ESTABLISHED.** No such \(B(d,E)\) is defined, and the sector
objects do not cover all possibilities:

- single-pole composite configurations are not exhausted;
- general off-axis configurations are not enumerated;
- post-jump mixed configurations are omitted even from the strongest reading
  of the all-\(b=1\) full-configuration claim;
- actual on-axis enumeration stops at \(d=14\); and
- no theorem bounds \(d\) above.

The strongest honest end-to-end statement presently available is the
following disjunction.

> **Maximal current reduction (conditional sheet perimeter).** Assume JC2 is
> false. One may select a GGV-minimal standard counterexample. Independently,
> one may choose a Sigray-normalized representative of that selected pair;
> its topological degree \(d\) is unchanged and \(d\ge6\). For every fixed
> fiber it has a finite entry datum \(E\) satisfying T7. If it has one pole
> and \(d\) is prime, the promoted single-pole theorem excludes it. If it is
> multi-pole and all \(b_i=1\), its pure \(M=1\) ancestry has a finite local
> marked-jump menu. In every other case—composite single-pole, off-axis, or
> post-jump mixed continuation—the current reduction stops before an
> exhaustive enumerated book.

This statement does not use the GGV polygon restrictions after selecting the
counterexample. That redundancy is evidence that the purported GGV-to-sheet
link has not been supplied.

---

## 2. Dependency ledger

The requested classifications are used literally where justified. Abhyankar
is a published monograph/lecture-note source whose journal-referee status was
not established; it is labelled that way rather than inaccurately forced into
“refereed-published.”

### 2.1 Externally published statements

| ID | Statement actually consumed | Classification | Exact role in the chain | Campaign replacement / caveat |
|---|---|---|---|---|
| **GGV1** | J. A. Guccione, J. J. Guccione, C. Valqui, “On the shape of possible counterexamples to the Jacobian Conjecture,” *J. Algebra* 471 (2017), 13–74, [DOI 10.1016/j.jalgebra.2016.08.039](https://doi.org/10.1016/j.jalgebra.2016.08.039): §4 minimal pair and standard \((m,n)\)-pair; the standardization propositions; Cor. 5.21; later regular-corner restrictions. | **refereed-published** | T2, and the published part of T3. It proves existence of a globally minimal standard representative if JC2 is false. | No replacement needed. The quantifier is existential over all counterexamples. `/tmp/jcrefs/1401.1784.tex` was an ephemeral local audit copy, not a banked repository source; publication metadata are above. |
| **GGV6** | J. A. Guccione, J. J. Guccione, R. Horruitiner, C. Valqui, “The Jacobian Conjecture: Approximate roots and intersection numbers,” *Pro Mathematica* 30(60) (2019), 51–89, [publisher page](https://revistas.pucp.edu.pe/index.php/promathematica/article/view/21094), Prop. 2.5. Under its displayed homogeneous-bracket hypotheses with normalized corner \((a/l,2)\), it gives the arithmetic predecessor criterion that reduces the \((8,28)\) predecessor directions to \((1,-2)\) and \((1,-3)\). | **refereed-published**; the journal's [official policy](https://revistas.pucp.edu.pe/index.php/promathematica/about/submissions) states that articles undergo arbitration/evaluation. | A subsidiary input to the special GGV22 Proposition 4.3 branch, not to the sheet/book branch. | No internal replacement. It inherits the same bounded-family limitation as Proposition 4.3. |
| **Chau99** | N. V. Chau, “Non-zero constant Jacobian polynomial maps of \(\mathbf C^2\),” *Ann. Polon. Math.* 71 (1999), 287–310, [DOI 10.4064/ap-71-3-287-310](https://doi.org/10.4064/ap-71-3-287-310), Theorem 4.4(E1), printed pp. 304–305; local text [refs/chau1999_apm71_full.pdf](refs/chau1999_apm71_full.pdf). For a nonzero constant-Jacobian pair monic in the required variable, the fiber-deficit set is a finite union of polynomially parametrized curves whose component degree ratio is \(\deg f/\deg g>0\), excluding a vertical-line component. Generic linear source change and target scalings supply the monicity used by the internal proof. | **refereed-published** | The sole **cited Keller-specific** external input in the promoted every-fiber repair of Sigray Proposition 5.8, T7. Standard resolution/intersection inputs are separately disclosed in §2.5. | Consumed, not replaced. [SOL-PROP58.md](SOL-PROP58.md) §§6–7 uses this to remove the fiber defect, with the N2 micro-step supplied in T7 above. It does **not** repair any later book-completeness issue. |
| **Ż08** | H. Żołądek, “An application of Newton–Puiseux charts to the Jacobian problem,” *Topology* 47 (2008), 431–469, [DOI 10.1016/j.top.2008.04.001](https://doi.org/10.1016/j.top.2008.04.001), Theorem 6.12: a Jacobian map of topological degree at most five is invertible; local official text [refs/zoladek2008_official.pdf](refs/zoladek2008_official.pdf). | **refereed-published** | T5, hence \(d\ge6\). | This published theorem replaces the campaign's need to trust Sigray Theorem 9.1. The chain cites Theorem 6.12 at statement level as an external black box and makes no independent validation claim. |
| **Abh77** | S. S. Abhyankar, *Lectures on Expansion Techniques in Algebraic Geometry*, TIFR Lectures on Mathematics and Physics 57, 1977, [official TIFR catalogue](https://mathweb.tifr.res.in/lectures.html), especially Prop. 17.4 and Thms. 18.13, 19.2 as cited in Sigray Lemma 2.1. | **published monograph / lecture notes** | External foundation for the rectangular normal form in T4. | [SIGRAY-AUDIT.md](SIGRAY-AUDIT.md) rederives the concrete Lemma 18.2/Prop. 17.4 uses, but leaves Thms. 18.13 and 19.2 as load-bearing external inputs; there is no promoted replacement for those two theorems. |

The GGV1 proof also cites van den Essen's book, Corollary 10.2.21, for the
subrectangular form, and Makar-Limanov for a standard support adjustment.
Those are transitive dependencies inside a refereed theorem, not separately
imported campaign lemmas. A public proof that unfolds GGV1 rather than citing
it as a black box should add them to its own detailed ledger.

### 2.2 Preprints and exact-version hazards

| ID | Statement actually consumed or invoked | Classification | Load-bearing? | Replacement status |
|---|---|---|---|---|
| **GGV2-pinned** | Guccione–Guccione–Valqui, arXiv:1605.09430v2, “The two-dimensional Jacobian conjecture and the lower side of the Newton polygon.” For a direction between \((0,-1)\) and \((1,-1)\), nonmonomial homogeneous \(R\), homogeneous \(G\), \([G,R]=R^i\), and positive directional value, Prop. 3.12 gives the three finite factor/predecessor alternatives used by the \((8,28)\) proof; the paper's lower-side/admissible-chain results assume a standard minimal pair. | **preprint (exact consumed version)** | Load-bearing only if T3 is stated with the lower-side/admissible-chain detail or the bounded Proposition 4.3 derivation. It is not needed for the sheet entry reduction. | A journal successor, “The lower side of the Newton polygon of hypothetical counterexamples to the plane Jacobian conjecture,” appeared online in *Quaestiones Mathematicae* on 2026-07-28, [DOI 10.2989/16073606.2026.2701437](https://doi.org/10.2989/16073606.2026.2701437). The campaign has not diffed that revised-title publication against pinned arXiv v2. Until equivalence is checked, classify the proposition text actually consumed as **preprint**, not retroactively as the journal article. |
| **GGV3** | Guccione–Guccione–Valqui, arXiv:1406.0886v3, “A system of polynomial equations related to the Jacobian Conjecture.” Theorem 1.9/Corollary 1.12, over a characteristic-zero domain/algebraic closure, give an equivalence between failure of JC and existence of Laurent-series data solving their canonical system for integers \(m,n\) with neither dividing the other. | **preprint** | Contextual for the polynomial-system lane; not load-bearing in JC2 \(\to\) sheet entries or books, and not used in the polygon statement of Proposition 4.3. | No promoted general replacement. The repo's bracket systems and audits check particular constructions/cases, not this paper's global equivalence. |
| **GGV5** | Guccione–Guccione–Horruitiner–Valqui, arXiv:1708.07936v1, “Some algorithms related to the Jacobian Conjecture.” Assuming JC false and a GGV1 standard minimal pair, Theorem 2.20 attaches a finite complete chain satisfying its fourteen conditions; Algorithm 8 outputs all admissible complete chains under an input bound on \(v_{1,1}(A_0)\). The reported run yields the bounded tables used for the \(\max(\deg P,\deg Q)\le150\) farm. | **preprint** | Load-bearing for any assertion that the farm exhausts GGV families under that stated degree cutoff; not load-bearing for T4–T9 and not an all-degree list. | [SECTION4-AUTOMATION.md](SECTION4-AUTOMATION.md) and code reproduce bounded tables/reductions, but do not replace the mathematical enumeration theorem for arbitrary input bounds. |
| **GGV22** | Guccione–Guccione–Horruitiner–Valqui, arXiv:2204.14178v1, “Increasing the degree of a possible counterexample to the Jacobian Conjecture from 100 to 108”: §2 degree dichotomy and Proposition 4.3 for \((A_0,m,n)=((8,28),3,2)\). | **preprint** | Load-bearing only for the repo's \((72,108)\) polygon claim. It is **not** load-bearing in the sheet/book reduction and cannot be used globally. | [CROSSCHECK.md](CROSSCHECK.md) validates independent transcriptions; [AUDIT.md](AUDIT.md) audits the downstream systems; neither proves Proposition 4.3's exhaustiveness. No promoted mathematical replacement exists. |

For precision, GGV22 Proposition 4.3 concludes that in that one family there
are \(P,Q\in L^{(1)}\) with \([P,Q]=x^2\) and either

\[
\begin{aligned}
N(P)&=\{(0,0),(1,0),(8,14),(8,16),(0,8)\},\\
N(Q)&=\{(0,0),(2,1),(12,21),(12,24),(0,12)\},
\end{aligned}
\]

or the same two sets with \((0,8)\) and \((0,12)\), respectively, removed.
This exact conclusion is why the proposition cannot be substituted for a
constant-Jacobian sheet-normalization theorem.

The 2013 Guccione–Guccione–Valqui article “A differential equation for
polynomials related to the Jacobian conjecture,” *Pro Mathematica* 27,
83–98, is **refereed-published/contextual** here under the same journal
[arbitration policy](https://revistas.pucp.edu.pe/index.php/promathematica/about/submissions).
GGV22 invokes it in its
broader bounded-degree elimination history, but no statement from it is a
book-landing link in T4–T10.

No statement from GGV3, GGV5, or GGV22 turns the bounded GGV family lane
into an upper bound on polynomial degree or topological degree. Their presence
in a dependency graph must not be read that way.

### 2.3 Sigray thesis statements

I. Sigray, *Jacobian trees and their applications*, ELTE PhD thesis (2008),
[official ELTE record](https://edit.elte.hu/xmlui/handle/10831/45438), is an
**unrefereed thesis**. The local source is
[refs/sigray_full.pdf](refs/sigray_full.pdf). The relevant statements and
their replacement status are:

| Thesis item | Use in the chain | Classification | Audit / replacement status |
|---|---|---|---|
| Not. 2.1; Lem. 2.1; Not. 2.3–2.4; St. 2.1, pp. 7–9 | Polynomial equivalence, rectangular normal form, global type \((\alpha,\beta)\). | **thesis-page** | Audited in [SIGRAY-AUDIT.md](SIGRAY-AUDIT.md); verified or verified-with-nit, with the concrete argument rederived. Still depends on the cited Abhyankar input at its broadest formulation. |
| Definitions/Notations and Statements 3.1–3.18; Prop. 3.1–3.2, pp. 10–18 | Eggers–Wall vertices, \(\pi,\kappa,\nu\), pattern roots, continuation, characteristic descent, degree transport. | **thesis-page** | The audit found multiple errata. Not. 3.5 is ill-defined under the printed P-presentation; St. 3.8 is false under that reading. The Q/jump/max reading is forced and internally proved in `xmodel/sol-h5a.md`, reviewed in `xmodel/grok-h5a-review.md`, and promoted in [AUDIT.md](AUDIT.md) §H5a. St. 3.18 needs the repaired conclusion \(F*(\varepsilon c)\). St. 3.14 retains a cross-fiber conjugation-twist gap. |
| Props. 4.1–4.6, pp. 19–23 | Approximate-root comparisons and the ladder later used by tower kills. | **thesis-page** | Prop. 4.2 has a genuine constant-leading-part gap in [SIGRAY-AUDIT.md](SIGRAY-AUDIT.md); there is no general promoted replacement. Particular tower uses claim to avoid the bad corner, so those uses are conditional on that guard. |
| Prop. 5.1; Not. 5.1–5.3; St. 5.1–5.2; Props. 5.2–5.7, pp. 23–28 | Pole status, ratios, \(\nu\)-menu, \(\Lambda\), lower bound, and the entry formulas. | **thesis-page** | Prop. 5.1's printed proof has a finite-nonzero-asymptotic gap; pole-only uses with \(g(P)=\infty\) avoid it. Prop. 5.3(ii),(viii) print inverted ratios and are internally corrected. Prop. 5.4 omits its q-half; [SIGRAY-AUDIT.md](SIGRAY-AUDIT.md) supplies a repair. Props. 5.5–5.7 are used only with the audit's corrections. |
| Prop. 5.8, p. 28 | \(d=\sum\Lambda\) on **every** fiber. | **thesis-page; printed proof absent** | Replaced mathematically by [SOL-PROP58.md](SOL-PROP58.md), [SOL-PROP58-REVIEW.md](SOL-PROP58-REVIEW.md), Chau Theorem 4.4, and the N2 micro-step written in T7. The promoted source file's header says its review patches are incorporated, but N2 and several wording/link patches remain stale in its body. This replacement repairs only the mass/entry layer. |
| Props./Statements 6.1–6.2, pp. 28–30 | Initial tree order/root comparisons and degree laws. | **thesis-page** | Included in the 72-item audit. St. 6.2 needs an omitted \(H\in T_a^+\) hypothesis; concrete consumers must show it. Prop. 6.2 prints an F/G hypothesis swap, repaired in the audit. |
| Remaining §6, Props./Statements 6.3–6.8, pp. 31–34, especially Props. 6.7–6.8 | Later root/branch comparisons and manufacture of same-branch pole ancestors. | **thesis-page** | **Outside the systematic audit.** Proposition 6.8 is nevertheless load-bearing in `SHEET6-MULTIPOLE.md`'s MP5–MP6 tree-coverage argument. No standalone promoted replacement exists. |
| Not./St./Props. of §7, especially St. 7.1–7.3, Prop. 7.2, Prop. 7.5 (22), Cor. 7.1 | Critical-value vertices, Euler equality, and budget accounting. | **thesis-page** | Not covered by the 72-item audit of §§2–5 and §6 through Proposition 6.2. Imported in the MP/book trust perimeter; no single standalone promoted replacement. |
| Not. 8.1; St. 8.1–8.5; Props. 8.1–8.4; Cor. 8.1, pp. 39–45 | Pattern identity, entry \(M\), multiplicity divisibility, \(M=1\) propagation and single-pole kill. | **thesis-page** | Re-used and partially rederived in the promoted MP/TDU documents, but not independently replaced as a complete theorem package. These are load-bearing for T7–T9. |
| Table (23); Not. 9.1–9.3; St. 9.1–9.6; Props. 9.1–9.3, pp. 46–52 | Entry seeds, characteristic sequences, cases I–IV, charges, shared budget, and step arithmetic. | **thesis-page** | §§7–9 have no comprehensive audit. Prop. 9.3 requires the E5 repair; St. 9.3(24) requires the E6 sign repair. [SHEET6-CAMPAIGN.md](SHEET6-CAMPAIGN.md) and satellites rederive particular clauses and exhibit false printed case eliminations, but do not replace all of §§7–9. |
| Thm. 9.1, p. 60 | Claimed \(d\ge6\). | **thesis-page; incomplete proof** | Not used. Replaced for the conclusion by refereed-published Żołądek Theorem 6.12. |

The compact current trust-set declaration is
[paper2/main.tex](paper2/main.tex) §“The trust set and the errata ledger”:
Prop. 4.2; Prop. 8.1(i)–(v); Cor. 6.1; St. 8.3(i) with Not. 4.1;
St. 3.9/3.17(i)/3.11(i); St. 8.4; St. 8.5 and St. 3.18;
Props. 5.7/5.8; Prop. 9.3 with E5; and St. 9.3(24)/9.4 with E6. That file
correctly says every obstruction theorem there is conditional on this set.

### 2.4 Internal-promoted statements

These are proofs or syntheses produced inside the campaign. They are not
external citations and have not undergone journal peer review, but they are
part of the chain's actual proof surface.

| Internal source | Replaces or proves | Remaining perimeter |
|---|---|---|
| [SIGRAY-AUDIT.md](SIGRAY-AUDIT.md) | A statement-by-statement audit of 72 items in §§2–5 and §6 through Proposition 6.2, thesis pp. 7–30: 21 verified, 33 verified-with-nit, 9 new errata, 2 known errata, 7 gaps; supplies several corrected derivations. | It does not cover Propositions 6.3–6.8 or §§7–9. Prop. 4.2, St. 3.14, and guarded Prop. 5.1 issues remain as stated. |
| `xmodel/sol-h5a.md`, `xmodel/grok-h5a-review.md`, [AUDIT.md](AUDIT.md) §H5a | Forces the Q/jump/max interpretation of \(\kappa_F\) and repairs the H5a coherence problem; E5 is then applied. | The equal-index assertion \(U_{7C}\) is a separate conjecture, though the 17-cell \(td=7\) tower result does not need it. |
| [SOL-PROP58.md](SOL-PROP58.md), [SOL-PROP58-REVIEW.md](SOL-PROP58-REVIEW.md) | Replaces the missing proof of Sigray Prop. 5.8 at every-fiber strength, completed in this master by T7's one-line N2 repair. | Imports Chau Theorem 4.4 and standard surface foundations. The source header overstates patch incorporation: N2 and the review's N1/N3/N4 wording/link cleanups remain stale. It explicitly does not repair off-axis, merge, suffix, or book completeness. |
| [SHEET6-TDUNIFORM.md](SHEET6-TDUNIFORM.md), [SHEET6-TDU-REVIEW.md](SHEET6-TDU-REVIEW.md) | Closed-form single-pole entry table, \(M=b\), and the prime-\(d\) single-pole theorem. | Composite single-pole searches survive; no uniform finite residual; exact corrected thesis/promoted perimeter is expanded in T7–T9. |
| [SHEET6-MULTIPOLE.md](SHEET6-MULTIPOLE.md), [SHEET6-MP-REVIEW.md](SHEET6-MP-REVIEW.md) | `MP0`–`MP9`: finite merge topology, entry pin, pure \(M=1\) anatomy, resonant first-jump calculus. | All-\(\mu\ge2\) mixed merges, post-jump \(M\ge2\) chains, general reachability, and coefficients remain. Its local marked-event landing theorem survives; only a **full-configuration** reading is broader than this perimeter. |
| [SHEET6-DEPTH.md](SHEET6-DEPTH.md), [SHEET6-DEPTH-REVIEW.md](SHEET6-DEPTH-REVIEW.md) | Finite \(w\)-alphabet and depth-invariant local jump menu on the \(M=1\) axis. | Does not prove a finite full-configuration book off the axis or after a jump. Correct safe depth metadata are \(2\,\mathrm{gen}(W)+2\). |
| [BOOK-ENUM.md](BOOK-ENUM.md), `cases/book_enum.py` | Concrete on-axis local-cell enumeration for \(6\le d\le14\). | Explicitly skips off-axis entries; does not cover all downstream mixed contexts; conservative cell aggregation is not a per-entry coverage certificate. |
| [BOOK-OFFAXIS.md](BOOK-OFFAXIS.md) | Off-axis entry census and partial chain/price laws; special \(d=7\) classification. | Its §10 P5 says the generic grid has no completeness certificate. Earlier contradictory sections are superseded. |
| [TOWER-UNIFORM.md](TOWER-UNIFORM.md) | Kills all 17 cells in the promoted \(d=7\) special route book. | Conditional on the Sigray trust set and filed route perimeter; not a universal off-axis landing theorem. |
| [TOWER-TD11.md](TOWER-TD11.md), `cases/td11_census.py`, `xmodel/sol-census-review.md` | Entry-clash theorem and an attempted 159-row diagnostic census at an exact-core tier. | No certified complete \(d=11\) census exists; the review finds the universal seven-class certificate broken, and beyond-core, nested, and multi-word sectors remain open. |

### 2.5 Uncited foundational inputs

Two standard mathematical packages are used without a precise source or a
full internal proof. They cannot honestly be assigned one of the four
requested evidence labels; the missing citations are themselves ledger
items.

| Input | Exact use | Classification | Replacement status |
|---|---|---|---|
| Resolution of indeterminacy for a rational map from a smooth projective surface, together with normalization, divisor intersection, push-pull/projection, and finite-flat degree facts | [SOL-PROP58.md](SOL-PROP58.md) §2 resolves \(\mathbf P^2\dashrightarrow\mathbf P^1\times\mathbf P^1\), decomposes horizontal and vertical boundary divisors, and turns intersection degree into the generic sheet number. | **uncited standard foundation; not independently audited** | No promoted replacement or exact bibliographic citation. Chau is the sole cited **Keller-specific** input, not the sole external mathematical fact in the proof. |
| Newton–Puiseux existence/termination and the basic finiteness of the Eggers–Wall tree attached to the branches at infinity | T6's underlying finite tree before the Sigray-specific decorations and transition formulas are imposed. | **uncited standard foundation / thesis-mediated** | No separate source or complete internal proof is identified. The Sigray thesis defines and uses the object, while the campaign audits only its listed statements through Proposition 6.2. |

---

## 3. Gap list, ranked by severity

### CRITICAL 1 — the starting predicate is wrong

The literal condition “\(J(f,g)=1\), not both linear-equivalent to
coordinates” admits nonlinear polynomial automorphisms. It cannot start a
counterexample reduction. Replace it everywhere by “\(F\) is not a
polynomial automorphism.” This is not a proof gap; it is a false hypothesis
translation.

### CRITICAL 2 — “every counterexample has GGV-minimal data” has the wrong quantifier

GGV minimizes \(\gcd(\deg P,\deg Q)\) over the set of **all**
counterexamples and selects a pair attaining that global minimum. It does not
make an arbitrary counterexample minimal. A proof by contradiction may work
with the selected pair, but the theorem must say

\[
  \exists\text{ counterexample}\Longrightarrow
  \exists\text{ GGV-minimal standard counterexample},
\]

not “every counterexample carries the selected minimal-pair data.” No
argument relates the selected pair's \(td\) to that of an arbitrary original
pair.

### CRITICAL 3 — the GGV-to-sheet arrow is absent and the reduced GGV object is often ill-typed

There is no theorem translating GGV corners/admissible chains into Sigray
pole/tree decorations. The early GGV standardization is a polynomial-ring
automorphism and preserves a Keller pair, but the per-family §4 reductions
used by the farm pass through Laurent automorphisms and finish with a map not
in \(\operatorname{Aut}\mathbf C[x,y]\). Proposition 4.3 lands at
\([P,Q]=x^2\), whereas Sigray assumes a constant-Jacobian polynomial pair.

One can re-normalize the selected counterexample independently in Sigray's
sense, but then the GGV data are discarded. Calling this a sequential
reduction is mathematically misleading.

### CRITICAL 4 — no canonical book object and no book-landing theorem

`B(td,entry)` does not occur as a defined object in the repository.
`BOOK(s,td)` variously denotes a local jump-cell menu, an aggregate of cells
over entry contexts, or an alleged set of full configurations. Those readings
have different completeness obligations.

A usable endpoint requires all of the following, none of which is presently
stated in one theorem:

1. a precise object \(B(d,E)\);
2. a deterministic map from every normalized sheet configuration to a book
   record;
3. proof that the map terminates and is total;
4. preservation of the branch, entry, and downstream context required by
   every cell kill; and
5. a fail-closed coverage certificate showing that no transition was skipped.

The natural first repair is a **marked-first-event landing theorem**: select
the earliest resonant/\(M\ne1\) event, include its complete pole-side
subtree, and explicitly type the unused branches and downstream continuation.

### CRITICAL 5 — the off-axis sector has no completeness theorem

[BOOK-OFFAXIS.md](BOOK-OFFAXIS.md) §10 P5 is explicit: for any
\(b\ge2\) entry, the generic grid loop has no completeness certificate. At a
fixed budget, reachable states can have unbounded numerator and \(M\), and
the solver's proved bounds scale with them. The reported 2691 generic cells
are therefore all `OPEN`; they are not an exhaustive book whose survivors
have merely not yet been killed.

This gap already occurs at two poles. The older parenthetical claim that a
mixed all-\(\mu_e\ge2\) merge requires \(s\ge3\) is **false**:
[BOOK-OFFAXIS.md](BOOK-OFFAXIS.md) §3 exhibits \(s=2\) entries with both
\(b_i\ge2\) and both arrivals of multiplicity two.

The \(d=7\) inversion is special. It is cap-free inside its hand-proved
classification, but the final tower theorem still declares the filed route
perimeter as a hypothesis. There is no analogous completed census at
\(d=11\), \(d=13\), or general \(d\).

### CRITICAL 6 — even the all-`b=1` “full book” omits post-jump configurations

The \(w\)-closure theorem controls pure \(M=1\) ancestry. It does not control
a resonant jump that emits \(M\ge2\), a subsequent \(M\ge2\) chain, and a
later merge whose arrivals are all \(\mu_e\ge2\). These two-jump/mixed
configurations are expressly quarantined in:

- [SHEET6-MULTIPOLE.md](SHEET6-MULTIPOLE.md) §4;
- [BOOK-BASH-R2.md](BOOK-BASH-R2.md) §6; and
- [TEMPLATE-ATTACK.md](TEMPLATE-ATTACK.md) §§1c and 6.

Thus `SHEET6-DEPTH.md` §8's “finite book for every \((s,d)\)” is an
overstatement if read as a full-configuration theorem. Its own §9 gives the
narrower, correct perimeter. A finite local first-jump menu may still be a
theorem; equality with the implemented full book is not.

### CRITICAL 7 — finite-range enumeration cannot reduce JC2

The implemented on-axis sweep is exactly \(6\le d\le14\). The off-axis
entry census discussed in the book files is also bounded. No cited GGV result
or sheet theorem supplies an upper bound on \(d\). The GGV22 “\(\ge125\) or
\((72,108)\)” result is a lower-bound dichotomy in polynomial degree and says
nothing that truncates topological degree.

Therefore “the books cover all configurations” is **not a theorem at every
\(d\)**, even before the sector omissions are considered.

| Sector | What is finite in theorem form? | What is actually enumerated? | Exhaustive full configurations? |
|---|---|---|---|
| Entry layer, any fixed \(d\) | Necessary arithmetic entry data \(E\), conditional on T7's corrected inputs | Entry scans in bounded campaigns | **Yes for the necessary entry menu at a fixed \(d\); no claim of realizability or full routes** |
| Single pole | Finite entry menu at fixed \(d\); prime entries killed | TDU searches at selected \(d\), with opens/frontiers in composite cases | **No** for composite \(d\) |
| Multi-pole all \(b_i=1\) | Finite pure-\(M=1\) local marked-event menu at fixed \((s,d)\) | `BOOK-ENUM` only for \(d=6,\ldots,14\) | **No** as a full-configuration theorem; post-jump mixed contexts omitted |
| Multi-pole some \(b_i\ge2\) | No general finite-state/termination theorem | Generic bounded census is uncertified; special \(d=7\) route book only | **No** |
| All \(d\) | No upper bound on \(d\) | No unbounded enumeration | **No** |

### HIGH 1 — composite single-pole configurations remain open

The promoted TDU arithmetic proves a strong prime-\(d\) single-pole theorem,
but composite rows with \(b\ge2\) survive. The current search record is:

| \(d\) | reported surviving single-pole search classes | qualification |
|---:|---:|---|
| 6 | 4 | open |
| 8 | 16 | open |
| 9 | 16 | includes a hand-checked zero-charge chain |
| 10 | 23 | open kinds appear |
| 12 | 71 | lower bound; depth frontier hit |
| 14 | 48 | open |
| 15 | 87 | lower bound / frontier residue |
| 16 | 212 | lower bound / frontier residue |

Source: [SHEET6-TDUNIFORM.md](SHEET6-TDUNIFORM.md) §§4–7 and
[SHEET6-TDU-REVIEW.md](SHEET6-TDU-REVIEW.md). These are search classes,
not known realizable counterexamples, but they are enough to refute a claim
of completed exclusion or completed finite-chain enumeration.

### HIGH 2 — the on-axis composite books are open

After both book bashes and the later L6/template attack, the modeled local
on-axis survivor counts are:

| \(d\) | surviving modeled on-axis cells | current obstruction |
|---:|---:|---|
| 6 | 1 | residue-A |
| 8 | 1 | residue-A |
| 9 | 2 | residue-A in the \(s=2\) and \(s=3\) panels |
| 10 | 2 | residue-A and `IIa(2,5,1)@w3` |
| 12 | 12 | \(4+2+6\) cells in the \(s=2,3,4\) panels |
| 14 | 5 | four cells at \(s=2\), one residue-A at \(s=3\) |

Source: [TEMPLATE-ATTACK.md](TEMPLATE-ATTACK.md) §§2–3. These 23 cells are
local/template survivors inside the modeled perimeter, not 23 exhaustive
full configurations. Twenty-two lie at composite \(d>6\).

The direct answer to the campaign question is: **no current argument kills
any on-axis panel completely at \(d=8,9,10,12,14\)**. Many individual cells
have been killed, but the cells in the table remain. `SHEET6-DIRECTIONB.md`
kills only the pure-zero-tail stratum of residue-A and explicitly leaves the
forced-nonzero-tail locus alive. Residue-A survives in every nonempty modeled
panel. Beyond \(d=14\), no concrete on-axis JSON book has been generated.

Closing these modeled cells would still not close the corresponding
topological degree, because composite single-pole and, generally, off-axis
sectors remain.

### HIGH 3 — the Sigray replacement is not end to end

The audit of thesis §§2–5 and §6 through Proposition 6.2 (pp. 7–30) is
substantial and caught real errors, but the book also imports Propositions
6.3–6.8 and §§7–9. The current chain therefore rests on an unrefereed,
partly incorrect source plus a distributed set of clause-specific repairs.
The most serious unresolved or guarded items are:

- Proposition 4.2's constant-leading-part gap, directly inside the tower
  trust set;
- Statement 3.14's cross-fiber conjugation issue;
- Proposition 5.1 outside the pole-only \(g(P)=\infty\) use;
- the un-audited §7 Euler/critical-value layer;
- §8 multiplicity and pattern laws without a standalone reproof; and
- §9 case transport/budget after the E5/E6 repairs.

Proposition 5.8 and H5a have promoted replacements. That does not constitute
a replacement of the entire tree-to-book genome.

### HIGH 4 — source status and version drift remain

The exact GGV2 version consumed by the repo is arXiv v2. A newly published
2026 journal successor exists, but its equivalence to the pinned text has not
been established. GGV5 and GGV22 remain preprint inputs. In particular,
cross-checking a Proposition 4.3 transcription does not replace a proof that
the proposition exhausts its claimed family.

### MEDIUM 1 — contradictory status prose is unsafe to cite

Several older conclusions remain in place after later retractions:

- [BOOK-BASH-R2.md](BOOK-BASH-R2.md) §§5–6 and
  [TEMPLATE-ATTACK.md](TEMPLATE-ATTACK.md) §3 say \(d=7,11,13\) are fully
  excluded. [BOOK-ENUM.md](BOOK-ENUM.md)'s scope rider retracts the global
  prime-panel inference. The later tower campaign closes \(d=7\) only under
  its filed perimeter; \(d=11\) and \(d=13\) remain open.
- [BOOK-OFFAXIS.md](BOOK-OFFAXIS.md) retains superseded “closed,”
  “retracted,” and later repaired narratives in one file. Its latest §10–§11a
  declarations, together with later tower files, must control.
- `SHEET6-DEPTH.md` retains the stale \(\mathrm{gen}(W)+2\) expression after
  review corrected the safe representative depth to
  \(2\,\mathrm{gen}(W)+2\).

Any public theorem should cite a frozen status ledger, not an unqualified
filename.

### MEDIUM 2 — the implemented artifacts do not prove per-entry coverage

The on-axis engine aggregates a cell over all supporting join contexts, uses
“any-context survival wins,” and truncates the list of associated entry tags
in output. That is safe for maintaining a conservative survivor superset, but
it is not a certificate that a particular full configuration maps to a
particular entry-specific record. The future compiler must retain exact
provenance and reject an uncovered transition.

---

## 4. Claims that are wrong, not merely unproved

1. **“Not linearly equivalent to coordinates” means counterexample.** False;
   nonlinear triangular automorphisms are counterexamples to that wording.
2. **“Every counterexample is a GGV minimal pair after normalization.”**
   False quantifier. GGV selects some globally minimal counterexample.
3. **“GGV Proposition 4.3 reduces a general counterexample to the book
   setting.”** False. It is the special \((8,28)\) family and ends with a
   Laurent pair satisfying \([P,Q]=x^2\).
4. **“The GGV reduced pair carries the same `td` sheet structure.”** Not even
   well-typed for the Laurent/nonconstant-bracket output; no such invariant
   transport is defined.
5. **“`BOOK(s,d)` is an exhaustive full-configuration book for every
   \((s,d)\).”** False as a reading of the current artifacts. The proved
   closure is the \(M=1\) local menu; the files themselves exclude off-axis,
   mixed, and \(M\ge2\) suffix sectors.
6. **“Mixed all-\(\mu\ge2\) merges occur only for \(s\ge3\).”** False
   off-axis; two-pole examples occur when both entry multipliers are at least
   two.
7. **“The prime topological-degree theorem excludes every prime-degree
   configuration.”** False. TDU's theorem is single-pole only. The old
   on-axis prime emptiness statement omitted off-axis configurations.
8. **“Topological degrees 11 and 13 are fully excluded.”** False in current
   campaign status. At \(d=11\) an attempted 159-row diagnostic artifact
   exists, but no certified complete census does; its universal certificate
   is broken. The \(d=13\) sector is open. The later \(d=7\) result does not
   repair those statements.

The following are not asserted to be mathematically false, but remain
unproved at the necessary generality: the corrected Sigray trust set, global
off-axis finiteness, full post-jump on-axis coverage, and realizability or
nonrealizability of the surviving composite templates.

---

## 5. Co-researcher assessment

### 5.1 Highest-leverage repair: define the endpoint and prove a total landing map

Before another cell is killed, define four noninterchangeable objects:

1. the finite **entry book** \(\mathcal E(d)\);
2. the finite **local marked-event menu** for a fixed entry;
3. a **route book** within a stated transition grammar; and
4. a **full-configuration book**.

Then prove a marked-first-event landing theorem with exact input/output
types. The proof must retain every unused branch and downstream continuation
on which a later kill can depend. Implement it with a fail-closed compiler
that emits a coverage certificate per entry and marks any unknown transition
`OPEN`. This single repair would decide which existing cell kills are global
and which are only local observations.

### 5.2 Highest-leverage mathematical repair: a cap-free `M>=2` state theorem

Find an invariant, monovariant, or proof-producing finite automaton for
\(M\ge2\) segments and all-\(\mu\ge2\) merges, including the post-jump
two-event case. The \(M=1\) invariant \(w\) is the model, but the off-axis
audit explains exactly where its lowest-terms proof fails. Budget alone
cannot solve this: zero/low-cost escapes already occur, and state numerator
and \(M\) are unbounded under the current description.

This repair simultaneously addresses the generic off-axis hole and the
post-jump hole inside the purported on-axis full book. Without it, increasing
the enumerator's caps is evidence gathering, not a completeness proof.

### 5.3 Highest-leverage foundation repair: one standalone corrected sheet theorem

Write a self-contained theorem, independent of Sigray's narrative, whose
conclusion is exactly the entry/tree/transition object consumed by the
compiler. Reprove the required parts of §§2–9 with the H5a, E5, E6, ratio,
epsilon, and Proposition 5.8 repairs incorporated into the statements. Either
prove Proposition 4.2 at its constant-leading corner or exclude that corner
as an explicit hypothesis at every consumer.

Only after these three repairs is it meaningful to claim an end-to-end
reduction. At that point the highest-leverage **exclusion** target is the
uniform residue-A/coefficient obstruction, because residue-A survives every
nonempty modeled on-axis panel. In parallel, a uniform composite single-pole
theorem is necessary. Neither scientific kill substitutes for the reduction
repairs above.

### 5.4 Strategic assessment

The campaign has a real theorem-shaped core: normalization; \(d\ge6\); the
repaired every-fiber mass formula; finite arithmetic entries at fixed \(d\);
and a powerful finite \(M=1\) marked-event calculus. Those pieces justify
continuing the book program.

The present bottleneck is not another finite case bash. It is a coverage
theorem. Until that is supplied, the honest public claim is a collection of
conditional sector obstructions, not a reduction of JC2 to enumerated books.

---

## 6. Referee checklist for any future “JC2 reduces to books” claim

A future master theorem should not be promoted unless its proof answers yes
to all of the following.

- Does the input say “nonautomorphism,” not merely “nonlinear” or “not
  linearly equivalent”?
- Is the GGV quantifier existential and globally minimal, or is a theorem
  supplied for an arbitrary pair?
- If GGV data are used downstream, is there a polynomial-automorphism
  comparison theorem to the Sigray frame? Are constant Jacobian and \(td\)
  preserved at every step?
- Is the exact external version of every GGV proposition identified, with
  published/preprint status?
- Is the Sigray trust set proved in one corrected source, including §§7–9 and
  the Proposition 4.2 corner?
- Is \(B(d,E)\) defined as entries, local cells, routes, or complete
  configurations?
- Is there a total, fail-closed landing map for single-pole, on-axis,
  off-axis, mixed-merge, root, and \(M\ge2\) suffix sectors?
- Is the enumeration cap-free or accompanied by a proof that its bounds are
  complete?
- Is the theorem uniform in \(d\), or is an independent upper bound on \(d\)
  proved?
- Are survivor and kill records attached to exact entry/context provenance?
- Are stale retracted claims excluded from the cited status snapshot?

On the repository state audited here, the answers to the comparison,
full-landing, off-axis, post-jump, and all-\(d\) questions are **no**.
