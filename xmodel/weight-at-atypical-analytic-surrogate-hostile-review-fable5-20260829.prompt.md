# Task: hostile review of a type-(2,3) analytic Keller surrogate

You are Fable 5, acting as an independent adversarial mathematical reviewer.
Work on repository basis commit
`31777ce90994a106aade85064c0d868e32863f94`.  Write exactly one deliverable:

`xmodel/weight-at-atypical-analytic-surrogate-hostile-review-fable5-20260829.md`

Write no other repository file, do not edit canonical ledgers, do not use git,
and do not enter, enumerate, search, read, build, status, modify, or control
`jc2-lean`.  Do not browse the web.  Temporary scratch outside the repository
is permitted.  Do not run Singular or any heavy/uncertain computation locally;
all requested checks are desk-scale exact algebra.

Review the sealed producer
`xmodel/weight-at-atypical-local-countermodel-sol56-20260829.md`, full SHA-256
`84afec54eb1f915ccb474a60ff72b1145ae4ffa7997a329fa8076dcbf59ea479`,
body SHA-256
`80b6fd58a0a141ec1a395c064c92bd2f7e206aa9eec9af15aea285aa69c6e350`.
Do not treat the producer as an oracle.  Consult the exact local definitions
and scope in
`xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md`
and its hostile review, but preserve the producer's explicit surrogate
boundary: it is not an actual polynomial-map quotient packet.

Attack, at minimum, and return a separate `CONFIRMED`, `REFUTED`, or `GAP`
verdict for each item:

1. The coordinate change and exact identity
   `dx wedge dy=s ds wedge dt=df wedge dg`, including the square-root branch,
   its uniform-in-`t` domain, and the original-variable interpretation.
2. The residual map `(P,Q)=(t^2,t^3+t)`, degree ratio `2:3`, and treatment of
   the self-intersection at `t=+-i` without merging source parameters.
3. The Hessian, central-fibre equation, two normalized branches, and local
   Milnor number one.  Check that no global polynomial atypicality is claimed.
4. For every finite `t_0!=0`, independently derive the fibre expansion and
   local `g`-degree two, including `t_0=+-i`.
5. At `t_0=0`, independently derive the two branch degrees `1+1`, and hence
   the analytic profile `w_an=2` and profile integral `I_an=2`.
6. Whether the formal height-three data `u=3`, `kappa^-=kappa^+=1`, `b^+=2`
   are correctly typed as a comparison profile rather than as an actual
   Eggers--Wall realization.
7. Scope: decide whether the report proves exactly that the isolated
   pointwise analytic ingredients do not imply strict excess, while leaving
   the full global Section-7 package and every actual polynomial-map theorem
   open.  Flag any remaining sentence that overclaims a dependency barrier.
8. Say whether the example adds unique value beyond the older local equality
   controls (especially its globally-in-`t` type-(2,3) residual map), and give
   the maximum exact statement safe to retain.

List every required repair and the cheapest useful successor.  An analytic
surrogate is not a polynomial map, a local Milnor cycle is not a certified
global atypical value, and formal height data are not an actual quotient
packet.  End the report with one standalone `<!-- BODY-END -->` line and no
seal block.
