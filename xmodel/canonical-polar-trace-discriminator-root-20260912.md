# Radial derivatives generate the source; the mixed-trace test remains open

ROOT, 2026-09-12. MANUAL / PRODUCER-CHECKED / UNPROMOTED. This postblind
note does not alter the FULL2150 frozen packet. The derivation was completed
before peer intake; this write follows that intake. No computational replay,
new literature theorem, properness, normality or JC2 claim is made.

## Exact source and finite generation

Let R=C[x,y], A=C[f,g], J(f,g)=1, and use the polynomial radial potential

    dH=(x dy-y dx)/2-f dg.

Write D_f=g_y partial_x-g_x partial_y and
D_g=-f_y partial_x+f_x partial_y. These commuting polynomial derivations
satisfy D_f f=D_g g=1 and D_f g=D_g f=0. With
E=(x partial_x+y partial_y)/2, the accepted radial calculation gives

    D_f H=-E(g),  D_g H=E(f)-f.

For the irreducible primitive graph relation P(f,g,H)=0, differentiation gives

    a=P_f/P_H=-D_f H=E(g),
    b=P_g/P_H=-D_g H=f-E(f),
    E=(f-b)D_f+aD_g,  E(H)=f D_f H.

Here a,b belong to R: no inverse of P_H is asserted to belong to R.
The following generation statement needs neither graph finiteness nor P.
Set D=max(deg f,deg g) in THIS polynomial frame and

    J_s=A[D_f^i D_g^j H : 1<=i+j<=s],  J_0=A.

Leibniz and the displayed expression for E show E(J_s) is contained in
J_(s+1), including s=0. Hence E^k f,E^k g belong to J_k. On polynomials
of total degree at most D, the operator

    pi_1=product_(0<=j<=D, j!=1) (E-j/2)/((1-j)/2)

projects to homogeneous degree one. It has degree D in E, so the linear
parts f_1,g_1 belong to J_D. Their coefficient matrix has determinant
J(f,g)(0)=1. Thus x,y belong to J_D and

    R=A[D_f^i D_g^j H : 1<=i+j<=D].

There are at most D(D+3)/2 listed positive-order derivatives. D is not a
uniform degree bound; a preliminary polynomial change of frame can enlarge
it. This upgrades the Euler field-generation argument to finite differential
algebra generation, not to integrality or an A-linear trace retraction.

Controls: f=x,g=y gives H=-xy/2 and recovers x,y immediately. On x!=0,
f=x^2,g=y/(2x),H=0 has J=1 and the same radial identity but fails generation:
the global polynomial hypothesis and invertible linear parts are essential.

## Cheapest mixed trace: useful control test, no forced violation

At an actual nodal target base change the accepted trace image is
S[1/u]+S[1/v]. For the already out-of-source rank-one control
h=u/v+v/u, all powers have trace in that additive module, whereas

    h_u h_v=2/(uv)-u/v^3-v/u^3

has a forbidden mixed principal part. Thus derivative products distinguish
that control. They have not been shown to force a mixed pole for the actual
Keller source, nor has the required actual node been forced.

Branch separation survives the test: take the product of
S[1/u][t]/(t^2-u) and S[1/v][s]/(s^3-v), with H=(t^-1,s^-1).
Each component is finite free etale over its respective localization.
D_u H is supported only on the first component and D_v H only on the
second. Their product is zero. All polynomial words in H and its derivatives
remain componentwise, so their traces lie in S[1/u]+S[1/v]. No polynomial
plane source, global radial frame or actual counterexample is asserted by
this auxiliary example. Finite derivative generation alone does not establish
the missing global relation between the branches.

Conclusion: retain the finite-generation interface as unpromoted; STOP the
generic mixed-derivative/control expansion until a source-specific mechanism
forces the forbidden class. No automatic higher-power farm is selected.

## Provenance, novelty and scope

WHOLE inputs: canonical-conductor-euler-residue-astra-20260912.md,
SHA256 0b5aba8a38c17b17669c3c7f057b0d6c1457333c6d6923a65502a5371ffb5a66;
radial-action-finite-graph-astra-20260912.md,
77669329f1c41ad39522bdf7a6484c59f63e45fd20eace77857845ed93115298.
Selected inputs: keller-trace-image-root-20260911.md lines190-235,
76fa7291c32150f8728b704116fdc92171ad40bf4c468bddfb1f01e0bf55c025;
keller-trace-shortcuts-gate-fable5-20260911.md relevant matched paragraphs,
78c8a8fbf6f0136f90bd99a75b62f3407f5cc91c6cf970d34d86a47e4008ffdb.
Historical TRACE-HAM already proposed mixed differential trace closure on
August24; general mechanism novelty is not claimed. Current canonical evidence
tiers, not old producer headers, own the imported radial and trace claims.

The history search was not explicitly scoped away from the two then-live
peer filenames; no peer text matched or was read, and ROOT's blind was already
sealed. This is a search-scope qualification, not a clean no-search record.
No new canonical OPEN identifier; finite-generation attachment only, no
descendants, allocation, source edit, runtime authority or publication.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4697`.
- Body SHA-256:
  `a2dcb0bb201ea4b00c748fbf4fcce868e3cd1742bb972816d67c523cb029cc80`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
