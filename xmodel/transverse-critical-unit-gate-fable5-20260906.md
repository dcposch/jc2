# Gate: transverse critical-point unit and explicit final C pivot

2026-09-06 12:57Z. Gate: Fable 5.1 (different model from producer Astra),
lane /tmp/jc2-lane.w1E8LW. Evidence: independent desk re-proof, own exact
symbolic controls (sympy, 1.4 s, normal mode, 30 s/512 MiB rlimits), producer
replay. No AWS, no jc2-lean, no heavy CAS, no ledger/tool/source edit, no
external post, no 190-row expansion.

Verdict: PROMOTED WITH FIX. Claims (1)-(4) are each CONFIRMED in exactly the
producer's stated scope, with claim (2) read under the author's correction
below. The producer's original bytes are unchanged; the fix is a reading of
one phrase, recorded here, not an edit.

All five charged inputs hash-match charged-inputs.list and the repo copies
(2fe9bfa8..., a0911458..., 8cf51bd8..., e34021ea..., e47fd16c...). Replay of
box/transverse-critical-unit-20260906/replay.py: rc 0, 0.44 s,
status PASS_NORMAL_ONLY, output SHA256 bbc8a29a...

## The fix (claim 2 wording)

The producer writes "n constant positive-row pivots on V0 with invertible
constant matrix M" (report line 35-36). The entries of M are NOT constants:
in the W-adapted basis, column P=W^r p_r+..., row (i'+1,r'-1) with r'>r
carries coefficients of G's W^(r'-r) and higher slices, and same-r rows below
the diagonal carry l=G's X-coefficient at W=0. My toy instantiation (8
columns X^i W^r, r=1,2, i=3..0, generic symbolic G with slices g1,g2,g3)
gives strictly-upper block zero, diagonal (-2,-2,-2,-2,-4,-4,-4,-4), 16 of
28 lower entries non-constant (samples -l, g2_1, 2 g1_1), det = 4096 =
prod(-2r). So the correct hypothesis is: M is lower triangular over the
base A with constant nonzero diagonal -2r, hence det M in Q*. The
block-determinant proof uses only det M in Q* and the exact zero block; it
never uses constancy of entries. With this reading the argument is valid.
The W190 lemma itself was gated earlier (linear-c-transverse-gate-fable5,
claim 4) exactly in this triangular-constant-diagonal form, so the
dependency is consistent with the fix.

## Claim (1): Delta is a unit in the full Keller quotient. CONFIRMED

G(X,0)=X^2+lX+m forces G_X(s,0)=2s+l=0 at s=-l/2, so J(s,0)=F_X(s,0)Delta
exactly, and J(s,0)=sum_i s^i J_i0 (finite). Hence in A[Z]

    1 - Z F_X(s,0) Delta = -(Z J_00 - 1) - Z sum_{i>=1} s^i J_i0,

a literal polynomial identity. Verified with F of X-degree 4, W-degree 3 and
G with three generic W-slices, all coefficients free symbols (identity holds
in Q[36 symbols][X,W,Z]); and over the nilpotent base Q[eps]/(eps^2) with
every coefficient a+eps*b (holds mod eps^2). Base change is a ring map, so
nilpotent and non-reduced Q-algebras are covered; only 2 invertible is used.
Inverse: Delta^{-1} = Z F_X(s,0) in B.

Refinement the producer does not state: the identity uses ONLY the inverse
relation and the W=0 rows J_i0, i>=1. The W>=1 positive rows are not needed.
Both of the used pieces are essential, by mutation:
- drop the inverse: F=G=X^2+W^2 has every J_ij=0 and Delta=0;
- drop the single row J_10: F=X, G=X^2+2X+(X+1)W has J=X+1, J_00=1 (unit),
  J_10=1, all other rows zero, Delta=G_W(-1,0)=0. So the quotient lacking
  one W=0 row does not force Delta invertible.
- at l=0 no positive row is needed (J_00=F_X(0,0)Delta directly).
The producer's caveat (line 23-24) is therefore right as worded: the
licence is for the complete quotient, or any sub-quotient containing the
inverse relation and every W=0 row, and for nothing smaller.

## Claim (2): evaluation row and block determinant. CONFIRMED (with fix)

For C in V with C(X,0)=beta X+gamma: J(C,G)(s,0)=C_X(s,0)Delta-C_W(s,0)*0
= beta Delta; on V0 (C(X,0)=0) it is 0. Both are exact polynomial
identities (checked with symbolic C, G). Appending the evaluation row to the
190 pivot rows, V0 columns first and the X-vector column last, gives
[M v; 0 Delta] with the zero block exactly zero and v non-constant; my toy
9x9 has det = det(M)*Delta symbolically. On B this is a unit by claim (1).
Mutations: adding X^3 to G (cubic restriction) makes the zero block nonzero
(G_X(s,0)!=0); adding X^2 (leading coefficient 2) keeps triangularity with
diagonal -4r, so "monic" can be relaxed to a constant nonzero leading
coefficient but NOT to a base-variable leading coefficient (s would need
its inverse and the 0 block would be lost).

The evaluation row is sum_i s^i * (row X^i W^0), an A-linear combination
of W=0 rows INCLUDING the constant row J_00 (weight s^0=1). So the
191-row system is not a 191-minor of the original coefficient matrix, and
it does involve the constant Jacobian coefficient, consistent with the
producer's statement that the identity needs the inverse relation.

## Claim (3): localized graph reconstruction of beta. CONFIRMED, no cost win

Exact identity (checked symbolically):

    beta - (J_00 u - F0_X(s,0))
      = (beta + F0_X(s,0)) (1 - u Delta) + u sum_{i>=1} s^i J_i0,

so beta = j u - F0_X(s,0) holds in B[u]/(u Delta - 1) with j=J_00, and
B -> B[u]/(u Delta-1) is an isomorphism because Delta is a unit in B. No
Keller stratum of the COMPLETE quotient is lost. But J_00 itself depends
on beta (coefficient G_W(0,0), the toy's g0_1), so j is not a graph
coordinate unless introduced as a fresh variable with relation j=J_00.
Accounting: beta removed (-1); u added with u Delta=1 (+1, a relation of
degree deg Delta+1 in the base); j added with j=J_00 (+1) or kept rational
as 1/Z. The polynomial-presentation variable count does not decrease.
F0_X(s,0)=F0_X(-l/2,0) has X-degree many terms in l, so substitution
fills in. The producer's non-claim of a cost win is correct.

## Claim (4): D108 sign formula. CONFIRMED as hypothetical input only

With h(X,0)=-X+c, D(X,0)=d1 X+d0, G=h^2-(b/3)h+D, symbolic W^1 jets
hw_i, dw_i: G(X,0)=X^2+(b/3-2c+d1)X+(c^2-bc/3+d0), s=c-b/6-d1/2,
Delta=d1 h_W(s,0)+D_W(s,0)=-J(h,D)(s,0). Flipping the sign to +J(h,D) is
detected. General form: Delta = J(h,D)(s,0)/h_X(s,0), so the (99,66) sign
h(X,0)=+X+c gives Delta=+J(h,D)(s,0) (checked). The literal D108 jets, its
14 residuals and whether Delta is nonzero there are NOT gated here; the
producer says the same (lines 67-70, 79-81).

Cheapest actual D108 discriminator (minutes, no solve): read only the W^0
and W^1 rows of h and D from the D108 stage JSON (four univariate
polynomials in X over the base); confirm h(X,0)=-X+c literally and D(X,0)
linear; form Delta=-J(h,D)(s,0) as a base polynomial. If Delta is
identically 0, claim (1) makes B=0: the complete Keller quotient of that
chart is empty, a kill. If not, test whether Delta reduces to 0 modulo the
14 source residuals (normal form, then a random-point lift as non-vacuity
control per FALLACY-v2 remainder rule); count terms of Delta and of
F0_X(s,0) for the pivot-cost estimate.

## Limits, FALLACY-v2, OPEN

- Cost: M^{-1} over A is adj(M)/det M with dense degree growth up to 189
  in the base; the lemma licenses one pivot, not a cheap inverse.
- Localizer: only Delta, and only on the complete quotient (inverse + all
  W=0 rows). Nothing licenses Delta!=0 on positive-only or W>=1-only rows.
- Constant C column: J(1,G)=0; it is the additive-constant kernel, never
  pivoted, never removed by this lemma.
- Not closed: properness, source coverage, existence of a Keller point,
  D108 unit result. J_00=1 cannot be set in the monic family without a
  gauge; Z stays a variable.
- Variable/ring map: X,W,Z plus symbolic coefficients over Q; nilpotent
  test over Q[eps]/(eps^2); no sat(), no remainder-degree, no pole or exit
  reasoning; no charge_basis line (no new exit-price assertion).
- OPEN[D108-LITERAL-JETS]: h(X,0)=-X+c and D(X,0) linear unverified here.
- OPEN[W-ADAPTED-EMISSION]: the 190-column source transform and its
  benchmark remain unemitted (unchanged from the prior gate).

Artifacts, owned, read-only after this report:
box/transverse-critical-unit-gate-fable5-20260906/gate_controls.py
(afd20613...), gate_controls.out (5d8ab0c4..., 24 true / 0 false),
replay.out (bbc8a29a...). Replay: python3 -B gate_controls.py from that
directory; needs only sympy.

<!-- BODY-END -->
