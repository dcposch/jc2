# D125 unguarded zero-k boundary and a pure-power second-order obstruction

2026-09-07. **DESK PASS, strictly scoped.** There is an explicit dependent-polynomial family on the unguarded k=0 boundary. None of its named pure-power points (R_t³,R_t⁵) admits an order-two deformation with the prescribed moving faces and k itself as deformation parameter. This is not a guarded point, a complete boundary classification, a flatness claim, or an exclusion of the k≠0 client.

## 1. The actual boundary family

Use the accepted varying-face chart, with odd receiver polynomials, λ₂=0, λ₃=1, H=p²(p³+g³), and lift

    φ(g)=v⁻¹,  φ(p)=v⁴u−v−v⁻¹.

Forget the inverse guard for k, then specialize k=0. The lower prescribed coefficients are now zero; only their closed support envelopes, not nonzero Newton endpoints, survive. Set

    R=R_t=H+(t+3)g p²+t p³−(t+3)p.

The complete negative part of φ(H) is −3v⁻³−9v⁻¹. The other three terms cancel it exactly. The checker expands only this degree-five R and finds no negative power. In particular

    φ(R)(0,v)=−v(v²+1)(v²+t+4).

Every R monomial has total degree≤5, 5i−7j≤1 and i≤2j. Its total top is H, its unique (5,−7)-top is g³p², it is odd, and R(0,0)=0. Therefore, over Q[t,α,β,γ],

    A₀=R³+αR,
    B₀=R⁵+βR³+γR

obey the full unguarded k=0 contract: the allowed A/B polygons, origins, entire total faces H³/H⁵, and entire inner faces g⁹p⁶/g¹⁵p¹⁰. Indeed multiplication adds the inequalities; all lower powers have strictly smaller inner weight and total degree, while the maximal inner face of each highest power is the stated single monomial. Their φ-lifts are ordinary, and [A₀,B₀]=0 because both are polynomials in R. This proves every coefficient equation without expanding the degree15/25 pair. The Jacobian scalar c₀k³ is zero here, not a unit.

For the whole β₁₅ target shear, let

    s_t=[p¹⁵]R⁵=t⁵−20t³(t+3)+30t(t+3)².

This scalar follows from the three possible exponent selections in (p⁵+t p³−(t+3)p)⁵. The literal [p¹⁵]B₀ is s_t+β, so B₀→B₀−(s_t+β)A₀ gives β'=−s_t and γ'=γ−α(s_t+β). Merely deleting a βR³ term is not that whole shear.

## 2. Precise deformation statement

Fix any characteristic-zero field K and t∈K. Suppose polynomials over K[k]/(k³) have

    A=R³+kA₁+k²A₂,   B=R⁵+kB₁+k²B₂,

with the fixed complete total faces, odd parity, zero origins and moving inner faces of the normalized chart. Then deg A₁,A₂≤13 and deg B₁,B₂≤23. In particular the (5,−7)-leading form of A₁ is exactly g²p, of weight3. The B₁/B₂ prescribed inner terms are respectively (5/3)g⁸p⁵ and (5/9)g. Require [A,B]=−5k³g²/9 modulo k³, equivalently zero through order two. These assumptions are inconsistent.

This is a receiver-polynomial obstruction: the proof does not need additional first/second-order lift equations. The parameter is k itself, not an unspecified ramified substitution k=s^m. Higher boundary families with α or γ nonzero are not covered by the proof below.

## 3. Centralizer and exact order identities

The only imported theorem is Arzhantsev–Petravchuk, *Closed and Irreducible Polynomials in Several Variables*, arXiv:math/0608157v2, [Lemmas4–5, p.5](https://arxiv.org/pdf/math/0608157v2): in characteristic zero, commuting nonconstant two-variable polynomials are algebraically dependent, and algebraically dependent polynomials lie in a common polynomial algebra K[S]. These statements, including the proof of Lemma5, were read directly; Lemma4's cited differential criterion is accepted at external-theorem trust, not independently reproved.

They imply the centralizer of R is K[R]. For R=F(S), prime degree5 gives either deg F=1 or deg F=5 and deg S=1. The latter would make H a scalar fifth power of a linear form, impossible since its p-adic multiplicity is2. Thus S is affine in R. Constants cause no exception. This argument works for every t and over the given K, not only generically.

The coefficient of k in the bracket is

    R² [R,3B₁−5R²A₁]=0.

K[g,p] is a domain, so 3B₁−5R²A₁=f(R). The left side is odd and has degree≤23, while deg R=5. Hence

    f(R)=aR+bR³.

The coefficient of k² is [R,E]=0, where the correct expression is

    E=3R²B₂−5R⁴A₂−(5/3)R A₁²−(1/3)f'(R)A₁.

The root seed omitted the last factor1/3. Indeed B₁=(5/3)R²A₁+f(R)/3, and differentiating [A₁,B₁] gives precisely that factor. A direct small-polynomial bracket control rejects replacing it by1. The centralizer gives E=h(R); the fixed origin implies h(0)=0.

If a≠0, reduction modulo R gives −aA₁/3=0 modulo R, hence R divides A₁.

If a=0, f'=3bR² and E is divisible by R. Divide E=h(R) by R:

    3RB₂−5R³A₂−(5/3)A₁²−bRA₁=h(R)/R.

Evaluating at the origin kills the constant term of h(R)/R, since A₁(0)=R(0)=0. Reducing this identity modulo R then gives R divides A₁². No possible linear centralizer term has been silently discarded.

## 4. Squarefreeness and the impossible face

Write

    R=pT,  T=p⁴+g³p+(t+3)gp+t p²−(t+3).

For t≠−3, p is coprime to T because T mod p=−(t+3). Also T_g=p(3g²+t+3). No nonconstant factor of the polynomial 3g²+t+3 can divide T: its p⁴ coefficient is1. Thus gcd(T,T_g)=1, so T and R are squarefree. Consequently R|A₁² implies R|A₁.

At t=−3, R=p²C with C=p³+g³−3p. The polynomials p and C are coprime. Also C_g=3g² and C(0,p)=p³−3p≠0, so C is squarefree. Hence R|A₁² implies rad(R)=pC divides A₁.

For t≠−3 the unique weighted leading monomial of R is g³p²; at t=−3 that of rad(R) is g³p. A polynomial divisor's leading form divides the product's leading form for the weight (5,−7), even though one weight is negative. Neither g³p² nor g³p divides A₁'s required leading monomial g²p. This contradicts both cases above and proves the stated order-two obstruction for every t.

## 5. Controls, history and stop boundary

Eight capped standard-library runs pass: normal/−O outputs agree byte-exactly; changing the actual R coefficient destroys polynomiality, changing the f' factor breaks the same bracket identity, and omitting all moving lower-face prescriptions admits the dependent jet

    A=R³+kR, B=R⁵+(5/3)kR³+(5/9)k²R  (mod k³).

That jet satisfies the other conditions by the proved functions-of-R/support argument, but its three moving lower-face coefficients are zero, not1,5/3,5/9. The actual face verifier rejects it; the omitted-face mutation accepts it and is caught. No full A/B power expansion is used for this control. The scripts also check the exact squarefreeness input identities, exceptional factorization, H's simple root, weighted leaders, and scalar shear coefficient. Zero Assert nodes; each command≤30wall/25CPU seconds,512MiB. Witness SHA256 `fac3910177f640869e69517e266126ce08f54f0950061e4b50a5eada53f336ee`.

The bounded checksum of named canonical files found a TD6 boundary-deformation entry, but it is a different source/pole-field client. No exact R_t or this moving-face obstruction was found in that scoped check; no priority or exhaustive-history claim follows. Primary versions, input hashes and exact reading scope are pinned in the owned evidence box.

**STOP:** an explicit non-Keller boundary family and a field-level order-two obstruction through its pure-power subfamily are established. No claim about the remaining α/γ centers, all k=0 points, ramified approaches, generic-fiber emptiness, guarded-N properness, solver cost or JC2 follows. All owned writers finish at custody publication; no worker or process remains.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7727`.
- Body SHA-256:
  `cd1c836239bef98b280c548b6d20d2bcf284f86e4cd82f0066d88f8fbf7005b2`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
