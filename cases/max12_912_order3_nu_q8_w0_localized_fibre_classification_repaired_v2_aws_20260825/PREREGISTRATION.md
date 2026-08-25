# Preregistration: localized `w=0` classification repairs

Date: 2026-08-25  
Status: **FROZEN BEFORE V2 CAS**

1. Preserve the V1 case/report and review without byte mutation.
2. Search deterministically for the least prime `p>=5` at which the primitive
   corrected octic is irreducible.  Rabin's criterion must output both
   `x^(p^8)-x=0 mod Q8` and
   `gcd(Q8,x^(p^4)-x)=1`; a separately generated Singular factorization at
   that exact prime must have one degree-eight factor.  The parser must gate
   the factor count and degree.  By Gauss reduction, this certifies
   irreducibility over `Q`.
3. Run the literal characteristic-zero ideals
   `D(e6) cap D(Q8) cap V(e8)` and
   `D(e6) cap D(Q8) cap D(e8)` in two engine/order implementations.  Both
   are expected unit ideals because the parent non-Q8 open is unit; failure
   quarantines the repaired cover.
4. Every new run pins not only the compiler but also its transitive
   `order3_fibre.py` and descent-replay dependencies.
5. In prose distinguish the base Jacobian from the loaded Q8-singular ideal,
   which also contains `inu*e6-1`, and define the corrected octic only up to
   the harmless sign used by the generator.
