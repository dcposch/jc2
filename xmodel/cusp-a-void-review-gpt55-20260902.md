# Hostile review: CUSP-A-VOID all-degree case-(A) gate

Lane: `CUSP-A-VOID-REVIEW-GPT55`. Date: 2026-09-02. Model: GPT-5.5.
Target: hostile line-by-line gate of `cusp-a-n8-gate-opus5-20260902.md`.

## 0. Custody

The four frozen inputs were hashed before mathematical reading. All match the
charge:

```text
2a1717aec9999608b13e3de9432d841d5746152e0b5590a87430d6a69215c459  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.p1akLB/inputs/cusp-a-n8-gate-opus5-20260902.md
6fa3447c0bdbc28347f287820bd95ea11c2fec37b3310d20adc8da3a75c87ea1  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.p1akLB/inputs/case-a-sweep-grok46-20260902.md
fa52e816869fc689db23d5dfb6354be0cf88cb361f365dd9ff16f51c01d97883  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.p1akLB/inputs/homcover-transfer-opus5-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.p1akLB/inputs/mprime-alln-h2-opus5-20260902.md
```

Aliases below: `CUSP` = the charged cusp report; `SW` = case-A sweep; `HT` =
homcover transfer; `MI` = mprime all-N H2. I also read the already banked local
review `xmodel/mprime-alln-review-gpt55-20260902.md`, cited as `MIR`, only to
check the typing of SMOOTH-KILL and MI Prop. 6.1. No `jc2-lean` content was
inspected. No canonical ledger was edited. No exit-price assertion is made, so
there is no `charge_basis` line.

Light replay only: `python3 box/cover_h1.py`; `python3
box/cuspa-n8-drivers-20260902/more.py`; `ctrl.py`; `fam.py`; `sweep8.py`;
`gd.py`. These are finite permutation/SNF checks; `ctrl.py` uses desk-scale
sympy for exact linear algebra. No Groebner/CAS decision procedure was used.

## 1. Executive verdict

```text
THEOREM NO-CUSP-PREIMAGE       CONFIRMED, with a basepoint/shrinking repair.
Case-(A) cone corollary        CONFIRMED; c is the cone vertex after LZ normalization.
THEOREM CUSP-A-VOID            CONFIRMED.  Chain I closes case (A), all N>=2.
(G-C) chi(E)=nu-Sigma*         CONFIRMED, with explicit RH puncture bookkeeping.
THEOREM PERIPHERAL-RANK        CONFIRMED as a geometric necessary condition.
Block-conjugacy lemma          CONFIRMED.
THEOREM MERIDIAN-SPAN          CONFIRMED.
THEOREM CUSP-A-VOID-II         CONFIRMED, under its H2/7.B/W>=2 typing.
COROLLARY CUSP-A-KAPPA         CONFIRMED, from PERIPHERAL-RANK plus CUSP-KILL.
COROLLARY kappa | a            CONFIRMED, same central-block scope.
MPRIME Prop. 6.1 cross-check   RESOLVED: it is about the affine cusp fibre,
                               not merely the dicritical map.  It conflicts
                               with NO-CUSP only under the now-empty antecedent.
SMOOTH-KILL composition        CONFIRMED at banked typing.
SUCC-1                         CONFIRMED only with transitive local monodromy;
                               B3 with a_p0=1 is consistent only if local
                               monodromy is not transitive.
```

Promotion recommendation: promote the case-(A) emptiness theorem. The cleanest
recording is:

```text
If F is Keller and c in A_F has transitive restricted local monodromy on the
N sheets of F over C^2 - A_F, then F^{-1}(c)=empty.  In MPRIME case (A), the
unique cusp has this property because the curve is Aut(C^2)-equivalent to the
weighted cone {x^p=y^q}.  Hence case (A) is empty for every N>=2.
```

Also record the independent direct contradiction with MI Prop. 6.1:
case (A) has one singular point and MI gives `a_p=1` there (`MI:442-450`,
`MI:483-486`; reviewed at `MIR:116-149`), while NO-CUSP gives `a_p=0`. This is
not a reason to reinterpret MI as dicritical-only; it is an additional kill of
the case-(A) antecedent.

Do not record any statement that B3 is killed, that B3 local monodromy is
transitive, or that the charged "MPRIME might be dicritical-only" flag is
resolved in that direction.

## 2. Theorem table, line by line

`CUSP:51-54` states NO-CUSP-PREIMAGE and smoothness of `E`. CONFIRMED. The
proof is the displayed theorem at `CUSP:110-128`, plus the case-(A) cone
corollary at `CUSP:130-139`. Repairs: choose basepoints, shrink to a Milnor
ball inside one local inverse chart, and say explicitly that components of the
restricted covering are orbits of the restricted monodromy.

`CUSP:56-58` states CUSP-A-VOID by Euler plus no nonconstant `A^1 -> C^*`.
CONFIRMED. The detailed proof is `CUSP:158-189`. It is H2-free at the stated
geometric scope "A_F homeomorphic to C and singular".

`CUSP:60-62` and `CUSP:266-275` state PERIPHERAL-RANK (`t=c=j`, base orbifold
genus zero). CONFIRMED, provided the object is an actual case-(A) Keller
covering, so Lemma F1 meridian generation applies.

`CUSP:64-65`, `CUSP:285-306` state block conjugacy and MERIDIAN-SPAN
`kappa*j <= a`. CONFIRMED. The proof is a necessary-condition theorem for the
case-(A) monodromy with central `z`.

`CUSP:67-71`, `CUSP:317-327` state CUSP-A-VOID-II. CONFIRMED at the report's
own typing: it consumes H2 through `W=N-a>=2` from 7.B' and the case-(A) cage
(`CUSP:329-333`).

`CUSP:73-75`, `CUSP:342-350` state CUSP-A-KAPPA. CONFIRMED, but its proof is
only as strong as PERIPHERAL-RANK plus CUSP-KILL plus `W>=2`. It supersedes
SW's conjectural status at `SW:322-335`.

`CUSP:77`, `CUSP:285-296`, `CUSP:360-364` state `kappa | a` and the byproducts
`a <= kappa*j`, `#cycles(bar m)=j`. CONFIRMED at the same central-block scope.
Do not export it to unrelated profiles without a central/block-forming element.

`CUSP:191-202` states `(G-C) chi(E)=nu-Sigma*` and `chi(E)=1`. CONFIRMED, with
the Riemann-Hurwitz expansion in section 6 below. The displayed proof is too
compressed but the identity is correct.

`CUSP:145-150` and `CUSP:701-703` flag MPRIME Prop. 6.1 as possibly a
dicritical ledger rather than an `E`-fibre statement. REFUTED as a flag. MI
defines `a_p=#F^{-1}(p)` at `MI:26-31`, proves `a_p=1` for `s=1` at
`MI:442-445`, applies that to case (A) at `MI:483-486`, and the local review
confirms it at `MIR:116-149`. The repair is to record the contradiction, not
to defer the ledger.

`CUSP:223-227` states the composed consequence with SMOOTH-KILL only at
SMOOTH-KILL's own typing. CONFIRMED. SMOOTH-KILL is banked as confirmed at
`MIR:27-35` and detailed at `MIR:87-112`.

`CUSP:623-626` states SUCC-1 in local-surjection language. CONFIRMED after
sharpening: local transitivity of `rho(Loc_c)` is the real sufficient
condition. Surjectivity `Loc_c -> pi_1(C^2-A_F)` is one way to get it.

## 3. Properness and surjectivity over the complement

The charged proof starts with "F is proper over X := C^2 - A_F" (`CUSP:115`).
That is right, but the surjectivity onto `X` should be stated.

Jelonek's non-properness set is being used in the campaign notation as
`D:=A_F` (`MI:26-31`). By definition, outside `A_F` the map is proper at every
target point. Properness is local on the target, so

```text
F^{-1}(X) -> X,     X = C^2 - A_F,
```

is proper. A Keller map has nonzero constant Jacobian, hence is dominant and
etale, so its image is dense and open. If `y in X` were not in the image, choose
image points `y_n -> y`. Properness over a small neighborhood of `y` gives a
compactness subsequence for preimages `x_n`, and continuity gives `F(x)=y`,
contradiction. Thus `F^{-1}(X)->X` is also surjective.

Since `F` is etale, it is quasi-finite; proper plus quasi-finite gives a finite
etale map over `X`. Its degree is the geometric degree `N`. Analytically this is
an `N`-sheeted covering. The full restricted cover over a local punctured ball
is exactly

```text
Y_B = Y x_X (B - A_F) = F^{-1}(B - A_F),
Y = C^2 - F^{-1}(A_F).
```

This checks mandatory item (1).

## 4. NO-CUSP-PREIMAGE

The theorem is `CUSP:110-128`. The proof stands with the following precise
version.

Pick `b0 in B-A_F`, and label the fibre of the global covering
`p:Y->X`. Let `i:B-A_F -> X` be inclusion. The restricted covering
`Y_B -> B-A_F` is classified, up to simultaneous conjugacy from the basepoint
choice, by

```text
rho_B = rho o i_* : pi_1(B-A_F,b0) -> S_N.
```

The connected components of `Y_B` are the orbits of `im(rho_B)` on the fibre.
If `i_*` is onto and `rho` is transitive, then `rho_B` is transitive, hence
`Y_B` is connected of degree `N`.

Now suppose `x in F^{-1}(c)`. Etaleness gives a local biholomorphism
`F|_U:U->V` at `x`. Shrink the chosen Milnor ball, if necessary, so
`B subset V` and the local fundamental group is unchanged. Then
`U'=(F|_U)^{-1}(B)` gives a section

```text
s:B-A_F -> Y_B,     s(y)=(F|_U)^{-1}(y).
```

For a covering over a connected base, the image of a section is open and closed
in the total space: locally it is one sheet of an evenly covered neighborhood.
Thus a section of a connected `N`-sheeted cover forces that cover to have
degree one. This contradicts `N>=2`. The "one B serves all of it" parenthetical
at `CUSP:120-121` is unnecessary; one preimage point already yields the
contradiction. If desired, finiteness of `F^{-1}(c)` follows from etale
quasi-finiteness and finite type.

This also gives the SUCC-1 strengthening: the theorem does not need
`i_*` surjective. It only needs the restricted local monodromy `rho_B` to be
transitive.

## 5. The cone local-to-global map

The corollary is `CUSP:130-139`. It is correct, with one coordinate
normalization caveat.

In case (A), MI Prop. 7.1 gives an automorphism taking `A_F` to
`{x^p=y^q}` with `gcd(p,q)=1`, and SMOOTH-KILL makes `p,q>=2`
(`MI:483-486`). The singular point `c` is therefore the preimage, under that
target automorphism, of the cone vertex `(0,0)`. The weighted action

```text
lambda . (x,y) = (lambda^q x, lambda^p y)
```

scales `x^p-y^q` by `lambda^(pq)`. With weighted radius, for instance
`R(x,y)= (|x|^(2p)+|y|^(2q))^(1/(2pq))`, every positive real weighted ray in
`C^2 - {x^p=y^q}` meets each weighted sphere exactly once. Therefore

```text
C^2 - {x^p=y^q}  ~=  (S_w - T(p,q)) x (0,infty),
B_e - {x^p=y^q}  ~=  (S_w - T(p,q)) x (0,e)
```

up to the usual Milnor-ball replacement of an ordinary small ball by an
equivalent conical neighborhood. The inclusion of the local complement into
the global complement is a homotopy equivalence, hence the local-to-global
map on pi_1 is an isomorphism. This proves the transitivity hypothesis used
in section 4. Mandatory item (3) passes.

The downstream smoothness statement also passes. If `F^{-1}(c)=empty`, then
`E=F^{-1}(A_F)` lies over the smooth curve `A_F-{c}`. Pullback of a smooth
divisor by an etale morphism is smooth, so `E` is a smooth affine curve; its
irreducible components are disjoint. The restriction to `A_F-{c} ~= C^*` is
etale on each component.

## 6. Euler and `(G-C)`

The Euler part of CUSP-A-VOID is `CUSP:165-170`. It is correct. Since
`A_F` is homeomorphic to `C`, `chi_c(A_F)=1`; also `chi_c(C^2)=1`. Additivity
for the closed-open decomposition `A_F subset C^2` gives `chi_c(X)=0`. The
finite `N`-fold covering `Y->X` gives `chi_c(Y)=N chi_c(X)=0`. Additivity for
`E subset C^2` gives

```text
chi_c(E) = chi_c(C^2) - chi_c(Y) = 1.
```

This checks mandatory item (4).

The displayed `(G-C)` identity is `CUSP:191-202`. The right derivation is as
follows. For an irreducible component `E_i`, let
`f_i:bar E_i -> P^1` be the map induced after normalizing `E_i` and `A_F`.
Let its degree be `d_i`. Split the punctures `S_i=bar E_i-E_i` into:

```text
S_i^0       punctures mapping to the cusp value 0,
S_i^*       punctures mapping to C^* = A_F - {c},
S_i^infty   punctures mapping to the point at infinity of the normalized A_F.
```

At affine points of `E_i`, including affine preimages of the cusp, the map is
unramified on normalizations because ambient `F` is a local biholomorphism.
Riemann-Hurwitz therefore has ramification only at punctures:

```text
2 - 2g_i = 2d_i - sum_{P in S_i}(e_P-1).
```

Now

```text
chi(E_i) = 2 - 2g_i - |S_i|
         = 2d_i - sum_{P in S_i} e_P.
```

The fibre over infinity has total multiplicity `d_i`, so
`sum_{S_i^infty} e_P=d_i`. If `nu_i` is the number of affine points of `E_i`
over the cusp, then the fibre over the cusp gives
`nu_i + sum_{S_i^0} e_P=d_i`. Hence

```text
chi(E_i) = nu_i - sum_{P in S_i^*} e_P.
```

Summing over components gives

```text
chi(E) = nu - Sigma*,     Sigma* = sum_i sum_{P in S_i^*} e_P.
```

This is the charged formula. The repair is that punctures over the cusp and
over infinity must be named; their multiplicities cancel. Without that split,
`CUSP:195-198` is too compressed to audit. With the split, mandatory item (6)
passes.

## 7. The `A^1 -> C^*` contradiction

The component argument is `CUSP:171-189`. It is correct.

Each smooth irreducible affine curve has
`chi=2-2g-theta <= 1`, equality exactly for `g=0`, `theta=1`, i.e. `A^1`
(`CUSP:171-179`). Since the integer component Euler characteristics sum to
`1`, at least one component is `A^1` (`CUSP:180-181`).

No component is contracted. If an irreducible curve component were mapped to a
point, then at a smooth point of that component the tangent line would lie in
the kernel of `dF`, contradicting the invertible Jacobian. Thus
`F|_{E_i}` is nonconstant (`CUSP:183-185`).

Finally, a morphism `A^1 -> C^*` corresponds to a unit in `C[t]`, and the only
units of `C[t]` are nonzero constants. This proves there is no nonconstant
morphism `A^1 -> C^*` (`CUSP:186-189`). Mandatory item (5) passes.

Together with section 4, this confirms THEOREM CUSP-A-VOID. It is actually
overdetermined: Chain I already contradicts `nu=0`, while MI Prop. 6.1 gives
the opposite necessary value `nu=a_p=1`.

## 8. MPRIME Prop. 6.1 cross-check

The cross-check is mandatory item (7). The ledger is not dicritical-only.

MI's standing setup defines `a_p=#F^{-1}(p)` and `a=a_p` on the smooth stratum
(`MI:26-31`). The pointwise fibre law is explicitly about target fibres:
`N-a_p=r_p W + K_p` (`MI:222-246`), and the derived form is
`a-a_p=(r_p-1)W+K_p` (`MI:248-256`). Prop. 6.1 then says that if `s=1`, the
single singular point is unibranch and `a_p=1` (`MI:442-450`). MI Prop. 7.1
applies this to case (A): `s=1`, `a_p=1`, `nu=0`, `K_p=a-1` (`MI:483-486`).
The local hostile review confirms Prop. 6.1 (`MIR:116-149`) and recommends
promotion (`MIR:387-399`).

Therefore `a_p=1` is a statement about the affine fibre `F^{-1}(p)`, hence
about `E=F^{-1}(A_F)`, while `K_p` is the dicritical excess term tied to that
same fibre by `(L)`. It is not merely a ledger of the dicritical map to
`A_F`.

Resolution: Prop. 6.1 and NO-CUSP-PREIMAGE cannot both be properties of an
existing case-(A) Keller map. Since both are confirmed conditional theorems,
the correct conclusion is that the antecedent is empty. The charged report's
"MPRIME not charged here; NOT claimed" flag (`CUSP:145-150`, `CUSP:701-703`)
should be replaced by:

```text
MI Prop. 6.1 gives a_p=1 at the unique case-(A) cusp.  NO-CUSP-PREIMAGE gives
a_p=0 because the local cusp complement maps onto the global complement.
Thus case (A) is empty.
```

This is compatible with FALLACY-v2: we are not identifying a flag, a place, and
a cover series. We are comparing two necessary statements about the same
target point after the Lin-Zaidenberg normalization.

## 9. Chain II

Chain II begins with the setup `CUSP:236-262`. The HT substrate supplies
`G=G_{p,q}`, central `z=alpha^p`, `H=rho^{-1}(Stab_1)`, `H_1(Y)=Z^j`, and
`N=M kappa` (`HT:358-365`). HT also supplies ORBIFOLD-CAGE and the formula
`2g+c=j` through `HT:419-430`. The charged report then proves two new
conditions.

PERIPHERAL-RANK (`CUSP:266-275`) is sound. A meridian of an affine component of
`E` is represented by a lift of the peripheral meridian `m` at a fixed sheet,
so it lies in the boundary of the compact torus-knot-cover core. Lemma F1 says
these component meridians generate `H_1(Y)=Z^j` (`HT:97-107`; consumed at
`CUSP:236-239`). Therefore `H_1(partial Sigma_H;Q)->H_1(Sigma_H;Q)` is onto.
For a compact orientable 3-manifold with `t` torus boundary components,
half-lives-half-dies gives image rank `t`. The image is all of `H_1`, so
`j=t`. Since `t=c`, `2g+c=j` gives `g=0`.

MERIDIAN-SPAN (`CUSP:285-306`) is also sound. Since `rho(z)` is central and
semiregular, its orbits are blocks of size `kappa`. On a block, any permutation
commuting with the simply transitive cyclic action is a power of `rho(z)`.
Thus if `rho(m)` fixes one point in the block, it is the identity on the whole
block. This proves `Fix(rho(m))` is a union of `a/kappa` whole blocks and
`kappa | a` (`CUSP:290-294`). The conjugacy statement for meridian lifts follows
by changing the sheet representative by a central power of `z` (`CUSP:295-296`).
The `j` geometric component meridians are distinct basis elements in
`H_1(C^2-E)` by Lemma F1, but block conjugacy gives at most `a/kappa` distinct
classes. Hence `j <= a/kappa`.

CUSP-A-VOID-II (`CUSP:317-327`) is valid. PERIPHERAL-RANK gives
`#cyc(bar m)=j`; the fixed identity blocks give `#Fix(bar m)>=a/kappa`, hence
`a <= kappa*j`. MERIDIAN-SPAN gives the opposite inequality. Equality forces
every cycle of `bar m` to be fixed, then every `z`-block to have
`rho(m)|_B=id`, hence `rho(m)=id` and `a=N`. Under the consumed H2/7.B typing,
`W=N-a=sum s_l mu_l>=2`, contradiction (`CUSP:326-333`).

The measured tables agree. The charged table has N=8 records with
`t=c=j`, `ndist=a/kappa<j`, and MERIDIAN-SPAN failing in all four cells
(`CUSP:396-410`), plus the N=9 spot with `t=c=2=j` and `ndist=1<j=2`
(`CUSP:418-421`). My local replay reproduced:

```text
cover_h1.py: four built-in controls pass, including Z (+) Z/3 and convention refusal.
more.py: N=1 positive control passes; N=8 ndist=a/kappa has 0 mismatches on 32 records;
         N=9 spot has 6 survivors, j=2, a=3, kappa=3, ndist=1, MERIDIAN-SPAN false.
ctrl.py: psi(meridian classes)={1} on checked cells; MERIDIAN-BASIS passes 0 at N=2,3,4.
fam.py: D=1,5,7,11,13 each has 6 family survivors with PERIPHERAL true and MSP false.
sweep8.py: 32 N=8 candidates; PERIPHERAL-RANK pass 32; MERIDIAN-SPAN pass 0.
gd.py: trefoil image order 24, centre order 2, c=2 and genus 0; family c=3.
```

Thus mandatory item (8) passes. The representation-level gate is not merely a
measurement: the measurement verifies that the charged survivors violate the
proved necessary inequality.

## 10. SMOOTH-KILL composition

The charged report phrases the composed consequence carefully at `CUSP:223-227`.
That composition is legitimate.

SMOOTH-KILL is confirmed in the local MPRIME review (`MIR:27-35`, `MIR:87-112`):
for a noninvertible Keller map with irreducible `A_F`, the curve `A_F` is
singular. If a noninvertible Keller map had `A_F` homeomorphic to `C`, then
`A_F` is irreducible and SMOOTH-KILL makes it singular. CUSP-A-VOID then
excludes it. If `A_F` were empty, the map would be proper etale of degree `N`
over simply connected affine space and hence an automorphism; so the
noninvertible case indeed has a nonempty nonproperness set. Therefore the safe
banked consequence is:

```text
For a noninvertible plane Keller map, A_F is not homeomorphic to C.
```

This is not a statement about arbitrary singular-branch profiles, and it does
not touch B3.

## 11. SUCC-1 and B3

The mechanism extends beyond cones in exactly this form:

```text
If the restricted local monodromy rho(pi_1(B_c-A_F)) is transitive on the N
sheets of F over C^2-A_F, then F^{-1}(c)=empty.
```

Surjectivity of `pi_1(B_c-A_F)->pi_1(C^2-A_F)` is sufficient, but not
necessary. This is the same section-of-a-connected-cover argument as section
4, with no weighted cone assumption.

The B3 cusp is the test that prevents overpromotion. MI's N4-PIN says the
rank-four B3 residual has exactly one cusp point `p_0`, with
`a_{p_0}=1` and `K_{p_0}=1` (`MI:580-593`, proof at `MI:595-605`). If the B3
local monodromy at that cusp were transitive on all `N` sheets, the generalized
NO-CUSP theorem would force `a_{p_0}=0`, contradicting N4-PIN. Hence the B3
record is consistent only if the local cusp monodromy is not transitive; it
must have at least the fixed sheet coming from the actual affine preimage.

So SUCC-1 is safe as a conditional theorem. It is not a license to delete B3
unless a separate local-monodromy transitivity theorem is proved for that
specific singular point. This answers mandatory item (10).

## 12. FALLACY-v2 audit

Flag/place/series: passed. The actual cone argument identifies the local cusp
complement and global complement only after Lin-Zaidenberg puts the unique
case-(A) cusp at the weighted cone vertex. B3 is explicitly excluded from that
identification.

Carrier/attainment and floor/attainment: passed. The N=8 survivors remain
representative monodromy data. The review uses them only as necessary-condition
inputs; no geometric realization is asserted.

Per-ray/exit-set charge: no exit price is asserted; no `charge_basis` line is
present.

Variable/ring map: passed. `a` is kept as the generic fibre count
`#Fix(rho(m))`; `a_p` is the affine fibre over a singular target point. The
charged report's useful correction "a is generic, not cusp-fibre" is retained,
but MI's `a_p=1` is not reinterpreted away.

No gap by cap or analogy: passed. The only extension beyond case (A), SUCC-1,
is typed by local monodromy transitivity. B3 is not killed by analogy.

## 13. Typed verdict block

```text
LANE              CUSP-A-VOID-REVIEW-GPT55
CHARGE            Hostile gate on CUSP-A-N8-GATE, every displayed theorem.

HASHES            4/4 frozen inputs match before reading.

NO-CUSP-PREIMAGE  CONFIRMED.  Properness over C^2-A_F is by Jelonek's
                  nonproperness-set definition; surjectivity onto the
                  complement follows from dominance plus local properness.
                  The restricted-cover proof is valid after making basepoints,
                  orbit/component classification, and ball-shrinking explicit.

CONE COROLLARY    CONFIRMED.  In LZ coordinates c is the origin/vertex of
                  {x^p=y^q}.  Weighted positive-real scaling gives
                  (S_w-T(p,q)) x (0,infty) globally and x (0,e) locally, so
                  local-to-global pi_1 is an isomorphism.

CUSP-A-VOID       CONFIRMED.  chi_c(E)=1; a smooth affine component has chi<=1;
                  one A^1 component is forced; etaleness prevents contraction;
                  no nonconstant morphism A^1 -> C^* exists.

(G-C)             CONFIRMED WITH BOOKKEEPING REPAIR.  Riemann-Hurwitz must
                  split punctures over cusp / C^* / infinity.  The cusp and
                  infinity terms cancel, leaving chi(E)=nu-Sigma*.

MPRIME PROP 6.1   CONFIRMED as an affine fibre statement, not dicritical-only.
                  It gives a_p=1 in case (A); NO-CUSP gives a_p=0.  The
                  contradiction is a direct case-(A) kill.

PERIPHERAL-RANK   CONFIRMED.  Boundary homology is onto because component
                  meridians generate H_1(Y); half-lives-half-dies gives t=j.

MERIDIAN-SPAN     CONFIRMED.  Central z-blocks collapse meridian classes, so
                  j<=a/kappa.  Hence kappa|a is confirmed.

CUSP-A-VOID-II    CONFIRMED under H2/7.B/W>=2 typing.  PERIPHERAL-RANK and
                  MERIDIAN-SPAN force rho(m)=1 and a=N, contradicting W>=2.

CUSP-A-KAPPA      CONFIRMED at the same typing; SW's conjecture is upgraded to
                  a theorem.

MEASURED REPLAY   CONFIRMED.  cover_h1 controls pass.  N=8: 32 candidates,
                  32 pass PERIPHERAL-RANK, 0 pass MERIDIAN-SPAN.  N=9 F9.1:
                  6 survivors, t=j, ndist=1<j=2.

SMOOTH-KILL COMP  CONFIRMED at banked typings.  Noninvertible Keller maps have
                  A_F not homeomorphic to C.

SUCC-1            CONFIRMED only as: transitive local monodromy implies
                  F^{-1}(c)=empty.  B3 with a_p0=1 is consistent only when the
                  cusp local monodromy is not transitive.

PROMOTE           Case (A) empty for every N>=2; NO-CUSP local-transitivity
                  lemma; Chain II PERIPHERAL-RANK and MERIDIAN-SPAN gates;
                  kappa|a; chi(E)=nu-Sigma* with the puncture split.

DO NOT PROMOTE    Any B3 deletion; any statement that MI Prop. 6.1 is
                  dicritical-only; any geometric realization of representative
                  covers; any new exit price.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `24245`.
- Body SHA-256:
  `9462f3006379e42b6a9b9b0c83bf4c9275c53ecd13dfd6fcffc92610b6ce5426`.
- Frozen basis: `695820fea6420a441602de761b87ca0ba63aba8b`.
