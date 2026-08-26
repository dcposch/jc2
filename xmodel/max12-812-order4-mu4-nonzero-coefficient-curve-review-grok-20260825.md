# Hostile review — `(8,12)` order-four `mu_4 != 0` normalized coefficient-curve client

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-client-20260825.md` |
| Target SHA-256 | `2a7c5b6e09818d523954f8896a339d5f31407650b1777dd83f7a5bbbe5eda4fa` |
| Compiler | `cases/max12_812_order4_mu4_nonzero_curve_20260825/compile_curve.py` |
| Compiler SHA-256 | `5c1add225079ff56454654bcbb893326bc95dc34cf5c3f763aa58a0ef012b8de` |
| Overall verdict | **REPAIR** |
| Smallest failing identity | the three printed parent SHA-256 values in target §1 |
| Smallest missing hypothesis | none that breaks a numbered mathematical claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Charged reviews were opened only to recompute their hashes and to read identities written in the named source files; no producer status line and no charged `CONFIRMED`/`REPAIR` string is evidence |
| Method | source reading and hand derivation only; SHA-256 of the target, compiler, freeze list, named parents, shared Faber source, and AWS wrappers; no CAS, solver, substantive exact Python, Sage, Singular, msolve, or Lean |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `4fe628a133ae62e16b1bec5e4ed6fcee420dd880` (named producer, compiler, and freeze uncommitted) |
| Date | 2026-08-25 |

Independently recomputed SHA-256 of the target is `2a7c5b6e09818d523954f8896a339d5f31407650b1777dd83f7a5bbbe5eda4fa`, matching the launch pin and `FREEZE.sha256`. Independently recomputed SHA-256 of the compiler is `5c1add225079ff56454654bcbb893326bc95dc34cf5c3f763aa58a0ef012b8de`, likewise matching. Producer verdict language, the target's own status line, and every charged review's overall token were not used as evidence. Live AWS outputs under `cases/max12_812_order4_mu4_nonzero_curve_20260825/aws_compile_box02_20260826T000001Z/` were not opened and are not evidence. No file other than this review was written.

---

## Verdict

The mathematical specification is correct as a coefficient-infinity necessary-condition client, and the AWS-only compiler source-reads as an honest implementation of that specification. Independently, from the stated tail convention alone: `g=w^{12}-E` and `f^3=w^{24}` give `g^2-f^3=-2w^{12}E+E^2`; `E^2` is `O(w^{-2})` before any specialization and `O(w^{-8})` on the exact-order-four leaf, so it cannot contaminate a nonnegative `w`- or `z`-degree; substituting `(r_1,\ldots,r_7)=(0,0,0,mu_4,0,0,R_7)` produces `g^2-f^3+2mu_4 f=-2R_7 w^5+O(w^4)=-2R_7 z^5+O(z^4)` with `[z^5]=-2R_7`. The six unsaturated generators `(r_1,r_2,r_3,r_4-1,r_5,r_6)` and `([z^{11}]V,\ldots,[z^6]V)` for `V=g^2-f^3+2f` are equal as ideals of `L[a_0,\ldots,a_6]`, by a triangular change with diagonal `-2`. After that quotient, `[z^5]V=-2r_7`. Weighted scaling `a_i\mapsto\lambda^{8-i}a_i` has `r_4` of weight sixteen and `r_7` of weight nineteen; `lambda^{16}mu_4=1` is the correct direction, loses no geometric point of the nonzero-load stratum over an algebraic closure, creates no new `G_m`-orbit, and the residual `mu_{16}` is honestly not quotiented. The compiler reconstructs depressed `F_{12}(f)` with no order-two loads, inverts the eighth root through the first `q` that can enter `[w^{-7}]z^{12}`, checks tail signs and weights, builds `V` independently as a `z`-polynomial, demands both ideal containments and the lead relation before saturating by `r_7`, and is AWS-gated at the script boundary. The firewall is written and compiled.

What fails is the freeze of the charged parents. Target §1 prints three 64-character SHA-256 strings that are not the SHA-256 of any file in the repository. Each matches the true hash of the named path in its first eight hex characters and then diverges. The named files exist and their actual hashes are the ones already frozen by the sibling `mu_4=0` elimination and by the source-audit erratum; the mathematical identities used from those files recompute. The defect is therefore a cryptographic misidentification of otherwise correct parents, not a wrong theorem. It is blocking for `CONFIRMED` because the producer does not uniquely hash its inputs.

**REPAIR**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-client-20260825.md` | `2a7c5b6e09818d523954f8896a339d5f31407650b1777dd83f7a5bbbe5eda4fa` | target (matches required pin and `FREEZE.sha256`) |
| `cases/max12_812_order4_mu4_nonzero_curve_20260825/compile_curve.py` | `5c1add225079ff56454654bcbb893326bc95dc34cf5c3f763aa58a0ef012b8de` | compiler (matches required pin, `FREEZE.sha256`, and the compiler's self-pin of the client) |
| `cases/max12_high_row_probe_20260824/shared_faber_probe.py` | `69f9e12c0fa1e98bb7bc4dda87ab00c7f87ce2fd9c80a4bf210d216ee1bd2d9f` | shared sparse Faber source (matches target §1, compiler `EXPECTED_SHARED_SHA256`, and `FREEZE.sha256`) |
| `xmodel/max12-812-order24-coefficient-infinity-source-audit-20260825.md` | `092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e` | named parent; **does not match** the string printed in target §1 |
| `xmodel/max12-812-terminal-exact-differential-divisor-theorem-20260825.md` | `1cd824c9553a800ddf390bc972a29656e1286699406b1ca46bbc94bdfe18084b` | named parent; **does not match** the string printed in target §1 |
| `xmodel/max12-812-terminal-exact-differential-divisor-review-grok-20260825.md` | `db67f16dbda759b8481fcbf32491fe77c37483bb5fe70830eb42e95541767251` | named in target §1; **does not match** the string printed there; unused as a verdict |
| `cases/max12_812_order4_mu4_nonzero_curve_20260825/run_compile_aws.sh` | `9a2318e906ffd084858b013cb6b973a94d0771072305359f75c4a58c72d04523` | freeze list |
| `cases/max12_812_order4_mu4_nonzero_curve_20260825/run_geometry_aws.sh` | `71dcafdfbf2ec6b07e0bf98cbe7b89179e40c7e4e6c31753c6599c34102094c8` | freeze list |
| `cases/max12_812_order4_mu4_nonzero_curve_20260825/launch_remote.sh` | `1e85dd78dd75cda4bae0d5bfef1d7e5d6a04f9bf9161efc99cde8aa80f82b6b9` | freeze list |
| `ops/aws_exact_lane.sh` | `ebe06a100ae8f6bcdbdc580be89954d4cbc560c97cd75014153d61292415959b` | freeze list |
| `xmodel/max12-812-order24-coefficient-infinity-source-audit-erratum-v2-20260825.md` | `aa90155ec8a182f4f451c77fc9548cf8035889efc230afdaea622f84eb18c495` | not charged by the target; records the *actual* source-audit hash; unused as a verdict |

Printed versus actual parent hashes:

| Named file | Printed in target §1 | Actual SHA-256 |
|---|---|---|
| source audit | `092dfb6dcdbb4fc52438b4027bef994607f61d9f04247ff19c5db2237af2ff9c` | `092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e` |
| terminal theorem | `1cd824c9f82601620500187c3a98cdd105769ee12988b2e3b12b7179f99a3fdb` | `1cd824c9553a800ddf390bc972a29656e1286699406b1ca46bbc94bdfe18084b` |
| terminal review | `db67f16d8e287ba74bb49e26d558b43f81592298446a8685143345089518fc79` | `db67f16dbda759b8481fcbf32491fe77c37483bb5fe70830eb42e95541767251` |

No file in `xmodel/` hashes to any of the three printed strings. Each printed string agrees with the true hash of the named path through eight hex characters and then diverges. That is a freeze failure, not a missing file. The sibling elimination `xmodel/max12-812-order4-mu4zero-davenport-stothers-elimination-20260825.md` and the source-audit erratum already freeze the *actual* source-audit and terminal-theorem hashes; those actual files are the ones read below.

The source audit is consumed only for the tail convention `(2.3)`, the exact-order-four load list `(2.5)`–`(2.6)`, the terminal row `(2.4)`, and the weighted homogeneity `(5.1)`. Those identities are re-derived from the displayed formulae in that file; the audit's status line, its §7, and the erratum that later repairs `(7.2)` are not inputs. The terminal theorem is consumed only for `8r_7'=j/u` with `j\neq 0` and the inverse-character line; its classification of the order-two `[6,2]` profile is not an input. The terminal review is unused as a verdict. No D1 compiler, no `(9,12)` formula, and no order-two load specialization is consumed.

`FREEZE.sha256` is internally consistent for every file it names. Repairing the three parent strings in the producer will change the producer bytes and therefore the compiler's `EXPECTED_CLIENT_SHA256`; those two pins must move together.

---

## Strongest exact theorem that survives

Let `L` be a characteristic-zero field. Let `f=z^8+a_6 z^6+\cdots+a_0` be the generic monic depressed octic over `L`, and let `g=F_{12}(f)` be its Faber polynomial of degree twelve, with no lower Faber constants. Write

```text
w=f^{1/8}=z+O(z^{-1}),
w^{12}-g(z(w))=sum_{ell>=1} r_ell w^{-ell}=:E.
```

Then, as an identity of Laurent series in `w` with coefficients in `L[a_0,\ldots,a_6]`,

```text
g^2-f^3=-2 w^{12} E+E^2,
```

and `E^2` has strictly negative `w`-order, hence strictly negative `z`-order. Consequently the polynomial `V=g^2-f^3+2f` has degree at most eleven, the two unsaturated ideals

```text
(r_1,r_2,r_3,r_4-1,r_5,r_6)
    =  ([z^{11}]V,[z^{10}]V,[z^9]V,[z^8]V,[z^7]V,[z^6]V)
```

of `L[a_0,\ldots,a_6]` are equal, the change of generators is triangular with diagonal `-2`, and

```text
[z^5]V+2 r_7  lies in  (r_1,r_2,r_3,r_4-1,r_5,r_6).
```

On the exact-order-four leaf `(r_1,\ldots,r_7)=(0,0,0,mu_4,0,0,R_7)` with `mu_4\in L^*` one has

```text
g^2-f^3+2 mu_4 f=-2 R_7 z^5+O(z^4),     [z^5]=-2 R_7.
```

The weighted `G_m`-action `a_i\mapsto\lambda^{8-i}a_i` sends `r_ell\mapsto\lambda^{12+ell}r_ell`. Over an algebraic closure, every geometric point of this leaf is represented, after a finite constant-field extension, on the affine chart `r_4=1`, `r_7\neq 0`; the residual `mu_{16}` is finite, fixes `r_4`, and acts on `r_7` by a primitive character. Emptiness of the saturation

```text
I_4=(r_1,r_2,r_3,r_4-1,r_5,r_6):r_7^{infinity}
```

would therefore eliminate the entire `mu_4\neq 0` order-four terminal leaf. Nonemptiness is only a coefficient-infinity necessary condition: it is not source exactness `8dR_7=j\,dx/u`, a polynomial Taylor realization, a Keller pair, order-four closure, or JC2.

The compiler specified in target §4, as read in source, reconstructs both presentations from the frozen shared Faber primitives, demands the two containments and the lead relation before saturating, and refuses to run off a registered AWS lane. Its geometry gate is emitted, not executed, in this review.

---

## Attack 1 — sign, constant, and `E^2` contamination

**CONFIRMED.** The displayed identity is forced by the tail convention. No `E^2` term can reach a nonnegative degree, even before the order-four specialization.

**Convention.** Target `(0.1)` is the source-audit convention `(2.3)` with the three order-four target gauges already imposed, so `H_F(w)=w^{12}`:

```text
w=f^{1/8}=z+O(z^{-1}),
w^{12}-g(z(w))=sum_{ell>=1} r_ell w^{-ell}.
```

Put `E` for the right-hand side. Then `g=w^{12}-E`. Because `w^8=f` one has `f^3=w^{24}`, and

```text
g^2-f^3=(w^{12}-E)^2-w^{24}=-2 w^{12} E+E^2.
```

This is target `(2.1)`. The sign of the cross term is the sign of `-2g_{\mathrm{lead}}E` with `g_{\mathrm{lead}}=w^{12}`, hence the sign of the convention `w^{12}-g=E`. The opposite tail convention would produce `+2w^{12}E`. Characteristic zero is used only later, for `2\neq 0` as a unit in the ideal-theoretic diagonal.

**`E^2` cannot contaminate a nonnegative degree.** Before any tail restriction, `E=O(w^{-1})`, so `E^2=O(w^{-2})`. Depression `[z^7]f=0` gives the monic eighth root

```text
w=z(1+U)^{1/8},     U=sum_{i=0}^6 a_i z^{i-8}=O(z^{-2}),
```

hence `w=z+O(z^{-1})` with no `z^0` term, and more precisely `w=z+(a_6/8)z^{-1}+O(z^{-2})`. In particular `w=z(1+O(z^{-2}))`, so

```text
w^{-1}=z^{-1}(1+O(z^{-2})).
```

Every strictly negative power of `w` expands as a series in strictly negative powers of `z`. Therefore `E^2=O(w^{-2})` is `O(z^{-2})` and contributes nothing to `[z^k]` for `k>=0`. This is an identity in the polynomial ring, not a statement on a locus.

On the exact-order-four leaf `(0.2)` one has `E=mu_4 w^{-4}+R_7 w^{-7}+O(w^{-8})`, so `E^2=mu_4^2 w^{-8}+O(w^{-11})`, which is even more negative. There is no route by which an `E^2` monomial can reach degree five, let alone degrees six through eleven.

**The shifted identity.** Substitute `(0.2)` into `(2.1)`:

```text
w^{12} E=mu_4 w^8+R_7 w^5+O(w^4)=mu_4 f+R_7 w^5+O(w^4),
g^2-f^3=-2 mu_4 f-2 R_7 w^5+O(w^4).
```

Tails `r_ell` with `ell>=8` produce `w^{12-ell}` of `w`-degree at most four, and are absorbed in `O(w^4)`. Adding `2 mu_4 f` yields target `(2.2)`:

```text
g^2-f^3+2 mu_4 f=-2 R_7 w^5+O(w^4).
```

The left side is a polynomial in `z`. For the right side, `w^5=z^5+O(z^3)` (the first correction in `w-z` is `O(z^{-1})`, so `[z^4]w^5=0`) and `O(w^4)=O(z^4)`. Hence

```text
g^2-f^3+2 mu_4 f=-2 R_7 z^5+O(z^4),
```

with `[z^5]=-2 R_7`. The terminal row `8 dR_7/dx=j/u` with `j\neq 0` makes `R_7` nonconstant, hence nonzero in the function field, which is target `(0.5)` before normalization. Without the shift, `g^2-f^3` has degree eight on this leaf (leading term `-2 mu_4 f`), so the order-four Davenport–Stothers equality used for the separate `mu_4=0` stratum does not apply. That split is correct and is not an input to the present client.

Attacks that failed: opposite tail sign; an `E^2` contribution to degree five from `mu_4^2 w^{-8}` after converting `w\to z` (still `O(z^{-8})`); a `z^4` term in `w^5` spoiling `[z^5]` (depression kills it); contamination of degrees `>=6` by `r_ell` with `ell>=8` (those hit `w`-degree `<=4`).

---

## Attack 2 — exact equality of the two unsaturated ideals

**CONFIRMED.** The two six-generator ideals are equal in `L[a_0,\ldots,a_6]`, not merely radical-equal or equal after saturation. The diagonal is `-2`. The lead identity holds after quotienting, and in fact as a congruence modulo the unsaturated ideal.

Write `V=g^2-f^3+2f`. From Attack 1, as series in `w`,

```text
V=-2 sum_{ell>=1} r_ell w^{12-ell}+2 w^8+E^2.
```

The summand `2w^8-2 r_4 w^8` regroups exactly as a polynomial identity in `z`:

```text
-2 r_4 w^8+2 f=2(1-r_4)f=-2(r_4-1)f,
```

because `w^8=f`. Thus

```text
V=-2 r_1 w^{11}-2 r_2 w^{10}-2 r_3 w^9-2(r_4-1)f
  -2 r_5 w^7-2 r_6 w^6-2 r_7 w^5+O(w^4)+E^2.
```

`E^2` contributes nothing in nonnegative degree. For each `k>=1`, depression gives `w^k=z^k+O(z^{k-2})`, so `[z^k]w^k=1` and `[z^k]w^j=0` whenever `j<k`. Extracting coefficients of `z^{11}` down to `z^6` therefore yields a triangular change of generators

```text
[z^{11}]V=-2 r_1,
[z^{10}]V=-2 r_2,
[z^9]V =-2 r_3 + r_1\cdot P_9,
[z^8]V =-2(r_4-1) + (r_1,r_2,r_3)-combination,
[z^7]V =-2 r_5 + (r_1,\ldots,r_4-1)-combination,
[z^6]V =-2 r_6 + (r_1,\ldots,r_5)-combination,
```

with each off-diagonal coefficient a polynomial in the `a_i` coming from the lower terms of higher `w`-powers, and with the entire contribution of `2f` absorbed into the principal ideal `(r_4-1)` via `-2(r_4-1)f`. Characteristic zero supplies that `-2` is a unit. Induction from degree eleven down to degree six therefore gives equality of the two ideals, which is target `(2.3)` and the “equivalently” clause of `(0.3)`–`(0.4)`.

The same expansion at degree five gives, *before* setting the six generators to zero,

```text
[z^5]V+2 r_7  \in  (r_1,r_2,r_3,r_4-1,r_5,r_6).
```

After quotienting, `[z^5]V=-2 r_7`. Tails `r_ell` with `ell>=8` hit only degree `<=4` and cannot disturb this identity. On the saturated chart `r_7\neq 0` one then has `deg_z V=5` exactly, which is `(0.5)`.

The compiler is nevertheless right not to trust the hand reduction: mutual standard-basis reduction is an independent check of the same equality, and reduction of `v_5+2 r_7` against either Gröbner basis is an independent check of the congruence. Those checks are specified and emitted; they are not executed in this review.

Attacks that failed: treating the change as only a variety statement (the diagonal is a unit, so the ideals are equal); a leftover `[z^6](2f)=2a_6` outside `(r_4-1)` (it is exactly the degree-six piece of `-2(r_4-1)f`); an `r_7` contribution to degree `>=6` (`w^5=z^5+O(z^3)`); claiming `[z^5]V=-2 r_7` as a polynomial identity before quotienting (it is only a congruence; the target states it on the locus).

---

## Attack 3 — weighted normalization of nonzero `mu_4`

**CONFIRMED.** The direction `lambda^{16} mu_4=1` is the correct chart of the weighted `G_m`-action. Geometric points of the nonzero-load stratum are neither created nor lost over an algebraic closure. Arithmetic descent is correctly not asserted. The residual `mu_{16}` and the order-four deck subgroup are correctly distinguished, and the client honestly retains all seven coefficients.

**Weights.** Source-audit `(5.1)`, specialized to the order-four client with no `k_j`, is the substitution identity

```text
r_ell(lambda^{8-i} a_i)=lambda^{12+ell} r_ell(a).
```

Thus `r_4` has weight sixteen and `r_7` has weight nineteen, which is target `(3.1)`. This is the action on coefficient space, not a rescaling of a particular geometric `z`. The compiler's monomial-weight check is the same identity, with weights `(8,7,6,5,4,3,2)` on `(a_0,\ldots,a_6)` and expected weight `12+ell`.

**Direction.** If `r_4(a)=mu_4\neq 0` and `a_i'=lambda^{8-i}a_i`, then `r_4(a')=lambda^{16} mu_4`. Setting this equal to one is `lambda^{16} mu_4=1`. The opposite exponent would send `r_4` to `mu_4` or to `mu_4^{-1}` and would not cut out the chart `r_4=1`. Over an algebraic closure of characteristic zero, `mu_4\neq 0` has sixteen sixteenth roots, so such a `lambda` exists after a finite extension of the constant field, as claimed.

**Open condition of weight nineteen.** The same substitution sends `r_7` to `lambda^{19} r_7`. Here `lambda\neq 0`, so `r_7=0` is preserved in both directions. The terminal row makes `R_7` nonconstant on any actual source, hence nonzero as a function; the coefficient-fibre analogue is the principal open `r_7\neq 0`, imposed by saturation. Moreover `gcd(19,16)=1`, so on the chart `r_4=1` the residual `mu_{16}` acts on `r_7` through the primitive character `zeta |-> zeta^{19}=zeta^3`. No additional invariant vanishing of `r_7` is forced along residual orbits.

**Creation and loss of geometric points.** The map from `{mu_4\neq 0}` to `{r_4=1}` is restriction to a slice of a `G_m`-orbit. Over an algebraic closure it is surjective on geometric points of the nonzero-load stratum and finite of degree sixteen. It does not produce new orbits. It loses precisely the locus `r_4=0`, which is the separate `mu_4=0` stratum and is out of scope. Points with `r_4\neq 0` and `r_7=0` scale to `r_4=1`, `r_7=0` and are then deleted by the mandatory saturation; those points fail `(0.2)` anyway. No geometric point of `(0.2)` is lost. `L`-rational points need not descend to `L`-points of `C_4`, because `lambda` may require a finite extension; the target states this and does not claim arithmetic descent.

**Residual symmetry.** The stabilizer of the chart `r_4=1` is `mu_{16}`. For `lambda=zeta` a fourth root of unity one has `zeta^{16}=1` and

```text
a_i |-> zeta^{8-i} a_i=zeta^{-i} a_i,
r_4 |-> r_4,     r_7 |-> zeta^{19} r_7=zeta^{-1} r_7,
```

which is the order-four deck action on coefficients written in source-audit `(4.1)` and `(4.5)`. The word “in particular” in target §3 is accurate: the deck is a subgroup of the residual `mu_{16}`, not the whole residual. The client keeps all seven coefficients and assumes no freeness of the residual action. Stabilizers on coordinate hyperplanes are therefore not a defect.

Attacks that failed: reversing the exponent of `lambda` (that does not cut out `r_4=1`); claiming loss of geometric points over `Qbar` (the slice meets every nonzero-load orbit); claiming the residual action is free (not asserted); identifying `mu_{16}` with the Kummer deck (the target does not).

---

## Attack 4 — compiler, independently of live output

**CONFIRMED as source, with repairable freeze coupling and cosmetic Singular/spec nits.** The compiler was read, not run. No emitted `.sing`, JSON, or AWS stdout is evidence.

**No hidden order-two loads.** The coefficient ring is `Ring([a0,...,a6])`. There is no `k_10`, `k_6`, `k_2`, `delta0`, or `c_j`. The Faber loop builds `F_j` for `j=0,\ldots,12` and then sets `g=faber[12]`. The unused `F_j` for `j<12` are discarded, not multiplied by a load. This matches source-audit `(2.6)` for `e=4` after the three target gauges, which leave only the monic `w^{12}`. No `(9,12)` branch of `Frontier.compile` is called.

**Depressed `(8,12)` Faber polynomial.** `f` is `{8:1}` plus `a_i` at exponents `0,\ldots,6`, so `[z^7]f=0`. The binomial construction is the shared source's construction:

```text
F_j=z^j sum_{k=0}^{floor(j/2)} binom(j/8,k) U^k
```

truncated to nonnegative `z`-degree, with `U=sum_{i=0}^6 a_i z^{i-8}`. For `j=12` this is the polynomial part of `w^{12}=z^{12}(1+U)^{3/2}`. The monic/degree check `g[12]=1` and no exponent `>12` is fail-closed. Binomial coefficients are exact `Fraction` values.

**Inverse-series depth.** A correction `t_q w^{-q}` first appears in `[w^{-ell}]z^{12}` at `q=11+ell`, because the linear term in `z^{12}` is `12 w^{11}\cdot t_q w^{-q}`. For `ell=7` this is `q=18`. The compiler sets `last_q=n+last_tail-1=18` and then verifies that `f(z(w))-w^8` has zero coefficients at every target `w^{7-q}` for `q=1,\ldots,18`. A hypothetical `t_{19}` would first enter `[w^{-8}]z^{12}`, which is below `r_7`. Lower `z`-powers in `g` need strictly smaller `q`. Depth is necessary and sufficient for `r_1,\ldots,r_7`. The shared helper `inverse_root_series` (depth `n+1=13`, only `r_1,r_2`) is not used; `inverse_root_to` is a local reconstruction from the shared primitives `zpower_coefficient`, `cadd`, `cmul`, `cscale`.

**Tail signs and weights.** `[w^{-ell}]g(z(w))` is scaled by `-1`, which is `r_ell=-[w^{-ell}]g` from `(0.1)`. Every monomial of every `r_ell` is checked to have weight `12+ell`, else the compiler fails. `r_1,\ldots,r_7` are all emitted.

**Independent shifted polynomial.** `V` is `zmul(g,g)-zpower(f,3)+2f`, a sparse `z`-polynomial, not a rearrangement of the tail series. The identity `deg V<=11` is checked by failing on any exponent `>11`; Attack 1 proves that this is an identity, so the check is a correct sanity gate rather than a locus restriction.

**Ideal containments, lead relation, mandatory saturation, fail-closed.** The emitted Singular program, as constructed by `emit_singular`, does the following and nothing weaker:

1. `Itail=r1,r2,r3,r4-1,r5,r6` and `Icoef=v11,v10,v9,v8,v7,v6`;
2. `Gtail=std(Itail)`, `Gcoef=std(Icoef)` after `option(redSB)`;
3. both `reduce(Itail,Gcoef)` and `reduce(Icoef,Gtail)` must be the zero ideal, else `SOURCE_EQUIVALENCE=FAIL` and `quit` (no geometry);
4. `reduce(v5+2*r7,Gtail)==0`, else the same failure;
5. only then `SS=sat(Itail,ideal(r7))`, `J=std(SS[1])`, and the unit/dimension/size/basis report.

Saturation is of the unsaturated tail ideal by the principal ideal `(r_7)`, which is `I_4` in `(0.3)`. It occurs before `dim`, `size`, or any emptiness statement. No expected dimension is hardcoded. The payload's `scope` block records `EMITTED_NOT_RUN` for equivalence and saturation, `NOT_COMPILED` for source exactness and finite Taylor, `order4_mu4_nonzero_closed: False`, and `JC2: NOT_CLAIMED`. That is the correct firewall at the compiler boundary.

**AWS guards.** `require_registered_aws` refuses unless `platform.system()=="Linux"`, `/sys/class/dmi/id/sys_vendor` is `Amazon EC2`, and `JC2_REGISTERED_AWS_LANE` is nonempty. `run_compile_aws.sh` and `run_geometry_aws.sh` repeat the OS/vendor check, export the tag, set `ulimit -v` to the registered caps `134217728` and `402653184` KiB, and `exec` through `ops/aws_exact_lane.sh`, which is itself AWS-gated, records host/start/argv, and appends end time, return code, and stdout/stderr hashes. `launch_remote.sh` writes a registration ledger before invoking either runner. The compiler additionally refuses a wrong client hash, a wrong shared-Faber hash, a wrong argv arity, and an already-existing output directory (`mkdir(..., exist_ok=False)`). This is fail-closed at the intended entry points.

**Singular syntax and interpretation hazards, none fatal as source.**

- `coeff_string` emits `Q`-rationals as `Fraction` strings (`3/2`, `-1/8`) with explicit `*` between factors, and rewrites `+-` to `-`. In `ring R=0,(a0,...,a6),dp` these parse as rationals, not integer quotients. A characteristic-`p` reuse of the same string would be a different program; the emitted ring is characteristic zero.
- `ideal_is_zero` walks `size(A)` and treats the empty generator list as zero. That is the correct convention for `reduce` returning an all-zero or empty remainder.
- `sat` is taken from `elim.lib`; `SS[1]` is the saturated ideal. This is the standard Singular contract. Absence of `elim.lib` on a host is an environment failure and, by the producer’s own rule, **NO VERDICT**.
- `reduce(v5+2*r7,Gtail)==0` tests the lead congruence only modulo `Gtail`. After both containments have passed, `Itail=Icoef` as ideals, so this is equivalent to reduction modulo `Gcoef`. The letter of target item 5 says “modulo either ideal”; one side after equality is enough.
- Target `(4.1)` lists `deg(std(J_4))`. The compiler does not print `deg`. This is a spec mismatch. It is also the safer omission: `r_4-1` makes `I_4` inhomogeneous, so a projective `deg` is not the invariant the rest of the client uses. Dimension, reduced-basis size, and the basis itself are the honest affine report.
- On-disk `tails.json` / `shifted_coefficients.json` are `json.dumps(..., sort_keys=True)` with default separators and a trailing newline, while the recorded SHA-256 hashes a canonical dump with `separators=(",", ":")` and no newline. Rehashing the files will not reproduce the recorded digests. Cosmetic recording hazard; the in-memory pin is well-defined.
- `build_order4` itself is not AWS-gated; only `main` is. Importing the compiler as a module on a non-AWS host could reconstruct the tails. Process nit, not a mathematical leak in the advertised entry point.

Attacks that failed: a hidden `k_{10}F_{10}` term (the ring and `g=faber[12]` forbid it); inverse depth only through the shared `n+1=13` (the local routine goes to `18`); tail sign `+` rather than `-` (`cscale(-1,\ldots)`); constructing `V` from the tail series (it is an independent `z`-polynomial); saturating after dimension (order is sat, then `std`, then `dim`); running geometry if equivalence fails (`quit`); a local workstation path through `main` (triple AWS gate).

---

## Attack 5 — firewall

**CONFIRMED.** Target §0 and §5, and the compiler `scope` block, state the same restriction and do not use it as a slogan covering a stronger claim.

A point of `C_4` is a 7-tuple of constants whose ordinary Faber tails are `(0,0,0,1,0,0,r_7)` with `r_7\neq 0`. Emptiness of `I_4` over an algebraically closed field of characteristic zero would yield emptiness over every extension, including every Kummer function field, and would therefore eliminate the `mu_4\neq 0` order-four leaf. That is a genuine necessary condition. The converse is correctly refused: a nonempty component, even a parametrized curve, does not produce a non-fourth-power Kummer class, does not solve `8dR_7=j\,dx/u`, does not impose the terminal-power/Belyi divisor constraints, does not produce polynomial Taylor realizations at finite branch points, and does not produce a Keller pair. Failures of containment, missing `r_7` saturation, timeout, OOM, or engine disagreement are **NO VERDICT**, not emptiness. Naming the affine scheme a “curve” is slightly prejudicial, but no dimension is preregistered as a pass token, so the name does not smuggle a theorem.

The `mu_4=0` Davenport–Stothers elimination is correctly cited as a separate stratum: without the shift, `g^2-f^3` has degree eight here, and that argument does not apply. Order-two loads are correctly absent. JC2 is not claimed.

---

## Findings, classified

**Repairable, blocking for `CONFIRMED`.**

1. Target §1 prints three SHA-256 strings that are not the SHA-256 of the named files, nor of any other file in `xmodel/`. The named source audit, terminal theorem, and terminal review exist; their actual hashes are `092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e`, `1cd824c9553a800ddf390bc972a29656e1286699406b1ca46bbc94bdfe18084b`, and `db67f16dbda759b8481fcbf32491fe77c37483bb5fe70830eb42e95541767251`. Each printed string shares an eight-character prefix with the true hash and then diverges. The mathematical identities read from those files recompute and are used correctly. Repair: replace the three strings by the actual hashes. Because the compiler pins the producer by SHA-256, the producer repair and `EXPECTED_CLIENT_SHA256` must move in one freeze.

**Repairable, non-blocking.**

2. Target `(4.1)` lists `deg(std(J_4))`; the emitted Singular program does not print it. The ideal is inhomogeneous (`r_4-1`), so the missing invariant is not the one the rest of the client uses. Recording `dim`, reduced-basis `size`, and the basis is the correct affine gate. Align `(4.1)` with the compiler, or add an explicitly affine substitute.

**Cosmetic.**

3. Target §1 says the hostile-review/erratum chain is recorded in the source audit. The erratum lives in a separate file and is the document that records the chain. The present client does not consume the repaired identity `(7.2)`, so not charging the erratum is mathematically harmless.
4. Lead-relation reduction is only modulo `Gtail`. After both containments, this is equivalent to “either ideal”.
5. On-disk JSON bytes are not the hashed canonical dumps.
6. Calling `C_4` a curve before dimension is known. No expected dimension is a verdict token.
7. `build_order4` can be imported off AWS; `main` cannot.

**Fatal.** None. No numbered mathematical identity in §§0,2–5 is false.

---

## Smallest failing identity

The smallest failing identity is the first parent pin in target §1:

```text
SHA-256(xmodel/max12-812-order24-coefficient-infinity-source-audit-20260825.md)
  = 092dfb6dcdbb4fc52438b4027bef994607f61d9f04247ff19c5db2237af2ff9c.
```

This is false. The two subsequent parent pins fail in the same way. No identity in `(0.1)`–`(0.5)`, `(2.1)`–`(2.3)`, `(3.1)`, or the compiler contract of §4 fails.

Live AWS outputs were not used as evidence.

REPAIR
