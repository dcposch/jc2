# Independent gate: common4/Q bad-coefficient typing

September 9, 2026. **CONFIRMED AT PROSPECTIVE-OBJECT SCOPE, with one wire-notation correction.** This is an independent Astra review of Sol's coefficient typing, not a builder authorization, computation, point, properness, ideal-membership result or source exclusion.

## 1. Receipt-first boundary and exact reads

Before any producer/input proof body, I checked the terminal receipt SHA `88011bd4c732bde47abe6c6524a8f8cfe66830656ea344b96cad693f9f2dedce`, its DONE/exit0/CLEAN/BODY_SEALED/ABSENT fields, all ten declared post-UNCHANGED/current hashes, and producer report SHA `5bd69bddb0c63cd9ba1e1c1ef44943e03fe63d5c536a7c8fe93af3595b26a9a9`. I then read the whole producer, all281 lines of baseline.py and387 lines of exporter.py **statically only**, and all eight remaining frozen inputs, including whole lift/receiver/centering contracts. The dated audit/history excerpts are context, not a new foundational replay. Exact paths, lengths and all12 input/receipt/report pins are in owned input-pins.json.

No builder import, make_contract, production_spec, records traversal, full stream, remote process, live M gate or other peer artifact was accessed. Root's terminal-process observation is recorded parent provenance, not an independent process check here. The manifest/header supply retained artifact metadata; this gate does not newly traverse those historical streams.

## 2. Slot and coefficient verdict: CONFIRMED

For common4 the A polygon is exactly `0<=i<=9, 0<=j, i+j<=15`; B has `i<=15, i+j<=25`. Hence raw counts are

\[
\sum_{i=0}^9(16-i)=115,\qquad
\sum_{i=0}^{15}(26-i)=296.
\]

A has ten total-top slots, seven inner slots, one common intersection and one separately fixed origin:17 fixed,98 free. B has16+11-1+1=27 fixed,269 free. This includes fixed zeros; it does not count only nonzero face monomials. Static make_contract assigns lattice points in increasing i, then increasing j, A before B. Before A's i=8 column there are

\[
14+\sum_{i=1}^7(15-i)=91
\]

free entries. At i=8, j=0,...,6 are free, so `(8,4),(8,5),(8,6)` have IDs95,96,97. The slot `(8,7)` lies on the total top but not the inner face. H has g-exponents0 or3; choosing three such factors gives only multiples of3, so `[g^8p^7]H^3=0`, without expanding H³. There is no competing assignment or variable ID at that slot.

With normalized mu=1 and centering `p_old=p+1`, direct binomial coefficient extraction gives

\[
h=[g^8p^4]A(g,p+1)
 =a_{8,4}+5a_{8,5}+15a_{8,6}+35a_{8,7}
 =x_{95}+5x_{96}+15x_{97}.
\]

Only j=4,...,7 can contribute, by total degree15. Its weight is `5*8-7*4=12>3`, so it is genuinely one forbidden centered coefficient. Reversing the centering sign would change the j=5 coefficient to -5 and would not center `(p_old-1)`; the PLUS sign is load-bearing.

**Exact notation correction:** Sol calls the zero wire `[[0,1],[0,1]]`. Static `F.wire()` actually returns canonical strings, `[["0","1"],["0","1"]]`. The coefficient value zero, fixed-slot status and all formulas are correct. No erroneous emitted object exists here; nevertheless numeric and string JSON wires are not byte-identical.

## 3. Normalization and complete object: CONFIRMED

For raw monic faces and mu!=0, use tau=mu:

\[
\bar A(g,p)=\mu^{-15}A_{raw}(\mu g,\mu p),\quad
\bar B(g,p)=\mu^{-25}B_{raw}(\mu g,\mu p).
\]

It sends the common4 parameter to1, preserves both entire monic outer faces, and transports

\[
c\mapsto c\mu^{-36},\quad z\mapsto z\mu^{36},\quad
\lambda_2\mapsto\lambda_2\mu^{-3},\quad
\lambda_3\mapsto\lambda_3\mu^{-2}.
\]

The accepted lift's corresponding physical transformation is `P_mu(u,v)=mu^-15 P(mu^5u,mu^-1v)` (and exponent -25 for Q). Thus polynomiality and all105 negative-row obligations survive this normalization. In common4 no root extension is needed to choose tau: mu is already a same-field unit. The ring at hand has already made this normalization and has no mu variable.

Coefficient scaling gives `bar a_(8,k)=mu^(k-7) a_raw_(8,k)`. Equivalently, substituting p+1 before coefficient extraction gives exactly `h_bar=mu^-3 h_raw`, where `h_raw=[g^8p^4]A_raw(g,p+mu)`. This is not a second normalization of h. Centering is used only to define h on the original coefficient ring; no centered replacement of the inverse map is proposed. Fixing both original target constants to zero is consistent with that use.

The variable count and IDs are therefore98+269+4=371: A0..97, B98..366, c367, existing z368, lambda2/3 at369/370. Static exporter payload confirms the816 indexed row records:

- 44 fixed-assignment identities, with fixed values carried in coefficient records;
- all660 Jacobian slots `0<=I<=23, J>=0, I+J<=38`, including the target subtraction at `(2,0)`;
- all30 A and75 B negative-Laurent slots for the ORIGINAL lift;
- six fixed-unit nonorigin vertex guards and `z*c-1`.

The omitted120 universal triangular Jacobian slots have I>=24 and are identities: source g-degrees at most9/15 imply bracket g-degree at most23. The660 count is `sum_(I=0)^23(39-I)=660`. The FIX and fixed-unit guard records are zero polynomial identities in this substituted presentation, not extra independent variables or asserted nonzero equations. Both origins are fixed zero, not guarded nonzero. Neither lambda is localized.

Appending fresh z_h after lambda3 gives ID371, global dp in the extended displayed order, and the prospective row

\[
\texttt{GUARD/h}:\quad x_{371}x_{95}+5x_{371}x_{96}
                  +15x_{371}x_{97}-1.
\]

Thus372 variables and817 indexed rows is exact, retaining every original row, map and guard. If later serialized, variable tuples must retain the exporter's increasing-ID order; the displayed commutative formula is already correct. This review emits no such row stream. Localization is not h=1: replacing its guard by that equation would change the object.

## 4. Ideal status and acceptance arrow: CONFIRMED WITH SCOPE LIMIT

h is nonzero in the ambient polynomial ring because95,96,97 are distinct free generators. This proves neither h nonzero on the full source nor `h notin I_full` or `h notin sqrt(I_full)`. Sol's phrase “no supplied identity” is accepted only as the absence of an exhibited identity in this bounded typing argument, not an exhaustive ideal-theoretic conclusion. No ideal-membership test was run.

For the exact prospective ideal

\[
I_h=I_{full}R[z_h]+(z_hh-1),
\]

properness over Q yields a maximal-ideal point over an algebraic closure (indeed a finite algebraic coefficient extension), not necessarily over Q. All source guards/rows persist there. The accepted inverse map

\[
g=v^{-1},\qquad p_{old}=v^4u-\lambda_2v^2-\lambda_3v-v^{-1}
\]

has determinant +v². All105 negative coefficients vanish, so the two finite Laurent images are polynomials; their bracket is c and their monic top terms are `u15 v60` and `u25 v100`. Exact degrees75/125 and the named accepted plane-automorphism degree criterion give the sufficient counterexample endpoint. Neither the conditional published necessity chain nor any rational-point assumption is needed.

Conversely, `I_h=(1)` excludes only h!=0 on the complete source. Equivalently some power of h belongs to I_full; this says nothing by itself about the other forbidden coefficients or I_full being the unit ideal. Neither outcome is established here. The baseline's historical PENDING/independent_certification:false headers refer to its creation; the frozen accepted-audit context records later full-stream acceptance. This gate neither reopens that review nor upgrades a freshly uninspected stream.

## 5. Optional highest-g sanity relation — independently derived, not a new parent

Write the centered polynomials as `A=g9*u6+g8*A8(u)+...` and `B=g15*u10+g14*B14(u)+...`. The only pairs contributing g22 to their bracket are (9,14) and (8,15). Factored differentiation gives

\[
[g^{22}]J=u^5\{9uB_{14}'-84B_{14}+80u^4A_8-15u^5A_8'\}.
\]

The full target has no g22 term; comparing coefficients after the monic factor u5 gives the displayed bracketed identity. In particular its u8 coefficient is

\[
-12[u^8]B_{14}+20[u^4]A_8=0,
\qquad [u^4]A_8=h.
\]

This agrees with root's proposed sanity relation and does **not** alone force h=0. It is an exact consequence of a tiny pair of leading-g coefficient formulas, not a full bracket expansion or a certified point. It also explains why the “ambient free slot” statement must not be mistaken for independence modulo the Jacobian ideal.

## 6. Terminal evidence and stop

Verdicts: coefficient/sign/IDs **CONFIRMED**; parameter transport **CONFIRMED**; full prospective372/817 object **CONFIRMED**; sufficient properness and one-open unit endpoints **CONFIRMED**; actual properness, point, membership, whole-weight transfer, efficiency and decision **NOT CLAIMED/NOT TESTED**. The sole producer correction is canonical zero-wire string notation.

Evidence is static whole-file review and the independent coefficient/count proofs above. There is no mathematical code or executable mutation suite to claim. The sign and localization warnings are mathematical distinctions, not reported changed-object subprocess results. All execution was bounded metadata/publication only; no source or high powers were materialized. Inputs are rehashed before and after publication. No AWS/SSH/web, solver, agents, new external messages, canonical/protected edits or live peer access. The own transaction and custody record exact pins; all writers finish before terminal handoff. STOP/IDLE.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9528`.
- Body SHA-256:
  `cb96336ec80c97dba78ccc23a35a5b8610eccc2092f5f5f984aad5ffa7b19016`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
