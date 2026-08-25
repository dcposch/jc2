# Exact characteristic-zero algebraicity on the double-`B` leaf

Date: `2026-08-24`  
Producer: campaign coordinator, exact AWS algebra lane  
Status: **PRODUCER-EXACT / PROVISIONALLY CLOSES THE DOUBLE-`B` LEAF / DIFFERENT-MODEL HOSTILE REVIEW REQUIRED**

## Claim

On the reviewed normalized maximum-12 `(9,12)` order-three landing

```text
k=mu=0,  nu=r6=1,
r1=r2=r3=r4=r5=r7=0,
3*p+10*r8=0,
```

every coefficient-field point has `p` algebraic over `Q`.  Hence every actual
Keller trajectory on this leaf has constant `p` and constant
`r8=-3*p/10`, contradicting the already-reviewed terminal row

```text
r8' = j/(9*u),   j != 0.
```

Subject to hostile review of the exact CAS certificate and its source trace,
the double-root-off-`W` four-point leaf is therefore empty of actual Keller
trajectories.

This does not empty any other root-free norm leaf and does not prove `(9,12)`,
maximum twelve, or JC2.

## 1. Source-honest ideal

Let `I` be the eight-equation ideal in
`Q[x0,x1,x2,x3,x4,x5,q,p]` obtained from the exact order-three fibre compiler
by setting `k=0` and imposing

```text
r1=r2=r3=r4=r5=r7=0,  r6=1,  10*r8+3*p=0.
```

The corrected generator
`cases/max12_912_order3_nu1_probe_20260824/generate_double_b_msolve.py`
has SHA-256
`5c1c6e6d6570d58f9c9f6104be151e6da68c90d0e2855af9021f533b92420b01`.
It pins the parent compiler SHA-256
`a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf`.
The frozen replay regenerates the input byte for byte.

The nonzero-`p` locus is represented without a saturation black box by

```text
J = I + (p*ip-1)
```

in nine variables.  The frozen input starts on its first line with exactly

```text
p, x0, x1, x2, x3, x4, x5, q, ip
```

and declares characteristic zero on its second line.  Its SHA-256 is
`a01186da8d162c407baf53afcec44a49231d5549fdd2756f9a6fceaa240cc6ba`.
The earlier runs in which an in-band comment was misread as a one-variable
declaration are quarantined and supply no evidence here.

## 2. Exact characteristic-zero basis of `J`

`msolve 0.10.1` reconstructed a non-unit reduced DRL Groebner basis over
characteristic zero.  The run used 126 machine primes, reported zero bad
primes, and reconstructed coefficients of at most 1,368 bits.  The basis has
1,246 elements.  The uncompressed result has 23,172,493 bytes and SHA-256

```text
6ce7d394989dedcffe303ff8aaf4fb3cb89e750cbf57ad6c15eb9231e11f399e.
```

This is not the hazardous characteristic-zero `[1]` short circuit: the output
is a non-unit 1,246-element rational basis and its log explicitly records the
CRT/rational-reconstruction phase.

The independent frozen parser decompresses the complete output, parses all
1,246 polynomials, recomputes every leading monomial in the declared graded
reverse lexicographic order, and checks that the printed first term is the
actual leading term.  The initial ideal contains

```text
p^5, x0^5, x1^5, x2^5, x3^5, x4^5, x5^5, q^6, ip^6.
```

These are leading monomials, not univariate equations.  Their role is to show
that the initial ideal, and hence `J`, is zero-dimensional.  Direct staircase
enumeration from all 1,246 leading monomials gives exactly 1,188 standard
monomials, so the exact quotient has degree 1,188.  This independently matches
the prior multi-prime discovery degree but does not rely on it.

## 3. Exact `p=0` slice

The complementary slice `I+(p)` was recomputed over `Q` with Singular.  A
direct two-way normal-form check proves

```text
I+(p) = C1 intersect C2,
```

where, after omitting the already-set coordinate `p`,

```text
C1 = (x1,x2,x3,x4,x5, 2*x0^2-9),
C2 = (x1,x2,x4,x5, 4*x3^3+81, x0-x3*q).
```

Both have `q` free.  Their dimensions/degrees are respectively `(1,2)` and
`(1,3)`.  The full slice has dimension one and degree five.  The two displayed
irreducible equations make the components reduced and prime over `Q`; the
direct intersection equality rules out hidden embedded structure in the
slice.  The replay also reproduces the independent `primdecGTZ` output.

## 4. Pointwise algebraicity and the terminal contradiction

Let an actual trajectory give a field-valued point of `I`.

- If `p=0`, then `p` is already constant.
- If `p!=0`, set `ip=p^{-1}`.  The point extends to `J`.  Because `Q[variables]/J`
  is finite-dimensional over `Q`, the image of `p` satisfies a nonzero
  polynomial over `Q`.

Thus `p` is algebraic over `Q` in both cases.  The trajectory field contains
the algebraically closed constant field `C`, so such an element lies in `C`
and has derivative zero.  The reviewed double-`B` equation gives
`r8=-3*p/10 in C`, hence `r8'=0`.  This contradicts the reviewed terminal
identity `9*r8'=j/u!=0`.

The argument needs only zero-dimensionality of the nonzero-`p` locus; it does
not need an explicit degree-630 elimination polynomial in `p`.  The separate
`p`-last elimination race remains useful as an independent certificate.

## 5. Replay and trust boundary

Run from the repository root:

```sh
python3 cases/max12_912_order3_double_b_q_gb_20260824/verify_result.py
```

Expected tail:

```text
zero_dimensional_initial_ideal=YES
standard_monomials=1188
p0_slice=dimension_1_degree_5_two_components_degrees_2_plus_3
```

The frozen parser proves that the preserved output has the stated exact
combinatorics and regenerates the source input.  It does not independently
prove that the 1,246 printed polynomials generate the input ideal; that equality
is the exact `msolve` computation's trust boundary.  An independent Singular
characteristic-zero computation and the `p`-last exact elimination are running,
and different-model hostile review is mandatory before canonical promotion.

Consumed reviewed facts:

- root-free norm/double-`B` normalization review SHA-256
  `b6ae9516430073e177a5174684109b437ab278fa04dd066686c58af57715588e`;
- collision-boundary/terminal-row review SHA-256
  `6d34908cbd2ead9769e4090fcab903ec5d5b7bd9db485db1d681708c5d36946e`.

The preceding independent algebra report, SHA-256
`e589d879fc7156f5e27d97333bb9814e9280c6a09341870b9a7f69711304978c`,
correctly stopped at `INCONCLUSIVE` before this corrected characteristic-zero
basis arrived.  Its exact `p=0` decomposition is reproduced and strengthened
by the direct intersection check above.

## Scope firewall

Proved at producer/CAS level only: algebraicity of `p` and terminal exclusion
on the normalized `k=mu=0`, `nu=1`, order-three double-`B` coefficient leaf.
Not proved: any other pair-norm leaf, a Taylor boundary, other invariant loads,
the order-one core, `(8,12)`, all `(9,12)`, maximum-twelve automorphy, a
counterexample, or JC2.

