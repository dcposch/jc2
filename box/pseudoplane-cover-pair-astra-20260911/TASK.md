# Bounded non-Euler double-cover discriminator

ROOT assignment, 2026-09-11 12:22 UTC. Original report reserve12:36 / HARD12:40
UTC, never reset. Manual research only; no computation or runtime engineering.

Quantity: does the involution on the explicit cover below impose a NEW global
ramification constraint on a hypothetical regular scalar-bracket pair, beyond
ordinary Euler bookkeeping and the already-rejected rational-deck shortcut?
Cheapest test: compactify the generic first-coordinate curve and derive the
exact involution/ramification/deleted-point constraints, <=15 minutes UNMEASURED.
Either give a genuine contradiction or isolate the precise missing inequality;
do not just rename the open problem or expand sparse polynomial families.

Accepted object: S=Spec C[A,U,Z]/(U^2-A-A^2 Z), with
{A,U}=2A^2, {A,Z}=4U, {U,Z}=2+4AZ. A pair H,G in this ring with
{H,G}=c in C* would yield a noninjective polynomial Keller pair by
Phi(x,y)=(x^2,x+x^3 y,2y+x^2 y^2). This is a sufficient counterexample
endpoint, not an etale S-selfmap question. No such pair exists in hand.

Proposed cover to verify in your own argument:
T={t^2-1=x^2 Z}; sigma(x,t,Z)=(-x,-t,Z);
q:T->S, (A,U,Z)=(x^2,xt,Z).
T minus D_-={x=0,t=-1} is A2 through
t=1+x^2 y, Z=2y+x^2 y^2. D_+={x=0,t=1} is the other line.
q is expected finite etale degree2; sigma is free and swaps D_+,D_-.
The invariant scalar pair pulls back to T and agrees under sigma.

ROOT independently owns the H-only Euler bookkeeping/literature premise test.
Do NOT repeat it as your deliverable. In particular, bare Euler identities
may cancel all boundary-degree terms; test a stronger FULL-PAIR constraint.
For a generic fibre C of H, dG is nowhere zero on C but may have zeros only
at deleted points in its smooth projective completion. Treat disconnected
fibres, finite values at deleted points, and ramification at infinity honestly.
No smoothness=>local triviality, finite field extension=>finite morphism,
intermediate quadratic=>full Galois, or etale=>ML/Picard functoriality shortcut.

History context: APPROACHES.md currently lines60-70 explicitly stops the
rational-deck argument as a duplicate of the August30 line-complement
firewall. PP-HOM-1, PP-LIN-U-1, PP-SEP-WT-1, PP-3WT-1 exclude only exact
families; arbitrary-H affine boundary and all-R no-mate remain GAP. Formal
colliding boundary curves lift to arbitrary order, with no algebraization.
Read only required relevant historical ranges if necessary and state scope.
ROOT's runtime engineering attempt failed; this cycle's engineering allocation
is CLOSED. No AWS, model launch, source/test/CAS/dummy/syntax/AST/import run.

Write exactly xmodel/pseudoplane-cover-pair-astra-20260911.md via the usual
local artifact begin/close/finalize/expected-verify transaction; owned support
only in this task box. Pin TASK and any read historical inputs before body
consumption; manual proofs may be self-contained. Each raised OPEN states
quantity and cheapest test. No shared ledgers, protected repository, network
or process control; no further agents. Skeleton has no marker, append bounded
sections, append literal <!-- BODY-END --> only after all sections are on disk
and final checks complete, with nothing after it before the tool-added seal.
Return custody hash FIRST, report/expected manifest hashes and actual completion
time; all writers idle. A useful negative discrimination is a valid result;
no promotion, global claim or extra review project merely to fill the lane.
