# Minimal-resolution ramification arithmetic genus — independent hostile review

Reviewer invocation: MORINEFREVIEW0740, configured gpt-5.6-sol / ultra; actual hosted identity UNVERIFIED.
Completed UTC: 2026-11-07T07:46:28.448380+00:00
Verdict: **CONFIRMED_AT_NAMED_FOUNDATIONS**
Evidence/lifecycle scope: MANUAL / independent review of the frozen ROOT proposal. Novelty unassessed; no JC2 conclusion.

## Exact claim reviewed

Let `g:Y -> P^2` be generically finite of degree `N>1`, with `Y` smooth irreducible projective over `C`. Let `U=A^2` be a whole open subset on which `g` is etale and whose image misses a target line `L`. Assume no smooth rational `(-1)`-curve is contracted by `g`. For `H=g^*L` and the full determinant divisor `R=div(det dg)`, including contracted components and all multiplicities, the claim is

    p_a(R) >= 1.

I also reviewed its application when `g=h o q`, where `h:X -> P^2` is the finite projective normalization in the function field of a hypothetical degree-`N` plane Keller map and `q:Y -> X` is the minimal resolution.

## Input custody and reading

- Startup ACK succeeded at `2026-11-07T07:38:39.762449+00:00` and remained a separate mode-0444 output. Startup observations do not establish model identity or mathematics.
- The copied reader SHA-256 was exactly `47e3aea5fd494d0966aad35312aa3eea689a000b05289bd03646b9e5d577fbe4`. Preflight verified all 17 packet members and the one declared PROPOSAL seal at basis `e2fca4ba314e0abfac3768fcc3f13241871dace9`.
- Whole reading was completed through returned `next_start` values: non-STATE `1743/3500` LF and STATE `83/140` LF. The non-STATE count includes historical `82/120` LF (`PROPOSAL` 72 and `FINITE_INTERFACE` 10).
- Reader help used 29 LF solely to obtain command syntax. Repeated body windows: 0. Report-body previews: 0. No command-format correction or retry was needed.
- `PROJECTIVE-RAMIFICATION-GENUS-1` is used only as the supplied MANUAL / PROVISIONAL / CONFIRMED_AT_NAMED_FOUNDATIONS statement. I did not reopen its proof.

## Reconstruction and hostile checks

### 1. Divisor and cone reduction

Because `g` is surjective and generically finite, `H` is nef, `H^2=N>0`, and no ampleness is assumed. The determinant of the differential is a nonzero section of `omega_Y tensor g^*omega_(P^2)^(-1)`, hence

    R ~ K_Y + 3H.

It is effective and supported in `Y-U`. Since `U` is dense `A^2`, `Y` is rational. Put `Q=K_Y+R=2K_Y+3H`. Adjunction for the possibly nonreduced Cartier divisor `R` gives

    Q.R = 2p_a(R)-2.

If `p_a(R)<=0`, then `Q.R<0`, so `Q` is not nef. On the `K_Y`-nonnegative part of the curve cone, `Q` is nonnegative because `H` is nef. The surface cone theorem therefore supplies a `K_Y`-negative extremal ray on which `Q` is negative. This use of the cone theorem is valid for nef-and-big `H`; it does not smuggle in ampleness.

### 2. Birational and point extremal contractions

A birational extremal contraction has exceptional curve `E` a smooth rational `(-1)`-curve. If `H.E=0`, then the morphism `g` contracts `E`, contrary to the hypothesis. Otherwise `H.E` is a positive integer, and

    Q.E = -2 + 3H.E >= 1,

contradicting negativity of the selected ray.

If the contraction is to a point, rationality and Picard rank one give `Y=P^2`. Writing `H=m[ell]`, negativity of `Q=(3m-6)[ell]` forces `m=1`, hence `N=H^2=1`, again impossible.

### 3. The one-ray fibration and its fibres

The remaining contraction is `pi:Y -> B` with connected one-dimensional fibres. Rationality gives `B=P^1`. For a general fibre `F`, `F^2=0` and `K_Y.F=-2`. If `H.F=0`, Hodge index for `H^2>0` would force the nonzero numerical class `F` to have negative square. Thus `H.F` is a positive integer. From

    Q.F = -4 + 3H.F < 0

one gets `H.F=1`, and hence `R.F=1`.

Every curve contracted by `pi` is in the same extremal numerical ray. Thus every prime component `C` of a fibre is numerically a positive multiple of `F` and has `C^2=0`. If a connected fibre were reducible, a component meeting another component would satisfy both `C.F_b=0` and `C.F_b>0`, a contradiction. If `F_b=mC`, then `1=H.F_b=m(H.C)` forces `m=1`. Flatness over the smooth base preserves arithmetic genus zero; an integral reduced fibre of arithmetic genus zero is smooth `P^1`. Therefore every fibre is `P^1`, and the standard ruled-surface classification gives `Y=F_n`.

### 4. Ample ruled branch

With the standard basis `S^2=-n`, `S.F=1`, write

    H = S + bF,    b>=n,    N=H^2=2b-n>1.

If `b>n`, then `H` is ample. A positive-dimensional fibre of `g` would contain a curve of `H`-degree zero, so none exists. Proper quasi-finiteness makes `g` finite. The accepted `PROJECTIVE-RAMIFICATION-GENUS-1` interface then contradicts `p_a(R)<=0`. Its hypotheses are exactly met here; this is the sole invocation of that interface.

### 5. Nonample endpoint and ramification multiplicities

It remains that `b=n`. Then `N=n>=2`, `H.S=0`, and `g` contracts `S`. At the generic point of `S`, `dg` has rank at most one, so `S` occurs in `R` with positive coefficient. Since `R.F=1` and `S.F=1`, that coefficient is exactly one and there is no other horizontal ramification prime. The canonical formula on `F_n` yields

    R = S + sum_j r_j F_j,    sum_j r_j = 2n-2 = 2N-2,

where the `F_j` are distinct fibres and `r_j>0`.

Each `F_j` is noncontracted because `H.F_j=1`. Factor `g` through the finite normalization of `P^2` in `C(Y)`. The birational factor is an isomorphism at the generic point of any noncontracted prime, since the normalization is normal. Consequently `r_j` is the different exponent for the corresponding finite extension of DVRs. In characteristic zero the extension is tame at codimension one, so `r_j=e_j-1`. The fundamental inequality gives `e_j f_j<=N`, hence

    r_j <= N-1.

No residue-degree-one assumption is used. Since the positive coefficients sum to `2(N-1)`, at least two distinct vertical fibres occur. Together with `S`, the support of `R` contains at least three distinct boundary curves.

### 6. Whole-`A^2` boundary basis

For the open immersion `U=A^2 subset Y`, divisor localization gives

    O(Y)^* -> O(U)^* -> direct_sum_(Z subset Y-U) Z[Z] -> Cl(Y) -> Cl(U) -> 0.

Both unit groups are `C^*`, and `Cl(U)=0`. Thus the free group on the codimension-one boundary primes maps isomorphically to `Pic(Y)`. For `Y=F_n`, `Pic(Y)=Z^2`, so there are exactly two boundary curves. This contradicts the three distinct ramification boundary curves above. The nonample endpoint is therefore excluded, completing `p_a(R)>=1`.

## Actual finite-normalization application

Let `F=(F_1,F_2):A^2 -> A^2` be a hypothetical Keller map of generic degree `N>1`. Set `A=C[F_1,F_2]`, `B=C[x,y]`, `K=Frac(B)`, and let `A'` be the integral closure of `A` in `K`. Any element of `A'` is integral over `B` as well; since `B` is integrally closed, `A' subset B`. Hence there is a birational morphism

    Spec(B) -> Spec(A').

It is quasi-finite because its composite with the finite map `Spec(A')->Spec(A)` is the etale, hence quasi-finite, Keller morphism. Zariski Main for the normal target makes it an open immersion. Normalizing projective `P^2` in `K` therefore gives a finite degree-`N` morphism `h:X->P^2` containing the whole source `U=A^2` as this open; no equality with the whole inverse image of the affine target is asserted.

The minimal resolution `q:Y->X` is projective and is an isomorphism over the smooth open `U`. Thus `g=h o q` is etale on `U` and its image there misses the line at infinity. Since `h` is finite, a curve is contracted by `g` exactly when it is `q`-exceptional. The minimal resolution has no exceptional smooth rational `(-1)`-curve. All hypotheses of the reviewed theorem therefore apply without assuming that `X` is smooth or Q-Gorenstein, that its singularities are rational, that `g` is finite, or that `H` is ample.

## Boundary-blowup sensitivity

For the blowup `beta:Y'->Y` of any boundary point, with exceptional curve `E` and `g'=g o beta`,

    K_(Y')=beta^*K_Y+E,    R_(g')=beta^*R_g+E.

Using `E^2=-1` and `beta^*D.E=0`, adjunction gives

    p_a(R_(g')) = p_a(R_g)-1.

Thus an arbitrary boundary blowup can lower the arithmetic genus. Its new `E` is a contracted `(-1)`-curve, exactly violating the relative-minimality hypothesis. The theorem cannot be transferred to an arbitrary log/SNC resolution.

## Verdict and limitations

**CONFIRMED_AT_NAMED_FOUNDATIONS.** The proposed proof is internally valid at the stated imports and accepted finite-interface scope. The checks do not turn arithmetic genus into geometric genus and do not imply reduced ramification, finiteness or surjectivity of the original affine map, existence of a Keller counterexample, novelty, or JC2.

No web/source/history/repository search, CAS, secondary model, control family, degree farm, shared-document/Git change, protected-tree access, or model retry was used. Named classical imports were checked for applicability here but not source-audited. The accepted finite theorem was not re-audited.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9049`.
- Body SHA-256:
  `a05af6c1db53b8dc4cebb6f31ed179ec80cee4589e5af6dd39422f0391061460`.
- Frozen basis: `c9f508a77890db2a70597826a51bc9a34ea20da7`.
