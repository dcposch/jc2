# Audit and quadratic-cover reduction for the Astra K16 lane

Working note for the root agent. Frozen inputs were hash-verified by root;
this sublane reads only those inputs and the new root-generated exact row
files. All claims below are factorwise over a characteristic-zero field
factor of A_t. This is not a proof of the all-t terminal statement.

## 1. Load-bearing hypotheses in the frozen sources

The original terminal row is not the radical target. In
`k16-terminal-proof-fable5-20260903.md:145` and
`k16-nzd-gamma-gpt55-20260903.md:386`,

    T_{t,0} = -c + tau_t,    c=-yg,
    tau_t = T^hom_{t,0},    wt(tau_t)=4t+1.

Thus `tau_t = T_{t,0}-T_{t,0}(0)`. The literal original `T_{t,0}` does not
belong to `sqrt(I_+)`: the origin belongs to `V(I_+)` and its value there is
the nonzero unit `yg`. The intended (8.1) statement is about the homogeneous
part. Root-generated `t3_rows.sing` and `t4_rows.sing` distinguish `T0` and
`tau` correctly.

TAIL-SPLIT, including the unit leading scalar of Q, is uniform for t>=3.
FITT and its set-theoretic elimination equality are uniform under that unit
hypothesis. The displayed EN series has a different status. The exact
statement in `k16-rank-criterion-fable5-20260903.md:36` is:

> If V(J_t^tail)={0} then grade I_2(N) = t-2 is maximal.

Its proof at line 322 begins with that same hypothesis. It deduces that
`G_1,...,G_{t-1}` is regular, then obtains the height needed for
Eagon--Northcott. These are not unconditional all-t height results in the
frozen input. The BRCR report explicitly preserves the hypotheses in its
Section 1.2. In particular one cannot invoke uniform CM/dimension one here
as already proved without supplying a stronger independent source.

Even a one-dimensional CM local ring need not be a DVR. The cusp ring
`K[s^2,s^3]_(s^2,s^3)` is a one-dimensional local CM domain and its maximal
ideal has two generators, so it is not a DVR. A CM curve may also be
nonreduced. The correct valuation construction is to pass to each
irreducible component of the reduced curve and normalize. At a normal
one-dimensional local point one gets a DVR. On a homogeneous one-dimensional
component the pullback of a homogeneous f is `c*z^d` (with the appropriate
normalized weight). The desired nonvanishing is precisely `c != 0`; the
existence of the valuation does not determine this coefficient.

There is a related qualification on the claimed equivalence with NZD.
Knowing Q is a nonzerodivisor on `S/(G)` lowers its dimension by one. It gives
zero-dimensionality only if `dim S/(G)=1` is separately known. The frozen
proof gets that latter assertion from tail zero-dimensionality, so it
cannot be recycled in the reverse direction. A template displaying the
issue is `G_i=B_i*(b+f)`, with `(B_i)` an hsop in P and `f` homogeneous of
weight `wt(b)`. Take `Q=b^2+f^2`. Its restriction to both associated
components `(b+f)` and the b-axis is nonzero, so it is an NZD, while the
component cut out by `b+f=0,Q=0` has positive dimension as soon as P has at
least two variables. This template has the same split-weight format; it
does not claim to be a K16 row system. The exact all-t target safe without
height assumptions is `sqrt(I_2(N)+(W_r))=m`, or directly (8.1).

LENGTH-SPLIT is an unconditional numerical identity and a conditional
intersection interpretation. Its axis multiplicity interpretation is
explicitly stated to hold when `(B)` is an hsop at rank report line 391.
`V(G)` contains the b-axis; for t>=3, `Q|axis=a0*b^2` with a0 a unit, so
the axis contributes only the origin to the actual terminal cone `V(I_+)`.
It is not an established positive-dimensional component of that latter
cone. Also `d_Gamma(3)=15/2`, so the weighted degree counts multiplicity
with stabilizer denominators, rather than literally 7.5 geometric points.

## 2. A height-free finite quadratic reduction of the weaker target

This is a new exact reduction usable for every t>=3, including every chart,
the rank-zero locus, and all rows below the square tail. It works over any
characteristic-zero coefficient field K, hence on each field factor of A_t.

Let `P=K[x_1,...,x_n]`, `S=P[b]`, and

    Q = a*b^2 + b0*b + c0,             a in K^times.

Divide all the other positive terminal rows by Q, and divide the
homogeneous target tau by Q. Let the resulting remainders be

    H_i = v_i+u_i*b,      i=1,...,m,
    h   = v+u*b.

For K16 use `n=t-1`, `m=2t-2`, Q=`T_{t,2t-1}`, and rows
`T_{t,1},...,T_{t,2t-2}`. Then

    I_+ = (Q,H_1,...,H_m),
    tau in sqrt(I_+) iff h in sqrt(I_+).

No division by a polynomial in the residual variables occurs: a is a field
unit, so this is ordinary polynomial division in P[b]. Define base ideals
and forms

    J0 = (u_i,v_i : all i),
    M_ij = v_i*u_j-v_j*u_i,
    W_i = a*v_i^2-b0*u_i*v_i+c0*u_i^2,
    F = (M_ij,W_i : all i,j),
    D_i = v*u_i-u*v_i,
    ell = 2*a*v-b0*u,
    nrm = a*v^2-b0*u*v+c0*u^2.

**Quadratic-cover criterion.** The following are equivalent:

    (1) tau in sqrt(I_+);
    (2) every D_i is in sqrt(F), and ell,nrm are in sqrt(J0).

This remains true when the determinantal locus has dimension greater than
one, when it is singular or nonreduced, and when some or all of the B-charts
are absent on a component.

Proof: extend scalars faithfully to an algebraic closure and use the
Nullstellensatz; radical membership then descends. The finite projection
`V(I_+) -> Spec P` has image V(F), by exactly the same quadratic Fitting
calculation as the banked FITT theorem, now with all reduced positive rows.
Equivalently this follows by a direct rank argument:

* If `(v_i,u_i)` has rank at least two, its minors do not all vanish.
* At rank one, if every u_i is zero then some v_i is nonzero, and its W_i
  equals `a*v_i^2`, excluding the point from V(F).
* At any other rank-one point, some u_r is nonzero and the only possible
  lift is `b=-v_r/u_r`. The minors ensure all H_i vanish there and
  `W_r=u_r^2*Q(-v_r/u_r)` tests whether it is a lift through Q. The value of h
  at that lift is `D_r/u_r`. All D_i vanish iff that value vanishes. This
  argument uses the union of all D(u_r), never a distinguished chart.
* At rank zero, all H_i vanish, so the fiber is the entire quadratic
  scheme `Q=0`. If its two roots counted with multiplicity are beta_1,
  beta_2, then the values of h have sum `ell/a` and product `nrm/a`.
  Both values are zero iff both ell and nrm are zero. This includes the
  double-root case: characteristic zero makes the trace condition valid.

Rank-zero points are exactly V(J0), hence the stated base radical
conditions are necessary and sufficient. QED.

The extra rank-zero test is essential. For example take P=K[x], Q=`b^2-1`,
all H_i zero, and h=`b-1`. All D_i and nrm vanish, but ell=-2 and h is
nonzero at the other root. Testing only norm or only augmented rank would
incorrectly accept radical membership. This example is an audit control,
not a K16 counterexample.

An equivalent rank-zero condition is

    ell in sqrt(J0),
    (b0^2-4*a*c0)*u^2 in sqrt(J0),

because `ell^2-4*a*nrm=(b0^2-4*a*c0)*u^2`. This is useful for separating the
ramified and unramified quadratic fibers, while the trace--norm form needs
no extra discriminant charts.

## 3. Ordinary base memberships lift to an explicit nilpotence certificate

Every generator of F belongs literally to `I_+ cap P`. For the minors,

    M_ij = u_j*H_i-u_i*H_j.

For the norms use the conjugation involution of the rank-two algebra
`P[b]/(Q)`, which sends b to `-b0/a-b`:

    W_i = a*H_i*conjugate(H_i) mod Q.

One can enlarge F to the literal zeroth Fitting ideal Ffull by adjoining

    X_ij = a*v_i*v_j-b0*u_j*v_i+c0*u_i*u_j.

The same block-matrix proof as FITT proves `Ffull subset I_+ cap P`. Directly,
these X_ij are minors of the presentation of the finite P-module S/I_+,
and zeroth Fitting ideals annihilate that module.

In A=`S/I_+`, the following identities hold:

    u_i*h = D_i,
    v_i*h = -b*D_i,
    a*h^2-ell*h+nrm = 0.                  (Cayley--Hamilton)

Therefore if every D_i belongs *ordinarily* to any explicitly certified
base ideal E contained in `I_+ cap P`, and if ell and nrm belong
*ordinarily* to J0, then `J0*h=0`, `ell*h=nrm*h=0`, and multiplication of
Cayley--Hamilton by h gives

    h^3=0 in A,    equivalently tau^3 in I_+.

This supplies a concrete uniform cubic-certificate target wholly within
the b-free polynomial ring, without requiring the stronger V0 theorem.
It is a sufficient criterion, not an assertion that its memberships hold
for the K16 coefficients at every t.

There is also an effective bound from arbitrary explicit powers. Suppose
`D_i^{e_i} in E subset I_+ cap P`, `ell^r in J0`, and `nrm^s in J0`, where
all exponents are positive. Put

    N = 1 + sum_i(e_i-1).

The two identities prove the equality `J0*h=(D_i)A`. The Nth power of
this ideal vanishes by the pigeonhole principle. Hence
`ell^{r*N}*h^N=nrm^{s*N}*h^N=0`. Iterating the quadratic relation shows

    h^[N*(1+r+2*s)-1] = 0.

Indeed, modulo `(ell^R,nrm^S)`, a quadratic root of
`a*Z^2-ell*Z+nrm` has exponent at most `R+2*S-1`: in the basis `{1,Z}` its
coefficients have weighted degrees K and K-1 in ell,nrm of weights 1,2;
the largest weight of a surviving monomial is `R+2*S-3`. Use R=rN,S=sN
on the module h^N*A. This bound is deliberately coarse and is not a
degree-only proof of any K16 membership.

When r=s=1 there is a sharper bound: multiplication of Cayley--Hamilton
by h gives `h^3 in (D_i)A`, so `h^(3*N)=0`. In particular, if all D_i
are ordinarily in E except for one whose square is in E, this mechanism
gives tau^6 in I_+. If every D_i^2 is in E, the bound is
`tau^[3*(2t-1)] in I_+` in the full K16 reduced-row setup.

An independent square-zero sufficient criterion is

    b3*tau in I_+,       tau in I_+ + (b3).

Indeed write tau=i+b3*f and multiply by tau. These two ordinary
memberships yield tau^2 in I_+ without any dimension statement. Root has
checked the first at t=3,4, but it is degree-forced there: the full quotient
has top weights 14 and 21, whereas b3*tau has weights 17 and 22. These data
must not be read as a uniform syzygy proof.

The second membership is **false at t=4**, by the completed exact slice
probe below. Thus this particular sufficient square-zero strategy is
already refuted as a uniform K16 route. At t=3 it holds for the elementary
reason that tau has weight 13 and the slice quotient has top weight 10.

## 4. Exact new probes

`audit_baseprobe.py` parses only the freshly root-generated exact row
files, works over `QQ(sqrt((t+1)/3))`, uses polynomial division in b over
`K[b4,u2,...]`, and computes the displayed base ideals with SymPy. The
coefficient-field map is `d -> sqrt((t+1)/3)`; for t=3,4 this is a field
embedding and covers the conjugate factor by the nontrivial automorphism.
No modular or localized membership is promoted.

The SymPy t=3 probe completed. At t=4 it proved the J0 memberships and
zero-dimensionality, but was stopped after about 20 minutes in the F
standard-basis computation. No result is inferred from that unfinished
stage. The exact Singular replay used the same row files, with an explicit
map to a b3-first lexicographic ring for ordinary univariate division,
then the explicit map `(b3,b4,u2,...)->(0,b4,u2,...)` on the b-free
coefficients. Every remainder was checked to equal v_i+u_i*b3. The
Singular t=3 replay agrees with all completed SymPy results.

The final, accepted logs are
`audit_baseprobe_t3_singular.log`, `audit_baseprobe_t4_singular.log`,
`audit_minors_t3.log`, and `audit_minors_t4.log`; all completed with exit
zero and the expected terminal marker and have no error/FAIL/division
marker. `audit_emit_baseprobe.py` emits their exact scripts. A discarded
stats-procedure syntax error is retained under the explicit name
`audit_baseprobe_t3_stats_development_error.log`; it is not a proof
transcript. An unoptimized interrupted t=4 Singular attempt and the
interrupted SymPy attempt are likewise retained but are not used beyond
their completed J0 output. There are no audit jobs left running.

| t | J0 length, top | F length, top | Ffull length, top | least tested D powers in F and Ffull | slice length, top | tau in I_++(b3) |
|---|---|---|---|---|---|---|
| 3 | 13, 6 | 84, 18 | 84, 18 | 1,1,1,2 | 29, 10 | yes |
| 4 | 42, 10 | 489, 25 | 481, 25 | 1,1,1,2,2,2 | 143, 17 | **no** |

All four ideals in each row are zero-dimensional. Every displayed top
weight was computed by enumerating the actual standard monomial basis
of the exact standard basis; it is not a predicted CI series. Both ell
and nrm belong ordinarily to J0 at both indices. D_i is indexed by the
original positive row k=i, for i=1,...,2t-2. Every entry 2 means the
first-power normal form is nonzero while the second-power normal form
is zero.

The base exponent-transfer theorem therefore supplies tau^6 in I_+ at
t=3 and tau^12 in I_+ at t=4. Root's direct checks supply the sharper
tau^2 in I_+ at both t, with tau itself nonzero. The purpose of this
separate calculation is the new height-free coefficient criterion and
its exact controls, not an improved numerical exponent.

These fixed-degree memberships contain little evidence for a uniform
coefficient identity. The weights are

    wt(ell)=4t+1, wt(nrm)=8t+2, wt(D_i)=7t+1-i.

Thus the ell/nrm memberships and all D_i squares are forced by the
*computed* finite quotient top degrees at t=3,4. Likewise the first three
D_i memberships are forced by their weights, whereas the remaining D_i
give actual nonzero classes. The slice target tau has weight 13>10 at
t=3 but weight 17=17 at t=4; its nonzero t=4 remainder rules out the
tempting uniform factorization through b3.

## 5. A uniform change to the actual approximate-root coefficient variables

The original high-spine coefficients `C_j` (of the polynomial C(X), not
the split-tail C_r) can themselves be used as independent polynomial
coordinates of P_t. This gives a uniform, explicit change of variables
which may make the approximate-root equations easier to study.

Write the original polynomial as

    C(X)=X^(t-1)+C_1 X^(t-2)+...+C_(t-1),
    U(X)=X^q+u_2 X^(q-2)+...+u_(2t) X,
    q=2t+1, e=3t+1, d^2=(t+1)/3.

For j=2,...,t-1 the weight-j spine equation is

    p_C(t,j)*C_j + p_Q(t,j)*u_j + lower-weight terms = 0.

Here p_C is the frozen unit pivot. Although the frozen formula for p_Q
was stated where u_j was a high solved variable, its same rational formula
is the coefficient of u_j for the lower values of j as well. The following
linearization proves this extension directly and avoids extrapolation.

Set b4=b3=0 and all deviations from the leading monomials to zero, except
for the formal perturbation `U=X^q+epsilon X^(q-j)`. Retain
`C=X^(t-1)`. Put

    g1=e/q, g2=e(d+q)/(2*q^2),
    y=(d+t+1)/(2*q), g=e*t*(3*d+2*(t+1))/(6*q^3),
    D=4*t-2*j+1.

The coefficient-array equation (3.4) of frozen BRCR gives

    delta S = s_j*epsilon X^(2t-j),
    s_j = 3*g*(q-j)/(y*D).

The baseline auxiliary polynomials are
`Q1=X^(t+1)`, `P1=g1*X^q`, `P2=g2*X^(t+1)` and the variations are
`delta P1=s_j*epsilon X^(q-j)`, `delta P2=delta Q1=0`.
D1 consequently gives

    delta V' = [s_j*(j-t)+2*g2*(q-j)]/(2*y)
                 *epsilon X^(3t-j).

The coefficient of `epsilon X^(4t+1-j)` in `Q1 V'-U'P1` is therefore

    p_Q(t,j)=(q-j)*[g2/y-g1
                    + 3*g/(y*D)*((j-t)/(2*y)-q)]
       = e*t*(q-j)*[(j-4*t-4)*d-2*(t+1)]
                    /[q*(d+t+1)^2*D].

Using `3*d^2=t+1` reduces this to the exact frozen expression

    p_Q(t,j) = -3*t*e*(q-j)*(A_Q*d+B_Q)
                  /[(t+1)*q*(3t+2)^2*(4t-2j+1)],
    A_Q=12t^2+16t+4-j*(3t+4),
    B_Q=2*(t+1)*(j-t).

The calculation is valid for every `1<=j<=2t`; no choice of low versus
high spine unknown was used. In particular, for `2<=j<=t-1`,

    A_Q >= 9t^2+15t+8,
    |B_Q| <= 2*(t+1)*(t-2),
    |d| >= 1.

Thus `A_Q*d+B_Q` is nonzero on both real embeddings and is a unit of A_t.
The other displayed factors are units at the stated integer indices.
Solving gives

    C_j = -(p_Q/p_C)*u_j + polynomial in b4,u_2,...,u_(j-1).

For C_1 one can obtain the b4 coefficient from translation covariance.
Temporarily permit the missing u_1 coefficient of U. Translation
`X -> X+epsilon` at the monomial point changes `(u_1,C_1,b4)` by
`(q,t-1,-1)*epsilon`. The high weight-one equation remains zero, hence

    p_b4 = q*p_Q(t,1)+(t-1)*p_C(t,1).

Restoring the gauge u_1=0 gives `C_1=gamma_t*b4`, where

    gamma_t = -(t-1)-q*p_Q(t,1)/p_C(t,1)
       = [(108t^3+126t^2+8t+8)*d-24t*(t^2-1)]
          /[(72t^3+90t^2+16t+8)*d-4t*(3t-4)*(t+1)].

The denominator is the numerator of the banked nonzero p_C(t,1), up to
a unit. The numerator is nonzero on both embeddings because, for t>=2,

    108t^3+126t^2+8t+8 > 24t*(t^2-1),  |d|>=1.

So gamma_t is a unit too. The resulting triangular coefficient map is
therefore a polynomial automorphism, factorwise, for every t>=2:

    A_t[b4,u_2,...,u_(t-1)]
          = A_t[C_1,C_2,...,C_(t-1)].

The inverse is obtained recursively, with only scalar units inverted.
This is stronger than a birational chart change: it is a global weighted
polynomial-coordinate change, preserving every radical-membership problem.
At t=3, `gamma_3=(4082*d-576)/(2810*d-240)`.

Root independently checked these images exactly at t=3,4:
`C_1=gamma_t*b4` and every `dC_j/du_j=-p_Q/p_C` for `2<=j<t`, in
`coordinate_check.py` and its per-index logs. These are image checks on the
uniform proof, not replacements for its unit arguments.

This does not identify the split B_r with power sums or fractional-power
coefficients. Such an identification remains a next step. It does remove
one possible obstruction to that approach: the actual monic C(X) has
independent coefficient parameters, so its root/multiplicity geometry can
be used without imposing an additional unknown locus in parameter space.

### 5.1 The resulting finite free ordered-root cover

Let n=t-1 and introduce rho_1,...,rho_n with weight one. The explicit map

    C_j -> (-1)^j*e_j(rho_1,...,rho_n),
    b4 -> -(rho_1+...+rho_n)/gamma_t

identifies P_t with the ring of symmetric polynomials in the rho_i. The
ordered-root ring `A_t[rho_1,...,rho_n]` is finite free of rank n! over P_t.
One way to see freeness without a generic-specialization argument is to
adjoin an ordered first root of the universal monic polynomial (a free
extension of degree n), divide by its monic linear factor, adjoin a root
of the resulting monic degree n-1 polynomial, and continue. The successive
free degrees are n,n-1,...,1, and the final presentation is exactly the
ring with the displayed elementary-symmetric relations.

Consequently, after also adjoining b3, the radical target is equivalent
to its pullback to the ordered-root ring: a power membership ascends, and
it descends because the extension is faithfully flat and ideal
contraction is exact. This is a finite cover at each fixed t, not a
purported flat family that changes t.

In these coordinates the collision locus of C with the distinguished
linear factor L=X-b4 is especially simple:

    C(b4)=(-1/gamma_t)^n
            * product_i (rho_1+...+rho_n+gamma_t*rho_i).

Thus `C(b4)=0` is an explicit symmetric union of hyperplanes in the
ordered-root cover. If the Moh/local-identity analysis reduces the
terminal obstruction to such collision strata, this cover exposes their
geometry uniformly and avoids solving for unspecified algebraic points
of the EN locus. No assertion that all obstructions lie there is made
by the coordinate lemma alone.

### 5.2 Translated C coefficients: the collision is one coordinate

There is an even more convenient global coordinate system. With n=t-1,
write

    C(L+b4)=L^n+Chat_1 L^(n-1)+...+Chat_n.

Then

    Chat_1=C_1+n*b4=(gamma_t+n)*b4,
    gamma_t+n=-q*p_Q(t,1)/p_C(t,1).

The last scalar is a unit: the coefficient formula proved above is valid
at j=1, and its numerator has
`A_Q=t*(12t+13) > |B_Q|=2*(t^2-1)` with `|d|>=1`. For j>=2 the usual
translation formula gives `Chat_j=C_j+lower-weight terms`. Therefore

    P_t=A_t[Chat_1,...,Chat_n],
    b4=Chat_1/(gamma_t+n),
    C(b4)=Chat_n.

This proves that the distinguished root collision `C(b4)=0` is a single
polynomial coordinate hyperplane, globally and on both factors. Its
coordinate ring is another polynomial ring over A_t. No generic
smoothness or specialization hypothesis is needed.

In the ordered-root cover put `delta_i=b4-rho_i`. The linear map from
rho to delta is invertible because gamma_t and gamma_t+n are units.
Now

    Chat_j=e_j(delta_1,...,delta_n),
    b4=(delta_1+...+delta_n)/(gamma_t+n),
    C(b4)=delta_1*...*delta_n.

The cover remains finite free of rank n!, but the collision arrangement
is now the union of coordinate hyperplanes `delta_i=0`. Multiple roots
of C are the hyperplanes `delta_i=delta_j`. Thus both types of root
collision relevant to the approximate-root discussion admit an explicit
uniform hyperplane description on a faithfully flat cover.

## 6. All-row minors alone: a new sufficient rank condition, exact at t=3,4

Use the same b3-linear remainders of *all* positive rows as in Section 2,
and write

    Nfull = ((v_i,u_i))_(i=1,...,2t-2),
    Jmin = I_2(Nfull).

For every t>=3 the following implication is elementary and unconditional:

    sqrt(Jmin)=m_P  ==>  V(I_+)={0}  ==>  (V0) and (8.1).

Indeed a point of V(I_+) makes every linear remainder H_i vanish at its
b3-coordinate, hence Nfull has the nonzero kernel vector `(1,b3)` and
its minors all vanish. If Jmin is m-primary, the base point is zero;
the unit-leading top row then restricts to a*b3^2 and forces b3=0.
No EN height, curve hypothesis, Fitting norm, or localization is used.

This is a sufficient condition, not a claimed equivalent reformulation
of (V0). A point of the rank-one locus of Nfull need not lift through Q,
so V0 can in principle hold even when that rank-one locus is nontrivial.

The exact new `audit_minors_t{3,4}.sing` computations give

| t | coefficient field | dimension of P/Jmin | length | top weight |
|---|---|---|---|---|
| 3 | Q(d), 3d^2=4 | 0 | 85 | 18 |
| 4 | Q(d), 3d^2=5 | 0 | 503 | 26 |

Both accepted logs finish `AUDIT_MINORS_DONE` with exit zero and no
error marker. Thus no norm generator W_i is needed to prove the full
cone zero-dimensional at these two indices: the additional positive
rows below the square tail already remove every nonzero rank-one base
point of the enlarged matrix.

The corresponding all-t statement remains **OPEN**. Compared with the
tail matrix, Nfull is overdetermined: it has 2t-2 rows in a base of
dimension t-1. This makes it a different potential coefficient-recursion
target, but expected codimension is not a proof. The exact residual for
this sufficient route is simply `sqrt I_2(Nfull)=m_P` factorwise for
every t>=3. No t beyond 4 was computed in this audit.
