# HOMCOVER-DISCRIMINATOR — torsion at the constrained N=4 cabled place

Lane: `HOMCOVER-DISCRIMINATOR`. Date: 2026-09-02. Agent: grok-4.6.
Desk-scale exact integer homology. Instrument: `box/cover_h1.py`.
No Groebner basis, no SIROCCO rerun, no CAS decision procedure.

## 0. Custody, hashes, method

The two charged frozen copies were hashed with `shasum -a 256` **before
any was read**. Both match the charge exactly:

```text
dcd40a425b2a2782deebec3f01c3b6859a8aa8d46b3e60639f9865a807d5ddba  ideation-20260902T0022Z-opus5.md
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  rep-96-inner-opus5-20260901.md
```

Below: **ID** = the ideation (Card B), **REP96** = REP-96-INNER.
Campaign files consumed on disk and cited by file and section, not
re-hashed as primary: `box/cover_h1.py` (instrument, including the
load-bearing lift-closed / transport convention); `box/bmfact_enum.py`
(class list, Hurwitz, BLOCK reconstruction); `FALLACY-v2.md`;
`pi1s4-close-residual-r2-opus5-20260831.md` Lemma 3.3 (cabling word);
`box/bmfact_962.sage` conventions (B1)–(B7), read only to name the
missing JSON. No charged file was edited. `jc2-lean` was not inspected.

**Instrument hashes, as run:**

```text
dfb90ce32f589aae00ce7f2d3188114bbf27396120a8da3d8e67c0145b5177b2  box/cover_h1.py
b51813adcf7a407f97c486995f7f99ba73f616d0f04594506a069757bdbf832b  box/bmfact_enum.py
```

**What was run.** One Python driver (`/tmp/homcover_disc.py`, not
installed in `box/`). Every number labelled MEASURED came out of that
run against the hashed instrument. Four instrument controls were
asserted before any discriminator number was read; the closed-braid
presentation of the trefoil was added as a fifth, because that is the
same 2-complex shape the local model uses.

**What was not run.** Sage, SIROCCO, the banked `bmfact_962.json` (not
present on this host; hunt in §6). No representation of
`pi_1(C^2 \ D)` is claimed. No exit price.

No `charge_basis` line: this report asserts no new exit price.

## 1. Verdict

**Typed: `ALL-TORSION` on the local group of the cabled place.**

The local group used for Card B is **not** the trefoil group `B_3` and
**not** the germ torus-knot group `T(3,25)`. It is the closed-braid
group of the affine braid at infinity

```text
G_infty  =  < xi_1, ..., xi_9  |  xi_j = phi_{rho_inf}(xi_j),  j=1..9 >
rho_inf  =  C_3(delta_3^2) · iota ,   iota = (delta_3^{k_*}, 1, 1),
k_* = -10 ,
```

in the **BLOCK** reading of REP96 §5 / CABLE-3 (adjacent blocks
`(1,2,3),(4,5,6),(7,8,9)`; orientation as written). This is the group
of the closed 9-braid of the tubular factorization — the object ID §5
names as the `(9,6)` place with Puiseux slope `3/2`, a trefoil cable.
The six classes / 144 tuples **are** homomorphisms `G_infty -> S_4`
(meridians to transpositions, image `S_4`, `Pi` a transposition,
GATE-3). MEASURED, every one of them:

```text
H_1(cover)  =  Z^3 (+) Z/2     on all 6 classes, all 144 tuples.
```

Relators evaluate to `1` in `S_4` on all 144. The `k=1` abelianization
of `G_infty` is `Z` (one component: a knot). Conjugacy in `S_4` does
not change `H_1`. Lift-closed as-written (`d_1 o d_2 = 0`).

**Card B outcomes, as charged:**

* `ALL-TORSION` → **fund the transfer lemma.** Every campaign-constrained
  local representation at this place carries torsion in `H^{ab}` of the
  induced cover. The candidate all-degree obstruction still has a live
  local source. Report: **loud, scoped.** This is a necessary-condition
  source at the place, not a theorem that the torsion survives in
  `pi_1(C^2 \ A)`, and not a kill of `(9,6,2)`.
* The stop condition (a torsion-free constrained local rep) **did not
  fire.** The razor is not degraded to a filter on this local model.

`OPEN[HOM-COVER-TRANSFER]` remains the load-bearing step. Passing
HOM-COVER is not existence (ID §3.2, carrier/attainment); failing it
locally is not a global kill.

## 2. Instrument controls, MEASURED

`python3 box/cover_h1.py`, then the same code path on the closed-braid
2-complex. All asserted before the discriminator:

```text
two transverse lines, 2-sheeted              H_1 = Z^2           PASS
trivial rho on Z^2, k=1                      H_1 = Z^2           PASS
cuspidal cubic = B_3, base                   H_1 = Z^1           PASS
cuspidal cubic, cyclic 2-fold                H_1 = Z (+) Z/3     PASS
closed braid of sigma_1^3 in B_2, base       H_1 = Z^1           PASS
closed braid of sigma_1^3, cyclic 2-fold     H_1 = Z (+) Z/3     PASS
```

The last two are the same nonzero answer as the fourth, obtained from
the presentation shape used on `G_infty`. A palindrome cannot detect
the Artin/Hurwitz dual (next paragraph); the `B_3` generator tests in
§3 can.

**Convention, labelled, not inferred.** Left Hurwitz on tuples applies
a Sage Tietze word rightmost letter first (REP96 §2, `bmfact_enum.py`).
The free-group automorphism whose *evaluation* equals that Hurwitz
action applies the same word **leftmost** letter first (the two actions
are dual). Relators are `xi_j^{-1} phi(xi_j)` in that dual. Check,
MEASURED: Artin-eval equals Hurwitz on all 144 reconstructed 9-tuples.
`cover_h1.py` is the SOURCE-GATE lift-closed instrument: `rho` as
written closed on every homomorphism below (`to_transport_convention`
was not needed). The two conventions give different covers in general;
the choice is declared, not silent.

**Analogue census, reproduced.** ID §7's unconstrained `B_3 -> S_4`
count is a control of the enumerator, not of Card B:

```text
B_3 -> S_4 :  96 homs, 54 transitive;  30 with torsion (56%)
              H_1 = Z^2  x24 ,  Z (+) Z/2  x24 ,  Z (+) Z/3  x6
```

Exact match of ID §7. The instrument-plus-enumerator is calibrated
against a known nonzero torsion answer *and* against a known census.

## 3. The local model, and three objects that are not it

Flag / place / series are kept apart. Four groups appear in this lane.
They are not identified.

**(L0) `G_infty` — the cabled place, primary.** Closed-braid group of
`rho_inf` as above. Cabling Tietze recovered from Lemma 3.3: the `g=2`
word is `C_2(sigma_1) = sigma_2 sigma_1 sigma_3 sigma_2 = [2,1,3,2]`,
and `g=3` is the same “push `g` strands across in turn.” MEASURED: that
word Hurwitz-fixes all 144 BLOCK 9-tuples, matching
`bmfact_enum.rho_inf_block_act`. Exponent length 56. This is the group
the six classes represent.

**(L1) Outer `B_3` — reduced-shape companion, not the place.** Block
products `(X,Y)` satisfy the braid relation, so they define
`B_3 -> S_4`, `sigma_1 |-> X`, `sigma_2 |-> Y`. These generators are
**block products of three meridians**, not meridians of `D`. ID's
`B_3 -> S_4` census treated `B_3` as the trefoil knot group (meridians
as generators). The two `B_3`'s are different maps. Not identified
with (L0).

**(L2) Inner tube — pattern torus braid, not the place.** Closure of
`delta_3^{k_*}` in `B_3`. GATE-3 is `T_1 = delta_3^{k_*} · c_h(T_1)`,
not `T_1 = delta_3^{k_*} · T_1`. For `noncst-T`, REP96 §2 gives
`h = e`, so the untwisted inner braid *is* a relation; for `noncst-4c`,
`h` is a double transposition and the untwisted closed braid is **not**
a homomorphism. Not identified with (L0).

**(L3) Germ `T(3,25)` — the germ of `Dbar` at `P_inf`, not the affine
cable.** Characteristic pair `(3; 25)`, group `<x,y | x^3 = y^{25}>`.
A meridian is `x^{-8} y` (`3*(-8)+25*1=1`). The affine 9-braid
`rho_inf` has exponent sum `16 = 2 delta_aff + d - 1`, which is the
affine ramification ledger, not the Milnor braid of the germ. The
representation spaces differ (§5), so the groups are not used as the
same object. Typed `OPEN[HOMCOVER-GINFTY-VS-T325]`, not filled by
saying both are “the place at infinity.”

**TB-GERM is not a constraint here.** THEOREM TB-GERM is a family-3
`(8,6)` statement, `beta_1 = 8 + 3 kappa` with `kappa` odd. At
`(9,6,2)`, `beta_1 = 25` and `(25-8)/3` is not an integer. Family-2
chart orders are `(a,d)=(3,9)`, not `(g, 4g)`. Not applicable; not
used as a filter; not replaced by analogy. The constrained set is
exactly REP96 §5's six classes.

## 4. What the six classes force locally

REP96 §5, hard-coded in `bmfact_enum.py`, six classes, each a
24-element `S_4`-conjugacy orbit, 144 tuples:

```text
noncst-T :  X=(3 4) Y=(2 3) Pi=(2 4) ,
            T_1 = ((1 3),(1 4),(1 3))  or  ((1 4),(1 3),(1 4))
noncst-4c:  X=(1 2 3 4) Y=(1 2 4 3) Pi=(3 4) ,
            T_1 = ((1 2),(2 3),(3 4)), ((2 3),(3 4),(1 4)),
                  ((3 4),(1 4),(1 2)), ((1 4),(1 2),(2 3))
```

Forced, and used:

* Transitivity of the **nine** meridians: image `S_4` on every class
  (REP96 (3.2); graph of the nine transpositions is connected).
* `Pi = XYX` is a transposition on every `(9,6,2)` class (parity fork,
  `sgn(Pi)=(-1)^9=-1`; never in `V_4`).
* GATE-3 at `k_* = -10` (`= 2 mod 4`): the class list *is* the live
  GATE-3 residual. `T_2, T_3` reconstructed by
  `iota = (delta_3^{k_*}, 1, 1)` (`OPEN[BMFACT-IOTA-SPLIT]` not
  resolved; this is the split `bmfact_enum.py` declares).
* BLOCK embedding: adjacent. `OPEN[BMFACT-TUBE-EMBEDDING]` and
  `OPEN[BMFACT-STRAND-VS-BLOCK]` are not resolved.

Forced, and **not** a local transitivity of the outer `B_3`:

* `noncst-T`: `<X,Y> = S_3` on `{2,3,4}`, not transitive on 4 letters.
  The fourth letter is supplied by the inner meridians of `T_1`.
* `noncst-4c`: `<X,Y>` is transitive on 4 letters.

That split is why a `B_3`-only analogue (L1) cannot decide Card B:
half the constrained classes are not even `S_4`-valued on the outer
`B_3`.

## 5. Razor, MEASURED

### 5.1 Primary: `G_infty` (L0)

```text
k=1 (group abelianization)     H_1 = Z^1                         PASS
class noncst-T-a, 24 conjugates H_1 = Z^3 (+) Z/2
class noncst-T-b, 24 conjugates H_1 = Z^3 (+) Z/2
class noncst-4c-0..3, 24 each   H_1 = Z^3 (+) Z/2
all 144                         144 / 144 equal to Z^3 (+) Z/2
relators hold in S_4            144 / 144
lift-closed                     as-written
```

**ALL-TORSION.** The cabling is what supplies the torsion on
`noncst-T`: the same outer datum, run as `B_3` on its 3-set, is
torsion-free (§5.2). After cabling, `Z/2` appears uniformly.

Free rank 3 is reported as measured, not interpreted as a component
count of a plane-curve complement. The RANK test of ID §3.2
(`rank = r(E)`) lives on the ACS-1 covering of `C^2 \ A`, not on a
cover of `G_infty`. Applying it here would be a flag/place/series
identification. Not applied.

### 5.2 Outer `B_3` (L1), analogue only

Campaign constraints pulled back to `(X,Y)`:

```text
unconstrained transitive B_3->S_4     54;  24 torsion-free (Z^2)
among those, Pi a transposition       24;  ALL 4cyc+4cyc;  H_1 = Z (+) Z/2
                                       (ALL-TORSION on this cut)
six-class outer, noncst-4c            transitive;  H_1 = Z (+) Z/2
six-class outer, noncst-T             not transitive on 4;
                                       H_1 on the 3-support = Z^2  (FREE)
```

If Card B had named `B_3` as the local model, the verdict would be
`SOME-TORSION-FREE`, with `noncst-T` the countermodel, and the attack
would degrade to a filter. That is **not** the local model of the
cabled place. It is recorded as a permanent scope limit on the
*analogue*, matching ID §5's own warning that 44% of unconstrained
degree-4 `B_3`-reps are torsion-free. The cable is what closes that
gap on the constrained set.

### 5.3 Inner tube (L2)

`k=1` of the closed `delta_3^{k_*}` is `Z`. On the six classes:

```text
noncst-T   T_1 is delta_3^{k_*}-fixed (h=e);
           not transitive on 4;  H_1 on the 3-support = Z^2 (+) Z/5
noncst-4c  T_1 is NOT delta_3^{k_*}-fixed (GATE-3 twists by c_h);
           not a homomorphism of this group; razor not run
```

The classes that *are* homomorphisms carry torsion. Not used as the
Card B model.

### 5.4 Germ `T(3,25)` (L3)

```text
homs T(3,25) -> S_4                         24
of those, meridian a transposition           6  (x=y a transposition)
of those, transitive on 4 letters            0
C_2 cyclic (same transposition, k=2)         H_1 = Z^1   (FREE)
```

`Delta_{T(3,25)}(-1) = 1` (`p,q` both odd): the torsion-free `C_2`
answer is the textbook value, a positive control of the 2-generator
enumerator. There is **no** campaign-constrained *transitive* `N=4`
representation of this germ group. Empty is not `ALL-TORSION` and not
a countermodel; it is a different object's representation space.
`OPEN[HOMCOVER-GINFTY-VS-T325]`.

Control of the same enumerator on `T(2,3)`: 96 homs, matching the
`B_3` count; meridians-to-transpositions yields 30 homs, none
transitive on 4 — meridians of the trefoil as a torus knot are not
the generators that give ID's 54 transitive `S_4`-reps. Another
flag/place split, not a bug.

## 6. Global ZvK, BLOCK reading, JSON

The charge: run the razor on the global banked `(9,6,2)` ZvK
presentation for each of the six classes **if** that presentation is
derivable from the banked SIROCCO JSON with cycle types + the BLOCK
reading; label the convention; do not resolve
`OPEN[BMFACT-STRAND-VS-BLOCK]`.

**JSON is not on this host.** Hunt, all absent:
`~/bmfact/bmfact-962-out/bmfact_962.json` and four obvious copies
under the repo and `$HOME`. Cycle types banked in LIVE STATE / the
Sage script's census (eight tangency transpositions + one node-fibre
identity of exponent 8) plus BLOCK do **not** determine the eight
tangency conjugators or the four node pairs. Without conjugators the
individual `(T)` / `(N_1)` relators are not a presentation.

What *is* derivable without the JSON is the **product** relation
`rho_inf`, from CABLE-3 and BLOCK. That is `G_infty`, already run.
It is the product of the global ZvK relations, not the global group.

**Convention, labelled:**

```text
reading        BLOCK, adjacent blocks (1,2,3),(4,5,6),(7,8,9)
iota split     (delta_3^{k_*}, 1, 1), k_* = -10
orientation    CABLE-3 as written (not inverse)
Artin dual     leftmost Tietze on words, matching left Hurwitz
cover_h1       as-written, lift-closed
```

`OPEN[BMFACT-STRAND-VS-BLOCK]` is not touched. `OPEN[BMFACT-ORIENTATION]`
is not touched. Typed `OPEN[HOMCOVER-GLOBAL-ZVK-JSON]`: the nine-factor
presentation is not derivable here. A successor with the JSON in hand
may form the nine local relators, *then* ask which of the 144 (if any)
are homomorphisms of the full group, *then* run the razor on those.
Running `cover_h1` on a non-homomorphism is undefined; the instrument
now fail-closes in that case.

## 7. What this funds, and what it does not

Card B's cheapest discriminator has returned `ALL-TORSION` on the
local group the six classes actually represent. That is the gate ID
named for funding the transfer lemma.

**Funded, as a candidate, not as a theorem.** The transfer step is:
a character supporting a campaign-constrained `rho` meets a root of
the local Alexander module of the cabled place, and that torsion
survives in `H^{ab}` of the ACS-1 covering of `C^2 \ A`. Nothing
here proves survival. Characteristic-variety input is still not
banked (ID §9 Card B: primary-source custody check owed). The
measured `Z/2` is a specific torsion, not a citation of Libgober.

**Not a kill of `(9,6,2)`.** The six classes are `rho_inf`-fixed, not
full-factorisation-fixed. Global `pi_1(C^2 \ D)` is a quotient of
`G_infty` by the affine tangency and node relations; those extra
relators can kill the `Z/2` or kill the representation. HOM-COVER on
the ACS-1 covering remains Card A's consumer of BMFACT survivors.

**Not JC2 at every degree.** An all-degree theorem needs the transfer
at a general cabled place, not one MEASURED `N=4` node. The node is
why the lemma is worth writing.

**Permanent analogue-scope limit, recorded:** unconstrained (and
`noncst-T` outer) `B_3 -> S_4` admits torsion-free covers. Any
statement “a trefoil at infinity forces torsion in every degree-4
cover” is false. The true statement the numbers permit is narrower:
*the constrained `G_infty`-covers of this cable all carry `Z/2`.*

## 8. FALLACY-v2 audit

* **Flag/place/series.** Four groups (L0–L3) are named and not
  identified. Affine `rho_inf` (exponent 16, 9 strands) is not the
  germ Milnor braid. Block products are not meridians. The RANK
  test is not applied to a cover of `G_infty`.
* **Carrier/attainment.** `ALL-TORSION` is a necessary-condition
  source. The 144 tuples are group-theoretic data, not a Keller
  map. `REPRESENTATIVE` is not `FULL_ACTUAL_EXIT`.
* **Floor/attainment.** `H_1 = Z^3 (+) Z/2` is an exact computed
  value of a specific 2-complex, not a bound. Free rank 3 is not
  converted into a component count.
* **Per-ray / exit-set.** No exit price. No `charge_basis` line.
* **Pole/interior.** Cabling and `k_*` are taken from the tube
  regime of REP96 §2, already justified there; not re-derived from
  a pole identity.
* **Variable / ring map.** Not in play (no ideal). The permutation
  convention is declared in §2.
* **`sat()` / raw remainder.** Not in play.
* **Not filled by cap or analogy.** TB-GERM was not transported.
  `T(3,25)` was not used as `G_infty`. `B_3` was not used as the
  Card B model. Global nine-factor ZvK was not invented from cycle
  types. Where the JSON is absent the verdict is typed `OPEN`.

## 9. Typed verdict block

```text
LANE            HOMCOVER-DISCRIMINATOR
INSTRUMENT      box/cover_h1.py  4/4 controls PASS, plus closed-braid
                trefoil Z (+) Z/3 PASS.  B_3->S_4 census 54/30 MATCHES
                ID §7.  Lift-closed as-written.
LOCAL MODEL     G_infty = closed-braid group of rho_inf = C_3(delta_3^2)·iota
                BLOCK adjacent, iota=(delta_3^{-10},1,1).  k=1 gives Z.
CONSTRAINTS     transitivity of the nine meridians; Pi a transposition;
                GATE-3 at k_*=-10; the six classes / 144 tuples.
                TB-GERM: NOT APPLICABLE (family 3 / (8,6); not used).
MEASURED        144/144  H_1 = Z^3 (+) Z/2
VERDICT         ALL-TORSION on the cabled-place local model.
                Transfer lemma FUNDED as a candidate.
                Stop condition (torsion-free constrained local rep)
                DID NOT FIRE.

NOT CLAIMED     kill of (9,6,2); existence of phi; JC2 at every degree;
                transfer; RANK test on G_infty; T(3,25) = G_infty.
GLOBAL ZvK      OPEN[HOMCOVER-GLOBAL-ZVK-JSON]  (SIROCCO JSON absent).
                Product relation run as G_infty.  STRAND-VS-BLOCK not
                resolved.
OPENS           OPEN[HOM-COVER-TRANSFER]  (still the load-bearing step)
                OPEN[HOMCOVER-GLOBAL-ZVK-JSON]
                OPEN[HOMCOVER-GINFTY-VS-T325]
SCOPE LIMIT     B_3 analogue, noncst-T outer: H_1 = Z^2 torsion-free
                on the 3-support.  Permanent limit on "trefoil => torsion",
                not on G_infty.
DEVIATIONS      Size paced 12-20KB.  Driver left in /tmp, not box/.
                cover_h1.py consumed with the SOURCE-GATE lift-closed
                patch (hashed above); controls re-run against that file.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18959`.
- Body SHA-256:
  `5558f3eea731c6edf11845a7f16ba67867d2c68ea90920153d0f6c5ef1d9256e`.
- Frozen basis: `cbe4be8530aac3038ce8ce93be1b8262de128ddf`.
