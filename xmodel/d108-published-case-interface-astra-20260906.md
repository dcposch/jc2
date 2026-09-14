# D108 published-case interface: the first citation-applicability gap is discharged

Evidence: exact literal source/chain arithmetic, plus **EXTERNAL-THEOREM** use of the cited primary results. Lifecycle: **PRODUCER-CHECKED**, awaiting an independent gate. No source point, properness, full coefficientwise cut map, freshly replayed large certificate, or unconditional JC2 result is claimed.

**Usable conclusion.** For a characteristic-zero field-valued specialization of the frozen D108 source, if its physical pair has nonzero constant Jacobian, then it belongs to the actual published `(8,28)` case of GGHV Proposition 4.3. The missing global-minimality hypothesis suggested in the prior gate is **not a hypothesis of the applicable chain theorem**. The complete fixed source edge forces the table's successor `(11/4,7)`, not merely its numerical degree pair. Consequently Proposition 4.3 supplies existence of one of its two literal polynomial/Laurent polygon systems with bracket `x^2`, at external-theorem trust. This is an existential implication, not a newly constructed coefficientwise transport.

Composing that implication with the independently retained external exclusion of **both** literal systems would exclude this D108 full-physical-Jacobian source family at the **externally trusted conditional tier**. It would not require another D108 solve. The independent proof-audit debt in the internal use of Corollary 7.4 is recorded separately below; it is not silently converted into an additional hypothesis of Proposition 4.3.

## 1. Inputs, versions, and publication boundary

This task begins after the terminal producer report `xmodel/d108-source-frontier-interface-astra-20260906.md`, SHA256 `39bbe041f6ad7ba704c58fe7dc442f46e91caa01fe2a34333c7250ac7a421ce7`, and the readable terminal gate body `xmodel/d108-source-frontier-gate-fable5-20260906.md`, SHA256 `e5f09997493d1e71ce862a43e84d464ea9232cb8e10ccdbb32cc2761108857f5`. The latter's workflow lifecycle was not promoted when assigned; its prose verdict is not used as a substitute for the primary statements. No live peer report was read. All earlier charged files remain unchanged.

History checksums read at the start of this task:

| File | SHA256 |
|---|---|
| APPROACHES.md | `7d6fcafe24500f9ec203d9a9d9a14f575327ff349a2af9bb7b47eca9359a4788` |
| AUDIT.md | `865b459ab70717ddae33eae2043b328b60bf01afc406058080a207f186bdab7b` |
| ladder/REDUCTION.md | `7f901db6c8e6fbc80c85581a331c247d5c219e23bf286136f77fbc0182ebbe1b` |

New primary snapshots are in `box/d108-published-case-interface-20260906/`. Acquisition used the following exact primary URLs; local `pdftotext -layout` produced the corresponding text files.

| Citation in GGHV 2022 | Exact primary/version and local basename | PDF SHA256 | Text SHA256 |
|---|---|---|---|
| [5] | [Some algorithms related to the Jacobian Conjecture, arXiv:1708.07936v1](https://arxiv.org/pdf/1708.07936v1), `ggvh-algorithms-1708.07936v1` | `e04e3bfd88c62346c467ec7c32f5bb236cdcb2ee4796525408c0c8d68632fcdb` | `49df06d11bbc4556a9b09771cdd60ca40a75b7542d327bbb622e09434e6a467e` |
| [2] | [The two-dimensional Jacobian conjecture and the lower side of the Newton polygon, arXiv:1605.09430v2](https://arxiv.org/pdf/1605.09430v2), `ggv-lower-1605.09430v2` | `c3828c7911619aff1c3ffa86bdb00f3822ab30c4f4af23f6abdb2baff6a4afab` | `77ae98339d7a70c476d89c01a2d38ba3aa1af98fbb0ba9da32c1759fde87a221` |
| [6], published | [Approximate roots and intersection numbers, Pro Mathematica 30(60), 2019, pp.51–89](https://revistas.pucp.edu.pe/index.php/promathematica/article/download/21094/20844), `ggvh-roots-published2019` | `823ff05f02615fc3ebb9f9763819bbce592fb7b5e4b1063ac07c658be01812eb` | `ca27cddafac8cfb40ae8f261378d7f449b81e06a55924d7d64a4daff805ec2d7` |
| [6], version crosswalk only | [arXiv:1708.09367v2](https://arxiv.org/pdf/1708.09367v2), `ggvh-roots-1708.09367v2` | `331fe6361ed98ec31795cc5f42ffc0a7af6ae70510fcdf78cce9672cad08c3f1` | `e9f84e0eeb542203b5e6926843fe4562f37b3c27575cfce98d9fee7936b91a6e` |

Important version distinction: **published Proposition 2.5 is arXiv-v2 Proposition 1.5**. ArXiv-v2 item 2.5 is a different remark. This report uses the published proposition actually cited by GGHV, including its preceding equations (2.1) and (2.2).

Previously frozen [GGHV arXiv:2204.14178v1](https://arxiv.org/pdf/2204.14178v1) PDF/text remain at `box/ideation-20260906T1210Z/ggvh-2204.14178v1.{pdf,txt}`, SHAs `ac18e80cc2391f204f73b908a6a6557eb1141d9fbb5ebdb9f6e0a22121db80bd` / `f3eca2a560b98784ec787104c8b9049ca44bc3dde4bacb38f121376736d02368`. GGV1 means *On the shape of possible counterexamples*, J. Algebra 471 (2017), primary local PDF `refs/guccione_valqui2017_ja471_shape_counterexamples.pdf` SHA `8b4267512c438c7ceda7e30cb63c225a554cf0d2195dc6325e9d1e42ab520c60`, text `box/census-coverage-20260905/core-ggv-layout.txt` SHA `e3694dde3f83c2ab6ed8d957fc6b53472e6a6dd55486af1dff345eade39e37b1`.

## 2. Exact statement interface, without global minimality

Work over a characteristic-zero field K, extending to its algebraic closure for root choices when necessary. Write `L=K[A,B]` and `L^(l)=K[A^(1/l),A^(-1/l),B]`. A pair in the sense of GGV1 Definition 4.3 has coprime integers m,n>1, nonzero constant Jacobian, equality of its total-degree and A-degree ratios with m/n, and negative `(1,-1)` value at `en_(1,0)(F)`. Standard adds membership in `L^(1)` and the same negative sign at `st_(1,0)(F)`. Global minimality, separately defined using the least gcd B among all counterexamples, is not in that definition.

Although the introduction to [5] §2 discusses a globally minimal standard pair as one application, its **Theorem 2.20** quantifies over every standard `(m,n)` pair. Its proof constructs a sequence from that pair and uses no equality of its gcd with the global minimum B. Section 2.4 and the sentence after Definition 2.25 likewise assert that chains from a standard pair are admissible. Section 3 introduces the `(m,n)` restrictions for a pair generating such a chain. Sections 5–6 list those chains and families. Minimality is used in [5] to deduce a lower bound for the global invariant B, not to restrict the quantifier of Theorem 2.20.

Here the earlier exact source audit, also independently checked by the terminal gate, gives the following before any residual equation is imposed:

`h_top=(X+W)^8 W^28`, `deg h=36`, `deg D<=37`, `deg C<=38`,

`F=h^3+(3D+a)h/2+C`, `G=h^2-bh/3+D`.

The determinant-one substitution `A=X+W, B=W` gives total degrees 108 and 72 and unique highest-A faces `A^24 B^84` and `A^16 B^56`. Thus every actual Keller specialization is a standard `(3,2)` pair. The degrees do not divide one another, so such a Keller specialization is a counterexample rather than a polynomial automorphism, as in the previously charged one-way full-ideal gate. This paragraph assumes a Keller specialization only conditionally; it asserts none exists.

The *complete* weight-`(4,-1)` faces are

`ell(F)=[A(AB^4-1)^7]^3`, `ell(G)=[A(AB^4-1)^7]^2`.

Their normalized endpoints are `A0=(8,28)` and `A0'=(1,0)`. There is no intervening edge between the `(1,0)` normal and `(4,-1)`: every source monomial satisfies both relevant half-plane bounds, and their two bounding lines meet at the unique highest-A monomial. The positive combinations of the two normals therefore expose just that vertex. This is the first edge in the standard-pair chain, of type II.b: its univariate polynomial has multiple distinct roots and its lower normalized endpoint has positive `(1,-1)` value.

Set `z=A^(1/4)B`. The faces become `A^m (z^4-1)^(7m)` for m=3 or 2. All four roots lambda of `z^4-1` are nonzero and simple in characteristic zero; the elementary Bezout identity is

`(z/4)*(4*z^3)-(z^4-1)=1`.

Every such root has multiplicity `7m` in the F or G face. The root transformation in [5] Theorem 2.20(8) therefore has l1=4 and forces

`A1 = (1,0) + 7*(1/4,1) = (11/4,7)`.

For clarity, substituting `B -> B+lambda*A^(-1/4)` gives a factor of exact B-order 7 in h's face: `((V+lambda)^4-1)^7` has V^7 coefficient `(4*lambda^3)^7 = 16384*lambda`, using lambda^4=1. It is nonzero for every root choice. Lower-weight source terms remain lower-weight under this homogeneous Laurent transformation; the theorem, not a truncated polynomiality guess, supplies the regular-corner successor.

Theorem 2.20 removes any intervening type-III corners while preserving this successor. GGV1 Proposition 5.19 allows only type I or II after those steps, with type II requiring gcd(a,b)>1. Here gcd(11,7)=1, so the resulting corner is type I. The type-I necessary inequality `4-11/7>1` is also satisfied. Thus this is the length-one chain `((8,28),(1,0)) -> (11/4,7)`, with `(m,n)=(3,2)` and degree maximum 108. This is exactly [5] §6, p.27, the `(8,28),(11/4,7),(3,2),108` row. The other `(8,28)` row has successor `(7/4,3)` and degree maximum 144 and is not being substituted for this one. The source has supplied the actual chain data that identify the published case.

## 3. One implication table and its trust boundary

| Arrow | Exact antecedent and conclusion | Status / trust |
|---|---|---|
| Literal source -> standard pair | Nonzero constant physical J, fixed source formulas, determinant-one `(A,B)`, exact degree/leading-face bounds -> standard `(3,2)` pair, A0=(8,28) | Exact source arithmetic + the charged one-way physical-realization gate; no source necessity claim |
| Standard source pair -> actual chain row | Full fixed edge, roots of `z^4-1`, multiplicity 7m -> A0'=(1,0), l1=4, A1=(11/4,7); type III can be removed and type II is impossible at gcd(11,7)=1 | Exact tiny root arithmetic + **EXTERNAL-THEOREM** [5] Thm2.20, GGV1 Prop5.19; no global-minimality assumption |
| Chain row -> published case | This complete chain and (m,n)=(3,2), degree maximum108 -> the `(8,28)` case in [5] §6 and GGHV §2 | Literal table/case identification; **discharged**, not just a match of two integers |
| Published case -> one of two systems | A counterexample in that case -> P*,Q* in `L^(1)`, bracket `x^2`, with exactly one of the two Prop4.3 polygon pairs | **EXTERNAL-THEOREM** GGHV Prop4.3; its existential conclusion is usable without explicit coefficientwise cuts |
| Two systems -> contradiction | Accept the retained external exact exclusions and their faithful transcription/normalization of both polygon systems | Existing externally trusted conditional result; **not freshly audited or replayed in this task** |

There is **no remaining named missing hypothesis at the published statement interface** established in these first four arrows. This does not make every internal proof step independently replayed, nor does it construct the coefficient functions of the x^(-2)/x^(-3) cuts. The prior label `GGV-CUT-EXHAUSTIVENESS` remains appropriate for that stronger internal, coefficientwise/reproof deliverable, but should not block use of the published existence theorem once its actual case antecedent has been checked.

The two final polygon pairs are the smaller pair

`P*: conv{(0,0),(1,0),(8,14),(8,16)}`,

`Q*: conv{(0,0),(2,1),(12,21),(12,24)}`,

and the larger pair obtained by adding `(0,8)` and `(0,12)`, respectively. All lattice points of either hull have nonnegative exponents, so the final `L^(1)` membership is actually polynomial membership. Their bracket is `x^2`, not a nonzero constant. Vertex attainment and normalization belong to the target-system/external-certificate interface and cannot be dropped. No source separation parameter has been identified with a cut-root difference. Field extensions for roots are allowed; no generic localization deleting exceptional Keller strata is used in the case-identification argument.

## 4. Exact hypotheses of the two formerly unread opposite-edge citations

These are local homogeneous-polynomial results. Neither has a global-minimal-pair antecedent. In [2] Notation3.10, if `en(R)-st(R)=(u1/l,n1)` and `st(R)=(u2/l,n2)`, then `gap(rho,l)=rho/gcd(rho,l)`, `N1=n1/gap(rho,l)=gcd(u1,n1)` and `N2=gcd(u2,n2)`.

**[2], Proposition 3.12 (v2 pp.11–12).** Take a direction strictly between `(0,-1)` and `(1,-1)`, nonmonomial homogeneous `R,T in L^(l)`, an integer i>=1 with `[T,R]=R^i`, and positive weighted value `u=v(R)>0`. Choose an integer L>0 with `L*u+rho+sigma>0`. With `R=x^(u/rho)r(z)`, `z=x^(-sigma/rho)y`, and N1,N2 as in Notation3.10, the conclusion is one of: a single nonzero-root linear power with rho dividing l; a root multiplicity theta<=N1 with `0<t<L*theta` and direction `-dir(t*st(R)+theta*(1,1))`; or theta dividing N2 with the same directional relation and positive starting y-exponent. The final single-root clause when l=1 gives `v_(1,-2)(en R)>0`. The proof was read in full; no hypothesis about the global gcd invariant occurs in it.

**[6], published Proposition 2.5 (pp.56–58).** Fix integers a,l>0, a/l>2, b=2, and a direction strictly between `(0,-1)` and `(1,-1)`. Its equivalence concerns existence of `c>0`, `d in {0,1}`, and homogeneous R,T satisfying the preceding (2.1): positive weight, `[T,R]=R^i` for i>=1, end `(a/l,2)`, start `(c/l,d)`. Crucially it additionally imposes (2.2): after removing the x monomial, R is **not** a power of one linear polynomial. The equivalent arithmetic condition is

`exists integer Delta: l<Delta<a/2, (a-2*Delta) divides (Delta-l)`,

with direction proportional to `(l,-Delta)`. The equivalent item(3) retains its primitive gcd ratio theta=1 and the integer `0<t<L`, with L the least integer for which `L*v(a/l,2)+rho+sigma>0`. The proof first shifts a split d=0 case to d=1 and then proves both directions of the divisibility criterion. These are existential statements about local homogeneous data, explicitly introduced without claiming an ambient Keller pair exists.

For the normalized endpoint `(7,2)` and l=1 used in GGHV's proof, the split-root criterion permits **only Delta=3**: the integers allowed by `1<Delta<7/2` are 2 and 3, and `3 does not divide 1`, whereas `1 divides 2`. Thus a split edge has direction `(1,-3)`. In the separate single-root case of [2] Prop3.12, rho=1 and positive weight `7+2*sigma>0` with sigma<=-2 allow `(1,-2)` or `(1,-3)`. This precisely preserves the one-root/two-root distinction in GGHV; applying the split-root proposition to every edge would incorrectly delete the `(1,-2)` branch.

These arithmetic specializations check the citations once their homogeneous R,T and positivity antecedents have been obtained. They do not manufacture those objects on arbitrary source base points.

## 5. Corollary 7.4: base hypotheses versus the range of its conclusion

The earlier gate's blanket `CONFIRMED` must be read with the following distinction. In GGV1's direction convention, after swapping coordinates the base data really do satisfy Cor7.4: total-degree and y-degree ratios3/2, J a nonzero constant, direction `d0=(-1,4)` in Dir(P), weighted value12>0, normalized starting corner `(28,8)` with 8<28, and auxiliary starting point `(21,6)=(3/4)(28,8)`.

But the corollary does not state that every earlier direction has a `4m`-th-power face. It imports from Prop7.3 the direction

`d_tilde = min{d in Dir(P) cap [(0,-1),d0] : v_e(P)>0 for every d<=e<=d0}`,

and propagates only for `d_tilde<=d<d0`. An application to an unidentified lower predecessor must show that this target direction is in that interval. The fixed corner `(84,24)` proves positivity on the cone spanned by `(1,-1)` and `(-1,4)`: its two values are60 and12, so every nonzero nonnegative combination is positive. It does **not by itself** prove positivity farther down toward `(0,-1)`. GGV1's proof of Prop7.3 and Cor7.4 refers to the earlier analogous proofs; [2] Prop2.2/2.7 invokes a nonzero axis term via van den Essen10.2.6. This task does not independently supply every instance of that further chain in the swapped source coordinates.

A genuine negative control makes the boundary concrete. Put `H=y(y*x^4-1)^7`, `P=H^3+1`, `Q=H^2+1`. The corresponding unswapped pair has the same two numerical degrees, right-face ratios and full initial edge used above, but J=0. The predecessor to `(-1,4)` for P is `(2,-7)` and has weighted value0, with endpoints `(0,0),(84,24)`. Thus the edge/numerical data alone cannot establish the missing range membership. This is **not** a Keller counterexample, is not claimed to satisfy the 14 source residuals, and does not refute Cor7.4 or Prop4.3.

There is also a convention correction to the gate's suggested Euler-uniqueness repair. GGV1 Prop2.11 is stated for `V0={rho+sigma>0,rho>0}`; it cannot be applied directly at `(-1,4)` merely by citing an s>0 factor. The safe argument applies it **before swapping**, at `(4,-1)`: `z=A^(1/4)B`, and `(z^4-1)^(7m)` has four distinct roots. Uniqueness then transports through the coordinate swap (and its bracket sign). The producer's multiple-factor argument is valid in those original coordinates. The swapped description `y^m(x^4*y-1)^(7m)` uses a different one-variable convention. This correction changes no explicit Euler identity and no q=4 conclusion.

Therefore: the local positivity-range step remains **independent proof-replay debt**, not a newly discovered contradiction and not an unfulfilled antecedent of the externally imported Proposition4.3. A future internal reproof should name and discharge it; a solver should not be commissioned simply because it remains un-reproved here.

## 6. Conditional composition with the retained external exclusions

All of `jc72108/CROSSCHECK.md` was read, SHA256 `70bc10f8810e65400b40ddd88a5b575acd7dc43676432ec9a37d43e0a8ef40ba`. Its recorded historical checks distinguish the two literal systems, check bracket/support/normalization agreement, and record external Helali and Suzuki exclusion paths for both. Root separately confirmed that those external exclusions survive the msolve errata; this task does not revive the superseded internal cCa2/cCa6 or msolve-header claims.

The current [Helali repository](https://github.com/bilLkarkariy/jc2-72-108-exact-certificates) still states exclusion of both transcribed coefficient systems while conditioning the degree-pair conclusion on the published reduction and faithful transcription. The fetched README snapshot is `helali-readme-snapshot.md`, SHA256 `125f186a7b66651a54dee670a8fdfdfc9b22be27fe27f477169a0d996a96673d`. Its current web statement is provenance, not a fresh certificate replay. The Suzuki archive is identified historically as Zenodo21483636; this task did not obtain or replay it (the web open failed). No giant certificate was downloaded, inspected, or executed, and no absent historical archive was represented as present.

The logically usable composition is:

`D108 source Keller point -> standard pair with the actual published chain -> Prop4.3 polygon pair -> contradiction from the retained external exclusions`.

Subject to those explicitly imported reduction/transcription/exclusion statements, this retires the **literal D108 full-physical-J source family** as a characteristic-zero counterexample search. It supplies no new exact unit-ideal certificate and does not prove a universal degree>=125 theorem independently of its published reduction perimeter, much less JC2. An unrelated source chart is not covered by matching its name to D108. Conversely, no proof that every Keller pair belongs to our source chart is needed for this one-way exclusion of that chart's physical Keller points.

## 7. Replay and exact read/unread inventory

Run, read-only, from any working directory:

`python3 /home/ubuntu/jc2/box/d108-published-case-interface-20260906/controls.py`

The stdlib-only checker reparses the pinned raw source, checks its support bounds and literal fixed face, computes the tiny root-shift polynomial in `Q[lambda,V]/(lambda^4-1)`, verifies the forced successor and the split/single direction arithmetic, and checks the negative positivity-control support. It returned `D108_PUBLISHED_CASE_SMALL_CONTROLS_PASS`. No CAS package, AWS worker, source-system expansion or solver is used. The shifted degree28 control has only22 quotient-ring terms; this is not a performance claim about the source ideal.

Six genuine alterations are fed to these same verifiers and rejected: source highest-face coefficient1->2; root power7->6; root equation lambda^4=1->2; ramification denominator4->3; successor11/4->7/4; and incorrectly allowing the split-root direction `(1,-2)`. The checker does not claim to test imported theorem proofs, the exhaustive table computation, source properness, a Keller point, full transport, or external exclusion certificates.

Read in full for this task: [5] Theorem2.20 including its entire proof; §2.4's admissibility derivation through Definition2.25; Proposition2.5 including its proof; all of §§5–6 including the family exclusions and Prop6.1 proof; [2] Prop3.12 including its entire proof and adjacent Notation3.10/Remark3.13, and the local §2 statements/proofs2.1–2.7; [6] the entire published §2 including Prop2.5's four-way proof and both preconditions; GGV1 Prop5.19's proof, the literal Def4.3, Prop7.3 and Cor7.4 statements/proof text; GGHV Prop4.3's entire proof; the entire historical CROSSCHECK.

Not claimed fully read or independently proved: every cited dependency of these proofs; all nine algorithm correctness proofs/implementations and their enumeration output; GGV1's whole paper, its Prop7.1/Cor7.2 proof chain and the complete Prop8.2 proof; all of GGHV's `as in Prop4.1` successor analysis; van den Essen's book10.2.6; Helali/Suzuki's large exact certificates and all their external mathematical dependencies. Merely snapshotting all pages does not count as reading the whole papers.

All task writers terminate before final custody publication. Parent may grant a fresh read-only independent review. Earlier artifacts, canonical ledgers, source bytes and jc2-lean were not edited; no AWS action occurred. The transactional report manifest and `box/d108-published-case-interface-20260906/custody.json` record terminal hashes and custody.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `22045`.
- Body SHA-256:
  `ebfaeada5fde63da102c5eaa59185ca35b407cbfa37f26fa5401bc36173f5b5d`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
