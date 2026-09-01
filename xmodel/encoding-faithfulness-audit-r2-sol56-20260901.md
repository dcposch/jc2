# Encoding-faithfulness audit: six characteristic ideals

**Status:** OPEN — audit in progress; no realization verdict is promoted by this draft.

## 0. Scope, frozen inputs, and hash gate

This is a fail-closed semantic audit of the six coefficient systems in
`msolve-prep-realization-grok46-20260831.md`.  It does not rerun a CAS and it
does not edit a ledger.  Before reading the inputs I recomputed:

```text
475ca486f3e2eed4a71e842dbe4f16ad9db43efd46c19a9318c22490e0d1010e  type86A-sliced-witness-pt0.m2.txt
c54d53f0a55586eb0fdd84d3aa311c6d64125a2cded8bec77aad1c3a8f40ec7f  msolve-prep-realization-grok46-20260831.md
3985fbedea72315c0ff3ffd4185de465ba16922bca872623fe2f02fe34cffc08  nodal-realization-86-96-grok46-20260831.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

All four match the charge.  Line references below are to those frozen bytes
(the identically hashed workspace copies are used for readable paths).

## 1. Executive verdict

**All six generated characteristic ideals are UNFAITHFUL.**  The `(8,6)`
jobs use odd coefficients of the raw binomial `p^3-q^4` before reducing its
even pole-order terms.  The `(9,6)` jobs instead force the raw binomial
`p^2-q^3` to have the target degree, thereby setting four legitimate
approximate-root coefficients to zero and searching only a strict slice.

The charged A point is decisive: it satisfies the old A equations, but it is
proper and has one infinity branch with Puiseux pair `(2,13)`.  Its true data
are `Delta=(8,6,19)`, `beta_1=13`, `delta_inf=6`; fifteen affine nodes give
`15+6=21`.  The anomaly is **not** two places.  The quadratic conjugates are
two coefficient embeddings, and the `+/-` Puiseux expansions are conjugate
series of one branch.

Neither old `(9,6)` EMPTY kill survives.  A corrected `(9,6,4)` locus is
explicitly NONEMPTY but its six-node question remains OPEN.  The exact curve

```text
q=t^6+8t^2,  p=t^9+12t^5+24t,
p^2-q^3-64q=64t^2
```

has exactly four affine nodes and realizes `(9,6,2)`.  The four `(8,6)`
targets require the corrected approximate-root jobs below.  Final suite:
five nodal types OPEN, `(9,6,2)` REALIZED.

## 2. Shared Tschirnhausen chart and conventions

For `(8,6)` the frozen chart is

```text
p=t^8+B t^5+C t^4+D t^3+E t^2+F t+G,
q=t^6+b t^4+gamma t^3+d t^2+e t+f,
H=p^3-q^4=sum h_j t^j.
```

For `(9,6)` it is

```text
p=t^9+A t^7+P6 t^6+B t^5+P4 t^4+C t^3+P2 t^2+D t,
q=t^6+a t^4+Q3 t^3+b t^2+Q1 t,
K=p^2-q^3=sum k_j t^j.
```

These are exactly the charts and raw expansions at MSOLVE-PREP 2.1--2.2
(lines 50--129).  The source/target gauges explain the displayed chart.
In particular the absent `p:t^7,q:t^5` terms make `h_23=0`, and the absent
`p:t^8,q:t^5` terms make `k_17=0`: these are the automatic first gap
conditions, not extra generators.  None of these gauges turns a raw
binomial remainder into the reduced second approximate root.

Notation is kept disjoint throughout:

- `c` is the third delta-sequence entry in `Delta=(d,n,c)`;
- `beta_1` is the first transverse Puiseux numerator;
- a *place* is a normalization point over the line at infinity;
- the `a` Puiseux conjugate series (`a=2` or `3`) describe one physical
  branch when the local equation is irreducible.  They are not `a` places.

## 3. First-principles dictionary: places, characteristic exponent, and delta split

Put `z=t^-1`,

```text
P(z)=z^d p(z^-1),        Q(z)=z^n q(z^-1),        a=d-n.
```

At `[1:0:0]` use `x=q/p` and `y=1/p`.  Then

```text
x=z^a Q/P,               y=z^d/P.
```

There is a unique formal parameter `r=z+O(z^2)` with
`r^a=z^a Q/P`, hence `x=r^a`.  Writing `z=z(r)` gives

```text
y = r^d A(r),
A(r)=P(z(r))^(d/a-1)/Q(z(r))^(d/a).
```

Thus `A=P^3/Q^4` for `(8,6)` and `A=P^2/Q^3` for `(9,6)`.
Terms of `y(r)` whose exponents are multiples of `a` are series in `x`
and are removed by the Tschirnhausen change `y -> y-Phi(x)`.  The first
remaining exponent is the first transverse numerator `beta_1`.  This is
the precise step omitted when raw coefficients of `H` or `K` are read as
characteristic coefficients.

Define the **normalized** coefficients

```text
hat_h_j = [r^(24-j)] P(z(r))^3/Q(z(r))^4,
hat_k_j = [r^(18-j)] P(z(r))^2/Q(z(r))^3.
```

Then a nonzero `hat_h_j` contributes exponent `32-j` to `y`, and a
nonzero `hat_k_j` contributes exponent `27-j`.  Vanishing the earlier
non-`a`-divisible terms pins the local `beta_1`.  Under properness this and
the reduced-approximate-root condition are equivalent descriptions of the
same datum, via `beta_1=32-c` or `27-c`.  For a polynomial incidence/rerun,
the coordinate-free way to impose it is therefore to reduce the second
approximate root to degree `c`.  Write `bar_h_j,bar_k_j` for its coefficients
after the triangular semigroup reduction specified in 7.1.  The exact
dictionary is:

| target `Delta` | `beta_1` | corrected reduced-root vanishings | exact open |
|---|---:|---|---|
| `(8,6,11)` | 21 | `bar_h_j=0`, `j={21,19,17,15,13}` | `bar_h_11 != 0` |
| `(8,6,9)` | 23 | preceding set plus `j={11,10}` | `bar_h_9 != 0` |
| `(8,6,7)` | 25 | preceding set plus `j=9` | `bar_h_7 != 0` |
| `(8,6,3)` | 29 | preceding set plus `j={7,5,4}` | `bar_h_3 != 0` |
| `(9,6,4)` | 23 | `bar_k_j=0`, `j={16,14,13,11,10,8,7,5}` | `bar_k_4 != 0` |
| `(9,6,2)` | 25 | preceding set plus `j={4,3}` | `bar_k_2 != 0` |

The chart identities at levels 23 and 17 remain automatic.  Degrees 10
and 4 in the `(8,6)` table are genuine gaps of `<8,6>`, not removable
even levels.  Conversely, the raw `(9,6)` jobs unnecessarily zero the
semigroup levels 15, 12, 9 and 6 instead of solving for their reduction
coefficients.

The AG--S/Abhyankar--Moh interpretation is the same statement globally:
`c` is the parameter degree of the **reduced second approximate root**,
not of the unreduced binomial.  Here the campaign's conversion and cluster
identities (NODAL-REALIZATION lines 19--25, 33--59) give

```text
(8,6): beta_1=32-c,  delta_inf=(beta_1-1)/2;
(9,6): beta_1=27-c,  delta_inf=beta_1-1;
delta_aff=(d-1)(d-2)/2-delta_inf.
```

The open coefficient has a second job.  Since
`gcd(d,n,c)=1` in all six rows, it excludes every nontrivial common right
component of `p,q`; the displayed parameter is then the normalization
parameter.  A polynomial parametrized image has one physical place at
infinity (only `t=infinity` lies over the infinity line).  Consequently
there is no missing independent "one-place open."  The old gcd-2/gcd-3
concern is about a multiple cover, not about two physical places, and the
corrected `c`-open already excludes it.  Affine immersivity and reduced
double points remain separate nodality tests.

Already at the second level the raw and reduced equations differ.  On
`h_21=0`, reduction of the degree-22 term gives

```text
bar_h_19 = h_19 + 4*b*(2*B+gamma),
```

in the normalization used here.  Thus `h_19=0` is not an off-by-one
version of the right equation; it is the wrong, unreduced coefficient.

## 4. Extraction and audit of the six generated ideals

The frozen generators are unambiguous (MSOLVE-PREP lines 140--655):

| job | frozen closed equations and open | reported suite state | encoding verdict |
|---|---|---|---|
| `type86_A` | raw `h_21,...,h_13=0`; raw `h_11!=0` | NONEMPTY | **UNFAITHFUL** |
| `type86_B` | raw `h_21,...,h_11=0`; raw `h_9!=0` | NONEMPTY | **UNFAITHFUL** |
| `type86_C` | raw `h_21,...,h_9=0`; raw `h_7!=0` | pending/timeout | **UNFAITHFUL** |
| `type86_D` | raw `h_21,...,h_5=0`; raw `h_3!=0` | pending/timeout | **UNFAITHFUL** |
| `type96_A` | raw `k_16,...,k_5=0`; raw `k_4!=0` | EMPTY in both engines | **UNFAITHFUL** |
| `type96_B` | raw `k_16,...,k_3=0`; raw `k_2!=0` | EMPTY in both engines | **UNFAITHFUL** |

For the four `(8,6)` jobs, the raw odd coefficients are taken before the
even pole-order terms have been reduced.  The charged witness below is an
actual false positive for A.  The same algebra affects every later level;
B's charged sliced points have the same `delta_inf=6` symptom.  In addition,
the B/C/D specs omit the reduced gap-degree-10 equation and D omits the
reduced gap-degree-4 equation.  This is neither a harmless index shift nor a
missing Rabinowitsch inverse.

The omitted equations are independent triangular obstructions, not optional
normalizations.  Once the coefficient of every available semigroup monomial
has been solved at its leading weight, degrees 10 and 4 remain because
`10,4` are gaps of `<8,6>`; no later auxiliary monomial can absorb either
coefficient.  The later raw equations `h_7,h_5,h_3` inspect different
coefficients before that reduction and cannot replace these gap equations.
There is also a small exact counterpoint for C.  Choose `gamma != 0`, put

```text
b=d=e=D=0,       B=4*gamma/3,       E=-B^2,
f=-107*gamma^2/81,  F=-2*B*C,       G=3*C^2/2,
C^3=-1648*gamma^4/10935.
```

Then direct substitution gives `h_21=...=h_9=0` and
`h_7=15*B^3*C^2 != 0`, so this is an old-C characteristic point.  But
`h_20=3C`; after the compulsory cancellation `G86=H-3C*p*q^2+...`, its
degree-17 coefficient is `-3C(B+2gamma)=-10C*gamma != 0`.  Thus even C's
later raw vanishings do not repair the high-level reduction error.  For D,
the independently necessary gap residuals at 10 and 4 are absent by
construction; its advertised exact encoding is rejected before any search
result is interpreted.

For the two `(9,6)` jobs the defect has the opposite polarity.  Setting every
raw coefficient above `c` to zero forces the *pure binomial slice*
`p^2-q^3` itself to have degree `c`.  The general reduced approximate root
also contains `p*q,q^2,p,q`.  The old locus is therefore sufficient when it
has a point: its forward type implication remains sound.  It is not
necessary and hence is not a faithful exact/exhaustive encoding.  An EMPTY
result proves only

> no point of that pure-binomial slice survives the stated immersion/colon
> opens.

It does **not** prove that the corrected characteristic locus is empty, and
therefore proves no `(9,6,c)` type kill.  This corrects the overclaim in
MSOLVE-PREP 2.3 (lines 131--138).  The resultant inverse and cover colon are
downstream restrictions on the wrong base ideal and cannot repair its
meaning.  The coordinator's warning that NONEMPTY remained provisional
(the frozen integration, lines 89--90) was therefore necessary but not
sufficient: EMPTY also had to remain provisional on encoding faithfulness.

## 5. Exact desk check of the charged type86_A witness

Let `zeta^2-zeta+18474=0`.  Reading the eleven values in the chart order
`(B,C,D,E,F,G,b,gamma,d,e,f)` gives

```text
p=t^8+t^5+(294-zeta)/144*t^3+(150-zeta)/48*t,
q=t^6+t^4+3/4*t^3+t^2-(138+zeta)/192*t+(2*zeta-71)/144.
```

The two roots of the quadratic give coefficient-conjugate curves, not two
places.  Direct substitution, using `zeta^2=zeta-18474`, gives

```text
h_21=h_19=h_17=h_15=h_13=0,
h_11=(355746-27671*zeta)/110592 != 0.
```

For instance `h_19=-9+3D-4e=0`; the irrationality of `zeta` proves the
displayed `h_11` is nonzero.  Thus this is genuinely a point of the old A
locus, not a variable-order accident.

Now reduce rather than merely inspect `H=p^3-q^4`.  Its leading coefficients
at this point are

```text
h_22=-4, h_21=0, h_20=-10, h_19=0.
```

The first two standard monomials have pole degrees 22 and 20, so put

```text
R=H+4*p^2*q+6*p*q^2.
```

Degrees 22, 21 and 20 cancel, whereas

```text
[t^19]R=h_19+4*(2B+gamma)=0+4*(2+3/4)=11.
```

Therefore the reduced second approximate root has degree `c=19`, not 11.
This single calculation exhibits the exact semantic bug.

For an independent local check let `s=t^-1`,

```text
P=s^8 p(s^-1)=1+s^3+D*s^5+F*s^7,
Q=s^6 q(s^-1)=1+s^2+3/4*s^3+s^4+e*s^5+f*s^6,
x=q/p=s^2 Q/P,                 y=1/p=s^8/P.
```

Expansion only through the deciding order gives

```text
x=s^2+s^4-1/4*s^5+s^6+(e-1-D)*s^7+O(s^8),
y=s^8-s^11-D*s^13+O(s^14).
```

The analytic Tschirnhausen coordinate

```text
y_star=y-x^4+4*x^5-10*x^6
```

satisfies

```text
y_star=(2+3D-4e)*s^13+O(s^14)=11*s^13+O(s^14).
```

After replacing `s` by the unique uniformizer with `x=r^2`, the branch is
`(x,y_star)=(r^2,11r^13+...)`.  It is irreducible with one Puiseux pair
`(2,13)`: `beta_1=13`, `delta_inf=(2-1)(13-1)/2=6`, and
`Delta=(8,6,32-13)=(8,6,19)`.

Properness is also desk-visible.  A nontrivial common right component would
have degree two.  Write a normalized quadratic as `phi=t^2+a*t+c`.  The
missing `t^7` coefficient of `p=P(phi)` forces `a=0`, after which `P(phi)`
is even, contradicting the nonzero `t^5` coefficient of `p`.  Hence the map
is birational.  Only `t=infinity` maps to the infinity line, so there is one
physical place.  The `+/-r` series are conjugates of that branch.

Conditioning on the charged machine statement of fifteen ordinary affine
nodes, the genus check is exact:

```text
p_a(degree 8)=21=delta_aff 15+delta_inf 6.
```

The frozen witness file itself is only a coefficient payload: line 6 says
`Nexpected=3` (neither 11 nor 15) and it contains no postcheck output.
Accordingly this audit verifies the infinity/genus split, but does not claim
that those eight lines alone replay the reduced degree-30 ordered scheme.

## 6. Per-ideal faithfulness verdicts and exact corrections

All six ideals are **UNFAITHFUL** to their advertised exhaustive meaning.
For A/B the error admits false positives; for 96A/96B it cuts to a strict
slice and admits false negatives; C/D inherit the A/B construction before
their computations finish.  The exact replacements are specified in 7.1.

| job | typed audit finding |
|---|---|
| `type86_A` | **UNFAITHFUL, witnessed false positive.** The charged point passes every raw generator/open but has `Delta=(8,6,19)`. |
| `type86_B` | **UNFAITHFUL.** Its raw equations make the same unreduced substitution; the charged sliced points' `delta_inf=6` are consistent with the same actual `c=19`, not target `c=9`. |
| `type86_C` | **UNFAITHFUL before computation.** The exact counterpoint in Section 4 passes old C but has a nonzero corrected degree-17 residual; replace the raw equations and add degree 10. |
| `type86_D` | **UNFAITHFUL as an exact encoding.** Its raw list omits the independent reduced gap residuals at degrees 10 and 4; replace it before interpreting any output. |
| `type96_A` | **UNFAITHFUL strict slice.** EMPTY kills only the slice `a15=a12=a9=a6=0`, not the full type. |
| `type96_B` | **UNFAITHFUL strict slice.** The same; in fact an exact four-node realization exists below. |

Two supplementary formulas already on disk give useful exact negative
controls for the old `(9,6)` EMPTY interpretation.  They are reproduced here
so the conclusion does not depend on a label in those reports.

For `(9,6,4)`, put

```text
p=t^9+3t^7+21/4*t^5+35/8*t^3+63/32*t,
q0=t^6+2t^4+5/2*t^2,                  y=q0+3/4.
```

The identity recorded and coefficient-checkable at
`xmodel/hf-twin-964-grok46-20260831.md:109-133` is

```text
y^3-p^2=27/1024*(8t^4+13t^2+16).
```

Hence, in the **shared constant-zero chart**,

```text
p^2-q0^3-(9/4)q0^2-(27/16)q0-27/64
  =-27/1024*(8t^4+13t^2+16).
```

This is a proper corrected-locus point of exact degree 4, while raw
`p^2-q0^3` has degree 12.  It also passes the affine-immersion open.  With
`z=t^2`,

```text
q0'=t*(6z^2+8z+5),
p' mod (6z^2+8z+5)=-27z/8-117/32.
```

The latter can vanish only at `z=-13/12`, where the quadratic has value
`27/8`, and `p'(0)=63/32`; hence `p',q0'` have no common root.  Exact
degree 4 together with `gcd(9,6,4)=1` also rules out a common right
component.  Thus the full corrected open is already NONEMPTY.
The cited desk analysis proves four nodes and leaves affine delta two as
either two more nodes or one `A_3` (`ibid.:135-157`), so it does not by
itself settle the six-node realization question.

For `(9,6,2)`, put

```text
q=t^6+8t^2,                 p=t^9+12t^5+24t,
p^2-q^3-64q=64t^2.
```

This lies in the shared chart and is proper: the identity recovers `t^2`,
then `t=p/(t^8+12t^4+24)`.  Its infinity type is therefore
`Delta=(9,6,2)`, `beta_1=25`, `delta_inf=24`, so `delta_aff=28-24=4`.
Let `w=t^4`.  Each of the two nonzero simple roots of
`w^2+12w+24` yields two pairs `{t,-t}`, one for each sign of `t^2`.
Within a fixed `w` those two pair-images have opposite nonzero
`q=t^2(w+8)`, while
`q^2=w*(w+8)^2=-8*(w+12)` distinguishes the two `w`-families.  Thus all
four images are distinct.  At them

```text
p'=8w(w+6) != 0,             q'=2t(3w+8) != 0,
```

and the velocities at `t,-t` have nonzero determinant.  They are four
ordinary nodes.  Since they exhaust `delta_aff=4`, there are no omitted
singularities.  This independently recovers the pair calculation in
`xmodel/block-descent-a1-genus-four-cable-b1-hostile-review-grok46-20260831.md:245-267`.
Thus `type96_B` is not merely NONEMPTY after correction: its advertised
nodal type is **REALIZED**.

## 7. Re-typed realization suite and rerun specification

### 7.1 Correct characteristic incidence ideals

Do not patch the old files by shifting an `h` or `k` subscript.  Introduce
the coefficients of the reduced second approximate root explicitly.

For `(8,6)` use

```text
G86 = p^3-q^4
    + a22*p^2*q + a20*p*q^2 + a18*q^3
    + a16*p^2   + a14*p*q   + a12*q^2
    + a8*p + a6*q.
```

The subscript is the leading pole degree.  Retain only terms of weight
strictly greater than the target `c`, let `g_j=[t^j]G86`, and use:

| job | auxiliary terms retained | closed equations | Rabinowitsch open |
|---|---|---|---|
| A, `c=11` | `a22,...,a12` | `g_22,...,g_12` | `u*g_11-1` |
| B, `c=9` | `a22,...,a12` | `g_22,...,g_10` | `u*g_9-1` |
| C, `c=7` | preceding plus `a8` | `g_22,...,g_8` | `u*g_7-1` |
| D, `c=3` | preceding plus `a6` | `g_22,...,g_4` | `u*g_3-1` |

For `(9,6)` use

```text
G96 = p^2-q^3 + a15*p*q + a12*q^2 + a9*p + a6*q.
```

For A (`c=4`) impose `[t^j]G96=0` for `5<=j<=16` and invert
`[t^4]G96`; for B (`c=2`) impose the coefficients for `3<=j<=16`
and invert `[t^2]G96`.  Constants may be omitted because every target
degree is positive.  These incidence systems are triangular in the `a_w`;
they may be eliminated to obtain the `bar_h/bar_k` equations in Section 3.
Their independent corrected equation counts in the eleven chart variables
are `5,7,8,11,8,10`, respectively.

On each corrected locus, retain the affine tests in their proper roles:
invert `Res_t(p',q')`; then run the reduced unordered double-point check
with `N=11,10,9,7,6,4`.  The corrected `c`-open already excludes common
degree-2/3 covers, although the old cover colon is harmless if its ring and
map are asserted.  Required semantic controls for the rerun are:

1. the charged witness must fail corrected A and be classified at `c=19`;
2. the displayed `(9,6,4)` point must satisfy corrected 96A;
3. the displayed four-node `(9,6,2)` point must satisfy corrected 96B;
4. the existing `(6,4,3)` nodal and monomial-cover controls remain.

### 7.2 Binding retyping

| advertised type | old suite label | sound label now | next action |
|---|---|---|---|
| `(8,6,11)` | raw ideal NONEMPTY | **OPEN / RECOMPUTE** | corrected A, then `I_DP` length 11 |
| `(8,6,9)` | raw ideal NONEMPTY | **OPEN / RECOMPUTE** | corrected B, then length 10 |
| `(8,6,7)` | pending | **OPEN / RECOMPUTE** | stop old job; corrected C, then length 9 |
| `(8,6,3)` | pending | **OPEN / RECOMPUTE** | stop old job; corrected D, then length 7 |
| `(9,6,4)` | **KILLED** by raw EMPTY | corrected locus **NONEMPTY**, nodal status **OPEN** | apply length-6 postcheck/search on corrected locus |
| `(9,6,2)` | **KILLED** by raw EMPTY | **REALIZED** by the exact four-node curve in Section 6 | corrected job only as a regression control |

Accordingly neither `(9,6)` KILL survives.  Neither raw `(8,6)` NONEMPTY
result says that its named corrected locus is nonempty.  The pending C/D
computations target the wrong ideals and cannot acquire a typed verdict by
finishing.  The only final realization verdict available after this audit is
the positive `(9,6,2)` witness; the other five advertised nodal types remain
OPEN at their stated scopes.

## 8. Guardrail checks, limitations, and final status

- **Flag/place/series:** the report never turns Puiseux conjugates, field
  embeddings, or `gcd(d,n)` into physical places.  The witness has one place.
- **Raw remainder degree:** every promoted type statement uses the reduced
  second approximate root; zero, vanished leaders, semigroup reductions and
  gap degrees 10/4 are explicit.
- **Variable/ring map:** the eleven-value witness order is declared, and the
  corrected jobs are incidence ideals in the frozen coefficient rings with
  named auxiliary coefficients.  Matching variable names are not used as a
  map proof.
- **Open and `sat()` discipline:** opens are Rabinowitsch equations on the
  corrected leading coefficient.  Colon/resultant operations are not allowed
  to change the semantic meaning of the base ideal.
- **Floor/attainment:** corrected NONEMPTY for `(9,6,4)` is not promoted to a
  nodal witness.  `(9,6,2)` is promoted only because four explicit transverse
  pairs exhaust the independently computed affine delta.
- **Evidence custody:** the charged A payload contains no 15-node transcript
  and has `Nexpected=3`; its nodality is consumed only as the charge states it.
  The infinity calculation is independently exact.
- **Scope:** no CAS, ledger edit, `jc2-lean` inspection, or exit-price claim was
  made.

Primary mathematical interfaces checked against the frozen report and the
published descriptions are the approximate-root/semigroup criterion in
[Assi--García-Sánchez](https://arxiv.org/abs/1407.0490) and the statement that
the second approximate-root value is the third delta entry in
[Fujimoto--Suzuki--Yokoyama](https://staff.fukuoka-edu.ac.jp/fujimoto/abh2/files/abh2.pdf).
The frozen NODAL-REALIZATION report itself records this exact job at line 195
and the beta/cluster/genus conversions at lines 19--59.

**Final status: CLOSED AS AN ENCODING AUDIT.**  All six advertised
exact/exhaustive encodings are rejected and replaced by the incidence
specifications in Section 7; the forward implications from the two strict
`(9,6)` slices remain sound.  Realization status is five OPEN and one
REALIZED, as typed in 7.2.
