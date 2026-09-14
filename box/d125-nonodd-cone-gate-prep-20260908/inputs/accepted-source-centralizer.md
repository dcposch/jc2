# D125 cone first contact from the polynomial source alone

2026-09-08. **UNREVIEWED SOURCE-INTERFACE THEOREM, producer checked.**
The proposed first-contact bridge holds under the literal polynomial
hypotheses below. No moving-lift result, ordinary-lift equation, degeneration
existence, elliptic-center theorem or later componentwise exclusion is used.
This is a necessary condition, not an exclusion or JC2 conclusion.

## 1. Exact statement and notation

Let K be a characteristic-zero field. Assume A,B in K[g,p] are odd under
(g,p)->(-g,-p), with total degrees15,25 and tops H³,H⁵, where

```text
H=p² V0, V0=g³+p³, w(g)=5, w(p)=-7,
w(A)<=3, w(B)<=5, [A,B]_(g,p)=c*g², c in K*.
```

These are accepted14c necessary conditions. We do NOT impose or use its
remaining faces or polynomiality equations. Write A_d,B_d for homogeneous
total-degree components and define the purely formal dilation

```text
A_s=sum_d s^(15-d) A_d, B_s=sum_d s^(25-d) B_d.
[A_s,B_s]=c*s^36*g².                              (1)
```

There exist homogeneous R3,R1 of degrees3,1 (zero allowed), scalars
alpha,beta,gamma in K, and

```text
R_s=H+s²R3+s⁴R1,             w(R_s)<=1,
alpha_s=alpha*s^10, beta_s=beta*s^10, gamma_s=gamma*s^20,
F=A_s-R_s³-alpha_s R_s,
q_s=5R_s²/3+beta_s-5alpha_s/9,
delta_s=gamma_s-beta_s alpha_s+5alpha_s²/9,
G=B_s-R_s⁵-beta_s R_s³-gamma_s R_s-q_s F
```

such that F is nonzero and

```text
j=ord_s F in {2,4,6,8},       ord_s G>=2j,
F_j=H C,
C!=0 homogeneous of degree10-j, even, w(C)<=2,
deg_g C<=2,                  V0 does not divide C.          (2)
```

In particular C has positive degree and vanishes at the origin.
This does NOT say C is nonzero on every component of V0=0.
The exact full shear is

```text
B_s-beta_s A_s
 =R_s⁵+(delta_s-5alpha_s²/9)R_s
       +(5R_s²/3-5alpha_s/9)F+G.                (3)
```

Scalar references may vanish. In proving (2), tentative j=12/14 is handled
with alpha_s of order10: no assumption ord(alpha_s)>=j is made.

## 2. Centralizer of H, proved here over K

The rational Hamiltonian centralizer is K(H); its polynomial part is K[H].
Here is an elementary proof, so no new external theorem is imported.

Put h=H and F0=K(h). The generic fiber, after algebraic closure of F0, has
equation g³=(h-p⁵)/p². Its right side has p-adic valuation-2. A rational root
would have valuation-2/3, impossible in the rational function field in p.
A cubic with no root is irreducible. The original polynomial
p²g³+p⁵-h is primitive over the p-polynomial ring (h is a nonzero constant),
so this generic fiber is geometrically integral. Consequently F0 is
algebraically closed in L=K(g,p): a nontrivial finite separable subextension
would split into a product after base change to an algebraic closure of F0,
contradicting that L tensor that closure is a domain.

For completeness, a Hamiltonian constant z in L is algebraic over F0.
Normalize the derivation to D=[H,-]/(3g²p²), so Dp=1 and D fixes F0.
L is finite algebraic over F0(p). Differentiating the monic minimal
polynomial of z over F0(p), when Dz=0, gives a polynomial of smaller degree
in z. Every differentiated coefficient is therefore zero. The constants
of d/dp in F0(p) are F0 in characteristic zero, so z is algebraic over F0.
The preceding paragraph gives z in F0.

Finally, if a(H)/b(H) is polynomial with coprime a,b in K[T], their Bezout
identity shows b(H) is a polynomial unit, hence b is constant. This proves
the polynomial assertion. A homogeneous polynomial centralizer of degree e
is consequently a scalar H^(e/5) if e is a nonnegative multiple of5,
and zero otherwise. No irreducibility of V0=0 is asserted or needed:
that SPECIAL fiber is reducible.

## 3. A-only references by finite polynomial normal forms

Use ordinary monomial division by H², with lexicographic g>p and leading
monomial g⁶p⁴. Replacing it using the other terms of H² strictly lowers
g-degree, preserves total degree and never increases w. Indeed H² has
weight2 at g⁶p⁴ and lower weights at its other monomials. The quotient
of a weight<=3 input has weight<=1.

Choose R3 and R1 by the exact divisions

```text
A_13 = 3H² R3 + N_13,
A_11 - 3H R3² = 3H² R1 + N_11,                  (4)
```

where both remainders are normal for g⁶p⁴. The quotient degrees and
weights give R3 in span_K{gp²,p³} and R1 in span_K{p}.
These formulas are factored identities, not expanded degree15 polynomials.

The order10 coefficient of R_s³ is 3R3 R1². Choose alpha so that

```text
A_5-3R3 R1²-alpha H
```

is normal for g³p², equivalently take its g³p² coefficient for alpha.
A homogeneous degree5 input permits just this scalar quotient.
Thus F_2=N_13, F_4=N_11, and F_10 is H-leading-monomial normal.
Every F_l is homogeneous of degree15-l and weight<=3; only even l occur.
F has no constant s coefficient and no s powers above14.

F cannot be identically zero. Otherwise, over K((s))[g,p],

```text
c*s^36*g²=[A_s,B_s]=(3R_s²+alpha_s)[R_s,B_s].
```

The first factor has total degree10, with top3H², whereas the nonzero
left side has degree2. Total degrees of nonzero polynomial products add.
This is impossible. Hence initially j is some even integer2<=j<=14.

## 4. Exact moving identity and normalization of every lower G kernel

Direct differentiation, with s and all scalar references held constant,
gives

```text
[A_s,B_s]
 =[R_s,(3R_s²+alpha_s)G-delta_s F-(5/3)R_s F²]+[F,G].       (5)
```

One can check it before any substitution by treating R,F,G as independent
variables: the three coefficients of dR wedge dF, dR wedge dG,
dF wedge dG are respectively
-delta-(10/3)R F, 3R²+alpha, 1 on BOTH sides.
This retains all alpha/beta/gamma cross terms.

All quantities have the combined grading deg(s)=deg(g)=deg(p)=1:
R_s has degree5, F degree15, G degree25. Moreover G is odd and w(G)<=5.
Always delta_s=(gamma-beta alpha+5alpha²/9)s^20, so
ord(delta_s F)>=20+j>2j, including tentative j=12/14.

Initially set beta=gamma=0. If earlier G coefficients vanish and a first
nonzero G_l occurs below2j, the order-l part of (5), using (1), is

```text
[H,3H²G_l]=0, hence [H,G_l]=0.                  (6)
```

Indeed RF² starts at2j, delta F strictly later, [F,G] starts at j+l>l,
and every correction in R_s or 3R_s²+alpha_s is at positive s-order.
Thus the polynomial centralizer applies. G_l is homogeneous of degree25-l.
For positive even l<2j<=28, the ONLY possible nonzero kernels are

```text
l=10: eta H³,                l=20: theta H.      (7)
```

Negative H powers are not polynomial coefficients and never enter this
argument. Remove the first by beta->beta+eta and the second by
gamma->gamma+theta. Exactly,

```text
Delta_beta G=-eta*s^10*(R_s³+F),
Delta_gamma G=-theta*s^20*R_s,
Delta delta_s=(-eta*alpha+theta)*s^20.            (8)
```

The designated leading kernel is removed and no earlier coefficient is
changed. All other terms in (8) are retained at later orders.
Proceeding in increasing l therefore produces ord G>=2j; each scalar
adjustment is used at most once. These changes do not alter A_s,B_s,F or j.
This finite induction needs only (5), not commutation of a moving generator
at every s or any rational reconstruction.

The order10 alpha terms in q_s and 3R_s²+alpha_s are included throughout.
In particular the coefficient -5alpha_s F/9 in the full-shear expression
(3) is not discarded when 10+j<2j. Formula (8) is not a partial B-kernel
shear: the unaltered A_s,B_s and the exact whole-beta-A identity (3) track
both beta and gamma.

## 5. The order2j polynomial obstruction and the four possibilities

Since2j<=28<36, taking order2j in (5) now yields

```text
[H,T]=0,    T=3H²G_(2j)-(5/3)H F_j².            (9)
```

T is polynomial and homogeneous of degree35-2j. For the possible even
j=2,4,...,14, this degree is divisible by5 only at j=10, when it is15.
Section2 therefore gives T=0 except possibly T=bH³ at j=10.
In every case T is divisible by H². Divide one H in (9) to obtain

```text
H divides F_j².                                (10)
```

V0=g³+p³ is squarefree in characteristic zero. Thus V0 divides F_j.
Write F_j=V0 Q. Since w(V0)=15 and w(F_j)<=3, w(Q)<=-12.
Any ordinary monomial with p-exponent0 or1 has weight at least-7.
Therefore p² divides Q and

```text
H divides F_j.                                 (11)
```

This is a filtered polynomial argument despite the repeated p² factor.
Without the weight it is false: P=gpV0 has H|P² (quotient g²V0) but H does
not divide P; w(P)=13. No high square need be expanded to check those factors.

At j=10, (11) and degree F_j=5 make F_j a scalar H, but the order10 normal
form in Section3 forbids that unless it is zero. At j=12/14 its degree is
3/1, so (11) again forces zero. These contradict the definition of j.
Only j=2,4,6,8 remain.

Set C=F_j/H. It is nonzero homogeneous of positive even degree10-j,
with w(C)<=2. Its claimed normality is not an assumed compatibility of
two division algorithms. For j=2/4, F_j is normal for g⁶p⁴ and w(F_j)<=3.
A monomial with g-exponent>=6 must then have p-exponent>=4; hence normality
forces deg_g F_j<=5. For j=6/8, total degree9/7 and weight<=3 already force
deg_g F_j<=5 (at j=8 it is at most4).
Since deg_g H=3 and K[p] is a domain,
deg_g F_j=3+deg_g C. Thus deg_g C<=2, proving V0 does not divide C.

This does NOT make C a unit on the product of component fields.
For example C=p(g+p) has degree2, weight-2 and g-degree1, but vanishes on
the line g=-p. It is a genuine countercontrol to selected-component
nonvanishing, not a claimed realization by a full source pair.

## 6. Provenance, controls and exact stopping point

The whole accepted14c source was read. Whole14v and14f were read as named
history/comparison: the shape of (5) and centralizer motivation are known,
but neither the elliptic-center first-contact conclusion nor its ordinary
lift arguments are transported here. Input-pins.json records all three
original paths and unchanged snapshots. No moving-lift report, later
consumer, live peer,15g proof or external theorem is a premise.

The new content is the complete polynomial-source construction (4),
the homogeneous scalar-kernel normalization with all alpha terms, and
the uniform j bound (2). The subsequent product-ring initial argument,
any exclusion on the reducible cubic, and source nonexistence remain
outside this theorem. No final exclusion is asserted.

Owned stdlib check.py SHA256
5fcaa71d6fa2f096e74ba8388b806cfc0e6899df885fe19b6bb837c7253665ab
checks the free-symbol differential identity (degree<=5 symbols, not
actual H powers), the exact whole beta shear, scalar order/kernel tables,
and tiny omitted-weight/selected-component controls.
The three mutations omit the alpha cross term, omit gamma, or perform
only a partial shear; each rejects normally and with -O.
Eight final declared modes completed correctly in2.002s, each
30wall/25CPU/512MiB, -I -B, no Assert gate.
The first toy checker accidentally subtracted beta² A in its positive
branch; its rejected bytes and failure record are preserved separately.
The one-line correction gives the exact displayed beta A identity.
No failed prototype supports the theorem.

No full A15/B25 or high actual R powers were expanded. No CAS, AWS/SSH,
solver, source enumeration, new lane, canonical/protected edit, or live
peer read occurred. Proof is universal prose; tiny tests are controls,
not a substitute. New files are confined to the owned box and this
transactional report. All children and writers terminal at handoff.
STOP/IDLE.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11539`.
- Body SHA-256:
  `3227bb8c6c4048ee8f0330d545c1accab28c6a3a9fdb222b69605458e7758226`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
