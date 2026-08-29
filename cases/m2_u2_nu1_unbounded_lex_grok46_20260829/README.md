# U2 nu=1 unbounded-lex packet (Grok 4.6, 2026-08-29)

Self-contained exact `int`/`Fraction` / sparse-polynomial arithmetic.
Stdlib only. No floats, no search caps, no engine import, no network, no CAS.
Cap tokens (`NUCAP`, `MAXNU`, `--cap`) are refused by both executables.

Charged replay:

```sh
cd cases/m2_u2_nu1_unbounded_lex_grok46_20260829
python3    emit_u2.py --output /tmp/u2.json
python3 -O emit_u2.py --output /tmp/u2-O.json && cmp /tmp/u2.json /tmp/u2-O.json
python3    test_u2.py
python3 -O test_u2.py
```
