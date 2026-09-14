# Independent print audit: Moh search items (1)–(13)

The frozen Moh PDF was rendered and visually inspected at printed pp.200–201 (PDF ordinals 61–62). Images: `printaudit-p200.png`, `printaudit-p201.png`. Additional inspected renderings: p.150 (`printaudit-p150.png`), p.179 (`printaudit-p179.png`), pp.185–190 (`printaudit-prev-46.png` through `printaudit-next-51.png`), pp.203–204 (`printaudit-app-64.png`, `printaudit-app-65.png`). Text extraction is `printaudit-moh.txt`; its display mathematics often disappear, so images control.

The p.200 Theorem (1)–(7) and p.200–201 search list (1)–(13) are different lists. The former theorem explicitly assumes total degree equals y-degree for both polynomials, specifies characteristic data, and chooses M_s as the largest characteristic exponent <= n−2. It then provides the major tower and extension, minor-disc classification, root count bound, and existence of a major successor. The proof cites Propositions 5.4 and 6.1 (with the tower construction already given in Prop.5.3). Its hypotheses contain no degree cap. After the proof, Moh introduces an application to degrees less than 100 and restarts numbering. The search list must be split into clauses, because items (1), (2), (3), and (6) are mixed.

| Search item | Exact mathematical content | Class and all-degree source |
|---|---|---|
| Preface | f=T_1^psi | C, target triangular automorphism (U,V) -> (U+H(V),V), where T_1^psi=f+H(g), printed p.185 after Prop.5.4 and p.200 preface. It preserves generated polynomial algebra and Jacobian. Under m<n, H is constant once degrees are normalized. |
| (1) | deg f=m=−M_1 < deg g=n <=100 | m=−M_1 is A/definition once f=T_1^psi, p.150 characteristic definition and Prop.2.2 pp.152–154; m<n is C choosing/reducing the target pair; n<=100 is B, the application cap and nothing more. Swap target coordinates if necessary, compensating sign by scaling one coordinate; if degrees are equal cancel proportional top forms by a triangular target map before ordering. |
| (2) | m does not divide n; M_s=n−2 | First clause is C/minimal representative and then A for that representative: if n=km, the zero top Jacobian implies g_n=c f_m^k and (U,V)->(U,V−cU^k) lowers deg g while retaining f and Keller/noncoordinate status. M_s=n−2 is A from First-Separation / Prop.5.4 + Lemma5.3 pp.185–186, under the stated total-degree minimality. Neither uses n<=100. |
| (3) | J(f,g)=1; both degrees cannot be reduced simultaneously | J=1 is C: if J=c in k*, postcompose by (U,V)->(c^−1 U,V). No simultaneous degree drop is A once choosing a counterexample with minimal deg f+deg g; source automorphisms preserve noncoordinate status and Keller condition. Prop.5.4 p.183 supplies the exact simultaneous-drop alternative excluded. |
| (4) | Printed: {n,M_1,...,M_s} is the part of characteristic data less than n−2 | The literal wording is internally inconsistent: n is not <n−2 and item(2) has M_s=n−2. Do not silently promote this sentence as a theorem. The intended effective truncation has a safe printed A replacement: p.200 Theorem(3) chooses M_s largest <=n−2; p.150 definitions define strictly increasing characteristic M_j and p.174 Definition–Remark removes terminal n−1. Code may use those sources without relying on the faulty literal item. This is not evidence for bounded-search pruning. |
| (5) | d_r=gcd(n,M_1,...,M_{r−1}) | A, literally the characteristic-data definition on p.150: d_1=n, d_{j+1}=gcd(n,M_1,...,M_j), with M_j chosen as the first exponent not divisible by d_j. Consequently d_{j+1} is a proper divisor of d_j. Also p.155 basic arithmetic property(1). |
| (6) | 3<=s<=5, d_s>=4 | A for s>=3 by Prop.5.5 pp.186–188 (s=2 gives coordinate or simultaneous degree reduction) and s=1 already impossible in First-Separation (M_1<0 whereas M_s=n−2>=0). A for d_s>=4 by Cor.6.1 pp.199–200 and the immediately following smallest-degree conclusion; d_s<=2 excluded by d_s/2<V_s<d_s. B for s<=5 only. The sentence immediately before (6) explicitly assigns d_s>=4 to Cor.6.1 and s>=3 to Prop.5.5, while introducing s<=5 as a computation in the bounded application. |
| (7) | V_{r+1} d_r/d_{r+1} >= V_r > d_r/(n−M_r) | A, Def.5.1(2) p.179, Prop.5.3 construction pp.180–182, p.200 theorem(4),(7). The integer V_r is multiplicity of a root of p(pi), whose degree is the left expression; the strict lower inequality selects a major successor. Valid at all heights. |
| (8) | Radii from Def.5.1; L=lcm of upper reduced denominators; A_{r−1}=denominator(L delta_{r−1}) | A, Def.5.1(3) p.179 gives exact radii, and the rest is integer arithmetic defining the denominator increment. No restriction on n or s. |
| (9) | V_r d_{r−1}/d_r=Delta_{r−1} A_{r−1}+square_{r−1} | A, Euclidean division definition with 0<=square<A. The degree divided is integral by the divisor chain. |
| (10) | V_{r−1}<=Delta_{r−1} if selected factor pi−a has a!=0 | A, root-of-unity orbit bound, explicitly proved in p.201 between (9) and (10). Group element: tbar->omega tbar over k<<tbar^A>>, with tbar^(L A)=t and omega primitive A-th root of unity. This is a Galois symmetry proving a necessity on every branch, not a choice of coordinates imposed as normalization. |
| (11) | V_{r−1}=j A_{r−1}+square_{r−1} if selected factor is pi | A, same p.201 group action: nonzero roots come in A-element orbits; zero multiplicity is congruent to total degree modulo A. Here j>=0 follows from nonnegative multiplicity and 0<=square<A. A=1 is allowed. |
| (12) | A_1 divides (n/d_2)V_2 and (m/d_2)V_2−1 | A as one branch of disjunction with (13), p.201 explicitly refers to proof of Prop.5.5; pp.187–188 derive it from the terminal constant Wronskian and Prop.A.5 plus Galois symmetry. The proof mechanism has no s=2 restriction once used at terminal D_1 of an arbitrary tower. |
| (13) | A_1 divides (m/d_2)V_2 and (n/d_2)V_2−1 | A as the other branch of the same disjunction; exchanging the two terminal polynomials exchanges (12),(13). No target swap may be used to discard one branch after fixing m<n. Both are necessary alternatives and the code keeps both. |

## Why (10)–(13) do not hide the search bound

Let Q=V_r d_{r−1}/d_r be the degree of the leading common polynomial at level r−1; Def.5.1(4) + Prop.4.6 gives this degree. Earlier centers have denominator dividing L. With A the denominator increment, the subgroup of Puiseux conjugations fixing t^(1/L) acts on the new coefficient pi by a primitive A-th root of unity (the numerator of L delta is coprime to A). Therefore every nonzero root has an orbit of exactly A roots with identical multiplicity. If a!=0 has multiplicity V, then A V<=Q, equivalently V<=floor(Q/A), which is (10). If a=0 has multiplicity V, all other roots contribute a multiple of A, so V=Q mod A, which is (11). This argument applies to every positive integer A, every Q, every degree n, and every tower length; characteristic zero and the fixed center field are the source hypotheses.

At the terminal disc, g_sigma and f_sigma=T_{1,sigma}^psi satisfy D(n,m,g_sigma,f_sigma)=nonzero constant, by Prop.4.6 and Def.5.1(4), exactly the equation used on p.187. Thus both polynomials have simple roots, have no common root, and their derivatives have no common root (Prop.A.5, used explicitly p.187). Their degrees are N=(n/d_2)V_2 and H=(m/d_2)V_2 by Def.5.1(1). Under the same mu_A action each polynomial has all exponents congruent to its degree modulo A. For A>1, if neither degree is 0 mod A then both polynomials vanish at zero, impossible; if both degrees are 0 mod A, both derivatives vanish at zero, also impossible. In the remaining case one polynomial vanishes at zero and simplicity forces degree congruent to 1. Consequently the ordered residues are (0,1) or (1,0), proving exactly (12) or (13). For A=1 both conditions are vacuous. This proves the extension from the s=2 context of Prop.5.5's proof to a terminal disc in every tower; it does not copy the two-characteristic-pair contradiction itself.

The additional p.188 relation A | (n*+m*)V_2−1 is consistent, but no such relation has to be assumed to obtain the above necessary disjunction. The above argument tracks which field is fixed and so does not conflate a physical branch with its conjugate series.

## Consequences for the literal core code

1. There is no explicit s<=5 filter in the inspected frozen `census`. `divisor_chains(K,4)` recurses through arbitrarily long strict divisor chains. Since d_2=K and s=2+len(chain), all allowed heights at a given n are enumerated.
2. The bounded height follows arithmetically from n>=3d_2>=12*2^(s−2), using m<n, m not dividing n, hence reduced ratio n/K>=3, and d_s>=4. At n<=100 this gives s<=5. At n<=200 it gives s<=6. Height six is first possible at n=192, m=128 with d_2,...,d_6=(64,32,16,8,4). This establishes a concrete search target to check that the code has no hidden height five cap.
3. The code's V_s<d_s check is all-degree A, Lemma5.3 p.185 and proof p.186; search (7) alone supplies only <=d_s. This extra strictness is required by the two distinct top roots, not bounded pruning. Combined with V_s>d_s/2, it gives u_s=d_s−V_s>=1. There is no legitimate V_s=0 top datum in this setup.
4. The code's K=d_2, e=n/K>=3, dd=m/K in [2,e−1], gcd(dd,e)=1 is precisely the reduced positive ratio m<n, m not dividing n. In particular K<=n/3 is not a bounded-degree result: m/K=1 would make m divide n. The independent Kmin=16 setting is neither one of Moh's items nor proved by the supplied Moh/Xu sources; the core count lane is auditing it separately.
5. The gcd recursion forces d_{s+1}=gcd(d_s,n−2)=gcd(d_s,2), because d_s divides n. Thus d_{s+1}=1 for odd d_s and 2 for even d_s; any parity consequence here is all-degree. There is no additional even-n restriction.
6. With n−M_{s−1} a positive multiple of d_s and u_s>=1, Def.5.1 gives delta_{s−1}=[u_s(n−M_{s−1})−d_s]/[V_s(n−M_{s−1})−d_s]>=0. This is Lemma6.1 p.194 and explicitly also the proof of Prop.5.6 p.189. It is all-degree and follows automatically in the core.
7. The p.201 remark after (13), citing Prop.5.6 pp.188–190, excludes choosing zero at every stage: after y->y−ax−b the terminal series would be pi t^delta_1, forcing a coordinate pair or simultaneous degree drop. A numerical 'some level admits (10)' is a necessary over-approximation of this restriction. Merely defining `any10()` does not impose it in `full_ok()` or `census(full=True)`. Its omission is missed pruning, not a coverage loss. One must not infer an actual nonzero branch from a row merely satisfying numerical (10).

No condition in this literal core was identified as an n<=100-only theorem wrongly carried to n<=200. The only two B clauses in the print have both actually been removed. Item(4)'s literal strict wording is faulty, but the code's endpoint handling has a safe independent printed source. This conclusion does not yet certify the separately implemented whole-tree/ODE/Xu operative screen or the independent Kmin filter, and it does not identify a formal numerical skeleton as a realized polynomial pair.

## Completing the two implicit steps in the d_s=3 reduction

This supplement checks why Cor.6.1's output is a smaller **noncoordinate** Keller pair, rather than merely a pair with smaller pi-degrees. It uses the printed Prop.6.2/6.3 formulas and a source translation. Renderings `printaudit-cor-58.png`–`printaudit-cor-60.png` show pp.197–199.

When d_s=3, Lemma5.3 forces u_s=1,v_s=2, and Prop.6.4 supplies the radius hypothesis of Prop.6.3. Let N=n/3 and M=m/3. In affine coordinates (Y,Z)=(y,y−bx−e), with b!=0 after setting the major slope a=0, Prop.6.2 gives deg_Z g=N and deg_Z f=M. Their Z-leading coefficients B(Y),A(Y) have respective degrees 2N,2M, as the top form shows and the first display in the proof of Prop.6.3 p.197 explicitly records. The coefficient of Z^(M+N−1) in the nonzero constant Jacobian gives

    N A'(Y) B(Y) − M A(Y) B'(Y) = 0.

Consequently A^N/B^M is constant. The nonconstant polynomials A and B have a common zero c. Translate Y to Y−c before performing Prop.6.3 (adjusting e so that Z is unchanged). This is a source affine automorphism, preserving total degrees, Jacobian, top slopes, and the minor radius hypothesis; now A(0)=B(0)=0.

For u_s=1,v_s=2 the explicit substitution in Prop.6.3 is

    Y=gamma^(−1),
    Z=a_0+a_1 gamma+pi gamma^2,
    X=(Y−Z−e)/b.

The pre-pi series has only the powers 0 and 1 because the expansion stops strictly below v_s/u_s=2. A term Y^i Z^j produces Laurent monomials in (gamma,pi) of total degree at most 3j−i. Here j<=N for g, so total degree <=3N=n; equality is possible only at i=0,j=N. Its coefficient B(0) was made zero. All remaining monomials have total degree <=n−1. The same argument gives degree <=m−1 for f. Prop.6.3(1) proves that the negative gamma powers cancel, so the outputs are polynomials with these total-degree bounds. Prop.6.3(3) gives their nonzero constant Jacobian because v_s−u_s−1=0. No claim that total degree equals pi-degree is needed.

The substitution is an isomorphism of rational function fields: its inverse is

    gamma=1/Y,
    pi=Y^2 (Z−a_0−a_1/Y).

If the transformed f~,g~ were polynomial coordinates, gamma=P(f~,g~) for some polynomial P. Pulling back by this inverse field map would give 1/Y=P(f,g), an element of k[X,Y]. This is impossible because Y is not a unit. Thus the transformed pair is noncoordinate. It contradicts minimality of deg f+deg g because **both** degrees strictly drop. This supplies the elementary missing mechanism behind Moh's printed p.200 statement that a smallest-degree counterexample must have d_s>3, without appealing to an unproved descendant shape or to a ramified field-degree identity.

## Explicit normalization group elements

For completeness, simultaneous literal y-monicity and J=1 can be obtained in one step. Suppose original J(f,g)=c!=0 and total degrees m,n. Choose a nonzero vector v with a=f_m(v)!=0 and b=g_n(v)!=0; this is possible over the infinite algebraically closed characteristic-zero field. Choose another vector w with det[w,v]=ab/c. Let L(X,Y)=w X+v Y. Then

    F(X,Y)=a^(−1) f(L(X,Y)),
    G(X,Y)=b^(−1) g(L(X,Y))

have y-leading coefficients 1, retain total degrees m,n, and satisfy J(F,G)=c det(L)/(ab)=1. L is an element of GL_2(k); the target diagonal scaling is also an automorphism. A target swap (U,V)->(V,−U) has determinant 1 and orders unequal degrees. In the equal-degree or divisible-degree case, the top Jacobian relation makes the larger top form a constant multiple of a power of the smaller one; a determinant-one target shear subtracts that power and lowers the degree. All these are explicit group elements, not blanket permissions to translate an arbitrary Puiseux center to zero. The f=T_1^psi replacement is the independent target shear (U,V)->(U+H(V),V) printed p.185; once m<n, only constant H can remain.
