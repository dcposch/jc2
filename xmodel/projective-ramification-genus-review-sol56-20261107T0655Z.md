# Independent hostile review: projective ramification genus

Verdict: **CONFIRMED_AT_NAMED_FOUNDATIONS**

Finalized UTC: 2026-11-07T07:00:32.644691+00:00
Task: `projective-ramification-genus-review-sol56-20261107T0655Z`
Reviewer configuration: gpt-5.6-sol / ultra; hosted identity UNVERIFIED.
Candidate producer: swarmHQ ROOT/Astra. The candidate was not presumed correct or novel.
Lifecycle effect: none; this report does not itself promote the claim.

## Exact reviewed statement

Over `C`, let `X` be a smooth irreducible projective surface, let
`h:X -> P^2` be finite of degree `N>1`, and let `L` be a target line.
Assume that `U≅A^2` is an open subset of `X`, that `h` is étale on
`U`, and that `h(U)` misses `L`. Let `H=h^*L` and let `R` be the
full ramification divisor with its different multiplicities. Conditional on
the named standard surface foundations and the supplied exact
CUBIC-SCROLL-DONOR-1 interface, the proposal proves `p_a(R)>=1`.

## Integrity and reading account

- Authorized startup succeeded at `2026-11-07T06:52:04.876155+00:00`;
  its ACK is mode 0444. The copied packet reader had the required SHA-256
  `47e3aea5fd494d0966aad35312aa3eea689a000b05289bd03646b9e5d577fbe4`.
- Preflight returned VERIFIED_PACKET for all 17 members and the one sealed
  proposal. No pin, hash, mode, ancestry, LF, or canonical-seal failure
  occurred.
- Whole non-STATE reading was exactly 1785 LF: MANIFEST 268; nine governors
  1342; ADMISSION 63; METHOD 9; PROPOSAL 67; CUBIC_INTERFACE 36.
  Whole STATE reading was 82 LF. Historical reading was exactly 103 LF,
  namely PROPOSAL 67 plus CUBIC_INTERFACE 36.
- Before the first real window I mistakenly queried unsupported
  `body --help`; it exited 2 and displayed zero body lines. I did not rerun
  that command. I then queried `window --help` and used the declared
  `window` interface. These two help outputs totaled 16 LF. Repeated body
  reading and report-body preview were both 0 LF; the repeat/help/preview
  charge was therefore 16/100 LF. No command correction allowance was used.
- No web, source, history, or repository search; no CAS, control family,
  degree farm, secondary model, model retry, adapter/settings/auth change,
  protected-repository access, or shared-document/Git mutation was used.

## Check of the proof

Write `Q=2K_X+3H=K_X+R`. Standard finite-map facts apply here:
a finite morphism between these smooth equidimensional surfaces is flat,
`H` is ample with `H^2=N`, and Riemann--Hurwitz gives the effective
Cartier divisor `R=K_X+3H`. In residue characteristic zero the
codimension-one different exponent is `e-1`.

Assume for contradiction that `p_a(R)<=0`. Adjunction/Riemann--Roch for
the full, possibly nonreduced and disconnected Cartier divisor gives
[
 Q.R=(K_X+R).R=2p_a(R)-2<0.
]
Thus `Q` is not nef. On the `K_X`-nonnegative part of the curve cone,
`Q=2K_X+3H` is positive away from zero. The surface cone theorem
therefore supplies a `K_X`-negative extremal ray on which `Q` is
negative.

The contraction classification leaves no missed case.

1. For a birational ray, its curve `E` is a `(-1)`-curve, hence
   `Q.E=-2+3H.E>=1`, a contradiction.
2. If the contraction is to a point, rationality of `X` and the smooth
   surface classification give `X=P^2`. Writing `H=O(m)), negativity
   is `-6+3m<0), so `m=1` and `N=1), again impossible.
3. Otherwise the contraction `pi:X->B` is to a smooth curve. Its general
   fibre `F` has `K_X.F=-2`; negativity gives
   `-4+3H.F<0`. Since `H.F` is a positive integer, `H.F=1`, and
   consequently `R.F=1`.

The last case genuinely makes `X` a Hirzebruch surface; no unspoken
relative-minimality hypothesis is needed. Rationality of `X` forces
`B=P^1`. For every scheme fibre
`F_b=sum m_iE_i`, ampleness and numerical equivalence with `F` give
[
 1=H.F_b=sum m_i(H.E_i).
]
All summands are positive integers, so every fibre is one reduced
irreducible curve. Flatness over the smooth curve and constancy of
arithmetic genus then rule out a singular fibre: a reduced irreducible
singular rational curve would have positive delta and hence positive
arithmetic genus. Thus `pi` is a smooth `P^1`-bundle over `P^1`;
equivalently `X=F_n` for some `n>=0). This also verifies the proposal's
explicit singular/reducible-fibre review target.

Intersecting the effective divisor `R` with `F` now shows that it has
one horizontal prime `C), with coefficient one and `C.F=1); all other
components, if any, are vertical. The effective pullback `T=h^*L`
likewise has one horizontal prime `B), with coefficient one and
`B.F=1`.

The two horizontal primes are distinct. If `C` were a component of
`T`, finiteness would give `h(C)=L`. The coefficient one of `C` in
the different `R` is `e_C-1), so tame characteristic-zero
ramification gives `e_C=2). But the coefficient of `C` in `h^*L`
is then two, forcing `T.F>=2), contrary to `T.F=1`. This checks the
ramification-index/pullback-multiplicity step even when the residue degree
of `C/L` exceeds one.

Every prime in the support of `R` or `T` lies in the boundary
`X-U`. Divisor-class localization is applicable to the normal surface
`X` and the open `U`:
[
 C^*=Gamma(X,O_X)^* longrightarrow Gamma(U,O_U)^*=C^*
 longrightarrow igoplus_{Zsubset X-U, {
m codim}=1} Z[Z]
 longrightarrow {
m Pic}(X) longrightarrow {
m Cl}(U)=0.
]
The first arrow is an isomorphism, so the boundary-prime group maps
isomorphically onto `Pic(X)=Z^2`. Hence there are exactly two boundary
curves. Since `C` and `B` are already distinct boundary curves, they
are all of them and form an integral basis. The unique-horizontal
statements then force `R=C` and `T=B`, with no vertical components.
Possible isolated points of `X-U` do not occur in the codimension-one
sum and do not affect either the isomorphism or the later inclusion
`U subset X-(supp R union supp T)`.

Let `S,F` be the standard basis of `Pic(F_n)`, with
`S^2=-n`. From `H.F=1`, write `H=S+bF). Ampleness gives `b>n),
and
[
 N=H^2=2b-n,qquad
 R=K_X+3H=S+(3b-n-2)F.
]
Because `R,H` are the integral boundary basis, their determinant has
absolute value one:
[
 left|b-(3b-n-2)
ight|=|2-N|=1.
]
With `N>1`, this forces `N=3`; then `2b-n=3`, `b>n`, and
`n>=0` force `n=1,b=2`. Thus the same finite map is a cubic
`h:F_1->P^2`.

The supplied accepted interface applies without enlargement: it covers
every finite cubic `F_1->P^2` and every target line. The original open
immersion `U≅A^2->F_1` is everywhere defined, has dense image, and lands
in
`F_1-(supp Ram(h) union supp h^*L)`.
It is therefore precisely the dominant morphism prohibited by
CUBIC-SCROLL-DONOR-1. This contradiction proves `p_a(R)>=1`.

For a nonempty reduced rational SNC forest with `c` connected
components, `chi(O_R)=c`, hence `p_a(R)=1-c<=0`; the stated forest
consequence follows.

## Limits

The cubic-scroll interface was consumed only at its supplied
MANUAL/BOOK-relative reviewed scope; its proof was not freshly audited.
The cone/contraction theorem, smooth ruled-surface classification,
Riemann--Roch/adjunction, finite-map Riemann--Hurwitz and tame DVR
multiplicity, and divisor localization remain named standard imports,
all with hypotheses met above.

This says nothing about a singular projective normalization, and replacing
one by a resolution would not preserve finiteness. Arithmetic genus is
not geometric genus. Positive arithmetic genus may come from incidence, singularities, or
nonreduced structure; disconnectedness does not turn it into geometric genus.
The result neither supplies smoothness for an actual Keller
normalization nor proves JC2 or novelty.

Final verdict: **CONFIRMED_AT_NAMED_FOUNDATIONS**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7650`.
- Body SHA-256:
  `2d2549622c62c7a6ac4ef2ebe8ecdb199337e0cf7dcb85024dbb6bcc234acf89`.
- Frozen basis: `bc9a5972e4215486b0bb3fc6ae419f07781dbb9f`.
