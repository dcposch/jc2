# Fable5.1 FIRST: finite-target asymptotic residue for graph subalgebras

First action 2026-09-12 11:33:59 UTC. Reserve 11:50 / HARD 11:53 UTC, never
reset. Different-model hostile FIRST of ROOT's manual producer report
graph-asymptotic-residue-root-20260912.md. All three snapshots in the lane
inputs directory were hashed before any body was read; all three matched the
expected pins (custody section). WHOLE read order: COORDINATION.md, the Astra
constant-graph control, the ROOT source. Independent manual reconstruction;
no interpreter, CAS, code, network, git, agents, corpus or scratch writes.
Only this file is authored, via apply_patch. The accepted constant-graph
theorem and the separate quadratic collision proof are NOT re-reviewed.
Mathematics remains PROVISIONAL; this report is the FIRST, not a promotion.

## Verdict summary

| Part | Verdict |
|---|---|
| A. source curve, p_H q_H r_H | CONFIRMED |
| B. infinity places, e, orders | CONFIRMED |
| C. residue -e f_{m-1}/(2 f_m) | CONFIRMED |
| D. all-degree necessity | CONFIRMED |
| E. h=k v^d zero-residue control | CONFIRMED |

Combined theorem: section 6. Own controls: section 7. Exclusions: section 8.

## 1. Part A: the source curve r_H=0 and the three restricted maps

Literal data (ROOT's P,Q,R agree with Astra's P=z u^3+y^2 u(3u+1) etc. at
u=1+v, since 3u+1=3v+4). Set t=1/x, v=xy, so x=1/t, y=tv, y^2=t^2 v^2, and
H=c+t^2 v^2 h(v). Direct substitution, done by hand:

    r_H = 2/t - 3v/t - (c+t^2 v^2 h)/t^3 = (2-3v-v^2 h)/t - c/t^3
        = f(v)/t - c/t^3.

So on x!=0, r_H=0 iff t^2 f(v)=c. Since f(0)=2!=0, the affine curve
D={f(xy)=c x^2} never meets x=0, so D is exactly this curve and r_H=x(f-cx^2)
vanishes on it. For p_H, replace c by t^2 f(v):

    p_H = t^2 (1+v)[ f(1+v)^2 + v^2 h (1+v)^2 + v^2(3v+4) ].

The h-terms cancel because f+v^2 h=2-3v; then
(2-3v)(1+v)^2 = 2+v-4v^2-3v^3 and adding 3v^3+4v^2 leaves v+2. Hence
p_H=t^2(v+1)(v+2). For q_H:

    q_H = t[ v + 3(1+v)^2(2-3v) + 3v^2(3v+4) ]
        = t[ v + 6+3v-12v^2-9v^3 + 9v^3+12v^2 ] = t(4v+6).

ROOT's inner identity f(v+1)^2+v^2[(v+1)^2 h+3v+4]=v+2 is the same
cancellation. Two numeric spot checks (h=1,c=1): at (v,t)=(0,1/sqrt2),
x=sqrt2,y=0,H=1: p_H=1, q_H=3 sqrt2, r_H=2sqrt2-2sqrt2=0, matching
t^2*2=1 and 6t. At (v,t)=(1,i/sqrt2): x=-i sqrt2, y=i/sqrt2, xy=1, H=1/2;
p_H=4-7=-3 = t^2*6; q_H=i/sqrt2-6i sqrt2+(21/2)i sqrt2 = 5i sqrt2 = 10t.
No ambient Jacobian identity, collision theorem, image theorem or guessed
normalization enters. **A: CONFIRMED.**

## 2. Part B: infinity places, ramification, local orders

D is a nonempty curve (the coefficient of x^m y^m in f(xy)-cx^2 is f_m=-h_d
!=0, m=d+2>=2). On every irreducible component v=xy is nonconstant (a
constant v=v_0 forces cx^2=f(v_0), so x constant, a point), hence t=1/x is
nonconstant too. So v:D~ -> P^1 is surjective and places over v=infinity
exist on the normalized projective model of each component.

Local model: with w=1/v the equation is t^2 F~(w)=c w^m,
F~(w)=f_m+f_{m-1}w+...+f_0 w^m, F~(0)=f_m!=0. The fibre over w=0 is t=0
only; the chart t=infinity contributes nothing since F~(0)!=0. So every
place over v=infinity has t->0, and:

- m even: t=+-w^{m/2}A(w), A^2=c/F~(w), A(0)^2=c/f_m!=0; the square root
  is a unit power series (recursion divides by 2A(0)). Two smooth branches,
  uniformizer w, e=1. If f=f_m g(v)^2 (possible only for m even; e.g.
  h=-9/8 gives f=2(1-3v/4)^2), D splits into two rational components
  t g(v)=+-sqrt(c/f_m); each carries one such branch, still e=1. ROOT's
  "choose either component" is correct.
- m odd: ord_w(c/f)=m is odd, so the place is ramified, e=2. With w^2=1/v,
  t=+-w^m A(w), A^2=c/(f_m+f_{m-1}w^2+...+f_0 w^{2m}); substituting back
  gives t^2 f(v)=A^2(f_m+f_{m-1}w^2+...)=c identically.

Exact orders at the selected place (uniformizer w in both cases):

    ord t = em/2,  ord v = -e,  ord x = -em/2,  ord y = e(m-2)/2,
    ord p_H = e(m-2),  ord q_H = e(m-2)/2,  r_H = 0.

These are equalities, not bounds, since (v+1)(v+2) and 4v+6 have exact
orders -2e and -e. For m>=2 all three target coordinates are regular, so the
restricted map extends across the place to a finite point of A^3:
(0,0,0) for m>2, and (c/f_2, +-4 sqrt(c/f_2), 0) for m=2. Whether that
point has a finite source preimage is irrelevant to D below. The source
point is genuinely at infinity (x has a pole of order em/2). There is no
extra factor in the even case: e=1. **B: CONFIRMED.**

## 3. Part C: the residue

With x=1/t, y=tv: x dy=(1/t)(t dv+v dt)=dv+v dt/t. Differentiating
t^2 f(v)=c gives dt/t=-(f'/f)dv/2, so on D

    x dy|_D = dv - (v/2)(f'/f) dv,

a form in C(v)dv, i.e. it descends to P^1_v. Writing f'/f=sum 1/(v-a_i)
over roots with multiplicity, f'/f=m/v+(sum a_i)/v^2+O(v^-3) and
sum a_i=-f_{m-1}/f_m=-A. Hence

    x dy|_D = (1-m/2)dv + (A/2)dv/v + O(v^-2)dv.

At w=0: dv=-dw/w^2 is exact (residue 0), dv/v=-dw/w has residue -1, and
O(v^-2)dv=O(1)dw is regular. Base residue: -A/2. Pulling back through a
place of ramification e multiplies dw/w by e up to a regular term, exact
forms stay exact, regular forms stay regular. So

    Res_P(x dy) = -e f_{m-1}/(2 f_m),

which I also rechecked in the odd case directly: v=w^-2, dv/v=-2dw/w.
Specializations: h=k!=0 gives f=2-3v-kv^2, m=2, f_2=-k, f_1=-3, e=1,
Res=-3/(2k). For deg h=d>=1: m=d+2, f_m=-h_d, f_{m-1}=-h_{d-1} (the term
-3v cannot reach degree d+1>=2), Res=-e h_{d-1}/(2h_d). Nonzero iff
f_{m-1}!=0, since e in {1,2}. Sign check by the residue theorem on P^1_v:
finite residues of x dy|_D are -a_i/2 with multiplicity, summing to A/2,
balancing -A/2 at infinity. **C: CONFIRMED.**

## 4. Part D: all-degree necessity

Suppose alpha is a polynomial one-form on A^3 (coefficients in C[p,q,r])
with d(phi_H^* alpha)=dx wedge dy. Then phi_H^* alpha - x dy is a closed
polynomial one-form on A^2; F(x,y)=int_0^x a(s,y)ds+int_0^y b(0,s)ds is a
polynomial primitive (only polynomial integration; F_y=b follows from
a_y=b_x). So phi_H^* alpha - x dy = dF with F in C[x,y]. This identity of
polynomial forms on A^2 pulls back along the normalization of any component
of D to an identity of rational differentials on D~.

At the selected place P: every coefficient a_i(p_H,q_H,r_H)|_D is a
polynomial in functions of order >=0 (section 2), hence in the local ring
at P; each d(p_H|_D) etc. is d of a regular function, hence regular. So the
pullback of ANY target-polynomial alpha is regular at P and has residue 0.
Also dF|_D=d(F(1/t,tv)) is d of a rational function on D~, whose Laurent
expansion has no w^-1 dw term, residue 0. Therefore Res_P(x dy|_D)=0,
contradicting -e f_{m-1}/(2f_m)!=0. No degree bound on alpha or F is used.

Why nothing else is needed: the argument lives on one place of one
component of D. The target point is used only as a point where polynomials
are regular. No second source branch, no statement about phi_H(A^2) or its
normality, no smoothness of the target point inside any image hypersurface,
no finiteness/injectivity of phi_H, and no full-preimage property of D
enters. The contrast is exactly target vs source coefficients: x itself has
a pole of order em/2 at P, so a primitive with source coefficients (such as
x dy) is not excluded and must not be substituted for alpha.

Pair to primitive: if F0,G0 in B_H=C[p_H,q_H,r_H] have J(F0,G0)=j in C^*,
choose any F1,G1 in C[p,q,r] with F0=F1(phi_H), G0=G1(phi_H) (they exist by
definition of B_H; nonuniqueness is harmless). Then alpha=(1/j)F1 dG1 is
target-polynomial and d(phi_H^* alpha)=(1/j)dF0 wedge dG0=dx wedge dy.
Hence no such pair exists at any degree. **D: CONFIRMED.**

## 5. Part E: the h=k v^d control

For h=k v^d, k!=0, d>=1: f=2-3v-k v^{d+2}, m=d+2>=3, f_m=-k, f_{m-1}=0
(degree m-1=d+1>=2 is untouched by 2-3v). So A=0 and Res_P=0 at every
place over v=infinity, both parities. The adjusted global source form
x dy-(1-m/2)d(xy) restricts to (A/2)dv/v+O(v^-2)dv=O(v^-2)dv=O(1)dw on the
base, regular at w=0; its pullback to an e=1 or e=2 place is regular. So
the principal part of x dy at these places is exactly the exact form
(1-m/2)dv, and no residue or principal-part computation at these same
places can distinguish x dy from a regular form modulo exact forms. This
retires only that local test. It supplies no target primitive, no B_H pair
and no exactness statement; the A=0 stratum stays undecided. This is a
genuine member of the family (same P,Q,R, same graph shape), not a surface
control. **E: CONFIRMED.**

## 6. Combined theorem (as reconstructed)

Let c in C^*, h in C[v] nonzero of degree d>=0, H=c+y^2 h(xy),
phi_H=(p_H,q_H,r_H) the restriction of the literal P,Q,R to z=H, and
B_H=C[p_H,q_H,r_H] subset C[x,y]. Put f(v)=2-3v-v^2 h(v), m=d+2,
f_m=-h_d, and f_{m-1}=-3 (d=0) or -h_{d-1} (d>=1). If f_{m-1}!=0 then
(i) no polynomial one-form alpha on A^3 satisfies d(phi_H^* alpha)=
dx wedge dy, and (ii) no F0,G0 in B_H have J(F0,G0) in C^*, at every
polynomial degree. In particular (ii) holds for every H=c+k y^2 with
ck!=0, so ROOT's quadratic conclusion is accepted via this proof. When
h=k v^d (d>=1) the places over v=infinity have zero residue and this test
is silent. Nothing is asserted for h=0, c=0, general H, or JC2.

## 7. Own manual controls

1. **Residue theorem on P^1_v** (section 3): finite residues sum to A/2,
   the infinity residue is -A/2; fixes sign and normalization independently
   of the Laurent expansion. At m=2: roots of kv^2+3v-2 sum to -3/k, finite
   sum 3/(2k), infinity -3/(2k).
2. **Globally split case h=-9/8, c arbitrary**: f=2(1-3v/4)^2, components
   t(1-3v/4)=+-sqrt(c/2). Directly dt/t=-dv/(v-4/3), so
   x dy|_D=-(4/3)dv/(v-4/3): residue -4/3 at v=4/3 and +4/3 at infinity.
   Formula: -f_1/(2f_2)=3/(2*9/8)=4/3. Matches, with e=1 and no extra
   factor; the theorem applies on each component.
3. **Compatibility with the Astra module certificate**: beta=2p dq^dr
   -q dp^dr-r dp^dq satisfies phi_H^* beta=-4c dx^dy, but
   d beta=2 dp^dq^dr!=0, so beta is not exact on A^3 and yields no
   target-polynomial alpha. The two results are consistent; the module
   certificate is not a primitive, as Astra already stated.
4. **Predicate check**: Res_P!=0 iff f_{m-1}!=0, e in {1,2}; at d>=1 this
   is exactly h_{d-1}!=0, and at d=0 it is automatic (f_1=-3).
5. **Two numeric point checks of (1)** (section 1) at v=0 and v=1.

## 8. Exclusions and scope

h=0: m=1, m odd so e=2, ord p_H=e(m-2)=-2, a pole; the finite-target
premise fails and nothing is claimed (the constant-graph theorem is not a
premise). c=0: t^2 f(v)=0 forces f(v)=0, v constant, no curve of the
required kind. f_{m-1}=0: section 5. No other r_H level, pole, degree or
parameter search is selected; no generic JC2 conclusion; no new canonical
OPEN; no charge_basis (no exit price asserted); no literature novelty
claim; no paid child. ROOT owns caps and terminal receipt-FIRST intake.

## Custody

- First action 2026-09-12T11:33:59Z; prepins taken at that time before any
  body read, in /tmp/jc2-lane.KiuakH/inputs; postpins at 11:40:13Z after
  the scientific body was on disk. All six values matched the expected pins:
  - COORDINATION.md
    33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597
  - constant-graph-subalgebra-control-astra-20260912.md
    590609a7a6f52f72e940a01604c5e6f0c1444277c54bfbb9c69e0fa0c55fd679
  - graph-asymptotic-residue-root-20260912.md
    7c67d9665708072c96e996588f7540b3d07caef2b90da8158f637543aa5c440a
- Read scope: exactly these three snapshots, each WHOLE in unclipped
  chunks, COORDINATION first. No inherited CLI reader, no original/corpus/
  source expansion, no linked files, no live peer output, no protected tree.
- Authoring: skeleton without marker, then three bounded apply_patch
  appends (sections 1-3; sections 4-8; custody plus marker). No shell
  redirection, heredoc write, tee, printf, Write or Edit tool touched any
  file. Only this report was created; no box/scratch file, no shared ledger
  edit, no artifact_finalize, no charge_basis line.
- Tools: read-only cat/sed/sha256sum/wc/grep/date only. No interpreter,
  CAS, code, network, AWS, SSH, git, process inspection or extra agent.
- Own WHOLE readback of the draft performed at 11:40Z before this final
  append; quantity (single coefficient obstruction f_{m-1}!=0 on the one
  curve r_H=0), scope (one symbolic family, no JC2 conclusion), controls
  (section 7) and destination basename checked against the task.
- Verdicts A-E CONFIRMED; no remaining GAP; nothing is sealed as a skeleton.
  Sealed before the 11:50Z reserve. No edits after this marker.

<!-- BODY-END -->
