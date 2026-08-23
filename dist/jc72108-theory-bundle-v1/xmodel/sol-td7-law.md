LAW FOUND: **FULL for the local Prop. 8.1(iv) rigid solve; partial as a kill of the whole 62-cell book.**
CRITERION: a class-B/C cell is T1-DEAD iff \(d_p\mid d_q\), equivalently \(M=d_p\), equivalently \(\bar\kappa\in\{3,4\}\).
CELLS KILLED: **56/62** = the one class-B cell plus 55 class-C cells; this removes 1,636/1,689 deduplicated routes.
CELLS LEFT: **6/62**, all class C; they support 53 routes, including 35 of the 1,390 budget-equality routes.
CONFIDENCE: **high** — symbolic iff proof, exact 62-cell census replay, and explicit admissible solutions for all six exceptions.

# The td=7 generalized zero-chain law

Throughout, \(d_p:=\deg p\), \(d_q:=\deg q\), and
\(M=\gcd(d_p,d_q)\). I interpret the prompt's “kappa” as the book's pinned
quantity

\[
  \bar\kappa_G:=\kappa_G(1-\pi(G));
\]

I write it as \(\bar\kappa\) to distinguish it from the Puiseux denominator
\(\kappa_G\). Cell tuples below are in the book's order
\((d_p,d_q,\nu_G,M_G)\).

## Theorem

**Theorem (generalized zero-chain rigid law).** Let a pinned class-B or
class-C merge cell have

\[
 \mu:=d_p-\nu\geq 1,\qquad
 \ell:=\frac{d_q-1}{\nu}-1\geq 1,
\]

where \(\mu\) is the multiplicity of the arriving zero-direction chain and
\(\ell\) is the number of \(q\)-only nonzero \(\nu\)-orbits. Then its reduced
Prop. 8.1(iv) equation has an admissible polynomial solution with nonzero
right-hand constant if and only if

\[
                         d_p\nmid d_q.
\]

Equivalently, the cell is killed by its Prop. 8.1(iv) rigid solve iff

\[
 \boxed{d_p\mid d_q}
 \quad\Longleftrightarrow\quad
 \boxed{(\mu+\nu)\mid\bigl(\mu(\ell+1)-1\bigr)}
 \quad\Longleftrightarrow\quad
 \boxed{M=d_p}
 \quad\Longleftrightarrow\quad
 \boxed{\bar\kappa\in\{3,4\}}.                 \tag{LAW}
\]

The last equivalence is specific to the td=7 P3 class-B/C pins. It makes
the route-level test especially short: compute the already-pinned
\(\bar\kappa\); values 3 and 4 die, while values 5 and 6 pass the local T1
solve. Merge arity is \(r=2\) in every one of the 62 cells and does not
enter the law. The \(\lambda\)-data select which routes enter the finite
book, but do not enter this vertex-local equation.

This is a full decision law for the requested *local rigid solve*. It is a
partial panel kill because six cells pass that solve; no claim of global
realizability is made for those six.

## Proof

### 1. All 62 cells have one normal form

Prop. 8.1(iv) forces every root of \(p\) to occur simply in \(q\), every
\(q\)-root outside \(p\) to be simple, and, for \(\nu\geq2\),
\(\eta\mathbin\Vert q\). This is proved in *BOOK-OFFAXIS.md* §6, R1.0,
lines 209–224. The general merge radical shape is recorded in the same
file at §7, R2.2, lines 317–327.

For P3 classes B and C, chain 2 arrives at the zero direction, chain 1 is
the sole nonzero arriving orbit, and there are no non-chain \(p\)-orbits:
\(\sum m_j=0\). The degree pins are

\[
 d_p=\mu+\nu,\qquad d_q=1+(\ell+1)\nu,
\]

from *BOOK-OFFAXIS.md* §10, P3, lines 521–549. Thus, up to nonzero pattern
scalars, every one of the 62 targets has

\[
 t=\eta^\nu,\qquad A=c^\nu\ne0,
\]
\[
 p=\eta^\mu(t-A),\qquad
 q=\eta(t-A)s(t),\qquad \deg s=\ell.             \tag{1}
\]

Class B is simply the \(\mu=1\) member. “Class B” here is P3's arrangement
label, not the on-axis family-I label.

### 2. Prop. 8.1(iv) is a triangular ladder

After division by \(1-u\), Prop. 8.1(iv) is

\[
 \rho p q'-p'q=Cp,\qquad C\ne0,\qquad
 \rho=\frac{d_p}{d_q}.                            \tag{2}
\]

The normalization and the top-degree identity
\(\rho=d_p/d_q\) are stated in *cases/l1_ode_check.py* lines 5–15 and in
*SHEET6-L1.md* §1, lines 73–81. Substituting (1) into (2), cancelling
\(\eta^\mu(t-A)\), and absorbing harmless nonzero pattern scalars gives

\[
 E(t):=(\rho-\mu)(t-A)s
       +(\rho-1)\nu t s
       +\rho\nu t(t-A)s'=\widetilde C.            \tag{3}
\]

Put \(d:=\mu+\nu=d_p\), \(D:=1+(\ell+1)\nu=d_q\), and normalize
\(s(t)=\sum_{j=0}^{\ell}s_jt^j\) by \(s_\ell=1\). The coefficient of
\(t^{\ell+1}\) in (3) vanishes automatically because \(\rho=d/D\). For
\(k=\ell,\ldots,1\), the coefficient of \(t^k\) gives the nonsingular
triangular recurrence

\[
 s_{k-1}
 =A\,
   \frac{1+dk-\mu(\ell+1)}{d(k-\ell-1)}s_k.       \tag{4}
\]

The denominator never vanishes in this range. The constant term is

\[
 \widetilde C=A(\mu-\rho)s_0.                     \tag{5}
\]

Since \(A\ne0\), \(\mu\geq1\), and \(0<\rho<1\), equation (5) is nonzero
iff \(s_0\ne0\). Iterating (4),

\[
 s_0=A^\ell\prod_{k=1}^{\ell}
 \frac{1+dk-\mu(\ell+1)}{d(k-\ell-1)}.           \tag{6}
\]

Therefore \(\widetilde C=0\) iff there is a \(k\in\{1,\ldots,\ell\}\)
such that

\[
 dk=\mu(\ell+1)-1.                               \tag{7}
\]

The range condition is automatic when the divisibility holds. Indeed,
\(\mu(\ell+1)-1>0\), while \(D>d\), and

\[
 \mu(\ell+1)-1+D=d(\ell+1).                      \tag{8}
\]

Thus (7) occurs iff \(d\mid D\), i.e. iff \(d_p\mid d_q\). At the zero
pivot the forced polynomial is

\[
 s=t^k(t-A)^{\ell-k};
\]

in particular \(\widetilde C=0\), contradicting the required nonzero
constant in Prop. 8.1(iv). It also makes the failure visible in the root
law: \(q\) acquires excess multiplicity at both \(0\) and \(t=A\).

This is precisely the mechanism of the on-axis ZCH ladder. When
\(\mu=1\), \(d=\nu+1\), and \(d\mid D\) reduces to
\((\nu+1)\mid\ell\). The known law and its zero-pivot solutions are in
*BOOK-BASH-R2.md* §0, lines 31–37, and §2, lines 80–130. Hence (LAW) is
an exact off-axis generalization, not a pattern fitted to the cell list.

### 3. The converse is also exact

Suppose \(d_p\nmid d_q\). No numerator in (4) vanishes, so the unique
monic \(s\) has \(s_0\ne0\), and (5) gives
\(\widetilde C\ne0\). The remaining root conditions follow directly from
(3), with no genericity assumption:

* at \(t=0\), nonzero \(\widetilde C\) gives \(s(0)\ne0\);
* at \(t=A\), it gives
  \(\widetilde C=(\rho-1)\nu A s(A)\ne0\), so \(s(A)\ne0\);
* at any root \(b\) of \(s\), it gives
  \(\widetilde C=\rho\nu b(b-A)s'(b)\ne0\).

Consequently every root of \(s\) is nonzero, different from \(A\), and
simple. Hence \(q\) has exactly the simple-root anatomy required by R1.0.
This proves both directions of the theorem. It is a linear triangular
solve, not a Gröbner computation.

### 4. Reduction to the pinned κ-law

The chain-1 handshake gives \(X=\bar\kappa-2\), and the cell ratio gives
\(X/\bar\kappa=d_p/d_q\); see *BOOK-OFFAXIS.md* §7, R2.1, lines 301–315,
and §10, P3, lines 521–545. Therefore

\[
 \frac{d_q}{d_p}=\frac{\bar\kappa}{\bar\kappa-2}. \tag{9}
\]

Here \(\bar\kappa\) is an integer greater than 2 (the characteristic-vertex
integrality is derived in *SHEET6-III.md* §3, lines 121–129). Thus
\(d_p\mid d_q\)
iff \(\bar\kappa/(\bar\kappa-2)\) is integral, iff
\(\bar\kappa-2\mid2\), iff \(\bar\kappa\in\{3,4\}\). Prop. 8.1(v) gives
\(M=\gcd(d_p,d_q)\), so the equivalent test \(M=d_p\) follows as well
(*BOOK-OFFAXIS.md* §7, R2.2(D), lines 327–331).

## Exact verdict on the 62 cells

*BOOK-OFFAXIS.md* does not print the 62 tuples individually. It states
the count and tuple convention in §10, P4, lines 578–606. The exact list
below is reconstructed from the book-cited standalone generator/reproducer:
*cases/scratch_offaxis_pricing/px5.py* lines 123–150 (class-C cells),
217–251 (B/C traversal), and 254–262 (route deduplication). Thus the list
is reproducible, but it should not be mistaken for a literal table in the
Markdown book.

### Killed class B: 1 cell

\[
 (d_p,d_q,\nu,M)=(3,9,2,3),\qquad
 \mu=1,\quad \ell=3,\quad\bar\kappa=3.
\]

This specializes to the old ZCH test \(3\mid3\). The one *class-B cell*
has 18 deduplicated priced completions (14 at budget equality); “single
class-B route” in the prompt is therefore accurate only if “route” means
merge cell.

### Killed class C: 55 cells

The 30 cells with \(\bar\kappa=3\) are

~~~text
(5,15,2,5), (7,21,2,7), (7,21,4,7), (7,21,5,7),
(9,27,2,9), (11,33,2,11), (11,33,4,11), (11,33,8,11),
(12,36,5,12), (12,36,7,12),
(15,45,2,15), (15,45,4,15), (15,45,11,15),
(17,51,10,17), (19,57,8,19), (19,57,14,19),
(22,66,13,22),
(27,81,10,27), (27,81,16,27), (27,81,20,27),
(32,96,19,32), (35,105,26,35), (42,126,25,42),
(43,129,32,43), (51,153,38,51), (52,156,31,52),
(62,186,37,62), (67,201,50,67), (83,249,62,83),
(99,297,74,99)
~~~

The 25 cells with \(\bar\kappa=4\) are

~~~text
(5,10,3,5), (8,16,3,8), (8,16,5,8), (11,22,7,11),
(13,26,5,13), (14,28,3,14), (14,28,9,14),
(17,34,11,17), (18,36,5,18), (18,36,7,18),
(20,40,13,20), (23,46,15,23), (26,52,17,26),
(28,56,11,28), (29,58,19,29),
(32,64,9,32), (32,64,21,32),
(38,76,15,38), (38,76,25,38),
(44,88,29,44), (50,100,33,50), (56,112,37,56),
(62,124,41,62), (68,136,45,68), (74,148,49,74)
~~~

Every displayed killed tuple has \(M=d_p\), as (LAW) predicts.

### Left by Prop. 8.1(iv): 6 class-C cells

Keeping the arbitrary nonzero scale \(A\) visible, the six non-killed cells
have the following explicit monic solutions. The
shown \(\widetilde C\) uses the normalization of (3).

| cell \((d_p,d_q,\nu,M)\) | \(\mu\) | \(\ell\) | \(\bar\kappa\) | forced \(s(t)\) | \(\widetilde C\) |
|---|---:|---:|---:|---|---|
| \((9,15,7,3)\) | 2 | 1 | 5 | \(t-\frac23A\) | \(-\frac{14}{15}A^2\) |
| \((10,15,7,5)\) | 3 | 1 | 6 | \(t-\frac12A\) | \(-\frac76A^2\) |
| \((15,25,8,5)\) | 7 | 2 | 5 | \(t^2-\frac23At-\frac19A^2\) | \(-\frac{32}{45}A^3\) |
| \((15,25,12,5)\) | 3 | 1 | 5 | \(t-\frac23A\) | \(-\frac85A^2\) |
| \((18,27,13,9)\) | 5 | 1 | 6 | \(t-\frac12A\) | \(-\frac{13}{6}A^2\) |
| \((39,65,32,13)\) | 7 | 1 | 5 | \(t-\frac23A\) | \(-\frac{64}{15}A^2\) |

All constants are nonzero because \(A\ne0\). The linear roots are visibly
nonzero and different from \(A\). In the sole quadratic case the roots
are \(A(1\pm\sqrt2)/3\), with discriminant \(8A^2/9\ne0\), and neither is
0 or \(A\). These six therefore genuinely pass the complete local rigid
solve; they are not merely failures of the divisibility kill.

## Route and budget effect

The local law is constant on all priced routes carrying the same merge
cell. Applying it to the deduplicated P4 route book gives

| outcome | cells | routes | budget-equality routes |
|---|---:|---:|---:|
| class B, killed | 1 | 18 | 14 |
| class C, killed | 55 | 1,618 | 1,341 |
| class C, left | 6 | 53 | 35 |
| total | 62 | 1,689 | 1,390 |

The budget inequality and the meaning of \(\psi\) are in
*BOOK-OFFAXIS.md* §10, P1, lines 486–500; the merge/trunk accounting is in
P2, lines 502–519; P4 gives the survivor totals at lines 551–606. The
\(\lambda\)-charges matter only before and after the local merge solve:
none occurs in (2)–(6). Thus the law kills every route through the 56
dead cells without inspecting its particular chain or terminal.

There are two route-count conventions in the sources. The generator reports
1,713 raw records and 1,689 after deduplication; the raw equality
count 1,413 is computed at *cases/book_offaxis.py* lines 881–893. The
corresponding deduplicated equality count is 1,390. *BOOK-OFFAXIS.md* P4
lines 587–603 uses the deduplicated figures, while its reproduction note at
lines 648–667 reports the raw engine figures. This explains the apparent
1713/1689 and 1413/1390 discrepancies. The three outcome rows in the table
above are obtained by parsing the deduplicated `lam=... <= budget=...`
lines by B/C cell and testing equality of the two printed integers.

## Interaction with the other requested ingredients

* **Primitivity.** The prompt attributes the L6 law
  \(\gcd(\bar\kappa_V,\nu_V)=1\) to *SHEET6-LROOT.md*, but that file contains
  no L6 statement. The actual proof is *SHEET6-III.md* §3, lines 121–129,
  and the synthesis is *TEMPLATE-ATTACK.md* §1a, lines 58–70. Since P3 has
  \(\nu_G\ge2\), it applies to all 62 merge cells. All 62 already pass it:
  it kills none of the six exceptions and none of the 56 cells killed by
  (LAW). This is a census sanity check, not an ingredient in the new
  ladder.
* **Depth closure.** *SHEET6-DEPTH.md* defines
  \(w=(\bar\kappa-\rho)/\nu\) in §1, lines 67–77, proves the nonzero-edge
  handshake in §5a, lines 218–233, and gives the \(\mu=1\) case-III
  zero-edge prototype in §5c, lines 253–277. *BOOK-OFFAXIS.md* R2.1,
  lines 301–315, is the general-\(\mu_0\) handshake used by class C; P3
  specializes it. Together these relations pin
  \(\bar\kappa,X,d_p,d_q\) before the present solve. DEPTH itself explicitly
  leaves the Prop. 8.1(iv) coefficient layer out of scope in §9, lines
  403–422.
* **T1/template mechanism.** *SHEET6-TEMPLATE.md* §2b, lines 156–165,
  illustrates the same vertex-local coefficient-solving principle. Its
  E5 calculation and corrected \(w_i^4\) formula are at §2c, lines
  226–244; that formula is explicitly solvable and non-obstructive there.
  It is specific to the td=6 pole-to-merge template and is not assumed for
  these td=7 cells. The new law is scale-independent, so pinning the
  nonzero scale \(A\) cannot change its zero/nonzero verdict.
* **Root budget.** *SHEET6-LROOT.md* actually proves the case-IV result
  \(\lambda_{\rm root}=0\) in §2, lines 100–126, and the x-side budget
  rigidity in §3, lines 136–160. Those facts concern terminal accounting,
  not the merge-local equation (2).
* **On-axis comparison.** The generalized ZCH law specializes exactly to
  \((\nu+1)\mid\ell\). The on-axis family-I law is irrelevant here because
  every P3 class-B/C merge has \(\nu_G\ge2\); no family-I extrapolation is
  used.

No **CONJECTURE** is used in this report. The remaining six cells are
proved local T1 survivors only; whether another local, transport, or
global mechanism kills them is outside this theorem.

## Reproduction

The exact distinct class-C tuples can be recovered from the generator's
already-deduplicated printed route lines by

~~~sh
cd /Users/dc/code/math/jc72108
python3 cases/scratch_offaxis_pricing/px5.py > /tmp/px5.out
perl -ne 'while (/C mu0=(\d+).*?cell\((\d+),(\d+)\)nu(\d+)M(\d+)/g) { print "$1 $2 $3 $4 $5\n" }' /tmp/px5.out \
  | sort -nu -k2,2 -k3,3 -k4,4 -k5,5 > /tmp/td7-C-cells.txt
wc -l /tmp/td7-C-cells.txt
~~~

The result is 61 lines with columns
\((\mu,d_p,d_q,\nu,M)\). For each line compute

~~~text
ell   = (dq - 1)/nu - 1
kbar  = 2*dq/(dq - dp)
dead  = (dq % dp == 0)
~~~

This returns 55 dead and the six explicit exceptions above. Adding the
class-B tuple \((3,9,2,3)\) returns the stated 56/62 verdict.
