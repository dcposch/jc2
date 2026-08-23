You are GPT-5.6 Sol, IMPLEMENTATION lane (own it end-to-end). Repo:
/Users/dc/code/math/jc72108. Execute the decisive bounded test recommended by
xmodel/sol-lift.md §3.3: CERTIFY (or refute) a characteristic-zero / p-adic lift
of the fully-reconstructed D43 residue-A witness at B=84. This advances Stage 2
of the algebraization gate; success = the first certified char-0 D43 point.

READ FIRST: xmodel/sol-lift.md IN FULL (esp. §1.2 the exact local lifting
criterion, §1.3 the certificate table, §3.3 the 4-step procedure), xmodel/
sol-d43full.md, and the engine cases/d43_full_family.py + certificates
cases/d43_full_certificate_p*.json. Char-0 target; work over Z_p / a number ring.

THE 4-STEP PROCEDURE (do real computation; use the existing 218-row assembler):
  1. COMMON INTEGRAL MODEL. Re-emit all 218 generators (34 parked + 95 old graph
     bands 6-24 + 89 late graph bands 26-42) over a common ring R = Z[1/N] (or
     directly over Z_p for p=105337), RETAINING the radical variables W_1,W_2,
     uW_i and their defining equations W_i^4 = A_i (do NOT substitute modular
     root values as integers -- keep them integral/radical). Audit that the mod-p
     reductions reproduce the banked systems (row/term/hash regression).
  2. p^2 CORRECTION TEST (cheap screen, eq 1.3). Take integral lifts x_1 of the
     banked mod-p witness xbar. Test whether the linear system
         J(xbar) * delta  ==  -F(x_1)/p   (mod p)
     is SOLVABLE using ALL 218 rows and the integral syzygies. SOLVABLE => the
     witness reaches p^2 (necessary, not sufficient). UNSOLVABLE => a genuine
     first-order LOCAL obstruction to lifting THIS point (report it precisely;
     it does not prove the whole char-0 family empty).
  3. LOCAL RANK/DIMENSION. Compute the full relative Jacobian rank c of the
     218-row system at xbar (block structure: parked 14 + graph 111 gave >=125;
     get the EXACT full rank), and the local ideal dimension at xbar. Beware the
     origin degeneracy Grok flagged (9 band-10 rows vanish at the FREE=0 origin)
     -- if the origin is too degenerate, move to a smooth point of the same
     modular component before certifying.
  4. STANDARD-SMOOTH CERTIFICATE => HENSEL. Find c generators and c variables
     with a c x c Jacobian minor that is a unit mod p (odd p, W_i != 0, so
     4W_i^3 is a unit -- the radical vars lift cleanly). Certify that these c
     equations locally generate the same ideal as all 218 and that the model is
     p-flat (local complete-intersection / flatness certificate). Then
     smoothness = formal smoothness => the point lifts through every R/p^n =>
     an R_p^ point => X_43(C) != empty (stacks 02H6 / infinitesimal lifting).

DELIVERABLE (write xmodel/sol-clift.md + emit engine/certificate JSON under
cases/): the integral model + reduction audit, the p^2 test result, the exact
local Jacobian rank + dimension, and EITHER a standard-smooth/Hensel certificate
(=> STAGE 2 CLEARED: first certified char-0 D43 point, state it) OR the precise
local obstruction found (=> a lead worth deciding family-wide). Honest tiers; do
NOT claim a char-0 point the certificate does not support. If the origin is
degenerate, say so and report the smooth-point search. No git, no msolve source
changes, no B=168 scale escalation (that is held for DC). Exact arithmetic.
Terse, technical.
