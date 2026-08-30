# Binding integration: moving-double-section nonnormal quadratic closure

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen integration basis: `4ad2fe75f074726bf6d64ade07da17ea1ea02771`  
Lifecycle: **PROMOTED, EXACT IN THE FIXED QUADRATIC PRESENTATION SCOPE**

## 0. Verdict, custody, and charged scope

This integration binds the exact producer

```text
9557f2c1396daba190927e6a220774362a02068b4197103357d30e8cfc78b75e
  xmodel/bd-a2-moving-double-section-normalization-conductor-sol56-20260830.md
  body 18927 / dfd050e37b97b119f6170259f7417ac69e8109723abec4abe8260e3c7a33be57
  manifest 6675be2beab682f5da3230db4631c5859ce76018ce1e73b21dea62eedcbc408a
```

to the independent GPT-5.5 xhigh hostile review

```text
afa01a4e9c635db3762bab2e62f05ff7d3880c2ae53b766114dfed94d158c715
  xmodel/bd-a2-moving-double-section-normalization-conductor-hostile-review-gpt55-20260830.md
  verdict CONFIRM_WITH_CORRECTIONS
```

The producer was transactionally sealed on authorship basis
`dca72076aa1615b0b1286fd4428a1acac7b65963`, first committed at
`f43ee99da2bc9f831d94e403dcd90622e87e8756`, and reviewed on exactly that
publication basis.  The review receipt was root-hash-checked and committed at
the present integration basis.  The older authorship basis is a dependency
snapshot, not a claim that the final file existed there.

The result charges the promoted proper-block/first-leg package
`ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778`,
the reviewed nonnormal quadratic reduction bound by integration
`45685cce7fa934a9adfd45e96a02410a18559314b20a132ba4dec2c1a7e0ac6d`,
and, for the independent boundary proof, the rational-forest integration
`6a8558e42a67f1ec5c8bcf12321b6e6805b30a570eba17862c6e7e24cd631b08`.
The hostile reviewer found no mathematical gap.  Its two-chart, conductor,
and open-boundary corrections are binding below.

## 1. Promoted closure theorem

Assume the promoted proper cubic intermediate-block first leg of a
hypothetical noninvertible plane Keller map, and choose a global trace-zero
Miranda basis whose four coefficients have exact maximum degree two.  Let
`X` be its integral projective incidence hypersurface of class `2A+3B` in
`P2 times P1`.

The prior nonnormal reduction proves that `X_aff` is normal and that every
projectively nonnormal case has exactly

```text
F=Q^2 L+T Q S+T^2 R,
C={T=Q=0},        [C]=(1,1),
D_0={T=L=0},      [D_0]=(0,1),
H=2C+D_0.                                             (1.1)
```

Here `Q` is irreducible bilinear and `L,S,R` are binary forms in the fibre
variables of degrees one, two, and three.  This remaining form is impossible.
More precisely, if `nu:Xnu->X` is the normalization, then its conductor over
`C` is a smooth connected genus-one double cover `pi_E:E->C`, and

```text
pi_(E*)O_E=O_C direct-sum O_C(-2),
nu_*O_Xnu/O_X=O_C(-2),
K_Xnu+E=nu^*K_X,
h^1(Xnu,O_Xnu)=1,       h^2(Xnu,O_Xnu)=0.             (1.2)
```

Every resolution of `Xnu` consequently has irregularity at least one.  The
dominant rational `A2` first leg instead yields a generically finite dominant
map from a projective rational surface after resolving indeterminacy, so
pullback of holomorphic one-forms forces irregularity zero.  This
contradiction closes the entire **nonnormal fixed-quadratic-presentation
stratum**.

## 2. Exact transverse quadratic and squarefree conductor cover

Both projections from the irreducible `(1,1)` curve `C` are isomorphisms.
Using a fibre coordinate `z` along `C`, `(T,Q)` are genuine normal
coordinates.  Exact bidegrees, not a tangent-cone approximation, give

```text
F=ell(z)Q^2+s(z)TQ+r(z)T^2,
ell in H^0(O_C(1)), s in H^0(O_C(2)), r in H^0(O_C(3)). (2.1)
```

The three coefficients never vanish together.  At the unique zero of `L`,
simultaneous vanishing of `S` and `R` would make both divisible by `L`, hence
would factor the primitive projective equation, contrary to the charged
integrality of `X`.

Set

```text
delta_C=s^2-4 ell r in H^0(C,O_C(4)).                 (2.2)
```

At the generic point of `C`, zero discriminant makes (2.1) nonreduced and a
nonzero square discriminant splits it.  Either contradicts the domain local
ring, so `delta_C` is nonzero and nonsquare in `C(C)`.

It is in fact squarefree.  A multiple zero cannot lie over `ell=0`: `ell`
has a simple zero; if `s` is nonzero then `delta_C` is nonzero there, while if
`s=0`, the no-common-zero result gives `r!=0` and (2.2) has a simple zero.
Where `ell` is a unit, the blowup chart `Q=Tw` has exact strict equation

```text
G(z,w)=ell(z)w^2+s(z)w+r(z)=0,                       (2.3)
```

independent of the radial coordinate `T`.  At a double root
`w_0=-s/(2ell)`,

```text
delta_C'(z_0)=-4 ell(z_0) G_z(z_0,w_0).              (2.4)
```

Thus a multiple root gives `Sing(G) times A1_T`, a codimension-one singular
locus.  Its points with `T!=0` are nonexceptional and map isomorphically into
the already normal affine incidence.  This is impossible.  Therefore
`delta_C` has four distinct simple zeros and `E` is smooth, connected, and
genus one.

## 3. The blowup is the finite normalization

Blow up the smooth complete-intersection curve `C=(T,Q)` in the ambient
threefold.  The two strict-transform charts are

```text
Q=Tw:       w^2L+wS+R=0,
T=Q tau:    L+tau S+tau^2R=0.                        (3.1)
```

Over `p in C`, the exceptional fibre is the length-two zero scheme

```text
ell(p)q^2+s(p)qt+r(p)t^2=0 in P1_[q:t].              (3.2)
```

No fibre is a whole `P1`, so the proper birational strict-transform map is
quasi-finite and hence finite.  The strict transform is a Cartier
hypersurface in a smooth threefold, so it is `S_2`; away from the exceptional
curve it is the charged normal locus `X-C`.

Along the exceptional curve, (2.3) is the smooth total double-cover curve
times the radial parameter.  The omitted chart is equally explicit: with
`z=ell` and after a unit rescaling, its equation is

```text
z+tau s(z)+tau^2 r(z)=0,                              (3.3)
```

whose `z` derivative is a unit at the exceptional point.  This covers the
ramified and unramified fibres over `C intersect D_0` and leaves no
codimension-one singularity along the residual section.  Branch fibres of
`E->C` are nonreduced as fibres, but the total curve and surface are smooth.
The strict transform is therefore `R_1` and `S_2`, hence normal, and is
exactly `Xnu`.

## 4. Exact conductor and irregularity

At every point of `C`, an invertible change of normal parameters makes one
quadratic coefficient a unit.  With `A=O_(C,p)`, the local inclusion is

```text
R=A[[t]] direct-sum A[[t]] t w
  subset S=A[[t]] direct-sum A[[t]] w,
a w^2+bw+c=0,             q=tw.                      (4.1)
```

The quotient is the free `A`-module `Aw`.  Both `t` and `q` annihilate it;
conversely an element `f(t)+g(t)q` annihilates `w` only if `f(0)=0`.
Therefore the full conductor downstairs is exactly `(T,Q)O_X`, not merely
generically, and upstairs it is `O_Xnu(-E)`.

The conductor pushout gives

```text
0 -> O_X -> nu_*O_Xnu direct-sum O_C -> pi_(E*)O_E -> 0. (4.2)
```

Trace splitting and the quartic branch divisor yield
`pi_(E*)O_E=O_C direct-sum O_C(-2)`, so the normalization quotient in (1.2)
follows.  The ambient codimension-two blowup formulas

```text
K_Bl=rho^*K_W+E_W,       Xnu=rho^*X-2E_W             (4.3)
```

give the canonical identity in (1.2) with coefficient one.

Finally, the hypersurface sequence for class `(2,3)` gives

```text
H^1(X,O_X)=H^2(X,O_X)=0                              (4.4)
```

because all cohomology of `O_P2(-2)` vanishes.  The long exact sequence of

```text
0 -> O_X -> nu_*O_Xnu -> O_C(-2) -> 0               (4.5)
```

then gives exactly the two cohomology values in (1.2).  Normality injects
`H^1(O_Xnu)` into `H^1` of every resolution.  Resolving the dominant rational
first-leg map from a projective rational source gives the contrary value
`q=0` in characteristic zero.

## 5. Independent rational-boundary contradiction

Let `U` be the smooth resolved first-leg target over `T!=0`, with any missed
affine branch or singular locus removed as in the charged first-leg theorem.
The curve `E` lies over `T=0`, so its strict transform is an actual component
of every SNC boundary of `U`; blowing up boundary points does not change its
genus.  The promoted rational-forest theorem forbids a positive-genus
boundary component.  Since `E` is smooth of genus one, this independently
excludes (1.1).

The residual strict transform `D` meets `E` at exactly one physical point.
At the unique zero `p_0` of `ell`, the exceptional equation is

```text
T(s(p_0)Q+r(p_0)T)=0.                                (5.1)
```

The curve `D` approaches only `[Q:T]=[1:0]`.  If `s(p_0)!=0`, the conductor
cover is unramified but `D` meets only this one of its two fibre points.  If
`s(p_0)=0`, then `r(p_0)!=0` and `D` meets the unique ramification point.
Thus an unramified double-cover fibre is not miscounted as two attachments.

## 6. Degenerate quartics and scope firewall

The quartic threat map remains useful only as a curve-theoretic diagnostic.
Types `2+1+1` and `3+1` give nodal and cuspidal conductor curves, but their
first blowup is nonnormal along the affine radial line and is not the surface
normalization.  Split types `2+2` and `4` contradict integrality; `delta=0`
is generically nonreduced.  No arithmetic-genus shortcut or degenerate-row
surface normalization is promoted.

Combining this integration with the prior smooth closure leaves only the
**normal singular** exact-quadratic incidence stratum, now reduced separately
to the reviewed finite numerical/combinatorial `D9`-decorated ADE threat map
in its proper-intersection/no-common-carrier regimes.  The active local
Cartan enumeration is not charged here.

This theorem is existential in one fixed global trace-zero quadratic basis:
if such a basis gives a nonnormal projective incidence, it is excluded.  It
does not prove that an arbitrary cubic block admits a quadratic basis, that
infinity or smoothness is basis-invariant, or that higher-degree incidences
are covered.  Normal-singular effectivity, common-carrier/nonfinite strata,
basis coverage, polynomial maps, counterexamples, and JC2 remain separate.
No heavy computation, AWS result, formal arc, finite-prefix, or attainment
claim enters this integration.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10330`.
- Body SHA-256:
  `022bc15dfdb784d3761bd1fc575c335b4af1cb95613177f8eb07634fad4f44e5`.
- Frozen basis: `4ad2fe75f074726bf6d64ade07da17ea1ea02771`.
