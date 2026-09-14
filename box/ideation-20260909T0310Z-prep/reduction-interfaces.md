## Executive verdict

The advertised end-to-end reduction

\[
  \text{Keller counterexample}
  \Longrightarrow \text{GGV polygon data}
  \Longrightarrow \text{sheet data of degree }d
  \Longrightarrow \text{an enumerated book entry}
\]

is **not a theorem in the repository or in the cited literature**.

What is presently supportable is weaker:

1. If the plane Jacobian conjecture is false, GGV's published minimal-pair
   theorem permits the selection of **some** globally minimal counterexample
   in a standard Newton-polygon frame. This is an existential selection from
   all counterexamples, not a normalization theorem for every given
   counterexample.
2. For the globally selected GGV pair, [TRANSPORT.md](TRANSPORT.md)
   Theorems 2.1 and 3.1 give an explicit Sigray-normalized representative of
   the same pair, with unchanged field-extension degree; equations
   (4.1)–(4.5) retain the native pre-Laurent GGV ledger losslessly.  This
   closes the T2-to-T4 normalization fork.  It does **not** translate a GGV
   chain into a decorated Sigray pole tree: later Laurent-chain records are
   only recoverable metadata, and the sheet construction still does not
   consume the GGV packet with the fidelity required by `G2-PSC`.
3. A Sigray-normalized counterexample has pole/tree data and, after the
   promoted repair of Sigray's unproved Proposition 5.8, a finite **entry menu**
   at each fixed topological degree. This is the strongest general finite
   reduction presently justified.
4. The passage from an entry menu to a complete **full-configuration** book
   is not general. In the all-\(b=1\) sector, `MP` plus the reviewed depth
   theorem does assert a conditional landing of every configuration at a
   marked first jump/root event in a finite local `BOOK(s,td)`. That is a
   genuine local landing theorem. It does not classify every downstream
   all-\(\mu\ge2\) / \(M\ge2\) continuation needed to treat the record as a
   complete configuration. The implementation also skips every off-axis
   entry, and the generic off-axis audit expressly reports that no
   completeness certificate exists for any \(b\ge2\) entry. Only bounded or
   specially hand-classified sectors have been concretely enumerated.
5. No theorem bounds the topological degree of a counterexample above. A
   run over \(td=6,\ldots,14\) therefore cannot be an end-to-end reduction of
   JC2 even if every one of those books were complete.

Thus the correct campaign-level conclusion is:

> **There is no unconditional theorem sending an arbitrary planar Keller
> counterexample to a configuration in a currently enumerated book
> \(B(td,\mathrm{entry})\).** The repository proves or promotes several
> valuable necessary-data reductions, but the universal book-landing link is
> missing.

### Terminology correction: the two obligations formerly called `G2`

This document now reserves two different names for two logically different
obligations that earlier roadmap notes sometimes conflated:

- **`G2-PSC` (packet/sheet compatibility):** a global theorem transporting
  the GGV packet/corner (and its provenance) into a specified, decorated
  Sigray pole-tree datum with enough fidelity to use the later book
  machinery.
- **`G2-BD` (bounded delay/carrier):** after a residue-A configuration has
  already been reached, a bound on the delay/carrier parameter needed to
  enter a finite book.

Neither obligation implies the other. A hybrid architecture that advertises
GGV polygon restrictions as input to the Sigray/book stage owes `G2-PSC`. A
pure Sigray architecture may bypass `G2-PSC` by selecting and minimizing a
hypothetical counterexample wholly inside the Sigray frame, but then the GGV
packet/farm is not an input to that proof. Such an architecture still owes
its own Sigray source theorem, full landing and coverage, and any `G2-BD` or
type/total-degree bound used by its chosen endpoint.

The rest of this document states the attempted chain theorem by theorem,
records every external dependency used by it, and separates gaps from claims
that are actually false.

---

## 7. Superseding roadmap correction: transport, delay, and degree control

This section supersedes earlier campaign shorthand that used `G2` for both a
global transport problem and a post-landing delay problem, or displayed the
sufficient local bounds below as equivalences. It is a correction of the
strategy map, not a promotion of any conjectural estimate.

### 7.1 `G2-PSC` and `G2-BD` are different obligations

The definitions in the terminology box above are canonical. In particular,

```
G2-PSC  =  GGV packet/corner -> decorated Sigray pole-tree transport/fidelity,
G2-BD   =  bounded delay/carrier after residue-A has already been reached.
```

There is no established implication in either direction. `G2-BD` says
nothing about whether the residue-A datum comes from the globally selected GGV
packet; `G2-PSC` says nothing by itself about bounding a later carrier.

The architecture determines whether `G2-PSC` is required:

- A **hybrid GGV-to-Sigray architecture** owes `G2-PSC` before it may use GGV
  polygon restrictions in a Sigray/book argument.
- A **pure Sigray architecture** can bypass `G2-PSC` by choosing and minimizing
  the hypothetical counterexample wholly in the Sigray frame. It may not then
  claim the unused GGV packet/farm as an input, and it still owes a Sigray
  source theorem, all-branch landing and coverage, and the delay/type bounds
  used by its endpoint.

### 7.2 The correct local implication chain for total degree

For a residue-A chart of type `(alpha,beta)` with face polynomial `Psi`, the
exact identity is

```
td = deg(Psi) / (alpha beta).
```

Within the stated residue-A hypotheses and with the same constant `C`, the
proved/formal implication map is

```
DIR(C)  <=>  PC(C)  <=>  RPMC(C)  =>  KJN(C).
```

The reverse implication `KJN(C) => RPMC(C)` is not established: a bound on
the total root multiplicity does not give the rootwise ceiling. The first
three formulations are therefore sufficient strengthenings of KJN, not
equivalent names for it.

Moreover, KJN is **type-relative**:

```
KJN(C):  deg(Psi) <= C (alpha beta)^2
          => td <= C alpha beta.
```

It becomes an absolute/cofinal total-degree ceiling only after an independent
theorem supplies a legitimately finite or uniformly bounded menu of
`(alpha,beta)` types, together with the provenance needed to place every
counterexample in that menu (and with the relevant constants bounded over the
menu). KJN alone does not supply that type theorem. Thus neither KJN nor the
stronger local conjectures, by themselves, makes the whole ladder
unconditional.

### 7.3 The correct one-way chain for bounded delay

For a degree-minimal counterexample **inside the residue-A class**, the
residue-A scale estimate is a sufficient route:

```
A-SCALE(B_A)  =>  UCD-A-min  =>  G2-BD.
```

No converse arrow is established. Nor does the restricted `UCD-A-min`
statement imply unrestricted UCD. The exact Keller-Henon family refutes the
unrestricted UCD/K2C formulation, while leaving the type-(2,3),
degree-minimal, residue-A statement open.

### 7.4 No promoted merger theorem

The local comparison currently supports only the following asymmetric fact:
on a fixed residue-A inventory, `A-SCALE` gives a coarse directional bound;
the directional condition does not recover the common scale `a+b`. Hence
there is no known equivalence or single promoted lemma joining `DIR` and
`A-SCALE`. The formal separation/countermodel work and this bridge analysis
are single-model campaign evidence, whereas the pure-boundary identity and
the exact unrestricted Henon obstruction have independent confirmations.

Algebraizing either formal obstruction family could yield a genuine
disproof route. Conversely, failure to algebraize those particular families
would not prove KJN, `G2-BD`, or the Jacobian conjecture: the global
transport/source, full landing, off-axis coverage, and type-provenance gaps in
Section 3 would still have to be discharged. None of those gaps is closed by
the corrected arrows above.

### 7.5 Physical-chart and exit-localization correction

VGG Corollary 7.4 does not supply the second physical infinity chart of the
same fixed pair.  Under signed transpose its live packet is subsumed by native
Corollaries 7.1/7.2 on the same `upper_dir=(-3,1)` edge; the 12/8 powers are
correct native face data.  VGG minimal re-selection is also chart-rigid: its
final oriented minimal transition is diagonal affine (followed only by the
translation of Proposition 5.20).  Therefore every reduction argument must
obtain the other physical chart from an intrinsic exact-pair constructor, not
from transpose or VGG re-selection.

The old aggregate `C74-PLACE` label is retired.  Different-model hostile
review `xmodel/g2-intrinsic-exact-pair-l3-l5-hostile-review-opus5-20260828-v1.md`
(`5d219c53...`) establishes the following split after its mandatory repairs:

```text
common/source-side
L1 native face-power custody                                      available
L2 root/multiplicity/component convention                         available

intrinsic exact-pair constructor
L3-exact all-root prefixes are actual fibre truncations           available
L4-exact the two charts cover all boundary places                 available
         only for a normalized Lemma 2.1 rectangle/NE-corner fibre
L5-exact certified terminal deck orbits biject normalized places available
         terminal record `(h,chart,kappa,F)` must carry `deg p_{h,F}=1`

hybrid VGG/GGV selected-source constructor
L3-hybrid selected translations are actual truncations            open (H-TRUNC)
L4-hybrid selected-source leaves cover both physical charts       open
L5-hybrid uncertified source leaves are terminal places           open / ill-typed
```

For an intrinsic terminal, `orbit size = e_S`, `stabilizer size =
kappa/e_S`, and `e_S = kappa/gcd(kappa,supp F)` with the empty-support
convention `gcd(kappa,{})=kappa`.  The unique continuation is Hensel lifting
on the shifted, `t`-cleared equation, not on the original Laurent equation.
Also `ord_t=(kappa/e_S)ord_S`; signs may be read on the cover, but numerical
place orders require this rescaling.  None of these intrinsic facts licenses
the hybrid arrows.

If every nonzero mismatch subtree is assumed to have a first exit, summing
over first exits merely repartitions the `RPMC(C)` sum.  Thus the previously
stated `EXIT-RPMC(C)` is equivalent to `RPMC(C)` under its clause 1, not a
cheaper implication.  A future local exit module may still organize a proof,
but it must produce a genuinely stronger inequality and must be invariant
under the permitted blowups/translations; no such theorem is promoted.

Frozen orientation is `(m,n)=(beta,alpha)=(3,2)` with
`(alpha,beta)=(2,3)`.  Proximity-closed means closed under the full relation
“proximate to,” including the second predecessor of a satellite point.
