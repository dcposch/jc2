# K16 square discriminant: duplicate equation and no additional cover ramification

2026-09-08. UNREVIEWED desk discriminator. **DUPLICATE / NO-GAIN at the
specified substitution and cover-count scope.** The proposed square is an
exact rescaling of the September6 nested-square equation. Its apparent second
quadratic cover is split on a hypothetical solution. Neither fact proves
nonexistence of the required polynomial solution; the original K16
`b=0, B*eta!=0` differential target stays OPEN. No new review lane is requested.

## 1. History checksum and exact scope

Read whole accepted boundary-product report and its Fable gate; whole prior
global-square and square-ramification reports; ueta §§2–7 (with adjacent
source conventions), f3abel §§6–7, and universal-series §§3–4.
Search was restricted to these named terminal histories and their title
discovery; no log body, raw/live report, protected tree or broad new survey
was read. Relevant history:
global-square §§2–3 already gives the exact nested square, full-degree
right side and failure of the other branch to remain rational;
square-ramification §§2–4 records the complementary-factor budget and
local-contact limitation; f3abel §7 and Series §§3–4 preserve the global
termination gap. None is promoted as a new obstruction here.

All seven input hashes are recorded in `input-pins.json`. The exact
closest source is
`xmodel/k16-global-square-discriminator-astra-20260906.md`,
SHA256 `ec8b5f36ace1ed47be7b615ce75295455e4bc6a93a71d11a75efcfa343883ba0`,
copied unchanged to `prior-global-square.md` in the owned box.

Use precisely the reviewed normalization `B=eta=1` over an algebraically
closed characteristic-zero field K, with moving nonzero leader
`lambda=lc A`, `deg A=m-2`, `deg W=q=2m-1`, `m>=4`,
`lc W=p lambda^2`, `p=1/[4(2d+1)]`, `3d^2=m`.
Both coefficient-field embeddings/factors are retained. No individual
leader is fixed by convenience. Origin markings are `W(0)=-1,W'(0)=1`.

## 2. Literal differential-polynomial identity and duplicate map

To avoid the previous note's different U notation, use the task's U and
call the old auxiliary variable T:

```text
U=x^3 A^2,
E=2xWW'-W^2+(3U/2-1)W-3U^2/16+3U/4+x,
S=U-4W-2,
F_W=(32/3)(xWW'+W^2+W)+(16/3)x+4.

V=2W+1,   T=U/2-V,   S=2T,
K_old=3T^2-2V^2-1-4x-2x(V-1)V'.

S^2-F_W = (4/3)K_old = -(16/3)E.                    (D)
```

These are identities with `W'` an independent formal symbol. They need no
division by a polynomial, coefficient, discriminant or selected root.
The source relation `U=x^3 A^2` becomes exactly the old
`T+V=x^3 A^2/2`, and conversely `W=(V-1)/2`.
Thus no equation or polynomiality hypothesis has been added or removed.

For reference only, the existing infinity balance transports literally:
`deg F_W=2q`, leader `(32/3)(q+1)p^2 lambda^4`, while
`lc S=(1-4p)lambda^2`. The equality of these leaders is exactly
`(2q-1)p^2+3p/2-3/16=0`, the known UT.
Here `1-4p=2d/(2d+1)!=0` on both factors. This is not a new residue,
degree inequality, or polynomial-abc argument.

## 3. Precise failure of the extra-double-cover count

On any hypothetical solution, in the rational function field K(x),

```text
U = x (xA)^2,       F_W=S^2,       S(0)=2.
```

Consequently adjoining `sqrt(U)` gives exactly `K(x)(sqrt(x))`;
adjoining `sqrt(F_W)` gives no further field extension. More explicitly,
the generic algebra for the latter cover is
`K(x)[z]/(z^2-S^2) = K(x) x K(x)`.
The combined generic algebra is two copies of `K(sqrt(x))`, not a
connected degree-four field.

This claim uses explicit maps, not an imported ramification theorem.
Write `x=t^2, y=t^3 A(t^2)`; then `y^2=U(x)` and
`t=y/(xA(x))` in the function field. The smooth completed parameter curve
is the t-line with infinity, and the map is exactly `x=t^2`.
Its only ramification places are t=0 and infinity, each index2.
At a nonzero finite root a of A of arbitrary multiplicity r,
`ord_a U=2r`; at0 it is `3+2 ord_0 A`; at infinity it is
`-q`, with q odd. These account for all places without squarefreeness.
Roots of S give crossings of the two split branches, not new ramification
after normalization. Common A/S roots likewise change no generic extension.
The old norm model's special x=-3/4 is nonzero here and remains unramified
in `x=t^2`, regardless of whether A or S vanishes there; it cannot be
silently counted as a new branch point of this different cover.

The first invalid arrow of the proposed naive cover count is therefore
“the discriminant square supplies a second independent connected double
cover.” Counting distinct zeros of F_W as branch points would make the
same mistake: every such valuation is even. This does NOT exclude a more
subtle rational-map argument using the differential dependence of F_W on W.
That dependence, under (D), is exactly the still-unresolved entire E=0.
No new universal inequality has been established, and no claim that every
Mason/ramification method must fail is made.

## 4. Tiny controls and terminal custody

Owned stdlib `check.py`, SHA256
`cbdd1f3d687c3df9512845518ecc97bdba3216e3f6fcb28fb2f3eba0100f4cc8`,
checks the four formal identities using rational coefficients and total
formal degree at most3. It constructs no actual source polynomial.
Both changed-object modes, `--omit-W` and `--wrong-x`, mutate the candidate
right side and are rejected by the literal residual comparison.
Positive and both mutations ran normally and with -O:
six declared modes behaved as required, elapsed1.385s, each capped at
30wall/25CPU/512MiB; no gating Assert is present. Commands/stdout/stderr/rc
are in `replay.json`. The cover proof is the explicit parameter map above,
not a sampled numerical or finite-degree source test.

This packet is confined to
`box/k16-square-discriminant-ramification-discriminator-20260908/`
and this transactionally published report. Inputs were not changed.
No CAS, AWS/SSH, full reconstruction, finite-m solver, additional lane,
canonical edit or external theorem import occurred. All children and writers
are terminal at handoff. STOP/IDLE.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6077`.
- Body SHA-256:
  `6c0a1e79b73111ea27014c125a7c37f6e0e297262c418be25feb728fcfb7d75f`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
