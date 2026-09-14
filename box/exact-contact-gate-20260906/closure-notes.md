# Independent sibling closure audit

Inputs: only the seven frozen files root mechanically hash-checked in this lane. Script `closure_fixed.py`; exact output `closure-fixed-results.json`. No producer code or artifact tree read. All rational arithmetic uses `Fraction`. This is a necessary packet/order/orbit computation, not existence of a Jacobian pair.

## The printed finite replacement for the depth cap

Moh p179 Def5.1 and its following note (moh.txt 2137–2148) say that **any** above-average subdisc may extend the tower. Prop5.3 p180 (2157–2184) applies to **any** factor of p of multiplicity V_r>d_r/(n−M_r), builds the next D_(r−1), and fixes its radius using the same global characteristic M_(r−1). Its pp180–182 proof rules out an earlier split at an intermediate M_r>L*>M_(r−1). The p200 theorem(4) restates the any-subdisc extension. Thus a complete fixed characteristic row has no free inserted characteristic exponent for sibling branches. Every major branch follows r→r−1 in the same global list, with its own V_r. At r=1, Prop4.6 gives D(n,−M1,g_sigma,T1_sigma)=nonzero constant (moh.txt1646–1648). Repeated roots or common roots would force the left side to vanish there; hence both leading patterns are squarefree and disjoint. This is a final major disc, and cannot continue as a major packet.

Consequently the report's arbitrary-W recursive search is unnecessary for these rows. A level2 sibling is forced final D1. A level3 sibling has one further nonfinal D2 and then final D1. The six rows have s=4. A cap of two disc transitions from their level3 sibling births already includes the whole legitimate major chain. The report's stated abstract depth cap nonetheless remains a cap unless this missing fixed-index theorem is supplied. No printed result justifies declaring arbitrary-W depths>2 impossible in its broader invented state space; the correct replacement is restriction to the fixed characteristic chain, not a numerical experiment at depth3 or4.

## Recursion and checks

At major node i use the source W_i=n−M_i. Given root count rho and packet invariant kappa,

    delta_i=1−W_i*kappa/(W_i*rho−m),
    abs(lambda_f)=m*kappa/(W_i*rho−m),
    P=rho*d_i/m, Q=rho*W_i/m, lo=d_i/W_i.

Enumerate p=pi^z product(pi^A−c_j)^r_j with P=z+A*sum(r_j), number of roots z>0 + A*len(r_j) ≤ Q, no multiplicity equal lo, some multiplicity >lo. For each nonzero orbit the A subtrees are Galois copies. Every major factor continues at index i−1; a minor factor contributes delta_zero−1 to the unsplit minor bound. Each major leaf contributes n*rho*kappa/((n+m)*rho−m).

Actual centre stabilizers are used: a zero factor retains L, and a nonzero factor changes L to lcm(L,den(delta_i)). Set A=den(L*delta_i). Final checks require both root counts congruent 0 or1 mod A, and do not allow both remainders1 (they would share the zero root). A=1 permits translating the origin and using z=0, avoiding redundant zero/nonzero descriptions. No primitivity A or invented cross-branch B is imposed. Selected source path V_i is required in the chosen factors. For these nine targets the selected factor types have no ambiguity of distinct stabilizers; repeating identical nonzero multiplicities makes equivalent choices.

The computed unsplit-minor outcome sets are:

| row | finite full outcome pairs (I_M,I_m) passing integrality and inequality |
|---|---|
| R001 | none |
| R009 | (8,8) |
| R025 | (12,8),(13,9),(16,6),(17,7),(21,5),(22,6) |
| R026 | (12,8),(13,9),(16,6),(17,7),(21,5) |
| R027 | (13,9),(17,7),(18,8),(21,5),(22,6) |
| R028 | (13,9),(17,7),(18,8),(22,6) |
| R050 | (8,8) |
| R057 | (18,6) |
| R058 | (18,6) |

These are sets of numerical pairs, not counts of unique tree configurations. Minor splitting can increase I_m; witnesses choose no additional minor split. No assertion of a realized polynomial pair is made.

## Explicit witnesses for all six claimed kills

The table below uses *actual* centre L values, including correct denominator shedding at zero factors. In n180,m120 rows the principal minor has rho_f=20 and delta=5, so it contributes4, with the universal baseline1. The forced top D3 has delta=1/6 and

    p3=pi^4(pi^6−c), P3=10,Q3=25, lo3=2/5.

It has six nonzero small children and one zero large child, both major. The small D2 children each have rho=10,kappa=5,L=6,delta=1/3,P=5,Q=4,A=1. Choose reduced multiplicities(2,3), which gives one final leaf of each of the first two types below. The zero large D2 has rho=40,kappa=30,L=1,delta=1/5,P=20,Q=16,A=5.

| leaf type | global count | rho_f | rho_g | delta | centre L | final A | contribution per leaf |
|---|---:|---:|---:|---|---:|---:|---:|
| small D2 factor r=2 | 6 | 4 | 6 | 13/18 | 6 | 3 | 2/3 |
| small D2 factor r=3 | 6 | 6 | 9 | 7/12 | 6 | 2 | 3/2 |
| large D2 factor r=2 | 5 | 4 | 6 | 2/3 | 5 | 3 | 4/5 |
| large D2 factor r=3 | 5 | 6 | 9 | 1/2 | 5 | 2 | 9/5 |
| large D2 factor r=1 (minor) | 5 per orbit | 2 | 3 | 6/5 | 5 | — | I_m += 1/5 |

For R025,R026,R027 choose large p2=(pi^5−a)(pi^5−b)(pi^5−c)^2. Then

    I_M=6*(2/3+3/2)+5*(4/5)=17,
    I_m=1+4+10*(1/5)=7.

R025 takes small path V3=1,V2=2; R027 takes small path V3=1,V2=3; R026 takes large path V3=4,V2=2. Thus every selected source radius and multiplicity is realized by this numerical tree. Every reduced multiplicity set is primitive: top(4,1), small(2,3), large(1,1,2). It also satisfies the report's stated B on actual ancestors: d3=12 divides M2=132; d2=60 divides M1=−120; the outer d4=6 divides both. All explicit search conditions Q integer, root count≤Q, positive major kappa, no zero kappa, multiplicity integrality, orbit law, final residues hold. This is already a depth≤2 completion under the described state rules. Thus the claim of no such completion for these three rows is **not reproducible even retaining the stated A and B**.

For R028 choose instead large p2=(pi^5−a)(pi^5−b)^3. Then

    I_M=6*(2/3+3/2)+5*(9/5)=22,
    I_m=1+4+5*(1/5)=6.

The selected large path has V3=4,V2=3. All reduced multiplicities remain primitive: (4,1),(2,3),(1,3). The same B divisibilities hold. This likewise directly contradicts the reported depth≤2 emptiness under its own listed constraints.

For n192,m144 (R057,R058), the principal minor has rho24,delta5. Top D3 has delta1/7,

    p3=pi^3(pi^7−c), P3=10,Q3=15,lo3=2/3.

Its seven small nonzero D2 children have rho12,kappa24/7,L7,delta4/7,P4,Q3,A1 and pattern multiplicities(1,3). Each gives one minor rho3 at delta8/7, and one final major rho9,rho_g12,kappa15/7,delta3/4,L7,A4,J9/7. The zero large D2 has rho36,kappa24,L1,delta1/4,P12,Q9,A4 and pattern p2=(pi^4−a)^3. Its four final major children have rho9,rho_g12,kappa15/4,delta9/16,L4,A4,J9/4. Thus

    I_M=7*(9/7)+4*(9/4)=18,
    I_m=1+4+7*(1/7)=6.

R057 selects the small V3=1,V2=3 path; R058 selects the large V3=3,V2=3 path. B holds: d3=12 divides M2=156; d2=48 divides M1=−144. The large p2 is a cube: it violates the false Lemma A. R058 already has exactly that cube as its frozen selected level2 pattern, while its newly closed small siblings have primitive(1,3). Therefore applying A only to new siblings also creates an inconsistency between different selections of the same full tree.

## Additional local differential-equation controls

One need not assume these reduced patterns have arbitrary compatible roots. The following upper-node checks explicitly solve the local equation from Moh Prop4.6/Appendix A.3:

    P*q'(pi)−Q*q(pi)*p'(pi)/p(pi)=C != 0.

They supply compatible squarefree q with all p-roots, and p not a power of q. The final-disc identities are also solved below; global gluing to a Jacobian pair remains unproved. No global realization follows from these separate local controls.

1. n180 top: z=pi^6, p=pi^4(z−1), q=pi(z−1)(z^3−3*z^2/2+3*z/8+1/16), (P,Q)=(10,25), C=45/8.
2. n180 small: p=pi^2(pi−1)^3, q=pi(pi−1)(pi^2−7*pi/5+7/25), (P,Q)=(5,4), C=21/25. Translate pi by a generic constant to place both roots away from0 without changing the A1 orbit law.
3. n180 large(1,1,2): set c=1,a+b=3,ab=3, p=(z−a)(z−b)(z−1)^2 with z=pi^5, q=pi(z−a)(z−b)(z−1), (P,Q)=(20,16), C=−60.
4. n180 large(1,3): take b=1 and 3*a^2−7*a+7=0, B=(a−7)/5, p=(z−a)(z−1)^3, q=pi(z−a)(z−1)(z+B), z=pi^5, (P,Q)=(20,16), C=20*B*a, nonzero.
5. n192 top: z=pi^7,p=pi^3(z−1),q=pi(z−1)(z−1/2), (P,Q)=(10,15), C=−35/2.
6. n192 small: p=pi(pi−1)^3,q=pi(pi−1)(pi−5/4), (P,Q)=(4,3), C=5/4.
7. n192 large: p=(pi^4−1)^3,q=pi(pi^4−1)(pi^4−5/4), (P,Q)=(12,9), C=15. This is a direct algebraic counterexample to the report's proposed reduced-pattern primitivity, including its local differential equation.

### Exact final leading-polynomial controls

Let D_(N,M)(g,f)=N*g*f'−M*f*g'. The following formulas are exact, squarefree and coprime, and satisfy the required actual Galois forms. `closure_controls.py` verifies all identities, squarefreeness, coprimality and residue supports in exact algebraic fields; JSON has seven upper-node and three final-node PASS controls.

* For final degrees(f,g)=(4,6), A=3: f=pi(pi^3−1), g=pi^6−3*pi^3/2+3/8. Then D_(3,2)=−9/8.
* For final degrees(6,9), A=2: f=pi^6+pi^4+5*pi^2/8+3/32; g=pi(pi^8+3*pi^6/2+21*pi^4/16+35*pi^2/64+63/512). Then D_(3,2)=−189/8192.
* For final degrees(9,12), A=4, set z=pi^4, b=(6+sqrt(6))/18, d=2/9+4*b/3, e=−4/81+4*b/9. Take f=pi(z^2+z+b), g=z^3+4*z^2/3+d*z+e. Then D_(4,3)=4*b*e !=0.

Multiply the weights by60 for n180,m120 and by48 for n192,m144. These cover every final major leaf type in all six explicit witnesses. They establish local polynomial compatibility, including the full r=1 identity, while leaving cross-node coefficient gluing open.

## R001/R009/R050: no arbitrary closure needed

All three are s=3. Every level2 major sibling is forced to D1 final. Their exceptional zero patterns give:

| row | zero rho_f,rho_g | actual L | delta | actual A | total I_M |
|---|---|---:|---|---:|---|
| R001 | 14,21 | 1 | 7/17 | 17 | 152/17 |
| R009 | 32,48 | 1 | 29/79 | 79 | 1592/79 |
| R050 | 10,35 | 1 | 13/22 | 22 | 123/11 |

All fail the final squarefree orbit residues and total integrality. The producer's R050 A=11 used coarse L4; the true zero-centre stabilizer L1 gives A22, an even stronger failure. R001's other pattern is Xu's(4,5), so it dies without A/B. R009 and R050 retain precisely the printed(8,8) numerical configuration; further minor splitting raises the minor expression and breaks equality. Their uniqueness is promotable at the stated necessary packet/contact level using the fixed-index replacement, not the producer's capped arbitrary-W argument.
