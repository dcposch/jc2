# Independent re-audit of the SHEET6-DEPTH root-meet claim

Date: 2026-08-28  
Auditor: GPT-5.6 Terra, independent read-only pass  
Scope: the 2026-08-12 chain-depth theorem under the 2026-08-28 root-scope
correction

## 0. Verdict

**The newly inserted root-scope supersession is FAIL AS FILED.** Its first
correction is right: corrected Proposition 8.4 is nonroot-only, root `M=1`
is allowed, and a genuine root merge is not Proposition 9.3 case (IV). Its
next inference is wrong: Proposition 9.3 case (I) independently recovers the
same strict numerical root window `w<1`.

More precisely:

1. A genuine merge at `(0,y)` has contact zero, hence `(0,y) in V_{2,a}`.
   Under the necessary `j>=1` convention for `V_{1,a}`, the root is not in
   `V_{1,a}`. Every incoming edge of such a root merge is therefore
   Proposition 9.3 **case (I)**, not case (IV).
2. Put `K_G=kappa_G(1-pi(G))`, `rho_G=D_G/P_G`,
   `w_G=(K_G-rho_G)/nu_G`, let `mu` be the arriving reduced multiplicity,
   and let `i=P_G/mu`. Case-I equations (c),(d), with the root data
   `(nu_F,K_F,D_F)=(1,1,l_f)`, give the exact identity

       X_F := D_F/i = mu(1-w_G).

   Hence every case-I root edge satisfies

       w_G = 1 - X_F/mu < 1.

   Equivalently, equation (d) first gives `K_G+n=nu_G`, so
   `K_G<nu_G`; positivity of `rho_G` already implies `w_G<1`.
3. On an all-`mu=1`, `r`-way root merge, MP6/MP7 give the reduced root
   pattern `(dp,dq)=(r,r+l)`, `k=0`, `l>=1`. Proposition 9.3(b) gives
   `X_F=dp/dq=r/(r+l)`, and therefore

       w_G = l/(r+l) in (0,1).                         (RM-I)

4. Thus the `td=6,m=2` depth result `W={2}` excludes every all-`M=1`
   root meet, including the omitted `l>=1` case-I family. No AWS census is
   needed for this analytic exclusion. This does **not** exclude the
   interior two-pole residue `(r,nu,l)=(2,3,1)`.
5. The all-`mu=1`, `l=1` root cell is nevertheless an exact local
   `Q`/reduced-ODE model with root `M=1`. It refutes any root extension of
   Proposition 8.4, but it has incoming `w=1/3`, not `w=2`, and so is not a
   countermodel to the corrected `td=6` reach exclusion.
6. The nonroot finite-`w` theorem survives. The sharp bound
   `d0=gen(W)+2` remains empirically verified but not proved in the filed
   argument; the reviewed safe theorem is `d0<=2*gen(W)+2`. At `td=6`,
   `gen(W)=0`, so both bounds are `2` and no conclusion changes.

The cleanest present boundary is therefore:

> At H1 tier, over the promoted MP anatomy, arbitrary-depth `M=1` segments
> have a finite computable `w` alphabet and a finite nonroot jump menu, with
> stabilization by the safe bound `2*gen(W)+2`. A genuine all-`M=1` root
> merge is case I and has `w=l/(r+l)<1`; hence its root layer is also finite,
> and the `td=6,m=2` root layer is empty because `W={2}`. Root `M=1` itself
> remains legal and locally realizable. This statement does not promote the
> independent multipole shared-budget claim, mixed-`mu`/off-axis packages,
> coefficient realizability, or the interior two-pole survivor.

## 1. Custody

The following are the exact bytes audited. Printed page numbers equal PDF
page numbers in the primary source.

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
ded3051d1a2009498f49bed20e5168d34b823518ab1b94ed340b380b37da6d15  ladder/SIGRAY-AUDIT.md
a08bf98e390bc38f60f216735577acb0650a9e9a86780b2fe2e69998fd06efb2  ladder/SHEET6-DEPTH.md
98199995f7d592007ff8155b355cf8eb5024305e9cdbd8fb92e102ed10929b91  ladder/SHEET6-DEPTH-REVIEW.md
7d75611eb2523171ccf4c7049b7d2fee115a1f8821eaa966d446ffac7c7d47c3  ladder/SHEET6-MULTIPOLE.md
d08eed7bbdf815489e383e4b08ead77f2ec51c50ba9173454f0d3dca9e66c3d4  ladder/SHEET6-MP-REVIEW.md
ca6245be6bd86359769f5d95a6b10dcfc1873f35a3daa45f7b70195de240c4d8  ladder/SHEET6-2POLE.md
8923208102c7286790d000c607ba44bddd7e482c693653aa73de36df93b94a00  ladder/BOOK-ENUM.md
26f0c64e8cb80ee6bac62e69f91d21dea74b01187150fbc786551f6885a35eb0  ladder/BOOK-OFFAXIS.md
5fc6b1634dc1ef0a0abe578411644fa166ffbfa16b8608cbce2a7b7b61465cd5  xmodel/sigray-later-m-package-source-audit-sol-ultra-20260828.md
fa25c8afe524a2bcecc305de50dc57831534a01e66614592a591acab393709f3  xmodel/sigray-section8-full-hostile-review-opus5-20260828.md
37b83208ddebb6e1242d341294d98f96116bad431c05a33ab43eaa147044d47e  xmodel/sigray-cyclic-semi-invariance-repair-sol-ultra-20260828.md
008a7e6949dbd84176515489c4bba4d9a61207ac675392c370bb98d32e7fb5ce  xmodel/sigray-cyclic-semi-invariance-repair-hostile-review-terra-20260828.md
70a72671ce1bc348902dcb60e3acf9cc5620b2dca4c24481a248906d203b135b  xmodel/sigray-cyclic-semi-invariance-repair-hostile-addendum-terra-20260828.md
a2b4d37c47deae18f25da7d1a687bf03243692953fa7e549c9198c479fe1c006  xmodel/sigray-cyclic-semi-invariance-repair-final-gate-terra-20260828.md
2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933  xmodel/sigray-section9-source-audit-sol-ultra-20260828.md
0729a5765729a9e3a6f99720a638cc94a3d3a7837e3946412e13c4233e6b5bad  xmodel/sigray-section9-source-audit-hostile-review-gpt55-20260828.md
e9245ec8d8b33d66a7f0c0365d891d15f8068894dc7e0e467d503556b4f3b255  xmodel/sigray-rootaware-engine-hostile-review-gpt55-20260828.md
93f98e4df5fd67536f3a5ab9c6f948a6bb06bbdbd10b825980596cc865c811d5  xmodel/sigray-rootaware-engine-cap-repair-terra-20260828.md
ee8a81a0a23437819be857e53f630d90fa0b793fc0666a2434d35b92c5d8013d  cases/depth_closure_check.py
0baf1d54328f0f9829126672536673af277068d4b6dda0221fd94b3c0994d212  cases/sigray_rootaware_smoke.py
b078c88424c566a8dd37c368e57e9e2aa8932f1bbde49d0c58580940eab806f3  cases/twopole_check.py
```

No canonical file was edited. No heavy census and no AWS job was run.

## 2. Root membership and the correct Proposition 9.3 case

Primary Sigray pp. 10--12 give the entire decision:

- Definition 3.2 includes the constant coefficient in contact order. Two
  distinct y-side series with different constants have `O(P,P*)=0`.
- Definition 3.3 identifies `(P,0)` and `(P*,0)` when `0<=O(P,P*)`.
- Definition 3.4 puts `I_P(O(P,P*))` in `V_{2,a}`.

For two characteristic paths whose first common vertex is `(0,y)`, their
contact is exactly zero. A genuine root merge is therefore not merely
*possibly* in `V_{2,a}`: it is in `V_{2,a}` by the tree definition.

The primary's technical `alpha_0=0` cannot put the root in `V_{1,a}`. The
necessary correction is `V_{1,a}` indexed by actual characteristic
exponents `j>=1`; otherwise Notation 3.4 asks for the undefined
`e_{-1}/e_0`. This is recorded at `ladder/SIGRAY-AUDIT.md:23`, proved and
explained at
`xmodel/sigray-section9-source-audit-sol-ultra-20260828.md:231-250`, and
hostile-confirmed at
`xmodel/sigray-section9-source-audit-hostile-review-gpt55-20260828.md:88`.

Thus a root merge has

```text
(0,y) in V_{2,a} \ V_{1,a},
```

so the exhaustive alternatives of Proposition 9.3 select case (I). Case
(IV) is reserved for a root outside `V_{1,a} union V_{2,a}` and cannot be
the classification of a genuine merge. `ladder/SHEET6-2POLE.md:83-89`
already states this correctly.

## 3. The case-I root handshake

Use Proposition 9.3's orientation: lower/rootward `F`, upper parent `G`,
`G=F+c`. Write

```text
P_G   = deg(p_G)                         (full degree)
rho_G = D_G/P_G
K_G   = kappa_G(1-pi(G))
w_G   = (K_G-rho_G)/nu_G
mu    = mult(p_F^red,c)
i     = P_G/mu
X_F   = D_F/i.
```

Case (I) uses equations (a)--(d), not (i)--(m). Equations (c),(d) are

```text
D_F = (D_G+n P_G)/nu_G,
K_F = (K_G+n)/nu_G,             n in N*.
```

At the root, Statement 9.2 gives `K_F=1`, so `K_G+n=nu_G`. Dividing (c)
by `i=P_G/mu` gives

```text
X_F = mu(rho_G+n)/nu_G
    = mu(nu_G-K_G+rho_G)/nu_G
    = mu(1-w_G).
```

Since `D_F=l_f>0` and `i>0`, this proves

```text
w_G = 1-X_F/mu < 1.                         (3.1)
```

This is stronger than merely retaining the necessary parent test
`K_G<nu_G`. It also shows exactly how the root cell factors through `w`.
For `mu=1`, (3.1) is the same handshake
`K_F-D_F/i=w_G` already proved for case-(I)/(II) edges in
`ladder/SHEET6-DEPTH.md:234-251`.

The campaign already contains the general case-I identity in
`ladder/BOOK-OFFAXIS.md:301-315`: its
`X_G=mu_e(kappa-bar_G-w_e)` specializes at root `kappa-bar_G=1` to (3.1).
The new DEPTH rollback overlooked its own promoted generalized handshake.

For all-`mu=1` root ancestry, MP6 forces `k=0` and MP7 gives

```text
(dp,dq)=(r,r+l),  l>=1.
```

Equation (b), together with (c),(d), says

```text
dp/dq = D_F/(i K_F) = X_F = r/(r+l).
```

Therefore

```text
w_G = 1-r/(r+l) = l/(r+l) in (0,1).          (3.2)
```

The old case-IV derivation remains valid for a non-`V_2` root endpoint.
Consequently the classification is not universal, but the strict numerical
condition `w<1` is: case I gives (3.1), while case IV gives the filed
`w=1-l_f/i_0<1` formula.

## 4. Consequences for `td=6` and the finite book

The nonroot depth calculation gives `W={2}` for each row-1 `M=1` ancestry
at `td=6,m=2`; see `ladder/SHEET6-DEPTH.md:218-223` and
`:357-363`. Every genuine root merge is case I and every incoming all-`mu=1`
edge must satisfy (3.2). Since `2` is not in `(0,1)`, no such root merge is
reachable. Equivalently, `w=2` and `rho>0` imply
`K_G=rho+2nu_G>nu_G`, directly failing the case-I equation-(d) test
`K_G<nu_G` recorded at `ladder/SHEET6-2POLE.md:244-247`.

Therefore:

- the old l-free phase-3 count remains invalid evidence;
- the corrected engine must retain `l>=1` and root `M=1` for general work;
- but an AWS root recensus is not needed to decide the `td=6` all-`M=1`
  root branch;
- the no-root conclusion does not touch the interior residue
  `Q=(6,12,3,2,5)`, which remains the distinguished two-pole survivor.

### Finite-book boundary

A book that literally omits possible root terminals is not exhaustive, so a
"full `BOOK(m,td)` without a root layer" is not proved. However, the root
layer at exactly the DEPTH theorem's all-`M=1` scope is easy to restore and
is finite without a depth cap. For fixed `r` and `w`, (3.2) gives at most
one value

```text
l = r w/(1-w),
```

subject to `l in N*`. Since `r<=m` and the depth theorem supplies a finite
`W`, the all-`mu=1` case-I root layer is finite. The independent root
top-degree pin `k_f=(r+l)l_f`, `psi=r+l-1`
(`ladder/SHEET6-MULTIPOLE.md:138-143`) also gives the usual singleton
Statement-9.4 bound when that budget is invoked, but it is not needed for
finiteness.

Accordingly:

- **proved at the reviewed DEPTH/H1 scope:** finite root-inclusive
  all-`M=1` pattern book, using (3.2) and the safe depth bound;
- **not proved merely by deleting roots:** an exhaustive full book;
- **not promoted by this audit:** mixed-`mu`/off-axis completeness, global
  cross-chain first-exit budget, coefficient/Puiseux realizability, or a
  full JC2 exclusion.

`ladder/BOOK-ENUM.md:19-23,39,50-58` reaches the correct no-root verdict in
its swept panels but labels the necessary window as case IV. Its root kill
can be retained after relabeling it by the case-I identity above.

## 5. The `r=2,l=1` local root cell

Let `a!=b`,

```text
p(eta)=(eta-a)(eta-b),
s(eta)=eta-(a+b)/2,
q(eta)=p(eta)s(eta).
```

Then

```text
2 p s' - p' s = -(a-b)^2/2 != 0.
```

With root slope `delta=dp/dq=2/3`, the reduced identity becomes

```text
delta p q' - p' q = -(a-b)^2 p/6,
```

which is exactly a nonzero scalar multiple of `p`. Thus `(dp,dq)=(2,3)`
is locally ODE-solvable and `M_root=gcd(2,3)=1`.

There is also an exact absolute `Q`-level scaling. Take each synthetic
incoming parent to have

```text
(D_G,P_G,nu_G,M_G,K_G)=(3,3,3,1,2),  mu=1, n=1.
```

Then `rho_G=1`, `w_G=1/3`, and equations (c),(d) give the root

```text
(D_F,P_F,nu_F,M_F,K_F)=(2,6,1,1,1),
```

with `P_F=i*dp=3*2=6` and `P_F=(r+l)D_F=3*2`. This is a concrete local
countermodel to the old root-`M=1` kill. It is not an actual Keller map and
not a `td=6` row-1 reach model: those chains have `w=2`, not `1/3`.

## 6. Exactly what survives from SHEET6-DEPTH

The following nonroot claims survive unchanged at their stated trust tier:

1. DS1 characteristic rigidity for depth-at-least-one `M=1` segment
   vertices, including `nu>=2`, `V_1` membership, and case-II consecutive
   characteristic edges. The separately flagged entry-edge H1 caveat
   remains.
2. DS2's exact step law
   `w_child=w_parent*n/((n-1)nu+1)`; neutral `n=1` steps conserve `w`, and
   resonant steps contract by at most `2/3`.
3. DS3's divisibility `Delta|num(w)`, finite resonance count, and finite
   computable closure `W(w_0)`.
4. DS4's nonroot all-`mu=1` handshake, join-through-`w` factorization,
   finite cell menu per `(w,r)`, and the corrected case-III ZCH 0-edge
   constraint.
5. Eventual menu stabilization with the **proved safe** bound
   `d0<=2*gen(W)+2`. The sharper `gen(W)+2` bound remains a cap-tested
   conjectural sharpening because the replay proof can require neutral
   steps between resonant steps; see
   `ladder/SHEET6-DEPTH-REVIEW.md:194-229,306-313`.
6. The exact `td=6,m=2` nonroot result `W={2}`, `gen=0`, `d0=2`, and the
   unique corrected pre-suffix IIa cell `(r,nu,l)=(2,3,1)` with child
   `(K,D/i,rho)=(5,3,1/2)`.

What does not survive is only the *case label* used in the root proof and
any use of corrected Proposition 8.4 to kill root `M=1`. The root numerical
window and the `td=6` root exclusion do survive by the case-I derivation.

## 7. Exact file findings and minimum repair map

### `ladder/SHEET6-DEPTH.md`

- `:7-18`: **FAIL AS FILED.** Keep the Proposition-8.4 scope, contact-zero,
  engine-cap, and budget statements. Replace `:11-15` by the case-I identity
  `X=mu(1-w)` and restore the `td=6` no-root conclusion.
- `:27-28`: historical text calls the root-merge edge case IV. Mark that
  specific historical claim false; a genuine merge is case I.
- `:60-62,335-355,401-406`: replace the unproved sharp `gen+2` proof claim
  by the safe `2*gen+2` bound, retaining sharp `gen+2` as tested.
- `:67-69`, `:297-316`, `:364-365`, `:397-414`, `:421-423`: the case-I
  rollback is overbroad. Insert (3.1)--(3.2); restore the finite all-`M=1`
  root layer and the `td=6` empty-root result.

### `ladder/SHEET6-DEPTH-REVIEW.md`

- `:3-10`, `:52-54`, `:290-304`, `:319-326`: **FAIL AS FILED** for saying
  case I lacks `w<1` and for withdrawing the `td=6` root result. The review's
  own confirmed case-I handshake at `:91-96,159-170` supplies the repair.
- `:44-47,194-229,306-313`: **PASS** and preserve the safe stabilization
  correction.

### MP and two-pole consumers

- `ladder/SHEET6-2POLE.md:83-89,244-247`: **PASS**; these already say a root
  merge is case I and derive `K_parent<nu_parent`.
- `ladder/SHEET6-2POLE.md:3-14,27-34,298-304`: the AWS-pending/no-root
  withdrawal is unnecessary after combining the preceding case-I test with
  `W={2}`.
- `ladder/SHEET6-2POLE.md:258-262`: historical l-free ratio rigidity is
  false, as its supersession recognizes; do not restore it.
- `ladder/SHEET6-MULTIPOLE.md:100-104,153-158`: parent reach is right; replace
  the pending `td=6` census disposition by the exact `W={2}` exclusion.
- `ladder/SHEET6-MULTIPOLE.md:140-143,158`: **PASS** for the root top pin and
  the exact `l=1` local ODE cell.
- `ladder/SHEET6-MP-REVIEW.md:145-171`: retain the diagnosis of the old cap
  failure, but its bounded-search uncertainty is resolved analytically by
  the depth invariant plus case-I equation (d).

### Section 8 boundary

- Corrected nonroot Proposition 8.4 remains proved; no root clause is
  restored. See
  `xmodel/sigray-section8-full-hostile-review-opus5-20260828.md:227-285`.
- Statement 8.4 edge divisibility is root-independent
  (`ibid.:117-139`) and still gives `mu|M_parent`.
- Statement 8.5's cyclic gap is closed by the promoted cyclic repair
  (`xmodel/sigray-cyclic-semi-invariance-repair-sol-ultra-20260828.md:102-189`)
  and its hostile/final gates. None of that implies root `M!=1`.

## 8. Light exact checks

Only local pure-Python checks were run; total wall time was 4.2 seconds.

```text
$ python3 cases/sigray_rootaware_smoke.py
PASS disposition root/NR/pole certificates
PASS sheet6_campaign.bash root-before-M filter
PASS mu=1 single-orbit and mu=2 case-I root emission
PASS unbounded MU1 l=98 and mandatory zero-charge cap residues
PASS twopole suffix root-before-M filter
PASS h3 and hiii BFS root-before-M filters
PASS twopole l>=1 menu, ODE parity, parent reach, and l=1 emission
PASS static no raw child.M==1 BFS shortcuts
ROOT-AWARE SMOKE PASS: 8 checks

$ python3 cases/depth_closure_check.py
PASS reached w-set == {2} (got [Fraction(2, 1)])
PASS no resonant (l>=1) chain step admissible anywhere (Delta|2 empty)
PASS arithmetic closure W(2) == {2}, gen 0
PASS cumulative jump menu constant for all depths 1..12
PASS td=6 corrected jump menu == {IIa (2,3,1) M=2}
ALL CHECKS PASS

$ python3 <inline exact Fraction gate>
PASS exact case-I root handshake: w=1/3, absolute Q scaling,
     l=1 ODE constant=-2
```

The root-aware engine's `l=98` single-chain MU1 witness is a separate
completeness regression. It does not alter the `r=2` all-`mu=1` root-merge
formula or the `td=6` `W={2}` argument.

## 9. Final classification

```text
Root Proposition 8.4 rollback:                     PASS
Root merge in V2 by contact zero:                  PASS; mandatory for a genuine merge
Root merge classified as Prop. 9.3 IV:             FAIL
Root merge classified as Prop. 9.3 I:              PASS
Case-I root identity X=mu(1-w):                    PASS
Universal numerical root condition w<1:            PASS, by case-specific derivations
All-mu=1 formula w=l/(r+l):                        PASS
td=6,m=2 root-meet exclusion from W={2}:           PASS
Old l-free/capped engine as evidence:              FAIL
r=2,l=1 root M=1 local Q/ODE cell:                 PASS
r=2,l=1 cell as a global Keller counterexample:    NOT CLAIMED
Nonroot finite W and finite menu:                   PASS
Sharp d0=gen(W)+2 proof:                           INCOMPLETE
Safe d0<=2*gen(W)+2:                               PASS
Root-deleted book as exhaustive BOOK(m,td):         FAIL
All-M=1 root-inclusive finite pattern layer:        PASS at DEPTH/H1 tier
Full campaign-wide BOOK / global shared budget:     NOT PROMOTED HERE
New DEPTH/DEPTH-REVIEW supersession:                FAIL AS FILED
```
