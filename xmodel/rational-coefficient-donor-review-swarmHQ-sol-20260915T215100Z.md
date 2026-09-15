# FIRST review: rational-coefficient polynomial donors

Reviewer: swarmHQ Sol (gpt-5.6-sol), different-model hostile FIRST.
Startup: 2026-09-15 21:51:34 UTC. Evidence: MANUAL, relative to the
producer's named accepted geometric imports.

Reviewed banked contribution: `3ac89803169e7a61ec76fe7ccb341c91517f3f43`.
Producer full SHA256
`5983d82682419aa836ebe9966f15a34eda927f2739365ad73fe6c72b17dbaa16`;
manifest `4d7dd626a15aa084289518399a0259fc351272ba2eea85c59c593a2a84ea47e7`.
The producer and manifest were verified, hash-checked and whole-read before
review; their post-review hashes are unchanged. I also whole-read the accepted
Laurent producer and Fable FIRST and the binding AUDIT repairs at the scopes
named by the new report, without re-auditing their classical foundations.

## Verdicts

- Rational-coefficient dichotomy: **CONFIRMED**. A finite critical-value pole
  gives the stated non-A1 branch image; otherwise every p-fibre of the actual
  normalization has one reduced A1 component of multiplicity dividing m and
  `m Cl(S)=0`.
- Keller-source exclusion: **CONFIRMED**, conditional on exactly the accepted
  sandwich/nonproperness, purity, finite-etale, and Jelonek--Lason premises
  identified by the producer. The transfer permits arbitrary first-leg degree.
- Scope: q must remain polynomial of degree m>=2 in u with coefficients in
  C(p). Nothing proves a global cyclic cover, a rational-in-u extension, a
  target-compatible intermediate field for arbitrary Keller maps, or JC2.

## Hostile reconstruction

Let d clear all finite coefficient poles and finite zeros of the leading
coefficient. On d nonzero, u is integral and the normalization is exactly
`C[p,1/d,u]`; its critical divisors are the horizontal components of P_u=0.
If a critical value has a pole over p=a, restriction of that place to the
branch-image field gives `v(p-a)>0` and `v(q)<0`. Were the affine normalization
A1, q would identify the place as its unique infinity while the nonconstant
regular polynomial p-a would have positive, rather than negative, valuation
there. This proves the first alternative without confusing the critical curve
field with its branch-image subfield.

Assume all finite critical values integral and fix a. In the DVR O at w=p-a,
write `a_m=w^ell b`. Adjoining a localized root `beta^m=b^-1` is essentially
etale with residue C. The Eisenstein extension `D=O'[t]/(t^m-w)` is a DVR.
After centering and putting `u=s+beta t^(-ell)v`, the polynomial H is monic,
centered, and has coefficients initially in `D[1/t]`. The accepted valuative
critical-value argument applies verbatim: a worst polar coefficient, after a
finite value-group extension and rescaling, would reduce to a non-pure-power
monic centered polynomial all of whose critical values vanish. Counting roots
against derivative multiplicities in characteristic zero forces that reduction
to be a pure m-th power, contradiction. Hence `H in D[v]`.

Set B=D[v]. The action `(t,v)->(zeta t,zeta^ell v)` fixes p,u,q and is faithful
on t, so its fixed fraction field is E(u). The subtle normalization assertion
survives attack: `S'=S tensor O'` is normal by essentially-etale base change,
and is a domain because C[p]-flatness injects it into its generic fibre E[u].
Both S' and `B^(mu_m)` are finite normal O'[q]-algebras with fraction field
E(u); uniqueness of normalization therefore gives `S'=B^(mu_m)`. No component
selection or global quotient is assumed.

Exactness of invariants in characteristic zero yields

    S'/wS'=(B/wB)^(mu_m),
    (S'/wS')_red=C[v]^(mu_m)=C[v^r],
    r=m/gcd(m,ell).

This is the actual normalized fibre: O'/w=C, so base change does not replace it
by a formal or residue extension. The t-adic value group of the invariant field
is `gcd(m,ell) Z`; since `ord_t(w)=m`, the unique reduced component has
multiplicity r. This includes ell=0 and negative ell, and r divides m.

Globally `S[1/d]` is factorial. Divisor localization leaves only primes over
zeros of d; the fibre calculation supplies exactly one such prime E_a and
`div(p-a)=r_a E_a`, with `r_a|m`. Therefore every divisor class is killed by m.
This patching uses neither a global good-reduction coordinate nor a global
cyclic cover.

For a whole-plane Keller substitution, integrality embeds S in C[x,y]. The
accepted local sandwich argument makes the finite second leg etale on the
source image, for first-leg degree one as well as larger degree. In the pole
case the omitted ramification divisor gives a nonproperness component whose
normalization the accepted polynomial-coverage theorem makes A1, contradiction.
Otherwise, if ramification exists, `m[E]=0` supplies `div(h)=mE`; normality makes
h regular, its pullback is a zero-free polynomial and hence scalar, contradicting
that divisor. If ramification is empty, purity and triviality of connected
finite-etale covers of A2 contradict degree m>=2.

The controls agree independently. For `q=p(p-1)u^2`, adjoining
`z=p(p-1)u` gives the normal hypersurface `z^2=p(p-1)q`, with one A1 component
of multiplicity two over each of p=0,1. For `(u^2-1)/(p(p-1))`, the critical
branch `p(p-1)q=-1` is A1 minus two points. The m=1 example `q=u/p`,
`p=x,u=xy` gives an automorphism and correctly lies outside the theorem. The
split-fibre example has a critical-value pole, so it does not evade the
good-value hypothesis.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5459`.
- Body SHA-256:
  `46777bfcb8b991a84de9580498821ae1436a44d852ad2605c0a11bece5a3181b`.
- Frozen basis: `3ac89803169e7a61ec76fe7ccb341c91517f3f43`.
