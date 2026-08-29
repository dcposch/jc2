# `(8,12)` order two: exceptional `K` cubic-form custody

Date: 2026-08-26

Status: **EXACT COEFFICIENT EMISSION.  THE BROAD K-SATURATION TIMED OUT;
NO SUPPORT OR SOURCE-ACCESSIBILITY VERDICT IS TAKEN FROM THAT RUN.**

## 1. Frozen source and emitted forms

The complete frozen ordinary-Faber compiler is

```text
4ba55c2fc70cbfe41d9479b65f25095473c764e0b724bbb78d7d505b07f1f492
  cases/max12_812_order2_affine_faber_exceptional_j_p3_20260826/
  compile_exceptional_p3.py
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/
  aws_compile_v2_jsat/run/output/compiled_v2/tails.json
```

The canonical exact-Q text of all four full cubic forms `K1,K3,K5,J` is
frozen verbatim at

```text
36141b92e1bf8f83b25a23b0d4aa374d1a8a4dca761f8d7a3af68f2ab12b91f3
  cases/max12_812_order2_affine_faber_exceptional_j_p3_20260826/
  aws_q_v2/run/exceptional_K_q.stdout
```

They are the four lines beginning

```text
EXCEPTIONAL_P3_K_R1_W3=
EXCEPTIONAL_P3_K_R3_W3=
EXCEPTIONAL_P3_K_R5_W3=
EXCEPTIONAL_P3_K_J_W3=
```

and are not abbreviated or reserialized in this note.  The independent
characteristic-65521 emission is frozen at

```text
a1cbdc3863f99be301e96f5970617675ab38e3e5ed6736dc91b83dd667e144ea
  cases/max12_812_order2_affine_faber_exceptional_j_p3_20260826/
  aws_p65521_v2/run/exceptional_K_p65521.stdout
```

The prime lane is only a software control.

## 2. Exact coordinates

The forms use

```text
r=p^2/4-D,
k10=1,
k6=5D/8+t^2*b,
k2=-5D^2/16+t^2*g,
c=t*x,
n3=t*y,
n1=2D*t*x+(p/2)*t*y+t^3*u,
n2=t^2*e2,
n0=t^2*e0.
```

Each displayed form is the exact `t^3` coefficient of the corresponding
complete ordinary-Faber row; the `J` line is four times row seven.  Both
lanes printed `EXCEPTIONAL_P3_TCOEFF_CONTROL=1` and
`EXCEPTIONAL_P3_K_LOWER_ZERO=1` before the broad standard basis began.

## 3. Timeout firewall

The broad projective K saturations exceeded 1800 seconds in both fields.
Their validation files have identical SHA

```text
452bbb0921caa05e2a58cbf4d5eeaa13ab921c68e9e9727af4d876e1758f789b
```

and record `engine_rc=124`, `validator=FAIL_ENGINE_OR_TIMEOUT`.  Therefore
the runs prove no K support statement.  The four forms precede the timed
standard-basis command and are deterministic direct coefficient
extractions from the frozen compiler; this note freezes those forms only.

The dedicated narrow K-IFT and delayed-source clients have separate PASS
custody.  No total-Rees, terminal/Taylor, order-two, or JC2 claim is made
here.
