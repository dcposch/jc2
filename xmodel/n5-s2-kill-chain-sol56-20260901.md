# N5-S2 kill chain: the PI1-S4-shaped survivor at N=5

## 0. Scope, source integrity, and fail-closed conventions

The mandated header skeleton was created before any source was opened.  The three
frozen inputs were then hashed, still before reading, and all matched:

```text
48d417d6980e52d61550a733f0dcded7d26a0c4e127677ac73bd544a8a00713b  b0-reducible-n5-opus5-20260831.md
bd6443b34e95213b0b2950e45c896417c492487c38a0a721eae4977d1e73f5d6  b0-reducible-n5-hostile-review-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Hereafter `B0:n`, `REV:n`, and `CNA:n` mean line `n` of those frozen
files, respectively.  A fact called *reviewed* below is limited to the corrected
promotion recommendation in `REV:142-164`; an assertion in the original B0 report
that REV withheld is not silently restored.  The prompt's ROW-KILL description is
used as a route template.  Every new $S_5$ statement is proved here or typed OPEN;
no $S_4$ conclusion is transferred merely by changing a subscript.

Notation is deliberately separated.  The curve-normalization parameter is $t$;
the unique normalization place at infinity is $\widetilde Q_\infty$, its physical
image on the projective curve is $P_\infty$, a physical affine double point is
$z$, $s_l$ is a dicritical-to-normalization cover degree, and the five letters
are sheets of the Keller covering.  The genus $g_L$ appearing
in B0's transversal-line formula is not the genus of the rational curve.  Floors
are used only as floors, and neither P3a nor P3b is asserted to be attained by a
Keller map.

No CAS or unbounded computation was run.  Literature downloads were streamed with
a 30-second timeout and hashed without creating source files.  No charged file,
canonical ledger, or `jc2-lean` artifact was edited or inspected.  This report
makes no new exit-price assertion.

## 1. Reviewed S2 pinning and exact curve data

Write $D=D_A$ for the unique component with nontrivial meridian.  The
reviewed ownership rows are exactly

| row | dicritical ownership | component data $(W,a)$ |
|---|---|---|
| P3a | $(\mu,\operatorname{corr},s)=(2,0,1)$ over $D$; one $(1,0,1)$ over each of two other components | $(2,3),(1,4),(1,4)$, $m=3$ |
| P3b | $(2,0,1)$ over $D$; both $(1,0,1)$'s over one other component | $(2,3),(2,3)$, $m=2$ |

This is `B0:233-244,506-515`, confirmed at `REV:38-56,68-78`.  The
cover-ramification floor forces every displayed $s=1$, not equality by
attainment (`REV:48-54,109-120`).  Consequently every component has
normalization $\mathbb A^1$, one place at infinity, and a birational polynomial
parametrization.  On $D$, zero correction makes the normalization map immersive.
Thus $D$ is irreducible and rational and every affine singularity has exactly
two smooth branches.  If their contact is $k_z\geq1$, the germ is
$A_{2k_z-1}$ and $\delta_z=k_z$; tangency is allowed.

One incidence correction is needed.  At a self-double point of $D$, the B0
shorthand $a_z=1$ assumes that no trivial-owner component also passes through
$z$.  In P3a one $W=1$ component may pass through it, in which case $a_z=0$
and its trivial boundary cluster supplies the fixed letter; two such components
cannot pass there.  In P3b its $W=2$ companion cannot pass through a two-branch
point of $D$.  This follows directly from LOC at `B0:362-372` and is the S2
version of REV's binding incidence repair at `REV:93-95`.  It does not change the
local $S_5$ constraint in §2.

Let $d=\deg \bar D$, let $r_1$ be the number of nodes, and put
$T:=\sum_{k_z\geq2}k_z$.  Let $M_\infty$ denote the promoted embedded
resolution quantity $\operatorname{mult}_{P_\infty}\bar D+\beta_h-1$ at the
infinity branch.  The exact genus budget is

\[
  \delta_{\rm aff}=\sum_{z\in\operatorname{Sing}D} k_z=r_1+T,\qquad
  \delta_\infty+\delta_{\rm aff}=\frac{(d-1)(d-2)}2.                 \tag{1.1}
\]

The promoted N-A-RES gate says
$M_\infty+2T\leq3d-3\Rightarrow\pi_1(\mathbb C^2-D)=\mathbb Z$
(`CNA:44-49`; coefficient audit `REV:122-136`).  Hence any still-live S2
candidate necessarily lies in the complementary integer range

\[
                 M_\infty+2T\geq3d-2.                              \tag{1.2}
\]

There is **no reviewed exact degree, upper degree bound, delta-sequence, Puiseux
characteristic, or value of either side of (1.1)**.  B0's formula
$d=3+2g_L+\Sigma_\infty\geq4$ is internally consistent, but REV withholds it
pending custody for the generic-line $\pi_1$-surjection (`B0:379-428`;
`REV:99-107,154`).  Here $g_L$ is a transversal-preimage genus.  It must not be
set to zero because $D$ is rational.  Also, raw $d$ is coordinate-dependent;
the coordinator requires degree payoffs to use $d_{\min}$ (`CNA:60-68,103`).

The only reviewed infinity pin beyond “one place” is Chau's common leading-pair
form (`B0:537-548`, confirmed in `REV:89,151`): in the Keller target coordinates
each component is parametrized at leading order by

\[
 (A_i t^{m_i r}+\cdots, B_i t^{m_i s}+\cdots),\qquad \gcd(r,s)=1,
\]

with the same $(r,s)$, and all components meet the same physical point of
$L_\infty$, denoted $P_\infty$.  The multiplier $m_D$, the later series, and the
denominator-shedding sequence are unpinned.  In particular, this leading
statement is not a ROW-NF and does not decide whether the infinity braid is torus
or cable.

## 2. The $S_5$ monodromy problem and the failed $S_4$ resolvent transfer

The reviewed monodromy is a necessary representation

\[
 \rho:\pi_1(\mathbb C^2-D)\twoheadrightarrow S_5,\qquad
 \rho(\text{meridian})\sim(2,1,1,1).                              \tag{2.1}
\]

All other component meridians are trivial, so the original representation factors
through this one-curve complement (`B0:550-569`; `REV:64-66,146-152`).
Transitivity comes from connectedness of the five-sheeted cover, and a transitive
group generated by transpositions is $S_5$: its transpositions are edges of a
connected graph on five vertices.  At every self-double point the two branch
meridians are **disjoint** transpositions.  Equal transpositions fix three letters,
and transpositions sharing one letter fix two, whereas the reviewed local fibre has
one fixed letter.  The incidence correction in §1 merely changes where that fixed
letter is represented; it does not alter this conclusion.

### 2.1 No nonabelian quotient resolvent

The normal subgroups of $S_5$ are $1,A_5,S_5$.  Indeed $A_5$ is simple, and a
normal subgroup meeting $A_5$ trivially would inject into $S_5/A_5$; a nontrivial
order-two normal subgroup would then be central, contrary to $Z(S_5)=1$.  Therefore

\[
                         S_5/A_5\simeq C_2                         \tag{2.2}
\]

is the only nontrivial proper quotient.  There is no $S_5\twoheadrightarrow S_3$,
and no analogue of $S_4\twoheadrightarrow S_4/V_4\simeq S_3$.  In particular,
the N=4 chain “transpositions to transpositions in a triple cover to normal-triple-
plane classification” stops at its first arrow.

There are useful *permutation resolvents*, but they are not quotients:

| action | degree | image of a natural transposition | consequence |
|---|---:|---|---|
| natural $S_5/S_4$ | 5 | $1^3 2$ | the original quintic cover |
| sign $S_5/A_5$ | 2 | $2$ | double cover; loses the $A_5$ layer |
| six Sylow-5 subgroups | 6 | $2^3$ | classical sextic resolvent, faithful |
| two-element subsets | 10 | $1^4 2^3$ | faithful degree-ten resolvent |

For the degree-six line, a stabilizer is the order-20 normalizer of a 5-cycle.
A transposition normalizes no Sylow-5 subgroup (the involutions in that affine
normalizer have natural type $1\,2^2$), hence has no fixed point and type $2^3$.
For the degree-ten line, $\{1,2\}$ and the three pairs disjoint from it are fixed,
while $\{1,j\}$ and $\{2,j\}$ are swapped for $j=3,4,5$.  Neither action produces a
simply branched triple cover.  Calling either one “the $S_5$ quotient” would
confuse an associated cover with a normal quotient.

The sign factor is exact but weak.  It makes the Galois closure factor through the
double plane fixed by $A_5$; the remaining layer has group $A_5$.  For even $d$,
sign already kills the infinity meridian, but an even permutation can still be a
nontrivial value of $\rho(\gamma_\infty)$.  Thus sign-triviality must not be
substituted for full INF-TRIVIAL.

### 2.2 What full INF-TRIVIAL would give

Let $\gamma_\infty$ be a meridian of $L_\infty$ in the affine complement.  If

\[
                         \rho(\gamma_\infty)=1,                    \tag{2.3}
\]

then (2.1) descends to $\pi_1(\mathbb P^2-\bar D)$.  Algebraic Riemann existence,
followed by normalization of $\mathbb P^2$ in the associated index-five field,
gives a connected normal finite map $f:X\to\mathbb P^2$ of degree five, unramified
off $\bar D$, with generic
inertia a transposition.  There is no divisorial ramification on $L_\infty$.
Because a normal surface is Cohen--Macaulay and the base is regular of dimension
two, this finite map is flat.  Writing
$f_*\mathcal O_X=\mathcal O\oplus E^\vee$ with $\operatorname{rk}E=4$, the trace
discriminant gives, because one-transposition inertia has tame discriminant
valuation one and hence reduced divisor $\bar D$,

\[
                  \mathcal O_{\mathbb P^2}(\bar D)\simeq(\det E)^2. \tag{2.4}
\]

Hence $d$ must be even, the same obstruction obtained from
$\operatorname{sgn}\rho(\gamma_\infty)=(-1)^d$.  For even $d$, (2.4) is not a
contradiction.

Miranda's binary-cubic theory is intrinsically degree three and supplies no
quintic branch identity.  Casnati's degree-five theory, in its modern
Casnati--Ekedahl form, says under the additional Gorenstein hypothesis that $E$
of rank four, a rank-five bundle $F$, and an alternating section determine a
Pfaffian resolution (five $4\times4$ Pfaffians).  It is structure data for covers,
not a theorem that their branch divisor has a scalar torus form.  Normality does
not by itself make the isolated points over $P_\infty$ Gorenstein.  Thus the
direct replacement is the exact question

```text
OPEN[N5-S2-QUINTIC-PLANE]:
  assuming rho(gamma_infinity)=1, exclude a normal flat degree-5 cover
  X -> P2 with Galois closure S5 and simple branch divisor Dbar, where D is
  rational, one-place, and has only two-smooth-branch affine singularities;
  first prove the cover Gorenstein at infinity or extend the Pfaffian theory,
  then classify the allowed Pfaffian discriminants.
```

No such classification is present in the reviewed inputs.  Chisini-type results,
even when their smooth-source/generic-branch hypotheses hold, give uniqueness from
a branch curve rather than nonexistence and therefore do not replace it.

## 3. S2 normal form

The reviewed data permit an affine coordinate normalization, not a degree-minimal
ROW-NF.  After swapping target coordinates if necessary, cancelling equal leading
terms by an affine shear, translating $t$, and scaling/translating the two target
coordinates, write

\[
 \eta(t)=(p(t),q(t)),\quad
 p=t^d+a_{d-2}t^{d-2}+\cdots+a_1t,\quad
 q=t^n+b_{n-1}t^{n-1}+\cdots+b_1t,
\quad d>n\geq1.                                                   \tag{3.1}
\]

The omitted affine-line case has cyclic complement and cannot support (2.1).
The map is birational onto $D$, and immersivity says $p'$ and $q'$ have no
common zero.  For distinct $t,u$, a self-intersection is cut out by the divided
differences

\[
 p^{[1]}(t,u)=\frac{p(t)-p(u)}{t-u},\qquad
 q^{[1]}(t,u)=\frac{q(t)-q(u)}{t-u}.                               \tag{3.2}
\]

Every fibre of $\eta$ has at most two points.  At an off-diagonal zero of (3.2)
the two tangent vectors are nonzero; its local intersection length is the contact
$k_z$, and the total unordered off-diagonal length is $\delta_{\rm aff}$.  These
are conditions on the coefficients, not equations that solve them.

Put $\zeta=1/t$, homogenize as $[X:Y:Z]=[p:q:1]$, and use the chart $X=1$ at
$P_\infty=[1:0:0]$.  With units $\alpha,\beta$,

\[
       u:=Z/X=\zeta^d\alpha(\zeta),\qquad
       v:=Y/X=\zeta^{d-n}\beta(\zeta).                            \tag{3.3}
\]

Thus $I(\bar D,L_\infty;P_\infty)=d$, the initial multiplicity is $d-n$, and

\[
             g:=\gcd(d,n)=\gcd(d,d-n).                             \tag{3.4}
\]

In the original Keller target coordinates, the common-leading-pair notation of §1
gives $d=m_Dr$, $n=m_Ds$, so $g=m_D$.  A later triangular target automorphism may
change this pair, which is why no claim about $d_{\min}$ is made here.  This is the
exact fork left by the reviewed pinning in the chosen coordinates.

* If $g=1$, no later term is needed to shed a denominator.  The degree
  semigroup delta-sequence is $\Delta=(d,n)$; the local leading pair is
  $(d-n,d)$, and the oriented infinity link is the corresponding torus knot
  (equivalently the $(d,n)$ torus braid convention used in §4).
* If $g\geq2$, (3.3) gives only the first cable level.  Birationality and one
  branch require a later gcd tower
  $(d,n,\delta_2,\ldots,\delta_h)$ with final gcd one, but neither the
  $\delta_i$, the approximate-root cancellations, nor the Puiseux pairs are
  pinned.  Consequently $\delta_\infty$ and $M_\infty$ are not functions of
  $(d,n)$ alone.

A triangular automorphism may subtract a polynomial in $q$ from $p$ whenever a
leader is cancellable.  Which leader vanishes is precisely delta-sequence data.
The reviewed cage therefore does **not** license a relation such as $p=r^2$,
$\deg(p-q^2)=6$, or any fixed modulus family.  The honest ROW-NF analogue stops
at (3.1)--(3.4), the immersion/double-fibre conditions, (1.1), and the survivor
inequality (1.2).  Supplying a full delta-sequence (or an exact degree row plus
all approximate-root remainders) is the first missing geometric input.

## 4. Infinity link and braid data

Use the proper vertical projection $x=p(t)$ from (3.1), after a generic affine
shear that preserves its degree, makes $p'$ have simple roots and separated
critical values, separates the singular fibre values, and makes every singular
local fibre transverse to both branches.
A generic fibre has $d$ meridians
$g_1,\ldots,g_d$, and Zariski--van Kampen makes them generate the affine
complement group.  Their transposition images must generate $S_5$, so the edge
graph is connected and, in particular, this lane independently obtains $d\geq4$.
This is not promotion of B0's separate transversal-genus formula.

Riemann--Hurwitz for $p:\mathbb P^1\to\mathbb P^1$ gives total affine vertical
ramification $V=d-1$.  A two-smooth-branch point of contact $k_z$ contributes a
local braid conjugate to $\sigma^{2k_z}$.  Hence the infinity braid
$\beta_\infty\in B_d$ has

\[
 \operatorname{perm}(\beta_\infty)=\text{a }d\text{-cycle},\qquad
 e(\beta_\infty)=d-1+2\delta_{\rm aff}.                            \tag{4.1}
\]

The permutation is a $d$-cycle because there is one normalization place at
infinity.  Formula (4.1) remains true when vertical critical values collide,
with ramification and exponent counted with multiplicity.

For a geometric basis, a meridian $\gamma_\infty$ of the line at infinity is the
ordered boundary product of the $g_i$ (up to the inverse/conjugacy dictated by
the Artin convention).  If $\tau_i=\rho(g_i)$, then

\[
 \rho(\gamma_\infty)\sim \tau_1\cdots\tau_d=:\Pi,
 \qquad \operatorname{sgn}\rho(\gamma_\infty)=(-1)^d.             \tag{4.2}
\]

Only triviality and sign will be used, so the harmless convention in (4.2) is
immaterial.

### 4.1 Coprime infinity

If $g=1$, the roots over a large circle satisfy uniformly
$t_j\sim cR^{1/d}e^{i(\theta+2\pi j)/d}$ and their $q$-values have leading
phase $n(\theta+2\pi j)/d$.  Coprimality keeps the leading points separated,
so the error is isotopic away in configuration space.  Thus, up to conjugacy,

\[
 \beta_\infty=\delta_d^n,\qquad
 \delta_d=\sigma_1\cdots\sigma_{d-1}.                             \tag{4.3}
\]

Here

\[
 \delta_\infty=\frac{(d-n-1)(d-1)}2,\quad
 \delta_{\rm aff}=\frac{(n-1)(d-1)}2,\quad
 M_\infty=2d-n-1,                                                  \tag{4.4}
\]

and (4.1) becomes $e(\beta_\infty)=n(d-1)$, checking (4.3).

### 4.2 Cable infinity and the INF-TRIVIAL stop

If $g\geq2$, put $d'=d/g$ and $n'=n/g$.  The leading motion has $d'$ outer
clusters of $g$ strands and outer torus braid $\delta_{d'}^{n'}$, but the
inner braid and its iterated cabling depend on the missing later entries of the
delta-sequence.  The underlying full permutation and (4.1) are known; a word in
$B_d$ is not.

Blackboard $g$-cabling multiplies every outer crossing into $g^2$ crossings, so
the outer contribution has exponent $n(d-g)$.  If $\iota$ denotes all inner
levels, the exact remaining exponent is

\[
             e(\iota)=d-1+2\delta_{\rm aff}-n(d-g).                 \tag{4.5}
\]

This integer, which may be negative, is only an exponent sum and does not recover
the inner word.  For the conditional old row $(d,n)=(6,4)$ with
$\delta_{\rm aff}=3$, it is $-5$, while the full exponent is $11$;
those numbers do not constitute a ROW-NF for S2.

The N=4 INF-TRIVIAL proof used an exact fold fibre whose disjoint half-twists
identified adjacent meridians, turning $\gamma_\infty$ into a product of squares.
That implication is target-independent: once such a relation is proved, applying
$\rho$ itself kills every square.  S2, however, supplies neither a fold equation
nor a paired collision fibre.  A product of an even number of transpositions can
be a nonidentity even permutation.  Therefore

```text
OPEN[N5-S2-INF-TRIVIAL-CABLE]:
  from the full S2 Puiseux/delta-sequence and an admissible projection, decide
  the boundary product in the cable-fixed transposition tuple; sign is insufficient.
```

For odd $d$, (4.2) already says full INF-TRIVIAL is impossible.  For even $d$, it
remains undecided until the exact cable or an equivalent local-link/ZvK relation
is supplied.

## 5. ROW-KILL / Theorem A test

### 5.1 Coprime S2 is killed

Assume $g=1$ and let $\boldsymbol\tau=(\tau_1,\ldots,\tau_d)$ be the transposition tuple in a
geometric fibre, with $\Pi=\tau_1\cdots\tau_d$.  With the right Hurwitz action
used in §5.2, put $\widehat\delta_d:=\delta_d^{-1}$.  Fixedness by the inverse is
equivalent, and its action can be written

\[
 \boldsymbol\tau\mathbin{\cdot}\widehat\delta_d
   =(\Pi\tau_d\Pi^{-1},\tau_1,\ldots,\tau_{d-1}),
\]

and $\boldsymbol\tau$ is fixed by $\widehat\delta_d^n$, from (4.3).  Since
$\widehat\delta_d^d$ conjugates every entry by $\Pi$, fixedness under
$\widehat\delta_d^{nd}$ says that $\Pi^n$
centralizes the generated $S_5$.  Its centre is trivial, so

\[
                             \Pi^n=1.                              \tag{5.1}
\]

Extend the tuple to a bi-infinite sequence by
$\tau_{j-d}:=\Pi\tau_j\Pi^{-1}$.  Fixedness by
$\widehat\delta_d^n$ is precisely $\tau_j=\tau_{j-n}$.  Translation by $d$ is
transitive modulo $n$ because $\gcd(d,n)=1$, so all entries form one orbit under
conjugation by $\Pi$.  Such a transposition orbit generates $S_5$ exactly when
its edge orbit is connected on five vertices.  Enumerating the seven cycle types
in $S_5$ leaves only

| cycle type of $\Pi$ | connected edge orbit | forced arithmetic |
|---|---|---|
| $(3)(2)$ | all six edges of $K_{3,2}$ | $6\mid n$, $d$ odd |
| $(4)(1)$ | the four-edge star from the fixed letter | $4\mid n$, $d$ odd |
| $(5)$ | a five-cycle (or its diagonal cycle) | $5\mid n$, $d$ even |

Identity, $(2)$, $(2^2)$, and $(3)(1^2)$ have no edge orbit meeting all five
vertices.  The last column uses (5.1) and
$\operatorname{sgn}\Pi=(-1)^d$.  In particular, every hypothetical coprime
representation has $n\geq4$.

Keep $p$ fixed and vary $q$ through polynomials of exact degree $n$ with fixed
leading coefficient.  Coprimality makes every resulting pair birational: the
degree of $\mathbb C(t)/\mathbb C(p,q_\varepsilon)$ divides both pole orders.  The infinity
germ and $\delta_\infty$ therefore stay fixed.  For $n\geq4$, two-point Hermite
evaluation and three-point value evaluation show that common derivative zeros,
nontransverse double fibres, and triple fibres are proper incidence loci.  Choose
a generic analytic arc $q_\varepsilon=q+\varepsilon h+O(\varepsilon^2)$ through
$q$ in their complement for $\varepsilon\ne0$.  The direction $h$ can
simultaneously satisfy $h^{[1]}(a_z,b_z)\ne0$ at every old contact: these are
finitely many nonzero linear conditions (the choice $h=t$ witnesses
nonzeroness).  Thus the nearby map is immersive with only ordinary nodes.

For each contact $z$, choose disjoint normalization discs about its two preimages
$a_z,b_z$.  On their ordered product, $p^{[1]}=0$ is smooth because the projection
is transverse to both branches, and the restriction of $q^{[1]}$ has a zero of
order $k_z$ at $(a_z,b_z)$.  The chosen perturbation changes it in a nonzero
constant direction there.  After fixing a product boundary free of zeros, local
intersection-number conservation gives exactly $k_z$ reduced ordered zeros nearby
for generic $\varepsilon$ (and the reversed ordered copies).  The constant global delta sum
then excludes extra nodes or loss to infinity.

This step does not invoke the unqualified delta-constant $\pi_1$ transport barred
at `CNA:40`.  Because $p$ is fixed, use the same regular base fibre; outside the
chosen singularity discs all vertical-tangency factors isotope unchanged.  Inside
the disc at $z$, the two normalization discs form one fixed two-strand tube.
Its $B_2$ is abelian, so all $k_z$ node factors have the form
$w_z\sigma^2w_z^{-1}$ with one common $w_z$.  If
$G_0=\pi_1(\mathbb C^2-D)$ and $G_\varepsilon$ is the nearby nodal complement group,
Zariski--van Kampen therefore gives the specialization in the required direction:

\[
 G_0\twoheadrightarrow G_\varepsilon
   =G_0/\!\left\langle\!\left\langle
      [w_z(\xi_z),w_z(\upsilon_z)]:z\text{ tangential}
    \right\rangle\!\right\rangle .                               \tag{5.2}
\]

Here $\xi_z,\upsilon_z$ are the two special branch meridians.  Under $\rho$, each
transported pair is a simultaneous conjugate of two disjoint
transpositions, so every added commutator dies.  Thus $\rho$ factors through
$G_\varepsilon$, and the unchanged fibre tuple still generates $S_5$.

For that nodal curve, $T=0$ and (4.4) gives

\[
             M_\infty=2d-n-1\leq2d-2\leq3d-3.
\]

Promoted N-A-RES (`CNA:44-49`) therefore makes its complement group $\mathbb Z$,
which cannot surject onto $S_5$.  This contradiction proves the new, review-gated
result

```text
THEOREM[S5-COPRIME-KILL]: no S2 representation exists when gcd(d,n)=1.
```

This fills B0's order-3/order-4 transfer gap by doing the $S_5$ orbit enumeration,
not by reusing the $S_4$ conclusion.  It needs neither a resolvent nor
INF-TRIVIAL.

Conditional row consequence: the two provisional triangular reductions at
`CNA:76-77`, from the labelled $(6,3)$--$(7,4)$ and $(6,3)$--$(8,3)$ rows to
coprime $(5,3)$ and $(4,3)$, now have an $S_5$ terminal kill by the theorem
above.  This transfers those reductions at their existing row-geometry scope;
it does not assert that either row is pinned by S2.

### 5.2 One cable row also dies: the affine-normal-form pair $(6,4)$

This row is not pinned by S2, but it is the closest N=4-shaped cable and can be
decided without its delta-sequence.  Its six strands form three asymptotically
separated tubes of two strands, and the induced tube braid is $\delta_3^2$.
The leading expansion at infinity supplies this genuine invariant tube system.
In a cable-adapted, based geometric tuple put

\[
 A=\tau_1\tau_2,\quad B=\tau_3\tau_4,\quad C=\tau_5\tau_6.
\]

Use the right Hurwitz convention
$(x,y)\mathbin{\cdot}\sigma=(y,y^{-1}xy)$ and
$\delta_3=\sigma_1\sigma_2$.  Inner two-strand braids preserve each block
product.  Zariski--van Kampen gives literal fixedness of the based strand tuple,
not merely fixedness up to simultaneous conjugacy.  Equivariance of block
products therefore gives
$(A,B,C)\mathbin{\cdot}\delta_3^2=(A,B,C)$.  A direct calculation in this stated
convention yields

\[
 C=A,\qquad ABA=BAB.                                               \tag{5.3}
\]

Put $H:=ABA=BAB$.  Then $HAH^{-1}=B$, so $A,B$ are conjugate.  Each is a
product of two transpositions; hence they are both identity, both 3-cycles, or
both double transpositions.

* If they are identity, the six entries use at most three edges, too few to
  connect five vertices.
* Two 3-cycle supports must intersect.  If their union had five letters, their
  supports would meet once; conjugate to $A=(123)$ and
  $B=(145)$ or $(154)$, direct evaluation violates (5.3).  Thus all factors fix
  a fifth letter.
* For double transpositions, (5.3) is equivalent to $(AB)^3=1$.  If $A=B$, their
  support has four letters.  If distinct, view them as two two-edge matchings:
  product order three occurs exactly when they share one edge (no shared edge
  gives order two with the same fixed vertex, or order five with different fixed
  vertices).  Their unique disjoint-edge factorizations then preserve the shared
  2-set and its complementary 3-set.

Every case gives an intransitive factor graph, contrary to generation of $S_5$.
Thus the whole $(6,4)$ cable is killed, including any member with the old
$\Delta=(6,4,3)$ data.  Fixedness by the inverse braid is equivalent; the stated
convention is what makes (5.3) the displayed formula.  No conclusion is drawn
for an arbitrary noncoprime pair:
other outer block lengths and the missing inner cables require their own
block-product analysis.

At its existing provisional row-geometry scope, `CNA:80-83` says that the sole
nodal $(8,4)$ survivor is target-equivalent to the $(6,4)$ survivor.  It therefore
inherits this kill.  This is a conditional consequence of that target equivalence,
not an assertion that either coordinate pair is pinned by S2; the $(8,6)$ and
$(9,6)$ numerical rows remain untouched.

## 6. Verdict and first missing tool

**Verdict: S2 remains OPEN, but its entire coprime stratum is KILLED and its
affine-normal-form $(6,4)$ cable stratum is KILLED.**  The same conclusion applies
to both P3a and P3b; their extra components have trivial meridians.  The surviving
question is now

```text
OPEN[PI1-S5-NODAL-NONCOPRIME]:
  Does there exist an irreducible polynomial curve D, normalization A1 and one
  place at infinity, with a degree-minimal target parametrization in affine
  normal form (3.1), d>n>=1, g=gcd(d,n)>=2, every affine singularity two
  smooth branches of contact k_z,
  M_infinity+2T >= 3d-2, and a surjection pi1(C2-D)->S5 sending meridians to
  transpositions and each local branch pair to disjoint transpositions?
  Require that no polynomial target automorphism yields either a coprime degree
  pair or the killed affine-normal-form pair (6,4).
```

This is a necessary cage, not a realization statement.  It is strictly narrower
than B0's DQ-1 because §5.1 removes $g=1$, but it is not one numerical row.

The **first missing tool is geometric**, before a quintic-cover classification:

```text
OPEN[N5-S2-ROW-PIN]:
  in degree-minimal target coordinates, derive from the reviewed N=5 Keller
  data either an exact degree/delta-sequence list for D (including all
  approximate-root remainders and the infinity multiplicity sequence), or a
  degree cap that makes that list finite.
```

Without ROW-PIN there is no S2 infinity type on which to run a full cable braid,
no licensed fold relation, and no value of $\rho(\gamma_\infty)$ to feed the
projective-cover route.  Once a row is pinned, the next decision is explicit:

1. compute its iterated-cable braid and block-product action and decide the fixed
   five-letter transposition tuple (the §5.2 calculation is the model);
2. if that calculation proves full INF-TRIVIAL rather than killing the tuple,
   invoke `OPEN[N5-S2-QUINTIC-PLANE]` from §2, not the S4 triple-plane theorem.

The classical sextic resolvent does not change this order: it retains full $S_5$,
turns each simple inertia into $2^3$, and supplies no classified triple plane.
The sign quotient supplies only parity.  Thus no safe replacement presently kills
all noncoprime S2 rows, and the fail-closed status is OPEN.

## 7. S1 handoff (not worked here)

S1 is a different singularity class and is not analyzed in this lane.  Its
reviewed packet is

\[
 (\mu,\operatorname{corr},s)_A=(2,1,1),\ (W_A,a_A)=(2,3),\qquad
 (\mu,\operatorname{corr},s)_B=(1,0,1),\ (W_B,a_B)=(1,4),
\]

with two components and one correction parameter of $K=1$, hence $M=3$ and one
singular branch (`REV:80-91`).  In S1a that point is unibranch and its local
projection is the natural $S_3$ on three letters.  In S1b it also contains a
smooth branch; the local sheet orbits are necessarily $3+2$, with $S_3$ and
$C_2$ projections, not an optional five-letter orbit.  The whole S1b germ has
$\delta\geq1+2=3$ (`REV:93-105`).

At other double points, companion-component incidence must be included, although
the disjoint-transposition conclusion survives.  The degree floor remains
generic-line-custody conditional, and no second affine singularity is forced
(`REV:95,105-107`).  Because S1 has a singular branch, N-A-RES and the S2
nodalization above do not apply.  Its handoff remains exactly
`OPEN[PI1-S5-CUSP]`, split into the corrected S1a and S1b local types
(`REV:154-160`).

## References and exact source record

The three mathematical campaign sources are the frozen files identified and
hashed in §0.  Line citations throughout refer only to those copies.  Chau's
primary PDF custody is inherited from the paired B0/REV review, not newly
downloaded here:

```text
8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f
Nguyen Van Chau, "Non-proper value set and the Jacobian condition,"
arXiv:math/0305088v1 (2003), Theorem 1 and Corollary 2, printed pp. 1-2.
https://arxiv.org/pdf/math/0305088
```

The following literature was streamed with bounded `curl`, read where text was
available, and SHA-256 hashed in this lane; no PDF was saved.

```text
0bfbaaf77c3c795189d5645466dd3d3ee32b872f5c962309751142d65535f875
Rick Miranda, "Triple Covers in Algebraic Geometry," Amer. J. Math. 107
(1985), 1123-1158, Introduction and Theorem 1.1 (printed p. 1124).
https://www.math.colostate.edu/~miranda/preprints/TripleCoversInAG.pdf

9673d33b4e76d305fed02219962ee962ed9481ce134c649c3168f75bade46a26
Manjul Bhargava, "Higher composition laws IV: The parametrization of quintic
rings," Ann. of Math. 167 (2008), 53-94, Introduction/Theorem 1, pp. 53-55,
and the index-six metacyclic subgroups in section 5.1, p. 71.
https://annals.math.princeton.edu/wp-content/uploads/annals-v167-n1-p02.pdf
DOI: 10.4007/annals.2008.167.53

e95d72d159d2f64e7beff2a8e8aef5c100262e87f8ca44ee0b896b838c60e09a
Gianfranco Casnati, "Covers of algebraic varieties II. Covers of degree 5
and construction of surfaces," J. Algebraic Geom. 5 (1996), 461-478.
Image-only scan used for exact bibliographic custody:
https://drive.usercontent.google.com/download?id=1TvjjJBAafLScjtzUmKyLmoMOC5wKN_f7&export=download

628cc47f5c183f491620f5ab65f7a34582d70e12274c8e55f0d6b8d66148ef05
Aaron Landesman, Ravi Vakil, and Melanie Matchett Wood, "Low-degree Hurwitz
stacks in the Grothendieck ring," Compos. Math. 160 (2024), 1784-1849,
section 3 and Theorem 3.16, pp. 1796-1809.  This is the readable primary
source for the all-Gorenstein degree-five Pfaffian parametrization and states
exactly how it generalizes Casnati Theorem 3.8.
https://par.nsf.gov/servlets/purl/10612589
DOI: 10.1112/S0010437X24007206

a4c396b2ad06040efc55a82ccdaec4dc579d7b4dcb464a855178a6b9dc8d30ea
Juan González-Meneses, "Basic results on braid groups," Ann. Math. Blaise
Pascal 18 (2011), 15-59, sections 2-3.
https://ambp.centre-mersenne.org/item/10.5802/ambp.293.pdf
DOI: 10.5802/ambp.293
```

Miranda is used only to delimit the triple-cover theorem's scope.  Bhargava
confirms that the classical resolvent of a quintic is sextic; the permutation
cycle computations in §2 are proved directly here.  Casnati and
Landesman--Vakil--Wood supply cover structure, not a classification of prescribed
plane branch divisors.  González-Meneses was consulted only as auxiliary braid-
group background; the plane-curve Zariski--van Kampen comparisons in §5 are
derived directly in this report, not attributed to that source.  No Chisini
theorem is consumed in a kill step.

<!-- BODY-END -->
