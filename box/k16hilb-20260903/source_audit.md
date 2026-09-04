# Frozen-source audit for the K=16 Hilbert/regular-sequence lane

All 16 frozen inputs passed a mechanically generated `sha256sum -c` manifest from
`xmodel/k16-hilbert-regseq-sol56-20260903.run.v2`.  This memo cites only the
frozen copies under `/tmp/jc2-lane.zmfoKT/inputs` and makes no new CAS claim.

## 1. Coefficient algebra and fibres

The common notation is

```text
q=2t+1,  e=3t+1,
H_t(y)=12q^2 y^2-12q(t+1)y+(t+1)(3t+2),
A_t=Q[y]/(H_t),  d=2qy-(t+1),
```

and substitution gives `A_t=Q[d]/(3d^2-(t+1))`; see
`/tmp/jc2-lane.zmfoKT/inputs/k16-terminal-proof-sol56-20260903.md:34-50`.
The auxiliary constants used by the terminal recurrence are
`g=et(3d+2(t+1))/(6q^3)` and `c=-yg`
(`/tmp/jc2-lane.zmfoKT/inputs/k16-terminal-proof-sol56-20260903.md:52-56`).
The denominator/resultant audit proves the relevant classes `y`, `g`, all high
pivots, and the last diagonal are units for every integer `t>=2`
(`/tmp/jc2-lane.zmfoKT/inputs/k16-terminal-proof-sol56-20260903.md:275-309`),
and proves that the parameter-denominator exception set is empty for integer
`t>=2` (`.../k16-terminal-proof-sol56-20260903.md:341-360`).

A geometric fibre means choosing a root of `H_t` in an algebraically closed
field.  The algebra splits over `Q` exactly for `t=3s^2-1`; its two factors have
`d=+s,-s`, equivalently
`y=(t+1+s)/(2q),(t+1-s)/(2q)`
(`/tmp/jc2-lane.zmfoKT/inputs/k16-cone-gate-gpt55-20260903.md:43-60`).
Thus among `t=3,...,8` there is no rationally split index.  The control `t=2`
has the two rational fibres `y=2/5` (`d=+1`) and `y=1/5` (`d=-1`).  At a split
index the product algebra must not be treated as a field, and both factors must
be tested (`.../k16-cone-gate-gpt55-20260903.md:50-61`).  At a non-split index,
one good modular root is enough for the properness promotion; the two modular
roots are embeddings of the same quadratic generic field and duplicate runs
are only redundancy
(`/tmp/jc2-lane.zmfoKT/inputs/k16-properness-gate-opus5-20260903.md:336-342`).

## 2. Residual ring, generators, and grading

After the high affine spine is solved, the residual ring is

```text
S_t=A_t[b3,b4,q_(2,0),...,q_(t-1,0)]
```

with exactly `n=t` variables, not `t+2`: `b3,b4` plus `t-2` q-variables.  This
count is explicit in
`/tmp/jc2-lane.zmfoKT/inputs/k16-properness-gate-opus5-20260903.md:68-72`
and again in
`/tmp/jc2-lane.zmfoKT/inputs/k16-subchart-q-opus5-20260903.md:82-84`.
The positive ideal is

```text
I_(t,+)=<T_(t,1),...,T_(t,2t-1)>.
```

See `/tmp/jc2-lane.zmfoKT/inputs/k16-cone-gate-gpt55-20260903.md:63-74`.
The residual weights are

```text
wt(b4)=1, wt(q_(i,0))=i (2<=i<t), wt(b3)=t+1.
```

The full spine grading, including eliminated variables, is recorded at
`.../k16-cone-gate-gpt55-20260903.md:96-117`.

For every positive row,

```text
wt(T_(t,k))=4t+1-k,                 1<=k<=2t-1.
```

This follows symbolically from the recurrence and change from `L=X-b4` back to
`X` (`.../k16-cone-gate-gpt55-20260903.md:119-122`), and every monomial obeys
`(t+1)a+b+sum i*c_i=4t+1-k`
(`/tmp/jc2-lane.zmfoKT/inputs/k16-terminal-proof-sol56-20260903.md:228-249`).
Consequently the positive rows have weights `4t,4t-1,...,2t+2` as `k` runs
from `1` to `2t-1`.  The `k=0` row is not in `I_(t,+)`: only its nonconstant
part has weight `4t+1`, while its constant part is a unit
(`/tmp/jc2-lane.zmfoKT/inputs/k16-properness-gate-opus5-20260903.md:68-77`).

The proposed band set `k=2t-1,2t-2,...,t-2` contains `t+2` rows but has actual
weights `2t+2,2t+3,...,3t+3`; it is not the set of highest-weight positive rows.
More importantly, a polynomial ring of dimension `t` over a field (or over the
zero-dimensional semisimple `A_t`) cannot contain a regular sequence of length
`t+2`.  A zero-dimensional homogeneous complete intersection/h.s.o.p. here has
exactly `t` elements.  Therefore the literal `t+2` regular-sequence request is
structurally impossible before computation.  A plausible repair is either the
`t` top-tail rows `k=t,...,2t-1` (the source calls these `t` quadratics after
`b4=1`: `/tmp/jc2-lane.zmfoKT/inputs/k16-subchart-q-opus5-20260903.md:659-667`)
or a greedy search for an arbitrary `t`-row subset.  Either repair must be
labelled as such rather than silently substituted for the prompt.

There is also a terminology issue: for a finite-length graded quotient the
eventual Hilbert polynomial is identically zero.  The interesting polynomial is
the terminating Hilbert-series polynomial `sum_d dim(S_t/I)_d s^d`; its value
at `s=1` is the fibrewise vector-space length.  The raw numerator displayed over
`product_j(1-s^(w_j))` encodes the same series but vanishes at `s=1`, so its
value at one is not the length; one must first divide/cancel or take the limit.

## 3. Closed indexed generator family

The Sol construction sets `L=X-b4`, writes `u_i=q_(i,0)`, and defines `U,C` and
their translated coefficient arrays explicitly in (2.1)-(2.2)
(`/tmp/jc2-lane.zmfoKT/inputs/k16-terminal-proof-sol56-20260903.md:78-96`).
It then defines the arrays `B,S` in (2.3)-(2.4) (`...:98-120`), the polynomials
`V,Y,Z,N,P0',R=-E_t` in (2.5) (`...:122-135`), and their completely
coefficientwise convolutions in (2.7) (`...:146-162`).

The high variables are ordered

```text
z_j=c_j (1<=j<t), z_j=u_j (t<=j<=2t), z_(2t+1)=b2,
```

and solved successively by `z_j=-rho_j/p_j`; the exact diagonals `p_C,p_Q,p_b2`
are displayed in (2.10)-(2.12)
(`/tmp/jc2-lane.zmfoKT/inputs/k16-terminal-proof-sol56-20260903.md:164-212`).
The terminal row is then

```text
T_(t,k)=-sum_(m>=k) binom(m,k)(-b4)^(m-k) R_m,
0<=k<2t.
```

This is the proved closed indexed form (2.13), and the source proves that after
exactly `2t+1` high solves it lies in the residual ring above
(`.../k16-terminal-proof-sol56-20260903.md:214-226`).  The equivalent `w`-picture
defines `Delta` by four coefficient identities and extracts
`T_(t,k)=-[w^(4t+1-k)]sigma_t(Delta)+yg[k=0]`; see
`/tmp/jc2-lane.zmfoKT/inputs/k16-terminal-proof-fable5-20260903.md:61-114`.

Sign convention must be declared.  Sol's frozen JSON convention gives
`T_(t,0)(0)=yg=-c` (`.../k16-terminal-proof-sol56-20260903.md:58-66`), whereas
the earlier Opus convention writes `T_(t,0)=c+tau_t`.  The properness audit
explains that these are overall-opposite families, hence define the same ideals
(`/tmp/jc2-lane.zmfoKT/inputs/k16-properness-gate-opus5-20260903.md:269-279`).

The safest uniform output of the indexed construction is weighted homogeneity
and the support bounds.  Sol explicitly says exact degree equality was a finite
control and that (2.14)-(2.15), not equality, is the uniform theorem
(`/tmp/jc2-lane.zmfoKT/inputs/k16-terminal-proof-sol56-20260903.md:381-389`).
Fable, by contrast, states uniformly that the pure `b4` power is present
(`/tmp/jc2-lane.zmfoKT/inputs/k16-terminal-proof-fable5-20260903.md:142-154`),
but later says the pure-`b4` coefficients form a growing `t`-indexed sequence
for which the near-axis rational-function theorem gives no uniform formula or
nonvanishing certificate (`.../k16-terminal-proof-fable5-20260903.md:252-270`).
Thus a uniform claim about the leading monomial/pure `b4` coefficient needs a
new derivation; the frozen sources do not safely supply it.

## 4. Properness promotion: exact usable statement

The audited lemma is: for a local domain `R`, a positively weighted polynomial
ring, and a homogeneous ideal `J`, if the special-fibre affine cone is `{0}`
over the algebraic closure of the residue field, then the generic-fibre cone is
`{0}`.  The proof uses properness of `Proj(R[x]/J)` and base change; see
`/tmp/jc2-lane.zmfoKT/inputs/k16-properness-gate-opus5-20260903.md:97-113`.
Finite generation, strictly positive degrees, and `S_0=R` are essential; this
is precisely why `T_(t,0)` is excluded (`.../k16-properness-gate-opus5-20260903.md:56-77`).

For the present ideals, cone `{0}` is equivalent to every variable being
nilpotent in the quotient, equivalently a pure power of every variable lying in
the monomial lead ideal.  This is field-independent and avoids relying on any
ambiguous interpretation of `dim` in a `wp` ring
(`/tmp/jc2-lane.zmfoKT/inputs/k16-properness-gate-opus5-20260903.md:79-95`).

The modular job must actually be the reduction of the same integral generators.
The corrected sufficient check is stronger than merely `p` not dividing
`12q^2` and `r` being a root: all fixed denominators, `r`, `yg`, and every high
pivot must be units (`.../k16-properness-gate-opus5-20260903.md:146-184`).  A
clean modular recurrence with `p>8t+3`, all `2t+1` pivots printed nonzero, and no
error marker self-certifies commutation with reduction by induction
(`.../k16-properness-gate-opus5-20260903.md:241-249`).  Singular division by
zero is loud but does not stop execution, so scanning output is load-bearing
(`.../k16-properness-gate-opus5-20260903.md:186-198`).

The lemma promotes only the conclusion `dim=0`/cone `{0}`.  It uses no flatness
and is one-directional (`.../k16-properness-gate-opus5-20260903.md:115-132`).
Accordingly a modular Hilbert series or modular length is measured in that
special fibre and does not become the characteristic-zero Hilbert series or
length by this lemma.  This is an inference from the explicitly non-flat,
one-directional proof, and matches the prompt's FALLACY-v2 warning.

## 5. Prior (V0) evidence and full weighted lead ideals

The later properness audit is the controlling status source:

* `t=3,4`: exact characteristic-zero `dim=0`;
* `t=5`: modular `dim=0` on both roots modulo `32009`;
* `t=6`: modular `dim=0` modulo `32003`;
* `t=7`: modular `dim=0` modulo `32059`;
* these modular cases satisfy the audited hypotheses and therefore prove (V0)
  in characteristic zero;
* `t=8,9,11` and all `t>=12` were not proved.

The complete table, including primes, roots, basis sizes and pure powers, is at
`/tmp/jc2-lane.zmfoKT/inputs/k16-properness-gate-opus5-20260903.md:311-345`.
In particular the previously measured full-`wp` pure powers were

```text
t=3: b3^2, b4^10, q2^8
t=4: b3^2, b4^12, q2^9, q3^8
t=5: b3^2, b4^14, q2^10, q3^9, q4^8
t=6: b3^2, b4^16, q2^11, q3^10, q4^9, q5^8
t=7: b3^2, b4^18, q2^13, q3^11, q4^10, q5^9, q6^9.
```

These are containments, not a list of the minimal generators of the full
initial ideal.  The extrapolation `q_j^(t+7-j)` is explicitly refuted at `t=7`
by `q2^13` and `q6^9` rather than the predicted exponents `12,8`
(`.../k16-properness-gate-opus5-20260903.md:374-383`).

The mandatory `t=2` controls are exact: at `y=1/5`, `dim I_(2,+)=1` and no
pure `b3` power occurs; at `y=2/5`, `dim=0` and the lead ideal contains
`b3^2,b4^8` (`.../k16-properness-gate-opus5-20260903.md:311-328`).  This agrees
with the direct geometric statement that the first fibre contains the whole
`b3` axis while the second cuts it (`/tmp/jc2-lane.zmfoKT/inputs/k16-cone-gate-gpt55-20260903.md:215-239`).

The failed earlier “initial-form upgrade” is a different construction.  It used
the coarse weight `w=0` on the surviving two-variable chart and `w=1` off it,
then formed the ideal generated by initial forms of the supplied generators;
its dimensions `2,3,3,4` at `t=4,5,6,7` do not describe the full `wp` initial
ideal (`/tmp/jc2-lane.zmfoKT/inputs/k16-subchart-q-opus5-20260903.md:531-544`).

The exact monomial order still needs care.  Prior runs declare variable order
`(b3,b4,q2,...,q_(t-1))` and order vector
`wp(t+1,1,2,...,t-1)`
(`/tmp/jc2-lane.zmfoKT/inputs/k16-properness-gate-opus5-20260903.md:398-403`).
The present prompt instead writes variables `(b4,q2,...,q_(t-1),b3)` with
`wp(1,2,...,t-1,t+1)`.  These represent the same grading after a permutation,
but weighted degree alone does not specify tie-breaking, so minimal initial
generators and least pure-power exponents may differ.  The new report must print
the exact ring variable order and Singular order used.  Pure-power existence
and zero-dimensionality remain invariant.

There are harmless basis-size discrepancies between older reports: the cone
gate gives sizes `4,20,81` for `t=2,y=2/5`, `t=3`, `t=4`
(`/tmp/jc2-lane.zmfoKT/inputs/k16-cone-gate-gpt55-20260903.md:244-255`), whereas
the later properness replay gives `3,15,66` for the analogous cases
(`.../k16-properness-gate-opus5-20260903.md:311-319`).  Since order/reduction
conventions can change basis cardinality, do not use “GB size” as an invariant.

## 6. Dependency chain and its limit in the frozen corpus

On every geometric fibre, weighted homogeneity makes `Z_+=V(I_(t,+))` a cone.
If `dim I_(t,+)=0`, it is only the origin.  Since the homogeneous part `tau_t`
of band zero has positive weight, it vanishes there, and the nonzero constant
part forces the full terminal ideal to be the unit ideal.  More precisely,

```text
<I_(t,+), constant+tau_t>=(1)  iff  tau_t in sqrt(I_(t,+)),
dim I_(t,+)=0  =>  the left side is (1).
```

This is Lemma CONE
(`/tmp/jc2-lane.zmfoKT/inputs/k16-cone-gate-gpt55-20260903.md:63-93`).  The later
audit identifies (V0) exactly with `dim I_(t,+)=0`, stresses that the radical
criterion is strictly weaker, and uses `t=2,y=1/5` as the witness
(`/tmp/jc2-lane.zmfoKT/inputs/k16-properness-gate-opus5-20260903.md:347-364`).

The frozen reports then state the dependency

```text
(V0) => terminal unit statement (8.1)
     => theorem (T) at that t through the banked constant spine,
        normalizer lemma, and second affine spine.
```

The named downstream links appear at
`/tmp/jc2-lane.zmfoKT/inputs/k16-terminal-proof-fable5-20260903.md:331-340`, and
the properness audit states that the promoted `t=3,...,7` conclusions pass
through the banked uniformly proved reduction chain
(`/tmp/jc2-lane.zmfoKT/inputs/k16-properness-gate-opus5-20260903.md:336-344`).
However, the actual statements and proofs of the constant spine, normalizer
lemma, and second affine spine are not reproduced in this frozen charged set.
The current report can accurately consume the chain as banked, but cannot
independently restate its “full” internal dependencies from these inputs alone.

If (V0) is proved uniformly for every `t>=3`, then the frozen chain yields (T)
for every such `t`; the reports separately treat `t=1,2` as banked/exact.  At
`t=2,y=1/5`, (V0) is false but (8.1) still holds by the exact tau criterion;
at `y=2/5`, (V0) holds.  Thus no uniform theorem should claim (V0) for all
`t>=2` (`/tmp/jc2-lane.zmfoKT/inputs/k16-cone-gate-gpt55-20260903.md:225-242`).

## 7. Source tensions to state explicitly

1. The literal `t+2` regular-sequence request contradicts the source's exact
   variable count `t`; it cannot succeed in any fibre.
2. The band interval in the prompt is not the “highest-weight” interval and its
   quoted possible endpoint `4t+1` belongs to band zero, excluded from `I_(t,+)`.
3. The Fable section-8 sentence calls the exact V0 range `t=3..6`
   (`/tmp/jc2-lane.zmfoKT/inputs/k16-terminal-proof-fable5-20260903.md:414-426`),
   although its own earlier table promotes `t=7` and the later properness audit
   definitively proves `t=3..7`.  Use the later audited status.
4. Fable's original modular-prime condition is explicitly corrected by the
   properness audit; use the pivot/denominator-integrality conditions, not just
   `p` prime to `12q^2` plus `H_t(r)=0`.
5. A modular zero-dimensional Hilbert computation promotes only (V0), not its
   length or entire Hilbert series.  Report modular and characteristic-zero
   lengths separately.
