# Complete T2/T3 nonemptiness: certificate contract and preflight

2026-09-06, Astra independent design lane. **PRODUCER-CHECKED; independent
review required. No full-ideal solution or properness result.** The separate
Fable reverse-implication gate is not duplicated here.

## Outcome

A finite-field point plus a Jacobian minor is **not** a characteristic-zero
certificate for these overdetermined systems. The missing exact excess-row
relations can be as hard as ideal membership. Repeated finite Hensel survival
does not remove that gap.

The more promising *verification* shortcut is an exact small witness algebra:
give `H(T)` monic of positive degree in `Q[T]`, and all semantic coordinates in
`Q[T]/(H)`, then verify every full constraint there. Neither a Gröbner basis of
the full ideal, irreducibility of H, nor a reverse ideal-containment proof is
needed. The existing acyclic circuit is preferable to expanding the direct
ideal for this check. This is a directly applicable sufficient certificate,
not evidence that a small witness exists or is easy to find.

The metadata-only preflight also found one harmless free direction:
`target_e` occurs in none of the full constraint formulas in all three charts.
Consequently a 449-column full-rank Jacobian test for the first chart is
impossible; one may set this unused coordinate to zero.

## 1. Client scope and executed preflight

The charged completed report is
`xmodel/t2t3-compressor-gate-astra-20260906.md`, SHA-256
`3f768563da1a6cb05d066790387aa498a351db0654a0a2335aaa8849b933542a`.
Its receipt is terminal `DONE`, `BODY_SEALED`; its full-builder count bug
remains a separate executable gate. This report consumes the mathematical
full-row specification, not an incomplete output stream.

| Complete chart | Variables | Nonzero universal rows | Proved rank upper bound | Minimum left-cokernel dimension |
|---|---:|---:|---:|---:|
| 99, delta=2 | 449 | 2754 | 448 | 2306 |
| 99, delta=5/2 | 447 | 2754 | 446 | 2308 |
| 108, free mean | 507 | 3196 | 506 | 2690 |

The rank bounds use only the syntactically zero `target_e` column; they are
not achieved-rank claims. The other coordinates' occurrence does not prove
their Jacobian independence. The full ideal is extended from the ring without
`target_e`, so specializing just that coordinate to zero preserves its
properness in both directions. This small simplification is not a major
dimensional reduction.

The pinned support-count assignments at p=1,000,000,007 make **every**
candidate constraint nonzero. They were constructed to prove universal row
counts, not to solve the ideal. In the delta=2 assignment, the three inverse
residuals are 600678998, 401774531, 258548891. No full-system point, Jacobian
at such a point, or exact local-generator certificate is present in this
charged metadata. Thus the current Hensel-certificate preflight is **NO**;
the ideal itself is **UNDECIDED**.

The new light replay is
`box/nonemptiness-certificate-20260906/preflight_controls.py`, SHA-256
`1c183967e67100d5309b0b8aba3d996368c91cfc03ec1e50db013bc270ee3893`.
It pins the three source JSON files, frozen direct builder and count metadata;
reads their coordinate expressions; evaluates no large polynomials; and uses
only standard-library rational/integer arithmetic for the controls below.

```
python3 box/nonemptiness-certificate-20260906/preflight_controls.py
python3 -O box/nonemptiness-certificate-20260906/preflight_controls.py
python3 -OO box/nonemptiness-certificate-20260906/preflight_controls.py
```

All three returned rc0 and byte-identical output. All three rejected the
deliberately wrong local-containment multiplier with rc1 and `Local
containment` when `--mutate-local-containment` was appended. The script has
no Assert nodes and checks that fact. No solver, fleet job, live report body,
or `jc2-lean` was accessed.

## 2. The sufficient Hensel certificate, with its actual burden

Let `I=(f_1,...,f_M) <= Q[s_1,...,s_N]` be the COMPLETE client ideal. Here is
a sufficient certificate for `I != (1)`:

1. A prime p, a finite field kappa=`F_(p^a)` with a checked presentation, and
   `a_bar in kappa^N`.
2. Polynomials `g_1,...,g_r`, r<=N, p-integral in the chosen coefficient
   model, vanishing at `a_bar`, and r chosen coordinate columns whose
   Jacobian minor is nonzero at `a_bar`.
3. For **every** full row f_i, an exact rational polynomial identity

   `h_i f_i = sum_(j=1)^r A_ij g_j`,

   where h_i is p-integral and `h_i(a_bar) != 0`. Record every coefficient
   and denominator. Coefficients A_ij may be rational, even with p in their
   denominators, because this conclusion is over the fraction field; do not
   mislabel such a certificate as flatness of the original integral model.

Lift the N-r free coordinates arbitrarily to the integers of the unramified
extension K/Q_p with residue field kappa. Multivariate Hensel lifts the r
remaining coordinates to solve all g_j exactly. The h_i remain units there,
so the identities force all f_i to vanish in K. Thus there is a unital map
`Q[s]/I -> K`; I is proper. Faithful field extension and the weak
Nullstellensatz then give a Qbar point of the complete ideal.

This proof uses a fixed number of coefficient variables. Its p-adic limit is
a finite-degree polynomial pair whenever the independently checked client
reconstruction says so; no growing-support limit enters.

It is enough to use a smooth *witness subscheme*: the g_j need not belong to
I. Consequently adding rational affine slice equations is allowed for this
existence direction. One may select independent full rows and fix the
remaining variables to obtain a square subsystem, but still owes every
displayed containment identity. A point of an arbitrary subset is not a
point of the full ideal. Conversely, equality between ideals is unnecessary.

This is the usual standard-smooth/Hensel mechanism. The relative smoothness
criterion explicitly retains flatness; smoothness of a special fibre alone
does not supply it. See the primary [Stacks smoothness criterion](https://stacks.math.columbia.edu/tag/01V4)
and [Henselian local rings](https://stacks.math.columbia.edu/tag/04GE).
The paragraph above gives the specific sufficient implication used here.

At a proposed mod-p full point, the cheaper first discriminator is the exact
next-digit equation. For a chosen integral lift a_n already solving every
row modulo p^n, first compute the integer numerator f(a_n), prove its
divisibility by p^n, and only then form

`D f(a_bar) delta = -f(a_n)/p^n (mod p)`.

The table shows why the left-cokernel matters. A nonzero pairing with that
divided carry kills this one predecessor branch. Its vanishing permits the
next digit, not all depths. Exact local containment makes the excess equations
automatic at every depth; a numerical rank calculation does not.

## 3. Exact controls that reject the tempting shortcuts

**Positive local certificate.** At p=5 and (x,y,z)=(1,1,1), use

`g=(x^2-1, y-x, zx-1)`, and the extra full row `f_4=x-1`.

The square minor is 2 modulo 5 and `(x+1) f_4=g_1`, with x+1 a unit at the
point. The complete ideal has the exact rational point (1,1,1). The multiplier
is genuinely needed for the selected subsystem because its other branch
x=-1 does not obey f_4.

**Primitive vertical negative control.** For any fixed L>=1,

`I_L=(x, x+p^L) <= Z[x]`.

Both rows are primitive. The special fibre is the reduced smooth point x=0;
its full Jacobian has maximal column rank one. The same coefficient vector
solves all equations modulo p^n for every n<=L. Nevertheless their difference
is p^L, so `I_L Q[x]=(1)`; the branch fails at the next precision. This rejects
special-fibre smoothness, mod-p row redundancy, maximal Jacobian rank, and any
unqualified fixed finite-depth survival test, even after primitive row
normalization. The replay uses p=5 and L=1,2,4,8,16.

**Vanishing-localizer negative control.** For I=(x,p), the identity
`x*p=p*x` annihilates the extra row modulo J=(x), but its multiplier x is zero
at the mod-p point. Forgetting that gate would certify a characteristic-zero
unit ideal as nonempty.

**Growing-support negative control.** The polynomial
`S_n(x)=sum_(j=0)^(n-1) p^j x^j` satisfies

`(1-px) S_n - 1 = -p^n x^n`.

It solves the fixed functional equation to arbitrary precision only by growing
its x-support. Its p-adic limit is `1/(1-px)`, not a polynomial; no polynomial
can satisfy that identity over Q_p[x]. This is different from completing a
fixed vector of finitely many source coefficients.

## 4. Cheaper exact alternative: a one-way witness algebra

Supply a monic `H(T) in Q[T]` of degree d>=1 and a vector
`s_i = r_i(T) in A=Q[T]/(H)`, with deg r_i<d. Verify coefficientwise that
every full generator evaluates to zero in A, including every inverse row.
Then A is a nonzero Q-vector space with basis 1,T,...,T^(d-1), and evaluation
gives a unital map `Q[s]/I -> A`. Therefore I is proper. H need not be
irreducible or squarefree; any maximal ideal of A supplies the required
characteristic-zero field point. No claim about smoothness of I is needed.

If coordinates are supplied as rational functions in T, require explicit
Bezout identities making their denominators units modulo H, or replace them
with their certified polynomial residues. Scalar rational denominators are
harmless in A. Inverse variables must satisfy their actual equations; it is
not enough that a proposed leader looks nonzero at a numerical approximation.

A positive exact control is `A=Q[T]/(T^2-2)`, x=T, y=T. It satisfies
`x^2-2`, `y^2-2`, and `y-x`, since

`y^2-2 = (x^2-2)+(y+x)(y-x)`.

The replay additionally checks the exact S-polynomial identity for the monic
triangular basis `(x^2-2,y-x)`. More generally, a monic standard basis for
any nonzero witness algebra is enough: verify all critical reductions and
that its standard monomials include 1, then verify the image of every f_i.
Merely lifting the coefficients of a modular Gröbner basis while retaining
its leading monomials does not verify these exact identities.

**Direct implementation client.** Start with delta=2's audited acyclic graph:
7,136 monic definitions and all 4,470 original constraint slots, equivalent
to the 2,754 nonzero direct images. Evaluate the fixed definitions successively
in A, then every constraint. Preserve the universal row-label set even when
all specialized values vanish. The graph ledger hash is
`f04474ab822711465a7bad2ca204b5852bc2d7d4ebe28d08ae720eb76fab00db`,
and its gate records the source and full row-label hashes in
`box/t2t3-compressor-gate-20260906/graph-replay.json`.

This needs no expanded 449-variable generator stream, no reverse inclusion
of a proposed witness ideal into I, and no full exact-Q Groebner calculation.
For a supplied small-d witness, reduced univariate arithmetic is a materially
different cost model. Its runtime is not measured here; coefficient height
still needs a cap and a worker-side implementation gate.

Candidate production can use modular solving plus attempted algebraic
reconstruction of an isolated sliced point, but *only exact evaluation* of
all full rows certifies a successful reconstruction. A failed reconstruction
at a degree/height cap proves no nonexistence. None of the charged artifacts
currently provides such a candidate.

## 5. History checksum and recommendation

This does not reopen a supposedly new unrestricted Cartier/Hensel route:

- `xmodel/as-fonly-residue-ball-collision-compactness-theorem-repaired-20260825.md`
  already states fixed-support, complete-row, arbitrarily-deep compactness
  and transfer to Qbar. Its SHA is
  `81ab0e5cce46d2ad93968500362275ae4a7dbf2d3cf080c54ace531218135d71`.
- `xmodel/as-fonly-residue-ball-adic-certificate-target-20260825.md` already
  proposes covered carry/cokernel transitions and explicitly excludes
  changing support and unverified all-depth continuation.
- `xmodel/as-gauge-growth-p3-depth6-cartier-d7-point-20260824.md` exhibits a
  frozen depth-five point whose divided sixth carry has an uncorrectable
  x^2*y^2 coefficient, even with arbitrary new correction support.
- `xmodel/d43-source-high-hensel-hostile-review-fable5-20260828.md` expressly
  limits p^16 survival to one branch and refuses smoothness or a
  characteristic-zero conclusion.

**Decision:** do not commission a free-standing “rank implies lift” lane or
large high-precision run from the count witness. The current preflight fails
before a Hensel theorem is applicable. Reserve the small-witness-algebra
contract as an acceptance path for genuine full-system modular/algebraic
candidates. If a full mod-p point arrives, compute its rank and first exact
carry before allocating high-depth lifting; seek exact excess-row relations
only if a structural source mechanism makes them compact. Without that
mechanism, local-generation certification relocates the hard ideal-membership
problem rather than bypassing it.

This leaves full-ideal properness, the independent reverse-implication gate,
and JC2 unresolved. No global claim, case closure, or external publication is
made.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13083`.
- Body SHA-256:
  `6a3818f0b4d86a5da4a6455011292818770ab5204cb2733de837a05987102089`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
