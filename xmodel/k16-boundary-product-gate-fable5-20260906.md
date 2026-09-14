# K16 boundary lemma gate: four exact claims CONFIRMED at scope; the product target stays OPEN

2026-09-06. Gate lane `k16-boundary-product-gate-fable5-20260906`, reviewer Fable, producer Astra. Basis `0d39df3c9fd69c939a8420c54d03228b9077777d`. Gated report `xmodel/k16-boundary-product-astra-20260906.md`, SHA-256 `1c4a1100cc774932f23da27e11bf828a6fa10d5e256ce1528694d356d9031d9c`.

**Verdict.** Claims 1–4 are each CONFIRMED as exact statements at the scope the producer states. No REFUTED item. No GAP that changes a conclusion; two scope remarks are recorded (§5, §6). Claim 1 is a uniform rational-to-polynomial lemma and proves nothing about polynomial solutions. Claims 3–4 are an exact reformulation of the polynomial target, not a new obstruction. The all-m product target `OPEN[K16-UETA-WHOLE-POLYNOMIAL]` / (BOUNDARY) remains OPEN. Nothing is promoted; no source-to-terminal interface is asserted by analogy. No exit-price assertion is made, so no `charge_basis` line applies.

## 1. Custody and replay

The six receipt hashes in `/tmp/jc2-lane.RGUzEP/charged-inputs.list` were checked mechanically against `sha256sum` of the six files in `/tmp/jc2-lane.RGUzEP/inputs`; all six agree, and they agree with the `charged_input_<i>_sha256` entries of the run receipt. The gated report's hash equals the one named in the prompt. The producer's cited but uncharged source `xmodel/k16-universal-series-fable5-20260905.md` was hashed on disk: `5ac0ff1ddcfc766dd1d5050c73e08203795f1ecc56be954b388ef0c1eaeb41bb`, as cited.

Producer checker `box/k16-boundary-product-20260906/check.py` (`159431da68c3f73a860bada1e62b377bb75a116ffc1cf84ad16a3c5aef3d47f5`) replayed in normal mode: eleven PASS lines and `ALL_EXACT_IDENTITY_CHECKS_PASS`. It uses bare `assert`; under `python3 -O` every comparison is erased and the same PASS lines print. This replay is therefore not optimization-safe, and the checker was left untouched.

Reviewer controls, all with explicit `GateFail` exceptions (verified to fire under `-O`): `box/k16-boundary-product-gate-fable5-20260906/gate_controls.py` (`66647a83615b3cfa7312f831836102fac641e8a8e2932082226c8bf7ee795d44`), output `gate_controls.out` (`807e75e1d86fbc0ce542652fb22fabf47e468fce7979b0c2583dd61b80d845aa`), 69 PASS, 20 KB total, sympy 1.12, under two minutes. Where the producer verified identities with free value symbols (`w, wp, a`, free `Z`), the controls use actual polynomials with generic coefficients. No AWS, heavy CAS, `jc2-lean`, ledger, producer or tool edit; the excluded ideation, factored-J gate, Sol2TB and C-linear items were not read.

## 2. Claim 1, pole/defect lemma: CONFIRMED

Setting: `A, W` rational, `E=0`, `B!=0`, `W` regular at 0 with `W(0)=-B`, characteristic zero.

**Nonzero finite point alpha**, `A` pole order `a>=0`, `W` pole order `w>=0`, `U=x^3A^2` pole order `2a`. Candidate orders `2w+1` (from `2xWW'`), `2a+w` (`UW`), `4a` (`U^2`), and the dominated `2w, w, 2a, 0`. Every cell was replayed for `a<=3`, `w<=7` with actual Laurent leaders:

| case | unique maximum | leader |
|---|---|---|
| `a=0, w>=1` | `2w+1` | `-2w*alpha*cW^2` |
| `a>=1, w<=2a-1` (includes `w=0`) | `4a` | `-(3/16)alpha^6*cA^4` |
| `a>=1, w>=2a` | `2w+1` | `-2w*alpha*cW^2` |

Uniqueness is strict in all cells: `2w+1` is odd and `4a` even, so they never tie; at the boundaries `w=2a-1` and `w=2a` the margins are exactly one. Both leaders need `alpha!=0`; the derivative leader also needs `w!=0` in `k`, which is where characteristic zero enters. Hence no pole at any nonzero finite point, and `W` is polynomial.

**Origin.** For `a>=2` the unique leader is `U^2` at order `4a-6>2a-3` with coefficient `-(3/16)c^4` (replayed `a=2,3,4`). For `a=1`, with the general jet `A=c/x+a0+a1x`, `W=w0+w1x+...`, `E` is regular; `[x^0]E=-w0(w0+B)`, which vanishes by `W(0)=-B`; and

```text
[x^1]E = B*(eta - w1 - (3/4)c^2),   independent of a0, a1.
```

This is (PD) with `W'(0)` free, stronger than the checker, which fixes `W'(0)=eta` and reads off `-(3/4)Bc^2`. With `B!=0` and the linear marking, `c=0` and `A` is polynomial. `eta!=0` is not used.

**Both negative controls verified whole-equation.** Jet omitted: `A=c/x`, `W=p0c^2x-B`, `eta=(p0+3/4)c^2=+/-sqrt(3)c^2/2!=0` gives `E==0`, `W(0)=-B`, `W'(0)=eta-3c^2/4`. `B=0`: `A=c/x`, `W=p0c^2x`, `eta=p0c^2` gives `E==0` with both markings and a pole. So the linear marking and `B!=0` are each necessary. Scope: uniform in degree; rational category to polynomial category; silent on polynomial nonexistence.

## 3. Claim 2, normalization: CONFIRMED

`Etilde(x)=s^2E(rx)` was verified with actual generic-coefficient polynomials at `m=4,5` modulo `h^2=sr^3`, not only pointwise. Degrees and `lcW/(lcA)^2=p` are preserved because `q-2(m-2)-3=0`. With `lcA=1/y`, `lambda^2y^2=B^(2m-2)/eta^(2m-1)` and `lcWtilde=p*lambda^2`; every nonzero `lambda` occurs. Converse: `B0=1`, `eta0^q=1/(lambda^2y^2)`, `s=1`, `r=1/eta0`, `h=lambda*y*eta0^(m-2)`; the constraint `h^2=sr^3` holds exactly iff `eta0^q*lambda^2y^2=1`, the sign of `h` fixes `lcA=1/y`, and then `lcW=p/y^2`. The covers are of degree 2 forward and `q` backward; over algebraically closed `k` both exist. All constants are nonzero for integer `m>=4` on both factors: `y=0` would need `3m^2=m`, `2d+1=0` would need `m=3/4`; the argument is symbolic in `d`.

## 4. Claim 3, quadratic finite-algebra model: CONFIRMED

`E=x(WJ-R)` holds identically. `J` is polynomial by `W(0)=-1`; `J(0)=1` uses `W'(0)=1` as well. With an actual `A=x^2+b1x+b0` (m=4): `deg R=deg Q=13=4m-3`, `Q(0)=Q(1)=-1`, `Q-sigmaQ=(2t-1)D`, `Q(t)Q(1-t)=-R(f(t))`; `Q(tau)=0 mod R`, `R(f)=0 mod Q`, `f(tau)=x mod R`, `tau(f(t))=t mod Q`. So both maps in (QA) are well defined and mutually inverse as algebra maps, hence multiplicities and nonreduced structure transfer automatically. Structurally, `R=(x/3)D^2-D-1` has discriminant `1+4x/3=(2t-1)^2`; the model is the rationalisation of that square root, and the two `D`-roots `1/(t-1)`, `-1/t` are exactly `Q` and `sigmaQ`.

**Ramification.** `R(-3/4)=-(9/64)(Z(-3/4)^2+8/3)^2`, so `R(-3/4)=0` iff `Z(-3/4)^2=-8/3` (both directions; the checker tests one). `R'(-3/4)=4/3` because the `Z'` coefficient `(9/16)Z^2+3/2` vanishes there; `Q'(1/2)=D(1/2)=-2`. The root is simple in `R`, lies in exactly one of `W, J`, and if in `W` the slope satisfies `3W'^2-4W'-2=0`, discriminant 40. It cannot be dropped: it is realised by an actual degree-2 `A` with `A(-3/4)^2=-128/27` (replayed), a codimension-one stratum excluded by no hypothesis, and it is precisely where the (DF) derivation divides by `2t-1`.

## 5. Claim 4, norm factorization and (DF): CONFIRMED as an exact reformulation

**Necessity.** Under (QA) the ideal `(W)/(R)` maps to `(M)/(Q)` with `deg M=q` by length; `a=M(0)M(1)!=0` since `Q(0)=Q(1)=-1`. `Q` and `sigmaQ` have disjoint roots away from `t=1/2` because `D` is a unit at a `Q`-root; at `1/2` both are simple. Multiplicities transfer through the local components. Concrete instance `A=x^2-5/18`: `x0=4/3` is a root of `R`, `t0=4/3` of `Q`, `tau(x0)=t0`, the divisor selected by `W1=x-4/3` is `t-4/3` alone, and `W1(f(t))=[W1(0)/(M1(0)M1(1))]M1(t)M1(1-t)`; with `W(0)=-1` the constant is `-1/a`. `J(f)=aNsigmaN` follows by cancellation from `WJ=R`.

**Prime label.** In `V=M'(t)sigmaM(t)-M(t)M'(1-t)` the prime means differentiate, then substitute; replayed `V=d/dt[M sigmaM]`, and by the chain rule `W'(f(t))=-V/(3a(2t-1))`. (DF) equals `3a t(t-1)(2t-1)` times the defect `J(f)-2W'(f)+(W(f)+1)/f-2D`, verified with actual `M, N, D` polynomials.

**Converse.** Cancelling the nonzero polynomial `3a t(t-1)(2t-1)` in `k[t]` is valid, so (DF) with `Q=MN`, `deg M=q` gives `E=0`; `W(0)=-1` and `J(0)=aN(0)N(1)=1`, hence `W'(0)=1`, are forced by `Q(0)=Q(1)=-1`. Scope remark on "the leading ratio must still be imposed": the top coefficient of `WJ=R` is (UT) in `p=lcW/lcA^2` (replayed), so any solution of the prescribed degrees already has `p` equal to one of the two roots; the ratio only selects the `d`-sign and is automatic in the union over both factors. Not a gap.

**Hidden strata.** None found: the `2t-1` division is undone by the polynomial form; `t=0,1` are units; `t=1/2` is treated; `A=0` is excluded by degree; (NF) and (DF) are homogeneous of degree 2 in the scale of `M`, so monic `M` loses nothing.

**Negative meta-fact (reviewer).** (DF) is `sigma`-anti-invariant, `DF(1-t)=-DF(t)`, and `DF=(2t-1)G0(f(t))` with `G0` a polynomial in `x` (replayed). So the `t`-model carries exactly the `x`-line residual `E/x=0` (q equations, the first being `W'(0)=1`) plus `M|Q` (q equations), in `q+m-1` unknowns: overdetermined by `m`, the same count as the `x`-space reconstruction in the ueta report §4. The model creates no independent equation.

**Root-swap control: CONFIRMED at its limited scope.** For `A=x^(m-2)`, `R=(3/16)x^(4m-3)-(3/4)x^(2m-2)-1` has `R(0)=-1` and zero next-to-leading coefficient, so at least two distinct nonzero roots (squarefree at `m=4,5` as well). A valid swap between a chosen and an unchosen root always exists since `deg N=q-1>=1`, and it changes `W'(0)=sum 1/rho`. Hence not every degree-q divisor meets the marked derivative, while all satisfy (NF) with the same complementary degrees. It shows nothing about a divisor with `W'(0)=1`, nothing about (DF), and monomial `A` is already excluded by f3abel §5 (b=B=eta=0 only for t>=3). It is a control against "divisor count suffices", not a near-miss and not a finite-m solve. Norm factorization alone does not imply differential compatibility: confirmed.

## 6. History checksum and what is new

Named older reports, verified hashes: ueta `f04c483c94f9c1320e4d630cfd52422ca3730ad396d0d653c3d3ef2a2c49e8ac`, Xempty `1f06694fb58d53c4a4b3c54dad88722cd31a5ccc894679ac52b0620b91e2623f`, f3abel `0d2b27fed00a27a1f21d0997adce38252405506839d74f674327f2ff994b22b4`, Series `5ac0ff1d...` above.

- **Pole lemma: new relative to these.** f3abel §7 treats formal Laurent tails at infinity and local formal series at 0 only; Xempty §7.2 (line 751) explicitly asks for "a larger marked rational category with a proved return to polynomiality"; ueta §7's parity argument is on `b=B=0`. Claim 1 supplies that return on the `b=0`, `B!=0` boundary. It is a lemma about the rational category, not an obstruction.
- **Quadratic model: new as a norm structure, not as a parametrization.** At `b=0, B=eta=1` Xempty's (UR2) map is `f(v)=4v^2+(16/3)v^4`, even in `v`, and equals `3t(t-1)` with `t=-(4/3)v^2` (replayed). The model is the even-part reduction of that quartic; this is what the producer's phrase "uses the extra b=0 biquadratic structure" means. The genuinely new content is `Q(t)Q(1-t)=-R(f(t))` with `sigma: t->1-t` and the resulting (NF)/(DF). f3abel's RC5/RC10 are resultant norms over the `K` and `C` algebras, a different object.
- **Residue route.** Series Prop 3.1 (lines 128–141) returns exactly (UT); the producer's statement that it "only returns the top balance" is consistent.

Classification for the ledger: Claim 1 = uniform lemma; Claims 3–4 = exact reformulation (primitive/circuit level), equivalent to the polynomial target per `m` in the union over `d`. Neither is a new obstruction, as the producer states.

## 7. Follow-on

None proposed. The anti-invariance fact in §5 shows the `t`-model has no equation beyond the `x`-line residual, so its cheap discriminators are the root-contact quadratics already in f3abel §6 (RC6, RC8) and the residue calculus already in Series Prop 3.1. A (DF)-based finite-m solve is excluded by the brief and would reproduce ueta §6. Fallacy audit: pole identities used only after checking `B!=0`, `W(0)=-B`, the vertex class at 0 and every leader; the ring maps are declared with image checks; the prime mark is defined; no floor is read as attainment; no cap or analogy fills a gap.

<!-- BODY-END -->
