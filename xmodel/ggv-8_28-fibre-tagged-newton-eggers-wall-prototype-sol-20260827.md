# One-chain GGV `8_28` -> fibre-tagged Newton/Eggers--Wall prototype

Date: 2026-08-27  
Author lane: Sol, `actual_total_g20`  
Verdict: **EXACT ONE-CHAIN CONTROL / NOT KELLER / NOT G2-PSC**

## 0. Bounded question and answer

I selected the already reviewed live GGV S4 chain `8_28`.  It has the
nontrivial MN step

\[
 (A_0,A'_0)=((8,28),(1,0)),\quad
 (\rho,\sigma,p,q)=(4,-1,3,4),\quad
 (m,n)=(3,2),\quad A_\gamma=(11/4,7).
\]

For one explicit polynomial realization, a paired, fibre-tagged
Newton--Puiseux/Eggers--Wall-style packet can be built exactly and can be
linked coefficient-by-coefficient to the GGV edge.  It recovers both
infinity charts, all 72 sheets of the smaller component, conjugation orbits,
residual polynomials, pole labels/orders, and the nontrivial Sigray
Q/jump/max transition `1 -> 4 -> 28`.

The current GGV ledger by itself is **not faithful enough** to determine that
packet.  A mutation with the same support, Newton polygons, complete-chain
record, common `(4,-1)` face, residual multiplicity `gamma=7`, and sheet
counts changes one pole order and total pole mass.  Thus the missing
invariant is not another corner number: it is paired, fibre-tagged residual
coefficient data in every infinity chart, together with its deck action and
an explicit source-to-flag map.

This is one non-Keller control, not the general corner-to-tree theorem and
not G2-PSC.

## 1. History and custody check

The prototype reads the live record, not a copied transcription.  Before
construction I ran `git log --follow` and targeted `git blame` on every
consumed source.  The relevant history is:

- `lib/families.py:442-488` and `tests/test_families.py:218-270`, including
  every `8_28` field, come from commit
  `25bc5cb5e1b352c59b599e88cf5d62e22e461ce0` (2026-08-05).  Their current
  SHA256 values are respectively
  `729a5ee7dd235ccca2138fd80035e08e3fed87fabf98a8fc4a0c7f9da089bd3e`
  and `845d42a2d410234f889d5d846f22f7152354896c67ab3d49152469260e892c0d`.
- `ladder/TRANSPORT.md` was introduced at
  `de4a7e6c4b7638a7db5f82bd00096903f7809cb8` and moved in the repository
  reorganization at `76e5346c90e14fbe30198070b5ce0629954558e3`.
  Its warnings that the rational ledger is not a corner-to-tree functor and
  does not determine fibre tags, residual cancellation, or pole status are
  original lines 448-463 and 699-701.  Current SHA256:
  `39a607c8935153c814cd51fb65a2f1c708a9e4ba5e1dd0f38f9c96401fc4a624`.
- The hostile transport review is
  `xmodel/grok-transport-review.md`, commit
  `12c09a22bb6a0de070045a2f18b087c76e3fb565`, SHA256
  `aa7fe37ba5c75df5f006d0af918d2315557b4db60b10cbc5954dfbf171cf558a`.
  It independently replayed the live `8_28` dump and confirms the exact
  GGV-to-Sigray normalization scope while retaining the tree-data gap.
- The Q/jump/max repair and different-model review are
  `xmodel/sol-h5a.md` at
  `7ddb48402965c7cf6b47ca90c0e8b59ba1236ea5`, SHA256
  `dd09069baeeaaa38644963571f929077af016cbbac664aaea9f3f50bee8f6d90`,
  and `xmodel/grok-h5a-review.md` at
  `c4ff436b088d16592c9478189b7e0677537ca2ca`, SHA256
  `3b8bd5c9e2a1f4132cff4353e0e7e0fd9b4426cbeea0b0c13d092161018f5d2f`.

The desk verifier pins all six hashes and fails before import on any drift.
The repository HEAD observed at construction was
`418e413593120d19e15e6546eb50c985f4b1f038`.

## 2. The exact control pair and the GGV edge

Put

\[
 z=xy^4,\qquad B=x(z-1)^7,
\]

and, for `tau` equal to 1 or 2, put

\[
 \begin{aligned}
 f&=B^2-x-y^8,\\
 g_\tau&=B^3-2x^2y^2+y^{12}+\tau xy^{15}.
 \end{aligned}                                      \tag{2.1}
\]

The native GGV component order is `(P,Q)=(g_1,f)`, with multipliers `(3,2)`
and degrees `(108,72)`.  The degree-sorted Sigray order is `(f,g_1)`, type
`(2,3)`.  This component bit matters.

With the convention that `in_(4,-1)` is the maximum-weight face,

\[
 \operatorname{in}_{4,-1}(f)=B^2,\qquad
 \operatorname{in}_{4,-1}(g_\tau)=B^3.
\]

The two face weights are 8 and 12.  The primitive common residual root is
`z=1` with multiplicity `gamma=7`; furthermore

\[
 v_{4,-1}(A_0)=4,\qquad
 \frac{\rho+\sigma}{v_{\rho,\sigma}(A_0)}=\frac34,
 \qquad
 \left(\frac{\gamma+4}{4},\gamma\right)=\left(\frac{11}{4},7\right).
\]

Thus this one edge realizes the live MN endpoint exactly.  Also

\[
 \begin{aligned}
 \operatorname{conv}(\{0\}\cup\operatorname{Supp}f)&=2S,\\
 \operatorname{conv}(\{0\}\cup\operatorname{Supp}g_\tau)&=3S,
 \end{aligned}
 \qquad
 S=\operatorname{conv}\{(0,0),(1,0),(8,28),(0,4)\}.
\]

This pair is only a geometry/control witness.  It is provably not Keller:

\[
 [f,g_1]\big|_{x=0}=-12y^{11}+8y^{22}.
\]

## 3. The two `f=a` fibres at `x=infinity`

Use `a=0,1`, set `x=s^-28`, and retain the exact key `z=xy^4`.  Multiplying
`f-a=0` by `s^56` gives

\[
 (z-1)^{14}=s^{28}+a s^{56}+z^2s^{112}.                 \tag{3.1}
\]

Hence

\[
 z=1+\xi s^2\left(1+\frac{a}{14}s^{28}+O(s^{30})\right),
 \qquad \xi^{14}=1,
\]

and, for `zeta^4=1`,

\[
 y=\zeta s^7z^{1/4}
   =\zeta s^7+\frac{\zeta\xi}{4}s^9+\cdots
    +\frac{a\zeta\xi}{56}s^{37}+\cdots .               \tag{3.2}
\]

The two fibres therefore have the same edge skeleton and topology, but the
fibre tag first changes `z` at `s^30` by `xi/14` and `y` at `s^37` by
`zeta*xi/56`.  Neither coefficient is in the present GGV lattice ledger.

### 3.1 Conjugation and sheets

There are `4*14=56` Puiseux presentations `(zeta,xi)`.  For a primitive
`omega in mu_28`, the two deck orientations act by

\[
 (\zeta,\xi)\longmapsto(\zeta\omega^{\pm7},
                         \xi\omega^{\pm2}).              \tag{3.3}
\]

Both actions give the same two free orbits of length 28.  The orbit bit is

\[
 \epsilon=\zeta^2/\xi^7\in\{+1,-1\};                   \tag{3.4}
\]

`xi^7` alone is not invariant.  Thus this chart has two geometric places,
each of ramification 28.

### 3.2 Residual pair, pole label, and Q/jump/max

The characteristic numerator/gcd sequence is

\[
 (\kappa;\beta_1,\beta_2)=(28;7,9),\qquad
 e_0,e_1,e_2=(28,7,1).
\]

It gives jump indices `(4,7)`, characteristic exponents `(1/4,9/28)`, and
the reviewed Q/jump/max values

\[
 \kappa_F:1\longrightarrow4\longrightarrow28,
 \qquad \bar\kappa:3\longrightarrow19.                  \tag{3.5}
\]

At the coarse cut `eta=x^(1/4)y`, the `f` residual is
`(eta^4-1)^14`.  Its exact Sigray tuple
`(D_f,deg p_f,nu,M,bar-kappa)` is

\[
 Q(F_0)=(8,56,4,14,3).
\]

Fix `zeta^4=1` and refine by
`eta=zeta+x^(-1/14)theta`.  With

\[
 K_\zeta=(4\zeta^3)^7,
\]

the paired residual top is

\[
 p_f=K_\zeta^2\theta^{14}-1,\qquad d_f=1,
 \qquad
 p_g=K_\zeta^3\theta^{21}-2\zeta^2,\qquad d_g=3/2.       \tag{3.6}
\]

At an `f` root, `theta=zeta*xi/4`, so

\[
 p_g(\theta)=\xi^7-2\zeta^2\ne0.                         \tag{3.7}
\]

Every one of the two places is therefore labelled a `g`-pole of order 42.
The refined tuple and paired degree are

\[
 Q(F_1)=(28,14,7,1,19),\qquad D_{g,F_1}=42.              \tag{3.8}
\]

This also tests the residual descent, rather than just denominators:

\[
 2-(9/28-1/4)14=1,\qquad
 3-(9/28-1/4)21=3/2.                                     \tag{3.9}
\]

The Sigray pole contribution is exactly

\[
 \Lambda_x=D_g\deg(p_f)/\nu=42\cdot14/7=84
          =2\text{ places}\cdot42.                      \tag{3.10}
\]

This is the requested Q/jump/max test: using the coarse value 4 at the
second cut would destroy the integer refined data and the pole accounting;
the reviewed maximum/jump value is 28.

## 4. The two fibres at `y=infinity`

Let `t=1/y` and `x=t^3X(t)`.  The exact fibre equation is

\[
 X^2(X-t)^{14}-1-a t^8-Xt^{11}=0.                        \tag{4.1}
\]

At `t=0`, its roots are the 16 simple values `c^16=1`.  Thus there are 16
unramified geometric places.  The difference between the `a=1` and `a=0`
solutions first appears as

\[
 X_1(t)-X_0(t)=\frac{c}{16}t^8+O(t^9),
 \qquad
 x_1(t)-x_0(t)=\frac{c}{16}t^{11}+O(t^{12}).              \tag{4.2}
\]

The exact paired `g` expression is

\[
 t^{12}g_\tau=
 X^3(X-t)^{21}+1+\tau X-2X^2t^{16}.                      \tag{4.3}
\]

Thus the pole residual on an `f` leaf is

\[
 c^{24}+1+\tau c=c^8+1+\tau c.                           \tag{4.4}
\]

For `tau=1` it is nonzero at every `c in mu_16`; all 16 places are poles of
order 12.  Together with the `x` chart, the sheet identity is

\[
 2\cdot28+16\cdot1=72=\deg f,                             \tag{4.5}
\]

so no infinity place is missing.  The baseline pole mass is

\[
 2\cdot42+16\cdot12=276.                                 \tag{4.6}
\]

The MacLane-style fingerprint is consequently: on the `x` side, the key
`z-1` followed by the two residual orbits with gcd chain `28,7,1`; on the
`y` side, 16 simple keys `X-c` with trivial ramification.  This phrase is a
fingerprint, not a claim that a general MacLane functor has been proved.

## 5. One matched-visible-data mutation

Change only

\[
 xy^{15}\longmapsto2xy^{15},\qquad g_1\longmapsto g_2.    \tag{5.1}
\]

Both coefficients are nonzero.  Therefore `g_1` and `g_2` have identical
support and Newton polygon `3S`.  They also have the same live GGV packet,
the same `(4,-1)` initial face `B^3`, the same `gamma=7` endpoint, the same
two fibre trees for `f=0,1`, the same 72-sheet inventory, and identical
`x=infinity` paired residuals through the pole cut.

But

\[
 \gcd(X^{16}-1,X^8+1+X)=1,
 \qquad
 \gcd(X^{16}-1,X^8+1+2X)=X+1.                            \tag{5.2}
\]

The unique cancellation is at `c=-1`.  Implicit differentiation of (4.1)
gives `X'(0)=7/8`; differentiating the bracket in (4.3) at this branch gives

\[
 21-22(7/8)=7/4\ne0.                                     \tag{5.3}
\]

Hence exactly one pole drops from order 12 to order 11.  All 18 geometric
places remain pole-labelled, but the total pole mass changes

\[
 276\longmapsto275.                                      \tag{5.4}
\]

This is a direct fidelity failure for any proposed transport whose input is
only the current GGV packet.  The mutation is detected immediately by the
paired `y`-chart residual polynomial.

## 6. Minimal sufficient typed packet

For this example, the following fields suffice to replay the transport:

1. the exact source pair and component orientation, not only the two support
   polygons;
2. the fibre value `a` and a stable fibre identifier;
3. the exact coordinate/key substitutions in **both** infinity charts;
4. at every cut, both residual polynomials `(p_f,p_g)`, all roots with
   multiplicities, and exact parent/child flag identifiers;
5. the deck action and its inverse, so presentations are grouped into
   geometric places rather than counted independently;
6. characteristic gcds, jump indices, and the reviewed Q/max `kappa` value;
7. evaluations of `p_g` on every `p_f` orbit, with pole label and order; and
8. an explicit inverse/source provenance map tying each residual coefficient
   back to the polynomial coefficient that produced it.

The existing fields

\[
 (A_0,A'_0),\ (\rho,\sigma,p,q),\ (m,n),\ S,c,
 \texttt{upper_dir},\texttt{rhs_exp},\ A_\gamma
\]

are enough for the edge skeleton, common-face valuation, denominator hint,
and support walls.  They do **not** recover the fibre coefficient in (3.2),
the residual in (4.4), the pole orders, or the pole mass.  No combination of
the listed lattice fields distinguishes (5.1).

## 7. Local certificate pullback versus G2-PSC

This prototype does furnish the **kind** of typed map needed for a
certificate-sized source pullback: equations (3.1) and (4.1), followed by
the explicit residual maps (3.6) and (4.3), send named source coefficients
to named receiver flags without guessing from visible corner data.  A local
compiler could carry only the flags touched by a small exact certificate and
verify its residual identities there.

It does not make the current V43G4 `t`-adic identity composable with K00.
That would still require an explicit row-chain map respecting the source
normalization, the fact that `t=-1/4` becomes a unit after `C6=1`, and the
target receiver types.  This example supplies no such map.

Most importantly, local certificate pullback is strictly weaker than
**G2-PSC**.  This control proves none of the global obligations:

- no theorem assigns such a packet to every reviewed complete GGV chain;
- no proof shows compatibility across every corner/Laurent transition;
- no global two-chart coverage or functoriality theorem is supplied;
- the explicit pair is not Keller; and
- one worked chain cannot establish the selected-counterexample bridge.

The right next theorem interface is therefore a fail-closed compiler

\[
 \text{exact selected source pair + fibre + GGV flag}
 \longrightarrow
 \text{paired residual/deck/Q/pole packet},
\]

with a proof that every consumed flag is covered.  Only after that local
interface works uniformly should a G2-PSC/global coverage claim be stated.

## 8. Replay and exact scope

Artifacts:

- `cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/verify.py`
- `cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/RESULT.json`
- this report

Replay from repository root:

```text
python3 cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/verify.py
```

The replay is standard-library-only and desk scale.  It verifies the source
hashes, imports the live `8_28` object, expands the sparse polynomials exactly,
checks both charts, computes the deck orbits in both orientations, performs
the exact cyclotomic gcd mutation test, and compares its result to the frozen
JSON object.

Final status: **PASS for this one non-Keller control and one mutation.**
There is no promotion of Conjecture T, G2-PSC, or any JC2 theorem here.

