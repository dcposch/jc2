# D125: conditional finite-boundary completion, not guarded emptiness

2026-09-08. **CONDITIONAL theorem-interface PASS, contingent on the frozen
PROVISIONAL high-alpha theorem.** Together with accepted14p/q/s/t/v and15e,
it excludes every finite field-coefficient source arc with k nonzero
generically and k=0 specially. For the k-saturated closure this implies

    (I:k^infinity)+(k)=S,

NOT I:k^infinity=S. The stronger scheme statement is that its k-nonzero
open is the whole saturated scheme, with all nilpotents retained. No source
point, properness, emptiness, global degeneration or JC2 conclusion follows.
This composition itself has not been independently reviewed or promoted.

## 1. One literal ring and one exhaustive case cover

Let S be the finite polynomial ring over Q in the free coefficients and k
of the exact14c ODD, lambda2=0, lambda3=1 moving-face source. Let I contain
EVERY unguarded Jacobian, negative-lift and prescribed-face equation. There
is NO inverse variable z and no zk-1 in S or I. Work first without the
optional whole-B shear slice; the same argument permits that slice.
This is the restricted sufficient source, not an exhaustive JC2 family.
No compressed81 graph map is a premise of this composition.

Put J=I:k^infinity, X=Spec(S/J), U=D_X(k). An arc of S/I to any
characteristic-zero K[[s]] with nonzero k(s) automatically factors through
S/J: if k^n f belongs to I, cancellation in the domain gives f=0.
The converse is immediate. Adding the three accepted14g saturated low
equations before saturation does not change J, since each already has a
power of k times it in I. These observations do not assert that the raw
unguarded low ideal equals its saturation over nilpotent rings.

Consider such an arc with ord_s(k)=m>0. Its field-valued center is classified
by14f over its coefficient field, without a root extension:

    A0=R_t0^3+alpha0 R_t0,
    B0=R_t0^5+beta0 R_t0^3+gamma0 R_t0,
    h0=t0+3, delta0=gamma0-beta0*alpha0+5alpha0^2/9.

The following branches exhaust every center and every remaining order:

| Condition | Exclusion and status |
|---|---|
| h0!=0 |14p, accepted; low rows first force alpha0=gamma0=0 |
| h0=0, delta0!=0 |14q, accepted, any alpha0 and any leading unit of k |
| h0=0, delta0=0, alpha0!=0 |14s tuned theorem, accepted |
| h0=0, delta0=0, alpha0=0, ord(alpha(s))<j |14v first contact plus15e, accepted |
| Same pure center, ord(alpha(s))>=j, including alpha(s)=0 |Frozen high-alpha theorem, PROVISIONAL; the sole new conditional premise |

In the last two rows gamma0=0 automatically; beta0 remains FREE. Use the
same actual14v A-reference ONCE:

    t(s)=[p13]A/3, h=t+3,
    alpha(s)=([p3]A+h^3)/t(s),
    R_s=R_t(s), F=A-R_s^3-alpha(s)R_s.

t(0)=-3 is a unit, alpha(0)=0, and14v supplies a finite 1<=j=ord(F)<m,
F_j=RC, and scalar references beta(s),gamma(s) with ord(G)>=2j and
ord(delta)>=j+1. The definitions of alpha and j depend only on this A,
not on a later choice of beta/gamma kernels. They are exactly the setup
shared by15e and the high-alpha theorem. A finite order is either <j or
>=j, and infinity belongs to the latter; there is no uncovered alpha=0
or F=0 case. This does not classify arbitrary nilpotent jets.

## 2. Field, parameter and beta bookkeeping

14p is stated with literal k=s^m. For k=s^m u(s), u(0)!=0, extend K finitely
to adjoin a chosen mth root v0 of u(0). Solve v(s)^m=u(s) recursively, with
unit scalar pivot m*v0^(m-1), then set tau=s*v(s). Its linear coefficient
is nonzero, so it has a formal compositional inverse. All rational source
identities, finite (g,p)-supports, fixed faces and the center are preserved,
and k=tau^m. This is a field extension and parameter isomorphism, NOT an
asserted same-field normalization or a change of receiver coordinates.
14q/s/15e and high-alpha admit arbitrary leading units directly. Their
internal algebraic-closure/Puiseux extensions are legitimate contradiction
devices; characteristic-zero field injections preserve the nonzero entries
in this case split. They impose no new localization on the source.

Under an entire target shear B->B-lambda A,
beta0->beta0-lambda and gamma0->gamma0-lambda*alpha0, so delta0 is unchanged.
Odd parity, ordinary lifts and all relevant bounds persist: A has degree15
versus B25 and maximal weight3 versus B5. Thus neither fixed B total nor
inner faces is changed. The origin remains zero, and the bracket is unchanged.
This is why beta need not be normalized to any particular value. If the
optional [p15]B=0 slice is used, the entire shear is available because
[p15]A=1. At t0=-3 that slice makes beta0=243, not zero; the case cover
already allows it. No argument silently drops beta without its gamma change.

## 3. From an existing finite boundary point to the conditional scheme result

Accepted14t supplies exactly the required direction, not its converse.
J is the kernel of S->(S/I)[1/k], so U is schematically dense in X.
If q is a point of X with k=0, the finite-type open immersion U->X and
the Noetherian valuative image-closure lemma give a DVR A mapping to X,
closed point over q, generic point in U. Thus all source coordinates lie
in A and k is nonzero in its maximal ideal. Completing A is injective and
gives a characteristic-zero complete DVR L[[s]]. The coefficient field
contains Q, which is enough for these rational equations; it need not
provide a prescribed section of a larger original field. Every nonzero
condition at q persists in the residue-field extension. The arc is now
covered by Sections1-2 and is forbidden, CONDITIONALLY on high-alpha.

The whole used statements and proofs were reread in the already pinned
primary snapshots: [Stacks Lemma32.15.1, tag0CM2, in section0CM1](https://stacks.math.columbia.edu/tag/0CM2)
and [Lemma10.160.10, tag0C0S](https://stacks.math.columbia.edu/tag/0C0S).
Their earlier dependencies remain imported at14t trust; no new geometric
theorem or proof of degeneration existence is introduced here.

Hence Spec(S/(J+(k))) is empty. If J+(k) were proper, a prime/maximal ideal
above it and then its residue field would supply a point, a contradiction.
Therefore J+(k)=S EXACTLY, not merely a displayed radical-membership bound.
Equivalently some b in S satisfies kb=1 modulo J. We have not constructed b
or bounded its degree. Consequently

    S/J  ~=  (S/J)[1/k]  ~=  (S/I)[1/k]
         ~=  S[z]/(I,zk-1).                       (C)

These are Q-algebra/scheme isomorphisms, not just field-point bijections.
Maps to DVRs kill nilpotents, but absence of every prime still forces the
unit identity, which holds on the entire possibly nonreduced ring.
Once that Q-identity holds, it survives every Q-algebra base change,
including nonreduced coefficient algebras. No unproved coefficient-field
descent or reducedness assertion is needed.

For completeness, the unguarded scheme has an existential open-and-closed
vertical split. Noetherian stabilization gives N with J=I:k^N and k^N J
contained in I. Since k is a unit modulo J, J+(k^N)=S. Then

    I=J intersect (I+(k^N)),
    S/I ~= S/J times S/(I+(k^N)).                 (D)

Indeed, if f=i+k^N a belongs to J, saturation gives a in J, so k^N a is
in I. This proves the intersection identity; comaximality gives the product
by the elementary Chinese remainder map. In the second factor k is nilpotent;
in the first it is invertible. N and the projectors are NOT computed.
Existing raw k=0 boundary points can all belong to that vertical factor.
Thus even this stronger scheme formulation says nothing about whether the
first factor is zero or nonzero.

## 4. Exact negative controls and stop

Take I_toy=(kw-1) in Q[k,w]. It is already k-saturated, has the point
(k,w)=(2,1/2), and k is a unit with inverse w. Yet I_toy+(k)=S_toy,
so it has no finite k->0 arc with generic k nonzero. The certificate is
1=kw-(kw-1). This REFUTES the inference J+(k)=S => J=S.
The nonreduced example Q[k,w,epsilon]/(kw-1,epsilon^2) has the same unit k
and a genuinely nonzero nilpotent epsilon. The unit conclusion does not
imply reducedness. For a vertical-split toy, I=k^2(kw-1) has saturation
(kw-1), and 1=k^2w^2-(kw-1)(kw+1) verifies comaximality with (k^2).
None is a Keller pair or a point of the actual source.

Twelve capped normal/-O tiny controls pass with identical rational-string
witness bytes and zero Assert nodes. They check the actual toy point/unit
and CRT identities, a changed nilpotent multiplication law, the full
beta/gamma shear, and a scalar unit-root reparameterization. Changed
hyperbola/CRT signs, omitted gamma transport and changed root coefficients
fail the same verifiers. No source/R powers or CAS were used. Witness SHA256
`57ede9d764ded48e047aaf5f1a7b6431279f0ab1b790dea46414469e1ed3bca2`.

Whole14p/q/s/t and its gate,15e producer/gate, and the frozen high-alpha
producer were read; the high-alpha gate remains LIVE and was NOT read.
Current pins and the precise read scope are in custody. This is one bounded
conditional composition, not a new source theorem, authority to add rows,
global existence assertion, solver result or descendant. The strongest
conditional conclusion is (C)/(D), not guarded emptiness. Transaction
verified; all writers idle at handoff. **STOP/IDLE.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9230`.
- Body SHA-256:
  `b17dab465b36e1e98666f960dbc4c952f0ce83ce470899b4ec1437a2fc70919f`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
