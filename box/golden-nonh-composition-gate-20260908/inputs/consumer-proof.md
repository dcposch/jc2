# Golden resonance: an independent conditional source consumer

Coordinator /root (Astra), September8 2026. PRODUCER-CHECKED only after the
declared scalar controls finish. This report is not a promotion. Its
conditional theorem is independent of the unreviewed two-regime conclusion;
the proposed composition with that conclusion needs ONE hostile Fable gate
covering both arrows. No oddness, full-golden or JC2 conclusion is assumed.

## 1. Literal conditional theorem

Let K have characteristic zero and contain either root rho of rho²-3rho+1.
Set t=1-rho, L=p+g, M=p+t*g, H=p²LM², D=pLM. Suppose A,B in K[g,p] have
total degrees15,25, tops H³,H⁵, weights<=3,5 for w(g)=5,w(p)=-7, and
[A,B]=c*g² with c!=0. Use combined degree1 for s,g,p and form A_s,B_s by
homogeneous dilation. Thus [A_s,B_s]=c*s36*g².

Assume there are the following polynomial reference data, with precisely
the indicated combined homogeneity, not arbitrary formal coefficients:

    R_s=H+sum_{r=1}^5 s^r R_{5-r}, w(R_s)<=1;
    alpha_s=alpha*s10, a0_s=a0*s15;
    F=A_s-R_s³-alpha_s R_s-a0_s, ord_s F=12,
    F12=lambda*D, lambda in K*;
    b_i,s=b_i*s^(25-5i) for i=0,...,4;
    q_s=5R_s²/3+(4/3)b4,s R_s+b3,s-5alpha_s/9;
    B_s=R_s⁵+sum_{i=0}^4 b_i,s R_s^i+q_s F+G,
    ord_s G>=24, deg_combined G=25.

R_s has g-leading term rho*g³p², since its lower components have
g-degree<=2 by degree and weight. Its moving critical point g_c(s,p),
with constant term g0=-p/t, is defined by R_{s,g}(g_c,p)=0. Require

    ord_s xi_s>=5, xi_s=R_s(g_c,p),
    ord_s theta_s>=15, theta_s=F(g_c,p).                 (R)

Zero series have infinite order. The theorem is: these hypotheses are
inconsistent. All alpha, a0 and b_i may vanish; no division by them or by
c is used. Lambda is nonzero over a FIELD. This is not a nilpotent-base
source classification, and no inverse-lift or actual Keller pair is needed.

## 2. The exact resonant initial is source-forced under (R)

Choose a square root a of t(t-1) over an algebraic closure of K, and work
in E=Kbar(p^(1/2)), with its uniquely extended p-derivation. Both a choices
are allowed; a!=0. At the fixed critical point,

    H(g0+w,p)=t(t-1)p³w²+t²p²w³,
    D(g0+w,p)=(t-1)p²w+t*p*w².

The formal implicit function theorem gives g_c in K(p)[[s]]. Since R_s
is cubic in g, the formal Morse coordinate zeta can be chosen with

    R_s=xi_s+zeta²,
    g=g_c+w_s(zeta),
    (partial g/partial zeta)_{s=0,zeta=0}=1/(a*p^(3/2)).  (1)

Explicitly zeta=w*sqrt((1/2)R_{s,gg}(g_c,p)+rho*p²w).
All inverse coefficients have nonnegative s-order; poles in p are harmless
in E. No quotient by the nonreduced divisor M² is being used.

F has combined degree15 and starts at12. Its degree3 first coefficient
lambda*D gives the transverse term

    F(g_c+w_s(zeta),p)=theta_s+ell_s*zeta+O(zeta²),
    ord_s ell_s=12,
    ell_12=lambda*(t-1)*p^(1/2)/a=k*p^(1/2),
    k=lambda*(t-1)/a !=0.                              (2)

All coefficients of zeta^n, n>=2, have s-order>=12. Set
zeta=s^(12/5)Y in a finite Puiseux extension. By (R), xi_s has order>=5,
strictly above24/5, so R_s has initial Y² at order24/5. Theta has
order>=15>72/5. Therefore F has initial k*p^(1/2)Y at order72/5.
The alpha_s R_s term is at least74/5 and a0_s at least15. The A initial is

    P=Y^6+k*p^(1/2)Y, order72/5.                       (3)

This conclusion retains every later coefficient of F, not just F12:
moving-center constants are precisely controlled by theta, and all
positive-zeta corrections beyond (2) are later in the joint order.

Each lower scalar B kernel has order at least
25-5i+(24/5)i=24+(5-i)/5>24. Only (5/3)R_s²F of q_s F can enter24;
the b4 R_s F term has order>=121/5, and the b3/alpha parts are later.
G starts at24 and its coefficient G24 has ordinary degree1. At (s,zeta)=0
it restricts to e*p for some e in K; corrections carry positive s-order.
Hence B has the monic initial

    Q=Y^10+(5/3)k*p^(1/2)Y^5+e*p, order24.             (4)

There are no omitted lower B terms. No assumption on G25 is required.
Equations (3),(4) are mathematical polynomials in E[Y]; the tiny checker
uses scalar coefficient projections only, not degree6/10 expansions.

## 3. Match the NONZERO initial Jacobian

The coordinate transformation gives EXACTLY

    [A_s,B_s]_(zeta,p)=c*s36*g(s,zeta,p)²*g_zeta.

Its leading coefficient at36 is c*p^(1/2)/(t²*a), nonzero, using (1).
The initial bracket order is72/5+24-12/5=36. It is therefore incorrect
to set [P,Q] to zero: the equality case is essential. Direct coefficient
differentiation, with all derivatives taken at fixed Y, gives

    [P,Q]_(Y,p)=(6e-(10/3)k²)Y^5+e*k*p^(1/2).

The Y10 coefficients cancel:6*(5/6)k-5k=0. No other coefficients occur.
The target has no Y5 term, so e=5k²/9. Matching the constant then gives

    c=(5/9)k³*t²*a=(5/9)lambda³*t*(t-1)².              (5)

Changing a to -a changes k and the target reciprocal by the same sign,
so (5) is independent of the Morse square-root choice.

## 4. Independently derive the incompatible weighted-face coefficient

The source's top weighted faces are determined by the TOTAL degree caps:

    in_w A=a_f*g²p+rho³*g9p6,
    in_w B=d_f*g+e_f*g8p5+rho⁵*g15p10.

Indeed 5i-7j=3 within total degree15 has only (2,1),(9,6), and
5i-7j=5 within degree25 has only (1,0),(8,5),(15,10). Their weights are
actually attained by the fixed tops. The weight10 part of [A,B]=c*g²
is the bracket of these faces, with determinant coefficients

    [g16p10]: 5a_f*rho⁵-3rho³*e_f=0,
    [g9p5]:   2a_f*e_f-6rho³*d_f=0,
    [g²]:     c=-a_f*d_f.

Thus e_f=5a_f*rho²/3, d_f=5a_f²/(9rho), and
c=-5a_f³/(9rho). This is a source consequence, not a further premise
imported from a face table. No actual high faces are expanded by the code.

Only the top monomial rho*g³p² of R_s has weight1: solving
5i-7j=1 within total degree<=5 gives exactly (3,2). Therefore R_s³
has no g²p coefficient, nor does alpha_s R_s. Since F12=lambda*D,
the g²p coefficient of A is a_f=lambda*t; later F coefficients have
ordinary degree<3. Using t²=rho, the forced face value is

    c=-(5/9)lambda³*t.                                (6)

Equations (5),(6) imply (t-1)²+1=0. But
(t-1)²+1=3rho, a unit in K. Since lambda,t are nonzero, this is a
contradiction. Both rho embeddings obey the same exact identity.

## 5. Composition interface, independent scope and stop

The root-checked but UNREVIEWED source report
golden-two-regime-initial-discriminator-astra-20260908.md,
SHA14c4cdeddf9b1166046759022378775fc7ebc147c7d939579cf93f6b78aa51c6,
derives the canonical references, ord G>=2j, H|F_j² and the non-H-divisible
alternative. For that alternative its two-regime argument yields j12 and
(R), with theta defined there as P0(g_c,p). At j12 these definitions agree:
finite normal blocks F=P0+R_s P1+R_s²P2 have ord Pi>=12 and combined
degrees15,10,5. Thus P1=P2=0, P0=F. Alternatively F has ordinary degree<=3
and is already normal. Also D|F12 and degree3 force F12=lambda*D, lambda!=0.
Its b_i, alpha, a0 and G data match Section1 exactly, without parity.

Consequently, IF both reports pass independent review, their composition
excludes the entire non-H-divisible first-correction branch of the unequal
golden receiver, even for NONODD A,B. This conditional composition is new;
it does not use the accepted odd-j12 theorem15l or the ansatz theorem15k,
and it does not classify the H-divisible branch. No source-to-six-case or
all-degree coverage claim is made. The complete JC2 goal remains open.

Root read the source proof whole and reproduced all ten source checker
outcomes22:16:05, normal/-O, matching rc/stdout/stderr and eight unchanged
pins in2.752seconds. The common-quadratic scalar sample is not proof;
the universal UFD/Euler argument in its text supplies that step. A single
Fable gate must examine the whole source argument, this initial derivation
and the face comparison, rather than reviewing only the easy last equation.

No additional source descendant, AWS run, CAS, full expansion, solver,
publication, protected-project action or external mathematical premise.
All objects in the owned checker are exact scalar/free-symbol coefficient
calculations. The symbolic lambda³ factor is justified by the displayed
homogeneity, not by specialization alone. Both conjugates are checked,
as are actual quintic-factor, face-sign and target-factor mutations. The
fourth negative control is a false resonance-order inference, not a changed
polynomial source. Replay results and source pins accompany this report.

## 6. Completed producer controls

All ten normal/-O outcomes completed successfully in2.611470seconds,
with eleven source/code pins unchanged. Each child used direct prlimit,
25CPU seconds/512MiB address space, Python -I -B and an outer30-second
subprocess timeout; no inner process-group wrapper. Positive results agree
and every declared negative mode rejects at its intended check. No Assert
node gates the checker. The universal proof is Sections2–4, not these
scalar tests.

- Owned checker box/golden-resonant-source-consumer-20260908/check.py:
  b47cffd1436080d8f32e925b94160361d6a781047d755b6ad2c387c47717a47b.
- Replay in that directory, replay.json:
  afda7aeeb7ddecddbe528693d475b020f71b23e7c2f42ff07df2731be19e716b.

No new OPEN identifier is raised: this is a proposed resolution of the
already named non-H-divisible resonant branch. H-divisible remains outside.

## COLLISIONS

- NONE: the existing open_collision extractor finds no explicitly raised
  OPEN entries. Root called its extractor/renderer directly; with no query,
  the CLI's unconditional broad corpus scan is unnecessary and could read
  unreleased local reports. No instrument was modified or collision closure
  inferred. Manual history comparison is the exact source/15k/15l distinction
  in Section5, not a new all-campaign scan.

All children are terminal; the report and controls are complete. Stop/idle
for this artifact after finalization; independent review remains mandatory.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10031`.
- Body SHA-256:
  `c2bc73bf65dd95d51c9eb27dc0be45f86cb3a8967d6b0481d4ac67a2078d4a7e`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
