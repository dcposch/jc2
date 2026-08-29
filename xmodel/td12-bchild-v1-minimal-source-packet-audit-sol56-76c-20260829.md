# TD12-BCHILD/v1: minimal source-packet audit

Date: 2026-08-29  
Author: Sol 5.6 (Ultra)  
Basis: `76c746f698103d20019bfeb72654a361ccc5371d`

## Result

The campaign already has the generic exact-pair-to-completion constructor,
but it has no instance of that constructor for either td12 U1 reduced cell.
Thus the missing object is not another theorem saying that Newton--Puiseux
coefficients exist.  It is a route-specific, coefficient-bearing source
instance.

There are two useful minimal packets, depending on the consumer.

### A. Minimal gate-evaluation packet

To evaluate only the first child in one named direction, it is enough to
supply

```text
ChildEvalJet_I :=
  coefficient field K and exact raw centre c
  + chart labels (side, kappa, u, parent top index R)
  + certified full index I=mult(P_0,c)
  + the finite f-side Laurent jet P_0,...,P_I
  + provenance map identifying every P_k with the coefficient of one
    exact f under one branch completion.
```

This packet emits

```text
v_(c,k)=[(eta-c)^(I-k)]P_k,  0<=k<=I,
```

without needing the original `g` or the approximate-root ladder.  It is the
smallest packet for the necessary pure-power rejection test.  Omitting the
provenance map would reduce it to an arbitrary formal interpolation and
would not make it a source jet.

### B. Minimal recurrence-producing packet

To derive the f jet from `J(f,g)=1`, or to certify it through the source
ladder, the smallest honest packet is

```text
TD12LocalPairJet_I :=
  PairRef(f,g) over K, with exact constant Jacobian and support bounds
  + fibre value a and component/side orientation
  + one exact boundary place S and completion map
      iota_S: K[x,y]/(f-a) -> K'((t))
  + the selected parent F, Puiseux prefix, kappa, u, and raw child centre c
  + exact f- and original-g Laurent coefficients through every grade
    needed to produce P_0,...,P_I, including top indices R,S
  + a declared free-side/gauge normalization for the one-equation/two-new-
    functions Keller recurrence
  + if reduced Proposition-8.1 q is consumed: the instantiated repaired
    tower (m; h_j,k_j,l_j,s_j) and the needed Laurent jets of every h_j
  + nonvanishing, support, coefficient-field, and denominator certificates.
```

Exact polynomials `f,g` plus the exact completion map can replace the finite
coefficient lists: substitution computes them.  Likewise the repaired
approximate-root tower is algorithmically reconstructible from an exact pair
and chart, modulo the campaign's explicitly filed Proposition-4.2 trust
boundary.  Storing both the exact pair and all emitted jets is redundant but
useful for custody/replay.

For all three first-child vectors one packet may share `PairRef`, fibre, and
source ladder, but it needs one `nu=25` completion/centre and the two
`nu=17` centres.  The two sibling vectors share the same parent f-jet.

## Absent versus merely uncited

| Field or theorem | Status on the frozen td12 basis | Reason |
|---|---|---|
| Generic exact pair/fibre -> normalized boundary places, completions, Puiseux expansions, residuals, and approximate-root decoration | **PRESENT BUT UNCITED BY THE CELL REPORTS** | The reviewed `g2-psc-typed-source-to-pole-tree-interface` gives this constructor, with its repairs and trust boundary. |
| Base chart identity and shared Keller convolution | **PRESENT/DERIVABLE BUT PREVIOUSLY UNPACKAGED FOR THIS CLIENT** | Printed Statement 3.7 and Proposition 4.1 give it; the provisional TD12-BCHILD report writes the coefficient formula. |
| Generic repaired positive-tree approximate-root recursion | **PRESENT BUT UNINSTANTIATED** | The Proposition-4.2 repair records `h_0=g`, `h_(j+1)=h_j^k-s_j f^l`, including the constant-corner branch. |
| A td12 U1 `PairRef(f,g)` with actual coefficients and support | **GENUINELY ABSENT** | The U1 record is a necessary-condition/reduced arithmetic family. No polynomial Keller realization is known or serialized. Exact pairs elsewhere in the repository are different scoped objects and cannot be substituted. |
| Fibre tag and exact boundary-place/completion instance for the B or sibling route | **GENUINELY ABSENT** | The symbols `A,B,B_+,B_-` name reduced orbit values, not a map from a fibre algebra to a complete DVR. |
| Full f-top `P_0` at the three roots | **PRESENT UP TO A NONZERO TOP SCALE, CONDITIONAL ON THE FULL INDEX** | Reduced `p` and Proposition 8.1(i) give `P_0=lambda_f p^I`; the direct-entry rider gives `I=6n`. This suffices for `v_(c,0)`, not the rest of the vector. |
| f-side lower pieces `P_1,...,P_I` | **GENUINELY ABSENT** | Only residue, vanishing, degree spaces and formal A/B interpolation are present. No source-provenanced values are emitted. |
| Original-g top coefficient `Q_0`, its top index `S`, and lower pieces | **GENUINELY ABSENT AS TYPED ROUTE DATA** | Type `(2,3)` suggests a first common-power relation only after a named tower stage is proved active. The trunk producer itself says that a named tower/index at the predecessor is not instantiated. An analogous td6 template is not this route. |
| Reduced `q_F` | **PRESENT, BUT NOT A SUBSTITUTE FOR ORIGINAL g** | It is the Proposition-8.1 quotient of the terminal derived `h_F` top after removing a power of reduced `p`. |
| Instantiated `(m;h_j,k_j,l_j,s_j)` ladder and its coefficient jets at the td12 trunk/sibling | **GENUINELY ABSENT** | The generic recursion exists, but neither cell record names its route-specific length, constants, polynomials, or Laurent coefficients. |
| Root/orbit ratios and coefficient fields | **PRESENT AT REDUCED-TOP SCOPE** | B has `B/A=9/8`; the sibling has `B_+/A=(9+3i)/8`, `B_-/A=(9-3i)/8`. Raw centres still require 25th/17th Kummer roots. |
| Residues and no-jump depth consumers | **PRESENT** | `e_k=22k mod25`, depth 24; `e_k=13k mod17`, two depth-16 consumers. These constrain an emitted jet but do not create it. |
| Gauge/free-side choice making the Keller ODE forward | **GENUINELY UNCHOSEN** | At each grade the recurrence contains both new f- and g-side functions. A support-normalized source parametrization must choose one side or solve a coupled finite system. |

The most economical next producer is therefore not a general-purpose heavy
CAS job.  It is a route-local symbolic source emitter whose input is an
explicit coefficient family for a hypothetical type-`(2,3)` pair and whose
first output is `ChildEvalJet_I`.  Until such a coefficient family is
defined, there is nothing source-typed to run.  If an exact pair is ever
available, direct substitution into its completion is cheaper and stronger
than recursively solving the one-equation/two-function Keller convolution.

## Custody

Actually charged files and recomputed hashes:

```text
4c3f2236a11f296f7eb194bb26e8cdc8ff0b91f10d8d7151e6314caa62629304  xmodel/g2-psc-typed-source-to-pole-tree-interface-sol-ultra-20260827.md
f7de3ae12918c9103d595e81ddc7fcb9082ba950698f70966ade3ea576cc79a1  xmodel/g2-psc-typed-source-to-pole-tree-interface-hostile-review-opus5-20260827.md
d409510a3df418f402a80cc954f646d35a054e9055783fadc0aaa234bb49b242  ladder/REDUCTION.md
10bc55d53f9cf9a9e6a4535787f6e208a25f0ebfbd6dbd803f68b00f8ca8f5cd  xmodel/sigray-prop42-constant-shift-repair-sol-ultra-20260828.md
5fc6b1634dc1ef0a0abe578411644fa166ffbfa16b8608cbce2a7b7b61465cd5  xmodel/sigray-later-m-package-source-audit-sol-ultra-20260828.md
599e2a9123194c580b89b822f5b7a218fa5e9735b16bcb744e0f0e4231584271  xmodel/m2-td12-u1-trunk-consumer-primary-grok46-20260829.md
635aecffbd226acbc29787cec86bc1fdcdfa459e1aa38a8d1a8acb5d6593b72a  xmodel/m2-20260829-promotions-theorem-interface-pass-sol56.md
```

No source or canonical file, code, AWS resource, or commit was changed.

*End of sealed report body.*

## Seal

- Body length: `7700` bytes (all bytes before this heading).
- Body SHA-256:
  `9d8a012d80b9ad2109a0ebc12ec65a61e69f09885ce5de8f38e1290492c77458`.
- Frozen Git basis:
  `76c746f698103d20019bfeb72654a361ccc5371d`.
