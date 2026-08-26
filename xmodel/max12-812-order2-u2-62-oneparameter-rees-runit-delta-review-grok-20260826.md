# Delta review — localization at `R=1+tau` versus the `(tau,varrho)` boundary

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md` |
| Target SHA-256 | `5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b` |
| Claim under review | localizing at `R=1+tau` before generic-chart saturation does not change the scheme-theoretic `(tau,varrho)` boundary, including nilpotents and embedded structure |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none in this exact setup; the identity is `K+b=(K:R^infinity)+b`, not `K=K_R cap S` |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. No producer status line is evidence |
| Method | source reading and hand algebra only; SHA-256 of the target and of the two charged client files; no Singular, Sage, msolve, Lean, or substantive exact Python |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target is
`5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b`,
matching the required pin. The phrase “formal unit” in target §2 is not a
proof and was not used as one. No file other than this review was written.

---

## Charged bytes actually opened

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md` | `5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b` | target (matches required pin) |
| `xmodel/max12-812-order2-u2-62-strict-rees-client-20260825.md` | `e5e3472f052b2ae932daefc9dec7a17106ca4c13f8b920ba59da627d0653fec7` | original polynomial ring, seven-row ideal, interior/boundary pipeline |
| `xmodel/max12-812-order2-u2-62-strict-rees-client-erratum-v2-20260825.md` | `5aa954cbe6396ef5de353519eaf10aed567aec55964bb197c9eb1576b131c10b` | interior saturation by `tau,varrho,j` (equivalently their product) |

The original V2 coefficient/load ring is the polynomial ring over `Q` on
`tau,varrho,B_0,...,B_6,k_{10},k_6,k_2,mu_2,mu_4,mu_6,j`.  It does not
invert `R=1+tau`.  The factor `R` occurs only as a polynomial coefficient
in the odd-row twists and in `gamma_7=(j/4)R`.  Interior saturation is
`K=I:(tau varrho j)^infinity`; the boundary scheme before the coefficient
saturation is `V(K+(tau,varrho))`; the final object is
`H=(K+(tau,varrho)):(B_0,...,B_6)^infinity`.

---

## Strongest exact lemma that survives

Let `S` be a Noetherian `Q`-algebra (in particular the original V2
polynomial ring), `I subset S` an ideal, `R=1+tau in S`,
`b=(tau,varrho)`, `h=tau varrho j`, and `m=(B_0,...,B_6)`.  Write
`K=I:h^infinity subset S` and `K_R=(I S_R):h^infinity subset S_R`.  Then:

1. `(I:h^infinity)S_R=(I S_R):h^infinity`, so localization commutes with
   `h`-saturation.  Sequential saturation by `tau`, `varrho`, `j` equals
   saturation by the product `h`.
2. The contraction is strictly larger in general:
   `K_R cap S=K:R^infinity`.  In particular `K=K_R cap S` is false as a
   statement in `S`.
3. On the closed subscheme `V(b)` the two ideals agree exactly:
   `K+b=(K:R^infinity)+b` as ideals of `S`.  Equivalently
   `S/(K+b) cong S_R/(K_R+b S_R)` canonically, because `R equiv 1 mod b`
   forces `S/b cong S_R/b S_R`.  This is equality of quotient ideals, so it
   retains nilpotents, embedded primes, and every associated prime.
4. The same identity after the final irrelevant saturation:
   `(K+b):m^infinity=((K:R^infinity)+b):m^infinity`.
5. On `S_R`, the substitutions `C_i=R^(i mod 2) B_i` and `J=R j` are
   automorphisms, `h` and `Lambda J=tau^3 varrho R j` are associates up to
   a power of `tau` already present in `h`, and `(C_0,...,C_6)=(B_0,...,B_6)`.
   None of these changes the saturated ideal of `S_R` before restriction.
   On `S` itself, replacing `j` by `J` before restriction replaces `K` by
   `K:R^infinity`, which is then killed by (3).

The hypotheses actually used are: `S` Noetherian (so colon chains stabilize
and saturations are finite colons; commutation of saturation with
localization holds even as a union of colons without stabilization);
`R=1+tau`, hence `(R,tau)=(1)` and `R^n-1 in (tau) subset b` for every
`n>=0`; `b=(tau,varrho)`; `h` a product of the generic-chart factors;
`m` finitely generated.  The argument never uses emptiness, reducedness,
or a formal-power-series unit.

This delta compares two algebraic boundary schemes.  It does not decide
whether either scheme is empty or realizable.

---

## 1. Contraction is not the identity in `S`

Let `U={1,R,R^2,...}`.  For any ideal `J subset S` and any `f in S`,

```text
f/1 in J S_R    iff    R^N f in J for some N>=0.
```

Apply this to `J=K`, using commutation of saturation with localization
(Section 3 below):

```text
K_R cap S = { f in S | R^N f in K for some N } = K:R^infinity.
```

Always `K subset K:R^infinity`.  The inclusion may be proper: saturating by
`R` deletes primary components of `K` whose radicals contain `R=1+tau`.
Those components lie on `V(R)` and are disjoint from `V(tau)` because
`(R,tau)=(1)`.  They are invisible on the `(tau,varrho)` boundary, but they
are genuine extra generators of the contraction in `S`.  Any argument that
identifies `K` with `K_R cap S` before restricting to `b` is false.

The candidate slogan “if `f/1 in K_R` then `R^N f in K`” is exactly the
membership test for the contraction, and is correct.  It does not by itself
give scheme equality off `V(b)`.

## 2. Exact agreement after quotient by `b`

**Lemma.**  `K+b=(K:R^infinity)+b` as ideals of `S`.

The inclusion `subseteq` is immediate.  Conversely take `f in K:R^infinity`,
so `R^N f in K` for some `N`.  Expand

```text
R^N=(1+tau)^N=1+tau*s_N,     s_N in S.
```

Thus `R^N-1 in (tau) subset b`, and

```text
f = R^N f - (R^N-1)f in K + b.
```

Hence `f in K+b`.  This is an equality of ideals, not of radicals and not
of reduced supports.  The quotient rings `S/(K+b)` and `S/((K:R^infinity)+b)`
are therefore identical, and they have the same nilradical, the same
associated primes, and the same embedded components.

The same arithmetic in `S/b`: the image of `R` is `1`, so the image of
`R^N` is `1`.  If `R^N f in K` then the class of `f` in `S/b` equals the
class of `R^N f`, which already lies in the image of `K`.  An `R`-power
denominator in `S_R` cannot create a new class modulo `b`, because that
denominator becomes the unit `1` rather than a zerodivisor or a
non-unit.  In particular it cannot create a new nilpotent or a new
embedded prime on `V(b)`.

**Canonical identification of ambients.**  Write `S_R=S[U]/(R U-1)`.  Then

```text
S_R / b S_R  cong  S[U]/(R U-1, tau, varrho).
```

Modulo `(tau,varrho)` one has `R=1`, hence `U-1=0`, and the right-hand
side is `S/(tau,varrho)`.  The kernel of `S -> S_R/b S_R` is exactly `b`:
if `R^M f in b` then the image of `f` in `S/b` is zero because `R^M equiv 1
mod b`.  So `S/b -> S_R/b S_R` is an isomorphism, not merely a bijection on
closed points.  Every point of `V(b)` already lies in `D(R)`, because a
prime containing both `tau` and `1+tau` contains `1`.

The geometric content of “`R` is a unit on the formal chart `tau=0`” is
precisely `(R,tau)=(1)` together with `R^n |-> 1` on `V(b)`.  That pair of
identities, not a power-series slogan, is what the proof uses.

A weaker hypothesis still suffices and is recorded only to mark the
boundary of the argument: if the image of `R` in `S/b` is any unit, not
necessarily `1`, then `R^N f in K` still implies that the class of `f` lies
in the image of `K`, because that image is an ideal of `S/b` and one may
multiply by the inverse of `R^N`.  The present `R=1+tau` is the stronger
case, and the proof never inverts in `S/b`.

If instead one localized at an element vanishing on `V(b)` (for instance
`tau` itself), one would have `R^N in b` and the identity would collapse:
the localized boundary would be empty while the original boundary need not
be.  The hypothesis `(R,tau)=(1)` is therefore sharp for this style of
argument.

## 3. Saturation commutes with localization, and the order is not swapped

**Commutation.**  For any multiplicative set, and without Noetherian
hypotheses,

```text
x/s in (I:h^infinity) S_U
  iff  exists u in U and n>=0 with u h^n x in I
  iff  x/s in (I S_U):h^infinity.
```

In the Noetherian ring `S` the colon chain `I:h subset I:h^2 subset ...`
stabilizes at some finite `N`, so `I:h^infinity=I:h^N` and the identity is
the ordinary commutation of a finite colon with localization.  The
stabilized-colon language of the V2 client uses this Noetherian
stabilization; the set-theoretic union definition does not need it.

**Product versus sequential saturation.**  In any commutative ring,
`(I:a^infinity):b^infinity=I:(a b)^infinity`.  Thus the erratum’s
sequential saturation by `tau`, then `varrho`, then `j` equals saturation
by `h=tau varrho j`.  The same holds after localizing at `R`.

**Order of operations.**  The candidate argument saturates by `h` first
(commuting with localization), then compares the two ideals after adding
`b`.  It does not:

- identify `K` with `K_R cap S` in `S` (false, Section 1);
- saturate by `m` before adding `b`;
- quotient `I` by `b` and then attempt to saturate by `h` (on `V(b)` one
  has `h=0`, so that swap is meaningless);
- contract and then saturate by `R` as a substitute for localizing
  (that produces `K:R^infinity` in `S`, which is the contraction, and is
  then fed into Section 2).

No silent swap occurs.  The equality after adding `b` is an equality of
ideals of `S`, so the subsequent colon by `m` is the same operation on the
same ideal:

```text
(K+b):m^infinity = ((K:R^infinity)+b):m^infinity.
```

Finite generation of `m` and Noetherianness of `S` make this colon a
finite stabilized saturation, as in the client’s last step.  Equality of
ideals is preserved by any colon.

On the localized side, saturation by `m S_R` commutes with localization
by the same argument as for `h`, and after the identification
`S/b cong S_R/b S_R` the irrelevant saturation is the same colon of the
same ideal of `S/b`.

## 4. Replacing `j` by `J=R j`, without using the boundary lemma

**On `S_R`.**  Here `R` is a unit, so `R^n` is a unit.  For every `n`,

```text
I S_R : (R j)^n = (I S_R : j^n) : R^n = I S_R : j^n,
```

because coloning by a unit is the identity.  Hence
`I S_R : j^infinity=I S_R : J^infinity` as ideals of `S_R`, before any
restriction to `b`.  This uses only that `R` is a unit in `S_R`.  It does
not use Section 2 and is not circular.

The coefficient change `C_i=R^(i mod 2) B_i` is an automorphism of `S_R`
for the same reason, with inverse `B_odd=C_odd/R`.  The irrelevant ideal
satisfies `(C_0,...,C_6)=(B_0,R B_1,...,B_6)=(B_0,...,B_6)` on `S_R`.  The
product `Lambda J=tau^3 varrho R j` is, on `S_R`, associate to
`tau^3 varrho j`.  Saturating by `tau^3 varrho` equals saturating by
`tau varrho`: if `(tau varrho)^n f in I` then
`(tau^3 varrho)^n f=tau^{2n}(tau varrho)^n f in I`, and conversely if
`tau^{3k} varrho^k f in I` then `(tau varrho)^{3k} f in I`.  Thus the
generic-chart factor after the invertible change yields the same saturated
ideal of `S_R` as `h`.  On `V(b)` the automorphism is the identity because
`R equiv 1`.

**On `S`, before restriction.**  Replacing `j` by `J` without inverting `R`
does change the saturated ideal:

```text
I:(tau varrho J)^infinity = I:(R h)^infinity = (I:h^infinity):R^infinity
  = K:R^infinity.
```

That is the same extra `R`-saturation as the contraction in Section 1.
Section 2 then says it becomes invisible after adding `b`.  The target
performs the `J`-change after localizing, so it is in the `S_R` case, where
the saturated ideal is literally unchanged before restriction.

## 5. Target language versus the lemma

Target §2 asserts that the change `(B,j)->(C,J)` “is an automorphism after
localizing at `R`, and `R` is a unit in the formal chart at `tau=0`.”  The
first clause is correct on `S_R` (Section 4).  The second clause, as
written, is not a proof that localization commutes with the boundary
scheme.  The precise replacement is the ideal equality of Section 2, which
uses `(R,tau)=(1)` and `R^n |-> 1 mod b` and never a formal-power-series
ring.

The quoted load-bearing claim is nevertheless true in the exact generality
needed for this client: the original polynomial V2 boundary
`H=(K+b):m^infinity` coincides, as a closed subscheme of `Spec(S)` and
including nilpotents and every embedded component, with the boundary
formed after localizing at `R`, saturating by the generic-chart factor,
quotienting by `b`, and saturating by the same irrelevant ideal.  No extra
hypothesis is missing.  The only identity that must not be claimed is
`K=K_R cap S` in `S`.

The candidate argument is valid for the stabilized colons used here, once
it is read as “the images in `S/b` of `K` and of `K_R cap S` coincide,”
not as equality of those two ideals in `S`.  Extension `K S_R subset K_R`
is automatic.  Final irrelevant saturation of equal boundary ideals
preserves equality.  No order of contraction, quotient, or saturation is
swapped.

---

## Firewall

This delta compares two presentations of one algebraic boundary scheme.  It
does not prove that scheme empty or nonempty, does not realize a Taylor
arc, does not exclude the fixed `[6,2]` source, does not close order two,
does not close `(8,12)`, does not prove maximum twelve, and does not prove
JC2.  It does not audit the toric map `Lambda |-> tau^3 varrho`, flatness
of `Q[Lambda] -> Q[tau,varrho,R^{-1}]`, or row-by-row identity of `(0.1)`.

CONFIRMED
