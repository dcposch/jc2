# Symbolic audit: `wp` leaders and the proposed regular sequence

Scope: frozen charged inputs only for mathematical claims, plus the official
Singular definition of `wp`.  No Singular calculation was run for this memo.
The receipt-derived 16-line manifest was checked with `sha256sum -c`; all 16
frozen inputs returned `OK`.

## 1. There are `t`, not `t+2`, residual variables

On a geometric fibre of

```text
A_t = Q[y]/(H_t)
```

the coefficient ring is a field (or one field factor at a split index); see
`k16-cone-gate-gpt55-20260903.md:45-60`.  The residual polynomial ring is

```text
R_t = K[b4,q_(2,0),...,q_(t-1,0),b3].
```

It has `1+(t-2)+1=t` variables and Krull dimension `t`.  The same ring and
weights are declared in `k16-terminal-proof-fable5-20260903.md:274-277`, and
the frozen emitter independently constructs exactly the residual list
`b3,q2_0,...,q(t-1)_0` at
`singular_terminal_driver.py:102-107`.

The requested band interval

```text
k = 2t-1, 2t-2, ..., t-2
```

has `t+2` rows.  Since
`deg_w(T_(t,k))=4t+1-k`
(`k16-terminal-proof-sol56-20260903.md:228-240`), their actual degrees are

```text
2t+2, 2t+3, ..., 3t+3.
```

Thus these `t+2` positive-degree elements cannot be a regular sequence in
`R_t`.  This is formal: a regular sequence in a polynomial ring of dimension
`t` has length at most `t`.  The ideal is proper because every positive-degree
homogeneous row vanishes at the origin.

The proposed complete-intersection series makes the contradiction visible:

```text
             product_(d=2t+2)^(3t+3) (1-s^d)
H_hyp(s) = -------------------------------------------------- .
           (1-s)(product_(j=2)^(t-1)(1-s^j))(1-s^(t+1))
```

At `s=1` its numerator has vanishing order `t+2` and its denominator order
`t`, so `H_hyp` has a zero of order two.  It cannot be the Hilbert series of a
nonzero graded quotient: an Artinian quotient has `H(1)=length>0`, while a
positive-dimensional quotient has a pole.  Consequently:

* the named `t+2` rows never form a regular sequence, for any `t` or fibre;
* no search for **any other `t+2` rows** can succeed;
* if a computation appears to match that product, the ring/series parsing is
  wrong.

The natural corrected candidate is the actual top tail

```text
T_(t,t),...,T_(t,2t-1),
```

which has exactly `t` rows.  It is precisely `Jt` in the frozen test emitter
(`analyze_rows.py:41-43`).  If this ideal is zero-dimensional on a fibre, then
these `t` homogeneous elements are an hsop and, because `R_t` is
Cohen--Macaulay, automatically a regular sequence.  Its predicted series and
length are

```text
H_top(s) = product_(d=2t+2)^(3t+1)(1-s^d)
           / ((1-s) product_(j=2)^(t-1)(1-s^j) (1-s^(t+1))),

L_top(t) = product_(d=2t+2)^(3t+1)d / ((t-1)!(t+1))
         = t/(t+1) * binomial(3t+1,t).
```

For `t=3,...,8`, this conditional CI length is respectively
`90, 572, 3640, 23256, 149226, 961400`.  These are lengths of the top-tail
quotient only; they are not predictions for the quotient by all positive
rows.

## 2. What Singular's `wp` means here

The official Singular manual defines lowercase `wp(a_1,...,a_n)` as the
global **weighted reverse lexicographical** ordering; uppercase `Wp` is the
weighted lexicographical ordering:
<https://www.singular.uni-kl.de/index.php/singular.pdf>, chapter 3,
"Monomial orderings".  The order requested in this lane is therefore

```text
(b4,q_(2,0),...,q_(t-1,0),b3),  wp(1,2,...,t-1,t+1).
```

For equal weighted degree, reverse lex scans exponent vectors from the last
variable to the first; at the last differing position, the monomial with the
smaller exponent is the larger monomial.  In particular, among monomials of
weighted degree `D`, `b4^D` is the greatest one.

This tie-break is essential.  Every term of a fixed positive row has the same
weighted degree

```text
D_(t,k)=4t+1-k;
```

the indexed proof is in
`k16-terminal-proof-sol56-20260903.md:228-263` and the array weights are
independently audited in `k16-cone-gate-gpt55-20260903.md:96-122`.
Therefore the weight comparison itself never distinguishes two terms of a
row.  There are two notions that must not be conflated:

```text
weight initial form in_w(T_(t,k)) = T_(t,k)          (all tied terms),
Singular lead under wp              = one monomial    (reverse-lex tie-break).
```

## 3. Exact symbolic description of each row leader

Put

```text
mu_(t,k) = T_(t,k)(b4=1,q_(2,0)=...=q_(t-1,0)=b3=0).
```

Weighted homogeneity shows that `mu_(t,k)` is exactly the coefficient of
`b4^(4t+1-k)`.  Hence, on any fibre on which `mu_(t,k) != 0`,

```text
LM_wp(T_(t,k)) = b4^(4t+1-k).                       (A)
```

Proof: let `m` be any other supported monomial.  At the largest-index
variable among `b3,q_(t-1,0),...,q_(2,0)` occurring in `m`, the exponent of
`b4^D` is zero and that of `m` is positive.  Reverse lex therefore makes
`b4^D` larger than `m`.

Without assuming `mu_(t,k) != 0`, the exact leader is still described by the
support theorem.  Among exponent vectors satisfying

```text
(t+1)a_b3 + a_b4 + sum_(j=2)^(t-1) j a_j = 4t+1-k,
```

and having nonzero coefficient, choose the vector for which

```text
(a_b3,a_(t-1),a_(t-2),...,a_2)
```

is lexicographically smallest.  The `b4` exponent is then forced by the
weight equation.  That monomial is `LM_wp(T_(t,k))`.

The closed recurrence really does define `mu_(t,k)`: the coefficient arrays
and high affine solve are equations (2.2)--(2.13) at
`k16-terminal-proof-sol56-20260903.md:86-225`; the executable version solves
weights `1,...,2t+1` and returns all terminal rows at
`terminal_array_recurrence.py:145-188`.  In particular, this is an indexed
sequence, not an interpolation.

There is, however, a fibrewise nonvanishing issue.  The Fable report states
`deg_b4 T_(t,k)=4t+1-k` and calls the pure power present
(`k16-terminal-proof-fable5-20260903.md:142-154`).  Taken literally over a
field, that assertion gives (A).  At a split index, though, a nonzero
coefficient in `A_t=K x K` may vanish on one factor; a uniform fibrewise
leader needs `mu_(t,k)` to be a unit, equivalently a nonzero norm.  The charged
subchart report certifies all these units only at fixed `t=3,...,7`, and
explicitly labels that check record-based and nonuniform
(`k16-subchart-q-opus5-20260903.md:495-510`).  The Fable report likewise says
the deeper `b4`-axis coefficients are growing, `t`-indexed sequences outside
its fixed-weight uniformity theorem
(`k16-terminal-proof-fable5-20260903.md:217-270`).

Thus the safe statement is:

```text
PROVED, fixed t=3,...,7 and every positive row:
    LM_wp(T_(t,k)) = b4^(4t+1-k).

UNIFORM, conditional on the exact residual unit statement:
    N_A_t/Q(mu_(t,k)) != 0 for all t>=3 and 1<=k<=2t-1.
```

The second line is not supplied by the displayed closed recurrence.  The
grading supplies the possible term and the exponent; it does not by itself
supply coefficient nonvanishing.  This is exactly the floor/attainment
distinction required by `FALLACY-v2.md:14-15`.

## 4. Consequence: the proposed coprime-leader proof cannot work

For the fixed certified range, every original row leader is a power of the
same variable `b4`.  Hence no two of them are coprime.  More sharply,

```text
< LM_wp(T_(t,1)),...,LM_wp(T_(t,2t-1)) >
    = (b4^(2t+2)),
```

and the same equality holds for the requested `t+2`-row band interval.  This
monomial ideal has dimension `t-1`, not zero.  Therefore neither the `t+2`
set nor even a corrected `t`-row subset can be proved regular by pairwise
coprime leaders in this variable order.

This does **not** conflict with a zero-dimensional full initial ideal.  In
general

```text
<LM(T_(t,k)) : original rows>  subsetneq  in_wp(I_(t,+))
             = <LM(g) : g in std_wp(I_(t,+))>.
```

When `I_(t,+)` is zero-dimensional, Buchberger `S`-polynomials must create
leaders involving the other variables, and the resulting monomial ideal
contains a pure power of every variable.  The frozen Fable initial-ideal
pattern cannot be reused: its emitter declares variable order
`(b3,b4,q2,...)` (`analyze_rows.py:23-30`), and its reported pattern is at
`k16-terminal-proof-fable5-20260903.md:343-352`.  The present order puts `b4`
first.  Separately, the failed subchart degeneration used a 0/1 weight that
kept selected residual variables at weight zero, not this `wp` order; see
`k16-subchart-q-opus5-20260903.md:531-544`.

## 5. Sharp uniform target left by this audit

The useful all-`t` proof target is not the leading monomials of the original
rows.  It is an indexed Buchberger/elimination construction of elements

```text
F_b4,F_q2,...,F_q(t-1),F_b3 in I_(t,+)
```

with unit leading coefficients and

```text
LM_wp(F_x)=x^(a_x(t))
```

on every fibre.  Equivalently, prove those pure powers belong to the full
`in_wp(I_(t,+))`.  Fixed modular computations can discover candidate
exponents and, through the charged properness lemma, certify `dim=0` at each
fixed `t`; they do not promote the exponents, Hilbert length, or a Buchberger
recurrence to characteristic zero or to all `t`.  Until such an indexed
construction is supplied, the uniform conclusion remains `OPEN`, while the
`t+2` regular-sequence formulation is formally refuted.
