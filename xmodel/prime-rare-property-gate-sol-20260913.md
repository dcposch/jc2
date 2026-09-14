# Rare primitive-element implication — different-model FIRST

Task: `prime-rare-property-gate-sol-20260913`  
Basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`  
First action: `2026-09-13T04:16:51.007992934Z`  
Network closed no later than `2026-09-13T04:17:18.334580663Z`, before the fixed `04:25Z` cutoff.

## Verdict

**REFUTED.** The general implication attributed to MathOverflow Answer 2.21,

`every nonconstant monomial x^i y^j is primitive for C(x,y)/R  =>  [C(x,y):R]=2`,

is false. ROOT's proposed construction is a valid degree-three counterexample. The cited answer gives one quadratic counterexample to `R=C(x,y)`; it does not establish a universal degree bound. Consequently, the invocation of “Answer 2.21” in the proof of arXiv:2407.13795v1, Theorem 3.2, is unsupported. This does **not** refute the theorem's Keller-specific statement, because the construction below is deliberately not Keller.

## Exact construction and hypotheses

Let `z,w` be algebraically independent over `C`, put

`L=C(z,w)`, `x=2z-w-1`, `y=w-z`, and `K=C(z^3,w)`.

The affine change is invertible:

`z=x+y+1`, `w=x+2y+1`.

Hence `L=C(x,y)`, while `u=(x+y+1)^3` and `v=x+2y+1` are algebraically independent polynomials and `K=C(u,v)`, exactly as Question 2.20 requires. Moreover `L=K(z)` and `z` has minimal polynomial `T^3-u`: it is Eisenstein at the prime `u` in `C(w)[u][T]`. Therefore `[L:K]=3`.

## Every nonconstant monomial is primitive

Fix a primitive cube root `zeta`. The cyclic `K`-automorphism `sigma(z)=zeta z`, `sigma(w)=w` has fixed field `K`. Work in the UFD `C(w)[z]`. For `i,j>=0`,

`x^i y^j = (2z-w-1)^i (w-z)^j`

has possible roots

`a=(w+1)/2` with multiplicity `i`, and `b=w` with multiplicity `j`.

Its transform has roots `a/zeta` and `b/zeta` with the same respective multiplicities. As rational functions of the transcendental `w`, neither transformed root equals either original root:

- `a/zeta=a` and `b/zeta=b` would force `zeta=1`;
- `a/zeta=b` and `b/zeta=a` each fail already by comparing the nonzero constant term in `w`.

Thus for `(i,j)!=(0,0)` the irreducible-divisor support of `sigma(x^i y^j)` differs from that of `x^i y^j`; the monomial is not fixed and hence is not in `K`. Since `[L:K]=3` is prime, there is no proper intermediate field: `K(x^i y^j)=L`. This is precisely the paper's “rare property,” now in degree three.

The optional extra condition also holds. Since `x+y=z-1` is not fixed by `sigma`, `K(x+y)=L`.

## What the cited source actually proves

The paper's Question 2.20 asks whether the rare property forces `R=C(x,y)` and permits the optional `x+y` condition. Answer 2.21 then says that the cited MathOverflow answer proved degree two. But the actual sole answer by Laurent Moret-Bailly starts with the *chosen* quadratic extension `L=R(sqrt(u))`, changes coordinates to `x=s+v`, `y=s+2v`, and verifies that every nonconstant monomial lies outside `R`, hence generates that quadratic `L`. It is an existence counterexample to equality, not a classification of every field having the rare property. The question author's later edit itself extrapolates “the answer shows” degree two; that extrapolation is absent from the answer.

## Consequence and scope

Theorem 3.2 may conceivably be true for independent Keller-specific reasons, but its displayed deduction “rare property; hence Answer 2.21 implies degree two” fails. Here `Jac(z^3,w)` in `(z,w)` coordinates is `3z^2`, so this counterexample supplies no Keller map, no JC2 counterexample, and no statement about the campaign's actual source. It only removes the cited general lemma from the prime-degree argument until a genuinely Keller-dependent replacement is supplied.

Primary provenance: arXiv:2407.13795v1, exact retained PDF SHA `c468d366ed3147043adc31795d30258176d9ecea3379a03422e150dc56e32b13`, Question/Answer 2.20/2.21 and Theorem 3.2 proof; MathOverflow question 472877 and complete sole answer 473055, asked 2024-06-08, answered 2024-06-11, answer edited 2024-06-12, question edited 2024-07-11. Exact read scope is in `PINS.json`.

No scientific execution, CAS, source mutation, worker action, or theorem promotion occurred.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4182`.
- Body SHA-256:
  `c6ecdf98d11ddf64361443e0f99a85593eed570eb16841764a58a6b94375fd8e`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
