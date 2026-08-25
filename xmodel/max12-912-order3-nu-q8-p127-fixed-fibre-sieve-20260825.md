# Max12 `(9,12)` selected-Q8 pure-Singular fixed-fibre sieve

Date: 2026-08-25  
Status: **producer-exact fixed-fibre theorem; generic-family consequences conditional; hostile different-model review required**

## 1. Exact result and scope

For the pinned selected-Q8 localized quotient, reduce modulo `127`, fix each
nonzero `w in F_127`, and impose

```text
inv*x5*(x3-2*x5)=1,             v*x5=x3-2*x5.          (1.1)
```

Pure Singular `std`, applied directly to the original eight generators, gives
a zero-dimensional fibre at all 126 values.  Every displayed `v` eliminant is
squarefree.  At 123 values the quotient has vector-space dimension 190 and
the eliminant is squarefree of degree 190, so `v` is a primitive element of
that reduced fibre.

There are exactly three exceptional values:

```text
w=39:  fibre dimension 190, eliminant degree 189;
w=56:  fibre dimension 189, eliminant degree 189;
w=125: fibre dimension 189, eliminant degree 189.       (1.2)
```

Thus this is not a claim of finite flatness over all `G_m`.  In particular,
the degree-189 values are excluded from every degree-190 factor sieve.

The sharp two-fibre patterns are

```text
w=25:  [2,188],
w=47:  [1,3,186].                                    (1.3)
```

Their proper subset-sum sets are respectively

```text
{2,188},             {1,3,4,186,187,189},             (1.4)
```

and are disjoint.  Independent, separately tagged executions reproduce the
two complete Singular outputs byte for byte:

```text
w=25 result.out  0b2da8f539bf5fa9f0897732eeb3468857c098743e106c11789be141db41e081
w=47 result.out  8d80f9211a79990398ba9e0db45fdd805e68d30722b31d5f0461ccfa1b7bee7f
```

The audit also intersects the subset-sum sets of all 123 primitive
degree-190 fibres and obtains only `{0,190}`.  The pair (1.3) is already the
minimal certificate.

## 2. Exact conditional irreducibility lemma

The following implication is exact but its hypothesis is not yet discharged.

Assume that the generic localized quotient over `F_127(w)` admits a common
monic degree-190 `v` polynomial `H(w,v)` on one finite-flat open containing
both `w=25` and `w=47`, and that its two specializations are the eliminants in
(1.3).  Then `H` is irreducible over `F_127(w)`.

Indeed, a proper monic generic factor of `v`-degree `d` specializes without a
degree drop at both points.  The specialized irreducible factors must group
to total degree `d`; hence `d` must belong to both proper subset-sum sets in
(1.4), which is impossible.

This argument must not be used before the common-monic/finite-flat
specialization hypothesis is proved.  Separate zero-dimensional fixed
fibres, even 126 of them, do not manufacture that hypothesis.

## 3. Conditional monodromy sharpening

Under the same common generic degree-190 action, the audited fibre `w=63` has
factor pattern

```text
[1,32,157].                                           (3.1)
```

The 32nd power of its Frobenius permutation is a single 157-cycle.  Once
irreducibility supplies transitivity, this already supplies primitivity: in
a nontrivial block system on 190 letters a block has size at most 95, whereas
a prime 157-cycle (which acts trivially on the fewer-than-157 blocks) would
have to lie inside one block.  Jordan's prime-cycle theorem then gives
`A_190`; the original permutation in (3.1) is odd, so the arithmetic
monodromy group is `S_190`.

This `S_190` conclusion remains conditional on the family bridge in section
2.  It is not asserted from the fixed fibres alone.

## 4. Diagonal-twist falsifier

The tempting shortcut that all nonzero `w` fibres are diagonal twists of one
fibre is false for the displayed quotient coordinates.  Solving all 161
exact support equations for diagonal weights on

```text
(w,c,d2,d4,x1,x3,x5)
```

gives rank seven and nullity zero.  Hence no nontrivial diagonal torus makes
each of the six imposed rows semi-invariant.  A genuine generic/flatness
calculation is still required.

## 5. Engine rollback and provenance

No `msolve` output contributes to this report.  Earlier `msolve 0.10.1`
answers included candidate points that fail the original rows under exact
Singular reduction; all such outputs, including apparent unit bases, remain
negative controls only.

The producer matrix ran on AWS Box02 host `ip-172-30-0-186`.  The 120-value
dispatcher (the six earlier audited values were excluded) used concurrency
88 and exited zero.  The exact audit, run on the same host under tag
`q8_p127_exhaustive_audit_v1`, reports

```text
audit.py        fcedd58d2784e104331242d7e2952d38201ce840d393b3e7bb8f96b249c93e16
audit.json      2e6b555e5c864d4ed055c066b6fcf5d38d91e66b7e43b2db905d8837c98c4fc0
audit stderr    e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
dispatcher      055bb16d1595336e2bf5d6407229cbc87bda55eded4360eb1c9934fc8623bd3f
fixed runner    11084528be3c14935b4542677795240ecf9716daf4d901cd4f917557daeafcd7
fixed generator 4af6f7eca198bcdf1e60151449e08099853669bd1d6965db3cddffa666032d2c
```

The diagonal-weight audit ran under tag `q8_diagonal_weight_audit_v1`:

```text
result.json     b7233d68fc0193c4ef8e918fd5e415b1dabaf4d39a16f32e65a8337d4312b7dd
weight audit    fb7c3aa812cd9980283ad7a7f27cef91d5978c0462d88ffa3bdd51f87d7efa8e
stderr          e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The portable case is
`cases/max12_912_order3_nu_q8_singular_broad_scan_aws_20260825`.

## 6. What remains open

The smallest missing lemma is the common monic degree-190/finite-flat
specialization bridge over `F_127(w)`.  After that, arithmetic
irreducibility, removal of a constant-field split, and good-reduction lifting
to characteristic zero are distinct steps.

Nothing here proves geometric or characteristic-zero irreducibility,
classifies components disjoint from the selected Q8 boundary, realizes the
Taylor coefficient families, imposes the terminal differential row, excludes
an actual `(9,12)` trajectory, closes maximum twelve, or proves JC2.

