# PHI-IMMERSION adjudication: is the A2 analytic model a (B3) object?

Date: 2026-09-02  
Lane: PHI-IMMERSION hostile adjudication  
Method: frozen-input desk audit; one SymPy identity/Jacobian check; no other CAS  
Lifecycle: **CONDITIONAL THEOREM CONFIRMED / B3 FILING REFUTED / MODEL BRIDGE PROVISIONAL**

## 0. Integrity, scope, and verdict

Before reading the mathematics, `shasum -a 256` on the five frozen copies in
`/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.XicF3D/inputs`
returned exactly:

```text
58020a0e85692a6a92e16db18fe2d540f6073e9de596c1348d3596c3597e8202  ideation-20260902T0741Z-fable51.md
2710e90fdcbf1c2c9f61d6a606cf1e6553de5de65e4899367005433bc4f4e5f5  block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
5f28c56396aa809ff040f294a03cede7898ee6396160add14fceff93fce32fa4  one-cusp-a2-r2-opus5-20260901.md
86caf003268ddc40143daa68d439079dbd82d1dac41e1da93f33a661d52f96ac  cell-32-spec-sol56-20260901.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  mprime-alln-h2-opus5-20260902.md
```

All matched. Only those copies were used as campaign sources. Below they are
abbreviated `submission`, `structure`, `r2`, `spec`, and `MPRIME`. No canonical
ledger was edited and `jc2-lean` was not inspected.

The headline adjudication is:

| charged step | verdict | exact scope |
|---|---|---|
| (1) retained chart, etale/surjective, `A_iota=Phi` | **CONFIRMED** | Exact for the displayed morphism. **GAP[EXACT-MODEL-ID]** remains because the structure source calls its identification with the charged horn provisional. |
| (2) `C_0 subset A_F`, `L_0 subset E` | **CONFIRMED** | No H2 is needed; in fact `A_F=A_pi union pi(Phi)`. |
| (3) `E0` forces residue immersivity | **CONFIRMED** | “Immersion” means everywhere nonzero differential/unramified normalization, not a globally injective embedding. |
| (4) H2 gives `A_F=C_0` and no singular branch | **CONFIRMED, CONDITIONAL** | The conclusion is correct after a small proof repair. The assertion that r2/CELL-32 itself assumed H2 is **REFUTED**. |

Thus PHI-IMMERSION stands as a theorem about the declared factorization. The
declared A2 model cannot be the H2/(B3) quartic horn. That does **not** kill the
abstract (B3) row: it shows that the provisional bridge from that row to this
block surface/chart is inconsistent. The running coefficient lane is not
itself a (B3) lane.

## 1. Step (1): the retained chart and its full Jelonek set

### 1.1 Identity, etaleness, and fibres

The frozen structure report explicitly calls

```text
A=x^2,   U=x+x^3 y,   Z=2y+x^2 y^2
```

the retained cyclic chart (`structure:96-98`), and r2 calls the same formula the
source chart `iota` (`r2:139-146`). Substitution gives

```text
U^2 = x^2+2x^4y+x^6y^2 = A+A^2Z,
```

so it defines `iota:A2_(x,y)->S`. For
`q=U^2-A-A^2Z`, if `x!=0` then `q_Z=-A^2!=0`, so `(A,U)` are local coordinates
on `S`, and

```text
det d(A,U)/d(x,y) = 2x^4 != 0.
```

If `x=0`, then `q_A=-1`, `(U,Z)` are local coordinates, and
`det d(U,Z)/d(x,y)=2`. Hence `iota` is etale everywhere. The full three-row
Jacobian has minors

```text
2x^4,  4x(1+x^2y),  2(1+4x^2y+2x^4y^2),
```

so the two-case argument also exhausts possible rank loss.

Surjectivity is equally explicit. For `(a,u,z) in S`, if `a=0` then `u=0` and
the unique preimage is `(0,z/2)`. If `a!=0`, each of the two roots `x^2=a`
has

```text
y=(u-x)/x^3,
2y+x^2y^2=(u^2-x^2)/x^4=z.
```

Thus the fibre has two points off `Phi=V(A,U)` and one point on `Phi`. This is
precisely the retained-line/deleted-twin geometry distinguished in
`structure:38-48`.

### 1.2 The charged limit and all other escaping families

For the submitted family

```text
(x,y)=(epsilon,-2/epsilon^2+c)
```

direct expansion gives

```text
A=epsilon^2,
U=-epsilon+c epsilon^3,
Z=-2c+c^2 epsilon^2.
```

It leaves every compact subset of the source and tends to `(0,0,-2c)`. Taking
`c=-z/2` realizes every `(0,0,z) in Phi` as an asymptotic value.

There is no second escape type. Let `(x_n,y_n)` escape while its image
converges. Bounded `A=x_n^2` makes `x_n` bounded, so escape forces
`|y_n|->infinity` after extraction. Bounded `U=x_n+x_n^3y_n` rules out `x_n`
being bounded away from zero; hence `x_n->0`. Put `t_n=x_n^2y_n`. Since

```text
Z_n=y_n(2+t_n),
```

bounded `Z_n` and unbounded `y_n` give `t_n->-2`. Consequently
`A_n->0` and `U_n=x_n(1+t_n)->0`. More sharply,

```text
c_n := y_n+2/x_n^2 = (t_n+2)/x_n^2 = Z_n/t_n -> -z/2,
```

so every finite-image escape is asymptotic to the submitted family
`y=-2/x^2+c_n`.

Algebraically, over `D(A)=S-Phi` one has

```text
C[x,x^-1,y] = R[A^-1][x]/(x^2-A),   y=(U-x)/x^3,
```

with the displayed formula for `Z` checking the inverse. Hence the restriction
is a finite etale double cover, and therefore proper. Combining this upper
bound with the family above proves the full equality

```text
A_iota = Phi.
```

**Provenance qualification.** The algebra is definitive, but the frozen
structure source introduces `S` under **PROVISIONAL model identification**
(`structure:30-35`) and retains that qualification in its maximum-safe result
(`structure:611-620`). Therefore “this is the actual first map of a genuine
H2/(B3) horn” remains `GAP[EXACT-MODEL-ID]`; it is not an independently promoted
fact. This qualification is where the eventual contradiction must be charged.

## 2. Step (2): composition, `C_0`, and the retained source line

For complex affine varieties, define `A_h` by the escaping-sequence criterion:
`y in A_h` if some sequence leaving every compact subset of the source has
`h(x_n)->y`. For regular maps `X -h-> Y -g-> Z`, the applicable composition
rule is

```text
g(A_h) subset A_(g o h) subset A_g union g(A_h).          (2.1)
```

For the left inclusion, compose a witnessing sequence with `g`. For the right,
start with an escaping `x_n` whose composite image converges. If `h(x_n)` has an
escaping subsequence, its limit is in `A_g`; otherwise a bounded subsequence
converges in the closed affine variety `Y` to some `y in A_h`, and the target
limit is `g(y)`. The hypotheses are: complex affine varieties in their Euclidean
topology, regular (hence continuous) maps, and this sequence characterization.
Dominant generically finite maps are needed for the usual algebraic “Jelonek
set” terminology and purity results, not for the two inclusions. Here `iota`,
`pi`, and `F` are same-dimensional etale/dominant maps, so the standard
Jelonek setting applies.

Apply (2.1) to `F=pi o iota`. It gives

```text
pi(Phi) subset A_F subset A_pi union pi(Phi).             (2.2)
```

There is also a useful strengthening omitted by the submission. Because
`iota` is surjective, an escaping sequence in `S` witnessing a point of `A_pi`
can be lifted pointwise to `A2`; every such lift must escape, since a convergent
lift would give a convergent image in `S`. Thus `A_pi subset A_F`, and

```text
A_F = A_pi union pi(Phi).                                 (2.3)
```

On `Phi=Spec C[Z]`, the restriction of `pi` is
`Z |-> (f_0(Z),g_0(Z))` (`structure:164-180`). It is nonconstant: an etale,
quasi-finite surface map cannot contract the curve `Phi` (and Step (3) gives an
independent coefficient proof). A polynomial map from `A1` with a nonconstant
coordinate is finite onto its image: if `h` is that coordinate, `Z` is integral
over `C[h]`. Its image is therefore closed. Consequently the notation in the
charge is legitimate as a set equality, not merely a closure convention:

```text
C_0 := pi(Phi)
     = closure{(f_0(z),g_0(z)): z in C}
     subset A_F.                                          (2.4)
```

Finally, for the retained line `L_0={x=0}`,

```text
iota(0,y)=(0,0,2y) in Phi,
```

so `F(0,y) in C_0 subset A_F` for every `y`. Hence
`L_0 subset E:=F^-1(A_F)`. Step (2) is confirmed without H2.

## 3. Step (3): the exact seven-polynomial dictionary

The spec's seven free polynomials are

```text
eta, s, p, C1, q, r, G in C[Z]
```

with `a*b*kappa!=0` (`spec:48-54`). After its derived definitions,

```text
P  = p + A C1 + A^2 C2,
Q  = q + A D1 + A^2 D2,
R0 = r + A E1 + A^2 E2,
S0 = s,
f=P+UQ,                 g=R0+US0                         (3.1)
```

(`spec:57-63,72-80`). In the completion along `Phi`, put `u=U`; then
`A=u^2-Zu^4+O(u^6)` (`structure:57-80`). Therefore

```text
f = p + q u + O(u^2),       g = r + s u + O(u^2),
f_0=p,  f_1=q,              g_0=r,  g_1=s.              (3.2)
```

In the older coefficient notation these are
`p=C_0`, `q=D_0`, `r=E_0`, `s=L_0`. The coefficient `E_0=r` must not be confused
with the equation tagged `E0`, and the free polynomial `G` must not be confused
with the target coordinate `g`.

The equation tagged `E0` is exactly

```text
2(q r' - p' s) = kappa,       kappa != 0,                (3.3)
```

where prime means `d/dZ` (`spec:43-45,95`). If `p'(z)=r'(z)=0` at any `z`, the
left side of (3.3) vanishes there, a contradiction. Hence

```text
(f_0'(z),g_0'(z))=(p'(z),r'(z)) != (0,0)   for every z.
```

This confirms the differential/holomorphic immersivity asserted in
`structure:172-180`. It does not mean a globally injective algebraic immersion:
the same source supplies distinct `z,z'` with the same image
(`structure:178-183`). The safe wording is **everywhere unramified
normalization parametrization**.

## 4. Step (4): H2, PROFILE, and the proof repair

MPRIME's standing H2 says that `D=A_F` is an irreducible Jelonek curve
(`MPRIME:26-31`). By (2.4), `C_0` is a nonconstant closed irreducible curve
contained in it. Two irreducible curves of dimension one cannot be properly
nested, so

```text
H2  =>  A_F=C_0.                                          (4.1)
```

There is one hostile correction to the submitted proof. “Every point has a
smooth branch” alone does **not** imply PROFILE (0)/(B1): at a multibranch point
one branch could be smooth and another singular, which is precisely how (B2)
or (B3) can occur. The conclusion is nevertheless repairable from a source the
submission already cites. `structure:178-180` identifies
`Phi=A1 -> C_0` as the normalization. Every analytic branch of `C_0` therefore
corresponds to a normalization preimage `z`; (3.3) makes its plane
parametrization have multiplicity one. Thus **every branch**, not just one branch
through every point, is smooth.

For the full charged function-pair packet, `structure:180-183` also supplies
distinct normalization points with the same image. Those points give a
multibranch singularity. Consequently the exact H2 filing of that packet, after
discarding its incompatible cusp label, is **(B1)**, not merely `(0)/(B1)`.
For a bare coefficient pair without the collision condition, the preliminary
geometric alternatives are row (0) or (B1).

MPRIME classifies row (0) as empty at every degree and (B1), defined by a
multibranch point with every branch smooth, as empty for `N<=16`
(`MPRIME:413-430`). Its NODAL-ALL-N theorem explicitly has the stronger
all-branches-smooth hypothesis and leaves the first numerical survivors at
`N>=17` (`MPRIME:340-384`). For this particular retained chart the floor is
sharper. In function fields,

```text
K(S)=C(T,V),   T=x^-2,   V=x^-1+xy,
C(x,y)=K(S)(x),          x^2=T^-1.
```

The `T`-valuation of `T^-1` is odd, so it is not a square in `C(T,V)` and
`[C(x,y):K(S)]=2` (`r2:81-90,139-146`). If
`m=[K(S):C(f,g)]`, multiplicativity gives

```text
N=[C(x,y):C(F)]=2m.                                      (4.2)
```

Thus an H2/B1 realization of this factorization can occur only at **even
`N>=18`**. This is a necessary range, not attainment or an existence witness.

The scope error is separate and material. r2 defines only the constant-bracket
system with an A-degree cap, for arbitrary residue data (`r2:26-37`); it says
rank-four field degree, the boundary curve `B`, and the partition table are not
used (`r2:69-74`), and reiterates that it does not touch the boundary/cusp census
(`r2:680-684`). CELL-32 is likewise only a finite coefficient decision bundle
(`spec:25-33`), and even a live point receives a degree label only after a
field-degree check (`spec:699-702`). MPRIME itself says N4-PIN is an input A2
*may consume*, one-directionally, not an A2 hypothesis (`MPRIME:642-647`).
Therefore Step (4)'s conditional implication is confirmed, but “the running A2
lane assumed H2” is refuted.

## 5. Which cusp is the horn's cusp?

The sources keep five nearby objects distinct:

| object | location and meaning |
|---|---|
| `c in B=A_F` | The affine **target** unibranch singularity. This is MPRIME's (B3) cusp. |
| `u_c in pi^-1(c) cap S` | The etale interior companion. `S` is smooth there; the pulled-back divisor `pi^-1(B)` has the cusp germ. |
| the `(3,1)` point in `R_bd=Y-S` | A deleted length-three ramification point over `c`; its special completion is OPEN. |
| `Phi subset S` | The smooth interior multiple-fibre line, not a boundary component. |
| `{T=0}` | The pole divisor for the A-degree filtration in a compactification of `S-Phi`; not the target cusp. |

The structure report explicitly separates `Phi`, `R_bd`, and deleted source
lines (`structure:38-48`), calls `c` the target cusp and `u_c` its interior
companion (`structure:198-221`), and warns that it has no ordinary-cusp equation
for the `(3,1)` boundary germ (`structure:236-241`). MPRIME defines “cusp” as a
unibranch singular germ of `A_F` (`MPRIME:401-405`), identifies the same
rank-four `B` with irreducible `A_F` (`MPRIME:607-619`), and files the horn in
(B3) (`MPRIME:624-647`). N4-PIN's unique cusp carries the `(3,1)` cycle and
`a_c=1` (`MPRIME:580-605`). There is no infinity-cusp reinterpretation.

Accordingly the contradiction under H2 is real. Equation (4.1) makes
`Phi->B` surjective. The structure report says the only point of `S` over the
cusp is the etale companion (`structure:621-625`), so it must be the point of
`Phi`; but the corresponding branch is smooth by Step (3), whereas a cusp is a
singular unibranch germ. If one instead retains the report's earlier open case
`u_c notin Phi` (`structure:198-203`), surjectivity supplies a separate point of
`Phi` above `c`; moreover an `S-Phi` point has two `iota`-preimages. The
submission's lower bound `a_c>=2` is conservative—the displayed model gives at
least three—contradicting N4-PIN's `a_c=1`.

What fails is therefore the simultaneous package

```text
provisional A2 exact-model identification + H2 + affine (B3) cusp.
```

The intended structure horn was trying to model the **same affine (B3) cusp**,
not a boundary cusp. The bare r2/CELL-32 equations, however, encode no cusp at
all. They are only constant-bracket algebra on `S` until the global bridge is
proved.

## 6. Re-filing and computational residue

The correct filing has three levels.

1. **Bare A2/CELL-32:** `PROFILE-UNTYPED`, `N-UNTYPED`. A NONEMPTY coefficient
   cell is not yet a Keller counterexample, a degree-eight object, or an `A_F`
   profile. Absence of an H2 assumption is not proof of `not H2`.
2. **Add H2 and the charged residue collision, but remove the cusp label:**
   PROFILE **(B1)**, possible only at even `N>=18`. The range is necessary only;
   MPRIME explicitly warns its floors are not witnesses (`MPRIME:824-829`).
3. **Add a genuine global realization at `N<=16`:** it cannot satisfy H2, so
   `A_F` must be reducible and the candidate belongs to the reducible/companion
   front. Equation (2.3) describes the mechanism: `C_0` is one component and
   any additional/cuspidal component must come from `A_pi`. MPRIME expressly
   leaves the reducible N=4 cage untouched (`MPRIME:20-24`).

The claimed quartic H2/(B3) use is therefore **REFUTED**. The useful remaining
questions are not more untyped U-corners. They are, in order:

```text
m=[K(S):C(f,g)];
A_pi and the irreducible components of A_F=A_pi union C_0;
whether the residue collision/normalization hypotheses actually hold;
then either the even-N>=18 (B1) branch or an explicitly reducible branch.
```

CELL-32 remains legitimate algebra: its corrected seven-polynomial/seven-law
system and desk-closed `G=0` section are not invalidated. But finite boxes prove
only box-local emptiness and never close the unbounded OPEN (`spec:567-570,
691-702`). Such work is confirmatory unless one of the bridge questions above
has already selected a live global branch.

**Allocation recommendation.** Stop new box01 A2 launches at the next safe
checkpoint; preserve the running job's result only as finite-box algebraic
evidence, because the spec itself says the boxes are a schedule rather than a
completeness bound (`spec:327-341`) and an EMPTY leaves `OPEN[A2-CELL-32]`
unchanged. Retarget the `a2-ubound` seat from a U-bound hunt to the field-degree
and component bridge `(m,A_pi,A_F)` above. Reopen heavy A2 computation only for
a proved even-`N>=18` B1 target or a declared reducible companion target. The
original N=4 H2/(B3) purpose merits neither the frontier seat nor the 64-vCPU
window; redirect that box to a genuine B3 instrument once a noncontradictory
analytic model is specified (MPRIME lists braid/ZvK or its pinned representation
gate at `MPRIME:703-712`).

## 7. Typed final block and guardrail audit

```text
STEP (1)  CONFIRMED in the declared model: iota etale, surjective,
          A_iota=Phi; all escapes are the deleted-twin asymptotic family.
          GAP[EXACT-MODEL-ID]: horn identification remains PROVISIONAL.
STEP (2)  CONFIRMED: C_0=pi(Phi) subset A_F, L_0 subset E;
          stronger equality A_F=A_pi union C_0.
STEP (3)  CONFIRMED: f_0=p, f_1=q, g_0=r, g_1=s and
          2(qr'-p's)=kappa excludes a common derivative zero.
STEP (4)  CONFIRMED conditional on H2, after the all-branches repair;
          REFUTED that r2/CELL-32 assumed H2.

REFILING  bare lane = PROFILE/N-UNTYPED;
          H2 + charged collision = (B1), even N>=18 only;
          actual N<=16 survivor = REDUCIBLE-A_F;
          N=4 + H2 + (B3) + this A2 bridge = EMPTY/INCONSISTENT.

CUSP      affine target cusp of A_F, exactly MPRIME (B3);
          not Phi, not {T=0}, not a cusp at infinity, and not the deleted
          ramification point over it.
```

FALLACY-v2: `Phi` (interior divisor), `{T=0}` (pole divisor), the target cusp,
its normalization place, `u_c`, and the deleted boundary point were kept
distinct. The parity statement `N=2m` is a field-degree identity, not
attainment; `N>=18` is only a floor. No finite degree box was promoted to a
global bound or witness. Equation-tag `E0`, coefficient `E_0=r`, and prime as
`d/dZ` were disambiguated. No saturation or raw-remainder claim was made. This
report makes no exit-price assertion, so no `charge_basis` declaration is due.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->`
  line, including its terminating newline; this seal is outside the body.
- Body bytes: `18646`.
- Body SHA-256:
  `4820a2cffbea7b9a8fcbc2ca853dfc40d903e18632adba78e4353e1977056e52`.
- Frozen inputs: `5/5 SHA-256 matched`.
- Status: **SEALED AT COMPLETION**.
