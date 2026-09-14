Complete coefficient DAG on the normalized necessary chart
=========================================================

The executable construction is boundary_full_dag.py. Its JSON receipt states
whether every phase completed. No partial receipt is a complete ideal, and
no circuit-count or evaluated residual is a properness certificate.

The target completion map factors exactly three affine parameters. It writes

    Y=F-(bG+c)/2, X=G+(a+b^2/4)/3,
    R=X^3+pX+q-Y^2.

Its inverse is polynomial over Q. Renaming X,Y to G,F gives the normalized
family used by the driver. Each target addition has strictly smaller major
and minor pole order than the polynomial it changes. Constants have order0,
whereas all relevant pole bounds are negative. Thus both complete boundary
faces, monic top forms, and total degrees are preserved. The Jacobian is
preserved by the target map of determinant1 in the (F,G) order. The old
source coefficient scheme is the normalized scheme times its three affine
target parameters, with every other equation transported through this map.
This is not an extra source translation or a fourth gauge.

For delta5/2 the exact G boundary map has65 coefficient generators over
A=Q[minor_u,minor_v,c]. It retains c freely until the required localization.
Let T=A[g_1,...,g_65]. The driver constructs every F coefficient and the
normalized target scalar p as polynomials in T, and R's leader lambda as
another polynomial in T. The target constant q is a separate free factor.
The total generator count before residual equations is therefore69.

Write G=sum_{r=0}^66 x^(66-r)G_r(w) and F=sum_{r=0}^99 x^(99-r)F_r(w),
w=y/x. Their fixed tops are P^2,P^3 with P=w^9(w-1)^24. At characteristic
ambient depth1<=r<=99, pG and q have not appeared. The row is

    N_r(w)-2F_0(w)F_r(w),
    N_r=(G^3)_r-sum_{i+j=r, i,j>0}F_iF_j.

Divide N_r by the monic polynomial F_0 in T[w]. Set F_r equal to one half
of the quotient and retain every coefficient of the remainder as a residual
equation. This is a polynomial coordinate graph; w is not localized, and
the remainder is not discarded. The omitted higher coefficients of the
original row vanish by the monic-division identity. The quotient degree
is at most99-r, so every F strip is within its total-degree triangle.

Beyond r=99 there are no further F coordinates. At r=132 the normalized pG
term first appears. Its leading w coefficient is p because G_0 is monic.
Solve p as minus the corresponding coefficient of G^3-F^2, retaining every
other row. All characteristic depths through142 must vanish. At depth143
set lambda equal to the leading w coefficient; retain the complete degree55
polynomial and all lower degree coefficients of R. The optional q merely
adds to R's constant; none of the retained negative faces, upper rows or
Jacobian rows depends on it.

The driver then emits all major and minor F rows, all major and minor R
rows, and every coefficient of J(F,G)-C through constant depth163, with

    C=-455*lambda/243.

The R major face is the exact transported P*q_face. The R minor target is
lambda*(pi*(pi^2-c))^5. Every centre term is included by the previously
proved boundary row formula. The source G boundary rows have already been
solved by their exact two-way map and independently replayed.

Each original source coefficient maps to its constructed circuit. Conversely
each g_i maps to its original retained G coefficient class; p and every F
coefficient are forced by the monic-division identities in descending degree.
These two maps are inverse after quotienting by ALL retained residuals.
Lambda is a derived coefficient, and the distinguished element is c*lambda.
The exact question is whether the ideal obtained by adjoining
z*c*lambda-1 is unit. The DAG receipt does not answer that question by itself.

For108 the analogous lengths are108/72, R degree63, p introduction144,
leader depth153, and Jacobian constant178. Its minor target is explicitly
-lambda*((pi-mu)^2-c)^7 and its mean mu remains free. For99 delta2 the
minor target is lambda*(zeta^2*(zeta+3*rho))^5. These modes exist in the
driver but are not claimed executed unless their own receipts say so.

The driver retains formal arithmetic circuits over Q, with two independent
exact rational evaluations attached only as arithmetic controls. Those
assignments need not satisfy the retained residual ideal and are never
called chart survivors. A digest commits to every residual coefficient in
its fixed block order; deterministic rerunning reconstructs the complete
list without writing an artifact tree. Literal nonzero constant detection
is reported separately, but a nonzero numerical evaluation of a nonconstant
residual is not a unit-ideal certificate. CPU and address-space limits are
840/900 seconds and1900MiB; bounded termination is explicitly typed.

Canonical source addon
----------------------

`boundary_canonical_addon.py` replays the same F/G/R coefficient construction
with hash-only arithmetic. Rational-constant simplification and every formal
operation are unchanged; numerical evaluations are disabled. It must match
the original G coefficient-map hash, p/lambda hashes, every characteristic
remainder hash, and every F/R boundary hash before composing new source rows.
The previously completed Jacobian receipt is bound by its complete file hash.

The adapter then recomputes the canonical monic degree33 and degree11 roots
from the normalized F, using the same `Source` routines as the independent
transverse-source construction. It recovers A2,A3,B1,B2,C2,C3 by monic
division. It retains the F/G D1 rows, all h2/h3 major and minor rows, the
h2 D1 rows, every remainder major/D1/minor row, and all remainder degree
overflow rows. There is no invented h3 D1 condition. The separated variable
called c_sep in Source's independent chart maps explicitly to this chart's
c; the normalized physical F/G coefficients are supplied directly, so no
extra diagonal or source translation is introduced.

Every new row is a polynomial in the same68 occurring generators. The free
q makes69 before localization; since q occurs nowhere in these rows or in
c*lambda, it can be factored out for the unit test. The one Rabinowitsch
variable then gives69 occurring generators for the exact decision ideal.
The addon receipt must say COMPLETE before its entire streamed source list
is counted as executed. Its circuit hashes constitute a reconstructed ideal,
not an ideal-membership decision.

Executed delta5/2 receipts: the evaluated boundary/characteristic/Jacobian
DAG completed46,770,392 arithmetic operations and retained33,135 coefficient
rows in760.15 wall seconds, with102,672KiB peak RSS. The canonical addon
then completed55,630,180 replay/composition operations in385.215 CPU seconds,
with105,488KiB peak RSS. All146 replay blocks and19,605 replay coefficients
matched exactly. Its30 new blocks retain40,906 more rows, including the
distinguished localizer. The composed full normalized source presentation
therefore retains74,041 rows. These are row counts, not ranks. Neither
receipt found a literal rational constant obstruction; neither performed
the required unit/properness computation.
