# Hostile audit of Opus 5 cross-review results `R1`--`R3`

Date: 2026-08-27  
Reviewer: Sol Ultra / Codex  
Target: `xmodel/ideation-20260827T2259Z-fable5-crossreview-opus5.md`,
only §§5.1--5.4 and the custody-drift assertion.  No other claim in that
report is adjudicated here.

No `jc2-lean` path was entered, listed, searched, read, built, statused, or
modified.  No AWS or web access occurred, no canonical file was edited, and
no heavy local computation was run.  The only write is this report.  The
small exact-rational replays used the producer's surviving `/tmp/jc2xr/`
scripts and additional rank calculations in memory.

## 0. Executive verdict

| Atom | Verdict | Promotion consequence |
|---|---|---|
| `R1`: rows `m == 4 (mod 8)`, `m >= 28`, are class-zero | **CONFIRMED, DUPLICATE** | Already independently promoted as the mod-8 class-death consequence of `NU-LAW`; no new credit here |
| `R1`: sector `b=2` is even in `z` | **CONFIRMED WITH WORDING REPAIR** | Promote as a free coefficient/certificate replay check; an arbitrary nonminimal annihilator need not display parity visibly |
| `R2`: seed-23 prefix and residue table | **CONFIRMED** | Exact finite `r=1`, degree-5 fixture |
| `R2`: displayed seed-23 Jacobian ranks | **CONFIRMED numerically; interpretation repaired** | The ranks also survive restriction to the prefix tangent space, but prove only a finite generic-rank statement on that toy chart |
| `R2`: seed-11 “same picture” | **REFUTED at the last two ranks after correct tangent restriction** | Correct restricted tail is `...,6,6,6`, not `...,6,7,7` |
| `R2`: nonlinear rows “keep cutting” / attack repricing | **GAP / NOT LICENSED** | No successive upper-survivor locus, branch-P point, or infinite independence was tested |
| `R3`: closed form | **CONFIRMED** | Promote as an exact toy-control identity |
| `R3`: eight-step recurrence | **CONFIRMED WITH CANCELLATION REPAIR** | Promote the primitive degree-7 relation below |
| `R3`: four fitted order-2, degree-7 operators | **CONFIRMED as identities; REFUTED as independent corroboration** | They are the same eight-step relation after `n=b+4k`, and the fitter's input literally uses the closed form |
| `R3`: unsectioned negative search | **MISREPORTED / NO EVIDENCE** | Surviving script searched `(order <= 4, degree <= 6)`, not the claimed `(<=6,<=8)`; an exact order-8 recurrence is already known |
| `R3`: `N0=30` | **VALID SUFFICIENT ROW CUTOFF, NOT A COEFFICIENT-INDEX `N0`, AND NONMINIMAL AT THIS POINT** | Useful only as proof-of-method; the fixture already fails row 23 |
| “round custody defect” | **FALSE; harmless to `R1`--`R3`** | The promise lasted until the four blind submissions sealed, and the canonical edits occurred afterward |

## 1. Hashes and replay basis

Core files read:

```text
e9f2a333ef94161e3e9c54288e4e06ed1047ee7a9c93254811787e6a2d517090  xmodel/ideation-20260827T2259Z-fable5-crossreview-opus5.md
8e1fbde0b1a0d0a0e6f397e11a02bb4cdc2ba85640bce403248b776e7e8e2f83  xmodel/ideation-20260827T2259Z-fable5-crossreview-opus5-prompt.md
8674f511a6a88801818c7ffda5f1fdfa52ac57e871e72757234a5d0a28291240  xmodel/ideation-20260827T2259Z-packet.md
d53c352d1e2bea8ae9c2b6e607c8224897d592718ee7297224d753c3c2814db2  xmodel/ideation-20260827T2259Z-fable5.md
34ccbed9b69540e7ff96e1da9b3027383f707bf5c50a016eda3cae7e1135d912  xmodel/ideation-20260827T2259Z-synthesis-sol.md
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md
71befadb3496f5f6c8e3136e7019de95dec2f205f2655734eac2c84d8e0e24d1  xmodel/ggv-quarter-root-sector-gate-rec-theorem-r8-sol-ultra-20260827.md
```

The `2259Z` synthesis hash is its present post-round hash, not a packet input.
The producer's surviving exact scripts, all read in full, hash as follows:

```text
5a79555197afc14a51a9ea6422d473bb5cf5c18b99b681a41a7297c8f4e10ffc  /tmp/jc2xr/r1check.py
8b6cd363ffe6c2e335a0fcc05476c2e99c8e0ca4b922ea4570a70f4bab0d8062  /tmp/jc2xr/fixture.py
4852a63b0274c6f472284ecbc7e25853b85690186da92053e0c7c08505ac0fa2  /tmp/jc2xr/ratio.py
37639fcbd254a3ed11446fa1cf71715e558d6594704cda9e6554de982f955d2d  /tmp/jc2xr/precfit.py
986c1faa76353e044ea814e0effbf5d1fe0864545e406d8cdc01906fc285d680  /tmp/jc2xr/r1tower_b.py
d31e12da965fd8df98327074a4ba26ee3a4b2e2d1c8f587d2afb00772ff7f633  /tmp/jc2xr/r1tower.py
7681d52b8df3f75c413be0ad8ede02f22fb732a8945e62829406e08a4399dd0d  /tmp/jc2xr/precfit_sec.py
19f1c70ba9404566fe6a8f5e6a9c5fd593cd1476898eac3aa88509f0f377f106  /tmp/jc2xr/closed.py
```

For custody chronology only, I also inspected the current ledgers.  Their
late, mutable audit-snapshot hashes were:

```text
a6d0a3ec605dee43c14f9b53e898442c216b7e683529937c8b0a3862e02c123c  APPROACHES.md
99e5feb7e81c7fc4f6fa3d228f0132d8cdcf253ba0a540cd2333b3c6c9f4c4a7  AUDIT.md
0afaba4741ea3eb257322f5893a6fe413100d4239d3334d3c8d80d1d252fc029  COORDINATION.md
f3ddfe9fc529de40ed3469d438f4dbf209114d85d38b10595abd680668e63286  PROGRESS.md
654c358e7c8760fc93ffeb0cfb0ea4fd62163a338195dccba13db865c2c87038  notes.md
```

Those five hashes are not used as mathematical authority.  A broad content
search was accidentally scoped to the repository rather than `xmodel/`; it
was truncated, excluded `jc2-lean`, and supplied no premise or conclusion.

The common exact input is

```text
q_n = 2/(n+2) [t^n] F(X,t)^((n+2)/8).
```

For the `r=1` control `H=X^4`, `p=X`, exactness of row `m=n+22` is exactly
`rho_n := Res_(X=0) q_n = 0`.

One transcription error precedes `R2` in target §4.1.  For general
`H=X^e`, the coefficient exponent is

```text
2 e j - e(n+2)/4 - 1,
```

not `2 e j - e(n+2)/2 - 1`.  The next displayed specializations
`[X^(5-n)]F_n/4` for `e=4` and `[X^(11-2n)]F_n/4` for `e=8`, and all scripts,
use the correct `/4` exponent.

## 2. `R1`: theorem and even-sector consequence

If `n=8N-2 >= 6`, then

```text
q_n = (1/(4N))[t^n]F^N in K[X],
m=n+22=8N+20=4(2N+5).
```

Choose `Phi in K[X]` with `Phi'=q_n` and put
`g=Phi/H^(m/4) in K[X,H^-1]`.  Then

```text
nabla_m(g)=H^(-m/4)d(Phi)=p^(-m)q_n dX.
```

Thus every such row is zero for every `H` and window.  The proof is correct.
The result is not new here: the sealed synthesis records independent
producer/reviewer promotion of the same `NU-LAW` consequence.

For the correctly normalized fixed-receiver section

```text
C_2(z)=sum_(k>=0) [p^(-24)q_(2+4k)dX] z^k in V_24[[z]],
```

odd `k` gives `2+4k == 6 (mod 8)`, so `R1` kills that coefficient.  Hence

```text
C_2(-z)=C_2(z),             C_2(z) in V_24[[z^2]].
```

This is a sound, free mutation/replay invariant.  The wording “any operator
must reproduce it” should mean that an operator **together with its initial
data or exact certificate** reproduces the zero odd coefficients.  A valid
nonminimal annihilating operator need not visibly have even coefficients or
otherwise advertise the symmetry in its printed form.

## 3. `R2`: exact reconstruction and the limit of the experiment

Write `F_i=sum_e a_(i,e)X^e`, take `F_i=0` for `i>=6`, and let
`rho_n=Res_0 q_n`.  For `1<=n<=5`, triangularity is literal:

```text
rho_n = a_(n,5-n)/4 + R_n(F_1,...,F_(n-1)).
```

Therefore the prefix chart `rho_1=...=rho_5=0` is obtained successively by

```text
a_(n,5-n) = -4 R_n.
```

For degree at most five, Python's `random.seed(23)` and integer draws in
`[-4,4]`, followed by those substitutions, give

```text
F1 = -3X - 4X^2 + 2X^5,
F2 = 4 + X - 2X^2 + 3X^5,
F3 = -4 - X + (9/4)X^2 - 4X^3 - 3X^4 - 3X^5,
F4 = 3 - (3/2)X - 4X^2 + 4X^3 + 2X^4 + X^5,
F5 = -1/2 - X - 4X^2 + X^3 - 2X^4 - X^5.
```

The five solved coordinates
`a_(1,4),a_(2,3),a_(3,2),a_(4,1),a_(5,0)` are respectively
`0,0,9/4,-3/2,-1/2`.  Rows `n=1,...,5` are all zero.  Exact replay gives:

```text
n       6       7         8         9          10        11
rho_n   0    -111/512   -75/128   12669/4096  -399/64   2625/512

n       12          13             14       15              16
rho_n   43877/8192  -156387/16384   0       -375777/262144  2259475/32768

n       17                    18
rho_n   -191228235/1048576    162499/1024
```

These are exactly the target's values.  Its dual-number ranks of
`(rho_6,...,rho_K)` in all 30 ambient coordinates also replay:

```text
K       6  7  8  9 10 11 12 13 14 15 16 17 18
rank    0  1  2  3  4  5  6  7  7  8  9 10 11.
```

The script differentiates after replacing the five solved coordinates by
constants; it does not differentiate their solution formulas.  The correct
rank on the tangent space of the prefix locus is

```text
rank(d(rho_1,...,rho_5,rho_6,...,rho_K))
  - rank(d(rho_1,...,rho_5)).
```

Here the prefix rank is five and, fortunately, the resulting restricted
ranks are the same displayed sequence.  Thus this one exact point certifies
that the eleven functions

```text
rho_7,...,rho_13,rho_15,...,rho_18
```

have generically independent differentials on this irreducible 25-parameter
prefix chart.  In characteristic zero that is a genuine finite algebraic-
independence statement.  In particular these nonlinear carry functions are
not identically, hence not generically, zero on this chart.

The degree-at-most-three seed 11 is less clean.  Row 23 is automatic because
`[X^4]F_1=0`; only rows 24--27 are solved, all four pinned values being zero.
The residues are

```text
n       6   7     8      9      10   11   12   13       14   15        16
rho_n   0  3/8  -3/16  -3/32   3/4   0   5/8  -105/128   0  -135/512   0.
```

The target's **ambient** ranks `0,1,2,3,4,4,5,6,6,7,7` replay.  But the
prefix rank is four and the ranks restricted to its tangent kernel are

```text
0,1,2,3,4,4,5,6,6,6,6.
```

Consequently the second seed does not support the last two advertised rank
increments.  It also disproves the narrative that restricted-rank plateaus
occur exactly when the evaluated residue is zero: `rho_15=-135/512` is
nonzero while its differential adds no restricted rank.

### What `R2` does and does not show

Because `F_i=0` for `i>=6`, every tested `rho_n`, `n>=6`, is indeed pure
nonlinear carry in `F_1,...,F_5`.  Seed 23 therefore gives a valid theorem
about eleven finite functions on one `r=1`, degree-5 prefix chart.

It does **not** show any of the following:

- independence on the common zero locus of the previously imposed upper
  rows (the seed already fails `rho_7`, row 29);
- nonemptiness or expected codimension of a row-28--40 survivor locus;
- infinite row independence;
- the same behavior on branch P, with its different receiver and windows;
- any face, raw-determinant, endpoint, or polynomial-`G` consequence.

Thus “the nonlinear residues do not vanish generically” is confirmed only
for this finite toy chart.  “Rows remain functionally independent and keep
cutting” must be replaced by the eleven-function statement above.  Fable's
optimistic generic-vacuity shortcut is refuted **in this control**, but that
does not license repricing the campaign's branch-P survivor march.  At most
it warns that random-prefix vanishing should not be budgeted as the expected
case before an on-stratum computation.

Promotion verdict for `R2`: **REPAIR before promotion**.  Bank the exact
seed-23 chart, residues, and correctly stated restricted-rank certificate;
discard the seed-11 last two ranks and the program-level repricing.

## 4. `R3`: closed form, recurrence, four-sections, and indices

Let

```text
F=X^8+A(X)t,       A=X^7+X^4+1,
c_n=Res_0 q_n.
```

Only the `n`th binomial term can contribute:

```text
q_n = 2/(n+2) binom((n+2)/8,n) X^(2-7n) A^n.
```

The residue asks for `[X^(7n-3)]A^n`.  Starting from `X^(7n)`, choosing
`b` factors `X^4` and `d` factors `1` gives the deficit equation

```text
3b+7d=3.
```

Its unique nonnegative solution is `(b,d)=(1,0)`, with multinomial
coefficient `n`.  Hence, including `n=0`,

```text
c_n = (2n/(n+2)) binom((n+2)/8,n).                    (4.1)
```

This derivation and the producer's direct check through `n=14` are correct.

Put `a=(n+2)/8`.  Direct falling-factorial division gives

```text
binom(a+1,n+8)/binom(a,n)
 = -(n+10)/8 * prod_(i=0)^6 ((7n-2)/8+i)
   / prod_(i=1)^8(n+i).
```

Combining the prefactor in (4.1) proves the displayed target recurrence.
Its two coefficients have the common factor
`(n+2)(n+8)(n+10)`.  The primitive form is cleaner:

```text
D7(n)c_(n+8) = N7(n)c_n,                              (4.2)

D7(n) = n(n+1)(n+3)(n+4)(n+5)(n+6)(n+7),
N7(n) = -(1/8) prod_(i=0)^6 ((7n-2)/8+i).
```

For `n>=0` the cancellation is harmless.  The only nonnegative root of the
forward coefficient `D7` is `n=0`.  Thus `c_1,...,c_8=0` implies all later
coefficients vanish; `c_0=0` is automatic.

### The four exact section operators

For `s_(b,k)=c_(b+4k)`, `b=0,1,2,3`, substitute `n=b+4k` into (4.2):

```text
A_b(k)s_(b,k) + B_b(k)s_(b,k+2) = 0,                  (4.3)

A_b(k) = (1/8) prod_(i=0)^6 ((28k+7b-2)/8+i),
B_b(k) = (4k+b)(4k+b+1)(4k+b+3)(4k+b+4)
         (4k+b+5)(4k+b+6)(4k+b+7).
```

Each is shift-order two and polynomial degree seven; the shift-one
coefficient is zero.  These factorizations agree, up to one nonzero scalar
per sector, with all four integer operators printed by
`precfit_sec.py`.  `B_0` has the sole nonnegative root `k=0`; `B_1,B_2,B_3`
have none.

This confirms the fitted identities, but not the target's claim of
“independent corroboration” or “no closed form used.”  The fitting script
literally defines its input by (4.1).  It blindly rediscovers a recurrence
from values, but those values are not independently extracted from `F`.
Moreover (4.3) is simply (4.2) sectioned, not separate evidence for R8's
geometric four-section construction.  The target's claim that the fits match
its displayed `D(n)` “exactly” also needs the three-factor cancellation above:
degree seven cannot literally equal the displayed degree-ten coefficient.

The negative unsectioned-search claim has a separate execution-record defect.  The
surviving `precfit.py` loops only over `R<=4`, `D<=6`, while the report says
`R<=6`, `D<=8`.  In any event (4.2) is an unsectioned order-eight recurrence,
so failure below order seven is weak evidence and says nothing about whether
four-sectioning is mathematically necessary.

### Three different `N0` indices

The bounds must not share one unnamed index:

| sector `b` | required section indices | max physical `n=b+4k` | max row `m=n+22` |
|---:|---:|---:|---:|
| 0 | `k=0,1,2` | 8 | 30 |
| 1 | `k=0,1` | 5 | 27 |
| 2 | `k=0,1` | 6 | 28 |
| 3 | `k=0,1` | 7 | 29 |

So the target's sector statements “`b=0` needs `N0=2`, the others `1`” are
correct when `N0` means **section coefficient index `k`**.  The union is
`c_0,...,c_8`; since `c_0` is automatic, rows 23--30 are a sufficient
eight-row test.  Calling that **row cutoff** `N0=30` is valid only after
explicitly changing conventions.  In an unsectioned coefficient convention
the cutoff is `n=8`.

At this particular fixture `c_1=1/4`, so it already fails row 23.  Its
minimal fixed-point survival decision cutoff is therefore row 23, not 30.
The useful content is the exact derivation of (4.1)--(4.3), including how a
singular forward coefficient changes the prefix.  It is a clean
proof-of-method fixture, but it is not a nontrivial surviving example, not a
campaign-wide `N0`, and not evidence that the recurrence machinery has
decided a previously undecided point.

Promotion verdict for `R3`: **PROMOTE WITH REPAIRS as a toy proof-of-method**.
Promote (4.1), the primitive recurrence (4.2), the factored sector operators
(4.3), and the three-way index translation.  Do not promote the claimed
independence of the fit, the misstated negative-search box, or the suggestion
that this dead-at-row-23 point supplies substantive campaign finite control.

## 5. Custody adjudication

Packet §1 says the named canonical files “will not be mutated until all blind
submissions seal.”  The sealed synthesis explicitly records that Sol,
Fable5, Opus5, and Grok46 all passed the corrected hash gate and sealed before
synthesis.  Filesystem chronology also places all four blind outputs before
the subsequent canonical writes and before the cross-review assignment.

Therefore the target's observation was a **post-seal hash difference**, not
a breach of the packet promise.  “That is false as of this session,” “a blind
round whose custody set mutates mid-flight,” and “re-pin before crediting any
lane in this round” are false temporal inferences.  The packet did not promise
immutability through later synthesis or cross-review.

The mistake is harmless to `R1`--`R3`: their proofs/replays use the immutable
submission, R7R1/R8 artifacts, and exact local arithmetic, not a disputed
canonical byte sequence.  The target also disclosed the late hashes and
caveated its canonical comparisons.  No blind submission should lose credit
and no round re-pin is required.  A later reviewer should simply hash the
actual post-seal sources it uses, exactly as a new review-custody snapshot.

## 6. Final promotion ledger

1. `R1`: **confirmed but duplicate**; separately bank only the corrected
   sector-even replay invariant if it is not already canonical.
2. `R2`: **repair required**; bank the seed-23 prefix fixture and its
   eleven-function generic-rank certificate at `r=1`/degree-5 scope.  Do not
   bank the seed-11 terminal ranks, survivor-locus language, or branch-P
   attack repricing.
3. `R3`: **promote only as a toy proof-of-method**, using the primitive and
   factored operators and explicit index conventions.  Reject its purported
   independent-fit evidence and campaign-`N0` significance.
4. Custody: **no `2259Z` blind-round defect**; the reported drift occurred
   after the promised seal boundary and is mathematically harmless here.
