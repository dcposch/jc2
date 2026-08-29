# Sigray Section 7: full independent source audit and repaired Euler ledger

Date: 2026-08-28  
Scope: Sigray, Section 7, printed pp. 35--39, from Notation 7.1 through
Corollary 7.1.  This is a source audit, not a proof of JC2 and not a landing
certificate.

## 0. Executive verdict

Section 7 has a sound mathematical core, but it is **not correct as printed**.
There are three layers.

1. The local critical-value statements (Statements 7.1--7.3,
   Propositions 7.1--7.3, and Proposition 7.2) are true after the already
   promoted repairs to Sections 3--6.  Statements 7.2, 7.3 and Proposition
   7.2 have no printed proofs; Proposition 7.1 has an `F/G` error and two
   reversed signs; Proposition 7.3 has several notation and deformation
   gaps.  Complete repairs are given below.
2. **Notation 7.3 is indexed incorrectly.**  It subtracts
   `kappa_F(pi(F)-1)` once for every normalized puncture.  Proposition 7.3
   proves only one such lower bound for the whole direction cluster
   `R^*_(F,c)`.  These are different when a special direction has more than
   one normalized puncture.  A two-branch exact local Jacobian-one germ below
   shows that the tempting strengthening to one bound per puncture is false
   in precisely the analytic category used by the printed deformation.
3. Consequently, literal Proposition 7.4 and literal equation (22) are not
   proved.  Equation (22), Proposition 7.4, and Corollary 7.1 become rigorous
   after replacing the per-puncture `delta_a` by a **per-direction-cluster
   excess**.  Equivalently, one may retain the printed `delta_a` but must add
   a nonnegative splitting term.  The printed final Euler line also has an
   independent sign typo, and its assertion that every value curve is
   biholomorphic to `C` is unproved and unnecessary.

The repaired result needed by the later books is

```text
td(f,g)
  = 1
    + sum_(F in T_(a0,cv)) kappa_F (pi(F)-1)
    + sum_(a in C) delta_a^cl,

delta_a^cl >= 0,       delta_a^cl = 0 for generic a.       (22-cl)
```

It still gives Corollary 7.1 and every Section 9 `lambda`/`psi` budget.
What does **not** survive is the campaign wording that `delta_a` is a sum of
nonnegative *per-puncture* excesses.  Slack zero forces every direction
cluster to saturate Proposition 7.3; it does not force every puncture in a
split cluster to have the baseline multiplicity individually.

Finally, Section 7 gives **no repair at all** for the newly exposed root case
of Proposition 8.4.  It never mentions `M_F`; `(0,y)` is positive, not a
critical-value vertex, and the Euler ledger has no row that is forced merely
by `M_(0,y)=1`.

## 1. Custody and conventions

Primary source:

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
```

The PDF page number equals the printed page number.  Section 7 begins on
printed p. 35 and ends on p. 39.  Git HEAD during the audit was
`418e413593120d19e15e6546eb50c985f4b1f038`.

Relevant corrected-package inputs, hashed during this audit:

```text
f1da7026320b3dedd47534428aa53e6df66c698888c398e4f7eb5288d89b0748  ladder/SIGRAY-AUDIT.md
10bc55d53f9cf9a9e6a4535787f6e208a25f0ebfbd6dbd803f68b00f8ca8f5cd  xmodel/sigray-prop42-constant-shift-repair-sol-ultra-20260828.md
47f2b608f47bc7f426c6cf3e8634c8704bdd675aa909eb63e3f4c6861c21dfb1  xmodel/sigray-prop42-constant-shift-repair-hostile-review-opus5-20260828-r1.md
110591663b4077509dee35f4c39daf687603c94cd3e20d559f78426da3ef6ca7  xmodel/sigray-prop51-forced-puncture-shift-coordinator-integration-sol-ultra-20260828.md
c3d6ff9239fb136cc35b815de6e229755f7d27b640481e7751d03d63291d1ebd  xmodel/sigray-prop67-prop68-source-audit-sol-ultra-20260828.md
bb033a7130da671c4a02b62053c8c24b6e68d9a453f542c93588eb945f1c8648  xmodel/sigray-lemma61-prop58-coordinator-integration-sol-ultra-20260828.md
47eef0925470fc769eec08e6d3bf972446feaaff6f6ef709c154edaa31054caf  xmodel/sigray-prop58-every-fiber-independent-audit-sol-ultra-20260828.md
```

The corrected notation is load-bearing.  On the fibre `f=a`, write

```text
A := f-a,
d_F := d_(A,F),
p_F^a := p_(A,F).
```

At `F in T_a^0`, the source's bare polynomial is

```text
P_F := p_(f,F) = p_F^a + a.
```

Thus the source condition `P_F(c)=a` becomes `p_F^a(c)=0`.  One must not
silently replace bare `P_F` by centred `p_F^a` in one line and retain the
bare cross-fibre formulas in the next.  For the `g`-pattern put
`q_F:=p_(g,F)`.

The following promoted repairs are assumed and are used explicitly:

- the jump/max interpretation of `kappa_F` forced by corrected Statement
  3.8;
- `d_F,p_F` mean the centred `f-a` data;
- Statement 3.14 transports truncations only up to a common root-of-unity
  change of residual coordinate;
- the complete Proposition 4.2 constant-shift repair, also for the
  translated pair `(A,g)`;
- the puncture-centred Proposition 5.1 threshold with
  `B_P=g-g(P)` at finite punctures and its sidedness/non-leakage theorem;
- repaired Propositions 6.7--6.8 and repaired Lemma 6.1;
- the every-fibre Proposition 5.8 identity.

No file under `jc2-lean` was read, built or modified.  No heavy computation
was needed; the audit used source extraction, exact hand algebra, and local
analytic models only.  No AWS job was warranted.

## 2. Statement-by-statement verdict ledger

| source item | page | strict source verdict | repaired mathematical verdict |
|---|---:|---|---|
| Notation 7.1 | 35 | **VERIFIED WITH NIT** | Well-defined with centred `d_F`; the opening suitable `kappa in N` is unused and should be `N*` if retained. |
| Statement 7.1 | 35 | **VERIFIED** | `F in T_(a,cv)` implies `pi(F)>1`.  Condition (7) is not needed for Proposition 4.1's order inequality. |
| Statement 7.2 | 35 | **GAP IN SOURCE** (no proof) | **PROVED** by the promoted Proposition 5.1 sidedness/non-leakage theorem. |
| Statement 7.3 | 35 | **GAP IN SOURCE** (no proof) | **PROVED** from pole-ray downness, Proposition 7.2, and repaired Sections 5--6. |
| Proposition 7.1 | 35--36 | **ERRATUM** | Statement true for the translated tower.  Printed proof says `d_(h_j,G)=0` where it needs `d_(h_j,F)=0`, and prints both edge slopes with the wrong sign. |
| Proposition 7.2 | 36 | **GAP IN SOURCE** (no proof) | **PROVED** directly from the centred threshold and the leading-bracket equation. |
| Notation 7.2 | 36 | **INCOMPLETE DEFINITION** | Well-defined after adding uniqueness from corrected Statement 3.13 / Proposition 7.2. |
| Proposition 7.3 | 36--38 | **ERRATUM + PROOF GAPS** | The cluster inequality and simple-direction equality are true.  The proof needs the forced centre, a corrected exponent, a proper local tube, and twist-equivariant transport. |
| Notation 7.3 | 38 | **STATEMENT-LEVEL INDEXING ERROR** | Replace per-puncture subtraction by per-direction-cluster subtraction, or add the splitting correction in Section 8 below. |
| Proposition 7.4 | 38 | **GAP AS LITERALLY TYPED** (no proof) | True for `delta_a^cl`; generic equality follows from simple directions.  Literal per-puncture nonnegativity is not obtained. |
| Proposition 7.5 | 38--39 | **ERRATUM / GAP AS LITERALLY TYPED** | Equation (22-cl) is true.  Printed proof uses the wrong `delta`, an unproved injectivity claim, boolean rather than multiplicity pushforward, and a wrong final sign. |
| Corollary 7.1 | 39 | **PRINTED PROOF UNSOUND THROUGH 7.4/7.5** | The inequality is true from repaired (22-cl), and remains valid for every later budget consumer. |

Chronologically, the first omitted proof is Statement 7.2 on p. 35.  The
first false displayed proof target is Proposition 7.1 on p. 36.  The first
load-bearing statement-level defect in the Euler ledger is Notation 7.3,
p. 38, lines 11--14 in a layout extraction of that page.

## 3. Notation 7.1 and Statements 7.1--7.3

### 3.1 Notation 7.1

The corrected definition is

```text
T_(a,cv) := {F in T_a : d_(f-a,F)=0 and d_(g,F)=0}.
```

The set does not depend on the suitable denominator written before the
source definition.  It is finite: each puncture ray has one and only one
zero of `d_(f-a)`, and there are finitely many punctures.

### 3.2 Statement 7.1

At a critical-value flag, write

```text
A_F^+ = p(eta),       g_F^+ = q(eta).
```

Both orders are zero.  Their leading Jacobian vanishes.  Proposition 4.1's
order calculation therefore gives

```text
0 = d_(A,F)+d_(g,F) > 1-pi(F),
```

so `pi(F)>1`.  Proposition 4.1's hypothesis (7) is not needed for the
nonnegativity/order comparison itself; this was independently re-derived in
the Sections 2--6 audit.  Hence a possibly scalar `q` is not an exception.

### 3.3 Statement 7.2

The source means `F_P^* notin T_(a,pole)`, although text extraction loses the
subscript.  If a ray contains `F in T_(a,cv)`, then `g(P)` is finite: on a
pole ray the unshifted order `d_(g,I_P(v))` is positive at every flag, while
at `F` it is zero.  The promoted Proposition 5.1 sidedness theorem then puts
`F_P^*` in `T_a^-`, not in `T_(a,pole)`.  This proves the omitted statement.

### 3.4 Proposition 7.2 first, then Statement 7.3

It is cleaner to prove Proposition 7.2 before Statement 7.3.

Let `P` be finite, put `b=g(P)` and `B=g-b`, and let `F_0=I_P(u_0)` be the
unique flag with `d_(A,F_0)=0`.  The corrected threshold `F_P^*` is in
`T_a^-`, so it lies strictly above `F_0`.  Therefore the centred defect is
still positive at `F_0`, and the leading bracket vanishes.  Write

```text
A_(F_0)^+ = p(eta),       B_(F_0)^+ = xi^e q(eta).
```

The residual `p` is nonconstant because the actual fibre branch supplies a
root.  The zero-bracket equation is

```text
0*p*q' - e*p'*q = 0.
```

Characteristic zero, `p' != 0`, and `q != 0` force `e=0`.  If `b!=0`,
adding `b` makes the leading order of `g` still zero; if `b=0`, it is already
zero.  Hence `F_0 in T_(a,cv)`.

Conversely, a ray containing a critical-value flag cannot be a pole ray by
Statement 7.2.  Thus

```text
g(P) in C  iff  the ray of P contains a critical-value flag.       (7.2-r)
```

Uniqueness follows from the unique zero of `d_(f-a)`.  This also repairs
Notation 7.2:

```text
Fhat_P := the unique element of T_(a,cv) on the ray of P.
```

For Statement 7.3, first observe that every positive flag on a pole ray is
`T_a^searrow`.  The pole threshold is searrow because, with type
`alpha<beta`,

```text
d_g/d_A = beta/alpha,
d_A+d_g = 1-u,
```

and therefore `d_A/(1-u)=alpha/(alpha+beta)<1<=deg p_A`.  An earlier
nearrow flag would remain nearrow up to the threshold by Proposition 6.6,
a contradiction.  Above the threshold, while `d_A>0`, the identity
`d_A+d_g+u-1=0` and `d_g>0` again give the searrow inequality.  Hence a ray
containing any nearrow flag is finite.  Apply (7.2-r) to obtain its unique
critical-value flag.  This proves the source's unproved Statement 7.3.

## 4. Proposition 7.1

Use the translated positive tower at `G=F^circ`:

```text
A=f-a,
h_0=g,
h_(j+1)=h_j^(k_j)-s_j*A^(l_j).
```

The repaired Proposition 4.2 permits `l_j=0` only for its one terminal
constant-shift step.  Put

```text
p=p_(A,F), q=p_(g,F),
r_0=q,
r_(j+1)=r_j^(k_j)-s_j*p^(l_j).
```

Then the correct claim is

```text
deg r_j = (l_j/k_j) deg p,       0<=j<=m-1.             (7.1-r)
```

The source says this is equivalent to `d_(h_j,G)=0`.  That is the wrong
flag: it is equivalent to `d_(h_j,F)=0`.

First, `G in T_a^+`, since `F` is the zero of `d_A` and `G` is its lower
edge endpoint.  Let `H=I_P(w)` lie strictly between `G` and `F`.  It is
positive.  It cannot be searrow:

- if `deg p_H=1`, repaired Lemma 6.1 makes `H` a positive nonzero-bracket
  pole threshold;
- if `deg p_H>1`, repaired Proposition 6.8 manufactures a pole on a branch
  through `H`.

There is no tree vertex between `H` and `F`, so in either case that pole
branch also passes through `F`, contradicting Statement 7.2 / the positivity
of `d_g` on pole rays.  Thus `H` is nearrow.

Proposition 6.3, applied along a common refined grid, says that every
preterminal tower relation at `G` persists at `H`.  Consequently

```text
k_j d_(h_j,H) = l_j d_(A,H),
k_j deg p_(h_j,H) = l_j deg p_(A,H).
```

On the open edge from `G` to `F`,

```text
d_(A,H) = deg p_(A,H) * (pi(F)-w),
```

not the source's `deg p_H*(w-pi(F))`.  Hence

```text
d_(h_j,H) = deg p_(h_j,H) * (pi(F)-w) >= 0.
```

Letting `w` increase to `pi(F)` and using continuity and bounded residual
degree gives `d_(h_j,F)=0`.  The residual recursion at `F` identifies
`r_j=p_(h_j,F)`, proving (7.1-r).  If a constant corner occurs, both sides
of (7.1-r) are zero because `l_j=0`; the repaired proposition therefore
covers exactly the case omitted by the printed `l_j in N*` version.

The printed proof has three exact corrections:

```text
d_(h_j,G)=0                       -> d_(h_j,F)=0,
d_H=deg(p_H)(w-pi(F))             -> d_H=deg(p_H)(pi(F)-w),
d_(h_j,H)=deg(p_(h_j,H))(w-pi(F)) -> same with pi(F)-w.
```

## 5. Proposition 7.3

### 5.1 Correct statement under centred notation

Let `F in T_(a,cv)`, `u=pi(F)`, `p=p_(f-a,F)`, and `q=p_(g,F)`.  Let `c`
be a realizable direction, so `F* c` exists.  Then `p(c)=0`.  Define the
direction cluster

```text
R^*_(F,c)
 := {P in Rbar_a\R_a : I_P(u+1/kappa)=F*c}.
```

It is independent of the sufficiently divisible suitable `kappa`: it is the
set of ends with the fixed truncation below `u` and coefficient `c` at
height `u`.  Every `P` in it is finite and

```text
g(P)=q(c).
```

Put `b_F=kappa_F(u-1)`.  Then

```text
L_(F,c):=sum_(P in R^*_(F,c)) Lambda(P) >= b_F.          (7.3a)
```

If `mult(p,c)=1`, then `R^*_(F,c)={P}` and

```text
Lambda(P)=b_F.                                           (7.3b)
```

In the source's bare notation these are `P_F(c)=a` and
`mult(P_F-a,c)=1`.

### 5.2 Simple direction: exact repaired proof

Let `R^*_(F,c)={P}`, put `b=q(c)=g(P)`, and write
`E=F_P^*=I_P(v)`.  Sidedness puts `E in T_a^-` and `v>u`.  For every
`H=I_P(w)`, `u<w<v`:

- `H in T_a^-`;
- the centred leading bracket of `(A,B)=(f-a,g-b)` vanishes;
- `deg p_(A,H)=1`.

The zero-bracket relation on the negative side has the form

```text
B_H^+ = s (A_H^+)^k,       k in N*, s in C*.             (5.1)
```

This follows directly from Proposition 4.3: if the primitive relation were
`(B_H^+)^K=s(A_H^+)^L`, residual degrees and `deg p_A=1` force `K=1`.
The integer `k` is the negative-tower exponent.  When `q-q(c)` is
nonzero it equals `ord_c(q-q(c))`; if `q` is constant at the critical flag,
it is determined by the first lower term of `g-b`.

This corrects a real source error.  The printed `k=mult(q,c)` is zero
whenever `q(c)=b!=0` under Notation 3.12, and is meaningless when `q` is
constant.  The source also writes the right leading form at `F` rather than
at `H` and drops the scalar `s`.

Continuity carries `d_(B,E)=k d_(A,E)`.  Since the direction is simple,
`deg p_A=1` all the way from just above `F` to `E`; no characteristic vertex
can intervene, so `kappa_E=kappa_F`.  The slope and terminal equations are

```text
d_(A,E)=u-v,
1-v=d_(A,E)+d_(B,E)=(k+1)(u-v).
```

Thus `kv=(k+1)u-1`, `d_(B,E)=-(u-1)`, and corrected Statement 3.15 gives

```text
Lambda(P)=-kappa_F d_(B,E)=kappa_F(u-1).
```

This proves (7.3b), including the constant-`q` case missed by the print.

### 5.3 General direction: a proper local-degree proof

Resolve the graph of `(f,g)` so that `f` and `g` extend to morphisms on a
smooth compactification.  The direction `(F,c)` is a point of a rational
boundary component.  Choose a sufficiently small analytic neighbourhood
`U` of that point and a disc `B(q(c),epsilon)` such that no other boundary
cluster enters `U` and the `g`-circle is avoided by the boundary of `U`.
For `a'` near `a`,

```text
g : U intersect Rbar_(a') -> B(q(c),epsilon)
```

is a proper finite map of constant total degree

```text
L_(F,c)=sum_(P in R^*_(F,c)) Lambda(P).
```

This is conservation of local intersection number / degree in a proper
one-parameter family.  For generic nearby `a'`, the root cluster of the
first-coordinate boundary polynomial splits into simple directions.  Pick
one such boundary point `Q` in `U`.  The simple case gives local degree
`Lambda(Q)=b_F`; a local degree cannot exceed the total degree of the finite
map, so `L_(F,c)>=b_F`.

This supplies the rigorous version of the printed geometric paragraph.
That paragraph needs all of the following corrections:

- isolate the zero of `P_F-a`, not the zero of bare `P_F`;
- for the fibre `a'`, the squarefree polynomial is `P_F-a'`, not `p_G`
  itself;
- `A` must be taken in a compactification/resolved graph, since the
  punctures are not points of affine `g^(-1)(B)`;
- `A_(a')` means `A intersect Rbar_(a')`, not the printed malformed
  `A intersect R_a^*`;
- the constant preimage count is in `A_(a')`, not “in `B(a,delta)`”;
- choose a generic `a'`, rather than first choosing any `a'` and later
  assuming squarefreeness.

### 5.4 Statement 3.14: what transports and what does not

The source writes exact equalities `p_G=p_F` and `p_(g,G)=p_(g,F)`.  Under
the audited Section 3 repair, the residual coordinate may change by
`eta -> zeta eta`.  Also, with centred notation,

```text
p_(f-a',G)(eta)
  = p_(f-a,F)(zeta eta) + (a-a').                        (5.2)
```

The `g`-pattern is precomposed by the same twist.  Exact named-root alignment
is therefore unavailable.  It is also unnecessary: (5.2) preserves height,
residual degrees, root multiplicities, local clusters and `g`-values after
the corresponding coordinate change.  The jump/max `kappa_F` is preserved
because the rooted contact tree and all characteristic jump multiplicities
are preserved; equivalently it is the locally constant ramification index
of the boundary component in the resolved family.  Hence `b_F` is constant
under transport.

This closes the Proposition 7.3 use of Statement 3.14 without assuming the
unproved exact `eta` alignment.

## 6. Why the per-puncture strengthening is false

The most tempting attempt to save literal Notation 7.3 is to split the
nearby generic direction once for each original puncture and add the simple
local degrees.  That addition is invalid: the generic points can lie over
different values of `g`, and the original normalized branches need not have
separate persistent neighbourhoods in the total surface.

Here is the smallest exact local model.  In a boundary chart put

```text
s=y^(-1),       t=x y^3,
x=t s^3,        y=s^(-1).
```

Then

```text
dx wedge dy = s ds wedge dt.
```

Define, on a bidisc about `(s,t)=(0,0)`,

```text
g=t,            f=t^2+s^2/2.
```

Since

```text
df wedge dg = (2t dt+s ds) wedge dt = s ds wedge dt,
```

the local Jacobian is exactly one.  At the height-`3` flag,

```text
p_F=t^2, q_F=t, d_f=d_g=0, pi(F)=3, kappa_F=1,
b_F=kappa_F(pi(F)-1)=2.
```

On the special fibre `f=0`,

```text
s^2=-2t^2
```

has two normalized branches.  On each, `z=t` is a uniformizer,
`y~Cz^(-1)`, `x~C'z^4`; their contact is `4>3`, so both belong to the one
direction cluster `R^*_(F,0)`.  On each branch `g=z`, hence

```text
Lambda(P_+)=Lambda(P_-)=1,
sum_(P in R^*) Lambda(P)=2=b_F.                           (6.1)
```

For small generic `a!=0`, the two simple directions are
`t=+sqrt(a)` and `t=-sqrt(a)`.  Each has local `g`-degree two, exactly the
simple-direction baseline, but their `g`-values are `+sqrt(a)` and
`-sqrt(a)`.  The cover of the `g`-disc has degree two, not four.  At
`a=0`, the two normalized punctures map to the same point of the already
normal total surface `(s,t)`; there are no two disjoint total-space
components that persist under deformation.

Thus Proposition 7.3 gives exactly (6.1), while literal Notation 7.3 assigns
this cluster

```text
(1-2)+(1-2)=-2.                                          (6.2)
```

The value curve `t -> (t^2,t)` is even an embedded copy of `C`, so neither
curve self-intersection nor a nonprimitive parametrization causes the
failure.  The error is exactly “one baseline per puncture” versus “one
baseline per direction parameter.”

This is a local analytic Keller germ, not a global polynomial Keller pair.
It therefore does not disprove a theorem quantified only over global
polynomial pairs (no nonautomorphic global examples are known).  It does
decisively refute the printed local-deformation inference and every proposed
one-neighbourhood-per-special-puncture repair.

## 7. Corrected Notation 7.3 and Proposition 7.4

For fixed `a`, let `C_a` be the finite set of realizable direction clusters

```text
C=(F,[c]),
F in T_(a,cv),
p_(f-a,F)(c)=0,
F*c exists.
```

The bracket `[c]` reminds us that cyclically conjugate coefficients describe
one geometric direction; equivalently use the affine residual direction
line on the boundary component.  Let

```text
R_C := R^*_(F,c),
r_C := #R_C,
L_C := sum_(P in R_C) Lambda(P),
b_C := kappa_F(pi(F)-1).
```

Proposition 7.2 partitions all finite punctures uniquely into these clusters.
The corrected definition is

```text
delta_a^cl := sum_(C in C_a) (L_C-b_C).                  (7.1)
```

Proposition 7.3 immediately gives

```text
delta_a^cl >= 0.
```

For generic `a`, every relevant first-coordinate direction is simple, so
each `R_C` is a singleton and Proposition 7.3 gives equality term by term:

```text
delta_a^cl=0 for generic a.                              (7.2)
```

This is the rigorous Proposition 7.4.

The literal source quantity is

```text
delta_a^lit
  = sum_(P finite puncture) [Lambda(P)-b_(Fhat_P)]
  = sum_(C in C_a) (L_C-r_C b_C).                        (7.3)
```

Therefore

```text
delta_a^cl
  = delta_a^lit + S_a,
S_a := sum_(C in C_a) (r_C-1)b_C >= 0.                  (7.4)
```

The splitting term `S_a` is zero generically but need not vanish at a
collision fibre.  Formula (7.4) is the exact way to repair the ledger without
silently changing its totals.

## 8. Proposition 7.5: repaired Euler proof

### 8.1 Fibre deficit

Let `d=td(f,g)` and

```text
N(a,b):=#(f,g)^(-1)(a,b).
```

The Keller condition makes every affine preimage simple.  Repaired
Proposition 5.8 says that the meromorphic degree of `g` on every normalized
fibre `Rbar_a` is `d`.  The divisor of `g-b` on `Rbar_a` therefore gives the
exact pointwise identity

```text
d-N(a,b)
  = sum_(P in Rbar_a\R_a, g(P)=b) Lambda(P).             (8.1)
```

This is the bridge between puncture local degrees and the global topological
degree.  No genericity in `a` is used.

### 8.2 Direction lines and multiplicity pushforward

Fix `a_0` and enumerate `T_(a0,cv)={F_1,...,F_s}`.  Each `F_i` determines
an affine residual direction line `E_i ~= A^1` on the resolved boundary and
a polynomial value map

```text
phi_i:E_i -> C^2,
c |-> (P_i(c),q_i(c)),                                   (8.2)
```

read in the cyclic quotient coordinate when necessary.  Statement 3.14,
with the common root-of-unity twist retained, and Proposition 7.2 identify
the fibres of these maps with all finite-puncture direction clusters in all
fibres of `f`.  Put `b_i=kappa_(F_i)(pi(F_i)-1)`.

The source replaces the multiplicity of `phi_i^(-1)(a,b)` by the boolean
relation `a ->_i b` and asserts that the image of `phi_i` is biholomorphic to
`C`.  Neither step is justified.  Polynomial parametrized curves can be
singular or self-intersecting, and different parameter values must be
counted additively at a common target.  The correct baseline constructible
function is

```text
B(a,b):=sum_i b_i * #phi_i^(-1)(a,b),                    (8.3)
```

counting distinct points of the direction normalization.  Different parameter
points are additive; ramification at one parameter point is not a second
baseline.  Injectivity is not needed.

By (8.1) and the cluster partition,

```text
d-N(a,b)=B(a,b)+E(a,b),                                  (8.4)
```

where `E(a,b)` is the sum of `L_C-b_C` over clusters with value `(a,b)`.
It is nonnegative, and

```text
sum_b E(a,b)=delta_a^cl.                                 (8.5)
```

Only finitely many `b` contribute for fixed `a`; equations (8.3)--(8.5),
not an ordinary infinite sum of constants, are the precise meaning of the
source's displayed `sum_(b in C)`.

### 8.3 Euler integration

Because `(f,g)` is etale and quasi-finite, `N` is a finite constructible
function.  Euler-Fubini gives

```text
1=chi_c(C^2)=integral_(C^2) N dchi_c,
d-1=integral_(C^2) (d-N) dchi_c.                         (8.6)
```

For every `i`, functoriality of constructible pushforward gives

```text
integral_(C^2) #phi_i^(-1)(z) dchi_c(z)
  = chi_c(E_i)=chi_c(A^1)=1.                             (8.7)
```

This remains true if the value curve is singular, self-intersecting, or
shared with another `F_j`.  Integrating (8.4), using (8.5)--(8.7), yields

```text
d-1=sum_i b_i + sum_(a in C) delta_a^cl,
```

which is (22-cl).

If one insists on literal Notation 7.3, substitute (7.4):

```text
d
 =1+sum_i b_i
   +sum_a delta_a^lit
   +sum_a S_a.                                           (22-lit-corrected)
```

The printed equation (22) omits `sum_a S_a`.

There is also an independent sign typo on printed p. 39.  The source writes

```text
1 = td - sum_i b_i + sum_a delta_(F_i,a)
```

and calls this equivalent to (22).  The sign before the delta sum must be
minus:

```text
1 = td - sum_i b_i - sum_a delta_a^cl.
```

The subscript `delta_(F_i,a)` is itself undefined; the statement uses
`delta_a`.

### 8.4 Corollary 7.1

Complete a chosen subset `{F_1,...,F_n}` of `T_(a,cv)` to the full set.
Every omitted baseline is positive by Statement 7.1, and every
`delta_a^cl` is nonnegative.  Equation (22-cl) gives

```text
td(f,g) >= 1 + sum_(i=1)^n kappa_(F_i)(pi(F_i)-1).
```

Thus Corollary 7.1 is a repaired theorem even though its printed proof runs
through the malformed Notation 7.3.

## 9. Dependency and blast-radius map

### 9.1 What survives unchanged

The later `lambda` budgets count **critical-value vertices**, not normalized
punctures:

```text
lambda_F=sum_(H in Y(F)) kappa_H(pi(H)-1).
```

That is exactly the one-baseline-per-vertex/direction-family accounting of
(22-cl).  Consequently the following campaign conclusions survive:

- Statement 9.3's height price for each distinct nearrow direction and its
  use of repaired Statement 7.3;
- Statement 9.4 and Statement 9.5, via repaired Corollary 7.1;
- all AF2/A2P `lambda` additions, which explicitly prove the relevant
  critical-value vertices are distinct;
- the `psi` charge on the x-side;
- the single-/multi-pole book budgets and their `td-1` or `td-2` caps;
- LROOT's count of one charge per cv vertex and the conclusion that the
  eight-class book receives no new root charge;
- the D73 conclusion that direction multiplicity alone does not force a
  strict **cluster** excess.

The campaign files consumed here had these hashes:

```text
9ff5d00567d7b6752ecc79892bb41959a450ddff3837bdb26179899ad2dfad5a  ladder/SHEET6-LROOT.md
82d94e1a43ae9ec315189b4892faafa840027f4f1696dba6a394866331aa22c6  ladder/SHEET6-LT-REVIEW.md
086a475927b5cdec68dcdffc836bf06c0418616113aa3ccc91bc98d9eafb1678  ladder/SHEET6-CAMPAIGN.md
905988471cf1458b5be949b7dfa2636f8e6b29a114cb7c2f1e30df11deb18d34  ladder/SHEET6-AF2.md
cf84555a61c9e69a33dc6abe67bbe5d79463d4deb15a1fb31743d13b3134a61e  ladder/SHEET6-A2P-REVIEW.md
78215e1ff847f10ee4df26615443f56ab49c9e21366137898c0742525d78decc  ladder/SHEET6-MULTIPOLE.md
dd3eee2f98e7757ab375a4ae243da256941c15e06a9e762e958cc647c70d52a9  ladder/REDUCTION.md
```

### 9.2 What must be weakened or reworded

The following current campaign wording is too strong:

- “`delta_a` is the per-puncture Lambda excess”;
- “Proposition 7.4 proves every puncture contributes a nonnegative excess”;
- “slack zero implies `Lambda(P)=kappa_F(pi(F)-1)` for every finite
  puncture.”

The correct implications are:

```text
delta_a^cl is a sum of nonnegative cluster excesses;

sum_a delta_a^cl=0
  => every direction cluster has
     sum_(P in R_C) Lambda(P)=kappa_F(pi(F)-1).
```

A split cluster can have several punctures of smaller individual
multiplicity, as Section 6 shows.  Even one puncture larger than the baseline
could in principle be balanced inside its cluster by other positive but
smaller punctures; Section 7 gives no puncturewise conclusion.

For the four LROOT slack-zero classes, `delta_a^cl=0` for every `a` still
follows from the global equality and nonnegativity.  Their live strictness
surface remains exactly the one already tested: force
`L_C>b_C` for some collision cluster.  The local D73 control
(`90546ffb...`, reviewed at `3c0df200...`) shows that multiplicity alone does
not do so.  Only the phrase “individual puncture nondegeneracy” must be
withdrawn.

### 9.3 Proposition 8.4 root case: explicit no

Nothing in Section 7 rules out or prices a singleton-pole configuration with
`M_(0,y)=1`.

- `M_F` does not occur in Notation/Statements/Propositions 7.1--7.5.
- All Section 7 charges lie at `H in T_(a,cv) subset T_a^0`.
- `(0,y)` has `pi=0` and `d_(f-a,(0,y))=l_f>0`; it is not a cv vertex.
- Statements 7.2 and Proposition 7.2 distinguish pole rays from finite-value
  rays, but do not turn an `M=1` root into a finite puncture or a cv vertex.
- Equation (22-cl) permits an empty root row; it charges only actual cv
  families and their cluster excesses.

Therefore the answer is **NO even under the singleton-pole hypothesis**.
Excluding the root `M=1` case requires a new theorem connecting the root gcd
to a finite-value direction/cv family, or a repaired root-inclusive
Proposition 8.4.  It cannot be recovered from Section 7.

## 10. Exact filing list

Recommended Section 7 errata/gap entries:

1. **S7-E1, Proposition 7.1, p. 36:** replace the goal
   `d_(h_j,G)=0` by `d_(h_j,F)=0`; reverse both occurrences of
   `w-pi(F)`; allow the repaired terminal `l_j=0` corner.
2. **S7-E2, Proposition 7.3, pp. 36--37:** under centred notation replace
   `p(c)=a` by `p(c)=0` and `mult(p_F-a,c)` by `mult(p,c)`; in bare notation
   retain the source formulas.  Replace `k=mult(q,c)` by the negative-tower
   exponent, equal to `ord_c(q-q(c))` only when that leading polynomial is
   nonzero after centring.  Replace the `F` leading form in the negative
   segment by `H` and retain its scalar.
3. **S7-G1, Proposition 7.3 deformation, pp. 37--38:** use a proper tube in
   a resolved compactification; replace exact Statement 3.14 alignment by a
   common root-of-unity twist; squarefree means `P_F-a'`; repair the malformed
   `A_(a')` and preimage-domain sentences.
4. **S7-E3, Notation 7.3, p. 38:** replace per-puncture subtraction by
   (7.1), or retain it and add the splitting term (7.4) everywhere.
5. **S7-G2, Proposition 7.4, p. 38:** no proof is printed; it is true for
   `delta^cl`, not obtained for literal `delta^lit`.
6. **S7-G3, Proposition 7.5, pp. 38--39:** replace boolean curve membership
   by multiplicity pushforward from the direction normalization line; delete
   the unsupported “biholomorphic with C” requirement; use Euler-Fubini.
7. **S7-E4, Proposition 7.5, p. 39:** change the final `+sum delta` to
   `-sum delta`, and `delta_(F_i,a)` to `delta_a` (or `delta_a^cl`).
8. **S7-G4, omitted proofs:** Statements 7.2, 7.3 and Proposition 7.2 need
   the proofs in Section 3 above; Notation 7.2 needs uniqueness.

## 11. Final verdicts

### Source

**SECTION 7 AS PRINTED: NOT VALIDATED.**  The earliest omitted proof is on
p. 35; the first proof-level false identities are on p. 36; the Euler ledger
becomes statement-level inconsistent at Notation 7.3 on p. 38.  Literal
Propositions 7.4--7.5 do not follow from Proposition 7.3.

### Repaired mathematics

**REPAIRED SECTION 7: PROVED AT THE CLUSTER/EULER LEVEL**, conditional only
on the already promoted corrected Sections 3--6 package and every-fibre
Proposition 5.8 listed in Section 1.  The repaired package includes
Statements 7.1--7.3, Propositions 7.1--7.3, cluster Proposition 7.4,
equation (22-cl), and Corollary 7.1.

### Campaign

**BOOK/BUDGET BLAST RADIUS: NO CLASS COUNT CHANGES.**  Corollary 7.1,
`lambda`, `psi`, and the global cv-vertex ledger survive.  Replace every
per-puncture interpretation of `delta` by the cluster interpretation.  The
root `M=1` gap is untouched and remains a genuine independent obligation.
