# Hostile review — universal odd-row Laurent-to-Faber pole recurrence

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_d1_universal_odd_pole_recurrence_20260826/` |
| Overall verdict | **CONFIRMED** |
| Smallest failing `(M,r,q,e,row)` | none |
| Smallest basis exception | none |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Producer PASS markers, validator strings, and the finite `M<=24` grid are not authority |
| Method | SHA-256 of every named pin; frozen odd block of `T` from `compile_cge3_universal.py`; generating-function identities over `Q[s]`; independent `Fraction` reconstruction of the transform, the degree bound, both row-seven vectors, and sharpness; miner and inventory inspection. No Singular, Sage, msolve, Lean, or AWS re-execution |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the six required primary pins match. Every path named in `FREEZE.sha256` (6/6), `EVIDENCE.sha256` (16/16), and `PRODUCER_FREEZE.sha256` (4/4) rehashes to the printed digest. Nested `results.sha256` on both V2 lanes rehashes to the retrieved `result.json`, `stdout`, and `stderr`. Failed V1 wrapper launches are no-verdict and were not used. Exact Q is the characteristic-zero software endpoint; `F_65521` is a second host running the same `Q`-Fraction miner with a modular assertion. The unbounded statement is the degree identity below, not the grid. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

The frozen odd Faber matrix is the ordinary generating function

```text
Phi(x) = (1-s x)^{-1/2} Y(x/(1-s x)),     s = p/2,
```

with the minus sign and the half exponent both forced by rows 1, 3, 5, 7. An odd proper principal part of pole order at most `q` along `L=z^2+s` has ordinary generating function in the span of `Y_(q,e)=x^e/(1+s x)^q` for `0<=e<q`, and the transform is exactly `x^e(1-s x)^{q-e-1/2}`. For every pair of integers `1<=r<=M` the functional `W_(M,r)=(1-s x)^{M-r-1/2}` makes `W Phi_(q,e)` a polynomial of degree `M-r+q-1<=M-1`, so the terminal coefficient vanishes identically over `Q[p]`. That identity is not inferred from `M<=24`.

The cutoff is sharp as a polynomial in `s`: the first outside generator `q=r+1,e=r` has terminal coefficient `(-s)^{M-r}`, and `q=M+1,e=M` has coefficient `1`. Specializing `p=0` collapses the basis and kills `(-s)^{M-r}` for `r<M`; that is the discriminant chart `V(p)`, not a failure of uniform sharpness. Both row-seven vectors are recovered with the charged signs. Substitution of an arbitrary series `p(sigma)` and sigma truncation are ring homomorphisms of a polynomial identity, so they commute with it; the Cauchy product of `W` with `Phi` is the claimed relation and does not alter the vanishing.

The theorem supplies a row syzygy after a pole ceiling and a target placement are known by other means. It does not prove the composed D1 inventory, any chart or fan cover, a D1 theorem, order two, maximum twelve, or JC2.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Six primary pins | hashes | all six match the required bytes |
| 0. Named manifests | every named file | `FREEZE` 6/6, `EVIDENCE` 16/16, `PRODUCER_FREEZE` 4/4, both nested `results.sha256` 3/3 |
| 0. V1 | failed wrapper | no-verdict; not evidence; V2 alone is charged |
| 1. Odd generating transform | sign and half exponent from the row matrix, rows 1,3,5,7 | **holds**; see §1 |
| 2. Pole-`q` basis and closed transform | span of `Y_(q,e)`, `0<=e<q`; `Phi=x^e(1-sx)^{q-e-1/2}` | **holds**; no parity, numerator-degree, polynomial-part, or indexing hole in the claimed class; see §2 |
| 3. Functional `W_(M,r)` and degree proof | all integers `1<=r<=M`, not the grid | **holds**; see §3 |
| 4. Sharpness | `q=r+1,e=r` equals `(-s)^{M-r}`; `q=M+1,e=M` equals `1`; `p=0` | **holds**; `p=0` is a chart degeneration; see §4 |
| 5. Row-seven vectors | `r=2` and `r=3` in powers of `p`, with signs | **holds**; see §5 |
| 6. Moving `p(sigma)` | substitution commutes with truncation; convolution | **holds**; see §6 |
| 7. Miner, counts, dual AWS, inventory SHA/ceiling | software control only | **holds** as a control; see §7 |
| 8. Firewall | no inventory, cover, D1, order two, max twelve, or JC2 | **holds**; see §8 |

---

## 0. Custody

Recomputed SHA-256 of the six required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../RESULT.md` | `97cb6fedc22c3352b304684c0e46e768eb12ce579ba52dbf24bb38be78533263` | producer report |
| `.../EVIDENCE.sha256` | `6ed0d583e64eecc9403f135692d0ac0b0158a3717ddd4daad84d4df76394ba87` | evidence freeze |
| `.../FREEZE.sha256` | `9990ba104bb7d5bf4e494e5faad59545b6a6500cbdd3db571ee25429d3e13ed0` | source freeze |
| `.../AWS_LAUNCH_METADATA.md` | `c36812e8ad47e92086f49d345abb9f89f624519adb0db38d8edf9ec372d2890f` | V2 launch metadata |
| `.../PRODUCER_FREEZE.sha256` | `81b0f9d772add009b1d7c6ed0caa9ef13098fc72f8921e502128ba1402901f6b` | producer pin list |
| `.../odd_pole_recurrence_miner.py` | `d1e3218e3104651996b77d440eb0d92924369c8c380ed3ccf0330a869a170c41` | AWS miner |

`FREEZE.sha256` names six files, all matching:

| Path | SHA-256 |
|---|---|
| `REGISTRATION.md` | `174ea935c6c40b753447473e56692f118a70d25aa599c2a69c42d1fc2ab1c6cf` |
| `odd_pole_recurrence_miner.py` | `d1e3218e3104651996b77d440eb0d92924369c8c380ed3ccf0330a869a170c41` |
| `run_aws.sh` | `30c82a6cb207314664ecd8e23969bf9770d48da8ad6091f8979a359fb3a78c19` |
| `launch_host.sh` | `522a7d036ce12fc0a279a301f27151d62dca47a6e25f07ac6c97e130fc3f58e9` |
| D1 `a=10` `source_inventory.json` | `884922fede59bc3540a61aa089a9ed92f65235b269330d63b9195afa69019297` |
| age10 `PRODUCER_FREEZE.sha256` | `60b2e1d52156f0648f7f39739f06c139d7d274c28fe4147eaba8d7213dfc2f0b` |

`EVIDENCE.sha256` names 16 V2 files; all 16 rehash. `PRODUCER_FREEZE.sha256` repeats the first four primary pins and rehashes. Nested `results.sha256` on each V2 lane rehashes to that lane's `compiled/result.json`, `stdout`, and `stderr`.

V1 is absent from the charged evidence tree. `RESULT.md` and `AWS_LAUNCH_METADATA.md` record that the first wrapper died on the miner's `output already exists` guard before any coefficient check. V2 `launch_host.sh` refuses a pre-existing job base and does not precreate `compiled/`. Distinct earlier V1 tags are not used below.

Exact Q and `F_65521` are genuinely separate frozen V2 runs.

| Charge | Exact `Q` (Box03) | `F_65521` (r6d) |
|---|---|---|
| Host | `ip-172-30-0-249` | `ip-172-30-0-45` |
| Tag | `…_q_v2_20260826_box03` | `…_p65521_v2_20260826_r6d` |
| PID | `240508` | `301104` |
| Characteristic token | `0` | `65521` |
| `result.json` SHA | `91fc6b2c9ccc241c926eefa7ed81b68a7590c9255cfa98e6130920f97396d67d` | `54be9ad23badf6cb1868481ec1439cb0a1084da15dca179acbbfd1c3eaf556d3` |
| Stdout SHA | `c70cd6418aa9f7ca6769ee1e7dc62e402773764ffaa149ec756cbfe4334d4a7c` | same printout |
| Stderr SHA | `379a0ecb4e29b75d226aabb229a8389ee4e8f555b68fad5ce6c3bb5e30e21d29` | `c44ced167cc45c31593294392b5e69585df48d4882a11dd71a0f9c620385ab1c` |
| Engine `rc` | `0` | `0` |
| Peak RSS / swaps | 31,960 KiB / 0 | 31,656 KiB / 0 |
| Wall | 1:11.36 | 1:11.13 |
| VM cap / timeout | 4,194,304 KiB / 600 s | same |

The two `result.json` files differ only in `characteristic` and `registered_aws_lane`. Counts, closed-form strings, row-seven `s`-scalars, and the inventory SHA are identical. Stdout is byte-identical because the miner never prints the characteristic. Stderr is GNU `time` only, with distinct RSS and wall; no `FAIL:`, no `Traceback`, exit status 0. The validator string is not a mathematical verdict.

A passing manifest is not a theorem. What follows is the source.

---

## 1. Odd frozen Faber generating transform

Ordinary odd Laurent and Faber rows are packed as

```text
Y(x) = sum_{m>=0} h_{2m+1} x^m,
Phi(x) = sum_{m>=0} Phi_{2m+1} x^m.
```

The frozen transport is `transform_series` of `compile_cge3_universal.py`. For `i-j=2n>=0`,

```text
T_{ij} =  ((j/2)_n / n! / 2^n) p^n,
```

and `T_{ij}=0` if `i-j` is negative or odd. Restricting to odd indices `i=2m+1`, `j=2k+1` gives `n=m-k` and `j/2=k+1/2`, so the coefficient of `s^{m-k}` in `Phi_{2m+1}` is

```text
(k + 1/2)_n / n! .
```

The ordinary generating function of those Pochhammer coefficients is `(1-s x)^{-(k+1/2)}`. Therefore

```text
Phi(x) = sum_k h_{2k+1} x^k (1-s x)^{-(k+1/2)}
       = (1-s x)^{-1/2} Y(x/(1-s x)).
```

The minus sign is forced: `(1+s x)^{-1/2}` would alternate. The half exponent is forced: an integer exponent would replace `k+1/2` by an integer Pochhammer.

Against rows 1, 3, 5, 7 this is the displayed odd block, all signs positive in `p`:

```text
Phi1 = h1
Phi3 = h3 + (p/4) h1
Phi5 = h5 + (3p/4) h3 + (3p^2/32) h1
Phi7 = h7 + (5p/4) h5 + (15p^2/32) h3 + (5p^3/128) h1.
```

Direct expansion of `(1-s x)^{-1/2} Y(x/(1-s x))` through `x^3` recovers those four rows with `s=p/2`. A sign error or a `+1/2` exponent already fails at `Phi3`. Even rows never enter: `T` vanishes on odd index gaps, so the odd generating function is closed.

---

## 2. Pole-`q` basis and closed image

On the square chart `L=z^2+s`. Odd rational functions with poles of order at most `q` at the two roots of `L`, and with proper numerator, are

```text
z P(z^2) / L^q,     deg P <= q-1.
```

That is a `q`-dimensional space. Expanding at infinity with local monomial `x ~ z^{-2}` converts the geometric basis `{z^{2e+1}/L^q : 0<=e<q}` onto `{x^{e'}/(1+s x)^q : 0<=e'<q}` by the index reversal `e' = q-e-1`. The two spanning sets are the same. The `+` in `1+s x` is the expansion of `L=z^2(1+s/z^2)` and is not optional: a Laurent factor `1-s x` would not cancel against the Faber substitution.

The claimed indexing `0<=e<=q-1` is therefore complete for odd proper principal parts of order at most `q`. Exact order `q` is the open subset on which the highest coefficient is nonzero; it still lies in the same span. Even functions contribute `Y=0` to the odd generating function and are not a missing odd generator. An improper numerator of `z`-degree `>=2q` splits as a polynomial at infinity plus a proper remainder of pole order `<=q`; only the remainder contributes to the sequence `(h_1,h_3,h_5,...)`. A finite polynomial `Y=x^k` is not the odd coefficient sequence of a function whose only poles are the roots of `L`, so it is not a counterexample to coverage of that class.

The transform is algebraic, not a truncated series:

```text
Phi_(q,e)(x)
  = (1-s x)^{-1/2} (x/(1-s x))^e / (1 + s x/(1-s x))^q
  = x^e (1-s x)^{-e-1/2} (1-s x)^q
  = x^e (1-s x)^{q-e-1/2},
```

because `1 + s x/(1-s x) = 1/(1-s x)`. For `0<=e<q` the exponent `q-e-1/2` is at least `1/2`, so every basis image is a formal binomial series of nonnegative half-integer order. Independent `Q`-reconstruction of `[x^m] Phi_(q,e)` from the ordinary basis and the odd `T` block agrees with this closed form for every `1<=q<=25`, `0<=e<q`, and `e<=m<=24` (5,525 identities). That grid is not the proof; the two-line substitution is.

No parity, numerator-degree, polynomial-part, or indexing exception that removes an odd proper pole-`q` term from the span was found.

---

## 3. The functional and the degree proof

Fix integers `1<=r<=M`. Set

```text
W_(M,r)(x) = (1-s x)^{M-r-1/2}.
```

For every `q<=r` and `e<q`,

```text
W_(M,r) Phi_(q,e) = x^e (1-s x)^{M-r+q-e-1}.
```

The exponent `M-r+q-e-1` is a nonnegative integer: `M-r>=0` and `q-e-1>=0`. The product is therefore an algebraic polynomial, of total degree

```text
e + (M-r+q-e-1) = M-r+q-1 <= M-1.
```

Hence `[x^M](W_(M,r) Phi_(q,e))=0` in `Q[s]=Q[p]`. The worst case `q=r` still has degree `M-1`. The identity holds for every pair of integers `1<=r<=M`, not merely for `M<=24`. The finite replay is a software control of the same polynomial identity and is not an inductive step.

The coefficient of `x^M` in `W Phi` is the linear combination of odd Faber rows `Phi_{2M+1},...,Phi_1` with weights `[x^j] W_(M,r)`. That is the claimed recurrence.

---

## 4. Sharpness and `p=0`

At the first outside generator `q=r+1`, `e=r`,

```text
W Phi_(r+1,r) = x^r (1-s x)^{M-r},
[x^M] = (-s)^{M-r}.
```

This is not the zero polynomial. At the terminal generator `q=M+1`, `e=M` one has `r=M` and `(-s)^0=1`. Neighbouring generators of the same pole, `q=r+1` with `e<r`, survive as well, with coefficient `(-s)^{M-e}`; they are not claimed as the distinguished negative control. The cutoff is therefore sharp on the whole pole-`(r+1)` space, uniformly in `s`.

On `p=0` one has `s=0`, `L=z^2`, and `Y_(q,e)=x^e` independently of `q`. The `q`-basis collapses. The polynomial `(-s)^{M-r}` evaluates to `0` whenever `r<M`, and the functional at `s=0` is `W=1`, which reads only `[x^M] Phi`. Every proper basis element has `e<q<=r<=M` and therefore `e<M` except the single terminal class `e=M`. Vanishing of `(-s)^{M-r}` at `s=0` for `r<M` is the discriminant specialisation `V(p)`, not a counterexample to uniform sharpness over `Q[s]`. The charged theorem is a polynomial identity; it remains sharp as such. Emptiness statements on `V(p)` are outside its scope.

---

## 5. Row-seven vectors

Row seven is `M=3`. Expanding `W` through `x^3` and converting `s^j=(p/2)^j`:

```text
r=2:  W = (1-s x)^{1/2}
      1,  -s/2,  -s^2/8,  -s^3/16
   -> 1,  -p/4,  -p^2/32, -p^3/128.

r=3:  W = (1-s x)^{-1/2}
      1,  +s/2,  +3 s^2/8,  +5 s^3/16
   -> 1,  +p/4,  +3 p^2/32, +5 p^3/128.
```

The miner stores the `s`-scalars `[1,-1/2,-1/8,-1/16]` and `[1,1/2,3/8,5/16]`; those are the same vectors. The order-two combination is therefore

```text
Phi7 - (p/4) Phi5 - (p^2/32) Phi3 - (p^3/128) Phi1,
```

and the order-three combination is

```text
Phi7 + (p/4) Phi5 + (3 p^2/32) Phi3 + (5 p^3/128) Phi1.
```

Both sign patterns are forced by the same generating functional. They are not independent experimental fits.

---

## 6. Moving `p(sigma)` and convolution

The terminal identity is the vanishing of a polynomial in `s` with coefficients in `Q`. Any homomorphism of `Q`-algebras sends that polynomial to zero. In particular:

- `s |-> p(sigma)/2` in `Q[[sigma]]` or in `Q[sigma]/(sigma^N)`;
- the truncation `Q[[sigma]] -> Q[sigma]/(sigma^N)`.

Homomorphisms commute with one another, so substituting a moving connection and then reducing modulo a sigma ceiling is the same as reducing first and then applying the finite matrix. No additional commutation hypothesis is required, and the identity does not become an asymptotic statement.

The Cauchy product of `W` with `Phi` is exactly `[x^M](W Phi)`, i.e. the claimed linear combination of odd rows. Convolution in the ordinary index does not add terms and does not move the vanishing. Convolution in `sigma`, coming from series coefficients of `w_j(p(sigma))`, is likewise the image of the same polynomial under `s |-> p(sigma)/2`. Linearity in `Y` means sums of pole-`<=r` terms still die. A pointwise product of two Laurent series adds pole orders and is a different operation: if `q_1+q_2>r` that product need not be annihilated, and the theorem does not claim that it is.

---

## 7. Miner, dual AWS, and composed inventory

Independent recomputation of the nested loops in `odd_pole_recurrence_miner.py` with `--max-terminal 24` gives

```text
38,024 Laurent-to-Faber transform checks,
17,550 q<=r annihilation checks,
   300 first-outside-pole sharp negative controls,
    24 terminal-pole negative controls,
```

matching both V2 `result.json` files. The annihilation count is the hockey-stick evaluation `C(27,4)=17550`; the sharp count is `sum_{M=1}^{24} M=300`. Every annihilation in that range is the zero `Q`-scalar; every first-outside control equals `(-1)^{M-r}` as the scalar of `s^{M-r}`; every terminal control equals `1`. Both row-seven `s`-vectors match §5. No failing tuple `(M,r,q,e,row)` exists in the charged grid. The grid remains a software control of the identity in §3.

The `F_65521` lane is not a native modular engine. It runs the same `fractions.Fraction` arithmetic and then reduces. All denominators in the `W` and closed-`Phi` coefficients for `M<=24` are of the form `2^a n!` with `n<=24`, hence invertible modulo the prime `65521>24`. Dual-host agreement is therefore automatic once the `Q` identities hold. That is acceptable for a software control of a characteristic-zero theorem; it is not a second proof. Distinct hosts, PIDs, RSS, wall-clock, stderr digests, and characteristic tokens are genuine custody that V2 ran twice.

The miner, when given the frozen inventory `884922fede59bc3540a61aa089a9ed92f65235b269330d63b9195afa69019297`, checks only:

- SHA of that file;
- `jet_maxima = {A:7, C:10, R:6, k10:6, k6:10, k2:6, p:10, mu20:10, mu4:6, mu6:2}`;
- every primitive family of `base_grade<=38` has `pole<=3`.

The file contains eleven primitive families, all with `base_grade<=36`, and the in-window maximum pole is three, attained by `k10 C^2` and `k2 C` at grade 36. The recorded first pole of order at least four is grade 43. The miner does not prove completeness of that list, does not re-expand the four source summands, and would still pass if a pole-one family were omitted. RESULT already says the inventory composition is not an independent completeness proof. That reading is enforced in §8.

Resource metadata in `AWS_LAUNCH_METADATA.md` matches the two GNU `time` transcripts: wall 1:11.36 / 1:11.13, RSS 31,960 / 31,656 KiB, swaps 0, cap 4 GiB, timeout 600 s, `rc=0`. Eight required stdout markers occur once each on both lanes. Those markers are not the theorem.

---

## 8. Firewall

The identity `[x^M](W_(M,r) Phi)=0` for pole order `<=r` is a linear syzygy among odd Faber rows. To apply it to a concrete source one must already know:

1. a complete pole ceiling `r` for that source, through the relevant grade;
2. which target monomials sit on which rows, so that the same combination of the full rows (source plus targets) can be evaluated.

Neither ingredient is proved here. The composed D1 `a=10` inventory SHA and its mechanical jet maxima are an input pin. Chart covers, fan covers, the square component, order two, maximum twelve, and JC2 are not so much as mentioned in the algebra of §§1–6, and RESULT does not claim them.

On `D(p)` the odd generating function is well-defined and the sharpness polynomial is nonzero. On `V(p)` the chart degenerates as in §4. Lifecycle opens `V(k0)` and every cell whose pole ceiling has not been certified remain outside the theorem.

---

## 9. Defect classification

No mathematical defect of the numbered claim was found. The generating transform, the odd proper-fraction basis, the degree identity, the sharpness polynomial, both row-seven specialisations, and the homomorphism argument for moving `p(sigma)` are independent of AWS markers and of the finite replay.

No custody defect of V2 was found. All named hashes match. V1 is fail-closed plumbing and is not charged. Exact Q and `F_65521` are distinct hosts with distinct PIDs, RSS, wall-clock, and characteristic tokens; the modular lane is a weaker software control than a native `F_65521` engine and is not used as a proof.

No scope wording defect that enlarges the theorem to an inventory, a D1 emptiness, order two, maximum twelve, or JC2 was found.

Smallest failing `(M,r,q,e,row)`: none.

Smallest basis exception: none.

CONFIRMED
