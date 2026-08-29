# td=12 U1 first trunk consumer (Grok 4.6, 2026-08-29)

Primary certificate for the displayed dirty chain cell of the source-pinned
`td=12`, `m=3`, `[2,2,2]`, type `(2,3)` U1 family. Exact `Fraction` / `int`
arithmetic only. No CAS, no caps, no other-packet imports.

## Charged commands

```sh
python3    test_trunk_consumer.py
python3 -O test_trunk_consumer.py
python3    trunk_consumer.py --emit /tmp/td12_u1_trunk.json
python3 -O trunk_consumer.py --emit /tmp/td12_u1_trunk-O.json
cmp /tmp/td12_u1_trunk.json /tmp/td12_u1_trunk-O.json
python3    trunk_consumer.py --cap 10 ; echo $?
```

Cap tokens are rejected (`CAP_TOKEN_REJECTED`). The executable is pinned to
`(w,M,budget)=(9/2,2,9)`.

## Scope

Reduced Prop. 8.1(iv) on the dirty trunk cell, plus the complete one-step
P0 menu from `(9/2,2)` at remaining budget 9 by the reviewed divisor law
`E | l*num(w)*T`. Does not prove landing, a Keller pair, a panel exclusion,
a td ceiling, gluing of `t^3-A`, or JC2.
