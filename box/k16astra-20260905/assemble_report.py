#!/usr/bin/env python3
"""Assemble the bounded root report from reviewed proof blocks and root findings.

Never adds a BODY-END marker: sealing is a separate completion-only step.
"""
from pathlib import Path
import re,json
p=Path(__file__).resolve().parent
out=p.parent.parent/'xmodel/k16-8point1-astra-20260905.md'
def take(name,start,end=None):
    s=(p/name).read_text();s=s[s.index(start):]
    if end:s=s[:s.index(end)]
    s=s.split('\n',1)[1].strip()
    s=re.sub(r'^## ([0-9A-Z.]+)\.?(.*)$',lambda m:'### '+m.group(2).strip(),s,flags=re.M)
    return s+'\n'
parts=[r'''# K=16 structural atom: exact polynomial Abel reduction

Lane: `k16-8point1-astra-20260905`. Date: 2026-09-05.

**PARTIAL. The all-t nonexistence theorem is still OPEN.** No promotion of
theorem (T) on the whole ray is made. The new main result is an exact,
coefficient-sensitive reformulation of (8.1): for every t >= 2 and every
field factor, its failure is equivalent to a normalized polynomial solution
of the single Abel equation (F3) below with B eta != 0. This includes every
b3 chart, with explicit polynomial reconstruction and gauge fixing.

The accompanying uniform results are:

- The homogeneous constant row satisfies
  `tau + g*b2*R = -sum_{k>=1} b4^k*T_{t,k}`, with
  `R=U'(b4)+b3*C(b4)`. Hence (8.1) holds on the cone intersected with either
  hypersurface b2=0 or R=0. The remaining chart is exactly D(b2*R).
- The actual coefficients of the monic C, and also its translated
  coefficients in L=X-b4, are global polynomial coordinates of the base.
  The ordered-root cover is finite free, including root collisions.
- A height-free quadratic trace/norm criterion handles all positive rows,
  all finite slope charts, and the rank-zero fibres of the quadratic cover.
- A hypothetical tau != 0 point gives an immersive nonproper boundary
  with an off-diagonal collision scheme of exact length 6t^2. The bare
  tower has a uniform Belyi identity, but its passport does not force
  residual rigidity.

Fresh exact controls reproduce both t=2 fibres and t=3,4. In particular
tau is not in I+ at t=3,4, but tau^2 is. At t=4, tau^2 is NOT in the
top-tail ideal alone. These finite nilpotence observations are not
interpolated to all t. Bounded t=8 computations are recorded in Section 9.

## 1. Frozen provenance and ring convention

The sixteen frozen files in `/tmp/jc2-lane.vB6DJB/inputs` were checked
before mathematical work. The manifest was generated mechanically from
`xmodel/k16-8point1-astra-20260905.run.v2`, using awk to pair
`charged_input_<i>_basename` and `charged_input_<i>_sha256`; then
`sha256sum -c` returned OK for all sixteen. No hash digit was retyped.
The durable generated manifest is
`box/k16astra-20260905/input-manifest.sha256`.

Only the frozen charged mathematical reports, the frozen Moh PDF, and
new files in this lane were used locally. No ledger, jc2-lean, ideation
file, or other running lane report was read or edited. Primary external
papers used only for applicability audits are linked below and in the
bounded source notes. Their conclusions are not imported as atom proofs.

Put q=2t+1, e=3t+1 and

    H_t(y)=12q^2 y^2-12q(t+1)y+(t+1)(3t+2),
    A_t=Q[y]/(H_t), d=2qy-(t+1), 3d^2=t+1,
    y=(d+t+1)/(2q),
    g1=e/q, g2=e(d+q)/(2q^2),
    g=e*t*(3d+2t+2)/(6q^3), c=-yg.

The residual rings are

    P_t=A_t[b4,u2,...,u_(t-1)], S_t=P_t[b3],
    wt(b4,u2,...,u_(t-1),b3)=(1,2,...,t-1,t+1).

Here u_j is q_(j,0). Statements about a field are read on each field
factor of A_t and then over its algebraic closure. No nonzero class of a
product algebra is treated as a unit without a factorwise argument.
The normalizer gives units y,g; directly,

    N(y)=(t+1)(3t+2)/(12q^2),
    N(g)=t^2(t+1)(3t+1)^2(4t+1)/(36q^6).

Both norms are nonzero for every integer t >= 2. The solved variables
b1,b2 and the coefficients of U,C,S,T,V are polynomial functions on S_t,
using only the banked scalar unit pivots. They are not extra independent
variables in the terminal ideal.

## 2. Normalization, hypotheses, and the dependency to theorem (T)

The original frozen constant row is inhomogeneous:

    T_{t,0}=yg+tau_t, wt(tau_t)=4t+1,
    I_{t,+}=(T_{t,1},...,T_{t,2t-1}),
    J_tail=(T_{t,t},...,T_{t,2t-1}).

Thus throughout this report tau means T_{t,0}-T_{t,0}(0), exactly the
homogeneous target in frozen terminal-proof Section 8 and DEP Section 3.
Literal T_{t,0} cannot belong to radical(I+), because the origin lies on
the positive cone and T_{t,0}(0)=yg != 0. This fixes notation, rather than
claiming that the intended weaker route is false.

The safe equivalences and implications at each fixed t are:

    tau in radical(I+)
      <=> (I+, T_{t,0})=S_t                         [weighted cone lemma]
      <=> terminal unit statement (8.1).

For the forward implication, the image of tau in S_t/I+ is nilpotent,
so yg+tau has a finite geometric-series inverse. Conversely, if a cone
point p had tau(p) != 0, choose a nonzero scalar lambda with
lambda^(4t+1)*tau(p)=-yg. Positive homogeneity preserves all I+ equations
under the weighted action, while the rescaled T_{t,0} vanishes. This
contradicts the unit ideal. This argument is factorwise in characteristic
zero and allows positive-dimensional cone components.

The charged reduction chain, frozen hsop Section 9 and terminal-proof
Sections 5.2 and 8, is then

    (8.1) at t
      => terminal normalized receiver chart has no solution
      => no solution of the original ray system, by the banked constant
         spine, normalizer lemma, and second affine spine
      => theorem (T) at t.

A uniform proof of the polynomial Abel assertion (F1)-(F4) would supply
the first line for every t >= 3, and hence promote (T) on the whole ray.
This report proves the equivalence to that assertion, not the assertion.
The reduction hypotheses are not replaced by a conjectural length.

There are three important qualifications on the proposed Gamma route.
Frozen rank-criterion Section 0 states EN-CURVE with the hypothesis
`V(J_tail)={0}`; its proof first obtains regularity of the G_r from that
hypothesis. Thus the charged CM dimension-one/EN series conclusion is
conditional, not an independent all-t height theorem. Even if supplied,
CM dimension one does not imply DVR: the cusp local ring
K[s^2,s^3]_(s^2,s^3) is a counterexample. Valuations belong to normalized
reduced branches and do not by themselves determine the leading scalar.
Also an NZD lowers dimension by one; zero-dimensionality requires the
dimension-one hypothesis on S_t/(G). The radical Fitting statement is
safe without this circular use of height.

LENGTH-SPLIT is a correct numerical identity and has its stated
intersection interpretation after the relevant hypotheses. The b3-axis
is a component of V(G); for t >= 3, the unit top coefficient gives
Q|axis=a0*b3^2, so the axis meets the full terminal cone only at the
origin. It is not a proved positive-dimensional component of V(I+).
The weighted degree d_Gamma(3)=15/2 also must not be read as a literal
number of reduced geometric points. None of these corrections weakens
the direct (8.1) formulation used below.

## 3. Universal local factorization and its proved strata
''']
parts.append(r'''
Use x=L=h-b4. Here U,C,T,S,V denote translated polynomials, for example
U_x(x)=U_h(x+b4); subscripts are suppressed inside the differential
identities. Primes mean d/dx. Set

    K=x^2*C-y*b3, F=x*T-g*b3, Y=x*S-b3*T-g*b2,
    R=U_x'(0)+b3*C_x(0)=U_h'(b4)+b3*C_h(b4), wt(R)=2t.

Before any positive terminal row is imposed, the solved spine gives

    D3: 2y*T'=g*(5C+3x*C'),
    D2: -3g*x*U'+K*F'-2K'*F+2y*x*Y'-y*Y=yg*b2,
    D1: 2y*x*V'+K*Y'-K'*Y-2U'*F=yg*b1,
    D0=K*V'-U'*Y=yg-E_t(h)=-tau-sum_{k>=1}T_{t,k}h^k.

In the local proof, a polynomial evaluated at 0 means x=0, hence h=b4;
u=U_x'(0), C0=C_x(0), T0=T_x(0), and R=u+b3*C0. This distinction is
essential to the displayed ideal identity.
''')
parts.append(take('structural-notes.md','## 2. New universal boundary factorization','## 4. Next exact jets'))
parts.append('\n## 4. The new full polynomial Abel atom\n')
parts.append(take('structural-notes.md','## 4B. The full polynomial Abel atom','## 5. Hyperelliptic'))
parts.append(r'''
### Independent row-image check and the remaining truncation issue

The universal symbolic proof was independently tested against the fresh
coefficient-array reconstruction on both t=2 fibres and at t=3,4. Before
imposing any positive terminal equation, write F for the left side minus
the right side of (F3), with eta=3R/y. The generated driver verifies

    g*y*F(x)+3x*(D0(x+b4)-D0(b4))=0.

Here D0 in this display is in the original h coordinate. Consequently
the coefficients of F after the solved spine generate exactly I+:
multiplication by x only shifts indices, and h=x+b4 changes the
nonconstant coefficients by an invertible triangular transformation.
This is a generator-level image check, not merely agreement of dimensions.
All four logs contain ABEL_ROW_IDENTITY_PASS and no error marker.

There is no finite-jet contradiction hidden at x=0. On b=0, choose any
C(x) in K[[x]], any T(0), and B,u0,y,g != 0. D3 determines T; the
x^n coefficient of D2 determines Y_n with diagonal y(2n-1); D1 then
determines V'. In D0=x^2 C V'-U'Y, the unique highest-index term in its
x^n coefficient is gB*[x^n]U'. Thus one can solve recursively and
uniquely for a formal U' with D0 identically gB*u0 != 0. These formal
solutions need not truncate. This proves that a successful argument must
use the linked polynomial coefficients and normalized truncation, not
only a bounded list of local jets.

For b=0, (F3) specializes to (A2) in the structural notes. With
a=3x^3 C^2/(4y^2) and kappa=By*eta/3, its useful factorization is

    w H = 3/(16y^4) * (x A^4-4B y^2 A^2-16y^3 kappa),
    A=xC, H=(2xw'-w-B+2a)/x.

If kappa != 0, gcd(w,A)=gcd(H,A)=1, H(0)=w'(0) != 0, and
deg(w,H)=(2t+1,2t). Repeated roots of w or H remain possible. The
leading balance is exactly (4t+1)omega^2+2alpha*omega-alpha^2/3=0,
equivalent to 3d^2=t+1, so it supplies no contradiction.

## 5. Global approximate-root coefficient coordinates
''')
coords=take('audit-notes.md','## 5. A uniform change to the actual approximate-root coefficient variables','## 6. All-row minors alone')
aa=coords.index('### 5.1');bb=coords.index('### 5.2')
coords=coords[:aa]+r'''
The ordered-root extension of the universal monic C is finite free of
rank (t-1)!: adjoin a first root by a monic relation of degree t-1,
divide by that factor, and repeat with free degrees t-2,...,1.
Consequently this cover is faithfully flat and preserves radical
membership in both directions. This is a cover at fixed t, not a
deformation changing t. The following translated version makes the
relevant collision especially simple.

'''+coords[bb:]
parts.append(coords)
parts.append('\n## 6. A quadratic-cover criterion for the weaker target\n')
parts.append(r'''
This criterion is valid for every t >= 3, without a height, smoothness,
or reducedness hypothesis. Work over a field factor K. Let
Q=a*b^2+b0*b+c0 be the top row, with a a scalar unit, and divide
every other positive row and tau by Q in P[b]:

    H_i=v_i+u_i*b (i=1,...,2t-2), h=v+u*b,
    I+=(Q,H_1,...,H_(2t-2)).

Only a is inverted. Define in the base P

    J0=(u_i,v_i), M_ij=v_i*u_j-v_j*u_i,
    W_i=a*v_i^2-b0*u_i*v_i+c0*u_i^2,
    F=(M_ij,W_i), D_i=v*u_i-u*v_i,
    ell=2a*v-b0*u, nrm=a*v^2-b0*u*v+c0*u^2.

Then exactly

    tau in radical(I+)
      <=> all D_i in radical(F), and ell,nrm in radical(J0).

Proof: over the algebraic closure the finite projection V(I+) -> Spec P
has image V(F). At rank two a minor excludes the point. At rank one,
if all u_i vanish, a nonzero v_i has W_i=a*v_i^2 != 0. Otherwise some
u_r != 0 and the unique possible lift is b=-v_r/u_r; the minors impose
all H_i=0 and W_r tests Q=0. At this lift h=D_r/u_r, with all D_i
vanishing precisely when h does. This uses the union of every D(u_r).
At rank zero the whole quadratic fibre remains. The two values of h,
counted with multiplicity, have sum ell/a and product nrm/a; both
are zero exactly when ell=nrm=0. This also covers a double root in
characteristic zero. Rank-zero points are V(J0), which proves both
directions by Nullstellensatz and descent of radical membership.

The trace condition is indispensable: with Q=b^2-1, all H_i zero,
and h=b-1, every D_i and nrm vanish but h does not vanish at b=-1.
This is an audit control, not a K16 counterexample. Equivalently the
rank-zero test is ell and (b0^2-4a*c0)*u^2 in radical(J0), since
ell^2-4a*nrm=(b0^2-4a*c0)*u^2. The trace/norm form avoids extra charts.
''')
parts.append(r'''
The criterion also transfers actual base certificates to nilpotence,
without a height hypothesis. In A=S/I+, one has

    u_i*h=D_i, v_i*h=-b*D_i, J0*h=(D_i)A,
    a*h^2-ell*h+nrm=0.

The minors and norms generating F belong literally to I+ intersect P.
If ell,nrm belong ordinarily to J0, multiplication of the last identity
by h gives h^3 in (D_i)A. If D_i^(e_i) belong to F and
N=1+sum(e_i-1), then (D_i)^N=0 and tau^(3N) belongs to I+.
This is an effective certificate transfer once its memberships are
proved; no such membership is inferred uniformly from degree data.

Exact base tests at t=3 give ell,nrm in J0, D1,D2,D3 in F, D4 not in F
but D4^2 in F. At t=4, D1,D2,D3 lie in F and D4,D5,D6 do not, while
their squares do. These give exponents 6 and 12 by the transfer, weaker
than the direct exact exponent 2. Their degree audit is important:
the base F quotient has top weights 18 and 25, so the square memberships
are already degree-forced after those finite computations. They are
controls, not evidence of a new uniform square-zero identity.

A new sufficient rank condition uses Nfull of ALL 2t-2 reduced positive
rows. If radical(I2(Nfull))=m_P, every cone point has base point zero,
since (1,b3) lies in its matrix kernel; Q|axis=a*b3^2 then forces
b3=0. This requires no norm generator or EN height. Exact tests give
P/I2(Nfull) dimension zero, lengths 85 and 503, top weights 18 and
26, at t=3,4 respectively. Its all-t extension is OPEN; expected
codimension is not a proof. Logs: audit_minors_t3.log and audit_minors_t4.log.

## 7. Marked boundary geometry and why the suggested shortcuts do not close
''')
parts.append(take('moh-linear-jacobian.md','## 2. Every K16 chart pair is nonproper','## 5. Primary nonproperness source check'))
parts.append(r'''
### A uniform bare-tower Belyi identity

At the residual origin put v=pi*h^t,
f(v)=v^2+v+y and G(v)=v^3+g1*v^2+g2*v+g. The exact normalizer identity is

    v*(q*f*G'-e*f'*G)-f*G=-yg.

It follows by expansion and reduction modulo 3d^2=t+1; the universal
driver belyi_identity.py checks it symbolically. Therefore

    R(v)=G(v)^q/(v*f(v)^e),
    R'(v)=-yg*G(v)^(q-1)/(v^2*f(v)^(e+1)).

Since yg is a unit, f,G are squarefree and coprime. R has degree
6t+3 and precisely the ramification partitions

    over 0: (q,q,q), over infinity: (e,e,1),
    over 1: (5,1^(6t-2)).

The last index follows from R(v)=1+(yg/5)*v^(-5)+O(v^(-6)). Both
t=2 factors have exactly this passport even though their cone dimensions
differ. Arbitrary residual points do not come equipped with the bare
cyclic quotient. Three-point-cover rigidity or this passport alone
therefore cannot decide V0 or establish (8.1). The full proof and exact
t=2,3,4 controls are in moh-notes.md and belyi_identity.log.

### Source applicability and residue moments

The frozen Moh paper, printed pp.148-149, Theorems 1.1-1.2, requires a
coherent complete system of root discs and yields approximate-root
coefficient valuation bounds. Its p.208 application produces the tower;
it does not state the remaining nonzerodivisor theorem. Recognizing the
tower is therefore not a fresh application discharging the atom.

No classification theorem found in the bounded primary-source check
excludes the required Abel polynomial solutions. The hypotheses of
the first-kind polynomial-coefficient theorem in
[Bravo et al., arXiv:2109.07853](https://arxiv.org/abs/2109.07853)
do not match the reciprocal equation, which has a linear term and
unavoidable poles. The equivariant second-kind theorem audited in
abel-source-audit.md requires the absent linear coefficient condition;
our coefficient B-2a has nonzero constant B. Solution-count bounds do
not exclude a single solution. No external classification is promoted.

The two tower charts glue to an O(-3) affine-line torsor over P^1.
The exact forms Q^a*P^b*dQ wedge dP give uniform residue moments;
each uses only L-jets through 2a+3b+4. The first is already the
boundary identity; the tested P-moment on b3=b1=0 also follows from
the spine. The necessary Q,P,Q^2 moments are derived in
moment-residues-notes.md and recorded in moment_residues.log.
Bezout coefficients in K[h] cannot be replaced by elements of K[U,V]
without controlling the boundary collisions. No vanishing follows here.

## 8. Exact foreground controls and reproducibility

emit_arrays.py reconstructs the coefficient arrays directly from the
frozen tail_structure.py formulas, in the L coordinate, translates to h,
and solves the 2t+1 weight-ordered scalar pivots. It checks affinity,
scalar/nonzero pivots, every eliminated variable, every high band,
the banked axis coefficient, the constant shift, and the new boundary
and Abel identities. It reads no previous generated row file.

The residual generator order for exact files is
(b4,u2,...,u_(t-1),b3), with weights (1,2,...,t-1,t+1).
At t=3,4 the coefficient fields are Q[d]/(3d^2-t-1), respectively
Q(sqrt(3)) and Q(sqrt(15)); both embeddings are covered by exact field
identities. At t=2 each rational factor is run separately. A separate
frozen SymPy reconstruction at t=3 matches every T_k exactly after
d -> 2qy-(t+1), not merely the leading coefficient or dimension.

| index/factor | dim S/I+ | length over field | least N: tau^N in I+ | dim tail | tail length |
|---|---:|---:|---:|---:|---:|
| t=2, y=1/5 | 1 | infinite | 1 | 1 | infinite |
| t=2, y=2/5 | 0 | 12 | 1 | 0 | 14 |
| t=3 | 0 | 66 | 2 | 0 | 90 |
| t=4 | 0 | 338 | 2 | 0 | 572 |

The full original T0 has nonzero normal form in every control. At t=3
the Q-vector-space length is twice the field length, namely 132;
there is no discrepancy with the charged rational-ring control.
The t=2 negative control proves that no zero-dimensionality test has
been silently substituted for the weaker radical condition.

The saved exact full-ideal bases have top weighted degrees 7,14,21
for t=2 positive, t=3, t=4. Standard monomials were enumerated by an
independent integer driver, giving the same lengths. Thus b3*tau=0
at t=3,4 is degree-forced there and is not a discovered all-t syzygy.
At t=4, reduce(tau^2,GB(J_tail)) is nonzero. Once the exact tail
dimension/length is known, its regular-sequence Hilbert series has
socle weight 35, which proves tau^3=0 in that fixed quotient because
its weight is 51. This is a fixed-index consequence of proved
finiteness, not the refuted uniform degree-bound argument.

The direct t=4 tail job was deliberately stopped during the unnecessary
raw tau^3 reduction, after its exact dimension, length, and nonzero
tau^2 result had returned. Its termination-time tau^3 output is not
accepted as a completed reduction; the explicit graded argument above
supplies that result. An early t=8 row-generation implementation was also
stopped after its pivot checks because term indexing was quadratic;
the replacement groups coefficients with coef(f,h), passes an exact
t=3 byte comparison, and completes. Neither stopped suffix is reported
as a completed calculation or a mathematical nonresult.

Additional exact image controls:

- t=3,4: every C-coordinate coefficient matches its uniform formula.
- t=2 both factors and t=3,4: boundary identities and the full Abel
  row identity pass before imposing the cone equations.
- t=3,4: R is neither proportional to d(b2)/d(b4) nor in the Jacobian
  ideal generated by the partial derivatives of b2. The simple
  potential/gradient shortcut is therefore rejected exactly.
- At t=4, S/(I+ +(b3)) has length 143 and top weight 17, and its
  weight-17 tau class is nonzero. Thus tau is NOT in I+ +(b3),
  ruling out the square-zero factorization through b3. The exact
  t=3 slice has length 29 and top weight 10, and tau vanishes there.

Driver invocations use `timeout 1800 stdbuf -oL`, in the foreground.
Representative replays, from the workspace root, are:

    python3 box/k16astra-20260905/emit_arrays.py 3 --out /tmp/fresh_t3_rows.sing > /tmp/fresh_t3.sing
    timeout 1800 stdbuf -oL Singular -q /tmp/fresh_t3.sing
    timeout 1800 stdbuf -oL python3 box/k16astra-20260905/sympy_crosscheck.py 3
    timeout 1800 stdbuf -oL python3 box/k16astra-20260905/structural_abel_general.py

The supplied driver files and logs are the durable reproductions;
the /tmp paths above illustrate an overwrite-free replay. No modular
localized ideal or modular nilpotence calculation is promoted.

## 9. Bounded t=8 computations

The fresh modular recurrence at t=8 uses p=32003 and d=31750,
equivalently y=11288. It passes all seventeen scalar pivots and both
local identities. Two single-core foreground jobs test the full
positive cone and the top-tail cone (the latter with the CI numerator
as a computation hint). Their final run outcomes are recorded below;
neither a Hilbert hint nor a predicted length is itself a certificate.
''')
for tag in ['t8p_plus','t8p_tailhint']:
    log=(p/f'{tag}.log').read_text() if (p/f'{tag}.log').exists() else ''
    done='CONE_COMPLETE' in log and '?' not in log and 'FAIL' not in log
    outcome=json.loads((p/'run_outcomes.json').read_text())[tag]
    status='COMPLETED; see exact markers below' if done else f"INCONCLUSIVE_TIMEOUT; exit {outcome['returncode']}; no mathematical conclusion"
    markers='\n'.join(x for x in log.splitlines() if x.startswith(('CONE_','GB_DONE','INPUT_','BASIS_','LEAD_')))
    parts.append(f'\n**{tag}: {status}.**\n\n```text\n{markers}\n```\n')
parts.append(r'''
Both jobs stopped at their 1800-second limits and were reaped. Neither
produced a dimension result, and no t=8 promotion is made. A future
homogeneous dimension-zero result would require properness for promotion.
The local coefficient ring is a localization of
Z[d,1/3]/(d^2-3) at (32003,d-31750). All fixed denominator integers are
smaller than the prime, y and g are nonzero, and each actual scalar
pivot has been tested nonzero, so the modular recurrence is the image
of the rational recurrence over this local domain. No conclusion about
an inhomogeneous unit ideal is licensed by this arithmetic model check.

## 10. Exact residual, t-range, and next step

The boundary and coordinate lemmas and full Abel equivalence hold for
every t >= 2; the quadratic-cover criterion holds for t >= 3, factorwise.
The previously charged
characteristic-zero range for (8.1), hence (T), is t=2 on both factors
and t=3,...,7; the stronger tail result is charged through t=6.
The current lane independently checks the requested t=2,3,4 controls.
No fixed range is extrapolated to all t.

The remaining global assertion is precisely:

    for every t>=3 and both d with 3d^2=t+1,
    every normalized polynomial C,W,B,b satisfying (F1)-(F3)
    has B*W'(0)=0.

Equivalently, in the original residual ring it is

    1 in (I_{t,+}, 1-z*b2*(U'(b4)+b3*C(b4))) in S_t[z].

Both formulations retain rank-zero points, root collisions, b3=0,
and all components of any dimension. They are equivalent to (8.1),
not merely sufficient tests for V0. No all-t solution of either
remaining assertion is contained in this report.

The most promising next step is a coefficient-sensitive polynomial
solution theorem for (F3). Its linked coefficients A=3x^3C^2/(4y^2)
and D=3bxC/(2y), fixed leading omega, and reconstruction are stronger
data than the degrees alone. Work in the translated C coordinates
or their finite free ordered-root cover; repeated roots must remain
in the argument. The b=0 factorization is a simpler subcase, but a
proof confined to that subcase cannot close the ray. The marked
boundary collision/moment formulation offers a complementary route
to the same missing global rigidity. Moh's existing coefficient
bounds and generic Abel solution-count theorems do not supply it.

## 11. Fallacy audit and completion record

- All constant-row shifts and signs are explicit and checked against
  both t=2 factors. Literal T0 is never used as the homogeneous tau.
- CM, expected height, and length interpretations retain their
  hypotheses. No dimensional conclusion is inferred from a degree
  formula, Hilbert hint, or an unproved regular sequence.
- The full Abel derivation uses only scalar units and exact polynomial
  divisions by x with zero constant numerator. It never discards a
  residual zero set. The finite-cover criterion uses all slope charts
  and separately tests the rank-zero quadratic fibre.
- Root covers are finite free at fixed t; this is not a deformation
  changing the number of variables t. No flatness/semicontinuity leap
  across indices is asserted.
- Characteristic-zero computations use declared exact field maps.
  A modular result can be promoted only through properness of a
  homogeneous cone, with its arithmetic model verified separately.
- Formal local series, compactified boundary points, affine points,
  and weighted-projective degrees are kept distinct. The formal
  solutions above are not polynomial counterexamples.
- The banned weighted Froberg, coprime-leader, degree-only resultant,
  and pure degree-bound tower routes were not retried as proof routes.
  The low-degree collision Bezout calculation concerns its explicitly
  proved two-variable leading forms, not the terminal ideal.
- No new exit-price assertion is made, so no charge_basis line is due.

All CAS jobs have exited and been reaped. Three independent reviews found
no load-bearing gap in the full Abel equivalence; their notation and
quantifier corrections are incorporated. The driver directory contains
`run_outcomes.json`, `artifact_checks.json`, and `artifacts.sha256` for
the final outcomes, accepted checks, and artifact custody. The result
is PARTIAL: the all-t theorem remains OPEN.
''')
body='\n'.join(parts).replace('tool,'+chr(92)+'+not','tool,\nnot').replace('tool,+not','tool,\nnot')
body=body.replace('same omega as in (A7)','omega specified in (F1)')
body=body.replace('unavoidable poles','the poles produced by the displayed substitutions')
body=body.replace('Fix t and a field factor as above.',
    'Fix t and an algebraic closure of a field factor of A_t. All polynomial solutions in this section are sought over that algebraic closure.')
body=body.replace('lower-weight terms','terms in earlier variables of the same total weight')
body=body.replace('is a polynomial immersion under the hypothesis tau!=0.',
    'is a polynomial parametrization with nowhere-vanishing differential when tau!=0. Here "immersive" refers only to this differential condition, not to a locally closed embedding.')
body=body.replace('the parent\'s pole-elimination','the independently derived pole-elimination')
body=body.replace('the parent\'s','the root lane\'s').replace('parent\'s','root lane\'s')
print('REPORT_BYTES',len(body.encode()),flush=True)
assert 20000<=len(body.encode())<=45000
out.write_text(body)
