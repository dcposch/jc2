# Mixed scalar attachment to the actual critical compatibility

ROOT, 2026-09-12. Transaction opened19:50:18UTC.
MANUAL / PRODUCER-CHECKED / UNPROMOTED. No computational result.

## Scope and pinned inputs

This is an explicit composition of accepted band maps with the accepted
stipulated mixed-forcing identity. It identifies ONE actual highest
coefficient, not the complete source arrays, REG, or source nonemptiness.
The model-comparison necessary test was already named in the September11
TASK; novelty is claimed only for the explicit attachment supplied here.

Scientific inputs, SHA-before-WHOLE in this continuing ROOT turn and
unchanged current repins (some fresh rereads supplement earlier whole reads):

- xmodel/f10-all-r-early-band-tower-gate-fable5-20260909.md
  4683f9c72fdf3b8432e36963921a52b667d01a88fede273ee3db78e484bd0bd1.
- xmodel/f10-all-r-critical-band-gate-fable5-20260909.md
  568436589b21637c0a44ebff79221b822618edbb50e4fc56d3a86bc93815a164.
- xmodel/f10-all-r-kernel-highest-interface-astra-20260910.md
  53e17b24e6a0c258e873bf2f1c84823b5367b269a7744a272bbe61ef9d0c7312.
- xmodel/f10-mixed-forcing-attachment-root-20260912.md
  7ccbd83024c10b1d4d3fb898eda2c07abe429a5377db53f44895a6c2b02618b2.
- box/f10-mixed-kernel-scalar-astra-20260911/TASK.md
  dc9e3a27ed8e3052e89e598eb00cae060c9eaf3a5216c6a61b75bc0b0a3835f3.

The first three interfaces and fourth stipulated identity are imported at
their current accepted scopes, not their historical unreviewed headers.
The early review's stray ell weight is not used: ell first enters later
than the critical gap. The leading ring is already quotiented by the exact
leading equations; it is NOT a free polynomial ring in its coefficients.

Fix r>=2, m=3r+1, n=5r+2, q=2r+1, d=r+1. Work over the whole accepted
leading algebra B, with monic C=theta^3+F theta^2+H theta+a and monic
quintic D, a,b=D(0),H units, and mCD'-nC'D=-theta^7. Set lambda=H/a.
Primes mean theta derivatives. Define the B-linear functional

    Gamma(V)=(21a/(2H))[theta^7] C^2 integral_0^theta V/C^2.

Formal inversion and integration are legal over this Q-algebra because a
is a unit. All identities below commute with arbitrary base change,
including nonreduced bases; no chosen field factor is used.

## 1. The critical image is annihilated by Gamma

For deg P<=1 and deg V<=2, write

    L_q(P,V)=m(CV'-C'V)+rPD'-nP'D,    T=mCV-nDP.

More generally, for L_h=mCV'-(n-h)C'V+(m-h)PD'-nP'D and kappa=m+n-h,
direct differentiation gives

    T'-(kappa/m)(C'/C)T=L_h+(kappa/m)theta^7 P/C.

Indeed T'-L_h=kappa(C'V-D'P), and the leading identity supplies the
remaining term. At h=q, kappa=2m, so

    (T/C^2)'=L_q/C^2+2theta^7 P/C^3.

Here deg T<=6. Integrate and multiply by C^2. The correction starts at
theta^8, and both T and the integration constant times C^2 have degree<=6.
Their theta^7 coefficients vanish. Consequently

    Gamma(L_q(P,V))=0.                                      (1)

In particular Gamma(r theta D'-nD)=0. Separately, expansion of C^-2
through theta gives

    [theta^7] C^2 integral theta^5/C^2
       =-2H/(7a)+2H/(6a)=H/(21a),
    Gamma(2theta^5)=1.                                     (2)

## 2. Exact identification with the retained critical row

Use the accepted free-z homogeneous source envelope and its fixed rho
coordinates Y_h of weight h. Let W_q be the ENTIRE earlier forcing at
gap q. The actual critical A band is P=(z-U*d0)theta+k_r. After the
three upper reconstructions the residual, with sign Jacobian minus target,
is

    R=L_q(P,V)+W_q+2z theta^5=R1 theta+R0.                  (3)

Equations(1)-(2) imply Gamma(R)=z+Gamma(W_q). This does not drop U*d0:
that term belongs to L_q and is annihilated by the full functional.

Write the actual k_r column as chi=(chi1,chi0), and choose the accepted
leading-ring left inverse (ell1,ell0) with ell1 chi1+ell0 chi0=1.
For the k_r-free residual (c1,c0), let

    k*=-(ell1 c1+ell0 c0),    Psi_q=chi1 c0-chi0 c1.

The determinant-one row identity gives, after k_r=k*,

    R=(-ell0 theta+ell1)Psi_q.

Put gamma=Gamma(-ell0 theta+ell1). The accepted zero-earlier control
Psi_q(0,z)=c_z z gives gamma*c_z=1, so c_z and gamma are leading units.
Therefore (3) proves the actual polynomial identity

    Psi_q(Y,z)=c_z (z+Gamma(W_q(Y))).                       (4)

Earlier bands have weights<q, so W_q has no z dependence. No entry of
chi is separately inverted. This is an identity in B[Y,z] before imposing
the remaining compatibilities, not a pointwise statement on source solutions.

## 3. Restriction to the last two kernel variables

Set Y_1=...=Y_(r-1)=0 and write xi=Y_r, eta=Y_(r+1). Retain free z.
All bands of gap<r vanish by positive weighted homogeneity. At gap r the
actual pair is xi(P_-,Q_-), where the unmodified kernel has rho=1; at
gap r+1 it is eta(P_+,Q_+), the modified rho=1 kernel. There is no earlier
forcing at either step because r+1<2r for r>=2. Thus these are exactly the
TASK's finite inverses, including their degree bounds and modification,
not unrelated homogeneous pairs.

Intermediate reconstructed bands are not simply discarded. A gap-2r band
can contain xi^2. But in W_q its partner would have gap1, whose band is zero.
The only positive gap pairs summing to 2r+1 with both weights in the
semigroup generated by r,r+1 are (r,r+1) and (r+1,r). Hence

    W_q|slice=xi*eta*W_mixed,
    W_mixed=(m-r)P_- Q_+'-(n-r-1)P_-' Q_+
              +(m-r-1)P_+ Q_-'-(n-r)P_+' Q_-.

This uses actual bands including their particular solutions. In particular,
with p=[theta^2]P_- and e=[theta^2]P_+, the actual source coefficients
are d0=p*xi and U=-e*eta. The critical A band is

    P=(z+ep*xi*eta)theta+k_r,

not z theta+k_r. The earlier upper rows give Q_-,4=p/2 and Q_+,4=2e;
the mixed theta^5 coefficient is 2ep. Thus (3)'s theta^5 row is
-2(z+ep*xi*eta)+2ep*xi*eta+2z=0 identically, including e=0 or p=0.

The accepted stipulated-forcing identity now applies to these actual pairs:

    Gamma(W_mixed)=21lambda^14 B_r,
    B_r=[u^14](phi'/phi)trunc_7(phi^(2nu-1))trunc_7(phi^(4-nu)),
    phi=1+u+X*u^2+Y*u^3,
    nu=n/m, X=aF/H^2, Y=a^2/H^3.

Here X,Y inside phi are leading-ring scalars, distinct from the kernel
coordinates Y_h and xi,eta. Substitution in(4) yields

    Psi_q|slice=c_z (z+21lambda^14 B_r*xi*eta),
    H_q|slice=c_z*21lambda^14 B_r*xi*eta,                    (5)

where H_q=Psi_q(Y,0) is the accepted highest form. All factors c_z,21,
lambda are units. Thus this ONE actual mixed coefficient is a unit over
the whole B exactly when B_r is. Its unit status is not settled here.

## 4. What the model-comparison test actually decides

The proposed regular comparison has variables X_i of weights i=1,...,d
and equations M_h=[T^h](1+sum_i X_i T^i)^(q/d), h=q,...,m. On its analogous
last-two slice the critical form is

    M_q=(q/d)(q/d-1)*xi*eta,

a nonzero rational unit times xi*eta. Consider only a graded B-polynomial
coordinate automorphism and an invertible weight-preserving row change.
On variables of weights r and r+1 modulo the lower-variable ideal, such
an automorphism scales xi and eta by units: weights are distinct, and no
power of weight r has weight r+1 for r>=2. The first equation can only be
multiplied by a leading-ring unit, since every other row has higher weight.
Consequently any such comparison with the actual highest block REQUIRES
B_r to be a unit. This justifies the previously named necessary test by
an explicit actual-source coefficient map.

A nonunit answer stops only this kind of graded model comparison on the
affected component. It need not refute REG itself, and says nothing about
an actual source point. A unit answer passes only this coefficient test;
it supplies neither the remaining comparison identities nor REG, complete
arrays, the retained low/source rows, source zero, all-F10 or JC2.

## Controls, history and read scope

- Zero earlier variables give Psi_q=c_z z, the accepted nonzero control.
  Changing the target to +2z theta^5 and the matched A band to -z theta+k
  changes this to -c_z z. Keeping the old answer fails by 2c_z z, a
  nonzero polynomial over any nonzero leading algebra. This is a changed
  equation control, not a Keller point.
- Omitting the ep*xi*eta term changes the actual theta^5 bookkeeping by
  2ep*xi*eta; no assertion that ep is nonzero on every component is made.
- r=1 is explicitly excluded: r+1=2r then invalidates the zero-forcing
  argument at the modified step. No r=1 extension is inferred.
- Only the accepted leading units and rational integers were inverted;
  no U,e,p,chi entry,B_r or chosen field component was inverted.

History checksum is targeted, not whole-corpus: current APPROACHES/AUDIT
mixed-forcing entries, REDUCTION's relevant search hits, the September11
TASK/scalar producer/FIRST and accepted kernel-interface sections were
compared. The necessary test is KNOWN; this report makes its actual
critical-coefficient attachment explicit. No corpus-wide novelty claim or
new canonical OPEN ID. Existing unit question remains: decide B_r unitness
for every integer r>=2. The selected cheapest test is the already prepared
single Q(nu)[X] Bezout identity plus all actual-r exceptions, conditional on
source-FIRST and installed runtime qualification; original bounded caps
remain unchanged and no runtime estimate is asserted here.

All mathematics is manual. No scientific code/import/syntax/AST/compile/
test/dummy, worker or AWS action; no live peer body used. This result is
PRODUCER-CHECKED and awaits different-model FIRST. Canonical promotion
is not implied by transactional publication. Own-only collision check
finds no new OPEN label. Administrative finalizer and apply_patch only.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9689`.
- Body SHA-256:
  `8f289b881f3a58a70a83ba2056db5342a8e7899475f272ff2e0ea5fa3c298bbf`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
