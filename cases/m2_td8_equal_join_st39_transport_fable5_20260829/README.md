# m2_td8_equal_join_st39_transport_fable5_20260829

Verification packet for the Fable 5 primary report
`xmodel/m2-td8-equal-join-st39-coefficient-transport-primary-fable5-20260829.md`
(td=8 equal-join route, Statement 3.9 coefficient transport).

Standard library only; exact `Fraction`/Gaussian-rational arithmetic for
all load-bearing identities.  The P6 layer is a log-polar *monomial*
instantiation of the full vertex system (exact in the exponents, float in
one angle; tolerance comment in `LP.close`).  The proofs are in the
report; this packet replays the arithmetic.

Layers: P1 local ODE constants and pole family; P2 drop-vertex/degree
transport arithmetic and pinned tower stages, symbolic Euclid gcd chains;
P3 M*-gcd consistency; P4 exact leading-coefficient factors over Q(i);
P5 exact twin-cycle closure at t=1; P6 end-to-end instantiation at
t = 0, 1, 2, 10 with prefactor-invariance reruns.

Replay:

```sh
python3 st39_transport_check.py        # ST39_TRANSPORT_CHECK_PASS checks=24987
python3 -O st39_transport_check.py     # same
python3 test_st39_transport_check.py   # ST39_TRANSPORT_TEST_PASS checks=24987 mutations=2
```

The finite scans (t ranges) are regression evidence; the report's hand
algebra plus the symbolic Euclid identities are the all-`t` proofs.
