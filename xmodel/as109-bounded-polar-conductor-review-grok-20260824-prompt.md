# Hostile different-model review: AS109 bounded polar conductor

Act as a hostile independent mathematical reviewer.  Review the frozen
producer

`xmodel/as109-bounded-polar-conductor-gate-20260824.md`

at SHA-256

`2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b`.

Charged clean-bank basis is
`6f2e49e63d74493910fa357a8adc82f0e40d219a`.  Verify the frozen case manifest
from the repository root:

`cases/as109_bounded_polar_conductor_20260824/MANIFEST.sha256`

whose SHA-256 is
`aa07a878b41adfbe9e07beaa48aa793562fb49228ffae8982aa8773f600df4e2`.
Reread the cited wild-symplectic producer/review and A-infinity chain; do not
infer a polynomial lift or rational deck action from completion.

Return a self-contained Markdown report with an overall verdict and a
numbered verdict for each claim below.  Re-run the registered replay, but also
use an independent derivation or second engine for every load-bearing finite
calculation.  Do not edit producer, case, canonical, ladder, or notes files.

1. **Basepoint and exterior divisor.** Check over `Z_p<x,y>` that
   `C_p=(x-x^p,y/(1-p*x^(p-1)))` is integral restricted-analytic, reduces to
   `(x-x^p,y)`, and has determinant one.  Over `Qpbar`, check the denominator
   is reduced with exactly `p-1` vertical components of valuation
   `-1/(p-1)`, outside the closed unit bidisc.  Police the terminology: this
   exterior affine polar divisor is not automatically projective infinity or
   the Hensel factor `A_infinity`.
2. **No polynomial-gauge cancellation.** For an arbitrary polynomial
   `phi=(X,Y)` with `det J(phi)=1`—without assuming JC or invertibility—check
   the factorwise proof that `gcd(1-p*X^(p-1),Y)=1`.  Verify that etaleness
   gives quasi-finite point fibres and that multiplicities/reducible pullbacks
   are handled.  Decide exactly what is invariant under polynomial
   symplectic automorphisms versus merely noncancellable under Keller right
   maps.
3. **Completed-orbit orientation.** Check against the frozen wild theorem
   that a hypothetical polynomial lift `F` has a unique identity-branch
   restricted-analytic symplectic gauge in the orientation
   `C_p o Phi_F=F`.  No reverse composition, rationality, polynomiality,
   global generic degree, or deck descent may be inserted.
4. **Unbounded conductor.** Audit the definition and canonicity of
   `kappa_n(F)`.  Prove or refute that a uniform degree bound—or a uniform
   bound on the nested canonical support cardinalities—makes `Phi_F`
   polynomial and contradicts Claim 2.  Check that the exact conclusion is
   `kappa_n -> infinity`, not a growth rate and not nonexistence of a
   polynomial lift.
5. **Finite-cap compactness.** Audit the systems
   `B_(p,n)(D_F,D_phi)` on total-degree simplices.  Check reduction maps,
   finiteness/finite branching, and the Koenig-lemma inverse-limit argument.
   Determine whether nonemptiness at every depth really yields a bounded
   polynomial gauge and bounded polynomial composition over `Z_p`.
6. **All-odd-prime first cap.** Independently expand a general
   `Phi=id+p(r,s)+p^2(r2,s2)` modulo `p^3` at caps `D_F=D_phi=p`.  Check that
   depth two survives; the first-coordinate cap forces every degree-at-least
   two coefficient of `r` to vanish; first-order determinant one forces
   `[x^(p-1)y]s=0`; and the `p^2*x^(2p-2)y` coefficient in the second
   composition is necessarily one.  Treat `p=3` binomial valuations
   explicitly.  Decide whether this necessary subsystem proves the full
   nonlinear cap empty for every odd prime.
7. **Exact controls.** Re-run the frozen `p=3,5` replay and independently
   reconstruct its necessary digit matrices.  Confirm or refute variable
   counts `20,42`, coefficient/augmented ranks `12/13,32/33`, forbidden
   monomials `x^4*y,x^8*y`, and manifest/stdout hashes.  Sample agreement is
   only a control on the structural all-prime proof.
8. **Scope and successor.** The maximum licensed promotion is
   `POLAR-CONDUCTOR / UNBOUNDED-GAUGE`: every hypothetical polynomial lift
   has unbounded relative analytic-gauge degree/support; every fixed pair of
   simultaneous map/gauge caps fails at some finite depth; the cap `p,p`
   fails at depth three.  It does not exclude a polynomial lift, identify
   `A_infinity`, descend a deck action, run `p=109`, or decide JC2.  Judge
   whether quantitative conductor growth or a proved comparison with
   `A_infinity` is the smallest honest successor.

For each claim label `CONFIRMED`, `PARTIAL`, `REFUTED`, or `TYPE-FAIL`, give
the smallest failing identity if any, and state the exact promotion and
quarantine at the top and bottom of the report.
