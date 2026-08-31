# Wild one-cusp quartic horn: valuation and completion structure

Date: 2026-08-31  
Author: Sol 5.6 Ultra (`wild_valuation_structure` research lane)  
Frozen lane basis: `1d97e7b76b9e53d849588cd678f47468bedd5de0`  
Lifecycle: **EXACT CONDITIONAL VALUATION LEMMAS / PROVISIONAL FIBRE COROLLARY / HORN OPEN**

## 0. Scope and dependency convention

This report is confined to exact desk algebra for the surviving wild
one-cusp quartic horn.  It makes no use of Picard, ML/Derksen, ruling
functoriality, boundary Fox coloring alone, or an independent residual
Kummer class.  No CAS computation is used.

Every assertion inherited from
`block-descent-a1-one-cusp-poisson-locally-finite-obstruction-sol56-20260831.md`
is marked **PROVISIONAL**.  In particular, until that parent clears its
separate different-model review, the claims that the two charged Hamiltonian
derivations are non-locally-finite and that both generic coordinate fibres
are hyperbolic are **PROVISIONAL** inputs rather than conclusions of this
lane.

The frozen lifecycle basis is `notes.md:15255-15319`; it registers the
Poisson parent and this descendant as provisional at `notes.md:15300-15306`.
The reviewed conditional function-pair input and the provisional
inverse-Kummer successor are typed separately in `AUDIT.md:69-85`.

## 1. Three different completions

Under the **PROVISIONAL model identification** supplied by the Poisson
parent, put

```text
S=Spec R,       R=C[A,U,Z]/(U^2-A-A^2Z),
Phi=V(A,U) subset S,                  kappa={f,g} in C*.
```

There are three objects which the packet sometimes discusses near one
another but which cannot be identified.

1. `Phi` is the reduced multiple-fibre line *inside* `S`; it is not a
   boundary component.
2. `R_bd=Y-S` is the ramification boundary in the finite normalization
   `Y->A2`.  It is not a closed subscheme of `S`, and hence has no defining
   ideal in the affine ring `R`.
3. In the cyclic cover, `L_0->Phi` is retained, while the other `L_j` are
   deleted source-boundary lines.  Their valuations do not arise from prime
   ideals of `R`.

This distinction is already explicit in the reviewed function-pair
construction (`...function-pair-coordinator-integration...md:82-105,
114-144`) and in the cyclic source description
(`...function-pair-cyclic-normalization...md:140-180,205-242`).

### 1.1 Exact completion along the intrinsic divisor `Phi`

Let `P=(A,U)` and `q=U^2-A-A^2Z`.  Complete the ambient polynomial ring at
`(A,U)`.  Since `R/P=C[Z]` and `q_A=-1-2AZ` is a unit in that completion, the
formal implicit-function theorem gives a unique zero-constant-term solution
`A=a(u,Z)` of

```text
A+ZA^2=U^2
```

With `u=U`, it is

```text
a(u,Z)=U^2-ZU^4+2Z^2U^6-5Z^3U^8+...
      =(sqrt(1+4ZU^2)-1)/(2Z),
```

where the quotient denotes its power series and is valid also at `Z=0`.
This gives an isomorphism directly; only after it is obtained does the
extended ideal become `(a(u,Z),u)=(u)`, since `a(u,Z) in (u^2)`.  Therefore

```text
R^_P  = C[Z][[u]],             R^_(R_P)=C(Z)[[u]],       (1.1)
A |-> a(u,Z),                  U |-> u.
```

Here the first expression is the formal completion along the whole affine
line and the second is the complete DVR at its generic point.  At the closed
point `p_z0=(A,U,Z-z0)`, one similarly has

```text
O^_(S,p_z0)=C[[u,w]],          w=Z-z0.                  (1.2)
```

In particular

```text
ord_P(U)=1,        ord_P(A)=2,        ord_P(Z)=0.
```

This also follows from the retained cyclic chart
`A=x^2, U=x+x^3y, Z=2y+x^2y^2`; the direct ring calculation above does not
depend on that chart.

The Poisson bracket becomes especially simple.  Put

```text
B(u,Z)=2+4Za(u,Z)=2sqrt(1+4Zu^2).
```

Then

```text
{u,Z}=B,
{F,G}=B(F_u G_Z-F_Z G_u),
X_H=B(H_u partial_Z-H_Z partial_u).                     (1.3)
```

Thus both charged fields extend continuously to `C[Z][[u]]` as derivations
which may lower the `u`-adic filtration by one.

Make the filtration exact by setting `nu(F)=ord_u(F)` and `nu(0)=+infinity`.
If

```text
F=h(Z)u^m+O(u^(m+1)),       G=k(Z)u^n+O(u^(n+1)),
```

then

```text
nu({F,G}) >= m+n-1,                                      (1.4)
in_(m+n-1){F,G}
 =2(m h k'-n h' k)u^(m+n-1).                            (1.5)
```

Here and in (1.9), a prime means differentiation with respect to the residue
coordinate `Z`; it is not a branch or prime-divisor label.

Equation (1.4) is only a floor: (1.5) can vanish.  For fixed `H` it gives

```text
nu(X_H^j F) >= nu(F)+j(nu(H)-1),                         (1.6)
```

again with equality only while the successive initial expressions do not
cancel.  This is the exact associated-graded Hamiltonian structure, rather
than a scalar-weight proxy for membership in `R`.

Every element has a unique form

```text
H=P_H(A,Z)+U Q_H(A,Z).                                  (1.7)
```

The **PROVISIONAL** parent theorem says that a nonconstant `X_H` is
non-locally-finite exactly when `H notin C[A]`.  In the coordinates (1.7),
this says only

```text
Q_H != 0  or  partial_Z P_H != 0.                        (1.8)
```

It imposes no universal initial order or eigenweight: `H=Z` has order zero,
whereas `H=U^N` has arbitrary order `N`, and each lies outside `C[A]`.
Consequently non-local-finiteness alone cannot turn the floor (1.4) into an
attained growth formula.

For the charged pair there is more information, but it comes from the
constant bracket and the reviewed companion curve, not from wildness.  Write

```text
f=f_0(Z)+f_1(Z)u+O(u^2),
g=g_0(Z)+g_1(Z)u+O(u^2).
```

The degree-zero coefficient of `{f,g}=kappa` is exactly

```text
2(f_1 g_0'-f_0' g_1)=kappa.                              (1.9)
```

Hence `(f_0',g_0')` never vanishes simultaneously.  The reviewed
function-pair theorem identifies `Z |-> (f_0(Z),g_0(Z))` with the immersive
normalization `Phi=A1 -> C_0` and supplies distinct `z,z'` with the same
image.  Neither coordinate polynomial can be constant (that would make the
image a line) or affine (that coordinate would separate `z,z'`).  Thus
`deg f_0,deg g_0>=2`.  Generically along `Phi`, both Hamiltonians therefore have
order zero and their degree `-1` symbols are

```text
gr_(-1)(X_f)=-2f_0'(Z) partial_u,
gr_(-1)(X_g)=-2g_0'(Z) partial_u.                        (1.10)
```

These leading symbols are locally nilpotent.  The **PROVISIONAL** global
non-local-finiteness must be carried by higher normal coefficients and global
reattachment, not by a nonzero formal eigenvalue in (1.10).  The exact
invariant-ring control explicitly permits arbitrary polynomial restrictions
and an etale first jet along `Phi`
(`...invariant-ring-quartic-gate-control...md:336-394`).

### 1.2 The charged cusp point

The target cusp `c in B` is not a point of `S`.  The packet supplies one
interior companion point `u_c in T=pi^(-1)(B) intersect S`, and leaves the
two cases `u_c in Phi` and `u_c notin Phi` open
(`...function-pair-cyclic-normalization...md:427-439`).  Put

```text
p=f-f(u_c),             q=g-g(u_c).
```

Since `pi=(f,g)` is etale on `S`, the complete local structure and the two
flows are exactly

```text
O^_(S,u_c)=C[[p,q]],
X_f=kappa partial_q,             X_g=-kappa partial_p.   (1.11)
```

Thus both **PROVISIONAL** globally wild fields are formally rectified to
translations at the only charged cusp companion point lying in `S`.  After
translating the target equation, the cusp appears there only as the pulled-back
divisor germ `b(f(u_c)+p,g(u_c)+q)=0` of `T`.  In particular, no local
eigenvalue or Newton polygon at `u_c` can detect global non-local-finiteness.

There is an exact infinite-jet restatement.  **PROVISIONAL** global
non-local-finiteness implies that, for `X_f`, at least one of the algebra
generators `A,U,Z`, expressed in `C[[p,q]]`, is killed by no nonzero
constant-coefficient operator `P(X_f)=P(kappa partial_q)`; otherwise all three generator
orbits would be finite and `X_f` would be locally finite.  Equivalently that
generator is not a finite double sum
`sum_lambda sum_(0<=j<m_lambda) a_(lambda,j)(p)q^j
exp(lambda q/kappa)`.
The analogous statement holds for `X_g` with `p` and `q` interchanged.  This
is a condition on the whole formal series, not on its first term.  By
contrast, the translated polynomial cusp germ itself has a finite translation
orbit and cannot be the witness.

The packet does not identify the actual `(3,1)` boundary germ with the
standard ordinary-cusp equation.  The cubic algebra with discriminant
`s^3-w^2` in `...kummer-inverse-collision-control...md:546-575` is explicitly
a compatibility control, not an equation for the charged completion.  A
more specific cusp-boundary expansion would therefore be an untyped
extrapolation.

### 1.3 What is determined along the actual ramification boundary

Literally, the `R_bd`-adic completion of `R=O(S)` is undefined because
`R_bd` is disjoint from `S`.  The full two-dimensional formal neighborhood
requires a chosen `Y` and pole expansions not present in the packet.  There
is nevertheless one exact generic valuation statement.

Let `b(f,g)` be a reduced irreducible equation of `B`.  At its generic point,
the surface fibre partition is `(2,1,1)`.  After completed strict
henselization, the target and the unique ramified factor have the tame form
(`...pseudoplane-companion-threat-map...md:263-303`):

```text
K[[b]] -> K[[s]],             b |-> s^2,                (1.12)
```

with two further unramified companion factors; here `K` is a separable
closure of the function field of `B`.  Since the singular irreducible curve
`B` is neither a vertical nor a horizontal line, both `b_f` and `b_g` are
nonzero at its generic point.  The identities

```text
X_f(b)=kappa b_g,              X_g(b)=-kappa b_f
```

therefore have valuation zero.  If `v(s)=1`, the normal principal parts are

```text
X_f ~ (kappa overline(b_g)/2)s^(-1)partial_s,
X_g ~-(kappa overline(b_f)/2)s^(-1)partial_s.            (1.13)
```

Consequently, for either charged field `D` and a ramified uniformizer,

```text
v(D^j s)=1-2j             for every j>=1.               (1.14)
```

This is exact generic quadratic-ramification pole growth.  It also gives a
global witness.  Some `h in O(S)` has `v(h)=k<0`: if the boundary valuation
ring contained all of `O(S)`, it would have a center on affine `S`, and
separatedness in the common model `Y` would identify that center with the
supposedly deleted generic point.  For either `D=X_f,X_g`, (1.13) then gives

```text
v(D^j h)=k-2j,                                           (1.15)
```

because the leading coefficient is a nonzero residue times
`product_(i=0)^(j-1)(k-2i)`.  The iterates are linearly independent.  Thus,
conditional on the reviewed charged boundary packet, (1.15) is an independent
boundary-valuation proof that both flows are non-locally-finite; it does not
use the **PROVISIONAL** automorphism/LND theorem.

The generic statement does not determine the special two-dimensional cusp
completion, and it does not identify `R_bd`, `Phi`, or a deleted `L_j`.

## 2. Exact invariant on a completed generic coordinate fibre

This section consumes the **PROVISIONAL** parent conclusion at
`...poisson-locally-finite-obstruction...md:384-440`.  For a general value
`a_f`, put

```text
C_f=V(f-a_f) subset S,       D=X_f|C_f,       D(g)=kappa.
```

The map `g:C_f->A1` is surjective etale of degree four.  Let
`Cbar_f` be its smooth projective completion, of genus `gamma_f`, and write

```text
Sigma=Cbar_f-C_f=Sigma_infty disjoint_union Sigma_fin,
r_infty=#Sigma_infty,          s_fin=#Sigma_fin.
```

For `p in Sigma`, let `e_p` be the ramification index of the completed map
`gbar:Cbar_f->P1`.  The following divisor is an exact invariant of the
completed Hamiltonian flow:

```text
div_Cbar_f(D)
 =sum_(p in Sigma_infty)(e_p+1)p
  -sum_(p in Sigma_fin)(e_p-1)p.                        (2.1)
```

Indeed, at a finite deleted point one can choose a uniformizer `z` with
`g-g(p)=z^e`.  At a point over infinity choose it with `g=z^(-e)`.  Since
`D(g)=kappa`, respectively

```text
D=(kappa/e)z^(1-e)partial_z,                            (2.2)
D=-(kappa/e)z^(e+1)partial_z.                           (2.3)
```

There are no zeros or poles on `C_f`, because `g` is etale there.  This proves
(2.1), including attainment at every place.  It also gives exact iterate
growth:

```text
finite p:
 D^j(z)=(kappa/e)^j product_(i=1)^(j-1)(1-ie)
          z^(1-je),

infinity p:
 D^j(z)=(-kappa/e)^j product_(i=1)^(j-1)(1+ie)
          z^(1+je).                                    (2.4)
```

At a finite ramified point `e>=2`, the first coefficient product never
vanishes, so the pole order of `D^j(z)` is exactly `je-1`.

Taking degrees in (2.1), or equivalently applying Riemann--Hurwitz, gives

```text
deg Zero(D)=sum_infinity(e_p+1)=4+r_infty,
deg Pole(D)=sum_fin(e_p-1)=2gamma_f+2+r_infty,
deg div(D)=2-2gamma_f.                                 (2.5)
```

In particular the finite ramification sum is positive.  This turns the local
formula into another global non-local-finiteness witness.  Choose a finite
ramified `p`, and by Riemann--Roch choose `h in O(C_f)` with its only pole at
`p`, of order `M>0`.  Then

```text
ord_p(D^j h)=-M-je                                     (2.6)
```

for all `j`; these iterates are linearly independent.  Since
`O(C_f)=R/(f-a_f)` and `(f-a_f)` is `X_f`-stable, local finiteness on `R` would
descend to the quotient.  Thus (2.6) proves `X_f` non-locally-finite from the
degree-four fibre structure itself.  Interchanging `f` and `g` proves the
same statement for `X_g`.

Equations (2.1), (2.4), and (2.6) are the requested exact invariant and
growth lower bound (in fact equality).  They use neither Picard nor
ML/Derksen, do not identify a flag with a place or cover series, and make no
claim that a valuation floor is attained without the displayed local
uniformizer witness.

## 3. Test against the quartic fibre and monogenic ledgers

### 3.1 Exact necessary degree-four tuples

The reviewed rank-four surface census is

```text
generic B: (2,1,1),       cusp c: (3,1),
omitted node n: (2,2),    e(T)=-3,
```

with `B` irreducible and its normalization `beta_B:A1->B`; see
`...quartic-branch-topology-coordinator-integration...md:100-104,213-227`
and `...pseudoplane-companion-threat-map...md:205-256`.

Choose the target line `{f=a_f}` generally enough to avoid `c,n`, every other
singular point of `B`, all critical values of `f o beta_B`, the singular locus
of `Y`, and tangencies to `B`.
At each intersection the completed base change is explicitly
`C[[b,t]] -> C[[s,t]]`, `b |-> s^2`.  Transversality of `{f=a_f}` to `B`
makes `g-g(p)` a unit times `b`, hence a unit times `s^2`; its curve
normalization therefore has local index two.
Since `S=Y-R_bd` and the line misses the omitted point `n`, there are no other
finite deleted points.  Thus every finite deleted point of the completed map
`gbar:Cbar_f->P1` is the unique missing ramified point of a `(2,1,1)` surface
fibre, and

```text
e_p=2 for every p in Sigma_fin,
s_fin=d_f:=deg(f o beta_B).                              (3.1)
```

Substitution in (2.5) gives the exact equality

```text
d_f=2gamma_f+2+r_f,                                     (3.2)
```

where `r_f` is the number of points over infinity on the completed generic
`f`-fibre.  The pole orders of `g` at those points form a partition
`lambda_f` of four.  Thus the numerical rows not excluded by this invariant
are

| `r_f` | `lambda_f` | `d_f` |
|---:|---|---:|
| 1 | `(4)` | `2gamma_f+3` |
| 2 | `(3,1)` or `(2,2)` | `2gamma_f+4` |
| 3 | `(2,1,1)` | `2gamma_f+5` |
| 4 | `(1,1,1,1)` | `2gamma_f+6` |

Here `gamma_f` is any nonnegative integer; the table asserts necessity, not
attainment.  Equivalently,

```text
d_f>=3,       d_f-r_f-2=2gamma_f in 2Z_(>=0),            (3.3)
e(C_f)=-4gamma_f-2r_f<0.                                (3.4)
```

On this stratum (2.1) says that `X_f` has simple poles at exactly the `d_f`
finite deleted places of `Cbar_f`, while its zero multiplicities at infinity
are obtained by adding one to the parts of `lambda_f`.  There are at least
`d_f+r_f>=4` punctures.

Interchanging the target coordinates gives the separate necessary identity

```text
d_g:=deg(g o beta_B)=2gamma_g+2+r_g,                     (3.5)
```

with the same four-row partition table for `lambda_g`.  No relation between
the two genera or the two infinity partitions is present in the packet.

This closes only the following exact sub-strata:

```text
d_f<=2 or d_g<=2;
d_h-r_h-2 notin 2Z_(>=0) for h=f or g;
lambda_h not a positive partition of 4 of length r_h.   (3.6)
```

For orientation, `d_h=3` forces `(gamma_h,r_h,lambda_h)=(0,1,(4))`;
`d_h=4` forces genus zero, `r_h=2`, and partition `(3,1)` or `(2,2)`.
No exclusion is extrapolated to any larger projection degree or to any tuple
which passes (3.2)--(3.5).

Because this table consumes the parent generic-fibre statement, the table and
the closures in (3.6) are themselves **PROVISIONAL** pending that parent's
different-model review.

### 3.2 The inverse-Kummer locus does not alter the flow divisor

Under the **PROVISIONAL exact-model identification**, the primitive
pseudo-plane parameters of the present ring are
`(mu,r_pp)=(2,2)`, where `r_pp` is the pseudo-plane type parameter.  For the
reviewed minimal-degree strict-block replacement, `mu=d1`; hence here

```text
mu=d1=2.                                                 (3.7)
```

Normalize the ruling coordinate by `t=A` and its multiple-fibre value by
`a_rho=0`.  The **PROVISIONAL** inverse-Kummer identities, with the residual
function renamed `r_E`, are

```text
div(c_0 o pi)=Phi+E,             [E]=-[Phi],
(t-a_rho)r_E=(c_0 o pi)^2,       div(r_E)=2E.             (3.8)
```

Thus this is the inverse of the original Kummer class, not a second class.
In completed local sheet equations (lowercase `u,v`, unrelated to the ring
generator `U`), the same **PROVISIONAL** successor gives

```text
J_t=t_1-t_2=u^2-v^2=(u-v)(u+v).                         (3.9)
```

More generally its displayed formula is `u^mu-v^mu`; quartic degree is the
degree of `P_t` in its generator variable and does not bound `mu` or the
target degrees of its coefficients
(`...kummer-inverse-collision-control...md:421-423`).

The valuation content of (3.9) is exact.  If a rank-one valuation `w`
centered at the collision has `alpha=w(u)>0`, `beta=w(v)>0`, then

```text
w(J_t)=2 min(alpha,beta),        alpha!=beta;
w(J_t)>=2alpha,                  alpha=beta,             (3.10)
```

with equality in the second row unless the two initial squares agree.  If the
two immersed branches are transverse, `(u,v)` is a regular parameter system
and the Newton segment is `conv{(2,0),(0,2)}`.  In the tangent stratum (3.10)
remains valid, but the Newton polygon in chosen regular parameters is not
determined.  Off `B`, the selected pair contributes
`2w(J_t)` to the order discriminant.  The full discriminant valuation is at
least this number, with equality only when every other sheet difference is a
unit; the discriminant of the finite-etale normalization remains a unit.

This is not one of the places in (2.1).  The **PROVISIONAL** collision
alternatives are exactly

```text
L0: z_0 outside B;
L1: z_0 an ordinary (2,1,1) point of B.                  (3.11)
```

The collision is never the cusp `c` or omitted node `n`, and tangency versus
transversality of its two immersed branches remains open
(`...function-pair-cyclic-normalization...md:328-342` and
`...kummer-inverse-collision-control...md:249-289`).  In `L0` both points are
interior etale points.  In `L1` they are the two interior companion points;
the ramified boundary point is a third, distinct point.  Thus `J_t` records
failure of the primitive element to separate etale sheets, not a new deleted
point or a change of any `e_p` in (2.1).

Equivalently, on `V=A2-B`,

```text
div(Disc(P_t))=2 I_t
```

is an index-of-order identity.  It supplies neither normalized ramification
nor an Orevkov--Chau local-degree correction.  At an ordinary `B` point the
separate norm identity is only

```text
P_t(a_rho)=lambda b^(kappa_B)c_0^2,
```

where `kappa_B in Z` is uncontrolled and may be negative.  Clearing a pole
can lower the degree of the relation modulo `b`.  These are the
**PROVISIONAL** negative controls in
`...index-at-infinity-resultant-control...md:190-296,375-433`; no boundary
unit is charged here.

Nor does the flow divisor determine the reviewed cyclic companion number
`N=#(T intersect Phi)`.  In the separately reviewed cyclic replacement put
`H_cyc=pi o f_2:A2_(x,y)->A2`.  To avoid overloading `D` for a vector field,
call the pullback curve `D_B=V(b o H_cyc)` and its generic `x`-fibre
cardinality `n_gen`; the subscript `x` below is this cyclic-source coordinate,
not the normal parameter `u` or a coordinate-fibre place.  At `mu=2` the
exact ledger is

```text
e(D_B)=-6-N,
sum_(nonzero orbit representatives)(n_gen-#(D_B)_x)=N+3. (3.12)
```

This is `...function-pair-coordinator-integration...md:36-43` specialized to
the present multiplicity.

Put `epsilon_c=1` when `u_c in Phi` and `0` otherwise.  Always
`N>=epsilon_c`.  In `L1` the two collision preimages are distinct from the
cusp point, so `N>=2+epsilon_c`; in `L0` the collision gives no lower bound
beyond `epsilon_c`.  Equations (2.1) and (3.12) count different curves and no
term can be transferred between them from the packet hypotheses.

### 3.3 Full surviving packet coordinates and cheapest discriminator

No forced packet stratum contradicts (2.1).  The region not excluded by this
lane is contained in the following necessary-coordinate list; no listed
tuple or cross-combination is asserted to occur:

1. **PROVISIONAL** `mu=d1=2` and, for each `h=f,g`, a tuple
   `(d_h,gamma_h,r_h,lambda_h)` satisfying its copy of the four-row table;
2. cusp incidence `u_c in Phi` or `u_c notin Phi`;
3. **PROVISIONAL** collision location `L0` or `L1` in (3.11), never `c,n`;
4. **PROVISIONAL** transverse or tangent immersed collision branches; and
5. the **PROVISIONAL** uncontrolled integer `kappa_B`; also
   `N>=epsilon_c`, strengthened to
   `N>=2+epsilon_c` in `L1`.

The single cheapest discriminator is

```text
Theta_h=d_h-r_h-2.                                      (3.13)
```

Compute `d_h` from the pole order of `h o beta_B` at the one place of `B` at
infinity, and compute `r_h` as the number of poles of the mate on the
completed generic `h`-fibre.  If `Theta_h` is negative or odd, that exact
projection stratum is impossible; if it is nonnegative even, it fixes
`gamma_h=Theta_h/2` and the partition row to test next.  The current packet
does not supply either number.  Determining them requires an actual SNC
boundary/pole expansion of the charged pair, not a CAS elimination; no local
computation was launched and no AWS registration is presently justified.

## 4. Maximum-safe conclusion

The valuation lane does not close a named wild mixed/mixed horn row.  It
proves the following exact conditional statements.

1. Under the **PROVISIONAL exact-model identification**, the retained multiple
   fibre has completion `C[Z][[U]]`, bracket (1.3), and associated-graded
   formula (1.5).  Charged first jets obey the
   unimodular identity (1.9), but their degree `-1` symbols are locally
   nilpotent and do not detect wildness.
2. The only point of `S` lying over the charged target cusp is the etale
   companion, where both fields are constant translations.  The completion
   at the length-three ramified
   boundary point is typed **OPEN** because the packet supplies no actual
   cusp Puiseux germ or pole expansion.
3. At the generic true boundary, both flows have degree `-2` normal symbol.
   Formula (1.15) supplies an actual element of `O(S)` with exact pole growth
   `k-2j`, proving non-local-finiteness from the reviewed boundary packet
   without the **PROVISIONAL** LF/LND classification.
4. Under the **PROVISIONAL** degree-four generic-fibre input, the divisor
   (2.1) and iterate formula (2.4) are exact.  They close only the projection
   sub-strata (3.6); all tuples in the four-row table remain unexcluded.
5. The **PROVISIONAL** locus `u^2-v^2=0` survives this test in every allowed
   location and tangency stratum because it is monogenic index, not normalized
   ramification.  No Orevkov--Chau term, second ruling, or independent Kummer
   class follows.

The cheapest next exact datum is `(d_h,r_h)` for either charged coordinate,
obtained from one genuine SNC boundary model and tested by `Theta_h`.  Until
such a model is supplied, the cusp Newton polygon, the special boundary
leading terms, and any transport from monogenic index to an actual dicritical
jump remain typed **OPEN**.

<!-- BODY-END -->
