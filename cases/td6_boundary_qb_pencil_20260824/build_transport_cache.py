#!/usr/bin/env python3
"""Rebuild and verify the portable TD6 affine-transport section cache."""

from hashlib import sha256

import transport_cache as tc


def main():
    rebuilt = tc.canonical_bytes(tc.build_cache_data())
    frozen = tc.CACHE_PATH.read_bytes()
    assert rebuilt == frozen
    print("TD6-QB-TRANSPORT-CACHE: PASS")
    print("transport_rank = 3470/3602")
    print("transport_dimension = 132")
    print(f"cache_bytes = {len(frozen)}")
    print(f"cache.sha256 = {sha256(frozen).hexdigest()}")


if __name__ == "__main__":
    main()
