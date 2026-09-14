# D125: exact low-Jacobian saturation, not new independent equations

2026-09-07. **DESK PASS for sparse source-valid preconditioning; NO additional compressed-coordinate or measured solver gain established.** The complete total-degree0/2 Jacobian rows, saturated by k, are exactly three simple equations. The proof starts from accepted14c moving faces, independently of the unpromoted boundary classification.

## 1. Literal rows before any division

Work in S=Q[k,a,x,y,e,b21,b12,b03,…], where a=a01, x=a12, y=a03 and the dots denote untouched coefficients. Odd parity and the exact polygons give

    A₁=a p,                  B₁=d g+e p,  d=5k²/9,
    A₃=k g²p+x gp²+y p³,     B₃=b21 g²p+b12 gp²+b03 p³.

The full target is [A,B]=−5k³g²/9. Higher homogeneous parts cannot enter Jacobian total degrees0 or2. Direct differentiation gives

    r0=−d a,
    r_gp=2ke−2dx−2a b21,
    r_p2=xe−3dy−a b12.

The g² row is identically −dk+5k³/9=0. The terms involving a b21,a b12 are real [A₁,B₃] contributions; they disappear only after a=0. No other low row was silently omitted.

## 2. Exact saturation and certificates

Let I_low=(r0,r_gp,r_p2), h1=9e−5kx and h2=x²−3ky. Then

    I_low : k^∞ = (a,h1,h2) =: G.

Explicit polynomial identities, before localization, are

    k²a = −(9/5)r0,
    k³h1 = (9/2)k²r_gp−(81/5)b21 r0,
    k⁴h2 = (9/5)k³r_p2−(9/10)xk²r_gp
             +(81/25)(x b21−k b12)r0.

Conversely,

    r0=−5k²a/9,
    r_gp=2k h1/9−2a b21,
    r_p2=x h1/9+5k h2/9−a b12.

Thus the ideals agree after inverting k. To identify the contraction exactly, eliminate a,e from G. The remaining ring is a polynomial extension of Q[k,x,y]/(x²−3ky). The polynomial x²−3ky is primitive and linear in y over Q[k,x], hence irreducible by Gauss's lemma; the quotient is a domain and k is nonzero. Therefore G is already k-saturated, proving the displayed equality. This is a statement about the LOW ideal only, not the saturation or properness of the full source ideal.

In the full guarded source, k is already a unit, so these are exact ideal replacements over arbitrary further coefficient quotients, including nilpotents. There is no new localization. In an unguarded ring they are not equivalent: k=0,a=x=1,e=y=b21=b12=0 annihilates I_low but not G. This is an actual low-row countercontrol, not a full-source point.

## 3. Presentation tradeoff

On k≠0, the three graphs are

    a=0, e=5kx/9, y=x²/(3k).

One may retain h2 as a quadratic relation instead of substituting y. In an ordinary polynomial presentation with zk−1, the third graph is y=z x²/3. All remaining high/low Jacobian rows, all polynomiality rows, faces and the inverse guard must be carried through any substitution. Keeping graph nodes does not by itself remove variables.

The raw low system has seven literal terms, versus five in G. This is an exact tiny count, not a timing result. There are three available raw-coordinate eliminations, but **no additive three-variable saving in the reviewed graph presentations**: a01 and a03 are already A-Hermite pivots at levels1 and3, while e is the unique free B₁ column eliminated by its fixed-coefficient B block. The sparse relations then constrain their reconstructed values. Changing the order of those eliminations might alter expression growth, but no such substitution or comparison was performed.

These consequences were already required by the complete source rows. The bounded history checksum found no explicit earlier formula in the named canonical files; generic origin/lambda arguments were already present. No novelty, extra independent equation, source exclusion, point, or speedup is claimed. This is an optional preconditioning contract, not code-generation or baseline-change authority.

## 4. Optional finite-arc interface — classification remains PROVISIONAL

Conditionally use the sealed field-point classification `129947ee…`, not its live gate. Let a DVR containing Q carry finite receiver coefficients and k, with nonzero k generically and k→0. The generic point obeys the guarded source; the special point belongs to the UNGUARDED closure. The inverse variable k⁻¹ need not extend to the DVR. Since the DVR is a domain, the certificate identities above imply a=h1=h2=0 throughout it.

At a classified center A₀=R_t³+αR_t, B₀=R_t⁵+βR_t³+γR_t, the actual low coefficients are

    a01=−α(t+3), e=−γ(t+3),
    a03=−(t+3)³+αt.

Hence α(t+3)=γ(t+3)=0. If the residue of a03 is nonzero, it is a DVR unit and x²=3ky gives

    ord(k)=2 ord(x),

so ord(k) must be even. Under the displayed boundary constraints, a03 is nonzero except when t=−3 and α=0. That exceptional locus is NOT excluded. There the valuation equation also involves ord(a03).

Even ramification is consistent with the low rows: k=s², x=s, y=1/3, e=5s³/9, a=0 gives a literal low-row solution with b21=b12=0. It is not a full-face or polynomial-lift solution. Also the low saturated fiber at k=0 contains x²=0, not necessarily x=0 over nonreduced rings. Thus neither this calculation nor an unramified no-jet result decides the guarded source or all ramified approaches. No existence of a finite boundary arc is assumed for every guarded point.

## 5. Exact controls and custody

Eight capped standard-library runs pass normally/−O, with byte-identical witnesses and zero Assert nodes. The same checker rejects removal of [A₁,B₃], a changed sign in the k⁴ certificate, and an illicit unguarded-equivalence claim at the actual low-row counterpoint. Only degree-three receiver polynomials and low rows were expanded; no degree15/25 pair, full ideal, AWS/SSH/CAS or solver was used.

Witness SHA256 `37fc6434e2020d4580bf7401f0ed1eefde80778d6165e2cb406bbd045a1c92ca`. Input/read-scope pins and the exact identities are retained in the owned box. The classification gate is live and was not read. All writers idle at custody handoff. **STOP:** sparse low-row equivalence and conditional valuation restrictions only; no full-ideal unit/properness, generic-fiber, runtime or JC2 claim.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6135`.
- Body SHA-256:
  `3588e59354e09f6aab3f2d406e4678f740907cf694c4af0510c5cdf87ec9e0dd`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
