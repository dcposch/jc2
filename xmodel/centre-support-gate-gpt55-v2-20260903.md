# Centre-support gate, GPT-5.5 v2, 2026-09-03

## Verdict

**CONFIRMED, with a proof correction.** The ungated `C_FULL_TREE` Prop. 5.6
zero-chain kill is promotable for **still-centred all-zero major chains**:
after the p.190 affine removal, such a chain has
\(\sigma_1=\pi t^{\delta_1}\), so Prop. 5.6 applies to every all-(11) major
path reaching \(D_1\). [DERIVED]

The charged one-line proof must not be quoted as "the current p.201 increment
action alone moves all non-integer exponents" when \(L>1\). On p.201 the
increment action fixes \(k((\bar t^{A_{r-1}}))=k((t^{1/L}))\), so its fixed
exponents are the old \(1/L\)-lattice, not just integers. The gap closes
because, on an all-zero still-centred chain, the full/ancestor Puiseux Galois
over the original centred chart fixes every previous zero coefficient and
moves every non-integer centre term. [DERIVED]

`OPEN[NONZERO-PARENT-TWIST]` remains correctly separated: a nonzero parent
factor may carry Galois-legal twisting coefficients as a configuration, and
that is not used by Prop. 5.6. [OPEN]

No new exit-price assertion is made; FALLACY-v2 `charge_basis` is inapplicable.

## Frozen Inputs

The manifest was generated mechanically from
`xmodel/centre-support-gate-gpt55-v2-20260903.run.v2` with `awk` using the
`charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines, then
checked with `sha256sum -c`. All ten frozen inputs under
`/tmp/jc2-lane.cNJIzk/inputs` returned `OK`. [MEASURED]

The generated manifest is
`box/centre-gate-20260903/input-manifest.sha256`. [ARTIFACT]

## Page Images

Rendered from the frozen Moh PDF with `pdftoppm -r 200`; printed page
\(p\) equals PDF page \(p-139\). [MEASURED]

Requested images:

```text
box/centre-gate-20260903/moh_p147.png
box/centre-gate-20260903/moh_p148.png
box/centre-gate-20260903/moh_p149.png
box/centre-gate-20260903/moh_p150.png
box/centre-gate-20260903/moh_p183.png
box/centre-gate-20260903/moh_p184.png
box/centre-gate-20260903/moh_p189.png
box/centre-gate-20260903/moh_p190.png
box/centre-gate-20260903/moh_p200.png
box/centre-gate-20260903/moh_p201.png
```

Added because the requested citations straddle page breaks:
`moh_p145.png` for Lemma 1.1 and `moh_p188.png` for the statement of
Prop. 5.6. [ARTIFACT]

## Source Checks

**Def. 1.3 / radii.** Page 146 defines a \(\pi\)-root as
\(\sigma=\sum_{j<\delta}a_jt^j+\pi t^\delta\) with \(a_j\in k\); page 147
states that this is the general point of the disc of metric radius
\(2^{-\delta}\) centered at the displayed sum. Therefore larger logarithmic
radius means smaller metric disc. If two centres first differ at exponent
\(e\), their metric distance is \(2^{-e}\); if \(e<\delta_{r-1}\), that
distance is larger than the radius \(2^{-\delta_{r-1}}\). They cannot both
lie in one \(D_{r-1}\). [PROVED-IN-SOURCE / DERIVED]

**Lemma 1.1.** Page 145 states the criterion: a disc \(D\) is one of the
associated tree discs iff it contains a root and contains two roots whose
distance equals the radius of \(D\). This matches the preceding distance
calculation and rules out inserting a moved centre term at a logarithmic
distance strictly below the next declared radius. [PROVED-IN-SOURCE]

**Prop. 5.3 packet.** Page 180 defines \(D_{r-1}\) for the chosen factor
\(\pi-C_r\) as the minimal disc containing all roots with
\(\operatorname{ord}(\tau-\tau_i)>\delta_r\); the proof on pp.180-183 rules
out an intermediate split before the computed \(\delta_{r-1}\). Thus a
Galois orbit with the same \(C_r=0\) but first separation
\(e\in(\delta_r,\delta_{r-1})\) contradicts the definition of that zero
packet, independently of the multiplicity of the factor. [PROVED-IN-SOURCE /
DERIVED]

**Multiplicity of the zero factor.** The proof does **not** need \(\pi=0\) to
be a simple root of \(p\). If the zero factor has multiplicity \(b\ge2\), it
is still one root value, hence one fixed parent packet. A moved lower centre
term would split that same packet at exponent \(e<\delta_{r-1}\), making the
minimal packet radius \(e\), not \(\delta_{r-1}\). [DERIVED]

**p.184 argument.** Page 184 first uses \(t^{1/\ell}\mapsto\omega t^{1/\ell}\)
to say that a non-integer exponent produces different roots. In the later
\(i>1\) paragraph Moh chooses a nonzero factor \(\pi-a\), and the nonzero
root need not be fixed. For the zero-chain lemma the specialization is
stronger: \(0\) is fixed by every multiplicative action on the \(\pi\)-line,
so conjugates remain in the zero parent packet. [PROVED-IN-SOURCE / DERIVED]

**p.190 removal.** Page 190 removes the \(t^{-1}\) and \(t^0\) centre terms
by \(x\mapsto x,\ y\mapsto y-ax-b\). Since all bottom radii in this search
are \(<1\) and the top radius is \(-1\), the only integral centre exponents
that can survive below \(\delta_1\) are exactly those affine terms. [PROVED-IN-
SOURCE / DERIVED]

**p.201 action and \(L\).** Page 201(8) defines \(L\), \(A_{r-1}\), and
\((\bar t)^{L A_{r-1}}=t\); the printed automorphism is over
\(k((\bar t^{A_{r-1}}))\), i.e. over the old field \(k((t^{1/L}))\). Therefore
current-increment fixed exponents are the old lattice. For a still-centred
all-zero chain, however, every ancestor zero coefficient is \(0\), so the
full Puiseux Galois over the original centred chart still fixes the branch
labels and moves any non-integer term. Hence the proof works for general
\(L\); it does not require \(L=1\). [PROVED-IN-SOURCE / DERIVED]

## Lemma

**LEMMA[ZERO-FACTOR-CENTRE].** Let \(D_s\supset\cdots\supset D_r\) be a major
tower in a chart centred at \(0\), and suppose the chosen factor of the
Prop. 4.6 polynomial at \(D_r\) is \(\pi\). In the unique zero packet used to
construct \(D_{r-1}\), every non-integer centre coefficient at an exponent
\(e\in(\delta_r,\delta_{r-1})\) vanishes. After the p.190 affine removal,
iteration along an all-zero still-centred chain gives
\(\sigma_1=\pi t^{\delta_1}\). [DERIVED]

Proof sketch: take a nonzero term \(a t^e\). A Puiseux Galois element fixing
the previous zero coefficients and moving \(t^e\) gives another root in the
same zero parent packet, with first separation \(e\). Since \(e<\delta_{r-1}\),
the two conjugates cannot both belong to the single minimal disc
\(D_{r-1}\) of logarithmic radius \(\delta_{r-1}\). Thus \(a=0\). Integer
terms are exactly the affine terms already removed at p.190. [DERIVED]

Scope: all still-centred zero chains, including forced zero siblings in the
whole-tree recursion. Nonzero parent factors are excluded from the lemma's
claim. [SCOPE]

## Cheapest Test Replay

Executed from copied frozen inputs in `box/centre-gate-20260903/`. [MEASURED]

`python3 box/centre-gate-20260903/centre_support_test.py`:

```text
(75,50; M=55,73; V2=3,V3=4)
delta = (-1, 1/5, 1/2)
L1=5 A1=2; L2=1 A2=5
deg g_sigma=9; deg T_sigma=6
free in (delta2,delta1) = {2/5}
40 checks, 0 failures
```

The three \(D_1\) tests do not cut \(a_{2/5}\). Prop. 1.2 makes the leading
root product independent of a shared centre coefficient; the \(r=1\) ODE is
a cylinder in \(a_{2/5}\); and the \(A_1=2\) increment fixes \(t^{2/5}\).
[MEASURED]

The parent action \(A_2=5\) kills \(a_{2/5}\) only on the zero child:
with \(C_2=0\), the orbit polynomial is \(y^5-a^5u^{10}\), so \(a\ne0\)
would create five centres separated at logarithmic distance \(2/5<1/2\).
For \(b=5,10,15,20\) this still inserts the same forbidden intermediate
split; multiplicity \(b\) is irrelevant. [MEASURED / DERIVED]

For \(C_2\ne0\), the resultant of
\(y-CWu-\lambda C^2W^2u^2\) against \(W^5-1\) is a monic degree-5 polynomial
in \(\mathbb Q[C,\lambda,y,u]\). Thus \(\lambda\ne0\) is Galois-legal as a
configuration; this is `OPEN[NONZERO-PARENT-TWIST]`, not a Prop. 5.6 input.
[MEASURED / OPEN]

Controls: `(64,48; V2=3,V3=3)` has free `{1/2}` and the zero child is split
by an \(A_2=4\) orbit of size 2; `(99,66; V2=8,V3=8)` has empty free set, so
Prop. 5.6 applies to zero children without the lemma. [MEASURED / DERIVED]

## Screen Replay

`python3 box/centre-gate-20260903/rerun_screens.py` reproduced the charged
gate table. [MEASURED]

```text
input rows: 658, printed: 6
PARTITION_PASS       330 rows / 52 classes
GATED_PASS           204 rows / 21 classes
UNGATED_PASS          55 rows / 11 classes
restored 204->55? True
```

Full replay table:

```text
PARTITION       348 / 52
PARTITION_ODE   347 / 52
PARTITION_PASS  330 / 52
GATED           216 / 21
GATED_ODE       215 / 21
GATED_PASS      204 / 21
UNGATED          60 / 12
UNGATED_ODE      58 / 12
UNGATED_PASS     55 / 11
```

`python3 box/centre-gate-20260903/opus5_probe.py` also reproduced:

```text
TREE             60 / 12
TREE_ODE         58 / 12
TREE_ODE_PASS    55 / 11
TREE_REC         23 / 7
TREE_REC_ODE     20 / 7
TREE_REC_PASS    20 / 7
```

Thus the gap-free/gapped split collapses as charged: accepting the lemma
restores `C_FULL_TREE` and moves the \(n\le100\) residue from 204 rows /
21 classes to 55 rows / 11 classes. [MEASURED / DERIVED]

## Typed Claims

```text
Hash gate                              MEASURED: all ten frozen inputs OK.
Page rendering                         MEASURED: Moh pages named by print page.
Def.1.3 centre support                 PROVED-IN-SOURCE: unrestricted sum below δ.
Lemma 1.1 radius convention             PROVED-IN-SOURCE: exact metric criterion.
p.201 current action                    PROVED-IN-SOURCE: over k((t^(1/L))).
Current action fixed set                DERIVED: old 1/L lattice, not only Z.
General-L zero-chain repair             DERIVED: use full/ancestor Galois.
Zero multiplicity b>=2                  DERIVED: no simple-root hypothesis needed.
p.184 zero specialization               DERIVED: π=0 fixed, conjugates stay zero.
p.190 affine removal                    PROVED-IN-SOURCE: removes -1 and 0 terms.
LEMMA[ZERO-FACTOR-CENTRE]               DERIVED: valid for still-centred zero chains.
Cheapest D1 tests                       MEASURED: do not cut a_{2/5}.
Parent A2 zero-child kill               DERIVED/MEASURED: cuts a_{2/5}.
Nonzero-parent twist                    OPEN: configuration-legal, Keller undecided.
UNGATED C_FULL_TREE                     CONFIRMED: promotable for all-zero chains.
204 -> 55, 21 -> 11                     MEASURED: frozen replay.
OPEN[NONZERO-PARENT-TWIST] separation   CONFIRMED: not used by Prop. 5.6.
```

## FALLACY-v2

No cv flag/place/series identification. No per-ray exit charge. No
`REPRESENTATIVE`/`FULL_ACTUAL_EXIT` claim. No pole identity. The 55-row count
is a necessary-screen residue, not an attainment theorem. `sat()` unused.
Variable maps for resultants were declared in
\(\mathbb Q[C,\lambda,y,u]\) and \(\mathbb Q[a,y,u]\), with the image check
being absence of cyclotomic symbols after eliminating \(W^A-1\). Prime marks
unused. No Statement 8.5 use. Target/arrival indices not used.

<!-- BODY-END -->
