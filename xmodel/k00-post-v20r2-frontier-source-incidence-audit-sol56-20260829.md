# Post-V20R2 frontier: valuation exhaustion versus source incidence

Date: 2026-08-29  
Author: Sol 5.6 Ultra  
Frozen campaign basis: `31777ce90994a106aade85064c0d868e32863f94`  
Status: **SEALED DESK AUDIT / NO K00-WIDE OR JC2 VERDICT**

## Verdict

If the review-gated valuation-three and valuation-five exclusions promote and
both reviewed valuation-four residuals `R4-00` and `R4-02` are proved empty,
then the valuation atlas is exhaustive **for the registered normalized
V20R2 `K[[Lambda]]` source functor**.  It would exclude every formal section
of that one functor, because every nonzero transverse series has one positive
integer order and the zero series is already killed at grade 19.

That conclusion is not yet K00-wide, even for the underlying fixed
`U=2,[6,2]` support.  V20R2 is an unramified `Lambda`-section compiler, while
closure-first incidence permits a DVR arc with

```text
Lambda = unit * t^e,       e >= 1.
```

No reviewed theorem forces `e=1`, or forces all other coordinates to be
series in `Lambda`.  The current integer atlas therefore does not by itself
exhaust the ramified arcs of the algebraic source.  It also omits the named
`C6=0` tip, `k10=0`/delayed-load faces, other load rays and square normal
cones, and the unmapped part of the collision terminal receiver.

The cheapest post-V20R2 packet is consequently a source/valuative comparison,
not another integer-valuation calculation.

## 1. Exact conditional endpoint inside V20R2

The frozen source is

```text
Phi_l = r_l(C,Lambda^2 k10,Lambda^6 k6,Lambda^10 k2)
        - Lambda^(12+l) delta_l,
delta=(0,mu2,0,mu4,0,mu6,Jdet/4),
```

at `C6=1`, with `k10[0]` and `Jdet[0]` units and

```text
k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0.
```

For a V20R2 section put

```text
m = min_i ord_Lambda(d_i).
```

There is a literal disjoint partition

```text
d=0
disjoint union {m=1} disjoint union ... disjoint union {m=5}
disjoint union {m>=6}.
```

No periodicity or cross-valuation analogy is used in this partition.  The
promoted results close `m=1`, `m=2`, `m>=6`, and `d=0`; the current
review-gated results would close `m=3` and `m=5`; valuation four is exactly
the still-live union `R4-00 disjoint union R4-02`.  Thus closing those two
residuals and promoting the two reviews would exhaust this partition.

An empty grade-19 jet functor excludes a same-source formal `K[[Lambda]]`
section without any lifting theorem: a formal section would have a
grade-19 truncation.  The converse is deliberately not used.  A surviving
finite jet would not be a formal arc, and no surviving cell is currently
asserted nonempty or attained.

## 2. Why this is not closure-first exhaustion

The relevant generic K00 incidence was registered in

```text
A = Q[Lambda,C0,...,C6,k10,k6,k2,mu2,mu4,mu6,Jdet],
I = (Phi1,...,Phi7),
K = I:Lambda^infinity:Jdet^infinity,
B = K+(Lambda)+M_K00,
H = B:(C6*k10*Jdet)^infinity.
```

The order is mandatory: source saturation, then the `Lambda=0` boundary and
K00 core, then the final generic-ray localization.  Restricting to K00 before
saturation gives the known unit certificate but does not compute `H`.

If a point of `V(H)` is genuinely approached from the source open, curve
selection/normalization supplies a DVR pullback.  In general it has

```text
Lambda(t)=u(t)t^e,            ord_t d(t)=m,
ord_t k10(t)=0,               ord_t Jdet(t)=0,
ord_t(k6,k2,mu2,mu4,mu6)>=1,
```

with `e,m` positive integers.  After a permitted finite unit/Kummer
extension one may normalize units, but one may not replace `t^e` by `t`
while retaining the V20R2 weights unless a separate theorem licenses it.
The pulled-back loads begin at `2e,6e,10e` and the targets at
`14e,16e,18e,19e`; transverse coefficients can occur at exponents not
divisible by `e`.  The current compiler is the special case `e=1`.

The minimal negative control is

```text
x^2-Lambda=0.
```

Its origin is approached by the ramified arc `Lambda=t^2,x=t`, but it has no
solution `x in K[[Lambda]]`.  Therefore emptiness of all unramified
`Lambda`-sections cannot be promoted to algebraic closure emptiness by formal
logic alone.  For arbitrary DVR arcs the natural atlas is at least the pair
`(e,m)`, or the rational slope `m/e`, together with the load/target orders;
the existing list `1,2,3,4,5,>=6,infinity` is not that atlas.

Accordingly:

- **Yes:** the atlas is exhaustive for the literal normalized V20R2 section
  functor.
- **No, not yet:** it is not proved exhaustive for closure incidence of the
  fixed support, K00 as a whole, or any actual-map source.

## 3. Remaining K00 support and normalization obligations

Even after the generic V20R2 section functor is empty, the following are
separate obligations.

1. **Weighted Kummer chart.**  `C6=1` is faithfully flat over `D(C6)` and is
   the correct generic-ray slice.  Emptiness there can descend on that open,
   provided the full loaded group action and opens are serialized.  It says
   nothing about the named `C6=0` (`rho=0`) tip.  The deck mate `T=-1` is
   unit/deck-equivalent to `T=1` and is not an additional component of this
   client.
2. **Load faces.**  `k10[0]!=0` selects one load ray.  Arcs with `k10` tending
   to zero, a later first `k10` coefficient, or a different first nonzero
   lower load are not covered.  Nor are other square-normal cones.  The five
   displayed zero constants are correct special-point equations for this
   K00 core; they are not a theorem that every relevant receiver point has
   this load profile.
3. **Jacobian open.**  `Jdet!=0` is the intended Keller-source condition and
   its zero locus need not be covered for an exclusion, but the source map
   must identify this symbol with the actual nonzero Jacobian constant and
   preserve the open.  Formal use of a symbol named `Jdet` is not that map.
4. **Receiver incidence.**  The full collision emitter and terminal-receiver
   pullback, including correction jets and Gate T, are not supplied by the
   seven ordinary tails.  Ordered chart certificates do not fill this map.
   The registered `M_K00` incidence is only the generic K00 ray of the fixed
   `[6,2]` ordinary-tail client.

The two finite Taylor families are still necessary for any claimed
trajectory or positive realization.  They are not needed to propagate a
valid negative inclusion: emptiness of an over-approximating tail source
would exclude its Taylor-realizable subset.  In particular, no compatible
finite row, residual packet, or algebraic boundary point is attainment.

## 4. Cheapest next packet

Register `K00-V20R2-VALUATIVE-COMPARISON/v1` before compiling another support.
It is a proof-sized source packet with these mandatory fields:

1. pin the exact ring `A`, all seven frozen rows, `M_K00`, the opens, and the
   saturation/restriction order above;
2. state the one implication actually needed:

   ```text
   generic K00 closure incidence
      => normalized DVR source arc
      => a member of a declared complete valuation atlas;
   ```

3. serialize the weighted `C6` Kummer action and finite-extension descent,
   rather than merely writing `C6=1`;
4. emit `e=ord_t(Lambda)`, `m=ord_t(d)`, and the individual orders of
   `k10,k6,k2,mu2,mu4,mu6,Jdet`, with the literal pulled-back grade calendar;
5. return exactly one of:
   `UNRAMIFIED_REDUCTION_PROVED`, with a proof that every relevant arc reduces
   to `e=1`; or `RAMIFIED_RESIDUAL_EMITTED`, with the complete `(e,m,load)`
   cones and a literal source emitter for the first uncovered cone;
6. replay both `x-Lambda*m` (restriction/saturation noncommutation) and
   `x^2-Lambda` (ramified-section failure) as mandatory negative controls;
7. state separately whether the output concerns formal tail data, a source
   arc, a Taylor trajectory, or an actual polynomial map.

This packet is cheaper and more decisive than a new valuation fan: a positive
comparison would let a closed V20R2 atlas decide the already registered
generic incidence, while a negative comparison identifies the exact
ramified source cells instead of launching an unbounded guess.  Only after
this bridge should the `C6=0` companion and `k10=0`/other-load packets be
ordered.

## 5. What remains before JC2

Even a proof that the generic `[6,2]` K00 incidence is empty would close only
one coefficient-infinity client.  A JC2 implication still needs a reviewed,
provenance-preserving chain from a hypothetical counterexample to this
client.  Presently no reviewed selector forces maximum twelve, degrees
`(8,12)`, exact order two, Kummer order two, `U=2`, the divisor profile
`[6,2]`, the generic K00 ray, or its V20R2 normalization.  Other order-two
profiles for larger `U`, order-four Kummer clients, other terminal supports,
load faces, square/ramified branches, and other degree/order cells therefore
remain outside the conclusion.

V20R2's 140 equations are exact formal source data for their frozen client.
They are not a polynomial map, an occurrence theorem, or a counterexample.
No statement in this audit asserts that any residual is nonempty, attained,
algebraizable, Taylor-realizable, or source-reachable.

## Pinned readings

```text
4cdbd2ca462378adbcd0fba103f79a2ad9e5fbd6c6a7d81682ebc45230c2b1c4  V20 PREREGISTRATION.md
c2996ec867f481d62663517022dd86a7ebea9065d70f6d8d825d505a250140d8  K00 closure-first PREREGISTRATION.md
abcb00ab31807437601073454488a8b787e3c11aaaffb2083e2e16769a7648e5  K00 HISTORY_TYPE_AUDIT.md
9c5bf1229cf45dd7ea4d5d3907fd6033c88c0d9768934d01ea79e658f3d65a17  honest-source discriminator
5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b  one-parameter Rees reduction
e5e3472f052b2ae932daefc9dec7a17106ca4c13f8b920ba59da627d0653fec7  strict-Rees source client
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9694`.
- Body SHA-256: `44bedad691928a6b551409c4f084e6252c4c14ee4fe6f05880e64d5578f16c3b`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
