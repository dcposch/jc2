# Primitive monodromy at \(td=6,7,8,9\): the first \(td\)-bound experiment

**Date:** 2026-08-21  
**Status:** executed; exact low-degree census banked  
**Code:** [cases/monodromy_td.py](../cases/monodromy_td.py)  
**Outcome:** **no topological degree \(6\le td\le9\) is forbidden.** The
experiment reaches the predicted \(A_d/S_d\) wall rather than a \(td\) bound.

## 1. Executive verdict

I enumerated all 29 primitive permutation groups of degrees \(6,7,8,9\),
enumerated their elements exactly, and intersected their cycle types with the
generic-\(a\) inertia-at-infinity profiles obtained from the printed Sigray
sheet formulas. I then constructed and checked product-one generating tuples.

The result has three levels.

1. **Raw sheet arithmetic:** 80 group/profile pairs survive, involving all 29
   primitive groups.
2. **After the promoted singleton-pole \(b=1\) entry kill:** 63 pairs survive,
   involving 27 groups. The only groups removed altogether are \(C_7\) and
   \(D_{14}\) at \(td=7\). Every degree remains.
3. **Uniform obstruction to a bound:** for every retained infinity profile
   there is an explicit genus-zero product-one tuple generating \(S_{td}\).
   Thus \(S_{td}\) survives every row, independently of the database census.

The two negative controls also survive:

- the genuine residue-A generic-fibre experiment has all 169 passports and an
  extremal witness with full \(S_6\), hence **primitive, no block descent**;
- the source-backed degree-nine Orevkov boundary-cover passport not only
  survives, but forces \(A_9\).

This is useful negative information for foundation gap G5. Group theory does
not presently bound \(td\). It says what a successful continuation must add:
an actual theorem controlling finite inertia/support, a justified primitivity
or block-descent bridge, and an independent geometric exclusion of the
alternating/symmetric cases. It also confirms the diagnosis in
[xmodel/sol-approaches.md](sol-approaches.md), §15: Keller separability does
not supply normality, and higher non-Galois primitive monodromy remains live.

## 2. What was actually specified—and what was not

The merged experiment in [APPROACHES.md](../APPROACHES.md), Stage 1, asks for
ramification at at most \(N\) places, Riemann--Hurwitz, transitivity,
primitivity, and an Orevkov negative control. The source survey
[xmodel/grok-approaches.md](grok-approaches.md), §23, likewise writes
“\(\le N\)” but never assigns \(N\). Neither entry supplies, for
\(td=7,8,9\),

- a genus for the normalized generic fibre;
- a menu of finite branch-cycle classes;
- a number of finite branch values;
- a translation from a sheet critical-value vertex to the number or support
  of inertia permutations.

The missing number cannot honestly be filled by putting \(N=td-1\).
[SHEET6-LROOT.md](../SHEET6-LROOT.md), §1, explains that Sigray's
\(td-1\) identity charges weighted **critical-value vertices**, once each,
regardless of how many punctures or directions lie above a vertex. In the
degree-six residue-A fibre, one \(x\)-side critical-value vertex represents 42
ramified \(e=2\) boundary punctures and at least 14 finite \(g\)-values; see
[GROK-MONODROMY.md](../GROK-MONODROMY.md), §1c.
[SHEET6-LT-REVIEW.md](../SHEET6-LT-REVIEW.md), §2, also records that the
printed sheet frame contains no global Riemann--Hurwitz excess formula for
\(\widehat g\).

There are two further conditional bridges.

- Connectedness gives **transitivity**, not primitivity. The minimal-\(td\)
  argument in [xmodel/sol-lateral3.md](sol-lateral3.md), §4, still needs a
  proof that an abstract block quotient descends to an \(\mathbb A^2\) open
  model and another polynomial, nonproper Keller map.
- The monodromy of the global finite étale cover over
  \(\mathbb A^2\setminus A(F)\) and the monodromy of the restricted generic
  fibre map \(\widehat g:\overline C_a\to\mathbb P^1\) are not identified by
  the survey data.

Accordingly, the word **admissible** below has a deliberately narrow meaning.

> A primitive group \(G\le S_d\) is group-theoretically admissible for a
> sheet-derived infinity profile \(\lambda\) if \(G\) contains an element
> \(\sigma_\infty\) of type \(\lambda\), and there exists some product-one
> tuple containing \(\sigma_\infty\) that generates \(G\) and has
> nonnegative integral Riemann--Hurwitz genus.

Finite inertia is existential and unrestricted because the survey does not
specify it. Passing this test gives an abstract connected compact branched
cover by Riemann existence. It does **not** give a plane polynomial Keller
pair, a valid boundary book, or even a passport that the missing geometry is
known to realize.

## 3. Exact infinity profiles from the sheet frame

### 3.1 Row-to-cycle conversion

For a global type \(2\le\alpha<\beta\), \(\gcd(\alpha,\beta)=1\), the printed
row arithmetic in [SHEET6-TDUNIFORM.md](../SHEET6-TDUNIFORM.md), §1, is

\[
 (D,D_g)=a(\alpha,\beta),\qquad
 (P,P_g)=b(\alpha,\beta),\qquad
 \Lambda(F)=\frac{ab\alpha\beta}{\nu},
 \qquad td=\sum_F\Lambda(F).
\]

For \(\nu>1\), Sigray Props. 5.4--5.6 give two cases:

- **A:** \(\nu\mid\alpha\) and \(\nu\mid b\beta-1\). The vertex represents
  \(P/\nu=b\alpha/\nu\) punctures, each with pole order
  \(D_g=a\beta\).
- **B:** \(\nu\mid\beta\) and \(\nu\mid b\alpha-1\). It represents one
  puncture of pole order \(D_g/\nu=a\beta/\nu\), and
  \((P-1)/\nu=(b\alpha-1)/\nu\) punctures of pole order \(D_g=a\beta\).

For \(\nu=1\), the two displayed puncture formulas coincide: there are \(P\)
punctures, each of pole order \(D_g\). The code records that row once.

These cycle lengths sum to \(\Lambda(F)\). For several pole vertices of the
same global type, the profiles concatenate. This distinction matters:
\(\Lambda(F)\) is the total mass of a puncture cluster, not automatically one
monodromy cycle. The generic-open-set interpretation of the local lengths as
actual \(g\)-pole orders is audited in [SOL-PROP58.md](../SOL-PROP58.md),
§4. Special fibres may redistribute boundary length, so the table is a
**generic-\(a\) sheet-entry table**, not a universal assertion at every
\(f\)-value.

### 3.2 Raw and entry-filtered menus

The exact row enumeration gives:

| \(td\) | Raw generic-\(a\) profiles for \(\sigma_\infty\) | Retained after the singleton-pole \(b=1\) kill |
|---:|---|---|
| 6 | \((6),(5,1),(4,2),(3,3)\) | \((5,1),(3,3)\) |
| 7 | \((7),(3,3,1)\) | \((3,3,1)\) |
| 8 | \((8),(7,1),(6,2),(4,4),(3,3,1,1)\) | \((7,1),(6,2),(4,4),(3,3,1,1)\) |
| 9 | \((9),(8,1),(6,3),(4,4,1),(3,3,3)\) | \((8,1),(6,3),(4,4,1),(3,3,3)\) |

The second column is the exact Prop. 5.4--5.6 arithmetic. The third applies
only the promoted result that a **singleton-pole** configuration with \(b=1\)
is impossible (Prop. 8.4 as assembled in
[SHEET6-TDUNIFORM.md](../SHEET6-TDUNIFORM.md), §6). It does not delete a
\(b=1\) vertex in a multi-pole configuration: §8 of that file explicitly
marks the missing multi-pole analogue.

The optional H5a/N1 interpretation \(\gcd(a,\nu)=1\) was not imposed. If it is
added as a sensitivity filter, it also deletes the degree-nine profile
\((6,3)\); every degree and all eleven degree-nine groups still survive via
other profiles. Later book/tree kills are incomplete and were not silently
promoted to a classification theorem.

## 4. Engine and completeness perimeter

GAP was not installed in the banked environment:

~~~text
command -v gap                         -> no output
Python sageall/libgap imports          -> unavailable
brew --version                         -> Homebrew 6.0.18
HOMEBREW_NO_AUTO_UPDATE=1 brew search '/^gap$/'
                                      -> no formula or cask in active taps
~~~

No installation was attempted. The requested fallback is a self-contained
pure-Python implementation using the official GAP PrimGrp low-degree data.
The group IDs, names, orders, and available matrix/permutation generator data
were transcribed from
[data/gps1.g](https://github.com/gap-packages/primgrp/blob/eac1e8cf43a9e20240397db00344f97fd24c0955/data/gps1.g), pinned at commit
eac1e8cf43a9e20240397db00344f97fd24c0955 and file blob
9f8efb2cc5ef6baee485bed87004e66ce1f4410f. Where PrimGrp uses a family
sentinel (for example PSL, PGL, Alt, or Sym), the script supplies an equivalent
standard natural action and verifies its closure and order. The current official
[PackageInfo.g](https://github.com/gap-packages/primgrp/blob/master/PackageInfo.g)
identifies PrimGrp 4.0.3 and states that the library is complete up to
permutation isomorphism in these degrees.

For each group the script independently checks:

1. exact closure and the advertised order;
2. transitivity;
3. primitivity by exhaustive block testing;
4. the full set of element cycle types;
5. a product-one generating tuple for every reported incidence;
6. integral, nonnegative Riemann--Hurwitz genus;
7. exact regeneration of the witness group under --check.

The complete primitive-group index used is:

| \(d\) | GAP primitive groups \(dPj\), with order |
|---:|---|
| 6 | \(6P1=\mathrm{PSL}(2,5)\) (60); \(6P2=\mathrm{PGL}(2,5)\) (120); \(6P3=A_6\) (360); \(6P4=S_6\) (720) |
| 7 | \(7P1=C_7\) (7); \(7P2=D_{14}\) (14); \(7P3=7{:}3\) (21); \(7P4=\mathrm{AGL}(1,7)\) (42); \(7P5=L(3,2)\) (168); \(7P6=A_7\) (2520); \(7P7=S_7\) (5040) |
| 8 | \(8P1=\mathrm{AGL}(1,8)\) (56); \(8P2=A\Gamma L(1,8)\) (168); \(8P3=\mathrm{ASL}(3,2)\) (1344); \(8P4=\mathrm{PSL}(2,7)\) (168); \(8P5=\mathrm{PGL}(2,7)\) (336); \(8P6=A_8\) (20160); \(8P7=S_8\) (40320) |
| 9 | \(9P1=3^2{:}4\) (36); \(9P2=3^2{:}D_8\) (72); \(9P3=3^2{:}Q_8=M_9\) (72); \(9P4=3^2{:}8=\mathrm{AGL}(1,9)\) (72); \(9P5=A\Gamma L(1,9)\) (144); \(9P6=3^2{:}(2' A_4)\) (216); \(9P7=\mathrm{AGL}(2,3)\) (432); \(9P8=\mathrm{PSL}(2,8)\) (504); \(9P9=P\Gamma L(2,8)\) (1512); \(9P10=A_9\) (181440); \(9P11=S_9\) (362880) |

## 5. Census results

Write \(dPj\) for PrimitiveGroup(d,j). Every entry in the last column both
contains the displayed infinity class and passes the existential Hurwitz
completion test.

| \(td\) | Retained \(\sigma_\infty\) | Compatible primitive groups |
|---:|---|---|
| 6 | \((5,1)\) | \(6P1,6P2,6P3,6P4\) |
| 6 | \((3,3)\) | \(6P1,6P2,6P3,6P4\) |
| 7 | \((3,3,1)\) | \(7P3,7P4,7P5,7P6,7P7\) |
| 8 | \((7,1)\) | \(8P1,8P2,8P3,8P4,8P5,8P6,8P7\) |
| 8 | \((6,2)\) | \(8P2,8P3,8P6,8P7\) |
| 8 | \((4,4)\) | \(8P3,8P4,8P5,8P6,8P7\) |
| 8 | \((3,3,1,1)\) | \(8P2,8P3,8P4,8P5,8P6,8P7\) |
| 9 | \((8,1)\) | \(9P4,9P5,9P7,9P11\) |
| 9 | \((6,3)\) | \(9P2,9P5,9P7,9P11\) |
| 9 | \((4,4,1)\) | \(9P1,9P2,9P3,9P4,9P5,9P6,9P7,9P10,9P11\) |
| 9 | \((3,3,3)\) | \(9P1,9P2,9P3,9P4,9P5,9P6,9P7,9P8,9P9,9P10,9P11\) |

For completeness, the raw-only incidences removed by the singleton entry
filter are:

| \(td\) | Raw-only profile | Groups containing it |
|---:|---|---|
| 6 | \((6)\) | \(6P2,6P4\) |
| 6 | \((4,2)\) | \(6P3,6P4\) |
| 7 | \((7)\) | all \(7P1,\ldots,7P7\) |
| 8 | \((8)\) | \(8P5,8P7\) |
| 9 | \((9)\) | \(9P8,9P9,9P10,9P11\) |

Thus:

| Layer | Group/profile rows | Distinct primitive groups | Distinct groups by degree |
|---|---:|---:|---|
| Raw Prop. 5.4--5.6 | 80 | 29/29 | \(4,7,7,11\) |
| Singleton-entry filtered | 63 | 27/29 | \(4,5,7,11\) |

The profile-specific restrictions are real—for example, only four of the
eleven degree-nine groups contain \((8,1)\)—but none removes \(S_d\), and their
union removes no degree.

## 6. Why every reported row has a Hurwitz completion

### 6.1 Database-group completion

Given a reported \(G\) and \(\sigma_\infty\in G\), append the pinned database
generators \(g_1,\ldots,g_r\) and then the inverse of the accumulated product:

\[
 \bigl(\sigma_\infty,g_1,\ldots,g_r,
       (\sigma_\infty g_1\cdots g_r)^{-1}\bigr).
\]

The tuple has product one and generates exactly \(G\). Identity closing terms
are omitted. The program checks Riemann--Hurwitz and, in the full mode,
re-closes each of the 63 tuples. This is enough for the stated existential
test because finite inertia was not specified.

### 6.2 Uniform genus-zero \(S_d\) completion

There is a stronger all-profile construction. Let \(\lambda\vdash d\) have
\(k\) cycles, including fixed points.

1. Factor \(\sigma_\infty^{-1}\) inside its cycles into \(d-k\)
   transpositions.
2. Choose one representative from each cycle and add \(k-1\) identical pairs
   \((\tau_i,\tau_i)\), where \(\tau_i\) joins the first cycle to the \(i\)-th
   cycle.

The paired terms do not change the product. The transposition graph is
connected, so the finite branch cycles generate \(S_d\). Their total defect is

\[
 (d-k)+2(k-1)=d+k-2,
\]

while \(\operatorname{ind}(\sigma_\infty)=d-k\). The total defect is
\(2d-2\), hence the resulting cover has genus zero.

If each finite factor is assigned its own branch value, this witness has

\[
 B=d+k-1
\]

branch values including infinity. If \(q\) is the number of nontrivial cycles
of \(\sigma_\infty\), it has

\[
 P=d+k-2+q
\]

ramified source points over all those values. The checked values are:

| \(td\) | Profile | \(S_d\) witness branch values \(B\) | Ramified source points \(P\) | Genus |
|---:|---|---:|---:|---:|
| 6 | \((5,1)\) | 7 | 7 | 0 |
| 6 | \((3,3)\) | 7 | 8 | 0 |
| 7 | \((3,3,1)\) | 9 | 10 | 0 |
| 8 | \((7,1)\) | 9 | 9 | 0 |
| 8 | \((6,2)\) | 9 | 10 | 0 |
| 8 | \((4,4)\) | 9 | 10 | 0 |
| 8 | \((3,3,1,1)\) | 11 | 12 | 0 |
| 9 | \((8,1)\) | 10 | 10 | 0 |
| 9 | \((6,3)\) | 10 | 11 | 0 |
| 9 | \((4,4,1)\) | 11 | 12 | 0 |
| 9 | \((3,3,3)\) | 11 | 13 | 0 |

These \(B,P\) values are **upper bounds for explicit witnesses**, not minima
and not a recovered value of the survey's \(N\). If a future theorem supplies
an \(N\), its meaning must first be fixed: branch values, ramified boundary
source points, all boundary punctures, and critical-value vertices are four
different counts. A smaller \(N\) would require a new support-minimizing
passport search; failure of the displayed witness would not itself be a
nonexistence proof.

## 7. Negative controls

### 7.1 Residue-A: the genuine \(\widehat g\) control

This is the most directly relevant control. In
[GROK-MONODROMY.md](../GROK-MONODROMY.md), the degree-six residue-A fibre has

\[
 \sigma_\infty=(3,3),
\]

and finite classes \((2),(2,2),(2,2,2)\). Writing \(a,b,c\) for the number of
branch values of those types, Riemann--Hurwitz gives

\[
 a+2b+3c=42,
\]

with 169 nonnegative solutions. The existing exact sweep was rerun:

~~~text
python3 cases/grok_monodromy.py
52 checks, 0 FAIL
all 169 passports witnessed in S6
~~~

Here “in \(S_6\)” means a factorization by permutations of six letters. The
169-passport sweep checks product, types, and transitivity for every row; it
does not claim that every one of those particular tuples generates the full
group. Full order (720) is checked for the extremal witness below, which is
already enough to defeat any universally forced-block conclusion.

The new script separately replays the extremal passport \((2)^{42}\). Its
product is one, its generated group has order \(720=S_6\), and its genus is
18. This mandatory control therefore reports exactly what
[xmodel/sol-lateral3.md](sol-lateral3.md), §4, requires:

> **primitive, full \(S_6\), no block descent.**

### 7.2 Orevkov \((48,64)\): corrected object and result

The survey's phrase “Orevkov \((48,64)\) place counts” conflates different
objects. In Orevkov's primary paper,
[*Counter-examples to the “Jacobian Conjecture at Infinity”*](https://www.math.univ-toulouse.fr/~orevkov/jci-e.pdf),
§2.4 and Prop. 2.5, \(N=9\) is the surface/topological degree. The numbers 48
and 64 are the polynomial degrees that the unique \(N=9\) solution of §2.4's
equations (8)--(15), under that section's hypotheses, would have **if** it
were a Jacobian-conjecture counterexample. This
\(N\) is unrelated to the survey's undefined support cap.

The repository supplies no complete generic-fibre \(\widehat g\) passport for
that datum. The primary source does, however, determine a degree-nine rational
boundary-component cover

\[
 \widetilde L_1\longrightarrow L_1
\]

with three branch profiles

\[
 (3,3,3),\qquad(4,4,1),\qquad(5,1,1,1,1).
\]

Their defects are \(6,6,4\), totaling \(16=2\cdot9-2\), so the cover has
genus zero. An explicit tuple, in the usual right-to-left convention, is

\[
\begin{aligned}
A&=(1\,2\,3)(4\,5\,6)(7\,8\,9),\\
B&=(2\,5\,4\,3)(6\,7\,9\,8),\\
C&=(1\,4\,8\,6\,2),
\end{aligned}
\qquad ABC=1.
\]

Exact closure gives order \(181440=|A_9|\). In fact the passport forces this
group in every transitive realization:

1. a nontrivial degree-nine block system would have three blocks of size
   three;
2. the 5-cycle can neither act nontrivially on three blocks nor fit inside
   one block, so the action is primitive;
3. Jordan's \(p\)-cycle theorem, with \(p=5\le9-3\), gives
   \(A_9\le G\);
4. all three branch permutations are even, so \(G\le A_9\).

Hence \(G=A_9\). The control **passes and forces the exceptional alternating
case**. Its scope remains important: this is boundary-component monodromy,
not an identified passport for \(\widehat g\), and the numerical splice datum
is not a global polynomial Keller pair. It is therefore an adjacent negative
control, not evidence that a degree-nine Keller cover exists.

## 8. What this says about the G5 wall

### 8.1 No degree exclusion

The direct answer is negative:

\[
 \boxed{\text{Current group theory forbids none of }td=6,7,8,9.}
\]

The mildest genuine restriction is at \(td=7\), where the retained
\((3,3,1)\) class removes \(C_7\) and \(D_{14}\). At \(td=6,8,9\), every
primitive group occurs with at least one retained profile. More decisively,
\(S_d\) occurs with every individual retained profile in every degree.

### 8.2 The only visible funnel is toward \(A_d/S_d\)

For a primitive subgroup \(G\le S_d\):

- if geometry supplies a transposition, then \(G=S_d\);
- if it supplies a single 3-cycle and \(d\ge6\), Jordan's theorem gives
  \(A_d\le G\).

The sheet-derived infinity permutations have too much support to invoke these
small-cycle conclusions by themselves. The minimum moved-point degrees of the
29 database groups, in PrimGrp-ID order, are:

| \(d\) | Minimum moved points \(\mu(dP1),\mu(dP2),\ldots\) |
|---:|---|
| 6 | \(4,4,3,2\) |
| 7 | \(7,6,6,6,4,3,2\) |
| 8 | \(7,6,4,6,6,3,2\) |
| 9 | \(8,6,8,8,6,6,6,7,6,3,2\) |

Thus a future bounded-support theorem may collapse the list toward \(A_d\) or
\(S_d\), but that is not a contradiction. The controls show both sides of the
wall concretely: residue-A simple inertia generates \(S_6\), while the
Orevkov boundary passport forces \(A_9\).

### 8.3 Exact missing inputs for a useful continuation

The primitive-monodromy route can feed G5 only after three new geometric
statements are supplied.

1. **Inertia-support theorem.** Translate a complete sheet/book record into
   finite branch classes and a bound on ramified boundary source points or
   branch values. Sigray's critical-value-vertex budget is not this theorem.
2. **Primitivity/descent theorem.** Either prove the relevant monodromy is
   primitive, or prove that a block quotient descends from an intermediate
   function field to a lower-degree polynomial, nonproper Keller map.
3. **Exceptional-group exclusion.** Couple the two coordinate fibrations,
   Jacobian contact pairing, discriminant parity, or boundary canonical data
   strongly enough to rule out \(A_d\) and \(S_d\). Group theory alone leaves
   them as the dominant survivors.

Even a successful \(B(D)\) bound of the kind proposed in
[xmodel/sol-lateral3.md](sol-lateral3.md) would depend on the polynomial
degree \(D\); it would not by itself repair the separate foundation gap that
there is no absolute upper bound on \(D\) or \(td\).

## 9. Reproduction

The script is standard-library only and makes no network calls.

~~~bash
python3 -B cases/monodromy_td.py
python3 -B cases/monodromy_td.py --details
python3 -B cases/monodromy_td.py --json
python3 -B cases/monodromy_td.py --check
python3 -B cases/grok_monodromy.py
~~~

Banked full-check result:

~~~text
29 primitive groups: closure/order/transitivity/primitivity PASS
63 entry-filtered group/profile Hurwitz rows: PASS
11 uniform S_d genus-zero profile controls: PASS
Orevkov boundary control: A9, order 181440, genus 0, PASS
residue-A control: S6, order 720, genus 18, PASS
cases/grok_monodromy.py: 52 checks, 0 FAIL; 169/169 passports
~~~

Banked SHA-256 values:

~~~text
cases/monodromy_td.py
  2642c0ab94e090527ba7714faa7925730d395a7db413d78ea10a3387d22c1aac
python3 -B cases/monodromy_td.py --json
  21dfde20d7ec6deaab0eeb8e55d3e230fcd2eb0ed02444936679efffcbc27bc2
~~~

The JSON output includes raw and entry-filtered profiles, profile-to-group
incidence, one exact pole-row derivation per profile with configuration counts,
cycle types of every witness, support upper bounds, and both controls. The
final repository artifacts from this experiment are only this report and
cases/monodromy_td.py; no git state was changed.

## 10. Banked conclusion

**Primitive monodromy is not a \(td\)-bound at the present information
level.** The exact low-degree data reject no \(td=6,7,8,9\); the strongest
uniform construction supplies \(S_d\) for every retained sheet profile; the
best source-backed degree-nine negative control supplies \(A_9\). This is not
a null result: it isolates the G5 obstruction cleanly. The next meaningful
experiment is not a larger unconstrained primitive-group census. It is the
Stage-2 coupled two-cover passport CSP, or first a theorem that turns sheet
critical-value data into an actual finite-inertia/support cap.
