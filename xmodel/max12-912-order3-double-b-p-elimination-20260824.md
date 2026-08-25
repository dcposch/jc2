# Exact univariate `p`-elimination on the double-`B` leaf

Date: `2026-08-24`  
Status: **PRODUCER-EXACT / DIRECT ALGEBRAICITY CERTIFICATE / HOSTILE REVIEW REQUIRED**

This is an immutable successor to
`xmodel/max12-912-order3-double-b-q-algebraicity-20260824.md`.  It does not
mutate that already-frozen producer or its active review.

## Result

For the corrected characteristic-zero saturation

```text
J = (r1,r2,r3,r4,r5,r7,r6-1,10*r8+3*p,p*ip-1)
```

of the normalized `k=mu=0`, `nu=1` order-three double-`B` fibre, exact
`msolve 0.10.1` elimination of the first eight variables returned a
one-element basis in `Q[p]`:

```text
P(p),  deg(P)=630,
support(P)={0,9,18,...,630},
P(0)!=0.
```

The primitive integer representative has 71 nonzero coefficients and
coefficient-list SHA-256
`459c4436ddc06c086171baab73a41bd9626e356c5749f445bf82766938431e68`.
The complete 38,205-byte output has SHA-256
`50d71a0b76239db801e5c75ff9497f33d62086c4b8f7b5fd0a3e1bfb67852a75`.

The output was reconstructed over characteristic zero from 120 primes, with
zero bad primes and maximum reported coefficient height 1,828 bits.  It is a
non-unit polynomial, so the known characteristic-zero first-prime `[1]`
short circuit is inapplicable.

## Source and independent controls

The frozen input begins with nine variables in `p`-last order, declares
characteristic zero, and contains exactly nine equations.  Its SHA-256 is
`1bde828bfe3cddb7342a10436b34913c6cf1adebb4d668f0947b3a1f1ad1f287`.
The replay regenerates it byte-for-byte from generator SHA-256
`5c1c6e6d6570d58f9c9f6104be151e6da68c90d0e2855af9021f533b92420b01`
and parent compiler SHA-256
`a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf`.

Three independent Singular product-order runs at primes `32003`, `100003`,
and `104729` each give dimension zero, degree 1,188, and a monic degree-630
`p` polynomial.  Reducing the reconstructed characteristic-zero `P` modulo
each prime and normalizing its leading coefficient matches all 71
coefficients exactly.  The modular checks are controls, not a
characteristic-zero proof; the 120-prime rational reconstruction is the exact
producer certificate.

The elimination telemetry unexpectedly labels the `ELIM(8)` input
`homogeneous input? 1`, even though `r6-1` and `p*ip-1` visibly contain
constants.  This may be an elimination-mode/internal-homogenization flag, but
it is explicitly charged to hostile review.  The parser nevertheless records
nine valid equations, and the result agrees coefficient-for-coefficient with
independent inhomogeneous Singular computations at three primes.

## Consequence for trajectories

Let a field-valued point satisfy the unsaturated double-`B` ideal.

- If `p=0`, then `p` is constant.
- If `p!=0`, adjoining `ip=p^{-1}` gives a point of `J`, so the elimination
  certificate gives `P(p)=0`.

Thus `p` is algebraic over `Q` at every point, without needing the stronger
1,246-element zero-dimensional basis.  On an actual trajectory, algebraicity
over `Q` places `p` in the algebraically closed constant field `C`.  The
reviewed relation `3*p+10*r8=0` makes `r8` constant, contradicting the reviewed
terminal row `9*r8'=j/u!=0`.

## Replay and trust boundary

Run:

```sh
python3 cases/max12_912_order3_double_b_p_elimination_20260824/verify_result.py
```

The replay checks every byte, regenerates the source input, parses all 71
terms, checks primitivity/support/nonzero constant term, and performs the
three independent modular coefficient comparisons.  As with the parent
package, exact membership `P in J` ultimately trusts the characteristic-zero
`msolve` elimination computation until an independently checked
transformation or exact Singular basis lands.  Such Singular races are
running on separate AWS nodes.

## Scope

Producer-exact only on the normalized `k=mu=0`, `nu=1`, order-three
double-`B` coefficient leaf.  No other pair-norm leaf, Taylor boundary,
other load, order-one core, `(8,12)`, all `(9,12)`, maximum-twelve,
counterexample, or JC2 conclusion follows.

