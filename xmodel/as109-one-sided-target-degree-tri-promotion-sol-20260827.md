# Promotion — AS109 one-sided target-degree obstruction (`AS-TRI`)

Date: 2026-08-27

Status: **PROMOTED AT THE EXACT 109-ADIC POLYNOMIAL-LIFT SCOPE BELOW.**

## Inputs and custody

- Producer: Opus5 cross-pollination report, §2.4,
  `xmodel/ideation-20260826T2350Z-crosspollination-opus5.md`, SHA-256
  `e645d822aa49199b69464f98b7b94846e6773e635bd389cb94a3a24806a3e341`.
- Different-model hostile review: Grok 4.6,
  `xmodel/as109-one-sided-target-degree-tri-review-grok-20260827.md`,
  SHA-256
  `4a49110d83c80de7e1654b866ea5ff293aafb43e049fcad96078a506360726ca`.
- Evidence: independent exact hand algebra over the DVR
  `R=Z_109`, with fraction field `K=Q_109`.  No CAS, numerical inference,
  web source, or formalization result is consumed.

## Promoted theorem

Let

```text
P = x - x^109 + 109*A,    Q = y + 109*B
```

belong to `R[x,y]`, and suppose `det J(P,Q)=1`.  Then

```text
deg_y(Q) >= 2, equivalently deg_y(B) >= 2.
```

Indeed, if `Q=q_1(x)y+q_0(x)` and
`P=sum_j p_j(x)y^j`, the coefficient of `y^m`, for
`m=deg_y(P)>=1`, in the Jacobian is

```text
p_m' q_1 - m p_m q_1' = 0.
```

In `K(x)` this gives `(p_m/q_1^m)'=0`, hence
`p_m=c q_1^m` for a constant `c in K`.  The seed congruence gives
Gauss valuations `v(p_m)>=1` and `v(q_1)=0`, so `c in 109R`.  The integral
target shear `P -> P-cQ^m` preserves both the Jacobian and the seed residue
while strictly reducing `deg_y(P)`.  Iteration ends with `P=p_0(x)`, where
`p_0'q_1=1` forces `p_0` to be linear, contradicting the polynomial
congruence `p_0 = x-x^109 (mod 109)`.

This proof is characteristic-zero 109-adic algebra.  It would be false if
`Z_109` were incorrectly read as `F_109`; polynomial reduction is not
evaluation as a function on the finite field.

## Licensed compositions

- With the already reviewed two-sided floor
  `max(deg_y A,deg_y B)>=12`, rule out the floor shapes
  `(deg_y A,deg_y B)=(12,0)` and `(12,1)`.
- Use the proof as a positive control for a residue-preserving integral
  target-shear ladder.

## Firewall

This theorem supplies no bound on `deg_y A`, no two-sided floor, no
max-12 routing theorem, no automatic integrality for higher-degree
Abhyankar steps, no existence or nonexistence theorem for AS109 lifts, no
support bound, no marked collision, no residue-field or power-series
version, and no JC2 conclusion.  The review separately confirms the
valuation criterion for an integral top-degree shear, but not the
producer's later monicization/Frobenius paragraph.  In that criterion,
`v(c)=0` is integral but residue-changing; only `v(c)<0` is nonintegral.
