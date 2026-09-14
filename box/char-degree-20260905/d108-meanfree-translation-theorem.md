# The repaired D108 chart admits a diagonal-translation slice

This theorem concerns the supplementary chart with a free quadratic mean.
It does not license a jet0 pin in the frozen mean-zero chart. The original
free-mean runs remain separately identified; an optimized slice is another
presentation whose gauge must be recorded.

Let the physical source action be

    T_q P(x,y)=P(x+q,y+q).

It preserves the two placed top directions and restored monicity. The
major centre y-x is unchanged. Its normalized coefficient action, for
ambient degree N, is

    t^r z^j -> t^r z^j (1+qt)^(N-r-j).

All exponents are nonnegative in the source degree triangle. The inverse
is T_-q. In particular, leading homogeneous forms, beta=1, and the scalar
characteristic leader lambda are unchanged.

## Exact minor-arc transport

Write the old strict jets as j0,u,v. For the transformed polynomial use

    j0'=j0-q,  u'=u,  v'=v-qu,
    mu'=mu+q^2u-2qv,  c'=c.

Set A=q^2u-2qv. The exact relationship of generic parameters is

    t_old=t/(1+qt),
    pi_old=(1+qt)^3*pi-A+(3q^2v-2q^3u)t+(q^3v-q^4u)t^2.

It follows by substituting the new arc into y_old=y_new+q and solving
for the coefficient of t_old^3. This is an invertible formal change:
t_old has order1 with unit leader, and pi_old is affine in pi with
unit coefficient. At t=0, pi_old=pi-A. Therefore the entire old face
`-((pi_old-mu)^2-c)` becomes `-((pi-mu')^2-c')`.

For a physical polynomial P normalized by N,

    K_(T_q P)(t,pi)=(1+qt)^N K_P(t_old,pi_old).

Consequently complete coefficient-zero prefixes in t are stable in both
directions. The coefficient transformation is triangular in t-degree,
with an invertible affine change of pi on each diagonal block. Every
coefficient in pi is included by the actual full-support source rows.
The leading nonzero face also transports as the complete polynomial;
its prescribed powers12/8 use the transformed mean. Higher terms in the
pi change cannot create a lower t-band.

In particular, the source stage0–8 pole rows are a complete prefix
through local powers4–12, together with the preceding1–3 powers.
The t^0 term is already zero from the prescribed top. Their coefficient
ideals are covariant under this action. The shallow Jacobian rows need
no unsupported covariance claim about a selected subset of coefficients:
on the full characteristic chart, the proved bound deg J<=25 makes
all those bands zero already.

## Major chart and monic coordinate graphs

The action only raises r and fixes z-exponents, so preserves every
source degree triangle, z-degree cap, and D2 floor. Existing equality
faces are unchanged because no smaller-weight source coefficient is
available to contribute. Thus the fixed D2 face and beta=1 remain fixed.

The D1 prefix-moment argument is the one proved in
`d108-algebra-translation-audit.md`: a new moment at weight W receives
old moments at W-4l, and its binomial multiplier has degree at most
k+l. The old available bound grows by8l, which covers every required
moment. The inverse action has the same property. This applies to the
full major h2 block and each finite outer prefix.

Monic approximate-root and division graphs commute with the action.
For example, the defining degree bound for the unique monic approximate
root is preserved by translation. For the particular h2 source graph,
h2-h3^4 has z-degree at most26; this cap is preserved because z-degree
does not increase. The free output-coordinate graph consequently maps
to the same source coefficient space. The strong front zero bands are
preserved because r only increases, and the inverse has the same
triangular property.

The entire characteristic family has scalar target coefficients. Keeping
those coefficients fixed gives Q_new=T_q Q_old. Its actual total-degree
upper equations and whole homogeneous target are therefore equivalent.
The existential target-family formulation does not require identifying
the new x=0 canonical specialization with the old one. All original
source equations are transported through the declared coordinate map.

## The slice and its inverse

Choose q=j0. The transformed j0' is zero, while u',v',mu',c remain free
subject to the transported source equations. This spends the residual
diagonal-translation parameter once. It does not normalize mu, c,
beta, lambda, or the Jacobian scalar.

More explicitly, the full chart is the product of its j0=0 slice with
a free scalar s: given a slice point and s, apply T_-s to its physical
polynomials and put

    j0=s,  u=u',  v=v'+s*u',
    mu=mu'+s^2*u'+2s*v',  c=c'.

These polynomial formulas invert the map obtained with q=j0. Thus no
boundary is discarded, including u=v=0 with arbitrary mean. Building
the repaired incidence with jet0 set to zero and mu retained presents
this slice, provided every other source graph and row is retained.

## Actual source controls

`d108-meanfree-translation-control.py/.json` passes over exact Q and
binds the implemented free-mean adapter plus an actual stage1 input.
It checks a translated full h3 incidence with new jets(0,1,0), mean-1,
and face `-pi^2-2pi+1`. The translated h2 is reconstructed exactly in
the actual solved major source graph. On an actual stage8 outer graph,
all56 B2 and117 A3 moment rows remain zero after translation. The exact
minor generic-parameter formula and complete coefficient transport are
checked through local order12. An actual free-mean stage1 source point
retains both F/G zero prefixes through order5 before and after the map.

These controls substantiate the source-coordinate map; the preceding
formal proof covers every coefficient and every stage. They are not a
unit calculation or a claimed characteristic-chart survivor.
