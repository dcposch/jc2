# Hostile different-model review — AS `B8` exact `(8,12)` `Z/27` survivor

| Field | Value |
|---|---|
| Producer | `xmodel/as-b8-max12-w3-survivor-aws-20260825.md` |
| Frozen case | `cases/as_b8_max12_w3_gate_aws_20260825/` |
| Terminology erratum | `xmodel/ideation-20260825T1550Z-cube-terminology-erratum.md` |
| Overall verdict | **CONFIRMED** |
| Mathematics | **CONFIRMED** |
| Source typing | **CONFIRMED** (non-blocking labels only) |
| Software | **CONFIRMED** (RREF rank is dual-AWS plus code audit; particular digits are independent) |
| Custody | **CONFIRMED** of the frozen two-host V2 AWS run; V1 is a genuine negative control |
| Wording / scope | **CONFIRMED.** Finite-depth firewall is load-bearing and correct |
| Mathematical defects | none |
| Terminology / custody / exposition defects | non-blocking only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Evidence | no-shell source review: hand algebra in `Z[x,y]` and `F_3`, integer sample points, full `F_3^2` census, RREF code audit, byte comparison of dual-host stdout, internal FREEZE/MANIFEST/SOURCE hash DAG. No Bash, Python, CAS, or solver on the local Mac; `replay_v2.py` was not executed locally |
| Git HEAD | `d0f6edfbfcd8fbe4c77ffadcd336df349c11eb7e` (`refs/heads/master`) |
| Review window | 2026-08-25 |

## Verdict

**CONFIRMED**

The integer pair is exactly as written. The source automorphism `B8`, the determinant-one target reorder `T8`, and the residue map `G8=T8∘A∘B8` are right-compositions, not group conjugates. The transported operator `D8` equals the direct Jacobian linearization on `F_3`, including the characteristic-three identity that produces `+R_y`. The V2 envelope `81+91=172` with `276` determinant rows is the complete monomial window for actual degrees `(8,12)` inside total D12. The displayed W2/W3 digits satisfy the Cartier equations by direct substitution. The exact divided residual is `-u^4+9u^2 y^8-3y^8`, whose negative is `u^4` modulo three. The parent W2 point fails modulo 27, and the W3 point satisfies `det J(P,Q)≡1 (mod 27)` by an exact integer identity, independently sampled at four `Z`-points. Actual total and partial-`y` degrees are `(8,12)` with unit leading `y` faces. Reduction modulo 3 is `G8`. The special fibre is noninjective. V1 is a real degree-overflow negative control, not a suppressed success. Dual-AWS V2 stdout is byte-identical. This is one explicit fixed-support determinant-one point over `Z/27`. It is not a complete predecessor family, inverse limit, `Z_3` or characteristic-zero map, maximum-twelve theorem, counterexample, selected Q8/TD6 object, or JC2.

## Strongest exact claim

Let `u=x+y^4` in `Z[x,y]`. The tame elementary automorphism `B8=(u,y+u^2)` has Jacobian determinant `1` and inverse `y=t-s^2`, `x=s-(t-s^2)^4`. The target reorder `T8(s,t)=(t,-s)` has Jacobian determinant `1`. Over `Z`,

```text
G8 = T8 ∘ A ∘ B8 = (y+u^2, u^3-u),    A(s,t)=(s-s^3,t),
```

and `det J(G8)=1-3u^2`. Over `F_3` this is etale of actual partial-`y` and total degrees `(8,12)` and `(8,12)`, with unit leading `y` coefficients `(1,1)`, and is not injective. It is an integral right-composition / source transform of the Artin–Schreier seed, not the conjugate `B8^{-1}∘A∘B8`.

In the complete degree-compatible envelope

```text
R: i+j≤12 and j≤8     (81 slots),
S: i+j≤12 and j≤12    (91 slots),
```

with every determinant coefficient of total degree at most 22 (276 rows), the deterministic zero-free-variable W2/W3 digits

```text
R2 = 2 x y^5 + x^2 y,     S2 = 0,
R3 = 2 x y^6 + x^3 y^5 + x^4 y,     S3 = x y^9
```

produce the integer pair

```text
P = y + u^2 + 3(2 x y^5 + x^2 y) + 9(2 x y^6 + x^3 y^5 + x^4 y),
Q = u^3 - u + 9 x y^9
```

which satisfies `det J(P,Q) ≡ 1 (mod 27)`, has the same actual degree pair `(8,12)`, and reduces modulo 3 to `G8`. The W2 truncation `(P2,Q2)=(P0+3R2,Q0)` has exact divided residual

```text
(det J(P2,Q2)-1)/9 = -u^4 + 9 u^2 y^8 - 3 y^8
```

and is not determinant one modulo 27. Omitting the full `9`-digit therefore fails the W3 gate. This is one explicit fixed-support determinant-one point over `Z/27` on the `(8,12)` checksum face.

## Sharpest non-claim

One finite-depth point over `Z/27` in one 172-slot envelope. Not a classification of the 68-dimensional linearized kernel, not a compatible `Z/81` or all-depth tower, not a `Z_3` or characteristic-zero polynomial map, not a Keller counterexample, not a maximum-twelve theorem, not selected Q8 or TD6, not a group conjugate of `A`, and not a resolution of JC2.

---

## 1. Source maps, orientation, and composition

`u=x+y^4` is triangular of Jacobian `1`. In source coordinates `(u,y)`,

```text
B8 = (u, y+u^2),     ∂(B8)/∂(x,y) has determinant
1·(1+8 u y^3) - 4 y^3 · 2u = 1.
```

`T8(s,t)=(t,-s)` has matrix `[[0,1],[-1,0]]` and determinant `1`. The minus is load-bearing: without it, `det J` of the residue map would be `3u^2-1 ≡ -1 (mod 3)`, a unit but not `1`. With it,

```text
A∘B8 = (u-u^3, y+u^2),
T8∘A∘B8 = (y+u^2, -(u-u^3)) = (y+u^2, u^3-u) = G8
```

already over `Z`. This is right-composition, equivalently an integral source transform, matching the `20260825T1550Z` terminology erratum. Independently, `B8^{-1}∘A∘B8` is a different pair.

Write `P0=y+u^2` and `Q0=u^3-u`. Binomial expansions, with mixed terms retained,

```text
u^2 = x^2 + 2 x y^4 + y^8,
u^3 = x^3 + 3 x^2 y^4 + 3 x y^8 + y^{12}.
```

The source guards `P0[(1,4)]=2` and `Q0[(2,4)]=Q0[(1,8)]=3` are exactly those mixed terms. Replacing `u^3` by the characteristic-three Freshman form `x^3+y^{12}` changes the Jacobian already modulo 27. Direct `(x,y)` partials give

```text
P0_x = 2u,                  P0_y = 1 + 8 u y^3,
Q0_x = 3u^2 - 1,            Q0_y = 4 y^3 (3u^2 - 1),
det J(P0,Q0) = 1 - 3 u^2,
```

so `G8` is etale over `F_3` and not etale over `Z`. The producer’s etale/noninjective sentence sits under the opening `Over F_3` block; that scoping is correct.

## 2. Envelope completeness

Monomials `x^i y^j` with `i+j≤12` number `sum_{d=0}^{12}(d+1)=91`. Restricting the first coordinate by `j≤8` leaves

```text
sum_{j=0}^{8}(13-j) = 13+12+…+5 = 81,
```

or equivalently 45 monomials of total degree `≤8` plus 9 monomials in each of degrees 9 through 12 with `j≤8`. All 276 positions of total degree `≤22` are `sum_{d=0}^{22}(d+1)=276`. Derivatives of two total-degree-12 maps have degree at most 11, so the Jacobian determinant cannot grow a coefficient outside those 276 rows. The image of `D8` on this envelope has total degree at most 18, well inside the row window. No omitted determinant row, and the 81-slot count is not a false 91-per-coordinate leftover.

The envelope is source-complete for actual degrees `(8,12)`: any pair of total degree `≤12` with first-coordinate `y`-degree `≤8` uses only these monomials. A degree-13 digit cannot cancel against `P0` or `Q0`, which already have degrees `≤8` and `≤12`. The ten excluded first-coordinate slots are exactly `j∈{9,10,11,12}` with `i+j≤12`; they are the V1 overflow room.

## 3. Transported operator

The ε-linearization of `det J(P0+εR, Q0+εS)` is `J(P0,S)+J(R,Q0)`. Reducing the partials of §1 modulo 3, using `u_y=4y^3≡y^3` and not the illicit `u_y=0`,

```text
P0_x ≡ 2u,     P0_y ≡ 1+2 u y^3,
Q0_x ≡ -1 ≡ 2, Q0_y ≡ -y^3,
```

hence

```text
J(P0,S)+J(R,Q0)
  ≡ 2u S_y - (1+2 u y^3) S_x - y^3 R_x - 2 R_y
  ≡ -y^3 R_x + R_y - (1+2 u y^3) S_x + 2u S_y  (mod 3),
```

because `-2≡1`. That last identity is characteristic three, not a characteristic-zero formula. The displayed `D8` therefore equals the direct Jacobian on every basis column as a corollary of the operator identity; the V2 loop that asserts the two formulae on all 172 columns is checking this identity, not discovering 172 accidents. No sign error from `T8`: the `+R_y` term is exactly `Q0=u^3-u` rather than `u-u^3`. No dropped `u_y` after `u=x+y^4`.

## 4. W2 digit, divided residual, W3 digit

**W2.** `R2=x^2 y+2 x y^5`, `S2=0`. Then over `F_3`

```text
R2_x ≡ 2 x y + 2 y^5,     R2_y ≡ x^2 + x y^4,
D8(R2,0) = -y^3 R2_x + R2_y
         ≡ x^2 + 2 x y^4 + y^8
         = u^2.
```

This `R2` is the truncation of the V1 structured point `u^2 y=x^2 y+2 x y^5+y^9` into `j≤8`. The omitted monomial is in the kernel: `D8(y^9,0)≡0` because `9y^8≡0`. So V2 does not assume V1; it recovers the unique degree-compatible part of that structured point.

**Exact residual.** Write `P2=P0+3R2=y+u^2(1+3y)-3y^9` and `Q2=Q0`. In `(u,y)` coordinates, whose Jacobian over `(x,y)` is 1, the parent without the `-3y^9` term has

```text
det J(y+u^2+3 u^2 y, u^3-u) = 1 - 9 u^4.
```

The perturbation `ε=-3`, `R=y^9` does not change `P_x` (`R_x=0`) and adds `ε·9 y^8` to `P_y`, so

```text
det J(P2,Q2) = 1 - 9 u^4 + 27 y^8 (3u^2-1)
             = 1 - 9 u^4 + 81 u^2 y^8 - 27 y^8.
```

Dividing by 9 and expanding `-u^4` binomially produces exactly the printed `E2`:

```text
-3 y^8 + 8 y^{16} + 14 x y^{12} + 3 x^2 y^8 - 4 x^3 y^4 - x^4.
```

Modulo 3 this is `-u^4`, so `-E2≡u^4`. Modulo 27 the extra terms vanish and `det2≡1-9u^4`, which is not `1`. The parent-without-W3 negative control is an identity, not a solver flag.

**W3.** `R3=2 x y^6+x^3 y^5+x^4 y`, `S3=x y^9`. Over `F_3`, `S3_y≡0` and

```text
D8(R3,S3) ≡ x^4 + x^3 y^4 + x y^{12} + y^{16} ≡ u^4,
```

using `4≡1` and `6≡0` in the binomial of `u^4`, not Freshman’s dream over `Z`. All four monomials of `(R3,S3)` lie in the 172-slot envelope.

## 5. Determinant modulo 27, degrees, reduction

```text
det J(P2+9 R3, Q2+9 S3)
  = det2 + 9(J(P2,S3)+J(R3,Q2)) + 81 det J(R3,S3).
```

The quadratic `81`-term vanishes modulo 27. The linear form equals `D8(R3,S3)` plus `3 J(R2,S3)`, so

```text
9 Lin ≡ 9 u^4  (mod 27).
```

With `det2≡1-9u^4 (mod 27)` this cancels to `1`. That is an integer polynomial identity modulo 27, not a reduction of a characteristic-three Frobenius Jacobian.

Expanded pair, every mixed binomial kept:

```text
P = x^2 + 3 x^2 y + 9 x^4 y + 2 x y^4 + 6 x y^5 + 18 x y^6 + 9 x^3 y^5 + y + y^8,
Q = -x + x^3 - y^4 + 3 x^2 y^4 + 3 x y^8 + 9 x y^9 + y^{12}.
```

Actual `y`-degrees `(8,12)` from unit faces `y^8` and `y^{12}`; actual total degrees `(8,12)` from those same faces and `x^3 y^5`. No term of `P` has `y`-degree above 8; no term of either coordinate exceeds total degree 12; no overflow is hidden inside powers of `u`. Reduction modulo 3 drops every coefficient divisible by 3 and returns `P0,Q0`. Independent integer samples of `det J(P,Q)`:

| `(x,y)` | `det` | `mod 27` |
|---|---:|---:|
| `(0,0)` | `1` | `1` |
| `(1,0)` | `-26` | `1` |
| `(0,1)` | `109` | `1` |
| `(1,1)` | `7885` | `1` |

At `(1,0)` the parent `(P2,Q2)` has determinant `-8≢1 (mod 27)`.

## 6. Special fibre, V1 negative control, rank

On `F_3^2`, with `y^4≡y^2` only as functions, `u^3-u` vanishes by Fermat, so `G8` lands on the line of second coordinate `0`. The nine source points and images are

| image | sources |
|---|---|
| `(0,0)` | `(0,0),(0,2),(1,2)` |
| `(1,0)` | `(1,0),(2,0),(2,1)` |
| `(2,0)` | `(0,1),(1,1),(2,2)` |

The displayed collision `(0,0),(1,2)↦(0,0)` is correct. It is an existence witness, not a claim that the fibre has size two; the cube report already listed the third point `(0,2)`. Over `Z/27` that collision is not claimed and is not needed.

V1 used all 182 total-D12 slots and the structured point `R2=u^2 y`, which already contains `3y^9` in `P2`. A `9`-digit cannot cancel a coefficient-`3` term, so `dydeg(P3)≥9`. Both hosts hit

```text
assert (dydeg(P3), dydeg(Q3)) == (8, 12)
AssertionError
```

after the determinant-mod-27 assert had already passed. Empty `replay.stdout` (SHA-256 `e3b0c442…` of the empty file), `time -v` exit status 1, Box02 RSS 30,040 KiB. V1 is therefore a genuine `(8,12)` failure and a genuine D12 determinant-one overflow, and is correctly excluded from every positive theorem. Its launcher wrote PID `0` and a newline-only `runner.rc` (SHA-256 `01ba4719…` of `'\n'`); that is a routing defect of the negative control only.

Rank 104 and nullity `172-104=68` are the dual-AWS RREF counts. The particular digits were not taken on trust: they satisfy the Cartier equations by the substitutions of §4. The RREF implementation is ordinary `F_3` Gaussian elimination with pivot scaling by `2` (self-inverse), free variables held at 0, and a consistency check. This review did not re-run that 276-by-172 elimination. Nullity 68 is a linearized dimension, not a classified scheme.

## 7. Hashes, AWS, replay

V2 was registered at `2026-08-25T16:21:28Z`, after V1 failed at `16:19:27Z` and before V2 execution. Timeline:

| event | UTC |
|---|---|
| V1 registration | `16:17:12Z` |
| V1 Box02 end (fail) | `16:19:27Z` |
| V2 registration | `16:21:28Z` |
| V2 Box02 end | `16:23:21Z` |
| V2 Box03 end | `16:23:25Z` |

Both V2 hosts ran `timeout 1800 python3 replay_v2.py` under Python 3.12.3, rc `0` (`runner.rc` is the well-known digest `9a271f2a…` of `'0\n'`), wall time `0.04s`, RSS 15,616 / 15,784 KiB. Both source-checks printed `REGISTRATION_V2.md: OK` and `replay_v2.py: OK`. The two `replay.stdout` files are byte-identical by direct read, both terminating at

```text
payload_sha256=5c9219e497e7cc14017a9fefc395aaaddcf420ccb8911b0db77c9b0b6985384f
AS-B8-MAX12-W3-SURVIVOR PASS
```

and both printing `R2=[[1,5,2],[2,1,1]]`, `S2=[]`, the six-term `E2`, `R3=[[1,6,2],[3,5,1],[4,1,1]]`, `S3=[[1,9,1]]`, degrees `8,12`, `parent_without_9_digit_fails_mod27=true`, and `determinant_mod27=1`. Stderr hashes differ only in host-specific `time -v` fields. Printed digits match the independent algebra of §§4–5. The payload JSON digest was not locally rebuilt (no-shell policy); it is dual-AWS identical.

Recorded hash DAG is internally consistent:

- `SOURCE_V2.sha256` cites `REGISTRATION_V2.md` `cff36025…` and `replay_v2.py` `691c89fc…`;
- `FREEZE.sha256` recites that same `SOURCE_V2.sha256` file digest `0c735bc5…`, the same `replay_v2.py` digest, both stdout digests `68bb9358…`, the producer report, and the terminology erratum;
- `MANIFEST.sha256` recites the same `SOURCE_V2` / `replay_v2.py` / stdout digests and the V1 negative-control tree;
- evidence copies of `SOURCE_V2.sha256` on Box02/Box03 match the case root.

Local `sha256sum` recomputation was not run. Dual-AWS `sha256sum -c SOURCE_V2.sha256` is the custody check that was run.

## 8. Terminology and scope

The producer constructs `G8` by `T8∘A∘B8` and titles the object “AS-source-transformed”, which is the erratum’s replacement for the cube report’s “right-conjugates”. Registration, README, and body refuse selected Q8, TD6, inverse limits, `Z_3`, characteristic zero, nonautomorphy, both maximum-twelve frontiers, counterexample, and JC2. “Complementary primitive maximum-twelve residue seed” and “finite branch” are checksum-face names plus a finite Hensel step, not a maximum-twelve theorem and not an inverse system. The `(8,12)` face is one of the two primitive characteristic-zero maximum-twelve *checksums*; that is a name for the degree pair. The next licensed producer gate is the complete W4 digit over this frozen W3 point in the same 172-slot envelope. A survivor there would still be finite-depth evidence only; an obstruction would kill only this point unless globalized over the W2/W3 kernel scheme.

## Mathematical defects

None.

## Source typing, software, custody, or wording defects (non-blocking)

1. Replay prints `source_reduction=B8`. The asserted reduction is to `G8=T8∘A∘B8`. Harmless label; the load-bearing asserts compare `P3,Q3` to `P0,Q0` modulo 3.
2. Empty `launcher.stdout` / `launcher.stderr` on both V2 hosts. Two-host identity is carried by `replay.stdout`, `runner.rc=0`, distinct `time -v` RSS, and distinct internal hostnames `ip-172-30-0-186` / `ip-172-30-0-249`.
3. `start.utc` equals `end.utc` on each V2 host, consistent with a 0.04s job written to one-second resolution; duration lives in `time -v`, not in those stamps.
4. Fibre witness lists two of the three `F_3`-preimages of `(0,0)`. Existence is correct; completeness of the special-fibre census is not claimed.
5. Rank/nullity `104/68` and the payload SHA-256 are dual-AWS plus code audit, not a second local engine. The displayed particular solution is independently substituted.
6. Cube-owner language “right-conjugates” / “AS-conjugate” remains in the sealed `1550Z` report and is already covered by the frozen terminology erratum. The producer under review does not repeat that slip.

None of these defects changes an identity or licenses a broader claim.

---

**Mathematics: CONFIRMED.**  
**Source typing: CONFIRMED.**  
**Software: CONFIRMED.**  
**Custody: CONFIRMED.**  
**Wording / scope: CONFIRMED.**

**Overall: CONFIRMED**
