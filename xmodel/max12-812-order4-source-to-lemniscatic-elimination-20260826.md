# `(8,12)` exact order four: source-to-lemniscatic elimination

Date: 2026-08-26

Status: **EXACT PRODUCER THEOREM; PROVISIONAL UNTIL THE REGISTERED HOSTILE
REVIEW CONFIRMS THE COMPOSITION.**  The two AWS V3 prime-lift replays and the
independent V2 `a6` control have closed with fail-closed PASS endpoints.  This
note is the first artifact to compose those endpoints with the already
confirmed genus-one target theorem.

## 0. Theorem and scope

Let `L` be a characteristic-zero constant field, enlarged harmlessly for
geometric questions, and let `C` be the smooth projective normalization of
an exact-order-four Kummer source

```text
u^4=h(x),                 C/<deck mu_4> = P1_x.
```

Let `f in L(C)[z]` be monic depressed of degree eight and let
`g=F_12(f)` be the ordinary Faber polynomial.  Suppose the coefficient-
infinity tail has nonzero order-four load:

```text
(r_1,...,r_7)=(0,0,0,mu_4,0,0,R_7),
mu_4 != 0,                 8 dR_7/dx=j/u != 0.        (0.1)
```

Then no such source exists.

Combined with the independently confirmed Shioda--Hall divisor-19 theorem
for `mu_4=0`, this eliminates the complete exact-order-four
coefficient-infinity leaf for `(8,12)`, for every source degree `U`.

This is a necessary-source theorem.  It does **not** eliminate the
exact-order-two or order-one leaves, prove `(8,12)` empty, prove maximum
twelve, construct a counterexample, or prove JC2.

## 1. Exact source and normalized coefficient curve

The source-typed V2 client and its independent review are

```text
c1aa88b40104205f327240dd33a4e674983577ce6d9dfafc82b8547959312621
  xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-client-v2-20260825.md
252bbd07d29084952453b45546cff7e0d8ddda7a72576311d1f982ee01a66200
  xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-review-grok-v2-20260825.md.
```

They consume the corrected coefficient-infinity source audit and confirmed
terminal differential theorem at SHAs

```text
092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e
1cd824c9553a800ddf390bc972a29656e1286699406b1ca46bbc94bdfe18084b
db67f16dbda759b8481fcbf32491fe77c37483bb5fe70830eb42e95541767251.
```

Those artifacts prove that (0.1) is the complete loaded order-four target:
there are no omitted lower Faber loads.  The Faber weight action has
`wt(r_4)=16`, so after a finite constant extension and a nonzero weighted
scaling every `mu_4!=0` source is represented by `r_4=1`.  Its normalized
coefficient image lies in

```text
J=((r_1,r_2,r_3,r_4-1,r_5,r_6):r_7^infinity)
    subset Q[a_0,...,a_6],                            (1.1)
```

and `r_7` is nonzero and nonconstant.  The compiler independently derives
the same ideal from the coefficients of
`g^2-f^3+2f` in degrees six through eleven and checks the two presentations
against one another before the saturated basis is emitted.  No `(9,12)`
formula is imported.

## 2. Evidence custody, V2 near-pass, and V3 repair

The 71-element characteristic-zero seed is not a guessed prime or an
overrestrictive component.  Its frozen Singular source and stdout have
SHAs

```text
d2fedf6c9b2b09787c7e45a00f1626ac10f7d4c68c44030102758021a55c9496
  coefficient_curve_v2_modsatQ.sing
5e780dcf82d2a3ac17c3ae7957c819c8b7b8a1a1de6231f88e4f808a2b348c45
  max12_812_order4_mu4_nonzero_curve_v2_modsatQ_..._box02.stdout.
```

The exact source constructs the six-generator `Itail` in (1.1), checks its
independent shifted-polynomial presentation, and then executes

```text
list SS=modSat(Itail,ideal(r7));
ideal J=modStd(SS[1]);
```

before printing `SOURCE_EQUIVALENCE=PASS`, `SAT_IS_UNIT=0`, `SAT_DIM=1`,
`SAT_BASIS_SIZE=71`, and the complete basis between unique
`SAT_BASIS_BEGIN/END` delimiters.  The V2 compiler has SHA
`7ede3c5a34bf4d2a1592dedaa268307bd464c8dd5b22936f684999aefbb1a5bd`.
It refuses any mismatch of either frozen input SHA or any missing/nonunique
sentinel or delimiter, requires exactly 71 nonempty one-line basis elements,
and copies those exact bytes into `JQ`.  Thus `JQ` is the frozen exact
saturation `J`, not merely an ideal for which the unsaturated generators
reduce to zero.  The later nonzero scalar normalization changes no generated
ideal; V2/V3 also check the raw and normalized ideals in both directions.
The printed `SOURCE_TO_SEEDED_Q=1` is only a redundant source-containment
control and is not the equality argument.

The immutable V1 seeded clients are non-decisive: their monicity preflight
printed zero and an invalid `exit(81)` let Singular continue.  V2 repaired
that defect by scalar-normalizing the exact characteristic-zero standard
basis and using fail-closed `quit` branches.  Its frozen input/results are

```text
ff7381f6ac2b78445a3ed9debab6a1116568984defe98a9d0ce77f414308fcbf
  cases/max12_812_order4_seeded_projection_v2_20260826/FREEZE.sha256
1c1c937c8ec58c13cdfcabef4d168490d60b00341622c5e8e650fb906b7fc47a
  cases/max12_812_order4_seeded_projection_v2_20260826/RESULTS.sha256.
```

V2's prime endpoint is nevertheless only a near-pass: it standardizes the
coefficientwise reduction before comparing it with the native special
fibre, and did not explicitly prove that the raw coefficientwise reduction
of the monic basis was itself a standard basis.  V2 stdout also contains
benign lines

```text
// ** GQ is no standard basis
```

because elementwise scalar normalization clears Singular's internal
standard-basis flag.  Nonzero scalar multiplication preserves a standard
basis mathematically, but V2 did not reset that software attribute.  Neither
issue is hidden or promoted here.

V3 consumes the exact V2 prime input of SHA
`28721c66a0838487dc9490f1a33cd4b3d95324ffe80aaef9dcedabed3c10645a`.
It explicitly marks the characteristic-zero normalized list as standard
only after its nonzero scalar normalization.  In characteristic `p=32003`,
write `Gbar_raw` for the coefficientwise reduction and
`Gbar=std(Gbar_raw)`.  V3 requires two-sided ideal equality

```text
<lt(Gbar_raw)> = <lt(Gbar)>                            (2.1)
```

after standardizing the two monomial ideals.  Since `Gbar_raw` and `Gbar`
generate the same polynomial ideal by construction, (2.1) is exactly the
standard-basis criterion for `Gbar_raw`.  Only after (2.1) passes does V3
set its `isSB` attribute and require every member of `Gbar` to reduce to
zero against it.

The V3 source and dual results are frozen at

```text
07c7582663a7f6569aaf0f8101f0b32ca631f711df33be3a03572d08996debe6
  cases/max12_812_order4_seeded_projection_v3_rawgb_20260826/FREEZE.sha256
ee921a6f3d63d1963a99ef564847d34f1975acd6f21604eb105d5136fafcb64b
  cases/max12_812_order4_seeded_projection_v3_rawgb_20260826/RESULTS.sha256.
```

Both independent AWS hosts consumed the identical source archive
`22337e0323a95ebe262a9f21d0c48aadfc1560d8a333b7a7db5a02e253dc8d8c`
and emitted the identical V3 Singular input
`97fc8dbec766dea32afa0c1857447341b81fc7ce87a0bec72764b055510e05a7`.
The Box03 and r6d stdout SHAs are respectively

```text
9d59776d2682d83ce873583ecae07c24059483fdc06d3f43dd542b169182cc34
77027e08c71352afa848ec1f3966d197919c1c623b8d727999516e327bc6b805.
```

They differ only in host/job paths printed by Singular.  Both give

```text
SEEDED_Q_MONIC=1
SEEDED_Q_DIM=1
SEEDED_Q_SIZE=71
SEEDED_Q_A6_NONZERO=1
QRED_RAW_LM_TO_STD=1
QRED_STD_LM_TO_RAW=1
QRED_RAW_IS_GB=1
QRED_CERTIFIED_REDUCES_STD=1
QRED_TO_NATIVE=1
NATIVE_TO_QRED=1
QRED_LM_TO_NATIVE=1
NATIVE_LM_TO_QRED=1
MINASS_COUNT=1
JP_TO_MINASS=1
MINASS_TO_JP=1
SPECIAL_FIBRE_PRIME=1
PLANE_SIZE=1
PLANE_FACTOR_COUNT=1
SEEDED_PROJECTION_CERTIFICATE=PASS.
```

The outer validation file has identical SHA
`4eae0cd3a340921c88891e12040f966cb65e7f0883121a1bb45cd77a15a61c0f`
on both hosts and records `engine_rc=0`, unique required sentinels, zero
`GQ is no standard basis` warnings, and `validator=PASS`.  There is no
separate `<tag>.rc` file: the evidence-grade wrapper records the actual
`rc=0` in each `<tag>.meta`, and the outer validation separately records
`engine_rc=0`.  Box03 used 192672 KiB RSS in 1:58.94, r6d used 192084 KiB
in 1:57.30, and both report zero swaps and process exit status zero.

The V2 `a6` lane independently prints two-sided equality
`J:a6^infinity=J`.  Its stdout SHA is
`cd97e2c95cf8e32d498367179b94600da08839c601f3e57329379eed6987d884`.
The proof below does not need to trust reductions against its unflagged
scaled basis: V3 proves `J` prime and `a6 notin J`, which implies the same
saturation equality formally.  The V2 lane is retained as a direct control.

## 3. Prime lift and one-dimensionality over `Q`

Let `V=Z_(32003)` and let `G` be the V3 monic basis.  Successful
coefficientwise reduction with no Singular diagnostic is the denominator
check; monicity ensures every leading term survives.  Section 2 proves that
the raw reduction is a standard basis, not merely that its standardized
ideal agrees with another ideal.  Its ideal and initial ideal agree two ways
with the native `r_7`-saturated special fibre.  The latter equals its unique
minimal prime two ways.  Thus the special-fibre quotient is a domain.

Division by the monic basis makes the standard monomials a free `V`-basis.
If two nonzero generic-fibre normal forms had zero product, divide their
coefficients by their minimum `32003`-adic valuations.  Torsion-freeness
then gives two nonzero special-fibre reductions with zero product, contrary
to the special domain.  Hence

```text
A_Q=Q[a_0,...,a_6]/J
```

is a domain.  The direct exact-`Q` sentinel `SEEDED_Q_DIM=1` proves
`trdeg_Q Frac(A_Q)=1`.  Also `SEEDED_Q_A6_NONZERO=1` proves `a6 notin J`.
Because `J` is prime,

```text
J:a6^infinity=J.                                      (3.1)
```

After the flat constant extension to `C`, multiplication by `a6` remains
injective.  Therefore no geometric coefficient component is contained in
the omitted chart `a6=0`; isolated points with `a6=0` are restored by
proper completion.

## 4. The residual image is nonconstant on every geometric component

Put

```text
s=a5,      t=a6,      q=s^2/t^3,      y=t^2,
v=y^4=t^8.                                              (4.1)
```

The exact special-fibre contraction to `F_32003[s,t]` is one nonzero
irreducible equation, so its image is one-dimensional.  The monic model is
flat.  If both `s` and `t` were algebraic on the generic fibre, primitive
univariate relations could be cleared into `V[s]` and `V[t]`; their
nonzero reductions would make the special `(s,t)` image zero-dimensional,
a contradiction.  Hence at least one of `s,t` is nonconstant.  If both
`q` and `v` were constant, then `t^8=v` and `s^2=q t^3` would make both
`s,t` algebraic over the constant field.  Therefore `(q,v)`, and hence
`(q,y)`, is nonconstant.

The exact characteristic-zero plane-membership certificate of SHA
`9b0e08c2d826286364f07f6a6fba9560e23ca8ea4fcba15cbbcf373152badbe3`
proves, after clearing a power of the nonzero `t`, that

```text
P(q,v)=0                                               (4.2)
```

in `Frac(A_Q)`.  The already confirmed residual theorem proves that
`P(q,v)` is geometrically irreducible.  Because both its function field and
`Frac(A_Q)` have transcendence degree one and (4.1) is nonconstant, (4.2)
induces a finite extension

```text
Q(P(q,v)=0)  -->  Frac(A_Q).                           (4.3)
```

After base change to `C`, every field factor of the finite generic algebra
lies over the generic point of the geometrically integral residual plane.
Thus every geometric coefficient component dominates that plane.  Adding
the actual function `y=t^2`, every component maps nonconstantly to the
geometrically irreducible normalization

```text
Y: P(q,y^4)=0.                                         (4.4)
```

This is a componentwise statement from the finite function-field extension;
it is not inferred from quotient irreducibility alone.

## 5. Source descent and the genus-one contradiction

The confirmed target theorem, its review, and its nonmutating tangent
erratum have SHAs

```text
cd6c37c145e325a48dbf382453bde4c727b98a576897d10a1f9b3752ebdd1756
59fb338533ff47a25d00893684caa3076bb7bb7bc2a43ab788cabbc0eb932c6a
26a083fcfa805a52fdb295ceaaf94ae7497047d8545a2323a48a688ac39e2300.
```

They prove that the complete normalization of (4.4) is a geometrically
irreducible genus-one curve.  More explicitly, the independently confirmed
lemniscatic corollary and review at SHAs

```text
97ace425a5fc0dc03aa12edb2e09f29e3143566b0939d3ce833a3872ee32a07f
09684e0be2784758b97f7e82e19ae9c8a33c7375d637417740d8f21b7d686425
```

identify it over `C` with

```text
Z_E^2=X_E^3-16X_E,              j=1728,               (5.1)
```

and exhibit a nonzero regular differential.

A genuine source gives a nonconstant coefficient map from `C`: otherwise
the polynomial coefficient `r_7` would be constant, contrary to
`8dR_7/dx=j/u!=0`.  Its image is therefore dense in one geometric
coefficient component.  Section 4 makes the induced map to `Y` nonconstant.

Under the reviewed order-four deck action,

```text
a_i |-> zeta^(-i) a_i.
```

Consequently `q=a5^2/a6^3` and `y=a6^2` are invariant under the deck
`mu_4`.  The map `C --> Y` descends to a nonconstant rational map

```text
P1_x=C/<deck mu_4>  -->>  Y.
```

Properness extends it across every pole.  But a nonconstant characteristic-
zero morphism from `P1` to a genus-one curve is impossible: equivalently,
pullback of the nonzero differential from (5.1) would be a nonzero regular
differential on `P1`, while `H^0(P1,Omega^1)=0`.  This contradiction proves
the theorem of Section 0 for `mu_4!=0`.

## 6. Completion of exact order four and firewall

The complementary theorem and its independent confirmed review are

```text
a5d40fd81838118735c4c2ad379bbac0a1e7d70a66a4a419eff078e8099d7b03
  xmodel/max12-812-order4-mu4zero-davenport-stothers-elimination-20260825.md
a40827f99f63292d8cceb95cc491493bec1a618424f0fd8043236279d5aa8904
  xmodel/max12-812-order4-mu4zero-davenport-stothers-review-grok-20260825.md.
```

They eliminate the entire exact-order-four `mu_4=0` stratum for all `U`
by the unique Hall/Shioda order-four Davenport--Stothers normal form and the
divisor-19 contradiction.  Sections 1--5 eliminate `mu_4!=0`.  Since the
source audit proves these are the only order-four load alternatives, the
complete exact-order-four coefficient-infinity leaf is empty.

This conclusion is still **producer-tier pending hostile review of this
composition**.  In particular, no computational PASS token alone is being
used as a theorem, and no result from V1 is consumed.
