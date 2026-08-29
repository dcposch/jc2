# Coordinator integration — Sigray Proposition 5.4 and the pole degree pin

Date: 2026-08-28  
Verdict: **PROMOTE WITH SOURCE ERRATA**

## Frozen evidence

```text
f2ee74b5c8f07048488c3b78e5f76bc293beae4b7199614ce75b8e1c18165f75  R1 producer
c3f0bfde24fb265e6ece9fce40089868fd64b01b3f6f5eac3ef0ee5df43e1f30  Opus5 hostile review (REPAIR)
be9e4b747e02ba97a30b8d6254514f568dec8a197dcbbc4a49446ba5fdb38a9e  repaired R2 producer
4c6164b9cf01a797ca6d1029e038f44d7e9f32b34e405c38ec53b2c2f2256bea  R1 checker (1,788 PASS)
4d15680faf3301d9dfc645141c9fbc4a8ee7a4b5f0eb06ea3a74a9baf2ca77ac  R2 checker (943 PASS)
270e3a3c3b879776180057fa02868c8981b12aa37cb674cc3b8965723e1edbfd  R2 custody
```

The root coordinator replayed both checkers successfully.

## Integrated theorem

At a pole vertex `F`, put `p=p_F`, `q=p_(g,F)` and let the normalized type
be `(alpha,beta)`, with `alpha/beta=k_f/k_g` and `alpha>=2`.

The printed proof of Proposition 5.3(iv) misses the genuine algebraic branch
`deg p=1, deg q=0`; the constant bracket alone does not exclude it.  At the
immediate pre-threshold flag `G`, however, the positive-region first tower
relation has exponents `(alpha,beta)`.  Legal common-`K` Statement 3.9
transport along the chosen branch gives

```text
alpha*deg q = beta*deg p.
```

Hence `alpha | deg p`, so `deg p>=alpha>=2`.  Squarefreeness then gives at
least two roots and closes Proposition 5.3(iv).

For `nu_F!=1`, Statement 3.16 writes

```text
p(eta)=eta^epsilon P(eta^nu),  epsilon in {0,1}.
```

The bracket is

```text
alpha*p*q' - beta*p'*q = nonzero constant.
```

Deck-character projectors split `q`.  Every wrong character lies in the
homogeneous kernel `alpha*p*R'-beta*p'*R=0`.  At a simple root of `p`, a
nonzero kernel element of local order `m` would require `alpha*m=beta`,
impossible for coprime `alpha>=2`.  Thus the wrong characters vanish and

```text
p=P(eta^nu)       => q=eta*Q(eta^nu),
p=eta*P(eta^nu)   => q=Q(eta^nu).
```

This proves the omitted `q`-half of Proposition 5.4 and the complete
Statement 5.2(ii) divisibility menu.

## Source-status changes and firewall

- Proposition 5.3(iv): statement true, printed proof incomplete; repaired by
  the pole degree pin above.
- Proposition 5.4: statement true, printed proof omits the entire `q`-half;
  complete repair promoted.
- Statement 5.2(i): its middle ratio is printed backwards.  Correct is
  `D_F/D_(g,F)=alpha/beta`, equivalently
  `D_(g,F)/D_F=beta/alpha`.
- The `alpha=1` abstract bracket admits character mixing exactly on the
  linear branch; it is excluded by normalized type and the degree pin.
- Proposition 5.8, landing, later propagation, realizability of the menu,
  and JC2 remain separate.  No degree ceiling is inferred.
