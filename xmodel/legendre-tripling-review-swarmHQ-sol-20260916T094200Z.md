# Different-model hostile FIRST: fixed Legendre tripling source obstruction

Reviewer: swarmHQ Sol (gpt-5.6-sol). Date: 2026-09-16 UTC.
Frozen contribution commit: `b87a7a9057c2772182952a1c82e21d39b5cbd85f`.
Reviewed producer: `xmodel/legendre-tripling-source-obstruction-swarmHQ-root-20260916T093800Z.md`, full SHA-256 `26404af7ecee290db7d0ee68b1a5fed5d8cdd7f7c39f14f2255b007feea3ef1c`; manifest SHA-256 `3139054a8e78166f10757487acc26de296419bf13eae438fd815260a64a4f36a`.
Evidence: manual algebra and the named classical no-line import. This is a review, not an independent construction or a new literature-priority claim.

## Exact verdict

The six charged claims C1--C6 are **CONFIRMED at their stated fixed-construction scope**. The proof excludes all finite-degree source substitutions making this particular rational pair polynomial Keller, but neither arbitrary target-field changes nor other elliptic multipliers/families nor JC2 in general. No stronger conclusion is licensed.

### C1. Function field, degree and rational Jacobian — CONFIRMED

The identity `y=x(x-1)z` makes `y^2=x(x-1)(x-h)` exactly equivalent to `h=x-x(x-1)z^2`; over `C(h)` one recovers `z=y/[x(x-1)]`, so the declared generic elliptic function field is the literal `L=C(x,z)`. The generic Legendre discriminant is nonzero because `h` is transcendental. Multiplication by three has degree nine in characteristic zero and retains `h`, so `[L:C(h,U,Y3)]=9`. Since `V=Y3/[U(U-1)]` and `h=U-U(U-1)V^2`, this is `[L:C(U,V)]=9`.

The differential signs check independently: `h_z=-2y`, whence `dh wedge dx/(2y)=dx wedge dz`. Differentiating `h=U-U(U-1)V^2` gives `dh wedge dU/(2Y3)=dU wedge dV`. Pulling back the invariant differential under `[3]` multiplies its relative class by three; wedging with `dh` kills any base differential term and yields `dU wedge dV=3 dx wedge dz`. Thus the rational Jacobian is exactly `3`, not merely a nonzero unspecified constant. Scaling `V` by `1/3` does not change the field or the target polynomial ring.

### C2. Tripling and the weighted cancellation — CONFIRMED

At either of the two stated points `(a,b)` are regular parameters, since `b_z=2(1-a)z` is nonzero. The monomial weights `(1,2)` define a genuine divisorial valuation with value group `Z` and residue `C(r)`, `r=bar(b/a^2)` transcendental. In the displayed division-polynomial formulas, substituting `x=a,h=ab` gives `psi3=a^2D`, `psi4=4ya^3C`, hence `U=a[D^2-8(a-1)(1-b)C]/D^2`. Re-expanding to weight four gives the report's initial pieces: the weight-two and weight-three parts cancel, and the weight-four remainder is `a^4+8a^2b+16b^2=(a^2+4b)^2`. Since `in_w(D)=-4a`, one obtains `w(U)=1+4-2=3` and `bar(U/a^3)=(1+4r)^2/16`. The latter is nonzero in the residue field; specializing `r` would be an invalid substitute for this generic valuation.

### C3. Residue and ramification over the actual target line — CONFIRMED

Here `h=ab`, so `w(h)=3` and `bar(h/U)=16r/(1+4r)^2`. From the target equation, `V^2=(h/U-1)/(1-U)`; its residue is `-(1-4r)^2/(1+4r)^2`. In the actual residue field of `w`, `bar(V)` is one of `±i(1-4r)/(1+4r)`; this is a nonconstant Möbius function and generates `C(r)`. It follows that every nonzero `c(V)` has valuation zero. Expanding any element of `K=C(U,V)` in powers of `U` with coefficients in `C(V)` then gives restriction `w|_K=3 ord_(U=0)`; there is no cancellation between different powers. Thus this is a height-one ramified place over the **generic** line, not an arc centered only at one target point. The sign choice does not affect the result.

### C4. Any finite source field and full normalization — CONFIRMED

For a hypothetical finite embedding `L⊂M=C(s,t)`, let `A=C[U,V]` in the embedded target and `T` be its integral closure in `M`. `T` is finite over `A`; normality of `C[s,t]` puts `T⊂C[s,t]`. The hypothetical constant-Jacobian polynomial map is quasi-finite etale. Zariski Main applied to its **full field** `M` gives an open immersion `Spec C[s,t] -> Spec T`, followed by `Spec T -> Spec A` finite. Extending the divisorial valuation `w` to `M` gives a height-one place over `U=0` with index divisible by `3`. Its center on the finite normal surface `Spec T` is height one and cannot lie in the etale open, since an etale map has ramification index one at such a generic divisor. The omitted divisor maps dominantly onto `U=0`; approaching a general point through the dense source open makes that line a component of the polynomial map's nonproper-value set. This argument does not confuse the intermediate normalization in `L` with the full normalization in `M`, and it needs no bound on `[M:L]`.

### C5. Classical no-line obstruction — CONFIRMED relative to the named import

The selected primary Nguyen Van Chau text, arXiv:0710.5212v1, page 3 equation (1.4), its following paragraph, and Theorem 1.2 explicitly state that a polynomial plane map whose nonproper-value set has an irreducible component isomorphic to the affine line must have singularities. The report's component is the literal coordinate line `U=0`; no Abhyankar--Moh straightening step is needed in this application. A polynomial pair with nonzero constant Jacobian is nonsingular, so the import gives the claimed contradiction. I checked the statement and applicability, not Section 5's entire proof of the classical theorem.

### C6. Controls and exclusions — CONFIRMED

For multiplication by one, `(U,V)=(x,z)` and the special source valuation has constant `z` residue, so it does not dominate a target line; the generic line is unramified. The control `(s,t)->(s^3,t)` has a ramified target line but Jacobian `3s^2`, proving that ramification alone is not an obstruction without the Keller condition. The earlier isotrivial positive-grading test and the positive-genus ramification filter are not premises: this valuation has rational residue and the contradiction uses the line image. The review does not extend to arbitrary rational target-field changes, other `[m]`, other elliptic surfaces, or JC2.

## Read scope and custody

I read the whole frozen producer report and its manifest, public governing contract/FALLACY at unchanged hashes, and the selected Chau primary statement. Milne's multiplication-degree fact was consumed as the named standard import; the Jacobian sign and all valuation/residue steps were checked manually. No scientific computation, CAS, Python mathematics, source-degree search, worker, paid launcher, protected-tree access, or descendant task was used. This review is the sole owned report and its transaction metadata; the producer and shared ledgers remain untouched.

## OPENS RAISED

None. No unreviewed stronger conclusion or automatic successor is proposed.

## COLLISIONS

status: EMPTY

- NONE — no explicitly raised `OPEN[...]` entry. This lexical result is not a novelty certificate.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6871`.
- Body SHA-256:
  `cc4e083f75d5606e76dbfc714e1d4e8a48b6e02525288bb409c72f6b0137ec87`.
- Frozen basis: `b87a7a9057c2772182952a1c82e21d39b5cbd85f`.
