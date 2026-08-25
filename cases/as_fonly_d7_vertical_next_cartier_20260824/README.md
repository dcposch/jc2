# Vertical first following Cartier gate

This portable producer derives and attaches the first following Cartier row
to the full-C5 vertical D7 gate.  It uses exact integer division before
reduction modulo three, then checks every structural base and every
first-digit Frobenius value.

Run:

```sh
./replay_all.sh
```

Expected runtime is about 10 seconds with less than 100 MB RSS.  No Singular,
Lean, AWS, or large-memory computation is used.

Scope is one finite next-digit lift on the charged vertical `p=3,D=7`
branch.  There is no recurrence, all-depth lift/no-lift, characteristic-zero,
counterexample, or JC2 claim.
