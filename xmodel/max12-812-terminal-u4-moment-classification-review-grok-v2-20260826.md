# Hostile review — complete `U=4` terminal moment classification (`m=2,4`)

| Field | Value |
|---|---|
| Target | `cases/max12_812_terminal_u4_moment_classification_20260826/` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks the registered `U=4` census |
| Smallest counterexample / repair | none |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. The charged `U=3` review is same-model and is not used as a PASS/CONFIRMED certificate; the logarithmic derivative `T'/T=kappa/P=sum n_i/(x-c_i)`, vanishing of power sums through degree `U-2`, `kappa=sum n_i c_i^{U-1}`, the converse reconstructing coprime monic `A,B` with `deg(A-B)=D-U+1` and `A-B` squarefree, the degree box `U-1<=D<=m(U-1)`, exactness `gcd(m, all n_i)=1`, and the radicand exponents `m-alpha` / `m+beta` are taken as the *statements* of the charged theorem, then every `U=4` identity, profile, affine quotient, and listed class below is re-derived from those statements plus the frozen bytes |
| Method | source reading, hash recomputation, complete JSON inspection, and hand derivation only; no enumerator execution, no Singular, no Lean, no Sage, no local quadratic-field replay of `enumerate_u4.py` |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `574e873d4753b57dbaeb0fb83e320fbef3694724` (frozen case uncommitted) |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of every required pin matches the V2 launch list recorded below. The two charged-parent hashes named in this prompt supersede the mistyped pair in the canceled V1 prompt; the frozen parent bytes match the V2 pins, not the V1 typos. Producer summary language, the AWS `U4_TERMINAL_MOMENT_CLASSIFICATION_PASS` token, the coordinator narrative, and the un-preregistered `5/44` counts were not used as evidence. No file other than this review was written. The frozen case was not edited.

---

## Verdict

The frozen AWS census is the complete affine classification of exact-order `m in {2,4}` terminal moment configurations at `U=4`. Independently: after sending two labelled support points to `0,1`, the remaining two moment equations are a linear formula for `y` and a genuine quadratic in `x` whose discriminant is `4 n_1 n_2 n_3 n_4`; the linear branch `n_1+n_2=0` is a gauge artefact that never fires under the code's same-sign placement of the first two weights, and is already captured as a quadratic (often rational) solution in the complementary labelling; the degree-three moment is the Vandermonde leftover, hence nonzero on four distinct nodes. The unordered signed profiles with `3<=D<=3m`, positive parts at most `m`, unrestricted positive pole parts, and `gcd(m, parts)=1` are exactly five at `m=2` and thirty-six at `m=4`, with a unique empty profile `(3,3|-3,-3)`. Affine canonicalization over all twelve ordered normalization pairs, followed by sorting `(weight, coordinate-key)`, merges Galois conjugates precisely when a same-sign permutation is realized by an affine map, and keeps them as two classes over the algebraic closure when all same-sign variable weights are distinct; the representation key cannot identify two inequivalent weighted 4-tuples. Every retained class is a collision-free root of that quadratic, so the charged converse already supplies coprime monic `A,B`, `deg(A-B)=D-3`, squarefreeness, Wronskian constant `kappa`, and radicand exponents; the engine certificates are redundant given those identities, and the hand-checked samples agree. The test `3*gcd(parts)<=D` is the correct necessary Boccara--Zannier count of edges after scaling, used only as a fail-closed Boolean checksum, never as a generator of the class totals. The independently recounted totals are `m=2`: 5 tested / 5 viable / 5 affine classes (1 rational, 4 quadratic) and `m=4`: 36 tested / 35 viable / 44 affine classes (5 rational, 39 quadratic). A clean r6d replay with matching source hash, rc 0, empty stderr, 8 GiB cap unused, and zero swap is engine evidence that the closed form was evaluated; it is not a substitute for the derivation that the quadratic plus the profile list is exhaustive. This is only the `U=4` terminal differential equation.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `cases/.../REGISTRATION.md` | `cfbd82dd8e03aa5f7c753e442e9994b011a2fa1fe1e0bdeea197a9663570e354` | preregistration (matches required pin; counts not predicted) |
| `cases/.../enumerate_u4.py` | `31f9b51beca1702ba23443ced509350d7769c2ef52dad5a62051e33883c347ae` | enumerator source (matches pin and AWS `source_sha256`) |
| `cases/.../run_aws.sh` | `d98fdd62620c5419a07208aedae71b17e074653f79abc5c0edae11a169760c1d` | AWS gate, `ulimit -v 8388608`, 600s timeout (matches pin) |
| `cases/.../launch_remote.sh` | `9dbdb7ae1d8668924c25eef553840e8c4325d7ab5557ae36becdf1bc7218a1e5` | remote wrapper (matches pin) |
| `cases/.../aws_r6d/output/classes.json` | `8719cb71fa2e70d2aa11e20243e252fafd7e0aad2ef782449faff754fac143ee` | census payload (matches pin, stdout `payload_sha256`, and `classes_sha256`) |
| `cases/.../aws_r6d/output/stdout` | `e3bca8cfb7ad028dcfc61e28be142db47591f4651b13e61264759d51d2836f78` | job log (matches pin; identical to `launcher.stdout`) |
| `cases/.../aws_r6d/output/stderr` | `e3b0c44298fc1c149afbf4f8996fb92427ae41e4649b934ca495991b7852b855` | empty file; SHA-256 of the empty byte string (matches V2 pin) |
| `xmodel/max12-812-terminal-logderivative-pte-u3-classification-20260826.md` | `8e1535aac96785ecf72df6ed22cdd239031d89d82e84fbe0d2078ce6b786c5dc` | charged theorem (matches V2 pin; supersedes the canceled V1 typo) |
| `xmodel/max12-812-terminal-logderivative-pte-u3-review-grok-20260826.md` | `91772fd704b7622da3367810101f0efb171594222b8696d241a6b76682c07c20` | same-model audit of the charged theorem (read; unused as a verdict; matches V2 pin) |

`FREEZE.sha256` records only the four source files and matches those four hashes. Output hashes are not in the freeze file; they are the V2 prompt pins, and they match the frozen bytes. The canceled V1 prompt named two wrong charged-parent hashes and a mistyped empty-stderr nibble; those strings are not used here.

The charged theorem is consumed only for: `T'/T=kappa/P=sum n_i/(x-c_i)`; vanishing of `sum n_i c_i^k` for `0<=k<=U-2`; `kappa=sum n_i c_i^{U-1}!=0`; the converse constructing coprime monic `A,B` of common degree `D` from distinct nodes and nonzero signed weights; `deg(A-B)=D-U+1` with `A-B` squarefree; the box `U-1<=D<=m(U-1)`; exactness `gcd(m, all n_i)=1`; and radicand exponents `m-alpha` at a zero of `T` and `m+beta` at a pole. Its `U=3` lists are not an input to any `U=4` count. No scope-firewall sentence of either parent is an input.

---

## Strongest exact theorem that survives

Let `L` be a characteristic-zero field after the already licensed finite constant extension. Let `m in {2,4}` be the exact Kummer order, and let `U=4`. A signed multiplicity profile is an unordered pair of partitions `(alpha, beta)` of a common integer `D` with `3<=D<=3m`, `r=len(alpha)>=1`, `s=len(beta)>=1`, `r+s=4`, every `alpha_i` in `{1,...,m}`, every `beta_j>=1`, and `gcd(m, all alpha_i, all beta_j)=1`. Write `n=(alpha, -beta)`.

After an affine source change sending two labelled support points to `0` and `1`, the remaining support `(x,y)` is given by

```text
y = (n2 + n3 x) / (n1 + n2 + n3),
n3(n1+n2) x^2 - 2 n2 n3 x + n2(n1+n3) = 0,
disc = 4 n1 n2 n3 n4.
```

The quadratic is never identically zero on a nonzero integer 4-tuple. Over an algebraic closure there are therefore at most two roots. A root is retained if and only if `{0,1,x,y}` are four distinct points. Two retained roots determine the same affine class if and only if some affine map `z |-> p z + q` with `p!=0` together with a permutation of equal-weight same-sign points identifies their weighted 4-tuples; otherwise they are two classes over the algebraic closure. Galois conjugation is not an additional identification.

The exact lists are:

- `m=2`: five profiles, five affine classes, of which one is rational (`(2,1|-2,-1)` at `(0,1,2/3,-1/3)`) and four are quadratic.
- `m=4`: thirty-six profiles, one empty (`(3,3|-3,-3)`), forty-four affine classes, of which five are rational (the self-dual 2+2 profiles with `alpha=beta` and `alpha_1!=alpha_2`) and thirty-nine are quadratic. Nine profiles contribute two classes each, all of them the two square-root signs on a 4-tuple of pairwise distinct same-sign variable weights.

Every retained class has moments of degrees `0,1,2` equal to zero, nonzero degree-three moment `kappa`, coprime monic `A,B` reconstructed by the charged converse, `deg(A-B)=D-3`, `A-B` squarefree, Wronskian `A'B-AB'=kappa prod (X-c_i)^{|n_i|-1}`, and radicand exponents `m-n_i` (equivalently `m-alpha` or `m+beta`) summing to `4m`. Existence of a collision-free root agrees with the necessary weighted-tree inequality `3 gcd(parts)<=D`; that inequality is not used to produce the class count.

This is only the terminal differential equation at `U=4`. It does not produce another Faber tail, Taylor polynomiality, a Keller pair, a whole Kummer leaf, `(8,12)`, a bound on all `U`, or JC2.

---

## Attack 1 — normalized `U=4` moment equations

**CONFIRMED.** The quadratic, the discriminant `4 n1 n2 n3 n4`, the linear branch, and nonvanishing of the degree-three moment all survive.

Place the four distinct nodes at `(0,1,x,y)` with nonzero integer weights `(n1,n2,n3,n4)` summing to zero. Characteristic zero is standing. The charged identities at `U=4` are

```text
n1+n2+n3+n4 = 0,
n2 + n3 x + n4 y = 0,
n2 + n3 x^2 + n4 y^2 = 0,
kappa = n2 + n3 x^3 + n4 y^3 != 0.
```

The `k=0` equation is the profile constraint. The `k=1` equation solves for `y` because `n4 != 0`:

```text
y = -(n2+n3 x)/n4 = (n2+n3 x)/(n1+n2+n3).
```

The denominator is `-n4`, never zero. Substitute into `k=2`, write `S=n1+n2+n3=-n4`, and clear `S^2=n4^2`. Dividing the leftover factor `n4` produces

```text
n3(n3+n4) x^2 + 2 n2 n3 x + n2(n2+n4) = 0.
```

The sum-zero relations `n3+n4=-(n1+n2)` and `n2+n4=-(n1+n3)` convert this into the monic-in-spirit quadratic used by the enumerator

```text
n3(n1+n2) x^2 - 2 n2 n3 x + n2(n1+n3) = 0.                 (Q)
```

Its discriminant expands as

```text
(-2 n2 n3)^2 - 4 n3(n1+n2) n2(n1+n3)
  = 4 n2 n3 [ n2 n3 - (n1+n2)(n1+n3) ]
  = -4 n1 n2 n3 (n1+n2+n3)
  = 4 n1 n2 n3 n4.
```

All four weights are nonzero integers, so the discriminant is a nonzero integer. Over an algebraic closure there are two roots, except on the linear locus `n3(n1+n2)=0`. The factor `n3` is nonzero, so that locus is exactly `n1+n2=0`. Then `n3+n4=0` as well, the linear coefficient `-2 n2 n3` is nonzero, and there is a unique rational

```text
x = -c/b = (n1+n3)/(2 n3).
```

Under the enumerator's labelling, the first `r` weights are the positive parts and the rest are the negative parts. For `r>=2` the first two weights are both positive, so `n1+n2=D!=0`. For `r=1` one has `n1=D` and `n2=-beta_1` with `beta_1 <= D-2`, so `n1+n2>=2`. The linear branch is therefore dead in this gauge. It is not a missing family: a configuration whose canceling pair sits at `{0,1}` is the same geometric 4-tuple after sending two same-sign points to `{0,1}`, where (Q) is a genuine quadratic (and is often a perfect square). The implementation still contains the linear formula; that is defensive, not a second census.

If all four moments of degrees `0` through `3` vanished, the Vandermonde matrix on four distinct nodes would force `n=0`. Distinctness plus nonzero weights therefore imply `kappa != 0` with no extra hypothesis. Collision with `{0,1}` or `x=y` is a genuine degeneration to fewer than four support points and is correctly discarded.

**What would have flipped this attack.** Expanding at the origin rather than at infinity; taking `P` non-monic so that the leading coefficient of `kappa/P` is not `kappa`; a gauge in which `n1+n2=0` was treated as `0=0` (both `a` and `b` vanishing), which cannot occur for nonzero weights; characteristic dividing a weight so that a residue vanished.

---

## Attack 2 — profile exhaustiveness

**CONFIRMED.** No duplicate partition, no missing sign type, no extra gcd row, no `D` outside `3<=D<=3m`.

Sign types for four nonzero integers summing to zero are `r in {1,2,3}` zeros (equivalently `1`, `2`, or `3` poles). The generator `partitions(total, length, max_part)` emits each nonincreasing tuple of positive parts of the given length with each part at most `max_part` once: the first part runs downward from `min(max_part, total-length+1)`, and the tail is nonincreasing of maximum equal to that first part. Alpha is generated with `max_part=m`; beta with `max_part=D`, which is no restriction on a partition of `D`. Exactness is `math.gcd(m, *parts)!=1`, a skip, not a rewrite.

**`m=2`, box `3<=D<=6`.**

- `r=1`: alpha is a single part `D<=2`, incompatible with `D>=3`. Zero profiles.
- `r=2`: `(2,1|-2,-1)` at `D=3`; `(2,2|-3,-1)` at `D=4`. The sibling `(2,2|-2,-2)` has gcd `2` and is skipped. No alpha of length two and parts `<=2` exists for `D>=5`.
- `r=3`: `(1,1,1|-3)`, `(2,1,1|-4)`, `(2,2,1|-5)`. The vertex `(2,2,2|-6)` has gcd `2` and is skipped.

Five tested, five with `gcd=1`. JSON order is `r` then `D` then alpha then beta, and matches this list.

**`m=4`, box `3<=D<=12`.**

- `r=1`: `(3|-1,-1,-1)`, `(4|-2,-1,-1)`. Two profiles. Three distinct positive parts summing to `D<=4` is impossible (`1+2+3=6`), so this type never has three distinct pole weights in range.
- `r=2`: length-two alpha with parts `<=4` exists only for `D<=8`. Before the gcd filter there are twenty-two `(alpha,beta)` pairs; four fail exactness, namely `(2,2|-2,-2)`, `(4,2|-4,-2)`, `(4,4|-6,-2)`, `(4,4|-4,-4)`. Eighteen remain, including the empty `(3,3|-3,-3)`.
- `r=3`: the nonincreasing triples of parts in `{1,2,3,4}` are twenty tuples across `D=3..12`; four fail exactness, namely `(2,2,2|-6)`, `(4,2,2|-8)`, `(4,4,2|-10)`, `(4,4,4|-12)`. Sixteen remain.

Total tested: `2+18+16=36`. The gcd skips are exactly the profiles whose Kummer order divides `m` properly. No labelled pair `(2,1)` versus `(1,2)` is emitted twice. No fourth sign type exists.

**What would have flipped this attack.** Bounding pole parts by `m` (would drop `(1,1,1|-3)` at `m=2` and every `beta_j>m`); starting `D` at `2` (impossible: `deg(A-B)=D-3` would be negative); omitting `r=1` or `r=3`; treating `gcd(m, parts)=1` as `gcd(alpha)=1` only.

---

## Attack 3 — affine canonicalization and quadratic conjugates

**CONFIRMED.** Conjugates are merged over the algebraic closure precisely when an affine same-sign permutation identifies them, and are kept as two classes when the weighted 4-tuple is rigid. The representation key cannot merge inequivalent classes.

The affine group fixing infinity is `z |-> p z + q` with `p!=0`. It is the correct source automorphism: infinity is distinguished by `T(infinity)=1`. Any such map is uniquely determined by the images of two distinct points. Looping over the twelve ordered pairs of support points as the pair sent to `(0,1)`, then sorting the pairs `(weight, Quad.key())`, therefore produces every affine image in which two support points lie at `0` and `1`, written as an unordered weighted 4-tuple. The minimum of those twelve tuples is a complete invariant of the affine class of a labelled profile.

`Quad.key()` is `(d, a.numerator, a.denominator, b.numerator, b.denominator)` with `d` the squarefree radicand of the discriminant and `a,b` in lowest terms. A field element of `Q(sqrt(d))` has a unique such writing. If two retained roots produce the same canonical key, they determine the same weighted 4-tuple of field elements, hence the same class: there is no room for a false merge of inequivalent classes.

False separation is the remaining risk: two affinely equivalent roots whose keys differ. The connecting map is always among the twelve gauges, and arithmetic stays inside the same squarefree quadratic field, so the twelve-candidate sets coincide and the minima coincide. Empirically the merge-versus-split decision on the frozen JSON is exactly the weight-symmetry criterion:

- `r=2`, `alpha=beta`, `alpha_1 != alpha_2`: one root is `x=0` (because `n1+n3=0`), discarded; the other is rational. Five classes at `m=4`, one at `m=2`.
- `r=2`, all four absolute weights equal: both roots collide (`x=0` and `x=1`). This is `(3,3|-3,-3)` after the gcd filter. Empty.
- `r=2`, `alpha_1=alpha_2` or `beta_1=beta_2` but not all four equal: the two square-root signs are either `x |-> 1-x` (equal zeros) or the two pole positions of a single 4-tuple (equal poles). One class.
- `r=2`, four pairwise distinct parts: both signs survive and no affine map preserving weights connects them (the unique map sending the weight-`alpha_1` zero to `0` and the weight-`alpha_2` zero to `1` is the identity in this gauge). Two classes. These are exactly `(4,1|-3,-2)`, `(3,2|-4,-1)`, `(4,2|-5,-1)`, `(4,3|-6,-1)`, `(4,3|-5,-2)`.
- `r=3` or `r=1`: the discriminant is negative, so both roots are non-real and cannot collide with `{0,1}`. The condition `y=x` or `y in {0,1}` would force `x` rational, which it is not. Both roots are therefore collision-free. They merge if and only if at least two of the three same-sign variable weights are equal (an affine permutation of those points), and remain two classes if and only if those three weights are pairwise distinct. At `m=4` the distinct triples are exactly `(3,2,1)`, `(4,2,1)`, `(4,3,1)`, `(4,3,2)`. At `r=1` three distinct pole parts cannot sum to `D<=4`, so both `r=1` profiles have a repeated pole and class count one.

This is the same decision over `C` as over `Q(sqrt(d))`: orientation-reversing complex conjugation is not an affine map, but whenever the weights permit a same-sign permutation, an explicit `C`-affine map (for equal zeros, `z |-> 1-z`; for three equal zeros, multiplication by a primitive sixth root sending one equilateral triangle to the other as unordered sets; for equal poles, swapping the two pole coordinates) identifies the two signs. When the weights are all distinct, no such map exists.

Galois orbits are not quotiented, and should not be: the charged theorem works after a finite constant extension, and two conjugate points of the moment scheme with rigid weights are two geometric classes over the algebraic closure.

**What would have flipped this attack.** Quotienting by `Gal(Qbar/Q)` (would collapse the nine double profiles and report `35` classes at `m=4`); identifying `T` with `1/T` (would merge `(3,1|-2,-2)` with `(2,2|-3,-1)`); a key that stored a non-squarefree `d` or an unreduced `b`, permitting the same field element two writings; looping only over pairs of zeros rather than all twelve pairs.

---

## Attack 4 — exact quadratic arithmetic and certificates

**CONFIRMED.** Every registered identity follows from the charged converse on a collision-free root of (Q). Hand samples match the JSON, including both square-root signs, the linear-gauge-avoiding rational branch, and the empty profile.

`Quad` is `a+b sqrt(d)` with `d` squarefree, `d=0` the rationals, and `a,b` in `Q`. Addition, multiplication, inverse by the norm `a^2-d b^2`, and polynomial Euclidean algorithm are the standard quadratic-field operations. The inverse exists for a nonzero element because `d` is not a square in `Q`. Polynomial gcd over a field detects a common root in `C`. None of this was re-executed locally; it is read as an implementation of field arithmetic, and the identities it claims are the charged ones.

On any collision-free solution of the moments through degree `U-2` with nonzero integer weights, the charged converse already gives:

1. moments of degrees `0,1,2` vanish, by construction of (Q);
2. the degree-three moment is nonzero, by Vandermonde;
3. `A=prod_{n_i>0}(X-c_i)^{n_i}` and `B=prod_{n_i<0}(X-c_i)^{-n_i}` are coprime monic of degree `D`;
4. `deg(A-B)=D-U+1=D-3`;
5. `A-B` is squarefree (a nonzero constant, when `D=3`, included);
6. `W=A'B-AB'=kappa A B/P=kappa prod (X-c_i)^{|n_i|-1}`, so the quotient of `W` by that product is the constant `kappa` with the charged Wronskian sign;
7. radicand exponents `m-n_i`, summing to `4m`.

The enumerator's `verify_class` rechecks all seven and aborts the job on failure. The PASS token therefore means those asserts did not fire. Independently, the samples below were recomputed from (Q) by hand and agree with the frozen coordinates, fields, `kappa`, `difference_degree`, and radicand vectors. Because the certificates are theorems about any collision-free moment solution, a matching `(x,y)` is already a complete class; the engine gcd/Wronskian replay is belt-and-suspenders, not an extra mathematical hypothesis.

Squarefree decomposition of the discriminant folds even prime exponents into `outside` and leaves a squarefree (possibly negative) `d`. Perfect squares take the rational branch `d=0` with two (possibly colliding) rational roots. The identity `disc=4 n1 n2 n3 n4` was used as a read-side check on the implementation, not as an input to the samples.

**What would have flipped this attack.** Opposite Wronskian sign `AB'-A'B` (constant `-kappa`); omitting the constant-`G` edge `D=3` from squarefreeness; treating exponent-zero uncharged zeros as missing radicand factors in a degree count (they are present as `0` and the remaining parts still sum to `4m`); a zero of `A-B` at a support point, which the charged coprimality forbids.

---

## Attack 5 — Boccara--Zannier checksum `3 gcd(parts)<=D`

**CONFIRMED** as a necessary existence criterion and as a fail-closed Boolean equality. It is not a source of the `5/44` totals.

A weighted bicolored tree on `U=4` vertices has three edges. If `g=gcd(all vertex weights)`, every edge weight is a multiple of `g`, and scaling produces a tree of total weight `D/g` with three edges of positive integer weight, hence `D/g >= 3`, i.e.

```text
3 g <= D.
```

This is the `U=4` case of `(U-1) gcd(alpha_i, beta_j) <= D`. Necessity does not use Lu--Song, Boccara, or Zannier as black boxes: it is the edge count.

The enumerator solves every exact-order profile first, then asserts

```text
bool(collision-free affine classes) == (3 g <= D).
```

It does not skip a profile because the inequality fails, and it does not compare `class_count` to a tree-enumeration formula. A mismatch would have aborted the job; the PASS token means the Boolean equality held on all thirty-six `m=4` rows and all five `m=2` rows. That does not assume `44`.

Independently, `3g<=D` fails inside the exact-order box at exactly one tested profile: `(3,3|-3,-3)`, `g=3`, `D=6`, `9 ≰ 6`. For that profile (Q) is `x(x-1)=0`, both roots collide, and the JSON class list is empty. For every `r=1` and `r=3` profile, three positive parts summing to `D` and divisible by `g` force `D>=3g` automatically, so the inequality never fails on those types. For `r=2` the only exact-order all-equal 4-tuple in range is `(3,3|-3,-3)`; `(2,2|-2,-2)` and `(4,4|-4,-4)` are gcd-skipped. Sufficiency on the remaining profiles is not an input: it is the statement that (Q) has a non-colliding root, which Attack 3 proves by type (`r=1,3` both roots non-real; `r=2` self-dual unequal parts keep one rational; equal-weight empty is excluded; otherwise two real roots, and `y=x` is never a root because it would require a pole part equal to `D`).

Using the inequality as a count oracle for plane trees would be a different, stronger claim, and is not made. Plane-tree combinatorics can outnumber affine classes (labelled embeddings, orientations already identified by affine maps). The Boolean checksum is the correct load-bearing use.

**What would have flipped this attack.** Skipping profiles with `3g>D` before solving (would make sufficiency an unproved input); asserting `class_count` equal to a Lu--Song tree count; treating `3g<=D` as sufficient in general `U` without solving.

---

## Attack 6 — complete JSON, samples, totals, firewall

**CONFIRMED.** The frozen payload is one compact JSON object plus a trailing newline; its SHA-256 matches stdout. Independently recounted structure:

```text
m=2: 5 profiles, 5 viable, 5 classes (1 rational, 4 quadratic)
m=4: 36 profiles, 35 viable, 44 classes (5 rational, 39 quadratic)
empty profiles: 1, namely D=6 alpha=(3,3) beta=(3,3)
class_count=2 profiles: 9, contributing 18 of the 44
every radicand vector sums to 4m
every difference_degree equals D-3
every tree_exists flag equals 3 gcd(parts)<=D
no duplicate (alpha, beta, coordinates) record
```

Accounting of the forty-four `m=4` classes, not using the engine:

| type | profiles | doubles | singles | classes |
|---|---:|---:|---:|---:|
| `1+3` | 2 | 0 | 2 | 2 |
| `2+2` | 18 (1 empty) | 5 | 12 | 22 |
| `3+1` | 16 | 4 | 12 | 20 |
| total | 36 | 9 | 26 + 1 empty | 44 |

The five rationals are `(2,1|-2,-1)`, `(3,1|-3,-1)`, `(4,1|-4,-1)`, `(3,2|-3,-2)`, `(4,3|-4,-3)`. Each has `c=0` in (Q), one colliding root `x=0`, and surviving root `x=2 n2/D`.

Hand-checked samples, covering every branch named in the prompt:

**Rational `2+2`, `m=2` and `m=4`.** Weights `(2,1,-2,-1)`. Then `a=-6`, `b=4`, `c=0`, `disc=16`. Roots `x=0` (collide) and `x=2/3`. Then `y=-1/3`. Moments: `k=1` gives `1-4/3+1/3=0`; `k=2` gives `1-8/9-1/9=0`; `kappa=1-16/27+1/27=4/9`. Coordinates, field `d=0`, `kappa`, `difference_degree=0`, and radicands `[0,1,4,3]` at `m=2` and `[2,3,6,5]` at `m=4` match the JSON.

**Equal-zero quadratic, merged conjugates.** Weights `(2,2,-3,-1)`. Then `a=-12`, `b=12`, `c=-2`, `disc=48=16*3`. Roots `x=1/2 ± (1/6) sqrt(3)`. For the plus sign, `y=2-3x=1/2-(1/2)sqrt(3)`. The map `z |-> 1-z` sends this 4-tuple to the minus-sign 4-tuple and preserves the two weight-`2` zeros. One class, `d=3`. Direct expansion gives `kappa=(1/3)sqrt(3)`, matching the JSON.

**Empty profile.** Weights `(3,3,-3,-3)`. Then `c=0` and both roots of (Q) are `0` and `1`. No collision-free solution. `3g=9>6`. JSON `class_count=0`, `tree_exists=false`.

**Rigid `2+2`, two classes over the algebraic closure.** Weights `(4,1,-3,-2)`. Then `a=-15`, `b=6`, `c=1`, `disc=96=16*6`. Roots `x=1/5 ± (-2/15)sqrt(6)` in the code's sign convention, with `y=(1-3x)/2` equal to `1/5 ± (1/5)sqrt(6)` of opposite radical sign. Four distinct weights, both 4-tuples collision-free, two classes, `d=6`. Both JSON rows match, including both `kappa` signs.

**Equal-pole `1+3`, merged as one 4-tuple.** Weights `(4,-2,-1,-1)`. Then `disc=-32=16*(-2)`, roots `x=-1 ± sqrt(-2)`. The `y`-formula sends each root to the other, so the two signs are the two equal-weight poles of a single configuration `{0,1,-1+sqrt(-2),-1-sqrt(-2)}`. Vieta: `x+y=-2`, `xy=3`, `kappa=-2-(x^3+y^3)=-12`. JSON matches, one class.

**Three equal zeros, merged orientations.** Weights `(1,1,1,-3)`. Then `a=2`, `b=-2`, `c=2`, `disc=-12`. Roots `(1 ± sqrt(-3))/2`, the two points completing an equilateral triangle on `[0,1]`; `y` is the centroid. The affine map `z |-> tau-bar * z` sends one unordered triangle to the other. One class, `d=-3`. Directly `x^3=-1` and `y^3=-sqrt(-3)/9`, so `kappa=sqrt(-3)/3`, matching the JSON. The same support with weights scaled by `3` is the equality-case profile `(3,3,3|-9)` at `m=4`, `3g=D=9`, with `kappa` scaled by `3` to `sqrt(-3)`.

**Distinct-zero `3+1`, two classes.** Weights `(3,2,1,-6)`. Then `disc=-144`, `d=-1`, `x=2/5 ± (6/5)sqrt(-1)`, `y=(2+x)/6=2/5 ± (1/5)sqrt(-1)`. Three distinct zero weights, two classes. JSON matches.

Deduplication is per profile: `by_canonical` never compares distinct `(alpha,beta)`. Distinct profiles are distinct ramification types. Duals `(alpha,beta)` versus `(beta,alpha)` are `T` versus `1/T` and are correctly separate (the charged identity is not invariant under `T |-> 1/T`).

The strongest licensed statement is the theorem recorded above. The remaining firewall is: no other Faber tail, no Taylor polynomiality, no Keller pair, no source landing, no bound on `U`, no classification for `U>=5` (the moment system is then of degree `>=3` and is not this quadratic), no identification of affine classes with a plane-tree count, and no `(8,12)` or JC2 statement. Registration already refuses those promotions; the JSON `scope` string is `U=4 terminal moment equation only`; stdout does not name a lower tail.

**What would have flipped this attack.** A JSON class whose coordinates fail (Q) or collide; a second empty profile; a `class_count=2` row with a repeated same-sign weight; a radicand vector not summing to `4m`; a silent extra profile in the JSON not in the hand list.

---

## Attack 7 — AWS provenance

**CONFIRMED** as a clean implementation replay. Distinguished from the independent census proof in Attacks 1--6.

| Check | Frozen fact |
|---|---|
| Host | `ip-172-30-0-45`, `dmi=Amazon EC2`; `run_aws.sh` refuses non-Linux and non-Amazon |
| Tag | `max12_812_terminal_u4_moment_classification_20260826T024415Z_r6d` |
| Python | 3.12.3 (`math.gcd` with several arguments is licensed) |
| Source pin | stdout `source_sha256` equals the enumerator hash; the runner aborts on mismatch |
| rc | file `aws_r6d/rc` is `0`; `launch.meta` `launcher_rc=0`; `/usr/bin/time` exit status `0` |
| Diagnostics | job stderr empty; no traceback; PASS line present; tree/certificate asserts did not fire |
| Wall clock | `02:44:56Z` to `02:44:57Z`; `/usr/bin/time` elapsed `0:00.50`, user `0.49s` |
| Memory cap | `ulimit -v 8388608` (8 GiB); max RSS `19480` kB |
| Swap | `Swaps: 0` |
| Timeout | 600s with `TERM` then `KILL`; unused |
| Payload | stdout `payload_sha256` equals `classes_sha256` equals the JSON file hash |
| Stdout identity | `output/stdout` is byte-identical to `launcher.stdout` (the runner tees) |

The launch path in `launcher.stderr` is `/home/ubuntu/jobs/max12_812_terminal_u4_moment_classification_20260826T024415Z_r6d/...`, consistent with an r6d job root and not with a Mac path. Registration's fail-closed list (failed identity, criterion mismatch, Python exception, non-AWS host, missing tag, timeout, nonzero return) is the list of events that did not occur.

This is evidence that the frozen enumerator, with the frozen source hash, was executed once on AWS and wrote the frozen JSON. Completeness of the census is the closed-form quadratic plus the exhaustive profile list, not the fact that Python returned zero. A substantial rerun is not required for the identities and counts above. A rerun would be required only if the frozen bytes were disputed; they match every V2 pin.

**What would have flipped this attack.** Nonzero rc; nonempty stderr; source hash mismatch; a Mac `uname`; nonzero swap with the 8 GiB cap saturated; a `payload_sha256` disagreeing with the JSON file; absence of the registered PASS tag after a certificate failure that was then ignored.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | After gauge `(0,1,x,y)`, `y` is linear in `x` and `x` satisfies (Q) with discriminant `4 n1 n2 n3 n4`; linear branch `n1+n2=0` is a dead gauge; `kappa!=0` on distinct nodes | **CONFIRMED** | identically zero (Q); both `a` and `b` vanishing; expansion at `0` |
| 2 | Exact-order profiles: 5 at `m=2`, 36 at `m=4`; unique empty `(3,3|-3,-3)`; no duplicate/missing partition | **CONFIRMED** | pole parts bounded by `m`; a second unordered writing of `(2,1)` |
| 3 | Affine min-of-twelve key merges conjugates iff a same-sign permutation is affine, else two classes over the algebraic closure; no false merge of inequivalent 4-tuples | **CONFIRMED** | Galois quotient; `T ~ 1/T`; non-unique `Quad` writing |
| 4 | Charged certificates on every collision-free root; samples agree, including both signs, the rational branch, and the empty profile | **CONFIRMED** | opposite Wronskian sign; a sample whose `(x,y)` fails (Q) |
| 5 | `3 gcd<=D` is the edge-count necessity at `U=4`; used only as fail-closed Boolean existence, not as a class-count formula | **CONFIRMED** | skipping `3g>D` before solving; asserting a tree-count equality |
| 6 | Totals `5` and `44` independently accounted; JSON complete; firewall is the terminal equation at `U=4` only | **CONFIRMED** | a JSON row off (Q); a hidden lower-tail claim |
| 7 | AWS r6d, matching hashes, rc 0, empty stderr, cap unused, zero swap: engine replay, not the census proof | **CONFIRMED** | source-hash mismatch; nonzero rc; Mac host |

---

## Remarks (non-blocking)

1. The linear branch in `solve_profile` is unreachable with same-sign placement of `(n1,n2)` and is not a defect. The geometry it would have parametrized is present as ordinary quadratic (often rational) solutions.
2. `canonical` keys are dropped from the JSON, so an external replay cannot re-check the min-of-twelve step from the payload alone. The merge/split pattern on weights is an independent substitute and matches every row.
3. Radicand exponent `0` is stored rather than omitted. Degree `4m` still holds. Display only.
4. Several quadratic classes have rational `kappa` (for example `(4,2|-3,-3)` with `d=2` and `kappa=4/9`), which is consistent: `kappa` is a symmetric function of a conjugate pair that has already been merged.
5. The Boolean tree checksum coinciding with existence is stronger than necessity plus the one empty profile, and is proved for this box by the collision analysis, not by citing Lu--Song as an oracle.
6. Characteristic zero is essential and present: Vandermonde, `U-1=3!=0` in the charged degree formula, and nonzero integer residues.

None of these remarks changes a numbered verdict.

---

## Strict scope firewall

This review confirms a complete affine classification of exact-order two and exact-order four terminal moment configurations at `U=4`. It does **not**:

- solve `r_1'=...=r_6'=0` or determine any algebraic fibre of those constants;
- produce a remaining Faber coefficient function, a rational or polynomial trajectory, either original Taylor-boundary family, a strict Rees boundary, or a Keller pair;
- classify `U>=5`, bound `U`, realize an arbitrary passport, or lift a passport to a lower Faber fibre;
- equate affine classes with a combinatorial plane-tree count;
- close the order-four client, the order-two client, the cell `(8,12)`, maximum twelve, or JC2.

Registration's last paragraph matches this boundary. No creep was found in the JSON, the stdout summaries, or the enumerator comments.

---

## Terminal boundary (accepted, not enlarged)

```text
U=4_normalized_quadratic=PROVED
discriminant_4*n1*n2*n3*n4=PROVED
linear_branch_n1+n2=0_dead_in_gauge=PROVED
kappa_degree_three_nonzero=PROVED
m=2_five_profiles_five_classes=PROVED
m=4_thirty_six_profiles_one_empty_forty_four_classes=PROVED
conjugates_merged_iff_affine_same_sign=PROVED
Boccara_Zannier_3gcd_leq_D_boolean_checksum=PROVED
charged_certificates_on_collision_free_roots=PROVED
AWS_replay_engine_evidence_not_census_proof=PROVED
other_six_tails=NOT_SOLVED
Taylor_polynomiality=NOT_CLAIMED
U_bounded=NOT_CLAIMED
U>=5_classified=NOT_CLAIMED
any_Kummer_leaf_closed=false
(8,12)_empty=false
maximum_twelve=NOT_CLAIMED
JC2=NOT_CLAIMED
```

CONFIRMED
