# Independent centre/radius/face audit — 2026-09-05

This is an independent sub-audit of gate parts (1) and (3), using the frozen charged PDF and engine. It does not edit a ledger or claim a solver result. The parent mechanically verified all seven charged hashes before delegation. `moh-layout.txt` is a fresh `pdftotext -layout` extraction of `/tmp/jc2-lane.8Gzrci/inputs/moh1983_jram340_configurations_of_roots.pdf`. The PNGs `moh-p149.png`, `moh-p161.png`, `moh-p167.png`, `moh-p179.png`, `moh-p191.png` were rendered from that same PDF and visually inspected; these check the formulas which OCR omits. `centre_radius_exact.py` independently checks the rational arithmetic, support enumeration, and face coefficient comparison; its output is `centre_radius_exact.json`.

## 1. The numerical radii: the source δ₂ is 1/3

Moh Def. 5.1(3), printed p.179, is the explicit product formula in the inspected `moh-p179.png`; OCR anchor `moh-layout.txt:2131`–`2135`. With

```
n=99, M=(-66,77,97), d=(99,33,11,1), V₂=V₃=8,
```

the formula gives

```
δ₃ = 1−(99−97)/(99−97−1) = −1,
δ₂ = 1−(99−77)[8(99−97)−11]/[(99−97−1)[8(99−77)−11]]
   = 1−22·5/165 = 1/3,
δ₁ = 1−165·[8·22−33]·[8·2−11]/[1·(8·165−33)·(8·22−11)]
   = 1−(165·143·5)/(1287·165) = 4/9.
```

The source δ₂ cannot simultaneously be 4/3. The 4/3 belongs to the homogenized coordinate `z=ty−1`, where `t=x^{-1}`. Multiplication of the difference of two y-roots by t increases its order by 1. Therefore the D₂ z-radius is `1+δ₂=4/3`, and the D₁ z-radius is `1+δ₁=13/9`. They produce `t=s³,z=πs⁴` and `t=e⁹,z=αe¹²+Πe¹³` after constant-centre removal. The older labels in the prompt must be read with this coordinate distinction.

Moh p.201 (8) only defines denominator increments: `L_j=lcm{den δ_s,...,den δ_(j+1)}` and `A_j=den(L_j δ_j)` (`moh-layout.txt:3288`–`3291`; the faithful transcription in `box/moh14-20260905/moh_skeleton_full.py:21`–`31` corroborates the displayed source). Here

```
L₂=1, A₂=3;  L₁=3, A₁=3;  full inward cover denominator=9.
```

This definition alone is not a theorem that every truncated centre belongs to `(1/L_j)Z`. The assertion in frozen `d108-center-opus5-20260905.md:61`–`66` needs an argument about the disc orbit. In this row one can supply a short proof stronger than the slogan.

## 2. Centre lemma proved from the 72-root majority disc

Moh Def.5.1(4), p.179, writes the unique general point as `σ_i=Σ a_jt^j+πt^(δ_i)` (`moh-layout.txt:2137`–`2138`). By the generic-disc discussion and Prop.1.2, p.147 (`moh-layout.txt:373`–`390`), the centre is truncated strictly below δ_i, and a polynomial's generic-point multiplicity equals its root count in the disc. Def.5.1(1), p.179 (`moh-layout.txt:2120`–`2124`, verified on PNG), gives for g the D₂ count

```
(n/d₃)V₃ = (99/11)·8 = 72.
```

Take one finite Puiseux cover containing all g-roots and the centre terms. Every cover Galois automorphism fixes g and the valuation, so it sends D₂ to a same-radius disc containing 72 roots counted with multiplicity. Two equal-radius ultrametric discs are identical or disjoint. Disjointness would demand at least 144 of the 99 roots. Consequently every Galois automorphism fixes D₂.

Uniqueness of the truncated generic-point centre then says that every exponent below δ₂ occurring with nonzero coefficient is integral: a term with nonintegral exponent is moved by a suitable root-of-unity automorphism, giving a distinct truncated centre and hence a distinct disc. This includes ALL possible terms with denominators dividing 9; no inner cover can introduce such a term into the earlier, invariant D₂ centre. A denominator dividing 9 in the inward cover is not inherited ramification of an outer disc.

With the leading major line already y=x and total-degree normalization in place, the y-centre exponents lie in `[-1,1/3)`. The only integers are −1 and 0; the former has coefficient 1 fixed by the placed leading line. Thus

```
σ₂ = t^{-1}+a₁+πt^{1/3},
z = ty−1 = a₁t+πt^{4/3}.
```

This proves the claimed one-dimensional centre lemma for the actual (99,66) tower. It does not assume it. Its proof uses g's 72 roots; it must not identify the auxiliary degree-11 h₃ with Moh's characteristic polynomial T₃ (degree 145).

The trace η of the source-support theorem does not remove fractional terms. In `xmodel/moh-hsupport-gate-astra-20260905.md:98`–`106`, `η=−[y^(N−1)]Q/N∈k[x]`, and its action centres the OUTERMOST common disc. Its Laurent exponents are integers ≤0, so it cannot cancel a nonintegral exponent. That theorem explicitly does not assume inner D₁ centering (`:78`–`87`). The absence of fractional terms here follows from the majority-disc proof, not η. Also, the D₁ substitution `e¹²+Πe¹³` in `xmodel/g9966-outer-bridge-grok46-20260903.md:145`–`148` is a specified inner Puiseux centre, not the polynomial trace η.

## 3. The K₂ face has the correct threefold conjugacy

At D₂, the multiplicity of g is 72; at D₁ it is `(99/33)·8=24` (Def.5.1(1)). The reduced common factor at D₂ has degree `V₃d₂/d₃=24` and the selected child factor has multiplicity `V₂=8`. Equivalently, for the canonical cubic approximate root h₂ of g, the respective multiplicities are 24 and 8 when the complete coherent system is used (Moh Thm.1.1, p.149; `moh-layout.txt:478`–`482`).

After centring D₂, its denominator increment A₂=3 makes nonzero residue α occur with the orbit `{α,ωα,ω²α}`. The zero-root alternative is impossible for multiplicity 8: the weight-96 K₂ face has only q divisible by 3, so its multiplicity at zero is divisible by 3. Three nonzero conjugates of multiplicity 8 exhaust degree 24. Therefore, with β=α³≠0,

```
face_D₂(K₂) = (π³−β)^8.
```

This is the source-compatible conjugate structure. Setting β=1 requires the separate scale gauge, which this sub-audit leaves to the gauge ledger. The frozen engine implements it literally in `/tmp/jc2-lane.8Gzrci/inputs/band_engine.py:364`–`372`: the q=24 top coefficient is 1, and `(r,q)=(4k,24−3k)` receives `(-1)^k binom(8,k)`, for 1≤k≤8. Under `t=s³,z=πs⁴`, all these terms have weight96 and sum to `(π³−1)^8`. There is no D=108-style wrong conjugacy in K₂.

## 4. Radius 32 is right; making its h₃ face strict is a separate, fatal issue

At a generic D₂ point, a degree-11 quasi-approximate h₃ with eight roots in D₂ and three in the other leading cluster has

```
ord_t h₃(σ₂)=8·(1/3)+3·(−1)=−1/3,
ord_s K₃=3(11−1/3)=32,  K₃=t¹¹h₃.
```

The generic transcendental π gives exact orders for the individual factors, so 32 is an exact order, not merely a lower bound. In the 66 lower polynomial slots, fresh enumeration gives 43 weights below32, two at32, and21 above32. The equality slots are `(4,5)` and `(8,2)`. Their coefficients give the most general centered face

```
P(π)=π⁸+aπ⁵+bπ².
```

The frozen engine `band_engine.py:242`–`253` retains only weights≥33 for its lower terms, hence sets a=b=0. Frozen centre report `d108-center-opus5-20260905.md:266`–`269` calls 33 “face weight32 made strict,” but that phrase does not license deleting the equality coefficients. The old necessity dossier `xmodel/g9966-chart-necessity-opus5-20260903.md:459`–`462` asserts a pure eighth power by citing Moh Prop.4.4/6.1. The printed Prop.4.4 conclusion is about g,T₁^ψ,...,T_r^ψ (`moh-layout.txt:1526`); Prop.6.1 concerns g and characteristic T_i in minor discs (`:2727`–`2762`). Neither names the canonical degree-11 h₃. Substituting h₃ for a characteristic T is an unproved variable/object identification.

There is a stronger obstruction: the source's approximate-root coefficient theorem forces a NONZERO a.

Construct a coherent complete system of g-points at accuracy −3. D₂ is one point, with 72 roots and order−3. For each remaining root in the principal minor disc, shrink its root disc to the unique rational radius at which the generic order of g equals−3, merging duplicates. For a root τ the profile is `ν_τ(d)=Σ_ρ min(d,ord(τ−ρ))`, with roots repeated according to multiplicity. It is continuous, piecewise rational-affine and strictly increasing, starting at −99 when d=−1 and tending to infinity. The solution ν_τ(d)=−3 is rational and has d>−1. Two distinct selected discs cannot be properly nested, because strict nesting would strictly increase ν; thus they are equal or disjoint. After merging equal discs they exhaust the remaining27 roots. This is exactly the complete/coherent definition, p.148 (`moh-layout.txt:445`–`461`). The independent custody worker hostile-checked this completion argument.

Prop.6.1 applies to the principal minor branch at r=3: its multiplicity3 is ≤`d₃/(n−M₃)=11/2`. Every selected minor point has ord g=−3<0 and is therefore a distribution detector for `g,T₁^ψ,T₂^ψ` by Prop.6.1(2), p.191 (`moh-layout.txt:2754`–`2762`, inspected `moh-p191.png`). Their degrees are 99,66,55, giving ratios9:6:5. The 55 is reproducible from Moh’s characteristic arithmetic: q₁=−66, q₂=77−(−66)=143, λ₂=99q₁+33q₂=−1815, μ₂=λ₂/33=−55; Prop.2.2 identifies degree T₂ as −μ₂ (the auxiliary formulas occur on printed p.150, `moh-layout.txt:572`–`582`, and the degree identity on p.152). Def.3.1(4), p.161 (`moh-layout.txt:1155`–`1172`, inspected `moh-p161.png`) makes the degree of each g leader a multiple of9. Thus every multiplicity in this complete coherent system is divisible by9.

Apply Thm.1.1 twice, first to g→h₂ and then h₂→h₃, using the canonical cube approximate roots. At these same points h₂ has accuracy−1 and h₃ accuracy−1/3, with the requisite divisibility by3 at each step. No unproved composition assertion that nested roots equal a ninth root is needed. Thm.1.2, p.149 (`moh-layout.txt:495`–`507`, visually checked `moh-p149.png`) now applies to

```
h₂=h₃³+C₂h₃+C₃,  deg_y C₂,deg_y C₃≤10,
ord_t C₂(σ₂)≥−2/3,  ord_t C₃(σ₂)≥−1.
```

Let `U=face_64(t²²C₂)` and `V=face_96(t³³C₃)`. The centered support proof makes U,V polynomials in π. Both have degree≤10 because the y-degree bound survives translation and homogenization. Their weight congruences sharpen this to `U∈span(π¹⁰,π⁷,π⁴,π)` and `V∈span(π⁹,π⁶,π³,1)`. Taking the weight96 face of the exact h₂-adic identity yields

```
(π³−β)^8 = P(π)^3 + U(π)P(π) + V(π).
```

`deg(UP)≤18` and `deg V≤9`. Compare π²¹ coefficients:

```
−8β = 3a,   hence a=−8β/3≠0.
```

The frozen/replayed charts set a=0 while fixing β=1. Thus their h₃ face slice does not receive the source data justified by the same approximate-root theorem. Releasing jet0 does not alter a. The correct radius32 does not imply the strict cutoff33; the latter removes at least one source-forced nonzero coordinate. This is a new face/support obstruction shared by both branches, separate from the repaired centre.

Do not automatically set b=20β²/9. The π¹⁸ coefficient also receives `U₁₀π¹⁰·π⁸`, so the local identity only gives `U₁₀=20β²/3−3b`. The first coefficient a alone already refutes the strict pure-π⁸ face. A safe enlarged repair would retain both equality coordinates, impose a=−8β/3 when the source C₂ floor is imposed, and leave b free until a further source or coefficient calculation resolves it.

The exact script confirms this comparison symbolically. It is a certificate about source-to-chart necessity, not a Keller counterexample or a solver rekill. Both arithmetic constants 6264 and64 can remain valid inside the old strict chart while its source necessity fails. The parent should withhold promotion unless a new source-complete face repair is actually replayed.
