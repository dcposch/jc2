# Research lane: endgame of the 610 degree-zero linear-root chamber

You are a bounded primary research lane (paper mathematics; read-only).
Determine the terminal structure of the vanishing tower in the `(6,10)`
scale-two degree-zero chamber of the max11 campaign, and derive the closing
contradiction or a proof that more input is needed.

## Frozen input

Read from `dcposch/jc2-lean` at current `origin/master` (`d4e9bfe` or later),
project `max11-partial-y/`. The committed 610 modules
(`LowScale610*`, `Sol610*` tracked ones) plus the tracked green predecessors
of this chain. The live chain (untracked scratch, so re-derive statements
you cannot read; their reports are quoted here):

1. Source-honest wrapper: at a linear root `a` of the local scale `h0` of a
   literal normalized `(6,10)` source (after the Backwire peel and the
   affine depression), the order-69 head of the compact post-collapse
   numerator `Q` forces `p32(a)=0 ∨ q41(a)=0`, where `p32,p21,p1,p0` and
   `q53,q41,q3,q2,q1` are the depressed sextic/decic coefficient functions
   and `w1,a42,s2,u2,b63,lambda` the remaining compact coordinates. The
   order-69 monomial of `Q` is `7583143431241728 * p32^3 * q41`.
2. Order-70: on `p32(a)=0`, the head forces
   `p21(a)=0 ∨ (q41(a)=0 ∧ q3(a)=0)`; on `q41(a)=0`, it gives
   `p32(a)=0 ∨ 10 p32^2 q53 + (18 p32 w1 − 27 p21) q3 = 0` at `a`.
3. Order-71: on `p32=p21=0`, forces `p1=0` or a nine-term cofactor in
   `(p32n,p21n,a42,q41,q3,w1,p1,q53)`; on `p32=q41=q3=0`, an eight-term
   residual. (`p32n,p21n` are the next jet coefficients — the tower mixes
   first derivatives once a coefficient is pinned to zero.)
4. Live arms after order 71: `p32=p21=p1=0`; `p32=p21=0` with the nine-term
   cofactor; `p32=q41=q3=0` with the eight-term residual; `q41=0` with the
   five-term cofactor (this arm cannot use a clean compact-numerator
   coefficient without mixing `q41'`).

The tower's engine: `Q = h^69 * (jet quotient)`, the jet quotient's value
at the root is the degree-zero head, and a simple-pole/pole-order
obstruction from `degreeZeroPrimitive610_ratFuncDeriv_eq_simplePole`
forces each successive head to vanish on the current chamber.

## Questions

1. **What does the tower converge to?** If the vanishing propagates
   (`p32=p21=p1=p0=0` and/or the q-side analogue), what does total
   vanishing of one side's depressed coefficients at `a` mean for the
   literal source? Candidates: the depressed sextic acquires a root of
   multiplicity ≥ 5 at `a`, or the decic side degenerates — check what the
   landed normalization (leading coefficients `h^r` exactness, the
   Backwire peel data, discriminant/resultant facts in the committed
   LowScale610 modules) forbids. Identify the exact committed theorem that
   the total-vanishing limit contradicts, if any.
2. **Do the cofactor arms die uniformly?** The nine-term, eight-term, and
   five-term cofactors: are they nonvanishing on their chambers for degree
   or leading-coefficient reasons (same style as the 68 terminal closure:
   exact identity + impossible degree cases), or do they define genuine
   subvarieties needing their own towers? For the five-term arm blocked by
   `q41'` mixing: find the correct second-order object (e.g. differentiate
   the order-69 identity once in the source variable before evaluating)
   that unblocks it.
3. **Finite bound.** Is there a provable a priori bound on the tower depth
   (e.g. the pole order of the primitive, 69+depth vs the `h`-adic
   valuation budget of `Q`, which is a polynomial of bounded degree in
   `h`) after which vanishing of all heads is impossible? If `Q` has
   `h`-degree `T`, the tower cannot demand more than `T-69` orders — state
   the exact `T` from the committed jet-quotient definition and what
   happens at the ceiling.

## Report

Write `xmodel/max11-610-degree-zero-endgame-grok46-20260831.md` with
verdict `DERIVED` (closing argument for the whole linear-root chamber,
referee-checkable), `PARTIAL`, or `BLOCKED`, with all computations shown
and UNVERIFIED labels where you could not read a source. No overclaims.
