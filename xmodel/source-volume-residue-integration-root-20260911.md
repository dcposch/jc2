# Source-volume residue: exact Wright duplicate, not a new source case

ROOT, 2026-09-11. MANUAL / UNPROMOTED integration. JC2 unresolved.
Frozen basis: 0d39df3c9fd69c939a8420c54d03228b9077777d.

## Outcome and decision

The proposed affine surface cannot carry ANY extending constant-Jacobian
pair, without degree or support restrictions. However, ROOT's separate
history check identifies the marked surface exactly with Wright's already
proved m=3, alpha1=-1, alpha2=0 case. This is a classical duplicate, not
a new exclusion of an unretired actual-Keller source. Close this candidate;
do not buy an echo gate or launch an automatic family enlargement.

The task's useful discriminator is its sharpness: higher-order Laurent
terms can have zero residue and an explicit global primitive. This
obstruction does not close the campaign's S/T construction.

## Exact geometry and obstruction

Let Y be the affine scheme

    xy=z(z-1), xw=zy, y^2=(z-1)w.

The terminal [Astra report](source-volume-residue-astra-20260911.md) checks
the entire scheme on D(z-1),D(z), then obtains two full plane charts:

    U0: (x,z,y,w)=(x,xu,u(xu-1),u^2(xu-1)),
    U1: (x,z,y,w)=(x,1+x^2v,xv(1+x^2v),v(1+x^2v)^2).

Their overlap is x!=0 and u=xv+x^-1. The omitted line E=Y-U0 is
x=0,z=1,y=0. The form omega=dx wedge du extends as x dx wedge dv,
with divisor E. The localized plane charts prove smoothness and
integrality, not just a dense birational parametrization.

Local primitives -u dx and -xv dx differ by -dx/x. If a global regular
primitive existed, the polynomial Poincare lemma on the two planes would
make -dx/x the differential of an element of C[x,x^-1,u]. That is
impossible: the x^-1 coefficient of an x-derivative of a Laurent
polynomial is zero. For P,Q regular on Y and J_(x,u)(P,Q)=c!=0,
c^-1 P dQ would be just such a primitive. This proves the claimed
unrestricted exclusion, without any all-source classification.

## Exact marked Wright identification: ROOT calculation

On U0 put X=u and Y0=x. The actual embedded coordinate ring is

    C[x,xu,xu^2-u,xu^3-u^2]
      = C[Y0,XY0,X^2Y0-X,X^3Y0-X^2].

This is literally Wright's m=3, alpha1=-1, alpha2=0 ring. To check the
marking geometrically, introduce a different second plane chart

    (s,W) -> (x,z,y,w)=(s+s^3W,1+s^2W,sW,W).

Its image is Y-L, where L={z=y=w=0}, the retained line u=0 in U0.
An inverse is s=x/z on D(z) and s=y/w on D(w), with W=w. These formulas
agree by xw=zy; the relations give z=1+s^2W, y=sW, x=sz on both opens.
D(z) union D(w) is precisely Y-L. Thus both compositions are identities
on the full chart. Together with U0 it covers Y, and their overlap is
u!=0, with transition

    s=u^-1, W=u^3x-u^2.

This exhibits the P1 bundle with the SAME marked source plane and missing
fibre E; it is not an abstract surface isomorphism that changes the
etale-chart condition. Direct differentiation also gives
omega=s ds wedge dW, consistent with its simple zero along E.

Wright's coefficient-nonzero theorem therefore already covers this ring.
See David Wright, [Affine surfaces fibered by affine lines over the
projective line](https://www.researchgate.net/publication/258233253_Affine_surfaces_fibered_by_affine_lines_over_the_projective_line),
Illinois J. Math. 41 (1997), Theorem3.3. The generator and transition
conventions are explicitly restated in
[Rodriguez Diaz, Theorems3.7 and3.9](https://arxiv.org/html/2403.02219v2).
Only these formulas/restatements are used; none of that preprint's stronger
source-classification or final coordinate-change claims is imported.

The mechanism itself was already recorded in the campaign's
[September7 d125 torsor discriminator](d125-torsor-geometry-discriminator-astra-20260907.md),
SHA7beff9e113580e22aba68f79811ed45f2023e195f7998a51cd224163a775db5a,
read WHOLE by ROOT. Its actual m=4 receiver has alpha1=0, so the
coefficient obstruction does not exclude that receiver.

## Sharpness and surviving limits

For plane charts glued by u=x^m v+g(x), m>=0, an extending pair requires
Res(g(x)dx)=0. No affineness, sufficiency or exhaustive classification is
asserted for arbitrary such gluings. For g=lambda*x^-k, k>=2, the forms

    beta0=-(k*u*dx+x*du)/(k-1),
    beta1=-((m+k)*x^m*v*dx+x^(m+1)*dv)/(k-1)

agree on the overlap and differentiate to omega. For the campaign's
T:t^2-1=x^2Z, the transition y=v-2x^-2 is exactly m=0,k=2,lambda=-2.
It therefore has a global primitive. Exactness is necessary for a
constant-Jacobian pair; it does not produce one of the special form P dQ.
Neither the T pair nor a general Keller-source landing theorem is supplied.

Other selected primary checks did not supply shortcuts: Regeta's
[Theorem4.1 and Remark4.2](https://arxiv.org/pdf/1311.0232) make universal
aff2 algebraicity a JC2 reformulation and exhibit nonintegrable sl2;
automatic Lie integration is unavailable. The 2021
[bracket-width paper](https://ems.press/content/serial-article-files/26631?nt=1)
states Hypothesis(J), rather than proving it. Its sum-of-brackets and
standard Danielewski discussions supply no single Keller pair on T.
These were selected passage reads, not whole-paper audits or a completed
web round. The explicit surface proofs above do not depend on them.

## Terminal custody and bounded scope

Astra actual work23:43:31--FINAL idle23:49:53UTC:382 author-wall seconds,
not billing, credits, CPU or account-wide usage. Original reserveSep12
00:00/HARD00:03 met. ROOT received FINAL, then read custody FIRST/WHOLE,
hash996ea100ec68218dff2fd06db2c7259fd8262b85e90813c57c7914e87dcd1a5d.
All three input and three owned pins matched; report/PINS/manifest were
read WHOLE. Exact artifact expected-verification returned VERIFIED:

- report cfdda7018c4dd47e3aa1a155e33504116e3d7151c1c8d83aa855f0032ea4e342;
- manifest 7c6527fc9f16aa03c3fa0f797936fd3bb0345f2c78a2f08984c176b10b723735;
- PINS d15df3f9b32e38f0f93f66bcd61d98e1c8b25d2ddcfba829bbb4eb90e1482f17.

ROOT's Wright comparison was not an added premise in Astra's frozen
three-input task. Same-family co-research is not different-model promotion.
No AUDIT promotion, new canonical OPEN or descendant is selected.

QUANTITY: existence of unrestricted extending constant-Jacobian pairs on
this exact marked Y, and whether its exclusion is genuinely new.
CHEAPEST TEST: manual chart/residue computation and exact generator/transition
comparison; performed, no scientific subprocess. COLLISIONS: classical
Wright alpha1-nonzero case and existing d125 mechanism; no new OPEN to scan.
Own WHOLE readback and basis/scope checks precede sealing. No CAS/AWS
allocation, Fable call, protected access, shared-evidence deletion or commit.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6646`.
- Body SHA-256:
  `9c19fb9e36b116fc720fb714b018571cd096a7c0ed74df13ec1a366606e0b961`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
