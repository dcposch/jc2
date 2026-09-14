# Low-fiber tower transfer — different-model FIRST

Sol, September 13, 2026. MANUAL / DIFFERENT-MODEL FIRST. Verdict: **CONFIRMED, conditional on the three accepted Keller/block premises and EMBEDDED-PLANE-TRANSFER-1 exactly as curated in the task.** This reviews the new compositum and image-closure composition only; it does not reprove those premises.

## Claim-by-claim verdict

- **Compositum degree inequality: CONFIRMED.** For `M_r=K E_r`, scalar extension gives the finite `M_r`-algebra `E_(r-1) tensor_(E_r) M_r`, of vector-space dimension `[E_(r-1):E_r]`. Its multiplication image in `L` is a finite domain over `M_r`, hence a field, and contains exactly the generators of `K E_(r-1)=M_(r-1)`. Therefore `[M_(r-1):M_r] <= [E_(r-1):E_r] <=3`. Neither equality nor divisibility is used.
- **Last-strict-drop argument: CONFIRMED.** Since `M_0=L` and `M_m=K`, if `L!=K` the last strict adjacent drop `M_(r-1)>M_r` has `M_r=K` and degree exactly 2 or 3. If its upper field is `L`, the accepted generic-mapping-degree-at-most-three premise applies; otherwise it is an actual strict intermediate `K<M_(r-1)<L` with second leg 2 or 3, excluded by the accepted block premises. Thus `L=K`, and accepted birational Keller automorphy finishes. Equal steps and `E_m<K` cause no gap.
- **Geometric image-closure tower: CONFIRMED.** The hypotheses imply the asserted field tower, including arbitrary/nonbirational `i` and generic source degree up to 3.
- **Finite compositions/iteration escape: CONFIRMED.** The proof bounds each induced field step, not the full iterate's point fibers or a product `3^m`.
- **Controls and stated exclusions: CONFIRMED.** They expose exactly the two invalid substitutions—degree divisibility after compositum and ambient generic degree in place of every-fiber control—and the reversed inclusion for projections.

## Geometric reconstruction

Let `Z_r` be the reduced closure of `j_r(A2)`. The initial assumption makes `Z_0` integral of dimension two and gives `[L:C(Z_0)]<=3`. For each `r`, the restricted map `Z_(r-1)->Z_r` is dominant because its image contains the dense set `j_r(A2)`. Every one of its point fibers is a subset of an ambient `phi_r` fiber, hence has at most three points. It is therefore quasi-finite. Dimension stays two, and over `C` its function-field extension is separable; after shrinking, the generic geometric fiber consists of `[C(Z_(r-1)):C(Z_r)]` distinct points. Consequently every induced degree is at most three.

Pullback through the dominant maps embeds

```
L >= C(Z_0) >= C(Z_1) >= ... >= C(Z_m).
```

From the full factorization `j_m=i h`, every rational function on `Z_m`, pulled back to `A2`, is a rational expression in `f,g`; hence `C(Z_m) subset K`. Equality is neither claimed nor needed. This remains valid when `i` is nonbirational: the preceding quasi-finiteness already forces its composite image to have dimension two. Exceptional targets do not create a hidden degree because the premise bounds every ambient point fiber. Conversely, an ambient generic-degree bound alone cannot control a restriction over an exceptional locus.

## Controls and scope attacks

For the degree-drop control, with `alpha^3=2` and primitive cube root `zeta`, `E=Q(alpha)` has degree 3 over `Q`, while `L=Q(alpha,zeta)` has degree 2 over both `E` and `K=Q(zeta alpha)`. Also `KE=L`. Thus the cubic step `E/Q` becomes the quadratic step `L/K` after compositum; 2 does not divide 3. The producer's inequality is the correct invariant.

For the geometric control, `phi(a,b,c,d)=(a,ab,c,d)` is birational, but on the embedded plane `j(s,t)=(0,s,s^4,t)` it becomes `(0,0,s^4,t)=i(s^4,t)`, of restriction degree 4. The relevant ambient fibers at `a=0,ab=0` contain a free `b`, so the every-fiber hypothesis deliberately fails. This confirms the distinction between generic ambient degree and actual image-closure degree.

Finally, a projection identity `h=pi j_m` gives `K subset C(Z_m)`, the reverse of the containment required by the field theorem. It is therefore correctly excluded. No numerical `2^a3^b` theorem, solvable-monodromy inference, unrestricted high-degree source, degree-at-least-four step, arbitrary projection, or whole-JC2 conclusion follows.

Applying the promoted every-fiber bound stepwise to `G`, identity stabilizations, and polynomial conjugations closes only the named full-factorization iteration escape. Long's four-variable instance remains conditional on its previously accepted explicit polynomial source-coordinate factorization. No blocker or additional scope correction was found.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4592`.
- Body SHA-256:
  `d2ff987885287e70f96c3c1a1212caa055c77d101d517d4dea3902b3637c556f`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
