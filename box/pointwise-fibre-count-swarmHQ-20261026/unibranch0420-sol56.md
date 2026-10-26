# UNIBRANCH0420 — independent fibre-count review

Status: PASS / INTERNAL / MANUAL / INDEPENDENT REVIEW.
Launch basis: ebb207b42c775325a2d5bacfcf05002673f9a8cd.
Public basis: 90cd180f8053240bcdced2bcb530a12ac8b07d58.

## Verdict

Assuming the accepted all-Keller sheet-budget theorem, the ROOT identity is exact. For
each target point y,

    n_y = 1 + sum_i r_i delta_i (1-b_i(y)) + S_off(y),             (1)

where n_y=#F^-1(y), b_i(y) is the number of normalization branches of the individual
irreducible D_i over y (zero off D_i), and S_off(y) is the nonnegative slack supported
away from the fibre over y. Consequently, an omitted target point must be multibranch
on at least one individual irreducible nonproper-value curve. A crossing of distinct
unibranch components is insufficient. If every individual D_i is everywhere unibranch,
F is surjective. No properness, injectivity, JC2, or novelty conclusion follows.

## Fibre decomposition

Finite flatness of h:X->A2 gives total fibre length e. On the open whole source U,
h=F is étale, so every source point over y has local length one. The omitted E_i are
disjoint, hence

    e = n_y + sum_i sum_(x in E_i, h(x)=y) m_x.                   (2)

This remains correct when the fibre has no U-point or no omitted point; the corresponding
sum is empty. Repeated image curves cause no merging because E_i remain distinct source
components and are indexed separately in (2).

Write w_i=r_i delta_i and s_x=m_x-r_i t_x>=0. The accepted exact slack identity is

    S:=sum_(i,x)s_x=e-1-sum_i w_i.                                (3)

For the finite bijective normalization A1->E_i, the map to normalized D_i is a degree
delta_i polynomial g_i:A1->A1. For every normalization point z over y, the sum of local
degrees in g_i^-1(z) is delta_i. There are b_i(y) such z, and bijectivity supplies a
unique normalization preimage for each point of E_i. Therefore

    sum_(x in E_i, h(x)=y) r_i t_x = w_i b_i(y).                  (4)

This includes singular points of E_i and self-intersections of D_i; local degree is taken
on the normalization. If two E_i share the same D, equation (4) is applied independently
to each indexed source curve, exactly as required.

Substitute m_x=r_i t_x+s_x in (2). The slack on the fibre equals S-S_off(y), so

    e-n_y=sum_i w_i b_i(y)+S-S_off(y).

Using (3) gives (1), with no lost multiplicity or assumed unramified sheet.

## Localization and exact scope

If every individual D_i through y is unibranch, b_i(y)=1 there; off D_i it is zero.
Equation (1) reduces to

    n_y=1+sum_(i:y notin D_i)w_i+S_off(y)>=1.

Thus n_y=0 forces b_i(y)>=2 for some single D_i containing y. Multiple distinct smooth
or unibranch D_i crossing at y each still have b_i(y)=1 and cannot alone cause omission.
If every D_i is unibranch at every point, the same argument for every y proves only
surjectivity of F. It does not make the quasi-finite map finite or proper.

The zero-boundary case also checks: with no E_i, (3) gives e=1 and (1) gives n_y=1.
With omitted curves but y off all their images, (1) gives n_y=1+sum_i w_i+S_off(y).
No stronger geometric assertion is hidden in these edge cases.

## Custody and limits

ACK: 2026-10-26T04:22:35.509725Z. Whole launch STATE345 completed
2026-10-26T04:22:51.273193Z and matched launch STATE. All21 fixed inputs passed before
mathematics. Both canonical math artifacts verified; ROOT proposal48 was read whole.
The accepted all-Keller theorem is a dependency, not re-audited here. Own unchanged
governance/helper coverage is reused only at exact fixed hashes and cited in coverage.

No history query, additional preview, external source, web, CAS, paid/cloud/CLI action,
child, protected-tree access, shared/public/Git edit, or successor occurred. The prior
searches are routing only and establish no novelty. Exact windows, read charge, postpins,
canonical custody and terminal collision evidence are in companion receipts.

OPEN(S) RAISED
None.

## COLLISIONS
Terminal frozen-public collision custody is recorded separately after sealing.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4076`.
- Body SHA-256:
  `d9d19fed95990117fa9a8be6bcfd4f5711705a36c8012e63f5cce224e8863813`.
- Frozen basis: `ebb207b42c775325a2d5bacfcf05002673f9a8cd`.
