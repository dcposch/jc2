# F10 global middle resonance: exact normalization and an affine-W discriminator

Producer: Astra /root/nonemptiness_certificate. First action 2026-09-10 05:45:12 UTC; controlling stop 05:57:00 UTC, reserve 05:55:00. Manual mathematics only, no scientific execution. Seven current-pinned inputs and exact read scopes are in the owned PINS.json and READ-SCOPE.md. This is a new research producer, not a promotion gate.

## Outcome

GAP on uniform global H7-unitness: neither a unit theorem for every actual middle exponent nor an allowed leading counterexample is proved. There is, however, an exact whole-ring normalization, with no missing target relation, and a further explicit reduction of the single resonance equation to a polynomial **linear in W**. Its potentially vanishing coefficient is kept, not divided away. These give a smaller exact obstruction than the residual-cubic count; they do not assert that the obstruction has or lacks points.

The normalization was suggested by ROOT and checked independently below. The affine-W identity is a manual coefficient derivation here. The accepted local three-exception cover remains unchanged; it does not answer the global question.

## 1. Exact ring and exponents

Fix an integer r>=2 and h in {r+2,...,2r}. Put

    m=3r+1, n=5r+2, nu=n/m,
    alpha=(m+n-h)/m.

Thus 5m-3n=-1, 5/3<nu<2 and 2<alpha<7/3. In particular alpha, alpha-1, alpha-2 and alpha-nu are nonzero rational units. The rational exponents stay linked to r,h throughout.

Let L be the accepted universal guarded leading Q-algebra:

    C(theta)=theta^3+F theta^2+H theta+a,
    D(theta)=sum_(i=0)^5 D_i theta^i, D_5=1, D_0=b,
    m C D'-n C' D=-theta^7,  a*b invertible.

All coefficient rows are imposed. Accepted 17o proves H a unit in this very L; 17s and 17zw use the same C,H,a. That unit, not an additional guard or a chosen component, is used below. Arguments are identities of commutative Q-algebras, including nonreduced bases. The zero algebra is harmless. No leading-point existence is assumed.

Write (X)_k=X(X-1)...(X-k+1), and set

    c(z)=1+z+V z^2+W z^3,
    t_i(X)=[z^i] c(z)^X,
    t_5=t_5(nu),
    B_nu=Q[V,W,(W*t_5)^-1]/(t_6(nu),t_7(nu)).             (1)

The power is its formal binomial series; every displayed coefficient is a finite polynomial with rational coefficients. B_nu is not assumed a field, reduced, finite or nonzero.

## 2. A two-sided normalization, including the target coefficient

There is an exact isomorphism

    L = B_nu[s,s^-1].                                     (2)

The forward coordinates are

    s=H/a,  V=F*a/H^2,  W=a^2/H^3,
    C/a=c(s*theta).

All are defined since H,a are units. Let G=(C/a)^nu. Dividing the leading equation by the units m,C,G in L[[theta]] gives

    (D/G)'=-theta^7/(m*C*G).

Formal integration over Q shows D=bG+O(theta^8). Consequently t_6(nu)=t_7(nu)=0 in the normalized coordinates, and

    D/b=d(s*theta),   d(z)=sum_(i=0)^5 t_i(nu) z^i.

Monicity of D gives b*t_5*s^5=1, so t_5 is a unit. W is already a unit. This defines the forward map to (1).

Conversely, over any B_nu-algebra and any unit s, set

    a=1/(W*s^3), H=1/(W*s^2), F=V/(W*s),
    b=1/(t_5*s^5), C=a*c(s*theta), D=b*d(s*theta).          (3)

Both C and D are monic of their stated degrees, with the specified constants. Since d=c^nu+O(z^8),

    m*c*d'-n*c'*d=O(z^7).

The left side is a polynomial of degree at most 7. Its z^7 coefficient is

    (5m-3n)*W*t_5=-W*t_5.

Therefore it equals exactly -W*t_5*z^7, and substitution in (3) gives

    mCD'-nC'D=-a*b*W*t_5*s^8*theta^7=-theta^7.

The factor is exactly 1, not an unspecified unit to be repaired by scaling. Thus there is no missing target relation. Direct substitution in the coordinate formulas recovers V,W,s and every coefficient of C,D, proving both inverse identities. No maximal-ideal or reducedness argument is needed for (2).

Also

    H7_h=[theta^7](C/a)^alpha=s^7*t_7(alpha).              (4)

Hence the original global unit question is exactly the unit question for t_7(alpha) in B_nu: a unit stays a unit in a Laurent extension, and evaluation s=1 is a retraction that takes any purported inverse back to B_nu. This unit-test retraction does not specialize the full source. Laurent scale remains free; this is coefficient-coordinate normalization, not an unauthorized source automorphism or s=1 specialization of the full source.

## 3. Explicit low-degree equations and the additional linear row

The finite partitions i+2j+3k=6,7 give the following exact polynomials. Define E_X=720*t_6(X)/(X)_2 and Q_X=5040*t_7(X)/(X)_3, interpreted as polynomial identities in X:

    E_X=(X-2)(X-3)(X-4)(X-5)
       +30(X-2)(X-3)(X-4)V
       +180(X-2)(X-3)V^2+120(X-2)V^3
       +120(X-2)(X-3)W+720(X-2)VW+360W^2;

    Q_X=(X-3)(X-4)(X-5)(X-6)
       +42(X-3)(X-4)(X-5)V
       +420(X-3)(X-4)V^2+840(X-3)V^3
       +210(X-3)(X-4)W+2520(X-3)VW
       +2520(V^2*W+W^2).                                 (5)

For example the seven-degree partitions with k=0 give the four terms
(X)_7/7!, (X)_6 V/5!, (X)_5 V^2/(3!2!), (X)_4 V^3/3!;
k=1 gives (X)_5 W/4!, (X)_4 VW/2!, (X)_3 V^2W/2!;
k=2 gives (X)_3 W^2/2!. This derives Q_X without a coefficient subprocess. The analogous six-degree partitions derive E_X. At nu all divided rational factors are units, so (1) is equivalently guarded by E_nu=Q_nu=0.

Put

    sigma=alpha+nu, pi=alpha*nu, A=sigma-7,
    B2=sigma^2-pi-12sigma+47,
    B3=sigma^3-2sigma*pi-18(sigma^2-pi)+119sigma-342,
    P(V)=840V^3+420A V^2+42B2 V+B3,
    ell(V)=12V+A,
    Z(V,W)=P(V)+210*ell(V)*W.                             (6)

Subtracting Q_nu from Q_alpha cancels the V^2W and W^2 terms. The divided differences of the consecutive cubic and quartic in (5) are B2 and B3, respectively. Thus the exact polynomial identity is

    Q_alpha-Q_nu=(alpha-nu)*Z.                            (7)

In B_nu, where Q_nu=0, this yields

    H7_h=s^7*(alpha)_3*(alpha-nu)*Z/5040.                  (8)

Every prefactor in (8) is a unit. Therefore **H7_h is a global unit if and only if Z is a global unit in B_nu**. The resonance quotient has the exact presentation

    B_nu/(Z)
    =Q[V,W,(W*t_5)^-1]/(E_nu,Q_nu,P+210*ell*W).           (9)

This is a whole-ring equivalence, not merely a residue-field necessary condition, and retains the whole guarded leading algebra. It uses only one contact at alpha; no unjustified t_6(alpha)=0 row has been added.

## 4. The denominator boundary and what is still missing

The linear W row does NOT justify dividing by ell. Its zero locus forces V=-A/12. At this value direct substitution in (6) gives the rational scalar

    P_0=B3-(7/2)A*B2+(175/72)A^3.                        (10)

The two cubic contributions are 420*A*(A^2/144) and
-840*A^3/1728, totaling 175*A^3/72. This is a hand check of the coefficient in (10).

For a fixed actual (r,h), if P_0!=0, polynomial division by ell gives
P=P_0+ell*J(V). In (9),

    ell*(J+210W)=-P_0,

so ell is a unit of that resonance quotient, including nilpotents. Only then may one eliminate W as -P/(210ell). If P_0=0, the ell=0 residue-field branch must instead retain BOTH leading rows with V=-A/12 and the original W*t_5 guard. I have proved neither that P_0 is nonzero for all actual integer pairs nor that this latter branch is impossible. When P_0 vanishes, a principal-open elimination alone is not an exact scheme cover of (9); the polynomial presentation (9) is the safe object.

On the open ell!=0, the exact remaining problem is E_nu(V,-P/(210ell))=Q_nu(V,-P/(210ell))=0 with ell, W and t_5 invertible. Clearing denominators is legitimate only in that localization. No resultant, factorization, root count, coefficient norm, separability or nonzero constant remainder has been computed or asserted.

The missing uniform mathematical assertion is now precise: for every linked integer pair (r,h), the guarded algebra in (9) is zero. Equivalently it has no maximal ideal, since every nonzero commutative unital ring has one. A hypothetical maximal residue field may be any characteristic-zero extension, in particular one with complex V,W. Bounds on real alpha,nu supply no positivity for those coefficients. No argument supplied here excludes that maximal ideal, and no such ideal has been exhibited.

## 5. Controls and scope

1. Known-exponent control: t_7(nu)=0 in the actual leading algebra, and t_7(0)=t_7(1)=t_7(2)=0 identically. Thus a blanket nonvanishing claim at those exponents is false on any nonzero leading algebra. Formula (8) expressly uses that actual middle alpha avoids all four values; this is not an invented leading point.

2. Missing-contact control: if d is only the degree-five truncation without imposing the two leading contacts, write c^nu-d=t_6 z^6+t_7 z^7+O(z^8). Then mcd'-nc'd has z^5 coefficient -6m*t_6; after t_6=0 its z^6 coefficient is -7m*t_7. Both rows are needed for the exact target, rather than arbitrary monic cubics being licensed as leaders.

3. Guard and repeated-root control: in a field with W*t_5 nonzero, the derived exact target -W*t_5*z^7 forbids repeated roots of c or d and common roots: their constant terms are 1, so roots are nonzero; a repeated c-root makes both terms of the bracket vanish, as does a repeated d-root or a common root. Dropping the target/guard removes this contradiction. This checks that no arbitrary repeated-root or degenerate polynomial control was passed off as a guarded leading solution. No reality of the simple roots is implied.

4. Rank-stratum control: ell can vanish as a polynomial coefficient over Q[V,W]. Its inverse is not licensed by the fact that it is generically nonzero. Equation (10), together with the leading rows, is the explicit retained boundary test, not a claimed counterexample on that boundary.

This report neither strengthens 17zw's local count to a global count nor eliminates a middle variable globally. Every earlier, forcing, remaining source, guard and reconstruction equation is unchanged and outside this coefficient-only task. Even a future proof that (9)=0 would only settle the middle coefficient-unit question; it would not prove full-source existence, emptiness, a finite r bound or JC2. No computation or follow-on is authorized.

## Raised OPEN quantity, cheapest test, custody

No new canonical OPEN ID. Existing global H7-unit question remains: for each r there are r-1 linked coefficients, and the request is uniform in r. The sharp remaining test is the guarded zero/nonzero question (9), with boundary (10) retained; a uniform exact algebraic certificate or an actual guarded leading field point would settle it. The smallest preliminary documentary/manual check is whether the rational scalar P_0 can vanish at the actual linked integer pairs; by itself a negative answer would only license W elimination, not prove unitness. No such computation was executed or requested here.

Own-only collision check: new box and final report were absent at first action; only the transaction-owned partial and own box are written. No existing frozen input was edited. No other report, provenance, current computation or peer body was read. Own WHOLE and raised-OPEN review precede the marker. All seven original hashes are rechecked for final custody, which is handed off before the report result. Producer verdict: exact reduction proved; global unit assertion GAP, no counterexample, zero scientific execution.

Own WHOLE read completed 05:52:55 UTC; the final unit-test clarification was reread with its patch. Raised-OPEN quantity/cheapest-test and own-only collision checks complete. No further mathematical action is pending within this task.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11624`.
- Body SHA-256:
  `563a8cd062a120c74b5dab406fc48ec449b32873793a0dde5a1fcb21d5a6d178`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
