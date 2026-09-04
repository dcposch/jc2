# K = 16 terminal cone: weighted Hilbert series, regular sequences, and full weighted initial ideals

Date: 2026-09-03--04  
Lane: proof-attack (global terminal-cone statement)  
Verdict: **PARTIAL** -- the literal regular-sequence proposal is impossible,
the fixed range is strengthened, but the all-`t` statement is not proved.

## 1. Scope, conventions, and charged-input integrity

This report studies the global homogeneous cone ideal, not any sub-chart:

```text
A_t = Q[y]/(H_t),
H_t = 12(2t+1)^2 y^2 - 12(2t+1)(t+1)y + (t+1)(3t+2),
S_t = A_t[b4,q2_0,...,q(t-1)_0,b3],
I_(t,+) = <T_(t,1),...,T_(t,2t-1)>.
```

Writing `d=2(2t+1)y-(t+1)` gives `3d^2=t+1`.  On a geometric
fibre the coefficient ring is a field.  The rational algebra splits exactly
when `t=3s^2-1`; among `t=3,...,8` there is no split index, while `t=2`
has the two factors `y=1/5,2/5`.  This is the fibre convention of
`k16-cone-gate-gpt55-20260903.md:43-61`.

There are exactly

```text
1 + (t-2) + 1 = t
```

polynomial variables.  Each reported length is a vector-space dimension over
the coefficient field of that run.  For an exact nonsplit index this is the
field `A_t`, its length agrees after passage to either geometric fibre, and
the underlying `Q`-dimension is twice as large.  A modular length is only the
length over the displayed finite field.

The exact Singular order used for every new prompt-order result is

```singular
ring S=K,(b4,q2_0,...,q(t-1)_0,b3),wp(1,2,...,t-1,t+1);
```

where lowercase `wp` is weighted reverse lexicographic, including its
reverse-lex tie-break.  In this report `in_wp(I)` means the monomial ideal
`minbase(lead(std(I)))` in that exact ordered ring.  It is not merely the
weight-filtration initial form.

Before any computation, the receipt
`xmodel/k16-hilbert-regseq-sol56-20260903.run.v2` was parsed mechanically:
an `awk` program paired its `charged_input_i_sha256` and
`charged_input_i_basename` fields and produced
`box/k16hilb-20260903/charged_inputs.sha256`.  A direct `sha256sum -c`
returned `OK` on all 16 lines; the unedited transcript is
`charged_inputs.check`.  No digest was retyped.

## 2. Construction of the homogeneous cone ideals

The drivers implement the closed indexed coefficient-array construction, not
interpolation.  In the notation of the charged source it forms `U,C`, their
translated coefficient arrays, the convolutions `B,S,V,Y,Z,N,P0',R`, solves
the `2t+1` high variables successively by their proved nonzero diagonals, and
then extracts

```text
T_(t,k) = - sum_(m>=k) binom(m,k)(-b4)^(m-k) R_m,
0 <= k < 2t.
```

See `k16-terminal-proof-sol56-20260903.md:78-226`.  The frozen JSON family
uses the overall-opposite convention for `R` from one earlier report; this
does not change any generated ideal.

The symbolic grading check gives

```text
wt(b4)=1, wt(qj_0)=j, wt(b3)=t+1,
deg_wp T_(t,k)=4t+1-k                 (1 <= k <= 2t-1).
```

Thus the positive-row degrees are `4t,4t-1,...,2t+2`.  The
recurrence-generated accepted jobs check homogeneity and this degree before
the standard-basis call.  The preexpanded wrappers preserve the already
checked row expressions byte-for-byte; the final target-assisted wrapper also
repeats the checks.  Band zero is excluded: it has a nonzero constant part
and is not homogeneous.

For modular work I used `p=1009`.  It satisfies `p>8t+3` throughout the
range.  The split roots of `H_t mod p` are

| `t` | roots modulo 1009 |
|---:|---|
| 3 | `632, 810` |
| 4 | `468, 990` |
| 5 | `433, 760` |
| 6 | `380, 940` |
| 7 | `400, 475` |
| 8 | `64, 352` |

The metadata checks the chosen root, `y`, `g`, `yg`, and each of the `2t+1`
high pivots for nonvanishing.  Both roots were evaluated at `t=3,...,6`;
the two modular `t=3` transcripts are diagnostic because a later parser error
taints their clean-exit status, while the exact `t=3` computation is accepted.
The `t=4,...,6` pairs are clean.  One root is enough at the nonsplit rational
indices for the properness dimension certificate because the two modular
roots are two embeddings of the same characteristic-zero quadratic field;
this says nothing about equality of modular lengths.  At a rationally split
index both characteristic-zero factors would be mandatory.  A final `t=8`
fallback used the also-good prime `p=73`, roots `34,61`, at `y=34`; it had
`g=38`, `yg=51`, all 17 pivots nonzero, and two independent point checks.

## 3. Weighted Hilbert series and quotient lengths

Put

```text
D_t(s)=(1-s) product_(j=2)^(t-1)(1-s^j) (1-s^(t+1)).
```

For a completed standard basis `G`, Singular's `hilb(G,1,WTS)` produced the
numerator `N_t(s)`.  The independent decoder exactly divided `N_t` by `D_t`,
required zero remainder, and checked that the coefficient sum equals
`vdim(G)`.  The useful object is the terminating polynomial

```text
P_t(s)=N_t(s)/D_t(s)=sum_n h_(t,n)s^n.
```

The eventual Hilbert polynomial of every Artinian quotient here is simply
zero; `P_t` is the finite weighted Hilbert-series polynomial requested in the
lane.  `hilb(G,2,WTS)` is *not* that polynomial and is not used.

The completed full-cone results are:

| `t` | field/run | `dim` | `deg P_t` | fibre length | logical type |
|---:|---|---:|---:|---:|---|
| 3 | exact `A_3` | 0 | 14 | 66 | characteristic zero |
| 4 | exact `A_4` | 0 | 21 | 338 | characteristic zero |
| 5 | `F_1009`, both roots | 0 | 30 | 1709 | modular length; char-0 dimension only |
| 6 | `F_1009`, both roots | 0 | 39 | 8621 | modular length; char-0 dimension only |
| 7 | `F_1009`, root 400 | 0 | 49 | 43133 | modular length; char-0 dimension only |
| 8 | good fibres at `p=1009,73` | OPEN | OPEN | OPEN | no completed standard basis |

The coefficient vectors are recorded without compression in
`t3_exact_full_hilbert.json`, `t4_exact_full_hilbert.json`, and
`t{5,6,7}_mod_p1009_b0_full_hilbert.json`.  For compact reference:

```text
P3=[1,1,2,2,4,4,6,6,8,7,8,6,6,3,2]

P4=[1,1,2,3,4,6,8,10,13,16,19,22,25,27,29,30,29,28,25,20,14,6]

P5=[1,1,2,3,5,6,10,12,17,21,28,33,43,49,60,68,80,87,100,
    105,115,118,124,120,121,109,100,80,61,29,1]

P6=[1,1,2,3,5,7,10,14,19,25,33,42,54,67,83,101,122,145,171,
    199,230,262,296,330,365,399,431,460,485,504,516,519,512,493,
    460,413,349,269,170,54]

P7=[1,1,2,3,5,7,11,14,21,27,37,47,63,78,101,124,156,188,232,
    275,333,390,462,534,624,710,816,917,1037,1150,1282,1400,1537,
    1655,1786,1893,2009,2089,2174,2214,2249,2230,2198,2099,1981,
    1786,1560,1251,906,468].
```

At `t=8`, direct `std`, `groebner`, and `slimgb` routes and corrected
Hilbert-guided routes in both variable orders reached their 1800-second caps
before a standard basis or even the separately instrumented finite seed was
printed.  The `p=73` retries did the same.  Thus no `t=8` dimension, Hilbert
polynomial, or length is inferred from these runs.

### A uniform length conjecture

All five full coefficient vectors, not just their sums, equal the strictly
positive prefix

```text
F_t(s) = [ product_(d=2t+2)^(4t)(1-s^d) / D_t(s) ]_+,
```

where `[sum a_n s^n]_+` stops immediately before the first coefficient
`a_n<=0`.  An independent Gaussian-binomial calculation uses

```text
R_t(s) = [4t choose 2t-1]_s (1-s^t)
         product_(j=t+2)^(2t-1)(1-s^j)
```

and gives for `t=8` a first nonpositive coefficient `a_62=-844`, last
positive coefficient `a_61=1228`, and candidate length

```text
L_8^Fr = 215702.
```

The corresponding candidate (not an actual `t=8` quotient series) is

```text
P8^Fr=[1,1,2,3,5,7,11,15,21,29,39,51,68,87,112,142,179,222,276,
337,411,497,597,711,845,994,1165,1357,1572,1809,2075,2362,2678,
3020,3388,3779,4198,4634,5091,5564,6047,6534,7025,7503,7967,
8407,8809,9163,9462,9684,9820,9858,9775,9560,9200,8672,7963,
7064,5949,4613,3044,1228].
```

This is the **weighted-Froberg conjecture for this row family**, not a proof
of the actual `t=8` value.  The exact raw-series recurrence and a uniform
partition/subset formula are in `froberg_audit.md`; the nonlinear first-sign
cutoff gives no proved scalar recurrence for the lengths.  In particular,
the observed list

```text
66, 338, 1709, 8621, 43133
```

is evidence for `F_t`, not an interpolated all-`t` theorem.

## 4. Highest-weight-row regular-sequence test and corrected search

There is a structural off-by-two obstruction in the proposed test.  The band
interval written in the prompt,

```text
k=t-2,...,2t-1,
```

contains `t+2` rows and has actual degrees

```text
3t+3,3t+2,...,2t+2.
```

It is therefore the bottom tail plus two rows, not the highest-weight
`t+2` rows.  More decisively, `S_t` has dimension `t`.  Its positive-degree
rows vanish at the origin, so their ideal is proper, and no regular sequence
of length `t+2` can exist.  The hypothetical quotient series

```text
product_(d=2t+2)^(3t+3)(1-s^d) / D_t(s)
```

has a zero of order two at `s=1`; a nonzero graded quotient has either a
positive value there (finite length) or a pole (positive dimension).  Hence
equality is impossible for every `t` and every fibre.  The same height
argument also disposes of the genuinely highest-weight choice
`k=1,...,t+2`, and it makes a greedy search for *any* `t+2` rows vacuous.

Direct tests of the literal interval agree with the theorem:

| `t` | selected rows | `dim` | fibre length | CI-numerator equality |
|---:|---|---:|---:|---|
| 3 | `1,...,5` | 0 | 66 | no |
| 4 | `2,...,7` | 0 | 359 | no |
| 5 | `3,...,9` | 0 | 2001 | no |
| 6 | `4,...,11` | 0 | 11354 | no |
| 7 | `5,...,13` | not obtained (1800 s) | not obtained | no, by height theorem |
| 8 | `6,...,15` | not obtained (retired at 743 s) | not obtained | no, by height theorem |

These ideals can be zero-dimensional; they are simply not complete
intersections and their `t+2` displayed generators are not a regular
sequence.

The dimensionally meaningful repair is the `t`-row tail

```text
J_t^tail=<T_(t,t),...,T_(t,2t-1)>,
degrees 3t+1,3t,...,2t+2.
```

Whenever this ideal is zero-dimensional, its `t` homogeneous generators are
an hsop in the Cohen--Macaulay polynomial ring, hence a regular sequence.  Its
then-forced Hilbert series and length are

```text
Hilb(S_t/J_t^tail;s)
  = product_(d=2t+2)^(3t+1)(1-s^d) / D_t(s),

L_t^tail = product_(d=2t+2)^(3t+1)d / ((t-1)!(t+1))
         = t/(t+1) binom(3t+1,t).
```

The direct equality test succeeds at `t=3,...,6`, with selected rows and
lengths

| `t` | rows | field | `dim` | length | verdict |
|---:|---|---|---:|---:|---|
| 3 | `3,4,5` | exact | 0 | 90 | regular sequence |
| 4 | `4,5,6,7` | exact | 0 | 572 | regular sequence |
| 5 | `5,...,9` | mod 1009 | 0 | 3640 | regular sequence after properness + CM |
| 6 | `6,...,11` | mod 1009 | 0 | 23256 | regular sequence after properness + CM |
| 7 | `7,...,13` | mod 1009 | not obtained (1800 s) | not obtained | OPEN |
| 8 | `8,...,15` | mod 1009 | not reached incrementally | not obtained | OPEN |

The last two characteristic-zero CI conclusions do not promote a modular
length by fiat: properness first proves characteristic-zero dimension zero,
and Cohen--Macaulayness then independently forces the characteristic-zero CI
series from the row degrees.

## 5. Full weighted initial ideals and pure-power certificates

For each completed prompt-order run, the entire minimal monomial basis was
written both as monomials and as exponent vectors, then checked for contiguous
indices, arity, componentwise-divisibility antichain, count, and pure-power
minima.  The complete lists are the `*_full_initial_ideal.tsv` artifacts; it
would be both error-prone and far beyond the report budget to inline thousands
of monomials.

| `t` | field | minimal generators | least pure-power exponents in `(b4,q2,...,b3)` order |
|---:|---|---:|---|
| 3 | exact | 20 | `(8,6,4)` |
| 4 | exact | 81 | `(10,7,6,5)` |
| 5 | mod 1009 | 340 | `(12,8,7,7,6)` |
| 6 | mod 1009 | 1391 | `(14,10,8,8,7,6)` |
| 7 | mod 1009 | 5830 | `(16,11,9,8,8,8,7)` |
| 8 | `p=1009,73` attempts | OPEN | OPEN |

Thus the full `in_wp(I_(t,+))` contains a power of every variable throughout
the completed range, and this is an order-internal certificate of dimension
zero.  The measured `b4` exponent is `2t+2`.  The other columns do not yet
support a proved formula in `t`; in particular, their short sequences should
not be smoothed into the already-refuted pattern from the prior report.

The older computations used

```text
(b3,b4,q2,...),wp(t+1,1,2,...),
```

so their minimal bases and pure exponents legitimately differ, although the
Hilbert series agrees in every overlap `t=3,...,7`.  The earlier failed
dimensions `2,3,3,4` are still less relevant: those were ideals generated by
initial forms for the coarse sub-chart weight `0` on survivor variables and
`1` off the chart.  They were neither this order nor the full lead ideal of a
standard basis (`k16-subchart-q-opus5-20260903.md:531-544`).

## 6. Uniform leading-form attack

Every term of `T_(t,k)` has the same weighted degree.  Consequently the pure
weight initial form is the whole row:

```text
in_weight(T_(t,k))=T_(t,k).
```

Only the reverse-lex tie-break in Singular's `wp` chooses a monomial.  Define

```text
mu_(t,k)=T_(t,k)(b4=1,q2_0=...=q(t-1)_0=b3=0).
```

This is exactly the coefficient of `b4^(4t+1-k)`.  Since `b4` is the first
variable, that pure power is the greatest monomial of the fixed weighted
degree.  Therefore the exact symbolic statement is

```text
mu_(t,k) != 0  ==>  LM_wp(T_(t,k))=b4^(4t+1-k).       (6.1)
```

Without the nonvanishing hypothesis, the leader is the supported exponent
vector whose reversed tail
`(a_b3,a_(t-1),...,a_2)` is lexicographically smallest, with `a_b4` forced by
the weight equation.  The closed recurrence computes `mu_(t,k)`, but its
depth grows with `t`; the charged reports conflict between a stated pure-power
attainment and the later admission that no uniform nonvanishing certificate
for these growing axis coefficients was obtained.  Under the FALLACY-v2
floor/attainment rule, (6.1) is unconditional only after a fixed-fibre unit
check, and remains conditional uniformly.

Even granting all those units, the hoped-for proof collapses for a simpler
reason: all original-row leaders are powers of the same variable.  At each
fixed checked index `t=3,...,7` (and uniformly conditional on all the
`mu_(t,k)` being units),

```text
<LM(T_(t,1)),...,LM(T_(t,2t-1))>=(b4^(2t+2)),
```

so no two selected rows have coprime leaders and this monomial ideal has
dimension `t-1`.  The powers of `qj_0` and `b3` in Section 5 arise only from
leaders of Buchberger `S`-polynomials:

```text
<LM(original rows)>  is strictly contained in  in_wp(I_(t,+)).
```

The sharp uniform target for `(V0)` is therefore an indexed construction of
`F_x in I_(t,+)` for every residual variable with a unit coefficient and
`LM_wp(F_x)=x^(a_x(t))`, or, more strongly, a proof of the weighted-Froberg
maximal-rank conjecture.  The latter controls the complete Hilbert function,
whereas pure powers alone control dimension.  Neither follows from weighted
support, the original row leaders, or the finite tables.  No all-`t` proof
results here.

## 7. The t = 2 fibre controls

Both rational fibres were computed exactly in the prompt order, with
`D_2=(1-s)(1-s^3)`.

At `y=1/5`,

```text
N_(2,-)=1-s^6-s^7-s^8+s^9+s^10,
Hilb=N_(2,-)/D_2
    =1+s+s^2+2s^3+2s^4+2s^5+2s^6+s^7
     +(s^9+s^10)/(1-s^3).
```

The series does not terminate, `dim=1`, and

```text
in_wp(I_(2,+))=(b4^6,b4^4*b3,b4^2*b3^2),
```

so there is no pure `b3` power.  This is the required negative control.

At `y=2/5`,

```text
N_(2,+)=1-s^6-s^7-s^8+s^10+s^11,
Hilb=1+s+s^2+2s^3+2s^4+2s^5+2s^6+s^7,
dim=0, length=12.
```

The minimal lead ideal has four generators and least pure powers
`b4^6,b3^3`.  The older values `b4^8,b3^2` came from the reversed variable
order and are not contradictory.  Notably, degree data alone predict the
same Froberg length 12 on both fibres, while the first fibre is actually
one-dimensional; this is a sharp control against promoting the conjecture
from degrees.

## 8. Characteristic-zero interpretation and FALLACY-v2 audit

The charged properness lemma applies to a homogeneous ideal in a positively
graded polynomial ring over a local domain: if one good special fibre has
only the cone vertex, then the generic fibre does too.  Here that is
equivalent to dimension zero and also to a pure power of every variable in a
full monomial initial ideal.  The emitted metadata supplies the required
denominator/pivot checks, and every accepted output was scanned for Singular's
nonfatal division-by-zero/error messages.

The lemma is one-directional and contains no flatness assertion.  It promotes

```text
modular dim=0  ==>  characteristic-zero dim=0,
```

but does **not** identify modular and characteristic-zero Hilbert functions
or lengths.  Accordingly `1709,8621,43133` are reported as modular fibre
lengths even though they certify characteristic-zero `(V0)` at their fixed
indices.  The exact values `66,338` need no promotion.  Section 4's tail CI
argument is separately justified by properness plus Cohen--Macaulayness.

No flag, exit set, or exit price is asserted in this report, so the
FALLACY-v2 `charge_basis` line is inapplicable.  No saturation, ambiguous ring
map, or raw normal-form claim is used.  The full order, coefficient field,
variable order, and fibre are printed in every accepted transcript.

## 9. Verdict and dependency chain

The requested verdict **`(V0) for all t>=3 PROVED` is not reached**.

What is proved is:

```text
(V0) = dim I_(t,+)=0 in characteristic zero for t=3,...,7;
the literal t+2 regular-sequence proposal is impossible for every t;
the corrected tail is a regular sequence for t=3,...,6;
the all-t weighted-Froberg identity and all-t pure-power containments are OPEN.
```

For each fixed proved index, the banked dependency is

```text
(V0)
  => homogeneous cone is only the origin
  => tau_t vanishes on it and band-zero constant is nonzero
  => terminal unit statement (8.1)
  => banked constant spine
  => banked normalizer lemma
  => banked second affine spine
  => theorem (T) at that t.
```

At `t=2,y=1/5`, `(V0)` fails but (8.1) still holds by the weaker radical
criterion; the `y=2/5` fibre satisfies `(V0)`.  With the separately banked
small indices, the present certified chain reaches theorem (T) only through
the fixed range, not all `t>=1`.  The exact residual statement for a global
promotion is an indexed full-initial-ideal/pure-power construction (or a
uniform maximal-rank theorem), not another sub-chart radical membership.

## 10. Reproducibility artifacts

All new files are under `box/k16hilb-20260903/`.  Principal drivers and audits:

```text
emit_hilbert_job.py              closed-recurrence exact/modular emitter
emit_preexpanded_cone_job.py     requested/legacy/alternative-engine wrapper
decode_hilbert.py                exact weighted-denominator division
froberg_series.py                positive-prefix candidate
extract_initial_ideal.py         full minimal-basis validator/TSV writer
source_audit.md                  charged-source theorem/citation audit
symbolic_audit.md                wp leader and height-obstruction audit
computation_audit.md             clean/tainted/output consistency audit
froberg_audit.md                 independent q-binomial candidate derivation
initial_ideal_validation.md      complete-list validation summary
report_audit.md                  independent final logic/evidence audit
artifacts.sha256                 deterministic directory manifest
artifact_summary.json            byte counts and SHA-256 records
```

Every Singular invocation in this lane ran in the foreground under
`timeout 1800`; no job used more than one core, and at most three lane jobs ran
concurrently.  `.resource` files record wall time, maximum RSS, and exit
status.  Completion marker, empty stderr, zero resource exit, and a clean error
scan are necessary acceptance conditions.  A Hilbert-guided run additionally
requires an independently known target or a target-free re-standardization;
the early `t8_mod_p1009_b0_requested_target` run is explicitly excluded.  It
omitted Singular's terminal Hilbert-vector bookkeeping zero and therefore
stopped circularly after one generator.  The full initial-ideal lists are kept
as TSV artifacts because the completed list already has 5,830 generators at
`t=7`; the optimized exact bitset antichain check validated that entire file in
0.75 seconds and replayed the six earlier TSVs byte-for-byte.

<!-- BODY-END -->
