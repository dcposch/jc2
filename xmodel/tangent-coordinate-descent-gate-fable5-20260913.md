# FIRST review of the tangent coordinate-descent obstruction (Fable 5.1)

Fable 5.1, September 13 2026, different-model FIRST. Inputs read only from
the lane inputs directory; all four SHA-256 pins matched before whole
reading (custody section). Manual reasoning only: no code, CAS, network,
agents, or shared files. ROOT collector. No successor is authorized here.

## Verdict

Main theorem (clean stratum (S): deg p>=5, p'(0)!=0, gcd(A,B)=1, no
polynomial target coordinate h has a source-coordinate pullback):
**CONFIRMED**, conditional only on the named classical imports
(Jelonek nonproperness uniruledness, Abhyankar-Moh-Suzuki, Bertini-Sard,
Zariski's Main Theorem, constructible Euler pushforward). No bridge is
REFUTED. No bridge is a GAP. Four wording imprecisions are recorded below;
neither changes a step. The p'(0)=0 and gcd(A,B)!=1 strata stay open, as
Input1 states.

## Bridge table

| # | Bridge | Verdict |
|---|--------|---------|
| 1 | nu(C,v)=(C,vA(Cv),v^2B(Cv)) finite, birational, image Sigma | CONFIRMED |
| 2 | Sigma non-normal; Sigma∩{C=0} is the parabola Psi=D^2-4p1E | CONFIRMED |
| 3 | f=h∘nu nonconstant | CONFIRMED |
| 4 | deg F_c = N = d+1 for generic c; F_c Keller | CONFIRMED |
| 5 | Boundary attachment: deleted incidence is actual nonproperness of F_c | CONFIRMED |
| 6 | Generic f=c smooth, componentwise birational onto nonproperness components; Jelonek gives A1 | CONFIRMED |
| 7 | Disconnected-A1 lemma f=P(s); hyperbola lemma; f=P0(C), k>=1 | CONFIRMED |
| 8 | Full C=0 source: x=0 triangular iso plus 2-sheeted gamma=0 cover of Psi!=0 | CONFIRMED |
| 9 | Z avoids Psi=0; Z in nonproperness set; l=chi_c(Z)>=0 | CONFIRMED |
| 10 | W'=gamma, m(w0)=2+ord p', per-line integral N, identity (10) | CONFIRMED |
| 11 | m>=5 family satisfies (S), q'=wp'/2, full divisibilities, J=-2 | CONFIRMED |

## Reconstruction and attack notes

**1. Normalization.** With w=Cv, D=vA(Cv)=p(w)/C and E=v^2B(Cv)=q(w)/C^2,
so nu parametrizes the sweep. From q'=wp'/2 one gets 4B+2wB'=A+wA'; the
leading coefficients give (2d+2)b_lead=d a_lead, so deg B=deg A=d-1,
deg q=d+1, and B(0)=p1/4. Integrality: p(w)-CD=0 is monic up to a
nonzero constant, so w is integral; with aA+bB=1, v^2=a(w)vD+b(w)E
(multiply v^2(aA+bB)=v^2), monic in v. C[C,v]=C[C,D,E][v] is finite.
Birationality: [C(C,w):C(C,p,q)] divides both d and d+1. Finite
birational onto a hypersurface from the normal A2: nu is the
normalization. Attack tried: could the extension degree argument fail
because C is adjoined? No; p and q have constant coefficients, so the
degrees over C(C) are exactly d and d+1.

**2. Non-normality.** partial_v nu=(0,p'(w),v(2B+wB'))=(0,p',(v/2)p')
by the same identity. It vanishes on Cv=alpha for every root alpha of
p'; deg p'=d-1>=4 gives at least one, and p1!=0 makes alpha!=0. A finite
birational map onto a normal variety is an isomorphism (ZMT), which would
force an injective differential. So Sigma is not normal, hence not A2.
nu is finite, so surjective onto Sigma; nu(0,v)=(0,p1 v,p1 v^2/4) is the
whole reduced Sigma∩{C=0}, isomorphic to the parabola since p1!=0.

**3. f nonconstant.** If h∘nu=b then Sigma⊂{h=b}, both irreducible of
dimension 2, so Sigma={h=b}≅A2, normal. Contradiction with 2.

**4. Degree.** In source coordinates (H,y',z') and target coordinates
(h,h2,h3), F=(H,G2,G3) and the Jacobian is ∂(G2,G3)/∂(y',z'), a nonzero
constant; every F_c is Keller, hence étale and quasi-finite. Over a dense
target open U where F is finite étale of degree N, F^{-1}(t)⊂S_c for
t∈T_c∩U, and S_c∩F^{-1}(U) is a nonempty open of the irreducible S_c for
generic c. I recomputed N: over C!=0, gamma=(CD-p(w))/2 and the residual
equation W(w)=q+(w/2)(CD-p)-C^2E has leading coefficient
-a_lead/(2d+2)!=0 in degree d+1, then x=C/gamma, y, z are determined.
So N=d+1>=6.

**5. Boundary attachment (the load-bearing arrow).** I reconstructed it
without any base-change rule. Let V={x!=0,gamma!=0}=F^{-1}{C!=0}. The
map V→Y={(t,w):C(t)!=0,W(w;t)=0}, (x,y,z)↦(F(x,y,z),w) is an isomorphism
onto Y minus Gamma={gamma=0}, with inverse gamma=(CD-p(w))/2, x=C/gamma,
u=w/gamma, y=(u-1)/x, z=(gamma-gamma0-a(u-1))/(bx^2). Gamma≅C*×A1_w via
t=(C,p(w)/C,q(w)/C^2). Cutting by h=c: S_c∩V≅Y_c minus Gamma_c, where
Y_c={W=0} inside the smooth threefold (T_c∩{C!=0})×A1_w is of pure
dimension 2, while Gamma_c={f(C,w/C)=c} is pure dimension 1 because f is
nonconstant (bridge 3). Hence Gamma_c lies in the closure of S_c∩V inside
Y_c. A sequence of S_c∩V converging in Y_c to a point of Gamma_c has
images converging to pi(Gamma_c) while x=C/gamma→∞. So pi(Gamma_c) is in
the nonproperness set of F_c, and its closure too (Jelonek's set is
closed). Attack tried: could S_c have another source piece over C!=0?
No; F^{-1}{C!=0} is exactly V.

**6. Curve normalizations.** f=c is smooth for generic c (Sard). nu is an
isomorphism off Z=nu^{-1}(non-normal locus), a curve; generic f=c meets
Z finitely and has no component in C=0. Each component Gamma' maps
finitely and generically injectively, hence birationally, onto a closed
irreducible curve inside the nonproperness set, i.e. onto a component of
it. Jelonek-Lason Thm 3.2 covers that set by nonconstant polynomial A1
images; a component, being an irreducible closed curve, equals one image.
Input3's lift-to-normalization argument is correct: A1→K is finite
surjective, the completion P1→K̄~ sends only ∞ to the omitted points, so
exactly one point is omitted and K~=A1. Gamma' smooth and birational
finite onto K is that normalization, so Gamma'≅A1. Punctured rational
curves are excluded, as Input1 says.

**7. Lemmas.** Disconnected version: straighten one generic component to
s=0 (AMS, Palka Thm B). Every component of every other generic fibre
avoids that axis, so s is a nonzero constant on it and, being a closed
irreducible curve inside a line s=const≅A1, equals the line. Infinitely
many such lines kill every t-dependence, so f=P(s). Then
f_v=p'(Cv)(h_D+(v/2)h_E)=P'(s)s_v vanishes on Cv=alpha; P'(s)≡0 there
would make s constant on the hyperbola and put a C* inside an A1 fibre;
so s_v≡0 there. Hyperbola lemma: g(C)=s(C,alpha/C) has g'=s_C, nowhere
zero on C*, so g'=cC^n, n!=-1 (log obstruction), g=aC^m+b with a!=0,
m!=0. The A1 fibre s=b misses the hyperbola, so Cv-alpha is a unit on it,
Cv=beta constant; beta!=0 would make C and v units, hence constants, on
a curve. So beta=0 and s=b is an axis; s-b is prime, so s-b=λC or λv;
s_v=0 selects C. Checked: every step uses that s is a coordinate (reduced
irreducible A1 fibres), not only a submersion. f=P0(C), k=deg P0>=1.

**8. C=0 sheets.** {xγ=0}={x=0}⊔{γ=0}, disjoint since γ|_{x=0}=γ0!=0
(Input2: dF1 would vanish otherwise). Input2's identities xF2=uA(γu)+2
and x^2F3=u(uB(γu)+1) are correct (γ-divisibility is built into p=wA,
q=w^2B). On x=0: D=ky with k=A(γ0)+(γ0+a)A'(γ0), E=bB'(γ0)z+m0y^2, and
J(F)=γ0·k·bB'(γ0)=-2b forces k,l0!=0: a triangular automorphism. On
γ=0 (x!=0 forced), coordinates (x,u)∈C*×A1: D=(p1u+2)/x,
E=(p1u^2/4+u)/x^2, and I recomputed Psi=[(p1u+2)^2-p1^2u^2-4p1u]/x^2
=4/x^2; the inverse x^2=4/Psi, u=(Dx-2)/p1 satisfies the E equation
identically. So exactly three preimages over every point of {C=0,Psi!=0}
and one over Psi=0. Input2's Jacobian chain (bx^3)(-γ)(2γ^2)C^-3=-2b
checked.

**9. Z and l.** By (5), h=P0(0) on the parabola, so for c!=P0(0) the
curve Z=T_c∩{C=0}={h0=c} misses Psi=0 and every point of Z has exactly
three F_c-preimages. Properness near such a point would give a finite
étale degree-N cover with N>=6>3. So Z lies in the nonproperness set;
if h0 is nonconstant, generic Z is smooth and each component is a
component of that set, hence A1 by bridge 6, and l=chi_c(Z)=#components
>=1; if h0 is constant, Z=∅ and l=0. chi_c(S_c∩{C=0})=l+2l=3l, the
second term because γ=0 restricts to a 2-sheeted finite étale cover of
Z⊂{Psi!=0}.

**10. Euler identity.** W'(w)=q'-wp'/2+(CD-p)/2=γ(w;t) exactly. Hence
roots of W with γ!=0 are simple and every root with γ=0 has
m=1+ord(γ)=2+ord(p') since γ'=-p'/2. Multiple roots occur only on Gamma,
consistent with the fibre count N off pi(Gamma). Pushforward of the
constructible function "number of distinct roots" along the finite map
Y_c→T_c∩{C!=0} gives chi_c(Y_c)=N(1-l)-∫_{Gamma_c}(m-1)dχ, and removing
Gamma_c gives chi_c(S_c∩{C!=0})=N(1-l)-∫_{Gamma_c} m dχ. Gamma_c is the
k disjoint lines C=C_i (distinct nonzero roots of P0=c), and on each
∫(2+ord p')dχ=2+deg p'=N. Nodes of the image curve are irrelevant: the
integral is taken on Gamma_c, where distinct tangency parameters are
distinct points. Total chi_c(S_c)=N(1-l-k)+3l=N-Nk-(N-3)l<=0 for k>=1,
l>=0, N>=6, against chi_c(A2)=1. Constants: c generic avoids P0(0), the
finitely many critical values of f and h0, non-reduced cuts of P0, and
the complement of the rank-N open; empty h0-cuts are the l=0 case. The
h=C sign check (k=1, l=0, chi=0 for C*×A1) reproduces.

## Explicit family check

For m>=5, gamma0=1, a=-(m+1)/m, b=1, A=(4-2(m+1)w^(m-1))/(m-1),
B=(1-mw^(m-1))/(m-1), p=wA, q=w^2B. Hand check of 4B+2wB'=A+wA': the
left side is [4-(2m^2+2m)w^(m-1)]/(m-1) and the right side is
[4-2(m+1)(1+(m-1))w^(m-1)]/(m-1); equal, so q'=wp'/2. At w=1: A=-2,
B=-1, B'=-m, (1+a)B'=1. Expansion in x with u=1+xy, γu=1+(a+1)xy+O(x^2):
uA(γu)+2 vanishes at x=0 (x-divisibility); u^2B(γu)+u
=(1+2xy)(-1+xy)+1+xy+O(x^2)=O(x^2) (x^2-divisibility). p'(0)=4/(m-1)!=0;
A=0 needs w^(m-1)=2/(m+1), B=0 needs w^(m-1)=1/m, incompatible for m>=2,
so gcd(A,B)=1. deg p=m>=5, N=m+1 unbounded, J(F)=-2. The stratum (S) is
nonempty in every degree >=5. CONFIRMED; no new family is proposed.

## Wording imprecisions (not gaps)

- Input1 §3 says "In its finite normalization they remain boundary points
  too". The proof does not need any normalization of Y_c; the escape
  x=C/gamma→∞ along Y_c itself suffices. Harmless.
- Input1 §1 says the parabola statement uses "finiteness"; more precisely
  it uses surjectivity of the finite nu onto the closed Sigma. Harmless.
- Input1 §2 writes the hyperbola conclusion as "s affine in C"; the
  proof gives s=λC+μ with λ!=0, which is what §2 then uses. Harmless.
- Input3's item 1 cites Jelonek-Lason Thm 3.2 for coverage by polynomial
  A1 images; the argument also needs S_F closed, which is part of the
  definition/theorem there (S_F is closed by Definition 2.1). Harmless.

## Scope and custody

Closed here: only the clean stratum (S) of the literal whole polynomial
tangent-sweep triple. Not closed: p'(0)=0 (the critical hyperbola through
C=0 and identity (6) both fail), gcd(A,B)!=1 (integrality of v and the
normalization identification fail), any other ambient construction, and
JC2 itself. The accepted mapping-degree<=5 plane closure is not used.
Imports were audited for applicability only: Jelonek needs a generically
finite polynomial A2→A2 map (supplied by Keller F_c after the two
coordinate changes); AMS needs a closed A1 in A2 (supplied by smooth
fibre components and by smooth generic Z). Neither import was re-proved.

Input pins matched before whole reading, all four:
3219ee5472f0f9d7467c9ab7cf129db36c65881624760f038b6e6f3723b49a9c
tangent-coordinate-descent-astra-20260913.md (Input1);
c5524dd9e10e61ea0f12e3f76ef18ef0782aa52c18845c035ae8013e12c61fd6
tangent-component-fibres-root-20260913.md (Input2);
47fe56279edd700499d5f43f8beab0bbd0aa75be01350544a8257a673e2339c2
CLASSICAL-INPUTS.md (Input3);
77ec0b282f4813ee9a2b71ebced492cc6f0b9262acf90a28f444ed9a507190bd
COORDINATION.md (Input4, skimmed for the skeleton/append/marker
contract only). Postpins were re-hashed after whole own readback and
were unchanged. No charge_basis line: no exit price is asserted.
External ops/lane.sh owns custody; no local finalizer was run.

<!-- BODY-END -->
