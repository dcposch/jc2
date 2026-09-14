# Contact lift: finite section is not finite suspension

ROOT, September12,2026. MANUAL/DOCUMENTARY, UNPROMOTED.
KNOWN contact-lift mechanism / SCOPE-CONFLICT for the proposed theorem use.
No Keller pair, normality theorem, new degree bound or JC2 conclusion.

## Exact calculation on the actual source

Let F=(f,g):A2->A2 be any complex polynomial Keller map with J(f,g)=1.
Write alpha=(x dy-y dx)/2 and take its polynomial canonical primitive
dH=alpha-f dg. If a chosen frame makes j=(f,g,H) finite birational,
retain that hypothesis literally; it is not a hypothesis that F is finite.

On A3 consider theta_source=dz+alpha and theta_target=dw+u dv. Then

    Phi(x,y,z)=(f(x,y),g(x,y),z+H(x,y)),
    Phi*theta_target=theta_source.

Both are contact forms, since their wedge with their differential is the
nonvanishing standard volume up to coordinate order. Setting s=z-xy/2
puts theta_source=ds+x dy, so this is also a strict standard-contact lift
after a polynomial source coordinate change. This is an exact polynomial
identity, not an appeal to local Darboux normalization.

There is another polynomial triangular automorphism

    T(x,y,z)=(x,y,z-H(x,y))

for which Phi composed with T=(f,g,z)=F times id_A1. Thus the contact lift
has exactly the original geometric degree. It is finite if and only if F
is finite: writing A=C[f,g] subset R=C[x,y], the product asks whether R[z]
is finite over A[z]. One direction extends finite generators; the other
reduces a finite module modulo z, yielding R finite over A. Composition
with T does not change finiteness. It is likewise a polynomial automorphism
if and only if F is: one direction uses the explicit triangular inverse;
an inverse for the product restricts on target z=0 to a polynomial inverse
for F. This calculation proves neither degree one nor finiteness for F.

The section Phi(x,y,0)=j(x,y) can therefore be finite even though no
finiteness of Phi has been established. Extra z cancels H independently.
As a scope control WITHOUT the Keller/contact hypothesis, use F=(x,xy),
H=y: j=(x,xy,y) is a closed embedding, but Phi=(x,xy,z+y) has an affine
line above (0,0,0). This only refutes the bare section-to-total inference.
Positive control: f=x,g=y,H=-xy/2 gives the triangular invertible lift.
No hypothetical noninvertible Keller map is asserted to exist.

## Primary theorem boundary and decision

[Cerveau--Deserti, arXiv1602.08866v2](https://arxiv.org/html/1602.08866v2),
Theorem1.1 and Propositions2.3--2.5, describe contact AUTOMORPHISMS and
their projection to plane automorphisms; the proof uses the Reeb direction
and polynomial exactness. Their input already assumes invertibility.
The birational results likewise start with birational maps. None supplies
that missing hypothesis for an arbitrary polynomial Keller lift. ROOT
read these statements and the short2.3/2.5 proofs, not the whole paper.

The campaign's prior contact-vector calculation already leaves the global
conductor division missing, and its deck-exactness check already uses this
paper in a different section. This is a bounded interface clarification,
not a new global contact program or another relaxed-control family. Do not
launch an automorphism-classification lane on Phi without separately proving
the very invertibility/birationality premise it requires. No FIRST is
selected for this unused documentary restriction; global ranking unchanged.

## Custody and read scope

Current-pinned then WHOLE local inputs:

- xmodel/canonical-contact-globality-discriminator-root-20260912.md,
  19bc27e6c6eec5bbdd16c6eb60c281634325c72381364e8f48d8a9f9b4e83739;
- xmodel/quadratic-deck-exactness-discriminator-root-20260911.md,
  6e134cb833e8ce7feacfad8835c5a5011e26c82498ad12c6e3ea943b0e038b7c;
- xmodel/canonical-conductor-euler-residue-astra-20260912.md,
  0b5aba8a38c17b17669c3c7f057b0d6c1457333c6d6923a65502a5371ffb5a66;
- xmodel/hypersurface-radial-pinching-control-astra-20260912.md,
  08457a1dbf44378f9b4b066247d7f8c8311addced8ddeee430848b8c0aeb0a3d.

Two targeted discovery queries; combined discovery output clipped, so no
complete-result claim. Only the direct primary article above is relied on;
other snippets are not evidence. Direct HTML statements/definitions and
the2.3--2.5 proof passage were subsequently read. No raw HTML/PDF snapshot
hash, exhaustive novelty assessment, broad-sweep or full-paper credit.
Canonical exact-term searches did not establish a new closing mechanism.
Manual algebra, text/hash/status, web reads, apply_patch and unchanged local
administrative finalizer only. No scientific interpreter/CAS/import/AST/
syntax/test, worker, protected-tree/mirror operation, or live peer payload.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4684`.
- Body SHA-256:
  `4d9f14a9b42e92d94ecaeb90ae9e4021a67f386fd59c699cff46ca446e5e457c`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
