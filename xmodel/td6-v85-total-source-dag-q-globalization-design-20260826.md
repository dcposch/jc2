# TD6 successor design: source-DAG globalization in all licensed `q` jets

Date: 2026-08-26

Status: design/acceleration note only.  No all-`q` theorem is claimed.

## 1. Algebraic compression

Let `A` be the frozen normalized source coefficient ring, localized only at
the registered set `S`, and let

```text
T=(F,q2,...,q14,q16,...,q24).
```

Suppose the literal total raw rows `f_i(T)` lie in `A_S[T][X]`, and the
frozen special certificate is

```text
s = sum_i a_i*f_i(0),                 s in S, a_i in A_S[X].       (1.1)
```

Then no new elimination is needed to prove

```text
s = sum_i a_i*f_i(T) + F*h_F + sum_e q_e*h_e.                     (1.2)
```

Indeed, order the variables `T1,...,Tn` and use the literal telescoping
divided differences

```text
D_j f = (
  f(T1,...,Tj,0,...,0)-f(T1,...,Tj-1,0,...,0)
)/Tj.
```

Polynomiality makes every division exact in `A_S[T][X]`, and (1.2) follows
from (1.1) with `h_j=-sum_i a_i*D_j f_i`.  This is an equality of source
DAGs; expanding every `h_j` is optional evidence, not mathematics.

Consequently any DVR arc on `D(S)` satisfying the total raw rows and sending
all entries of `T` to the maximal ideal is impossible: the right side of
(1.2) lies in the maximal ideal while `s` is a unit.

## 2. Why the TD6 q family is a good fit

For the frozen normalized boundary

```text
p=t^15,
q=t + sum_e q_e*t^e + t^25,
```

the homogeneous transport matrix is independent of every `q_e`; only its
affine source RHS changes, linearly, at the exact source key
`('g','X',0,e)`.  Hence the frozen transport pivots can be reused and their
RHS solution is polynomial (indeed affine) in all q variables.  The raw
receiver is then built polynomially from the transported bands, from
`Q_PRIME=q'`, and from the q2 load coordinate `B=q2`.  No receiver operation
requires inversion of a q variable.

The V85TF1 identity already supplies (1.1) after totalizing `F`, with all 132
transport-free section coordinates retained and with coefficient denominator
exactly `U*H`.  Therefore the all-q successor should prove source-DAG
polynomiality and denominator ancestry, rather than repeat staged CURRENT
elimination or expand twenty-two independent certificates.

## 3. Required exact gates

The compressed theorem is licensed only after the following checks.

1. **Literal total source.** Rebuild every affine transport RHS contribution
   from its original source key.  Retain `B=q2` and every direct derivative
   term `e*q_e*t^(e-1)` in `Q_PRIME`.
2. **No truncation.** Use a sparse polynomial/circuit ring in all q variables,
   not the existing square-zero EJet.  Degree bounds may be reported after
   construction but not imposed by the coefficient type.
3. **Denominator ancestry.** Prove that all transport pivot inversions are
   q-independent and that their irreducible factors lie in the registered
   `U,H,B3` set.  Raw receiver operations must be multiplication/addition
   only.  Neither `F` nor any q variable may occur in a denominator.
4. **Exact specialization.** At all q variables zero, reproduce every V85TF1
   raw FIRST row, the genuine 2,893-term P12, all labels `0..131`, and the
   V85 beta-zero quotient hash.
5. **Omission controls.** Removing one transport-RHS q path, one direct
   `Q_PRIME` path, q2's `B` path, P12, or an active FIRST row must change the
   appropriate source/replay digest.
6. **Gauge firewall.** `q15` is omitted only if the frozen target-shear gauge
   gives an exact two-sided total-coordinate map compatible with fixed
   `p=t^15`.  Otherwise include q15 together with the orbit/target variable
   which absorbs it.  A tangent-level gauge marker is insufficient.
7. **Chart scope.** State explicitly that dead stretch, correction,
   F1-orbit/pole, centering, and remaining boundary moduli are still frozen.

The source-DAG certificate should emit the ordered telescoping variable list,
hash every total raw source circuit, record each pivot-denominator ancestor,
and replay (1.2) symbolically.  A small expanded q2 client is the acceptance
fixture: it must retain both beta paths and reproduce V85 at beta zero before
the compressed all-q theorem is trusted.

## 4. Strategic effect

If these gates pass, the reviewed CURRENT factors `F,G,L` cease to be the
critical q-neighborhood obstruction on this normalized slice: the genuine
raw P12/FIRST identity bypasses the staged presentation without inverting
`G` or `L`.  The TD6 frontier then moves to the first genuinely missing total
chart directions—most likely q15/orbit gauge custody, dead stretch,
correction, pole/orbit, centering, and boundary overlap—rather than more
CURRENT alternate-minor computation.

This design does not supply those charts or a finite cover, and proves no
whole fixed A3, TD6, SP-2, landing, or JC2 claim.

