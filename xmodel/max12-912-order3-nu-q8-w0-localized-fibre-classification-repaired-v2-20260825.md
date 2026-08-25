# Localized `w=0` corrected-Q8 fibre — reviewed repairs V2

Date: 2026-08-25  
Status: **PRODUCER-EXACT REPAIR SUCCESSOR; V1 CORE REVIEWED
`CONFIRMED_WITH_REPAIRS`; V2 HOSTILE REVIEW PENDING**

## 1. Scope and immutable parent

This is a nonmutating repair successor to
`max12-912-order3-nu-q8-w0-localized-fibre-classification-20260825.md`
(SHA256
`bb09d7dd5d2eda3aafda2272403e0cb2e6a03e43f657ee524929e5c88cf4e1d0`)
and its Grok review (SHA256
`fa649cd0a799d7f8cdbd702cdbb02c2660b57d2fa674a7177c0a3307cfcc23e4`,
verdict `CONFIRMED_WITH_REPAIRS`). The V1 report and case bytes are unchanged.

The theorem remains exactly the finite affine chart

```text
p=1, k=mu=0, w=0, x5!=0, x3-2*x5!=0
```

of the six divided approximate-cubic rows. Its scheme is

```text
Y0 ~= Spec(Q[v]/(Q8)),
Q8 = 999v^8+1539v^7-1782v^6-6498v^5-7320v^4
     -4428v^3-1548v^2-296v-24,
```

the displayed sign being a convention: the generator's eliminant is the
associate `-Q8`. The V1 scheme-isomorphism, squarefreeness, `r6`-unit, full
relative-Jacobian-unit, and absence of unloaded or loaded non-Q8 points are
unchanged. This V2 supplies the six requested custody/wording repairs.

No horizontal landing, source-boundary, projective escape, terminal, Taylor,
`p=0`, other `(9,12)` leaf, maximum-twelve, Keller-pair, or JC2 conclusion is
added.

## 2. Independent irreducibility certificate

The corrected octic is primitive over `Z`. An AWS-only deterministic search
found the least tested good prime `p=7`. After monic normalization its
reduction is

```text
q(v)=v^8+4v^7+2v^6+v^5+6v^4+2v^3+4v^2+v+5 in F7[v].
```

The pure-stdlib Rabin lane certifies exactly

```text
v^(7^8)-v = 0 mod q,
gcd(q,v^(7^4)-v)=1.
```

Since the only prime divisor of `8` is `2`, this is the degree-eight Rabin
criterion. A separately generated Singular lane at the same prime reports
one factor, of degree eight and multiplicity one, and certifies mutual ideal
divisibility between that factor and `q`. Its fail-closed parser requires

```text
factor_count=1, degree_sum=8, degree8_count=1,
mutual_divisibility=1.
```

Thus `q` is irreducible over `F7`, and Gauss reduction proves `Q8`
irreducible over `Q`. This does not rely on the V1 same-CAS characteristic-
zero factor display. The first Singular parser attempt is retained as a
negative control: an invalid `intvec` extraction produced diagnostics and no
PASS marker; it is not consumed.

Decisive output hashes are

```text
Rabin stdout             eb389979e8c75f7b85d18f413c70ef6413d7ff1738365b62be35a1915e3fd1e2
Singular factor stdout   8a05b14f4f0a9aa86eb213c55f6853c7b7019138f123f7d607e85bd1e45fba1b
```

## 3. Missing characteristic-zero `r8` splits

The two V1-preregistered but unexecuted characteristic-zero non-Q8 splits
were run literally:

```text
D(e6) intersect D(Q8) intersect V(e8),
D(e6) intersect D(Q8) intersect D(e8).
```

Both are unit ideals in the Box02 `std`/block implementation and the Box03
`slimgb`/total-degree implementation. Every lane returns
`original_remainder_zero=1`, `dim=-1`, `size=1`, and exactly one PASS marker.
This completes the advertised `V(e8) union D(e8)` split; its emptiness is
also consistent with the already-reviewed parent non-Q8 unit ideal.

The four stdout hashes are

```text
Box02 V(e8)  85cbc6c61ca5eea890e80c6d0354c4ad99fe56e0518276f24327b726d99c9e8e
Box02 D(e8)  85a005232722220b17a3081ce3535b189a37d6fe24a0d17a99ae7499c2384d3e
Box03 V(e8)  00625142b1288c9ea2299b1d9a2086c1d402a82b4bd9e5fbe6f6f9f9695c6464
Box03 D(e8)  197c6d52df65bb4f52aa879338c0501feb688bb0243bdd244a995b1999e613fd
```

## 4. Exact source-fidelity and wording repairs

The V1 source calculation for the singular locus is the **loaded Q8
singular ideal**

```text
(Ibase, inu*e6-1, Q8, detJ),
```

not the shorter ideal printed in V1 §4. Because the separately computed
`(Ibase,e6)` is the unit ideal, `e6` is already a unit on `Y0`; the loaded
inverse is redundant on this scheme, so the unit conclusion is unchanged.
This report cites the ideal actually computed.

The constructive shape basis was printed only for the Box02 `q8` lane. It is
an optional coordinate reconstruction. The scheme isomorphism continues to
use the reviewed exact argument

```text
ker(Q[v] -> A)=(Q8),  dim_Q A=8=deg(Q8),
```

and does not pretend that a base-lane shape basis was printed.

Every new non-Q8 lane explicitly hashes the transitive
`order3_fibre.py` source at
`a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf`
and the descent replay at
`5dcb0a67d79859c04d83d2c20ff8518a148a78c1229f42b00169c5842d5e7256`.
The factor certificate is intentionally independent of those sources: it
tests the displayed integer octic alone.

## 5. Replay and exact conclusion

The small AWS replay checks the two independent irreducibility endpoints,
all four characteristic-zero split endpoints, transitive source pins, fixed
stdout hashes, and the failed-parser negative control. The valid Box02 replay
returns `rc=0` and

```text
Q8_W0_LOCALIZED_FIBRE_REPAIRED_V2_REPLAY_PASS
```

with stdout SHA256
`b9a2208054567c7832ca79c8c6f6560562e9455fde679cdd7413330c42990148`.
An earlier wrapper used unavailable `rg` after the mathematical replay had
passed; that wrapper is retained as a software negative control and is not
the acceptance endpoint.

Therefore all six hostile-review repairs are discharged at producer tier:

1. the loaded singular ideal is cited exactly;
2. irreducibility has a good-prime Rabin certificate plus an independently
   parsed Singular factor count;
3. both characteristic-zero non-Q8 `r8` splits are executed;
4. shape-basis provenance is narrowed;
5. transitive fibre/descent sources are explicitly pinned; and
6. the sign of the corrected octic is stated only up to a unit.

The mathematical theorem remains the V1 localized affine scheme theorem at
its strict scope. The exact next gate is now the separately preregistered
source-horizontal split before any `w=0` or projective-boundary inference.
