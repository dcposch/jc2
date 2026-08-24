# Independent research — exploit the AS `p=3`, depth-five cap-eight survivor

Work in `/Users/dc/code/math/jc2` at committed basis
`c327bdc8d02472feba42573760325099f34b8cdf`. This is a nonblocking research
lane, not a hostile review or promotion decision.

Read in full the committed AS chain:

- `xmodel/as109-wild-symplectic-conductor-gate-20260824.md` and review;
- `xmodel/as109-bounded-polar-conductor-gate-20260824.md` and review;
- `xmodel/as-gauge-growth-p3-depth4-gate-20260824.md` and review;
- its case replay and independent checker.

New exact producer checkpoint, not yet canonical: over `Z/243`, let

```text
A = x + 9*x^5 - 9*x^5*y
B = y + 9*x^4 + 198*x^4*y + 144*x^4*y^2
S5(A) = 1 + 3*A^2 + 9*A^4 + 27*A^6 + 81*A^8
P = A-A^3
Q = B*S5(A)
```

Direct exact reduction says `deg(A),deg(B)<=6`, `deg(P),deg(Q)<=8`,
`J(A,B)=1 mod 243`, hence `J(P,Q)=1 mod 243`, and
`(P,Q)=(x-x^3,y) mod 3`. Its nonzero reduced supports are

```text
P = 27*x^7*y + 216*x^7 + 234*x^5*y + 9*x^5 + 242*x^3 + x
Q = 81*x^8 + 135*x^6*y^2 + 189*x^6*y + 27*x^6
    + 144*x^4*y^2 + 207*x^4*y + 9*x^4 + 3*x^2*y + y.
```

First independently verify those identities without importing a producer
script. Then pursue, in order:

1. Derive the structural cancellation. In digit language the motif begins
   with `c=x^5(1-y)`, `d=x^4(1+y+y^2)` and a later correction
   `f=5*x^4*y^2+7*x^4*y`. Explain invariantly why the top Q carry cancels,
   why `{c,d}` becomes divisible by three, and how `f` absorbs the remaining
   divergence carry. Seek a Hamiltonian, boundary-Wronskian, or filtered
   identity that can be iterated rather than a lucky coefficient fit.
2. Decide the true depth-five minimum if tractable: can cap seven survive?
   Use source/gauge quotient, boundary jets, primary decomposition, or a
   certificate-grade finite solve. Do not claim D=8 minimal from the displayed
   survivor alone.
3. Attempt to lift the exact motif to depth six (`mod 729`). Test fixed cap
   eight first, then caps nine and ten only as needed. Reconstruct every
   candidate in the exact composed equations, with total-degree simplices and
   all integer carries. Record a survivor explicitly or a compact obstruction.
4. Look for a recurrence or a slower-than-`2n-1` cap-growth upper bound.
   Respect the reviewed polar theorem: every fixed cap must eventually fail,
   so a fixed-degree all-depth claim is impossible. A sublinear or stepped
   unbounded family would nevertheless materially change the disproof lane.
5. State exact scope. A finite-depth survivor is not a characteristic-zero
   polynomial lift, does not settle `A_infinity` or deck descent, and does not
   decide JC2.

Use exact arithmetic only. Put scratch programs and outputs under `/tmp`.
Do not edit producer cases, canonical files, notes, ladder files, prompts,
logs, or run records, and do not launch AWS. Write exactly one report:

`xmodel/as-depth5-survivor-successor-codex-20260824.md`

Include explicit formulas/certificates, reproducibility commands for any
`/tmp` scripts, the strongest exact result, and a precise next discriminator.
