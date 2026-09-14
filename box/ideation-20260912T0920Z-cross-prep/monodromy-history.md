
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
