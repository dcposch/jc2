# Independent rank-lane audit: the t=8 integrality caveat

Verdict for this subtask: **CAVEAT DISCHARGED-HERE**. The charged clause (i) had
an explicit missing fail-stop (H-int) certificate. This audit supplies that
certificate at the original prime `(32003,11288)` and the new prime
`(32027,23825)`. Consequently the rank lane does not force a conditional final
theorem after this audit. This note does not prejudge the separate H2b replay
or the parent agent's whole-cone logic audit.

## 1. What the frozen caveat means

The exact condition is not merely that 32003 is prime, that H_8 has a simple
root, or that a_0 is nonzero. It is that the exact terminal rows and their
derived B_r,C_r (and, for the other route, I_2 and W_r) have coefficients in
the local coefficient ring at `(32003,yy-11288)`, and that their modular
implementations are the reductions of these same generators. The rank
report separates `(H-gen)` from `(H-int)` and says that t=8 had no `PINT PASS`:
its entire p-integrality evidence was the absence of Singular's `? div. by 0`
marker, expressly described as a detector rather than a fail-stop
(`xmodel/k16-rank-criterion-fable5-20260903.md:498`, especially 503–510).
The frozen harvest expressly says `(T)_8 inherits it`
(`/tmp/jc2-lane.yGKJor/inputs/k16-t8-fglm-harvest-opus5-20260905.md:431`).

If that missing certificate were left unaudited, the conservative gate type
would be `CONFIRMED-CONDITIONAL[(H-int) at (t,p,yy)=(8,32003,11288)]`.
This is a generator-integrality condition, not a condition that the rank
variety itself is reduced or geometrically irreducible. The label
`single-prime` is a replication limitation; it is not an extra mathematical
hypothesis in the properness lemma.

Clause (i) itself is `V(B_1,...,B_7,C_1,...,C_7)={0}`. The banked `(B)` hsop
statement is stronger, and implies it. Calling clause (i) literally the
assertion that `(B)` is an hsop conflates these two statements; the
implication used here is valid (`xmodel/k16-rank-criterion-fable5-20260903.md:209`,
especially 223). The existing modular transcript prints
`PARTI (B,C): dim=0 vdim=5224` and `PARTI (B) alone: dim=0 vdim=11440`
(`box/k16rank-20260903/rank_t8_mod_p32003_b0_parti.out:254`). No second
Groebner calculation of these banked ideals was needed to discharge H-int.

## 2. Direct certificate from every exact coefficient

The new executable is
`box/k16-t8-gate-20260905/rank_pintegral_audit.py`; it writes
`rank-pintegrality.json` and its stdout is preserved in `rank-pintegrality.log`.
It uses only integer arithmetic, `fractions.Fraction`, regular expressions,
and a restricted arithmetic AST evaluator. Assertions stop on malformed row
syntax, any unclassified division, a denominator divisible by p, a missing
or duplicate row/pivot, a wrong row map, a wrong root, or a zero pivot.

Its exact source is
`box/k16rank-20260903/terminal_t8_exact_none.out`, SHA-256
`8f41559606bbf9f2c592f5569ee0feef596d7196d39d2290941bdf889990f767`.
The file contains all 16 rows, 17 high pivots, and its existing terminal
`RECURRENCE_PASS`/`DRIVER_DONE` markers. The certificate independently checks
all **45,806** denominator occurrences (**45,290** distinct integer values)
in all 16 exact rows. Every denominator is a unit modulo **both** 32003 and
32027. The top eight rows used by the rank and H2b generators have **9,576**
denominator occurrences. The root agent's separately obtained count of
9,584 for the generated prefix includes the eight `/2` coefficient-extraction
divisions, so those counts agree in scope rather than contradict each other
(`box/k16-t8-gate-20260905/rank-pintegrality.json:87`).

The scan does not merely extract a convenient subset of fractions: it
checks all names against `yy,b3,b4,q2_0,...,q7_0`, validates the allowed row
characters, and asserts that every slash introduces an integer denominator
at a token boundary. Thus these exact row expressions themselves lie in
the relevant local coefficient ring. This direct argument proves the
needed row integrality even independently of the spine-denominator list.

For `(H-gen)`, the executable compares the entire RHS of every top row
`T8,...,T15` byte-for-byte to the exact dump in both
`box/k16rank-20260903/rank_t8_mod_p32003_b0_parti.sing` and
`box/k16t8-20260905/affinewms2_t8_mod_p32003_b0.sing`.
All 16 comparisons pass; input hashes are in
`box/k16-t8-gate-20260905/rank-pintegrality.json:90`.
The actual coefficient map is `yy -> 11288` into F_32003, with identity
images of `b4,q2_0,...,q7_0,b3`, in this order and with weights
`1,2,...,7,9`; the P ring drops b3. The rank script extracts `a_r,b_r,c_r`
by coefficient evaluation/differentiation and division by 2, then forms
`B_r=a_0 b_r-a_r b_0`, `C_r=a_0 c_r-a_r c_0` and W_r by ring operations
(`box/k16rank-20260903/rank_driver.py:75`). The harvested generator does
the same (`box/k16t8-20260905/gen.py:63`). Because 2 is a unit, these
operations commute with reduction. This supplies the required generator
map, not merely matching variable names.

## 3. Independent spine-denominator certificate

The banked properness gate's denominator inventory is (D-a) through (D-h):
fixed integers bounded by `8t+3`, yy, 2yy, q, 2q², 6q³, the 2t+1 high
pivots, and the additional pivots `yy*g` and `q/yy`
(`xmodel/k16-properness-gate-opus5-20260903.md:146`, especially 152–175).
The exact generator confirms divisions by the corresponding quantities
(`box/k16rank-20260903/singular_terminal_driver.py:124`, 147, 160, 167, 184).
Here t=8 gives q=17, e=25, N=33, and the largest bounded integer is 67.
Both primes exceed 67; both roots satisfy H_8=0, its derivative is a unit,
and disc H_8=124848 is nonzero modulo each prime. The values are:

| unit | p=32003, yy=11288 | p=32027, yy=23825 |
|---|---:|---:|
| g | 1643 | 14643 |
| yy*g | 16447 | 31391 |
| q/yy | 24918 | 21816 |

The 17 high-pivot residues, in declared weight order 1 through 17, are:

```text
32003: 19097 11155 2103 17277 5948 15406 5053 2740 11134
       28585 10574 18801 2606 22291 21604 6325 30404
32027: 16870 31014 15113 6794 2465 3266 10817 16904 6126
       8453 19387 12639 5080 14953 13068 24958 17165
```

Every entry is nonzero. The pivot order is checked against
`C1,...,C7,q8_0,...,q16_0,b2`, bands 32 down to 16, and exactly 17 entries
are required. Each short exact pivot expression is evaluated over Q at
the stated integer root using Fraction arithmetic before reduction.

As an independent parsing/control path, the old banked
`box/k16propgate-20260903/pintegral_check.py` was run unchanged. Its old
one-line pivot input format was produced mechanically from the exact
two-line `PIVOT weight=... band=... variable=...` format: preserve the band,
variable and exact coefficient; replace the parameter name `yy` by its old
name `y`. The resulting explicit 17-line data file is
`rank-pivots-bank-format.txt`. Both banked executions report exactly 17
pivots and `PINT_RESULT ... PASS (all denominators are P-units)`:
`box/k16-t8-gate-20260905/banked-pint-32003.log:31` and
`box/k16-t8-gate-20260905/banked-pint-32027.log:31`.
This is the same positive certificate missing from the frozen rank lane,
now supplied without changing that frozen lane or its ledger.

## 4. Consequence for promotion

Let R be the localisation at `(p,yy-r)` of the integral coefficient model,
with the fixed prime-to-p integer denominators inverted. Its fraction
field is `Q(yy)/(H_8)=Q(sqrt(3))`. The B_r have positive weights 10 through
16 and coefficients in R. The banked F_32003 computation gives
`V(B_1,...,B_7)={0}`. The **properness promotion lemma**, not affine
flatness, therefore gives the same conclusion over the algebraic closure
of Q(sqrt(3)): `xmodel/k16-properness-gate-opus5-20260903.md:99`.
Its proof takes `Proj(R[b4,q2_0,...,q7_0]/(B))`; the morphism to Spec R is
proper, its special fibre is empty, and its closed image cannot avoid the
closed point of a local base unless it is empty. The gate explicitly says
**No flatness** (`xmodel/k16-properness-gate-opus5-20260903.md:117`).

Thus `(B)` is an hsop over Q(sqrt(3)), its characteristic-zero CI length
is `product(10,...,16)/7! = binomial(16,7)=11440`, and `(i)_8` follows.
This characteristic-zero length follows from a now-proved hsop and its
weights; it is not an unjustified lift of a modular length.

**Recommended parent-report type:** `H-int_8: CONFIRMED (PINT PASS supplied
by this gate); (i)_8: CONFIRMED; inherited DETECTOR-ONLY caveat: CLOSED`.
If the whole-cone W certificate and its logic pass, the final verdict may
be **(T)_8 CONFIRMED**, without an `(i)_8` condition. A second successful
prime strengthens the computational replication record but is not
necessary for the mathematical direction of this properness implication.

No ledger was written; no fleet instance was launched for this subtask;
only notes/artifacts under the authorized gate box were created. No new
exit-price assertion is made, so no charge_basis line is applicable.
