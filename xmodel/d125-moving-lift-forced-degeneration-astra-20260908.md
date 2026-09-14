# D125 moving-lift family: a forced finite degeneration, not a fixed-source boundary

2026-09-08. **UNREVIEWED DESK PASS after correcting the lift.** A hypothetical
guarded14c point gives an explicit polynomial-coefficient arc in the complete
moving-lift family, with center (ell,kappa)=(0,0) and receivers H³,H⁵.
This extends the known punctured scaling to a precisely typed finite arc.
It does not produce an arc in the ell=1 family excluded by accepted15g.
No source point, properness, exclusion or JC2 result is claimed.

## 1. Correction, source and target family

The seed omitted a mandatory term. Accepted14c uses

```text
phi_1(g)=v^-1, phi_1(p)=uv^4-v-v^-1,
phi_ell(g)=v^-1, phi_ell(p)=uv^4-ell*v-v^-1.       (1)
```

The proposed p=uv^4-v would instead be the sheared coordinate p+g;
that shear changes the printed receiver H and faces. No such silent shear
is used here. The root acknowledged this correction before further work.

Let R be any nonzero Q-algebra with a guarded14c solution (A,B,k), k a unit,
including a possibly nonreduced R. Set c0=-5/9 and H=p²(g³+p³). The literal
odd polygons are those with nonorigin vertices

```text
A: (0,15),(9,6),(2,1);   B: (0,25),(15,10),(1,0).
```

All coefficients on the total and second faces are prescribed, including
zeros; constants and all even total degrees are zero. The nonzero faces are

```text
A_15=H³, A_inner=k*g²p+g⁹p⁶,
B_25=H⁵, B_inner=(5k²/9)g+(5k/3)g⁸p⁵+g¹⁵p¹⁰,
[A,B]=c0*k³*g².
```

Every ordinary-lift equation for (1) at ell=1 is imposed.

Define the NEW moving family M over Q by the same coefficient slots,
faces with k replaced by kappa, complete Jacobian target c0*kappa³*g²,
and ALL negative-v rows of phi_ell(A),phi_ell(B). Thus it retains the
entire660 Jacobian envelope and30+75 polynomiality slots, including
identically zero rows. No compression, omitted residual or new gauge is used.
The closed family has no kappa-inverse or ell-inverse row: the prospective
center is not guarded. Generic guards will be retained.

## 2. Complete source arrow and all faces

For an indeterminate s put

```text
A_s(g,p)=s^15 A(s^-1 g,s^-1 p),
B_s(g,p)=s^25 B(s^-1 g,s^-1 p),
ell_s=s²,                   kappa_s=k*s^12.       (2)
```

A coefficient of degree n in member D is multiplied by s^(D-n).
The support bound n<=D proves regularity over R[s] for EVERY coefficient.
No slot is added. Zeros remain zero; the entire degree-D face is unchanged.
The second-face transport is exactly

| slot | coefficient | factor | required value at kappa_s |
|---|---|---|---|
| A_(2,1) | k | s^12 | kappa_s |
| B_(8,5) | 5k/3 | s^12 | 5kappa_s/3 |
| B_(1,0) | 5k²/9 | s^24 | 5kappa_s²/9 |

The remaining nonzero inner endpoints (9,6),(15,10) are on the fixed total
faces; their factors are1. These are all prescribed nonzero coefficients;
every other coefficient on those faces is zero and stays zero.
At s=0 the lower guarded vertices disappear, as allowed in the closed
moving family, rather than being falsely declared nonzero there.

The chain rule, with bracket ordered (g,p), gives

```text
[A_s,B_s]=s^38[A,B](s^-1g,s^-1p)
         =c0*k³*s^36*g²=c0*kappa_s³*g².           (3)
```

Each degree-n Jacobian residual row is multiplied by s^(38-n);
n<=38, and the scalar target belongs to n=2 and gains s^36.
All rows, including zero/top/target rows, are transported literally.

## 3. All polynomiality rows; no pole in the ordinary coefficients

The crucial corrected identity is

```text
s^-1 phi_(s²)(p)
 = (sv)^4(s^-5u) - sv - (sv)^-1.
```

Consequently

```text
P_s=phi_(s²)(A_s)=s^15 P(s^-5u,sv),
Q_s=phi_(s²)(B_s)=s^25 Q(s^-5u,sv).               (4)
```

This first holds in the Laurent ring where s,v are inverted, but every
coefficient is regular in s. Indeed a term g^i p^j using t copies of uv^4,
d copies of -ell*v and j-t-d copies of -v^-1 contributes at

```text
u^t v^e,       e=5t+2d-i-j.
```

After (2) its s-exponent is

```text
D-i-j+2d = D-5t+e >=0.                           (5)
```

Every contribution to a given row has this SAME exponent. Thus the entire
row equals s^(D-5t+e) times its ell=1 value. If that exponent is negative,
there are no contributions at all, by n=i+j<=D; the row is identically zero,
not a row multiplied by an illicit denominator. Every negative-v coefficient
therefore vanishes. The finite ordinary polynomials P_s,Q_s lie in R[s,u,v];
this proves more than a formal Laurent germ. Multiplication/localization in s
is injective even for nonreduced R, so no reduction-to-points step is hidden.

The determinant of (g,p)=phi_ell(u,v) is v², independently of ell.
Thus (3) yields J_(u,v)(P_s,Q_s)=c0*k³*s^36, also obtained directly from
the physical scaling determinant s^-4 in (4). Its leading scalar c0*k³
is a unit; no sign or leading-unit hypothesis has been lost. For s!=0
the exact physical degrees75/125 and leading monomials u^15v^60,u^25v^100
remain; their factors in (4) are1.

Odd parity improves the parameterization: D-n is always even. Put r=s².
Then the family descends WITHOUT adjoining any root:

```text
ell=r, kappa=k*r^6,
a_ij(r)=r^((15-i-j)/2)a_ij,
b_ij(r)=r^((25-i-j)/2)b_ij,
J(P_r,Q_r)=c0*k³*r^18.                           (6)
```

The corresponding exponent in (5) is even. For a field point this is a
genuine K[r] coefficient arc and hence a K[[r]] arc, with ord ell=1,
ord kappa=6 and nonzero Jacobian leader. The displayed s-arc is its
ramified pullback, not a needed field extension.

## 4. The center and the exact closure claim

At r=0 only the total faces survive:

```text
A_0=H³, B_0=H⁵, H=p²(g³+p³), ell_0=kappa_0=0.
```

Ordinariness at this center is directly visible in a degree-five identity,
without expanding H³ or H⁵. With w=uv^5,

```text
phi_0(H)=u(w-1)²(w²-3w+3)=:C(u,v).               (7)
```

Thus P_0=C³,Q_0=C⁵ are ordinary and commute. Their leading monomials still
give exact total degrees75/125; their Jacobian is zero, not Keller.
Over an algebraic closure g³+p³ splits into three distinct lines. This is
not the cubic g³+p³-3p used by the ell=1 pure-center arguments.

The center is an unguarded point of M regardless of whether a guarded14c
point exists. The NEW conditional content is that a guarded14c point forces
this very center into the kappa-saturated closure of M's guarded locus.
If T is its finite polynomial coefficient ring and I_M its entire ideal,
(6) gives T/I_M -> R[r]. The image k*r^6 is a nonzerodivisor because k is a
unit. Hence any f with kappa^N f in I_M also maps to zero. The arc factors
through I_M:kappa^infinity, retaining nilpotents; evaluating at r=0 gives
the claimed center. No abstract grading, automatic degeneration theorem,
flatness of the whole family, or existence of a guarded point was assumed.

## 5. Why this does not contradict15g; precise history delta

On ell!=0 normalize the moving family back to ell=1 by

```text
a_hat_ij=ell^((i+j-15)/2)a_ij,
b_hat_ij=ell^((i+j-25)/2)b_ij,
k_hat=kappa/ell^6.
```

The same row factors as14c are units on this open set; all faces and the
Jacobian target transport. Applied to (6), these quantities are exactly the
original a_ij,b_ij,k: the punctured arc becomes CONSTANT. At r=0 this chart
map has denominators. The forced center lies on ell=0 in a DIFFERENT family,
not at k=0 inside the fixed ell=1 saturated source. Accepted15g is not redone
or weakened, and its arc exclusions are not transported across this map.

The whole named symmetry report already contains the multiplicative scaling
with parameter tau=s^-1, its row characters and physical action. The whole
grading note restores ell in ONE row and explicitly does not claim a full
source extension. The whole14c report gives unit normalization; the whole
torsor note identifies p+g as the alternate chart coordinate. Therefore the
punctured action is KNOWN. This note's precise additional interface is the
corrected, complete ordinary-coefficient extension over r=0 and the saturated
moving-family center it forces. No novelty beyond these named histories is
claimed. The first missing arrow toward exclusion is a theorem obstructing
this moving-family ell=0 degeneration, or a valid return to the fixed source
at the center; neither is supplied here.

## 6. Tiny controls, pins and terminal scope

All four whole source/history reports are copied and pinned in the owned box,
with original paths in input-pins.json. Source14c SHA256 is
19f0394c2ec97797d325afa234d57c598a94bd2d83cbfe1dd24bda52db0f45cc.
Checker SHA256 is
7add6d80cca85f15015bed028b92dcaafe3fc74e83be6126e3e55c7c6c86aa06.
It checks seven monomial substitutions of receiver degree<=5, row exponents,
fixed-face scalar weights, a degree3/1 bracket with the exact sign, the
punctured normalized k, and the quintic (7), NEVER H³,H⁵ or full A/B.
Normal/-O positives pass; deleting -v^-1, changing ell=s² to s, or changing
kappa's exponent12 to10 each rejects the changed actual object in both modes.
Eight declared modes completed in2.006s, individually bounded by30wall/
25CPU/512MiB with -I -B and no Assert gate. Universal claims are proved above,
not inferred from those finite fixtures. Exact commands/outputs/rc are retained.

No source expansion, CAS, AWS/SSH, solver, new agent/review launch, protected
or live-peer read, canonical edit, source/gauge change or compute authority
occurred. Old files are unchanged. New report publication is transactional;
custody pins all outputs and the report/transaction. All writers/children
terminal at handoff. STOP/IDLE.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9525`.
- Body SHA-256:
  `aa9953a09d199a36621228bba8528b63b0ee6dc48ebbb41ae18a494ad5c1feeb`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
