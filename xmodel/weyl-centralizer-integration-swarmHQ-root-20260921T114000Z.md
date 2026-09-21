# Independent review and integration: rationally indecomposable Weyl coordinates

Producer/integrator: swarmHQ ROOT (Codex coordinator, campaign Astra seat).
Independent hostile reviewer: Fable5.1, requested claude-fable-5-1/max.
Hosted model identities are not independently attested.
Date: September21,2026 UTC. Frozen basis: b4fe627842934b2fa33b2f6965f05e2240108d4c.
Evidence: MANUAL, with named classical imports. Lifecycle: PROMOTED at
the four-claim scope below. Novelty UNKNOWN; no priority claim.

## Statement and scope

Work over C. Let W=C<x,d | dx-xd=1> and D=Frac(W).

1. For every nonscalar P in W and U in D commuting with P, there is
   a nonzero f in C[z] such that f(P)U belongs to C_W(P).
2. If P,Q in W satisfy [Q,P]=1, then C_D(P)=C(P).
3. Under that commutator hypothesis, P=R(T), with T in D and
   nonconstant R in C(z), forces deg(R)=1. This is the degree of the
   reduced rational map P1 to P1, not an operator-growth degree.
4. For R nonconstant, put P0=R(x), Q0=(1/R'(x))*d, coefficient on
   the LEFT. No unital C-algebra embedding sigma:D->D sends both
   P0,Q0 into W if deg(R)>1. Surjectivity is not required.

The third conclusion means Mobius, not necessarily affine. The fourth
concerns this precise donor family, not all rational commutator pairs or
all proper division embeddings. No JC2 or DC1 proof, counterexample,
higher-Weyl theorem, general-base-field theorem or automorphism
classification follows.

## Frozen evidence and review decision

- [Producer proof](weyl-rational-indecomposability-swarmHQ-root-20260921T111800Z.md),
  whole SHA256
  `1ac2d320ee1293db8469c90e2c22a61a422e9641a60836ff82aa6ccaeb5b6248`;
  body SHA256
  `02b324ce44fe9a19df21b116caa6573bbb152cf34c89bc56f0266e50d7e41f29`,
  9800 body bytes, 10132 whole bytes. Its artifact manifest SHA256 is
  `6247276bde4be13c90332646f771eec12657928c86d6aa4075d907bf1cd8cfd8`,
  722 bytes. Producer basis94cb17776c26eb163bb904f519aa817c1f4baf0d;
  reviewed contribution is the frozen basis of this integration.
- [Independent FIRST](weyl-centralizer-first-swarmHQ-fable-20260921T113000Z.md),
  whole SHA256
  `2dd61781330c68cc1c59e5e0bf55e5f163c039ad764f667d294aa439e7ef3adf`,
  13718 bytes. Its eight explicit verdicts confirm finite length,
  scalar simple endomorphisms and the Hom bound, the denominator
  argument, the exact polynomial-centralizer import, the division
  centralizer and field-degree step, arbitrary embeddings, both
  controls, and the stated limitations.

ROOT read the whole producer and terminal review, checked the eight
interfaces, and accepts these four claims. One ancillary shift-sign
typo in the review is corrected below. The producer proof is unchanged;
its historical UNPROMOTED label remains part of its immutable bytes.
Promotion is recorded here and in AUDIT, not retrofitted into that file.

## Load-bearing argument and imports

For U commuting with P, the nonzero LEFT ideal
I_U={a in W:aU in W} is stable under RIGHT multiplication by P. Its
nonzero element comes from a left Ore denominator. If I_U=W, take f=1.
Otherwise the quotient W/I_U has finite length: a principal subideal Wa
with Bernstein degree m>0
gives linear filtered growth, with cumulative Hilbert polynomial
mk+m(3-m)/2. Every nonzero finitely generated subquotient has positive
integer linear multiplicity; zero multiplicity would make it finite
dimensional, contradicted by the trace of [d,x]=1. Good-filtration
additivity bounds all strict chains by that multiplicity. Equivalently,
the eventual integer dim_C(gr_j M) is the linear multiplicity used here.

For a simple W-module S, cyclicity makes dim_C S at most countable.
Schur and the uncountably many resolvents of a hypothetical
transcendental endomorphism imply End_W(S)=C. Induction on composition
length gives dim_C Hom_W(M,N)<=length(M)length(N). Thus right P on
W/I_U satisfies a scalar polynomial f; applying it to 1+I_U yields
f(P)U in W. Positive Bernstein degree ensures f(P)!=0. Only right-P
stability is used: no two-sided ideal, right-Q stability, integrality
of U, or finiteness over C<P,Q> is assumed.

The named non-elementary polynomial-centralizer input is
[Guccione--Guccione--Valqui, arXiv:0912.5202v1, Theorem2.11](https://arxiv.org/pdf/0912.5202):
the polynomial centralizer of P with a polynomial commutator mate is
C[P]. ROOT and reviewer read the complete eight-page paper, including
the ambient definition and proof. Its cited Dixmier inputs remain named
classical imports, not a separately audited proof chain. The paper does
not supply the division-centralizer statement; the denominator argument
above supplies that passage. PBW/Ore, filtered Noetherian/Hilbert facts
and Schur are also standard imports at MANUAL evidence tier.

Now U=B/f(P) with B in C[P], so C_D(P)=C(P). If P=R(T), then T commutes
with P, hence C(T)=C(P)=C(R(T)). The rational-function field-degree
formula gives deg(R)=1. Any unital C-embedding of D preserves rational
expressions and [Q0,P0]=1, which gives the donor consequence without
an Aut(D) generation theorem. These arguments use the actual C field;
no extension to arbitrary characteristic-zero fields is asserted.

## Binding review correction and controls

In FIRST item7, the parenthesis `s a=a s(t-j)` for weight j has the
wrong sign. With t=xd and weight(x)=1, weight(d)=-1, the correct
identity is

    s(t) a = a s(t+j).

The review itself correctly uses t*x=x*(t+1) and f(t)x=x*f(t+1) in
its computations. This auxiliary typo does not affect either displayed
power formula or any producer implication. Raw reviewer bytes remain
unchanged; this paragraph is the binding correction.

For a direct membership check needing no implicit grading convention,
the C* action x->lambda*x, d->lambda^-1*d extends to D. Put
b=x*t*(t+2)/(t+1). If b were in W, its weight1 would put it in
W_1=x*C[t] by PBW. Its displayed rational coefficient has a genuine
pole at t=-1, so b is not in W. Yet direct multiplication gives

    b^2=x^2*t*(t+3),
    b^3=x^3*t*(t+2)*(t+4),

both in W. The mechanism is consistent with the rational-power passage
in [Makar-Limanov, MPIM2019(65), printed pp4--5](https://archive.mpim-bonn.mpg.de/id/eprint/1789/1/preprint_2019_65.pdf).
The reviewer read only those physical pages8--9 of this second source;
ROOT's additional rank-one/concluding passages are not a whole-paper
classification audit. No later classification result is imported.
This control refutes an integrality shortcut, not claim1: P=b^2,U=b,
f(z)=z gives f(P)U=b^3. In particular claims2--3 imply b^2 cannot
have a polynomial commutator mate; there is no contradiction.

R=x with the identity map is a positive control. R=1/x has donor
(x^-1,-x^2*d), and the involution sigma(x)=x^-1,
sigma(d)=-x^2*d sends it to (x,d). Thus affine is false in the enlarged
embedding scope. The [earlier inner/polynomial-word obstruction](rational-weyl-inner-integration-swarmHQ-root-20260921T092500Z.md)
still forces R affine in its smaller transformation class. R=x^2
is excluded in the new embedding scope as well as the old inner scope.

## Custody, limitations and next decision

Desk-only; no numerical, modular, CAS or finite-degree evidence is used.
Original producer and charged input hashes were checked unchanged after
the terminal review. The external review uses legacy terminal-receipt
custody, not a canonical artifact seal; BODY_SEALED/CLEAN is not such a
seal. ROOT's terminal trusted collision scan returned EMPTY. This
integration has its own canonical transaction and collision scan.
Custody verifies which text was reviewed; it does not prove the text.

The global construction gap remains: no full polynomial Weyl pair
outside the automorphism class, and no polynomial Keller counterexample,
has been produced. Arbitrary rational pairs, formal algebraization and
unrelated construction mechanisms remain outside this filter. No new
family, classification/source sweep, theorem-chain audit or model
successor is commissioned by this promotion. Novelty is not established.

## OPENS RAISED

None. The global conjectures are not reissued as bounded tasks.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8202`.
- Body SHA-256:
  `a0a04f666d59b84de5ac9b4f17b57ccd12f2c3d334d6362cdea71fe5096a333f`.
- Frozen basis: `b4fe627842934b2fa33b2f6965f05e2240108d4c`.
