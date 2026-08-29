# Coordinator integration: corrected DEPTH root-meet theorem

Date: 2026-08-28  
Lifecycle: **PROMOTED at the all-`M=1` DEPTH/H1 scope**

## Evidence

```text
b8d6e68678aed7cd83e8d754faa4053776a794a357c851517dc296db704da434
  xmodel/sigray-sheet6-depth-root-meet-reaudit-terra-20260828.md
656c257e5a01dc159166a2a0beef5e5f0e12e2b39b04fd8c0b4840ce46c4c168
  xmodel/sigray-sheet6-depth-root-meet-reaudit-hostile-gpt55-20260828.md
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
  refs/sigray_full.pdf
```

The different-model hostile verdict is `PASS-WITH-REPAIR`.  This integration
uses the review's repaired proof and does not amend either frozen report.

## Exact theorem

Use Proposition 9.3 with lower/rootward `F=(0,y)` and upper parent `G`,
`G=F+c`.  A genuine root merge has contact zero, hence

```text
F in V_(2,a) \ V_(1,a),
```

where `V_1` uses actual characteristic indices `j>=1`; otherwise Notation
3.4 would require the undefined `e_(-1)`.  Thus a genuine root merge is case
I, not case IV.  The application requires, as in the promoted MP anatomy,
`F,G in V_a cap T_a^searrow` and `D_F>0`.

Let

```text
K_G   = kappa_G(1-pi(G)),
P_G   = deg(p_G),
rho_G = D_G/P_G,
w_G   = (K_G-rho_G)/nu_G.
```

At the lower root, Proposition 8.1(i) gives
`p_F^full=(p_F^red)^i`.  If
`mu=mult(p_F^red,c)`, Statement 3.17 gives

```text
P_G=mult(p_F^full,c)=i*mu,
```

so `i=P_G/mu` is derived, not free notation.  Proposition 9.3(I)(c),(d)
and Statement 9.2 give

```text
D_F=(D_G+n P_G)/nu_G,
1=K_F=(K_G+n)/nu_G,
n in N*.
```

Consequently, with `X_F=D_F/i`,

```text
X_F=mu(1-w_G),                  (R1)
w_G=1-X_F/mu<1.                (R2)
```

The strict inequality uses `D_F>0`, `i>0`, and `mu>0`.

For an all-`mu=1`, `r`-way root meet, the promoted MP6/MP7 anatomy has
reduced root degrees

```text
(dp,dq)=(r,r+l),  r>=2, l>=1.
```

At `u=0`, Proposition 8.1(iv)'s top-degree cancellation gives
`X_F=dp/dq=r/(r+l)`.  Combining with (R1) yields

```text
w_G=l/(r+l) in (0,1).          (R3)
```

This top-degree proof replaces the producer's terse use of Proposition
9.3(b); equivalently (b) gives the same identity only after all of its case-I
and Statement-8.2 hypotheses are stated.

The reviewed DEPTH calculation at `td=6,m=2` gives `W(2)={2}` and
`gen(W)=0`.  Equation (R3) therefore excludes every all-`M=1` root meet in
that scope.  The interior two-pole residue
`Q=(6,12,3,2,5)` is nonroot and is not excluded.

## Boundaries retained

- Root `M=1` is legal.  The exact local `r=2,l=1` ODE/Q cell has
  `w=1/3` and `M_root=1`; it refutes any root extension of Proposition 8.4
  but is neither a Keller map nor a `td=6` reach model.
- For mixed `mu`, only (R1)--(R2) are proved here; formula (R3) is the
  all-`mu=1` anatomy.
- No off-axis/mixed-`mu` root completeness, coefficient realizability,
  global shared budget, full `BOOK(m,td)`, or JC2 exclusion is promoted.
- The nonroot finite-`W` and finite-menu theorem remains promoted.  The safe
  proved stabilization bound is `d0<=2*gen(W)+2`; `gen(W)+2` remains only
  empirically verified in general.  At `td=6`, both give `d0=2`.
- The corrected root-aware engines remain valuable completeness diagnostics.
  Their old finite caps and `M=1`-before-root pruning are still invalid; an
  AWS census cannot replace the analytic proof above.

No broad `twopole_check.py` run is evidence for this integration.  The
hostile reviewer interrupted that diagnostic when it exceeded the light
scope.  The promotion rests on the primary algebra, the frozen reports, and
the bounded `depth_closure_check.py` result recorded by the review.
