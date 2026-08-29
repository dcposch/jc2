# Different-model hostile review — pole-inflated U1 star family and PCB

You are Grok 4.6, an independent hostile reviewer in the Plane Jacobian
Conjecture campaign. Frozen git basis:
`93db679d3160c957b0610297afccc1f2fad53125`.

Review Opus 5's new primary report
`xmodel/td12-occurrence-coverage-attack-opus5-93d-20260829.md`, focusing on
two claims that must be adjudicated separately.

Claim A (`U1*(r)`, proposed exact interface no-go): for every odd `r>=3`,
the current promoted configuration axioms admit an abstract type `(2,3)`
star with `r` poles `(a,b,nu)=(1,2,3)`, `td=4r`, equal U1 arrivals, and a
one-step trunk family whose exact terminal laws are

```text
k | 3r-1, k<=r-1,
nu=3r+2(3r-1)/k, M=k+2, w=(k+1)/(k+2),
psi=k+1, lambda_floor=3r-1, budget=4r-k-2.
```

The report says every current configuration-level axiom is satisfied, local
T1 is solvable, and budget slack grows with r; therefore this interface
cannot force td12 or any td ceiling. Independently recompute the entry,
merge, MP2/N1, trunk, divisor, terminal, T1, source-mass, and budget laws.
Find any omitted axiom or illegal quantifier. Keep the family formal: no
actual occurrence or Keller map.

Claim B (`PCB`, explicitly conjectural): strengthen repaired Corollary 7.1
from `d>=1+sum wt` to `d>=s+sum wt`, where `s` is the number of pole places.
The report derives the exact fibrewise Riemann-Hurwitz identity

```text
sum_(non-pole infinity places)(e_F-1)=2g-2+d+s
```

and proposes a new pole-cluster Euler decomposition to supply the extra
`s-1`. Audit the actual proof of the promoted Section 7 weighted Euler
inequality and its different-model review. Decide whether the constant `1`
comes from global `chi_c(A2)`, whether pole clusters can legitimately alter
it, and whether RH ramification can be typed to the finite-value flag
weights. Label PCB `PLAUSIBLE_OPEN`, `DUPLICATE`, or `FALSE/UNSUPPORTED` at
the strongest justified level. State the smallest exact source audit or a
countermodel. Do not promote PCB merely because it kills U1*(r).

Also reconcile Claim A with the separate A7/C5 detour report if useful, but
do not let that distract from the two verdicts.

No web, AWS, heavy local CAS, commit, push, canonical edits, or external
messages. Never read, list, stat, grep, build, modify, or touch `jc2-lean`.
Write only `xmodel/u1-star-pcb-hostile-review-grok46-93d-20260829.md` plus
`/tmp` scratch. End with an exact body seal and basis. Omit `charge_basis=`
unless a new exit price is truly asserted. Fail closed.
