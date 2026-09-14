#!/usr/bin/env python3
"""Integer audit of the K=7 degree band quoted by the frozen tower report."""


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


K = 7
smin = ceil_div(2 * (K - 1), 3)
b_from_total = ceil_div(2 * K + 1, 3)
b_from_y = smin + 1
b_min = max(b_from_total, b_from_y)
b_max = 2 * K - 1
residual = list(range(b_min, b_max + 1))
floor_killed = [b for b in range(1, b_max + 1) if 3 * b <= 2 * K]
banked = {5}
proposed_closed = set(range(9, 14))
open_degrees = [b for b in residual if b not in banked | proposed_closed]

print(f"K={K}")
print(f"smin={smin}")
print(f"b_from_total={b_from_total}")
print(f"b_from_y={b_from_y}")
print(f"b_min={b_min}")
print(f"b_max={b_max}")
print(f"residual={residual}")
print(f"floor_killed_positive={floor_killed}")
print("composite_only=[0]")
print(f"banked={sorted(banked)}")
print(f"proposed_closed={sorted(proposed_closed)}")
print(f"open={open_degrees}")

assert (smin, b_min, b_max) == (4, 5, 13)
assert floor_killed == [1, 2, 3, 4]
assert open_degrees == [6, 7, 8]
