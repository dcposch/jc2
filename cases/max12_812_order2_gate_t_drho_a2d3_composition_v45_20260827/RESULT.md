# KGT-DRHO-UAC-A2D3 result

Date: 2026-08-27

Status: **EXACT-Q COMPILER AND VALIDATOR PASS; CONTACT EXCLUSION REMAINS
PROVISIONAL PENDING DIFFERENT-MODEL HOSTILE REVIEW.**

The frozen V45 verifier rebuilt the seven unspecialized general-`rho`
actual-total rows through grade 20 from the pinned V44 emitter and all 569
tails.  It matched each rational grade-20 row against the V44R1 canonical
hash and consumed the V44R3 exact-Q, `F_65521`, and cross-lane custody
results before taking the contact quotient.

For

```text
ord(A)=2, ord(C)=5, ord(R)>=3; d=3; G=17; T=20,
```

the verifier then obtained:

```text
lower contact vanishings:             20
pre-G zero row coefficients:          119 = 7*17
finite shifted-map entries:           29
total/D1 equalities, rho -> +lambda:  147 = 7*21
total/D1 equalities, rho -> -lambda:  147 = 7*21
total exact coefficient equalities:   294
```

The map was generated from the pinned `B23` inventory rather than entered
as a 29-line table.  It retains `ell1..ell3`; shifts the `A` jets at index 2,
the `C` jets at index 5, and the `R` jets at index 3; applies the forced
factor `2` to `C` and factor `4` to the constant `R` component; and maps
`k,k1,k2c` to the three `k10` jets.  The mechanically derived relative jet
depths are

```text
p/A/C=3, R=1, k10=2, k6=0, k2=0.
```

Here `k6=0` and `k2=0` mean leading-only declarations.  Neither leading
load occurs in a surviving row through grade 20.  The claimed maxima have
actual terminal source witnesses `ell3`, `az5/ac5`, `ez8/ec8`,
`cs4/rs4`, and `k2c`.

Both Kummer deck embeddings give identical hashes for all seven mapped row
windows `g=17..20`.  Separately, the verifier checks the cubic Hensel jet

```text
lambda0=epsilon*rho,
lambda1=-ell1/(2*lambda0),
lambda2=-(ell2+lambda1^2)/(2*lambda0),
lambda3=-(ell3+2*lambda1*lambda2)/(2*lambda0)
```

for `epsilon=+1,-1`, checks the two opposite-root allocations, pins both
orientation markers in the reviewed `B23` endpoint transcript, and pins its
exact terminal residue `(3/2)*rho^2*cv^2` and empty closed-`R` tail.

The registered AWS lane was
`max12_812_order2_gate_t_drho_a2d3_composition_v45_20260827T031200Z_q`
on `ip-172-30-0-34` (`r6i.16xlarge`, 64 vCPU, 512 GiB).  The exact compiler
used one core for 5m38.30s, peaked at 199,032 KiB RSS, used zero swap, and
exited zero under a 64 GiB virtual-memory cap.  The immutable results are

```text
ada147715900468e727c3c56b76f99d642bc9ffccce6f81a0dac704372036ad8
  aws_q_r6i/compiled/result.json
27c7c28db2e18522e5e13134a3581bb818e344fa564fa18d473378472d7f203e
  aws_q_r6i/RESULT.json
53ab25b43632ed85484de5a00439f5abeca1d57d5ec9a0f708a00a06772bc169
  aws_q_r6i/EVIDENCE.sha256
```

The exact result is a source/D1 finite-jet identity and custody composition.
The provisional contact consequence is: after the already reviewed
generic-square first-normal, half-weight, and exact reduced `M=0` gates,
the strict contact above is excluded on `D(rho*k)` by the reviewed `B23`
endpoint.  Different-model review must still attack the factorization,
index/factor map, endpoint import, localizer, root orientations, and
documentary adequacy before narrow promotion.

This is one contact only.  It is not a strict unique-`AC` cover, a
generic-square cover, an equality-face or positive-order-load statement, a
result on `k=0` or `rho=0`, a staged Rees-chart or terminal-receiver theorem,
either global `G2` obligation, Gate T, order two, maximum twelve, JC2, or a
counterexample.

