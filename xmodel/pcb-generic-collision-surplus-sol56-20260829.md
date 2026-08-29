# PCB on a generic fibre: quotient-collision surplus and a degree-six zero-excess control

Author: Sol 5.6 proof-side lane  
Date: 2026-08-29 UTC  
Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`  
Lifecycle: `PRIMARY EXACT REFORMULATION / PROPOSED ATYPICAL BRIDGE REFUTED AT DEPENDENCY SCOPE / REVIEW REQUIRED`

## 0. Verdict

The reviewed Section-7 quotient package gives a sharper exact formulation of
the proposed `PCB-EXCESS` bridge than the current integral notation exposes.
It also fixes the direction of the proposed atypical-value argument.

Let

```text
U_i=A1_z,                phi_i=(P_i,Q_i),
d_i=deg(P_i),            b_i=kappa_i^+(u_i-1),
I_i=integral_(U_i) w_i dchi_c.
```

For a generic fibre of `f`, write `G` for the compactification genus, `s`
for the number of pole ends of `g`, and `n` for the number of finite-value
ends.  Then the following identities are exact:

```text
n = sum_i d_i,
E_gen := sum_i (I_i-b_i)
       = sum_i b_i(d_i-1) + chi_gen - 1
       = sum_i b_i(d_i-1) + 1 - 2G - s - n.
```

Consequently generic-fibre `PCB-EXCESS`, namely `E_gen>=s-1`, is equivalent
to the single integer inequality

```text
sum_i b_i(d_i-1) >= 2G + 2s + n - 2.                 (QCS)
```

Equivalently, if `delta(f)=1-chi_gen=2G+s+n-1` is Suzuki's total infinity
defect,

```text
sum_i b_i(d_i-1) - delta(f) >= s-1.                  (QCS')
```

Thus the correctly typed missing theorem is a **quotient-collision surplus**
of `s-1`, not “one weight unit at an atypical value.”  The collision term
uses ramification of the first-coordinate maps `P_i`; the excess term uses
actual local `g`-degrees `w_i`.  No pole place is identified with a flag,
quotient point, or Puiseux series.

More precisely, for every fibre value `a`, if

```text
q_i(a)=# distinct roots of P_i(z)=a,
epsilon(a)=sum_i sum_(P_i(z)=a) (w_i(z)-b_i),
```

then

```text
chi(f^-1(a))-chi_gen
  = sum_i b_i(d_i-q_i(a)) - epsilon(a).               (FC)
```

An atypical Euler jump is therefore a collision deficit **minus** weight
excess.  It can be positive with `epsilon(a)=0`.  Hence

```text
ATYPICAL-EXISTENCE  does not imply  EXCESS-1
```

from the reviewed Section-7, Suzuki, fibre-cover, or local Jacobian-one
inputs.  The proposed `WEIGHT-AT-ATYPICAL` route stops unless one proves a
new global-polynomial strictness theorem.

A matched degree-six control makes this failure sharp at the first relevant
topological degree.  It has generic data

```text
d=6, G=1, s=2, n=2, one quotient line with (d_1,b_1)=(2,5),
delta(f)=5, collision capacity=5, E_gen=0,
```

so PCB would fail by one.  An exact Jacobian-one boundary germ realizes
`P=z^2`, `Q=z`, and constant weight `w=5`, including equality at the
collision; a transitive degree-six permutation triple realizes the matching
generic genus-one cover and its `5+1` collision split.  These are a matched
local/Hurwitz control, **not** one global polynomial pair and not a
counterexample to PCB or JC2.  They prove that any successful strictness
argument must use the common global polynomial `A2` filling or an equivalent
source-boundary constraint absent from the current inputs.

The cheapest next discriminator is therefore not a special-fibre weight
search.  On one source-complete generic-fibre packet, compute only

```text
Xi = sum_i b_i(d_i-1) - (2G+2s+n-2).
```

This is exactly the PCB margin.  The residue-A source is the smallest
nontrivial client, but the test must return `UNDERDETERMINED` if even one
quotient degree, flag baseline, genus, or end count is unfiled.

## 1. Licensed inputs and notation

The proof uses the following frozen, reviewed facts.

1. The actual-weight Section-7 repair and hostile review
   `c253bd12...` / `727f5850...` construct the quotient lines, actual
   weights, and exact deficit identity

   ```text
   d-N = sum_i (phi_i)_! w_i,
   d-1 = sum_i I_i,
   w_i(z)>=b_i,
   w_i(z)=b_i away from {0} union Crit(P_i).
   ```

   Here `b_i=kappa_i^+(u_i-1)` is the generic high baseline.  This does not
   transport the actual jump/max decoration across fibres.

2. The resolution-free quotient construction `aec8bd7e...`, with the
   final delta gate `758c0226...`, proves that `P_i` is a nonconstant
   polynomial and that the disjoint union of the `U_i` parametrizes exactly
   the finite-value direction clusters, with no cyclic or cross-flag
   duplication.  Only its fixed-`kappa` conclusion failed; the actual-weight
   repair is used here instead.

3. The reviewed Suzuki packet `b96a656...` / `57e6d4a1...` proves that a
   polynomial Keller coordinate `f` is primitive, its generic fibre is
   connected, and

   ```text
   sum_a [chi(f^-1(a))-chi_gen]
     = 1-chi_gen
     = 2G+(s+n)-1.
   ```

   A nonautomorphic pair has positive total defect.  This is the already
   known `ATYPICAL-EXISTENCE` half.

4. The exact local equality control `90546ffb...`, independently reviewed
   at `3c0df200...`, shows that a multiple root of `P_i-a` can retain
   `w_i=b_i` in an exact Jacobian-one boundary germ.  The degree-six control
   below is its specialization `(R,L,q)=(6,2,t)`.

Throughout, `d=td(f,g)`.  On a generic fibre, `s` counts physical pole
places, `n` counts physical finite-value places, `i` indexes proper
critical-value flags/quotient lines, and `z` indexes direction clusters.
These sets are never identified.

## 2. Fixed-fibre collision identity

Let `R_a=f^-1(a)` and put `chi_a=chi_c(R_a)`.  Integrate the exact pointwise
deficit over the second target coordinate:

```text
integral_(b in A1) [d-N(a,b)] dchi_c
  = d-chi_a.
```

On the quotient side, finite pushforward and Euler-Fubini give

```text
d-chi_a
  = sum_i sum_(z in P_i^-1(a)) w_i(z),                 (2.1)
```

where roots are distinct geometric points; ramification multiplicity is not
inserted.  Collisions of `Q_i`-values cause no problem because the source
points remain additive in the pushforward.

Choose `a_gen` outside the finite union of all critical values of `P_i`, all
`P_i(0)`, and all exceptional-weight images.  Then `P_i^-1(a_gen)` has
`d_i` nonzero simple roots and every corresponding cluster is a singleton
of weight `b_i`.  Hence

```text
d-chi_gen = sum_i d_i b_i.                             (2.2)
```

For arbitrary `a`, define

```text
q_i(a)    = #P_i^-1(a),
epsilon(a)= sum_i sum_(P_i(z)=a) [w_i(z)-b_i] >= 0.
```

Equation (2.1) becomes

```text
d-chi_a = sum_i q_i(a)b_i + epsilon(a).
```

Subtracting from (2.2) proves `(FC)`:

```text
chi_a-chi_gen
  = sum_i b_i[d_i-q_i(a)] - epsilon(a).                (2.3)
```

This is the exact sign.  A collision raises the fibre Euler characteristic;
actual weight excess offsets that jump.  Atypicality by itself gives no
positive lower bound on `epsilon(a)`.

## 3. Sum over values and the generic PCB criterion

For a degree-`d_i` polynomial, the sum of the distinct-root deficits is

```text
sum_a [d_i-q_i(a)] = d_i-1.                            (3.1)
```

This is the finite ramification divisor of `P_i:A1->A1`, or equivalently
the total multiplicity of `P_i'`.

Because `w_i=b_i` off a finite set and `chi_c(A1)=1`,

```text
I_i-b_i = sum_(z in A1) [w_i(z)-b_i].                  (3.2)
```

Grouping the right side by `a=P_i(z)` gives

```text
sum_a epsilon(a)=sum_i(I_i-b_i)=E_gen.                 (3.3)
```

Summing (2.3), using (3.1)--(3.3) and Suzuki's exact total defect, yields

```text
1-chi_gen
  = sum_i b_i(d_i-1)-E_gen,

E_gen
  = sum_i b_i(d_i-1)+chi_gen-1.                        (3.4)
```

This also independently follows by subtracting `sum_i b_i` from
`d-1=sum_i I_i` and using (2.2).

On the chosen generic fibre the actual flag weight is `wt_i(a_gen)=b_i`.
Every simple direction cluster contains one finite place, so

```text
n=sum_i d_i,             chi_gen=2-2G-s-n.             (3.5)
```

Substituting (3.5) in (3.4) proves

```text
E_gen-(s-1)
  = sum_i b_i(d_i-1) - (2G+2s+n-2).                   (3.6)
```

The right side is the announced margin `Xi`.  Thus `(QCS)` is not a
heuristic sufficient condition: it is exactly generic-fibre PCB.

There is also a useful local decomposition.  Put

```text
C(a)=sum_i b_i[d_i-q_i(a)],
J(a)=chi_a-chi_gen.
```

Then (2.3) says

```text
C(a)-J(a)=epsilon(a)>=0,
sum_a C(a)=sum_i b_i(d_i-1),
sum_a J(a)=delta(f),
sum_a epsilon(a)=E_gen.                                (3.7)
```

Therefore `EXCESS-1` is equivalent to strict inequality at at least one
value in (3.7).  Merely proving that some `J(a)>0` proves no strictness.

## 4. Exact degree-six zero-excess controls

### 4.1 Jacobian-one boundary chart

Use

```text
s=y^-1,             t=x y^6,
x=t s^6,            y=s^-1,
g=t,                f=t^2+s^5/5.
```

Then

```text
dx wedge dy = s^4 ds wedge dt = df wedge dg,
```

so the local Jacobian is exactly one.  On the boundary `s=0`,

```text
P(z)=z^2,       Q(z)=z,       b=kappa(6-1)=5.
```

For `a!=0`, the two simple roots `z=+-sqrt(a)` give distinct `g`-values.
Solving `f=a` near either root gives

```text
t-z = nonzero_constant*s^5 + O(s^10),
```

so each direction has local `g`-degree five.  On `a=0`,

```text
t^2=-s^5/5.
```

Since `gcd(2,5)=1`, its normalization has one branch and `ord(g)=5`.
Thus the collided cluster also has weight five:

```text
w(z)=5 for every z,       I=5,       I-b=0.            (4.1)
```

This is an algebraic boundary chart and exact Jacobian-one germ.  In the
original affine coordinates `f` contains `y^-5/5`; it is not a polynomial
Keller pair on `A2`.

### 4.2 Matching connected generic cover

On six letters, take the permutations

```text
sigma_+     = (1 2 3 4 5),
sigma_-     = (0 1 2 4 3),
sigma_infty = (0 3 1 5 2),
```

with composition ordered so that

```text
sigma_+ sigma_- sigma_infty = 1.
```

All three have cycle type `(5,1)`, and the generated group is transitive
because the two finite cycles have different fixed letters.  Their total
index is `4+4+4=12`; Riemann--Hurwitz gives genus one for the connected
degree-six cover.

Remove the two points over infinity, of pole orders `5` and `1`, and remove
the ramified five-cycle point over each of the two finite branch values.
The resulting affine curve has

```text
G=1,       s=2,       n=2,       chi_gen=-4,
```

and `g` is unramified on the affine part.  When the two finite branch values
coalesce, their product is `sigma_infty^-1`, again of type `(5,1)`.  The
two-branch monodromy then splits into a degree-five component and a
degree-one component.  Removing the finite five-cycle point and the poles
gives `G_m` on the degree-five component and `A1` on the degree-one
component, so

```text
chi_special=0+1=1,       chi_special-chi_gen=5.         (4.2)
```

This matches (2.3) exactly:

```text
collision deficit = b(d_1-q_1(0)) = 5(2-1)=5,
weight excess      = 0,
Euler jump         = 5.
```

It also matches Suzuki and the generic PCB margin:

```text
delta(f)=1-chi_gen=5,
sum b_i(d_i-1)=5,
E_gen=0,
Xi=5-(2+4+2-2)=-1.
```

Riemann existence licenses the connected generic curve cover.  The
collision calculation is a Hurwitz/admissible-cover control.  No common
algebraic surface family, embedding in `A2`, polynomial `f,g`, source
compactification, or Keller counterexample is claimed.  The point is the
dependency boundary: curve topology, transitive monodromy, Suzuki defect,
and exact local Jacobian-one collision equality do not force `EXCESS-1`.

## 5. Consequences for the campaign

1. **Stop the current atypical prove-route.**  `ATYPICAL-EXISTENCE` is
   classical and already reviewed.  The missing arrow is not a bookkeeping
   additivity lemma.  Equations (2.3) and (3.7) show that it is exactly a
   strict actual-weight theorem `epsilon(a)>0` at some value.  The reviewed
   local equality family and the degree-six control show that no argument
   confined to local Proposition 7.3, Riemann--Hurwitz, Suzuki defects, or
   fibre monodromy can supply it.

2. **Retain PCB only in the generic quotient-collision form.**  A possible
   global theorem is

   ```text
   QCS: for every nonproper polynomial Keller pair,
        sum_i b_i(deg P_i-1)-delta(f) >= s-1.
   ```

   This is correctly typed and exactly equivalent to generic PCB, not a new
   consequence of existing inputs.  A proof must use the common global
   polynomial source/boundary filling, or another invariant absent from the
   matched control.

3. **Do not infer a td12/U1 selector.**  Even a proof of QCS would first
   require a provenance-preserving generic-fibre landing before it could
   alter a reduced book budget.  The abstract `U1*(R)` records do not file
   `P_i`, `d_i`, `G`, or the full finite-end partition and cannot be plugged
   into (3.6).  Full QCS may exclude a landed U1 sector; it does not select
   td12, type `(2,3)`, or U1.

4. **The conditional budget bridge becomes precise.**  On an actual generic
   fibre, if the selected first-separation flags are a subset of the full
   quotient flag set, then `E_gen>=e` really lowers the shared Corollary-7.1
   ceiling by `e`, because

   ```text
   sum_(selected) b_i <= sum_(all) b_i = d-1-E_gen.
   ```

   This does not license subtraction on a formal pole/merge floor until the
   selected flags and generic-fibre provenance are constructed.

## 6. Cheapest decisive next experiment

Build one read-only `QCS-MARGIN/v1` packet for a source-complete generic
fibre.  Required inputs are exactly

```text
PairRef and generic fibre value/rider;
complete proper-cv flag set i;
for every i: descended P_i, d_i=deg P_i, and b_i=kappa_i^+(u_i-1);
G, s, and n, with n independently checked against sum_i d_i;
the map from every selected book exit flag to its quotient-line i.
```

Compute, using integers only,

```text
Xi = sum_i b_i(d_i-1)-(2G+2s+n-2).
```

Outcomes:

- `Xi<0`: PCB fails on that source packet.  Unless the packet is an actual
  polynomial Keller pair, this is a packet-level falsifier, not an actual
  counterexample.
- `Xi=0`: PCB is sharp on that packet; no strict-excess descendant is
  licensed.
- `Xi>0`: PCB holds on that packet with exact margin `Xi`; downstream
  budgets may consume it only after their flags are mapped injectively.
- missing/inconsistent input: `UNDERDETERMINED`, listing the first absent
  object.  Do not manufacture quotient degrees from reduced orbit counts.

The filed residue-A source is the first control because `d=6,s=2` is the
smallest nonvacuous pole count and the matched zero-excess control has the
same `(d,s)` values.  If its full generic quotient packet is not actually
filed, stop immediately; completing that packet is the mathematical task.
No CAS or AWS is needed for the margin once the source objects exist.

## Nonclaims

This report does not prove or refute PCB on actual nonproper Keller maps,
prove QCS, construct a polynomial map, select td12 or U1, land any book
record, lower a formal budget, or decide JC2.  The degree-six control is not
one global source object.  Its role is to prove that the current local,
curve, monodromy, and atypicality inputs permit zero excess and therefore
cannot prove the missing strictness by themselves.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15043`.
- Body SHA-256:
  `a2cf302ad66c01980e2e70c482ab0d9914b9b616525736d5735a9de7900a147f`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
