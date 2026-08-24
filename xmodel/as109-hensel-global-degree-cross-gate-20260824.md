# AS109 HENSEL-TO-GLOBAL-DEGREE / MONODROMY CROSS-GATE

Date: 2026-08-24  
Lane: independent cross-gate  
Dependency: only the dual-confirmed conditional AS109 Hensel lemma  
Status: **EXACT SCOPED THEOREM / NO NEW CONTRADICTION**

## 0. Verdict

Assume, conditionally, that there exists a polynomial

```text
F=(P,Q) in Z_109[x,y]^2,
F mod 109=(x-x^109,y),
det J_F=1.
```

Put

```text
K=Q_109,
M=K(P,Q),
L=K(x,y),
d=[L:M].
```

Then:

1. **`d >= 109`.**  Thus every complex map obtained by abstractly embedding
   the finitely generated coefficient field has mapping/topological degree at
   least 109.
2. Over a two-variable formal target tube, the finite separable generic
   algebra splits off 109 degree-one factors:

   ```text
   L tensor_M E  ~=  E^109 x A_infinity,
   dim_E A_infinity=d-109.                              (0.1)
   ```

   The displayed factors are the 109 integral Hensel branches.  The residual
   factor records generic sheets not controlled by those integral balls.
3. Local analytic/formal monodromy fixes the 109 displayed sheets
   individually.  Hensel supplies no nontrivial inertia element and no
   rational `C_109` deck action.
4. No divisibility or congruence for `d` follows.  Exact controls with the
   same residue-ball mechanism realize every integer degree `N>=109` once
   the constant-Jacobian hypothesis is removed.

The result is quantitatively stronger than “there are two colliding points,”
but it is not a new obstruction to an exact lift.  The smallest missing
global datum is elimination of `A_infinity`, or algebraic descent of the
formal branch permutations.

Exact arithmetic replay:

```bash
python3 cases/as109_degree_cross_20260824/check.py
```

Current result: **32/32 checks pass**.

## 1. Generic degree exists and is separable

The identity `det J_F=1` makes `P,Q` algebraically independent over `K`.
Indeed, differentiating an algebraic relation between them would contradict
the independence of `dP,dQ`.  Since both `L` and `M` have transcendence
degree two over `K`, `L/M` is finite.  It is separable in characteristic zero.

Its degree `d` is the generic number of geometric points in a fibre.  After
an embedding of a field of definition into `C`, it is the usual complex
mapping/topological degree.

## 2. Uniform Hensel branches give field embeddings

Fix `b in F_109` and choose integral representatives for `a,b`.  Introduce
independent target parameters `S,T` and the `109`-adically complete ring

```text
R=Z_109[[S,T]],       E=Frac(R).
```

Set the formal target to

```text
(U,V)=(109S,b+109T).
```

For each `a in F_109`, reduce the system

```text
F(X,Y)=(U,V)
```

modulo 109 at `(X,Y)=(a,b)`.  Fermat and the special derivative give

```text
F_bar(a,b)=(0,b),       J(F_bar)=I_2.
```

The parameter version of multivariate Hensel over the `109`-adically
complete ring `R` therefore gives a unique pair

```text
(x_a(S,T),y_a(S,T)) in R^2,
x_a=a mod 109,       y_a=b mod 109,                    (2.1)
```

satisfying `F(x_a,y_a)=(109S,b+109T)` exactly.

The elements `109S` and `b+109T` are algebraically independent over `K`.
Substitution using (2.1) defines an `M`-homomorphism

```text
sigma_a : L -> E.
```

It is injective: the image of `K[x,y]` contains the two algebraically
independent elements `P(x_a,y_a)=109S` and `Q(x_a,y_a)=b+109T`, so its
kernel has height zero and hence is zero.  The 109 homomorphisms are distinct
because `sigma_a(x)` have pairwise distinct residues modulo 109.

A separable extension of degree `d` has at most `d` embeddings into any
overfield.  Consequently

```text
d >= 109.                                                (2.2)
```

Equivalently, base change of the finite separable field algebra splits as
(0.1).  Each `E` factor is a clopen, degree-one, unramified formal branch.
There may be further `E` factors inside `A_infinity`; (0.1) claims only the
109 integral sections supplied by Hensel.

### Why the `b`-values do not add

There are 109 choices of `b`, and hence `109^2` source residue balls in all.
They lie over 109 disjoint target balls.  Generic degree counts sheets over
one target neighbourhood.  Therefore the correct lower bound is 109, not
`109^2`.

## 3. Passage to complex topological degree

Let `k_0` be the subfield of `Q_109` generated over `Q` by the finitely many
coefficients of `F`.  It is finitely generated of characteristic zero.  The
generic degree of a dominant generically finite morphism between geometrically
integral varieties is unchanged by extension of the constant field.  One can
see this by restricting to a nonempty target open on which the morphism is
finite locally free: its rank survives scalar extension.

Thus the degree over `k_0` equals the degree `d` over `Q_109`.  Any embedding
`k_0 -> C` produces a complex Keller map of the same degree.  Hence its
complex topological degree satisfies

```text
td=d>=109.                                               (3.1)
```

One may alternatively adjoin all 109 preimages of one integral target to
`k_0` and embed that still-finitely-generated field into `C`.  This preserves
109 distinct unramified points in one complex fibre.  The function-field
argument above additionally identifies the generic degree cleanly.

## 4. What monodromy and inertia actually say

Over the formal tube, the 109 sections in (2.1) are individually rational
over `E`.  The local absolute Galois/decomposition action therefore fixes
each corresponding sheet.  In particular:

```text
local ramification index = 1,
local residue degree     = 1
```

on every displayed branch.  The degree inequality is also the fundamental
inequality `sum e_i f_i <= d` applied to these 109 branches.

The product `E^109` admits every permutation of its factors, including the
cyclic relabelling

```text
a |-> a+c,       c in F_109.
```

This is only an automorphism of the **split base-changed algebra**.  Hensel
does not show that it descends to an element of `Aut_M(L)`, or even that the
109 embedded copies of `L` have the same image subfield of `E`.  Consequently:

* no global `C_109` deck group is obtained;
* no element of order 109 is forced in global monodromy;
* no divisibility `109 | d` follows;
* transitivity of global monodromy is compatible with the local subgroup
  fixing 109 sheets.

Two exact conditional strengthenings isolate the missing bridges:

1. If the cyclic factor permutation descends faithfully to `Aut_M(L)`, then
   Artin's fixed-field theorem gives `109 | d`.
2. If, independently, `A_infinity=0`, then `d=109`.  If the cyclic action
   also descends, `L/M` is cyclic Galois of degree 109, and the classical
   Galois Keller theorem would contradict nonautomorphy.

Neither descent nor `A_infinity=0` is supplied by residue-ball Hensel.

## 5. Exact no-congruence mechanism control

For every integer `N>=109`, put

```text
G_N=(x-x^109+109x^N,y).
```

Then

```text
G_N mod 109=(x-x^109,y),
det J_GN=1-109x^108+109N x^(N-1)=1 mod 109
```

on every integral residue ball.  Thus the identical Hensel argument gives
109 integral inverse branches over each target ball `(0,b)`.  But the
characteristic-zero generic degree of `G_N` is exactly `N`.  Taking
`N=109,110,111,...` realizes arbitrary congruence classes.

These are deliberately **non-Keller** controls: their Jacobian is a unit on
the integral balls but is not the constant polynomial one.  They prove that
the local splitting data alone carry no divisibility or congruence.  Any
such conclusion under exact `J=1` would require genuinely new global
constant-Jacobian or infinity input.

## 6. Cross-check against campaign structures

### 6.1 Sheet-number ledger

The AS109 lane cannot land in the active `td=6` book: (3.1) places it at
`td>=109`.  The promoted TDU result excludes **single-pole** configurations
when `td` is prime.  It would apply at `td=109` only after a separate theorem
proves `d=109`, and even then it leaves multi-pole configurations.  The
unvetted claim excluding all prime sheet degrees is not consumed.

Thus the new lower bound separates the AS109 disproof lane from the current
sheet-six proof ledger; it does not close either lane.

### 6.2 Secant projector and collision algebra

On the formal target tube, the 109 sections produce

```text
109^2 = 11881 ordered source pairs,
109*108 = 11772 ordered off-diagonal pairs.
```

Over one chosen source branch there are 108 off branches.  Globally a
degree-`d` separable map has off rank `d(d-1)` over the target and `d-1` over
one source sheet.  The inequalities

```text
d(d-1) >= 109*108,       d-1 >= 108
```

are exactly (2.2).  The secant idempotent merely records this clopen split;
as already reviewed, its equation lies in the localized collision ideal and
adds no coefficient rank.

### 6.3 Leading degree and support bounds

Bézout supplies only

```text
d <= deg(P) deg(Q).
```

Hence a hypothetical lift must satisfy `deg(P)deg(Q)>=109`.  But the seed
already forces `deg(P)>=109`, so the coarse bound is inert.  A named fixed
support family with an independently proved generic-degree upper bound below
109 would be excluded immediately; no current AS109 support has such a bound.
Leading-form divisibility does not constrain the residual rank `d-109`.

### 6.4 Bounded-y frontier

Any characteristic-zero theorem saying the map is an automorphism in a
bounded `y`-degree range forces `d=1` and therefore contradicts (2.2).  This
recovers the AS109 family exclusions (and, pending review, the independent
`deg_y<=5` frontier).  The quantitative degree statement supplies no larger
`y`-degree cutoff by itself; this interaction is still the already-known
noninjectivity contradiction in degree language.

## 7. Smallest missing global bridge

The exact residual object is `A_infinity` in (0.1).  Eliminating it requires
one of the following genuinely global statements:

* every generic sheet over the AS109 target tube is integral/bounded;
* a finite-flat normalization model across characteristic 109 with no
  horizontal contribution at infinity;
* properness/finite-ness over a target neighbourhood strong enough to keep
  the special Artin--Schreier degree 109 constant; or
* a support-specific exact upper bound `d<=109`.

For a Keller counterexample, uncontrolled nonproper branches at infinity are
precisely the expected escape mechanism.  Therefore “prove
`A_infinity=0`” is a precise form of the known nonproperness wall, not a cheap
new lemma.

Separately, turning the formal `a |-> a+c` relabelling into a rational deck
transformation requires an algebraization/descent theorem for local inverse
branches.  That is the smallest bridge to a `109 | d` statement.  No such
datum follows from Hensel, the secant idempotent, fixed finite support alone,
or the present sheet ledger.

## 8. Scope firewall

This report assumes an exact finite polynomial lift; it does not construct
one.  It proves a conditional degree lower bound and formal splitting, not a
new AS109 nonexistence result, not a congruence theorem, and not a JC2
decision.  It uses no web-priority claim, no AWS computation, and edits no
canonical file.
