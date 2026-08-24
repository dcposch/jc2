# AS109 bounded-support gate

**Verdict: `NO-FROZEN-GRAMMAR`.**

- Round: `20260824T0719Z-c17bd25`
- Prime/seed: `p=109`, `(x-x^109,y)` over `F_109`
- Registered cap: at most eight distinct correction slots
- Enumeration: **not run**
- AWS: **not used**
- Characteristic-zero inference: **none**
- Ledgers: not edited

The preregistration and manifest were frozen before any transition enumerator
was written or run. The monomial-count cap does not make the exponent grammar
finite: already at the first lift there are infinitely many two-slot,
collision-preserving representatives with unbounded exponent. The exact
source gauge that identifies these representatives changes their literal
supports and their first nonlinear residual supports. No finite normal-form
theorem with successor transport was supplied or proved. A degree rectangle
would make the computation finite but is expressly forbidden and would be an
unregistered sparse cap.

The preregistered stop therefore fires before SCC enumeration. There is no
`HEIGHT-CERT`, `NO-CYCLE-AT-8`, `SUPPORT-ONLY`, or `FEASIBLE-CYCLE` result.

## 1. Frozen artifacts

The exact freeze file is
`cases/as109_support_20260824/FREEZE.sha256`:

| Artifact | SHA-256 |
|---|---|
| `cases/as109_support_20260824/PREREGISTRATION.md` | `be9138a90b661f069197a4c22235ee1caa4e03fcecd2dab8c980e8934f2d6301` |
| `cases/as109_support_20260824/manifest.json` | `c69d70805bdba5793f385fca9c289f9a12a8c58c45e1625e1c2f69a9632f0364` |
| `cases/as109_support_20260824/FREEZE.sha256` | `0a535ca2877ec3672044faa5c5f20878c4b95adddf4087b89f772d030d6e140e` |

Post-freeze exact replay artifacts:

| Artifact | SHA-256 |
|---|---|
| `cases/as109_support_20260824/verify_spec_obstruction.py` | `1bb8f86596b75bd43e467dc84b569e8fb2bb2744c198c40f5244f0b054634165` |
| `cases/as109_support_20260824/spec_obstruction.json` | `b95ad244da3ea75100c61143dc9c0026ac567c8acfc2398a86ce1623a101131e` |

The replay uses only exact integer and `F_109` sparse-polynomial arithmetic.
It recomputes the two frozen hashes before checking the control family.

## 2. Exact registered equations

Use the fixed integral representative through the first nonlinear successor:

```text
P=x-x^p+p A_0+p^2 A_1,
Q=y      +p B_0+p^2 B_1                  modulo p^3.
```

Writing `L(A,B)=A_x+B_y`, direct determinant expansion gives

```text
E1: L(A_0,B_0)=x^(p-1),

E2: L(A_1,B_1)=-N(A_0,B_0),

N(A,B)=(A_x-x^(p-1))B_y-A_yB_x           over F_p.
```

For monomials the exact nonlinear interaction is

```text
[x^a y^b,x^c y^d]
 =(a*d-b*c)x^(a+c-1)y^(b+d-1).
```

The coefficient is reduced modulo 109; zero-coefficient interactions are not
edges. The frozen collision conditions are

```text
A_i(1,0)-A_i(0,0)=0,
B_i(1,0)-B_i(0,0)=0,                    i=0,1.
```

The frozen gate retains those stricter marked-section equations. A
post-freeze audit proves that they are unnecessary for a future exact
fixed-support lift, as follows.

### 2.1 Hensel nonautomorphy lemma

Let `F in Z_109[x,y]^2` reduce to `(x-x^109,y)` and satisfy `det J_F=1`
exactly. For a residue point `c in F_109^2`, the derivative of the reduction
is the identity. Multivariate Hensel therefore says that, for every integral
target `t` reducing to `F_bar(c)`, the equation `F(z)=t` has exactly one
solution in the residue ball `c+109 Z_109^2`.

Fix `b in F_109`. For every `a in F_109`,

```text
F_bar(a,b)=(a-a^109,b)=(0,b).
```

Consequently every target in the ball `(0,b)+109 Z_109^2` has one preimage
in each of the 109 distinct balls `(a,b)+109 Z_109^2`. Thus `F` is
noninjective over `Q_109`.

This also has the required complex scope. A polynomial has only finitely many
coefficients; adjoining those coefficients and two of the distinct Hensel
preimages to `Q` gives a finitely generated characteristic-zero field. Such
a field embeds abstractly in `C`. The determinant identity and collision
survive the embedding, producing a complex polynomial Keller
nonautomorphism. Hence an exact integral fixed-support solution would be a
direct JC2 counterexample, not merely a modular survivor.

This lemma does **not** assert that a solution exists and does not repair the
failed finite grammar. The frozen collision equations remain in force for
this run; the witness family below satisfies them anyway.

## 3. Parametric obstruction to literal finiteness

For every integer `m>=1`, put

```text
A_0=y^m,
B_0=x^108 y.
```

Then, exactly over `F_109`,

```text
A_0x+B_0y=x^108.
```

Both corrections vanish on `y=0`, so the two marked sections remain fixed.
There are exactly two correction slots:

```text
(P,(0,m)),  (Q,(108,1)).
```

Thus every `m` satisfies the first lift and collision conditions with two
slots, far below the cap eight. The exponent `m` is unbounded. A cap on the
*number* of monomials therefore does not imply a finite set of exponent
vertices.

This is not merely a formal tangent family. Let

```text
G_m=(x+109 y^m,y).
```

It is an exact integral triangular polynomial automorphism, has determinant
one and inverse `(x-109 y^m,y)`, and fixes `(0,0)` and `(1,0)`. Precomposing
the canonical first Artin--Schreier lift by `G_m` produces precisely the
displayed `(A_0,B_0)` modulo `109^2`. Hence the family lies inside the full
frozen source-gauge relation, not outside it.

Literal enumeration is therefore infinite. Omitting these representatives
would require a proved gauge normal form, not a larger loop limit.

## 4. The gauge does not preserve the proposed graph data

For the same family, exact calculation gives

```text
N(A_0,B_0)
 =-x^216+(m mod 109)x^107 y^m.             (4.1)
```

The canonical representative `A_0=0`, `B_0=x^108y` has only the first term
`-x^216`. Thus first-order gauge-equivalent representatives have different
nonlinear residual supports, including an arbitrary exponent `m`.

The exact gauge does transport through the successor, but it demonstrates
the support problem rather than removing it. Precompose the canonical
`W_3` tower by `G_m`; the transported second-layer correction is

```text
A_1=-x^108 y^m,
B_1= x^216 y+108 x^107 y^(m+1).             (4.2)
```

Equations (4.1)--(4.2) satisfy `E2` and the marked collision exactly. They
introduce three new correction slots, so the union through `E2` has five
slots but is not a same-slot cycle. The replay checks this for
`m=1,2,3,108,109,110,1000`; the displayed formulas prove it for every
`m>=1`. In particular, the `x^216` residual has coefficient `-1` for every
`m`, including `m` divisible by 109.

Consequences:

1. An SCC on literal exponent vertices depends on which representative of
   the frozen gauge orbit is used.
2. Quotienting by the full gauge without transporting its higher correction
   layers can create or delete apparent support transitions.
3. Transporting the gauge exactly introduces new, unbounded exponent slots,
   so it does not itself give a finite support normal form.
4. The property “this displayed representative uses at most eight slots” is
   not enough to define a gauge-invariant finite transition graph.

## 5. Why a symbolic motif enumeration was not substituted

One could propose a redesigned grammar with exponent variables instead of
literal exponent vertices. That would require, before claiming exhaustive
enumeration:

- a finite list of correction-incidence motifs covering every minimal
  support of size at most eight;
- a proof that disconnected or simultaneously born cancellation components
  may be removed or represented without losing the collision condition;
- a terminating solver for all nonnegative exponent equations and all
  congruence branches in coefficients such as `a*d-b*c mod 109`;
- a canonical gauge section, or an exact groupoid transition rule, through
  `mod 109^3`;
- a proof that the same-slot cycle predicate is invariant under that rule.

None follows merely from the cap, and no such theorem was supplied by the
idea card or obtained in this gate. Sampling the exponent parameters would
be a hidden rectangle. Declaring only corrections that cancel a previously
present residual would omit simultaneous cancellation cycles unless a new
minimal-support ordering theorem were proved.

Accordingly a symbolic-motif compiler is a possible **redesign**, not the
registered experiment. The current root must stop rather than invent that
new dependency during enumeration.

### 5.1 Closed-support contraction criterion for a redesign

There is a stronger positive criterion than checking one nonlinear
successor. For fixed correction supports write the exact determinant equation
over `Z_109` as

```text
E(u)=L(u)-s+109 N(u)=0,
s=x^108,
N(A,B)=[A,B]-x^108 B_y.
```

Let `U'` be a finite free coefficient module after a proved gauge section and
let `W` be a finite residual module such that

```text
s in W,  L(U') subset W,  N(U') subset W.
```

If `L:U'->W` has a `Z_109`-unit inverse—or a right inverse `R` with the
chosen section `U'=im R`—then

```text
T(u)=R(s-109 N(u))
```

is a 109-adic contraction. Integral polynomial maps are 1-Lipschitz on the
unit coefficient ball, so the factor 109 makes `T` strictly contracting.
Its unique fixed point satisfies `E(u)=0`. Combined with the Hensel lemma,
`CLOSED-SUPPORT + UNIT-L` would therefore produce a direct JC2
counterexample.

No enumerated core exists in this stopped run, so no candidate meets this
criterion. The exact controls fail closure:

- for the canonical slot `B=x^108y`, `L(U)` is supported at `x^108` while
  `N(U)` already contains `x^216`;
- even the five-slot union in (4.2) is not closed: the allowed slot
  `B=x^216y` by itself produces `N=-x^324`, outside its derivative residual
  span.

The replay checks the second counterresidual. This criterion is recorded only
as a resurrection target; it does not authorize adding slots until closure,
widening eight, or searching an exponent rectangle.

## 6. Controls and exact replay

`verify_spec_obstruction.py` checks:

1. both frozen input hashes;
2. `E1` and collision for the parametric triangular family;
3. the nonlinear formula (4.1);
4. the transported successor (4.2), including `E2` and collision;
5. two active first-layer slots, five union slots through the successor, and
   absence of a same-slot cycle;
6. the persistent new `x^216` residual;
7. failure of `CLOSED-SUPPORT` via the exact `-x^324` counterresidual.

The canonical escaping ray is recovered at `m` absent/zero:

```text
B_0=x^108y -> B_1=x^216y -> ... .
```

This is a control, not a height certificate for all cap-eight supports.
Gauge and toy-cycle transition controls were not built because the frozen
grammar failed before an enumerator existed. Running them on a hand-selected
finite exponent box would violate the preregistration.

Replay command:

```text
python3 cases/as109_support_20260824/verify_spec_obstruction.py
```

Expected top-level output:

```text
verdict = PASS-SPEC-OBSTRUCTION-CONTROL
enumeration_run = false
```

## 7. Exact interpretation and next trigger

`NO-FROZEN-GRAMMAR` means:

- the proposed cap-eight graph is not yet a finite exhaustive mathematical
  object;
- no statement has been proved about the existence or absence of cap-eight
  bounded-support lifts;
- no support SCC or coefficient-feasible cycle has been found;
- no characteristic-zero inference is available;
- no cap, degree, or prime may be changed as a response.

Conditionally, an exact `CLOSED-SUPPORT + UNIT-L` support would give a
characteristic-zero counterexample by contraction and the Hensel lemma. No
such support was found or tested by enumeration here.

The only resurrection trigger is a separately reviewed theorem giving either
(a) a finite gauge-normal-form grammar with exact successor transport, or
(b) a terminating symbolic-motif classification exhaustive for all exponent
supports of size at most eight. A request to choose a large exponent box is
not a trigger.

No result here proves or disproves JC2.
