# Sigray Section 9 source audit: table (23), transition package, and the `td < 6` claim

Date: 2026-08-28  
Producer: `sol-ultra`, independent source/desk audit  
Scope: Sigray thesis, printed pp. 45--60, especially Proposition 9.1,
Notations 9.1--9.3, Statements 9.1--9.12, Propositions 9.2--9.3, and
Theorem 9.1.  Earlier Sections 3--8 are used only with the repairs already
promoted in the current audit campaign.  In particular, the root clause of
Proposition 8.4 is **not** assumed.  No web, no AWS, no canonical-file edit,
and no access to or edit of `jc2-lean` was used.

## 0. Executive verdict

There are four different verdicts which must not be conflated.

1. **Table (23) is arithmetically complete.**  Its eleven numerical rows are
   exactly the solutions of the Section 5 scaling, congruence, and
   `Lambda <= 6` constraints.  The first printed row labelled `6` is row
   **5**.  This is a row-label error, not a missing or duplicate numerical
   row.

2. **The printed Section 9 transition proof is not valid as written.**  In
   addition to many typing and copy errors, it contains:

   - the wrong sign in Statement 9.3 (24);
   - the wrong denominators in Proposition 9.3(III), items (g),(h);
   - a phantom Diophantine solution in Statement 9.6;
   - a factor-exponent error in the displayed `q` patterns of Statements
     9.6 and 9.11;
   - the already-catalogued omitted zero-charge families E2, E3, E4 in
     Statements 9.8--9.10;
   - a literal `Y(F)` definition which makes the sets nested along a
     characteristic chain, while Statement 9.4 counts them as disjoint;
   - a false Statement 9.12 dichotomy and a row-number error.

3. **The row-4 (`td=4`) exclusion is repairable without root Proposition
   8.4.**  Every `M=1` outcome actually needed in the repaired row-4 graph is
   at a nonroot vertex.  Root terminations are handled instead by
   Proposition 9.3(m), or by the stronger `psi`-budget (25) using the axis
   ratio.  The E2--E4 zero-charge families are self-families; finiteness of
   the characteristic sequence forces an eventual charged, `M=1`, or root
   exit.  This is the repaired campaign closure, not the printed proof.

4. **Theorem 9.1 (`counterexample => td >= 6`) also becomes repairable, but
   only after adding an argument absent from the thesis.**  For `td <= 5`,
   Proposition 5.8 and `Lambda >= 3` give one pole, with table row in
   `{1,4,5,7,10}`.  The pole identity

       M_F = gcd(deg p_F, deg p_{g,F})

   kills rows `1,5,7,10` at their nonroot pole entry; repaired Statement
   9.12 kills row 4.  The thesis itself states neither this row-selection
   completion nor the entry kills.  Section 9 does **not** exclude
   `td=6`: at degree six it leaves the single-pole rows 8 and 9 after entry
   pinning, and it says nothing sufficient about the two-pole `3+3` case.

Thus the exact disposition is:

- **printed theorem proof:** incomplete;
- **corrected Section 3--9 reconstruction:** `td < 6` survives;
- **degree `td=6` exclusion:** not claimed by Theorem 9.1 and not proved by
  Section 9;
- **dependence on root Proposition 8.4:** none in the corrected `td < 6`
  proof.

## 1. Source custody and method

Primary source:

| file | SHA-256 |
|---|---|
| `refs/sigray_full.pdf` | `9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae` |

Canonical consumers inspected only after the independent primary
reconstruction:

| file | SHA-256 at audit time |
|---|---|
| `ladder/SHEET6-CAMPAIGN.md` | `086a475927b5cdec68dcdffc836bf06c0418616113aa3ccc91bc98d9eafb1678` |
| `ladder/SHEET6-REVIEW.md` | `89d6303c28908274521b5247891cc643be066eeac2ec05bd13618c378b5ed97c` |
| `ladder/SHEET6-AF2.md` | `905988471cf1458b5be949b7dfa2636f8e6b29a114cb7c2f1e30df11deb18d34` |
| `ladder/SHEET6-AF3.md` | `555363fde61291a0c689bbf9d789c01f73734e0c403d350d85ae2fd0ddab8099` |
| `ladder/SHEET6-H3.md` | `a0d71267314471e976dff11f6243f6a4e83b92579bdc9e246eafc891a5718384` |
| `ladder/SHEET6-HIII-REVIEW.md` | `aaaf1dbaba44128200814dfb576f64a9f073e08c01ccfa11230a0b79f97fe86e` |
| `ladder/SHEET6-A3L1-REVIEW.md` | `6c045f36686e5dd73c6f067597d8a01857094a1add06288b955ef0e06b6aa44b` |
| prior Sections 8 audit, `xmodel/sigray-later-m-package-source-audit-sol-ultra-20260828.md` | `5fc6b1634dc1ef0a0abe578411644fa166ffbfa16b8608cbce2a7b7b61465cd5` |

The PDF was read page-on-page and with local `pdftotext -layout`.  Exact
integer and `Fraction` checks were run locally for the small Diophantine
systems.  The calculations below give algebraic completeness proofs, so no
bounded search is a proof dependency.

## 2. Orientation and notation used in this report

For one characteristic edge write

    G = F + c,             F = G^o,

where `G` is the upper vertex (farther from `(0,y)`) and `F` the lower,
rootward vertex.  Put

    Q(G) = (D, P, N, M, K),
    P = deg p_G,
    N = nu_G,
    K = kappa_G(1-pi(G)).

At the reduced Proposition 8.1 level let

    mu = mult(p,c),
    i  = P/mu.

The last equality follows because `p_F = p^i` and Statement 3.17 gives
`P = mult(p_F,c) = i mult(p,c)`.  Proposition 9.3 uses `i` without
redeclaring it; this is its intended meaning.

For cases I and II, the correct edge arithmetic is

    deg(p)/deg(q) = (D+nP)/(i(K+n)),
    D_F            = (D+nP)/N,
    K_F            = (K+n)/N.                         (2.1)

For case III, with `nu = nu_F`, the correct arithmetic is

    deg(p)/deg(q) = (nu D+nP)/(i(nu K+n)),
    D_F            = (nu D+nP)/N,
    K_F            = (nu K+n)/N.                      (2.2)

The source prints `nu_F` rather than `nu_G=N` in the denominators of the
last two expressions in (2.2).  Equation (2.2) follows from the repaired
Section 3 jump law

    kappa_F = nu_F kappa_G/nu_G.

The ratio in (2.2) is unchanged because the common `nu_G` cancels.  This
explains why several source ratio calculations look plausible even though
their child `D,K` data are not correctly typed.

## 3. Proposition 9.1 and table (23)

### 3.1 Complete re-enumeration

For type `(alpha,beta)`, Section 5 gives positive integers `a,b` with

    (D_F,D_g,F)                    = a(alpha,beta),
    (deg p_F,deg p_g,F)            = b(alpha,beta),
    Lambda(F) = ab alpha beta/nu.                       (3.1)

The orbit congruence is exactly one of

    nu | alpha and nu | (b beta-1),
    nu | beta  and nu | (b alpha-1).                    (3.2)

Also `1<alpha<beta`, `gcd(alpha,beta)=1`, and Proposition 5.7 gives
`beta <= Lambda`.  Hence `Lambda <= 6` makes the enumeration finite
without any guessed search cutoff.  Equations (3.1)--(3.2) give exactly:

| row | `(alpha,beta)` | `a` | `b` | `nu` | `(D,Dg)` | `(P,Pg)` | `Lambda` | pole `M` |
|---:|---|---:|---:|---:|---|---|---:|---:|
| 1 | `(2,3)` | 1 | 1 | 2 | `(2,3)` | `(2,3)` | 3 | 1 |
| 2 | `(2,3)` | 1 | 1 | 1 | `(2,3)` | `(2,3)` | 6 | 1 |
| 3 | `(2,3)` | 2 | 1 | 2 | `(4,6)` | `(2,3)` | 6 | 1 |
| 4 | `(2,3)` | 1 | 2 | 3 | `(2,3)` | `(4,6)` | 4 | 2 |
| 5 | `(3,4)` | 1 | 1 | 3 | `(3,4)` | `(3,4)` | 4 | 1 |
| 6 | `(3,4)` | 1 | 1 | 2 | `(3,4)` | `(3,4)` | 6 | 1 |
| 7 | `(2,5)` | 1 | 1 | 2 | `(2,5)` | `(2,5)` | 5 | 1 |
| 8 | `(2,5)` | 1 | 3 | 5 | `(2,5)` | `(6,15)` | 6 | 3 |
| 9 | `(3,5)` | 1 | 2 | 5 | `(3,5)` | `(6,10)` | 6 | 2 |
| 10 | `(4,5)` | 1 | 1 | 4 | `(4,5)` | `(4,5)` | 5 | 1 |
| 11 | `(5,6)` | 1 | 1 | 5 | `(5,6)` | `(5,6)` | 6 | 1 |

The PDF labels rows 5 and 6 both `6`.  The first is row 5.

### 3.2 The pole `M` pin

At a pole vertex, Proposition 5.1 gives `m_F=0`; Proposition 4.2 then says
the `h` family is just `h_0=g`.  Notation 8.1 therefore gives

    M_F = gcd(deg p_F,deg p_g,F).                       (3.3)

The last column above is (3.3), not an assumed menu.  Proposition 5.3(i)
explicitly says a pole vertex is neither `(0,x)` nor `(0,y)`.  It is also
in the down tree: with `m_F=0`, take `h=g` in Proposition 6.4, and
Proposition 5.3(vii) gives equality in its degree/order criterion.
Consequently the corrected nonroot Proposition 8.4 licenses every
single-pole entry kill in the table.

**Verdict on Proposition 9.1:** numerical statement verified; row label
erratum; its later use needs the unstated pole pin (3.3).

## 4. Notations 9.1--9.3 and Statements 9.1--9.5

### 4.1 Notation 9.1

The PDF says `F in V_a union T_a^+` and defines

    Q(F)=(D_F,deg p_F,nu_F,M_F,kappa_F(1-pi(F))).

This is ill-typed on the extra nonvertex points of `T_a^+`: `D_F`,
`nu_F`, and `kappa_F` were defined on `V_a`.  The clean domain is simply
`F in V_a` (and, in each consumer, the indicated intersection with the
down tree, pole set, or root).  Restricting to `V_a cap T_a^+` would be too
narrow because it would exclude pole vertices.

### 4.2 Statement 9.1

For a pole vertex,

    K_F := kappa_F(1-pi(F)) = D_F+D_g,F.

This follows immediately by multiplying Proposition 4.1's
`d_F+d_g,F=1-pi(F)` by `kappa_F`.  There is only an extra closing
parenthesis in the printed statement.

**Verdict:** verified with typographical repair.

### 4.3 Notation 9.2 and hidden regularity

The source sets an upper nonroot down vertex `A`, its lower neighbor
`B=A^o`, and says that **`B` is regular over `A`** when `A` is the only
nonroot down child whose lower neighbor is `B`.  Statements 9.7--9.10 say
`F:=G^o is regular over F`; this must read **regular over `G`**.

For a characteristic sequence of a singleton pole, regularity is not an
extra assumption, but the proof is hidden.  If a lower chain vertex had a
second nonroot down child `H`, then `H in V_a` has more than one root and
therefore `deg p_H>1`; Propositions 6.7--6.8 produce a pole on that sibling
branch.  It is distinct from the pole on the characteristic branch,
contradicting singleton-pole uniqueness.  This is the exact
unique-pole-sibling exclusion consumed in Statements 9.6--9.12.

### 4.4 Statement 9.2

At `F=(0,y)` the intended data are

    D_F=d_F,       nu_F=1,       kappa_F(1-pi(F))=1.

These follow from the root normalization (`kappa=1`, `pi=0`) and the
root's non-Puiseux-characteristic convention.

There is a necessary Definition 3.4 clarification.  Although `alpha_0=0`
was introduced for predecessor formulas, `V_1` must use only actual
characteristic exponents `alpha_j`, `1<=j<=m`.  Otherwise Notation 3.4 at
the root asks for the undefined quotient `e_{-1}/e_0`, the separately
adjoined roots in `V_a` are pointless, and Proposition 9.3(IV) is
incoherent.  This does **not** exclude the root from `V_2`: two y-side
series with different constant coefficients have contact zero, so
`(0,y)` can be a case-I (`V_2`) terminal.  This SF1 distinction is used in
Sections 8 and 9 below.

**Verdict:** verified with the explicit `1<=j` convention.

### 4.5 Statement 9.3: the sign error E6

Let lower `F=I_P(u)` be down, let the exit child
`G=F+c*=I_P(v)` be up, and let `H=I_P(w)` be the cv vertex on that exit
ray.  Write `K_F=kappa_F(1-u)`.  The correct inequality is

    kappa_H(pi(H)-1) >=
      D_F/mult(p_F,c*) - K_F,                    c* != 0,

    kappa_H(pi(H)-1) >=
      (D_F/mult(p_F,c*) - K_F)/nu_F,             c* = 0.       (4.1)

Indeed `w-u >= d_F/mult(p_F,c*)`, and for `c*!=0`,

    kappa_H(w-1)
      >= kappa_F(w-1)
       = kappa_F(w-u)+kappa_F(u-1)
      >= D_F/mult(p_F,c*)-K_F.

The PDF inserts a minus before `kappa_F(u-1)`.  Since
`kappa_F(u-1)=-K_F`, its printed right side is `D/mult+K_F`, the opposite
sign from both the algebra and every numerical use on pp. 52--59.  For
`c*=0`, use `kappa_H>=kappa_F/nu_F` to obtain the second line of (4.1).

**Verdict:** false as printed; exactly repaired by (4.1).

### 4.6 Notation 9.3 and Statement 9.4: the `Y(F)` overlap E9

Literally, the PDF defines `Y(F)` to contain every cv vertex `H` for which
some Puiseux ray `P` contains both `F=I_P(u)` and
`H=I_P(pi(H))`.  If `F'` is rootward of `F` on that ray, then

    H in Y(F)  implies  H in Y(F').

Thus the `Y(F_i)` are nested, not disjoint, along the characteristic
sequence.  Corollary 7.1 counts a cv vertex once, whereas the proof of
Statement 9.4 replaces a union of cv vertices by
`sum_i lambda_(F_i)`.  That inference is invalid.  The index mismatch in
Statement 9.5 (statement sums `i=1..n`, proof applies 9.4 to
`F_0,...,F_n`) is a symptom of the same issue.

The source's later claims `lambda_F=0` when no branch exits at `F` reveal
the intended meaning: **local exit mass**, not all descendant cv mass.
Here is an explicit replacement theorem, rather than a renamed
assumption.

Let `C=(F_0,...,F_n)` be the characteristic path of a singleton pole in
the y-component.  For a y-side cv vertex `H`, the vertices of `C` which
lie on the ray from `(0,y)` to `H` form a terminal interval

    {F_i,F_(i+1),...,F_n}.

This is the elementary no-remerging property of a tree.  For `1<=i<=n`,
define `E_i` to be the set of cv vertices for which the displayed interval
starts at `F_i`; equivalently, their branch first separates from the
characteristic path at the lower vertex `F_i`.  (A possible set with first
index zero is irrelevant to the transitions and is simply not selected.)
Then

    E_i = Y_lit(F_i) \ Y_lit(F_(i-1)),
    lambda_i^exit := sum_(H in E_i) kappa_H(pi(H)-1).          (4.2)

The uniqueness of the first separation index proves that the `E_i` are
pairwise disjoint.  It also proves the local-pricing property.  At the
edge `F_(i-1)=F_i+c`, an alternative direction `c*!=c` shares `F_i` with
the characteristic ray but not `F_(i-1)`.  Singleton-pole regularity makes
that alternative child up, and Statement 7.3 supplies a cv vertex farther
out on the same ray.  That vertex lies in `E_i`.  Different child
vertex-directions (cyclically conjugate roots in one `eta^nu-c^nu` orbit
count as one direction at this level) lie in disjoint subtrees and
therefore give distinct cv vertices.  Consequently every alternative direction priced by corrected
Statement 9.3 contributes, additively, to exactly the one local charge
`lambda_i^exit`.  Conversely, the child/root correspondence of Statements
3.16--3.18 shows that when the reduced pattern has no alternative
vertex-direction/orbit, `E_i` is empty and the source's asserted zero
charge is justified.

Finally choose the x-side cv vertex in the proof of 9.4.  It is distinct
from every `E_i` because the x- and y-trees are different components
(Statement 3.3).  If `psi l_f<k_f`, the proof of 9.4 gives it integral
weight at least `psi`.  Apply Corollary 7.1 once to the honest set

    {x-side vertex} union (disjoint union of E_i).

This gives the repaired cumulative budget

    sum_(i=1)^n lambda_i^exit <= td(f,g)-1-psi,                 (4.3)

and, with `psi=1`,

    sum_(i=1)^n lambda_i^exit <= td(f,g)-2.                     (4.4)

For arbitrary vertices, the printed Statement 9.4 is valid only after
adding pairwise-disjoint exit sets (or an antichain condition strong enough
to imply it).  Formula (4.3) is the minimal theorem actually needed.  The
argument above proves it for the singleton-pole characteristic sequence;
it discharges the campaign's H2 at this trust perimeter and makes no claim
about the literal `lambda_F` of Notation 9.3.

**Verdict:** Notation 9.3/Statement 9.4/Statement 9.5 form a genuine
definition--usage gap as printed; (4.2)--(4.4) are the minimal repair.

### 4.7 Proposition 9.2

Starting from a pole, repeatedly applying `o` strictly lowers `pi` through
the finite vertex set and ends at `(0,y)`.  This gives a finite,
pairwise-distinct characteristic sequence.  Its down-tree typing follows
from the corrected Section 6 descent argument; singleton-pole regularity
is the lemma in Section 4.3 above.

**Verdict:** verified with the implicit finiteness/down-tree typing made
explicit.

## 5. Proposition 9.3: exact case arithmetic

### 5.1 Cases I--III

The four cases are intended to be exhaustive according to whether the
lower endpoint is a nonroot `V_2` point, a `V_1` point at the predecessor
characteristic height, a `V_1` point above that height, or the root outside
`V_1 union V_2`.  The root can also be in `V_2`, hence case I; it cannot be
in `V_1` under the corrected `j>=1` convention.

For I--II, items (a)--(d) are (2.1) and are correct.  For III, items (e)
and (f) are correct, but (g),(h) must be (2.2); the PDF's denominator
`nu_F` is wrong.  The printed proof derives only (a)--(d) and says every
remaining assertion is similar.  That is not a proof of the case split or
of the root assertions.

The reduced patterns used later are:

    I:    deg p=k+mu,          deg q=k+1;

    IIa:  deg p=(k+mu)nu,      deg q=(k+l+1)nu+1;

    IIb:  deg p=(k+mu)nu+1,    deg q=(k+1)nu+1;

    III:  deg p=mu+k nu,       deg q=1+k nu.                   (5.1)

For IIa, `k>0` forces `l=0` by Statement 8.2.  The corrected reduced ODE
root law makes the distinguished factor occur to exponent `mu-1` in `q`.
In particular, when `mu=2` it is simple in `q`, not squared.

### 5.2 Case IV

Write `K=(1-v)kappa_G`.  The source's unbound `nu` in (k) must be
`nu_G=N`.  The intended formulas are

    N=kappa_G,
    K<N,
    d_(0,y) = [D+(N-K)P]/N in N,
    d_(0,y)<P,
    d_(0,y) M/P in N.                                      (5.2)

The last condition is a hidden use of the Section 8 Bezout package.  The
Bezout coefficients may be negative, but here they are used only in an
integer linear combination of degree/order pairs; no rational product is
asserted to be polynomial.  Transporting that combination to the root
gives the divisibility in (5.2).  With `M=1` it becomes the axis
contradiction used in Proposition 8.4; with `M>=2` it is only an
integrality condition and is not itself contradictory.

The axis inequalities give a stronger terminal budget.  Set

    R := P/d_(0,y),
    psi := ceil(R)-1.

Statement 3.17 and the root chart relations give

    k_f >= P,       l_f=d_(0,y),

so `psi l_f<k_f`.  Therefore (4.3) applies with this `psi`.  This is the
correct axis use; the inequalities point in the same direction and do not
form a direct contradiction.

**Verdict on Proposition 9.3:** (a)--(f) verified after typing `i`; (g),(h)
false as printed and repaired by (2.2); (i)--(m) have only a placeholder
proof, but (5.2) follows from the corrected Section 3--8 package.  Any
consumer must separately allow the SF1 root-in-`V_2` case I.

## 6. Statements 9.6--9.11: statement ledger and exact arithmetic

In every item below, `lambda` means the local exit charge (4.2).  The
regularity hypothesis plus Statement 6.2 says that every alternative root
has smaller multiplicity than the arrival root: otherwise its child would
also be down, violating regularity.  Statement 8.4 gives
`mu | M_G`.  These two hidden steps are used in all six proofs.

The PDF also leaves several family parameters unbound.  The intended
domains forced by the equations are: the Statement 9.6/9.11 odd family
parameters are in `N*`; the Statement 9.7--9.10 parameters are in `N`
(with the separate `s>=1` restriction on the 9.9/9.10 root alternatives);
and every newly introduced self-family parameter below is in `N` unless
explicitly stated otherwise.

### 6.1 Statement 9.6

Hypothesis:

    Q(G)=(j,2j,3,2,5),        F=G^o regular over G.

Case IV is impossible because `K_G=5` is not `<nu_G=3`.  For `mu=2`,
IIa with `k>0,l=0` gives

    (k+2)nu/((k+1)nu+1) = (1+2n)/(5+n),
    n == 1 (mod 3).

After cross multiplication,

    nu(4k+9-kn)=1+2n.                                      (6.1)

Positivity bounds `n<4+9/k`, so (6.1) is finite.  Its only solutions with
`k>=1,nu>1` are

    (k,n,nu)=(1,10,7), (2,7,5).

The PDF also lists `(1,13,25)`.  At `k=1,n=13`, the left coefficient in
(6.1) is zero and the right side is 27.  The raw ratio has a
`nu=25,n=12` solution, but `12` violates `n==1 mod 3`.  Thus the printed
case B and its `(75,51)` child are phantom.  It is absorbed by the broad
`lambda>=3` disjunct, so it does not make the final disjunction too small.

For `k=0`, the exact solutions are

    l=0, n=9s+4, nu=2s+1,        s>=1,

giving the printed zero-charge family.  The displayed IIa/IIb `q`
patterns wrongly square the distinguished factor; the degrees and the
ODE require exponent one.

Correct statement alternatives:

- `M_F=1`;
- `lambda_F>=3` (possibly redundant after deleting the phantom case);
- `Q(F)=(7j,21j,7,3,5)`, `lambda_F>=2`;
- `Q(F)=(5j,20j,5,4,4)`, `lambda_F>=2`;
- `Q(F)=((6s+3)j,(4s+2)j,2s+1,2,3s+3)`, `lambda_F=0`, `s>=1`.

**Verdict:** statement survives with proof-level E1/E7 repairs.

### 6.2 Statement 9.7

Hypothesis:

    Q(G)=(j,3j,7,3,5).

Repairs:

- `F=G^o` is regular over **G**, not over F;
- alternative (i) is `M_F=1`, not the hypothesis-contradicting `M_G=1`;
- in case IV, (5.2) gives `d_F=j`, not the proof's `7j`;
- the stated root datum `Q(F)=(j,3j,1,M,1)` is the consistent one.

For the zero-charge IIa branch,

    3nu/((l+1)nu+1)=(1+3n)/(5+n),
    n=7m+2.

This reduces to

    nu[2-(3m+1)l]=3m+1.

Thus `l=0`, `m=2s+1`, `nu=3s+2`; no `l>0,nu>1` solution exists.  The
child is exactly

    Q(F)=((6s+4)j,(9s+6)j,3s+2,3,2s+2).

**Verdict:** exhaustive after the listed typing/arithmetic repairs.

### 6.3 Statement 9.8 and E2

Hypothesis:

    Q(G)=(j,4j,5,4,4).

Again, regularity is over G, (i) must be `M_F=1`, and (iv) must say
`Q(F)`, not `Q(G)`.  Case IV gives `Q(root)=(j,4j,1,M,1)`.

For `mu=2`, `i=2j`.  A zero-charge IIa branch has `k=0` and satisfies

    2nu/((l+1)nu+1)=(1+4n)/(8+2n),
    n=5m+1.

After substituting `n=5m+1`, cross multiplication gives

    nu[3-(4m+1)l]=4m+1.

There is no solution with `l>0,nu>1`.  For `l=0`, this is

    15nu=4n+1,

so

    nu=4s+3, n=15s+11,
    M_F=gcd(2nu,nu+1)=2.                               (E2)

This is not `M_F=1`.  It gives the omitted possibility

    Q(F)=((12s+9)j,(16s+12)j,4s+3,2,3s+3),
    lambda_F=0.                                          (6.2)

For `mu=4`, the source accidentally repeats the `mu=2` equation.  The
correct equation is

    4nu/((l+1)nu+1)=(1+4n)/(4+n).

It has the same `nu,n` family and gives the printed numerical child with
`M_F=4`.  The source sentence saying `l=0 => M_F=1` directly contradicts
its later computation `M_F=4`.

**Verdict:** incomplete as printed; add both the `M=2` E2 family (6.2)
and the corrected `M=4` family.

### 6.4 Statement 9.9 and E3

Put `r=4s+3`.  The input is

    Q(G)=(3rj,4rj,r,4,3(r+1)/4).

The case-IV root alternative is possible only for `s>=1`; at `s=0`,
`K=N=3`, violating (j).  In the zero-charge IIa calculation,

    n=s+m r.

For `mu=2` and `mu=4` the two source equations reduce respectively to

    2nu/((l+1)nu+1)=(4m+1)/(2m+2),
    4nu/((l+1)nu+1)=(4m+1)/(m+1).

Both imply

    nu[3-(4m+1)l]=4m+1.

Therefore `l=0`, `m=3t+2`, `nu=4t+3`, giving zero-charge children of the
same numerical family, with `M_F=2` and `M_F=4`, respectively.  The two
printed “no solution” claims are false.

**Verdict:** incomplete as printed; add both E3 self-families, correct
`M_G` to `M_F` in (i), and restrict the case-IV alternative to `s>=1`.

### 6.5 Statement 9.10 and E4

Put `r=3s+2`.  The input is

    Q(G)=(2rj,3rj,r,3,2(r+1)/3).

The root alternative is possible only for `s>=1`.  The zero-charge
`mu=3` equation reduces to

    3nu/((l+1)nu+1)=(3m+1)/(m+1),

hence

    nu[2-(3m+1)l]=3m+1.

Thus `l=0`, `m=2t+1`, `nu=3t+2`, and `M_F=3`.  It is a zero-charge
self-family after rescaling `j'=rj`.  The printed “no solution” assertion
is false.

Printed alternative (iv), the `M=4` Statement 9.8 family, is produced
nowhere in the proof and is a copy-paste intrusion.  It should be deleted
and replaced by the E4 `M=3` self-family.  Also repair regularity over G,
`M_G` to `M_F`, and the root's `s>=1` condition.

**Verdict:** incomplete as printed; corrected list as above.

### 6.6 Statement 9.11

The input is

    Q(G)=((6s+3)j,(4s+2)j,2s+1,2,3s+3).

Case IV is impossible because `K_G>nu_G`.  The `k>0` IIa equation has
exactly

    (k,m,nu)=(2,2,5), (1,3,7),

giving the printed `M=4` and `M=3` charged children.  The `k=0` solutions
are

    l=0, m=3phi+1, nu=2phi+1,       phi>=1,

and give the printed zero-charge self-family.  As in Statement 9.6, the
displayed `q` patterns must have distinguished-factor exponent one, not
two.

**Verdict:** statement verified with the E7 pattern repair.

## 7. Every `M=1` kill: root versus nonroot

The corrected Proposition 8.4 available to this audit is:

> If the pole set is a singleton and `F` is a **nonroot** down vertex,
> then `M_F != 1`.

It is not licensed at `(0,y)`.  Section 9 uses `M=1` in two places.

### 7.1 Entry kills

Rows 1, 5, 7, and 10 have pinned pole `M=1`.  Pole vertices are nonroot,
so these kills are licensed.

### 7.2 Transition kills in the row-4 graph

The root cannot be in `V_1`, but it may be in `V_2` and hence may terminate
through Proposition 9.3(I), the SF1 case.  It is therefore not enough to
declare every I--III outcome nonroot.

For the row-4 graph, however, direct arithmetic eliminates every SF1
possibility:

- Statement 9.6 and Statement 9.11 inputs have `K_G>=nu_G`, so root
  `K_F=1` would require `n=nu_G-K_G<=0`.
- At the Statement 9.7 input, root forces `n=2`.  For `mu=3` the right
  side of the case-I ratio is `1`, whereas `(k+3)/(k+1)>1`; for `mu=1`
  the right side is `1/3`, whereas the reduced pattern has ratio `1`.
- At Statements 9.8--9.9 inputs, a root case-I ratio is `mu/4`.  If
  `mu<4` this is `<1` while `(k+mu)/(k+1)>=1`; if `mu=4`, the right side
  is `1` while the left side is `>1`.
- At the Statement 9.10 input, the corresponding ratio is `mu/3`; the
  identical `<1`/`=1` comparison excludes `mu=1,3`.

Thus every `M_F=1` alternative used in the repaired row-4 proof occurs at
a nonroot lower child.  The root clause of Proposition 8.4 is never used.

Outside this graph, SF1 is real and must remain separately modelled.  Any
canonical consumer which kills an arbitrary root case-I child merely from
`M_root=1` must be rolled back.

## 8. Corrected Statement 9.12: complete row-4 proof

### 8.1 Correct statement

The PDF says a singleton pole “cannot have type (3)” and immediately says
`td=4`.  Row 3 has `Lambda=6`.  The input of Statement 9.6 at `j=2` is
exactly row 4:

    Q(F_0)=(2,4,3,2,5).

The corrected statement is therefore:

> If a normalized counterexample has a singleton pole, that pole cannot
> have **row 4** of table (23).

### 8.2 State graph

The row-4 budget is `td-2=2`.  From Statement 9.6:

- `M=1` dies nonroot;
- `lambda>=3` exceeds the budget;
- `(1/3,nu=7,M=3,K=5)` arrives with charge at least 2 and enters 9.7;
- `(1/4,nu=5,M=4,K=4)` arrives with charge at least 2 and enters 9.8;
- the `(3/2,nu odd,M=2)` family has zero charge and enters 9.11.

At the 9.7/9.10 (`R=3`) side:

- every non-self exit is `M=1` or has a further positive charge;
- a case-IV root has `R=3`, hence `psi=2`; (4.3) allows at most
  `td-1-psi=1`, but the accumulated charge is at least 2;
- E4 is a zero-charge `M=3` self-family.

At the 9.8/9.9 (`R=4`) side:

- every non-self exit is `M=1` or has a further positive charge;
- a case-IV root with `M=4` has `R=4`, hence `psi=3`; (4.3) allows zero,
  but the accumulated charge is at least 2;
- E2 and E3 supply zero-charge self-families with `M=2` or `M=4`.

The 9.11 family either pays at least 2 and enters one of those two sides,
dies with `M=1`, or repeats as a zero-charge self-family.

### 8.3 Exact closure of the omitted E2 `M=2` family

This is the only new continuation which must be written explicitly to
avoid hiding behind the pre-existing campaign engine.  Put `r=4s+3` and

    Q(G)=(3rj,4rj,r,2,3(r+1)/4).

Case IV is impossible: (5.2) gives `d_root=rj`, so

    d_root M_G/P_G = (rj*2)/(4rj)=1/2,

violating (m).  A root case I is also impossible because its ratio would
be `mu/4<=1/2`, while its reduced pattern has ratio greater than one.

For a nonroot child, `mu | 2`.  Arrival `mu=1`, case I, case IIb, and case
III give `M_F=1`; IIa with `k>0` creates an exit and hence
`lambda_F>=1`.  Only IIa with `k=0` can remain.  Write

    n=s+m r.

Its exact equation is

    2nu/((l+1)nu+1)=(4m+1)/(2m+2),

or

    nu[3-(4m+1)l]=4m+1.

It forces

    l=0, m=3t+2, nu=4t+3.

The child is

    Q(F)=(3r nu j,4r nu j,nu,2,3(nu+1)/4),

which is the identical family with new scale `j'=rj` and parameter `t`;
its exit charge is zero.

### 8.4 Why zero-charge recurrence is not a survivor

Proposition 9.2 says the characteristic sequence is finite and ends at the
root.  Along any branch which has not already contradicted the `M=1` or
budget conditions, Sections 8.2--8.3 show that the only next move is
another member of the same zero-charge family.  It cannot repeat forever,
and its root exit is either arithmetically impossible (`M=2`) or killed by
the `psi` budget (`M=3,4`).  Hence an eventual contradiction is forced.

This is the missing completeness argument behind the campaign phrase
“zero-charge loops must exit.”  It is not present in the thesis.

### 8.5 Verdict on Statement 9.12

- **As printed:** false proof and wrong row label.  Its claimed dichotomy
  fails because (26) permits the printed case-IV terminals, and E2--E4
  were omitted.
- **After repairs:** row 4 is excluded.  The proof needs the local
  exit-charge budget, the stronger terminal `psi`, the corrected
  transition lists, finiteness, and only the nonroot part of Proposition
  8.4.

## 9. Theorem 9.1 and the exact `td <= 5` / `td=6` boundary

### 9.1 `td <= 5`

Proposition 5.8 gives

    td(f,g)=sum_(pole F) Lambda(F),

and Proposition 5.7 gives `Lambda(F)>=beta>=3`.  Therefore `td<=5` permits
only one pole.  Table (23) reduces the entry to rows

    {1,4,5,7,10}.

The pole pin (3.3) gives `M=1` on rows 1, 5, 7, and 10.  These are safe
nonroot Proposition 8.4 kills.  Corrected Statement 9.12 kills row 4.
Thus no counterexample has `td<=5`, equivalently every counterexample has
`td>=6`.

This proof is complete only after the repairs in this report.  The PDF's
one-line proof “by Propositions 9.1 and Statement 9.12” omits four of the
five rows and is not valid on its own.

### 9.2 `td=6`

At degree six the pole partitions are:

- one pole with one of rows `2,3,6,8,9,11`;
- two row-1 poles, `3+3`.

The pin kills single-pole rows 2, 3, 6, and 11, leaving row 8 with `M=3`
and row 9 with `M=2`.  Proposition 8.4 does not apply to the two-pole
configuration.  Statement 9.12 concerns row 4 and contributes nothing.

Accordingly, Section 9 proves no `td=6` exclusion.  The introduction's
phrase about extending results “to topological degree 6” must mean raising
the lower-bound threshold to `td>=6`, not ruling out degree six.  Any
stronger degree-six ledger belongs to the later campaign, not to the
thesis proof audited here.

## 10. Compact statement ledger

| item | printed verdict | repaired verdict / minimum action |
|---|---|---|
| Prop. 9.1 | sound numbers, bad label | verified; first `6` label -> `5`; add pole `M` pin for consumers |
| Not. 9.1 | ill-typed union domain | restrict `Q` to vertices `V_a` |
| St. 9.1 | sound | delete extra parenthesis |
| Not. 9.2 | sound orientation | say lower `G=F^o` is regular over upper `F`; singleton-pole regularity is a hidden lemma |
| St. 9.2 | sound intended root data | explicitly exclude `alpha_0` from `V_1`; retain possible root `V_2`/SF1 |
| St. 9.3 | false sign | replace by (4.1) |
| Not. 9.3 | literal nested sets | replace by local exit sets (4.2) on a characteristic path |
| St. 9.4 | proof double-counts | use disjoint exit charges; then (4.3) is proved |
| Prop. 9.2 | sound | make finiteness/down typing explicit |
| St. 9.5 | index/proof mismatch | use `i=1..n` local exit charges and (4.4) |
| Prop. 9.3 I--II | sound arithmetic | define `i=P/mu`; close typing |
| Prop. 9.3 III | wrong child denominators | replace (g),(h) by (2.2) |
| Prop. 9.3 IV | unbound `nu`, no proof | replace by (5.2); expose Bezout and axis dependencies |
| St. 9.6 | statement essentially survives | delete phantom B; correct `q` exponents; keep zero family |
| St. 9.7 | several typos | regular over G; `M_F`; root `d=j`; family verified |
| St. 9.8 | incomplete | add E2 `M=2`; correct `mu=4` equation; `Q(F)`, `M_F` |
| St. 9.9 | incomplete | add E3 `M=2,4` self-families; root only `s>=1`; `M_F` |
| St. 9.10 | incomplete/copy error | add E4 `M=3` self-family; delete spurious `M=4` alternative; root only `s>=1`; `M_F` |
| St. 9.11 | statement survives | correct `q` exponents |
| St. 9.12 | wrong row and false proof | row 4; use Section 8 closure, not printed dichotomy |
| Thm. 9.1 | conclusion repairable, proof incomplete | add pole pin kills for rows 1/5/7/10 and repaired row-4 proof |

## 11. Minimal repair stack and dependency map

The smallest trustworthy `td<6` proof needs exactly:

1. corrected Sections 3--6 local order/root law and down-tree propagation;
2. Proposition 5.8 and `Lambda>=3`;
3. corrected Proposition 8.1 polynomiality/gcd, Statement 8.4 edge
   divisibility, and **nonroot** Proposition 8.4;
4. table (23) with row 5 label and pole pin (3.3);
5. Definition 3.4 root typing (`V_1` uses `j>=1`; root `V_2` remains);
6. Proposition 9.3 with E5 and case-IV repairs;
7. Statement 9.3 with E6;
8. local, disjoint exit charges E9 and budget (4.3);
9. E1/E2/E3/E4/E7 transition corrections;
10. unique-pole regularity, the SF1 exclusion specific to the row-4 graph,
    and characteristic-sequence finiteness;
11. the axis `psi` terminal budget.

No root `M!=1` theorem occurs in this list.  No negative Bezout exponent is
used as a polynomial in Section 9: polynomiality is inherited from the
repaired Proposition 8.1; case IV uses only an integer linear combination.
No new tower-comparability claim is needed beyond the corrected Section 8
producer package.

## 12. Reconciliation with canonical consumers

### 12.1 `SHEET6-CAMPAIGN.md` Sections 3a and 4

The campaign's E2 zero-charge `M=2` family is **previously known and
independently revalidated here from the primary equation**.  The exact
continuation in Section 8.3 proves its self-family property and the
finite-exit argument used by the campaign.  E3 and E4 are likewise
independently reproduced.  The campaign's state graph is the repaired
graph; it must not be described as the printed Statements 9.6--9.11.

The campaign's budget layer is valid only under its E9/H2 branch-at-F
interpretation.  This report supplies the clean difference-set version
(4.2); literal Notation 9.3 remains unusable.

### 12.2 `SHEET6-REVIEW.md` E2--E4 and G2--G3

The review's E2--E4 findings are confirmed exactly, including the gcds and
zero-charge self-families.  Its G2 diagnosis is also correct for the
**printed** Statement 9.12: (26) does not kill the source's root outcomes.
The repaired row-4 proof uses (25), case IV(m), and finiteness.  Its G3
diagnosis remains correct as a source-proof criticism; the later pole pin
makes rows 1/5/7/10 mathematically dead but that argument is absent from
the thesis.

### 12.3 AF2/AF3/H3/HIII

- AF2's numerical gap prices agree with the corrected minus-`K` formula
  (4.1); any quotation of the printed plus-`K` formula must be corrected.
- AF3's pole pin and E9 filing are independently confirmed.
- H3/HIII's terminal `psi` mechanism is the correct axis use and is needed
  in repaired Statement 9.12.  It inherits the local-exit repair of
  Statement 9.4.
- HIII's SF1 warning is real in general: `(0,y)` can lie in `V_2`.  It is
  absent from the row-4 graph by the exact ratio checks in Section 7.2,
  not by a blanket “roots are IV” convention.

### 12.4 Rollback / survival ledger

Survives:

- table (23)'s eleven numerical rows;
- pole `M` pin and nonroot entry kills;
- E2--E4 campaign corrections;
- repaired row-4 exclusion;
- repaired conclusion `counterexample => td>=6`;
- all degree-six campaign work as a **separate** later analysis, subject to
  its own stated hypotheses.

Must be rolled back or qualified:

- any claim that the PDF itself proves Theorem 9.1 with its one-line
  citation;
- any use of literal Notation 9.3 in a sum along comparable vertices;
- any use of the printed sign in (24) or printed denominators (g),(h);
- any claim that Statements 9.8--9.10 are exhaustive as printed;
- any blanket root `M=1` kill from Proposition 8.4;
- any claim that Section 9 excludes `td=6`;
- any treatment of SF1 as impossible merely because `alpha_0=0` was
  introduced.

## 13. Final trust verdict

The source's Section 9 is not a proof that can be promoted statement by
statement without repair.  Its arithmetic core is recoverable, but its
budget notation, transition completeness, root typing, and final assembly
all require explicit amendments.

After those amendments, the precise mathematical result needed here does
survive:

    singleton-pole row 4 is impossible;
    rows 1,5,7,10 die at their nonroot pole entry;
    therefore a normalized counterexample has td >= 6.

This repaired result does not use the quarantined root clause of
Proposition 8.4 and does not exclude topological degree six.
