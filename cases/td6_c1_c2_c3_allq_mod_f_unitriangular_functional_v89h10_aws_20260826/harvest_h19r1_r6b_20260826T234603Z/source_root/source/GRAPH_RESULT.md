# TD6 V89H10G full-q transported-FIRST topology result

Date: 2026-08-26

Verdict: **PASS as exact producer telemetry; no unimodularity theorem yet.**

After rebuilding all 38 literal FIRST rows with all 22 licensed independent
q variables and imposing exactly `F=0` on `D(U)`, the registered relative
pivot matrix `B=A(0)^(-1)A(q)` has `N=B-I` with 532 nonzero entries and
6,069 affine-q coefficient terms.  Its exact digest is
`38fb14e38daa36d597cc7ae1cd2bd5dd402ef2cd1587337321b8c204eeeb7f36`.

The full support graph, and already the q2..q14 subgraph, has one cyclic SCC:

```text
(0,1,2,3,4,5,6,7,8,9,10,11,12,13).
```

All remaining nodes are singleton acyclic components.  The q16..q24-only
subgraph is entirely acyclic.  Thus the exact full-q determinant and inverse
problem reduces from 38 rows to one 14-by-14 low-q block followed by
unitriangular back-substitution; high q does not enlarge the SCC.

At each preregistered exact generic-E3 point—low q all one, all licensed q
all one, and alternating signs—the SCC-product determinant is exactly one.
These finite evaluations find no obstruction but are not a polynomial
determinant proof.  No P12 division or functional claim was made.

V1 failed at the first ancestor-import sentinel because its launcher omitted
`TD6_Q_EXPONENT=2`; it computed no math and is deployment-negative only.
R1 repaired only inherited environment sentinels.  Both R1 AWS runs returned
rc 0 with byte-identical stdout and mathematical artifacts.

Custody:

- R1 archive SHA `008a9c6e3c972e935376d505a9184c4a97870157f4258b409dfd4488a4eff216`.
- SOURCE_GRAPH SHA `f9adcc0c51dcf5844739aec433f37f218bcda6892dc0007ae541530118ec6b75`.
- Client SHA `38ebb6bd417408ef024b64660119691e89af09ac5996dd641c32d311a59fc162`.
- Byte-identical stdout SHA `859332b79367f134ce11c8e36ed310c59eb43b5b47e5cfd8a937f995d24aab49`.
- Affine-edge artifact SHA `f72294bd4e5d74627c3b5877dd8d6830a8a96d061294063df2a145ed3de00263`.
- Topology artifact SHA `e183ca51e02c7d21c7283f556b5a111a08e5b472627b9b5b6fb20c2183139176`.
- Point-determinant artifact SHA `d47b6551c8ca9922997b4ef28f95e44d2f0879a81caa5ac469c934e50ea7f0ed`.

No unit-ideal, source-point, total-Rees, whole-TD6, or JC2 conclusion follows.
All substantive computation ran on AWS; `jc2-lean` was not touched.
