# Q3-to-Q0 constructive completion after a restored Q4 model

Consume the exact full-Q4 restoration producer at SHA-256
`9fa649802565ad52a448c23e8091e9bdeca90576d35834a61ae19ed701fb119c`.
For each directly replayed Q5 SAT model, first reconstruct its canonical
degree-five restoration `(H5,J5)`.  Then descend source degrees 3,2,1,0.
At degree `d`, compute the literal integer determinant row divided by 81,
solve the full F3 divergence equation with a homogeneous degree-`d+1`
fourth digit, and directly verify divisibility by 243 before descending.

Every higher row must remain divisible by 243 after each step.  At the end,
the literal determinant minus one must be coefficientwise divisible by 243,
the total-degree support cap must remain seven, and the map must reduce
exactly to `(x-x^3,y)` modulo three.

As a finite-ring positive control, lift target `(0,0)` independently from
the three source residue balls `(0,0),(1,0),(2,0)` and verify three distinct
preimages modulo 243.  This is not an inverse-limit node and licenses no
Qbar/C collision or counterexample claim by itself.

All substantive execution is AWS-only.  The first two structurally distinct
input models are mandatory; the third is a component-dependence control.

