# TWIN-ORDER derive-or-OPEN: td12 U1 sibling

Date: 2026-08-29  
Producer: Sol 5.6 (Ultra), exact desk mathematics  
Frozen Git basis: `92ebe92ad5986a47f01af9ed901260595dfed869`  
Lifecycle: sealed producer disposition; different-model review required for
promotion

## 0. Verdict

```text
GAUSSIAN NON-TORSION:  PROVED (and history-duplicate of the 1224Z checks)
TD12 CLOSURE LAW:      OPEN -- no source-backed law reaches the ratio
SIBLING ROUTE KILL:    NOT OBTAINED
```

Put

```text
rho := B_+/B_- = (4+3i)/5.
```

Then, more strongly than merely `rho` not being a root of unity,

```text
rho^N notin mu_infinity                         (N in Z, N != 0).      (0.1)
```

Consequently any *proved* route holonomy of the form

```text
rho^N = zeta,       N != 0,       zeta in mu_infinity                 (0.2)
```

would kill the td12 `nu=17` U1 sibling cell immediately.  No currently
promoted source statement, route record, or formal recurrence supplies
(0.2).  The native `mu_17` deck fixes the orbit variable `t=eta^17` and
hence fixes `B_+` and `B_-` separately; common chart dilation fixes their
ratio; root-label swap sends `rho` to `rho^-1` and is compatible with every
value of `rho`.  Statement 3.9 transports coefficients down one edge at a
time but gives no equality between the two distinct northeast exits.

The exact missing premise is therefore not “a finite symmetry.”  It is a
**closed, source-backed coefficient-transport holonomy with nonzero net
`rho`-exponent**, returning to the same *labelled* gauge and producing
(0.2).  Instantiating such a holonomy first requires an occurring
`TD12LocalPairJet_S`/`PairRef_S`, its common completion and source jets, the
two child transports, and an endpoint identification or periodic return.
Those data are absent.  The correct current disposition is `OPEN`, with no
rigid-ordering, independence, occurrence, or exclusion corollary.

## 1. Custody and perimeter

Files read and hashes recomputed on the frozen basis:

```text
fd51a7f4f48b60659a16f64d5a2d4d17e2a3039e909d6c01fa25c6819d994516
  xmodel/ideation-20260829T1224Z-fable5.md
ae0b8956c77d448c0084d15ce7739d0130322c7a4d6e0f436bd1367b3b5924bf
  xmodel/ideation-20260829T1224Z-crosspoll-fable5.md
229da0125132a62757474be8814d0421e2186c4b82017b121700856287fb0266
  xmodel/ideation-20260829T1224Z-crosspoll-opus5.md
1e7fec45508e03015f06efcd33e68abdf295d0513b48867bf53c6f21b844c3d9
  xmodel/ideation-20260829T1224Z-crosspoll-grok46.md
805152bf2e68edad1a5d55b9fff7092e7a19f40171406050c9d9b50e994de608
  xmodel/ideation-20260829T1224Z-synthesis.md
9a9e948cafbea9fa448b84435c0ce004dec92903ba56984759353bf6a8d132bc
  xmodel/m2-td12-u1-sibling-t1-ratio-solve-r1-sol56-20260829.md
432a4152387cff943e220a6236912f2481a1ea3004d2c53ae95f14eb267f1ab0
  xmodel/m2-td12-u1-sibling-t1-ratio-solve-r1-hostile-review-grok46-20260829.md
70cf67b2241b1361e958e673b81d883f34a87be9e5fe3631a3a36c35646c3060
  xmodel/m2-td12-u1-sibling-exact-charge-r1-hostile-review-fable5-20260829.md
876d1717efdc69865cfae6c8b5d4ef983440a5f0997a9edf3cf13a2a5cc70aab
  xmodel/td12-bchild-v1-primary-fable5-hostile-disposition-r1-sol56-76c-20260829.md
e469e94dbf4393fe820345678c2582ca7f7a528695c25d065fb224b4f796cf61
  xmodel/m2-td8-equal-join-st39-coefficient-transport-primary-hostile-review-opus5-20260829.md
97ba497fffcf0a0ee5c9ee259acc325810659a9fd5376a47b38c87476fd2c5b4
  xmodel/td12-formal-cascade-rank-v1-coordinator-integration-sol56-20260829.md
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
  refs/sigray_full.pdf
```

The printed source was reread at Statements 3.9, 3.16--3.18,
Propositions 4.2 and 4.4, and Proposition/Statements 8.1--8.5 (printed
pp. 15--22 and 39--43).  The td8 transport theorem was used only as a
negative-control pattern: its route-specific twin law is not a td12 premise.

No web, AWS, CAS, heavy local computation, canonical edit, commit, or push
was used.  No exit price is asserted, so no `charge_basis` declaration is
applicable.

## 2. Exact arithmetic certificate

The reviewed T1 solve gives, up to the common nonzero scale `A` and swap,

```text
B_+ = (9+3i)A/8,       B_- = (9-3i)A/8,
rho = B_+/B_- = (4+3i)/5.
```

In the Gaussian integers,

```text
4+3i = i(2-i)^2,       5=(2+i)(2-i),
rho = i(2-i)/(2+i).
```

The Gaussian integers are a UFD, `2+i` and `2-i` are nonassociate primes
of norm five, and therefore

```text
v_(2+i)(rho) = -1,       v_(2-i)(rho) = +1.                    (2.1)
```

For every nonzero integer `N`, `v_(2+i)(rho^N)=-N != 0`.  A root of unity
is a unit at every finite place, so has valuation zero.  This proves (0.1).
It also proves the raw-root version: if `c_+^17=B_+` and
`c_-^17=B_-`, then `delta:=c_+/c_-` satisfies `delta^17=rho`; if `delta`
were torsion, so would `rho`.  Replacing either representative by a
`mu_17` multiple or swapping the two roots does not change this conclusion.

This is an arithmetic obstruction **only after** a separate theorem produces
a torsion equation.  Absolute value is useless here: `|rho|=1` despite
infinite multiplicative order.

## 3. What symmetry does and does not imply

The reduced shape at gauge `A=1` is

```text
p=(t-1)^2(t^2-(9/4)t+45/32),
q=eta(t-1)(t^2-(9/4)t+45/32).
```

Its two extra roots are unordered.  The coefficient equations are invariant
under their swap.  Formally over `Q(A)`, the quadratic splits over
`Q(A,i)` and the involution `i -> -i` exchanges `B_+` and `B_-`; at the
ratio level it sends `rho -> rho^-1`.  Applying this involution twice is the
identity for every nonzero `rho`.  Thus a finite-order exchange symmetry
does **not** imply `rho^2=1`, or any torsion relation.  It would do so only
if an additional labelled fixed-point/holonomy equation identified the
transported gauge with the original one multiplicatively.

This separates three actions that the draft idea conflated:

1. `eta -> epsilon eta`, `epsilon^17=1`, fixes `t` and every orbit value
   `A,B_+,B_-`; it cannot exchange distinct `t`-orbits.
2. Common `t`-dilation scales `(A,B_+,B_-)` together and fixes `rho`.
3. Abstract root-label swap or field conjugation sends `rho` to `rho^-1`
   and imposes no equation on `rho`.

The already reviewed statement that the two numerical conjugates are not
one native deck orbit follows simply from `B_+ != B_-`; non-torsion is not
needed for it.  Calling the directions “rigidly ordered” would therefore be
both unnecessary at deck scope and false at unordered/field-symmetry scope.

## 4. Source-backed closure audit

### 4.1 Printed root and edge laws

- Statement 3.18, under the campaign's repaired orbit reading, selects one
  continuing raw representative in each `mu_17` orbit.  It supplies no map
  from the `B_+` orbit to the `B_-` orbit and no periodicity equation.
- Statement 3.9(i)--(iii) transports multiplicity, the first nonzero Taylor
  coefficient, and the chart degree across **one named edge**.  Applied at
  `B_+` and `B_-`, it yields two evaluations of the same parent data, not an
  equality or proportionality between those evaluations.
- Statements 3.16--3.17 identify the two simple roots as two distinct
  direction-orbits.  Here both are northeast because `1*52<68`; the
  multiplicity-two arrival is the sole searrow continuation because
  `2*52>68`.  The two northeast exits are not a displayed pair of identical
  downstream `T_a^&` vertices that later reconverge.

No closed walk, return map, or nonzero power of `B_+/B_-` occurs in these
statements.

### 4.2 Global tower laws

Propositions 4.2 and 4.4 make an actual pair's Abhyankar tower and its prefix
constants global along compatible edges.  This can create cross-branch laws
only after both branches carry typed downstream vertex equations and some
shared initialization is consumed twice.  That is exactly what happened in
the td8 equal-join route: ratioing two identical child equations gave the
route-specific, reviewed identity

```text
(A_1/A_2)^2 = omega^(-15),       omega^nu=-1.
```

The identity was a *consequence* of the td8 route's multiplicities, drop
stages, leading factors, shared tower constants, and two actual child
vertices.  It is not a general Statement-3.9 law.

For td12 S17, custody contains no occurring `PairRef_S`, no completion, no
child vertex types or tower leading factors below the two northeast exits,
and no endpoint identification.  There is therefore nothing to ratio and no
cycle to close.  Transporting the td8 exponent or its torsion conclusion by
analogy would violate the campaign's explicit `OPEN` guardrail.

Statement 8.5 does not repair this: where its non-`V_{2,a}` lower-endpoint
hypothesis holds, it proves an `M`-divisibility, not a coefficient-ratio
identity.  It supplies neither the missing branch transports nor a return.

### 4.3 Charge gates and the source recurrence

The promoted charge theorem already counts two distinct flags and 32
necessary direction-level pure-power tests.  Non-torsion neither doubles
that count nor proves algebraic independence of the tests.

At lower-jet scope the reviewed `SOURCE_UNDERDETERMINED` theorem is stronger
negative evidence.  The two sibling vectors are evaluations of one common
`P_k` family, but the full order-one Keller convolution admits a formal
choice that changes the `B_+` evaluation while leaving the `B_-` evaluation
zero, with the matched g-side response.  Hence neither Galois conjugacy nor
a fixed cross-evaluation law follows from the top data plus the homogeneous
order-one Keller equation.  The later promoted cascade theorem strengthens
the same firewall: the type-`(2,3)` polynomial response makes the entire
depth-16 homogeneous window formally transparent in its stated range.
Genuine Keller content is deferred to the distant inhomogeneous row

```text
s* = D_F + D_g - kbar_F,
```

and no source vector or cap exists there.

These formal witnesses are not exact polynomial Keller pairs and do not
prove that no global holonomy can ever exist.  They do prove that a
holonomy cannot be extracted from the currently available reduced top and
homogeneous-window equations.

## 5. Precise `OPEN` interface

A future `TWIN-ORDER` kill is licensed only after a source packet proves all
of the following:

```text
H1  PairRef_S(f,g), J(f,g)=1, and occurrence of the nu=17 sibling cell;
H2  one common completion/source-jet family and the two centres
      c_+^17=B_+, c_-^17=B_-;
H3  typed edge/tower transport on both exits, including every leading
      factor and shared constant used in a ratio;
H4  a genuine endpoint identification or periodic return to the same
      labelled gauge (not unordered root swap, field conjugation, or a
      native mu_17 representative change);
H5  after cancellation, a proved nonzero net exponent N in
      rho^N=zeta with zeta torsion.
```

`H5` plus §2 gives an immediate exact contradiction.  The first currently
missing logical premise is `H4`; the first missing executable object is
`H1`/`H2`, namely `TD12LocalPairJet_S`.  Without them, a dynamical
pigeonhole argument is also unavailable: no self-map is defined whose
iterate multiplies a gauge by `rho`, and no periodic state is proved.

This is the narrowest useful stop.  It does not say a global source law is
impossible; it says exactly where new information must enter.

## 6. History deduplication

1. The general ratio/torsion idea appeared in the 0250Z td8 equal-join
   planning and later became the route-specific reviewed td8 twin law.
2. The exact Gaussian certificate for the td12 ratio was introduced in the
   1224Z Fable blind report and independently rechecked in the Opus and Grok
   cross-pollination reports.  It is not new in this note.
3. The same cross-pollination already rejected the advertised rigidity/
   independence payoff: swap is inversion/conjugation, Galois linkage of
   lower jets is unforced, and the 32 necessary tests were already canonical.
4. The reviewed TD12-BCHILD disposition subsequently gave an explicit
   one-sided level-one variation, and the promoted cascade result stopped
   homogeneous-window descendants.  Those results make a new “independence
   from non-torsion” lane duplicate and ill-typed.

Accordingly this report closes the previously scheduled short
derive-or-`OPEN` residue.  It creates no new avenue, does not rerank Avenue
2, and does not launch a descendant.  The honest successor is the already
named global source bridge / route-separated S17 pair packet, not another
torsion computation.

## 7. Maximum safe consequence and non-claims

Promotable after independent review:

> For the reviewed td12 sibling T1 template, `rho=(4+3i)/5` has infinite
> order even modulo roots of unity.  Thus any future source-backed closed
> holonomy forcing `rho^N` torsion for `N!=0` excludes that reduced cell.
> No such holonomy is present in current custody; native deck, dilation,
> label swap, printed one-edge transport, the charge gates, and the
> homogeneous Keller window do not supply it.

Not claimed: occurrence or nonoccurrence of the sibling cell; an actual
route automorphism; ordering or algebraic independence of the two child
vectors; a source packet; a depth-gate verdict; landing; a `td=12` panel
kill; a degree bound; a counterexample; or any JC2 conclusion.

<!-- UNIQUE::TWIN-ORDER-DERIVE-OR-OPEN-SOL56-20260829 -->

## Seal

- Body length: `13268` bytes (all bytes before this heading).
- Body SHA-256:
  `b186cad9e634c4878366482d16aacba5f72ef378e7a4ad84382de32d128ef046`.
- Frozen Git basis: `92ebe92ad5986a47f01af9ed901260595dfed869`.
