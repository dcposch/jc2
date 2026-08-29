#!/usr/bin/env python3
"""Exact active-c2 A-adic prefix identities through the deepest D11 class.

This is a light standard-library discovery checker.  It imports the frozen
general-prefix recurrence implementation after pinning its bytes, but derives
the active substitutions and factorizations independently below.
"""

from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "cases/ggv_8_28_upper_endpoint_q1_prefix_d7_d8_target_20260828"
    / "verify_q1_prefix_target.py"
)
SOURCE_SHA256 = "fceb189badafad877c1142b8925480516111790707954d2000421b8190fde119"


def load_source():
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256
    spec = importlib.util.spec_from_file_location("frozen_prefix", SOURCE)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def only_power(item, power):
    return {key: value for key, value in item.items() if key[0] == power}


def main():
    v = load_source()
    F = v.general_prefix(11)
    _, g = v.continuation(F, 11)

    T = v.la_term
    add = v.la_add
    mul = v.la_mul
    scale = v.la_scale
    shift = v.la_shift
    subst = v.la_substitute
    negative = v.la_negative

    s = T(1, 0, "s")
    u = T(1, 0, "u")
    z = T(1, 0, "z")
    r = T(1, 0, "r")
    q = T(1, 0, "q")
    p1 = T(1, 0, "p1")
    c2 = T(1, 0, "c2")
    f4 = T(1, 0, "f4")
    f5 = T(1, 0, "f5")
    f6 = T(1, 0, "f6")

    # Active component after the independently proved D9 repair A | T:
    # V0=A*S and T=A*U.  D8's deepest pole is a square in
    # K=64*F4-Z^2, so field-radical polynomiality first gives A | K.
    active = {"v0": T(1, 1, "s"), "t": T(1, 1, "u")}
    k = add(scale(64, f4), scale(-1, mul(z, z)))
    d8_initial = negative(subst(g[8], active))
    d8_minus_2 = only_power(d8_initial, -2)
    expected_d8_minus_2 = scale(v.Q(3, 32768), shift(-2, mul(k, k)))
    assert d8_minus_2 == expected_d8_minus_2

    # Write K=A*R.  The complete remaining D8 polar part is the c2 cube
    # in H=S^2-2Z.  On the genuine active open c2 != 0 this gives A | H.
    f4_k_lift = add(scale(v.Q(1, 64), mul(z, z)), T(v.Q(1, 64), 1, "r"))
    k_lift = dict(active, f4=f4_k_lift)
    h = add(mul(s, s), scale(-2, z))
    d8_after_k = negative(subst(g[8], k_lift))
    expected_d8_after_k = scale(
        v.Q(-5, 65536), shift(-1, mul(c2, v.la_power(h, 3)))
    )
    assert d8_after_k == expected_d8_after_k

    # On c2 != 0 set H=A*Q, equivalently Z=(S^2-AQ)/2.
    z_h_lift = add(
        scale(v.Q(1, 2), mul(s, s)), T(v.Q(-1, 2), 1, "q")
    )
    d = add(r, scale(-4, mul(s, u)))
    p = add(scale(256, f5), scale(-1, mul(r, s)),
            scale(2, mul(mul(s, s), u)))

    d9 = subst(subst(g[9], k_lift), {"z": z_h_lift})
    expected_d9 = scale(v.Q(3, 65536), shift(-1, mul(d, p)))
    assert negative(d9) == expected_d9

    # D10's deepest class repairs the D9 product: at a field root,
    # D*P=0 and P*(P-2*S*D)=0 imply P=0 in both D=0 and P=0 cases.
    d10 = subst(subst(g[10], k_lift), {"z": z_h_lift})
    d10_minus_2 = only_power(d10, -2)
    expected_d10_minus_2 = scale(
        v.Q(3, 524288),
        shift(-2, mul(p, add(p, scale(-2, mul(s, d))))),
    )
    assert d10_minus_2 == expected_d10_minus_2
    # Hostile scalar controls for the two D9 branches.
    assert v.la_scalar_value(shift(1, expected_d9),
                             {"r": 4, "s": 1, "u": 1,
                              "f5": v.Q(1, 256)}) == 0
    assert v.la_scalar_value(shift(2, expected_d10_minus_2),
                             {"r": 4, "s": 1, "u": 1,
                              "f5": v.Q(1, 256)}) != 0
    assert v.la_scalar_value(shift(1, expected_d9),
                             {"r": 5, "s": 1, "u": 1,
                              "f5": v.Q(3, 256)}) == 0
    assert v.la_scalar_value(shift(2, expected_d10_minus_2),
                             {"r": 5, "s": 1, "u": 1,
                              "f5": v.Q(3, 256)}) == 0

    # Lift the repaired class P=A*P1.  This removes every D9 pole.  The
    # remaining D10 class and deepest D11 class share D=R-4SU as a factor.
    f5_p_lift = add(
        scale(v.Q(1, 256), mul(r, s)),
        scale(v.Q(-1, 128), mul(mul(s, s), u)),
        T(v.Q(1, 256), 1, "p1"),
    )

    def lifted(weight):
        item = subst(g[weight], k_lift)
        item = subst(item, {"z": z_h_lift})
        return subst(item, {"f5": f5_p_lift})

    assert not negative(lifted(9))
    q2 = add(
        scale(2048, f6),
        scale(-2, mul(s, p1)),
        mul(q, add(r, scale(-8, mul(s, u)))),
        scale(-8, mul(u, u)),
    )
    expected_d10_after_p = scale(
        v.Q(1, 524288),
        shift(-1, mul(d, add(scale(20, mul(c2, d)), scale(3, q2)))),
    )
    assert negative(lifted(10)) == expected_d10_after_p

    b11 = add(
        scale(-10, mul(mul(c2, s), d)),
        scale(-3072, mul(f6, s)),
        scale(3, mul(p1, mul(s, s))),
        scale(-3, mul(mul(q, s), add(r, scale(-6, mul(s, u))))),
        scale(-6, mul(u, add(r, scale(-6, mul(s, u))))),
    )
    expected_d11_minus_2 = scale(
        v.Q(1, 1048576), shift(-2, mul(d, b11))
    )
    assert only_power(lifted(11), -2) == expected_d11_minus_2

    # Mutations: each load-bearing structure must be detected.
    assert expected_d8_minus_2 != scale(v.Q(3, 32768), shift(-2, k))
    assert expected_d8_after_k != scale(
        v.Q(-5, 65536), shift(-1, mul(c2, v.la_power(h, 2)))
    )
    assert expected_d9 != scale(v.Q(3, 65536), shift(-1, p))
    assert expected_d10_minus_2 != scale(
        v.Q(3, 524288), shift(-2, mul(p, p))
    )

    print("PASS_EXACT_ACTIVE_C2_D8_D11_PREFIX")
    print("source_sha256=" + SOURCE_SHA256)
    print("D8: A|K; on c2!=0, A|(S^2-2Z)")
    print("D9: A | (R-4SU)*(256F5-RS+2S^2U)")
    print("D9+D10: A | 256F5-RS+2S^2U")
    print("postlift D10 and deepest D11 retain the factor R-4SU")


if __name__ == "__main__":
    main()
