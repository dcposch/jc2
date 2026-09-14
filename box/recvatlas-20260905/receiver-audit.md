# Independent receiver audit

This note uses the nine frozen inputs whose mechanical verification was reported
by the primary agent. It reads only the frozen Fable report, frozen K16 report,
and the frozen Moh PDF. The generated text and rendered PDF page are in this
directory as `receiver-moh.txt` and `receiver-moh197.png`. No source, ledger,
ideation, Lean, or final report file was edited. No background computation was
started. The statements below are algebraic proofs; they require no Gröbner
basis calculation.

## 1. There are three different receiver statements

Use an arbitrary characteristic-zero field K and the orientation

    Jac(P,Q) = P_gamma Q_pi - P_pi Q_gamma.

The symbol `k=1` should not also name the field. The Jacobian scalar `c` must
be a nonzero field element, or an explicitly inverted coefficient parameter.
If c=0 is allowed, the claimed emptiness is false for an unrelated reason.

The following coefficient conditions are inequivalent:

1. **Full forward wedge:** for every j>=0,
   `deg_gamma coefficient(pi^j,P) <= 3j`, and similarly for Q.
2. **Positive coefficients only:** the same inequalities only for j>=1,
   including the weaker literal parenthesis in the task that only constrains
   `coefficient(pi,P)`.
3. **Reverse monic index:** if N=deg_pi P and M=deg_pi Q, impose
   `deg_gamma coefficient(pi^(N-j),P) <= 3j`, and the analogous Q condition.

The full forward wedge is empty with Jac=c gamma. The second and third
conditions admit explicit nonconstant monic pairs in every positive degree.
Consequently the indexing cannot be silently repaired while retaining an
emptiness conclusion.

## 2. Full forward wedge: exact all-degree emptiness theorem

For finite bounds N,M>=0, define the coefficient ring

    S_NM = K[c,c_inv, p_ij (0<=j<=N,0<=i<=3j),
                       q_ij (0<=j<=M,0<=i<=3j)].

Here `c*c_inv-1` is a defining equation, and the displayed order can be used
as the generator order, with pairs (j,i) lexicographically increasing.
Define universal polynomials over this coefficient ring by

    P = sum_(j=0)^N sum_(i=0)^(3j) p_ij gamma^i pi^j,
    Q = sum_(j=0)^M sum_(i=0)^(3j) q_ij gamma^i pi^j.

Let J_NM contain `c*c_inv-1` and every coefficient of
`Jac(P,Q)-c*gamma`. One may add monicity equations at degrees N,M; they do
not affect the result.

**Theorem.** J_NM=(1), for every N,M. Hence its union over all finite bounds
has no pair with nonzero c.

**Proof.** At pi=0, P=p_00 and Q=q_00, both independent of gamma. Therefore
P_gamma and Q_gamma are divisible by pi. Their Jacobian is divisible by pi.
In particular its coefficient of gamma*pi^0 is zero. The corresponding
receiver equation is exactly

    E_10 = coefficient(gamma*pi^0, Jac(P,Q)-c*gamma) = -c.

The explicit unit certificate is

    1 = -c_inv*E_10 - (c*c_inv-1).

This proves the theorem scheme-theoretically, over every coefficient
extension. With c a fixed nonzero scalar, the certificate is simply
`1=(-1/c)*E_10`. In fact this proof needs no characteristic-zero assumption:
the stated full-wedge contradiction holds in every characteristic.

**Geometric interpretation.** The full wedge forces the entire line pi=0
to have a single image (p_00,q_00). Its Jacobian must vanish along pi=0.
The prescribed Jacobian c*gamma does not vanish identically there. The
problem is the constant coefficient, not a sophisticated degree estimate.

**Critical pullback implication.** If a unital homomorphism
`phi:S_NM -> R` satisfies `phi(J_NM) subset I` in a declared localization
of R, then `1=phi(1)` belongs to that localized source ideal. Indeed pulling
back the displayed certificate gives an explicit source unit certificate.
This is a valid method only when images of *all* receiver equations have
been proved to lie in the necessary source ideal. The empty receiver
cannot provide that missing membership proof by itself. Matching ell=1,
Newton slopes, or degrees establishes no such membership.

## 3. The weakened and reverse-index systems are nonempty

For every N>=1 and every c in K^*, the pair

    P = pi^N + (c/2)*gamma^2,
    Q = pi

is nonconstant, monic in pi, and satisfies Jac(P,Q)=c*gamma. It obeys:

* the condition on the coefficient of pi alone;
* every forward coefficient inequality for j>=1;
* the full reverse-index inequalities at degrees (N,1).

It violates exactly the forbidden constant-coefficient requirement of the
full forward wedge. Thus the parenthetical condition `deg_gamma[pi]<=3`
does not define an empty receiver when taken literally on its own.

A complete classification is available for the small slice in which P,Q
are both monic and affine in pi. Write

    P=pi+B(gamma), Q=pi+D(gamma).

Then Jac=c*gamma if and only if

    D=B-(c/2)*gamma^2+d, with d in K.

For the reverse-index bound at degree one, additionally require deg B<=3;
then deg D<=3 automatically. For the positive-coefficients-only condition,
B is arbitrary. This classifies the entire monic affine slice, not the
full arbitrary-degree receiver.

There is also a useful complete classification of all affine-in-pi pairs,
without monicity. Let P=A*pi+B and Q=C*pi+D, with A,C not both zero. The
pi coefficient of the Jacobian is A'*C-A*C'. Its vanishing implies that
A,C are proportional over K. After an invertible constant linear change
of target coordinates, write the pair as `(A*pi+B,E(gamma))`; let the
new Jacobian scalar be c'. The equation is

    -A*E' = c'*gamma.

Since K[gamma] is a UFD, A=a or A=a*gamma for a in K^*. The two forms are

    (a*pi+B, -(c'/(2a))*gamma^2+e),
    (a*gamma*pi+B, -(c'/a)*gamma+e).

B is arbitrary and e is constant. The first form is the usual degree-two
fold type. The second is birational and contracts the critical line; for
example `(gamma*pi,gamma)` has Jacobian -gamma. Monicity in pi excludes
the second form. This example shows why a blanket claim about all
linear-Jacobian polynomial pairs being folds would be false even before
addressing the much stronger arbitrary-degree monic classification.

No classification of all monic arbitrary-degree solutions is established
here. The displayed all-degree family is a disproof of emptiness for the
weakened and reverse-index interpretations, not a completeness theorem.

## 4. What Moh Proposition 6.3 actually supplies

The frozen PDF was read as a page image: printed p.197, PDF page 58.
Proposition 6.3 assumes the displayed source degree and monicity
conditions, delta_s=-1, and the radius inequality
`delta^*_(s-1)>=v_s/u_s`. It defines

    theta = y^(-1), gamma = theta^(1/u_s),
    z = y-b*x-e,
    sigma = sum_j a_j*theta^j + pi*theta^(v_s/u_s).

Thus, writing u=u_s, v=v_s and
`A(gamma)=sum_j a_j*gamma^(u*j)`, the substitution is

    y = gamma^(-u),
    z = A(gamma)+pi*gamma^v,
    x = (gamma^(-u)-e-A(gamma)-pi*gamma^v)/b.

The proposition supplies polynomiality of the descended pair, monicity
in pi, the stated pi degrees, and

    Jac_gamma,pi(gbar(sigma),Tbar_1(sigma))
        = -(u/b)*gamma^(v-u-1).

It does **not** print Fable's forward Newton coefficient inequality.
The proof on p.198 explicitly retains the nonzero root truncation A.
The linear-Jacobian case is v=u+2; v=3 follows only when u=1.
Consequently the 671 rows with ell=1 cannot all be assigned slope three
merely from ell=1 if some have u>=2.

The sign and exponent are independently checked by differentiation:

    x_pi = -gamma^v/b, y_gamma=-u*gamma^(-u-1), y_pi=0,
    Jac_gamma,pi(x,y) = -(u/b)*gamma^(v-u-1).

The terms involving A' cancel because y_pi=0. This is an exact ring-map
identity in the Laurent polynomial ring with gamma inverted and b
inverted. Polynomiality of the descended pair is a further source
condition supplied by the proposition's hypotheses, not by the chain
rule alone.

## 5. The correct coefficient transport includes the root truncation

Let a source polynomial be

    h(y,z) = sum_(i,r) h_ir*y^i*z^r,  i,r>=0.

Its literal pullback is the Laurent polynomial

    D(gamma,pi) = sum_(i,r) h_ir*gamma^(-u*i)
                          *(A(gamma)+pi*gamma^v)^r.

The coefficient of pi^j is exactly

    D_j(gamma) = gamma^(v*j)
       *sum_(i,r>=j) binomial(r,j)*h_ir*gamma^(-u*i)*A^(r-j).

Every negative gamma coefficient must vanish for D to be polynomial.
Once those vanish, nothing in source polynomiality alone forces
`deg_gamma D_0<=0`: the terms A^(r-j) are still present.

The genuine shifted support statement is obtained by setting

    D_tilde(gamma,pi) = D(gamma, pi-A(gamma)*gamma^(-v)).

Then

    D_tilde = h(gamma^(-u),pi*gamma^v)
            = sum_(i,j) h_ij*gamma^(v*j-u*i)*pi^j.

Therefore every exponent pair (a,j) in D_tilde satisfies

    a<=v*j and a congruent to v*j modulo u.

Negative a are allowed. This is a statement in a Laurent ring after a
Laurent shear, and is not the unshifted polynomial wedge used in the
emptiness theorem. Omitting either the shift or the negative exponents
changes the receiver object. The shear has Jacobian one, so it preserves
the monomial Jacobian equation; it does not preserve polynomiality in
gamma.

A modest unconditional unshifted degree estimate, when A is polynomial
of degree a and deg_z h<=N, is

    deg_gamma D_j <= v*j+a*(N-j)

after negative powers cancel, provided a>=0. This follows term by term
from i>=0 and r<=N. It differs from both simple forward and reverse
index bounds. No claim is made that it is sharp under all of Moh's
additional characteristic hypotheses.

## 6. Explicit counterexample to Fable's polynomiality argument

Set u=1, v=3, A=gamma+gamma^2 and take source polynomials

    F(y,z)=y^3*z-y^2-y,
    H(y,z)=y*z-1,
    g(y,z)=F(y,z)^2+H(y,z).

Under y=gamma^(-1), z=gamma+gamma^2+pi*gamma^3, direct substitution gives

    F -> pi,
    H -> gamma+gamma^2*pi,
    g -> pi^2+gamma^2*pi+gamma.

The last polynomial is monic in pi, is a genuine polynomial descent of
a polynomial source, and has a positive gamma term at pi=0. Hence
`deg_gamma coefficient(pi^0,gbar)<=0` is false. In original coordinates
z=y-b*x-e with b=1,e=0, g has total degree eight and is monic in y.
This example refutes the inference “source polynomiality implies the
unshifted forward Newton wedge,” including when source degree and
monicity are retained.

This example is **not** claimed to satisfy every source hypothesis of a
Keller chart or Proposition 6.3, and it is not a counterexample to the
Jacobian conjecture. Its role is exactly bounded: the support inference
as stated in Fable Section 2.3 does not follow from polynomiality. An
extra theorem from the full necessary source ideal would be needed.

Changing g to `F^3+z^2` gives the monic polynomial descent

    pi^3+(gamma+gamma^2+pi*gamma^3)^2.

Its coefficient of pi^2 is gamma^6. Thus a reverse-index bound with
three at the first coefficient below the leading term is not implied
by source polynomiality and monicity either.

## 7. Consequences for the clients and promotion

The frozen Fable report itself describes positive-dimensional t=2,
y=1/5 K16 cone families and proposes sampling their purported receiver
points (Section 6, Card A). Therefore those cone points cannot at once
be genuine points of the full forward-wedge empty receiver. At least
one of the asserted support, coordinates, localization, or source map
must change. K16's displayed Jacobian is

    Jac_gamma,pi(Q,P)=-c*z+tau*pi, z=pi-gamma.

At tau=0 the critical line is z=0. The linear change from (gamma,pi)
to (z,pi) changes every coefficient support assertion. Calling z the
new descent variable is permissible only together with the transported
polynomials and support equations. At tau!=0, choosing the critical
linear form as a coordinate also requires transporting these equations.
An invariant coincidence “linear Jacobian” supplies no coefficient
homomorphism into the empty receiver.

The present audit proves no all-t K16 vanishing and no implication to
(8.1) or (T). It supplies a complete empty-receiver certificate for the
literal full bound, an explicit obstruction to promoting numerical
receiver assignments, and nonempty families under other readings. Any
coverage fraction must count verified coefficient maps and ideal
memberships, with all unsupported branches returned as UNASSIGNED.
In particular 671/1110 is an exponent census until those maps exist;
it is not a discharged residue fraction.

No new exit-price claim is made in this note, so no `charge_basis` line
is applicable.
