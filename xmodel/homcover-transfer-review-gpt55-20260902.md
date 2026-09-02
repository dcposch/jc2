# Hostile review: HOMCOVER-TRANSFER

Lane: HOMCOVER-TRANSFER-REVIEW  
Model: gpt-5.5  
Date: 2026-09-02  
Report target: 18-28 KB  
Charged inputs:

```text
fa52e816869fc689db23d5dfb6354be0cf88cb361f365dd9ff16f51c01d97883  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.kE2tEf/inputs/homcover-transfer-opus5-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.kE2tEf/inputs/mprime-alln-h2-opus5-20260902.md
```

Both SHA-256 hashes were verified before reading. I label the transfer report
`HT` and the MPRIME report `MI`. I also ran `python3 box/cover_h1.py`; all four
built-in controls passed, including the `Z (+) Z/3` trefoil control and the
transport-convention refusal. The computations below used independent inline
Python drivers and the repository `box/cover_h1.py`; no charged file was edited.

No exit-price assertion is made here, so no `charge_basis` line is emitted.

## Executive verdict

```text
THEOREM NO-PUSHFORWARD        CONFIRMED, with scope note.
Measured witness              CONFIRMED: Z (+) Z/2 -> Z after one relator.
THEOREM CENTRAL-RANK          CONFIRMED.  The r = j branch is impossible.
THEOREM CUSP-PARITY           CONFIRMED.
THEOREM ORBIFOLD-CAGE         CONFIRMED.
THEOREM CUSP-A-EMPTY          CONFIRMED at the stated typing:
                              N <= 6 proof/finite replay, N = 7 measured
                              exhaustive, N = 8 nonempty by exhibit.
GAP[CUSP-CAGE-KUROSH-DIVISOR] CONFIRMED as a real gap in MI.
Repair impact                 CONFIRMED: M >= 2 and CUSP-KILL survive; the
                              promoted CUSP-CAGE congruence block must be
                              replaced, and MI's N=4 escape is dead.
ACS-FIX-VS-DEFICIT            CONFIRMED exactly under H2 + 7.B, not beyond.
```

The important hostile point is positive: the charged transfer report is not
overclaiming the local-to-global torsion refutation. It correctly refutes only
the direction "local torsion forces global torsion." It does not prove a global
torsion theorem, and it does not close the one-cusp multibranch horn.

## 1. NO-PUSHFORWARD and the witness

**Verdict: CONFIRMED.**

HT names the two possible local-to-global sources at lines 116-120: the
link-at-infinity map and the local germ map. The theorem then treats an arbitrary
homomorphism `phi: Gamma -> G` at lines 122-135. That is enough for both maps
once the intended inclusion-induced homomorphism exists:

* if `phi` is surjective, then `phi(Lambda)=H`, so `Lambda^ab -> H^ab` is a
  quotient map;
* if `phi` is not surjective, then only `phi(Lambda) <= H`, hence there is a map
  to `H^ab` but no injectivity or torsion preservation.

This covers the two algebraic directions that matter for pushforward: source
torsion may be killed by a quotient, and source torsion may also be invisible
when the image is proper. If someone intended a reverse restriction map
`G -> Gamma`, that is not a local-to-global map supplied by the topology and is
not needed for the refutation.

I replayed the witness in HT:142-152. With the braid presentation
`B_3=<s1,s2 | s1 s2 s1 = s2 s1 s2>` and the left-action representation

```text
s1 = (1,2,3,0)
s2 = (1,3,0,2)
w  = (s1 s2^-1)^3
```

both the braid relator and `w` evaluate to the identity. Passing through
`to_transport_convention`, `cover_h1` gives:

```text
B_3 cover H_1                         = Z^1 (+) Z/2
B_3 / <<(s1 s2^-1)^3>> cover H_1      = Z^1
```

So the witness is not cosmetic. The added relator is killed by `rho` and still
removes the torsion in the stabilizer cover. That is exactly the failure mode a
local-to-global torsion theorem would have to exclude.

Scope note: HT's theorem refutes transfer of torsion from a local/link group to
the global cover. It does not say global covers cannot have torsion for other
reasons, and it does not decide whether the link-at-infinity map is actually
surjective.

## 2. CENTRAL-RANK

**Verdict: CONFIRMED.**

HT:367-379 proves the sharp rank statement. The proof is short and survives
checking. In the case-(A) substrate there is a central extension

```text
1 -> Z_H -> H -> Delta -> 1
```

with `Z_H ~= Z`, an infinite cyclic group. Kurosh gives
`Delta ~= F_r * C_1 * ... * C_k` with finite cyclic `C_i`, so
`H_2(Delta;Z)=0`: `H_2(F_r)=0`, `H_2(C_n)=0`, and homology of a free product
splits in degree two. The five-term exact sequence for the extension therefore
injects `Z_H` into `H^ab`. Hence

```text
rank H^ab = rank Delta^ab + 1 = r + 1.
```

For a Keller cover, the plane-curve complement gives `H^ab ~= Z^j`, so
`j=r+1`, i.e. `r=j-1`. There is no remaining case in which `r=j` can occur
without making the central cyclic image finite in `H^ab`, which the injection
forbids.

This directly corrects MI. MI allows `r in {j-1,j}` at lines 537-538, and its
worked N=4 escape at lines 565-570 uses exactly `r=j=2`. That branch is not
merely unproved; it is incompatible with the five-term sequence.

## 3. CUSP-CAGE gap and repair impact

**Verdict: GAP confirmed in MI; repair confirmed.**

The gap is real in the charged MPRIME report:

* MI:535-539 asserts
  `Delta ~= F_r * (Z/p)^{*u} * (Z/q)^{*v}` and then derives
  `r in {j-1,j}` plus `u<=1`, `v<=1`.
* MI:541-545 promotes congruences and the derived bound `N >= M >= pq+1` from
  that full-factor model.
* MI:565-570 records the N=4 escape `(p,q)=(3,4), M=4, (u,v)=(1,0), r=j=2`.

Kurosh does not give full `Z/p` and `Z/q` factors for an arbitrary finite-index
subgroup of `Z/p * Z/q`; it gives intersections with conjugates of the finite
factors, hence subgroups. Proper divisors are genuine. For example, in
`C_6 * C_5`, the kernel of the map to `C_2` sending the `C_6` generator to the
nontrivial element intersects `C_6` in `C_3`, not in all of `C_6`.

The cyclicity conclusion is also misphrased in MI. Since CENTRAL-RANK gives
`Delta^ab ~= Z^j / <zeta>` up to the free part, the finite torsion in
`Delta^ab` must be cyclic. A direct sum of finite cyclic Kurosh-factor
contributions is cyclic exactly when the contributing orders are pairwise
coprime. It is not equivalent to "at most one factor over the p-side and at most
one over the q-side"; two p-side factors of coprime orders, such as `2` and `3`
when `p=6`, are not excluded by cyclicity alone.

The repair in HT:412-440 is the right replacement. It moves from the false
full-factor Kurosh statement to the orbifold-cover statement with local degrees
`m_i | p`, `l_i | q`, and cone orders `p/m_i`, `q/l_i`. This preserves:

* `M >= 2`: if `M=1`, then `Delta=Z/p * Z/q` has `r=0`, and CENTRAL-RANK gives
  `j=1`, contradicting the CUSP-KILL consequence `j>=2`.
* CUSP-KILL: the proof of MI:512-533 handles the `j=1` case by Lin-Zaidenberg,
  identifies `H` with the same torus-knot group, then uses rational Euler
  characteristic and Campbell. It does not need the later Kurosh divisor
  congruences.
* COR 7.2/nonregularity: MI:554-562 depends on the Galois-cover/Campbell
  argument, not on the incorrect cage congruences.

Exact promotion impact: the promoted CUSP-CAGE paragraph MI:535-545 should not
be quoted as written. Replace it with CENTRAL-RANK plus HT's ORBIFOLD-CAGE
conditions `(C-1)` through `(C-4)` and CUSP-PARITY. Delete the general
full-factor congruence cases and the general `N>=pq+1` consequence. Keep
CUSP-KILL, keep nonregularity, and keep `M>=2` with the new proof above. MI's
N=4 "not closed here" escape is invalid; the N=4 H2 residual loses case (A) and
is exactly the B3 cusp-plus-multibranch horn, as HT:558-566 says.

## 4. ORBIFOLD-CAGE and CUSP-PARITY

**Verdict: both CONFIRMED.**

For ORBIFOLD-CAGE, the Euler characteristic algebra in HT:428-433 checks out.
The degree-`M` orbifold cover has underlying surface with genus `g` and `c`
boundary components, so the Kurosh free rank is `r=2g+c-1`. CENTRAL-RANK gives
`2g+c=j`. Substituting this into the orbifold Euler characteristic identity and
using `sum m_i = sum l_i = M` gives

```text
s + s' = M + 2 - j.
```

The torsion condition `(C-2)` follows because `Delta^ab` is the quotient of
`Z^j` by one cyclic central image, so its torsion is cyclic; hence the finite
cone-order contributions must be pairwise coprime. Condition `(C-3)` follows
from the congruence on a block orbit:

```text
k_i * (p/m_i) == 1 mod kappa
```

and similarly for `q/l_i`. Condition `(C-4)` follows because `rho(z)` is central
in a transitive group and therefore semiregular: each block-orbit of `alpha`
becomes one point-orbit exactly when `k_i` is invertible modulo `kappa`.

For CUSP-PARITY, HT:448-458 is also correct. The sign character factors through
`G^ab ~= Z<m>`, with `alpha -> q m` and `beta -> p m`. The meridian cycle type
`1^a prod_l mu_l^{s_l}` gives

```text
eps = sgn rho(m) = (-1)^{sum_l s_l (mu_l - 1)}.
```

Then `sgn rho(alpha)=eps^q`, `sgn rho(beta)=eps^p`, equivalently
`(-1)^(N-s)=eps^q` and `(-1)^(N-s')=eps^p`.

Spot-check on the explicit N=8 survivor below, with `(p,q,N)=(2,3,8)`:

```text
alpha = (1,2,4,6,0,7,5,3)   cycle type (4,4), cycles s=2
beta  = (1,3,4,2,5,0,7,6)   cycle type (6,2), cycles s'=2
z=alpha^2=beta^3            order kappa=2, so M=4
m=alpha beta^-1             cycle type (3,3,1,1), so a=2 and eps=+1
```

Here `j=2` from homology. ORBIFOLD-CAGE gives
`s+s'=4=M+2-j`. The p-side local degrees can be `(2,2)`, giving no nontrivial
p-cone order; the q-side can be `(1,3)`, giving finite order `3`. This satisfies
pairwise coprimality and `gcd(3,kappa)=1`. Parity gives
`sgn(alpha)=+1=eps^3` and `sgn(beta)=+1=eps^2`.

## 5. ACS-FIX-VS-DEFICIT

**Verdict: CONFIRMED exactly under H2 + 7.B.**

The hypotheses are exactly the ones HT states. MI defines the generic meridian
cycle data at lines 83-88:

```text
N = a + sum_l s_l mu_l,    W = N-a = sum_l s_l mu_l,
7.B' says every mu_l >= 2 under H2.
```

Therefore the generic meridian cycle type is
`1^a prod_l mu_l^{s_l}` with every nontrivial cycle length at least two. The
number of fixed points is exactly `a`; there is no hidden length-one dicritical
cycle left to inflate `#Fix`. HT:254-272 uses no extra hypothesis beyond
MPRIME `[P3]` plus 7.B' under H2.

The companion identity-meridian case is consistent because it is outside this
scope. The ideation warning says an N=4 companion with `W_2=1` has
`a^(2)=3`, and since no element of `S_4` has exactly three fixed points, its
meridian must be the identity with four fixed points. That is a reducible
profile: the sheet is lost at infinity, not through local monodromy. HT keeps
that warning out of H2 at lines 269-271. So the repair is not "a=#Fix always";
it is "a=#Fix for the H2 meridian cycle type after 7.B removes mu=1."

## 6. CUSP-A-EMPTY

**Verdict: CONFIRMED at the stated typing.**

The N=4 desk proof in HT:471-488 checks out. N4-PIN gives `a=2`, `W=2`, one
dicritical `(s_1,mu_1)=(1,2)`, meridian type `(2,1,1)`, and `eps=-1`.
CUSP-KILL gives `j>=2`; since `j<=a=2`, `j=2`. CENTRAL-RANK gives `r=1`.
With `M kappa=4` and `M>=2`, `M` is `2` or `4`. Then `(C-1)` gives
`s+s'=M`, and CUSP-PARITY forces `p,q` both odd. The partition analysis then
forces either an even divisor on one side or a common factor, contradiction.
The second trefoil/transposition proof in HT:490-500 is also sound: for the
remaining `(2,3)` partition, `G_{2,3}=B_3` is generated by two conjugates of the
meridian; two transpositions cannot act transitively on four letters.

The N=5 desk proof in HT:502-516 also checks. Since `5` is prime, `M=5`,
`kappa=1`, and `j` is `2` or `3`. The three cases `(j,a)=(2,2),(2,3),(3,3)`
are exhausted. In each case, parity and the partitions of `5` force either
wrong parity, repeated non-coprime cone orders, an even `p` or `q` where both
must be odd, or a common divisor.

For N=6 and N=7 I reran the finite enumeration independently. My filter order
differs from HT's, so my intermediate counts are not meant to reproduce its
"1673 reps" number. The verdict is the same, and the checks are stricter at the
front gate:

```text
N=6:
  numerical cage pairs = 4
  pairs = (2,3), (2,5), (3,2), (5,2)
  relation-satisfying pairs checked = 35,712
  transitive pairs checked          = 19,920
  H2+cage+parity cheap survivors    = 0
  homology survivors                = 0

N=7:
  finite/collapsed representatives with p,q<=130 = 22
  pairs = (2,3), (2,7), (2,21), (2,35), (2,49), (2,63),
          (2,77), (2,91), (2,105), (2,119), (3,2), (3,10),
          (7,2), (10,3), (21,2), (35,2), (49,2), (63,2),
          (77,2), (91,2), (105,2), (119,2)
  relation-satisfying pairs checked = 4,999,152
  transitive pairs checked          = 4,014,720
  H2+cage+parity cheap survivors    = 0
  homology survivors                = 0
```

This confirms the N=7 result at the same typing HT gives it: measured
exhaustive, not upgraded to a symbolic proof of the unbounded-family collapse.
The count I would promote is "22 representatives, zero survivors"; the larger
raw/transitive counts are audit evidence only.

For N=8, nonemptiness is genuine. The explicit `(2,3)` representation from the
spot-check satisfies:

```text
alpha^2 = beta^3 = (2,4,0,5,1,3,7,6)
rho is transitive
|rho(G)| = 24, so it is nonregular
meridian m = alpha beta^-1 has type (3,3,1,1), hence a=2
M=4, kappa=2, j=2
H_1 of the stabilizer cover = Z^2, torsion-free
```

With `alpha` fixed to the displayed `(4,4)` permutation, my replay finds exactly
16 admissible `beta` choices, matching HT's `(2,3)` base-cell count at
HT:546-548. I did not need the full `192` count to confirm the theorem-level
frontier. What is confirmed is the charged mathematical claim: case (A) is
empty through N=7, and the first group-theoretic survivors occur at N=8.

## 7. Line-by-line impact on the promoted text

The safe integration delta is:

```text
KEEP     MI CUSP-KILL, with its classical-theorem dependencies.
KEEP     MI COR 7.2 nonregularity.
KEEP     the conclusion M>=2 for j>=2, but derive it from CENTRAL-RANK.
REPLACE  MI:535-545 CUSP-CAGE with CENTRAL-RANK + ORBIFOLD-CAGE + CUSP-PARITY.
DELETE   the general full-factor congruence cases and the general N>=pq+1 bound.
DELETE   the MI N=4 escape as a live residual; it uses r=j=2.
PROMOTE  case (A) empty for 4<=N<=7, measured at N=7, nonempty at N=8.
DO NOT   claim anything about case (B3), (9,6,2), (9,6,4), or JC2 globally.
```

This is a strengthening of the cusp cage, not a weakening of CUSP-KILL. The
only promoted material it invalidates is the exact Kurosh/congruence packaging
and the N=4 `r=j` escape.

## 8. FALLACY-v2 audit

Flag/place/series are kept separate. NO-PUSHFORWARD treats local/link groups
and global groups as connected by a homomorphism, not as the same object. The
only identification used later is the case-(A) Lin-Zaidenberg identification of
`pi_1(C^2 \ A_F)` with the torus-knot group, which MI supplies.

Floor/attainment is respected. The N=8 representations are only
group-theoretic survivors, not realized Keller maps. The report must not turn
them into actual exits.

Carrier/attainment is respected. The N=7 exhaustion is measured at the
representation-cage level and remains typed as measured because the symbolic
collapse of the unbounded families is not proved.

Variable/ring map issues are not present; no Groebner or `sat()` computation is
used. The only load-bearing convention is the permutation transport convention
in `box/cover_h1.py`, and I used `to_transport_convention` in every homology
calculation.

Prime labels are harmless: `s'` is the q-side cone-preimage count, not a
derivative. The dicritical `s_l` does not get merged with the orbifold `s`.

No gap is filled by cap or analogy. The failed local-to-global transfer is
reported as refuted; the unproved link-at-infinity surjectivity and mod-p
irregular-cover divisibility remain outside this review; the B3 horn is
untouched.

## 9. Replay method notes

The independent enumerator used these gates, in this order. First it generated
the numerical orbifold cells from divisors `M|N`, `M>=2`, `kappa=N/M`, choices
`2<=j<=a<=N-2`, meridian partitions of `N-a` into parts at least two, and
partitions of `M` into p-side and q-side local degrees. It enforced
`gcd(p,q)=1`, CUSP-PARITY, pairwise coprimality of the nontrivial cone orders,
and coprimality with `kappa`. This reproduced HT's visible cell counts:

```text
N=4: 0 pairs
N=5: 0 pairs
N=6: 4 pairs, exactly (2,3), (2,5), (3,2), (5,2)
N=7: 22 finite representatives with p,q<=130
N=8: 40 finite representatives with p,q<=200
```

Second, for each finite representative it enumerated permutations `A,B in S_N`
with `A^p=B^q`. It computed the central image `z`, `kappa=order(z)`,
`M=N/kappa`, the meridian `m=A^e B^f` with `e q + f p = 1`, and then imposed
transitivity, `2<=#Fix(m)<=N-2`, the parity identities, and
`j=M+2-#cycles(A)-#cycles(B)`. Only after those cheap gates did it call
`cover_h1` on `<alpha,beta | alpha^p=beta^q>`, using
`to_transport_convention([A,B])`, and require torsion-free `H_1` of rank `j`.
Finally it discarded regular actions by computing the generated permutation
group order.

This filter order explains the one harmless count discrepancy with HT. HT says
"1673 reps filtered" for N=6; I count all relation-satisfying and transitive
pairs first, and in that order no N=6 pair reaches the homology call. The
mathematical comparison point is therefore not the intermediate number but the
terminal count, which is zero in both runs.

The N=8 fixed-alpha normalization was checked only where needed. For
`(p,q)=(2,3)`, fixing

```text
alpha = (1,2,4,6,0,7,5,3)
```

and scanning all `beta in S_8` gives 33 cube roots of `alpha^2`, of which 16
pass the full gate. That matches HT's base-cell line and gives a concrete
audit bridge between my labelled-pair enumeration and HT's normalized count.

## Final verdict block

```text
NO-PUSHFORWARD          CONFIRMED.
WITNESS                 CONFIRMED: one relator kills Z/2 in the trefoil cover.
CENTRAL-RANK            CONFIRMED: rank H^ab = r+1, so r=j-1.
CUSP-PARITY             CONFIRMED.
ORBIFOLD-CAGE           CONFIRMED.
CUSP-A-EMPTY            CONFIRMED: N<=6 proof/finite replay; N=7 measured
                         exhaustive with 22 representatives and 0 survivors;
                         N=8 survivor exhibited.
CUSP-CAGE GAP           CONFIRMED in MI:535-545 and MI:565-570.
REPAIR                  CONFIRMED: preserves M>=2 and CUSP-KILL; replaces the
                         promoted Kurosh congruence block.
ACS-FIX-VS-DEFICIT      CONFIRMED under exactly H2 + 7.B; reducible
                         identity-meridian companion remains consistent and
                         outside scope.
PROMOTION CONSEQUENCE   Case (A) is gone for 4<=N<=7.  At N=4 under H2, the
                         residual is exactly case (B3), not case (A).
NON-CLAIMS              No all-degree JC2 closure, no B3 kill, no geometric
                         realization of N=8 survivors, no (9,6,2)/(9,6,4)
                         global transfer.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19019`.
- Body SHA-256:
  `d61bc06a5327b5bde3ad812fdd2e27709c06f08fd13bbf62b7784dc30ab1eca9`.
- Frozen basis: `ecbcec7a26a4d8afd2d10f82a32e341aaccb4949`.
