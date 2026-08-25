# Selected-Q8 moving-v Hensel lift, order 32

This custody package freezes the completed AWS Box03 order-32 moving-v
coefficient lift. The source hashes are pinned in `run.meta`; the lightweight
verifier checks hashes and every fail-closed endpoint without invoking CAS.

```sh
python3 cases/max12_912_order3_nu_q8_p127_hensel_order32_aws_20260825/verify.py
```

Scope: formal-local over `F_127` modulo `(w-25)^32`; no rational/global or
characteristic-zero conclusion.

