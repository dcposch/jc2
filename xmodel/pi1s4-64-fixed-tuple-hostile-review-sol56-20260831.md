# Hostile review: fixed generating transposition 6-tuples for the (6,4) cable

## 0. Scope, frozen inputs, and method

I created this report's header skeleton before touching an input. I then ran
`shasum -a 256` on the three frozen copies. All three matched the charge exactly:

```text
a60887501137251f50f1ce7bf8ddc8921b1f22e20a4aebced47ce35699a0fad8  pi1s4-64-fixed-tuple-opus5-20260831.md
aa873151fca957516e4a2ffe94d79733659307a038d252b2a50d94bcd4f1a9eb  row-sweep-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

References below of the form `fixed:Lx-y`, `sweep:Lx-y`, and `integration:Lx-y`
mean those frozen copies. I used right-to-left permutation composition, matching the
displayed witness. I ran no CAS, enumeration, or other computational search. The only
literature fetch was the streamed primary triple-cover source recorded and hashed in
§9; no source file was saved. Thus the charged Python enumeration is treated only as
an unverified redundancy claim; the count below is re-derived by hand. The report
makes no exit-price assertion.

## 1. Explicit cable braid and exponent of the inclusion

**Verdict: CONFIRMED, with one wording qualification.** Put `x=p(t)`, `y=q(t)`,
`s=t^{-1}`, and use the infinity chart `u=1/x`, `v=y/x`. After a formal
reparametrization, `v=s^2` and

```text
u=c_6s^6(1 + even powers through s^8 + gamma_9 s^9 + ...),  gamma_9 != 0.
```

For `xi=x^{-1/6}`, inversion gives `s=alpha xi(1+even powers+ a_9xi^9+...)`,
with `a_9 != 0`. Therefore

```text
y=s^2x = c xi^(-4)(even unit + c'xi^9+...),
```

so the first exponents separating different coarse roots and the two roots inside
one coarse cluster are respectively `2/3` and `(10-beta_1)/6`; at `beta_1=15`
the latter is `-5/6`. The six roots consequently form the three two-element
blocks `B_i={j:j=i mod 3}`. Their centres execute `delta_3^2`, and the braid has
the framed-cable normal form

```text
rho_infty = C_2(delta_3^2) (sigma^k_1,sigma^k_2,sigma^k_3).
```

The exponent is especially easy to check without assigning a fractional twist to
any nonclosed tube. There are 12 cross-tube pairs, each contributing twice winding
`2/3`, and three in-tube pairs, each contributing twice winding
`(10-beta_1)/6`. Hence

```text
e(rho_infty)=16+(10-beta_1)=26-beta_1,
e(C_2(delta_3^2))=2^2 e(delta_3^2)=4*4=16,
e(iota)=k_1+k_2+k_3=10-beta_1.
```

Thus `e(iota)=-5` at `beta_1=15` (`fixed:L107-172,181-187`). The sentence that
each tube “contributes `-5/3`” should be read only as an average winding account:
the outer braid permutes tubes, so no individual closed-tube winding determines an
individual `k_i`. Only their integer sum is invariant and is all the later proof uses.

## 2. Four-way exponent cross-check for the infinity braid

**Verdict: numerical identity CONFIRMED; “four independent derivations” is too
strong.** The four calculations reduce as follows.

1. The finite projection has total ramification `deg p'=5`, while three ordinary
   nodes contribute three positive squares, so `e=5+3*2=11`. Five *simple*
   tangency factors require a generic/simple projection; without it, the invariant
   statement is that their total exponent is five.
2. The genus split gives `delta_infty=7`, hence
   `e=(d-1)^2-2delta_infty=25-14=11`.
3. The winding calculation of §1 gives `16-5=11` directly.
4. The cable is the `(2,3)` cable of the trefoil: blackboard doubling starts with
   slope `2e(delta_3^2)=8`, then the inner exponent `-5` leaves slope `3`.
   Its genus is `2g(T(3,2))+(2-1)(3-1)/2=3`, so the standard quasipositive
   genus equality gives `e=2g+d-1=6+5=11`.

The first three are sufficient. The fourth is a consistency check conditional on
the standard quasipositive-surface equality and the already derived cable framing;
it is not independent of the cabling computation. All specializations to `11`
remain conditional on the provisional row datum `beta_1=15` and hence
`delta_infty=7` (`fixed:L195-220`; `integration:L70-92`).

## 3. Outer-level analysis on three tubes

**Verdict: CONFIRMED-AS-CORRECTED; not promotable as written.** The sentence that
promoted coprime Theorem A “reruns verbatim” (`fixed:L228-230`) is outside its
scope: its entries are transpositions generating `S_4`, whereas the outer entries
are even block products and in (O4) generate `A_4`. The needed result fortunately
has a direct two-line proof. Fixedness of `(Pi_1,Pi_2,Pi_3)` under `delta_3^2`
gives

```text
Pi_3=Pi_1,   Pi Pi_1 Pi^-1=Pi_2,   Pi Pi_2 Pi^-1=Pi_1,
```

equivalently, for `x=Pi_1=Pi_3`, `y=Pi_2`,

```text
xyx=yxy=Pi.
```

Because a product of two transpositions is the identity, a 3-cycle, or a
nonidentity element of the Klein four group `V_4`, the exhaustive solutions are:

```text
O1: x=y=e;
O2: x=y=tau in V_4\{e};
O3: x=y=rho, a 3-cycle;
O4: x=rho, y=rho v, v in V_4\{e}.
```

For the 3-cycle branch, passage to `A_4/V_4` first forces `y in rho V_4`;
substitution verifies the braid relation for all four `v`, with `v=e` giving O3.
In O4,

```text
H=<rho,rho v>=<rho,v>=V_4 semidirect <rho>=A_4,   Z(H)=1,
Pi=rho^-1 v rho in V_4\{e},   Pi^2=e.
```

This also states exactly what the promoted package contributes: A′(1) gives
block-product fixedness; A′(2) gives the conjugacy orbit; A′(3) puts `Pi^2` in
the centre of `<Pi_1,Pi>`, which is `A_4` in O4; A′(4) is silent because
`4` does not divide `6`. References to A′(5) at `fixed:L271-272,505-506` must
be removed: the frozen scope says only A′(1)–(4) are available
(`sweep:L34-45,169-180,309-314`). The overloaded charged notation `V` should
likewise be replaced by `V_4` and `V_4\{e}`. The direct enumeration and
centrelessness conclusion themselves are sound (`fixed:L232-276`).

## 4. Fixed-point equations, classification, count, and witness

**Verdict: CONFIRMED-AS-REPAIRED.** For blocks `A_i` with products `Pi_i`, direct
iteration of the cabled Hurwitz action gives

```text
C_2(delta_3^2)(A_1,A_2,A_3)
 = (w' A_2 w'^-1, w A_3 w^-1, A_1),
w=Pi_1Pi_2,  w'=Pi Pi_2^-1.
```

Thus, with `S_i=sigma^k_i A_i`, (F1)–(F3) at `fixed:L297-310` are exact:

```text
A_1=w'S_2w'^-1,  A_2=wS_3w^-1,  A_3=S_1.
```

Back-substitution gives `A_1=G sigma^K(A_1)G^-1`, where `G=w'w` and
`K=sum k_i`; in O4, `G=rho=Pi_1`. For `A_1=(alpha,beta)`, `c=alpha beta`,
the identities `sigma^(2m)A_1=c^mA_1c^-m` and
`sigma^(2m+1)A_1=c^m sigma(A_1)c^-m` reproduce the charged solve. At
`K=-5`, O1 gives six constant non-generating tuples, O2 is inconsistent,
O3 gives `8*3=24` tuples contained in an `S_3`, and O4 gives

```text
beta=rho^-1 alpha,
alpha one of the three transpositions in supp(rho),
v in V_4\{e};
```

these generate `S_4` because `A_1` generates the `S_3` on `supp(rho)` and
the conjugated middle block contains a transposition moving the fourth letter.

The exact `72` is an orbit-stabilizer count, not an appeal to the charged Python
run. Simultaneous `S_4` conjugation is transitive on the `8*3=24` pairs
`(rho,alpha)`: the centralizer `<rho>` cycles the three admissible `alpha`, and
the stabilizer of a fixed ordered pair is trivial. The three choices of
`v in V_4\{e}` therefore give three distinct free orbits of size `24`, hence
`3*24=72`. Equivalently the injective parameters give `8*3*3=72`. Together
with O1 and O3, the hand classification also yields `102` fixed tuples total,
exactly `72` of them generating; the claimed machine enumeration is unnecessary.

For the displayed witness, all relations check by hand. With

```text
rho=(123), alpha=(12), beta=(23), v=(12)(34),
T=((12),(23),(13),(34),(12),(23)),
```

right-to-left multiplication gives

```text
Pi_1=Pi_3=(123),  Pi_2=(134)=rho v,
Pi=(13)(24)=rho^-1 v rho,
w=(234),  w'=(124),  G=w'w=(123).
```

Conjugation by `Pi` interchanges `Pi_1` and `Pi_2`, so the outer fixedness and
braid relation hold. For `(k_1,k_2,k_3)=(0,-5,0)`, the order-three pair action
gives `S_2=sigma^-5((13),(34))=((14),(13))`. Conjugating by `w'` gives
`((12),(23))=A_1`; conjugating `S_3=A_3=((12),(23))` by `w` gives
`((13),(34))=A_2`; and `S_1=A_1=A_3`. These are F1, F2, and F3 respectively.
Also `sigma^-5 A_1=((13),(12))`, whose conjugate by `G=(123)` is `A_1`,
verifying the collapsed equation (5.1). The entries `(12),(23),(34)` generate
`S_4`; `Pi` has two cycles, so `6=2g_L+2+2` gives `g_L=1`.

Finally, `sigma_2 T=((12),(12),(23),(34),(12),(23))`: positions 1–2 are
equal and positions 4–5 are disjoint. Hence the displayed conjugates of
`sigma_1` and `sigma_4^2` really stabilize `T`. This verifies the advertised
individual tangency and node relations, but not the still-OPEN simultaneous
`5 sigma + 3 sigma^2` factorization (`fixed:L403-430,484-500`).

## 5. Nonemptiness criterion

**Verdict: theorem CONFIRMED after filling an omitted general-`K` case check.** The
charged text generalizes O4 from `K=-5` but does not explicitly re-kill O1–O3
for arbitrary `K` (`fixed:L365-381`). The repair is short and essential to the
“only if” direction. In O1 every two-entry block is `(a,a)` and the equations
make all entries the same. In O2 every solution uses only the same two disjoint
transpositions (possibly swapped). In O3 every factorization of `rho` and every
conjugator is supported on `supp(rho)`. These cases generate at most `C_2`, a
four-group, and `S_3`, respectively, for every `K`; none generates `S_4`.

In O4, put `A_1=(alpha,beta)`, `alpha beta=rho`, and `G=rho`. If `K=2m`,
the fixed equation says that `rho^(m+1)` centralizes both transpositions. A
nontrivial 3-cycle in `S_4` centralizes no transposition, so this is possible
exactly when `m+1=0 mod 3`, i.e. `K=4 mod 6`. If `K=2m+1`, write
`h=rho^(m+1)`. The case `h=e` would force `alpha=beta`. Otherwise the product
condition forces `alpha` to invert the 3-cycle on the same support and then
forces `h=rho`, i.e. `K=1 mod 6`. Both parities therefore say precisely

```text
an S_4-generating fixed tuple exists  iff  K=1 mod 3.
```

Each admissible parity has the same three factorizations of each `rho` and hence
the same 72-count. Since `K=e(iota)=10-beta_1`, this is equivalent to
`beta_1=0 mod 3`. This proves both directions of the advertised criterion, and
at `beta_1=15` supplies the 72 witnesses. The result is conditional only when
specialized to the provisional census assertion that the residual row has
`beta_1=15`; the group-theoretic criterion itself is exact.

## 6. Comparison with the (4,2) case

**Verdict: CONFIRMED only with a narrowed meaning of “structurally absent.”** At
`(4,2)`, `(d',n')=(2,1)` and A′(4) forces the two block products to be equal;
the resulting outer group is cyclic, and the promoted `(4,2)` solve cannot
generate `S_4`. At `(6,4)`, `(d',n')=(3,2)`, A′(4) is inapplicable, and O4
exhibits unequal block products generating the centreless group `A_4`. A′(3)
then merely requires the already true relation `Pi^2=e`.

Thus the **A′(4) equal-product collapse** is genuinely unavailable. The broader
claim that `(6,4)` has “no analogue” of any `(4,2)` obstruction overstates what
was proved: the local-factorization problem can still obstruct all 72 tuples.
As in §3, “A′(3)/A′(5)” must be replaced by A′(3) alone
(`fixed:L502-507`).

## 7. Coverage and row-uniformity

**Verdict: `(6,4)` coverage CONFIRMED-AS-CORRECTED; the claimed `(8,4)` transfer
is REFUTED at fixed-braid level.** The sentence that conjugacy merely “relabels”
the tuples (`fixed:L518-523`) is imprecise. If `rho'=b rho b^-1`, the actual
bijection is

```text
T |-> b.T : Fix_gen(rho) -> Fix_gen(rho').
```

Hurwitz moves preserve the transposition conjugacy class and the subgroup
generated by all entries, so this proves conjugacy invariance of both cardinality
and generation.

There is also a direct row-uniform argument: §2 puts every place of the specified
type, in transported tube coordinates, in the form
`C_2(delta_3^2)(sigma^k_1,sigma^k_2,sigma^k_3)` with integer exponents whose
sum is `-5`; §§4–5 solve **every** such integer distribution. The individual
residues change the actual 72 tuples, but neither existence, count, nor O4 form.
This closes the `k_i` quantifier. For formal promotion, the report should state or
cite the standard Puiseux-braid conjugacy/tubular-normal-form lemma rather than
assert it in one sentence; its asymptotic calculation substantially supplies the
proof. The displayed O4 shape is literal only in the chosen tube coordinates.
Subject to that repair, the result covers the whole `(6,4)`, `beta_1=15` row,
not merely the attained curve. Its application to that row remains conditional on
the frozen provisional census (`fixed:L511-523`; `integration:L70-92`).

The shear `P=p+q^2` changes the chosen vertical degree from 6 to 8. It preserves
the affine complement, but it does not turn a merely necessary fixed `B_6` tuple
into a fixed generating `B_8` tuple; no actual complement representation was
constructed. The frozen sweep proves target-isomorphism yet still leaves the
`(8,4)` fixed-tuple question OPEN (`sweep:L293-320`). Therefore
`fixed:L103-105,537-540` cannot transfer this braid theorem “verbatim.”

## 8. Restriction through the fold

**Verdict: PASS AFTER REWRITE; promotable as a pullback-surjectivity lemma, not as
a solution of the union complement.** The geometric preimage can be made exact.
Set

```text
A(x,y)=x^2-y^3-2xy+(2/3)y^2-(16/27)x+(1/9)y-1/9.
```

The witness identity in `sweep:L143-149` is `A(r^2,q)=8r/27`. Thus an equation
of the sextic is `A(x,y)^2-(64/729)x=0`, and under `nu(u,y)=(u^2,y)` it factors
as

```text
(A(u^2,y)-8u/27)(A(u^2,y)+8u/27).
```

These are the distinct components `D'` and `D'^-`, proving
`nu^-1(D)=D' union D'^-` rather than merely asserting it.

For the group argument distinguish the target fold line `L_t={x=0}` from the
source line `L_s={u=0}` and put

```text
X=C^2-D,                 X^o=X-L_t,
X~=C^2-(D' union D'^-),  X~^o=X~-L_s.
```

Then `nu:X~^o -> X^o` is a connected unbranched double cover (a complex plane
curve complement is path-connected). Hence its image `K` in
`G=pi_1(X^o)` has index two. A generic meridian `mu_t` has odd deck parity,
so `G=K<mu_t>`. The inclusion `j:X^o -> X` is surjective on fundamental groups,
and `j(mu_t)=1`: at a point of `L_t-D`, the meridian bounds a small transverse
disk after the line is restored.

Given a surjection `phi:pi_1(X)->S_4`, therefore,

```text
S_4=phi j(G)=phi j(K),
```

so its pullback to `pi_1(X~^o)` is surjective. It factors through `pi_1(X~)`:
a source-line meridian maps under the fold to `mu_t^2` (equivalently, the
branched map already extends across `L_s`), hence is killed. A generic meridian
of either lifted component is away from the fold line, where `nu` is locally
biholomorphic, and maps to a meridian of `D`; both therefore map to
transpositions. This proves the displayed conclusion at `fixed:L554-570` after
replacing “restricts” by “pulls back,” stating connectedness, identifying the
index-two subgroup, and adding the descent across `L_s`.

The promoted coprime result that each component separately has cyclic complement
does not determine the complement of their union. Their intersections and the
resulting van Kampen relations remain to be analyzed. Thus the restriction
theorem is safe, while “two separately settled components” is only a reduction,
not a closing theorem.

## 9. Triple-cover reduction sketch

**Verdict: group-theoretic opening CONFIRMED; the global-cubic and displayed
discriminant reduction are REFUTED.** Quotienting by the Klein four group does
give `S_4/V_4 ~= S_3`; transpositions remain transpositions, while two disjoint
transpositions have the same image because their product lies in `V_4`. The
quotient is still surjective and its degree-three action is transitive, so the
associated unbranched cover of the complement is connected. Extending it to a
normal finite flat triple cover of `A^2`, with exactly the asserted branch
scheme at the nodes, is plausible but requires an algebraization/normalization
and flatness argument that `fixed:L573-586` does not supply.

The load-bearing inference

```text
projective modules over C[x,y] are free  =>  the triple algebra is C[x,y][z]
```

is false. Quillen–Suslin only makes the rank-two trace-zero (Tschirnhausen)
module free. A general free triple algebra needs two generators and three
quadratic relations, equivalently a binary cubic with four coefficient
functions. For a basis and coefficients `a,b,c,d`, its branch discriminant is

```text
D=b^2c^2-3a^2d^2+4a^3c+4bd^3-6abcd.
```

A selected generator yields a depressed cubic only over the fraction field
unless the coefficient needed to eliminate the second generator is a unit.
Moreover, that selected cubic's polynomial discriminant is the true branch
discriminant times an index square (in Miranda's notation, `27 b^2 D`). Thus
one cannot infer `f=4a^3+27b^2` for two global polynomials.

Primary check: Rick Miranda, *Triple Covers in Algebraic Geometry*, **American
Journal of Mathematics** 107 (1985), Theorem 2.7, Remark 2.8.1, Lemma 4.5,
and the proof of Proposition 5.2,
`https://www.math.colostate.edu/~miranda/preprints/TripleCoversInAG.pdf`.
The PDF was streamed without saving; SHA-256
`0bfbaaf77c3c795189d5645466dd3d3ee32b872f5c962309751142d65535f875`.

Even under an extra global-monogenicity hypothesis, `deg a<=2` and `deg b<=3`
do not follow merely because their discriminant has degree six: cancellation of
higher homogeneous terms has not been excluded. Only the final conditional
step is sound: once an exact sextic discriminant and those bounds are separately
proved, the unique infinity point `[1:0:0]` forces its leading form to be
`c y^6`, yielding the displayed leading-form identity.

A successor must therefore rederive: (i) extension, normality and flatness of the
triple cover; (ii) its exact reduced branch/discriminant divisor; (iii) either a
binary-cubic elimination using the four-coefficient `D` above or a genuine
global-monogenicity theorem with no index square; and (iv) independent pole or
degree bounds. Until then `OPEN[PI1S4-(6,4)-TRIPLE-COVER]` is only a route, not a
reduction theorem.

## 10. Itemized verdicts and promotion recommendation

| charged item | verdict | promotion condition |
|---|---|---|
| 1. Cable/tubes/inner exponent | **CONFIRMED** | State the cable form up to braid conjugacy; retain only the invariant sum `sum k_i=10-beta_1`. |
| 2. Four checks of `e(rho_infty)=11` | **CONFIRMED-AS-QUALIFIED** | The number is exact conditional on `beta_1=15`; do not advertise all four routes as independent or assume five simple critical values without genericity. |
| 3. Outer `(3,2)` analysis | **CONFIRMED-AS-CORRECTED** | Use the direct periodicity proof, not full Theorem A on non-transposition tube products; use A′(1)–(4) exactly as scoped and delete A′(5). |
| 4. F1–F3, O4, 72, witness | **CONFIRMED-AS-REPAIRED** | The block conjugators, classification, three free orbits of 24, and every displayed witness relation check. No machine enumeration is needed. |
| 5. `3 | beta_1` iff criterion | **CONFIRMED-AS-REPAIRED** | Insert the uniform non-generation of O1–O3 for every `K`; then both directions and the 72-count for every admissible distribution follow. |
| 6. `(4,2)` comparison | **CONFIRMED-AS-QUALIFIED** | Say only that the A′(4) equal-product/cyclic collapse is structurally absent; other obstructions remain possible. |
| 7. Whole-row coverage | **CONFIRMED-AS-CORRECTED for `(6,4)`** | Use Hurwitz transport under braid conjugacy and the all-`k_i` solve; make the tubular conjugacy lemma explicit. The claimed fixed-braid transfer to `(8,4)` is **REFUTED/OPEN**. |
| 8. Fold and triple-cover successors | Fold: **CONFIRMED-AS-REWRITTEN**. Triple cover: **REFUTED beyond its group-theoretic opening**. | Promote the fold pullback lemma with the index-two diagram and line-meridian descent. Keep all global-cubic, exact-discriminant, and degree-bound claims OPEN. |

**Promotion recommendation: REJECT THE CHARGED REPORT AS A UNIT.** It contains a
theorem-scope violation, an unavailable A′(5) citation, an invalid `(8,4)`
fixed-braid transfer, and a false freeness-to-monogenicity implication. These are
not editorial defects in the successor-facing portions.

The following smaller package is safe to promote after the repairs stated above:

1. the `(6,4)` cable normal form and `e(iota)=10-beta_1`;
2. the corrected direct outer classification O1–O4;
3. F1–F3 and the all-`K` theorem
   `Fix_gen(rho_infty) != empty iff 3 | beta_1`, with exactly 72 tuples, all O4,
   in transported tube coordinates; and
4. the restriction-through-fold pullback-surjectivity lemma.

The specialization `beta_1=15` remains conditional on the provisionally routed
ROW-SWEEP input. Even after that specialization, the conclusion is only that the
infinity braid does **not** close the row: a fixed generating tuple is a necessary
state, not an `S_4` quotient. The simultaneous local braid-factorization problem
remains OPEN. The triple-cover route must be rederived from the general binary-cubic
algebra before any successor cites a discriminant identity or degree bound.

<!-- BODY-END -->
