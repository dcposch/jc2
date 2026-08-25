# Hostile source-fidelity referee report

**Object.** Generic-`c` frozen-`b=1` selected-localizer unit, producer note
`xmodel/max12-912-order3-nu-q8-w0-rankdrop-b1-generic-c-localizer-unit-20260825.md`,
case
`cases/max12_912_order3_nu_q8_w0_rankdrop_b1_loaded_saturation_aws_20260825/`.

**Mode.** Read-only. No Bash, local CAS, solver, or network. The two accepted
AWS r6d endpoints were treated as the computations under review. Hashes were
checked for internal consistency among the note, generator, replay, manifests,
and endpoint `source.sha256`; they were not independently recomputed by the
reviewer.

**Ramified-audit provenance.** By the immutable provenance erratum,
`xmodel/max12-912-order3-nu-q8-w0-rankdrop-ramified-arc-audit-claude-20260825.md`
(SHA-256 `01891db1...cb75330`) was produced by Grok, not Claude. Its mathematics
and `NOT_CONFIRMED` verdict are unchanged. This is a separate review session.

## 1. Imposed source and substitution

**Finding: holds.** The pinned compiler imposes exactly
`(e1,e3,e5,e7,e2,e4)`. The frozen generator fail-closes on the tuple
`(1,3,5,7,2,4)`, and the Singular source forms exactly
`SI=se1,se3,se5,se7,se2,se4`. The Rabinowitsch polynomial is added afterward,
not as another source row. No terminal or Taylor row is hidden. Although
`se6,se8` are compiled as named unused polynomials, neither enters `SI`.

The map is exactly

```text
map phi=S,w,c,2+u,1,x1,x3,x5;
```

so `d2 -> 2+u`, `d4 -> 1`. The six frozen polynomials agree term-for-term with
the source rows quoted in the ramified audit.

## 2. Coefficient ring, localizer, and contraction

**Finding: holds, with the coefficient-field firewall below.** The working
ring and selected localizer are

```text
ring R=(0,c),(inv,w,u,x1,x3,x5),(dp(1),dp(5));
poly A=x3-2*x5;
ideal J=I,inv*w*x5*A-1;
```

Thus the coefficient field is exactly `Q(c)`, not `Q[c]`, and the localizer is
exactly `inv*w*x5*(x3-2*x5)-1`. The product order puts `inv` in the first
elimination block. In characteristic zero,

```text
I:(w*x5*A)^infinity
 = (I+(inv*w*x5*A-1)) intersect Q(c)[w,u,x1,x3,x5].
```

Consequently `eliminate(GJ,inv)` is the contraction, provided `GJ` is a
Groebner basis. Adding the landing centre after a unit contraction is
redundant; the report correctly treats `GC=(1)` as stronger than `GL=(1)`.

## 3. Exact meaning of the two unit bases

Granting Singular's standard-basis computations, `GC=(1)` implies `1 in J`
and hence emptiness of the selected open in the frozen slice over `Q(c)`.
Both accepted endpoints print

```text
landing_empty=1
GL[1]=1
GC[1]=1
Q8_W0_RANKDROP_B1_LOCALIZER_ELIMINATION_PASS
```

The two computations are different algorithms (`std` and `slimgb`) in the
same Singular 4.3.2 binary, on one host and with the same order. They are not
two CAS systems or two independently authored implementations.

The frozen direct package does **not** print a membership identity

```text
1 = sum a_i*phi(e_i) + b*(inv*w*x5*(x3-2*x5)-1).
```

There is no `lift`, `modStd`, or cofactor file in that freeze. Its conclusion
is therefore an ordinary Singular standard-basis theorem, not a separately
checkable source-generator membership theorem. The live modular lane
mentioned by the producer is not part of the reviewed freeze.

Custody is internally consistent: both generated inputs, source pins,
zero diagnostics, rc-zero endpoints, Singular version, wall/RSS records, and
the fail-closed regeneration replay agree with the producer note. The replay
regenerates each input byte-for-byte, verifies the source/map/localizer and
unit markers, and bans diagnostics; it is a custody replay, not a second
Groebner computation. Two minor custody qualifications remain: the compiler's
transitive descent-replay pin is enforced on import but is not listed in the
top manifest, and the result is two algorithms in one binary/order.

## 4. Both slice losses are binding

1. **Coefficient-field loss.** A unit over `Q(c)` clears to an identity with a
   nonzero denominator/content polynomial `D(c) in Q[c]`. Its finite roots
   are invisible here. Until `D(c)` or the `Q[c]` saturation is computed,
   “generic finite `c`” means off an unknown finite set.

2. **Frozen-`d4` loss.** The map imposes `d4=1` identically. An arc with
   `d4=1+B1*t+...` is not a point of this scheme. The maximal honest geometric
   conclusion is emptiness of selected points/arcs whose whole coefficient
   curve stays in the frozen slice, at generic finite `c`.

Therefore this result is not an arbitrary-ramification theorem, a theorem on
the whole rank-drop line, or a full selected-horizontal-closure/Hsrc theorem.
The parent preregistration's description of the slice as “decisive ... for
arbitrary ramification at `b=1`” is too broad and cannot be inherited into the
reviewed producer theorem.

## 5. Reconciliation with the ramified audit

There is no contradiction with the surviving slope-two initial cone

```text
(X1, 3*X3-5*X5, 9*W+4*X5^2).
```

An initial cone need not continue. The frozen-slice unit does kill any actual
generic-`c` selected continuation with `d4` identically one, but it does not
kill nonconstant `d4` drift, exceptional finite `c`, the rest of the doubled
rank-drop line, or the full ambient saturation. In particular it is weaker
than the ramified audit's polynomial-parameter Shard B1 and cannot overturn
that audit's `NOT_CONFIRMED` verdict for arbitrary ramification.

## 6. Firewall and next exact objects

No conclusion is licensed about exceptional finite `c`, other rank-drop
values, coefficient infinity, Taylor/terminal realization, trajectories, the
whole `(9,12)` cell, maximum twelve, or JC2.

The smallest missing trust certificate is a printed `lift`/membership identity
for `1 in J` over `Q(c)`. The next exceptional locus is the denominator/content
polynomial `D(c)` (equivalently the `Q[c]` selected saturation). Independently,
nonconstant `d4` drift must be represented by a ring retaining that variable,
for example the pointed chart `d4=1+v`, `d2=2+v+u`.

## Verdict

The source identity, localizer and contraction semantics, two-algorithm unit
bases, custody replay, and producer-note firewall survive hostile review.
`GC=(1)` licenses emptiness of the selected open of the frozen `d4=1` slice at
generic finite `c` as a Singular 4.3.2 standard-basis theorem. It does not
license a cofactor, classify finite `c`, cover `d4` drift, or prove a whole
rank-drop/Hsrc statement.

Required quotation repairs are: treat the result as CAS-GB trust until a lift
is frozen; do not inherit “arbitrary ramification at `b=1`”; and do not cite it
as the polynomial-parameter Shard B1 or as a full-Hsrc theorem.

**CONFIRMED_WITH_REPAIRS**
