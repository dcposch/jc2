# Different-model hostile review: V43C5 V2 exact total `a1^628`

You are the independent hostile reviewer.  Work in
`/Users/dc/code/math/jc2`.  Write exactly one report at

`xmodel/max12-812-order2-p0-total-rees-j2-a1-total-converter-v43c5-v2-hostile-review-grok-20260827.md`.

Do not edit any producer, evidence, ledger, or `jc2-lean` file.  Do not read a
different model's unpublished review of V43C5 V2.  This is a new review of the
combined total identity: neither the C4 nor G4 review is inherited as a review
of the converter.  Desk-scale exact checks are welcome, but do not run the
four-minute full producer locally or start heavy local algebra.  Stop any
diagnostic before 4 GiB RSS or sustained multi-core use; the charged AWS replay
is already exact and zero-swap.

## Charged object and theorem

Case:

`cases/max12_812_order2_p0_total_rees_j2_a1_total_converter_v43c5_v2_20260827/`

Freeze SHA-256:

`dab07efa6090152cb8e427992e871c2300c7131d2478c6645bffe9fc200046cd`

Charged proof circuit SHA-256:

`f8426bcf6bb4acbe4a2c12e1897588a7b8ce92bc02da84b7fc02d64d64c145e4`

Charged result SHA-256:

`215a64b27e3ea43fd3238158a5e07e686d3de4c7d12ff5bde0e691f916938299`

Claimed theorem: for the frozen literal total raw ordered-a1 rows through grade
19, in the ordinary polynomial ring

`S=Q[t,X19_total]`,

there is an exact 25-row arithmetic-circuit identity

`a1^628 = sum_j M_j(t,X) R_j(t,X)`.

Under the exact map

`Q[t,X19_total] -> Q[rho,X19_total]`, `t |-> rho^2`,

this yields a pure total certificate and thus the requested form with `W=0`.
There is no localization or division by `t`.

## Mandatory custody audit

1. Rehash `FREEZE.sha256` and verify every listed byte.  Report the exact
   proof/result/producer/prereg/AWS-evidence/source-manifest hashes.
2. Distinguish the wrapper's `v2_producer_sha256=d1238596...` from the result's
   inherited base-V1 `producer_sha256=00d3912a...`.  Decide whether this is
   transparently and sufficiently pinned, or a promotion blocker.
3. Confirm V1 is only a preserved pre-certificate failure at
   `('literal total map',59,70)`, not earlier mathematical evidence.
4. Confirm C4 and G4 input freezes, exact certificates, and completed reviews
   are the bytes charged by the combined freeze.  Do not accept their review
   conclusions as proof of the new composition; use them only as audited
   source identities.
5. Assess the exact custody scope of the locally frozen copy of the 1,989-file
   AWS source manifest (SHA `50cbf25b...`) and the immutable remote-source
   statement.  Separate any packaging nit from the polynomial theorem.

## Mandatory exact mathematical audit

Independently check the following chain, with explicit ring and types.

### A. Literal corpus/map

- There are exactly 70 named slots, 59 unique nonzero total rows, 11 zero
  slots, 66 positive variables, 65 rho-zero variables, and sole general-only
  variable `ez9`.
- The zero slots are exactly
  `Tg10_1` through `Tg10_7`, `Tg11_4`, `Tg11_6`, `Tg12_6`, `Tg13_6`.
- Every nonzero row is rehashed from its literal polynomial and every zero
  slot has the canonical zero hash
  `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`.
- Verify that the pinned total-row compiler really encodes `t=rho^2`, rather
  than introducing an unrelated parameter or silently discarding odd-rho
  terms.  State exactly what source check justifies the map.

### B. Source identities and bridge

- Replay or independently inspect the exact C4 identity
  `a1^104=sum C_j R_j(0)` on its 16 final literal rows.
- Replay or independently inspect the exact G4 identity
  `5*t^6*a1^4=sum G_i R_i(t)` on its 11 rows.
- For every used special row, verify that the converter checks
  `R_j(t)=R_j(0)+t Delta_j` coefficientwise, including exact divisibility by
  `t`, in the same variable alphabet.
- Check the sign: `H=-sum C_j Delta_j` must give
  `sum C_j R_j(t)=a1^104-tH`.
- Check that dividing the G4 multipliers by 5 is legal and produces exactly
  `t^6*a1^4`, with no hidden denominator in `t`.

### C. Circuit composition—the load-bearing point

Let `x=a1^104`, `y=tH`, and
`Phi=sum_(k=0)^5 x^(5-k)y^k`.  Check independently that the serialized final
multiplier roots are exactly

- `C_j*Phi*a1^4` for every C4 row, plus
- `(H^6/5)*G_i` for every G4 row,

with coincident row labels added once.  Check all 25 final labels and the
target exponent `4+6*104=628`.

Be especially hostile here: `final_sum_root`, `schema_rhs_root`, and
`target_root` need not be the same hash-consed DAG node because distributivity
and the two source identities are derivation rules.  Determine whether the
frozen record plus checked source identities and the exact sixth-power schema
constitute a complete typed derivation of

`sum M_j R_j = a1^4((x-y)Phi+y^6)=a1^4x^6=a1^628`,

or whether the producer merely annotates an unproved equality.  Trace every
substitution and scalar.  If a derivation edge is missing, classify it as a
real theorem blocker even if the abstract algebraic formula is plausible.
An independent tiny exact-Q check of the universal identity is encouraged.
Do not use random evaluation as evidence.

### D. Replay and mutations

Audit the exact reconstruction of all 950 expression nodes and all committed
roots.  Verify that each of the nine controls is meaningful and rejected:
wrong bridge sign; `1/5 -> 1/4`; power `6 -> 5`; target `628 -> 627`; final
`Tg19_7` multiplier deletion; literal `Tg15_7` generic corruption; literal
`Tg19_7` special-fibre corruption; zero-row-name deletion; and zero-row-hash
corruption.  Identify any mutation that tests only metadata rather than the
mathematical identity.

## Scope firewall

Even on PASS, conclude only membership in the frozen literal total raw
ordered-a1 grade-through-19 ideal.  Do not infer a terminal-receiver chain
map, source reachability, normalized K00, the order-two/maximum-twelve case,
or JC2.  Note explicitly that K00 transport remains separately untyped.

## Required report ending

End with exactly one token:

- `GROK_CONFIRMED_TOTAL_A1_628_V43C5_V2`
- `GROK_REPAIRABLE_TOTAL_A1_628_V43C5_V2`
- `GROK_REJECTED_TOTAL_A1_628_V43C5_V2`

State all blockers before the token and separate nonblocking custody/control
nits from mathematical defects.
