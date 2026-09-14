# Proposed p523 place: four additional inverse nodes

MANUAL / UNREVIEWED. ROOT static finite-field calculation, no scientific
execution. First source work approximately03:45UTC September12; transaction
opened03:48:42UTC. Original publication reserve03:58/HARD04:01 unchanged.
This extends the existing proposed523/V0 precheck; it is not a qualified
place, row packet, rank observation, source point or source exclusion.

## 1. Exact source and result

All arithmetic in this note is in k=F523. Charge the literal retained
producer `box/f10-necessary-rows-producer-astra-20260911/produce.py`, SHA
5078142850c5f4d2e4f08da18fad01ea0271bf36c18740df372884747535280a.
It was freshly read WHOLE as inert text this turn, with current pin-before
read reuse from the immediately preceding support gate; final postpin below.
The existing proposed place and first-five-scalar precheck were freshly
pinned before WHOLE reads:

- `xmodel/f10-p523-place-candidate-root-20260911.md`, SHA
  7b0298b10e190bfde6b6e32ad448ec2bf99dbcc099519c786b602159e1b9a4b1.
- `xmodel/f10-r3-vzero-place-astra-20260911.md`, SHA
  3f70c36d66bb9cc8fdbbb53a8546fcf1dc4547897374cc50a3b55658d7b1bbcb.

Those earlier manual claims remain UNREVIEWED; this note does not promote
their full septic vector. Starting from their literal W=151, V=0 and
t5=9, this note independently derives C,D and the four late scalars:

| named inverse node | actual defining residue | inverse | integer product |
|---|---:|---:|---:|
| critical_c | 36 | 247 | 8892=17*523+1 |
| pivot8, selected c1 | 464 | 195 | 90480=173*523+1 |
| pivot9, selected c1 | 429 | 306 | 131274=251*523+1 |
| pivot10, selected c1 | 298 | 86 | 25628=49*523+1 |

Thus four of the ten formerly uncomputed scalar nodes survive, conditional
on the previously stated leading specialization. The six det1,...,det6
remain UNCHECKED. None is implied by this table. The unchanged producer and
checker must independently reconstruct every node; no hardcoding or bypass.

## 2. Independent leading-polynomial arithmetic

In k, 17/10=54, W^-1=381 since151*381=57531=110*523+1.
Let c=1+T+151T^3. For t_j=[T^j]c^(17/10), the formal derivative identity
c*(c^nu)'=nu*c'*c^nu gives

    j*t_j=(55-j)*t_(j-1)+(165-j)*151*t_(j-3),

with t0=1 and negative indices zero. The seven recurrence numerators,
reduced modulo523, are54,247,27,0,45,0,0. Division by1,...,7 gives

    (t0,...,t7)=(1,54,385,9,0,9,0,0).

For example the j6 numerator is9*(49+159*151)=9*24058,
and24058=46*523. At j7 both contributing predecessors vanish. Since
9^-1=465, the normalized literal leading polynomials are

    C=T^3+381T+381,
    D=T^5+T^3+159T^2+6T+465.

This also independently checks contact6/contact7 at these residues. As a
direct polynomial cross-check, 10CD'-17C'D=-T^7: its remaining nontrivial
coefficients at T5,T4,T3,T2 are respectively

    -21+33*381 = 24*523,
    50*381-31*159 = 27*523,
    13*381-41*6 = 9*523,
    507*381-51*465 = 324*523.

At T1 and T0 the coefficients are381*(20*159-7*6)=381*6*523
and381*(60-17*465)=-381*15*523. T6 is identically zero.

## 3. Actual late column recurrence

Write a=381 and kappa=17-h. The literal operator is

    O_h(A,B)=10CB'-kappa*C'B+(10-h)*AD'-17A'D.

For h7,8,9 the source chooses Avar=1, targetvar=0 and Bvar of degree<=2.
Set s=10-h=kappa-7 and Bvar=b2*T^2+b1*T+b0. The T4,T3,T2 equations give

    b2=-5*s/(20-3*kappa),
    b1=0,
    b0=((20-kappa)*a*b2+3*s)/(3*kappa).

The residual column, in the source's exact order(T,1), is

    c1=20*a*b2+318*s,
    c0=-kappa*a*b0+6*s.

These formulas implement the source's descending upper solve before any
low-row cancellation. None divides by a parameter polynomial. Evaluating:

| h | kappa | s | (b0,b1,b2) | (c1,c0) |
|---|---:|---:|---|---|
| 7 | 10 | 3 | (400,0,263) | (355,40) |
| 8 | 9 | 2 | (388,0,375) | (464,72) |
| 9 | 8 | 1 | (369,0,132) | (429,267) |

Useful literal fractions for checking the table: b2 at h7,8,9 is
3/2,10/7,5/4. Their b0 is a/2+3/10, (110*a/7+6)/27,
(5*a+1)/8. All small denominators are units in k.

At h10 the DIFFERENT choice is Avar=0, targetvar=-T4. The upper solve
therefore sets b2=1,b1=0,b0=13*a/21=460, and the residual column is

    (c1,c0)=(20*a,-7*a*b0)=(298,138).

This equals the source's independent literal ell-column formula when F=0,
H=a. The source tests c1 BEFORE c0; all three h8/9/10 c1 are nonzero.
Their inverse products appear in section1. No alternative coordinate choice
or unsupported claim that every column coordinate is invertible is used.

## 4. The critical z coefficient is independent of early forcing

The source introduces z for the first time at h7. All earlier Ab/Bb and
Uglobal,d0 are independent of z. Thus the z coefficient of Apart is T,
that of target is -2T5, and that of forcing is zero. This statement holds
whenever the earlier circuit is defined, without inspecting its unknown
early inverse values. The upper solve is linear, so its z coefficient Bz
is found solely from

    O_7(T,Bz)-(-2T5).

The contribution 3TD'-17D+2T5 is

    -8T3-1749T2-84T-7905.

Descending cancellation gives

    Bz=(-583/10)+(-2/5)*T = 517+418T.

The remaining low coefficients, again in the exact order(T,1), are

    base1=-84=439,
    base0=10*a*(418-517)-17*465=356.

The code defines Psi7=c1*base0-c0*base1, with c1=355,c0=40 from
section3. Therefore the ACTUAL affine-graph coefficient is

    [z]Psi7=355*356-40*439=108820=208*523+36.

This sign uses the literal source definition, not a choice of determinant
orientation. It is independent of the Lambda functional used to complete
the low column; this note does not certify that additional identity. The
source later requires Psi7=Hq+critical_c*z and independently inverts the
actual scalar. It may still refuse on any earlier/later mandatory check.

## 5. Scope, controls and stopping point

QUANTITY: four specific scalar residues and their inverse products at the
already proposed523/V0 leading place. CHEAPEST TEST: this inert-source,
hand-recurrence check is completed; a different-model static review would
be approximately10 minutes UNMEASURED planning wall, not a launch or cap.

Controls: using the h8/9 Avar=1 formula at h10 is wrong because Avar is0
and targetvar=-T4 there; the explicit h10 solve above retains that distinction.
Swapping the low determinant order changes critical_c's sign and would
not equal the named source expression. Nonzero late coordinates alone do
not validate ANY det1,...,det6, the claimed monic vector, source anomaly
rows, full payload or rank. A failed remaining scalar is BAD PLACE, not
a characteristic-zero vanishing, source point or counterexample.

COLLISIONS: the two September11 candidates explicitly leave these ten nodes
unknown. The new contribution is the four named late-node evaluations;
finite-place evaluation, initial primality/root checks and the first five
scalars are OLD. This does not reopen a stopped source family or provide
a new all-degree mechanism. Six completed-map determinant tests remain;
no separate determinant farm or dependent task is selected by this note.

No code/source/cap changes, mathematical subprocess, local import/AST/syntax/
test, AWS operation, coefficient artifact or scientific output was used.
The unrelated arithmetic.py read in this turn was selected inert context,
not a charged WHOLE arithmetic review. Only the three exact inputs above
are mathematical premises for this note. No new external theorem is used.

Own complete untruncated preseal readback and all three unchanged postpins
completed03:51UTC; hand-checks include the independent leading ODE,
ascending upper coefficients, source determinant sign and all four explicit
inverse products. No raised canonical OPEN identifier. Final marker is added
only after these checks; expected transaction verification and sealed WHOLE
readback follow. Basis0d39df3c9fd69c939a8420c54d03228b9077777d.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7876`.
- Body SHA-256:
  `497c24df18cc3b797e2cbd2aa890ca63a0442762b3060ff0f9f777782e5db9a2`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
