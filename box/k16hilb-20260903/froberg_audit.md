# Audit of the weighted Froberg candidate

## 1. Exact meaning of the candidate

Put

\[
 W_t=\{1,2,\ldots,t-1,t+1\},\qquad
 D_t=\{2t+2,2t+3,\ldots,4t\},
\]

and let

\[
 R_t(s)=\frac{\prod_{d\in D_t}(1-s^d)}
                 {\prod_{w\in W_t}(1-s^w)}
       =\sum_{n\geq0}a_{t,n}s^n.
\]

Here `[R_t]_+` means the **strictly positive prefix**, not coefficientwise
`max(0,-)`: if

\[
 \nu_t=\min\{n\geq0:a_{t,n}\leq0\},
\]

then

\[
 F_t(s)=[R_t(s)]_+=\sum_{0\leq n<\nu_t}a_{t,n}s^n,
 \qquad L_t^{\rm Fr}=F_t(1).
\]

This is exactly the convention implemented in
`box/k16hilb-20260903/froberg_series.py:33-37,48-56`.

## 2. Comparison with the observed Hilbert functions

An exact coefficient-vector comparison, not merely comparison of coefficient
sums, gives:

| `t` | `nu_t` | `deg F_t` | `L_t^Fr` | observed comparison |
|---:|---:|---:|---:|---|
| 3 | 15 | 14 | 66 | exact `A_3` and both `p=1009` roots: equal |
| 4 | 22 | 21 | 338 | exact `A_4` and both `p=1009` roots: equal |
| 5 | 31 | 30 | 1709 | both `p=1009` roots: equal |
| 6 | 40 | 39 | 8621 | both `p=1009` roots: equal |
| 7 | 50 | 49 | 43133 | clean `p=1009`, root-400 requested-order run and legacy replay: equal |

The candidate data, including the first nonpositive coefficients
`-2,-4,-41,-81,-8`, are recorded at
`froberg_t2_t8.json:50-102,120-192,215-312,341-464,500-652`.
The exact characteristic-zero lengths for `t=3,4` are at
`t3_exact_full_hilbert.json:2,38-39` and
`t4_exact_full_hilbert.json:2,53-54`.  The two-root modular vectors are at
`t3_mod_p1009_b{0,1}_full_hilbert.json:2,38-39`,
`t4_mod_p1009_b{0,1}_full_hilbert.json:2,53-54`,
`t5_mod_p1009_b{0,1}_full_hilbert.json:2,72-73`, and
`t6_mod_p1009_b{0,1}_full_hilbert.json:2,93-94`.  For `t=7`, the vector and
sum are now in both `t7_mod_p1009_b0_full_hilbert.json` and
`legacy_t7_hilbert.json`.  The former comes from the clean new
requested-order recurrence run (`JOB_DONE`, empty stderr, resource `exit=0`);
the latter is a Hilbert replay of the previously recorded monomial lead ideal,
whose underlying cone certificate was the `p=32059`, root `4425` run
(`/tmp/jc2-lane.zmfoKT/inputs/k16-properness-gate-opus5-20260903.md:311-323`).
The two JSON files are byte-for-byte identical.  The new 5,830-generator
initial ideal was also independently parsed and antichain-validated in
`t7_mod_p1009_b0_full_initial_ideal_validation.json`, producing
`t7_mod_p1009_b0_full_initial_ideal.tsv`.

Thus the observed statement is strong at each checked fibre: the **whole
Hilbert function** agrees with `F_t`, not just its length.

## 3. Independent computation of the `t=8` prediction

There is a useful polynomial identity

\[
 R_t(s)= {4t\brack 2t-1}_s(1-s^t)
          \prod_{j=t+2}^{2t-1}(1-s^j),                       \tag{1}
\]

because multiplying the denominator of the Gaussian binomial by
`(1-s^t) product_(j=t+2)^(2t-1)(1-s^j)` leaves precisely the denominator
with weights `W_t`.  Formula (1) also shows that the displayed rational
function is actually a polynomial.

As an independent check of the existing denominator-expansion script, I
computed `{32 bracket 15}_s` from

\[
 {n\brack k}_s={n-1\brack k}_s+s^{n-k}{n-1\brack k-1}_s
\]

and multiplied by `(1-s^8) product_(j=10)^15(1-s^j)`.  The coefficients in
degrees `0,...,61` are positive, the degree-61 coefficient is `1228`, and the
degree-62 coefficient is `-844`.  Their sum is

\[
 \boxed{L_8^{\rm Fr}=215702},\qquad \nu_8=62,\quad \deg F_8=61.
\]

This agrees with `froberg_t2_t8.json:696-799,881-882`.  It is an exact integer
calculation of the **candidate**, independent of Singular; it is not a
measurement of `A_8[b4,q,b3]/I_(8,+)`.

One superficially completed target-guided artifact does not alter that status.
`t8_mod_p1009_b0_requested_target.out` fed the conjectural numerator to
`std(I,H,WTS)` with the required trailing bookkeeping-zero sentinel missing;
the true last coefficient `1228` was consequently consumed as that sentinel.
It returned a one-generator result of dimension seven and did not
independently re-standardize that result together with the input ideal.  It is
an excluded malformed-input experiment, not a test of `F_8`.

All corrected-target and independent-engine retries have now terminated.  At
`p=1009`, the legacy-order target, requested-order target, and legacy-order
`slimgb` runs each timed out at 1800 seconds.  At `p=73`, the legacy-order
target, requested-order target, and legacy-order `redSB` target also each
timed out at 1800 seconds.  Every transcript stops after
`ROW_GRADING_CHECK=PASS` and the row-order record, before
`TARGET_SEED_SIZE`, dimension, Hilbert, or pure-power output.  Thus none is
seed evidence or full-ideal evidence.

The smaller prime was arithmetically admissible: `73>8*8+3`, the roots of
`H_8` are `34,61`, and the selected branch has `y=34`, `g=38`, `yg=51`, with
all 17 high pivots nonzero and both modular point checks passing.  This
certifies a good emitted reduction only.  Since its standard-basis jobs all
timed out, it provides no dimension or Hilbert-function measurement.  No lane
Singular job remains running.

## 4. What is uniform, and what is not

There is an exact recurrence for the untruncated raw series:

\[
 R_{t+1}(s)=R_t(s)\,
 \frac{(1-s^{t+1})\prod_{d=4t+1}^{4t+4}(1-s^d)}
 {(1-s^t)(1-s^{t+2})(1-s^{2t+2})(1-s^{2t+3})}.             \tag{2}
\]

Equivalently, if `p_t(m)` counts partitions of `m` using parts in `W_t`
(and is zero for `m<0`), then

\[
 a_{t,n}=\sum_{S\subseteq D_t}(-1)^{|S|}
          p_t\left(n-\sum_{d\in S}d\right),                \tag{3}
\]

and the exact uniform candidate length is

\[
 L_t^{\rm Fr}=\sum_{n=0}^{\nu_t-1}a_{t,n},\qquad
 \nu_t=\min\{n:a_{t,n}\leq0\}.                             \tag{4}
\]

Equations (1)--(4) are a reproducible uniform definition/algorithm.  They do
not simplify to a proved scalar recurrence for `L_t^Fr`, because the cutoff
`nu_t` is defined by a first-sign change and positive truncation is nonlinear.
The numerical residuals

```text
L_(t+1)^Fr - 5 L_t^Fr = 8, 19, 76, 28, 37       (t=3,...,7)
```

already rule out the tempting exact factor-five recurrence.  Moreover the
unique quartic interpolating only the five observed lengths at `t=3,...,7`
predicts `144921`, not `215702`, at `t=8`.  This is a concrete reminder that
five scalar checks determine no credible extrapolation; `215702` comes from
the full degree/weight formula, not from fitting the length sequence.

## 5. Logical status and sharp limits of the checks

The defensible uniform statement is therefore:

> **Weighted-Froberg conjecture for this family.**  For every `t>=3`, the rows
> `T_(t,1),...,T_(t,2t-1)` have the degree-by-degree maximal-rank behaviour
> needed for `Hilb(A_t[b4,q,b3]/I_(t,+);s)=F_t(s)` (fibrewise at split `t`).

It is verified as a Hilbert-function identity in the fields listed in the
table, but no uniform maximal-rank/semi-regularity theorem has been derived
from the closed indexed generator family.  In particular:

* the finite candidate at `t=8` does **not** prove `dim I_(8,+)=0`;
* fixed `t=3,...,7` checks do not prove the conjecture for any new `t`;
* the properness lemma promotes modular `dim=0`, but not a modular Hilbert
  series or length to characteristic zero
  (`source_audit.md:181-186`); hence `1709,8621,43133` remain modular lengths
  unless separately computed or flatness is proved in characteristic zero;
* equality of Hilbert series does not determine the full weighted initial
  ideal, its pure powers, or a regular sequence;
* degrees and weights alone cannot force the formula.  At `t=2` the same
  Froberg calculation gives length `12` (`froberg_t2_t8.json:3-36`): the
  exact `y=2/5` fibre indeed has length `12`, while the exact `y=1/5` fibre is
  one-dimensional and its series does not terminate
  (`t2_split_exact_b1_full.out:1-17` versus
  `t2_split_exact_b0_full.out:1-12`).

Accordingly, `215702` is a well-certified **prediction**, while the actual
`t=8` length and the uniform equality remain OPEN.
