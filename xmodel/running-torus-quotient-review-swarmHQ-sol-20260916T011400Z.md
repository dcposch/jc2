# Different-model review: no rational-target repair of the running quotient

Reviewer: swarmHQ gpt-5.6-sol, native task torus_quotient_sol_review.
Recorder: ROOT, transcribing the mathematical terminal review and final
verdict; this is not a verbatim execution log.
Evidence: MANUAL hostile proof review. Verdict: CONFIRMED, items A-E.
Completed: 2026-09-16T01:13:51Z.
Reviewed contribution: 5d9f995186d4814480cba2af0f1b1a9a18f45b82.

## Custody

The [charged proof](running-torus-quotient-target-rigidity-swarmHQ-root-20260916T011000Z.md)
and its manifest were frozen before this review. Sol reported unchanged
pre/post HEAD, expected basis, body/full/manifest and comparison hashes,
0444 modes for proof and manifest, and finalizer verification VERIFIED.
ROOT collected the complete mathematical review message and final verdict,
then observed authoritative COMPLETED before authoring this record.

Exact charged pins:

- Producer full:
  c2fb1886735a0e9070aa65b06d94dd91c9ae02223e976d9b203fd6efa9f26107.
- Producer body:
  22837333166c2916e082461405d2d1b9fdead05dc6d527d01eaa195952a049a5.
- Producer manifest:
  5d353f8b7f4acbf3acd78a16bd8ccbd3aad390c923296757bfd3457debf4ae22.
- Embedded basis: da1f1d30906fdf08a878c88126584173f1af7415.
- [Volume-neutral comparison](volume-neutral-torus-quotient-swarmHQ-root-20260915.md):
  181d7ae11675d27a61da977f143abaf5797415d6c64923e11be336281ce6df80.
- [Literal-triple/affine-section comparison](affine-target-plane-sections-swarmHQ-root-20260915T235600Z.md):
  4f47a46ee118fefe613dfefb01d223d80b957e931703235aad8b6d773eb3361c.
- FALLACY-v2.md:
  e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.

No files were edited by the reviewer, no network or scientific computation
was used, and no sealed bytes changed. Integrity supports custody, not the
mathematical conclusion; the independent derivations are below.

## A. Invariant rings and literal quotient — CONFIRMED

Source weights(1,-1,-2) make invariant exponents satisfy a=b+2c. Hence
the source invariant ring is C[xy,x^2z]=C[u,r], where

    xy=u-1,       x^2z=5-3u-r.

Target weights(-2,-1,1) give C[RQ,R^2P]. Expansion of the literal triple
independently yields

    R=xr,       xQ=4u+2-3u^2r,       x^2P=u^2+u-u^3r.

With w=ur, the induced whole-plane map is exactly

    s=2r+4w-3w^2,       t=w^2+wr-w^3.

No boundary is removed to establish either invariant ring or these identities.

## B. Jacobian and generic degree — CONFIRMED

The factorization through(w=ur,r) has determinants

    r  and  det[[4-6w,2],[2w+r-3w^2,w]]=-2r.

Therefore its source Jacobian is -2r^2. Elimination gives

    c=w^3-2w^2+s*w-2t=0,       r=c'/2.

The polynomial c is irreducible in C(s,t)[w]: in C(s)[w,t], it is
linear in t with unit coefficient and has prime quotient C(s)[w]; it is
primitive as a polynomial in w over C(s)[t], so Gauss's lemma applies.
Since the source field is C(s,w), the generic degree is3. This degree
does not conflict with a Keller degree exclusion: the Jacobian is nonconstant.

## C. Entire image and exceptional fibres — CONFIRMED

Any simple root w of c gives r=c'/2!=0 and u=w/r, an actual source
point. A cubic without a simple root has the form(w-a)^3. Coefficient
comparison forces a=2/3 and(s,t)=(4/3,4/27). There the only candidate
requires r=0,w=2/3, incompatible with w=ur. Thus the image is precisely
A2 minus this point.

The line r=0 contracts to(0,0). The latter cubic w^2(w-2) also has
the simple root w=2, giving(u,r)=(1,2). The proof does not assume
quasi-finiteness; the contracted line is explicitly included.

## D. Polynomial pullbacks of rational target functions — CONFIRMED

For a dominant polynomial map Phi:A2->A2 with cofinite image, write a target
rational function in reduced form a/b and suppose its pullback is a
polynomial H. Then a(Phi)=b(Phi)H as a polynomial identity.
For any irreducible beta dividing a nonconstant b, choose a point of
V(beta) outside V(a) and the finite omitted set. Coprimality and the
dimension of the curve allow this. Cofinite image supplies a preimage;
evaluation contradicts a(q)!=0. Thus b is constant.

Applied to the exact quotient, this proves

    C[u,r] intersect C(s,t)=C[s,t]

in the specified source field. It does not require finiteness, flatness,
properness or quasi-finiteness of the map.

## E. All rational-target repairs and scope — CONFIRMED

If rational h,k in C(s,t) pull back to polynomials, item D makes h,k
polynomials. The chain rule gives

    J_(u,r)(h(Psi),k(Psi))=-2r^2*J_(s,t)(h,k)(Psi),

which vanishes on r=0 and cannot be a nonzero constant. The conclusion
covers all such rational target pairs, including dominant nonbirational
pairs, on this fixed whole source plane.

The negative control Phi(a,b)=(a,ab), h(s,t)=t/s with pullback b is
valid: its noncofinite image shows why the lemma needs the image hypothesis.

There is no extension to arbitrary source substitutions, finite covers,
other torus actions or triples, target functions outside C(s,t), or general JC2.
Weights(1,-1,-2) remain outside the volume-neutral theorem. The comparison
claims are not broadened or collectively assumed. No successor is proposed.

## ROOT intake

ROOT's independent reconstruction agrees with A-E. The new result closes
only the named fixed quotient and rational-target repair. No computation
is represented as having been independently executed. Producer-time
lifecycle wording remains frozen; any promotion is recorded in AUDIT.

## OPENS RAISED

None; review complete at its charged scope.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Checker exit0, handle collected. This is not a novelty certification.
ROOT matched the five listed file hashes again before closure; unchanged.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5786`.
- Body SHA-256:
  `a3260f17c3d98b6503e942ba3df1a258d6dc813828a38338cff36846a694d4ad`.
- Frozen basis: `5d9f995186d4814480cba2af0f1b1a9a18f45b82`.
