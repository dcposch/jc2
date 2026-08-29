# Result

## Exact upstream gate: PASS

The minimal bridge mutation broadens the existing constructor fallback from
`ImportError` to `(ImportError, NotImplementedError)`.  On the frozen
PassageMath host, the explicit libSingular constructor reproducibly refused a
polynomial ring over `ZZ[x,y]`, while the generic Sage multivariate polynomial
parent accepted the same commuting `Dx,Dy` shadow used by `ore_algebra`.

The upstream algebraic-integral example then produced a genuine order-two
telescoper `L`, nonzero Ore certificate `C`, and field certificate `B`.  Both
independent exact checks passed:

```text
(L - Dy*C) mod the composed Ore ideal = 0
L(t*y) - Dy(B) in the algebraic function field = 0
```

The frozen exact certificate is `job/output/upstream_certificate.json`, SHA-256
`8daac27d5f064381b4ee1066a8a4e3479294db3a694cbb67024ec2257d1c2969`.
The candidate SHA-256 is
`b8d0a75e6a292d3aff2b1f1da4a4a9649bf4d0f9dabbb075775feba0bf9c5d03`.

## Frozen rank-one control: TIMEOUT, no certificate

Only after the upstream exact gate passed, the worker charged the preregistered
rank-one control.  It remained inside
`annihilator_of_composition(ss=ss, xx=xx, yy=ya)` for the full four-hour inner
cap and terminated with exit code 124 at `CONTROL_COMPOSITION`.  It never
entered creative telescoping and emitted neither `control_candidate.json` nor
`control_certificate.json`.

This is a backend/computational incompatibility of the current generic
multivariate composition path with the control's size.  It is not a reducer
disagreement and gives no mathematical PASS or FAIL for the rank-one control.
The real frozen branch was therefore not run.

Exact resource record:

```text
inner wall time       4:00:00
inner user time       14404.79 s
maximum RSS           286564 KiB
swaps                  0
pipeline exit          124
worker exit            124
monitor exit           0
terminal               TIMEOUT_CONTROL
final group members    0
final swap             0 KiB
```

## Scope firewall

The upstream PASS certifies only that the two-line bridge/build workaround can
produce and exactly verify a real creative-telescoping certificate on the
published algebraic-integral example.  The timeout says nothing about the
existence of a control telescoper, the HENS-CT mathematical strategy, any
rank-one survivor, JC2, or any file outside this case.  No canonical file and
no `jc2-lean` file was read or modified.

