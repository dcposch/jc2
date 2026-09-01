# Hostile review: ONE-CUSP-A2 r2

## 1. Scope, integrity, and verdict scale

All four frozen inputs were hashed before mathematical inspection. The computed
SHA-256 values were, in the charged order,
`5f28c56396aa809ff040f294a03cede7898ee6396160add14fceff93fce32fa4`,
`4009c3abdc16e972aec121206664a21adc81ff8467dfe8d5a0f561e90f3a86d5`,
`26079008ffeba9b94ecfcc79c63690cc232f7f50f655d477835dc26b80f59cd3`, and
`763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9`;
all match. I used only the frozen copies in the charged `inputs` directory and
desk-scale polynomial algebra: no CAS, literature, canonical ledger, charged
file, or `jc2-lean` was used or changed.

Verdicts below are `PROMOTE`, `PROMOTE AFTER REPAIR` (the proof survives a
stated correction), `OPEN` (no safe conclusion), and `REJECT`. Citations of the
form `r2:L-M`, `theta:L-M`, `prior:L-M`, and `integration:L-M` refer respectively
to the four charged basenames in the order listed by the request. Default
refutation was applied claim by claim. No exit-price assertion or declaration
is made.

## 2. Propositions 2.1–2.3: the \((T,V)\) chart

**Verdict: PROMOTE AFTER REPAIR.** The chart and filtration dictionary are
correct, but Proposition 2.1 asserts rather than proves irreducibility
(`r2:81-90`). The missing proof is short: in
`C[A,U][Z]`, the coefficients of the primitive linear polynomial
`-A^2Z+(U^2-A)` are coprime; Gauss's lemma therefore makes it irreducible.
This also supplies the domain/nonzerodivisor premise needed for localization.

With `T=A^{-1}` and `V=U/A`, the relation gives
`Z=V^2-T`, and the displayed forward and inverse generator images prove
`RR[A^{-1}]=C[T^{±1},V]` (`r2:81-90`). Direct differentiation gives
`{T,U}=-2`, hence `{V,T}=2T` and

```text
{F,G}=2T(F_V G_T-F_T G_V).
```

This returns `{A,U}=2A^2` and
`{U,Z}=4V^2/T-2=2+4AZ`, so both advertised generator controls are exact
(`r2:92-104`) and agree with the independently reviewed bracket
(`theta:51-79`; `prior:24-68`).

For `P=Σ C_i(Z)A^i`, substitution gives
`C_i(V^2-T)T^{-i}` with lowest term `C_i(V^2)T^{-i}`; for `UQ` it gives the
odd lowest term `V D_j(V^2)T^{-j-1}`. Even and odd terms cannot cancel. Thus
the equivalence in Proposition 2.3, including the oddness condition at pole
order `d+1`, is exact (`r2:116-137`). Add the conventions
`v(0)=+∞`, `deg_A(0)=-∞`; without them two displayed universal equalities are
literally undefined on zero components. Also retain the parity clause: the
coefficientwise `A`-degree filtration is not *just* a pole bound.

The place audit passes. The report explicitly distinguishes `{T=0}` from the
interior line `Phi` (which is approached at `T=∞`), the target place, and the
cover factor (`r2:139-151`). No flag, physical place, or series is merged.

## 3. Theorem 3.2: formal unobstructedness along \(\Phi\)

**Verdict: PROMOTE AFTER REPAIR.** The existence/surjectivity theorem is
correct. Its freedom statement should say **two** independent `C[Z]`
parameters at every positive `A`-level, not the singular, ambiguous “a free
`C[Z]` at each level” (`r2:195-219,526-530`).

Write `∂p=p_Z`, `∂r=r_Z`; this renaming is mandatory because `r2:110` first
defines a prime as `d/dV` and §3 silently reuses primes for `d/dZ`. Direct
coefficient collection in the reviewed formulas gives, for `n>=1`,

```text
O_n=4(n+1)(C_(n+1)∂r-∂p E_(n+1))+M_n,
E_n=(4n+2)(D_n∂r-∂p L_n)
    +2(2n C_n s_Z-C_(n,Z)s)+2(q E_(n,Z)-2n q_Z E_n)+Λ_n,
```

where `M_n` contains no even coefficient above level `n` and no odd one above
level `n`, while `Λ_n` contains only levels below `n` apart from the displayed
terms. These support statements follow term-by-term from the shifts contributed
by `A^2`, `H=A+A^2Z`, and `c=2+4AZ`; they agree with `r2:158-186` and with the
previously checked low-level expansion (`prior:244-258`).

The restriction `n>=1` is a necessary repair to `r2:174-176`: at `n=0` the
display counts the unique residue term twice and gives
`4(q∂r-∂p s)` instead of the actual `2(q∂r-∂p s)`. The proof handles
`E_0=kappa` separately and only invokes this formula at positive `n`, so the
recursion survives.

Here is exactly where coprimality enters. If
`gcd(∂p,∂r)=1`, choose `a,b in C[Z]` with `a∂r+b∂p=1`. For any `W`,
`(X,Y)=(aW,-bW)` solves `X∂r-∂pY=W`. Conversely coprimality in the PID
`C[Z]` makes the kernel exactly
`(X,Y)=(∂p tau,∂r tau)`, `tau in C[Z]`. This proves both surjectivity and the one-parameter kernel
of each individual Bezout equation (`r2:188-193`; the minimal family supplies
the premise at `theta:225-246`).

Coprimality is actually redundant in the theorem: the residue equation itself
supplies `(2q/kappa)∂r+(-2s/kappa)∂p=1`. It is the algebraic mechanism used by
the recursion, not an additional dependence on companion immersivity.

Starting from fixed `(p,q,r,s)` satisfying
`2(q∂r-∂p s)=kappa`, solve `O_0` for `(C_1,E_1)`, then `E_1` for
`(D_1,L_1)`, then `O_1` for `(C_2,E_2)`, and so on. The nonzero scalar factors
are invertible in characteristic zero. Every earlier kernel choice merely
enters the next known remainder; surjectivity of the new pair absorbs it, so no
later equation takes an old choice back. For fixed residue data the solution
set is therefore a noncanonical inverse-limit affine torsor with one kernel
parameter for `(C_m,E_m)` and one for `(D_m,L_m)` for each `m>=1`.

Finally, the completion notation is legitimate: for `I=(A,U)`, the relation
implies `I^2=(A)`, so the `I`-adic and `A`-adic topologies are equivalent and
the completion is
`C[Z][[A]] ⊕ U C[Z][[A]]`. Thus the proof establishes unrestricted formal
lifts, not finite polynomial termination.

## 4. Corollary 3.3: the claimed impossibility of bottom-up obstruction

**Verdict: REJECT AS STATED; PROMOTE ONLY THE REPLACEMENT BELOW.** Theorem 3.2
proves surjectivity of unrestricted finite-jet truncation maps. It does not
prove a negative theorem about every possible “bottom-up induction”
(`r2:221-237,531-536`).

There are immediate counterexamples to the wording. In the `A`-degree-zero
class, bottom-up coefficient comparison gives `[A^0]E=kappa` and then the
uncancellable `[A^1]E=2kappa Z`, proving emptiness (`theta:325-344`). In the
`A`-linear class the same procedure obstructs precisely because termination
sets the next Bezout compensator `(C_2,E_2)` to zero (`prior:244-258`). Most
sharply, Lemma 4.1 starts at the bottom and proves that every recursively forced
`L_n` is nonzero; that is a bottom-up proof of nontermination.

What is safe is:

> For residue data satisfying the first-jet equation, every finite jet of the
> unrestricted formal system extends through the next odd and even equations;
> the extension fiber is a noncanonical `C[Z]^2`. Hence there is no
> finite-order **formal-lifting** obstruction. A finite polynomial solution may
> still fail because the resulting recursion cannot terminate.

The reinterpretation of the two earlier bounded obstructions as termination
statements is therefore sound. “No bottom-up induction can ever obstruct,”
“never the bottom,” and analogous strategy-wide negatives must not be
promoted.

## 5. Lemma 4.1: polynomial mates

**Verdict: PROMOTE.** Let `f=phi(Z)` and `g=R_0+US_0`. The odd equation is
`O=-4phi_Z(R_0)_A`. If `phi_Z=0`, the bracket vanishes; otherwise the domain
property forces `R_0=r(Z)`. The even equation then is

```text
-phi_Z(4H(S_0)_A+cS_0)=kappa.
```

Since the product is a nonzero unit in `C[A,Z]`, `phi_Z` is a nonzero constant
and the second factor is constant. For `S_0=ΣL_nA^n`, its coefficients are

```text
(4n+2)L_n+4nZL_(n-1).
```

Thus `L_0=-kappa/(2phi_Z)` and
`L_n=-(2nZ/(2n+1))L_(n-1)` for every `n>=1`. All are nonzero, so a polynomial
`S_0` cannot terminate (`r2:270-285`). This proves exactly that no
`g in RR`, of any finite `A`-degree, is a mate. It does not exclude a formal
mate—the displayed recurrence constructs one—and therefore dovetails with,
rather than contradicts, Theorem 3.2.

## 6. Proposition 4.2 and §5: affine reduction and cell eliminations

**Verdict: PROMOTE AFTER A ONE-LINE REPAIR.** For any solution, Lemma 4.1 and
Proposition 2.3 give
`1<=alpha,beta<=3`. After swapping coordinates, if `alpha=beta`, the leading
Wronskian equation makes the two leading coefficients constant multiples;
subtracting that multiple strictly lowers one pole order. The lowered
coordinate cannot reach valuation `>=0`, again by Lemma 4.1. One affine step
therefore gives exactly
`(alpha,beta) in {(3,2),(3,1),(2,1)}` (`r2:295-319`). The affine target action
preserves the coefficient cap and multiplies `kappa` by its nonzero determinant.

For `beta=1`, coefficientwise parity forces
`E_2=L_1=L_2=0` and `g_-1=E_1(V^2)+VL_0(V^2)` (`r2:321-329`). In cell `(3,1)`,
the leading equation gives `f_-3=c k^3`, `k=g_-1`; oddness of `f_-3` forces
`k` odd and hence `E_1=0`. Thus `g=r(Z)+Us(Z)`, and both `g^2` and `g^3` stay
inside the `A`-degree-two class. The next Laurent coefficient integrates to

```text
f_-2=k^2(3c g_0+c_3),
```

so `f-cg^3-c_3g^2` has pole order at most one (`r2:331-365`). Equal-order
affine cancellation then lands in `C[Z]`, contradicting Lemma 4.1. The source
only spells out the descended valuation `-1` case; add that if it is already
`>=0`, Proposition 2.3 and Lemma 4.1 apply immediately.

In cell `(2,1)`, the leading equation instead gives `f_-2=c_0g_-1^2`.
Here `g=(r+AE_1)+Us`, and direct squaring shows its even part has `A`-degree at
most two and odd part at most one. Hence `f-c_0g^2` again has pole order at most
one and the same two-case descent ends at Lemma 4.1 (`r2:367-383`).

The subtractions by `g^2` or `g^3` are triangular polynomial target
automorphisms, not elements of `Aff_2`; the report mostly keeps this distinction
(`r2:385-394`), and it should remain explicit in promotion. Both eliminations
are unconditional: neither uses a residue normal form, `T_0`, the companion
curve, nor any boundary/exit datum.

## 7. §6: rigidification of cell \((3,2)\)

**Verdict: REJECT AS PRINTED; PROMOTE A CORRECTED, STRONGER
RIGIDIFICATION.** The leading-form work is sound. With nonzero constants
`a=c_1`, `b=c_2`, one gets

```text
S_0=s,  E_2=bZ eta^2,  D_2=aZ eta^3,
2bC_2=Z eta(3as+c_5 eta).
```

The first line follows from the odd common factor `h=Veta(V^2)`; the last is
the complete polynomial solution of `[A^3]O=0` (`r2:401-452`). Also,
`[A^5]E` vanishes after this substitution.

The next calculation is wrong. Writing every prime here explicitly as
`d/dZ`, direct collection gives

```text
[A^4]E = -2D_2E_1-4D_1E_2+10D_2E_2'-8D_2'E_2
          +Z(8D_1E_2'+12D_2E_1'-8D_1'E_2-4D_2'E_1).
```

Put `F=D_1-D_2'`, `G=E_1-E_2'`. Substitution of the leading forms reduces
this to `2 Z eta` times

```text
3a eta(2Z G'eta-G eta-2Z G eta')
-2b(2Z F'eta-F eta-4Z F eta').
```

The printed (6.4) instead has `-3Feta-8ZFeta'` (`r2:454-462`). For a concrete
refuter, take `a=b=eta=G=1`, `F=3/2`; equivalently
`D_2=E_2=Z`, `D_1=5/2`, `E_1=2`. The direct coefficient above is zero, whereas
the two sides of printed (6.4) are `-3` and `-9`.

There is a clean exact repair. Set `K=2bF-3a eta G`. The corrected equation is

```text
2Z eta K'-eta K-4Z eta'K=0.
```

If nonzero `K` and `eta` have degrees `k` and `e`, its top coefficient is
multiplied by the odd integer `2k-1-4e`, impossible. Hence `K=0`, i.e.

```text
2c_2(D_1-D_2')=3c_1 eta(E_1-E_2').
```

Thus printed Proposition 6.1 analyzes its displayed equation correctly but does
not describe the actual cell; its leading-coefficient formula (`r2:464-477`)
cannot be promoted downstream. Only its coarse degree dichotomy happens also to
follow from the corrected, stronger identity.

Consequently “eight polynomials/seven equations” (`r2:484-505,647-653`) is
also false. One may retain eight polynomials and eight identities, including
the corrected `[A^4]E`; better, eliminate `D_1` and use the seven free
polynomials
`eta,s,C_0,C_1,D_0,E_0,G`, with
`E_1=E_2'+G` and
`D_1=D_2'+(3a/(2b))eta G`, against the seven lower identities listed at
`r2:494-496`. This is the safe successor model.

It is not yet a unique gauge: rescaling `eta` can be absorbed into
`(c_1,c_2,c_5)`, and the residual affine shear `f -> f+lambda g` sends
`c_5` to `c_5+2lambda c_2^2`, so `c_5` may be normalized to zero. These
redundancies do not alter the corrected equations but further undercut the word
“rigid” if it is meant uniquely rather than structurally.

## 8. §8: AWS/CAS specification audit

**Verdict: REJECT SPEC-1 and SPEC-2 pending rewrite. PROMOTE only the
evidence semantics.** No CAS was run. The following are desk-detectable faults.

1. **Wrong and missing equation.** SPEC-1 item 4 asks the engine to certify the
   false printed (6.4) (`r2:588-590`). The true coefficient has the nonconstant
   factor `2 Z eta` and the corrected bracket displayed in §7 above. Moreover,
   Proposition 6.1 never solved (6.4), but the SPEC-2 ideal omits all
   coefficients of `[A^4]E` (`r2:610-612`). Thus “decide cell” describes a
   relaxation: `NONEMPTY` can be spurious. Use the corrected seven-polynomial
   parametrization, or retain eight polynomials and add every coefficient of
   the eighth identity.

2. **Reserved/colliding identifiers and differentiation order.** In
   `r2:568-573`, `Q` denotes both the rational base and an unknown polynomial,
   while indexed `c(i,k)` collides with `c=2+4AZ`; function-style generator
   names are not portable, and names such as `I` or `E` are protected in some
   engines. No CAS, version, or differentiation signature is named. Use safe
   ASCII prefixes such as `cc_i_k`, call the structural factor `chi`, and define
   wrappers `dA(h)`, `dZ(h)`. Before building equations assert
   `dA(A)=dZ(Z)=1` and `dA(Z)=dZ(A)=0`. Never pass an ambiguous prime mark.

3. **Tower-ring/map bug.** `Q[parameters][A,Z]` (`r2:568-569`) and the
   parameter-only ideal ring (`r2:610-612`) are different rings. Declare the
   coefficient field, complete ordered generator lists and monomial/block
   orders, then declare and test the coefficient-extraction/flattening map.
   Every extracted `A`- and `Z`-coefficient must land in the parameter ring;
   leaving `Z` behind tests vanishing at a point, not a polynomial identity.
   Rebuild specialized `P,Q,R_0,S_0` in the target ring—alias replacement and
   matching names are not a ring map.

4. **Degree-list and vanished-leader bugs.** The SPEC-1 cap `k<=8` cannot hold
   `D_2=c_1 Z eta^3` when `deg eta=3`, whose degree can be ten
   (`r2:568,583-587`). “`deg_A<=2`” must actually zero every higher template
   level. Extract coefficients by explicit exponent, assert reconstruction,
   use partial rather than total degree, and define `deg(0)=-infinity`.
   In SPEC-2, `s` is called degree `sig`, but only `eta_e` is saturated
   (`r2:598-615`); so `sig` is merely a cap unless its leader is separately
   required nonzero. Any `F,G` degree branch likewise needs zero branches and
   explicit leaders. Do not zip sparse coefficient arrays against an assumed
   consecutive degree list.

5. **Denominators and saturation.** `Cb_2` is not declared as either an alias
   or a variable with a defining relation (`r2:607-608`). The safest model keeps
   a coefficient vector for `C_2` and adds the coefficients of
   `2c_2 C_2-Z eta(3c_1s+c_5eta)`. The instruction to extract the ideal component
   returned by `sat()`, reject batch errors, and check its ring is directionally
   correct (`r2:614-618`), but also verify field, order, map images, and the unit
   ideal by exact normal-form reduction of `1`, not object/string equality.

6. **Controls.** The `(3,1)` negative-control idea is sound but under-specified:
   encode the complete specialized system through its actual top `A`
   coefficient and enforce `c'`, `kappa`, and `s` nonzero, with leader charts
   if `s` has only a degree cap (`r2:625-629`). The positive control is invalid.
   Theorem 3.2 supplies an infinite formal series, not a degree-three polynomial,
   a fixed-`N` solution, or one retaining the terminal `(3,2)` relations
   (`r2:630-633`). A valid finite-jet control, independent of those relations,
   is

   ```text
   kappa=2,  f=Z,
   g=U(-1+(2/3)AZ-(8/15)A^2Z^2+(16/35)A^3Z^3).
   ```

   It has `O=0` and `E=2 mod A^4` by the Lemma 4.1 recurrence. Test only the
   corresponding finite-jet equations and verify the witness directly.

The final reading at `r2:635-640` is correct: after a faithful exact encoding,
unit ideal is a theorem only for that finite degree box and merely evidence for
the unbounded claim; a proper ideal is a candidate source whose saturation
factor and original `E,O` identities require exact witness postcheck. This
matches the absence of any degree cap (`theta:124-128,405-410`) and the
coordinator's `NONEMPTY`-postcheck rule (`integration:89-90`).
Such a witness is not yet specifically “degree 8”: that label additionally
uses the unencoded condition `[K:C(f,g)]=4` (`theta:431-440`). Until that field
degree is checked, report only a constant-bracket/counterexample candidate.

## 9. Fallacy-v2 audit and promotion recommendations

The bundle **fails promotion as a whole** because Corollary 3.3 is overstated,
(6.4) is false, the residual equation count is wrong, and the proposed CAS
ideal omits that equation. The valid parts have the following individual gate:

| Item | Recommendation | Binding scope or repair |
|---|---|---|
| Proposition 2.1 | PROMOTE AFTER REPAIR | Add irreducibility and inverse-map proof. |
| Proposition 2.2 | PROMOTE | Bracket and generator checks are exact. |
| Proposition 2.3 | PROMOTE AFTER REPAIR | Add zero conventions; always retain leading parity. |
| Theorem 3.2 | PROMOTE AFTER REPAIR | Put `n>=1` on (3.2), remove redundant gcd premise, and state two freedoms per positive level. |
| Corollary 3.3 | REJECT AS STATED | Promote only “no finite-order unrestricted formal-lifting obstruction.” |
| Lemma 4.1 | PROMOTE | Polynomial mates are excluded at every finite `A`-degree. |
| Proposition 4.2 | PROMOTE | The three-cell affine census is exhaustive. |
| Cells `(3,1)`, `(2,1)` | PROMOTE AFTER MINOR REPAIR | Add the already-nonnegative valuation branch; kills remain unconditional. |
| §6 through (6.3) | PROMOTE | Leading forms and `C_2` integration are exact. |
| Printed (6.4), Proposition 6.1 | REJECT FOR THE CELL | Wrong coefficients; replace by `2c_2 F=3c_1 eta G`. |
| “8 polynomials/7 equations” | REJECT | Correct model is 8/8 or, after elimination, 7/7. |
| SPEC-1 / SPEC-2 | REJECT PENDING REWRITE | False identity, omitted constraint, and unsafe ring/degree mechanics. |
| Positive-control claim | REJECT AND REPLACE | Use the explicit finite jet in §8, outside terminal cell constraints. |
| Finite-box `EMPTY` reading | PROMOTE | Exact only inside a faithful box; evidence only globally. |

FALLACY-v2 passes on flag/place/series separation, pole/interior scoping,
floor-versus-attainment, and the absence of any exit charge. Carrier,
per-ray charging, merge-free descent, and target-arrival indexing are not used.
It fails as written on prime/derivative disambiguation and variable/ring maps;
the proposed `sat()` wrapping is only partial, and the degree implementation
does not branch safely on vanished leaders. The repairs in §§3, 7, and 8 are
the safe replacements. No conclusion here selects a partition row, asserts an
exit price, or upgrades finite-box evidence to unbounded attainment.

<!-- BODY-END -->
