# V43C5 preregistration: exact special/generic converter to total `a1^628`

## Frozen question

Let `S = Q[t,X19_total]`, with `t` mapped to `rho^2`, and let `J` be the
literal frozen 59-row raw ordered-a1 ideal through grade 19.  Combine only:

1. the provisional exact V43C4 special certificate
   `a1^104 = sum_j C_j R_j(0)` in `Q[X19_rho0]`; and
2. the independently reviewed V43G4 total certificate
   `5*t^6*a1^4 = sum_i G_i R_i(t)` in `S`.

Decide constructively whether `a1^628` belongs to `J`, and serialize its row
multipliers as an ordinary-polynomial arithmetic circuit.

## Registered converter

For every special row, verify coefficientwise that

`R_j(t) = R_j(0) + t*Delta_j(t)`

and that the literal `R_j(0)` is byte-independent polynomial-equal to the C4
rho-zero row.  Set

`H = -sum_j C_j*Delta_j`, so

`B := sum_j C_j*R_j(t) = a1^104 - t*H`.

With `x=a1^104`, `y=t*H`, and

`Phi=sum_(k=0)^5 x^(5-k)*y^k`, replay the universal identity

`x^6-y^6=(x-y)*Phi`.

After rationally normalizing G4 by `1/5`, the registered final row
multipliers are

- `C_j*Phi*a1^4` on the special rows; plus
- `(H^6/5)*G_i` on the generic rows.

Their sum against the literal total rows is therefore exactly

`a1^4*((x-y)*Phi+y^6)=a1^(4+6*104)=a1^628`.

This derivation is purely polynomial: no localization, division by `t`,
completion, radical inference, or probabilistic identity testing.  Division
by 5 is allowed because the coefficient field is Q.  The result is stronger
than `a1^N*(1+rho*W)`: it has `W=0`.

## Exact replay and controls

The producer must:

- rehash and replay the complete V43C4 proof and V43G4 freeze/certificate;
- reconstruct all 59 literal total rows and all 66 positive variables from
  the pinned V43 source, including the general-only `ez9` variable;
- replay the G4 identity by direct exact sparse multiplication;
- verify all 16 C4 special-row fibres and every exact `Delta_j` division;
- serialize every multiplier as a hash-consed Add/Mul/Scale/Pow/Sparse DAG;
- reload the serialized DAG fail closed and reconstruct every registered root;
- check the universal sixth-power converter schema exactly over Q.

Required negative controls: wrong bridge sign; `1/5` changed to `1/4`;
converter power 6 changed to 5; literal Tg15_7 generic-row corruption; literal
Tg19_7 special-fibre corruption; final Tg19_7 multiplier deletion; and target
exponent 628 changed to 627.

## Verdict and firewall

Only
`PASS-A1-TOTAL-RAW-CIRCUIT-CERTIFICATE-A1-628-V43C5`
with complete hashes is a provisional positive verdict.  V43C4 review may run
in parallel, but both this converter and V43C4 require independent review
before promotion.  Scope is only the frozen literal raw ordered-a1
grade-through-19 ideal.  No terminal receiver, source-reachability, normalized
K00, order-two, maximum-twelve, or JC2 theorem follows automatically.

Run on AWS only, one core, 8 GiB virtual memory and twenty minutes.  Fail
closed on any source mismatch, map mismatch, mutation acceptance, resource
cap, or incomplete replay.
