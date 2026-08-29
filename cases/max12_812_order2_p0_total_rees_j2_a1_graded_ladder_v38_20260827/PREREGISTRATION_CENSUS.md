# V38 preregistration A: AWS discovery census

Date: 2026-08-27

This first, separately frozen stage computes only the combinatorial sizes needed
to preregister the hardened ordered-`a1`, `rho=0` graded ladder.  It performs no
linear-algebra membership decision.  Heavy enumeration is permitted only in a
registered Amazon EC2 lane.

The source ideal is the same hash-pinned homogeneous raw-row ideal `I_19` used
by V37: every frozen ordered-`a1`, `rho=0` literal source row through grade 19.
V38 enumerates every monomial multiple of every nonzero row at each requested
weight and takes the exact bipartite connected component containing the target.
There is no cofactor-degree or total-degree cap.  Variables absent from every
source row remain faithful polynomial-extension spectators and are omitted.

The preregistered targets are

```text
W17 = a1*k^3       W18 = a1^2*k^2
W19 = a1^3*k       W20 = a1^4
W21 = a1*k^4       W22 = a1^2*k^3
W23 = a1^3*k^2     W24 = a1^4*k
W25 = a1^5
```

W17--W20 are census controls with frozen expected values inherited from V37.
W21--W25 are discovery censi.  The emitted fields are the number of all row
products, union support (including an isolated target), target-component row
products, target-component monomials, and component nonzero entries.  A second
AWS replay validator must independently reconstruct all nine censi.  Only the
validated, hash-bound output may supply expected constants to the subsequently
frozen decision stage.

This census has no mathematical implication beyond sizing and completeness of
the enumerated fixed-weight linear problems.
