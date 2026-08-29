# V82QST Gate 0 — exact CURRENT denominator diagnostic

## Verdict

The preregistered q2..q10 diagnostic completed on two registered AWS hosts.
Every lane reached the exact CURRENT reduction, wrote its reduced-coordinate
table and complete denominator factorization, and then exited `rc=1` at the
unchanged fail-closed foreign-factor assertion.  This is an intended
diagnostic endpoint, not a producer PASS.

For every q-axis the reduced CURRENT vector has rank `1/1` and kernel
dimension zero over the staged fraction field.  Its common denominator is,
up to a nonzero rational scalar,

```text
F * G * L * U^a * V^b,

F = C*U - V^2 + U^3,
G = V^4 + 4*F^2,
L = 4*U^3*G^2 + V^4*(V^2+4*U^3)*(V^2+2*F)^2.
```

No additional irreducible denominator factor appears.  The exact axis ledger
is:

| axis | reduced coordinates | `(a,b)` | coordinate-table SHA-256 | denominator-diagnostic SHA-256 |
|---|---:|---:|---|---|
| q2 | 10 | (4,3) | `8177fac70f319030af2ac8e4c550c6ce7f7eb15e3bf376e3f64cdd795e9011ed` | `c4287f692d0b8e1dd644ce55e73b5148f8afb25557c5d988beb7839c753581b1` |
| q3 | 10 | (4,3) | `44cb535a44cfc4760f4352c67dd600fff4327f3a9dcd10fb948e408fd499f614` | `c4287f692d0b8e1dd644ce55e73b5148f8afb25557c5d988beb7839c753581b1` |
| q4 | 10 | (4,3) | `3952a8e416745068a7df6fc8458ffcb10c729789dd545bab99ac1c4a53c1bf78` | `c4287f692d0b8e1dd644ce55e73b5148f8afb25557c5d988beb7839c753581b1` |
| q5 | 7 | (4,3) | `84ca8552e64c7d2ffa87ce8d008164624624362aa16ac30fe75dfb6c521e4592` | `44ed62a320d72e458ecd98100776bfe537def1fcd357275b6b68e578f1073742` |
| q6 | 6 | (4,3) | `6df3d0de185f83060024092c5a7b1b89e8111079ad2ed1e7a5dcf3c1e456267a` | `0218b12341163000b92786aedcd74f5e16b603cc05bb4cb8455db8cd188766bd` |
| q7 | 5 | (3,3) | `7f289a12e4a50017d724b02c2b179405aab81b8bf0aae75d884ba04b17013fd4` | `0fc17fe56ff6504fae9d9d3e09eca1015c3b754aa4114ad3ccff357ed8b3ab89` |
| q8 | 4 | (3,3) | `c121f4cf039bddb983e6fee9da32ed6baa083afe3675bc3194859c781e697cdf` | `db33df15feb1074e851fa2fb4a54ec0c653a3a886c3a8099d94be2faf54c597f` |
| q9 | 3 | (2,3) | `d68bbd7cfecc03e7413136c7dcf4328b2a44ed015b16b24d04c3516c3ac6a7e1` | `e871d8f38ba054c120f9e7e858c3843393929a897e73a6dfb3a6c172e92a1a41` |
| q10 | 2 | (2,2) | `212b7f81db6848ad52c814b98070fb15819c73588e6923b25ac1a9836619b2ed` | `c8c24573d54df557990418dd2305723f89609b9cd41517d802517f8302e91d2b` |

The separate reviewed V82QSF package proves the displayed nested identities;
Gate 0 independently records that exactly those three foreign factors occur
in the staged CURRENT presentation.

## Execution and custody

- Box03 (`98.80.65.144`, `ip-172-30-0-249`) ran q2..q6 under
  `/home/ubuntu/runs/td6_v82qst0_current_box03_20260826T084017Z`.
- r6d (`100.26.198.153`, `ip-172-30-0-45`) ran q7..q10 under
  `/home/ubuntu/runs/td6_v82qst0_current_r6d_20260826T084017Z`.
- Each lane was capped at 2 GiB and 7,200 seconds.
- Source archive SHA-256:
  `1d1ecff404bd532f7d4a82ec274185ca4ec4933e83845b2db72cff7d1c05a30a`.
- Patched exact parent SHA-256:
  `ccf6f89292855fa94e01f93f582ba31d454b784618d73e60b390a0d54e2f6ce0`.
- Closure-manifest SHA-256:
  `d8244d6aa59603347b6e309fd913b140c3e40bf00eacf4ffabf5230b0d882e7b`.

## Scope firewall

This package is a denominator/presentation diagnostic on the fixed,
source-typed A3 slice and the inherited staged principal open.  Fraction-field
rank one does not prove a coefficient survives on any raw divisor fibre, and
the common denominator does not prove that the associated principal opens
cover the source scheme.  No q2..q10 CURRENT obstruction theorem, raw-fibre
empty theorem, family statement, TD6 closure, SP-2 statement, landing result,
or JC2 consequence follows.

Gate 2 raw substitutions remain conditional on the independently
preregistered alternate-pivot Gate 1 result.
