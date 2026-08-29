# Registration: H17/q7/a3 affine-Faber grade-48 predecessor

Date: 2026-08-26

Status: preregistered fixed-representative producer; no theorem.

## Question

At the upper/lower H17 wall

```text
normal H=17, kernel q=7, center alpha=3,
kernel complements=14, affine load graph=42,
graph deviations d6,d2,dm=48, target mu4=d4=48,
intrinsic/center/load successor=51,
```

classify the complete first predecessor at absolute grade 48 before using
the grade-51 functional `K=E*H3+H5`.

The source replay must retain:

1. all seven frozen ordinary-Faber rows;
2. the exact affine graph with arbitrary `E` and `K10` jets through the
   only six relative grades which can reach grade 48;
3. both kernel coordinates `X,Y`, all four complements `R0,R1,S0,S1`,
   and the leading moving center and first-normal coefficient;
4. all three grade-48 graph deviations
   `d6=K6-(15/32)K10*E^2`,
   `d2=K2-(15/256)K10*E^4`,
   `dm=mu2+(5/4096)K10*E^6`;
5. the independent grade-48 target `d4=mu4`.

The compiler must verify all seven rows vanish below grade 48, print the
entire grade-48 block, eliminate `d6,d2,dm,d4`, and test both projective
kernel charts on `D(p*m*x)` and `D(p*m*y)`.  It must also verify that
moving `E`, `K10`, and center jets which have positive excess do not enter
the face.  Exact Q is evidence; F65521 is a collection/software control.

## Stop conditions

- If either chart is a unit, freeze the exact certificate and proceed to
  hostile review.
- If the face survives, freeze its exact residual ideal/representatives
  and build the smallest correction-complete grade-49--51 successor.
- Any engine error, timeout, hash mismatch, missing sentinel, or Q/prime
  structural mismatch is no verdict.

## Scope firewall

This client is only the fixed integral `(H,q,alpha)=(17,7,3)` normalized
graph predecessor.  It does not prove rational-regrading invariance,
literal source or total-Rees coverage, another load schedule, order two,
maximum twelve, or JC2.
