# Cubic-base unit counterexample: Fable FIRST and binding clarifications

Publication by swarmHQ ROOT; the independent Fable review follows verbatim.
Evidence: MANUAL. Review verdict: CONFIRMED on all six charged items.
Frozen reviewed commit: 1f8ae3c9857abfe3908975bc21e8aa702d7f0067.
Producer report: [explicit construction](cubic-base-unit-counterexample-swarmHQ-root-20260917T215500Z.md),
SHA256 7b62f7c13256fac9a045308cd99577bae7dbb68e7a28a7d070c6e8c6469ff33d.

## Custody and scope of this copy

The original completed review is preserved unchanged, SHA256
3e948216dc4f212ca60c32e9b0d0962af0c3191afca325fae8b8072fa67d7d08,
17699 bytes. Its entire content is the exact suffix of this publication body.
The independent supervisor and original child census were terminal before
receipt-first collection at 22:13 UTC September17. Receipt gives start
22:03:24, end22:12:35, exit0/DONE, four charged originals UNCHANGED, clean
completion boundary. Original review, receipt and log were frozen0444;
pre/post hashes agreed. The legacy BODY_SEALED receipt records a completed
body, not an appended canonical seal; independent seal verification found
no Body-bytes declaration, as expected. This separately named copy receives
the canonical publication seal; the original was not repaired or rewritten.

The original header's placeholder “22:1x UTC” is not an exact completion
timestamp. The terminal log reports author completion22:12:07; the receipt's
independent completion boundary is22:12:35. No mathematical claim depends
on choosing one of those clocks. Requested model=fable/effort=max; hosted
identity is harness-reported and not independently attested. Review
agreement and custody checks do not substitute for the displayed proof.

## Binding mathematical clarifications by ROOT

1. The surface's integrality follows from irreducibility of P-h(s) in
   C(s)[x,y] and primitivity over C[s]: the coefficient of the monomial y
   is the nonzero constant -3. Gauss's lemma applies. Monicity in s alone
   is not the argument at this step. The producer's alternative
   localization/x-factor argument also works.
2. On the geometric generic fiber over Kbar=overline(C(t)), choose s0 with
   h(s0)=t. If w=a+x*s0 were scalar, its value at (0,-t/3) would make it 1.
   But w-1=x^2+x^3*y+s0*x has y-degree1 and is nonzero, whereas any
   nonzero polynomial multiple of P-t has y-degree at least3. Thus it
   remains nonconstant. This is the explicit replacement for the producer's
   loose assertion that its rank-three normal form transfers unchanged.
   Alternatively, faithful base extension preserves the nonzero element
   w-1 of the generic coordinate ring.
3. The review's incidental phrase “onto the cubic norm-one surface” is
   TOO STRONG if read as surjective. For the map (x,y)->(T=P,U=a,V=x)
   into U^3-3UV^2+TV^3=1, V=0 forces x=0 and U=1. The target also has
   the lines V=0,U=omega for the other cube roots omega of1, and these
   are missed. The map is regular and dominant (indeed an isomorphism
   over V!=0, with y=(U-1-V^2)/V^3), NOT surjective. Neither surjectivity
   nor any broader norm-surface theorem is promoted or used.
4. None of the review's optional third integrality route, conceptual
   norm-surface commentary, or source-priority suggestions is a separate
   theorem promotion. The claimed characteristic-zero result is precisely
   the explicit nonsingular/all-fiber-irreducible polynomial with its
   non-base cubic-cover unit and its no-rational-mate certificate.

ROOT independently reconstructed the six claims, including both corrected
proof justifications and the scope restriction. The accepted globalization
and horizontal-puncture reductions remain intact. This refutes auxiliary
unit vanishing without additional Keller assumptions, not JC2. No novelty
claim, Briancon identification, new family, new exit price or new OPEN.

## COLLISIONS

Actual command from the research checkout:

    python3 ops/open_collision.py xmodel/.cubic-base-unit-first-swarmHQ-fable-20260917T221500Z.md.partial-37462202eaf0b3c515e6cc49376fc0e5 --root .

Terminal exit0, actual output:

    ## COLLISIONS

    status: EMPTY

    - NONE — the report contains no explicitly raised `OPEN[...]` entries.

This checks raised tags, not novelty. The original review's own truthful
“not run” statement is preserved below. The entire original 17699-byte
report was independently compared with this body's suffix by tail/cmp,
exit0. This publication's authoring is complete; the original completion
marker below is the body's unique final marker.

## Verbatim terminal Fable review

# Hostile FIRST review: explicit cubic-base unit counterexample (CUBIC-BASE-UNIT-COUNTEREXAMPLE-1)

Reviewer: independent Fable reviewer, swarmHQ (requested model=fable, effort=max).
Identity limit: the hosted identity is not independently exposed; the harness
reports model id `claude-fable-5-1`, which this reviewer cannot verify from inside
the session. Different-model status relative to the producer (Astra ROOT) and the
same-model co-checker (Astra/Maxwell) rests on the launcher's model request.
Role: hostile reviewer only. No delegation, no coordinator, no promotion authority.
Evidence: MANUAL reconstruction only (no CAS, numerics, enumeration, network).
Frozen reviewed commit: 1f8ae3c9857abfe3908975bc21e8aa702d7f0067 (git HEAD at
start and at finish, submodule recursion disabled).
Charged producer: xmodel/cubic-base-unit-counterexample-swarmHQ-root-20260917T215500Z.md
(sha256 7b62f7c13256fac9a045308cd99577bae7dbb68e7a28a7d070c6e8c6469ff33d).
Acknowledgment: /home/ubuntu/swarmHQ/runtime/cubic-base-unit-review-20260917/FABLE-STARTUP.md (chmod 444).
Startup 2026-09-17T22:03:33Z; writing finished 2026-09-17T22:1x UTC (see console log).

## Overall verdict

CONFIRMED on all six charged items. The proof is complete as written. Two
sentences in the producer are imprecise as justifications (items 3 and 4 below)
but each has a one-line correct replacement using only material already in the
producer; neither affects any stated conclusion. The result is exactly what the
producer says: a nonsingular P with every closed fibre irreducible and reduced,
geometrically integral generic fibre, and a global non-base unit on
X_h={P=h(s)} with h=s^3-3s, together with a proof that this P has no rational
constant-Jacobian mate. It refutes the unconditional auxiliary assertion
(nonsingularity + all-fibre irreducibility alone force base/scalar units on the
polynomial-cover surfaces). It does not touch JC2, and it contradicts no
promoted claim.

| # | Item | Verdict |
|---|------|---------|
| 1 | a^3-3ax^2+Px^3=1, inverse of w=a+xs, determinant/resultant norm | CONFIRMED |
| 2 | punctured-plane isomorphism, Jacobian -1, no critical point incl. x=0 | CONFIRMED |
| 3 | every closed P-c irreducible and reduced incl. c=+/-2; geometric generic integrality; X_h smooth integral | CONFIRMED (one wording note) |
| 4 | w non-base; nonconstant on the geometric generic fibre; section argument vs denominators | CONFIRMED (one wording note) |
| 5 | no rational constant-Jacobian mate | CONFIRMED |
| 6 | consequence/scope: auxiliary assertion only, not JC2; earlier reports consistent; no novelty | CONFIRMED |

## Item 1: exact identity, inverse, norm — CONFIRMED

Reconstruction, independent of the producer's expansion. Put u=x^2 k, so a=1+u.

    a^3-3ax^2 = 1+3u+3u^2+u^3-3x^2-3x^2 u
              = 1+3x^2(k-1)+3x^4 k(k-1)+x^6 k^3.

With k-1=xy this is 1+3x^3y+3x^5ky+x^6k^3, and

    Px^3 = -3x^3y-3x^5ky-x^6k^3,

so a^3-3ax^2+Px^3=1 as polynomials. Identity (1) holds.

Inverse. a^3+(xs)^3=(a+xs)(a^2-axs+x^2s^2) (sum of cubes), and
(a+xs)(-3x^2)=-3ax^2-3x^3s, so

    wb = a^3-3ax^2+x^3(s^3-3s),

which is a^3-3ax^2+x^3P=1 in T=C[x,y,s]/(s^3-3s-P). T is free of rank 3 over
C[x,y] on (1,s,s^2) because the relation is monic in s. So w is a unit of T.

Independent cross-check in the chart of item 2: w=x(v+s)=(v+s)/z and
b=x^2(v^2-vs+s^2-3)=(v^2-vs+s^2-3)/z^2, while on X_h localized at x the
equation reads z^3=h(v)+h(s)=(v+s)(v^2-vs+s^2-3). Hence wb=z^3/z^3=1. This
is the conceptual source of the unit and agrees with the algebraic identity.

Norm. Multiplication by w on the ordered basis (1,s,s^2) has columns
(a,x,0), (0,a,x), (xP,3x,a) (using s^3=3s+P). Its determinant is
a(a^2-3x^2)+xP·x^2 = a^3-3ax^2+x^3P = 1. With the monic cubic first,
Res_s(f,g)=prod_i g(alpha_i)=prod_i(x·alpha_i+a)=-x^3 f(-a/x)=a^3-3ax^2+Px^3=1.
The opposite argument order gives (-1)^{3·1}=-1; the producer fixed the
convention explicitly, so no sign ambiguity remains. Norm 1 is also forced
(a unit's norm is a unit of C[x,y]); the point is that it is attained by a
non-base element. No CAS is needed; every step above is a few lines.

## Item 2: punctured-plane coordinates, Jacobian, nonsingularity — CONFIRMED

Map declared (FALLACY-v2 variable/ring-map rule): psi: C[x,x^-1,y] -> C[z,z^-1,v],
x -> 1/z, y -> z^2v-z-z^3; phi: z -> 1/x, v -> 1/x+x+x^2y (= a/x since
a/x = 1/x + xk = 1/x + x + x^2y). Both are C-algebra maps (images of x and z
are units). psi(phi(z)) = z; psi(phi(v)) = z+1/z+(1/z^2)(z^2v-z-z^3) = v;
phi(psi(x)) = x; phi(psi(y)) = (1/x^2)(1/x+x+x^2y)-1/x-1/x^3 = y. So it is an
isomorphism. Jacobian: z_x=-1/x^2, z_y=0, v_y=x^2, so det d(z,v)/d(x,y) =
(-1/x^2)(x^2)-0 = -1, a nonzero constant. Dividing (1) by x^3 with v=a/x,
z=1/x gives v^3-3v+P=z^3, i.e. P=z^3-h(v). (2) holds.

Critical points are coordinate-free. On x!=0 the chart is an isomorphism onto
z!=0, where dP = 3z^2 dz + (3-3v^2) dv and 3z^2 != 0. On x=0: P(0,y)=-3y
directly, and P_y = -3-3x^2(xy+k)-3x^4k^2 evaluates to -3 at x=0. No critical
point on the whole plane. CONFIRMED.

## Item 3: fibres, localization, generic integrality, X_h — CONFIRMED

Non-cube. For any field F of characteristic 0 (in fact char != 3) and any
c in F: a cube root g in F(v) of v^3-3v+c is integral over F[v], hence in
F[v] (integrally closed), of degree 1, g=alpha v+beta with alpha^3=1; the v^2
coefficient 3alpha^2 beta=0 forces beta=0, and then the v coefficient is 0,
not -3. The contradiction does not even involve c. So v^3-3v+c is never a cube.

Irreducibility chain. z^3-g is a cubic over F(v) without a root, hence
irreducible in F(v)[z]; monic in z, so by Gauss irreducible in F[v,z]; z does
not divide it (z-constant term -g != 0), so it stays prime in F[v,z,z^-1];
via psi, P-c is prime in F[x,x^-1,y]. In the UFD F[x,y] write
P-c = prod p_i^{e_i}. Factors not associate to x stay prime after inverting x,
so primality of the image forces exactly one non-x factor with exponent 1;
and x does not divide P-c because (P-c)(0,y)=-3y-c != 0. Hence P-c is
irreducible AND reduced in F[x,y] for every c in F. No component or
multiplicity is lost in the localization: the only elements that become units
are scalar multiples of powers of x, and x is not a factor.

c=+/-2. v^3-3v+2=(v-1)^2(v+2) and v^3-3v-2=(v+1)^2(v-2); the affine cubic
z^3=(v-1)^2(v+2) is singular at (z,v)=(0,1) (resp. (0,-1)). These points have
z=0, i.e. lie outside the image of the plane (x=1/z). The non-cube argument is
uniform in c, so the fibres P-2 and P+2 are irreducible and reduced; there is
no conflict with nonsingularity of P on the plane. The producer's treatment is
correct.

Geometric generic fibre. Apply the chain with F = algebraic closure of C(t),
c=t: P-t irreducible in F[x,y], so the geometric generic fibre is integral.
X_h generic fibre: F=C(s), c=h(s): P-h(s) irreducible in C(s)[x,y].

X_h integral (wording note). The producer says "since its equation is monic
in s, or equivalently by its localization and the same x-factor test". The
step from irreducible in C(s)[x,y] to irreducible in C[s][x,y]=C[x,y,s] needs
P-h(s) to be primitive over C[s]; that follows from the coefficient -3 of y
(not from monicity in s, which concerns Gauss over C[x,y] and would need
irreducibility over C(x,y) instead). The producer's alternative route is
correct as stated: in C[z,z^-1,v,s] the equation is z^3=h(v)+h(s); with
F=C(s), c=h(s), z^3-(h(v)+h(s)) is irreducible in C(s)(v)[z], then in
C(s)[v,z] (monic in z), then in C[s,v,z] (primitive over C[s], leading
coefficient 1), then prime after inverting z; pulling back, all factors of
s^3-3s-P in C[x,y,s] but one are powers of x, and x does not divide it
because its x=0 value is s^3-3s+3y != 0. So T is a domain. (A third route:
monic in s plus no critical points, since a root r in C[x,y] of r^3-3r=P would
give P critical points on r=1.) Not a gap: the result stands.

Smoothness of X_h: the gradient of h(s)-P is (-P_x,-P_y,h'(s)) and
(P_x,P_y) != 0 everywhere by item 2. X_h is smooth and integral. CONFIRMED.

## Item 4: non-base unit; geometric generic fibre; denominators — CONFIRMED

Section. sigma: s -> (0,-h(s)/3,s). P(0,y)=-3y, so P(sigma(s))=h(s); the pullback
sigma^*: T -> C[s], (x,y,s) -> (0,-h(s)/3,s) is a well-defined C-algebra map,
and sigma^*(w)=a(0,.)+0=1.

Denominators. Suppose w=p(s)/q(s) in Frac(T) with p,q in C[s], q!=0. Then
q(s)w=p(s) in T (T is a domain, so T sits in its fraction field). Applying
sigma^* gives q(s)·1=p(s), so w=1 in Frac(T), hence in T. But
w-1 = x^2k + x·s + 0·s^2 in the free basis (1,s,s^2) over C[x,y], with
s-coordinate x != 0, so w-1 != 0 in T. Contradiction: w is not in C(s). The
section is polynomial in s, so no denominator of the section arises, and the
clearing step above handles rational denominators of w. Equivalent cleaner
form: in T_eta = T tensor_{C[s]} C(s) the point sigma_eta is a C(s)-algebra map
T_eta -> C(s) fixing C(s), so a base element w would satisfy w=sigma_eta(w)=1;
T -> T_eta is injective (domain, localization at C[s]-{0}). CONFIRMED.

Geometric generic fibre (wording note). Let K=C(t), Kbar its algebraic
closure, and choose s0 in Kbar with h(s0)=t (t=h(s) is finite of degree 3 over
K, so Kbar is also the algebraic closure of C(s)). Then
T tensor_{C[s]} Kbar = Kbar[x,y]/(P-t), and w=a+x·s0 is a unit there with
inverse a^2-a x s0+x^2 s0^2-3x^2, because wb = 1 + x^3(t-P). It is nonconstant:
if w = lambda in Kbar, evaluating at the Kbar-point (0,-t/3) of the fibre
gives lambda=1; but w-1 = x^2+x^3y+s0·x has y-degree 1 with nonzero y-coefficient
x^3, while every nonzero multiple of P-t has y-degree >= 3 (leading y-term
-x^6y^3). So w-1 != 0 in Kbar[x,y]/(P-t). The producer's phrase "the same
section and normal-form argument work after extending the generic base" is
loose, since once s specializes to s0 the rank-three normal form over C[x,y]
is no longer the relevant structure; the y-degree argument (or the free
structure of the z-localized chart) is the correct one-line replacement. The
conclusion — a nonconstant unit on the geometric generic fibre of P — holds.
CONFIRMED.

## Item 5: no rational constant-Jacobian mate — CONFIRMED

Model. C(x,y)=C(z,v) and, with t:=P transcendental, C(x,y) is the function
field over K=C(t) of the affine curve z^3-v^3+3v=t, whose projective closure
is C_t: Z^3=V^3-3VW^2+tW^3. Smoothness over Kbar: affine chart W=1 has
F_z=3z^2, F_v=3-3v^2; a singular point needs z=0, v=+/-1, hence t=+/-2, impossible
since t is transcendental over C and +/-2 in C. On W=0: Z^3=V^3 with V,Z != 0
and G_Z=3Z^2 != 0. C_t is a smooth plane cubic, hence geometrically integral,
and it is the smooth projective model of the generic fibre (birational via
item 2, and a smooth projective curve is unique in its birational class).

eta = dv/(3z^2) = dv/F_z. On the smooth affine chart dv/F_z = -dz/F_v is the
standard regular nowhere-vanishing differential; at z=0 it reads
dz/(3v^2-3) with 3v^2-3 != 0 there (v=+/-1 at z=0 would force t=+/-2). At
infinity, u=1/v, Z0=z/v: Z0^3=1-3u^2+tu^3, dv=-du/u^2, z^2=Z0^2/u^2, so
eta=-du/(3Z0^2)=-du/G_{Z0}; at u=0, Z0^3=1, G_{Z0}=3Z0^2 != 0, so u is a local
parameter and eta is regular and nonzero. All points of C_t(Kbar) are covered
by the two charts (points with W=0 have V != 0). eta is holomorphic and
nowhere zero (as expected for genus 1).

Bracket. Chain rule: J_xy(P,Q)=J_zv(P,Q)·det d(z,v)/d(x,y) = -J_zv(P,Q), so
J_zv(P,Q)=-c. Sign is immaterial (c != 0 iff -c != 0). Relative differential:
Omega_{C(z,v)/K} = (C(z,v)dz + C(z,v)dv)/(dP), dP=3z^2dz+(3-3v^2)dv, so
dz = (3v^2-3)dv/(3z^2) and
d_K Q = [Q_z(3v^2-3)+3z^2Q_v]/(3z^2) dv = [P_zQ_v-P_vQ_z]/(3z^2) dv = -c·eta.
(4) holds.

Poles. Over Kbar, at a point with uniformizer pi, Q=pi^{-m}u (m>=1, u a local
unit) has dQ = (-m u pi^{-m-1} + u' pi^{-m}) dpi of order exactly -m-1 because
m != 0 in characteristic 0 and dpi generates Omega^1 at a smooth point. Since
-c·eta is holomorphic, Q has no pole at any Kbar-point, so Q is in
H^0(C_t x Kbar, O) = Kbar (geometrically integral projective curve). Then
dQ = 0, so c·eta = 0, so c = 0. Contradiction. No Q in C(x,y), a fortiori no
polynomial Q, has J(P,Q) a nonzero constant (either order, since J(Q,P)=-J(P,Q)).
Constants after field extension are handled correctly: the argument runs over
Kbar and uses only c in C. CONFIRMED.

## Item 6: exact consequence and scope — CONFIRMED

What is refuted. The unconditional assertion "P nonsingular with every closed
fibre irreducible implies every global unit of X_h={P=h(s)} is a base
(scalar) unit, equivalently geometric-generic unit vanishing" is false: this P
satisfies the hypotheses (items 2, 3) and X_h with h=s^3-3s carries the
non-base global unit w (items 1, 4). The producer correctly limits the
refutation to this auxiliary assertion.

Not JC2. The Keller hypothesis is absent and cannot hold: item 5 shows P is
not a component of any Keller pair, nor even of a rational pair with nonzero
constant Jacobian. Consistently, the generic fibre has genus 1, so P is not a
coordinate, matching the producer's P=x control (T=C[y,s], units C^*).

Consistency with earlier reports (read-only check, hashes verified against the
producer's pins: horizontal a9a9c381..., globalization 87dc47e2..., D4
65906bba...). The horizontal-unit polynomial-base reduction states its
conclusion as a REDUCTION: "geometric-generic unit vanishing follows if global
units are constant on X_h ... not a solution of them" (its lines 36-39), and
raises no vanishing assertion (line 218). The globalization report says "It
does not prove that O(X)^* consists of base units" (line 131) and its
quadratic interface "supplies the whole-plane map; it does not exclude that
map" (lines 108-109). The frontier (APPROACHES.md lines 89-96, 111-123) records
both as PROMOTED with "Excluding these global units remains open" and "The
remaining test is unit vanishing on these selected polynomial-cover surfaces".
The present example is the cubic analogue of that quadratic interface: (x,y)
-> (P,a,x) is a regular map from the plane onto the cubic norm-one surface
U^3-3UV^2+TV^3=1 (identity (1)), exactly the kind of map the globalization
report declined to exclude. Nothing promoted is contradicted; the reduction
and the globalization theorem are instantiated, not refuted, by this P (deg
h=3 >= 2 as the horizontal report requires).

No novelty or identification. The producer claims no novelty, no
identification with a named published example, no Briançon identity, and no
family search; none is asserted here either. No external source was consulted
and the stopped 2015 factorially-closed-rings body is not used.

## Attacks attempted that did not break the proof

- Resultant sign convention (order of arguments): fixed explicitly; the
  determinant norm is 1 independently.
- A hidden x-factor or multiplicity in some fibre: excluded by (P-c)(0,y)=-3y-c.
- c=+/-2 singular cubics: singular points have z=0, off the plane; fibres remain
  irreducible and reduced by the uniform non-cube argument.
- The section argument with a rational w in C(s): cleared denominators inside T.
- Base change of the "normal form": replaced by a y-degree argument; holds.
- Points at infinity and the z=0 points of C_t for eta: all regular, nonzero.
- Constants after base change: Q in Kbar forces c=0.
- Whether the example is secretly a coordinate: no (genus 1, no mate).

## FALLACY-v2 check

No exit claim, so no charge_basis line is required and none is declared.
Ring maps are declared with inverses and image checks (item 2). No pole
identity is used without its hypotheses (item 5 checks smoothness and every
chart). No cap or analogy fills any gap. Prime marks in this report are
labels only except h'(s) and u' in item 5, which are ordinary derivatives.

## Read scope, pins, COLLISIONS, constraints

Read whole: the charged producer, FALLACY-v2.md, COORDINATION.md. APPROACHES.md:
read by keyword grep plus lines 86-124 (context only). Earlier reports (repo
files at the frozen commit, read-only): horizontal-unit-polynomial-base
(grep plus lines 28-45 and 168-192), geometric-unit-globalization (grep plus
lines 87-112), D4 counterexample (hash only). No other files were opened.
jc2-lean and jc2-web were not entered or enumerated.

Pre-pins (22:03 UTC) and post-pins (22:09 UTC) on /tmp/jc2-lane.1sAS5o/inputs,
all MATCH the charged pins before and after review:

- cubic-base-unit-counterexample-swarmHQ-root-20260917T215500Z.md 7b62f7c13256fac9a045308cd99577bae7dbb68e7a28a7d070c6e8c6469ff33d
- FALLACY-v2.md e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5
- COORDINATION.md 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e
- APPROACHES.md 905313fb08c6e94410b8c4a9a4537bf69ac3ff63284a14c9a34761263fc1505f

The repo copy of the producer at the frozen commit has the same hash as the
input copy. Git HEAD was 1f8ae3c9857abfe3908975bc21e8aa702d7f0067 at start and
at finish.

## OPENS RAISED

None. No successor proposal, no new OPEN, no promotion action.

## COLLISIONS

Not run. The collision checker (python3 ops/open_collision.py) was not executed
because only read-only shell/hash checks and apply_patch on the two owned
outputs are permitted in this lane. This report raises no `OPEN[...]` entries,
so the expected checker outcome would be EMPTY, but that is an expectation,
not an observed output.

Constraints honored: no CAS or scientific execution, no numerics, enumeration,
network, AWS, provider calls, Git mutation, input/shared edits, protected
access, artifact_finalize or seal.py. Only the acknowledgment file and this
report were written. Legacy parent owns custody; this report carries no seal.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `22312`.
- Body SHA-256:
  `97372ca70d18f6bf58d783b14c4be1e3c2e6309cc1b09b80502fdb3f728a6077`.
- Frozen basis: `1f8ae3c9857abfe3908975bc21e8aa702d7f0067`.
