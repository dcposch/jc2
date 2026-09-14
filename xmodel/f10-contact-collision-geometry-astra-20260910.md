# Off-diagonal paired contacts: manual global dimension discriminator

2026-09-10. Producer lane Astra; UNREVIEWED. First action 00:27:44 UTC;
fixed controlling stop 00:42:44 UTC; publication reserve starts 00:39:44 UTC.
This clock never resets. Only the three pinned WHOLE inputs below are charged.
ZERO mathematical subprocesses or coefficient artifacts. No computational
search, eliminant expansion, or mathematical code is part of this report.

## 1. Input and claim perimeter

- ROOT-CARD: box/f10-contact-collision-geometry-prep-20260910/ROOT-CARD.md,
  SHA256 224b8914c4411309cd1462775222600c0ce07d76972155aecc20858b59ec5859.
- accepted17w producer: xmodel/f10-two-exponent-contact-discriminator-astra-20260909.md,
  SHA256 4bbecd357077b422fbe636de61c9feefc5b304d88eea0a872b476456b1fbdf30.
- accepted17w first gate: xmodel/f10-two-exponent-contact-gate-fable5-20260909.md,
  SHA256 4a46e7f605759016829fcfb8ad92586fa9ebe875c4b5a62835b603c8b0ab1e90.

All three hashes matched before any WHOLE input read. Their union is the
entire science scope. The producer/gate have the exact ROOT-CARD acceptance
qualification: the gate's incidental Cramer expression must read
e_y=12(1+L)E/Gamma, with positive sign; u normalization is only a field-point
fact or the explicit u-unit chart. Old lifecycle prose does not override
that assignment. No linked provenance or actual coefficient file is read.

The question concerns the ENTIRE guarded complex algebraic locus, not one
component, one regular fibre, or only prescribed rational exponent pairs.
Even total finiteness would not establish emptiness or exclude rational
specializations. Contact emptiness still would not close the source/JC2.

## 2. Outcome: dimension at most one; zero-dimensionality remains GAP

For the exact ROOT-CARD ring C, the entire spectrum has Krull dimension at
most one (or is empty). This is a global bound, not a bound on one component
or a fixed-exponent fibre. No positive-dimensional component is exhibited.
The requested zero-dimensionality/emptiness verdict remains GAP.
All these algebras are of finite type over Q; extending the coefficient
field to an algebraically closed characteristic-zero field preserves this
dimension bound, even if irreducible components split after extension.

The additional manual fact behind this partial bound is an EMPTY UNGUARDED
fibre at (x,y)=(3,6), where all exponent denominators are units. The accepted
monic cubic makes the unguarded algebra finite over the exponent plane.
Its support therefore is a proper closed subset of that plane. Localizing
W cannot increase dimension. This argument is insufficient to exclude
curves in that proper closed support; section 6 states their exact test.

In particular, the partial bound is not an assertion that a finite fibre
or one empty guarded fibre proves total finiteness. The unguarded finite
algebra and its closed support are indispensable to the argument.

## 3. Exact global ring, guard, and read-back

Write d=y-x, s=x+y, p=xy and

    Gamma=36p+9s^2-114s+181,
    Omega=15s^2-36p-30s+35,
    D=x*y*(x-1)*(y-1)*(3x-5)*(3y-5)*(2-x)*(2-y)
      *d*(s-3)*(4-s)*Gamma*Omega,
    S=Q[x,y,D^-1],                 H=D*W.

The desired algebra is exactly

    C=S[V,W,W^-1]/(A_x,B_x,A_y,B_y).

All factors of D, and W itself, are explicitly inverted. On the prescribed
5/3<x<y<2 every factor of D is nonzero, with the accepted Gamma/Omega
positivity. Over the complex exponent plane we use only their nonvanishing;
no order or sign is imposed on coefficients or exponents. The divisors
x=0, y=0, x=1, y=1, 3x=5, 3y=5, x=2, y=2, d=0, s=3, s=4,
Gamma=0, Omega=0 are outside Spec S and cannot supply a countercomponent
to this question. No other exponent divisor is removed below.

For clarity the literal rows being used are

    A_X=W^2/2+(X-2)(V+(X-3)/6)W
       +(X-2)V^3/6+(X-2)(X-3)V^2/4
       +(X-2)(X-3)(X-4)V/24
       +(X-2)(X-3)(X-4)(X-5)/720,

    B_X=W^2/2+V^2W/2+(X-3)VW/2+(X-3)(X-4)W/24
       +(X-3)V^3/6+(X-3)(X-4)V^2/12
       +(X-3)(X-4)(X-5)V/120
       +(X-3)(X-4)(X-5)(X-6)/5040.

Here are finite formulas for all algebra objects used in the proof. They
are definitions by the charged polynomials and monic division, not emitted
or evaluated coefficient artifacts:

    P_X=4V^3+4(X-3)(X-1)V^2
       +(X-3)(X-4)(4X-5)V/5
       +(3X-4)(X-3)(X-4)(X-5)/105,
    Q_X=(X-3)(3X-4)+12(X-1)V-12V^2,
    Vstar=(13-3s)/12,             L=(x-1-V-Vstar)/d,
    N=(1+L)P_x-LP_y,             w=12N/Gamma,
    E=Q_y P_x-Q_x P_y,           M=E/(48d(s-3)),
    F0=A_x(V,w),                 F1=(A_y(V,w)-A_x(V,w))/d,
    R1=F1-E/(d*Gamma),           J=-(6Gamma/Omega)R1,
    Z0=rem_J F0,                 Z1=rem_J M.

In these definitions J is monic of degree three; Z0,Z1 have degree at most
two; w has degree exactly three. Each coefficient belongs to S. Inverting
the product D in a commutative ring inverts each listed factor, so every
division displayed here is valid globally on Spec S, including at primes
where an individual Q_x or Q_y vanishes.

The accepted identities are polynomial identities after these explicit
denominators are cleared; their derivations therefore apply to S, not only
to rational specializations. In particular

    24(A_X-B_X)=P_X+Q_X W,
    (1+L)Q_x-LQ_y=-Gamma/12,
    (P_x+Q_x W,P_y+Q_y W)=(W-w,E).

The last identity is over S[V,W] and uses the unit -Gamma/12; it does not
invert either Q separately. With W=w the four-row ideal becomes
(F0,F1,M)=(J,Z0,Z1). Thus, even BEFORE imposing W!=0,

    C0:=S[V,W]/(A_x,B_x,A_y,B_y)
       ~=S[V]/(J,Z0,Z1).

The map fixes S and V and sends W to w. For the inverse, J=0 gives R1=0;
Z1=0 gives M=0 and hence E=0; Z0=0 gives F0=0; then F1=0 and A_y=0.
The ideal identity restores both P+QW equations, and so both B rows.
This is a ring isomorphism with nilpotents retained. Finally

    B=S[V]/(J),                 C0=B/(Z0,Z1),
    C=C0[w^-1].

B is a FREE S module of rank three with basis 1,V,V^2; C0 is a finite
S module. C is of finite type over S and has finite fibres, but this report
does not assert that C is finite over S: localization by w can destroy
that property. No original unnormalized u has been silently inverted here.

## 4. An exact empty unguarded fibre and the global dimension bound

Take (x,y)=(3,6), a complex/rational exponent-plane point used only to test
the full algebraic family. It is outside the prescribed real interval.
Here d=3, s=9, p=18, Gamma=532 and Omega=332. Every factor of D is nonzero.

Direct substitution into the literal rows gives

    A_3=W^2/2+VW+V^3/6,
    B_3=W(W+V^2)/2.

Consider any common zero over an algebraic closure of Q. If W=0, A_3=0
implies V=0, whereas A_6(0,0)=4*3*2*1/720=1/30, a contradiction.
If W!=0, B_3=0 implies W=-V^2, so V!=0 and

    A_3(V,-V^2)=V^3(3V-5)/6.

Thus V=5/3, W=-25/9. The fourth row rules out this point: directly from
the displayed B_X formula,

    B_6(V,-V^2)=-V^3+V^2/4+V/20,
    B_6(5/3,-25/9)=-125/27+25/36+1/12=-104/27 != 0.

These two cases exhaust every field point, including the W=0 branch.
Consequently C0 tensor_S k(3,6) is the zero algebra. For justification
without any reducedness assumption: it is a finite-dimensional algebra;
if nonzero it has a maximal ideal and then a point over the algebraic
closure, contradicting the two-case calculation.

Because C0 is finite over S, Nakayama's lemma at this maximal ideal gives
(C0)_(3,6)=0. Equivalently a neighbourhood of (3,6) misses the support of
C0. The domain S is a localization of Q[x,y], of dimension two, and the
support of a finite S module is closed. It follows that supp_S C0 is a
PROPER closed subset, of dimension at most one. Since S->C0 is finite,
dim C0<=1. Localization cannot increase Krull dimension, and hence

    dim C <= 1,                   unless C is the zero ring.

Equivalently the generic unguarded fibre over Q(x,y) is zero. This does
not assert that every specialization is zero: a finite torsion S algebra
can be supported on a curve. It is exactly that remaining possibility
which the requested zero-dimensionality discriminator must address.

## 5. An exact finite rank test for the W guard, fibre by fibre

Write J=V^3+j2 V^2+j1 V+j0 and let

            [ 0  0  -j0 ]
    T =     [ 1  0  -j1 ],       e=(1,0,0)^t.
            [ 0  1  -j2 ]

T is multiplication by V on B in the ordered basis 1,V,V^2. If z_i is
the three-coordinate column of Z_i, the ideal (Z0,Z1) in B is the S-span
of the six columns of

    K=[z_0, T z_0, T^2 z_0, z_1, T z_1, T^2 z_1].

Indeed any multiplier in B has a representative of degree at most two in
V with coefficients in S, so these are every needed product. In particular
C0 is the cokernel of this literal 3-by-6
presentation matrix. Define one further column, without expanding it,

    c=w(T)^3 e.

This is the coordinate vector of w^3 in B. The exponent three is essential
and is not a claim that a global saturation stabilizes at three.

At any prime q of S, put k=kappa(q) and A=C0 tensor_S k. Its k-dimension
is at most three. The guarded fibre A[w^-1] is zero exactly when w is
nilpotent in A. In a k algebra of dimension at most three this is equivalent
to w^3=0: nilpotent multiplication by w has nilpotency index at most three,
and its action on 1 recovers w^3. Therefore

    C tensor_S k != 0
      <=> c is not in the k-column-span of K
      <=> rank_k[K|c] > rank_k K.                         (*)

This equivalence covers every residue field, algebraic closures, zero
residual polynomials, multiple roots, and nonreduced fibres. It requires
no sign assumption and does not invert a matrix entry globally.

For an explicit finite chart statement, let I_(r+1)(K) be the ideal of all
(r+1)-minors of K. For r=0,1,2 choose any r-minor m of K (m=1 when r=0)
and any (r+1)-minor n of [K|c], and put

    S_(r,m,n) = S[(mn)^-1]/I_(r+1)(K).                    (**)

A zero polynomial choice gives the empty chart. Each nonempty chart is
exactly a locus on which rank K=r and rank[K|c]=r+1. Conversely every
prime satisfying (*) belongs to one such chart. Thus these finitely many
charts cover EXACTLY the image of Spec C in Spec S. No divisor has been
discarded by any one choice of m or n; all choices and all three ranks are
retained. The extra localizations in (**) are a covering description, not
an enlargement of the guard D.

Since V satisfies a monic cubic and W=w(V), the residue field at any prime
of C is algebraic over the residue field at its image prime in S. For an
irreducible component this equates the transcendence degrees of its
function field and of the closure of its image. Both rings are of finite
type over Q, so the component and that image closure have equal dimension.
The constructible image is the finite union of the charts (**). It follows
that dim C is the largest dimension of a nonempty chart (**). This is a
dimension statement; it is not an isomorphism of C with that chart union.

The (3,6) calculation also gives a concrete nonvanishing conclusion about
K without claiming a computed minor: its specialization there has rank
three because its cokernel is zero. Hence at least one 3-minor of K is a
nonzero element of S, and I_3(K) is nonzero. This gives the same proper
support/dimension-at-most-one argument as section 4. Which minor it is,
and its coefficients, have neither been computed nor asserted.

## 6. The exact remaining elimination statement

The requested result dim C<=0 (allowing C=0) is now equivalent to either
of the following statements, NEITHER of which is proved here:

1. For every r=0,1,2 and every minor pair m,n in (**), the chart ring
   S[(mn)^-1]/I_(r+1)(K) is zero or has Krull dimension zero.

2. For EVERY height-one prime q of S, reduce the literal J,Z0,Z1,w modulo
   q into kappa(q)[V]. Then the coordinate column of w^3 belongs to the
   column span of K over kappa(q); equivalently

       w^3 belongs to (J,Z0,Z1) in kappa(q)[V].            (***)

To see why no other positive-dimensional case is missing from statement
2: the generic fibre is already zero by section 4. A positive-dimensional
component of C would therefore have dimension one and its generic image
would be a height-one prime of the two-dimensional S, by the algebraicity
of residue fields. Conversely failure of (***) at a height-one prime
gives a nonzero finite guarded algebra over that residue field, hence a
prime of C whose image closure and own closure both have dimension one.

This pinpoints the unresolved elimination issue as the possible survival
of a curve divisor after the W guard. A nonzero single resultant, a
nonzero single 3-minor, or the already-proved generic emptiness can only
show that the image is proper; those facts do not establish (***) at
every such divisor. No common-factor exclusion, height-two certificate,
or nonzero rank-stratum eliminant has been supplied. In particular no
sign is asserted on unexpanded coefficients.

The single-contact projection lens would need precisely to rule out those
curve families of distinct exponents with shared coefficients, on EVERY
relevant component and every exceptional locus. Birationality of just one
component, or an assertion at one regular fibre, does not supply (***).

## 7. Changed-object controls and mathematical limits

- FINITE FIBRES ARE NOT TOTAL FINITENESS. Over S'=Q[a,b], replace the
  charged objects by the toy J'=V^3-1, Z0'=Z1'=0 and w'=V^3. The guarded
  algebra equals S'[V]/(V^3-1), since w'=1 there. Every fibre has dimension
  three as a vector space, yet its total Krull dimension is two. This is
  a changed-object control, not a counterexample to the charged formulas.

- EVEN ONE EMPTY UNGUARDED FIBRE DOES NOT GIVE DIMENSION ZERO. The finite
  toy S'-algebra S'/(a), with guard w'=1, has empty fibre at a=1 and
  nonempty curve support a=0. Thus the logical strength of section 4 is
  exactly the proved bound one; its emptiness calculation is not promoted
  to a zero-dimensionality certificate.

- ONE EMPTY GUARDED FIBRE DOES NOT EVEN FORCE PROPER CLOSED SUPPORT BEFORE
  GUARDING. In the free rank-one algebra S' with w'=a, the guarded algebra
  S'[a^-1] has empty fibre at a=0 and dense two-dimensional image. This
  is why section 4 checked W=0 as well as W!=0 and used C0's finiteness.

- NONZERO IS NOT NONNILPOTENT. In k[epsilon]/(epsilon^3), take w=epsilon.
  It is a nonzero vector, but localization at w is zero. The guard test
  using c=w^3 rather than w correctly yields zero. This also explains why
  (*) is a fibrewise test, not an assertion that w^3 annihilates a global
  S-module whenever its localization vanishes.

- NO EXPONENT DIVISOR IS HIDDEN. The divisions in section 3 use factors of
  D. The d=0 diagonal and the other listed factors are intentionally absent
  from this question. For example dropping d from the guard would make L
  undefined there and repeat the single-contact equations; that different
  object is not covered by the distinct-exponent reduction.

- COMPLEX VERSUS PRESCRIBED. The point (3,6) is only a lawful specialization
  of the complex algebraic family, and is not an admissible prescribed
  exponent pair. If (***) were to fail, the resulting complex curve would
  refute zero-dimensionality of C; it need not meet 5/3<x<y<2, nor have the
  rational/integer specializations required by the original problem. No
  such curve has been constructed here. If (***) were proved, the finite
  algebraic exponent set would still need exclusion. Neither possibility
  by itself establishes all earlier forcing/companion rows or closes JC2.

## 8. Documentary scope and disposition

The three pin-verified WHOLE inputs are the entire scientific record used.
The mathematical work was manual substitution, exact ring identities and
finite-module reasoning. No mathematical subprocess of any size, emitted
coefficient file, numerical search, CAS, network, process inspection, AWS, SSH,
agent launch, ledger/corpus/history scan, protected tree inspection, shared
file mutation, or follow-on execution occurred. Existing publication tools
were used only for the owned documentary transaction. Frozen basis files
were not altered. Root owns terminal custody and any first different-model
gate or promotion; this producer supplies no promotion or execution authority.

Verdict: PARTIAL global dimension <=1 established; requested dimension <=0,
emptiness, or an exact positive-dimensional countercomponent remains GAP,
precisely the divisor condition (***) / all-chart dimension test (**).

## OPEN(S) RAISED

- ASSIGNED GAP ONLY, no new canonical ID: determine whether every guarded
  height-one exponent prime satisfies (***), equivalently whether every
  nonempty chart (**) is zero-dimensional. The rank objects are specified
  exactly by the charged polynomial formulas; their divisor/rank verdict
  is unproved. A coefficient expansion, elimination, or code campaign is
  not authorized by this report. No source or JC2 closure follows.

## COLLISIONS

status: EMPTY

- NONE found in the own-only extraction: the assigned report and box were
  absent at first action. No corpus collision search was licensed or run.
  ROOT-CARD's bounded historical checksum is not a new all-corpus claim.

The completed own WHOLE report and PINS were read; the own-only OPEN and
collision extraction was checked at 00:34:57 UTC. The only raised question
is the assigned, precisely specified GAP above. This final completion edit
records that review and the explicit field-extension perimeter; no new
mathematical computation or external read was performed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17525`.
- Body SHA-256:
  `69e00076c29d8817565cedf2d0bbf7916a9f3a9ba28e1b8dba8cc799d577989b`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
