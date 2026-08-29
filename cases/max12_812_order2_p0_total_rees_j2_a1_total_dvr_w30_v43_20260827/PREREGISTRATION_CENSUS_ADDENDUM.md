# V43 preregistration census addendum

Date: 2026-08-27  
Status: **ADDITIVE CUSTODY CORRECTION; FROZEN QUESTION UNCHANGED**

## Custody and scope

The original preregistration remains byte-immutable:

```text
97fa7074ef0c116b87feb5d2edeac3b6788db603227361f78715b085468345a0
  PREREGISTRATION.md
```

This note corrects only the stale support census in Required construction,
item 1.  It does not change the frozen question, exponent `N=6`, weight 30,
row corpus, maps, controls, outcome policy, or resource caps.  In particular,
the question remains whether

```text
U(rho^2),  U(0)=1,  with  a1^6*U(rho^2) in J.
```

## Correct literal census and map

The literal regenerated total-rho alphabet through grade 19 has 66
positive-sigma-weight variables, while the rho-zero support has 65:

```text
X19^tot = X19^0 union {ez9},        |X19^tot| = 66,
                                         |X19^0| = 65,
S       = Q[rho,X19^tot],
sp      : S -> Q[X19^tot],          rho |-> 0.
```

The sole general-only term is

```text
Tg19_2 contains (3/8)*rho^2*a1*ez9
         =       (3/8)*t*a1*ez9,    t=rho^2.
```

Thus `ez9` is not rho-torsion: it is a positive-weight spectator after
specialization because its sole source-row coefficient is divisible by
`rho^2`.  The 70 literal total rows still specialize exactly to the frozen
rho-zero rows.  The frozen ideal is extended faithfully along
`Q[X19^0] -> Q[X19^tot]`.

The exact supporting corpus-map correction is pinned by

```text
d322d4177d4592d02100a8eaaa7841c463c44d7cd67b44cbdd6529f4bc721808
  xmodel/max12-812-order2-p0-total-rees-j2-a1-rho0-to-total-dvr-design-erratum-v43-sol-20260827.md
```

## Freeze rule

Every V43 source freeze created after this note must include both
`PREREGISTRATION.md` and this addendum in its source manifest.  Any compiler
or report that says the literal total-rho alphabet has 65 positive variables
is stale; 65 is only the rho-zero support census.  This correction cannot be
used to alter the preregistered mathematical decision or to reinterpret a
failed computation as a verdict.
