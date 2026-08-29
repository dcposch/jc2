# Coordinator integration — TD12 B global source bridge

Date: 2026-08-29 UTC  
Coordinator: Sol 5.6  
Lifecycle: `PROMOTED_B_SOURCE_BRIDGE_CORE_NO_ROUTE_KILL`

## 0. Evidence and binding disposition

Fable 5 primary:

```text
0175063f5dcef9c3ba1c70d3ad883ad28f8757d514ec387b968b29324272274b
  xmodel/td12-global-source-bridge-b-fable5-92e-20260829.md
  body 39510 bytes:
  539ecec1d4255067a7819bb7577e69809a1b4f0800ab8e8313d1ad026fa58278
```

Different-model Grok 4.6 hostile review:

```text
20684d3e5ea0f070817c08c72d0dd1b45e691787429bd8eb57eaf68296431bf8
  xmodel/td12-global-source-bridge-b-fable5-hostile-review-grok46-92e-20260829.md
  body 41244 bytes:
  dab4058f598c05dbd5d00448c7e36c56dbbbfa7869ec3df3189f4640876a85b4
8800a77b8102cfabb49636e0139f3bc1465755ee6dec42b8c0259080497913cf
  xmodel/td12-global-source-bridge-b-fable5-hostile-review-grok46-92e-20260829.run.v2
```

The run is `DONE` on frozen basis
`92ebe92ad5986a47f01af9ed901260595dfed869`, with stable prompt, adapter,
validator, `FALLACY-v2.md`, and composed-model-prompt hashes;
`charge_basis_status=ABSENT` is correct. Verdict is `PASS_WITH_REPAIR`.

Binding disposition:

```text
PROMOTE C1--C3 SOURCE-BRIDGE CORE AT NAMED-ACTUAL-OCCURRENCE SCOPE
PROMOTE C4 OPERATOR/KERNEL STRUCTURE WITH CORRECT FIRST-RESONANCE FORM
DO NOT PROMOTE THEOREM-B UNIFORM SCHEME OR A NONTRIVIAL j=17 OBSTRUCTION
NO B-ROUTE KILL, OCCURRENCE, PAIRREF, CAP, OR JC2 CONCLUSION
```

## 1. Promoted source bridge

Fix a characteristic-zero polynomial pair `(f,g)` with `J(f,g)=1` that is
not an automorphism, normalized of type `(2,3)`, and a **named actual
occurrence** `(a,S,F)` of the B state

```text
(nu_F,kbar_F,X,M,w)=(25,17,25,3,2/3),
P_0=lambda_f p^i,       G_0=c_g p^r,
r=3i/2,                 i positive and even,
p=(t-A)^2(t-B),         q=eta(t-A)(t-B),
t=eta^25,               A,B nonzero and distinct,
kappa_F>17.
```

Keep `nu_F=25`, `kbar_F=17`, `X=25`, the chart denominator `kappa_F`, and
graded indices distinct. The native Newton--Puiseux/Sigray chart is
functorial from **the pair plus the named occurrence**, not from the pair
alone and not from the GGV interface without its separate riders. Its
pieces `P_k,G_k` are finite polynomial functionals of the pair coefficients
and the finite Puiseux prefix. This is not a serialized value packet and is
not an occurrence theorem. For each fixed polynomial pair,

```text
K_h=D_h+(kappa_F-17) deg_y(h)
```

bounds its chart support; there is no uniform degree or `kappa_F` cap over
all hypothetical pairs.

In the graded completion, subtract greedily the finite fractional-power
responses in the kernel of `J(f^F,-)`. Every nonzero homogeneous top of the
reduced deviation at drop `delta<s*` has

```text
delta in 25 Z,
s*=D_F+D_g-17=25(i+r)-17.
```

There are at most `i+r-1` such slots; the process cannot exhaust `g^F` and
its terminal reduced deviation has top drop exactly `s*`. Its top piece `T`
satisfies the unique inhomogeneous landing row. After substituting
`P_0=lambda_f p^i`, this becomes

```text
25 p T' + (25i-17)p'T
  = (kappa_F/(i lambda_f)) p^(1-i).
```

The exact identity

```text
25 p q' - 17 p' q = 25 p (AB+(8B-9A)t)
```

shows that the landing row is solvable in `C[eta][1/p]` iff `8B=9A`.
On that locus its unique on-weight solution is

```text
T=gamma q p^(-i),
gamma=kappa_F/(25 i lambda_f A B).
```

Thus the genuinely inhomogeneous source row lands exactly on the already
reviewed T1 ratio and passes uniquely. It has the same reduced `(p,q)`
solvability condition as terminal Proposition 8.1(iv); it is not an
object-level identification with the terminal approximate root when
`m_F>1`.

## 2. Binding repairs and below-landing scope

- The first approximate-root scale is
  `s_0=c_g^2/lambda_f^3`, unless the gauge `lambda_f=1` is fixed.
- The completion depends on `(pair,a,S,F)`; `OCCURRENCE-B25` and `CAP-B25`,
  not an absent formal constructor, remain the emission blockers.
- N1 is a sufficient route datum; the exact nonabsorbability arithmetic is
  `s*=-17 mod 25`, not a new equivalence theorem about N1.
- The universal coefficient scheme is promoted only in the elementary
  fixed-support sense: its fixed-`Delta` Keller locus is algebraic. The
  constructible stratification/etale regularity write-up remains outline,
  and the union over unbounded supports is not finite-dimensional.
- The binomial polynomial response is licensed through `s<=r`; statements
  through all `s<25` also require `r>=24`, equivalently `i>=16` here.

For the tail below the landing, the fresh operator is

```text
L_j[T_j]=25pT_j'+(25i+j-17)p'T_j.
```

It has a `C(eta)` kernel exactly when `j=17 mod 25`; at nonresonant rows an
actual-pair solution is unique in `C(eta)`. At the first resonance the
correct primitive equation is

```text
(p^i T_17)'=RHS_17/(25 i lambda_f),
```

not Fable's equation with an extra `p^(i-1)`. Grok's review promotes the
correct operator and primitive form, but does **not** prove that the two
orbit residue functionals are nonzero or independent on the admissible
class.

The later exact Sol expansion

```text
edfec0a0d9abb8b24db9406bdc1147348114f198a4a9e92a10486bbe9131a720
  xmodel/td12-b25-resrow-v1-provisional-sol56-20260829.md
  body 11988 bytes:
  9c72c20e02efcb74fd351f7ac820268386a625dbfc60b855dc18a1e212766b4f
```

finds `RHS_17` to be an exact derivative, making both residues identically
zero and moving the first potentially nonvacuous resonance to `j=42`, beyond
B24. That sharper endpoint remains provisional pending independent review;
it supersedes the Grok review's scheduling recommendation, not any theorem
promoted above. Stop `TD12-B25-RESROW/v1` at `j=17` provisionally and do not
launch `j=42` without a source-bearing client.

## 3. Firewall

No value of `P_k` or `v_(B,k)` for `k>=1`, serialized `PairRef`, B-state
occurrence, uniform cap, gate verdict, tree landing, coverage statement,
finite book, exit price, degree bound, route exclusion, counterexample, or
JC2 result follows. The bridge redirects the B route from homogeneous-window
algebra to actual occurrence/source support and later intermediate jets; it
does not solve those problems.

<!-- END-SEALED-BODY::td12-global-source-bridge-b-coordinator-integration-sol56-20260829 -->

## Seal

- Body byte count: `6243`.
- Body SHA-256:
  `89fc2555eeeb4424a45cde47a16b910b3a34b9ac42a3b91717d89e5442b759d5`.
- Frozen input basis:
  `92ebe92ad5986a47f01af9ed901260595dfed869`.
