# V82QST1S sparse staged-pivot checkpoint

## Verdict

The dual-host sparse staged-EJet cells for q2 and q10 completed.  Both cells
preserve the reviewed ascending raw transport, restriction, source ancestry,
and direct-q-prime omission controls; only the staged FIRST/previous-pole/
CURRENT pivot selector is changed.

On both Box03 and r6d, the sparse selector reproduces the corresponding Gate 0
CURRENT result exactly:

| axis | rank/kernel | denominator support | reduced-coordinate SHA-256 | denominator-diagnostic SHA-256 |
|---|---|---|---|---|
| q2 | `1/1`, kernel 0 | `F*G*L*U^4*V^3` | `8177fac70f319030af2ac8e4c550c6ce7f7eb15e3bf376e3f64cdd795e9011ed` | `c4287f692d0b8e1dd644ce55e73b5148f8afb25557c5d988beb7839c753581b1` |
| q10 | `1/1`, kernel 0 | `F*G*L*U^2*V^2` | `212b7f81db6848ad52c814b98070fb15819c73588e6923b25ac1a9836619b2ed` | `c8c24573d54df557990418dd2305723f89609b9cd41517d802517f8302e91d2b` |

Each cell intentionally exits `rc=1` only after writing the exact table and
factor ledger, at the unchanged fail-closed foreign-factor assertion.  Thus
this sparse selector supplies no second principal open and no change in the
factor ideal for either endpoint axis.

## Execution and custody

- Source archive SHA-256:
  `7db94918342d4bfa0363cbe57a40a2ebdc9533124012bcb0a90051bb7605445f`.
- Box03 run root:
  `/home/ubuntu/runs/td6_v82qst1s_current_box03_20260826T090357Z`.
- r6d run root:
  `/home/ubuntu/runs/td6_v82qst1s_current_r6d_20260826T090357Z`.
- Each cell was capped at 2 GiB and 7,200 seconds.
- Both hosts passed the platform, source-closure, review-pin, shell, and Python
  syntax preflights.

The reverse-order q2/q10 cells from the same launch remain a separate live
experiment and are not consumed by this checkpoint.

## Scope firewall

This is alternate-pivot diagnostic evidence on the fixed source-typed A3 slice
and inherited staged localization.  It does not establish raw divisor-fibre
behavior, CURRENT obstruction on any excluded divisor, a Cech cover, or a
family theorem.  It does not license q3..q9 pivot expansion by itself.  No TD6,
SP-2, landing, or JC2 conclusion follows.
