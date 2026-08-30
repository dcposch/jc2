# Hostile review: exact global radical of the unloaded K00 rows

Reviewer: Fable 5 (independent hostile lane; producer is Sol 5.6 Ultra)
Date: 2026-08-29 UTC
Reviewed body: `xmodel/k00-unloaded-surface-global-radical-sol56-20260829.md`,
body SHA-256 `41d6460a0f1228f192f67c98c75accdfa3d7ccb29d6dda080015ea8393f50959`
(5661 bytes, marker unique and standalone; recomputed and matched).
Frozen basis `9b64db896b65e100839f6d75fbeea661cd818b9c` = current `HEAD`
(scoped git query; `jc2-lean` untouched).

## Verdict

`CONFIRM_WITH_CORRECTIONS`.

The theorem `sqrt(I) = J` in `Q[d0,...,d5]` is correct and was re-proved here
end-to-end without Singular, without the producer's `liftstd`/`reduce` code
path, and without `minAssGTZ`, from the frozen bytes alone, in pure exact
Python-stdlib arithmetic (seconds-scale; scripts inline below). Both
containments, the primality of `J`, all four serialized quintic identities in
the original seven-row presentation, the V3 serialization defect, the V4
repair, and the functor-of-points scope all check out. The corrections are
wording-only (C1–C2 below); no mathematical statement in the sealed body is
wrong. In addition, this review independently **proves** the sharp
first-power-five claim that the producer had only screened in memory.

Promotion recommendation: **promote** the exact global radical equality at
its stated unloaded-source, characteristic-zero scope, with the report's §4
firewall attached verbatim, and record the exponent refinement of §5 below as
reviewer-proved. No rerun needed.

## 1. Seals, custody, and output discipline — CONFIRMED

Every pinned hash was recomputed and matched:

- report body `41d6460a...` (5661 bytes; `<!-- BODY-END -->` appears once as a
  standalone line, the second occurrence is quoted inside the seal text);
- source prelude `5b0a77e6...` — and, closing the provenance chain, the packet
  copy is byte-identical to the declared V14R1 origin
  `cases/max12_812_order2_u2_62_k00_colon_local_v14r1_20260827/aws_q_box01_pass/compiled/serialized_replay_prelude_Q.sing`
  (same SHA-256);
- V4 producer `bb95d104...` (packet top and run dir identical), V4
  `run_exact.sh` `81c1af14...`, V4 stdout `e7b23ec5...`;
- custody manifest `8f307a03...`; all **36** entries re-verified OK, including
  all **28** multiplier files (`POWER_F{0,1,2,5}_LIFT_{1..7}.poly`);
- replay script `a14e3f84...`, replay stdout `d8c59b0e...`, replay stderr
  `2465661...`, `run_replay.sh` `3d3fc6cb...`;
- LAUNCH pins for V3 (`f6ba8d19...` wrapper, `903d2c35...` producer),
  `global_minass.sing` `8fd2faa1...`, `local_power.sing` `83eb1ce7...`,
  `aws_exact_lane.sh` `ebe06a10...`.

No zero-byte file exists anywhere in the packet. All four cited lanes carry
`.meta` records with `rc=0`, end timestamps, and stdout/stderr hashes matching
the frozen files; `lanes.log` agrees. Marker provenance was traced in the
scripts, not assumed: the V4 stdout is `Singular -v` banner (ending `Auf
Wiedersehen.`) followed by the quiet producer run's own `print` markers; the
replay stdout is the fail-closed `sha256sum -c CUSTODY.sha256` transcript (36
`OK` lines, `set -euo pipefail`, runs before Singular) followed by the quiet
replay's markers. Every failure branch in both Singular scripts prints a
typed `..._FAIL=...` marker and quits before the endpoint line, so
`PASS_K00_SURFACE_EXACT_GLOBAL_RADICAL_J` cannot be reached fail-open. V1
(harness false-failure) and V2 (resource-cancelled, no power marker, rc 1) are
preserved as negative custody only and are cited as evidence nowhere. The
r6a `LOCAL-POWER` screening lane has no artifacts in this packet and the
report does not rely on it. The replay hardcodes exponent 5
(`-f0^5` … `-f5^5`), consistent with `..._REPLAY_EXPONENT=5`.

## 2. Two-containment proof — CONFIRMED, independently and CAS-free

Let `psi : Q[d0..d5] -> Q[d3,d4]` be the Q-algebra map

```text
d0 -> 2*d4+d4^2,  d1 -> (1+d4)*d3/8,  d2 -> d4+16*d3^2,
d3 -> d3,         d4 -> d4,           d5 -> 2*d3,
```

i.e. exactly the graph `D(S,T)` with `S=d4`, `T=d3`.

**Lemma (`ker psi = J`, constructive).** `psi(f0)=psi(f1)=psi(f2)=psi(f5)=0`
(verified exactly), so `J ⊆ ker psi`. Conversely, substitute variables one at
a time in the order `d0,d1,d2,d5`. Each generator has the form
`c*x - phi` with `c` in `{1,8,1,1} ⊆ Q^*` and `phi` involving only `d3,d4`;
for any polynomial `p`, `p - p|_{x<-phi/c}` is divisible by `x - phi/c =
(1/c)*f`, hence lies in `(f)`. Chaining the four steps gives
`p ≡ psi(p) mod J` for every `p`. So `psi(p)=0` implies `p ∈ J`. ∎

- **`I ⊆ J`:** `psi(r_i) = 0` was verified by exact expansion for all seven
  frozen rows (parsed from the pinned prelude bytes with a strict
  character-set/token validator; term counts 16, 23, 27, 36, 40, 42, 57;
  total degrees 4, 4, 5, 5, 5, 6, 6; all constant terms vanish). By the
  lemma, each `r_i ∈ J`. This leg is Groebner-free in this review — it does
  not reuse the producer's or replay's `reduce`/`std` calls.
- **`J` prime of dimension two, without `minAssGTZ`:** by the lemma,
  `Q[d0..d5]/J ≅ im(psi) = Q[d3,d4]` (surjective since `d3,d4` are fixed), a
  domain of Krull dimension 2. So `J` is prime, `dim J = 2`, height 4, and
  `sqrt(I) ⊆ sqrt(J) = J`.
- **`J ⊆ sqrt(I)` from the serialized certificate, original presentation:**
  the 28 pinned multiplier files were parsed independently and the four
  identities

  ```text
  f_a^5 = c_{a,1}*r1 + ... + c_{a,7}*r7,   a in {0,1,2,5},
  ```

  were expanded directly against the seven frozen rows as given (never
  against a standard basis, never through `liftstd`). All four residuals are
  identically zero (largest multiplier 549 terms; whole check < 1 s). Hence
  each `f_a ∈ sqrt(I)`.

Together: `sqrt(I) = J`, exactly over `Q`. The displayed graph `D(S,T)` is
the correct parametrization and `(S,T)=(d4,d3)` is forced, so the point of
`V(J)` over any field is unique on the graph as claimed.

Independent mutation battery (all detected, beyond the packet's own):

- input mutation `16 -> 15` in `f2`: rows 2–7 leave `ker(psi_bad)`;
- interior-coefficient mutation (one monomial of `c_{2,4}` scaled by 2): F2
  identity fails;
- row mutation (`r1 -> r1 + d3^2`): F0 identity fails (`c_{0,1}` has 224
  terms, nonzero);
- wrong-exponent controls: the same multipliers fail against `f_a^4` and
  `f_a^6` for every `a`;
- cross-wired certificate (`c_{1,j}` against `f0^5`): fails.

## 3. V1–V4 repair ledger — CONFIRMED

- **V1** stopped at `...FAIL=BASIS_REPLAY` from comparing a matrix object
  with scalar zero; retained as negative custody; no power conclusion. As
  documented.
- **V2** is a deliberately terminated non-verdict (no power marker emitted);
  not evidence. As documented.
- **V3 defect verified byte-exactly**, not just by byte counts: for each of
  F0, F1, F2, F5, the V3 `POWER_F*_LIFT.matrix` file equals the V4
  `POWER_F*_LIFT_1.poly` file minus its trailing newline (10728/10729,
  18216/18217, 27105/27106, 310/311 bytes). So V3's `write(matrix)` truly
  serialized only the **first** of the seven vector entries, and V3 alone
  could never have supported an independent replay of the identities.
- **V4 is a genuine repair, not a restatement:** the V3→V4 producer diff
  contains only the shape guards, the 28 per-entry `write` calls, and the new
  serialized-multipliers marker; no mathematical formula changed. The
  promotion-bearing artifact is the fresh replay, which re-derives the four
  identities from the serialized files by direct expansion — the same
  computation this review reproduced from scratch with matching results. The
  in-memory `liftstd` path was used by this review for nothing.

## 4. Exponent five: sufficient AND now proved first — upgraded

Kept separate from the radical equality, as required:

- **Sufficiency** (`f_a^5 ∈ I`) is proved by the portable, replayed,
  hash-pinned certificate. This alone carries `sqrt(I)=J`.
- **Minimality** was, in the packet, producer-screen only: the V3/V4
  `FIRST_POWER_*=5` markers rest on `reduce` against an in-memory `liftstd`
  basis whose standard-basis completeness is trusted from Singular internals
  and is not serialized (114 elements, not shipped). The sealed body scopes
  this honestly ("not needed for the radical theorem").
- **This review closes that gap.** All seven rows have order ≥ 2 at the
  origin (row 6 has order 3), so `I ⊆ m^2` with `m=(d0..d5)`; each `f_a` has
  a nonzero linear part, so `f_a ∉ I` — power 1 fails. Stronger: suppose
  `f_a^4 = sum_j h_j r_j`. Comparing homogeneous components in degrees 2–4
  gives a finite exact Q-linear system in the unknown components `[h_j]_s`,
  `s ≤ 2` (203 equations, 175 nontrivial columns). Exact Gaussian elimination
  over Q produces an inconsistent row for **every** `a in {0,1,2,5}`:

  ```text
  f_a^4 ∉ I + m^5  ⊇  I.
  ```

  Since `f_a^k ∈ I ⇒ f_a^4 = f_a^{4-k}*f_a^k ∈ I` for `k ≤ 4`, all
  powers 1–4 fail, and power 5 succeeds by the certificate. **First power is
  exactly five for each displayed generator**, now proved independently of
  Singular's `std`/`reduce` internals. The producer's sharp observation is
  therefore CONFIRMED and may be recorded as proved rather than screened.

## 5. Functor-of-points consequence and firewall — CONFIRMED, and sharp

- Fields `K/Q`: correct. `f_a(d)^5 = 0` forces `f_a(d)=0`; the point lies on
  `D(S,T)` with `(S,T)=(d4,d3)` uniquely.
- Reduced `Q`-algebras: correct; the identities have coefficients in `Q`, so
  they specialize to any `Q`-algebra, and reducedness kills `f_a(d)`.
- Formal series: `K[[t]]` over a characteristic-zero field is a domain,
  hence reduced; correct (reducedness is all that is used; the domain wording
  is merely stronger).
- **The reduced hypothesis is necessary, not cautious:** over
  `A = Q[d0..d5]/m^2` the universal point kills all seven rows (`I ⊆ m^2`)
  while `f_a` survives as its nonzero linear part. So any inference of the
  graph equations at a nonreduced/scheme-level point, or on a mixed loaded
  trajectory, an associated-graded step, a ramification reduction, or an
  attainment step **without first proving the unloaded rows vanish in a
  reduced target** is not merely unlicensed — it is false in general. The §4
  firewall is exactly right, and the report asserts no map, recentering,
  resonance, coverage, jet-lifting, attainment, counterexample, or JC2
  consequence. The loaded source shape quoted in §4 indeed does not set `I`
  to zero, so no wholesale transfer is possible.
- Characteristic scope: the rows, the graph (`/8`), and the multipliers
  (denominators include `2^k` and odd primes such as `1837 = 11*167` and
  `313515279 = 3^4*7^2*11*43*167`) require those primes invertible; the
  char-0/`Q`-algebra scope stated is the honest one and no char-`p`
  extension is licensed by this packet.

## 6. Minimal-prime lane — corroboration only, and it corroborates

`MINASS_1.txt` matches the four generators quoted in the report byte-for-byte.
Two-way identification with `J` was re-proved here by **explicit exact
combinations**, not by reduction inside a decomposition routine:

```text
f5 = -g1
2*f1 = g3 - (1+d4)*g1
f2 = g2 - 4*(d5+2*d3)*g1
f0 = g4 - 4*d5*g3 + (1+d4)*g2
```

and conversely `g1=-f5`, `g2=f2-4*(d5+2*d3)*f5`, `g3=2*f1-(1+d4)*f5`, with
`g4` recovered from the third line. All eight identities expand to zero, so
`(g1,g2,g3,g4) = J` as ideals. The verdict above stands entirely on §2 and
would be unchanged if the minass lane were discarded.

## 7. Corrections and observations

- **C1 (wording, sealed body §2 and LAUNCH.md replay section).** "The fresh
  replay uses no standard-basis or lifting computation" is not literally
  true: `replay_global_power.sing` calls `std(J)` and `std(BAD)` (tiny,
  triangular) for the `I ⊆ J`, `dim`, and input-mutation preflight legs. What
  is true and load-bearing: the replay uses **no standard basis of `I` and no
  lift/`liftstd`**, and the four certificate identities are checked by direct
  expansion. Repair is a one-sentence rewording; this review's own `I ⊆ J`
  leg is substitution-based and fully GB-free, so nothing mathematical
  depends on the sentence.
- **C2 (observation, no repair required).** The shipped certificate-mutation
  control (`c0_1 -> c0_1+1`) has residual exactly `r1`, i.e. it certifies
  only `r1 != 0`. It is valid but weak; the packet describes it accurately,
  and the stronger interior-coefficient, row, wrong-exponent, and cross-wired
  mutations were all exercised here and detected.
- Everything else checked (36-file manifest count, zero-swap/RSS claims
  against the `time -v` records, marker lists, basis commit, V2/V1 typing,
  28-file count, `D(S,T)` coordinate order) matches the sealed body exactly.

## 8. Replay of this review

Pure Python 3 stdlib, exact `fractions.Fraction` arithmetic, run from the
case directory; total < 10 s. The three stages printed, respectively: (i) all
seven `psi(r_i)==0`, four `psi(f_a)==0`, and the four identity residuals
zero; (ii) all mutation detections, the eight `g`/`f` combination identities,
row orders `[2,2,2,2,2,3,2]`, and the four out-of-span linear parts; (iii)
`INFEASIBLE` for all four depth-4 graded systems. Core checker (stage i;
stages ii–iii reuse the same classes exactly as described in §2–§4):

```python
import re
from fractions import Fraction as F
NV=6
class P:
    def __init__(s,d=None): s.d=d or {}
    @staticmethod
    def var(i):
        e=[0]*NV; e[i]=1; return P({tuple(e):F(1)})
    @staticmethod
    def const(c):
        c=F(c); return P({(0,)*NV:c} if c else {})
    def _c(s,o): return o if isinstance(o,P) else P.const(o)
    def __add__(s,o):
        o=s._c(o); d=dict(s.d)
        for k,v in o.d.items():
            n=d.get(k,F(0))+v
            if n: d[k]=n
            elif k in d: del d[k]
        return P(d)
    __radd__=__add__
    def __neg__(s): return P({k:-v for k,v in s.d.items()})
    def __sub__(s,o): return s+(-s._c(o))
    def __rsub__(s,o): return s._c(o)+(-s)
    def __mul__(s,o):
        o=s._c(o); d={}
        for k1,v1 in s.d.items():
            for k2,v2 in o.d.items():
                k=tuple(k1[t]+k2[t] for t in range(NV))
                n=d.get(k,F(0))+v1*v2
                if n: d[k]=n
                elif k in d: del d[k]
        return P(d)
    __rmul__=__mul__
    def __truediv__(s,o):
        if isinstance(o,P): o=o.d[(0,)*NV]
        o=F(o); return P({k:v/o for k,v in s.d.items()})
    def __pow__(s,n):
        r=P.const(1); b=s
        while n:
            if n&1: r=r*b
            b=b*b; n>>=1
        return r
    def subs(s,im):
        r=P.const(0)
        for k,v in s.d.items():
            t=P.const(v)
            for i,e in enumerate(k):
                if e: t=t*(im[i]**e)
            r=r+t
        return r
def parse(x):
    s=x.replace('^','**').replace('\n','').replace(' ','')
    o=[];i=0
    for m in re.finditer(r'\d+',s):
        j=m.start(); o.append(s[i:j])
        if j>=2 and s[j-2:j]=='**': o.append(m.group(0))
        elif j>=1 and s[j-1]=='d': o.append(m.group(0))
        else: o.append('F(%s)'%m.group(0))
        i=m.end()
    o.append(s[i:])
    env={'F':F}
    env.update({'d%d'%i2:P.var(i2) for i2 in range(NV)})
    return eval(''.join(o),{'__builtins__':{}},env)
src=open('aws_r6b_global_power_v4/prelude_Q.sing').read()
r={int(m.group(1)):parse(m.group(2))
   for m in re.finditer(r'poly r(\d)=([^;]+);',src)}
d=[P.var(i) for i in range(NV)]
f={0:d[0]-2*d[4]-d[4]**2, 1:8*d[1]-(1+d[4])*d[3],
   2:d[2]-d[4]-16*d[3]**2, 5:d[5]-2*d[3]}
S,T=d[4],d[3]
psi=[2*S+S**2,(1+S)*T/8,S+16*T**2,T,S,2*T]
assert all(not r[i].subs(psi).d for i in range(1,8))      # I subset J
assert all(not f[a].subs(psi).d for a in f)               # J = ker psi gens
for a in f:
    s=P.const(0)
    for j in range(1,8):
        c=parse(open('aws_r6b_global_power_v4/POWER_F%d_LIFT_%d.poly'
                     %(a,j)).read())
        s=s+c*r[j]
    assert not (s-f[a]**5).d                              # J subset sqrt(I)
print('SQRT(I)=J CONFIRMED')
```

Stage iii builds, for each `a`, the exact linear system
`[f_a^4]_m = sum_{s+t=m} [h_j]_s [r_j]_t` for `m=2..4` over all monomials
(unknowns `[h_j]_s`, `s<=2`) and eliminates over `Q`; an inconsistent
`0 = nonzero` row appears in every case, proving `f_a^4 ∉ I + m^5`.

## 9. Summary of exact-claim verdicts

| claim | verdict |
|---|---|
| all seals/custody, 36 files, 28 multipliers, stdout markers, no zero-byte/live verdicts | CONFIRMED |
| `I ⊆ J` from the frozen rows (GB-free substitution) | CONFIRMED |
| `J` prime, dim 2, no `minAssGTZ` | CONFIRMED |
| four identities `f_a^5 = Σ c_{a,j} r_j` in the original presentation | CONFIRMED |
| `sqrt(I) = J` exactly over `Q` | CONFIRMED |
| V3 first-entry-only serialization; V4 + fresh replay a genuine repair | CONFIRMED |
| exponent 5 sufficient | CONFIRMED (certificate) |
| exponent 5 first power for each generator | PROVED by this review (was producer-screen) |
| functor-of-points scope (fields / reduced / formal series) + firewall | CONFIRMED; reduced hypothesis proved necessary |
| minass output = `J` (corroboration only) | CONFIRMED |
| replay described as using "no standard-basis … computation" | CORRECTION C1 (wording) |

No exit-price assertion is made or consumed in this review; `charge_basis`
is intentionally absent.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17402`.
- Body SHA-256:
  `1300566c9b862a1c4624b893e91e426ac7295d004667ea247cab9883005b8c01`.
- Frozen basis: `9b64db896b65e100839f6d75fbeea661cd818b9c`.
