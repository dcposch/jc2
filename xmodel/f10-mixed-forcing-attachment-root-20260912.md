# F10 mixed forcing: fill the missing stipulated-algebra attachment

ROOT,2026-09-12; first publication action18:44:30UTC.
MANUAL/PRODUCER-CHECKED, UNPROMOTED; a focused proposed closure of the
previous review's missing-input gap, not a unit proof or source exclusion.

## Exact scope and inputs

The September11 FIRST aa8b0148... could not check the complete forcing
identity because its sole input omitted W, L_h and the four inverse formulas.
Here those data are charged explicitly from the frozen TASK. The conclusion
is conditional on that WHOLE stipulated Q-algebra, including its polynomial
divisibility/degree/normalization premises. No actual source coefficient-array
identification or regular-model comparison is added.

Inputs SHA-before-WHOLE:

- box/f10-mixed-kernel-scalar-astra-20260911/TASK.md
  dc9e3a27ed8e3052e89e598eb00cae060c9eaf3a5216c6a61b75bc0b0a3835f3.
- xmodel/f10-mixed-kernel-scalar-astra-20260911.md
  f6fe0986808f697e5e437af7f40ae5064cb609c92887a42a10963e91d09191c8.
- xmodel/f10-mixed-scalar-unit-gate-fable5-20260911.md
  aa8b0148f8bfb63ef072b23106f92bafa703a6b83033984e17a62f49eb70230f.

Fix integer r>=2, m=3r+1,n=5r+2. Let C be monic cubic and D monic
quintic, C(0)=a,D(0)=b,C'(0)=H, with a,b,H units and
mCD'-nC'D=-theta^7. All computations use formal power series at theta=0
over the stated commutative Q-algebra; divisions by C are legal there since
a is a unit. No reducedness, field factor or additional scalar inverse is
assumed. Write P=P_-,Q=Q_-,R=P_+,S=Q_+, e=[theta^2]R.
Their degree bounds are deg P,deg R<=2 and deg Q,deg S<=4.

Put a1=m-r,a2=m-r-1,b1=n-r,b2=n-r-1, so
a1+b2=a2+b1=2m and a1+a2=3m-n. In this notation the TASK gives

    L_r(P,Q)=mCQ'-b1 C'Q+a1 PD'-nP'D=0,
    L_(r+1)(R,S)=mCS'-b2 C'S+a2 RD'-nR'D=-2e theta^6,
    W=a1 PS'-b2 P'S+a2 RQ'-b1 R'Q.

## 1. Check the ENTIRE antiderivative identity

Define

    E=-b2 PS/C^2-b1 RQ/C^2+2n DPR/C^3.

Direct differentiation gives

    E' = W/C^2 - 2(R L_r(P,Q)+P L_(r+1)(R,S))/C^3
                    -6 theta^7 PR/C^4.                         (A)

Here is a coefficient audit, rather than a reference to an unspecified W.
Expand the right side and replace theta^7 by nC'D-mCD'. The coefficients
of P'S and R'Q are -b2/C^2 and -b1/C^2. Those of PS' and RQ' are
(a1-2m)/C^2=-b2/C^2 and (a2-2m)/C^2=-b1/C^2. The C'PS and C'RQ
terms have coefficients2b2/C^3 and2b1/C^3. The D(P'R+PR') coefficient
is2n/C^3. The D'PR coefficient is
(-2(a1+a2)+6m)/C^3=2n/C^3; the remaining DC'PR coefficient is
-6n/C^4. These are exactly every term of E'. No forcing term is omitted.

Substituting the two stipulated L-values into(A) yields

    W/C^2=E'-4e theta^6 P/C^3+6 theta^7 PR/C^4.

After integrating from0 and multiplying by C^2, the coefficient of theta^7
in C^2 E is2n[theta^7](DPR/C): PS and RQ have degree<=6. The constant
of integration contributes C^2 E(0), also degree<=6. The last integral
starts in degree8 and contributes nothing. The theta^6 integral contributes
exactly -4e P(0)/(7a), since its first integral coefficient is
theta^7 P(0)/(7a^3) and C^2 has constant term a^2. Thus the stated functional
Gamma=(21a/(2H))[theta^7] C^2 integral(W/C^2) satisfies

    Gamma=(21an/H)[theta^7](DPR/C)-6e P(0)/H.                  (B)

This proves the previously uncharged W-to-(B) step under the exact TASK.

## 2. Check the modified inverse, including its degree bounds

Let alpha=kappa_r/m=2nu-1 and beta=kappa_(r+1)/m=4-nu,
nu=n/m. Let T_alpha,T_beta be the theta-truncations through7 of
(C/a)^alpha,(C/a)^beta. In the plus inverse the TASK uses
T=T_beta-(2e/7)theta^7, so T'+2e theta^6=T_beta'. Consequently

    R=R0+(2e/7)C',       S=S0+(2e/7)D',
    R0=(C T_beta'/beta-C'T_beta)/theta^7,
    S0=(nD T_beta'/(m beta)-D'T_beta)/theta^7.

R0,S0 are polynomials: they equal the already stipulated polynomials R,S
minus the displayed polynomial corrections. They retain degrees<=2,<=4.
The omitted degree assumptions in the old FIRST are therefore explicitly
supplied, not inferred from a Laurent expression. Differentiating the
leading identity also gives L_h(C',D')=-7theta^6 for every h, agreeing with
the full modified row. The finite inverse formulas and leading identity give

    mCQ-nDP=T_alpha,             mCS0-nDR0=T_beta.

For example the second numerator is (-mCD'+nC'D)T_beta=theta^7 T_beta;
the T_beta' terms cancel identically. All of these are whole-polynomial
equalities, not sampled coefficients.

## 3. Cancellation and the reduced scalar

The leading identity says nDC'/C=mD'+theta^7/C. Since deg(PD')<=6,

    [theta^7](DPC'/C)=P(0)/(na).

Inserting R=R0+(2e/7)C' into(B) therefore cancels the ENTIRE
6e P(0)/H correction, with no division by e or P(0). Further,

    n[theta^7](DPR0/C)
       =-[theta^7](T_alpha R0/C)
       =[theta^14](C'/C)T_alpha T_beta.                       (C)

The first equality drops mQR0 of degree<=6. For the second, substitute R0;
the discarded T_alpha T_beta'/beta has degree<=13. This identifies all
dropped terms by their actual degree rather than their intended role.

Now lambda=H/a is a unit. With u=lambda theta and
phi(u)=1+u+Xu^2+Yu^3, X=aF/H^2,Y=a^2/H^3, one has
C(theta)=a phi(lambda theta), C'/C=lambda phi'/phi. Degree7 truncation
commutes with this invertible rescaling. Equation(C) contributes lambda^15
to coefficient theta^14, while a/H=lambda^-1. Therefore

    Gamma(W)=21 lambda^14 B(nu,X,Y),
    B=[u^14](phi'/phi) trunc_7(phi^(2nu-1)) trunc_7(phi^(4-nu)).

This proves the complete algebraic attachment claimed here. The separately
reviewed leading presentation S_r=Q[X,Y,(Yd5)^-1]/(d6,d7),
dk=[u^k]phi^nu, remains at its existing scope. The conclusion above neither
assumes nor establishes B's unitness. It holds over the whole stipulated
algebra, including nilpotents, and commutes with its base changes.

## Controls and interpretation

- Negative algebraic audit of(A): change the W coefficient of P'S from
  -b2 to+b2 while leaving E and both L_h definitions fixed. The formal
  coefficient comparison differs by2b2/C^2, with b2=4r+1 a nonzero rational
  unit. This falsifies that mutated general antiderivative identity; it is
  a symbolic identity control, not an actual Keller point or runtime test.
- The literal correction in(B) is indispensable before R is replaced:
  its cancellation partner comes from (2e/7)C'. Dropping either term while
  retaining the other leaves6eP(0)/H with its sign. No claim that eP(0)
  is nonzero on every component is needed or made.
- The already checked limiting control nu=5/3, X=1/3,Y=1/27 has B=0,
  since phi=(1+u/3)^3 gives the degree13 integrand(1+u/3)^13. It is not
  an actual finite r and prevents promoting a generic-parameter unit as
  all-parameter nonvanishing without its denominator/exception analysis.

This is PROPOSED-CLOSED only for the old missing-input algebraic step.
Different-model review is pending. The actual-r unit question, attachment
to any complete source coefficient arrays, regular-model comparison, REG,
source zero, all-F10 and JC2 remain unproved by this note. A future symbolic
elimination result must separately preserve Yd5 inversion and prove every
exceptional denominator nonzero at nu=(5r+2)/(3r+1), all integer r>=2.

## Read scope and custody

Three named inputs read WHOLE after current pins; existing accepted leading
presentation imported, not a new foundation review. All algebra manual;
no CAS, helper/import/AST/syntax/test/dummy execution, worker, source artifact
generation or live peer output consumed. Native source-author lanes are
independent and none of their unfinished output is an input. No new canonical
OPEN ID. Manual collision check identifies the exact previous gap above;
the corpus-reading collision scanner is not run across live report boundaries.
Unchanged administrative finalizer0f6aaf7d... and own apply_patch only.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7827`.
- Body SHA-256:
  `4da7d525998d89c5cecc6c8a0122b2e879747bd14e367716986f5a5cc521f9ef`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
