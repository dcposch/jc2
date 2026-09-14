# D108: translation inside the characteristic calculation is a valid basis change

This is different from setting jet0=0 in the source chart. The latter
fails the covariance control in `d108-translation-audit.md`. The
construction below keeps jet0 free and leaves the original minor
incidence and pole equations in their original coordinates.

Let `s=jet0` be an unchanged scalar coefficient-ring variable. On
physical polynomials define `T_s P(x,y)=P(x+s,y+s)`. Its inverse is
T_-s. For a polynomial normalized using its ambient degree N,

\[
t^rz^q\longmapsto t^rz^q(1+st)^{N-r-q}.
\]

All exponents are nonnegative because the full coefficient triangle
is used. Thus this is a polynomial coefficient map over Q[s], with
polynomial inverse and no localized variable denominator.

Keep the old h, its source coefficient graph, and all old minor
parameters. Compute `h'=T_s h` as an expression. Replace the free
outer coefficients by coordinates for `D'=T_s D` and `C'=T_s C`.
The declared inverse map is

\[
D=T_{-s}D',\qquad C=T_{-s}C',
\]

with all other old parameters fixed. The characteristic polynomial
built using h',D',C' and unchanged scalar target coefficients is
exactly T_s of the original characteristic polynomial. Its total
degree bound and specified highest homogeneous form are equivalent
under translation; its scalar leader lambda is unchanged. No jet,
minor-face polynomial, or source gauge is normalized by this step.

## The existing outer linear coefficient spaces are invariant

For D108 the source constraints on each outer block are its full
degree triangle, q cap 35, D2 floor `W=4r+5q>=W0`, and the D1
prefix moments at offsets 0,...,stage:

\[
\sum_{4r+5q=W}\binom qk c_{r,q}=0,
\qquad 0\le k<E_0-2W.
\]

Translation preserves the triangle and q cap. It only increases r,
so preserves the D2 floor. For the new moment at W,k, the term
arising from translation power l uses old weight `W'=W-4l` and
multiplies its old coefficient by

\[
\binom qk\binom{N-W'/4+q/4}{l}s^l.
\]

The q-factor is a polynomial over Q of degree at most k+l. Express
it in the binomial basis `binom(q,j)`, j<=k+l. If W'<W0, every
coefficient involved is zero by the D2 floor. Otherwise W' is an
earlier included prefix weight, and its available moment indices
satisfy

\[
j<E_0-2W'=E_0-2W+8l.
\]

Since the new row has `k<E0-2W`, all j<=k+l are within that bound.
Therefore every new moment is a polynomial combination of existing
old moments and D2 zero coefficients. The same calculation with -s
proves inverse invariance. Thus using the same rational linear
parameter basis for D' and C' is valid, with the stated forward and
inverse maps. An implementation should bind this map to its actual
solved basis or perform the argument in the full coefficient ring
before transporting the rational graph map.

The front conditions `D_r=0` for r<=30 and `C_r=0` for r<=62 are
also preserved, since translation only raises r. D31 and C63 are
unchanged on that locus, so the optional retained-tau shapes
`D31=tau*z31*(1+z)^4`, `C63=3*tau^2*z34/8` are preserved as well.
No choice of tau or a component is introduced.

## Why the finite original pole rows can remain untouched

After the proved front preprocessing and the constant B1 reduction,
the earliest effective outer contribution to normalized F or G is
at t32; the constant B1 contribution starts at t36. Substitution of
the old minor arc, whose w-coordinate has positive t-order, cannot
lower that exponent. Hence the stage-0–8 pole rows through local
power 12 involve only the original h2. They may be retained
unchanged in the old variables. Likewise the tested shallow
Jacobian bands are already consequences of the characteristic
total-degree bound. If deeper source rows later reach an outer
term, those rows must explicitly use the inverse images
`D=T_-s D'`, `C=T_-s C'`; they must not silently use D',C' as old
coefficients.

The characteristic calculation may consequently gain the simpler
translated h coefficient expression without transporting the
physical minor face. This is an invertible algebraic presentation
of the same equations, not a source-chart jet0 slice or an added
Keller assumption. Jet0 remains a free original coordinate.

## Independent review of the two accompanying theorems

`nondegeneracy-theorem.md` remains correct under its explicit top,
D2-face, and actual-degree hypotheses. Its use of a common
polynomial generator is supplied by the audited primary Lemmas
4–5 of Arzhantsev–Petravchuk. All degree-divisibility and local
face-power steps are valid over every algebraically closed
characteristic-zero point field. The original minor mean issue
does not enter that conditional polynomial theorem.

`full-characteristic-keller-theorem.md` also survives review. The
formal derivative induction uses actual **total** degree at every
index, scalar target coefficients, and the unique equality-weight
term's missing highest factor. Its nonzero first derivative term
therefore cannot cancel. The total-degree necessity for all
effective indices comes from the explicit root minimum in the
printed p172 proof, rather than extending the p169 common-top
assertion past its stated i<r range. The last characteristic
polynomial is not assigned the earlier common top. The final
exclusion of J=0 uses the characteristic gcd dividing 2 and the
unequal two-point top. Both appendices correctly distinguish a
conditional theorem or abstract algebraic point from an exhibited
Keller pair or a completed computation.
