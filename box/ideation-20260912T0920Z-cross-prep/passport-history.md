\((3)\) and \((3)\); because they lie over the same point of \(\mathbb{P}^1\)
the geometrically correct object is the single permutation
\(\sigma_\infty=(1\,2\,3)(4\,5\,6)\) of type \((3,3)\). The two writings
differ by a Hurwitz move that does not change the existence question.

Each 3-cycle is an even permutation, so \(\sigma_\infty\) is even. Its
ramification contribution is \((3-1)+(3-1)=4\).

### 1c. x-side cluster (LR2 + T2c) \(\to\) 42 places of \(e=2\), types \((2),(2,2),(2,2,2)\)

LR2 (SHEET6-LROOT.md §3): the x-component of \(T_a\) carries exactly one
cv-vertex \(G\), with \(\kappa_G=1\). All 42 x-side Puiseux series form a
single cluster (pairwise contact \(\ge\pi_G\ge R=3\)), with no
characteristic exponent below \(\pi_G\).

CLASSICAL T2c squeezes the remaining slack: contacts are integers in units
of \(v=1/y\), each \(\ge 3\), and \(g\) finite forces the per-series contact
sum \(U_i\in\{123,124\}\), hence \(\pi_G\in[3,3+2/41)\). Combined with
integer contacts, the first split is at height **exactly 3**. (The St 9.4
integrality \(\kappa(\pi-1)\in\mathbb{N}\) gives the same pin
\(\pi_G=3\), but is not needed: T2c + integrality of contacts suffice.
This is the Sigray-free half of the x-side input; LR2 is used only as the
already-established single-cluster pin the mission statement asks for.)

Write the x-expansion at the point \([0:1:0]\) as
\(x=c_0'+a_3 v^3+a_4 v^4+\cdots\) (the coefficients of \(v^1,v^2\) vanish,
or else \(g\to\infty\) and the leftover td is not \(3+3\)). The 42 series
are the 42 choices of leading coefficient \(a_3\). The leading form of
\(f-a\) at this point is \(q\,a_3^{42}+\text{lower}=a\) with \(q\neq 0\)
(vanishing order of the \(y^{126}\)-form of \(f\) at \(c_0'\) is exactly 42,
or else \(\pi_G>3\)). For generic \(a\) this is a degree-42 equation with
42 distinct simple roots: **42 distinct \(a_3\)**, each a holomorphic branch
of \(x\) as a function of \(v\), hence a place of degree \(n=1\).

Contact between any two is exactly 3, so \(U=41\cdot 3=123\) and
CLASSICAL's T2 formula gives

\[
e'=n(125-U)=1\cdot 2=2.
\]

A group of \(m\) series sharing the same \(a_3\) (a multiple root of the
pattern at \(G\)) would have \(U\ge 4(m-1)+3(42-m)=m+122\). The window
\(U\in\{123,124\}\) forces \(m\le 2\). Multiplicity \(\ge 3\) pushes
\(U\ge 125\), and \(g\) is no longer finite of positive order. So the only
specialisation of \(p_G\) away from 42 simple roots is a mixture of simple
and double roots, which can only *lower* the number \(t\) of ramified
x-places (a double root either stays one place of \(e=2\), or splits into
two unramified \(e=1\) places). The generic — and, given the leading form
of \(f\), forced-for-generic-\(a\) — count is \(t=42\).

**Degree budget of \(\hat g\).** At each finite value the ramification
indices of all preimages sum to 6. Affine preimages are unramified
(\(J=1\)), so the infinite places over one value contribute a total of at
most 6. Each ramified x-place has \(e=2\), so at most three of them may
share a \(g\)-value. The local monodromy at that value is then of type
\((2)\), \((2,2)\), or \((2,2,2)\) (plus fixed points). Hence the generic
x-side passport is

\[
(2)^a\,(2,2)^b\,(2,2,2)^c,\qquad a+2b+3c=42,
\]

and there are at least \(\lceil 42/3\rceil=14\) distinct x-side \(g\)-values.
The engine counts 169 nonnegative integer solutions \((a,b,c)\).

Two configurations **die here, by the degree budget, with no appeal to
\(S_6\)**:

- Unsplit cluster (one \(g\)-value for all 42 places): \(\sum e=84>6\).
- Pure leading-form collapse \(L(a_3)=c\,a_3^{63}\) (the \(y^{189}\)-form
  of \(g\) alone). On the 42nd-roots of the fibre equation this takes
  exactly two values, 21 places each: \(\sum e=42>6\).

Neither is forced. The actual limit of \(g\) along an x-branch is a
polynomial \(L(a_3)\) of degree 63 (leading coefficient nonzero because
