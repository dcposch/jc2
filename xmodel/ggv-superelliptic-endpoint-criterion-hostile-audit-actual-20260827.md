# Hostile audit: superelliptic endpoint criterion from Opus5 Card A

Date: 2026-08-27  
Auditor lane: `actual_total_g20`  
Target: `xmodel/ideation-20260827T1349Z-opus5.md`, section 3.2 and Card A  
Target SHA-256:
`1c17b61f00079802b20fc459550eea7bc7b09bcdcc98f27c233bde91cf348968`  
Status: **ENDPOINT THEOREM CONFIRMED WITH NARROW REPAIRS; GENERAL-H
MODE/PROVENANCE/GGV CONSEQUENCES REMAIN OPEN**

## 0. Executive verdict

The main new algebraic statement is correct.  Let `K` be a
characteristic-zero field, let `0 != H in K[X]`, and choose its squarefree
decomposition

```text
H=A^2 B,       A,B in K[X],       B squarefree.
```

Then the rational ODE

```text
2 H g' + H' g = 2 H                                      (0.1)
```

has a solution `g in K(X)` if and only if

```text
A is in im(N_B),       N_B(v)=Bv'+(3/2)B'v,  v in K[X].  (0.2)
```

This is a theorem about the **rational endpoint**.  It gives a genuine,
degree-uniform decision procedure and the sufficient exclusion
`deg(A)<deg(B)-1` when `deg(B)>=1`.

Four presentation repairs are required.

1. In the passage from `M(Y)=1` to (0.1), the normalized variable is
   `g=4HY`, not the earlier `g=HY`.  This is only a factor-of-four repair and
   does not change solvability.
2. The reduced denominator of a solution **divides** the displayed common
   denominator `A0`; it need not equal it.
3. `N_B` is injective only when `deg(B)>=1`.  For constant `B`, its kernel is
   the constants and its image is all of `K[X]`.
4. The superelliptic reformulation must use the normalized connected Kummer
   component and the appropriate character eigenspace.  The literal cover
   written in Opus5 can be reducible; in the charged case its minimal cover is
   `w^2=H`, not the unreduced equation `u^8=H^4`.

The smallest counterexample to both subsidiary overstatements is already
`H=X^2`: take `A=X`, `B=1`.  Then `N_1(1)=0`, so `N_1` is not injective, while
`g=X/2` solves (0.1) and has reduced denominator `1`, not `A0=X`.  This is
**not** a counterexample to (0.2).

The following stronger claims are not established by the endpoint theorem:
general-`H` homogeneous-mode completeness, denominator provenance from raw
polynomial jets, a raw `2S/3S` lift, landing a genuine GGV chain in this
endpoint, a GGV-family exclusion, `G2-PSC`, `G2-BD`, or JC2.

## 1. Verdict table

| Charged item | Verdict |
|---|---|
| R3 endpoint coefficient | **CONFIRMED** |
| Change of variable to (0.1) | **CONFIRMED**, with factor-of-four notation repair |
| Integrating-factor identity | **CONFIRMED** |
| `H=X^8-1` de Rham obstruction | **CONFIRMED** |
| General `H=A^2B` criterion (0.2) | **CONFIRMED** |
| Finite-pole classification for `g` | **CONFIRMED**: any pole is at an even-multiplicity root and has half that order |
| “denominator exactly `A0`” | **REFUTED / REPAIR**: reduced denominator divides `A0` |
| Rational degree `deg(g)=1` | **CONFIRMED**, but the stated nonvanishing argument needs a resonance repair |
| `N_B` injective | **CONFIRMED for `deg B>=1`; REFUTED for constant `B`** |
| `deg N_B(v)=deg v+deg B-1` | **CONFIRMED for `deg B>=1`, `v!=0`; constant-`B` exception required** |
| Codimension `deg B-1` | **CONFIRMED for `deg B>=1`; codimension is `0`, not `-1`, for constant `B`** |
| `deg A<deg B-1` exclusion | **CONFIRMED** |
| Listed endpoint examples | **CONFIRMED**, with scope note for `H=X^16-1` |
| General `(alpha,beta,N)` algebra | **CONFIRMED** |
| Naive “exact on `u^beta=...`” wording | **REPAIR**: normalize/reduce the cover and retain the Kummer character |
| General-`H` mode completeness | **OPEN** |
| Raw polynomial provenance | **OPEN** |
| GGV landing/cofinal family exclusion | **OPEN** |

## 2. Independent derivation of the charged endpoint

Use the face operator

```text
E(F,G)=12 F_X G-8 F G_X-t(F_X G_t-F_t G_X).
```

After the reviewed R3 homogeneous terms have been removed, write the first
residual as `t^22 d(X)`.  Only `F_0=H^2` enters at this weight, and direct
differentiation gives

```text
E_22=-20 H H' d-8 H^2 d'=1.                           (2.1)
```

Set

```text
g=-8 H^2 d.                                            (2.2)
```

Then, identically,

```text
2H g'+H'g
 =2H(-20HH'd-8H^2d')
 =2H.                                                   (2.3)
```

Thus (2.1) and (0.1) are equivalent over `K(X)`.  In the reviewed squarefree
R3 case, its pole lemma writes `d=-Y/(2H)`, so (2.2) becomes

```text
g=4HY.                                                  (2.4)
```

Consequently

```text
2Hg'+H'g=2H(4HY'+6H'Y)=2H M(Y).                       (2.5)
```

This pins the normalization repair.  Opus5's separate identity for
`g_0=HY`,

```text
H g_0'+(H'/2)g_0=(H/4)M(Y),                           (2.6)
```

is itself correct, but `g_0` is one quarter of the `g` used in (0.1).

Dividing (0.1) by `2H` gives

```text
g'+(H'/(2H))g=1,
(sqrt(H) g)'=sqrt(H).                                  (2.7)
```

For `M(Y)=1`, (2.4) equivalently gives

```text
d(H^(3/2)Y)=(1/4)sqrt(H) dX.                           (2.8)
```

Hence the integrating-factor/de Rham interpretation is exact, including its
normalizing constant.

### The `X^8-1` class

Put `H=X^8-1`, `w^2=H`, and `omega=dX/w`.  On the smooth projective
normalization,

```text
d(Xw)=(5X^8-1) omega,
[X^8 omega]=(1/5)[omega],
[w dX]=[(X^8-1)omega]=-(4/5)[omega].                   (2.9)
```

Also `dw=4X^7 omega`, so `[X^7 omega]=0`, as Opus5 states.  The curve has
genus three and `omega` is a nonzero holomorphic differential.  It cannot be
the differential of a rational function: a nonconstant rational primitive
has a pole, and its differential then has a pole, while `omega` is
holomorphic.  Thus `[w dX]!=0` in the meromorphic/function-field de Rham
quotient.  This independently recovers the reviewed impossibility of
`M(Y)=1` for this exact replacement edge.

## 3. Proof of the general `A in im(N_B)` theorem

Write `H=A^2B` with `B` squarefree.  Equation (0.1) is

```text
g'+(A'/A+B'/(2B))g=1.                                  (3.1)
```

Set `u=Ag`.  Then

```text
u'+(B'/(2B))u=A,
2Bu'+B'u=2AB.                                          (3.2)
```

First, `u` has no finite pole.  At a prime not dividing `B`, the derivative
of a principal part has one more pole than the regular coefficient times
that principal part, so it cannot cancel.  At a simple root of `B`, a pole
of integer order `s>=1` has leading coefficient `-s+1/2`, which is nonzero
in characteristic zero.  Thus `u in K[X]`.

At every simple root of `B`, equation (3.2) is regular only if `u` vanishes.
Since `B` is squarefree, `B|u`.  Write `u=Bv`, `v in K[X]`.  Substitution
into (3.2) gives

```text
A=Bv'+(3/2)B'v=N_B(v).                                 (3.3)
```

Conversely, if (3.3) holds, then

```text
g=Bv/A                                                   (3.4)
```

directly satisfies (0.1).  This proves both directions without a degree cap
or a denominator search.

### Exactness on the normalized boundary curve

Let `z^2=B`; this is the normalization of `w^2=H` under `w=Az` (componentwise
when the constant square class splits).  Equation (3.3) is equivalent to

```text
d(z^3v)=z(Bv'+(3/2)B'v)dX=Az dX=w dX.                 (3.5)
```

Thus (0.2) is exactly the vanishing of `[w dX]` in the function field of the
normalized quadratic boundary curve.  This also explains why repeated
factors belong in `A`, while the actual genus/branch data belong in the
squarefree part `B`.

## 4. Poles, degree, denominator, and the two real defects

### 4.1 Finite poles

At a root of `H` of multiplicity `e`, let a putative pole of `g` have order
`s`.  The leading coefficient in the left side of (0.1) is proportional to

```text
e-2s.                                                   (4.1)
```

Therefore a pole can occur only when `e` is even, and then its order is
exactly `e/2`.  There are no poles away from the roots of `H`.  If

```text
A0=product over roots/prime factors of even multiplicity e of p^(e/2),
```

then the correct conclusion is

```text
reduced_denominator(g) divides A0.                     (4.2)
```

Using `A0` as a fixed common denominator is sound.  Since `deg(g)=1`, an
ansatz `g=P/A0` has `deg(P)=deg(A0)+1`, hence `deg(A0)+2` coefficient
unknowns.  Cancellations in `P/A0` are allowed and sometimes forced.

Opus5's firewall instead quotes the coefficient
`((12-N)e+4s)`.  At `N=22` that vanishes at `s=5e/2`, not at `e/2`; this is
the pole order of the residual `d`, before the shift `g=-8H^2d`.  Subtracting
the `2e` contributed by `H^2` gives the possible `g`-pole `e/2`.  The report
conflates these two typed pole orders in that sentence.

The smallest denominator counterexample is

```text
H=X^2,       A0=X,       g=X/2.
```

It satisfies (0.1), but its reduced denominator is `1`.  Even with
nonconstant squarefree part, cancellation occurs.  Take

```text
B=X,
v=2(X-1)^2,
A=N_B(v)=(X-1)(7X-3),
H=X(X-1)^2(7X-3)^2,
g=Bv/A=2X(X-1)/(7X-3).                                (4.3)
```

Here `A0=(X-1)(7X-3)`, but the factor `X-1` cancels.  Exact substitution in
`Q(X)` gives zero residual in (0.1).

### 4.2 Degree at infinity

Let `h=deg(H)` and let `delta=deg(numerator(g))-deg(denominator(g))`.  If
`g~cX^delta`, the prospective leading coefficient of
`2Hg'+H'g` is `(2delta+h)lc(H)c` in degree `h+delta-1`.

- `delta>1` produces degree greater than `h` and cannot equal `2H`.
- `delta<=0` produces degree below `h`; if `2delta+h=0`, the leading term
  cancels and the degree drops still further.
- Hence `delta=1`, and comparison gives `c=2/(h+2)`.

So `deg(g)=1` is correct.  The phrase “`2 deg(g)+deg(H)` never vanishes in
characteristic zero” is not correct for arbitrary rational functions:
`H=X^2`, `g=1/X` has degree `-1` and is a homogeneous solution, with
`2(-1)+2=0`.  The resonance cannot remove the forced degree-one particular
term, which is the repaired proof above.

### 4.3 Structure of `N_B`

If `b=deg(B)>=1` and `v` is nonzero of degree `n`, then

```text
deg N_B(v)=n+b-1,
lc N_B(v)=(n+(3/2)b)lc(B)lc(v) != 0.                  (4.4)
```

Thus `N_B` is injective.  Leading-term reduction also gives

```text
K[X]=im(N_B) direct-sum K[X]_(degree <= b-2),
codim im(N_B)=b-1.                                    (4.5)
```

In particular, nonzero `A` with `deg(A)<b-1` is excluded.

If `B` is a nonzero constant, however,

```text
N_B(v)=Bv',       ker N_B=K,       im N_B=K[X].       (4.6)
```

The smallest refutation is `N_1(1)=0`.  Perfect-square edges are still all
solvable; only the injectivity and codimension wording changes.  Uniformly,
the cokernel dimension is `max(deg(B)-1,0)`.

## 5. Audit of the displayed examples

All examples in section 3.2 survive at endpoint scope.

| `H` | Decision and exact reason |
|---|---|
| `X^8-1` | `A=1`, `B=H`, and every nonzero image of `N_B` has degree at least `7`; excluded. |
| `X^16-1` | Same argument with minimum image degree `15`; excluded as an endpoint with leading edge `F_0=(X^16-1)^2`.  This is **not** the original non-Keller control whose own `F_0` is `X^16-1`. |
| `X^D-1`, `D>=2` | Squarefree, `A=1`, `deg B-1=D-1>0`; excluded uniformly. |
| `h^2` | `B=1`; choose a polynomial antiderivative `v` with `v'=h`, so `g=v/h` solves. |
| `c(X-r)^D` | Direct witness `g=2(X-r)/(D+2)` for every `D>=1`. |
| `X^2(X^2-1)` | `A=X`, `B=X^2-1`, `v=1/3`; indeed `N_B(1/3)=X` and `g=(X^2-1)/(3X)`. |

A desk-scale exact replay in Singular 4.4.1 over `Q` checked the normalized
`M` identity, the last two rational witnesses, the counterexample (4.3),
`N_1(1)=0`, and the resonant homogeneous solution `1/X`; all cleared
polynomial remainders were zero.  Opus5's claimed `33/33` reference run has
no frozen script or case table in its twelve-line lifecycle log, so that
empirical count is not independently custody-verifiable.  The proof above
does not use it.

## 6. General `(alpha,beta,N)` formula

For

```text
E(F,G)=alpha F_XG-beta FG_X-t(F_XG_t-F_tG_X),
```

direct differentiation gives the exact homogeneous identity

```text
E(F,t^n F^gamma)
 =t^n F^gamma F_X(alpha-beta gamma-n).                 (6.1)
```

Hence the formal homogeneous exponent is

```text
gamma=(alpha-n)/beta,                                  (6.2)
```

provided `beta!=0` and the chosen fractional power belongs to the charged
differential extension.

After all lower modes have actually been removed and the first residual is
`t^N d`, its coefficient is

```text
(alpha-N)F_0'd-beta F_0d'=1.                           (6.3)
```

Put `q=(alpha-N)/beta` and `d=F_0^q v`.  The two logarithmic terms cancel,
leaving

```text
v'=-1/(beta F_0^(q+1))
  =-(1/beta)F_0^((N-alpha-beta)/beta).                 (6.4)
```

Thus Opus5's algebraic formula is correct.

The geometric statement needs a type refinement.  For the cover wording,
assume `beta` is a positive integer (after a harmless sign normalization),
and let

```text
s=F_0^((N-alpha-beta)/beta)
```

in the minimal Kummer extension determined by this fractional power.  A
rational endpoint `d` is equivalent to a primitive `v` satisfying
`v'=-s/beta` in the `s K(X)` Kummer-character component.  Over a field
containing the needed roots of unity this is obtained by character
projection; descent back to `K` is linear.  One should take the normalization
of the connected component, rather than the possibly reducible affine
equation

```text
u^beta=F_0^(N-alpha-beta).                              (6.5)
```

For `(alpha,beta,N)=(12,8,22)` and `F_0=H^2`,

```text
q=-5/4,       s=F_0^(1/4)=sqrt(H),
v'=-(1/8)sqrt(H).                                      (6.6)
```

The written equation `u^8=F_0^2=H^4` is reducible/nonminimal; the charged
component reduces to `w^2=H`.  With `g=-8H^2d`, (6.6) becomes
`(wg)'=w`, exactly (2.7).

Formulae (6.1)--(6.6) do **not** prove that every required fractional mode
lies in `K(X)[[t]]`, that the displayed modes are complete for a
non-squarefree `H`, or that the residual `d` has the provenance required by
a polynomial source jet.  Those are separate hypotheses, not consequences
of superelliptic exactness.

## 7. History, contamination, and novelty adjudication

The R3 producer was already present before this ideation round, and its
hostile review has since completed:

```text
b1851156c83657fa85eb875df7e191a99fd339bfcb79ca1a752742ddff9f70b7
  xmodel/ggv-8_28-keller-face-rational-mode-exclusion-r3-sol-20260827.md
27fcd25640f62a92c147863e7a8ef8ca4b7b004f05d54450c8d2d8811c97cdc6
  xmodel/ggv-8_28-keller-face-rational-mode-exclusion-r3-hostile-review-grok-20260827.md
```

The producer already stated the six rational modes for the exact squarefree
replacement edge, the endpoint (2.1), its pole reduction to `M(Y)=1`, and the
polynomial degree obstruction; the later hostile review confirmed them.
The packet still recorded that review as live, but its timing does not alter
the novelty boundary: none of those source claims is new in Opus5 Card A.

History searches excluding every `1349Z` submission found no pre-round use of
the `H^(3/2)` primitive, the boundary-curve de Rham class, or the operator
`N_B`; `git log -S'N_B(v)'` and the corresponding integrating-factor history
search returned no commit.  Older repository occurrences of
“superelliptic” concern other lanes and do not state this endpoint theorem.
The exact criterion (0.2), its finite degree wall, and its normalization
interpretation are therefore **new to the campaign at the packet cutoff**, as
far as the recorded history shows.  This is a campaign-novel application of
elementary first-order differential algebra, not a claim of literature
priority.

Opus5 explicitly disclosed seeing the single current-round Grok line saying
that the integrating factor of `M` is `H^(-1/2)`.  Grok's sealed report does
indeed contain that line, while a current-round search finds `N_B` only in
the Opus5 submission.  Accordingly:

- the integrating-factor observation is **convergent current-round work**, not
  clean independent novelty for Opus5;
- the whole Opus5 submission remains
  `BLINDNESS-DEGRADED-BY-ONE-RG-LINE`;
- there is no textual evidence that the `A in im(N_B)` theorem came from the
  contaminating line, but cognitive independence cannot be certified from a
  lifecycle summary.

## 8. Exact promotion boundary

Mathematically eligible for a future narrow promotion, at endpoint-only
scope:

1. the equivalence between (2.1), (0.1), normalized quadratic-curve
   exactness, and (0.2);
2. the corrected pole/common-denominator and degree bounds;
3. injectivity/codimension of `N_B` for `deg B>=1`, with the constant-`B`
   branch handled separately;
4. the sufficient exclusion `deg A<deg B-1`; and
5. the algebraic general `(alpha,beta,N)` formula with the normalized Kummer
   eigenspace wording.

Not eligible from this audit: Card A's advertised cofinal GGV payoff.  Before
that payoff can be stated, a separate reviewed theorem must compile the
complete general-`H` mode list, prove the residual's raw polynomial
provenance, and land named GGV face data in the endpoint without changing
fibre, pole, target, or support type.  Until then this is a strong exact
instrument for a supplied endpoint, not a family exclusion.
