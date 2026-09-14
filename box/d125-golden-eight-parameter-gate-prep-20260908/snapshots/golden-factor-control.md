# Golden top: exact degree-three divisibility and normal-remainder obstruction

2026-09-08. **Elementary countercontrol: the squarefree-Q implication fails.** There is a unique nonzero degree-three solution with any prescribed nonzero coefficient of g²p. It fits that coefficient and the unequal polygon, but no other source equation, full-source point or supplied first-contact hypothesis is claimed. This task uses only the accepted minimal receiver's literal golden field/top/support and polynomial algebra, independently of any pending Q exclusion or nonodd work.

## 1. Field and complete degree-three classification

Work over a characteristic-zero FIELD K containing rho with rho²−3rho+1=0. Put

    t=1−rho, L=p+g, M=p+t g,
    H=p² L M², D=p L M.

The three linear factors p,L,M are distinct. Both rho and t are units;
t²=rho and t⁻¹=2−rho. These statements hold for BOTH roots rho and3−rho. Over Q the quadratic is irreducible by the rational-root test, so Q[rho] is a field; no additional extension or preferred real embedding is chosen.

Unique factorization gives the exact equivalence

    H divides F²  <=>  D divides F                (1)

for every F in K[g,p]. Each multiplicity1 or2 in H requires multiplicity at least1 in F. Consequently all solutions of degree<=3 are exactly

    F=lambda D, lambda in K.

For exact degree3, lambda!=0. This classification does not assume homogeneity in advance: division by the degree3 polynomial D makes the quotient constant. For such a nonzero F,

    F²/H=lambda² L,        H does NOT divide F.   (2)

Equation(2) is a factored identity; no actual H² or degree6 square was expanded in the controls. More generally, writing F=D U gives w(F)<=3 exactly when w(U)<=0, while H divides F exactly when pM divides U. The weight condition alone cannot force this extra divisibility.

In the squarefree-Q argument the crucial step was V0|F² =>V0|F. Here V0=L M² is NOT squarefree, and the implication is false. Replacing V0 by its radical only gives L M|F; the weight bound then forces one p factor, not the two factors and extra M required for H|F.

## 2. Exact unequal-face compatibility, both conjugates

D expands as p³+(2−rho)gp²+(1−rho)g²p. If the prescribed nonzero unequal face coefficient is [g²p]F=a, the UNIQUE degree-three solution is

    F_a=a[g²p+(3−rho)gp²+(2−rho)p³],
    lambda=a/t=a(2−rho).                         (3)

Its weight is exactly3, it is odd, and its three monomials lie in the accepted unequal polygon: i+j<=15, i<=2j and5i−7j<=3. Only g²p lies on the weight3 face. The other two coefficients are lower-weight slots; the listed source face does not forbid them.

This is same-field compatibility with the low face coefficient, not independent normalization of all guards. For the accepted monic golden outer face, kappa=rho. The literal unequal face relations then require

    b=rho³, f=rho⁵, e=(5/3)a rho²,
    d=(5/9)a²/rho, c=−(5/9)a³/rho.

Thus a=1 is compatible with c=−5/(9rho), not an independently imposed c=1. Both conjugates are retained by replacing rho with3−rho everywhere, including H and these scalars. No chosen root, source point or other coefficient row is silently discarded.

If a future source argument supplies H|F² for a degree-three first-contact coefficient, it cannot exclude that coefficient merely by the Q weight argument. Equation(3) is a nonzero face-compatible algebraic survivor of THIS condition only. No source derivation of H|F² is asserted here.

## 3. Normal-remainder and implicit-coordinate failures

D and F_a are monomial-normal for the leading monomial g³p² of H (whose coefficient rho is a unit): their g-degree is2. Yet they vanish identically on BOTH reduced lines L=0 and M=0. Hence weight<=3 normal remainders no longer inject into the product K[p]² obtained by normalizing the REDUCED zero set of V0. In K[g,p]/(L M²), the class of D is nonzero and square-zero. Passing to reduced branches loses this nilpotent information. This is an explicit obstruction before any proposed source or Newton-initial argument.

There is also a first-order coordinate warning. Consider only the tiny odd deformation H+s p, of weight<=1. On the simple branch g=−p,

    H_g=rho²p⁴,
    g=−p−s/(rho²p³)+O(s²),
    F_a(g,p)=−lambda*s/(rho*p)+O(s²).

Thus this nonzero normal remainder, whose order0 restrictions all vanish, has a first simple-branch moving residue with an affine pole. On the repeated line g=−p/t, H_g=0. An unramified formal root g=g0+s g1+... of H+s p=0 would require

    H_g(g0,p)g1+p=0,

which is impossible in K(p). A ramified construction would need separate hypotheses and analysis. The deformation is an algebraic control, NOT an actual golden source family. No higher jet, branch classification or claimed regularity after ramification is added.

## Evidence and stop

The complete accepted minimal receiver composition report was read and pinned; its original historical status header is unchanged. Named history checks covered that report, APPROACHES and ladder/REDUCTION; no exhaustive novelty claim. No new primary theorem is imported.

Ten capped normal/−O runs pass over the exact quadratic field with both conjugates, zero Assert nodes and byte-identical witnesses. Actual mutations change the degree-three middle coefficient, freeze the wrong conjugate, reverse the moving-root sign, or impose an incompatible c normalization. Controls expand only factors of degree<=5 and scalar products; square divisibility is checked through exact factor multiplicities. Inputs, report, code, witnesses and transaction are pinned in owned custody. No full source, H², CAS, AWS, new model, shared/protected edit or live peer was used. **STOP: exact failure of squarefree/normal-remainder transport; no exclusion, full-source survivor, search or computation license. All writers idle at terminal handoff.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5938`.
- Body SHA-256:
  `003390bdfa1705bfd34be438383c4e9543f29398ff95884a4408946d1cbe68c2`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
