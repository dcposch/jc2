# Fable gate: D125 pure low-alpha discriminator (independent hostile review)

2026-09-07, 22:09–22:17 UTC. **Verdict: claims 1–6 CONFIRMED as stated; the
interval 2j/3 <= ord(alpha) < j remains GAP, exactly as the producer says.**
Replay: normal and -O stdout are byte-identical to the charged final witness;
all five mutations fail with the intended exception in both modes. Two
evidence-description defects in the checker are recorded in §3; neither
touches the theorem. This is review only: no launch, promotion, source
normalization, degeneration theorem or JC2 conclusion is drawn.

Inputs: the twelve frozen files under `/tmp/jc2-lane.TpVOVO/inputs`; hashes in
`box/d125-pure-low-alpha-gate-fable5-20260907/input-pins.sha256`. Main report
`e5416761…`, checker `6e3583de…`, helper `25be0862…` match the charge. The
four accepted reports (14c/f/g/v) were read whole and consumed only at their
imported trust (K[R] centralizer, first contact F_j=RC with C even, C(0)=0,
V∤C, ord G>=2j, ord delta>=j+1, j<m, low rows and their k-saturation). The
2200 blind round, the pure-uniform history report and its gate were not read.

## 1. Claim-by-claim verdicts

**1. Coefficientwise centralization — CONFIRMED.** I rederived identity (1)
from A=R³+αR+F, B=R⁵+βR³+γR+qF+G: a_s q_s − b_s = αβ−5α²/9−γ = −δ_s exactly
(the −5α/3 R² and +5α/3 R² terms cancel), and the F² term is
−(10R/3)F[R,F] = −[R,(5/3)RF²]. It holds for the moving R_s because scalar
series are constants for the (g,p) bracket. ord[F,G] >= j+2j = 3j and the
target −(5/9)k³g² has order 3m >= 3j+3, so [R_s,H] ≡ 0 mod s^(3j). The
induction is sound: [R,H_0]=0 gives H_0=b_0(R) by the accepted centralizer;
subtracting b_0(R_s) commutes with R_s exactly, leaves a multiple of s, and the
step repeats through order 3j−1. Every power of R_s is retained; H has
bounded (g,p)-degree, so each b_ℓ is a genuine polynomial.

**2. Generic-point embedding — CONFIRMED.** L is the fraction field of
Kbar[g,p]/(V), a domain by 14v §1. Φ(G)=R_s(G,p)−z lies in L[[s,z]][G];
Φ(g) ∈ (s,z) because R(g,p)=p²V=0 in L and h(0)=0; Φ'(g) ≡ 3p²g² mod s, a
unit of L since V divides neither p nor g. Hensel's lemma over L[[s,z]] gives
the unique root with initial value g and no negative powers. The root r_s of
−α/3 lies in Kbar[[s^(1/2)]] with order a/2 >= 1/2, so the substitution is a
continuous K[[s]]-algebra map preserving precision mod s^(3j); a_s ↦ 3r_s²+α=0
exactly, killing the G term. Division by p, g is only Hensel division in L,
not a source localization or coverage statement.

**3. Involution and nonconstancy — CONFIRMED.** σ(V)=−V, so σ acts on L;
R_s is odd, so −σ(g(s,z)) and g(s,−z) both solve R_s(G,p)=−z with initial
value g, and uniqueness gives σ(g(s,z))=−g(s,−z). Oddness of F then gives
σ(f_n)=(−1)^(n+1)f_n. With F_j=RC and R(g(0,z),p)=z, [s^j]f_0=0 and
[s^j]f_1=C|V. C|V ∉ Kbar: a constant c would satisfy C−c ∈ (V), evaluation at
the origin (which lies on V) forces c=0, contradicting V∤C. The n>=3 terms of
the σ-even part start at >= j+3a/2, so that part has exact order j+a/2 and
leading term ρC|V. Earlier-odd case: a nonzero σ-anti-invariant element is
never in Kbar. Equal-order case: the two eigencomponents cannot cancel, and
the invariant component is the nonconstant ρC|V. Kbar is algebraically
closed in L, so nonconstant means transcendental. U≠0, f finite, f<=j+a/2.

**4. Critical-root cancellations and (6) — CONFIRMED; interval GAP.** In the
field L((s^(1/2))) leading coefficients multiply, so at
e=min(d+f,a/2+2f)<3j the left side of (5) has coefficient −δ_d ψ,
−(5/3)ρψ², or their sum (equal orders), each a nonzero polynomial in ψ of
degree 1 or 2 over Kbar; equating it to the scalar coefficient of b_s(r_s)
would make ψ algebraic, hence constant. δ=0 is the d=∞ branch of the same
case split, and b_s(r_s) is scalar at every half-integral order. Hence
d+f>=3j and a/2+2f>=3j; with f<=j+a/2 these give 3a>=2j and d>=2j−a/2.
Nothing stronger follows: the §3 prefix has (j,a,f,d)=(8,7,11,14), satisfies
both inequalities and has a<j, so the method as written cannot close
2j/3<=a<j. No Pell identity is used anywhere in the surviving argument.

**5. Corrected scalar identity (7) — CONFIRMED.** With g=0 jets
R̄=p⁵+tp³−hp, [p]F=αh, [p³]F=0, [p]G=e+δh: [p]H=αe (the 3R²G and RF² terms
start at p³), and [p³]H = 3h²(e+δh) + α[p³]G + (5/3)α²h³ (from −(5/3)R̄F̄²
with R̄≡−hp). The right side is b1·t − b3·h³ since R̄² is even. The gauge
[p³]G=[p¹⁵]G=0 is reachable (matrix in (η,θ) has determinant t, a unit) and
says nothing about b3; the shorter advisory formula needs b3=0, a different
gauge that would move [p³]G. Correct as printed.

**6. Factored nilpotent prefix — CONFIRMED.** By hand: r'²−C=RM; H's
s¹⁶,s¹⁹,s²⁰ terms cancel pairwise between 3R²G and −(5/3)RF²; the s²²
coefficient is (5/3)R(RM+C−r'²)=0 and the s²³ coefficient is
(5/9)RC(RM+C−r'²)=0, so H ≡ 0 mod s²⁴. The replayed universal four-variable
identity confirms this. [F,G] starts at 24 and the target at 33, so (1) is
the full bracket mod s²⁴. Parity odd, origins zero, degrees <=11/<=21,
i<=2j and weight bounds hold; the only weight-3 A term is s¹¹g²p (from r'),
and the weight-5 B terms are exactly (5/3)s¹¹g⁸p⁵ (from (5R²/3)F) and
(5/9)s²²g (from M), matching k, 5k/3, 5k²/9 with k=s¹¹. All five generators
lift ordinarily (replayed witness), so A,B are polynomial. My independent
degree-3 truncated-jet control reproduces [p]A=0, y=−3s⁷, x=2s¹¹, k=s¹¹,
d=e=5s²²/9, hence x²−3ky=9s¹⁸+4s²² and e−5kx/9=−5s²²/9. The raw low rows
vanish mod s²⁴ (r_gp, r_p2 first appear at s³³, s²⁹) while the saturated
forms fail, because k is nilpotent and admits no inverse. The exact polygon
edges beyond these displayed constraints are not in the frozen inputs and
are taken at 14c/14f trust. No jet-to-arc inference is licensed or made.

## 2. Replay and custody

Fresh scratch subtree `/tmp/jc2-gate-fable5-scratch-1772257` containing only
the two byte-copied files at the repository-shaped paths; both hashes equal
the charge before and after every run, no bytecode written. Each child:
`timeout 30`, `ulimit -t 25`, `ulimit -v 524288`, `/usr/bin/python3 -B`
(plus `-O`). Positive stdout: `84d8b19b…` in both modes, equal to the
charged final witness bytes; stderr empty. The ten mutation runs exit 1 with
messages "universal pre-3j mixed identity" (delta sign, intermediate),
"actual scalar-kernel jet identity", "actual retained scalar cubic
coefficient", "nonconstant even leading transverse coefficient". A scratch
`--record` reproduced all twelve stdout hashes, return codes and modes of the
charged final-replay; mutation stderr hashes differ only through the
relocated traceback path. Zero Assert nodes confirmed. Outputs, commands and
`custody.json` are under `box/d125-pure-low-alpha-gate-fable5-20260907/`.

## 3. Evidence-description defects (checker only, theorem unaffected)

- The "actual scalar-kernel jet identity" uses Rjet=−hp−3p³ with h=3, which
  is no R_t p-jet ([p³]R_t=t=h−3=0). It is harmless because [p³]R_s never
  enters the left side of (7), and the retained-cubic check only exercises
  the right side; but the α[p³]G term is untested (Gjet has no p³ term) and
  the label "actual" overclaims. Verified by hand above.
- The parity toy sorts by p-exponent parity, not the σ total-degree parity
  the proof uses, and its "constant C" mutation is rejected by a hard-coded
  expected polynomial, not by a nonconstancy test. It does not evidence the
  C(0)=0, V∤C argument; that argument is confirmed by hand above.
- The "remaining interval" line is arithmetic on four literals; it records
  consistency of the countercontrol with (6), not an openness proof.

Nothing here changes a verdict. Necessary bound 3ord(alpha)>=2j: CONFIRMED.
ord(alpha)>=j: GAP, untouched. STOP/IDLE.

<!-- BODY-END -->
