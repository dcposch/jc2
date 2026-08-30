# Binding integration: one-point D3 Halphen weighted obstruction

Date: 2026-08-30 UTC  
Integrator: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `591b8d944be1310483d9eccb8495008457a9f19a`  
Disposition: **PROMOTE WITH REVIEW CORRECTIONS / ACTUAL-MORPHIC ROW EMPTY**

## 0. Binding verdict

Promote the one-point index-three Halphen obstruction on its exact charged
scope.  In an actual normal morphic proper-block occurrence of

```text
m=3,                 T=2t0,
F_(t0)=3L,           exact plane CFS level two,
minimal strictly-Henselian-insoluble floor level one,
```

the promoted local gates leave only the critical triple-root shard.  After
the legal local translations, every survivor has complete lowest weighted
face

```text
X^3+tY^3+alpha*t^2*X*Y+eta*t^5,       eta!=0,
wt(X,Y,t)=(5,4,3).
```

The weighted exceptional curve always has boundary invariant one.  It is a
smooth genus-one curve when `alpha^3+27eta!=0`; on equality it is an
irreducible rational curve with one ordinary node, and resolving that
self-node produces a graph cycle.  The weighted strict transform is normal,
so the node persists as `uv+r^n`, `n>=1`, and every good resolution retains
the genus or cycle.

At actual proper-block occurrence the marked finite normal incidence is the
local germ of the intermediate surface.  Its singular center is disjoint from
the everywhere-defined etale first-leg image `V=g1(A2)`, so the extracted
configuration is boundary on a common resolution.  This contradicts the
reviewed morphic rational-forest theorem for the actual dominant morphism
`A2->V`.  Therefore the row `m=3,T=2t0` is empty in the actual normal morphic
proper-block scope.

This is not an abstract surface nonexistence theorem, a global occurrence
theorem, a statement about arbitrary rational domination, a polynomial map,
or JC2.

## 1. Frozen evidence and custody

```text
58173d4f18a575ca49164fafef91b7ba8b50e670c9e8a39376d55bb647732e2f
  xmodel/bd-a2-d3-halphen-weighted-boundary-obstruction-sol56-20260830.md
  body 2fc2cd21c17cda40118eb281fbd36d6f7f586e33386930952f415b2f4f440bee
ee2a3697e251771cad96ec198f17967b33807156e71ed4c47692da4eecd16381
  xmodel/bd-a2-d3-halphen-weighted-boundary-obstruction-sol56-20260830.md.artifact.json

290edb38183ad3868cb8482ccfcd4c2b66cfc4101c8aaaed512b3c69bfb1ec20
  xmodel/bd-a2-d3-halphen-weighted-boundary-corrigendum-sol56-20260830.md
  body aa65587227ce63081330434cc0001a4b61a588bd106ef513848dc779af5c1092
fd954ded8ea910e52da57f032156f4d5d489e83f14fe6acee30660a2868b9871
  xmodel/bd-a2-d3-halphen-weighted-boundary-corrigendum-sol56-20260830.md.artifact.json

5ac604b99f017fe9d051540e992b91241188d2ee3cfde94c500c5df058644f6c
  xmodel/bd-a2-d3-halphen-weighted-boundary-hostile-rereview-fable5-20260830.md
  raw body ae5c2545da7c5422ad611a9d91dbd6bce7ea276102bf3d943b1c09197536ee80
8f4e419c0cd89352b1eddab311dbc938006ea06a3c955e8d3c45e7429f161acf
  xmodel/bd-a2-d3-halphen-weighted-boundary-hostile-rereview-fable5-20260830.run.v2
```

The compact Fable 5 lane exited zero.  Before reading its report, root
reproduced the immutable prompt, Claude adapter, launcher, Seatbelt profile,
charge validator, `FALLACY-v2.md`, reconstructed composed prompt, report,
log, and all eight charged mathematical hashes.  The raw report body hash
matched the receipt, `charge_basis_status=ABSENT` was the required outcome,
and the report was stamped on its receipt basis before custody commit
`591b8d94`.  Fable returns `CONFIRM_WITH_CORRECTIONS`.

The exact replay is

```text
2601681db842d66ce5cc479c4304ab684b983b634cad5f7995b8b9b5c25b340a
  ops/d3_halphen_weighted_boundary_replay.py
```

Fable reproduced ordinary, `-O`, and `-OO` output byte-for-byte: 599 bytes,
SHA-256 `a5d5ec6b3abcca9d83edf45f04ff5ca81376f257d4ae0970004f5155041a150c`.
The sign mutation and unknown argument both fail closed; the script has no
AST `assert` nodes.

## 2. Adopted review reconstruction

### 2.1 Complete face

The equation `5a+4b+3c=15` has exactly the four monomials

```text
X^3,       tY^3,       t^2XY,       t^5.
```

After the first-cube relations and the legal translation
`X=x+st, Y=y+lambda*t`, the complete sub-weight-15 residue is

```text
(d-lambda^3)t^4+kappa*X*t^3.
```

The final CFS flags kill these two terms and impose `eta!=0`.  Thus no lower
or equal-weight term is omitted, and no coefficient normalization or illegal
parameter-dependent rescaling is used.  Literal raw coefficient-base degree
three is essential only to this census.

### 2.2 Exceptional curve

On the index cover of the `t!=0` chart, the exceptional curve is the free
`mu_3` quotient of the Hesse cubic.  Direct elimination gives the unique
singular locus exactly when

```text
alpha^3+27eta=0.
```

Off it the quotient is smooth genus one.  On it the cover is an honest
triangle whose lines and vertices are each permuted transitively; the
quotient is one irreducible rational component with its two marked points
identified, hence one ordinary node.  The curve avoids the index-three
quotient vertex because `eta!=0`, and is smooth at the index-four point.
Fable supplies the omitted one-line compactification check: at every Hesse
point with `w=0`, `F_u=3u^2!=0`.  There is no hidden singularity at infinity.

### 2.3 Normality and persistence

Every index cover of the weighted strict transform is a hypersurface and its
finite characteristic-zero quotient is Cohen--Macaulay, hence `S2`.  The
strict transform is smooth over every smooth point of the exceptional curve;
its only possible singularities are the free-orbit node and the quotient
point, so it is `R1` and normal.

At the node, parametric Morse reduction gives `uv+phi(r)`.  Normality rules
out `phi=0`, hence after a unit rescaling `phi=r^n`, `n>=1`.  For `n=1`, one
blowup records the two branches by parallel edges; for `n>=2`, the
`A_(n-1)` chain joins two branches of the same irreducible component.  Both
give first Betti number one.  The quotient resolution adds only a rational
tree.  Point blowups preserve `sum(genera)+b1`, so every good resolution has
boundary invariant one.

### 2.4 Actual-block interface

The identity `F(t;0,0,1)=s^3t^3` gives a local order-three Weierstrass
factor.  This proves local finite incidence, not global projective finiteness.
Identification with the intermediate surface is an explicit actual-normal-
incidence premise.  Under that premise, the singular point has multiplicity
at least three and cannot lie in the etale first-leg image.  The forest
theorem is applied to the actual image `V=g1(A2)`, without shrinking and
without replacing the morphism by a rational map.

## 3. Binding corrections

The producer is consumed only through its prior corrigendum and these review
repairs:

1. Add the `w=0` smoothness check above to the Hesse compactification.
2. The replay checks the displayed singular candidates but not their
   exhaustiveness; the prose elimination supplies exhaustiveness.
3. The replay's `analytic_shift` metadata mentions `z` while operating in the
   `z=1` chart.  This is cosmetic and has no mathematical consumer.
4. Retain every corrigendum firewall: other Du Val points are permitted;
   finiteness is local; the strict transform is not normalized after the
   fact; the occurrence premise is explicit; and cycle persistence uses the
   resolved local model rather than connectedness alone.

No correction changes the row verdict.

## 4. Maximum-safe theorem and stop rule

> **One-point D3 Halphen obstruction.**  Charge the promoted D3 Hodge row,
> local gates, block structure, corrected morphic forest theorem, literal raw
> coefficient degree three, and actual normal locally finite proper-block
> incidence.  Then every survivor in `m=3,T=2t0` extracts a boundary
> subconfiguration of invariant one, contradicting the rational-forest
> boundary of the actual first-leg image.  Hence this row has no actual
> morphic proper-block occurrence.

Stop further CFS, weighted-face, Hesse, or global-control work intended only
to close this row.  Retain the diagonal and global surfaces as regression
controls, not occurrences.  Redirect D3 capacity to the two sectioned rows
and to block-general discriminants.  A local or global surface without the
actual first-leg interface remains compatible with this theorem.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8281`.
- Body SHA-256:
  `c3104d390d9f0d48159c74b270e7025af5d566bde1962904ca28119ada3c9f87`.
- Frozen basis: `591b8d944be1310483d9eccb8495008457a9f19a`.
