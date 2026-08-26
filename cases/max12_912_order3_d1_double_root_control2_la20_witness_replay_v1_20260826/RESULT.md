# Literal witness replay result

Verdict: `PASS`, subject to the same fixed-source firewall as the producer.

The registered r6d AWS run completed rc `0`, with empty compiler/CAS stderr,
empty hardened stdout-diagnostic file, and all required markers. Without
recomputing any saturation or Gröbner basis, it independently parsed the nine
frozen expanded generators and checked the producer's printed certificate by
literal polynomial arithmetic:

```text
s^96*la^20-s^97*TAIL-sum FINAL[i]*I[i] = 0.
```

It then checked the exact eight-term dehomogenized witness and primitive
integral scaling, enumerated every exponent vector, verified that no term
contains `s` or `rho`, and obtained

```text
WEIGHT_MULTISET=80x1,81x1,82x5,88x1
```

with the unique weight-80 monomial exactly `la^20`. This makes the seven
strict halfspaces in the producer's `CONE_PREMISES_PROVISIONAL.md` an exact
finite-support consequence. It remains a witness obstruction region, not a
full Gröbner cone; no equality face was tested.

Custody:

- tag: `max12_912_order3_d1_double_root_control2_la20_witness_replay_v1_20260826T024500Z_r6d`
- worker PID: `210328`
- compiled source SHA-256:
  `cba367e6c5aff8d199ef52f21a60152ee689d1fd5ca962fc8a349526f751b6a1`
- stdout SHA-256:
  `1fdddc051d8a7cdad2b6e250e4d9332897568cb9da436bfcb3c954dd2f35b297`
- runtime/max RSS: below timing resolution / `10120` KiB; no swap
- producer stdout pinned in compiled source:
  `a0611ede0e667d45f569a954fdaa73818f0ebea328212b8c46d4ccb0aa29fe08`

This replay corroborates a certificate copied from the producer stdout; it is
not an independent derivation of the equations. It proves nothing about
moving axis/load, nonzero `q2`, another source/support, equality faces, the
whole double-root fan, D1, or JC2.
