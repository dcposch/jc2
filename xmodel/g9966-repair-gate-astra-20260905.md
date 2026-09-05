**Hostile promotion gate: the repaired (99,66) branch kills**

Lane `g9966-repair-gate-astra-20260905`; frozen basis `524a3f5e60636eca4525b66c1ed9bac0d88624b2`.

**Verdict: REFUTED for both claimed re-certifications. Do not restore PROMOTED.** The centre lemma is true, the D2 radius is correct, and the two reported arithmetic units are authentic. The repair nevertheless retains a false exact-face restriction: its degree-11 auxiliary root has D2 face `pi^8`, whereas Moh's approximate-root theorem and the correctly encoded K2 face force the coefficient of `pi^5` to be `-8/3`. Freeing the minor constant leaves this missing coefficient zero. The resulting units certify the displayed restricted ideals, not the source branches.

There is also a gauge-accounting error. Two source translations survive placement of the directions at infinity. Their residual parameter cannot set `Hc_11_0` to zero: that coefficient is invariant. It can safely be freed at these endpoints because it does not occur in their equations. This fixes that particular pin, but does not fix the face obstruction.

**1. Custody and conventions.** Before mathematical use, I built `box/g9966-repair-gate-20260905/inputs.sha256` with `awk -F=` from the receipt's indexed `_basename` and `_sha256` fields and its `lane_inputs_dir`, then ran `sha256sum -c`. All seven frozen copies returned `OK`; the transcript is `hash-check.txt`. No content mismatch occurred. All work is confined to this report and `box/g9966-repair-gate-20260905/`; no ledger or `jc2-lean` work was performed, and no `ideation-*` input was used.

Citation abbreviations for inspected files:

| abbreviation | path |
|---|---|
| E | `/tmp/jc2-lane.8Gzrci/inputs/band_engine.py` |
| R | `/tmp/jc2-lane.8Gzrci/inputs/g9966-d2-precise-sol56-20260905.md` |
| C | `/tmp/jc2-lane.8Gzrci/inputs/d108-center-opus5-20260905.md` |
| P | `box/g9966-d2-precise-20260905/band_engine.py` |
| M | `box/g9966-repair-gate-20260905/moh-layout.txt` |
| N | `box/g9966-repair-gate-20260905/` |

M is a fresh extraction of the charged PDF; page images in N check formulas omitted by OCR. Detailed audits are `centre-radius-audit.md`, `gauge-audit.md`, and `custody-audit.md`. A third reader independently checked the new face obstruction.

Engine `F` has degree99 and is Moh's `g`; engine `G` has degree66 and is Moh's first characteristic polynomial. The canonical auxiliary roots have degrees33 and11. They are `h2,h3`, not Moh's characteristic `T2,T3`. Confusing these objects would invalidate the use of the source. Coordinates are `t=x^-1`, `w=ty`, `z=w-1`, `K2=t^33 h2`, and `K3=t^11 h3`.

**2. Lemma C, derived rather than inherited.** Moh Def.5.1(3), printed p.179, gives the logarithmic radii. Substitution of `n=99`, `M=(-66,77,97)`, `d=(99,33,11,1)`, and `V2=V3=8` gives

```text
delta3 = 1 - 2/1 = -1,
delta2 = 1 - 22*5/165 = 1/3,
delta1 = 1 - (165*143*5)/(1287*165) = 4/9.
L2=1, A2=3; L1=3, A1=3.
```

See M:2131–2138 and the page179 image; denominator increments are Moh p.201(8), M:3288–3291. Thus the prompt's `delta2=4/3` must mean the z-radius, not Moh's y-radius. The exact conversion is `ord(z1-z2)=1+ord(y1-y2)`, so the D2 z-radius is `4/3` and the D1 z-radius is `13/9`. After centre removal the substitutions are `t=s^3,z=pi*s^4` and `t=e^9,z=alpha*e^12+Pi*e^13`.

Def.5.1(4) specifies a unique generic point with centre truncated strictly below its radius (M:2137–2138; also Prop.1.2, M:373–390). `L2=1` alone does not prove the centre assertion. Here is a direct proof. By Def.5.1(1), D2 contains `(99/11)*8=72` roots of g, counted with multiplicity (M:2120–2124). Pass to a finite Puiseux cover containing all roots. Every cover Galois automorphism preserves g and valuation and takes D2 to a disc of the same radius containing72 roots. Equal-radius ultrametric discs are equal or disjoint; two disjoint such discs would require144 of99 roots. Therefore D2 is Galois invariant.

Its unique truncated centre is consequently fixed by every deck transformation. A nonintegral exponent with a nonzero coefficient would be moved by a suitable root of unity and would give a different truncated centre. This excludes exponents with denominator9 just as it excludes denominator3 or any other denominator. In particular the later D1 cover cannot insert exponents in `(0,1)` into the earlier z-centre. 

Since total degree equals y-degree, every g-root has order at least -1. After placing the major direction at `y=x`, the integral y-exponents below `1/3` are therefore `-1,0`. The first is the already placed leading term. Hence

```text
sigma2 = t^-1 + a1 + pi*t^(1/3),
z      = a1*t + pi*t^(4/3).
```

Thus Lemma C is confirmed. The source-support trace `eta=-[y^(N-1)]Q/N` is polynomial in x and cannot cancel fractional exponents (frozen support gate:42–46). It centres the outer support. The majority-disc argument supplies the missing justification in C:61–66 and C:271–274.

**3. Full normalization ledger.** The ledger distinguishes group actions, internal coordinate definitions and equations. Counting pins alone does not establish equivalence.

| engine convention or restriction | action and accounting |
|---|---|
| Two distinct leading directions become `y=0,y=x`; top `P0=y^3(y-x)^8` | Shear `y->y+mu*x` and scale `y->lambda*y` place two projective directions, spending two linear parameters. Source constants do not affect these directions. E:242–243. |
| F,G and the auxiliary roots monic | Two target scalings normalize leading coefficients. Canonical h2,h3 are then monic without extra source spends. E:363–367,484–493. |
| K2 face scale `beta=1` and selected child coefficient1 | Uniform dilation with compensating target scales: `F_lambda=lambda^-99 F(lambda*x,lambda*y)`, `G_lambda=lambda^-66 G(lambda*x,lambda*y)`. It sends `beta->beta*lambda^-4`; choose `lambda^4=beta` over the algebraic closure. Picking a conjugate child is a representative choice. E:367 and328–334. |
| Major D2 constant `a1=0` | Source translation `(x,y)->(x+A,y+B)` sends the root constant to `a1+A-B`. It spends the combination `B-A`. |
| Pristine minor constant0; replay `jet0` free | The same pullback sends the minor constant j to `j-B`. With major centre fixed, the residual diagonal translation `(A,B)=(q,q)` changes j freely. Thus the two centre constants can be normalized by two independent parameters; the replay keeps one of them as a redundant free coordinate. E:288–304; P:255–298. |
| Delta=5/2 `Hc_11_0=0`, metadata `b0=fixed_zero` | No residual source translation can impose this. It is an extra equation/pin, not a legitimate spend of the second translation. E:275–278. It must be proved independently or released. |
| Delta=2 double root at `zeta=0`, face `zeta^2(zeta+3rho)` | A generic-variable translation must propagate to `y=j+ut+(a2+zeta)t^2`. Replacing only the face omits the at-level root position. E:288–296,545–555. No universal source gauge for the omitted a2 is proved here. |
| Delta=5/2 odd face `pi(pi^2-c)` | The denominator2 deck action forces a monic odd cubic and the zero root plus a nonzero conjugate pair. c stays free and localized. Neither E nor P sets `c=1`; there is no second torus spend. E:297–304. |
| No h3² term in h2; no h2² term in F | Characteristic-zero approximate-root constructions define intermediate roots and transform remainder coordinates with F,G fixed; these are internal coordinate choices. E:307–388,484–493. |
| `K2c` replacement coordinates, seven D1 pivots, outer and joint pivots | Unit-triangular coordinate replacement and elimination by nonzero rational coefficients; no group normalization. E:191–239,314–361,400–470. |
| Total-degree boxes, D2 floors, D1 and minor rows | Necessary support claims or equations, each requiring a source theorem. They are not gauge spends. The strict h3 equality-face deletion fails that requirement, as shown below. |
| `z=w-1`, cover uniformizers, coefficient1 on a generic variable | Coordinate definitions and cover reparametrizations. The shift `w-1` records the already placed direction. They supply no extra source translation. |
| `rho!=0` or `c!=0` | Open-stratum restrictions implemented by `Zrho*rho-1` or `Zc*c-1`. No localizer is assigned a numerical value. E:608–650. |
| `jacobian_normalization_control` and finite stage schedule | The named control verifies the Jacobian coordinate formula. It does not impose `J0=1`. The endpoint rows set positive-degree coefficients to0; uniform dilation multiplies J by `lambda^-163` and preserves those equations. Finite truncation omits equations, with the degree bound recorded by the driver. E:506–537,666–722. |

Every nonconstant term of the centred h3 template is divisible by `y-x` (vmin is positive for r<=10). Thus

```text
h3(x,x) = Hc_11_0,
h3(x+q,x+q) = Hc_11_0.
```

The residual translation preserves this coefficient. Therefore R:73–84 and C:276–293 do not supply the claimed ledger. They also conflate Hc with an effective-root integration constant called b0. An auxiliary Xu equation can force Hc=0 under further hypotheses; this gate uses the following unconditional endpoint repair instead.

There is a completely safe endpoint repair of this pin. In either terminal job `max_t=8`: the delta2 pole band is8 and the delta52 band is16 on `t=s^2`. The extra h3 term is exactly `Hc_11_0*t^11`. Sparse products have nonnegative t powers, so it cannot enter K2, F,G, or a selected row through t^8. `free_h11_check.py` recompiles only the inner-count assertion `103->104`, releases Hc in the branch map, and compares all78 K2 coefficients exactly. The image is identical and the free-variable set gains precisely Hc. Downstream row definitions receive identical polynomials, so the stage8 identity64 extends to the polynomial ring adjoining Hc. See `free-h11-check.json`. 

The exact delta2 probe `face-minor-shift-probe.json` confirms that propagating a2 leaves one more free parameter. Residual diagonal translation changes a2 by a multiple of u; payment by this action needs separate coverage at u=0. This gate does not divide by u.

**4. Correct radius and K2 conjugacy; incorrect strict h3 face.** Def.5.1(1) gives g multiplicities72 at D2 and24 at D1. Def.5.1(4) and Prop.4.6(1) give its D2 face `p(pi)^3`, with p monic of degree24 and the selected child of multiplicity8 (M:1632–1635,2137–2138). The centred g face has only powers divisible by3. Since p is monic of degree24, `p(omega*pi)^3=p(pi)^3` implies `p(omega*pi)=p(pi)`. Thus p is a polynomial in pi³; a zero root cannot have multiplicity8. The three nonzero conjugates of the selected residue exhaust degree24. Each D1 has g order `24*(4/9)+48*(1/3)-27=-1/3`. Completing these three points with minor points at that accuracy, using Prop.6.1 as detailed below, permits Thm.1.1 to give h2 multiplicity8 at each. Consequently

```text
face_D2(K2) = (pi^3-beta)^8,  beta=alpha^3 != 0.
```

The D1 centre also has no hidden intervening terms: deck transformations fixing `t^(1/3)` preserve its alpha-packet of24 g-roots, all of which D1 contains. Equal-radius conjugate discs cannot be disjoint within that packet. Its centre therefore lies in `k((t^(1/3)))`, and no such exponent lies strictly between `1/3` and `4/9`.

E:364–372 encodes exactly this face with beta1: `(r,q)=(4k,24-3k)` has coefficient `(-1)^k binom(8,k)`. All these terms have weight96 for `W=3r+4q`. The (99,66) K2 face does not have the D=108 conjugacy error documented in C:208–212.

At a generic D2 point h3 has eight roots in that disc and three in the other leading cluster. Hence

```text
ord_t h3 = 8*(1/3)+3*(-1) = -1/3,
ord_s K3 = 3*(11-1/3) = 32.
```

The transcendental generic coefficient makes this an exact valuation. However, exact valuation32 determines a nonzero face, not the polynomial `pi^8`. Of the66 lower slots,43 are below32, two are at32, and21 are above32. The two equality slots are `(4,5)` and `(8,2)`; the general centred face is

```text
H(pi)=pi^8+kappa*pi^5+ell*pi^2.
```

E:245–253 uses `vmin=ceil((33-3r)/4)`, deleting both equality coordinates. Thus “33 is32 made strict” is arithmetic, not a source licence. The old assertion of a pure eighth power appeals to Moh propositions about g and characteristic T-polynomials; those propositions do not identify the degree11 h3 with a characteristic T. More strongly, the source forces kappa to be nonzero.

Here are all hypotheses for that stronger claim. Complete the single g-point D2 to a coherent complete system at accuracy `-3`. For each of the remaining27 roots, follow its disc until the generic valuation of g is `-3`, and merge repeated discs. Along a root ray this valuation is `sum min(delta,ord(tau-root))`, a continuous piecewise rational-affine function with positive slope, starting below `-3` and tending to infinity. The required radius exists and is rational. Different resulting discs are disjoint or equal; together with D2 they cover all99 roots. This is Moh's complete/coherent definition, p.148, M:445–461.

The principal minor packet has multiplicity3, below `d3/(n-M3)=11/2`, so Prop.6.1 applies at r3. Every added point is strictly in that packet after radius `-1` and has `ord g=-3<0`. Prop.6.1(2), p.191, makes it a distribution detector for `g,T1,T2` (M:2727–2762; the proof also covers radii at least1, M:2855–2874). These polynomials have degrees99,66,55. The last number follows from the characteristic recurrence `q2=143`, `lambda2=99*(-66)+33*143=-1815`, `mu2=-55`, and Prop.2.2(1), printed pp.150,152. Their reduced ratio is9:6:5. Def.3.1(4), p.161, M:1155–1172, therefore forces every added g multiplicity to be divisible by9. The major multiplicity72 is divisible by9 too.

Apply Moh Thm.1.1, p.149, first to the canonical cube root h2 of g, then to the canonical cube root h3 of h2. The complete system persists, with accuracies `-1` and `-1/3`; divisibility by3 holds at both steps. No assertion equating a nested cube root with a ninth root is needed. Thm.1.2 applies to

```text
h2=h3^3+C2*h3+C3,     deg_y C2,deg_y C3 <= 10,
ord C2(sigma2) >= -2/3,    ord C3(sigma2) >= -1.
```

These are the actual inequalities on the inspected page149, M:478–507. Normalize C2 by t^22 and C3 by t^33. Their floors are weights64 and96. At equality their faces satisfy

```text
U in span{pi^10,pi^7,pi^4,pi},
V in span{pi^9,pi^6,pi^3,1},
(pi^3-beta)^8 = H(pi)^3 + U(pi)*H(pi) + V(pi).
```

Now `deg(UH)<=18` and `deg V<=9`. Comparing the coefficient of pi^21 gives

```text
-8*beta = 3*kappa,
kappa = -8*beta/3 != 0.
```

The engine has beta1 and kappa0. This contradicts source coverage on both branches, independently of jet0 and Hc. `forced_face_control.py` checks the comparison over Q with beta symbolic; its negative control gives `-8` at the old face and its positive control gives0 at kappa `-8/3`. The next coefficient gives `U10=20*beta^2/3-3*ell`, so ell must not be prematurely pinned to `20/9`; it remains free at this argument's level.

Ordinary Euclidean division still represents low-q K2 outputs with the old h3: at t^4 divide `-8*z^21` by `z^8(1+z)^3`, obtaining quotient and remainder of degree10. But that C2 quotient has weights12 through52, below the source floor64. Thus the output-coordinate change is algebraically valid while the source restriction fails. `forced-face-control.json` checks the division and weight bound.

**5. Replay custody and fresh execution.** All230 entries in Sol's artifact manifest passed independently. The pristine engine hash is `3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9`; the precise engine hash is `76d8c7206f70ba190d1a21fff812c016cbde497cd64071c29c91cfe8089f3c06`. Both match the archived files. The earlier endpoint `joint_elimination` objects exactly match Sol's pristine controls.

| branch | pristine endpoint | Sol precise endpoint | exact identity in its quotient |
|---|---|---|---|
| delta2 `[2,1]` | stage4, `stage4_J_d159_k35=6264` | same label and constant | `1=(1/6264)*stage4_J_d159_k35` |
| delta5/2 `[1,1,1]` | stage8, `stage8_G_local16_coord0=64` | same label and constant | `1=(1/64)*stage8_G_local16_coord0` |

All35 delta2 pivot expressions and118 residuals, and all66 delta52 pivots and its one residual, specialize exactly at `jet0=0` to pristine. Labels, row accounting and h3 maps agree; the free generators gain exactly jet0. Constant picks in the minor substitution lower y powers within the triangular source support, while zero picks recover the old terms. Hence the raw row support is unchanged. This proves inclusion of the pristine declared charts, not coverage of every source object.

The coefficient field is Q. Joint pivots use only nonzero rational coefficients, exclude rho/c, and are resolved in the declared symbol order. The residual ring includes the active symbols plus a Rabinowitsch variable; the remaining inactive coordinates are free polynomial extensions. There is no `sat()` wrapper extraction in these endpoint scripts: they directly impose the localization equation. Four independent Singular replays, covering both pristine and both precise endpoints, returned dimension-1 and basis1. Controls `<p,Zp-1>`, `<p-1,Zp-1>`, and the raw residual returned `0,1,0` on reduction of1. No modular result or parameter division supplies a verdict. See N's `custody-independent-checks.json` and `custody-endpoint-specialization.json`.

I also ran the complete precise delta2 stage4 engine locally, not merely its emitted Singular file. It exited0 in GNU wall time `5:52.88`, peak RSS160068KiB, and reproduced35 pivots,118 residual rows, and the literal6264. Local SymPy1.12 differs from Sol's1.14.0; nevertheless the entire `joint_elimination` object, including pivot maps, raw-row hash, residual hash and Singular result, is exactly equal. The final JSON SHA-256 is `2797fc1f150c563693deea04a9ab8d4e59b8c5450981e5d5d0a8212001a0d664`. Records are `local-delta2/stage4.*` and `local-delta2-comparison.json` in N. This satisfies the requested independent final-stage replay within60 minutes.

**6. Corrected-face diagnostics and disposition.** The separate diagnostic engine retains the charged radius, supports above the face, outer construction and stage schedule; adds the raw equality terms `(-8/3)*t^4*z^5+ell*t^8*z^2`; re-solves both minor maps exactly with jet0 free; and leaves Hc_11_0 free. The old basis is preserved, so an equality coefficient is not accidentally substituted for a differently defined old Hc symbol. Exact leader controls pass on both branches:18 pivots on delta2 and20 on delta52, with no residual. This is a face correction, not the specialization inclusion proved for Sol's jet0-only enlargement.

The diagnostic engine SHA-256 is `a8956254b4714d5e327998ad3222016f4280031f22345ccaef2b1824369890ca`; its builder, complete diff and initial controls are in N. The results are:

| corrected diagnostic | measured result | exact point in pre-joint free coordinates |
|---|---|---|
| delta2 stage4 | 35 pivots, zero residual, dimension917; GNU wall6:12.36, RSS166216KiB | jet0=rho=1, all other950 coordinates0 |
| delta52 stage8 | independently proved NONUNIT by direct substitution of all1285 rows; no completed Gröbner dimension claimed | jet0=c=1, all other929 coordinates0 |

For delta2, an independent evaluation substitutes the full952-coordinate assignment into K2 and outer blocks BEFORE multiplying F,G. All659 raw rows vanish, including the formerly6264-labelled row. For delta52 the same method, without reading a solver endpoint, verifies all1285 rows and sends the formerly64-labelled row to0. The localizer and its inverse are1 in each case. Perturbing `B1c_0_32` from0 to1 produces515/1039 nonzero rows, respectively; the first is `stage1_J_d162_k35=-864`, also checked by direct differentiation. Setting the localizer0 makes its wrapper equation -1.

Certificates are `corrected-point-delta2-validation.json` and `corrected-point-delta52-trial.json`, with reproducible scripts in N. After the exact delta52 point proved nonunit, I deliberately terminated the redundant symbolic job with SIGTERM; its rc143 and `face-delta52/intentional-stop.json` record that choice. No conclusion is inferred from termination. These points witness survival of the corrected finite diagnostic equations, including delta2's retained at-level slice, not a full source system or Keller pair.

The charged claim combines true centre/radius facts with an unproved—and here contradicted—pure h3 face. Therefore the verdicts on the requested re-certifications are:

| branch | gate verdict | status to carry forward |
|---|---|---|
| delta2 `[2,1]`, `17(pppp)` | **REFUTED** | `OPEN[G9966-DELTA2-SOURCE-FACE]`; the at-level minor-root coordinate is an additional coverage obligation. |
| delta5/2 `[1,1,1]`, `17(tttt)` | **REFUTED** | `OPEN[G9966-DELTA52-SOURCE-FACE]`; Hc can be released without changing the old endpoint but that alone is insufficient. |

The refutation concerns promotion by these certificates. It neither supplies a Keller pair nor settles either branch's ultimate existence. A safe replacement must encode the allowed h3 equality face, carry every minor centre actually used, and certify its resulting necessary ideal. Authentic units on restricted charts cannot replace that coverage argument.

FALLACY-v2 checks distinguish valuation from face, h3 from characteristic T, and partial-chart points from Keller pairs. Source hypotheses, ring maps, Q* pivots and localization controls are explicit above. No new exit-price assertion is made; no `charge_basis` line or ledger edit is appropriate.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `21605`.
- Body SHA-256:
  `46efe6729e502056a8fee56d518ce2530575be92d0c3cb012866ac88bc28de08`.
- Frozen basis: `524a3f5e60636eca4525b66c1ed9bac0d88624b2`.
