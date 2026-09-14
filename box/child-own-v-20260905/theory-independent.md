# Independent own-child root-count theory notes

This note uses the frozen Moh PDF and gate checked by the root agent. It is a
conditional calculation for a source pair with the campaign's necessary data;
it is not a realization assertion. The printed locations below were checked
from fresh page renders, notably pp.180 and207. No ledger or old artifact is
modified.

## 1. Coordinate map and characteristic data

Put q=d_s, v=V_s, u=q-v and c=u/q. Proposition6.3, pp.197–198, under its
minor-disc radius hypothesis, uses y=gamma^(-u), z=y-beta*x-e, and
z=A(gamma)+pi*gamma^v, with beta nonzero and deg A<v. Thus

    x=(gamma^(-u)-e-A(gamma)-pi*gamma^v)/beta.

The new coefficient parameter is gamma and the polynomial/root variable is
pi. Its infinity is gamma->infinity, whereas the polynomializing minor disc
in Proposition6.3 is about gamma->0. These places must not be identified.
The transformed G,F,T_j have exact pi-degrees c*n,c*(-M_1),c*(-mu_j).
The retained characteristic support is M'_i=c*M_i, i<s, with n'=c*n;
d'_i=c*d_i for the retained prefix. This follows from the characteristic-jet
Hensel argument, not from dividing a list of labels alone: canonical
approximate-root relations persist after substitution, every strict lower
canonical weight remains strict, and the prescribed exact degrees of the
successive approximate roots force the first terms outside the successive
Puiseux sublattices at c*M_i. The p.150 criterion counts nonzero constant
coefficients. The recurrence, directly derived from that definition, is
mu_1=M_1 and mu_j=(d_{j-1}/d_j)mu_{j-1}+M_j-M_{j-1}.

The raw last retained gcd is u. When u=1 this closes the raw characteristic
chain. A terminal M'_{s-1}=n'-1 is the p.174 exceptional pair and must be
dropped under the campaign's effective-pair convention; after the drop the
boundary gcd need not be1. A child with u>1 has only a retained finite prefix:
its later own characteristic support is not determined by these degrees.
The Prop6.3 radius hypothesis is automatic from Prop6.4 when u=1. No such
blanket licence follows when u>1.

## 2. Root-count meaning and top inversion

Definition5.1(1), p.179, means

    V'_i = #roots(G in the actual child D'_{i-1}) / (n'/d'_i).

Counts include multiplicity. The normalization ratio n'/d'_i=n/d_i is
unchanged, but its numerator is a root count in a newly located disc.

Let delta=delta_{s-1}>0 have reduced fraction a/b, and h=d_{s-1}/q.
Set N=n-M_{s-1}; the source radius formula simplifies to

    delta=(u*N-q)/(v*N-q).

The source major D_{s-1} contains (n/q)v>n/2 roots of g. Distinct Galois
conjugate discs of the same radius are disjoint; hence this disc is invariant
and its truncated centre is rational. After its slope and constant are
normalized to zero, it has zero centre, because 0<delta<1.

Proposition4.6, p.170, gives g_D=p^(n/d_{s-1}), with deg p=v*h. Full
Galois symmetry, not the cumulative denominator of an abstract radius list,
forces

    p(xi)=const * xi^z product_nu (xi^b-c_nu)^r_nu,
    c_nu nonzero distinct, z+b*sum r_nu=v*h.

For one orbit write its initial plane-curve equation y^b*x^a=c_nu. In the
new chart this becomes x^a=c_nu*gamma^(u*b). There are a distinct initial
x coefficients, each with the same multiplicity r_nu*n/d_{s-1}. This is a
projection-degree computation on a physical place, and does not identify a
place with one of its b source cover series. The resulting child pi growth
is R=u/delta-v. Each corresponding nonzero child coefficient therefore has
normalized count r_nu. All other child roots have the zero coefficient at
this growth, and its normalized count is

    W_zero=u*h-a*sum r_nu
          =u*h-delta*(v*h-z).

The child top radius is -R. Algebra gives
R=(v-u)q/(u*N-q), in agreement with the retained own characteristic data
and the monomial Jacobian exponent ell=v-u-1. The source finite-x points
above y=0 contribute to the zero remainder; their count is supplied by the
exact total degree n'. The other source tangent y~beta*x belongs to
Gamma->0 and supplies no larger child growth.

Thus a selected nonzero source factor with multiplicity V_{s-1} gives
W_{s-1}=V_{s-1}, whereas a selected zero factor gives
W_{s-1}=u*h-delta*(v*h-V_{s-1}). The row does not itself name zero or
nonzero coefficients. Equality of labels is a consequence only on the
first branch.

## 3. First support cannot hide between source radii

Proposition5.3, p.180, defines the next disc as the minimal disc containing
all selected roots of g and the relevant approximate-root polynomials.
Suppose all selected coefficients so far are zero, after the allowable
linear and constant normalization. The current selected set is invariant
under Galois conjugation over k((t)), because it is described by ord y>delta.
If the next truncated common centre had its first nonzero coefficient at
e strictly between the current and next radii, minimality says every root
in that set shares that coefficient. Galois invariance then forces e to be
an integer: otherwise conjugation gives a different coefficient and forces
a separation at e, contrary to the next radius's minimal definition.

For the source rows at issue every source radius is <1, directly from
Def5.1's positive numerator/denominator formula. The initial retained radius
is >=0: n-M_{s-1} is a positive multiple of q, so u*N-q>=0. A common
constant is translated away, and no positive integer lies in these gaps.
Consequently, before the first nonzero coefficient, the centre is exactly
zero and the first nonzero coefficient must occur at a recorded source
radius delta_j, j=s-1,...,2. A numerical lattice point produced by taking
the lcm of denominators of prior ZERO radius coefficients is not a possible
first support coefficient. Zero has no denominator.

At such a zero-centre node the applicable cyclic orbit length is the FULL
reduced denominator b_j of delta_j. Using only the incremental denominator
A_j of the abstract radius list is insufficient. This is an additional
necessary consequence of the actual root configuration. It is not an
assertion that a passed orbit condition realizes a polynomial pair.

If the raw initial radius is0, normalization makes the selected constant
coefficient zero. This is the n'-1 dropped-tail case. Its inverse root contribution
is0; the raw all-roots child count is the relevant remaining gcd. The next
positive radius starts the effective inversion analysis.

## 4. Whole-route count recipe

Write R_i=(n/d_i)V_i for the source count in D_{i-1}; R_s=(n/q)v.
Let j be the first selected nonzero coefficient (delta_j>0). For every
k>j the selected coefficient is zero. Start C=n' and process k=s-1
through j+1 in decreasing order:

    C <- C-delta_k*(R_{k+1}-R_k),
    W_k=C/(n/d_k).

The decrement is exact: R_{k+1}-R_k source cover-series roots leave at
order delta_k, and inversion multiplies that aggregate projection count
by delta_k. Full orbit symmetry makes the result integral for an actual
configuration. Equivalently,

    W_k=d'_k-d_k*sum_{l=k}^{s-1}
                    delta_l*(V_{l+1}/d_{l+1}-V_l/d_l).

At the first nonzero coefficient, W_j=V_j. For every i<j, W_i=V_i.
For the latter assertion fix one inverse initial coefficient. Local formal
inversion has a nonzero leading derivative and maps each further source
subdisc to an inverse subdisc with the same number of roots of g and of
every retained approximate root. The b conjugate source discs at the
first coefficient become a inverse coefficient discs, each preserving
these per-disc counts. Later ramification does not invalidate this local
bijection. With n'/d'_i=n/d_i, normalized counts are equal.

The disc correspondence is also metric, rather than inferred from labels.
Before the first nonzero coefficient its inverse radius is

    delta'_k=v-u/delta_k.

After the first coefficient e=delta_j, a source radius delta_i maps to

    delta'_i=v-u-(u/e)*(1-delta_i).

Together with the retained approximate-root degree data these identify the
same successive own child discs; the common polynomial terms introduced
by A(gamma) translate their centres and do not change counts. The child's
Jacobian is a monomial, so one must use the corresponding radial identities,
not literally Def5.1(3) with constant Jacobian.

For a reduced campaign source, Proposition5.6 (pp.188–190) rules out the
all-zero D1 centre: its stated alternatives are a coordinate pair or an
automorphism reducing the degrees. This is a reduction statement, NOT a
proof that no arbitrary source pair can have an all-zero centre. Within
the campaign's reduced-source scope it forces such a j>=2. It follows
that W_2=V_2 for every actual licensed descendant in that scope. This is a
new disc-identification proof for level2; the old equality of scale factors
alone did not establish it. Therefore the elementary inequality W_2<=d'_2
can legitimately be consumed there. Outside the reduced-source hypothesis,
this level2 conclusion needs an all-zero branch case and is not automatic.

## 5. Finite alternatives and their exact logical type

For each prospective first index j, require delta_j>0. At every earlier
zero node k>j put P_k=V_{k+1}d_k/d_{k+1}; the necessary orbit condition is
P_k-V_k>=0 and divisible by the FULL b_k=den(delta_k). At j a selected
nonzero orbit requires b_j V_j<=P_j. (An integral radius0 is removable
and cannot be the first nonremovable coefficient.) These conditions yield
at most s-2 prospective first-support indices. Each index determines the
entire vector W by the formula in section4. Thus projecting this finite
list gives finite per-level alternatives, with correlations retained by
storing the whole vectors.

This is a finite NECESSARY OUTER SET unless further source conditions are
checked. Other necessary constraints include: the p/q differential equation;
the squarefree q degree and its cyclic orbit capacity; every nonselected
major branch's required continuation; and the actual normalized counts'
integrality. A passed numerical branch is not attained by an exhibited
source pair. It is incorrect to label all outer-set members realizable.
If the outer set is empty, no reduced actual source can have that first-
support route: report a separate necessary-source-configuration obstruction.
Do not infer any arbitrary own V by ex falso, or call an empty set a
DETERMINED value. Partial forced coordinates (for example a forced zero
top split) remain useful conditional calculations even when no complete
reduced route survives. Conversely a singleton nonempty outer set makes
that coordinate conditionally DETERMINED for every possible actual source;
it does not establish that such a source exists.

Child root totals and the own major bounds may be used to detect a source
route inconsistency after computing the physical counts. They should not
be imposed merely to cap the values before auditing U-NEG or C-TOP. In
particular, an elementary U-NEG contradiction for the forced W2=V2 is
valid in the reduced, licensed scope even when no complete source route
exists; it does not rely on declaring a fictional child for an empty set.

## 6. Printed and gate controls

Fresh p.207 transcription (n',m',M'_2,V'_2,delta'_2,delta'_1,J):

    (16,12,13,3,-1,1/4,X)
    (21,14,16,2,-1/2,7/6,X)
    (21,14,18,5,-1,1/3,X)
    (15,10,11,3,-1,1/2,X^2)
    (15,10,11,2,-1,4/3,X^2)

The source is s=3 in all five; the first nonzero coefficient must be at
j=2, hence own V2 is forced to the printed value. These are genuine
source-to-descendant numeric checks, not evidence that copying every
higher V is valid.

The source (99,66) printed on p.202 has M=(-66,77,97), V=(8,8).
It is absent from the p.207 transformed table. Here q=11,u=3,v=8;
formal retained labels would be (n',m')=(27,18), M'=(-18,21), with
terminal retained gcd3 and a separate unresolved Prop6.3 radius licence.
The original printed source labels must stay (-66,77,97); no p.207 child
with those labels is printed.

For the gate row (180,120), M=(-120,132,150,178), V=(2,4,5),
q6,u1,v5,h2,delta3=1/6. The source top p has degree10; V3=4 cannot
be nonzero because6*4>10, so p=xi^4(xi^6-c) and the own split is
15+15. Thus W3=1 while W2=2. The V2=3 alternate has W3=1,W2=3.
At the next zero-centre source node delta2=1/5, P2=20, so the selected
V2=2 or3 is necessarily nonzero; no hidden earlier fractional centre
coefficient is possible by section3.

For (96,72), M=(-72,36,78,94), V=(4,3,5), q6,u1,v5,
delta3=1/7, P3=10 and z3=3; its forced own top count is1 and split8+8.
The further full-stabilizer route can be incompatible. Preserve this
forced-top calculation without presenting the row as a realized child
or overwriting it with vacuous data from an empty complete-route set.

## 7. Independent metric check and the dropped-tail obstruction

The root agent and this audit independently found that multiplying the
constant-Jacobian Def5.1 radius formula by ell+1 AFTER the n'-1 drop is
wrong in general. In the 222 u=1 nonempty first-support candidates, all576
non-dropped per-level comparisons agree with the explicit inverse metric,
but104 dropped per-level comparisons disagree (12 dropped comparisons
happen to agree). For parent108/72, M=(-72,84,104,106), V=(8,8,3), the
first support is j2. The actual inverse radii are delta'_2=0,delta'_1=1/3;
the old dropped formula gives -2/5,0. Therefore radii must be generated
from the actual inverse metric; the dropped effective-list formula is not
an identification theorem.

The following apparent additional obstruction to all90 dropped rows is
OPEN and MUST NOT BE PROMOTED; the translation audit below blocks it. Proposition6.2
only states the separate y- and z-degrees; it does not by itself force a
monomial z-leading coefficient (p.198's first proof line writes y^k+...).
In contrast, the literal EXACT MONICITY in pi asserted by Proposition6.3
forces it. If H(y,z) is one of the retained source polynomials, of z-degree
N_H=u*(-mu_H)/q, write its z-leading coefficient L_H(y). The prescribed
substitution gives pi-leading coefficient

    gamma^(v*N_H) L_H(gamma^(-u)).

If H(sigma) is monic in pi, this coefficient is constant nonzero. The
Laurent substitution is injective, so

    L_H(y)=constant*y^(v*(-mu_H)/q).

In particular, for C nonzero, H(y,z) cannot have a root branch z->infinity
as y->C: its z-leading coefficient is nonzero at C, so roots remain bounded
in the local y-C Puiseux field (the reciprocal equation has nonzero constant
term and no reciprocal root tending to0).

A dropped row has u=1 and n-M_{s-1}=q, hence delta_{s-1}=0. Normalize the
selected source constant centre to0. At that source disc, Proposition4.6
supplies the retained T_{s-1} leading polynomial p^A q_0, where q_0 is
squarefree and deg q_0=V_s(n-M_{s-1})/q=v>=3. Its nonzero roots give
source branches y->C nonzero while x (equivalently z) tends to infinity.
This contradicts the preceding monicity consequence for that retained
polynomial. For19 of the90 dropped rows p itself may be monomial, so an
argument involving only g misses them; the squarefree q_0 in T_{s-1}
supplies the remaining obstruction. This is a necessary-data contradiction
under Prop6.3's full hypotheses, not a licence to discard the n'-1 pair and
silently reuse constant-Jacobian radius identities.


**Translation audit of the apparent monicity obstruction (OPEN).** A source
translation y->y-C appears to preserve the printed radius hypotheses while
changing L_H(y) to L_H(y+C). Repeating the naive monicity argument would
force that coefficient to be a pure power centred at every C, which is
impossible for positive degree. Therefore the special normalization/unit
convention used by the printed monicity conclusion must be pinned before
using it to exclude arbitrary finite-y pole locations. The preceding
apparent90-row obstruction is recorded as an audit question only; it is
not a promoted kill. For the deliverable use actual inverse metric radii
and type the dropped-tail effective tower correspondence OPEN where the
p.174 constant-Jacobian convention has not been transferred to the child.

**Resolution for the dropped rows in one fixed licensed chart.** The preceding
arbitrary-translation monicity argument is unnecessary. The p.170 exponent
A=(-mu_{s-1}+M_{s-1}-n)/d_{s-1} was checked exactly on all90 dropped rows:
it is integral and lies between13 and341. Thus q_0 actually divides the
retained T_{s-1} initial polynomial, with no cancellation. There are at least
three distinct source constant residues among its roots. Whatever source
constant normalization the licensed chart uses, at most one residue is0;
choose a nonzero residue C. Its source root branch has x->infinity,y->C.
In the FIXED Prop6.3 map gamma=y^(-1/u), a finite choice of inverse root gives
gamma->C^(-1/u), finite and nonzero, and

    pi=(y-beta*x-e-A(gamma))/gamma^v -> infinity.

But T_{s-1}(sigma) is, by Prop6.3(1),(2), a monic pi-polynomial over k[gamma].
Every pi-root is integral over k[gamma], so no root has a pole above a finite
gamma point. This is the contradiction. It is unaffected by choosing a
different source constant normalization, because no single translation can
send all three distinct residues to0. This fixed-chart proof validates a
separate necessary-data obstruction for all90 dropped rows under the full
printed Prop6.3 conclusions. It does not require the erroneous assertion
that leading coefficients are pure powers after every arbitrary translation.
