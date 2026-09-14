# Furter transition typing: the printed residue-A row1/merge route

2026-09-07. **NO-GAIN at the first substantive edge.** The named route's
coordinate substitution is affine over a Laurent coefficient field, but its
nontrivial pattern transport is leading-term extraction, NOT composition by
a univariate polynomial. The affine shadow, when normalized to fix0 with
derivative1, is exactly the identity. No contact bound, bounded delay, source
exclusion or global no-go follows.

## One route, with its actual qualification

Choose the distinguished residue-A route printed in
[SHEET6-2POLE §6a](../ladder/SHEET6-2POLE.md:326) and corrected in
[SHEET6-L1 §7](../ladder/SHEET6-L1.md:356): two row1 poles
P_± with (D,deg p,nu,M,kappa-bar)=(2,2,2,1,5), merge
G_m=(6,12,3,2,5), followed by the named suffix (42,126,7,3,5) and (0,y).
The correction allows free merge depth; the older diagram's 'FIRST step'
is not a new hypothesis here. Select the explicitly printed minimal genome
m_Gm=1 and its G_m-to-P_+ refined transport; P_- obeys the identical formula.

The complete local formula is in the terminal
[simultaneous substitution report §§3–4](sigray-residue-a-subst-transport-gpt56-20260828.md:240).
That report labels its pair a conditional formal leading seed, not a full
Keller germ, and does not cover m_Gm=2. This task claims neither actual
realization nor complete source-to-route coverage. It tests the printed edge
itself and stops there; later suffix maps are not invented.

Work in a finite characteristic-zero extension L containing the displayed
constants. Put r²=3, a_±=(3±r)/2, c_±³=a_±, and

    P(z)=(z³-a_+)(z³-a_-)=z⁶-3z³+3/2,
    d_i=P'(c_i) != 0,   W_i=-A(c_i)/d_i².

Here A(z) is the single correction polynomial explicitly constructed in
§4.1 of the source report, not a newly selected coefficient or gauge. Its
specific formula is unnecessary for the typing obstruction.

## Primary transition and exact ring map

Sigray's primary Notation3.9 and Statements3.7–3.9, pp.13–15, define the
transverse coordinate eta_F and the finite Laurent expansion of h^F.
The proof of Statement3.9 explicitly gives

    eta_G = x^(1/kappa) (eta_F-c).

Thus eta_F=c+x^(-1/kappa) eta_G. This inverse follows directly from the
displayed coordinate definition; the later printed x^(-kappa) substitution
is the known exponent typo, not a different transition. The auxiliary-h
suitable-refinement hypothesis remains load-bearing for its multiplicity
conclusions; see [SIGRAY-AUDIT, St3.9](../ladder/SIGRAY-AUDIT.md:40).

For the chosen refined edge, the retained source's exact formula is

    Z=x^(1/42),   z=c_i+Z^(-5) eta.                 (1)

These are TWO independent chart variables Z and eta; z is transverse, not
the infinity uniformizer. With t=Z^(-1), (1) defines the ring isomorphism

    tau_i : L[t,t^-1,z] -> L[t,t^-1,eta],
    t |-> t,  z |-> c_i+t^5 eta,
    inverse: eta |-> t^-5(z-c_i).                  (2)

Over L[t] it is not an isomorphism across t=0: its inverse has a pole and
the specialized map sends z to the constant c_i. This is the first place
where one cannot turn the physical transition into a nonconstant polynomial
map of a single zero-centered special-fiber parameter.

## Why the useful pattern transport is not composition

The source prints, in the same common parameter,

    f_* = t^-12 P(z)^2 + t^-2 A(z),
    g_* = t^-18 P(z)^3 + (3/2)t^-8 P(z)A(z) + t² C(z).

Because c_i is a simple root, P(c_i+t^5 eta)=d_i t^5 eta+O(t^10).
Consequently the exact parent patterns are

    F_i(eta) = [t^0](t² tau_i(f_*))
             = d_i² eta²+A(c_i),
    G_i(eta) = [t^0](t³ tau_i(g_*))
             = d_i³ eta³+(3/2)d_i A(c_i) eta.       (3)

The scaled expressions in (3) are regular at t=0, so these coefficient
extractions are literal. They reproduce the source's equations(POLE),
lines282–283. In particular, the parent F_i receives contributions from TWO
different merge Laurent layers, not just the merge leading pattern P².

This supplies a decisive elementary discriminator. The merge f-pattern has
degree12 in z; F_i has degree2 in eta. For any nonconstant polynomial
psi in L[eta], even allowing nonzero scalar multiples and additive constants,

    deg(P(psi)^2)=12 deg(psi) >= 12,

so it cannot equal F_i. A constant psi cannot equal F_i either. The g-pattern
similarly drops18 to3. The existing transition therefore cannot be used as
a compositional factor transporting these leading polynomials. It is the
bivariate substitution PLUS layer-dependent leading-term operation in(3).
No assumption about a later route or an unproved polynomial mate is needed
for this first-edge failure.

## Do not overstate the Laurent objection

Treating t as a coefficient in L(t), the coordinate map
phi_i(eta)=c_i+t^5 eta IS an honest affine polynomial. Its inverse is also
affine over L(t). Laurent coefficients alone do not violate a theorem about
polynomials over a characteristic-zero field. However, every finite composite
of these coordinate maps and affine re-centerings is affine; if F(0)=0 and
F'(0)=1, then F is exactly the identity. It fails the accepted Furter core's
essential F!=z hypothesis and supplies no nontrivial contact bound. For
example phi_i^-1 composed with phi_i is identically eta.

Nor are the two incoming roots a loop: phi_j^-1 composed with phi_i is
eta+(c_i-c_j)t^-5, not a zero-fixing germ when i!=j. Re-centering it again
only gives the identity. Comparing the unrefined denominators21 and42 would
instead introduce s=t²: its forward derivative at0 is0, while its inverse
needs a square-root base change. This is an optional scalar interpretation,
not a new mandatory ramification obstruction: working on the already printed
common cover removes that extra base-change arrow but does not repair(3).

**First missing arrow:** the nontrivial source/pattern transport in(3) is not
a composition of nonconstant one-variable polynomial self-maps with a
nonidentity, multiplier-one composite. No such additional map is provided
by this named route. This rejects Sol Card2's proposed port for this printed
client only; it neither refutes Furter nor precludes another precisely typed
client. No second route or G2-PSC reconstruction is pursued.

## Evidence and stop

`box/furter-transition-typing-20260907/input-pins.json` pins eight exact inputs
and two derived reading artifacts. The primary PDF SHA256 is
`9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae`;
the full terminal transport report is
`87cfc52baa3e4b06f2c3a841ad6017c062ded45456586cb1854120f35f4304f6`.
`read-scope.md` records complete versus selected reading and the abandoned
exploratory atlas display. No computational test was needed: equations(2)–(3),
the degree obstruction and the affine-identity control are exact desk checks.
No external fetch, implementation, CAS, AWS/SSH, live cross report, new agent,
canonical edit or protected-tree inspection. All writers terminal at handoff.
**STOP / IDLE: one scoped transition-typing discriminator, no new authority.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7066`.
- Body SHA-256:
  `9c509553b10c8012d84bde52792a45ed76d798d9e517d4b642725d6969c5b812`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
