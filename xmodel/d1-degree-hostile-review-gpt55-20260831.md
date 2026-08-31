# Hostile Review: D1-DEGREE Report (Sol)

## Hash Verification

Verified before mathematical review:

```text
0549dfafe339d20c67fe0d64a0bc713c1e64850013fbaab9f07f654c7fbf8fc2  inputs/d1-degree-bound-sol56-20260831.md
b9a83b0783f4b9b844bc881739e0b3c7c63efeb8683f862e007e6584af238696  inputs/pi1s4-close-residual-r2-opus5-20260831.md
bafe5e8929a77aa306e76ebdee1b300bbaf579a685f793cd8684ad861f041270  inputs/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md
```

All three frozen input copies match the charged hashes. Review uses those copies only.

## Sources Fetched

Fetched primary bytes by direct `curl -LfsS URL | shasum -a 256`, without saving PDFs:

```text
30b497466c1c27923a918db1c7277e90485667647fb3f2d6505f3f2c26ef420e  189637 bytes
Z. Jelonek, "The set of points at which a polynomial map is not proper",
Ann. Polon. Math. 58 (1993), 259-266.
https://matwbn.icm.edu.pl/ksiazki/apm/apm58/apm5834.pdf

febddbecb4c54d354fefca1a7e7730fcc18c0e2807fe3e03b5af8017b1d59d39  268049 bytes
Nguyen Van Chau, "Non-zero constant Jacobian polynomial maps of C^2",
Ann. Polon. Math. 71 (1999), 287-310.
https://matwbn.icm.edu.pl/ksiazki/apm/apm71/apm7135.pdf

a8476f967c1dd2f929cc80f494d05b1fc77d973558aa40bafef6e3a935a17fff  562720 bytes
Z. Jelonek and M. Lason, "Quantitative properties of the non-properness set
of a polynomial map", Manuscripta Math. 156 (2018), 383-397.
https://link.springer.com/content/pdf/10.1007/s00229-017-0965-0.pdf

da2c918f0aca141043333b05863a088abea6402c43fdd8e589aa074e81e9159a  229101 bytes
Jelonek-Lason arXiv v2 cross-check.
https://arxiv.org/pdf/1411.5011v2
```

Springer's page for Jelonek, "Testing sets for properness of polynomial mappings",
DOI `10.1007/s002080050316`, was reachable as article metadata only; its PDF endpoint
redirected to an access/cookie flow. I did not use any theorem unique to that paper.

## Item 1: Target Automorphism Unboundedness

Verdict: **PASS, with the nonempty-class caveat.**

Re-derivation. Let `F=(P,Q)` be a residual Keller map with geometric degree
`N=4`, and let `T_k(u,v)=(u,v+u^k)`. Then
`F_k=T_k o F=(P,Q+P^k)` is again Keller because `det dT_k=1`, and
`C(P,Q+P^k)=C(P,Q)`, so the function-field degree is still `4`.
Properness is target-isomorphism invariant:
`A_{F_k}=T_k(A_F)`. The finite normal cover can be replaced by
`T_k o q:Y -> A^2`; connectedness, degree, branch locus, local fibre
cardinalities, `a_D`, `a_p`, monodromy classes, normalisations, and incidences
are all pulled through the target isomorphism. Thus `Br=D_1`, `D_0`
unbranched, transposition meridians, disjoint local transpositions at
`Sing D_1`, and the two-component residual structure are preserved.

For `gamma(t)=(p(t),q(t))` birational on `D_1`, choose `k` with
`k deg p > deg q`. Then `T_k gamma=(p,q+p^k)` has coordinate degrees
`(deg p,k deg p)`, with no top-degree cancellation. Since the map remains
birational and the projective pullback of a generic line has degree
`k deg p`, the ordinary plane degree of `T_k(D_1)` is `k deg p`, unbounded.

The literal statement "no finite raw-degree bound exists" is only meaningful
after excluding the vacuous case. What is proved is: if the residual class is
nonempty, its target-automorphism orbit has unbounded ordinary `deg D_1`.
Therefore any promoted payoff must be target-invariant, or must first fix a
canonical target gauge.

## Item 2: Jelonek/Chau Typing

Verdict: **PASS.**

Jelonek 1993 Theorem 15 bounds the hypersurface of nonproperness by the
coordinate degrees:

```text
deg S_f <= ((prod_i deg f_i) - mu(f)) / min_i deg f_i.
```

For `F=(P,Q)`, `deg P=M >= E=deg Q`, and `mu(F)=4`, this gives
`deg A_F <= (ME-4)/E < M`, hence, integrally, `deg A_F <= M-1`.
Since `A_F=D_1 union D_0` is reduced with distinct curve components,
`d+deg D_0 <= M-1`, so `d <= M-2`. This is a coordinate-degree estimate,
not an `N=4` estimate. Jelonek-Lason Theorem 3.2 likewise uses the
algebraic degree `d` of the map and covers `S_f` by parametric curves of
degree at most `d-1`; it does not replace algebraic degree by geometric
degree. The "Testing sets" PDF was not available as primary bytes here and
is not needed: the hashed Jelonek/Jelonek-Lason statements already show the
claimed non-bound.

Chau 1999 applies to a nonzero constant-Jacobian map after a generic source
linear change making the polynomials monic in `y`. Theorem 4.4(E1) gives, for
each dicritical-image parametrisation, the same degree ratio as
`deg P / deg Q`. Because the residual has `s_1=s_0=1`, the parametrisation
degree pair of each component is a scalar multiple of the reduced target
degree pair. Write

```text
g=gcd(d,n),       (u,v)=(d/g,n/g),
gcd(deg P,deg Q)=k,       (deg P,deg Q)=k(u,v).
```

Chau Theorem B says either `v=1`, or
`4 = r u + s v >= min(2v,u)` with `r,s >= 0`, not both zero. For `v=2`,
coprimality gives `u` odd and `u>=3`, and `4=2*2` is allowed. For `v>=3`,
`min(2v,u)<=4` forces `u<=4`; with `u>v` and coprime this leaves only
`(u,v)=(4,3)`. Thus the charged trichotomy

```text
(u,1),       (odd u,2),       (4,3)
```

is exactly the `N=4` consequence. Finally, if `D_0` has scale `g_0` on the
same reduced pair, Jelonek gives `(g+g_0)u <= ku-1`; since `g_0>=1`, this
implies `g <= k-2 = gcd(deg P,deg Q)-2`. This still does not bound `g`
unless a separate bound on the target coordinate degrees is supplied.

## Item 3: The Identity d = 2g_L + c(Pi) + 2

Verdict: **PASS as an identity, FAIL as a degree bound.**

Here `g_L` must mean the genus of the compact normalization of the finite
degree-four curve `q^{-1}(L) -> L`, after compactifying a generic affine target
line `L` to `P^1`. Choose `L` avoiding `Sing D_1`, meeting `D_1` transversely
in `d` points, and generic enough that the line-complement map on
fundamental groups is surjective. Since the global degree-four cover is
connected, the restricted cover over `L-D_1` is connected.

Each of the `d` finite branch points has transposition monodromy, so its
ramification contribution is `1`. Let `Pi` be the product of the finite
transpositions; the monodromy over infinity is `Pi^{-1}`, and if `c(Pi)` is
the number of cycles on four letters, the ramification contribution over
infinity is `4-c(Pi)`. Riemann-Hurwitz for a degree-four cover of `P^1` gives

```text
2g_L - 2 = -8 + d + 4 - c(Pi),
so d = 2g_L + c(Pi) + 2.
```

Equivalently, the affine curve `q^{-1}(L)` has
`chi_c = 4(1-d)+3d = 4-d`, while its compactification has `c(Pi)` punctures,
again giving `d=2g_L+c(Pi)+2`. The derivation is sound, but it merely converts
raw degree into compact slice genus plus the infinity permutation. No promoted
input bounds `g_L`.

## Item 4: Noncoprime List Through d <= 9

Verdict: **PASS.**

Use only `d>n>=1`, `g=gcd(d,n)>=2`, and the Chau shapes for
`(u,v)=(d/g,n/g)`.

The family `(u,1)` is exactly `n=g` with `n|d` and `d/n=u>=2`. Through
`d<=9` this gives

```text
(4,2);
(6,2),(6,3);
(8,2),(8,4);
(9,3).
```

The family `(odd u,2)` gives `d=gu`, `n=2g`, with odd `u>=3`. Through
`d<=9` this contributes

```text
(6,4), (9,6).
```

The family `(4,3)` gives only `g=2` in this range:

```text
(8,6).
```

Combining and ordering by `d` yields exactly

```text
(4,2);
(6,2),(6,3),(6,4);
(8,2),(8,4),(8,6);
(9,3),(9,6).
```

The identity `d=2g_L+c(Pi)+2` imposes no additional pair-level deletion in
this range: for the listed even `d`, an even infinity permutation with
`c=2` or `4` is the only parity issue, and for `d=9`, `c=1` or `3` is
compatible with an integral nonnegative genus. The scale inequality
`g<=gcd(deg P,deg Q)-2` also gives no finite deletion without a bound on the
target degree gcd.

## Item 5: Coprime Kill-List Reduction

Verdict: **PASS, but only as an intermediate-table filter.**

The promoted coordinator table lists the `d<=9` survivors under `(C1)+A(3)`:

```text
(4,3),(5,4),(7,4),(8,3),(9,4),(9,8).
```

Because these are coprime, each pair is already its own reduced Chau pair
`(u,v)`. Chau's `N=4` trichotomy keeps `(4,3)` and deletes the other five:

```text
(5,4): min(8,5)=5 > 4;
(7,4): min(8,7)=7 > 4;
(8,3): min(6,8)=6 > 4;
(9,4): min(8,9)=8 > 4;
(9,8): min(16,9)=9 > 4.
```

Thus the elimination is sourced by the hashed Chau Theorem B together with
Theorem 4.4(E1)'s ratio identification for residual dicritical images. This
does not mean `(4,3)` is promoted as an actual residual escape; it is just the
only member of that intermediate `d<=9` coprime survivor table not removed by
the Chau shape filter. The separately promoted PI1-S4 Main Theorem is stronger
on its stated coprime scope.

## Item 6: CLOSE-RESIDUAL Invariant Caveat

Verdict: **PASS; the caveat is necessary.**

The CLOSE-RESIDUAL payoff "`deg D_1<=4` closes the residual" is a statement
about a chosen target embedding of the curve. Item 1 shows that the same
Keller/residual object can be moved by target automorphisms to arbitrarily
large raw degree without changing the cover problem. Therefore raw
`deg D_1<=4` is not an invariant campaign target.

The invariant formulation is sound:

```text
if min_{T in Aut(A^2)} deg T(D_1) <= 4, then apply CLOSE-RESIDUAL to T(D_1)
and pull the contradiction back by T^{-1}.
```

This uses only target-isomorphism invariance of the Keller property, the
asymptotic set, and the finite cover/monodromy data. It remains conditional on
the independent status of the CLOSE-RESIDUAL low-degree proof itself; this
review confirms the coordinate-invariance repair, not every proof step inside
that lane.

## Verdict And Recommendation

Overall verdict: **PROMOTE-AS-CORRECTED / PROMOTE AT TYPED SCOPE.**

Promote these statements:

```text
If the residual class is nonempty, ordinary plane degree of D_1 is unbounded
under target automorphisms preserving the Keller and residual data.

The meaningful degree target is d_min=min_T deg T(D_1), or a raw degree after
choosing a canonical target gauge.

Every escaping residual must satisfy gcd(d,n)=g>=2, reduced pair
(d/g,n/g) in (u,1), (odd u,2), or (4,3), and
g <= gcd(deg P,deg Q)-2.

d = 2g_L + c(Pi) + 2, where g_L is the compact genus of a generic restricted
degree-four cover over a target line and c(Pi) is the number of cycles of the
infinity permutation.

Through d<=9 the noncoprime Chau list is
(4,2); (6,2),(6,3),(6,4); (8,2),(8,4),(8,6); (9,3),(9,6).

The promoted coprime intermediate survivor table is Chau-filtered to (4,3).
```

Do **not** promote a literal unconditional "no finite bound exists" without the
nonempty-class/vacuity caveat, and do **not** promote any raw-degree CLOSE
payoff except in the invariant `d_min<=4` form or after a canonical target gauge
is specified. No CAS was run, no charged file or canonical ledger was edited,
and `jc2-lean` was not inspected.

<!-- BODY-END -->
