# Coordinator integration: multipole selected-exit attachment and shared inequality

Date: 2026-08-28  
Lifecycle: **PROMOTED at selected-exit/MFE inequality scope**

## Evidence

```text
86b491adc6ba6b21fcec5a8722126d80f3666d8e3d9f2cdcf4568d408bbc83a8
  xmodel/sigray-multipole-global-first-exit-partition-sol-ultra-20260828.md
ac49c025e3e010d3ecaf3839adf51c40cb88b0088198ae1c5ab1198e07cc8004
  xmodel/sigray-multipole-global-first-exit-partition-hostile-review-gpt56-20260828.md
9f4526f209366098f12bbe60387a190c6d2942a374c05fad092917bc79145f14
  xmodel/sigray-multipole-selected-orbit-attachment-repair-gpt56-20260828.md
f55a00f5259d77766cc8179f3d1248ee0c1320daf411f04758487d2e94e216bb
  xmodel/sigray-multipole-selected-orbit-attachment-hostile-fable5-20260828.md
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
  refs/sigray_full.pdf
```

Fable5's independent hostile verdict is `PASS-WITH-REPAIR`. The theorem is
promoted only after applying the exact endpoint repair below. The frozen
producer, first hostile review, repair packet, and Fable report remain
unaltered.

## Correct ambient object

Definition 3.3 already makes `T_a^*` the common-prefix/contact quotient:

```text
I_P(t)=I_Q(t)  iff  t<=O(P,Q).
```

Thus a split cannot remerge. For a flag `H=I_P(v)`, its rootward segment
`I_P([0,v])` is independent of the representative. If the pole flags are
`I_(P_j)(v_j)`, set

```text
U^full = union_j I_(P_j)([0,v_j]).
A_P    = {t : I_P(t) in U^full}
       = [0, max_j min(v_j,O(P,P_j))].
```

In particular `A_P` is rootward closed: a ray cannot leave `U^full` and
later re-enter it.

## Mandatory endpoint repair

The repair packet's display `(3.2)`, `O(P,P_j)=u` for every pole
representative through a selected-exit base `F=I_P(u)`, is too strong at a
pole endpoint. Replace that paragraph by the following argument.

Fix a pole segment `I_(P_j)([0,v_j])` containing `F`. If it continues above
`F` (`u<v_j`), contact greater than `u` would give, on a sufficiently fine
common denominator, the same corrected-Statement-3.18 child on the pole
segment. The selected direction would then be a pole-chain arrival, contrary
to its definition. Hence `O(P,P_j)=u` and
`min(v_j,O(P,P_j))=u`. If instead the pole segment ends at `F`
(`u=v_j`), contact may exceed `u`, but its contribution is still
`min(v_j,O(P,P_j))=u`. Pole segments not containing `F` contribute strictly
less than `u`. Therefore in every case

```text
A_P=[0,u].
```

This is the only conclusion used downstream. No consumer uses the false
universal equality `(3.2)`.

## Promoted selected-exit lemma

For one orbit-set of selected exits at each vertex of the set-theoretic
union `U^full`:

1. each selected positive exit has a Statement-7.3 cv witness outside
   `U^full`, attached uniquely at its base vertex;
2. distinct effective cyclic direction-orbits at one vertex have distinct
   witnesses; and
3. exits based at different vertices have distinct witnesses.

Corrected Statement 3.18 supplies the orbit-to-actual-direction bridge.
Repaired Propositions 6.7--6.8 show that every remaining down direction is
a pole arrival and is removed before pricing. Shared suffix vertices occur
once in `U^full`, and a merge arrival is not charged once per incoming pole
path.

## Promoted MFE inequality

Apply actual-weight `(C7.1*)` once to the pairwise-distinct selected y-side
witnesses plus the separately certified x-side witness of weight at least
`psi`. The local Section 9/AF2 price bounds then give

```text
sum_(F in U^full) lambda_F^exit <= td(f,g)-1-psi.       (MFE)
```

This is now GREEN at the selected-exit/shared-inequality scope. Consumers
must form one actual direction-orbit set per vertex of the union and count
the shared suffix once.

## Boundaries retained

- This is an inequality only. It does not restore printed `(22)`, literal
  `delta_a`, `(22-cl)`, equality or slack itemization.
- It does not transport a fixed or cross-fibre `kappa`; each cv witness uses
  its own actual weight.
- It does not prove MP8's categorical no-refinement/no-charge claim. Local
  zero-exit calculations and the resonant witness remain valid only at their
  stated scopes.
- It proves neither an exhaustive root/SF1 book nor a `td=6` exclusion. The
  corrected all-`M=1` root-meet theorem is a separate DEPTH/H1 result.
- Any engine that prices per incoming edge or duplicates a shared-suffix
  vertex is nonconforming even though the mathematical theorem is now
  promoted.

