# CORRECTED-863-KILL-REVIEW

Lane: CORRECTED-863-KILL-REVIEW.  Date: 2026-09-01.

Status: SEALED.

Verdict: KILL-BINDING, conditional only on the charged two-engine
computational result being the as-run result for the hashed files.  I found no
encoding defect in the corrected Delta=(8,6,3) curve-level incidence system.
The as-run `.ms` and patched `.m2` files encode the audit section 7.1 corrected
D system: closed `g_j=[t^j]G86=0` for `4<=j<=22`, open `g_3!=0` by
Rabinowitsch, in the normalized `(8,6)` chart with the retained auxiliary
terms of pole degree strictly greater than `c=3`.

No new exit-price assertion is made in this report.

## 1. Hash Gate And Inputs

I verified the two frozen review inputs before reading them:

```text
d80c691861d362f1569b38c80a222c2df4992e62f13297adc2e5a996d99a0f18  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.p4m8n5/inputs/corrected-suite-codegen-grok46-20260901.md
a3c7137cdb2cf46c7d9026cfbcba54b0b6e5b47a6ef36ad7ee2976a905c8b196  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.p4m8n5/inputs/encoding-faithfulness-audit-r2-sol56-20260901.md
```

Both match the charged hashes.  I also verified the as-run job-file hashes:

```text
cd13e1c25bcfcc43d30c238420ab8383580b8c078b16c0b0ff967ff43761d75b  box/corrected_863.ms
411b2e865602aefc8c3bc9993318e3980a62cf21ae5ad3ac30c3b4ec446fd74f  box/corrected_863.m2
```

Both match the hashes in the review charge.  Note a custody wrinkle: the
codegen report records the original emitted hash
`a6c7e647316f6546145a855b4f8ee972a188f5a2db1171304f5f032c7beff937`
for `box/corrected_863.m2` at lines 209-211 of the frozen codegen report.  The
review charge explicitly names the later coordinator-patched hash
`411b2e...fd74f`, and the file on disk matches that patched hash.  I therefore
reviewed the as-run patched `.m2`, not the stale codegen-hash artifact.

Line references below are to the frozen inputs or the as-run repo files:

```text
charged_input:
  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.p4m8n5/inputs/corrected-suite-codegen-grok46-20260901.md
  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.p4m8n5/inputs/encoding-faithfulness-audit-r2-sol56-20260901.md
jobs:
  box/corrected_863.ms
  box/corrected_863.m2
```

## 2. Correct Specification Re-derived

The audit's shared `(8,6)` chart is, in its notation,

```text
p = t^8 + B t^5 + C t^4 + D t^3 + E t^2 + F t + G
q = t^6 + b t^4 + gamma t^3 + d t^2 + e t + f
H = p^3 - q^4 = sum h_j t^j
```

This is stated in the audit at lines 51-57.  The audit then explains that raw
coefficients are not the characteristic coefficients: the second approximate
root must be reduced by triangular semigroup terms.  The exact global
dictionary at audit lines 138-149 says that `(8,6,3)` requires the preceding
reduced vanishings plus `j={7,5,4}` and the open `bar_h_3 != 0`.  The explicit
rerun specification is audit section 7.1, lines 469-486:

```text
G86 = p^3-q^4
    + a22*p^2*q + a20*p*q^2 + a18*q^3
    + a16*p^2   + a14*p*q   + a12*q^2
    + a8*p + a6*q
```

Retain terms whose weights are strictly greater than the target `c`.  For D,
`c=3`, so all eight displayed auxiliary terms are retained.  With
`g_j=[t^j]G86`, the required closed equations are `g_22,...,g_4`, and the
required open is `u*g_3-1`.  The codegen report repeats the same chart and
dictionary at lines 62-76 and the same P1 layout at lines 106-119, but I did
not use that transcript as the derivation source.

Independent expansion in SymPy, starting only from the audit chart and
section 7.1 `G86`, gives support from degree 0 through 22 and `g_23=0`.  The
first coefficients are:

```text
g_22 = a22 - 4*b
g_21 = 3*B - 4*gam
g_20 = a22*b + a20 + 3*C - 6*b^2 - 4*d
g_19 = 2*a22*B + a22*gam + 3*D - 12*b*gam - 4*e
```

These are the corrected reduced-root equations, not the old raw odd
`h_21,h_19,...` list.  In particular `g_22=0` solves `a22=4*b`, and then

```text
g_19 | a22=4*b = h_19 + 4*b*(2*B+gam),
```

matching the audit's reduced-vs-raw warning at lines 180-187 and the codegen
sanity transcript at lines 97-104.  The semigroup slots are triangular with
leading coefficient 1 in `a22,a20,a18,a16,a14,a12,a8,a6` at degrees
`22,20,18,16,14,12,8,6`.  Degrees 10 and 4 are genuine gap residuals; they
are not absorbable by omitted `a10` or `a4` variables.  This matches audit
lines 151-156 and 202-215.

## 3. The `.ms` File As Run

The first line of `box/corrected_863.ms` is exactly the msolve variable list:

```text
a22,a20,a18,a16,a14,a12,a8,a6,B,C,D,E,F,G,b,gam,d,e,f,u
```

The second line is `0`, hence characteristic 0.  The file has 22 lines total:
20 variables, 20 generators, no leading in-band comment, no parentheses, no
trailing comma on the last generator, and one trailing newline.  The variable
list is exactly the 19 base variables of the audit/M2 chart plus the
Rabinowitsch variable `u`.

I parsed every polynomial line, converted `^` to exponentiation, expanded the
audit-derived `G86` independently, and compared exact SymPy equality.  Every
generator matched its intended coefficient.  The full comparison table is:

```text
ms line  degree/open  term count  canonical digest prefix  result
3        g22          2           cfd9297985c3f31e         match
4        g21          2           4d9f140c9fc3f373         match
5        g20          5           90fc41917e75cf6e         match
6        g19          5           39c13d67a79a3771         match
7        g18          10          0ea16437f9d35586         match
8        g17          10          12acb113caaa871b         match
9        g16          19          2fc62fa1af3fde5c         match
10       g15          19          94efd90def74eeea         match
11       g14          29          f16651051b9750e3         match
12       g13          32          487e3f5f0ad7508b         match
13       g12          46          7286427502a88cc2         match
14       g11          45          a26ca2d7f73739aa         match
15       g10          56          3529ebd3b44abf97         match
16       g9           57          7f1bcfc3ab705e91         match
17       g8           64          fbae163b844d5b68         match
18       g7           55          0fa16942a886ce70         match
19       g6           59          7d701481fe3e9e54         match
20       g5           47          e42438a1dd37fed3         match
21       g4           44          b98b1e9f4282ea0e         match
22       u*g3-1       32          8424208cf5bc358e         match
```

This verifies coefficient-by-coefficient that the `.ms` polynomial list is
`g_22,g_21,...,g_4,u*g_3-1`.  It also verifies the variable-order/count hazard:
msolve will parse line 1 as the intended variable list, not as a comment or as
a malformed first variable.

For the single most relevant low-degree terms, the independent expansion gives
the following.  These are not copied from the codegen transcript.

```text
g_4 =
  3*C*G^2 + 2*C*G*a16 + 2*C*G*a22*f + C*a14*f + C*a20*f^2
  + C*a8 + 6*D*F*G + 2*D*F*a16 + 2*D*F*a22*f + 2*D*G*a22*e
  + D*a14*e + 2*D*a20*e*f + 3*E^2*G + E^2*a16 + E^2*a22*f
  + 3*E*F^2 + 2*E*F*a22*e + 2*E*G*a22*d + E*a14*d
  + 2*E*a20*d*f + E*a20*e^2 + F^2*a22*d + 2*F*G*a22*gam
  + F*a14*gam + 2*F*a20*d*e + 2*F*a20*f*gam + G^2*a22*b
  + G*a14*b + 2*G*a20*b*f + G*a20*d^2 + 2*G*a20*e*gam
  + 2*a12*b*f + a12*d^2 + 2*a12*e*gam + 3*a18*b*f^2
  + 3*a18*d^2*f + 3*a18*d*e^2 + 6*a18*e*f*gam + a6*b
  - 4*b*f^3 - 6*d^2*f^2 - 12*d*e^2*f - e^4 - 12*e*f^2*gam
```

```text
g_3 =
  3*D*G^2 + 2*D*G*a16 + 2*D*G*a22*f + D*a14*f + D*a20*f^2
  + D*a8 + 6*E*F*G + 2*E*F*a16 + 2*E*F*a22*f + 2*E*G*a22*e
  + E*a14*e + 2*E*a20*e*f + F^3 + F^2*a22*e + 2*F*G*a22*d
  + F*a14*d + 2*F*a20*d*f + F*a20*e^2 + G^2*a22*gam
  + G*a14*gam + 2*G*a20*d*e + 2*G*a20*f*gam + 2*a12*d*e
  + 2*a12*f*gam + 6*a18*d*e*f + a18*e^3 + 3*a18*f^2*gam
  + a6*gam - 12*d*e*f^2 - 4*e^3*f - 4*f^3*gam
```

The `.ms` final line is exactly `u*g_3-1` after multiplication through by `u`
and subtraction of 1.

## 4. The Patched `.m2` File As Run

The patched `box/corrected_863.m2` encodes the same incidence ideal:

```text
R0 = QQ[a22, a20, a18, a16, a14, a12, a8, a6,
        B, C, D, E, F, G, b, gam, d, e, f,
        MonomialOrder => GRevLex]
St = R0[t]
p = t^8 + B*t^5 + C*t^4 + D*t^3 + E*t^2 + F*t + G
q = t^6 + b*t^4 + gam*t^3 + d*t^2 + e*t + f
G86poly = p^3 - q^4 + ... + a8*p + a6*q
gj = (j) -> coefficient(t^j, G86poly)
closedIdx = {22,21,...,4}
Iopen = sub(I0, R) + ideal(sub(gopen, R)*u - 1)
```

Specific file evidence:

```text
box/corrected_863.m2:16   R0 over QQ, 19 base generators, GRevLex
box/corrected_863.m2:18   assert(numgens R0 == 19)
box/corrected_863.m2:21   St = R0[symbol t]
box/corrected_863.m2:22   assert(numgens St == 1)
box/corrected_863.m2:24   p in the audit chart
box/corrected_863.m2:25   q in the audit chart
box/corrected_863.m2:26   G86poly in the audit section 7.1 form
box/corrected_863.m2:29   killt = map(R0, St, {0_R0})
box/corrected_863.m2:32   gj = (j) -> coefficient(t^j, G86poly)
box/corrected_863.m2:33   closedIdx = 22 down to 4
box/corrected_863.m2:37   gopen = gj(3)
box/corrected_863.m2:40   R = R0[u]
box/corrected_863.m2:41   assert(numgens R == 1)
box/corrected_863.m2:42   Rabinowitsch open sub(gopen,R)*u - 1
```

The `.m2` file contains the cover colon and affine-immersion computations, but
those are not part of the base kill decision.  They are downstream:

```text
box/corrected_863.m2:45-48   Cover0 = ideal(B,D,F,gam,e)
box/corrected_863.m2:50-63   colonInf loop with ring asserts
box/corrected_863.m2:65-66   Icolon from Iopen
box/corrected_863.m2:68-78   resultant inverse and IimmColon
box/corrected_863.m2:83-85   gb and EMPTY test are for Iopen
```

Thus `.m2` and `.ms` use the same mathematical generators:

```text
base ring variables:  a22,a20,a18,a16,a14,a12,a8,a6,B,C,D,E,F,G,b,gam,d,e,f
open variable:        u
closed generators:    [t^22]G86, [t^21]G86, ..., [t^4]G86
open generator:       u*[t^3]G86 - 1
coefficient field:    QQ / characteristic 0
```

The `.ms` ring is a flattened `QQ[base,u]`; the `.m2` ring is the tower
`R0[u]` with `R0=QQ[base]`.  For ideal emptiness and generator content these
are the same polynomial ring over `QQ` up to the displayed variable ordering.
No generator appearing in the `.ms` file mentions a variable outside line 1,
and no expected variable is missing from the union of the ring declarations.

## 5. Coordinator Patch Audit: `gj`

The dangerous patched line is:

```m2
gj = (j) -> coefficient(t^j, G86poly);
```

This is the right argument order for Macaulay2.  The official Macaulay2
documentation for `coefficient` gives usage `coefficient(m,f)`, requires `m`
and `f` to be ring elements in the same ring, and says the output is an
element of the coefficient ring of that ring.  It also explicitly notes that
the returned value is in the coefficient ring even when that coefficient ring
is another polynomial ring:

```text
https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Macaulay2Doc/html/_coefficient.html
```

Applied here:

```text
St = R0[t]
t^j in St
G86poly in St
coefficientRing(St) = R0
```

So `coefficient(t^j, G86poly)` extracts the coefficient of the monomial `t^j`
and returns an element of `R0`, with all `a` variables and chart variables in
the base.  That is exactly what the audit specification means by `[t^j]G86`.

I did not have a local `M2` executable on PATH, so I could not rerun a live M2
probe in this review environment.  The as-run M2 result is consumed from the
charge (`rc=0`, char 0, `gb=|1|`).  For encoding faithfulness, the static check
is decisive because the patched line uses the documented signature and the
same-ring condition is enforced by the file structure and asserts.

I see no silent-zero hazard in the patched extraction:

1. Wrong-ring monomial: no.  `use St` precedes construction of `p`, `q`,
   `G86poly`, and `closedGens`; the symbol `t` is the generator of `St`.
   `t^j` and `G86poly` are in the same ring.
2. Base-variable loss: no.  Since `St=R0[t]`, the coefficient ring is `R0`,
   not `QQ`; the `a` and chart variables remain as coefficients.
3. Degree-0 edge: no.  The closed range is `j=4..22` and the open is `j=3`.
   These are positive powers of `t`; none asks for the constant coefficient.
   Even if an absent monomial were requested, the documented result would be
   `0_R0`, but the independent expansion shows all intended degree slots are
   being queried in the right polynomial.
4. Map-to-zero footgun: no for `gj`.  The patched `gj` does not apply `killt`
   to coefficients.  `killt` is named and used only for the resultant after
   the base ideal is built.

The required three coefficient spot checks against independent SymPy
expansion are stronger than spot checks: all 20 `.ms` lines matched.  In
particular:

```text
[t^22]G86 = a22 - 4*b
[t^19]G86 = 2*B*a22 + a22*gam + 3*D - 12*b*gam - 4*e
[t^10]G86 = canonical digest 3529ebd3b44abf97, 56 terms, matches .ms line 15
[t^4]G86  = canonical digest b98b1e9f4282ea0e, 44 terms, matches .ms line 21
[t^3]G86  = canonical digest 1c2de556af8f71f2fa47c9bb32fdcbf5febec4a8c07719250fc64dca3112687d, 31 terms;
             .ms line 22 is u*[t^3]G86 - 1
```

The `g_4` and `g_3` formulas displayed above are the direct low-degree
cross-checks most likely to catch a silent-zero or wrong-ring extraction bug.

## 6. Empty Semantics And Cover Locus

The charged computational result says the corrected `.ms` Groebner run
returned `basis=[1]`, and the M2 mirror returned `dim=-1`, `gb=|1|`, `rc=0`,
char 0.  This review does not revalidate the Groebner computation itself.  It
does check that the unit ideal, if returned for these files, has the needed
semantic meaning.

The `.m2` flow tests `Iopen` itself for the unit ideal:

```text
I0       = ideal(g_22,...,g_4)
Iopen    = I0 + ideal(u*g_3 - 1)
Icolon   = colonInf(Iopen, Cover)
Iimm...  = I0 + ideal(u*g_3 - 1, v*Res(p',q') - 1)
Gb       = gens gb Iopen
EMPTY    iff Iopen == ideal(1_R)
```

This is visible at `box/corrected_863.m2:35-43` and `83-85`.  Therefore the
reported unit ideal is before cover colon and before the affine-immersion
resultant.  That is the strongest possible direction for the kill: if the
open characteristic incidence locus is empty before adding downstream nodality
conditions, then every stricter locus is empty too.

The Rabinowitsch open is part of `Iopen`, so the empty set is the open locus
`g_22=...=g_4=0`, `g_3!=0`.  This is exactly the corrected type-D incidence
locus from audit section 7.1.  The audit states at lines 169-177 that because
`gcd(d,n,c)=1` in the corrected rows, the corrected `c`-open excludes every
nontrivial common right component; affine immersivity and reduced double
points are separate nodality tests.  For `(8,6,3)`, `gcd(8,6,3)=1`.

The explicit old cover ideal in the job is:

```text
Cover0 = ideal(B, D, F, gam, e)
```

On this cover locus,

```text
p = t^8 + C*t^4 + E*t^2 + G
q = t^6 + b*t^4 + d*t^2 + f
```

so `p` and `q` are even polynomials in `t`.  Since `G86` is a polynomial in
`p` and `q`, every odd coefficient of `G86` vanishes on this locus.  I checked
this directly in SymPy:

```text
g_5 | Cover0 = 0
g_3 | Cover0 = 0
g_1 | Cover0 = 0
all odd g_j for 1<=j<=21 vanish on Cover0
```

Thus no legitimate corrected `(8,6,3)` point is hidden inside the old degree-2
cover locus: `u*g_3-1` already makes that locus disjoint from `Iopen`.  More
generally, a common right component of degree `m>1` would divide the degrees of
`p`, `q`, and the exact reduced second approximate root degree `c`; the open
`g_3!=0` fixes `c=3`, incompatible with the only common divisor possibility
for 8 and 6.  The colon is harmless but unnecessary for the curve-level empty
claim.

## 7. Self-checks And Positive Control

I reran the required positive control `(9,6,2)` in SymPy using the audit's
displayed curve at lines 434-443 and the codegen transcript at lines 179-190:

```text
q = t^6 + 8*t^2
p = t^9 + 12*t^5 + 24*t
G96 = p^2 - q^3 + a15*p*q + a12*q^2 + a9*p + a6*q
(a15,a12,a9,a6) = (0,0,0,-64)
```

The independent expansion gives:

```text
G96 = 64*t^2
closed g_16..g_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
g_2 = 64
g_1 = 0
g_0 = 0
```

So the corrected encoding method does not kill the known realized
`(9,6,2)` curve.  This is the positive control requested in the review charge.

I also spot-reran the other two codegen self-checks for method sanity:

```text
charged A false-positive:
  h_21=h_19=h_17=h_15=h_13=0
  h_11=59291/18432 - 27671*zeta/110592
  h_22=-4, h_20=-10
  [t^19](H+4*p^2*q+6*p*q^2)=11

HF-twin (9,6,4):
  corrected closed g_16..g_5 all vanish
  g_4=-27/128
  g_2=-351/1024
  g_0=0
```

These agree with the codegen transcript's qualitative claims: the old
`(8,6,11)` point fails the corrected reduced-root system, while the corrected
`(9,6,4)` membership example is nonempty at the incidence level.  They are not
needed for the P1 kill, but they do confirm that the corrected-coefficient
method is not globally overrestrictive.

## 8. Guardrail Review

FALLACY-v2 checks applied:

```text
Flag/place/series:
  No physical-place count is inferred from conjugate Puiseux series or field
  embeddings.  The P1 conclusion is only about the corrected characteristic
  incidence locus being empty.

Variable/ring map:
  The M2 map and tower rings are explicit.  Matching variable names alone are
  not used as proof; the `.ms` list is parsed and compared to an independent
  expansion, and M2's `coefficient(m,f)` signature is checked against the
  official documentation.

Raw remainder degree:
  The encoded equations are coefficients of `G86`, not raw `H=p^3-q^4`.
  The gap residuals `g_10` and `g_4` are included.

sat() wrapping:
  No `saturate()` is used.  Opens are Rabinowitsch equations.  The colon loop
  is downstream and ring-asserted; the kill decision is already `Iopen==(1)`.

Floor/attainment:
  This report does not infer node counts from a floor or from a representative
  locus.  Empty characteristic incidence is consumed only as a curve-level
  obstruction for `(8,6,3)`.

Carrier/attainment and target/arrival index:
  The target is fixed `Delta=(8,6,3)`, equivalently exact reduced second
  approximate-root degree `c=3`, not a legacy Moh raw-index label.
```

## 9. Repairs

No repair is required for the as-run P1 files.

The only nonblocking custody note is that the sealed codegen report's
per-file table has the pre-patch `.m2` hash.  The review charge supplied the
post-patch hash, and the repo file matches it.  Future consumers should verify
the as-run hash from the job file itself or from this review charge, not from
the stale codegen line.

## 10. Final Binding Statement

Encoding verdict: KILL-BINDING.

Under the charged computational fact that the hashed
`box/corrected_863.ms` run returned `basis=[1]` and the hashed patched
`box/corrected_863.m2` mirror returned unit ideal evidence over characteristic
0, the corrected `(8,6,3)` characteristic open locus is empty over `QQ`.

Because that open locus is exactly audit section 7.1's corrected type-D curve
incidence system, and because the unit ideal is obtained for `Iopen` before
cover colon, immersion, or double-point restrictions, there is no remaining
curve-level `(8,6,3)` path in this encoding chain.  The kill binds at the
curve level, subject only to the charged CAS result rather than to any defect
in the reviewed encoding.
