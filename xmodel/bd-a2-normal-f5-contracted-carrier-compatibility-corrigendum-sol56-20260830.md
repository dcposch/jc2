# Corrigendum: contracted-carrier compatibility in the marked F5 states

Date: 2026-08-30 UTC  
Producer: Sol 5.6 delegated lane `/root/quadratic_degeneracy_frontier`  
Frozen basis: `00b2fb0c682c5ca2a056af588a29b2421c1b7ce4`  
Lifecycle: **EXACT CORRIGENDUM / MUST ACCOMPANY THE CHARGED F5 CARRIER PACKET**

## 0. Correction verdict and charged artifact

This packet corrects one false combinatorial sentence in the immutable
sealed artifact

```text
f942e743dc206d958f31892e838d7517fe23eacbc863b56c9441b60152bc0cb4
  xmodel/bd-a2-normal-f5-decorated-carrier-effectivity-reduction-sol56-20260830.md
  body e4823537bbaa3bb6142790456c11814d9be32c8b3f4c93f2563a2a13eb2a641d.
```

Section 6 of that artifact says that three five-subsets with pairwise
intersection two cannot coexist by inclusion-exclusion.  That unqualified
statement is false.  For example,

```text
{1,2,3,4,7},   {1,2,5,6,8},   {3,4,5,6,9}             (0.1)
```

are three five-subsets of a nine-set with every pairwise intersection of
size two and empty triple intersection.

The marked F5 constraints are stronger than the false general statement.
After imposing them, the original **maximum of two contracted carriers is
still correct in each of the smooth, `q=6`, and `q=8` states**, but for
different state-specific reasons.  The complete corrected numerical table
is

| marked state | single candidate classes | compatible unordered pairs | maximum compatible family |
|---|---:|---:|---:|
| smooth `p_0` | 70 | 560 | 2 |
| singular `q=6` | 20 | 10 | 2 |
| singular `q=8` | 24 | 36 | 2 |

Consequently Section 9's instruction to add zero, one, or two contracted
carriers remains correct.  No carrier class, nine-tag F5 table entry,
ramification equation, cap, or energy formula changes.  Consumers must,
however, charge this corrigendum with the original packet; the original
inclusion-exclusion sentence must not be reused outside its marked scope.

## 1. Common numerical compatibility condition

Keep the notation of the charged packet.  In its `F_2` total-transform
marking an affine coefficient-basepoint carrier has class

```text
Z_J=S_0+2F-sum_(j in J)E_j,       |J|=5.              (1.1)
```

For two distinct classes,

```text
Z_J.Z_K=2-|J cap K|.                                  (1.2)
```

Distinct contracted curves lie over distinct target points: the fibre over
one target point contains at most the one source line `{q} times P1`.
Therefore their strict transforms are disjoint, and numerical coexistence
requires

```text
|J cap K|=2.                                          (1.3)
```

At most one irreducible carrier can have a given class, since two distinct
effective curves in that class would have intersection `Z_J^2=-3`.  Thus a
family of distinct effective contracted carriers gives a family of distinct
subsets satisfying (1.3).  The converse is not asserted: (1.3) is numerical
compatibility, not proximity or effectivity.

## 2. Smooth F5 state

Let `l` be the index from

```text
L=F-E_l,
T=S_0+4F-sum_(i!=l)E_i.
```

Disjointness from `L,S,T` says exactly

```text
J={l} union K,       K subset U,       |U|=8, |K|=4.  (2.1)
```

There are `binom(8,4)=70` candidates.  For two candidates, (1.3) becomes
`|K cap K'|=1`.  For fixed `K`, choose the common element in four ways and
the other three elements of `K'` from the four-element complement in four
ways.  Hence the compatible unordered-pair count is

```text
70*(4*4)/2=560.                                       (2.2)
```

Three compatible candidates cannot occur.  Directly in the original
nine-set, all three `J` contain `l`, so their triple intersection has size
at least one.  If every pair has intersection two, inclusion-exclusion
would give

```text
|J_1 union J_2 union J_3|
 =15-6+|J_1 cap J_2 cap J_3|>=10,                     (2.3)
```

which is impossible in a nine-set.  This is the missing hypothesis in the
original argument and the exact reason the counterexample (0.1), whose
triple intersection is empty, does not belong to the smooth marked state.

## 3. Singular `q=6` state

Here `l notin J`, and in the eight-element universe

```text
U={1,...,9} minus {l},
|I_6|=6,       O=U minus I_6,       |O|=2,
|J|=5,         |J cap I_6|=3.                         (3.1)
```

Every candidate is uniquely

```text
J=O union K,       K subset I_6,       |K|=3.          (3.2)
```

This gives `binom(6,3)=20` candidates.  Two candidates satisfy (1.3) if
and only if their three-subsets `K,K'` are disjoint.  They are then
complements in `I_6`; hence

```text
binom(6,3)/2=10                                       (3.3)
```

compatible unordered pairs.  Three pairwise compatible candidates would
require three pairwise disjoint three-subsets of the six-set `I_6`, which
is impossible.  Thus the maximum is two.

## 4. Singular `q=8` state

Now the eight-element universe splits as

```text
U=I_4 disjoint-union O,       |I_4|=|O|=4,             (4.1)
```

and every candidate is uniquely

```text
J=K union N,       K subset I_4, |K|=2,
                   N subset O,   |N|=3.                (4.2)
```

There are `binom(4,2)binom(4,3)=24` candidates.  Distinct three-subsets of
the four-set `O` meet in exactly two elements.  Therefore two candidates
satisfy (1.3) exactly when

```text
K cap K'=empty,       N!=N'.                           (4.3)
```

There are three unordered complementary pairs `{K,I_4 minus K}`.  After
canonically ordering the two members of such a pair, there are four choices
for `N` and three different choices for `N'`.  Thus the number of compatible
unordered carrier pairs is

```text
3*(4*3)=36.                                           (4.4)
```

A compatible triple would require three pairwise disjoint two-subsets of
the four-set `I_4`, again impossible.  The maximum is two.

## 5. Dependency and similar-assumption audit

The only affected claims in the charged packet are the unqualified sentence
in Section 6 and the proof supporting the phrase “zero, one, or two” in
Section 9.  Replace the Section 6 paragraph beginning after (6.2) by the
table and state-specific proofs above.  Section 9, item 3, remains literally
valid.

The broader global-state finiteness claim did not depend on the false
general maximum: independently, the exact budget

```text
sum_j B.C_j+sum_k nu_k=4,       nu_k>=1                (5.1)
```

would bound the number of contracted carriers by four.  The corrected
marked combinatorics sharpens that independent bound back to two.

A scan of the remaining finite assertions found no second use of the false
five-subset principle:

* the raw counts `70,20,24` are the binomial counts in (2.1), (3.2), and
  (4.2);
* the pair counts are now derived explicitly in (2.2), (3.3), and (4.4);
* the nine singular-F5 fibre tags come from Cartan integrality, marked
  `B_s/U_s` fibre vertices, and physical branch partitions, not from this
  subset-family bound;
* the target-line, actual-fibre, class-group, support-genus, and conditional
  ramification-energy formulas contain no contracted-carrier cardinality
  assumption.

The finite replay can be performed by listing the at most seventy subsets
in each marked row and testing (1.3); the largest possible triple check is
`binom(70,3)=54740`, well inside a seconds-scale standard-library audit.
The closed forms above are proofs and do not charge that replay as evidence.

This corrigendum does not improve proximity or effectivity, factor the
singular-F5 local different, control the Cartier multiplicities `nu_k`, or
charge the out-of-basis Euler/`A^1`-ruling proposal.  Every scope firewall
and remaining gap in the original sealed packet stays in force.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7659`.
- Body SHA-256:
  `488da252288cd9cc14ea797529d49b2d9db3c0a74bcab4308965ac07205182b6`.
- Frozen basis: `00b2fb0c682c5ca2a056af588a29b2421c1b7ce4`.
