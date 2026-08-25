# Max12 `(9,12)` corrected-Q8 order-128 invariant-support certificate

Date: 2026-08-24  
Status: **producer-exact finite-box certificate; hostile review required**

## 1. Exact result and scope

On the selected corrected-Q8 formal branch, the exact six-row quotient was
Hensel-lifted through order `w^127` at eight good finite-field
specializations.  For each specialization and each of

```text
(n,q),       (theta,Z),       (theta,q),       (w,q),              (1.1)
```

every rectangular monomial matrix in

```text
1 <= d_left,d_right <= 24,
(d_left+1)*(d_right+1) <= 108                              (1.2)
```

has full column rank on coefficients `w^0,...,w^111`.  There are `229`
rectangles per pair per prime, hence

```text
229 * 4 * 8 = 7,328                                       (1.3)
```

full-rank matrices.  No fit nullity and no relation hit occurred.  The final
`16` coefficients were reserved as a holdout; because every fit matrix was
already injective, no candidate reached the holdout test.

For each pair in (1.1), this exactly excludes a nonzero polynomial
`H in Q[X,Y]` whose support lies in any rectangle (1.2) from vanishing on the
selected characteristic-zero formal branch.  Univariate polynomials of
degree at most `24` are included by placing them in a rectangle with the
other degree equal to one.

This is a rectangular-support theorem, not a sparse-support theorem.  For
example, a sparse polynomial of bidegree `(24,24)` is outside the certificate
because its bounding rectangle has `625` columns.  No relation outside (1.2),
relation with algebraic rather than rational coefficients, global equation,
normalization, genus, projective-boundary classification, rational
trajectory, all-`(9,12)`, maximum-twelve, counterexample, or JC2 conclusion
is claimed.

## 2. Pinned invariant definitions

The computation consumes the frozen global quotient, with fixed nonzero
load `nu`, and uses

```text
n     = r6/p^9,
q     = r8/p^10,
theta = a0^2/p^9 = w*(1+w*c^3)^2,
Z     = q^9/n^10.                                         (2.1)
```

Here `p` is the approximate-cubic coordinate; finite-field primes below are
denoted by `ell`.  The parity-only formula `r6=p^9 R6(v)` is not used.  The
terminal differential condition remains the necessary identity

```text
nu^10 h^3 (Z')^9 = j^9 Z^8,                              (2.2)
```

but (2.2) is not part of the support-rank computation and no trajectory
conclusion is drawn from it here.

## 3. Good reductions and exact matrix data

The remote run used the immutable source hashes

```text
modular_support.py  c36d6cf1ca538a39923412075fb44be77ed30023107f4eac755722b7d796dea0
run_matrix.py       c57bea5c7423a26aaf22caf4d2894dc5dc5645793d58f127d101d86d4b68cfe6
replay.py           b94cc59a2d64602481a1e5709709c990dc3dc5f766b8c2b0eab9a5439746aa1a
AWS runner          389d9eb23eae1080a9dce3b3521322f9de2adc8766a7c74a2db55e61fbd981a1
``` 

and returned exit code zero with empty stderr.  Each worker verifies
primality by trial division, checks `Q8(v)=0`, inverts every encountered
rational denominator, and checks the six-by-six Hensel Jacobian determinant
is nonzero:

| `ell` | Q8 root `v` | Jacobian determinant mod `ell` |
|---:|---:|---:|
| 10007 | 980  | 2820 |
| 10037 | 1220 | 4798 |
| 10039 | 8298 | 4999 |
| 10061 | 5525 | 4921 |
| 10067 | 1853 | 6058 |
| 10069 | 5814 | 5358 |
| 10079 | 8882 | 8870 |
| 10091 | 5216 | 4305 |

All four searches in every result record

```text
tested_rectangles                    = 229
full_column_rank_rectangles          = 229
max_tested_columns                   = 108
hits                                 = []
nonzero_fit_nullities                = []
tested_rectangles_sha256             =
  5ca5018958874fca091d18a8eafd4a4bd3a089bdb59b4c75232d70310e932ae1. (3.1)
```

The frozen lightweight audit independently reconstructs the rectangle list
and its hash, verifies every source/output hash and good-reduction field, and
aggregates the `7,328` matrices.  It does not pretend to recompute the Hensel
lifts or ranks; the pinned worker is the reproducible exact computation.

## 4. Why one good reduction gives the bounded `Q`-exclusion

Suppose a nonzero `H in Q[X,Y]` supported in a tested rectangle vanished on
one of the pairs (1.1) along the selected characteristic-zero branch.  Clear
denominators and divide all integer coefficients by their gcd.  The resulting
primitive integer polynomial remains nonzero modulo every prime `ell`.

At any row of the table, all structural denominators are invertible and the
six-by-six Jacobian is a unit.  Exact Hensel uniqueness therefore identifies
the computed series with the reduction of the selected branch at the prime
ideal `v -> v_ell`.  Reducing the identity `H=0` supplies a nonzero coefficient
vector in the kernel of the corresponding `112`-row monomial matrix.  This
contradicts its full column rank.  Thus any one listed good reduction suffices
for the stated characteristic-zero rational-coefficient exclusion.

The remaining seven primes provide independent replay robustness and rule
out specialization-specific rank accidents; they do not enlarge the degree
box or prove a whole-component statement.  A relation over the Q8 number
field need not remain in the same rectangle after taking its norm to `Q`, so
the certificate is deliberately not advertised for algebraic coefficients.

## 5. Execution provenance and successor

The exact AWS payload is frozen under

```text
cases/max12_912_order3_nu_q8_order128_invariant_support_20260824/aws/
```

from remote path

```text
/home/ubuntu/jc2q8/out/q8_invariant_support_order128_v1/.
```

The summary SHA-256 is

```text
32147526bd6522a9ffb5fc672415765cedd3e6f653314fa8064a214f943c3d79,
```

and stderr is empty with SHA-256

```text
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.
```

This negative result strengthens the structural conclusion that the Taylor
variables are formally local coordinates and that no small natural plane
projection cuts the Q8 branch.  The next informative gate is therefore
global: exact component grouping/projective boundary, or the terminal Belyi
passport combined with the polynomial Taylor divisor conditions.  Increasing
the same relation boxes again has lower expected information gain.

## 6. Audit

```sh
python3 cases/max12_912_order3_nu_q8_order128_invariant_support_20260824/audit.py \
  | diff -u cases/max12_912_order3_nu_q8_order128_invariant_support_20260824/audit.json -
shasum -a 256 -c \
  cases/max12_912_order3_nu_q8_order128_invariant_support_20260824/MANIFEST.sha256
```

Because local swap pressure triggered a user stop on heavy local algebra,
the rank computation was run only on AWS.  The local audit is hash and JSON
logic only.
