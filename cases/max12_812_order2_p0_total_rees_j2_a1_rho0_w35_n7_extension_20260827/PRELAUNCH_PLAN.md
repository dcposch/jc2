# Weight-35 / N=7 rho-zero extension plan

Date: 2026-08-27  
Status: **PREPARED, NOT LAUNCHED**

## Question

Let `J0` be the full frozen rho-zero raw ordered-`a1` ideal through grade
19, extended to the literal 66-variable total alphabet by the spectator
`ez9`.  Decide whether

```text
a1^7 is in J0.
```

A negative answer excludes every total identity `a1^7*U(rho^2) in J` with
`U(0)=1`.  A positive rho-zero answer is only a necessary gate for a total
certificate.

## Seeded extension before a full rebuild

The frozen exact N=6 functional `Lambda6` satisfies

```text
Lambda6(a1^6)=1,       Lambda6((J0)_30)=0.
```

Split the weight-35 monomials as

```text
R0_35 = a1*R0_30 direct-sum B35,
```

where `B35` is spanned by monomials not divisible by `a1`.  Start with

```text
Lambda_seed(a1*m)=Lambda6(m),       Lambda_seed(B35)=0.
```

Every product `a1*p` with `p in (J0)_30` is annihilated automatically.
For the remaining weight-35 products solve only

```text
A_B*x = -Lambda_seed(product)
```

for values on the active non-`a1` monomials.  A solution gives an honest
N=7 dual certificate immediately.  Inconsistency only refutes this fixed
extension of `Lambda6`; it is not an N=7 membership verdict.

If the fixed seed fails, form the correction block

```text
A30*delta = 0,        delta(a1^6)=0,
A_D*delta + A_B*x = -residual_seed,
```

closing the downshifted `a1`-divisible support under the complete weight-30
incidence relation.  This is the block form of testing
`a1^6 in (J0:a1)` and avoids recomputing already-satisfied `a1*(J0)_30`
rows.  Only if that block is not smaller should the unrestricted weight-35
dual be emitted directly.

## Staged execution and controls

1. Run `compile_w35_n7_seed_extension.py --phase preflight` on AWS only,
   initially under 192 GiB and one hour.  It records full product/component
   dimensions, the `a1`/non-`a1` split, seed residual support, forced rows,
   matrix nnz and estimated bytes.  Report these dimensions before a solve.
2. If the extension block fits, run an independent `F_65519` sparse
   extension solve first.  The exact N=6 denominator is nonzero modulo this
   prime.  Modular failure is diagnostic only.
3. On modular success, run exact Q with a six-hour cap on a 512-GiB-class
   AWS host.  Do not run heavy algebra locally.
4. Reconstruct all unrestricted weight-35 products from the literal emitter
   and replay the completed functional against every product, not only the
   target component.  Require `Lambda7(a1^7)=1`.
5. Mutate by one the unique target coefficient in a selected target product
   and require residual one.  Freeze source, matrix, solution, certificate,
   resource logs and complete manifests before considering N=8.

The compiler pins the exact N=6 certificate/result/compiler census, the
reviewed `0de6a2b2...` source theorem, the Fable5 additive review, and the
literal 66/65-variable census addendum.  No cutoff above weight 35 is in
scope.
