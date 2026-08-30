# Binding integration: quadratic ramification connectedness and F5 lattice closure

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen integration basis: `3647d740119088e5bc5ee7a16255eb6b7344e6e3`  
Lifecycle: **PROMOTED, EXACT IN THE DECLARED STRATUM**

## 0. Verdict and custody

This integration binds the exact global producer

```text
4978e225d4847a29d4d87876fa347132871ddba958afb9db6ede2b1699c45a39
  xmodel/bd-a2-ramification-connectedness-f5-lattice-closure-sol56-20260830.md
  body 13850 / 2fa574c72a81e6b736cd6847fcbb9cc9272b60ed34c46ef40c1996a3020d92b6
```

to the independent GPT-5.5 xhigh hostile review

```text
444e813d22e4e9c2f9e0b03c8ed025952601f10a30928e36b39ad0b7a36bf1fe
  xmodel/bd-a2-ramification-connectedness-f5-lattice-hostile-review-codex55-20260830.md
  body 11936 / 5e76465483713b91c9f65d9792d046f450d98e63fdb2bb123645b2938c2fdc03
  verdict CONFIRM_WITH_CORRECTIONS
```

The review independently reconstructed the relative canonical class, ample-
connectedness argument, resolved-graph eliminations, rank-eleven conic-bundle
marking, classification of contracted curves, local-to-global carrier step,
all lattice equations, and the enumeration over every labelled four-subset.
It found no mathematical gap. Its corrections are binding below.

The producer's internal `Frozen basis` field is `1efd7a76...`: that records
the authorship/dependency snapshot on which its desk derivation began. The
producer was transactionally published and first committed at
`78da50bd31b3f7fd8d07ed8fc5ddbbf0ad4290d1`; the review ran on exactly that
commit. Its charged F5 local integration is the sealed artifact `8fcd071f...`,
also authored on basis `1efd7a76...` and committed before the producer. These
are distinct lifecycle facts, not a claim that the producer file existed at
the older commit. Neither frozen input is mutated.

Fable 5 and Opus 5 were attempted first but the shared Claude account refused
both jobs at its monthly spend ceiling before model work. Grok 4.6 likewise
failed before model work because its Build balance was exhausted. Their
quarantined receipts make no mathematical contribution. GPT-5.5 is a fresh
model/context distinct from the Sol 5.6 producer and satisfies the campaign's
different-model promotion gate.

## 1. Exact promoted theorem

Let `X` be a smooth irreducible hypersurface of class `2A+3B` in
`P2 times P1`. Let `pi:X->P2` be generically finite and finite near the
reduced squarefree infinity curve `H=X intersect {line at infinity}~A`.
Assume the promoted dominant-`A2` first-leg hypotheses: the resolved full
boundary is a rational forest, the boundary classification and attachment
theorems apply, and the dominant block morphism supplies
`O(U)^*=O(X minus H)^*=C^*` for the localization argument.

Then no such first leg exists. More explicitly:

```text
F1,F2,F4,F7 are impossible by connected ramification plus two attachments;
F5 is impossible by its exact 3+5 different and the conic-bundle lattice;
F3,F6 violate the assumed projective finiteness near H;
F8,F9 admit no reduced rational-tree refinement.
```

Thus the entire smooth, projectively finite, reduced-squarefree quadratic
stratum in this fixed-basis incidence model is empty under the declared
dominant-`A2` first-leg hypotheses.

## 2. Global connectedness removes the reducibility loophole

Adjunction on `X~2A+3B` gives

```text
A^2=3,  A.B=2,  B^2=0,  K_X=-A+B,
R_pi=K_X-pi^*K_P2=2A+B.
```

`O_X(2A+B)` is the restriction of the ample ambient bundle `O(2,1)`.
Characteristic zero and generic finiteness make the Jacobian section nonzero,
so `R_pi` is a nonzero effective ample Cartier divisor. If its reduced
support were disconnected, partitioning the Cartier multiplicities between
two disjoint nonzero effective divisors `D_1,D_2` would give
`D_i^2=R_pi.D_i>0` and `D_1.D_2=0`, contradicting the Hodge index theorem.
Hence the **connected reduced support** of `R_pi` is connected; no reducedness
or irreducibility of the Cartier divisor is assumed.

The promoted attachment integration excludes a ramification component inside
reduced `H`, so this projective support is the closure of the reduced affine
ramification support. In an embedded resolution, the connected total
transforms of connected `H` and of this connected reduced support are trees
inside the assumed forest. Two distinct physical attachment points give two
independent joining paths. Contracting the two trees leaves parallel edges,
hence a cycle. The promoted exact attachment counts therefore eliminate
`F1,F2,F4,F7`, including reducible and nonreduced ramification divisors.

## 3. The F5 lattice is finite and empty

For `F5`, use the nine-singular-fibre conic bundle `q:X->P1` with `F=B`, a
section `S`, and fibre components `E_i` disjoint from `S`. With `E_1` chosen
in the fibre containing the `(0,1)` infinity component `L`, the exact marking
is

```text
S^2=-2,  S.F=1,  E_i^2=-1,
A=2S+5F-sum_(i=1)^9 E_i,
L=F-E_1,
T=S+4F-sum_(i=2)^9 E_i.
```

An irreducible `A`-null curve disjoint from `H=L+S+T` is literally
`{target point} times P1`, hence a smooth `q`-section of square `-3`. Its
class must be

```text
Z_I=S+2F-E_1-sum_(i in I)E_i,
I subset {2,...,9},  |I|=4.
```

Distinct effective such curves are disjoint, so
`Z_I.Z_J=1-|I intersect J|=0` whenever two coexist. No stronger unused claim
about triples is needed.

The reviewed local F5 calculation gives two reduced smooth transverse
source-different germs. `D_3` denotes the **weight-three transverse** branch,
with contact vector `(1,1,1)` against `(L,S,T)`; `D_5` denotes the
**weight-five tangent** branch, with vector `(1,2,2)`. The displayed tangent
lines in the local calculation are not themselves the analytic branches.
If both germs belonged to one global prime, their distinct normalization
points over connected `H` would already create a cycle. Thus a possible
survivor has distinct carrier primes `D_3,D_5`, each with Cartier coefficient
one. Their vectors exhaust `R_pi.(L,S,T)=(2,3,3)`, so every other prime is an
`A`-null `Z_I`.

Put `x=F.D_3`, `y=F.D_5`, and let `N` be the total Cartier multiplicity of
the `A`-null primes. Then `x,y>=1` and

```text
x+y+N=R_pi.F=4.
```

The local transverse intersection contributes one to `D_3.D_5`. The equality
`D_3.D_5=1` is imposed only as a **necessary survivor condition**: if there is
any further intersection, the boundary path and that extra interior path
already form a forbidden cycle.

Writing

```text
D_3=xS+(2x+1)F-(x-1)E_1-sum a_jE_j,
D_5=yS+(2y+2)F-(y-1)E_1-sum b_jE_j
```

gives nonnegative integral `a_j=D_3.E_j`, `b_j=D_5.E_j` and

```text
sum a_j=4x,  sum b_j=4y,
a_j+b_j+c_j=2,
delta_3=(D_3^2+x-1)/2 in Z_(>=0),
delta_5=(D_5^2+y-3)/2 in Z_(>=0),
sum a_j*b_j=xy+3x+2y-2.
```

Here `c_j` records the actual Cartier multiplicities of the `Z_I` terms.
The coordinate equality bounds every `a_j,b_j` by two. The seven possible
partitions are therefore a literal finite enumeration. The reviewer reran
all labelled subsets: doubled `Z` has 70 labelled solutions forming one
permutation orbit, while the other six rows have none. The sole orbit is

```text
R_pi=D_3+D_5+2Z,
D_3=S+3F-sum_(j in J)E_j,
D_5=S+4F-sum_(j in J)E_j,
Z=S+2F-E_1-sum_(i in I)E_i,
J={2,...,9} minus I,
D_3.D_5=1,  D_3.Z=3,  D_5.Z=4.
```

It is impossible in two independent ways. First,

```text
D_3+Z=A=L+S+T=H.
```

Restricting to `Y=X minus H` gives `[D_3]+[Z]=0` in `Cl(Y)`. For
`U=Y minus Supp(R_pi)`, the charged equality
`O(U)^*=O(Y)^*=C^*` makes the localization map from the free group on the
reduced ramification primes inject into `Cl(Y)`, contradicting this nonzero
relation. The coefficient two of `Z` in the Cartier different is irrelevant
to the reduced-prime map.

Second, the resolved F5 boundary configuration gives one path from `D_3` to
`D_5`, while the positive intersections with the `H`-disjoint component `Z`
give another interior path. Blowups only subdivide these distinct paths, so
their cycle cannot disappear. Hence `F5` has no survivor.

## 4. Scope firewall and next clients

This theorem does not cover nonreduced infinity, a singular incidence
surface, affine coefficient common zeros, source/fibre/target degree drops,
projective coefficient basepoints outside finiteness, or change to a better
global trace-zero basis. It is not general quadratic or cubic block closure,
primitivity, existence/nonexistence of a polynomial Keller map, a
counterexample, or JC2.

The next quadratic clients are the adjacent basepoint/nonfinite, singular,
degree-drop, and basis-minimization strata. No larger lattice search or heavy
CAS is licensed by this promotion; all heavy or uncertain computation remains
AWS-only after a source-reviewed packet.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8709`.
- Body SHA-256:
  `919a024751d6b28b02908f384297a59b791d1a0d52abb931f9fe5840a486df1a`.
- Frozen basis: `3647d740119088e5bc5ee7a16255eb6b7344e6e3`.
