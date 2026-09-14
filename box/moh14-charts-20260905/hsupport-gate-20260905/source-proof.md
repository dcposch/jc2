# Source and algebra note: h-support gate

This note separates the centered D1 calculation from a necessary chart for an
actual descended pair. It proves a safe completion using the largest common
root disc. It does not assert a Gröbner verdict or close the bounded Jacobian
conjecture. The ten charged inputs were mechanically hash-verified by the
coordinator before this source audit.

## 1. Source statements actually used

Primary source: `refs/moh1983_jram340_configurations_of_roots.pdf`.
Printed page = PDF page minus 139; PDF pages below are one-indexed.

* Printed pp.147–148 / PDF8–9: Proposition 1.2 identifies the multiplicity
  of a general disc point with its number of roots; the proof computes a
  polynomial's order by summing the orders of its linear factors.
  Text anchors: `box/depth-drivers-20260902/moh.txt:373–391`, `425–440`.
* Printed p.148 / PDF9: the approximate root is the polynomial part of the
  formal root at y-infinity. Text: same file, `463–468`.
* Printed p.149 / PDF10: Theorem 1.1 transfers a coherent complete system's
  multiplicities to an approximate root, provided the root index divides
  every multiplicity. Definition 1.5 and Theorem 1.2 require a common
  coherent complete system and a quasi-approximate root. For
  `F=h^d+sum_j a_j h^(d-j)`, they give `deg_y a_j<deg_y h` and
  `ord a_j(sigma_i)>=j lambda/d`. They do not give a total-degree bound or
  an x-width bound. Text: same file, `478–507`. The printed equation was
  visually checked because parts of the OCR equation are missing.
* Printed p.171 / PDF32: the Remark following Proposition 4.6 explicitly
  treats `J(f,g)=x^ell`. It replaces condition (3) by
  `lambda=(-1-ell+delta)/(n-m_r)` and the corresponding strict inequalities
  for earlier indices. Text: same file, `1709–1715`; the equation was
  visually checked in the PDF. A nonzero scalar multiplying the Jacobian
  changes leading constants, not any valuation in this calculation.
* Printed pp.173–175 / PDF34–36: Proposition 5.1 constructs the disc
  containing all roots of `g product_i T_i`. The p.174 Definition–Remark
  drops a terminal `M_h=n-1`. Text: same file, `1813–1841`, `1877–1918`.
* Printed p.179 / PDF40: Definition 5.1(1) counts the roots in each major
  disc; (3) gives the logarithmic radii; (4) writes the general point as
  `sum_j a_j t^j + pi t^delta_i`, including its center. The note after the
  definition says that `D_s` contains all roots of `g product_i T_i`.
  Text: same file, `2111–2146`. This page was visually checked.
* Printed p.188 / PDF49: Proposition 5.6 makes
  `sigma_1=pi t^delta_1` an additional hypothesis. It does not assert that
  every first major disc already has this center. Text: same file,
  `2611–2619`; the printed formula was visually checked.
* Printed pp.197–198 / PDF58–59: Proposition 6.3 gives descended
  polynomials in `(gamma,pi)`, monic in pi, with their specified pi-degrees,
  and Jacobian `-u_s/b * gamma^(v_s-u_s-1)`. It does not identify total
  degree with pi-degree. Proposition 6.4 licenses this descent when
  `u_s=1` under its source hypotheses. Text:
  `box/recvatlas-20260905/cohort/moh-p196-198.txt:64–92`, `147–168`.
  Printed p.197 was visually checked.

The charged compiler implements the source-to-child characteristic map in
`/tmp/jc2-lane.zzLFCU/inputs/sprime3_compiler.py:113–154`. Its terminal-radius
and D1 data are in `157–174`. This note consumes that already charged
descent identification; it does not identify an old source disc with a
child disc merely because the indices have similar names. The child disc
below is reconstructed for the child pair and its effective characteristic
data using the monomial-Jacobian version of the order calculation.

## 2. What the centered D1 calculation proves

Use the user's monomial convention `y^a x^b`; the compiler stores a
monomial as `(b,a)`. Put `t=x^-1`, let pi be transcendental over the
coefficient field, and suppose that the general point really is
`sigma=pi t^delta_1` in the polynomial coordinate being used. Then

`ord F(t^-1,sigma)=min_{c_ab!=0}(a delta_1-b)`.

There is no cancellation at the minimum: different a give different
powers pi^a, and for a fixed a the minimum t-exponent determines b.

For a monic polynomial h of y-degree K and the threshold

`B=V_2 delta_1+(K-V_2)delta_s`,

the full centered D1 coefficient space is exactly

`h=y^K+sum h_ab y^a x^b`,

`0<=a<K, 0<=b<=floor(a delta_1-B)`.

An empty inner range contributes no monomials. The monic term is allowed
because `K delta_1-B=(K-V_2)(delta_1-delta_s)>=0`. The sum is finite without
any total-degree or x-width cap. At coefficient deficit i the analogous
centered D1 inventory uses `floor(a delta_1-iB)`.

For a source quasi-approximate root with V_2 roots in D1 and all K roots in
Ds, the product formula gives

`ord h(sigma_1)=V_2 delta_1+sum_outer ord(sigma_1-rho)>=B`.

The interior roots contribute delta_1 and the remaining root separations
are at least delta_s. Obtaining that root distribution for the chosen
approximate root uses the coherent-system/multiplicity hypotheses of
Theorem 1.1; obtaining the coefficient inequalities uses Theorem 1.2.
Neither theorem silently removes the center in Definition 5.1(4).

The old restrictions `a+b<=K` and `b<=K-V_2` appear in frozen
`sprime3_compiler.py:186–205`. Its explanation at `189–193` justifies a
divisibility condition on a degree-K face, then applies the restriction to
every lower term. Frozen `moh14-fullorder-grok46-20260905.md:205–208`
calls this a Newton width without giving the missing source implication.
The older `box/orderbasis-20260903/order_basis_full.py:190–198` has the
same caps. Agreement with that earlier loop is not a proof.

No group element establishing those two caps has been supplied. A target
translation changes only a terminal alpha or beta constant. It cannot
remove a coefficient of h. Nor is changing h while fixing Q a free gauge:
with beta_1=0, h is the unique q-th approximate root of Q. A polynomial
source shear in y can move h coefficients, but preservation and coverage
must be proved for the entire resulting support; its mere existence does
not justify deleting arbitrary coordinates.

## 3. A center countercontrol, and its exact logical scope

On the numerical data `K=4`, `delta_1=9/4`, `delta_s=-2`, `V_2=1`,
`B=-15/4`, consider

`h=y(y-x^2)^3+x^5`.

It is monic of y-degree four. Put `x=t^-1` and
`sigma=t+pi t^(9/4)`. Direct substitution gives leading term
`-pi t^(-15/4)`, so `ord h(sigma)=-15/4`. Equivalently, setting
`t=z^4` gives lowest z-exponent -15 with coefficient -pi; this was
checked by exact SymPy expansion. However the raw monomial `x^5` has
centered weight -5, below B. Thus it is omitted even by the uncapped
centered D1 inventory.

The root near t has expansion beginning `t+3t^4+...`; the other three
roots begin at order -2. This exhibits the relevant one-inner/three-outer
root behavior at the displayed coarse disc levels. It is a counterexample
to deducing raw weight support solely from a bound at a nonzero-center
disc. It is not a source-realized characteristic tower, descended
monomial-Jacobian pair, or Keller counterexample.

In particular the center issue must not be advertised as settled just by
adding the 76 raw D1 coordinates. There is no need to classify exactly
which actual child centers are possible to make the safe repair below.

## 4. The largest-disc bound for the monomial-Jacobian child

Write the descended pair as P,Q, with

`deg_y P=n=eK`, `deg_y Q=m=qK`, `K=gcd(n,m)`, `e>q>=2`,
`J(P,Q)=c x^ell`, `c!=0`.

In Proposition 6.3 these are respectively the descended g and descended
T_1. Both are among the polynomials covered by the largest-disc statement
in Proposition 5.1 and Definition 5.1. We need only that both root sets
are contained in Ds, not that Ds is already the smallest disc for just
their product; other characteristic polynomials can enlarge it.

Here is the terminal radius calculation, distinguishing the source input
from the elementary specialization. At the terminal effective index,
Moh's order relation uses the denominator `n-M_s`. At a generic point of
the disc containing all roots, each monic polynomial of y-degree N has
order N delta_s, so the normalized order lambda is delta_s. The p.171
monomial-Jacobian relation therefore specializes to

`delta_s=(delta_s-(ell+1))/(n-M_s)`.

Solving gives

`delta_s=-(ell+1)/(n-M_s-1)`.

This is the terminal instance of the charged Phi_eff formula. The
replacement of -1 by `-(ell+1)` is explicitly sourced at p.171; in the
underlying t-order identity it also follows from
`J_{t,y}(P,Q)=-c t^(-ell-2)`. The construction of the root disc, as
opposed to this final arithmetic identity, is the Proposition 5.1 source
step. The p.174 drop is a no-op on all twelve charged children.

The resulting positive number `d=-delta_s` is the same on every V-fibre
of a class:

| Class `(n,m; M_2,...,M_s; ell;s)` | d |
|---|---:|
| `(16,12;6,13;3;3)` | 2 |
| `(18,12;2,9;2;3)` | 3/8 |
| `(24,16;-12,-2,5;1;4)` | 1/9 |
| `(24,16;12,17;1;3)` | 1/3 |
| `(24,18;-15,14;1;3)` | 2/9 |
| `(24,18;9,20;1;3)` | 2/3 |

## 5. An explicit polynomial group element

Let N=qK and write the Q-roots, with multiplicity, as rho_1,...,rho_N
in the Puiseux field. Their mean is the polynomial

`eta(x)=(sum rho_i)/N=-[y^(N-1)]Q/N in k[x]`.

If Ds has a center a, then `ord(rho_i-a)>=delta_s`. Characteristic zero
gives `ord(N)=0`; ultrametricity gives `ord(eta-a)>=delta_s`. Therefore
every root rho of either P or Q satisfies

`ord(rho-eta)>=delta_s`.

Apply the actual polynomial automorphism

`phi:(x,y)->(x,y+eta(x))`, inverse `(x,y)->(x,y-eta(x))`.

Its Jacobian is 1. The transformed pair P0=P composed with phi,
Q0=Q composed with phi remains monic in y of the same degrees and
has `J(P0,Q0)=c x^ell`. Its roots are rho-eta. Pairwise root contacts,
and hence the disc radii, are unchanged by a common translation. This
normalization has no parameter-dependent denominator and no excluded
coefficient stratum: the only denominator N is a nonzero integer.

This group element centers the largest disc sufficiently for a bound. It
does not purport to put every marked D1 center at zero. No restriction on
an omitted D1 coordinate is justified by this shear alone.

## 6. Elementary weighted support theorem

Give x weight 1 and y weight d=-delta_s>0. Multiplying both weights by
the denominator of d makes them integral if desired. Since each root
of P0,Q0 has t-order at least -d, their elementary symmetric coefficient
formulas give, for F=P0 or Q0 of y-degree N_F,

`deg_x [y^a]F <= floor(d(N_F-a))`.

Thus the weighted degree of F is at most d N_F.

Let h be the unique q-th approximate root of Q0:

`h=y^K+sum_(j=1)^K H_j(x)y^(K-j)`.

This is polynomial over k[x], by the formal-root definition on p.148 or
by the following direct recursion. Match the coefficients
`y^(qK-j)`, j=1,...,K, in Q0 and h^q. The new coefficient is q H_j
plus sums of products of earlier H_i whose indices sum to j. By
induction each such product has x-degree at most d j. The coefficient
in Q0 also has degree at most floor(dj), so division by the nonzero
integer q gives

`deg_x H_j <= floor(dj)`.

Consequently h has the necessary support

`G_h={(b,a):0<=a<K, 0<=b<=floor(d(K-a))}`.

The same coefficient matching gives
`deg_y(Q0-h^q)<(q-1)K`, which is precisely beta_1=0.

For completeness, polynomial h-adic division gives the required
coefficient support without assuming a common quasi-approximate-root
system for P and Q. If a polynomial F has weighted degree at most dL,
and its leading y-term is A(x)y^r with r>=K, then the quotient term
`A(x)y^(r-K)` has weighted degree at most d(L-K). Multiplication by
h has weighted degree at most dL. Subtracting that product preserves
the bound and lowers y-degree. Monicity guarantees polynomial division
without any coefficient localization. Repeat this division to obtain

`P0=h^e+sum_(i=1)^e alpha_i h^(e-i)`,
`Q0=h^q+sum_(i=2)^q beta_i h^(q-i)`.

Every coefficient has y-degree below K, and at deficit i its necessary
support is

`G_i={(b,a):0<=a<K, 0<=b<=floor(d(iK-a))}`.

This is an elementary filtered-division theorem. The source supplies
the root disc and the descended polynomial pair; the proof above
supplies the finite polynomial inventories. It does not infer a
total-degree bound from monicity alone.

## 7. Union completion and consumption

Let D_h,D_i be the uncapped centered D1 inventories in section 2.
For the final repair emit

`H_h=D_h union G_h`, `H_i=D_i union G_i`

in the h, alpha_i, and beta_i blocks, keeping beta_1 absent because h
is the actual approximate root of Q0. These spaces contain every
previously omitted centered D1 monomial and every coordinate needed by
the source-derived largest-disc chart. They can contain many additional
pairs; that is harmless for an emptiness argument.

The source map is explicit: form eta, translate P,Q, compute h by the
q-th-root recursion, divide P0,Q0 by monic h, and assign these polynomial
coefficients to the G coordinates of the emitted chart, setting all
coordinates in H minus G to zero. This produces a chart point from
every actual descended pair covered by the charged child data.

The terminal constant translations used by the compiler are sound
group elements `P0->P0-const(alpha_e)` and
`Q0->Q0-const(beta_q)`. They preserve the Jacobian and the weighted
support; q>=2 ensures the approximate root is unaffected by subtracting
a constant from Q0. A failed scalar-shear audit remains a reason to
omit that shear, not to omit its coefficient variables.

On each of the six classes in the table, an exact characteristic-zero
UNIT on this completed fibre chart is therefore a valid theorem-(T)
kill of that fibre. A class is killed by UNIT on every fibre, or by
UNIT on a class support envelope containing all its fibre charts with
the explicit zero-coordinate specializations. A representative fibre
does not kill another fibre merely because n,m,M,ell agree.

Rabinowitsch `T c-1` encodes c!=0. An exact-Q unit identity transports
to any algebraically closed characteristic-zero extension, contradicting
the source chart point. A timeout, modular result without exact-Q
confirmation, or UNIT on a chart lacking the necessary G inclusion is
not that contradiction. No current raw-D1-only certificate is consumed
unconditionally by this note.

The true frozen 425-generator regression is the s'=4 singleton
`C_n24m16_Mm12_m2_5_ell1_s4`, not V3_2. Frozen
`moh14-fix-solve-opus5-20260905.md:133–150` explicitly identifies that
425-vs-425 control and separately mentions V3_2 with 514 older rows.
For the s'=4 singleton all G inventories already lie inside the raw D1
inventories, so the safe completion changes none of its generators.
This identity must be reported with the correct stem rather than
silently treating the two labels as interchangeable.

## 8. Exact circuit graph extension: independent implementation review

The final solver representation also uses
`source-complete/ops/circuit_emit.py`. This is an exact graph extension,
not a support specialization. Let A be the original rational parameter
ring, including c, and let S=A[U] adjoin the ordered auxiliary variables.
At each Horner stage, the emitter computes the coefficient polynomials
of `previous*h+alpha_i` or `previous*h+beta_i`. For a coefficient not
already represented by a single parameter or the constant 1, it inserts
one new variable u and the equation `u-f=0`. The polynomial f uses only
original parameters and previously introduced auxiliary variables.

This order gives a homomorphism theta:S->A by recursively substituting
each computed coefficient for u. Its kernel is exactly the ideal D of
these graph equations: successively eliminating each monic equation
`u-f` identifies S/D with A. This works over arbitrary A-algebras,
including nonreduced rings, and imposes no nonvanishing condition.

The final Horner maps represent P and Q. The emitter differentiates them
coefficientwise: a Q monomial x^r y^s and a P monomial x^u y^v contribute
`(rv-su)x^(r+u-1)y^(s+v-1)`. This is the native convention
`Q_x P_y-Q_y P_x`. It subtracts c at x^ell y^0. If E is this list of
Jacobian coefficients in S, theta(E) is therefore the list of ordinary
x,y coefficients of the original native Jacobian equation. Consequently

`S[T]/(D,E,Tc-1) is isomorphic to A[T]/(theta(E),Tc-1)`.

The phrase “contraction of the circuit ideal” always includes the graph
equations D. Contracting just the auxiliary Jacobian equations E would
not assert this graph identification.

For comparison with native h-adic extraction, the polynomials
`y^a h^j`, `0<=a<K`, form a triangular monic basis over A[x], ordered by
their y-degrees a+jK. On every finite degree interval the change of
basis from y-powers has a polynomial inverse and diagonal ones. Thus the
ordinary coefficient ideal and the h-adic coefficient ideal are equal
in A, after extracting their x coefficients, and remain equal on
adjoining Tc-1. This proves the circuit presentation defines the same
chart as the completed native presentation.

The implementation sites are: primitive support parsing `43–54`, exact
convolution `55–62`, Horner construction and fresh monic auxiliaries
`70–85`, native-sign Jacobian construction `86–98`, and separate rational
specialization controls `106–128`. The source review verified the
recurrence and sign symbolically. An independent static check of all
eleven emitted circuit stems also verified agreement of row.k with
closed_form.ell, distinct declared variables, unique primitive x,y
monomials, declared versus actual row counts, and triangular dependence
of every auxiliary definition. The two rational specialization controls
per stem are regression controls, not the proof of the ring isomorphism.

The circuit uses the native Jacobian sign. Relative to the high-first
convention `J(P,Q)=P_x Q_y-P_y Q_x`, the explicit invertible map is
`c_native=-c_highfirst`, `T_native=-T_highfirst`; it preserves Tc-1.
No name matching or implicit orientation choice is needed.

## 9. Terminal characteristic data, copied V marks, and a stronger class map

The final necessity argument is independent of the compiler's copying
of the inner V marks. Those marks must not be silently interpreted as
literal counts in the child major discs. For example, in the M2_9
class the copied terminal V mark is 8 while the corresponding scaled
gcd is 2. Substituting these directly as literal child quantities into
Definition 5.1(1) would give a root count exceeding the total degree.
That is a warning about the interpretation of the marks, not a new
mathematical kill of the source row. No such inference is used here.

The terminal characteristic entry used by G has a separate source
derivation. Printed p.154/PDF15 says that the sequences
`{n,mu_1,...,mu_r}` and `{n,M_1,...,M_r}` determine each other, gives
their equal gcds, and recovers the characteristic data from the
corresponding sequence of monic characteristic polynomials T_i.
The text anchor is `box/depth-drivers-20260902/moh.txt:778–795`;
the page was visually checked. Proposition 6.3(2) scales the y-degree
of every corresponding T_i, not just the first two polynomials.

Write a=u_s/d_s=1/d_s on these source rows. The transformed polynomials
are obtained by the same substitution in g,T_1,...,T_(s-1), so their
degrees give `n'=a n` and `mu'_i=a mu_i`, for i<s. They retain their
characteristic-polynomial construction; arbitrary unrelated polynomials
with numerically matching degrees are not being substituted for them.
Since d_s divides all these integers,

`d'_j=gcd(n',mu'_1,...,mu'_(j-1))=a d_j`.

The auxiliary identities on printed p.150/PDF11 are

`lambda_j=sum_(i=1)^j (M_i-M_(i-1))d_i`, `mu_j=lambda_j/d_j`,

with M_0=0. Equivalently,

`mu_j d_j=M_j d_j+sum_(i<j)(d_i-d_(i+1))M_i`.

This is a triangular recovery formula for the M_i. Substituting
`mu'_i=a mu_i`, `d'_i=a d_i` and inducting on j gives
`M'_j=a M_j`: numerator terms scale by a^2 and the coefficient of
M'_j scales by a. Thus the terminal child entry is
`M'_(s-1)=M_(s-1)/d_s`, independently of every V mark. The terminal
gcd becomes 1, with each preceding strict gcd drop retained. Apply
the p.174 effective-index convention if needed; no listed child
requires that deletion. The primary p.150 identities provide this
homogeneity argument without relying on an OCR transcription of the
displayed inverse formula on p.154.

Accordingly D_i(v) in the final emitted union can be read as the
specified raw support associated with the inherited mark v. Its
presence is harmless even if its literal-child-D1 interpretation needs
more work. The actual source-to-chart proof only uses G_i, calculated
from the verified terminal data (n',m',M'_last,ell), the largest-disc
construction, and the trace translation. The root-count explanation
for the centered D1 lemma in section 2 is conditional on literal disc
root counts; it is not a validation of all copied V marks.

There is a useful strengthened consumption rule. All fibres v of a
fixed class have the same n',m',M'_last,ell. Therefore their G_i spaces
are identical. Every final fibre chart `S_i(v)=D_i(v) union G_i`
contains the same source-receiving G chart, by its explicit zero-extra-
coefficient map. Exact-Q UNIT on any one of these final completed
fibre charts consequently kills the entire class. This shortcut is
proved by the common G inclusion, not by matching fibre names or
treating a representative as the literal union. UNIT on all fibres
or on the class envelope remains sufficient, but is no longer
necessary for class consumption under this strengthened source map.
