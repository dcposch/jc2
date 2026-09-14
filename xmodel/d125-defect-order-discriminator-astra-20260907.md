# D125 unequal/Q defect-order discriminator

Status: **YES, algebraically justified next capped comparison; PREPARATION ONLY.** 2026-09-07. No AWS access, CAS, solver, deployment, full source parsing, Jacobian/lift expansion or B substitution. The previous dp attempt timed out without a G block; this proposal supplies no ideal decision and no measured speedup.

## 1. Outcome and exact scope

On the frozen **unequal/rational** complete client, the proposed order makes each of the **192 nonkernel free B variables** the leading monomial of a polynomial obtained by constant rational row operations on original Jacobian equations. This includes every homogeneous B block d=1..24, with its actual forced faces. The four free kernel coordinates are exactly `B_g0_p5`, `B_g0_p10`, `B_g0_p15`, `B_g0_p20`.

Keep all **269 names and 803 literal rows**, including 105 lift equations, zero/fixed-map residuals, all guards and all low Jacobian equations. The scalar target remains `J(A,B)+(5/9)*gamma^2`; neither a field change nor a source change is proposed. In particular there is **no degree-15 target shear**, no B reconstruction expansion, no lambda elimination and no gauge. The graph complement has 71 A + 4 kernel + 2 lambda = **77** coordinates, not the gauged 76-coordinate presentation. This is a leading-ideal statement, not a dimension assertion.

Consequently, if the full ideal is proper, any Groebner basis for this order must have a polynomial with each of these 192 variable leading monomials: a divisor of a variable is either itself or 1, and 1 would make the ideal unit. This does not say when slimgb will discover them. Reducing by them may cause the same large polynomial fill that explicit B substitution would cause.

**Recommendation:** one same-cap 300-second exact-Q comparison is better justified than first paying to construct expanded B formulas. It has the same input rows and avoids a new expanded input. It is not a prediction that the solve will finish or use less memory.

## 2. Exact order

In the existing displayed variable order put

`W1(A_ij)=15-i-j; W1(B_ij)=25-i-j; W1(lambda2)=3; W1(lambda3)=2`,

`W2(B_ij)=25-i-j`, with W2 zero otherwise, and `W3(B_ij)=i`, with W3 zero otherwise. Compare monomials lexicographically by

`(W1, W2, W3, ordinary total degree, -last exponent, ..., -first exponent)`.

Every free A/B coefficient is strictly below its fixed entire outer face. All 269 W1 entries are positive integers, ranging from 1 to 24. Thus this is a global multiplicative well-order: bounded first weight contains only finitely many monomials, and the final dp comparison separates ties. The lambda weights make them positive too; no lift equation is altered or declared redundant by choosing them.

Owned `witnesses.json` supplies all 269 names, three exact 269-entry vectors, all block witnesses and the complete ring declaration. Digests:

- Canonical order descriptor: `64c212c26a9883d1c0f674b93f0246f67e22a8b742b643c6628fd3c14014db66`.
- Complete proposed ring declaration: `d894d6427d39b774c403165c83bffddbe993b96345ee00d652f5af7a06219bca`.
- The same names with the original dp descriptor reproduce the frozen first-attempt ring digest `ccd93ccf39b0109a36dc89d54f1fd281bcef17b1dc5fab3c65f2988027333d73` in a separate tiny metadata check.

## 3. Actual face and all-layer proof

Here `H=pi^2*(pi^3+gamma^3)`, `A15=H^3`, `B25=H^5`. Below their outer faces the known nonzero coefficients are `A_(2,1)=1`, `B_(1,0)=5/9`, `B_(8,5)=5/3`. Every prescribed zero and both target constants remain fixed as in the source contract.

For `1<=d<=24`, the actual free B columns are exactly `i=0..q_d`, `q_d=floor((7d+4)/12)`, in degree-d monomials `gamma^i*pi^(d-i)`. The known B terms at d=1 and d=13 are forcing, not free columns. The degree-(d+13) Jacobian equations have the form

`L_d(B_d_free) + [H^3,K_d] + sum_(k+e=d+15, k<15, e>d) [A_k,B_e] = 0`,

where `L_d(C)=[H^3,C]`. B degrees below d cannot enter. The target at physical degree 2 is outside these layers.

Each free B_d linear monomial has first two weights `(25-d,25-d)`. If both coefficients in a forcing bracket are free, its monomial has

`W1=(15-k)+(25-e)=25-d`, but `W2=25-e<25-d`.

Replacing a positive-defect coefficient by its prescribed rational scalar strictly lowers W1. Replacing a zero-defect top coefficient by its prescribed scalar leaves W1 unchanged and gives W2=0. The separate `[H^3,K_d]` term is constant in coefficient variables and therefore strictly smaller as well. Thus **every forcing monomial is below every free B_d variable**, before doing any substitution or using any lift relation. This remains true under constant row combinations, even when terms cancel.

The reviewed kernel proof applies to the actual H: it has a simple root at pi/gamma=-1. From `[H,C]=0` for homogeneous C_d, the order at that root gives `5*ord(C)=d`; hence the kernel is zero unless 5 divides d, when it is the scalar span of `H^(d/5)`. Each `H^r`, r=1..4, lies wholly in the actual free B columns, has pi^(5r) coefficient 1 and lies strictly below the fixed inner face. No generic-root assumption is used.

For `H^3=sum h_p*gamma^p*pi^(15-p)`, the exact matrix entry is

`M_d[r,i]=(p*d-15*i)*h_p`, `p=r+1-i`, with `h_0,h_3,h_6,h_9=1,3,3,1`.

The rows r=i-1 for i>=1 have triangular diagonal -15i. All such columns can be solved in terms of column 0. In the four kernel blocks that column is the marked kernel scalar; W3 makes every other column strictly larger. In a nonkernel block the remaining constant Schur pivot also solves column 0. Equivalently, descending-column rational RREF has pivots q_d,...,1 in kernel blocks, and q_d,...,0 otherwise. The kernel graph relations lead at B_i because their only same-layer alternative is a multiple of B_0; all other forcing has smaller W1/W2. Nonkernel relations lead at their solved B_i.

All nonzero diagonal matrix rows have `r<=q_d+8<=22`, so they belong to the source's full `0<=gamma-exponent<=23` Jacobian envelope. There is no missing row from the 660-versus-780 envelope distinction. The exact ranks sum to 192 across 196 columns. The d=25 block is already fixed; B0 is fixed zero, not a pivot. Therefore Jacobian physical degrees 0..13, the degree-2 target, every unselected high-degree compatibility row, and all 105 lift rows remain obligations.

These are polynomials in the **original ideal**, obtained with rational constants only. No additional equation, localization, point, properness or exclusion has been obtained.

## 4. Primary Singular support and syntax

The version-matching Singular **Release-4-3-2** reference says that `slimgb` uses the basering order and requires it to be global; it also documents `option(redSB)`. Thus the proposed global order is within its documented scope. [Primary slimgb reference, lines 7037-7057](https://raw.githubusercontent.com/Singular/Singular/Release-4-3-2/doc/reference.doc).

The same release documents `a(...)` as an extra comparison row, allowing integer weights including zero; it refines a subsequent ordering. Use the explicit three full-length rows followed by dp:

`ring R=0,(unchanged_names),(a(W1_entries),a(W2_entries),a(W3_entries),dp);`

The owned ring string contains integers, not the placeholder identifiers above. These are successive refinements on the same variable list, not disjoint variable blocks. Do **not** pass a rectangular 3-by-269 object to `M`: that syntax requires a square full-rank matrix. The final dp tie-break avoids needing to manufacture one. The documentation notes that predefined/refined orders can avoid the cost of general matrix evaluation. [Primary ordering definitions, lines 1181-1290](https://raw.githubusercontent.com/Singular/Singular/Release-4-3-2/doc/pdata.doc).

This is documentary support, **not an executed test of the retained installed binary**. Before any full attempt, one tiny future-authorized engine control must confirm the actual three-a syntax, global attribute and leading monomials across W1/W2/W3/dp ties. No local CAS or remote action was taken here.

## 5. Minimal versioned adaptation, not implemented here

Keep the frozen input JSONL/Singular files byte-identical and keep `read_source` unchanged: it must still verify the original dp header, both original file pins, all 269 variable IDs and all 803 literal equations. A small new order helper must validate the exact names against the descriptor above, then replace **only the initial ring-declaration line** of the returned execution prefix. Compare the remaining prefix bytes exactly with the original. Preserve the old file; emit only a fresh versioned execution input.

The narrow checker change is to add an optional explicit weight-row argument to `key`, propagate it through every leading-term choice in `normal_form` and `proper_certificate`, and bind the same order descriptor in `ring_id`/`parse_result`. For this attempt there is only the one fixed new descriptor, not an arbitrary-order framework. The weighted key is the expression in section 2. Legacy dp controls may retain their explicit old descriptor; production must not fall back silently. The source ring digest and execution/result order digest are different named fields, not interchangeable.

The driver must bind the new helper/checker/caller pins, source pins, ring-declaration and order-descriptor digests in a fresh registration and authority. Its footer must emit that new result order digest. Parsing still requires literally empty stderr, exact nonzero engine-I size, complete indexed I/G/T, no trailing text, and correct engine-to-original zero/duplicate mapping. `short=0` remains. **Never pass a weighted basis to the old dp verifier.**

For a unit result, retain and replay the original-row cofactor identity against all 803 fixed source rows; polynomial multiplication and that identity are order-independent. For a nonunit result, the exact-Q checker must verify Buchberger's criterion, nonzero normal form of 1, and zero normal forms of **every original equation under this weighted order**. It certifies a proper superideal, which suffices for original-ideal properness; no `G subset I` proof is required. A raw incomplete G block, timeout, parser marker, modular output or unverified nonunit list is no decision.

Required tiny delta controls before a new root GREEN: (a) real installed-engine order comparisons across all four refinements; (b) a weighted graph basis `x-y^2,z-y^3` using first weights `(3,1,4)` is a GB with leaders x,z, but is not a dp GB—the dp S remainder is `x*y-z`; this distinguishes the comparator; (c) order-header/vector drift, source-prefix/row omission, zero/duplicate I mapping and corrupted cofactor rejection; (d) the existing false-proper control `(x*y-1,x^2)` still fails Buchberger. These are **pending controls**, not runs claimed in this report.

After code/delta acceptance, a prospective comparison can reuse the previous 300-second decision plus conditional lift in the same cap, optional 120-second verification only after normal completion, 450-second total, 16-GiB AS/group RSS and inherited 64-MiB per-stream FSIZE/core-zero limits. Same single attempt, no retries, extra gauges, compression, enlarged resources or changed fields. These are a proposal only; no solver authorization or worker custody is assumed.

## 6. Actual tiny replay, inputs and terminal custody

Owned check.py uses only the frozen small face maps, integer degree inequalities and rational matrices no larger than 38-by-15. It never calls the coefficient-row exporter or forms a full J/lift coefficient. It checks all actual free columns and lower nonzero fixed-face positions, all 24 ranks and leading-column directions, all four monic kernels, positive W1, the 803/269 metadata and 952 degree/free-or-fixed weight inequalities. Normal and `-O` emit identical exact witnesses, passing in 0.06/0.23 seconds. Changed-object controls zero W2, reverse W3, and replace H by nonprimitive pi^5: all three reject at the intended check in both modes. Each command had 30-wall/25-CPU-second and 512-MiB AS limits; observed maximum RSS across the eight runs was 38172 KiB, largest wall 0.52 seconds. No approximate minor file was consumed.

Read perimeter: the whole terminal B reconstruction producer and Fable gate, the whole frozen baseline map helper and repaired exact checker/caller, current transaction helper, and the primary documentation above. The B gate's float-degraded historical minor artifact is not relied on; the present matrices and witnesses use Fraction arithmetic. Other reconstruction/geometry filenames were discovered by path-only search, not read. No live geometry peer, protected project, shared ledger, remote worker or full client stream was accessed or changed.

Frozen local inputs (SHA-256):

- `xmodel/d125-minimal-receiver-b-reconstruction-astra-20260906.md`: `cd2792c8ec4fdbd286fe7925f36739337ea621eb69d5ea8df90a7cd5804c82bf`.
- `xmodel/d125-b-reconstruction-gate-fable5-20260906.md`: `3f154e7816deb5de39e727f99cafac3328592c703af246614d4f1e9fe2ccf1ea`.
- `box/d125-small-source-exporter-prep-20260906/baseline.py`: `ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53`.
- `box/d125-small-exact-solver-strict-repair-20260907/exact.py`: `7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9`.
- Same directory `driver.py`: `7f081576ea72005c2509ef2d575aa63b9fd53416987f3535ed520fd79fdc130d`.

Prospective original source pins, retained from accepted custody and not re-read here: JSONL `b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac`; Singular `c089c33301e3889e0c20527386719f411907cf2957ecfad3d93c65f7be24e718`. These must be freshly checked in any later authorized execution.

Owned artifacts in `box/d125-defect-order-discriminator-20260907/`:

- `check.py`: `5fb9827d147e693b3de49e1d4c9125880c6e459318e1c32a92f78f712a97531d`.
- `witnesses.json`: `6e8c0102089ca6d046f4e1834ce30917a1dff6b2ad7d8ab29de95e7fc7eb83a1`.
- `replay.json`: `984ba0abc7b7d686c844cb31988598d85883bda492cea01d8da69b2139c87c6c`.

All eight controls and the separate dp-name digest check are terminal. No job or worker was launched or retained. Only this report and the owned three small artifacts were created. **STOP: order mechanism justified; installed-engine delta and any full solver require new authority.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14321`.
- Body SHA-256:
  `222e48e95fe2f1de024060129b6165bc7cbce27f21a5eb9f4d6ad85632f5768b`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
