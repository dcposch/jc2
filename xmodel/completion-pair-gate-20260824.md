# `COMPLETION-PAIR-GATE-20260824`

- Status: **FROZEN — EXACT SCOPED RANK-2 NO-GO**
- Producer/model: OpenAI Codex, GPT-5 family; completion-pair root X
- Basis: `dd11599b07eb05591b5c006791005eef19457d8e`
- Frozen synthesis read:
  `xmodel/ideation-20260824T0453Z-synthesis.md`
- Synthesis SHA-256:
  `76d9b7685771f65138fcb3c3dba1cfdd1ab104a9a5b21a7e3262c971f96ff790`
- Execution: paper-first only; no browser, fleet, generic surface search,
  public contact, artifact computation, or shared-ledger edit

## Verdict

The finite-normalization/open-chart perimeter is sound after the
different/canonical language is stated with dualizing modules and Weil
divisors.  In rank two it yields an exact separator:

> **Rank-two no-go.**  A plane polynomial map over `C` with nonzero constant
> Jacobian cannot have function-field degree two.

Equivalently, no hypothetical plane Keller counterexample can have a
rank-two normalization.  The proof constructs the requested forbidden
principal boundary relation.  A finite normal rank-two algebra over
`A=C[u,v]` is globally

```text
R = A[z]/(z^2-h).
```

Étaleness on the affine open chart forces `z` to be a unit on
`U=Spec C[x,y]`.  Since that chart has only constant units, this is
impossible: `z` is trace zero and cannot be a scalar.  Equivalently, after
factoring the squarefree `h`, each branch factor has principal divisor `2E`
supported on the deleted boundary, contradicting injectivity of the boundary
divisor group in `Cl(X)`.

This is strictly weaker than JC2: it excludes only generic degree two.  It is
therefore a genuine scoped no-go rather than `RESTATEMENT`.  The registered
stop condition has fired, so no rank-three schema was opened.

## 1. Exact finite-normalization/open-chart perimeter

Let `F=(P,Q):A^2_C -> A^2_C` satisfy
`P_x Q_y-P_y Q_x=c in C^*`; rescale one target coordinate so that `c=1`.
Set

```text
A=C[P,Q] ~= C[u,v],       B=C[x,y],
K=Frac(A),                L=Frac(B),
R=the integral closure of A in L,
X=Spec R,                 U=Spec B.
```

The following statements are exact.

### 1.1 Algebraic independence, finiteness, and the canonical open immersion

The differentials `dP,dQ` are a basis of `Omega^1_B`, so `P,Q` are
algebraically independent.  Hence `A` is a polynomial ring and `L/K` is a
finite separable extension.  Since `A` is excellent, its normalization `R`
in `L` is finite over `A`.

There is a canonical inclusion `R subset B`.  Indeed, an element of `L`
integral over `A` satisfies the same monic equation over `B`; normality of
`B` then puts it in `B`.

The map `Spec B -> Spec A` is étale and of finite type, hence quasi-finite.
Zariski Main, in its normalization form, factors it as

```text
U=Spec B  --j, open immersion-->  X=Spec R
          --pi, finite-->         Spec A.
```

The fraction fields of `R` and `B` are both `L`, so `j` is dense and
birational.  JC2 for this pair is exactly the assertion `j(U)=X`.

### 1.2 `R` is finite free over `A`

The normal surface `R` satisfies `S_2`, so it is Cohen--Macaulay.  Locally at
a prime of `A`, every localization of `R` above it has the same dimension and
is Cohen--Macaulay.  Miracle flatness, equivalently
Auslander--Buchsbaum over the regular local ring `A_p`, makes `R_p` free over
`A_p`.  Thus `R` is finite projective over `A`; Quillen--Suslin makes it
finite free.  Its rank is `[L:K]`.

No Gorenstein or monogenic hypothesis is used here.

### 1.3 Units, divisorial boundary, and the localization sequence

Because `R subset B`, every unit of `R` is a unit of `B`.  Therefore

```text
R^* = B^* = C^*.
```

Let `D=X-U`.  If `D` were nonempty but had codimension at least two,
normal Hartogs extension would give

```text
R=Gamma(X,O_X)=Gamma(U,O_U)=B,
```

so the affine open immersion would be an isomorphism.  Hence every nontrivial
completion has at least one codimension-one boundary component.  Write these
components as `D_1,...,D_r`.

For a normal noetherian integral scheme, divisor localization gives

```text
R^* -> B^* -> direct_sum_i Z[D_i]
    -> Cl(X) -> Cl(U) -> 0.
```

Here the first unit map is an isomorphism and `Cl(U)=Cl(A^2)=0`.  Consequently

```text
direct_sum_i Z[D_i]  ~=  Cl(X).
```

In particular, there is no nonzero principal Weil divisor supported on the
boundary.  Producing merely a boundary class is not an obstruction; a proof
must produce a nonzero relation in this free boundary group.

### 1.4 Dualizing module, codifferent, and ramification conventions

Since `R` is finite free over the regular Gorenstein ring `A`, its canonical
module is

```text
omega_R = Hom_A(R,A).
```

The separable trace pairing identifies this module with the codifferent

```text
D^{-1}_{R/A}
  = {ell in L : Tr_{L/K}(ell R) subset A}.
```

It is a rank-one reflexive `R`-module.  It need not be invertible unless `R`
is Gorenstein.  Thus a general completion argument may not silently use a
Cartier different or a globally principal determinant.

At each height-one point, the extension of DVRs has a nonnegative different
exponent.  These exponents define an effective ramification Weil divisor.
With compatible rational top forms, the canonical formula is a Weil-divisor
formula

```text
K_X = pi^* K_A2 + Diff_pi = Diff_pi,
```

not automatically an equality of Cartier divisors.  On `U`, the map equals
the Keller map and is étale, so the ramification/different support lies in
`D`.  These statements are well-defined but, in arbitrary rank, do not
themselves produce a principal boundary relation.

## 2. Rank-two monogenic form

Assume for contradiction that `[L:K]=2`.  Then `R` is finite free of rank two
over `A`.  Because `2` is invertible, the trace projection splits:

```text
R = A*1 direct_sum M,       M=ker(Tr_{R/A}).
```

The summand `M` is projective of rank one.  Since `Pic(A)=0`, choose a global
generator `z` and write `M=Az`.  In the basis `(1,z)`, write

```text
z^2 = h + b z,       h,b in A.
```

The trace of multiplication by `z` is `b`, while `z` lies in the trace-zero
summand.  Hence `b=0`, and multiplication gives an isomorphism

```text
R ~= A[T]/(T^2-h),       T |-> z.                 (2.1)
```

The element `h` is nonzero and nonconstant.  If it were a nonzero constant,
it would be a square in `C`, so the generic quadratic algebra would split and
could not be the field `L`.  The case `h=0` is not a domain.

Normality makes `h` squarefree.  Indeed, if an irreducible `q` satisfied
`q^2 | h`, then `z/q` would satisfy the monic equation

```text
(z/q)^2-h/q^2=0
```

over `A`, hence would be integral over `R`.  Normality would put `z/q` in
`R=A direct_sum Az`; comparing coefficients after multiplication by `q`
would require `q` to be a unit, a contradiction.

The relative differentials are now explicit:

```text
Omega_{R/A} ~= (R/(2z)) dz.                       (2.2)
```

Thus the non-étale locus of `pi` is exactly `V_X(z)`, the ramification
divisor.

## 3. Exact rank-two contradiction

Because `j` is an open immersion, cotangent base change gives

```text
Omega_{B/A} ~= B tensor_R Omega_{R/A}.
```

The Keller condition says `Omega_{B/A}=0`.  Combining this with (2.2) gives

```text
B/(2z)B=0,
```

so `z` is a unit in `B`.  But `B^*=C^*`; hence `z` would be a scalar.  Its
trace is zero, so that scalar would be zero, contradicting that a unit is
nonzero.  This proves the rank-two no-go.

The same contradiction is visible as the requested principal boundary
relation.  Factor the squarefree element

```text
h = c q_1 ... q_s
```

into distinct irreducibles of `A`.  Above `q_i=0` there is a unique prime
divisor

```text
E_i = V_X(q_i,z).
```

At its generic point, `z` is a uniformizer and `q_i=z^2` times a unit, so

```text
div_X(q_i)=2E_i.                                  (3.1)
```

Equation (2.2) and étaleness on `U` put every `E_i` in `D`.  Thus (3.1) is a
nonzero principal relation in the free boundary divisor group, contradicting
the localization isomorphism of Section 1.3.  Equivalently, `q_i` restricts
to a nowhere-vanishing regular function on `U`, hence to a nonconstant unit
of `B`, which is impossible.

This proof uses the open chart rather than assuming it: `j` comes canonically
from Zariski Main, and the differential base-change identity verifies exactly
how Keller étaleness removes the quadratic ramification divisor.

## 4. Scope, cost, and stop

The output is the exact certificate

```text
RANK2-NOGO:
no constant-Jacobian plane polynomial map over C has [L:K]=2.
```

It uses no degree bound on `P,Q`, no compactification, no GGV/Sigray receiver,
and no unproved class/canonical positivity.  It does not address ranks three
or higher and therefore is not a proof of JC2.

The gate cost was one paper derivation.  No software artifact was needed, so
`cases/completion_pair_gate_20260824/` was not created.  The registered stop
condition was the first exact scoped separator; it has fired.  Opening a
rank-three or one-boundary family in this generation would violate the task's
stop discipline and is not licensed by the rank-two result.

No claim is promoted by this report.  It is frozen for independent hostile
review.
