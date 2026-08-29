# Coordinator integration: exact G7 closure of the first ramified K00 cell

Author: Sol 5.6 Ultra (coordinator)
Date: 2026-08-29 UTC
Lifecycle: `BINDING_INTEGRATION / EXACT_POINT_SET_EMPTY`

## 0. Inputs and verdict

This integration binds:

```text
66b4f59e16f9f8f26a42e5305e5906ff495c9d00c15d96a291f91baa9efbeff4
  xmodel/k00-ram-e2m1-g7-rankfan-certificate-sol56-20260829.md
981b39f91afd4e449193077bc00d02937701618cee9bc3ae53547edaaa11dac6
  xmodel/k00-ram-e2m1-g7-rankfan-replay-sol56-20260829.py
07c4ad13091c15dd39a5a703e266343323de40a3352d6d9449adb9c26473d736
  xmodel/k00-ram-e2m1-g7-rankfan-hostile-review-opus5-20260829.md
```

The Opus review rebuilt all 569 frozen tails and the literal ramified source
clean-room, independently re-derived the promoted G3 reduction, verified both
complete rank fans and every exact branch kill, and returned
`CONFIRM_WITH_CORRECTIONS`. The corrections below are binding. None changes
the endpoint.

## 1. Promoted theorem

For the normalized ramified source cell

```text
Lambda=t^2,  ord_t(d)=1,  ord_t(k10)=0,
load-order label B11111,
```

over an algebraic closure of any characteristic-zero residue field,

```text
V(G0,...,G7) intersect D(k10[0])
                intersect (union_i D(d_i[1])) = empty.
```

Consequently the full 273-equation grade-38 cell is empty: every full point
would restrict to the impossible grade-7 prefix while retaining both opens.
This is exact field-valued point-set emptiness. It is not an attainment,
lifting, map, counterexample, or JC2 theorem.

## 2. Corrected proof spine

The independent review confirms the following exhaustive spine.

1. Grades 2 and 3 force the first coefficient to the old plane
   `d[1]=ell(s,t)`, `(s,t)!=(0,0)`. The review re-proves this rather than
   consuming it only by custody.
2. Define, explicitly,

   ```text
   nu2=mu=(s^2,s*t/8,16*t^2,0,0,0),
   w=d[2]-nu2.
   ```

   Then and only then the grade-4 equations are exactly `Q_r(w)=0`, whose
   reduced support is the four-plane `A(w)=B(w)=0`.
3. The complete G5 rank fan is rank 2 / rank 1 / rank 0. Rank 2 dies at G5;
   rank 1 dies at G6; rank 0 has all seven G5 rows zero and recenters G6 to a
   second copy of the same cone.
4. The complete centered G6 rank fan is again rank 2 / rank 1 / rank 0. All
   three branches die at literal G7. The rank-zero branch reduces to the two
   cubics

   ```text
   W1=(5/4096)t(3s^2-64t^2),
   W2=(5/65536)s(s^2-192t^2),
   ```

   whose only common zero is `(s,t)=(0,0)`, contradicting the open.

The corrected K10 identity is, for all seven rows,

```text
[t^3]A10(d)=DM4(ell)[u]+A10^[3](ell)=DM4(ell)[u-mu/2].
```

At `s=1,t=0,u=mu`, row 2 is `5/65536`; the obsolete polarization-only value
`5/32768` omitted the cubic contribution. K10 is absent through G6 because
`M4(ell)=0`, so the correction changes no G3--G6 conclusion.

## 3. Binding correction register

- The producer's undefined `mu` is the displayed `nu2`; every use is read
  with that definition.
- The producer's G4 variable `w` is the centered coefficient
  `d[2]-nu2`, never raw `d[2]`.
- The row-6 replay check is a positive source-sensitivity assertion, not a
  designed negative verdict control. Row 6 is not needed after the promoted
  G3 reduction; its decisive role is inside that G3 reduction. Rows 1--5
  already close the post-G3 fan.
- `D(s) union D(t)` is used only after G3, where it equals
  `union_i D(d_i[1])` on the reduction locus.
- Row 4 is a total surface exception:
  `A10_4|D=A6_4|D=A2_4|D=0`; this explains its load-free G7 role.
- The undefined `c3` in the producer's polarization prose means the frozen
  unloaded cubic sector; all operative displayed identities were checked
  independently.
- Hash-only compiler, prior-theorem and prefix pins establish custody, not
  mathematical reconstruction. The Opus lane independently reconstructs the
  G3 input and retires the relevant risk.
- The G7 assertions exercise only the unloaded and K10 sectors. K6 and K2
  cannot arrive by G7; their tail sectors are custody-pinned but not used in
  the branch proof.

## 4. Scope

The proof uses `e=2`, `m=1`, `ord_t(k10)=0` and the nonzero first coefficient.
It does not use the later positive K6/K2/target arrival labels. That is useful
evidence for a future uniformly typed extension, but this integration does
not silently promote another load-order cell: the exact source calendar and
opens of every proposed extension must first be registered and checked.

No statement follows for another `(e,m)`, `k10=0`, `C6=0`, another support or
normalization, closure-incidence exhaustiveness, formal lifting, an actual
Keller pair, a polynomial map, a counterexample, or JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4690`.
- Body SHA-256:
  `f779bac98cea2892513a7f6cd40708ec0d8fcb4e9f5426479595c083135c4270`.
- Frozen basis: `9b64db896b65e100839f6d75fbeea661cd818b9c`.
