# Coordinate-resonant affine angular operators

ROOT manual candidate; publication opened2026-09-11 21:23:29UTC (exact
transaction manifest owns the clock). Original reserve21:35/HARD21:38UTC.
Basis0d39df3c9fd69c939a8420c54d03228b9077777d. INTERNAL/UNREVIEWED.
No computation, source realization, general annihilator reduction or JC2
conclusion. The exact native growing-shear report is PROVISIONAL and its
FIRST different-model review was launched21:23:07 before this exploration.

Inputs: native report c179106b8dabb3eeb20a0757e75faf952d0d6f42511fc90f2450126b11ef58b7;
Bass1989 PDF86f642941d2cea0f1d438996d8e81833ac53b6039c4c81e1564adc411f614b1e,
printed41--42 and49, source theorem1.4 externally trusted at its exact scope.
The native leading-coefficient argument is re-derived below rather than
assuming a generalization of its conclusion. No other research report is
a mathematical input. All statements below are manual proof candidates.

## Exact question

Put ep=p partial_p, eq=q partial_q, delta=p partial_q. For integer r>=0
and complex constants A,B,C consider

    Phi=ep-r+delta(A ep+B eq+C).

Composition order is literal: delta on the LEFT. Decide which algebraic
formal germs in ker(Phi) can be nonpolynomial, and whether any such germ
can be globally regular on an actual polynomial-plane Keller source.
Cheapest test: exact homogeneous coefficient recurrence and convergence
bounds, one manual lane under15minutes; no coefficient farm.

## 1. Complete homogeneous recurrence

For d<r the degree-d triangular matrix has diagonal i-r, 0<=i<=d,
so its kernel is zero. For d=r+n, the coefficients with p-exponent below r
vanish successively. The coefficient of p^r q^n is free; above it the
diagonal entries j, 1<=j<=n, are nonzero. Put K=A r+C and

    V_(n,0)=1,
    V_(n,j)=(-1)^j binom(n,j) product_(k=0)^(j-1)
                           [B n+K+(A-B)k].                 (1)

Indeed j V_(n,j)+(n-j+1)[B n+K+(A-B)(j-1)]V_(n,j-1)=0.
Every formal kernel element is therefore uniquely

    f=p^r sum_(n>=0)c_n sum_(j=0)^n V_(n,j) p^j q^(n-j). (2)

In particular f=p^r(H(q)+p times a formal series), H(q)=sum c_n q^n.
If f is nonzero and algebraic, H is algebraic. To see this without any
nonzero-point formal substitution, take a nonzero polynomial relation
Q(p,q,f)=0 and assign weights wt(p)=1, wt(q)=0, wt(T)=r. Its nonzero
initial part Q_mu gives Q_mu(p,q,p^r H)=0. Every summand has p-degree mu
after substitution, so division by p^mu gives a nonzero polynomial relation
in q,H. It is nonzero because for each q^b T^k the required p-degree
mu-rk is unique. All relevant p-orders are bounded below. f=0 is trivial.

## 2. The growing cases force H entire

We use the exponential coefficient bound |[p^i q^j]f|<=L^(i+j+1) for
algebraic formal f over C. Section5 supplies an elementary reduction to
univariate algebraic convergence, not an unproved formal specialization.

Suppose B!=0. Choose fixed 0<epsilon<1 such that
epsilon |A-B|<=|B|/4, and put j_n=floor(epsilon n).
For all sufficiently large n and 0<=k<j_n,

    |B n+K+(A-B)k| >= |B|n/2.

The corresponding coefficient of f in (2) is exactly c_n V_(n,j_n):
different n have different total degrees. Since binom(n,j_n)>=1,

    |c_n|^(1/n) <= L^((r+n+1)/n) (|B|n/2)^(-j_n/n) -> 0.

Thus H is entire and algebraic, hence polynomial, and f is polynomial.
This argument deliberately uses an EARLY coefficient, not q=0: later
factors in (1) may vanish, even for infinitely many n.

Now suppose B=0, A!=0 and K is not -A times a nonnegative integer.
At q=0, the coefficient of p^(r+n) is
c_n(-1)^n product_(k=0)^(n-1)(K+A k). No factor is zero. For large k,
|K+A k|>=|A|k/2, so the nth root of this product tends to infinity
(even its last n/2 factors already give a growing power of n).
The convergent algebraic restriction f(p,0) therefore again forces
|c_n|^(1/n)->0. H, and hence f, is polynomial.

An entire algebraic H is polynomial by the elementary polynomial root
bound outside a disk, followed by Cauchy estimates, as in the native report
and Bass printed49. No coefficient arithmetic or degree bound is assumed.

## 3. Every nongrowing case and honest controls

Suppose B=0, A!=0 and K=-A J for an integer J>=0. Formula(1) vanishes
for j>J, for every n. Formula(2) simplifies EXACTLY to

    f=p^r sum_(j=0)^J binom(J,j)(A p)^j H^(j)(q).        (3)

Here H^(j) is the ordinary jth derivative. Conversely(3) lies in ker(Phi)
for any H in C[[q]], by(1). Algebraic H has algebraic derivatives and
therefore yields algebraic f; the preceding leading-coefficient argument
gives the converse. H=1/(1-q) supplies a genuine rational nonpolynomial
germ for every r,J,A!=0. Its leading p^r coefficient is nonpolynomial,
so cancellation cannot accidentally turn it into a polynomial.

If A=B=0, put u=q-Cp. Then ep+Cdelta becomes p partial_p with u fixed,
and every solution is

    f=p^r H(q-Cp).                                    (4)

It is algebraic precisely when H is; H=1/(1-u) again gives an honest
nonpolynomial rational control. This includes C=0 and r=0. These two
degenerate families refute a uniform ALL-GERM polynomiality statement;
they are not counterexamples on an actual Keller-plane source.

## 4. Actual-source corollary and exact remaining gap

Conditional on Bass1.4 (R/A torsion-free over C[ep,eq]) and its applicability
after a linear target change, EVERY operator Phi above is injective on R/A
for an actual polynomial-plane Keller extension in normalized target
coordinates p,q with a source point over (0,0). Here A in R/A denotes the
ring C[p,q], not the coefficient constant A used above.

First if Phi(f) is polynomial, subtract the finite homogeneous truncation
through its degree from the formal inverse expansion of f. Those finitely
many homogeneous terms lie in C[p,q]; the resulting tail is still in R,
has Phi(tail)=0, and is algebraic formal. For a Keller map, the formal
inverse at the chosen source point over (0,0) exists by the nonzero Jacobian.
It embeds R injectively in C[[p,q]] (translate the source point if needed), and
its image is algebraic over C(p,q) since the dominant generically finite
map has finite function-field extension. This is an embedding, not a
claim that an arbitrary infinite formal projection lies in R.
Target normalization is an explicit hypothesis: a translation of arbitrary
fixed target coordinates would change the displayed operator. For the zero
right-hand side take any nonnegative truncation cutoff; otherwise its degree
is the stated cutoff.

The growing cases give polynomiality directly. In(3), p-degree is at most
r+J, so the nonzero polynomial operator product_(i=0)^(r+J)(ep-i)
kills f. Bass1.4 then makes f polynomial. In(4), the linear target shear
leaves C[p,q]=C[p,u] unchanged and gives the operator p partial_p-r;
apply the same Bass theorem in the sheared target coordinates. Thus the
actual-source statement holds for all complex A,B,C, although the algebraic
germ statement has exactly the exceptional families above.

This expands the tested coordinate-resonant family but does NOT show an
arbitrary U-annihilator can be chosen with delta-degree one, linear diagonal
ep-r, or affine delta coefficient. Multiplying/combining annihilators does
not supply that reduction. No JC2 closure, unconditional new external
theorem, degree bound or novelty claim follows. No additional descendant or
expensive computation is licensed by this candidate. FIRST review is needed
before promotion, independent of the native family's pending review.

## 5. Elementary coefficient-bound justification

For completeness, write f=sum_d F_d with F_d homogeneous of degree d and
P_d(t)=F_d(t,1), a polynomial of degree at most d. A nonzero polynomial
relation Q(p,q,f)=0 remains a nonzero polynomial after p=tz,q=z: the
substitution on polynomial rings is injective. Except for finitely many
complex t, Q(tz,z,T) is not identically zero. For each such t, the formal
restriction sum_d P_d(t)z^d is algebraic in z, hence converges. Consequently
there is an integer M>=1, depending on t, with |P_d(t)|<=M^(d+1) for all d.

Take a closed complex disk avoiding those finitely many exceptional t.
Its closed subsets defined by these bounds for M=1,2,... cover the disk.
The Baire theorem gives one such subset containing a smaller open disk
centered at t0. On a closed disk of radius eta inside that open disk,
Cauchy's estimates bound the coefficient of (t-t0)^j in P_d by
M^(d+1) eta^(-j). Expanding on |t|=1 and summing at most d+1 terms gives
|P_d(t)|<=L^(d+1) there for a fixed sufficiently large L. A second Cauchy
estimate bounds every coefficient of P_d by L^(d+1). These are precisely
the coefficients of F_d, proving the claimed two-variable bound.

Only standard univariate algebraic convergence, Baire's theorem and Cauchy
estimates enter this reduction. It never substitutes a nonzero constant
into an arbitrary two-variable formal series: p=tz,q=z is homogeneous,
so each coefficient is a finite polynomial. This also independently explains
why the early-coefficient estimate in Section2 is legitimate.

## Checks and disposition

The recurrence explicitly checks composition order, every d<r and d>=r,
r=0, all constants zero, the constant shear, bounded-p truncation J=0,
and infinitely many possible late-factor zeros when B!=0. No positivity
assumption on complex A,B,C is hidden in the modulus estimates. Baire and
the analytic estimates are standard external background; Bass1.4 is a named
conditional source input, not reproved here. Native report and primary PDF
were pinned and read before use, then checked again before sealing.
This is one manual unreviewed candidate, not a completed proof of JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9679`.
- Body SHA-256:
  `9ec72692266130b4a12a64902720f5943fd435aa5ad8af650d600b368b724478`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
