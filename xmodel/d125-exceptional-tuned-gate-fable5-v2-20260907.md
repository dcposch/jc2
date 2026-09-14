# D125 tuned exceptional center: independent hostile gate (Fable 5.1, v2)

2026-09-07. **VERDICT: CONFIRMED** (proof correct as written, with typed dependencies and one scope remark). Independent hostile review of
`xmodel/d125-exceptional-tuned-discriminator-astra-20260907.md` (body SHA-256
`cc0561a9a74bfc35675c0c3139c51eea3b145491008cf8ba853fc412f27e29ef`, frozen
basis `0d39df3c`). Frozen inputs only: `/tmp/jc2-lane.11dUFq/inputs` (7 files).
Producer checker NOT run (v2 launcher note: shared basename `check.py`; helper
path unavailable). Independent stdlib controls only, under
`box/d125-exceptional-tuned-gate-fable5-v2-20260907/`.

## 1. Claim under review and what is NOT reviewed

Claim: over a char-0 field K, no arc of the accepted normalized odd moving-face source with all coefficients in K[[s]], k(s) of finite order m>=1 (any leading unit), center t0=-3, alpha0!=0 and delta0=gamma0-beta0*alpha0+5alpha0^2/9=0. Not reviewed and not claimed by the producer: the alpha0=gamma0=0 pure center, existence/degeneration/properness of any arc, a new global source identity, JC2. Consumed as dependencies (custody only, not re-hardened): 14c source facts ([g^2p]A=k, fixed faces A15=H^3/B25=H^5, [g^9p^6]A=1, odd lattices 5i-7j<=3 / <=5, target -(5/9)k^3 g^2, all A negative rows), 14f field-point form A0=R^3+alpha0 R, B0=R^5+beta0 R^3+gamma0 R with R=R_{-3}=p^2(p^3+g^3-3p), the polynomial centralizer K[R], and 14g's exact a01=0 (k^2 a01=-(9/5)r0 in the domain K[[s]]). The producer checker was NOT run (v2 instruction); all evidence below is from the seven frozen files and my own controls.

## 2. Identity (I): verdict

CONFIRMED. With f(z)=z^3+alpha z, b(z)=5z^4+3beta z^2+gamma, a_s=3R^2+alpha, q_s=5R^2/3+beta-5alpha/9, delta_s=gamma-beta*alpha+5alpha^2/9 one has b=a_s q_s+delta_s and q_s'=10R/3 (C1 gate `b-equals-aq-plus-delta`). Expanding [f(R)+F, b_int(R)+q_sF+G] termwise: [f(R),.]=a_s[R,.], [R,q_s]=0, [F,q_sF]=-(10/3)R F[R,F], so [A,B]=a_s[R,G]-delta_s[R,F]-(10/3)RF[R,F]+[F,G]=[R,a_sG-delta_sF-(5/3)RF^2]+[F,G] since [R,RF^2]=2RF[R,F]. Hand-derived and replayed exactly on two formal generators (R=g and R=g+p^2, three random trials each, moving alpha/beta/delta series, [F,G]!=0 enforced). Mutations `--mutate-wrong-quadratic` (-5/9), `--mutate-omit-cross`, `--mutate-zero-cross` (F,G in K[R], which would make the omit-cross test vacuous) fail at the named C1 gates in normal and -O. F bookkeeping also confirmed: [p]F=[p]A=0 (a01=0 exact), [p^3]F=[p^3]A+3alpha(s)=0 by the definition alpha=-[p^3]A/3 with [p^3]R=-3 and [p]R=[g^2p]R=0 (C3 `R-low-coeffs`), [g^2p]F=k(s), F0=0, so 1<=j<=m; deg F<=13 and w<=3 from the fixed faces and oddness; each F_i is ordinary because phi(R) is ordinary (C3 `R-lift-ordinary`, actual degree-5 expansion) and the A negative rows hold coefficientwise in s. All coefficient equations used sit at orders <=2j<=2m<3m.

## 3. Reference removal (K) and the finite induction of §4

CONFIRMED. (K) is exact: changing beta,gamma by eta s^l, theta s^l changes q_s by eta s^l, hence G by -eta s^l R^3-theta s^l R-eta s^l F and delta by theta s^l-eta s^l alpha(s); A,B untouched; (I) re-holds with the new references (C2 gates, mutation `--mutate-omit-reference-betaF` fails at `C2-reference-G`). Kernel step: [R,a0 G_l]=a0[R,G_l]+G_l[R,a0]=a0[R,G_l], and a0!=0 in the domain K[g,p], so [R,G_l]=0 and the accepted centralizer gives G_l in K[R]; deg<=23<25 and oddness (R odd, powers independent) give eta R^3+theta R. Order audit, every intermediate order, replayed by hand: (i) l<j: delta F has order >=j+1, F^2 >=2j, [F,G] >=j+1, alpha_i multiply already-removed G's; F corrections land at >=l+j>j-1. (ii) first nonzero delta_d, d<j: at l in [j,j+d-1] the delta-indices are <=d-1 (zero, delta0=0 included), F^2 at 2j>l, [F,G]_l uses G_0..G_{d-1}=0; the removals change delta only at orders >=j>d; at j+d the sole delta term is delta_d F_j, giving [R,a0 G_{j+d}-delta_d F_j]=0 and Sect.3's linear consequence F_j=0. (iii) l in [j,2j-1]: same, and (K) at l>=j keeps delta zero below j. Result ord delta>=j, ord G>=2j with the induced delta_j and the -eta_j F_j shift of G_{2j} both retained. C6 checks the index inequalities on a grid m<=8 (bookkeeping only; the uniform statement is the displayed inequalities). Scope remark, not a defect: branch (ii) with d=0 is exactly the untuned case delta0!=0, so Sects.3-4 alone already prove the alpha0!=0, delta0!=0 obstruction; the producer correctly does not claim this and the live untuned theorem is not a premise here.

## 4. Order-2j fiber composition (§5) and zero lemma (§3)

CONFIRMED. (Q): at order 2j the alpha_i terms multiply G_1..G_{2j-1}=0, the only delta term is delta_j F_j, (F^2)_{2j}=F_j^2, and [F,G]_{2j}=sum_i [F_i,G_{2j-i}] with 2j-i<=j so every G there is zero: [F,G] drops by the PROVED ord G>=2j, not identically. Irreducibility of R-r, r!=0: as a cubic in g over Kbar((p)) after dividing by p^2 the constant is p^3-3p-r p^{-2} of valuation -2 (at t=-3 the g-coefficient is 0, so the valuation set of a root of valuation n is {3n,-2}, never balanced); no root, cubic irreducible over Kbar(p); content gcd(p^2,p^5-3p^3-r)=1 (constant -r); Gauss (C4). In the domain Kbar[g,p]/(R-r): a0=0, so (5r/3)F_j^2+delta_j F_j+h(r)=0 with leading coefficient -5r/3!=0 (alpha0!=0 used); it splits over Kbar and a domain forces F_j = a root. sigma=(-g,-p) sends (R-r) to (R+r) and F_j to -F_j, so the constants are opposite (C7 toy on R=g); with c=c_r/r, F_j-cR lies in (R-r) and (R+r), non-associate primes (2r!=0), so (R^2-r^2)=a0/3 divides it: F_j=cR+a0U. Zero lemma: w(a0)=2 (C3 `weight-a0`), deg a0=10, so U odd, deg<=3, w<=1, slots exactly p,p^3,gp^2 (C3 `U-slots`, no polygon transport); phi(R)(u,0)=3u (C3 `R-lift-v0`) so the v^0 coefficient of phi(a0) is the nonzero polynomial 27u^2+alpha0 (nonzero for every alpha0), hence phi(U) ordinary by lowest-v-power comparison in the domain K[u]; complete negative rows (0,-1,1),(-1,-3,2) (C3 `lift-negative-rows`, cubic lifts only) force U=dS; [p]Z=-alpha0 d then [p^3]Z=-3c kill d,c (C3 `low-rows-kill-c-d`; mutation `--mutate-low-p3` rejected). No squarefreeness of R=p^2 V and no R=0 fibre is used. The consequence lemma (odd h mod 3z^2+alpha0 has remainder lambda z, C5 random odd h) is correct. F_j=0 contradicts j=ord F.

## 5. Own controls, pins, replay, scope

Own `box/d125-exceptional-tuned-gate-fable5-v2-20260907/gate_controls.py` (SHA `de6a79c3…`, stdlib, 0 Assert nodes, 61 named gates) and `runner.py` (`6ba74698…`): 12 runs = normal/-O x {none, wrong-quadratic, omit-cross, zero-cross, omit-reference-betaF, low-p3}; positives exit 0 with byte-identical witnesses `45de42f6e5ac04c2a84450db98be669bdb95d77170134bb1721b0e4aa0812fbe`; each mutation exits 1 at its named first gate in both modes; 1.3 s wall total under 30 wall/25 CPU s/512 MiB per run (`replay.json`). Actual source expansions: degree-5 R and S, R^2 only for its weight, cubic lifts of p,p^3,gp^2 and the degree-5 lift of R; no R^3/R^5/A15/B25. `input_pins.txt` pins the seven frozen files; the frozen discriminator hashes `d0937ebe…` (matches the producer terminal) and its body seal is `cc0561a9…`. Finite grids (C4 n-range, C6 m<=8) and the C7 toy are bookkeeping, not uniform proof; the uniform steps are the hand derivations above. Producer `check.py` (frozen `ec6c1840…`) was read, not run: its identity gate uses a single formal R=g, its `lowcheck`/order loops are scalar/grid bookkeeping consistent with its own scope line; its witness `dbbcf4b8…` is a custody fact taken from root. Typed gaps (dependencies, uncharged): GAP-CENTRALIZER (A-P Lemmas 4-5 external trust via 14f), GAP-CENTER-FORM (14f field classification supplies A0,B0 and that the arc's s=0 point is an unguarded k=0 point), GAP-SOURCE-FACTS (14c/14g literal values listed in Sect.1), GAP-TRANSACTION (roots/receipts not in the frozen set). No exit-price claim, so no charge_basis line. No CAS, solver, AWS, SSH, network, live peer, ledger, protected tree or frozen-file edit; producer checker not executed.

## 6. Verdict table and corrections

| item | verdict |
|---|---|
| (I) exact identity, -5/3 factor, cross bracket retained | CONFIRMED (C1, two formal R, 3 named mutations) |
| F reference: [p]F=[p^3]F=0, [g^2p]F=k, 1<=j<=m, deg<=13, w<=3, ordinary | CONFIRMED |
| (K) exact reference change incl. -eta s^l F and delta_j | CONFIRMED (C2, betaF mutation) |
| Sect.4 induction over every intermediate order; delta_d persistence; ord delta>=j, ord G>=2j | CONFIRMED (hand index audit; C6 bookkeeping) |
| (Q) at 2j; [F,G] drops only by proved ord G>=2j | CONFIRMED |
| R+-r absolutely irreducible at t=-3; quadratic splits; opposite constants; F_j=cR+a0U | CONFIRMED (C4, C7) |
| Zero lemma: slots p,p^3,gp^2; 27u^2+alpha0 nonzero polynomial; U=dS; d,c killed | CONFIRMED (C3, low-p3 mutation) |
| Scope/stop clauses (no pure center, existence, properness, JC2) | CONFIRMED |
| Corrections | none required; remark: Sects.3-4 with d=0 already cover delta0!=0 (unclaimed); [R,a0G_l]=0 => [R,G_l]=0 needs the one-line domain step, implicit in the text |

**STOP/IDLE.** Review only; no promotion or deployment authority beyond the verdicts above.

<!-- BODY-END -->
