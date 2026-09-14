# Independent actual constant-Jacobian row, bounded reordered check

Both checks adjoin the necessary scalar `J(F,G)(0,0)-Jc`, with the **same**
retained `Jc` used in the D1 identity and nonzero wrapper. They start from
immutable copies of the quotient transition: delta2 after global J bands
through 66, gauge dimension 230; delta52 through 89, gauge dimension 44.
The copied state and phase hashes, map, free ring, old residuals, new row,
normal-form relation, and exact Singular scripts are recorded in the artifacts.
These checks reorder one required row. They neither complete missing bands
nor prove a survivor of the entire chart.

* Delta2: `print-audit-corner-quotient-delta2.json` is PASS, NONUNIT,
  full gauge dimension **229**. The combined row has 2,562 terms.
* Delta52: `print-audit-corner-numberfield-delta52.json` is PASS, NONUNIT,
  full gauge dimension **43**. The actual ordinary row has 676 terms and its
  combined normal form has 448 terms. Their difference is exactly divisible
  by the retained monic quadratic; see
  `print-audit-corner-delta52-raw-vs-nf.json`.

All products use the complete first physical Taylor polynomials of the seven
source blocks. For a block normalized by degree D, the normalized z slots
(D,0), (D-1,0), (D-1,1) give value c[D,0], x derivative
c[D-1,0]-c[D-1,1], and y derivative c[D-1,1]. Thus rebuilding
H=h^3+C2*h+C3, F=H^3+A2*H+A3, G=H^2+B1*H+B2 preserves the exact
origin Jacobian. Replacing z by w-1 gives those derivative values directly
in the corresponding w slots. The t^163 w^0 normalized bracket is exactly
the same global constant. Higher Taylor terms cannot contribute to a first
derivative at the origin; their coefficient variables remain in the declared
full ring and map.

The native corner arithmetic reduces only modulo the already retained monic
quadratic q, and emits one combined scalar A+B*d. It never splits A and B.
The ordinary delta52 computation independently verifies the complete scalar
before this reduction. `print-audit-corner-runtime-control.json` freezes the
audit-only backend and verifies exact rational/monomial decoding, including a
negative control for local SymPy1.12's conversion of FLINT integer exponents
into floating exponents. The first local attempt was rejected by the exact QQ
exporter; its artifact is explicitly REJECTED_LOCAL_FLOAT_EXPONENT. The used
backend differs only by casting each exponent to Python int before decoding.

## Exact delta52 transport, with both complex embeddings

Let d=Zface_H2_2, e=Zface_H2_5, a=283/3500658,
b=37/20415837456. The retained equation is

    q=d^2-a*d*e^2+b*e^4.

The old residual ideal consists of four further D1 consequences of q,
`ZJ*J-1`, q, and (after this check) the corner row, with c inverted. These
are the actual saved residuals, not assumed equations. The driver verifies
every old row under the following map.

The saved J is weighted homogeneous of weight 13 for weights (d,e)=(2,1),
and every monomial has a positive e exponent. Consequently e is already a
unit: in the old quotient, its explicit inverse is U=ZJ*(J/e), because
`e*U-1=ZJ*J-1`. Set R=d*U^2. Then R satisfies
q0(R)=R^2-a*R+b. The discriminant is negative, so q0 is irreducible over Q.
Use the exact field K=Q[R]/q0, while **retaining e as a Laurent variable**.
Neither e=1 nor the generic field Q(e) is used.

After d=R*e^2, J=e^13*C(R), where the recorded linear polynomial is

    C(R)=899024633/19400965606745691058340631684797544164189037312
         -9707329957*R/2217760128800376206943373535070592611361344.

The driver computes the exact inverse of C modulo q0, verifies its Bezout
identity, and computes its nonzero field norm

    169/8255130439244578066486725184296422710517831112479039636314076088366764900352.

The forward map is d -> R*e^2 and ZJ -> C(R)^(-1)*Einv^13,
with e*Einv-1 retained. Its inverse maps Einv -> U and R -> d*U^2.
The relation q0 maps to U^4*q modulo e*U-1. The equality
C(R)=U^13*J and the verified Bezout identity prove that the image of ZJ
under the round trip is ZJ; the other generators round trip immediately.
Thus this is an isomorphism of the already localized Q-algebras, including
the transported corner row. It makes no further chart restriction.
K tensor C has both roots of q0, so passing to K chooses neither complex
component. Dimension and the unit-ideal question are preserved.

Exact Singular in this coefficient field returns active-ring dimension 10
and reduce(1,GB)=1. Both c-localization wrapper controls return the expected
0 and 1. There are 33 untouched full-chart coordinates, hence total gauge
dimension 33+10=43. The transported ring retains e, Einv, c, and Zc, with
both inverse equations. All generator orders and integer denominator scales
are explicit. The successful driver takes about three seconds.

The two direct QQ delta52 Gröbner attempts reached their 600-second limits
and are explicitly COMPUTE_BOUND_IN_CORNER_GROEBNER. The ordinary delta2
expansion was stopped after 616 seconds and has a separate explicit
COMPUTE_BOUND_IN_ORDINARY_CORNER_EXPANSION receipt. These abandoned attempts
do not replace the successful exact checks above. No artifact used for a
conclusion remains pending.
