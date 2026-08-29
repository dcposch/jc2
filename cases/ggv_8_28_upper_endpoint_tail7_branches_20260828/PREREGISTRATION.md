# Preregistration: exact field split of the reduced tail-seven endpoint seed

Date: 2026-08-28

Source: the frozen 41-parameter normalized tail-seven residual, SHA-256
`770ba6d9b312e235e491b4ad948707c41ad4a622b3a17239fdfe62f353606e11`.

Four literal source equations involve only

```text
a=p68,  b=p60,  c=p54:

4+6b-8a+(32/9)a^2=0,
3/2+6c-(3/4)b+4ab-3a+(4/3)a^2=0,
c(-3/4+4a)+b(-9/8+(3/2)a)=0,
c(-9/8+(3/2)a)=0.
```

Over any characteristic-zero field, these equations force exactly

```text
(a,b,c)=(3/4,0,0)  or  (3/2,0,0).
```

Indeed the last equation is `(3/2)c(a-3/4)=0`.  If `a=3/4`, the first and
third equations force `b=c=0`.  Otherwise the last and third force `c=b=0`,
and the first factors as `(32/9)(a-3/4)(a-3/2)`.

Compile both branches independently, substitute the fixed values, and
eliminate every newly affine compatibility pivot over Q.  Each resulting
field-valued branch has

```text
31 operative parameters plus two unconstrained raw reconstruction modes,
143 equations = 116 quadrics + 27 cubics,
303 exact raw-coordinate reconstruction formulas.
```

The authoritative branch bytes are:

```text
a=3/4:
a887e6197293f0b0229ed27f06e40149912d2c4fb7a0f9de1a2c8d69ddec6e4d  BRANCHES/a3_4.json
457726da9ff0949e025a331b8e27349d4c4461374a865c0700d3e0f64b5d90cd  BRANCHES/a3_4_q.sing

a=3/2:
b1bb657096e6e7936f86ab76adadf39a62f85d57c14b592f450689d09f4051a4  BRANCHES/a3_2.json
714117a4562f9e284b2f46f7260774d7819ff6ef171af5776ac9b08008aa6dde  BRANCHES/a3_2_q.sing
```

Before either full branch, solve their identical necessary subsystem on
`p78,...,p85`: 16 quadrics in eight variables, frozen as

```text
3e586cc283526efa9c12f51f5be5535d31eaa1b03ee0296783438acabf9feaab  BRANCHES/shared_block.json
458dce839bce84004be992e146603f05dbce4a1716c5717a4c7ac130e2e1707c  BRANCHES/shared_block_q.sing
```

An exact-Q unit of this shared block kills both field branches and stops the
larger launches immediately.

Run both exact-Q engines independently on audited r6d, one core each, with
64-GiB virtual-memory caps, two-hour engine caps, zero swap, and at least
150 GiB of aggregate post-cap headroom.  The already-running unsplit lane is
independent and remains authoritative as a cross-check.

Positive stop: an exact rational parameter point must reconstruct all 303
raw coordinates and pass the literal branch-P endpoint verifier with
`D0=...=D21=0,D22=1`.  Exact unit stops exclude only the corresponding
normalized tail-seven field branch.  Properness, modular output, timeout,
memory exhaustion, or partial bases prove no point and no broad endpoint
claim.  No row-34, class-tower, `D23`, landing, family, or JC2 inference is
licensed here.
