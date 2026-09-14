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
