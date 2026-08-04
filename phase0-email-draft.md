# Draft: Phase-0 email to C. Valqui / J.A. & J.J. Guccione / R. Horruitiner

Subject: The open (72,108) case of your Jacobian Conjecture degree bound

Dear Professors Valqui and Guccione,

Following the July 20 counterexample to the Jacobian Conjecture in dimension 3,
the plane case — and with it your program's degree bound — has become newly
prominent. Your 2022 paper (arXiv:2204.14178) leaves exactly one case below 125
open: A0 = (8,28), (m,n) = (3,2), reduced in Proposition 4.3 to [P,Q] = x^2 with
prescribed Newton polygons, where the associated system of polynomial equations
resisted solution.

I am attempting to settle that case computationally, with modern dedicated
Groebner engines (msolve) rather than general-purpose CAS elimination, in two
independent formulations: (a) the direct bilinear coefficient system from
Proposition 4.3, and (b) your D_k-tower reduction. Three requests, if you are
willing:

1. Could you share the exact system (notebook or text) that you could not
   solve, and the modified form of the system St(n,m) for the case
   [P,Q] not in K^x that you mention in arXiv:1406.0886?
2. Do you recall the failure mode — memory/time blowup in the elimination
   itself, or an elimination that succeeded but produced a residual relation
   that resisted your valuation techniques?
3. Are you (or anyone you know of) currently working on this case? I have no
   wish to duplicate an effort already underway, and would be glad to combine
   forces — the result is the capstone of your program, and any writeup would
   naturally be joint or at minimum fully credited.

I will of course share anything I find, in either direction: a discard (raising
the bound to 125) or a surviving solution of the reduced system.

Best regards,
[name]

---
Contact leads: C. Valqui — PUCP (Pontificia Universidad Catolica del Peru);
J.A. & J.J. Guccione — Universidad de Buenos Aires / CONICET;
R. Horruitiner — PUCP (2018 MSc thesis).
