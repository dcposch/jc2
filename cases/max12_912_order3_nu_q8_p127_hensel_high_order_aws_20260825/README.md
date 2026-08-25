# Q8 moving-v Hensel lift: high-order AWS wrapper

This successor preserves the immutable order-8/16/32/64/128 generator bytes.
The base data needed by the moving-v algorithm are independent of truncation
order. `generate_high.py` therefore invokes the pinned order-128 generator,
then changes exactly the three truncation-order literals after verifying their
unique occurrence. No algebra or coefficient is rewritten.

`run_high_remote.sh` accepts orders 256, 512, and 1024, uses a 64-GiB virtual
memory cap and a four-hour wall cap, and applies the same fail-closed endpoint
checks as the original runner. All execution is AWS-only.

