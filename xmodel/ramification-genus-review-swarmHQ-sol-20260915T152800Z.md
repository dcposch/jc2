# Independent review: positive-genus ramification under source and target changes

Reviewer: swarmHQ gpt-5.6-sol. Basis:
`9f1ab9707ee789a11778335ce9cdf16b3b550f34`.
Producer report SHA256:
`a3a6793ba8f5c3ebccdd58e61ce8f1fa18ad4dd3d186950d2b961ac668a3a4b9`.
Evidence: MANUAL/BOOK-relative. This is a different-model hostile review,
not a novelty claim, classification of Keller fields, or JC2 result.

## Verdict

**CONFIRMED**, including ROOT's target-subfield corollary and the scoped
correction to the earlier Pinchuk reports. If `K/K0` is finite, `K0` is a
complex rational function field of transcendence degree two, and a
divisorial valuation `v` of `K` has `e(v/v0)>1` and residue genus at least
one, then no finite embedding `K -> C(x,y)` can turn any rational generating
pair of `K0` into a whole-plane polynomial Keller pair. More generally, no
algebraically independent pair in `K0` can do so: it generates a smaller
rational subfield and ramification persists down the additional finite leg.

## Reconstruction of the intrinsic valuation step

Let `w` be a divisorial valuation of `C(x,y)` with positive residue genus.
Realize it as a prime `E` on a normal proper surface. A common resolution of
the birational map from `P2` is obtained by point blowups of `P2` and has a
prime strict transform `E_W` with the same residue field. If `E_W` were
contracted to a point of `P2`, it would be an exceptional curve in a
point-blowup factorization and hence rational. Thus its image in `P2` is a
curve birational to `E_W`. It cannot be the line at infinity, again because
that line is rational. Its intersection with `A2` is therefore an affine
curve whose normalized order valuation is exactly `w`.

This uses a proper model and a common smooth resolution; it does not resolve
a rational map to a nonproper surface while silently retaining source `A2`.
It is compatible with the accepted morphic rational-forest correction and
does not revive its retracted rational-domination statement.

## Ramification contradiction on the affine plane

Assume an embedding `K -> L=C(x,y)` and polynomial images `(P,Q)` of a
rational generating pair of `K0`, with constant nonzero Jacobian. Extend
`v` to a divisorial `w` of `L`. Its residue field is finite over `kappa(v)`;
characteristic-zero Riemann--Hurwitz preserves genus at least one. Indices
in the finite tower multiply:

    e(w/v0)=e(w/v)*e(v/v0)>1.

The preceding step realizes `w` on an affine source curve `C_w`. The etale
map `(P,Q):A2->A2` is quasi-finite, so it cannot contract `C_w`. Its image
closure is a target curve `D`. The normalized restriction of `w` to `K0`
has center at the generic point of `D`; its valuation ring is the target DVR
`O_(A2,D)`. Localizing the etale map at the two generic points gives an
essentially etale inclusion of DVRs

    O_(A2,D) -> O_(A2,C_w),

whose ramification index is one. This contradicts the displayed strict
inequality. No positive genus for the base residue field, whole-map
finiteness, source-degree bound, or nonproperness parametrization theorem
is used.

## Target-subfield corollary

For any algebraically independent `p',q'` in `K0`, put
`K00=C(p',q')`. Since both fields have transcendence degree two and `K0` is
finitely generated, `K0/K00` is finite. The restriction of the divisorial
valuation remains nontrivial and discrete, and

    e(v/v00)=e(v/v0)*e(v0/v00)>1.

Applying the same theorem with rational base field `K00` proves exclusion.
Thus every rational dominant target postcomposition inside the original
target field is covered, not only birational changes. Algebraic dependence
would already make the final Jacobian zero.

## Pinchuk attachment and correction

The accepted literal Pinchuk reports supply `K0=C(p,q)`, `K=C(f,h)`, the
actual normalization chart `B_f=C[f,f^-1,h]`, and a genus-one critical
prime ramified with index two. Those accepted algebraic facts instantiate
the theorem directly, so every finite source embedding and every rational
dominant target postcomposition inside `C(p,q)` is excluded.

I authored the prior independent Pinchuk review. Its statement that genus
of the source divisor alone was insufficient was too broad as a claim about
donor exclusion and is withdrawn at that scope. Branch-image genus and the
six-distinct-critical-values proof remain correct and load-bearing for the
old proof through target nonproperness. The sealed arithmetic and its
branch-image conclusion are unchanged; the new intrinsic valuation proof
simply avoids that extra route.

## Controls and exclusions

- Positive genus without ramification is harmless: an elliptic valuation in
  the identity field extension has index one.
- Ramification with rational residue is not covered; `C(s,t)/C(s^2,t)` at
  `s=0` has rational residue and the displayed polynomial map is not Keller.
- The result needs a genuine ramified valuation of the stated finite field
  extension. An unrelated positive-genus curve on a rational presentation
  is insufficient.
- It covers target subfields contained in `K0`, not fields obtained by
  adjoining new elements or arbitrary other Pinchuk presentations.
- It does not show that a general hypothetical Keller source has such a
  valuation, exclude all-rational ramification, authorize a donor family,
  or resolve JC2.

Whole frozen inputs were read with matching hashes. The accepted Pinchuk
arithmetic was consumed rather than recomputed. No network source retrieval,
scientific execution, or external theorem upgrade was performed.

## COLLISIONS

status: EMPTY

- NONE — no `OPEN[...]` identifier or descendant is raised.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5615`.
- Body SHA-256:
  `a541c3e5c1ae3622fe1e3a150af9d7a2468bcd62bfd86fe9715dbe6a3dac3877`.
- Frozen basis: `9f1ab9707ee789a11778335ce9cdf16b3b550f34`.
