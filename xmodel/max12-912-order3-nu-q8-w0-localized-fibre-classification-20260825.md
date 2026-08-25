# Selected `(9,12)` corrected-Q8 localized `w=0` fibre classification

Date: 2026-08-25  
Status: **PRODUCER-EXACT; HOSTILE REVIEW PENDING**

## 1. Exact theorem and firewall

Let `Y_0` be the characteristic-zero affine scheme obtained from the exact
reviewed `p=1`, `k=mu=0`, `nu`-loaded approximate-cubic compiler by setting
`w=0` in precisely

```text
r1/t=r3/t=r5/t=r7/t=r2=r4=0
```

and adjoining only the two graph/localization equations

```text
v*x5-x3+2*x5=0,
inv*x5*(x3-2*x5)-1=0.                              (1.1)
```

Write

```text
Q8(v)=999*v^8+1539*v^7-1782*v^6-6498*v^5
      -7320*v^4-4428*v^3-1548*v^2-296*v-24.       (1.2)
```

Then

```text
Y_0  ~=  Spec(Q[v]/(Q8(v))).                       (1.3)
```

Moreover `Q8` is irreducible and squarefree over `Q`, the output `r6` is a
unit on `Y_0`, and the full relative `8 x 8` Jacobian of the six source rows
plus (1.1), with respect to
`(c,d2,d4,x1,x3,x5,inv,v)`, is a unit on `Y_0`.  Thus over `Qbar` this affine
localized fibre consists of exactly the eight reduced smooth corrected-Q8
contacts.  There is no unloaded point and no loaded non-Q8 point in this
chart.

This theorem is **only** the finite affine `p=1` chart

```text
w=0,   x5!=0,   x3-2*x5!=0.                        (1.4)
```

It does not classify the source boundary `x5=0` or `x3-2*x5=0`, their
intersection, a projective limit in which one of
`c,d2,d4,x1,x3,x5` diverges, or the separate `p=0` chart.  It does not impose
the terminal row `r8`, either true-centre Taylor polynomiality family, or a
rational-trajectory condition.  It gives no exclusion of every selected
component, `(9,12)`, maximum degree twelve, a Keller pair, or JC2.

## 2. Frozen source and exhaustive cover

The calculation was preregistered before any CAS launch.  Its immutable
source pins are

```text
generate.py                                      90b13704a850a70593a2c2d057637f1e2b4180534c5832890ce6814bfe03925a
run_remote.sh                                    4717772835703a9eef8cc17a47f0d28e2ab8bebc704a143948ffb231bca489d1
PREREGISTRATION.md                               3fe8e56af3e20d4661d7ba7c4c00d83353a5f6fcbf195587f2a1668c2cd84754
PREREGISTRATION.manifest.sha256                  a46bd2e229bf8f8056f57ddebe8146deba684bd41aa63baa7126c1eea633bf81
reviewed quotient_compiler.py                    22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545
reviewed quotient parent MANIFEST.sha256         3d60b5675ac623ce66f3b718ca79161de7f24d6d05f82cf910fe060680c93ac4
```

If `e6=r6|_(w=0)` and `detJ` is the full Jacobian determinant, the registered
set-theoretic cover was

```text
V(e6)
union [D(e6) intersect V(Q8)]
union [D(e6) intersect D(Q8)],                    (2.1)
```

with the last locus split independently by `V/D(detJ)` and `V/D(r8)`.
Every open was encoded by a new inverse equation.  Hence the base, unloaded,
loaded, Q8, Q8-smooth, Q8-singular, non-Q8, non-Q8-smooth,
non-Q8-singular, non-Q8-`r8=0`, and non-Q8-`r8!=0` modes are literal ideals;
there is no informal division or omitted factor orbit.

## 3. Exact AWS matrix

The primary exact run used Singular 4.3.2 on Box02
`ip-172-30-0-186`, with `std` and a block order.  The independent
characteristic-zero replay used Box03 `ip-172-30-0-249`, `slimgb`, and total
degree order.  Fresh good-characteristic controls used 127 on Box02 and
32003 on Box03.  All 34 runs returned `rc=0`, the unique PASS marker, and
zero remainder for every original ideal generator.  Their stderr contains
only `/usr/bin/time -v` custody text with exit status zero.

The decisive characteristic-zero rows are:

| stratum | Box02 `std`/block | Box03 `slimgb`/`dp` |
|---|---:|---:|
| base | dimension 0, length 8, squarefree degree-8 `v` eliminant `Q8` | same; independent basis size 29 |
| `V(e6)` | unit ideal | unit ideal |
| `D(e6)` | dimension 0, length 8, eliminant `Q8` | same |
| `D(e6) cap D(Q8)` | unit ideal | unit ideal |
| `D(e6) cap V(Q8) cap D(detJ)` | dimension 0, length 8, eliminant `Q8` | same |
| `D(e6) cap V(Q8) cap V(detJ)` | unit ideal | unit ideal |

The good-characteristic matrices reproduce every displayed dimension,
length, squarefreeness, Q8 gcd, and emptiness result.  Over `F_127`, Q8 has
factor degrees `1+1+1+5`, with rational roots `26,58,67`; no rational-root
shortcut is used.  Over `Q`, Singular returns one irreducible factor.

The independent AWS-only aggregate is frozen in the same case:

```text
aggregate.py                                     2114a5a73b5a24965a25cda5af563e0e913ef422ad2c2c944561caed5981f079
aggregate.json                                   c11e0500cd6a113eba1c3364f0902cd2eb117c5cc965bfb960b61bb6b1b88e7b
aggregate stdout                                 2615d3c71d6208fbaa4c84d88ca892373e26a38c9e7b802d0f1906ff9a129fe8
aggregate stderr                                 65db7b2d4904e7263cd13c24cc60cb410d5a026a850c8892e5a0d58f72161936
aggregate run.meta                               f16cc3771e4c525806b2afa8102886ff0287a22d6b3a7d939ff6ba11b2ca35e5
```

It reports exactly `34` audited runs: `14` reduced length-eight Q8 rows and
`20` unit ideals.

## 4. Proof of the scheme identity

Let `A=Gamma(Y_0,O)`.  The primary base computation gives

```text
dim_Q(A)=8,     ker(Q[v] -> A)=(Q8),              (4.1)
```

because the principal `v`-elimination ideal has monic degree-eight generator
equal to Q8 up to a nonzero scalar.  Thus `Q[v]/(Q8)` injects into `A`; both
are eight-dimensional Q-vector spaces, so the injection is an isomorphism.
This proves (1.3), not just equality of projected point sets.  Squarefreeness
then makes `A` reduced, and irreducibility makes it a degree-eight field over
Q.

The literal ideal `(I_base,e6)` is the unit ideal, while the inverse-open
`D(e6)` has the same length-eight Q8 algebra.  Hence `e6` is a unit on all of
`Y_0`.  Likewise the Q8-singular ideal `(I_base,Q8,detJ)` is the unit ideal,
while the Q8-smooth inverse-open retains all eight points; consequently
`detJ` is a unit.  Finally the literal loaded non-Q8 inverse-open is the unit
ideal.  These statements also follow directly from the exhaustive cover
(2.1), and the independent engine/order replay gives the same result.

## 5. Exact consequence and next gate

Any actual selected trajectory whose coefficient-source closure reaches
`w=0` at a finite point satisfying (1.4) necessarily reaches one of the
corrected-Q8 contacts.  At that point the separately reviewed selected-Q8
positive-genus theorem applies at its own strict scope.  This is a
composition only after the actual-trajectory landing and finite-chart
hypotheses have been proved; the present fibre calculation does not prove
them.

The next fail-closed gate is therefore the complement of (1.4): classify the
disjoint affine source strata

```text
x5=0, x3!=0;       x5=x3=0;       x5!=0, x3-2*x5=0,              (5.1)
```

and then the projective coefficient-source boundary obtained by taking the
closure of the full six-row family before specializing `w=0`.  The order
“homogenize/saturate over Q[w], then specialize” is mandatory: homogenizing
the already-specialized fibre would not certify absence of an escaping
horizontal branch.  Terminal `r8` and Taylor provenance remain charged on
every surviving boundary component.
