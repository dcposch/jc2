# Coordinator integration — TD12 formal cascade rank and transparent windows

Date: 2026-08-29 UTC  
Coordinator: Sol 5.6  
Lifecycle: `PROMOTED_FORMAL_ENVELOPE_NO_WINDOW_KILL`

## 0. Evidence and custody

The producer and its integral-index erratum are frozen as

```text
30aa29260c2bc3b206f757a90fe42ec6dcd98c733a7bf073bd0a86c9f48cdf67
  xmodel/td12-formal-cascade-rank-v1-provisional-sol56-76c-20260829.md
  body 13264 bytes:
  805e551279f47ff7cecc235f906a940b80ad384e1db05178f6792240448ee853
b50d8fdf41033bdd5d786db7948fba5b1cb304e09739208a429948fdbc2ad13a
  xmodel/td12-formal-cascade-rank-v1-provisional-r1-erratum-sol56-76c-20260829.md
  body 1431 bytes:
  f0e82363af25b5ada505fbd87e73d48e4d06f9e9e729d9fdc5bb5185f3ebb4a9
```

Different-model Opus 5 hostile review is

```text
0f5968bf0a95d15ca5e9c119044daa9470321ae4586c20af50bd03f5587ac274
  xmodel/td12-formal-cascade-rank-v1-hostile-review-opus5-ccb-20260829.md
  body 25485 bytes:
  66b15f5d535d68a84c1324cdea826a067ceeb25345a637a8c53e79db07b7afc9
```

Its verdict is `PASS_WITH_REPAIR`.  Run record
`3f1cd34754b812377f86d87d7beb041c6a98d27794f83f3ff8ff980c56b5abf6`
is `DONE` on basis `ccb6cd52eeab95f169b40f0a48668c3acd7a607e`, with
stable prompt, adapter, charge-basis validator, `FALLACY.md`, and composed
model-prompt hashes.  This is not an exit claim; `charge_basis_status=ABSENT`
is correct.

## 1. Promoted formal quotient theorem

On the separately declared B and sibling routes, the eta-to-t root-floor
factorization gives the reduced operator `T_s` and the output lower floor

```text
eta^(e_s-1) P^(r-1) F_s C,
```

whose exponent at a t-root of multiplicity `m_j` is
`m_j(r+i)-s-1`.  For `1<=s<nu`, `T_s:C[t]->C[t]` is injective.  Its nominal
finite-cap cokernel and its intrinsic cokernel `C[t]/T_s(C[t])` both have
dimension `q`: two for B and three for the sibling.

The sharp natural-cap endpoint formula and both complete tables are promoted
with the added rider `n_*>=1`, which holds here because `q>=2` and
`0<M<nu`.  B has sharp cokernel one for `s=1,...,8` and two for
`s=9,...,24`; the sibling has two for `s=1,...,4` and three for
`s=5,...,16`.  This retires the earlier claim of one shared infinity
cokernel.

## 2. Repaired formal lift and binding disposition

The hostile review proves a stronger range than the producer claimed.  With

```text
i,r in Z_(>0),       r=3i/2,
F_s=product_j (t-a_j)^max(0,m_j*i-s),
```

arbitrary f-side jets in the declared `(V)/(W)` class admit the polynomial
g-side response

```text
g_hat=c_g f_hat^(3/2).
```

It satisfies the g-side vanishing ladder, weight class, and declared natural
cap, and solves every homogeneous Keller row `E_s` through

```text
s<=r=3i/2.
```

The clamped source floor above is mandatory when `s>i`.  Consequently the
binding disposition is

```text
NO_FORMAL_CASCADE_KILL_IN_WINDOW
  GIVEN 3i/2>=depth AND THE NAMED ROUTE OCCURS.
```

The B depth-24 window is therefore formally transparent for `i>=16`, and the
sibling depth-16 window for `i>=12`; integrality of `r=3i/2` forces `i` even.
The earlier riders `i>=24` and `i>=16` were sufficient but not sharp.
Direct-entry `i=6n` is not a premise of this formal theorem.

The response has `J=0` and solves only homogeneous rows.  The genuine Keller
content remains at the distant inhomogeneous order
`s*=D_F+D_g-kbar_F`.  Failure of this particular lift at `s=r+1` is not an
obstruction and does not identify a first bite.  The cap-preservation clause
is proved only for the declared natural cap; a larger source cap requires a
fresh additive-degradation calculation.

## 3. Control repairs

The rank/matrix cases use `i=30`.  The producer's order-two binomial control
instead uses `(i,r)=(6,9)`; both satisfy the integral type-`(2,3)` rider.
Opus independently checked the eta-level chain rule, every displayed order,
the depth-relevant thresholds B `i=16` and sibling `i=12`, and the sharp
failure at `r+1` of this construction.

The checker derives `(M,q)` from each multiplicity tuple.  A coordinated
change of the sibling tuple can therefore describe another internally valid
route without tripping an internal assertion.  Route identity is bound by
the published ordinary/optimized stdout hash

```text
35f6f1719154755b82c58d13db8fdc9045152f8f780053cca59102d6b9e6f008,
```

not by assertions alone.  This is the accepted repair; the frozen producer
checker is not rewritten.

## 4. Campaign consequence and scope firewall

Stop all further homogeneous-window cascade descendants.  A future purely
formal successor, if any, must target the inhomogeneous row `s*`, not
`s=i+1` or `s=r+1`.  The next source deliverables remain the separate
`TD12-B25-PAIRPACK/v1` and
`TD12-S17-SIBLING-PARENT-PAIRPACK/v1`.

This result supplies no `PairRef`, source vector, completion, polynomial
Keller partner, exact pair, landing, gate verdict, exclusion, or occurrence
theorem.  It does not identify the B and sibling source states.  No standalone
recurrence engine, AWS launch, counterexample, degree bound, or JC2 conclusion
is licensed.

<!-- END-SEALED-BODY::td12-formal-cascade-rank-v1-coordinator-integration-sol56-20260829 -->

## Seal (outside the sealed body)

- Body byte count: `5129`.
- Body SHA-256:
  `3dfaa86248c9dcc14dcb018b900104242fa98ed71bc33f699102cd8b15136b82`.
- Frozen input basis:
  `ccb6cd52eeab95f169b40f0a48668c3acd7a607e`.
