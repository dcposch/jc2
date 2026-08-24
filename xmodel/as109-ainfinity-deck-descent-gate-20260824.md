# AS109 `A_infinity` / DECK-DESCENT GATE

Date: 2026-08-24  
Lane: successor to the AS109 Hensel-to-global-degree cross-gate  
Dependency: the reviewed conditional AS109 Hensel lemma and its degree theorem  
Status: **EXACT REDUCTION + FINITE DISCRIMINATORS / NO AUTOMATIC KILL**

## 0. Verdict

Assume, conditionally, that

```text
F=(P,Q) in Z_109[x,y]^2,
F mod 109=(x-x^109,y),
det J_F=1.
```

Write `p=109`, `K=Q_p`, `M=K(P,Q)`, `L=K(x,y)`, and
`d=[L:M]`.  The predecessor theorem gives, over a suitable formal target
field `E`,

```text
L tensor_M E  ~=  E^p x A_infinity,       dim_E A_infinity=d-p.       (0.1)
```

This gate gives four exact conclusions.

1. The residual rank has a finite valued-algebra description.  For the
   `p`-adic Gauss valuation on the target tube,

   ```text
   d-p = sum of multiplicities of generic roots (u,v)
         with min(v_p(u),v_p(v)) < 0.                                 (0.2)
   ```

   Equivalently, it is the total valued-Groebner/tropical multiplicity at
   the common negative source weights.  Thus a fixed exact support and
   coefficient candidate has a finite `A_infinity=0` test: enumerate the
   negative common weights and solve their initial systems.  This is the
   strongest new special-seed discriminator found here.

2. If the formal fibre algebra is finite over the integral target ring,
   rank constancy forces `A_infinity=0` and `d=p`.  The converse is not
   asserted.  Etaleness and Zariski Main alone do not give this finiteness:
   abstract etale models have special rank `p` and arbitrary residual
   generic rank.

3. The formal permutation `a |-> a+1` of the `p` Hensel factors does not
   automatically descend to a rational deck transformation.  Descent is a
   finite factor/graph calculation in the generic self-fibre algebra.  Even
   one descended off-diagonal factor gives only a deck map; one must also
   verify that its induced permutation contains the displayed `p`-cycle.
   If it does, then `p | d`.  If in addition `A_infinity=0`, then `d=p` and
   `L/M` is Galois.  The classical Galois Keller theorem then makes `F` an
   automorphism, contradicting the `p` distinct Hensel preimages of one
   `K`-point.

4. Trace, idempotent, secant, etale, and Zariski-Main data do neither job by
   themselves.  The exact non-Keller controls

   ```text
   G_N=(x-x^p+p*x^N,y),        N>=p+2,                              (0.3)
   ```

   have the same `p` integral Hensel branches, residual rank `N-p`, and
   trivial rational deck group.  They isolate precisely the global
   constant-Jacobian/infinity information that is still missing.

Accordingly the verdict is not `CONTRADICTION`.  It is a useful split into
two independent finite bridges:

```text
INFINITY BRIDGE:  exclude all common negative weights (or prove integral
                  finiteness of the formal fibre algebra);

DESCENT BRIDGE:   factor the self-fibre algebra and prove that a rational
                  deck map acts as the formal p-cycle.
```

Exact replay:

```bash
python3 cases/as109_ainfinity_20260824/check.py
```

Current result: **48/48 controls pass**.

## 1. The integral formal fibre algebra

Let

```text
R=Z_p[[S,T]],
B=R[X,Y]/(P(X,Y)-p*S, Q(X,Y)-p*T).                         (1.1)
```

The determinant of the relative Jacobian is `1`.  Hence `B` is an etale,
finitely presented, and therefore quasi-finite `R`-algebra.  Its special
fibre is completely explicit:

```text
B/pB
 ~= F_p[[S,T]][X,Y]/(X-X^p,Y)
 ~= product_(a in F_p) F_p[[S,T]].                         (1.2)
```

The factors are reduced because the derivative of `X-X^p` is `1` modulo
`p`.  Formal etaleness/Hensel lifts them to `p` disjoint sections.  The
`p`-adic completion sees these sections; a component living only after
inverting `p` has zero `p`-adic completion.

For a valuation-field formulation, localize `R` at the height-one prime
`(p)` and complete.  Denote the resulting complete DVR by `O`, its fraction
field by `E_0`, and its residue field by

```text
kappa=Frac(F_p[[S,T]]).
```

After passing to a completed algebraic closure `Omega` of `E_0`, the generic
fibre of (1.1) consists of `d` simple geometric points.  Simplicity follows
from `det J_F=1`.  Exactly `p` of them have both source coordinates in the
valuation ring: their reductions are the `p` simple solutions

```text
(X,Y)=(a,0),        a in F_p,                              (1.3)
```

and Hensel gives one and only one lift of each.  Every remaining point has
at least one source coordinate of negative valuation.

This is the integral meaning of (0.1): `A_infinity` records sheets that
escape the chosen integral model in the vertical `p`-adic direction.  It is
important not to identify it automatically with a component of the usual
projective boundary of a complex compactification.  Relating the two is an
additional infinity theorem.

## 2. Exact tropical ledger for `A_infinity`

Let `I` be the zero-dimensional ideal over `Omega`

```text
I=(P(X,Y)-p*S, Q(X,Y)-p*T).                                (2.1)
```

For a geometric root `z=(u,v)`, put

```text
w(z)=(val(u),val(v)).
```

Because every root is simple, its geometric multiplicity is one.  If roots
with the same valuation vector are grouped using their valued initial
ideal multiplicity, the fundamental theorem of tropical algebra gives

```text
d-p = sum_{w in Trop(I), min(w_1,w_2)<0} mult_w(I).         (2.2)
```

No generic-position assumption is hidden in (2.2): `mult_w(I)` means the
exact valued-Groebner multiplicity of the fixed coefficient system, not
merely the stable intersection number of two bare Newton polygons.

Consequences for an exact fixed-support lift are finite.

1. Enumerate weights at which each equation has at least two minimum-weight
   terms.
2. Retain weights with a negative coordinate.
3. Compute the two initial forms, saturating by the relevant torus
   coordinates and handling axes separately.
4. If every retained initial system is empty, then `A_infinity=0` and
   `d=p`.
5. Otherwise the initial-system multiplicities give the exact residual
   rank after the usual valued lifting check.

This can be placed ahead of a coupled coefficient compiler.  It is a
support/valuation filter, not a generic sparse search.  The determinant
identity can be included in the coefficient ideal before the initial-form
test.  A correction support incapable of tying the seed leading terms at
any negative weight cannot carry an `A_infinity` sheet.

The test does not by itself contradict a lift when it returns
`A_infinity=0`: it then proves only `d=p=109`.  Conversely, a surviving
negative initial system is a candidate mechanism, not an existence proof,
until it lifts in the exact valued system.

## 3. What finiteness would prove, and what Zariski Main does not

If `B` in (1.1) is finite over `R`, it is finite etale.  Since `R` is
connected, its rank is constant.  Equation (1.2) fixes that rank as `p`, so

```text
B finite over R  ==>  d=p  ==>  A_infinity=0.              (3.1)
```

This is an exact special-seed sufficient condition.  The reverse implication
is not used: equality of the generic degree with the displayed special rank
need not, without more work, supply finiteness of the original quasi-finite
model over every locus of `Spec R`.

Zariski Main embeds `Spec B` as an open subscheme of a finite `R`-scheme.
It does not say that the open immersion is surjective.  Generic components
of the open subscheme can disappear on the special fibre; their closures in
the finite model meet the omitted boundary over `p=0`.  The following
abstract mechanism control makes the rank freedom exact:

```text
B_r = R^p x (R[1/p])^r,       r>=0.                        (3.2)
```

Each `B_r` is finitely presented and etale over `R`, with

```text
B_r/pB_r ~= (R/p)^p,
rank(B_r tensor_R Frac(R))=p+r.                            (3.3)
```

Thus special splitting, etaleness, quasi-finiteness, and Zariski Main permit
arbitrary `dim A_infinity`.  The control is deliberately not claimed to be
an irreducible Keller polynomial model.  It proves the precise negative
statement that the listed general etale tools alone cannot bound the
residual rank.  A bound under the full polynomial `det J=1` hypotheses would
be new global input.

Global finiteness of a characteristic-zero Keller map is essentially the
properness wall and would settle that map.  Finiteness only over the AS109
formal tube is weaker and is a legitimate special-seed target: it fixes the
generic degree at `109` but does not itself make the global map proper.

## 4. Newton polygon control: residual rank can be arbitrary

For `N>=p+2`, set

```text
g_N(X)=X-X^p+p*X^N
```

and solve `g_N(X)=p*S` over the valuation field above.  The coefficient
valuation points are

```text
(0,1), (1,0), (p,0), (N,1).                               (4.1)
```

The lower Newton polygon has horizontal lengths and root valuations

```text
length 1:      valuation 1,
length p-1:    valuation 0,
length N-p:    valuation -1/(N-p).                         (4.2)
```

Hence exactly `p` roots are integral and exactly `N-p` escape integrality.
For the two-variable control `G_N=(g_N(x),y)`, this reads

```text
A_infinity rank = N-p.                                    (4.3)
```

It realizes every nonnegative residual rank while preserving the AS109
special fibre and all its simple Hensel sections.  Its Jacobian

```text
1-p*x^(p-1)+p*N*x^(N-1)
```

is not the constant polynomial `1`.  Thus (4.3) is a mechanism control, not
a counterexample to the special-seed claim.

## 5. Exact rational deck-descent test

The generic self-fibre algebra is

```text
C_L = L tensor_M L
    ~= L[X,Y]/(P(X,Y)-P(x,y), Q(X,Y)-Q(x,y)).               (5.1)
```

It is finite etale of rank `d` over `L`.  Multiplication gives the diagonal
`L`-factor.  Every additional `L`-factor is the graph of a rational deck
automorphism:

```text
X=R(x,y), Y=S(x,y),       R,S in L,
F(R,S)=F(x,y).                                               (5.2)
```

Conversely, every element of `Aut_M(L)` gives such an `L`-factor.  Therefore
factorization of (5.1), followed by matching the factor's completion to a
chosen Hensel transition, is an exact finite descent test.  One can perform
it with elimination/factorization over `L`, or equivalently search for and
verify the rational graph (5.2).

There is a necessary distinction between the following statements.

* An off-diagonal `L`-factor descends: this supplies one nonidentity deck
  automorphism, with no prescribed order.
* The formal cyclic relabelling descends: the induced permutation on the
  `p` integral factors contains the cycle `a |-> a+1`.

The first does not imply the second.  A map carrying the `a=0` branch to the
`a=1` branch need not continue around the other labelled branches as
translation; that continuation is exactly global monodromy information.

If the second statement holds, the deck group has order divisible by `p`:
the induced action contains a `p`-cycle, so the acting element has order
divisible by `p`, and Cauchy's theorem supplies a subgroup of order `p`.
For a finite separable extension,

```text
|Aut_M(L)| divides [L:M]=d,
```

so `p | d`.  If also `A_infinity=0`, then `d=p`, the automorphism group has
order `d`, and `L/M` is Galois.  The classical Galois case of the Jacobian
conjecture then forces `F` to be an automorphism.  But Hensel already gives
`p` distinct points in `Z_p^2` over the target `(0,0)`, contradicting
injectivity.  This gives a clean two-key conditional obstruction:

```text
A_infinity=0  +  rational descent of the p-cycle  ==>  no exact lift. (5.3)
```

## 6. Why formal permutations, trace, and secants do not descend it

After base change, the `E^p` factor in (0.1) admits all `p!` permutations.
These are automorphisms of a split scalar extension, not automatically
automorphisms of the field extension `L/M`.

The projector

```text
e_int=(1,...,1,0) in E^p x A_infinity
```

has multiplication trace `p`.  Trace does not make it descend.  If it came
from an idempotent of the field `L`, it would have to be `0` or `1`; when
`0<p<d`, it is neither.  More generally, descent requires invariance under
the full descent/monodromy action, and a numerical trace supplies no such
invariance.  When `d=p`, `e_int=1` is trivial and still contains no cyclic
symmetry.

Likewise, the explicit secant diagonal idempotent splits the diagonal from
the off algebra in (5.1).  Over a chosen formal source branch, the other
integral Hensel sections account for `p-1=108` off branches.  They fit inside
the global off rank `d-1`.  Splitting the aggregate off algebra does not
split each formal branch as an `L`-factor.

In group language, let `G` be a transitive geometric monodromy group on the
`d` sheets and `H` a sheet stabilizer.  Components of `L tensor_M L`
correspond to `H`-orbits; rational deck transformations correspond to the
normalizer quotient `N_G(H)/H`.  Labelling `p` sheets after the formal base
change gives no assertion that they are singleton `H`-orbits.  That missing
orbit statement is the deck-descent problem.

## 7. Deck control with no rational symmetry

The same family (0.3) has trivial rational deck group for `N>=p+2`.  It is
enough to prove this for `K(x)/K(g_N(x))`.

Every `K`-automorphism of `K(x)` is Mobius.  Since the polynomial `g_N` has
a unique pole, any automorphism fixing it fixes infinity and hence has the
form

```text
x |-> alpha*x+beta.
```

Comparing `g_N(alpha*x+beta)=g_N(x)` gives:

```text
x^N:       alpha^N=1;
x^(N-1):   p*N*alpha^(N-1)*beta=0, hence beta=0;
x^1:       alpha=1.                                      (7.1)
```

The middle comparison is uncontaminated by the `x^p` term because
`N-1>p`.  Thus the automorphism is the identity.  For
`G_N=(g_N(x),y)`, the variable `y` is already in the base field, so the
two-variable deck group is also trivial.

These controls simultaneously have `p` formal integral branches, all their
formal factor permutations, arbitrary residual rank, and no rational deck
map.  They rigorously stop any argument using only the local Hensel split,
Newton count, trace, or abstract secant idempotents.  They do not stop an
argument that uses the exact constant-Jacobian equations globally.

## 8. Interaction with the campaign ledgers

### 8.1 Sheet number

The predecessor bound remains `d>=109`.  Formula (2.2) upgrades the slack to
an exact nonnegative integer ledger.  If the infinity bridge succeeds, it
sets `d=109`; it does not enter the active `td=6` lane.  Prime sheet number
then invokes only those prime-degree results whose hypotheses have already
been reviewed; it is not permission to consume an unreviewed all-prime
claim.

### 8.2 Fixed-support compiler

For any proposed finite support, the cheapest exact discriminator is now:

```text
(i) impose reduction and det J=1 coefficient equations;
(ii) enumerate negative common tropical weights;
(iii) test the saturated initial systems;
(iv) only if they survive, run full coefficient elimination/Hensel lifting.
```

This can reject a support incapable of carrying the required residual
sheets, or certify `d=109` for that support.  A stronger contradiction still
needs a reviewed degree-109 obstruction or the deck bridge (5.3).

### 8.3 Secant compiler

Factorization of (5.1) is the corresponding exact deck discriminator.  The
diagonal factor should be divided out first.  Search the off algebra for an
`L`-linear graph factor, then compute its action on all `p` completed Hensel
branches.  Merely finding an off idempotent or matching one ordered pair is
insufficient.

## 9. Scope firewall and resurrection conditions

This report does **not** prove any of the following:

* `A_infinity=0` from `det J=1` alone;
* a general bound or congruence on `d-p`;
* descent of a formal branch permutation;
* that `A_infinity` is literally a complex projective-boundary component;
* nonexistence of an AS109 exact lift.

The lane should be resurrected immediately upon any one of these finite
inputs:

1. a named fixed support for an exact AS109 candidate, allowing the negative
   initial systems in (2.2) to be computed;
2. a theorem forcing (1.1) finite from the AS109 reduction plus the exact
   determinant equations;
3. a factorization of the off self-fibre algebra exhibiting a rational
   transition whose completed action is the `109`-cycle;
4. a reviewed obstruction to a nonautomorphic Keller map of generic degree
   exactly `109` strong enough to consume `A_infinity=0` alone.

Until then, the exact output is a finite two-gate architecture, not a
contradiction: negative-weight elimination controls the extra sheets, and
self-fibre factor descent controls the formal cyclic symmetry.
