# Hostile review: exact upper-face cascade through weights 3--6

Reviewer: Fable5 (different-model hostile referee)  
Date: 2026-08-27  
Charged producer:
`xmodel/ggv-8_28-upper-cascade-w3-w6-sol-ultra-20260827.md`  
Charged case: `cases/ggv_8_28_upper_cascade_w3_w6_20260827/`

## Overall verdict

**CORRECT / PROMOTE WITH TWO REPAIRS.**  The complete fixed-factor
parametrization of polynomial solutions through `D6`, the final dimensions
`63/60/61`, the characteristic-mode census, both `q1` separators, and the
`D22=0` firewall all survive independent rederivation.  Two claims require
correction:

1. the branch-Q intermediate row-five gcd stratum has dimension
   `26+c`, with maximum `29`, not `24+c` / maximum `28`;
2. the parametrization is exact for field-valued geometric points, hence for
   the underlying reduced support, but not for the natural coefficient
   **scheme**, which is nonreduced at the cone point.

The first error does not propagate to row six or to the final dimension `61`.
The second repair changes the scheme-theoretic wording, not the classified
set of polynomial solutions over a characteristic-zero field.

| # | charged atom | verdict |
|---:|---|---|
| 1 | source and case pins | **PASS** |
| 2 | same-weight operator and characteristic solution formula | **PASS** |
| 3 | P modes `c2,c4,c6`; Q mode `c4` through weight six | **PASS** |
| 4 | exact row-two and row-three gates | **PASS** |
| 5 | exact row-four gate and windows | **PASS** |
| 6 | row-five numerator formulas and gcd stratification | **PASS** |
| 7 | Q row-five stratum dimension `24+c`, maximum `28` | **FAIL**; correct value `26+c`, maximum `29` |
| 8 | row-six collapse `A|W` and final divisibility gates | **PASS** |
| 9 | necessity and existential sufficiency of the displayed P/Q parametrizations for field-valued points | **PASS** |
| 10 | literal equality with the full coefficient scheme | **FAIL**; the scheme is nonreduced at the cone point |
| 11 | final reduced component dimensions `63,60,61` in the 210-slot ambient | **PASS** |
| 12 | injectivity of each parameter map and P-component intersection dimension `59` | **PASS** |
| 13 | raw upper-window containment and absence of a lower cutoff through `D6` | **PASS** |
| 14 | listed gate mutations | **CORRECT**; some replay assertions are compact divisibility checks rather than independent universal proofs |
| 15 | three dense full-window fixtures and byte-exact result replay | **PASS** in the orchestration replay; Fable did not consume them as proof |
| 16 | branch-P `q1` rank/nonmembership separator | **PASS** |
| 17 | branch-Q `q1` rank/nonmembership separator | **PASS** |
| 18 | `q1` transversality and two-way separators | **PASS**, with the branch-Q row-three intersection sharpened to dimension `4` |
| 19 | `F=U^2,G=U^3`, all homogeneous rows zero, and `D22=0` | **PASS** |
| 20 | no affine endpoint, later-row, landing, Keller, or JC2 conclusion | **PASS** |

## 1. Custody and independent-review disclosure

The charged hashes were recomputed from live bytes:

```text
6e3d9104effe39c0dd0e34377bb7bdc6ede4f25f472f9f9c0098706aceffb60a  xmodel/ggv-8_28-upper-cascade-w3-w6-sol-ultra-20260827.md
54767fceaa1cc6b3feb64d9d07f7af1e2ffd43a725617123e6e6849091b23615  cases/ggv_8_28_upper_cascade_w3_w6_20260827/RESULT.json
```

Both match the required pins.  The case freeze also verifies on every file:

```text
PREREGISTRATION.md: OK
README.md: OK
RESULT.json: OK
verify_upper_cascade.py: OK
```

Different-model execution used Claude Code `2.1.228`; the session metadata
identifies the responding model exactly as `claude-fable-5`.  Fable read the
charged report and case, then rederived the identities from the recurrence
without running the producer verifier.  Its first high-effort response spent
its output budget on the hostile derivation; the same session was resumed at
low effort solely to render the verdict.  A final narrow resumption checked
the dual-number scheme counterexample below.

Separately, the coordinating exact replay ran

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B verify_upper_cascade.py --check
```

and returned

```text
{"P_dimension": 63, "Q_dimension": 61, "q1_separators": 2,
 "result_sha256": "54767fceaa1cc6b3feb64d9d07f7af1e2ffd43a725617123e6e6849091b23615",
 "status": "PASS"}
```

That replay is supporting evidence only.  The symbolic claims below were
rederived rather than inferred from a producer `PASS`.  No heavy local CAS or
AWS job was used, no canonical ledger was edited, and `jc2-lean` was not read,
built, status-inspected, or touched.

## 2. Characteristic architecture and mode census

Work over a characteristic-zero field `K`.  Put `F0=H^2`, `G0=H^3` and

```text
D_n = sum_(i+j=n) ((12-j) F_i' G_j + (i-8) F_i G_j').       (2.1)
```

For `R_n=G_n-(3/2)HF_n`, the terms involving the new weight are

```text
L_n(R_n)=2H((12-n)H'R_n-4HR_n').                            (2.2)
```

The kernel in `K(X)` is one-dimensional:

```text
ker L_n = < H^((12-n)/4) >.                                 (2.3)
```

This follows either by direct integration or by checking the full
characteristic identity.  For the chart expression

```text
E(F,G)=12F_XG-8FG_X-t(F_XG_t-F_tG_X),
```

one has

```text
E(F,t^m F^alpha)=t^m F^alpha F_X(12-m-8alpha).
```

Thus `alpha=(12-m)/8`, and recursive subtraction of the first nonzero
coefficient gives the complete formal solution for fixed `F`.

Through weight six this becomes

```text
P: G = F^(3/2) + c2 t^2 F^(5/4) + c4 t^4 F + c6 t^6 F^(3/4)
       mod t^7,

Q: G = F^(3/2) + c4 t^4 F
       mod t^7.                                             (2.4)
```

Indeed, on P, `H=A^2` makes (2.3) polynomial exactly at even weights,
giving leading kernels `A^5,A^4,A^3` at `2,4,6`.  On Q,
`H=A^2B` with squarefree `B` makes (2.3) rational only when
`4|(12-n)`, so only `n=4` occurs through six.  A forbidden fractional
mode cannot cancel the rational baseline: at its first weight it lies
outside `K(X)`.  This proves completeness, not just construction of one
family.

## 3. Independent row derivation

### 3.1 Rows two through four

Row one is unique:

```text
G1=(3/2)HF1.
```

The baseline residual at row two is `3F1^2/(8H)`, so polynomiality is
equivalent to

```text
H | F1^2.                                                   (3.1)
```

Hence `F1=AU` on P and `F1=ABU` on Q.  In both branches the non-mode
part at row three is

```text
U(12A^2F2-U^2)/(16A^3).                                    (3.2)
```

The P `c2` contribution is `(5/4)c2 A^2U`, already polynomial.  Reduction
at every simple root of `A` shows that (3.2) is polynomial iff `A|U`.
Therefore, on both branches,

```text
F1=HV,                  deg V<=7.                           (3.3)
```

This cuts the original 16-dimensional `F1` window to dimension eight.

Set `Delta=4F2-V^2`.  Direct binomial expansion gives

```text
R4=(3/4)VF3+3Delta^2/(128H)+polynomial modes.               (3.4)
```

Consequently

```text
P: Delta=AW,       deg W<=10;
Q: Delta=ABW,      deg W<=9.                               (3.5)
```

Squarefreeness makes these conditions necessary and sufficient.  Their
codimensions in the 15-dimensional `F2` window are four and five.

### 3.2 Row five and the corrected Q count

After (3.5), the exact remaining numerators are

```text
Q: A^2 | 3W(16AF3-VW),                                    (3.6Q)

P: A^2 | 3W(16AF3-VW)
          +10c2 A V(8F2-V^2).                              (3.6P)
```

Write `C=gcd(A,W)`, `A=C A0`, `W=C W0`, and `c=deg C`.
For Q, and for the P locus `c2=0`, the baseline gate is exactly

```text
A0 | V,
A0 | 16F3-(V/A0)W0.                                       (3.7)
```

On P the mode adds exactly `c2=0 or A|V`.  These formulas all pass.

The producer's Q dimension is wrong.  Its ambient `(V,W,F3)` has dimension
`8+10+14=32`.  On the stratum with fixed divisor `C|A`,

```text
dim W  = 10-c,
dim V  =  5+c,
dim F3 = 11+c,
```

so

```text
dim(Q row-five stratum) = 26+c.                            (3.8)
```

The maximum is `29` at `C=A` (`c=3`).  The printed `24+c` and “maximum
28” are not only false but mutually inconsistent, since `24+3=27`.
For comparison, the producer's P counts survive: `25+c`, maximum `29`,
on `c2=0`, and dimension `26` on the arbitrary-`c2`, `A|V` locus.

### 3.3 Row six

The baseline nonpolynomial numerators are exactly

```text
N6P = 192A^3WF4 + 6(8AF3-VW)^2 - AW^3,
      denominator 1024A^4;

N6Q = 192A^3BWF4 + 6(8AF3-VW)^2 - ABW^3,
      denominator 1024A^4B.                                (3.9)
```

On P the remaining `c2` contribution is

```text
c2(640A^2VF3+20A^2W^2-20AV^2W-5V^4)/(2048A^3),            (3.10)
```

apart from the polynomial term `(5/4)c2AF4`.

At a simple root of `A` not dividing `W`, row five forces `V` to order at
least one and its residual bracket to the needed order.  In (3.9), the
term `-AW^3` then has order exactly one, while the square has order at least
two, the `F4` term at least three, and the common-denominator form of
(3.10) at least three.  Cancellation is impossible.  Hence

```text
A|W,       W=AZ,
Delta=HZ,  F2=(V^2+HZ)/4,       deg Z<=6.                  (3.11)
```

Substitution leaves precisely

```text
P: A  | 8F3-VZ;
Q: AB | 8F3-VZ.                                            (3.12)
```

The factor `B` in Q follows at the simple roots of `B` from the square term
in (3.9).  Row five is now automatic on Q.  On P the mode condition is
exactly `c2=0 or A|V`; when `c2` is active, `A|V` also makes (3.10)
polynomial.  Thus

```text
P: F3=(VZ+AT)/8,       deg T<=9;
Q: F3=(VZ+ABT)/8,      deg T<=8.                           (3.13)
```

`F4,F5,F6` remain arbitrary in their raw windows; `c4,c6` on P and `c4`
on Q remain free.  Equations (3.3), (3.11), and (3.13), together with
(2.4), prove necessity and existential sufficiency through `D6` for
ordinary field-valued polynomial points.

## 4. Dimensions, windows, and the scheme correction

For fixed leading factors, the 210 raw slots split as 81 `F` slots and
129 `G` slots.  The parameter counts are

```text
P, c2=0:
  8(V)+7(Z)+10(T)+13(F4)+12(F5)+11(F6)+2(c4,c6) = 63;

P, A|V, c2 arbitrary:
  4(V/A)+7(Z)+10(T)+36(F4..F6)+3(c2,c4,c6) = 60;

Q:
  8(V)+7(Z)+9(T)+36(F4..F6)+1(c4) = 61.                   (4.1)
```

The two P supports intersect where `c2=0` and `A|V`, in dimension `59`.
Neither contains the other.  The parameters are recovered successively
from `F1,F2,F3`, then the mode constants from `G2,G4,G6`, so each component
map is injective.  The resulting reduced-support codimensions are
`147,150,149`.

Every upper bound is exact.  A baseline term at weight `n` containing `k`
positive `F` coefficients has degree at most

```text
24 + sum_r(16-i_r) - 16k = 24-n.
```

The P `c2` and `c4` mode contributions have bounds `22-n` and `20-n`;
the `c6` leading term has degree 12 in the `G6` window of upper degree 18.
The Q `c4` mode has bound `20-n`.  Also `deg(VZ)<=13`,
`deg(AT)<=13`, and `deg(ABT)<=13`.  There is no positive lower cutoff
through weight six.

### 4.1 Literal scheme equality is false

The producer calls (4.1) the “full raw solution scheme.”  The equations do
not license that wording.  Let

```text
R=K[epsilon]/(epsilon^2)
```

and choose any `f in K[X]`, `deg f<=15`, with `H` not dividing `f`.  Set

```text
F0=H^2,       F1=epsilon f,       F_n=0 for n>=2,
G0=H^3,       G1=(3/2)H epsilon f, G_n=0 for n>=2.          (4.2)
```

The raw windows hold.  Directly in (2.1), `D1=0`: the `F1'` terms cancel
`12-12`, and the `H'F1` terms cancel `33-12-21`.  For `n>=2`, every term
is zero except the possible `(1,1)` contribution at `n=2`, which is
quadratic in `epsilon` and hence zero.  Thus (4.2) is an `R`-point of the
natural `D1,...,D6` coefficient scheme (indeed of every homogeneous row).

But `F1=HV` has no solution `V in R[X]` because its `epsilon` coefficient
would require `H|f`.  Equivalently, the field argument
`H|F1^2 => H|F1` fails over the dual numbers because `F1^2=0`.

Fable independently checked this attack and returned **PASS**.  At the cone
point the determinant scheme has all 16 raw `F1` tangent directions, while
the parametrized reduced support has only the eight `HV` directions.  The
scheme is therefore nonreduced there, with at least eight excess tangent
directions.  This does not say that every generic component point is
nonreduced, nor does it add a new field-valued solution.  The clean repair is:

> Replace “full raw solution scheme” by “field-valued polynomial solution
> set” or “underlying reduced geometric support.”

The dimensions in (4.1) remain correct dimensions of the reduced supports
(and hence their topological component dimensions).

## 5. Controls and replay scope

The frozen replay reconstructs three full-upper-degree fixtures: P with
`c2=0`, P with active `c2`, and Q.  It checks every `D0,...,D6` exactly over
`Q`; every `F_n` and `G_n` reaches its raw upper degree.  It also checks the
listed mutations:

* `F1=A` on P and `F1=AB` on Q pass row two and fail row three;
* `V=1,F2=0` passes row three and fails row four;
* `V=Z=c2=1`, `W=A`, `F3=1/8` passes row four and fails the P mode gate
  at row five (residue `10A mod A^2`);
* `V=Z=1,F3=0`, `W=A`, `c2=0` passes row five and fails row six on both
  branches.

Some mutation flags in the script reduce to the exact divisibility residue
such as `A` not dividing `-1`; they are faithful sentinels, not a replacement
for the derivation above.  In particular, the replay did not expose the
incorrect intermediate Q dimension because that number is absent from
`RESULT.json`.

## 6. The `q1` comparisons and separators

The two already-reviewed image operators are

```text
P: T_A(Q)=2AQ'-3A'Q,                        deg Q<=12;
Q: T_Q(Q)=4ABQ'-(6A'B+AB')Q,               deg Q<=11.      (6.1)
```

On the squarefree loci, `T_A` is injective: a kernel would require
`Q^2=cA^3`.  Thus its rank is 13 in the 16-dimensional `F1` window.
On squarefree coprime Q, a kernel of `T_Q` would require
`Q^4=cA^6B`; the valuations at simple roots forbid it, so the rank is 12.

The relevant intersections are uniform, not fixture accidents:

| branch | divisibility space | dimension | intersection with `q1` image | dimension |
|---|---|---:|---|---:|
| P | `A K[X]_{<=11}` | 12 | `T_A(A K[X]_{<=8})` | 9 |
| P | `A^2 K[X]_{<=7}` | 8 | `T_A(A^2 K[X]_{<=4})` | 5 |
| Q | `AB K[X]_{<=10}` | 11 | `T_Q(AB K[X]_{<=6})` | 7 |
| Q | `A^2B K[X]_{<=7}` | 8 | `T_Q(A^2B K[X]_{<=3})` | 4 |

For example, divisibility of `T_A(Q)` by `A` forces `A|Q` because
`gcd(A,A')=1`; a second `A` forces a second factor.  On Q, reduction modulo
`A` and `B` first forces `AB|Q`, and a second `A` then forces
`A^2B|Q`.  The dimensions meet the Grassmann lower bounds, so all four
pairs are transverse and span the full 16-dimensional window.

The clean cascade-but-not-`q1` separator is `F1=H`, uniformly on both
squarefree branches.  On P, membership would reduce to

```text
A'Q2+2AQ2'=1,
```

whose leading coefficient is `(4+2d)lc(Q2)` in degree `d+3`.  On Q it
would reduce to

```text
2A'BQ3+3AB'Q3+4ABQ3'=1,
```

whose leading coefficient is `(12+4d)lc(Q3)` in degree `d+4`.  Neither
has a polynomial solution in characteristic zero.  Conversely,
`T_A(A)=-AA'` and `T_Q(AB)` give `q1`-positive elements failing the
row-three `H` divisibility.  Thus neither gate implies the other.

The report's fixtures agree: P uses `A=X^4-1`; Q uses
`B=X^2-1`, `v=X^2/5`, and

```text
A=Bv'+(3/2)B'v=X^3-(2/5)X.
```

Fable checked this norm-survivor identity and the rank/nonmembership
arguments independently.

## 7. Closed square control and the endpoint firewall

For every `deg V<=7`, put

```text
U=H+(V/2)t,       F=U^2,       G=U^3.                      (7.1)
```

Both determinant brackets in `E(F,G)` vanish identically because `F` and
`G` are powers of the same `U`.  The nonzero positive coefficients are

```text
F1=HV,       F2=V^2/4,
G1=(3/2)H^2V,  G2=(3/4)HV^2,  G3=V^3/8,
```

and their degrees are exactly inside the frozen windows.  With `V=1`,
Section 6 proves `F1=H` lies outside both `q1` images.  Therefore even **all**
homogeneous vanishing rows do not imply `q1`.

The same identity gives `D22=0`.  It is not a point of the endpoint system

```text
D1=...=D21=0,       D22=1.
```

Hence there is no contradiction with the tower theorem that licenses `q1`
only after the affine target and `D23=0`.  Nothing here decides `D23`, an
endpoint-normalized face, a GGV landing, a Keller pair, or JC2.

## 8. Maximum promotable theorem

Let `K` be a characteristic-zero field.  Fix the frozen raw windows through
weight six and fixed monic factors of one of the following types:

```text
P: H=A^2,       deg A=4, A squarefree;
Q: H=A^2B,      deg A=3, deg B=2,
                 A,B squarefree and gcd(A,B)=1.
```

Then the geometric polynomial solutions of `D1=...=D6=0` are exactly:

```text
P:
  F1=HV,                         deg V<=7,
  F2=(V^2+HZ)/4,                 deg Z<=6,
  F3=(VZ+AT)/8,                  deg T<=9,
  F4,F5,F6 arbitrary,
  G given by the P formula (2.4),
  c4,c6 arbitrary, and c2=0 or A|V;

Q:
  F1=HV,                         deg V<=7,
  F2=(V^2+HZ)/4,                 deg Z<=6,
  F3=(VZ+ABT)/8,                 deg T<=8,
  F4,F5,F6 arbitrary,
  G given by the Q formula (2.4),
  c4 arbitrary.                                             (8.1)
```

Necessity and existential sufficiency both hold.  The underlying reduced P
locus is the union of components of dimensions `63` and `60`, meeting in
dimension `59`; the reduced Q locus has dimension `61`.  The parameter maps
are injective, and every coefficient lies in its raw window.  The natural
coefficient scheme has this reduced support but is nonreduced at the cone
point, so no reducedness, primary-decomposition, or scheme-isomorphism claim
is promoted.

For the previously reviewed `q1` image operators (6.1), the square family
(7.1) with `V=1` proves that homogeneous determinant vanishing, even at all
weights, does not imply `q1`.  This statement has endpoint `D22=0` and gives
no result for the affine endpoint-normalized problem.

## 9. Sharp endpoint-extension successor

Use the simplest q1-negative branch-P control

```text
A=X^4-1,       V=1,       F1=H=A^2,       c2=0.            (9.1)
```

Do **not** freeze the square solution's later coefficients.  Retain every
remaining parameter allowed by (8.1), every later raw `F` slot, and the
later P characteristic constants `c8,c10,c12`.  Compile the characteristic
form through `D21` on the complete frozen D3 windows.  In those windows `F`
has no slot from weight 15 onward and `G` has no slot at weight 22, so
`D22=1` is a slotless accumulated compatibility target rather than another
same-row solve.

The charged question is

```text
D1=...=D21=0,       D22=1,       with (9.1),              (no D23).  (9.2)
```

The certificate contract is:

* **positive:** exact rational coefficient lists for every surviving raw
  slot, a frozen direct replay of `D0,...,D22`, the raw-window audit, and the
  exact rank proof that `F1=H` is outside `im T_A`.  Conditional on the
  reviewed tower theorem, this proves that `D23` adds genuinely new
  information;
* **negative:** name the earliest obstructed row and provide an exact
  divisibility/residue or left-cokernel certificate on every prior stratum.
  If nonlinear elimination remains, give a complete saturated-cover
  Nullstellensatz certificate for the fixed-control ideal.  Failure of one
  specialization or one heuristic solve is not a negative certificate.

A negative answer to (9.2) excludes only this fixed separator.  It does not
prove that the endpoint prefix implies `q1`; the next escalation would keep
the full q1-negative locus rather than a single `V`.  Compilation is desk
work, but any heavy exact elimination belongs on AWS.

---

**Final referee verdict:** promote the exact field-valued `D1..D6` cascade,
the reduced component dimensions `63/60/61`, the q1 nonimplication theorem,
and the `D22=0` firewall.  Correct the Q row-five count to `26+c`, maximum
`29`, and forbid the phrase “full solution scheme”: the natural scheme is
provably nonreduced at the cone point.  No affine endpoint, D23, face,
landing, Keller, counterexample, or JC2 conclusion follows.

## Report SHA-256

The self-referential stamp is excluded.  The SHA-256 of the 566-line report
body above is

```text
91d9142f7db420068b6f9cc20bbd381fc9b3b52ae29d62284a6f5762db5333e9
```

Reproduce with:

```bash
head -n 566 \
  xmodel/ggv-8_28-upper-cascade-w3-w6-hostile-review-fable5-20260827.md \
  | shasum -a 256
```
