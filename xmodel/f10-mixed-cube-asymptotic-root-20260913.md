# Mixed scalar: nonzero leading term on all seven cube branches

ROOT, September13,2026. MANUAL / PRODUCER-CHECKED / UNPROMOTED.
This proves generic and sufficiently-large-r scalar unitness if the manual
argument survives independent review. It gives NO effective integer cutoff,
NO all-r certificate, NO complete-source comparison/REG or source exclusion,
and does not resolve JC2. No scientific interpreter or CAS was executed.

## Inputs and exact claim

The same scalar and whole-leading interface are those of
xmodel/f10-mixed-univariate-reduction-root-20260912.md,
SHA7b8545a623a771ebd423b441c4c1567389d0ca837d4e5b80c8990bc52b1075f8.
The universal reciprocal trace is independently rederived below; its earlier
report is xmodel/f10-mixed-reciprocal-trace-root-20260912.md,
SHA6c357b0b7fee0ba049c2a35960a111b97642aa72f24f637aed4efbcaa959ba61.
Both were read WHOLE in this continuation after current pins, using separate
chunks for the reciprocal note. The corrected prior shortcut intake,
SHA47dcaf21296a91fb15300a7b4adab17dbb52d56022f147d15f20a184629babc7,
was consulted for its determinant correction and rejected universal ratio;
its first body read preceded the fresh pin and was partially output-truncated.
Neither the rejected ratio nor its incorrect determinant is a premise here.
Current COORDINATION pin33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597.

Let phi=1+u+Xu^2+Yu^3, d_k=[u^k]phi^t and

    B(t,X,Y)=[u^14](phi'/phi) T_(2t-1) T_(4-t),
    T_s=trunc_(degree<=7) phi^s.

Take the WHOLE leading algebra d6=d7=0, with its accepted guard and septic
description at actual t=(5r+2)/(3r+1), r>=2. Set delta=t-5/3. The claim is:
on every one of its seven branches at delta=0,

    B = -2 delta^2/279006525 + O(delta^(15/7)).          (1)

The meaning is convergent power series after delta=h^7, not a choice of real
roots. All seven branches have the SAME nonzero coefficient. Consequently B
is a unit for every sufficiently small nonzero complex delta, hence for all
sufficiently large integer r. The exceptional actual integers form a finite
set, but this note neither identifies that set nor proves it empty.

## 1. Adapted exact coordinates and the boundary algebra

Put a=X-1/3, c=Y-1/27-a/3, and v=u/(1+u/3). Then

    phi=(1-v/3)^(-3) C(v),    C(v)=1+a v^2+c v^3,
    d_k=[v^k](1-v/3)^(k-1-3t) C(v)^t.                 (2)

The second identity follows directly by substituting in the formal residue
phi^t du/u^(k+1); du=(1-v/3)^(-2)dv. It is a finite-coefficient identity,
not an analytic change of variables requiring a root choice.

At t=5/3, binomial(t,2)=5/9 and binomial(t,3)=-5/81. Therefore EXACTLY

    d6=-(5/81)(a^3-9c^2),
    G:=d7+d6/3=-(5/27)a^2 c.                           (3)

In particular the boundary quotient is Q[a,c]/(a^3-9c^2,a^2c).
Its length is seven: a monic Groebner presentation for lex c>a is
c^2-a^3/9, a^2c, a^5, with standard monomials
1,a,a^2,a^3,a^4,c,ac. The two possible overlaps reduce to a^5 and then0.
This quotient is also the critical algebra of a^3c-3c^3, up to nonzero
constant factors. No singularity-classification theorem is used.

The septic P from the input becomes 9a^7 at delta=0, but its U=3a^2 is
not invertible there. Thus one must NOT identify this boundary quotient with
Q[a]/(a^7) by specializing Y=V/U. We use the faithful two-equation source
to obtain the branches, and the generic septic only to count all of them.

## 2. All seven branches, with their coefficients

Give a,c,delta weights2,3,7. From (2),

    d6=-(5/81)(a^3-9c^2) + terms of weight>=7,
    G=-(5/27)a^2c + delta/5103 + terms of weight>=8.    (4)

For the constant term in the second line, at a=c=0 the delta-linear
coefficient of d6 is1/1458 and that of d7 is-1/30618. Their combination
-1/30618+1/4374 equals1/5103. All other delta-linear terms containing a
or c have greater weight; all delta^2 terms have weight>=14. At delta=0,
(3) excludes any additional lower-weight terms.

Write delta=h^7, a=h^2 A, c=h^3 C0. Dividing d6 by h^6 and G by h^7
gives two polynomial (hence analytic) equations in h,A,C0. At h=0 they are

    A^3=9 C0^2,     A^2 C0=1/945,
    A^7=1/99225.                                     (5)

There are exactly seven distinct solutions, all nonzero. The Jacobian of
the scaled pair at each is

    25 A^4/729 + 100 A C0^2/243 = 175 A^4/2187 != 0.

The analytic implicit-function theorem therefore supplies seven convergent
branches A_j(h),C_j(h). They yield distinct a_j for sufficiently small h!=0.
The accepted generic septic has degree7, so these already exhaust it; on
these branches U=3h^4 A_j(0)^2+O(h^5) is nonzero and Yd5 tends to the
nonzero cube guard. Thus no unguarded or extra field component was substituted.

## 3. Exact shifted trace and its lowest weight

For arbitrary degree<=7 T_1,T_2, set A_i(w)=w^7 T_i(1/w), and let
q0(w)=w^3+w^2+Xw+Y. Multiplication by w has
det(I-uM)=phi(u), hence phi'/phi=-sum_(k>=0)Tr(M^(k+1))u^k.
Coefficient extraction gives B=-Tr(w A_1 A_2) for the displayed powers.
This identity is polynomial and remains true in nonreduced quotients.

Shift w=z-1/3, so q0(w)=q(z):=z^3+a z+c. Define

    Q_s(v)=trunc_7[(1-v/3)^(7-3s) C(v)^s],
    A_s(z)=z^7 Q_s(1/z).

Indeed Q_s=(1-v/3)^7 T_s(v/(1-v/3)), a degree<=7 polynomial; its
truncation description follows from agreement through v^7. The exact
scalar is now

    B=-Tr_(Q[z]/q)((z-1/3) A_(2t-1) A_(4-t)).         (6)

Assign z weight1. At delta=0 both powers equal7/3. Let
A=z^7 trunc_7(C^(7/3))(1/z), homogeneous of weight7. The only further
terms of weight7 in the two A_s are their delta-linear CONSTANT terms:

    A_(2t-1)=A+2delta/5103+terms of weight>=8,
    A_(4-t)=A-delta/5103+terms of weight>=8.            (7)

To see exhaustiveness, a delta-linear term at coefficient v^k contributes
weight7+(7-k), so only k=7 has weight7. Its constants are the v^7
coefficients of -6delta log(1-v/3) and 3delta log(1-v/3), respectively.
Terms involving a,c or delta^2 have strictly greater weight.

Division by the homogeneous monic q and its trace preserve weight. The
factor -z in (6) has weight1 and contributes only weight>=15. Thus the
weight14 part is one third the trace of the product of (7).

## 4. The finite trace calculation

Using binomial(7/3,2)=14/9 and binomial(7/3,3)=14/81, direct reduction
of A modulo q gives

    A = alpha z^2 + beta z + gamma  (mod q),
    alpha=(4/9)ac,
    beta=(2/9)c^2-(4/81)a^3,
    gamma=(8/27)a^2c.

The requisite moments are Tr1=3, Trz=0, Trz^2=-2a, Trz^3=-3c and
Trz^4=2a^2, by the cubic recurrence. In particular TrA=0 identically.
On the leading relation a^3=9c^2, beta=-2a^3/81 and

    TrA^2=2a^2 alpha^2-6c alpha beta
            -2a(beta^2+2alpha gamma)+3gamma^2
          =(288+48-8-384+192)a^7/6561
          =136a^7/6561.

The cross terms with the delta constants vanish because TrA=0, whereas
Tr1=3 cancels the outer factor1/3 for their product. Equations (5)--(7)
therefore give

    B_[14] =136a^7/19683 -2delta^2/5103^2
           =-14a^7/19683
           =-2delta^2/279006525.                     (8)

Here delta^2=99225a^7 on the leading solution. All omitted terms have
weight>=15, so substitution of any of the seven convergent branches proves
(1). No pairing-nondegeneracy, real positivity or generic-point selection
was used. Symmetry in the two exponents is retained; at h=0 the expression
vanishes, in agreement with the known cube control. The nonzero coefficient
depends on keeping BOTH delta constants, including their product: dropping
them changes136 to the correct final -14 only after the missing -150 is
restored. This is a meaningful manual transcription control, not a runtime test.

## 5. Consequences, precise gap and scheduling

The seven-branch leading coefficient is nonzero, so the generic scalar
norm is nonzero. Its order at delta=0 is14 with leading coefficient
(-2/279006525)^7. Equivalently the selected univariate P,F are generically
coprime over Q(t). This is a manual nonvanishing proof, not the missing
exact Bezout DATA certificate or its checked exception list.

Continuity on the FINITE seven analytic branches gives an epsilon>0 for
which B never vanishes when0<|delta|<epsilon. Since actual
delta=1/(3(3r+1)), all sufficiently large r are covered at scalar level.
No numerical epsilon or integer R0 is supplied. A nonzero rational norm has
only finitely many rational zeros, but this does not exclude an exceptional
r>=2. No all-F10 conclusion follows even from an eventual all-r scalar proof.

This changes the mathematical discriminator from 'generic nonvanishing
unknown' to 'compute/exclude the finite actual exceptions or obtain an
effective uniform interval bound', CONDITIONAL ON independent FIRST.
It does not select a large finite-r farm, code rewrite, worker or cap rise.
The already accepted all-r producer/checker remains unchanged and unrun.

A targeted exact-constant/cube-deformation/Puiseux history search in F10
reports and canonical route/reduction/evidence records found no earlier
instance; hash substring hits were discarded. This is not a literature
novelty claim. All derivations are elementary formal coefficients, finite
trace and analytic implicit functions; no external theorem was newly imported.
ROOT sent the coordinate and trace calculations to the live Astra co-research
lane before seeing any response/body. Its eventual report is corroborative
co-research, NOT a blind different-model promotion gate.

No new canonical OPEN is raised. No source/runtime/shared foundation was
modified by this report. No protected-tree read, compute, AWS mutation,
staging, commit or external publication. Any later source/review conclusion
must retain the finite-but-unidentified exceptions and full-source gaps.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9728`.
- Body SHA-256:
  `a861c8475439da3066e41083327e81c269d18c6b84146ad9df4985dadcc38fa3`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
