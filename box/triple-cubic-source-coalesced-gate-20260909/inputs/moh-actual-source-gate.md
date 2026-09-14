# Hostile gate: positive-face slope screen on the actual Moh (25,15) receiver (Fable, 2026-09-06)

Lane `/tmp/jc2-lane.BKNySb`, basis `0d39df3c`. Charged report
`xmodel/positive-face-actual-receiver-discriminator-astra-20260906.md`, SHA-256
`07e53340…75c46` (verified whole-file), checker `check.py` SHA `e85416c7…22b9eb`
(matches the report's pin). Read whole: charged body and code; root Euler
composition `41a2efed…`; my own Euler gate `3eb7a6e5…`; row2515 order gate §§1–3,
5–7; top-face license §§2.2–3; Moh h-support gate §§1–4; FALLACY-v2. Primary
Moh text inspected in `moh-layout.txt` (Def 5.1 with its note, Prop 5.2 gloss,
Prop 5.3 statement and the opening of its proof, Lemma 6.1–Prop 6.4) and the
page images of printed pp.197–198 rendered from the frozen PDF. No live lane
file, D125 chain, AWS, CAS, solver, chart, ledger, FALLACY, external post or
`jc2-lean` access.

## Verdict summary

| Item | Verdict |
|---|---|
| Source centering (polynomial Q-mean, shear, constant b0) | CONFIRMED, conditional on the NAMED child-data transport |
| Entire zero-slope packet = D1' packet (10 P + 6 Q roots, contacts ≥ 7/5) | CONFIRMED from Def 5.1(1) and Prop 5.3's minimal-disc definition; monomial-J usage of Prop 5.3 NAMED, not re-proved |
| Face exhaustion: degrees 25/15, γ-degrees ≤ 15/9, endpoints (15,10)/(9,6), sole positive nonmonomial edge (1,1) | CONFIRMED |
| Equation (E): 5(4eh′−5e′h)=h, π \| E, root divisibility | CONFIRMED |
| [2,1] slope equation a²−a−1=0, a=3 branch excluded | CONFIRMED |
| [1,1,1] slope equation S=π³−γ³ | CONFIRMED |
| Q scaling (5/3)E, sign, monomial endpoints | CONFIRMED |
| Field-point vs scheme boundary | CONFIRMED as stated: K-point conditions only; no ideal membership, no nonredundancy |
| Independence from Moh Prop 4.6's boundary ODE | GAP (likely recovery, see §4) |
| Any partition or receiver excluded | none; count alone NO GAIN, as the report says |

Nothing in this gate is a receiver point, a chart cut, an exhaustiveness
claim or a K7 licence.

## 1. Controls

Supplied `check.py` run from a copy: 15 PASS normal and `-O`, 0.003 s. Own
`own_check.py` (SHA `00c27f7a…`, exact `Fraction` sparse polynomials, no CAS):
28 PASS normal and `-O`, 0.03 s, 17 MiB. Changed objects relative to the
producer: (i) the bracket is computed in the actual (γ,π) variables, not in
the pre-reduced z form, on random e,h and on every partition, for both the
P component H⁵ and the Q component H³; (ii) the [2,1] Euler system is solved
as a linear system in the five coefficients of e at a=2 and a=3 (both
inconsistent, rank 5) and for [3] (consistent); (iii) the three displayed
[2,1] rows are compared with the full residual on a 36-point rational grid,
and eliminated by hand to `row2 = 2(a²−a−1)/(5a(3−a))`; (iv) the π^0 defect,
face-exhaustion box enumeration over all primitive directions up to 12, and
a toy ultrametric replay of the mean-centering step. My first guess for the
eliminated constant, −2/(a(3−a)), was wrong; the exact value is 2/(5a(3−a)). Files: `box/positive-face-actual-receiver-gate-fable5-20260906/`
(`own_check.py`, `*_normal.out`, `*_O.out`, `moh-58.png`, `moh-59.png`,
`det-59.png`).

## 2. Claim 1: source centering and face exhaustion

**Named dependency.** The client is the licensed u_s=1 descent of the actual
(125,75; M=(−75,105,123); d=(125,25,5,1); V=(2,4)) parent, with the accepted
effective child datum (25,15; M2′=21, V2′=2; k=2) and radii δ2′=−1, δ1′=7/5
exactly as banked in row2515 gate §2–3 and top-face license §3. I retain this
as a dependency and do not re-derive it; the report also correctly refuses to
mix the (125,75; M2=90) sibling.

**Prop 6.3 read on the page image (p.197).** Hypotheses: deg g = deg_y g = n,
δ_s=−1, minor radius δ*_{s−1} ≥ v_s/u_s (supplied by Prop 6.4 at u_s=1, p.198).
Conclusions: (1) ḡ(σ), T̄_i^ψ(σ) ∈ k[γ,π]; (2) monic in π with π-degrees
u_s n/d_s, u_s(−μ_1)/d_s, … ; (3) J_{γ,π}(ḡ(σ), T̄_1^ψ(σ)) = −(u_s/b) γ^{v_s−u_s−1}.
With v_s=4, u_s=1 this is −γ²/b: exponent k=2 ≥ 0, c=−1/b ≠ 0, π-degrees
125/5=25 and 75/5=15. So the report's polynomiality, monicity, π-degree and
monomial-J inputs are the printed statement, not inferences. Determinant check
(p.198 image at 220 dpi): the printed matrix carries −1/(bγ^{v_s}) as the
∂x/∂π entry and the final fraction shows the exponent with reversed sign; both
are typos. From the explicit substitution y=θ^{−1}=γ^{−u_s},
x=(y−e−σ)/b with σ ∋ πθ^{v_s/u_s}=πγ^{v_s}, one gets ∂x/∂π=−γ^{v_s}/b and
det = −(u_s/b)γ^{v_s−u_s−1}, which is the statement. The report uses only the
statement, so this typo does not touch it.

**Outer-disc centering: CONFIRMED.** Def 5.1's note (p.179) says the minimal
disc D_s containing all roots of g·ΠT_j^ψ satisfies (1)–(4); for the child
this is D2′ of radius −1 containing every P and Q root. The Q-mean
η=−[π^{14}]Q/15 is polynomial in γ, the map π→π+η has determinant one and
fixes γ, and the ultrametric mean argument (division by 15 has valuation 0)
puts every P and Q root at t-order ≥ −1. This is the terminal h-support gate
§4 argument, cited correctly. Monicity plus elementary symmetric functions
give total degree ≤ 25/15, with equality from the π leaders. No D1 centering
is used, so the h-support gate §3 objection (nonzero D1 centre, x^5 control)
does not apply. The shear moving the selected slope to zero and the constant
translation π→π+b0 are again determinant-one, γ-fixing maps.

**Entire-packet claim: CONFIRMED with a named usage.** Def 5.1(1): in D_i,
g has (n/d_{i+1})V_{i+1} roots and T_j^ψ has (−μ_j/d_{i+1})V_{i+1} roots. For
the child at i=1: P has (25/5)·2=10 and Q has (15/5)·2=6 roots in D1′.
Prop 5.3 (p.180) defines D_{r−1} as *the minimal disc containing all roots
τ_i of g·ΠT_j^ψ with ord(τ−τ_i) > δ_r*, i.e. the whole residue class of the
major factor, and asserts the tower stays major. Its hypothesis is the
majority condition on V_r; here V2′=2 > d2′/(n′−M2′)=5/4, consistent with the
top-face license's major/minor rule. Hence the D1′ packet is exactly the set
of roots sharing the selected slope, contains 10+6 roots, and all mutual
P–P, Q–Q and P–Q contacts are ≥ 7/5. The report's identification of that
packet with the π^{10}, π^6 factors of H⁵, H³ is consistent (the license
normalizes the major slope to zero). NAMED, not re-proved here: Def 5.1/Prop
5.3 are printed for J=1; their use on the monomial-J child is how Moh himself
fills the transformed table on p.207 (radii −1 and 1/4, 7/6, 1/2 next to
Jacobians X, X²), backed by the p.169/p.171 remarks for Props 4.4/4.6. The
radii themselves are already inside the named child-data dependency; the only
new content drawn from Prop 5.3 is minimality of D1′, which is its definition.

**Galois stability and b0: CONFIRMED.** The packet is {ρ : ord_t(ρ−η) > −1}
with η ∈ K[t^{−1}]; automorphisms of the Puiseux closure over K((t)) preserve
ord_t and permute roots of P, so the packet is stable and its mean η0 lies in
K((t)). Order > −1 with integral exponents gives ord η0 ≥ 0, η0=b0+O(t).
For each packet root ρ of P or Q, ρ−η0 is the mean of ten differences of
order ≥ 7/5, so ord(ρ−b0) ≥ min(7/5,1)=1. The other 15/9 roots keep order
exactly −1 and nonzero slopes.

**Face exhaustion: CONFIRMED.** Each coefficient of π^a is ± an elementary
symmetric function of 25−a (or 15−a) roots, at most 15 (or 9) of order −1,
the rest of order ≥ 1; polynomiality in γ gives deg_γ ≤ min(15, 25−a) and
deg_γ ≤ min(9, 15−a). The coefficient of γ^{15}π^{10} is the product of the
fifteen nonzero slopes, nonzero; likewise γ^9π^6. My enumeration over the
support boxes {i ≤ 15, i+j ≤ 25} and {i ≤ 9, i+j ≤ 15} for all primitive
positive (r,s) with r,s ≤ 12 finds (1,1) as the only direction whose face
contains more than one lattice point, and the inequality in the report
(`ri+sj ≤ sN+(r−s)i`) proves it for all r,s. The advertised two-root weight
(1,3) is therefore monomial on this client. The mixed-sign direction tied to
7/5 is outside the positive theorem, as the report says.

Attacks that failed: (a) "the packet is a proper subpacket" fails against
Prop 5.3's minimal-disc definition; (b) "Q's zero-slope roots are not the D1′
Q roots" fails against Def 5.1(1)'s T_1^ψ count of 6 and the common slope
inside a radius-7/5 disc; (c) "η is the Q-mean, P roots could leave the disc"
fails because D2′ is defined on g·ΠT^ψ jointly; (d) the report never uses the
rejected h-width/order-prefix chart or its scalar shear.

## 3. Claim 2: the outer-face Euler equation

**(E) derivation: CONFIRMED.** With E=γ⁴e(z), H=γ⁵h(z), z=π/γ and the
convention [A,B]=A_γB_π−A_πB_γ, E_γ=γ³(4e−ze′), E_π=γ³e′, H_γ=γ⁴(5h−zh′),
H_π=γ⁴h′, so [E,H]=γ⁷(4eh′−5e′h) and [E,H⁵]=γ²H⁵ ⟺ 5(4eh′−5e′h)=h. Verified
bivariately on six random (e,h) and on every partition. The opposite bracket
convention only replaces E by −E and leaves every slope equation unchanged.
deg e ≤ 4 is the promoted theorem's bound at (1,1), l=3 after t=γ³; the
theorem is invoked on the full polynomial pair (P,Q), not on a face, which
is the load-bearing hypothesis I flagged in the earlier gate.

**π | E and root divisibility: CONFIRMED.** Adding a π^0 term cγ⁴ to E
produces a nonzero π^9 term in [E,H⁵] against a right side of π-order 10
(own control). At a root of h of multiplicity m, e·h′ has order m−1 unless
e vanishes there, while e′h and h have order ≥ m; so every root of h divides
e. This is exactly GGV Prop 2.11(1) transported, as in my earlier gate.

**[3]: CONFIRMED.** e=z(z−1)(−25z²+35z−7)/105 satisfies [E,H⁵]=γ²H⁵ and
[(5/3)E,H³]=γ²H³ bivariately; unscaled E fails for H³, so the 5/3 factor is
load-bearing. No slope freedom, no obstruction.

**[2,1]: CONFIRMED.** e=z(z−1)(z−a)(Az+B). The undivided identity
5(4Nh′−5N′h)−15a(3−a)h = 30z(a²−a−1)h holds exactly with
N=z(z−1)(z−a)((3−a)−5z). The three displayed rows agree with the full
residual on the grid, and eliminating them gives row2 = 2(a²−a−1)/(5a(3−a)),
so a²−a−1=0 is necessary and, off a ∈ {0,3}, sufficient at Euler-face level.
The a=3 branch: row3 gives B=1/(15a) ≠ 0 while row1 at a=3 forces B=0; my
direct linear solve at a=3 is inconsistent, so no solution hides behind the
denominator. Both golden roots avoid 0, 1 and 3, so the license's
noncollision factor Ω=a(a−1) is compatible.

**[1,1,1]: CONFIRMED.** Divisibility and degree force e=λ z s(z),
λ ∈ K^×, and 4eh′−5e′h = h(Az²+2Bz+3C) exactly (own control), so (E) reads
5λ(Az²+2Bz+3C)=1 ⇒ A=B=0, 15λC=1; one slope normalized to 1 gives C=−1,
S=π³−γ³, e=−z(z³−1)/15. Verified bivariately for both components. The other
two slopes are the primitive cube roots of unity.

**Monomial endpoints: CONFIRMED.** E=γ³π/(3B−A) works on γ^Aπ^B with
denominators 15,75,9,45. Every surviving positive face is Euler-compatible,
so no partition is excluded and no face is shown to extend to a pair. The
count alone is NO GAIN, as the report states.

## 4. Boundary, licensing, and redundancy

**Field-point vs scheme: CONFIRMED as stated.** Both slope equations are
statements about the K-points (a, or (a,b)) of an actual normalized pair.
Nothing here is an ideal-membership, nonreducedness or nonredundancy
statement about any chart ideal, and the report claims none.

**What it licenses.** Only radical point conditions. Adding a²−a−1 (in the
[2,1] stratum) or 1+a+b, a+b+ab (in [1,1,1]) to a complete necessary chart
is sound as V(I) ⊆ V(I+(…)) provided the chart's slope parameters are the
actual slopes in the same normalization (major slope 0, one nonzero slope 1,
top faces H⁵ and H³ after the p.198 coordinates and the three γ-fixing maps
of §2). It does not license a finite coefficient-field substitution as a
chart rewrite: a specialization a ↦ (1±√5)/2 must be run as a chart over
Q(√5), and conjugate values give conjugate charts, so emptiness of one is
emptiness of both; it must not be folded into a Q-chart's coefficient ring.
It authorizes no monomial deletion, no support change, no reverse Keller lift.

**Strongest surviving scope.** The slope conclusions need only: the named
child datum (radii −1, 7/5, V2′=2, M2′=21), Prop 6.3(1)–(3), the outer-disc
centering and the source-safe outer face H⁵/H³. Claim 1's full
positive-direction exhaustion is not needed for them; it is needed only to
show that no other positive face could add a constraint on this client.

**Redundancy: GAP.** Moh Prop 4.6 (p.171, monomial-J remark) supplies at the
top level a boundary polynomial q(π) of degree n′−M2′=4 tied to p(π) by a
differential relation, not merely the root-count corollary the top-face
license used (1+l ≤ n′−M2′). Here deg e ≤ 4 with z | e and every root of h
dividing e is exactly the shape of that q, and (E) is a first-order relation
between e and h. It is therefore plausible, and I could not exclude in this
slot, that a²−a−1=0 and S=π³−γ³ are Prop 4.6's ODE specialized to this row.
That would make the screen a recovery of a known constraint absent from the
frozen charts, not a new independent equation. Either way it is a valid
necessary point condition. The b=a+1 relation to F2 cubic data is a numeric
coincidence, not a source identification, as the report says.

## 5. Residual obligations

1. A Prop 5.3 monomial-J statement with the ℓ-shift is printed only as
   remarks plus Moh's own p.207 usage; it sits inside the named child-data
   dependency and is not re-proved here.
2. Redundancy with the Prop 4.6 boundary ODE is undecided (§4).
3. Any consumption must re-verify that the consuming chart's slope
   parameter equals the actual normalized slope; otherwise the point
   condition is misapplied.

No exit price is asserted here.

<!-- BODY-END -->
