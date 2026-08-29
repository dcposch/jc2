# Sol 5.6 different-model hostile disposition — TD12-BCHILD/v1 Fable primary

Date: 2026-08-29  
Reviewer: Sol 5.6 (different-model hostile mathematical review)  
Frozen Git basis: `76c746f698103d20019bfeb72654a361ccc5371d`

Charged producer:
`xmodel/td12-bchild-v1-primary-fable5-76c-20260829.md`.

This is a correction/disposition only.  It does not edit the producer or any
canonical/source/code file, does not construct a local pair, and does not
license a software migration.

## 0. Custody and charged perimeter

The following full-file SHA-256 hashes were recomputed before this review:

```text
1a60264334ae99f60ff79f1ed8b4a75cb42abf30f5e4ae8001a51b9064056d84  xmodel/td12-bchild-v1-primary-fable5-76c-20260829.md
b8125795c6e469daa9711e674d149ea7259c5165180378bd1e672002ced78c05  xmodel/td12-bchild-v1-provisional-sol56-76c-20260829.md
bb70bc4b96d37a5a87bcbf9cba26db7fb96b45e9e0189204fde18f104a517900  xmodel/td12-bchild-v1-minimal-source-packet-audit-sol56-76c-20260829.md
79df783a0ed9e370621e750f4e6564dc9871b53e1481898e77dcdd037711ad1c  xmodel/td12-bchild-v1-minimal-source-packet-audit-r1-erratum-sol56-76c-20260829.md
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
599e2a9123194c580b89b822f5b7a218fa5e9735b16bcb744e0f0e4231584271  xmodel/m2-td12-u1-trunk-consumer-primary-grok46-20260829.md
52ffafa2e79823e275e084d9d3c3a36329401cc9449a6e572379ce1ee0390b69  xmodel/m2-td12-u1-sibling-exact-charge-r1-sol56-20260829.md
```

Actual source passages charged: Lemma 2.1 and Notation 2.4 (global type),
Propositions 4.1, 4.2 and 4.4, Statement 5.1 and Proposition 5.3(ii),(viii),
and the Statement 3.7/Notation 3.9--3.11 chart expansions in the pinned PDF;
the type-`(2,3)` declarations and the displayed `nu=25` and `nu=17` route
states in the two pinned campaign reports; and the four frozen TD12-BCHILD
reports named above.  No conclusion is charged to an unpinned source.

The Fable report's own body seal was independently recomputed and matches:

```text
report_body_bytes  = 33565
report_body_sha256 = d5b099c2627b86d11345b8283080fcd746c1a0352cc8058182951710e5065feb
```

## 1. Disposition

```text
Fable primary:               PASS_WITH_REPAIR
campaign-level outcome:      SOURCE_UNDERDETERMINED
maximum current promotion:   symbolic recurrence + conditional own-order
                             absorption + formal level-1 nonidentifiability
```

The producer found a genuinely useful identity: the fresh f-side
coefficient can be absorbed at the same order by an explicit g-side
response.  The exact recurrence, its right-hand-side landing order, the
conditional absorption identity, the leading child coefficients, and the
two level-1 formal choices all survive review.  No non-top child vector is
emitted.

Four repairs are required before consumption:

1. The `nu=25` B state and `nu=17` sibling state are alternative reduced
   route states.  They do not share a `PairRef`, completion, common parent,
   first-resolvent constant, or g-side scale.  Only the two `nu=17` roots
   evaluate one common `P_k` family.
2. On either type-`(2,3)` route, the ratio is not a free initialization:
   conditionally on occurrence in the source tree,
   `D_g/D_F=d_g/d_F=3/2`, hence `r=3i/2`.  What remains missing is the
   route-specific scale/top coefficient and, more fundamentally, the exact
   pair, completion, contact ledger, lower jets and caps.
3. Without that type pin, Theorem B absorbs only variations divisible by
   `p^(i-r)` when `r<i`; its unrestricted image-inclusion sentence must be
   domain-qualified.  The level-1 examples do satisfy the divisibility and
   survive even in the producer's more general symbolic setting.
4. The asserted “exactly one infinity cokernel” and the resulting numerical
   cascade codimension are not proved by the report.  They depend on an
   explicitly frozen polynomial domain, target, root-floor quotient and cap.
   Those data are among the report's declared missing inputs.  The cascade
   is therefore a candidate lane, not a promotable theorem.

## 2. Exact recurrence and RHS-order audit — PASS

Write `kappa=Q*kappa_F`, top indices `n_f=Q D_F`, `n_g=Q D_g`, and

```text
P_a = p_(f,n_f-Qa),       G_b = p_(g,n_g-Qb).
```

The coefficient of `x^((j+k)/kappa-1)` in the chart Jacobian is

```text
(1/kappa) * (j p_(f,j) p_(g,k)' - k p_(f,j)' p_(g,k)).
```

Since `J_(x,eta)(f^F,g^F)=x^(-u)`, the unscaled landing is
`j+k=kappa(1-u)`.  Dividing the on-lattice equation by `Q` gives exactly

```text
(E_s)  sum_(a+b=s) ((D_F-a)P_a G_b'-(D_g-b)P_a'G_b)
       = kappa_F * 1_(s=s*),

s* = D_F + D_g - kappa_F(1-u)
   = D_F + D_g - kbar_F.
```

Thus the producer's indexing, factor `kappa_F`, sign and landing order are
correct.  The windows are homogeneous.  Even under its weaker `i,r>=1`
assumption, `s*=25(i+r)-17>24` and
`s*=17(i+r)-13>16`; the type-`(2,3)` pin only increases the separation.

Order zero also passes.  Unique factorization of `P_0=p^i` in

```text
D_F P_0 G_0' - D_g P_0'G_0 = 0
```

gives `G_0=c_g p^r` with `D_F*r=D_g*i`.  For these source routes the global
type and root-to-pole ratio theorem specialize this to

```text
D_g/D_F=3/2,       r=3i/2,
```

separately in each hypothetical route realization.  This does not identify
the two realizations or their constants `c_g`.

## 3. Theorem B audit — exact identity, narrower conclusion

For

```text
A_s[delta P]=(D_F-s)delta P G_0'-D_g(delta P)'G_0,
B_s[delta G]=D_F P_0(delta G)'-(D_g-s)P_0'delta G,
delta G=(r*c_g/i)p^(r-i)delta P,
```

direct expansion leaves two coefficients:

```text
[p^r (delta P)'] : -c_g D_g + (r*c_g/i)D_F = 0,
[p^(r-1)p'delta P] :
  c_g*r*(D_F-s)
  +(r*c_g/i)*(D_F*(r-i)-i*(D_g-s)) = 0.
```

Both vanish exactly by `D_F*r=D_g*i`.  The identity is sound.

Polynomial typing is load-bearing.  If `r>=i`, the response is polynomial
for every polynomial `delta P`.  If `r<i`, it is polynomial only when
`p^(i-r) | delta P`.  The reviewed vanishing ladder guarantees that for the
displayed level-1 choices (and, as a sufficient general bound, for
`s<=r`), but not for every higher-order source-admissible piece.  Therefore
the general statement must be read as

```text
A_s({delta P : p^(i-r)|delta P}) subset im(B_s)       (r<i),
```

not as unrestricted `im(A_s) subset im(B_s)`.  In the actual type-`(2,3)`
route packet, `r=3i/2>=i`, so this rider disappears; it remains essential
to the producer's advertised arbitrary-`r` theorem.

The reduced substitution with an auxiliary `Z` is also algebraically exact:

```text
G_s=c_g p^(r-i)((r/i)P_s+Z)

=> c_g p^(r-1)[D_F p Z'-i(D_F-s)p'Z]=-K_s.
```

It is a reformulation, not yet a closed recurrence or a rank theorem.

## 4. Level-1 negative controls — PASS at formal coefficient tier

At `s=1`, `K_1=0`.  The zero choice and each displayed nonzero `P_1`, with
the matched `G_1`, satisfy `E_1`, the weight class, the root floors and the
natural top-degree bound.  In particular, when `r<i`, multiplying the B
exhibit by `p^(r-i)` leaves root exponents `(2r,r-1)`, and the sibling
exhibit leaves `(2r,r-1,r)`; all are nonnegative for `r>=1`.

The B choice changes `v_(B,1)` from zero to nonzero.  The sibling choice
changes one of `(v_(+,1),v_(-,1))` while leaving the other zero.  Therefore
the frozen top data plus the full order-1 Keller equation do not identify
the level-1 vector entry, and no Galois-conjugacy relation between the two
sibling evaluations follows from the window equations alone.

This is formal local-coefficient nonidentifiability, not two exact Keller
pairs and not an assertion that either choice extends through orders
`2..depth`.

The leading entries `v_(B,0)` and `v_(S_j,0)` are correctly obtained by
Taylor expansion of `P_0`; they are nonzero.  Consequently the first-child
polynomial has degree exactly `i` and the level-1 delay/nonzero guard passes
structurally.  Its unknown remaining coefficients still prevent every
gcd/binomial gate.

## 5. Cokernel/cascade audit — QUARANTINE

The claim of exactly one infinity cokernel condition is not licensed by the
argument given.  In a fixed weight class write `p=P(t)`, `t=eta^nu`,
`G=eta^e H(t)`, where `deg_t P=M` (`M=3` for B and `M=4` for the sibling).
After stripping `p^(i-1)`, the g-side operator has the form

```text
T_s(H)=A(t)H'(t)+B(t)H(t),
deg A=M+1,       deg B<=M.
```

For a finite cap `deg H<=N`, it maps an `(N+1)`-dimensional domain into a
target of nominal dimension `N+M+1`.  Root-floor factorization and a leading
resonance can change the target, but they do not by themselves prove that
its remaining cokernel is one-dimensional.  The answer varies with the
chosen domain, cap, target floors and whether the resonant degree is the cap
endpoint.  The B and sibling reduced polynomials also have different
numbers of distinct `t`-roots (two versus three), so one common dimension
count cannot be inferred from the displayed leading-term resonance.

Accordingly, these statements remain promotable:

- the exact reduced `Z` equation;
- injectivity of the unstripped homogeneous polynomial solution on
  `0<s<nu`, because `p^(r-s/nu)` is not a polynomial;
- possible finite-root divisibility and infinity compatibility conditions
  as explicit objects for a future rank computation.

These statements are not yet promotable:

- “exactly one” cokernel condition per order;
- the quoted `<=1 + r`-dependent codimension;
- “first Keller bite is at `s=2`” without an explicit nonzero, typed
  `K_2` and a frozen target/cap;
- any kill, closure, or deep extension based on that cascade.

The producer itself calls the cascade a candidate in its firewall; that
weaker label is the safe one.

## 6. Route-separated next producers

### 6.1 `TD12-B25-PAIRPACK/v1`

Suggested owner: Fable 5 primary; Sol integration; exact Grok hostile review
in the background after a provisional packet exists.

Required inputs:

```text
PairRef_B(f_B,g_B), with coefficient/support hashes and J=1 certificate;
an occurrence witness for the type-(2,3) nu=25 cell
  (nu,kbar,X,M,w)=(25,17,25,3,2/3);
the fibre value, y-side branch, Notation-3.9 prefix and exact completion;
c_B^25=B, the route gauges, full i and the direct-entry rider if i=6n is used;
the route-B contact ledger through normalized depth 24;
f/g (or fully typed derived-source) Laurent jets and exact degree/support caps.
```

Required outputs:

```text
a custody-sealed TD12LocalPairJet_B;
P_0..P_i and G_0..G_i, with E_s replay and all polynomial target spaces;
v_B and C_B,1, then the normalization/gcd/binomial verdict;
the first recentered state only after a pass;
fail-closed states PAIRREF_ABSENT, OCCURRENCE_UNPROVED,
COMPLETION_UNTYPED, CONTACT_LEDGER_INCOMPLETE, CAP_UNPINNED,
CASCADE_FAIL and DENOMINATOR_JUMP.
```

This producer must not silently search for an inverse polynomial pair.  If
no exact `PairRef_B` exists in custody, its correct immediate output is
`PAIRREF_ABSENT`.

### 6.2 `TD12-S17-SIBLING-PARENT-PAIRPACK/v1`

Suggested owner: Opus 5 primary; Sol integration; Fable 5 or Grok hostile
review in the background.

Required inputs:

```text
an independent PairRef_S(f_S,g_S), with support hashes and J=1 certificate;
an occurrence witness for the type-(2,3) nu=17 cell
  (nu,dp,dq,kbar,X,M,w)=(17,68,52,13,17,4,3/4);
one fibre/parent completion and the unordered T1 roots
  B_+/-=(9+/-3*sqrt(-1))A/8, with c_+/-^17=B_+/-;
the route-S gauges, full i/direct-entry rider, common contact ledger through
  normalized depth 16, f/g or derived-source jets, and exact caps.
```

Required outputs:

```text
one custody-sealed TD12LocalPairJet_S and one common P_k/G_k family;
both vectors v_+,v_- by simultaneous evaluation of that family;
both level-1 normalization/gcd/binomial verdicts and coupled deeper replay;
an exact base-field/Kummer/Galois audit, with no rationalized roots;
the same fail-closed states as B, plus ROOT_FIELD_UNTYPED and
INDEPENDENT_ROOT_SOLVES_FORBIDDEN.
```

The two sibling evaluations must never be produced as independent source
states.  Conversely, this packet must not reuse the B route's `PairRef`,
completion or `c_g`.

### 6.3 Desk/AWS threshold

Source typing, prefix/rate audit, identities, hashing and finite support
manifests remain desk-scale.  No AWS/CAS run is licensed before a finite,
route-specific pair/completion packet exists.  Once such a packet freezes a
coefficient field, variable order, support cap and equation manifest, any
inverse search, Groebner/resultant elimination, broad parameter enumeration,
or normalization/Puiseux expansion of uncertain cost belongs on a registered
AWS worker.  B and sibling may then run in parallel because their packets are
independent.  Provisional outputs should publish immediately; review does not
block descendants, but promotion does.

An executable desk-only precursor is a separate formal cascade-rank lane:
fix the type-`(2,3)` ratio, state the exact domain/codomain/floors/cap at each
order, and compute the operator rank symbolically.  It must not call its
formal jet envelope a `PairRef`.

## 7. Canonical impact

No currently promoted mathematical theorem needs retraction.  The only
false cross-route packet-sharing sentence was in the provisional minimal
packet audit and is already withdrawn by its sealed R1 erratum.  The Fable
producer is provisional and should remain immutable with this disposition
attached.

At the next canonical integration, update only the live frontier/history:

- record `SOURCE_UNDERDETERMINED` and the exact symbolic `E_s` recurrence;
- record own-order absorption with its typing rider and the level-1 formal
  two-choice witness;
- replace any operational “one packet emits all three vectors” wording by
  separate B and sibling-parent packet producers;
- label the cokernel/cascade dimension as an unproved candidate pending the
  finite rank lane;
- record that no software migration, AWS computation, child vector, gate
  verdict, or JC2 consequence is licensed.

## 8. Scope firewall

Nothing here supplies an exact polynomial pair, proves occurrence of either
route cell, extends the level-1 examples, evaluates a depth gate, proves a
landing or exclusion, constructs a counterexample, or proves JC2.  No
canonical/source/code file was edited, and no commit or push was made.

## Seal

- Body length: `14248` bytes (all bytes before this heading).
- Body SHA-256: `45d79d5ed605e7a17a121971a747c10b1f4b30d4b9db805d2c090f3528f0c1dd`.
- Frozen Git basis: `76c746f698103d20019bfeb72654a361ccc5371d`.
