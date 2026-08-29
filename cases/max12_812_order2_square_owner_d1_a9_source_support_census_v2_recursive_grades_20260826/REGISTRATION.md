# Registration: correction-aware precursor for the D1 `a=9` source receiver

Date: 2026-08-26

Status: **PREREGISTERED DUAL-AWS NAVIGATION CLIENT; NO THEOREM ENDPOINT.**

The V1 literal-Faber census failed closed because it divided the raw source by
`sigma^27` after inserting arbitrary higher jets.  Those jets need not obey
the lower source equations.  V2 therefore makes no initial divisibility
assumption.  For each of the seven frozen Faber/source tails it recursively
extracts every coefficient at grades `0,...,31` by

```text
g_q = Q_q|_(sigma=0),
Q_(q+1) = (Q_q-g_q)/sigma,
```

and checks each polynomial identity exactly.  It prints every nonzero row and
its full variable-dependency support.  The substitutions and jet window are
identical to V1:

```text
p through sigma^4;
A=sigma^9(A0+...+sigma^4 A4);
C=sigma^10(C0+...+sigma^4 C4);
R=sigma^9(R0+...+sigma^2 R2);
k10 through sigma^2;
k6,k2 through sigma^4;
mu2 through sigma^3;
mu4,mu6,J retained.
```

This is a literal Faber/source diagnostic, not affine Laurent P2/P3.  It pins
the complete frozen tail ancestry and retains every lower load and target.

Run exact Q on Box03 and `F_65521` on r6d, each with a 16-GiB virtual-memory
cap, a 600-second compiler cap, and an 1800-second Singular cap.  Require
recursive quotient identities, exactly 224 row-status markers, rc 0, no
diagnostics, and zero swap.

## Acceptance and firewall

A PASS certifies only the exact coefficient census of this finite jet
substitution.  The first nonzero lower rows are constraints that a later
correction-aware quotient must carry; they are not contradictions.  V2 gives
no elimination, root allocation, arc, scheme, `a=9`, square, order-two,
`(8,12)`, maximum-twelve, or JC2 conclusion.  The tied-load Chebyshev/Pell
solution remains an expected survivor/control.

