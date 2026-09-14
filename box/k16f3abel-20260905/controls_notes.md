# Direct F3 controls and uniform scalar elimination

All mathematical inputs were the frozen `/tmp/jc2-lane.zx9GKm/inputs` files.
The direct driver uses the displayed F1--F3 equations, not the original
spine or any generated terminal rows. Exact runs use Singular over the
declared characteristic-zero field and the two small family/certificate
checks additionally use SymPy over Q.

Put q=2t+1, alpha=3/(4y^2), and let F denote the left side of F3 minus
its right side. Write

    C=x^(t-1)+c1*x^(t-2)+...+c_(t-1),
    W=omega*x^q+sum_(k=1)^(q-1) w_k*x^k-B.

The coefficient [x^(2q)]F is zero by the normalizing equation. For
k=q-1,...,1 in descending order, [x^(q+k)]F is affine in w_k, with
scalar coefficient

    lambda_k=2((q+k-1)*omega+alpha)
            =(6d(d+1)+k+1)/(2y^2(2d+1)).

Every other w-variable in this row has already been solved. In particular
D*W has degree shift t<q, and the explicit eta terms have degrees at most
t+1<q+1. The displayed expression follows from
omega=1/(4y^2(2d+1)), using 3d^2=t+1. For t>=2, either d>=1 or d<=-1;
then d(d+1)>=0, so the numerator is strictly positive. Thus lambda_k is
a nonzero scalar on both embeddings, including rational split factors.
At the final coefficient [x^q]F the coefficient of B is

    -((2q-1)*omega+alpha)=-2d*alpha=-3d/(2y^2),

also a nonzero scalar. Therefore each C,b determines a unique W,B by
polynomial expressions in c1,...,c_(t-1),b. The coefficients of x^0 and
x^1 in F are identically zero from W(0)=-B and eta=W'(0). The exact
remaining ideal is

    J_t=([x^2]F,...,[x^(q-1)]F)

in k[c1,...,c_(t-1),b], with weights (1,...,t-1,t+1). The generator
weights are 4t,4t-1,...,2t+2. The target B*eta has weight 4t+1. This
elimination is a scheme identity with nonzero scalar pivots and includes
all repeated-root strata.

All solved coefficients W_k, B and eta are affine in b: their weights
are respectively q-k, q, q-1, each less than 2(t+1). Write

    W=P+bQ, B=M+bN, eta=rho+b*sigma,
    Q(0)=-N, Q'(0)=sigma.

Then

    [b^3]F=-Q'/2+(N+Q)/x-sigma/2
           =-sum_(j=3)^t (j-2)Q_j*x^(j-1)/2.

The leading Q_t is -1/(2y(3d+2)). Consequently the row [x^(t-1)]F
has the scalar b^3 coefficient (t-2)/(4y(3d+2)), nonzero for t>=3.
This is a useful exact structural relation; it does not imply target
vanishing by itself.

On C=x^(t-1), weighted uniqueness gives

    B=eta=0,
    W=omega*x^q-b*x^t/(2y(3d+2)).

Direct substitution gives

    F=E*b^2*x^(2t)+(t-2)*b^3*x^(t-1)/(4y(3d+2)),
    E=((2t-1)/(3d+2)^2+3/(3d+2)
        -((2t-1)/(2d+1)+3)/2)/(4y^2).

Thus this monomial-C slice forces b=0 for all t>=3. At t=2,d=-1 both
coefficients vanish, explaining the free b-line.

The scalar E factors as

    E=3(d+1)(1-8d^2-9d^3)/(4y^2(3d+2)^2(2d+1)),
    N(E)=-9q^4(t-2)(27t^3+17t^2+t+2)
          /((t+1)^2(3t+2)^2(3t-1)^2(4t+1)).

Consequently E is a scalar unit on both factors for every t>=3, and
the top residual is a monic quadratic in b after scalar division.
The omega, high-pivot, B-pivot, Q-leading, E, b^3-axis and norm formulas
were independently verified as exact rational identities by
`controls_uniform_identities.py`; all seven markers passed.

## Exact controls

The residual-ring map from the direct coefficient ring is the identity
on c_i,b after the scalar elimination of w_k,B. The monomial order is
Singular wp(1,...,t-1,t+1); the generators are the remaining coefficients
in ascending x powers. No modular computation enters this table.

| t, d or field | Dimension | Field length | NF(B eta)=0 | NF((B eta)^2)=0 |
|---|---:|---:|---:|---:|
| 2, -1, y=1/5 | 1 | infinite | yes | yes |
| 2, +1, y=2/5 | 0 | 12 | yes | yes |
| 3, Q[d]/(3d^2-4) | 0 | 66 | no | yes |
| 4, Q[d]/(3d^2-5) | 0 | 338 | no | yes |

The user's proposed y=1/5 control requiring B eta to be nonzero is
incompatible with F1--F3. It is dimension zero that fails on this fibre;
B eta vanishes even in the nonreduced coordinate ring. For d=-1 let c=c1.
The direct equations are

    R2=441*c^8/2500-6*c^5*b/25-9*c^2*b^2/4,
    R3=102*c^7/25-93*c^4*b/5,
    R4=177*c^6/50-33*c^3*b/2,
    B=18*c^5/125-3*c^2*b/5,
    eta=3*c^4/10+9*c*b/2.

An exact row certificate is

    B*eta=(6c/5)*R2-(72c^2/1025)*R3+(171c^3/5125)*R4.

A standard basis, with primitive scalar normalizations, is

    (59*c^6-275*c^3*b, c^4*b, c^2*b^2).

Its radical is (c): the second and third relations force c=0 if b!=0,
and the first forces c=0 when b=0. The reduced solution family is

    C=x, W=-25*x^5/4+5*b*x^2/2, B=eta=0, b arbitrary.

At d=+1 the monomial-C expression is W=25*x^5/48-b*x^2/4 and its F3
residual is -2*b^2*x^4, so it only solves the equations when b=0.

Reproducibility files are `controls_emit_direct.py`, the four
`controls_t*_raw.sing` direct residual systems, the corresponding
`.sing`, `.log` and `_gb.txt` files, and
`controls_t2_certificate.py` / `.log`. All CAS jobs were foreground,
bounded by `timeout`, and passed through `stdbuf -oL`.

The t=8 modular homogeneous experiment ended with
`INCONCLUSIVE_TIMEOUT` after 1800.070965 seconds. Before std, all scalar
pivots, leading and low coefficients, weighted homogeneity, origin, and
positive/negative controls passed. No standard basis, dimension, length,
or target membership result was obtained. Nothing is promoted at t=8.
The result and complete process metadata are in
`controls_t8_guided/guided_gb_result.json`. Its only permitted
characteristic-zero bridge was properness for the positively weighted
homogeneous ideal; a localized modular unit ideal was never used.
The timed-out process and the subsequent small exact identity-check
process were both reaped. No control task remains running.
