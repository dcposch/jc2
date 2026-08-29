# Addendum: re-review of the cyclic semi-invariance patch

Date: 2026-08-28  
Reviewed coordinator hash: `e4f895ba51002e315221fa28efa60d55c79671fc9d210ac3130a3149abc8b42c`  
Verdict: **FAIL (one small remaining typing/citation gap).**

The patch fully discharges the first condition.  Statement 3.16 gives the
zero/nonzero `mu_nu` orbit decomposition; corrected Statement 3.18 realizes
a representative of every root orbit.  Two effective nonzero orbits, or a
zero and a nonzero orbit, give two branches first differing at `pi(G)`, hence
put `G` in `V_(2,a)`.  A zero orbit alone contradicts `nu_G>1` through
Statement 3.16.  Thus there is exactly one nonzero orbit and, correctly,

```text
p_G = C (eta^nu-c^nu)^l,  C,c != 0.
```

The added scalar is necessary under Notations 3.9--3.10 and harmless.  The
added `x`-side calculation and synchronized refinement rule also correctly
preserve the effective action and the one-character conclusion.

The ODE character computation is then correct **if** Proposition 4.6 is
typed at `G`: both left terms transform by `omega^(s-1)` and the nonzero
right side by the trivial character, so `s=1 (mod nu)`; the `nu=1` case is
automatic.

The patch does not yet prove that typing from the cited sentence
“Corollary 6.1 and tower persistence place `G` in `T_a^+`.”  In Notation 4.1
the relation `H preceq G` is defined only when both flags are already in
`T_a^+`; consequently the printed Statement 8.5 phrase
`F prec H preceq G` cannot, by itself, establish the missing membership.
Nor is the printed post-Proposition-4.2 “condition (7) is automatic” remark
a source proof; its repair is a separate corrected Proposition 4.2 input.

Smallest repair: insert the noncircular one-line check before invoking the
preorder.  Since `F in T_a^&` gives `d_F>0`, and `F=G+c` with
`u=pi(F)>v=pi(G)`, Statement 3.17 gives

```text
d_G = d_F + (u-v) deg(p_F) > 0,
```

so `G in T_a^+`.  Proposition 4.2 then defines its terminal polynomial
`h_G=h_(m_G,G)` with `h_0=g`.  Finally cite the promoted corrected
Proposition 4.2 (rather than the printed remark) for the condition-(7)
premise.  With those two explicit lines, Proposition 4.6 is typed and the
patch earns **PASS** for Statement 8.5.

This addendum does not change the earlier Section 7 boundary: the
arbitrary-truncation cyclic lemma supplies zero-order polynomial descent,
not the coefficient-chart/final-resolution identification.
