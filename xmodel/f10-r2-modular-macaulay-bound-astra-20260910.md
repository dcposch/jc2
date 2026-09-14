# r2: basis-free modular Macaulay weight bound

NEW CONDITIONAL MANUAL THEOREM, UNREVIEWED. First action 2026-09-10 15:31:53 UTC; fixed hard
cap 15:53:00 UTC, publication reserve 15:50:00 UTC, never reset. Exact
owned report, transaction and box destinations were absent. Basis
0d39df3c9fd69c939a8420c54d03228b9077777d.

Exactly four inputs were hash-pinned before bodies. Fresh WHOLE read: the
FIRST fullsource gate. Explicit previously completed same-byte WHOLE reuse:
the fullsource producer and cyclic producer/gate, after all current pins
matched. No clipping or missing tail. Prior authorship is disclosed.
No other input, coefficient body, code, enumeration or scientific subprocess
is used. ROOT's bound is a proposal to prove, not a premise.

## 1. Verdict and exact coefficient matrix

The proposed weight-30 bound is COMPLETE under the FULL special highest
regularity premise. A fully prescribed basis-free matrix over the residue
field k has 247 rows and 754 columns; membership of the constant vector 1
is equivalent to the unlocalized special quotient being zero. No chosen
35-element quotient basis or multiplication table is required. Optional
elimination of the compatibility-column span gives a seven-row quotient
with 330 additional columns, but no canonical seven coordinates are
asserted without that actual elimination.

This is a theorem about a prospective instrument, not an actual matrix,
rank, coefficient calculation, place, unit certificate or source result.
The accepted 17zzw local-model/source-lift hypotheses remain mandatory.
No scientific enumeration or computation was performed; counts below are
derived by finite hand sums.

Let S=k[Y1,Y2,Y3], with weights 1,2,3, and let S_{<=n,c} denote its span
of monomials of weight at most n and weight congruent to c modulo five.
Write f5,f6,f7 for the ACTUAL special Psihat_h(Y,1), with highest forms
H5,H6,H7 regular, and I=(f5,f6,f7), R=S/I. The fifteen additional rows g_j
are exactly the six K1_i, eight K0_i and the mixed L1-U0 L0 of the accepted
cyclic interface. They have respective upper weights

    (13,12,11,10,9,8; 15,14,13,12,11,10,9,8; 19)

and cyclic classes given by those weights modulo five. Put Q=R/(g_j).
All named zero/dependent slots remain; a coefficient bound need not be
attained. The matrix columns are the literal coefficient vectors of

    m*g_j, wt(m)<=12, wt(m)+deg_cyclic(g_j)=0 mod5;
    m*f_h, wt(m)<=30-h, wt(m)+h=0 mod5,

in ALL monomials of S_{<=30,0}. Its target is the constant monomial 1.
This is ordinary polynomial coefficient equality, not reduction in a
guessed quotient basis. Every column has class zero. Since 19+12=31 and
its actual monomial weights are multiples of five, the first group has
weight at most 30; the second does so by construction.

## 2. The load-bearing strictness statement

Under regularity of the highest forms, for every N,

    I intersect S_{<=N} = sum_(h=5)^7 f_h*S_{<=N-h}.       (1)

Here a negative filtration bound means the zero space. Proof with degree
control: represent p in I as sum b_h f_h and let D=max(wt(b_h)+h).
Let b_h,top mean its weight-(D-h) part, possibly zero. If D>wt(p), the
degree-D terms cancel: sum b_h,top H_h=0. Exactness of
the graded Koszul complex of the regular H_h expresses this homogeneous
syzygy by coefficients c_hj=-c_jh, c_hh=0, of weight D-h-j, as
b_h,top=sum_j c_hj H_j. Replace b_h by b_h-sum_j c_hj f_j. The represented
polynomial is unchanged, since the paired products f_h f_j cancel, and
the maximal weighted degree strictly decreases. Repetition reaches
D<=wt(p)<=N. This proves (1); p=0 uses the zero representation. No
unbounded effective Nullstellensatz estimate is invoked.

If p has cyclic class zero, projecting each resulting b_h to class -h
preserves p and does not increase weight. Thus (1) also has exactly the
class-restricted form used by the matrix. The argument uses graded Koszul
exactness and projection onto a direct monomial grading, not averaging or
division by five. It is valid in every characteristic. It controls the
actual lower terms of f_h; using only H_h in the matrix would be wrong.

## 3. Completeness, soundness, and the accepted source lift

The accepted regular-highest theorem says R is spanned by ALL monomials
of weight <=12, with seven dimensions in each cyclic class. No selection
of a basis is needed for this spanning fact. If Q=0, write 1=sum a_j g_j
in R, project a_j to the complementary cyclic class, and choose polynomial
representatives b_j in S_{<=12,-deg(g_j)}. The polynomial

    p=1-sum b_j g_j

lies in I and S_{<=30,0}. Applying (1) and then cyclic projection gives
the required bounded compatibility coefficients. Consequently 1 lies in
the displayed matrix column span. Conversely such a column identity is
a literal identity in (f,g), hence Q=0, without any regularity assumption
for this positive direction.

For generic SOURCE lifting, positive polynomial equality alone is not
enough. Retain an authenticated integral local model with fraction field
the WHOLE accepted B, integrality of all three f_h and of every used named
g_j, and FULL same-special highest regularity. Accepted 17zzw then makes
the local unlocalized quotient finite and uses Nakayama to lift its zero
special fibre to zero generic quotient, hence zero guarded source through
the accepted nineteen-row cover/core. Modular L0^35 membership is not the
constant target and does not lift. No new proof of those foundations or
alteration of their qualifications is claimed here.

The complete 754-column test requires authenticated reductions of all
fifteen g_j. A particular positive identity can instead use a subset:
the FIRST gate's refinement requires integrality only on its used rows,
applies the finite argument to that subideal, and then takes the full
generic source as a further quotient. This does not pretend that an
undefined special reduction of an unused nonintegral row exists.

## 4. Exact hand counts and permissible compression

The number of monomials of exact weight n is

    p(n)=sum_(c=0)^floor(n/3) (floor((n-3c)/2)+1).

This counts choices of the exponents of Y3, then Y2, with the Y1 exponent
forced. The needed finite sums were performed by hand:

| object | weights | counts at those weights | total |
| --- | --- | --- | ---: |
| rows | 0,5,10,15,20,25,30 | 1,5,14,27,44,65,91 | 247 |
| f5 multipliers | 0,5,10,15,20,25 | 1,5,14,27,44,65 | 156 |
| f6 multipliers | 4,9,14,19,24 | 4,12,24,40,61 | 141 |
| f7 multipliers | 3,8,13,18,23 | 3,10,21,37,56 | 127 |

For example p(30)=16+14+13+11+10+8+7+5+4+2+1=91. The compatibility
group therefore has 424 columns. The all-monomial coefficient spans of
weight <=12 have class counts

    class 0: p(0)+p(5)+p(10)=20,
    class 1: p(1)+p(6)+p(11)=1+7+16=24,
    class 2: p(2)+p(7)+p(12)=2+8+19=29,
    class 3: p(3)+p(8)=3+10=13,
    class 4: p(4)+p(9)=4+12=16.

There are 102 such monomials in total, but only the complementary class
is used for each row. The fifteen g_j have class multiplicities
(3,2,2,4,4) in classes 0,1,2,3,4. Their column count is consequently

    3*20 + 2*16 + 2*13 + 4*29 + 4*24 = 330.

Thus the raw coefficient matrix is 247-by-754, or 247-by-755 with the
target appended. These are fixed slot counts, not counts of nonzero or
independent coefficients. No actual coefficient field element is supplied.

By (1), the compatibility columns span I intersect S_{<=30,0}; their
quotient is R_0, of dimension seven. Their rank is therefore 240 under the
premise. As a separate homogeneous-H Koszul count check, shifts 11,12,13
give 80,71,62 monomials, and the triple shift 18 gives 29. Thus
424-(80+71+62-29)=240. Quotienting that column span leaves an intrinsic
seven-dimensional row space and 330 g-columns. Choosing its coordinates
requires actual elimination, but not a full 35-basis or a multiplication
table. The raw form above avoids that coordinate choice entirely. Under
the hypotheses, the g-images are exactly J_0 and the combined cokernel is
Q_0. Thus full rank 247 of the combined raw matrix is equivalent to
membership of 1 and Q=0. No coefficient-independent choice of 240 pivot
columns or seven row coordinates is promised.

For a specified used-row subset the same proof permits the smaller bound
D=max_j 5*floor((w_j+12)/5). For the complete fifteen-row mask D=30. If
the mixed row is not used, D<=25; for all fourteen other rows the analogous
raw matrix has 156 rows and (91+80+71)+306=548 columns. That subideal's
unit test is stronger than the full ideal's test; dropping the mixed row
is NOT an equivalence for arbitrary data. No alternate run is proposed.
There is no assertion that 30 is the optimal bound for the unknown actual
coefficients, only a complete uniform bound with these prescribed spans.

## 5. Changed-hypothesis control: a unit ideal missed without the highest premise

Over any field k, use weights x:1,y:2,z:3 and set

    f5=x^5, f6=x^6, f7=x^7;
    g=x*y^7-1 in the weight-15/class-0 K0_1 slot;
    all other fourteen g slots zero.

These are changed polynomials, NOT actual r2 coefficients. The stated
weights and cyclic classes hold, but the highest zero locus contains the
plane x=0. Put t=x*y^7. Modulo (x^5), t^5=0, whereas g=0 imposes t=1.
The full quotient is zero; a literal identity is

    1=x^5*y^35-(1+t+t^2+t^3+t^4)*g.              (2)

Its maximum weighted product degree is 75. Yet no identity from the
proposed weight-30 matrix exists. Modulo (x^5) all compatibility columns
vanish. A remaining identity would be 1=a(t-1), with a represented by
monomials of weight <=12. In that quotient the inverse is UNIQUE:

    a=-(1+t+t^2+t^3+t^4).

Its nonzero term t^4=x^4*y^28 has weight 60 and cannot be represented
with weight <=12, or even <=15, modulo the homogeneous monomial ideal
(x^5). This is a contradiction. Here filtered strictness alone even holds
for I=(x^5); the missing finite weight-12 spanning assertion already breaks
the proposed completeness. The accepted 17zzw lifting countercontrols
remain in force as well; none is replaced by this changed example.

## 6. Remaining quantity, read scope and stop

The exact next scientific quantity is the constant-vector membership in
this actual finite-field coefficient matrix AFTER authentication of the
integral model and full-special highest certificate. No place, coefficient
array, rank, membership, timing or height estimate is known here. A rejected
candidate identity is not certified nonmembership. Even certified special
Q nonzero would not give generic or guarded-source survival. No all-r,
degree-frontier or JC2 conclusion follows.

All four input pins matched before reads. The fullsource FIRST gate was
freshly read WHOLE; the other three use explicitly permitted, actually
completed same-byte WHOLE reuse. No clipping or missing tail occurred.
No provenance, baseline, code, old arithmetic, live highest-code review or
other lane was read. All authored writes use apply_patch, each below the
1500-word per-write cap; the existing transaction is documentary only.

## OPEN(S) RAISED

None new. The bound/completeness question is answered conditionally. The
actual model, full-special highest certificate and constant-vector test
remain unknown, with exact test specified above. No execution, review,
implementation, research lane or follow-on is authorized.

## COLLISIONS

status: EMPTY. Own-only absence check, no corpus scan or shared write.

Own WHOLE review and all four repeated pins completed at 15:40:55 UTC;
the final degree-part clarification and count wording were then reread.
Exact final report/transaction targets were still absent before sealing.
Mathematics is complete; only documentary transaction and custody follow.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11700`.
- Body SHA-256:
  `0b987622eb43c104d9bec25dd62235524e4f55eff24dc80a8a5c176eb44f6140`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
