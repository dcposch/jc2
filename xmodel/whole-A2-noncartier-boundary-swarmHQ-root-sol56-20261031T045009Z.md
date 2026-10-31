# A whole affine-plane chart does not force its omitted line to be Cartier

Producer: swarmHQ ROOT (campaign-configured gpt-6-astra; hosted identity unverified).
Independent hostile reviewer: swarmHQ (configured gpt-5.6-sol; hosted identity unverified).
Date: 2026-10-31T04:51:32.371937+00:00
Basis: d873bee2f519f5f2dec33f259c0dbc59c45ae011
Evidence tier: MANUAL, relative to the named standard foundations below.
Lifecycle: PROVISIONAL. Independent review PASS on the fixed example.

## Statement and scope

Let B=C[x,y,z]/(xy-z^2(z-1)), X=Spec B, and E=V(x,z). The normal affine surface X is singular only at (0,0,0). Its complement X-E is the WHOLE affine plane under

    (u,v) -> (x,y,z)=(u,v(1+uv)^2,1+uv).

The omitted E is a scheme-smooth affine line, non-Cartier of local index2 at the singularity, although Cl(X)=Z[E]. The projection (x+y,z) is finite flat of degree2 onto a smooth plane. These combined hypotheses therefore do not force ambient smoothness or Cartierness of E.

The projection restricted to X-E has Jacobian u-v(1+uv)^2 and critical points inside that affine-plane chart. It is NOT Keller. This is not a JC2 counterexample and does not refute a theorem using actual etaleness on the whole source.

## Dependencies and prior work

The [earlier smooth-ramification-support example](smooth-ramification-singular-source-swarmHQ-root-sol56-20261031T034712Z.md) has complement A1 times G_m. This fixed example addresses a different coarse hypothesis: it has a whole A2 chart and a free boundary-generated class group, but its ramification is not confined to the omitted line. Neither example settles smoothness of the actual Keller normalization. Historical priority and novelty are unassessed; no family or repair toward a Keller map is proposed.

## Exact reviewed argument

The following23LF are byte-identical to lines15-37 of the [sealed independent review](../box/whole-A2-noncartier-boundary-swarmHQ-20261031T045009Z/independent-review.md): 3140bytes, SHA256 `3565c657fcac89c1196eff11e754b6adfbac95d9be811b03fece2f858182e51f`. No mathematical change was made to this proof during integration.

Write `F=xy-z^2(z-1)` and `E=V(x,z)`.

1. For `w=1+uv`, substitution `(x,y,z)=(u,vw^2,w)` gives `xy=z^2(z-1)`. On `D(x)`, `(u,v)=(x,(z-1)/x)`; on `D(z)`, `(u,v)=(x,y/z^2)`. The relation makes the formulas agree and makes each composition the identity. Since `X-E=D(x) union D(z)` and `u=0` forces `z=1`, the image is exactly the whole `A2`, with no missing locus.

2. Viewed over the UFD `C[x,z]`, `F` is primitive and linear in `y`, hence irreducible by Gauss's lemma. Thus `B` is a two-dimensional domain. Its gradient is `(y,x,-3z^2+2z)`; imposing the equation leaves only `p=(0,0,0)`. A hypersurface is Cohen-Macaulay (`S2`), and regularity away from this codimension-two point gives `R1`; Serre's criterion makes `B` normal. At `p`, `F` has no linear term, so the embedding dimension is three while the dimension is two: `p` is singular and unique.

3. `B/(x,z)=C[y]`, so `E` is scheme-smooth `A1`. In `B_p`, the classes of `x,z` are independent in `(x,z)/m(x,z)` because `m(x,z)` lies in `m^2` and `x,y,z` are independent in `m/m^2`. Nakayama therefore shows `(x,z)` is not principal, so the prime Weil divisor `E` is not Cartier at `p`.

4. Near `p`, `z-1` is a unit. At the height-one generic point of `E`, also `y` is a unit and `x=z^2(z-1)/y`; hence `z` is a uniformizer and `ord_E(x)=2`. No other height-one prime over `(x)` remains near `p`, so `div(x)=2E` locally. Together with non-Cartierness, this proves local Cartier index exactly two.

5. Globally the only height-one components of `V(x)` are `E` and `L=V(x,z-1)`. Their orders are respectively two and one, so `div_X(x)=2E+L`. The class-group localization sequence for the normal scheme gives `Z[E] -> Cl(X) -> Cl(X-E)=Cl(A2)=0`. If `nE=div(f)`, then `f` has zero divisor on `A2`; unique factorization, equivalently `O(A2)^*=C^*`, makes `f` constant, hence `n=0`. Therefore `Cl(X)=Z[E]` and `[L]=-2[E]`. Global infinite order is compatible with the order-two local class; global freeness does not imply local Cartierness.

6. With `s=x+y`, `t=z`, and `T=x`, substitution in both directions gives
`B = C[s,t,T]/(T^2-sT+t^2(t-1))`.
The polynomial is monic of degree two, so the target ring injects and `B` is free with basis `1,T`. Thus `h` is finite flat, dominant, and of degree two.

7. For this monogenic algebra,
`Omega_(B/C[s,t]) = (B/(2T-s)) dT`, so the entire relative non-etale support is exactly `V(2T-s)=V(x-y)`; there is no hidden second component. On the whole chart,
`h j(u,v)=(u+v(1+uv)^2,1+uv)` and
`det D(h j)=u-v(1+uv)^2=x-y`.
It vanishes at `(u,v)=(0,0)`, whose image `(0,0,1)` is a smooth point of `U`. Along the generic point of `E`, `x-y=-y` is a unit, so the map is generically etale there. These facts confirm both the complete support and its essential intersection with `U`.

Named standard foundations used are Gauss's lemma, the hypersurface Cohen-Macaulay and Jacobian criteria, Serre normality, Nakayama's lemma, height-one DVR divisor theory, the normal-scheme class-group localization sequence, factoriality and units of affine space, monic-quotient freeness, monogenic relative differentials, and finite-flat unramified/etale equivalence.

## Replay and negative controls

Desk-only: the inverse charts, local divisor orders, monic quadratic presentation and Jacobian calculation are explicit above. No CAS, numerical experiment or parameter sweep was used. [Original candidate, review, custody and checksums](../box/whole-A2-noncartier-boundary-swarmHQ-20261031T045009Z/README.md) retain exact sealed bytes. The critical point (u,v)=(0,0) inside U is the decisive negative control against a Keller interpretation.

## Limitations and next test

This closes only the coarse global-class-group/whole-chart shortcut. A valid actual-normalization argument must use further Keller-specific information, including etaleness on U; it cannot infer local Cartierness merely from a free global class group. No properness, surjectivity, degree-one or JC2 conclusion follows. No construction of a non-Keller family or repaired map is part of this result.

## OPENS RAISED

None. Existing actual-source finite-normalization gaps retain their scopes.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `d873bee2f519f5f2dec33f259c0dbc59c45ae011` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6460`.
- Body SHA-256:
  `0d85b2357c15e940f65e08d265b85ea6b00a4c45055aaf5b11390116cc337874`.
- Frozen basis: `d873bee2f519f5f2dec33f259c0dbc59c45ae011`.
