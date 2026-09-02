# CUSP-A-VOID-COUNTERMODEL — hidden-assumption audit and representation hunt

Lane: `CUSP-A-VOID-COUNTERMODEL`. Date: 2026-09-02. Agent: Grok 4.6.
Adversarial review of charged producer `CUSP-A-N8-GATE` (Opus 5).
Desk topology plus exact integer permutation/homology. No Groebner, no
CAS, no AWS, no ledger edit, no `jc2-lean`. Instrument `box/cover_h1.py`
consumed unmodified. No `charge_basis`: no new exit price.

## 0. Custody

Frozen copies hashed with `shasum -a 256` **before any was read**; 4/4 match:

```text
2a1717aec9999608b13e3de9432d841d5746152e0b5590a87430d6a69215c459  cusp-a-n8-gate-opus5-20260902.md
6fa3447c0bdbc28347f287820bd95ea11c2fec37b3310d20adc8da3a75c87ea1  case-a-sweep-grok46-20260902.md
fa52e816869fc689db23d5dfb6354be0cf88cb361f365dd9ff16f51c01d97883  homcover-transfer-opus5-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  mprime-alln-h2-opus5-20260902.md
```

**GATE** = n8-gate, **SW** = case-A sweep, **HT** = transfer, **MI** =
MPRIME-ALLN-H2; line numbers are these frozen copies.

```text
dfb90ce32f589aae00ce7f2d3188114bbf27396120a8da3d8e67c0145b5177b2  box/cover_h1.py
```

`python3 box/cover_h1.py` — 4/4 controls PASS. Homology via
`to_transport_convention`. Drivers in `/tmp`; not in `box/`.

## 1. Verdict

```text
NO-CUSP-PREIMAGE    SURVIVES.  No countermodel on a Keller self-map of C^2
                    nor on any open of C^2.  The N-fold cover of C^2 minus
                    a cone curve is refused at chi, at pi_1, and at A^1->C^*.

CUSP-A-VOID         SURVIVES, H2-free, every N>=2.  Carried by §2.  An A^1
                    component cannot miss the cusp and cannot hit it.

PERIPHERAL-RANK     SURVIVES at the stated typing (Lemma F1: Y is a
                    plane-curve complement).  REFUTED as a group-theoretic
                    claim about all transitive torsion-free G_{p,q}->S_N:
                    explicit genus-1 covers exist, all outside 2<=j<=a<=N-2.

MERIDIAN-SPAN       SURVIVES at the stated typing (F1).  Empirically NEVER
                    holds for a transitive torsion-free G_{p,q}->S_N at
                    2<=N<=9 in the scan — including the 26 cage survivors,
                    which violate kappa*j<=a, as GATE claims.  Equality is
                    the trivial representation.

CUSP-A-VOID-II      SURVIVES.  0 reps pass both gates.  Terminal rho(m)=1
                    is the trivial representation (a meridian normally
                    generates a knot group); transitivity at N>=2 kills
                    the equality case; W>=2 from 7.B' is optional.

PROP 6.1 CONFLICT   Charged MPRIME text supports Reading A (a_p = affine
                    fibre of the cusp = 1, a point of E over c).  That
                    reading is incompatible with NO-CUSP-PREIMAGE and with
                    (M') at a_p=0.  The clash is an emptiness proof, not a
                    rescue of case (A).  CUSP-KILL's y_0 construction is
                    not an independent geometric step.
```

Chain I is not refuted. Chain II's genus-0 claim does not survive as a
statement about abstract torus-knot covers; it does survive for
plane-curve complements, and no violator was found in the Keller window.

## 2. Hidden assumptions, and models that fail them

### 2.1 Facts consumed

**NO-CUSP-PREIMAGE** (GATE:110–128):

* P1. `F` proper over `X := C^2 \ A_F` (Jelonek's `A_F`).
* P2. `F` étale on `C^2`, hence a local biholomorphism (Keller).
* P3. `Y := C^2 \ E` connected (curve complement in `C^2`).
* P4. classifying `rho : pi_1(X) -> S_N` transitive (from P3).
* P5. `F^{-1}(c)` finite (étale ⇒ quasi-finite).
* P6. a local biholomorphism at `x |-> c` supplies a section of `Y -> X`
  over a small `B \ A_F` (shrink `B` into `F(U)`).
* P7. `B \ A_F` path-connected and locally path-connected (unibranch
  link is a knot).
* P8. restricted covering over `B \ A_F` classified by
  `rho ∘ inclusion_*`.
* P9. `pi_1(B \ A_F) -> pi_1(X)` **surjective** (cone, §3).
* P10. a section of a connected `N`-sheeted covering forces `N = 1`
  (irregular covers allowed).
* P11. `N >= 2`.

In case (A), P9 is an isomorphism, from Lin–Zaidenberg plus the weighted
`C^*`-action (§3), not an extra geometric hypothesis.

**CUSP-A-VOID** (GATE:157–189) consumes P1–P11 and:

* E1. `chi_c` additive on a closed-open decomposition of a triangulable
  pair (ordinary `chi` agrees here).
* E2. `chi_c(C^2) = 1`.
* E3. a finite covering multiplies `chi` (affine varieties have finite
  CW type, Hamm; a covering lifts cells).
* E4. `chi(X) = 0` (`A_F ≃ C`, or `X ≃ S^3 \ T(p,q)`).
* E5. `E = F^{-1}(A_F)` a closed algebraic curve.
* E6. `E` smooth (NO-CUSP-PREIMAGE: the only candidate singularities
  were analytic cusps over `c`).
* E7. irreducible components of a smooth curve in `C^2` are pairwise
  disjoint (they meet only at singular points of `E`).
* E8. a smooth irreducible affine curve has `chi = 2-2g-theta <= 1`,
  equality iff `A^1` (`theta >= 1`: a complete curve is not affine).
* E9. integers `<= 1` summing to `1` force some equal to `1`.
* E10. `F|_{E_i}` non-constant (`dF` invertible; no positive-dimensional
  fibre).
* E11. image of `E_i` avoids `c` (NO-CUSP-PREIMAGE).
* E12. `A_F \ {c} ≅ C^*` (normalisation `t |-> (t^q, t^p)` iso off 0).
* E13. no non-constant morphism `A^1 -> C^*` (`C[t]^* = C^*`).
* E14. morphisms of varieties are algebraic (`exp` is not a competitor).
* E15. base field `C` (LZ, analytic topology, units).

**PERIPHERAL-RANK** (GATE:264–275) consumes Lemma F1 (HT:97–107:
meridians of a plane-curve complement are a basis of `H_1`), the cone
retraction of `X` onto `M_0 = S^3 \ int nu(T(p,q))` lifting to
`Y ≃ Sigma_H`, meridians of `E` freely homotopic into `∂ Sigma_H`, and
half-lives-half-dies (image of `H_1(∂; Q) -> H_1(M; Q)` has rank `t`
when `∂M` is `t` tori).

**MERIDIAN-SPAN** (GATE:298–306) consumes F1, that the meridians of the
`j` components are the classes `[h_i]` for `i in Fix(rho(m))`, that
meridians of one irreducible component are conjugate, and
block-conjugacy (`rho(z)` central in a transitive subgroup of `S_N` is
semiregular; `Fix(rho(m))` is a union of blocks; `kappa | a`).

### 2.2 Models that break one fact while keeping the stated hypotheses

**Abstract `N`-fold cover of `X = C^2 \ {x^p=y^q}`.** Exists,
classified by any transitive `rho: G_{p,q}->S_N`. The 26 cage
survivors are such covers (§6). Here `chi(Y)=0`. This is the model
the charge names.

The argument refuses to let this `Y` be an open of `C^2` with curve
complement, at three independent places, all of which fire:

1. *Empty complement.* `Y = C^2` would require `chi(Y) = 1`, against
   `chi(Y) = 0` (E2–E4). GATE C8 is this bookkeeping with the source
   replaced by a surface of `chi <= 0`.
2. *Zero-dimensional complement.* `C^2` minus a finite set is simply
   connected (real codimension 4). A finite cover of `X` has `pi_1` a
   finite-index subgroup of infinite `G_{p,q}`, hence is never simply
   connected.
3. *Curve complement.* Then `chi(E) = 1` (E1–E5), `E` smooth (E6), some
   component is `A^1` (E7–E9), and that component maps non-constantly
   into `C^*` (E10–E12), impossible (E13). Independently F1 fails on
   the 26: GATE C4 measures `#` distinct meridian classes
   `= a/kappa < j = rank H^{ab}`.

The abstract cover is a Stein surface of Euler characteristic 0; it
is not an open of `C^2`. The refusal is not a missing case.

**Other models, in brief.** GATE C8 (`V=C^*×C`, `F=(u^2,v)`): étale of
degree 2, `E` empty, `0=0`; replacing `V` by `C^2` restores `chi(E)=1`.
E2 is load-bearing. GATE C9 (`F=(u^2,v):C^2->C^2`): not étale, fibre
over the origin nonempty; P2 fails. `z |-> e^z` is not a morphism of
affine varieties (E14). Two copies of `C^*` meeting at a point have
`chi=1` with no `A^1`, but they can meet only over `c`; smoothness
removes the meeting point. `chi` multiplicativity for the finite cover
`Y->X` is licensed by Hamm finite CW type, or independently by
`X ≃ S^3 \ T(p,q)` having `chi=0`. Any étale polynomial self-map of
`C^2` is Keller (`C[x,y]^*=C^*`), so a countermodel cannot live on
`C^2`. No model was found in which the *stated* hypotheses hold and
the conclusion fails.

Replacing (iv) by "`E->C^*` is an `a`-sheeted covering, so `chi(E)=0`"
is **not safe**: `C^* ⊂ A_F` and `F` is not proper over `A_F`. GATE
does not use this. The `A^1->C^*` step uses only `C[t]^*=C^*`.

## 3. The `C^*`-retraction, and Lin–Zaidenberg

GATE:132–139 identifies `pi_1(B_c \ A_F) -> pi_1(C^2 \ A_F)` with an
isomorphism because `{x^p = y^q}` is a weighted cone: both the global
complement and a small ball minus the curve deformation-retract onto
`S^3 \ T(p,q)` via `lambda · (x,y) = (lambda^q x, lambda^p y)`.

**Exact statement, over `C`.** An irreducible simply connected algebraic
curve in `C^2` is `Aut(C^2)`-equivalent to a quasihomogeneous curve
`{x^k=y^l}` (Lin–Zaidenberg, Soviet Math. Dokl. 28 (1983) 200–204 =
Dokl. Akad. Nauk SSSR 271 (1983) 1048–1052). Palka, arXiv:1405.5391:
every topologically contractible algebraic curve in `C^2` has equation
`x^n=y^m` in some algebraic coordinates, `gcd(n,m)=1`; LZ is the
singular half (`m>=2`). Arzhantsev–Zaidenberg, arXiv:1110.3028,
Theorem 1.3(a): reduced irreducible singular *acyclic* (`pi_0=pi_1=1`)
plane curve equivalent to a unique `{y^a=x^b}` with `1<a<b`, `gcd=1`.
For a complex affine algebraic curve these coincide (normalisation
`A^1`, bijective). GATE's citation "Invent. Math. 68 (1982) 1–17"
(GATE:492, via MI:491–492) is the wrong paper; the theorem quoted is
the 1983 Doklady note. The content GATE uses is the standard theorem.

**There are no non-quasihomogeneous unicuspidal curves homeomorphic to
`C` in `C^2`, over `C`.** That is the theorem. The `C^*`-retraction is
not an extra assumption on case (A): LZ supplies the quasihomogeneous
normal form, and the weighted action exists on that form. Euclidean
balls about the origin are invariant under the inward action
(`|lambda^q x|^2+|lambda^p y|^2 <= |x|^2+|y|^2` for `|lambda|<1`,
`p,q>=1`), so the retraction of `C^2 \ A_F` onto a weighted sphere
complement restricts to a small Euclidean ball. P9 is an isomorphism.

**Scope.** Over `C`, algebraic curves in the affine plane. Not in
positive characteristic. Not unicuspidal curves that fail to be
homeomorphic to `C` (annuli with two places at infinity, `b_1=1`;
positive genus); not reducible simply connected curves (case (B)); not
wild topological embeddings. Off the LZ substrate, local `pi_1` at a
cusp need not surject, and `A_F \ {c}` need not be `C^*`. Chain I's
three uses of "homeomorphic to `C`" (GATE:611–613: `chi(A_F)=1`; the
cone giving P9; `A_F \ {c} ≅ C^*`) fail together there. That is scope,
not a countermodel inside case (A). MPRIME case (A) *is* this
substrate: H2, every singular point unibranch, Lemma A (`D~ ≅ A^1`)
making the normalisation bijective (MI:483–494).

## 4. Fibre over `c`: can an `A^1` pass over the cusp?

Charge (3) asks to defeat "`A^1 -> C^*` is constant" by an `A^1`
component whose image is *not* in `C^*`.

**Local iso of surfaces.** If `x in F^{-1}(c)` and P2 holds, `F` carries
the germ `(E,x)` isomorphically onto `(A_F,c)`, a `(p,q)`-cusp. Hence
`E` is singular at `x`. A smooth `A^1` cannot contain `x`. Equivalently:
a non-constant morphism `A^1 -> {x^p=y^q}` factors through the
normalisation `n: A^1 -> A_F`, `n(t)=(t^q,t^p)`; a non-constant
polynomial `C->C` is surjective, so the image hits `c`.

**Covering-space form (emptiness).** Suppose `x in F^{-1}(c)`
nonetheless. P6 gives a section of `F^{-1}(B \ A_F) -> B \ A_F`. The
restricted covering has degree `N` (`B \ A_F ⊂ X` and `F: Y -> X` is
an `N`-sheeted covering: P1, every point of the punctured ball has
exactly `N` affine preimages; non-properness at `c` contributes
escaping sequences as one *approaches* `c`, not missing sheets over
`X`). P8–P9: `pi_1(B \ A_F)` acts through a surjection onto `pi_1(X)`,
hence transitively (P4). The restricted covering is connected of
degree `N`. A section forces `N=1` (P10). Contradiction.

The fibre over `c` is empty. Step (iv) is then forced: the `A^1` from
(iii) maps into `C^*` and is constant. A smooth `A^1` cannot hit `c`;
a singular component that hits `c` is forbidden by NO-CUSP-PREIMAGE.

## 5. MPRIME Prop. 6.1: two readings, one supported

SW:277–278 quotes MI Prop. 6.1 as "unique unibranch cusp, `K_p=a-1`,
`a_p=1`". GATE:145–151 flags a possible conflict with
NO-CUSP-PREIMAGE. The charged MPRIME text was read here.

**Standing definition** (MI:31): `a_p = #F^{-1}(p)`, and `a = a_p` for
`p in D_0`. Lemma 4.1 (MI:222–246) uses this as the count of affine
preimages that stay near `F^{-1}(p) ∩ A^2`; the remaining `N-a_p`
escape to the compactification.

**Prop. 6.1** (MI:441–450): if `s=1`, say `Sing D={p}`, then
`(M'-def)` gives `a_p = 1-(r_p-1)W`; `a_p>=0` and `W>=2` force
`r_p=1` and `a_p=1`.

**Prop. 7.1** (MI:483–494) specialises to case (A): `s=1`, `a_p=1`,
`nu=0`, `K_p=a-1`. Then MI:507–510: "`a_p=1` puts a single, unibranch
point of `E` over `p`". **CUSP-KILL** (MI:512–520) constructs
`E = E_0 ∪ {y_0}` with `(E,y_0) ≅ (D,p)` analytically.

**Reading A — about `E`.** `a_p` is the affine fibre of the unique
singular point of `A_F`. It equals 1. `E` is singular there, of the
same analytic type as the cusp of `A_F`. `K_p=a-1` is the Orevkov
excess at that cusp. This is what SW quotes.

**Reading B — about the dicritical / compactified finite map only.**
`a_p` counts points of `Y=Spec B` (MI:52–56) rather than of source
`A^2`, and no affine point of `E` need lie over `c`. This would
reconcile Prop. 6.1 with NO-CUSP-PREIMAGE.

**The charged MPRIME text supports Reading A**, and does not support
Reading B. The standing definition is `#F^{-1}(p)` on source `A^2`;
Prop. 7.1 and CUSP-KILL use it to put a point of `E` over `p`.

**The conflict is real as an instantiation, and empty as a rescue.**
If NO-CUSP-PREIMAGE holds then `a_c=0`. Plug `s=1`, `nu=0`, `a_p=0`
into `(M')` (MI:92–95): `a(nu+s-1)-sum a_p = 0 = N nu - 1 = -1`.
Into `(L)` and `(K)` (MI:251–256): `r_p=1` gives `K_p=a-a_p=a`, while
`(K)` gives `K_p=a-1`. Same `0=-1`. Theorem (E) (MI:96–98), which is
Chain I's Euler, still wants `chi(E)=1`; with `a_p=0` one cannot fill a
puncture of a cover of `C^*` to produce that `+1`. The identities and
the topology cannot be simultaneously instantiated. That is a third
emptiness proof for case (A) (MPRIME bookkeeping plus
NO-CUSP-PREIMAGE), not a countermodel.

CUSP-KILL's *written proof* constructs `y_0` from `a_p=1` and is
not a valid independent geometric step once NO-CUSP-PREIMAGE is
believed. Its *conclusion* `j>=2` is recovered without `y_0`:
`j=1` and `a_p=0` makes `E ≅ C^*` of Euler characteristic 0, against
`chi(E)=1`. Chain I does not consume CUSP-KILL. Chain II lists it for
the census window `2<=j<=a`; the all-degree emptiness proof of
CUSP-A-VOID-II does not need `y_0`. SW's `K_p=a-1` constraint is
inside an empty case and does not bear on (B3).

## 6. Chain II, by explicit representations

Left-action homs `G_{p,q}=<alpha,beta | alpha^p=beta^q> -> S_N`,
converted by `to_transport_convention` at the `cover_h1` call. Alpha
one class-rep per cycle type; beta runs over `S_N`. Relator
`alpha^p beta^{-q}`. Meridian `m=alpha^e beta^f` with `eq+fp=1`
(Bezout pairs differ by a central power, which cancels).
`kappa=ord rho(z)`; `a=#Fix(rho(m))`; `t=#` orbits of
`<rho(m),rho(z)>`; `j=` free rank of torsion-free `H^{ab}`. Scan: all
coprime `(p,q)<=7` at `N<=8`; at `N=9` selected pairs including
`(2,3),(3,4)` and swaps. `N=1` control: trivial `rho` has `H_1=Z^1`.

### 6.1 Census of torsion-free transitive covers

```text
N   rel    trans    tf      tors     PER pass/fail   MSP pass/fail  both
2      44     22       6      16          6 / 0            0 / 6      0
3      98     38      15      23         15 / 0            0 / 15     0
4     292     92      31      61         24 / 7            0 / 31     0
5    1280    600     149     451         58 / 91           0 / 149    0
6    7610   3464    1028    2436        300 / 728          0 / 1028   0
7   52086  29074    3661   25413        639 / 3022         0 / 3661   0
8  344085 151624   22135  129489       2276 / 19859        0 / 22135  0
9* 504745 118797   16343  102454       3963 / 12380        0 / 16343  0
```

`9*` = selected pairs. `kappa | a` failed in **0** records. MSP
(`kappa*j <= a`) passed in **0** torsion-free transitive records at
`N>=2`. Both gates passed in **0**.

Keller window `2<=j<=a<=N-2`, nonregular (`|rho(G)|>N`):

```text
N=8 cage, coprime (p,q)<=7, alpha class-reps:
  16 x (2,3) kappa=2 j=2 a=2 t=2 mer=(3,3,1,1) PER=pass MSP=fail
   6 x (3,2) kappa=2 j=2 a=2 t=2 mer=(3,3,1,1) PER=pass MSP=fail
   6 x (3,4) kappa=2 j=3 a=4 t=3 mer=(4,1^4)   PER=pass MSP=fail
   4 x (4,3) kappa=2 j=3 a=4 t=3 mer=(4,1^4)   PER=pass MSP=fail
  total 32, matching GATE / HT / SW.
N=9 selected:
   6 x (2,3) kappa=3 j=2 a=3 t=2 mer=(6,1^3)   PER=pass MSP=fail
   3 x (3,2) mirror, alpha-normalised
N<=7 cage window: 0, matching CUSP-A-EMPTY.
PER-FAIL inside 2<=j<=a<=N-2: 0, including regular covers.
```

GATE's 26 (32 with the `(3,2)` mirror) all violate `kappa*j<=a`, and
all pass `t=j`. Replayed.

### 6.2 Explicit MSP violators (the 26, sampled)

Left-action, 0-based. Relator `alpha^p=beta^q` holds; `cover_h1` after
`to_transport_convention`.

**Trefoil cell, N=8.** `p=2,q=3`, types `(4,4)/(6,2)`:

```text
A = (1, 2, 3, 0, 5, 6, 7, 4)
B = (1, 4, 3, 6, 2, 7, 0, 5)
z = A^2 = B^3 = (2, 3, 0, 1, 6, 7, 4, 5)     kappa = 2
m = A B^{-1} = (7, 1, 5, 3, 2, 4, 0, 6)      a = 2, mer=(3,3,1,1)
H_1 = Z^2                                     j = 2, t = 2
kappa*j = 4  >  a = 2                         MSP FAIL, PER PASS
```

Cell count 16 on this numerical type.

**Family cell, N=8.** `p=3,q=4`, types `(6,2)/(8)`, `kappa=2`, `j=3`,
`a=4`, `t=3`, `mer=(4)`, `kappa*j=6>4`. Count 6, and 4 on the swap.

**F9.1, N=9.** `p=2,q=3`, types `(6,3)/(9)`:

```text
A = (1, 2, 3, 4, 5, 0, 7, 8, 6)
B = (1, 6, 3, 8, 5, 7, 2, 0, 4)
kappa=3, j=2, a=3, t=2, mer=(6,1^3), H_1=Z^2
kappa*j = 6  >  a = 3                         MSP FAIL, PER PASS
```

Count 6, matching SW/GATE.

These are not countermodels to MERIDIAN-SPAN as a theorem about plane
complements: they are the representations the theorem kills. F1 says
`j` equals the number of distinct meridian classes, and block-conjugacy
bounds that number by `a/kappa`. The survivors have `j > a/kappa`.

Why MSP never holds at `N>=2`, even off the cage: CENTRAL-RANK plus the
orbifold picture give `j=2g+t` for torsion-free covers, and
`t >= #Fix(bar m) >= a/kappa`, so `j >= a/kappa` always, i.e.
`kappa*j >= a`. MSP is the opposite inequality. Equality throughout
forces `g=0`, `bar m=id`, `n_0=M`, hence `rho(m)=id` and `a=N`. A
meridian normally generates a knot group (Wirtinger: generators are
conjugate to `m`; equivalently, meridian Dehn filling is `S^3`). So
`rho(m)=1` implies `rho=1`, not transitive at `N>=2`. The equality case
is the trivial representation. That is why the MSP column is
identically 0 in §6.1.

### 6.3 Explicit genus-0 violators (PERIPHERAL-RANK off F1)

PERIPHERAL-RANK as "every torsion-free transitive `G_{p,q}->S_N` has
`t=j`" is **false**. Witnesses, all outside `2<=j<=a<=N-2`:

**Genus 1, `a=0`, N=4.** `p=3,q=4`, types `(3,1)/(4)`:

```text
A = (1, 2, 0, 3)          A^3 = id
B = (2, 0, 3, 1)          B^4 = id
m = A B^{-1} = (2, 3, 1, 0)     mer=(4), a=0, t=1
kappa=1, H_1=Z^3                j=3
2g+t=j  =>  g=1                 PER FAIL
```

Profile count 3 at `(3,4)` and 4 at the swap `(4,3)`.

**Genus 1, `a=1`, N=8.** `p=2,q=7`, types `(2^4)/(7,1)`:

```text
A = (1, 0, 3, 2, 5, 4, 7, 6)
B = (0, 2, 3, 4, 6, 1, 7, 5)
kappa=1, j=4, a=1, t=2, mer=(7,1), H_1=Z^4     g=1
```

Here `j>a`, so CUSP-KILL's `j<=a` already excludes it. SW's cheap-gate
emptying of `(2,7)` is the meridian/`a`-window, not PERIPHERAL-RANK.

**Genus 1, `a=2`, N=9.** `p=3,q=4`, types `(3^3)/(4,4,1)`:

```text
A = (1, 2, 0, 4, 5, 3, 7, 8, 6)
B = (0, 2, 3, 4, 1, 6, 8, 5, 7)
kappa=1, j=5, a=2, t=3, mer=(7,1,1), H_1=Z^5   g=1
```

Again `j>a`. Closest approach to the Keller window; still outside.
N=6 also has PER-FAIL with `j>a`. No PER-FAIL was found with
`2<=j<=a<=N-2`, regular or not, at `N<=9`. Inside GATE's window the
genus-0 gate holds in every measured record; outside it, genus 1 is
the phenomenon F1 forbids.

**Scope narrowing, mandatory.** PERIPHERAL-RANK may not be quoted as a
fact about torus-knot representation varieties. It is a theorem about
covers that are plane-curve complements (F1: meridians generate `H_1`,
hence `H_1(∂)->H_1(Sigma_H)` is onto, hence `b_1=t` by
half-lives-half-dies). Drop F1 and the claim is false, with the
witnesses above. GATE's proof *does* cite F1 (GATE:270–275). The 32/32
pass on the cage is consistent with that typing and is not independent
evidence that `g=0` is group-theoretic.

### 6.4 CUSP-A-VOID-II

The two inequalities `a <= kappa j` (PERIPHERAL-RANK plus `t>=n_0`)
and `a >= kappa j` (MERIDIAN-SPAN) force equality, hence `rho(m)=1`,
hence the trivial representation, against transitivity at `N>=2`. The
scan found 0 representations passing both gates, in or out of the
cage. No violator.

GATE consumes `W>=2` from 7.B' under H2 to contradict `a=N`. That step
is stronger than needed: `rho(m)=1` is already non-transitive. Chain
II's emptiness of case (A) at the representation level therefore does
not depend on H2, 7.B', or CUSP-KILL's `y_0`. It does depend on F1,
without which MERIDIAN-SPAN fails and the 26 (and many more) survive
as abstract covers. That is the intended kill, and it stands.

## 7. FALLACY-v2

* **Flag/place/series.** Germ, global `G_{p,q}`, and the link at
  infinity are kept distinct. They coincide in case (A) by LZ plus the
  cone (§3). `A_F \ {c}` is never identified with `A_F`. (B3) is not
  touched.
* **Carrier/attainment.** The 26 are `REPRESENTATIVE`. Refuting them as
  plane-curve complements is not `FULL_ACTUAL_EXIT`. No realisation.
* **Floor/attainment.** `chi(E_i)<=1` is a bound; the kill uses `=1`,
  forced by an integer sum. Equality in MERIDIAN-SPAN is the trivial
  representation, not an attainment on a nonempty set.
* **Per-ray / exit-set.** No exit price; no `charge_basis`.
* **Variable/ring map.** Transport convention declared; left-action
  homs inverted at the call. Relator `alpha^p beta^{-q}` as in HT/SW/GATE.
* **No gap filled by cap or analogy.** (G-A) without `Delta_infty` left
  undecided. Genus-0 off the Keller window is reported, not repaired by
  restricting the scan. Prop. 6.1 is not rewritten as Reading B. (B3)
  is OPEN relative to this lane.

## 8. Typed verdict block

```text
LANE              CUSP-A-VOID-COUNTERMODEL

NO-CUSP-PREIMAGE  SURVIVES.  Carried by P1-P11; P9 in case (A) is LZ plus
                  the weighted C^* action (isomorphism).
CUSP-A-VOID       SURVIVES, every N>=2, H2-free.  Carried by P1-P11 +
                  E1-E15.  Scope: C, algebraic, A_F homeomorphic to C
                  and singular, F Keller N>=2.  Not claimed off that
                  substrate (annuli, positive genus, (B3)).
LIN-ZAIDENBERG    Confirmed over C (Soviet Math. Dokl. 28 (1983) 200-204).
                  No non-quasihomogeneous unicuspidal curve homeomorphic
                  to C in C^2.  GATE's Invent. Math. 68 (1982) cite is
                  the wrong paper.
A^1 THROUGH CUSP  Impossible (smooth: germ would be a (p,q)-cusp;
                  singular: fibre over c empty).  Step (iv) stands.
PROP 6.1          Charged MPRIME text supports Reading A (a_p=1, a point
                  of E over c).  Instantiating A with NO-CUSP-PREIMAGE
                  yields 0=-1 in (M') and (L)+(K).  Empty case, not a
                  rescue.  CUSP-KILL's y_0 is not independent.
PERIPHERAL-RANK   SURVIVES with F1.  REFUTED as a group-theoretic claim:
                  N=4 (3,4) A=(1,2,0,3) B=(2,0,3,1) j=3 a=0 t=1 H_1=Z^3;
                  N=8 (2,7) A=(1,0,3,2,5,4,7,6) B=(0,2,3,4,6,1,7,5)
                  j=4 a=1 t=2; N=9 (3,4) A=(1,2,0,4,5,3,7,8,6)
                  B=(0,2,3,4,1,6,8,5,7) j=5 a=2 t=3.  All outside
                  2<=j<=a<=N-2.  Inside that window: 0 violators at
                  N<=9; 32/32 N=8 cage pass.
MERIDIAN-SPAN     SURVIVES with F1.  All 26 cage survivors (and every
                  tf transitive rep at 2<=N<=9 in the scan) violate
                  kappa*j<=a; those are the representations the theorem
                  kills.  Equality is the trivial representation.
CUSP-A-VOID-II    SURVIVES.  0 reps pass both gates.  rho(m)=1 is
                  non-transitive at N>=2; W>=2 is optional.
N=8 / N=9         16+6+6+4=32 cage, all PER pass, all MSP fail.
                  F9.1: 6 records, kappa=3 j=2 a=3 t=2.
NOT CLAIMED       (B3), (9,6,2), (9,6,4), existence of F, JC2.
                  PERIPHERAL-RANK is not a theorem about all torus-knot
                  covers.
CONSUMED          GATE/SW/HT/MI at §0 hashes; cover_h1 4/4 PASS;
                  LZ 1983; half-lives-half-dies; Wirtinger; Hamm; C[t]^*.
OPENS LEFT        GATE SUCC-1 (local pi_1 off a cone); (B3).
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `25242`.
- Body SHA-256:
  `7e8ccabef43874c3e817d2c7744b16f46f83380bdf3aaeb4894cb5ec75cbdcb7`.
- Frozen basis: `809f2d0175f202d63fe4b33c5b8e68f66791d126`.
