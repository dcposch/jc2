#!/usr/bin/env python3
"""Assert-free exact tests for td8_equal_join_prop81iv_r1."""

from fractions import Fraction

from td8_equal_join_prop81iv_r1 import (
    certificate,
    fixed_route_certificates,
    identity_residual,
    patterns,
    two_orbit_residual,
)


passed = 0


def chk(name: str, condition: bool) -> None:
    global passed
    if not condition:
        raise SystemExit("CHECK_FAILED:" + name)
    passed += 1


# A finite scan is regression only; the source identity is algebraic in nu.
for t in list(range(0, 1001)) + [10_000, 10**6]:
    c = certificate(t)
    nu = 4 + 3 * t
    chk("nu", c["nu"] == nu)
    chk("identity", c["checks"]["prop81iv"] is True)
    chk("gcd", c["degrees"]["M"] == 3)
    chk("rhs", c["rhs_constant"] == 4 * nu)
    chk("firewall", c["claim_firewall"]["geometric_realizability"] is False)

# Direct sparse-polynomial controls.
p, q = patterns(4)
chk("p-shape", p == {0: Fraction(1), 8: Fraction(3),
                      16: Fraction(3), 24: Fraction(1)})
chk("q-shape", q == {1: Fraction(1), 9: Fraction(1)})

# Hostile mutations: each must leave a nonzero residual or refuse the input.
chk("mut-one-minus-u", identity_residual(4, one_minus_u=7) != {})
chk("mut-delta", identity_residual(4, delta=17) != {})
fixed = fixed_route_certificates()
chk("incoming-consumer", fixed["each_incoming_21_15"]["identity_ok"] is True)
chk("trunk-consumer", fixed["trunk_85_35"]["identity_ok"] is True)
chk("mut-incoming-root-ratio", two_orbit_residual(
    7, 2, 4, 2, 1, 7, 5, 56) != {})
chk("mut-trunk-root-ratio", two_orbit_residual(
    17, 3, 5, 3, 2, 17, 7, 255) != {})
for bad_nu in [2, 3, 5, 6, 8]:
    refused = False
    try:
        identity_residual(bad_nu)
    except ValueError:
        refused = True
    chk("off-residue-refused", refused)
for bad_t in [-1, True, Fraction(1, 2)]:
    refused = False
    try:
        certificate(bad_t)  # type: ignore[arg-type]
    except ValueError:
        refused = True
    chk("bad-t-refused", refused)

print(f"TD8_EQUAL_JOIN_PROP81IV_R1_TEST_PASS checks={passed}")
