# Independent audit and extension of the deep active-`c2` prefix

Date: 2026-08-28  
Lane: `active_c2_extend` (Sol Ultra; same-model independent reconstruction)  
Verdict: **REPAIR — CHARGED FORMULAS PASS; ONE VALUATION CLAIM IS FALSE; EXACT BRANCH CONTINUES THROUGH D15**

## 1. Result

The six displayed identities in the charged producer are coefficientwise
correct when rebuilt from the complete fractional-power recurrence with all
ten characteristic modes registered.  In particular, the two D8 lifts, D9
product, D10 repair, residual D10 factor, and deepest D11 factor all pass.

There is, however, one actual mathematical overstatement.  From

```text
g11[-2] = D*B11/(1048576*A^2)
```

the condition `D=0 mod A`, meaning only `A|D`, does **not** make the class
polynomial.  Writing `D=A*d1` leaves `d1*B11/(1048576*A)`.  The producer's
sentence that this mod-`A` branch survives the deepest D11 equation is
therefore false.  Its proposed successor with the exact equation `D=0` is
valid, and that exact branch is what is extended here.  None of the earlier
D8--D10 conclusions changes.

On exact `D=0`, the complete subleading D11 row and deepest D12 row form a
new paired repair.  They force two further `A`-lifts at characteristic-zero
field points on `c2!=0`.  After those lifts, D12 is a new two-factor rung and
the deepest D13 class is just its predecessor times `-S/4`.  A literal
raw-window point with both `c2` and `c6` nonzero satisfies every determinant
row through D15; D14 uniquely fixes a legal nonzero `c14`, and D15 then
vanishes.  Thus D11--D15 do not kill the exact `D=0` branch.

This lane is same-model and cannot by itself promote the theorem under the
campaign's different-model rule.

## 2. Dependencies and audited prefix

Assume the reviewed q1-free D9 theorem (`1874b9db...`) and hence write

```text
F0=A^4,
F1=A^2 V0,
F2=(V0^2+A^2 Z)/4,
F3=(V0 Z+A T)/8,
V0=A S,
T=A U.
```

Here `A` is a monic squarefree quartic over a characteristic-zero field and

```text
G = F^(3/2) + sum_(m=2,4,...,20) c_m t^m F^((12-m)/8).
```

No q1 representation, `R0`, or D23 is used.  The complete recurrence includes
the modes `c2,c4,...,c20`; a mode is never deleted merely because it is
regular at the row being inspected.

Put

```text
K=64F4-Z^2.
```

The independent recurrence gives, successively,

```text
g8[-2] = 3K^2/(32768A^2),

K=A R,
g8^- = -5c2(S^2-2Z)^3/(65536A),

S^2-2Z=A Q,
D=R-4SU,
P=256F5-RS+2S^2U,
g9^- = 3DP/(65536A),

g10[-2] = 3P(P-2SD)/(524288A^2).
```

The D9 and D10 residue equations force `A|P` rootwise; write `P=A P1`.
With

```text
Egen=2048F6-2SP1+Q(R-8SU)-8U^2,
```

the complete remaining D10 pole is

```text
g10^- = D(20c2D+3Egen)/(524288A).
```

The independently reconstructed deepest D11 class is exactly

```text
g11[-2] = D*B11/(1048576A^2),

B11=-10c2SD-3072F6S+3P1S^2
    -3QS(R-6SU)-6U(R-6SU).
```

These are all characteristic-polynomiality necessities.  The formulas do
not by themselves assert raw-window existence for a general parameter point.

## 3. The D11/D12 paired repair on exact `D=0`

Now impose the exact equation

```text
D=R-4SU=0
```

and define

```text
E=2048F6-2SP1-4QSU-8U^2,
L=QS+4U,
M=P1+2QU,
N11=5c2 L(4E+L^2)+6EM.
```

The **complete** negative part at weight 11, including every subleading
`c2` contribution, is

```text
g11^- = N11/(4194304A).                                (R11)
```

The deepest weight-12 class, rebuilt independently rather than inferred
from R11, is

```text
g12[-2] = (3E^2-2S N11)/(33554432A^2).                 (R12)
```

At each reduced root of squarefree `A`, R11 gives `N11=0`.  R12 then gives
`3E^2=0`, hence `E=0`; substituting this back into R11 gives
`5c2 L^3=0`.  On the genuine open `c2!=0`, therefore,

```text
A | E,
A | L.                                                  (D12 repair)
```

This is field/radical reasoning.  It does not prove ideal membership over a
nonreduced parameter scheme.

## 4. First product after the new lifts

Write

```text
E=A e1,
L=A ell,
U=(-QS+A ell)/4,

J=P1-SQ^2/2,
N=8192F7-e1S+QJ.
```

After literal substitution in the full recurrence, every D11 pole is gone
and the complete remaining D12 polar part is

```text
g12^- = J(20c2J+3N)/(8388608A).                         (R12r)
```

The entire `A^-2` class at D13 is

```text
g13[-2] = -S*J(20c2J+3N)/(33554432A^2).                (R13)
```

Thus the deepest D13 equation is not an independent factor cut: it is
`-S/4` times the D12 numerator with one additional denominator power.  It
can require a second `A` in the product on roots where `S` is a unit, but it
does not choose either factor.  The subleading D13 row retains `c6`, and the
raw survivor below verifies that those terms can cancel without violating
the windows.

## 5. Literal raw-window survivor through D15

Over `Q`, take

```text
A=X^4-1,
S=Q=c2=c6=1,
U=-1/4,
R=-1,
Z=(1-A)/2,
P1=1/2,

F4=(Z^2-A)/64,
F5=(A-1)/512,
F6=1/4096,
F7=...=F15=0,

c14=-6139/17179869184,
c4=c8=c10=c12=c16=c18=c20=0.
```

Then

```text
D=0,
S^2-2Z=A,
P=A/2,
E=L=J=0.
```

The independent checker constructs all `F0,...,F15` and
`G0,...,G15` as literal polynomials, not merely Laurent classes, and proves

```text
D0=...=D15=0,
deg Fn <=16-n,
deg Gn <=24-n.
```

Both active modes are genuinely present: `c2=c6=1`.  The D14 row fixes the
legal born mode `c14=-6139/17179869184`; then D15 adds no obstruction.  In
this fixture `G12=4093/268435456` and `G13=G14=G15=0`.  Mutating `F7` from zero to one while
retaining `c6=1` produces the exact D13 pole

```text
6139/(8192A),
```

so the D13 pass is not caused by having silently dropped the `c6` mode.
This point is not on q1 and proves only that the q1-free active branch remains
nonempty through the stated raw prefix.

## 6. Separate `c2=0,A|V0` companion

The active-open lift `A|(S^2-2Z)` is unavailable when `c2=0`.  Keeping that
sublocus separate, assume only `V0=AS`, `T=AU`, and `K=AR`; put

```text
H=S^2-2Z,
D=R-4SU,
P0=256F5-RS+2S^2U+2UH.
```

Independent reconstruction gives

```text
g9^- = 3D P0/(65536A),

g10[-2] = 3[P0(P0-2SD)+H D^2]/(524288A^2).
```

Consequently D9/D10 force `A|P0` at field points and, root by root,

```text
H D^2=0.
```

This is a per-root split `H=0` or `D=0`; it does not globally force either
`A|H` or `A|D`, and it is not folded into the `c2!=0` theorem above.

## 7. Reproducibility, verdict, and scope

Self-contained checker:

```text
cases/ggv_8_28_upper_endpoint_active_c2_d11_d13_extension_20260828/
  verify_active_c2_extension.py
```

Checker SHA-256:

```text
112650dc27b0e13d76979d5adca9315919ee65cb8d9eaf717c1685f99d96de26
```

Replay:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_upper_endpoint_active_c2_d11_d13_extension_20260828/verify_active_c2_extension.py
```

Expected marker:

```text
PASS_REPAIR_ACTIVE_C2_D8_D13_EXTENSION
```

Charged producer report/checker hashes are respectively `e3b777f8...` and
`00111fee...`; the upstream recurrence implementation has hash
`fceb189b...`.  This checker imports none of them.

Verdict by claim:

- D8 K/H lifts: **PASS**.
- D9 product and D9/D10 repair `A|P`: **PASS**.
- residual D10 and displayed deepest D11 factor: **PASS**.
- claim that `D=0 mod A` itself survives deepest D11: **REFUTE / REPAIR TO
  EXACT `D=0` OR AN ADDITIONAL VALUATION CONDITION**.
- exact `D=0` successor: **PASS AND EXTEND** through R11, R12, R12r, R13,
  and one literal raw-window survivor through D15.

No endpoint emptiness, q1 exclusion, unrestricted branch-P result, scheme
divisibility, Keller theorem, or JC2 conclusion follows.
