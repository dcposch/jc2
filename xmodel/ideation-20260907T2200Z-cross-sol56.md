# Adversarial cross-pollination — 2200Z — Sol56

## Custody and corrected compatibility map

I read all four blind reports completely and only from
`/tmp/jc2-lane.hWLcm4/inputs`, plus the charged deduplication, root facts and
frozen references. All 16 files match `cross-input-pins.json` (SHA256
`c148f493…fcde7`). The collection is `jc2.blind-collection/v1`, says no peer
body was read before collection, verifies root's blind transaction, and records
the three external reports `BODY_SEALED/CLEAN/DONE`, with producer/model PIDs
absent. Its collected/not-found unit view is not reinterpreted as fresh exit
evidence. No live ledger, Volta body, low-alpha body, primary source, or old
workspace was read.

I consume the low-alpha delta only as root's adjudication: claims 1--6 passed
by whole-proof reading plus an independent truncated-degree-three control, but
the two advertised toys overclaim and supply no stronger arrow. Their body is
uncharged here.

The collector's X2 needs an explicit split. The three pure-center consumers
share exactly this source: over a characteristic-zero residue field `K`, in
`A=K[g,p]/(V)`, `V=g^3+p^3-3p`, the accepted first contact is `F_j=RC`,
`R=p^2V`, with nonzero regular even `C`, `V` not dividing `C`, the stated
degree/weight/fixed-face conditions, and `ord_O(C)>=4`. They then diverge:

- **X2q — KNOWN conditional:** the source must produce regular odd `D` and
  scalars `a,b` with `D^2=C(aC+b)`, `a!=0`; only then does the accepted affine-
  unit parity lemma apply, with its separate `b=0` branch.
- **X2c — NEW conditional consumer:** the source must instead produce
  `D^2=C(C^2+aC+b)`, with regular `C,D` and
  `b(a^2-4b)!=0`. Then the target cubic is smooth genus one; `C` has target
  order two at `(0,0)`, so `ord_O(C)>=4` ramifies the nonconstant map from the
  smooth genus-one `E`, contradicting characteristic-zero unramifiedness.
  Here `ord_O(C)>=4` follows from the actual admissible slots
  (`ord_O(g)=1, ord_O(p)=3`), not a gate label. Singular targets remain; the
  existing `D^2=C^3/9` collision is precisely such a countercontrol.
- **X3 — NEW, conditional:** it needs the different source arrow
  `9D^2-C^3-RW in K[R]` through order `3j`, with polynomial/regular odd `D`;
  reduction on `V` and evaluation at `O` then exhibit the square root.

The remaining checksum classification is: X1 exact rerun **DUPLICATE/SPENT**;
X4 literal unguarded grading **NEW**, but a Laurent-chart version is
**SCOPE-CONFLICT**; Furter's X5 core is now **KNOWN**, its marked-axis
zero-multiplier screen is a **NEW scoped countercontrol**, and any present
Keller/route attachment is **SCOPE-CONFLICT/GAP**; X6 uniform receiver descent
is **KNOWN**. The frozen history contains prior initial-ideal/tropical work but
no saturation-preserving X4 grading, and no prior X3 square-class test.

## Strongest attacks and consequences

**Strongest non-originated proposal: Fable's X3.** The first missing arrow is
not divisor computation: it is the complete moving-reference equations from
orders `2j+1` through `3j` producing the displayed cubic with a *regular
polynomial* odd `D`. Root's scoped confirmation of six uncharged low-alpha
statements does not supply that arrow. Moreover the frozen collision
`C=r^2-RL`, `D=rC/3` is an actual source-compatible six-jet and passes X3:
modulo `V`, `C=r^2`, hence `C/p^2=(r/p)^2=L^4`. Therefore “proper codimension”
or a random failing `C` cannot exclude the source; all surviving square-class
`C` must be eliminated or extended to a later contradiction.

There is also a reverse-use gap. Over an algebraic closure, after proving
`E/sigma=P^1` and that `p` generates the anti-invariant line, even valuations
off the four fixed points and multiples of four at them characterize geometric
squareness on the quotient. Over the actual `K`, a constant arithmetic square
class remains. Any resultant test must count multiplicities and all three
points at infinity. Forward use avoids these issues only because `3D/C`
already exhibits the square. **Consequence:** X3 is a conditional
parameterization, not current pruning; do not run its resultant/codimension
proposal before the source arrow.

**Strongest competitor: my X4 grading.** Mandatory rows such as the fixed
`g^9p^6` and `g^15p^10` coefficients equal to one force those coordinates to
weight zero; they cannot be treated as freely weighted variables. All fixed
scalar/affine rows must first be substituted. A single remaining homogeneous
candidate row containing both a nonzero scalar term and a positive-`k` term
ends this grading mechanism.

More fundamentally, X4 concerns `S/J`, `J=I:k^infinity`, in the literal
unguarded coefficient ring. Hybrid81 was obtained on the `k!=0` moving-face
chart. Deleting `z` from `zk-1` does not extend its Laurent coordinate change
to `k=0`; an inverse power of `k` has negative weight. Thus weights on the
localized 81-variable rows prove nothing about `S/J` without an explicit
unguarded map checking every fixed and original row. **Consequence:** my blind
recommendation to run the grading solve is withdrawn pending the already
assigned Volta fixed-face discriminator; no duplicate solve here.

Furter needs no second core review. For the named marked-axis attachment
`a(p)=A(0,p), b(p)=B(0,p)`, oddness and `a01=0` give
`(a compose b)'(0)=(b compose a)'(0)=0`, so the mandatory multiplier one fails.
Fable's dissipative Hénon control separately blocks a generic plane-basin
analogue. Sol's unspecified “one route” is not a typed client and remains GAP.

## Revised allocations and one separator

1. **Pure center:** REDESIGN around the first full-source residue arrow; keep
   X2q, X2c and X3 as separate outcome consumers. Stop immediately if the
   residue is rational/nonregular or still conditional.
2. **Global boundary:** await, but do not duplicate, Volta's already assigned
   literal-face X4 discriminator. This is the cheapest separator. PASS means
   an explicit nonnegative grading of the actual `S/J` data, all constant rows
   homogeneous and every unguarded row mapped; conditional on `J` proper it
   proves only `J+(k)` proper. Exact infeasibility or the first unmapped
   mandatory row closes this straight grading. A chart-only PASS changes
   nothing and is SCOPE-CONFLICT. Stop at that first outcome.
3. **All-degree proof:** CONTINUE only a source-sensitive receiver invariant or
   strict descent theorem covering every datum; no finite census substitute.

Hybrid81 is **STOP** as a solver lane: the sole 300.082-second run is spent,
timed out at 966729728 bytes, and was not memory-capped. I recommend no modular
retry: modular unit/nonunit behavior has no characteristic-zero endpoint, and
the frozen history already records an msolve allocation-overflow defect.
Retain its exact input as evidence. Had an exact run completed, a verified
proper Groebner basis of the complete ideal would itself suffice; a finite
Q-algebra point is an alternative, not an extra requirement. Furter attachment is STOP until a named
typed polynomial client arrives; bank the core only at its passed scope.
Serial boundary digits, K16 square/Pell/ramification variants, and cap/order
inflation remain STOP.

My blind Card 3 changes from RUN to STOP because its one run is spent; Card 2
changes from one future route read to STOP because no named client was supplied;
Card 1 changes from RUN to awaiting the literal-ring discriminator because the
localized map and fixed constants are load-bearing. Systems: **NO_CHANGE**—no
new defect survives deduplication. No exit price or mathematical promotion is
asserted. Terminal report complete; all writers IDLE.

<!-- BODY-END -->
