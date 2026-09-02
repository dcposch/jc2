# Hostile review: ORTHO-DEFECT / ORTHO-FLOOR / DESCENT-DEGREE

Lane: ORTHO review, GPT-5.5, 2026-09-02.

Scope: frozen charged inputs in
`/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.Ye6yNV/inputs`.
I did not inspect `jc2-lean` and did not edit canonical ledgers.

## 0. Custody

The required SHA-256 check was run first. All five hashes matched:

```text
0916a85a7a8090d04461fa356518fb2ffd877374d1b8452a2b808d6f77156934  ideation-20260902T1608Z-opus5.md
ca9157617ecfd05fc21bffa6814aea830d1826c75b2ff7965c0128919f8da64a  n-vs-mapdeg-opus5-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  integration17-coordinator-fable51-20260902.md
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  d1-subtree-opus5-20260902.md
b404282f3c366a98dbcc745bcfb88cf64293cb17c6004ae784ce00f920c15bd2  ideation-20260902T1608Z-fable51-coordinator.md
```

Line references below are to those frozen copies unless explicitly prefixed
`xmodel/` for the read-only checks of integration #14 and #16 section C.

## 1. Verdict Matrix

| item | verdict | source line | exact repair / promotion |
|---|---:|---|---|
| ORTHO-DEFECT | CONFIRMED | `ideation-20260902T1608Z-opus5.md:107-120` | Promote the general identity with `(ep-dq)^2`. The `2deN` form requires `ep=dq`. "No gauge" applies to the general identity, not to dropping `(ep-dq)^2`. |
| common-resolution typing | CONFIRMED WITH REPAIR | `ideation-20260902T1608Z-opus5.md:75-90` | State that `m_nu` is the multiplicity of the strict transform of a generic member at the ordered blow-up center `nu`; it is `0` when the generic member misses that center. The total-transform exceptional basis is orthogonal after taking the union cluster. |
| ORTHO-FLOOR | CONFIRMED ONLY UNDER `ep=dq`; otherwise the executive statement is overbroad | overbroad: `ideation-20260902T1608Z-opus5.md:33-39`; repaired: `:133-135` | Promote `N >= L_S/(2de)` only under `ep=dq` and `d,e>0`. In general promote `N >= (L_S-(ep-dq)^2)/(2de)`, possibly vacuous. |
| ORTHO-DIV | CONFIRMED UNDER `gcd(d,e)=1` AND `ep=dq` | `ideation-20260902T1608Z-opus5.md:147-153` | Promote the stronger statement `#{nu: Delta_nu != 0} <= 2deN`; divisibility is a corollary. If `ep!=dq`, replace the budget by `(ep-dq)^2+2deN`. |
| ORTHO-SPLIT | CONFIRMED UNDER `ep=dq` | `ideation-20260902T1608Z-opus5.md:155-158` | Promote `#(cl(P)\cl(Q)) <= 2dN/e` and `#(cl(Q)\cl(P)) <= 2eN/d` for positive `d,e`. In the general formula add the `(ep-dq)^2` budget term. |
| DESCENT-DEGREE | CONFIRMED | `ideation-20260902T1608Z-opus5.md:213-218` | Promote with the explicit hypotheses `alpha beta != 0`, `d>0`, and both maps dominant. Leading cancellation is for degree descent, not for the map-degree proof. |
| NO-CEILING -> NO-CEILING[SINGLE-CLASS] | CONFIRMED AS SCOPE RETYPING | `n-vs-mapdeg-opus5-20260902.md:448-461`; `ideation-20260902T1608Z-opus5.md:293-307` | The proof is one-class. Retype the scope. Do not claim this changes any numerical ceiling, because `Delta^2=-2deN` is the same two-class intersection identity as `A.B=N`. |
| NOETHER-K specialisation | GAP AS WRITTEN; CONFIRMED ONLY AS A QUADRATIC ANALOGUE | `n-vs-mapdeg-opus5-20260902.md:345-356`; `ideation-20260902T1608Z-opus5.md:317-324` | Do not promote "NOETHER-K is the `p=q` specialisation" as a theorem. Promote: the quadratic equation `sum a_i^2=D^2-N` is the one-class diagonal analogue of ORTHO's mixed moment. The full NOETHER-K includes a canonical linear identity not supplied by ORTHO. |
| D1-PIN consistency | CONFIRMED AT D1 UNIT GRANULARITY | `d1-subtree-opus5-20260902.md:347-354`, `:522-524`; `integration17-coordinator-fable51-20260902.md:51-55` | For Moh `(64,48)`, `2de=24`, `N=9`, so ORTHO budget is `216`. D1 gives `q_D1=3/4`, `sum V2=12`, hence `sum_B 24*(3/4)V2(B)=216`. |
| `(64,48), N=4` arithmetic witness | ENRIQUES-CONSISTENT AS A MULTISET; EXCLUDED BY D1-STAR/D1-PIN | witness: `ideation-20260902T1608Z-opus5.md:258-267`; D1 row: `d1-subtree-opus5-20260902.md:522-524`; final binding: `integration17-coordinator-fable51-20260902.md:54` | Proximity inequalities alone do not kill the multiset: a single chain with the 14 `(1,2)` points first and the 40 `(1,1)` points after has no Enriques violation. The actual Moh row is now pinned to `N=9`, so `N=4` is dead for D1 reasons. |

## 2. Common Resolution Proof

Let `F=(P,Q): A^2 -> A^2` be dominant over `C`, with
`p=deg P`, `q=deg Q`. Dominance in dimension two makes the map generically
finite; write `N` for its geometric degree. Choose an ordered common resolution
`pi: X -> P^2` obtained by blowing up the union of the infinitely-near base
clusters at infinity needed by the two pencils `{P=u}` and `{Q=v}` and by their
generic mutual intersections at infinity.

For a blow-up center `nu` in that ordered union, define

```text
m_nu  = ord_nu(strict transform of a generic member P=u),
m'_nu = ord_nu(strict transform of a generic member Q=v).
```

If the center `nu` belongs only to the other pencil's cluster and the generic
member misses it, the multiplicity is `0`. This is the necessary convention when
the base loci differ. Equivalently, `m_nu` and `m'_nu` are the coefficients of
the total exceptional transforms in the final pullback classes of the generic
projective closures.

Use the total-transform basis. If `E_nu` denotes the total transform on the final
surface of the exceptional divisor created at `nu`, then

```text
H^2 = 1,  H.E_nu = 0,  E_nu.E_mu = -delta_{nu,mu}.
```

This remains true after taking the union of the two clusters. The strict
exceptional curves are not orthogonal in general; the total transforms are. This
is exactly the basis used in the charged statement at
`ideation-20260902T1608Z-opus5.md:86-90`.

Let `C_u` and `C_v` be the strict transforms of generic members of the two
pencils. Then

```text
C_u = pH - sum m_nu E_nu,
C_v = qH - sum m'_nu E_nu.
```

Two generic members of the same resolved pencil are disjoint, so

```text
C_u^2 = 0,     C_v^2 = 0.
```

The intersection `C_u.C_v` is the generic affine intersection number of
`P=u, Q=v`, hence

```text
C_u.C_v = N.
```

Equivalently, in the total-transform basis,

```text
sum m_nu^2       = p^2,
sum (m'_nu)^2    = q^2,
sum m_nu m'_nu   = pq - N.
```

Now set

```text
Delta = e C_u - d C_v
      = (ep-dq)H - sum (e m_nu - d m'_nu) E_nu.
```

The intersection-theoretic computation gives

```text
Delta^2 = e^2 C_u^2 - 2de C_u.C_v + d^2 C_v^2 = -2deN.
```

The coordinate computation in the orthogonal total-transform basis gives

```text
Delta^2 = (ep-dq)^2 - sum_nu (e m_nu - d m'_nu)^2.
```

Therefore

```text
sum_nu (e m_nu - d m'_nu)^2 = (ep-dq)^2 + 2deN.      (ORTHO-DEFECT)
```

This uses no Keller hypothesis, no `H2`, no irreducibility, and no Moh gauge.
The specialization

```text
sum_nu (e m_nu - d m'_nu)^2 = 2deN
```

requires `ep=dq`; in the campaign this is the GGV/Moh leading-form
normalisation `p=Kd`, `q=Ke`.

## 3. Corollaries

Write `Delta_nu=e m_nu-d m'_nu` and `L_S=sum_{nu in S} Delta_nu^2`.

For every subset `S`,

```text
L_S <= (ep-dq)^2 + 2deN.
```

Thus the exact floor is

```text
N >= (L_S - (ep-dq)^2)/(2de),        d,e > 0.
```

Only when `ep=dq` does this become the advertised monotone subset floor

```text
N >= L_S/(2de).
```

This is the main repair. The executive summary lines
`ideation-20260902T1608Z-opus5.md:33-39` omit that hypothesis; the formal
statement at lines `133-135` has it right.

Assume now `gcd(d,e)=1` and `ep=dq`. If `Delta_nu=0`, then
`e m_nu=d m'_nu`, hence `(m_nu,m'_nu)=(dt_nu,et_nu)`. If `Delta_nu != 0`, then
`Delta_nu^2 >= 1`. Therefore

```text
#{nu: Delta_nu != 0} <= sum Delta_nu^2 = 2deN.
```

Since `Delta_nu == e m_nu (mod d)` and `e` is invertible mod `d`,

```text
#{nu: d does not divide m_nu} <= 2deN.
```

The same argument mod `e` gives

```text
#{nu: e does not divide m'_nu} <= 2deN.
```

This proves ORTHO-DIV, and also repairs the line `ideation-...:153`: the coupled
form holds outside the stronger non-proportional set `{Delta_nu != 0}`.

For ORTHO-SPLIT, if `nu in cl(P)\cl(Q)`, then `m_nu>=1`, `m'_nu=0`, and
`Delta_nu^2=e^2 m_nu^2 >= e^2`. Hence

```text
#(cl(P)\cl(Q)) <= 2deN/e^2 = 2dN/e.
```

Similarly,

```text
#(cl(Q)\cl(P)) <= 2deN/d^2 = 2eN/d.
```

So the split statement is valid under `ep=dq`. Outside that gauge the same proof
has the larger budget `(ep-dq)^2+2deN`.

## 4. Desk Controls

I reran the desk resultant check with Python `3.14.7` and sympy `1.14.0`, exact
over `Q`, using `deg_x Res_y(P-u,Q-v)`.

```text
C1 resultant: -u + x
C2 resultant: (-u + x)^2
C3 resultant: (-4*u^3 + 3*u*x^2 + 4*v^2 + x^3)/4
C4 resultant: (-u + x^2)^3
C5 resultant: -u + x
```

| control | map `(P,Q)` | `(p,q)` | `(d,e)` | hand multiplicities | LHS | `N` by resultant | RHS |
|---|---|---:|---:|---|---:|---:|---:|
| C1 | `(x,y)` | `(1,1)` | `(1,1)` | two proper points at infinity: `(m,m')=(1,0),(0,1)` | `1+1=2` | `1` | `2` |
| C2 | `(x,y^2)` | `(1,2)` | `(1,1)` | `P` has mult `1` at `z_y`; `Q` has mult `2` at `z_x` | `1+4=5` | `2` | `(1-2)^2+2*2=5` |
| C3 | `(y^2+x, y^3+(3/2)xy)` | `(2,3)` | `(2,3)` | sequence below | `36` | `3` | `12*3=36` |
| C4 | `(x^2,y^3)` | `(2,3)` | `(2,3)` | `P` mult `2` at `z_y`, `Q` mult `3` at `z_x` | `6^2+(-6)^2=72` | `6` | `12*6=72` |
| C5 | `(x,y+x^2)` | `(1,2)` | `(1,2)` | triangular Keller, leading forms `x,x^2`; `P` has one proper point, `Q` has four unit base points, only the first common | `1+1+1+1=4` | `1` | `4` |

C2 is the negative control for the missing term: the naive `2deN` value is `4`,
but the true value is `5`; `(ep-dq)^2` is load-bearing.

C3 hand resolution: in the chart `X=1` at `z_x=(1:0:0)`, write local
coordinates `(y,z)=(Y/X,Z/X)`.

```text
P_u: y^2 + z - u z^2 = 0,
Q_v: y^3 + (3/2) y z - v z^3 = 0.
```

For `P_u`, the curve is smooth with tangent `z=0`; two generic fibres have
intersection multiplicity `4` at infinity, giving four unit base points along
that tangent. For `Q_v`, the tangent cone is `yz`; the branch tangent to `z=0`
shares the first infinitely-near point with the `P` chain, and the branch
tangent to `y=0` supplies the remaining four unit points of the `Q` cluster.
The ordered union can be written

```text
nu:          nu0  nu1  nu2  nu3 | eta1 eta2 eta3 eta4
m(P):         1    1    1    1  |  0    0    0    0
m'(Q):        2    1    0    0  |  1    1    1    1
3m-2m':      -1    1    3    3  | -2   -2   -2   -2
squares:      1    1    9    9  |  4    4    4    4
```

The internal checks are `sum m^2=4=p^2`, `sum (m')^2=9=q^2`, and
`sum mm'=3=pq-N`.

C4 is the required added non-automorphism with `d!=e` and `N>=2`. It is dominant,
has Jacobian `6xy`, and is not Keller. C5 is a Keller automorphism in the same
leading-form gauge: `Jac(x,y+x^2)=1`, `l(P)=x`, `l(Q)=x^2`, `ep=dq=2`.

## 5. DESCENT-DEGREE

The charged proof at `ideation-20260902T1608Z-opus5.md:213-218` is correct.
Let

```text
G_1 = beta^d P^e - alpha^e Q^d
Phi(u,v) = (u, beta^d u^e - alpha^e v^d).
```

Then `(P,G_1)=Phi o (P,Q)`. For generic `(a,b)`, the equation

```text
beta^d a^e - alpha^e v^d = b
```

has exactly `d` distinct solutions in `v`, and over each solution the fibre of
`(P,Q)` has `N` points counted with multiplicity. Hence

```text
N(P,G_1) = d N(P,Q).
```

Equivalently, geometric degree is multiplicative under dominant generically
finite composition. The only hypotheses needed here are `alpha beta != 0`,
`d>0`, and dominance. The leading-form cancellation is needed for Moh/GGV degree
descent, not for this map-degree equality.

## 6. NO-CEILING Retyping

The retyping is correct as a scope repair. Section 3.7 of `n-vs-mapdeg` states
one class

```text
Z = D H - sum a_i E_i,     Z^2=N,
```

and proves that the stated one-class constraints do not bound `D=Z.H` at fixed
`N`; see `n-vs-mapdeg-opus5-20260902.md:448-461`. That proof does not quantify
over pairs `(C_u,C_v)` with

```text
C_u^2=C_v^2=0,     C_u.C_v=N,     C_u.H : C_v.H = d:e.
```

For such a pair, `Delta=eC_u-dC_v` has `Delta.H=0` and
`Delta^2=-2deN`. That is a genuine pair negativity absent from the one-class
proof.

But it is not new information beyond `A^2=B^2=0` and `A.B=N`; it is exactly the
same identity rewritten. The coordinator's blind submission already states this
as `(LATTICE)` from `A^2=B^2=0`, `A.B=N` at
`ideation-20260902T1608Z-fable51-coordinator.md:9-18`.

Therefore the record repair should be narrow:

```text
NO-CEILING -> NO-CEILING[SINGLE-CLASS].
```

Do not promote "NO-CEILING is false." Its one-class theorem remains true. Also
do not claim the retyping changes a numerical bound already drawn from it:

* Integration #14 section C says the day's instruments yield floors and no
  degree ceiling from the lattice/profile/Noether package
  (`xmodel/integration14-coordinator-fable51-20260902.md:75-89`). ORTHO does not
  by itself give `D <= C(N)`, so no numerical bound changes there.
* Integration #16 section C says the free `D_1` sub-tree only lowers `N`
  (`xmodel/integration16-coordinator-fable51-20260902.md:90-98`). That sentence
  is overbroad: it is true for the contact functional, not for all boundary
  functionals. Integration #17 has already retyped it to
  `UPPER-ONLY[CONTACT]` and half-retracted FILTER-INVERSION at
  `integration17-coordinator-fable51-20260902.md:60-71`.

So the retyping changes scope language and the classification of a route; it
does not create a new campaign ceiling or alter any promoted numeric lower
floor.

## 7. NOETHER-K

The charged "NOETHER-K is the `p=q` one-vector specialisation" should not be
promoted literally.

What is true: the quadratic equation in NOETHER-K,

```text
sum a_i^2 = D^2 - N,
```

is the same total-transform quadratic form as the mixed moment

```text
sum m_i m'_i = pq - N,
```

after diagonalising to a one-class ledger. This is an analogue, not the full
ORTHO theorem with `p=q`.

What fails literally: ORTHO's fibre classes satisfy `C_u^2=C_v^2=0`. If one
sets `p=q` and also makes it a one-vector statement `m=m'`, then
`sum m_i^2=p^2` and `sum m_i m'_i=p^2`, forcing `N=0`, not the Keller
geometric degree. NOETHER-K also includes the linear canonical equation
`sum a_i = 3D - 2N - kappa + n(W-S)` at
`n-vs-mapdeg-opus5-20260902.md:345-356`; ORTHO does not supply that.

Repair:

```text
NOETHER-K[QUADRATIC] is the one-class diagonal analogue of ORTHO's mixed moment.
NOETHER-K[FULL] is not a specialisation of ORTHO.
```

## 8. D1-PIN / D1-STAR Consistency

D1-PIN states, at a bottom major disc `B`,

```text
N_B = V_2(B) q(B),
q(B) = (1-delta_1)de/(d+e),
```

with the exact row values printed at `d1-subtree-opus5-20260902.md:522-528`.
D1-STAR states that below `delta_1` the `g` roots separate as a star and no `f`
root follows a `g` root below that level (`d1-subtree-...:365-378`). Thus the
ORTHO interpretation is:

* proportional discs above the first separation have `Delta_nu=0` and contribute
  zero;
* the nonzero square budget is carried by the star separation below `delta_1`;
* at D1's own bottom-disc granularity, the square budget is exactly
  `2de V_2(B)q(B)`.

For Moh's `(64,48)` row, D1 gives

```text
u = 12,     q(B)=3/4,     U = 9
```

at `d1-subtree-opus5-20260902.md:522-524`. Integration #17 binds the final
reading `(64,48) -> 9` at
`integration17-coordinator-fable51-20260902.md:51-55`. Here `2de=24`, so

```text
N = sum_B V_2(B) * 3/4 = 12 * 3/4 = 9,
ORTHO budget = 2deN = 24*9 = 216.
```

Termwise over D1 bottom units,

```text
sum_B 2de V_2(B)q(B) = sum_B 24*(3/4)V_2(B)
                     = 18 * sum_B V_2(B)
                     = 18*12
                     = 216.
```

This confirms consistency. ORTHO is not an alternative proof of D1-PIN; it is
the global square-budget check that the D1-PIN/D1-STAR decomposition must obey.

## 9. The `(64,48), N=4` Arithmetic Witness

The producer's arithmetic witness at `ideation-20260902T1608Z-opus5.md:258-267`
uses `(K,d,e)=(16,3,4)`, `N=4`, and the multiset

```text
40 points with (m,m')=(1,1),  Delta= 1,
14 points with (m,m')=(1,2),  Delta=-2.
```

The arithmetic is correct:

```text
sum Delta      = 40 - 28 = 12 = dN,
sum Delta^2    = 40 + 56 = 96 = 2deN,
sum m Delta    = 12,
sum m' Delta   = 40 - 56 = -16 = -eN.
```

It is also consistent with the bare Enriques proximity inequalities. Put the 14
`(1,2)` points first and the 40 `(1,1)` points after them in a single free chain,
each point proximate only to its predecessor. Then for every nonterminal point,

```text
m_i  >= m_{i+1},     m'_i >= m'_{i+1},
```

and the terminal point has no proximate successor. A desk checker on that chain
returned zero proximity violations. Therefore proximity alone does not refute
the multiset. It remains only a multiset witness, not a full degree-64/48
cluster with Moh data.

D1-STAR/D1-PIN now excludes it for the actual Moh row. The frozen D1 table has
`q(B)=3/4` for `(64,48)` (`d1-subtree-...:522-524`), and Integration #17 binds
the row to `N=9` (`integration17-...:54`). Thus `N=4` is not an admissible D1
value for the charged `(64,48)` row. The kill is D1 arithmetic/star structure,
not Enriques proximity.

## 10. What ORTHO Can and Cannot Decide

ORTHO can decide:

* the exact global square budget on a common total-transform resolution for any
  dominant polynomial map;
* subset lower bounds on `N` when `ep=dq`;
* bounded counts of non-proportional, non-divisible, and one-sided cluster
  points;
* consistency of a fully typed Moh/D1 decomposition with the global
  intersection budget;
* map-degree scaling along Moh's `G_1=beta^d P^e-alpha^e Q^d` descent.

ORTHO cannot decide:

* a degree ceiling `D <= C(N)` by itself, since proportional chains contribute
  zero to `sum Delta_nu^2` while carrying degree;
* any lower bound on `L_S` from an untyped tree;
* realisability of a multiplicity multiset;
* Enriques proximity, unless a proximity graph is supplied;
* D1-PIN or D1-STAR, which are stronger Jacobian/Moh statements;
* the `(64,48), N=4` row without the D1 input. ORTHO permits the arithmetic
  multiset; D1 excludes the row.

No new mathematical OPEN is needed from this review. The bounded computation
left to the census is implementation-level: emit
`L(skel)=sum_{visible}(e m-d m')^2`, bounded by `0 <= L(skel) <= 2de U(skel)`
under `ep=dq` and the existing `N` ceiling.

## 11. Typed Verdict Block

```text
SUBMISSION    ORTHO round, Opus ideation 1608Z plus coordinator LATTICE.

ORTHO-DEFECT  CONFIRMED.  General theorem:
              sum_nu (e m_nu - d m'_nu)^2 = (ep-dq)^2 + 2deN.
              Promote with common-resolution typing and total-transform basis.

ORTHO-FLOOR   CONFIRMED only under ep=dq.  General repaired floor:
              N >= (sum_S Delta_nu^2 - (ep-dq)^2)/(2de).
              The executive no-hypothesis subset form is overbroad.

ORTHO-DIV     CONFIRMED under gcd(d,e)=1 and ep=dq:
              #{Delta_nu != 0} <= 2deN, hence the two divisibility bounds.

ORTHO-SPLIT   CONFIRMED under ep=dq:
              #(cl(P)\cl(Q)) <= 2dN/e and #(cl(Q)\cl(P)) <= 2eN/d.

DESCENT       CONFIRMED:
              N(P, beta^d P^e - alpha^e Q^d) = d N(P,Q).

NO-CEILING    RETYPE to NO-CEILING[SINGLE-CLASS].  The pair negativity is real
              but is only the A^2=B^2=0, A.B=N identity.  No numeric bound from
              integration #14 or #16 changes; #16's universal UPPER-ONLY prose
              is repaired to UPPER-ONLY[CONTACT], as Integration #17 records.

NOETHER-K     GAP as "p=q specialisation" of ORTHO.  Promote only:
              NOETHER-K[QUADRATIC] is the one-class diagonal analogue of the
              mixed moment; NOETHER-K[FULL] has extra canonical content.

CONTROLS      Five desk controls pass: the charged three, plus non-Keller
              (x^2,y^3) with d!=e and N=6, plus Keller automorphism
              (x,y+x^2) in leading-form gauge.  C2 confirms the (ep-dq)^2
              term is necessary.

D1            CONSISTENT.  On Moh (64,48), D1 gives q(B)=3/4, sum V2=12,
              N=9; ORTHO gives 2deN=24*9=216, equal to
              sum_B 24*(3/4)V2(B).

N=4 WITNESS   Enriques proximity does not refute the multiset
              40*(1,1)+14*(1,2).  D1-PIN/D1-STAR excludes it for the actual
              (64,48) row by pinning N=9.

PROMOTION     Promote ORTHO-DEFECT, ORTHO-FLOOR[EP=DQ],
              ORTHO-FLOOR[GENERAL], ORTHO-DIV[EP=DQ,GCD],
              ORTHO-SPLIT[EP=DQ], DESCENT-DEGREE, and
              NO-CEILING[SINGLE-CLASS].  Do not promote the literal
              NOETHER-K specialisation sentence or any claim that ORTHO alone
              kills a Moh survivor.
```

<!-- BODY-END -->
