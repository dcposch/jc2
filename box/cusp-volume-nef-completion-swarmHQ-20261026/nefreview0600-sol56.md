# NEFREVIEW0600 — independent finite-boundary completion audit

Status: PASS / INTERNAL / MANUAL / INDEPENDENT REVIEW.
Launch basis: a5cf1925fefb68c5990c08214e163b3f7f5a97ff.
Public basis: c3a384e1ce42e65fcbbe26ee711e84be6f05cb23.

## Verdict

At the adopted DIVISORIAL scope, NORMALIZEDV0535 correctly defines a finite quantity

    M_C=c/t_0=max{a, max_(p_j<0)c(-p_j)/z_j},
    t_0=min{c/a, min_(p_j<0)z_j/(-p_j)},                           (1)

and proves

    I(Y,B) <= I(W,C) <= M_C^2,    I(Y,B)>0.                       (2)

The interval defining t_0 is exactly the simultaneous EFFECTIVITY+NEFNESS interval for
the chosen ray rho*C+tP. It is not the unrestricted nef threshold. The strict estimate
M_C<sqrt(I(Y,B)) remains unproved; no external-invariant, infinitely-singular, or JC2
conclusion follows.

## Coefficients, positivity, and every source block

On a full smooth compact resolution rho:X->W, write

    rho*C=C'+sum z_j A_j,    P=sum_(j over cusp p)p_j A_j.

Because C is effective Q-Cartier, z_j>=0 on all exceptional blocks. On the cusp block,
z_j>0: a local equation of neC vanishes at p and has positive order at every divisorial
valuation centred there. The cusp maximal nef part P is nonzero, exceptional-nef and
coefficientwise nonpositive. Projection gives

    a=-P.C'=sum_(j over p)z_j(P.A_j)>0.

Every term is nonnegative; at least one is positive because the cusp intersection matrix
is invertible and P is nonzero. On an embedded resolution of the unibranch cusp, C' meets
one component A_b once, so a=-p_b. Other ambient singularities along smooth points of C
are allowed: P is extended by zero there, while their z_j remain in rho*C.

## Exact effective-plus-nef interval

Put H(t)=rho*C+tP. Its C' coefficient is one; cusp-exceptional coefficients are
z_j+t p_j, and coefficients on all other blocks remain z_j>=0. Thus H(t) is effective
exactly for 0<=t<=q_C=min z_j/(-p_j). On exceptionals,

    H(t).A_j=t(P.A_j)>=0,

with zero on other blocks, while H(t).C'=c-ta. Every other irreducible curve is not a
component of the effective support, so has nonnegative intersection. Hence H(t) is both
effective and globally nef exactly for 0<=t<=t_0. For t>q_C only effectivity is known to
fail; the proof correctly does not claim nefness fails there unless t>c/a.

At t_0, nefness on the smooth projective X gives

    0<=H(t_0)^2=c-t_0^2 V_W(p),

so I(W,C)=cV_W(p)<=c^2/t_0^2=M_C^2. The reviewed finite comparison and
B^2=eC^2 give I(W,C)>=I(Y,B)>0, establishing (2).

## Resolution invariance and normalized consumer

Under further point blowup, rho*C and P pull back, so H_new(t)=sigma*H(t). Birational
pullback preserves effectivity and nefness. More concretely, a new exceptional ratio is
a weighted average of old z_j/(-p_j), or increases when the centre lies on C'; old
components persist. Thus q_C, a, t_0 and M_C are unchanged. Common refinements give
model independence.

With m=ne and c=1/m, each mz_j at the cusp is a positive integer, hence

    c(-p_j)/z_j=(-p_j)/(mz_j).

This is denominator control only. The adopted data say mC is Cartier, not that m is the
exact Cartier index, and supply no numerator bound on -p_j. Therefore the finite strict
conditions a<sqrt(I(Y,B)) and c(-p_j)/z_j<sqrt(I(Y,B)) remain genuinely unproved.

## Full-block adjunction scope

Let s count every exceptional contact with C' on a full compact SNC resolution and let
L_full=P_full+N_full be decomposed blockwise. Adjunction and numerical projection give

    L_full.C'=s-2-R.C,
    sum_(all contacting blocks)(-P_block.C')=2-s+R.C+N_full.C'.    (3)

Since N_full.C'>=0, (3) is valid without suppressing other source singularities. Its left
side is not automatically the cusp a. Only under the additional one-contact hypothesis
s=1 with the cusp block sole does it specialize to a=1+R.C+N_full.C'>=1. That hypothesis
is not adopted. The q-only singularity statement applies to target Y, not source W.

## Custody and limits

Measured recovery ACK: 2026-10-26T05:59:21.201883Z. Whole launch STATE194 completed
2026-10-26T05:59:34.662479Z and matched launch STATE. All36 fixed inputs passed before
mathematics. NORMALIZEDV88 was canonically verified and read whole. Accepted parent V and
finite lower comparison were used only at reviewed scope.

The initial metadata probe used my inferred shorthand `runtime/nefreview0600-STATE.md`;
that path was not dispatched and did not exist. I immediately recovered the canonical
`runtime/nefreview0600-launch-state.md` from the fixed registry. No mathematical impact.
No source/history query, new bound design, control, paid/CLI/cloud action, child, protected
access, shared/public/Git edit, promotion or successor occurred. Exact windows, reuse,
postpins, charges and collision custody are in companion receipts.

OPEN(S) RAISED
None. The strict normalized comparison is the existing retained gap.

## COLLISIONS
Terminal frozen-public collision custody is recorded separately after sealing.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4981`.
- Body SHA-256:
  `8e93efc99f2ba1ccb22d97dcbc5f0b78527d82abc251b98580f3a634deb826b3`.
- Frozen basis: `a5cf1925fefb68c5990c08214e163b3f7f5a97ff`.
