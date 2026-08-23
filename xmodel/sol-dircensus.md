# DIR(C): rootwise census

Date: 2026-08-23.

This census uses as exact inputs [sol-truth.md](sol-truth.md) §1,
[sol-bridge2.md](sol-bridge2.md), and [sol-pc.md](sol-pc.md) §0.  The realization
tier is part of every conclusion:

- **KELLER CONTROL**: an actual constant-Jacobian polynomial.
- **BOOK-RELATIVE**: exact data inside a filed Newton/entry book, conditional on
  that book being realized by a Keller polynomial.
- **FORMAL**: local or numerical data only.  This is not a Keller germ unless
  explicitly said otherwise.

The exact root formula is
\[
 R_P={B\Delta_P\over\alpha\beta\mu_P},\qquad
 \Delta_P=\sum_{\gamma\mid P,\ {\rm pole}}p_\gamma .
\tag{1}
\]
For a realized whole book,
\[
 \sum_P\Delta_P=td,\qquad
 \sum_P{\mu_P\over B}R_P={td\over\alpha\beta},\qquad
 \sum_P{\mu_P\over B}=1.
\tag{2}
\]
Thus \(td/(\alpha\beta)\) is a weighted average of the root ratios, not
generally a root ratio.

## 1. Numerically complete root rows

| source/root | tier | \((B,\alpha,\beta,\mu_P,\sum p_\gamma)\) | \(R_P\) | status |
|---|---|---:|---:|---|
| Hénon, unique proper root | KELLER CONTROL | \((\kappa,1,2,\kappa,1)\) | \(1/2\) | actual, \(\kappa=42\,2^r\) in the filed tower |
| residue-A \(Y\)-root | BOOK-RELATIVE | \((84,2,3,63,3+3)\) | \(4/3\) | exact equality in the filed template |
| residue-A \(X\)-root | BOOK-RELATIVE | \((84,2,3,21,0)\) | \(0\) | \(g\) finite at this root |
| same two-pole inventory at \(\mu=B\) | FORMAL | \((B,2,3,B,3+3)\) | \(1\) | comparison only; no realization claim |
| class-kill family | FORMAL, **NON-KELLER** | \((B,\alpha,\beta,B,\alpha\beta B^2-\alpha B)\) | \(B^2-B/\beta\) | excluded by the pure-minor identity |

Consequently the maximum among **fully specified filed admissible root tuples**
is
\[
                         R_{\rm complete,max}=4/3.
\tag{3}
\]
Among actual polynomial Keller controls in this file it is only \(1/2\).

The value (3) must not be called the maximum of the books.  Except for the
residue-A template, the books do not file \(B\), \(\mu_P\), or the partition of
their pole branches among proper roots.  Their exact root row has only the
schema
\[
 (B,\alpha,\beta,\mu_P,\sum_{i\in S_P}p_i)
       =(?,\alpha,\beta,?,\sum_{i\in S_P}p_i),\qquad
 R_P={B\sum_{i\in S_P}p_i\over\alpha\beta\mu_P},
\tag{4}
\]
where both \(S_P\) and the two question marks are unfiled.  Reporting a numeric
\(R_P\) for such a row would manufacture data.

## 2. Exact pole profiles in the \(td\leq12\) books

For compactness write an entry packet as
\[
 [\Lambda;a,b,\nu],\qquad \Lambda={ab\alpha\beta\over\nu}.
\]
The filed local monodromy rule gives the displayed generic-\(a\) multiset
\(\mathbf p\) of pole orders: in case A it is \(b\alpha/\nu\) copies of
\(a\beta\); in case B it is one \(a\beta/\nu\) and
\((b\alpha-1)/\nu\) copies of \(a\beta\).
Every table row below therefore gives the exact global data
\[
 (?,\alpha,\beta,?,\mathbf p),\quad
 \sum\mathbf p=td,\quad
 \max_P R_P\geq\bar R:={td\over\alpha\beta}
\tag{5}
\]
**if** the row has a Keller realization.  It does not give the rootwise
partition required in (4).

### 2.1 Single-pole entry inventories

These are all post-pin/N1 single-pole entry rows through \(td=12\).  “Entry”
means that later tree/coefficient gates have not been asserted.

| id | \(td\) | \((\alpha,\beta)\) | packet \([\Lambda;a,b,\nu]\) | exact \(\mathbf p\) | \(\bar R\) | book status |
|---|---:|---:|---:|---:|---:|---|
| S1 | 4 | (2,3) | [4;1,2,3] | (3,1) | 2/3 | closed with \(td\leq5\) |
| S2 | 6 | (2,5) | [6;1,3,5] | (5,1) | 3/5 | downstream dead |
| S3 | 6 | (3,5) | [6;1,2,5] | (5,1) | 2/5 | entry |
| S4 | 8 | (2,3) | [8;2,2,3] | (6,2) | 4/3 | entry |
| S5 | 8 | (2,7) | [8;1,4,7] | (7,1) | 4/7 | entry |
| S6 | 8 | (4,7) | [8;1,2,7] | (7,1) | 2/7 | entry |
| S7 | 9 | (2,3) | [9;1,3,2] | (3,3,3) | 3/2 | entry |
| S8 | 9 | (3,4) | [9;1,3,4] | (4,4,1) | 3/4 | entry |
| S9 | 9 | (3,8) | [9;1,3,8] | (8,1) | 3/8 | entry |
| S10 | 10 | (2,3) | [10;1,5,3] | (3,3,3,1) | 5/3 | entry |
| S11 | 10 | (2,9) | [10;1,5,9] | (9,1) | 5/9 | entry |
| S12 | 10 | (3,5) | [10;1,2,3] | (5,5) | 2/3 | entry |
| S13 | 10 | (5,9) | [10;1,2,9] | (9,1) | 2/9 | entry |
| S14 | 12 | (2,3) | [12;1,2,1] | (3,3,3,3) | 2 | entry |
| S15 | 12 | (2,5) | [12;2,3,5] | (10,2) | 6/5 | entry |
| S16 | 12 | (2,9) | [12;1,2,3] | (9,3) | 2/3 | entry |
| S17 | 12 | (2,11) | [12;1,6,11] | (11,1) | 6/11 | entry |
| S18 | 12 | (3,5) | [12;2,2,5] | (10,2) | 4/5 | entry |
| S19 | 12 | (3,10) | [12;1,2,5] | (10,2) | 2/5 | entry |
| S20 | 12 | (3,11) | [12;1,4,11] | (11,1) | 4/11 | entry |
| S21 | 12 | (4,11) | [12;1,3,11] | (11,1) | 3/11 | entry |
| S22 | 12 | (6,11) | [12;1,2,11] | (11,1) | 2/11 | entry |

There are no post-pin/N1 single-pole rows at prime \(td=7,11\).

### 2.2 Multi-pole BOOK-ENUM inventories

This is the complete filed \(6\leq td\leq12\) multi-pole list.  Repetition is
shown by a superscript.  Status codes: \(L\) is an off-axis L6 ladder entry;
\(H\) fails the promoted H5a/N1 condition; \(R\) is the residue-A template
cell; \(B\) is another BOOK-ENUM row.  These codes are inventory status, not a
polynomial realization.

| id | \(td/k\) | \((\alpha,\beta)\) | packets | exact \(\mathbf p\) | \(\bar R\) | status |
|---|---:|---:|---|---:|---:|---|
| M1 | 6/2 | (2,3) | [3;1,1,2]\(^2\) | (3,3) | 1 | R |
| M2 | 7/2 | (2,3) | [3;1,1,2]+[4;1,2,3] | (3,3,1) | 7/6 | L; \(td=7\) tower-dead |
| M3 | 8/2 | (2,3) | [4;1,2,3]\(^2\) | (3,3,1,1) | 4/3 | L |
| M4 | 8/2 | (3,4) | [4;1,1,3]\(^2\) | (4,4) | 2/3 | B |
| M5 | 9/2 | (2,3) | [3;1,1,2]+[6;1,1,1] | (3,3,3) | 3/2 | B |
| M6 | 9/2 | (2,3) | [3;1,1,2]+[6;2,1,2] | (6,3) | 3/2 | H |
| M7 | 9/3 | (2,3) | [3;1,1,2]\(^3\) | (3,3,3) | 3/2 | B |
| M8 | 10/2 | (2,3) | [4;1,2,3]+[6;1,1,1] | (3,3,3,1) | 5/3 | L |
| M9 | 10/2 | (2,3) | [4;1,2,3]+[6;2,1,2] | (6,3,1) | 5/3 | H |
| M10 | 10/2 | (3,4) | [4;1,1,3]+[6;1,1,2] | (4,4,2) | 5/6 | B |
| M11 | 10/2 | (2,5) | [5;1,1,2]\(^2\) | (5,5) | 1 | B |
| M12 | 10/2 | (4,5) | [5;1,1,4]\(^2\) | (5,5) | 1/2 | B |
| M13 | 10/3 | (2,3) | [3;1,1,2]\(^2\)+[4;1,2,3] | (3,3,3,1) | 5/3 | L |
| M14 | 11/2 | (2,3) | [3;1,1,2]+[8;2,2,3] | (6,3,2) | 11/6 | L; audit conditional |
| M15 | 11/2 | (2,5) | [5;1,1,2]+[6;1,3,5] | (5,5,1) | 11/10 | L; audit conditional |
| M16 | 11/3 | (2,3) | [3;1,1,2]+[4;1,2,3]\(^2\) | (3,3,3,1,1) | 11/6 | L; audit conditional |
| M17 | 12/2 | (2,3) | [3;1,1,2]+[9;1,3,2] | (3,3,3,3) | 2 | L |
| M18 | 12/2 | (2,3) | [3;1,1,2]+[9;3,1,2] | (9,3) | 2 | B |
| M19 | 12/2 | (2,3) | [4;1,2,3]+[8;2,2,3] | (6,3,2,1) | 2 | L |
| M20 | 12/2 | (2,3) | [6;1,1,1]\(^2\) | (3,3,3,3) | 2 | B |
| M21 | 12/2 | (2,3) | [6;1,1,1]+[6;2,1,2] | (6,3,3) | 2 | H |
| M22 | 12/2 | (2,3) | [6;2,1,2]\(^2\) | (6,6) | 2 | H |
| M23 | 12/2 | (3,4) | [4;1,1,3]+[8;2,1,3] | (8,4) | 1 | B |
| M24 | 12/2 | (3,4) | [6;1,1,2]\(^2\) | (4,4,2,2) | 1 | B |
| M25 | 12/2 | (2,5) | [6;1,3,5]\(^2\) | (5,5,1,1) | 6/5 | L |
| M26 | 12/2 | (3,5) | [6;1,2,5]\(^2\) | (5,5,1,1) | 4/5 | L; \((3,5)\) list-relative dead |
| M27 | 12/2 | (5,6) | [6;1,1,5]\(^2\) | (6,6) | 2/5 | B |
| M28 | 12/3 | (2,3) | [3;1,1,2]\(^2\)+[6;1,1,1] | (3,3,3,3) | 2 | B |
| M29 | 12/3 | (2,3) | [3;1,1,2]\(^2\)+[6;2,1,2] | (6,3,3) | 2 | H |
| M30 | 12/3 | (2,3) | [4;1,2,3]\(^3\) | (3,3,3,1,1,1) | 2 | L |
| M31 | 12/3 | (3,4) | [4;1,1,3]\(^3\) | (4,4,4) | 1 | B |
| M32 | 12/4 | (2,3) | [3;1,1,2]\(^4\) | (3,3,3,3) | 2 | B |

The union of the two tables contains every filed global type encountered here:
\[
\begin{split}
 &(2,3),(2,5),(2,7),(2,9),(2,11),\\
 &(3,4),(3,5),(3,8),(3,10),(3,11),\\
 &(4,5),(4,7),(4,11),(5,6),(5,9),(6,11).
\end{split}
\]

The rows \(H=\{\mathrm{M6,M9,M21,M22,M29}\}\) are not counted as live after
H5a.  M26 is dead only relative to the filed \(td=12,(3,5)\) 14-cell book;
that verdict does not cover the distinct single-pole row S18.  The \(td=11\)
audit is conditional.  These qualifications do not alter
the numerical point below: uneliminated/book-live rows already have average
strictly above \(4/3\).

## 3. Q1: maximum seen

The answer depends on the word “seen”:

| census level | exact conclusion |
|---|---|
| actual polynomial Keller controls | maximum filed \(R_P=1/2\) |
| fully specified admissible root tuples | maximum filed \(R_P=4/3\), at residue A |
| \(td\leq12\) book inventories | rootwise maximum is **not determined**; \(B,\mu_P,S_P\) are missing |
| conditional Keller lift of the books | some root must satisfy the lower bounds below |

The first book-relative obstructions to treating \(4/3\) as a ceiling are:

| entry/book row(s) | \((td,\alpha,\beta)\) | exact forced statement under a Keller lift | present status |
|---|---:|---:|---|
| S7, M5, M7 | (9,2,3) | \(\max_P R_P\geq3/2\) | entry/BOOK-ENUM arithmetic; not in the promoted off-axis ladder |
| S10, M8, M13 | (10,2,3) | \(\max_P R_P\geq5/3\) | unadjudicated; M8/M13 are promoted off-axis ladder rows |
| M14, M16 | (11,2,3) | \(\max_P R_P\geq11/6\) | tower-dead only under the conditional \(td=11\) audit |
| S14, M17--M20, M28, M30, M32 | (12,2,3) | \(\max_P R_P\geq2\) | type-\((2,3)\) rows unadjudicated; H5a-dead M21/M22/M29 omitted |

Therefore:

- **No fully specified banked root exceeds \(4/3\).**
- **Several banked inventories do exceed it in the only exact sense presently
  available:** every Keller realization of the row would contain some root
  above \(4/3\).  Through \(td=12\), the largest such forced average is \(2\).
- \(2\) is not an observed maximum and not an upper bound.  The root receiving
  the pole mass may have a much larger ratio.

## 4. Q2: light roots, growth families, and the pure minor

### 4.1 No actual dangerous germ is presently constructed

No filed actual constant-Jacobian germ has
\(\mu_P/B\to0\) and \(\Delta_P\geq1\).  The actual Hénon control has
\(\mu_P/B=1\); the residue-A numerical root has \(\mu_P/B=3/4\) and is only
book-relative.  The non-Keller class-kill family is irrelevant by hypothesis.

The bank does contain the following precise growth directions:

| family | tier | exact pole data | root tuple / ratio information |
|---|---|---|---|
| fixed-type uniform two-entry family, \(b\) odd | FORMAL | \((\alpha,\beta)=(2,3)\), packets \([3b;1,b,2]^2\); \(\mathbf p=(3^{\,2b})\), \(td=6b\) | \((?,2,3,?,\sum_{i\in S_P}p_i)\); any Keller lift has \(\max R_P\geq b\) |
| coefficient-solved one-pole schema, \(A=30t+5\) | FORMAL | packet \([4A;A,2,3]\); \(\mathbf p=(3A,A)\), \(td=4A\) | root landing unfiled; any Keller lift has \(\max R_P\geq2A/3\) |
| coefficient-solved two-pole schema, \(A\) odd | FORMAL | packets \([3A;A,1,2]^2\); \(\mathbf p=(3A,3A)\), \(td=6A\) | root landing unfiled; any Keller lift has \(\max R_P\geq A\) |
| \(q=2\) carrier insertion | FORMAL | \(\mathbf p=(3,3)\), \(\Delta=6\) while carrier/conductor grows | **not** a DIR growth family: pole mass stays fixed |

Here \(3^{\,2b}\) means \(2b\) copies of \(3\).  The coefficient-solved schemas
satisfy the filed local pole laws, N1, displayed local coefficient identities,
and terminal numerical gates.  They do **not** supply a compatible
local chart transition, a global boundary tree, or a polynomial Keller
realization.  In particular, none meets the question's stronger requirement
of pole data from an actual constant-Jacobian germ.

There are two logically separate possible growth axes:

1. **additive pole-mass growth:** \(td/(\alpha\beta)\to\infty\), already present
   formally at fixed type \((2,3)\);
2. **light-root concentration:** a fixed positive pole mass lands at roots with
   \(\mu_P/B\to0\).

The books realize neither axis at Keller tier.  The first is the stronger
formal lead: by (2), a Keller lift would make \(\max R_P\) unbounded regardless
of how its pole mass is partitioned.

### 4.2 What the pure-minor identity actually caps

At a proper root the exact identity has the form
\[
 \Delta_P=\alpha\beta B\mu_P-n_P,\qquad n_P\geq0.
\tag{6}
\]
It yields only
\[
 0\leq\sum_{\gamma\mid P}p_\gamma
       \leq\alpha\beta B\mu_P,\qquad R_P\leq B^2.
\tag{7}
\]
This kills the class-kill mechanism but is on the wrong \(B\)-scale for DIR.
Even a hypothetical bound \(\Delta_P\leq K\mu_P\) would give only
\[
 R_P\leq {KB\over\alpha\beta},
\]
still not a universal constant.

Since \(\Delta_P\) is integral, DIR(\(C\)) would in particular force
\(\Delta_P=0\) whenever \(B>C\alpha\beta\mu_P\).

The needed statement is:

> **CONJECTURE (root-pole cap \(C\)).**
> For every proper boundary root of a Keller map,
> \[
> \sum_{\gamma\mid P,\ {\rm pole}}p_\gamma
>       \leq C\,{\alpha\beta\mu_P\over B}.
> \tag{RPC}
> \]

RPC is exactly DIR(C), not a proof of it.  The missing step is a transfer from
the pure-minor/Smith thick-line data to rootwise displaced-intersection
retention.  The current ledger controls conductor/contact and supplies the
identity \(\Delta_\gamma=p_\gamma\), but it supplies no inequality coupling the
sum of these pole orders to \(\mu_P/B\).  Signed adjunction also leaves the
finite-end/compactification term uncontrolled.

## 5. Q3: verdict

**VERDICT: NEUTRAL at Keller tier; no finite \(C\) is supported.**

- The empirical envelope of numerically complete admissible tuples is
  \(C_{\rm obs}=4/3\), with equality at the filed residue-A root.  It is not a
  justified DIR constant.
- At book tier, \((2,3)\) rows carry the weighted lower bounds
  \(3/2,5/3,11/6,2\) through \(td=12\); the \(5/3\) and \(2\) off-axis rows
  remain unadjudicated.  Hence \(C=4/3\) is specifically unsupported as soon
  as one contemplates a Keller lift of those books.
- No banked row gives the missing \(B,\mu_P\), and root landing needed to turn
  those certificates into actual root tuples; no actual Keller growth
  direction has been exposed.
- The precise counterexample lead is the **fixed-\((2,3)\),
  bounded-denominator/unbounded-pole-mass direction**, most sharply the
  locally coefficient-solved family
  \([3A;A,1,2]^2\) with pole profile \((3A,3A)\).  A compatible pure-minor
  constant-Jacobian chart/tree realization would immediately contradict every
  DIR(C).  That realization is exactly what is absent.

Thus the decisive next truth test is not another conductor/contact estimate.
It is either (i) construct a genuine Keller chart/tree lift of that
unbounded-pole-mass family, or (ii) prove RPC by a new rootwise
pure-minor-to-displaced-intersection transfer.
