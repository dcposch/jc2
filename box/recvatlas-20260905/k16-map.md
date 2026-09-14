# K16 / (8.1): literal map audit and exact exceptional control

Status: the stipulated all-coefficient Newton receiver has no licensed
K16 pullback. The obstruction is the scalar unit coefficient
`[gamma*pi^0]P=-g`. This is present uniformly after the banked spine, and
is checked independently on the entire exceptional `t=2,d=-1` family.
No new K16 index is closed; `(8.1)` and `(T)` retain their charged status.

The root agent verified the frozen charged input receipt before this
subtask. This note uses the frozen K16 report's displayed `(REC)`, `(DEP1)`,
and `(DEP2)`, together with frozen Fable §1.2(b), §4.2, §4.4, and Card A.
The basic `h` and Laurent polynomial ansatz was additionally read from
existing box artifacts, read-only. Their actual SHA-256 hashes are saved
in `k16_map_check.json` under `extra_readonly_provenance`.

## 1. Separate the three rings and the two source ideals

Fix `t>=2` and a field factor of `Q[d]/(3d^2-t-1)`, extending to an
algebraic closure when discussing points. Set `q=2t+1`, `e=3t+1`, and
take the charged unit normalizers `y,g`, with `c=-yg != 0`.

The direct F3 coefficient ring is

    R_t = k[c1,...,c_(t-1),b].

The high F3 recurrence determines the charged polynomials `B,eta,W` in
that ring, and the positive necessary ideal is

    I_+ = (E2,...,E_(2t)).

The terminal constant is `T0=yg+tau`, where

    tau = -(gy/3)*B*eta mod I_+.

The full terminal chart uses `I_full=I_+ +(T0)`. The atom asks whether
`tau` belongs to `sqrt(I_+)`, equivalently whether `I_full` is the unit
ideal. These ideals must not be interchanged: the exceptional cone is a
point of `I_+`, and is not a point of `I_full`.

The ordinary polynomial chart has independent variables `(gamma,pi)`.
After the source reconstruction write

    z = pi-gamma,
    x = h-b4 = pi^3*(z+b1)+B*pi^2+b*pi,
    K = x^2*C-y*b,
    F_aux = x*T-g*b,
    Y = x*S-b*T-g*B.

Here `x` is the translated auxiliary polynomial used in frozen `(REC)`;
it is not an independent source coordinate after substitution. The
charged reconstructed pair has the form

    Q = U(x) + K(x)/pi + y*x/pi^2,
    P = P0(x) + Y(x)/pi + F_aux(x)/pi^2 + g*x/pi^3.       (K1)

`P0` differs from the integral called `V` in `(REC)` only by a constant
gauge (in the older normalization it is `V-g*b1`). Constants do not
affect any result below. The displayed rational expressions cancel to
polynomials, as the original ordinary chart or direct expansion shows;
the Laurent ring is only a convenient identity-checking ring.

In the quotient by the positive source ideal,

    J_(gamma,pi)(Q,P) = -c*(pi-gamma)+tau*pi
                      = c*gamma+(tau-c)*pi.            (K2)

Thus the positive cone supplies a general *linear* Jacobian. The full
terminal chart imposes `tau=c`, so it supplies `J=c*gamma`. By contrast,
the known exceptional cone has `tau=0` and `J=c*(gamma-pi)`.

## 2. A unit forbidden coefficient, before any CAS or point argument

The constant coefficient of `P` in `pi` has a linear gamma term:

    [gamma*pi^0]P = -g.                                (K3)

To prove this without any generic-root assumption, work in the formal
Laurent ring of (K1). Gamma first occurs in `x` at the term
`-gamma*pi^3`. A polynomial in `x` divided by `pi^r` for `r<=2` cannot
contribute a gamma term at pi-degree zero. The last term of (K1) is

    g*x/pi^3 = g*(pi-gamma+b1)+g*B/pi+g*b/pi^2.

Its coefficient of `gamma*pi^0` is exactly `-g`. Cancellation of the
negative pi powers does not change a nonnegative Laurent coefficient.
The additive `P0` gauge cannot change it. Since `g` is a scalar unit at
every permitted `t` and factor, (K3) is never an optional vanished-leader
branch.

The stipulated Newton condition for every coefficient `j>=0`,

    deg_gamma [pi^j]P <= 3*j,

requires the left side of (K3) to vanish. It is therefore incompatible
with the actual normalized K16 coefficient support. This is a
coefficient obstruction, not a coincidence of numerical invariants.

There is a nearby true weaker statement. A monomial `gamma^a*pi^j`
coming from (K1) obeys `3*a-j<=3`, because its denominator has degree at
most three and every occurrence of gamma contributes at least pi^3 in
the numerator. Consequently all positive pi coefficients obey the
proposed weak inequality `a<=3*j`, and the only possible forbidden
support at `j=0` has `a=1`. Removing the constant coefficient condition
therefore changes the system materially. Under that alternative reading,
the elementary all-j emptiness proof does not apply.

There is also a short countercontrol to the asserted implication from
pre-descent polynomiality. Put `y=gamma^(-1)` and
`sigma=gamma^2+pi*gamma^3`, a truncation with `u=1,v=3`. The polynomial

    H(y,z)=(y^3*z-y)^2+y*z

descends exactly to

    H(gamma^(-1),sigma)=pi^2+gamma^2*pi+gamma.

This is polynomial and monic in pi, but its constant pi coefficient is
gamma. Hence original polynomiality and descended monicity by themselves
do not give the proposed support bound. The omitted truncation terms
allow cross-layer pole cancellations. This example is not asserted to
be a Keller pair, a Moh-admissible branch, or a counterexample to any
source theorem with additional hypotheses. It pinpoints the failed
algebraic inference in Fable's stated derivation. The driver verifies
the substitution exactly.

## 3. Literal critical-line homomorphism and its localization

Introduce receiver source variables `(Gamma,Pi)`, kept distinct from
coefficient variables. Over `R_t/I_+`, the coordinate substitution

    chi: R_t[gamma,pi] -> R_t[Gamma,Pi],
    gamma |-> Gamma+(1-tau/c)*Pi,
    pi    |-> Pi                                         (K4)

has determinant one and inverse
`Gamma=gamma+(tau/c-1)*pi`, `Pi=pi`. It uses only the scalar unit `c`.
Applying the chain rule to (K2) gives

    J_(Gamma,Pi)(chi(Q),chi(P)) = c*Gamma mod I_+.

This is a literal ring map, and the equality follows by substituting
the source coefficient rows. It is a valid pullback to the receiver
with arbitrary polynomial support and linear Jacobian.

It is not a pullback to the stipulated all-j Newton receiver. Indeed

    [Gamma*Pi^0]chi(P) = -g.                             (K5)

On the atom chart `tau!=0`, declare the localization

    A_t = R_t[tau^(-1)]/I_+.

Put `kappa=tau/c` and `lambda=c/tau`. The leading pi^4 coefficient of
`chi(h)` is `kappa`, so the target scalings

    Qhat=lambda^q*chi(Q), P_hat=lambda^e*chi(P)

restore monicity of degrees `4q,4e`. They give

    J(Qhat,P_hat)=c*lambda^(q+e)*Gamma,
    [Gamma*Pi^0]P_hat=-g*lambda^e.                       (K6)

Every displayed multiplier is a unit in the declared localization.
The support failure therefore persists on precisely the chart used by
the atom. One cannot divide by `tau` on the exceptional `tau=0` cone;
that chart has to be retained separately.

For completeness a coefficient-level map to the *relaxed* receiver is
literal. Let its independent generators be `a_ij,b_ij,C,Cinv`, covering
all supports of `Qhat,P_hat`, with ideal generated by the coefficients
of `J(Quniv,Puniv)-C*Gamma` and `C*Cinv-1`. Declare

    a_ij |-> [Gamma^i Pi^j]Qhat,
    b_ij |-> [Gamma^i Pi^j]P_hat,
    C    |-> c*lambda^(q+e),
    Cinv |-> c^(-1)*lambda^(-q-e).                     (K7)

The universal Jacobian rows pull back into `I_+` by the exact source
identity and the chain rule; the inverse row pulls back to zero. The
forbidden support generator `b_10=0` of the requested receiver instead
pulls back to the unit `-g*lambda^e`. Thus (K7) does not descend to that
receiver unless the atom chart is already proved empty. Claiming that
descent as an input to the emptiness proof would assume the target
theorem.

On the full terminal chart, `tau=c` and (K4) is the identity. Formula
(K3) still blocks the requested support. Showing that this proper-support
map existed modulo `I_full` would itself require `1 in I_full`, the
unclosed `(8.1)` statement. The computation does not prove that no
unrelated homomorphism can exist into an already zero quotient; it
proves that the proposed coordinate reconstruction fails a necessary
image check and supplies no new emptiness theorem.

## 4. Exact free-b-axis negative control, derived from frozen REC

At `t=2,d=-1`, take the charged family

    y=1/5, g=7/125, c=-7/625,
    C=x, W=-25*x^5/4+5*b*x^2/2, B=eta=b1=0.

Direct substitution into F3 gives zero for every `b`. Integrating `(REC)`
and choosing its prescribed coefficient gauge gives

    U=x^5-b*x^2/2,    P0=x^7-7*b*x^4/20,
    T=14*x^2/25,     S=7*b*x/25+7*x^4/5,
    x=pi^3*(pi-gamma)+b*pi.

Use (K1) with `K=x^3-b/5`, `Y=x*S-b*T`, `F_aux=x*T-7*b/125`.
These are polynomial pairs over `Q[b]`. The independent SymPy driver
first asserts polynomiality, then computes the derivatives exactly:

    deg_pi Q=20, deg_pi P=28, both monic;
    J(Q,P)=7*(pi-gamma)/625;
    [pi^0]Q=0, [pi^0]P=-7*gamma/125.

Its full support scan finds exactly one violation of `a<=3*j`:

    polynomial P, exponent (a,j)=(1,0), coefficient -7/125.

All `j>=1` support inequalities pass on the whole b-family. Thus the
issue is not a finite truncation or an approximate numeric mismatch.
This family contradicts Fable Card A's assertion that its cone points
have the stipulated *all-coefficient* Newton shape. It does not
contradict the charged F3 or `(8.1)` calculations.

Set `Gamma=gamma-pi`, `Pi=pi`. Then the same exact pair has

    J_(Gamma,Pi)=-7*Gamma/625,
    [Gamma*Pi^0]P=-7/125.

The reorientation also changes its pi degrees to `(15,21)` with leading
coefficients `-Gamma^5,-Gamma^7`; it does not preserve monicity. This is
why the tau-zero branch cannot be silently treated using the localized
monic map of (K6).

Driver: `k16_map_check.py`. It uses exact rational SymPy operations and
no Groebner basis. It completed in approximately two seconds with
`OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1` under `timeout 60`.
The complete pair coefficients, outcomes, and supplemental hashes are
saved in `k16_map_check.json`. All processes from this subtask exited.

## 5. Consequences and non-consequences

The requested receiver, if interpreted for every `j>=0`, may be proved
empty by its own equations. That fact discharges **zero K16 branches
through the proposed map**: its source necessity fails the unit
coefficient check. The same failure affects the claimed deduction of
`(8.1)` from critical-line straightening.

The charged valid implication chain remains

    B*eta vanishes on V(I_+)
    <=> tau in sqrt(I_+)
    <=> (8.1)
     => K16 terminal chart empty
     => original K16 ray empty at that t
     => (T) at that t,

using exactly the charged cone lemma and source normalizer/spines.
The new receiver construction does not establish the first antecedent.
No all-t promotion or K16 milestone notification follows.

Typed atlas disposition for this proposed receiver:

    UNASSIGNED[K16-SUPPORT-PI0]
    obstruction: [Gamma*Pi^0]P_hat=-g*(c/tau)^e is a unit
    required replacement: a receiver admitting the source support,
                          together with a new emptiness/classification
                          theorem strong enough for its marked source.

No exit-price or exit-set claim is made, so no charge_basis line is due.
