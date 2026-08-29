# Promotion: universal odd-row Laurent-to-Faber pole functional

Date: 2026-08-26

Status: **PROMOTED FORMAL THEOREM AFTER DIFFERENT-MODEL HOSTILE REVIEW.**

## Frozen custody

```text
97cb6fedc22c3352b304684c0e46e768eb12ce579ba52dbf24bb38be78533263
  cases/max12_812_order2_square_owner_d1_universal_odd_pole_recurrence_20260826/RESULT.md
6ed0d583e64eecc9403f135692d0ac0b0158a3717ddd4daad84d4df76394ba87
  cases/max12_812_order2_square_owner_d1_universal_odd_pole_recurrence_20260826/EVIDENCE.sha256
9990ba104bb7d5bf4e494e5faad59545b6a6500cbdd3db571ee25429d3e13ed0
  cases/max12_812_order2_square_owner_d1_universal_odd_pole_recurrence_20260826/FREEZE.sha256
81b0f9d772add009b1d7c6ed0caa9ef13098fc72f8921e502128ba1402901f6b
  cases/max12_812_order2_square_owner_d1_universal_odd_pole_recurrence_20260826/PRODUCER_FREEZE.sha256
0263315e1df7f6044870e6c8fec26f36fe4d6860e44bb015e2ab903bcfae1a7e
  xmodel/max12-812-order2-square-d1-universal-odd-pole-recurrence-hostile-review-grok-20260826.md
```

The hostile reviewer rehashed the complete V2 custody, reconstructed the
frozen odd Faber block, and rederived the unbounded identity without using
the finite replay as an induction.  The first wrapper attempt failed before
mathematics and remains no-verdict.  Exact Q and the independent r6d modular
assertion run are software controls; the promoted theorem is the formal
degree proof.

## Promoted formal theorem

Put `s=p/2` and encode the odd Laurent and ordinary Faber coordinates by

```text
Y(x)=sum_(m>=0) h_(2m+1)*x^m,
Phi(x)=sum_(m>=0) Phi_(2m+1)*x^m.
```

For the campaign's frozen Faber transport,

```text
Phi(x)=(1-s*x)^(-1/2)*Y(x/(1-s*x)).                (1)
```

The proper odd principal parts of pole order at most `q` along
`L=z^2+s` are spanned by

```text
Y_(q,e)=x^e/(1+s*x)^q,  0<=e<q,
```

and (1) sends a basis element exactly to

```text
Phi_(q,e)=x^e*(1-s*x)^(q-e-1/2).                  (2)
```

Fix integers `1<=r<=M`.  If a separately certified source has pole ceiling
`r`, then the terminal-row functional

```text
W_(M,r)=(1-s*x)^(M-r-1/2)
```

annihilates it:

```text
[x^M](W_(M,r)*Phi_(q,e))=0  for every q<=r, e<q.  (3)
```

Indeed the product is the polynomial
`x^e*(1-s*x)^(M-r+q-e-1)` of degree
`M-r+q-1<=M-1`.  This proves (3) for all `M,r`; it is not limited to the
AWS grid `M<=24`.  The cutoff is sharp as a polynomial in `s`: the first
outside class `q=r+1,e=r` has terminal coefficient `(-s)^(M-r)`, and the
terminal class `q=M+1,e=M` has coefficient one.  Substitution of an
arbitrary moving series `p(sigma)` and truncation at any sigma ceiling are
ring homomorphisms and preserve (3).

For row seven (`M=3`) the two campaign vectors are therefore forced:

```text
r=2: [1,-p/4,-p^2/32,-p^3/128],
r=3: [1,+p/4,+3*p^2/32,+5*p^3/128].
```

At `p=0` the pole basis degenerates and the distinguished sharpness
coefficient can specialize to zero when `r<M`; this does not invalidate the
polynomial identity and supplies no `V(p)` emptiness theorem.

## Required use discipline

The functional may be applied only after a complete source pole ceiling and
the placement of every target row have been proved independently.  It does
not itself certify an inventory, a target census, a fan/chart cover, or any
emptiness statement.  In particular it is not by itself a D1 theorem, a
whole-square theorem, order two, maximum twelve, or JC2.
