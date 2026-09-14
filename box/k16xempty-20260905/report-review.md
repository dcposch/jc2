# Bounded hostile review of the unsealed K16 X report

Reviewer: Astra `/root/uniform`, 2026-09-05.
Read: `xmodel/k16-xempty-astra-20260905.md`, approximately 38.55 KB,
including Sections 1–9. No CAS was used in this review and no report
body was edited.

**Verdict: the finite characteristic-zero argument, literal chart
transport, and final dependency chain are mathematically sound as
written, subject to the stated independently audited arithmetic
artifacts. Uniform emptiness is correctly left OPEN. Two concise
wording fixes are recommended in Section 7.3 before sealing.**

## Required precision fixes in the inserted uniform material

1. Add at the start of Section 7.3: **“Assume B eta != 0 throughout this
   subsection.”** The later b-chart arguments state this hypothesis,
   but the opening claim says the zero curve is rational for fixed
   b,B,eta and its formulas work “for every parameter value.” At
   b=B=eta=0 the open zero curve is empty, so the unconditional opening
   is too broad. The entire intended target already has B eta invertible;
   this edit only makes that hypothesis explicit.

2. Replace **“Geometrically the plane quartic has a triple origin,
   which is the part removed by xL nonzero.”** with **“The plane quartic
   has a triple origin, which the open condition xL != 0 removes.”**
   The original wording can assert that the triple origin is the whole
   removed locus. For b != 0, the point (x,L)=(0,-2b) also lies on
   Rfree=0 and is removed by xL != 0. No finite-algebra proof uses the
   inaccurate exclusivity: the graph has L(0)=-b and R(0)=-3b^4/16.

There are no broken internal numerical cross-references in the inserted
Section 7. Its equation labels remain unique. “It remains open in these
notes” could be changed to “It remains open here” for style, but that is
not a mathematical issue.

## Audited logical points

- Section 3 uses the legitimate finite-matrix route. The checked minor
  is a minor of the exact characteristic-zero matrix with a declared
  reduction and p-unit denominators. Its nonzero modular determinant
  proves its exact determinant nonzero. Surjectivity onto the entire
  declared weight piece then contains the actual T^2 target. This is
  stronger than matching a modular target rank and does not claim to
  lift radical membership or affine emptiness. The adjugate expression
  is an exact finite certificate even without expanded decimal
  coefficients.
- The quadratic field representation with e=3d is correct. At t=3,4,5
  the fields are irreducible, so the exact field calculation covers both
  embeddings. No split-factor conclusion is taken from only one factor.
- In Section 4, homogenization of T^2 to b-degree m gives
  Delta^(m-4) H^4. The main multiplier u^4 Delta^(8-m) yields
  (u Delta H)^4. Thus the m=6 and m=7 specializations and the geometric
  series terms have the right exponents and signs.
- The boundary formula follows from eta-B=A-bDelta and gives B^4
  exactly. Its A and Delta cofactor signs are correct. It keeps eta as
  a reconstructed polynomial.
- The general transport inequality follows by adding the weighted
  bounds on deg_b(a_k) and deg_b(E_k). It ensures m<4n, so every claimed
  main exponent is nonnegative. The boundary n formula has the correct
  factorization and sign.
- Section 6's intrinsic H identity, open/closed radical equivalences,
  and gluing exponent r(s+1) are valid. The ambient derivative is not
  improperly asserted tangent to the terminal scheme.
- The finite-algebra maps in Section 7.3 keep nilpotents. On b!=0,
  x and L are units modulo R and v and g are units modulo Q. On b=0,
  removing R's exact x^3 factor and Q's exact g factor gives matching
  lengths and retains the distinguished marked behavior. The count
  supplies no d-integrality constraint, as the report correctly says.
- Section 8 uses the positive row ideal and homogeneous tau with its
  constant shift. The cone lemma needs neither V0 nor properness of the
  affine chart. The final inference to theorem (T) is explicitly
  conditional on the banked reconstruction and spine arrows.
- The t>=8 residual is supported by the frozen
  `k16-8point1-astra-20260905.md`, lines 1061–1064, which explicitly banks
  **(8.1)** through t=7, rather than merely an unrelated theorem (T)
  proof. The report also states the t>=6 version if those banked indices
  are not consumed.
- The t=2 correction is necessary and correctly stated. A nonempty
  positive cone with B=eta=0 is compatible with empty U and X.

No all-t statement is promoted by the finite certificates, the t-free
differential equation, the rational quartic transform, or the failed
descent. Final process shutdown and sealing remain the primary agent's
operational check; the body was unsealed when reviewed.
