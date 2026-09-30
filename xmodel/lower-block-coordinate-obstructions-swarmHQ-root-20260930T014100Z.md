# Lower-block coefficient fibers do not give the missing plane coordinate

Producer: swarmHQ ROOT/Codex, integrating independent Astra and Opus5.5
calculations; Fable5.1 supplied an overlapping top-coefficient observation.
Requested model identities are attribution, not hosted-identity attestations.
Date: September 30, 2026.
Basis: `07082627defead2f55e05812b9ba81e45e59bbe4`.
Evidence: MANUAL, with elementary complex Euler-characteristic additivity.
Lifecycle: PRODUCER-CHECKED / UNPROMOTED. No accepted-ledger upgrade.
Novelty: UNKNOWN. JC2 remains unresolved.

## Definition and exact claims

Define the coefficients by the literal polynomial used in the
[fixed-high-coefficient report](marked-root-fixed-coefficient-slices-swarmHQ-root-20260915T124800Z.md).
For n>=4, in C[x,y,z3,...,zn], put p=1+xy and

    Phi(T)=(1-y*T)^(n-1)*(p*T-x)
       +(p*T-x)^2*[n*y*(y*T+1/2)+z3*(p*T+x/2)
                         +sum(j=4..n) z_j*T^(j-2)]
       =sum(k=3..n) C_k*T^k+A2*T^2+T-A0.

For arbitrary lambda=(lambda2,...,lambda[n-2]), let

    X_lambda=Spec C[x,y,z3,...,zn]/
                  (A2-lambda2,C3-lambda3,...,C[n-2]-lambda[n-2]),
    r=C[n-1],   q=C[n],   b=A0,   m=n-2.

When n=4, only A2 is fixed. These are LOWER-block fibers, not the
previously classified fibers obtained by fixing ALL high coefficients.

1. For every mu in C, S_mu=X_lambda intersect{r=mu} is not A2.
   Its x*p!=0 stratum is (C*)^2; its x=0 stratum is A1; its p=0
   stratum is empty for mu=0 and is m disjoint A1's otherwise.
2. For every beta in C, no reduced irreducible component of the q=beta
   fiber admits a dominant morphism from A2. In particular that fiber is
   not A2. For every polynomial h in C[T], r+h(q)=h(0) is not A2.
3. In contrast X_lambda intersect{x=0} is A2, and (r,q,b) restricts
   there to (r,q,0), an isomorphism onto that target plane.

In particular, if X_lambda is identified with affine three-space, neither
q nor any r+h(q) is a polynomial coordinate on it. This rules out these
specified final coordinate steps, not arbitrary target coordinates,
plane sections, quotient constructions, or polynomial substitutions.

The conclusions are proved directly from this definition. They require
neither a three-space coordinate-completion theorem, a constant-Jacobian
claim for the ambient map, nor its purported generic mapping degree.
No external manuscript is independently certified here.

## 1. Reconstruction on the torus chart

On p!=0, the coefficients C3,...,Cn determine z3,...,zn by a descending
triangular linear system. For j>=4 a variation dz_j contributes

    dz_j*(p^2*T^j-2*p*x*T^(j-1)+x^2*T^(j-2)),

and dz3 contributes p^3*dz3 to the T^3 coefficient. The diagonal entries
p^2,...,p^2,p^3 are units. This is the old report's reconstruction, without
transferring its conclusions about a differently constrained fiber.

On x*p!=0 set t=x/p, a=1/p. The inverse is x=t/a, y=(1-a)/t;
the (x,y) base here is exactly the torus with coordinates (t,a).
Evaluation of the displayed definition gives

    Phi(t)=0,   Phi'(t)=a^m.

Put P0(T)=T+sum(j=2..n-2)lambda_j*T^j. A point of X_lambda on this
chart therefore satisfies

    P0'(t)+(n-1)*r*t^(n-2)+n*q*t^(n-1)=a^m,       (1)
    b=P0(t)+r*t^(n-1)+q*t^n.                     (2)

Conversely, choose t,a,r,q obeying (1), and b by (2). The fixed high
coefficients reconstruct the z_j regularly. The remaining discrepancy
between its actual Phi and P0+r*T^(n-1)+q*T^n-b is alpha*T^2+beta.
Its value and derivative at nonzero t both vanish, so alpha=beta=0.
Thus this reconstruction has the prescribed low coefficients too.

Fixing r=mu in (1) uniquely solves q, regularly on (C*)^2, and (2)
then determines b. This proves the torus-stratum assertion as an affine
scheme isomorphism, not just a generic parameter count.

For comparison, varying the high coefficients with x,y fixed also gives

    delta A2=-1/2 sum(k=3..n) k*t^(k-2)*delta C_k,
    delta A0=-1/2 sum(k=3..n) (k-2)*t^k*delta C_k.

These identities verify Opus's affine-linear coefficient formulas
uniformly. They extend regularly over x=0 in the p!=0 chart. No
small-n computational extrapolation is being used.

## 2. The two boundary strata

At x=0, p=1, direct coefficient extraction yields

    A2=-(n-2)*y/2,
    C3=z3+[(n-1)(n-2)/2+n]*y^2,
    Ck=zk+(-1)^(k-1)*binom(n-1,k-1)*y^(k-1)  (k>=4),
    A0=0.

Fixing the lower coefficients and r determines y,z3,...,z[n-1] and
leaves zn free. Hence S_mu intersect{x=0}=A1, for every mu and lambda.
Fixing only the lower coefficients leaves the two free coordinates
r,q instead: this proves the positive plane control in claim3.

At p=0, x is invertible, y=-1/x, and the literal definition becomes

    Phi(T)=-x^(-m)*(T+x)^(n-1)+n*T-n*x/2+x^3*z3/2
                              +x^2*sum(j=4..n) z_j*T^(j-2).

Therefore r=-x^(-m), q=0, and b=(n+2)*x/2-x^3*z3/2.
The lower equations solve z4,...,zn with diagonal x^2, leaving x
invertible and z3 free. Thus X_lambda intersect{p=0}=C* times A1.

Imposing r=mu makes this stratum empty for mu=0. Otherwise x^m=-1/mu
has m distinct nonzero complex roots, each leaving one affine line.
These lines and the x=0 line are disjoint and exhaust the complement
of the torus stratum in S_mu.

For mu=0, p has no zero on S_mu and is a unit in its coordinate ring:
modding out by p gives the zero ring. It is nonconstant on the torus
stratum, so S_mu cannot be A2, whose only units are nonzero constants.

For mu!=0, additivity of compactly supported complex Euler characteristic
gives chi_c(S_mu)=0+1+m=n-1, whereas chi_c(A2)=1. This uses the underlying
complex variety; no smoothness, reducedness, or hidden irreducibility
hypothesis for the whole fiber is needed. It proves claim1. It does
NOT exclude dominant maps A2->S_mu merely from that Euler characteristic.

## 3. Top coefficient and arbitrary triangular shears

Write d=p*z_n+(-1)^(n-1)*y^(n-1), so q=p*d. In the ORIGINAL ring,

    1=p*[sum(j=0..n-2)(1-p)^j-x^(n-1)*z_n]+x^(n-1)*d.    (3)

Thus (p) and (d) are comaximal after any of the lower equations too.
The q=0 fiber decomposes into its disjoint closed-and-open p=0 and
d=0 pieces. The first is always C* times A1 by section2. If the
second is nonempty the fiber is disconnected; if empty the whole
fiber is C* times A1. Neither is A2.

In fact fix ANY q=beta and call the fiber T_beta. On x*p!=0 equation(1)
uniquely solves r, so this stratum is a torus. On x=0 it is one A1.
For beta!=0 there is no p=0 stratum and p is a unit everywhere. For
beta=0 the d=0 piece has p invertible, while the p=0 piece is exactly
C* times A1 as above. Every irreducible component of T_beta has
dimension at least2, since it is cut out by n-2 equations in A^n.
The same lower bound holds for the nonempty open-and-closed pieces
and for localization at p. The x=0 boundary line cannot contain an
irreducible component. Hence the p-invertible piece has a unique
irreducible component, with dense torus, on which p is nonconstant.
For beta=0 the other component has nonconstant unit x.

A dominant A2 morphism to any such REDUCED component would inject
its coordinate ring into C[s,t]. Its nonconstant unit must map to a
constant, contradicting injectivity. This proves the stronger claim2
without assuming that the whole fiber is reduced. In particular, a
map from A2 into T_beta cannot have two-dimensional image. This
settles the proposed constant-q plane-restriction test uniformly;
it is not an exclusion of arbitrary restrictions with varying q.

Now fix h in C[T]. The fiber r+h(q)=h(0) misses p=0, since on p=0
one has q=0 but r=-x^(-m)!=0. Hence p is a unit on this entire
affine fiber. To show that it is nonconstant, substitute r=h(0)-h(q)
into (1):

    P0'(t)+(n-1)*(h(0)-h(q))*t^(n-2)+n*q*t^(n-1)-a^m=0.   (4)

If deg(h)>=2, the leading q coefficient is
-(n-1)*h_lead*t^(n-2), nonzero on the torus. For constant h the
q coefficient is n*t^(n-1), again nonzero. For h=h0+h1*q with h1!=0,
it is t^(n-2)*(n*t-(n-1)*h1), nonzero away from one t-value.
For every base point in the resulting dense open of the (t,a) torus,
the nonconstant polynomial (4) has a complex root q. Reconstruction
in section1 produces the source point. Hence p=1/a takes varying
values on the fiber. It is a nonconstant unit, ruling out A2.
Neither irreducibility nor separability of (4) is needed.

## Review, comparisons, and excluded stronger readings

Astra independently supplied the all-mu stratification and Euler argument;
ROOT initially obtained the mu=0 obstruction with unnecessary external
hypotheses. Opus independently supplied the arbitrary-h obstruction,
the top-coefficient test and the positive plane control. ROOT's hostile
cross recomputed these from evaluation/derivative identities and made
the exceptional t-value in the linear-h case explicit. This is different-
model checking of Opus, but same-model checking of the additional
Astra/ROOT argument. The report remains UNPROMOTED throughout.

A separately frozen Astra hostile cross independently confirmed the
strata and shear argument and supplied the stronger all-beta component
argument just given. ROOT checked its dimension bound and dense-torus
step before inclusion. That addition is same-model co-checking, not
a different-model promotion. It removes the suggested small-n dimension
experiment rather than commissioning a new family.

Fable's overlapping top-coefficient/unit observation is valid after
correcting its proposed p=0 witness to x=1,y=-1. Its assertion that
r=c fibers avoid p=0 for nonzero c is not: the boundary lines in
section2 remain. Nor must every plane restriction cross p=0:
claim3 supplies a plane with p=1. Nonconstant-unit exclusions must
retain their nonconstancy hypothesis. Arbitrary parametrizations of
that positive-control plane can pass through a hypothetical Keller
pair; no such pair has been constructed here.

The old fixed-high-coefficient classification has two free low
outputs; the present lower-block restriction has three remaining
outputs before one further equation. The
[quartic invariant-section theorem](marked-quartic-section-swarmHQ-root-20260917T181100Z.md)
concerns a different target quotient. Neither old theorem alone
proves the assertions above. Bounded searches of frozen public evidence
and dated team history found the old fixed-high calculation as the
nearest relevant comparison, not a prior proof of these exact claims.
One overly broad search clipped and is not claimed exhaustive.
No originality, priority or comprehensive literature search is asserted.

No result covers arbitrary combinations involving b, nonlinear sections,
unrelated donors, or arbitrary plane maps. No coordinate search, parameter
farm, or small-n successor is commissioned. The current specified
continuation has a uniform manual obstruction; expanding the catalogue
would not itself change the missing global plane-source implication.

## Replay and integrity

Desk-only over C. No CAS, cloud computation, randomness, primes, or degree
range search. The literal polynomial and the displayed inverse formulas,
boundary equations and units provide the full algebraic replay data.
The Euler step uses additivity, chi_c(C*)=0 and chi_c(A1)=1.

Frozen evidence full-file SHA256:

    old fixed-high report a56a1de74b34a283e1c4f32bc4e316f0da372f4c75a18c60afd1fd96589333e5
    old quartic report 31a05849a5b5dba8a249be386133894dfe9f761d7f9021c91282863b4e8fcdaa
    ROOT initial cd580af5387b89f255d7470eb2a95ca05d60dd6a096a061d22e1d8562e6bf316
    Astra initial 02f9c0dd32235cf6707e5d1714e10b10ec5556c5e6bd742873a5eb18188daeff
    Opus initial 236572579e6826892018258694c9d0e9dd24bc2e0ae5d37fb81419c8e441386a
    Fable initial e3370da7dac533220de1cdbfacf8c54f6fcd1c27ad15bb33e449aa763ad3fefa
    ROOT cross af9e666e2ff0cf9bb73577718f084ed0d8924acb946d134b637dc08896836b8d
    Astra cross 2120fbf12591f68460ead43c9c762db9b3684baeaff0019d0332a26ea6e63174

Original assessment artifacts retain their internal/legacy custody.
This separately authored integration does not retrofit their seals.
The mathematical argument is complete here; hashes are integrity
evidence, not a substitute for proof or different-model promotion.

## OPENS RAISED

None. No new execution or automatic successor is requested.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `07082627defead2f55e05812b9ba81e45e59bbe4` (Git blobs only).
The preliminary scan used the terminal immutable ROOT cross at the
hash above. EMPTY is not novelty or mathematical certification; a
final report scan is required before banking.

Whole author readback and unchanged evidence hashes verified at measured
2026-09-30 01:50:11 UTC. The mathematical body is complete; only this
completion record and final marker were appended after that check.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12799`.
- Body SHA-256:
  `65d1e08795c8ac0af12f25a407af3ad85bd3eaba10d23cadbb0685a8374cf0d1`.
- Frozen basis: `07082627defead2f55e05812b9ba81e45e59bbe4`.
