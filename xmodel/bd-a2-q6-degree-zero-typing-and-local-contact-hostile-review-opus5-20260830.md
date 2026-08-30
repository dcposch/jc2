# Hostile review (Opus 5): q=6 degree-zero typing repair and local-contact closure

Date: 2026-08-30 UTC
Reviewer: Opus 5, different-model hostile review
Charged basis: `f63b8bd9400ff86eb385c2f705e885015c624068`
Receipt status: `ABSENT` (no exit-price assertion; no `charge_basis` line)

## 0. Custody

All ten charged SHA-256 values reproduce byte-exactly. Derived checks:

```text
typing adjudication body 9818 bytes 650be07da65edee18d7e7d3a8482675c59e61c35c4bfc7a6ed6e90edc0c511c5  MATCH seal
local audit body        22514 bytes 941d4e27b95bee2483b98fa62c4e1b9c9b94e7dff7aa200848ab03977461522d  MATCH seal + v2 §2
v2 body                 14628 bytes 03590225ea52239df4d485b4b7aaac015af4d4e8975aba299b637663f6ce2f34  MATCH seal
prior opus5 review body 23422 bytes c968ed6f60b3cd65868050a49180a5f5bbc37ae2241042e9aa6870290f75c90f  MATCH adjudication §1
carrier integration body 13359 bytes a946988a77a558786a1226d9d7f05c179c7662f33685bf1acab211ce95e884e0  MATCH seal
v1 engine ops/q6_f5_affine_ade_threat_replay.py  b892cd1520f13f10093fc51f547672cb8145ad4949c92a86a6ecb9055f3bdd46  MATCH v2 pin
```

No `jc2-lean` access of any kind, no D3 report, no sibling external-model
prompt/log/report/receipt, no heavy CAS, no web, no `pilot-local.log`. No
charged file, artifact, or Git state was edited. All algebra below is
independent desk computation (`sympy`/integer lattice arithmetic) and the
finite replays are the charged programs run unmodified; the two diagnostic
enumerations in §7 and §8 are separate drivers that import the hash-pinned
engine without writing to it.

I did not defer to any seal, manifest, verdict, or prior model identity. The
`A`/`B` geometry, the nine-blowup lattice, the F5 blowup charts, the polar
germs, and the affine-root machinery were each rebuilt from scratch and only
then compared.

---

## 1. Geometry of `A`, `B`, `r` and the both-null typing — `CONFIRMED`

**The frame is literally a bidegree-(2,3) surface in `P2 x P1`.** I did not
take this from the charged text; I reconstructed it from the invariants.
With `h,l` the two hyperplane classes on `P2 x P1` (`h^3=0`, `l^2=0`,
`h^2 l=1`) and `X in |2h+3l|`:

```text
A^2 = h^2(2h+3l) = 3       A.B = hl(2h+3l) = 2       B^2 = l^2(...) = 0
K_X = (-3h-2l)+(2h+3l) = -h+l = -A+B                 K_X^2 = -1
(A+B)^2 = 7
```

These are exactly the charged integration §2 values `A^2=3, A.B=2, B^2=0,
K=-A+B, K_Xtilde^2=-1`, and `(A+B)^2=7` agrees with the independent
`Bl_9 F_2` computation in §2 below. So `pi:X->P2` is the degree-three cover
(`A^2=3`, the cubic incidence), `rho:X->P1` is the conic bundle
(`A.B=2`), and the nine contractions to `F_2` follow from `K^2=-1` vs
`K_{F_2}^2=8`. The charged claim that "both factors of `O_X(1,1)` come from
the ambient `P2 x P1`" is corroborated, not assumed.

**`A+B=r^*O_X(1,1)` with ample downstairs bundle.** `O(1,1)` is very ample on
`P2 x P1` (Segre), so its restriction to the closed subvariety `X` is ample.
`A` and `B` are the `r`-pullbacks of `pi^*O_{P2}(1)` and `rho^*O_{P1}(1)`,
hence `A+B=r^*(O(1,1)|_X)`. **Checked literally.**

**Projection formula step.** Let `C` be irreducible on `Xtilde` with
`A.C=B.C=0`. Then `(r^*H).C=H.r_*C` with `H=O(1,1)|_X` ample. If `r(C)` were
a curve, `r_*C=deg(C/r(C))·r(C)` is a nonzero effective 1-cycle and
`H.r_*C>0`. Hence `r_*C=0` and `r(C)` is a point: `C` is `r`-exceptional.
**Literally correct, and it is the right repair** — the prior review's
objection rested on `A` being nef-not-ample, which is true (`A.Z_J=0` for a
contracted carrier, so `pi` is *not* finite; the campaign's "reduced finite"
label must not be read as finiteness of `pi`), but `A+B` is ample and that
suffices.

**Du Val minimality types it.** `r` is the *minimal* resolution (the charged
frame contracts nothing crepant-trivially beyond the Du Val exceptional
locus), and on the minimal resolution of a rational double point every
irreducible exceptional curve is a smooth rational `(-2)`-curve. So `C` is a
`(-2)`-root, not a strict/nonexceptional polar prime. **CONFIRMED.**

## 2. The integral root list — `CONFIRMED`

On `Bl_9 F_2` (`S0^2=-2, S0.F=1, F^2=0, P_i^2=-1`), write
`C=sS0+bF-sum x_iP_i`.

* `B.C=F.C=s`, so `B.C=0` kills the `S0` coefficient exactly. **✓**
* Then `A.C=2b-sum x_i` and `C^2=-sum x_i^2`.
* `C^2=-2` (forced by §1, not assumed) gives `sum x_i^2=2`: exactly two
  `x_i=+/-1`.
* `2b=sum x_i` then gives, with no other solution:
  `{+1,-1} -> b=0`, `{+1,+1} -> b=1`, `{-1,-1} -> b=-1`.

So the complete integral list is `+/-(P_i-P_j)` and `+/-(F-P_i-P_j)`.
**(2.1) VERIFIED exhaustive.** I confirmed by direct lattice arithmetic that
`S0.(F-P_i-P_j)=1` for every pair and `S0.(P_i-P_j)=0`. **(2.2) ✓**

The exclusion of the `F`-family away from the F5 tree is sound *given* the
charged binding statement (integration §3) that no ADE point of `X` lies on
`H` away from `p_0`: exceptional curves over an affine ADE point then satisfy
`S0.C=0`, which `F-P_i-P_j` never does. This is an inherited dependency, not
a new assumption, and it is correctly cited.

**One structural strengthening the adjudication does not state.** `S0` meets
each local tree in a *single* component with multiplicity one
(`S0.R1=1, S0.R2=0`; `S0.E1=1, S0.E2=S0.E3=0`), so each F5 tree contains
**exactly one** `F`-type root. There is no second, unregistered `F`-type
class available anywhere.

## 3. B3/U3 chronologies, `M_R`, and the double-count — `CONFIRMED`

Recomputed every class from the charged chronologies (4.2)/(4.3):

```text
R1=F-P_l-P_o1  A.=0 B.=0 C^2=-2 S0.=1 T.=1 L.=1     R1.R2=1
R2=P_o1-P_o2   A.=0 B.=0 C^2=-2 S0.=0 T.=0 L.=0
E1=F-P_o1-P_o2 A.=0 B.=0 C^2=-2 S0.=1 T.=1 L.=0     E1.E2=E2.E3=1, E1.E3=0
E2=P_o2-P_l    A.=0 B.=0 C^2=-2 S0.=0 T.=0 L.=1
E3=P_o1-P_o2   A.=0 B.=0 C^2=-2 S0.=0 T.=0 L.=0
```

This is an `A2` chain with `L,S0,T` all on `R1` (`L` and the `S,T` pair at
distinct points), and an `A3` chain with `S0,T` on the spin `E1`, `L` on the
central `E2`, `E3` free — exactly the marked tags `B_3/A_2` and `U_3/A_3` of
integration §3, reproduced independently. Both are also independently
confirmed by the analytic charts of §6 below (`L` at `Z=0`, `S,T` both at
`Z=1`; and for U3, `L` sits at the residual `A1` point that becomes `E2`).

`R1` and `E1` are in `M_R` **with coefficient two**:

```text
M_R(B3,tau!=0) = 2R1+R2   = 2F-2P_l-P_o1-P_o2
M_R(U3)        = 2E1+2E2+E3 = 2F-2P_l-P_o1-P_o2      (equal, verified)
M_R(B3,tau=0)  = 2R1+2R2  = 2F-2P_l-2P_o2
```

**Exact identity found, stronger than the charged claim.** With `L=P_l`
(Du Val `p_0`),

```text
A - H = A - (L+S0+T) = M_R           (verified in both markings)
```

so `pi^*(line at infinity) = H + M_R` literally. `M_R` is therefore not a
bookkeeping choice: it is the exceptional part of the pullback of the
infinity line, and `C_str = r^*R_X - M_R` is by construction the residual
strict part. Recomputed:

```text
C_str(tau!=0)=4S0+9F-P_o1-P_o2-2sum_I P_i  c=(0,1,1,2^6)  sum=14 sumsq=26
C_str(tau=0) =4S0+9F-2P_o1-2sum_I P_i      c=(0,2,0,2^6)  sum=14 sumsq=28
both: A.C_str=8, B.C_str=4, S0.C_str=1, T.C_str=1
```

matching audit (5.1)–(5.5) exactly. Adding `R1` (or `E1`) again as a strict
prime would count one irreducible curve twice inside `r^*R_X`; an irreducible
curve is either `r`-exceptional or not, and these are. **No omitted object;
the alleged omission is a type conflation, as adjudicated. CONFIRMED.**

## 4. The other `A`-null type — `CONFIRM_WITH_CORRECTIONS`

**Proved, not merely cited.** Let `C` be irreducible, nonexceptional,
`A.C=0`. Then `(A+B).C=B.C>0`, so `r(C)` is a curve on `X` contracted by
`pi`. Because `X` sits in the *product* `P2 x P1`, a positive-dimensional
fibre of `pi` is contained in `{q} x P1`, which is irreducible of dimension
one; hence it equals `{q} x P1`. Therefore

```text
B.C = rho^*O(1).({q} x P1) = 1        exactly.
```

`{q} x P1 = P1` is smooth rational, so its proper transform is smooth
rational, `p_a=0`, and `K.C=-A.C+B.C=1` gives `C^2=-3`. **`B.C=1` and
`C^2=-3` CONFIRMED.**

**`|J|=5` and `J=O union K` are forced, and I derived them rather than
importing them.** Writing `C=aS0+(2a+eps)F-sum x_iP_i`, `B.C=1` gives `a=1`;
`A.C=0` and `C^2=-3` give `sum x_i = sum x_i^2 = 5+2eps`, so every `x_i` is
0 or 1 and `|J|=5+2eps`. The lattice alone therefore permits `|J|=5,7,9`.
The extra input is disjointness from `H`:

```text
S0.Z = b-2 = eps   -> eps=0 -> |J|=5
T.Z  = 3-|I cap J| -> |I cap J|=3
L.Z  = [l in J]    -> l not in J
=> J = O union K, K subset I, |K|=3.      (20 candidates = C(6,3))
```

matching integration §4 (20 `q=6` candidates) and audit (5.6) exactly.

**Correction (one missing step in the adjudication).** §2.2 goes from "its
image on `X` is contracted by `pi`" straight to `Z_J` with `|J|=5`. The
binding carrier theorem states `|J|=5` only for carriers over an **affine**
target point. The missing half-line: any curve contracted to a point of the
infinity line lies in `pi^*(L_inf)=H+M_R`, whose components are
`L,S0,T` (each with `A`-degree one, hence not contracted) and exceptional
roots (case 2.1). So a *nonexceptional* contracted curve is over an affine
point, is disjoint from `H`, and `eps=0` follows. Add this sentence; the
conclusion is unaffected.

**Coefficient claims — verified.** In `c=(0,1,1,2^6)` both outside entries
are one and every `J` contains both, so at most one carrier, coefficient one;
`C_str-Z_J` has `c^Z=(0,0,0,1,1,1,2,2,2)`, `sum=9`, `sumsq=15`, `A.=8`,
`B.=3` (all recomputed). In `c=(0,2,0,2^6)` one outside entry is zero while
every `J` contains it, so no carrier is effective — and this is
orientation-independent, since reversing the outside chronology only swaps
which outside entry vanishes. **CONFIRMED.**

## 5. Exhaustiveness at positive `A`-degree — `CONFIRMED` (with a proof the adjudication does not give)

The charged argument ("registered germs total eight; an extra prime would
exceed eight") is correct but leaves the localization implicit. The literal
statement is:

* `A.C_str` computed against the *infinity* line is
  `C_str.(H+M_R)` by the §3 identity, i.e. the total contact of the strict
  ramification with the infinity fibre, summed over **all** points of `H`.
* At `p_0` that contribution is, exactly and for every member of the family,

```text
len C[[v,z]]/(h,h_z) = ord_v Res_z(h,h_z) = ord_v(-v^8(v+1)) = 8
```

  (verified symbolically; equivalently Teissier `mu+mult-1=6+3-1=8`, with the
  three smooth branches of `h` pairwise meeting in `1,1,2`). This is
  family-invariant because `p|_{u=0}=f_z|_{u=0}=h_z` for every
  `f=h+u(a u+b v+c)`.
* Contracted carriers lie over affine target points, so none passes through
  `p_0`; locally at `p_0`, `div(p)` is the strict germs only.

Since the global total is `8` and the `p_0` contribution is already `8`, every
other local contribution is zero: **no strict prime meets the infinity fibre
away from `p_0`, and no strict prime has any `A`-degree away from the F5
cluster.** Combined with §1–§4 the trichotomy is exhaustive. **CONFIRMED.**

## 6. Independent reconstruction of the q=6 local contact census — `CONFIRM_WITH_CORRECTIONS`

Everything below was recomputed from `h=z(z-v)((1+v)z-v)`,
`f=h+u(a(z)u+b(z)v+c(z))`, `p=f_z`. Every displayed equation of the charged
audit reproduced **exactly**.

### 6.1 `B3/A2`

* Surface tag. Quadratic part `u(v-tau z)` has rank 2; the splitting-lemma
  residual is `(1-tau)^2 z^3+O(z^4)`, so `A2` iff `tau!=1`. **(2.1) ✓**
* `v`-chart: `f/v^2 = U(1-tau Z)+v Z(Z-1)^2+O(vU,v^2)`. **(2.2) ✓**
  Exceptional at `v=0` is `U(1-tauZ)=0`: `E1={U=0}`, `E2={Z=1/tau}`, node at
  `Z=1/tau`, going to `Z=infinity` as `tau->0`. **✓**
* Branch sites: `h`'s three branches `z=0`, `z=v`, `z=v/(1+v)` give
  `q_L: Z=0` and `q_ST: Z=1` shared by `S,T`. Their intersection drops
  `2 -> 1` and `1 -> 0`, i.e. `S.T=1`, `L.S=L.T=0` — the `q=6` values, derived
  analytically. **✓**
* `U=-vZ(Z-1)^2/(1-tauZ)+O(v^2)` and

```text
p/v^2 = (Z-1)(-2 tau Z^2+3Z-1)/(1-tau Z) + O(v)      (2.4) exact, zero residue
```

* `m=(2,1)`: `ord_{E1}(p)=2` (the `v^1` term `-tau U` is itself `O(v)` on
  `E1`), `ord_{E2}(p)=1` (there `U` is a generic unit). `n=C_{A2}m=(3,0)`.
  The three finite zeros of (2.4) are exactly `n_1=3`. **(2.6) ✓**
* `Z=1` germ: solved the joint `f=p=0` expansion. `U1=U2=0`, then
  `k=-1/2` and `u=v^4/(4(1-tau))+O(v^5)`, **independently of every
  coefficient**. **(2.5) ✓** Slope `-1/2` lies strictly between the section
  slopes `0` and `-1`, so `S`, `T` and this germ separate after one blowup of
  `q_ST` — for *all* parameter values, so no hidden tangency stratum.
* Quadratic block: `Delta=9-8tau`; roots never equal `0`, `1` or `1/tau` while
  `tau!=1`; at a simple root `u=unit·v^2`, degree 2. `4+2+2=8`. **(2.8) ✓**
  `Delta=0` forces `tau=9/8` and the double site `Z=2/3`, distinct from all
  boundary sites and from the node `Z=8/9`. **✓**
* Weierstrass trichotomy (2.9) is exhaustive over `C[[r]]` (even order ⟹
  analytic square root, two branches meeting with multiplicity `k=ord(d)/2`;
  odd order ⟹ nonsquare ⟹ one branch, ramified; zero ⟹ literal square).
  **Consistency check I added: all three rows have weighted total `4`, so
  every row sums to the invariant `8`.** ✓

### 6.2 `tau=0`

* `z`-chart `u=zx, v=zy`:
  `f/z^2 = xy+z[(1-y)^2+x(a1x+b1y+c2)]+z^2(y-y^2)`; the `z`-coefficient at the
  node is `1`, so the blown-up surface is smooth there. **(2.10) ✓**
* `p = z^2[(y-1)(y-3)+a1x^2+b1xy+2c2x+O(z)]`. **(2.11) ✓**
  Restrictions: `E1 -> (y-1)(y-3)`, `E2 -> a1x^2+2c2x+3`, node value `3`.
* `m=(2,2)`, `n=C_{A2}m=(2,2)`: neither restriction is ever identically zero
  (constant `3` on `E2`), so this is family-invariant and `(2,1)` cannot be
  restored. **(2.13) ✓**
* `E1` sites `y=1,3` (i.e. `Z=1,1/3`, agreeing with (2.4) at `tau=0`), degrees
  `4` and `2`; `E2` residual `Q_E2=a1X^2+2c2XW+3W^2`, never zero, never at the
  node, discriminant `D0=c2^2-3a1`. **(2.14)–(2.15) ✓**
* Site-count consistency: `n_1=2` equals the two finite `E1` roots (so the
  free endpoint `q_L` of `E1` carries no contact, and indeed (2.4) is `1` at
  `Z=0`); `n_2=2` equals the two projective roots of `Q_E2` including the free
  endpoint. **No omitted site.**
* Partitions `4+2+1+1`, `4+2+2`, `4+2+2·1` all sum to `8`. **(2.17) ✓** The
  doubled realisation is genuine: for `a=c=0,b=1`, `p=h_z`, and along the
  `u`-axis `v ~ -z^3/u` gives `p ~ 3z^2`, so `ord_C(p)=2` with `ord_C(u)=1` —
  coefficient two, `A`-degree one. **✓**

### 6.3 `U3/A3`

* `a0!=0` is forced by normality (else `z | f`). **✓** Critical value
  `-a0 v^4(8a0v-c1^2+2c1v)/c1^4 = (a0/c1^2)v^4+O(v^5)`, so the tag is `A3`
  for every higher coefficient. **✓**
* `f/v^2=U(a0U+c1Z)+vZ(Z-1)^2+O(v)`; `E1={U=0}`, `E3={a0U+c1Z=0}`, residual
  `A1` at `U=Z=0`. `S,T` at `Z=1` on `E1`; `L` sits **at the residual `A1`
  point**, so after its resolution `L` meets `E2` — reproducing
  `L.E2=1, L.E1=L.E3=0` and the marked "central vertex" tag. **(3.1)–(3.2) ✓**
* `E1` initial polar `= 2Z(Z-1)`: contacts at `Z=1` (the smooth germ) and
  `Z=0` (the cusp, at the node after resolving the `A1`). Hence
  `n=(2,1,0)` and `m=C_{A3}^{-1}n=(2,2,1)`. **(3.6) reconstructed, not
  matched by coincidence. ✓**
* Cusp: substituting `v=t^2, z=lam t^3+mu t^4, u=-t^4/c1+nu t^5` gives
  `p:t^5 -> nu=4lam/c1` and then `f:t^8 -> a0+2c1^2 lam^2=0`, i.e.
  **`2lam^2=-a0/c1^2`** — the audit's sign is right (my first hand pass
  dropped the `nu t^5` back-reaction). `ord_t(u)=4`, `ord_t(v)=2`: a genuine
  cusp of `A`-degree 4. **(3.3)–(3.4) ✓**
* Smooth germ: `p:z^3 -> k1=1/2` (i.e. `y=z-v=-z^2/2`) and
  `f:z^5 -> u=z^4/(4c1)+O(z^5)`. **(3.5) ✓** Slope `1/2` strictly between the
  section slopes `0` and `1`.
* `4+4=8`. Every controlling coefficient is a nonvanishing function of
  `a0,c1` only, and **none of `b1,c2,a1` enters at the determining orders**, so
  `U3` has no modulus-special cell — verified, not asserted.

### 6.4 Omission hunt — result

Searched for zero polynomials, collisions, doubled and infinitely-near cases:
no site polynomial can vanish identically (`E1` fixed factors; `E2` constant
term `3`); no quadratic root collides with `q_L`, `q_ST`, or the node; the
`E1`/`E2` contact counts `n_i` are exactly saturated by the found sites, so no
free-endpoint contact is missed; double sites are handled by the two
exhaustive Weierstrass trichotomies at arbitrary depth. **I found no omitted
case.** The audit's `lambda_ij` correction in §6 is the right one, and the
engine's `tangent:i,j` rule (accepting any `lambda>=1`) is a strict
*relaxation* of it — the safe direction for an elimination.

### 6.5 Corrections required on the local audit

1. **The `a(0)=0` normalization is asserted, not proved** (a target shear
   preserving `u=0` acts trivially on `h`, and completing the square in `u`
   is a *source* change that reintroduces `uv^2`-type terms outside the
   ansatz). This does not damage anything: I recomputed both charts with
   `a(0)=a0` free. The `E1` initial polar (2.4) is **identically independent
   of `a0`**; the `tau=0` residual becomes
   `Q=(a0^2-a0b1+a1)X^2+2(2a0+c2)XW+3W^2` with
   `D0=a0^2+3a0b1+4a0c2+c2^2-3a1`, still with `W^2`-coefficient `3`, still
   never zero at the node, and with the identical trichotomy. State the
   census as normalization-invariant rather than relying on the shear.
2. **The cell split is exhaustive only modulo the upstream tag list.** `B3`
   assumes `b(0)!=0` and `U3` assumes `b(0)=0, c1!=0`. The remaining cell
   `b(0)=0` and `c'(0)=0` has quadratic part `a0u^2` of rank one, hence
   corank two, hence `D`/`E` type — outside the `q=6` marked list
   `{B_3/A_2, U_3/A_3}` of integration §3. Cite that, do not leave it silent.
3. **The `tau=1` boundary of the `B3` cell** is not an unhandled stratum: it
   is the `B_4/A_3` row eliminated upstream ("the singleton contact is
   internal"). The audit says only "the tag is exactly `tau!=1`"; name the
   row that absorbs it.

With those three sentences added, **the local-contact review gate is
closed**, not merely repeated: I reconstructed every `U3` and `B3` modulus
stratum, degree/Cartier weight, pair rule, physical-site chronology, and
exceptional vector independently, and all agree.

## 7. Replays, mutations, and whether code must change — `CONFIRMED`, with a named finding

```text
ordinary / -O / -OO : byte-identical, 37859 bytes,
  27ca7c500f411843c34c1aad60d51261b6e66e9ba712eddf48aa67893add8f3e   (= v2 §7)
corrected raw sha    33d8841e0609857220f80fc3d46e8a33ccfc655ef19bfb42b465ee802ae13216   ✓
survivor payload     830 bytes ab2fc3c6c5d47160fa947542dd5d33e375c9221a43df05c10cd99cfb6926b46d ✓
AST assert nodes     v1 = 0, v2 = 0                                   ✓
--mutate-drop-vertical  rc=1 "FAIL:vertical a=0 domain was not exercised"
--mutate-contact        rc=1 "FAIL:q6 baseline multiplicity sum must be fourteen"
  both, in ordinary, -O and -OO                                       ✓
all 28 rows: pair_condition_matches_before_carrier = 0,
             energy_pruning_applied = false                           ✓
added metas 142, added candidate records 3317                         ✓ (= (0.2))
```

Every cell of both v2 §5 tables and of the §4 / (4.3) minima tables
reproduces from the run, including the honest `0` in the `tau=0` doubled row.
Timing 3.8 s, standard library.

**Types are kept distinct by construction, and correctly.** `make_component`
builds roots only as coordinate *differences* `(coords[j],coords[j+1])`, i.e.
`P_i-P_j`; `shifted_total` requires `sum(delta)=0` and `sum(c)=14`. An
`F`-type root has `F`-coefficient one, so subtracting it would move
`sum(c)` from 14 to 12 and drop the `F`-coefficient from 9 to 8 — the engine
**structurally cannot** absorb one. That is exactly right, because by §2–§3
the only `F`-type root is already inside `M_R`. Carriers enter only through
`carrier_representatives` (`J = O union three I-coordinates`, matching my
derivation in §4) and strict primes only through the degree multiset with
`d_j>=1`. Roots, carriers and strict primes are therefore disjoint by degree
and by class. **No code extension is needed.**

**Named finding (new).** I measured how much the typing lemma actually
carries, by appending a hypothetical extra strict prime of `A`-degree zero
and weight one to each cell and lowering the Euler cap by one:

```text
12 of 14 cells (both rank filters, 24 runs): pair matches 0, survivors 0
B3_tau0_distinct_residual, B3_tau0_split_residual:
  RuntimeError "only two- through four-prime q6 cells are registered"
  (join_candidates guard: require(2 <= count <= 4))
```

So (i) in twelve cells the repair is a typing clarification with no numerical
stake, and (ii) in the two `tau=0` four-prime cells the engine has **no
capacity** for a fifth prime and would abort fail-closed. It is therefore the
typing lemma of §1–§5, not the software, that covers those two cells. This
should be stated in the integration: the adjudication's "no code change is
needed" is correct, but for those two cells it is correct *because* the
lemma holds, not because the enumerator would have covered the object.

## 8. Re-adjudication of the earlier review's other corrections — `CONFIRMED`

**Root/block machinery is load-bearing — reproduced from scratch.** I wrote
an independent relaxed enumerator (class identities, adjunction parity and
`p_a>=0`, the weighted totals `sum w_j a_j = A0`, `sum w_j eps_j = 1`,
`sum w_j t_j = 1`, `sum_j w_j x_j = c`, and the pair rule; no
`connected_coordinate_blocks`, no `branch_differences`, no owner map, no
energy bound, no carrier filter). Over the positive-`a` slice:

```text
B3_tau_ne0_Delta_ne0              4
B3_tau_ne0_Delta0_doubled         2
B3_tau_ne0_Delta0_doubled_plus_Z  1
B3_tau0_odd_residual              4       total 11
```

— the prior review's eleven, cell for cell. **The adjudication's acceptance
of correction 2 is right.**

**But the constraints that remove those eleven are proved identities, not
heuristics.** I checked this rather than assuming it:

* For a root `E=P_p-P_q` and a strict prime `C`, `C.E = x_p - x_q`
  identically. `connected_coordinate_blocks` encodes exactly this (offsets
  `offset_{j+1}=offset_j-value_j`). Exact.
* `n = C_A m` is forced by `(r^*div p).E_i = 0` on the minimal resolution of a
  Gorenstein (Du Val) point, since `p=f_z` is a regular function. Exact.
* "At most one positive strict edge per component" and the single-owner rule
  are the rational-forest no-cycle condition: two roots of one chain met by
  one prime close a cycle through the chain; and two *different* strict
  primes meeting one chain close a cycle **because every strict prime passes
  through the connected `p_0` cluster** (§5). Exact — and note this couples
  §8 to §5: if a strict prime could avoid the cluster, the single-owner rule
  would need re-derivation.

I confirmed the shape by inspecting the four generic-`B3` relaxed matches:
each has all three primes carrying positive contact `(2,1,1)` with one
affine `A1` component, summing correctly to `n=4` but violating the
single-owner forest rule.

**Energy inequalities eliminate nothing.** `energy_pruning_applied=false` in
all 28 rows of the actual output. (4.1) and (4.2) are valid for `a>=0`
(`x^2>=x` only), and the reported minima all reproduce, but no executable
metadata row is pruned by them. Degree-one vertical candidates are covered by
the exact join alone. **The adjudication's acceptance of correction 3 is
right**, and the residual tension in v2 §4's closing sentence should be
resolved in the integration text.

**The `a=0` slice is independently root-machinery-free.** My relaxed
superset gives 361 admissible `a=0` metadata rows across the fourteen cells
and **zero** pair-condition matches in every one. It also independently
reproduces (1.3)/(3.1): the six cells `U3`, `U3+Z`, `odd`, `odd+Z`,
`doubled`, `doubled+Z` admit **no** `a=0` metadata at all, because a
weight-two prime cannot own the unit `eps` and every weight-one leg there has
degree four. (My per-cell *meta counts* differ from the prior review's, since
we count `(c,a,eps,t)` tuples differently; the decisive quantities — zero
matches, and which cells are empty — agree exactly.) **Correction 4 stands as
a genuine robustness result.**

---

## 9. Verdicts

| item | object | verdict |
|---|---|---|
| 1 | `A`,`B`,`r` geometry; `A+B=r^*O_X(1,1)` ample; projection formula; Du Val `(-2)` typing | `CONFIRMED` |
| 2 | Exhaustive root list `+/-(P_i-P_j)`, `+/-(F-P_i-P_j)`; `S0.(F-P_i-P_j)=1`; `F`-family only at the F5 tree | `CONFIRMED` |
| 3 | B3/U3 chronologies; `R1`,`E1` in `M_R`; double-count refused | `CONFIRMED` |
| 4 | `A.C=0,B.C>0` nonexceptional `=>` full `pi`-fibre, `B.C=1`, `Z_J`, `J=O union K`, `|K|=3`, coefficient `<=1` / none at `tau=0` | `CONFIRM_WITH_CORRECTIONS` (missing "affine target point" step; supplied in §4) |
| 5 | Positive-`A`-degree exhaustiveness; registered germs consume the same eight | `CONFIRMED` (localization proof supplied in §5) |
| 6 | Full independent q=6 local contact census; omission hunt | `CONFIRM_WITH_CORRECTIONS` (three scope sentences, §6.5) |
| 7 | v2 replay, `-O`/`-OO`, mutations; no code extension; type separation | `CONFIRMED` (with the fifth-prime capacity finding) |
| 8 | Root/block load-bearing; energy eliminates nothing; `a=0` slice robust | `CONFIRMED` |

**Overall: `CONFIRM_WITH_CORRECTIONS`.** The adjudication's central claim —
that the prior review's `A`-degree-zero gap is a type conflation and not an
omitted configuration — is correct, and I could not break it from any
direction. Its "no code change needed" disposition is correct. The
corrections are three missing scope sentences in the local audit, one missing
derivation step in the adjudication, and one honest statement about where the
enumerator would have been unable to help.

## 10. Maximum-safe theorem

> Fix the charged reduced normal-singular quadratic `q=6` F5 frame, i.e. the
> bidegree-`(2,3)` incidence `X subset P2 x P1` with `A=pi^*O(1)`,
> `B=rho^*O(1)`, `K_X=-A+B`, minimal Du Val resolution `r:Xtilde->X`, and the
> nine-blowup marking `S=S0`, `B=F`, `A=2S0+5F-sum P_i`,
> `T=S0+3F-sum_I P_i`, `|I|=6`. Assume the binding Euler/`A1`-ruling,
> rational-forest, and normal-F5 carrier/effectivity integrations, the marked
> `q=6` tag list `{B_3/A_2, U_3/A_3}`, and reduced infinity.
>
> **Typing.** Every irreducible curve on `Xtilde` falls into exactly one of
> three classes: (i) `A.C=B.C=0`, forcing `C` to be `r`-exceptional (because
> `A+B=r^*O_X(1,1)` is the pullback of an ample bundle) and hence a Du Val
> `(-2)`-root, necessarily of the form `+/-(P_i-P_j)` or `+/-(F-P_i-P_j)`,
> the latter only inside the unique F5 tree where it already occurs with
> multiplicity two in `M_R=A-H`; (ii) `A.C=0<B.C`, forcing `C` to be a full
> `pi`-fibre `{q} x P1` with `B.C=1`, `C^2=-3`, and, being disjoint from `H`,
> of class `Z_J=S0+2F-sum_J P_j` with `J=O union K`, `|K|=3`; (iii)
> `A.C>0`, a strict/nonexceptional prime. Since
> `A.C_str = C_str.(H+M_R) = 8` globally and
> `len C[[v,z]]/(h,h_z)=8` at `p_0` alone, every strict prime meets infinity
> only at the F5 cluster and its whole `A`-degree lies there. Hence the
> registered weighted local germs exhaust the strict primes, and **no
> `A`-degree-zero strict prime exists**.
>
> **Census.** The strict polar decomposition at the F5 cluster is one of the
> nine registered `(degree, Cartier weight, pair rule)` strata of total
> weighted `A`-degree eight — `U3/A3: 4+4`, `m=(2,2,1)`, `n=2e1+e2`;
> `B3/A2, tau!=0`: `4+2+2` or the `Delta=0` Weierstrass trichotomy,
> `m=(2,1)`, `n=3e1`; `B3/A2, tau=0`: `4+2` plus the `D0` residual
> trichotomy, `m=(2,2)`, `n=(2,2)` — with strict totals
> `(0,1,1,2,2,2,2,2,2)` for `U3` and `B3, tau!=0` (optionally minus one
> contracted carrier) and `(0,2,0,2,2,2,2,2,2)` for `B3, tau=0` (no carrier
> possible, in either outside orientation).
>
> **Enumeration.** Admitting every reduced strict prime with `B`-degree
> `a_j=F.C_j>=0`, including the three global vertical classes `F`, `F-P_o`,
> `F-P_i`, the necessary-lattice enumeration over all affine-ADE difference-
> root allocations within the Euler rank caps, together with the rank-zero
> controls, contains **no configuration satisfying the local pair conditions**
> in any of the 28 rows, **before** any carrier-forest or unlabelled-cycle
> filtering. Hence neither `U3/A3` nor any `B3/A2` modulus admits a necessary
> global boundary configuration in this fixed `q=6` frame.

This is a **necessary-lattice, fixed-presentation** theorem. It does not
prove the quadratic frame occurs; it is not coefficient realization,
effectivity, or attainment; it says nothing about nonquadratic incidences,
nonreduced infinity, nonfinite/projective-basepoint cases, degree drops, a
finite cubic algebra, a polynomial map, or JC2. `REPRESENTATIVE` is not
`FULL_ACTUAL_EXIT`; no exit price is asserted anywhere in this review.

**Scope gates that remain explicit and open:** (a) the binding tag list
`{B_3/A_2, U_3/A_3}` for `q=6`, which absorbs both the `tau=1` boundary
(`B_4/A_3`) and the corank-two cell `b(0)=c'(0)=0`; (b) the binding statement
that no ADE point lies on `H` away from `p_0`; (c) reduced infinity; (d) the
rational-forest theorem, on which the single-owner root rule and the
one-branch-per-prime licence both rest; (e) quadratic-frame existence and
minimization.

## 11. Exact dependencies

* Charged local contact audit `48717ce3...` (its own review gate is closed by
  §6 of this report, subject to the three corrections of §6.5).
* Charged typing adjudication `d2122d82...` (subject to the §4 correction).
* Binding integrations: normal-F5 carrier/effectivity `a5bf78c8...`,
  Euler/`A1`-ruling `f092a715...`, rational-forest `6a8558e4...`.
* `sum_j w_j d_j = 8` at the cluster and `A.C_str=8` globally, linked by
  `A=H+M_R` and the local length `len C[[v,z]]/(h,h_z)=8`.
* The forest one-branch-per-prime licence (audit §6) and the single-owner
  root rule (which additionally consumes §5 of this report).
* Hash-pinned finite software: v1 engine `b892cd15...`, v2 wrapper
  `c2ca2874...`.

## 12. Cheapest decisive successor

The prior review's successor ("decide whether the polar can have an
`A`-degree-zero component") is **discharged** by §1–§5 and needs no
computation. The cheapest decisive next step is therefore *not* more `q=6`
lattice work. It is a one-paragraph integration edit followed by a hard stop:

1. Fold the four corrections (§4 affine-target step; §6.5 items 1–3; §7
   fifth-prime capacity note) into the adjudication and the local audit, and
   promote the §10 theorem as the fixed-presentation `q=6` closure.
2. Stop all reduced finite normal-singular F5 `q=6` work.
3. Move the quadratic front to the scope escapes in the order of remaining
   force: **quadratic-frame existence/minimization first** — it is the only
   gate whose failure would make the entire `q=6`/`q=8` lattice program
   vacuous — then nonreduced infinity, then nonfinite/projective-basepoint
   cases, then degree drops.

If a single further `q=6` computation is wanted as insurance, the cheapest
one with any remaining power is to raise the engine's `join_candidates` arity
guard from `4` to `5` and rerun the two `tau=0` four-prime cells with a
spurious fifth prime, converting §7's fail-closed abort into a positive
`zero`. That is a three-line change and about four seconds of desk time, and
it would remove the last cell where the closure rests on the lemma alone.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `31680`.
- Body SHA-256:
  `43660b5d0516a875590aa98142c6edef2fc8b9b83db612289e1f648397db0a00`.
- Frozen basis: `2dc56cb6a4d21fbbbbf4b040a42ef6e88d7c4d66`.
