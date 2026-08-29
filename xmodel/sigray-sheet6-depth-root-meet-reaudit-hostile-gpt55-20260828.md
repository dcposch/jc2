# Hostile re-audit of SHEET6-DEPTH root-meet re-audit

Date: 2026-08-28
Auditor: GPT-5.5 hostile independent pass
Target: xmodel/sigray-sheet6-depth-root-meet-reaudit-terra-20260828.md
Target sha256: b8d6e68678aed7cd83e8d754faa4053776a794a357c851517dc296db704da434
Primary reference: refs/sigray_full.pdf
Primary sha256: 9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae

No canonical file was edited. No AWS job was run. I did not enter, list,
search, read, build, modify, status, or control jc2-lean.

## Verdict

PASS-WITH-REPAIR.

The producer's central mathematical correction is right: a genuine root merge
is a contact-zero vertex in V2 \ V1, hence Proposition 9.3 case I, and the
case-I equations force the same strict root-side numerical obstruction that
the withdrawn case-IV argument was trying to use. In the all-mu=1 root-meet
scope this gives

```text
X_root = D_root/i = mu(1-w_parent),
w_parent = l/(r+l),
```

so the td=6, m=2 depth alphabet W={2} excludes the all-M=1 root meet. The
local r=2,l=1 root cell is still real at the reduced ODE/Q level and has
M_root=1; it is not a td=6 reach model.

Repairs are required because the producer overstates some interfaces:

1. The normalization i=P_G/mu must be justified from Proposition 8.1 at the
   lower root vertex plus Statement 3.17, not introduced as free notation.
2. Proposition 9.3(b) is licensed only under the full Proposition 9.3 and
   Statement 8.2 hypotheses. It is better to derive dp/dq=D_root/i at the
   root from Proposition 8.1(iv)'s top-degree cancellation.
3. "Universal root condition w<1" must be read as a necessary condition for
   a Proposition-9.3 root edge satisfying the relevant case hypotheses, not
   as a root-M=1 kill or a full campaign root exclusion.
4. The producer's check ledger must not report the broad twopole_check.py run
   as a completed light check unless run in an explicitly bounded/light mode.
   In this audit it was interrupted and not used as evidence.

## 1. Root membership and case label

Primary source check:

- Definition 3.2, p. 10: O(P,P*) is the first exponent at which coefficients
  differ. The constant coefficient is included.
- Definition 3.3, p. 11: (P,u) and (P*,u) are identified when u <= O(P,P*).
- Definition 3.4, p. 11: IP(O(P,P*)) is a V2 vertex.

For two y-side branches whose first common tree point is (0,y), their
constant terms differ before any positive exponent is shared. Hence
O(P,P*)=0 and IP(0)=(0,y) lies in V2. A genuine root merge is therefore not
case IV.

There is a necessary printed-reading repair in V1. Definition 3.1 introduces
alpha_0=0 "for technical reasons", but Notation 3.4 later assigns
nu_F=e_{j-1}/e_j at a V1 point. If j=0 were admitted as a characteristic
vertex index, e_{-1} would be undefined and Proposition 9.3's case IV would
be vacuous at (0,y). The only coherent reading is:

```text
V1 uses actual characteristic exponents alpha_j with j>=1.
```

Under that reading a genuine root merge satisfies

```text
(0,y) in V2,a \ V1,a,
```

so Proposition 9.3 selects case I for each incoming edge. This confirms the
producer at lines 18-21 and 119-128, modulo making the j>=1 repair explicit.

## 2. Prop 9.3 hypotheses and normalization

The orientation in Proposition 9.3 is lower/rootward F and upper parent G,
with G=F+c. For a root meet, F=(0,y). The equations can be used only after
the following are established:

```text
F, G in Va cap Ta&,
G = F+c,
F is the genuine root merge in V2 \ V1.
```

This is not cosmetic. Proposition 8.1 also needs F in Ta&, and Statement 8.2
is part of the derivation of Proposition 9.3(b). The all-M=1 root-meet
applications in the MP/DEPTH package do assert the required Ta& status, but
the report should say so before using the algebra.

Now fix one incoming edge. Let

```text
K_G   = kappa_G(1-pi(G)),
P_G   = deg(p_G)       full degree at the upper parent,
rho_G = D_G/P_G,
w_G   = (K_G-rho_G)/nu_G.
```

At the lower root F, Proposition 8.1(i) gives

```text
p_F^full = (p_F^red)^i_F.
```

If mu=mult(p_F^red,c), then Statement 3.17 applied to G=F+c gives

```text
P_G = mult(p_F^full,c) = i_F * mu.
```

Thus the producer's i=P_G/mu is valid, but it is not an independent
normalization. It is the root i_F transported through Statement 3.17 and
Proposition 8.1. This is the required repair to target lines 22-27 and
135-142.

## 3. Case-I root handshake

In case I, Proposition 9.3(c),(d), p. 50, give

```text
D_F = (D_G+n P_G)/nu_G,
K_F = (K_G+n)/nu_G,
n in N*.
```

Statement 9.2, p. 48, gives at the root:

```text
nu_F=1,
K_F=kappa_F(1-pi(F))=1.
```

Therefore K_G+n=nu_G. Dividing the D equation by i=P_G/mu gives

```text
X_F := D_F/i
     = mu(D_G/P_G+n)/nu_G
     = mu(rho_G+n)/nu_G
     = mu(nu_G-K_G+rho_G)/nu_G
     = mu(1-w_G).
```

This re-derives the producer's key formula. Positivity is also not optional:
for the root Ta& applications D_F=d_F>0 and i,mu>0, hence X_F>0 and

```text
w_G = 1 - X_F/mu < 1.
```

A weaker route is equation (d) alone: K_G+n=nu_G with n>=1 gives K_G<nu_G,
and rho_G>0 then gives w_G=(K_G-rho_G)/nu_G<1. The full X formula is still
useful because it identifies the root pattern parameter.

## 4. Equation (b) attack

The producer line 36 says Proposition 9.3(b) gives X_F=dp/dq=r/(r+l). This
is repairable but too terse.

Proposition 9.3(b) is not an independent axiom. The proof on p. 51 derives
it from (a),(c),(d) and Statement 8.2. Therefore it may be invoked only
inside the exact case-I/case-II hypotheses, with the lower F non-pole and in
Ta&. At the root meet those hypotheses are intended, but they need to be
stated.

The cleaner root derivation avoids (b). Proposition 8.1(iv), p. 40, at
u=0 is

```text
delta p q' - p' q = p.
```

At the root delta=d_F/i=D_F/i=X_F because kappa_F=1 by Statement 9.2. In
the all-mu=1 root anatomy MP6/MP7 give

```text
deg p = dp = r,
deg q = dq = r+l,
l>=1.
```

The highest degree term on the left has coefficient

```text
delta*dq - dp.
```

Since dq>1 and dp+dq-1>dp, the top term must cancel. Hence

```text
X_F = delta = dp/dq = r/(r+l).
```

Using Proposition 9.3(b) gives the same answer after substituting (c),(d)
and K_F=1, but the top-degree argument is less fragile and should be the
filed proof.

## 5. All-mu=1 root formula

Combining the case-I handshake with the all-mu=1 top-degree value gives

```text
X_F = 1-w_G = r/(r+l),
w_G = l/(r+l).
```

Since r>=2 at a genuine merge and l>=1 in MP7's root correction, this lies
strictly in (0,1). This confirms the producer's formula at lines 35-39 and
178-194 after replacing the equation-(b)-only citation by the repaired
derivation above.

Do not generalize this beyond its inputs. The formula w=l/(r+l) is the
all-mu=1 root formula. For mixed mu, the case-I identity remains
X=mu(1-w), but the simple l/(r+l) expression is not established here.

## 6. td=6 exclusion

The canonical DEPTH input gives the row-1 td=6 value

```text
w_0 = 2,
W(2) = {2},
gen(W)=0.
```

This is recorded in ladder/SHEET6-DEPTH.md:218-223 and reproduced by
cases/depth_closure_check.py. Every incoming all-M=1 root edge would need
w=l/(r+l) in (0,1). Since the only available incoming depth value is w=2,
there is no all-M=1 root meet in the td=6, m=2 DEPTH scope.

The exclusion is analytic. It does not require the old l-free phase-3 root
enumeration, and it does not require an AWS recensus. It also does not kill
the interior two-pole residue Q=(6,12,3,2,5); that residue is nonroot.

## 7. Local r=2,l=1 model

The producer's local countermodel to a root extension of Proposition 8.4 is
correct.

Take a!=b and

```text
p(eta)=(eta-a)(eta-b),
s(eta)=eta-(a+b)/2,
q(eta)=p(eta)s(eta).
```

Then

```text
2 p s' - p' s = -(a-b)^2/2 != 0.
```

For delta=2/3,

```text
delta p q' - p' q = -(a-b)^2 p/6,
```

so the reduced ODE has the required scalar-p multiple. The root reduced
degrees are (dp,dq)=(2,3), hence M_root=gcd(2,3)=1.

At Q level, set each incoming parent to

```text
(D_G,P_G,nu_G,M_G,K_G)=(3,3,3,1,2),
mu=1,
n=1.
```

Then rho_G=1 and w_G=(2-1)/3=1/3. Case I gives

```text
D_F=(3+3)/3=2,
K_F=(2+1)/3=1,
P_F=i*dp=3*2=6,
M_F=1.
```

This is a local root-M=1 model, not a Keller map and not a td=6 row-1 reach
model. It has incoming w=1/3, while the td=6 chains have w=2.

## 8. Stabilization boundary

The producer is correct to preserve the safe stabilization theorem and not
the sharp proof.

The nonroot DEPTH mechanism gives a finite W alphabet by the divisibility
and numerator-contraction law. The replay proof in the reviewed DEPTH file
does not prove d0=gen(W)+2 in general; the hostile review at
ladder/SHEET6-DEPTH-REVIEW.md:194-229 explains why neutral steps may be
needed between resonant steps. The safe proved boundary is

```text
d0 <= 2*gen(W)+2.
```

At td=6, gen(W)=0, so both the safe and sharp bounds give d0=2. No td=6
conclusion changes.

## 9. Repair map for the frozen producer

Apply these repairs to
xmodel/sigray-sheet6-depth-root-meet-reaudit-terra-20260828.md:

1. Lines 18-21 and 110-128: PASS, but add the formal V1 repair
   "j>=1 actual characteristic exponents" as a hypothesis required to keep
   Notation 3.4 and Proposition 9.3 coherent.
2. Lines 22-27 and 135-142: repair i=P_G/mu by inserting the derivation
   P_G=mult(p_F^full,c)=i_F*mu from Proposition 8.1(i) at the lower root
   and Statement 3.17.
3. Lines 29-34 and 161-168: PASS after adding positivity and hypotheses:
   F=(0,y) must be in Va cap Ta&, D_F>0, i>0, and mu>0.
4. Lines 35-39 and 184-188: replace "Proposition 9.3(b) gives" by either
   "Proposition 9.3(b), under its full hypotheses, gives" or preferably by
   the Proposition 8.1(iv) top-degree cancellation proof.
5. Lines 54-63, 196-199, and 409-416: replace any bare "universal root"
   wording by "necessary for a Proposition-9.3 root edge under the case-I or
   case-IV hypotheses." Do not let it read as a root-M=1 kill or a global
   root exclusion.
6. Lines 201-250: PASS at the all-M=1 DEPTH/H1 scope. Add an explicit
   exclusion of mixed-mu/off-axis/global-book promotion.
7. Lines 374-401: repair the check ledger. In this audit,
   cases/twopole_check.py was interrupted after it moved outside the light
   scope; do not cite a full PASS for it. The td=6 root conclusion rests on
   the exact algebra plus depth_closure_check.py, not on that broad script.
8. Lines 421-427: keep safe d0<=2*gen(W)+2 as PASS; keep gen(W)+2 as
   empirical/unproved unless a chaining lemma is supplied.

## 10. Scope

Promoted by this audit:

```text
genuine root merge = V2 \ V1 and Prop 9.3 case I;
case-I root identity X=mu(1-w);
all-mu=1 root formula w=l/(r+l);
td=6,m=2 all-M=1 root-meet exclusion from W={2};
local r=2,l=1 root M=1 ODE/Q model;
safe stabilization d0<=2*gen(W)+2.
```

Not promoted:

```text
root extension of Proposition 8.4;
root-deleted BOOK(m,td) as exhaustive;
mixed-mu root completeness;
off-axis root packages;
coefficient/Puiseux realizability of the local ODE model;
global shared-budget/multipole first-exit claim;
full JC2 exclusion.
```

## 11. Light exact checks run

```text
$ shasum -a 256 xmodel/sigray-sheet6-depth-root-meet-reaudit-terra-20260828.md
b8d6e68678aed7cd83e8d754faa4053776a794a357c851517dc296db704da434

$ shasum -a 256 refs/sigray_full.pdf
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae

$ python3 cases/sigray_rootaware_smoke.py
ROOT-AWARE SMOKE PASS: 8 checks

$ python3 cases/depth_closure_check.py
PASS reached w-set == {2} (got [Fraction(2, 1)])
PASS no resonant (l>=1) chain step admissible anywhere (Delta|2 empty)
PASS arithmetic closure W(2) == {2}, gen 0
PASS cumulative jump menu constant for all depths 1..12
PASS td=6 corrected jump menu == {IIa (2,3,1) M=2}
ALL CHECKS PASS

$ python3 <inline exact Fraction gate>
PASS exact root r=2,l=1: w=1/3, root D=2,K=1, ODE constant=-2
```

I also started `python3 cases/twopole_check.py`, but interrupted it because
the broad run exceeded the intended light-check scope and began producing a
capped diagnostic enumeration. It is not used as evidence in this verdict.
