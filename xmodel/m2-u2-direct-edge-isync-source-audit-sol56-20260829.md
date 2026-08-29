# Direct nested-U2 edge: source and `i`-sync audit

Date: 2026-08-29  
Role: source audit answering Fable P1  
Binary verdict: **CERTIFIED** for an actual direct inner-U2-to-outer-U2
edge; not a certification of an unrefined stage-R census row  
Scope: printed adjacent-vertex identities and their exact reduced/full-degree
normalization only

## 0. Verdict

**CERTIFIED.**  Let `O` be an outer U2 merge and let `H` be an inner U2
merge vertex which arrives **directly** at `O`, so that in the printed tree
notation

```text
H = O + c.
```

Then the literal printed chain is

```text
deg(p_H^full)
  = mult(p_O^full,c)                         [Statement 3.17(i)]
  = i_O mult(p_O^red,c)                      [Proposition 8.1(i)]
  = i_O mu_e.
```

This chain has no chain-only or leaf-only premise.  It therefore applies
when `H` is itself an inner merge.  Applying Proposition 8.1(i) also at
`H` gives the full product synchronization

```text
i_H dp_H = i_O mu_e.                         (IS)
```

For an inner U2 cell, `dp_H=r*mu`, so `(IS)` is
`i_H*r*mu=i_O*mu_e`.  Statement 8.4 supplies `mu_e | M_H`, and
`M_H | dp_H`; hence the ratio required by `(IS)` is integral.  For an
actual edge the equality is not optional: it is forced by the single full
degree `deg(p_H^full)` appearing on both sides.

The positive integer `n_e` is even more direct.  With the correct
orientation, Proposition 9.3 itself states `n_e in N*` and equation (d)
gives

```text
kbar_O = (kbar_H+n_e)/nu_H.                  (NE)
```

No `i`-normalization is needed to obtain `(NE)` or the integrality of
`n_e`.  The degree identity is needed for the companion `X` handshake,
not for `(NE)`.

Thus Fable P1 is discharged for the theorem's explicitly hypothesized
actual direct edge.  It is **not** discharged for a generic stage-R record
labelled only as an “inner arrival”: that census contracts or forgets
inter-merge segments, carries no full degrees/`i`, and explicitly treats
its rows as conditional skeletons.  The smallest remaining census lemma is
a row-to-edge refinement/coverage lemma stated in Section 7.

## 1. Custody and exact sources

Exact SHA-256 inputs:

- Fable P1 review,
  `xmodel/m2-u2-nested-nu1-boundary-r1-hostile-review-fable5-20260829.md`,
  full `5cf66cd018e938cbc07cdeb9623baf28c667122ca602736154b8a694ec0142d7`,
  body `0fcd5675bee9a8a10562507ceaa40cd8518e601759956235f63ae91b012ec3d5`;
- reviewed target,
  `xmodel/m2-u2-nested-nu1-boundary-r1-sol56-20260829.md`,
  full `99bbe233f8f6f7273b2e5f89705aa5f2189681ce649a8723a66a0f99fa92912b`,
  body `11e44767526044590b2f3ed8ceaed6b0aa3eaa98b30008e15bc725149d8b90cf`;
- printed source,
  `refs/sigray_full.pdf`,
  `9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae`;
- campaign transcription and tier policy,
  `ladder/BOOK-OFFAXIS.md`,
  `7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77`;
- previously promoted orientation/full-degree dictionary,
  `ladder/SHEET6-DEPTH.md`,
  `ad9ced6c0420902f8cf63edf3636bed8633be511e925f208d24a24c35d71036d`;
- U2 normal-form producer and review,
  `xmodel/m2-u2-nu1-unbounded-lex-primary-grok46-20260829.md`,
  `9c20947be6d2ac6aad19176fae66f0b4acfb6ec6bce257a2169d8d266c667613`,
  and
  `xmodel/m2-u2-nu1-unbounded-lex-primary-hostile-review-fable5-20260829.md`,
  `e156f94ca83026fe04b287100ca79f72325c80a82f8ed3f3f8a94044db440740`;
- stage-R implementation witness,
  `cases/book_offaxis.py`,
  `c22e3a1f977fef94022f34378232fcc78148fa506501f71ec6a57313d6042ebc`.

Printed-page citations below use the PDF's printed page numbers, which are
the physical PDF page numbers.

## 2. Orientation: the three naming systems

The notation must be mapped before any formula is transported.  Use neutral
names `O` (outer merge) and `H` (the direct arriving inner merge).  The exact
dictionary is

| role | this audit | BOOK R2.1 | Proposition 9.3 | Statement 3.17 |
|---|---|---|---|---|
| outer/coarser vertex | `O` | `G` | `F` | `G` |
| arriving/finer vertex | `H` | `H_e` | `G` | `F` |
| tree relation | `H=O+c` | `H_e -> G` | `G=F+c` | `F=G+c` |

Proposition 3.2 and Statement 3.17, printed pp. 17--18, define the refined
vertex by `F=G+c`; hence `H=O+c`.  Proposition 9.3, printed pp. 50--51,
uses the opposite letters, `G=F+c`; hence its `F` is `O` and its `G` is
`H`.  The formulas below use this explicit substitution.  No conclusion is
drawn merely because two reports use the same letter `G`.

## 3. Literal full-degree chain

### 3.1 Statement 3.17(i)

For any adjacent `F=G+c` in `V_a`, Statement 3.17(i), printed p. 18,
states

```text
deg(p_F^full)=mult(p_G^full,c).
```

Substituting `F=H`, `G=O` gives

```text
deg(p_H^full)=mult(p_O^full,c).               (3.17)
```

The statement does not require `H` to be a chain vertex, a pole leaf, or an
`M=1` vertex.  Both U2 merge vertices are in the displayed domain.

### 3.2 Proposition 8.1(i)

At `O`, Proposition 8.1(i), printed pp. 39--40, defines

```text
i_O=deg(p_O^full)/M_O^*
```

and a reduced polynomial `p_O^red` such that

```text
f_O^+ = (xi^delta p_O^red)^i_O.
```

Consequently the full leading pattern is, up to a nonzero scalar,
`(p_O^red)^i_O`, and root multiplicities satisfy

```text
mult(p_O^full,c)=i_O mult(p_O^red,c).
```

By definition of an arrival multiplicity in BOOK R2,
`mu_e=mult(p_O^red,c)`.  Combining with `(3.17)` proves

```text
deg(p_H^full)=i_O mu_e.                       (DEG)
```

This is exactly the normalization asserted in BOOK R2.1.  SHEET6-DEPTH
Section 1 records the same two-source chain, but the proof here is directly
from the printed pages and does not inherit that sheet's `M=1` scope.

### 3.3 Full index/product synchronization

Applying Proposition 8.1(i) at the inner merge `H` gives

```text
deg(p_H^full)=i_H dp_H.
```

Together with `(DEG)` this is

```text
i_H dp_H=i_O mu_e.                            (IS)
```

For the direct nested-U2 theorem,

```text
dp_H=r*mu,                 mu_e=ell,
i_H*r*mu=i_O*ell.                              (IS-U2)
```

Statement 8.4, printed p. 42, gives `ell | M_H`; Proposition 8.1(v)
gives `M_H=gcd(dp_H,dq_H)`, so `ell | dp_H`.  Therefore `(IS-U2)` has no
local divisibility obstruction: algebraically one may take `i_O` divisible
by `dp_H/ell` and then `i_H=i_O*ell/dp_H`.  With several direct arrivals,
a common `i_O` can be chosen divisible by every `dp_{H_e}/mu_e`.

This last observation is only numerical solvability.  In an actual
configuration the indices are not freely assigned; `(IS)` says their
already-defined values must agree because both expressions equal the same
full degree.  Conversely, an abstract census tuple that contains no full
degrees does not thereby acquire actual indices.

## 4. The positive edge index is printed independently

The outer U2 merge lies in `V_{2,a}\V_{1,a}` and its nonzero direct
arrival is Proposition 9.3 case (I), as recorded in BOOK R2.  Proposition
9.3 says, before equations (a)--(d), that in cases (I)/(II) there exists
`n_e in N*`.  Equation (d), under the dictionary of Section 2, is

```text
kappa_O(1-pi(O))
  = ((1-pi(H))kappa_H+n_e)/nu_H.
```

Writing `kbar_V=kappa_V(1-pi(V))` gives

```text
kbar_O=(kbar_H+n_e)/nu_H,                     (NE)
n_e=nu_H*kbar_O-kbar_H in N*.
```

For a direct inner U2 arrival `nu_H=1`, hence

```text
n_e=kbar_O-kbar_H in N*.
```

This is precisely the integer anchor used by the reviewed direct-boundary
theorem.  It is not obtained by dividing a full degree, and its integrality
does not ride on `(DEG)`.  Thus the P1 review's sentence tying
`n_e in N*` itself to `i`-normalization is too strong.

The companion handshake does use `(DEG)`.  Proposition 9.3(c) reads

```text
D_O=(D_H+n_e deg(p_H^full))/nu_H.
```

Divide by `i_O`, use `(DEG)`, and put
`rho_H=D_H/deg(p_H^full)`, `X_O=D_O/i_O`:

```text
X_O=mu_e(rho_H+n_e)/nu_H
   =mu_e(kbar_O-w_H),
w_H=(kbar_H-rho_H)/nu_H.
```

So the whole R2.1 handshake, not merely `(NE)`, is certified for the
actual direct inner-merge edge.

## 5. Direct merge grammar versus a mandatory chain

No printed clause found in the cited chain mandates a chain vertex between
two merges.  Proposition 3.2 allows every refined child `H=O+c` determined
by a root direction; Statement 3.17 applies to that adjacent pair without
classifying `H` as chain or merge.  If `H` itself has at least two children,
it is an inner merge and remains a valid direct child of `O`.

This establishes grammatical possibility and the conditional identities;
it does not prove that any specified pair of U2 reduced cells is globally
realizable.  “Direct” remains a hypothesis of the nested theorem, not an
existence conclusion of this audit.

## 6. Why stage R still cannot consume every inner-arrival row

The printed theorem tier and the census tier are different objects.

BOOK-OFFAXIS Section 3 describes stage-R objects as conditional merge
skeletons.  Section 9 says an “inner-merge arrival” has unknown child weight
which must be composed down inter-merge segments.  Section 10 P5 further
states that the corrected census does not quotient last-vertex `nu`,
`kbar`, full pattern degree, or partner-dependent merge legality; its
honesty rider (ii) therefore declines to use `n_e`/`i`-sync as census kills.

The implementation confirms that perimeter.  In `cases/book_offaxis.py`:

- `hierarchies` stores only nested tuples of leaves/internal `G` nodes;
- `merge_cells` calls them “conditional ... skeletons” and passes an inner
  child upward only through an emitted `M` divisor;
- `expand2` represents an inner node by `('G',children,M_G)` with no full
  degree, `i`, terminal `nu`, terminal `kbar`, or segment-length tag;
- `stage_rp_census` consequently returns every skeleton OPEN and explicitly
  says full pattern degree and partner-dependent legality are not quotiented.

Matching the tuple label “inner” to the printed vertex `H` would therefore
be an unproved map.  In particular, a contracted hierarchy edge can stand
for an inner merge followed by a nonempty P0 segment; then its actual outer
arrival vertex is the segment endpoint, not the inner U2 merge, and the
direct theorem's formula cannot be substituted unchanged.

Accordingly, the source certificate changes no current 0-DEAD/0-ALIVE/all-
OPEN stage-R-prime census verdict by itself.

## 7. Smallest missing lemma and downstream scope

The smallest remaining lemma for census use is:

> **Direct-edge refinement/coverage lemma.**  Refine every abstract
> stage-R inner-arrival incidence by its actual inter-merge segment.  Prove
> that the zero-length class maps to adjacent vertices `H=O+c`, with the
> census reduced U2 data equal to their Proposition 8.1 reduced patterns;
> route every positive-length class to a separately proved P0-terminal
> formula.  The refinement must retain enough full-degree data to verify
> `deg(p_H^full)=i_O mu_e` rather than identify similarly named reduced
> quantities.

No new local `i`-sync lemma is missing for the zero-length class: Sections
3--4 already prove it.  What is missing is coverage from an abstract
contracted census row to that class.

Maximum safe downstream consequence:

1. Fable P1 is discharged for every **actual direct** inner-U2-to-U2 edge.
   The provisional direct-boundary enumeration may use
   `n_e in N*` and the R2.1 handshake to exclude that printed-edge slice,
   subject to its other reviewed hypotheses and R4 (`alive != existent`).
2. The certificate does not promote an arbitrary stage-R “inner arrival”
   to a direct edge, does not cover any intervening P0 segment, and does not
   turn a conditional skeleton into a realizable cell.
3. No full-cell completeness, landing, gluing, Statement 3.9 coefficient
   compatibility, panel death, degree ceiling, `G2`, or JC2 consequence
   follows.

No web, AWS, heavy computation, canonical edit, commit, or push was used.

---

Report-body SHA-256 (all bytes before the separator line above):
`6c24091eecb78fe82b664794421fb8e1685c60394d807ed21d2866d16b38f0f2`.
