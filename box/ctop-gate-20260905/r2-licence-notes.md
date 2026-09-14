# Independent source / disc-licence audit (r2)

Frozen PDF: `/tmp/jc2-lane.yqyWvI/inputs/moh1983_jram340_configurations_of_roots.pdf`.
Root mechanically verified the charged hash before delegation. This audit independently ran
`pdftotext -layout` and rendered printed pp.179,197,198,207 directly from that PDF with
`pdftoppm`, saved as `r2-licence-pNNN.png`. No prior page image was used as proof.

## Literal statements

Printed p.179, Definition 5.1 introduces a *tower of major discs*, not a numerical
sequence independently of discs:

> A tower of major discs D_s ⊋ D_{s-1} ⊋ ... ⊋ D_r satisfies the following four criteria with a sequence of integers {V_i : i=(r+1,...,s+1)}:

Its (1) reads:

> In the disc D_i the polynomials g(y) have precisely (n/d_{i+1}) V_{i+1} roots. T_j^ψ(y) has precisely (-μ_j/d_{i+1}) V_{i+1} roots for j=1,...,i,

Its (2) reads:

> the numbers V_i satisfy V_{i+1}d_i/d_{i+1} ≥ V_i > d_i/(n-M_i) for i=r+1,...,s, V_{s+1}=d_{s+1},

Thus `V_s ≤ d_s` follows by substituting the top normalization into the upper
inequality. It is necessary for an *actual identified tower*. Violating it makes an
asserted tower impossible; without identification of the numerical labels with the
actual tower it proves a labeling failure, not impossibility of the underlying pair.
The literal definition begins with r≥2; Prop.5.3 extends a tower down to D_1 (and
p.187 explicitly uses the s=2 tower). The i=1 root count is consequently legitimate
for an actual tower extended to D_1, but i=1 is not in the initial r≥2 definition
in isolation.

Prop.6.3(2), printed p.197, says:

> ḡ(σ), T̄_1^ψ(σ), ..., T̄_{s-1}^ψ(σ) are monic in π with π-degree u_s n/d_s, u_s(-μ_1)/d_s, ..., u_s(-μ_{s-1})/d_s respectively,

This is a degree statement for polynomials in k[γ,π]. Over the algebraic closure
of k(γ) it gives exactly n'=u_s n/d_s roots counted with multiplicity. It does not
say “n' roots in D'_1”; it neither defines D'_1 nor prints inherited V labels.
The proof p.198 identifies a degree-n' leading polynomial at **γ→0**, built from
the source minor disc. This is not the child's major tower at γ→∞.

The substitution is, with C(γ)=∑a_jγ^j and j<v_s,

    y = γ^{-u_s},
    z = C(γ) + π γ^{v_s},
    x = (γ^{-u_s} - e - C(γ) - πγ^{v_s})/b.

The construction starts with the source minor disc at θ=1/y→0. The source major
tower is over t=1/x→0. The child's own infinity discs are over t'=1/γ→0. These
three places and their root variables cannot be equated merely because the
arithmetic identity n'/d'_i = n/d_i holds.

The paragraph immediately before Prop.6.3 says that the Jacobian is modified to
a monomial. Formula (3) p.197 gives J_{γ,π}=-(u_s/b)γ^{v_s-u_s-1} (direct
chain-rule calculation confirms that exponent). Consequently the child does not
satisfy the constant-Jacobian hypotheses used to construct Def.5.1 verbatim.
There can be a modified monomial-J tower with the same root-count interpretation,
but that extension and the identification of its V's must be established.

The failure of a *literal* transfer of all four Def.5.1 criteria is already visible
in Moh's printed p.207 positive control: child n=16, M_2=13 has δ_2=-1, whereas
Def.5.1(3) alone yields -1/(16-13-1)=-1/2. The correct printed value incorporates
the Jacobian X through the factor 2. This does not alone disprove the count
criterion, but prevents treating the whole child tuple as an unchanged Def.5.1
instance.

## Positive information about M is stronger than the report's citations

Printed p.154 says:

> the existence of such a sequence of polynomials T_r^ψ(f(x,y),g(x,y)) implies that the characteristic data {d_i,M_i} can be recovered by ... formula

and explicitly notes that the n,μ sequence and n,M sequence determine each other.
Together with the exact child π-degrees in Prop.6.3(2), this is a possible route
to identify the retained M list. It says nothing analogous about inherited V.
The p.150 characteristic recipe is about the f expansion in η=g^{-1/n}, over
k(x), not about the physical g=0 root tower over k((1/x)). Termination of that
characteristic sequence cannot identify a particular physical cluster.

## Independent verification of the 96/72 top-label countercalculation

Use the charged numerical source row

    n=96, m=72, M=(-72,36,78,94), V_2=4,V_3=3,V_4=5,
    d=(96,24,12,6,2), u_4=1, v_4=5.

Direct Def.5.1 radius arithmetic gives

    δ_4=-1, δ_3=1/7, δ_2=2/7, δ_1=1/3.

D_3 contains 80 g-roots (96/6·5). It has more than half of all g-roots, so it is
fixed under Puiseux Galois conjugation: two distinct conjugates would be disjoint
and would require at least 160 roots. Its truncated centre is therefore rational
in t; after choosing the major slope to be 0 and translating the common constant,
no positive integer exponent lies below 1/7. Hence its general point is
σ_3=π t^{1/7}.

Prop.4.6 at D_3 supplies the common p polynomial with degree

    v = V_4 d_3/d_4 = 5·12/6 = 10,
    g_{σ_3}=p^8 (up to a nonzero scalar),
    (T_2^ψ)_{σ_3}=p^15 (up to a nonzero scalar).

Here μ_2 = (d_1/d_2)M_1 + (M_2-M_1) = -180, so the latter exponent is
(-μ_2)/d_3=15. The selected source V_3=3 is a root multiplicity in p. Since the
radius is 1/7, every nonzero root of p has a seven-element conjugacy orbit with
constant multiplicity. A multiplicity-three nonzero root would require degree
at least 21, exceeding deg p=10. Thus the selected root is zero. The remaining
seven degree units form one simple nonzero orbit, giving

    p(π) = constant · π^3(π^7-a),  a≠0.

The 7 nonzero exits carry 7·8=56 source g-roots, and 7·15=105 source T_2-roots.
For each such branch y=c t^{1/7}+higher terms, c^7=a. Put y=γ^{-1}; inversion
gives

    x = a γ^7 + lower powers of γ,
    π_child = -b a γ^2 + lower powers of γ.

All seven conjugate leading coefficients c coalesce into this one nonzero
coefficient (-ba), because c^7=a. Ramification divides the number of branches
by seven: the child cluster has 8 g-roots and 15 T_2-roots. This can be checked
on the elementary leading relation y^7=a/x, which becomes x=aγ^7; the seven
source y-roots over x become one x-root over γ, with the transverse multiplicity
8 (respectively 15) retained.

The source zero group has order(y)>1/7, so its corresponding child roots have
π_child/γ^2→0. Prop.6.3 total degrees are 16 for g' and 30 for T'_2. Thus the
other child leading cluster contains exactly the remaining 8 g-roots and 15
T'_2-roots. At the child's top radius -2 there are two distinct leading values,
0 and -ba, each with g count 8. Either prospective lower top disc therefore
has normalized count

    V'_3 = 8 / (n'/d'_3) = 8/(16/2) = 1,

not the copied source V_3=3. The T'_2 check is simultaneous:
15 / ((-μ'_2)/d'_3) = 15/(30/2)=1. This is an actual root-count transformation,
not an inequality imposed on a guessed label. The discarded label asks for
24 roots in a child of degree16, but the correctly transformed top clusters
have 8 each.

This is a **conditional local calculation**: if a pair realizing the source
row exists, its first source major face has the stated form and transforms as
above. It is not a constructed global Keller counterexample. Deeper source
or child obstructions could still exclude the row. It refutes the claimed
universal *inheritance identification* that is load-bearing for the proposed
C-TOP kill. In particular, an arbitrary Laurent expansion with the same M list
must not be presented as a global descended pair.

## U-NEG conclusion

For any actual child disc D'_1 with normalized count W_2, the elementary
inequality is valid:

    (n'/d'_2) W_2 = #g'-roots in D'_1 ≤ n', hence W_2≤d'_2.

What has not been licensed is substituting the campaign's copied V_2 for W_2.
The one-liner in the charged report does exactly that before proving that it
is the same disc, centre, radius, base valuation, and normalization. The p.207
five-row table is a genuine positive control for those five rows; it is not a
general inheritance statement. The report itself names the remaining
identification OPEN, then nevertheless makes u_s=1 exclusions unconditional.
A valid general count bound plus an unproved (and at top demonstrably false)
label transfer does not supply a blanket U-NEG licence.

Verdict on the claimed proof: REFUTED as an unconditional licence; the honest
residual is OPEN[CHILD-LEVEL2-IDENTIFICATION]. This does not assert that some
U-NEG source row is realized by polynomials; nor that no independent screen
can exclude all those rows.

No new exit-price assertion is made. No charge_basis line is applicable.

## Primary witness revision: 180/120, with complete top approximate-root check

The 96/72 derivation above is valid as a conditional top transformation but may
have independent deeper source obstructions. Prefer the following row, reported
by the independent enumerator audit to pass its additional cumulative support
checks (passing these checks is still not a polynomial-existence witness):

    n=180,m=120,M=(-120,132,150,178),V=(2,4,5),
    d=(180,60,12,6,2), μ=(-120,-108,-522), u_s=1,v_s=5.

The first source major disc D_3 has radius 1/6 and contains150 of180 g-roots,
so the same >half argument makes its centre rational and, after constant
translation, σ_3=πt^{1/6}. Prop.4.6 has v=10. The selected V_3=4 must be the
zero multiplicity: a nonzero six-element orbit at multiplicity4 would exceed
deg p=10. Hence, up to nonzero constants,

    p(π)=π^4(π^6-a), a≠0,
    g_σ=p^15, (T_1)_σ=p^10, (T_2)_σ=p^9.

For the final approximate root T_3, Prop.4.6(2) supplies the stronger check

    (T_3)_σ=p^41 q,
    41=(-μ_3+M_3-n)/d_3=(522+150-180)/12,
    deg q = v(n-M_3)/d_3=10·30/12=25.

The roots of q are all distinct and include the roots of p. Conjugacy gives

    q(π)=constant·π∏_{j=1}^4(π^6-b_j),

where b_j are distinct nonzero constants and one equals a. Thus no hidden
source T_3 branch has an order less than1/6 inside D_3. All branches outside
D_3 are in the other original tangent direction; they do not create larger
poles at child γ∞.

Under the u_s=1,v_s=5 substitution, each nonzero orbit with y=c t^{1/6}
inverts to x=c^6γ^6 and child π/γ→-bc^6. Six source conjugates become one
child leading value. Consequently:

* g's six nonzero exits, each of multiplicity15, yield15 child roots at
  one nonzero leading coefficient; the degree30 total leaves15 at0.
* T_1's corresponding exits give10 and10, matching child degree20.
* T_2's corresponding exits give9 and9, matching child degree18.
* At the p-shared nonzero orbit T_3 has multiplicity42 (41+1); the other
  three nonzero q-orbits each have multiplicity1. Inversion gives42+1+1+1=45
  nonzero-leading child roots. Its exact degree87 leaves42 at0.

Thus the complete child top leading factors have the form

    p_child(w)=w(w-A), A≠0,
    g'_top=p_child^15,
    (T'_1)_top=p_child^10,
    (T'_2)_top=p_child^9,
    (T'_3)_top=p_child^41 q_child,

where q_child has5 simple roots including0,A and three further distinct
nonzero values. The last count is2·42+3=87, so this checks the top disc against
T'_3 too, not merely g'. The top disc radius is-1. The two eligible g-clusters
both have15 roots; either gives

    actual child V'_3=15/(30/2)=1,

where the campaign copies V_3=4. The characteristic tuple inferred from the
exact π-degrees is

    n'=30,m'=20,M'=(-20,22,25),d'=(30,10,2,1), μ'=(-20,-18,-87).

The generalized monomial-J radius agrees: J∝γ^3 gives
δ'_3=-(3+1)/(30-25-1)=-1. This is internally consistent complete top Newton
information and directly shows how the copied V differs from the actual
child normalized count. It is a conditional computation for a source pair
realizing the row, not an assertion that such a global pair exists.
