# TD12 distant inhomogeneous row: R1 range/transgression erratum

Date: 2026-08-29  
Author: Sol 5.6  
Frozen Git basis: `92ebe92ad5986a47f01af9ed901260595dfed869`  
Charged producer:
`xmodel/td12-inhomogeneous-row-first-invariant-sol56-20260829.md`

## 0. Disposition

```text
REPAIR_REQUIRED
SECTION_5_1_RANGE_SHARPENED
NO_ORIGINAL_ENDPOINT_TRANSGRESSION_FROM_T1
ENDPOINT_HERMITE_CLASS_UNCHANGED
NO_ROUTE_KILL_UNCHANGED
```

The producer's endpoint Hermite congruence, multiple-root support
penetration, binary no-kill disposition, and endpoint-unit packet are
unchanged.  One sentence in Section 5.1 used injectivity beyond the range in
which the binomial particular is known to be polynomial.  The correction is
load-bearing for small `i`, although it does not change either transparent
window at its stated threshold.

## 1. Correction to Section 5.1

The producer states

```text
G_s=G_s^bin for 1<=s<nu.
```

Read this instead as

```text
G_s=G_s^bin for 1<=s<=min(r,nu-1),                  (R1.1)

and therefore for every 1<=s<nu only under the added rider

r>=nu-1.                                            (R1.2)
```

Proof.  The promoted formal lift proves that the coefficient of
`G^bin=c_g F^(3/2)` is polynomial only through `s<=r=3i/2`.  In that range,
induction is valid: after equality at all smaller grades, the difference at
grade `s<nu` is a polynomial in the kernel of `B_s`; its formal generator
`p^(r-s/nu)` is nonpolynomial, so injectivity forces the difference to zero.
For `r<s<nu`, the binomial coefficient need not be polynomial.  One cannot
subtract it from the actual polynomial `G_s`, and kernel injectivity alone
does not produce a polynomial particular.  Failure of the binomial lift at
`r+1` is not an obstruction.

Consequently, the producer's next sentence must also be range-qualified.
The first polynomial **homogeneous kernel of `B_s`** is still at `s=nu`, but
the first source correction to the binomial expression is not proved to wait
until `nu` when `r<nu-1`; it may already be needed at `r+1` to restore
polynomiality.

The full pre-resonance conclusion remains valid in the two transparent
window regimes actually used later:

```text
B: i>=16 => r=3i/2>=24=nu-1;
S: i>=12 => r=3i/2>=18>16=nu-1.
```

The producer did not assume the separate direct-entry rider `i=6n`, and it
must not be silently imported.  If a descendant explicitly proves and
charges direct entry, it also implies (R1.2) for the displayed U1 family;
that is not part of this report's unconditional route-occurrence premise.

## 2. Terminal T1 versus the original endpoint class

The producer's Section 5.2 distinction is binding and is sharpened here to
prevent an unsafe downstream reading.

Repaired Proposition 8.1 gives the terminal approximate-root compatibility

```text
nu*p*q' - kbar*p'*q = Theta*p,       Theta!=0.       (R1.3)
```

This is an unconditional **compressed source consequence** for an actual
route occurrence in the repaired Proposition-8.1 tower domain.  The reviewed
B and S templates solve (R1.3).  It does not, by itself, identify `q`,
`Theta`, or their root evaluations with the producer's original-pair object

```text
[Kcal_(s*)] in K[t]/(H_i).
```

That identification requires a source-provenanced transgression through the
instantiated approximate-root tower: the actual `(h_j,k_j,l_j,s_j)`, their
coefficient grades, and the maps from the original `P_a,G_b` to the terminal
coefficient.  Those data remain absent.

The producer's literal calculation with

```text
h_1=g^2-s_0*f^3=h_F,  s_0=c_g^2,  m_F=1
```

is valid only as the conditional first-resolvent-terminal case, together
with the displayed top normalization and grade identification.  It explains
how (R1.3) can be the quotient of the original `s*` content; it does not prove
that the frozen B or S route has `m_F=1`, and it supplies no longer-tower
transgression.

Accordingly, any producer wording such as "terminal quotient of the same
Keller content" means only "a consequence of the same exact Keller pair
after the repaired tower construction."  It does not mean equality with,
or a computed image of, the endpoint Hermite class.

## 3. What does not change

The proof of

```text
Kcal_(s*)(t) == kappa_F mod
  product_j(t-a_j)^(m_j*i-1)
```

uses only the exact endpoint convolution, `r>=i`, polynomial fresh pieces,
and deck folding.  It does not use the binomial particular.  Sections 2--4,
the B count `3i-2`, the S count `4i-3`, and the double-root support ranges
are therefore unchanged.

The no-kill conclusion is also unchanged and, if anything, strengthened at
small `i`: without polynomiality of the binomial particular beyond `r`,
there is still less licensed information connecting the low homogeneous
rows to the distant endpoint.  T1 remains compatible but does not evaluate
the endpoint class.  The smallest missing source object remains the
route-separated endpoint unit/Hermite packet or a fully instantiated tower
transgression.

## 4. Custody and scope

Recomputed full-file SHA-256 hashes:

```text
1272b394387d744ae065680c8327ff79d0179fb994c6d03d6d8c27d41d371c61
  xmodel/td12-inhomogeneous-row-first-invariant-sol56-20260829.md
97ba497fffcf0a0ee5c9ee259acc325810659a9fd5376a47b38c87476fd2c5b4
  xmodel/td12-formal-cascade-rank-v1-coordinator-integration-sol56-20260829.md
0f5968bf0a95d15ca5e9c119044daa9470321ae4586c20af50bd03f5587ac274
  xmodel/td12-formal-cascade-rank-v1-hostile-review-opus5-ccb-20260829.md
5fc6b1634dc1ef0a0abe578411644fa166ffbfa16b8608cbce2a7b7b61465cd5
  xmodel/sigray-later-m-package-source-audit-sol-ultra-20260828.md
```

The charged producer's body seal also re-verifies: `15383` bytes and
SHA-256
`36381aca4e450047507d46cbf9f2c1a1f17a6f4d4fd3333e372b491f28f8de41`.

This erratum supplies no `PairRef`, direct-entry theorem, source coefficient,
tower instance, transgression, endpoint-unit value, gate verdict, route
occurrence, exclusion, counterexample, or JC2 conclusion.  It edits no
producer, canonical, source, code, AWS, or `jc2-lean` object.

<!-- END-SEALED-BODY::td12-inhomogeneous-row-first-invariant-r1-erratum-sol56-20260829 -->

## Seal (outside the sealed body)

- Body byte count: `6110` (all bytes before this heading).
- Body SHA-256:
  `332e4d4a2f6d8da6426edcd785b99306d68c5710c3b1dc2ac09210e6b09dba7a`.
- Full-file SHA-256 is emitted with the transmittal after sealing.
- Frozen Git basis: `92ebe92ad5986a47f01af9ed901260595dfed869`.
