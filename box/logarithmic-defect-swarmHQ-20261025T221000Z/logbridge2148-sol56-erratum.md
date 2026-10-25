# LOGBRIDGE2148 — erratum to independent hostile review

Status: ERRATUM / PASS_CONDITIONAL RETAINED / INTERNAL / MANUAL.
Launch/report basis: 0c400ae8e72550d822f7783472e082e1d96ca409.

The sealed review incorrectly states that

    K_Z-f*(K_S+D)=-f*D

and consequently changes the strict-C coefficient from -1 to -e. I withdraw both
statements. They omit the differential ramification divisor. For the generically finite
morphism of smooth surfaces,

    K_Z=f* K_S+R_f,
    K_Z-f*(K_S+D)=R_f-f*D.

At generic C, f*D has coefficient e and R_f has coefficient e-1, because the normal
ramification index is e and the residue extension is separable. The difference is -1.
Equivalently, Delta=K_S+D has no strict-B component, so f*Delta has no strict-C
component, while div(Omega_Z) has coefficient -1 there. The original TOPIDEAL2135 line
was correct.

This correction does not affect the H2-vanishing argument: a dual section still has a
negative coefficient along strict C, and its birational pushforward lies in I_B, whose
global sections vanish. Therefore the one-sided conclusion

    h1(Z,f*omega_S(D))=e-1-Delta.c1(V)>=0,
    Delta.c1(V)<=e-1

and the report's PASS_CONDITIONAL verdict survive. The residual inequality (6), the
provisional sheet budget, their combination, and JC2 remain expressly uncertified.

The original report, manifest, coverage, result, partial, and collision receipts remain
byte-identical and visibly retain the error. This erratum relies only on the original 47
pinned inputs plus `runtime/logbridge2148-root-ramification-check.md`, read whole as
5 LF/1060 bytes/SHA-256 aa69bb94a451786c9a14e3d74db5a682397af072fb1965d8ee4a5ddb4a30f5b8,
mode0664. No source, history query, family, CAS, paid/cloud work, child, Git mutation,
or public/shared/protected edit was used.

OPEN(S) RAISED
None.

## COLLISIONS
Terminal frozen-public collision custody is recorded separately after sealing.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `1935`.
- Body SHA-256:
  `0e793815d46b7d48e3bcc86bc9d3f33a9755689b725326dc649e70a1648288c6`.
- Frozen basis: `0c400ae8e72550d822f7783472e082e1d96ca409`.
