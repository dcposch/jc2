# Source-image notes for own-child descent

Read-only frozen source: `/tmp/jc2-lane.wwyG4k/inputs/moh1983_jram340_configurations_of_roots.pdf`.
Root verified the charged hashes before delegation. Fresh local image reads covered
printed pp.179,197,198,199,202,207. PDF page number is printed page minus 139.
`p207.png`, `p202.png`, `p179.png`, `p197.png`, `p198.png`, `p199.png` are fresh
renders in this directory. OCR is `moh-layout.txt`; images govern formulas.

## Exact published controls

The p.202 source table gives six rows, with bracketed entries paired within
columns. It prints effective terminal M3=n−2 plus, for even n, the n−1 pair in
a separate M4 column. Thus the five u_s=1 inputs to p.207 are:

| n | m | effective source M | source V=(V2,V3) | source δ2 | source δ1 |
|---|---|---|---|---|---|
|64|48|(-48,52,62)|(3,3)|1/4|9/16|
|84|56|(-56,64,82)|(2,3)|2/7|16/21|
|84|56|(-56,72,82)|(5,3)|1/4|7/12|
|75|50|(-50,55,73)|(3,4)|1/5|1/2|
|75|50|(-50,55,73)|(2,4)|1/5|1/3|

The p.202 M4 entries are 63 for n64 and 83 for n84. They are the ineffective
n−1 pair, not an additional retained input to Prop.6.3. P.207 has:

| source | n′ | m′ | M′ | d′ including final gcd | V′2 | δ′2 | δ′1 | Jacobian |
|---|---|---|---|---|---|---|---|---|
|64/48|16|12|(-12,13)|(16,4,1)|3|-1|1/4|X|
|84/56, M2=64|21|14|(-14,16)|(21,7,1)|2|-1/2|7/6|X|
|84/56, M2=72|21|14|(-14,18)|(21,7,1)|5|-1|1/3|X|
|75/50, V2=3|15|10|(-10,11)|(15,5,1)|3|-1|1/2|X²|
|75/50, V2=2|15|10|(-10,11)|(15,5,1)|2|-1|4/3|X²|

Only M′2, not the full M′ or d′ tuple, is printed at p.207; the rest of each tuple
is its exact p.150 prefix-gcd interpretation. At p.207 Moh explicitly chooses
in the first case a major root σ=πt^(1/4) and a minor root
σ*=t^−1+a0+a1t+a2t²+πt³.

The p.207 introductory prose has an evident `(64,68)` typo; the source table
on p.202 and descendant 16/12 both give source 64/48. Do not make 64/68 a unit test.

P.202's sixth row is exactly
`(n,m)=(99,66), M=(-66,77,97), V=(8,8), δ2=1/3, δ1=4/9`.
There is no M4 entry. Its gcds are `(99,33,11,1)` and u_s=11−8=3.
Moh does not print its transformed data on p.207: he explicitly says he applies
Prop.6.4 to the first three degree cases, all with u3=1. If Prop.6.3's radius
hypothesis is independently supplied for 99/66, its retained labels are
`n′=27,m′=18,M′=(-18,21),d′=(27,9,3)`. The old published M=(-66,77,97) must
still be retained verbatim as the *source* identity. Calling (-18,21) the
printed p.207 99/66 child would be false. Calling the absence of 99/66 a
negative control for terminal-gcd closure would also be false: Prop.6.4 simply
does not apply when u_s=3.

## Source statements governing the interpretation

P.179 Def.5.1(1): a disc D_i contains exactly `(n/d_(i+1))*V_(i+1)` roots
of g, and exactly `((-μ_j)/d_(i+1))*V_(i+1)` roots of T_j^ψ for j=1,…,i.
Thus in a child chart V′_i is defined by the actual child disc D′_(i−1)
and the roots of the actual descended G, divided by n′/d′_i.
P.179 Def.5.1(2) includes V_(s+1)=d_(s+1) and
`V_(i+1)*d_i/d_(i+1) ≥ V_i > d_i/(n−M_i)`.

P.197 Prop.6.3 assumes source δ_s=−1 and the *minor-disc* radius
`δ*_(s−1)≥v_s/u_s`. With θ=y^−1, γ=θ^(1/u_s), and
`z=y−b x−e`, its substitution is `z=A(γ)+πγ^v_s`. The transformed polynomials
are monic in π with exact degrees
`u_s*n/d_s,u_s*(−μ1)/d_s,…,u_s*(−μ_(s−1))/d_s`.
P.198 Prop.6.4 supplies the minor radius if u_s=1; it does not cover u_s≥2.
P.199 Cor.6.1 covers the special constant-Jacobian descended case d_s=3,
M_s=n−2 and identifies scaled characteristic data. This corollary is not a
universal V-transfer theorem.

A typography hazard at pp.197–198 was checked at high resolution. P.197's
statement gives `J=−(u_s/b)γ^(v_s−u_s−1)`, agreeing with the displayed coordinate
map and p.207. P.198's determinant instead prints the π derivative as
`−1/(bγ^v_s)` and its final fraction as `−u_s/(bγ^(v_s−u_s−1))`.
Those proof displays are internally inconsistent with the map (and with each
other). Direct differentiation of the map gives
`x=(γ^−u_s−e−A(γ)−πγ^v_s)/b`, hence `x_π=−γ^v_s/b`,
`y_γ=−u_s γ^(−u_s−1)` and the statement's exponent. Fresh crops:
`p197-jac.png`, `p198-det.png`, `p198-jac.png`.

## Exact top inversion and what it does, and does not, determine

Normalize the source major tangent to zero and translate its constant centre.
The D_(s−1) source disc holds n*v_s/d_s > n/2 roots, so every equal-radius
Galois conjugate is the same disc. Its centre is rational. For positive
δ_(s−1)<1 the truncated centre is zero. Put

```
u=u_s, v=v_s, c=(n−M_(s−1))/d_s,
δ_(s−1)=(u*c−1)/(v*c−1)=a/b in lowest terms,
P=v*d_(s−1)/d_s.
```

At this disc Prop.4.6 gives G-leading polynomial p^(n/d_(s−1)), where
p has degree P. Write zero multiplicity z and nonzero b-orbit multiplicities
r1,…,rt; then `P=z+b*(r1+…+rt)`. Every nonzero orbit has an inverse initial
polynomial of degree a. Each inverse coefficient has exactly
`(n/d_(s−1))*rj` child G-roots. Its normalized top value is rj.
This statement counts cover roots under inversion of places; it does not
identify a source cover series with an inverse series. The projection
ratio is a/b, and there are a inverse coefficients per orbit, which must
not be merged.

The zero inverse coefficient has normalized count

```
W0=u*d_(s−1)/d_s − a*(r1+…+rt).
```

The source numerical row fixes P and a/b but may not fix z and the orbit
partition, or select a unique child major subdisc. Thus a naive declaration
that all child V equal W0, or all child V equal copied V, is unsupported.
One must enumerate compatible zero/nonzero route modes and sibling partitions,
then impose the child's disc/tower identifications. The raw top test threshold
is `W>d′_rawtop/(n′−M′_rawtop)` when the relevant monomial-Jacobian local
version of the major-disc theory is available. That threshold must not be
used to manufacture an attained multiplicity.

Controls directly from this calculation:

* Gate180/120 has a/b=1/6,P=10,z=4,(rj)=(1),d′_rawtop=2.
  Thus W0=1 and every nonzero inverse value is 1: exactly 15+15 G-roots,
  giving V′3=1 rather than copied 4. The source selected V3=4 is forced
  to be the zero factor because one nonzero 6-orbit of multiplicity4
  would need degree24>10.
* Gate96/72 has the analogous forced top 8+8 split and V′3=1 rather
  than copied3. Further source levels may fail a cumulative stabilizer
  condition; this top calculation does not assert source realization.
* Moh64/48 has p=(ξ⁴−a)^3; inversion gives 12+4 G-roots and V′2=3.
* Moh84/56,M2=64 has a/b=2/7,P=21 and the selected orbit multiplicity2.
  The selected source 42 cover roots produce twelve inverse roots, split
  into **two** coefficients of six each; each coefficient has V′2=2.
  Counting the twelve together would give the wrong answer4.
* Moh84/56,M2=72 requires the selected V2=5 to be nonzero: for s=3 the
  sole selected transition cannot stay zero by Prop.5.6. Thus z=1 and
  a nonzero orbit of multiplicity5 are forced, giving V′2=5. If one
  used only the numeric congruence admitting a zero selected factor5,
  one could falsely return child values3 or4, contradicting the print.

## A conditional route formula worth checking before implementation

Suppose the selected source route is zero through split indices
s−1,…,j+1 and has first nonzero coefficient at split j. For i>j put
`C_k=n*V_(k+1)/d_(k+1)` and `C_(k−1)=n*V_k/d_k`. The child root count in
the successive inverse zero-centre branch is

```
R_i=n′−Σ_(k=i)^(s−1) δ_k*(C_k−C_(k−1)),
W_i=R_i/(n/d_i).
```

Each summand is the exact source exit set at its first nonzero source
coefficient, converted by its projection ratio. For i≤j, local inversion
at a fixed nonzero selected coefficient preserves each individual disc
count, so its normalized value is the source V_i. This produces the
Gate180 values `(V2,1)` when the first nonzero split is j=2.
The formula is a geometric inversion calculation conditional on a valid
route; it is not a certificate that every numeric route is realizable.

Before the first nonzero coefficient, every zero-selected disc remains
fixed by the *full* source Galois group. Its centre is rational, and all
source δ_i<1. Consequently there is no hidden fractional centre term on
that all-zero prefix. Full reduced denominators of δ_i govern first
nonzero orbit sizes on that prefix; blindly accumulating the denominators
of earlier *zero* splits permits spurious routes. This is the issue
already observed on Gate96. Any finite-set API should distinguish a
necessary candidate set from an exact attainable set. An existential
`Tree.embeds(V)` witness is only an abstract route, never a polynomial
pair or proof that all proposed coefficient choices exist.

## Additional radius cross-check

P.202 really prints source75/50,V2=2 with bracketed δ1=1/3. This is another
numerical typo: substituting the same printed `(n,m,M,V)` in Def.5.1(3)
gives δ1=2/3 (the frozen enumerator also returns 2/3). The p.207 child
value δ′1=4/3 agrees with 2/3. Inversion below a first nonzero source
coefficient at exponent α gives

```
δ′_i=v−u*(α+1−δ_i)/α.
```

For α=1/5,u=1,v=4, δ1=2/3 this is 4/3. Using the p.202 typo1/3 would
produce −1/3 and fail the exact published child control. The source table
above is a literal transcription, not a replacement of Def.5.1(3).

## Independent first-nonzero candidate computation

`first_nonzero_candidates.py` imports the charged frozen enumerator and reads
the prior mechanically regenerated operative row dictionaries, then rebuilds
all degrees, gcds, radii and inverse zero counts independently. It checks
full-denominator congruences on the zero prefix and the first nonzero orbit
size. Optional q-simple-root capacity gives exactly the same output. It
DOES NOT discard candidate tuples by child count inequalities, and makes no
claim that these abstract candidates are realized by coefficients.

Its `first-nonzero-candidates.json` records all 1,420 rows, candidate and
rejected routes, defects, and controls. The necessary route filter has 323
singleton tuple rows, 2 double tuple rows, 1,095 empty rows. Empty by u_s:
`{1:888,2:200,3:5,4:2}`. They cannot honestly be called a new mathematical
kill count without promoting the cumulative-invariance and route-completeness
arguments. Gate96 has an empty full route set but independently determined
top value1, so an API must retain partial determined data despite an empty
full-tuple route set. Its gate row has forced V3=0-factor multiplicity3 and
at the next layer full denominator7, p-degree6: no nonzero selected
multiplicity4 orbit can fit.

The only two multiple tuples in this necessary first-centre model are:

* `(168,112),M=(-112,84,156,166),V=(1,5,3)` gives child
  `(42,28),M′=(-28,21,39),d′=(42,14,7,1)` and candidate
  `(V′2,V′3) ∈ {(1,3),(1,5)}`.
* `(192,128),M=(-128,160,172,190),V=(3,3,3)` gives child
  `(48,32),M′=(-32,40,43),d′=(48,16,8,1)` and candidate
  `(V′2,V′3) ∈ {(3,2),(3,3)}`.

For all 325 nonempty rows this model preserves V2 and satisfies root-count
upper bounds and nesting. Its 46 raw major lower-window defects occur at
zero-radius/dropped raw characteristic tails; check effective indices before
interpreting them. The result does not fill the missing values on empty full
routes by arbitrary integers from a cap.

## Corrected whole-source compatibility engine

The first-nonzero outer set above is intentionally incomplete as a source
configuration test. `box/lib/own_v_routes.py` now supplies the reusable
`OwnVRouteTree(source).compatible_first_support(j)` check. Its state L is the
actual denominator lattice of the common centre, not the lcm of every previous
radius. At a node of radius δ its cyclic orbit increment is den(Lδ). A zero
coefficient leaves L unchanged; a nonzero coefficient changes L to
lcm(L,denδ). An integral removable constant leaves the reduced all-zero danger
state true. Terms common between radii are in the inherited centre field, so
they do not enlarge L without a parting. Every above-threshold zero and nonzero
p factor must have a valid continuation, including nonselected siblings.
The original operative q-root count capacity, resonance exclusion, and bottom
conditions (12)/(13) are retained. Bottom all-zero towers fail the campaign's
reduced-source Prop.5.6 condition.

This source-only compatibility refinement examines the 327 preliminary routes
in 325 rows. It keeps 90 routes in 90 rows; 1,330 rows have an empty necessary
whole-source route set. The nonempty u histogram is
`{1:70,2:11,3:6,4:2,5:1}`; 25 of the nonempty rows have the raw dropped tail.
No pair or coefficient realization follows from a witness. Every retained row
has one necessary own-V tuple in this structural model. Neither preliminary
two-valued example survives: both 168/112 and 192/128 have compulsory sibling
constraints that fail with the actual centre lattice.

Driver `check_full_source_routes.py` banks witnesses and counts in
`full-source-routes.json`. Unit tests `test_own_v_routes.py` pass 6 tests,
covering all Moh-five controls, both Gate180 alternatives, Gate96's empty
complete route, both preliminary ambiguity examples, and the explicit Gate180
centre lattice `1 → 1 → 5`: the zero split at radius1/6 does not introduce6.

## Dropped-tail finite-pole check requested during the audit

A minimality-only argument must be handled carefully: p.180's actual printed
Prop.5.3 definition uses roots of `g∏_(i=1)^r T_i` for D_(r−1), hence includes
T_r, not only the retained T_1,…,T_(r−1). Fresh crop `p180-union.png` confirms
upper limit r. Thus minimality alone at r=s does not show that a retained
polynomial attains the radius0 split.

There is a stronger argument directly from Def.5.1(4) and Prop.4.6. A dropped
raw child tail is `u=1,n−M_(s−1)=d_s`, so the source radius δ_(s−1)=0.
Apply Prop.4.6 at the actual source disc D_(s−1) with r=s−1. Its q polynomial
has degree

```
Q=V_s*(n−M_(s−1))/d_s=V_s≥3.
```

That q is squarefree and is a factor of the leading polynomial of the RETAINED
T_(s−1); the accompanying p power has nonnegative exponent
`(−μ_(s−1)+M_(s−1)−n)/d_(s−1)`. This is an integer between 13 and 341
on the 90 operative dropped rows. Thus at least two distinct constant residues
are attained by roots of T_(s−1) at this source radius0. After any constant
translation at least one such residue is C≠0. On that branch x has a pole and
y→C. Under Prop.6.3's exact coordinate map, γ→γ0 with γ0^u=C^−1, so γ0≠0,
and `π=(y−b x−e−A(γ))/γ^v` has a pole. But the transformed T_(s−1) is monic
in π with coefficients in k[γ], by Prop.6.3(1),(2). It has no root with a
pole over a finite value γ0: in a monic equation the π^degree term would have
strictly smaller valuation than every other term, impossible.

This proves a separate incompatibility of a licensed polynomial descendant
with the source radius0 configuration. It does not claim that mismatching
raw/effective radius formulas alone is a contradiction. It uses the retained
T_(s−1), avoiding the p.180 root-union ambiguity. All 90 operative dropped
rows have u_s=1, so Prop.6.4 supplies the descent licence. None of this
requires a Keller pair to be exhibited.
